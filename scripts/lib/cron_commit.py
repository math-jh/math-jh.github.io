#!/usr/bin/env python3
"""cron_commit — cron 워커가 자기 산출물을 직접 커밋하는 공용 헬퍼. push 는 안 한다.

왜 워커가 직접 커밋하나:
  autopush 는 워킹트리에 남은 것을 전부 긁어 haiku 분류기에 넘긴다. 봇 산출물이
  거기 섞이면 (a) 분류기가 볼 diff 가 커지고 (translate_worker 가 자기 EN 을
  직접 커밋하게 된 것도 이 이유다 — 2026-07-14 에 EN 재번역 몇 편이 분류기 예산을
  넘겨 autopush 가 멈췄다) (b) 여러 cron 의 산출물이 "Auto-mechanical: N file(s)"
  한 커밋에 묶여 어느 cron 이 뭘 했는지 히스토리에서 사라진다.

  워커가 자기 파일만 자기 이름으로 커밋해 두면 autopush 는 그걸 건드리지 않는다 —
  커밋된 것은 `git add -A` 대상이 아니므로 분류 대상에서 빠지고, autopush 에는
  push 만 남는다.

왜 여기서 push 하지 않나:
  origin 상태·CI 재시도·defer 판단을 autopush 한 곳에 모아 둔다. autopush 는
  2026-08-11 부터 "cron 커밋만 밀려 있으면 최대 7 일 push 를 미룬다" 로 동작하는데,
  워커가 직접 밀면 그 정책이 조용히 무력화된다.
"""
from __future__ import annotations

import fcntl
import os
import subprocess
import time
from pathlib import Path
from typing import Callable, Iterable, Sequence

BLOG_ROOT = Path(__file__).resolve().parents[2]
# autopush 와 같은 락 — 둘 다 같은 레포에 git 을 건다.
AUTOPUSH_LOCK = Path("/tmp/blog-autopush.lock")
LOCK_WAIT_SEC = 120
LASTMOD_SKIP = "[lastmod-skip]"

# author 는 사용자, 커밋 행위자는 Claude — autopush·translate_worker 와 같은 정체성
# 체계(2026-07-22). autopush 의 defer 판정이 **committer 이름으로** cron 산출물을
# 가리므로, 이 값을 바꾸면 defer 가 에러 없이 무력화된다 (대시보드 sec_git 의
# auto/manual 구분도 같은 규약을 쓴다).
IDENTITY = {
    "GIT_AUTHOR_NAME": "Junhyeok Kim", "GIT_AUTHOR_EMAIL": "kujuburi@icloud.com",
    "GIT_COMMITTER_NAME": "Claude", "GIT_COMMITTER_EMAIL": "noreply@anthropic.com",
}


def _git(repo: Path, *args: str) -> tuple[int, str, str]:
    p = subprocess.run(["git", *args], cwd=str(repo), capture_output=True,
                       text=True, env={**os.environ, **IDENTITY})
    return p.returncode, p.stdout, p.stderr


def dirty_paths(paths: Iterable[str], repo: Path = BLOG_ROOT) -> list[str]:
    """<paths> 중 실제로 변경된 것들 (수정·추가·삭제).

    `-z` 로 읽는다 — core.quotepath 가 비ASCII 경로를 이스케이프해서 돌려주면
    그대로 pathspec 에 넣을 수 없다.
    """
    rels = [str(p) for p in paths if p]
    if not rels:
        return []
    rc, out, _ = _git(repo, "status", "--porcelain", "-z", "--", *rels)
    if rc != 0:
        return []
    return [rec[3:] for rec in out.split("\0") if len(rec) > 3]


def commit_outputs(worker: str, paths: Sequence[str], summary: str, *,
                   marker: str | None = LASTMOD_SKIP,
                   log: Callable[[str], None] | None = None,
                   repo: Path = BLOG_ROOT,
                   wait_sec: int = LOCK_WAIT_SEC) -> bool:
    """<paths> 중 변경분을 `cron(<worker>): <summary> <marker>` 로 커밋한다.

    커밋했으면 True. 변경이 없거나 autopush 가 락을 쥐고 있으면 False 이며 이는
    실패가 아니다 — 파일은 워킹트리에 남고 다음 autopush 틱이 가져간다.

    커밋 대상은 **변경된 것으로 실측된 경로만** pathspec 으로 지정한다. 사용자가
    손으로 staging 해 둔 다른 파일이 cron 커밋에 딸려 들어가지 않게 하려는 것이고,
    아직 존재하지 않는(한 번도 안 만들어진) 산출물 경로를 넘겨도 `git add` 가
    pathspec 불일치로 죽지 않게 하려는 것이다.
    """
    say = log or (lambda _m: None)
    changed = dirty_paths(paths, repo)
    if not changed:
        return False

    subject = f"cron({worker}): {summary}".rstrip()
    if marker:
        subject += f" {marker}"

    fd = os.open(str(AUTOPUSH_LOCK), os.O_CREAT | os.O_RDWR)
    try:
        deadline = time.time() + wait_sec
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except OSError:
                if time.time() >= deadline:
                    say("commit: autopush 가 락을 쥐고 있다 — 건너뜀 "
                        "(다음 autopush 가 가져간다)")
                    return False
                time.sleep(5)

        # 락을 기다리는 동안 상태가 바뀌었을 수 있다 (autopush 가 방금 커밋했다든지).
        changed = dirty_paths(paths, repo)
        if not changed:
            return False
        rc, _, err = _git(repo, "add", "--", *changed)
        if rc != 0:
            say(f"commit: git add 실패 — {err.strip()[:200]}")
            return False
        rc, out, err = _git(repo, "commit", "-m", subject, "--", *changed)
        if rc != 0:
            say(f"commit 실패: {(err.strip() or out.strip())[:200]}")
            _git(repo, "reset", "-q", "--", *changed)
            return False
        say(f"committed: {subject}")
        return True
    finally:
        os.close(fd)
