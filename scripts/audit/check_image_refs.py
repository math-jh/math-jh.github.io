#!/usr/bin/env python3
"""Check that every image/asset referenced by a Math post actually exists.

Scans _posts/Math/**/*.md for image references (markdown ![](…), <img src>,
and frontmatter overlay_image/teaser/image) and verifies each local path
resolves to a file in the repo. External (http, data:) refs are skipped.

Usage:  python3 scripts/audit/check_image_refs.py
Exit:   0 if all references resolve, 1 if any are missing.
"""
import os
import re
import sys
import glob

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
POSTS = [f for f in glob.glob(os.path.join(REPO, "_posts/Math/**/*.md"), recursive=True)
         if not f.endswith("CLAUDE.md")]

# any referenced asset path, by image extension, in markdown / html / frontmatter
REF = re.compile(r'(/assets/[^\s)"\'\]]+?\.(?:svg|png|jpe?g|gif|webp))', re.I)
# also catch non-/assets local image refs (markdown, html, frontmatter)
MD = re.compile(r'!\[[^\]]*\]\(([^)\s]+)')
HTML = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']')
FM = re.compile(r'^\s*(?:overlay_image|teaser|image)\s*:\s*(\S+)', re.M)


def local(p):
    p = p.strip().strip('"\'').split('#')[0].split('?')[0]
    return p and not p.startswith(("http://", "https://", "data:", "mailto:"))


def main():
    refs = set()
    missing = {}
    for f in POSTS:
        txt = open(f, encoding="utf-8", errors="ignore").read()
        cands = set(REF.findall(txt))
        for rx in (MD, HTML, FM):
            cands |= {m for m in rx.findall(txt) if local(m)}
        for p in cands:
            refs.add(p)
            fp = (REPO + p) if p.startswith("/") else os.path.join(os.path.dirname(f), p)
            fp = fp.split("#")[0].split("?")[0]
            if not os.path.exists(fp):
                missing.setdefault(p, set()).add(os.path.relpath(f, REPO))

    print(f"distinct image assets referenced: {len(refs)} | MISSING: {len(missing)}\n")
    for p in sorted(missing):
        print(f"✗ {p}")
        for post in sorted(missing[p]):
            print(f"      ← {post}")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
