#!/usr/bin/env python3
"""그 작업이 오갔던 세션에서 **사용자 발화만** 뽑는다.

Marvin 은 git history 와 파일만 본다. 그래서 "무엇이 바뀌었는가"는 정확히 쓰지만
"왜 그렇게 정했는가"는 diff 에서 추측하게 되고, 실제로 틀린 유래를 적은 적이 있다
(2026-08-07 dd 스윕 글의 도입부. 사용자가 손으로 고쳤다). 결정은 대화에 있었다.

트랜스크립트는 `~/.claude/projects/<project-slug>/*.jsonl` 이고 사용자 세션은 14 일
보존된다 (`~/.local/bin/reap-claude-sessions.py`, CLAUDE_SESSION_KEEP_DAYS). 커밋
날짜로 창을 잡아 그 구간의 발화를 시간순으로 낸다.

**user 역할 레코드가 곧 사용자 발화는 아니다.** 슬래시 커맨드 본문, `/commit` 이
주입하는 상태 블록, 붙여넣은 검토 지시서, task-notification, system-reminder 가 전부
같은 역할로 들어온다. 아래 DROP 과 길이 상한이 그것들을 걷어낸다.

사용법:
    user_voice.py --shas a8e2c693,69c01388        커밋 날짜에서 창을 잡는다
    user_voice.py --since 2026-08-07 --until 2026-08-09
    user_voice.py --shas a8e2c693 --grep '미분|매크로'
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PROJECT_DIR = Path.home() / ".claude/projects/-home-junhyeok-math-jh-github-io"

# 사용자가 친 것이 아닌 user 역할 레코드.
DROP = re.compile(
    r"<system-reminder>|<local-command-caveat>|<command-name>|<command-message>"
    r"|<task-notification>|<tool-use-id>|Caveat: The messages below"
    r"|^\[cron\]|^# 검토 지시서|^## 현재 상태|^## 절차|이 턴은 bash_guard"
    r"|^\[Request interrupted|^\[Image:|^Continue from where you left off"
)
# 사람이 친 지시는 짧다. 이보다 길면 스킬 본문·붙여넣은 문서다.
MAX_INPUT = 1500


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO), *args], capture_output=True, text=True
    ).stdout


def window_from_shas(shas: list[str], pad_before: int, pad_after: int):
    """커밋 날짜에서 창을 잡는다. 결정은 커밋보다 **앞서** 오가므로 앞을 넓게 준다."""
    stamps = []
    for sha in shas:
        out = git("log", "-1", "--format=%cI", sha).strip()
        if out:
            stamps.append(datetime.fromisoformat(out))
    if not stamps:
        raise SystemExit("커밋 날짜를 못 읽었다: " + ",".join(shas))
    return (min(stamps) - timedelta(days=pad_before),
            max(stamps) + timedelta(days=pad_after))


def texts(rec: dict) -> list[str]:
    content = rec.get("message", {}).get("content")
    if isinstance(content, str):
        return [content]
    if isinstance(content, list):
        return [c.get("text", "") for c in content if c.get("type") == "text"]
    return []


def collect(lo: datetime, hi: datetime, pat: re.Pattern | None, max_chars: int):
    rows, scanned, oldest = [], 0, None
    for path in sorted(glob.glob(str(PROJECT_DIR / "*.jsonl"))):
        scanned += 1
        mtime = datetime.fromtimestamp(os.path.getmtime(path), timezone.utc)
        oldest = mtime if oldest is None else min(oldest, mtime)
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("type") != "user" or not rec.get("timestamp"):
                    continue
                try:
                    when = datetime.fromisoformat(rec["timestamp"].replace("Z", "+00:00"))
                except ValueError:
                    continue
                if not (lo <= when <= hi):
                    continue
                for t in texts(rec):
                    t = t.strip()
                    if not t or len(t) > MAX_INPUT or DROP.search(t):
                        continue
                    if pat and not pat.search(t):
                        continue
                    rows.append((when, Path(path).stem[:8], " ".join(t.split())[:max_chars]))
    rows.sort()
    return rows, scanned, oldest


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shas", help="쉼표로 구분한 커밋 (이 날짜들로 창을 잡는다)")
    ap.add_argument("--since", help="YYYY-MM-DD")
    ap.add_argument("--until", help="YYYY-MM-DD")
    ap.add_argument("--grep", default="", help="주제어 정규식 (생략하면 창 전체)")
    ap.add_argument("--pad-before", type=int, default=2, help="커밋 앞 며칠까지 (기본 2)")
    ap.add_argument("--pad-after", type=int, default=1, help="커밋 뒤 며칠까지 (기본 1)")
    ap.add_argument("--max-chars", type=int, default=600, help="발화 하나의 표시 상한")
    ap.add_argument("--limit", type=int, default=80, help="발화 건수 상한 (기본 80)")
    args = ap.parse_args()

    if args.shas:
        lo, hi = window_from_shas([s.strip() for s in args.shas.split(",") if s.strip()],
                                  args.pad_before, args.pad_after)
    elif args.since and args.until:
        lo = datetime.fromisoformat(args.since).astimezone()
        hi = datetime.fromisoformat(args.until).astimezone()
    else:
        raise SystemExit("--shas 또는 --since/--until 이 필요하다")

    pat = re.compile(args.grep) if args.grep else None
    rows, scanned, oldest = collect(lo, hi, pat, args.max_chars)

    fmt = "%Y-%m-%d %H:%M"
    print(f"# 창: {lo.astimezone().strftime(fmt)} ~ {hi.astimezone().strftime(fmt)}"
          f" · 트랜스크립트 {scanned}개"
          + (f" (가장 오래된 것 {oldest.astimezone().strftime('%Y-%m-%d')})" if oldest else ""))
    shown = rows[: args.limit]
    for when, sid, text in shown:
        print(f"\n[{when.astimezone().strftime('%m-%d %H:%M')} {sid}] {text}")

    if len(rows) > len(shown):
        print(f"\n(상한 {args.limit}건에서 끊었다. 이 창의 발화는 {len(rows)}건이고"
              " 대부분은 다른 작업 이야기다. `--grep '<주제어|주제어>'` 로 좁히거나"
              " `--pad-before 0` 으로 창을 줄여라.)")

    if not rows:
        print("\n(이 창에 사용자 발화가 없다. 보존 기간(14일)을 벗어났거나 그날 대화가"
              " 없었다는 뜻이다. 없는 발화를 지어내지 말고, 결정 근거는 커밋 메시지와"
              " 코드 주석에서만 취한다.)")
    print(f"\n— {len(shown)}/{len(rows)}건")


if __name__ == "__main__":
    main()
