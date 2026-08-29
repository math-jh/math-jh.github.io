#!/usr/bin/env python3
"""section_anchor_gate — EN 번역의 섹션(§§) 링크 앵커 게이트 + 결정론 수리.

번역 프롬프트는 교차참조가 불확실하면 KO 형태를 그대로 두라고 지시하고
"a post-processing pass will normalise it"을 약속한다 — 이 모듈이 그 pass다.

검사 대상: EN 파일의 `](/en/…#anchor)` 중 라벨 앵커(def3·prop-def3·conj4류,
대상 글의 명시형 id 포함)가 아닌 것 = H2 섹션 앵커. 라벨 앵커는 md_lint가
담당하므로 여기서 재검사하지 않는다.

수리 사다리 (전부 결정론, LLM 없음):
  1. 앵커 ∈ EN 대상 글의 헤딩 슬러그 → 통과.
  2. 앵커 ∈ KO 대상 글의 헤딩 슬러그(한글 잔존) → 같은 위치의 EN 헤딩으로 수리.
  3. 이 파일의 KO 원본에서 같은 대상을 가리키는 n번째 링크의 KO 앵커로 2를 재시도
     (번역기가 영문 슬러그를 틀리게 지어낸 경우).
  4. 실패 → FAIL 보고 (자동 수정 없음).
KO/EN 헤딩 개수가 다르면 위치 매핑이 성립하지 않으므로 수리하지 않는다.
수리는 앵커와 링크 텍스트의 §§표시명을 함께 고친다.

EN 대상 글이 레포에 없으면: KO 짝이 있으면 "미번역 대상"으로 유보(DEFER)하고,
이후 그 글의 번역이 완료될 때 sweep_target()이 코퍼스를 훑어 그때 수리한다
(ledger 없는 자가 치유). KO 짝도 없으면 FAIL.

슬러그 규칙은 kramdown-parser-gfm 1.1.0 generate_gfm_header_id 를 미러한다
(raw 헤딩 텍스트 → downcase → [^\\p{Word}\\- \\t] 제거 → 공백·탭→'-' →
중복 카운터 suffix). 수식 포함 헤딩도 raw 기준이다 — 실측:
"The Abelian Group $\\Hom_\\Ab(G,H)$" → the-abelian-group-hom_abgh.

CLI:
  section_anchor_gate.py check  <en-file>... [--mdlint]
  section_anchor_gate.py repair <en-file>... [--apply]
  section_anchor_gate.py sweep  <en-file>    [--apply]   # 이 글을 가리키는 링크 해소
  section_anchor_gate.py audit  [--apply]                # 전 EN 코퍼스
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# postnav 공용 모듈 (포스트 인덱스·라벨 파서) — 이름 충돌을 피해 경로 로드.
_spec = importlib.util.spec_from_file_location(
    "postnav_common", ROOT / "scripts" / "postnav" / "common.py")
_pn = importlib.util.module_from_spec(_spec)
sys.modules["postnav_common"] = _pn   # dataclass가 모듈 등록을 요구한다
_spec.loader.exec_module(_pn)

MDLINT = ROOT / ".agents" / "hooks" / "md_lint.py"

# md_lint 와 동일한 라벨 앵커 문법 (유도형). 명시형 id는 대상 글에서 실측.
LABEL_ANCHOR_RE = re.compile(r"^(?:prop-def|def|ex|prop|thm|lem|cor|rmk|conj)\d+$")

# 링크 텍스트는 bare `]` 를 허용하지 않되, 맨 앞의 `[범주]` 접두 한 겹만 예외로
# 둔다 — 타 카테고리 인용의 하우스 형식이 `[\[Category\] §Title, ⁋Definition 1]`
# 인데, 번역 엔진이 EN 에서 백슬래시를 떨어뜨려 `[[Category] §Title, …]` 로 나온다
# (KO 원문은 전량 이스케이프 형태, EN 에만 322 건). 접두를 못 읽으면 그 링크는
# 게이트에 아예 안 보여 앵커 검증이 통째로 건너뛰어진다 — 2026-08-15 에 그 경로로
# 한글 앵커 `#극한의-보편성질` 이 EN 본문까지 나갔다.
# 중첩을 일반 허용하지 말 것: 수식 속 `[1, \infty)` 같은 여는 괄호에서 매치가
# 시작돼 진짜 링크를 삼킨다 (실측 4건 회귀).
LINK_RE = re.compile(
    r"\[(?P<text>(?:\[[^\]\n]*\])?(?:\\.|[^\\\]\n])*)\]"
    r"\((?P<path>/(?:ko|en)/[^)\s#]*)#(?P<anchor>[^)\s]+)\)"
)
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)(?:[ \t]*\{#([^}]+)\})?[ \t]*$")


def gfm_slug(text: str) -> str:
    s = text.lower()
    s = re.sub(r"[^\w\- \t]", "", s)
    return s.replace(" ", "-").replace("\t", "-")


@dataclass
class Heading:
    level: int
    text: str    # raw (IAL 제외)
    slug: str    # 중복 카운터 반영
    line: int


def extract_headings(text: str) -> list[Heading]:
    """fence 밖 ATX 헤딩 전부, 문서 순서. 슬러그 중복 카운터는 GFM 방식."""
    heads: list[Heading] = []
    counter: dict[str, int] = {}
    in_fence = fence_char = None
    fence_len = 0
    for i, line in enumerate(text.split("\n"), start=1):
        if in_fence:
            m = _pn.FENCE_CLOSE_RE.match(line)
            if m and m.group(1)[0] == fence_char and len(m.group(1)) >= fence_len:
                in_fence = None
            continue
        m = _pn.FENCE_OPEN_RE.match(line)
        if m:
            in_fence, fence_char, fence_len = True, m.group(1)[0], len(m.group(1))
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        if m.group(3):
            slug = m.group(3)
        else:
            base = gfm_slug(m.group(2))
            n = counter.get(base, -1) + 1
            counter[base] = n
            slug = base if n == 0 else f"{base}-{n}"
        heads.append(Heading(len(m.group(1)), m.group(2), slug, i))
    return heads


# ── 포스트 인덱스 (모듈 캐시) ───────────────────────────────────────────────

_POSTS = None
_BY_PERMALINK = None

def _posts():
    global _POSTS, _BY_PERMALINK
    if _POSTS is None:
        _POSTS = _pn.iter_posts()
        _BY_PERMALINK = {p.permalink.rstrip("/"): p for p in _POSTS if p.permalink}
    return _POSTS

def _by_permalink(path: str):
    _posts()
    return _BY_PERMALINK.get(path.rstrip("/"))

def _counterpart(post, lang: str):
    for p in _posts():
        if p.lang == lang and p.category_dir == post.category_dir and p.base == post.base:
            return p
    return None

def _post_of(path: Path):
    rp = path.resolve()
    for p in _posts():
        if p.path == rp:
            return p
    return None


@dataclass
class GateResult:
    repairs: list[str] = field(default_factory=list)
    fails: list[str] = field(default_factory=list)
    defers: list[str] = field(default_factory=list)
    mdlint_lines: list[str] = field(default_factory=list)
    changed: bool = False

    @property
    def log_lines(self) -> list[str]:
        return ([f"수리: {r}" for r in self.repairs]
                + [f"유보(EN 미번역 대상): {d}" for d in self.defers]
                + [f"FAIL: {f}" for f in self.fails]
                + [f"md_lint: {m}" for m in self.mdlint_lines])


def _target_box_ids(post) -> set:
    doc = _pn.parse_labels(post.path.read_text(encoding="utf-8"))
    return {b.anchor for b in doc.boxes if b.anchor}


def _ko_link_anchors(F_ko_text: str, ko_permalink: str) -> list[str]:
    """KO 원본에서 ko_permalink 를 가리키는 섹션 링크의 앵커들 (문서 순)."""
    out = []
    for m in LINK_RE.finditer(F_ko_text):
        if m.group("path").rstrip("/") == ko_permalink and \
                not LABEL_ANCHOR_RE.match(m.group("anchor")):
            out.append(m.group("anchor"))
    return out


def gate_text(text: str, en_path: Path, only_target: str | None = None):
    """본문 하나를 게이트에 통과시켜 (새 본문, GateResult)를 반환.

    only_target: 이 permalink 를 가리키는 링크만 검사 (sweep 용).
    """
    res = GateResult()
    spans = _pn.protected_spans(text)
    me = _post_of(en_path)
    rel = str(en_path.relative_to(ROOT)) if en_path.is_relative_to(ROOT) else str(en_path)

    # /ko/ 링크가 EN 본문에 남은 것은 별개의 번역 버그 — 보고만.
    for m in re.finditer(r"\]\(/ko/[^)\s]*\)", text):
        if not _pn.in_spans(m.start(), spans):
            res.fails.append(f"{rel}: EN 본문에 /ko/ 링크 잔존 — {m.group(0)[:80]}")
            break

    edits = []          # (start, end, replacement)
    boxid_cache: dict[str, set] = {}
    ko_anchor_cursor: dict[str, int] = {}   # 대상별 몇 번째 섹션 링크인지

    for m in LINK_RE.finditer(text):
        if _pn.in_spans(m.start(), spans):
            continue
        path, anchor = m.group("path").rstrip("/"), m.group("anchor")
        if not path.startswith("/en/"):
            continue
        if only_target and path != only_target:
            continue
        target = _by_permalink(path)

        if target is None:
            ko_twin = _by_permalink(path.replace("/en/", "/ko/", 1))
            if ko_twin is None:
                res.fails.append(f"{rel}: 대상 글 없음 (ko 짝도 없음): {path}#{anchor}")
            elif not LABEL_ANCHOR_RE.match(anchor):
                # 라벨 앵커는 번역되는 순간 그대로 유효해지므로 유보 대상이 아니다.
                res.defers.append(f"{rel}: {path}#{anchor}")
            continue

        # 각주 앵커: 대상에 [^name]: 정의가 있으면 유효.
        fn = re.match(r"^fn:(.+)$", anchor)
        if fn:
            if not re.search(rf"^[ \t]{{0,3}}\[\^{re.escape(fn.group(1))}\]:",
                             target.path.read_text(encoding="utf-8"), re.MULTILINE):
                res.fails.append(f"{rel}: {path}#{anchor} — 대상에 해당 각주 없음")
            continue

        # 라벨 앵커는 md_lint 관할 — 유도형 문법이거나 대상의 명시형 id면 통과.
        if LABEL_ANCHOR_RE.match(anchor):
            continue
        if path not in boxid_cache:
            boxid_cache[path] = _target_box_ids(target)
        if anchor in boxid_cache[path]:
            continue

        # 여기부터는 섹션 링크 — KO 원본과의 n번째 대응(사다리 3)을 위해
        # 유효·무효를 가리지 않고 대상별로 순번을 센다.
        nth = ko_anchor_cursor.get(path, 0)
        ko_anchor_cursor[path] = nth + 1

        en_heads = extract_headings(target.path.read_text(encoding="utf-8"))
        en_slugs = [h.slug for h in en_heads]
        if anchor in en_slugs:
            continue

        ko_target = _counterpart(target, "ko")
        idx = None
        if ko_target is not None:
            ko_heads = extract_headings(ko_target.path.read_text(encoding="utf-8"))
            if len(ko_heads) != len(en_heads):
                res.fails.append(
                    f"{rel}: {path}#{anchor} — ko/en 헤딩 개수 불일치"
                    f"(ko {len(ko_heads)}/en {len(en_heads)}), 위치 매핑 불가")
                continue
            ko_slugs = [h.slug for h in ko_heads]
            if anchor in ko_slugs:                       # 사다리 2
                idx = ko_slugs.index(anchor)
            else:                                        # 사다리 3
                me_ko = _counterpart(me, "ko") if me else None
                if me_ko is not None:
                    cands = _ko_link_anchors(
                        me_ko.path.read_text(encoding="utf-8"),
                        path.replace("/en/", "/ko/", 1))
                    if nth < len(cands) and cands[nth] in ko_slugs:
                        idx = ko_slugs.index(cands[nth])

        if idx is None:
            res.fails.append(f"{rel}: {path}#{anchor} — 대상 헤딩 해소 실패 (수동 확인)")
            continue

        new_slug = en_slugs[idx]
        new_text = m.group("text")
        sm = re.search(r"§§(?P<sec>[^\]]*)$", new_text)
        if sm:
            new_text = new_text[:sm.start()] + "§§" + en_heads[idx].text
        replaced = f"[{new_text}]({m.group('path')}#{new_slug})"
        edits.append((m.start(), m.end(), replaced))
        res.repairs.append(f"{rel}: #{anchor} → #{new_slug}"
                           + (f" (§§{en_heads[idx].text})" if sm else ""))

    if edits:
        out = text
        for s, e, rep in sorted(edits, reverse=True):
            out = out[:s] + rep + out[e:]
        res.changed = True
        return out, res
    return text, res


def _mdlint_filtered(en_path: Path) -> list[str]:
    """md_lint CLI 실행 후 'EN 미번역 대상' 오탐(참조 대상 글 없음)을 필터."""
    try:
        r = subprocess.run([sys.executable, str(MDLINT), str(en_path)],
                           capture_output=True, text=True, timeout=120)
    except Exception as e:
        return [f"md_lint 실행 실패: {e!r}"]
    # md_lint 출력은 `<경로>:` 헤더 한 줄 + `  - <지적>` 들이다. 헤더를 지적으로
    # 세면 목록에 파일명만 든 항목이 섞이고, 그게 그대로 텔레그램·opus 프롬프트에
    # 지적인 척 들어간다 (건수 상한·"n fixed / m left" 산수도 같이 어긋난다).
    lines = [l.strip()[2:].strip() for l in (r.stdout + r.stderr).splitlines()
             if l.strip().startswith("- ") and "자동 검사 경고" not in l]
    kept = []
    for l in lines:
        mm = re.search(r"참조 대상 글 없음: (/en/[^\s]+)", l)
        if mm and _by_permalink(mm.group(1).replace("/en/", "/ko/", 1)) is not None:
            continue                       # KO 짝 실존 → 미번역 대상, 오탐
        kept.append(l)
    return kept


def run_gate(en_path: Path, ko_path: Path | None = None, apply: bool = True,
             mdlint: bool = False) -> GateResult:
    """워커용 진입점: 검사 + (apply면) in-place 수리. 예외는 호출측이 감싼다."""
    text = en_path.read_text(encoding="utf-8")
    new, res = gate_text(text, en_path)
    if res.changed and apply:
        en_path.write_text(new, encoding="utf-8")
    if mdlint:
        res.mdlint_lines = _mdlint_filtered(en_path)
    return res


def sweep_target(en_path: Path, apply: bool = True) -> GateResult:
    """en_path 글의 번역 완료 직후: 이 글을 가리키는 미해소 섹션 앵커를 코퍼스에서
    수리한다 (유보분의 자가 치유). 수리된 형제 파일은 커밋하지 않고 워킹트리에
    남긴다 — 다음 autopush 가 가져간다."""
    agg = GateResult()
    me = _post_of(en_path)
    if me is None or not me.permalink:
        return agg
    target_pl = me.permalink.rstrip("/")
    needle = f"]({target_pl}#"
    for p in _posts():
        if p.lang != "en" or p.path == me.path:
            continue
        text = p.path.read_text(encoding="utf-8")
        if needle not in text:
            continue
        new, res = gate_text(text, p.path, only_target=target_pl)
        if res.changed and apply:
            p.path.write_text(new, encoding="utf-8")
        agg.repairs += res.repairs
        agg.fails += res.fails
        agg.changed = agg.changed or res.changed
    return agg


# ── CLI ────────────────────────────────────────────────────────────────────

def _report(res: GateResult, applied: bool) -> None:
    for line in res.log_lines:
        print(line)
    n = len(res.repairs)
    print(f"SUMMARY 수리 {n} / 유보 {len(res.defers)} / FAIL {len(res.fails)}"
          + ("" if applied or not n else "  (dry-run — --apply 로 쓰기)"))


def main() -> int:
    ap = argparse.ArgumentParser(prog="section_anchor_gate")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("check", "repair"):
        s = sub.add_parser(name)
        s.add_argument("files", nargs="+")
        s.add_argument("--apply", action="store_true")
        s.add_argument("--mdlint", action="store_true")
    s = sub.add_parser("sweep")
    s.add_argument("files", nargs=1)
    s.add_argument("--apply", action="store_true")
    s = sub.add_parser("audit")
    s.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    agg = GateResult()
    if args.cmd == "audit":
        targets = [p.path for p in _posts() if p.lang == "en"]
    else:
        targets = [Path(f).resolve() for f in args.files]

    if args.cmd == "sweep":
        agg = sweep_target(targets[0], apply=args.apply)
    else:
        apply = args.cmd != "check" and args.apply
        for f in targets:
            text = f.read_text(encoding="utf-8")
            new, res = gate_text(text, f)
            if res.changed and apply:
                f.write_text(new, encoding="utf-8")
            if getattr(args, "mdlint", False):
                res.mdlint_lines = _mdlint_filtered(f)
            agg.repairs += res.repairs
            agg.fails += res.fails
            agg.defers += res.defers
            agg.mdlint_lines += res.mdlint_lines
    _report(agg, getattr(args, "apply", False))
    return 1 if agg.fails else 0


if __name__ == "__main__":
    sys.exit(main())
