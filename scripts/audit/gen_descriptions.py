#!/usr/bin/env python3
"""Generate `description:` frontmatter for KO posts missing it, via claudemimo.

Run once. Idempotent (skips posts that already have description).
Logs every result; after completion, audits for Han character leakage.
"""
import glob
import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LANG = "ko"
TARGET_GLOB = f"_posts/Math/*/{LANG}/*.md"
LOG = REPO / "scripts" / "audit" / "gen_descriptions.log"
CLAUDEMIMO = "/home/junhyeok/.local/bin/claudemimo"
TIMEOUT = 120


PROMPT_TMPL = """다음 한국어 수학 블로그 글의 검색 결과 미리보기용 description meta tag를 한국어로 작성하세요.

요구사항:
- 1~2문장, 총 80~140자
- 한자 사용 절대 금지 (한국어 한글로만 작성)
- 수식 기호 사용 금지 ($$ $ \\ 등)
- 영문 수학 용어는 그대로 두되 가급적 한국어 용어 우선
- "이 글에서는", "이 포스트는" 같은 메타 표현 금지 — 글이 다루는 내용을 직접 서술
- 결과만 출력 (마크다운/따옴표/설명 없이)

제목: {title}

본문 발췌:
{excerpt}"""


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("---", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 3:]


def get_field(fm, name):
    m = re.search(rf'^{name}:\s*"?(.+?)"?\s*$', fm, re.M)
    return m.group(1) if m else None


def strip_math(body):
    body = re.sub(r"\$\$.+?\$\$", " ", body, flags=re.S)
    body = re.sub(r"\$.+?\$", " ", body)
    return body


def call_llm(prompt):
    p = subprocess.run(
        [CLAUDEMIMO, "-p", "--output-format", "text"],
        input=prompt, capture_output=True, text=True, timeout=TIMEOUT,
    )
    if p.returncode != 0:
        return None, f"rc={p.returncode}: {p.stderr.strip()[:200]}"
    out = p.stdout.strip()
    # Strip surrounding quotes if model wrapped result
    if out.startswith('"') and out.endswith('"'):
        out = out[1:-1].strip()
    return out, None


# Explicit \u escapes — literal CJK chars in source can be mis-encoded by shell
# heredocs (e.g. 豈 is U+8C48 not U+F900), making the range swallow Hangul.
HAN = re.compile("[一-鿿㐀-䶿豈-﫿]")


def insert_description(fm_text, desc):
    """Insert `description: "..."` into frontmatter, after `title:` if present."""
    escaped = desc.replace('"', '\\"')
    line = f'description: "{escaped}"'
    if re.search(r"^description:", fm_text, re.M):
        return re.sub(r"^description:.*$", line, fm_text, count=1, flags=re.M)
    # Insert after title line
    if re.search(r"^title:", fm_text, re.M):
        return re.sub(r"(^title:.*$)", rf"\1\n{line}", fm_text, count=1, flags=re.M)
    return line + "\n" + fm_text


def main():
    log_f = open(LOG, "a")

    def log(msg):
        line = f"[{time.strftime('%H:%M:%S')}] {msg}"
        print(line)
        log_f.write(line + "\n")
        log_f.flush()

    files = sorted(glob.glob(str(REPO / TARGET_GLOB)))
    missing = []
    for f in files:
        txt = Path(f).read_text()
        fm, _ = parse_frontmatter(txt)
        if fm is None:
            continue
        if get_field(fm, "description"):
            continue
        missing.append(f)

    log(f"total={len(files)} missing_description={len(missing)}")

    ok = fail = han_flagged = 0
    for i, f in enumerate(missing, 1):
        rel = Path(f).relative_to(REPO)
        txt = Path(f).read_text()
        fm, body = parse_frontmatter(txt)
        title = get_field(fm, "title") or Path(f).stem

        prose = strip_math(body)
        prose = re.sub(r"\s+", " ", prose).strip()
        excerpt = prose[:1500]
        prompt = PROMPT_TMPL.format(title=title, excerpt=excerpt)

        try:
            desc, err = call_llm(prompt)
        except subprocess.TimeoutExpired:
            desc, err = None, "timeout"
        if err or not desc:
            fail += 1
            log(f"[{i}/{len(missing)}] FAIL {rel}: {err}")
            continue

        # Han check
        if HAN.search(desc):
            han_flagged += 1
            log(f"[{i}/{len(missing)}] HAN_LEAK {rel}: {desc!r}")
            # Still write it; we'll fix in post-pass
        # Sanity: length
        if len(desc) > 300:
            log(f"[{i}/{len(missing)}] LONG {len(desc)}c {rel}: {desc[:80]!r}")
        if len(desc) < 30:
            log(f"[{i}/{len(missing)}] SHORT {len(desc)}c {rel}: {desc!r}")

        new_fm = insert_description(fm, desc)
        Path(f).write_text("---" + new_fm + "---" + body)
        ok += 1
        log(f"[{i}/{len(missing)}] OK {rel}: {desc[:80]}")

    log(f"DONE ok={ok} fail={fail} han_flagged={han_flagged}")


if __name__ == "__main__":
    main()
