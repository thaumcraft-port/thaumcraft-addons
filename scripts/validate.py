#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate.py - CI gate for the addon repository.

Checks every jar under ``mods/`` for:

* readable loader metadata (mods.toml / neoforge.mods.toml / fabric.mod.json);
* a folder layout of ``mods/<mc>/`` or ``mods/experimental/<mc>/`` that
  matches the Minecraft version declared inside the jar;
* a declared ``thaumcraft`` dependency;
* no duplicate ``(modId, mc, modVersion)``;
* clean file names (ASCII only, no legacy ``(20738+)`` prefix);
* optionally, that ``catalog/mods.json`` and ``README.md`` are up to date.

Exit code is non-zero when any error is found.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tc4lib  # noqa: E402

_ASCII_RE = re.compile(r"^[\x20-\x7E]+$")
_HINT_RE = re.compile(r"^\(\d+[-+]\)")
_FOLDER_MC_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")


def validate(repo_root: str) -> tuple:
    errors = []
    warnings = []
    records = []

    mods_root = os.path.join(repo_root, tc4lib.MODS_DIR)
    if not os.path.isdir(mods_root):
        errors.append("missing %s/ directory" % tc4lib.MODS_DIR)
        return records, errors, warnings

    seen = {}
    for dirpath, _dirnames, filenames in os.walk(mods_root):
        rel_dir = os.path.relpath(dirpath, repo_root).replace("\\", "/")
        parts = rel_dir.split("/")[1:]  # drop leading 'mods'
        has_jar = any(f.lower().endswith(".jar") for f in filenames)
        folder_mc = parts[-1] if parts and _FOLDER_MC_RE.match(parts[-1]) else None
        if has_jar and folder_mc is None:
            errors.append("%s: file must live in mods/<mcversion>/ (or mods/experimental/<mcversion>)" % rel_dir)
        elif has_jar and parts and parts[0] not in ("experimental",) and len(parts) != 1:
            warnings.append("%s: unexpected nesting" % rel_dir)

        for fn in sorted(filenames):
            if not fn.lower().endswith(".jar"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, repo_root).replace("\\", "/")

            if _HINT_RE.match(fn):
                errors.append("%s: strip the legacy '(build)' prefix from the file name" % rel)
            if not _ASCII_RE.match(fn):
                errors.append("%s: file name must be ASCII only" % rel)

            try:
                rec = tc4lib.scan_mod(path, repo_root)
            except Exception as exc:  # noqa: BLE001
                errors.append("%s: cannot read loader metadata (%s)" % (rel, exc))
                continue

            records.append(rec)

            if folder_mc and rec["mc_version"] != folder_mc:
                errors.append(
                    "%s: folder says MC %s but jar declares MC %s" % (rel, folder_mc, rec["mc_version"])
                )
            if not rec["tc4"] or not (rec["tc4"].get("raw")):
                errors.append("%s: no 'thaumcraft' dependency declared" % rel)
            if not rec["mod_id"]:
                errors.append("%s: modId is empty" % rel)

            key = (rec["mod_id"], rec["mc_version"], rec["mod_version"])
            if key in seen:
                errors.append("%s: duplicate of %s (%s)" % (rel, seen[key], "/".join(key)))
            else:
                seen[key] = rel

    return records, errors, warnings


def check_generated(repo_root: str) -> list:
    from build_catalog import build  # local import

    problems = []
    fresh = build(repo_root)
    current = tc4lib.load_catalog(repo_root)
    # compare ignoring volatile timestamp
    fresh_cmp = dict(fresh)
    cur_cmp = dict(current)
    fresh_cmp.pop("generated_at", None)
    cur_cmp.pop("generated_at", None)
    if fresh_cmp != cur_cmp:
        problems.append("catalog/mods.json is out of date; run 'python scripts/build_catalog.py'")

    import gen_readme

    if gen_readme.main(["--repo-root", repo_root, "--check"]) != 0:
        problems.append("README.md is out of date; run 'python scripts/gen_readme.py'")
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate the addon repository.")
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--check-generated", action="store_true", help="also verify catalog/README freshness")
    args = parser.parse_args(argv)

    repo_root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    records, errors, warnings = validate(repo_root)

    if args.check_generated:
        errors.extend(check_generated(repo_root))

    print("scanned %d jar(s)" % len(records))
    for rec in records:
        print("  [%s] %-22s %-10s %-9s %s" % (
            "exp" if rec["channel"] == "experimental" else "ok ",
            rec["mod_id"],
            rec["mc_version"],
            rec["loader"],
            tc4lib.tc4_requirement(rec),
        ))
    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)

    if errors:
        print("\nFAILED with %d error(s)" % len(errors))
        return 1
    print("\nOK - %d mod(s) validated" % len(records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
