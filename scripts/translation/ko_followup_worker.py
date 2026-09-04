#!/usr/bin/env python3
"""Follow up dashboard-confirmed Korean fixes and synchronize the English post.

The dashboard checkbox is a request, not an acknowledgement.  One request is
handled per run: Antigravity proposes the narrowly scoped EN replacement, then
Codex sees only the original finding plus KO/EN unified diffs and decides whether
both changes implement that finding.  The queue item is removed only after a
passing check and a successful content commit.
"""

from __future__ import annotations

import difflib
import fcntl
import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import translate_worker as tw


REQUEST_STATE = Path.home() / ".local/state/blog_dashboard_kotypo.json"
LOG_PREFIX = "KO-FOLLOWUP"
MAX_REPLACEMENTS = 12


def log(message: str) -> None:
    tw.log(f"{LOG_PREFIX}: {message}")


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def _repair_latex_controls(value):
    """Repair legacy model JSON where `\\times` decoded as TAB + ``imes``."""
    if isinstance(value, str):
        return value.replace("\times", r"\times")
    if isinstance(value, list):
        return [_repair_latex_controls(v) for v in value]
    if isinstance(value, dict):
        return {k: _repair_latex_controls(v) for k, v in value.items()}
    return value


def _line_for_quote(text: str, quote: str) -> int | None:
    pos = text.find(quote)
    return text.count("\n", 0, pos) + 1 if pos >= 0 else None


def _diff(old: str, new: str, old_name: str, new_name: str) -> str:
    lines = difflib.unified_diff(
        old.splitlines(), new.splitlines(), fromfile=old_name, tofile=new_name,
        lineterm="", n=4,
    )
    return "\n".join(lines) or "(no changes)"


def _fallback_ko_base(path: str, reviewed_at: str) -> str | None:
    cmd = ["git", "rev-list", "-1"]
    if reviewed_at:
        cmd.append(f"--before={reviewed_at}")
    cmd.extend(["HEAD", "--", path])
    proc = subprocess.run(cmd, cwd=tw.BLOG_ROOT, capture_output=True, text=True)
    commit = proc.stdout.strip()
    if proc.returncode != 0 or not commit:
        return None
    shown = subprocess.run(
        ["git", "show", f"{commit}:{path}"], cwd=tw.BLOG_ROOT,
        capture_output=True, text=True,
    )
    return shown.stdout if shown.returncode == 0 else None


def _actionable_findings(entry: dict, baseline: str) -> list[dict]:
    out = []
    for raw in entry.get("verify_ko_typos_review") or []:
        finding = _repair_latex_controls(dict(raw))
        if str(finding.get("verdict") or "UNSURE").upper() == "FALSE":
            continue
        if not finding.get("line"):
            finding["line"] = _line_for_quote(baseline, str(finding.get("quote") or ""))
        out.append(finding)
    return out


ANTIGRAVITY_PROMPT = """You are applying a narrowly scoped follow-up to an English mathematics post.

The Korean author edited the KO file in response to the original reviewed findings.
Use the KO unified diff and those findings to update the current English file. Make
only English changes required by the accepted KO changes. Preserve every unrelated
byte, all LaTeX, Jekyll syntax, anchors, references, and translation provenance.
Do not correct or enrich anything outside the original findings.

Return JSON only:
{"replacements":[{"old":"exact unique substring from current EN","new":"replacement"}]}

Each `old` must occur exactly once in CURRENT EN. Use JSON-compliant double
backslashes for LaTeX. If the English already expresses the corrected Korean,
return {"replacements":[]}.

ORIGINAL FINDINGS:
@@FINDINGS@@

KO DIFF (audit baseline -> current):
@@KO_DIFF@@

CURRENT EN:
--- BEGIN EN ---
@@CURRENT_EN@@
--- END EN ---
"""


def antigravity_candidate(current_en: str, findings: list[dict], ko_diff: str) -> str:
    prompt = (ANTIGRAVITY_PROMPT
              .replace("@@FINDINGS@@", json.dumps(findings, ensure_ascii=False, indent=2))
              .replace("@@KO_DIFF@@", ko_diff)
              .replace("@@CURRENT_EN@@", current_en))
    payload = tw._parse_json_object(tw.call_translator(prompt, thinking=False))
    replacements = payload.get("replacements") if isinstance(payload, dict) else None
    if not isinstance(replacements, list) or len(replacements) > MAX_REPLACEMENTS:
        raise RuntimeError("Antigravity returned an invalid replacement list")
    candidate = current_en
    for item in replacements:
        if not isinstance(item, dict):
            raise RuntimeError("Antigravity replacement is not an object")
        old = str(item.get("old") or "")
        new = str(item.get("new") or "")
        if not old or candidate.count(old) != 1:
            raise RuntimeError("Antigravity replacement source is not unique")
        candidate = candidate.replace(old, new, 1)
    return candidate


CODEX_PROMPT = """Review one completed Korean-source correction and its English follow-up.

You receive ONLY the original reviewed findings and the two unified diffs. Judge
whether the KO diff resolves exactly the original issue, and whether the EN diff
faithfully reflects that resolved Korean meaning without invention, omission, or
unrelated rewriting. An empty EN diff is acceptable only when the old English
already expressed the corrected meaning. Do not use outside mathematical knowledge
to broaden the requested correction. Do not fail harmless spelling, punctuation,
or synonymous terminology cleanup within the same edited sentence; fail only an
unrelated semantic change or an English change unsupported by the corrected KO.

Return JSON only:
{"pass":true,"why":"short concrete reason"}

ORIGINAL FINDINGS:
@@FINDINGS@@

KO DIFF:
@@KO_DIFF@@

EN DIFF:
@@EN_DIFF@@
"""


def codex_pass(findings: list[dict], ko_diff: str, en_diff: str) -> tuple[bool, str]:
    prompt = (CODEX_PROMPT
              .replace("@@FINDINGS@@", json.dumps(findings, ensure_ascii=False, indent=2))
              .replace("@@KO_DIFF@@", ko_diff)
              .replace("@@EN_DIFF@@", en_diff))
    with tempfile.TemporaryDirectory(prefix="codex-ko-followup-") as tmp:
        out_path = Path(tmp) / "last-message.json"
        proc = subprocess.run(
            [tw.CODEX_BIN, "exec", "--ignore-user-config",
             "--model", tw.CODEX_REVIEW_MODEL,
             "-c", f'model_reasoning_effort="{tw.CODEX_REVIEW_EFFORT}"',
             "--sandbox", "read-only", "--skip-git-repo-check", "--ephemeral",
             "--color", "never", "--output-last-message", str(out_path), "-"],
            input=prompt, capture_output=True, text=True,
            timeout=tw.CODEX_REVIEW_TIMEOUT_SEC, cwd=tmp,
        )
        if proc.returncode != 0 or not out_path.exists():
            raise RuntimeError(
                f"Codex follow-up exited {proc.returncode}: {tw._flat(proc.stderr)[:180]}"
            )
        payload = tw._parse_json_object(out_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("pass"), bool):
        raise RuntimeError("Codex returned an invalid follow-up JSON shape")
    return payload["pass"], str(payload.get("why") or "").strip()[:500]


def _acquire_autopush_lock() -> int | None:
    deadline = time.time() + tw.COMMIT_LOCK_WAIT_SEC
    fd = os.open(str(tw.AUTOPUSH_LOCK), os.O_CREAT | os.O_RDWR)
    while True:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            return fd
        except OSError:
            if time.time() >= deadline:
                os.close(fd)
                return None
            time.sleep(5)


def _commit_pair(ko_path: Path, en_path: Path) -> tuple[bool, str]:
    rel_ko = str(ko_path.relative_to(tw.BLOG_ROOT))
    rel_en = str(en_path.relative_to(tw.BLOG_ROOT))
    changed = subprocess.run(
        ["git", "diff", "--quiet", "--", rel_ko, rel_en], cwd=tw.BLOG_ROOT,
    ).returncode != 0
    if not changed:
        return True, "already committed"
    name = subprocess.run(
        ["git", "config", "user.name"], cwd=tw.BLOG_ROOT,
        capture_output=True, text=True,
    ).stdout.strip() or "Junhyeok Kim"
    email = subprocess.run(
        ["git", "config", "user.email"], cwd=tw.BLOG_ROOT,
        capture_output=True, text=True,
    ).stdout.strip() or "math-jh@users.noreply.github.com"
    env = {
        **os.environ,
        "GIT_AUTHOR_NAME": name,
        "GIT_AUTHOR_EMAIL": email,
        "GIT_COMMITTER_NAME": "Claude",
        "GIT_COMMITTER_EMAIL": "noreply@anthropic.com",
    }
    title = tw._post_title(en_path)
    proc = subprocess.run(
        ["git", "commit", "--only", "-m",
         f"cron(translate-followup): KO 수정 반영 및 EN 동기화: {title}",
         "--", rel_ko, rel_en],
        cwd=tw.BLOG_ROOT, capture_output=True, text=True, env=env,
    )
    return proc.returncode == 0, tw._flat(proc.stderr or proc.stdout)[:300]


def _clear_completed(entry: dict) -> None:
    for key in (
        "verify_ko_typos", "verify_ko_typos_review", "ko_reviewed_at",
        "ko_review_base_content", "ko_review_base_sha256",
    ):
        entry.pop(key, None)
    entry["ko_followup_completed_at"] = datetime.now(timezone.utc).isoformat(
        timespec="seconds"
    )


def run_one() -> int:
    requests = _read_json(REQUEST_STATE)
    state = tw.load_state()
    files = state.get("files", {})

    target = None
    stale = []
    for request_key in requests:
        path, sep, reviewed_at = request_key.rpartition("@")
        entry = files.get(path)
        if not sep or not entry or entry.get("ko_reviewed_at", "") != reviewed_at:
            stale.append(request_key)
            continue
        target = (request_key, path, reviewed_at, entry)
        break
    if stale:
        latest = _read_json(REQUEST_STATE)
        for key in stale:
            latest.pop(key, None)
        _write_json(REQUEST_STATE, latest)
        log(f"stale request {len(stale)}건 정리")
    if target is None:
        log("nothing requested")
        return 0

    request_key, path, reviewed_at, entry = target
    ko_path = tw.BLOG_ROOT / path
    en_rel = entry.get("en_path") or ""
    en_path = tw.BLOG_ROOT / en_rel
    if not ko_path.is_file() or not en_path.is_file():
        log(f"WAIT {path}: KO/EN 파일을 찾지 못함")
        return 1

    baseline = entry.get("ko_review_base_content") or _fallback_ko_base(path, reviewed_at)
    if baseline is None:
        log(f"WAIT {path}: KO 감사 기준 판본을 복원하지 못함")
        return 1
    findings = _actionable_findings(entry, baseline)
    if not findings:
        log(f"WAIT {path}: 검증할 유효 지적이 없음")
        return 1

    current_ko = ko_path.read_text(encoding="utf-8")
    current_en = en_path.read_text(encoding="utf-8")
    ko_diff = _diff(baseline, current_ko, f"a/{path}", f"b/{path}")
    if ko_diff == "(no changes)":
        log(f"WAIT {path}: 체크 후 KO 변경이 없음")
        return 0

    log(f"START {path}: 지적 {len(findings)}건, Antigravity EN 반영")
    try:
        candidate = antigravity_candidate(current_en, findings, ko_diff)
        warnings: list[str] = []
        hard_error = tw.validate_translation(
            candidate, ko_content=current_ko, reason="polish",
            en_current=current_en, warnings=warnings,
        )
        old_lints = set(tw.lint_latex(current_en))
        new_lints = set(tw.lint_latex(candidate)) - old_lints
        old_struct = set(tw.lint_structure(baseline, current_en))
        new_struct = set(tw.lint_structure(current_ko, candidate)) - old_struct
        if hard_error or new_lints or new_struct:
            detail = hard_error or next(iter(new_lints or new_struct))
            raise RuntimeError(f"deterministic gate: {detail}")
        en_diff = _diff(current_en, candidate, f"a/{en_rel}", f"b/{en_rel}")
        passed, why = codex_pass(findings, ko_diff, en_diff)
    except Exception as exc:
        log(f"WAIT {path}: {tw._flat(exc)[:240]}")
        return 1
    if not passed:
        log(f"WAIT {path}: Codex 미통과 — {tw._flat(why)}")
        return 0

    fd = _acquire_autopush_lock()
    if fd is None:
        log(f"WAIT {path}: autopush 락을 얻지 못함")
        return 1
    try:
        if _sha(ko_path.read_text(encoding="utf-8")) != _sha(current_ko) \
                or _sha(en_path.read_text(encoding="utf-8")) != _sha(current_en):
            log(f"WAIT {path}: 검증 중 KO/EN 파일이 다시 바뀜")
            return 1
        en_path.write_text(candidate, encoding="utf-8")
        committed, detail = _commit_pair(ko_path, en_path)
        if not committed:
            en_path.write_text(current_en, encoding="utf-8")
            subprocess.run(
                ["git", "reset", "-q", "--", str(en_path.relative_to(tw.BLOG_ROOT))],
                cwd=tw.BLOG_ROOT,
            )
            log(f"WAIT {path}: 커밋 실패 — {detail}")
            return 1
    finally:
        os.close(fd)

    _clear_completed(entry)
    entry["reason"] = "ko-followup"
    entry["ko_git_commit_ts"] = tw.git_last_commit_ts(ko_path)
    tw.save_state(state)
    latest = _read_json(REQUEST_STATE)
    latest.pop(request_key, None)
    _write_json(REQUEST_STATE, latest)
    log(f"PASS {path}: KO·EN diff 승인, 큐 제거 — {tw._flat(why)}")
    return 0


def main() -> int:
    if not Path(tw.AGY_BIN).exists() or not Path(tw.CODEX_BIN).exists():
        log("translator or Codex CLI missing")
        return 2
    if not tw.acquire_lock():
        log("another translation instance running, exit")
        return 0
    try:
        return run_one()
    finally:
        tw.release_lock()


if __name__ == "__main__":
    raise SystemExit(main())
