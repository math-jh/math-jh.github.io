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
"""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path

import dependency_classifier as dc

STAGES = ("S1", "S2", "S3")
PROVIDER = {"S1": "Antigravity", "S2": "Claude Opus", "S3": "Codex"}

AGY_BIN = dc.AGY_BIN
AGY_MODEL = dc.AGY_MODEL
AGY_AGENT = os.environ.get("DEPENDENCY_AGY_AGENT", "blog-dependency-judge")
CLAUDE_BIN = dc.CLAUDE_BIN
CLAUDE_MODEL = dc.CLAUDE_MODEL
CODEX_BIN = dc.CODEX_BIN
CODEX_MODEL = dc.CODEX_REVIEW_MODEL
CODEX_EFFORT = dc.CODEX_REVIEW_EFFORT
TIMEOUT = int(os.environ.get("DEPENDENCY_SHADOW_TIMEOUT", "1500"))
CLAUDE_SYSTEM = ("You are a judging engine for the internal links of a mathematics blog. "
                 "Follow the user prompt exactly and return only the requested JSON.")
# 인자 하나의 한도는 페이지 크기의 32배다 (이 Pi 는 16K 페이지라 512 KiB). agy 는
# 프롬프트를 인자로 받으므로 넘기 전에 잘라야 한다 — 여유를 두고 400 KB.
MAX_PROMPT_BYTES = int(os.environ.get("DEPENDENCY_SHADOW_MAX_PROMPT_BYTES", "400000"))


class ModelError(RuntimeError):
    pass


# The last raw response text, kept so a caller can save it when validation drops rows.
LAST_RAW = ""


def available(stage: str) -> bool:
    return dc.provider_available(PROVIDER[stage])


def _agy(prompt: str) -> tuple[dict, dict]:
    proc = subprocess.run(
        [AGY_BIN, "--print", prompt, "--agent", AGY_AGENT, "--model", AGY_MODEL,
         "--output-format", "json", "--disable-slash-commands", "--print-timeout", "20m"],
        cwd="/tmp", stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=TIMEOUT,
    )
    if proc.returncode:
        raise ModelError(f"Antigravity exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    envelope = json.loads(proc.stdout)
    if envelope.get("status") != "SUCCESS":
        raise ModelError(f"Antigravity status {envelope.get('status')}: "
                         f"{str(envelope.get('error', ''))[:300]}")
    usage = dict(envelope.get("usage") or {})
    usage["turns"] = envelope.get("num_turns")
    global LAST_RAW
    LAST_RAW = str(envelope.get("response", ""))
    return dc.parse_json_value(LAST_RAW), usage


def _claude(prompt: str) -> tuple[dict, dict]:
    env = {**os.environ, "CLAUDE_CODE_DISABLE_ADVISOR_TOOL": "1"}
    proc = subprocess.run(
        [CLAUDE_BIN, "-p", "--model", CLAUDE_MODEL, "--tools", "",
         "--system-prompt", CLAUDE_SYSTEM, "--output-format", "json"],
        input="[cron]\n\n" + prompt, cwd="/tmp", env=env,
        capture_output=True, text=True, timeout=TIMEOUT,
    )
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
    return dc.parse_json_value(LAST_RAW), usage


def _codex(prompt: str, schema: dict | None) -> tuple[dict, dict]:
    with tempfile.TemporaryDirectory(prefix="dependency-shadow-codex-") as tmp:
        tmp_path = Path(tmp)
        out_path = tmp_path / "last-message.json"
        args = [CODEX_BIN, "exec", "--model", CODEX_MODEL,
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
            raise ModelError(f"Codex exited {proc.returncode}: {proc.stderr.strip()[:400]}")
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
        return dc.parse_json_value(LAST_RAW), usage


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
