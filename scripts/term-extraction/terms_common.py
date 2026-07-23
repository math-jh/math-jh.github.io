#!/usr/bin/env python3
"""terms_common.py — 찾아보기 데이터(_data/terms.yml) 공용 라이브러리.

extract_terms.py(수확기)와 terms_lint.py(검증·정규화기)가 공유하는 규칙을 한
곳에 둔다. 2026-07-18 Index_ko.md(마크다운 표) → terms.yml 이전 때 실측된
드리프트들이 이 모듈의 존재 이유다:

  * 글자 분류 — 수식 래퍼는 속 글자로 풀고($\\mathfrak{a}$-adic → A), 발음
    기호는 NFD 분해로 접는다(Čech → C). 옛 변환은 이걸 안 해서 수식·Č 시작
    용어 28개가 전부 Z 절로 밀렸다.
  * 중복 판정 — id/en 원문 비교로는 Čech_*/čech_* 같은 대소문자·발음기호
    변형을 못 잡는다(실제로 중복 2쌍이 그렇게 살아남았다). dedup_key 로.
  * 라벨 정본 — 대괄호는 categories.yml 의 ko 표시명, § 뒤는 대상 글의
    "현재" frontmatter title. 하드코딩 표(옛 CATEGORY_KO)와 수확 당시 제목은
    반드시 드리프트한다(실측: 대괄호 114건·제목 83건이 어긋나 있었다).
  * 정렬 — 숫자 인지 자연 정렬. 평문 키로는 $T_{2\\frac{1}{2}}$-space 가
    T_1 과 T_2 사이에 꽂힌다(frac 의 f 가 space 의 s 보다 앞이라서).

semantic_checks() 는 두 소비자가 공유하는 검사기다: lint 는 이 결과를
보고·수정하고, 수확기는 쓰기 직전 게이트로 쓴다(새 에러가 생기면 쓰지 않음).
"""
from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

import yaml

BLOG_ROOT = Path("/home/junhyeok/math-jh.github.io")
TERMS_PATH = BLOG_ROOT / "_data" / "terms.yml"
CATEGORIES_PATH = BLOG_ROOT / "_data" / "categories.yml"

# 교양수학 카테고리. 2026-07-21 룰링: 이들 카테고리의 정의는
# 커리큘럼상 선행이지만 '정식 거처'가 아니므로, 어떤 용어의 defs가 전부
# 교양수학뿐이면 이후 전공 글의 정의를 뉘앙스 판정 없이 defs에 추가한다.
#
# 단일 출처 = _data/categories.yml 의 `section: liberal_arts` (이중 SoT 감사
# [U2], 2026-07-22). 예전엔 여기(슬러그)와 gloss_backfill(폴더명)에 각각
# 하드코딩돼 있었다 — 교양 카테고리가 늘면 yml 의 section 만 바꾸면 된다.


def _gen_ed_sets() -> tuple[frozenset, frozenset]:
    """(url 슬러그 집합, _posts/Math/<Category> 폴더명 집합)."""
    cats = yaml.safe_load(CATEGORIES_PATH.read_text(encoding="utf-8"))
    slugs, dirs = set(), set()
    for name, info in (cats.get("subjects") or {}).items():
        if (info or {}).get("section") == "liberal_arts":
            base = name.split(" / ")[-1].replace(" ", "_")
            dirs.add(base)
            slugs.add(base.lower())
    return frozenset(slugs), frozenset(dirs)


GEN_ED_CATS, GEN_ED_DIRS = _gen_ed_sets()

# ---------------------------------------------------------------------------
# 정규화 (글자 분류·정렬·중복 키)
# ---------------------------------------------------------------------------

_WRAP_RE = re.compile(r"\\math(?:frak|bb|cal|rm|bf|sf|scr|it)\{([^{}]*)\}")
_FRAC_RE = re.compile(r"(\d+)\\frac\{(\d+)\}\{(\d+)\}")  # 2\frac{1}{2} → 2.5
_MACRO_RE = re.compile(r"\\([a-zA-Z]+)")


def fold(s: str) -> str:
    """수식·발음기호를 접은 평문. 분류·정렬·중복 판정의 공통 전처리."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = _FRAC_RE.sub(lambda m: str(int(m[1]) + int(m[2]) / int(m[3])), s)
    s = _WRAP_RE.sub(r"\1", s)
    s = _MACRO_RE.sub(r"\1", s)
    return s.replace("$", "")


def letter_of(en: str) -> str | None:
    """이 용어가 속할 절(A–Z). 라틴 글자가 하나도 없으면 None — 호출자가
    사람 리뷰로 돌려야 한다 (Z 에 던져 두는 건 오늘로 금지)."""
    m = re.search(r"[A-Za-z]", fold(en))
    return m.group(0).upper() if m else None


def nat_key(en: str):
    """숫자 인지 자연 정렬 키. T_0 < T_1 < T_2 < T_{2½} < T_3 이 되게
    숫자 토큰은 수치로 비교한다."""
    s = fold(en).lower()
    toks = re.findall(r"\d+(?:\.\d+)?|[a-z]+", s)
    return tuple(
        (0, float(t), "") if t[0].isdigit() else (1, 0.0, t) for t in toks
    )


def dedup_key(s: str) -> str:
    """대소문자·발음기호·수식 무시 중복 판정 키."""
    return re.sub(r"[^a-z0-9]", "", fold(s).casefold())


def slugify_id(en: str) -> str:
    """엔트리 id(앵커). 옛 수확기와 같은 알고리즘 — 기존 id 와의 호환이
    목적이므로 바꾸지 말 것."""
    s = en.lower().strip()
    s = re.sub(r"[^\w\-]+", "_", s, flags=re.UNICODE)
    return re.sub(r"_+", "_", s).strip("_")


# ---------------------------------------------------------------------------
# 인명 파생 고유명사 대문자 정규화
# ---------------------------------------------------------------------------
# 용어 추출 LLM 이 인명 파생 형용사를 자주 소문자로 낸다(hermitian form…).
# 색인 en 표기는 저장 직전 이 표로 강제 교정한다. 관용적으로 소문자인 형용사
# (abelian·cartesian·boolean)는 표에 넣지 않아 그대로 둔다 — 코퍼스·표준 관례.
# 키는 발음기호 접은 소문자, 값은 정본 표기(악센트 포함).
_PROPER_FORMS = {
    "hermitian": "Hermitian", "noetherian": "Noetherian", "artinian": "Artinian",
    "gaussian": "Gaussian", "hamiltonian": "Hamiltonian", "lagrangian": "Lagrangian",
    "jacobian": "Jacobian", "laplacian": "Laplacian", "lipschitz": "Lipschitz",
    "taylor": "Taylor", "maclaurin": "Maclaurin", "euler": "Euler", "cauchy": "Cauchy",
    "riemann": "Riemann", "riemannian": "Riemannian", "hausdorff": "Hausdorff",
    "dolbeault": "Dolbeault", "fubini": "Fubini", "study": "Study", "hodge": "Hodge",
    "rham": "Rham", "eilenberg": "Eilenberg", "whitney": "Whitney", "cartan": "Cartan",
    "tychonoff": "Tychonoff", "wirtinger": "Wirtinger", "galois": "Galois",
    "frobenius": "Frobenius", "grothendieck": "Grothendieck", "serre": "Serre",
    "zariski": "Zariski", "krull": "Krull", "dedekind": "Dedekind", "sylow": "Sylow",
    "fourier": "Fourier", "legendre": "Legendre", "bernoulli": "Bernoulli",
    "hilbert": "Hilbert", "banach": "Banach", "lebesgue": "Lebesgue", "weil": "Weil",
    "hopf": "Hopf", "poincare": "Poincaré", "betti": "Betti", "weyl": "Weyl",
    "weierstrass": "Weierstrass", "stokes": "Stokes", "newton": "Newton",
    "leibniz": "Leibniz", "kahler": "Kähler", "chern": "Chern", "ricci": "Ricci",
    "pontryagin": "Pontryagin", "stiefel": "Stiefel", "chevalley": "Chevalley",
    "bruhat": "Bruhat", "schubert": "Schubert", "plucker": "Plücker",
    "grassmann": "Grassmann", "grassmannian": "Grassmannian", "veronese": "Veronese",
    "segre": "Segre", "nakayama": "Nakayama", "yoneda": "Yoneda", "quillen": "Quillen",
    "postnikov": "Postnikov", "steenrod": "Steenrod", "morse": "Morse", "bott": "Bott",
    "cartier": "Cartier", "picard": "Picard", "jacobi": "Jacobi", "cayley": "Cayley",
    "sylvester": "Sylvester", "jordan": "Jordan", "schur": "Schur", "koszul": "Koszul",
    "wedderburn": "Wedderburn", "maschke": "Maschke", "burnside": "Burnside",
    "leray": "Leray", "thom": "Thom", "noether": "Noether", "artin": "Artin",
    "gauss": "Gauss", "laplace": "Laplace", "hensel": "Hensel", "witt": "Witt",
    "clifford": "Clifford", "minkowski": "Minkowski", "lorentz": "Lorentz",
    "dirichlet": "Dirichlet", "neumann": "Neumann", "sobolev": "Sobolev",
    "borel": "Borel", "baire": "Baire", "urysohn": "Urysohn", "zorn": "Zorn",
    "kronecker": "Kronecker", "wronskian": "Wronskian", "hessian": "Hessian",
    "green": "Green", "beltrami": "Beltrami", "riesz": "Riesz", "fatou": "Fatou",
}
_PROPER_LOOKUP = {
    "".join(c for c in unicodedata.normalize("NFD", k)
            if not unicodedata.combining(c)).lower(): v
    for k, v in _PROPER_FORMS.items()
}
_PROPER_TOKEN_RE = re.compile(r"[A-Za-zÀ-ÿ]+")


def _proper_sub(m: "re.Match") -> str:
    tok = m.group(0)
    key = "".join(c for c in unicodedata.normalize("NFD", tok)
                  if not unicodedata.combining(c)).lower()
    return _PROPER_LOOKUP.get(key, tok)


def normalize_proper_case(en: str) -> str:
    """en 표기의 인명 파생 고유명사를 정본 대문자형으로 교정한다.
    수식($...$) 구간은 건드리지 않고, 표에 없는 관용 소문자 형용사(abelian…)도
    그대로 둔다. 이미 올바른 표기는 멱등(idempotent)."""
    parts = re.split(r"(\$[^$]*\$)", en)
    for i in range(0, len(parts), 2):       # 짝수 인덱스 = 비수식 구간
        parts[i] = _PROPER_TOKEN_RE.sub(_proper_sub, parts[i])
    return "".join(parts)


# ---------------------------------------------------------------------------
# 레포 조회 (정본 소스)
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# `published: false` 초안 판정의 **단일 출처** (이중 SoT 감사 [9], 2026-07-22).
# 예전엔 4곳(여기 permalink_map·terms_usage_lint·deprecated_terms_lint·
# translate_worker)이 각자 다른 정규식/라인스캔으로 재구현해, `published : false`
# 같은 변형에서 판정이 갈릴 수 있었다. 콜론 앞 공백·대소문자·따옴표 변형을 전부
# 허용하고, 라인 전체를 매치해 `published_at:` 류 오인은 배제한다.
# (실코퍼스 규약은 `published: false` 한 형태뿐 — 허용 폭은 방어용이다.)
_PUB_FALSE_LINE_RE = re.compile(r"^published\s*:\s*['\"]?false['\"]?\s*$", re.I | re.M)


def published_false_in_fm(fm_block: str) -> bool:
    """frontmatter 블록 본문(`---` 사이 텍스트)만 갖고 있을 때의 판정."""
    return bool(_PUB_FALSE_LINE_RE.search(fm_block))


def is_draft(text: str) -> bool:
    """파일 전문(또는 head 절단본)에서 published:false 초안 판정.

    닫는 `---` 가 절단돼도 동작한다 — head 를 2000자만 읽는 호출자를 위해
    `\\n---` 이전(없으면 끝까지)을 frontmatter 로 본다."""
    if not text.startswith("---"):
        return False
    block = text[3:].split("\n---", 1)[0]
    return published_false_in_fm(block)


def _frontmatter(text: str) -> dict[str, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def permalink_map() -> dict[str, dict]:
    """permalink(끝 슬래시 제거) → {title, published, path}. _posts 전체와
    _pages 를 포함한다. 라벨 § 정본과 url 유효성 검사의 근거."""
    out: dict[str, dict] = {}
    for base in (BLOG_ROOT / "_posts", BLOG_ROOT / "_pages"):
        for p in base.rglob("*.md"):
            try:
                text = p.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            fm = _frontmatter(text)
            pl, title = fm.get("permalink"), fm.get("title")
            if not pl or not title:
                continue
            out[pl.rstrip("/")] = {
                "title": title,
                "published": not is_draft(text),  # 단일 출처 판정 (감사 [9])
                "path": str(p.relative_to(BLOG_ROOT)),
            }
    return out


def category_ko_maps() -> tuple[dict[str, str], dict[str, str]]:
    """(url 슬러그 → ko 표시명, "Math / X" → ko 표시명). 라벨 대괄호의 정본.
    categories.yml 에 없는 카테고리는 여기 없음 — 호출자는 없으면 에러를
    내야 한다 (옛 수확기처럼 영문 이름으로 대충 폴백하지 말 것)."""
    cats = yaml.safe_load(CATEGORIES_PATH.read_text(encoding="utf-8"))
    by_slug: dict[str, str] = {}
    by_name: dict[str, str] = {}
    for name, info in (cats.get("subjects") or {}).items():
        slug = name.split(" / ")[-1].lower().replace(" ", "_")
        by_slug[slug] = info["ko"]
        by_name[name] = info["ko"]
    return by_slug, by_name


def url_slug(url: str) -> str | None:
    """/ko/math/<slug>/... → <slug>."""
    seg = url.split("#")[0].strip("/").split("/")
    return seg[2] if len(seg) >= 3 and seg[1] == "math" else None


# ---------------------------------------------------------------------------
# terms.yml 텍스트 수술 (포맷 보존 파서/직렬화기)
# ---------------------------------------------------------------------------
# yaml.dump 재직렬화는 헤더 주석과 기존 인용 스타일을 다 날리므로, 파일을
# (헤더, 글자 → 엔트리 청크 목록) 으로 쪼개 청크 단위로만 만진다.

_GROUP_RE = re.compile(r"^([A-Z]):(\s*\[\]\s*)?$")


def split_file(text: str) -> tuple[list[str], dict[str, list[str]]]:
    header: list[str] = []
    groups: dict[str, list[str]] = {}
    cur: str | None = None
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = _GROUP_RE.match(lines[i])
        if m:
            cur = m.group(1)
            groups[cur] = []
            i += 1
            continue
        if cur is None:
            header.append(lines[i])
            i += 1
            continue
        if lines[i].startswith("- id:"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("- id:") \
                    and not _GROUP_RE.match(lines[j]):
                j += 1
            groups[cur].append("\n".join(lines[i:j]).rstrip("\n"))
            i = j
            continue
        i += 1  # 그룹 내 빈 줄 등
    while header and header[-1] == "":
        header.pop()
    return header, groups


def join_file(header: list[str], groups: dict[str, list[str]]) -> str:
    out = list(header)
    for letter in sorted(groups):
        if not groups[letter]:
            continue  # 빈 그룹은 쓰지 않는다 (조판이 깨진다)
        out.append(f"{letter}:")
        out.extend(groups[letter])
    return "\n".join(out) + "\n"


def chunk_field(chunk: str, field: str) -> str | None:
    m = re.search(rf"^  {field}: (.*)$", chunk, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if v.startswith(("'", '"')) and v.endswith(v[0]) and len(v) >= 2:
        v = v[1:-1].replace("''", "'") if v[0] == "'" else v[1:-1]
    return v


def chunk_id(chunk: str) -> str:
    m = re.match(r"^- id: (\S+)", chunk)
    return m.group(1) if m else ""


def yaml_quote(s: str) -> str:
    """단순 스칼라로 안전하면 그대로, 아니면 작은따옴표."""
    if re.match(r"^[A-Za-z0-9가-힣$\\(][^#]*$", s) and ": " not in s \
            and not s.endswith((" ", ":")) and "'" not in s:
        return s
    return "'" + s.replace("'", "''") + "'"


def render_entry(eid: str, en: str, ko: str, primary: str | None,
                 label: str, url: str) -> str:
    lines = [f"- id: {eid}",
             f"  en: {yaml_quote(en)}",
             f"  ko: {yaml_quote(ko)}"]
    if primary in ("ko", "en"):
        lines.append(f"  primary: {primary}")
    lines += ["  defs:",
              f"  - label: '{label.replace(chr(39), chr(39) * 2)}'",
              f"    url: {url}"]
    return "\n".join(lines)


def insert_sorted(chunks: list[str], chunk: str) -> None:
    """nat_key 순서상 첫 위치에 삽입 (기존 목록이 완벽 정렬이 아니어도
    이 정책이면 국소적으로 옳은 자리에 들어간다)."""
    k = nat_key(chunk_field(chunk, "en") or "")
    pos = len(chunks)
    for i, c in enumerate(chunks):
        if nat_key(chunk_field(c, "en") or "") > k:
            pos = i
            break
    chunks.insert(pos, chunk)


# ---------------------------------------------------------------------------
# 의미 검사 (lint 와 수확기 쓰기 게이트가 공유)
# ---------------------------------------------------------------------------

class Issue:
    def __init__(self, level: str, code: str, msg: str, fixable: bool = False):
        self.level, self.code, self.msg, self.fixable = level, code, msg, fixable

    def __repr__(self):
        return f"[{self.level}] {self.code}: {self.msg}"

    def key(self):
        return (self.code, self.msg)


# ko_short: 표제어가 부분열로 커버하지 못하는 단축 파생형 목록 (예: 자기동형사상
# 의 "자기동형"). md_lint 가 폐용어 감시에 파생해 쓴다 (이중 SoT 감사 [10]-별칭,
# 2026-07-22 — 예전엔 md_lint._DEPR_EXTRA 수동 목록).
ENTRY_KEYS = {"id", "en", "ko", "ko_short", "primary", "note", "defs", "refs", "see"}
REF_KEYS = {"label", "url"}
SEE_KEYS = {"label", "id", "lang"}


def semantic_checks(data: dict, pmap: dict[str, dict],
                    ko_by_slug: dict[str, str]) -> list[Issue]:
    issues: list[Issue] = []
    E, W = "E", "W"
    all_ids: Counter = Counter()
    en_keys: Counter = Counter()
    id_keys: dict[str, list[str]] = {}

    if not isinstance(data, dict):
        return [Issue(E, "PARSE", "최상위가 매핑이 아님")]

    for letter, terms in data.items():
        if terms is None or terms == []:
            issues.append(Issue(E, "EMPTY_GROUP", f"빈 그룹 {letter}", fixable=True))
            continue
        for t in terms:
            tid = t.get("id", "?")
            # 스키마 — ko 는 영문 전용 용어(epimorphism 등)에서 정당하게
            # 비어 있을 수 있으므로 경고만 (조판은 빈 ko 를 생략한다)
            for req in ("id", "en"):
                if not t.get(req):
                    issues.append(Issue(E, "SCHEMA", f"{tid}: {req} 누락/공백"))
            if not t.get("ko"):
                issues.append(Issue(W, "SCHEMA", f"{tid}: ko 비어 있음 (영문 전용이면 정상)"))
            unknown = set(t) - ENTRY_KEYS
            if unknown:
                issues.append(Issue(W, "SCHEMA", f"{tid}: 모르는 키 {sorted(unknown)}"))
            # 생략 = 미판정(표시상 en), en = prose 영어 확정(2026-07-19 스윕 룰링,
            # md_lint 훅·deprecated_terms_lint 가 이 ko 형을 prose 금지로 본다), ko = 한국어 확정
            if t.get("primary") not in (None, "ko", "en"):
                issues.append(Issue(E, "PRIMARY", f"{tid}: primary={t['primary']!r} (ko/en/생략만)"))
            all_ids[tid] += 1
            en_keys[dedup_key(t.get("en", ""))] += 1
            id_keys.setdefault(dedup_key(tid), []).append(tid)
            # 글자 분류
            lo = letter_of(t.get("en", ""))
            if lo is None:
                issues.append(Issue(E, "GROUP", f"{tid}: en 에 라틴 글자 없음 — 분류 불가"))
            elif lo != letter:
                issues.append(Issue(E, "GROUP", f"{tid}: {letter} 그룹에 있지만 {lo} 그룹이어야 함", fixable=True))
            # defs/refs
            for kind in ("defs", "refs"):
                for ref in (t.get(kind) or []):
                    if set(ref) - REF_KEYS:
                        issues.append(Issue(W, "SCHEMA", f"{tid}: {kind} 에 모르는 키 {sorted(set(ref) - REF_KEYS)}"))
                    url = (ref.get("url") or "").split("#")[0].rstrip("/")
                    label = ref.get("label") or ""
                    if url not in pmap:
                        issues.append(Issue(E, "URL", f"{tid}: {ref.get('url')} 이 어떤 글의 permalink 도 아님"))
                        continue
                    if not pmap[url]["published"]:
                        issues.append(Issue(W, "UNPUB", f"{tid}: {url} 은 published:false 초안 (발행 전까지 프로덕션 404)"))
                    slug = url_slug(url)
                    canon_cat = ko_by_slug.get(slug or "")
                    mb = re.match(r"^\[([^\]]*)\]\s*§(.*)$", label)
                    if not mb:
                        issues.append(Issue(E, "LABEL", f"{tid}: 라벨 형식이 '[카테고리] §제목' 이 아님: {label!r}", fixable=True))
                        continue
                    if canon_cat and mb.group(1) != canon_cat:
                        issues.append(Issue(E, "LABEL", f"{tid}: 대괄호 [{mb.group(1)}] ≠ categories.yml [{canon_cat}] ({url})", fixable=True))
                    if mb.group(2).strip() != pmap[url]["title"]:
                        issues.append(Issue(E, "LABEL", f"{tid}: §{mb.group(2).strip()!r} ≠ 현재 제목 {pmap[url]['title']!r} ({url})", fixable=True))
            # see
            for s in (t.get("see") or []):
                if set(s) - SEE_KEYS:
                    issues.append(Issue(W, "SCHEMA", f"{tid}: see 에 모르는 키 {sorted(set(s) - SEE_KEYS)}"))
                if s.get("lang") not in (None, "ko"):
                    issues.append(Issue(E, "LANG", f"{tid}: see.lang={s.get('lang')!r} (ko 또는 생략만)"))

    # 중복
    for tid, n in all_ids.items():
        if n > 1:
            issues.append(Issue(E, "DUP_ID", f"id {tid!r} 가 {n}회"))
    for k, ids in id_keys.items():
        if len(set(ids)) > 1:
            issues.append(Issue(E, "DUP_ID", f"정규화하면 같은 id: {sorted(set(ids))} (Čech/čech 류)"))
    for k, n in en_keys.items():
        if n > 1 and k:
            issues.append(Issue(E, "DUP_TERM", f"en 정규화 키 {k!r} 인 항목이 {n}개"))

    # see.id 대상 존재 (전체 id 수집 후에만 가능)
    idset = set(all_ids)
    for terms in data.values():
        for t in (terms or []):
            for s in (t.get("see") or []):
                if s.get("id") and s["id"] not in idset:
                    issues.append(Issue(E, "SEE", f"{t.get('id')}: see → {s['id']!r} 항목이 없음"))
    return issues
