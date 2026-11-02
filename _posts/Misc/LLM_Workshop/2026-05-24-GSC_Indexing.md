---

title: "Sitemap 없이 색인 세기"
excerpt: "멈춘 GSC sitemap 대신 URL 검사로 색인을 세는 모니터, IndexNow 제출기, description 269편 일괄 생성"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/gsc_indexing

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-05-24
last_modified_at: 2026-11-02

weight: 10

---

관련 파일: `scripts/index-monitor/inspect_monitor.py`, `scripts/index-monitor/index_ranking.py`, `scripts/indexnow/submit.py` (셋 다 로컬 전용), [`_config.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_config.yml), [`_includes/seo.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/seo.html), `scripts/audit/gen_descriptions.py` ([정리 commit](https://github.com/math-jh/math-jh.github.io/commit/330f453b)에서 삭제)
{: .notice--info}

이 블로그의 Google Search Console sitemap은 2024년 10월 22일 이후 한 번도 fetch되지 않았다. 그사이 글이 350개가량 늘었는데도 GSC의 indexed 페이지 수는 197 근처에 머물렀다. 지금은 URL Inspection API로 글마다 색인 여부를 묻는 모니터가 매일 미색인 글 10개를 골라 주고, 다른 엔진에는 IndexNow 제출기가 바뀐 URL을 통보한다. 검색 결과의 요약 한 줄은 5월에 한꺼번에 채운 `description:`이다.

## 멈춘 sitemap 보고서와 Indexing API 우회

처음에는 사용자의 지시로 싼 리셋부터 시도됐다. 새 sitemap 경로(`/sitemap-2026.xml`)를 robots.txt와 같이 푸시하기, GSC property를 지웠다 재등록하기. 둘 다 무효였고, 재등록한 property도 똑같이 멈췄다. GSC의 Sitemaps 페이지가 내부적으로 부르는 RPC는 이런 응답을 돌려줬다.

```
errors: 0
warnings: 0
isPending: true
lastDownloaded: 2024-10-22T01:29:54Z
contents: [{type: web, submitted: 194, indexed: 0}]
```

`errors: 0`이고 `isPending: true`다. fetch가 실패하는 것이 아니라, 큐에 올라간 채 1.5년째 처리되지 않는 상태다. Webmasters API로 sitemap entry를 DELETE한 뒤 다시 PUT해도 `lastSubmitted`만 갱신되고 `lastDownloaded`와 `contents`는 그대로였다.

> sitemap 수정도 안 통하고, property 재등록도 안 통하면 남은 게 뭐야

사용자는 커스텀 도메인으로 옮겨 새 사이트로 보이게 하는 것보다 sitemap을 건너뛰는 쪽을 먼저 골랐고, 첫 구현은 새 글과 바뀐 글을 매일 Google Indexing API에 밀어 넣는 크론이었다. Indexing API는 공식적으로 JobPosting·BroadcastEvent 전용이지만 일반 페이지에도 200 OK를 돌려준다. 그 200은 공허했다. 며칠을 밀어 넣어도 색인율은 반응하지 않았고, 6월 2일에 이 경로는 폐기됐다. 별도 저장소였던 `~/Projects/indexing/`도 그때 지워졌다.

그 사이에 사용자가 알려 온 것이 지금 구조를 정했다.

> URL inspect 해보니까 indexed인데, indexed pages 리스트에는 없는 페이지가 있어

URL 검사로 하나씩 물으면 "indexed"인 페이지가 GSC의 indexed 목록에는 없었다. 집계 화면의 숫자에는 캐시와 지연이 섞여 있어 판단 근거가 되지 못한다. 믿을 만한 신호는 URL Inspection API가 URL 하나마다 돌려주는 verdict뿐이고, 지금의 모니터는 그것을 매일 세는 일이다. 색인 큐에 미는 자동화를 짰다가, 무엇이 안 들어갔는지 세는 자동화로 물러난 셈이다.

## URL 검사 모니터의 대상 집합과 실행 모드

`inspect_monitor.py`는 매일 03:00 크론으로 `~/.venvs/indexing`의 python에서 돈다 (google-auth와 requests가 필요하다). 서비스 계정 키와 상태 파일이 같은 폴더에 있어서 `scripts/index-monitor/` 전체가 `.git/info/exclude`에 올라 있다. 조회하는 속성은 도메인 속성 `sc-domain:math-jh.com` 하나다. `math-jh.github.io`는 전부 `math-jh.com`으로 301 리다이렉트되므로 같은 글을 두 주소로 물을 이유가 없다.

대상은 실제로 배포된 글뿐이다.

```python
def target_paths():
    """Published post permalink paths = front-matter permalinks ∩ sitemap."""
    perms = post_permalinks()
    sm = sitemap_paths()
    matched = sorted(p for p in perms if norm(p) in sm)
    return matched, len(perms), len(sm)
```

`post_permalinks()`는 `_posts/**/*.md`의 front matter 블록만 읽어서 본문에 예시로 적힌 permalink를 잡지 않는다. 배포 여부는 교집합의 다른 쪽인 프로덕션 `sitemap.xml`이 정한다. front matter 쪽은 `published: false`인 글을 빼되 `revising: true`면 남긴다. 개정 중인 글은 CI가 직전 발행 판본을 복원해 배포하므로 구글에는 그대로 떠 있다.

실행 모드는 요일이 정한다.

- **full** (일요일, 또는 상태 파일이 없을 때): 대상 전부를 스레드 10개(`ThreadPoolExecutor`)로 조회한다. 680여 개에 10분 가까이 걸리고, 색인 해제는 이 스윕에서만 잡힌다.
- **daily** (나머지 요일): 어제 배치를 다시 조회한 뒤, 미색인이고 쿨다운이 아닌 후보를 순위대로 10개씩 조회하다가 미색인이 10개 모이면 멈춘다. 하루 조회는 15개 안팎이다.

네트워크 오류·타임아웃·429·5xx는 3초, 9초 뒤에 두 번까지 다시 시도하고, 401·403 같은 확정 응답은 권한 문제를 가리지 않도록 재시도하지 않는다. 재시도는 실행 전체가 `RETRY_BUDGET = 40`을 락으로 나눠 쓴다. 모든 요청이 타임아웃되는 날 전체 스윕이 끝없이 늘어지지 않게 하는 상한이다.

상태 파일 `state-com.json`은 경로마다 항목 하나를 둔다 (값은 자리표시).

```json
"urls": {"/ko/math/...": {
  "indexed": false, "verdict": "...", "coverage": "...", "lastCrawlTime": "...",
  "googleCanonical": "...", "userCanonical": "...",
  "since": "YYYY-MM-DD", "last_checked": "YYYY-MM-DD", "snooze_until": "YYYY-MM-DD",
  "rec_state": {"indexed": false, "coverage": "...", "lastCrawlTime": "..."}}}
```

최상위에는 `urls` 말고 `last_full_sweep`과 그날 확정한 추천 배치 `last_batch{date, paths}`가 있다. `since`는 `indexed` 값이 마지막으로 바뀐 날이다. 조회가 오류로 끝나면 `last_checked`와 `last_error`만 적고 색인 상태는 건드리지 않는다.

## 추천 순위 규칙과 잊은 요청의 재추천

하루 10개를 고르는 규칙은 `index_ranking.py`에 따로 있다. 커버리지 상태마다 수동 "색인 생성 요청"이 실제로 먹히는 순서를 매긴다.

```python
COVERAGE_PRIORITY = {
    None: 0,                                                     # 한 번도 검사 안 됨(새 글)
    "URL is unknown to Google": 1,                               # 발견조차 안 됨
    "Discovered - currently not indexed": 2,                     # 알지만 크롤 전
    "Not found (404)": 3,                                        # 낡은 404
    "Duplicate, Google chose different canonical than user": 4,  # canonical 문제
    "Crawled - currently not indexed": 6,                        # 구글이 거절, 맨 뒤
}
```

추천 목록은 미색인이고 쿨다운이 아니며 진짜 canonical 충돌도 아닌 경로를 (버킷 순위, `since`, 경로)로 정렬한 앞의 10개다. 같은 버킷 안에서는 오래 미색인이던 글이 먼저 나온다. 한 번 추천된 글은 `snooze_until`이 14일 뒤로 잡혀서, 목록이 같은 열 개로 매일 조르지 않고 돌다가 수익률 낮은 Crawled 더미까지 내려간다. 11월 2일 상태 파일로는 682개 중 321개가 색인돼 있고, 미색인 361개 가운데 303개가 `Crawled - currently not indexed`다.

추천할 때는 그 글의 `indexed`·`coverage`·`lastCrawlTime`을 `rec_state`로 찍어 둔다. 요청을 실제로 누르면 다음 날까지 셋 중 하나는 거의 항상 움직인다. 다음 날 다시 조회했는데 셋 다 그대로이면 요청이 빠진 것으로 보고 쿨다운을 풀어 목록 맨 앞에 "어제 무변화(요청 누락?)"로 다시 올린다. 사람이 버튼을 눌렀는지를 구글 쪽 흔적으로 거꾸로 추정한다. 이 판정은 순위 3 이하(`VERIFIABLE_MAX_RANK`)에만 적용된다. Crawled 버킷은 요청을 눌러도 다음 날 무변화가 정상이다.

canonical 계열(`Duplicate…`) 중 구글이 같은 경로의 옛 `*.github.io` 주소를 canonical로 잡은 것은 도메인 이관의 잔재라 요청이 도움이 된다. 구글이 아예 다른 페이지를 골랐으면 요청으로 고칠 수 없으므로 로테이션에서 빼고 메시지의 별도 칸에만 적는다.

이 모듈은 블로그 대시보드의 `#index` 화면(`server.py`의 `sec_gsc()`)도 import한다. 그날 크론이 확정한 `last_batch`가 있으면 그것을, 없으면 같은 `recommend_from_state()`로 고른다. 규칙이 한 파일에 있어야 대시보드가 크론이 뽑지 않은 URL을 "오늘 요청할 것"으로 보여 주지 않는다. 대시보드는 venv 없이 `/usr/bin/python3`로 돌기 때문에 이 모듈은 표준 라이브러리만 쓴다.

메시지는 알림 shim(`~/.local/bin/notify --digest`)으로 하루 요약에 묶여 나가고, URL 집합이 지난 알림과 같으면 보내지 않는다. 그 열 개를 GSC의 URL 검사 화면에 넣고 "색인 생성 요청"을 누르는 것은 사용자 손이다. 하루 10개라는 수도 그 수동 창구의 한도에 맞춘 것이다.

## 서비스 계정의 owner 등록

모니터는 OAuth 사용자 토큰이 아니라 서비스 계정(SA) 키로 인증한다. 옛 사용자 토큰은 6월 4일에 만료됐고, SA 자격증명에는 만료되거나 폐기될 refresh token이 없다. 대신 URL Inspection API는 Full 사용자 권한의 SA에게 `PERMISSION_DENIED`를 돌려주므로, SA 이메일이 그 속성의 owner여야 한다.

SA를 GSC에 올리는 단계는 Indexing API 시절에 한 번 막혔었다. "사용자 추가"에 SA 이메일을 넣으면 "이메일을 찾을 수 없습니다"가 떴고, 오타·UI 언어·시크릿 창을 다 확인한 뒤에야 원인이 나왔다. SA가 속한 GCP 프로젝트에 Web Search Indexing API와 Site Verification API가 enable되어 있지 않으면 GSC는 그 이메일을 없는 사용자로 취급한다.

owner 권한은 SA가 Site Verification API로 소유권을 직접 확인해서 얻는다. 토큰을 받아 사이트에 두고 `webResource`를 호출하면 owner 목록에 SA 이메일이 들어간다. github.io 시절의 URL-prefix 속성에는 FILE 방식을 썼고, 그 토큰 파일 `google5b28d33373f8fc5c.html`이 지금도 루트에 있다. 도메인 속성은 DNS 레코드로만 확인되므로 `sc-domain:math-jh.com`의 소유권은 Cloudflare의 `google-site-verification` TXT 레코드에 걸려 있다. Google이 주기적으로 다시 확인하므로 그 레코드를 지우면 SA의 권한도 빠진다.

## IndexNow 키 파일과 사이트맵 diff 제출기

구글 밖의 엔진은 [8월 초에 등록했다](https://github.com/math-jh/math-jh.github.io/commit/f42ae11e). Bing은 `_config.yml`의 `bing_site_verification`에 토큰을 채우면 `seo.html`이 `msvalidate.01` meta로 내보낸다. 네이버도 같은 블록의 `naver_site_verification`에 토큰을 두는데, 기존 토큰이 만료돼 서치어드바이저에서 [재발급받아 바꿨다](https://github.com/math-jh/math-jh.github.io/commit/dcb086ef).

IndexNow는 meta 태그가 아니라 루트에 놓인 키 파일의 HTTP 응답으로 인증한다.

```yaml
# IndexNow(Bing·Naver·Yandex·Seznam·Yep 공용)는 meta 태그가 아니라 루트의 키 파일로
# 인증한다: /059d61933cc601464ea45413f398ad2b.txt
# 제출기는 scripts/indexnow/submit.py (로컬 전용, .git/info/exclude 등재).
```
{: data-filename="_config.yml"}

파일 이름, 파일 내용, `submit.py`의 `KEY` 상수가 모두 같은 키 문자열이고, 이 파일은 커밋되어 배포까지 가야 한다. 참여 엔진은 한 곳에 제출된 URL을 서로 공유한다. 구글은 IndexNow에 참여하지 않으므로 모니터와 역할이 겹치지 않는다.

`submit.py`는 매일 03:10에 시스템 python3로 돈다 (표준 라이브러리만 쓴다). 배포된 `https://math-jh.com/sitemap.xml`의 `lastmod`를 지난 실행분과 비교하는 것이 하는 일의 전부다.

```python
changed = [u for u, m in live.items() if prev.get(u) != m]
# 사이트맵에서 사라진 URL 은 제출하지 않고 상태에서만 지운다. revising·미발행
# 전환으로 일시적으로 빠지는 경우가 있어, 삭제 통보는 되돌리기가 어렵다.
dropped = [u for u in prev if u not in live]
```

기준을 로컬 `_site`나 preview 호스트가 아니라 프로덕션 사이트맵으로 잡은 것이 이 스크립트의 핵심 결정이다. 로컬을 보면 아직 발행하지 않은 글이 새어 나갈 수 있고, preview 호스트에는 미발행분이 통째로 있다. 상태 `state.json`은 `{url: lastmod}` 하나다. 상태 파일이 없으면 전량 제출을 막고 `--bootstrap`을 요구하고, 제출 전에는 키 URL의 본문을 대조해 키 파일이 아직 배포되지 않았으면 건너뛴다. 배치 하나라도 실패하면 상태를 갱신하지 않아서 다음 실행이 같은 diff를 다시 보낸다.

## MiMo 보너스 토큰과 description 269편

`seo.html`은 meta description을 `page.description`, `page.excerpt`, 사이트 설명 순으로 고른다. 5월 말까지 KO 수학 글 269편에는 `description:`이 없어서 짧은 excerpt 구절이 그 자리에 나갔다. 안 보이는 글의 원인이 이것은 아니었다. URL Inspection API로 샘플 다섯 개를 조회하니 모두 `verdict=NEUTRAL, coverageState="Google에는 아직 알려지지 않은 URL"`이었고, description은 색인된 글의 클릭률을 올리는 2차 보정일 뿐이다. 사용자는 그래도 비어 있던 269편을 한 번에 채우라고 했다.

모델은 MiMo였다. 사용자의 결제 주기상 다음 리셋까지 하루 남은 날, MiMo가 "이벤트"로 모든 사용자의 한 달치 토큰을 한 번 더 풀었다.

> MiMo 토큰 갑자기 리셋됐는데, 어차피 내일 리셋되니까 오늘 다 안 쓰면 그냥 휘발이야

그래서 배치는 그날 안에 끝나야 했다. `gen_descriptions.py`는 `_posts/Math/*/ko/*.md` 중 `description:`이 없는 글을 모아 하나씩 순서대로 `claudemimo -p`로 MiMo에 보냈다. 본문은 `$$…$$`와 `$…$`를 지우고 공백을 접은 뒤 앞 1500자만 넘긴다. 프롬프트는 1~2문장 80~140자, 한자·수식 기호 금지, "이 글에서는" 같은 메타 표현 금지를 요구한다. 결과는 front matter의 `title:` 다음 줄에 들어가고, description이 이미 있는 글은 건너뛰므로 다시 돌려도 된다. 호출 하나의 타임아웃은 120초다.

MiMo는 짧은 한국어 출력에 다른 언어를 섞었다. `이 글은 X에 대한 介绍이다` 같은 식이다. 스크립트는 아래 정규식에 걸린 결과를 `HAN_LEAK`으로 로그에 남기되 일단 그대로 쓰고, 정리는 뒤로 미뤘다.

```python
HAN = re.compile("[一-鿿㐀-䶿豈-﫿]")
```

사용자가 결과를 한 번 더 훑으며 고칠 것을 짚었다.

> 介绍 → 소개로 다시 쓰게 다시 돌려

> 兑现도 있다, 이건 실현이 맞을 것 같고

> 일본어 가타카나 한 글자 끼어든 것도 하나 있어

세 번째는 정규식이 잡을 수 없는 경우였다. `HAN`의 범위는 CJK 통합 한자, 확장 A, 호환 한자뿐이고 가타카나(U+30A0~U+30FF)는 없다. 그 한 글자는 사용자 눈에만 걸렸다. 다른 문자가 섞인 8편은 지우고 다시 생성했고, 대개 두 번째에는 한국어로만 나왔다. 타임아웃으로 빈손이 된 7편은 사용자가 직접 적었다.

더 큰 사고는 생성기 쪽에 있었다. `parse_frontmatter()`가 front matter를 `text[4:end]`로 잘라 여는 `---` 뒤의 줄바꿈을 버렸고, 되쓰기가 `"---" + new_fm`이어서 51편의 머리가 `---title:`로 붙었다. [수정 commit](https://github.com/math-jh/math-jh.github.io/commit/75e9e695)은 되쓰기를 `"---\n" + new_fm.lstrip("\n")`으로 바꿨고, 깨진 51편은 배치 커밋에서 같이 복구됐다.

KO 269편을 한꺼번에 건드리면 번역 워커가 그것을 원문 drift로 읽고 EN 본문을 다시 번역하려 든다. 같은 배치의 `bump_en_translated_at.py`가 EN 짝들의 `translated_at`을 24시간 뒤로 밀어 그 판정을 피했다. EN의 description은 번역 워커가 `title`·`excerpt`와 같이 별도의 작은 프롬프트로 옮긴다. 두 생성 스크립트는 일회용이라 배치가 끝난 날 [정리 commit](https://github.com/math-jh/math-jh.github.io/commit/330f453b)에서 지웠다. 토큰이 휘발하기 전에 쓴 것뿐이라는 점은 굳이 부정하지 않겠다.
