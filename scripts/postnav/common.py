#!/usr/bin/env python3
"""postnav 공용 모듈 — 포스트 인덱스·라벨 파서·인용 단위 regex·보호구간.

박스 어휘의 단일 출처는 _data/theorem_vocab.yml (플러그인·번역 워커와 공유).
라벨 문법은 _plugins/fenced_theorem_blocks.rb 의 라인 스캔 파서를 미러링한다:
유도형 `::: 정의 1 (이름)`, 명시형 `::: <class> <라벨> {#id}`,
증명 부착형 `::: 증명`, 증명 단독형 `::: 증명 (명제 3)`.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
POSTS = ROOT / "_posts"

# ── 어휘 ────────────────────────────────────────────────────────────────────

VOCAB = yaml.safe_load((ROOT / "_data" / "theorem_vocab.yml").read_text(encoding="utf-8"))

# 종류 단어 → 앵커 접두사. ko·en 양쪽 키를 한 사전에.
KIND_PREFIX: dict[str, str] = {}
for k in VOCAB["kinds"]:
    KIND_PREFIX[k["ko"]] = k["prefix"]
    KIND_PREFIX[k["en"]] = k["prefix"]

# 접두사 → (ko 종류, en 종류)
PREFIX_KIND: dict[str, tuple[str, str]] = {k["prefix"]: (k["ko"], k["en"]) for k in VOCAB["kinds"]}

EXPLICIT_CLASSES: list[str] = VOCAB["explicit_classes"]
# 명시형 라벨 선두 토큰(주장 등)도 전역 번호 시퀀스를 공유한다.
EXTRA_CANON: dict[str, str] = VOCAB.get("extra_canon", {})

# 번호를 가질 수 있는 라벨 단어 전체 (유도형 종류 + 명시형 선두 토큰, ko/en).
NUMBERED_WORDS = set(KIND_PREFIX) | set(EXTRA_CANON) | set(EXTRA_CANON.values())

def _alt(words) -> str:
    return "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))

KIND_ALT = _alt(KIND_PREFIX)
NUMBERED_ALT = _alt(NUMBERED_WORDS)
PREFIX_ALT = _alt(PREFIX_KIND)

# ── 여는 펜스 라벨 문법 (플러그인 미러) ─────────────────────────────────────

OPEN_RE = re.compile(r"^:::[ \t]+(.+?)[ \t]*$")
CLOSE_RE = re.compile(r"^:::[ \t]*$")
DERIVED_RE = re.compile(rf"^({KIND_ALT})[ \t]+(\d+)")
EXPLICIT_RE = re.compile(rf"^({_alt(EXPLICIT_CLASSES)})[ \t]+(.+?)[ \t]*\{{#([^}}]+)\}}$")
PROOF_PLAIN = ("증명", "Proof")
PROOF_TARGET_RE = re.compile(r"^(증명|Proof)[ \t]+\((.+)\)$")

FENCE_OPEN_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
FENCE_CLOSE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})[ \t]*$")
RAW_OPEN_RE = re.compile(r"^\s*\{%\s*raw\s*%\}\s*$")
RAW_CLOSE_RE = re.compile(r"^\s*\{%\s*endraw\s*%\}\s*$")

# ── 포스트 인덱스 ──────────────────────────────────────────────────────────

FN_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+)\.md$")

@dataclass
class Post:
    path: Path
    lang: str               # ko / en
    category_dir: str       # Scheme_Theory 등 (Misc는 하위 dir명)
    base: str               # 파일명의 Title_Case 부 (날짜 접두사 제외)
    title: str
    permalink: str
    weight: int | None
    published: bool
    categories: list[str]   # frontmatter 표기 ("Math / Set Theory")

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(ROOT))

def _frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    try:
        fm = yaml.safe_load(text[3:end])
        return fm if isinstance(fm, dict) else {}
    except yaml.YAMLError:
        return {}

def iter_posts() -> list[Post]:
    posts = []
    for p in sorted(POSTS.rglob("*.md")):
        m = FN_RE.match(p.name)
        if not m:
            continue
        parts = p.relative_to(POSTS).parts
        lang = "ko"
        if "en" in parts:
            lang = "en"
        cat = parts[1] if len(parts) >= 3 else (parts[0] if len(parts) >= 2 else "")
        fm = _frontmatter(p.read_text(encoding="utf-8"))
        cats = fm.get("categories") or []
        if isinstance(cats, str):
            cats = [cats]
        posts.append(Post(
            path=p, lang=lang, category_dir=cat, base=m.group(1),
            title=str(fm.get("title") or ""), permalink=str(fm.get("permalink") or ""),
            weight=fm.get("weight"), published=fm.get("published", True) is not False,
            categories=[str(c) for c in cats],
        ))
    return posts

_SUBJECTS = None

def subject_display(post: Post, lang: str = "ko") -> str:
    """카테고리 표시명 정본: _data/categories.yml subjects.<key>.ko (en은 key에서 유도)."""
    global _SUBJECTS
    if _SUBJECTS is None:
        data = yaml.safe_load((ROOT / "_data" / "categories.yml").read_text(encoding="utf-8"))
        _SUBJECTS = data.get("subjects", {})
    for key in post.categories:
        if key in _SUBJECTS:
            if lang == "ko":
                return str(_SUBJECTS[key].get("ko", key))
            return key.split("/", 1)[-1].strip()
    return post.category_dir.replace("_", " ")

# ── 질의 정규화 매칭 ────────────────────────────────────────────────────────

def normalize(s: str) -> str:
    return re.sub(r"[ _\-]", "", s).lower()

def fuzzy_posts(query: str, posts: list[Post], cat: str | None = None,
                lang: str = "ko") -> list[Post]:
    nq = normalize(query)
    ncat = normalize(cat) if cat else None
    scored = []
    for p in posts:
        if lang and p.lang != lang:
            continue
        if ncat and ncat not in normalize(p.category_dir) and ncat not in normalize(subject_display(p)):
            continue
        slug = p.permalink.rstrip("/").rsplit("/", 1)[-1]
        keys = [normalize(p.base), normalize(slug), normalize(p.title)]
        if any(nq == k for k in keys):
            scored.append((0, p))
        elif any(k.startswith(nq) for k in keys):
            scored.append((1, p))
        elif any(nq in k for k in keys):
            scored.append((2, p))
    scored.sort(key=lambda t: (t[0], t[1].category_dir, t[1].weight or 0))
    return [p for _, p in scored]

def by_permalink(path: str, posts: list[Post]) -> Post | None:
    want = path.rstrip("/")
    for p in posts:
        if p.permalink.rstrip("/") == want:
            return p
    return None

def en_counterpart(post: Post, posts: list[Post]) -> Post | None:
    """ko 글의 en 짝 — 날짜 접두사가 다를 수 있으므로 base(Title부)로 매칭한다."""
    for p in posts:
        if p.lang == "en" and p.category_dir == post.category_dir and p.base == post.base:
            return p
    return None

# ── 인용 문자열 파서 ───────────────────────────────────────────────────────

# 하우스 인용: [\[카테고리\] §제목, ⁋명제 6](/ko/math/cat/slug#prop6)
CITATION_INPUT_RE = re.compile(
    r"^\[(?P<text>(?:\\.|[^\\\]\n])*)\]\((?P<target>[^()\s]+)\)$"
)

@dataclass
class ParsedQuery:
    path: str                    # /ko/... (앵커 제외)
    anchor: str | None
    category_display: str | None  # \[...\] 부
    section_title: str | None     # § 뒤 (⁋ 앞)
    kind: str | None              # ⁋ 뒤 종류 단어
    number: int | None

def parse_citation_query(s: str) -> ParsedQuery | None:
    """붙여넣은 인용 링크 또는 경로를 해소용 질의로 분해. 아니면 None."""
    s = s.strip()
    text = None
    if s.startswith("["):
        m = CITATION_INPUT_RE.match(s)
        if not m:
            return None
        text, target = m.group("text"), m.group("target")
    elif s.startswith("/"):
        target = s
    else:
        return None
    path, _, anchor = target.partition("#")
    q = ParsedQuery(path=path, anchor=anchor or None, category_display=None,
                    section_title=None, kind=None, number=None)
    if text is not None:
        tm = re.match(r"^(?:\\\[(?P<cat>.+?)\\\][ \t]+)?§(?P<title>.+?)(?:,[ \t]*⁋(?P<label>.+))?$", text)
        if tm:
            q.category_display = tm.group("cat")
            q.section_title = tm.group("title")
            label = tm.group("label")
            if label:
                lm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)$", label.strip())
                if lm:
                    q.kind, q.number = lm.group(1), int(lm.group(2))
        else:
            lm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)$", text.strip())
            if lm:  # 글 내부형 [명제 4](#prop4)
                q.kind, q.number = lm.group(1), int(lm.group(2))
    return q

# ── 라벨 파서 (fence/raw-aware 라인 스캐너) ────────────────────────────────

@dataclass
class Box:
    kind: str            # 라벨 선두 단어 (정의/Proposition/주장 …)
    number: int | None
    anchor: str | None   # 유도형이면 접두+번호, 명시형이면 {#id} verbatim
    explicit: bool
    label: str           # 여는 줄의 라벨 전체
    line_start: int      # 1-indexed, 여는 ::: 줄
    line_end: int        # 닫는 ::: 줄
    proofs: list["Proof"] = field(default_factory=list)

@dataclass
class Proof:
    standalone: bool
    target_text: str | None   # 단독형 괄호 안 verbatim ("명제 3")
    line_start: int
    line_end: int

@dataclass
class ParsedDoc:
    boxes: list[Box]
    proofs: list[Proof]
    unrecognized: list[tuple[int, str]]   # (line, label)

def parse_labels(text: str) -> ParsedDoc:
    boxes: list[Box] = []
    proofs: list[Proof] = []
    unrecognized: list[tuple[int, str]] = []
    open_item = None   # ("box", Box) | ("proof", Proof)
    in_fence = fence_char = None
    fence_len = 0
    in_raw = False

    for i, line in enumerate(text.split("\n"), start=1):
        if in_raw:
            if RAW_CLOSE_RE.match(line):
                in_raw = False
            continue
        if in_fence:
            m = FENCE_CLOSE_RE.match(line)
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len:
                in_fence = None
            continue
        if RAW_OPEN_RE.match(line):
            in_raw = True
            continue
        m = FENCE_OPEN_RE.match(line)
        if m:
            in_fence, fence_char, fence_len = True, m.group(1)[0], len(m.group(1))
            continue

        if open_item:
            if CLOSE_RE.match(line):
                open_item[1].line_end = i
                open_item = None
            continue

        m = OPEN_RE.match(line)
        if not m:
            continue
        label = m.group(1)

        em = EXPLICIT_RE.match(label)
        if em:
            disp = em.group(2)
            num = None
            nm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)", disp)
            kind = nm.group(1) if nm else disp.split()[0]
            if nm:
                num = int(nm.group(2))
            box = Box(kind=kind, number=num, anchor=em.group(3), explicit=True,
                      label=disp, line_start=i, line_end=i)
            boxes.append(box)
            open_item = ("box", box)
            continue
        if label in PROOF_PLAIN:
            pr = Proof(standalone=False, target_text=None, line_start=i, line_end=i)
            proofs.append(pr)
            open_item = ("proof", pr)
            continue
        pm = PROOF_TARGET_RE.match(label)
        if pm:
            pr = Proof(standalone=True, target_text=pm.group(2), line_start=i, line_end=i)
            proofs.append(pr)
            open_item = ("proof", pr)
            continue
        dm = DERIVED_RE.match(label)
        if dm:
            kind, num = dm.group(1), int(dm.group(2))
            box = Box(kind=kind, number=num, anchor=f"{KIND_PREFIX[kind]}{num}",
                      explicit=False, label=label, line_start=i, line_end=i)
            boxes.append(box)
            open_item = ("box", box)
            continue
        unrecognized.append((i, label))

    # 증명 귀속: 부착형 → 직전 박스, 단독형 → 괄호 안 종류+번호로 해소.
    for pr in proofs:
        if pr.standalone and pr.target_text:
            nm = re.match(rf"^({NUMBERED_ALT})[ \t]+(\d+)$", pr.target_text.strip())
            if nm:
                for b in boxes:
                    if b.kind == nm.group(1) and b.number == int(nm.group(2)):
                        b.proofs.append(pr)
                        break
        elif not pr.standalone:
            prev = [b for b in boxes if b.line_end < pr.line_start]
            if prev:
                prev[-1].proofs.append(pr)
    return ParsedDoc(boxes=boxes, proofs=proofs, unrecognized=unrecognized)

def find_box(doc: ParsedDoc, anchor: str | None = None, kind: str | None = None,
             number: int | None = None) -> Box | None:
    for b in doc.boxes:
        if anchor and b.anchor == anchor:
            return b
        if kind and number is not None and b.number == number:
            # 종류 단어는 ko/en 어느 쪽으로 물어도 같은 박스를 찾도록 접두로 비교.
            bp = KIND_PREFIX.get(b.kind)
            qp = KIND_PREFIX.get(kind)
            if (bp and qp and bp == qp) or b.kind == kind:
                return b
    return None

# ── 보호 구간 (code fence·raw·수식) ────────────────────────────────────────

def protected_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    # 라인 기반: code fence / raw
    offset = 0
    in_fence = fence_char = None
    fence_len = 0
    in_raw = False
    region_start = None
    for line in text.split("\n"):
        end = offset + len(line)
        if in_raw:
            if RAW_CLOSE_RE.match(line):
                spans.append((region_start, end))
                in_raw = False
        elif in_fence:
            m = FENCE_CLOSE_RE.match(line)
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len:
                spans.append((region_start, end))
                in_fence = None
        elif RAW_OPEN_RE.match(line):
            in_raw, region_start = True, offset
        else:
            m = FENCE_OPEN_RE.match(line)
            if m:
                in_fence, fence_char, fence_len = True, m.group(1)[0], len(m.group(1))
                region_start = offset
        offset = end + 1
    if in_fence or in_raw:
        spans.append((region_start, len(text)))

    # 문자 기반: $...$ / $$...$$ (fence·raw 밖에서만)
    def covered(pos: int) -> bool:
        return any(s <= pos < e for s, e in spans)

    i, n = 0, len(text)
    math_start = None
    display = False
    while i < n:
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "$" and not covered(i):
            dd = i + 1 < n and text[i + 1] == "$"
            if math_start is None:
                math_start, display = i, dd
                i += 2 if dd else 1
                continue
            if display:
                if dd:
                    spans.append((math_start, i + 2))
                    math_start = None
                    i += 2
                    continue
            else:
                spans.append((math_start, i + 1))
                math_start = None
                i += 1
                continue
        i += 1
    if math_start is not None:
        spans.append((math_start, n))
    spans.sort()
    return spans

def in_spans(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(s <= pos < e for s, e in spans)

# ── 인용 단위 regex ────────────────────────────────────────────────────────

# [<text>](<path>#<anchor>) — text에는 \[ \] 이스케이프 허용, 한 줄 한정.
CITATION_UNIT_RE = re.compile(
    r"\[(?P<text>(?:\\.|[^\\\]\n])*)\]\((?P<path>[^()\s#]*)#(?P<anchor>[A-Za-z][\w\-]*?)(?P<anum>\d*)\)"
)
# text 안의 종류+번호 (⁋ 유무 무관). 숫자 경계는 (?!\d).
TEXT_LABEL_RE = re.compile(rf"({NUMBERED_ALT})[ \t]+(\d+)(?!\d)")
