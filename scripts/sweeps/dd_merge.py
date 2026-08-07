#!/usr/bin/env python3
r"""에이전트 판정을 모아 커버리지를 검증하고 하나의 결정 파일로 합친다.

빠진 아이디·모르는 아이디·중복을 전부 보고한다. 판정이 없는 후보는 자동으로
치환에서 빠지므로(dd_apply 가 yes 만 적용) 안전하지만, 커버리지가 100%가
아니면 그 사실을 드러내는 것이 이 스크립트의 목적이다.
"""
import argparse, collections, glob, json, os, sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cands')
    ap.add_argument('decdir')
    ap.add_argument('-o', '--out', required=True)
    a = ap.parse_args()

    rows = [json.loads(l) for l in open(a.cands, encoding='utf-8')]
    amb = {r['id']: r for r in rows if r['kind'] == 'AMBIG'}

    dec, dup, unknown = {}, [], []
    for p in sorted(glob.glob(os.path.join(a.decdir, '*.jsonl'))):
        for ln, line in enumerate(open(p, encoding='utf-8'), 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                print(f'  !! 파싱 실패 {p}:{ln}', file=sys.stderr)
                continue
            i, v = o.get('id'), o.get('verdict')
            if i not in amb:
                unknown.append((p, i))
                continue
            if i in dec and dec[i] != v:
                dup.append((i, dec[i], v))
            dec[i] = v

    missing = sorted(set(amb) - set(dec))
    cnt = collections.Counter(dec.values())
    print(f'AMBIG 후보 {len(amb)}건', file=sys.stderr)
    for k, v in sorted(cnt.items()):
        print(f'   {k:8s}{v:6d}', file=sys.stderr)
    print(f'   {"미판정":8s}{len(missing):6d}', file=sys.stderr)
    if unknown:
        print(f'   모르는 id {len(unknown)}건 (예: {unknown[:3]})', file=sys.stderr)
    if dup:
        print(f'   판정 충돌 {len(dup)}건 (예: {dup[:3]})', file=sys.stderr)

    with open(a.out, 'w', encoding='utf-8') as fh:
        json.dump(dec, fh, ensure_ascii=False, indent=0)

    # unsure·미판정 목록은 사람이 볼 수 있게 따로
    review = os.path.splitext(a.out)[0] + '_review.md'
    with open(review, 'w', encoding='utf-8') as fh:
        fh.write('# 사람이 봐야 하는 항목\n\n')
        for label, ids in (('unsure', [i for i, v in dec.items() if v == 'unsure']),
                           ('미판정', missing)):
            fh.write(f'## {label} ({len(ids)}건)\n\n')
            for i in sorted(ids):
                r = amb[i]
                fh.write(f"- `{i}` {r['file']}:{r['line']} — `{r['old']}`\n"
                         f"  - 문맥: `{r.get('context','')[:120]}`\n")
            fh.write('\n')
    print(f'-> {a.out} / {review}', file=sys.stderr)


if __name__ == '__main__':
    main()
