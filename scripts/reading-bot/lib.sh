#!/usr/bin/env bash
# Tmux-driver helpers for Marvin (reading-bot).
# Long-lived `claude` session named $R_SESSION. Each tick: ensure session is
# up, git sync the blog, /clear context, inject a one-liner pointing at
# marvin.md. The model is pinned via the `--model` launch flag only (NOT the
# `/model` slash command, which persists to the *shared* ~/.claude/settings.json
# and would clobber the user's interactive default every tick). Fire-and-forget;
# turn runs visibly in the session. `tmux attach -t reader-bot` to watch.

set -euo pipefail

R_SESSION="reader-bot"
BLOG_ROOT="$HOME/math-jh.github.io"
BOT_MODEL="haiku"

if [ -x "$HOME/.npm-global/bin/claude" ]; then
  CLAUDE_BIN="$HOME/.npm-global/bin/claude"
elif command -v claude >/dev/null 2>&1; then
  CLAUDE_BIN="$(command -v claude)"
else
  CLAUDE_BIN="claude"
fi

BUSY_RE='esc to interrupt|Esc to interrupt|Interrupt'

log() { printf '[%s reader-bot] %s\n' "$(date '+%H:%M:%S')" "$*" >&2; }

_pane() { tmux capture-pane -t "$R_SESSION" -p 2>/dev/null || true; }

ensure_session() {
  if tmux has-session -t "$R_SESSION" 2>/dev/null; then
    return 0
  fi
  log "session '$R_SESSION' missing — launching claude"
  tmux new-session -d -s "$R_SESSION" -x 220 -y 50
  tmux send-keys -t "$R_SESSION" -l -- \
    "cd $BLOG_ROOT && $CLAUDE_BIN --permission-mode bypassPermissions --model $BOT_MODEL"
  tmux send-keys -t "$R_SESSION" Enter
  if ! wait_ready 60; then
    if _pane | grep -qiE 'do you trust|trust the files|trust this folder'; then
      log "trust dialog detected — accepting default (Enter)"
      tmux send-keys -t "$R_SESSION" Enter
      wait_ready 30 || log "still not ready after trust dialog — check manually"
    else
      log "claude not ready after 60s — check 'tmux attach -t $R_SESSION'"
    fi
  fi
}

git_sync() {
  git -C "$BLOG_ROOT" pull --rebase --autostash >/dev/null 2>&1 || \
    log "git pull --rebase failed (continuing)"
}

wait_idle() {
  local max_secs="${1:-90}" waited=0 prev="" cur=""
  while [ "$waited" -lt "$max_secs" ]; do
    cur="$(_pane)"
    if ! grep -Eq "$BUSY_RE" <<<"$cur" && [ "$cur" = "$prev" ] && [ -n "$cur" ]; then
      return 0
    fi
    prev="$cur"
    sleep 3
    waited=$((waited + 3))
  done
  log "wait_idle timed out after ${max_secs}s (proceeding anyway)"
  return 1
}

send_line() {
  tmux send-keys -t "$R_SESSION" -l -- "$1"
  tmux send-keys -t "$R_SESSION" Enter
}

wait_ready() {
  local max="${1:-90}" waited=0
  while [ "$waited" -lt "$max" ]; do
    if _pane | grep -qiE 'bypass permissions|shortcuts \('; then return 0; fi
    sleep 2; waited=$((waited + 2))
  done
  return 1
}

send_verify() {
  local cmd="$1" expect="$2" attempt w
  for attempt in 1 2 3; do
    send_line "$cmd"
    w=0
    while [ "$w" -lt 12 ]; do
      sleep 1; w=$((w + 1))
      if _pane | grep -qiE "$expect"; then return 0; fi
    done
    log "retry: '$cmd' not confirmed (/$expect/), attempt $attempt"
  done
  log "WARNING: '$cmd' never confirmed (/$expect/) — proceeding anyway"
  return 0
}

prep_marvin() {
  wait_idle 100 || true
  wait_ready || log "wait_ready timed out (proceeding)"
  tmux send-keys -t "$R_SESSION" C-e
  tmux send-keys -t "$R_SESSION" C-u
  send_line "/clear"
  sleep 3
  # NOTE: deliberately NOT re-asserting the model via `/model $BOT_MODEL` here.
  # The `/model` slash command persists the choice to the shared
  # ~/.claude/settings.json, clobbering the user's interactive default (opus)
  # on every tick. The session is already pinned to $BOT_MODEL by the
  # `--model` launch flag in ensure_session(), which is session-scoped and
  # never touches settings.json. /clear does not reset the model, so haiku
  # persists for the session's lifetime without re-asserting it.
}

# Delete bot-injected Claude session jsonl files so they stop cluttering
# `claude --resume`. Identified by the fixed first-user-prompt we send via
# tmux. Scoped to the blog project directory, and we keep files modified in
# the last 10 minutes to avoid deleting the still-running session.
cleanup_bot_sessions() {
  # Match the injected prompt as a user message *content* field, not just any
  # appearance of the string — otherwise normal sessions that happened to read
  # or grep marvin.md would also match.
  local pattern='"content":"Read [^"]*/scripts/(reading-bot|blogdev-bot)/marvin\.md and execute it now\."'
  local d f deleted=0
  for d in \
    "$HOME/.claude/projects/-home-junhyeok-math-jh-github-io"
  do
    [ -d "$d" ] || continue
    while IFS= read -r f; do
      if grep -qE "$pattern" "$f" 2>/dev/null; then
        rm -f "$f"
        deleted=$((deleted + 1))
      fi
    done < <(find "$d" -maxdepth 1 -type f -name '*.jsonl' -mmin +10 2>/dev/null)
  done
  [ "$deleted" -gt 0 ] && log "cleaned $deleted bot session file(s)"
  return 0
}
