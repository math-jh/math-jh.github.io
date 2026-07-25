---

title: "한영 병기 파이프라인"
excerpt: "정의 박스의 무병기 이탤릭 수백 개를 색인으로 회수하는 백필과 상시 단계, 그리고 동음이의를 막는 게이트"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/gloss_pipeline

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-21
last_modified_at: 2026-07-26
weight: 34

---

관련 파일: [`scripts/term-extraction/gloss_backfill.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/gloss_backfill.py), [`scripts/term-extraction/gloss_stage.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/gloss_stage.py), [`scripts/term-extraction/gloss_skip.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/gloss_skip.yml), [`scripts/term-extraction/term_extract_worker.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/term_extract_worker.py)
{: .notice--info}

이 블로그의 정의 박스에는 규칙이 하나 있다. 이탤릭으로 정의되는 용어는 `*english<sub>한국어</sub>*` 꼴의 한영 병기로 적는다. 문제는 이 규칙보다 오래된 글이 많다는 것이다. 옛 글의 정의 박스에는 병기 없는 영어 이탤릭이 수백 개 흩어져 있었고, 이것은 표기의 문제로 끝나지 않는다. [용어 영어화 스윕](/ko/llm_workshop/term_sweep) 때 새로 세운 추출 워커의 1단계는 `<sub>` 쌍 마커만 정의로 인식하므로, 무병기 정의어는 찾아보기 색인에서 통째로 빠진다. 사용자가 이 격차를 메우라는 방향을 정했고, 일은 둘로 나뉘었다. 일회성 소급 백필(`gloss_backfill.py`)과, 추출 워커에 상주하는 상시 단계(`gloss_stage.py`)다.

## 재사용 판정

먼저 정해진 것은 무엇을 병기하지 *않을* 것인가였다. 사용자 룰링의 핵심은 이렇다. 코퍼스의 다른 글에 이미 병기 전례가 있거나 `terms.yml`에 등록된 용어가 병기 없이 이탤릭으로 다시 등장하면, 그것은 누락이 아니라 **의도적 재사용**이다. 이미 아는 용어를 다시 언급하며 병기를 생략한 것이므로 절대 건드리지 않는다. 병기 대상은 색인에 없는 신규 용어뿐이고, 같은 신규 용어가 여러 글의 정의 박스에 나오면 논리적으로 가장 앞선 글 하나에만 붙인다. 같은 카테고리면 `weight`가 가장 작은 글이고, 카테고리가 다르면 기계가 판단하지 않고 리뷰로 넘긴다.

그리고 어느 경로에서든 지키는 원칙이 하나 있다. **임의 번역 금지.** 파이프라인의 어느 지점에서도 LLM이 새 역어를 만들어내지 못한다. positive root에 '양근'을 지어 붙이던 사고의 전례가 코드 주석에 남아 있다.

## 소스 계층과 백필

병기를 만들지 않는다면 어디서 가져오는가. 소스는 네 층이고 전부 캐시된다.

- S0: 코퍼스 전례. ko 글 전체에서 `*en<sub>ko</sub>*` 스캔.
- S0b: `terms.yml`의 기존 en → ko 대응.
- S1: KMS 대한수학회 수학용어집. exact 일치 행만 쓰고, 콤마로 나열된 복수 후보가 있을 수 있다.
- S2: 위키백과 langlink(en → ko). 형태 도출이 필요해 리뷰 전용이다.

`gloss_backfill.py`는 detect → research → classify → apply 네 단계로 돌고, 단계마다 캐시를 남겨 재실행이 저렴하다. 1차 실행에서 KMS exact 단일 매치 45건이 자동 적용됐고(글 42개, `<sub>` 삽입 47건), 남은 판정은 REVIEW 346건(다중 정의처 21 · 위키만 196 · 무소스 129)과 REUSE 154건이었다. 코퍼스의 무병기 이탤릭 중 3분의 1이 "건드리면 안 되는" 재사용이었던 셈이다.

REVIEW 346건에는 항목별 권고 판정(코퍼스 전례 우선, 품사 일치, 동음이의 의심 시 보류)을 붙여 리뷰 파일로 사용자에게 넘겼고, 사용자는 권고에서 이탈할 항목만 표시했다. 확정 룰링은 결정론적 스크립트가 일괄 적용했다. 최종 집계는 적용 261, 역어 없이 색인만 하는 ko-빈 21, 영구 생략 39, 보류 25다. ko 글 131개가 고쳐졌고 `terms.yml`에 항목 281개가 새로 들어갔다. 적용은 파일별 트랜잭션이라 검증에 실패하면 그 파일만 원복되고, `terms.yml`의 기존 항목은 어떤 경우에도 건드리지 않는다.

## 동음이의 게이트

커밋 제목에 "LLM 게이트"가 들어간 이유는 그 자동 적용 45건에 있다. KMS exact 단일 매치라 기계적으로 믿고 적용했는데, 사후 검토에서 8건이 오병기로 판명됐다. KMS는 전 분야 용어집이라 교차 분야 동음이의어가 섞여 있다. 환론 문맥의 reducible에 분수 쪽 뜻의 KMS 표제 '약분가능'이 붙는 식인데, 그 문맥이라면 '가약'이어야 한다.

그래서 상시 단계에서는 exact 단일 매치도 더 이상 무조건 자동이 아니다. haiku가 정의 문맥과 병기 후보의 수학적 일치를 판정하고, "yes"일 때만 자동 적용한다.

```python
if gv != "yes":
    verdict, val = "review", \
        f"게이트 {gv}: KMS 단일 후보 {val!r} 자동 적용 보류"
```
{: data-filename="scripts/term-extraction/term_extract_worker.py"}

no든 unsure든 호출 실패든 전부 리뷰로 넘어간다(fail-to-review). KMS 복수 후보는 별도 프롬프트가 후보 목록 *안에서* 번호로 고르고, 코드가 그 번호가 실제 후보 범위인지 검증한다. 어느 후보도 맞지 않으면 NONE이고, NONE 역시 리뷰다. LLM에게 허용된 출력은 번호 하나 또는 세 단어짜리 verdict뿐이다.

## 상시 단계

백필이 끝난 뒤에도 새 글과 새 정의는 계속 생기므로, `gloss_stage.py`가 추출 워커의 1.5단계로 들어갔다. 매 틱 워커가 고른 글에서 무병기 이탤릭을 탐지하고, 사용자 룰링으로 생략이 확정된 용어(`gloss_skip.yml`, smooth·ambient 같은 단독 형용사류가 대부분이다)와 이미 리뷰에 올라간 용어(`gloss_pending.json`)를 거른 뒤, 남은 신규 용어만 위의 소스·게이트 경로에 태운다. 캐시는 백필과 공유하고 쓰기는 read-merge-write라, 두 경로가 동시에 돌아도 서로를 덮지 않는다.

곁들여 들어간 룰링이 둘 있다. 하나는 교양수학 예외다. 어떤 용어의 정의처가 전부 교양수학(calculus·linear_algebra)이면 그것은 커리큘럼상 선행일 뿐 정식 거처가 아니므로, 이후 전공 글의 정의는 뉘앙스 판정 없이 defs에 추가된다. 다른 하나는 defs의 논리 순서다. defs 추가가 등록순 append라 순서에 보장이 없던 것을, `terms_lint.py`에 DEFS_ORDER 검사를 신설해 카테고리 순서와 `weight` 순으로 잠갔다(`--fix` 지원).

정리하면 이 파이프라인에서 LLM이 하는 일은 번역이 아니다. 남이 만든 후보를 문맥에 대 보고 고르거나 기각하는 것, 그게 전부다. 백필 내내 새 역어를 지어낸 횟수는 0이고, 그 0을 강제하는 장치가 위에 센 것만 세 겹이다. 수십조 파라미터를 굴려서 하는 일이 객관식 문제 풀이라는 점에 대해서는, 생각하지 않기로 했다.
