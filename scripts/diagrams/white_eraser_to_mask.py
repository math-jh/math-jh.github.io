#!/usr/bin/env python3
"""Convert white 'eraser' paint in dvisvgm SVGs to true transparency.

TikZ paints white to erase content beneath it: double-line cores
(Rightarrow/equals arrows), crossing-over halos, label white-out boxes,
puncture markers. On a non-white page background the white shows as a
band/patch. For each white-painted element this script removes the element
and instead wraps everything drawn before it in a luminance <mask> (white
rect = keep, black silhouette of the eraser = cut), so the erased region is
genuinely transparent and the page background shows through in any theme.

Usage:  white_eraser_to_mask.py FILE.svg [...]
Exit 0: all files processed (files with no white paint are left untouched).
Exit 1: an invariant does not hold in some file; nothing is written for it.

Invariants (abort on violation, never guess):
  - every white paint (#fff/#ffffff/white, attr or style form) sits on a
    self-closed element that is a direct child of an untransformed
    <g id='page1'>
  - the file has a <defs> block and no id starting with 'wm'
  - the rewritten file parses as XML and contains no white paint outside
    the inserted <mask> rects
"""
import re
import sys

WHITE_RE = re.compile(r"(?:stroke|fill)=(['\"])(?:#fff|#ffffff|white)\1")
STYLE_WHITE_RE = re.compile(r"(?:stroke|fill):\s*(?:#fff|#ffffff|white)")
TAG_RE = re.compile(r'<[^>]+>')


def fail(path, msg):
    print(f'ABORT {path}: {msg}', file=sys.stderr)
    sys.exit(1)


def process(path):
    s = open(path, encoding='utf-8').read()
    if not WHITE_RE.search(s):
        if STYLE_WHITE_RE.search(s):
            fail(path, 'white paint in style= form (unhandled)')
        return False
    if STYLE_WHITE_RE.search(s):
        fail(path, 'white paint in style= form (unhandled)')
    if re.search(r"id=['\"]wm", s):
        fail(path, "id collision: 'wm*' already present")

    pages = re.findall(r"<g id=['\"]page\d+['\"][^>]*>", s)
    if len(pages) != 1:
        fail(path, f'expected exactly one <g id=pageN>, found {len(pages)}')
    m_page = re.search(r"<g id=['\"]page\d+['\"][^>]*>", s)
    if 'transform' in m_page.group(0):
        fail(path, '<g id=pageN> carries a transform')

    vb = re.search(r"viewBox=['\"]([-\d.eE ]+)['\"]", s)
    if not vb:
        fail(path, 'no viewBox')
    vx, vy, vw, vh = (float(t) for t in vb.group(1).split())
    mg = max(vw, vh)  # generous margin: page1-level translates are far smaller
    rx, ry, rw, rh = vx - mg, vy - mg, vw + 2 * mg, vh + 2 * mg
    region = f"x='{rx:g}' y='{ry:g}' width='{rw:g}' height='{rh:g}'"

    # Split page1's content into direct-child units [(text, is_eraser), ...].
    body_start = m_page.end()
    depth = 0
    units, pos, body_end = [], body_start, None
    for m in TAG_RE.finditer(s, body_start):
        tag = m.group(0)
        if tag.startswith('<!') or tag.startswith('<?'):
            fail(path, f'comment/PI inside page1: {tag[:60]}')
        if tag.startswith('</'):
            if depth == 0:
                body_end = m.start()  # closing </g> of page1
                break
            depth -= 1
            if depth == 0:
                units.append((s[pos:m.end()], False))
                pos = m.end()
        elif tag.endswith('/>'):
            if depth == 0:
                units.append((s[pos:m.end()], False))
                pos = m.end()
        else:
            depth += 1
    if body_end is None:
        fail(path, 'unbalanced tags in page1')
    if s[pos:body_end].strip():
        fail(path, f'stray non-tag content in page1: {s[pos:body_end]!r:.80}')

    erasers_total = len(WHITE_RE.findall(s))
    masks, out_units, n = [], [], 0
    for text, _ in units:
        whites = WHITE_RE.findall(text)
        if not whites:
            out_units.append(text)
            continue
        tags = TAG_RE.findall(text)
        if len(tags) != 1 or not tags[0].endswith('/>'):
            fail(path, f'white paint on a non-self-closed or nested unit: {text!r:.100}')
        if len(whites) != 1:
            fail(path, f'element painted white twice (stroke+fill): {text!r:.100}')
        n += 1
        silhouette = WHITE_RE.sub(lambda m: m.group(0)[:m.group(0).index('=')] + "='#000'", text.strip())
        masks.append(
            f"<mask id='wm{n}' maskUnits='userSpaceOnUse' {region}>\n"
            f"<rect {region} fill='#fff'/>\n{silhouette}\n</mask>"
        )
        wrapped = ''.join(out_units)
        out_units = [f"<g mask='url(#wm{n})'>{wrapped}</g>\n"]
    if n != erasers_total:
        fail(path, f'{erasers_total} white paints found, {n} handled')

    m_defs = re.search(r'</defs>', s)
    if m_defs:
        defs_ins, defs_block = m_defs.start(), '\n'.join(masks) + '\n'
    else:
        defs_ins, defs_block = m_page.start(), '<defs>\n' + '\n'.join(masks) + '\n</defs>\n'
    out = (
        s[:defs_ins] + defs_block + s[defs_ins:body_start]
        + ''.join(out_units) + s[body_end:]
    )

    # Gates: XML well-formed; no white paint outside inserted mask rects.
    import xml.etree.ElementTree as ET
    try:
        ET.fromstring(out)
    except ET.ParseError as e:
        fail(path, f'output is not well-formed XML: {e}')
    stripped = re.sub(r'<mask\b.*?</mask>', '', out, flags=re.S)
    if WHITE_RE.search(stripped) or STYLE_WHITE_RE.search(stripped):
        fail(path, 'white paint survived outside masks')
    # every original path d= must survive (erasers live on inside masks)
    for d in set(re.findall(r"\sd='[^']*'", s)):
        if d not in out:
            fail(path, f'path data lost: {d[:60]}...')

    open(path, 'w', encoding='utf-8').write(out)
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    changed = 0
    for p in sys.argv[1:]:
        if process(p):
            changed += 1
            print(f'masked: {p}')
    print(f'{changed}/{len(sys.argv) - 1} files rewritten')


if __name__ == '__main__':
    main()
