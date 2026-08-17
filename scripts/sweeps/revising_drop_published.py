#!/usr/bin/env python3
"""개정 중인 글에서 `published: false` 를 걷어낸다 (2026-08-17 일회성 이관).

옛 규약은 `published: false` + `revising: true` 였다. 두 키가 함께 붙어 있으니
`published: false` 를 "미발행 초안"으로 읽는 쪽(대시보드 개요, 용어 스윕, 번역 워커)이
개정 중인 발행 글을 초안으로 셌다. 새 규약은 `revising: true` 하나이고, 그것이
CI(scripts/ci/freeze_revising_posts.py)에서 직전 발행 판본 복원을 부른다.

이 스크립트는 **frontmatter 의 `published: false` 한 줄만** 지운다. 본문은 바이트 단위로
같아야 하며, 다르면 그 파일을 건드리지 않고 중단한다.

    revising_drop_published.py            # dry-run (기본)
    revising_drop_published.py --apply
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FM_RE = re.compile(r"\A(---\r?\n)(.*?)(\r?\n---\r?\n)", re.S)
REVISING_RE = re.compile(r"^revising:\s*true\s*$", re.M)
UNPUB_RE = re.compile(r"^published:\s*false\s*$", re.M)


def strip_published(text: str) -> str | None:
    """frontmatter 에서 published:false 줄만 뺀 전문. 대상이 아니면 None."""
    m = FM_RE.match(text)
    if not m:
        return None
    head, fm, tail = m.group(1), m.group(2), m.group(3)
    if not REVISING_RE.search(fm) or not UNPUB_RE.search(fm):
        return None
    lines = fm.split("\n")
    kept = [ln for ln in lines if not UNPUB_RE.match(ln.rstrip("\r"))]
    if len(kept) != len(lines) - 1:      # 정확히 한 줄만 사라져야 한다
        return None
    return head + "\n".join(kept) + tail + text[m.end():]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files", "_posts"],
                             capture_output=True, text=True).stdout.splitlines()
    hit, skipped, bad = [], [], []
    for rel in tracked:
        if not rel.endswith(".md"):
            continue
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        out = strip_published(text)
        if out is None:
            if REVISING_RE.search(text[:2000]) and UNPUB_RE.search(text[:2000]):
                bad.append(rel)      # 대상인데 형태가 예상과 다르다
            continue
        # 게이트: 본문은 한 바이트도 달라지면 안 된다.
        body_old = text[FM_RE.match(text).end():]
        body_new = out[FM_RE.match(out).end():]
        if body_old != body_new or len(text) - len(out) not in range(15, 22):
            bad.append(rel)
            continue
        hit.append(rel)
        if args.apply:
            path.write_text(out, encoding="utf-8")

    mode = "적용" if args.apply else "dry-run"
    print(f"revising_drop_published ({mode}): 대상 {len(hit)}편")
    for rel in bad:
        print(f"  중단 대상 제외: {rel}", file=sys.stderr)
    if skipped:
        print(f"  건너뜀 {len(skipped)}편", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
