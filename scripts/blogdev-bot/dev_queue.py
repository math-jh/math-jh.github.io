#!/usr/bin/env python3
"""blogdev-bot(Marvin) 기계 게이트 — `[dev]` 커밋 큐를 계산한다. LLM 호출 없음.

왜 있는가: 예전 Marvin은 "쓸 게 있는지" 판단하려고 매 틱 세션을 띄워
state.json·git log를 읽고 클러스터링한 뒤에야 "nothing to cover"로 끝났다.
매일 돌리면 대부분의 날이 그 헛턴이 된다. 이 스크립트가 **커밋 메시지의
`[dev]` 태그만 보고** 기계적으로 판정하므로, 쓸 게 없는 날은 모델을 아예
띄우지 않는다.

워터마크가 둘인 이유 (written.log 의 마지막 기록들에서 계산):

  gate  = 모든 기록(wrote/augment/skip/seed) 중 가장 최신 sha
          → 이보다 새로운 `[dev]` 커밋이 없으면 **LLM을 띄우지 않는다**.
  scan  = `wrote`/`augment`/`seed` 기록 중 가장 최신 sha
          → Marvin이 *검토할* 범위의 시작점.

둘을 분리해야 "주제가 아직 빈약해서 스킵" 이 제대로 동작한다. skip은 gate만
전진시키므로 같은 얇은 커밋으로 매일 모델이 깨어나지 않고, scan은 그대로 있으니
나중에 같은 주제 커밋이 더 쌓이면 이전 것들과 **합쳐서** 한 편으로 다룬다.

주의 — `git log --grep='[dev]'` 은 정규식이라 `[dev]`가 문자클래스(d|e|v)로
해석돼 사실상 전 커밋에 매칭된다 (2026-07-25 실측: 200/200). 반드시 `-F`.

사용법:
  dev_queue.py                    큐 출력. exit 0 = 쓸 것 있음, 3 = 없음(조용히 종료)
  dev_queue.py --json             같은 내용을 JSON으로
  dev_queue.py --record wrote  --sha <sha> --slug <slug> --detail <path>
  dev_queue.py --record augment --sha <sha> --slug <slug> --detail <path>
  dev_queue.py --record skip    --sha <sha> --detail "<이유>"
  dev_queue.py --seed [<sha>]     워터마크 초기화 (기본 HEAD)
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LOG = Path(__file__).resolve().parent / "written.log"
WORKSHOP = REPO / "_posts/Misc/LLM_Workshop"

DEV_MARKER = "[dev]"
MAX_QUEUE = 40          # 첫 실행에서 히스토리가 길 때의 상한 (잘리면 로그로 알린다)
ADVANCING = ("wrote", "augment", "seed")   # scan 워터마크를 전진시키는 액션
EXIT_NOTHING = 3        # drive.sh 가 이 코드를 보고 조용히 종료한다


def git(*args, check=True):
    p = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, text=True)
    if check and p.returncode != 0:
        sys.exit(f"git {' '.join(args)} 실패: {p.stderr.strip()[:300]}")
    return p.stdout


def known(sha):
    """sha 가 현재 히스토리에 존재하는 커밋인가 (rebase 후 유실 대비)."""
    if not sha or sha == "-":
        return False
    p = subprocess.run(["git", "-C", str(REPO), "cat-file", "-e", f"{sha}^{{commit}}"],
                       capture_output=True)
    return p.returncode == 0


def read_records():
    """written.log 를 오래된 것 → 최신 순 리스트로. 형식 깨진 줄은 건너뛴다."""
    if not LOG.exists():
        return []
    out = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 3:
            continue
        out.append({"ts": cols[0], "action": cols[1], "sha": cols[2],
                    "slug": cols[3] if len(cols) > 3 else "-",
                    "detail": cols[4] if len(cols) > 4 else ""})
    return out


def watermarks(records):
    """(gate_sha, scan_sha) — 히스토리에 실재하는 가장 최신 기록 기준."""
    gate = next((r["sha"] for r in reversed(records) if known(r["sha"])), None)
    scan = next((r["sha"] for r in reversed(records)
                 if r["action"] in ADVANCING and known(r["sha"])), None)
    return gate, scan


def dev_commits(since):
    """since 이후의 `[dev]` 커밋 — 오래된 것부터. since 가 None이면 전체 히스토리."""
    rng = f"{since}..HEAD" if since else "HEAD"
    fmt = "%H\x1f%cI\x1f%s"
    raw = git("log", "-F", f"--grep={DEV_MARKER}", "--no-merges", "--reverse",
              f"--format={fmt}", rng)
    commits = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        sha, iso, subject = line.split("\x1f", 2)
        commits.append({"sha": sha, "date": iso[:10], "subject": subject, "files": []})
    truncated = max(0, len(commits) - MAX_QUEUE)
    commits = commits[:MAX_QUEUE]
    for c in commits:
        files = git("show", "--name-only", "--format=", c["sha"]).split()
        c["files"] = files
    return commits, truncated


def workshop_inventory():
    """기존 LLM Workshop 글 목록 — 보완 후보를 고르기 위한 재고."""
    items = []
    if not WORKSHOP.is_dir():
        return items
    for p in sorted(WORKSHOP.glob("*.md")):
        if p.name == "CLAUDE.md":
            continue
        title = permalink = ""
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines()[:30]:
            if line.startswith("title:") and not title:
                title = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("permalink:") and not permalink:
                permalink = line.split(":", 1)[1].strip()
        items.append({"path": str(p.relative_to(REPO)), "title": title,
                      "permalink": permalink})
    return items


def append(action, sha, slug, detail):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    LOG.parent.mkdir(parents=True, exist_ok=True)
    new = not LOG.exists()
    with LOG.open("a", encoding="utf-8") as fh:
        if new:
            fh.write("# blogdev-bot 집필 기록 — <utc>\\t<action>\\t<covered_sha>"
                     "\\t<slug>\\t<detail>\n"
                     "# action: seed | wrote | augment | skip\n")
        fh.write(f"{ts}\t{action}\t{sha}\t{slug or '-'}\t{detail or ''}\n")
    print(f"기록: {action} {sha[:8]} {slug or '-'} {detail or ''}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--record", choices=["wrote", "augment", "skip"])
    ap.add_argument("--sha")
    ap.add_argument("--slug", default="-")
    ap.add_argument("--detail", default="")
    ap.add_argument("--seed", nargs="?", const="HEAD", default=None,
                    help="워터마크 초기화 (기본 HEAD)")
    args = ap.parse_args()

    if args.seed is not None:
        sha = git("rev-parse", args.seed).strip()
        append("seed", sha, "-", "watermark 초기화")
        return 0

    if args.record:
        if not args.sha:
            sys.exit("--record 에는 --sha 가 필요하다")
        sha = git("rev-parse", args.sha).strip()
        append(args.record, sha, args.slug, args.detail)
        return 0

    records = read_records()
    gate, scan = watermarks(records)
    pending, truncated = dev_commits(gate)

    if not pending:
        msg = (f"새 [dev] 커밋 없음 (gate={gate[:8] if gate else 'none'}) "
               "— LLM 호출 없이 종료")
        if args.json:
            print(json.dumps({"pending": [], "reason": msg}, ensure_ascii=False))
        else:
            print(msg)
        return EXIT_NOTHING

    # 검토 범위는 scan 부터 — skip 으로 넘긴 얇은 커밋들을 새 커밋과 합쳐 볼 수 있게.
    review, _ = dev_commits(scan)
    if truncated:
        print(f"경고: [dev] 커밋이 상한({MAX_QUEUE})을 넘어 {truncated}건 잘렸다",
              file=sys.stderr)

    if args.json:
        print(json.dumps({"gate": gate, "scan": scan, "pending": pending,
                          "review": review, "truncated": truncated,
                          "workshop": workshop_inventory()},
                         ensure_ascii=False, indent=2))
        return 0

    print(f"gate={gate[:8] if gate else 'none'}  scan={scan[:8] if scan else 'none'}  "
          f"새 [dev]={len(pending)}건  검토범위={len(review)}건")
    print(f"\n=== 검토 범위 [dev] 커밋 (오래된 것부터 — 이 순서로 다룬다) ===")
    for c in review:
        print(f"\n{c['sha'][:8]}  {c['date']}  {c['subject']}")
        for f in c["files"][:25]:
            print(f"    {f}")
        if len(c["files"]) > 25:
            print(f"    … +{len(c['files']) - 25} files")
    print(f"\n=== 기존 LLM Workshop 글 {len(workshop_inventory())}편 (보완 후보) ===")
    for it in workshop_inventory():
        print(f"  {it['path'].split('/')[-1]}  {it['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
