#!/usr/bin/env python3
"""blogdev-bot(Marvin) 기계 게이트 — `[dev]` 커밋 큐를 계산한다. LLM 호출 없음.

왜 있는가: 예전 Marvin은 "쓸 게 있는지" 판단하려고 매 틱 세션을 띄워
state.json·git log를 읽고 클러스터링한 뒤에야 "nothing to cover"로 끝났다.
매일 돌리면 대부분의 날이 그 헛턴이 된다. 이 스크립트가 **커밋 메시지의
`[dev]` 태그만 보고** 기계적으로 판정하므로, 쓸 게 없는 날은 모델을 아예
띄우지 않는다.

원장(ledger) 방식
-----------------
검토 범위는 워터마크가 아니라 **커밋별 해소 상태**로 정한다.

    검토 범위 = (baseline 이후의 모든 `[dev]` 커밋) − covered − dismissed

한 틱이 다룬 주제의 커밋만 covered 로 빠지므로, 같은 범위에 있던 다른
주제는 순서와 무관하게 남는다. 워터마크 하나로 범위를 자르면 한 틱이 여러
주제를 만났을 때 **다루지 않은 주제가 조용히 범위 밖으로 밀려난다**
(2026-08-15 실측: 그렇게 묻힌 주제 10건 — 양끝맞춤 4커밋, 검색엔진 등록
2커밋 등). 그래서 범위는 워터마크가 아니라 원장이 정한다.

해소 상태는 셋이다.

  covered   `wrote`/`augment` — 글로 다뤘다. 범위에서 빠진다.
  dismissed `dismiss` — 열어 보니 주제가 못 된다(오타·주석·한두 줄). 영구히 뺀다.
  deferred  `skip` — 아직 얇다. **범위에는 남기고** 모델만 안 깨운다.

deferred 가 범위에 남는 것이 핵심이다. 같은 주제의 커밋이 더 쌓여 모델이
깨어나면 그때 이전 것과 **합쳐서** 한 편으로 다룬다. 모델을 깨우는 조건은
"범위에 deferred 아닌 커밋이 있는가" 하나다.

baseline 은 가장 최근 `seed` 기록의 sha 다. 그보다 오래된 기록은 원장 계산에서
무시한다(v1 워터마크 기록과의 경계). git log 비용 상한 역할도 겸한다.

주의 — `git log --grep='[dev]'` 은 정규식이라 `[dev]`가 문자클래스(d|e|v)로
해석돼 사실상 전 커밋에 매칭된다 (2026-07-25 실측: 200/200). 반드시 `-F`.

사용법:
  dev_queue.py                    큐 출력. exit 0 = 쓸 것 있음, 3 = 없음(조용히 종료)
  dev_queue.py --json             같은 내용을 JSON으로
  dev_queue.py --record wrote    --shas <a,b,c> --slug <slug> --detail <path>
  dev_queue.py --record augment  --shas <a,b,c> --slug <slug> --detail <path>
  dev_queue.py --record dismiss  --shas <a,b,c> --detail "<이유>"
  dev_queue.py --record skip    [--shas <a,b,c>] --detail "<이유>"
  dev_queue.py --seed [<sha>]     원장 baseline 재설정 (기본 HEAD)

--record wrote/augment/dismiss 는 --shas 가 현재 미해소 목록 안에 있는지
검사한다. 범위 밖 sha 를 넘기면 거부한다 — 있지도 않은 커밋을 covered 로
적어 범위를 통째로 날리는 것이 옛 방식의 실패였다.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LOG = Path(os.environ.get("BLOGDEV_LOG")
           or Path(__file__).resolve().parent / "written.log")
WORKSHOP = REPO / "_posts/Misc/LLM_Workshop"

DEV_MARKER = "[dev]"
MAX_QUEUE = 40          # 범위가 비정상적으로 길 때의 상한 (잘리면 로그로 알린다)
RESOLVING = ("wrote", "augment")     # 범위에서 빼는 액션 — 글로 다뤘다
DISMISSING = ("dismiss",)            # 범위에서 빼는 액션 — 주제가 아니다
DEFERRING = ("skip",)                # 범위에 남기고 모델만 안 깨우는 액션
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
    """written.log 를 오래된 것 → 최신 순 리스트로. 형식 깨진 줄은 건너뛴다.

    sha 칸은 쉼표로 여러 개를 담을 수 있다(v2). v1 기록은 한 개짜리로 읽히며,
    baseline seed 보다 오래되면 원장 계산에서 어차피 무시된다.
    """
    if not LOG.exists():
        return []
    out = []
    for line in LOG.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 3:
            continue
        shas = [s.strip() for s in cols[2].split(",") if s.strip() and s.strip() != "-"]
        out.append({"ts": cols[0], "action": cols[1], "shas": shas,
                    "slug": cols[3] if len(cols) > 3 else "-",
                    "detail": cols[4] if len(cols) > 4 else ""})
    return out


def ledger(records):
    """(baseline, covered, dismissed, deferred) — baseline 이후 기록만 반영한다."""
    start = 0
    baseline = None
    for i, r in enumerate(records):
        if r["action"] == "seed" and r["shas"] and known(r["shas"][0]):
            baseline, start = r["shas"][0], i + 1
    covered, dismissed, deferred = set(), set(), set()
    for r in records[start:]:
        target = (covered if r["action"] in RESOLVING else
                  dismissed if r["action"] in DISMISSING else
                  deferred if r["action"] in DEFERRING else None)
        if target is None:
            continue
        target.update(s for s in r["shas"] if known(s))
    # 나중에 글로 다룬 커밋은 defer 상태를 벗는다 (기록 순서와 무관하게).
    deferred -= covered | dismissed
    return baseline, covered, dismissed, deferred


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
    return commits


def unresolved(records):
    """미해소 `[dev]` 커밋 전체 — 오래된 것부터, 상한 없이. 파일 목록은 안 붙인다.

    표시용 큐는 MAX_QUEUE 로 자르지만 `--shas` 검사는 이 목록을 쓴다. 잘린
    목록으로 검사하면 상한 너머의 커밋이 "범위 밖"으로 거부되는데, 정작 그것들은
    아직 해소되지 않은 것들이라 기록을 막을 이유가 없다.
    """
    baseline, covered, dismissed, deferred = ledger(records)
    return [c for c in dev_commits(baseline)
            if c["sha"] not in covered and c["sha"] not in dismissed], deferred


def review_queue(records):
    """(review, deferred_shas, truncated) — 표시용. 오래된 것부터 MAX_QUEUE 까지."""
    commits, deferred = unresolved(records)
    truncated = max(0, len(commits) - MAX_QUEUE)
    commits = commits[:MAX_QUEUE]
    for c in commits:
        c["files"] = git("show", "--name-only", "--format=", c["sha"]).split()
        c["deferred"] = c["sha"] in deferred
    return commits, deferred, truncated


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


def append(action, shas, slug, detail):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    LOG.parent.mkdir(parents=True, exist_ok=True)
    new = not LOG.exists()
    joined = ",".join(shas) if shas else "-"
    with LOG.open("a", encoding="utf-8") as fh:
        if new:
            fh.write("# blogdev-bot 집필 기록 — <utc>\\t<action>\\t<sha[,sha…]>"
                     "\\t<slug>\\t<detail>\n"
                     "# action: seed | wrote | augment | dismiss | skip\n")
        fh.write(f"{ts}\t{action}\t{joined}\t{slug or '-'}\t{detail or ''}\n")
    short = ",".join(s[:8] for s in shas) if shas else "-"
    print(f"기록: {action} {short} {slug or '-'} {detail or ''}")


def resolve_shas(raw, records, action):
    """--shas 를 full sha 로 펴고, 현재 미해소 목록 안에 있는지 검사한다."""
    commits, _ = unresolved(records)
    order = [c["sha"] for c in commits]
    pending = set(order)
    if raw is None:
        if action not in DEFERRING:
            sys.exit(f"--record {action} 에는 --shas 가 필요하다 "
                     "(다룬 주제에 속한 커밋을 전부 나열할 것)")
        # skip 은 생략하면 "지금 범위 전체를 훑었고 쓸 게 없다"는 뜻이다.
        return order
    out, bad = [], []
    for token in raw.split(","):
        token = token.strip()
        if not token:
            continue
        p = subprocess.run(["git", "-C", str(REPO), "rev-parse", f"{token}^{{commit}}"],
                           capture_output=True, text=True)
        if p.returncode != 0:
            bad.append(f"{token} (해석 실패)")
            continue
        sha = p.stdout.strip()
        if sha not in pending:
            bad.append(f"{token} (검토 범위 밖)")
            continue
        out.append(sha)
    if bad:
        sys.exit("--shas 거부: " + "; ".join(bad) +
                 "\n검토 범위 안의 sha 만 기록할 수 있다 — 범위 밖을 covered 로 "
                 "적으면 다루지 않은 주제가 통째로 묻힌다.")
    if not out:
        sys.exit("--shas 가 비었다")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--record", choices=["wrote", "augment", "dismiss", "skip"])
    ap.add_argument("--shas", help="쉼표로 구분한 커밋 sha 목록")
    ap.add_argument("--slug", default="-")
    ap.add_argument("--detail", default="")
    ap.add_argument("--seed", nargs="?", const="HEAD", default=None,
                    help="원장 baseline 재설정 (기본 HEAD)")
    args = ap.parse_args()

    if args.seed is not None:
        sha = git("rev-parse", f"{args.seed}^{{commit}}").strip()
        append("seed", [sha], "-", "원장 baseline 재설정")
        return 0

    if args.record:
        records = read_records()
        shas = resolve_shas(args.shas, records, args.record)
        append(args.record, shas, args.slug, args.detail)
        return 0

    records = read_records()
    baseline, covered, dismissed, deferred = ledger(records)
    review, _, truncated = review_queue(records)
    wake = [c for c in review if not c["deferred"]]

    if not wake:
        where = f"baseline={baseline[:8] if baseline else 'none'}"
        msg = (f"모델을 깨울 [dev] 커밋 없음 — 미해소 {len(review)}건이 전부 "
               f"deferred ({where}), LLM 호출 없이 종료") if review else (
               f"새 [dev] 커밋 없음 ({where}) — LLM 호출 없이 종료")
        if args.json:
            print(json.dumps({"pending": [], "reason": msg}, ensure_ascii=False))
        else:
            print(msg)
        return EXIT_NOTHING

    if truncated:
        print(f"경고: 미해소 [dev] 커밋이 상한({MAX_QUEUE})을 넘어 {truncated}건 잘렸다",
              file=sys.stderr)

    if args.json:
        print(json.dumps({"baseline": baseline, "review": review,
                          "pending": wake, "deferred": sorted(deferred),
                          "covered": len(covered), "dismissed": len(dismissed),
                          "truncated": truncated,
                          "workshop": workshop_inventory()},
                         ensure_ascii=False, indent=2))
        return 0

    deferred_review = [c for c in review if c["deferred"]]
    print(f"baseline={baseline[:8] if baseline else 'none'}  "
          f"선정후보={len(wake)}건  deferred보관={len(deferred_review)}건  "
          f"해소됨 covered={len(covered)} dismissed={len(dismissed)}")
    print("\n=== 선정 후보 [dev] 커밋 (non-deferred, 오래된 것부터) ===")
    for c in wake:
        print(f"\n{c['sha'][:8]}  {c['date']}  {c['subject']}")
        for f in c["files"][:25]:
            print(f"    {f}")
        if len(c["files"]) > 25:
            print(f"    … +{len(c['files']) - 25} files")
    if deferred_review:
        print("\n=== deferred 보관분 (단독 선정 금지, 같은 주제 후보에만 병합) ===")
        for c in deferred_review:
            print(f"\n{c['sha'][:8]}  {c['date']}  {c['subject']}  [deferred]")
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
