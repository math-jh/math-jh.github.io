#!/usr/bin/env bash
# 대시보드 서버 재기동.
#
# pgrep 패턴은 명령줄 시작부터 서버 프로세스 꼴 전체로 앵커한다. 부분 문자열
# 매치("dashboard/server[.]py")를 쓰면 그 경로를 인자로 언급만 한 셸(bash -c)까지
# 잡아 죽인다 — 호출한 세션이 exit 144 로 끊기는 사고가 네 번 있었다.
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$HOME/.local/state/blog_dashboard.log"
PAT='^/usr/bin/python3 [^ ]*/dashboard/server\.py$'

for pid in $(pgrep -f "$PAT"); do
  kill "$pid" 2>/dev/null
done
sleep 1
setsid /usr/bin/python3 "$DIR/server.py" >>"$LOG" 2>&1 < /dev/null &
sleep 2
pgrep -af "$PAT" || { echo "기동 실패 — $LOG 확인"; exit 1; }
