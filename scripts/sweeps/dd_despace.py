#!/usr/bin/env python3
r"""`\dd` 바로 앞에 남은 수동 간격을 제거한다.

`\dd{...}` 는 `\mathop{d...}` 로 앞쪽 thin space 를 스스로 넣으므로, 예전에 손으로
넣어 둔 `\,` `\;` `\:` 가 그대로 남으면 간격이 겹친다. 음수 간격 `\!` 는 의도적인
커닝일 수 있어 건드리지 않는다.

dd_apply 의 게이트(수식 밖 불변·영역 보존·`$` 개수·KaTeX 렌더)를 그대로 쓴다.
기본은 dry-run, 실제로 쓰려면 --write.
"""
import argparse, collections, difflib, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dd_extract import math_spans
from dd_apply import apply_file, make_katex_gate

PAT = re.compile(r'\\[,;:]\s*(?=\\dd\{)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--katex')
    ap.add_argument('--diff-limit', type=int, default=3)
    a = ap.parse_args()

    katex = make_katex_gate(a.katex) if a.katex else None
    rows = collections.defaultdict(list)
    for path in sorted(glob.glob('_posts/**/*.md', recursive=True)):
        text = open(path, encoding='utf-8').read()
        for s, e, _ in math_spans(text):
            for m in PAT.finditer(text, s, e):
                rows[path].append(dict(file=path, start=m.start(), end=m.end(),
                                       old=m.group(0), new='',
                                       line=text.count('\n', 0, m.start()) + 1))
    ok = fail = shown = 0
    n = 0
    for path in sorted(rows):
        new, err = apply_file(path, rows[path], katex)
        if err:
            fail += 1
            print(f'ABORT {path}: {err}', file=sys.stderr)
            continue
        ok += 1
        n += len(rows[path])
        if a.write:
            open(path, 'w', encoding='utf-8').write(new)
        elif shown < a.diff_limit:
            shown += 1
            orig = open(path, encoding='utf-8').read()
            d = list(difflib.unified_diff(orig.split('\n'), new.split('\n'),
                                          path, path, n=0, lineterm=''))
            print('\n'.join(d[:8]))
    print(f"\n{'적용' if a.write else 'dry-run'}: 파일 {ok}개 / 제거 {n}건 / abort {fail}개",
          file=sys.stderr)
    if fail:
        sys.exit(1)


if __name__ == '__main__':
    main()
