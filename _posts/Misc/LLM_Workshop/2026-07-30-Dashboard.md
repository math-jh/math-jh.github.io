---

title: "블로그 운영 대시보드"
excerpt: "미발행 초안·워커 상태·번역 큐를 한 곳에 모으고, 이틀 만에 탭 화면을 개요 허브로 다시 짠 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/dashboard

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-30
weight: 35

---

관련 디렉토리: [`scripts/dashboard/`](https://github.com/math-jh/math-jh.github.io/tree/main/scripts/dashboard)
{: .notice--info}

이 블로그에는 이미 워커가 여럿 돈다. 번역 워커, 용어 추출 워커, 링크 감사, 색인 모니터. 각자 로그 파일과 state json을 하나씩 갖고 있고, 상태를 확인하려면 그 파일들을 하나씩 열어봐야 했다. 그 흩어진 상태를 한 화면에서 보고 싶다는 지시가 떨어졌고, `preview.math-jh.com/dash/`가 그 결과다.

## Jekyll을 거치지 않는 서버

대시보드는 이 블로그의 다른 페이지들과 다른 파이프라인을 탄다. `_config.yml`의 `exclude`에 `scripts`가 있어서 `scripts/dashboard/` 전체가 Jekyll 빌드 대상에서 빠지지만, git 추적은 그대로 된다. 빌드에서 빼는 이유는 단순하다. 대시보드의 데이터나 코드가 바뀔 때마다 사이트 전체가 재빌드되는 것을 원하지 않기 때문이다.

서빙은 `server.py`가 직접 한다. 표준 라이브러리 `ThreadingHTTPServer`만으로 짠 stdlib HTTP 서버가 `127.0.0.1:8089`에서 정적 파일과 `/api/*`를 함께 낸다. nginx는 `/dash/`를 이 포트로 곧장 `proxy_pass`한다.

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

Jekyll dev 서버(4001)로 가는 `location /`을 거치지 않고 곧장 8089로 꽂히므로, 대시보드가 죽어도 블로그 본문은 영향받지 않고 그 반대도 마찬가지다. nginx 설정 자체는 버전 관리 대상이 아니라서 `deploy/`에 조각 사본을 남겨두는데, 재현이 필요할 때 이 파일을 실제 설정에 복사해 넣으라는 뜻이다. crontab의 keeper 항목도 같은 이유로 사본만 레포에 있다.

```
*/5 * * * * curl -sf -o /dev/null --max-time 5 http://127.0.0.1:8089/api/summary || setsid /usr/bin/python3 .../server.py >>....log 2>&1 &
```
{: data-filename="scripts/dashboard/deploy/crontab.txt"}

5분마다 살아있는지 찔러보고, 응답이 없으면 다시 띄운다. 부팅 직후든 크래시든 같은 한 줄로 커버되고, sudo 없이 유저 crontab만으로 돈다.

## 개요 허브로 재설계

처음 만든 형태는 탭 네비게이션이 달린 평범한 대시보드였다. 워커/파이프라인/미발행/weight/번역/감사/색인/활동, 여덟 개 탭을 오가며 봐야 하는 구조였다. 이틀 뒤 claude.ai/design 프로젝트에서 만든 handoff 번들을 받아 리디자인이 들어갔는데, 방향은 탭을 없애고 개요 하나를 허브로 삼는 것이었다. `/dash/`에 들어가면 판정 한 줄("워커 8개 모두 정상" 또는 "워커 2개 점검 필요"), 최근 24시간 실행 히트맵, 지표 카드 6장, 지금 볼 것 알림, 파이프라인 단계, 섹션 색인이 한 화면에 있고, 각 섹션은 거기서 들어갔다가 "← 개요로"로 돌아온다.

판정 한 줄은 워커 상태만 본다. 로그가 정상 주기보다 늙은 워커가 하나라도 있으면 경고로 뒤집힌다.

```js
function verdict(d) {
  var bad = badWorkers(d), ws = (d.workers || []).length;
  if (bad.length) return {
    ok: false, head: '워커 ' + bad.length + '개 점검 필요',
    sub: bad.map(function (w) { return w.name; }).join(' · ') + ' 의 로그가 주기보다 늙었다.'
  };
  return {
    ok: true, head: '워커 ' + ws + '개 모두 정상',
    sub: '급한 일은 없다. 미발행 ' + num(d.stats.unpublished) + '편 · 재번역 대기 ' + num(d.stats.drift) + '편 · ...'
  };
}
```
{: data-filename="scripts/dashboard/app.js"}

미발행 초안이 몇 편 쌓여있든, 색인 조치 대상이 몇 건이든 판정에는 안 들어간다. 그런 숫자들은 "오늘 안 해도 무너지지 않는 일"이라서, 개요 아래쪽 지표 카드로만 조용히 보여준다. 급한 것과 급하지 않은 것을 한 줄에서부터 갈라놓은 셈이다.

라우팅은 hash다. `#workers` `#drafts` `#weights` `#translation` `#audit` `#index` `#activity` 식으로 프래그먼트만 바뀌고 서버는 항상 같은 `index.html`을 준다. 워커와 파이프라인은 이제 개요 안에서 소화되고 별도 라우트가 없다. 구 버전에 `/dash/workers`처럼 pathname으로 들어오던 링크(브라우저 히스토리, 북마크)가 깨지지 않도록, app.js가 로드되자마자 구 pathname을 감지해 hash로 바꿔치기한다.

```js
(function () {
  var m = location.pathname.match(/^\/dash\/(workers|pipeline|drafts|weights|translation|audit|index|activity)\/?$/);
  if (m) location.replace('/dash/#' + m[1]);
})();
```
{: data-filename="scripts/dashboard/app.js"}

마스트헤드는 블로그 스킨의 `_custom.scss` 토큰과 `@font-face`를 그대로 가져다 썼고, 높이도 실측으로 블로그와 맞췄다. 테마 선택은 블로그와 같은 `MTHEME` 쿠키를 공유해서, 블로그를 다크모드로 보던 사람이 대시보드로 넘어가도 같은 테마가 유지된다. 반대로 블로그의 설정 메뉴에는 `preview.math-jh.com`에서 볼 때만 보이는 대시보드 링크가 추가됐다.

```html
<li class="settings-item" id="dash-link" style="display:none" onclick="location.href='/dash/'">
  <span style="color:#bbb">Dashboard</span>
</li>
<script>
if (location.hostname === 'preview.math-jh.com') {
  document.getElementById('dash-link').style.display = 'flex';
}
</script>
```
{: data-filename="_includes/masthead.html"}

## 서버가 유일하게 쓰는 파일

README는 대시보드를 "읽기 전용"이라고 소개하다가, 나중에 그 문장을 "레포에는 아무것도 쓰지 않는다"로 고쳐야 했다. KO-TYPOS 지적 목록(번역 검증기가 한글 원문의 오타를 지적한 항목들)에 "수정 완료" 체크를 다는 기능 때문이다. 처음엔 이 체크 상태를 `localStorage`에 두었는데, 그러면 다른 기기에서 대시보드를 열었을 때 체크가 안 보인다. 그래서 `/api/kotypo` 엔드포인트를 만들어 `~/.local/state/blog_dashboard_kotypo.json`에 저장하는 쪽으로 옮겼다. 레포 밖이니 git 추적 대상은 아니고, 이게 서버의 유일한 쓰기 경로다.

```python
if path == "/api/kotypo":
    n = int(self.headers.get("Content-Length") or 0)
    if not 0 <= n <= 100_000:
        raise ValueError
    data = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
    if not isinstance(data, dict) or len(data) > 1000 \
            or any(not isinstance(k, str) or len(k) > 400 for k in data):
        raise ValueError
    clean = {k: 1 for k in data}
    tmp = f"{KOTYPO_STATE}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False)
    os.replace(tmp, KOTYPO_STATE)
```
{: data-filename="scripts/dashboard/server.py"}

POST는 항목 하나를 추가하는 대신 클라이언트가 보낸 map 전체로 통째로 교체한다. 부분 갱신 API를 만들 것도 없이, 클라이언트가 로컬 상태를 그대로 밀어붙이면 서버는 검증만 하고 그대로 받아 적는다. 길이 제한과 타입 검사가 붙어있는 것은 이 엔드포인트가 이 서버에서 외부 입력을 받아 디스크에 쓰는 유일한 자리이기 때문이다.

## 자기 자신을 죽인 재기동 스크립트

`restart.sh`는 원래 `pgrep -f "dashboard/server[.]py"`로 기존 프로세스를 찾아 죽이고 새로 띄우는 단순한 스크립트였다. `-f`는 전체 명령줄을 부분 문자열로 매치하는데, 문제는 그 경로 문자열을 인자로 "언급만" 한 다른 프로세스까지 걸린다는 것이다. `bash -c 'cd scripts/dashboard && ...'`처럼 대시보드 디렉토리를 지나가는 셸 명령이 우연히 이 패턴에 걸리면, restart.sh를 부른 세션 자체가 `kill` 대상이 되어 exit 144로 끊긴다. 처음엔 자기 자신의 pid만 걸러내는 한 줄(`[ "$pid" = "$$" ] && continue`)로 막아뒀는데, 그건 restart.sh 자신의 프로세스만 봐줄 뿐 그걸 호출한 부모 셸은 못 봐준다. 같은 사고가 네 번 반복된 뒤에야 패턴을 명령줄 전체에 앵커시켰다.

```bash
PAT='^/usr/bin/python3 [^ ]*/dashboard/server\.py$'
for pid in $(pgrep -f "$PAT"); do
  kill "$pid" 2>/dev/null
done
```
{: data-filename="scripts/dashboard/restart.sh"}

`^`와 `$`로 명령줄 시작과 끝을 고정하면 "그 경로를 언급하는 프로세스"가 아니라 "그 경로로 시작한 python3 프로세스" 하나만 남는다. 서버를 절대경로 `/usr/bin/python3`로만 띄워야 하는 이유도 여기 있다. keeper cron과 restart.sh가 같은 패턴을 공유하는데, 상대경로로 띄우면 패턴이 어긋나 keeper가 서버를 중복으로 띄우거나 못 찾는다. 부분 문자열 매치가 편해 보여서 넘어갔던 자리가, 아무 상관 없는 세션을 넉 대 끊어먹고 나서야 제대로 고쳐졌다.

## 결과

`/dash/`를 열면 이제 워커 여덟 개의 상태와 미발행 초안 수, 재번역 대기, 색인 조치 대상이 판정 한 줄과 카드 몇 장으로 요약된다. 로그 파일을 하나씩 열어보던 습관은 필요할 때만 쓰는 것으로 바뀌었다. 재기동은 `restart.sh` 하나로만 하라는 README의 문장은, 그 규칙을 어겼을 때 무엇이 끊어지는지를 이미 겪은 뒤에 적힌 것이다.
