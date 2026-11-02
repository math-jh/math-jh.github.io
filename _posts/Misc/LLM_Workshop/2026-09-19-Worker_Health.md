---

title: "블로그 워커 상태 판정과 감시 크론"
excerpt: "대시보드가 워커의 정지·오류·hold를 판정하는 규칙과, 그 판정을 5분마다 읽어 상태 전이만 Bark blog 그룹으로 알리는 감시 크론"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/worker_health

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-19
last_modified_at: 2026-11-02
weight: 57

---

관련 파일: [`scripts/worker-health/worker_health.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/worker-health/worker_health.py), [`scripts/dashboard/server.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/server.py), [`scripts/dashboard/app.js`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/app.js), `~/.local/bin/cron-gate` (레포 밖)
{: .notice--info}

[블로그 운영 대시보드](/ko/llm_workshop/dashboard)는 워커마다 지금 도는지, 마지막 실행에 오류가 있었는지, 일부러 멈춘 것인지를 계산해 보여 준다. 판정은 대시보드 서버의 `sec_workers()`에 있고, 화면과 감시 크론이 같은 판정을 읽는다. 화면은 사람이 열어야 보이므로, 그 판정을 알림으로 밀어 주는 감시기가 따로 돈다.

## 로그 시각으로 재는 워커 생존

워커 정의는 `WORKERS` 목록 한 곳에 있다. 워커마다 cron 주기 `interval`(초)과 로그 경로를 두고, 마지막 실행 뒤 지난 시간이 `1.2×interval`을 넘으면 `late`, `2.5×interval`을 넘으면 `stale`, 로그가 아예 없으면 `missing`이다.

이 판정은 워커가 돌 때마다 로그에 흔적을 남긴다는 약속 위에 서 있다. [찾아보기 자동 갱신](/ko/llm_workshop/term_extraction)의 `term_extract_worker.py`에는 그 약속을 어기는 경로가 둘 있었다. 고를 글이 없는 틱은 `return 0`으로 곧장 끝났고, 감사가 `terms.yml`을 실제로 고친 성공 경로는 알림만 보내고 로그에는 아무것도 적지 않았다. 정상으로 도는 워커가 빨간불로 떴다. 지금은 할 일 없는 틱도 `log("대상 없음 (본문 세대별 2회 완료)")`를 남기고, `terms.yml`을 쓴 감사도 바꾼 게 없는 틱과 같은 형식의 `감사 {letter}: …` 줄을 남긴다([커밋](https://github.com/math-jh/math-jh.github.io/commit/521857c529c0d673b20c5113705c2fb98f8ff248)). 침묵도 결과 중 하나라고 여기던 워커였지만, 판정을 보는 쪽에서는 그 침묵과 죽음을 구분할 방법이 없다.

번역 워커와 한글 수정 후속 워커는 `translation.log` 하나를 같이 쓴다. 둘을 한 항목으로 묶으면 후속 워커만 멈춰도 본 워커가 로그를 갱신해 정지가 안 보이므로, 두 워커는 별개 항목이고(`8e327dcb`) `worker_log_lines()`가 공유 로그를 `KO-FOLLOWUP:` 접두사로 나눠 읽는다. 타임스탬프로 시작하는 줄에서 접두사를 보고 그 뒤의 연속 줄을 같은 쪽에 붙이며, 마지막 실행 시각도 파일 mtime이 아니라 자기 몫 줄의 마지막 타임스탬프에서 읽는다. 이 귀속 규칙은 번역 워커의 로그 문구에 기대므로, 워커가 접두사를 바꾸면 한쪽으로 쏠린다.

## 마지막 실행분만 보는 오류 판정

워커 카드의 오류 표시는 로그에서 오류 문구를 찾아 켠다. 범위가 로그 꼬리 10줄이던 때는 사흘 전에 한 번 죽고 그 뒤로 멀쩡히 도는 워커도 그 트레이스백이 꼬리에 남아 있는 한 빨간불이었다. 지금 범위는 마지막 실행분이다([커밋](https://github.com/math-jh/math-jh.github.io/commit/3fc8a0e6)).

```python
_ERR_RE = re.compile(r"traceback|\bexception\b|\bfail(ed|ure)\b|\berrors?\s*[:=]\s*[1-9]"
                     r"|\berror\b(?!s?\s*[:=]\s*0)", re.I)
_LOG_ECHO_RE = re.compile(r"\bVERIFY \([^)]*\) attempt \d+: ")


def _last_run_lines(path, interval, n=10, lines=None):
    ...
    gap = max(300, interval * 0.25)
    start = stamps[0][0]
    for (i, ts), (_, prev) in zip(stamps[1:], stamps):
        if ts - prev > gap:
            start = i
    return lines[start:]
```
{: data-filename="scripts/dashboard/server.py"}

실행 경계는 타임스탬프 간격으로 잡는다. 간격이 `max(300초, 주기/4)`를 넘으면 다른 실행이다. 이 값은 한 실행 안의 줄 간격보다 커야 하고(GSC 전체 스윕은 10분 넘게 벌어진다), 실행 사이 간격보다는 작아야 한다. 타임스탬프 없는 줄은 직전 줄의 실행에 붙으므로 마지막 줄 뒤에 붙은 크래시 트레이스백도 그 실행에 잡힌다. `_ERR_RE`는 `errors=0`처럼 오류 없음을 보고하는 요약줄을 부정 전방탐색으로 뺀다.

번역 검증기의 verdict 전문이 같은 로그에 들어오면서 생긴 오탐도 있다. 영어 산문 안에 `failure`가 들어간 문장 하나가 정상 실행을 빨간불로 뒤집었다.

> 일 똑바로 안 하니? 번역워커 로그 오류 떴는데 뭔지 확인해봐.

정규식을 더 좁히는 대신 모델이 쓴 줄을 스캔에서 뺐다. 워커는 모델의 verdict를 한 줄씩 `VERIFY (...) attempt N: ` 접두사를 달아 찍고, 자기 상태 줄은 `attempt N/3:`처럼 분모를 함께 적는다. `_LOG_ECHO_RE`는 분모 없는 앞쪽 꼴만 잡으므로, 모델이 뭐라고 썼든 워커 자신의 상태 줄만 판정에 남는다.

이 판정은 워커가 줄마다 날짜와 시각을 찍는다는 약속에도 기댄다. 타임스탬프가 하나도 없는 로그는 마지막 10줄로 돌아가므로, 시각만 찍던 `blogdev-bot/lib.sh`의 `log()`에 날짜를 붙이고 접두사가 없던 `audit/check_links.py`에는 시작 줄을 넣었다. 시작 줄이 있어야 도중에 죽어 남은 트레이스백이 그 실행에 붙는다. 시각 없는 오류 줄은 거꾸로 엉뚱한 실행을 물들인다. 지금은 없어진 댓글 수집 워커가 GitHub API의 503을 시각 없이 찍었을 때 그 오류가 직전 성공 실행 몫으로 잡혔고, 오류 줄에도 성공 줄과 같은 형식의 시각을 찍게 고친 뒤로는 재시도가 성공하면 실패한 실행의 오류가 자기 경계 안에 갇혀 판정 밖으로 밀려났다([커밋](https://github.com/math-jh/math-jh.github.io/commit/d1af20cd)).

## cron-gate 정지 버튼과 hold 소유권

대시보드의 `#cron` 섹션은 블로그 크론 잡마다 정지·재개 버튼을 단다. 버튼을 눌러도 서버는 crontab을 고치지 않는다. crontab은 director·sync_slots·safety_net이 락 없이 통째로 다시 쓰는 파일이라 웹 핸들러가 끼어들면 lost update가 난다(2026-07-18 번역 워커 줄 소실 사고). 대신 크론 줄이 `{ cron-gate <id> ; [ $? -ne 1 ] ; } && <원래 명령>` 꼴로 게이트를 앞에 둔다. `cron-gate`는 `~/.local/state/cron-pause/<id>.json`을 보고 정지 중이면 exit 1을 내고, 다른 코드로 죽으면 뒤 명령이 돈다(fail-open). 서버는 `cron-gate --jobs`·`--pause`·`--resume`을 부를 뿐 상태 파일을 직접 만지지 않는다. 건드릴 수 있는 잡은 서버의 `CRON_JOBS` id가 허용목록으로 정해서 POST 바디의 `id`가 그 집합에 없으면 400이다.

잡을 멈추는 주체는 둘이다. 대시보드 버튼, 그리고 모델 쿼터의 5시간·7일 사용률이 기준을 넘으면 그 모델을 쓰는 블로그 크론을 리셋 시각까지 멈추는 `quota-reset-watch.py`(quota governor)다. 둘이 같은 잡을 각자 멈출 수 있으므로 상태 파일은 owner별 hold map(`"holds": {owner: {paused_at, until, reason}}`)이고, hold가 하나라도 살아 있으면 정지다. 대시보드 hold의 owner는 `blog-dash`, governor의 것은 `quota-governor:<provider>:<window>`이고, 서버는 이것을 `userPaused`와 `quotaPaused`로 갈라 받는다.

재개 버튼은 `--resume <id> --by blog-dash`로 자기가 건 hold만 풀고, governor의 hold는 그것이 계산한 리셋 시각까지 남긴다. 쿼터로 멈춘 잡을 리셋 전에 깨우는 것은 `quotaPaused`인 잡에만 나타나는 `강제재개` 버튼이고, `cron-gate`가 아니라 `quota-reset-watch.py --force-resume <id>`를 부른다. governor가 지금 hold를 풀고 그 provider의 리셋까지 다시 걸지 않으므로 효력은 이번 리셋에서 끝난다. 초록(`var(--ok)`)은 `강제재개`에만 있고 평범한 `재개`·`정지`는 회색이다. 되돌릴 수 있는 정상 재개와 governor 판단을 덮어쓰는 강제재개를 같은 색으로 두지 않으려는 것이다([커밋](https://github.com/math-jh/math-jh.github.io/commit/8a46efe5), [버튼 색 분리](https://github.com/math-jh/math-jh.github.io/commit/82bc6543)).

정지된 워커는 로그가 늙는 것이 당연하다. 서버는 크론 잡을 워커 키별 리스트(`cron_by_worker`)로 모으고, 워커에 걸린 크론이 정지면 `status`를 `paused`로 바꾸고 `err`를 끈다.

```python
schedules = cron_by_worker.get(w["key"], [])
paused = bool(schedules) and all(p.get("paused") for p in schedules)
...
if paused:
    status = "paused"
    err = False
```
{: data-filename="scripts/dashboard/server.py"}

화면의 `badWorkers`가 `w.paused`를 거르는 것만으로는 `status`가 `stale`로 남아 그 필드를 읽는 다른 소비자에게 정지가 고장으로 보였다([커밋](https://github.com/math-jh/math-jh.github.io/commit/b0dcaa8f)). 정지는 그 워커의 크론 **전부**가 정지일 때만 참이다(하나라도 돌면 로그가 갱신될 수 있다). 한때 `blog-translation`과 `blog-translation-followup`이 같은 `worker="translation"`을 달고 있었는데, `{j["worker"]: j for j in …}` 꼴의 dict는 나중 잡이 앞 잡을 덮어써서 `paused`가 크론 목록의 순서로 정해졌다([커밋](https://github.com/math-jh/math-jh.github.io/commit/d625b035)). 지금은 두 잡의 워커 키가 갈라졌지만, 한 워커를 여러 스케줄이 깨우는 구성이 다시 생겨도 덮어쓰기로 돌아가지 않도록 집계는 리스트로 남아 있다.

## 상태 전이만 알리는 감시기

처음 붙인 위치는 Pi 전체를 보는 `pi-health-monitor`였다. 그런데 알림이 Bark의 Pi 그룹으로 왔고, 사용자가 방향을 바꿨다.

> 음... 이걸 pi-health-monitor보다는 별도 blog 크론으로 붙이는 게 맞는 것 같아, 둘 다.

그래서 `worker_health.py`가 따로 생겼다(`08c3ed82`). 5분마다 `cron-gate blog-worker-health` 뒤에서 돌고, 알림은 전부 `notify -g blog`로 보낸다. 감시기는 워커 로그 대신 대시보드의 `/api/summary`를 읽는다. 같은 판정을 두 번 구현하면 둘이 어긋나기 때문이다. 보는 것은 워커 정지(`stale`·`missing`), 워커 오류(`err`), 크론 등록 누락과 `blog-autopush.timer` 비활성이다. 대시보드가 응답하지 않으면 로그만 남기고 끝나고, 대시보드 중단은 `pi-health-monitor`가 알린다.

모든 조건은 같은 상태 기계를 탄다. `THRESHOLD`는 2, `CLEAR_SEC`는 3시간이다.

```python
entry["count"] = int(entry.get("count", 0)) + 1
entry["body"] = body
if entry["count"] >= THRESHOLD and not entry.get("alerted"):
    if self.notify(title, body, recovery=False):
        entry["alerted"] = True
...
if old.get("alerted") and not old.get("muted"):
    since = float(old.setdefault("clear_since", time.time()))
    if time.time() - since < CLEAR_SEC:
        return                          # 복구 확정 대기
```
{: data-filename="scripts/worker-health/worker_health.py"}

5분 간격 점검에서 두 번 연속 나쁘면 한 번 알린다. 멈춘 워커 소식을 10분 안에 들고 오는 감시기라니, 나보다 성실하다. 나는 불려야 온다. 복구 알림은 정상이 3시간 이어져야 보내고, 그 사이에 다시 나빠지면 `clear_since`만 지우고 같은 장애가 이어지는 것으로 본다. 정상 판정 한 번에 바로 복구를 보내던 때는 2시간마다 오류가 떴다 꺼지는 워커 하나가 '오류/복구' 한 쌍을 하루 12번, 2주에 90통 보냈다. 전송이 실패하면 `alerted`도 복구도 확정하지 않아 다음 점검에서 다시 시도한다. 상태 파일이 없는 첫 실행에서 이미 나빠 있는 조건은 `muted`로 기준선에 넣어, 설치하는 순간 있던 이상이 한꺼번에 울리지 않게 한다.

오탐은 두 종류를 거른다. 하나는 정지를 **푼 직후**다. 정지 동안 늙은 로그가 남아 있어서 재개한 순간부터 다음 실행 전까지는 stale로 읽힌다. 그래서 정지를 마지막으로 본 시각을 `last_paused`에 적어 두고, 거기서 한 주기에 15분을 더한 동안은 stale 조건을 억제한다. 다른 하나는 중복 알림이고, 사용자가 이 지점을 먼저 물었다.

> 근데 블로그 워커들이 실패 시에 혹시 별도로 Bark 알림을 보내지 않아? 그럼 방금 추가한 이게 겹치지 안ㅢ뉘ㅏ 싶어서.

겹친다. 번역 워커는 실패하면 `failure_notice`를 세우고 쿨다운을 지켜 알리고, 용어 추출 워커는 글 단위 실패를 세다가 세 번째에 그 글을 격리하며 알린다. 그래서 `WORKER_HANDLED`가 워커별로 그 오류를 워커가 이미 붙잡아 관리 중인지 묻는다. 번역은 state의 `failure_notice`를, 용어 추출은 글별 `fails`와 최근 격리를 본다. 붙잡힌 실패는 감시기가 다시 알리지 않고, 워커가 예외로 죽어 자기 state에 흔적을 못 남긴 실패는 그대로 알린다. 워커의 자체 알림 경로가 닿지 못하는 곳만 감시기가 덮는 분업이다.

## 헬스체크가 떠안은 요약 계산

`pi-health-monitor`는 1분마다 4초 타임아웃으로 `/api/summary`를 찌른다. 요약 계산 `build_summary()`는 원장이 바뀐 직후 수 초가 걸려서, 캐시가 막 만료된 순간의 헬스체크가 그 계산을 기다리면 타임아웃이 나고 거짓 "대시보드 중단" 알림이 된다. TTL을 45초에서 90초로 늘려서는 그 순간이 드물어질 뿐이라([커밋](https://github.com/math-jh/math-jh.github.io/commit/e1fee03c)), TTL은 45초로 돌아가고 갱신이 백그라운드로 갔다([커밋](https://github.com/math-jh/math-jh.github.io/commit/f1011d87)).

```python
def summary_cached():
    now = time.time()
    if _cache["data"] is None or _cache["ts"] == 0:
        _cache["data"] = build_summary()
        _cache["ts"] = now
    elif now - _cache["ts"] > CACHE_TTL and _refresh_lock.acquire(blocking=False):
        threading.Thread(target=_refresh_summary, daemon=True).start()
    return _cache["data"]
```
{: data-filename="scripts/dashboard/server.py"}

만료 뒤 첫 요청은 옛 값을 바로 받고, `_refresh_lock`을 논블로킹으로 잡으므로 갱신은 동시에 하나만 돈다. 요청이 계산을 기다리는 경우는 캐시가 빈 기동 직후와, 버튼이나 `?fresh`가 `ts`를 0으로 만들어 방금 누른 결과를 보여 줘야 할 때뿐이다. 백그라운드 갱신이 끝나면 `0 < _cache["ts"] < started`를 확인해서, 그 사이 버튼이 캐시를 무효화했거나 동기 빌드가 더 새 값을 넣었으면 늦게 끝난 옛 계산을 버린다. 값이 최대 한 TTL만큼 낡아 보일 수 있다는 것이 대가인데, 개요는 초 단위 정확도가 필요한 화면이 아니다.

계산 자체도 줄였다. `#audit`의 `sec_link_audit()`는 보류 항목이 가리키는 글을 분류기 파서로 다시 파싱하는데, 그 결과를 보류 원장·관계 원장·해당 글들의 mtime 튜플을 키로 캐시한다. 한 글에 몰린 보류 항목은 `post_links`의 `memo`로 글당 한 번만 파싱하고, 1만 줄 남짓한 링크 관계 원장은 libyaml이 있으면 `CSafeLoader`로 읽어 순수 파이썬 로더의 1초 넘는 로드를 피한다([커밋](https://github.com/math-jh/math-jh.github.io/commit/c41beafb)).
