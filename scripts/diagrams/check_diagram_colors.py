#!/usr/bin/env python3
"""SVG 색상 인벤토리 게이트 — 다이어그램 색 체계의 CSS 규칙에 없는 색을 경고한다.

인라인 다이어그램의 다크 모드 색은 속성 선택자 규칙(유한 목록)으로 정해지므로,
목록 밖의 색(예: 새 accentN!K 혼합)은 라이트/다크 동일로 렌더돼 다크에서 어긋날
수 있다. build.sh가 SVG 생성 직후 호출한다. 경고만 하고 빌드는 막지 않는다.

Usage: check_diagram_colors.py FILE.svg [...]

allowlist는 CSS 소스 두 곳(_sass/_diagram-colors.scss, assets/css/main_dark.scss)의
속성 선택자에서 파싱해 유도한다 — 규칙을 추가하면 자동으로 통과한다.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# CSS 선택자에 없지만 의도적으로 규칙이 없는 색들
EXTRA = {
    '#000', '#fff',        # 잉크(currentColor)·지우개(배경색) — 값 규칙은 별도 형태
    '#a56f14',             # accent1: 다크 동일 유지라 선택자 부재
    '#00008b', '#008000',  # 동일 유지 룰링 (Partial_Derivatives 메쉬, Homology-4)
}

# img.invert(필터)로 렌더되는 예외 — CSS 색 체계 밖 (plugin의 EXCEPTIONS와 동기)
SKIP = {'Homology-3.svg', 'Homology-5.svg', 'Poincare_Duality-3.svg', 'Poincare_Duality-5.svg'}


def allowlist():
    allowed = set(EXTRA)
    for css in (ROOT / '_sass/_diagram-colors.scss', ROOT / 'assets/css/main_dark.scss'):
        allowed |= set(re.findall(r"\[(?:stroke|fill)='(#[0-9a-fA-F]{3,6})'\]", css.read_text()))
    return {c.lower() for c in allowed}


def main(paths):
    allowed = allowlist()
    warned = False
    for p in paths:
        f = Path(p)
        if f.name in SKIP:
            continue
        colors = {c.lower() for c in re.findall(r"(?:stroke|fill)='(#[0-9a-fA-F]{3,6})'", f.read_text())}
        unknown = colors - allowed
        if unknown:
            warned = True
            print(f"WARN {f.name}: 색 체계 밖의 색 {sorted(unknown)} — "
                  f"다크 모드 규칙이 없어 동일색으로 렌더됨. _diagram-colors.scss에 등록할 것", file=sys.stderr)
    return 0 if not warned else 0  # 경고만, 빌드는 통과


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
