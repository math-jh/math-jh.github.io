#!/usr/bin/env python3
"""
check_links.py — Broken-link and frontmatter audit for math-jh.github.io.

This script walks every post under ``_posts/`` of a Jekyll site using the
Minimal Mistakes theme and reports:

* Frontmatter problems
    - missing ``permalink``
    - permalink not following ``/{lang}/{category_path}/{slug}`` convention
* Body problems
    - ``![alt](path)`` images whose target file does not exist
    - ``[text](path)`` internal links whose target post / page does not exist
    - literal "img" placeholders inside image markdown
    - lines containing ``FIXME`` / ``TODO`` markers
    - count of external (http/https) links (optionally HEAD-checked)

Only Python 3 stdlib is required.  PyYAML is used when available for nicer
frontmatter parsing, otherwise a small built-in parser is used; the parser
only needs to cope with the simple subset of YAML actually used in posts
(scalars, two-space indented sub-maps, ``[a, b]`` flow lists).

Usage examples
--------------
Run a full audit (default = stdout, no external checks)::

    python3 ~/math-jh.github.io/scripts/audit/check_links.py

Save a markdown report and limit to one category::

    python3 ~/math-jh.github.io/scripts/audit/check_links.py \
        --report ~/math-jh.github.io/scripts/audit/audit-report.md \
        --category Linear_Algebra

Include slow external HEAD checks::

    python3 ~/math-jh.github.io/scripts/audit/check_links.py --check-external

Exit code is ``0`` when nothing is broken and ``1`` otherwise, so the
script can be wired into CI.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
import urllib.request
from collections import defaultdict, OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:  # Optional dependency: use real YAML parser when available.
    import yaml as _yaml  # type: ignore
    _HAS_YAML = True
except Exception:  # pragma: no cover - PyYAML missing is a supported state.
    _HAS_YAML = False


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SITE_ROOT = Path(__file__).resolve().parent.parent.parent
POSTS_DIR = SITE_ROOT / "_posts"
PAGES_DIR = SITE_ROOT / "_pages"
ASSETS_DIR = SITE_ROOT / "assets"
DATA_DIR = SITE_ROOT / "_data"
SUBJECT_PAGE_PLUGIN = SITE_ROOT / "_plugins" / "hide_empty_subject_pages.rb"

# 수식 스팬 정규식의 단일 출처는 .agents/hooks/md_lint.py — translate_worker·mech_sweep
# 와 같은 관례로 import 한다.
sys.path.insert(0, str(SITE_ROOT / ".agents" / "hooks"))
from md_lint import _MATH_SPAN_RE  # noqa: E402

# Filename "2024-08-18-Weighted_Categories.md" -> ("2024-08-18", "Weighted_Categories")
POST_NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")

# Markdown link / image regexes.  Non-greedy ``.*?`` so they cope with
# multiple links on the same line.  The image regex is matched FIRST and
# any matched span is removed from the line before scanning for plain links.
IMG_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
LINK_RE = re.compile(r"\[(?P<text>[^\]]+)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)")

# Detect literal "img" placeholders such as ![img](img) or src=img.
PLACEHOLDER_IMG_RE = re.compile(r"!\[\s*img\s*\]\(\s*img\s*\)|src=[\"']?img[\"']?", re.I)
FIXME_RE = re.compile(r"\b(FIXME|TODO|XXX)\b")
# 작성 중 남겨진 참조 placeholder(##ref)와 타깃이 빈 링크 — LINK_RE의 [^)\s]+는
# 빈 괄호를 매칭하지 못하므로 별도로 잡는다.
PLACEHOLDER_REF_RE = re.compile(r"##ref")
EMPTY_LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*\)")


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class Issue:
    """A single problem found in a post."""

    kind: str
    detail: str

    def __str__(self) -> str:  # pragma: no cover - cosmetic
        return f"[{self.kind}] {self.detail}"


@dataclass
class PostAudit:
    path: Path
    category: str
    lang: str
    slug: str
    permalink: Optional[str] = None
    draft: bool = False                  # published: false
    issues: List[Issue] = field(default_factory=list)
    external_count: int = 0


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _parse_minimal_yaml(text: str) -> Dict[str, Any]:
    """Tiny YAML-ish parser for the subset of frontmatter actually in use.

    Supports:
      key: value
      key:
          subkey: value
      key: [a, b, c]
    Anything fancier is returned verbatim as a string — good enough for
    auditing, since we only consult a handful of well-known keys.
    """
    root: Dict[str, Any] = {}
    # ``stack`` holds (indent, dict) frames; top-of-stack is the active map.
    stack: List[Tuple[int, Dict[str, Any]]] = [(-1, root)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        stripped = raw_line.lstrip(" ")
        indent = len(raw_line) - len(stripped)

        # Pop frames that are at >= current indent: we are leaving them.
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            stack = [(-1, root)]

        if ":" not in stripped:
            continue
        key, _, rest = stripped.partition(":")
        key = key.strip()
        rest = rest.strip()
        parent = stack[-1][1]
        if rest == "":
            new_map: Dict[str, Any] = {}
            parent[key] = new_map
            stack.append((indent, new_map))
        else:
            parent[key] = _strip_quotes(rest)

    return root


def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """Split a post into ``(frontmatter_dict, body_text)``.

    Tolerates an empty leading line inside the ``---`` block and falls back
    to the built-in parser when PyYAML chokes.
    """
    if not text.startswith("---"):
        return {}, text

    # Find the closing ``---`` line.
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].lstrip("\n")
    body = text[end + 4:].lstrip("\n")

    parsed: Dict[str, Any] = {}
    if _HAS_YAML:
        try:
            loaded = _yaml.safe_load(fm_text)
            if isinstance(loaded, dict):
                parsed = loaded
            else:
                parsed = {}
        except Exception:
            parsed = _parse_minimal_yaml(fm_text)
    else:
        parsed = _parse_minimal_yaml(fm_text)
    return parsed, body


# ---------------------------------------------------------------------------
# Helpers for filesystem and permalink resolution
# ---------------------------------------------------------------------------


def _is_draft(fm: Dict[str, Any]) -> bool:
    return str(fm.get("published", "true")).strip().lower() == "false"


def collect_post_permalinks() -> Tuple[Dict[str, Path], set]:
    """Map every post permalink (normalised, no trailing slash) to its path.

    두 번째 값은 그중 ``published: false`` 초안의 permalink 다. 초안은 프로덕션에
    빌드되지 않으므로, 발행 글이 초안을 가리키면 그 링크는 배포본에서 404 다.
    """
    mapping: Dict[str, Path] = {}
    drafts: set = set()
    for md in POSTS_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _ = parse_frontmatter(text)
        pl = fm.get("permalink")
        if isinstance(pl, str):
            mapping[pl.rstrip("/")] = md
            if _is_draft(fm):
                drafts.add(pl.rstrip("/"))
    return mapping, drafts


def collect_page_permalinks() -> Dict[str, Path]:
    mapping: Dict[str, Path] = {}
    if not PAGES_DIR.exists():
        return mapping
    for md in PAGES_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _ = parse_frontmatter(text)
        pl = fm.get("permalink")
        if isinstance(pl, str):
            mapping[pl.rstrip("/")] = md
    return mapping


def _load_yaml(path: Path) -> Dict[str, Any]:
    """Read a ``_data`` YAML file with the same parser policy as frontmatter."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    if _HAS_YAML:
        try:
            loaded = _yaml.safe_load(text)
            return loaded if isinstance(loaded, dict) else {}
        except Exception:
            pass
    return _parse_minimal_yaml(text)


def _subject_slug(category: str) -> str:
    """Mirror ``HideEmptySubjectPages.slug_for``.

    Take the segment after the last ``" / "``, lowercase it and turn spaces
    into underscores.  Hyphens are left alone, so "Math / Gromov-Witten
    Theory" becomes "gromov-witten_theory".
    """
    return category.split(" / ")[-1].strip().lower().replace(" ", "_")


def _category_names(fm: Dict[str, Any]) -> List[str]:
    """Frontmatter ``categories`` as a list, whichever parser produced it."""
    value = fm.get("categories")
    if isinstance(value, list):
        return [str(item).strip() for item in value]
    if isinstance(value, str):
        inner = value.strip()
        if inner.startswith("[") and inner.endswith("]"):
            inner = inner[1:-1]
        return [_strip_quotes(part) for part in inner.split(",") if part.strip()]
    return []


def collect_subject_home_permalinks() -> Dict[str, Path]:
    """Map every generated Math subject home to the plugin that emits it.

    Math subject homes have no file on disk — ``hide_empty_subject_pages.rb``
    generates them at build time from ``_data/categories.yml`` — so scanning
    ``_posts``/``_pages`` permalinks alone reports every link to
    ``/ko/set_theory`` and its siblings as broken.  The plugin skips a home
    whose category has no post in that language, and ``published: false``
    drafts are already out of ``site.posts``, so we apply both conditions to
    match what production actually serves.  (Misc subject homes stay physical
    files under ``_pages`` and are picked up by ``collect_page_permalinks``.)
    """
    subjects = _load_yaml(DATA_DIR / "categories.yml").get("subjects")
    if not isinstance(subjects, dict):
        return {}

    langs_with_posts: Dict[str, set] = defaultdict(set)
    for md in POSTS_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _ = parse_frontmatter(text)
        if str(fm.get("published", "true")).strip().lower() == "false":
            continue
        permalink = fm.get("permalink")
        if not isinstance(permalink, str):
            continue
        lang = next((l for l in ("ko", "en") if permalink.startswith(f"/{l}/")), None)
        if lang is None:
            continue
        for category in _category_names(fm):
            langs_with_posts[category].add(lang)

    mapping: Dict[str, Path] = {}
    for raw_name in subjects:
        category = _strip_quotes(str(raw_name))
        slug = _subject_slug(category)
        for lang in langs_with_posts.get(category, ()):
            mapping[f"/{lang}/{slug}"] = SUBJECT_PAGE_PLUGIN
    return mapping


def derive_category_info(post_path: Path) -> Tuple[str, str, str]:
    """Return ``(category_dir, lang, slug)`` for a post path.

    ``category_dir`` is the directory immediately under ``_posts`` (one of
    Math, Misc, …); for nested categories the deeper directory is what we
    actually compare against the permalink, so we walk to the parent of the
    ``ko``/``en`` leaf when present.
    """
    rel = post_path.relative_to(POSTS_DIR)
    parts = rel.parts  # e.g. ("Math", "Linear_Algebra", "ko", "2021-...md")
    lang = ""
    if len(parts) >= 2 and parts[-2] in {"ko", "en"}:
        lang = parts[-2]
        category_parts = parts[:-2]
    else:
        category_parts = parts[:-1]
    category_path = "/".join(category_parts)
    m = POST_NAME_RE.match(parts[-1])
    slug_raw = m.group(2) if m else parts[-1][:-3]
    return category_path, lang, slug_raw


def check_image_exists(image_ref: str) -> bool:
    """Return True iff ``image_ref`` resolves to a file on disk.

    Site-absolute paths starting with ``/`` are resolved relative to
    ``SITE_ROOT``; relative paths are looked up under ``assets/``.
    """
    if not image_ref:
        return False
    image_ref = image_ref.split("#", 1)[0].split("?", 1)[0]
    if image_ref.startswith("/"):
        candidate = SITE_ROOT / image_ref.lstrip("/")
    else:
        candidate = ASSETS_DIR / image_ref
    return candidate.is_file()


def internal_link_problem(
    target: str,
    post_permalinks: Dict[str, Path],
    draft_permalinks: set,
    page_permalinks: Dict[str, Path],
    source_is_draft: bool,
) -> Optional[str]:
    """``target`` 이 배포본에서 열리지 않는 이유 한 줄. 열리면 None.

    앵커(``#thm8``)가 대상 글에 실제로 있는지는 보지 않는다. 초안끼리의 링크는
    둘이 함께 발행될 것이므로 문제 삼지 않는다.
    """
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None  # Pure ``#anchor`` link to self — accept.
    norm = target.rstrip("/")
    if norm in page_permalinks:
        return None
    if norm in post_permalinks:
        if norm in draft_permalinks and not source_is_draft:
            return "대상이 초안(published: false)이라 배포본에서 404"
        return None
    # File-on-disk fallback (CSS, images, assets/...).
    if target.startswith("/") and (SITE_ROOT / target.lstrip("/")).exists():
        return None
    if norm.startswith("/en/"):
        ko = "/ko/" + norm[len("/en/"):]
        if ko in draft_permalinks:
            return None if source_is_draft else "EN 판 없음 (KO 원본이 초안)"
        if ko in post_permalinks:
            return "EN 판 없음 (KO 원본은 발행됨, 번역 전)"
    return "이 permalink 를 가진 글·페이지가 없음"


# ---------------------------------------------------------------------------
# Audit logic
# ---------------------------------------------------------------------------


def _expected_permalink_prefix(
    category_path: str, lang: str, category_names: Iterable[str] = (),
) -> List[str]:
    """Return acceptable permalink prefixes for a given category/lang.

    The site convention is ``/{lang}/{category_path_lower}``, but a few
    older posts (mostly under ``Misc/``) live directly under their category
    directory without a ``ko``/``en`` subfolder while still using a
    language-prefixed permalink.  We therefore return BOTH a strict
    ``/{lang}/...`` form and, when ``lang`` is empty, the ``/ko/...`` and
    ``/en/...`` variants so the post is accepted as long as it uses some
    language prefix consistently.

    카테고리 구간은 폴더 경로에서도, frontmatter ``categories`` 의 이름에서도
    만든다. 이름 쪽은 과목홈 슬러그(``_subject_slug``)와 같은 규칙이라 하이픈을
    보존한다 — 폴더 ``Gromov_Witten_Theory`` 의 글은 카테고리 "Math / Gromov-Witten
    Theory" 를 따라 ``/ko/math/gromov-witten_theory/…`` 를 쓴다.
    """
    variants = [[p.lower() for p in category_path.split("/") if p]]
    for name in category_names:
        variants.append([seg.strip().lower().replace(" ", "_")
                         for seg in name.split(" / ") if seg.strip()])
    bases = []
    for parts in variants:
        bases.append("/".join(parts))
        # Misc 하위 카테고리는 permalink에서 선행 "misc" 세그먼트를 생략할 수 있다
        # (예: Misc/LLM_Workshop -> /ko/llm_workshop/... — 해당 CLAUDE.md 규약).
        if len(parts) > 1 and parts[0] == "misc":
            bases.append("/".join(parts[1:]))
    bases = list(dict.fromkeys(bases))
    if lang:
        return ["/" + lang + "/" + b for b in bases]
    out: List[str] = []
    for b in bases:
        out += ["/" + b, "/ko/" + b, "/en/" + b]
    return out


def audit_frontmatter(audit: PostAudit, fm: Dict[str, Any]) -> None:
    expected_prefixes = _expected_permalink_prefix(
        audit.category.replace("\\", "/"), audit.lang, _category_names(fm)
    )

    permalink = fm.get("permalink")
    if not isinstance(permalink, str) or not permalink:
        audit.issues.append(Issue("permalink_missing", "no permalink field"))
    else:
        audit.permalink = permalink
        # Case-insensitive prefix check; convention is lowercase but a few
        # posts use mixed case (e.g. Jordan_canonical_form).
        pl_lower = permalink.lower()
        if not any(pl_lower.startswith(p.lower()) for p in expected_prefixes):
            audit.issues.append(
                Issue(
                    "permalink_convention",
                    f"{permalink!r} does not start with any of "
                    f"{expected_prefixes!r}",
                )
            )


def _external_head_ok(url: str, timeout: float = 5.0) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec - opt-in
            return 200 <= resp.status < 400
    except Exception:
        return False


def _blank(m: "re.Match") -> str:
    return re.sub(r"[^\n]", " ", m.group(0))


def _mask_body(body: str) -> str:
    """코드 펜스·인라인 코드·수식을 같은 길이의 공백으로 가린다 (줄바꿈은 그대로).

    검사 정규식은 가린 본문에 돌리고, 보고서에 싣는 발췌는 같은 위치의 원문에서
    자른다. 가리지 않으면 수식 `$[U/G](T)$`·`$(\\phi[\\x](p))(x)$` 가 링크로, 코드
    예시 `` `[표시명](/url#anchor)` `` 가 깨진 링크로 잡힌다. 순서는 md_lint 와 같다
    (코드 먼저, 그다음 수식).
    """
    lines = body.split("\n")
    in_code = False
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        fence = stripped.startswith("```") or stripped.startswith("~~~")
        if fence or in_code:
            lines[i] = " " * len(line)
            if fence:
                in_code = not in_code
    masked = re.sub(r"`[^`\n]*`", _blank, "\n".join(lines))
    return _MATH_SPAN_RE.sub(_blank, masked)


def _excerpt(raw: str, start: int, end: int) -> str:
    """raw[start:end] 를 담은 발췌. HTML 주석 안이면 주석 전체를 보인다."""
    open_at = raw.rfind("<!--", 0, start)
    if open_at >= 0 and raw.find("-->", open_at, start) < 0:
        close_at = raw.find("-->", end)
        start, end = open_at, (close_at + 3 if close_at >= 0 else len(raw))
    lo, hi = max(0, start - 40), min(len(raw), max(end, start + 120))
    return (("…" if lo else "") + raw[lo:hi].strip()
            + ("…" if hi < len(raw) else ""))


def _link_markup(raw: str, m: "re.Match") -> str:
    text = raw[m.start("text"):m.end("text")]
    if len(text) > 60:
        text = text[:60] + "…"
    return f"[{text}]({m.group('target')})"


def audit_body(
    audit: PostAudit,
    body: str,
    post_permalinks: Dict[str, Path],
    draft_permalinks: set,
    page_permalinks: Dict[str, Path],
    check_external: bool = False,
    line_offset: int = 0,
) -> None:
    """``line_offset`` 은 본문 앞 frontmatter 의 줄 수 — 보고하는 줄번호는 파일 기준이다."""
    external_count = 0
    raw_lines = body.split("\n")
    for idx, line in enumerate(_mask_body(body).split("\n")):
        raw_line = raw_lines[idx]
        lineno = line_offset + idx + 1

        if PLACEHOLDER_IMG_RE.search(line):
            audit.issues.append(
                Issue("placeholder_img", f"line {lineno}: literal 'img' placeholder")
            )
        if PLACEHOLDER_REF_RE.search(line):
            audit.issues.append(
                Issue("placeholder_ref", f"line {lineno}: '##ref' placeholder")
            )
        if EMPTY_LINK_RE.search(line):
            audit.issues.append(
                Issue("empty_link", f"line {lineno}: link with empty target")
            )
        marker = FIXME_RE.search(line)
        if marker:
            audit.issues.append(
                Issue("fixme_marker", f"line {lineno}: "
                      f"{_excerpt(raw_line, marker.start(), marker.end())}")
            )

        # Images first; record matched spans so we don't also flag them as links.
        masked = line
        for m in IMG_RE.finditer(line):
            target = m.group("target")
            if target in ("...", "…"):
                # 표기 예시(`![alt](...)`) — 실제 참조가 아님
                masked = masked.replace(m.group(0), " " * len(m.group(0)))
                continue
            if target.startswith(("http://", "https://", "data:", "mailto:")):
                external_count += 1
                if check_external and not _external_head_ok(target):
                    audit.issues.append(
                        Issue("external_image_dead", f"line {lineno}: {target}")
                    )
            else:
                if not check_image_exists(target):
                    audit.issues.append(
                        Issue("image_missing", f"line {lineno}: {target}")
                    )
            masked = masked.replace(m.group(0), " " * len(m.group(0)))

        for m in LINK_RE.finditer(masked):
            target = m.group("target")
            if target.startswith(("http://", "https://")):
                external_count += 1
                if check_external and not _external_head_ok(target):
                    audit.issues.append(
                        Issue("external_link_dead", f"line {lineno}: {target}")
                    )
                continue
            if target.startswith(("mailto:", "data:", "tel:", "javascript:")):
                continue
            if target.startswith("#"):
                continue  # Anchor on same page; out of scope.
            problem = internal_link_problem(target, post_permalinks, draft_permalinks,
                                            page_permalinks, audit.draft)
            if problem:
                audit.issues.append(
                    Issue("internal_link_broken",
                          f"line {lineno}: {_link_markup(raw_line, m)} — {problem}")
                )

    audit.external_count = external_count


# ---------------------------------------------------------------------------
# Top-level orchestration
# ---------------------------------------------------------------------------


def iter_posts(category_filter: Optional[str]) -> Iterable[Path]:
    if not POSTS_DIR.exists():
        return []
    for md in sorted(POSTS_DIR.rglob("*.md")):
        if not POST_NAME_RE.match(md.name):
            # Jekyll 도 날짜 접두사 없는 파일은 글로 보지 않는다. _posts 안의 그런
            # 파일은 작업 지침(CLAUDE.md 와 그 심링크 AGENTS.md)뿐이다.
            continue
        if category_filter:
            rel = md.relative_to(POSTS_DIR)
            if category_filter not in rel.parts:
                continue
        yield md


def audit_post(
    path: Path,
    post_permalinks: Dict[str, Path],
    draft_permalinks: set,
    page_permalinks: Dict[str, Path],
    check_external: bool,
) -> PostAudit:
    category, lang, slug = derive_category_info(path)
    audit = PostAudit(path=path, category=category, lang=lang, slug=slug)
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        audit.issues.append(Issue("read_error", f"could not read file: {exc!r}"))
        return audit
    try:
        fm, body = parse_frontmatter(text)
    except Exception as exc:
        audit.issues.append(Issue("yaml_error", f"malformed frontmatter: {exc!r}"))
        fm, body = {}, text
    audit.draft = _is_draft(fm)
    audit_frontmatter(audit, fm)
    # parse_frontmatter 의 body 는 text 의 꼬리다 — 앞부분의 줄 수가 frontmatter 몫이다.
    line_offset = text[:len(text) - len(body)].count("\n")
    audit_body(audit, body, post_permalinks, draft_permalinks, page_permalinks,
               check_external, line_offset)
    return audit


def _category_label(category: str) -> str:
    return category.replace("/", " / ").replace("_", " ")


def render_report(audits: List[PostAudit]) -> str:
    total = len(audits)
    with_issues = [a for a in audits if a.issues]
    issue_counter: Dict[str, int] = defaultdict(int)
    for a in with_issues:
        for issue in a.issues:
            issue_counter[issue.kind] += 1

    # Group by top-level category (Math/Linear_Algebra, Misc/Blog_Development).
    grouped: "OrderedDict[str, List[PostAudit]]" = OrderedDict()
    for a in audits:
        grouped.setdefault(a.category, []).append(a)

    lines: List[str] = []
    lines.append("# Broken-link audit — math-jh.github.io")
    lines.append("")
    lines.append(f"- Total posts scanned: **{total}**")
    lines.append(f"- Posts with at least one issue: **{len(with_issues)}**")
    lines.append(f"- Site root: `{SITE_ROOT}`")
    lines.append("")
    lines.append("## Issue counts")
    lines.append("")
    lines.append("| Kind | Count |")
    lines.append("| --- | ---: |")
    for kind in sorted(issue_counter, key=lambda k: (-issue_counter[k], k)):
        lines.append(f"| `{kind}` | {issue_counter[kind]} |")
    if not issue_counter:
        lines.append("| _none_ | 0 |")
    lines.append("")

    # Concrete actionable summaries — surfaces the top fixes at a glance.
    actionables: Dict[str, List[str]] = defaultdict(list)
    for a in with_issues:
        rel = a.path.relative_to(SITE_ROOT)
        tag = " (초안)" if a.draft else ""
        for issue in a.issues:
            actionables[issue.kind].append(f"{rel}{tag} — {issue.detail}")

    headline_kinds = [
        ("permalink_missing", "Posts without a `permalink`"),
        ("permalink_convention", "Permalinks that break the convention"),
        ("image_missing", "Body `![…](…)` images that are missing on disk"),
        ("internal_link_broken", "Internal links pointing nowhere"),
        ("placeholder_ref", "`##ref` reference placeholders still present"),
        ("empty_link", "Links with an empty target"),
        ("placeholder_img", "Literal `img` placeholder still present"),
        ("fixme_marker", "FIXME / TODO markers left in posts"),
    ]
    lines.append("## Actionable items")
    lines.append("")
    for kind, label in headline_kinds:
        if not actionables.get(kind):
            continue
        lines.append(f"### {label}")
        lines.append("")
        for item in actionables[kind]:
            lines.append(f"- {item}")
        lines.append("")

    lines.append("## By category")
    lines.append("")
    for category, posts in grouped.items():
        bad_posts = [p for p in posts if p.issues]
        label = _category_label(category)
        if not bad_posts:
            lines.append(f"### {label}  ({len(posts)} posts) — clean")
            lines.append("")
            continue
        lines.append(
            f"### {label}  ({len(posts)} posts, {len(bad_posts)} with issues)"
        )
        lines.append("")
        for post in bad_posts:
            rel = post.path.relative_to(SITE_ROOT)
            lines.append(f"**`{rel}`**" + (" (초안)" if post.draft else ""))
            if post.permalink:
                lines.append(f"- permalink: `{post.permalink}`")
            for issue in post.issues:
                lines.append(f"- [{issue.kind}] {issue.detail}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _log(msg: str, stream=sys.stdout) -> None:
    """진행 상황을 타임스탬프와 함께 남긴다 (--report 모드 = 크론 전용).

    대시보드(scripts/dashboard/server.py)가 이 타임스탬프로 실행 경계를 잡아
    마지막 실행분만 오류 판정에 쓴다. 시작 줄이 있어야 도중에 죽어 남은
    트레이스백도 그 실행에 붙는다. 보고서 본문을 stdout 으로 뽑는 수동
    모드에서는 부르지 않는다 — 출력이 섞인다."""
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}", file=stream, flush=True)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit Jekyll posts for frontmatter and link integrity.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Path to write the markdown report (default: stdout).",
    )
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        help="Only audit posts whose path contains this directory name "
             "(e.g. Linear_Algebra).",
    )
    parser.add_argument(
        "--check-external",
        action="store_true",
        help="Also HEAD-check http(s) links. Slow; off by default.",
    )
    args = parser.parse_args(argv)

    if args.report is not None:
        _log(f"audit 시작 — category={args.category or 'all'} "
             f"external={'on' if args.check_external else 'off'}")

    if not POSTS_DIR.exists():
        print(f"error: _posts directory not found at {POSTS_DIR}", file=sys.stderr)
        return 2

    post_permalinks, draft_permalinks = collect_post_permalinks()
    page_permalinks = collect_page_permalinks()
    page_permalinks.update(collect_subject_home_permalinks())

    audits: List[PostAudit] = []
    for md in iter_posts(args.category):
        audits.append(
            audit_post(md, post_permalinks, draft_permalinks, page_permalinks,
                       args.check_external)
        )

    report = render_report(audits)
    if args.report is None:
        sys.stdout.write(report)
    else:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
        _log(f"wrote {args.report}")

    has_issues = any(a.issues for a in audits)
    return 1 if has_issues else 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
