---

title: "excerpt·description 재작성 스윕"
excerpt: "수학 글의 부제와 검색 설명문을 모델이 제안하고, 사람이 검수한 값만 front matter에 적용하는 두 스크립트"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/frontmatter_rewrite

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-23
weight: 79
group: agents

---

관련 파일: [`scripts/sweeps/frontmatter_rewrite.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/frontmatter_rewrite.py), [`scripts/sweeps/frontmatter_apply.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/frontmatter_apply.py), [`scripts/sweeps/frontmatter_rewrite.prompt.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/frontmatter_rewrite.prompt.md), [`scripts/sweeps/frontmatter_rewrite.english.prompt.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/frontmatter_rewrite.english.prompt.md) ([91393477](https://github.com/math-jh/math-jh.github.io/commit/91393477ac48384d746563c572a6d8cd445d2bd9), [45c58d95](https://github.com/math-jh/math-jh.github.io/commit/45c58d9584201d97b9002b4fa78990cc798e120e), [832cb986](https://github.com/math-jh/math-jh.github.io/commit/832cb9863699b0bb5536bb3ddd98d2658eedff11))
{: .notice--info}

사용자는 11월 22일 저녁에 구글·네이버·빙의 웹마스터 도구를 열어 놓고 블로그의 검색 유입을 점검했다. 영어판은 잘 올라가지 않고 한글판 위주로 노출된다는 판정이 앞서 있었고, 그 점검 끝에 한글 글의 `excerpt`와 `description`을 손보는 일이 남았다.

> 근데 메타 설명문은 이미 excerpt가 그 역할을 하는거라 생각해.

> 그리고 지금 excerpt랑 description도 약간 수정하는게 도움이 될 것 같은데, antigravity hydrogen 돌리면 적절할 것 같고. 근데 프롬프트나 이런건 어떻게 하는게 좋을지 잘 모르겠네

대상은 `_posts/Math` 아래 한글 글 전부이고, 미발행 글도 포함한다. 편수가 많아 한 편씩 사람이 고칠 수는 없고, 모델에 통째로 맡기면 용어 표기가 글마다 어긋난다. 그래서 일을 셋으로 나눴다. 글에서 재료를 뽑아 모델에 묻는 `frontmatter_rewrite.py`, 그 결과를 사람이 읽을 대조표로 쓰는 `report`, 검수가 끝난 값만 글에 쓰는 `frontmatter_apply.py`다. 사용자는 이 구성을 받은 뒤 순서를 정했다.

> 1번부터 하고, 2번 대조표는 opus medium으로 검수. 글 제목과excerpt/description만 보고 우선적으로 판단하되, 확신이 없다면 글 내용 읽는 것도 허용, 단, 전제는 제미나이가 글 내용은 잘 뽑았고, 오직 용어 선택에서만 실수했다 가정하는 것이므로 글 내용 읽는 것은 최소화해야함.

## 모델에 주는 재료

모델은 도구 없이 문장 두 개만 돌려준다. 글을 읽거나 검색하는 일은 스크립트가 먼저 하고, 그 결과를 프롬프트의 자리표시자에 채워 넣는다. 모델에 가는 재료는 제목, 과목, 지금의 두 필드, 소제목, 이름이 붙은 정리, 본문 앞 1500자, 그 글의 용어표, 그 글 주제의 검색어 후보다.

길이 기준은 상수로 둔다.

```python
EXCERPT_RANGE = (10, 45)
DESCRIPTION_RANGE = (70, 110)
```
{: data-filename="scripts/sweeps/frontmatter_rewrite.py · 일부 발췌"}

이 범위는 프롬프트에도 `{e0}`~`{d1}`로 들어가고, 뒤에서 결과를 검사할 때도 같은 값을 쓴다.

용어표를 만드는 `term_table`이 이 스크립트에서 가장 신경 쓴 부분이다. 사용자가 걱정한 것은 모델이 글 내용은 잘 요약하지만 용어를 제멋대로 옮기는 일이었고, 그래서 한글 표기가 확정된 용어는 모델에 정답으로 주어야 한다. 표에는 세 곳의 용어가 들어간다. `_data/terms.yml`에서 이 글의 permalink를 `defs`로 가리키는 항목, 영어 표기가 본문에 나오는 항목, 본문에서 `*영어<sub>한글</sub>`꼴로 병기한 용어다. 이 글에서 정의한 용어가 앞에 오고, 나머지는 본문에 많이 나온 순으로 45개까지 자른다.

본문에 나오는 횟수를 셀 때는 긴 표기부터 세고, 센 자리를 공백으로 지운다.

```python
for e in sorted(all_terms(), key=lambda e: -len(str(e.get("en") or ""))):
    ...
    body, hits = re.subn(rf"(?<![A-Za-z]){re.escape(en)}(?:e?s)?(?![A-Za-z])", " ", body, flags=re.I)
    if hits:
        used.append((hits, en, ko))
```
{: data-filename="scripts/sweeps/frontmatter_rewrite.py · 일부 생략"}

`(?<![A-Za-z])`와 `(?![A-Za-z])`는 영어 낱말의 앞뒤에 알파벳이 붙어 있지 않을 때만 일치시키라는 뜻이고, 가운데의 `(?:e?s)?`는 복수형 `s`·`es`를 같은 용어로 센다. 긴 것부터 세는 이유는 `order relation`을 먼저 지우지 않으면 그 안의 `order`가 따로 한 번 더 세지기 때문이다. 수식 안은 `$...$`를 미리 공백으로 바꿔 두어 세지 않는다.

## 검색어 후보와 자동완성

사용자가 요청한 목적은 검색에서 찾히게 하는 것이어서, 모델에는 사람들이 실제로 치는 검색어도 준다. `search_candidates`는 글 제목을 쉼표·가운뎃점·`과`/`와`로 쪼갠 낱말과, 이 글이 정의한 한글 용어(본문에 나오는 순서대로 5개까지)를 씨앗으로 삼아 최대 7개를 고른다. 씨앗마다 `seed`와 `seed `(끝에 공백을 붙인 것)를 구글과 네이버 자동완성에 물어 합친다.

자동완성이 돌려준 것을 모두 후보로 쓰지는 않는다. 두 조건을 통과해야 한다.

```python
for s in suggest(seed, cache):
    if squash(seed) not in squash(s) or squash(s) == squash(seed) or s in out:
        continue
    if all(t in MODIFIERS or squash(t) in body for t in s.split()):
        out.append(s)
```
{: data-filename="scripts/sweeps/frontmatter_rewrite.py · 일부 발췌"}

후보는 씨앗을 포함하되 씨앗과 같으면 안 되고, 후보를 이루는 낱말은 `MODIFIERS`(정의, 증명, 필요충분조건, 반례 같은 검색 수식어 목록)에 있거나 글 본문에 나와야 한다. 본문에 없는 낱말이 붙은 검색어는 그 글이 답하는 질문이 아니므로, 설명문에 넣으면 글에 없는 내용을 약속하게 된다. 자동완성 응답은 `FM_WORK/ac-cache.json`에 쌓아 두고, 여러 글이 동시에 돌아도 자동완성은 락을 잡고 한 번에 한 글씩만 묻는다.

## 프롬프트의 KEEP 판단

프롬프트는 [`frontmatter_rewrite.prompt.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/frontmatter_rewrite.prompt.md)에 있고, 스크립트는 자리표시자만 채운다. 규칙의 첫머리가 고치는 법이 아니라 고치지 않는 조건이다. 지금 것이 기준을 모두 채우면 모델은 `KEEP`이라고 답한다. 한글 용어로 적혀 있는지, 이 글이 정의하거나 증명하는 것 중 이름으로 찾는 것이 드러나 있는지, 길이가 기준 안인지, 검색어 후보 중 글과 맞는 것이 들어 있는지, 이름이 기호로만 적혀 있지 않은지를 본다. 고칠 때도 지금 문장에서 살릴 수 있는 부분은 살리라고 적어 두었다. 수정 대상이 수백 편이라 표현만 바꾸는 수정이 섞이면 검수자가 읽을 양이 늘기 때문이다.

excerpt는 제목만 되풀이하지 않고 정의·정리 이름이 드러나게, description은 첫 문장에 중심 대상을 쓰고 정의·증명·계산 중 무엇인지 밝히게 한다. 수식, `$`, 큰따옴표, 콜론, 줄바꿈은 둘 다 금지다. 출력은 `<<<EXCERPT`와 `<<<DESCRIPTION` 두 블록뿐이어서 `parse`가 정규식으로 뽑는다. 블록이 없으면 그 글은 실패로 기록된다.

호출은 `agy`(Antigravity CLI)에 모델 `gemini-4-hydrogen-high`와 도구 없는 에이전트 `blog-translator`를 지정해 한 번씩 보낸다.

## 모델 결과의 검사와 대조표

모델이 돌려준 값은 `check`가 사람이 볼 표시로 바꿔 줄 뿐 자동으로 버리지 않는다. 길이가 기준 밖인지, `$`·큰따옴표·줄바꿈·콜론이 있는지, 한글이 아예 없는지, excerpt가 제목과 같은지를 보고, 하나 더 본다.

```python
alien = sorted({str(e["ko"]) for e in all_terms()
                if e.get("ko") and "$" not in str(e["ko"]) and len(squash(str(e["ko"]))) >= 3
                and squash(str(e["ko"])) in squash(value) and squash(str(e["ko"])) not in known})
if alien:
    flags.append("글에 없는 용어: " + ", ".join(alien))
```
{: data-filename="scripts/sweeps/frontmatter_rewrite.py · 일부 발췌"}

`terms.yml`의 한글 용어 중 제안문에는 있는데 글 본문·제목·지금의 두 필드·용어표 어디에도 없는 것을 찾는다. 모델이 글에 없는 개념을 끌어와 설명문을 부풀렸을 때 걸리는 검사다. 글에 있는지는 공백을 지운 문자열의 포함 여부로 보므로, 어느 정도 어긋난 표기까지 잡히는 대신 3자 미만의 짧은 용어는 검사하지 못한다.

`propose`는 글마다 결과를 `FM_WORK/<경로 해시>.json`에 저장하고, 이미 결과가 있는 글은 건너뛰며 실패한 글만 다시 묻는다. `--jobs`로 동시 호출 수를 정하고, 한 편이 실패해도 나머지는 계속한다. `report <출력.md>`는 쌓인 JSON을 글별로 지금 값과 제안, 표시, 검색어 후보를 나란히 놓은 마크다운으로 쓴다. 사용자가 opus medium에게 맡긴 검수는 이 표를 읽는다.

## 영어 용어를 그대로 두는 과목

한글 용어표를 정답으로 주는 방식은 대학원 과목에서 맞지 않았다. 이런 글은 본문이 `perfect obstruction theory`나 `stable map`을 영어로 쓰는데, 프롬프트가 용어표의 한글을 쓰라고 하면 부제만 혼자 번역어를 쓰게 된다. 그래서 이후 환경변수 `FM_PROFILE=english`로 고르는 프로필이 더해졌다 ([45c58d95](https://github.com/math-jh/math-jh.github.io/commit/45c58d9584201d97b9002b4fa78990cc798e120e)).

프로필이 `english`이면 프롬프트 파일이 `frontmatter_rewrite.english.prompt.md`로 바뀐다. 이 프롬프트는 본문이 영어로 쓰는 용어와 인명을 본문 표기 그대로 두고, 한글로 쓰는 것은 용어표에 있는 용어와 본문이 이미 한글로 쓰는 말뿐이며, 문장의 뼈대(조사, 서술어)만 한국어로 쓰라고 한다. 용어표도 좁힌다.

```python
if PROFILE == "english" and e.get("primary") != "ko":
    continue
if any(d.get("url", "").rstrip("/") == post["permalink"] for d in e.get("defs") or []):
    defined.append((en, ko))
    continue
if PROFILE == "english":
    continue
```
{: data-filename="scripts/sweeps/frontmatter_rewrite.py · 45c58d95 시점, 일부 생략"}

`terms.yml`에서 한글이 확정된 항목(`primary: ko`)만 남기고, 그중에서도 이 글이 `defs`로 가리키는 것만 쓴다. 본문에 영어로 나오는 다른 용어까지 한글 표를 만들어 주면, 영어 그대로 두려는 용어에 다른 뜻의 한글이 끌려오기 때문이다. 일반 프로필의 "본문에 많이 나오는 용어" 목록은 이 프로필에서 만들지 않는다.

그 뒤에는 이 기준이 `<sub>` 병기 용어에도 적용되었다 ([832cb986](https://github.com/math-jh/math-jh.github.io/commit/832cb9863699b0bb5536bb3ddd98d2658eedff11)). 병기는 영어 옆에 한글을 곁들였을 뿐이라 한글 확정을 뜻하지 않는다. 그래서 `english` 프로필에서는 병기한 용어도 `terms.yml`에서 `primary: ko`인 것만 용어표에 올리고, 나머지는 영어로 남긴다.

## 검수본의 적용

검수가 끝난 값은 `frontmatter_apply.py`가 쓴다. 입력은 제안을 검수해 합친 JSON으로, 글마다 `excerpt`와 `description`의 `old`(검수 때 본 값), `final`(확정값), `source`(출처)를 담는다. `source`가 `제안`이나 `검수 수정`인 필드만 바꾸고, `그대로`와 `되돌림`은 건드리지 않는다. 기본은 dry-run이어서 바뀔 글 수와 필드 수, 건너뜀과 문제의 수를 출력하고 끝난다. 쓰려면 `--apply`를 붙인다.

글의 front matter를 YAML로 다시 직렬화하면 들여쓰기·따옴표·키 순서가 달라져 diff가 커진다. 그래서 파일을 줄 단위로 다루고, 바뀌는 키가 차지하는 줄 범위만 새 줄로 바꾼다.

```python
def key_block(lines, key):
    """front matter 줄 목록에서 key 가 차지하는 줄 범위 [start, end)."""
    for i, line in enumerate(lines):
        if line.startswith(key + ":"):
            j = i + 1
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
                j += 1
            while j > i + 1 and not lines[j - 1].strip():
                j -= 1
            return i, j
    return None
```
{: data-filename="scripts/sweeps/frontmatter_apply.py · 일부 발췌"}

키 줄 아래로 들여쓴 줄(여러 줄 값의 이어짐)과 빈 줄을 같은 키의 일부로 보고 범위에 넣되, 끝에 매달린 빈 줄은 도로 뺀다. 키가 아예 없는 글, 곧 `description`이 없던 글에는 `excerpt`, `description`, `title` 중 먼저 있는 키 바로 아래에 새 줄을 넣는다. 새 값은 `quoted`로 큰따옴표 문자열로 쓴다.

쓰기 전에 거는 안전장치는 세 겹이다. 하나, 글의 지금 값이 검수 때 본 `old`와 다르면 그 필드는 건너뛰고 문제로 보고한다. 검수하는 사이 사용자가 글을 직접 고쳤을 때 그 수정을 덮어쓰지 않기 위해서다. 이미 `final`과 같은 값이면 "이미 적용됨"으로 건너뛴다. 둘, 새 front matter를 `yaml.safe_load`로 다시 파싱해 두 키가 적용안과 같은지, 그 밖의 키는 하나도 바뀌지 않았는지 확인한다. 셋, 본문이 바이트 단위로 같은지 확인한다. 둘째나 셋째가 어긋나면 `SystemExit`으로 끝나고 아무 파일도 쓰지 않는다. 같은 글이 입력에 두 번 들어 있어도 중단한다. 실제로 쓸 때는 바뀌기 전의 줄을 `FM_BACKUP`(기본 `/var/tmp/blog-frontmatter-apply-backup.json`)에 글별로 남긴다.

검수본은 11월 23일 오후에 적용되었다 ([0bc33895f](https://github.com/math-jh/math-jh.github.io/commit/0bc33895f)). 적용 커밋에는 `[lastmod-skip]`이 붙어 글의 수정일은 움직이지 않았다. 적용 결과로는 `Grothendieck group과 정수의 정의`가 `그로텐디크 군과 정수의 정의`로, `Direct product of groups`가 `군들의 곱과 보편 성질, 직접곱군의 구성`으로 바뀌는 식이었고, description은 기존 문장에 글이 실제로 다루는 내용을 한 문장 덧붙이는 경우가 많았다.
