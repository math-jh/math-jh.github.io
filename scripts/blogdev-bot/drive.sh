#!/usr/bin/env bash
# Cron entry point for Marvin (blogdev-bot). Fires daily 10:05; most days the
# mechanical gate below exits before any model is spawned.
# 2026-07-20: tmux 상주 세션 → `claude -p` 단발 전환 (구독 과금 확인).
# 옛 tmux 드라이버는 lib.sh(함수 그대로)와
# ~/.local/share/tmux-bots-archive/blogdev-drive.sh.tmux 에 보존.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib.sh
source "$HERE/lib.sh"   # log·git_sync·CLAUDE_BIN·BLOG_ROOT 재사용 (tmux 함수 미사용)

git_sync

# 기계 게이트 — 새 `[dev]` 커밋이 없으면 LLM을 아예 띄우지 않는다. 예전에는 이
# 판정을 모델이 했으므로, 쓸 게 없는 날도 세션 하나를 온전히 태웠다. 매일 돌리는
# 이상 그 헛턴이 대부분의 날이 된다.
#   exit 0 = 큐에 작업 있음 / 3 = 없음 / 그 외 = 오류
set +e
"$HERE/dev_queue.py" >/dev/null
gate_rc=$?
set -e
case "$gate_rc" in
  0) log "새 [dev] 커밋 있음 — marvin 기동" ;;
  3) log "새 [dev] 커밋 없음 — LLM 호출 없이 종료"; exit 0 ;;
  *) log "dev_queue.py 오류 (rc=$gate_rc) — 중단"; exit 1 ;;
esac

log "launching claude -p (sonnet) for marvin"
cd "$BLOG_ROOT"
if ! timeout 2400 "$CLAUDE_BIN" -p --model sonnet \
      --permission-mode bypassPermissions \
      "Read $HERE/marvin.md and execute it now."; then
  log "claude -p failed"
  exit 1
fi
log "marvin turn complete"
