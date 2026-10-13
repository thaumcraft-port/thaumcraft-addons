#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_readme.py - one-click regeneration of ``README.md``.

Renders ``README.template.md`` using the live catalog and writes ``README.md``.

    python scripts/gen_readme.py            # build catalog + render README
    python scripts/gen_readme.py --check    # fail if README.md is stale (CI)

Supported placeholders in the template
--------------------------------------
``{{GENERATED_AT}}`` ``{{TOTAL}}`` ``{{MC_VERSIONS}}`` ``{{RELEASES_PAGE}}``
``{{TABLE_STABLE}}`` ``{{TABLE_EXPERIMENTAL}}`` ``{{MOD_CARDS}}``
``{{BUILD_MATRIX}}`` ``{{CHECKSUMS}}``
"""

from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tc4lib  # noqa: E402

# The generated timestamp changes on every run; ignore it when diffing.
_TS_RE = re.compile(r"生成时间：[0-9T:.+\-Z]+")


def _normalise(text: str) -> str:
    return _TS_RE.sub("生成时间：<TS>", text)


# --------------------------------------------------------------------------- #
# Renderers
# --------------------------------------------------------------------------- #
def _table_for(records) -> str:
    rows = []
    for r in sorted(records, key=lambda x: (x["mod_name"].lower(), x["mod_version"])):
        rows.append(
            [
                r["mod_name"],
                "`%s`" % r["mod_id"],
                "`%s`" % r["mod_version"],
                tc4lib.loader_display(r["loader"]),
                tc4lib.tc4_requirement(r),
                tc4lib.human_size(r["size"]),
                "[下载](%s)" % r["download_url"],
            ]
        )
    headers = ["模组", "modId", "版本", "加载器", "TC4R 要求", "大小", "下载"]
    return tc4lib.md_table(headers, rows)


def render_tables(data: dict, channel: str) -> str:
    mods = [r for r in data["mods"] if r["channel"] == channel]
    if not mods:
        return "_暂无。_"
    blocks = []
    for mc in sorted({r["mc_version"] for r in mods}):
        group = [r for r in mods if r["mc_version"] == mc]
        blocks.append("#### Minecraft %s\n\n%s" % (mc, _table_for(group)))
    return "\n\n".join(blocks)


def render_mod_cards(data: dict) -> str:
    mods = [r for r in data["mods"] if r["channel"] == "stable"]
    by_name: dict = {}
    for r in mods:
        by_name.setdefault(r["mod_name"].lower(), []).append(r)
    blocks = []
    for key in sorted(by_name):
        entries = sorted(by_name[key], key=lambda x: x["mc_version"])
        name = entries[0]["mod_name"]
        mod_ids = sorted({e["mod_id"] for e in entries})
        lines = ["### %s (`%s`)" % (name, "` / `".join(mod_ids))]
        desc = next((e["description"] for e in entries if e.get("description")), "")
        if desc:
            lines.append("")
            lines.append("> %s" % tc4lib.md_escape(desc))
        lines.append("")
        for e in entries:
            lines.append(
                "- **Minecraft %s** · %s · 模组版本 `%s` · 需要 %s · [下载](%s)"
                % (
                    e["mc_version"],
                    tc4lib.loader_display(e["loader"]),
                    e["mod_version"],
                    tc4lib.tc4_requirement(e),
                    e["download_url"],
                )
            )
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) if blocks else "_暂无。_"


def render_build_matrix(data: dict) -> str:
    rows = []
    for r in data["mods"]:
        tc4 = r.get("tc4") or {}
        build = tc4.get("build")
        rows.append(
            [
                r["mod_name"],
                r["mc_version"],
                tc4lib.loader_display(r["loader"]),
                "`%s`" % r["mod_version"],
                tc4.get("base") or "?",
                str(build) if build is not None else "任意",
                ("实验" if r["channel"] == "experimental" else "正式"),
            ]
        )
    rows.sort(key=lambda x: (x[1], x[0].lower()))
    return tc4lib.md_table(["模组", "MC", "加载器", "模组版本", "TC4R 基线", "最低构建号", "通道"], rows)


def render_checksums(data: dict) -> str:
    lines = ["| 文件 | SHA-256 |", "| --- | --- |"]
    for r in data["mods"]:
        lines.append("| `%s` | `%s` |" % (r["file_name"], r["sha256"]))
    inner = "\n".join(lines)
    return "<details>\n<summary>点击展开全部 SHA-256 校验和</summary>\n\n%s\n\n</details>" % inner


def render(template: str, data: dict) -> str:
    mc_versions = " · ".join(data["mc_versions"]) if data["mc_versions"] else "-"
    repl = {
        "{{GENERATED_AT}}": data["generated_at"],
        "{{TOTAL}}": str(data["total"]),
        "{{MC_VERSIONS}}": mc_versions,
        "{{RELEASES_PAGE}}": tc4lib.RELEASES_URL,
        "{{TABLE_STABLE}}": render_tables(data, "stable"),
        "{{TABLE_EXPERIMENTAL}}": render_tables(data, "experimental"),
        "{{MOD_CARDS}}": render_mod_cards(data),
        "{{BUILD_MATRIX}}": render_build_matrix(data),
        "{{CHECKSUMS}}": render_checksums(data),
    }
    out = template
    for key, value in repl.items():
        out = out.replace(key, value)
    return out


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
def render_from_root(repo_root: str, release_tag: str) -> str:
    import build_catalog  # noqa: WPS433 (local import)

    data = build_catalog.build(repo_root, release_tag)
    build_catalog.write_catalog(repo_root, data)
    build_catalog.write_checksums(repo_root, data)
    tpl_path = os.path.join(repo_root, "README.template.md")
    with open(tpl_path, "r", encoding="utf-8") as fh:
        template = fh.read()
    return render(template, data)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate README.md from README.template.md.")
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--release-tag", default=os.environ.get("RELEASE_TAG", "latest"))
    parser.add_argument("--check", action="store_true", help="exit 1 if README.md is out of date")
    args = parser.parse_args(argv)

    repo_root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme = render_from_root(repo_root, args.release_tag)
    readme_path = os.path.join(repo_root, "README.md")

    if args.check:
        current = ""
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as fh:
                current = fh.read()
        if _normalise(current) != _normalise(readme):
            print("README.md is out of date; run: python scripts/gen_readme.py", file=sys.stderr)
            return 1
        print("README.md is up to date")
        return 0

    with open(readme_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(readme)
    print("wrote %s" % os.path.relpath(readme_path, repo_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
