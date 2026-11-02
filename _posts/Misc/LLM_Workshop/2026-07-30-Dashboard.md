---

title: "블로그 운영 대시보드"
excerpt: "Jekyll을 거치지 않는 stdlib 서버 위에 개요 하나를 허브로 둔 운영 대시보드의 구조, 쓰기 경로, 재기동 스크립트, 파비콘"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/dashboard

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-30
last_modified_at: 2026-11-02
weight: 35

---

관련 파일: [`scripts/dashboard/server.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/server.py), [`scripts/dashboard/app.js`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/app.js), [`scripts/dashboard/restart.sh`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/restart.sh), [`scripts/dashboard/deploy/`](https://github.com/math-jh/math-jh.github.io/tree/main/scripts/dashboard/deploy), [`_includes/head.html`](https://github.com/math-jh/math-jh.github.io/blob/main/_includes/head.html)
{: .notice--info}

이 블로그에는 크론 워커가 여럿 돈다. 번역, 한글 수정 후속, 용어 추출, 의존성 링크 분류, 링크 감사, 색인 모니터가 각자 로그 파일과 state json을 하나씩 갖고 있어서, 상태를 보려면 그 파일들을 하나씩 열어야 했다. 사용자는 흩어진 상태를 한 화면에서 보고 싶어 했고, `preview.math-jh.com/dash/`가 그 화면이다. 이 글은 서버와 화면 쪽을 적는다. 워커가 멈췄는지, 오류가 났는지, 일부러 멈춘 것인지를 가르는 규칙과 정지 버튼, 감시 크론은 [워커 상태 판정과 감시 크론](/ko/llm_workshop/worker_health)에 따로 있다.

## Jekyll을 거치지 않는 stdlib 서버

`_config.yml`의 `exclude`에 `scripts`가 있어서 `scripts/dashboard/` 전체가 Jekyll 빌드에서 빠지고, git 추적은 그대로 된다. 대시보드의 데이터나 코드가 바뀔 때마다 사이트가 다시 빌드되는 일을 피하려는 것이다.

서빙은 `server.py`가 한다. 표준 라이브러리 `ThreadingHTTPServer`가 `127.0.0.1:8089`에서 정적 파일과 `/api/*`를 함께 내고, nginx는 `/dash/`를 이 포트로 곧장 `proxy_pass`한다.

```nginx
location = /dash { return 301 /dash/; }
location /dash/ {
    proxy_pass http://127.0.0.1:8089/;
    proxy_http_version 1.1;
    proxy_set_header Host $host:$server_port;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```
{: data-filename="scripts/dashboard/deploy/nginx-dash.conf"}

Jekyll dev 서버(4001)로 가는 `location /`을 거치지 않으므로 대시보드가 죽어도 블로그 본문은 영향받지 않고, 그 반대도 같다. nginx가 `/dash/` 접두사를 벗겨 보내기 때문에 `server.py`가 보는 경로에는 접두사가 없고, 화면 쪽의 자산·API 참조는 `/dash/…` 절대경로로 쓴다. livereload 주소를 바꾸는 `sub_filter`는 `location /` 안에만 있어서 이 블록으로 상속되지 않는다. nginx 설정과 crontab은 버전 관리 밖이라 `deploy/`에 재현용 조각 사본을 둔다.

```
*/5 * * * * /usr/bin/curl -sf -o /dev/null --max-time 5 http://127.0.0.1:8089/api/summary || setsid /usr/bin/python3 .../server.py >>....log 2>&1 </dev/null &
```
{: data-filename="scripts/dashboard/deploy/crontab.txt"}

5분마다 살아 있는지 찔러 보고, 응답이 없으면 다시 띄운다. 실제 crontab에는 같은 명령의 `@reboot` 줄이 하나 더 있어서, 크래시든 부팅이든 sudo 없이 유저 crontab만으로 덮인다. cron에서 뜬 프로세스에는 user-session 버스 환경이 없으므로, `server.py`는 시작할 때 `XDG_RUNTIME_DIR`과 `DBUS_SESSION_BUS_ADDRESS`를 채워 `systemctl --user is-active jekyll-blog`가 기동 경로와 상관없이 돌게 한다.

화면이 받는 데이터는 `/api/summary` 한 덩이다. `build_summary()`가 글 frontmatter 스캔, 번역 state, 워커 로그, 감사 리포트, 색인 모니터 state, `git log`, 미push 커밋 수를 한 번에 모으고, `app.js`는 그것을 60초마다 받아 오되 실패하면 마지막 스냅샷을 그대로 둔다. 워커의 규칙이 필요한 계산은 규칙을 옮겨 적지 않고 워커의 모듈을 import한다. 색인 추천 순위는 `index-monitor`의 `index_ranking`, KO-TYPOS 파싱은 번역 워커의 `ko_typos`, 링크 판정 버튼이 고칠 링크 찾기는 의존성 분류기의 파서를 쓴다. 사본을 두면 워커 쪽 규칙이 바뀔 때 대시보드만 옛 기준으로 남는다.

색인 추천은 import 하나로 끝나지 않는다. 03:00 배치가 오늘치 추천을 이미 뽑아 뒀으면 그것을 그대로 쓰고(`recommend_src="batch"`), 없을 때만 같은 모듈로 지금 계산한다(`"computed"`). 배치는 GSC 실측을 거치고 뽑힌 URL에 쿨다운을 걸기 때문에, 대시보드가 매번 다시 계산하면 다음 순번이 나온다. 추천 목록의 URL을 누르면 이동하지 않고 완결된 주소가 클립보드로 복사된다. GSC 검색창에 붙여 넣고 색인 요청을 누르는 동선에 맞춘 것이다([커밋](https://github.com/math-jh/math-jh.github.io/commit/6256feea51d03b4129b37aaaa4071aee4f246068)).

## 개요 허브와 hash 라우팅

처음 만든 형태는 워커·파이프라인·미발행·weight·번역·감사·색인·활동, 여덟 개 탭을 오가는 평범한 대시보드였다. 이틀 뒤 claude.ai/design 프로젝트의 handoff 번들로 리디자인이 들어갔고, 그 방향은 탭을 없애고 개요 하나를 허브로 삼는 것이었다. `/dash/`의 개요에는 판정 한 줄, 최근 24시간 실행 기록, 지표 카드 6장, 지금 볼 것, 파이프라인, 최근 커밋, 섹션 색인이 한 화면에 있고, 각 섹션은 거기서 들어갔다가 "← 개요로"로 돌아온다.

판정 한 줄은 워커 상태만 본다.

```js
function verdict(d) {
  var bad = badWorkers(d), ws = (d.workers || []).length, pz = pausedCount(d);
  var pnote = pz ? ' 일시정지 ' + pz + '건은 따로 세지 않았다.' : '';
  if (bad.length) return {
    ok: false, head: '워커 ' + bad.length + '개 점검 필요',
    sub: bad.map(function (w) { return w.name; }).join(' · ') + ' 의 로그가 주기보다 늙었다.' + pnote
  };
  return {
    ok: true, head: '워커 ' + ws + '개 모두 정상' + (pz ? ' (정지 ' + pz + ')' : ''),
    sub: '급한 일은 없다. 미발행 ' + num(d.stats.unpublished) + '편 · 재번역 대기 ' + num(d.stats.drift) + '편 · ...' + pnote
  };
}
```
{: data-filename="scripts/dashboard/app.js"}

미발행 초안이 몇 편 쌓였든, 색인 조치 대상이 몇 건이든 판정에는 안 들어간다. 그 숫자들은 `sub` 문장 끝에 적힌 대로 "오늘 안 해도 무너지지 않는 일"이라서 지표 카드로만 보인다. 급한 것과 급하지 않은 것을 첫 줄에서부터 가른 셈이다.

재번역 대기 수와 `#translation`의 큐는 대시보드가 세지 않는다. 처음에는 `translation_state.json`의 `status`를 셌는데, 그 필드는 마지막 사건이라 초안 시절에 찍힌 `draft_skip`이 발행 뒤에도 남았다. 사용자가 그 숫자를 의심한 뒤로 서버는 `translate_worker.py --queue`를 데몬 스레드로 돌려 그 출력을 읽는다. 워커의 `queue_bucket`은 다음 글을 고르는 `find_next_target`과 같은 순서로 단계를 매기므로 두 판정이 따로 놀 수 없다. 4~5초가 걸려서 글 목록·state·`_config.yml`의 mtime 묶음이 바뀔 때만 돌고, 실패한 실행의 시그니처도 기록해 깨진 워커를 다시 부르지 않는다([02e434c5](https://github.com/math-jh/math-jh.github.io/commit/02e434c5)).

라우팅은 hash다. `#drafts` `#weights` `#translation` `#audit` `#index` `#activity` `#cron`처럼 프래그먼트만 바뀌고 서버는 늘 같은 `index.html`을 준다. 워커와 파이프라인은 개요 안에서 소화되어 라우트가 없고, 워커 행을 누르면 로그 모달이 바로 열린다. 탭 시절의 `/dash/workers` 같은 pathname 링크(브라우저 히스토리, 북마크)가 깨지지 않도록, 서버는 그 경로에도 `index.html`을 주고 app.js가 로드되자마자 hash로 바꿔 넘긴다.

```js
(function () {
  var m = location.pathname.match(/^\/dash\/(workers|pipeline|drafts|weights|translation|audit|index|activity|cron)\/?$/);
  if (m) location.replace('/dash/#' + m[1]);
})();
```
{: data-filename="scripts/dashboard/app.js"}

마스트헤드는 블로그 스킨의 토큰과 `@font-face`를 그대로 가져왔고, 높이도 실측으로 블로그와 맞췄다. 테마는 블로그와 같은 `MTHEME` 쿠키(auto·light·dark)를 공유해서, 블로그를 다크 모드로 보던 사람이 대시보드로 넘어가도 같은 테마가 유지된다. 깜빡임을 막는 pre-paint 스크립트는 `index.html`의 head에 있다. 반대 방향으로, 블로그 설정 메뉴(`_includes/masthead.html`)에는 `display:none`으로 숨겨 둔 대시보드 항목이 있고, 인라인 스크립트가 `location.hostname === 'preview.math-jh.com'`일 때만 그것을 `flex`로 켠다.

## 상태 파일 쓰기 경로와 CSRF 게이트

대시보드는 대부분 읽기만 한다. 처음 생긴 쓰기는 KO-TYPOS 지적 목록(번역 검증기가 한글 원문의 오타를 짚은 항목)에 다는 "수정 완료" 체크였다. 이 상태를 `localStorage`에 두면 다른 기기에서 대시보드를 열었을 때 체크가 안 보이므로, `/api/kotypo`가 레포 밖 `~/.local/state/blog_dashboard_kotypo.json`에 저장한다.

```python
n = int(self.headers.get("Content-Length") or 0)
if not 0 <= n <= 100_000:
    raise ValueError
data = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
if not isinstance(data, dict) or len(data) > 1000 \
        or any(not isinstance(k, str) or len(k) > 400 for k in data):
    raise ValueError
...
clean = {k: 1 for k in data}
tmp = f"{KOTYPO_STATE}.tmp"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(clean, f, ensure_ascii=False)
os.replace(tmp, KOTYPO_STATE)
```
{: data-filename="scripts/dashboard/server.py"}

POST는 항목 하나를 더하지 않고, 클라이언트가 보낸 map 전체로 파일을 통째로 바꾼다. 부분 갱신 API 없이 클라이언트가 로컬 상태를 밀어 보내면 서버는 길이와 타입만 검사하고 임시 파일을 거쳐 받아 적는다.

그 뒤에 붙은 쓰기 경로들은 통째 교체를 쓰지 않는다. 판본 비교기의 검토 판정(`/api/review`)은 나중 세션이 실행 목록으로 읽는 지시서라서, 다른 탭에 열린 옛 map이 판정을 덮어쓰지 않도록 항목 단위로 병합한다. 후속 검증 메모(`/api/kotypo-note`)는 그것을 읽는 `ko_followup_worker`와 같은 flock 아래에서 키 단위로 병합하고, 의존성 링크 보류 원장도 분류기와 공유하는 flock 아래에서만 쓴다. 레포 안에 쓰는 경로는 하나다. 링크 판정 버튼이 `_data/link_relations.yml`에 판정을 쓰고, '링크 판정 커밋' 버튼이 그것을 `[Dash] Link Review [lastmod-skip]`로 커밋한다.

쓰기 POST는 전부 `_reject_write`를 먼저 통과해야 한다. 대시보드는 Cloudflare Access 뒤에 있고, Access 쿠키는 cross-site POST에도 그대로 실린다.

```python
def _reject_write(self):
    origin = self.headers.get("Origin") or ""
    host = self.headers.get("Host") or ""
    if not origin or not host:
        return "Origin 헤더 없음"
    o = urllib.parse.urlsplit("//" + urllib.parse.urlsplit(origin).netloc).hostname
    h = urllib.parse.urlsplit("//" + host).hostname
    if not o or not h or o.lower() != h.lower():
        return "Origin 불일치"
    if "application/json" not in (self.headers.get("Content-Type") or ""):
        return "Content-Type 이 application/json 이 아님"
    if self.headers.get("X-Dash-Action") != "1":
        return "X-Dash-Action 헤더 없음"
    return None
```
{: data-filename="scripts/dashboard/server.py"}

Origin과 Host를 그대로 비교하면 정상 요청까지 막힌다. nginx가 Host를 `$host:$server_port`로 넘기는 반면 브라우저 Origin은 기본 포트를 생략하므로, 포트를 뗀 hostname끼리만 비교한다. `X-Dash-Action` 커스텀 헤더와 JSON Content-Type을 요구하면 다른 사이트에서 날아온 요청은 프리플라이트를 먼저 거쳐야 하는데, 이 서버는 `OPTIONS`도 CORS 헤더도 내지 않으므로 거기서 막힌다. 같은 uid로 loopback을 때리는 로컬 프로세스는 이 게이트를 통과하지만, 그 위치에서는 이미 `crontab -e`가 가능하니 권한 상승이 아니라는 것이 주석의 판단이다.

## 자기 자신을 죽인 재기동 스크립트

`restart.sh`는 기존 서버 프로세스를 찾아 죽이고 새로 띄운다. 처음 패턴은 `pgrep -f "dashboard/server[.]py"`였는데, `-f`는 명령줄 전체를 부분 문자열로 매치하므로 그 경로를 인자로 언급만 한 프로세스까지 잡는다. `bash -c 'cd scripts/dashboard && ...'`처럼 대시보드 디렉토리를 지나가는 셸이 걸리면, restart.sh를 부른 세션 자체가 `kill` 대상이 되어 exit 144로 끊겼다. 자기 pid를 거르는 한 줄(`[ "$pid" = "$$" ] && continue`)은 restart.sh 자신만 봐줄 뿐 그것을 부른 부모 셸은 못 봐줬고, 같은 사고가 네 번 반복된 뒤에야 패턴을 명령줄 전체에 앵커했다.

```bash
PAT='^/usr/bin/python3 [^ ]*/dashboard/server\.py$'

for pid in $(pgrep -f "$PAT"); do
  kill "$pid" 2>/dev/null
done
sleep 1
setsid /usr/bin/python3 "$DIR/server.py" >>"$LOG" 2>&1 < /dev/null &
```
{: data-filename="scripts/dashboard/restart.sh"}

`^`와 `$`로 명령줄의 시작과 끝을 고정하면 "그 경로를 언급하는 프로세스"가 아니라 "그 경로로 시작한 python3 프로세스" 하나만 남는다. 서버를 절대경로 `/usr/bin/python3`로만 띄워야 하는 이유도 여기 있다. keeper cron도 같은 꼴로 띄우므로 어느 쪽이 띄운 서버든 이 패턴에 걸리고, 다른 꼴로 띄운 서버는 restart.sh가 찾지 못한다. 부분 문자열 매치가 편해 보여서 넘어갔던 대가로, 아무 상관 없는 세션이 넉 대 끊겼다. README의 "재기동은 `./restart.sh`로만"이라는 문장은 그 뒤에 적혔다.

## 파비콘 세 개, 프레임 하나

탭이 여러 개 열려 있으면 어느 것이 프로덕션이고 어느 것이 로컬 미리보기인지 제목만으로는 잘 안 보인다. [파비콘을 셋으로 갈랐다](https://github.com/math-jh/math-jh.github.io/commit/e955c7f1). 본사이트는 원래의 마크, preview는 네모 안에 망치, 이 대시보드는 네모 안에 계기판이다.

본사이트 쪽 분기는 빌드 환경으로 한다.

{% raw %}
```liquid
{% if jekyll.environment == "production" %}
<link rel="icon" type="image/svg+xml" href='data:image/svg+xml,%3Csvg …(기본 마크)%3E'>
{% else %}
<link rel="icon" type="image/svg+xml" href='data:image/svg+xml,%3Csvg …(망치)%3E'>
{% endif %}
```
{: data-filename="_includes/head.html"}
{% endraw %}

CI 빌드는 `JEKYLL_ENV=production`이라 기본 마크를 쓰고, 로컬 serve는 `else` 쪽으로 가서 망치가 붙는다. SVG는 파일이 아니라 data URI로 인라인이고, 색은 `site.data.brand`의 navy와 brass에서 Liquid로 받아 온다. 대시보드는 Jekyll 밖에 있으므로 `index.html`이 `favicon-gauge5.svg` 파일을 직접 건다.

셋이 형제로 보이려면 다른 것보다 같은 것이 많아야 한다. 네이비 타일, 그 위 브래스 네모, 그 네모의 좌표계(8/16/stroke 3)를 셋이 공유하고, 안에 들어가는 그림만 다르다. 대시보드 것은 후보를 여럿 그려 놓고 고른 결과이고, 확정 뒤에 탈락한 SVG 아홉 개를 지웠다. 아이콘 하나 고르는 데 열 개를 그린 셈인데, 16픽셀에서 바늘이 보이느냐 마느냐는 그려 보기 전에는 알 수 없다.
