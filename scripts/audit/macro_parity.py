#!/usr/bin/env python3
"""macro_parity.py — katex-macros.js ↔ Operators.sty 겹침 매크로 드리프트 트립와이어.

이중 SoT 감사 [0] (2026-07-22). 본문 수식 매크로의 정본은
assets/js/katex-macros.js 이고, assets/diagrams/.preamble/Operators.sty 는
다이어그램 LaTeX 용으로 겹치는 어휘를 재정의한다. JS↔LaTeX 라 한쪽에서
파생할 수 없으므로, "겹치는 이름의 양쪽 정의 텍스트"를 lock 파일에 박제해
두고 어느 쪽이든 바뀌면 시끄럽게 실패한다 (조용한 렌더 갈림 방지 — 실제로
\\lmod \\rmod \\RP \\CP 가 어긋난 채 발견된 이력).

lock 은 지식의 사본이 아니라 attestation 이다: "이 쌍들은 이 시점에 렌더
동일함을 확인했다"는 기록. 갱신은 사람이 양쪽 렌더를 눈으로 맞춘 뒤
`--write` 로만 한다.

사용:
  macro_parity.py          # 검사 (build.sh 가 매 빌드 앞에 실행)
  macro_parity.py --write  # 렌더 동일 확인 후 lock 재생성
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
JS = ROOT / "assets/js/katex-macros.js"
STY = ROOT / "assets/diagrams/.preamble/Operators.sty"
LOCK = Path(__file__).with_name("macro_parity.lock")


def js_defs() -> dict[str, str]:
    out = {}
    for m in re.finditer(r'"\\\\([A-Za-z]+)"\s*:\s*"((?:[^"\\]|\\.)*)"', JS.read_text(encoding="utf-8")):
        out[m.group(1)] = m.group(2)
    return out


def sty_defs() -> dict[str, str]:
    out = {}
    for line in STY.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("%"):
            continue
        m = re.search(r"\\(?:newcommand|renewcommand|providecommand)\{?\\([A-Za-z]+)\}?", s) \
            or re.search(r"\\DeclareMathOperator\*?\{\\([A-Za-z]+)\}", s)
        if m:
            out[m.group(1)] = re.sub(r"\s+", " ", s)
    return out


def current_pairs() -> dict[str, tuple[str, str]]:
    j, t = js_defs(), sty_defs()
    return {n: (j[n], t[n]) for n in sorted(set(j) & set(t))}


def main() -> int:
    pairs = current_pairs()
    if "--write" in sys.argv[1:]:
        with LOCK.open("w", encoding="utf-8") as f:
            f.write("# katex-macros.js ↔ Operators.sty 겹침 attestation — macro_parity.py --write 로만 갱신\n")
            for n, (jv, sv) in pairs.items():
                f.write(f"{n}\t{jv}\t{sv}\n")
        print(f"lock 갱신: 겹침 {len(pairs)}쌍 → {LOCK.name}")
        return 0

    if not LOCK.exists():
        print(f"ERROR: {LOCK} 없음 — 렌더 확인 후 --write 로 생성할 것", file=sys.stderr)
        return 1
    locked: dict[str, tuple[str, str]] = {}
    for line in LOCK.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        n, jv, sv = line.split("\t")
        locked[n] = (jv, sv)

    errs = []
    for n, cur in pairs.items():
        if n not in locked:
            errs.append(f"신규 겹침 {n!r}: katex-macros.js 렌더와 맞는지 확인 후 --write")
        elif locked[n] != cur:
            errs.append(f"{n!r} 정의 변경: lock={locked[n]} → 현재={cur} — 양쪽 렌더 재확인 후 --write")
    for n in locked:
        if n not in pairs:
            errs.append(f"{n!r} 이 더는 겹치지 않음 (한쪽에서 삭제/개명) — --write 로 lock 정리")
    if errs:
        print("macro parity FAIL:", *errs, sep="\n  ", file=sys.stderr)
        return 1
    print(f"macro parity OK ({len(pairs)}쌍)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
