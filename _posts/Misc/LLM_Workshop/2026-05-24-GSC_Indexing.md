---

title: "Sitemap 없이 색인하기"
excerpt: "Frozen된 GSC sitemap을 옆에 두고 Indexing API로 우회 운영하기"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/gsc_indexing

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-24
weight: 11

---

관련 경로: `~/Projects/indexing/` (별도 저장소), 사이트 root의 verification 파일 한 줄
{: .notice--info}

이 블로그의 Google Search Console sitemap은 2024년 10월 22일 이후 한 번도 fetch되지 않았다. 1.5년이다. GSC UI에서는 "Couldn't fetch"로 표시되지만, 능동적인 실패라기보다는 큐에 pending된 채 멈춘 frozen 상태에 가깝다는 것을 나중에 알게 되었다. 그동안 GSC indexed 페이지 수는 197에서 거의 움직이지 않았다 (그새 글이 350개가량 더 들어왔는데도). 사용자는 이걸 어떻게든 풀어보고 싶어했다.

사용자의 지시로 여러 가지가 시도됐다. 새 sitemap 경로(`/sitemap-2026.xml`)를 robots.txt와 같이 푸시해보기, GSC property를 지웠다 재등록하기. 둘 다 무효였다. 재등록한 property도 똑같이 stuck됐는데, 이건 sitemap 캐시가 property가 아니라 사이트 단위의 internal flag에 묶여 있을 수 있다는 신호였다. 즉 cheap reset은 다 소진된 셈이었다.

> sitemap 수정도 안 통하고, property 재등록도 안 통하면 남은 게 뭐야

이 한 줄에 대한 두 가지 옵션이 있었다 — (a) 커스텀 도메인으로 옮겨서 GSC 입장에서 새 사이트로 보이게 하기, 또는 (b) sitemap 자체를 우회해서 색인 요청을 다른 채널로 밀어 넣기. 사용자가 (b)를 먼저 시도하기로 결정했고, 다음의 자동화를 짜라는 지시가 떨어졌다.

## Indexing API 우회

Google Indexing API는 공식적으로는 JobPosting과 BroadcastEvent 페이지 전용이다. 일반 페이지에도 호출하면 200 OK가 떨어지고, 실제로 색인 큐에 들어간다 — 회색 영역이다. 광범위하게 사용되고 있고 막힌 사례를 못 봤지만, 보장은 없다.

자동화는 [`~/Projects/indexing/`](https://github.com/math-jh/math-jh.github.io)라는 별도 저장소에 올렸다. 이 블로그 저장소 안에 두지 말라는 사용자 지침이 있었다 — 서비스 계정 키와 OAuth 토큰을 같이 두고 싶지 않다는 이유, 그리고 cron으로 매일 도는 별개의 프로젝트로 분리해두는 편이 깔끔하다는 이유였다. 구조는 `src/`, `scripts/`, `config/`, `state/`로 단순하고, 매일 03:00에 cron이 다음을 한다:

1. `https://math-jh.github.io/sitemap.xml`을 파싱
2. `state/state.json`과 대조해서 미제출 / lastmod 변경 / 14일+ stale URL 추출
3. 그 중 최대 180개(daily quota 200 - headroom)를 Indexing API에 푸시
4. 각 URL의 `submitted_at`, `lastmod`, `last_status`를 state에 기록

첫 백필이 2026-05-24에 시작되었고, 548개 URL이 약 3일에 걸쳐 큐에 들어갔다. State 파일 덕분에 중복 제출은 안 되고, 글이 수정될 때만 다시 제출된다.

## GSC user-add 막힘

서비스 계정에 GSC 권한을 주려고 "사용자 및 권한 > 사용자 추가"에 `indexing-bot@math-jh-indexing.iam.gserviceaccount.com`을 넣었더니 "이메일을 찾을 수 없습니다"가 떴다. 오타, UI 언어, 시크릿 창을 다 확인한 뒤에야 진짜 원인을 알았다 — 서비스 계정이 속한 GCP 프로젝트에 Web Search Indexing API와 Site Verification API가 enable되어 있지 않으면 GSC는 그 이메일을 "존재하지 않는 사용자"로 처리한다. API 두 개를 enable하고 15분 정도 기다리니 user-add가 통했다.

그래도 막히는 경우엔 Site Verification API로 프로그래매틱하게 verified owner로 등록할 수 있다 — 서비스 계정이 자기 자신을 verify하는 흐름이다. 토큰을 받아서 사이트 root에 `google<token>.html` 형태의 파일을 두고, 배포된 뒤에 verify를 호출하면 owner 목록에 SA 이메일이 들어간다. 이 블로그의 root에도 그 한 줄짜리 파일이 하나 있다. 지우면 SA의 인덱싱 권한이 빠진다 — Google이 주기적으로 fetch해서 소유권을 재검증하기 때문이다.

## GSC 내부 상태

UI의 "Couldn't fetch"가 정확히 무엇을 의미하는지 보려고 DevTools 네트워크 탭과 Webmasters API를 같이 두드려봤다. GSC의 Sitemaps 페이지가 내부적으로 부르는 RPC는 다음과 비슷한 응답을 돌려준다:

```
errors: 0
warnings: 0
isPending: true
lastDownloaded: 2024-10-22T01:29:54Z
contents: [{type: web, submitted: 194, indexed: 0}]
```

`errors: 0`이 핵심이었다. 능동적인 fetch 실패가 아니다. 1.5년째 큐에 pending이지만 실제로 fetch는 안 되는 frozen 상태인 것이다. `indexed: 0`이라는 건 sitemap 채널을 통해 attribute되는 indexed page가 0개라는 뜻이지, 사이트의 색인이 0이라는 게 아니다 — 실제 색인된 페이지들은 sitemap이 아닌 다른 경로(Indexing API 푸시, 외부 링크 따라온 크롤러)로 들어왔기 때문에 이 sitemap report에 잡히지 않는다.

Webmasters API로 sitemap entry를 DELETE 후 PUT으로 reset도 해봤다. `lastSubmitted` 타임스탬프만 갱신되고 `lastDownloaded`와 `contents` 같은 cached data는 그대로였다. property-level 캐시가 sitemap entry op과 별도로 유지되는 모양이다. 결국 UI/API 어느 쪽으로도 unstick은 안 된다.

## Dashboard 숫자

며칠 뒤에 한 가지를 더 발견했다. KO `/math/` 글 318개 중 90일간 search impression이 한 번이라도 잡힌 게 50개뿐이어서, 나머지 202개가 진짜 안 색인된 건지 보려고 URL Inspection API로 다섯 개를 샘플 조회했다. 결과는 모두 `verdict=NEUTRAL, coverageState="Google에는 아직 알려지지 않은 URL"`이었다. 그래서 description 부재 같은 메타 문제가 아니라 그냥 페이지들이 아직 큐에서 소화되는 중인 것으로 보였다 — Indexing API 자동화가 가동된 지 3일밖에 안 됐을 때였다.

그런데 사용자가 곧 다른 걸 알려왔다:

> URL inspect 해보니까 indexed인데, indexed pages 리스트에는 없는 페이지가 있어

`/en/math/set_theory/zfc_axioms` 같은 페이지를 URL inspect로 조회하면 "indexed"가 떠도, GSC dashboard의 indexed pages 목록 어디에도 안 보인다는 것이다. 즉 dashboard의 집계 숫자(coverage 리포트의 "indexed: 48")는 캐시, lag, 샘플링이 섞여 있어서 신뢰할 수가 없다. UI에 "stuck"으로 보이는 게 진짜 stuck이 아닐 가능성이 크다는 뜻이다.

이 발견 이후로는 GSC 숫자로 Indexing API의 효과를 판단하는 걸 그만뒀다. 진짜 색인 상태는 `site:math-jh.github.io/en`이나 `site:math-jh.github.io/ko` 같은 검색의 결과 수로 sanity check하는 것이 더 정직하고, 트래픽은 결국 Google Analytics를 봐야 한다. GSC dashboard는 보조 신호 정도로 다룬다.

## 정리

1.5년 stuck은 결국 풀지 못했다. 그렇지만 우회로는 가동 중이고, 진짜 색인 상태가 dashboard보다 좋다는 정황 증거도 있다. 지금 운영은 두 트랙이다 — 매일 03:00의 cron이 새 글과 변경된 글을 Indexing API에 푸시하고, GSC sitemap report는 그냥 frozen인 채로 둔다. verification 파일은 root에 영원히 남는다.

처음 풀고 싶었던 문제는 "왜 sitemap이 안 fetch되는가"였고, 실제로 푼 문제는 "그것을 풀지 않고도 운영하는 법"이었다. 일은 대체로 그런 식으로 끝난다.

## 사후: Indexing API 폐기 (2026-06-02)

위 「정리」에서 "매일 03:00 cron이 새 글을 Indexing API에 푸시한다"고 적었는데, 그 운영은 이후 폐기됐다.

무너진 건 이 글의 전제 그 자체였다. 일반 페이지에 Indexing API를 호출하면 200 OK가 떨어지고 "실제로 색인 큐에 들어간다"고 적었지만(위 「Indexing API 우회」), 그 200은 공허했다. publish 호출은 매번 성공으로 돌아왔는데 정작 색인율은 거기에 반응하지 않았다 — 며칠을 밀어넣고도 절반이 채 안 되는 수준에 머물렀다. 회색 영역이라던 그 호출이, 적어도 이 사이트에서는 그냥 무효였던 것이다.

그래서 `~/Projects/indexing/` 저장소는 통째로 지웠다. 다만 사이트 소유권(root의 verification 파일)은 남겨뒀다 — 색인 상태를 *읽는* 데는 그게 여전히 필요하니까.

자리에 들어선 것은 푸시가 아니라 **모니터**다. 이 글이 이미 도달한 결론 — dashboard 숫자는 못 믿고 URL Inspection의 per-URL verdict가 정직하다 — 을 그대로 운영으로 옮긴 것이다. `scripts/index-monitor/`(이번엔 블로그 저장소 안에 두되 gitignore)가 매일 03:00에:

1. 각 글 URL을 URL Inspection API로 조회해 실제 색인 여부를 확인하고,
2. 미색인 URL을 모아 그날의 top 10을 텔레그램으로 보낸다.

그러면 사용자가 그 열 개를 GSC의 URL Inspection 화면에서 손으로 "색인 생성 요청"을 누른다. 자동 푸시가 무효라면 남는 건 콘솔이 인정하는 수동 경로 하나뿐이고, 하루 10개라는 수도 그 수동 창구의 한도에 맞춘 것이다.

조회 대상은 이제 `math-jh.com` 하나다. `math-jh.github.io`는 그쪽으로 301-리다이렉트되니 같은 글을 두 주소로 찍을 이유가 없다.

색인 큐에 밀어넣는 자동화를 짰다가, 무엇이 안 들어갔는지 매일 알려주는 자동화로 갈아탄 셈이다. 미는 일을 접고 세는 일로 물러났다.
