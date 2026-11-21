#!/usr/bin/env python3
"""Objective features of a link occurrence, and the evidence-quote match score.

None of these decide a relation.  They feed the risk score that chooses which
judgments get a second look (Step 2), so they only have to correlate with
disagreement, not cause it.  They are computed from the text by code, never by
a model.
"""
from __future__ import annotations

import difflib
import html
import re
import unicodedata
from pathlib import Path

BOX_ANCHOR_RE = re.compile(r"^(def|prop|thm|lem|cor|ex|rmk)\d+$")
BOX_KIND = {"def": "definition", "prop": "proposition", "thm": "theorem", "lem": "lemma",
            "cor": "corollary", "ex": "example", "rmk": "remark"}
FOOTNOTE_DEF_RE = re.compile(r"(?m)^\[\^([^\]\s]+)\]:")
POST_DATE_RE = re.compile(r"^(\d{4}-\d\d-\d\d)-")


def anchor_of(target: str) -> str:
    return target.split("#", 1)[1] if "#" in target else ""


def target_kind(target: str) -> str:
    anchor = anchor_of(target)
    if not anchor:
        return "post"
    m = BOX_ANCHOR_RE.match(anchor)
    if m:
        return BOX_KIND[m.group(1)]
    return "section"


def post_date(path: Path) -> str | None:
    m = POST_DATE_RE.match(path.name)
    return m.group(1) if m else None


def footnote_spans(text: str) -> list[tuple[int, int]]:
    starts = [m.start() for m in FOOTNOTE_DEF_RE.finditer(text)]
    spans = []
    for i, start in enumerate(starts):
        limit = starts[i + 1] if i + 1 < len(starts) else len(text)
        brk = re.search(r"\n\s*\n(?=\S)", text[start:limit])
        spans.append((start, start + brk.start() if brk else limit))
    return spans


def _open_parens_before(line: str, col: int) -> int:
    depth = 0
    in_math = False
    for ch in line[:col]:
        if ch == "$":
            in_math = not in_math
        elif not in_math and ch in "(（":
            depth += 1
        elif not in_math and ch in ")）" and depth:
            depth -= 1
    return depth


def link_features(link, text: str, doc, *, source_path: Path,
                  target_path: Path | None, pair_size: int, article_links: int) -> dict:
    """Features of one occurrence.  ``doc`` is ``parse_labels(text)``."""
    same_page = link.target.startswith("#")
    line_no = link.line
    lines = text.split("\n")
    line = lines[line_no - 1] if 0 < line_no <= len(lines) else ""
    line_start = text.rfind("\n", 0, link.start) + 1
    in_box = in_proof = False
    for box in doc.boxes:
        if box.line_start < line_no < box.line_end:
            in_box = True
        for proof in box.proofs:
            if proof.line_start < line_no < proof.line_end:
                in_proof = True
    for proof in doc.proofs:
        if proof.line_start < line_no < proof.line_end:
            in_proof = True
    target_line = None
    target_before = None
    if same_page:
        anchor = anchor_of(link.target)
        for box in doc.boxes:
            if box.anchor == anchor:
                target_line = box.line_start
                target_before = box.line_start < line_no
                break
    earlier = None
    if not same_page and target_path is not None:
        a, b = post_date(source_path), post_date(target_path)
        if a and b:
            earlier = b <= a
    return {
        "same_page": same_page,
        "target_kind": target_kind(link.target),
        "in_footnote": any(a <= link.start < b for a, b in footnote_spans(text)),
        "in_heading": line.lstrip().startswith("#"),
        "in_proof": in_proof,
        "in_box_statement": in_box and not in_proof,
        "in_paren": _open_parens_before(line, link.start - line_start) > 0,
        "target_line": target_line,
        "target_before": target_before,
        "target_post_earlier": earlier,
        "pair_size": pair_size,
        "article_chars": len(text),
        "article_links": article_links,
    }


_ESCAPE_RE = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|$~<>])")
_IAL_RE = re.compile(r"\{:[^}]*\}")
_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_EMPH_RE = re.compile(r"(\*\*|__|\*|`)")


def normalize_quote(text: str) -> str:
    text = unicodedata.normalize("NFC", html.unescape(text or ""))
    text = _IAL_RE.sub("", text)
    text = _LINK_RE.sub(r"\1", text)
    text = _ESCAPE_RE.sub(r"\1", text)
    text = _EMPH_RE.sub("", text)
    text = text.replace("$", "")
    return " ".join(text.split())


def quote_score(evidence: str, source_text: str) -> float:
    """1.0 when the evidence is in the source after normalising, else the best ratio.

    Escapes, markup, math delimiters, and whitespace are normalised away first, so
    a faithful quote that differs only in those scores 1.0.  The score is a risk
    feature, not a gate: nothing is rejected for a low score.
    """
    ev = normalize_quote(evidence)
    if not ev:
        return 0.0
    src = normalize_quote(source_text)
    if ev in src:
        return 1.0
    matcher = difflib.SequenceMatcher(None, src, ev, autojunk=False)
    best = 0.0
    blocks = sorted(matcher.get_matching_blocks(), key=lambda b: -b.size)[:5]
    for block in blocks:
        if not block.size:
            continue
        start = max(0, block.a - block.b - len(ev) // 4)
        window = src[start:start + len(ev) + len(ev) // 2]
        best = max(best, difflib.SequenceMatcher(None, window, ev, autojunk=False).ratio())
    return round(best, 3)
