#!/usr/bin/env python3
"""판본 스냅샷 빌드 — 임의의 git ref 를 구워서 HTML 만 남긴다.

비교기(#compare)의 "이전" pane 은 구워진 페이지여야 한다. 마크다운을 따로 렌더하면
플러그인(fenced_theorem_blocks·diagram_tag·link_normalizer…)을 흉내내야 하므로,
그 ref 의 트리를 통째로 꺼내 진짜 jekyll 로 빌드한다.

산출물은 `~/.local/state/blog-snapshots/<sha12>/` 에 남는다:

    MANIFEST.json     sha·제목·커밋시각·빌드시각·문서 수
    html/**/*.html    _site 의 ko/·en/ 만 (pagefind·assets 제외 → 판본당 ~95MB)
    katex-macros.js   그 판본의 매크로 (구간 안에서 매크로가 바뀐 적이 있다)

pane 의 CSS·JS 는 현재 판본 것을 쓴다 (내용 diff 가 목적이므로 의도한 선택).
매크로만 판본을 따라가는 이유는 매크로가 바뀌면 옛 본문의 수식이 아예 렌더되지
않아 diff 가 아니라 렌더 실패로 보이기 때문이다.

트리를 꺼내는 데 worktree 를 쓰지 않는다 (이 repo 는 read-only git 만 허용).
`ls-tree`+`cat-file` 로 직접 푼 뒤 `.git` 만 심볼릭 링크로 걸어준다 —
last_modified_git.rb 가 `git -C <source> log` 로 날짜를 읽으므로 링크가 없으면
그 플러그인이 빈 손으로 돌아간다. 링크된 git 은 읽기만 한다.

사용법:
    snapshot.py <ref> [--force] [--keep]
    snapshot.py --list
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SNAP_ROOT = Path.home() / ".local/state/blog-snapshots"
# /tmp 는 tmpfs(RAM) 라 빌드 산출물을 올리면 7GB 중 2GB 여유를 그대로 먹는다.
WORK_ROOT = Path("/var/tmp/blog-snapshot-build")
MEM_MAX = "1500M"  # jekyll-blog.service 와 같은 한도 — 임시 빌드가 dev 서버를 굶기지 않게

KEEP_TREES = ("ko", "en")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO), *args], capture_output=True, text=True, check=True
    ).stdout


def resolve(ref: str) -> str:
    return git("rev-parse", f"{ref}^{{commit}}").strip()


def materialize(sha: str, dest: Path) -> int:
    """<sha> 의 트리를 dest 에 푼다. 반환값은 푼 파일 수."""
    listing = subprocess.run(
        ["git", "-C", str(REPO), "ls-tree", "-r", "-z", sha],
        capture_output=True,
        check=True,
    ).stdout
    entries = []
    for rec in listing.split(b"\0"):
        if not rec:
            continue
        meta, path = rec.split(b"\t", 1)
        mode, kind, blob = meta.split(b" ")
        if kind != b"blob":
            continue
        entries.append((mode.decode(), blob.decode(), path.decode("utf-8", "surrogateescape")))

    proc = subprocess.Popen(
        ["git", "-C", str(REPO), "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    assert proc.stdin and proc.stdout
    proc.stdin.write(("\n".join(e[1] for e in entries) + "\n").encode())
    proc.stdin.close()

    for mode, _blob, path in entries:
        header = proc.stdout.readline()
        size = int(header.split()[2])
        data = proc.stdout.read(size)
        proc.stdout.read(1)  # trailing newline
        target = dest / path
        target.parent.mkdir(parents=True, exist_ok=True)
        if mode == "120000":  # symlink
            link = data.decode()
            if target.exists() or target.is_symlink():
                target.unlink()
            os.symlink(link, target)
            continue
        target.write_bytes(data)
        if mode == "100755":
            target.chmod(0o755)
    proc.wait()
    return len(entries)


def build(src: Path, site: Path, log: Path) -> None:
    env = dict(os.environ)
    env.update(
        BUNDLE_PATH=str(REPO / "vendor/bundle"),
        BUNDLE_FORCE_RUBY_PLATFORM="true",
        JEKYLL_ENV="development",  # dev 서버(4001)와 같은 환경 — 그쪽이 "현재" pane 이다
    )
    cmd = [
        "systemd-run", "--user", "--scope", "-q",
        "-p", f"MemoryMax={MEM_MAX}",
        "-p", "MemorySwapMax=256M",
        "--",
        "bundle", "exec", "jekyll", "build",
        "--source", str(src),
        "--destination", str(site),
        "--unpublished",   # 감사 대상 141편이 양쪽 판본 모두 published:false 다
        "--trace",
    ]
    with log.open("wb") as fh:
        rc = subprocess.run(cmd, cwd=src, env=env, stdout=fh, stderr=subprocess.STDOUT).returncode
    if rc != 0:
        tail = log.read_text(errors="replace").splitlines()[-25:]
        raise SystemExit("jekyll build 실패 (rc=%d)\n%s" % (rc, "\n".join(tail)))


def harvest(site: Path, dest: Path, src: Path) -> int:
    html_root = dest / "html"
    if html_root.exists():
        shutil.rmtree(html_root)
    count = 0
    for tree in KEEP_TREES:
        srcdir = site / tree
        if not srcdir.is_dir():
            continue
        for path in srcdir.rglob("*.html"):
            rel = path.relative_to(site)
            out = html_root / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, out)
            count += 1
    macros = src / "assets/js/katex-macros.js"
    if macros.exists():
        shutil.copyfile(macros, dest / "katex-macros.js")
    return count


def snapshot(ref: str, force: bool = False, keep: bool = False) -> Path:
    sha = resolve(ref)
    short = sha[:12]
    dest = SNAP_ROOT / short
    manifest = dest / "MANIFEST.json"
    if manifest.exists() and not force:
        print(f"이미 있음: {dest}")
        return dest

    subject = git("log", "-1", "--format=%s", sha).strip()
    committed = git("log", "-1", "--format=%cI", sha).strip()

    work = WORK_ROOT / short
    src, site = work / "src", work / "site"
    if work.exists():
        shutil.rmtree(work)
    src.mkdir(parents=True)

    t0 = time.time()
    print(f"[1/3] 트리 전개 {short} …", flush=True)
    files = materialize(sha, src)
    # 플러그인이 `git -C <source> log` 로 날짜를 읽는다. 링크가 없으면 조용히 빈 값.
    os.symlink(REPO / ".git", src / ".git")

    print(f"[2/3] jekyll build ({files} files) …", flush=True)
    dest.mkdir(parents=True, exist_ok=True)
    build(src, site, dest / "build.log")

    print("[3/3] HTML 추림 …", flush=True)
    pages = harvest(site, dest, src)
    manifest.write_text(
        json.dumps(
            {
                "sha": sha,
                "short": short,
                "ref": ref,
                "subject": subject,
                "committed": committed,
                "built_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "pages": pages,
                "build_seconds": round(time.time() - t0, 1),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    if not keep:
        shutil.rmtree(work, ignore_errors=True)
    print(f"완료: {dest}  ({pages} pages, {round(time.time()-t0)}s)")
    return dest


def list_snapshots() -> None:
    if not SNAP_ROOT.is_dir():
        print("(없음)")
        return
    for d in sorted(SNAP_ROOT.iterdir()):
        m = d / "MANIFEST.json"
        if not m.exists():
            print(f"{d.name}\t(미완성)")
            continue
        info = json.loads(m.read_text(encoding="utf-8"))
        print(f"{info['short']}\t{info['committed'][:16]}\t{info['pages']}p\t{info['subject'][:60]}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ref", nargs="?", help="git ref (예: 4a061156^)")
    ap.add_argument("--force", action="store_true", help="이미 있어도 다시 빌드")
    ap.add_argument("--keep", action="store_true", help="빌드 트리를 지우지 않는다 (디버깅)")
    ap.add_argument("--list", action="store_true", help="스냅샷 목록")
    args = ap.parse_args()

    if args.list or not args.ref:
        list_snapshots()
        return
    snapshot(args.ref, force=args.force, keep=args.keep)


if __name__ == "__main__":
    main()
