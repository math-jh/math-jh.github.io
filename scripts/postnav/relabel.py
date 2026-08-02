#!/usr/bin/env python3
"""relabel — 라벨 번호 shift + 재라벨링 cascade (글 내부·en 짝·inbound 전파).

사용:
  relabel.py shift '<글지정>' --from 18 --by 2 [--apply]

동작: ko 글의 번호 ≥ from 인 모든 박스를 by만큼 밀고(전역 공유 카운터),
같은 매핑을 (1) 글 내부 라벨 정의 줄 (2) 글 내부 참조 링크 (3) 단독형 증명 귀속
(4) en 짝 파일 (5) inbound 인용 전체에 단일 패스로 전파한다.
기본은 dry-run diff. --apply 시에만 실제 쓰기 (대상 파일 git-clean 필수).

삽입 전 실행이 정석: shift로 번호 자리를 비운 뒤 새 박스를 삽입한다.
삭제는 박스를 지운 뒤 음수 --by로 당긴다 (dangling inbound는 REVIEW로 보고).

자동 치환하지 않고 REVIEW로만 보고: 링크 없는 맨텍스트 언급, 명시형 {#id}의
id 자체(표시 번호는 shift), 텍스트↔앵커 불일치 등 판단이 필요한 것 전부.
"""

from __future__ import annotations

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

from common import (
    CITATION_UNIT_RE, KIND_PREFIX, NUMBERED_ALT, PREFIX_KIND, ROOT,
    TEXT_LABEL_RE, Post, en_counterpart, in_spans, iter_posts,
    parse_labels, protected_spans,
)
from find_post import resolve_one, fail

REVIEW: list[str] = []

# 숫자 읽기(한자어)의 끝자리 받침: 조사 선택용. 0은 '십'(ㅂ)으로 끝난다.
_DIGIT_BATCHIM = {0: "ㅂ", 1: "ㄹ", 2: None, 3: "ㅁ", 4: None, 5: None,
                  6: "ㄱ", 7: "ㄹ", 8: "ㄹ", 9: None}
_JOSA_RE = re.compile(r"^(으로|은|는|이|가|을|를|과|와|로)")


def _josa_for(n: int, josa: str) -> str:
    b = _DIGIT_BATCHIM[n % 10]
    if josa in ("으로", "로"):
        return "로" if b in (None, "ㄹ") else "으로"
    pairs = {"은": ("은", "는"), "는": ("은", "는"), "이": ("이", "가"), "가": ("이", "가"),
             "을": ("을", "를"), "를": ("을", "를"), "과": ("과", "와"), "와": ("과", "와")}
    with_b, without_b = pairs[josa]
    return with_b if b else without_b


def josa_check(text: str, end_pos: int, old: int, new: int, rel: str, ln: int) -> None:
    """shift된 인용 링크 직후의 조사 — 받침 범주가 바뀌면 REVIEW (자동 수정 안 함)."""
    m = _JOSA_RE.match(text[end_pos:end_pos + 2])
    if not m:
        return
    j = m.group(1)
    if _josa_for(old, j) != _josa_for(new, j):
        REVIEW.append(f"{rel}:{ln}: 번호 {old}→{new} 뒤 조사 '{j}' → '{_josa_for(new, j)}' 확인 필요"
                      f" ('이'가 계사 이다/이며 어간이면 그대로 둘 것)")


def line_offsets(text: str) -> list[int]:
    offs = [0]
    for line in text.split("\n")[:-1]:
        offs.append(offs[-1] + len(line) + 1)
    return offs


def masked_segments(text: str) -> list[str]:
    return sorted(text[s:e] for s, e in protected_spans(text))


def shift_opening_lines(text: str, doc, mapping: dict[int, int], rel: str) -> list[tuple[int, int, str]]:
    """::: 여는 줄들(파서가 준 줄번호만)의 번호 shift → char-range 에딧 목록."""
    offs = line_offsets(text)
    lines = text.split("\n")
    edits = []

    def edit_line(lineno: int, new_line: str) -> None:
        old_line = lines[lineno - 1]
        if new_line != old_line:
            edits.append((offs[lineno - 1], offs[lineno - 1] + len(old_line), new_line))

    for b in doc.boxes:
        if b.number is None or b.number not in mapping:
            continue
        old_line = lines[b.line_start - 1]
        new_line, n = re.subn(
            rf"^(:::[ \t]+(?:[\w\-]+[ \t]+)?{re.escape(b.kind)}[ \t]+){b.number}(?!\d)",
            lambda m: f"{m.group(1)}{mapping[b.number]}", old_line, count=1)
        if n != 1:
            REVIEW.append(f"{rel}:{b.line_start}: 여는 줄 번호 치환 실패 — 수동 확인: {old_line!r}")
            continue
        edit_line(b.line_start, new_line)
        if b.explicit:
            REVIEW.append(f"{rel}:{b.line_start}: 명시형 {{#{b.anchor}}} — 표시 번호만 "
                          f"{b.number}→{mapping[b.number]} shift, id는 유지 (id 개명 여부 판단 필요)")
    for pr in doc.proofs:
        if not pr.standalone or not pr.target_text:
            continue
        tm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)$", pr.target_text.strip())
        if not tm:
            continue
        old = int(tm.group(2))
        if old not in mapping:
            continue
        old_line = lines[pr.line_start - 1]
        new_line = re.sub(rf"(\({re.escape(tm.group(1))}[ \t]+){old}(?!\d)",
                          lambda m: f"{m.group(1)}{mapping[old]}", old_line, count=1)
        edit_line(pr.line_start, new_line)
    return edits


def shift_citations(text: str, own_paths: set[str], target_paths: set[str],
                    mapping: dict[int, int], explicit_map: dict[str, tuple[str, int]],
                    rel: str, is_target_file: bool) -> list[tuple[int, int, str]]:
    """인용 단위 [<text>](<path>#<anchor>)의 번호+앵커 동시 shift.

    is_target_file: 대상 글 자신(ko/en) — path가 빈 값(#anchor)이거나 자기 permalink.
    inbound 파일 — path가 대상 permalink(ko/en)일 때만.
    """
    spans = protected_spans(text)
    offs = line_offsets(text)

    def lineno(pos: int) -> int:
        lo, hi = 0, len(offs) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if offs[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    edits = []
    for m in CITATION_UNIT_RE.finditer(text):
        if in_spans(m.start(), spans):
            continue
        path = m.group("path").rstrip("/")
        if is_target_file:
            if path and path not in own_paths:
                continue
        else:
            if path not in target_paths:
                continue
        aword, anum = m.group("anchor"), m.group("anum")
        body = m.group("text")

        if anum and aword in PREFIX_KIND:
            old = int(anum)
            if old not in mapping:
                continue
            new = mapping[old]
            # text 안에서 같은 접두의 종류+번호 — 마지막 출현(⁋ 위치)을 치환.
            cands = [t for t in TEXT_LABEL_RE.finditer(body)
                     if KIND_PREFIX.get(t.group(1)) == aword]
            if not cands:
                REVIEW.append(f"{rel}:{lineno(m.start())}: 앵커 #{aword}{old} 인데 텍스트에 "
                              f"대응 라벨 없음 — 수동 확인: {m.group(0)[:100]!r}")
                continue
            t = cands[-1]
            if int(t.group(2)) != old:
                REVIEW.append(f"{rel}:{lineno(m.start())}: 텍스트 '{t.group(0)}' ↔ 앵커 "
                              f"#{aword}{old} 불일치 — 기존 오류, 수동 수정 필요")
                continue
            new_body = body[:t.start(2)] + str(new) + body[t.end(2):]
            replaced = f"[{new_body}]({m.group('path')}#{aword}{new})"
            edits.append((m.start(), m.end(), replaced))
            josa_check(text, m.end(), old, new, rel, lineno(m.start()))
        else:
            # 명시형 id 앵커: id는 verbatim 유지, 표시 번호만 shift.
            full_id = aword + anum
            if full_id not in explicit_map:
                continue
            kind, old = explicit_map[full_id]
            if old not in mapping:
                continue
            cands = [t for t in TEXT_LABEL_RE.finditer(body)
                     if t.group(1) == kind and int(t.group(2)) == old]
            if not cands:
                continue
            t = cands[-1]
            new_body = body[:t.start(2)] + str(mapping[old]) + body[t.end(2):]
            edits.append((m.start(), m.end(), f"[{new_body}]({m.group('path')}#{full_id})"))
            REVIEW.append(f"{rel}:{lineno(m.start())}: 명시형 #{full_id} 참조 — 표시 번호만 "
                          f"{old}→{mapping[old]}, id 유지")
    return edits


def bare_text_scan(text: str, doc, mapping: dict[int, int], rel: str) -> None:
    """링크·::: 줄 밖의 종류+번호 평문 언급 — 치환하지 않고 REVIEW."""
    spans = list(protected_spans(text))
    offs = line_offsets(text)
    opening = {b.line_start for b in doc.boxes} | {p.line_start for p in doc.proofs}
    cited = [(m.start(), m.end()) for m in CITATION_UNIT_RE.finditer(text)]
    lines = text.split("\n")
    for m in TEXT_LABEL_RE.finditer(text):
        if int(m.group(2)) not in mapping:
            continue
        if in_spans(m.start(), spans) or any(s <= m.start() < e for s, e in cited):
            continue
        ln = next((i for i in range(len(offs) - 1, -1, -1) if offs[i] <= m.start()), 0) + 1
        if ln in opening:
            continue
        REVIEW.append(f"{rel}:{ln}: 링크 없는 평문 언급 '{m.group(0)}' — shift 여부 판단 필요: "
                      f"{lines[ln - 1].strip()[:100]!r}")


def apply_edits(text: str, edits: list[tuple[int, int, str]]) -> str:
    for s, e, _ in edits:
        for s2, e2, _ in edits:
            if (s, e) != (s2, e2) and s < e2 and s2 < e:
                fail(f"에딧 겹침 (내부 버그): {s}-{e} vs {s2}-{e2}")
    out = text
    for s, e, rep in sorted(edits, reverse=True):
        out = out[:s] + rep + out[e:]
    return out


def transform_file(post: Post, mapping, explicit_map, own_paths, target_paths,
                   is_target: bool) -> str | None:
    text = post.path.read_text(encoding="utf-8")
    edits = []
    if is_target:
        doc = parse_labels(text)
        edits += shift_opening_lines(text, doc, mapping, post.rel)
        bare_text_scan(text, doc, mapping, post.rel)
    edits += shift_citations(text, own_paths, target_paths, mapping, explicit_map,
                             post.rel, is_target)
    if not edits:
        return None
    new = apply_edits(text, edits)
    if masked_segments(text) != masked_segments(new):
        fail(f"{post.rel}: 보호 구간(수식·fence)이 변경됨 — abort")
    return new


def cmd_shift(args) -> None:
    posts = iter_posts()
    target, _ = resolve_one(args.post, posts, lang="ko")
    if target.lang != "ko":
        fail("ko 원본을 지정할 것 — en 짝은 자동으로 함께 처리된다")
    en = en_counterpart(target, posts)

    doc = parse_labels(target.path.read_text(encoding="utf-8"))
    nums = sorted({b.number for b in doc.boxes if b.number is not None})
    moving = [n for n in nums if n >= args.start]
    if not moving:
        fail(f"번호 ≥ {args.start} 인 박스가 없음 (실존: {nums})")
    mapping = {n: n + args.delta for n in moving}
    if min(mapping.values()) < 1:
        fail("shift 결과 번호가 1 미만이 됨")
    untouched = {n for n in nums if n < args.start}
    collide = untouched & set(mapping.values())
    if collide:
        fail(f"shift 결과 번호 충돌: {sorted(collide)} — 삭제가 덜 됐거나 delta 오류")

    explicit_map = {b.anchor: (b.kind, b.number) for b in doc.boxes
                    if b.explicit and b.number is not None}
    ko_pl = target.permalink.rstrip("/")
    en_pl = en.permalink.rstrip("/") if en else None
    target_paths = {p for p in (ko_pl, en_pl) if p}

    print(f"PLAN {target.rel}: {len(moving)}개 박스 shift "
          f"({moving[0]}..{moving[-1]} → {mapping[moving[0]]}..{mapping[moving[-1]]}, by={args.delta:+d})")

    changes: list[tuple[Post, str]] = []
    for p, is_target, own in ([(target, True, {ko_pl})] +
                              ([(en, True, {en_pl})] if en else [])):
        new = transform_file(p, mapping, explicit_map, own, target_paths, is_target)
        if new is not None:
            changes.append((p, new))
    if en is None:
        print("NOTE en 짝 없음 — ko만 처리")
    for p in posts:
        if p.path == target.path or (en and p.path == en.path):
            continue
        new = transform_file(p, mapping, explicit_map, set(), target_paths, False)
        if new is not None:
            changes.append((p, new))

    for p, new in changes:
        old = p.path.read_text(encoding="utf-8")
        diff = difflib.unified_diff(old.splitlines(keepends=True), new.splitlines(keepends=True),
                                    fromfile=p.rel, tofile=p.rel + " (shifted)")
        sys.stdout.writelines(diff)
        print()

    if REVIEW:
        print("── REVIEW (자동 치환 안 함 — 판단 필요) " + "─" * 30)
        for r in REVIEW:
            print("  " + r)

    print(f"SUMMARY 파일 {len(changes)}개 변경" + ("" if args.apply else " (dry-run — 쓰지 않음)"))
    if not args.apply:
        return

    files = [p.rel for p, _ in changes]
    dirty = subprocess.run(["git", "status", "--porcelain", "--", *files],
                           cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if dirty:
        fail("대상 파일에 미커밋 변경 있음 — 커밋 체크포인트 후 재실행:\n" + dirty)
    print("APPLY 대상: (IDE에 열린 파일이 있으면 버퍼 저장이 덮을 수 있음 — 닫고 실행할 것)")
    for f in files:
        print("  " + f)
    for p, new in changes:
        p.path.write_text(new, encoding="utf-8")
    # 사후 게이트: 대상 글 재파싱 — 번호 유일성.
    doc2 = parse_labels(target.path.read_text(encoding="utf-8"))
    nums2 = [b.number for b in doc2.boxes if b.number is not None]
    if len(nums2) != len(set(nums2)):
        print("ERROR shift 후 번호 중복 발견 — 즉시 확인 필요", file=sys.stderr)
        sys.exit(1)
    print("DONE")


def main() -> None:
    ap = argparse.ArgumentParser(prog="relabel")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("shift")
    s.add_argument("post")
    s.add_argument("--from", dest="start", type=int, required=True)
    s.add_argument("--by", dest="delta", type=int, required=True)
    s.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    cmd_shift(args)


if __name__ == "__main__":
    main()
