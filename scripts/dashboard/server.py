#!/usr/bin/env python3
"""blog_dashboard — preview.math-jh.com/dash/ 의 백엔드.

정적 파일(index.html·dashboard.css·app.js)과 /api/* JSON을 같은 포트에서 낸다.
nginx(4000)의 /dash/ location이 여기로 proxy_pass 한다 — Jekyll을 거치지 않으므로
데이터 갱신이 사이트 rebuild를 유발하지 않는다.

엔드포인트
    GET /api/summary        대시보드 전체 데이터 (45s 캐시)
    GET /api/log?name=<key> 워커 로그 tail (기본 200줄)
    GET /api/translog?path=<p>  번역 워커 로그에서 그 글의 마지막 시도 구간
    GET /api/heat           개요 수정량 잔디 — KST 날짜별 KO 글 줄 추가·삭제·커밋 수 (전체 기간,
                            git 밖 로컬 글은 LOCAL_GIT 스냅샷으로 함께 센다)
    GET /api/heat/day?d=<날짜>  그날 KO 글을 고친 커밋·로컬 스냅샷과 글
    GET /api/lint?path=<p>  단일 글에 md_lint.py CLI 실행 (발행 준비도)
    GET/POST /api/kotypo    KO-TYPOS '수정' 체크 상태 (전체 map 교체 방식)
    POST /api/kotypo-note   후속 검증 모델에게 전할 메모 (요청 키 단위 병합 저장)
    GET /api/compare/*      판본 비교기 — 목록·diff·감사 지적 전문·판본별 매크로
    POST /api/review        비교기의 검토 판정 (항목 단위 병합 저장)
    GET/POST /api/linkdeps/*  링크 의존성 판정(#audit 아래쪽) — 데이터와 동작은 linkdeps_api.py

링크 의존성 판정은 linkdeps_api 가 `_data/link_relations.yml` 과 ~/.local/state/dependency-classifier 에
쓴다. 그 외의 쓰기는 상태 파일뿐이다:
~/.local/state/blog_dashboard_kotypo.json · …_kotypo_notes.json · …_review.json,
그리고 로컬 글 스냅샷 저장소 blog-dashboard-local-posts.git
(git 밖 KO 글을 2시간마다 커밋 — 원격 없음, 레포의 .git 과 별개).
"""
import fcntl
import glob
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# cron(keeper/@reboot)에서 기동되면 user-session 버스 환경이 없어
# `systemctl --user`가 실패한다 — 기동 경로와 무관하게 동작하도록 보충.
_RUNTIME_DIR = f"/run/user/{os.getuid()}"
os.environ.setdefault("XDG_RUNTIME_DIR", _RUNTIME_DIR)
os.environ.setdefault("DBUS_SESSION_BUS_ADDRESS", f"unix:path={_RUNTIME_DIR}/bus")

HERE = os.path.dirname(os.path.abspath(__file__))
# scripts/dashboard/ 안에 살므로 두 단계 위가 레포 루트다. Jekyll 은 _config 의
# exclude 에 scripts 가 있어 이 디렉토리를 빌드에 포함하지 않는다.
ROOT = os.path.dirname(os.path.dirname(HERE))
STATE = os.path.expanduser("~/.local/state")
KOTYPO_STATE = f"{STATE}/blog_dashboard_kotypo.json"
# 후속 검증 요청에 붙는 사용자 메모. 키는 KOTYPO_STATE 와 같은 `<ko-path>@<ko_reviewed_at>`.
# ko_followup_worker 가 읽어 프롬프트에 넣고 승인 시 지운다 — 쓰기는 양쪽 다 이 flock 으로.
KOTYPO_NOTES = f"{STATE}/blog_dashboard_kotypo_notes.json"
KOTYPO_NOTES_LOCK = f"{KOTYPO_NOTES}.lock"
# ko_followup_worker 가 같은 요청을 이 횟수 이상 연속 WAIT 로 넘기면 행에 '후속 처리 막힘'을
# 띄운다. 근거는 translation_state 의 `ko_followup_wait` = {request, count, at, reason}.
FOLLOWUP_STUCK_AFTER = 2
QUOTA = os.path.expanduser("~/Projects/hud-display/state/claude_quota.json")
PORT = int(os.environ.get("BLOG_DASH_PORT", "8089"))
CACHE_TTL = 45    # 만료 후 첫 요청은 옛 값을 받고 갱신은 백그라운드 (summary_cached)

# preview 의 운영자 댓글 폼(dev 빌드의 Comments.js)이 POST /api/comment/{new,edit,delete} 로
# 부른다. 파일만 바꾸고 커밋하지 않는다 — 작업 트리가 더러우면 blog-autopush 가 다음 실행에서
# 커밋하고 바로 push 한다(cron 커밋 defer 를 타지 않는다). 형식·검증은 add_comment.rb 에만 둔다.
COMMENT_SCRIPT = os.path.join(ROOT, "scripts/comments/add_comment.rb")
COMMENT_OWNER_NAME = "K"
# add_comment.rb·Worker 의 THREAD_RE·COMMENT_ID_RE 와 같다 (service-map contracts.comments-thread-key).
COMMENT_THREAD_RE = re.compile(r"(?:ko|en)__[A-Za-z0-9_-]{1,116}")
COMMENT_ID_RE = re.compile(r"c-\d{8}-[a-f0-9]{6}")


def _touch_thread_page(thread):
    """그 스레드 글의 md mtime 만 올린다(git 에는 잡히지 않는다). 댓글 목록 자체는 조각
    /comments/<키>.html(_plugins/comment_fragments.rb)이라 빌드마다 다시 만들어지지만, 글
    HTML 에 남은 댓글 수와 조각 주소(첫 댓글이면 새로 생긴다)는 dev 서버(--incremental)가
    _data 변경만으로는 다시 렌더하지 않는다 — 고쳐진 글은 새로 읽은 site.data 로 렌더한다."""
    permalink = "/" + thread.replace("__", "/")
    pat = re.compile(r"^permalink:\s*['\"]?" + re.escape(permalink) + r"/?['\"]?\s*$", re.M)
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, "_posts")):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8") as f:
                    head = f.read(4096)
            except OSError:
                continue
            if pat.search(head):
                os.utime(p)

# 색인 요청 추천 순위는 index-monitor 와 **같은 모듈**을 쓴다. 규칙을 여기 복제하면
# inspect_monitor 가 순위를 바꿀 때 대시보드만 조용히 옛 규칙으로 남는다.
sys.path.insert(0, f"{ROOT}/scripts/index-monitor")
try:
    import index_ranking
except Exception:
    index_ranking = None

sys.path.insert(0, f"{ROOT}/scripts/lib")
sys.path.insert(0, f"{ROOT}/scripts/dependency-classifier")

# KO-TYPOS 파싱도 워커와 **같은 모듈**을 쓴다. 복제해 두면 한쪽만 늙는다 —
# 2026-08-15 실측: 대시보드 사본에 legacy fallback 이 없어 워커가 보는 8건 중
# 1건만 보였다. import 가 실패하면 지적을 빈 목록으로 두고(사본을 되살리지 않고)
# 넘어간다.
sys.path.insert(0, f"{ROOT}/scripts/translation")
try:
    from ko_typos import extract_ko_typos as _ko_typos
except Exception:
    def _ko_typos(_verdict):
        return []

# 링크 의존성 판정(감사 페이지 #audit 아래쪽)의 데이터층 — 분류기 파이프라인과 같은 모듈로 읽고 쓴다.
try:
    import linkdeps_api as _linkdeps
except Exception:
    _linkdeps = None

# 판본 비교기(#compare)의 데이터층. bs4 가 없으면 비교기만 죽고 나머지는 그대로 산다.
sys.path.insert(0, HERE)
try:
    import compare as _compare
except Exception as _e:  # noqa: BLE001
    _compare = None
    _compare_err = str(_e)

# ── 워커 정의 ────────────────────────────────────────────────────────────────
# interval: cron 주기(초). age > 2.5*interval 이면 stale(빨간불) 판정.
WORKERS = [
    dict(key="translation", name="번역 워커", schedule="00:15부터 4시간", interval=14400,
         log=f"{ROOT}/scripts/translation/translation.log", log_kind="translation"),
    dict(key="translation_followup", name="한글 수정 후속 워커", schedule="02:15부터 4시간", interval=14400,
         log=f"{ROOT}/scripts/translation/translation.log", log_kind="followup"),
    dict(key="terms", name="용어 추출", schedule="홀수 시각 :15", interval=7200,
         log=f"{ROOT}/scripts/term-extraction/term_extract_worker.log"),
    dict(key="dependency", name="의존성 링크 분류", schedule=":05 / :45", interval=1800,
         log=os.path.expanduser("~/.local/state/dependency-classifier.log")),
    dict(key="terms_lint", name="용어 lint", schedule="매일 04:20", interval=86400,
         log=f"{ROOT}/scripts/term-extraction/term_extraction_lint.log"),
    dict(key="link_norm", name="링크 정규화 감사", schedule="매일 04:30", interval=86400,
         log=f"{ROOT}/scripts/audit/link_normalizer.log"),
    dict(key="audit", name="주간 링크 감사", schedule="일 05:00", interval=604800,
         log=f"{ROOT}/scripts/audit/audit.log"),
    dict(key="index_monitor", name="GSC 색인 모니터", schedule="매일 03:00", interval=86400,
         log=f"{ROOT}/scripts/index-monitor/monitor.log"),
    dict(key="blogdev", name="개발 노트 봇", schedule="매일 10:25", interval=86400,
         log=f"{ROOT}/scripts/blogdev-bot/run.log"),
    dict(key="pagefind", name="Pagefind 재색인", schedule="매일 04:50", interval=86400,
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
                "drift_needed", "last_modified_at", "categories", "revising")


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
        # 개정 중 표시 — CI 의 freeze_revising_posts.py 가 이 글들을 직전 발행 판본으로
        # 되돌려 내보낸다. 즉 프로덕션에 아직 안 나간 수정본이 이것들이다.
        revising=meta.get("revising", "").lower() == "true",
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


def subject_names():
    """_data/categories.yml subjects → {카테고리 문자열: (한국어 이름, 영어 이름)}.
    영어 이름은 키에서 'Math / ' 같은 앞 구간을 뗀 것이다 (블로그 EN 인용 라벨과 같다).
    항목이 블록 꼴과 한 줄 꼴({ ko: …, … })로 섞여 있어 줄 단위가 아니라 YAML 로 읽는다."""
    try:
        import yaml
        with open(f"{ROOT}/_data/categories.yml", encoding="utf-8") as fh:
            subjects = (yaml.safe_load(fh) or {}).get("subjects") or {}
    except Exception:  # noqa: BLE001 — 이름을 못 읽으면 경로에서 딴 이름으로 간다
        return {}
    return {k: ((v or {}).get("ko") or k.split(" / ", 1)[-1], k.split(" / ", 1)[-1])
            for k, v in subjects.items()}


def post_label(p, names):
    """글을 부르는 이름 '[카테고리] 제목' — KO 글은 한국어 과목명, EN 글은 영어 과목명."""
    ko, en = names.get(p["cat_fm"]) or (None, None)
    name = (en if p["lang"] == "en" else ko) or p["category"].split("/")[-1].replace("_", " ")
    return f"[{name}] {p['title']}"


# ── 섹션별 수집 ──────────────────────────────────────────────────────────────
def sec_posts(posts):
    now = time.time()
    cutoff30 = time.strftime("%Y-%m-%d", time.localtime(now - 30 * 86400))
    ko = [p for p in posts if p["lang"] == "ko"]
    en = [p for p in posts if p["lang"] == "en"]
    unpub = [p for p in ko if not p["published"]]
    names = subject_names()
    for p in posts:
        p["label"] = post_label(p, names)

    en_index = {(p["category"], p["slug"]) for p in en}
    ko_index = {(p["category"], p["slug"]) for p in ko}
    for p in ko:
        if not p["single"]:
            p["has_en"] = (p["category"], p["slug"]) in en_index
    orphan_en = [dict(path=p["path"], title=p["title"], category=p["category"], label=p["label"])
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
            posts=[dict(weight=p["weight"], title=p["title"], label=p["label"], published=p["published"],
                        permalink=p["permalink"], path=p["path"], drift=p["drift"],
                        has_en=p["has_en"], chars=p["chars"], mtime=p["mtime"],
                        date=p["date"])
                   for p in items],
        ))

    stats = dict(
        ko=len(ko), en=len(en),
        published=sum(1 for p in ko if p["published"]),
        unpublished=len(unpub),
        # 개정 중은 미발행이 **아니다**. `revising: true` 한 키가 규약이 된
        # 2026-08-17 이후로 이 글들은 발행 글로 세어지고, 프로덕션에는 CI 가
        # 되살린 직전 판본이 떠 있다. 개요는 이 수를 미발행 칸에 덧붙여 낸다.
        revising=sum(1 for p in ko if p["revising"]),
        categories=len(cats),
        # 신규 판정은 frontmatter date 기준 — 자동 커밋이 파일을 상시 건드려
        # mtime 은 "최근 추가"의 신호가 되지 못한다.
        new30d=sum(1 for p in ko if p["date"] >= cutoff30),
        chars=sum(p["chars"] for p in ko),
        missing_en=sum(1 for p in ko if p["published"] and not p["has_en"]),
        orphan_en=len(orphan_en),
    )

    unpub_sorted = sorted(unpub, key=lambda p: p["mtime"], reverse=True)
    return stats, categories, orphan_en, [dict(
        title=p["title"], label=p["label"], category=p["category"], weight=p["weight"], path=p["path"],
        permalink=p["permalink"], chars=p["chars"], mtime=p["mtime"], date=p["date"],
        drift=p["drift"], has_en=p["has_en"]) for p in unpub_sorted]


_RUN_TS_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})(?::(\d{2}))?")


def worker_log_lines(w, n=2000):
    """공유 번역 로그의 후속 접두사와 그 연속 줄을 같은 워커에 귀속한다."""
    lines = tail(w["log"], 20000, maxbytes=2_000_000)
    kind = w.get("log_kind")
    if kind:
        selected = []
        followup = False
        for ln in lines:
            if _RUN_TS_RE.match(ln.lstrip("[")):
                followup = bool(re.match(r"^\[[^]]+\] KO-FOLLOWUP:", ln))
            if followup == (kind == "followup"):
                selected.append(ln)
        lines = selected
    return lines[-n:]


def _log_runs(path, now, window=86400, lines=None):
    """로그의 타임스탬프(local)로 최근 24시간 실행 시각 목록을 만든다.
    분 단위로 dedupe — 한 실행이 여러 줄을 남겨도 틱 하나."""
    seen, out = set(), []
    for ln in (tail(path, 2000, maxbytes=500_000) if lines is None else lines):
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


_ERR_RE = re.compile(r"traceback|\bexception\b|\bfail(ed|ure)\b|\berrors?\s*[:=]\s*[1-9]"
                     r"|\berror\b(?!s?\s*[:=]\s*0)", re.I)

# 모델이 쓴 문장을 그대로 실은 줄. 오류 스캔에서 뺀다 — 번역 검증기의 verdict 전문이
# 같은 로그에 들어오는데, 그 영어 산문에 error·failure 가 흔하다 (2026-08-17 실측:
# "interpretation of gluing failure conveyed identically" 한 줄로 정상 실행이 고장으로
# 떴다). 워커 자신의 상태 줄은 `attempt N/3:` 처럼 시도 횟수를 함께 적으므로 남는다.
_LOG_ECHO_RE = re.compile(r"\bVERIFY \([^)]*\) attempt \d+: ")


def _last_run_lines(path, interval, n=10, lines=None):
    """마지막 실행이 남긴 줄만 돌려준다. 오류 판정 범위를 여기로 좁히면,
    지난 실행에서 난 오류가 로그 꼬리에 남아 있어도 최신 실행이 깨끗하면
    불이 꺼진다.

    실행 경계는 타임스탬프 간격으로 잡는다 — gap 을 넘으면 다른 실행이다.
    타임스탬프 없는 줄(트레이스백 등)은 직전 줄의 실행에 붙으므로, 마지막
    줄 뒤에 붙은 크래시도 잡힌다. 날짜 없는 로그(blogdev-bot·audit)는
    경계를 알 수 없어 마지막 n 줄로 폴백한다."""
    lines = tail(path, 400, maxbytes=500_000) if lines is None else lines
    stamps = []
    for i, ln in enumerate(lines):
        m = _RUN_TS_RE.search(ln)
        if not m:
            continue
        try:
            stamps.append((i, time.mktime(
                (int(m.group(1)), int(m.group(2)), int(m.group(3)),
                 int(m.group(4)), int(m.group(5)), int(m.group(6) or 0), 0, 0, -1))))
        except Exception:
            continue
    if not stamps:
        return lines[-n:]
    # 한 실행 안의 줄 간격(GSC full sweep 은 10 분 넘게 벌어진다)보다는 크고,
    # 실행 사이 간격(=cron 주기)보다는 작아야 한다.
    gap = max(300, interval * 0.25)
    start = stamps[0][0]
    for (i, ts), (_, prev) in zip(stamps[1:], stamps):
        if ts - prev > gap:
            start = i
    return lines[start:]


def sec_workers():
    now = time.time()
    out = []
    # 일시정지된 워커는 로그가 늙는 게 정상이다 — stale 로 불을 켜면 의도된 정지가
    # 고장으로 읽힌다. 프런트가 그 구분을 할 수 있게 정지 상태를 같이 실어 보낸다.
    # 번역과 한글 수정 후속은 별도 worker 키로 각각의 hold를 판정한다.
    cron_by_worker = {}
    for job in sec_cron()["items"]:
        if job.get("worker"):
            cron_by_worker.setdefault(job["worker"], []).append(job)
    for w in WORKERS:
        target = w.get("log") or w.get("watch")
        log_lines = worker_log_lines(w) if w.get("log") else []
        ts = mtime(target)
        if w.get("log_kind"):
            stamps = _log_runs(w["log"], now, window=float("inf"), lines=log_lines)
            ts = stamps[-1] if stamps else None
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
        runs = _log_runs(w["log"], now, lines=log_lines) if w.get("log") else []
        if not runs and ts is not None and now - ts <= 86400:
            runs = [int(ts)]
        lines = log_lines[-10:]
        # 표시용 꼬리는 10 줄이지만 오류 판정은 마지막 실행분만 본다.
        # errors=0 / error_count: 0 같은 정상 요약줄을 오탐하지 않도록 좁게 잡는다.
        # quota-gate blocked 는 설계된 스킵이지 오류가 아니다.
        # 모델 출력을 그대로 실은 줄(_LOG_ECHO_RE)은 스캔에서 뺀다.
        err = any(_ERR_RE.search(ln) and not _LOG_ECHO_RE.search(ln)
                  for ln in (_last_run_lines(w["log"], w["interval"], lines=log_lines) if w.get("log") else []))
        schedules = cron_by_worker.get(w["key"], [])
        paused = bool(schedules) and all(p.get("paused") for p in schedules)
        # 기존 단일 cron_id 필드는 유지하되, 실행 가능한 스케줄을 우선 가리킨다.
        p = next((p for p in schedules if not p.get("paused")),
                 schedules[0] if schedules else {})
        # 수동/쿼터 hold가 있으면 로그가 낡거나 마지막 실행에 오류가 남아 있어도
        # 현재 상태는 장애가 아니라 의도된 정지다. 소비자가 paused 필드를 놓쳐도
        # stale/error로 오인하지 않도록 status 자체도 정규화한다.
        if paused:
            status = "paused"
            err = False
        out.append(dict(key=w["key"], name=w["name"], schedule=w["schedule"],
                        status=status, age=age, last_ts=ts, err=err, tail=lines,
                        runs=runs, has_log=bool(w.get("log")),
                        paused=paused, cron_id=p.get("id"), interval=w["interval"]))
    return out


# 번역 큐에서 각 글이 지금 어느 단계에 있는가. state 의 status 는 마지막으로 기록된
# 사건이라 (초안일 때 박힌 draft_skip 이 발행된 뒤에도 남는다) 이 질문에 답하지 못한다.
# 판정은 워커의 `translate_worker.py --queue` (find_next_target 과 같은 단계 조건) 에
# 맡기고 여기서 다시 구현하지 않는다. 한 번에 4~5초 걸리므로 요약 계산을 붙잡지 않게
# 백그라운드에서 돌리고, 글·state·_config.yml 이 바뀌었을 때만 다시 돈다. 첫 계산이
# 끝나기 전에는 None 이다.
TQUEUE_CMD = ["/usr/bin/python3", f"{ROOT}/scripts/translation/translate_worker.py", "--queue"]
_tqueue = {"sig": None, "data": None, "error": None, "running": False}
_tqueue_lock = threading.Lock()


def _tqueue_signature():
    paths = sorted(glob.glob(f"{ROOT}/_posts/Math/*/*/*.md"))
    return (hash(tuple(paths)), max((mtime(p) or 0 for p in paths), default=0),
            mtime(f"{ROOT}/scripts/translation/translation_state.json"),
            mtime(f"{ROOT}/_config.yml"))


def _tqueue_run(sig):
    rc, out, err = run(TQUEUE_CMD, timeout=60)
    try:
        data, error = (json.loads(out), None) if rc == 0 else (None, err.strip()[-300:])
    except ValueError as e:
        data, error = None, f"JSON: {e}"
    with _tqueue_lock:
        # 실패해도 sig 를 기록한다 — 안 그러면 요약 갱신마다 다시 돈다. 직전 집계는 남긴다.
        _tqueue.update(sig=sig, error=error, running=False)
        if data is not None:
            _tqueue["data"] = data


def translation_queue():
    sig = _tqueue_signature()
    with _tqueue_lock:
        if sig != _tqueue["sig"] and not _tqueue["running"]:
            _tqueue["running"] = True
            threading.Thread(target=_tqueue_run, args=(sig,), daemon=True).start()
        return _tqueue["data"], _tqueue["error"]


TRANSLATION_LOG = f"{ROOT}/scripts/translation/translation.log"
_TL_START = re.compile(r"\] translating \([^)]*\): (\S+) → (\S+)")


def translation_attempt_lines(src, limit=400):
    """번역 워커 로그에서 그 글의 마지막 시도 구간 (번역 큐의 최근 시도 상세).

    시도는 `translating (…): <KO 경로> → <EN 경로>` 줄에서 시작해, 그 글의 `committed:`
    줄까지거나 다음 시도·후속 워커(KO-FOLLOWUP)·다른 글을 가리키는 줄 바로 앞까지다. 경로가
    없는 줄(청크 진행 등)은 구간 안에 있으면 그 시도의 줄이다. 시작 줄을 못 찾으면 그 경로가
    들어간 줄의 끝부분을 준다."""
    if not src.startswith("_posts/") or ".." in src:
        return []
    try:
        with open(TRANSLATION_LOG, encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return []
    for i in range(len(lines) - 1, -1, -1):
        m = _TL_START.search(lines[i])
        if m and m.group(1) == src:
            break
    else:
        return [ln for ln in lines if src in ln][-limit:]
    own = (src, m.group(2))
    out = [lines[i]]
    for ln in lines[i + 1:i + limit]:
        if _TL_START.search(ln) or "KO-FOLLOWUP:" in ln:
            break
        if "_posts/" in ln and not any(x in ln for x in own):
            break
        out.append(ln)
        if "] committed:" in ln:
            break
    return out


def sec_translation():
    p = f"{ROOT}/scripts/translation/translation_state.json"
    try:
        d = json.load(open(p))
    except Exception:
        return None
    files = d.get("files", {})
    recent = []
    ko_typos = []
    n_actionable = n_false = n_unreviewed = 0
    try:
        with open(KOTYPO_NOTES, encoding="utf-8") as f:
            notes = json.load(f)
        if not isinstance(notes, dict):
            notes = {}
    except (OSError, ValueError):
        notes = {}
    for path, v in files.items():
        st = v.get("status", "?")
        ts = v.get("last_attempt_ts") or 0
        recent.append(dict(path=path, status=st, ts=ts,
                           retries=v.get("retries") or v.get("retry") or 0,
                           verdict=v.get("verdict") or v.get("verify_verdict") or ""))
        # An explicit empty value means a later review cleared the finding.  Use
        # the legacy verdict parser only for old entries that never had this key;
        # `or` here resurrects dismissed findings from stale verdict prose.
        typos = (v.get("verify_ko_typos") or []) \
            if "verify_ko_typos" in v else _ko_typos(
                v.get("verdict") or v.get("verify_verdict") or "")
        if not typos:
            continue
        # Codex 판정(translate_worker :: review_ko_findings)이 있으면 항목에 붙인다.
        # 판정은 주장 문자열로 맞춘다 — 저장 순서에 기대면 목록이 어긋났을 때
        # 엉뚱한 항목에 VALID 가 붙는다.
        by_claim = {r.get("claim"): r for r in (v.get("verify_ko_typos_review") or [])}
        items = []
        for t in typos:
            r = by_claim.get(t) or {}
            verdict = (r.get("verdict") or "").upper()
            line = r.get("line")
            items.append(dict(text=t, verdict=verdict or None,
                              kind=r.get("kind") or "ERROR",
                              line=line if isinstance(line, int) and line > 0 else None,
                              quote=r.get("quote") or "",
                              issue=r.get("issue") or "",
                              source=r.get("source") or "",
                              why=r.get("why") or "",
                              fix=r.get("recommended_fix") or "",
                              suggested=r.get("suggested_fix") or ""))
            if verdict == "FALSE":
                n_false += 1
            elif verdict:
                n_actionable += 1
            else:
                n_unreviewed += 1
        live = [i for i in items if i["verdict"] != "FALSE"]
        if not live:
            continue
        verified_at = v.get("ko_reviewed_at") or v.get("verified_at") or ""
        request_key = f"{path}@{verified_at}"
        rejected = v.get("ko_followup_rejected_request") == request_key
        note = notes.get(request_key) if isinstance(notes.get(request_key), dict) else {}
        wait = v.get("ko_followup_wait")
        stuck = None
        if isinstance(wait, dict) and wait.get("request") == request_key \
                and int(wait.get("count") or 0) >= FOLLOWUP_STUCK_AFTER:
            stuck = dict(count=int(wait["count"]), at=wait.get("at") or "",
                         reason=wait.get("reason") or "")
        ko_typos.append(dict(
            path=path, items=[i["text"] for i in items], detail=items,
            live=len(live), verified_at=verified_at,
            followup_rejected_at=v.get("ko_followup_rejected_at") if rejected else "",
            followup_rejection=(v.get("ko_followup_rejection_reason") or "")
                               if rejected else "",
            note=note.get("note") or "", note_at=note.get("at") or "",
            followup_stuck=stuck,
        ))
    recent.sort(key=lambda r: r["ts"], reverse=True)
    ko_typos.sort(key=lambda r: r["verified_at"], reverse=True)
    queue, queue_error = translation_queue()
    return dict(stats=d.get("stats", {}), queue=queue, queue_error=queue_error,
                recent=recent[:30], ko_typos=ko_typos,
                ko_typo_actionable=n_actionable, ko_typo_false=n_false,
                ko_typo_unreviewed=n_unreviewed, state_mtime=mtime(p))


def sec_comment_prs():
    """승인 대기 중인 `comment/*` PR을 GitHub에서 직접 센다."""
    rc, out, err = run([
        "/usr/bin/gh", "pr", "list", "--repo", "math-jh/math-jh.github.io",
        "--state", "open", "--limit", "100",
        "--json", "number,title,url,headRefName,createdAt",
    ])
    if rc != 0:
        return dict(count=None, items=[], error=(err or out).strip()[:240])
    try:
        values = json.loads(out)
    except (TypeError, json.JSONDecodeError) as exc:
        return dict(count=None, items=[], error=f"PR JSON 파싱 실패: {exc}")
    items = [
        dict(number=value.get("number"), title=value.get("title", ""),
             url=value.get("url", ""), created_at=value.get("createdAt", ""))
        for value in values if str(value.get("headRefName", "")).startswith("comment/")
    ]
    return dict(count=len(items), items=items, error=None)


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
    # 사이트가 googlebot noindex 로 내는 글(index_ranking.site_noindexed)은 조치 대상이
    # 아니다. 미색인 목록·조치 대상 수·추천에서 빼고, coverage 분포는 따로 센다 —
    # 구글이 태그를 읽었는지는 그 분포가 `Excluded by 'noindex' tag` 로 옮겨 가는지로 안다.
    noindexed = index_ranking.site_noindexed() if index_ranking else (lambda path: False)
    unindexed, by_coverage, by_coverage_noindex = [], {}, {}
    for path, v in urls.items():
        if not isinstance(v, dict):
            continue
        cov = v.get("coverage") or "?"
        if noindexed(path):
            by_coverage_noindex[cov] = by_coverage_noindex.get(cov, 0) + 1
            continue
        by_coverage[cov] = by_coverage.get(cov, 0) + 1
        if v.get("indexed"):
            continue
        snooze = v.get("snooze_until") or ""
        unindexed.append(dict(path=path, coverage=cov, since=v.get("since", ""),
                              checked=v.get("last_checked", ""),
                              snoozed=bool(snooze and snooze > today)))
    unindexed.sort(key=lambda r: (r["snoozed"], r["since"]))

    # 오늘의 색인 요청 추천. 03:00 크론이 이미 오늘치를 뽑아 뒀으면 **그걸** 쓴다
    # (그 배치는 GSC 실측을 거쳤고, 뽑히면서 쿨다운이 걸려 여기서 다시 계산하면
    # 다음 순번이 나온다). 아직 안 돌았거나 어제 것이면 같은 모듈로 직접 고른다.
    # 배치가 뽑힌 뒤에 noindex 설정이 켜졌을 수 있으므로 배치에도 같은 필터를 건다.
    batch = d.get("last_batch") or {}
    rec_paths, rec_src = [], "none"
    if batch.get("date") == today and batch.get("paths"):
        rec_paths, rec_src = [p for p in batch["paths"] if not noindexed(p)], "batch"
    elif index_ranking:
        cands = [k for k, v in urls.items()
                 if isinstance(v, dict) and v.get("indexed") is not True]
        rec_paths = index_ranking.recommend_from_state(urls, cands, today)
        rec_src = "computed"
    recommend = [dict(path=p, coverage=(urls.get(p) or {}).get("coverage"),
                      since=(urls.get(p) or {}).get("since", ""))
                 for p in rec_paths]

    return dict(mtime=mtime(p), total=sum(by_coverage.values()), unindexed=unindexed[:25],
                unindexed_count=len(unindexed), by_coverage=by_coverage,
                by_coverage_noindex=by_coverage_noindex,
                noindex_total=sum(by_coverage_noindex.values()),
                actionable=sum(1 for r in unindexed if not r["snoozed"]),
                last_batch=batch.get("date"),
                last_full_sweep=d.get("last_full_sweep"),
                recommend=recommend, recommend_src=rec_src,
                host="https://math-jh.com")


# ── 수정량 잔디 (개요) ────────────────────────────────────────────────────────
# KO 글이 날마다 얼마나 고쳐졌는지 — 레포 전체 기간, KST 날짜별 git numstat 의 줄 추가+삭제.
# 워커가 쓰는 커밋([Cron]·[Dash])은 뺀다. [Auto] 는 작업 트리를 짝수 정시에 주워 담은
# 사람의 편집이라 센다. 전체 numstat 이 몇 초 걸려 HEAD 가 바뀔 때만 백그라운드로 다시 센다.
_HEAT_SKIP = ("[Cron]", "[Dash]")
_post_labels = {}   # 경로·permalink → '[카테고리] 제목' — build_summary 가 채운다 (날짜 상세에 쓴다)
_heat = {"sig": None, "data": None, "running": False}
_heat_lock = threading.Lock()


def _ko_post(path):
    return path.startswith("_posts/") and path.endswith(".md") and (
        "/ko/" in path or path.startswith("_posts/Misc/"))


def _numstat_path(p):
    """numstat 의 이름 바뀜 표기(`a/{x => y}/b`, `x => y`)에서 새 경로."""
    if " => " not in p:
        return p
    m = re.match(r"(.*)\{(.*) => (.*)\}(.*)", p)
    return m.group(1) + m.group(3) + m.group(4) if m else p.split(" => ")[-1]


def _kst_day(ts):
    return time.strftime("%Y-%m-%d", time.gmtime(int(ts) + 9 * 3600))


def _heat_log(cmd, local):
    """numstat 로그 → (rc, err, {KST 날짜: [커밋…]}). 부모 없는 커밋(첫 커밋)은 세지 않는다 —
    로컬 스냅샷 저장소의 첫 커밋은 그때까지의 글 전체를 담은 기준선이다."""
    rc, out, err = run(cmd, cwd=ROOT, timeout=90)
    days = {}
    if rc != 0:
        return rc, err, days
    cur = None
    for ln in out.splitlines():
        if ln.startswith("@@"):
            sha, ts, parents, subject = ln[2:].split("\t", 3)
            cur = None
            if parents and not subject.startswith(_HEAT_SKIP):
                cur = dict(sha=sha, subject=subject, add=0, dele=0, files=[], day=_kst_day(ts),
                           local=local)
                if local:
                    cur["subject"] = time.strftime("%H:%M", time.gmtime(int(ts) + 9 * 3600)) + " 스냅샷"
                days.setdefault(cur["day"], []).append(cur)
            continue
        if cur is None or not ln.strip():
            continue
        a, d, path = ln.split("\t", 2)
        path = _numstat_path(path)
        if a == "-" or not _ko_post(path):
            continue
        cur["add"] += int(a)
        cur["dele"] += int(d)
        cur["files"].append(path)
    return rc, err, days


def _heat_run(sig):
    fmt = "--format=@@%h%x09%at%x09%P%x09%s"
    rc, err, days = _heat_log(["git", "log", "--no-merges", "--numstat", fmt, "--", "_posts"], False)
    # 로컬 글이 스냅샷에서 빠지는 것(발행돼 git 으로 넘어감·삭제)은 수정이 아니라 --diff-filter=d.
    lrc, lerr, ldays = _heat_log(["git", "--git-dir", LOCAL_GIT, "log", "--numstat",
                                  "--diff-filter=d", fmt], True) if os.path.isdir(LOCAL_GIT) else (0, "", {})
    if rc == 0:
        for k, v in ldays.items():
            days.setdefault(k, []).extend(v)
        days = {k: [c for c in v if c["files"]] for k, v in days.items()}
        days = {k: v for k, v in days.items() if v}
    with _heat_lock:
        _heat.update(sig=sig, running=False,
                     error=err.strip()[-300:] if rc else lerr.strip()[-300:] if lrc else None)
        if rc == 0:
            _heat["data"] = days


def heat_days():
    """({KST 날짜: [커밋…]}, 세는 중, 지문) — 캐시를 바로 주고, 레포 HEAD 나 로컬 스냅샷
    HEAD 가 바뀌었으면 다시 세기를 시작한다."""
    _, head, _ = run(["git", "rev-parse", "HEAD"], cwd=ROOT, timeout=5)
    _, lhead, _ = run(["git", "--git-dir", LOCAL_GIT, "rev-parse", "-q", "--verify", "HEAD"], timeout=5)
    sig = head.strip()[:12] + ":" + lhead.strip()[:12]
    with _heat_lock:
        if sig != _heat["sig"] and not _heat["running"]:
            _heat["running"] = True
            threading.Thread(target=_heat_run, args=(sig,), daemon=True).start()
        return _heat["data"], _heat["running"], _heat["sig"]


# ── 로컬 글 스냅샷 (잔디) ─────────────────────────────────────────────────────
# .git/info/exclude 로 git 에서 빠진 KO 글(비공개 연구 스트림)은 커밋이 없어 잔디에 안 잡힌다.
# 그래서 원격 없는 별도 저장소(LOCAL_GIT, 작업 트리 = 이 레포)에 그 글들만 2시간마다 스냅샷
# 커밋하고 잔디가 그 numstat 을 함께 센다. 공개 글도 autopush 가 2시간마다 주워 담은 차이로
# 세므로 같은 간격이어야 두 쪽이 같은 잣대다. 시각은 KST 짝수 정시 2분 전(…, 21:58, 23:58) —
# 하루의 마지막 스냅샷이 자정 직전이라 밤 편집이 다음 날로 넘어가지 않는다. 대상은 매번
# `git ls-files --others --ignored` 로 다시 뽑으므로 exclude 를 고치면 따라간다. 스냅샷은
# 인덱스를 비우고 대상만 담아 만든 트리라, 대상에서 빠진 글은 그 스냅샷에서 지워진다.
# 의존성 분류기가 로컬 글에 직접 쓰는 링크 식별자(`data-lid`, 커밋이 없어 [Cron] 으로 거를 수
# 없다)는 지운 본문을 저장한다 — 워커 편집이 수정량에 섞이지 않게. 그래서 이 저장소의 판본은
# lid 가 빠진 본문이다.
LOCAL_GIT = f"{STATE}/blog-dashboard-local-posts.git"
LOCAL_EVERY = 2 * 3600
_LOCAL_NAME = re.compile(r"/\d{4}-\d{2}-\d{2}-[^/]+\.md$")
_LOCAL_LID = re.compile(r'\s*data-lid="[^"]*"')
_LOCAL_EMPTY_IAL = re.compile(r"\{:\s*\}")
_local_lock = threading.Lock()


def _lgit(*args, stdin=None):
    cmd = ["git", "-c", "user.name=blog-dashboard", "-c", "user.email=blog-dashboard@localhost",
           "--git-dir", LOCAL_GIT, "--work-tree", ROOT, *args]
    if stdin is None:
        return run(cmd, cwd=ROOT, timeout=60)
    try:
        p = subprocess.run(cmd, cwd=ROOT, input=stdin, capture_output=True, text=True,
                           encoding="utf-8", timeout=60)
        return p.returncode, p.stdout, p.stderr
    except Exception as e:
        return -1, "", str(e)


def local_posts():
    """git 이 무시하는 KO 글 경로 (Syncthing 충돌 사본 제외). 실패하면 None."""
    rc, out, _ = run(["git", "ls-files", "--others", "--ignored", "--exclude-standard", "-z", "--", "_posts"],
                     cwd=ROOT, timeout=30)
    if rc != 0:
        return None
    return sorted(p for p in out.split("\0")
                  if p and _ko_post(p) and _LOCAL_NAME.search(p) and ".sync-conflict-" not in p)


def local_snapshot():
    """로컬 글이 지난 스냅샷과 다르면 새 스냅샷 커밋을 남긴다. 남겼으면 True."""
    with _local_lock:
        files = local_posts()
        if files is None:
            return False
        if not os.path.isdir(LOCAL_GIT) and run(["git", "init", "-q", "--bare", LOCAL_GIT], timeout=30)[0]:
            return False
        entries = []
        for f in files:
            try:
                with open(os.path.join(ROOT, f), encoding="utf-8") as fh:
                    text = _LOCAL_EMPTY_IAL.sub("", _LOCAL_LID.sub("", fh.read()))
            except (OSError, UnicodeDecodeError):
                return False
            rc, blob, _ = _lgit("hash-object", "-w", "--stdin", stdin=text)
            if rc:
                return False
            entries.append(f"100644 {blob.strip()}\t{f}\n")
        if _lgit("read-tree", "--empty")[0] or (
                entries and _lgit("update-index", "--add", "--index-info", stdin="".join(entries))[0]):
            return False
        rc, tree, _ = _lgit("write-tree")
        if rc:
            return False
        rc, head, _ = _lgit("rev-parse", "-q", "--verify", "HEAD")
        head = head.strip() if rc == 0 else ""
        if head and _lgit("rev-parse", "HEAD^{tree}")[1].strip() == tree.strip():
            return False
        rc, sha, _ = _lgit("commit-tree", tree.strip(), *(["-p", head] if head else []),
                           "-m", "스냅샷" if head else "기준선")
        return rc == 0 and _lgit("update-ref", "HEAD", sha.strip())[0] == 0


def _local_loop():
    while True:
        try:
            local_snapshot()
        except Exception as e:   # 스냅샷 한 번이 실패해도 다음 시각에 다시 한다
            print(f"local_snapshot: {e}", file=sys.stderr)
        now = time.time()
        # KST 짝수 정시 = UTC 홀수 정시. 그 2분 전의 다음 시각까지 잔다.
        time.sleep(((now - 3600 + 120) // LOCAL_EVERY + 1) * LOCAL_EVERY + 3600 - 120 - now)


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
    # 미push 커밋. 워커가 자기 산출물을 직접 커밋하고 autopush 가 cron 커밋만
    # 밀려 있으면 최대 7 일 push 를 미루므로, 며칠씩 쌓여 있는 게 정상 상태다.
    # 여기 없으면 "왜 사이트에 안 나오지"의 답이 대시보드에 아예 안 보인다.
    # fetch 는 하지 않는다 — origin/main 은 autopush 가 2 시간마다 갱신한다.
    rc, out, _ = run(["git", "log", "--pretty=%ct", "origin/main..HEAD"], cwd=ROOT)
    unpushed = [int(x) for x in out.split() if x.isdigit()] if rc == 0 else []
    return dict(jekyll=jekyll, mem=mem[0] if mem else "",
                pagefind_mtime=mtime(f"{ROOT}/_site/pagefind/pagefind-entry.json"),
                quota=quota, dirty=dirty[:20], dirty_count=len(dirty),
                unpushed=len(unpushed),
                unpushed_oldest=min(unpushed) if unpushed else None)


# ── cron 제어 ────────────────────────────────────────────────────────────────
# 정지/재개는 crontab 을 고치지 않는다. crontab 에 박힌 cron-gate 가 상태파일
# 하나를 보고 뒤 명령을 돌릴지 말지 정하고, 이 서버는 그 CLI 만 호출한다.
# crontab 은 director/sync_slots/safety_net 이 락 없이 rewrite 하므로 웹에서
# 건드리면 lost update 가 난다 (2026-07-18 번역워커 라인 소실 사고).
CRON_GATE = os.path.expanduser("~/.local/bin/cron-gate")
QUOTA_GOVERNOR = os.path.expanduser("~/.local/bin/quota-reset-watch.py")
# 키가 곧 허용목록이다. 연구 파이프라인(research-*)은 Pi 대시보드(:8088) 소관.
CRON_JOBS = [
    dict(id="blog-translation",      name="번역 워커",        worker="translation"),
    dict(id="blog-translation-followup", name="한글 수정 후속", worker="translation_followup"),
    dict(id="blog-terms",            name="용어 추출",        worker="terms"),
    dict(id="blog-dependency-classifier", name="의존성 링크 분류", worker="dependency"),
    dict(id="blog-terms-lint",       name="용어 lint",        worker="terms_lint"),
    dict(id="blog-terms-deprecated", name="폐기 용어 점검",   worker=None),
    dict(id="blog-devbot",           name="개발 노트 봇",     worker="blogdev"),
    dict(id="blog-links-audit",      name="주간 링크 감사",   worker="audit"),
    dict(id="blog-pagefind",         name="Pagefind 재색인",  worker="pagefind"),
    dict(id="blog-link-normalizer",  name="링크 정규화 감사", worker="link_norm"),
    dict(id="blog-gsc-monitor",      name="GSC 색인 모니터",  worker="index_monitor"),
    dict(id="blog-indexnow",         name="IndexNow 제출",    worker=None),
    dict(id="blog-pr-notify",        name="PR 알림",          worker=None),
    dict(id="blog-dependabot",       name="Dependabot 검토",  worker=None),
    dict(id="blog-worker-health",    name="워커 감시",        worker=None),
    dict(id="timer:blog-autopush",   name="autopush",         worker=None),
]
CRON_IDS = {j["id"] for j in CRON_JOBS}
_cron_cache = {"ts": 0.0, "data": None}


def gate_cli(*args, timeout=15):
    """cron-gate 호출 — 정지 상태를 읽고 쓰는 유일한 경로."""
    try:
        p = subprocess.run([CRON_GATE, *args], capture_output=True, text=True,
                           timeout=timeout)
        return json.loads(p.stdout or "{}")
    except Exception as e:
        return {"ok": False, "error": f"cron-gate 호출 실패: {str(e)[:160]}"}


def sec_cron():
    now = time.time()
    if _cron_cache["data"] is not None and now - _cron_cache["ts"] < 15:
        return _cron_cache["data"]
    rows = {r["id"]: r for r in (gate_cli("--jobs", "--json").get("jobs") or [])}
    out = []
    for j in CRON_JOBS:
        r = rows.get(j["id"])
        out.append(dict(id=j["id"], name=j["name"], worker=j["worker"],
                        schedule=(r or {}).get("schedule", ""),
                        next=(r or {}).get("next", ""),
                        paused=bool(r and r.get("paused")),
                        until=(r or {}).get("until"), by=(r or {}).get("by"),
                        holds=(r or {}).get("holds", []),
                        userPaused=any(h.get("by") == "blog-dash"
                                       for h in (r or {}).get("holds", [])),
                        quotaPaused=bool((r or {}).get("quotaPaused")),
                        # crontab/timers.conf 에서 게이트가 사라지면 버튼이 무의미해진다
                        missing=r is None, timer=j["id"].startswith("timer:")))
    data = dict(items=out, paused=sum(1 for x in out if x["paused"]), billing=billing_routes())
    _cron_cache.update(ts=now, data=data)
    return data


# 크론의 과금 경로(구독·API) — 읽기만 한다. 모드는 Pi 대시보드 #llm 이 판정기 CLI 로 바꾼다
# (service-map claude-credit·gemini-credit, 계약 claude-credit-route·gemini-credit-route).
BILLING_CLI = (("claude", "Claude", os.path.expanduser("~/.local/bin/claude-credit")),
               ("gemini", "Gemini", os.path.expanduser("~/.local/bin/gemini-credit")))


def billing_routes():
    out = []
    for pid, name, cli in BILLING_CLI:
        try:
            p = subprocess.run([cli, "route", "--json"], capture_output=True, text=True, timeout=10)
            r = json.loads(p.stdout or "{}")
        except Exception:  # noqa: BLE001 — 표시만 하므로 모르면 모른다고 보인다
            r = {}
        out.append(dict(provider=pid, name=name, route=r.get("route"), mode=r.get("mode"),
                        reason=r.get("reason")))
    out.append(dict(provider="codex", name="Codex", route="subscription", mode=None,
                    reason="API 미설정"))
    return out


def build_summary():
    posts = scan_posts()
    stats, categories, orphan_en, unpublished = sec_posts(posts)
    translation = sec_translation()
    # 재번역 대기는 워커가 지금 drift 단계에서 집을 글만 센다. drift_needed 표시가
    # 있어도 초안·개정 중인 글은 건너뜀 칸에, EN 이 아직 없는 글은 신규 번역 칸에 있다.
    queue = (translation or {}).get("queue")
    stats["drift"] = len(queue["buckets"]["drift"]) if queue else None
    audit, gsc = sec_audit(), sec_gsc()
    # 글을 부르는 이름('[카테고리] 제목'). KO 글은 categories 의 글마다 label 이 붙어 있으니,
    # 여기는 감사 상세와 색인 추천이 가리키는 EN 글·permalink 만 따로 싣는다.
    by_key = {}
    for p in posts:
        by_key[p["path"]] = p["label"]
        if p["permalink"]:
            by_key[p["permalink"]] = p["label"]
    _post_labels.clear()
    _post_labels.update(by_key)
    refs = {r["path"] for r in (gsc or {}).get("recommend") or []}
    for lines in ((audit or {}).get("details") or {}).values():
        refs.update(ln.split(" — ", 1)[0].replace(" (초안)", "").strip() for ln in lines)
    return dict(
        ts=time.time(),
        stats=stats,
        categories=categories,
        orphan_en=orphan_en,
        unpublished=unpublished,
        labels={k: by_key[k] for k in refs if k in by_key},
        workers=sec_workers(),
        translation=translation,
        comment_prs=sec_comment_prs(),
        audit=audit,
        gsc=gsc,
        git=sec_git(),
        system=sec_system(),
        cron=sec_cron(),
    )


_refresh_lock = threading.Lock()


def _refresh_summary():
    started = time.time()
    try:
        data = build_summary()
    finally:
        _refresh_lock.release()
    # 도는 동안 버튼이 무효화(ts=0)했거나 동기 빌드가 더 새 값을 넣었으면 버린다.
    if 0 < _cache["ts"] < started:
        _cache.update(data=data, ts=started)


def summary_cached():
    """TTL 만료는 옛 값을 바로 주고 백그라운드에서 갱신한다 (stale-while-revalidate).

    요약 계산은 원장이 바뀐 직후 수 초가 걸려, 1분마다 4초 타임아웃으로 찌르는
    pi-health-monitor 가 그 계산을 떠안으면 거짓 "대시보드 중단"이 난다.
    판정·커밋 버튼과 ?fresh 가 ts 를 0 으로 만든 경우만 기다렸다가 새 값을 준다.
    """
    now = time.time()
    if _cache["data"] is None or _cache["ts"] == 0:
        _cache["data"] = build_summary()
        _cache["ts"] = now
    elif now - _cache["ts"] > CACHE_TTL and _refresh_lock.acquire(blocking=False):
        threading.Thread(target=_refresh_summary, daemon=True).start()
    return _cache["data"]


# ── HTTP ────────────────────────────────────────────────────────────────────
STATIC = {"/": ("index.html", "text/html; charset=utf-8"),
          "/index.html": ("index.html", "text/html; charset=utf-8"),
          "/dashboard.css": ("dashboard.css", "text/css; charset=utf-8"),
          "/app.js": ("app.js", "application/javascript; charset=utf-8"),
          # 판본 비교기는 SPA 밖의 독립 문서다 — pane 이 블로그 스타일시트를
          # 통째로 물어야 해서 대시보드 스킨과 한 문서에 둘 수 없다.
          # audit-2026-08.* 는 이번 전수 감사 검토 전용 판이다 (감사 지적 레일·
          # 지적↔변경 잇기가 notes/audit-2026-08 에 묶여 있다). 감사와 무관한
          # 범용 비교기는 compare.* 로 따로 만든다.
          "/audit-2026-08.html": ("audit-2026-08.html", "text/html; charset=utf-8"),
          "/audit-2026-08.css": ("audit-2026-08.css", "text/css; charset=utf-8"),
          "/audit-2026-08.js": ("audit-2026-08.js", "application/javascript; charset=utf-8"),
          # 범용 판본 비교기 (감사와 무관하게 임의 판본을 비교한다)
          "/compare.html": ("compare.html", "text/html; charset=utf-8"),
          "/compare.css": ("compare.css", "text/css; charset=utf-8"),
          "/compare.js": ("compare.js", "application/javascript; charset=utf-8"),
          "/linkdeps.js": ("linkdeps.js", "application/javascript; charset=utf-8"),
          "/linkdeps.css": ("linkdeps.css", "text/css; charset=utf-8")}


# 비교 대상 글의 permalink 를 찾기 위한 얕은 캐시 (frontmatter 스캔은 0.1s 남짓).
_posts_cache = {"ts": 0.0, "by_path": {}, "all": []}


def posts_indexed():
    now = time.time()
    if now - _posts_cache["ts"] > CACHE_TTL:
        allp = scan_posts()
        _posts_cache.update(ts=now, all=allp, by_path={p["path"]: p for p in allp})
    return _posts_cache

# 섹션 경로(/dash/audit …) — 전부 index.html 을 주고 app.js 가 경로를 읽어 그린다.
# workers·pipeline 은 개요에 있어서 app.js 가 /dash/ 로 바꾼다.
# (nginx 가 /dash/ 를 벗겨 보내므로 여기서 보는 경로는 "/audit" 처럼 접두사가 없다.)
SECTIONS = {"workers", "pipeline", "drafts", "weights", "translation", "audit",
            "index", "activity", "cron"}


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

        if path == "/api/kotypo":
            try:
                with open(KOTYPO_STATE, encoding="utf-8") as f:
                    return self._send(200, f.read().strip() or "{}")
            except OSError:
                return self._send(200, "{}")

        if path in ("/api/linkdeps", "/api/linkdeps/link", "/api/linkdeps/pilot"):
            return self._linkdeps_get(path, q)

        if path == "/api/summary":
            if q.get("fresh"):
                _cache["ts"] = 0
            return self._send(200, json.dumps(summary_cached(), ensure_ascii=False))

        if path == "/api/heat":
            days, running, sig = heat_days()
            return self._send(200, json.dumps({
                "today": _kst_day(time.time()), "pending": days is None and running, "sig": sig,
                # [줄 추가, 삭제, git 커밋 수, 그중 로컬 스냅샷 줄 수(추가+삭제)]
                "days": {k: [sum(c["add"] for c in v), sum(c["dele"] for c in v),
                             sum(1 for c in v if not c["local"]),
                             sum(c["add"] + c["dele"] for c in v if c["local"])]
                         for k, v in (days or {}).items()}}))

        if path == "/api/heat/day":
            day = (q.get("d") or [""])[0]
            days, _, _ = heat_days()
            return self._send(200, json.dumps({"day": day, "commits": [
                dict(sha=c["sha"], subject=c["subject"], add=c["add"], dele=c["dele"], local=c["local"],
                     files=[_post_labels.get(f, f.replace("_posts/", "", 1)) for f in c["files"]])
                for c in (days or {}).get(day, [])]}, ensure_ascii=False))

        if path == "/api/translog":
            src = (q.get("path") or [""])[0]
            return self._send(200, json.dumps({"path": src, "lines": translation_attempt_lines(src)},
                                              ensure_ascii=False))

        if path == "/api/log":
            key = (q.get("name") or [""])[0]
            w = WORKER_BY_KEY.get(key)
            if not w or not w.get("log"):
                return self._send(404, json.dumps({"error": "unknown worker"}))
            n = min(int((q.get("n") or ["200"])[0] or 200), 2000)
            return self._send(200, json.dumps(
                {"name": w["name"], "path": w["log"], "lines": worker_log_lines(w, n)},
                ensure_ascii=False))

        if path == "/api/lint":
            rel = (q.get("path") or [""])[0]
            # 경로 탈출 방지: _posts 아래의 .md 만 허용
            full = os.path.normpath(os.path.join(ROOT, rel))
            if not full.startswith(f"{ROOT}/_posts/") or not full.endswith(".md") \
                    or not os.path.exists(full):
                return self._send(400, json.dumps({"error": "bad path"}))
            rc, out, err = run(["python3", f"{ROOT}/.agents/hooks/md_lint.py", full],
                               cwd=ROOT, timeout=60)
            return self._send(200, json.dumps(
                {"path": rel, "rc": rc, "out": out, "err": err}, ensure_ascii=False))

        if path.startswith("/api/compare/"):
            return self._compare(path, q)

        return self._send(404, "not found", "text/plain; charset=utf-8")

    # ── 판본 비교기 ─────────────────────────────────────────────────────
    def _versions(self, old, new):
        """임의 ref(브랜치·sha·HEAD~3)를 스냅샷 키로 바꾼다.

        아직 안 구운 판본이면 409 로 알려서 클라이언트가 빌드를 걸게 한다 —
        요청 하나가 100 초를 붙잡고 있으면 서버가 다른 요청을 못 받는다.
        """
        out = []
        for v in (old, new):
            if v in ("", None):
                out.append("")
                continue
            info = _compare.resolve_ref(v)
            if not info:
                raise ValueError(json.dumps({"error": f"알 수 없는 ref: {v}"},
                                            ensure_ascii=False))
            short = info["short"]
            if short != "worktree" and _compare.snapshot_status(short)["state"] != "ready":
                raise ValueError(json.dumps(
                    {"error": "스냅샷 없음", "need_build": short, "ref": v,
                     "subject": info.get("subject", "")}, ensure_ascii=False))
            out.append(short)
        return out[0], out[1]

    def _compare(self, path, q):
        if _compare is None:
            return self._send(503, json.dumps(
                {"error": f"compare 모듈 로드 실패: {_compare_err}"}, ensure_ascii=False))
        one = lambda k, d="": (q.get(k) or [d])[0]      # noqa: E731

        if path == "/api/compare/list":
            try:
                old, new = self._versions(one("old"), one("new"))
            except ValueError as e:
                return self._send(409, str(e))
            return self._send(200, json.dumps(
                _compare.post_list(posts_indexed()["all"], old, new, one("audit")),
                ensure_ascii=False))

        if path == "/api/compare/refs":
            return self._send(200, json.dumps(_compare.git_refs(), ensure_ascii=False))

        if path == "/api/compare/audits":
            return self._send(200, json.dumps(_compare.audit_runs(), ensure_ascii=False))

        if path == "/api/compare/prefs":
            return self._send(200, json.dumps(_compare.prefs(), ensure_ascii=False))

        if path == "/api/compare/snapshot":
            info = _compare.resolve_ref(one("ref"))
            if not info:
                return self._send(404, json.dumps({"error": "알 수 없는 ref"},
                                                  ensure_ascii=False))
            st = _compare.snapshot_status(info["short"])
            st.update(subject=info.get("subject", ""), committed=info.get("committed", ""))
            return self._send(200, json.dumps(st, ensure_ascii=False))

        if path == "/api/compare/macros":
            ver = one("v", "worktree")
            if not re.fullmatch(r"worktree|[0-9a-f]{7,40}", ver):
                return self._send(400, "bad version", "text/plain; charset=utf-8")
            return self._send(200, _compare.macros(ver),
                              "application/javascript; charset=utf-8")

        if path == "/api/compare/instructions":
            rel = one("path")
            paths = [rel] if rel else None
            # 어느 두 판본을 보고 쓴 지시인지 머리에 박아 준다 — 받는 쪽이 같은 자리를
            # 직접 대조할 수 있어야 한다.
            return self._send(200,
                              _compare.instructions(paths, one("old"), one("new")),
                              "text/plain; charset=utf-8")

        if path == "/api/compare/finding":
            key, iid = one("key"), one("id")
            if not re.fullmatch(r"[\w.-]{1,120}", key or "") \
                    or not re.fullmatch(r"[A-Z]+-\d+[a-z]?", iid or ""):
                return self._send(400, json.dumps({"error": "bad key"}))
            return self._send(200, json.dumps(
                {"key": key, "id": iid, "text": _compare.finding_detail(key, iid)},
                ensure_ascii=False))

        if path == "/api/compare/diff":
            rel = one("path")
            meta = posts_indexed()["by_path"].get(rel)
            if not meta or not meta.get("permalink"):
                return self._send(400, json.dumps({"error": "알 수 없는 글"},
                                                  ensure_ascii=False))
            try:
                old, new = self._versions(one("old"), one("new", "worktree"))
            except ValueError as e:
                return self._send(409, str(e))
            try:
                data = _compare.diff(rel, old, new, meta["permalink"], one("audit"))
            except FileNotFoundError as e:
                return self._send(404, json.dumps({"error": str(e)}, ensure_ascii=False))
            except Exception as e:  # noqa: BLE001
                return self._send(500, json.dumps({"error": f"{type(e).__name__}: {e}"},
                                                  ensure_ascii=False))
            data["post"]["title"] = meta.get("title", "")
            return self._send(200, json.dumps(data, ensure_ascii=False))

        return self._send(404, "not found", "text/plain; charset=utf-8")

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        if path.startswith("/api/linkdeps/"):
            why = self._reject_write()
            if why:
                return self._send(403, json.dumps({"ok": False, "error": why}, ensure_ascii=False))
            return self._linkdeps_post(path)
        if path.startswith("/api/comment/"):
            why = self._reject_write()
            if why:
                return self._send(403, json.dumps({"ok": False, "error": why}, ensure_ascii=False))
            return self._comment_action(path.rsplit("/", 1)[1])
        if path not in ("/api/kotypo", "/api/kotypo-note", "/api/cron/pause", "/api/cron/resume",
                        "/api/cron/force-resume",
                        "/api/review", "/api/compare/snapshot",
                        "/api/compare/snapshot-delete", "/api/compare/prefs"):
            return self._send(404, "not found", "text/plain; charset=utf-8")
        why = self._reject_write()
        if why:
            return self._send(403, json.dumps({"ok": False, "error": why},
                                              ensure_ascii=False))
        if path == "/api/compare/prefs":
            try:
                n = int(self.headers.get("Content-Length") or 0)
                body = json.loads(self.rfile.read(n).decode("utf-8") or "{}") if n else {}
                cur = _compare.set_prefs(body)
            except Exception as e:  # noqa: BLE001
                return self._send(400, json.dumps({"ok": False, "error": str(e)},
                                                  ensure_ascii=False))
            return self._send(200, json.dumps({"ok": True, **cur}, ensure_ascii=False))
        if path.startswith("/api/compare/snapshot"):
            return self._snapshot_action(path)
        if path == "/api/review":
            return self._review()
        if path == "/api/kotypo-note":
            return self._kotypo_note()
        if path != "/api/kotypo":
            return self._cron_action(path)
        # 클라이언트가 전체 map 을 보내 통째로 교체한다 (키 (path@verified_at) → 1).
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 <= n <= 100_000:
                raise ValueError
            data = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            if not isinstance(data, dict) or len(data) > 1000 \
                    or any(not isinstance(k, str) or len(k) > 400 for k in data):
                raise ValueError
        except Exception:
            return self._send(400, json.dumps({"error": "bad body"}))
        clean = {k: 1 for k in data}
        tmp = f"{KOTYPO_STATE}.tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(clean, f, ensure_ascii=False)
        os.replace(tmp, KOTYPO_STATE)
        return self._send(200, json.dumps({"ok": True, "n": len(clean)}))

    # ── 쓰기 경로의 게이트 ───────────────────────────────────────────────
    # 막으려는 건 브라우저 CSRF 다 — 이 대시보드는 Cloudflare Access 뒤에 있고
    # Access 쿠키는 cross-site POST 에도 실린다. 커스텀 헤더까지 요구하면
    # cross-origin 요청은 프리플라이트를 거쳐야 하는데 그건 통과하지 못한다.
    # 반대로 같은 uid 로 127.0.0.1 을 때리는 로컬 프로세스는 막지 않는다 —
    # 그 상황이면 이미 crontab -e 가 되므로 권한 상승이 아니다.
    def _reject_write(self):
        origin = self.headers.get("Origin") or ""
        host = self.headers.get("Host") or ""
        if not origin or not host:
            return "Origin 헤더 없음"
        # 포트를 뺀 호스트명으로 비교한다 — nginx 가 Host 를 `$host:$server_port`
        # 로 넘기는 반면 브라우저 Origin 은 기본 포트를 생략하므로, netloc 을
        # 그대로 비교하면 정상 요청이 전부 막힌다.
        o = urllib.parse.urlsplit("//" + urllib.parse.urlsplit(origin).netloc).hostname
        h = urllib.parse.urlsplit("//" + host).hostname
        if not o or not h or o.lower() != h.lower():
            return "Origin 불일치"
        if "application/json" not in (self.headers.get("Content-Type") or ""):
            return "Content-Type 이 application/json 이 아님"
        if self.headers.get("X-Dash-Action") != "1":
            return "X-Dash-Action 헤더 없음"
        return None

    def _comment_action(self, action):
        """운영자 댓글: add_comment.rb 를 운영자 이름·role 로 불러 댓글 파일을 바꾼다."""
        def fail(code, msg):
            return self._send(code, json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
        if action not in ("new", "edit", "delete"):
            return fail(404, "없는 동작")
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 < n <= 64_000:
                raise ValueError
            b = json.loads(self.rfile.read(n).decode("utf-8"))
            if not isinstance(b, dict):
                raise ValueError
        except Exception:
            return fail(400, "본문이 JSON 이 아니다")
        thread = str(b.get("thread") or "")
        if len(thread) > 120 or not COMMENT_THREAD_RE.fullmatch(thread):
            return fail(400, "잘못된 스레드 키")
        cmd = ["ruby", COMMENT_SCRIPT, "--thread", thread]
        message = str(b.get("message") or "")
        if action == "new":
            reply = str(b.get("replying_to") or "")
            mentions = b.get("mentions") or []
            if not isinstance(mentions, list):
                return fail(400, "mentions 는 목록이어야 한다")
            mentions = [str(m) for m in mentions]
            for cid in ([reply] if reply else []) + mentions:
                if not COMMENT_ID_RE.fullmatch(cid):
                    return fail(400, f"잘못된 댓글 id: {cid[:40]}")
            cmd += ["--message-file", "-", "--name", COMMENT_OWNER_NAME, "--role", "owner"]
            if reply:
                cmd += ["--reply-to", reply]
            for m in mentions:
                cmd += ["--mention", m]
        else:
            cid = str(b.get("id") or "")
            if not COMMENT_ID_RE.fullmatch(cid):
                return fail(400, "잘못된 댓글 id")
            cmd += ["--edit", cid, "--message-file", "-"] if action == "edit" else ["--delete", cid]
        try:
            r = subprocess.run(cmd, input=message, capture_output=True, text=True,
                               timeout=30, cwd=ROOT)
        except Exception as e:  # noqa: BLE001
            return fail(500, f"add_comment.rb 실행 실패: {e!r}")
        if r.returncode != 0:
            lines = r.stderr.strip().splitlines()
            return fail(400, lines[-1] if lines else f"add_comment.rb rc={r.returncode}")
        _touch_thread_page(thread)
        return self._send(200, json.dumps({"ok": True, "result": r.stdout.strip()},
                                          ensure_ascii=False))

    def _linkdeps_get(self, path, q):
        if _linkdeps is None:
            return self._send(503, json.dumps({"ok": False, "error": "linkdeps_api 없음"},
                                              ensure_ascii=False))
        try:
            if path == "/api/linkdeps/link":
                data = _linkdeps.link_detail((q.get("lid") or [""])[0], (q.get("unit") or [""])[0])
            elif path == "/api/linkdeps/pilot":
                data = _linkdeps.pilot()
            else:
                data = _linkdeps.snapshot()
        except KeyError as e:
            return self._send(404, json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        except Exception as e:  # noqa: BLE001
            return self._send(500, json.dumps({"ok": False, "error": repr(e)}, ensure_ascii=False))
        return self._send(200, json.dumps({"ok": True, **data}, ensure_ascii=False))

    def _linkdeps_post(self, path):
        """링크 의존성 판정의 판정 동작. 본문은 JSON, 동작 이름은 경로 끝."""
        if _linkdeps is None:
            return self._send(503, json.dumps({"ok": False, "error": "linkdeps_api 없음"},
                                              ensure_ascii=False))
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 <= n <= 200_000:
                raise ValueError("본문이 너무 크다")
            b = json.loads(self.rfile.read(n).decode("utf-8") or "{}") if n else {}
            action = path.rsplit("/", 1)[1]
            if action == "rule":
                out = _linkdeps.rule(b["lid"], b["relation"], b.get("explanation") or "")
            elif action == "reopen":
                out = _linkdeps.reopen(b["lid"])
            elif action == "audit":
                out = _linkdeps.audit(b["lid"], b["relation"], b.get("explanation") or "")
            elif action == "register":
                out = _linkdeps.register(b["qid"], b.get("explanation") or "")
            elif action == "issue":
                out = _linkdeps.edit_issue(b["id"], b.get("statement"), b.get("description"))
            elif action == "move":
                out = _linkdeps.move(b["lid"], b.get("from"), b.get("to"), b.get("new"))
            elif action == "close":
                out = _linkdeps.close_issue(b["id"], b["action"], b.get("into"))
            elif action == "draft":
                out = _linkdeps.draft(b["id"], b["action"], b.get("edited"), b.get("choice"),
                                    bool(b.get("accept_recheck", True)))
            elif action == "precedent":
                out = _linkdeps.precedent(b["id"], b["action"], b.get("description"))
            elif action == "consolidate":
                out = _linkdeps.consolidate(b["kind"], b.get("ids") or [])
            else:
                return self._send(404, json.dumps({"ok": False, "error": "없는 동작"},
                                                  ensure_ascii=False))
        except _linkdeps.Busy as e:
            return self._send(409, json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        except (KeyError, ValueError) as e:
            return self._send(400, json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        except Exception as e:  # noqa: BLE001
            return self._send(500, json.dumps({"ok": False, "error": repr(e)}, ensure_ascii=False))
        return self._send(200, json.dumps({"ok": True, **out}, ensure_ascii=False))

    def _snapshot_action(self, path):
        """판본 굽기·지우기. 굽기는 백그라운드 스레드라 즉시 돌아온다(진행은 폴링)."""
        if _compare is None:
            return self._send(503, json.dumps({"ok": False, "error": "compare 없음"},
                                              ensure_ascii=False))
        try:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n).decode("utf-8") or "{}") if n else {}
        except Exception:  # noqa: BLE001
            return self._send(400, json.dumps({"ok": False, "error": "bad body"}))
        if path.endswith("snapshot-delete"):
            ok = _compare.delete_snapshot(str(body.get("short", "")))
            return self._send(200 if ok else 400,
                              json.dumps({"ok": ok}, ensure_ascii=False))
        try:
            st = _compare.start_snapshot(str(body.get("ref", "")))
        except ValueError as e:
            return self._send(400, json.dumps({"ok": False, "error": str(e)},
                                              ensure_ascii=False))
        return self._send(200, json.dumps({"ok": True, **st}, ensure_ascii=False))

    def _kotypo_note(self):
        """후속 검증 메모 한 건을 쓰거나(빈 문자열이면) 지운다. 요청 키 단위 병합."""
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 <= n <= 20_000:
                raise ValueError
            body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            key = body.get("key")
            note = body.get("note")
            if not isinstance(key, str) or "@" not in key or len(key) > 400 \
                    or not key.startswith("_posts/") or not isinstance(note, str) \
                    or len(note) > 4000:
                raise ValueError
        except Exception:
            return self._send(400, json.dumps({"ok": False, "error": "bad body"}))
        note = note.strip()
        with open(KOTYPO_NOTES_LOCK, "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            try:
                with open(KOTYPO_NOTES, encoding="utf-8") as f:
                    notes = json.load(f)
                if not isinstance(notes, dict):
                    notes = {}
            except (OSError, ValueError):
                notes = {}
            at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
            if note:
                notes[key] = {"note": note, "at": at}
            else:
                notes.pop(key, None)
            tmp = f"{KOTYPO_NOTES}.tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(notes, f, ensure_ascii=False, indent=1)
            os.replace(tmp, KOTYPO_NOTES)
        _cache["ts"] = 0
        return self._send(200, json.dumps({"ok": True, "note": note, "at": at if note else ""},
                                          ensure_ascii=False))

    def _review(self):
        """검토 판정 — 항목 단위 **병합** 저장.

        kotypo 처럼 전체 map 을 교체하지 않는다. 이 상태는 나중 세션이 실행 목록으로
        읽는 지시서라, 다른 탭이 열려 있다는 이유로 판정이 통째로 날아가면 안 된다.
        """
        if _compare is None:
            return self._send(503, json.dumps({"ok": False, "error": "compare 없음"},
                                              ensure_ascii=False))
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 <= n <= 8192:
                raise ValueError
            patch = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            rel = patch.get("path", "")
            # 메모 삭제·완료는 id 로만 오므로 경로 검사 대상이 아니다.
            if patch.get("kind") not in ("note-del", "note-done"):
                full = os.path.normpath(os.path.join(ROOT, rel))
                if not full.startswith(f"{ROOT}/_posts/") or not full.endswith(".md"):
                    raise ValueError("bad path")
            state = _compare.review_update(patch)
        except Exception as e:  # noqa: BLE001
            return self._send(400, json.dumps({"ok": False, "error": str(e)},
                                              ensure_ascii=False))
        return self._send(200, json.dumps({"ok": True, "state": state},
                                          ensure_ascii=False))

    def _cron_action(self, path):
        try:
            n = int(self.headers.get("Content-Length") or 0)
            if not 0 <= n <= 4096:
                raise ValueError
            body = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
            jid = body.get("id")
            if jid not in CRON_IDS:      # 허용목록 — 임의 id 로 파일 못 만든다
                raise ValueError
        except Exception:
            return self._send(400, json.dumps({"ok": False, "error": "bad body"},
                                              ensure_ascii=False))
        if path.endswith("force-resume"):
            try:
                p = subprocess.run([QUOTA_GOVERNOR, "--force-resume", jid],
                                   capture_output=True, text=True, timeout=20)
                res = json.loads(p.stdout or "{}")
            except Exception as e:  # noqa: BLE001
                res = {"ok": False, "error": f"quota governor 호출 실패: {str(e)[:160]}"}
        elif path.endswith("pause"):
            args = ["--pause", jid, "--by", "blog-dash", "--json"]
            until = body.get("until")
            if isinstance(until, str) and re.match(r"^\d{4}-\d{2}-\d{2}T[\d:+\-]{4,14}$", until):
                args += ["--until", until]
        else:
            # 이 버튼의 소유권(blog-dash)만 해제한다. quota-governor hold는
            # reset 시각까지 독립적으로 남아야 한다.
            args = ["--resume", jid, "--by", "blog-dash", "--json"]
        if not path.endswith("force-resume"):
            res = gate_cli(*args)
        _cron_cache["ts"] = 0.0          # 다음 폴에서 바로 새 상태가 보이게
        _cache["ts"] = 0.0
        return self._send(200 if res.get("ok") else 500,
                          json.dumps(res, ensure_ascii=False))


def main():
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    srv.daemon_threads = True
    threading.Thread(target=_local_loop, daemon=True).start()
    srv.serve_forever()


if __name__ == "__main__":
    main()
