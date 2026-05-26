#!/usr/bin/env python3
"""
check_links.py — Broken-link and frontmatter audit for math-jh.github.io.

This script walks every post under ``_posts/`` of a Jekyll site using the
Minimal Mistakes theme and reports:

* Frontmatter problems
    - missing ``permalink``
    - permalink not following ``/{lang}/{category_path}/{slug}`` convention
    - missing ``header.overlay_image``
    - ``overlay_image`` path inconsistent with the category directory
    - ``overlay_image`` file not present on disk
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

SITE_ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = SITE_ROOT / "_posts"
PAGES_DIR = SITE_ROOT / "_pages"
ASSETS_DIR = SITE_ROOT / "assets"

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
    overlay_image: Optional[str] = None
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


def collect_post_permalinks() -> Dict[str, Path]:
    """Map every post permalink (normalised, no trailing slash) to its path."""
    mapping: Dict[str, Path] = {}
    for md in POSTS_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm, _ = parse_frontmatter(text)
        pl = fm.get("permalink")
        if isinstance(pl, str):
            mapping[pl.rstrip("/")] = md
    return mapping


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


def check_internal_link(
    target: str,
    post_permalinks: Dict[str, Path],
    page_permalinks: Dict[str, Path],
) -> bool:
    """Return True iff ``target`` resolves to a known post, page or file."""
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return True  # Pure ``#anchor`` link to self — accept.
    norm = target.rstrip("/")
    if norm in post_permalinks or norm in page_permalinks:
        return True
    # File-on-disk fallback (CSS, images, assets/...).
    if target.startswith("/"):
        candidate = SITE_ROOT / target.lstrip("/")
        if candidate.exists():
            return True
    return False


# ---------------------------------------------------------------------------
# Audit logic
# ---------------------------------------------------------------------------


def _expected_permalink_prefix(category_path: str, lang: str) -> List[str]:
    """Return acceptable permalink prefixes for a given category/lang.

    The site convention is ``/{lang}/{category_path_lower}``, but a few
    older posts (mostly under ``Misc/``) live directly under their category
    directory without a ``ko``/``en`` subfolder while still using a
    language-prefixed permalink.  We therefore return BOTH a strict
    ``/{lang}/...`` form and, when ``lang`` is empty, the ``/ko/...`` and
    ``/en/...`` variants so the post is accepted as long as it uses some
    language prefix consistently.
    """
    parts = [p.lower() for p in category_path.split("/") if p]
    base = "/".join(parts)
    if lang:
        return ["/" + lang + "/" + base]
    return ["/" + base, "/ko/" + base, "/en/" + base]


def _expected_image_prefix(category_path: str) -> str:
    """Expected directory prefix for overlay_image.

    For deeply nested categories like ``Misc/Peripherals/Tools`` the actual
    convention drops the trailing leaf, since images live in
    ``Misc/Peripherals/``.  We accept any prefix-match against the
    category path to stay tolerant.
    """
    return "/assets/images/" + category_path


def audit_frontmatter(audit: PostAudit, fm: Dict[str, Any]) -> None:
    expected_prefixes = _expected_permalink_prefix(
        audit.category.replace("\\", "/"), audit.lang
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

    header = fm.get("header")
    overlay = None
    if isinstance(header, dict):
        overlay = header.get("overlay_image")
    if not isinstance(overlay, str) or not overlay:
        audit.issues.append(Issue("overlay_missing", "header.overlay_image not set"))
        return

    audit.overlay_image = overlay
    expected_img_prefix = _expected_image_prefix(audit.category)
    # Tolerant: allow either the full category path or any parent of it.
    cat_parents = []
    parts = audit.category.split("/")
    for i in range(len(parts), 0, -1):
        cat_parents.append("/assets/images/" + "/".join(parts[:i]))
    if not any(overlay.startswith(p + "/") for p in cat_parents):
        audit.issues.append(
            Issue(
                "overlay_category_mismatch",
                f"{overlay!r} not under {expected_img_prefix!r}",
            )
        )

    if not check_image_exists(overlay):
        audit.issues.append(
            Issue("overlay_missing_file", f"file not on disk: {overlay}")
        )


def _external_head_ok(url: str, timeout: float = 5.0) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # nosec - opt-in
            return 200 <= resp.status < 400
    except Exception:
        return False


def audit_body(
    audit: PostAudit,
    body: str,
    post_permalinks: Dict[str, Path],
    page_permalinks: Dict[str, Path],
    check_external: bool = False,
) -> None:
    external_count = 0
    # Iterate line-by-line so we can also detect placeholder / FIXME markers
    # with helpful line numbers.
    for lineno, line in enumerate(body.splitlines(), start=1):
        if PLACEHOLDER_IMG_RE.search(line):
            audit.issues.append(
                Issue("placeholder_img", f"line {lineno}: literal 'img' placeholder")
            )
        if FIXME_RE.search(line):
            audit.issues.append(
                Issue("fixme_marker", f"line {lineno}: {line.strip()[:120]}")
            )

        # Images first; record matched spans so we don't also flag them as links.
        masked = line
        for m in IMG_RE.finditer(line):
            target = m.group("target")
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
            if not check_internal_link(target, post_permalinks, page_permalinks):
                audit.issues.append(
                    Issue("internal_link_broken", f"line {lineno}: {target}")
                )

    audit.external_count = external_count


# ---------------------------------------------------------------------------
# Top-level orchestration
# ---------------------------------------------------------------------------


def iter_posts(category_filter: Optional[str]) -> Iterable[Path]:
    if not POSTS_DIR.exists():
        return []
    for md in sorted(POSTS_DIR.rglob("*.md")):
        if category_filter:
            rel = md.relative_to(POSTS_DIR)
            if category_filter not in rel.parts:
                continue
        yield md


def audit_post(
    path: Path,
    post_permalinks: Dict[str, Path],
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
    audit_frontmatter(audit, fm)
    audit_body(audit, body, post_permalinks, page_permalinks, check_external)
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
        for issue in a.issues:
            actionables[issue.kind].append(f"{rel} — {issue.detail}")

    headline_kinds = [
        ("overlay_missing", "Posts missing `overlay_image`"),
        ("overlay_missing_file", "Overlay images referencing a nonexistent file"),
        ("overlay_category_mismatch", "Overlay images in the wrong category folder"),
        ("permalink_missing", "Posts without a `permalink`"),
        ("permalink_convention", "Permalinks that break the convention"),
        ("image_missing", "Body `![…](…)` images that are missing on disk"),
        ("internal_link_broken", "Internal links pointing nowhere"),
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
            lines.append(f"**`{rel}`**")
            if post.permalink:
                lines.append(f"- permalink: `{post.permalink}`")
            if post.overlay_image:
                lines.append(f"- overlay_image: `{post.overlay_image}`")
            for issue in post.issues:
                lines.append(f"- [{issue.kind}] {issue.detail}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


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

    if not POSTS_DIR.exists():
        print(f"error: _posts directory not found at {POSTS_DIR}", file=sys.stderr)
        return 2

    post_permalinks = collect_post_permalinks()
    page_permalinks = collect_page_permalinks()

    audits: List[PostAudit] = []
    for md in iter_posts(args.category):
        audits.append(
            audit_post(md, post_permalinks, page_permalinks, args.check_external)
        )

    report = render_report(audits)
    if args.report is None:
        sys.stdout.write(report)
    else:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
        print(f"wrote {args.report}")

    has_issues = any(a.issues for a in audits)
    return 1 if has_issues else 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
