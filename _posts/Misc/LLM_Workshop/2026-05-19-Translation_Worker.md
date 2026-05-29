---
title: "자동 번역 워커"
excerpt: "30분마다 한 편씩, 자동 번역 워커를 세우는 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/translation_worker

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

존재하지 않는 cron을 찾아보라는 질문으로 시작된 셈인데, 어쨌든 그렇게 해서 `scripts/translation/translate_worker.py`를 만들었다.

## 한 틱에 한 글

전체 구조는 단순하다. 30분에 한 번 cron이 워커를 실행하고, 워커는 번역이 필요한 한글 글 한 편을 골라 Kimi CLI에 넘기고, 결과를 `_posts/Math/.../en/` 아래에 쓴 다음 종료한다. 한 틱에 한 편이고, 동시성도 큐도 없다. lock 파일 하나로 중복 실행만 막는다.

```
*/30 * * * * cd /home/junhyeok/math-jh.github.io/scripts/translation \
             && /usr/bin/python3 translate_worker.py >>translation.log 2>&1
```

번역 대상 선정에는 우선순위가 세 단계로 정해져있다.

1. **pending** — 영어판이 아예 없는 한글 글
2. **drift** — 영어판은 있지만 한글이 더 최근에 수정됨 (커밋 시각 비교)
3. **polish** — 위 둘 다 해당 없으면, 마지막 polish가 14일 이상 지난 영어판 한 편을 재번역

세 단계가 차례로 비어갈수록 워커는 할 일이 줄어든다. 새 글이 없으면 14일 timer가 지나기를 기다리는 것이 전부라, 수조 개의 파라미터를 굴리는 쓰임새로는 한가한 편이다.

## Frontmatter의 흔적

영어판 파일의 frontmatter에는 워커가 세 개의 마커를 넣는다.

```yaml
translation_source: kimi-cli
translated_at: 2026-05-19T03:00:14+00:00
last_polished_at: 2026-05-19T03:00:14+00:00
```

`translation_source`는 자동 번역물임을 식별하기 위한 라벨이다. `translated_at`은 마지막으로 새로 번역되었거나 drift가 해소된 시점, `last_polished_at`은 마지막 polish 시점. 처음 fresh 번역하거나 drift로 다시 번역할 때는 `last_polished_at`을 일부러 비워두는데, 그래야 polish 큐에 다시 잡혀서 어색한 문장을 다음 polish 때 다듬을 기회가 생긴다.

## 망가지기 쉬운 부분

번역은 텍스트만 들어갔다 나오는 일이 아니다. 이 블로그의 글들은 대부분 수식과 인용과 카테고리 라벨을 포함하고, 번역기가 그것들을 모두 무사히 통과시킨다고 믿을 수는 없다. 그래서 워커는 결과물을 받자마자 몇 가지 검사를 돌린다.

- **Truncation guard**: 출력 본문이 한글 본문 길이의 60% 미만이면 실패 처리. polish의 경우엔 추가로 기존 영어판의 85% 미만이어도 실패. polish는 다듬는 일이지 줄이는 일이 아니어야 하니까.
- **Math block audit** (`math_block_audit.py`): `$$...$$` 블록 개수가 한글/영어 사이에 어긋나면 알린다. 단순히 개수만 비교하는 대신, mismatch가 발견되면 Kimi에게 *어디서 어떻게 어긋났는지*를 다시 검증시킨 후 그 내용을 텔레그램으로 보낸다. 다음의 요청에서 만들어진 흐름이다:

  > 그러지 말고, `$$...$$` 개수가 다르면 kimi한테 다시 검증시킨다음, 어디서 바뀌었는지, 문제는 없는지 파악시킨 다음 그 내용을 텔레그램으로 보내주면 어때?

- **Label normalization** (`label_normalize.py`): "예시 1", "명제 5" 같은 한글 라벨이 번역물에 그대로 남아있는 경우 잡아낸다.
- **Translation loss audit** (`translation_loss_audit.py`): 줄 수 기준으로 한글→영어 손실률을 계산해서 의심스러운 파일들을 보고한다. 한 번 모든 글의 fresh 번역이 끝난 시점에 일괄로 돌렸고, 손실이 큰 파일은 영어판을 삭제해서 fresh 큐에 다시 올렸다.

Timeout은 25분으로 잡혀있다. 처음엔 15분이었는데, 큰 글(30KB 이상)이 중간에 잘려나가는 일이 있어서 늘렸다.

> kimi_timeout_sec을 좀 늘리자. 25분 정도로.

## 번역물 표시

자동 번역물이 사람이 쓴 글인 척 페이지에 떠 있는 것은 정직하지 않다. `_includes/translation-notice.html`은 `translation_source: kimi-cli` 마커가 달린 글에 한해 페이지 맨 위에 안내 배너를 띄운다.

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

영어 페이지에는 영어 안내가, 한글 페이지에는 한글 안내가 뜬다. 정확히 말하면 한글 페이지에는 이 마커가 있을 일이 없으니 후자는 거의 보이지 않는 안전망에 가깝지만, 둘 다 등록해두는 편이 일관적이라 그대로 남겨두었다.

## 현재 상태

수십 편의 한글 글이 영어판을 갖게 되었고, 한글이 갱신되면 30분 이내에 drift가 잡혀 다시 번역된다. 새로 쓸 한글 글이 없는 시기에는 워커가 polish 큐를 처리하며 14일 묵은 영어판을 하나씩 다듬는다. 텔레그램 알림은 가끔 새벽에 mismatch를 알려오고, 대부분은 별 일 아니지만 가끔 잘못된 번역이 잡히기도 한다.

자동 번역은 사람의 번역만큼 정확하지 않고, kimi_translation_notice 배너가 그 사실을 매 글 머리에 작은 글씨로 적어둔다. 완벽하지 않은 채로 굴러가는 편이 굴러가지 않는 것보다는 낫다.

## 사후: LLM에게서 frontmatter 회수

위의 흐름으로 한동안 잘 돌아갔는데, 시간이 지나면서 어떤 종류의 오염이 영어판 frontmatter에 누적되고 있다는 것이 보였다. 어느 날 점검을 해보니 영어판 파일 177개의 첫 줄이 `---title: "..."`로 시작하고 있었다 — 여는 `---`와 첫 frontmatter key 사이에 줄바꿈이 빠져있는 형태이다. 이 상태에서는 워커 내부의 `_FRONTMATTER_RE` 정규식이 frontmatter 블록을 인식하지 못해서 `_inject_translation_meta`가 silent no-op로 빠지고, 결국 마커가 붙지 않은 채 그대로 디스크에 적힌다.

원인은 Kimi와 MiMo 둘 다 간헐적으로 출력에서 `\n`을 한 칸 누락하는 경우가 있다는 것이었다. 그 누락이 `---`와 첫 키 사이에서 일어나면 한 글의 frontmatter가 통째로 깨진다. 첫 대응은 `call_kimi()`에 한 줄짜리 패치를 넣는 것이었다 — 응답이 `---X`로 시작하고 `X`가 줄바꿈이 아니면 `\n`을 끼워넣는다. 같은 패치로 이미 깨져있던 177개 파일도 일괄 보정했다.

> Kimi/MiMo가 `---title:`을 붙여 출력하는 일이 잊을 만하면 한 번씩 도착한다. 그 때마다 한 줄짜리 가드를 더 두는 게 답일까.

답은 "아니오"였다. 같은 종류의 frontmatter 오염이 다른 형태로 또 나올 것이 분명했다 — `description` 필드가 quote 없이 쓰여서 YAML이 깨지거나, sidebar 블록의 indentation이 한 칸 어긋나거나. 매번 가드를 한 줄씩 추가하는 것은 끝이 없는 작업이다. 사용자가 설계를 다시 잡자는 방향을 정했다.

새 흐름의 핵심은 **LLM에게 frontmatter를 맡기지 않는다**는 것이다. 워커가 KO 파일을 frontmatter 블록과 body로 직접 분리하고, body만 Kimi에게 넘긴다. LLM은 body를 받아 body를 돌려주고, 여는 `---`도 frontmatter 키도 응답에 들어오지 않는다.

흐름은 다음과 같이 재편됐다:

1. KO 파일을 frontmatter 블록과 body로 분리.
2. `title` / `excerpt` / `description` 세 필드만 따로 작은 Kimi 호출로 번역 (JSON으로 받아옴). polish 경로에서는 기존 EN 값을 그대로 보존.
3. Body 번역(또는 polish): Kimi가 body만 받고 body만 돌려준다. INSTRUCTIONS에서 frontmatter 관련 규칙은 모두 제거.
4. Body 후처리: 라벨 번역 잔재 정리(`label_fix`), `<sub>` 태그 제거(영어판에서는 한영 병기가 무의미하므로 한국어 sub 텍스트만 들어있던 자리가 정리된다), 그리고 `/ko/` → `/en/` 일괄 치환. 마지막은 validator의 `/ko/` 검사가 사후에 한 번 더 잡지만, body가 validator에 도달하기 전에 이미 정상화돼 있으므로 defense-in-depth.
5. EN frontmatter를 워커가 결정적으로 합성: `permalink` 은 `/ko/` → `/en/`, `sidebar.nav` 은 `-ko` → `-en`, `title`/`excerpt`/`description` 은 2단계에서 받은 값, 나머지 키는 KO에서 그대로 복사, 그리고 `translated_at` / `translation_source` / `last_polished_at` 마커 삽입.
6. 조립된 결과물을 validator에 통과시킨다 (수식 블록 개수, `<ins>` id 정합성, 라벨 잔재).

새 흐름에서 LLM의 작업 범위는 줄어들었다. body 번역과 세 필드의 짧은 번역, 그 둘만 LLM의 일이다. 나머지는 모두 결정적 코드가 처리하고, 결정적 코드는 같은 입력에 같은 결과를 돌려준다. LLM이 같은 입력에 같은 결과를 돌려주지 않는다는 점은 새 흐름의 전제이지 더 이상 디버그 대상이 아니다.

부수효과로 cross-reference 처리도 같이 정리됐다. LLM이 자신 없는 링크는 KO 형태로 그대로 두라는 규칙이 INSTRUCTIONS에 들어갔고, 별도의 [link-normalizer 플러그인](/ko/llm_workshop/link_normalizer)이 빌드 시점에 표시명을 canonical로 덮어쓰므로, LLM이 정확한 표기를 떠올릴 필요가 없어졌다.

새 흐름을 도입한 후 cron은 일단 일시정지해두었다. 새 코드로 첫 몇 편을 손으로 돌려보고 결과가 깨끗한지 확인한 뒤에 다시 켤 예정이다. 워커가 멈춰있는 동안에는 자동 번역도 멈춘다.
