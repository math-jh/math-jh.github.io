# primary 무표기 73종 검토 목록 (2026-07-19)

용어 영어화 룰링에서 **아직 primary 판정이 없는** terms.yml 항목 중, 초안
prose 에 실제로 등장하는 73종이다 (나머지 무표기였던 346종은 출현 0이라
일괄 `primary: en` 처리 완료). 사용자 검토 후 `_data/terms.yml` 의 해당
항목에 다음 중 하나를 달면 훅·린트가 즉시 따라온다:

- `primary: en` — prose 영어 확정 (이후 잔존 출현은 스윕 대상)
- `primary: ko` — 한국어 확정
- 조건부면 `primary: en` + `note: '조건 지침'` (note 있으면 자동 경고 제외)

건수는 초안(published:false) prose 실측 (링크 라벨·병기·헤딩 제외).

| ko 형 | 출현 | 항목 id (en) | 지시 |
|---|---|---|---|
| 다양체 | 360건/28편 | variety (variety) | en |
| 대수적 | 144건/55편 | algebraic (algebraic) | en |
| 서로소 | 79건/25편 | disjoint (disjoint) | ko |
| 선형사상 | 61건/15편 | linear_map (linear map) | ko |
| 부분다양체 | 55건/17편 | submanifold (submanifold) | ko |
| 정규화 | 48건/17편 | normalization (normalization) | en |
| 국소화 | 35건/6편 | localization (localization) | en |
| 호모토피 | 30건/4편 | homotopy (homotopy) | en |
| 교차수 | 29건/10편 | intersection_number (intersection number) | en |
| 부분표현 | 29건/2편 | subrepresentation (subrepresentation) | en |
| 비퇴화 | 23건/4편 | nondegenerate (nondegenerate) | en |
| 외미분 | 20건/6편 | exterior_derivative (exterior derivative) | en |
| 초평면 | 18건/2편 | hyperplane (hyperplane) | en+note (calculus 글에만 ko) |
| 부분가군 | 16건/3편 | submodule (submodule) | en |
| 접다발 | 16건/8편 | tangent_bundle (tangent bundle) | en |
| 동차다항식 | 15건/5편 | homogeneous_polynomial (homogeneous polynomial) | en |
| 사교다양체 | 14건/4편 | symplectic_manifold (symplectic manifold) | en |
| 대각합 | 14건/1편 | trace (trace) | en |
| 전단사사상 | 14건/3편 | bimorphism (bimorphism) | en |
| 동치류 | 13건/6편 | equivalence_class (equivalence class) | en |
| 범함수 | 12건/5편 | functional (functional) | en |
| 여차원 | 11건/5편 | codimension (codimension) | en |
| 벡터다발 | 11건/6편 | vector_bundle (vector bundle) | en |
| 리만 계량 | 10건/3편 | Riemannian_metric (Riemannian metric) | en |
| 연결성분 | 9건/3편 | connected_component (connected component) | en |
| 선형동치 | 9건/2편 | linearly_equivalent (linearly equivalent) | en |
| 인덱스 | 9건/4편 | index (index) | en |
| 교차 중복도 | 7건/3편 | intersection_multiplicity (intersection multiplicity) | en |
| 대수적으로 닫힌 체 | 7건/6편 | algebraically_closed_field (algebraically closed field) | en |
| 동차좌표 | 7건/3편 | homogeneous_coordinates (homogeneous coordinates) | en |
| 갈루아 | 7건/3편 | galois (Galois) | en |
| 외대수 | 6건/4편 | exterior_algebra (exterior algebra) | en |
| 구조상수 | 6건/4편 | structure_constant (structure constant) | en |
| 정칙성 | 6건/2편 | Regularity (Castelnuovo-Mumford regularity) | en |
| 쌍마다 서로소 | 6건/2편 | pairwise_disjoint (pairwise disjoint) | ko |
| 아이디얼 | 6건/3편 | ideal (ideal) | en |
| 토릭 다양체 | 6건/1편 | toric_variety (toric variety) | en |
| 일반점 | 6건/2편 | generic_point (generic point) | en |
| 단위분할 | 5건/3편 | partition_of_unity (partition of unity) | en |
| 대칭대수 | 4건/1편 | symmetric_algebra (symmetric algebra) | en |
| 피복공간 | 4건/1편 | covering_space (covering space) | en |
| 카테고리 | 4건/3편 | category (category) | en |
| 정규공간 | 4건/1편 | normal_space (normal space) | en |
| 쌍선형형식 | 4건/3편 | bilinear_form (bilinear form) | en |
| 정수적 | 3건/2편 | integral (integral) | en |
| 직교여공간 | 2건/2편 | orthogonal_complement (orthogonal complement) | en |
| 영사상 | 2건/2편 | zero_map (zero map) | en |
| 초곡면 | 2건/1편 | hypersurface (hypersurface) | en |
| 열린 부분스킴 | 2건/1편 | open_subscheme (open subscheme) | en |
| 반사적 | 2건/1편 | reflexive (reflexive) | en |
| 분리공리 | 2건/1편 | separation_axiom (separation axiom) | en |
| 동차원소 | 1건/1편 | homogeneous_element (homogeneous element) | en |
| 연결공간 | 1건/1편 | connected_space (connected space) | en |
| 대수적 군 | 1건/1편 | algebraic_group (algebraic group) | en |
| 국소적으로 닫힌 | 1건/1편 | locally_closed (locally closed) | en |
| 내림사슬조건 | 1건/1편 | descending_chain_condition (descending chain condition) | en |
| 닫힌점 | 1건/1편 | closed_point (closed point) | en |
| 시작 대상 | 1건/1편 | initial_object (initial object) | en |
| 쌍대 격자 | 1건/1편 | dual_lattice (dual lattice) | en |
| 국소적으로 유한 | 1건/1편 | locally_finite (locally finite) | en |
| 대각화가능 | 1건/1편 | diagonalizable (diagonalizable) | en |
| 극대 아이디얼 | 1건/1편 | maximal_ideal (maximal ideal) | en |
| 영공간의 차원 | 1건/1편 | nullity (nullity) | en |
| 아핀 뿔 | 1건/1편 | affine_cone (affine cone) | en |
| 비퇴화 쌍선형형식 | 1건/1편 | non-degenerate_bilinear_form (non-degenerate bilinear form) | en |
| 쌍대다발 | 1건/1편 | dual_bundle (dual bundle) | en |
| 더 섬세한 | 1건/1편 | finer (finer) | en |
| 초월적 | 1건/1편 | transcendental (transcendental) | en |
| 순서집합 | 1건/1편 | ordered_set (ordered set) | en |
| 선형연산자 | 1건/1편 | linear_operator (linear operator) | ko |
| 합성열 | 1건/1편 | composition_series (composition series) | en |
| 비대칭적 | 1건/1편 | asymmetric (asymmetric) | en |
| 적분곡선 | 1건/1편 | integral_flow (integral flow) | en |

---

## 적용 결과 (2026-07-19 23:51)

지시 그대로 terms.yml 에 반영 완료: en 68 (초평면은 en+note 'Calculus 만 한글'),
ko 5 (서로소·선형사상·부분다양체·쌍마다 서로소·선형연산자). 최종 en 700 / ko 155 /
무표기 0, terms_lint 에러 0.

**bimorphism 조사 결과**: 항목 자체는 정당하다 — [범주론] §범주 L131 이
`*bimorphism<sub>전단사사상</sub>*` (monomorphism+epimorphism) 을 실제로 정의한다.
그러나 초안 출현 14건(등각사상·Riemann 사상정리·복소다양체)은 전부 "holomorphic
전단사사상" = **전단사(bijective)인 사상**이라는 합성어로, 범주론 bimorphism 이
아니다. 전단사는 primary ko 확정이므로 이 용법은 정당한 한글이다. 따라서
bimorphism 은 en + note (동음이의 구분) 로 처리해 14건이 스윕에 걸리지 않게 했다.

주의: '정칙성'(id Regularity) 의 en 은 Castelnuovo-Mumford regularity 지만
복소해석 문맥의 정칙성은 holomorphicity 다. 스윕 워커는 문맥으로 판단할 것.
