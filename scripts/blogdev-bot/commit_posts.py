#!/usr/bin/env python3
"""Marvin 이 방금 쓴 워크숍 글을 커밋한다. push 는 autopush 몫.

왜 드라이버가 커밋하나:
  글을 워킹트리에 남겨 두면 autopush 가 가져가는데, autopush 의 분류는 경로만
  본다 — `_posts/Misc/LLM_Workshop/` 아래면 사용자가 손으로 고친 글도 Marvin
  이름으로 커밋됐다 (5ffc5cbe: 기존 글 +1/-3 이 Marvin author 로 남았다).
  봇이 자기 산출물만 자기 이름으로 커밋해 두면 그 오귀속이 사라지고, autopush
  쪽 워크숍 버킷은 사용자 변경만 담는 폴백이 된다.

`--before` 파일에는 드라이버가 모델을 띄우기 **전에** 찍어 둔 dirty 경로가 한 줄에
하나씩 들어 있다. 그때 이미 더러웠던 파일은 사용자 작업이므로 커밋에서 뺀다.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BLOG_ROOT = HERE.parents[1]
sys.path.insert(0, str(BLOG_ROOT / "scripts" / "lib"))

from cron_commit import MARVIN_AUTHOR, commit_outputs, dirty_paths  # noqa: E402

WORKSHOP_DIR = "_posts/Misc/LLM_Workshop"


def _title(rel: str) -> str:
    """글 제목 (frontmatter). 못 읽으면 파일 이름."""
    stem = Path(rel).stem
    try:
        head = (BLOG_ROOT / rel).read_text(encoding="utf-8")[:2000]
    except OSError:
        return stem
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', head, re.MULTILINE)
    return m.group(1) if m else stem


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--snapshot", type=Path,
                   help="지금 dirty 한 워크숍 경로를 이 파일에 적는다 (모델 실행 전)")
    g.add_argument("--before", type=Path,
                   help="--snapshot 이 남긴 목록. 여기 없는 변경만 커밋한다")
    args = ap.parse_args()

    if args.snapshot:
        args.snapshot.write_text("\n".join(dirty_paths([WORKSHOP_DIR])) + "\n",
                                 encoding="utf-8")
        return 0

    before = {ln.strip() for ln in args.before.read_text(encoding="utf-8").splitlines()
              if ln.strip()} if args.before.exists() else set()
    new = [p for p in dirty_paths([WORKSHOP_DIR]) if p not in before]
    if not new:
        print("commit: 새 워크숍 산출물 없음")
        return 0

    n = len(new)
    detail = "\n".join(f"- {_title(p)}" for p in new)
    # 실패해도 rc 는 0 이다 — 커밋을 못 하면(락 경합 등) 글은 워킹트리에 남고
    # autopush 가 가져간다. 드라이버를 실패로 만들 일이 아니다.
    if not commit_outputs(f"Development Bot ({n} file{'s' if n > 1 else ''})",
                          new, detail, marker=None, author=MARVIN_AUTHOR,
                          log=print):
        print(f"commit: 커밋하지 못했다 ({n}건은 워킹트리에 남는다)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
