#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""release_bundle.py - build release assets under ``dist/``.

Produces, for every Minecraft version present:

* ``dist/thaumcraft-addons-<mc>-<version>.zip``  - all jars for that MC version
* ``dist/<original-file-name>.jar``              - flat copy for direct download
* ``dist/SHA256SUMS``                            - checksums of every asset
* ``dist/release_notes.md``                      - markdown release body

    python scripts/release_bundle.py --version 2026.10.14
"""

from __future__ import annotations

import argparse
import datetime
import os
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_catalog  # noqa: E402
import tc4lib  # noqa: E402


def build_zips(repo_root: str, data: dict, version: str) -> list:
    dist = os.path.join(repo_root, "dist")
    os.makedirs(dist, exist_ok=True)
    created = []
    for mc in data["mc_versions"]:
        mods = [r for r in data["mods"] if r["mc_version"] == mc]
        zname = "thaumcraft-addons-%s-%s.zip" % (mc, version)
        zpath = os.path.join(dist, zname)
        with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
            for r in mods:
                src = os.path.join(repo_root, r["file"])
                arc = "%s-MC%s/%s" % (r["mod_id"], mc, r["file_name"])
                zf.write(src, arc)
        created.append(zpath)
        # flat copy for direct download links
        for r in mods:
            src = os.path.join(repo_root, r["file"])
            dst = os.path.join(dist, r["file_name"])
            with open(src, "rb") as fh_in, open(dst, "wb") as fh_out:
                fh_out.write(fh_in.read())
            created.append(dst)
    return created


def write_sums(dist: str) -> str:
    path = os.path.join(dist, "SHA256SUMS")
    names = sorted(
        f for f in os.listdir(dist) if f != "SHA256SUMS" and os.path.isfile(os.path.join(dist, f))
    )
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        for name in names:
            fh.write("%s  %s\n" % (tc4lib.sha256_of(os.path.join(dist, name)), name))
    return path


def render_notes(data: dict, version: str, tag: str) -> str:
    lines = ["# Thaumcraft 4R Addons - %s" % version, ""]
    lines.append("本版本共收录 **%d** 个附属模组，覆盖 Minecraft %s。" % (data["total"], "、".join(data["mc_versions"])))
    lines.append("")
    for mc in data["mc_versions"]:
        lines.append("## Minecraft %s" % mc)
        lines.append("")
        bundle = "thaumcraft-addons-%s-%s.zip" % (mc, version)
        lines.append("**整包下载**: [%s](%s)" % (bundle, tc4lib.download_url(bundle, tag)))
        lines.append("")
        rows = []
        for r in sorted([m for m in data["mods"] if m["mc_version"] == mc], key=lambda x: x["mod_name"].lower()):
            rows.append(
                [
                    r["mod_name"],
                    "`%s` %s" % (r["mod_version"], r["loader"]),
                    tc4lib.tc4_requirement(r),
                    "[%s](%s)" % (r["file_name"], tc4lib.download_url(r["file_name"], tag)),
                ]
            )
        lines.append(tc4lib.md_table(["模组", "版本", "TC4R 要求", "下载"], rows))
        lines.append("")
    lines.append("> 版本仅供参考，请遵循各模组原作者的开源许可。")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build release assets into dist/.")
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--version", default=os.environ.get("RELEASE_VERSION") or
                        datetime.date.today().strftime("%Y.%m.%d"))
    parser.add_argument("--tag", default=os.environ.get("RELEASE_TAG", "latest"))
    args = parser.parse_args(argv)

    repo_root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data = build_catalog.build(repo_root, args.tag)
    build_catalog.write_catalog(repo_root, data)

    assets = build_zips(repo_root, data, args.version)
    sums = write_sums(os.path.join(repo_root, "dist"))
    notes_path = os.path.join(repo_root, "dist", "release_notes.md")
    with open(notes_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_notes(data, args.version, args.tag))

    print("version : %s" % args.version)
    print("assets  : %d file(s) + SHA256SUMS" % len(assets))
    for a in assets:
        print("  %s" % os.path.relpath(a, repo_root))
    print("notes   : %s" % os.path.relpath(notes_path, repo_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
