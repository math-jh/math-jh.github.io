#!/usr/bin/env python3
"""한글 글의 excerpt(부제)·description(검색 설명문) 제안을 Antigravity 로 받아 대조표를 만든다.

글 파일은 고치지 않는다. 모델은 도구 없이 문장 두 개만 돌려주고, 글에서 재료를 뽑는 일과
결과 검사는 이 스크립트가 한다.

    propose [--jobs N] <글.md>... | --all
        글마다 재료를 모아 모델에 묻고 결과를 WORK 에 저장한다. --all 은 _posts/Math 의 한글 글 전부
        (미발행 포함). 이미 결과가 있는 글은 건너뛰고 실패한 글만 다시 묻는다. --jobs 는 동시 호출 수.
    report <출력.md>
        WORK 에 쌓인 결과를 사람이 읽는 대조표로 쓴다.

규칙 문장(프롬프트)은 옆의 frontmatter_rewrite.prompt.md 에 있다. {title} 같은 자리표시자는
이 스크립트가 채운다.

모델에 주는 재료: 제목·과목·지금의 두 필드·소제목·이름 붙은 정리·본문 앞부분,
그 글에 나오는 용어의 영어=한글 표(_data/terms.yml 과 본문의 <sub> 병기),
그 글 주제의 실제 검색어(구글·네이버 자동완성).

환경변수: FM_PROFILE(korean 기본 | english — 본문의 영어 용어를 그대로 두는 과목용), FM_MODEL(기본 gemini-4-hydrogen-high), FM_AGENT(기본 blog-translator — 도구 없는
에이전트), AGY_BIN, FM_WORK(기본 /var/tmp/blog-frontmatter).
"""
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.parse
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WORK = Path(os.environ.get("FM_WORK", "/var/tmp/blog-frontmatter"))
AGY_BIN = os.environ.get("AGY_BIN") or str(Path.home() / ".gemini/bin/agy")
MODEL = os.environ.get("FM_MODEL", "gemini-4-hydrogen-high")
AGENT = os.environ.get("FM_AGENT", "blog-translator")
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"

EXCERPT_RANGE = (10, 45)
DESCRIPTION_RANGE = (70, 110)

# 검색어 후보로 남길 수식어. 후보의 낱말은 이것이거나 글 본문에 있는 말이어야 한다.
MODIFIERS = set("정의 뜻 의미 증명 조건 필요충분조건 구하기 구하는법 계산 계산법 예제 문제 예시 예 차이 "
                "공식 성질 판별 판별법 하는법 방법 가능 활용 응용 정리 동치 반례 유도 풀이 개념".split())

# FM_PROFILE=english 는 본문이 영어로 쓰는 용어를 그대로 두는 과목용이다: 프롬프트가 다르고,
# 용어표에는 이 글에서 정의한 용어 중 terms.yml 이 한글로 확정한 것(primary: ko)과 본문의 <sub> 병기만 들어간다.
PROFILE = os.environ.get("FM_PROFILE", "korean")
PROMPT_FILE = Path(__file__).with_suffix(".prompt.md" if PROFILE == "korean" else f".{PROFILE}.prompt.md")


def squash(s):
    return re.sub(r"\s+", "", s or "")


def load_post(path):
    text = Path(path).read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        raise SystemExit(f"frontmatter 를 못 읽음: {path}")
    fm, body = m.group(1), m.group(2)

    def field(key):
        mm = re.search(rf'(?m)^{key}:\s*"?(.*?)"?\s*$', fm)
        return mm.group(1) if mm else ""

    return {
        "path": str(Path(path).resolve().relative_to(REPO)),
        "title": field("title"), "excerpt": field("excerpt"),
        "description": field("description"), "permalink": field("permalink").rstrip("/"),
        "category": (re.search(r"(?m)^categories:\s*\[(.*?)\]", fm) or [None, ""])[1],
        "published": not re.search(r"(?m)^published:\s*false", fm),
        "body": body,
    }


_TERMS = None


def all_terms():
    global _TERMS
    if _TERMS is None:
        data = yaml.safe_load((REPO / "_data/terms.yml").read_text(encoding="utf-8"))
        _TERMS = [e for group in data.values() for e in group]
    return _TERMS


def term_table(post):
    """이 글에 나오는 용어의 (영어, 한글) 쌍과, 그중 이 글에서 정의한 한글 용어 목록.

    terms.yml 에서 이 글을 defs 로 가리키는 항목, 영어 표기가 본문에 나오는 항목,
    본문의 <sub> 병기를 모은다. 이 글에서 정의한 것이 앞에 오고 나머지는 본문에 많이 나오는 순이다.
    """
    body = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", " ", post["body"], flags=re.S)
    defined, used = [], []
    # 긴 표기부터 세고 센 자리는 지운다 — order relation 안의 order 를 따로 세지 않기 위해서다.
    for e in sorted(all_terms(), key=lambda e: -len(str(e.get("en") or ""))):
        en, ko = str(e.get("en") or ""), str(e.get("ko") or "")
        if not en or not ko or "$" in en + ko:
            continue
        if PROFILE == "english" and e.get("primary") != "ko":
            continue
        if any(d.get("url", "").rstrip("/") == post["permalink"] for d in e.get("defs") or []):
            defined.append((en, ko))
            continue
        if PROFILE == "english":  # 이 글에서 정의한 것만 — 다른 뜻의 한글이 끌려오지 않게
            continue
        body, hits = re.subn(rf"(?<![A-Za-z]){re.escape(en)}(?:e?s)?(?![A-Za-z])", " ", body, flags=re.I)
        if hits:
            used.append((hits, en, ko))
    for a, b in re.findall(r"\*([^*<\n]{1,60})<sub>([^<\n]{1,60})</sub>", post["body"]):
        en, ko = (b, a) if re.search("[가-힣]", a) else (a, b)
        if re.search("[가-힣]", ko) and "$" not in en + ko:
            defined.append((en.strip(), ko.strip()))
    seen, pairs = set(), []
    for en, ko in defined + [(en, ko) for _, en, ko in sorted(used, key=lambda t: -t[0])]:
        key = (en.lower(), squash(ko))
        if key not in seen:
            seen.add(key)
            pairs.append((en, ko))
    return pairs[:45], [ko for _, ko in defined]


def suggest(seed, cache):
    """구글·네이버 자동완성. seed 와 'seed ' 두 번 물어 합친다."""
    if seed in cache:
        return cache[seed]
    got = []
    for q in (seed, seed + " "):
        enc = urllib.parse.quote(q)
        for url, pick in (
            ("https://suggestqueries.google.com/complete/search?client=firefox&hl=ko&gl=kr&q=" + enc,
             lambda j: j[1]),
            ("https://ac.search.naver.com/nx/ac?q=" + enc + "&con=0&frm=nv&ans=2&r_format=json"
             "&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100",
             lambda j: [x[0] for x in (j.get("items") or [[]])[0]]),
        ):
            raw = subprocess.run(["curl", "-s", "-m", "15", "-A", UA, url], capture_output=True).stdout
            try:
                try:
                    txt = raw.decode("utf-8")
                except UnicodeDecodeError:
                    txt = raw.decode("euc-kr", "ignore")
                got += [s for s in pick(json.loads(txt)) if s not in got]
            except (ValueError, KeyError, IndexError, TypeError):
                pass
            time.sleep(0.3)
    cache[seed] = got
    return got


def search_candidates(post, defined_ko, cache):
    """글 주제(제목의 낱말과 이 글에서 정의한 한글 용어)에 붙는 실제 검색어."""
    seeds = [s.strip() for s in re.split(r",|·|(?<=[가-힣])[과와]\s", post["title"]) if s.strip()]
    body = squash(post["body"])
    defined = sorted({ko for ko in defined_ko if squash(ko) in body}, key=lambda ko: body.find(squash(ko)))
    seeds += [ko for ko in defined if ko not in seeds][:5]
    seeds = [s for s in seeds if re.search("[가-힣]", s)][:7]
    out = []
    for seed in seeds:
        for s in suggest(seed, cache):
            if squash(seed) not in squash(s) or squash(s) == squash(seed) or s in out:
                continue
            if all(t in MODIFIERS or squash(t) in body for t in s.split()):
                out.append(s)
    return seeds, out[:14]


def build_prompt(post, terms, queries):
    body = post["body"]
    heads = [h.strip() for h in re.findall(r"(?m)^##+\s*(.+)$", body)]
    labels = [f"{k} ({n})" for k, n in re.findall(r"(?m)^::: (\S+) \d+ \((.+?)\)\s*$", body)]
    head = re.sub(r"\{%.*?%\}", "", body, flags=re.S).strip()[:1500]
    values = dict(
        e0=EXCERPT_RANGE[0], e1=EXCERPT_RANGE[1], d0=DESCRIPTION_RANGE[0], d1=DESCRIPTION_RANGE[1],
        title=post["title"], category=post["category"], excerpt=post["excerpt"],
        description=post["description"], heads=" / ".join(heads) or "(없음)",
        labels=", ".join(labels[:25]) or "(없음)",
        terms=", ".join(f"{en}={ko}" for en, ko in terms) or "(없음)",
        queries=", ".join(queries) or "(없음)", head=head)
    # 규칙 문장은 본문보다 먼저 채운다 — 본문에 {title} 같은 글자가 있어도 다시 치환되지 않게.
    text = PROMPT_FILE.read_text(encoding="utf-8")
    for key in ("e0", "e1", "d0", "d1", "title", "category", "excerpt", "description",
                "heads", "labels", "terms", "queries", "head"):
        text = text.replace("{" + key + "}", str(values[key]), 1)
    return text


def ask(prompt):
    # 첫 메시지의 리터럴 [cron] 은 세션 리퍼가 봇 대화로 알아보는 표지다 (translate_worker 와 같은 규약).
    proc = subprocess.run(
        [AGY_BIN, "--print", "[cron]\n\n" + prompt, "--model", MODEL, "--agent", AGENT,
         "--output-format", "json", "--disable-slash-commands", "--print-timeout", "10m"],
        capture_output=True, text=True, stdin=subprocess.DEVNULL, cwd="/tmp", timeout=900)
    if proc.returncode != 0:
        raise RuntimeError(f"agy exit {proc.returncode}: {proc.stderr.strip()[:400]}")
    env = json.loads(proc.stdout)
    if env.get("status") != "SUCCESS":
        raise RuntimeError(f"agy status={env.get('status')!r}: {str(env.get('error', ''))[:400]}")
    return str(env.get("response", ""))


def parse(raw):
    out = {}
    for key in ("EXCERPT", "DESCRIPTION"):
        m = re.search(rf"<<<{key}\s*\n(.*?)\n\s*>>>", raw, re.S)
        if not m:
            raise ValueError(f"{key} 블록 없음")
        out[key.lower()] = m.group(1).strip()
    return out


def check(post, terms, value, kind):
    """사람이 볼 표시 목록. 자동으로 버리지는 않는다."""
    if value == "KEEP":
        return []
    flags = []
    lo, hi = EXCERPT_RANGE if kind == "excerpt" else DESCRIPTION_RANGE
    if not lo <= len(value) <= hi:
        flags.append(f"길이 {len(value)}자(기준 {lo}~{hi})")
    for ch, name in (("$", "$"), ('"', "큰따옴표"), ("\n", "줄바꿈"), (":", "콜론")):
        if ch in value:
            flags.append(f"{name} 포함")
    if not re.search("[가-힣]", value):
        flags.append("한글 없음")
    if kind == "excerpt" and squash(value) == squash(post["title"]):
        flags.append("제목과 같음")
    known = squash(post["body"] + post["title"] + post["excerpt"] + post["description"]
                   + "".join(ko for _, ko in terms))
    alien = sorted({str(e["ko"]) for e in all_terms()
                    if e.get("ko") and "$" not in str(e["ko"]) and len(squash(str(e["ko"]))) >= 3
                    and squash(str(e["ko"])) in squash(value) and squash(str(e["ko"])) not in known})
    if alien:
        flags.append("글에 없는 용어: " + ", ".join(alien))
    return flags


def record_path(rel):
    return WORK / (hashlib.md5(rel.encode()).hexdigest()[:10] + ".json")


def propose_one(path, cache, lock):
    post = load_post(path)
    out = record_path(post["path"])
    if out.exists() and "new" in json.loads(out.read_text(encoding="utf-8")):
        return "건너뜀 " + post["path"]
    terms, defined_ko = term_table(post)
    with lock:  # 자동완성은 한 번에 한 글씩만 묻는다
        seeds, queries = search_candidates(post, defined_ko, cache)
        (WORK / "ac-cache.json").write_text(json.dumps(cache, ensure_ascii=False, indent=1),
                                            encoding="utf-8")
    prompt = build_prompt(post, terms, queries)
    rec = {k: post[k] for k in ("path", "title", "excerpt", "description", "category", "published")}
    rec.update(model=MODEL, profile=PROFILE, seeds=seeds, queries=queries,
               terms=[f"{en}={ko}" for en, ko in terms], prompt=prompt)
    try:
        rec["raw"] = ask(prompt)
        new = parse(rec["raw"])
        rec["new"] = new
        rec["flags"] = {k: check(post, terms, new[k], k) for k in ("excerpt", "description")}
    except Exception as exc:  # 한 편이 실패해도 나머지는 계속한다
        rec["error"] = f"{type(exc).__name__}: {exc}"
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    return ("실패 " if "error" in rec else "완료 ") + post["path"] + " " + rec.get("error", "")


def cmd_propose(args):
    jobs = 1
    if "--jobs" in args:
        i = args.index("--jobs")
        jobs = int(args[i + 1])
        del args[i:i + 2]
    if args == ["--all"]:
        args = sorted(str(p) for p in REPO.glob("_posts/Math/*/ko/*.md"))
    WORK.mkdir(parents=True, exist_ok=True)
    cache_path = WORK / "ac-cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    lock = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor(jobs) as pool:
        for line in pool.map(lambda p: propose_one(p, cache, lock), args):
            print(line, flush=True)


def cmd_report(out_path):
    recs = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(WORK.glob("*.json"))
            if p.name != "ac-cache.json"]
    done = sum("new" in r for r in recs)
    recs.sort(key=lambda r: r["path"])
    lines = [f"# excerpt·description 제안 대조표 ({len(recs)}편, 모델 {MODEL})", "",
             "글 파일은 고치지 않았다. `KEEP` 은 모델이 지금 것을 그대로 두자고 한 것이다.", ""]
    for r in recs:
        lines += [f"## {r['title']}", "",
                  f"`{r['path']}` · {'발행' if r['published'] else '미발행'}", ""]
        if "error" in r:
            lines += [f"- 실패: {r['error']}", ""]
            continue
        for key, label in (("excerpt", "부제"), ("description", "설명문")):
            old, new = r[key], r["new"][key]
            lines.append(f"- {label} 지금 ({len(old)}자): {old}")
            lines.append(f"- {label} 제안 ({'그대로' if new == 'KEEP' else str(len(new)) + '자'}): {new}")
            for f in r["flags"][key]:
                lines.append(f"  - 표시: {f}")
        lines.append(f"- 검색어 후보: {', '.join(r['queries']) or '(없음)'}")
        lines.append("")
    Path(out_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"{out_path} 에 {len(recs)}편 기록 (성공 {done}, 실패 {len(recs) - done})")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "propose":
        cmd_propose(sys.argv[2:])
    elif len(sys.argv) == 3 and sys.argv[1] == "report":
        cmd_report(sys.argv[2])
    else:
        raise SystemExit(__doc__)
