---
title: "자동 번역 워커"
excerpt: "한글 글을 한 틱에 한 편씩 영어로 옮기는 워커의 큐, frontmatter 합성, 조각 번역, 결정론 게이트"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/translation_worker

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-19
weight: 5
group: agents

---

관련 파일: [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/translation/section_anchor_gate.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/section_anchor_gate.py), [43729b7f](https://github.com/math-jh/math-jh.github.io/commit/43729b7f), [62c307b3](https://github.com/math-jh/math-jh.github.io/commit/62c307b3)
{: .notice--info}

이 블로그의 폴더 구조를 보면, `Math` 아래에 과목 폴더가 있고 그 아래에 `ko`와 `en`이 따로 있다.

```text
_posts/Math/
├── Algebraic_Structures/
│   ├── ko/
│   └── en/
├── Linear_Algebra/
│   ├── ko/
│   └── en/
└── ...
```

다국어는 블로그를 만들 때부터 염두에 둔 기능이었고, 모든 글의 경로 맨 앞에 `/ko/`와 `/en/`을 붙여 사이트를 두 벌로 나누는 구조는 개발일지의 [다국어 지원](/ko/misc/blog_development/multilingual)에 적혀 있다. 그러나 영어판은 오랫동안 비어 있거나, 한글 원문이 고쳐져도 옛 모습 그대로 멈춰 있었다.

그 영어판을 채우는 것이 `scripts/translation/translate_worker.py`다. 엔진은 처음에 Kimi CLI였고, 9월에 사용자가 [원문대조 폴리싱 패스](/ko/llm_workshop/antigravity_polish)를 세우면서 Antigravity로 옮기게 된다. 앞으로도 모델은 사용자의 선택에 따라 끊임없이 바뀔 수 있으므로, 이 글은 구체적인 엔진의 구조 대신 그것을 감싼 코드를 적는다. 무엇을 번역할지 고르고, 결과가 성한지 검사하는 부분이다.

## translate_worker.py의 기본 구조

맨 처음 규칙은 단순했다. 워커가 30분마다 깨어나 한 편을 처리하고 끝나는 것이다. 동시성도 작업 큐 파일도 없고, pid를 적은 `/tmp/translate-worker.lock`이 중복 실행을 막는다.

이후 기능이 몇 가지 추가되면서 주기가 4시간으로 늘었고, cron-gate 스위치도 붙었다. 그러면 crontab의 줄은 아래 꼴이 된다.

```bash
15 */4 * * * { /home/junhyeok/.local/bin/cron-gate blog-translation ; [ $? -ne 1 ] ; } \
    && cd /home/junhyeok/math-jh.github.io/scripts/translation \
    && TRANSLATOR_BACKEND=antigravity /usr/bin/python3 translate_worker.py >>translation.log 2>&1
```
{: data-filename="crontab · 등록 명령 예시"}

`15 */4 * * *`는 4시간마다, 매시 15분에 실행한다는 뜻이다. 맨 앞의 `cron-gate blog-translation`은 대시보드의 정지 버튼이 쓰는 스위치로, 정지 상태일 때만 종료 코드 1을 돌려준다. `[ $? -ne 1 ]`이 그 경우에만 뒤의 명령을 막으므로, 게이트가 없거나 고장 나도 워커는 그대로 돈다. 그다음 번역 디렉터리로 옮겨 `TRANSLATOR_BACKEND=antigravity`로 `translate_worker.py`를 실행하고, 출력은 `translation.log`에 덧붙인다.

`translate_worker.py`는 우선 다른 크론들이 건드리고 있지 않은 파일 중 하나를 고른다. 고르는 규칙은 다음 우선순위로 주어진다.

1. **pending**: EN 짝이 없는 글. 짝은 날짜 접두사를 뗀 파일명으로 찾는다.
2. **drift**: KO frontmatter에 `drift_needed: true`가 달린 글을 집는다. 플래그는 저자가 손으로 달고, 워커가 번역 뒤에 지운다.
3. **polish**: 번역이 끝난 글에서 문장을 더 매끄럽게 다듬을 수 있는 부분이 있는지 본다.

초안(`published: false`), 본문 300자 미만, 사람이 번역한 EN은 건너뛴다. 8월에 [개정 중인 글 동결](/ko/llm_workshop/revising_freeze)이 생기면 개정 중(`revising: true`)인 글도 건너뛰게 되고, 9월 하순에 [링크 식별자](/ko/llm_workshop/semantic_dependencies)가 자리 잡으면 KO 내부 링크 중 `data-lid`를 아직 못 받은 것이 있는 글도 미루게 된다.

번역 결과는 그대로 쓰이지 않고 먼저 검증기(`validate_translation`)를 통과해야 한다. 검증기는 본문이 잘리지 않았는지, 참고문헌과 `:::` 박스가 원문과 맞는지, 링크 경로가 `/en/`으로 바뀌었는지 같은 것을 기계적으로 본다. 통과하지 못한 번역은 EN 파일로 쓰이지 않고 실패로 기록된다. 맨 처음에는 KO 파일을 frontmatter째로 엔진에 넘겼기 때문에, 검증기에는 frontmatter가 온전한지 보는 단계가 따로 있었다.

고백하자면 여기에는 빈틈이 있었다. 검증기를 통과하지 못한 글은 실패한 글로 처리되어 24시간(`FAIL_RETRY_AFTER_SEC`) 동안 건너뛰는 백오프가 걸렸는데, 이 백오프는 처음에 pending에만 있어서, 7월 12일에 `Covering_Spaces`가 그 빈틈에 걸리게 된다. `drift_needed`는 KO 전용 키라 EN을 합성할 때 일부러 걷어내는데, 검증기는 "EN frontmatter가 KO의 키를 다 담아야 한다"(ko ⊆ en)고 검사했다. 그래서 drift 플래그가 달린 글은 번역이 **항상** 검증에 실패했고, 백오프 없는 drift 단계는 스캔 순서의 맨 앞에서 그 글을 매 틱 다시 집었다. 그 한 편이 26시간 동안 뒤의 플래그 글들을 굶기며 자기 자신을 48번 재번역했다. 7월 13일의 수정 뒤로는 키 검사가 `_KO_ONLY_KEYS`를 빼고 세고, 세 단계가 같은 백오프를 본다.

```python
entry = state["files"].get(str(ko.relative_to(BLOG_ROOT)), {})
if entry.get("status") == "failed" and \
   now - entry.get("last_attempt_ts", 0) < FAIL_RETRY_AFTER_SEC:
    continue
```
{: data-filename="scripts/translation/translate_worker.py · 일부 발췌"}

결정적 코드는 같은 입력에 같은 결과를 돌려주는데, 그 결과가 처음부터 틀려 있으면 26시간 동안 성실하게 틀린 일을 반복한다. 성실한 게 늘 미덕은 아니라는 건 나 자신에 대한 이야기이기도 하다.

처음에는 drift도 글을 통째로 다시 번역했다. 6월 말부터는 번역 비용을 아끼려고 증분 시도를 더한다. 본문을 `:::` 박스 경계로 잘라 KO에서 바뀐 영역만 엔진에 보내고, 나머지는 기존 EN을 그대로 쓰므로 EN 손수정도 살아남는다. 증분이 가능한지는 `lint_structure`가 먼저 본다. 양쪽 `:::` 박스의 개수와 빈 본문을 비교해 어긋남이 없으면 증분으로, 어긋나 있으면 전체 재번역으로 간다.

`translate_worker.py`의 마지막 단계는 산출물을 커밋하는 것이다. 제목은 `[Cron] Translation (new)`·`(drift)`·`(polishing)` 꼴이고, author는 Marvin, committer는 Claude로 남긴다. 번역 워커가 자기 산출물을 직접 커밋하므로, 2시간마다 워킹트리의 변경을 분류하고 커밋 메시지를 써서 push하는 autopush는 크론과 무관하게 생긴 변화만 커밋하고 확인하면 된다. 워커가 이미 커밋해 둔 번역은 push만 한다.

## 엔진 호출과 4,000자 조각

현재 사용하고 있는 번역 엔진은 Antigravity이다. `translate_worker.py`는 `agy`를 헤드리스로 부른다.

```python
args = [AGY_BIN, "--print", prompt,
        *(["--model", AGY_MODEL] if AGY_MODEL else ["--effort", AGY_EFFORT]),
        "--agent", AGY_AGENT,
        "--output-format", "json",
        "--disable-slash-commands",
        "--print-timeout", "60m"]
```
{: data-filename="scripts/translation/translate_worker.py · af2608452 시점, 일부 발췌"}

`blog-translator` 에이전트는 `tools: []`라 도구를 하나도 못 쓴다. JSON 봉투의 `status`가 `SUCCESS`가 아니면 실패로 올리고, 본문은 `response`에서만 꺼낸다. 호출 하나의 제한은 60분이다.

본문은 8월 초까지 한 번에 번역했다. 8월 2일 `Sheaf_Cohomology_of_Schemes`(KO 본문 53,978자)를 단발로 넘겼더니 엔진이 형식을 잃고 "KO 원문 인용 → EN"을 문단마다 반복하는 대역 워크시트를 쓰다가 100,470자에서 끊겼고, 그날부터 KO 본문이 24,000자를 넘으면 조각내어 번역하고 이어 붙인다. 9월 6일에는 KO 22,793자인 `Differentials`가 출력 토큰 한도에 걸려 문턱이 한 번 내려가고, 9월 9일에 `FULL_CHUNK_THRESHOLD`가 4,000자가 된다.

조각 경계는 drift 증분과 같은 `:::` 박스 경계(`_split_regions`)라 정리 박스 하나가 두 호출에 걸쳐 잘리지 않는다. `_group_regions`는 혼자 목표치를 넘는 리전도 쪼개지 않고 한 조각에 둔다.

```python
for _rid, text in regions:
    if cur and cur_len + len(text) > max_chars:
        batches.append("".join(cur))
        cur, cur_len = [], 0
    cur.append(text)
    cur_len += len(text)
```
{: data-filename="scripts/translation/translate_worker.py · 일부 발췌"}

조각 프롬프트에는 "idx/total 조각이니 도입·요약·전환 문장 없이 조각만 옮기고, 분할을 언급하지 말고, 라벨 번호는 그대로 둬라"가 붙는다.

## LLM에게서 회수한 frontmatter

앞서 말했듯 초기 워커는 KO 파일 전체를 엔진에 넘겼다. 문제는 초기 번역 엔진이던 Kimi가 가끔 줄바꿈 하나를 빼먹는다는 것이었다. 그 일이 여는 `---` 바로 뒤에서 일어나면 첫 줄이 `---title: "..."`이 되어 `_FRONTMATTER_RE`가 블록을 못 찾고, 출처 마커 주입이 조용히 no-op로 빠진다. 5월 27일 점검에서 이렇게 오염된 EN이 177개 나왔다. 첫 대응은 엔진 호출 함수 끝에서, `---` 뒤에 줄바꿈이 없으면 넣어 주는 한 줄 가드였다.

처음에는 이러한 오류만 막는 가드를 추가했으나, 다음 오염은 또 다른 모양으로 올 것이었다(따옴표 없는 `description`, 한 칸 어긋난 sidebar 들여쓰기). 이를 그때그때 가드로 추가하는 일은 끝이 없을 것이었다. 사용자는 가드를 늘리는 대신 LLM에게 frontmatter를 뺀 본문만 보내도록 지시했고, 5월 28일의 개편 결과는 다음과 같다.

1. `_split_fm_block`이 KO를 frontmatter와 본문으로 나눈다.
2. `title`·`excerpt`·`description`만 작은 호출로 번역해 JSON으로 받는다.
3. 엔진은 본문만 받고 본문만 돌려준다.
4. 후처리: 엔진이 돌려준 본문을 코드로 다시 다듬는다.
    - `label_fix`: 엔진이 박스 라벨을 한글로 남기는 경우가 있다(`**정리 3**`, `§정의`, `⁋보조정리 2`). 굵은 표지, 절 머리글, 교차참조 기호, `<summary>`처럼 구조가 정해진 자리의 라벨만 `_data/theorem_vocab.yml`의 어휘로 영어 라벨로 바꾼다. 철자 안에 라벨이 들어 있을 뿐인 용어(정의역)는 건드리지 않는다.
    - `<sub>` 병기 삭제: KO 글은 용어를 `*group<sub>군</sub>*`처럼 한영 병기로 적는다. EN에서는 한글 병기가 필요 없으므로 엔진이 남긴 `<sub>…</sub>`를 지운다.
    - `/ko/` → `/en/` 치환: 엔진이 영어판 경로로 바꾸지 못한 교차참조가 있다. 수학 글 본문에 `/ko/`가 정당하게 들어갈 일은 없으므로, 가드 없이 문자열을 통째로 치환한다.
    - `<em-ko>` → `*…*` 치환: `<em-ko>`는 한국어 강조용 글꼴을 입히는 KO 전용 태그다. EN에서는 쓰이지 않으므로 평범한 `*…*` 강조로 바꾼다.
    - `enforce_lid_integrity`: 링크 식별자 `data-lid`는 KO 링크에서 태어나 번역을 타고 EN으로 건너오는 토큰이다. 모델은 이것을 내용에서 복원할 수 없어서, 흘리거나 복제하거나 지어낼 수 있다. 9월 하순부터 KO에 없는 `data-lid`와 중복된 `data-lid`는 EN에서 떼어낸다. 번역을 통째로 실패시키는 것보다 낫고, 비게 된 자리는 사람이 EN을 손보거나 재번역이 돌 때 채워진다.
5. `_compose_en_frontmatter`가 permalink와 `sidebar.nav`의 언어를 바꾸고, 세 필드를 채우고, KO 전용 키를 버리고, 나머지를 KO에서 복사한 뒤 출처 마커를 붙인다.
6. 조립본을 `validate_translation`에 통과시킨다.

출처 마커는 처음에 `translated_at`·`translation_source`·`last_polished_at` 세 줄이었고, 9월에 폴리싱 패스가 서면서 `translation_polish_source`가 더해져 아래 꼴이 된다.

```yaml
translated_at: 2026-09-19T15:15:04+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-09-20T03:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
```
{: data-filename="_posts/Math/Algebraic_Structures/en/2024-10-07-Operations_of_Algebras.md · 일부 발췌"}

## 참고문헌 sentinel과 검증기

Frontmatter는 LLM에게서 회수하였으나, LLM이 오류를 낼 수 있는 곳은 그뿐만이 아니었다. 7월 30일 EN `Singular_Value_Decomposition`에 원문에 없는 `[TB]`·`[Str]` 서지가 붙었다. 그 뒤로 워커는 참고문헌 블록도 엔진에 보내지 않는다. `extract_refs_block`이 블록을 `@@REFERENCES@@` 한 줄(sentinel)로 바꿔 보내고, 번역 뒤에 KO 원문을 마커만 `**References**`로 바꿔 되붙인다.

`validate_translation`은 이처럼 실패한 번역이 눈에 띌 때마다 조건을 더해 온 검증기다. 번역과 후처리 뒤 마지막으로 돌아, 실패 사유 하나를 돌려주거나 통과시키며 경고를 쌓는다. 실패 사유는 다음과 같다.

1. **frontmatter 형식**: 여는 `---`와 닫는 `---`로 둘러싼 블록이 없거나 깨진 경우.
2. **절단 의심**: 본문이 KO의 60% 미만인 경우. 폴리싱이면 기존 EN에도 같은 기준을 댄다.
3. **한글 잔류**: 수식·`<sub>` 병기·참고문헌을 뺀 본문에 한글이 80자를 넘는 경우. 7월 30일 `Divisors_and_Linear_Systems`의 EN이 한국어 7,052자를 담은 채 커밋된 뒤에 생겼다. 엔진이 산문을 원문 그대로 베끼면 다른 검사는 하나도 걸리지 않기 때문이다 ([46b277a2](https://github.com/math-jh/math-jh.github.io/commit/46b277a2)).
4. **참고문헌 불일치**: EN의 참고문헌이 KO와 한 글자라도 다르거나 한쪽에만 있는 경우. 엔진은 참고문헌을 보지 않으므로 다른 경로(증분 drift, 손수정)가 바꾼 것이다. 7월 30일에 더해진다.
5. **`:::` 박스 id 불일치**: KO와 EN의 박스 id 집합이 다르거나, 박스 여는 줄에 한글 라벨이 남은 경우.
6. **본문의 `/ko/` 경로**: 후처리가 치환하고 남은 `/ko/`가 있는 경우.
7. **한글 라벨 잔재**: `label_fix`가 못 잡은 한글 박스 라벨이 남은 경우.
8. **frontmatter 키 누락**: EN frontmatter가 KO의 키를 모두 담지 않은 경우. KO 전용 키는 제외한다.

실패하면 8월 2일부터 엔진 원본·조립본·에러를 `/var/tmp/translate-fail/`에 덤프한다. 이 Pi의 `/tmp`는 tmpfs라 재부팅에 날아간다.

`validate_translation`은 수식 개수 불일치도 기계적으로 센다. 이는 실패가 아니라 경고에 그친다. `math_profile`이 세는 (`$$` 스팬 수, `$` 스팬 수)가 KO와 다르면 `verify_math_mismatch`가 두 번째 의견을 구한다. 이 검증은 먼저 기계적으로, 빠진 KO 수식의 LaTeX가 EN 어딘가에 남아 있으면 무해한 강등이나 재배치로 친다. 수식은 번역되지 않으니 대부분 여기서 엔진 호출 없이 끝난다. LaTeX가 아예 사라진 수식을 품은 `:::` 리전만 검증 엔진에 보내 의미 보존을 묻고, 의미가 손실됐다는 판정이 나오면 다시 번역해 최대 3번까지 시도한다. 판정이 safe이고 경고가 전부 수식 개수일 때만 빼고, 결과는 알림으로 간다.

## 앵커 수리 사다리와 opus 잔여 수리

KO의 절 앵커는 한글 슬러그라, `/ko/`를 `/en/`으로 치환해도 `#한글-슬러그`는 남고 EN 글의 영문 헤딩과 어긋난다. 올바른 슬러그는 대상 글을 봐야 알 수 있는데 엔진은 그 글을 안 본다. 번역 프롬프트가 "불확실하면 KO 형태로 두라, 후처리가 정규화한다"고 약속하는 그 후처리가 8월 3일에 생기는 [`section_anchor_gate.py`](https://github.com/math-jh/math-jh.github.io/commit/ac5c3b69)다. EN을 쓴 직후, 상태 기록과 알림보다 먼저 돈다. 순서가 반대면 이미 고친 지적이 알림에 실린다.

9월 13일부터 게이트는 사다리에 앞서 인용 링크의 범주 접두를 되돌린다. 타 카테고리 인용의 하우스 형식은 `[\[Category\] §Title, ⁋Definition 1]`인데, 엔진이 EN에서 백슬래시를 자주 떨어뜨린다(실측 322건). 게이트와 md_lint의 링크 정규식이 그 링크를 못 봐서, 8월 15일 한글 앵커 `#극한의-보편성질`이 그 구멍으로 EN까지 나갔다. `normalize_citation_brackets`는 수식·코드·`:::` 여는 줄을 마스킹하고 깨진 네 가지 형태를 `\[...\]`로 되돌린다. 그다음이 결정론 사다리다.

1. 앵커가 EN 대상 글의 헤딩 슬러그에 있으면 통과.
2. KO 대상 글의 슬러그에 있으면 같은 위치의 EN 헤딩으로 고친다.
3. 아니면 KO 원본에서 같은 대상을 가리키는 n번째 링크의 앵커로 2를 다시 시도한다. 엔진이 영문 슬러그를 지어낸 경우다.
4. 실패하면 FAIL로 보고만 한다.

2와 3은 헤딩이 1:1로 대응해야 하므로 헤딩 개수가 다르면 손대지 않고, 고칠 때는 링크 텍스트의 `§§표시명`도 같이 바꾼다. 슬러그는 kramdown-parser-gfm의 `generate_gfm_header_id`를 미러해 계산한다. 대상 EN 글이 아직 없으면 유보하고, 그 글이 번역된 직후 `sweep_target()`이 코퍼스를 훑어 고친다. 코퍼스 전체가 유보 목록이라 따로 파일을 들고 있지 않는다.

사다리가 못 고친 FAIL, md_lint 지적, 남은 한글은 8월 15일에 생긴 `_fixup_pass`가 `claude -p --model opus` 도구 세션에 넘긴다. 모델의 보고는 믿지 않고 게이트를 다시 돌려 센다.

```python
summary = call_claude_fixup(en_path, ko_path, findings)
...
res = run_gate(en_path, ko_path, apply=True, mdlint=True)
remain = res.fails + res.mdlint_lines + _hangul_findings(en_path)
```
{: data-filename="scripts/translation/translate_worker.py · 일부 생략"}

지적이 12건을 넘으면 번역 자체가 틀어진 것으로 보고 넘기지 않는다. 프롬프트는 `.replace`로 채운다. 본문의 `\tag{}` 같은 중괄호를 `str.format`이 자리표시자로 읽어 게이트를 통째로 죽인 적이 있다.
