#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tc4lib - read Thaumcraft 4R addon metadata and TC4R dependency versions.

This module is the shared work-horse for every script in ``scripts/``:

* :func:`read_jar_metadata` opens a mod jar and extracts loader, mod id,
  version, authors, description and the full dependency list.
* :func:`parse_tc4_range` turns a ``thaumcraft`` version range such as
  ``[4.2.3.5-1.20.1-port.0.1.0-20738,)`` into structured data
  (``base`` / ``mc`` / ``port`` / ``build``).
* :func:`scan_mod` produces the canonical JSON record used by the catalog,
  README generator, release bundler and the CI validator.

The library works on the *compiled* metadata inside a jar
(``META-INF/mods.toml``, ``META-INF/neoforge.mods.toml`` or
``fabric.mod.json``).  ``tomllib`` is used when available; a small, tolerant
fallback parser covers Python < 3.11 so the scripts run everywhere.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import zipfile
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

try:  # Python 3.11+
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - fallback for 3.8-3.10
    tomllib = None  # type: ignore

# --------------------------------------------------------------------------- #
# Repository constants
# --------------------------------------------------------------------------- #
REPO = "thaumcraft-port/thaumcraft-addons"
REPO_URL = "https://github.com/%s" % REPO
RELEASES_URL = "%s/releases" % REPO_URL
LATEST_DOWNLOAD = "%s/latest/download" % RELEASES_URL
MODS_DIR = "mods"
CATALOG_DIR = "catalog"
CATALOG_FILE = os.path.join(CATALOG_DIR, "mods.json")
DOCS_DIR = "docs"

# Core Thaumcraft mod ids (add extras as ports appear).
THAUMCRAFT_MODIDS = ("thaumcraft",)
TINKERER_MODIDS = ("thaumictinkerer", "thaumic_tinkerer", "thaumictinkerer")

# loader -> candidate metadata paths inside the jar (first hit wins).
_META_CANDIDATES = (
    ("neoforge", ("META-INF/neoforge.mods.toml",)),
    ("forge", ("META-INF/mods.toml",)),
    ("fabric", ("fabric.mod.json",)),
)

# ``4.2.3.5-1.20.1-port.0.1.0-20738`` -> base / mc / loader / port / build
_TC4_VER_RE = re.compile(
    r"^(?P<base>\d+(?:\.\d+)*)"
    r"(?:-(?P<mc>\d+\.\d+(?:\.\d+)?)"
    r"-(?P<loader>port|forge|neoforge|fabric)"
    r"\.(?P<port>[0-9A-Za-z][0-9A-Za-z.\-]*?)"
    r"-(?P<build>\d+))?$"
)
_BASE_RE = re.compile(r"^(?P<base>\d+(?:\.\d+)*)")
# filename hint, e.g. ``(20737-)mod.jar`` / ``(20738+)mod.jar``
_HINT_RE = re.compile(r"^\((?P<build>\d+)(?P<op>[-+])\)")


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
def sha256_of(path: str, chunk: int = 1 << 20) -> str:
    """Return the SHA-256 digest of *path* as a lowercase hex string."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def _as_text(value: Any) -> str:
    """Normalise authors (str | list) and strip whitespace."""
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v).strip() for v in value if str(v).strip())
    return str(value).strip()


def _first_bound(version_range: str) -> str:
    """Return the lower bound token of a Maven-style version range."""
    rng = (version_range or "").strip()
    if rng in ("", "*"):
        return ""
    inner = rng.strip()
    if inner[0] in "[(" and inner[-1] in "])":
        inner = inner[1:-1]
    return inner.split(",")[0].strip()


def parse_tc4_range(version_range: str) -> Dict[str, Any]:
    """Parse a ``thaumcraft`` version range into structured fields.

    Returns a dict with ``raw``, ``lower``, ``base``, ``mc``, ``port`` and
    ``build`` (int or ``None``).  ``build`` is the TC4R port build number that
    tells users *which* core build the addon needs.
    """
    raw = (version_range or "").strip()
    lower = _first_bound(raw)
    out: Dict[str, Any] = {
        "raw": raw,
        "lower": lower,
        "base": None,
        "mc": None,
        "port": None,
        "build": None,
    }
    if not lower:
        return out
    m = _TC4_VER_RE.match(lower)
    if m:
        out["base"] = m.group("base")
        out["mc"] = m.group("mc")
        out["port"] = m.group("port")
        if m.group("build"):
            out["build"] = int(m.group("build"))
        return out
    m2 = _BASE_RE.match(lower)
    if m2:
        out["base"] = m2.group("base")
    return out


def tc4_label(info: Dict[str, Any]) -> str:
    """Human friendly one-liner for a parsed TC4 range."""
    base = info.get("base") or "?"
    build = info.get("build")
    port = info.get("port")
    parts = ["TC4R %s" % base]
    if port:
        parts.append("port %s" % port)
    parts.append("build %s" % build if build else "build 任意")
    return " / ".join(parts)


def parse_filename_hint(name: str) -> Optional[Dict[str, Any]]:
    """Extract the legacy ``(20738+)`` / ``(20737-)`` TC4 build hint."""
    m = _HINT_RE.match(name)
    if not m:
        return None
    return {"build": int(m.group("build")), "op": m.group("op")}


# --------------------------------------------------------------------------- #
# TOML / JSON metadata parsing
# --------------------------------------------------------------------------- #
def _strip_comment(line: str) -> str:
    """Remove a trailing ``#`` comment while respecting quoted strings."""
    in_s = None
    for i, ch in enumerate(line):
        if in_s:
            if ch == in_s:
                in_s = None
        elif ch in "\"'":
            in_s = ch
        elif ch == "#":
            return line[:i]
    return line


def _fallback_toml(text: str) -> Dict[str, Any]:
    """Minimal, tolerant parser for ``*.mods.toml`` when tomllib is absent.

    Handles the subset FML actually emits: comments (including trailing
    comments after ``[[table]]`` headers), literal ``'''`` multiline strings,
    quoted strings, booleans, numbers and simple inline arrays.
    """
    root: Dict[str, Any] = {}
    current: Optional[Dict[str, Any]] = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        line = _strip_comment(raw).strip()
        if not line:
            continue
        if line.startswith("[[") and line.endswith("]]"):
            path = line[2:-2].strip()
            node: Any = root
            parts = path.split(".")
            for p in parts[:-1]:
                node = node.setdefault(p, {})
                if isinstance(node, list) and node:
                    node = node[-1]
            last = parts[-1]
            current = {}
            node.setdefault(last, [])
            if isinstance(node[last], list):
                node[last].append(current)
            continue
        if line.startswith("[") and line.endswith("]"):
            # single (non-array) table -> ignore its keys
            current = {}
            continue
        if "=" not in line:
            continue
        key, _, val = raw.partition("=")
        key = key.strip()
        val = val.strip()
        # keys before any header belong to the document root
        target = current if current is not None else root
        if val.startswith("'''") or val.startswith('"""'):
            quote = val[:3]
            body = val[3:]
            while quote not in body:
                if i >= len(lines):
                    break
                body += "\n" + lines[i]
                i += 1
            body = body.split(quote, 1)[0]
            target[key] = body
            continue
        if val.startswith('"'):
            end = 1
            while end < len(val) and (val[end] != '"' or val[end - 1] == "\\"):
                end += 1
            target[key] = val[1:end]
            continue
        val = _strip_comment(val).strip()
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
            target[key] = items
        elif val.lower() in ("true", "false"):
            target[key] = val.lower() == "true"
        else:
            target[key] = val
    return root


def _parse_toml(text: str) -> Dict[str, Any]:
    if tomllib is not None:
        try:
            return tomllib.loads(text)
        except Exception:
            pass
    return _fallback_toml(text)


def _normalise_toml(data: Dict[str, Any], loader: str) -> Dict[str, Any]:
    """Extract the fields we care about from a parsed mods.toml."""
    mods = data.get("mods") or []
    mod = mods[0] if mods else {}
    deps: List[Dict[str, Any]] = []
    raw_deps = data.get("dependencies") or {}
    for owner, entries in raw_deps.items():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            dep_type = entry.get("type")
            mandatory = entry.get("mandatory")
            if dep_type is not None:
                required = str(dep_type).lower() in ("required",)
                dtype = str(dep_type).lower()
            else:
                required = bool(mandatory)
                dtype = "required" if required else "optional"
            deps.append(
                {
                    "owner": owner,
                    "mod_id": entry.get("modId", ""),
                    "version_range": entry.get("versionRange", ""),
                    "mandatory": required,
                    "type": dtype,
                    "side": entry.get("side", "BOTH"),
                    "ordering": entry.get("ordering", "NONE"),
                }
            )
    return {
        "loader": loader,
        "mod_id": mod.get("modId", ""),
        "mod_name": mod.get("displayName") or mod.get("modId", ""),
        "mod_version": str(mod.get("version", "")),
        "authors": _as_text(mod.get("authors")),
        "description": (mod.get("description") or "").strip(),
        "license": data.get("license", ""),
        "loader_version": data.get("loaderVersion", ""),
        "dependencies": deps,
    }


def _normalise_fabric(data: Dict[str, Any]) -> Dict[str, Any]:
    deps: List[Dict[str, Any]] = []
    for mod_id, rng in (data.get("depends") or {}).items():
        deps.append(
            {
                "owner": None,
                "mod_id": mod_id,
                "version_range": rng if isinstance(rng, str) else "*",
                "mandatory": True,
                "type": "required",
                "side": "BOTH",
                "ordering": "NONE",
            }
        )
    for mod_id, rng in (data.get("recommends") or {}).items():
        deps.append(
            {
                "owner": None,
                "mod_id": mod_id,
                "version_range": rng if isinstance(rng, str) else "*",
                "mandatory": False,
                "type": "optional",
                "side": "BOTH",
                "ordering": "NONE",
            }
        )
    return {
        "loader": "fabric",
        "mod_id": data.get("id", ""),
        "mod_name": data.get("name") or data.get("id", ""),
        "mod_version": str(data.get("version", "")),
        "authors": _as_text(data.get("authors")),
        "description": (data.get("description") or "").strip(),
        "license": data.get("license", ""),
        "loader_version": "",
        "dependencies": deps,
    }


def read_jar_metadata(path: str) -> Dict[str, Any]:
    """Read loader metadata from a jar and return a normalised dict."""
    with zipfile.ZipFile(path) as zf:
        names = set(zf.namelist())
        for loader, candidates in _META_CANDIDATES:
            for cand in candidates:
                if cand not in names:
                    continue
                with zf.open(cand) as fh:
                    text = fh.read().decode("utf-8", "replace")
                if cand.endswith(".json"):
                    meta = _normalise_fabric(json.loads(text))
                else:
                    meta = _normalise_toml(_parse_toml(text), loader)
                meta["meta_path"] = cand
                return meta
    raise ValueError("no recognised loader metadata found")


# --------------------------------------------------------------------------- #
# Canonical record
# --------------------------------------------------------------------------- #
def scan_mod(path: str, repo_root: str = ".", channel: Optional[str] = None) -> Dict[str, Any]:
    """Scan one jar and return the canonical catalog record."""
    rel = os.path.relpath(path, repo_root).replace("\\", "/")
    rel_dir = os.path.dirname(rel)
    parts = rel_dir.split("/")
    if channel is None:
        channel = "experimental" if "experimental" in parts else "stable"

    meta = read_jar_metadata(path)
    deps: List[Dict[str, Any]] = meta.get("dependencies", [])

    # MC version: dependency on minecraft, else derive from folder / version.
    mc = ""
    for dep in deps:
        if dep["mod_id"] == "minecraft":
            b = _first_bound(dep["version_range"])
            m = re.match(r"^(\d+\.\d+(?:\.\d+)?)", b)
            if m:
                mc = m.group(1)
            break
    if not mc:
        for seg in reversed(parts):
            if re.match(r"^\d+\.\d+(\.\d+)?$", seg):
                mc = seg
                break

    # TC4R core dependency.
    tc4: Dict[str, Any] = {}
    tinkerer: Optional[Dict[str, Any]] = None
    for dep in deps:
        mid = dep["mod_id"].lower()
        if mid in THAUMCRAFT_MODIDS and not tc4:
            tc4 = parse_tc4_range(dep["version_range"])
            tc4["mandatory"] = dep["mandatory"]
        elif mid in TINKERER_MODIDS and tinkerer is None:
            tinkerer = parse_tc4_range(dep["version_range"])

    record: Dict[str, Any] = {
        "file": rel,
        "file_name": os.path.basename(path),
        "size": os.path.getsize(path),
        "sha256": sha256_of(path),
        "channel": channel,
        "mc_version": mc or "unknown",
        "loader": meta["loader"],
        "mod_id": meta["mod_id"],
        "mod_name": meta["mod_name"],
        "mod_version": meta["mod_version"],
        "authors": meta["authors"],
        "license": meta["license"],
        "description": meta["description"],
        "tc4": tc4,
        "thaumic_tinkerer": tinkerer,
        "dependencies": deps,
        "filename_hint": parse_filename_hint(os.path.basename(path)),
    }
    return record


def scan_dir(repo_root: str = ".") -> List[Dict[str, Any]]:
    """Scan every jar under ``<repo_root>/mods`` and return sorted records."""
    mods_root = os.path.join(repo_root, MODS_DIR)
    records: List[Dict[str, Any]] = []
    for dirpath, _dirnames, filenames in os.walk(mods_root):
        for fn in sorted(filenames):
            if fn.lower().endswith(".jar"):
                records.append(scan_mod(os.path.join(dirpath, fn), repo_root))
    records.sort(key=lambda r: (r["mc_version"], r["channel"], r["mod_id"]))
    return records


def download_url(file_name: str, tag: str = "latest") -> str:
    """Release asset download URL for *file_name*."""
    if tag == "latest":
        return "%s/%s" % (LATEST_DOWNLOAD, file_name)
    return "%s/download/%s/%s" % (RELEASES_URL, tag, file_name)


def load_catalog(repo_root: str = ".") -> Dict[str, Any]:
    path = os.path.join(repo_root, CATALOG_FILE)
    if not os.path.exists(path):
        return {"mods": []}
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: str, data: Any) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def tc4_requirement(record: Dict[str, Any]) -> str:
    """Short human string describing the required TC4R core build."""
    tc4 = record.get("tc4") or {}
    base = tc4.get("base")
    build = tc4.get("build")
    if not base and build is None:
        raw = tc4.get("raw") or ""
        return raw if raw else "未声明"
    if build is None:
        return "≥ %s" % base
    return "≥ %s (build %s)" % (base, build)


_LOADER_DISPLAY = {"forge": "Forge", "neoforge": "NeoForge", "fabric": "Fabric"}


def loader_display(loader: str) -> str:
    return _LOADER_DISPLAY.get((loader or "").lower(), (loader or "").capitalize())


def md_escape(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def md_table(headers: List[str], rows: List[List[str]]) -> str:
    """Render a GitHub-flavoured markdown table."""
    out = ["| " + " | ".join(headers) + " |"]
    out.append("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        out.append("| " + " | ".join(md_escape(str(c)) for c in row) + " |")
    return "\n".join(out)


def human_size(num: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if num < 1024 or unit == "GB":
            return "%.1f %s" % (num, unit) if unit != "B" else "%d B" % num
        num /= 1024.0
    return "%d B" % num
