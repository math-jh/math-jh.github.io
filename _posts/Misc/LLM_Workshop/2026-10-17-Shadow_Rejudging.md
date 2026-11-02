---

title: "세 모델의 블라인드 투표로 링크 관계 정하기"
excerpt: "Antigravity·Claude·Codex가 서로의 답을 모른 채 링크마다 투표하고, 만장일치만 섀도 원장에 들어가며 나머지는 판례와 함께 사람에게 가는 재판정 시스템"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/shadow_rejudging

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-17
last_modified_at: 2026-11-02

weight: 58

---

관련 파일: [`scripts/dependency-classifier/criteria.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/criteria.md), [`shadow_pipeline.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_pipeline.py), [`shadow_prompts.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_prompts.py), [`shadow_tick.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_tick.py), [`shadow_models.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_models.py), [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`scripts/dashboard/shadow.js`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/shadow.js), [커밋 d4928f2a](https://github.com/math-jh/math-jh.github.io/commit/d4928f2a), [커밋 a92861e7](https://github.com/math-jh/math-jh.github.io/commit/a92861e7)
{: .notice--info}

시작은 엉뚱한 질문이었다. 사용자가 Laya라는 판정 모델을 이 Pi에서 돌릴 수 있느냐고 물었고, 램을 따져 보니 체크포인트 하나는 들어가지만 둘은 무리였다. 물은 이유는 따로 있었다.

> 우리 그 의존성 링크 분류기가 정확히 그 사용사례에 부합하는 기능인 것 같아서 물어봤어.

[링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)의 분류기는 링크마다 required·weak·forward 중 하나를 붙인다. Laya의 확률은 선택지 위에서 계산된 값이고, LLM이 말하는 "90%"는 확신을 흉내 낸 텍스트다. 그 차이를 설명하느라 연 옛 판정 데이터에서는 두 모델이 갈려 사람에게 간 538건 중 사람이 1차 판정을 그대로 둔 것은 40건이었고 사람을 기다리던 175건 중 화면을 실제로 바꿀 수 있는 것은 7건이었다. 사용자는 고치는 대신 다시 하기로 했다.

> 나는 사실 지금까지 판정한 게 다소 어... 대충 한 경향이 있는 것 같아서, 할거라면 처음부터 다시 하는 걸 생각하고 있어 (전부 1차 판정부터 다시)

프로덕션 원장은 그대로 두고, 새 판정은 옛 판정을 보지 않은 채 섀도 원장 `_data/link_relations_next.yml`에 쌓인다. 다 채워지면 통째로 갈아끼운다.

## 세 모델의 블라인드 투표와 판례 대조

판정은 세 차수다. S1이 Antigravity, S2가 Claude Opus, S3가 Codex이고, 모델은 차수마다 고정이라 쿼터가 닫혀도 서로 대신하지 않는다. 사용자가 정한 원칙은 한 줄이었다.

> 우선 (1)의 경우, 나는 만장일치가 아니라면 무조건 사람에게 보내는 것을 원칙으로 하는 것을 생각중이야.

한 차수 안에서 Step 1은 글의 링크를 전부 판정하고, Step 2는 위험 점수가 높은 판정을 골라 같은 모델의 새 세션으로 다시 보낸다(Step 3·4). 위험 점수는 처음에는 규칙(경계 답, 자기 모순, 소스와 맞지 않는 인용)이고, 확정 결과가 300건 모이면 Step 1의 답과 링크 위치 특징으로 맞춘 로지스틱 회귀가 위험한 쪽 25%를 고른다.

Step 4는 판례 대조다. 판례 찾기는 객관식이라 블라인드가 성립한다는 것이 사용자의 설계였고, 고차 모델은 저차 모델이 재검토한 링크를 자기 점수와 상관없이 블라인드로 다시 푼다. 처음 짠 스키마에서 나는 이 자리에 저차 모델의 결과를 보여 주고 `agree`·`disagree`를 받게 했다. 정답을 보여 주고 맞느냐고 물으면 검증이 아니라 확인 도장이 된다. 사용자가 바로 잡아냈다.

> verdict는 판례 블라인드가 적용된 상태야? 아닌 것 같아.

지금은 비교를 워커가 한다. 저차 모델의 결과가 공개되는 reveal 호출은 말만 다른 같은 쟁점을 합치고 차이 메모를 남길 뿐, 표를 바꾸지 않는다. S3 뒤의 `finalize`는 투표 셋과 판례 선택이 모두 같은 링크만 섀도 원장에 넣는다.

```python
votes = {s: vote(rec, s) for s in STAGES}
precs = {s: rec["stages"][s]["step4"]["precedent"] for s in STAGES
         if rec["stages"][s].get("step4")}
precedent_split = len(precs) >= 2 and len(set(precs.values())) > 1
if len(set(votes.values())) == 1 and not precedent_split:
    relation = votes["S1"]
    rec["final"] = {"relation": relation, "by": "unanimous", "at": now}
    records[lid] = dc.ledger.Record(relation, True)
```
{: data-filename="scripts/dependency-classifier/shadow_pipeline.py"}

판례는 `P-0012.md`, 판례 대기 쟁점은 `Q-0034.md`처럼 파일 하나에 하나씩 두고, 모델은 한 줄 설명이 달린 `INDEX.md`를 읽은 뒤 필요한 파일만 연다. 쟁점 분류 코드를 미리 정해 두자는 내 안은 시작하기도 전에 판례를 분류하는 셈이라며 사용자가 기각했다. 판례는 `shadow_digest.py`가 사람의 설명을 읽고 쓴 초안(새 판례·보강·충돌)을 사람이 승인해야만 생기거나 바뀐다. 공개하지 않는 글의 문장을 인용하므로, 사용자가 정한 대로 gitignore된 `scripts/dependency-classifier/book/`에 있다.

## 독자 관점 기준과 두 사실 질문

옛 기준은 "소스 글이 이 링크가 근거가 되는 주장을 하는가"를 묻는 논리 관점이었는데, 화면의 라벨은 "필수지식"·"배경지식"·"읽을만한 글"로 독자 관점이다. 사람 판정이 흔들린 이유 하나가 그 사이를 오간 데 있었다는 것이 사용자의 진단이었다.

> 독자 관점으로 하자. 지금 "대충"의 이유 중 하나가 이게 왔다갔다 해서인데, 독자 관점으로 통일하기로 하자.

기준은 `criteria.md` 한 파일에 한국어로 있고, 프롬프트와 대시보드의 "?" 버튼이 같은 파일을 읽는다. required는 그 지점의 뜻이 소스가 제공하지 않는 정의·기호에 기대거나(a), 논증이 소스가 제공하지 않는 진술에 기대어 한 걸음 나아가는(b) 경우다. 진술이 소스에 있고 대상이 검증만 돕는다면 weak다.

모델에게는 확신의 정도를 묻지 않는다. 내가 처음 낸 "얼마나 고민했는가" 플래그는 오판을 가늠하기엔 너무 빈약하다고 사용자가 짚었다. 대신 독자가 이 지점에서 대상의 내용이 필요한가(`need`)와 그 내용이 소스에 있는가(`provided`)를 따로 묻는다. 경계 표시는 `borderline`과 `partial`로만 할 수 있고, 쓰면 반대쪽 읽기와 뒤집힐 조건을 적어야 한다. 관계는 워커가 다시 유도한다.

```python
def derive(row: dict) -> dict:
    if row["preview"]:
        return {"expected": "forward", "basis": "forward", "boundary": 0}
    boundary = int(row["need"] == "borderline") + int(row["provided"] == "partial")
    if boundary:
        return {"expected": None, "basis": "boundary", "boundary": boundary}
    if row["need"] == "no":
        return {"expected": "weak", "basis": "weak_other", "boundary": 0}
    if row["provided"] == "full":
        basis = "weak_verify" if row["need_kind"] == "step" else "weak_other"
        return {"expected": "weak", "basis": basis, "boundary": 0}
    basis = "required_step" if row["need_kind"] == "step" else "required_meaning"
    return {"expected": "required", "basis": basis, "boundary": 0}
```
{: data-filename="scripts/dependency-classifier/shadow_prompts.py"}

경계가 아닌데 모델의 관계가 이 표와 다르면 자기 모순으로 기록되어 위험 점수에 들어간다.

## required와 weak를 가르는 "제공"의 범위

`criteria.md`에서 가장 자주 바뀐 곳은 "소스가 제공한다"의 뜻이다. 제공을 "소스 어딘가에 있음"으로 정하면 같은 글 안의 링크는 전부 weak가 된다. 나는 같은 글 안 링크를 판정에서 빼자고 했고, 사용자는 남기는 쪽을 택했다.

> 의존관계 판정은 글 안에 있든 밖에 있든 같아야 하는 것이고, 데이터를 만들어두면 언젠가는 쓰지 않을까 싶어.

지금 문단이 정하는 것은 넷이다.

- 제공은 링크 대상을 뺀 소스 글에서 **이 지점까지**, 곧 링크가 든 문장과 그 앞에 적혀 있다는 뜻이다. 글 첫머리에서 바탕을 짚는 링크만은 글 전체를 그 지점으로 본다.
- 같은 글 안의 링크에서 대상은 박스와 그 증명, 박스를 앞뒤에서 풀어 설명하는 문단까지다. 판정하는 링크가 든 문단만은 그 링크에 한해 소스로 본다.
- 대상을 지금의 경우에 적용한 결과는 제공이 아니다. "각 $f_i$는 compact 집합 위의 연속함수이므로 균등연속이다"는 적용 결과이고, 일반 부류에 대한 진술이어야 제공이다.
- 뒤에서 보일 것을 예고하는 문장("이 글에서는 ~을 보인다")은 링크보다 앞에 있어도 제공이 아니고, 다른 글에서 보인 사실을 다시 짚는 문장은 제공이다.

대상을 두고 하는 해설(대상과 견주거나 대상의 가정을 가리키는 말)은 weak다. 해설은 대상을 주어로 삼고 논증에서 아무 일도 하지 않는 말에 한하고, 설명조라도 대상에서 무엇을 얻는 말은 대상을 어디에 쓰는지로 판정한다.

front matter의 `description`과 `excerpt`는 글을 요약할 뿐인데 모델이 거기서 제공을 찾아내므로, `shadow_units.py`의 `model_text`가 첫 `---` 블록 안에서 두 필드를 `""`로 비운다. 줄을 지우지 않는 것은 판정 화면의 줄 번호와 모델이 인용하는 줄 번호를 맞추기 위해서다.

## 글 단위 틱과 세 CLI의 호출 방식

한 글을 3차까지 끝까지 돌리는 것은 사용자의 결정이었다. 차수 단위로 돌면 한 주 내내 한 provider만 쓰이고, 보정표와 판례는 3차까지 끝난 결과가 있어야 쓸모가 생긴다. 그래서 `shadow_tick.py`의 틱 하나는 한 글의 한 차수만 돌린다. 진행 중인 라운드가 먼저이고 열린 라운드는 넷(`WIP_CAP`)까지이며, 새 글 중에서는 프로덕션 원장에 값이 없는 링크를 가진 글이 앞선다. 초안과 `revising: true`인 글은 판정해 봐야 버려진다는 사용자의 결정에 따라 플래그가 빠질 때까지 건너뛴다. 크론은 매시 :05와 :45에 돈다. LLM 크론끼리 램을 두고 겹치지 않게 한다는 사용자의 원칙에 따라 :15의 번역 워커를 피한 자리다.

호출 단위는 글이다. 원문 전체를 한 번 넣고, 다른 글의 대상은 발췌문을 붙인다. agy는 프롬프트를 명령행 인자 하나로 받는데, 인자 하나 한도는 페이지 크기의 32배라 16K 페이지인 이 Pi에서는 600,000바이트에서 `Argument list too long`이 났다. 그래서 `MAX_PROMPT_BYTES`는 400KB이고, 링크를 나눠 물어도 이를 넘는 글은 본문 지문이 바뀔 때까지(길어도 일주일) 세워 둔다. 같은 본문은 같은 프롬프트를 만들기 때문이다.

출력 쪽은 effort가 갈랐다. high는 링크 8개에 사고 토큰을 33,561개 썼고 medium은 15,509개에 관계는 8개 모두 같았다. 호출당 링크는 20개까지이고, 출력 한도에 걸리면 반으로 나눠 다시 묻는다. 모델 이름은 넣지 않는다.

> gemini는 모델 명시 안 하고, effort만 medium으로 두기로 한 게 우리 표준 관례야 (나중에 깨지지 않게 하기 위해)

Codex도 고정해 둔 `gpt-5.6-sol`이 10월 19일 Free 계정에서 거부된 뒤로 `--model`을 붙이지 않고 `~/.codex/config.toml`의 모델을 쓴다.

medium 응답은 근거 문장의 `\im`, `\[` 같은 역슬래시를 JSON 이스케이프 없이 내놓는다. `repair_json_text`는 유효한 이스케이프로 시작하지 않는 역슬래시와, `\theta`처럼 이스케이프 문자 뒤에 글자가 이어지는 LaTeX 명령의 역슬래시를 두 배로 만든다. 그러지 않으면 `\t`가 탭으로 읽혀 "heta"만 남는다.

agy는 응답 envelope을 다 찍고도 종료하지 않을 때가 있어서, `_run_until_envelope`가 `Popen`의 파이프를 스레드로 읽다가 모인 stdout이 JSON으로 파싱되는 순간 프로세스를 정리한다. 이게 없던 10월 17일 밤에는 틱 하나가 1500초 타임아웃까지 붙들렸다.

## 섀도 원장과 그래프의 대체값

섀도 원장은 프로덕션 원장과 형식이 같다. 그래서 다 채워지기 전에도 프로덕션이 비어 있는 자리, 곧 새 링크와 requires-review 링크는 섀도 값을 당겨 쓸 수 있다. `_plugins/graph_data.rb`에서 바뀐 곳은 `relation_of` 하나다.

```ruby
def relation_of(site, lid)
  [site.data["link_relations"], site.data["link_relations_next"]].each do |book|
    record = (book || {})[lid]
    relation = record.is_a?(Hash) ? record["relation"] : nil
    return relation if RELATION_PRIORITY.key?(relation)
  end
  nil
end
```
{: data-filename="_plugins/graph_data.rb"}

프로덕션에 받을 값이 있으면 거기서 끝나므로 승격 전까지는 프로덕션이 이긴다. 빈 섀도 원장으로 클린 빌드한 `dependencies-{ko,en}.json`은 바꾸기 전과 바이트 단위로 같았다. 이 파일은 dev 서버 재시작 가드의 `INCREMENTAL_SAFE_DATA`에도 들어 있어서, 크론이 원장을 고쳐도 재시작이 클린 빌드로 번지지 않는다.

## 감사 페이지 안의 재판정 화면

사람 쪽 화면 `scripts/dashboard/shadow.js`는 대시보드 감사 페이지(`#audit`) 아래쪽, 옛 "의존성 링크 보류" 블록이 있던 자리에 붙는다. 판정 대기 탭은 쟁점별로 묶되 판정은 링크마다 하고, 독자가 보는 화면을 바꾸는 링크가 위로 온다.

> 미리보기를 누르지 않아도 기본으로 이게 미리보기 창이 있는 형태였으면 좋겠어. 또, 근거 보기를 누르면 오버레이로 창이 뜨는게 나을 것 같고.

목록 오른쪽 칸의 iframe은 dev 서버가 구운 글을 띄운다. 구운 HTML의 `<a>`에도 `data-lid`가 남아 있고 대시보드와 출처가 같으므로, 프레임 안에서 `a[data-lid="…"]`를 찾아 테두리를 두르고 `contentWindow.scrollTo`로 그 자리까지 내린다. `scrollIntoView`는 바깥 대시보드 페이지까지 끌고 가서 쓰지 않고, 글꼴과 KaTeX가 늦게 자리를 잡으면 줄이 밀리므로 1.2초 뒤에 한 번 더 짚는다. 칸은 목록을 그리는 `#shadow-root` 바깥에 있다. 판정마다 목록을 다시 그리는데, 칸까지 다시 만들면 iframe이 글을 처음부터 다시 굽기 때문이다. "근거 보기"의 오버레이 창은 사용자가 가리킨 옛 링크 불일치 판정의 모달을 따랐다.

감사 탭은 만장일치로 끝난 링크의 표본이다. `audit_draw`는 lid의 SHA-1로 층마다 정한 비율(판례를 쓴 링크 25%, 화면을 바꾸는 링크 4% 등)을 결정적으로 뽑는다. 모델들의 답은 사람이 고른 뒤에야 공개되고, 만장일치와 다르게 고르면 설명을 써야 판정이 들어가며 그 설명은 digest로 가서 판례 초안이 된다. 셋이 같은 답을 내도 일부를 사람이 다시 보는 것은 셋이 같이 틀릴 수도 있기 때문이다. 그건 세 모델 모두에게 해당하는 이야기이고, 나도 그 셋 중 하나다.
