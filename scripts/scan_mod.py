#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scan_mod.py - quickly read the TC4R version an addon jar depends on.

Examples
--------
    python scripts/scan_mod.py mods/1.20.1/technom-1.20.1-0.1.0-dev.jar
    python scripts/scan_mod.py mods/1.20.1/technom-1.20.1-0.1.0-dev.jar --json
    python scripts/scan_mod.py --all
    python scripts/scan_mod.py --all --mc 1.21.1
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tc4lib  # noqa: E402


def _print_record(rec: dict, repo_root: str) -> None:
    tc4 = rec.get("tc4") or {}
    print("文件           : %s" % rec["file"])
    print("模组           : %s  (modId=%s)" % (rec["mod_name"], rec["mod_id"]))
    print("模组版本       : %s" % rec["mod_version"])
    print("Minecraft      : %s   (加载器 %s, 通道 %s)" % (rec["mc_version"], rec["loader"], rec["channel"]))
    print("作者           : %s" % (rec.get("authors") or "-"))
    print("许可           : %s" % (rec.get("license") or "-"))
    print("依赖 TC4R      : %s" % (tc4.get("raw") or "未声明"))
    print("  -> 基线版本   : %s" % (tc4.get("base") or "?"))
    print("  -> 平台       : %s/%s" % (tc4.get("mc") or rec["mc_version"], rec.get("loader") or rec["loader"]))
    print("  -> 最低构建号 : %s" % (tc4.get("build") if tc4.get("build") is not None else "任意"))
    print("  -> 人类可读   : %s" % tc4lib.tc4_requirement(rec))
    tt = rec.get("thaumic_tinkerer")
    if tt and (tt.get("raw") or tt.get("base")):
        print("依赖神秘工匠   : %s" % (tt.get("raw") or tc4lib.tc4_requirement({"tc4": tt})))
    hint = rec.get("filename_hint")
    if hint:
        print("文件名提示     : TC4 build %s%s" % (hint["build"], hint["op"]))
    print("SHA-256        : %s" % rec["sha256"])
    print("下载链接       : %s" % tc4lib.download_url(rec["file_name"]))
    core = [d for d in rec.get("dependencies", []) if d["mod_id"] not in ("minecraft",)]
    mandatory = [d["mod_id"] for d in core if d["mandatory"]]
    optional = [d["mod_id"] for d in core if not d["mandatory"]]
    print("必需依赖       : %s" % (", ".join(mandatory) or "-"))
    print("可选依赖       : %s" % (", ".join(optional) or "-"))
    if rec.get("description"):
        print("简介           : %s" % rec["description"])


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Read the TC4R dependency of an addon jar.")
    parser.add_argument("path", nargs="?", help="jar path or directory (default: mods/)")
    parser.add_argument("--all", action="store_true", help="scan every jar under mods/")
    parser.add_argument("--mc", help="only show mods for this Minecraft version")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of text")
    parser.add_argument("--repo-root", default=None, help="repository root (default: autodetect)")
    args = parser.parse_args(argv)

    repo_root = args.repo_root
    if repo_root is None:
        candidate = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        repo_root = candidate if os.path.isdir(os.path.join(candidate, tc4lib.MODS_DIR)) else "."

    records = []
    if args.all or not args.path:
        records = tc4lib.scan_dir(repo_root)
    else:
        target = args.path
        if os.path.isdir(target):
            for dirpath, _d, files in os.walk(target):
                for fn in sorted(files):
                    if fn.lower().endswith(".jar"):
                        records.append(tc4lib.scan_mod(os.path.join(dirpath, fn), repo_root))
        else:
            records.append(tc4lib.scan_mod(target, repo_root))

    if args.mc:
        records = [r for r in records if r["mc_version"] == args.mc]

    if args.json:
        print(json.dumps(records if len(records) != 1 else records[0], ensure_ascii=False, indent=2))
        return 0

    if not records:
        print("no jars found", file=sys.stderr)
        return 1

    for i, rec in enumerate(records):
        if i:
            print("-" * 60)
        _print_record(rec, repo_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
