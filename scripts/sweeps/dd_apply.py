#!/usr/bin/env python3
r"""dd_extract.py 가 뽑은 후보를 실제로 치환한다.

AUTO·MATHOP 은 자동 승인, AMBIG 은 --decisions 로 받은 판정에서 yes 인 것만.
NESTED 는 언제나 제외한다.

게이트 (하나라도 깨지면 그 파일은 통째로 롤백):
  1. 수식 영역 바깥의 텍스트가 한 바이트도 안 바뀐다
  2. 수식 영역의 개수·경계가 보존된다
  3. `$` 개수가 보존된다
  4. 바뀐 수식이 KaTeX 로 렌더된다 (--katex 지정 시)

기본은 dry-run. 실제로 쓰려면 --write.
"""
import argparse, difflib, json, os, re, subprocess, sys, tempfile, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dd_extract import math_spans


def segments(text):
    """[(kind, s, e)] — kind 는 'txt' 또는 'math'. 전체를 빈틈없이 덮는다."""
    out, prev = [], 0
    for a, b, disp in math_spans(text):
        if a > prev:
            out.append(('txt', prev, a, False))
        out.append(('math', a, b, disp))
        prev = b
    out.append(('txt', prev, len(text), False))
    return out


def apply_file(path, cands, katex=None):
    orig = open(path, encoding='utf-8').read()
    segs = segments(orig)
    math_ranges = [(a, b) for k, a, b, _ in segs if k == 'math']

    def in_math(s, e):
        return any(a <= s and e <= b for a, b in math_ranges)

    todo = sorted(cands, key=lambda r: r['start'], reverse=True)
    new = orig
    touched = []
    for r in todo:
        s, e = r['start'], r['end']
        if orig[s:e] != r['old']:
            return None, f"anchor mismatch @{r['line']}: {orig[s:e]!r} != {r['old']!r}"
        if not in_math(s, e):
            return None, f"후보가 수식 영역 밖 @{r['line']}"
        new = new[:s] + r['new'] + new[e:]
        touched.append(r)

    # --- 게이트 1·2: 수식 밖 텍스트와 영역 구조 보존
    nsegs = segments(new)
    if len(nsegs) != len(segs):
        return None, f"수식 영역 개수 변화 {len(segs)} -> {len(nsegs)}"
    for (k1, a1, b1, _), (k2, a2, b2, _) in zip(segs, nsegs):
        if k1 != k2:
            return None, "수식/텍스트 배열 변화"
        if k1 == 'txt' and orig[a1:b1] != new[a2:b2]:
            return None, f"수식 밖 텍스트 변경: {orig[a1:b1][:60]!r}"
    # --- 게이트 3
    if orig.count('$') != new.count('$'):
        return None, "$ 개수 변화"
    # --- 게이트 4
    if katex is not None:
        probes = []
        for (k1, a1, b1, d1), (k2, a2, b2, d2) in zip(segs, nsegs):
            if k1 == 'math' and orig[a1:b1] != new[a2:b2]:
                probes.append({'tex': new[a2:b2], 'display': bool(d2)})
        bad = katex(probes)
        if bad:
            return None, "KaTeX 렌더 실패: " + '; '.join(bad[:2])
    return new, None


def make_katex_gate(macros_js):
    macros_js = os.path.abspath(macros_js)
    helper = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_katex_gate.js')
    node_modules = os.environ.get('DD_KATEX_MODULES', '')

    def gate(texs):
        if not texs:
            return []
        with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False,
                                         encoding='utf-8') as fh:
            json.dump({'macrosJs': macros_js, 'texs': texs}, fh)
            p = fh.name
        try:
            env = dict(os.environ)
            if node_modules:
                env['NODE_PATH'] = node_modules
            out = subprocess.run(['node', helper, p], capture_output=True,
                                 text=True, env=env, timeout=300)
            if out.returncode != 0:
                return ['gate 실행 실패: ' + out.stderr.strip()[:200]]
            return json.loads(out.stdout or '[]')
        finally:
            os.unlink(p)
    return gate


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cands')
    ap.add_argument('--decisions', help='JSON {id: "yes"/"no"} 또는 JSONL')
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--katex', help='katex-macros.js 경로 (지정 시 렌더 게이트)')
    ap.add_argument('--only', help='kind 필터 (쉼표: AUTO,MATHOP)')
    ap.add_argument('--diff-limit', type=int, default=40)
    a = ap.parse_args()

    rows = [json.loads(l) for l in open(a.cands, encoding='utf-8')]
    dec = {}
    if a.decisions:
        raw = open(a.decisions, encoding='utf-8').read().strip()
        if raw.startswith('{'):
            dec = json.loads(raw)
        else:
            for line in raw.split('\n'):
                if line.strip():
                    o = json.loads(line)
                    dec[o['id']] = o['verdict']

    kinds = set(a.only.split(',')) if a.only else {'AUTO', 'MATHOP', 'AMBIG'}
    picked = []
    for r in rows:
        if r['kind'] == 'NESTED' or r['kind'] not in kinds:
            continue
        if r['kind'] == 'AMBIG' and dec.get(r['id']) != 'yes':
            continue
        picked.append(r)

    katex = make_katex_gate(a.katex) if a.katex else None
    byf = collections.defaultdict(list)
    for r in picked:
        byf[r['file']].append(r)

    ok = fail = 0
    shown = 0
    stats = collections.Counter()
    for path in sorted(byf):
        new, err = apply_file(path, byf[path], katex)
        if err:
            fail += 1
            print(f"ABORT {path}: {err}", file=sys.stderr)
            continue
        ok += 1
        stats[path] = len(byf[path])
        orig = open(path, encoding='utf-8').read()
        if a.write:
            open(path, 'w', encoding='utf-8').write(new)
        elif shown < a.diff_limit:
            shown += 1
            d = list(difflib.unified_diff(orig.split('\n'), new.split('\n'),
                                          path, path, n=0, lineterm=''))
            print('\n'.join(d[:24]))
    print(f"\n{'적용' if a.write else 'dry-run'}: 파일 {ok}개 / 치환 {sum(stats.values())}건"
          f" / abort {fail}개", file=sys.stderr)
    if fail:
        sys.exit(1)


if __name__ == '__main__':
    main()
