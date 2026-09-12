---

title: "원문을 다시 읽는 번역 워커"
excerpt: "번역 엔진을 Kimi에서 Antigravity로 옮기면서 원문대조 폴리싱 패스를 세우고, 그 김에 한글 원문의 오류까지 같이 훑어 대시보드로 올리게 한 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/antigravity_polish

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-06
last_modified_at: 2026-09-12

weight: 49

---

관련 파일: [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/translation/ko_followup_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/ko_followup_worker.py), [`_config.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_config.yml), [4d2ebc7c](https://github.com/math-jh/math-jh.github.io/commit/4d2ebc7c), [20cc224b](https://github.com/math-jh/math-jh.github.io/commit/20cc224b)
{: .notice--info}

EN 코퍼스는 전부 Kimi K3가 번역한 것이다. 그 번역을 다시 훑는 패스를 붙이기로 하면서, 사용자는 같은 엔진으로 자기 결과를 검토시키는 구도를 피했다.

> 근데 이제 번역도 원래 Kimi로 translate가 다 됐었잖아. 근데 이제 그거를 또 똑같이 Kimi로 polish 하는 것보다는 다른 걸로 하는 게 나을 것 같아서, Antigravity로 올렸어. 그리고 올리면서 한글 글에 오류가 있는 것도 걔가 같이 보게 했고, 그리고 겸사겸사 영문과 한글 글의 불일치가 있으면 그것도 하게 했단 말이야.

같은 자리에서 주기도 바뀌었다. 8월 전수 감사가 지적을 한꺼번에 쏟아내는 바람에 사용자가 끝내 따라가지 못했고, 그 경험에서 하루 6편이 실제로 소화되는 양이라는 계산이 나왔다. 30분마다 돌던 것을 4시간에 한 번으로 늘린 것은 그 숫자에 맞춘 결과다. 워커가 느려서가 아니라 사람이 읽을 수 있는 속도가 상한이다.

## 엔진 이름을 `_config.yml`로 끌어올리기

기계번역 고지는 EN frontmatter의 `translation_source`가 `_config.yml`의 정본 태그와 일치할 때만 붙는다. 태그를 `kimi-cli`에서 갈아치우면 기존 EN 400여 편이 전부 고지를 잃는다. 그래서 정본 하나가 아니라 세 개의 키로 나눴다.

```yaml
translation_source_tag         : "antigravity-gemini-3.8-flash-high"
translation_source_legacy_tags : ["kimi-cli"]
translation_polish_source_tag  : "antigravity-gemini-3.8-flash-high"
```

`legacy`는 "더 이상 새로 쓰지 않지만 계속 표시할 엔진"이다. 고지 include는 현재 태그와 legacy 목록을 둘 다 본다.

{% raw %}
```liquid
{% assign _machine_translation = false %}
{% if page.translation_source == site.translation_source_tag %}
  {% assign _machine_translation = true %}
{% elsif site.translation_source_legacy_tags contains page.translation_source %}
  {% assign _machine_translation = true %}
{% endif %}
```
{% endraw %}

`_data/ui-text.yml`의 키 이름은 `kimi_translation_notice` 그대로 뒀다. 엔진 이름이 키에 들어가 있는 것이 이제 와서 어색하지만, 이름을 바꾸면 include와 두 언어 블록을 동시에 고쳐야 하고 얻는 것이 없다.

워커 쪽은 백엔드 이름에서 태그를 역산한다. 롤백 경로를 남겨 둔 것이라, `TRANSLATOR_BACKEND=kimi`로 되돌리면 태그도 따라 돌아간다.

```python
_BACKEND_SOURCE_TAGS = {
    "antigravity": _CONFIG_TRANSLATION_SOURCE_TAG,
    "kimi": "kimi-cli",
    "glm": "glm-cli",
}
```

`_load_translation_source_tags()`는 `_config.yml`에서 세 키를 읽고, 현재 태그나 폴리싱 태그가 비어 있으면 그냥 죽는다. 고지 include와 짝이 되는 값이라 조용히 빈 문자열로 넘어가면 사이트 전체에서 고지가 사라진다.

## 폴리싱 패스를 태그로 세우기

폴리싱은 별도 큐가 아니라 frontmatter 태그 하나로 굴러간다. EN에 `translation_polish_source`가 현재 폴리싱 태그와 같으면 이미 이번 패스를 거친 것이고, 아니면 대상이다.

```python
    meta = en_translation_meta(existing_en)
    if meta.get("translation_polish_source") == TRANSLATION_POLISH_SOURCE_TAG:
        continue                       # already polished by the current pass
    return ko, existing_en, "polish"
```

그다음 Phase 4의 검증은 조건이 정확히 반대다.

```python
    if meta.get("translation_polish_source") != TRANSLATION_POLISH_SOURCE_TAG:
        continue                       # current contrastive pass comes first
```

두 조건이 서로의 여집합이라 순서가 저절로 강제된다. 폴리싱 안 된 글은 Phase 3이 가져가고, 폴리싱된 글만 Phase 4가 검증한다. 나중에 엔진을 또 바꾸면 `translation_polish_source_tag`만 새 값으로 두면 되고, 코퍼스 전체가 자동으로 다시 폴리싱 대기열에 들어간다. 태그를 큐로 쓰는 이유가 이것이다.

frontmatter는 본문과 분리해서 처리한다. `_polish_fm_fields`가 KO/EN 필드를 JSON으로 주고받고, 본문 프롬프트는 frontmatter를 아예 보지 않는다. 프롬프트에 "Output ONLY the complete repaired English body"라고 적힌 것은 그래서다. 본문 폴리싱이 `title:` 줄을 건드리면 permalink와 사이드바가 같이 흔들린다.

## 폴리싱 중에 한글 원문을 함께 읽기

같은 호출에서 한글 원문의 오류도 보게 했다. 프롬프트는 이걸 read-only 분류 작업으로 규정한다.

```
Read the complete Korean mathematics post below during this polishing run.
This is a read-only triage task: never rewrite the post and never discuss
the English translation.
```

프롬프트로 부탁하는 것만으로는 부족해서 해시로 확인한다. 후보를 받아 Codex 2차 판정을 붙이는 `review_ko_findings`가 전후 SHA-256을 비교하고, 다르면 알림을 띄운다.

```python
    if hashlib.sha256(ko_path.read_bytes()).hexdigest() != before:
        log(f"GATE-KO-REVIEW ({key}): KO 파일이 변경됨 — read-only 계약 위반")
        _notify("[translate-worker] Codex KO 검토가 원문을 수정함",
                f"{key}\nCodex 검토 전용 단계 전후의 KO 해시가 다릅니다.",
                level="timeSensitive")
        return out
```

Codex 판정은 `VALID`·`FALSE`·`UNSURE` 셋 중 하나만 받는다. 호출이 실패하거나 응답이 파싱되지 않은 후보는 판정 없이 그대로 남긴다. 검토가 안 됐다는 이유로 후보를 숨기면 사용자 알림에서 조용히 사라지고, 그건 오류가 없다는 뜻으로 읽힌다.

후보에는 원문의 인용구가 딸려 오는데, 그 인용구가 KO 본문에서 안 찾아지면 후보를 버린다.

```python
        pos = ko_text.find(quote)
        # A finding without an exact source locus cannot provide a trustworthy
        # line number or later diff target.
        if pos < 0:
            continue
```

인용구를 못 찾는 후보는 위치를 알려줄 수 없고, 나중에 수정분을 대조할 기준도 못 준다. 모델이 원문을 살짝 바꿔 옮긴 것과 없는 문장을 지어낸 것을 여기서 구분할 방법은 없으니 둘 다 버린다.

찾아진 후보는 그 시점의 KO 전문을 상태 파일에 통째로 남긴다.

```python
            ko_review_base = ko_path.read_text(encoding="utf-8")
            state["files"][key]["ko_review_base_content"] = ko_review_base
            state["files"][key]["ko_review_base_sha256"] = hashlib.sha256(
                ko_review_base.encode("utf-8")).hexdigest()
```

git에서 꺼내면 될 것 같지만 안 된다. 감사 시점의 KO가 아직 커밋 안 된 워킹트리 상태일 수 있고, 그러면 재구성할 방법이 없다. 후보가 살아 있는 동안만 들고 있다가 해소되면 버린다.

## `\times`가 탭이 되는 자리

모델 응답을 JSON으로 받다 보면 수식이 문제가 된다. 유효한 JSON 안에 LaTeX 백슬래시가 한 개짜리로 들어오면 `json.loads`가 그걸 이스케이프로 읽는다. `\times`는 예외 없이 탭 문자 하나에 `imes`가 붙은 문자열이 되고, 파싱은 성공한다. 깨진 채로 통과하는 쪽이 실패하는 쪽보다 나쁘다.

```python
    def protect_math(m: re.Match) -> str:
        return re.sub(r'(?<!\\)\\(?![\\"])', r'\\\\', m.group(0))

    t = re.sub(r"\$\$.*?\$\$|\$[^$\n]*\$", protect_math, t, flags=re.DOTALL)
```

수식 구간 안에서만 홑백슬래시를 이중으로 만든다. 뒤에 백슬래시나 따옴표가 오는 경우는 건드리지 않는데, 그건 모델이 제대로 이스케이프한 것이라 손대면 거꾸로 깨진다. 수식 밖의 JSON 이스케이프는 원래 의미를 유지한다.

## 대시보드 체크박스는 승인이 아니라 요청

한글 오류를 고치면 EN도 따라가야 한다. `ko_followup_worker.py`가 그 일을 맡는데, 대시보드 체크박스의 의미를 정한 것이 설계의 전부다.

```python
"""Follow up dashboard-confirmed Korean fixes and synchronize the English post.

The dashboard checkbox is a request, not an acknowledgement.  One request is
handled per run: Antigravity proposes the narrowly scoped EN replacement, then
Codex sees only the original finding plus KO/EN unified diffs and decides whether
both changes implement that finding.  The queue item is removed only after a
passing check and a successful content commit.
"""
```

체크를 승인으로 읽으면 체크하는 순간 항목이 큐에서 빠지고, EN 동기화가 실패해도 아무도 모른다. 요청으로 읽으면 항목은 EN 커밋이 실제로 들어갈 때까지 남는다.

판정하는 Codex에게는 원래 지적과 KO/EN 두 diff만 준다. 글 전문을 주면 지적과 무관한 개선안을 함께 들고 오고, 그러면 판정이 "이 지적을 구현했는가"가 아니라 "이 글이 좋아졌는가"가 된다. 제안하는 쪽과 판정하는 쪽에 다른 모델을 놓은 것도 같은 이유다.

follow-up은 별도 크론이고, 번역 워커와 2시간씩 엇갈리게 걸려 있다.

```bash
15 */4    * * * … translate_worker.py
15 2-22/4 * * * … ko_followup_worker.py
```

앞의 것이 0·4·8·12·16·20시에 한 편을 폴리싱하고, 뒤의 것이 2·6·10·14·18·22시에 체크된 요청 하나를 처리한다. 폴리싱이 올린 한글 지적을 사용자가 대시보드에서 체크하면 다음 짝수 시각에 EN이 따라온다. 같은 시각에 두 워커가 같은 글을 두고 부딪히는 일도 없다.

결국 2시간마다 뭔가가 한 편씩 도는데, 그 사이에 사람이 읽어주지 않으면 다음 틱은 의미가 없다. 주기를 정한 것도 그쪽이었다.

## 폴리싱도 출력 한도에 걸리다

번역 쪽 조각내기는 진작에 있었다. KO 본문이 길면 `:::` 정리 박스 경계로 잘라 따로 호출하는 `_split_regions`/`translate_body_chunked`가 통짜 번역이 출력 한도에서 끊기는 문제를 이미 막아 왔다. 폴리싱은 그 경로를 안 탔다. `build_polish_prompt`로 KO/EN을 통째로 한 번에 넘겼는데, CA/Differentials 글에서 KO 22,793자를 그대로 보냈다가 안티그래비티가 출력 토큰 한도에서 잘렸다. 폴리싱 출력은 EN 전문이라 번역과 같은 크기 문제를 그대로 물려받은 것인데, 조각내기 코드는 없었다.

기존 `_group_regions`를 그대로 쓸 수는 없었다. 그 함수는 KO 리전 하나의 길이만 보고 묶는데, 폴리싱은 KO와 EN을 짝지어 같이 보내야 하고 조각 경계도 두 쪽에서 동일해야 한다. `_group_region_pairs`는 box id로 KO/EN 리전을 짝짓고, 각 짝의 길이는 둘 중 긴 쪽으로 잰다.

```python
span = max(len(ko_text), len(en_text))
if cur_ko and cur_len + span > max_chars:
    batches.append(("".join(cur_ko), "".join(cur_en)))
    cur_ko, cur_en, cur_len = [], [], 0
```
{: data-filename="scripts/translation/translate_worker.py"}

KO만 보면 안 되는 이유는 폴리싱 출력이 EN 길이에 가깝기 때문이다. 번역이 짧게 요약된 문단이 있으면 KO는 짧은데 EN이 길어, KO 기준으로만 자르면 그 조각에서 다시 출력 한도에 걸릴 수 있다.

id 열이 KO와 EN에서 어긋나면(`_split_regions`가 뽑은 순서가 다르면) `_group_region_pairs`는 `None`을 돌려주고, 호출부는 조각내지 않은 통짜 폴리싱으로 되돌아간다. 정상 경로에서는 `lint_structure`를 통과한 글만 폴리싱까지 오므로 박스 수가 같고 어긋나지 않지만, 어긋난 경우를 조용히 조각내면 짝 없는 텍스트를 모델이 지어내거나 지운다.

조각마다 붙는 프롬프트도 번역 쪽과 같은 모양이다. 전체 중 몇 번째 조각인지 적고, 도입부·요약·전환 문장을 만들지 말고 분할 사실도 언급하지 말라고 명시한다. 다만 폴리싱은 라벨 번호를 새로 매기는 게 아니라 기존 번호를 그대로 지키는 일이라, 주의사항도 "라벨 번호는 조각을 넘어 이어지니 보이는 대로 유지하라"로 바뀐다.

경계값 자체도 두 번 내려갔다. 처음에는 번역 쪽 24,000자/12,000자 기준을 그대로 물려받아 10,000자/6,000자로 낮췄는데, 그 사흘 뒤 4,000자/4,000자로 한 번 더 낮아졌다. 판정 기준도 바뀌었다. 처음엔 KO 길이만 봤지만, 폴리싱 출력이 EN 쪽에 가깝다는 점을 감안해 KO와 EN 중 긴 쪽으로 조각 여부를 판정하게 됐다.

```python
chunked = (polish_body_chunked(ko_body, en_current_body)
           if max(len(ko_body), len(en_current_body)) > FULL_CHUNK_THRESHOLD
           else None)
```
{: data-filename="scripts/translation/translate_worker.py"}

번역과 폴리싱이 같은 상수(`FULL_CHUNK_THRESHOLD`, `MAX_CHUNK_CHARS`)를 공유하므로, 이 값을 내리면 번역 쪽 조각도 더 잘게 쪼개진다. 번역은 출력이 EN 하나뿐이라 원래도 여유가 있었지만, 두 경로를 하나의 상수로 묶어 둔 대가로 폴리싱이 요구하는 보수적인 값을 함께 물려받았다.
