#!/usr/bin/env bash
# Build blog diagrams from a per-article LaTeX source.
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
# Crossing-over diagrams: --png (raster, white halo flattened to transparent).
#
# Usage:
#   scripts/diagrams/build.sh <Category>/<Article>      # assets/diagrams/Math/<Category>/<Article>.tex
#   scripts/diagrams/build.sh path/to/<Article>.tex
#   scripts/diagrams/build.sh [--png] [--out DIR] <target>
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PRE="$ROOT/assets/diagrams/.preamble"
BASEFONT=10
SCALE=1.1          # display scale: node text = SCALE x body text (1.0 = exact match)
GLYPH_BOLD=0.25    # pt of stroke added to glyphs so thin CM hairlines don't go subpixel (0 = off)
DENSITY=1024
MODE=svg
OUT=""

args=()
while [ $# -gt 0 ]; do
  case "$1" in
    --png) MODE=png; shift;;
    --out) OUT="$2"; shift 2;;
    *) args+=("$1"); shift;;
  esac
done
[ ${#args[@]} -eq 1 ] || { grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 1; }
TARGET="${args[0]}"

if [ -f "$TARGET" ]; then
  TEX="$(cd "$(dirname "$TARGET")" && pwd)/$(basename "$TARGET")"
else
  TEX="$ROOT/assets/diagrams/Math/${TARGET%.tex}.tex"
fi
[ -f "$TEX" ] || { echo "no such tex: $TEX" >&2; exit 1; }
ART="$(basename "$TEX" .tex)"
CAT="$(basename "$(dirname "$TEX")")"
[ -n "$OUT" ] || OUT="$ROOT/assets/images/Math/$CAT"
mkdir -p "$OUT"

WORK="$(mktemp -d /var/tmp/diagbuild.XXXXXX)"
trap 'rm -rf "$WORK"' EXIT
export TEXINPUTS="$PRE:$(dirname "$TEX"):"

# Split <Article>.tex into one compilable single-page job per %%FIG chunk.
NFIG=$(python3 - "$TEX" "$WORK" <<'PY'
import sys, re
src, work = sys.argv[1], sys.argv[2]
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
# split body on %%FIG markers
chunks, cur = [], []
for ln in body:
    if re.match(r'\s*%%FIG', ln):
        if any(s.strip() for s in cur): chunks.append(cur)
        cur = []
    else:
        cur.append(ln)
if any(s.strip() for s in cur): chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    doc = preamble + '\n\\begin{document}\n' + '\n'.join(ch) + '\n\\end{document}\n'
    open(f'{work}/fig-{i}.tex', 'w', encoding='utf-8').write(doc)
print(len(chunks))
PY
)
[ "$NFIG" -ge 1 ] || { echo "no %%FIG figures found in $TEX" >&2; exit 1; }

emit () { awk -v pt="$1" -v b="$BASEFONT" -v s="$SCALE" 'BEGIN{printf "width:%.2fem", s*pt/b}'; }
echo "# $CAT/$ART  ($NFIG figures)  ->  $OUT"

for i in $(seq 1 "$NFIG"); do
  ( cd "$WORK" && latex -interaction=nonstopmode -halt-on-error "fig-$i.tex" >"fig-$i.log" 2>&1 ) \
    || { echo "latex FAILED (fig $i):" >&2; tail -20 "$WORK/fig-$i.log" >&2; exit 1; }
  if [ "$MODE" = svg ]; then
    dvisvgm --no-fonts --bbox=preview "$WORK/fig-$i.dvi" -o "$OUT/$ART-$i.svg" >/dev/null 2>"$WORK/d-$i.log" \
      || { echo "dvisvgm FAILED (fig $i):" >&2; cat "$WORK/d-$i.log" >&2; exit 1; }
    f="$OUT/$ART-$i.svg"
    python3 - "$f" "$GLYPH_BOLD" <<'PY'
import re, sys
p, bold = sys.argv[1], sys.argv[2]
s = open(p, encoding='utf-8').read()
# White halo / label fill -> transparent (item 2); dvisvgm bg already transparent.
s = re.sub(r"(fill=['\"])#f{3}(?:f{3})?(['\"])", r"\1none\2", s)
s = re.sub(r"(fill:)#f{3}(?:f{3})?", r"\1none", s)
s = re.sub(r"(fill=['\"])white(['\"])", r"\1none\2", s)
# Embolden glyphs: dvisvgm --no-fonts renders text as filled paths via <use>; thin
# Computer Modern hairlines fade to subpixel at body size. Add a matching stroke.
if float(bold) > 0:
    s = s.replace("<use ", f"<use stroke='#000' stroke-width='{bold}' stroke-linejoin='round' ")
open(p, 'w', encoding='utf-8').write(s)
PY
    ptw="$(grep -oE "width='[0-9.]+pt'|width=\"[0-9.]+pt\"" "$f" | head -1 | grep -oE '[0-9.]+')"
    printf '  %-30s %s\n' "$ART-$i.svg" "$(emit "$ptw")"
  else
    ( cd "$WORK" && dvips -q -o "fig-$i.ps" "fig-$i.dvi" 2>/dev/null )
    magick -density "$DENSITY" "$WORK/fig-$i.ps" -background none -alpha on \
      -fuzz 2% -fill none -opaque white "$OUT/$ART-$i.png" 2>/dev/null \
      || { echo "magick FAILED (fig $i)" >&2; exit 1; }
    pxw="$(identify -format '%w' "$OUT/$ART-$i.png")"
    ptw="$(awk -v px="$pxw" -v d="$DENSITY" 'BEGIN{printf "%.3f", px*72/d}')"
    printf '  %-30s %s\n' "$ART-$i.png" "$(emit "$ptw")"
  fi
done
