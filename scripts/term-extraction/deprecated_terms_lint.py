#!/usr/bin/env python3
"""영어화 확정 용어의 한국어형 잔존/신설 전수 검사.

source of truth 는 `_data/terms.yml` — `primary: en` 항목의 ko 형이 prose 에
남아 있으면 보고한다 (판정 로직은 .agents/hooks/md_lint.py 를 import, 단일 소스).
md_lint 훅이 편집 시점의 신설을 막는 실시간 가드라면, 이 스크립트는 배치 가드다.
스윕 완료 후 기준값은 0이어야 하며, 이후 0이 아니면 새 글이 오염된 것이다.

기본 대상은 published:false 초안 전체다 — 발행글의 잔존 한국어는 스윕 범위
판정(보수 규정)이 따로 있었으므로 `--all` 을 줄 때만 포함한다.
prose 한정: frontmatter·수식·코드·참고문헌(prose_lines) + 헤딩·링크 라벨·<sub> 제외.

사용: deprecated_terms_lint.py                   (초안 전체)
      deprecated_terms_lint.py --all             (발행글 포함)
      deprecated_terms_lint.py 파일...            (지정 파일만)
      deprecated_terms_lint.py --notify          (cron 용: 베이스라인 대비
                                                  신규 오염만 텔레그램 알림)
      deprecated_terms_lint.py --write-baseline  (현 잔존을 기지 보류분으로 기록)
종료코드: 잔존 있으면 1 (--notify 는 신규 있으면 1).
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, ".agents", "hooks"))
from md_lint import _DEPR, _depr_count  # noqa: E402
from terms_common import is_draft  # noqa: E402
from terms_usage_lint import prose_lines  # noqa: E402

if _DEPR is None:
    sys.exit("_data/terms.yml 로드 실패")
tier1, protected = _DEPR

# 초안 판정은 terms_common.is_draft 단일 출처 (이중 SoT 감사 [9], 2026-07-22).
BASELINE = os.path.join(HERE, "deprecated_baseline.txt")

FLAGS = {"--all", "--notify", "--write-baseline"}
args = [a for a in sys.argv[1:] if a not in FLAGS]
include_published = "--all" in sys.argv[1:]
notify = "--notify" in sys.argv[1:]
write_baseline = "--write-baseline" in sys.argv[1:]

if args:
    targets = args
else:
    targets = []
    for path in sorted(glob.glob(f"{ROOT}/_posts/Math/**/ko/*.md",
                                 recursive=True)):
        try:
            head = open(path, encoding="utf-8").read(2000)
        except OSError:
            continue
        if include_published or is_draft(head):
            targets.append(path)

total = 0
keys = set()
rows = []
for path in targets:
    per = {}
    try:
        lines = list(prose_lines(path))
    except OSError:
        continue
    for ln, text in lines:
        if text.lstrip().startswith("#"):
            continue  # 헤딩의 한국어는 보호구역 (헤더 변경 금지 규칙)
        got = _depr_count(text, tier1, protected)
        for w, n in got.items():
            per.setdefault(w, []).append((ln, n))
    if per:
        rel = os.path.relpath(path, ROOT)
        for w, hits in sorted(per.items()):
            n = sum(c for _, c in hits)
            total += n
            keys.add(f"{rel}|{w}")
            lns = ",".join(str(ln) for ln, _ in hits[:6])
            rows.append(f"{rel}: '{w}'→{tier1[w]} ×{n} (L{lns})")
            print(rows[-1])
print(f"-- 한국어형 잔존 {total}건 / {len(targets)}파일")

if write_baseline:
    with open(BASELINE, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(keys)) + "\n")
    print(f"베이스라인 {len(keys)}키 기록 → {BASELINE}")
    sys.exit(0)

if notify:
    # 기지 보류분(베이스라인)은 무시하고 신규 오염만 알린다
    try:
        base = {l.strip() for l in open(BASELINE, encoding="utf-8") if l.strip()}
    except OSError:
        base = set()
    new = sorted(keys - base)
    if new:
        from terms_lint import send_notify
        ex = ", ".join(k.split("|")[1] for k in new[:5])
        send_notify(f"영어화 확정 용어의 한국어형 신규 {len(new)}건: "
                    f"{ex}{' …' if len(new) > 5 else ''} "
                    f"(deprecated_terms_lint.py 로 확인)",
                    subject="[용어 린트]")
        print(f"신규 {len(new)}건 알림")
    sys.exit(1 if new else 0)

sys.exit(1 if total else 0)
