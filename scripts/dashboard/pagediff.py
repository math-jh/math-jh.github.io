#!/usr/bin/env python3
"""구워진 두 판본의 본문을 블록 단위로 정렬해 diff HTML 두 벌을 만든다.

정렬은 4 단계다. 오정렬이 글 전체로 번지지 않게 각 단계가 다음 단계의 작업 범위를
가둔다:

  L1  블록 해시가 정확히 같은 것끼리 붙인다 (difflib, 순서 보존).
      감사 수정은 글당 몇 군데뿐이라 대부분이 여기서 끝난다.
  L2  L1 이 못 붙인 **틈 안에서만** 유사도 매칭. 순서를 보존하는 1:1 DP 에
      하한(FLOOR)을 걸어, 우연히 비슷해 보이는 삭제·추가의 오결합을 막는다.
  L3  짝지어진 블록 안에서 단어 단위 diff.
  L4  변경 토큰만 <del>/<ins> 로 감싼다. 마크는 절대 태그 경계를 넘지 않는다.

라벨 id(`def1`·`ex2`…)는 **가점으로만** 쓴다. 블록을 하나 끼워넣으면 뒤 형제가
전부 재번호되므로, id 동일성으로 매칭하면 삽입 하나에 뒷부분 전체가 어긋난다.

표시 규칙이 오정렬의 안전망이다:

  ratio == 1.0   표시 없음
  ratio >= FLOOR 블록 안 단어 표시
  ratio <  FLOOR 짝짓지 않음 → 왼쪽 통째 삭제 + 오른쪽 통째 추가

낮은 유사도에서 잘못 짝지어도 화면은 "통째 교체"고, 그건 올바르게 안 짝지어졌을
때의 화면과 같다. 즉 그 오류는 리뷰어가 보는 것을 바꾸지 않는다.

수식(`\\(..\\)`·`\\[..\\]`·`$..$`)·svg·img 는 원자 토큰이라 내부는 건드리지 않는다
(CLAUDE.md 의 mask-first 를 HTML 에 적용한 것). 마크가 수식 안으로 들어가면 KaTeX
가 렌더에 실패해 diff 가 아니라 깨진 화면이 된다.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher

from bs4 import BeautifulSoup, NavigableString, Tag

FLOOR = 0.6          # 이 아래면 짝짓지 않는다 (통째 교체로 보여준다)
BAND = 12            # 틈 안 DP 의 대각선 밴드 — 순서가 크게 뒤바뀐 매칭을 애초에 배제
ATOMIC_KINDS = ("figure", "svg", "img", "table")  # 내부를 단어로 쪼개지 않는 블록

# 본문에서 걷어낼 것 — 목차·로컬그래프·스크립트는 글 내용이 아니다.
DROP_SELECTORS = (
    "aside.sidebar__right",
    "nav.toc",
    ".localgraph-side",
    "script",
    "style",
    "#comments",
    ".page__comments",
)

_WS = re.compile(r"\s+")
_SHY = re.compile("[­​]")


# ────────────────────────────────────────────────────────────── 본문 추출


def extract_article(html: str) -> Tag | None:
    soup = BeautifulSoup(html, "html.parser")
    node = soup.select_one('.page__content[itemprop="text"]') or soup.select_one(".page__content")
    if node is None:
        return None
    for sel in DROP_SELECTORS:
        for junk in node.select(sel):
            junk.decompose()
    return node


# ────────────────────────────────────────────────────────────── 블록


@dataclass
class Block:
    kind: str            # 태그+첫 클래스 (`div.definition`, `h2`, `p`, `mathblock`…)
    html: str            # 원본 마크업 (bare 텍스트 노드는 감싼 형태)
    text: str            # 정규화 텍스트 (해시·유사도용)
    words: list[str] = field(default_factory=list)
    key: str = ""

    def __post_init__(self) -> None:
        if not self.words:
            self.words = self.text.split()
        if not self.key:
            self.key = hashlib.blake2b(
                f"{self.kind}\x00{self.text}".encode(), digest_size=16
            ).hexdigest()

    @property
    def atomic(self) -> bool:
        return self.kind.split(".")[0] in ATOMIC_KINDS


def _norm(s: str) -> str:
    return _WS.sub(" ", _SHY.sub("", s)).strip()


def _kind_of(tag: Tag) -> str:
    classes = tag.get("class") or []
    return f"{tag.name}.{classes[0]}" if classes else tag.name


def split_blocks(article: Tag) -> list[Block]:
    """본문을 최상위 블록 열로 자른다.

    kramdown 은 display 수식을 태그로 감싸지 않고 맨 텍스트로 흘린다. 그런 조각도
    블록으로 잡아야 수식만 바뀐 변경을 짚을 수 있다.
    """
    blocks: list[Block] = []
    pending: list[str] = []

    def flush_text() -> None:
        raw = "".join(pending)
        pending.clear()
        if not _norm(raw):
            return
        text = _norm(raw)
        kind = "mathblock" if text.startswith(("\\[", "$$")) else "textblock"
        blocks.append(Block(kind=kind, html=f'<div class="d-bare">{raw}</div>', text=text))

    for child in article.children:
        if isinstance(child, NavigableString):
            pending.append(str(child))
            continue
        if not isinstance(child, Tag):
            continue
        flush_text()
        kind = _kind_of(child)
        markup = str(child)
        if kind.split(".")[0] in ATOMIC_KINDS:
            # 도식·표는 텍스트가 거의 없어 마크업 자체로 같고 다름을 판정한다.
            text = _norm(child.get_text(" ")) + " §" + hashlib.blake2b(
                markup.encode(), digest_size=8
            ).hexdigest()
        else:
            text = _norm(child.get_text(" "))
        blocks.append(Block(kind=kind, html=markup, text=text))
    flush_text()
    return blocks


# ────────────────────────────────────────────────────────────── 정렬


def _ratio(a: Block, b: Block) -> float:
    if a.atomic or b.atomic:
        return 1.0 if a.key == b.key else 0.0
    sm = SequenceMatcher(a=a.words, b=b.words, autojunk=False)
    if sm.real_quick_ratio() < FLOOR or sm.quick_ratio() < FLOOR:
        return 0.0
    r = sm.ratio()
    if a.kind != b.kind:
        r *= 0.85          # 종류가 다르면 감점 (문단↔정의블록 등)
    return r


def _align_gap(old: list[Block], new: list[Block], oo: int, no: int) -> list[tuple]:
    """틈 안에서만 도는 단조 1:1 DP. 반환은 (op, oi, ni, ratio) 열."""
    n, m = len(old), len(new)
    if not n:
        return [("ins", None, no + j, 0.0) for j in range(m)]
    if not m:
        return [("del", oo + i, None, 0.0) for i in range(n)]

    sim = [[0.0] * m for _ in range(n)]
    for i in range(n):
        lo, hi = max(0, i - BAND), min(m, i + BAND + 1)
        for j in range(lo, hi):
            r = _ratio(old[i], new[j])
            sim[i][j] = r if r >= FLOOR else 0.0

    best = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            take = best[i - 1][j - 1] + sim[i - 1][j - 1] if sim[i - 1][j - 1] else -1.0
            best[i][j] = max(best[i - 1][j], best[i][j - 1], take)

    ops: list[tuple] = []
    i, j = n, m
    while i > 0 or j > 0:
        s = sim[i - 1][j - 1] if i > 0 and j > 0 else 0.0
        if i > 0 and j > 0 and s and abs(best[i][j] - (best[i - 1][j - 1] + s)) < 1e-9:
            ops.append(("edit", oo + i - 1, no + j - 1, s))
            i, j = i - 1, j - 1
        elif i > 0 and (j == 0 or best[i - 1][j] >= best[i][j - 1]):
            ops.append(("del", oo + i - 1, None, 0.0))
            i -= 1
        else:
            ops.append(("ins", None, no + j - 1, 0.0))
            j -= 1
    ops.reverse()
    return ops


def align(old: list[Block], new: list[Block]) -> list[tuple]:
    sm = SequenceMatcher(a=[b.key for b in old], b=[b.key for b in new], autojunk=False)
    ops: list[tuple] = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            ops += [("same", i1 + k, j1 + k, 1.0) for k in range(i2 - i1)]
        else:
            ops += _align_gap(old[i1:i2], new[j1:j2], i1, j1)
    return ops


# ────────────────────────────────────────── 블록 안 단어 diff (토큰화 = mask-first)

TAG, MATH, WORD, SPACE = "tag", "math", "word", "space"
_MATH_OPEN = (("\\(", "\\)"), ("\\[", "\\]"), ("$$", "$$"), ("$", "$"))


def tokenize(s: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "<":
            j = s.find(">", i)
            j = n - 1 if j < 0 else j
            out.append((TAG, s[i : j + 1]))
            i = j + 1
            continue
        hit = next((p for p in _MATH_OPEN if s.startswith(p[0], i)), None)
        if hit:
            left, right = hit
            j = s.find(right, i + len(left))
            # 줄을 넘는 짝은 수식이 아니다 — 워크숍 글의 셸 코드 블록에 `$` 가 흩어져
            # 있어 그대로 두면 문단 하나가 통째로 원자 토큰이 되어 표시가 뭉개진다.
            if 0 <= j <= i + 4000 and "\n" not in s[i:j]:
                out.append((MATH, s[i : j + len(right)]))
                i = j + len(right)
                continue
        if c.isspace():
            j = i
            while j < n and s[j].isspace():
                j += 1
            out.append((SPACE, s[i:j]))
            i = j
            continue
        j = i
        while j < n and not s[j].isspace() and s[j] != "<":
            if any(s.startswith(p[0], j) for p in _MATH_OPEN) and j > i:
                break
            j += 1
        j = max(j, i + 1)
        out.append((WORD, s[i:j]))
        i = j
    return out


def _wrap(toks: list[tuple[str, str]], el: str, hid: int) -> str:
    """마크가 태그 경계를 넘지 않게 조각내 감싼다."""
    out: list[str] = []
    run: list[str] = []

    def flush() -> None:
        if not run:
            return
        chunk = "".join(run)
        run.clear()
        if chunk.strip():
            out.append(f'<{el} class="d-tok" data-h="{hid}">{chunk}</{el}>')
        else:
            out.append(chunk)

    for kind, raw in toks:
        if kind == TAG:
            flush()
            out.append(raw)
        else:
            run.append(raw)
    flush()
    return "".join(out)


def inline_diff(old_html: str, new_html: str, hid: int) -> tuple[str, str, int, dict]:
    a, b = tokenize(old_html), tokenize(new_html)
    sm = SequenceMatcher(a=[t[1] for t in a], b=[t[1] for t in b], autojunk=False)
    left, right, n = [], [], 0
    gone, came = [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            left.append("".join(t[1] for t in a[i1:i2]))
            right.append("".join(t[1] for t in b[j1:j2]))
            continue
        changed = False
        if i2 > i1:
            piece = _wrap(a[i1:i2], "del", hid)
            left.append(piece)
            changed |= "d-tok" in piece
            gone += [t[1] for t in a[i1:i2] if t[0] in (WORD, MATH)]
        if j2 > j1:
            piece = _wrap(b[j1:j2], "ins", hid)
            right.append(piece)
            changed |= "d-tok" in piece
            came += [t[1] for t in b[j1:j2] if t[0] in (WORD, MATH)]
        if changed:
            n += 1
    # 바뀐 토큰만 따로 남긴다 — 감사 지적과 이어붙이는 근거가 이것이다 (블록 전문이
    # 아니라 실제로 손댄 자리여야 한다).
    return "".join(left), "".join(right), n, {"del": " ".join(gone), "ins": " ".join(came)}


# ────────────────────────────────────────────────────────────── pane 조립

_OPEN_TAG = re.compile(r"^(\s*)<([A-Za-z][\w:-]*)((?:\"[^\"]*\"|'[^']*'|[^>])*)>")


def mark_block(html: str, attrs: dict[str, str], classes: tuple[str, ...] = ()) -> str:
    """블록의 **자기 여는 태그**에 속성·클래스를 얹는다.

    바깥에 div 를 덧씌우지 않는 이유는 본문 CSS 가 `.page__content` 의 자식 구조를
    보기 때문이다 (`:first-child`·인접 선택자). 감싸는 순간 조판이 미묘하게 달라져
    diff 가 아닌 것이 diff 처럼 보인다.
    """
    m = _OPEN_TAG.match(html)
    if not m:
        return html
    lead, name, rest = m.group(1), m.group(2), m.group(3)
    if classes:
        cm = re.search(r'\sclass="([^"]*)"', rest)
        if cm:
            rest = rest[: cm.start()] + f' class="{cm.group(1)} {" ".join(classes)}"' + rest[cm.end():]
        else:
            rest += f' class="{" ".join(classes)}"'
    for k, v in attrs.items():
        rest += f' {k}="{v}"'
    return f"{lead}<{name}{rest}>" + html[m.end():]


_ID_ATTR = re.compile(r'(\sid=")([^"]+)(")')
_FRAG = re.compile(r'((?:xlink:)?href="#)([^"]+)(")')
_URLREF = re.compile(r'(url\(#)([^)]+)(\))')


def prefix_ids(html: str, prefix: str) -> str:
    """pane 안 모든 id 와 그 내부 참조에 접두사를 붙인다.

    두 판본을 한 문서에 넣으면 도식 svg 의 글리프 id 가 충돌한다. `<use href="#g0-1">`
    은 문서에서 **처음 만난** id 로 해석되므로, 오른쪽 도식이 왼쪽 글리프로 그려져도
    에러 없이 그럴듯하게 나온다 (같은 계열 사고: 367af0e5 xref 미리보기).
    글 밖으로 나가는 링크(`/ko/…#def1`)는 조각 참조가 아니므로 건드리지 않는다.
    """
    html = _ID_ATTR.sub(lambda m: f"{m.group(1)}{prefix}{m.group(2)}{m.group(3)}", html)
    html = _FRAG.sub(lambda m: f"{m.group(1)}{prefix}{m.group(2)}{m.group(3)}", html)
    html = _URLREF.sub(lambda m: f"{m.group(1)}{prefix}{m.group(2)}{m.group(3)}", html)
    return html


def diff_articles(old_html: str, new_html: str) -> dict:
    old_art, new_art = extract_article(old_html), extract_article(new_html)
    if old_art is None or new_art is None:
        raise ValueError("본문(.page__content)을 찾지 못했다")

    old_blocks, new_blocks = split_blocks(old_art), split_blocks(new_art)
    ops = align(old_blocks, new_blocks)

    left, right, hunks = [], [], []
    # 블록 목록 — 감사 항목의 인용문을 어느 블록에 붙일지 정하는 데 쓴다. 변경이 없는
    # 블록도 들어간다: "지적됐는데 안 고쳐진 것"이 바로 그런 블록에 앉는다.
    index: list[dict] = []
    hid = 0
    for op_no, (kind, oi, ni, ratio) in enumerate(ops):
        # data-op 은 스크롤 동기화의 닻이다 — 양쪽에 다 있는 op 만 같은 번호를 갖는다.
        anchor = {"data-op": str(op_no)}
        if kind == "same":
            left.append(mark_block(old_blocks[oi].html, anchor, ("d-blk",)))
            right.append(mark_block(new_blocks[ni].html, anchor, ("d-blk",)))
            index.append({"op": op_no, "hunk": None, "kind": "same",
                          "old": old_blocks[oi].text, "new": new_blocks[ni].text})
            continue
        hid += 1
        tag = {**anchor, "data-h": str(hid)}
        index.append({
            "op": op_no, "hunk": hid, "kind": kind,
            "old": old_blocks[oi].text if oi is not None else "",
            "new": new_blocks[ni].text if ni is not None else "",
        })
        if kind == "edit":
            a, b = old_blocks[oi], new_blocks[ni]
            atomic = a.atomic or b.atomic
            if atomic:
                # 도식·표는 안을 쪼개지 않는다 — 블록 자체가 변경 표시다.
                lh, rh, n = a.html, b.html, 1
                touched = {"del": a.text, "ins": b.text}
            else:
                lh, rh, n, touched = inline_diff(a.html, b.html, hid)
            klass = ("d-blk", "d-edit") + (("d-atomic",) if atomic else ())
            left.append(mark_block(lh, tag, klass))
            right.append(mark_block(rh, tag, klass))
            hunks.append(
                {
                    "id": hid,
                    "kind": "atomic" if (a.atomic or b.atomic) else "edit",
                    "ratio": round(ratio, 3),
                    "marks": n,
                    "old": a.text[:400],
                    "new": b.text[:400],
                    "touched": touched,
                }
            )
        elif kind == "del":
            b = old_blocks[oi]
            left.append(mark_block(b.html, tag, ("d-blk", "d-gone")))
            hunks.append({"id": hid, "kind": "del", "ratio": 0.0, "marks": 1,
                          "old": b.text[:400], "new": "",
                          "touched": {"del": b.text, "ins": ""}})
        else:
            b = new_blocks[ni]
            right.append(mark_block(b.html, tag, ("d-blk", "d-new")))
            hunks.append({"id": hid, "kind": "add", "ratio": 0.0, "marks": 1,
                          "old": "", "new": b.text[:400],
                          "touched": {"del": "", "ins": b.text}})

    return {
        "left": prefix_ids("\n".join(left), "L-"),
        "right": prefix_ids("\n".join(right), "R-"),
        "hunks": hunks,
        "blocks": index,
        "stats": {
            "blocks_old": len(old_blocks),
            "blocks_new": len(new_blocks),
            "changed": len(hunks),
            "edited": sum(1 for h in hunks if h["kind"] in ("edit", "atomic")),
            "added": sum(1 for h in hunks if h["kind"] == "add"),
            "deleted": sum(1 for h in hunks if h["kind"] == "del"),
        },
    }
