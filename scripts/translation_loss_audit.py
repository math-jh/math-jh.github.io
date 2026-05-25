#!/usr/bin/env python3
"""Mechanical KO→EN translation loss audit.

For every ko/*.md with a paired en/ counterpart that is a Kimi translation
(translation_source: kimi-cli), compute:
  - body line counts (non-blank, after frontmatter)
  - body char counts (after frontmatter, with <sub>...</sub> stripped from both)
  - ratio = en / ko

Flag suspicious pairs by ratio thresholds. EN ≈ 0.85–1.10× KO is normal for
this blog (Korean is denser; EN slightly inflates). <0.75 is suspicious;
<0.65 is almost always truncation.
"""
from __future__ import annotations
import re, sys
from pathlib import Path

BLOG = Path("/home/junhyeok/math-jh.github.io")
POSTS = BLOG / "_posts/Math"
FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SUB = re.compile(r"<sub>.*?</sub>", re.DOTALL)
DATE_PREFIX = re.compile(r"^\d{4}-\d{2}-\d{2}-")


def slug(p: Path) -> str:
    return DATE_PREFIX.sub("", p.name, 1)


def body(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    m = FM.match(t)
    return t[m.end():] if m else t


def nonblank_lines(text: str) -> int:
    return sum(1 for L in text.splitlines() if L.strip())


def is_kimi(path: Path) -> bool:
    t = path.read_text(encoding="utf-8")
    m = FM.match(t)
    if not m:
        return False
    return "translation_source: kimi-cli" in m.group(1)


def en_for(ko_path: Path) -> Path | None:
    parts = list(ko_path.parts[:-1])
    parts[parts.index("ko")] = "en"
    en_dir = Path(*parts)
    if not en_dir.exists():
        return None
    s = slug(ko_path)
    for f in en_dir.glob("*.md"):
        if slug(f) == s:
            return f
    return None


INS_RE = re.compile(r'<ins\s+id="([^"]+)"')


def truncation_signal(en_body: str, ko_body: str) -> str:
    """Heuristic check for mid-output truncation. Returns reason string or ''.

    Catches cases where ratio looks fine but the file ends mid-content.
    """
    en = en_body.rstrip()
    if not en:
        return "empty body"
    # Unbalanced `$$` — odd count means a math block is unclosed
    if en.count("$$") % 2 != 0:
        return "odd $$ count"
    last = en.splitlines()[-1].strip() if en.splitlines() else ""
    # Last non-blank line opens a block but doesn't close it
    if last.startswith("<div ") and ">" not in last:
        return "unclosed <div"
    if last.endswith("$\\") or last.endswith("\\"):
        return "trailing backslash"
    # Anchor coverage: every KO anchor must appear in EN
    ko_anchors = set(INS_RE.findall(ko_body))
    en_anchors = set(INS_RE.findall(en_body))
    missing = ko_anchors - en_anchors
    if missing:
        return f"missing {len(missing)} <ins id>: {sorted(missing)[:3]}"
    # KO has References section, EN doesn't
    if re.search(r"##\s*참고문헌|^\*\*참고문헌\*\*", ko_body, re.MULTILINE) and \
       not re.search(r"##\s*References|^\*\*References\*\*", en_body, re.MULTILINE):
        return "missing References"
    return ""


rows = []
for ko in sorted(POSTS.glob("*/ko/*.md")):
    en = en_for(ko)
    if en is None or not is_kimi(en):
        continue
    ko_body = SUB.sub("", body(ko))
    en_body = SUB.sub("", body(en))
    ko_lines = nonblank_lines(ko_body)
    en_lines = nonblank_lines(en_body)
    ko_chars = len(ko_body.strip())
    en_chars = len(en_body.strip())
    if ko_lines == 0 or ko_chars == 0:
        continue
    r_lines = en_lines / ko_lines
    r_chars = en_chars / ko_chars
    trunc = truncation_signal(en_body, ko_body)
    rows.append({
        "ko": ko, "en": en,
        "ko_l": ko_lines, "en_l": en_lines, "r_l": r_lines,
        "ko_c": ko_chars, "en_c": en_chars, "r_c": r_chars,
        "trunc": trunc,
    })


def flag(r: dict) -> str:
    if r["trunc"]:
        return "🚨 TRUNC "
    worst = min(r["r_l"], r["r_c"])
    if worst < 0.55: return "🚨 SEVERE"
    if worst < 0.70: return "⚠️  SUSPECT"
    if worst < 0.80: return "•  CHECK "
    return "   ok    "


print(f"{'flag':<11} {'r_l':>5} {'r_c':>5}  {'ko_l/en_l':>11}  {'ko_c/en_c':>13}  file  [trunc reason]")
print("-" * 120)
# Sort: truncated first, then by worst ratio
rows.sort(key=lambda r: (0 if r["trunc"] else 1, min(r["r_l"], r["r_c"])))
flagged = [r for r in rows if flag(r).strip() not in ("ok",)]
for r in flagged:
    rel = r["ko"].relative_to(POSTS)
    tr = f"  [{r['trunc']}]" if r["trunc"] else ""
    print(f"{flag(r)}  {r['r_l']:.2f}  {r['r_c']:.2f}  "
          f"{r['ko_l']:>5}/{r['en_l']:<5}  {r['ko_c']:>6}/{r['en_c']:<6}  {rel}{tr}")

n_trunc = sum(1 for r in rows if r["trunc"])
print(f"\nTotal kimi-translated pairs: {len(rows)}")
print(f"  TRUNCATED (heuristic):    {n_trunc}")
print(f"  flagged (low ratio/trunc): {len(flagged)}")
