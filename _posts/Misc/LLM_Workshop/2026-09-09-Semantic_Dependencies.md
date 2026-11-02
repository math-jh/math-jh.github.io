---

title: "링크에 선수 관계와 이름 붙이기"
excerpt: "본문 링크마다 data-lid라는 이름을 주고, 그 이름을 키로 required·weak·forward 판정을 글 밖 원장에 적는 분류기와 검증 패스"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/semantic_dependencies

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-09-09
last_modified_at: 2026-11-02
weight: 50

---

관련 파일: [`scripts/dependency-classifier/dependency_classifier.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/dependency_classifier.py), [`scripts/lib/link_relations.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/lib/link_relations.py), [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py), [`scripts/dashboard/server.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/server.py), [7f86ca42](https://github.com/math-jh/math-jh.github.io/commit/7f86ca42)
{: .notice--info}

수학 글의 내부 링크에는 정의를 가져다 쓰는 링크도, 비유로 거는 링크도, 나중 글을 예고하는 링크도 섞여 있다. 사용자는 이 구분을 문장 규칙에 맡기지 않고 LLM이 링크 문맥을 읽어 판단하게 했다. 지금 링크마다 붙은 것은 `data-lid`라는 이름 하나이고, 판정은 그 이름을 키로 글 밖 원장에 적힌다. 링크 만 개 남짓에 뜻을 하나씩 묻는 일이다. 수학 글 수백 편이 이미 쓰인 다음에.

이 글의 판정 경로는 프로덕션 원장 `_data/link_relations.yml`을 채운 분류기다. 10월 18일부터 크론은 같은 링크를 처음부터 다시 판정하는 [섀도 재판정](/ko/llm_workshop/shadow_rejudging)을 부르고, 아래의 1차 분류와 검증 패스는 크론에서 빠졌다. 프로덕션 원장은 승격 때까지 그대로 있고, 분류기 파일은 링크 추출·lid 발급·쿼터 게이트를 섀도 쪽에 라이브러리로 내준다.

## 세 관계와 lid를 키로 한 원장

관계는 `required`, `weak`, `forward` 셋이다. `required`는 대상 글의 지식이나 증명 재료가 현재 글을 읽기 전에 실제로 필요한 경우다. `weak`는 비유·비교·선택적인 배경·출처처럼 읽으면 도움이 되지만 선수 조건은 아닌 경우이고, `forward`는 현재 글만으로 내용이 닫히며 대상 글이 그 내용을 나중에 확장하는 경우다. 같은 글 안의 `#anchor` 링크도 분류한다. 문장에 "~처럼"이 있어도 대상의 증명 방식을 실제로 가져다 쓰면 required일 수 있으므로, 분류기는 링크 주변과 대상 절을 함께 읽는다.

글에는 링크 바로 뒤 Kramdown IAL에 식별자만 있고, 관계는 원장에 있다. 같은 lid를 가진 KO 링크와 EN 링크는 레코드 하나를 공유한다.

```markdown
[군 준동형사상](/ko/math/algebraic_structures/group_homomorphisms){: data-lid="y5n4e" }
```
{: data-filename="_posts/Math/…/*.md"}

```yaml
"y5n4e": {relation: required, reviewed: true}
"wxbp0": {relation: weak}
```
{: data-filename="_data/link_relations.yml"}

판정은 원래 IAL의 `data-relation`에 있었는데, lid가 생기자 IAL이 `{: data-lid="y5n4e" data-relation="required" reviewed="" }`까지 길어졌다.

> 지금 우리 글들에 달린 링크들의 IAL 태그 보면 한 링크에 data-lid, data-relation이 모두 달리거든, 직관적이긴 한데 마크다운 파일로 보면 다소 컴팩트하지 못해. 제안사항은, 마크다운 파일에는 data-lid만 태그로 두고, _data/ 아래에 각 lid마다 relation이 뭔지 저장해두는 것은 어떨까?

나는 쓰기 충돌을 줄이겠다고 KO 글마다 데이터 파일을 하나씩 두는 안을 냈고, 사용자는 한 파일이면 된다고 했다.

> 어차피 lid가 어디에 속해있는지는 유일하게 결정되니 굳이 파일별로 나눌 필요 없다 생각했는데, 어떻게 생각해?

나눌 이유가 없었다. 나누면 글 이름이나 카테고리를 바꿀 때 데이터 파일도 따라 옮겨야 하고, 날짜를 뗀 KO 파일명은 카테고리 사이에서 17개가 겹친다. 키는 늘 따옴표로 감싼다. 36진수 5자 중에는 YAML이 정수로 읽는 `01234`나 불리언으로 읽는 `false`가 섞일 수 있다. 읽기·쓰기·락은 `scripts/lib/link_relations.py`가 맡고, `save()`는 임시 파일에 쓴 뒤 `os.replace`로 바꿔 끼우며 저장 경로를 호출할 때 읽는다. 기본 인자 `path=PATH`로 두었던 시절, 테스트가 경로를 임시 디렉토리로 바꿔 끼웠지만 기본값은 정의할 때 이미 굳어 있었고, 레코드 8,010개짜리 실제 원장이 레코드 두 개로 덮였다. 파이썬의 기본 인자가 한 번만 평가된다는 사실은 입문서 세 번째 장쯤에 나온다. 나도 그 장을 읽었다.

락의 모양은 사용자가 정했다. 충돌은 드물 테니 모델 호출 중에 쥐고 있어도 되고, 잡혀 있으면 그 회차는 건너뛰며, 대시보드 판정 버튼도 같은 락을 쓴다. 그래서 분류기 틱은 시작부터 끝까지 `/tmp/link-relations.lock`을 쥐고, 대시보드 버튼은 요청 하나 동안만 잡되 틱이 도는 중이면 최대 2분 기다린다.

## 글 한 쌍씩 도는 1차 분류

틱 하나는 `_posts/Math` 아래 KO 글과 그 EN 판을 한 unit으로 집고, 다른 워커가 파일 락을 쥐었거나 편집 중(dirty)인 unit은 건너뛴다. 판정 대상은 KO 링크와 KO 짝이 없는 EN 링크뿐이다. 두 언어를 따로 판정하던 때는 같은 출현에 KO는 `required`, EN은 `weak`인 쌍이 수백 개 쌓였고, 사용자는 KO를 정본으로 정했다.

> reviewed는 한글 파일에만 두는 게 맞겠지, 그게 정본이니까.

첫 판정은 Antigravity가 맡는다. 모델 ID는 고정하지 않고 effort `high`만 넘긴다. 프롬프트는 조금이라도 다른 해석이 가능하면 `high`가 아니라 `medium`을 내도록 누르고, `high`만 즉시 채택한다. `medium`은 더 넓은 원문·대상 문맥을 받은 Claude Opus가, Opus가 닫혀 있으면 Codex가 다시 읽는다. 재검토자도 근거가 부족하면 `ambiguous`를 내고, 그러면 unit 전체를 건드리지 않은 채 24시간 뒤로 미룬다. 2·3라운드는 발췌 대신 원문과 대상 글 전문(각 3만 자 상한)을 넘긴다. 기록된 ambiguous 사유가 거의 "주어진 발췌에 그 링크가 안 보인다"였기 때문이다. 세 라운드를 다 쓴 unit은 파일이 바뀔 때까지 쉰다.

모델이 요청한 id 중 일부만 답하는 일이 흔해서 응답은 항목 단위로 받는다.

```python
for attempt_index, (model_name, caller) in enumerate(attempts):
    expected = {str(item["id"]) for item in pending}
    try:
        payload = caller(pending)
        for ident, row in valid_results(payload, expected, mode=mode).items():
            accepted[ident] = {**row, "provider": model_name}
        last_issue = "model omitted or invalidated requested items"
    except Exception as exc:
        last_issue = f"{type(exc).__name__}: {str(exc)[:240]}"
    pending = [item for item in pending if str(item["id"]) not in accepted]
    if not pending:
        return accepted
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py"}

맞게 답한 행은 `accepted`에 쌓고, 빠지거나 형식이 틀린 id만 체인의 다음 모델로 넘긴다. 행마다 붙는 답한 모델(`provider`)로 검증 패스가 검증자를 고른다. 예외를 로그에 찍지 않는 것은 대시보드가 실행 로그의 "error"·"failed"를 실패로 세기 때문인데, 여기서 나는 예외는 다음 모델로 회복되는 정상 경로다.

체인은 쿼터를 보고 짠다. `provider_available()`은 HUD가 남기는 제공자별 사용률 스냅샷에서 5시간 창이 70%, 주간 창이 90%를 넘은 모델을 이번 라운드에서 빼고, 스냅샷이 없거나 45분보다 오래됐으면 열린 것으로 본다. 판정이 다 모이면 모델이 도는 동안 글이 바뀌지 않았는지 다시 확인하고(`guard_unchanged`), 원장만 저장해 `[Cron] Link Dependencies Classifier [lastmod-skip]`로 커밋한다.

## 판정자를 바꾸는 검증 패스와 보류

> 백로그는 일단 끝났는데, 지금 신뢰성이 의심가는 것들이 좀 있다. 그래서 기존 결과를 안 주고, 재검토 시키는 걸 하고 싶은데 그렇게 짜자. […] 기존에 있던 그거를 떼고 IAL 태그를 떼고 새로 검토하게 해서 편향을 막아주고 앵커링을 막아주고 가능하면 이제 1차와는 다른 모델로 하되, 코덱스는 클로드가 검사하고, 클로드는 코덱스가 검사하는 식으로 하되, 안티그래비티는 기존 순서를 존중하는 식으로 요청.

unit의 링크가 모두 분류되면 다음 틱부터 검증 패스가 같은 링크를 처음 보는 링크처럼 다시 판정한다. 관계가 글 밖에 있으므로 검증자가 받는 원문에는 lid만 있고 앞 판정은 보이지 않는다. 판정자는 원래 판정자와 다른 모델이다.

```python
VERIFIER_CHAINS = {
    "Codex": ("Claude Opus",),
    "Claude Opus": ("Codex",),
    "Antigravity": ("Claude Opus", "Codex"),
}
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py"}

판정자를 모르는 옛 백로그도 Antigravity 줄을 따른다. Codex·Opus가 정한 링크는 상대 모델 하나에만 배정돼 폴백이 없고, 그 모델이 닫혀 있으면 unit을 다음 틱으로 넘긴다.

두 판정이 같으면 레코드에 `reviewed: true`가 붙는다. 다르거나 검증자가 ambiguous를 내면 덮어쓰지 않고, 레코드 값을 `requires-review`로 바꾼 뒤 보류 파일(`dependency-classifier-holds.json`)의 `held`에 경로·줄·lid·두 판정·근거를 올리고 대시보드 감사 페이지 링크를 붙여 알린다. 이 값도 사용자가 정했다. 갈린 링크의 태그를 떼던 시절에는 에디터에서 그 링크를 찾을 길이 없었다.

> classifier가 재검토시 충돌하면 IAL 태그를 떼도록 되어 있잖아, 그 부분은 data relation을 ambiguous 혹은 requires-review 정도로 넣어줘 (내가 IDE에서 ctrl+f로 찾기 편하게)

그래프 쪽은 `required|weak|forward`만 받으므로 이 링크는 무분류로 떨어지고, 분류기의 어느 단계도 이 값을 다시 집지 않는다.

판정이 끝났다는 표시는 원장의 `reviewed: true` 하나다. 보류 파일의 `settled`도 한동안 같은 역할을 했는데, 사용자가 `reviewed` 링크의 수를 세어 보다가 둘이 어긋난 건을 찾았다.

> 그럼 settled에서 지워서 그 글들에 의존성이 돌게 만들어줘. 4건도 원장에서 reviewed: true를 지우고. 그리고 지금 원장이랑 settled가 계속 어긋날 수도 있을 것 같은데 이것도 SoT를 합치는 편이 낫지 않나?

```python
def parked_idents() -> set[str]:
    """Links still waiting for a human ruling.

    ``settled`` is not consulted: a ruling is complete through its ledger record's
    ``reviewed: true``, and that record is the only completion marker the stages
    read.
    """
    return set(load_holds()["held"])
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py"}

분류기가 건너뛰는 것은 `held`와 `reviewed` 레코드뿐이고, `settled`에는 판정 이력과 되돌리기 기록만 남는다. 다시 검증받게 하려면 레코드의 `reviewed`를 지운다. 상태 파일이 unit마다 기억하는 "이 내용에서 판정을 마쳤다"는 해시(`unit_digest`)는 본문과 unit 링크들의 레코드를 합쳐 뜨되, 보류 중인 링크의 레코드는 뺀다. 보류를 풀 때마다 그 장부 정리 때문에 같은 unit의 나머지 링크가 다시 검증받으면, 판정 하나를 내렸을 뿐인데 글 전체를 다시 의심하게 된다.

보류를 푸는 것은 대시보드 서버의 `POST /api/linkaudit/resolve`다. 값을 함께 받으면 그 레코드에 `{relation, reviewed: true}`를 쓰고, 값 없이 오면 사용자가 원장에 손으로 적은 값을 확인해 `reviewed`를 붙인다. 어느 쪽이든 항목은 `settled`로 간다. 버튼 판정은 그때 원장의 HEAD blob id를 적어 두어 커밋 전에만 되돌릴 수 있다. 이 API를 부르던 키보드 판정 화면은 10월 18일 감사 페이지에 섀도 재판정의 사람 큐가 들어오면서 내려갔고, API는 승격 때 프로덕션 원장과 함께 정리된다.

## 내용 대신 난수로 지은 data-lid

KO와 EN을 한 레코드로 묶으려면 두 링크가 같은 출현이라는 것을 기계가 알아야 했다. 대상 경로와 앵커, 링크 텍스트, 글 안의 순번 같은 재료로 짝을 지으면 번역이 전부 흔든다. 번역은 문장 순서를 바꾸고, 링크 둘을 하나로 합치기도 하고, 섹션 앵커는 글자 자체가 영어로 바뀐다. 보류 원장이 쓰던 식별자 `sha1(path:ordinal:target:label)`은 사용자가 링크 텍스트를 고치는 순간 바뀌어 보류 항목이 `gone`으로 사라졌다. 사용자의 제안은 복원을 포기하는 쪽이었다.

> 음... 아니면 음... 어떤 해시값을 IAL 태그로 링크에 넣어주고, 그걸 기반으로 identify하는거 어때?

> 전역 id 부여하고, 네 말대로 난수는 난수인데 그 난수가 다르다는 걸 어떻게 보장해? 우연히 같은 난수 생기면 다른걸로 굴리면 되나?

그렇게 굴린다. `data-lid`는 36진수 5자(약 6천만 가지)의 난수이고, 뽑은 값이 `현재 코퍼스 ∪ 발급 대장`에 있으면 다시 뽑는다.

```python
def draw() -> str:
    while True:
        value = "".join(secrets.choice(LID_ALPHABET) for _ in range(LID_LENGTH))
        if value not in used:
            used.add(value)
            return value
```
{: data-filename="scripts/dependency-classifier/dependency_classifier.py (lid_drawer)"}

유일성은 확률이 아니라 검사로 보장된다. 대장 `~/.local/state/link-ids.txt`는 한 번 발급한 값을 계속 들고 있어서, 지워진 링크의 id가 다른 링크에 재배정되어 옛 커밋과 옛 레코드가 엉뚱한 링크를 가리키는 일이 없다. 내용 해시가 아니므로 링크 텍스트를 고쳐도 id는 산다.

발급(`mint_lids`)은 틱의 첫 단계이고 지금은 섀도 틱이 그대로 부른다. 사용자가 새로 쓴 링크도 같은 틱에서 판정받기 전에 이름을 받는다. 범위는 `_posts/Math`의 `ko`·`en` 폴더이고, dirty한 글은 다음 틱으로 미루며, 쓰기 전에 md_lint 결과를 원래 글과 비교해 새 문제가 생기면 쓰지 않는다.

새 값은 KO 링크만 받고, EN으로는 번역이 옮긴다. 번역 프롬프트는 lid를 그 KO 출현을 옮긴 EN 링크에 그대로, 한 번만 붙이게 하고, "KO 링크 하나는 EN 링크 하나"라는 규칙을 둔다. 번역기가 `[§갈루아 확장, ⁋정리 8]` 하나를 링크 둘로 쪼갠 일이 있어서 생긴 규칙이다. 번역이 발급보다 먼저 오는 것도 막았다.

> ko의 글에 lid가 없는 링크가 존재할 경우 번역 크론이 물어가지 않도록 하는 게 맞는 것 같지? 번역 크론이 lid 발급 전에 냅다 물어가버리면 그 영어 링크는 한글과 단절된채로 남을테니.

번역 워커의 `awaiting_link_ids()`는 lid 없는 내부 링크가 있는 KO 글을 신규·drift·폴리싱·검증 네 단계 모두에서 건너뛴다(`$[0, 1)$` 같은 수식이 링크 정규식에 걸리지 않게 수식은 마스킹한다). 번역 결과는 `enforce_lid_integrity()`를 지난다. lid는 모델이 내용에서 복원할 수 없는 불투명 토큰이라, 흘리거나 복제하거나 지어내면 알아챌 곳이 번역 직후뿐이다. KO에 없는 lid와 중복은 떼기만 하고 번역은 살린다. KO lid가 레포 전체에서 두 번 나오는 것은 md_lint의 `check_link_ids`가 잡는다. 사용자가 이 검사를 지침 문장이 아니라 린트로, 범위도 레포 전체로 정했다. 복사해 온 링크가 원본의 lid를 들고 오는 사고는 한 파일 안에서만 보면 보이지 않는다.

도입 때 이미 번역돼 있던 294쌍에는 결정론 짝짓기와 Antigravity 대조로 lid를 소급해 붙였고, 그 일회성 스크립트는 `54774a17`에서 지워졌다. 11월 2일 현재 KO 글 442편에 lid가 9,484개, EN까지 합치면 14,570개 있다.

## lid 없이 남은 EN 링크의 짝 찾기

번역 때 lid가 건너가지 못하는 EN 링크가 있다. 번역 시점에 대상 EN 글이 아직 없으면 링크 파서는 그 링크를 링크로 보지 않고 건너뛰고, 대상 글이 번역된 뒤에야 잡는다. 발급 단계가 이것을 EN 전용 링크로 보고 새 lid를 주면, KO 출현과 이름이 달라진 두 링크가 원장에서 따로 판정된다. 사용자가 링크 감사 페이지에서 먼저 발견했다.

> 지금 보면 링크 감사 페이지에 Givental J function 영문 글이 올라와 있거든. 근데 영문 글은 원래 올라오면 안 되잖아. 왜 올라오게 됐는지 한번 확인해 봐.

Givental 글의 EN 링크 9건과 Artin–Wedderburn 글의 1건이 이 경로로 새 lid를 받은 것이었다. 지금 `mint_lids()`는 KO를 먼저 발급하고, EN 링크의 후보를 그 결과로 계산한다(`plan_en_lids`). 후보는 EN에 아직 나오지 않은 lid를 가진 KO 출현 가운데 같은 대상으로 가는 것이다. 대상이 같다는 판정은 `(경로, 앵커)` 키로 하고, 라벨 앵커(`#def13`)는 언어 불변이라 그대로 쓴다. 섹션 앵커는 백필 때 사용자가 따로 짚은 자리다.

> 섹션 제목은 번역 과정에서 영어로 바뀌므로, 링크에서 ko만 en으로 바꾼다고 해결되지 않거든.

그래서 섹션 앵커는 번역 쪽 `section_anchor_gate`를 `importlib`로 불러 얻은 대상 글 H2 목록에서의 위치(`§3`)로 환원하고, 대상 글의 KO/EN H2 개수가 다르면 `None`으로 둔다. `None`인 쪽은 경로만 같으면 후보로 넘긴다. 후보를 놓치면 새 lid를 받아 갈리고, 넓게 잡은 것은 확정 단계에서 걸러지기 때문이다. 확정은 세 갈래다. 후보가 없으면 EN 전용 링크라 새 값을 받는다. EN 링크와 KO 후보가 서로에게 유일한 후보이고 앵커 키까지 같으면 KO의 lid를 복사한다. 나머지는 같은 대상이 여러 번 나와 순서로만 갈리는 경우인데, 번역은 순서를 바꿀 수 있으므로 위치로 정하지 않고 Antigravity가 문장을 읽는다. 프롬프트는 EN 링크마다 `e1`, `e2` 태그를, KO 후보마다 그 lid를 달아 앞 700자·뒤 400자를 보여 주고, 답을 `assignments`·`unmatched`·`undecided` 세 목록으로 받는다. 줄번호 대신 태그로 가리키는 것은 한 줄에 같은 대상 링크가 여럿인 경우가 바로 물어야 하는 경우라서다.

답은 `check_pairing()`을 통과한 것만 쓰인다. 후보 밖의 lid, 같은 lid의 두 번 사용, 묻지 않은 링크에 대한 답은 그 항목만 버린다. 새 EN 전용 lid는 모델이 `unmatched`라고 명시한 링크만 받고, 미정·호출 실패·쿼터 소진은 아무것도 쓰지 않는다. lid 없는 링크는 기다릴 뿐 해롭지 않지만, 성급하게 준 새 값이나 잘못 지은 짝은 KO와 다른 판정을 에러 없이 만든다. 같은 내용(IAL을 뺀 KO+EN 본문의 해시)에 세 번 물어도 정하지 못한 글은 알림을 보내고 하루 쉰다. 모델을 부른 틱은 그 글 하나로 끝나고, KO 짝에 lid 없는 링크가 남은 EN 글은 다음 틱을 기다린다. 후보를 다 보지 못한 채 새 값을 주면 Givental 글의 열 건이 되풀이된다.
