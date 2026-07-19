#!/usr/bin/env python3
"""terms_search.py — terms.yml 용어 검색 (추가 전 중복·sees 후보 확인용).

정규화(dedup_key: 대소문자·발음기호·수식 접기) 완전일치 + 부분열 일치를
en·ko·id 세 필드에 대해 본다.

CLI:    terms_search.py <질의> [--exact]
import: search(q, exact=False) -> list[(letter, chunk)]
        by_dedup(en_or_ko) -> chunk | None   (정규화 완전일치 1건)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from terms_common import (  # noqa: E402
    TERMS_PATH, chunk_field, chunk_id, dedup_key, split_file,
)


def _load() -> dict[str, list[str]]:
    _, groups = split_file(TERMS_PATH.read_text(encoding="utf-8"))
    return groups


def search(q: str, exact: bool = False) -> list[tuple[str, str]]:
    qd = dedup_key(q)
    out = []
    for letter, chunks in _load().items():
        for c in chunks:
            fields = [chunk_id(c), chunk_field(c, "en") or "",
                      chunk_field(c, "ko") or ""]
            keys = [dedup_key(f) for f in fields if f]
            if exact:
                if qd in keys:
                    out.append((letter, c))
            elif any(qd and qd in k for k in keys):
                out.append((letter, c))
    return out


def by_dedup(term: str) -> str | None:
    """en 또는 ko 가 정규화 완전일치하는 항목 청크 (없으면 None)."""
    qd = dedup_key(term)
    if not qd:
        return None
    for _, chunks in _load().items():
        for c in chunks:
            if qd in (dedup_key(chunk_field(c, "en") or ""),
                      dedup_key(chunk_field(c, "ko") or "")):
                return c
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    hits = search(sys.argv[1], exact="--exact" in sys.argv[2:])
    for letter, c in hits:
        print(f"[{letter}]")
        print(c)
        print()
    print(f"-- {len(hits)}건")
