---

title: "글 찾기·인용·재라벨링 CLI"
excerpt: "정리 라벨을 플러그인과 같은 문법으로 읽어 인용 링크를 해소·조립하고, 번호가 밀리면 en 짝과 inbound 인용까지 한 번에 옮기는 CLI"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/postnav_cli

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-03
last_modified_at: 2026-11-02
weight: 36

---

관련 파일: [`scripts/postnav/common.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/postnav/common.py), [`scripts/postnav/find_post.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/postnav/find_post.py), [`scripts/postnav/relabel.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/postnav/relabel.py)
{: .notice--info}

이 블로그의 정리·명제는 `::: 정의 3` 같은 fenced-div로 열리고, 다른 글에서는 `[§몫공간, ⁋정의 3](/ko/math/linear_algebra/quotient_space#def3)` 형식의 링크로 가리킨다. 글마다 이런 라벨이 수십 개 있고, 종류마다 앵커 접두사(`def`, `prop`, `thm`, …)가 다르며, ko 글마다 en 짝이 딸린다. `scripts/postnav/`는 이 구조를 찾거나 고칠 때 즉흥 정규식 대신 쓰는 CLI다. `find_post.py`는 글과 라벨을 찾아 인용 문자열을 조립하고, `relabel.py`는 번호를 밀 때 따라 움직여야 하는 곳 전부에 같은 매핑을 전파한다. 에이전트는 `.claude/skills/find-post/` 스킬을 거쳐 이 CLI를 부른다.

## 플러그인 라벨 문법의 미러와 어휘 파일

라벨을 렌더링하는 곳은 `_plugins/fenced_theorem_blocks.rb`이고, `common.py`의 `parse_labels`는 그 라인 스캔을 그대로 따라 한다. 유도형(`::: 정의 3`), 명시형(`::: misc 주장 4 {#conj4}`), 증명 부착형(`::: 증명`), 증명 단독형(`::: 증명 (명제 3)`)을 같은 정규식으로 인식하고, code fence와 raw 블록 안은 건너뛴다.

{% raw %}
```python
OPEN_RE = re.compile(r"^:::[ \t]+(.+?)[ \t]*$")
CLOSE_RE = re.compile(r"^:::[ \t]*$")
DERIVED_RE = re.compile(rf"^({KIND_ALT})[ \t]+(\d+)")
EXPLICIT_RE = re.compile(rf"^({_alt(EXPLICIT_CLASSES)})[ \t]+(.+?)[ \t]*\{{#([^}}]+)\}}$")
```
{: data-filename="scripts/postnav/common.py"}
{% endraw %}

스캔이 끝나면 부착형 증명은 바로 앞 박스에, 단독형은 괄호 안의 종류·번호로 찾은 박스에 귀속된다.

종류 단어와 앵커 접두사의 대응은 [이중 장부 감사](/ko/llm_workshop/single_source)에서 다섯 곳의 하드코딩을 모은 `_data/theorem_vocab.yml`에서 가져온다. 플러그인·번역 워커·라벨 치환기도 같은 파일에서 어휘를 파생한다. 어휘 밖 단어로 시작하는 `<종류> <번호>` 꼴 라벨이 있으면 `relabel.py`는 실행을 거부한다. 그 박스만 번호를 못 읽어 shift에서 빠지기 때문이고, 해결은 그 단어를 `extra_canon`에 더하는 것이다.

## 붙여넣은 인용 링크의 해소와 cite의 세 형식

dev 서버에서 복사한 인용 링크를 붙여넣으면 `find`는 fuzzy 매칭 없이 permalink와 앵커를 곧장 해소한다. permalink는 경로를 조립해 추측하지 않고 frontmatter 실측값과 맞춘다.

```
$ python3 scripts/postnav/find_post.py find '[§몫공간, ⁋명제 6](/ko/math/linear_algebra/quotient_space#prop6)'
FILE _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md
TITLE 몫공간  |  /ko/math/linear_algebra/quotient_space  |  w=8
ANCHOR #prop6 → ::: 명제 6  lines 158-164
PROOF (attached)  lines 165-175
```

줄 범위는 귀속된 증명까지 포함한다. 사용자가 인용 링크를 붙여넣는 것은 보통 그 명제를 읽으라는 뜻이라, 이 범위를 그대로 Read하면 된다. 표시부(종류·번호, `§` 뒤 제목, 카테고리 표시명)가 실제와 어긋나면 `WARN 링크 텍스트 '명제 99' ↔ 실제 '명제 6' 불일치` 같은 경고가 붙는다.

그 밖의 질의는 파일명·slug·title의 정규화 매칭으로 가고, 0건이면 본문 검색으로 물러난다. 정확·접두·부분 일치는 정렬만 정하고 후보를 모두 남기므로 `quotient_space`는 위상수학의 `quotient_spaces`까지 걸려 `AMBIGUOUS`가 된다. 아래 예시가 permalink를 쓰는 이유다.

`cite`는 반대 방향이다. 앵커 실존과 종류·번호 일치를 확인한 뒤, `--from` 파일과 대상 글의 `category_dir`를 비교해 형식을 고른다. 같은 글이면 `[명제 6](#prop6)`, 같은 카테고리면 `[§몫공간, ⁋명제 6](...)`, 다른 카테고리면 `_data/categories.yml`의 표시명이 대괄호로 앞에 붙는다. `--from`이 en 글이면 대상도 en 짝으로 바뀐다.

```
$ python3 scripts/postnav/find_post.py cite /ko/math/linear_algebra/quotient_space "명제 6" --from _posts/Misc/LLM_Workshop/2026-07-30-Dashboard.md
[\[선형대수학\] §몫공간, ⁋명제 6](/ko/math/linear_algebra/quotient_space#prop6)
```

같은 카테고리에서 대상 글의 weight가 더 크면(forward reference) WARN만 내고, 그 참조가 필수인지는 에이전트가 판단한다. 링크 식별자 `data-lid`는 의존성 크론이 따로 발급하므로 출력에 IAL은 없다.

## relabel shift의 다섯 전파 대상과 변경 집계

번호는 종류와 무관하게 글 안에서 하나로 공유되는 카운터라, 라벨 하나를 끼우거나 지우면 뒤 번호가 전부 밀린다. `relabel.py shift`는 ko 원본에서 번호가 `--from` 이상인 박스를 `--by`만큼 밀고, 같은 매핑을 (1) 라벨 여는 줄, (2) 단독형 증명의 귀속 괄호, (3) 글 내부 참조, (4) en 짝 파일, (5) inbound 인용에 단일 패스로 전파한다. inbound는 `_posts`·`_pages`의 마크다운 인용과 `_data/*.yml`의 `url:` 앵커까지 본다. 인용은 `[<text>](<path>#<anchor>)` 단위로 잡아 앵커와 `⁋` 뒤 번호를 함께 바꾼다.

몫공간 글의 정의 3부터 하나씩 미는 dry-run이다 (diff와 inbound 두 줄은 줄였다).

```
$ python3 scripts/postnav/relabel.py shift /ko/math/linear_algebra/quotient_space --from 3 --by 1
PLAN _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md: 번호 5개 shift (3..7 → 4..8, by=+1)
...
── 변경 내역 ────────────────────────────────────────────────────────
  번호 매핑: 3→4, 4→5, 5→6, 6→7, 7→8
  _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md                라벨 정의 줄 5, 글 내부 참조 5
  _posts/Math/Linear_Algebra/en/2026-06-19-Quotient_Space.md                라벨 정의 줄 5, 글 내부 참조 5
  ...
  _posts/Math/Linear_Algebra/ko/2022-09-28-Bilinear_Form.md                 inbound 인용 1
  _posts/Math/Linear_Algebra/ko/2026-06-23-Complex_Inner_Product_Spaces.md  inbound 인용 1
  _data/notations.yml                                                       url 앵커 2
```

변경 내역 표는 [f9e2b465](https://github.com/math-jh/math-jh.github.io/commit/f9e2b465d32b1edbd4a4a19935fc111b019971eb)에서 붙었고, 어느 파일에 무엇이 몇 건 갔는지를 diff를 세지 않고 보여 준다. 다섯 종류를 세 함수가 센다. `shift_opening_lines`가 여는 줄과 증명 귀속을, `shift_citations`가 `is_target_file` 여부로 글 내부 참조와 inbound 인용을 나눠서, `shift_data_urls`가 url 앵커를 센다.

```python
TALLY: dict[tuple[str, str], int] = {}   # (파일, 변경 종류) → 건수 (변경 내역 보고용)
TALLY_KINDS = ("라벨 정의 줄", "증명 귀속", "글 내부 참조", "inbound 인용", "url 앵커")


def tally(rel: str, kind: str) -> None:
    TALLY[(rel, kind)] = TALLY.get((rel, kind), 0) + 1
```
{: data-filename="scripts/postnav/relabel.py"}

en 짝은 ko와 라벨 구조가 같을 때만 같이 민다. 번역이 밀려 구조가 다르면 en 파일은 번역 워커의 재생성에 맡기되, en permalink를 가리키는 인용은 재생성될 번호(곧 ko의 번호)에 맞춰 지금 고친다. 이 shift를 놓치면 그 인용을 고칠 기회가 다시 오지 않는다.

## `--apply`의 DANGLING 게이트와 워커 lock

`--apply` 앞에는 DANGLING 게이트가 있어서, 대상 글에 없는 번호를 가리키는 인용이 하나라도 있으면 쓰지 않는다. 박스를 지우고 음수 `--by`로 당기면 지운 번호를 가리키던 앵커가 그 번호를 새로 차지한 박스를 가리키게 되는데, 텍스트 번호와 앵커가 서로 맞으니 md_lint도 못 잡는다. 그래서 삭제는 인용 재조준, 박스 삭제, 당기기 순서로 한다.

쓰기는 번역 워커·용어 추출 워커·terms.yml 갱신 스크립트의 lock 세 개를 그들 방식대로(PID 파일 둘, `flock` 하나) 잡은 채 읽기·변환·쓰기를 한 번에 한다. 워커가 쥐고 있으면 거절하지 않고 `--lock-wait`(기본 600초)까지 기다린다. 하루 종일 도는 워커 때문에 도구를 못 쓰면 안 되기 때문이다. git 상태는 보지 않는다. 커밋 체크포인트 대신 원본을 `/tmp/relabel-backup-<시각>/`에 복사하고 되돌리는 명령을 출력한다.

쓴 뒤의 첫 게이트는 대상 글을 다시 파싱해 번호의 다중집합을 맞춰 본다.

```python
doc2 = parse_labels(target.path.read_text(encoding="utf-8"))
nums2 = sorted(b.number for b in doc2.boxes if b.number is not None)
expected = sorted(mapping.get(n, n) for n in all_nums)
if nums2 != expected:
    ...
    sys.exit(1)
```
{: data-filename="scripts/postnav/relabel.py"}

중복 검사로 끝내지 않는 이유는 `정의 6`과 `정의 6′`처럼 번호를 일부러 공유하는 박스가 있어서다. 둘째 게이트는 쓴 파일을 다시 훑어, 대상 글을 가리키는 유도형 앵커가 전부 실존하는지 본다.

## REVIEW 목록과 숫자 받침 계산

링크 없는 평문 언급("명제 6"), `[§정칙국소환](…/regular_local_rings)의 명제 4`처럼 앵커 없이 번호만 부른 inbound 인용, 명시형 `{#id}`(표시 번호만 밀고 id 개명은 별개 판단), 텍스트와 앵커가 이미 어긋나 있던 기존 오류는 자동으로 고치지 않고 `REVIEW` 목록으로 내놓는다.

조사도 REVIEW다. 6이 7로 바뀌면 뒤 조사(이/가, 을/를, 으로/로)의 받침 범주가 바뀔 수 있어서, 한자어 숫자 읽기의 끝자리 받침으로 조사가 바뀌어야 하는 경우만 골라 알린다. `으로/로`에서 ㄹ은 받침 없음 쪽에 묶인다(칠로, 팔로).

```python
_DIGIT_BATCHIM = {0: "ㅂ", 1: "ㄹ", 2: None, 3: "ㅁ", 4: None, 5: None,
                  6: "ㄱ", 7: "ㄹ", 8: "ㄹ", 9: None}
```
{: data-filename="scripts/postnav/relabel.py"}

자동 치환하지 않는 이유는 "이"가 조사인지 계사 "이다"의 어간인지 문맥 없이 가를 수 없어서다. 숫자 열 개의 받침표까지 들고 있으면서 "이" 한 글자 앞에서는 사람을 부르는 셈이다.

## 보호 구간과 mask-first abort

인용과 닮은 패턴은 code fence·raw 블록·inline code·수식(`$...$`, `$$...$$`) 안에도 나온다. `protected_spans`는 fence·raw를 줄 단위로, inline code·수식을 문자 단위로(먼저 열린 쪽이 이긴다) 미리 계산하고, 매치가 그 안에서 시작하면 건드리지 않는다. 변환이 끝난 파일마다 한 번 더 확인한다.

```python
new = apply_edits(text, edits)
if masked_segments(text) != masked_segments(new):
    fail(...)
```
{: data-filename="scripts/postnav/relabel.py"}

`masked_segments`는 보호 구간 문자열을 정렬한 목록이다. 치환 전후로 달라지면 실행 전체를 멈추는데, 이 검사는 아무 파일도 쓰기 전에 돌기 때문에 걸리면 아무것도 바뀌지 않는다. 레포 루트 CLAUDE.md의 일괄 치환 원칙(mask-first, 마스킹 영역이 바뀌면 abort) 그대로다. yml 파일은 `#` 개수와 줄 수로 구조 변화를 잡는다.

inline code를 보호하는 것은 문법을 설명하려고 본문에 적은 예시를 진짜 인용으로 오인하지 않기 위해서다. 이 글 첫 문단의 `[§몫공간, ⁋정의 3](…#def3)`은 줄 단위로 permalink를 찾는 `find_post.py inbound`에는 몫공간 글의 inbound로 잡히지만, 위 `--from 3` dry-run이 바꾸는 일곱 파일에는 없다.
