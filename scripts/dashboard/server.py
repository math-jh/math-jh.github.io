#!/usr/bin/env python3
"""blog_dashboard — preview.math-jh.com/dash/ 의 백엔드.

정적 파일(index.html·dashboard.css·app.js)과 /api/* JSON을 같은 포트에서 낸다.
nginx(4000)의 /dash/ location이 여기로 proxy_pass 한다 — Jekyll을 거치지 않으므로
데이터 갱신이 사이트 rebuild를 유발하지 않는다.

엔드포인트
    GET /api/summary        대시보드 전체 데이터 (45s 캐시)
    GET /api/log?name=<key> 워커 로그 tail (기본 200줄)
    GET /api/lint?path=<p>  단일 글에 md_lint.py CLI 실행 (발행 준비도)

읽기 전용 — 레포에 아무것도 쓰지 않는다.
"""
import json
import os
import re
import subprocess
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
# scripts/dashboard/ 안에 살므로 두 단계 위가 레포 루트다. Jekyll 은 _config 의
# exclude 에 scripts 가 있어 이 디렉토리를 빌드에 포함하지 않는다.
ROOT = os.path.dirname(os.path.dirname(HERE))
STATE = os.path.expanduser("~/.local/state")
QUOTA = os.path.expanduser("~/Projects/hud-display/state/claude_quota.json")
PORT = int(os.environ.get("BLOG_DASH_PORT", "8089"))
CACHE_TTL = 45

# ── 워커 정의 ────────────────────────────────────────────────────────────────
# interval: cron 주기(초). age > 2.5*interval 이면 stale(빨간불) 판정.
WORKERS = [
    dict(key="translation", name="번역 워커", schedule=":15 / :45", interval=1800,
         log=f"{ROOT}/scripts/translation/translation.log"),
    dict(key="terms", name="용어 추출", schedule=":00 / :30", interval=1800,
         log=f"{ROOT}/scripts/term-extraction/term_extract_worker.log"),
    dict(key="terms_lint", name="용어 lint", schedule="매일 04:20", interval=86400,
         log=f"{ROOT}/scripts/term-extraction/term_extraction_lint.log"),
    dict(key="comments", name="댓글 수집", schedule="*/15", interval=900,
         log=f"{ROOT}/scripts/comments/fetch_comments.log"),
    dict(key="link_norm", name="링크 정규화 감사", schedule="매일 04:30", interval=86400,
         log=f"{ROOT}/scripts/audit/link_normalizer.log"),
    dict(key="audit", name="주간 링크 감사", schedule="일 05:00", interval=604800,
         log=f"{ROOT}/scripts/audit/audit.log"),
    dict(key="index_monitor", name="GSC 색인 모니터", schedule="매일 03:00", interval=86400,
         log=f"{ROOT}/scripts/index-monitor/monitor.log"),
    dict(key="blogdev", name="개발 노트 봇", schedule="매일 10:05", interval=86400,
         log=f"{ROOT}/scripts/blogdev-bot/run.log"),
    dict(key="pagefind", name="Pagefind 재색인", schedule="*/30", interval=1800,
         watch=f"{ROOT}/_site/pagefind/pagefind-entry.json"),
]
WORKER_BY_KEY = {w["key"]: w for w in WORKERS}

_cache = {"ts": 0.0, "data": None}


# ── 유틸 ─────────────────────────────────────────────────────────────────────
def tail(path, n=12, maxbytes=200_000):
    try:
        size = os.path.getsize(path)
        with open(path, "rb") as f:
            f.seek(max(0, size - maxbytes))
            raw = f.read()
    except OSError:
        return []
    lines = raw.decode("utf-8", "replace").splitlines()
    return lines[-n:]


def mtime(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return None


def run(cmd, cwd=None, timeout=20):
    try:
        p = subprocess.run(cmd, cwd=cwd, timeout=timeout,
                           capture_output=True, text=True)
        return p.returncode, p.stdout, p.stderr
    except Exception as e:  # timeout·실행불가 전부 여기로
        return -1, "", str(e)


# ── 글 스캔 ──────────────────────────────────────────────────────────────────
_FM_SPLIT = re.compile(r"^---\s*$", re.M)
_SIMPLE_KEYS = ("title", "permalink", "weight", "published", "date",
                "drift_needed", "last_modified_at", "categories")


def parse_post(path):
    """frontmatter 얕은 파싱 — 중첩 키(sidebar 등)는 무시한다."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None
    parts = _FM_SPLIT.split(text, maxsplit=2)
    if len(parts) < 3:
        return None
    fm, body = parts[1], parts[2]
    meta = {}
    for line in fm.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if k in _SIMPLE_KEYS:
            meta[k] = v.strip('"').strip("'")

    rel = os.path.relpath(path, ROOT)
    seg = rel.split(os.sep)[1:-1]        # _posts 와 파일명을 뺀 카테고리 경로
    # Misc/* 는 ko/en 하위 폴더 없이 평평하다 — 단일 언어(ko)로 취급한다.
    if seg and seg[-1] in ("ko", "en"):
        lang, single = seg[-1], False
        seg = seg[:-1]
    else:
        lang, single = "ko", True
    category = "/".join(seg) or "?"
    # 짝 매칭은 날짜 접두사를 뗀 slug 로 한다 — en 파일은 번역 시점 날짜를 달고
    # 생성되므로 ko 와 파일명이 그대로 일치하지 않는다.
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", os.path.basename(path))[:-3]

    try:
        weight = float(meta.get("weight", ""))
    except ValueError:
        weight = None

    # frontmatter의 categories 문자열 — _data/categories.yml subjects 키와 정확히
    # 일치한다(디렉토리명은 하이픈·중첩에서 어긋나므로 순서 매칭엔 이걸 쓴다).
    cat_fm = meta.get("categories", "").strip("[]").split(",")[0].strip().strip('"').strip("'")

    return dict(
        path=rel,
        lang=lang,
        category=category,
        cat_fm=cat_fm,
        title=meta.get("title", os.path.basename(path)),
        permalink=meta.get("permalink", ""),
        weight=weight,
        published=meta.get("published", "true").lower() != "false",
        date=meta.get("date", ""),
        drift=meta.get("drift_needed", "").lower() == "true",
        chars=len(body),
        mtime=mtime(path) or 0,
        single=single,
        slug=slug,
        has_en=single,                   # 실제 짝 매칭은 sec_posts 에서 채운다
    )


_POST_FN = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")


def scan_posts():
    posts = []
    for dirpath, dirnames, filenames in os.walk(f"{ROOT}/_posts"):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if _POST_FN.match(fn):       # CLAUDE.md 등 비-글 파일 제외
                p = parse_post(os.path.join(dirpath, fn))
                if p:
                    posts.append(p)
    return posts


_SUBJECT_KEY = re.compile(r'^  "([^"]+)"\s*:')


def subject_order():
    """_data/categories.yml subjects 블록의 키 순서 → {카테고리 문자열: 순위}.
    키 순서가 곧 사이트 표시 순서다 (그 파일 머리 주석 참조)."""
    order, in_subjects = {}, False
    try:
        with open(f"{ROOT}/_data/categories.yml", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("subjects:"):
                    in_subjects = True
                elif in_subjects:
                    if line[:1] not in (" ", "\n", "#"):
                        break                # 다음 최상위 키
                    m = _SUBJECT_KEY.match(line)
                    if m:
                        order[m.group(1)] = len(order)
    except OSError:
        pass
    return order


# ── 섹션별 수집 ──────────────────────────────────────────────────────────────
def sec_posts(posts):
    now = time.time()
    cutoff30 = time.strftime("%Y-%m-%d", time.localtime(now - 30 * 86400))
    ko = [p for p in posts if p["lang"] == "ko"]
    en = [p for p in posts if p["lang"] == "en"]
    unpub = [p for p in ko if not p["published"]]

    en_index = {(p["category"], p["slug"]) for p in en}
    ko_index = {(p["category"], p["slug"]) for p in ko}
    for p in ko:
        if not p["single"]:
            p["has_en"] = (p["category"], p["slug"]) in en_index
    orphan_en = [dict(path=p["path"], title=p["title"], category=p["category"])
                 for p in en if (p["category"], p["slug"]) not in ko_index]

    cats = {}
    for p in ko:
        c = cats.setdefault(p["category"], [])
        c.append(p)
    sub_order = subject_order()
    categories = []
    for name, items in sorted(cats.items()):
        items.sort(key=lambda p: (p["weight"] is None, p["weight"] if p["weight"] is not None else 0))
        categories.append(dict(
            name=name,
            # categories.yml subjects 키 순서상의 순위. Misc/Peripherals/* 처럼
            # 하위 폴더가 한 키를 공유하면 같은 값 — 클라이언트가 이름으로 tiebreak.
            order=min((sub_order[p["cat_fm"]] for p in items if p["cat_fm"] in sub_order),
                      default=len(sub_order)),
            total=len(items),
            unpublished=sum(1 for p in items if not p["published"]),
            posts=[dict(weight=p["weight"], title=p["title"], published=p["published"],
                        permalink=p["permalink"], path=p["path"], drift=p["drift"],
                        has_en=p["has_en"], chars=p["chars"], mtime=p["mtime"],
                        date=p["date"])
                   for p in items],
        ))

    stats = dict(
        ko=len(ko), en=len(en),
        published=sum(1 for p in ko if p["published"]),
        unpublished=len(unpub),
        categories=len(cats),
        drift=sum(1 for p in ko if p["drift"]),
        # 신규 판정은 frontmatter date 기준 — 자동 커밋이 파일을 상시 건드려
        # mtime 은 "최근 추가"의 신호가 되지 못한다.
        new30d=sum(1 for p in ko if p["date"] >= cutoff30),
        chars=sum(p["chars"] for p in ko),
        missing_en=sum(1 for p in ko if p["published"] and not p["has_en"]),
        orphan_en=len(orphan_en),
    )

    unpub_sorted = sorted(unpub, key=lambda p: p["mtime"], reverse=True)
    return stats, categories, orphan_en, [dict(
        title=p["title"], category=p["category"], weight=p["weight"], path=p["path"],
        permalink=p["permalink"], chars=p["chars"], mtime=p["mtime"], date=p["date"],
        drift=p["drift"], has_en=p["has_en"]) for p in unpub_sorted]


_RUN_TS_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})(?::(\d{2}))?")


def _log_runs(path, now, window=86400):
    """로그의 타임스탬프(local)로 최근 24시간 실행 시각 목록을 만든다.
    분 단위로 dedupe — 한 실행이 여러 줄을 남겨도 틱 하나."""
    seen, out = set(), []
    for ln in tail(path, 2000, maxbytes=500_000):
        m = _RUN_TS_RE.search(ln)
        if not m:
            continue
        try:
            ts = time.mktime((int(m.group(1)), int(m.group(2)), int(m.group(3)),
                              int(m.group(4)), int(m.group(5)), int(m.group(6) or 0),
                              0, 0, -1))
        except Exception:
            continue
        if now - ts > window or ts > now + 3600:
            continue
        key = m.group(0)[:16]
        if key in seen:
            continue
        seen.add(key)
        out.append(int(ts))
    return sorted(out)[-300:]


def sec_workers():
    now = time.time()
    out = []
    for w in WORKERS:
        target = w.get("log") or w.get("watch")
        ts = mtime(target)
        age = None if ts is None else now - ts
        if age is None:
            status = "missing"
        elif age > 2.5 * w["interval"]:
            status = "stale"
        elif age > 1.2 * w["interval"]:
            status = "late"
        else:
            status = "ok"
        # 타임라인용 실측 실행 기록. 타임스탬프 없는 로그(또는 watch 파일)는
        # 마지막 갱신 시각 하나로 폴백한다.
        runs = _log_runs(w["log"], now) if w.get("log") else []
        if not runs and ts is not None and now - ts <= 86400:
            runs = [int(ts)]
        lines = tail(w["log"], 10) if w.get("log") else []
        # errors=0 / error_count: 0 같은 정상 요약줄을 오탐하지 않도록 좁게 잡는다.
        # quota-gate blocked 는 설계된 스킵이지 오류가 아니다.
        err = any(re.search(r"traceback|\bexception\b|\bfail(ed|ure)\b|\berrors?\s*[:=]\s*[1-9]"
                            r"|\berror\b(?!s?\s*[:=]\s*0)", ln, re.I)
                  for ln in lines)
        out.append(dict(key=w["key"], name=w["name"], schedule=w["schedule"],
                        status=status, age=age, last_ts=ts, err=err, tail=lines,
                        runs=runs, has_log=bool(w.get("log"))))
    return out


def _ko_typos(verdict):
    """verify verdict의 KO-TYPOS 섹션에서 실제 지적 항목만 뽑는다.
    '(none detected)' 류 한 줄이나 빈 섹션은 [] 로 취급한다."""
    out, on = [], False
    for ln in str(verdict).splitlines():
        s = ln.strip()
        if s.upper().startswith("KO-TYPOS"):
            on = True
            continue
        if on:
            if s.startswith("- "):
                out.append(s[2:])
            elif not s.startswith("-"):
                break
    return out


def sec_translation():
    p = f"{ROOT}/scripts/translation/translation_state.json"
    try:
        d = json.load(open(p))
    except Exception:
        return None
    files = d.get("files", {})
    by_status = {}
    recent = []
    ko_typos = []
    for path, v in files.items():
        st = v.get("status", "?")
        by_status[st] = by_status.get(st, 0) + 1
        ts = v.get("last_attempt_ts") or 0
        recent.append(dict(path=path, status=st, ts=ts,
                           retries=v.get("retries") or v.get("retry") or 0,
                           verdict=v.get("verdict") or v.get("verify_verdict") or ""))
        typos = _ko_typos(v.get("verdict") or v.get("verify_verdict") or "")
        if typos:
            ko_typos.append(dict(path=path, items=typos,
                                 verified_at=v.get("verified_at") or ""))
    recent.sort(key=lambda r: r["ts"], reverse=True)
    ko_typos.sort(key=lambda r: r["verified_at"], reverse=True)
    return dict(stats=d.get("stats", {}), by_status=by_status,
                recent=recent[:15], ko_typos=ko_typos, state_mtime=mtime(p))


def sec_comments():
    p = f"{ROOT}/_data/recent_comments.yml"
    try:
        text = open(p, encoding="utf-8").read()
    except OSError:
        return None
    # 평탄한 고정 스키마라 yaml 없이 읽는다 (의존성 최소화)
    out = {"ko": [], "en": []}
    lang, cur = None, None
    for line in text.splitlines():
        m = re.match(r"^(ko|en):", line)
        if m:
            lang = m.group(1)
            continue
        if re.match(r"^\s*-\s", line):
            cur = {}
            out.setdefault(lang or "ko", []).append(cur)
        m = re.match(r"^\s*-?\s*(permalink|title|author|updated|anchor):\s*(.*)$", line)
        if m and cur is not None:
            cur[m.group(1)] = m.group(2).strip().strip('"')
    return dict(ko=out.get("ko", []), en=out.get("en", []), mtime=mtime(p))


# audit-report.md의 "### <제목>" → Issue counts 표의 kind 키 매핑
_AUDIT_KIND = {
    "Permalinks that break the convention": "permalink_convention",
    "Internal links pointing nowhere": "internal_link_broken",
    "FIXME / TODO markers left in posts": "fixme_marker",
}


def sec_audit():
    p = f"{ROOT}/scripts/audit/audit-report.md"
    try:
        text = open(p, encoding="utf-8").read()
    except OSError:
        return None
    counts = dict(re.findall(r"^\|\s*`([a-z_]+)`\s*\|\s*(\d+)\s*\|", text, re.M))
    scanned = re.search(r"Total posts scanned:\s*\*\*(\d+)\*\*", text)
    issues = re.search(r"at least one issue:\s*\*\*(\d+)\*\*", text)
    # Actionable items 아래 "### 제목" 블록별 bullet 을 kind 별 상세로 수집
    details = {}
    m = re.search(r"^## Actionable items\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if m:
        for sec in re.finditer(r"^### (.+?)\s*$\n(.*?)(?=^### |\Z)",
                               m.group(1), re.M | re.S):
            kind = _AUDIT_KIND.get(sec.group(1).strip(), sec.group(1).strip())
            details[kind] = [ln[2:].strip() for ln in sec.group(2).splitlines()
                             if ln.startswith("- ")]
    return dict(mtime=mtime(p),
                counts={k: int(v) for k, v in counts.items()},
                details=details,
                scanned=int(scanned.group(1)) if scanned else None,
                posts_with_issues=int(issues.group(1)) if issues else None)


def sec_gsc():
    p = f"{ROOT}/scripts/index-monitor/state-com.json"
    try:
        d = json.load(open(p))
    except Exception:
        return None
    urls = d.get("urls", {})
    today = time.strftime("%Y-%m-%d")
    unindexed, by_coverage = [], {}
    for path, v in urls.items():
        if not isinstance(v, dict):
            continue
        cov = v.get("coverage") or "?"
        by_coverage[cov] = by_coverage.get(cov, 0) + 1
        if v.get("indexed"):
            continue
        snooze = v.get("snooze_until") or ""
        unindexed.append(dict(path=path, coverage=cov, since=v.get("since", ""),
                              checked=v.get("last_checked", ""),
                              snoozed=bool(snooze and snooze > today)))
    unindexed.sort(key=lambda r: (r["snoozed"], r["since"]))
    return dict(mtime=mtime(p), total=len(urls), unindexed=unindexed[:25],
                unindexed_count=len(unindexed), by_coverage=by_coverage,
                actionable=sum(1 for r in unindexed if not r["snoozed"]),
                last_batch=(d.get("last_batch") or {}).get("date"),
                last_full_sweep=d.get("last_full_sweep"))


def sec_git():
    rc, out, _ = run(["git", "log", "-25", "--pretty=format:%h\x1f%ct\x1f%an\x1f%cn\x1f%s"], cwd=ROOT)
    if rc != 0:
        return []
    rows = []
    for line in out.splitlines():
        try:
            sha, ts, author, committer, subject = line.split("\x1f")
        except ValueError:
            continue
        # cron이 올리는 커밋(autopush Auto*·번역 워커·workshop 봇 등)은 git
        # 정체성 체계상 전부 committer=Claude다. 그 외는 수동.
        kind = "auto" if committer == "Claude" else "manual"
        rows.append(dict(sha=sha, ts=int(ts), author=author, subject=subject, kind=kind))
    return rows


def sec_system():
    rc, out, _ = run(["systemctl", "--user", "is-active", "jekyll-blog"], timeout=5)
    jekyll = out.strip() or "unknown"
    mem = tail(f"{STATE}/jekyll-mem.log", 1)
    quota = None
    try:
        q = json.load(open(QUOTA))
        if q.get("ok"):
            quota = dict(weekly=q["weekly"]["utilization"],
                         h5=q["limit5h"]["utilization"], ts=q.get("ts"))
    except Exception:
        pass
    rc, out, _ = run(["git", "status", "--porcelain"], cwd=ROOT)
    dirty = [ln for ln in out.splitlines() if ln.strip()]
    return dict(jekyll=jekyll, mem=mem[0] if mem else "",
                pagefind_mtime=mtime(f"{ROOT}/_site/pagefind/pagefind-entry.json"),
                quota=quota, dirty=dirty[:20], dirty_count=len(dirty))


def build_summary():
    posts = scan_posts()
    stats, categories, orphan_en, unpublished = sec_posts(posts)
    return dict(
        ts=time.time(),
        stats=stats,
        categories=categories,
        orphan_en=orphan_en,
        unpublished=unpublished,
        workers=sec_workers(),
        translation=sec_translation(),
        comments=sec_comments(),
        audit=sec_audit(),
        gsc=sec_gsc(),
        git=sec_git(),
        system=sec_system(),
    )


def summary_cached():
    now = time.time()
    if _cache["data"] is None or now - _cache["ts"] > CACHE_TTL:
        _cache["data"] = build_summary()
        _cache["ts"] = now
    return _cache["data"]


# ── HTTP ────────────────────────────────────────────────────────────────────
STATIC = {"/": ("index.html", "text/html; charset=utf-8"),
          "/index.html": ("index.html", "text/html; charset=utf-8"),
          "/dashboard.css": ("dashboard.css", "text/css; charset=utf-8"),
          "/app.js": ("app.js", "application/javascript; charset=utf-8")}

# 구 상세 경로 — 라우팅은 hash(#workers …)로 넘어갔지만, 북마크된 구 경로에도
# index.html 을 줘야 app.js 가 hash 라우트로 리다이렉트할 수 있다.
# (nginx 가 /dash/ 를 벗겨 보내므로 여기서 보는 경로는 "/workers" 처럼 접두사가 없다.)
SECTIONS = {"workers", "pipeline", "drafts", "weights", "translation", "audit",
            "index", "activity"}


class Handler(BaseHTTPRequestHandler):
    server_version = "blogdash/1.0"

    def log_message(self, fmt, *args):  # 기본 stderr 접근로그 억제
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(body)
        except BrokenPipeError:
            pass

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(u.query)
        path = u.path.rstrip("/") or "/"

        # 파비콘 SVG — 같은 디렉토리의 favicon-*.svg 만 허용
        if re.fullmatch(r"/favicon-[a-z0-9]+\.svg", u.path):
            try:
                with open(os.path.join(HERE, os.path.basename(u.path)), "rb") as f:
                    return self._send(200, f.read(), "image/svg+xml")
            except OSError:
                return self._send(404, "not found", "text/plain; charset=utf-8")

        if path in STATIC or u.path in STATIC or path.lstrip("/") in SECTIONS:
            fn, ctype = (STATIC.get(u.path) or STATIC.get(path)
                         or ("index.html", "text/html; charset=utf-8"))
            try:
                with open(os.path.join(HERE, fn), "rb") as f:
                    return self._send(200, f.read(), ctype)
            except OSError:
                return self._send(404, "not found", "text/plain; charset=utf-8")

        if path == "/api/summary":
            if q.get("fresh"):
                _cache["ts"] = 0
            return self._send(200, json.dumps(summary_cached(), ensure_ascii=False))

        if path == "/api/log":
            key = (q.get("name") or [""])[0]
            w = WORKER_BY_KEY.get(key)
            if not w or not w.get("log"):
                return self._send(404, json.dumps({"error": "unknown worker"}))
            n = min(int((q.get("n") or ["200"])[0] or 200), 2000)
            return self._send(200, json.dumps(
                {"name": w["name"], "path": w["log"], "lines": tail(w["log"], n)},
                ensure_ascii=False))

        if path == "/api/lint":
            rel = (q.get("path") or [""])[0]
            # 경로 탈출 방지: _posts 아래의 .md 만 허용
            full = os.path.normpath(os.path.join(ROOT, rel))
            if not full.startswith(f"{ROOT}/_posts/") or not full.endswith(".md") \
                    or not os.path.exists(full):
                return self._send(400, json.dumps({"error": "bad path"}))
            rc, out, err = run(["python3", f"{ROOT}/.claude/hooks/md_lint.py", full],
                               cwd=ROOT, timeout=60)
            return self._send(200, json.dumps(
                {"path": rel, "rc": rc, "out": out, "err": err}, ensure_ascii=False))

        return self._send(404, "not found", "text/plain; charset=utf-8")


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    srv.daemon_threads = True
    srv.serve_forever()


if __name__ == "__main__":
    main()
