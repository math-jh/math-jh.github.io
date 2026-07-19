#!/usr/bin/env python3
"""usage_dominance.py — 블로그 전체에서 용어의 영어형 vs 한국어형 우세 실측.

용어를 terms.yml 에 추가하기 전 primary 판정의 근거를 만든다 (2026-07-19
스윕의 교훈: limit=리밋처럼 사전 지식이 코퍼스와 어긋날 수 있다 — 실측이
정본). prose 한정: frontmatter·수식·코드·링크 라벨·<sub> 병기 제외.

CLI:    usage_dominance.py <en형> <ko형>          예) usage_dominance.py limit 극한
import: dominance(en, ko) -> (en_count, ko_count, verdict)
        verdict ∈ {"en", "ko", "insufficient"}  (총출현 < MIN_TOTAL 이면 판정 유보)
"""
from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

BLOG_ROOT = Path(__file__).resolve().parents[2]
MIN_TOTAL = 5          # 이 미만이면 유의미한 값이 아님 → insufficient
KO_WIN_RATIO = 2.0     # ko 가 en 의 2배 초과 + MIN_TOTAL 이상일 때만 ko 판정

_FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
_MASKS = [
    re.compile(r"```.*?```", re.DOTALL),            # code fence
    re.compile(r"\$\$.*?\$\$", re.DOTALL),          # display math
    re.compile(r"(?<!\$)\$[^$\n]+\$(?!\$)"),        # inline math
    re.compile(r"`[^`\n]*`"),                       # inline code
    re.compile(r"<sub>.*?</sub>", re.DOTALL),       # 병기
    re.compile(r"\[(?:\\.|[^\]\\])*\]\([^)]*\)"),   # 링크 (라벨 포함)
]


def _prose(text: str) -> str:
    text = _FM_RE.sub("", text)
    for rx in _MASKS:
        text = rx.sub(" ", text)
    return text


_CORPUS: list[str] | None = None


def _corpus() -> list[str]:
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = []
        for p in glob.glob(f"{BLOG_ROOT}/_posts/Math/**/ko/*.md",
                           recursive=True):
            try:
                _CORPUS.append(_prose(open(p, encoding="utf-8").read()))
            except OSError:
                pass
    return _CORPUS


def count_term(term: str) -> int:
    if not term:
        return 0
    # 영어형은 단어 경계, 한국어형은 부분열 (조사가 붙으므로)
    if re.search(r"[A-Za-z]", term):
        rx = re.compile(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])",
                        re.IGNORECASE)
        return sum(len(rx.findall(t)) for t in _corpus())
    return sum(t.count(term) for t in _corpus())


def dominance(en: str, ko: str) -> tuple[int, int, str]:
    n_en, n_ko = count_term(en), count_term(ko)
    if n_en + n_ko < MIN_TOTAL:
        return n_en, n_ko, "insufficient"
    if n_ko > KO_WIN_RATIO * n_en and n_ko >= MIN_TOTAL:
        return n_en, n_ko, "ko"
    return n_en, n_ko, "en"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    e, k, v = dominance(sys.argv[1], sys.argv[2])
    print(f"en {sys.argv[1]!r}: {e}회 · ko {sys.argv[2]!r}: {k}회 → {v}")
