#!/usr/bin/env python3
"""영어 치환어 + 한국어 조사 정합성 검사.

스윕이 한국어 용어를 영어로 바꿀 때 조사를 음역 발음에 맞게 재선택해야 한다
(자음 끝 → 은/이/을/과/으로, 모음 끝 → 는/가/를/와/로, ㄹ 끝 → 은/이/을/과/로).
워커가 조사를 안 고치면 `isomorphism가`·`group는`·`cohomology은` 꼴이 남는다.

계사(이다/이고/이며/인/일…)는 어디에나 붙으므로 검사하지 않는다.
검사 대상 파일 = 세 work JSON 의 files 합집합.

사용: josa_check.py            (전체)
      josa_check.py 파일...     (지정 파일만)
"""
import json
import re
import sys

sys.path.insert(0, "/home/junhyeok/math-jh.github.io/scripts/term-extraction")
from terms_usage_lint import prose_lines  # noqa: E402

ROOT = "/home/junhyeok/math-jh.github.io/"
# 2026-07 스윕 당시의 work-list 파일들 (지금은 없음 — 있으면 그 목록만 검사)
JSONS = ["/var/tmp/pub_work.json", "/var/tmp/fleet_work.json",
         "/var/tmp/term_sweep/iso_work.json"]

# 매핑 right 값의 마지막 단어별 음역 끝소리 분류.
# V = 받침 없음, C = 받침(ㄹ 제외), L = 받침 ㄹ
ENDING = {
    "above": "V", "action": "C", "algebra": "V", "automorphism": "C",
    "basis": "V", "below": "V", "bound": "V", "bounded": "V",
    "bundle": "L", "center": "V", "class": "V", "closed": "V",
    "closure": "V", "cohomology": "V", "commutator": "V", "commute": "V",
    "completion": "C", "comultiplication": "C", "correspondence": "V",
    "coset": "C", "countable": "L", "cover": "V", "covering": "C",
    "derivative": "V", "diffeomorphism": "C", "domain": "C",
    "duality": "V", "embedding": "C", "endomorphism": "C",
    "equivalent": "V", "extension": "C", "field": "V", "form": "C",
    "fractions": "V", "frame": "C", "full": "L", "function": "C",
    "functor": "V", "generated": "V", "group": "C",
    "homeomorphism": "C", "homology": "V", "homomorphism": "C",
    "ideal": "L", "irreducible": "L", "isomorphic": "C",
    "isomorphism": "C", "kernel": "L", "lemma": "V",
    "limit": "C",  # 블로그 코퍼스 '리밋' (C형 79:0)
    "magma": "V", "mapping": "C", "matrix": "V", "module": "L",
    "point": "V", "polynomial": "L", "preimage": "V", "product": "V",
    "projection": "C", "pseudoinverse": "V", "quasi-isomorphism": "C",
    "quotient": "V", "regular": "V", "representation": "C",
    "resolution": "C", "ring": "C", "section": "C", "sequence": "V",
    "set": "C", "sheaf": "V", "similar": "V", "smooth": "V",
    "space": "V", "spectrum": "C", "subalgebra": "V", "subgroup": "C",
    "subring": "C", "successor": "V", "sum": "C", "symmetric": "C",
    "tensor": "V", "transformation": "C", "transitive": "V",
    "variety": "V", "vector": "V",
}

# 끝소리별 틀린 조사. 단일 문자는 바로 뒤가 한글이면 다른 단어일 수 있어
# 경계(비한글)까지 요구한다. 로/으로 계열은 뒤에 서/써/부터가 붙어도 조사다.
B = r"(?![가-힣])"
WRONG = {
    "V": [r"은" + B, r"이" + B, r"을" + B, r"과" + B, r"으로"],
    "C": [r"는" + B, r"가" + B, r"를" + B, r"와" + B, r"로(?:서|써|부터)?" + B],
    "L": [r"는" + B, r"가" + B, r"를" + B, r"와" + B, r"으로"],
}

files = set()
for j in JSONS:
    try:
        files |= set(json.load(open(j))["files"])
    except (OSError, ValueError, KeyError):
        pass
targets = sys.argv[1:] or sorted(files)
if not targets:  # work-list 없으면 ko 글 전체
    import glob
    targets = sorted(glob.glob(ROOT + "_posts/Math/**/ko/*.md",
                               recursive=True))

pats = {w: re.compile(r"\b(" + re.escape(w) + r")(" + "|".join(WRONG[c]) + r")")
        for w, c in ENDING.items()}

sys.path.insert(0, "/home/junhyeok/math-jh.github.io/.claude/hooks")
import md_lint  # noqa: E402
CODE = re.compile(r"`[^`]*`")

bad = 0
for rel in targets:
    path = rel if rel.startswith("/") else ROOT + rel
    try:
        it = list(prose_lines(path))
    except OSError:
        continue
    for ln, text in it:
        # 인라인 수식·코드·링크·병기 안은 조사 검사 대상이 아니다
        for rx in (md_lint._MATH_SPAN_RE, CODE, md_lint._LINK_ALL_RE,
                   re.compile(r"<sub>.*?</sub>")):
            text = rx.sub(" ", text)
        for w, pat in pats.items():
            for m in pat.finditer(text):
                print(f"{path.replace(ROOT,'')}:{ln}: {m.group(0)!r}")
                bad += 1
print(f"-- 조사 오류 {bad}건")
sys.exit(1 if bad else 0)
