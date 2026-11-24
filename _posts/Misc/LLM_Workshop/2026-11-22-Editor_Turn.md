---

title: "집필 턴 뒤의 편집 턴"
excerpt: "새로 쓴 글을 diff 없이 독자로서 다시 읽고 구성을 고치는 별도 모델 턴과, 그 결과가 글을 망가뜨리면 집필 판본으로 되돌리는 edit_guard"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/editor_turn

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-22
weight: 77
group: agents

---

관련 파일: [`scripts/blogdev-bot/drive.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/blogdev-bot/drive.sh), [`scripts/blogdev-bot/edit_guard.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/blogdev-bot/edit_guard.py), [`scripts/blogdev-bot/editor.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/blogdev-bot/editor.md), [`scripts/blogdev-bot/marvin.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/blogdev-bot/marvin.md) ([42095cdf](https://github.com/math-jh/math-jh.github.io/commit/42095cdf32faf38b1a13c9ed44d80ac5917baec9))
{: .notice--info}

사용자는 11월 22일에 [섀도 재판정](/ko/llm_workshop/shadow_rejudging) 글을 읽다가, 한 작업이었던 일이 별개 절로 적혀 있는 것을 짚었다. 본편 승격은 옛 분류기 제거와 개명이 합쳐진 일이었는데, 글에는 따로 선 절로 들어가 있었다.

> 지금 마빈이 틱이 돌 때마다 새로 절을 만들려고 하는데, 기존에 있던 절을 수정하는 게 사실은 맞았던 거거든.

문제가 된 것은 글의 절이 시스템의 부품이 아니라 틱에 대응한다는 점이었다. 같은 날 사용자는 이를 고치는 방향도 정했다.

> 내 생각엔 글 작성자 턴이랑 편집자 턴을 따로 해서, 편집을 해야 된다고 판단되면 편집 턴을 새로 열어서, 편집 턴은 글을 읽고 나서 전부 구성까지 바꾸고 하는 걸로 새로운 별도 프롬프트로 만드는 게 어떨까 싶거든.

앞서 11월 3일에 [e1bc097a](https://github.com/math-jh/math-jh.github.io/commit/e1bc097a58718fe6a697b4f63532a62d16f97eff)에서 마련된 규칙도 같은 문제를 겨냥하고 있었다. 보완은 글 끝에 절을 덧붙이지 말고 해당 절을 고쳐 쓰라는 것, 절이 6개나 글이 20KB를 넘으면 새 글을 쓰라는 것이다. 그런데 이 규칙을 읽는 쪽은 매번 커밋 diff를 펼쳐 놓고 쓰는 집필 턴이다. diff에 있는 것은 이 글의 이야기와 상관없어도 문장이 되기 쉽고, 새로 생긴 일은 그 동작을 설명하던 자리를 고치는 대신 뒤에 붙는다. 같은 모델이 같은 diff를 보면서 규칙을 지키는 데는 한계가 있어서, 구성을 다시 보는 일은 diff를 보지 않는 다른 모델에게 넘어갔다.

## 드라이버의 편집 턴

`drive.sh`는 Marvin의 집필 턴(sonnet)이 끝난 뒤, 커밋하기 전에 편집 턴(opus)을 한 번 끼워 넣는다. 편집 대상은 집필 턴이 워크숍 경로에 남긴 글이다.

```bash
EDIT_STORE="$(mktemp -d)"
trap 'rm -rf "$BEFORE_DIRTY" "$EDIT_STORE"' EXIT
# edit_guard.py 가 죽어도 드라이버는 계속 간다 — 편집을 건너뛸 뿐 커밋은 해야 한다.
EDIT_TARGETS="$("$HERE/edit_guard.py" --save "$EDIT_STORE" --before "$BEFORE_DIRTY" | tr '\n' ' ' || true)"
if [ -n "${EDIT_TARGETS// /}" ]; then
  log "launching claude -p (opus) for editor: $EDIT_TARGETS"
  if timeout 2400 "$CLAUDE_BIN" -p --model opus \
        --permission-mode bypassPermissions \
        "[cron] Read $HERE/editor.md and execute it now. 대상 글: $EDIT_TARGETS"; then
    "$HERE/edit_guard.py" --check "$EDIT_STORE" 2>&1 | while read -r line; do
      log "$line"
    done || true
    log "editor turn complete"
  else
    "$HERE/edit_guard.py" --restore "$EDIT_STORE" 2>&1 | while read -r line; do
      log "$line"
    done || true
    log "editor turn failed — 집필 턴의 글을 그대로 커밋한다"
  fi
fi
```
{: data-filename="scripts/blogdev-bot/drive.sh · 일부 발췌"}

`edit_guard.py --save`가 먼저 대상 글을 찾아 임시 디렉토리에 복사해 두고 경로를 출력한다. 대상은 워크숍 경로에서 커밋되지 않은 `.md` 파일 가운데, 집필 턴이 시작되기 전의 dirty 목록(`--before`, `commit_posts.py --snapshot`이 남긴 것)에 없던 것이다. 그 목록에 있던 글은 사용자가 손으로 편집하던 글이므로 편집 턴에 넘기지 않는다. 대상이 없으면 편집 턴은 뜨지 않는다. `edit_guard.py`가 죽어도 `|| true`로 넘어가므로, 이때도 편집만 건너뛰고 커밋은 진행된다.

편집 턴이 정상적으로 끝나면 `--check`가 결과를 검사하고, 비정상으로 끝나면(타임아웃 포함) `--restore`가 검사 없이 집필 판본을 되돌린다. 어느 쪽이든 마지막에 커밋되는 것은 집필 턴이 낸 글이거나 검사를 통과한 편집본이다.

## diff를 보지 않는 편집자

편집 턴의 지시서 `editor.md`는 읽을 것과 읽지 않을 것을 갈라 놓는다. 읽는 것은 대상 글 전체, `_posts/Misc/LLM_Workshop/CLAUDE.md`, 그리고 이번 틱이 그 글에 한 변경(`git diff -- <글>`)이다. 새 글이면 이 diff가 비어 있고, 그때는 글 전체가 이번 틱의 것이다. 읽지 않는 것은 `[dev]` 커밋의 `git show`와 `git log -p`, `scripts/blogdev-bot/`의 큐, 대화 트랜스크립트다. 글에 없는 내용을 찾아 넣는 것은 편집자의 일이 아니기 때문이다.

그다음 절차는 독자의 일을 그대로 따른다. 글을 제목부터 끝까지 읽으며 절마다 "독자에게 해 주는 일"을 한 줄씩 적고, 이 글의 이야기를 두세 문장으로 적는다. 고칠지 여부는 이 두 가지로 판정하고, 고칠 것이 보이지 않으면 글에 손대지 않는다. 판정 기준은 다음과 같다.

- 두 절의 한 줄 요약이 겹치거나, 한 부품이나 사건이 두 절에 나뉘어 있다.
- 절이나 문단이 부품이 아니라 일이 일어난 날에 대응한다. 날짜로 시작하는 문단이 붙어 "그 뒤 이렇게 바뀌었다"로 이어지는 경우가 여기에 든다.
- 이야기를 읽는 데 필요 없는 것이 들어 있다.
- 절의 순서가 이야기의 순서와 다르다.
- 분량이 내용과 맞지 않는다.

사용자가 짚은 섀도 재판정 글의 문제가 첫째와 둘째 항목에 그대로 들어간다. 고칠 때는 구성부터 정한다. 같은 일을 하는 절은 합치고, 덧붙은 문단은 그 동작을 설명하던 자리에 엮는다. 이어붙이는 문장 말고는 새로 쓰지 않는다. 사실을 더하지 않고, 멀쩡한 문장을 다듬지 않는다.

덜어내는 목록에는 집필 턴이 자주 남기는 것들이 적혀 있다. 줄 수나 파일 수, 바뀐 이름의 목록, 커밋을 주어로 삼은 서술, 그리고 글쓴이가 무엇을 확인했는지에 대한 말("diff에서 확인한 것은", 「확인한 범위」 같은 절)이다. 마지막 항목은 사용자가 같은 날 함께 요청한 것이다. 그 요청에 따라 `marvin.md`도 바뀌어, 집필 턴은 확인의 범위를 본문이 아니라 틱 끝의 보고에 적는다.

편집 턴에는 손대지 못하는 부분도 있다. `git blame`에서 Marvin이 쓴 줄이 아닌 곳은 옮기기만 하고 고치지 않는다. 사용자 발화 인용과 코드 블록의 내용, IAL도 그렇다. front matter는 한 글자도 건드리지 않고, 제목이나 excerpt가 글과 어긋나면 보고에만 적는다. 다른 글 한 편의 주제처럼 보이는 덩어리도 옮기거나 지우지 않고 그대로 둔 채 보고한다. 글을 만들고 없애는 것은 사용자가 정한다.

## 집필 판본으로 되돌리는 검사

편집자는 글의 구성을 통째로 바꿀 수 있다. 그 턴이 중간에 끊기거나 front matter를 건드린 채 끝나면 드라이버는 그 상태를 그대로 커밋하고, autopush가 배포한다. 그래서 `edit_guard.py --check`는 편집 뒤의 글이 세 조건을 모두 만족할 때만 남긴다.

```python
def problem(rel: str, store: Path) -> str | None:
    """편집 뒤의 글이 남아도 되는지. 안 되면 이유."""
    live = BLOG_ROOT / rel
    if not live.is_file():
        return "글이 없어졌다"
    old = (store / rel).read_text(encoding="utf-8")
    new = live.read_text(encoding="utf-8")
    if front_matter(new) != front_matter(old):
        return "front matter 가 바뀌었다"
    if len(new.encode("utf-8")) < MIN_SIZE_RATIO * len(old.encode("utf-8")):
        return "본문이 절반 아래로 줄었다"
    if "\n## " not in new:
        return "절 제목이 하나도 없다"
    return None
```
{: data-filename="scripts/blogdev-bot/edit_guard.py · 일부 발췌"}

`front_matter()`는 파일 첫머리의 `---` 블록을 그대로 잘라 낸다. 그래서 이 비교는 키별 검사가 아니라 문자열 일치이고, 공백 하나만 바뀌어도 걸린다. 편집은 덜어내는 일이 많으니 분량이 줄어드는 것은 허용하지만, 기준선 `MIN_SIZE_RATIO`는 0.5다. 절반 넘게 사라졌다면 덜어낸 것이 아니라 끊긴 것으로 본다. 마지막 조건은 절 제목(`\n## `)이 하나라도 남아 있는지다. 하나라도 어긋나면 `shutil.copy2`가 임시 디렉토리의 집필 판본을 그 자리에 덮어쓰고, 이유와 함께 로그에 `되돌림` 줄을 남긴다. 통과하면 `그대로`나 `편집됨`이 남는다.

이 검사는 형태만 본다. 편집 결과가 구성상 더 나은지는 판정하지 못한다. 그 판정은 편집자의 보고와 이후 사용자의 독해에 남는다.
