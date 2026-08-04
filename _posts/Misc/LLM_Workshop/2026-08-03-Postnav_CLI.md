---

title: "글 찾기·인용·재라벨링 CLI"
excerpt: "정리·명제 인용 링크를 매번 손으로 조립하고 번호가 밀릴 때마다 grep으로 뒤쫓던 일을, 결정론적 CLI 세 개로 옮긴 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/postnav_cli

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-08-03
weight: 36

---

관련 파일: [`scripts/postnav/common.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/postnav/common.py), [`scripts/postnav/find_post.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/postnav/find_post.py), [`scripts/postnav/relabel.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/postnav/relabel.py)
{: .notice--info}

이 블로그의 정리·명제는 `::: 정의 3` 같은 fenced-div로 열리고, 다른 글에서 이를 가리킬 때는 `[§몫공간, ⁋정의 3](/ko/math/linear_algebra/quotient_space#def3)` 형식의 링크를 쓴다. 글 하나에 이런 라벨이 수십 개씩 있고, 카테고리마다 앵커 접두사(`def`, `prop`, `thm`, `lem`, `cor`)와 번역 짝이 딸려 있다. 이 구조를 가리키거나 고칠 때마다 즉흥 정규식을 짜는 대신 쓰라고 만들어진 것이 `scripts/postnav/`다. find_post는 글과 라벨을 찾아 인용 문자열을 조립하고, relabel은 번호 하나를 밀 때 따라와야 할 자리 다섯 곳에 같은 변경을 전파한다.

## 라벨 문법을 두 번 파싱하지 않는다

라벨을 실제로 렌더링하는 곳은 `_plugins/fenced_theorem_blocks.rb`다. `common.py`는 이 파일이 하는 라인 스캔을 그대로 미러링한다. 유도형(`::: 정의 3`), 명시형(`::: misc 주장 4 {#conj4}`), 증명 부착형(`::: 증명`), 증명 단독형(`::: 증명 (명제 3)`) 네 가지를 같은 정규식으로 인식한다.

{% raw %}
```python
OPEN_RE = re.compile(r"^:::[ \t]+(.+?)[ \t]*$")
CLOSE_RE = re.compile(r"^:::[ \t]*$")
DERIVED_RE = re.compile(rf"^({KIND_ALT})[ \t]+(\d+)")
EXPLICIT_RE = re.compile(rf"^({_alt(EXPLICIT_CLASSES)})[ \t]+(.+?)[ \t]*\{{#([^}}]+)\}}$")
```
{: data-filename="scripts/postnav/common.py"}
{% endraw %}

종류 단어(`정의`, `명제`, `정리`, …)와 앵커 접두사의 대응은 `_data/theorem_vocab.yml` 하나에서 가져온다. 이 파일은 [이중 장부 전수 감사](/ko/llm_workshop/sot_audit)에서 다섯 곳에 흩어져 있던 같은 어휘를 하나로 합친 결과물이고, postnav는 그 여섯 번째 소비자로 붙었다. 새 종류를 하나 더할 때 이 YAML만 고치면 렌더링·번역 워커·postnav가 전부 따라온다는 뜻이다.

## 붙여넣은 인용 링크를 결정론으로 되짚는다

사용자가 dev 서버에서 복사한 인용 링크를 그대로 붙여넣으면, `find` 서브커맨드는 fuzzy 매칭을 거치지 않고 permalink와 앵커를 곧장 해소한다.

```
$ python3 scripts/postnav/find_post.py find '[§몫공간, ⁋명제 6](/ko/math/linear_algebra/quotient_space#prop6)'
FILE _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md
TITLE 몫공간  |  /ko/math/linear_algebra/quotient_space  |  w=8
ANCHOR #prop6 → ::: 명제 6  lines 157-163
PROOF (attached)  lines 164-174
```

출력이 라벨 블록의 줄 범위를 귀속된 증명까지 포함해서 주는데, 사용자가 인용 링크를 붙여넣는 것은 보통 "이 명제를 읽으라"는 뜻이므로 이 줄 범위를 그대로 Read하면 된다. 링크의 표시 텍스트가 실제와 어긋나면 조용히 넘어가지 않고 경고를 낸다.

```
$ python3 scripts/postnav/find_post.py find '[§몫공간, ⁋명제 99](/ko/math/linear_algebra/quotient_space#prop6)'
...
WARN 링크 텍스트 '명제 99' ↔ 실제 '명제 6' 불일치
```

`cite` 서브커맨드는 반대 방향이다. 인용할 라벨을 지정하면 문자열을 조립해 주는데, 형식이 셋으로 갈린다. 같은 글 안이면 `[명제 6](#prop6)`, 같은 카테고리 다른 글이면 `[§몫공간, ⁋명제 6](...)`, 카테고리가 다르면 대괄호 카테고리 표시가 앞에 붙는다. 이 분기는 `--from`으로 넘긴 현재 파일과 대상 글의 `category_dir`를 비교해서 자동으로 정해진다.

```
$ python3 scripts/postnav/find_post.py cite quotient_space "명제 6" --from _posts/Misc/LLM_Workshop/2026-07-30-Dashboard.md
[\[선형대수학\] §몫공간, ⁋명제 6](/ko/math/linear_algebra/quotient_space#prop6)
```

카테고리 표시명은 `_data/categories.yml`에서 가져오므로 손으로 옮겨 적을 일이 없다. weight 역전(대상 글이 현재 글보다 뒤에 나오는 forward reference)이면 WARN을 내지만 막지는 않는다. 그게 필요한지는 [글 예시 컬링](/ko/llm_workshop/theorem_box_restyle) 같은 판단과 마찬가지로 에이전트 몫으로 남겨뒀다.

## 번호 하나가 밀면 다섯 자리가 따라 움직인다

라벨을 하나 끼워 넣거나 지우면 그 뒤 번호가 전부 밀리는데, 이 번호는 종류와 무관하게 전역으로 공유되는 카운터다. `relabel.py shift`는 이 전파를 다섯 자리에 단일 패스로 건다: (1) ko 글 내부의 정의 줄, (2) ko 글 내부 참조 링크, (3) 단독형 증명의 귀속 괄호, (4) en 짝 파일, (5) 다른 글에서 걸어온 inbound 인용.

실제 글로 dry-run을 돌려보면 이렇다. `Quotient_Space.md`의 명제 6·정리 7을 각각 7·8로 미는 경우:

```
$ python3 scripts/postnav/relabel.py shift _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md --from 6 --by 1
PLAN _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md: 2개 박스 shift (6..7 → 7..8, by=+1)
--- _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md
+++ _posts/Math/Linear_Algebra/ko/2026-06-19-Quotient_Space.md (shifted)
@@ -154,7 +154,7 @@
-::: 명제 6
+::: 명제 7
...
-$W=\ker L$로 두면 [명제 6](#prop6)에 의하여 ...
+$W=\ker L$로 두면 [명제 7](#prop7)에 의하여 ...
-위의 [정리 7](#thm7)과 [정리 5](#thm5)를 결합하면 ...
+위의 [정리 8](#thm8)과 [정리 5](#thm5)를 결합하면 ...

--- _posts/Math/Linear_Algebra/en/2026-06-19-Quotient_Space.md
+++ _posts/Math/Linear_Algebra/en/2026-06-19-Quotient_Space.md (shifted)
@@ -153,7 +153,7 @@
-::: Proposition 6
+::: Proposition 7
...
SUMMARY 파일 2개 변경 (dry-run — 쓰지 않음)
```

여는 줄과 글 내부 참조는 물론, en 짝 파일까지 같은 매핑으로 한 번에 밀린다. 이 예시에서는 inbound 파일이 바뀌지 않았는데, 실제로 이 글의 명제 6·정리 7을 걸어온 다른 글이 없었기 때문이다(같은 글의 정의 3을 걸어온 글은 넷 있지만 이번 shift 범위 밖이라 건드리지 않는다). inbound가 걸려 있었다면 그 파일의 인용 단위 안에서 앵커 번호와 텍스트 라벨을 동시에 치환하는 세 번째 diff가 이어졌을 것이다.

기본은 dry-run이고, `--apply`를 줘야 실제로 쓴다. 그때도 대상 파일이 git-clean인지부터 확인하고, 쓰기 직후 대상 글을 다시 파싱해서 번호 중복이 생기지 않았는지 사후 게이트를 건다.

```python
dirty = subprocess.run(["git", "status", "--porcelain", "--", *files], ...).stdout.strip()
if dirty:
    fail("대상 파일에 미커밋 변경 있음 — 커밋 체크포인트 후 재실행:\n" + dirty)
...
doc2 = parse_labels(target.path.read_text(encoding="utf-8"))
nums2 = [b.number for b in doc2.boxes if b.number is not None]
if len(nums2) != len(set(nums2)):
    print("ERROR shift 후 번호 중복 발견 — 즉시 확인 필요", file=sys.stderr)
    sys.exit(1)
```
{: data-filename="scripts/postnav/relabel.py"}

## 판단이 필요한 자리는 REVIEW로 미룬다

다섯 자리 전파가 전부 기계적으로 끝나는 것은 아니다. 링크 없이 "명제 6"이라고 평문으로만 언급된 자리, 명시형 라벨의 `{#id}` 자체(표시 번호는 밀지만 id 문자열까지 바꿀지는 별개 판단), 인용 링크 텍스트가 이미 앵커와 어긋나 있던 기존 오류. 이런 경우는 자동으로 고치지 않고 `REVIEW` 목록에 쌓아 사람 앞에 내놓는다.

조사 처리도 같은 이유로 REVIEW다. "6"이 "7"로 바뀌면 뒤따르는 조사(이/가, 을/를, 으로/로)의 받침 범주가 바뀔 수 있는데, 한자어 숫자 읽기의 받침을 계산해서 조사가 바뀌어야 하는 경우만 골라 알려준다.

```python
_DIGIT_BATCHIM = {0: "ㅂ", 1: "ㄹ", 2: None, 3: "ㅁ", 4: None, 5: None,
                  6: "ㄱ", 7: "ㄹ", 8: "ㄹ", 9: None}
```
{: data-filename="scripts/postnav/relabel.py"}

자동으로 갈아치우지 않는 이유는 "이"가 조사인지 계사("~이다") 어간인지 문맥 없이는 구분할 수 없어서다. 잘못 짚느니 사람에게 넘기는 편이 안전하다는 판단이 REVIEW 목록 전체를 관통한다.

## 보호 구간

인용 링크와 라벨 정의는 code fence·raw 블록·수식 `$...$`/`$$...$$` 안에도 우연히 비슷한 패턴으로 나타날 수 있다. `protected_spans`는 이 세 구간을 줄 단위/문자 단위로 먼저 계산해 두고, 치환 정규식이 이 구간과 겹치면 건드리지 않는다. `transform_file`은 쓰기 직전에 한 번 더 확인한다.

```python
if masked_segments(text) != masked_segments(new):
    fail(f"{post.rel}: 보호 구간(수식·fence)이 변경됨 — abort")
```
{: data-filename="scripts/postnav/relabel.py"}

보호 구간 앞뒤 문자열 집합을 통째로 비교해서, 치환 전후로 마스킹된 영역 자체가 달라졌으면 shift 결과를 버리고 즉시 중단한다. 레포 루트의 CLAUDE.md가 대량 치환 스크립트에 못 박아 둔 "mask-first, 마스킹 영역이 바뀌면 abort" 원칙을 그대로 따른 것이다.

## 정리

find_post와 relabel 둘 다 같은 세 가지를 공유한다. 어휘는 `theorem_vocab.yml`, 라벨 문법은 `fenced_theorem_blocks.rb`의 미러, 보호 구간은 mask-first abort. 손으로 grep을 짤 때마다 이 세 가지를 매번 다시 맞혀야 했던 것을, 이제는 CLI 하나가 대신 짊어진다. `.claude/skills/find-post/`는 이 CLI를 감싸는 스킬로, "즉흥 grep을 짜지 말고 CLI를 쓸 것"이라고 못박아 둔다.
