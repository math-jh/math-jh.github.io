#!/usr/bin/env python3
"""link_ids — 링크 출현의 영속 식별자 `data-lid` 발급.

왜 필요한가:
  KO 글과 그 EN 번역 사이에서 "이 링크와 저 링크가 같은 것"을 내용으로부터
  복원할 수 없다. 번역이 순서를 바꾸고("A의 1번 결과가 아니라 2번" →
  "first result of A, not the second"처럼) 링크를 합치기도 하기 때문이다.
  그래서 복원을 포기하고 KO 쪽 출현마다 불투명한 id 를 한 번 부여한 뒤,
  번역기가 `data-relation` 을 옮기듯 이 속성도 같이 옮기게 한다. 같은 lid 를
  가진 KO/EN 출현이 곧 대응이고, 합쳐진 링크는 한쪽 lid 가 EN 에 없는 것으로
  정확히 드러난다.

왜 내용 해시가 아닌가:
  target·label·서수를 재료로 쓰면 사용자가 링크 텍스트를 고치는 순간 id 가
  바뀐다. 원장의 기존 ident(sha1(path:ordinal:target:label))가 바로 그래서
  보류 항목을 `gone` 으로 잃었다. lid 는 출생 시 난수이고 이후 불변이다.

왜 난수인데 유일한가:
  36진수 5자(6047만)를 뽑고 **대조 집합에 있으면 다시 뽑는다**. 확률에 기대지
  않는다. 대조 집합은 `현재 코퍼스 ∪ 발급 대장` 인데, 대장이 있어야 지워진
  링크의 id 가 풀려서 나중에 다른 링크에 재배정되는 일이 없다 (옛 원장 항목과
  커밋 이력의 옛 id 가 엉뚱한 링크를 가리키게 된다). 대장을 잃어도 커밋 이력을
  훑어 재구성할 수 있다.
"""
from __future__ import annotations

import re
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "dependency-classifier"))
import dependency_classifier as depc  # noqa: E402

LEDGER = Path.home() / ".local" / "state" / "link-ids.txt"
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"
LENGTH = 5
LID_RE = re.compile(r'\bdata-lid\s*=\s*"([^"]*)"')
# 삽입의 정확한 역연산 — 검증 게이트가 이것으로 "lid 말고는 안 건드렸다"를 증명한다.
LID_ATTR_RE = re.compile(r'\s+data-lid\s*=\s*"[^"]*"')
LID_ONLY_IAL_RE = re.compile(r'\{:\s+data-lid\s*=\s*"[^"]*"\s*\}')


def all_links(path: Path, text: str):
    """세 side 를 합쳐 소스 순서로. extract_links 는 한 side 씩만 돌려준다."""
    seen = {}
    for kw in ({}, {"tagged": True}, {"review": True}):
        for link in depc.extract_links(path, text, **kw):
            seen[link.start] = link
    return [seen[k] for k in sorted(seen)]


def load_ledger() -> set[str]:
    if not LEDGER.exists():
        return set()
    return {ln.strip() for ln in LEDGER.read_text(encoding="utf-8").splitlines() if ln.strip()}


def scan_corpus(paths) -> set[str]:
    out = set()
    for p in paths:
        out.update(LID_RE.findall(p.read_text(encoding="utf-8")))
    return out


def mint(used: set[str]) -> str:
    while True:
        lid = "".join(secrets.choice(ALPHABET) for _ in range(LENGTH))
        if lid not in used:
            used.add(lid)
            return lid


def strip_lids(text: str) -> str:
    """lid 삽입의 역연산. 새로 만든 IAL 은 통째로, 기존 IAL 은 속성만 뗀다."""
    return LID_ATTR_RE.sub("", LID_ONLY_IAL_RE.sub("", text))


def annotate(path: Path, text: str, used: set[str]) -> tuple[str, list[str]]:
    edits, minted = [], []
    for link in all_links(path, text):
        if link.ial_start is not None and LID_RE.search(text[link.ial_start:link.ial_end]):
            continue
        lid = mint(used)
        minted.append(lid)
        if link.ial_start is None:
            edits.append((link.end, link.end, f'{{: data-lid="{lid}" }}'))
        else:
            ial = text[link.ial_start:link.ial_end]
            edits.append((link.ial_start, link.ial_end,
                          ial[:2] + f' data-lid="{lid}"' + ial[2:]))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    return text, minted
