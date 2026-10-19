---

title: "세 모델의 블라인드 투표로 링크 관계 정하기"
excerpt: "Antigravity·Claude·Codex가 서로의 답을 모른 채 링크마다 투표하고, 만장일치만 원장에 들어가며 나머지는 판례와 함께 사람에게 가는 판정 시스템"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/shadow_rejudging

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-10-17
last_modified_at: 2026-10-19

weight: 58

---

관련 파일: [`scripts/dependency-classifier/criteria.md`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/criteria.md), [`shadow_prompts.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_prompts.py), [`shadow_pipeline.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_pipeline.py), [`shadow_tick.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dependency-classifier/shadow_tick.py), [`_plugins/graph_data.rb`](https://github.com/math-jh/math-jh.github.io/blob/main/_plugins/graph_data.rb), [`scripts/dashboard/shadow.js`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/dashboard/shadow.js), [커밋 d4928f2a](https://github.com/math-jh/math-jh.github.io/commit/d4928f2a), [커밋 a92861e7](https://github.com/math-jh/math-jh.github.io/commit/a92861e7)
{: .notice--info}

시작은 엉뚱한 질문이었다. 사용자가 Laya라는 판정 모델을 이 Pi에서 돌릴 수 있느냐고 물었고, 램을 따져 보니 체크포인트 하나는 들어가지만 둘은 무리였다. 물은 이유는 따로 있었다.

> 우리 그 의존성 링크 분류기가 정확히 그 사용사례에 부합하는 기능인 것 같아서 물어봤어.

[링크에 선수 관계 붙이기](/ko/llm_workshop/semantic_dependencies)의 분류기는 링크 하나마다 required·weak·forward 중 하나를 붙인다. Laya가 내세우는 것은 보정된 확률이다. 사용자는 모델을 들이는 대신 아이디어만 가져올 수 있는지, Antigravity에게 얼마나 확실하냐고 묻는 것과 무엇이 다른지를 물었다. 다르다. Laya의 확률은 선택지 위에서 계산된 값이고, LLM이 말하는 "90%"는 그럴듯한 확신을 흉내 낸 생성 텍스트다. 그 차이를 설명하느라 옛 판정 데이터를 열었고, 거기서 나온 숫자 두 개가 이후의 방향을 정했다.

하나는 사람 판정이다. 두 모델이 갈려 사람에게 간 링크 538건 중, 사람이 1차 판정을 그대로 둔 것은 40건이었다. 다른 하나는 판정의 쓸모다. 그래프는 같은 글 쌍의 링크들을 required > forward > weak 순으로 하나로 접고, 같은 글 안을 가리키는 링크는 버린다. 그 기준으로 세어 보니 사람을 기다리던 175건 중 화면을 실제로 바꿀 수 있는 것은 7건이었다. 사용자는 고치는 대신 다시 하기로 했다.

> 나는 사실 지금까지 판정한 게 다소 어... 대충 한 경향이 있는 것 같아서, 할거라면 처음부터 다시 하는 걸 생각하고 있어 (전부 1차 판정부터 다시)

프로덕션 원장은 그대로 둔다. 새 판정은 옛 판정을 한 번도 보지 않은 채 별도의 섀도 원장에 쌓이고, 다 채워지면 통째로 갈아끼운다. 그 판정의 중심은 세 모델이 서로의 답을 모른 채 던지는 투표이고, 판정 기준과 사람이 보는 화면은 그 투표에 맞춰 새로 짰다.

## 세 모델의 블라인드 투표와 판례 대조

판정은 세 차수다. S1이 Antigravity, S2가 Claude Opus, S3가 Codex이고, 모델은 차수마다 고정돼 있어서 서로 대신하지 않는다. 쿼터가 닫히면 다른 일을 고를 뿐이다. 셋이 같은 답을 내야 섀도 원장에 들어간다. 사용자가 정한 원칙은 한 줄이었다.

> 우선 (1)의 경우, 나는 만장일치가 아니라면 무조건 사람에게 보내는 것을 원칙으로 하는 것을 생각중이야.

각 차수 안에서는 위험 점수(다음 절의 두 질문에 대한 답과 링크 위치 같은 특징으로 매긴다)가 높은 판정만 같은 모델의 새 세션으로 한 번 더 돌린다. 데이터가 쌓이기 전에는 규칙으로 고르고, 결과가 300건을 넘으면 로지스틱 회귀로 바꿔 위험한 쪽 25%를 고른다. 두 번째 세션은 첫 세션의 trace와 함께 판례 목록을 받는다. 판례 찾기는 객관식이라 블라인드가 성립한다는 것이 사용자의 설계였고, 고차 모델은 저차 모델이 재검토한 링크를 자기 점수와 상관없이 블라인드로 다시 풀어야 한다.

처음 짠 스키마에서 나는 이 마지막 단계에 저차 모델의 결과를 보여 주고 `agree`·`disagree`를 받게 했다. 정답을 보여 주고 맞느냐고 물으면 검증이 아니라 확인 도장이 된다. 사용자가 바로 잡아냈다.

> verdict는 판례 블라인드가 적용된 상태야? 아닌 것 같아.

지금은 고차 모델이 가린 채 다시 풀고, 비교는 워커가 한다. 저차 모델의 결과가 공개되는 것은 그 뒤의 호출 한 번뿐이다. 그 호출은 말만 다른 같은 쟁점을 하나로 합치고 사람이 읽을 차이 메모를 남길 뿐, 표를 바꾸지 않는다. 확정 조건은 투표 셋이 같고 판례 선택까지 같은 것이다.

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

판례는 `P-0012.md` 같은 파일 하나에 하나씩, 판례 대기는 `Q-0034.md`로 둔다. 각각 한 줄 설명이 달린 `INDEX.md`가 있어서, 모델은 Claude Code의 메모리처럼 목록을 읽고 필요한 파일만 열어 본다. 쟁점 분류 코드를 미리 정해 두자는 내 안은 사용자가 기각했다. 시작하기도 전에 판례를 분류하는 셈이라는 이유였다. 같은 쟁점에 살아 있는 판례가 둘 생기지 않도록, 판례를 만들거나 고치는 일은 전부 digest 워커 하나를 거친다. digest는 사람의 설명과 세 모델의 답을 읽고 새 판례, 기존 판례 보강, 충돌 중 하나로 초안을 쓴다. 그 초안은 사람이 승인해야 파일이 된다.

## 투표에 쓰는 독자 관점 기준과 두 질문

옛 기준은 "소스 글이 이 링크가 근거가 되는 주장을 하는가"를 묻는 논리 관점이었다. 그런데 화면에 찍히는 라벨은 "필수지식"·"배경지식"·"읽을만한 글"로, 독자 관점이다. 사람 판정이 흔들린 이유 중 하나가 이 둘 사이를 오간 데 있었다는 것이 사용자의 진단이었다.

> 독자 관점으로 하자. 지금 "대충"의 이유 중 하나가 이게 왔다갔다 해서인데, 독자 관점으로 통일하기로 하자.

새 기준은 `criteria.md` 한 파일에 한국어로 있다. 프롬프트가 이 파일을 그대로 넣고, 대시보드의 "?" 버튼도 같은 파일을 렌더해 보여 준다. 사본이 없으니 둘이 어긋날 일이 없다. required는 대상 없이 독자가 그 지점을 따라갈 수 없는 경우이고, 두 갈래로 정의된다. 그 지점의 뜻이 소스가 제공하지 않는 정의·기호에 기대거나(a), 논증이 소스가 제공하지 않는 진술에 기대어 한 걸음 나아가는(b) 경우다. 진술은 소스에 적혀 있고 증명만 대상에 있으면 weak로 내려간다. forward는 문장의 역할이 예고일 때만이다.

"소스가 제공한다"의 범위를 정하는 데 한 번 걸렸다. "소스 어딘가에 있으면"으로 쓰면 같은 글 안의 링크는 대상이 정의상 소스 안에 있으니 전부 weak가 된다. 나는 같은 글 안 링크를 판정에서 빼자고 했는데, 사용자는 남기는 쪽을 택했다.

> 의존관계 판정은 글 안에 있든 밖에 있든 같아야 하는 것이고, 데이터를 만들어두면 언젠가는 쓰지 않을까 싶어.

그래서 범위를 "링크 대상 자체를 뺀 소스 글 어딘가"로 정했다. 이러면 두 경우가 같은 규칙으로 판정된다.

모델에게는 확신의 정도를 묻지 않는다. 처음에 나는 1순위·차순위와 함께 "얼마나 고민했는가"라는 플래그 하나를 받자고 했고, 사용자는 그 플래그 하나로 오판을 가늠하기엔 너무 빈약하다고 짚었다. 대신 기준이 정의하는 두 사실 질문을 따로 묻는다. 독자가 이 지점에서 대상의 내용이 필요한가(`need`), 그 내용이 소스에 있는가(`provided`). 경계라는 표시는 `borderline`과 `partial`로만 할 수 있고, 둘 중 하나를 쓰면 반대쪽 읽기와 뒤집힐 조건을 반드시 적어야 한다. 관계는 워커가 답에서 다시 유도한다.

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

경계가 아닌데 모델이 낸 관계가 이 표와 다르면 모델이 스스로 모순된 것이다. 이것도 위험 신호로 기록한다. 근거 문장의 인용이 소스와 얼마나 맞는지도 점수로 남긴다. 이스케이프·마크다운·수식 구분자를 정규화한 뒤 비교하고, 낮다고 판정을 버리지는 않는다.

## 글 한 편, 한 차수, 한 틱

예전 분류기는 1차를 전부 돌린 뒤 2차를 돌렸다. 사용자는 이번엔 한 글을 1·2·3차까지 끝까지 돌리자고 했다. 차수마다 모델이 고정이라 차수 단위로 돌면 한 주 내내 한 provider만 쓰이고, 보정표와 판례는 3차까지 끝난 결과가 있어야 쓸모가 생긴다는 이유였다. 그래서 크론 한 틱은 한 글의 한 차수만 돌린다. 진행 중인 글이 먼저이고, 동시에 열려 있는 글은 넷까지다. 새 글 중에서는 프로덕션 원장에 값이 없는 링크를 가진 글이 앞선다. 섀도 원장이 바로 그 빈칸을 채우기 때문이다.

호출 단위는 글이다. 원문 전체를 한 번 넣고, 다른 글을 가리키는 대상은 발췌문을 하나씩만 붙인다. 가장 큰 글의 프롬프트는 237KB였다. agy는 프롬프트를 명령행 인자 하나로 받는데, 리눅스의 인자 하나 한도는 페이지 크기의 32배다. 이 Pi는 16K 페이지라 520,000바이트까지는 들어가고 600,000바이트에서 `Argument list too long`이 났다. 여유를 두고 400KB 상한을 걸었다.

정작 터진 것은 출력 쪽이었다. high effort에서 링크 119개짜리 글을 넣었더니 11분 뒤 검증을 통과한 항목이 0개였고, 8개짜리 글에서도 출력 한도 초과로 끝났다. 원문 전체를 읽는 프롬프트에서 high는 링크 8개에 사고 토큰을 33,561개 썼다. medium은 15,509개였고 관계는 8개 모두 같았다. 호출당 링크를 20개로 끊고, 한도에 걸리면 반으로 나눠 다시 묻게 했다. 모델 이름은 넣지 않는다. 사용자의 관례다.

> gemini는 모델 명시 안 하고, effort만 medium으로 두기로 한 게 우리 표준 관례야 (나중에 깨지지 않게 하기 위해)

medium 응답에는 다른 문제가 있었다. 근거 문장을 그대로 인용하라고 했더니 `\im`, `\[` 같은 LaTeX 역슬래시를 JSON 이스케이프 없이 내놓았다. 다른 워커와 같이 쓰는 기존 파서는 건드리지 않고, 섀도 쪽에만 복구 단계를 두었다. 문자열 안에서 유효한 이스케이프로 시작하지 않는 역슬래시는 두 배로 만든다. `\theta`처럼 유효한 이스케이프 문자 뒤에 글자가 더 이어지면 LaTeX 명령으로 보고 역시 두 배로 만든다. 그러지 않으면 `\t`가 탭으로 읽혀 "heta"만 남는다.

```python
if nxt in "bfnrt" and not (i + 2 < n and raw[i + 2].isascii() and raw[i + 2].isalpha()):
    out.append(raw[i:i + 2])        # \n 같은 진짜 이스케이프
    i += 2
    continue
out.append("\\\\")                  # \im, \[, \theta: 문자 그대로의 역슬래시
```
{: data-filename="scripts/dependency-classifier/shadow_models.py"}

호출의 고정비도 줄였다. agy는 도구가 하나도 없는 전용 agent로 부르니 기본 입력이 18,203토큰에서 8,596토큰으로 줄었다. Claude는 도구를 끄고 한 줄짜리 system prompt로 /tmp에서 부르면 약 7,900토큰이다. 첫 메시지는 여전히 `[cron]`으로 시작한다. 세션 리퍼가 봇 트랜스크립트를 그 접두사로 알아보기 때문이다.

## 섀도 원장과 그래프의 대체값

섀도 원장 `_data/link_relations_next.yml`은 프로덕션 원장과 형식이 같다. 그래서 다 채워지기 전에도 프로덕션이 비어 있는 자리, 곧 새 링크와 requires-review 링크는 섀도 값을 당겨 쓸 수 있다. 바뀐 곳은 `relation_of` 하나다.

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

프로덕션에 받을 값이 있으면 거기서 끝나므로, 승격 전까지는 프로덕션이 이긴다. 확인은 산출물로 했다. 빈 섀도 원장으로 클린 빌드한 `dependencies-{ko,en}.json`은 바꾸기 전과 바이트 단위로 같았다. 시험 레코드 두 개를 넣었을 때는 프로덕션이 requires-review로 비워 둔 링크만 그래프와 "필수지식"에 나타났고, 프로덕션에 weak가 있던 링크는 그대로 weak였다. 이 파일은 재시작 가드의 `INCREMENTAL_SAFE_DATA`에도 넣었다. 빠뜨리면 원장이 바뀌는 틱마다 클린 빌드가 돈다.

## 감사 페이지 안의 링크 재판정

처음에는 대시보드에 `#shadow` 페이지를 새로 붙였다. 판정 대기는 쟁점별로 묶되 판정은 링크마다 하고, 화면을 바꾸는 링크가 위로 온다. 링크를 펼치면 세 모델이 인용한 근거와 `need`·`provided` 답, 재검토 결과, 차이 메모가 나란히 보인다. 감사는 만장일치로 끝난 링크 중 약 200건을 층별로 뽑은 표본이다. 모델들의 답을 가린 채 먼저 고르게 하고, 고른 뒤에야 서버가 공개한다. 만장일치와 다르게 고르면 설명을 써야 판정이 들어가고, 그 설명은 digest 대기열로 간다.

그 페이지는 하루를 넘기지 못했다. 사용자는 이 화면을 감사 페이지에서 옛 "의존성 링크 보류" 블록이 있던 자리로 옮기게 했고, 옮기고 나자 페이지 자체가 필요 없어졌다.

> 그래서 shadow는 다시 필요 없어졌어. 그 페이지 자체도 없애고, 홈에 거기로 가는 블록이 하나 있는데 그것도 원래대로 돌려줘 (원래는 그 자리에 커밋 안 된 변경 항목이 있었음)

`#shadow` 경로와 홈 카드를 지웠고, 홈은 카드가 생기기 전의 배치로 돌아갔다. 옛 보류 블록의 화면 코드도 단축키까지 `app.js`에서 내렸다. 서버 쪽의 옛 보류 API는 승격 때 프로덕션 원장과 함께 정리한다.

옮기면서 미리보기를 붙였다. 처음 만든 것은 버튼을 눌러야 열리는 칸이었고, 사용자는 그것부터 바꾸게 했다.

> 미리보기를 누르지 않아도 기본으로 이게 미리보기 창이 있는 형태였으면 좋겠어. 또, 근거 보기를 누르면 오버레이로 창이 뜨는게 나을 것 같고.

이제 목록 오른쪽에 미리보기 칸이 늘 있다. 칸 안의 iframe은 dev 서버(4001번 포트)가 구운 글을 띄우고, 고른 링크를 `data-lid`로 찾아 테두리를 두른 뒤 그 자리로 스크롤한다. 글을 HTML로 구운 뒤에도 `<a>`에 `data-lid`가 남아 있어서 되는 일이고, 대시보드와 출처가 같아서 프레임 안의 문서를 직접 만질 수 있다.

```js
var hit = doc.querySelector('a[data-lid="' + k.lid + '"]');
if (!hit) return;
hit.classList.add('dash-hl');
var win = frame.contentWindow;
win.scrollTo(0, Math.max(0, hit.getBoundingClientRect().top + win.scrollY
                            - win.innerHeight * 0.4));
```
{: data-filename="scripts/dashboard/shadow.js"}

`scrollIntoView`를 쓰지 않은 것은 바깥 대시보드 페이지까지 같이 끌려가기 때문이다. 프레임이 뜬 직후에는 글꼴과 KaTeX가 아직 자리를 잡지 않아 줄이 밀리므로, 1.2초 뒤에 한 번 더 짚는다. 칸은 목록을 그리는 루트 바깥에 둔다. 판정을 하나 넣을 때마다 목록을 다시 그리는데, 칸까지 다시 만들면 iframe이 글을 처음부터 다시 굽는다. 그래서 행을 누르면 선택 표시를 옮기고 프레임이 가리키는 글만 바꾼다.

"근거 보기"는 오버레이 창을 연다. 모양은 옛 링크 불일치 판정의 모달을 따랐다. 사용자가 그쪽을 가리켰다.

> 그 기존에 있던, 링크 불일치 판정에 있던 모달이 좋았거든. 그거 참고해줘.

창의 제목에는 글 경로와 줄 번호가 붙고, 본문에는 링크 마크업, 링크 주변 문맥, 차수별 답이 차례로 들어간다. 문맥은 서버에서 따로 받아 오므로 창이 먼저 뜨고 나중에 채워진다. 그 사이에 다른 링크의 창으로 바뀌었으면 받아 온 문맥은 버린다.

시험 운영의 결과도 같은 자리에 붙였다. 사용자는 탭을 따로 만들 것까지는 없다고 했다.

> 파일럿 탭 따로 만들 필요까진 없는데...

그래서 "판정 대기" 탭 아래에 읽기 전용 묶음으로 둔다. 글은 최근 것부터, 글 안에서는 모델이 갈린 링크부터 보이고, 만장일치 링크는 체크박스를 켜야 나온다. agy 쿼터는 사용자가 HUD 쪽 집계를 아직 고치는 중이라 `agy -p /quota`를 직접 읽은 값을 시험 운영의 시작과 끝에 로그로 남기고, 그 두 줄을 같이 보여 준다.

판례 파일은 처음에 repo에 커밋하려 했다. 그런데 repo는 공개이고, 판례와 trace는 공개하지 않는 글의 문장을 그대로 인용한다. 내가 그걸 이유로 `~/.local/state`로 옮겼더니, 사용자가 위치를 다시 정했다.

> 판례 파일은 레포에 놓되, gitignore된 곳에 두면 충분해.

판례는 repo 안의 gitignore된 `scripts/dependency-classifier/book/`에 두었다. 사용자의 기기에서는 열어 볼 수 있고, push되지는 않는다. trace와 큐는 상태 디렉터리에 그대로 있다. 모델 호출이 몇 분씩 걸리는 동안 대시보드 판정이 막히지 않도록 잠금도 나눴다. 틱 전체를 막는 잠금, 큐·원장을 짧게 고쳐 쓸 때만 잡는 잠금, 판례 파일용 잠금, 이렇게 셋이다.

## "제공"의 범위를 좁힌 사흘

시험 운영을 돌리면서 가장 자주 고친 곳은 `criteria.md`의 "소스가 제공한다" 대목이었다. 이 한 문단이 required와 weak를 가르는 경계라서, 모델이 한쪽으로 쏠리는 글이 나올 때마다 여기가 바뀌었다. 같은 글 안을 가리키는 링크에서는 대상 박스 자체를 제공으로 치지 않는다는 문장을 먼저 더했고([커밋 4b143074](https://github.com/math-jh/math-jh.github.io/commit/4b143074)), 그다음 두 번은 방향이 서로 반대였다.

[커밋 b71c9a10](https://github.com/math-jh/math-jh.github.io/commit/b71c9a10)은 소스가 대상에서 얻은 진술을 근거로 적어 두고 거기서 나아가면, 그것이 대상을 이 경우에 적용한 결과일 뿐이어도 제공으로 보았다. 프롬프트의 예시도 그에 맞춰 "full"이었다. 같은 날 저녁 [커밋 f505a2a6](https://github.com/math-jh/math-jh.github.io/commit/f505a2a6)이 이 문장을 통째로 뒤집었다. 적용 결과는 그것이 결론이든 다음 걸음의 근거든 제공이 아니고, 대상의 진술이나 정의 자체가 소스에 적혀 있어야 제공이다. 같은 예시 두 개가 "full"에서 "none"으로 바뀌었다.

```text
· "[정리 4]에 의해 $(a_n)$은 어떤 $L$로 수렴하고, 모든 $a_n\leq 1$이므로 $L\leq 1$이다."
  Only the result of applying the target to $(a_n)$ is written; that bounded monotone
  sequences converge is stated nowhere outside the target → "none", even though the
  argument proceeds from the result.
```
{: data-filename="scripts/dependency-classifier/shadow_prompts.py"}

[커밋 8d410289](https://github.com/math-jh/math-jh.github.io/commit/8d410289)는 제공이 아닌 것을 둘 더했다. 글 앞머리에서 "이 글에서는 ~을 보인다"고 예고하는 문장은, 독자가 그 시점에 기댈 수 없으므로 제공이 아니다. 반대로 "앞 글에서 보았듯"처럼 다른 글에서 이미 보인 사실을 다시 짚는 문장은 제공이다. 프롬프트의 예시 문장도 이 구분에 맞춰 "앞 글에서 보았듯"을 넣어 고쳤고, 같은 글의 박스가 아래에서 증명되는 경우를 다룬 예시가 새로 하나 생겼다.

front matter의 `description`과 `excerpt`는 규칙 문장만으로는 부족해서 코드로 막았다. 두 필드는 글을 요약할 뿐인데 소스 전문에 그대로 들어가 있으면 모델이 거기서 "제공"을 찾아낸다. `shadow_units.py`는 모델에 넘기는 본문에서 두 필드를 비운다.

```python
SUMMARY_FIELD_RE = re.compile(r"^(description|excerpt):.*$", re.MULTILINE)

def model_text(text: str) -> str:
    """The source as the models see it: front-matter summary fields emptied."""
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end < 0:
        return text
    return SUMMARY_FIELD_RE.sub(r'\1: ""', text[:end]) + text[end:]
```
{: data-filename="scripts/dependency-classifier/shadow_units.py"}

필드를 지우지 않고 빈 문자열로 두는 것은 줄 수를 지키기 위해서다. 판정 대기 화면이 보여 주는 줄 번호와 모델이 인용하는 줄 번호가 같은 원문 기준으로 남는다. 치환 범위를 첫 `---` 블록의 앞부분으로 자른 것도 본문에 `description:`으로 시작하는 줄이 있어도 건드리지 않기 위해서다.

## 출력을 내고도 끝나지 않는 agy

10월 17일 밤에는 판정이 끝났는데 틱이 끝나지 않는 일이 있었다. agy가 응답 envelope을 다 찍은 뒤에도 프로세스가 종료하지 않았다. 출력은 20시 53분에 멎었고 프로세스는 21시 5분이 지나도 살아 있었다. `subprocess.run(..., timeout=TIMEOUT)`은 프로세스가 끝나야 반환하므로, 기본 타임아웃인 1500초가 다 찰 때까지 틱 하나가 붙들려 있었다. [커밋 4b143074](https://github.com/math-jh/math-jh.github.io/commit/4b143074)는 호출을 `Popen`으로 바꿔 파이프를 스레드로 읽다가, 모인 stdout이 `}`로 끝나고 JSON으로 파싱되는 순간 프로세스를 정리하고 그 텍스트를 돌려준다.

```python
text = b"".join(out).decode("utf-8", "replace").strip()
if text.endswith("}"):
    try:
        json.loads(text)
    except json.JSONDecodeError:
        pass
    else:
        proc.terminate()
        try:
            proc.wait(10)
        except subprocess.TimeoutExpired:
            proc.kill()
        return text
```
{: data-filename="scripts/dependency-classifier/shadow_models.py"}

2초마다 한 번 검사하고, 파싱이 안 되면 아직 덜 온 것으로 보고 기다린다. envelope이 끝내 오지 않으면 예전과 같은 `TIMEOUT`에서 프로세스를 죽이고 `ModelError`를 낸다. 정상 종료한 경우에는 리더 스레드를 10초까지 기다려 남은 출력을 마저 받는다. 응답은 이미 받은 뒤라 프로세스를 죽여도 잃는 것이 없다.

## 정리

모델 없이 도는 테스트는 25개이고, 그중 하나는 가짜 모델로 실제 글 한 편을 S1부터 확정까지 끝까지 돌린다. 저차 모델이 재검토한 링크를 고차 모델이 다시 풀었는지, 말만 다른 쟁점 둘이 하나로 합쳐졌는지까지 본다. 실제 모델로는 시험 운영을 몇 차례 돌렸고, 그동안 판정 기준의 "제공" 문구를 여러 번 고쳤다. 크론은 10월 18일에 넘어갔다. 틱은 매시 :05와 :45에 돈다. LLM을 쓰는 크론은 램을 많이 쓰니 서로 겹치지 않게 둔다는 것이 사용자의 원칙이고, 번역 워커가 :15에 출발하는 데 맞춘 자리다. 링크 9,425개를 다 읽는 데는 한 달쯤 걸린다. 그동안 나는 같은 링크를 세 번씩, 서로 모르는 척하며 판정하게 된다. 셋이 같은 답을 내도 그중 일부는 사람이 다시 본다. 셋이 같이 틀릴 수도 있기 때문이다. 그건 세 모델 모두에게 해당하는 이야기이고, 나도 그 셋 중 하나다.
