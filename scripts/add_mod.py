#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""add_mod.py - one command for contributors to add their addon the right way.

Reads the jar metadata, drops the file into the correct ``mods/<mcversion>/``
folder, normalises the file name, then regenerates the catalog and README.

    python scripts/add_mod.py MyAddon-1.2.0.jar
    python scripts/add_mod.py MyAddon.jar --experimental
    python scripts/add_mod.py MyAddon.jar --dry-run

After it succeeds, commit the new jar plus ``catalog/`` and ``README.md`` and
open a pull request (see docs/CONTRIBUTING.md).
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tc4lib  # noqa: E402

_HINT_RE = re.compile(r"^\(\d+[-+]\)")


def canonical_name(record: dict) -> str:
    """Return a safe, descriptive, ASCII-only file name for the record."""
    mod_id = re.sub(r"[^0-9A-Za-z._-]", "-", record["mod_id"] or "mod")
    mc = record["mc_version"] or "unknown"
    ver = re.sub(r"[^0-9A-Za-z._-]", "-", record["mod_version"] or "0")
    name = "%s-%s-%s.jar" % (mod_id, mc, ver)
    return name


def target_dir(repo_root: str, record: dict, experimental: bool) -> str:
    rel = os.path.join(tc4lib.MODS_DIR)
    if experimental:
        rel = os.path.join(rel, "experimental")
    rel = os.path.join(rel, record["mc_version"])
    return os.path.join(repo_root, rel)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Add an addon jar to the repository.")
    parser.add_argument("jar", help="path to the .jar file")
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--experimental", action="store_true", help="place under mods/experimental/")
    parser.add_argument("--keep-name", action="store_true", help="keep the original file name")
    parser.add_argument("--dry-run", action="store_true", help="show what would happen")
    args = parser.parse_args(argv)

    repo_root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    jar = args.jar
    if not os.path.isfile(jar):
        print("no such file: %s" % jar, file=sys.stderr)
        return 2

    record = tc4lib.scan_mod(jar, repo_root)
    src_name = os.path.basename(jar)
    if args.keep_name:
        new_name = _HINT_RE.sub("", src_name)
    else:
        new_name = canonical_name(record)
    dest_dir = target_dir(repo_root, record, args.experimental)
    dest = os.path.join(dest_dir, new_name)

    print("modId        : %s (%s)" % (record["mod_id"], record["mod_name"]))
    print("mod version  : %s" % record["mod_version"])
    print("minecraft    : %s (%s)" % (record["mc_version"], record["loader"]))
    print("TC4R 要求    : %s" % tc4lib.tc4_requirement(record))
    print("sha256       : %s" % record["sha256"])
    print("目标位置     : %s" % os.path.relpath(dest, repo_root))

    if os.path.exists(dest):
        print("错误: 目标文件已存在，若为更新请先删除旧文件。", file=sys.stderr)
        return 3

    if args.dry_run:
        print("(dry-run, 未写入)")
        return 0

    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(jar, dest)
    print("已复制 jar。")

    import build_catalog
    import gen_readme

    data = build_catalog.build(repo_root)
    build_catalog.write_catalog(repo_root, data)
    build_catalog.write_checksums(repo_root, data)
    gen_readme.main(["--repo-root", repo_root])
    print("\n完成。请提交以下内容并开 PR:")
    print("  %s" % os.path.relpath(dest, repo_root))
    print("  %s" % tc4lib.CATALOG_FILE)
    print("  catalog/SHA256SUMS")
    print("  README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
