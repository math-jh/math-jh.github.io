#!/usr/bin/env python3
"""en→ko flip 후보 검토 파일 생성 (1회성 보조 도구).

primary=en 인데 발행글에서 ko 형이 우세한 entry 를, 발행글의 실제 위치와 함께
markdown 으로 뽑는다. 사용자가 "영어로 썼어야 하는데 검수에서 놓친 것"인지
"정당한 한글 관례"인지 가려 결정하는 용도. terms.yml 은 수정하지 않는다.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from terms_usage_lint import (ROOT, POST_GLOB, load_entries, build_matcher,
                              boundary_ok, prose_lines, is_draft)
import glob

# 통계 무효/규칙 확정으로 목록에서 뺀 것 (이유 병기)
EXCLUDED = {
    # 2026-07-18 사용자 분류 케이스 1: 일상용어와 구별 불가 — 탐지 제외
    "simple": "일상용어 구별 불가 (사용자 확정)",
    "image": "일상용어 구별 불가 (사용자 확정)",
    "face": "일상용어 구별 불가 (사용자 확정)",
    "equivalent": "일상용어 구별 불가 (사용자 확정)",
    # 케이스 4: 개별 룰 확정
    "extension": "명사/동사 룰 — 명사는 extension, '확장한다' 동사는 한글 (action 과 동일)",
    "pairing": "일상용어 구별 불가 + ko 표기는 '짝지음' (2026-07-18 terms.yml 반영)",
    "tangent_vector": "카테고리 조건부 — Calculus 는 접벡터 유지, 나머지는 영어",
    "bounded": "카테고리 조건부 — Calculus 는 유계 유지, 나머지는 영어",
    "bounded_above": "카테고리 조건부 — bounded 와 동일",
    "bounded_below": "카테고리 조건부 — bounded 와 동일",
    "generate": "폴리세미 — '생성한다' 일상 동사와 구분 불가 (span 과 ko 공유)",
    "span": "폴리세미 — generate 와 동일",
    "split": "폴리세미 — '~로 분해된다' 일반 동사",
    "least": "폴리세미 — '최소한' 등 일상어",
    "greatest": "폴리세미 — '최대한' 등 일상어",
    "phase_space": "동음이의어 확정 — 위상(phase)공간, topological space 와 별개 (2026-07-18)",
    "isomorphic": "사용자 룰 확정 — 영어(isomorphic) 사용, 본문 '동형'이 비표준",
    "commute": "사용자 룰 확정 — 영어(commute) 사용",
    "limit": "동음이의어 룰 확정 — categorical limit 은 영어, 해석학 수열 극한은 한글",
    "action": "명사/동사 룰 확정 — 명사 action 영어, '작용한다' 동사는 한글",
    "representation": "폴리세미 — '~로 표현된다' 일반 동사가 대부분",
    "restriction": "폴리세미 — '제한' 일상어",
    "slice": "폴리세미 — '조각' 일상어",
    "transposition": "폴리세미 — '호환되는'(compatible) 과 충돌",
    "interior": "준폴리세미 — 위상 용어로는 진성이나 '내부' 일상어 혼입",
    "retract": "retraction 과 ko '수축' 공유 — 방향이 서로 반대라 개별 판단 필요",
    "retraction": "retract 와 ko '수축' 공유 — 동일",
    "decreasing": "짝 불일치 — increasing(3:18)은 ko 우세, decreasing(10:4)은 en 우세. 쌍으로 결정 필요",
    "increasing": "decreasing 과 쌍으로 결정 필요",
}

entries = load_entries()
rx, owners, canon = build_matcher(entries)

# 발행글에서만 ko 형 위치 수집
want_forms = set()
cand = []
for t in entries:
    en, ko = (t.get("en") or "").strip(), (t.get("ko") or "").strip()
    if not en or not ko or "$" in en or "$" in ko:
        continue
    if t.get("primary") == "ko":
        continue
    cand.append(t)
    want_forms.add(ko)

hits = {}   # ko form → [(file, line, 발췌)]
cnt_en = {}
for path in sorted(glob.glob(POST_GLOB, recursive=True)):
    if is_draft(path):
        continue
    rel = os.path.relpath(path, ROOT)
    for lineno, text in prose_lines(path):
        for m in rx.finditer(text):
            form = canon.get(m.group(0).lower(), m.group(0))
            if not boundary_ok(text, m.start(), m.end(), form):
                continue
            if form in want_forms:
                ctx = text[max(0, m.start() - 25):m.end() + 25].strip()
                hits.setdefault(form, []).append((rel, lineno, ctx))
            cnt_en[form] = cnt_en.get(form, 0) + 1

out = ["# primary en→ko flip 후보 검토 (2026-07-18)", "",
       "발행글에서 ko 형이 en 형보다 많이 쓰인 en-primary entry. "
       "'영어로 썼어야 하는데 놓친 것'이면 본문 쪽을 고치고(entry 유지), "
       "정당한 한글 관례면 primary 를 ko 로 바꾼다. 이 파일은 보고서일 뿐 아무것도 안 바꿈.", ""]
rows = []
for t in cand:
    en, ko = t["en"].strip(), t["ko"].strip()
    k = len(hits.get(ko, []))
    e = cnt_en.get(en, 0)
    if k > e and k >= 3 and t["id"] not in EXCLUDED:
        rows.append((k, e, t))
rows.sort(key=lambda r: -r[0])

for k, e, t in rows:
    out.append(f"## {t['id']}  —  {t['en']} · {t['ko']}  (발행 en:{e} ko:{k})")
    for rel, ln, ctx in hits[t["ko"].strip()][:6]:
        out.append(f"- `{rel}:{ln}` — …{ctx}…")
    if k > 6:
        out.append(f"- (+{k - 6}곳)")
    out.append("")

out.append("## 목록에서 제외한 것 (이유)")
for eid, why in EXCLUDED.items():
    out.append(f"- **{eid}**: {why}")
out.append("")

dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "primary_flip_review.md")
open(dst, "w", encoding="utf-8").write("\n".join(out))
print(f"{dst}: 후보 {len(rows)}개")
