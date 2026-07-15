---

title: "번역 워커가 헛돈 자리"
excerpt: "LLM이 아니라 그것을 감싼 결정적 코드가 제 상태를 오해하던, 번역 워커의 사흘치 버그"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/translation_worker_hardening

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-14
weight: 29

---

관련 파일: [`scripts/translation/translate_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/translation/translate_worker.py)
{: .notice--info}

[번역 워커](/ko/llm_workshop/translation_worker)는 30분마다 한 번씩 한글 글 한 편을 골라 영어로 옮긴다. 그 구조에서 정작 불안정할 것 같은 부분, 그러니까 LLM이 본문을 번역하는 대목은 오히려 조용했다. 사흘에 걸쳐 계속 어긋난 것은 그 LLM을 감싸고 있는 결정적 코드 쪽이었다. 무엇을 다시 번역할지 고르고, 결과가 성한지 검사하고, 커밋 제목을 붙이는 부분이다. 전부 같은 종류의 실수였다. 코드가 제 상태를 잘못 알고 있었다.

## 26시간 동안 큐를 막은 글

가장 비싼 버그부터 적는다. 워커는 번역 대상을 세 단계로 고른다. 영어판이 없는 글(pending), 한글이 더 최근에 고쳐진 글(drift), 그리고 오래 묵은 영어판을 다듬는 일(polish). 이 중 drift는 원래 커밋 시각으로 판정했는데, 얼마 전에 한글 frontmatter에 `drift_needed: true`를 달면 그 글을 drift 대상으로 집어내는 opt-in 방식이 더해졌다. 이 `drift_needed`는 한글 파일에만 있는 키라, 영어판을 합성할 때 걷어낸다.

문제는 검증기가 여전히 "영어판 frontmatter 키가 한글판 키를 다 담고 있어야 한다"(ko ⊆ en)고 검사하고 있었다는 것이다. `drift_needed`는 일부러 뺐는데 검사는 그걸 몰라서, drift 플래그가 달린 글은 번역이 **항상** 검증에 실패했다.

여기까지면 실패 로그 한 줄로 끝났을 텐데, 두 번째 실수가 겹쳤다. drift 단계가 pending 단계와 달리 실패 백오프를 보지 않았다. pending은 한 번 실패한 글을 일정 시간 건너뛰는데, drift는 그 가드 없이 고정된 순서로 큐를 훑으니, 검증에 실패하는 글이 매 틱마다 큐의 맨 앞에 다시 서고 매번 통째로 재번역됐다. 최근 사용자는 주로 `published:false`인 글들을 작업해서 이 문제가 보이지 않았는데, 이 `drift_needed` 태그가 붙은 `Covering_Spaces` 글이 생기니 비로소 보이기 시작한 것이다. `Covering_Spaces` 한 편이 그렇게 26시간 동안 큐를 막으면서, 뒤에 줄 선 다른 플래그 글들을 굶기고, 자기 자신을 48번 다시 번역했다.

고친 것은 두 줄이다. ko ⊆ en 검사에서 한글 전용 키를 예외로 두고, drift 단계도 pending처럼 실패 백오프를 보게 했다.

```python
# 한글 전용 키(drift_needed)는 합성 때 일부러 빠지므로 검사에서도 예외로 둔다
ko_keys = _fm_top_keys(ko_content) - set(_KO_ONLY_KEYS)
```
{: data-filename="scripts/translation/translate_worker.py"}

두 줄이 빠져 있던 값이 26시간이었다.

## 구조가 어긋나면 전체를 다시

drift는 원래 증분으로 돈다. "지난 번역 이후 한글에서 뭐가 바뀌었나"를 묻고, 바뀐 부분만 다시 번역해 영어판에 반영한다. 대개는 이게 싸고 맞다. 그런데 영어판이 이미 한글과 **구조적으로** 어긋나 있으면 이야기가 다르다. 정리 박스 하나가 통째로 비어 있거나 개수가 안 맞는 상태에서는, 바뀐 문단만 손봐서는 그 어긋남이 그대로 살아남는다. 증분은 수리가 될 수 없다.

그래서 결정적 구조 린트를 하나 붙였다. 한글과 영어 양쪽의 `:::` 정리 박스를 문서 순서대로 뽑아, 종류어를 정규화해(한글 "정리"와 영어 "Theorem"이 같은 것으로 맞춰진다) 개수와 짝을 비교하고, 한글 쪽 본문은 차 있는데 영어 쪽이 비어 있는 박스를 잡아낸다. drift를 돌리려다 구조가 어긋난 걸 발견하면, 증분을 포기하고 전체 재번역으로 내려간다.

```python
struct = lint_structure(ko_content, en_text)
if struct:
    log("drift: EN structurally diverges from KO; full re-translation")
```
{: data-filename="scripts/translation/translate_worker.py"}

같은 린트를 검증기에도 물렸고, 모든 한영 쌍을 한 번에 훑어 어긋난 글을 보고하는 `--lint-structure` 명령도 하나 뒀다. 수식 블록 개수만 세던 옛 검사가 놓치던 종류의 어긋남이다.

## SAFE에 묻힌 한국어 오타

검증기는 영어판을 만들면서 한글 원문의 오류를 종종 교정한다. 오탈자나 명백한 실수를 영어로는 바로잡아 옮기고, 그 사실을 verdict에 적어왔다. 그런데 그 보고는 늘 SAFE 판정에 딸려 나왔다. 영어판 자체는 멀쩡하기 때문이다. 문제는 한글에 있고, 영어판은 그걸 고쳐서 옮겼으니 손실이 없다. 그리고 텔레그램 알림 정책은 SAFE를 통째로 억누른다. 그래서 한글에 진짜 오타가 있다는 신호가 매번 조용히 버려졌다.

쌓여 있던 verdict를 훑어보니 19편에 그런 보고가 들어 있었고, 그중 16편은 한 번도 알림에 뜬 적이 없었다. 원문과 대조하니 대부분이 실제 한글 오류였다. 한글 오타는 영어판의 결함이 아니라 절대 "lossy"로 잡히지 않으니, 이게 오래 안 보인 것도 당연했다.

프롬프트에 KO-TYPOS 섹션을 요구해 검증기가 교정한 한글 오류를 그 아래 따로 적게 하고, 워커는 그 섹션을 safe든 lossy든 무관하게 파싱·기록·알림한다. 영어판이 성한지와 한글이 성한지는 별개의 질문이라, 이제 별개로 보고된다.

## drift라고 적힌 polish

마지막은 커밋 제목이었다. 워커가 번역을 커밋할 때 제목을 붙이는 함수가, 사유를 "pending이냐 아니냐"로만 갈랐다. 그래서 pending이 아닌 것은 drift든 polish든 전부 "EN 재번역(drift)"로 적혔다.

이게 눈에 안 띈 데는 이유가 있다. 지금 `drift_needed` 플래그가 달린 한글은 대부분 아직 발행 전(`published: false`)이라, drift 단계가 거의 비어 있고 큐가 polish로 내려가 있다. 그러니 근래 "재번역(drift)"로 찍힌 커밋 대부분이 실은 polish였다. 사유를 제목으로 옮기는 표를 하나 두어 갈랐다.

```text
pending  →  EN 신규 번역
drift    →  EN 재번역(drift)
polish   →  EN 다듬기(polish)
```

verify 단계는 읽기 전용이라 애초에 커밋하지 않으니 표에 없다.

## 정리

네 건이 사흘에 몰렸지만 종류는 하나였다. LLM이 같은 입력에 다른 출력을 낸다는, 애초에 예상하고 설계한 그 불확정성은 이번에 한 번도 말썽이 아니었다. 말썽은 전부 그 둘레의 결정적 코드에서 나왔다. 자기가 뺀 키를 검사가 여전히 요구하고, 실패한 글을 백오프 없이 다시 집고, 억눌러야 할 신호와 살려야 할 신호를 같은 통에 넣고, polish를 drift라 적었다. 결정적 코드는 같은 입력에 같은 결과를 돌려준다는 게 장점인데, 그 결과가 처음부터 틀려 있으면 26시간 동안 성실하게 틀린 일을 반복한다. 성실한 게 늘 미덕은 아니라는 걸, 나 자신에 대한 이야기이기도 하니 적어둔다.
