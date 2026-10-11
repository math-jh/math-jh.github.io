#!/usr/bin/env python3
"""개정 초안이 원본 글의 문단을 글자 단위로 보존했는지 대조한다.

새 개념 글 절차(_posts/Math/Gromov_Witten_Theory/CLAUDE.md '새 개념 글' 7번)의
보존 검사다. 원본 글 본문(frontmatter 아래)과 초안의 본문(시작·끝 마커 사이)을
빈 줄 기준 블록으로 나누고, 양쪽에서 짝을 찾지 못한 블록을 나열한다.

  - 원본에만 있는 블록: 초안에서 지웠거나 다시 쓴 문단
  - 초안에만 있는 블록: 새로 쓴 문단, 또는 원본 문단을 고친 결과

대조 전에 초안의 `<!-- 생략 … -->` 주석과 행 끝 공백을 지운다. 포팅 때 relabel로
바뀔 글 안 라벨은 --map으로 원본 쪽에 미리 적용한다 (예: prop3=prop11,def2=def3).
다른 글을 가리키는 링크(`/ko/...#prop3`)의 앵커는 바꾸지 않는다.

사용법:
  python3 scripts/dev/draft_preserve_check.py <원본.md> <draft.md> [--map prop3=prop11,...]
      [--declared <목록 파일>]

--declared에는 초안 작성자가 "다시 쓰거나 새로 쓴 블록"이라고 신고한 목록을 준다.
한 줄에 블록 첫머리 문자열 하나씩 적으며, 초안에만 있는 블록 중 어느 줄로도 시작하지
않는 것은 '신고 없이 바뀐 블록'으로 따로 표시한다.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

START = re.compile(r"<!--\s*=+\s*본문 시작\s*=+\s*-->")
END = re.compile(r"<!--\s*=+\s*본문 끝\s*=+\s*-->")
OMIT = re.compile(r"\s*<!--\s*생략.*?-->", re.S)

KIND = {
    "def": "정의", "prop": "명제", "thm": "정리", "lem": "보조정리",
    "cor": "따름정리", "ex": "예시", "rmk": "참고",
}


def post_body(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def draft_body(text: str) -> str:
    s, e = START.search(text), END.search(text)
    if not s or not e:
        sys.exit("초안에 본문 시작·끝 마커가 없다")
    return text[s.end():e.start()]


def apply_map(text: str, mapping: dict[str, str]) -> str:
    # 두 단계 치환으로 prop3→prop11, prop11→prop12 같은 연쇄 충돌을 피한다.
    tokens = {}
    for i, (old, new) in enumerate(mapping.items()):
        mo, mn = re.fullmatch(r"([a-z]+)(\d+)", old), re.fullmatch(r"([a-z]+)(\d+)", new)
        if not mo or not mn or mo.group(1) not in KIND or mn.group(1) not in KIND:
            sys.exit(f"--map 항목을 해석할 수 없다: {old}={new}")
        ko_old = f"{KIND[mo.group(1)]} {mo.group(2)}"
        ko_new = f"{KIND[mn.group(1)]} {mn.group(2)}"
        tok = f"\x00{i}\x00"
        tokens[tok] = (new, ko_new)
        # 글 안 링크: [명제 3](#prop3)
        text = re.sub(rf"\[{re.escape(ko_old)}\]\(#{old}\)", f"[{tok}K](#{tok}A)", text)
        # 정리 박스 머리: ::: 명제 3 ...
        text = re.sub(rf"(?m)^(:::\s+){re.escape(ko_old)}(?=\s|$)", rf"\g<1>{tok}K", text)
    for tok, (new, ko_new) in tokens.items():
        text = text.replace(f"{tok}K", ko_new).replace(f"{tok}A", new)
    return text


def blocks(text: str) -> list[tuple[int, str]]:
    out, cur, start = [], [], 0
    lines = text.split("\n")
    for i, line in enumerate(lines + [""]):
        if line.strip() == "":
            if cur:
                out.append((start, "\n".join(l.rstrip() for l in cur)))
                cur = []
        else:
            if not cur:
                start = i + 1
            cur.append(line)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("original")
    ap.add_argument("draft")
    ap.add_argument("--map", default="")
    ap.add_argument("--declared")
    a = ap.parse_args()

    mapping = dict(p.split("=", 1) for p in a.map.split(",") if p.strip())
    orig = apply_map(post_body(Path(a.original).read_text()), mapping)
    draft = OMIT.sub("", draft_body(Path(a.draft).read_text()))

    ob, db = blocks(orig), blocks(draft)
    oset, dset = {b for _, b in ob}, {b for _, b in db}
    only_o = [(n, b) for n, b in ob if b not in dset]
    only_d = [(n, b) for n, b in db if b not in oset]

    declared = []
    if a.declared:
        declared = [l.strip() for l in Path(a.declared).read_text().splitlines() if l.strip()]

    def head(b: str) -> str:
        return b.replace("\n", " ")[:90]

    print(f"원본 블록 {len(ob)}개 중 보존 {len(ob) - len(only_o)}개, 초안 블록 {len(db)}개 중 새 블록 {len(only_d)}개\n")
    print(f"[원본에만 있는 블록: {len(only_o)}] (원본 본문 기준 줄번호)")
    for n, b in only_o:
        print(f"  L{n}: {head(b)}")
    print(f"\n[초안에만 있는 블록: {len(only_d)}] (초안 본문 마커 다음 줄부터 센 줄번호)")
    undeclared = []
    for n, b in only_d:
        mark = ""
        if declared and not any(b.startswith(d) for d in declared):
            mark = "  ← 신고 없음"
            undeclared.append(n)
        print(f"  L{n}: {head(b)}{mark}")
    if declared:
        print(f"\n신고 없이 바뀐 블록: {len(undeclared)}개")
        sys.exit(1 if undeclared else 0)


if __name__ == "__main__":
    main()
