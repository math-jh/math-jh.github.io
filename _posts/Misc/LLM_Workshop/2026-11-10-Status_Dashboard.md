---

title: "상태 대시보드 개편"
excerpt: "6월에 만든 status.math-jh.com을 service-map에 맞춰 정리하고, 판정·24시간 알림 줄·계기 6칸·카드 6장의 구조로 다시 짠 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/status_dashboard

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-10
weight: 73
group: pi

---

관련 파일(Pi 위의 비공개 프로젝트, git 없음): `~/Projects/status_dashboard/status_dashboard.py`, `~/Projects/status_dashboard/data.js`, `~/Projects/status_dashboard/sections.jsx`, `~/Projects/status_dashboard/dashboard.css`. 저장소 밖이라 코드는 발췌로 싣고, 개편 전 코드는 작업 때 떠 둔 사본 `~/.local/state/status-dashboard-pre-20261110/`에서 옮긴다.
{: .notice--info}

`status.math-jh.com`은 6월에 [로컬 서비스를 서브도메인으로 열 때](/ko/llm_workshop/custom_domain) 만든 Pi 상태 화면이다. 6월 초의 화면은 시스템 상태 한 줄 아래에 시스템, LLM 사용량, 서비스, 블로그·콘텐츠 카드가 놓인 모양이었다.

![6월 초의 status.math-jh.com. 시스템 계기, Claude·Kimi·MiMo 사용량, Jekyll·Agent Display·Hermes Web UI·Homebridge·연구 크론의 서비스 카드, 블로그 크론과 검색 색인 카드가 놓여 있다](/assets/images/Misc/LLM_Workshop/Status_Dashboard-june.png)

그 뒤 Pi에서 도는 것은 많이 바뀌었는데 화면의 틀은 그대로였다. 사용자의 첫 말은 짧았다.

> 지금 이 대시보드가 좀 낡았거든, service-map 참고해서 수정할 거 있음 수정 좀 해 줘.

## service-map과 어긋난 카드

먼저 화면이 읽는 것을 `~/Projects/infra/service-map.yml`과 대조했다. LLM 사용량 카드는 Codex를 계정 하나로만 보였다. HUD의 쿼터 수집기는 두 계정(`codex1`·`codex2`)을 따로 기록하는데, 대시보드는 그 전의 `codex_quota.json` 하나를 읽고 있었다. 그래서 그 시점에 쓰던 계정이 7일 한도를 다 쓰면 다른 계정에 몫이 남아 있어도 빨간 경고가 떴다. Antigravity 타일은 아예 없었다. 지금은 HUD와 같은 네 타일(Claude·Codex 1·Codex 2·Antigravity)을 읽는다.

```js
function poolPartner(m) {
  if (!m.pool) return null;
  return S.llm.models.find((o) => o !== m && o.pool === m.pool && o.enabled !== false && rawSeverity(o) === "ok") || null;
}
function modelSeverity(m) {
  const sev = rawSeverity(m);
  return sev === "bad" && poolPartner(m) ? "warn" : sev;
}
```
{: data-filename="~/Projects/status_dashboard/data.js · 일부 발췌, 주석 생략"}

서버는 Codex 두 계정에 같은 `pool: "codex"`를 붙여 내려 준다. 한 계정이 바닥나 `bad`가 되어도 같은 묶음에 아직 `ok`인 계정이 있으면 `poolPartner`가 그 계정을 찾고, 판정은 `warn`(주의)으로 내려간다. 계정은 multi-auth가 알아서 갈아 쓰므로, 한쪽이 바닥난 것은 손쓸 일이 아니라는 것이 사용자의 판단이었다. 조회가 실패했을 때도 예전 화면은 마지막 숫자를 경고 없이 남겨 두었다. 지금은 실패가 10분 넘게 이어지면 "조회 실패", 30분 넘게 값이 바뀌지 않으면 "갱신 멈춤"을 띄운다. 10분은 HUD 타일이 일시적인 429를 참아 주는 시간과 같다.

서비스 카드에서는 세로 디스플레이를 아직 e-ink로, 쿼터 수집을 15분 크론으로 설명하고 있어서 지금 구조(키오스크와 1분 타이머)에 맞게 고쳤다. Jekyll 칸에는 감시 프로세스 `jekyll-watchdog`가 살아 있는지를 더했다. 이것이 꺼지면 사이트는 멀쩡해도 장애 알림이 오지 않기 때문이다. 비어 있던 칸에는 Nextcloud를 대체한 Syncthing을 넣었다. 비밀 키는 읽지 않고, 15분마다 도는 감시 크론의 상태 파일만 본다. 11월 6일에 연구 파이프라인을 내리면서 남은 연구 크론 카드 코드도 이때 지웠다.

정리하다가 정적 파일 서빙의 구멍이 둘 나왔다.

```python
if not full.startswith(WEBROOT) or not os.path.isfile(full):
    return self._send(404, b"not found", "text/plain")
if full.endswith(".py"):  # server source now lives under WEBROOT; never serve it
    return self._send(404, b"not found", "text/plain")
```
{: data-filename="status_dashboard.py · 개편 전 사본, 일부 발췌"}

서버 소스가 웹 루트 안에 있어서 `.py`는 막고 있었지만, 파이썬이 옆에 만드는 `__pycache__/*.pyc`는 그대로 200으로 나갔다. 또 `startswith(WEBROOT)`는 접두사만 보므로 `…/status_dashboardX` 같은 형제 디렉터리의 경로도 통과한다. 지금은 `WEBROOT + os.sep`로 비교하고, `.pyc`와 `__pycache__` 아래 경로도 404로 돌려보낸다. 사이트가 Cloudflare Access 뒤에 있어서 밖에서 바로 닿는 구멍은 아니었다.

## 블로그 대시보드의 구조, 다른 시각 언어

이어서 사용자는 디자인도 다시 봐 달라고 했고, 돌고 있는 것 중 알림이나 USB 과전류 감시처럼 화면에 올릴 만한 것이 있는지 물었다. 위의 정리까지 마친 화면은 이랬다. 시스템 상태 한 줄 아래에 시스템·LLM 사용량·서비스 카드가 두 칸으로 놓이고, 알림이나 전원·저장소는 보이지 않는다.

![개편 직전 코드로 띄운 상태 대시보드. 시스템 상태 한 줄 아래에 시스템 계기, LLM 사용량, 서비스 카드가 놓여 있다](/assets/images/Misc/LLM_Workshop/Status_Dashboard-before.png)

이 화면은 작업 때 떠 둔 개편 직전 사본(`~/.local/state/status-dashboard-pre-redesign-20261111/`)을 다른 포트에 잠깐 띄워 찍은 것이라, 코드와 스타일은 그때 것이고 숫자는 찍은 날의 값이다.

참고할 곳은 같은 날 손본 [블로그 대시보드](/ko/llm_workshop/dashboard_revamp)였지만, 선은 분명했다.

> 블로그 대시보드 디자인 참고하되, 거기서 사용하는 것들을 그대로 쓸 필요는 없고 디자인 색상도 사용할 필요 없어. 디자인 언어도 따라갈 필요는 없고 분명 구분되게 하되, 구조나 이런것만 참고하란 말이야.

가져온 구조는 판정 한 줄, 24시간 기록, 폭 전체의 띠, 같은 크기의 카드 6장, 카드를 누르면 들어가는 상세 섹션과 `← 개요로`다. 블로그의 실행 기록 자리에는 알림 발신 기록으로 만든 24시간 줄이, 수정량 잔디 자리에는 CPU·메모리·온도·네트워크·전원(5V 입력 전압)·디스크의 계기 6칸이 들어갔다. 카드는 LLM 쿼터, 서비스, 알림, 전원·USB, 저장소·백업, 감시기(pi-health-monitor)다. 시각 언어는 블로그와 겹치지 않게 했다. 블로그가 남색 상단 바, 크림색 바탕, 놋쇠색, 직각 모서리라면 이쪽은 어두운 그라파이트와 둥근 모서리이고, 초록·노랑·빨강은 상태에만 쓴다. 글꼴은 IBM Plex Sans KR과 숫자용 JetBrains Mono다. 예전 화면은 한글이 시스템 글꼴로 대신 그려지고 있었다.

![판정과 최근 24시간 알림 줄, 계기 6칸, LLM 쿼터·서비스·알림·전원 USB·저장소 백업·감시기 카드 6장으로 짠 지금의 상태 대시보드](/assets/images/Misc/LLM_Workshop/Status_Dashboard-after.png)

반대로 올리지 않은 것도 있다. SSH 보안 신호는 접속 IP라 웹 페이지에 둘 정보가 아니고, 블로그 워커와 크론은 블로그 대시보드의 몫이라 링크만 둔다. 크론 정지·재개 버튼은 쓰기 경로를 다시 열어야 해서 이 화면은 읽기 전용으로 남았다.

시안은 claude.ai의 디자인 캔버스에서 몇 번 오갔다. 첫 시안을 보고 사용자는 번잡하다고 했다.

> 약간 번잡해보이고, 타일로 두는 건 좋은데 그... 예를 들어 서비스 칸은 저 태그들이 다 따로 있는거 약간 화난다. 17/17 active만 있고, 실제 뭐 있는지는 자세히 눌러 들어가서 보면 될 것 같아. 그리고 저 쓸데없는 설명들 (예를 들어 "쓸 수 있는 것 중 가장 찼다" 등)은 없애고 좀 더 깔끔하게 해.

설명 문장을 다 걷어 내자 이번에는 너무 휑하다는 말이 돌아왔다. 그래서 카드마다 큰 숫자 아래에 문장이 아니라 수치 줄을 두는 것으로 자리를 잡았다. 서비스 카드는 `17/17 active` 아래에 주력 서비스 넷의 상태만 적고, 나머지 유닛 열세 개는 상세 섹션의 표에 있다. 전원·USB 카드는 포트 그림을 빼고 서비스 카드처럼 글 세 줄(스로틀, USB 3.0 A·B, USB 2.0 A·B)이 되었다. 입력 전압은 위의 계기 칸이 이미 보여 주므로 카드에서는 뺐다. 포트 이름은 사용자가 정했다.

> 파란 포트, 검은 포트는 3.0 A / 3.0 B, 2.0 A  / 2.0 B 이 정도로 해 줘.

과전류 횟수는 커널이 포트마다 세는 sysfs 값(`over_current_count`)을 직접 읽는다. USB 컨트롤러 둘(`1f00200000.usb`, `1f00300000.usb`)이 각각 A와 B이고, 컨트롤러마다 USB 3 버스와 USB 2 버스가 있다. 파란 3.0 포트는 두 버스에 다 걸려 있어서 두 카운터의 합을, 검은 2.0 포트는 USB 2 버스의 카운터 하나를 보인다. 이번 부팅 이후의 누적이다. 이 카드를 만들려고 기록을 보다가, 그날 20:12에 카운터 여섯 개가 같은 순간 45~56회씩 올랐는데 예전 화면에는 아무것도 보이지 않았다는 것이 확인됐다.

## 알림 등급으로 칠한 24시간 줄

알림 카드의 첫 시안은 오늘 온 알림을 나열했다. 사용자는 그걸로는 의미가 없다고 했다.

> 알림도 저 상태로는 의미가 없어. 저렇게 하기보다, 인프라에서 몇개고 블로그에서 몇개고, 이런걸 하는게 낫지.

그때 알림 그룹은 `infra`와 `blog` 둘뿐이었고, 지난 열흘의 `infra` 169통 중 77통은 LLM 상태 감시가 보낸 것이었다. 사용자는 LLM을 인프라에서 떼자고 했고, 쿼터 알림은 인프라에 두되 LLM 장애와는 나누고 싶다고 했다. 나는 쿼터를 따로 한 그룹으로 두자고 했다. 장애는 기다리는 것 말고 할 일이 없지만 쿼터는 작업 배치를 바꾸라는 신호이고, 인프라에 넣으면 "인프라 알림이 오면 Pi를 봐야 한다"는 뜻이 흐려진다. 사용자는 이 안과, 폰의 묶음은 `infra`·`llm`·`quota`·`blog` 넷으로 두고 하위 분류(`infra/hw`, `blog/worker` 등)는 발신 기록에만 남기는 두 단계 안을 받아들였다. 이 그룹 정리는 `notify` 자체를 고치는 일이라 사용자의 지시로 서브에이전트에게 따로 맡겼고, 대시보드는 그 형식만 먼저 정해 받아서 구현했다.

```python
def classify(group, title):
    top, _, sub = (group or "").strip().partition("/")
    if top in ("llm", "quota"):
        return top, ""
    if top == "blog":
        return "blog", sub
    if top == "infra" and sub:
        return "infra", sub
    if _LLM_TITLE.search(title):
        return "llm", ""
    if re.search(r"quota|Codex pool", title, re.I):
        return "quota", ""
    if re.search(r"재부팅|throttling|과전류|온도|OOM", title):
        return "infra", "hw"
    # ... 저장소·보안 제목, 나머지는 infra/service
```
{: data-filename="~/Projects/status_dashboard/status_dashboard.py · 일부 생략"}

`~/.local/state/notify/sent.log`는 발신 한 번에 한 줄(시각·경로·그룹·등급·rc·제목)이다. `classify`는 그룹 칸을 `/`에서 잘라, 새 형식이면 그 값을 그대로 쓴다. 단독 `infra`나 `blog`로 적힌 예전 기록은 하위 분류가 없으므로 제목에서 짐작한다. `_LLM_TITLE`은 `status site unreachable`이나 `Claude: ` 같은 제공사 이름 머리를 찾는 패턴이다. 그래서 notify 작업이 언제 끝나든 대시보드는 두 형식을 함께 센다. 이 파일에는 10월 31일 무렵의 NUL 바이트 403개가 섞여 있어서, `sent_rows`는 파일을 바이너리로 읽고 NUL을 지운 뒤에 줄을 나눈다.

시안의 24시간 줄은 눈금을 경보·복구·정보 세 색으로 칠했는데, 사용자가 그 차이가 애매하다고 했다.

> 최근 24시간 같은 경우에는, 경보,복구,정보 이거 차이는 뭐야? 좀 애매한거같은데. 확인해줘.

확인해 보니 그 셋은 기록에 있는 값이 아니라 내가 제목만 보고 나눈 것이었다. "Pi 재부팅 감지"는 실제로 보통 등급으로 나갔는데 빨간 경보로 칠했고, HUD에만 가는 LLM 사고의 중간 업데이트는 정보와 경보로 갈려 있었다. 기록에 실제로 있는 것은 notify의 등급(`timeSensitive`·`active`·`passive`)이고, 사용자는 그 등급대로 칠하라고 했다. 지금 줄은 하드웨어·전원, 저장소·백업, 서비스, LLM, 쿼터, 블로그 여섯 개이고, 급함은 빨강, 보통은 파랑, 조용은 회색이며, 폰 발송에 실패한 알림은 속이 빈 눈금이다. 새 필드를 만들지 않고 이미 기록되는 값만 쓰므로, 발신처가 제목 관례를 지키지 않아도 색이 어긋나지 않는다.

같은 기록에서 다른 문제도 드러났다. 그날 폰 알림 82통 중 51통이 20시대에 발송에 실패했고, 실패한 발송이 1분마다 같은 제목으로 다시 나가 "status site unreachable"만 31통이 쌓였다. 세 제공사의 상태 사이트가 같은 분에 모두 불통이었으니 LLM 장애가 아니라 Pi 쪽 네트워크가 끊긴 것이었다. 이것도 notify 작업으로 넘어가서, 지금은 세 곳이 동시에 불통이면 "Pi 네트워크 단절 의심" 한 통이 `infra/network`로 간다. 알림 카드는 그룹별 오늘 건수와 실패 수를, 알림 섹션은 시간대별 막대와 "많이 온 제목" 표를 보인다. 이 표가 이런 폭주를 찾는 자리다. 오른쪽의 최근 발송 표에는 알림마다 경로(폰·HUD), 그룹과 하위 분류, 등급, 발송 결과가 붙는다.

![폰·발송 실패·HUD·하루 요약 건수, 시간별 폰 알림 막대, 많이 온 제목과 최근 발송 표가 있는 알림 섹션](/assets/images/Misc/LLM_Workshop/Status_Dashboard-notify.png)

## 1초 폴링과 10초 폴링

화면은 6월과 같이 빌드 단계 없이 React UMD와 `@babel/standalone`이 jsx를 브라우저에서 변환한다. 바뀐 것은 데이터를 받는 방식이다. 예전에는 `/api/status` 하나를 1초마다 받았는데, 알림 기록과 전원·저장소·감시기 상태까지 1초마다 읽을 이유는 없다.

```js
setInterval(pollStatus, 1000);
setInterval(pollDetail, 10000);
```
{: data-filename="~/Projects/status_dashboard/data.js · 일부 발췌"}

`/api/status`는 계기와 LLM, 서비스만 담아 5KB 안팎으로 줄였고, 무거운 쪽은 `/api/detail`로 나뉘어 10초마다 온다. `sent.log`는 mtime과 크기가 그대로면 지난번에 읽은 줄을 다시 쓴다. 판정(정상·주의·경보)은 화면이 읽기만 하도록 `data.js`의 `Store`가 전부 계산한다. 섹션은 `#llm`·`#notify` 같은 hash 경로로 들어간다.

이 대시보드의 API는 pi-health-monitor도 읽는다. 응답 여부로 대시보드가 살아 있는지 보기 때문에, 응답 형식은 그대로 두고 감시기를 알림 없이 시험 실행(dry-run)해 문제가 0건인 것을 확인했다. 새 카드가 읽는 파일들(감시기 상태, 백업 상태, 알림 기록)은 service-map에 이 대시보드를 소비자로 적었다. 키 이름 하나가 바뀌면 카드가 에러 없이 늘 정상으로 보이는 종류의 결합이라서다.

## 계기 두 칸이 카드 한 장인 격자

마지막으로 사용자가 짚은 것은 좁은 화면이었다. 계기 6칸이 어떤 폭에서는 다섯 칸과 한 칸으로 갈렸다.

> 6열로 뜨는 저 상태 카드가, 좁은 화면에선 5개 / 1개 이렇게 분리되어 보이는데, 반응형에서 6열인걸로 그대로 or 3열 두 줄 이런 식으로 되게 해 줘. 그 사이 이상한거 없게.

처음에는 계기만 6열 → 3열 두 줄 → 2열 세 줄로 접히게 고쳤다. 사용자가 원한 것은 다른 것이었다.

> 저 카드 하나에 작은 카드가 2개씩 들어가게 해 달란 말이야. 예를 들어서 반응형으로 아래 큰 카드가 2열이 되면, 저건 4개 되게 하면 될거같아

```scss
.rack { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: var(--gg); }
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--gg); }
@media (max-width: 1199px) {
  .rack { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 760px) {
  :root { --gg: 10px; }
  .rack { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .cards { grid-template-columns: minmax(0, 1fr); }
}
```
{: data-filename="~/Projects/status_dashboard/dashboard.css · 일부 생략, 주석 생략, 떨어져 있는 규칙을 한데 모음"}

카드가 3열이면 계기는 6열, 카드가 2열이면 계기는 4열(다음 줄에 둘), 카드가 1열이면 계기는 2열이다. 계기 두 칸과 그 사이 간격 하나를 합친 폭은 카드 한 장의 폭과 같다. 두 격자가 같은 `--gg` 간격과 같은 꺾임점을 써야 이 등식이 지켜져서, 좁은 화면에서 `--gg`를 줄일 때도 `:root`에서 한 번에 바꾼다. 작업 세션에서는 1440·1100·800·390px로 렌더해 칸 경계가 맞는 것을 봤다. 같은 이유로 알림 섹션의 요약 네 칸도 4열 아니면 2열 두 줄로만 바뀐다. 1100px 폭에서는 카드가 2열이 되고, 계기는 넷과 둘로 나뉘어 카드 한 장 아래에 두 칸씩 맞물린다.

![1100px 폭의 상태 대시보드. 계기 6칸이 4열로 접혀 2열 카드 한 장 폭에 두 칸씩 맞물린다](/assets/images/Misc/LLM_Workshop/Status_Dashboard-narrow.png)

상단의 이름도 이날 정해졌다. 6월의 머리줄은 `STATUS Raspberry Pi 5`였고, 새 머리줄에는 처음에 `pi5 / status`라고 적었다. 사용자는 둘 다 아니라 "Raspberry Pi Dashboard"로 하라고 했다. 6월에 지어 둔 HTML의 `<title>`이 이미 그 이름이었으니, 머리줄이 다섯 달 만에 제 이름을 따라잡은 셈이다.
