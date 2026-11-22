#!/usr/bin/env python3
"""편집 턴의 앞뒤를 지킨다: 집필 턴이 남긴 글을 따로 떠 두고, 편집 턴이 글을
망가뜨렸으면 그 판본으로 되돌린다.

편집 턴(editor.md)은 글의 구성을 통째로 바꿀 수 있다. 그 턴이 타임아웃으로 중간에
끊기거나 front matter 를 건드린 채 끝나면, 드라이버는 그 상태를 그대로 커밋하고
autopush 가 배포한다. 그래서 편집 턴의 결과는 이 스크립트의 검사를 통과해야 남는다.

    edit_guard.py --save DIR --before FILE   집필 턴의 산출물을 DIR 에 복사하고 경로를 출력
    edit_guard.py --check DIR                편집 뒤 검사. 어긋난 글은 DIR 의 판본으로 되돌린다
    edit_guard.py --restore DIR              검사 없이 전부 되돌린다 (편집 턴이 실패로 끝났을 때)

`--before` 는 commit_posts.py --snapshot 이 남긴 목록이다. 거기 있던 경로는 사용자가
편집 중이던 글이므로 대상에서 뺀다.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BLOG_ROOT = Path(os.environ.get("BLOGDEV_ROOT") or HERE.parents[1])
sys.path.insert(0, str(HERE.parents[1] / "scripts" / "lib"))

from cron_commit import dirty_paths  # noqa: E402

WORKSHOP_DIR = "_posts/Misc/LLM_Workshop"
# 편집은 덜어내는 일이 많지만, 절반 넘게 사라졌다면 덜어낸 것이 아니라 끊긴 것이다.
MIN_SIZE_RATIO = 0.5


def front_matter(text: str) -> str | None:
    """첫 `---` 블록. 없으면 None."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    return text[:end + 5] if end >= 0 else None


def targets(before: Path) -> list[str]:
    seen = {ln.strip() for ln in before.read_text(encoding="utf-8").splitlines()
            if ln.strip()} if before.exists() else set()
    return [p for p in dirty_paths([WORKSHOP_DIR], repo=BLOG_ROOT)
            if p not in seen and p.endswith(".md") and Path(p).name != "CLAUDE.md"
            and (BLOG_ROOT / p).is_file()]


def save(store: Path, before: Path) -> int:
    for rel in targets(before):
        dest = store / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(BLOG_ROOT / rel, dest)
        print(rel)
    return 0


def saved(store: Path) -> list[str]:
    return sorted(str(p.relative_to(store)) for p in store.rglob("*.md"))


def problem(rel: str, store: Path) -> str | None:
    """편집 뒤의 글이 남아도 되는지. 안 되면 이유."""
    live = BLOG_ROOT / rel
    if not live.is_file():
        return "글이 없어졌다"
    old = (store / rel).read_text(encoding="utf-8")
    new = live.read_text(encoding="utf-8")
    if front_matter(new) != front_matter(old):
        return "front matter 가 바뀌었다"
    if len(new.encode("utf-8")) < MIN_SIZE_RATIO * len(old.encode("utf-8")):
        return "본문이 절반 아래로 줄었다"
    if "\n## " not in new:
        return "절 제목이 하나도 없다"
    return None


def check(store: Path, force: bool) -> int:
    for rel in saved(store):
        why = "편집 턴이 끝나지 못했다" if force else problem(rel, store)
        live = BLOG_ROOT / rel
        if why is None:
            same = live.read_bytes() == (store / rel).read_bytes()
            print(f"edit: {rel} {'그대로' if same else '편집됨'}")
            continue
        live.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(store / rel, live)
        print(f"edit: {rel} 되돌림 — {why}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--save", type=Path)
    g.add_argument("--check", type=Path)
    g.add_argument("--restore", type=Path)
    ap.add_argument("--before", type=Path)
    args = ap.parse_args()
    if args.save:
        if not args.before:
            ap.error("--save 에는 --before 가 필요하다")
        return save(args.save, args.before)
    return check(args.check or args.restore, force=bool(args.restore))


if __name__ == "__main__":
    sys.exit(main())
