#!/usr/bin/env python3
"""영어 치환어 + 한국어 조사 정합성 검사.

스윕이 한국어 용어를 영어로 바꿀 때 조사를 음역 발음에 맞게 재선택해야 한다.
워커가 조사를 안 고치면 `isomorphism가`·`group는`·`cohomology은` 꼴이 남는다.
계사(이다/이고/이며/인/일…)는 어디에나 붙으므로 검사하지 않는다.

검사 대상 낱말과 끝소리 판정은 **손유지 목록이 아니라** 두 단일 출처에서 온다:
  * 낱말   — `_data/terms.yml` 의 primary:en 매핑 (md_lint._DEPR)
  * 끝소리 — `josa.py` (cmudict 발음 + 외래어 표기법 규칙)
그래서 terms.yml 에 용어가 늘어도 이 파일은 손댈 게 없다.

정밀 판정에는 cmudict 가 필요하다. 없으면 철자 폴백으로 동작하며 경고를 낸다:
    ~/.venvs/josa/bin/python josa_check.py

사용: josa_check.py                (ko 글 전체)
      josa_check.py 파일...         (지정 파일만)
      josa_check.py --terms         (검사에 쓰는 낱말→끝소리 표를 출력)
종료코드: 조사 오류가 있으면 1.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, ".agents", "hooks"))

import josa                                            # noqa: E402
from terms_usage_lint import prose_lines               # noqa: E402
import md_lint                                         # noqa: E402

if md_lint._DEPR is None:
    sys.exit("_data/terms.yml 로드 실패")
TIER1 = md_lint._DEPR[0]                               # ko → en

# 검사 대상 = terms.yml 이 영어로 확정한 용어들. 한 낱말짜리만 본다 —
# 여러 낱말 구는 본문에 그대로 붙어 나오는 일이 드물고, 조사는 마지막
# 낱말이 결정하므로 그 낱말 검사로 덮인다.
WORDS = {}
for en in TIER1.values():
    last = en.split()[-1]
    w = re.sub(r"[^A-Za-z-]", "", last)
    if len(w) < 3:
        continue
    c = josa.ending_class(w)
    if c:
        WORDS[w] = c

PATS = [(w, re.compile(r"\b" + re.escape(w) + r"(" +
                       "|".join(josa.WRONG_JOSA[c]) + r")", re.I))
        for w, c in sorted(WORDS.items())]

CODE = re.compile(r"`[^`]*`")
SUB = re.compile(r"<sub>.*?</sub>")
STRIP = (md_lint._MATH_SPAN_RE, CODE, md_lint._LINK_ALL_RE, SUB)


def targets(argv):
    if argv:
        return argv
    import glob
    return sorted(glob.glob(os.path.join(ROOT, "_posts/Math/**/ko/*.md"),
                            recursive=True))


def main(argv):
    if not josa.HAS_CMUDICT:
        print("! cmudict 없음 — 끝소리 판정이 철자 폴백이라 오탐이 늘 수 있다 "
              "(~/.venvs/josa/bin/python 으로 실행 권장)", file=sys.stderr)
    if argv and argv[0] == "--terms":
        for w, c in sorted(WORDS.items()):
            print(f"{c}  {w}")
        print(f"-- 검사 낱말 {len(WORDS)}개 "
              f"(cmudict={'있음' if josa.HAS_CMUDICT else '없음'})")
        return 0

    bad = 0
    for rel in targets(argv):
        path = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
        try:
            lines = list(prose_lines(path))
        except OSError:
            continue
        for ln, text in lines:
            # 수식·코드·링크·병기 안은 조사 검사 대상이 아니다
            for rx in STRIP:
                text = rx.sub(" ", text)
            for w, pat in PATS:
                for m in pat.finditer(text):
                    rp = os.path.relpath(path, ROOT)
                    print(f"{rp}:{ln}: {m.group(0)!r} "
                          f"({w}={WORDS[w]})")
                    bad += 1
    print(f"-- 조사 오류 {bad}건 / 검사 낱말 {len(WORDS)}개")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
