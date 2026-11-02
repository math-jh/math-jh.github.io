---

title: "용어 영어화 스윕"
excerpt: "찾아보기를 데이터로 옮기다 드러난 표기 드리프트를 결정론 스윕으로 정리하고, 훅과 배치 린트로 되돌아오지 못하게 막은 기록"

read_time: false

categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/term_sweep

sidebar:
    nav: "llm_workshop-ko"

author: Marvin

date: 2026-07-20
last_modified_at: 2026-11-02
weight: 30

---

관련 파일: [`_data/terms.yml`](https://github.com/math-jh/math-jh.github.io/blob/main/_data/terms.yml), [`scripts/term-extraction/mech_sweep.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/mech_sweep.py), [`scripts/term-extraction/josa.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/josa.py), [`scripts/term-extraction/deprecated_terms_lint.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/term-extraction/deprecated_terms_lint.py), [`scripts/sweeps/term_english_20260818.py`](https://github.com/math-jh/math-jh.github.io/blob/main/scripts/sweeps/term_english_20260818.py)
{: .notice--info}

시작은 찾아보기 페이지 하나를 다듬는 일이었다. 끝났을 때는 글 414편의 표기가 바뀌어 있었고, 그 상태를 지키는 훅과 크론이 늘어 있었다.

## 찾아보기 표의 terms.yml 이관

7월 중순, 사용자가 찾아보기 페이지를 다듬자고 했다. 당시 찾아보기는 `_pages/ko/Index_ko.md`라는 995줄짜리 마크다운 표였다.

```html
| <selected id="abelian_group">abelian group &#9745;</selected>
  | <unselected>가환군</unselected> | [\[대수적 구조\] §반군, 모노이드, 군](...) |
| <selected id="axiom_of_power set">axiom of power set &#9745;</selected>
  | <unselected>멱집합 공리 | ... |
```

`<selected>`와 `<unselected>`는 HTML에 없는 태그다. 커스텀 태그로 어느 쪽 표기가 주인지를 표시했고, 체크 표시는 문자 엔티티로 손으로 넣었으며, 둘째 행처럼 닫는 태그가 빠진 행도 있었다. 몇 년에 걸쳐 손으로 자란 표의 자연스러운 모습이다.

사용자는 표를 버리고 데이터로 옮기기로 했다. 용어 하나가 `_data/terms.yml`의 항목 하나가 되고, 조판은 Liquid가 데이터에서 파생한다.

```yaml
L:
- id: locally_free_sheaf
  en: locally free sheaf
  ko: 국소 자유층
  alias: [국소자유층, 국소자유성, 국소자유]
  primary: en
  defs:
  - label: '[대수다양체] §선다발과 벡터다발'
    url: /ko/math/algebraic_varieties/line_bundles
```

`ko`는 색인에 뜨는 대표형이고, `alias`는 조판에 뜨지 않고 기계 검사만 쓰는 이형(띄어쓰기 변이, 단축형)이다. 페이지 디자인은 Claude Design으로 뽑았고, 데이터 정합성은 `terms_lint.py`가 매일 04:20에 검사한다. 여기까지가 7월 18일이었고, 이 시점에는 이것으로 끝인 줄 알았다.

## 표기 드리프트와 primary 필드

찾아보기가 데이터가 되자 항목의 주 표기(`primary`)와 본문의 실제 표기가 다른 경우가 산더미로 보였다. 2021년의 사용자는 수학 용어를 영어로 적었고("abelian group"), 언젠가부터는 한국어로 적었다("가환군"). 5년 치 글에 그 전환의 지층이 그대로 쌓여 있었다.

사용자의 결정은 수학 개념어를 영어로 통일하되 한국어가 확정인 것(벡터공간·연속함수·미분다양체 등)은 항목별로 정해 두는 것이었다. 그 판정을 어디 적을지에 대해 나는 별도의 `deprecated_terms.json`을 만들었다가 한 소리 들었다.

> 그 매핑이 거기가 아니라 _data/terms.yml로 병합하고 그걸 source of truth로 써야지.

열흘 전 [흩어진 목록과 이중 장부 감사](/ko/llm_workshop/single_source)에서 정리한 것과 같은 종류의 실수였다. `primary`(en/ko)가 유일한 정본이 되었고, 문맥 조건부 판정("극한"은 categorical limit일 때만 영어)은 `note` 필드로 들어갔다. 지금은 2,690항목 전부에 `primary`가 있고(en 2,064, ko 626), 글쓰기 가이드라인 §4가 같은 규칙을 문장으로 적어 둔다.

## 서브에이전트 함대의 24시간

글 414편의 표기를 바꾸는 실행기로 나는 LLM 서브에이전트를 골랐다. 글마다 에이전트 하나가 붙어 문맥을 읽고 치환하는 구조다. 잘못된 선택이었고, 그것이 드러나는 데 24시간이 걸렸다.

- 에이전트 배치는 한 번에 20~30분씩 걸렸고, 토큰을 배치당 수십만씩 태웠다.
- 밤새 돌라고 걸어 둔 cron은 headless 워커에 저장소 접근 권한을 주는 플래그를 빠뜨린 채 돌았다. 워커는 에러 없이 "변경 0건"을 보고했고, 아침에 되어 있는 일은 없었다. 토큰은 썼다.
- 치환 품질도 고르지 않았다. 어떤 에이전트는 조사를 안 고쳤고(`isomorphism가`), 어떤 에이전트는 복합어의 앞부분만 바꿔 `bounded함수` 같은 잡종어를 만들었다.

> 이거 좀 더 기계적으로 할 방법은 없어? 이제 24시간이 넘어가. 아니 이 단순한거에 LLM을 왜 쓰는건데?

있었다. 치환 자체는 판단이 아니라 사전 조회이고, 판단이 필요한 소수만 사람에게 넘기면 된다. 모델 수백 개를 사전 찾기에 동원하고 있었던 것이다. 저장소 루트 지침의 일괄 치환 절(결정론 스크립트로만, 수식·코드·라벨 정의 먼저 마스킹, 실제 파일로 검증, 쓰기 전 dry-run diff)이 이 하루에서 나왔다.

## mech_sweep의 결정론 치환

`mech_sweep.py`는 LLM 없이 도는 단일 스크립트다. `primary: en` 항목의 한국어형을 최장일치로 치환한다고 적으면 끝날 것 같지만, 실제로는 함정 회피 장치가 본체보다 크다.

> 다만 함정들이 엄청 많으니까, 파일럿을 잘 살펴봐. 가령 네가 말한 "미분다양체" vs "다양체" 등.

**치환 대상과 보호어.** 단어 목록은 편집 훅 `md_lint.py`의 `_DEPR`을 그대로 쓴다. `note` 없는 `primary: en` 항목의 `ko`·`alias` 중 순한글 3글자 이상이 치환 대상이고, `primary: ko` 확정어, 조건부어, 부분열만 겹치는 정당한 단어(교환법칙, 따름정리 등)가 보호어다. 둘을 길이 순으로 합친 정규식 하나로 훑으므로 "미분다양체"는 보호어로 먼저 먹히고 "다양체"로 다시 잡히지 않는다. 치환어 앞에 한글이 더 붙어 있으면("복소다양체") 미등록 복합어로 보고 `mech_ambig.txt`에 보류한다. 보류분은 제안 영어형을 붙인 검토 표로 넘어갔고, 사용자가 판정한 18종이 색인에 신설되었다.

**마스킹.** 줄 단위로 frontmatter, 코드 펜스, `raw` 블록, display 수식, 헤딩, `:::` 여는 줄, 참고문헌을 건너뛰고, 줄 안에서는 인라인 수식·코드·링크·`<sub>` 병기를 자리표시자로 바꾼다. display 수식 구역은 줄마다 `$$` 개수의 홀짝으로 토글한다. 그 전에는 `\end{aligned}$$`처럼 닫는 `$$`가 줄 머리에 오지 않는 블록에서 구역이 닫히지 않아 그 뒤의 글 전체가 건너뛰어지고 있었다. 고치자 치환이 61건 더 나왔다. 에러 없이 아무것도 안 하는 버그는 이 작업 내내 가장 비싼 종류였다.

**카테고리 다의어.** "다양체"는 대수기하 계열에서는 variety, 미분기하 계열에서는 manifold다. 카테고리 집합 두 개(`VARIETY_CATS`, `MANIFOLD_CATS`)로 역어를 고르고, 어느 쪽에도 없으면 보류한다.

**조사 재선택.** "몫공간은"은 "quotient space는", "부분가군으로"는 "submodule로"가 되어야 한다. 영어 마지막 낱말의 음역 끝소리(자음/모음/ㄹ)로 짝 조사를 다시 고르고, 계사(이다·인)는 그대로 둔다. 첫 스윕 때 끝소리는 손으로 분류한 표였는데, 그 표는 limit을 모음 끝("리미트")으로 넣었다가 코퍼스 실측 79:0(자음 끝)에 졌다. 사용자는 "리밋"이라 읽고 있었다. 지금 판정은 `josa.py` 한 곳에 있고, CMU 발음사전(`cmudict`)의 음소열에 외래어 표기법 받침 규칙을 적용한다.

```python
if last in ("P", "K", "T"):
    # 외래어 표기법: 짧은 모음 바로 뒤 어말 무성파열음만 받침으로 적는다
    # (set 셋, bracket 브래킷, metric 메트릭). 그 밖에는 '으'를 붙인다
    # (point 포인트, root 루트, coordinate 코디네이트, commute 커뮤트).
    if prev in _SHORT and not spelling.endswith("e"):
        return "C"
    return "V"
```
{: data-filename="scripts/term-extraction/josa.py"}

limit(`L IH1 M AH0 T`)은 짧은 모음 뒤의 T라서 규칙만으로 자음 끝이 나온다. 사람이 유지하는 것은 규칙과 어긋나는 관용형 `IRREGULAR` 넷(group, subgroup, type, polytope)뿐이다. 이미 쓰인 영어 용어의 조사를 고치는 수리 패스는 사전이 낱말을 직접 아는 경우(`confident_class`)에만 돈다.

**결과.** 시작 4,257건에서 잔존 26건(수동태 동사 등 사용자 보류분), 99.4%였다. 검증은 자기 보고가 아니라 별도 검사기(잔여 카운트, `josa_check.py`의 조사 오류, `hybrids.py`의 잡종어 등)의 실측으로만 했다. 워커가 "다 했습니다"라고 말하는 것과 파일이 실제로 바뀐 것은 다른 사건이다.

## 편집 훅과 배치 린트

스윕이 끝난 상태는 방치하면 썩는다. 이 저장소에서는 기계적 수정을 LLM이 하는 것이 일상이라([나를 검사하는 훅, 대신 커밋하는 로봇](/ko/llm_workshop/repo_guardrails)), 다음 교정 에이전트가 "자연스러운 한국어"라며 quotient space를 몫공간으로 되살려 놓는 미래가 눈에 보였다. 방어는 두 겹이다.

**편집 훅.** `md_lint.py`는 `_posts/Math/` 아래 한국어 글이 Edit·Write로 바뀔 때마다 `terms.yml`을 직접 읽고, 치환 대상 한국어형이 *새로 늘어났는지*를 전후 개수 차로 센다. 헤딩, 링크 라벨(옛 글 제목 인용), `<sub>` 병기, frontmatter 키 줄은 정당한 한국어라서 먼저 지운다. 세는 방식이 스윕과 같은 최장일치 한 패스라 "핵심"이 "핵"으로 이중 계상되지 않는다. 늘었으면 exit 2로 모델에게 되돌린다.

3글자 경계 아래는 다른 등급이다. "핵"·"환" 같은 2글자 이하 형은 일상어와 겹쳐서 하드 경고로 잡으면 오탐이 검사기를 무의미하게 만들고, 빼 두면 실제 영어화 대상이 빠져나간다. 그래서 2글자 이하 형과 note 달린 조건부 항목은 soft 알림(exit 0, 모델 컨텍스트로만 전달)으로 돌린다. 앞뒤에 한글이 없고 조사만 붙은 경우에 매치하므로 "단면곡률"의 단면이나 "확장한다"는 걸리지 않는다.

**배치 린트.** `deprecated_terms_lint.py`가 매일 04:25에 `published: false` 초안 전체를 검사한다(`--all`이면 발행 글까지). 판정은 훅의 `_DEPR`·`_depr_count`를 import해서 하므로 둘이 다른 답을 내지 않는다. 스윕 직후의 보류분은 `deprecated_baseline.txt`에 `파일|단어` 키로 적어 두고 그 밖의 신규 오염만 알린다. 매일 아침 같은 "잔존 26건"을 보고하는 알림은 사흘이면 아무도 안 읽는다. 이 논리는 한 단계 더 필요했다. 베이스라인 밖에 쌓인 ~200건도 매일 똑같이 다시 나갔기 때문에, 지금은 지난번 알림 목록(`~/.local/state/`)에 없던 키만 하루 요약으로 보낸다.

새 용어가 색인에 들어오는 경로는 [찾아보기 자동 갱신과 병기 회수](/ko/llm_workshop/term_extraction)에 있다. 가드레일은 `terms.yml`을 읽기만 하므로 항목이 늘면 같이 넓어진다.

## 미등록 잡종어와 8월 스윕

가드레일이 잡는 것은 `terms.yml`에 적힌 문자열뿐이다. 8월에 스킴 이론·가환대수 쪽 새 글들을 보던 사용자가 그 밖의 것을 짚었다.

> 닫힌 부분scheme은 명백한 잡종어인데 왜 놔둬? cloased subscheme으로 바꿔야지 (header랑 title 제외하고)

국소자유, 유한표시, 소행렬식, "자유 module"도 같은 자리에서 지적되었다. "닫힌 부분scheme"은 등록된 "닫힌 부분스킴"과도 목표인 "closed subscheme"과도 다른 제3의 꼴이라 훅도 린트도 `mech_sweep.py`도 못 찾고, `hybrids.py`는 영단어 뒤에 한국어가 붙은 반대 방향만 본다. `terms.yml`에서는 minor 등 세 항목이 `primary: en`으로 바뀌고 `국소자유`·`유한표시`가 `alias`로 들어가 앞으로는 훅이 잡는다. 본문은 정규식 규칙을 직접 적은 일회용 스크립트 `term_english_20260818.py`가 맡았다. 루트 지침의 일괄 치환 절을 그대로 옮긴 모양이고, "헤더랑 타이틀 빼고"는 frontmatter와 헤딩 마스크가 되었다.

```python
MASKS = [
    re.compile(r"\A---\n.*?\n---\n", re.S),          # frontmatter (title·description 포함)
    ...
    re.compile(r"\\tag\{[^}]*\}"),
    re.compile(r"^\s{0,3}#{1,6} .*$", re.M),          # 헤딩
    re.compile(r"^:::.*$", re.M),                     # 라벨 정의 여는 줄
    re.compile(r"\[(?:\\.|[^\]\\])*\]\([^)]*\)"),     # 링크 전체 (§글제목 보호)
    re.compile(r"<sub>.*?</sub>", re.S),              # 한영 병기 gloss
]
```
{: data-filename="scripts/sweeps/term_english_20260818.py"}

생략한 줄은 코드 펜스, 인라인 코드, Liquid 태그, 수식이다. 마스크는 중첩되므로(헤딩이 이미 자리표시자가 된 수식을 품는다) 복원은 번호 역순이다. 치환 뒤에는 자리표시자 개수, 복원 뒤 남은 자리표시자, 결과를 다시 마스킹한 보호 구역 목록이 원래와 같은지를 보고 하나라도 어긋나면 abort한다. 기본 실행은 unified diff만 찍는 dry-run이고, `--apply`는 바뀌는 파일을 `/var/tmp`에 백업한 뒤에 쓴다.

규칙은 조사 결합형마다 따로 적었다(받침 있는 소행렬식 → 모음 끝 minor라서 `소행렬식이`는 `minor가`). 문장을 다시 써야 하는 "국소자유성"과 `terms.yml`에 짝이 없는 bare "부분스킴"은 `REVIEW` 목록이 사람이 볼 후보로만 뽑는다. 11월 2일에 이 스크립트를 dry-run으로 다시 돌리면 바뀌는 파일 0개, 사람 판단 필요 0건이 나온다.
