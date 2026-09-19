#!/usr/bin/env python3
"""블로그 크론 워커 감시 — 상태 전이만 Bark 의 blog 그룹으로 알린다.

블로그 대시보드(:8089)의 /api/summary 를 읽어 세 가지를 본다.

* 워커 정지: 로그가 주기의 2.5배 넘게 멈춤(stale) 또는 로그 없음(missing).
  cron-gate 정지가 풀린 직후에는 정지 동안 늙은 로그가 그대로 stale 로 읽히므로,
  마지막으로 정지를 본 시각부터 한 주기 + 15분 동안은 stale 을 보지 않는다.
* 워커 오류: 마지막 실행 로그의 오류 줄(err). 워커가 이미 붙잡아 자기 알림
  경로로 관리하는 실패(WORKER_HANDLED)는 여기서 다시 알리지 않는다. 붙잡히지 않은
  실패(크래시 등)는 워커 상태에 흔적이 안 남으므로 그대로 알린다.
* 크론 등록 누락과 blog-autopush.timer 비활성.

모든 조건은 2회 연속 확인 후 한 번 알리고, 복구 때 한 번 더 알린다. 첫 실행은
현재 이상을 조용히 기준선으로 삼는다. 대시보드가 응답하지 않으면 로그만 남긴다
(대시보드 중단 알림은 pi-health-monitor 몫이다).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime
from pathlib import Path

HOME = Path.home()
BLOG = HOME / "math-jh.github.io"
SUMMARY_URL = "http://127.0.0.1:8089/api/summary"
STATE_PATH = HOME / ".local/state/blog-worker-health.json"
NOTIFY = HOME / ".local/bin/notify"
THRESHOLD = 2
RESUME_GRACE_SLACK = 15 * 60

TRANSLATION_STATE = BLOG / "scripts/translation/translation_state.json"
TERMS_STATE = BLOG / "scripts/term-extraction/term_extract_worker_state.json"
TERMS_QUARANTINE_SEC = 7 * 24 * 3600   # term_extract_worker.QUARANTINE_SEC


def log(msg: str) -> None:
    print(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}", flush=True)


def load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=STATE_PATH.parent, prefix=".blog-worker-health.")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=1)
        os.replace(name, STATE_PATH)
    finally:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass


def fetch_summary() -> tuple[dict | None, str | None]:
    try:
        with urllib.request.urlopen(SUMMARY_URL, timeout=20) as r:
            return json.loads(r.read().decode("utf-8")), None
    except Exception as e:
        return None, repr(e)[:200]


def timer_active(unit: str) -> bool:
    env = dict(os.environ)
    env.setdefault("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")
    r = subprocess.run(["systemctl", "--user", "is-active", "--quiet", unit],
                       env=env, timeout=15)
    return r.returncode == 0


# ── 워커가 스스로 붙잡아 알리는 실패 ───────────────────────────────────────────
def translation_handled(now: float) -> bool:
    """번역 실패는 record_failure 가 failure_notice 를 세우고 쿨다운을 지켜 알린다."""
    st = load_json(TRANSLATION_STATE) or {}
    return bool(st.get("failure_notice"))


def terms_handled(now: float, interval: float) -> bool:
    """글 단위 실패는 fails 로 세다가 3회째에 격리하며 알린다."""
    posts = (load_json(TERMS_STATE) or {}).get("posts", {})
    for ps in posts.values():
        if ps.get("fails", 0) > 0:
            return True
        q = ps.get("quarantined_until")
        if q and now - (q - TERMS_QUARANTINE_SEC) < 2 * interval:
            return True
    return False


WORKER_HANDLED = {
    "translation": lambda now, interval: translation_handled(now),
    "terms": terms_handled,
}


# ── 조건 추적 ──────────────────────────────────────────────────────────────────
class Monitor:
    def __init__(self, state: dict, initial: bool, dry_run: bool):
        self.state = state
        self.initial = initial
        self.dry_run = dry_run
        self.seen: set[str] = set()

    def notify(self, title: str, body: str, recovery: bool) -> bool:
        if self.dry_run:
            log(f"[dry-run] {title}: {body}")
            return True
        r = subprocess.run([str(NOTIFY), "-s", title, "-b", body, "-g", "blog",
                            "-l", "active" if recovery else "timeSensitive"],
                           capture_output=True, text=True, timeout=30)
        log(f"notification {'sent' if r.returncode == 0 else f'failed rc={r.returncode}'}: {title}")
        return r.returncode == 0

    def condition(self, key: str, bad: bool, title: str, body: str,
                  suppressed: bool = False) -> None:
        self.seen.add(key)
        conds = self.state.setdefault("conditions", {})
        old = conds.get(key)
        if suppressed:
            conds.pop(key, None)
            return
        if self.initial:
            if bad:
                conds[key] = {"count": THRESHOLD, "alerted": False, "muted": True, "body": body}
            return
        if bad:
            if old and old.get("muted"):
                old["body"] = body
                return
            entry = old or {"count": 0, "alerted": False, "since": now_iso()}
            entry["count"] = int(entry.get("count", 0)) + 1
            entry["body"] = body
            if entry["count"] >= THRESHOLD and not entry.get("alerted"):
                if self.notify(title, body, recovery=False):
                    entry["alerted"] = True
            conds[key] = entry
            return
        if not old:
            return
        if old.get("alerted") and not old.get("muted"):
            if not self.notify(f"복구: {title}", "현재 점검에서 정상 상태로 돌아왔습니다.",
                               recovery=True):
                return
        conds.pop(key, None)

    def drop_unseen(self) -> None:
        for key in list(self.state.get("conditions", {})):
            if key not in self.seen:
                self.state["conditions"].pop(key)


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def check(m: Monitor, summary: dict, now: float) -> None:
    last_paused = m.state.setdefault("last_paused", {})

    for w in summary.get("workers", []):
        key = str(w.get("key", "unknown"))
        name = w.get("name", key)
        status = str(w.get("status", "missing"))
        paused = bool(w.get("paused"))
        interval = float(w.get("interval") or 3600)
        if paused:
            last_paused[key] = now
        resumed = last_paused.get(key)
        in_grace = bool(resumed) and now - resumed < interval + RESUME_GRACE_SLACK

        m.condition(f"stale:{key}", status in {"stale", "missing"}, "블로그 워커 정지",
                    f"{name}: status={status}, 마지막 실행 {fmt_age(w.get('age'))} 전",
                    suppressed=paused or in_grace)

        handled = WORKER_HANDLED.get(key)
        err = bool(w.get("err"))
        m.condition(f"err:{key}", err, "블로그 워커 오류",
                    f"{name}: 마지막 실행 로그에 오류가 있습니다.",
                    suppressed=paused or bool(err and handled and handled(now, interval)))

    items = (summary.get("cron") or {}).get("items", [])
    for job in items:
        job_id = str(job.get("id", "unknown"))
        m.condition(f"cron:{job_id}", bool(job.get("missing")), "블로그 크론 등록 누락",
                    f"{job_id}가 crontab/timer 등록에서 사라졌습니다.",
                    suppressed=bool(job.get("paused")))

    autopush_paused = any(j.get("id") == "timer:blog-autopush" and j.get("paused") for j in items)
    m.condition("timer:blog-autopush", not timer_active("blog-autopush.timer"),
                "블로그 autopush 타이머 중단", "blog-autopush.timer가 active가 아닙니다.",
                suppressed=autopush_paused)


def fmt_age(age) -> str:
    if not isinstance(age, (int, float)):
        return "?"
    h = age / 3600
    return f"{h:.1f}시간" if h < 48 else f"{h / 24:.1f}일"


def main() -> int:
    dry_run = "--dry-run" in sys.argv[1:]
    now = time.time()
    state = load_json(STATE_PATH)
    initial = state is None
    state = state or {}

    summary, err = fetch_summary()
    if summary is None:
        log(f"대시보드 응답 없음, 점검 생략 ({err})")
        return 0

    m = Monitor(state, initial, dry_run)
    check(m, summary, now)
    m.drop_unseen()
    state["checked_at"] = now_iso()
    bad = [k for k, v in state.get("conditions", {}).items()]
    if not dry_run:
        save_state(state)
    if initial or bad:
        log(f"{'seed ' if initial else ''}이상 {len(bad)}건: {', '.join(bad) or '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
