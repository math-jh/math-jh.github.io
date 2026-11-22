#!/usr/bin/env python3
"""Material Symbols Sharp 를 사이트가 쓰는 아이콘만 남긴 subset 으로 만든다.

원본(전체) 폰트: scripts/fonts/material-symbols-sharp.full.woff2  (Google, Apache 2.0)
출력:           assets/css/fonts/material-symbols-sharp.woff2   (assets/css/fonts.scss 가 부른다)

아이콘은 두 길로 그려진다.
  - ligature: 요소 텍스트 'search' 가 rlig 로 아이콘 글리프 하나가 된다 (.material-icons)
  - 코드포인트: CSS content: "\\e873" 처럼 PUA 코드포인트를 직접 쓴다 (_subject-cards.scss)

쓰이는 아이콘 이름은 소스에서 모은다 (넉넉하게 잡는 쪽으로).
  - HTML·Liquid·Markdown: class 에 material-icons/material-symbols 가 있는 요소의 텍스트,
    icon.html 의 name="..."
  - YAML·front matter: icon: 값 (navigation.yml 등 — Liquid 가 요소 텍스트로 넣는다)
  - JS·인라인 스크립트: 문자열 리터럴 가운데 아이콘 이름과 정확히 같은 것
  - SCSS: content: "\\eXXX"
FILL·wght·GRAD·opsz 가변 축은 그대로 둔다.

새 아이콘을 쓰면 이 스크립트를 다시 돌린다. 빠진 아이콘은 이름 글자 그대로(예: graph_3) 보인다.

  python3 scripts/fonts/subset_material_symbols.py           # subset 생성
  python3 scripts/fonts/subset_material_symbols.py --check   # _site 의 렌더 결과가 subset 에 다 있는지
"""

import argparse
import re
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[2]
FULL = ROOT / "scripts/fonts/material-symbols-sharp.full.woff2"
OUT = ROOT / "assets/css/fonts/material-symbols-sharp.woff2"

SCAN_DIRS = ["_includes", "_layouts", "_pages", "_posts", "_data", "_plugins",
             "_sass", "assets/css", "assets/js", "scripts/dashboard", "assets/dev-preview"]
SCAN_FILES = ["_config.yml"]
SKIP_PARTS = {"vendor", "katex", "node_modules"}
EXTS = {".html", ".md", ".yml", ".yaml", ".js", ".scss", ".css", ".rb", ".liquid"}

NAME = r"[a-z0-9_]+"
RE_ELEMENT = re.compile(r"""class=["'][^"']*material-(?:icons|symbols)[^"']*["'][^>]*>\s*(""" + NAME + r")\s*<")
RE_INCLUDE = re.compile(r"include\s+icon\.html\s+name=[\"'](" + NAME + r")[\"']")
RE_YAML_ICON = re.compile(r"^\s*-?\s*icon\s*:\s*[\"']?(" + NAME + r")[\"']?\s*(?:#.*)?$", re.M)
RE_STRING = re.compile(r"[\"'`](" + NAME + r")[\"'`]")
RE_CSS_CP = re.compile(r'content\s*:\s*["\']\\([0-9a-fA-F]{4,5})["\']')
RE_SITE_ELEMENT = re.compile(r"""class=["'][^"']*material-(?:icons|symbols)[^"']*["'][^>]*>\s*([^<\s]*)\s*<""")
NAME_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789_"


def ligatures(font):
    """아이콘 이름 -> 리가처 글리프. rlig 의 LigatureSubst 를 그대로 읽는다."""
    rev = {g: chr(cp) for cp, g in font.getBestCmap().items() if cp < 0x80}
    out = {}
    for lk in font["GSUB"].table.LookupList.Lookup:
        for st in lk.SubTable:
            st = st.ExtSubTable if lk.LookupType == 7 else st
            if st.LookupType != 4:
                continue
            for first, ligs in st.ligatures.items():
                for lig in ligs:
                    comps = [first] + list(lig.Component)
                    if all(c in rev for c in comps):
                        out.setdefault("".join(rev[c] for c in comps), lig.LigGlyph)
    return out


def source_files():
    for d in SCAN_DIRS:
        for p in (ROOT / d).rglob("*"):
            if p.is_file() and p.suffix in EXTS and not (SKIP_PARTS & set(p.parts)):
                yield p
    for f in SCAN_FILES:
        yield ROOT / f


def collect(lig_names):
    names, codepoints = set(), set()
    for p in source_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        names.update(RE_ELEMENT.findall(text))
        names.update(RE_INCLUDE.findall(text))
        names.update(RE_YAML_ICON.findall(text))
        if p.suffix in {".js", ".html"}:
            names.update(n for n in RE_STRING.findall(text) if n in lig_names)
        codepoints.update(int(h, 16) for h in RE_CSS_CP.findall(text))
    return {n for n in names if n in lig_names}, codepoints


def build():
    font = TTFont(FULL)
    ligs = ligatures(font)
    names, codepoints = collect(set(ligs))
    cmap = font.getBestCmap()
    glyphs = {ligs[n] for n in names} | {cmap[cp] for cp in codepoints if cp in cmap}
    unicodes = [ord(c) for c in NAME_CHARS + " "] + sorted(codepoints)

    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.layout_closure = False   # 남긴 이름의 리가처만 — 글자 전체로 닫으면 아이콘 전부가 딸려 온다
    opts.notdef_outline = True
    opts.name_IDs = ["*"]
    opts.name_languages = ["*"]
    sub = subset.Subsetter(opts)
    sub.populate(glyphs=sorted(glyphs), unicodes=unicodes)
    sub.subset(font)
    font.flavor = "woff2"
    font.save(OUT)

    kept = ligatures(TTFont(OUT))
    missing = sorted(n for n in names if n not in kept)
    if missing:
        sys.exit(f"subset 에서 리가처가 빠졌다: {missing}")
    print(f"{len(names)} 개 이름 + 코드포인트 {len(codepoints)} 개 -> {OUT.relative_to(ROOT)} "
          f"({FULL.stat().st_size // 1024} KB -> {OUT.stat().st_size // 1024} KB)")
    print(" ".join(sorted(names)))


def check():
    """_site 의 렌더된 HTML 에서 아이콘 요소 텍스트를 모아 subset 에 다 있는지 본다."""
    kept = set(ligatures(TTFont(OUT)))
    site = (ROOT / "_site").resolve()
    seen = {}
    for p in site.rglob("*.html"):
        for n in RE_SITE_ELEMENT.findall(p.read_text(encoding="utf-8", errors="replace")):
            if n and "{" not in n:
                seen.setdefault(n, str(p.relative_to(site)))
    missing = {n: where for n, where in seen.items() if n not in kept}
    for n, where in sorted(missing.items()):
        print(f"MISSING {n}  ({where})")
    print(f"_site 아이콘 {len(seen)} 종, subset 에 없는 것 {len(missing)} 종")
    return 1 if missing else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    sys.exit(check() if ap.parse_args().check else build())
