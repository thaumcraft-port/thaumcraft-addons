#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build.py - cross-platform one-shot: rebuild catalog + README (+ validate).

    python scripts/build.py
    python scripts/build.py --validate
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Rebuild catalog and README.")
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--validate", action="store_true", help="also run the validator")
    args = parser.parse_args(argv)

    repo_root = args.repo_root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    import build_catalog

    build_catalog.main(["--repo-root", repo_root])

    import gen_readme

    rc = gen_readme.main(["--repo-root", repo_root])
    if rc != 0:
        return rc

    if args.validate:
        import validate

        return validate.main(["--repo-root", repo_root, "--check-generated"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
