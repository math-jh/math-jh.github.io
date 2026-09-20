#!/usr/bin/env python3
"""link_pair_llm — 결정론으로 못 지은 KO/EN 링크 대응을 모델에게 묻는다.

link_pairing 이 증명되는 대응만 쓰고 남긴 것은 대부분 "같은 대상으로 가는 링크가
양쪽에 같은 개수로 있는데 어느 것이 어느 것인지는 순서로만 갈리는" 경우다.
순서는 번역이 바꿀 수 있으므로 기계가 정하면 안 되고("A의 1번 결과가 아니라
2번" → "first result of A, not the second"), 문장을 읽어야 정해진다.

모델에게 본문을 붙여 넣지 않고 **파일 경로와 줄번호만** 준다. 이유가 둘이다.
첫째, 발췌를 뜨면 모델이 보는 것과 파일의 그 자리가 어긋날 수 있다. 둘째,
모델이 파일을 열면 결정론 단계가 이미 써 둔 lid 들이 같이 보여서, 그 대응이
잘못돼 있고 그것이 지금 묻는 링크를 잡아먹고 있는 경우를 모델이 짚을 수 있다.
그 지적은 `problems` 로 받아 사람이 본다.

모델은 판단만 하고 **파일은 이 스크립트가 쓴다**. 후보는 같은 정규화 키를 가진
KO 링크로만 제시하므로 모델이 다른 글로 가는 링크를 잘못 붙일 수 없고, 반환된
lid 는 제시한 후보 집합 안에 있어야 하며 한 번씩만 쓸 수 있다.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "dependency-classifier"))
sys.path.insert(0, str(ROOT / "scripts" / "lib"))
import link_ids as L  # noqa: E402
import link_pairing as P  # noqa: E402
from blog_file_lock import try_acquire_file_locks  # noqa: E402
from cron_commit import commit_outputs  # noqa: E402

depc = L.depc
STATE = Path.home() / ".local" / "state" / "link-pairing-llm.json"
AGY_BIN = os.environ.get("DEPENDENCY_AGY_BIN", str(Path.home() / ".gemini/bin/agy"))
AGY_MODEL = os.environ.get("LINK_PAIR_AGY_MODEL", "gemini-3.8-flash-high")
AGY_TIMEOUT = int(os.environ.get("LINK_PAIR_TIMEOUT", "900"))
MAX_ATTEMPTS = 2

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["assignments", "unmatched", "problems"],
    "properties": {
        "assignments": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["en_ref", "lid"],
                "properties": {"en_ref": {"type": "string"},
                               "lid": {"type": "string"}},
            },
        },
        "unmatched": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["en_ref", "why"],
                "properties": {"en_ref": {"type": "string"},
                               "why": {"type": "string"}},
            },
        },
        "problems": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["note"],
                "properties": {"line": {"type": "integer"},
                               "note": {"type": "string"}},
            },
        },
    },
}

PROMPT = """You are matching internal links between a Korean mathematics article \
and its English translation. Read both files yourself; no excerpts are provided.

Korean source : {ko}
English source: {en}

Every link occurrence in the Korean file carries a permanent identifier written \
as `data-lid="xxxxx"` inside its Kramdown IAL. The English file has already \
received that identifier wherever the correspondence could be proven \
mechanically. What is left below could not be: the same target is linked several \
times in one article and only the sentences say which occurrence is which. \
Translation may reorder them, and may merge two Korean links into one English \
link, so an English link legitimately has no counterpart sometimes.

For each English link listed here, decide which Korean occurrence it renders. \
Each one carries a tag like `[e3]`; answer with that tag, because a single line \
can hold several links to the same target and the line number alone would not \
say which of them you mean.

{groups}

Rules:
- Use a `lid` only from the candidate list shown for that same English link.
- Use each `lid` at most once across the whole answer.
- If the English link merges several Korean occurrences, or you cannot tell which \
one it renders, list it under `unmatched` with a short reason. Guessing is worse \
than leaving it: an unmatched link is reviewed by a human, a wrong match is not.
- While reading, you will see `data-lid` values already placed. If one of them \
looks wrong, and especially if a wrong placement is occupying an occurrence that \
one of the links below should have taken, report it under `problems` with the \
line number. Do not try to fix it.

Answer with JSON only."""


def _load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, STATE)


def open_groups(ko_post, en_post):
    """아직 짝이 없는 EN 링크와, 같은 키를 갖는 KO 후보들."""
    ko_text, ko_groups = P._grouped(ko_post)
    en_text, en_groups = P._grouped(en_post)
    taken = set(L.LID_RE.findall(en_text))
    out = []
    counter = 0
    for key, en_links in en_groups.items():
        loose_en = [lk for lk in en_links if P._lid_of(en_text, lk) is None]
        if not loose_en:
            continue
        candidates = []
        for lk in ko_groups.get(key, []):
            lid = P._lid_of(ko_text, lk)
            if lid and lid not in taken:
                candidates.append((lid, lk.line, lk.target))
        if not candidates:
            continue
        # 한 줄에 같은 대상 링크가 여럿일 수 있으므로 줄번호로는 가리킬 수 없다.
        tagged = []
        for lk in loose_en:
            counter += 1
            tagged.append((f"e{counter}", lk))
        out.append((key, tagged, candidates))
    return ko_text, en_text, out


def render_groups(groups) -> str:
    blocks = []
    for key, tagged, candidates in groups:
        lines = [f"Target `{key[0]}` anchor `{key[1] or '(none)'}`:"]
        for ref, lk in tagged:
            lines.append(f"  [{ref}] English link at line {lk.line}  ->  {lk.target}")
        lines.append("  Korean candidates:")
        for lid, line, target in candidates:
            lines.append(f"    lid {lid}  line {line}  {target}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def call_model(ko_post, en_post, groups) -> dict:
    prompt = PROMPT.format(ko=ko_post.path.relative_to(ROOT),
                           en=en_post.path.relative_to(ROOT),
                           groups=render_groups(groups))
    with tempfile.TemporaryDirectory(prefix="link-pair-") as tmp:
        schema_path = Path(tmp) / "schema.json"
        schema_path.write_text(json.dumps(SCHEMA), encoding="utf-8")
        proc = subprocess.run(
            [AGY_BIN, "--print", prompt, "--model", AGY_MODEL,
             "--add-dir", str(ROOT), "--output-format", "json",
             "--json-schema", str(schema_path), "--disable-slash-commands",
             "--print-timeout", "15m"],
            cwd=str(ROOT), stdin=subprocess.DEVNULL,
            capture_output=True, text=True, timeout=AGY_TIMEOUT)
    if proc.returncode != 0:
        raise RuntimeError(f"agy exited {proc.returncode}: {proc.stderr.strip()[:400]}")
    envelope = json.loads(proc.stdout)
    if envelope.get("status") != "SUCCESS":
        raise RuntimeError(f"agy status {envelope.get('status')}: {envelope.get('error', '')}")
    return depc.parse_json_value(str(envelope.get("response", "")))


def validate(answer: dict, groups) -> tuple[list, list[str]]:
    """(EN 링크, lid) 목록과 거절 사유들. 규칙을 어긴 항목만 버린다."""
    by_ref, allowed = {}, {}
    for _key, tagged, candidates in groups:
        for ref, lk in tagged:
            by_ref[ref] = lk
            allowed[ref] = {lid for lid, _l, _t in candidates}
    accepted, refused, used, answered = [], [], set(), set()
    for item in answer.get("assignments", []):
        # 프롬프트가 태그를 `[e3]` 꼴로 보여주므로 대괄호째 돌아오는 것이 자연스럽다.
        ref = str(item.get("en_ref") or "").strip().strip("[]").strip()
        lid = item.get("lid")
        if ref not in by_ref:
            refused.append(f"{ref}: 묻지 않은 링크")
        elif ref in answered:
            refused.append(f"{ref}: 한 링크에 두 번 답함")
        elif lid not in allowed[ref]:
            refused.append(f"{ref}: 후보 밖의 lid {lid}")
        elif lid in used:
            refused.append(f"{ref}: lid {lid} 중복 사용")
        else:
            answered.add(ref)
            used.add(lid)
            accepted.append((by_ref[ref], lid))
    return accepted, refused


def write_pair(en_post, old_text, accepted) -> str | None:
    new = P.apply_copies(old_text, accepted)
    why = P.gate(en_post, old_text, new, accepted)
    if why:
        return why
    lease = try_acquire_file_locks([en_post.path])
    if lease is None:
        return "락 실패"
    try:
        mode = os.stat(en_post.path).st_mode & 0o7777
        fd, tmp = tempfile.mkstemp(prefix=".lid.", suffix=".tmp",
                                   dir=str(en_post.path.parent))
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(new)
        os.chmod(tmp, mode)
        os.replace(tmp, en_post.path)
    finally:
        lease.release()
    return None


DONE_KEY = "_finished"
NOTIFY = Path.home() / ".local" / "bin" / "notify"


def announce_done(state: dict) -> None:
    """백필이 끝났음을 한 번만 알리고 스스로 멈춘다.

    일회성 작업이라 소진된 뒤에도 10분마다 코퍼스를 다시 훑을 이유가 없다.
    알림은 notify 가 유일한 발신 지점이고 실패해도 예외를 올리지 않는다 —
    알림 때문에 워커가 죽으면 안 된다. 상태에 남긴 표시로 재발신을 막는다.
    """
    if state.get(DONE_KEY):
        return
    # 틱마다 도는 회수는 그 틱이 고친 글만 본다. KO 쪽에서 사람이 검토를 마쳐
    # 회수 조건이 성립한 글은 그 경로로 안 잡히므로, 끝낼 때 한 번 전부 훑는다.
    try:
        subprocess.run([sys.executable, str(Path(__file__).with_name(
            "retire_en_reviewed.py")), "--apply"], cwd=str(ROOT), timeout=600)
    except Exception as exc:                           # noqa: BLE001
        print(f"마무리 회수 실패: {exc}")
    pairs = [k for k in state if k != DONE_KEY]
    matched = sum(state[k].get("matched", 0) for k in pairs)
    held = sum(state[k].get("unmatched", 0) for k in pairs)
    refused = sum(len(state[k].get("refused", [])) for k in pairs)
    problems = sum(len(state[k].get("problems", [])) for k in pairs)
    body = (f"{len(pairs)}쌍 처리 · 대응 확정 {matched}건\n"
            f"모델 보류 {held} · 규칙위반 거절 {refused} · 지적 {problems}\n"
            "크론은 스스로 정지했다. 분류기·번역 워커를 재개할 수 있다.")
    state[DONE_KEY] = {"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "matched": matched}
    _save_state(state)
    for command in ([str(NOTIFY), "-s", "링크 대응 백필 완료", "-b", body,
                     "-l", "timeSensitive", "--archive"],
                    [str(Path.home() / ".local" / "bin" / "cron-gate"),
                     "--pause", "blog-link-pairing"]):
        try:
            subprocess.run(command, capture_output=True, timeout=30)
        except Exception as exc:                       # noqa: BLE001
            print(f"완료 처리 실패({command[0]}): {exc}")


def pending_pairs():
    posts = P.sag._posts()
    pairs = [(p, P.sag._counterpart(p, "en")) for p in posts if p.lang == "ko"]
    return [(a, b) for a, b in pairs if b]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-pairs", type=int, default=2)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="한 쌍만: KO 파일 경로 조각")
    args = ap.parse_args()

    if not args.dry_run and not depc.provider_available("Antigravity"):
        print("Antigravity 쿼터 소진 — 이번 틱 건너뜀")
        return 0

    state = _load_state()
    done = 0
    written: list[str] = []
    for ko_post, en_post in pending_pairs():
        if done >= args.max_pairs:
            break
        key = str(ko_post.path.relative_to(ROOT))
        if args.only and args.only not in key:
            continue
        record = state.get(key, {})
        if not args.only and record.get("attempts", 0) >= MAX_ATTEMPTS:
            continue
        ko_text, en_text, groups = open_groups(ko_post, en_post)
        if not groups:
            continue

        asked = sum(len(en_links) for _k, en_links, _c in groups)
        if args.dry_run:
            print(f"\n=== {key} — 물을 링크 {asked}개 ===")
            print(render_groups(groups)[:1500])
            done += 1
            continue

        slot = depc.acquire_provider_slot("Antigravity")
        try:
            answer = call_model(ko_post, en_post, groups)
        except Exception as exc:                       # noqa: BLE001
            record["attempts"] = record.get("attempts", 0) + 1
            record["error"] = str(exc)[:300]
            state[key] = record
            _save_state(state)
            print(f"{key}: 호출 실패 — {exc}")
            done += 1
            continue
        finally:
            slot.close()

        accepted, refused = validate(answer, groups)
        failure = write_pair(en_post, en_text, accepted) if accepted else None
        record = {
            "at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "attempts": record.get("attempts", 0) + 1,
            "asked": asked,
            "matched": 0 if failure else len(accepted),
            "unmatched": len(answer.get("unmatched", [])),
            "refused": refused,
            "problems": answer.get("problems", []),
        }
        if failure:
            record["gate"] = failure
        elif accepted:
            written.append(str(en_post.path.relative_to(ROOT)))
        state[key] = record
        _save_state(state)
        note = f"거절 {len(refused)}" if refused else ""
        print(f"{key}: 물음 {asked} / 확정 {record['matched']} "
              f"/ 모델 보류 {record['unmatched']} {note}"
              + (f" / 게이트 {failure}" if failure else ""))
        done += 1

    if written:
        detail = "\n".join(f"- {path}" for path in written)
        commit_outputs("Link Pairing", written, detail, log=print)
        # 방금 lid 를 채운 EN 링크는 이제 KO 의 완료를 상속할 수 있다. 그 자리에서
        # 마커를 회수해 두면 이 백필이 끝나는 시점에 남는 잔재가 없다.
        subprocess.run([sys.executable, str(Path(__file__).with_name(
            "retire_en_reviewed.py")), "--apply", "--quiet", *written], cwd=str(ROOT))
    if done == 0:
        print("남은 쌍 없음")
        announce_done(state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
