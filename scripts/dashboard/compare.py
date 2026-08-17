#!/usr/bin/env python3
"""판본 비교기(#compare)의 데이터층 — 스냅샷·diff·감사 지적·검토 상태.

서버(server.py)는 라우팅만 하고 내용은 전부 여기서 만든다.

  - 왼쪽 pane  = 스냅샷(`snapshot.py` 가 구워둔 판본의 HTML)
  - 오른쪽 pane = 라이브 dev 서버(4001). 워킹트리를 그대로 비추므로 빌드가 필요 없다.
  - 정렬·마크  = pagediff.py
  - 오른쪽 레일 = notes/audit-2026-08 의 지적 (by-category 가 정본, findings 가 전문)
  - 검토 상태  = ~/.local/state/blog_dashboard_review.json (항목 단위)

검토 상태를 **항목 단위**로 잡는 이유는 이 파일이 다음 작업의 지시서가 되기
때문이다. `글 × 지적 id × 판정 × 메모` 면 나중 세션이 그대로 실행 목록으로 읽는다.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import threading
import time
import urllib.request
from pathlib import Path

import pagediff

ROOT = Path(__file__).resolve().parents[2]
SNAP_ROOT = Path.home() / ".local/state/blog-snapshots"
REVIEW_STATE = Path.home() / ".local/state/blog_dashboard_review.json"
# 범용 비교기가 마지막으로 고른 판본 짝·감사. 대량 sweep 을 검토할 때는 같은 두 판본을
# 며칠씩 오가므로, 새로고침마다 기본값으로 돌아가면 성가시다. 브라우저가 아니라 여기에
# 두는 이유는 메모와 같다 — 맥에서 고른 짝이 아이패드에서도 그대로여야 한다.
COMPARE_PREFS = Path.home() / ".local/state/blog_dashboard_compare.json"
AUDIT_DIR = ROOT / "notes/audit-2026-08"
DEV_ORIGIN = os.environ.get("BLOG_DEV_ORIGIN", "http://127.0.0.1:4001")

VERDICTS = ("ok", "revert", "more", "hold")


# ── 스냅샷 ──────────────────────────────────────────────────────────────────


def snapshots() -> list[dict]:
    out = []
    if SNAP_ROOT.is_dir():
        for d in sorted(SNAP_ROOT.iterdir()):
            m = d / "MANIFEST.json"
            if m.exists():
                try:
                    out.append(json.loads(m.read_text(encoding="utf-8")))
                except ValueError:
                    pass
    out.sort(key=lambda x: x.get("committed", ""), reverse=True)
    return out


def _git(*args: str, timeout: int = 20) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True, text=True, timeout=timeout,
    ).stdout


# ── 임의 ref: 브랜치·태그·sha·HEAD~3 ────────────────────────────────────────
#
# 스냅샷은 sha 로 캐시한다. 브랜치 이름을 그대로 키로 쓰면 브랜치가 움직인 뒤에도
# 옛 빌드를 재사용해 조용히 틀린 판본을 보게 된다.

_SNAP_KEY = re.compile(r"^[0-9a-f]{12}$")


def resolve_ref(ref: str) -> dict | None:
    """ref → {sha, short, subject, committed}. 못 찾으면 None."""
    if not ref or ref == "worktree":
        return {"sha": "", "short": "worktree", "subject": "워킹트리 (지금)",
                "committed": ""}
    if _SNAP_KEY.match(ref) and (SNAP_ROOT / ref / "MANIFEST.json").exists():
        return json.loads((SNAP_ROOT / ref / "MANIFEST.json").read_text(encoding="utf-8"))
    out = _git("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}").strip()
    if not out:
        return None
    info = _git("log", "-1", "--format=%H%x1f%s%x1f%cI", out).strip().split("\x1f")
    if len(info) < 3:
        return None
    return {"sha": info[0], "short": info[0][:12], "subject": info[1], "committed": info[2],
            "ref": ref}


def git_refs(limit: int = 40) -> dict:
    """판본 고르개가 쓰는 목록 — 브랜치·최근 커밋·구워둔 스냅샷."""
    branches = [b.strip().lstrip("* ").strip()
                for b in _git("branch", "--format=%(refname:short)").splitlines()
                if b.strip()]
    commits = []
    for line in _git("log", f"-{limit}", "--format=%H%x1f%s%x1f%cI").splitlines():
        parts = line.split("\x1f")
        if len(parts) == 3:
            commits.append({"sha": parts[0], "short": parts[0][:12],
                            "subject": parts[1], "committed": parts[2]})
    return {"branches": branches, "commits": commits, "snapshots": snapshots()}


# ── 스냅샷 온디맨드 빌드 ────────────────────────────────────────────────────
#
# 한 번에 하나만 굽는다. 이 Pi 는 여유 RAM 이 2GB 남짓이고 빌드가 1.5GB 를 쓰므로
# 두 개가 겹치면 dev 서버(MemoryMax 1.5G)가 먼저 죽는다.

_jobs: dict[str, dict] = {}
_job_lock = threading.Lock()


def snapshot_status(sha12: str) -> dict:
    if (SNAP_ROOT / sha12 / "MANIFEST.json").exists():
        return {"state": "ready", "short": sha12}
    job = _jobs.get(sha12)
    if not job:
        return {"state": "absent", "short": sha12}
    return {k: v for k, v in job.items() if k != "proc"}


def start_snapshot(ref: str) -> dict:
    info = resolve_ref(ref)
    if not info:
        raise ValueError(f"알 수 없는 ref: {ref}")
    short = info["short"]
    if (SNAP_ROOT / short / "MANIFEST.json").exists():
        return {"state": "ready", "short": short, "subject": info.get("subject", "")}
    with _job_lock:
        running = [s for s, j in _jobs.items() if j.get("state") == "running"]
        if running and running[0] != short:
            return {"state": "busy", "short": running[0]}
        if _jobs.get(short, {}).get("state") == "running":
            return snapshot_status(short)
        job = {"state": "running", "short": short, "ref": ref,
               "subject": info.get("subject", ""), "started": time.time()}
        _jobs[short] = job

    def run() -> None:
        try:
            p = subprocess.run(
                ["python3", str(Path(__file__).with_name("snapshot.py")), info["sha"]],
                capture_output=True, text=True, timeout=1800,
            )
            job["state"] = "ready" if p.returncode == 0 else "error"
            job["log"] = (p.stdout + p.stderr)[-2000:]
        except Exception as e:  # noqa: BLE001
            job["state"] = "error"
            job["log"] = str(e)
        job["seconds"] = round(time.time() - job["started"], 1)

    threading.Thread(target=run, daemon=True).start()
    return snapshot_status(short)


def delete_snapshot(sha12: str) -> bool:
    d = SNAP_ROOT / sha12
    if not _SNAP_KEY.match(sha12) or not (d / "MANIFEST.json").exists():
        return False
    shutil.rmtree(d, ignore_errors=True)
    return True


def changed_paths(old_sha: str, new_sha: str = "") -> set[str]:
    """두 판본 사이에 바뀐 글 경로. new 가 비면 워킹트리(커밋 안 된 수정 포함)와 비교."""
    args = ["diff", "--name-only", old_sha] + ([new_sha] if new_sha else []) + ["--", "_posts"]
    return {ln for ln in _git(*args).splitlines() if ln.endswith(".md")}


# ── 감사 지적 ───────────────────────────────────────────────────────────────
#
# by-category/*.md 가 사람이 정리한 정본이다 (항목 id·줄번호·요약·수정안·처리 상태가
# 한 줄에 다 있고, 줄번호는 현재 파일 기준으로 옮겨져 있다). findings/*.md 는 같은
# 항목의 전문이고, applied*/ 는 1·2 차 반영 기록이다.

_H3 = re.compile(r"^###\s+(w[\d.]+)\s+(\S+)\s*(?:\((.*)\))?\s*$")
_ITEM = re.compile(
    r"^-\s+(?P<done>✔\s*)?(?:<span[^>]*>)?"
    r"\*\*(?P<lines>L[^*]+)\*\*\s+`(?P<id>[A-Z]+-\d+)`\s+—\s+(?P<summary>.*)$"
)
_SUB = re.compile(r"^\s+-\s+(?:\*\*)?(수정안|수정함|완료|보류)(?:\*\*)?:\s*(?P<body>.*)$")
_CLEAN = re.compile(r"</?span[^>]*>")

_cache: dict[str, tuple[float, object]] = {}


def _cached(key: str, ttl: float, build):
    now = time.time()
    hit = _cache.get(key)
    if hit and now - hit[0] < ttl:
        return hit[1]
    val = build()
    _cache[key] = (now, val)
    return val


def _parse_by_category() -> dict[str, dict]:
    """key(`Category__basename`) → {items, status, category, w}"""
    index: dict[str, dict] = {}
    bycat = AUDIT_DIR / "by-category"
    if not bycat.is_dir():
        return index
    for f in sorted(bycat.glob("*.md")):
        category = f.stem
        key = None
        cur = None
        for line in f.read_text(encoding="utf-8").splitlines():
            h = _H3.match(line)
            if h:
                key = f"{category}__{h.group(2)}"
                index[key] = {
                    "key": key,
                    "category": category,
                    "w": h.group(1),
                    "status": (h.group(3) or "").strip(),
                    "items": [],
                }
                cur = None
                continue
            if key is None:
                continue
            m = _ITEM.match(line)
            if m:
                cur = {
                    "id": m.group("id"),
                    "lines": _CLEAN.sub("", m.group("lines")).strip(),
                    "summary": _CLEAN.sub("", m.group("summary")).strip(),
                    "fix": "",
                    "resolution": "",
                    "done": bool(m.group("done")),
                }
                index[key]["items"].append(cur)
                continue
            s = _SUB.match(line)
            if s and cur is not None:
                label, body = s.group(1), _CLEAN.sub("", s.group("body")).strip()
                if label == "수정안":
                    cur["fix"] = body
                else:
                    cur["resolution"] = f"{label}: {body}" if body else label
                    cur["done"] = True
    return index


_FM = re.compile(r"^---\s*$", re.M)
# `## BUG-1 (L31, L40, 예시 2) — 수정 제안`
_FINDING_H2 = re.compile(r"^##\s+([A-Z]+-\d+[a-z]?)\s*(?:\(([^)]*)\))?\s*(?:—\s*(.*))?$")


def _parse_findings() -> dict[str, dict]:
    """key → {path, lane, verdict, mechanical, sections:{id: 전문}}"""
    out: dict[str, dict] = {}
    fdir = AUDIT_DIR / "findings"
    if not fdir.is_dir():
        return out
    for f in sorted(fdir.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        parts = _FM.split(text, maxsplit=2)
        meta: dict[str, str] = {}
        body = text
        if len(parts) >= 3:
            body = parts[2]
            for line in parts[1].splitlines():
                m = re.match(r"^([a-z_]+):\s*(.*)$", line)
                if m:
                    meta[m.group(1)] = m.group(2).strip()
        sections: dict[str, str] = {}
        heads: dict[str, dict] = {}
        cur_id, buf = None, []
        for line in body.splitlines():
            h = _FINDING_H2.match(line)
            if h:
                if cur_id:
                    sections[cur_id] = "\n".join(buf).strip()
                cur_id, buf = h.group(1), [line]
                heads[cur_id] = {"lines": (h.group(2) or "").strip(),
                                 "title": (h.group(3) or "").strip(),
                                 "lead": ""}
            elif cur_id:
                buf.append(line)
                if not heads[cur_id]["lead"] and line.strip():
                    heads[cur_id]["lead"] = line.strip()
        if cur_id:
            sections[cur_id] = "\n".join(buf).strip()
        out[f.stem] = {
            "path": meta.get("path", ""),
            "lane": meta.get("lane", ""),
            "verdict": meta.get("verdict", ""),
            "audited": meta.get("audited", ""),
            "mechanical": meta.get("mechanical", ""),
            "sections": sections,
            "heads": heads,
        }
    return out


def _parse_applied() -> dict[str, dict]:
    """key → {id: 반영 요약} — 1 차는 tsv, 2 차는 json."""
    out: dict[str, dict] = {}
    d1 = AUDIT_DIR / "applied"
    if d1.is_dir():
        for f in sorted(d1.glob("*.tsv")):
            items = {}
            for line in f.read_text(encoding="utf-8").splitlines():
                if "\t" in line:
                    i, s = line.split("\t", 1)
                    items[i.strip()] = s.strip()
            out.setdefault(f.stem, {}).update(items)
    d2 = AUDIT_DIR / "applied2"
    if d2.is_dir():
        for f in sorted(d2.glob("*.json")):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except ValueError:
                continue
            items = {
                it.get("id", "?"): f"[{it.get('status', '?')}] {it.get('summary', '')}"
                for it in data.get("items", [])
            }
            out.setdefault(f.stem, {}).update(items)
    return out


def _item_sort(iid: str) -> tuple:
    """`BUG-2` · `STYLE-10` · `QUESTION-2a` 를 종류 → 번호 → 접미사 순으로."""
    m = re.match(r"^([A-Z]+)-(\d+)(.*)$", iid)
    if not m:
        return (iid, 0, "")
    return (m.group(1), int(m.group(2)), m.group(3))


def audit_index() -> dict:
    def build():
        bycat = _parse_by_category()
        findings = _parse_findings()
        applied = _parse_applied()
        keys = set(bycat) | set(findings) | set(applied)
        merged: dict[str, dict] = {}
        for k in keys:
            base = bycat.get(k, {"key": k, "items": [], "status": "", "category": k.split("__")[0], "w": ""})
            fin = findings.get(k, {})
            app = applied.get(k, {})
            items = {it["id"]: dict(it) for it in base["items"]}
            for iid, summary in app.items():
                items.setdefault(iid, {"id": iid, "lines": "", "summary": "", "fix": "",
                                       "resolution": "", "done": True})
                items[iid]["applied"] = summary
                items[iid]["done"] = True
            # by-category 는 **발행 중인 글**만 정리돼 있다. 나머지(report 레인 다수)는
            # 요약이 findings 에만 있으므로 절 머리(줄번호·제목)와 첫 문단으로 채운다.
            # 안 채우면 레일에 id 만 뜬 빈 항목이 남고, 지적↔변경 잇기도 근거를 잃는다.
            for iid, sec in fin.get("sections", {}).items():
                it = items.setdefault(iid, {"id": iid, "lines": "", "summary": "", "fix": "",
                                            "resolution": "", "done": False})
                it["has_detail"] = True
                head = fin.get("heads", {}).get(iid, {})
                if not it["lines"]:
                    it["lines"] = head.get("lines", "")
                if not it["summary"]:
                    lead = head.get("lead", "")
                    title = head.get("title", "")
                    it["summary"] = (f"{title} — {lead}" if title and lead else (lead or title))[:600]
            merged[k] = {
                **base,
                "path": fin.get("path", ""),
                "lane": fin.get("lane", ""),
                "verdict": fin.get("verdict", ""),
                "mechanical": fin.get("mechanical", ""),
                "items": sorted(items.values(), key=lambda x: _item_sort(x["id"])),
            }
        return merged

    return _cached("audit", 60.0, build)


def finding_detail(key: str, item_id: str) -> str:
    fin = _cached("findings", 60.0, _parse_findings)
    return fin.get(key, {}).get("sections", {}).get(item_id, "")


def key_for(relpath: str) -> str:
    """`_posts/Math/<Cat>/ko/<file>.md` → `<Cat>__<file>`"""
    parts = relpath.split("/")
    base = parts[-1][:-3] if parts[-1].endswith(".md") else parts[-1]
    cat = parts[-3] if len(parts) >= 3 and parts[-2] in ("ko", "en") else (parts[-2] if len(parts) >= 2 else "?")
    return f"{cat}__{base}"


# ── 검토 상태 ───────────────────────────────────────────────────────────────


def review_state() -> dict:
    try:
        data = json.loads(REVIEW_STATE.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data.setdefault("items", {})
            data.setdefault("posts", {})
            data.setdefault("notes", [])
            return data
    except (OSError, ValueError):
        pass
    return {"version": 1, "items": {}, "posts": {}, "notes": []}


def review_update(patch: dict) -> dict:
    """항목/글 단위 부분 갱신. 통째 교체가 아니라 병합이다 (동시 편집 손실 방지)."""
    state = review_state()
    now = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    kind = patch.get("kind")
    if kind == "item":
        path, iid = patch.get("path", ""), patch.get("id", "")
        verdict = patch.get("verdict", "")
        if not path or not iid or (verdict and verdict not in VERDICTS):
            raise ValueError("bad item patch")
        k = f"{path}|{iid}"
        if not verdict and not patch.get("note"):
            state["items"].pop(k, None)
        else:
            entry = state["items"].get(k, {})
            if verdict:
                entry["verdict"] = verdict
            if "note" in patch:
                entry["note"] = str(patch["note"])[:2000]
            entry["at"] = now
            state["items"][k] = entry
    elif kind == "post":
        path = patch.get("path", "")
        status = patch.get("status", "")
        if not path or status not in ("done", "open", ""):
            raise ValueError("bad post patch")
        if status in ("", "open"):
            state["posts"].pop(path, None)
        else:
            state["posts"][path] = {"status": status, "at": now}
    elif kind == "note":
        # 임의 위치 메모. 위치는 **줄번호가 아니라 인용문**으로 잡는다 — 마크다운을 열지
        # 않고 말로만 지시할 수 있어야 하고, 줄번호는 다음 수정 한 번에 어긋난다.
        # 인용문 + 절 제목 + 정리 라벨이면 사람도 Claude 도 grep 한 번에 찾는다.
        path = patch.get("path", "")
        text = str(patch.get("text", "")).strip()
        if not path or not text:
            raise ValueError("bad note")
        note = {
            "id": f"n{int(time.time() * 1000) % 10_000_000}",
            "path": path,
            "at": now,
            "side": patch.get("side", "new"),
            "heading": str(patch.get("heading", ""))[:200],
            "label": str(patch.get("label", ""))[:80],
            "quote": str(patch.get("quote", ""))[:400],
            "text": text[:4000],
            "status": "open",
        }
        state["notes"].append(note)
    elif kind == "note-del":
        nid = patch.get("id", "")
        state["notes"] = [n for n in state["notes"] if n.get("id") != nid]
    elif kind == "note-done":
        for n in state["notes"]:
            if n.get("id") == patch.get("id"):
                n["status"] = "done" if patch.get("status") == "done" else "open"
                n["at"] = now
    else:
        raise ValueError("unknown kind")

    REVIEW_STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = REVIEW_STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    os.replace(tmp, REVIEW_STATE)
    return state


# ── 목록 ────────────────────────────────────────────────────────────────────


def prefs() -> dict:
    """마지막으로 고른 판본 짝·감사. 없으면 빈 값."""
    try:
        d = json.loads(COMPARE_PREFS.read_text(encoding="utf-8"))
        if isinstance(d, dict):
            return {k: str(d.get(k, "")) for k in ("old", "new", "audit")}
    except (OSError, ValueError):
        pass
    return {"old": "", "new": "", "audit": ""}


def set_prefs(patch: dict) -> dict:
    cur = prefs()
    for k in ("old", "new", "audit"):
        if k in patch:
            cur[k] = str(patch[k])[:80]
    COMPARE_PREFS.parent.mkdir(parents=True, exist_ok=True)
    tmp = COMPARE_PREFS.with_suffix(".tmp")
    tmp.write_text(json.dumps(cur, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, COMPARE_PREFS)
    return cur


def default_pair(snaps: list[dict]) -> tuple[str, str]:
    """기본 비교 짝 — 스냅샷이 둘 이상이면 **가장 오래된 것 ↔ 가장 최근 것**.

    감사처럼 구간 전체를 훑는 검토에서는 워킹트리가 기준으로 부적절하다. 크론(번역·
    용어 추출·terms-lint)이 30 분마다 커밋해 오른쪽이 검토 중에 움직이고, 그 편집이
    감사 변경과 섞여 보인다. 스냅샷을 양쪽에 두면 검토 대상이 고정된다.
    """
    if not snaps:
        return "", "worktree"
    if len(snaps) == 1:
        return snaps[0]["short"], "worktree"
    return snaps[-1]["short"], snaps[0]["short"]   # snapshots() 는 최신순


def post_list(posts: list[dict], old: str, new: str = "", audit_slug: str = "") -> dict:
    """비교 대상 목록. posts 는 server.scan_posts() 결과.

    audit_slug 를 주면 그 감사(audit.json)의 항목 수를 글마다 얹는다. 안 주면 구
    2026-08 ad-hoc 색인을 쓴다 (감사 전용판이 그 경로를 쓴다).
    """
    audit = audit_index()
    run_items: dict[str, list] = {}
    if audit_slug:
        run_items = {p["path"]: p.get("items", [])
                     for p in audit_run(audit_slug).get("posts", [])}
    state = review_state()
    snaps = snapshots()
    d_old, d_new = default_pair(snaps)
    old = old or d_old
    new = new or d_new
    changed = changed_paths(_snapshot_sha(old),
                            "" if new == "worktree" else _snapshot_sha(new)) if old else set()
    by_path = {p["path"]: p for p in posts}

    rows = []
    for path, p in by_path.items():
        key = key_for(path)
        a = audit.get(key)
        if audit_slug:
            items = run_items.get(path, [])
            if not items and path not in changed:
                continue
            open_items = [i for i in items if i.get("status") == "open"]
        else:
            if not a and path not in changed:
                continue
            items = (a or {}).get("items", [])
            open_items = [i for i in items if not i.get("done")]
        reviewed = sum(1 for i in items if f"{path}|{i['id']}" in state["items"])
        rows.append({
            "path": path,
            "key": key,
            "title": p.get("title", ""),
            "permalink": p.get("permalink", ""),
            "category": p.get("category", ""),
            "lang": p.get("lang", "ko"),
            "weight": p.get("weight"),
            "published": p.get("published", True),
            "changed": path in changed,
            "items": len(items),
            "open": len(open_items),
            "reviewed": reviewed,
            "verdict": (a or {}).get("verdict", ""),
            "lane": (a or {}).get("lane", ""),
            "audit_status": (a or {}).get("status", ""),
            "revising": bool(p.get("revising")),
            "done": state["posts"].get(path, {}).get("status") == "done",
        })
    # 검토를 마친 글은 맨 아래로 — 남은 일이 위에 모인다.
    rows.sort(key=lambda r: (r["done"], not r["changed"], r["category"],
                             r["weight"] if r["weight"] is not None else 1e9))
    return {"posts": rows, "snapshots": snaps, "old": old, "new": new, "counts": {
        "total": len(rows),
        "changed": sum(1 for r in rows if r["changed"]),
        "done": sum(1 for r in rows if r["done"]),
        "revising": sum(1 for r in rows if r["revising"]),
        "needs_user": sum(1 for r in rows if r["verdict"] == "needs_user"),
    }}


# ── diff ────────────────────────────────────────────────────────────────────


def _snapshot_sha(short: str) -> str:
    """스냅샷 디렉토리 이름 → 커밋 sha (MANIFEST 가 정본)."""
    if not short or short == "worktree":
        return "HEAD"
    try:
        return json.loads((SNAP_ROOT / short / "MANIFEST.json").read_text(encoding="utf-8"))["sha"]
    except (OSError, ValueError, KeyError):
        return short


def _snapshot_html(sha12: str, permalink: str) -> str:
    rel = permalink.strip("/")
    path = SNAP_ROOT / sha12 / "html" / f"{rel}.html"
    if not path.exists():
        raise FileNotFoundError(f"스냅샷에 없는 글: {permalink} ({sha12})")
    return path.read_text(encoding="utf-8", errors="replace")


def _live_html(permalink: str) -> str:
    url = DEV_ORIGIN + permalink
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def load_version(version: str, permalink: str) -> str:
    if version == "worktree":
        return _live_html(permalink)
    return _snapshot_html(version, permalink)


def source_diff(path: str, old: str, new: str = "worktree") -> str:
    if not old or old == "worktree":
        return ""
    refs = [_snapshot_sha(old)] + ([] if new == "worktree" else [_snapshot_sha(new)])
    return _git("diff", "--no-color", *refs, "--", path, timeout=30)


# ── 규약 형식의 감사 (audit.json) ───────────────────────────────────────────
#
# 형식·규칙은 scripts/audit/AUDIT-PROTOCOL.md 가 정본이다. 여기서는 읽고 붙이기만 한다.
# 핵심은 **항목 하나 = 블록 하나**이고, 위치를 인용문으로 잡는다는 것 두 가지다.

# 한 감사를 여러 파일로 나눠 내도 된다 — 카테고리별·배치별로 떨어지는 게 자연스럽다.
# 같은 slug 끼리 합쳐 하나로 읽는다 (같은 글이 여러 파일에 나오면 항목을 이어 붙이고
# id 로 중복을 지운다).
AUDIT_JSON_GLOB = "notes/audit-*/audit*.json"
# 인용문 대조용 정규화 — 공백·수식 구분자·강조·링크·인라인 HTML 을 지운다. 마크다운
# 원문과 렌더된 본문 텍스트를 같은 자리에 놓기 위한 최소한의 손질이다.
# (<sub>영문</sub> 병기가 흔해서 태그를 안 지우면 그 문장은 전부 안 맞는다.)
_Q_DROP = re.compile(r"<[^>]+>|\\\(|\\\)|\\\[|\\\]|\$\$|\$|\*|_|`|\]\([^)]*\)|[\[\]]|[­​\s]")
PROBE = 40   # 인용문 전체가 안 맞을 때 쓰는 접두 길이 (한글 40자면 글 안에서 대개 유일)


def norm_quote(s: str) -> str:
    return _Q_DROP.sub("", s or "")


def _audit_files() -> dict[str, list[Path]]:
    """slug → 그 감사를 이루는 파일들. slug 는 **폴더 이름**에서 온다
    (`notes/audit-2026-11/` → `2026-11`). 파일을 열어 보지 않으므로 목록이 싸다."""
    out: dict[str, list[Path]] = {}
    for f in sorted(ROOT.glob(AUDIT_JSON_GLOB)):
        out.setdefault(f.parent.name.replace("audit-", "", 1), []).append(f)
    return out


def audit_runs() -> list[dict]:
    """감사 목록 — 비교기의 감사 고르개가 쓴다."""
    def build():
        out = []
        for slug, files in sorted(_audit_files().items()):
            run = audit_run(slug)
            out.append({
                "slug": slug,
                "title": run.get("title", ""),
                "base_ref": run.get("base_ref", ""),
                "generated_at": run.get("generated_at", ""),
                "posts": len(run.get("posts", [])),
                "items": sum(len(p.get("items", [])) for p in run.get("posts", [])),
                "files": [str(f.relative_to(ROOT)) for f in files],
            })
        return out
    return _cached("audit_runs", 30.0, build)


def audit_run(slug: str) -> dict:
    """감사 하나를 통째로 (여러 파일이면 합쳐서). mtime 을 캐시 키에 넣는다."""
    files = _audit_files().get(slug, [])
    if not files:
        return {}
    key = f"audit_run:{slug}:" + ",".join(str(f.stat().st_mtime_ns) for f in files)

    def build():
        merged: dict = {"slug": slug, "posts": []}
        by_path: dict[str, dict] = {}
        for f in files:
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if d.get("schema", "").split("/")[0] != "blog-audit":
                continue          # 감사 폴더에 든 다른 json 은 무시한다
            for k in ("title", "base_ref", "generated_at", "schema"):
                if not merged.get(k):
                    merged[k] = d.get(k, "")
            for p in d.get("posts", []):
                cur = by_path.get(p["path"])
                if cur is None:
                    by_path[p["path"]] = dict(p)
                    merged["posts"].append(by_path[p["path"]])
                    continue
                seen = {i.get("id") for i in cur.get("items", [])}
                cur["items"] = cur.get("items", []) + [
                    i for i in p.get("items", []) if i.get("id") not in seen]
                cur["verdict"] = cur.get("verdict") or p.get("verdict", "")
        return merged

    return _cached(key, 3600.0, build)


def audit_post(slug: str, path: str) -> dict:
    for p in audit_run(slug).get("posts", []):
        if p.get("path") == path:
            return p
    return {}


def attach_audit(result: dict, items: list[dict]) -> list[dict]:
    """항목을 블록에 앉히고, 그 블록의 변경에 잇는다.

    셋 중 하나로 끝난다:
      - 블록을 찾았고 그 블록에 변경이 있다  → 그 변경에 카드가 붙는다
      - 블록은 찾았는데 변경이 없다          → status:applied 면 **미반영 의심**
      - 블록을 못 찾았다                     → 인용문이 낡았다는 뜻 (unmatched)
    """
    blocks = result.get("blocks", [])
    norm_old = [(b, norm_quote(b["old"])) for b in blocks]
    out = []
    for it in items:
        rec = dict(it)
        rec["hunks"], rec["ops"] = [], []
        q = norm_quote(it.get("quote", ""))
        hits = [b for b, t in norm_old if q and q in t] if q else []
        partial = False
        if q and not hits:
            # 인용문이 블록 경계를 넘거나(원문 한 줄 ⊄ 렌더 블록) 렌더에서 표기가 일부
            # 달라지면 통째로는 안 맞는다. 앞머리로 한 번 더 찾는다.
            probe = q[:PROBE]
            hits = [b for b, t in norm_old if probe in t]
            partial = bool(hits)
        if not hits:
            rec["match"] = "unmatched" if q else "no_quote"
            out.append(rec)
            continue
        rec["ambiguous"] = len(hits) > 1
        rec["partial"] = partial
        blk = hits[0]
        rec["ops"] = [blk["op"]]
        if blk["hunk"]:
            rec["hunks"] = [blk["hunk"]]
            rec["match"] = "linked"
        else:
            rec["match"] = "no_change"
        # was/now 가 있으면 그 블록의 여러 변경 중 하나로 좁히고, after 쪽에 was 가
        # 그대로 남아 있으면 안 고쳐진 것으로 본다.
        was = norm_quote(it.get("was", ""))
        if was and was in norm_quote(blk["new"]):
            rec["still_present"] = True
        if rec["match"] == "no_change" and it.get("status") == "applied":
            rec["suspect"] = "미반영 의심 — 반영했다고 되어 있는데 이 블록에 변경이 없다"
        elif rec.get("still_present") and it.get("status") == "applied":
            rec["suspect"] = "미반영 의심 — 고쳤다는 조각이 아직 그대로 있다"
        out.append(rec)
    return out


# ── 지적 ↔ 변경 잇기 ────────────────────────────────────────────────────────
#
# 감사 지적은 본문 조각을 수식(`$…$`)이나 인용부호로 집어 말한다. 그 조각이 실제로
# 손댄 자리에 나타나면 둘을 잇는다. **정밀도 우선**이다 — 애매하면 잇지 않고
# "지적 없는 변경"으로 남긴다. 근거 없이 이어붙인 지적은 리뷰어를 잘못된 안심으로
# 이끌지만, 안 이어진 변경은 그냥 눈으로 확인할 거리로 남을 뿐이다.

_MATH_SNIP = re.compile(r"\$([^$]{2,200})\$")
_QUOTED = re.compile(r'["“]([^"”]{4,80})["”]')
_MATH_WRAP = re.compile(r"\\[()\[\]]|\$")


def _flatten(s: str) -> str:
    return re.sub(r"\s+", "", _MATH_WRAP.sub("", s or ""))


def link_items(hunks: list[dict], items: list[dict]) -> None:
    sigs = []
    for it in items:
        text = " ".join(x for x in (it.get("summary"), it.get("fix"), it.get("applied")) if x)
        math = {_flatten(m) for m in _MATH_SNIP.findall(text)}
        math = {m for m in math if len(m) >= 3}
        quotes = {q.strip() for q in _QUOTED.findall(text) if len(q.strip()) >= 4}
        sigs.append((it, math, quotes))
        it["hunks"] = []

    for h in hunks:
        touched = h.get("touched") or {}
        flat = _flatten(f"{touched.get('del', '')} {touched.get('ins', '')}")
        scored = []
        for it, math, quotes in sigs:
            best = max((len(s) for s in math if s in flat), default=0)
            best = max(best, max((len(q) for q in quotes if _flatten(q) in flat), default=0))
            if best:
                scored.append((best, it))
        # 긴 조각이 걸린 지적이 더 확실하다. 셋까지만 남긴다 — 짧은 기호 하나로 걸린
        # 지적까지 다 보여주면 근거가 흐려진다.
        scored.sort(key=lambda x: -x[0])
        h["items"] = [it["id"] for _, it in scored[:3]]
        for _, it in scored[:3]:
            it["hunks"].append(h["id"])


def _tag_items(html: str, hunks: list[dict]) -> str:
    """마크에 data-item 을 얹는다 (호버 툴팁이 이걸 읽는다)."""
    for h in hunks:
        if h.get("items"):
            html = html.replace(f'data-h="{h["id"]}"',
                                f'data-h="{h["id"]}" data-item="{" ".join(h["items"])}"')
    return html


def _apply_items(result: dict, items: list[dict]) -> None:
    """항목이 가리키는 변경에 표를 달고(HTML 의 data-item), 연결 수를 센다."""
    by_hunk: dict[int, list[str]] = {}
    for it in items:
        for h in it.get("hunks", []):
            by_hunk.setdefault(h, []).append(it["id"])
    for h in result["hunks"]:
        h["items"] = by_hunk.get(h["id"], [])
    for hid, ids in by_hunk.items():
        for side in ("left", "right"):
            result[side] = result[side].replace(
                f'data-h="{hid}"', f'data-h="{hid}" data-item="{" ".join(ids)}"')
    result["stats"]["linked"] = sum(1 for h in result["hunks"] if h["items"])


def diff(path: str, old: str, new: str, permalink: str, audit_slug: str = "") -> dict:
    old_html = load_version(old, permalink)
    new_html = load_version(new, permalink)
    result = pagediff.diff_articles(old_html, new_html)

    src = source_diff(path, old, new)
    lines = src.splitlines()
    src_hunks = sum(1 for ln in lines if ln.startswith("@@"))
    src_lines = sum(1 for ln in lines
                    if ln[:1] in "+-" and not ln.startswith(("+++", "---")))
    changed = result["stats"]["changed"]
    # 불일치 게이트 — 정렬이 깨졌는지만 본다. 기준은 hunk 수가 아니라 **바뀐 줄 수**다:
    # 원문 한 hunk 가 절 하나를 통째로 덧붙이면 블록은 정당하게 여러 개가 바뀐다(실측
    # 오탐 5건이 전부 그 꼴이었다). 반대로 바뀐 줄보다 바뀐 블록이 많으면 짝이 밀린
    # 것이다. 원문에 변경이 있는데 렌더에 하나도 없는 경우도 같이 잡는다.
    result["source"] = {
        "hunks": src_hunks,
        "lines": src_lines,
        "text": src[:200_000],
        "suspect": bool(src) and (changed > max(8, src_lines) or (src_lines and changed == 0)),
    }

    state = review_state()
    if audit_slug:
        # 규약 형식(audit.json): 인용문으로 블록을 잡고, 그 블록의 변경에 잇는다.
        post = audit_post(audit_slug, path)
        items = attach_audit(result, post.get("items", []))
        _apply_items(result, items)
        result["audit"] = {
            "slug": audit_slug,
            "verdict": post.get("verdict", ""),
            "note": post.get("note", ""),
            "items": items,
            "suspects": [i["id"] for i in items if i.get("suspect")],
            "unmatched": [i["id"] for i in items if i.get("match") == "unmatched"],
        }
    else:
        # 구 경로 — 2026-08 ad-hoc 노트를 그대로 읽는 감사 전용판이 쓴다.
        key = key_for(path)
        audit = audit_index().get(key, {})
        items = []
        for it in audit.get("items", []):
            rk = f"{path}|{it['id']}"
            # 전문을 payload 에 같이 실어 보낸다 — 호버에서 바로 읽혀야 해서 왕복이
            # 없어야 한다. 글 하나치라 몇 KB 다.
            items.append({**it, "review": state["items"].get(rk, {}),
                          "detail": finding_detail(key, it["id"])})
        link_items(result["hunks"], items)
        result["left"] = _tag_items(result["left"], result["hunks"])
        result["right"] = _tag_items(result["right"], result["hunks"])
        result["stats"]["linked"] = sum(1 for h in result["hunks"] if h["items"])
        result["audit"] = {
            "key": key,
            "lane": audit.get("lane", ""),
            "verdict": audit.get("verdict", ""),
            "status": audit.get("status", ""),
            "mechanical": audit.get("mechanical", ""),
            "items": items,
        }
    result["post"] = {"path": path, "permalink": permalink, "old": old, "new": new,
                      "done": state["posts"].get(path, {}).get("status") == "done"}
    result["notes"] = [n for n in state["notes"] if n.get("path") == path]
    return result


# ── Claude 에게 넘길 지시서 ─────────────────────────────────────────────────


def _version_line(label: str, ver: str) -> str:
    info = resolve_ref(ver) if ver else None
    if not info or info["short"] == "worktree":
        return f"- {label}: 워킹트리 (커밋 안 된 지금 상태)"
    when = (info.get("committed") or "")[:16].replace("T", " ")
    return f"- {label}: `{info['short']}` ({when}) {info.get('subject', '')}".rstrip()


def instructions(paths: list[str] | None = None, old: str = "", new: str = "") -> str:
    """메모와 판정을 그대로 붙여 쓸 수 있는 작업 지시서로 만든다.

    위치는 인용문으로 적는다 — 받는 쪽이 마크다운에서 그 문장을 찾으면 되고,
    줄번호처럼 다음 수정 한 번에 어긋나지 않는다.
    """
    state = review_state()
    audit = audit_index()
    notes = [n for n in state["notes"] if n.get("status") != "done"
             and (paths is None or n.get("path") in paths)]
    by_path: dict[str, list] = {}
    for n in notes:
        by_path.setdefault(n["path"], []).append(n)

    # 되돌리기·추가수정 판정도 같이 싣는다 — 승인은 할 일이 없으므로 뺀다.
    for k, v in state["items"].items():
        p, _, iid = k.partition("|")
        if paths is not None and p not in paths:
            continue
        if v.get("verdict") in ("revert", "more"):
            by_path.setdefault(p, []).append({"verdict": v, "id": iid, "path": p})

    if not by_path:
        return ""

    label = {"revert": "되돌릴 것", "more": "추가 수정 필요"}
    old_line, new_line = _version_line("이전", old), _version_line("이후", new)
    old_sha = (resolve_ref(old) or {}).get("short", "") if old else ""
    out = ["# 검토 지시서 (판본 비교기)", "",
           "## 무엇을 보고 쓴 지시인가", "",
           "아래 두 판본을 나란히 놓고 읽으며 적었다.", "",
           old_line, new_line, ""]
    if old_sha and old_sha != "worktree":
        out += [f"필요하면 직접 대조할 수 있다: `git diff {old_sha} -- <파일>`", ""]
    out += ["각 항목의 위치는 **인용문**으로 적혀 있다. 해당 글의 KO 마크다운에서 그 문장을",
            "찾아 고칠 것. 줄번호는 신뢰하지 말 것.",
            "",
            "advisor 는 부르지 말 것. 예외는 하나 — 지시 자체가 수학적으로 의심스러운 주장을",
            "담고 있어 그대로 따르면 글이 틀리게 되는 경우다. 그때만 확인하고, 나머지 지시는",
            "그대로 수행한다.",
            ""]
    for p, entries in sorted(by_path.items()):
        out.append(f"## {p}")
        for e in entries:
            if "text" in e:
                where = " · ".join(x for x in (e.get("heading"), e.get("label")) if x)
                out.append(f"- 위치: {where or '(글 전체)'}")
                if e.get("quote"):
                    out.append(f"  - 인용: “{e['quote']}”")
                out.append(f"  - 지시: {e['text']}")
            else:
                iid = e["id"]
                item = next((i for i in audit.get(key_for(p), {}).get("items", [])
                             if i["id"] == iid), {})
                out.append(f"- 감사 지적 {iid} — {label.get(e['verdict']['verdict'], '')}")
                if item.get("summary"):
                    out.append(f"  - 지적: {item['summary']}")
                if item.get("fix"):
                    out.append(f"  - 수정안: {item['fix']}")
                if e["verdict"].get("note"):
                    out.append(f"  - 내 메모: {e['verdict']['note']}")
        out.append("")

    # 반영이 끝나면 여기 실린 메모는 지운다. 메모는 브라우저가 아니라 이 Pi 에
    # 있으므로(~/.local/state/blog_dashboard_review.json) 세션이 직접 지워 줘야
    # 사용자가 다음 검토를 빈 목록에서 시작한다. **id 로** 지우는 이유는, 지시서를
    # 복사한 뒤에 사용자가 새로 적은 메모까지 날리지 않기 위해서다.
    ids = [n["id"] for n in notes if n.get("id")]
    if ids:
        out += [
            "## 반영을 마친 뒤",
            "",
            "위 지시를 모두 반영했으면 **여기 실린 메모를 지운다.** 메모는 이 Pi 에 있고,",
            "지우지 않으면 다음 검토 때 이미 처리된 지시가 그대로 다시 나온다.",
            "",
            "```",
            "python3 scripts/dashboard/notes_cli.py --del " + " ".join(ids),
            "```",
            "",
            "id 로 지우므로 이 지시서를 만든 뒤에 새로 적힌 메모는 남는다. 반영하지 못하고",
            "남긴 지시가 있으면 그 id 는 빼고 지운다.",
            "",
        ]
    return "\n".join(out)


def macros(version: str) -> str:
    if version == "worktree":
        return (ROOT / "assets/js/katex-macros.js").read_text(encoding="utf-8")
    p = SNAP_ROOT / version / "katex-macros.js"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return (ROOT / "assets/js/katex-macros.js").read_text(encoding="utf-8")
