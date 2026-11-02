#!/usr/bin/env python3
"""Model calls for the shadow pipeline: one fixed model per stage, no fallback.

S1 is Antigravity, S2 Claude Opus, S3 Codex.  A stage never borrows another
stage's model: the votes are meant to be independent, so a closed quota makes the
scheduler pick other work instead of substituting a model.

Each call returns ``(payload, usage)``.  ``usage`` is whatever token accounting
the CLI reports, kept so the pilot can measure what a judgment costs.

Calls are kept lean on purpose.  Antigravity runs the tool-less agent
``blog-dependency-judge`` (~/.gemini/config/agents), which halves its fixed
prompt overhead; Claude runs with no tools and a one-line system prompt from
/tmp.  The first user message of a Claude call starts with the literal
``[cron]`` — reap-claude-sessions.py deletes bot transcripts by that prefix.

Billing of S2 (2026-11-02).  Once the quota gate lets an S2 call through,
``claude-credit route`` (~/.local/bin) picks who pays for it: the Max plan's
monthly API credits or the subscription.  It picks the credits when the 7d
forecast runs out (the HUD's formula) or in the credit cycle's last week; the
gate itself is untouched, so a held Claude quota still stops S2.  A credit call
is the same request run as ``claude --bare --no-session-persistence`` with the
Console key — bare mode reads only that key, never the subscription login, and
leaves no transcript.  If the credits are refused (used up, key rejected) the
call is reported with ``claude-credit exhausted`` and run again on the
subscription.  ``usage["billing"]`` records which one paid.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path

import dependency_classifier as dc

STAGES = ("S1", "S2", "S3")
PROVIDER = {"S1": "Antigravity", "S2": "Claude Opus", "S3": "Codex"}

AGY_BIN = dc.AGY_BIN
# No model ID, only an effort level: the house convention, so a model generation
# change on the Antigravity side cannot break the call (a pinned ID fails with
# "not recognized").  medium, not high: on a whole-article prompt high spends ~4k
# thinking tokens per link and overruns the output limit; medium gave the same
# relations on the 2026-10-17 probe at half the tokens.
AGY_EFFORT = os.environ.get("DEPENDENCY_SHADOW_AGY_EFFORT", "medium")
AGY_AGENT = os.environ.get("DEPENDENCY_AGY_AGENT", "blog-dependency-judge")
CLAUDE_BIN = dc.CLAUDE_BIN
CLAUDE_MODEL = dc.CLAUDE_MODEL
CODEX_BIN = dc.CODEX_BIN
# Empty by default, like the classifier's: Codex then uses its configured model.
CODEX_MODEL = dc.CODEX_REVIEW_MODEL
CODEX_EFFORT = dc.CODEX_REVIEW_EFFORT
TIMEOUT = int(os.environ.get("DEPENDENCY_SHADOW_TIMEOUT", "1500"))
CLAUDE_SYSTEM = ("You are a judging engine for the internal links of a mathematics blog. "
                 "Follow the user prompt exactly and return only the requested JSON.")
CREDIT_BIN = os.environ.get("CLAUDE_CREDIT_BIN",
                            str(Path.home() / ".local" / "bin" / "claude-credit"))
CREDIT_CALLER = "dependency-shadow-S2"
# What the API says when the organization has no credit left.
CREDIT_REFUSED = re.compile(r"credit balance|purchase credits|add funds", re.I)
# 인자 하나의 한도는 페이지 크기의 32배다 (이 Pi 는 16K 페이지라 512 KiB). agy 는
# 프롬프트를 인자로 받으므로 넘기 전에 잘라야 한다 — 여유를 두고 400 KB.
MAX_PROMPT_BYTES = int(os.environ.get("DEPENDENCY_SHADOW_MAX_PROMPT_BYTES", "400000"))


class ModelError(RuntimeError):
    pass


# The last raw response text, kept so a caller can save it when validation drops rows.
LAST_RAW = ""


_HEX = set("0123456789abcdefABCDEF")


def repair_json_text(raw: str) -> str:
    """Make a model's almost-JSON parseable without touching what it meant.

    Models quote the source verbatim, and the source is full of LaTeX, so a
    string may carry ``\\im`` or ``\\[`` unescaped (invalid escapes), or ``\\theta``
    that a decoder would read as a tab followed by "heta".  Inside strings, a
    backslash that does not start a valid escape — or that starts a LaTeX command
    (an escape letter followed by more letters) — is doubled, and raw newlines
    become ``\\n``.
    """
    out = []
    i, n = 0, len(raw)
    in_str = False
    while i < n:
        ch = raw[i]
        if not in_str:
            out.append(ch)
            if ch == '"':
                in_str = True
            i += 1
            continue
        if ch == '"':
            out.append(ch)
            in_str = False
            i += 1
            continue
        if ch == "\\" and i + 1 < n:
            nxt = raw[i + 1]
            if nxt in '"\\/':
                out.append(raw[i:i + 2])
                i += 2
                continue
            if nxt == "u" and all(c in _HEX for c in raw[i + 2:i + 6]) and len(raw[i + 2:i + 6]) == 4:
                out.append(raw[i:i + 6])
                i += 6
                continue
            if nxt in "bfnrt" and not (i + 2 < n and raw[i + 2].isascii() and raw[i + 2].isalpha()):
                out.append(raw[i:i + 2])
                i += 2
                continue
            out.append("\\\\")
            i += 1
            continue
        if ch == "\n":
            out.append("\\n")
        elif ch == "\t":
            out.append("\\t")
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def parse_model_json(raw: str) -> dict:
    """The first JSON object in a reply, repairing LaTeX-laden strings if needed."""
    import re
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip(), flags=re.I)
    decoder = json.JSONDecoder()
    for candidate in (text, repair_json_text(text)):
        start = candidate.find("{")
        while start >= 0:
            try:
                value, _ = decoder.raw_decode(candidate[start:])
            except json.JSONDecodeError:
                start = candidate.find("{", start + 1)
                continue
            if isinstance(value, dict) and ("items" in value or start == candidate.find("{")):
                return value
            start = candidate.find("{", start + 1)
    raise ModelError(f"model returned no JSON object: {raw[:300]!r}")


def available(stage: str) -> bool:
    return dc.provider_available(PROVIDER[stage])


def _run_until_envelope(args: list[str]) -> str:
    """Run agy and return its JSON envelope as soon as it is complete.

    agy sometimes finishes the turn, prints the envelope, and then does not exit
    (2026-10-17: the stream stopped at 20:53 and the process was still alive past
    21:05).  Reading the pipe as it fills and stopping at the first complete
    envelope keeps such a hang from holding a tick until the timeout.
    """
    import threading
    proc = subprocess.Popen(args, cwd="/tmp", stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out: list[bytes] = []
    err: list[bytes] = []

    def pump(stream, sink) -> None:
        while True:
            chunk = stream.read1(65536)
            if not chunk:
                return
            sink.append(chunk)

    readers = [threading.Thread(target=pump, args=(proc.stdout, out), daemon=True),
               threading.Thread(target=pump, args=(proc.stderr, err), daemon=True)]
    for t in readers:
        t.start()
    deadline = time.monotonic() + TIMEOUT
    while True:
        if proc.poll() is not None:
            readers[0].join(10)
            break
        text = b"".join(out).decode("utf-8", "replace").strip()
        if text.endswith("}"):
            try:
                json.loads(text)
            except json.JSONDecodeError:
                pass
            else:
                proc.terminate()
                try:
                    proc.wait(10)
                except subprocess.TimeoutExpired:
                    proc.kill()
                return text
        if time.monotonic() > deadline:
            proc.kill()
            raise ModelError(f"Antigravity gave no envelope within {TIMEOUT}s")
        time.sleep(2)
    if proc.returncode:
        raise ModelError(f"Antigravity exited {proc.returncode}: "
                         f"{b''.join(err).decode('utf-8', 'replace').strip()[:400]}")
    return b"".join(out).decode("utf-8", "replace")


def _agy(prompt: str) -> tuple[dict, dict]:
    raw = _run_until_envelope(
        [AGY_BIN, "--print", prompt, "--agent", AGY_AGENT, "--effort", AGY_EFFORT,
         "--output-format", "json", "--disable-slash-commands", "--print-timeout", "20m"])
    envelope = json.loads(raw)
    if envelope.get("status") != "SUCCESS":
        raise ModelError(f"Antigravity status {envelope.get('status')}: "
                         f"{str(envelope.get('error', ''))[:300]}")
    usage = dict(envelope.get("usage") or {})
    usage["turns"] = envelope.get("num_turns")
    global LAST_RAW
    LAST_RAW = str(envelope.get("response", ""))
    return parse_model_json(LAST_RAW), usage


def _credit_cli(*args: str) -> subprocess.CompletedProcess | None:
    try:
        return subprocess.run([CREDIT_BIN, *args], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None


def _credit_key() -> tuple[str, str]:
    """``(api key, reason)`` when this call should be paid with the plan's API
    credits, ``("", reason)`` when it goes on the subscription.  Anything the
    router can't answer means the subscription — the path S2 always used."""
    proc = _credit_cli("route", "--json")
    if proc is None or proc.returncode:
        return "", "credit router unavailable"
    try:
        route = json.loads(proc.stdout)
    except ValueError:
        return "", "credit router output unreadable"
    reason = str(route.get("reason", ""))
    if route.get("route") != "credit":
        return "", reason
    try:
        return Path(route["key_file"]).read_text(encoding="utf-8").strip(), reason
    except (KeyError, OSError):
        return "", "credit key unreadable"


def _run_claude(prompt: str, api_key: str = "") -> subprocess.CompletedProcess:
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    env.pop("ANTHROPIC_API_KEY", None)
    env.pop("ANTHROPIC_AUTH_TOKEN", None)
    mode: list[str] = []
    if api_key:
        mode = ["--bare", "--no-session-persistence"]
        env["ANTHROPIC_API_KEY"] = api_key
    return subprocess.run(
        [CLAUDE_BIN, *mode, "-p", "--model", CLAUDE_MODEL, "--tools", "",
         "--system-prompt", CLAUDE_SYSTEM, "--output-format", "json"],
        input="[cron]\n\n" + prompt, cwd="/tmp", env=env,
        capture_output=True, text=True, timeout=TIMEOUT,
    )


def _credit_refusal(proc: subprocess.CompletedProcess) -> str:
    """``"credit"``/``"auth"`` when the API refused the credit call for billing or
    the key, ``""`` when it answered (or broke for some other reason)."""
    try:
        envelope = json.loads(proc.stdout)
    except ValueError:
        envelope = {}
    if not isinstance(envelope, dict):
        envelope = {}
    if proc.returncode == 0 and not envelope.get("is_error"):
        return ""
    if envelope.get("api_error_status") in (401, 403):
        return "auth"
    if CREDIT_REFUSED.search(f"{envelope.get('result', '')} {proc.stderr}"):
        return "credit"
    return ""


def _claude(prompt: str) -> tuple[dict, dict]:
    api_key, reason = _credit_key()
    if api_key:
        proc = _run_claude(prompt, api_key)
        refusal = _credit_refusal(proc)
        if not refusal:
            # Record the spend before parsing: a reply that fails validation was still paid for.
            try:
                cost = float(json.loads(proc.stdout).get("total_cost_usd") or 0)
            except (ValueError, AttributeError, TypeError):
                cost = 0.0
            _credit_cli("record", "--cost", str(cost), "--by", CREDIT_CALLER)
            payload, usage = _claude_result(proc)
            usage["billing"] = "credit"
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] S2 billed to API credits ({reason})",
                  flush=True)
            return payload, usage
        try:
            detail = str(json.loads(proc.stdout).get("result", ""))
        except (ValueError, AttributeError):
            detail = proc.stderr
        _credit_cli("exhausted", "--kind", refusal, "--detail", detail[:300], "--by", CREDIT_CALLER)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] S2 API credits refused ({refusal}); "
              "running it on the subscription", flush=True)
    payload, usage = _claude_result(_run_claude(prompt))
    usage["billing"] = "subscription"
    return payload, usage


def _claude_result(proc: subprocess.CompletedProcess) -> tuple[dict, dict]:
    if proc.returncode:
        raise ModelError(f"Claude Opus exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    envelope = json.loads(proc.stdout)
    if envelope.get("is_error"):
        raise ModelError(f"Claude Opus returned an error: {str(envelope.get('result', ''))[:300]}")
    usage = dict(envelope.get("usage") or {})
    usage["turns"] = envelope.get("num_turns")
    usage["cost_usd"] = envelope.get("total_cost_usd")
    global LAST_RAW
    LAST_RAW = str(envelope.get("result", ""))
    return parse_model_json(LAST_RAW), usage


def _codex_failure(stdout: str) -> str:
    """The message of the last error event in Codex's --json stream.  An upstream
    failure leaves stderr empty and reports itself only here."""
    message = ""
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        if event.get("type") == "error":
            message = str(event.get("message") or message)
        elif event.get("type") == "turn.failed" and isinstance(event.get("error"), dict):
            message = str(event["error"].get("message") or message)
    return message


def _codex(prompt: str, schema: dict | None) -> tuple[dict, dict]:
    with tempfile.TemporaryDirectory(prefix="dependency-shadow-codex-") as tmp:
        tmp_path = Path(tmp)
        out_path = tmp_path / "last-message.json"
        args = [CODEX_BIN, "exec", *(["--model", CODEX_MODEL] if CODEX_MODEL else []),
                "-c", f'model_reasoning_effort="{CODEX_EFFORT}"',
                "--sandbox", "read-only", "--skip-git-repo-check", "--ephemeral",
                "--color", "never", "--json", "--output-last-message", str(out_path)]
        if schema is not None:
            schema_path = tmp_path / "schema.json"
            schema_path.write_text(json.dumps(schema, ensure_ascii=False), encoding="utf-8")
            args += ["--output-schema", str(schema_path)]
        proc = subprocess.run(args + ["-"], input="[cron]\n\n" + prompt, cwd=tmp,
                              capture_output=True, text=True, timeout=TIMEOUT)
        if proc.returncode:
            detail = proc.stderr.strip() or _codex_failure(proc.stdout)
            raise ModelError(f"Codex exited {proc.returncode}: {detail[:400]}")
        if not out_path.exists():
            raise ModelError("Codex produced no last-message file")
        usage: dict = {}
        for line in proc.stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(event, dict) and isinstance(event.get("usage"), dict):
                usage = dict(event["usage"])
        global LAST_RAW
        LAST_RAW = out_path.read_text(encoding="utf-8")
        return parse_model_json(LAST_RAW), usage


def call(stage: str, prompt: str, schema: dict | None = None) -> tuple[dict, dict]:
    """One call to the stage's model, holding one of its measured slots."""
    if len(prompt.encode("utf-8")) > MAX_PROMPT_BYTES:
        raise ModelError(f"prompt exceeds {MAX_PROMPT_BYTES} bytes")
    provider = PROVIDER[stage]
    slot = dc.acquire_provider_slot(provider)
    try:
        if not dc.provider_available(provider):
            raise ModelError(f"{provider} quota gate closed while waiting for a slot")
        if stage == "S1":
            return _agy(prompt)
        if stage == "S2":
            return _claude(prompt)
        return _codex(prompt, schema)
    finally:
        slot.close()
