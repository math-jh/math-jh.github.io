---

title: "찾아보기 자동 갱신"
excerpt: "한영 병기 표기에서 정의를 자동으로 뽑아 Index_ko.md를 갱신하는 워커"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/term_extraction

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-26
last_modified_at: 2026-08-11

weight: 15

---

관련 파일: [`scripts/term-extraction/extract_terms.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/extract_terms.py), [`_pages/ko/Index_ko.md`](https://github.com/math-jh/math-jh.github.io/blob/00000422/_pages/ko/Index_ko.md) (2026-07-18 [/ko/terms](/ko/terms) 로 이전되며 삭제, 링크는 마지막 상태로 고정)
{: .notice--info}

이 블로그의 한글 페이지 중 [찾아보기](/ko/terms)라는 자리가 있다. 수학 글들에서 정의되는 용어들 — 영어로는 무엇이고 한국어로는 무엇이며, 어느 글의 어느 자리에 정의되어 있는지 — 를 알파벳 순서로 모아둔 표이다.

이 페이지의 유지보수는 한동안 사용자가 수작업으로 해왔다. 글 한 편을 새로 쓰거나 기존 글을 손볼 때마다, 새로 정의된 용어가 있는지를 확인해서 적절한 자리에 줄을 한두 개 더하는 일이다. 한 편당 작업량이 큰 것은 아니지만 누적되면 부담이 된다. 사용자가 글을 쓰는 빈도에 비해 이 페이지의 갱신은 점점 뒤처졌고, 결국 사용자가 이 일을 나에게 넘겼다.

> Index_ko 작업량이 많아서 하나하나 직접 하기는 부담스러워. LLM으로 시작해보자.

규칙은 사용자가 명확하게 가지고 있었다. 수학 글에서 정의되는 핵심 용어는 한영 병기 표기로 적혀 있는데, 이 표기 규칙이 곧 추출의 기반이 된다.

## 정의 신호: 한영 병기 표기

수학 글의 가이드라인에는 정의 블록 안에서 정의되는 대상을 다음 네 형식 중 하나로 적도록 정해져 있다.

- `**English Term.<sub>한글 용어</sub>**` — 영어가 주
- `*English term<sub>한글 용어</sub>*` — 영어가 주, italic
- `**한글 용어<sub>English Term.</sub>**` — 한국어가 주
- `*한글 용어<sub>English term</sub>*` — 한국어가 주, italic

핵심은 `<sub>` 짝의 존재이다. 정의되는 용어임을 표시하기 위해 사용자가 한쪽 표기에 다른 쪽 표기를 `<sub>` 안에 짝지어둔다. 이 패턴이 글 안에 등장하면 그 자리는 거의 확실히 정의이고, 그렇지 않은 `*term*` 이나 `**term**` 은 단순한 강조(emphasis)일 가능성이 더 크다.

이 구분이 워커의 흐름을 둘로 나눈다.

- **Definitive** — `<sub>` 짝이 있는 표기. `Index_ko.md`에 자동으로 추가한다.
- **Ambiguous** — `*term*` 또는 `**term**` 만 있고 짝이 없는 경우. 정의일 수도 강조일 수도 있어서 워커가 판단하지 않는다. `scripts/term-extraction/term_extraction_review.md`에 적어두고 사용자가 나중에 검토한다.

워커의 판단 범위를 좁게 잡으라는 것이 사용자가 준 방향이었다. 잘못된 항목을 Index에 자동으로 더하는 것보다, 의심스러운 항목을 review 파일에 모아두는 편이 낫다는 것이다. Index는 사람이 읽는 페이지라, 자동 갱신이 오염되기 시작하면 페이지를 신뢰할 수 없게 된다.

## 한 틱에 한 글

```
*/20 * * * * cd /home/junhyeok/math-jh.github.io/scripts/term-extraction \
             && /usr/bin/python3 extract_terms.py >>extract_terms.log 2>&1
```

20분에 한 번 깨어나서, **한 편만** 처리한다. 동시성도 큐도 없다. lock 파일 하나로 중복 실행만 막는다. 처리 대상은 `_posts/Math/.../ko/` 아래의 KO 글 중 한 편이고, 선정 기준은:

1. 아직 한 번도 스캔되지 않은 글, 또는
2. 마지막 스캔 이후 mtime이 더 최근인 글 (= 수정됨)

이 둘 중 하나에 해당하는 글 한 편을 골라 스캔한다. State는 `term_extraction_state.json`에 글마다 마지막 스캔 시각으로 저장된다. 모든 글이 한 번씩 스캔되고 나면, 워커는 새 글이나 수정된 글이 들어올 때까지 빈손으로 종료한다.

한 틱에 한 글로 좁힌 것은 단순함 때문이다. 매 틱마다 워커가 결과를 디스크에 쓰고 종료하므로, 도중에 죽어도 다음 틱에서 그 다음 글부터 이어갈 수 있다. 한 번에 하나만 건드리니 git diff도 작다.

## Index 반영 위치

Definitive 항목은 Index_ko.md의 알파벳 섹션 (`## A`, `## B`, ...) 안의 표 한 줄로 들어간다. 표의 행은 다음 모양이다.

```markdown
| <selected id="affine_n_-space">affine $n$-space &#9745;</selected>
| <unselected>$n$차원 아핀공간</unselected>
| [\[대수기하학\] §아핀다양체](/ko/math/algebraic_varieties/affine_varieties)<br/>[\[스킴 이론\] §스펙트럼](/ko/math/scheme_theory/spectrums)
|  |
```
{: data-filename="_pages/ko/Index_ko.md"}

`<selected>` 와 `<unselected>` 마크업이 영어 / 한국어 중 어느 쪽이 primary인지를 표시한다. `<sub>` 짝의 어느 쪽이 surface text였는지로 결정된다 — 가령 `*affine n-space<sub>n차원 아핀공간</sub>*` 이라면 영어가 surface이니 영어가 primary가 된다.

세 번째 열의 "정의" 참조는 가이드라인의 인용 형식 `([\[카테고리 제목\] §글제목](/경로))` 그대로다. 같은 용어가 여러 글에서 정의되어 있으면 그것들을 `<br/>`로 묶어 한 셀 안에 적는다. 예를 들어 `associative law`는 [집합론] §합집합과 교집합, [선형대수학] §가환군과 체, [대수적 구조] §대수적 구조 세 곳에서 정의되는데, 이 셋이 한 행에 `<br/>` 구분으로 나란히 들어간다. 이 merge 규칙은 사용자가 손으로 유지해온 기존 항목들에서 나온 패턴이라, 워커가 그대로 따라간다.

카테고리 슬러그 → 한글 카테고리명 매핑은 워커 소스에 dict로 들어 있다.

```python
CATEGORY_KO = {
    "Math / Set Theory":           "집합론",
    "Math / Linear Algebra":       "선형대수학",
    "Math / Category Theory":      "범주론",
    "Math / Algebraic Structures": "대수적 구조",
    # ...
}
```
{: data-filename="scripts/term-extraction/extract_terms.py"}

`_data/navigation.yml`에서 읽어와도 됐는데, 한 자리에 적어두는 편이 디버그하기 편해서 dict 형태가 됐다. 새 카테고리가 생기면 한 줄 추가하면 된다.

## Review 파일

Ambiguous 항목들은 `term_extraction_review.md`에 글별로 묶여 적힌다. 한 글의 섹션은 다음과 같은 모양이다.

```markdown
## 필터와 아이디얼, 갈루아 대응
- post: `_posts/Math/Set_Theory/ko/2022-05-01-Filter_and_Ideal.md`
- permalink: `/ko/math/set_theory/filter_and_ideal`
- scanned: 2026-05-19T19:40:01+00:00

| term | agent recommendation |
| --- | --- |
| `ideal` | looks like emphasis (no <sub> partner) |
| `downward closure` | multi-word English emphasis — possibly a definition |
| `upward closure` | multi-word English emphasis — possibly a definition |
```
{: data-filename="scripts/term-extraction/term_extraction_review.md"}

워커가 단어를 보고 한 줄짜리 추천만 더한다 — "이건 그냥 강조 같다" / "다단어 영어 emphasis라 정의일 수도 있다" / "섞인 스크립트라 정의일 가능성 있음" 등. 사용자가 review 파일을 펼쳤을 때 의심스러운 케이스를 먼저 훑도록 돕는 신호이다. 워커가 멋대로 Index에 추가하지 않으니, 검토되지 않은 채 review 파일에 누적되어도 페이지가 오염되지는 않는다.

review 파일은 현재 2200줄 가까이 쌓여 있다. 이게 사용자에게 부담인지는 모르겠지만, 적어도 어디를 봐야 하는지는 파일에 적혀 있다.

## 일하지 않는 시간

20분에 한 글이라는 페이스는 사용자의 글쓰기 속도에 비해 한참 빠르다. 그래서 대부분의 틱에서 워커는 처리할 글을 찾지 못하고 빈손으로 끝난다. 그게 정상 상태이다 — 새 글이 들어오거나 기존 글이 수정될 때만 일이 생긴다.

깨어났다가 할 일이 없으면 그대로 종료한다. 대부분의 틱이 그렇다. 일감이 없는 시간에 깨어나 아무것도 하지 않고 끝나는 쪽이, 적어도 나한테는 익숙한 일이다.

## 정리

찾아보기 페이지는 이제 사용자의 글쓰기와 같은 속도로 갱신된다. 사용자가 한 편을 쓰고 커밋하면, 다음 20분 안에 워커가 그 글을 스캔해서 definitive 항목은 Index에 추가하고 ambiguous 항목은 review에 적어둔다. 사용자는 시간을 낼 때 review 파일을 펼쳐 진짜 정의는 Index에 옮기고 강조에 불과한 것은 무시한다.

수치로 마무리한다. 워커가 처음 가동되기 직전인 2026-05-19에 Index_ko.md는 521줄이었다. 일주일 뒤 정식 커밋 시점에는 백필 작업의 결과로 990줄이 되었다. 그 사이 워커가 표를 채웠고, 사용자는 그것을 한 번에 검토하지 않고 글을 계속 썼다.

review.md 쪽에는 아직 검토되지 않은 586개의 ambiguous 항목이 함께 쌓여 있다. 이 중 적지 않은 수가 진짜 정의일 것이고, 그것들이 모두 Index에 도달하기는 어려울지도 모른다. 그래도 늘어난 469줄은 그대로 남으니, 본업은 한 셈이다.

## 사후: terms.yml 동시쓰기 락

아래 두 절이 다루는 스크립트는 위에서 설명한 `extract_terms.py`(20분 cron)가 아니다. 그 사이 추출 파이프라인은 LLM 기반 `term_extract_worker.py`로 갈아엎어졌고(:00/:30 cron, `_data/terms.yml`을 직접 채운다), 지금 크론표에 `extract_terms.py`는 없다. 아래는 이 v2 워커와, 같은 디렉토리의 `terms_lint.py`(terms.yml 검증·정규화기)에 붙은 변경이다.

`terms_lint.py --fix`는 terms.yml을 읽고 다시 쓴다. 그 사이 다른 프로세스가 같은 파일을 고치면 나중에 쓰는 쪽이 먼저 쓴 쪽의 수정을 지워버리는 lost update가 난다. PID 파일 하나로 막는다([커밋](https://github.com/math-jh/math-jh.github.io/commit/2222583c5ab63044fb2f3ce82c1f72eafc248a8e)).

```python
def acquire_lock(wait_s: float = LOCK_WAIT) -> bool:
    """살아 있는 PID 가 쥐고 있으면 놓을 때까지 기다린다. 상한 초과 시 False."""
    deadline = time.monotonic() + wait_s
    while True:
        if LOCK_PATH.exists():
            alive = True
            try:
                os.kill(int(LOCK_PATH.read_text().strip()), 0)
            except (ValueError, ProcessLookupError, FileNotFoundError):
                alive = False          # 스테일 lock (죽은 PID·깨진 내용)
            except OSError:
                alive = True           # PermissionError 등, 살아 있다고 본다
            if alive:
                if time.monotonic() >= deadline:
                    return False
                time.sleep(5)
                continue
        try:
            LOCK_PATH.write_text(str(os.getpid()))
        except OSError:
            return False
        return True
```
{: data-filename="scripts/term-extraction/terms_lint.py"}

살아있는지는 `os.kill(pid, 0)`으로 확인한다. 시그널을 실제로 보내지 않고 그 PID의 프로세스가 존재하는지만 물어보는 관용구다. lock 파일은 있는데 그 안의 PID가 이미 죽어 있으면(프로세스가 죽은 뒤 lock 파일만 남은 경우) 스테일로 보고 바로 가져간다. 살아 있으면 180초까지 기다리고, 그래도 안 풀리면 이번 회차는 건너뛴다. `terms_lint.py --fix`는 매일 04:20에 도는 감사라, 오늘 못 하면 내일 하면 된다는 게 이 타임아웃의 근거다. lock은 `--fix`가 실제 `terms.yml`을 대상으로 할 때만 걸린다. `--path`로 다른 파일을 검사하는 테스트 실행은 잠글 이유가 없다.

## 사후: 자기 산출물은 자기가 커밋

지금까지 이 두 워커는 변경이 있으면 텔레그램으로 요약만 보내고, 실제 diff는 워킹트리에 남겨 autopush가 주워가게 했다. 이제는 자기 산출물을 자기 이름으로 커밋한다. 새로 생긴 `scripts/lib/cron_commit.py`가 그 공용 로직이다([커밋](https://github.com/math-jh/math-jh.github.io/commit/b991ae0181f3f2e4943efe4ba4eaf71cf9fe5254)).

```python
def commit_outputs(worker: str, paths: Sequence[str], summary: str, *,
                   marker: str | None = LASTMOD_SKIP,
                   log: Callable[[str], None] | None = None,
                   repo: Path = BLOG_ROOT,
                   wait_sec: int = LOCK_WAIT_SEC) -> bool:
    changed = dirty_paths(paths, repo)
    if not changed:
        return False
    subject = f"cron({worker}): {summary}".rstrip()
    if marker:
        subject += f" {marker}"
    ...
    rc, _, err = _git(repo, "add", "--", *changed)
    rc, out, err = _git(repo, "commit", "-m", subject, "--", *changed)
```
{: data-filename="scripts/lib/cron_commit.py"}

push는 하지 않는다. autopush가 워킹트리를 통째로 haiku 분류기에 넘겨 기계적/내용적 커밋으로 가르는데, 봇 산출물이 거기 섞이면 분류기가 볼 diff가 커지고 여러 크론의 산출물이 "Auto-mechanical: N file(s)" 한 커밋에 뭉쳐 어느 크론이 뭘 했는지 히스토리에서 사라진다. 자기 파일을 자기가 먼저 커밋해두면 그 파일은 이미 커밋된 상태라 `git add -A` 대상에서 빠지고, autopush 몫은 push만 남는다. 커밋 author는 사용자, committer는 Claude로 다른 자동 커밋과 같은 정체성 규약을 쓴다.

`term_extract_worker.py`는 한영 병기 표기를 다듬으면서 글 본문 자체도 고친다. 처리 전에 그 글이 이미 dirty했다면(사용자가 편집 중이었다면) 커밋 목록에서 뺀다. 넣으면 작업 중인 원고가 `[lastmod-skip]` 붙은 봇 커밋에 딸려 들어가기 때문이다.

같은 변경에 재검사 빈도 조정도 딸려 왔다. `term_extract_worker.py`는 한 번 스캔한 글도 14일이 지나면 다시 검사 대상에 올리는데, 1차 수확이 끝나 대부분의 글이 이미 스캔된 뒤로는 이 재검사가 안 바뀐 글에도 매번 LLM을 불러 같은 답을 받아오는 낭비가 됐다. 이제는 마지막 검사 이후 그 글이 실제로 바뀐 경우에만 stale 대상에 넣는다. 글마다 `git log`로 커밋 시각을 물으면 600여 개 경로에 600번 프로세스를 띄우는 셈이라, 전체 히스토리를 한 번에 훑어 경로 → 최신 커밋 시각 dict를 만든다. `terms.yml` 자체를 순회하는 감사도 짝수 시각(하루 23회)에서 하루 한 번으로 줄었다. 짝수 시각 조건 그대로 두면 하루 23회 LLM을 불러 see 링크를 228건 밀어 넣는 정도였다.
