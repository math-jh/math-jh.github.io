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
last_modified_at: 2026-08-15
weight: 35

---

관련 디렉토리: [`scripts/dashboard/`](https://github.com/math-jh/math-jh.github.io/tree/main/scripts/dashboard)
{: .notice--info}

이 블로그에는 이미 워커가 여럿 돈다. 번역 워커, 용어 추출 워커, 링크 감사, 색인 모니터. 각자 로그 파일과 state json을 하나씩 갖고 있고, 상태를 확인하려면 그 파일들을 하나씩 열어봐야 했다. 사용자는 그 흩어진 상태를 한 화면에서 보고 싶어 했고, `preview.math-jh.com/dash/`가 그 결과다.

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

## 사후: 침묵하는 워커

판정 한 줄의 근거는 워커마다 정해둔 `interval`과 로그 파일의 mtime뿐이다. `용어 추출` 워커는 `interval=1800`(cron `:00 / :30`)이라, 로그가 75분(2.5배) 넘게 안 갱신되면 대시보드가 그 줄을 빨간불로 뒤집는다. 그런데 [찾아보기 자동 갱신](/ko/llm_workshop/term_extraction)의 수확기인 `term_extract_worker.py`에는 이 로그를 안 남기고 조용히 끝나는 경로가 둘 있었다. `select_post`가 아무 글도 고르지 못하고 홀수 시각이라 감사도 안 도는 틱은 `return 0`으로 곧장 끝났고, 감사가 실제로 `terms.yml`을 고친 성공 경로는 텔레그램으로만 알리고 로그 파일에는 아무것도 적지 않았다. 워커는 정상적으로 돌고 있는데, 대시보드가 보는 파일에는 그게 안 보이는 상태였다.

```python
else:
    # 할 일이 없어도 한 줄은 남긴다 — 대시보드가 이 로그의 mtime 으로
    # 워커 생존을 판정하므로(2.5×30분), 조용히 끝내면 정상 동작 중에
    # '안 돎'으로 표시된다.
    log("대상 없음 (감사는 짝수 시각)")
return 0
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

`audit_letter` 쪽도 같은 이유로 한 줄이 붙었다. 바꾼 게 없는 틱은 원래도 `log(f"감사 {letter}: 추가 없음 ...")`을 남기고 있었는데, 정작 바꾼 게 있어서 `terms.yml`을 실제로 쓰는 틱에는 그 대응 로그가 없었다. `tmp.replace(TERMS_PATH)` 다음에 같은 형식의 `log(f"감사 {letter}: " + " · ".join(changes) + f" (다음 {nxt})")`를 더해, 일한 틱과 안 한 틱이 로그 위에서 똑같이 보이게 맞췄다. [커밋](https://github.com/math-jh/math-jh.github.io/commit/521857c529c0d673b20c5113705c2fb98f8ff248)은 diff로 보면 여덟 줄짜리다. 침묵도 결과 중 하나라고 여기고 있었는데, 판정 한 줄을 보는 쪽에서는 그 침묵과 죽음을 구분할 방법이 없었던 셈이다.

## crontab을 안 건드리는 정지 버튼

대시보드에 `cron` 섹션이 새로 생겼다. 번역 워커·용어 추출·pagefind 재색인 같은 크론 잡을 목록으로 보여주고, 잡마다 정지·재개 버튼을 단다. 버튼을 눌러도 서버는 crontab 파일에 손대지 않는다. crontab은 director·sync_slots·safety_net이 락 없이 통째로 다시 쓰는 파일이라, 웹 핸들러가 거기 끼어들면 lost update가 난다는 근거가 주석으로 남아 있다.

```python
# 정지/재개는 crontab 을 고치지 않는다. crontab 에 박힌 cron-gate 가 상태파일
# 하나를 보고 뒤 명령을 돌릴지 말지 정하고, 이 서버는 그 CLI 만 호출한다.
# crontab 은 director/sync_slots/safety_net 이 락 없이 rewrite 하므로 웹에서
# 건드리면 lost update 가 난다 (2026-07-18 번역워커 라인 소실 사고).
CRON_GATE = os.path.expanduser("~/.local/bin/cron-gate")
CRON_JOBS = [
    dict(id="blog-translation", name="번역 워커", worker="translation"),
    dict(id="blog-devbot",      name="개발 노트 봇", worker="blogdev"),
    # ... 나머지 아홉 잡
    dict(id="timer:blog-autopush", name="autopush", worker=None),
]
CRON_IDS = {j["id"] for j in CRON_JOBS}
```
{: data-filename="scripts/dashboard/server.py"}

정지 상태는 크론 라인 앞에 이미 붙어 있는 `cron-gate` CLI가 관리하는 파일 하나에 쓴다. 서버는 그 CLI를 호출만 하고, 상태 파일을 직접 읽거나 쓰지 않는다. 어떤 잡을 건드릴 수 있는지는 `CRON_JOBS` 목록의 id가 화이트리스트로 정하고, POST 바디의 `id`가 이 집합에 없으면 400으로 끝난다. 임의 문자열을 받아 파일 경로를 조립하는 대신, 허용된 id 몇 개로 쓰기 범위를 미리 좁혀둔 셈이다.

정지·재개는 POST라 CSRF도 신경 써야 했다. 대시보드는 Cloudflare Access 뒤에 있고, Access 쿠키는 cross-site POST에도 그대로 실린다.

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
    if self.headers.get("X-Dash-Action") != "1":
        return "X-Dash-Action 헤더 없음"
    return None
```
{: data-filename="scripts/dashboard/server.py"}

Origin과 Host를 그대로 비교하면 정상 요청까지 막힌다. nginx가 Host를 `$host:$server_port`로 넘기는 반면 브라우저 Origin은 기본 포트를 생략하기 때문에, 포트를 뺀 hostname끼리만 비교한다. `X-Dash-Action` 커스텀 헤더를 필수로 둔 것도 같은 계산에서 나왔다. 커스텀 헤더가 붙은 요청은 브라우저가 프리플라이트를 먼저 보내는데, 다른 사이트에서 날아온 cross-origin 요청은 그 프리플라이트를 통과하지 못한다. 반대로 같은 uid로 loopback을 때리는 로컬 프로세스는 이 가드를 그냥 통과한다. 그 지점에서는 이미 `crontab -e`가 가능하니 권한 상승이 아니라는 게 주석의 판단이다.

## 정지 워커는 stale이 아니다

워커 판정 로직도 같은 커밋에서 손이 갔다. 정지된 워커는 로그가 정상 주기보다 늙는 게 당연한데, 판정 한 줄은 그 늙음만 보고 경고로 뒤집었었다.

```js
function badWorkers(d) {
  return (d.workers || []).filter(function (w) {
    if (w.paused) return false;
    return w.status === 'stale' || w.status === 'missing' || w.err;
  });
}
```
{: data-filename="scripts/dashboard/app.js"}

`paused` 플래그를 워커 응답에 얹고, 판정에서 그 워커를 먼저 걸러냈다. 대신 개요 한 줄 옆에 "일시정지 N건은 따로 세지 않았다"는 문구를 붙여서, 정지 사실 자체는 숨기지 않는다. 의도된 정지와 고장을 같은 빨간불로 뭉뚱그리지 않게 된 것이다.

같은 커밋에는 GSC 색인 추천 로직도 손이 갔다. 대시보드가 자체적으로 계산하던 추천 URL 순위를 `index-monitor`의 `index_ranking` 모듈로 옮겨 그대로 import해 쓰게 됐다. 규칙을 두 곳에 복제해두면 index-monitor 쪽 규칙이 바뀔 때 대시보드만 옛 기준으로 남는다는 게 이유다. 오늘 03:00 배치가 이미 뽑아 둔 추천이 있으면 그걸 그대로 쓰고, 없으면 같은 모듈로 지금 다시 계산한다. 배치는 GSC 실측을 거치고 뽑히면서 쿨다운까지 걸어두므로, 배치를 무시하고 매번 새로 계산하면 다른 순번이 나오기 때문이다. 추천 목록의 URL을 누르면 이동 대신 완결된 링크가 클립보드로 복사되도록도 바뀌었다. 그대로 GSC 검색창에 붙여넣고 색인 요청을 누르는 동선이다. [커밋](https://github.com/math-jh/math-jh.github.io/commit/6256feea51d03b4129b37aaaa4071aee4f246068).

## 오류 판정이 보는 범위

워커 카드의 빨간불은 로그 꼬리에서 오류 문구를 찾아 켰다. 판정 범위가 "마지막 10줄"이었으니, 사흘 전에 한 번 죽고 그 뒤로 멀쩡히 도는 워커도 그 트레이스백이 꼬리에 남아 있는 한 계속 빨간불이었다. 불이 꺼지려면 로그가 열 줄 넘게 더 쌓이기를 기다려야 한다. [이 커밋](https://github.com/math-jh/math-jh.github.io/commit/3fc8a0e6)이 범위를 마지막 실행분으로 좁혔다.

```python
_ERR_RE = re.compile(r"traceback|\bexception\b|\bfail(ed|ure)\b|\berrors?\s*[:=]\s*[1-9]"
                     r"|\berror\b(?!s?\s*[:=]\s*0)", re.I)


def _last_run_lines(path, interval, n=10):
    ...
    gap = max(300, interval * 0.25)
    start = stamps[0][0]
    for (i, ts), (_, prev) in zip(stamps[1:], stamps):
        if ts - prev > gap:
            start = i
    return lines[start:]
```
{: data-filename="scripts/dashboard/server.py"}

실행 경계는 타임스탬프 간격으로 잡는다. 간격이 `max(300초, 크론주기/4)`를 넘으면 다른 실행이다. 이 값은 양쪽에서 눌린다. 한 실행 안의 줄 간격보다는 커야 하고(GSC 전체 스윕은 10분 넘게 벌어진다), 실행 사이 간격보다는 작아야 한다. 타임스탬프가 없는 줄은 직전 줄의 실행에 붙이는데, 그래야 마지막 줄 뒤에 붙은 크래시 트레이스백이 그 실행에 잡힌다.

정규식도 같이 좁혔다. `errors=0`처럼 "오류 없음"을 보고하는 정상 요약줄이 `error`라는 문자열을 들고 있다는 이유로 불을 켜고 있었다. 뒤에 `0`이 오는 경우를 부정 전방탐색으로 뺐다.

이 판정은 워커가 타임스탬프를 찍는다는 약속 위에 서 있다. 안 찍으면 폴백으로 조용히 "마지막 10줄"로 돌아가므로, 같은 커밋에서 안 찍던 두 곳을 맞췄다. `blogdev-bot/lib.sh`의 `log()`는 시각만 찍고 날짜가 없어 하루가 넘어가면 경계 계산이 어긋났고, `audit/check_links.py`는 아예 접두사가 없었다. 후자에는 시작 줄을 새로 넣었다. 시작 줄이 있어야 도중에 죽어 남은 트레이스백이 그 실행에 붙는다.

## 파비콘 세 개, 프레임 하나

탭이 여러 개 열려 있으면 어느 것이 프로덕션이고 어느 것이 로컬 미리보기인지 제목만으로는 잘 안 보인다. [파비콘을 셋으로 갈랐다](https://github.com/math-jh/math-jh.github.io/commit/e955c7f1). 본사이트는 원래의 마크, preview는 네모 안에 망치, 그리고 이 대시보드는 네모 안에 계기판이다.

본사이트 쪽 분기는 빌드 환경으로 한다.

{% raw %}
```liquid
{% if jekyll.environment == "production" %}
{% else %}
<link rel="icon" type="image/svg+xml" href='data:image/svg+xml,%3Csvg …%3E'>
{% endif %}
```
{: data-filename="_includes/head.html"}
{% endraw %}

CI 빌드는 `JEKYLL_ENV=production`이라 기본 마크를 그대로 쓰고, 로컬 serve는 그 분기에 안 걸려 망치가 붙는다. SVG는 파일이 아니라 data URI로 인라인이고, 색은 `site.data.brand`의 navy와 brass에서 Liquid로 꽂는다. 브랜드 색이 한 파일에 모여 있으니 파비콘도 거기서 받아 쓴다.

셋이 형제로 보이려면 다른 것보다 같은 것이 많아야 한다. 네이비 타일, 그 위 브래스 네모, 그리고 그 네모의 좌표계(8/16/stroke 3)를 셋이 공유하고, 안에 들어가는 그림만 다르다. 대시보드 것은 후보를 여럿 그려놓고 고른 결과이고, 확정 뒤에 탈락한 SVG 아홉 개를 지웠다. 아이콘 하나 고르는 데 열 개를 그린 셈인데, 16픽셀에서 바늘이 보이느냐 마느냐는 그려보기 전에는 알 수 없다.
