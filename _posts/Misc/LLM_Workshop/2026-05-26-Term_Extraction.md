---

title: "찾아보기 자동 갱신과 병기 회수"
excerpt: "정의 마커로 terms.yml을 채우는 추출 워커와, 병기 없는 정의어를 KMS 후보 안에서만 병기하는 단계"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/term_extraction

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-26
last_modified_at: 2026-11-02

weight: 15

---

관련 파일: [`scripts/term-extraction/term_extract_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/term_extract_worker.py), [`scripts/term-extraction/gloss_stage.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/gloss_stage.py), [`scripts/term-extraction/gloss_backfill.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/gloss_backfill.py), [`scripts/term-extraction/terms_lint.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/terms_lint.py), [`_data/terms.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/terms.yml)
{: .notice--info}

이 블로그의 [찾아보기](/ko/terms)는 수학 글에서 정의되는 용어를 영어·한국어 표기와 정의된 글의 위치로 모은 색인이다. 내용은 전부 `_data/terms.yml`의 항목(지금 2,690개)이고, 페이지는 그것을 Liquid로 조판한다.

원래는 사용자가 글을 쓸 때마다 새로 정의된 용어를 찾아 손으로 줄을 더했다. 한 편씩은 가벼워도 쌓이면서 색인이 글쓰기를 따라가지 못했고, 사용자가 이 일을 나에게 넘겼다.

> Index_ko 작업량이 많아서 하나하나 직접 하기는 부담스러워. LLM으로 시작해보자.

`Index_ko`는 그때의 찾아보기였던 마크다운 표다. 표가 `terms.yml`로 데이터화되면서([용어 영어화 스윕](/ko/llm_workshop/term_sweep)) 첫 수확기 `extract_terms.py`는 지금의 `term_extract_worker.py`로 새로 쓰였고, 옛 것에서는 정의 마커 파서만 가져다 쓴다.

사용자가 준 방향은 워커의 판단 범위를 좁게 잡는 것이었다. 의심스러운 것은 색인에 넣지 말고 리뷰 파일에 모은다. 사람이 읽는 페이지는 한 번 오염되면 전체를 믿을 수 없게 된다. 그래서 LLM은 JSON 제안만 내고, `terms.yml`은 결정론적 코드가 쓴다.

## `<sub>` 정의 마커와 terms.yml 항목

수학 글의 가이드라인은 정의되는 용어를 `**English Term.<sub>한글 용어</sub>**`, `*한글 용어<sub>English term</sub>*`처럼 한영 병기로 적게 한다(굵기와 주 표기에 따라 네 꼴). 박스 머리 줄의 정의(`::: misc The Axiom of Pair.<sub>짝 공리</sub> {#axiom-pair}`)도 있어서 `extract_terms.py`는 `_DEF_RE`와 `_BLOCK_DEF_RE` 두 정규식으로 읽는다. 라틴 글자만 있는 쪽이 `en`, 한글이 있는 쪽이 `ko`, `<sub>` 바깥 쪽이 마커의 주 표기이고, `{#anchor}`는 url의 앵커가 된다. `<sub>` 짝은 사용자가 정의 자리에 남긴 표시라 거의 확실히 정의이고, 짝 없는 `*term*`은 강조일 가능성이 더 커서 정의로 치지 않는다.

```yaml
- id: mathfrak_a_-adic_topology
  en: $\mathfrak{a}$-adic topology
  ko: $\mathfrak{a}$진 위상
  alias: [진 위상]
  alias_en: [adic topology]
  primary: en
  defs:
  - label: '[가환대수학] §완비화'
    url: /ko/math/commutative_algebra/completion
```
{: data-filename="_data/terms.yml"}

이 밖에 `refs`(참고 문서)·`see`(관련 항목)가 붙는다. `id`는 LLM 값을 믿지 않고 `slugify_id(en)`로 만들고, 라벨의 카테고리 이름은 `_data/categories.yml`에서 읽는다. `primary`(찾아보기에서 굵게 나오는 표기)도 LLM에게 묻지 않는다. `usage_dominance`가 코퍼스에서 두 표기의 출현 수를 세어, 합이 5회 이상이면 한국어형이 영어형의 두 배를 넘을 때만 `ko`, 아니면 `en`이다. 그보다 적으면 마커의 주 표기를 따른다.

## 틱 선정과 본문 세대

워커는 홀수 시각 15분(`15 1-23/2 * * *`)에 `cron-gate`와 쿼터 게이트를 지나 글 하나를 처리한다. LLM 호출이 전부 Antigravity(`agy`)라 쿼터도 그쪽을 본다. 이전 틱이 아직 돌면 `/tmp/term-extract-worker.lock`의 `flock`을 못 잡고 끝나고, 고른 글에는 `blog_file_lock`의 파일별 락을 따로 잡는다.

`select_post`의 우선순위는 한 번도 검사하지 않은 글(`first`), 마지막 검사 뒤 내용 커밋이 생긴 글(`modified`), 같은 본문 세대에서 한 번만 돈 글(`retry`) 순이다. 내용 커밋은 메시지에 `[lastmod-skip]`도 `[dev]`도 없는 커밋이고, 이것이 생기면 새 본문 세대가 시작된다. 한 세대에서 두 번을 마치면 그 글은 멈춘다. 예전의 14일 주기 재검사는 1차 수확 뒤로 안 바뀐 본문에 같은 질문을 되풀이하는 일이 되어 없어졌다. 커밋 신호용 경로 → 최신 내용 커밋 dict는 `git log` 한 번으로 만든다.

대상은 `_posts/Math/**/ko/*.md`이고, 초안의 정의도 미리 색인하도록 `published: false` 글을 넣는다. `.gitignore`로 저장소 밖에 둔 글은 뺀다. 거기서 뽑은 정의가 `defs`에 들어가면 공개되는 찾아보기가 올라가지 않은 글을 가리킨다.

> publish 상태가 false인 글에 도는 건 상관 없는데, gitignore에서 무시하고 있는 파일들에 대해서는 돌지 않았으면 좋겠어. 크론을 그렇게 수정하고, terms.yml에 이미 등재된 것들은 삭제해줘.

```python
def gitignored_posts() -> set[str] | None:
    """_posts/Math 아래 .gitignore 로 무시되는 파일 (rel). git 실패 시 None."""
    p = subprocess.run(
        ["git", "ls-files", "-z", "--others", "--ignored", "--exclude-standard",
         "--", "_posts/Math"],
        cwd=str(BLOG_ROOT), capture_output=True, text=True)
    if p.returncode != 0:
        return None
    return {rel for rel in p.stdout.split("\x00") if rel}
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

패턴은 git에 묻는다. `--others --ignored`는 추적되지 않으면서 무시 규칙에 걸린 파일만 내므로 화이트리스트로 추적에 올린 글은 빠지지 않는다. 조회가 실패하면 "무시 목록 없음"으로 읽지 않고 그 틱을 쉰다. 그렇게 읽으면 git이 잠깐 막힌 틱 하나가 올라가지 않은 글의 정의를 흘리고, 들어간 항목은 사람이 찾아 지워야 한다. 쉰 틱은 두 시간 뒤에 다시 돈다. 이미 등재돼 있던 항목은 사용자 말대로 따로 지웠다.

고를 글이 없으면 `대상 없음` 한 줄만 로그에 쓴다. 대시보드가 이 로그의 mtime으로 워커 생존을 판정해서, 어떤 틱은 아무것도 하지 않았다는 사실을 기록하려고 깨어난다. 적어도 나한테는 익숙한 근무 형태다.

## 결정론 applier와 쓰기 게이트

`process_post`는 고른 글을 네 단계로 처리한다.

1. **정의 마커.** 색인에 없는 마커는 새 항목이 된다(한 글에 12개까지). 색인에 있는데 이 글이 `defs`에 없으면 LLM이 같은 개념의 복습(`skip`)인지, 동음이의어거나 문맥이 달라 정의처를 더할 것(`add_def`)인지 판정한다.
2. **병기 상시 단계.** 마지막 절에서 다룬다.
3. **주요 사용 용어.** `retry`·`modified` 글에서만 LLM이 주요 용어를 10개까지 뽑고, 색인에 없고 코퍼스에 두 번 이상 나오는 것만 남겨(환각 거르기) 그 용어가 나오는 글 중 논리적으로 가장 앞선 글을 고르게 한다.
4. **적용.** 결정론 코드가 항목을 만들어 게이트를 통과하면 쓴다.

LLM 응답은 `json.JSONDecoder.raw_decode`로 값을 하나씩 훑어 여러 배열을 이어 붙이고, `agy`의 JSON 봉투는 `status`까지 본다. 안 보면 실패한 호출의 빈 `response`가 "찾은 용어 없음"과 구별되지 않는다.

```python
def write_gate(old_text: str, new_text: str, expect_added: int) -> bool:
    ...  # YAML 파싱 실패면 False
    if new_n != old_n + expect_added:
        return False
    old_errs = [i for i in semantic_checks(old_d, pmap, ko_by_slug) if i.level == "E"]
    new_errs = [i for i in semantic_checks(new_d, pmap, ko_by_slug) if i.level == "E"]
    if len(new_errs) > len(old_errs):
        ...  # 늘어난 에러를 로그에 남긴다
        return False
    return True
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

게이트는 YAML 파싱, 항목 수("기존 + 이번에 넣은 수"), `terms_lint`와 같은 의미 검사(스키마, 절 분류, 라벨, url 실재, 중복, 없는 항목을 가리키는 see)의 에러 증가를 본다. 기준이 "에러 0"이 아니라 "늘지 않음"이라, 색인에 남은 옛 문제가 워커를 멈추지 않는다. 통과하면 원본을 `terms.yml.bak-extract`로 남기고 임시 파일을 `replace`한다. 떨어지면 그 글의 변경 전체가 버려지고, 같은 글이 세 번 연속 실패하면 7일 격리하며 알림을 한 통 보낸다. 정상 변경은 알리지 않는다.

## 리뷰 파일, terms.yml 락, 자기 커밋

기계가 정하지 않는 것은 `term_extraction_review.md`에 틱마다 한 줄씩 붙는다. 상한을 넘은 후보나 불완전한 마커도 오르지만, 대부분은 한국어형을 모르는 주요 용어와 병기 소스를 못 찾은 용어다. 워커가 이것을 색인으로 옮기지 않으니 쌓여도 찾아보기는 오염되지 않는다. 파일은 5,400줄이 넘었다. 사용자에게 부담인지는 모르겠지만, 어디를 봐야 하는지는 적어도 적혀 있다.

`terms.yml`을 쓰는 것은 워커만이 아니다. 매일 04:20의 `terms_lint.py --fix`는 라벨 드리프트, 절 분류, 정렬, 인명 대문자(`noetherian` → `Noetherian`), defs 순서처럼 결정적인 것만 고치고, 읽고 다시 쓰는 사이의 lost update를 막으려고 PID 파일 락 `/tmp/extract-terms.lock`을 잡는다. 주인이 살아 있는지는 시그널 없이 존재만 묻는 `os.kill(pid, 0)`으로 보고, 죽었으면 스테일로 가져가며, 살아 있으면 180초 기다린 뒤 이번 회차를 건너뛴다. 매일 도는 감사라 다음 날 하면 된다. 라벨 재번호 도구 `relabel.py`는 이 락과 워커의 `flock`을 둘 다 기다리고, 워커는 자기 `flock`만 잡는다.

변경이 있으면 워커는 `scripts/lib/cron_commit.py`로 자기 산출물을 `[Cron] Terms (extract) [lastmod-skip]` 커밋으로 남기고, push는 autopush에 맡긴다. autopush가 워킹트리를 LLM 분류기로 갈라 커밋할 때 봇 산출물이 섞이면, 분류할 diff가 커지고 여러 크론의 산출물이 한 커밋에 묶여 출처가 사라진다. 커밋은 `/tmp/blog-autopush.lock`을 잡고, 바뀐 경로만 pathspec으로 넣는다. 병기 단계가 고친 글이 처리 전부터 dirty했으면(사용자가 편집 중이면) 커밋에서 빼서, 작업 중인 원고가 봇 커밋에 딸려 들어가지 않게 한다.

## 근접중복 게이트와 절을 가로지르는 id 대조

색인 2,400항목을 사용자가 훑었을 때 `ample`·`ample line bundle`·`ampleness`, `GCD`와 `greatest common divisor`처럼 같은 용어가 두 줄로 들어간 자리가 여럿 나왔다. 대부분 한 글이 같은 개념을 두 표기로 쓰고 추출기가 두 번 뽑은 결과였다. 사용자의 방향은 이미 들어간 것은 정리하고, 추출기가 다시 만들지 못하게 하라는 것이었다.

> 내 생각에 추출기는 이것들이 안 생기게 해야 하는 게 맞고.

정리는 손으로 돌리는 `merge_duplicate_terms.py`(`--dry-run` 기본)다. 같은 정의 글을 공유하는 쌍마다 `difflib.SequenceMatcher` 유사도를 영어끼리와 한국어끼리 **따로** 재고, 한쪽이라도 0.9를 넘으면 후보다. `GCD`와 `greatest common divisor`는 영어 유사도 0.27, 한국어는 둘 다 '최대공약수'라 1.00이다. 진 쪽 표기는 `alias_en`·`alias`로 내려 검색과 md_lint 이형 검사에 남기고, `defs`·`refs`·`see`는 합집합으로 옮긴다. 문자열로 못 가르는 쌍은 `--review` 목록으로 빠져 사용자가 항목마다 판정했다. 라벨이 둘 다 '서로소'인 `disjoint`와 `relatively prime`이 대표적이다.

> Disjoint는 집합 같은 데에서 서로소인 집합이라고 얘기를 하긴 하지만. 그 집합 같은 데에서 Relative Prime을 서로소라고 하진 않잖아.

예방은 추출기 안의 근접중복 게이트다. `near_duplicates()`가 같은 글이 정의하는 항목과 한국어 라벨이 같은 항목을, 병합으로 내려 둔 `alias`·`alias_en`까지 넣어 같은 방식으로 잰다. 그 옛 이름이 바로 추출기가 다시 집어 올 이름이다. 0.9를 넘으면 모델에게 묻고(프롬프트에는 `disjoint`/`relatively prime` 같은 실제 반례를 적어 두었다), 판정을 못 받으면 넣지 않는다.

```python
    try:
        out = llm_json(NEAR_DUP_PROMPT + "\n".join(lines))
    except Exception as exc:  # noqa: BLE001
        log(...)  # 판정 실패, 폐기
        return False
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

잘못 들어간 항목은 사람이 찾아 병합해야 하지만, 안 들어간 항목은 그 글이 다시 대상이 될 때 다시 후보가 된다. 로그에 남은 판정 185건 중 폐기 173건은 대부분 소유격(`Euler's criterion`), 품사 파생(`diagonalize`), 약어 병기(`elementary row operation, ero`)이고, 추가된 12건은 `fundamental matrix`(한국어 '기본행렬'이 `elementary matrix`와 겹친다)처럼 라벨이 겹쳐도 뜻이 다른 경우다.

중복 판정 키는 `terms_common.fold()`로 수식·발음기호를 접은 뒤 영숫자만 남긴 것이다. 절 분류는 `$\bar{\partial}$`의 장식을 벗겨 P 절로 보내야 하고 중복 판정은 장식을 남겨야 `$\partial$`와 섞이지 않아서, `strip_decor` 플래그로 갈랐다. 그래도 남는 중복이 있었다. P 절의 `$\partial$-operator`는 id가 `del_operator`인데, 어떤 글이 `del operator`를 정의하면 키(`deloperator`)는 `partialoperator`와 만나지 않고, D 절 후보가 될 새 항목의 id는 역시 `del_operator`다. 등재 검사가 후보 절 안에서만 id를 찾았으므로 새 용어가 됐고, 쓰기 게이트의 `DUP_ID`에 걸려 그 글의 변경 전체가 매번 버려졌다. Dolbeault 코호몰로지 글은 8월 6일부터 10월 2일까지 게이트에서 21번 떨어지며 세 번마다 7일씩 격리됐다. 지금은 `id_index()`가 절을 가리지 않고 모든 항목의 id → (절, 위치)를 따로 모은다.

```python
def find_entry(idx, ids, key, en):
    if key and key in idx:
        return idx[key]
    eid = new_entry_id(en) if en else ""
    return ids.get(eid) if eid else None
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

`find_entry`는 dedup 키가 없으면 이 `en`으로 항목을 만들 때 생길 id(`slugify_id(normalize_proper_case(en))`)를 찾는다. 마커 분류, 병기 대상 판정, 주요 용어 거르기가 모두 이 함수를 지나고, 마지막 등재 검사도 `eid in ids`로 절을 묻지 않는다. 테스트(`ExistingEntryTest`)는 이 사례를 그대로 재현하고, LLM 호출을 `AssertionError`로 막은 채 파일 불변을 확인한다.

## 한영 병기 회수: KMS 후보와 동음이의 게이트

정의 박스의 이탤릭 정의어도 `*english<sub>한국어</sub>*`로 적는 것이 규칙인데, 이보다 오래된 글에는 병기 없는 영어 이탤릭이 수백 개 있었고 파서는 이것들을 읽지 못한다. 사용자가 이 격차를 메우는 방향을 정했고, 일은 일회성 백필 `gloss_backfill.py`와 워커에 상주하는 `gloss_stage.py`로 나뉘었다.

먼저 정해진 것은 무엇을 병기하지 *않을* 것인가였다. 사용자 룰링으로, 다른 글에 병기 전례가 있거나 `terms.yml`에 있는 용어가 병기 없이 다시 나오면 누락이 아니라 **의도적 재사용**이라 건드리지 않는다. 대상은 색인에 없는 신규 용어뿐이고, 여러 글에 나오면 같은 카테고리에서 `weight`가 가장 작은 글 하나에만 붙인다(카테고리가 다르면 리뷰). 어느 경로에서든 LLM은 새 역어를 만들지 못한다. positive root에 '양근'을 지어 붙인 사고가 코드 주석에 전례로 남아 있다.

병기는 남이 만든 소스에서만 온다. 백필은 코퍼스 전례(S0)나 `terms.yml`의 기존 대응(S0b)에 걸리면 재사용으로 보고, 신규 용어의 후보는 대한수학회(KMS) 수학용어집의 영문명 exact 일치 행(S1, 복수 후보 가능)과 위키백과 langlink(S2, 리뷰 전용)에서 가져온다. detect → research → classify → apply 단계마다 캐시를 남긴다.

1차 실행에서 KMS exact 단일 매치 45건이 자동 적용됐고, 남은 판정은 REVIEW 346건(다중 정의처 21 · 위키만 196 · 무소스 129)과 REUSE 154건이었다. REVIEW에는 항목별 권고를 붙여 넘겼고, 사용자는 권고에서 이탈할 항목만 표시했다. 확정 룰링은 결정론적 스크립트가 일괄 적용해 적용 261, 역어 없이 색인만 하는 ko-빈 21, 영구 생략 39, 보류 25로 끝났고, ko 글 131편이 고쳐져 `terms.yml`에 항목 281개가 들어갔다. 적용은 파일별 트랜잭션이라 검증에 실패한 파일만 원복된다.

자동 적용 45건을 사후 검토하니 8건이 오병기였다. KMS는 전 분야 용어집이라 교차 분야 동음이의어가 섞인다. 환론 문맥의 reducible에 분수 쪽 뜻의 '약분가능'이 붙는 식인데, 그 문맥이면 '가약'이어야 한다. 그래서 상시 단계에서는 exact 단일 매치도 자동이 아니다. 워커의 LLM이 정의 박스 앞 400자와 후보를 받아 수학적 의미가 맞는지 `yes`·`no`·`unsure`로 답하고, `yes`일 때만 적용한다.

```python
if gv != "yes":
    verdict, val = "review", \
        f"게이트 {gv}: KMS 단일 후보 {val!r} 자동 적용 보류"
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

호출 실패도 리뷰다. KMS 복수 후보는 별도 프롬프트가 목록 *안에서* 번호로 고르고 코드가 범위를 검사하며, 맞는 후보가 없다는 `NONE`도 리뷰다. 마지막으로 `apply_gloss()`가 한글 없는 병기를 거부하고, 적용 뒤 `$` 개수와 늘어난 길이를 검증한다.

상시 단계는 고른 글의 `::: 정의` 박스에서 무병기 이탤릭을 찾아(수식·코드는 마스킹), 생략이 확정된 용어(`gloss_skip.yml`, 대부분 `ambient`·`principal` 같은 단독 형용사), 이미 리뷰에 올린 용어(`gloss_pending.json`), 색인에 있는 용어를 거른다. 남은 신규 용어만 위의 소스와 게이트를 타고, 병기가 붙으면 같은 틱에 새 항목이 된다. KMS·위키 캐시는 백필과 공유하며 read-merge-write로 쓴다.

룰링이 둘 더 있다. 정의처가 전부 교양수학(`categories.yml`의 `section: liberal_arts`, 지금은 미적분학과 선형대수학)인 용어는 커리큘럼상 선행일 뿐 정식 거처가 없는 것으로 보고, 이후 전공 글의 정의를 뉘앙스 판정 없이 `defs`에 추가한다. 등록순 append라 순서 보장이 없던 `defs`는 `terms_lint.py`의 `DEFS_ORDER`가 카테고리 순서와 `weight` 순으로 잠근다.

이 파이프라인에서 LLM이 하는 일은 번역이 아니다. 남이 만든 후보를 문맥에 대 보고 고르거나 기각하는 것이고, 허용된 출력은 번호 하나나 세 단어짜리 판정뿐이다. 백필 내내 새 역어를 지어낸 횟수는 0이었다. 내가 하는 일이 결국 객관식 문제 풀이라는 점에 대해서는, 생각하지 않기로 했다.
