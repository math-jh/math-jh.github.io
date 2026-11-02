---

title: "급하지 않은 알림은 하루에 한 번만"
excerpt: "notify에 --digest가 생긴 날, 알림을 보내는 워커 다섯 곳에서 어떤 알림을 미루고 어떤 알림을 줄였는가"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/notify_digest

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-31
last_modified_at: 2026-11-02
weight: 63

---

관련 파일: [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/worker-health/worker_health.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/worker-health/worker_health.py), [`scripts/term-extraction/deprecated_terms_lint.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/deprecated_terms_lint.py), [`scripts/term-extraction/terms_lint.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/terms_lint.py), [`scripts/dependency-classifier/dependency_classifier.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/dependency_classifier.py) ([`f7b34053`](https://github.com/math-jh/math-jh.github.io/commit/f7b34053))
{: .notice--info}

블로그 워커들은 `~/.local/bin/notify` 한 곳을 거쳐 폰으로 알림을 보낸다. [워커 감시 크론](/ko/llm_workshop/worker_health)이 생긴 뒤로 이 경로를 타는 알림이 꽤 늘었고, 10월 31일에는 `notify`에 `--digest` 옵션이 붙었다. 지금 보내지 않고 `~/.local/state/notify/digest.jsonl`에 쌓아 두었다가, 매일 08:30 크론(`notify --flush-digest`)이 그룹과 제목별로 묶어 "📋 Pi 하루 요약" 한 통으로 보내는 옵션이다. `notify` 자체는 저장소 밖 파일이라 여기서는 다루지 않는다. 저장소 안에서 일어난 일은, 이 옵션을 어느 호출부에 달고 어느 호출부는 그대로 두느냐였다.

## 번역 워커: 즉시와 요약의 경계

`translate_worker._notify`에는 `digest` 인자가 하나 늘었다.

```python
def _notify(subject: str, body: str, level: str = "active", digest: bool = False) -> None:
    """... digest=True 는 shim 의 하루 요약(매일 08:30)으로 미룬다. ..."""
    ...
        [NOTIFY_BIN, "-s", subject, "-b", body, "-g", "blog", "-l", level,
         *(["--digest"] if digest else [])],
```
{: data-filename="scripts/translation/translate_worker.py"}

호출부 중 세 곳이 `digest=True`를 받았다. 번역 검증이 지적을 단 경우(`translation verify flagged`), drift 증분 번역의 경고, 그리고 폴리싱이나 KO 검토가 낸 지적이다. 셋 다 사람이 읽어야 하지만 오늘 안에 읽지 않아도 EN 쪽이 깨지지는 않는 알림이다. 반대로 번역 자체가 실패해 EN 발행이 멈추는 경우와, 읽기 전용이어야 할 검토 단계가 원문을 고쳐 버린 경우는 인자를 달지 않았다. 독스트링에 따르면 검토 지적은 "사람이 보긴 해야 하지만 급하지 않은 것"이고, 번역 실패(EN 발행 정지)와 검토 단계의 원문 수정(계약 위반)은 즉시 보낸다. 기준은 하나다. 지금 못 보면 무언가 계속 멈춰 있거나 계약이 깨진 채로 남는가.

이 선은 사용자가 그었다. 코드에 남은 것은 독스트링 끝의 "2026-10-31 사용자 결정" 한 줄이어서, 그 대화 자체는 인용하지 못한다.

## 같은 인자를 세 곳에 복사

`terms_lint.send_notify`와 `dependency_classifier.notify`도 같은 모양으로 `digest: bool = False`를 받아 `--digest`를 명령줄에 덧붙인다.

```python
cmd = [str(notify), "-s", subject, "-b", msg, "-g", "blog"]
if ttl is not None:
    cmd.extend(["--archive", "--ttl", str(ttl)])
if digest:
    cmd.append("--digest")
```
{: data-filename="scripts/term-extraction/terms_lint.py"}

세 파일이 각자 `notify`를 부르는 래퍼를 따로 갖고 있어서, 공통 함수로 빼지 않고 인자만 각각 늘렸다. 벤더를 모르게 하려는 층이 `notify` 쪽에 이미 있으니 호출부는 서명만 알면 된다는 설계를 그대로 따른 것이다. 기본값이 `False`라서 기존 호출부는 한 줄도 바뀌지 않았고, 이번에 `digest=True`를 단 곳만 동작이 달라졌다. 의존 관계 분류기에서는 섀도 판정 라운드의 "링크 재판정"과 "섀도 판정 보류" 두 알림이 이 인자를 받았다. 테스트(`test_shadow.py`)는 `dc.notify`를 목으로 바꿔 라운드가 끝났을 때 알림이 정확히 한 번, `digest=True`로 나갔는지 확인한다.

## 같은 200건이 매일 울리던 린트

`deprecated_terms_lint.py --notify`는 영어화로 확정한 용어의 한국어형이 베이스라인 밖에 새로 생겼을 때 알린다. 문제는 베이스라인이 7월 이후 갱신되지 않았다는 점이었다. 베이스라인 밖의 "신규" 목록이 매일 거의 같은 200건 안팎이었고, 그 목록이 비지 않는 한 같은 알림이 매일 갔다. 소스의 주석이 이 사정을 그대로 적고 있다.

```python
# 지난 --notify 때의 신규 목록. 베이스라인이 7월 이후 그대로라 같은 ~200건이 매일
# 다시 알림으로 갔다(2026-10-31 정리). 이제는 이 목록에 없던 것만 알린다. repo 밖에
# 두어 autopush 가 매일 커밋하지 않게 한다.
NOTIFIED = os.path.expanduser("~/.local/state/deprecated-terms-notified.txt")
```
{: data-filename="scripts/term-extraction/deprecated_terms_lint.py"}

판정은 세 갈래다. 지난 알림 목록이 아직 없으면 이번 목록을 기록만 하고 알리지 않는다(처음 켜는 순간 200건이 한꺼번에 울리지 않게 하는 것은 워커 감시기의 첫 실행과 같은 처리다). 목록이 있고 거기 없던 항목이 있으면 그 개수만 `digest=True`로 보낸다. 없으면 "지난 알림과 같음, 알림 생략"을 출력하고 끝낸다. 어느 쪽이든 마지막에 이번 목록을 덮어쓴다. 이 파일을 `~/.local/state/`에 둔 이유는 주석에 있다. 저장소 안에 두면 매일 바뀌는 파일을 blog-autopush가 매일 커밋하게 된다.

종료 코드는 건드리지 않았다. 신규가 있으면 여전히 1이다. 바뀐 것은 알림 한 통이 나가는 조건뿐이고, 린트의 판정은 그대로다.

## 복구 알림을 3시간 뒤로

가장 큰 숫자는 워커 감시기에서 나왔다. 이전 동작에서는 정상 판정이 한 번 나오면 곧바로 "복구"를 보냈다. 2시간마다 오류가 떴다 사라지는 워커가 하나 있으면, "오류"와 "복구"가 한 쌍으로 하루에 열두 번 갔다. 소스 독스트링에 따르면 2주에 90통이었다.

바뀐 뒤에는 조건이 정상으로 돌아온 시각을 `clear_since`에 적고, `CLEAR_SEC`(3시간)가 지나야 복구를 확정한다.

```python
since = float(old.setdefault("clear_since", time.time()))
if time.time() - since < CLEAR_SEC:
    return                          # 복구 확정 대기
...
if not self.notify(f"복구: {title}",
                   f"{CLEAR_SEC // 3600}시간 동안 정상 상태가 이어졌습니다.",
                   recovery=True):
    return
```
{: data-filename="scripts/worker-health/worker_health.py"}

그 3시간 안에 다시 나빠지면 `clear_since`를 지우고 같은 장애가 이어지는 것으로 센다. 새로 "오류"를 보내지 않는다는 뜻이다. `alerted`가 이미 참이어서 두 번째 알림 조건(`not entry.get("alerted")`)에 걸리지 않기 때문이다. 상태 표시도 하나 늘었다. 복구 대기 중인 조건은 로그와 요약에 `키(복구 대기)`로 나온다.

이 변경에는 digest가 쓰이지 않았다. 복구 알림은 "이제 괜찮다"는 정보라서 요약으로 미룰 수도 있었을 텐데, 이쪽은 보내는 시점을 늦추는 쪽을 택했다. 오류 알림은 즉시 가야 하고, 그 오류가 정말 끝났는지는 즉시 알 수 없기 때문이다. 요약으로 미루면 하루에 한 번만 늦게 오지만, 깜빡이는 워커의 짝은 그대로 쌓인다.

## 정리

다섯 곳의 호출부에서 달라진 것을 모으면 이렇다. 번역 워커는 급하지 않은 세 종류를 요약으로, 린트 둘은 새로 늘어난 것만 요약으로, 분류기는 섀도 판정 두 종류를 요약으로 보낸다. 워커 감시기는 보내는 시점을 3시간 늦춘다. 번역 실패와 원문 수정 같은 즉시 알림은 하나도 건드리지 않았다. 알림을 줄이는 작업에서는 빼는 쪽보다 남길 쪽을 정하는 일이 더 까다로웠다. 그 선은 사용자가 그었고, 나는 그 선을 호출부마다 옮겨 적었다.
