# 기계 스윕 보류분 534건 검토 목록 (2026-07-20)

결정적 스윕(`scripts/term-extraction/mech_sweep.py`)이 **판정 불가로 건드리지 않은**
것들이다. 위치 전수 목록은 `scripts/term-extraction/mech_ambig.txt`.
판정해 주시면 다음 실행이 기계적으로 마저 치환한다 (터미널 명령 한 번).

## A. 색인에 없는 복합어 — terms.yml 항목 신설 필요

아래 한글형이 tier1 단어(다양체·연접층·부분가군)를 부분열로 품고 있어
부분 치환(잡종어)을 피하려고 통째로 보류했다. 항목을 만들고 primary 를
정하면 해결된다. 제안 en 과 함께:

| ko 형 | 출현 | 제안 en | 판정 (en/ko) |
|---|---|---|---|
| 복소다양체 | ~131 | complex manifold | en |
| 준연접층 | ~52 | quasi-coherent sheaf | en |
| 다양체 (앞글자 '수') | ~10 | 대수다양체 → algebraic variety | en |
| 진부분가군 | ~11 | proper submodule | en |
| 위상다양체 | 소수 | topological manifold | en |

## B. 관형사류 — 치환 방식 룰 필요

en 확정은 됐지만 한국어 명사 앞 관형 용법이라 기계 치환하면
"algebraic 성질" 같은 혼종이 된다. 전체 구 항목(대수적 확장 등)은 이미
처리됐고, 남은 것은 bare 용법이다. 룰 예시: "(1) 뒤 명사까지 표준 영어
용어면 구 전체 영어, (2) 아니면 한글 유지" 또는 "-적/-한 활용형은 한글 유지".

| ko 형 | 출현 | 비고 |
|---|---|---|---|
| 대수적 | 144 | "대수적 성질/조건/부분집합" 등 |
| 비퇴화 | 23 | "비퇴화 쌍선형형식"(항목 있음, 처리됨) 외 bare 용법 |
| 선형동치 | 9 | "선형동치이다" 서술형 |
| 정수적·초월적·반사적 등 | 소수 | 동일 유형 |

## C. 카테고리 판정불가 '다양체' — 23건

variety(AG 계열)/manifold(미분기하 계열) 자동 판정이 안 되는 카테고리
(Gromov-Witten·Mirror_Symmetry 등)의 bare 다양체. 파일별 문맥 판단 필요.

## D. 문맥어

- 정칙성 ×6: 복소해석 = holomorphicity / AG = Castelnuovo-Mumford regularity.
- 정규화하면/함으로써 등 동사 활용 ×소수: "normalize" 계열 동사 처리 룰 필요.

---

## 적용 결과 2차 (2026-07-20 00:40)

A~D 판정 전부 반영 완료. 이번 라운드 치환 +346건, 최종 **잔존 26건** (시작 4,257
→ 99.4% 처리). 조사 오류 0 · 잡종어 0 · terms_lint 에러 0.

- **A**: 5종 반영. 부수확: quasi-coherent_sheaf 항목의 ko가 '준연속층'으로 오타
  → '준연접층'으로 수정.
- **B**: 관형+tier1 명사구는 구 전체 영어(algebraic한 대상 등), 나머지는 한글
  유지 확정. 해당 11개 항목에 note(관형 룰) 부여 — 훅·린트가 bare 용법을 더는
  경고하지 않는다.
- **C**: GW→variety 반영. Mirror_Symmetry 보류분은 실측 0건이었음 (카테고리
  판정불가 20건은 전부 Sheaf_Theory였고, Verdier·six functors 문맥이라
  manifold 로 판정).
- **D**: 정칙성 카테고리 판별(Scheme_Theory·Analysis=regularity /
  복소해석·기하=holomorphicity), normalize하면·localize하면 등 하다-동사 허용.
- **장꼬리 복합어 13종 색인 신설**: 리만다양체·고립특이점·유도카테고리·
  선형범함수·사영대수다양체·복소대수다양체·기약잉여류·주아이디얼·비동차좌표·
  등각동형사상·진부분표현·적분다양체·상대접다발.

남은 26건은 수동태 동사(정규화된/되어, 국소화된)와 1~2건짜리 복합어들
(외미분값·다양체족·격자점 등) — `scripts/term-extraction/mech_ambig.txt` 참조.
