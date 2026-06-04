#!/usr/bin/env bash
# Drive the long-lived `translation-verify` tmux session (an interactive
# `claude --model haiku`, SUBSCRIPTION-billed) to run one translation-verify
# task, then return. Fire-and-forget: this script injects the prompt and exits;
# it does NOT wait for completion. The session is told to write its verdict to a
# file and then create a `.done` sentinel, which translate_worker.py polls for.
#
# Why a tmux session and not `claude -p`: on this machine `claude -p` bills the
# pay-as-you-go API credit (the rate-limit safety net) BEFORE the subscription,
# whereas an interactive session bills the subscription. See blog memory
# reference_claude_billing_subscription_vs_api.
#
# Why the prompt is passed as a FILE (one-line "Read <file>" via send-keys):
# tmux send-keys turns newlines into Enter (submitting a multi-line paste at its
# first blank line) and mangles $$/backslash. A single-line instruction sidesteps
# both. Adapted from ~/Database/research/cron/tmux/lib.sh.
#
# Usage: verify_session.sh <prompt_file>
set -euo pipefail

SESSION="translation-verify"
MODEL="haiku"
LAUNCH_CWD="/home/junhyeok/math-jh.github.io"   # already-trusted dir (avoids trust dialog)

# cron's PATH is minimal — resolve binaries explicitly.
if command -v claude >/dev/null 2>&1; then CLAUDE_BIN="$(command -v claude)"
elif [ -x "$HOME/.local/bin/claude" ]; then CLAUDE_BIN="$HOME/.local/bin/claude"
else CLAUDE_BIN="claude"; fi
if command -v tmux >/dev/null 2>&1; then TMUX_BIN="$(command -v tmux)"; else TMUX_BIN="tmux"; fi

# `--kill`: tear down the session. The worker calls this at the end of every run
# so the session never lingers idle between cron ticks (it is re-created lazily on
# the next verify). No-op if the session doesn't exist.
if [ "${1:-}" = "--kill" ]; then
  "$TMUX_BIN" kill-session -t "$SESSION" 2>/dev/null || true
  exit 0
fi

PROMPT_FILE="${1:?usage: verify_session.sh <prompt_file> | --kill}"

# claude's TUI shows an interrupt hint while a turn runs (busy). wait_idle also
# falls back to output-stability, so a wrong marker degrades gracefully.
BUSY_RE='esc to interrupt|Esc to interrupt|Interrupt'

log()       { printf '[%s verify-session] %s\n' "$(date '+%H:%M:%S')" "$*" >&2; }
_pane()     { "$TMUX_BIN" capture-pane -t "$SESSION" -p 2>/dev/null || true; }
send_line() { "$TMUX_BIN" send-keys -t "$SESSION" -l -- "$1"; "$TMUX_BIN" send-keys -t "$SESSION" Enter; }

wait_ready() {                                  # REPL accepting input?
  local max="${1:-90}" w=0
  while [ "$w" -lt "$max" ]; do
    if _pane | grep -qiE 'bypass permissions|shortcuts \('; then return 0; fi
    sleep 2; w=$((w + 2))
  done
  return 1
}

wait_idle() {                                   # no busy marker AND pane stable
  local max="${1:-120}" w=0 prev="" cur=""
  while [ "$w" -lt "$max" ]; do
    cur="$(_pane)"
    if ! grep -Eq "$BUSY_RE" <<<"$cur" && [ "$cur" = "$prev" ] && [ -n "$cur" ]; then return 0; fi
    prev="$cur"; sleep 3; w=$((w + 3))
  done
  return 1
}

ensure_session() {                              # launch once if missing
  if "$TMUX_BIN" has-session -t "$SESSION" 2>/dev/null; then return 0; fi
  log "session missing — launching: claude --model $MODEL"
  "$TMUX_BIN" new-session -d -s "$SESSION" -x 220 -y 50
  # Model pinned via launch FLAG (session-scoped). Never send /model — it
  # persists to the shared ~/.claude/settings.json and clobbers the user's
  # interactive default.
  "$TMUX_BIN" send-keys -t "$SESSION" -l -- \
    "cd $LAUNCH_CWD && $CLAUDE_BIN --permission-mode bypassPermissions --model $MODEL"
  "$TMUX_BIN" send-keys -t "$SESSION" Enter
  if ! wait_ready 60; then
    if _pane | grep -qiE 'do you trust|trust the files|trust this folder'; then
      log "trust dialog — accepting default (Enter)"
      "$TMUX_BIN" send-keys -t "$SESSION" Enter
      wait_ready 30 || log "still not ready after accepting trust dialog"
    else
      log "claude not ready after 60s, no trust dialog — check 'tmux attach -t $SESSION'"
    fi
  fi
}

ensure_session
wait_idle 120 || true                           # don't trample a still-running turn
wait_ready || log "wait_ready timed out (proceeding)"
# Clear any stray text in the input box (send-keys APPENDS at the cursor), then
# /clear so the next task starts from an empty conversation (context isolation).
"$TMUX_BIN" send-keys -t "$SESSION" C-e
"$TMUX_BIN" send-keys -t "$SESSION" C-u
send_line "/clear"
sleep 3
send_line "Read $PROMPT_FILE and do exactly what it says. Output nothing in this chat."
