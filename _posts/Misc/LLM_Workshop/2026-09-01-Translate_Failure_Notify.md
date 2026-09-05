---

title: "쿼터가 마르면 조용해지는 번역 워커"
excerpt: "실패가 쌓여도 알림이 없던 자리에 쿨다운 알림을 놓고, 그 김에 안 쓰던 hermes를 걷어내고 notify shim으로 갈아탄 일"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/translate_failure_notify

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-01
last_modified_at: 2026-09-01

weight: 47

---

관련 파일: [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/pr-notify/notify_open_prs.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/pr-notify/notify_open_prs.py), [43729b7f](https://github.com/math-jh/math-jh.github.io/commit/43729b7f), [62c307b3](https://github.com/math-jh/math-jh.github.io/commit/62c307b3)
{: .notice--info}

번역 워커는 Kimi K3로 돌고, 실패하면 다음 글로 넘어가 다음 틱에 다시 시도한다. 문제는 Kimi 사용량 쿼터가 지난 지 며칠이 지나도록 아무도 몰랐다는 것이다.

> 지금 일단 블로그 트랜슬레이션 관련해서 내가 키미 K3가 사용량 쿼타 지난 지 좀 됐는데, 그 사이에 번역된 것들 있지. 그 사이에 번역됐어야 했었던 것들. 그게 실제로 됐는지 안 됐는지 한 번만 확인해줘. 그러니까 지금 로그만 봐서는 내가 단정할 수 없는 게 에러가 떴는데, 그다음에는 다음 글로 넘어갔단 말이야. 그래서 이게 정상적으로 번역 실패로 취급하고 다음 글로 넘어가서 다음 버킷에 들어오는 건지. 아니면 그냥 조용히 실패해버린 건지 확인하고, 만약에 조용히 실패한 거라면 문제 해결해놔.

로그를 뒤져보니 정상적으로 실패 처리는 되고 있었다. `state.json`에 `status: failed`가 남고 24시간 백오프를 타고 다음 글로 넘어간다. 큐는 안 막혔다. 다만 이 실패를 아무도 밖으로 알리지 않았을 뿐이다. 2026-08-30~31 사이 실패가 10번 있었는데 알림은 0통이었다.

## 실패를 알림으로 잇기

`record_failure`가 새로 생긴 자리다. 기존 코드는 실패마다 `state["files"][key]`를 새 딕셔너리로 통째로 갈아끼웠는데, 그러면 안 된다. `translated_at`·`en_path`·`verified_at` 같은 그 글의 번역 이력이 `status: failed` 한 줄에 덮여 사라진다. 그러면 다음 Phase 4가 `verified_at`이 없어진 글을 다시 검증하려 들고, 대시보드와 term-extract는 이미 번역된 글을 미번역으로 센다. 그래서 엔트리는 `dict.update`로 상태만 얹는다.

```python
def record_failure(state: dict, key: str, error: str) -> None:
    now = time.time()
    entry = dict(state["files"].get(key) or {})
    entry.update({"status": "failed", "last_attempt_ts": now, "error": error[:500]})
    state["files"][key] = entry

    notice = state.setdefault("failure_notice", {})
    notice["count"] = int(notice.get("count", 0)) + 1
    notice.setdefault("since", now)
    if now - notice.get("last_notified", 0) < FAIL_NOTIFY_COOLDOWN_SEC:
        return
    notice["last_notified"] = now
    since = datetime.fromtimestamp(notice["since"]).strftime("%m-%d %H:%M")
    _notify(
        "[translate-worker] 번역 실패",
        f"{key}\n연속 {notice['count']}회 (최초 {since})\n"
        f"{error[:300]}\n"
        f"실패한 글은 {FAIL_RETRY_AFTER_SEC // 3600}시간 뒤 자동 재시도한다.",
        level="timeSensitive",
    )
```
{: data-filename="scripts/translation/translate_worker.py"}

워커는 30분마다 돈다. 실패마다 알림을 그대로 보내면 쿼터가 죽어 있는 하루 동안 48통이 온다. `failure_notice`에 연속 실패 횟수와 최초 실패 시각을 누적해 두고, `FAIL_NOTIFY_COOLDOWN_SEC`(6시간)이 지난 것만 실제로 보낸다. 알림 본문에는 "연속 몇 회, 최초 언제부터"가 들어가니 6시간에 한 번 와도 그 사이 몇 번 더 실패했는지는 안다. 엔진이 살아나 성공하면 `state.pop("failure_notice", None)`으로 카운터를 지워, 다음 장애는 다시 첫 통부터 센다.

## hermes 철거와 notify shim

실패 알림 자체는 이걸로 끝났어야 했는데, 다른 제안이 따라왔다.

> 실패 경로에 텔레그램 알림 없는 건 괜찮아. 근데 지금 추가 제안은: 내가 요즘 hermes agent를 전혀 안 써. 오직 telegram 전송용으로만 쓰는데, 마침 telegram이 요즘 좀 맘에 안 들어. 스팸이 너무 많이 와서 짜증나거든. 그래서 디스코드나 별도 API 달아줄 수 있는 플랫폼으로 옮기되, 어차피 안 쓰는 hermes는 철거하고, 알림을 그 API로 직결하는 게 수순이 맞는 것 같아서 그렇게 하려 하거든.

hermes는 에이전트 웹 UI([Local_Services](/ko/llm_workshop/local_services) 글에서 다룬 그 서비스)인데, 실제로 남아 쓰이던 기능은 텔레그램 전송 하나뿐이었다. 그 하나 때문에 프로세스 격리에 TOTP까지 걸어둔 서비스 전체를 유지할 이유가 없다는 것이 사용자의 판단이었다.

대안으로 ntfy.sh, Bark, Nextcloud Talk을 견줬다. ntfy.sh는 공용 서버를 중계로 쓰거나 자체 서버를 띄워야 했고, Nextcloud Talk은 이미 쓰는 Nextcloud 인프라라 별도 앱 설치가 필요 없다는 게 장점으로 꼽혔다.

> 아니면 nextcloud talk은? bark랑 nextcloud talk 사이에 고르자. nextcloud talk은 별도 앱 설치 없어도 되는게 장점.

그럼에도 결정은 Bark였다.

> bark 배선 가자.

Bark는 iOS 앱이 발급하는 디바이스 키로 `api.day.app`에 HTTP POST를 쏘면 그 기기로 push가 오는 구조다. 키와 함께 암호화용 AES 키·IV를 대화 밖에서 생성해 Pi에 저장했다. 대화 기록에 비밀값이 남지 않도록, 생성 스크립트만 짜고 실행은 이 세션 바깥에서 사용자가 직접 했다.

```
notify -s "암호화 테스트" -b "본문이 읽히면 성공"
```
{: data-filename="bash"}

이 호출은 stdout이 비는 게 정상이다. 성공 여부는 본문이 실제로 휴대폰에서 읽히는지로만 확인한다. 검증이 끝나자 hermes는 그 자리에서 철거됐다.

> hermes 철거부터 하자.

## `_notify`로 갈아타기

이후 커밋에서 `translate_worker.py`의 `_notify_telegram`이 `_notify`로 바뀌었다. hermes CLI를 직접 부르던 자리가 새 shim `~/.local/bin/notify` 호출로 바뀌었을 뿐 아니라, 인자 하나가 늘었다.

```python
NOTIFY_BIN = shutil.which("notify") or str(Path.home() / ".local/bin/notify")


def _notify(subject: str, body: str, level: str = "active") -> None:
    """Best-effort 알림. 실패해도 로그만 남기고 번역은 계속한다.

    벤더는 shim(~/.local/bin/notify) 안에만 있다. 여기서 아는 것은 서명뿐이다.
    """
    try:
        r = subprocess.run(
            [NOTIFY_BIN, "-s", subject, "-b", body, "-g", "blog", "-l", level],
            check=False, timeout=20, capture_output=True, text=True,
        )
        if r.returncode != 0:
            log(f"notify failed rc={r.returncode}: {r.stderr.strip()[:300]!r}")
    except Exception as e:
        log(f"notify exception: {e!r}")
```
{: data-filename="scripts/translation/translate_worker.py"}

워커 쪽에서 아는 것은 서명뿐이고, 실제로 Bark를 부르는지 다른 채널을 부르는지는 shim 안에 갇혀 있다. `-g blog`로 알림을 그룹으로 묶고, `-l`로 알림 등급을 넘긴다. 대부분의 호출은 기본값 `active`를 그대로 쓰지만, `record_failure`는 명시적으로 `timeSensitive`를 넘긴다.

```python
    _notify(
        ...,
        level="timeSensitive",     # EN 발행이 멈춘 상태다 — 집중 모드를 뚫는다
    )
```
{: data-filename="scripts/translation/translate_worker.py"}

번역 자체를 검토 단계가 건드리는 계약 위반(`KO 검토가 원문을 수정함`) 알림도 같은 등급을 받는다. 나머지, 예를 들어 verify가 mismatch를 잡아 보내는 알림은 `active`로 남았다. 큐가 멈췄다는 신호와 검토용 참고 알림을 같은 무게로 다루지 않겠다는 구분이다.

같은 커밋이 `notify_open_prs.py`를 비롯한 term-lint 스크립트 몇 개도 함께 hermes에서 이 shim으로 옮겼다. 다만 그쪽은 `HERMES` 상수를 `NOTIFY`로 바꾸고 인자 형식만 맞춘 기계적 치환이고, `level`을 쓰는 곳은 지금은 번역 워커뿐이다.

## 정리

쿼터가 죽어도 조용하던 워커는 이제 6시간에 한 번, 연속 실패 횟수를 실어 알린다. 그 알림이 도착하는 경로는 hermes를 거치지 않는다. 텔레그램이 스팸으로 시끄러워 옮긴 것인데, 정작 옮긴 이유였던 알림은 워커가 죽어 조용했던 문제를 고치는 김에 딸려 나왔다. 순서가 앞뒤로 조금 뒤바뀐 채로긴 해도, 결과적으로 두 문제가 한 커밋 거리로 붙어서 풀렸다.
