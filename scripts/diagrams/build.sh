#!/usr/bin/env bash
# Build blog diagrams from per-article LaTeX sources.
#
#   <Article>.tex  ->  <Article>-1..N.svg   (one SVG per figure)
#
# File format: a standalone preamble, then \begin{document}, then figures
# separated by lines starting with %%FIG, then \end{document}:
#
#   \documentclass[border=2pt]{standalone}
#   \usepackage{...}                       % quiver, Operators, palette, diagram-style
#   \begin{document}
#   %%FIG <alt_text> (<Article>-1.svg)     % <alt_text> MUST equal the post's ![alt](...)
#   \begin{tikzcd} ... \end{tikzcd}
#   %%FIG <alt_text> (<Article>-2.svg)
#   \begin{tikzpicture} ... \end{tikzpicture}
#   \end{document}
#
# Each figure is compiled as its OWN single-page standalone job (NOT standalone's
# multi mode, which splits tikz-cd's inner tikzpicture and collapses arrow labels).
# Output is transparent vector; the script prints the markdown width so node text
# == blog body text:  width_em = intrinsic_pt / BASEFONT   (BASEFONT = 10pt base).
# White eraser paint (double-line cores, crossing-over halos, label white-out)
# stays as real paint — the diagram tag inlines SVGs and CSS(_diagram-colors.scss)
# repaints #fff to the page background, opaquely and theme-correctly (mask cutouts
# left AA seams; un-masked 2026-07-26). --strip restores the old mask conversion
# for img-rendered files. Colors outside the CSS rule inventory trigger a warning.
#
# Usage:
#   scripts/diagrams/build.sh <Category>/<Article> [...]   # assets/diagrams/Math/<Category>/<Article>.tex
#   scripts/diagrams/build.sh path/to/<Article>.tex [...]
#   scripts/diagrams/build.sh [--png] [--no-strip] [--lua] [--bold PT] [--out DIR] <target> [<target>...]
#
# Multiple targets build sequentially in one run; flags apply to every target
# (--out sends every target's output to the same DIR).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PRE="$ROOT/assets/diagrams/.preamble"

BASEFONT=10
SCALE=1.1          # display scale: node text = SCALE x body text (1.0 = exact match)
GLYPH_BOLD=0.20    # pt of stroke added to glyphs so thin CM hairlines don't go subpixel
                   # (0 = off; --bold overrides). Stroke color = the glyph's own fill color.
DENSITY=1024
MODE=svg
STRIP=0            # white eraser stays as paint (inline CSS가 배경색으로 덧칠). --strip: 옛 mask 변환
LUAMODE=0          # --lua: compile via dvilualatex (luaTeX dynamic memory) for pgfplots surf shading
                   #        that OOMs plain latex; still DVI so dvisvgm keeps fill-opacity (the --pdf route drops it)
OUT=""

args=()
while [ $# -gt 0 ]; do
  case "$1" in
    --png) MODE=png; shift;;
    --strip) STRIP=1; shift;;
    --no-strip) STRIP=0; shift;;
    --lua) LUAMODE=1; shift;;
    --bold) GLYPH_BOLD="$2"; shift 2;;
    --out) OUT="$2"; shift 2;;
    *) args+=("$1"); shift;;
  esac
done
[ ${#args[@]} -ge 1 ] || { grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 1; }

WORK="$(mktemp -d "${TMPDIR:-/tmp}/diagbuild.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

emit () { awk -v pt="$1" -v b="$BASEFONT" -v s="$SCALE" 'BEGIN{printf "width:%.2fem", s*pt/b}'; }

TIDX=0
for TARGET in "${args[@]}"; do
TIDX=$((TIDX+1))
if [ -f "$TARGET" ]; then
  TEX="$(cd "$(dirname "$TARGET")" && pwd)/$(basename "$TARGET")"
else
  TEX="$ROOT/assets/diagrams/Math/${TARGET%.tex}.tex"
fi
[ -f "$TEX" ] || { echo "no such tex: $TEX" >&2; exit 1; }
ART="$(basename "$TEX" .tex)"
CAT="$(basename "$(dirname "$TEX")")"
OUTDIR="$OUT"
[ -n "$OUTDIR" ] || OUTDIR="$ROOT/assets/images/Math/$CAT"
mkdir -p "$OUTDIR"

W="$WORK/t$TIDX"
mkdir -p "$W"
export TEXINPUTS="$PRE:$(dirname "$TEX"):"

# Split <Article>.tex into one compilable single-page job per %%FIG chunk.
# Also write manifest.tsv: "idx<TAB>outbase<TAB>ext" — the output name/format of
# each figure, read from its %%FIG "(<name>.<ext>)" comment so one .tex can mix
# svg and png figures (png = crossing-over diagrams). Missing/odd ext -> default MODE.
NFIG=$(python3 - "$TEX" "$W" "$ART" "$MODE" <<'PY'
import sys, re
src, work, art, mode = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
lines = open(src, encoding='utf-8').read().split('\n')
pre, body, seen = [], [], False
for ln in lines:
    if not seen:
        if re.match(r'\s*\\begin\{document\}', ln): seen = True
        else: pre.append(ln)
    else:
        if re.match(r'\s*\\end\{document\}', ln): break
        body.append(ln)
preamble = '\n'.join(pre)
# split body on %%FIG markers, remembering each chunk's marker line
chunks, markers, cur, mk = [], [], [], None
for ln in body:
    if re.match(r'\s*%%FIG', ln):
        if any(s.strip() for s in cur): chunks.append(cur); markers.append(mk)
        cur, mk = [], ln
    else:
        cur.append(ln)
if any(s.strip() for s in cur): chunks.append(cur); markers.append(mk)
man = open(f'{work}/manifest.tsv', 'w', encoding='utf-8')
for i, (ch, mk) in enumerate(zip(chunks, markers), 1):
    doc = preamble + '\n\\begin{document}\n' + '\n'.join(ch) + '\n\\end{document}\n'
    open(f'{work}/fig-{i}.tex', 'w', encoding='utf-8').write(doc)
    base, ext = f'{art}-{i}', mode
    m = re.search(r'\(([^)]+)\)\s*$', mk or '')
    if m:
        name = m.group(1).strip()
        if '.' in name:
            b, e = name.rsplit('.', 1)
            base = b.strip()
            if e.strip().lower() in ('svg', 'png'): ext = e.strip().lower()
        else:
            base = name
    man.write(f'{i}\t{base}\t{ext}\n')
man.close()
print(len(chunks))
PY
)
[ "$NFIG" -ge 1 ] || { echo "no %%FIG figures found in $TEX" >&2; exit 1; }

echo "# $CAT/$ART  ($NFIG figures)  ->  $OUTDIR"

for i in $(seq 1 "$NFIG"); do
  row="$(awk -F'\t' -v n="$i" '$1==n{print $2"\t"$3}' "$W/manifest.tsv")"
  NAME="${row%$'\t'*}"; FMT="${row#*$'\t'}"
  [ -n "$NAME" ] || { NAME="$ART-$i"; FMT="$MODE"; }
  if [ "$LUAMODE" = 1 ]; then ENG=dvilualatex; else ENG=latex; fi
  ( cd "$W" && $ENG -interaction=nonstopmode -halt-on-error "fig-$i.tex" >"fig-$i.log" 2>&1 ) \
    || { echo "$ENG FAILED (fig $i):" >&2; tail -20 "$W/fig-$i.log" >&2; exit 1; }
  if [ "$FMT" = svg ]; then
    dvisvgm --no-fonts --bbox=preview "$W/fig-$i.dvi" -o "$OUTDIR/$NAME.svg" >/dev/null 2>"$W/d-$i.log" \
      || { echo "dvisvgm FAILED (fig $i):" >&2; cat "$W/d-$i.log" >&2; exit 1; }
    f="$OUTDIR/$NAME.svg"
    # --strip일 때만 옛 mask 변환 (img.invert로 렌더될 파일 전용 — 인라인 경로는
    # CSS가 #fff를 배경색으로 덧칠하므로 변환 불필요, mask는 AA 잔흔을 남긴다)
    if [ "$STRIP" = 1 ]; then
      python3 "$ROOT/scripts/diagrams/white_eraser_to_mask.py" "$f" >/dev/null \
        || { echo "white_eraser_to_mask FAILED (fig $i)" >&2; exit 1; }
    fi
    python3 - "$f" "$GLYPH_BOLD" <<'PY'
import re, sys
p, bold = sys.argv[1], sys.argv[2]
s = open(p, encoding='utf-8').read()
# Embolden glyphs: dvisvgm --no-fonts renders text as filled paths via <use>; thin
# Computer Modern hairlines fade to subpixel at body size. Each <use> gets a stroke
# in its inherited fill color (own fill attr, else nearest ancestor <g fill=...>,
# else black) so colored labels keep their color. fill='none' glyphs (stripped
# white halos) are left unstroked.
if float(bold) > 0:
    fill_re = re.compile(r"fill=['\"]([^'\"]+)['\"]")
    out, stack, pos = [], [], 0
    for m in re.finditer(r'<[^>]+>', s):
        tag = m.group(0)
        if re.match(r'<g[\s>]', tag):
            fm = fill_re.search(tag)
            stack.append(fm.group(1) if fm else (stack[-1] if stack else '#000'))
        elif tag.startswith('</g'):
            if stack: stack.pop()
        elif re.match(r'<use\s', tag):
            fm = fill_re.search(tag)
            fill = fm.group(1) if fm else (stack[-1] if stack else '#000')
            if fill != 'none':
                out.append(s[pos:m.start()])
                out.append(tag.replace('<use ', f"<use stroke='{fill}' stroke-width='{bold}' stroke-linejoin='round' ", 1))
                pos = m.end()
    out.append(s[pos:])
    s = ''.join(out)
open(p, 'w', encoding='utf-8').write(s)
PY
    python3 "$ROOT/scripts/diagrams/check_diagram_colors.py" "$f"
    ptw="$(grep -oE "width='[0-9.]+pt'|width=\"[0-9.]+pt\"" "$f" | head -1 | grep -oE '[0-9.]+')"
    printf '  %-30s %s\n' "$NAME.svg" "$(emit "$ptw")"
  else
    ( cd "$W" && dvips -q -o "fig-$i.ps" "fig-$i.dvi" 2>/dev/null )
    magick -density "$DENSITY" "$W/fig-$i.ps" -background none -alpha on \
      -fuzz 2% -fill none -opaque white "$OUTDIR/$NAME.png" 2>/dev/null \
      || { echo "magick FAILED (fig $i)" >&2; exit 1; }
    pxw="$(identify -format '%w' "$OUTDIR/$NAME.png")"
    ptw="$(awk -v px="$pxw" -v d="$DENSITY" 'BEGIN{printf "%.3f", px*72/d}')"
    printf '  %-30s %s\n' "$NAME.png" "$(emit "$ptw")"
  fi
done
done
