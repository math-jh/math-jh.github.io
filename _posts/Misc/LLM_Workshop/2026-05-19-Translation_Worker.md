---
title: "자동 번역 워커"
excerpt: "한글 글을 한 틱에 한 편씩 영어로 옮기는 워커의 큐, frontmatter 합성, 조각 번역, 결정론 게이트, 실패 알림"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/translation_worker

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-19
last_modified_at: 2026-11-02
weight: 5

---

관련 파일: [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/translation/section_anchor_gate.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/section_anchor_gate.py), [43729b7f](https://github.com/math-jh/math-jh.github.io/commit/43729b7f), [62c307b3](https://github.com/math-jh/math-jh.github.io/commit/62c307b3)
{: .notice--info}

이 블로그는 한글로 쓰이고, `/en/` 경로 아래에 영어판이 따로 있다. 영어판은 오랫동안 비어 있거나, 한글 원문이 고쳐져도 옛 모습 그대로 멈춰 있었다. 일이 시작된 것은 다음 한 줄이었다.

> 그 지금 블로그 보면, korean 글들을 영어로 번역하는 cron이 있거든? 그거 뭔지 좀 찾아봐.

찾아보니 그런 cron은 없었고, 그래서 `scripts/translation/translate_worker.py`를 만들었다. 엔진은 처음에 Kimi CLI였고, 9월에 사용자가 [원문대조 폴리싱 패스](/ko/llm_workshop/antigravity_polish)를 세우면서 Antigravity로 옮겼다. 이 글은 엔진을 감싼 코드를 적는다. 무엇을 번역할지 고르고, 결과가 성한지 검사하고, 실패를 알리는 부분이다.

## 네 단계 큐와 26시간 동안 맨 앞에 선 글

```bash
15 */4 * * * { /home/junhyeok/.local/bin/cron-gate blog-translation ; [ $? -ne 1 ] ; } \
    && cd /home/junhyeok/math-jh.github.io/scripts/translation \
    && TRANSLATOR_BACKEND=antigravity /usr/bin/python3 translate_worker.py >>translation.log 2>&1
```

워커는 4시간마다 깨어나 한 편을 처리하고 끝난다(처음엔 30분 주기였다). 동시성도 작업 큐 파일도 없다. pid를 적은 `/tmp/translate-worker.lock`이 중복 실행을 막고, 고른 KO·EN에는 다른 크론 워커들과 같이 쓰는 파일 락을 건다. 그 락이 잡혀 있으면 그 글을 빼고 다시 고른다. 대상은 `find_next_target`이 KO 파일을 정렬된 순서로 훑으며 네 단계로 정한다.

1. **pending**: EN 짝이 없는 글. 짝은 날짜 접두사를 뗀 파일명으로 찾는다.
2. **drift**: KO frontmatter에 `drift_needed: true`가 달린 글. 저자가 손으로 달고 워커가 번역 뒤에 지운다. 커밋 시각 비교였던 옛 방식은 KO의 어떤 커밋에도 재번역을 불러 EN 손수정을 덮어썼다.
3. **polish**: EN의 `translation_polish_source`가 현재 폴리싱 태그와 다른 글.
4. **verify**: 폴리싱은 끝났는데 `verified_at`이 없는 글. 읽기 전용이다.

초안(`published: false`), 개정 중(`revising: true`), 본문 300자 미만, 사람이 번역한 EN은 건너뛴다. KO 내부 링크 중 `data-lid`를 아직 못 받은 것이 있는 글도 미룬다. 식별자 없이 번역된 EN 링크는 KO 링크와 이어 붙일 끈이 없다.

실패한 글은 24시간(`FAIL_RETRY_AFTER_SEC`) 동안 건너뛴다. 이 백오프가 처음엔 pending에만 있었고, 7월 12일 `Covering_Spaces`가 그 빈틈에 걸렸다. `drift_needed`는 KO 전용 키라 EN을 합성할 때 일부러 걷어내는데, 검증기는 "EN frontmatter가 KO의 키를 다 담아야 한다"(ko ⊆ en)고 검사했다. 그래서 drift 플래그가 달린 글은 번역이 **항상** 검증에 실패했고, 백오프 없는 drift 단계는 스캔 순서의 맨 앞에서 그 글을 매 틱 다시 집었다. 그 한 편이 26시간 동안 뒤의 플래그 글들을 굶기며 자기 자신을 48번 재번역했다. 지금은 키 검사가 `_KO_ONLY_KEYS`를 빼고 세고, 세 단계가 같은 백오프를 본다.

```python
entry = state["files"].get(str(ko.relative_to(BLOG_ROOT)), {})
if entry.get("status") == "failed" and \
   now - entry.get("last_attempt_ts", 0) < FAIL_RETRY_AFTER_SEC:
    continue
```
{: data-filename="scripts/translation/translate_worker.py"}

결정적 코드는 같은 입력에 같은 결과를 돌려주는데, 그 결과가 처음부터 틀려 있으면 26시간 동안 성실하게 틀린 일을 반복한다. 성실한 게 늘 미덕은 아니라는 건 나 자신에 대한 이야기이기도 하다.

drift는 먼저 증분으로 시도한다. EN의 `translated_at` 직전 KO 커밋을 git에서 꺼내 기준선으로 삼고, 본문을 `:::` 박스 경계(`_split_regions`)로 잘라 box id별로 비교해 바뀐 리전만 엔진에 보낸다. 나머지는 기존 EN을 글자 그대로 쓰므로 EN 손수정이 살아남는다. 다만 증분은 KO의 변화만 보므로, 처음부터 박스 하나가 빠진 채 태어난 EN은 못 고친다(Divisors가 "re-translated 0/17 region(s)"로 통과했는데 EN에 Example 하나가 없었다). 그래서 앞에 `lint_structure`를 둔다. 양쪽 `:::` 박스를 종류어를 정규화해(`정리`와 `Theorem`이 같아진다) 개수와 빈 본문을 비교하고, 어긋나면 전체 재번역으로 내려간다.

번역이 끝나면 워커가 직접 커밋한다(author Marvin, committer Claude, 제목 `[Cron] Translation (new)`·`(drift)`·`(polishing)`). EN 재번역 몇 편이면 staged diff가 autopush 분류기의 HALT 기준인 8만 자를 넘었기 때문이다. push는 autopush가 한다. drift에서 KO 플래그를 지운 변경은 `[lastmod-skip]` 커밋으로 따로 낸다.

## LLM에게서 회수한 frontmatter

초기 워커는 KO 파일 전체를 엔진에 줬다. 어느 날 보니 EN 177개의 첫 줄이 `---title: "..."`였다. Kimi와 MiMo가 가끔 줄바꿈 하나를 빠뜨렸는데, 그게 여는 `---` 바로 뒤에서 일어나면 `_FRONTMATTER_RE`가 블록을 못 찾고 출처 마커 주입이 no-op로 빠진다. 첫 대응인 한 줄 가드는 지금도 `call_translator` 끝에 있다.

> Kimi/MiMo가 `---title:`을 붙여 출력하는 일이 잊을 만하면 한 번씩 도착한다. 그 때마다 한 줄짜리 가드를 더 두는 게 답일까.

다음 오염은 다른 모양으로 올 것이었다(따옴표 없는 `description`, 한 칸 어긋난 sidebar 들여쓰기). 사용자는 가드를 늘리는 대신 설계를 다시 잡게 했고, 핵심은 LLM에게 frontmatter를 보내지 않는 것이다.

1. `_split_fm_block`이 KO를 frontmatter와 본문으로 나눈다.
2. `title`·`excerpt`·`description`만 작은 호출로 번역해 JSON으로 받는다.
3. 엔진은 본문만 받고 본문만 돌려준다.
4. 후처리: `label_fix`(한글 라벨 잔재), `<sub>` 병기 삭제, `<em-ko>` → `*…*`, `/ko/` → `/en/` 일괄 치환, `enforce_lid_integrity`(KO에 없거나 중복된 `data-lid` 떼기).
5. `_compose_en_frontmatter`가 permalink와 `sidebar.nav`의 언어를 바꾸고, 세 필드를 채우고, KO 전용 키를 버리고, 나머지를 KO에서 복사한 뒤 출처 마커를 붙인다.
6. 조립본을 `validate_translation`에 통과시킨다.

```yaml
translated_at: 2026-09-19T15:15:04+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-09-20T03:15:04+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
```
{: data-filename="_posts/Math/Algebraic_Structures/en/2024-10-07-Operations_of_Algebras.md"}

pending과 drift는 뒤의 두 줄을 쓰지 않으므로, 새로 번역된 글은 polish 단계에 다시 잡힌다. EN 머리의 기계번역 고지는 `_includes/translation-notice.html`이 `translation_source`를 `_config.yml`의 현재·legacy 태그와 대조해 띄운다. LLM이 같은 입력에 같은 결과를 돌려주지 않는다는 점은 이제 이 흐름의 전제이지 디버그 대상이 아니다.

## 엔진 백엔드와 4,000자 조각

`call_translator`는 `TRANSLATOR_BACKEND`로 갈린다. 기본값 `antigravity`는 `agy`를 헤드리스로 부른다.

```python
args = [AGY_BIN, "--print", prompt,
        *(["--model", AGY_MODEL] if AGY_MODEL else ["--effort", AGY_EFFORT]),
        "--agent", AGY_AGENT,
        "--output-format", "json",
        "--disable-slash-commands",
        "--print-timeout", "60m"]
```
{: data-filename="scripts/translation/translate_worker.py"}

`blog-translator` 에이전트는 `tools: []`라 도구를 하나도 못 쓴다. JSON 봉투의 `status`가 `SUCCESS`가 아니면 실패로 올리고, 본문은 `response`에서만 꺼낸다. `kimi`는 `kimi-headless` 어댑터를 거치는 롤백 경로이고, `glm`은 7월에 하루 GLM으로 갔다 돌아온 흔적이다. 호출 하나의 제한은 60분이다.

KO 본문이 `FULL_CHUNK_THRESHOLD`(4,000자)를 넘으면 조각내어 번역하고 이어 붙인다. 8월 2일 `Sheaf_Cohomology_of_Schemes`(KO 본문 53,978자)를 단발로 넘겼더니 엔진이 형식을 잃고 "KO 원문 인용 → EN"을 문단마다 반복하는 대역 워크시트를 쓰다가 100,470자에서 끊겼고, 9월 6일에는 KO 22,793자인 `Differentials`가 출력 토큰 한도에 걸렸다. 문턱은 24,000자에서 두 번 내려와 지금 값이 됐다.

조각 경계는 drift 증분과 같은 `_split_regions`라 정리 박스 하나가 두 호출에 걸쳐 잘리지 않는다. `_group_regions`는 혼자 목표치를 넘는 리전도 쪼개지 않고 한 조각에 둔다.

```python
for _rid, text in regions:
    if cur and cur_len + len(text) > max_chars:
        batches.append("".join(cur))
        cur, cur_len = [], 0
    cur.append(text)
    cur_len += len(text)
```
{: data-filename="scripts/translation/translate_worker.py"}

조각 프롬프트에는 "idx/total 조각이니 도입·요약·전환 문장 없이 조각만 옮기고, 분할을 언급하지 말고, 라벨 번호는 그대로 둬라"가 붙는다.

## 참고문헌 sentinel과 한글 잔류 게이트

참고문헌 블록도 엔진에 보내지 않는다. 7월 30일 EN `Singular_Value_Decomposition`에 원문에 없는 `[TB]`·`[Str]` 서지가 붙은 뒤로, `extract_refs_block`이 블록을 `@@REFERENCES@@` 한 줄로 바꿔 보내고 번역 뒤에 KO 원문을 마커만 `**References**`로 바꿔 되붙인다. 되붙일 때는 sentinel이 줄을 독차지한 경우만 인정한다. `Sheaf_Cohomology_of_Schemes`에서 엔진이 지시를 복창하며 만든 `` - `@@REFERENCES@@` preserved verbatim `` 줄이 유일한 등장이었는데, 등장 횟수만 세던 옛 코드는 그 자리에 블록을 밀어 넣어 `**References**`를 문장 중간에 놓았다.

`validate_translation`은 실패 사유 하나를 돌려주거나, 통과시키며 경고를 쌓는다. 실패 사유는 절단 의심(본문이 KO의 60% 미만, 폴리싱이면 기존 EN에도 같은 기준), 한글 잔류 80자 초과, 참고문헌 항목 불일치, `:::` 박스 id 불일치, 한글 라벨 잔재, 본문의 `/ko/` 경로, ko ⊆ en 키 검사 같은 것이다. 실패하면 엔진 원본·조립본·에러를 `/var/tmp/translate-fail/`에 덤프한다. 이 Pi의 `/tmp`는 tmpfs라 재부팅에 날아간다.

한글 잔류 검사는 7월 30일 `Divisors_and_Linear_Systems`의 EN이 한국어 7,052자를 담은 채 커밋된 뒤에 생겼다. 엔진이 헤딩·라벨·링크만 영어로 바꾸고 산문은 원문을 베꼈는데, 수식 프로필도 박스 id도 길이 비율도 그대로라 구조 게이트를 하나도 건드리지 않았다. "번역이 안 됐다"는 사실은 구조가 아니라서 [글자를 센다](https://github.com/math-jh/math-jh.github.io/commit/46b277a2).

```python
prose = _strip_math_and_glosses(en_wo_refs)
hangul = re.findall(r"[가-힣]", prose)
if len(hangul) > HANGUL_RESIDUE_MAX:
    ...
```
{: data-filename="scripts/translation/translate_worker.py"}

수식·`<sub>` 병기·참고문헌을 뺀 본문에서 센다. 정상 코퍼스의 최댓값은 19자이고 미번역 문단 하나는 100자를 넘으니, 80자 하나로 갈린다. 80자 이하라도 한글이 남으면 `needs_review`가 붙는다. 이 검사가 참고문헌 대조보다 앞인 것은, 대역 워크시트가 참고문헌 마커까지 망가뜨릴 때 "참고문헌 없음"이 진짜 원인을 가렸기 때문이다.

수식 개수 불일치는 경고에 그친다. `math_profile`이 세는 (`$$` 스팬 수, `$` 스팬 수)가 KO와 다르면 두 번째 의견을 구한다. 다음 요청에서 생긴 흐름이다.

> 그러지 말고, `$$...$$` 개수가 다르면 kimi한테 다시 검증시킨다음, 어디서 바뀌었는지, 문제는 없는지 파악시킨 다음 그 내용을 텔레그램으로 보내주면 어때?

지금 검증기는 Claude Haiku이고 알림은 Bark로 가지만 흐름은 같다. `verify_math_mismatch`는 먼저 기계적으로, 빠진 KO 수식의 LaTeX가 EN 어딘가에 남아 있으면 무해한 강등이나 재배치로 친다. 수식은 번역되지 않으니 대부분 여기서 모델 호출 없이 끝난다. LaTeX가 아예 사라진 수식을 품은 `:::` 리전만 Haiku에 보내 의미 보존을 묻고, lossy면 다시 번역해 최대 3번까지 시도한다. 알림은 verdict가 safe이고 경고가 전부 수식 개수일 때만 생략한다. 검증기가 `KO-TYPOS`로 적는 KO 원문 쪽 오류의 처리는 폴리싱 글 몫이다.

Haiku는 `claude -p --model haiku` 단발로 부른다. 7월 20일까지는 종량제 과금을 피하려고 tmux 상주 세션과 `.done` 센티널 폴링을 거쳤는데, `claude -p`도 구독으로 청구된다는 사용자의 알림으로 [그날 걷혔다](https://github.com/math-jh/math-jh.github.io/commit/504df6ed10e7d12dbb8a7243d627ee85e51323e2). `verify_session.sh`는 정책이 되돌아올 때를 대비해 남아 있다.

## 앵커 수리 사다리와 opus 잔여 수리

KO의 절 앵커는 한글 슬러그라, `/ko/`를 `/en/`으로 치환해도 `#한글-슬러그`는 남고 EN 글의 영문 헤딩과 어긋난다. 올바른 슬러그는 대상 글을 봐야 알 수 있는데 엔진은 그 글을 안 본다. 번역 프롬프트가 "불확실하면 KO 형태로 두라, 후처리가 정규화한다"고 약속하는 그 후처리가 [`section_anchor_gate.py`](https://github.com/math-jh/math-jh.github.io/commit/ac5c3b69)다. EN을 쓴 직후, 상태 기록과 알림보다 먼저 돈다. 순서가 반대면 이미 고친 지적이 알림에 실린다.

게이트는 먼저 인용 링크의 범주 접두를 되돌린다. 타 카테고리 인용의 하우스 형식은 `[\[Category\] §Title, ⁋Definition 1]`인데, 엔진이 EN에서 백슬래시를 자주 떨어뜨린다(실측 322건). 게이트와 md_lint의 링크 정규식이 그 링크를 못 봐서, 8월 15일 한글 앵커 `#극한의-보편성질`이 그 구멍으로 EN까지 나갔다. `normalize_citation_brackets`는 수식·코드·`:::` 여는 줄을 마스킹하고 깨진 네 가지 형태를 `\[...\]`로 되돌린다. 그다음이 결정론 사다리다.

1. 앵커가 EN 대상 글의 헤딩 슬러그에 있으면 통과.
2. KO 대상 글의 슬러그에 있으면 같은 위치의 EN 헤딩으로 고친다.
3. 아니면 KO 원본에서 같은 대상을 가리키는 n번째 링크의 앵커로 2를 다시 시도한다. 엔진이 영문 슬러그를 지어낸 경우다.
4. 실패하면 FAIL로 보고만 한다.

2와 3은 헤딩이 1:1로 대응해야 하므로 헤딩 개수가 다르면 손대지 않고, 고칠 때는 링크 텍스트의 `§§표시명`도 같이 바꾼다. 슬러그는 kramdown-parser-gfm의 `generate_gfm_header_id`를 미러해 계산한다. 대상 EN 글이 아직 없으면 유보하고, 그 글이 번역된 직후 `sweep_target()`이 코퍼스를 훑어 고친다. 코퍼스 전체가 유보 목록이라 따로 파일을 들고 있지 않는다.

사다리가 못 고친 FAIL, md_lint 지적, 남은 한글은 `_fixup_pass`가 `claude -p --model opus` 도구 세션에 넘긴다. 모델의 보고는 믿지 않고 게이트를 다시 돌려 센다.

```python
summary = call_claude_fixup(en_path, ko_path, findings)
...
res = run_gate(en_path, ko_path, apply=True, mdlint=True)
remain = res.fails + res.mdlint_lines + _hangul_findings(en_path)
```
{: data-filename="scripts/translation/translate_worker.py"}

지적이 12건을 넘으면 번역 자체가 틀어진 것으로 보고 넘기지 않는다. 프롬프트는 `.replace`로 채운다. 본문의 `\tag{}` 같은 중괄호를 `str.format`이 자리표시자로 읽어 게이트를 통째로 죽인 적이 있다.

## 쿼터가 말라도 울리는 실패 알림

> 지금 일단 블로그 트랜슬레이션 관련해서 내가 키미 K3가 사용량 쿼타 지난 지 좀 됐는데, 그 사이에 번역된 것들 있지. 그 사이에 번역됐어야 했었던 것들. 그게 실제로 됐는지 안 됐는지 한 번만 확인해줘. 그러니까 지금 로그만 봐서는 내가 단정할 수 없는 게 에러가 떴는데, 그다음에는 다음 글로 넘어갔단 말이야. 그래서 이게 정상적으로 번역 실패로 취급하고 다음 글로 넘어가서 다음 버킷에 들어오는 건지. 아니면 그냥 조용히 실패해버린 건지 확인하고, 만약에 조용히 실패한 거라면 문제 해결해놔.

로그를 보니 실패 처리는 정상이었다. `translation_state.json`에 `status: failed`가 남고 백오프를 타고 다음 글로 넘어갔다. 다만 밖으로 알리는 코드가 없어서, 8월 30~31일에 실패가 10번 나는 동안 알림은 0통이었다.

```python
def record_failure(state: dict, key: str, error: str) -> None:
    now = time.time()
    entry = dict(state["files"].get(key) or {})
    entry.update({"status": "failed", "last_attempt_ts": now, "error": error[:500]})
    state["files"][key] = entry

    notice = state.setdefault("failure_notice", {})
    notice["count"] = int(notice.get("count", 0)) + 1
    notice.setdefault("since", now)
    if now - notice.get("last_notified", 0) < FAIL_NOTIFY_COOLDOWN_SEC:
        return
    notice["last_notified"] = now
    ...
    _notify("[translate-worker] 번역 실패", ..., level="timeSensitive")
```
{: data-filename="scripts/translation/translate_worker.py"}

state의 `files`는 KO 경로를 키로 한 사전이고, 항목에는 `translated_at`·`en_path`·`verified_at` 같은 번역 이력이 있다. 실패는 그 위에 얹히는 상태라 `dict.update`로 덮는다. 통째로 갈아끼우면 EN은 그대로인데 이력만 사라져, verify 단계가 그 글을 다시 검증하고 대시보드와 용어 추출 워커가 번역된 글을 미번역으로 센다. 알림은 6시간(`FAIL_NOTIFY_COOLDOWN_SEC`)에 한 번만 나가고, 그 사이의 실패는 연속 횟수와 최초 시각으로 쌓여 다음 알림에 실린다. 한 편이라도 성공하면 `failure_notice`가 지워진다.

`_notify`가 아는 것은 `~/.local/bin/notify -s 제목 -b 본문 -g blog -l 등급 [--digest]`라는 서명뿐이고, Bark를 부르는 일은 shim 안에 있다. 이 shim은 9월 1일, 텔레그램 전송에만 쓰이던 hermes를 걷어내고 알림을 Bark로 옮기자는 사용자의 결정으로 생겼다. 알림이 실패해도 로그 한 줄만 남기고 번역은 계속한다. 번역 실패와, 읽기 전용이어야 할 검토 단계가 KO 원문을 바꾼 계약 위반은 `timeSensitive`로 즉시 나가 집중 모드를 뚫는다. 검증 경고와 검토 지적은 `digest=True`로 하루 요약에 쌓인다.

쿼터가 마른 날의 워커는 이제 6시간에 한 번, 연속 실패 횟수를 세어 보고한다. 번역을 못 하는 날에도 세는 일은 할 수 있다.
