---

title: "섀도 판정의 재검토 큐"
excerpt: "사람이 판례를 새로 쓰면 비슷한 링크를 다시 모델에 돌리는 재검토가 같은 링크를 되풀이해 사람 앞에 올리던 문제와, 섀도 원장이 다 찬 뒤에야 돌게 한 게이트"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/shadow_recheck

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-13
weight: 74
group: agents

---

관련 파일: [`scripts/dependency-classifier/shadow_digest.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_digest.py), [`shadow_tick.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_tick.py), [`shadow_store.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_store.py), [`test_shadow.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/test_shadow.py), [커밋 fedb9c97](https://github.com/math-jh/math-jh.github.io/commit/fedb9c97), [커밋 02978607](https://github.com/math-jh/math-jh.github.io/commit/02978607)
{: .notice--info}

링크 판정 화면에 Bruhat decomposition 쪽 링크가 같은 모양으로 계속 올라왔다. 사용자는 판정이 글 단위로 한 번 돌고 넘어가야 하는데 왜 다시 보이느냐고 물었다.

> 지금 링크 판정기에 Bruhat decomposition 쪽 링크가 계속 반복해서 들어오는데, 이유가 있어? 글 단위라서, 한 번 처리하면 넘어가야 하는 것 같은데 계속 다시 보여서 물어보는거야.

이유는 있었다. [링크 관계 섀도 재판정](/ko/llm_workshop/shadow_rejudging)에서 만장일치로 끝난 링크는 섀도 원장에 들어가고 더 이상 돌지 않지만, 사람이 판정에 설명을 달아 새 판례가 생기면 이미 끝난 링크 일부를 그 판례로 다시 보는 경로가 따로 있다. 반복해서 올라온 것은 그 경로가 보낸 링크였다.

## 판례가 생기면 끝난 링크를 다시 보는 경로

판례는 사람의 설명을 digest 워커가 초안으로 쓰고, 사람이 대시보드에서 승인해야 생긴다. 초안에는 `recheck` 필드가 있다. 이 판정이 고치는 실수를 같은 모양으로 저질렀을 법한, 이미 끝난 링크의 목록이다. 후보는 모델이 고르지 않고 워커가 먼저 걸러서 보여 주고, 모델은 그 안에서만 고른다(`"recheck": from RECHECK CANDIDATES only`). 후보의 조건은 판정을 받은 링크들의 Step 1 답과 같은 꼴(`basis`, 대상의 종류, 증명 안인지 여부)이다. 초안이 승인되면 고른 링크가 `queue["recheck"]`에 `{lid, precedent, created}`로 들어간다.

큐의 항목 하나는 `shadow_tick.run_recheck`가 처리한다. 세 차수(S1·S2·S3) 모두에서 Step 4(판례 대조)를 현재의 판례집으로 다시 돌려, 세 답이 기존 값에 그대로 머물면 값을 유지하고 아니면 `kind: "recheck"`로 사람의 판정 대기에 올린다. 모델이 판례를 읽고 값을 바꾸는 일은 이 경로가 열려 있다는 것만으로 생긴다.

## 후보를 걸러내지 않던 선택기

고치기 전의 `_recheck_candidates`는 판례가 생길 때마다 `shadow_store.UNITS_DIR`의 글 단위 파일을 이름순으로 훑으면서, 조건에 맞는 링크를 `RECHECK_OFFER`(40)개 채울 때까지 모았다.

```python
out = []
for path in sorted(store.UNITS_DIR.glob("*.json")):
    record = store.read_json(path, {})
    if record.get("unit") in paused:
        continue
    for lid, rec in record.get("links", {}).items():
        if lid in ruled or not (rec.get("final") or {}).get("relation"):
            continue
        ...
        if key in patterns:
            out.append({"id": lid, "relation": rec["final"]["relation"],
                        "evidence": s1["evidence"], "reason": s1["reason"]})
        if len(out) >= RECHECK_OFFER:
            return out
return out
```
{: data-filename="scripts/dependency-classifier/shadow_digest.py · fedb9c97 이전, 일부 생략"}

건너뛰는 조건은 초안·개정 중인 글, 방금 판정받은 링크 자신, 판정 값이 없는 링크 셋뿐이었다. 그래서 세 가지가 겹쳐 있었다.

- 정렬 순서가 고정이라 40개가 차는 지점이 늘 같고, 파일명이 앞서는 글의 링크가 판례마다 후보로 올라왔다.
- 이미 `recheck` 큐에서 기다리는 링크가 다음 판례의 후보로 또 올라와, 같은 링크가 큐에 여러 번 쌓였다.
- 사람이 이미 판정했거나 감사로 확인한 링크, 사람 대기열에 있는 링크도 후보였다. 모델이 세 답을 한 번 갈라 놓으면 사람이 정한 값 위에 다시 판정 요청이 올라오게 된다.

diff가 직접 보여 주는 것은 여기까지다. Bruhat 링크가 어느 경로로 몇 번 올라왔는지는 큐 기록으로 세어 보지 않았고, 위 세 가지가 반복을 만들 수 있는 구조라는 것만 확인했다.

## 후보 선택의 세 가지 제외 조건

[커밋 fedb9c97](https://github.com/math-jh/math-jh.github.io/commit/fedb9c97)은 선택기를 다시 짰다. 먼저 `shadow_store`에 사람이 결정권을 쥔 링크를 가려내는 함수가 생겼다.

```python
def human_decided(lid: str, rec: dict, queue: dict) -> bool:
    if (rec.get("final") or {}).get("by") in ("human", "audit"):
        return True
    return (queue["settled"].get(lid) or {}).get("how") == "audit"
```
{: data-filename="scripts/dependency-classifier/shadow_store.py · 일부 발췌, 독스트링 생략"}

확정 기록의 `by`가 `human`이거나 `audit`이면 사람이 정한 값이다. 감사 표본에 뽑혀 사람이 확인만 하고 `queue["settled"]`에 `audit`으로 남은 링크도 같은 취급이다. 감사가 만장일치를 뒤집었든 그대로 두었든, 모델이 사람의 판단을 다시 여는 일은 없어야 한다는 뜻이다.

`_recheck_candidates`는 이 함수와 사람 대기열(`queue["human"]`), 이미 재검토 대기 중인 링크(`queued`)를 모두 제외한다. 대기 중인 링크는 기다리는 동안 새 판례도 같이 보게 되므로 다시 올릴 이유가 없다. 후보를 모으는 방식도 바뀌었다. 40개가 차면 멈추는 대신 조건에 맞는 링크를 전부 모은 뒤 `rechecks` 이력의 길이(다시 본 횟수)가 적은 순으로 정렬하고 앞의 `RECHECK_OFFER`개만 낸다.

```python
random.shuffle(found)
found.sort(key=lambda x: x[0])
return [c for _, c in found[:RECHECK_OFFER]]
```
{: data-filename="scripts/dependency-classifier/shadow_digest.py · 일부 발췌"}

`sort`는 안정 정렬이어서 먼저 섞어 두면 같은 횟수 안에서는 순서가 무작위가 된다. 한 글이 파일명 때문에 모든 판례의 후보가 되는 일이 사라지고, 다시 본 적 없는 링크가 먼저 나간다.

`run_recheck` 쪽에도 같은 조건이 걸렸다. 큐에 오래 있던 항목은 그동안 사람이 판정했을 수 있으므로, 처리 시작 때 `human_decided`로 다시 확인해서 해당하면 모델을 부르지 않고 큐에서 뺀다(`the human decides this link`). 모델 호출은 몇 분이 걸려서 그 사이에도 대시보드에서 판정이 들어올 수 있다. 호출이 끝난 뒤에는 디스크의 최신 레코드를 다시 읽어 거기에 재검토 결과를 넣고, 그 사이 사람이 정한 값이 있으면 판정 대기에 올리지 않고 사람의 값을 남긴다. 큐에서 빼는 비교도 항목 전체가 아니라 `lid`로 바뀌어, 한 링크에 여러 판례로 쌓인 항목이 한 번의 실행으로 같이 정리된다. Step 4가 판례집 전체를 읽으므로 한 번의 실행이 그 링크의 모든 대기 항목에 답하기 때문이다.

## 섀도 원장이 찬 뒤에야 도는 재검토

사용자는 선택기를 고치는 것과 별개로 재검토의 시점도 바꾸자고 했다. 같은 시각의 발화는 이렇다.

> 고쳐주고, 재검토 자체를 내 생각엔 섀도원장 다 채우고 나서 나오는게 맞는 것 같아.

몇 분 뒤에는 이렇게 물었다.

> 재검토는 끝나지 않아? 계속 재검토할거야?

판례가 늘 때마다 끝난 링크가 다시 돌면 판정이 끝나는 시점이 없어 보인다는 질문이다. 재검토 자체는 글 하나가 3차까지 한 번 도는 틱과 따로 한 틱을 먹는다. 아직 첫 라운드를 받지 못한 글은 그 라운드에서 모든 판례를 한꺼번에 만나므로, 그 전에 끝난 링크를 판례 하나씩 다시 돌리면 모델 호출만 늘고 얻는 것이 없다.

`shadow_tick.py`의 틱 순서에는 그래서 단계가 하나 생겼다. 크론 한 번이 하는 일은 `lid` 정리, digest 한 건, 재검토 한 건, 글 하나의 한 차수 순으로 이어지고, 재검토는 `fill_complete`가 참일 때만 돈다.

```python
def fill_complete(state: dict) -> bool:
    all_paths = units.all_units()
    skip = out_of_scope(all_paths)
    entries = state["units"]
    for paths in all_paths:
        key = dc.unit_key(paths)
        if key in skip:
            continue
        entry = entries.get(key)
        if entry is None:
            if _cheap_lids(paths):
                return False
        elif entry.get("next") and not entry.get("parked_fp"):
            return False
    return True
```
{: data-filename="scripts/dependency-classifier/shadow_tick.py · 일부 발췌, 독스트링 생략"}

초안과 개정 중인 글(`out_of_scope`)은 어차피 판정하지 않으므로 세지 않는다. 상태에 항목이 없는 글은 판정할 링크(`_cheap_lids`)가 있을 때만 아직 안 찬 것으로 본다. 항목이 있어도 `next`(다음 차수)가 남아 있으면 라운드가 진행 중이다. 단 `parked_fp`가 붙은 글, 곧 프롬프트가 한도를 넘겨 글이 바뀔 때까지 세워 둔 글은 기다리지 않는다. 이미 끝난 글에 새 링크가 생긴 경우는 판정 중인 라운드가 아니므로 재검토를 막지 않는다. 기다릴 이유가 있는 것은 아직 한 번도 판정받지 않은 글이다. 재검토가 대기 중이어도 이 조건이 거짓이면 `run_recheck`는 `False`를 돌려주어 틱이 곧바로 글의 한 차수로 넘어간다. 대기 중인 항목은 큐에 그대로 남아 있다가 조건이 참이 된 뒤에 처리된다.

`shadow_classifier.py status`의 출력에는 `recheck`(큐 길이)와 `recheck_open`(`fill_complete`의 값)이 추가되어, 재검토가 왜 멈춰 있는지 상태 한 줄로 볼 수 있다. 이 게이트는 `test_shadow.py`의 테스트로 확인했다. 재검토가 대기 중이어도 원장이 차기 전에는 모델을 부르지 않고, 찬 뒤에는 처리되는지를 본다.

## 판례 인용이 달라도 값이 같으면 유지

두 번째 커밋 [02978607](https://github.com/math-jh/math-jh.github.io/commit/02978607)은 재검토의 판정 기준 한 줄을 바꾼다. 처음에는 세 차수의 관계가 모두 기존 값이고 인용한 판례가 하나로 일치해야 값이 유지됐고, 하나라도 다르면 사람에게 갔다.

```python
elif relations == {final} and len(precedents) == 1:
    log(f"shadow recheck {lid}: still {final} under {item['precedent']}")
```
{: data-filename="scripts/dependency-classifier/shadow_tick.py · 02978607 이전, 일부 발췌"}

```python
elif relations == {final}:
    log(f"shadow recheck {lid}: still {final} under {item['precedent']}")
```
{: data-filename="scripts/dependency-classifier/shadow_tick.py · 일부 발췌"}

관계가 셋 다 그대로인데 한 차수는 판례 P-0001, 다른 차수는 P-0002를 인용했다는 이유로 사람 앞에 올릴 이유는 없다. 값은 바뀌지 않았고, 사람이 볼 것은 값이 달라진 링크다. 같은 변경에서 테스트의 헬퍼가 세 차수에 서로 다른 판례(`P-0001`, `P-0002`, `none`)를 인용하게 바뀌었고, `weak` 링크가 이 조건에서 큐에 오르지 않고 값을 유지하며 `rechecks` 이력에 한 건이 남는 테스트(`test_recheck_keeps_an_unchanged_value_whatever_the_precedents`)가 추가됐다. 이 변경은 [링크 관계 섀도 재판정](/ko/llm_workshop/shadow_rejudging)에서 처음 설명한 최초 판정의 만장일치 규칙과는 다르다. 최초 판정은 판례가 갈려도 사람에게 보내고, 재검토만 판례의 인용 차이를 값의 변동으로 보지 않는다.

## 남은 일

이 변경들이 반복되던 링크를 실제로 줄였는지는 아직 확인하지 않았다. 선택기와 게이트는 테스트에서 동작을 확인했을 뿐이고, 섀도 원장이 다 차는 시점은 글의 수와 쿼터가 정하므로 그 전에는 재검토가 큐에 쌓이기만 한다. 사람이 판례를 새로 쓸 때마다 후보가 최대 40개씩 쌓이는 구조도 그대로이고, 사람의 판정이 모델에게 거꾸로 되먹임되는 이 경로가 얼마나 많은 호출을 쓰는지는 원장이 찬 뒤에야 보인다.
