#!/usr/bin/env python3
"""용어 영어화 스윕 (2026-08-18) — terms.yml primary: en 항목의 한국어형·혼합표기 정리.

대상: closed/open subscheme, minor, free module, locally free sheaf,
infinitesimal deformation·lifting, diagonal morphism, defining ideal.

마스킹(치환 금지 구역): frontmatter 블록, code fence·inline code, 수식
($$...$$, $...$, \\tag{}), 헤딩, `:::` 여는 줄, 마크다운 링크 전체,
<sub> 병기, Liquid 태그. 마스킹 영역이 한 글자라도 변하면 abort한다.

사용법:
    python3 scripts/sweeps/term_english_20260818.py            # dry-run diff
    python3 scripts/sweeps/term_english_20260818.py --apply    # 실제 쓰기
"""
import difflib
import pathlib
import re
import shutil
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
BACKUP = pathlib.Path("/var/tmp") / f"term_sweep_{time.strftime('%Y%m%d_%H%M%S')}"

MASKS = [
    re.compile(r"\A---\n.*?\n---\n", re.S),          # frontmatter (title·description 포함)
    re.compile(r"```.*?```", re.S),                   # code fence
    re.compile(r"`[^`\n]*`"),                         # inline code
    re.compile(r"\{%.*?%\}", re.S),                   # Liquid (diagram alt 등)
    re.compile(r"\$\$.*?\$\$", re.S),                 # display math
    re.compile(r"\$[^$\n]*\$"),                       # inline math
    re.compile(r"\\tag\{[^}]*\}"),
    re.compile(r"^\s{0,3}#{1,6} .*$", re.M),          # 헤딩
    re.compile(r"^:::.*$", re.M),                     # 라벨 정의 여는 줄
    re.compile(r"\[(?:\\.|[^\]\\])*\]\([^)]*\)"),     # 링크 전체 (§글제목 보호)
    re.compile(r"<sub>.*?</sub>", re.S),              # 한영 병기 gloss
]

# 조사는 음역 발음 기준으로 재선택한다 (소행렬식: 받침 有 → minor: 모음 끝).
# 계사(이다·이고·이기도)는 무엇이든 그대로 붙으므로 유지한다.
RULES = [
    (r"닫힌 부분스킴", "closed subscheme"),
    (r"열린 부분스킴", "open subscheme"),
    (r"닫힌 부분scheme", "closed subscheme"),
    (r"열린 부분scheme", "open subscheme"),
    (r"소행렬식들이다", "minor들이다"),
    (r"소행렬식들이", "minor들이"),
    (r"소행렬식들의", "minor들의"),
    (r"소행렬식들에", "minor들에"),
    (r"소행렬식들로", "minor들로"),
    (r"소행렬식들(?![가-힣])", "minor들"),
    (r"소행렬식이기도", "minor이기도"),
    (r"소행렬식이란", "minor란"),
    (r"소행렬식이다", "minor이다"),
    (r"소행렬식이고", "minor이고"),
    (r"소행렬식이", "minor가"),
    (r"소행렬식은", "minor는"),
    (r"소행렬식을", "minor를"),
    (r"소행렬식과", "minor와"),
    (r"소행렬식으로", "minor로"),
    (r"소행렬식의", "minor의"),
    (r"소행렬식에", "minor에"),
    (r"소행렬식(?![가-힣])", "minor"),
    (r"국소자유 sheaf", "locally free sheaf"),
    (r"국소자유이고", "locally free이고"),
    (r"국소자유(?![가-힣])", "locally free"),     # '국소자유성'은 문장 재작성이 필요해 제외
    (r"자유 가군", "free module"),
    (r"자유 module", "free module"),
    (r"무한소 변형", "infinitesimal deformation"),
    (r"무한소 lifting", "infinitesimal lifting"),
    (r"대각선 morphism", "diagonal morphism"),
    (r"정의 ideal", "defining ideal"),
]
RULES = [(re.compile(p), r) for p, r in RULES]

# 기계 치환 대상이 아니라 사람이 판단할 것 — 문장 재작성이 필요하거나 SoT 근거가 없다.
REVIEW = [
    (re.compile(r"국소자유성[가-힣]*"), "문장 재작성 필요 (…가 locally free라는 것)"),
    (re.compile(r"(?<![린힌] )부분스킴[가-힣]*"), "terms.yml에 bare subscheme 항목 없음"),
]

SENTINEL = "\x00%d\x00"


def mask(text):
    store = []

    def take(m):
        store.append(m.group(0))
        return SENTINEL % (len(store) - 1)

    for rx in MASKS:
        text = rx.sub(take, text)
    return text, store


def unmask(text, store):
    # 마스크는 중첩된다 (헤딩·`:::` 줄·링크가 이미 자리표시자가 된 수식을 품는다).
    # 바깥 마스크가 항상 더 큰 번호이므로 역순으로 풀어야 안쪽까지 복원된다.
    for i in range(len(store) - 1, -1, -1):
        text = text.replace(SENTINEL % i, store[i])
    return text


def sweep(text):
    masked, store = mask(text)
    holes = masked.count("\x00")
    counts = {}
    for rx, repl in RULES:
        masked, n = rx.subn(repl, masked)
        if n:
            counts[rx.pattern] = counts.get(rx.pattern, 0) + n
    if masked.count("\x00") != holes:
        raise SystemExit("ABORT: 마스킹 자리표시자가 치환에 훼손되었다")
    new = unmask(masked, store)
    if "\x00" in new:
        raise SystemExit("ABORT: 복원되지 않은 자리표시자가 남았다")
    # 실제 파일을 다시 마스킹해 보호구역이 한 글자도 안 변했음을 확인한다.
    if mask(new)[1] != store:
        raise SystemExit("ABORT: 마스킹 영역(수식·링크·헤딩·병기)이 변경되었다")
    return new, counts


def review_hits(text):
    masked, _ = mask(text)
    out = []
    for rx, why in REVIEW:
        for m in rx.finditer(masked):
            out.append((m.group(0), why))
    return out


def main(apply_):
    targets = sorted(p for p in ROOT.glob("_posts/*/*/ko/*.md"))
    total, touched, review = {}, [], []
    for path in targets:
        src = path.read_text(encoding="utf-8")
        new, counts = sweep(src)
        for hit, why in review_hits(src):
            review.append((path, hit, why))
        if new == src:
            continue
        touched.append(path)
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        rel = path.relative_to(ROOT)
        if apply_:
            dst = BACKUP / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dst)
            path.write_text(new, encoding="utf-8")
        else:
            sys.stdout.writelines(difflib.unified_diff(
                src.splitlines(True), new.splitlines(True),
                f"a/{rel}", f"b/{rel}"))

    print(f"\n=== {'적용' if apply_ else 'dry-run'}: {len(touched)}개 파일 ===")
    for k, v in sorted(total.items(), key=lambda kv: -kv[1]):
        print(f"  {v:4d}  {k}")
    if apply_:
        print(f"백업: {BACKUP}")
    if review:
        print(f"\n=== 사람 판단 필요 {len(review)}건 ===")
        for path, hit, why in review:
            print(f"  {path.relative_to(ROOT)}: '{hit}' — {why}")


if __name__ == "__main__":
    main("--apply" in sys.argv[1:])
