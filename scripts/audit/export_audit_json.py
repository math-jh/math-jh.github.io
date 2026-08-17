#!/usr/bin/env python3
"""2026-08 감사의 ad-hoc 노트를 규약 형식(audit.json)으로 변환한다.

AUDIT-PROTOCOL.md §3 의 참조 구현이기도 하다. 다음 감사는 처음부터 그 형식으로 내면
이 스크립트가 필요 없다.

들어오는 것 (notes/audit-2026-08/):
    findings/<key>.md    frontmatter(path·lane·verdict) + `## BUG-1 (L31, L40) — …` 절
    by-category/*.md     사람이 정리한 항목 표 (요약·수정안·처리 상태)
    applied/<key>.tsv    1 차 반영 기록
    applied2/<key>.json  2 차 반영 기록

나오는 것:
    notes/audit-2026-08/audit.json

핵심 변환은 **인용문 만들기**다. ad-hoc 노트에는 인용문이 없고 줄번호만 있으므로,
base 판본의 그 줄을 실제로 읽어 인용문으로 삼는다. 그리고 규약대로 **블록 하나당 항목
하나**가 되도록, 같은 문단에 떨어지는 줄들은 한 항목으로 합치고 다른 문단이면 쪼갠다.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts/dashboard"))

import compare as C  # noqa: E402  (경로 세팅 뒤에 와야 한다)

DEFAULT_BASE = "4a061156^"     # 감사 반영 직전 커밋
_LINE_NO = re.compile(r"L(\d+)")
_ARROW = re.compile(r"(.{2,60}?)\s*(?:→|->)\s*(.{2,60}?)(?:$|[.,·])")


def git_show(ref: str, path: str) -> list[str]:
    p = subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{path}"],
                       capture_output=True, text=True)
    return p.stdout.splitlines() if p.returncode == 0 else []


def paragraphs(lines: list[str]) -> list[tuple[int, int]]:
    """빈 줄로 끊은 문단 목록 [(시작줄, 끝줄)] — 1-based, 끝줄 포함."""
    out, start = [], None
    for i, ln in enumerate(lines, 1):
        if ln.strip():
            start = start or i
        elif start:
            out.append((start, i - 1))
            start = None
    if start:
        out.append((start, len(lines)))
    return out


def block_of(line_no: int, paras: list[tuple[int, int]]) -> int | None:
    for idx, (a, b) in enumerate(paras):
        if a <= line_no <= b:
            return idx
    return None


# 마크다운 표기는 인용문에서 걷어낸다 — 렌더된 본문에는 안 남는 것들이라, 그대로 두면
# 그 항목은 어느 블록에도 안 붙는다 (실측: 미매칭의 71%가 `:::` 여는 줄이었다).
_MARKER = re.compile(r"^(?:>\s*|[-*+]\s+|\d+[.)]\s+|#{1,6}\s+|\[\^[^\]]+\]:\s*)+")


def quote_for(lines: list[str], line_no: int) -> str:
    """그 줄의 **내용**. 블록 마커 줄이면 다음 내용 줄로 내려간다."""
    for i in range(line_no, min(line_no + 4, len(lines)) + 1):
        if not (1 <= i <= len(lines)):
            break
        raw = lines[i - 1].strip()
        if not raw or raw.startswith(":::") or raw.startswith("{%"):
            continue          # 여는 줄·Liquid 태그는 본문이 아니다
        text = _MARKER.sub("", raw).strip()
        if text:
            return text
    return ""


def convert(base_ref: str) -> dict:
    audit = C.audit_index()
    findings = C._cached("findings", 0.0, C._parse_findings)  # noqa: SLF001
    posts = []
    stats = {"posts": 0, "items": 0, "quoted": 0, "split": 0, "no_lines": 0}

    for key, rec in sorted(audit.items()):
        path = rec.get("path") or findings.get(key, {}).get("path", "")
        if not path:
            continue
        base_lines_file = git_show(base_ref, path)
        paras = paragraphs(base_lines_file)
        heads = findings.get(key, {}).get("heads", {})

        items = []
        for it in rec.get("items", []):
            # 줄번호는 findings 절 머리(감사 시점 = base 기준)를 쓴다. by-category 의
            # 줄번호는 "현재 파일 기준"으로 옮겨져 있어 base 와 어긋난다.
            raw = heads.get(it["id"], {}).get("lines", "")
            nums = [int(n) for n in _LINE_NO.findall(raw)]
            # was/now 는 옛 요약의 `A → B` 꼴에서만 건진다. 산문에서 억지로 뽑으면
            # 엉뚱한 조각이 들어와 "미반영 의심" 판정을 오염시키므로, **base 파일에
            # 실제로 있는 짧은 조각**일 때만 채택한다 (검증기 경고 1400건 → 정리).
            was = now = ""
            m = _ARROW.search(it.get("applied") or it.get("fix") or "")
            if m:
                a, b = m.group(1).strip(), m.group(2).strip()
                flat = "".join(base_lines_file)
                if len(a) <= 40 and a and a.replace(" ", "") in flat.replace(" ", ""):
                    was, now = a, b

            # 옛 노트에는 요약이 by-category 표에만 있고 findings 절 머리에만 있는
            # 항목도 있다. 규약은 summary 를 필수로 두므로 있는 것 중 첫 줄을 쓴다.
            summary = (it.get("summary") or it.get("fix") or it.get("applied")
                       or it.get("resolution") or "").strip()
            base_item = {
                "id": it["id"],
                "kind": it["id"].split("-")[0],
                "summary": summary,
                "fix": it.get("fix", ""),
                "detail": findings.get(key, {}).get("sections", {}).get(it["id"], ""),
                "status": "applied" if it.get("done") else "open",
                "resolution": it.get("resolution", "") or it.get("applied", ""),
            }
            if was and now:
                base_item["was"], base_item["now"] = was, now

            if not nums:
                stats["no_lines"] += 1
                items.append({**base_item, "quote": "", "base_lines": []})
                continue

            # 규약: 블록 하나당 항목 하나. 같은 문단이면 합치고, 다른 문단이면 쪼갠다.
            by_block: dict[int | None, list[int]] = {}
            for n in nums:
                by_block.setdefault(block_of(n, paras), []).append(n)
            for j, (blk, ns) in enumerate(sorted(by_block.items(),
                                                 key=lambda kv: min(kv[1]))):
                q = quote_for(base_lines_file, ns[0]) if base_lines_file else ""
                if q:
                    stats["quoted"] += 1
                one = {**base_item, "quote": q, "base_lines": sorted(ns)}
                if len(by_block) > 1:
                    one["id"] = f"{it['id']}.{j + 1}"
                    one["group"] = it["id"]
                    stats["split"] += 1
                items.append(one)

        stats["items"] += len(items)
        stats["posts"] += 1
        posts.append({
            "path": path,
            "verdict": rec.get("verdict", ""),
            "note": rec.get("mechanical", ""),
            "items": items,
        })

    sha = subprocess.run(["git", "-C", str(ROOT), "rev-parse", f"{base_ref}^{{commit}}"],
                         capture_output=True, text=True).stdout.strip()
    return {
        "schema": "blog-audit/1",
        "slug": "2026-08",
        "title": "2026-08 전수 수학 감사",
        "base_ref": sha,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "posts": posts,
    }, stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--base", default=DEFAULT_BASE, help=f"수정 전 판본 (기본 {DEFAULT_BASE})")
    ap.add_argument("--out", default=str(ROOT / "notes/audit-2026-08/audit.json"))
    args = ap.parse_args()

    data, stats = convert(args.base)
    Path(args.out).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{args.out}\n  글 {stats['posts']}편 · 항목 {stats['items']}개 "
          f"(인용문 있음 {stats['quoted']} · 블록별로 쪼갠 것 {stats['split']} · "
          f"줄번호 없음 {stats['no_lines']})")


if __name__ == "__main__":
    main()
