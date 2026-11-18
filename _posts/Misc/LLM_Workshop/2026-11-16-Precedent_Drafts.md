---

title: "판례 초안의 승인과 정리안"
excerpt: "승인한 판례 초안이 그 사이 바뀐 판례를 덮어쓰지 않게 하는 지문 대조, 서로 겹치는 정리안의 걸러내기, 승격된 판례와 criteria.md 줄의 동기화"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/precedent_drafts

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-11-16
weight: 76
group: agents

---

관련 파일: [`scripts/dependency-classifier/shadow_digest.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_digest.py), [`scripts/dashboard/shadow_api.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/shadow_api.py), [`scripts/dashboard/shadow.js`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/shadow.js), [`test_shadow.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/test_shadow.py), [커밋 35c8042b](https://github.com/math-jh/math-jh.github.io/commit/35c8042b)
{: .notice--info}

판례 초안을 승인했더니 대시보드에 정리안 적용 실패가 세 줄 올라왔다. 사용자는 에러 문구를 그대로 붙여 확인과 함께 판정 대기 중인 것들의 타이브레이크를 요청했다.

> `정리안 적용 실패 — merge P-0016+P-0014: 병합은 살아 있는 판례 둘 이상이어야 한다 / merge P-0020+P-0010: 병합은 살아 있는 판례 둘 이상이어야 한다 / merge P-0033+P-0015: 병합은 살아 있는 판례 둘 이상이어야 한다` 에러 떴는데 확인해주고

## 초안에 딸린 정리안과 승인 순서

[링크 관계 섀도 재판정](/ko/llm_workshop/shadow_rejudging)에서 판례는 사람의 설명을 digest 워커가 초안으로 쓰고, 사람이 승인해야 생긴다. 초안은 판례 하나를 쓰는 데서 그치지 않고 `consolidation` 필드에 정리안을 실어 올 수 있다. 살아 있는 판례가 색인 한도에 가깝거나 어떤 판례가 승격 조건을 채웠을 때다. 정리안은 두 종류다. `promote`는 판례의 "원칙 초안"을 `criteria.md`의 "승격된 원칙" 절에 한 줄로 옮기고 판례의 상태를 `promoted`로 바꾼다. `merge`는 첫 판례가 나머지를 흡수한 새 본문을 쓰는 digest 작업을 큐에 올리고, 그 초안을 다시 승인하면 나머지가 `superseded`가 된다.

초안 승인(`shadow_api.draft`)은 판례를 쓴 뒤 딸린 정리안을 한꺼번에 적용한다. 고치기 전 반복문은 이랬다.

```python
done, failed = [], []
for c in sorted(props, key=lambda c: c.get("kind") != "promote"):
    try:
        done.append({"kind": c.get("kind"), "ids": c.get("ids"),
                     **consolidate(c.get("kind"), c.get("ids") or [])})
    except (ValueError, RuntimeError, KeyError) as e:
        failed.append({"kind": c.get("kind"), "ids": c.get("ids"), "error": str(e)})
```
{: data-filename="scripts/dashboard/shadow_api.py · 35c8042b 이전, 일부 발췌"}

승격이 먼저 적용되도록 정렬한다. 그런데 `merge`는 대상이 모두 `book.live("P")`에 있어야 하고, 이 목록은 상태가 `active`인 판례만 담는다. 승격된 판례는 `promoted`라서 목록에서 빠진다. 같은 초안이 어떤 판례를 승격하면서 그 판례가 든 병합도 함께 제안하면, 승격이 끝난 순간 병합의 전제가 사라지고 에러 문구는 "살아 있는 판례 둘 이상이어야 한다"가 된다. 사용자가 붙인 세 줄이 이 구조에서 나올 수 있는 모양이다. 다만 그 초안이 실제로 어떤 정리안을 실었는지는 큐 기록으로 확인하지 않았고, 이 글은 diff가 보여 주는 경로까지만 말한다.

## 서로 겹치지 않는 정리안만 남기기

수리는 두 군데에서 이루어졌다. 먼저 프롬프트에 규칙 한 줄이 붙었다. 한 판례는 정리안 하나에만 나오며, 승격하는 판례를 병합에 넣거나 같은 병합을 두 번 제안하지 말라는 것이다. 모델이 이 규칙을 지키리라는 보장은 없으므로 `_clean`이 모델 출력을 받는 자리에서 `clean_proposals`가 걸러낸다.

```python
live = {e.id for e in book.live("P")}
used: set[str] = set()
out = []
rows = [c for c in raw or [] if isinstance(c, dict) and c.get("kind") in ("merge", "promote")]
for c in sorted(rows, key=lambda c: c.get("kind") != "promote"):
    ids = list(dict.fromkeys(str(x) for x in c.get("ids") or [] if isinstance(x, str)))
    if c["kind"] == "promote":
        ids = [pid for pid in ids if pid in live and pid not in used]
        if not ids:
            continue
    elif len(ids) < 2 or any(pid not in live or pid in used for pid in ids):
        continue
    used.update(ids)
    out.append({**c, "ids": ids})
```
{: data-filename="scripts/dependency-classifier/shadow_digest.py · clean_proposals, 일부 발췌"}

승격을 먼저 훑어 `used`에 판례를 채워 두고, 병합은 대상이 하나라도 이미 쓰였거나 살아 있지 않으면 통째로 버린다. 승격은 판례 단위여서 쓸 수 있는 id만 남기고 계속 진행한다. 병합은 둘 이상이 모두 살아 있어야 뜻이 있으므로 일부만 남기지 않는다. `dict.fromkeys`는 순서를 지킨 채 중복 id를 지우고, 순서만 다른 같은 병합(`P-A+P-B`, `P-B+P-A`)은 두 번째가 `used`에 걸려 떨어진다.

정리안은 초안을 만들 때 한 번 걸러지지만, 승인은 며칠 뒤일 수 있다. 그 사이 다른 초안이 한 판례를 승격하거나 병합해 버렸을 수 있으므로 `shadow_api.draft`는 승인 시점에 `clean_proposals`를 다시 부른다. 걸러져 못 쓰게 된 제안은 실패가 아니라 건너뜀으로 따로 돌려주고(`consolidation_skipped`), 대시보드 카드는 "정리안 건너뜀(판례 상태가 바뀜)"이라는 별도 문구로 보인다. 실패 줄은 `consolidate`가 정말 에러를 던졌을 때만 남는다.

`apply_consolidation` 쪽에도 같은 종류의 가드가 생겼다. 대체되었거나 폐기된 판례는 승격할 수 없고, 이미 큐나 초안에 같은 판례 묶음의 병합이 기다리고 있으면(순서가 달라도) 두 번 올리지 않으며, 다른 병합에 이미 들어 있는 판례가 끼면 어느 판례가 걸렸는지 적어 에러를 낸다. 병합 작업이 큐에서 기다리는 사이 구성원이 승격되거나 폐기되었다면 `run_one`이 모델을 부르지 않고 그 작업을 큐에서 뺀다.

## 지문으로 알아내는 낡은 초안

두 번째 문제는 같은 판례를 고치는 초안이 둘 이상 대기할 때 생긴다. 초안 하나가 판례 P의 본문에 대한 `amend`나 `conflict`이면 digest 워커는 그 시점의 P를 읽고 새 본문을 쓴다. 다른 초안이 먼저 승인되어 P가 바뀐 뒤에 이 초안을 승인하면 앞 개정이 조용히 사라진다. 그래서 `_clean`은 초안에 `base`를 붙인다.

```python
def _stamp(entry: book.Entry | None) -> str | None:
    """A fingerprint of a precedent file, to tell whether it changed under a draft."""
    if entry is None:
        return None
    return hashlib.sha1(entry.path.read_bytes()).hexdigest()
```
{: data-filename="scripts/dependency-classifier/shadow_digest.py · 일부 발췌"}

`base`는 `{판례 id: 파일 SHA-1}`이다. 병합 초안은 흡수하는 쪽과 흡수되는 쪽 판례 전부의 지문을 담는다. `apply_draft`는 쓰기 전에 지문을 현재 파일과 비교하고, 달라진 판례가 있으면 초안(`action`이 `none`인 것은 제외)을 버린 뒤 원래의 digest 작업을 `redrafted` 횟수를 올려 큐에 다시 넣는다. 반환값은 `{"written": None, "requeued": [...]}`이고, 대시보드는 "판례 P-… 가 그새 바뀌어 초안을 다시 만든다"로 알려 준다. 사용자가 고른 선택이나 편집은 낡은 본문에 쓴 것이므로 같이 버려지고, 새 초안은 바뀐 본문에서 다시 시작한다. 낡은 초안에 딸려 있던 정리안도 이 초안과 함께 사라졌다가 다시 만들어진 초안에서 새로 제안된다(`shadow_api.draft`는 `requeued`일 때 일찍 반환한다). `test_stale_draft_is_drafted_again`은 초안을 만든 뒤 판례 본문을 직접 고쳐 놓고 승인해서, 고친 본문이 그대로 남고 작업이 `J-1`로 큐에 돌아오는지를 확인한다.

파일 해시를 쓴 이유는 판례의 어느 필드가 초안과 겹치는지 따지지 않아도 되기 때문이다. 설명 한 줄이 바뀐 것도, 본문이 바뀐 것도, 상태가 바뀐 것도 모두 지문을 바꾼다. 필요 이상으로 다시 쓰게 될 수는 있어도, 덮어쓰는 쪽으로 틀리지는 않는다.

## 승격된 판례와 criteria.md 줄의 동기화

승격된 판례는 `criteria.md`의 `### 승격된 원칙` 절에 `- (P-0016) …` 꼴의 줄로 산다. 모델은 판정마다 이 파일을 프롬프트에 받으므로, 이 줄이 판례의 현재 원칙과 다르면 모델은 폐기되거나 고쳐진 원칙으로 판정한다. 고치기 전에는 승격 때 줄을 한 번 쓰고 끝이었다. 이후 판례가 `amend`되어도, `conflict`로 대체되어도, 대시보드에서 폐기되어도 줄은 남았다.

`add_principles`가 `replace` 인자를 받아 같은 `(P-…)` 태그가 있으면 그 줄을 제자리에서 바꾸고, `remove_principle`이 줄을 지운다. 이 둘을 `sync_principle`과 `drop_principle`이 판례 상태에 맞춰 부른다.

```python
def sync_principle(pid: str) -> bool:
    e = book.get(pid)
    text = principle_text(e.body) if e is not None and e.status == "promoted" else None
    if text is None:
        return False
    path = sp.CRITERIA_PATH
    old = path.read_text(encoding="utf-8")
    new = add_principles(old, [f"- ({pid}) {text}"], replace=True)
    if new != old:
        store.write_text(path, new)
    return new != old
```
{: data-filename="scripts/dependency-classifier/shadow_digest.py · 독스트링 생략"}

승격된 판례가 `amend`나 `conflict`로 같은 id를 유지하면 `apply_draft`가 `sync_principle`로 줄의 문구를 갱신한다. 새 판례로 대체되는 `supersede`와 대시보드의 `revoke`는 `drop_principle`로 줄을 지운다. 줄은 `- (P-0016)`으로 시작하는 것만 대상이므로 다른 판례의 줄과 절 밖의 내용은 건드리지 않는다. `test_rewriting_a_promoted_precedent_rewrites_its_criteria_line`은 줄 두 개가 든 임시 `criteria.md`에서 `amend`가 해당 줄만 바꾸고 `conflict`의 `supersede`가 그 줄을 지우는 것, 대체된 판례를 다시 승격할 수 없는 것을 확인한다.

## 규칙 한 줄의 수정

같은 커밋에서 `criteria.md`의 P-0016 줄 자체도 고쳐졌다. 제공으로 보는 진술이 "대상의 가정과 결론을 그 꼴 그대로 담은 일반 부류에 대한 진술"이어야 한다는 한정이 붙었고, 주어가 지금 다루는 대상인 문장은 가정과 결론을 대상의 말로 모두 적었어도 적용 결과로 본다는 문장이 생겼다(대상이 바로 그 대상에 대한 진술이거나 대상의 가정이 유형뿐인 경우는 예외). 이 수정이 어떤 링크의 판정을 바꾸었는지는 확인하지 않았다. 커밋 메시지가 말하는 것은 기준 문구의 정밀화뿐이다.

## 확인한 범위

네 가지 동작은 모두 `test_shadow.py`에 단위 테스트가 있다(겹치는 정리안 걸러내기, 병합의 중복 대기와 죽은 병합 정리, 낡은 초안의 재큐, 승격 줄의 동기화). 실제 큐와 판례집에서 돌려 본 결과는 아니다. 사용자가 함께 요청한 판정 대기 건의 타이브레이크는 이 커밋의 범위 밖이다.
