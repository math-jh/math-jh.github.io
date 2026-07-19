#!/usr/bin/env python3
"""스윕이 만들어낸 "영단어 + 한국어 명사" 잡종어를 찾는다.

매핑에 있는 말(유계·기약·몫…)이 한국어 복합명사의 앞부분일 때 워커가 앞만
치환하면 `bounded함수`·`quotient대상` 같은 꼴이 남는다.

판정: 영단어 바로 뒤의 한글 꼬리가 **내용어(명사)로 시작하면** 잡종어.
명사 사전은 _data/terms.yml 의 한국어 표제어(자기유지됨)와, 표제어가 되지
못하는 접미명사(성·값·원·렬…) 손목록을 합쳐 만든다. 조사·활용어미로 시작하는
꼬리(`ring이`·`smooth한`·`algebra로서`)는 정상이므로 걸리지 않는다.

사용: hybrids.py            (커밋 대비 diff — 스윕이 새로 만든 것만)
      hybrids.py --all      (작업본 전체)
"""
import collections
import re
import subprocess
import sys

REPO = "/home/junhyeok/math-jh.github.io"

# terms.yml 표제어가 되기 어려운 접미명사
EXTRA = ["대상", "함수", "사상", "공간", "다양체", "복합체", "성", "값", "개",
         "원", "렬", "장", "류", "점", "꼴", "족", "열", "군", "환", "체", "층",
         "군의", "차수", "계수", "올", "덮개", "매장", "다발", "가군", "대수"]


def ko_terms():
    terms = set(EXTRA)
    y = open(f"{REPO}/_data/terms.yml", encoding="utf-8").read()
    for m in re.finditer(r"^\s*ko:\s*(.+?)\s*$", y, re.M):
        t = m.group(1).strip().strip("\"'")
        if re.fullmatch(r"[가-힣]{1,10}", t):
            terms.add(t)
    return sorted(terms, key=len, reverse=True)


NOUNS = ko_terms()
WORD = re.compile(r"\b([A-Za-z][A-Za-z\-]{2,})([가-힣]+)")

# 사용자가 스윕 이전부터 쓰던 표기 — 스윕 산물이 아니다
ALLOW = {"space값", "groupoid값", "clacky성", "automorphism군", "compact성",
         "root별"}


def is_hybrid(tail):
    return any(tail.startswith(n) for n in NOUNS)


def scan(lines):
    hits = collections.Counter()
    for line in lines:
        for m in WORD.finditer(line):
            whole, tail = m.group(0), m.group(2)
            if any(whole.startswith(a) for a in ALLOW):
                continue
            if is_hybrid(tail):
                hits[whole] += 1
    return hits


def grep_all(rev=None):
    """작업본(rev=None) 또는 특정 커밋에서 영단어+한글 꼴을 전부 긁는다."""
    cmd = ["git", "grep", "-h", "-P", r"[A-Za-z]{3,}[\x{AC00}-\x{D7A3}]"]
    if rev:
        cmd += [rev]
    cmd += ["--", "_posts"]
    return subprocess.run(cmd, cwd=REPO, capture_output=True,
                          text=True).stdout.splitlines()


now = scan(grep_all())
if "--all" in sys.argv:
    hits = now
else:
    # 스윕 이전부터 있던 표기(사용자 문체)는 제외하고, 늘어난 만큼만 본다.
    # diff 의 +줄만 보면 같은 줄의 기존 잡종어까지 잡히므로 개수를 비교한다.
    base = scan(grep_all("HEAD"))
    hits = collections.Counter()
    for w, c in now.items():
        d = c - base.get(w, 0)
        if d > 0:
            hits[w] = d
if not hits:
    print(f"잡종어 없음 (명사 사전 {len(NOUNS)}개 기준)")
    sys.exit(0)

print(f"잡종어 {sum(hits.values())}건 / {len(hits)}종")
for w, c in hits.most_common():
    print(f"{c:3d}  {w}")
    loc = subprocess.run(["git", "grep", "-n", "-F", w, "--", "_posts"],
                         cwd=REPO, capture_output=True, text=True).stdout
    for line in loc.splitlines()[:2]:
        path, _, rest = line.partition(":")
        print(f"       {path.split('/')[-1]}:{rest[:95]}")
sys.exit(1)
