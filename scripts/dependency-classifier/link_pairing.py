#!/usr/bin/env python3
"""link_pairing — KO 글의 `data-lid` 를 대응이 증명되는 EN 링크로 복사한다.

이미 번역된 글에는 lid 가 소급되지 않는다. 앞으로 번역되는 글은 번역기가
`data-relation` 을 옮기듯 lid 도 옮기므로 대응이 공짜로 생기지만, 기존 294쌍은
한 번 짝을 지어 줘야 한다. 이 모듈이 그 일회성 백필의 **결정론 구간**이다 —
짝이 강제되는 곳에만 쓰고, 애매한 곳은 손도 대지 않고 LLM 레인으로 넘긴다.

짝짓기 키는 `(언어 뗀 경로, 정규화된 앵커)` 이고 앵커 정규화가 핵심이다:

  * 라벨 앵커(`#def13`·`#prop7`류)는 언어 불변이라 그대로 쓴다. 전체 링크의
    89% 가 여기다.
  * 섹션 앵커(`#텐서곱` ↔ `#tensor-product`)는 번역되므로 글자로 비교하면
    "한쪽에만 있는 링크"로 오인된다. 실제로 그렇게 세었다가 EN-only 를 79건으로
    부풀린 적이 있다(참값 23건). 그래서 대상 글의 H2 헤딩 목록에서의 **위치**로
    환원한다 — section_anchor_gate 가 앵커 수리에 쓰는 것과 같은 대응이다.
  * 대상 글의 KO/EN 헤딩 개수가 다르면 위치 대응이 성립하지 않으므로 그 링크는
    결정론 대상에서 뺀다. 앵커를 대상 글에서 못 찾아도 마찬가지다.

한 키에 KO 1개 · EN 1개일 때만 복사한다. n:n 은 어느 출현이 어느 출현인지
순서로 정할 수 없고(번역이 순서를 바꾼다), 그게 바로 lid 를 도입한 이유다.
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "dependency-classifier"))
sys.path.insert(0, str(ROOT / "scripts" / "lib"))
import link_ids as L  # noqa: E402
from blog_file_lock import try_acquire_file_locks  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "section_anchor_gate", ROOT / "scripts" / "translation" / "section_anchor_gate.py")
sag = importlib.util.module_from_spec(_spec)
sys.modules["section_anchor_gate"] = sag
_spec.loader.exec_module(sag)
_pn = sag._pn          # postnav 공용 모듈 (라벨 파서)

UNRESOLVED = object()   # 결정론으로 환원 불가 — LLM 레인으로


def _h2_slugs(post) -> list[str]:
    return [h.slug for h in sag.extract_headings(post.path.read_text(encoding="utf-8"))
            if h.level == 2]


def norm_key(target: str, home):
    """링크 target 을 언어 중립 키로. 환원 불가면 UNRESOLVED."""
    path, _, frag = target.partition("#")
    path = path.split("?", 1)[0]
    if path:
        dest = sag._by_permalink(path)
        key_path = path.rstrip("/")
        for pre in ("/ko", "/en"):
            if key_path.startswith(pre + "/"):
                key_path = key_path[len(pre):]
                break
    else:
        dest, key_path = home, "@self"
    if not frag:
        return (key_path, "")
    if sag.LABEL_ANCHOR_RE.match(frag):
        return (key_path, frag)
    if dest is None:
        return UNRESOLVED
    other = sag._counterpart(dest, "en" if dest.lang == "ko" else "ko")
    if other is None:
        return UNRESOLVED
    mine, theirs = _h2_slugs(dest), _h2_slugs(other)
    if len(mine) != len(theirs) or frag not in mine:
        return UNRESOLVED
    return (key_path, f"§{mine.index(frag)}")


def _grouped(post):
    text = post.path.read_text(encoding="utf-8")
    groups = defaultdict(list)
    for link in L.all_links(post.path, text):
        key = norm_key(link.target, post)
        if key is not UNRESOLVED:
            groups[key].append(link)
    return text, groups


def _lid_of(text, link):
    if link.ial_start is None:
        return None
    m = L.LID_RE.search(text[link.ial_start:link.ial_end])
    return m.group(1) if m else None


def _context_fn(text):
    """(줄 → 포함 문맥 태그, H2 개수).

    태그는 그 줄을 감싸는 라벨 박스의 anchor(`def3` 류 — 언어 불변)이고, 박스
    밖이면 속한 H2 절의 순번이다. 절 순번은 KO/EN 절 개수가 같을 때만 의미가
    있으므로 개수를 함께 돌려준다.
    """
    doc = _pn.parse_labels(text)
    boxes = [(b.line_start, b.line_end, f"box:{b.anchor or b.line_start}")
             for b in doc.boxes]
    h2_lines = [h.line for h in sag.extract_headings(text) if h.level == 2]

    def ctx(line: int) -> str:
        for start, end, tag in boxes:
            if start <= line <= end:
                return tag
        return f"sec:{sum(1 for hl in h2_lines if hl < line)}"

    return ctx, len(h2_lines)


def plan_pair(ko_post, en_post):
    """이 한 쌍에서 복사할 (EN 링크, lid) 목록과 통계.

    두 단이다. 1단은 `(경로, 정규화 앵커)` 키가 양쪽에서 딱 하나씩인 경우.
    2단은 그 키가 n:n 인 묶음을 **포함 문맥**으로 더 쪼갠다 — KO 의 `def3`
    안에 X 로 가는 링크가 하나, EN 의 `def3` 안에도 하나면 그 박스가 서로의
    번역이므로 두 링크는 같은 것일 수밖에 없다. 같은 박스 안에 같은 대상이
    둘이면 순서로만 갈리므로 확정하지 않는다.
    """
    ko_text, ko_groups = _grouped(ko_post)
    en_text, en_groups = _grouped(en_post)
    copies, stat = [], defaultdict(int)

    def take(ko_link, en_link, rung):
        lid = _lid_of(ko_text, ko_link)
        if lid is None:
            stat["KO에 lid 없음"] += 1
            return
        existing = _lid_of(en_text, en_link)
        if existing == lid:
            stat["이미 동일"] += 1
            return
        if existing is not None:
            stat["EN에 다른 lid"] += 1
            return
        copies.append((en_link, lid))
        stat[rung] += 1

    leftover = []
    for key, en_links in en_groups.items():
        ko_links = ko_groups.get(key, [])
        if len(ko_links) == 1 and len(en_links) == 1:
            take(ko_links[0], en_links[0], "복사(키)")
        elif ko_links:
            leftover.append((ko_links, en_links))
        else:
            stat["KO에 대응 키 없음"] += len(en_links)

    if leftover:
        ko_ctx, ko_h2 = _context_fn(ko_text)
        en_ctx, en_h2 = _context_fn(en_text)
        for ko_links, en_links in leftover:
            if ko_h2 != en_h2:
                stat["절 개수 불일치"] += len(en_links)
                continue
            ko_tags = defaultdict(list)
            en_tags = defaultdict(list)
            for link in ko_links:
                ko_tags[ko_ctx(link.line)].append(link)
            for link in en_links:
                en_tags[en_ctx(link.line)].append(link)
            for tag, group in en_tags.items():
                peers = ko_tags.get(tag, [])
                if len(peers) == 1 and len(group) == 1:
                    take(peers[0], group[0], "복사(문맥)")
                else:
                    stat["순서로만 갈림"] += len(group)

    for key in ko_groups:
        if key not in en_groups:
            stat["EN에 없음"] += 1
    return en_text, copies, stat


def apply_copies(text, copies):
    edits = []
    for link, lid in copies:
        if link.ial_start is None:
            edits.append((link.end, link.end, f'{{: data-lid="{lid}" }}'))
        else:
            ial = text[link.ial_start:link.ial_end]
            edits.append((link.ial_start, link.ial_end,
                          ial[:2] + f' data-lid="{lid}"' + ial[2:]))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text


def gate(en_post, old, new, copies) -> str | None:
    """통과하면 None, 아니면 거절 사유."""
    if L.strip_lids(new) != old:
        return "역연산 불일치"
    if L.depc.hard_lint(en_post.path, new) - L.depc.hard_lint(en_post.path, old):
        return "lint 악화"
    lids = L.LID_RE.findall(new)
    if len(lids) != len(set(lids)):
        return "EN 안에서 lid 중복"
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    posts = sag._posts()
    pairs = [(p, sag._counterpart(p, "en")) for p in posts if p.lang == "ko"]
    pairs = [(a, b) for a, b in pairs if b]
    if args.limit:
        pairs = pairs[:args.limit]

    total = defaultdict(int)
    touched, refused = 0, []
    for ko_post, en_post in pairs:
        old, copies, stat = plan_pair(ko_post, en_post)
        for k, v in stat.items():
            total[k] += v
        if not copies:
            continue
        new = apply_copies(old, copies)
        why = gate(en_post, old, new, copies)
        if why:
            refused.append((str(en_post.path.relative_to(ROOT)), why))
            total["복사(키)"] -= stat.get("복사(키)", 0)
            total["복사(문맥)"] -= stat.get("복사(문맥)", 0)
            total["게이트 거절"] += len(copies)
            continue
        touched += 1
        if args.apply:
            lease = try_acquire_file_locks([en_post.path])
            if lease is None:
                refused.append((str(en_post.path.relative_to(ROOT)), "락 실패"))
                continue
            try:
                mode = os.stat(en_post.path).st_mode & 0o7777
                fd, tmp = tempfile.mkstemp(prefix=".lid.", suffix=".tmp",
                                           dir=str(en_post.path.parent))
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    f.write(new)
                os.chmod(tmp, mode)
                os.replace(tmp, en_post.path)
            finally:
                lease.release()

    print(f"짝 {len(pairs)}쌍 / {'수정' if args.apply else '수정 예정'} {touched}편")
    for k in ("복사(키)", "복사(문맥)", "이미 동일", "순서로만 갈림",
              "절 개수 불일치", "EN에 없음", "KO에 대응 키 없음",
              "KO에 lid 없음", "EN에 다른 lid", "게이트 거절"):
        if total.get(k):
            print(f"  {k}: {total[k]}")
    for path, why in refused:
        print(f"  거절 {path} — {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
