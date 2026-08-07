#!/usr/bin/env python3
r"""AMBIG 후보를 에이전트 판정용 배치 파일로 묶는다.

파일 단위가 아니라 **줄 단위**로 묶는다 — 한 줄에 여러 후보가 있으면 한 번에
보여주는 편이 문맥 판단에 유리하고 배치 수도 줄어든다. 배치는 카테고리로
나눠 한 에이전트가 비슷한 수학만 보게 한다.
"""
import argparse, collections, glob, json, os, re, sys

MARK_L, MARK_R = '«', '»'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cands')
    ap.add_argument('-o', '--outdir', required=True)
    ap.add_argument('--per-batch', type=int, default=70, help='배치당 줄 수')
    a = ap.parse_args()

    rows = [json.loads(l) for l in open(a.cands, encoding='utf-8')]
    amb = [r for r in rows if r['kind'] == 'AMBIG']

    # (파일, 줄) 로 묶고 그 줄 원문에 후보를 표시
    byline = collections.defaultdict(list)
    for r in amb:
        byline[(r['file'], r['line'])].append(r)

    filecache = {}
    items = []
    for (path, line), rs in sorted(byline.items()):
        if path not in filecache:
            filecache[path] = open(path, encoding='utf-8').read().split('\n')
        text = filecache[path][line - 1]
        # 줄 안에서의 offset 으로 변환하기 위해 파일 오프셋 기준 줄 시작을 구한다
        full = '\n'.join(filecache[path])
        lstart = sum(len(x) + 1 for x in filecache[path][:line - 1])
        marked = text
        for r in sorted(rs, key=lambda r: r['start'], reverse=True):
            s, e = r['start'] - lstart, r['end'] - lstart
            if not (0 <= s < e <= len(text)) or text[s:e] != r['old']:
                r['_bad'] = True
                continue
            marked = (marked[:s] + MARK_L + r['id'] + ':' + marked[s:e] + MARK_R
                      + marked[e:])
        good = [r for r in rs if not r.get('_bad')]
        if not good:
            continue
        items.append(dict(file=path, line=line, ids=[r['id'] for r in good],
                          marked=marked))

    cat = lambda p: p.split('/')[2] if p.startswith('_posts/Math') else 'Misc'
    bycat = collections.defaultdict(list)
    for it in items:
        bycat[cat(it['file'])].append(it)

    os.makedirs(a.outdir, exist_ok=True)
    for f in glob.glob(os.path.join(a.outdir, 'batch_*.md')):
        os.remove(f)
    n = 0
    manifest = []
    for c in sorted(bycat):
        chunk = bycat[c]
        for k in range(0, len(chunk), a.per_batch):
            n += 1
            part = chunk[k:k + a.per_batch]
            ids = [i for it in part for i in it['ids']]
            p = os.path.join(a.outdir, f'batch_{n:02d}.md')
            with open(p, 'w', encoding='utf-8') as fh:
                fh.write(f'# batch {n:02d} — {c} ({len(part)}줄 / 후보 {len(ids)}건)\n\n')
                for it in part:
                    fh.write(f"## {it['file']}:{it['line']}\n")
                    fh.write(it['marked'].strip() + '\n\n')
            manifest.append(dict(batch=n, path=p, category=c,
                                 lines=len(part), cands=len(ids), ids=ids))
    with open(os.path.join(a.outdir, 'manifest.json'), 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    tot = sum(m['cands'] for m in manifest)
    print(f'배치 {n}개 / 줄 {len(items)} / 후보 {tot}건', file=sys.stderr)
    for m in manifest:
        print(f"  batch_{m['batch']:02d}  {m['category']:24s} 줄{m['lines']:4d} 후보{m['cands']:5d}",
              file=sys.stderr)


if __name__ == '__main__':
    main()
