#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_catalog.py - scan ``mods/`` and (re)generate ``catalog/mods.json``.

The catalog is the single machine-readable source of truth consumed by the
README generator, the release bundler and the CI validator.

    python scripts/build_catalog.py
"""

from __future__ import annotations

import argparse
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tc4lib  # noqa: E402


def build(repo_root: str = ".", release_tag: str = "latest") -> dict:
    records = tc4lib.scan_dir(repo_root)
    for rec in records:
        rec["download_url"] = tc4lib.download_url(rec["file_name"], release_tag)

    counts: dict = {}
    for rec in records:
        key = "%s/%s" % (rec["mc_version"], rec["channel"])
        counts[key] = counts.get(key, 0) + 1

    mc_versions = sorted({r["mc_version"] for r in records})
    return {
        "repo": tc4lib.REPO,
        "generated_at": datetime.datetime.now(datetime.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "release_tag": release_tag,
        "mc_versions": mc_versions,
        "counts": counts,
        "total": len(records),
        "mods": records,
    }


def write_catalog(repo_root: str, data: dict) -> str:
    path = os.path.join(repo_root, tc4lib.CATALOG_FILE)
    tc4lib.save_json(path, data)
    return path


def write_checksums(repo_root: str, data: dict) -> str:
    path = os.path.join(repo_root, tc4lib.CATALOG_DIR, "SHA256SUMS")
    lines = ["%s  %s" % (r["sha256"], r["file"]) for r in data["mods"]]
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    return path


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build catalog/mods.json from mods/.")
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--release-tag", default=os.environ.get("RELEASE_TAG", "latest"))
    args = parser.parse_args(argv)

    repo_root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data = build(repo_root, args.release_tag)
    cat = write_catalog(repo_root, data)
    sums = write_checksums(repo_root, data)
    print("wrote %s (%d mods)" % (os.path.relpath(cat, repo_root), data["total"]))
    print("wrote %s" % os.path.relpath(sums, repo_root))
    for key in sorted(data["counts"]):
        print("  %-22s %d" % (key, data["counts"][key]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
