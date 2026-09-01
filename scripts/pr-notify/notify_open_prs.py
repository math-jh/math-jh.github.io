#!/usr/bin/env python3
"""열린 PR 중 아직 안 알린 것을 텔레그램으로 한 통에 묶어 보낸다.

크론 5분 간격. LLM 없이 `gh pr list` 결과와 상태파일 하나만 본다.
댓글 PR(`comment/*`)이 주 용도지만 대상을 가리지 않는다 — dependabot 도 같이 온다.

상태는 ~/.local/state/blog-pr-notify.json 의 `seen` 목록(PR 번호)이다. 번호는
재사용되지 않으므로 지우지 않는다. 닫히거나 머지된 PR을 목록에서 빼면 재오픈 때
다시 알림이 가므로, 가지치기는 일부러 하지 않는다.

상태파일이 없는 첫 실행은 지금 열린 PR을 전부 seen 으로 적고 아무것도 보내지
않는다. 도입 시점에 묵은 PR이 한꺼번에 날아가는 것을 막는다 (--notify-all 로 강제).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = "math-jh/math-jh.github.io"
STATE = Path.home() / ".local/state/blog-pr-notify.json"
GH = "/usr/bin/gh"
NOTIFY = Path.home() / ".local/bin/notify"
MAX_LISTED = 8  # 한 통에 이만큼만 적고 나머지는 건수로 접는다


def log(message: str) -> None:
    stamp = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{stamp}] {message}", flush=True)


def open_pulls() -> list[dict]:
    result = subprocess.run(
        [GH, "pr", "list", "--repo", REPO, "--state", "open", "--limit", "100",
         "--json", "number,title,url,headRefName,author,isDraft"],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gh pr list 실패 rc={result.returncode}: {result.stderr.strip()[:300]}")
    return json.loads(result.stdout or "[]")


def load_seen() -> set[int] | None:
    if not STATE.exists():
        return None
    try:
        return {int(n) for n in json.loads(STATE.read_text()).get("seen", [])}
    except (ValueError, OSError, json.JSONDecodeError) as error:
        # 상태파일이 깨졌을 때 전량 재알림을 내는 것이 조용히 침묵하는 것보다 낫다.
        log(f"상태파일 손상, 새로 만든다: {error!r}")
        return set()


def save_seen(seen: set[int]) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps({"seen": sorted(seen)}, ensure_ascii=False, indent=0) + "\n")
    tmp.replace(STATE)  # 원자적 교체 — 크론이 겹쳐 돌아도 반쪽 파일이 안 남는다


def compose(fresh: list[dict]) -> tuple[str, str]:
    subject = f"[블로그] 새 PR {len(fresh)}건"
    lines = []
    for pull in fresh[:MAX_LISTED]:
        author = (pull.get("author") or {}).get("login", "?")
        draft = " (draft)" if pull.get("isDraft") else ""
        lines.append(f"#{pull['number']} {pull['title']}{draft}")
        lines.append(f"  {pull['headRefName']} · {author}")
        lines.append(f"  {pull['url']}")
    if len(fresh) > MAX_LISTED:
        lines.append(f"… 외 {len(fresh) - MAX_LISTED}건")
    return subject, "\n".join(lines)


def send(subject: str, body: str, url: str) -> None:
    result = subprocess.run(
        [str(NOTIFY), "-s", subject, "-b", body, "-g", "blog", "--url", url],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"notify rc={result.returncode}: {result.stderr.strip()[:300]}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notify-all", action="store_true",
                        help="상태파일이 없어도 지금 열린 PR을 전부 알린다")
    parser.add_argument("--dry-run", action="store_true", help="보내지 않고 출력만 한다")
    args = parser.parse_args()

    try:
        pulls = open_pulls()
    except Exception as error:  # noqa: BLE001 — 크론이므로 로그만 남기고 다음 틱에 다시 본다
        log(f"PR 조회 실패: {error}")
        return 1

    seen = load_seen()
    if seen is None and not args.notify_all:
        save_seen({p["number"] for p in pulls})
        log(f"상태파일 초기화 — 열린 PR {len(pulls)}건을 알림 없이 seen 처리")
        return 0
    seen = seen or set()

    fresh = [p for p in pulls if p["number"] not in seen]
    if not fresh:
        return 0

    subject, body = compose(fresh)
    if args.dry_run:
        log(f"(dry-run) {subject}\n{body}")
        return 0

    try:
        # 한 건이면 그 PR로 곧장, 여러 건이면 저장소의 열린 PR 목록으로 간다.
        url = fresh[0]["url"] if len(fresh) == 1 \
            else f"https://github.com/{REPO}/pulls"
        send(subject, body, url)
    except Exception as error:  # noqa: BLE001
        # 보내지 못했으면 seen 을 갱신하지 않는다. 다음 틱에 다시 시도한다.
        log(f"전송 실패, seen 유지: {error}")
        return 1

    save_seen(seen | {p["number"] for p in fresh})
    log(f"알림 {len(fresh)}건: {', '.join('#' + str(p['number']) for p in fresh)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
