#!/usr/bin/env python3
"""md_lint 가 건너뛰는 2글자 이하 ko 용어(primary:en) 후보 스캐너.

md_lint 의 영어화 확정 용어 검사는 오탐이 많아 3글자↑만 본다
(`.claude/hooks/md_lint.py` 의 `_load_deprecated`). 그 갭을 메운다.

마스킹은 md_lint 와 같은 것을 재사용하고(<sub> 병기·링크 라벨·frontmatter
키 줄·헤딩·수식), 여기에 '긴 한글 낱말 안에 박힌 부분열'을 조사 경계로
걸러 후보를 뽑는다. 2글자 이하는 일상어와 겹치는 것이 대부분이므로
**출력은 후보이지 판정이 아니다** — 사람이 문맥을 읽고 고른다.

    python3 scripts/audit/short_terms_scan.py <파일.md> [...]

exit code 는 언제나 0 (게이트가 아니다).
"""
import glob
import os
import re
import sys

import yaml

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(_ROOT, ".claude", "hooks"))
import md_lint as M  # noqa: E402

# 표제어 뒤에 붙을 수 있는 조사 — 긴 것부터 (최장일치)
_JOSA = (
    "에서의|으로서|이라는|이라고|에서는|에서도|으로는|으로도|이며|이고|이라|이다"
    "|인|과의|와의|들의|들을|들이|들은"
    "|은|는|이|가|을|를|와|과|의|에|도|만|나|로|랑|께|보다|처럼|부터|까지|마다|조차"
)


def load_short_terms():
    """primary:en · note 없음 · ko 가 순한글 1~2글자인 항목 (표제어 + ko_short)."""
    data = yaml.safe_load(open(os.path.join(_ROOT, "_data", "terms.yml"), encoding="utf-8"))
    entries = [e for sec in data.values() for e in sec]
    ko_fixed = {str(e.get("ko", "")).strip() for e in entries if e.get("primary") == "ko"}
    short = {}
    for e in entries:
        if e.get("primary") != "en" or e.get("note"):
            continue
        forms = [str(e.get("ko", "")).strip()]
        forms += [str(s).strip() for s in (e.get("ko_short") or [])]
        for ko in forms:
            if re.fullmatch(r"[가-힣]{1,2}", ko) and ko not in ko_fixed:
                short[ko] = str(e.get("en", "")).strip()
    return short


def scan(path, pats, short):
    body = open(path, encoding="utf-8").read()
    body = M._SUB_GLOSS_RE.sub("", body)
    body = M._LINK_ALL_RE.sub("", body)
    body = M._FM_KO_KEY_RE.sub("", body)
    body = M._HEADING_LINE_RE.sub("", body)
    body = M._MATH_SPAN_RE.sub(lambda m: " " * len(m.group(0)), body)
    hits = []
    for i, line in enumerate(body.split("\n"), 1):
        for w, rx in pats.items():
            for mo in rx.finditer(line):
                lo = max(0, mo.start() - 30)
                hits.append((i, w, short[w], line[lo:mo.end() + 30].strip()))
    return sorted(hits)


def main(argv):
    targets = []
    for a in argv:
        targets += sorted(glob.glob(a)) if any(c in a for c in "*?[") else [a]
    if not targets:
        print(__doc__)
        return 0
    short = load_short_terms()
    pats = {w: re.compile(rf"(?<![가-힣]){re.escape(w)}(?:{_JOSA})?(?![가-힣])") for w in short}
    print(f"# primary:en · ko 2글자 이하 = {len(short)}종 (md_lint 미검사 구간)")
    for path in targets:
        hits = scan(path, pats, short)
        print(f"\n=== {path} : 후보 {len(hits)}건 ===")
        for i, w, en, ctx in hits:
            print(f"L{i}\t{w} → {en}\t…{ctx}…")
        if not hits:
            print("  (없음)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
