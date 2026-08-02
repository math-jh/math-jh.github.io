#!/usr/bin/env python3
"""find_post — 글·라벨 해소, 인용 링크 생성, inbound 조사.

사용:
  find_post.py find '<질의>' [--cat C] [--lang ko|en] [--grep]
      질의가 하우스 인용 링크나 /ko/... 경로면 결정론적으로 해소해
      파일 경로 + 라벨 블록 줄 범위(귀속 증명 포함)를 출력한다.
      그 외에는 정규화(fuzzy) 매칭: 파일명·슬러그·title 대상, 0건이면 본문 grep 폴백.
  find_post.py labels '<글지정>'
  find_post.py cite '<글지정>' '<라벨>' --from <현재파일>
  find_post.py inbound '<글지정>' [--label prop6]

'<글지정>'은 파일 경로·permalink·인용 링크·fuzzy 질의 모두 허용.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from common import (
    KIND_PREFIX, NUMBERED_ALT, PREFIX_KIND, ROOT,
    Post, by_permalink, en_counterpart, find_box, fuzzy_posts, iter_posts,
    normalize, parse_citation_query, parse_labels, subject_display,
)


def fail(msg: str) -> "sys.NoReturn":
    print(f"ERROR {msg}", file=sys.stderr)
    sys.exit(1)


def post_line(p: Post) -> str:
    flags = "" if p.published else "  DRAFT"
    w = f"w={p.weight}" if p.weight is not None else "w=?"
    return f"{p.rel}  |  {p.title}  |  {p.permalink}  |  {w}{flags}"


def resolve_one(query: str, posts: list[Post], cat: str | None = None,
                lang: str = "ko") -> tuple[Post, str | None]:
    """글지정 → (Post, anchor|None). 실패 시 종료(후보 나열)."""
    q = query.strip()
    # 1) 파일 경로
    for cand in (Path(q), ROOT / q):
        if cand.is_file():
            for p in posts:
                if p.path == cand.resolve():
                    return p, None
    # 2) 인용 링크 / permalink 경로
    pq = parse_citation_query(q)
    if pq and pq.path:
        p = by_permalink(pq.path, posts)
        if not p:
            fail(f"permalink 해소 실패: {pq.path} (frontmatter 실측 기준, 조립 추측 아님)")
        return p, pq.anchor
    # 3) fuzzy
    matches = fuzzy_posts(q, posts, cat=cat, lang=lang)
    if len(matches) == 1:
        return matches[0], None
    if not matches:
        fail(f"매칭 없음: {query!r} (키워드 본문 검색은 `find --grep` 사용)")
    print(f"AMBIGUOUS {len(matches)}건 — 하나를 지정할 것:", file=sys.stderr)
    for p in matches[:10]:
        print("  " + post_line(p), file=sys.stderr)
    sys.exit(1)


def print_anchor_info(p: Post, anchor: str, pq=None) -> None:
    doc = parse_labels(p.path.read_text(encoding="utf-8"))
    box = find_box(doc, anchor=anchor)
    if not box:
        print(f"WARN 앵커 #{anchor} 이 {p.rel} 에 없음. 실존 라벨은 `labels` 참조")
        return
    tag = "명시형 " if box.explicit else ""
    print(f"ANCHOR #{box.anchor} → {tag}::: {box.label}  lines {box.line_start}-{box.line_end}")
    for pr in box.proofs:
        kind = f"standalone: {pr.target_text}" if pr.standalone else "attached"
        print(f"PROOF ({kind})  lines {pr.line_start}-{pr.line_end}")
    if pq:
        # 붙여넣은 인용 링크의 표시부 대조 — 어긋나면 경고 (주 목적은 위 위치 출력).
        if pq.kind and pq.number is not None:
            qp = KIND_PREFIX.get(pq.kind)
            bp = KIND_PREFIX.get(box.kind)
            if pq.number != box.number or (qp and bp and qp != bp):
                print(f"WARN 링크 텍스트 '{pq.kind} {pq.number}' ↔ 실제 '{box.kind} {box.number}' 불일치")
        if pq.section_title and pq.section_title != p.title:
            print(f"WARN §제목 '{pq.section_title}' ↔ 실제 title '{p.title}' 불일치")
        if pq.category_display:
            disp = subject_display(p, p.lang)
            if pq.category_display != disp:
                print(f"WARN 카테고리 표시명 '{pq.category_display}' ↔ 정본 '{disp}' 불일치")


def cmd_find(args, posts):
    pq = parse_citation_query(args.query)
    if pq and pq.path:
        p = by_permalink(pq.path, posts)
        if not p:
            fail(f"permalink 해소 실패: {pq.path}")
        print("FILE " + p.rel)
        print(f"TITLE {p.title}  |  {p.permalink}  |  w={p.weight}"
              + ("" if p.published else "  DRAFT"))
        if pq.anchor:
            print_anchor_info(p, pq.anchor, pq)
        return

    matches = [] if args.grep else fuzzy_posts(args.query, posts, cat=args.cat, lang=args.lang)
    if matches:
        for p in matches[:10]:
            print(post_line(p))
        if len(matches) > 10:
            print(f"... 외 {len(matches) - 10}건")
        return

    # 본문 keyword 폴백
    if not args.grep:
        print(f"NOTE 제목/파일명/슬러그 매칭 0건 → 본문 keyword 검색 폴백: {args.query!r}")
    ncat = normalize(args.cat) if args.cat else None
    hits = []
    for p in posts:
        if args.lang and p.lang != args.lang:
            continue
        if ncat and ncat not in normalize(p.category_dir) and ncat not in normalize(subject_display(p)):
            continue
        n = p.path.read_text(encoding="utf-8").lower().count(args.query.lower())
        if n:
            hits.append((n, p))
    hits.sort(key=lambda t: -t[0])
    if not hits:
        print("NO MATCH")
        return
    for n, p in hits[:10]:
        print(f"{n:4d}회  " + post_line(p))


def cmd_labels(args, posts):
    p, _ = resolve_one(args.post, posts, lang=args.lang)
    print("FILE " + p.rel)
    doc = parse_labels(p.path.read_text(encoding="utf-8"))
    for b in doc.boxes:
        proofs = ", ".join(
            f"{pr.line_start}-{pr.line_end}" + (" (단독형)" if pr.standalone else "")
            for pr in b.proofs)
        tag = "  [명시형]" if b.explicit else ""
        print(f"{b.line_start:5d}: {b.label}  → #{b.anchor}{tag}"
              + (f"  proofs: {proofs}" if proofs else ""))
    for i, label in doc.unrecognized:
        print(f"WARN {i}행: 인식 불가 라벨 '{label}'")


def cmd_cite(args, posts):
    src_path = (Path(args.frm) if Path(args.frm).is_file() else ROOT / args.frm).resolve()
    if not src_path.is_file():
        fail(f"--from 파일이 실존하지 않음: {args.frm}")
    src = next((p for p in posts if p.path == src_path), None)
    if not src:
        fail(f"--from 파일이 포스트가 아님: {args.frm}")

    target, _ = resolve_one(args.post, posts, lang=src.lang)
    if src.lang == "en" and target.lang == "ko":
        en = en_counterpart(target, posts)
        if not en:
            fail(f"en 짝 없음: {target.rel}")
        target = en

    lm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)$", args.label.strip()) if args.label else None
    if lm:
        kind, num = lm.group(1), int(lm.group(2))
        box = find_box(parse_labels(target.path.read_text(encoding="utf-8")),
                       kind=kind, number=num)
    else:
        box = find_box(parse_labels(target.path.read_text(encoding="utf-8")),
                       anchor=args.label.lstrip("#"))
    if not box:
        fail(f"라벨 '{args.label}' 이 {target.rel} 에 없음 (`labels` 로 확인)")

    # 링크 텍스트의 종류 단어는 대상 글 언어 기준.
    prefix = KIND_PREFIX.get(box.kind)
    if box.explicit or not prefix:
        kind_word = box.kind
    else:
        kind_word = PREFIX_KIND[prefix][0 if target.lang == "ko" else 1]
    label_text = f"{kind_word} {box.number}"

    if src.path == target.path:
        out = f"[{label_text}](#{box.anchor})"
    elif src.category_dir == target.category_dir:
        out = f"[§{target.title}, ⁋{label_text}]({target.permalink}#{box.anchor})"
    else:
        disp = subject_display(target, target.lang)
        out = f"[\\[{disp}\\] §{target.title}, ⁋{label_text}]({target.permalink}#{box.anchor})"
    print(out)

    if (src.category_dir == target.category_dir and src.path != target.path
            and src.weight is not None and target.weight is not None
            and target.weight > src.weight):
        print(f"WARN forward reference: 대상 w={target.weight} > 현재 w={src.weight} — 필수가 아니면 금지")
    if not target.published:
        print("WARN 대상 글이 published: false (초안)")


def cmd_inbound(args, posts):
    p, _ = resolve_one(args.post, posts, lang="ko")
    targets = {p.permalink.rstrip("/")}
    en = en_counterpart(p, posts) if p.lang == "ko" else None
    if en:
        targets.add(en.permalink.rstrip("/"))
    label = args.label.lstrip("#") if args.label else None
    total = 0
    for q in posts:
        if q.path == p.path or (en and q.path == en.path):
            continue
        text = q.path.read_text(encoding="utf-8")
        for i, line in enumerate(text.split("\n"), start=1):
            for t in targets:
                for m in re.finditer(re.escape(t) + r"#([\w\-]+)", line):
                    if label and not re.fullmatch(re.escape(label), m.group(1)):
                        continue
                    total += 1
                    print(f"{q.rel}:{i}: {line.strip()[:160]}")
                    break
    print(f"TOTAL {total}건")


def main() -> None:
    ap = argparse.ArgumentParser(prog="find_post")
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("find")
    f.add_argument("query")
    f.add_argument("--cat")
    f.add_argument("--lang", default="ko")
    f.add_argument("--grep", action="store_true", help="본문 keyword 검색 강제")

    l = sub.add_parser("labels")
    l.add_argument("post")
    l.add_argument("--lang", default="ko")

    c = sub.add_parser("cite")
    c.add_argument("post")
    c.add_argument("label")
    c.add_argument("--from", dest="frm", required=True)

    i = sub.add_parser("inbound")
    i.add_argument("post")
    i.add_argument("--label")

    args = ap.parse_args()
    posts = iter_posts()
    {"find": cmd_find, "labels": cmd_labels, "cite": cmd_cite, "inbound": cmd_inbound}[args.cmd](args, posts)


if __name__ == "__main__":
    main()
