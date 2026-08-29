#!/usr/bin/env python3
"""결정적 용어 스윕 — terms.yml primary:en 의 ko형을 영어로 기계 치환.

LLM 없이 동작한다. 판정 불가능한 경우(미등록 한글 복합어, 모르는 조사 run)는
건드리지 않고 mech_ambig.txt 로 뽑는다.

사용: mech_sweep.py [--apply] [파일...]     (기본: 전체 published:false 초안, dry-run)
      mech_sweep.py --classify              (영어 끝소리 분류표만 출력)
"""
import glob
import os
import re
import sys

sys.path.insert(0, "/home/junhyeok/math-jh.github.io/scripts/term-extraction")
sys.path.insert(0, "/home/junhyeok/math-jh.github.io/.agents/hooks")
import md_lint  # noqa: E402

ROOT = "/home/junhyeok/math-jh.github.io"
TIER1, GUARD = md_lint._DEPR

# ── 영어 최종 단어의 음역 끝소리 분류 ────────────────────────────────────────
# 단일 출처는 josa.py (cmudict 발음 + 외래어 표기법). 예전에는 이 파일과
# josa_check.py 가 137개짜리 손유지 표를 각자 복사해 들고 있었다.
from josa import ending_class, confident_class  # noqa: E402


CLS = {}   # ko형 → (en형, 끝소리 class)
UNCLASSIFIED = []
for ko, en in TIER1.items():
    final = en.split()[-1]
    c = ending_class(final)
    if c is None:
        UNCLASSIFIED.append((ko, en, final))
        c = "C"  # 보수적 기본값 (틀리면 josa 재수리 패스가 잡는다)
    CLS[ko] = (en, c)

# 관형사류 (2026-07-20 사용자 룰 B): 뒤 명사까지 표준 영어 용어(tier1)면
# 구 전체를 영어로, 아니면 한글 유지(ambig). 서술형(이다/인…)은 fleet 관례대로
# "<en>하다/한". 그 밖의 용법은 보류.
ADJ_MAP = {"대수적": "algebraic", "정수적": "integral",
           "초월적": "transcendental", "반사적": "reflexive",
           "비대칭적": "asymmetric", "비퇴화": "nondegenerate",
           "선형동치": "linearly equivalent", "대각화가능": "diagonalizable",
           "더 섬세한": "finer", "국소적으로 닫힌": "locally closed",
           "국소적으로 유한": "locally finite"}
COP2HADA = {"이다": "하다", "인": "한", "이고": "하고", "이며": "하며",
            "이므로": "하므로", "이면": "하면", "이지만": "하지만"}
# 하다-동사 활용 (사용자 룰 D): "정규화하면" → "normalize하면"
VERB_MAP = {"정규화": "normalize", "국소화": "localize",
            "대각화": "diagonalize", "선형화": "linearize",
            "콤팩트화": "compactify", "특수화": "specialize"}
NO_AUTO = set(ADJ_MAP)

# 카테고리 다의어: bare '다양체'는 AG 계열에선 variety, 미분기하 계열에선
# manifold 다. 카테고리가 불명확하면 자동 치환하지 않고 ambig 로 보낸다.
VARIETY_CATS = {"Algebraic_Varieties", "Algebraic_Geometry", "Toric_Geometry",
                "Scheme_Theory", "Commutative_Algebra", "Stacks",
                "Derived_Algebraic_Geometry", "Algebraic_Structures",
                "Gromov_Witten_Theory"}  # GW=AG 계열 (사용자 룰 C). MS 는 보류.
MANIFOLD_CATS = {"Manifolds", "Riemannian_Geometry", "Complex_Geometry",
                 "Symplectic_Geometry", "Algebraic_Topology", "Topology",
                 "Lie_Theory", "Complex_Analysis",
                 "Sheaf_Theory"}  # Verdier·six functors 의 bare 다양체 (실측 확인)


def context_en(w, path):
    """카테고리 의존 타깃. None = 자동 금지(ambig)."""
    cat = path.split("/_posts/Math/")[1].split("/")[0] \
        if "/_posts/Math/" in path else ""
    if w == "다양체":
        if cat in VARIETY_CATS:
            return "variety"
        if cat in MANIFOLD_CATS:
            return "manifold"
        return None
    if w == "정칙성":
        # 사용자 룰 D: 카테고리로 판별 (CM regularity 문맥은 현재 출현 없음)
        return ("holomorphicity"
                if cat in ("Complex_Analysis", "Complex_Geometry")
                else "regularity")
    return CLS[w][0]

# ── 조사 변환 ────────────────────────────────────────────────────────────────
PAIR = {"은": 0, "는": 1, "이": 0, "가": 1, "을": 0, "를": 1, "과": 0, "와": 1}
PAIR_SET = {("은", "는"), ("이", "가"), ("을", "를"), ("과", "와")}
PAIR_FIX = {}
for a, b in PAIR_SET:
    PAIR_FIX[a] = (a, b)
    PAIR_FIX[b] = (a, b)
TAILS = {"", "의", "는", "도", "만"}
PLAIN_KEEP = {"의", "에", "에서", "에는", "에도", "에서는", "에서도", "도",
              "만", "만을", "만이", "까지", "부터", "마다", "조차", "보다",
              "처럼", "라도", "밖에", "뿐", "만큼", "에서만", "에서의", "마다의"}
COPULA_EXACT = {"인", "일", "임", "이"}  # '이'는 아래 pair 로직이 우선
COPULA_PREFIX = ("이다", "입니다", "이고", "이며", "이므로", "이면", "이지만",
                 "이지", "이어", "이었", "이던", "인데", "인지", "이니", "임을",
                 "임이", "임은", "이면서", "이기", "이라", "이려")


def fix_particle(run, cls):
    """치환 후 조사 run 을 끝소리 class 에 맞게 재선택. None = 판정 불가."""
    if run == "":
        return ""
    if run.startswith("들"):          # 복수 '들'(ㄹ)이 조사와 결합 — 그대로
        return run
    # 이라는/라는 계열 (+ "다양체라 하자" 의 이라/라)
    for c_form, v_form in (("이라는", "라는"), ("이라고", "라고"),
                           ("이란", "란"), ("이라", "라")):
        if run in (c_form, v_form):
            return v_form if cls == "V" else c_form
    # 으로/로 계열 (+꼬리)
    m = re.match(r"^(으로|로)(서|써|부터|는|도|의|만)?$", run)
    if m:
        stem = "로" if cls in ("V", "L") else "으로"
        return stem + (m.group(2) or "")
    # 계사 — 무엇이든 그대로 붙는다
    if run in COPULA_EXACT - {"이"} or run.startswith(COPULA_PREFIX):
        return run
    if run in PLAIN_KEEP:
        return run
    # 짝 조사 (+제한된 꼬리)
    if run[0] in PAIR_FIX and run[1:] in TAILS:
        c_form, v_form = PAIR_FIX[run[0]]
        return (v_form if cls == "V" else c_form) + run[1:]
    return None


# 띄어쓰기 변이: en-확정 ko 에 공백 포함이 204종 — 본문이 붙여 쓴 형태도 잡는다
for ko in list(TIER1):
    s = ko.replace(" ", "")
    if s != ko and len(s) >= 3 and s not in TIER1:
        TIER1[s] = TIER1[ko]
        CLS[s] = CLS[ko]
# 반대 방향(붙여 쓴 표제어의 띄어 쓴 변이)은 분리점을 알 수 없어 손목록
for spaced, solid in (("복소 다양체", "복소다양체"), ("위상 다양체", "위상다양체"),
                      ("리만 다양체", "리만다양체"), ("적분 다양체", "적분다양체"),
                      ("대수 다양체", "대수다양체")):
    if solid in TIER1 and spaced not in TIER1:
        TIER1[spaced] = TIER1[solid]
        CLS[spaced] = CLS[solid]
GUARD = set(GUARD)
for g in list(GUARD):
    s = g.replace(" ", "")
    if s != g and len(s) >= 3:
        GUARD.add(s)

# ── 라인 마스킹 ──────────────────────────────────────────────────────────────
CODE_RE = re.compile(r"`[^`]*`")
MATH_RE = md_lint._MATH_SPAN_RE
LINK_RE = md_lint._LINK_ALL_RE
SUB_RE = re.compile(r"<sub>.*?</sub>")
FLIP_RE = re.compile(r"\*([가-힣][가-힣 ]{0,24})<sub>([^<]*[A-Za-z][^<]*)</sub>\*")

WORDS = sorted(set(TIER1) | set(GUARD), key=len, reverse=True)
WORD_RE = re.compile("|".join(re.escape(w) for w in WORDS))
TIER1_BY_LEN = sorted(TIER1, key=len, reverse=True)
RUN_RE = re.compile(r"[가-힣]*")


def mask(text, store):
    def put(m):
        store.append(m.group(0))
        return f"\x00{len(store)-1}\x01"
    for rx in (MATH_RE, CODE_RE, LINK_RE, SUB_RE):
        text = rx.sub(put, text)
    return text


def unmask(text, store):
    # 마스크가 중첩될 수 있다 (<sub> 안의 수식 등) — 남지 않을 때까지 복원
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x01",
                      lambda m: store[int(m.group(1))], text)
    return text


def sweep_line(line, stats, ambig, path, ln):
    store = []
    # 1) 정의 현장 병기 뒤집기: *한국어<sub>en</sub>* → *en<sub>한국어</sub>*
    def flip(m):
        ko, en = m.group(1).strip(), m.group(2).strip()
        if ko in TIER1:
            stats["flip"] += 1
            return f"*{en}<sub>{ko}</sub>*"
        return m.group(0)
    line = FLIP_RE.sub(flip, line)
    # 반전된 병기 `*english<sub>한국어</sub>*` 바로 뒤 조사도 영어 끝소리로 재선택
    def flip_josa(m):
        final = m.group(1).split()[-1]
        cls = ending_class(final)
        if cls is None:
            return m.group(0)
        fixed = fix_particle(m.group(2), cls)
        if fixed is None or fixed == m.group(2):
            return m.group(0)
        stats["josa"] += 1
        return m.group(0)[: -len(m.group(2))] + fixed
    line = re.sub(r"\*([A-Za-z][^*<]*)<sub>[가-힣][^<]*</sub>\*([가-힣]+)",
                  flip_josa, line)
    text = mask(line, store)
    # 2) 용어 치환 (최장일치, guard 는 통과)
    out, pos = [], 0
    for m in WORD_RE.finditer(text):
        w = m.group(0)
        if m.start() < pos:
            continue
        if w not in TIER1:                       # guard 단어: 그대로
            out.append(text[pos:m.end()]); pos = m.end(); continue
        prev = text[m.start() - 1] if m.start() > 0 else ""
        if re.match(r"[가-힣]", prev):            # 미등록 복합어의 꼬리
            ambig.append((path, ln, f"복합어(앞): …{prev}{w}"))
            out.append(text[pos:m.end()]); pos = m.end(); continue
        run = RUN_RE.match(text, m.end()).group(0)
        if w in ADJ_MAP:                          # 룰 B: 관형사류
            adj_en = ADJ_MAP[w]
            if run in COP2HADA:                   # 서술형 → "<en>하다" 꼴
                out.append(text[pos:m.start()])
                out.append(adj_en + COP2HADA[run])
                pos = m.end() + len(run); stats["repl"] += 1; continue
            mW = re.match(r" ([가-힣]{2,14})", text[m.end():]) \
                if run == "" else None
            if mW:                                # 관형 + 명사구
                W = mW.group(1)
                cand = next((k for k in TIER1_BY_LEN
                             if W.startswith(k) and k not in NO_AUTO), None)
                if cand:
                    en2 = context_en(cand, path)
                    if en2:
                        cls2 = ending_class(en2.split()[-1]) or CLS[cand][1]
                        fixed2 = fix_particle(W[len(cand):], cls2)
                        if fixed2 is not None:
                            out.append(text[pos:m.start()])
                            out.append(f"{adj_en} {en2}{fixed2}")
                            pos = m.end() + 1 + len(W)
                            stats["repl"] += 2; continue
            ambig.append((path, ln, f"관형 보류: {w}"))
            out.append(text[pos:m.end()]); pos = m.end(); continue
        if w in VERB_MAP and re.match(r"^(하|한|할|함|했|되|된|될|됨|됐)", run):
            out.append(text[pos:m.start()])       # 룰 D: "normalize하면" 허용
            out.append(VERB_MAP[w] + run)
            pos = m.end() + len(run); stats["repl"] += 1; continue
        en = context_en(w, path)
        if en is None:
            ambig.append((path, ln, f"카테고리 판정불가: {w}"))
            out.append(text[pos:m.end()]); pos = m.end(); continue
        cls = ending_class(en.split()[-1]) or CLS[w][1]
        if run.startswith("정리"):                # 열린사상정리 → open mapping 정리
            fixed = " " + run
        else:
            fixed = fix_particle(run, cls)
        if fixed is None:
            ambig.append((path, ln, f"조사 판정불가: {w}+{run}"))
            out.append(text[pos:m.end()]); pos = m.end(); continue
        out.append(text[pos:m.start()]); out.append(en); out.append(fixed)
        pos = m.end() + len(run)
        stats["repl"] += 1
    out.append(text[pos:])
    return unmask("".join(out), store)


# ── 기존 영어 용어의 조사 오류 수리 (class은 → class는 등) ───────────────────
# 저자가 이미 쓴 조사를 고치는 패스이므로, 음역이 사전으로 확정된(고신뢰
# 경로) 단어 전체에 적용한다 (tier1 유도 금지 — 조건부·단축 매핑의 영어형(bounded·
# preimage 등)도 스윕이 도입했으므로 수리 대상이다). 규칙 추정 분류는 신규
# 치환에만 쓴다 (polytope 사례).
FINALS = {}
for _en in TIER1.values():
    _f = re.sub(r"[^A-Za-z-]", "", _en.split()[-1])
    _c = confident_class(_f) if len(_f) >= 3 else None
    if _c:
        FINALS[_f.lower()] = _c
JOSA_FIX = []
for fw, cls in FINALS.items():
    esc = "(?i:" + re.escape(fw) + ")"
    if cls == "V":
        JOSA_FIX.append((re.compile(esc + r"(은|을|과)(?![가-힣])"),
                         lambda m: m.group(0)[:-1] + PAIR_FIX[m.group(1)][1]))
        JOSA_FIX.append((re.compile(esc + r"이(?![가-힣])"),
                         lambda m: m.group(0)[:-1] + "가"))
        JOSA_FIX.append((re.compile(esc + r"으로"), lambda m: m.group(0)[:-2] + "로"))
        JOSA_FIX.append((re.compile(esc + r"이라는"), lambda m: m.group(0)[:-3] + "라는"))
    elif cls == "C":
        JOSA_FIX.append((re.compile(esc + r"(는|를|와)(?![가-힣])"),
                         lambda m: m.group(0)[:-1] + PAIR_FIX[m.group(1)][0]))
        JOSA_FIX.append((re.compile(esc + r"가(?![가-힣])"),
                         lambda m: m.group(0)[:-1] + "이"))
        JOSA_FIX.append((re.compile(esc + r"(?<![으])로(서|써|부터)?(?![가-힣])"),
                         lambda m: m.group(0).replace("로", "으로", 1)))
        JOSA_FIX.append((re.compile(esc + r"(?<!이)라는"),
                         lambda m: m.group(0)[:-2] + "이라는"))
    else:  # L
        JOSA_FIX.append((re.compile(esc + r"(는|를|와)(?![가-힣])"),
                         lambda m: m.group(0)[:-1] + PAIR_FIX[m.group(1)][0]))
        JOSA_FIX.append((re.compile(esc + r"가(?![가-힣])"),
                         lambda m: m.group(0)[:-1] + "이"))
        JOSA_FIX.append((re.compile(esc + r"으로"), lambda m: m.group(0)[:-2] + "로"))


def repair_josa(line, stats, store):
    text = mask(line, store)
    for rx, fn in JOSA_FIX:
        text, n = rx.subn(fn, text)
        stats["josa"] += n
    return unmask(text, store)


# ── 파일 처리 (prose 구역 판정) ──────────────────────────────────────────────
def process(path, stats, ambig):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = list(lines)
    i, n = 0, len(lines)
    if lines and lines[0].strip() == "---":       # frontmatter
        i = 1
        while i < n and lines[i].strip() != "---":
            i += 1
        i += 1
    in_fence = in_math = in_raw = False
    refs = False
    for j in range(i, n):
        raw = lines[j]
        s = raw.strip()
        if refs:
            continue
        if s == "**참고문헌**":
            refs = True; continue
        if re.match(r"^ {0,3}(`{3,}|~{3,})", raw):
            in_fence = not in_fence; continue
        if in_fence:
            continue
        if re.match(r"^\s*\{%\s*raw\s*%\}", raw):
            in_raw = True; continue
        if re.match(r"^\s*\{%\s*endraw\s*%\}", raw):
            in_raw = False; continue
        if in_raw:
            continue
        if in_math:
            if raw.count("$$") % 2 == 1:   # 닫는 줄 (\end{aligned}$$ 포함)
                in_math = False
            continue
        if raw.count("$$") % 2 == 1:       # 여는 줄
            in_math = True; continue
        if re.match(r"^#{1,6}\s", s):             # 헤딩 보호
            continue
        if s.startswith(":::"):                   # 라벨 정의 여는 줄 보호 — 손 수정 대상
            continue
        st = []
        new = sweep_line(raw, stats, ambig, path, j + 1)
        new = repair_josa(new, stats, st)
        if new != raw:
            out[j] = new
            stats["lines"] += 1
    return "\n".join(out)


def main():
    apply = "--apply" in sys.argv
    josa_only = "--josa-only" in sys.argv
    if "--classify" in sys.argv:
        for ko, en, final in UNCLASSIFIED:
            print(f"미분류: {final}  ({ko} → {en})")
        print(f"-- 미분류 {len(UNCLASSIFIED)} / {len(CLS)}")
        return
    if josa_only:
        # 조사 수리는 스윕이 도입한 오류의 교정이므로 발행글도 대상
        global sweep_line
        sweep_line = lambda line, stats, ambig, path, ln: line
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if args:
        targets = args
    elif josa_only:
        targets = sorted(glob.glob(f"{ROOT}/_posts/Math/**/ko/*.md",
                                   recursive=True))
    else:
        pubf = re.compile(r"^published\s*:\s*false", re.M)
        targets = [p for p in sorted(glob.glob(
                       f"{ROOT}/_posts/Math/**/ko/*.md", recursive=True))
                   if pubf.search(open(p, encoding="utf-8").read(2000))]
    total = {"repl": 0, "flip": 0, "josa": 0, "lines": 0}
    ambig = []
    changed = []
    for p in targets:
        stats = {"repl": 0, "flip": 0, "josa": 0, "lines": 0}
        new = process(p, stats, ambig)
        if stats["lines"]:
            changed.append((p, stats))
            if apply:
                open(p, "w", encoding="utf-8").write(new)
        for k in total:
            total[k] += stats[k]
    for p, st in changed:
        print(f"{os.path.relpath(p, ROOT)}: 치환 {st['repl']}, 병기반전 "
              f"{st['flip']}, 조사수리 {st['josa']}")
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"== [{mode}] 파일 {len(changed)}/{len(targets)}, 치환 {total['repl']}, "
          f"병기반전 {total['flip']}, 조사수리 {total['josa']}, 애매 {len(ambig)}")
    with open(f"{ROOT}/scripts/term-extraction/mech_ambig.txt", "w",
              encoding="utf-8") as f:
        for path, ln, msg in ambig:
            f.write(f"{os.path.relpath(path, ROOT)}:{ln}: {msg}\n")


if __name__ == "__main__":
    main()
