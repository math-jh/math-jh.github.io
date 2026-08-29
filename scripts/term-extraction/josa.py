#!/usr/bin/env python3
"""josa.py — 영어 용어의 한국어 음역 끝소리(V/C/L) 판정 단일 출처.

용어 영어화 스윕은 한국어 조사를 음역 발음에 맞게 다시 골라야 한다
(자음 끝 → 은/이/을/과/으로, 모음 끝 → 는/가/를/와/로, ㄹ 끝 → 은/이/을/과/로).
이 판정을 mech_sweep(치환기)와 josa_check(검사기)가 공유한다.

**손유지 목록을 쓰지 않는다.** 예전에는 137개 단어를 손으로 분류한 표를 두
파일이 각자 복사해 들고 있었고, 새 용어가 늘 때마다 사람이 채워야 했다. 지금은
CMU 발음사전(cmudict)에서 발음을 받아 외래어 표기법 받침 규칙을 적용한다.
사람이 유지하는 것은 발음규칙으로 안 나오는 관용형 IRREGULAR 뿐이다.

판정 경로 (앞에서 걸리면 끝):
  1. IRREGULAR      — 발음과 어긋나는 한국어 관용형
  2. cmudict 직접   — 표제어 126k
  3. 하이픈 뒤 낱말 — quasi-isomorphism → isomorphism
  4. 최장 접미분해  — coset → set, subalgebra → algebra (수학 조어 대응)
  5. 철자 폴백      — cmudict 밖 (사전 없을 때의 전면 폴백이기도 하다)

cmudict 가 없으면 5번만으로 동작한다(정확도는 떨어지지만 죽지 않는다).
설치: ~/.venvs/josa/bin/pip install cmudict — 그 인터프리터로 실행하면 1~4가 산다.

사용:
    from josa import ending_class, WRONG_JOSA
    ending_class("polynomial ring")   # -> "C"  (마지막 낱말로 판정)

    python3 josa.py --coverage        # terms.yml 전 용어 분류 경로 통계
    python3 josa.py <영단어>...        # 낱개 조회
"""
import os
import re
import sys

# ── cmudict (선택 의존) ──────────────────────────────────────────────────────
try:
    import cmudict as _cmudict
    _DICT = _cmudict.dict()
except ImportError:                                   # 없으면 철자 폴백만
    _DICT = {}

HAS_CMUDICT = bool(_DICT)

# ── 발음 → 끝소리 ───────────────────────────────────────────────────────────
_VOWELS = set("AA AE AH AO AW AY EH ER EY IH IY OW OY UH UW".split())
# 짧은 모음. 어말 무성파열음이 받침이 되는 조건이다 (set 셋 / commute 커뮤트).
_SHORT = set("AA AE AH EH IH UH".split())

# 발음규칙으로는 안 나오는 한국어 관용형. **여기만 사람이 유지한다.**
# 옛 손유지 표 137개를 이 규칙들로 재현했을 때 어긋난 것만 남았다.
# limit(리밋)·nondegenerate 등은 규칙이 이미 맞히므로 여기 없다.
IRREGULAR = {
    "group": "C",      # 그룹 — 긴 모음 뒤인데 받침 ㅂ (관용)
    "subgroup": "C",
    "type": "C",       # 타입 — 묵음 e 인데 받침 ㅂ (관용)
    "polytope": "C",   # 폴리톱 — 폴리토프(V)로 적기로 하면 이 줄을 지울 것
}


def _cls_from_phones(phones, spelling=""):
    """ARPAbet 음소열 → V / C / L.

    어말 무성파열음 판정에 철자를 함께 본다. cmudict 는 bracket(브래킷)과
    coordinate(코디네이트)의 끝을 똑같이 비강세 `AH0 T` 로 주어 음소만으로는
    못 가른다. 가르는 것은 묵음 e (magic e) 로, 이게 있으면 앞 모음이 길다.
    """
    if not phones:
        return None
    bare = [re.sub(r"\d", "", x) for x in phones]
    last = bare[-1]
    prev = bare[-2] if len(bare) > 1 else None
    if last in _VOWELS:
        return "V"                       # 모음 끝
    if last == "L":
        return "L"                       # 모듈·아이디얼·룰
    if last in ("M", "N", "NG"):
        return "C"                       # 폼·도메인·링
    if last in ("P", "K", "T"):
        # 외래어 표기법: 짧은 모음 바로 뒤 어말 무성파열음만 받침으로 적는다
        # (set 셋, bracket 브래킷, metric 메트릭). 그 밖에는 '으'를 붙인다
        # (point 포인트, root 루트, coordinate 코디네이트, commute 커뮤트).
        if prev in _SHORT and not spelling.endswith("e"):
            return "C"
        return "V"
    # 유성파열음·마찰음·파찰음·R 등은 '으/이' 첨가라 받침이 없다
    return "V"                           # field 필드, class 클래스, sheaf 시프


# 철자 폴백. cmudict 밖 낱말용이자, 사전이 없을 때의 전면 폴백.
# 긴 접미어부터 본다.
_SPELL = [
    ("tion", "C"), ("sion", "C"), ("ness", "V"), ("ism", "C"), ("ing", "C"),
    ("le", "L"), ("l", "L"),
    ("ce", "V"), ("se", "V"), ("ss", "V"),
    ("ng", "C"), ("m", "C"), ("n", "C"),
    ("c", "C"), ("k", "C"), ("p", "C"),
    ("s", "V"), ("x", "V"), ("z", "V"),
    ("y", "V"), ("e", "V"), ("a", "V"), ("o", "V"), ("i", "V"), ("u", "V"),
    ("r", "V"), ("t", "V"), ("d", "V"), ("f", "V"), ("g", "V"), ("h", "V"),
    ("v", "V"), ("w", "V"), ("b", "V"),
]


def classify_word(word):
    """한 낱말 → (class, 판정경로). 못 맞히면 (None, '미분류')."""
    w = re.sub(r"[^a-z-]", "", str(word).lower())
    if not w:
        return None, "미분류"
    if w in IRREGULAR:
        return IRREGULAR[w], "irregular"
    if w in _DICT:
        return _cls_from_phones(_DICT[w][0], w), "cmudict"
    base = w.split("-")[-1]
    if base != w:
        if base in IRREGULAR:
            return IRREGULAR[base], "irregular"
        if base in _DICT:
            return _cls_from_phones(_DICT[base][0], base), "hyphen"
    for i in range(1, max(1, len(base) - 2)):        # 최장 접미어부터
        suf = base[i:]
        if len(suf) >= 3 and suf in _DICT:
            return _cls_from_phones(_DICT[suf][0], suf), "suffix:" + suf
    for suf, c in _SPELL:
        if base.endswith(suf):
            return c, "spell:" + suf
    return None, "미분류"


def ending_class(term):
    """영어 용어(구 가능) → V / C / L. 마지막 낱말이 조사를 결정한다."""
    parts = str(term).split()
    if not parts:
        return None
    return classify_word(parts[-1])[0]


# 사전이 그 낱말 자체를 직접 알려준 경로. 접미분해(suffix)·철자폴백(spell)은
# 추정이라 제외한다. 본문을 고쳐 쓰는 파괴적 패스는 이것만 써야 한다 —
# 옛 손확정 표(OVERRIDE)가 맡던 역할이다.
CONFIDENT = ("irregular", "cmudict", "hyphen")


def confident_class(term):
    """고신뢰 경로로만 판정. 추정이면 None."""
    parts = str(term).split()
    if not parts:
        return None
    c, how = classify_word(parts[-1])
    return c if how.split(":")[0] in CONFIDENT else None


# ── 끝소리별 '틀린' 조사 ────────────────────────────────────────────────────
# 단일 문자 조사는 뒤가 한글이면 다른 낱말일 수 있어 경계를 요구한다.
# 로/으로 계열은 뒤에 서/써/부터가 붙어도 조사다.
_B = r"(?![가-힣])"
WRONG_JOSA = {
    "V": [r"은" + _B, r"이" + _B, r"을" + _B, r"과" + _B, r"으로"],
    "C": [r"는" + _B, r"가" + _B, r"를" + _B, r"와" + _B,
          r"로(?:서|써|부터)?" + _B],
    "L": [r"는" + _B, r"가" + _B, r"를" + _B, r"와" + _B, r"으로"],
}


# ── CLI ─────────────────────────────────────────────────────────────────────
def _tier1():
    """terms.yml 의 primary:en 매핑 (ko → en). md_lint 가 단일 출처."""
    root = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(root, ".agents", "hooks"))
    import md_lint
    if md_lint._DEPR is None:
        sys.exit("_data/terms.yml 로드 실패")
    return md_lint._DEPR[0]


def _main(argv):
    if not HAS_CMUDICT:
        print("! cmudict 없음 — 철자 폴백만 동작 "
              "(~/.venvs/josa/bin/python 으로 실행하면 정밀)", file=sys.stderr)
    if argv and argv[0] == "--coverage":
        import collections
        finals = sorted({en.split()[-1].lower() for en in _tier1().values()})
        by, unknown = collections.Counter(), []
        for f in finals:
            c, how = classify_word(f)
            by[how.split(":")[0]] += 1
            if c is None:
                unknown.append(f)
        print(f"terms.yml primary:en 마지막 낱말 {len(finals)}종")
        for k, v in by.most_common():
            print(f"  {k:10} {v:4d}  ({v/len(finals)*100:.0f}%)")
        print(f"  미분류     {len(unknown):4d}" + (f"  {unknown}" if unknown else ""))
        return 1 if unknown else 0
    if not argv:
        print(__doc__.strip().split("사용:")[-1])
        return 0
    for w in argv:
        c, how = classify_word(w.split()[-1])
        print(f"{w:28} {c or '?'}  ({how})")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
