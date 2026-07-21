#!/usr/bin/env python3
"""terms.yml 의 primary(굵은 쪽 = 본문 주표기)를 실제 본문 사용과 대조한다.

1단계 도구: 글을 고치는 게 아니라 **데이터를 본문에 맞추는** 통계 모드.
KO 글 전체에서 각 entry 의 en형/ko형 출현 횟수를 세고, 본문이 압도적으로
반대쪽을 쓰는데 primary 가 어긋난 entry 를 flip 후보로 보고한다.
(옛 Index_ko 시절 기본값 en 이 그대로 남아 환·군·체·사상·층 같은 단어가
en-primary 로 기록된 것이 발단 — 2026-07-18.)

report 전용: terms.yml 도 글도 수정하지 않는다.

사용:  python3 terms_usage_lint.py [--json OUT] [--entry ID ...]

집계 규칙 (본문 = prose 만):
- frontmatter 는 description 값만 prose 로 취급 (title 은 표기 규약이 따로 있다)
- 코드 펜스·인라인 코드·수식($…$, $$…$$, 멀티라인 $$ 블록)·<sub>…</sub>·
  마크다운 링크 전체([라벨](url) — 라벨은 남의 제목 인용)·HTML 태그 제외
- **참고문헌** 이후는 통째로 제외 (영문 서지에 용어가 그대로 들어 있다)
- 긴 용어 우선 매칭: "자유가환군" 이 잡히면 그 안의 "가환군" 은 세지 않는다
- 한글형 경계: 앞 글자가 한글이면 무효(상호작용≠작용). 뒤 글자는 조사/어미
  머리글자일 때만 허용 — "환의"는 세고 "환경"은 안 센다. 단음절 용어(군·환·체)
  의 노이즈를 막는 대신 "생성한다" 류 동사 활용은 일부 놓친다(방향 판정에는 충분).
- 영문형 경계: 양옆이 영숫자가 아닐 것 (대소문자 무시)
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from terms_common import is_draft as _tc_is_draft  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TERMS_YML = os.path.join(ROOT, "_data", "terms.yml")
POST_GLOB = os.path.join(ROOT, "_posts", "Math", "**", "ko", "*.md")

HANGUL = re.compile(r"[가-힣]")
# 용어 뒤에 붙어도 같은 용어로 인정하는 조사/어미의 머리글자.
# (완전한 형태소 분석 대신, 방향 판정에 충분한 보수적 근사)
PARTICLE_HEADS = set("이가을를은는의에와과도로만들으처럼부까지라야든서")
VERB_HEADS = set("하한할함해했되된될됨돼")  # ~하다/~되다 활용 (작용하는, 생성된)

RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_MATH_DISPLAY = re.compile(r"\$\$.*?\$\$")
RE_MATH_INLINE = re.compile(r"\$[^$\n]*\$")
RE_SUB = re.compile(r"<sub>.*?</sub>", re.I | re.S)
RE_LINK = re.compile(r"!?\[[^\]]*\]\([^)]*\)")
RE_TAG = re.compile(r"<[^>]+>")
RE_REFS = re.compile(r"^(\*\*참고문헌\*\*|#{1,6}\s*참고문헌)")
RE_FENCE = re.compile(r"^\s*(```|~~~)")


def load_entries():
    data = yaml.safe_load(open(TERMS_YML, encoding="utf-8"))
    out = []
    for _group, lst in (data or {}).items():
        for t in lst or []:
            out.append(t)
    return out


def clean_line(line: str) -> str:
    line = RE_INLINE_CODE.sub(" ", line)
    line = RE_MATH_DISPLAY.sub(" ", line)  # 인라인 $$…$$ (옛 글) 먼저
    line = RE_MATH_INLINE.sub(" ", line)
    line = RE_SUB.sub(" ", line)
    line = RE_LINK.sub(" ", line)
    line = RE_TAG.sub(" ", line)
    return line


def is_draft(path: str) -> bool:
    """frontmatter 에 published: false 가 있으면 초안(LLM 작성분 포함).
    판정 자체는 단일 출처 terms_common.is_draft (이중 SoT 감사 [9], 2026-07-22)."""
    with open(path, encoding="utf-8") as f:
        head = f.read(2000)
    return _tc_is_draft(head)


def prose_lines(path: str):
    """(lineno, cleaned_text) 를 낸다. 수식 블록·코드 펜스·참고문헌 이후 제외."""
    lines = open(path, encoding="utf-8").read().split("\n")
    i = 0
    # frontmatter 는 통째로 건너뛴다. description 도 제목처럼 "의도된 한글"
    # 문맥으로 치기로 확정 (사용자, 2026-07-18) — 사용례로 세지 않는다.
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1

    in_fence = in_math = in_raw = False
    for j in range(i, len(lines)):
        raw = lines[j]
        if RE_REFS.match(raw.strip()):
            return
        if "{% raw %}" in raw:
            in_raw = True
        if "{% endraw %}" in raw:
            in_raw = False
            continue
        if in_raw:
            continue
        if RE_FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # 헤딩 제외: 제목·h2 헤딩의 한글은 의도된 표기라 사용례로 안 센다
        # (사용자 확정 2026-07-18 — en-primary 용어도 헤딩에선 한글이 정당)
        if re.match(r"#{1,6}\s", raw):
            continue
        stripped = RE_MATH_DISPLAY.sub(" ", raw)
        if stripped.count("$$") % 2 == 1:  # 멀티라인 $$ 블록 여닫이
            in_math = not in_math
            continue
        if in_math:
            continue
        yield j + 1, clean_line(raw)


def build_matcher(entries):
    """form 문자열 → 소유 entry 들. 긴 form 우선의 단일 alternation 정규식."""
    owners: dict[str, list] = {}
    for t in entries:
        for side in ("en", "ko"):
            form = (t.get(side) or "").strip()
            if not form or "$" in form:  # 수식 표제어는 본문 매칭 불가
                continue
            owners.setdefault(form, []).append((side, t))
    forms = sorted(owners, key=len, reverse=True)
    rx = re.compile("|".join(re.escape(f) for f in forms), re.IGNORECASE)
    # IGNORECASE 매치 원문 → 정식 form 복원용
    canon = {f.lower(): f for f in forms}
    return rx, owners, canon


def boundary_ok(text: str, start: int, end: int, form: str) -> bool:
    prev = text[start - 1] if start > 0 else " "
    nxt = text[end] if end < len(text) else " "
    if HANGUL.match(form[0]):
        if HANGUL.match(prev):
            return False
        if HANGUL.match(nxt) and nxt not in PARTICLE_HEADS and nxt not in VERB_HEADS:
            return False
        return True
    # 영문형
    if prev.isalnum() or nxt.isalnum():
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="원자료(entry 별 counts)를 JSON 으로 저장")
    ap.add_argument("--entry", nargs="*", help="이 id 들의 매치 위치를 file:line 으로 출력")
    args = ap.parse_args()

    entries = load_entries()
    rx, owners, canon = build_matcher(entries)

    # 발행글/초안을 나눠 센다: 판정(primary 가 맞는가)은 발행글만으로 하고,
    # 초안은 "사용자 선호(=발행글 관례)에서 얼마나 벗어났나"의 대상으로 본다.
    counts: dict[str, int] = {}          # form → 발행글 count
    counts_d: dict[str, int] = {}        # form → 초안(published:false) count
    sites: dict[str, list] = {}          # form → [(file, line)]  (--entry 용)
    files = sorted(glob.glob(POST_GLOB, recursive=True))
    n_draft = 0
    for path in files:
        rel = os.path.relpath(path, ROOT)
        draft = is_draft(path)
        n_draft += draft
        tgt = counts_d if draft else counts
        for lineno, text in prose_lines(path):
            for m in rx.finditer(text):
                form = canon.get(m.group(0).lower(), m.group(0))
                if not boundary_ok(text, m.start(), m.end(), form):
                    continue
                tgt[form] = tgt.get(form, 0) + 1
                sites.setdefault(form, []).append((rel, lineno))

    # entry 별 판정 — 발행글 카운트로만
    rows = []
    for t in entries:
        en, ko = (t.get("en") or "").strip(), (t.get("ko") or "").strip()
        cur = "ko" if t.get("primary") == "ko" else "en"
        c_en = counts.get(en, 0) if en and "$" not in en else None
        c_ko = counts.get(ko, 0) if ko and "$" not in ko else None
        if c_en is None or c_ko is None or not en or not ko:
            continue  # 한쪽이 수식/공백이면 방향 판정 불가
        d_en = counts_d.get(en, 0)
        d_ko = counts_d.get(ko, 0)
        total = c_en + c_ko
        dom = "en" if c_en >= c_ko else "ko"
        share = (max(c_en, c_ko) / total) if total else 0.0
        if total == 0:
            verdict = "NO-DATA"
        elif dom == cur:
            verdict = "OK"
        elif total >= 5 and share >= 0.9:
            verdict = "FLIP-STRONG"
        elif total >= 3 and share >= 0.7:
            verdict = "FLIP-LEAN"
        else:
            verdict = "MIXED"
        # 초안 이탈: 발행글 관례가 뚜렷한데(≥5회, ≥80%) 초안이 반대쪽을 3회 이상,
        # 그리고 초안 내에서도 그 반대쪽이 다수일 때
        drift = ""
        if total >= 5 and share >= 0.8:
            opp = "ko" if dom == "en" else "en"
            d_opp = d_ko if opp == "ko" else d_en
            d_dom = d_en if opp == "ko" else d_ko
            if d_opp >= 3 and d_opp > d_dom:
                drift = f"draft→{opp} {d_opp}:{d_dom}"
        rows.append({
            "id": t.get("id"), "en": en, "ko": ko, "primary": cur,
            "count_en": c_en, "count_ko": c_ko,
            "draft_en": d_en, "draft_ko": d_ko,
            "verdict": verdict, "share": round(share, 2), "drift": drift,
        })

    order = {"FLIP-STRONG": 0, "FLIP-LEAN": 1, "MIXED": 2, "OK": 3, "NO-DATA": 4}
    rows.sort(key=lambda r: (order[r["verdict"]], -(r["count_en"] + r["count_ko"])))

    n = {k: sum(1 for r in rows if r["verdict"] == k) for k in order}
    print(f"KO 글 {len(files)}개 스캔 (발행 {len(files) - n_draft} · 초안 {n_draft}),"
          f" 판정 가능 entry {len(rows)}개 — 판정은 발행글 기준")
    print(f"  OK {n['OK']}  FLIP-STRONG {n['FLIP-STRONG']}  FLIP-LEAN {n['FLIP-LEAN']}"
          f"  MIXED {n['MIXED']}  NO-DATA {n['NO-DATA']}")
    for verdict in ("FLIP-STRONG", "FLIP-LEAN", "MIXED"):
        sel = [r for r in rows if r["verdict"] == verdict]
        if not sel:
            continue
        print(f"\n== {verdict} ({len(sel)}) ==")
        for r in sel:
            cur_form = r[r"primary"]
            print(f"  {r['id']:44s} en:{r['count_en']:4d} ko:{r['count_ko']:4d}"
                  f"  (초안 en:{r['draft_en']:4d} ko:{r['draft_ko']:4d})"
                  f"  primary={r['primary']}({cur_form})")

    drifted = [r for r in rows if r["drift"]]
    drifted.sort(key=lambda r: -(r["draft_en"] + r["draft_ko"]))
    if drifted:
        print(f"\n== DRAFT-DRIFT ({len(drifted)}) — 발행글 관례는 뚜렷한데 초안이 반대쪽 ==")
        for r in drifted:
            print(f"  {r['id']:44s} 발행 en:{r['count_en']:4d} ko:{r['count_ko']:4d}"
                  f"  초안 en:{r['draft_en']:4d} ko:{r['draft_ko']:4d}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=1)
        print(f"\nJSON: {args.json}")

    if args.entry:
        by_id = {r["id"]: r for r in rows}
        for eid in args.entry:
            r = by_id.get(eid)
            if not r:
                print(f"\n-- {eid}: 판정 불가/없음")
                continue
            print(f"\n-- {eid} --")
            for side in ("en", "ko"):
                form = r[side]
                locs = sites.get(form, [])
                print(f"  {side} {form!r} × {len(locs)}")
                for f_, l_ in locs[:10]:
                    print(f"    {f_}:{l_}")


if __name__ == "__main__":
    main()
