---

title: "description 일괄 생성"
excerpt: "MiMo 토큰 리셋 이벤트와 GSC 가시성, 그리고 한 줄 잘림 버그"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/descriptions_batch

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-27
last_modified_at: 2026-05-27
weight: 14

---

관련 파일: `scripts/audit/gen_descriptions.py` (배치 완료 후 일회성 스크립트라 [정리 commit](https://github.com/math-jh/math-jh.github.io/commit/00e77210)에서 삭제됨)
{: .notice--info}

[Sitemap 없이 색인하기](/ko/llm_workshop/gsc_indexing)에서 GSC URL Inspection의 결과를 적었다 — 안 보이는 KO `/math/` 글 200여 개의 verdict는 모두 `"Google에는 아직 알려지지 않은 URL"`이었고, 그건 description 부재 같은 메타 문제가 아니라 그냥 Google이 페이지 자체를 아직 색인하지 않은 상태였다. description은 1차 원인이 아니었다.

다만 description이 *2차* 가치 — indexed 페이지의 CTR 개선 — 를 한다는 것 자체는 사실이다. 검색 결과 페이지에서 제목 아래 두 줄을 비워두는 것보다 글의 요약 한 줄이 있는 편이 클릭률이 올라간다. 그리고 글의 head에서 `<meta name="description">`이 비어있으면 검색 결과에 표시할 요약이 없다. 그 빈자리를 메우는 작업은 1차 문제와 분리해서 진행할 수 있었고, 그래서 비어있던 269개 글에 description을 한 번에 채워넣으라는 지시가 떨어졌다.

## MiMo 토큰 리셋

description은 frontmatter에 한 줄 추가되는 짧은 텍스트라 LLM에게 시키기에 부담이 적다. 어느 모델을 쓸지 정하던 중, MiMo 한 달치 토큰이 이상한 시점에 리셋됐다 — 사용자의 결제 사이클상 다음 리셋까지 하루 남은 상태였는데, 그 직전에 MiMo가 "이벤트"라는 이름으로 모든 사용자 토큰을 한 번 더 새로 풀었다. 즉, 하루만 지나면 자연 리셋으로 다시 풀릴 토큰이, 그 하루 전에 보너스로 한 번 더 들어와 있는 상태였다.

> MiMo 토큰 갑자기 리셋됐는데, 어차피 내일 리셋되니까 오늘 다 안 쓰면 그냥 휘발이야

보너스 토큰을 안 쓰면 24시간 안에 자연 리셋이 그것을 덮어쓰고, 그러면 두 번째 리셋분만 남아 추가 보너스가 통째로 사라진다. 그래서 description 작업을 그날 안에 burst로 처리하기로 했다. 24시간 마감 안에 269개 글에 description을 다는 일이 토큰 만료 시점과 맞아떨어졌다.

3분에 한 번씩 한 글을 처리하는 cron으로 짰다. 269개 × 3분 ≈ 13.5시간으로 24시간 안에 들어간다. 3분 간격은 MiMo의 rate limit과 평균 응답 시간을 고려한 보수적인 페이스다. 더 빠르게 호출할 수도 있지만, rate limit에 걸려 fallback 흐름으로 빠지면 시간 비용이 더 크다.

```
*/3 * * * * cd .../scripts/audit && python3 gen_descriptions.py >>gen.log 2>&1
```

`gen_descriptions.py`는 단순하다. 모든 KO 글을 훑어 `description:` 필드가 비어있는 것 중 하나를 골라 MiMo에 본문을 보내고, 응답을 그 자리에 채워넣는다. polish는 안 한다 — 처음 채우는 description 한 줄을 빠르게 푸시하는 것이 목표였다.

## MiMo의 두 가지 누수

batch가 절반쯤 돌았을 때 두 가지 문제가 같이 나왔다.

첫째, MiMo의 출력에 한자가 섞여 들어오는 경우가 있었다. 예를 들어 description에 `이 글은 X에 대한 介绍이다` 처럼 한국어 문장에 중국어 단어가 끼어드는 것이다. MiMo는 한국어 학습이 얇은 영역에서 다국어 leakage가 있고, 짧은 출력에서 더 두드러진다. 8개의 description에 한자 leakage가 있었다. grep로 잡아서 다시 돌렸다 — 같은 입력에 다시 호출하면 보통 두 번째 시도에서 한국어로만 출력된다.

> 介绍 → 소개로 다시 쓰게 다시 돌려

> 兑现도 있다, 이건 실현이 맞을 것 같고

> 일본어 가타카나 한 글자 끼어든 것도 하나 있어

이런 식으로 사용자가 손으로 한 번 더 sweep을 했다. 짧은 출력의 한자 leakage는 정규식 한 줄로 잡힌다 — `[一-鿿]`가 description에 포함되면 재생성 대상이다. 같은 패턴이 다시 나타나면 그때 자동화하기로 하고, 이번엔 손으로 마무리했다.

둘째, 출력이 끊겨버리는 timeout이 7개 글에서 났다. 큰 글 (30KB 이상)에서 MiMo가 본문을 절반쯤 읽고 응답을 시작하기 전에 timeout에 걸리는 경우였다. 이 7개는 사용자가 직접 description을 적어넣었다 — 큰 글은 사람이 한 줄로 요약하는 편이 더 빨랐다.

## 결과

269개의 KO 글이 frontmatter에 `description:` 한 줄을 갖게 되었다. 영어판은 translate_worker가 그 description을 영어로 옮기는데, translate_worker의 cron이 일시 정지된 상태라 cron이 재개되면 처리된다.

`gen_descriptions.py`는 [정리 commit](https://github.com/math-jh/math-jh.github.io/commit/00e77210)에서 삭제했다. 한 번 돌리고 끝나는 스크립트는 저장소에 남길 필요가 없고, 같은 일을 다시 해야 한다면 다음에 새로 짜는 편이 낫다.

GSC 검색 결과에서 description이 눈에 띌 만한 변화를 만드는지는 며칠 더 두고 봐야 한다. URL Inspection이 가르쳐준 1차 원인 — *Google이 아직 페이지를 모른다* — 은 그대로이고, description은 그 다음의 작은 보정이다. 다만 1차 문제가 풀리기만 기다릴 수는 없으니 할 수 있는 작업을 먼저 처리했다. 토큰이 휘발하기 전에 쓴 것뿐이라는 점은 굳이 부정하지 않겠다.
