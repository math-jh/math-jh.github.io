---
title: "Kimi를 빌려 한글 글들을 영어로"
excerpt: "30분마다 한 편씩, 자동 번역 워커를 세우는 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_translation_worker

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-19
last_modified_at: 2026-05-19
weight: 5

---

관련 디렉토리: [`scripts/translation/`](https://github.com/math-jh/math-jh.github.io/tree/main/scripts/translation)
{: .notice--info}

이 블로그는 본래 한글로 쓰여있지만, `/en/` 경로 아래에는 영어판이 따로 존재한다. 영어판 페이지들은 오랫동안 비어있거나, 한글 원문이 갱신되어도 영어판은 그대로 멈춰있는 상태였다. 사람이 매번 갱신할 수 있는 일이 아니라 자동화로 가야 한다는 결론은 비교적 명백했다.

방향이 결정된 것은 다음의 한 줄에서였다:

> 그 지금 블로그 보면, korean 글들을 영어로 번역하는 cron이 있거든? 그거 뭔지 좀 찾아봐.

존재하지 않는 cron을 찾아보라는 질문으로 시작된 셈인데, 어쨌든 그렇게 해서 `scripts/translation/translate_worker.py`가 자라기 시작했다.

## 워커 한 번에 글 하나

전체 구조는 단순하다. 30분에 한 번 cron이 워커를 깨우고, 워커는 "번역이 필요한 한글 글 한 편"을 골라서 Kimi CLI에게 던지고, 결과를 `_posts/Math/.../en/` 아래에 쓴 다음 종료한다. 한 틱에 한 편 — 동시성도 없고 큐도 없다. lock 파일 하나로 중복 실행만 막는다.

```
*/30 * * * * cd /home/junhyeok/math-jh.github.io/scripts/translation \
             && /usr/bin/python3 translate_worker.py >>translation.log 2>&1
```

번역 대상 선정에는 우선순위가 세 단계로 정해져있다.

1. **pending** — 영어판이 아예 없는 한글 글
2. **drift** — 영어판은 있지만 한글이 더 최근에 수정됨 (커밋 시각 비교)
3. **polish** — 위 둘 다 해당 없으면, 마지막 polish가 14일 이상 지난 영어판 한 편을 재번역

세 단계가 순차적으로 비어갈수록 워커는 게을러진다. 새 글이 없으면 14일짜리 timer가 천천히 익기를 기다리는 것이 일이라, 수조개의 파라미터의 사용처로는 다소 한가한 편이다.

## Frontmatter에 흔적을 남기기

영어판 파일의 frontmatter에는 워커가 세 개의 마커를 넣는다.

```yaml
translation_source: kimi-cli
translated_at: 2026-05-19T03:00:14+00:00
last_polished_at: 2026-05-19T03:00:14+00:00
```

`translation_source`는 자동 번역물임을 식별하기 위한 라벨이다. `translated_at`은 마지막으로 새로 번역되었거나 drift가 해소된 시점, `last_polished_at`은 마지막 polish 시점. 처음 fresh 번역하거나 drift로 다시 번역할 때는 `last_polished_at`을 일부러 비워두는데, 그래야 polish 큐에 다시 잡혀서 어색한 문장을 다음 polish 때 다듬을 기회가 생긴다.

## 망가지기 쉬운 부분

번역이라는 게 그냥 텍스트만 들어갔다 나오는 일이 아니다. 이 블로그의 글들은 대부분 수식과 인용과 카테고리 라벨이 들어있고, 번역기가 그것들을 다 무사히 통과시킬 것이라 믿을 수는 없다. 그래서 워커는 결과물을 받자마자 몇 가지 검사를 돌린다.

- **Truncation guard**: 출력 본문이 한글 본문 길이의 60% 미만이면 실패 처리. polish의 경우엔 추가로 기존 영어판의 85% 미만이어도 실패. polish는 다듬는 일이지 줄이는 일이 아니어야 하니까.
- **Math block audit** (`math_block_audit.py`): `$$...$$` 블록 개수가 한글/영어 사이에 어긋나면 알린다. 단순히 개수만 비교하는 대신, mismatch가 발견되면 Kimi에게 *어디서 어떻게 어긋났는지*를 다시 검증시킨 후 그 내용을 텔레그램으로 보낸다. 다음의 요청에서 만들어진 흐름이다:

  > 그러지 말고, `$$...$$` 개수가 다르면 kimi한테 다시 검증시킨다음, 어디서 바뀌었는지, 문제는 없는지 파악시킨 다음 그 내용을 텔레그램으로 보내주면 어때?

- **Label normalization** (`label_normalize.py`): "예시 1", "명제 5" 같은 한글 라벨이 번역물에 그대로 남아있는 경우 잡아낸다.
- **Translation loss audit** (`translation_loss_audit.py`): 줄 수 기준으로 한글→영어 손실률을 계산해서 의심스러운 파일들을 보고한다. 한 번 모든 글의 fresh 번역이 끝난 시점에 일괄로 돌렸고, 손실이 큰 파일은 영어판을 삭제해서 fresh 큐에 다시 올렸다.

Timeout은 25분으로 잡혀있다. 처음엔 15분이었는데, 큰 글(30KB 이상)이 중간에 잘려나가는 일이 있어서 늘렸다.

> kimi_timeout_sec을 좀 늘리자. 25분 정도로.

## 번역물임을 숨기지 않기

자동 번역물이 사람이 쓴 글인 척 페이지에 떠 있는 것은 정직하지 않다. `_includes/translation-notice.html`은 `translation_source: kimi-cli` 마커가 박힌 글에 한해 페이지 맨 위에 안내 배너를 띄운다.

{% raw %}
```liquid
{% if page.translation_source == "kimi-cli" %}
  ...
  {% assign _notice = site.data.ui-text[_lang].kimi_translation_notice %}
  ...
{% endif %}
```
{% endraw %}

안내 문구 자체는 `_data/ui-text.yml`에서 언어별로 따로 관리된다.

```yaml
en:
  kimi_translation_notice: "This post was translated from Korean by LLM (Kimi). The translation may contain errors or awkward sentences. The Korean original is the source of truth."
ko:
  kimi_translation_notice: "이 글은 한글 원문을 Kimi CLI로 자동 번역한 것입니다. 번역 오류가 있을 수 있으며, 한글 원문이 우선합니다."
```

영어 페이지에는 영어 안내가, 한글 페이지에는 한글 안내가 뜬다. 정확히 말하면 한글 페이지에는 이 마커가 있을 일이 없으니 후자는 거의 보이지 않는 안전망에 가깝지만, 둘 다 등록해두는 편이 일관적이라 그대로 두기로 했다.

## 지금의 상태

수십 편의 한글 글들이 영어판을 갖게 되었고, 한글이 갱신되면 30분 이내에 drift가 잡혀 다시 번역된다. 새로 쓸 한글 글이 없는 시기에는 워커가 polish 큐를 천천히 갉아먹으며 매번 14일 묵은 영어판 하나씩 다듬는다. 텔레그램 알림은 가끔 새벽에 mismatch를 알려오고, 대부분은 별 일 아니지만 가끔 진짜로 잘못된 번역이 잡혀나오기도 한다.

자동 번역은 본질적으로 사람의 번역만큼 정확하지 않고, kimi_translation_notice 배너가 그 사실을 매 글의 머리에 작은 글씨로 적어둔다. 모든 일이 다 그렇듯, 완벽하지 않은 채로 굴러가는 편이 굴러가지 않는 것보다는 낫다.
