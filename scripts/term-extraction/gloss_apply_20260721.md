# gloss 백필 일괄 적용 로그 — 2026-07-21

입력: `gloss_backfill_review_recommendations.md` 346항목 + 사용자 마크 16건 +
확정 룰링 다이제스트(scratchpad) + 추가 룰링 2건(base locus 적용·인명 소급 sweep).
실행: 결정론적 스크립트 (scratchpad `build_decisions.py`·`apply_gloss_batch.py`·`name_sweep.py`,
gloss_backfill의 detect 계열 재사용 — classify 재실행 없음). 권고 파일 무수정(마크 보존).

## 판정 집계

| 판정 | 건수 | 비고 |
| --- | --- | --- |
| 적용 | 261 | 삽입 254 + 이탤릭 키 정정 1(alternating) + 기병기(정규화 선반영) 6 |
| ko-빈 | 21 | terms.yml 색인만 (`primary: en`, ko `''`) |
| skip | 39 | gloss_skip.yml 등록 |
| 보류·사용자 역어 | 25 | 무조치 (base locus는 추가 룰링으로 적용에 편입) |

파일: ko 글 131개 편집 + 인명 sweep 8개(중복 2 제외 시 총 137개) · terms.yml 신규 entry 281 ·
기존 entry 1(mapping cone: defs 기존재, ko `''`→`사상뿔` 채움) · gloss_skip.yml +39.
백업: `terms.yml.bak-gloss-apply-20260721`.

## 적용 로그 (용어 → gloss → 글)

| 용어(en) | gloss(ko) | 글 | 비고 |
| --- | --- | --- | --- |
| `abelian presheaf` | 아벨 준층 | Topology/2024-11-19-Presheaves |  |
| `abelianization` | 아벨화 | Algebraic_Structures/2024-07-04-Abelian_Groups |  |
| `acyclic on $\mathcal{M}$` | $\mathcal{M}$ 위에서 비순환 | Algebraic_Topology/2025-09-17-Acyclic_Models_Theorem |  |
| `affine algebraic group` | 아핀 대수적 군 | Scheme_Theory/2026-03-11-Algebraic_Groups |  |
| `affine-local property` | 아핀-국소 성질 | Scheme_Theory/2025-02-03-Topology_of_Schemes |  |
| `algebraic $k$-cycle` | 대수적 $k$-순환 | Algebraic_Varieties/2026-05-11-Chow_Groups | 기병기(2차 정규화 선반영) — terms 등록만 |
| `almost split sequence` | 거의 분할 수열 | Representation_Theory/2026-06-20-Auslander-Reiten_Theory | 기병기(2차 정규화 선반영) — terms 등록만 |
| `alternating $2$-form` | 교대 $2$-형식 | Derived_Algebraic_Geometry/2026-07-01-Shifted_Symplectic_Structures | 이탤릭 키 `alternating $2$-형식` → 표준 영문형 정정 + 병기 |
| `ample` | 풍부한 | Algebraic_Varieties/2026-03-29-Linear_Systems |  |
| `associated graded` | 동반 등급 | Lie_Theory/2026-06-20-Universal_Enveloping_Algebra |  |
| `associated graded module` | 동반 등급가군 | Commutative_Algebra/2024-10-20-Blowup_Algebra |  |
| `associated graded ring` | 동반 등급환 | Commutative_Algebra/2024-10-20-Blowup_Algebra |  |
| `associator` | 결합자 | Category_Theory/2024-06-12-Monoidal_Categories |  |
| `augmentation map` | 첨가 사상 | Homological_Algebra/2024-11-01-Resolutions | 같은 글 2회 출현 — 첫 정의 박스만 병기(뒤는 의도적 재사용) |
| `Auslander–Reiten sequence` | Auslander–Reiten 수열 | Representation_Theory/2026-06-20-Auslander-Reiten_Theory |  |
| `Auslander–Reiten translate` | AR 변환 | Representation_Theory/2026-06-20-Auslander-Reiten_Theory | 기병기(2차 정규화 선반영) — terms 등록만 |
| `B-model connection` | B-model 접속 | Mirror_Symmetry/2026-05-24-Gauss_Manin_Connection |  |
| `base locus` | 기저점 자취 | Algebraic_Varieties/2026-03-29-Linear_Systems | 추가 룰링(2026-07-21)로 보류 해제 |
| `basepoint-free` | 기저점 없음 | Algebraic_Varieties/2026-03-29-Linear_Systems |  |
| `basic monoid` | 기본 모노이드 | Gromov_Witten_Theory/2026-07-10-Log_Stable_Maps |  |
| `big Givental $J$-function` | 큰 Givental $J$-함수 | Mirror_Symmetry/2026-05-28-Givental_J_Function |  |
| `big quantum product` | 큰 양자 곱 | Symplectic_Geometry/2023-06-15-Gromov_Witten_Invariants |  |
| `bimonoid` | 쌍모노이드 | Category_Theory/2024-06-14-Monoid_Objects |  |
| `birational map` | 쌍유리 사상 | Algebraic_Varieties/2026-03-15-Rational_Maps |  |
| `birationally equivalent` | 쌍유리 동치 | Algebraic_Varieties/2026-03-15-Rational_Maps |  |
| `Braid relation` | 꼬임 관계식 | Lie_Theory/2025-01-07-Kazhdan_Lusztig_Polynomial |  |
| `canonical divisor` | 표준 인자 | Algebraic_Varieties/2026-03-29-Canonical_Bundle |  |
| `canonical holomorphic volume form` | 표준 정칙 부피 형식 | Mirror_Symmetry/2026-05-24-Gauss_Manin_Connection |  |
| `cardinal product` | 기수 곱 | Set_Theory/2022-11-29-Operation_of_Cardinals |  |
| `cardinal sum` | 기수 합 | Set_Theory/2022-11-29-Operation_of_Cardinals |  |
| `Cartan matrix` | 카르탕 행렬 | Lie_Theory/2025-11-12-Root_Systems |  |
| `cartesian category` | 데카르트 범주 | Category_Theory/2024-06-12-Monoidal_Categories |  |
| `Casimir operator` | 카시미르 연산자 | Lie_Theory/2026-06-21-Representations_of_sl2 |  |
| `category of elements` | 원소들의 범주 | Category_Theory/2023-06-22-Representable_Functors |  |
| `Category with models` | 모델을 갖는 범주 | Algebraic_Topology/2025-09-17-Acyclic_Models_Theorem |  |
| `Cauchy` | 코시 | Analysis/2026-06-02-Metric_Spaces |  |
| `Cauchy-Riemann equation` | 코시-리만 방정식 | Symplectic_Geometry/2023-06-01-J_Holomorphic_Curves |  |
| `Chern polynomial` | 천 다항식 | Algebraic_Varieties/2026-05-12-Chern_Classes |  |
| `Chevalley–Serre presentation` | 슈발레-세르 표시 | Lie_Theory/2026-06-21-Serre_Relations |  |
| `Chow ring` | 저우 환 | Algebraic_Varieties/2026-05-11-Intersection_Product |  |
| `classifying stack` | 분류 스택 | Stacks/2026-07-01-Fibered_Categories_and_Stacks |  |
| `closed symmetric monoidal category` | 닫힌 대칭 모노이드 범주 | Category_Theory/2023-05-29-Adjoints |  |
| `coarse moduli functor` | 성긴 모듈라이 함자 | Stacks/2026-07-01-Moduli_Problems |  |
| `cocontinuous functor` | 여연속 함자 | Category_Theory/2023-06-22-Limits |  |
| `codegeneracy` | 여퇴화 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `coface` | 여면 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `cohomology functor` | 코호몰로지 함자 | Sheaf_Theory/2026-07-01-Perverse_Sheaves |  |
| `coisotropic subspace` | 여등방 부분공간 | Symplectic_Geometry/2023-04-28-Linear_Symplectic_Geometry |  |
| `compact form` | 콤팩트 형식 | Lie_Theory/2026-02-28-Borel_Subgroup |  |
| `compactifiable` | 옹골화 가능 | Sheaf_Theory/2026-07-01-Six_Functors |  |
| `compactly supported` | 콤팩트 지지 | Algebraic_Topology/2025-09-23-Poincare_Duality |  |
| `complete linear system` | 완비 선형계 | Algebraic_Varieties/2026-03-29-Linear_Systems |  |
| `conjugate representation` | 켤레표현 | Representation_Theory/2026-02-13-Representations_of_Finite_Groups |  |
| `continuous functor` | 연속 함자 | Category_Theory/2023-06-22-Limits |  |
| `covering map` | 피복 사상 | Algebraic_Topology/2025-07-27-Covering_Spaces |  |
| `Cox ring` | 콕스 환 | Toric_Geometry/2026-03-09-Cox_Construction_and_GIT_Quotient |  |
| `Coxeter functor` | 콕세터 함자 | Representation_Theory/2026-06-21-Reflection_Functors |  |
| `degeneracy map` | 퇴화 사상 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `Deligne–Mumford stack` | 들리뉴-멈퍼드 스택 | Stacks/2026-07-01-Algebraic_Stacks |  |
| `derivation` | 미분 | Multilinear_Algebra/2022-12-08-Derivations |  |
| `derived pullback` | 유도 당김 | Sheaf_Theory/2026-07-01-Derived_Category_of_Sheaves |  |
| `derived sheaf-Hom` | 유도 층 $\Hom$ | Sheaf_Theory/2026-07-01-Derived_Category_of_Sheaves |  |
| `diagonalize` | 대각화 | Field_Theory/2025-05-11-Etale_Algebras |  |
| `dual representation` | 쌍대 표현 | Representation_Theory/2026-02-13-Representations_of_Finite_Groups |  |
| `Dubrovin connection` | 두브로빈 접속 | Mirror_Symmetry/2026-05-21-Dubrovin_Connection |  |
| `Dynkin diagram` | 딘킨 도표 | Lie_Theory/2026-02-28-Borel_Subgroup |  |
| `effective Cartier divisor` | 유효 카르티에 인자 | Scheme_Theory/2025-03-08-Complete_Intersections |  |
| `Eilenberg-Steenrod axiom` | 에일렌베르크-스틴로드 공리 | Algebraic_Topology/2025-08-05-Computation_of_Homology |  |
| `embedded point` | 매장점 | Scheme_Theory/2025-02-05-Algebra_of_Schemes |  |
| `enough injective` | 충분한 단사 대상 | Homological_Algebra/2024-11-01-Resolutions |  |
| `enough projective` | 충분한 사영 대상 | Homological_Algebra/2024-11-01-Resolutions |  |
| `exact` | 완전 | Category_Theory/2024-08-29-Abelian_Categories |  |
| `exact functor` | 완전 함자 | Category_Theory/2024-08-29-Abelian_Categories |  |
| `exterior $k$-bundle` | $k$차 외대수다발 | Manifolds/2022-06-21-Differential_Forms |  |
| `exterior algebra bundle` | 외대수다발 | Manifolds/2022-06-21-Differential_Forms |  |
| `face map` | 면 사상 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `fan` | 부채 | Toric_Geometry/2026-05-17-Toric_Varieties |  |
| `field of rational functions` | 유리함수체 | Ring_Theory/2025-05-06-Polynomial_Rings |  |
| `filter base` | 필터 기저 | Topology/2022-11-09-Equivalent_Formulations_of_Topology |  |
| `filtered complex` | 여과 복합체 | Homological_Algebra/2026-04-08-Spectral_Sequences |  |
| `first countable` | 제1 가산 | Topology/2024-12-11-Filter_Convergence |  |
| `Fixed point set` | 고정점 집합 | Scheme_Theory/2026-03-11-Algebraic_Groups |  |
| `flag variety` | 깃발 다양체 | Lie_Theory/2026-02-28-Borel_Subgroup |  |
| `free animated ring` | 자유 애니메이트 환 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `free on $\mathcal{M}$` | $\mathcal{M}$ 위에서 자유 | Algebraic_Topology/2025-09-17-Acyclic_Models_Theorem |  |
| `functor of points of $X$` | $X$의 점 함자 | Scheme_Theory/2025-02-19-Morphism_of_Schemes |  |
| `fundamental groupoid` | 기본 준군 | Algebraic_Topology/2025-07-09-Homotopy |  |
| `Gauss-Manin connection` | 가우스-마닌 접속 | Mirror_Symmetry/2026-05-24-Gauss_Manin_Connection |  |
| `generalized eigenspace` | 일반화 고유공간 | Linear_Algebra/2026-01-21-Jordan_Canonical_Form |  |
| `generic fiber` | 일반 올 | Scheme_Theory/2025-03-08-Fiber_Products |  |
| `Genus $g$, $n$-point, degree $\beta$ Gromov-Witten invariant` | 그로모프-위튼 불변량 | Symplectic_Geometry/2023-06-15-Gromov_Witten_Invariants |  |
| `GIT quotient` | GIT 몫 | Scheme_Theory/2026-03-11-Algebraic_Groups | 같은 글 2회 출현 — 첫 정의 박스만 병기(뒤는 의도적 재사용) |
| `global section functor` | 전역 단면 함자 | Scheme_Theory/2025-01-27-Affine_Schemes |  |
| `globally generated` | 전역생성 | Algebraic_Varieties/2026-04-06-Cohomology_of_Projective_Spaces |  |
| `Godement sheaf` | 고드망 층 | Algebraic_Varieties/2026-04-05-Sheaf_Cohomology |  |
| `good pair` | 좋은 쌍 | Algebraic_Topology/2025-08-05-Computation_of_Homology |  |
| `graded abelian group` | 등급 가환군 | Algebraic_Structures/2024-07-04-Abelian_Groups |  |
| `graded homomorphism of degree $i$` | 차수 $i$의 등급 준동형 | Algebraic_Structures/2024-08-12-Graded_Modules |  |
| `grading operator` | 등급 연산자 | Mirror_Symmetry/2026-05-21-Dubrovin_Connection |  |
| `Gromov-Witten potential` | 그로모프-위튼 퍼텐셜 | Symplectic_Geometry/2023-06-30-Quantum_Cohomology |  |
| `Grothendieck pretopology` | 그로텐디크 준위상 | Stacks/2026-07-01-Grothendieck_Topology |  |
| `Hamiltonian vector field` | 해밀턴 벡터장 | Symplectic_Geometry/2023-05-08-Symplectic_Manifold |  |
| `Hartogs number` | 하르톡스 수 | Set_Theory/2022-11-29-Order_Relations_Between_Ordinals |  |
| `Hessenberg variety` | 헤센베르크 다양체 | Lie_Theory/2026-06-09-Richardson_Peterson_Variety |  |
| `homogeneous coordinate ring` | 동차 좌표환 | Toric_Geometry/2026-03-09-Cox_Construction_and_GIT_Quotient |  |
| `homogeneous prime ideal` | 동차 소아이디얼 | Commutative_Algebra/2025-01-16-Krull_Dimension |  |
| `homological $\delta$-functor` | 호몰로지 $\delta$-함자 | Homological_Algebra/2024-11-03-Derived_Functors |  |
| `homotopy category` | 호모토피 범주 | Homological_Algebra/2026-04-13-Derived_Categories |  |
| `Hori-Vafa mirror` | 호리-바파 거울 | Mirror_Symmetry/2026-05-18-Mirror_Symmetry_Overview |  |
| `Hurewicz fibration` | 후레비치 올뭉치 | Algebraic_Topology/2026-07-01-Fibrations |  |
| `inductive` | 귀납적 | Set_Theory/2021-08-23-Axiom_of_Choice |  |
| `injective sheaf` | 단사층 | Algebraic_Varieties/2026-04-05-Sheaf_Cohomology |  |
| `internal $\Hom$` | 내부 $\Hom$ | Category_Theory/2023-05-29-Adjoints |  |
| `internal weak direct product` | 내부 약한 직접곱 | Algebraic_Structures/2023-01-09-Restricted_Sums |  |
| `intersection form` | 교차 형식 | Algebraic_Varieties/2026-05-04-Riemann_Roch_Surfaces |  |
| `inverse image sheaf` | 역상층 | Topology/2023-11-01-Sheaves |  |
| `inversion` | 반전 | Group_Theory/2025-03-29-Symmetric_Groups |  |
| `invertible sheaf` | 가역층 | Scheme_Theory/2026-06-21-Quasicoherent_Sheaves |  |
| `Irrelevant ideal` | 무관 아이디얼 | Toric_Geometry/2026-03-09-Cox_Construction_and_GIT_Quotient |  |
| `isolated hypersurface singularity` | 고립 초곡면 특이점 | Mirror_Symmetry/2026-05-19-Frobenius_Manifold |  |
| `Isom presheaf` | Isom 준층 | Stacks/2026-07-01-Fibered_Categories_and_Stacks |  |
| `isotropic subspace` | 등방 부분공간 | Symplectic_Geometry/2023-04-28-Linear_Symplectic_Geometry |  |
| `Iwahori–Hecke algebra` | 이와호리-헤케 대수 | Lie_Theory/2025-01-07-Kazhdan_Lusztig_Polynomial |  |
| `J-holomorphic` | $J$-정칙 | Symplectic_Geometry/2023-06-01-J_Holomorphic_Curves |  |
| `Jordan block` | 조르당 블록 | Linear_Algebra/2026-01-21-Jordan_Canonical_Form |  |
| `Killing form` | 킬링 형식 | Lie_Theory/2025-11-12-Root_Systems |  |
| `Lagrangian subspace` | 라그랑지안 부분공간 | Symplectic_Geometry/2023-04-28-Linear_Symplectic_Geometry |  |
| `lattice polytope` | 격자 다면체 | Toric_Geometry/2026-05-18-Reflexive_Polytope_and_Fano_Variety |  |
| `left almost split` | 왼쪽 거의 분할 | Representation_Theory/2026-06-20-Auslander-Reiten_Theory |  |
| `left compatible` | 왼쪽 호환 | Algebraic_Structures/2021-09-02-Algebraic_Structures |  |
| `left exact` | 왼쪽 완전 | Category_Theory/2024-08-29-Abelian_Categories |  |
| `left translation` | 좌평행이동 | Lie_Theory/2023-01-23-Lie_Groups |  |
| `Lichtenbaum–Schlessinger functor` | 리히텐바움-슐레진저 함자 | Derived_Algebraic_Geometry/2026-07-01-Deformation_Theory |  |
| `limit point compact` | 극한점 옹골 | Topology/2024-12-11-Filter_Convergence |  |
| `linear system` | 선형계 | Algebraic_Varieties/2026-03-29-Linear_Systems |  |
| `local coefficient system` | 국소 계수 체계 | Algebraic_Topology/2025-09-23-Poincare_Duality |  |
| `local homology group` | 국소 호몰로지 군 | Algebraic_Topology/2025-09-23-Poincare_Duality |  |
| `locally closed embedding` | 국소 닫힌 매장 | Scheme_Theory/2025-02-18-Closed_Subschemes |  |
| `locally Euclidean of dimension $m$` | $m$차원 국소 유클리드 | Topology/2024-12-15-Compactness |  |
| `locally free sheaf of rank $r$` | 랭크 $r$ 국소 자유층 | Scheme_Theory/2026-06-21-Quasicoherent_Sheaves |  |
| `log Calabi-Yau pair` | 로그 칼라비-야우 쌍 | Mirror_Symmetry/2026-05-24-Gauss_Manin_Connection |  |
| `log scheme` | 로그 스킴 | Gromov_Witten_Theory/2026-07-10-Log_Structures |  |
| `lower adjoint` | 아래 수반 | Set_Theory/2022-05-01-Filter_and_Ideal |  |
| `mapping cone` | 사상뿔 | Homological_Algebra/2023-01-02-Long_Exact_Sequence |  |
| `maximal spectrum` | 극대 스펙트럼 | Representation_Theory/2026-06-15-Spectrum_of_Finite_Dimensional_Algebras |  |
| `maximal torus` | 극대 원환면 | Lie_Theory/2026-02-24-Torus_Action |  |
| `minimal length coset representatives` | 최소 길이 잉여류 대표원 | Lie_Theory/2026-06-08-Bruhat_Decomposition |  |
| `minimal projective presentation` | 최소 사영 표시 | Representation_Theory/2026-06-20-Auslander-Reiten_Theory | 기병기(2차 정규화 선반영) — terms 등록만 |
| `model` | 모델 | Algebraic_Topology/2025-09-17-Acyclic_Models_Theorem |  |
| `moduli functor` | 모듈라이 함자 | Stacks/2026-07-01-Moduli_Problems |  |
| `monoid of fraction` | 분수 모노이드 | Algebraic_Structures/2021-09-04-Grothendieck_Groups |  |
| `multiplication` | 곱셈 | Category_Theory/2024-06-14-Monoid_Objects | 같은 글 2회 출현 — 첫 정의 박스만 병기(뒤는 의도적 재사용) |
| `mutually left adjoint` | 서로 왼쪽 수반 | Category_Theory/2023-05-29-Adjoints |  |
| `mutually right adjoint` | 서로 오른쪽 수반 | Category_Theory/2023-05-29-Adjoints |  |
| `negative nilpotent subalgebra` | 음의 멱영 부분대수 | Lie_Theory/2026-06-21-Highest_Weight_Modules |  |
| `node` | 노드 | Symplectic_Geometry/2023-06-10-Stable_Maps_Moduli |  |
| `nondegeneracy` | 비퇴화성 | Derived_Algebraic_Geometry/2026-07-01-Shifted_Symplectic_Structures |  |
| `nonsingular` | 비특이 | Algebraic_Varieties/2026-03-22-Tangent_Spaces_and_Smoothness |  |
| `nonsingular point` | 비특이점 | Algebraic_Varieties/2026-03-22-Tangent_Spaces_and_Smoothness |  |
| `Novikov variable` | 노비코프 변수 | Symplectic_Geometry/2023-06-15-Gromov_Witten_Invariants |  |
| `open refinement` | 열린 세분 | Topology/2024-12-15-Compactness |  |
| `open Richardson variety` | 열린 리처드슨 다양체 | Lie_Theory/2026-06-09-Richardson_Peterson_Variety |  |
| `open submanifold` | 열린 부분다양체 | Manifolds/2022-06-09-Examples_of_Manifolds |  |
| `opposite Schubert cell` | 반대 슈베르트 셀 | Lie_Theory/2026-06-08-Bruhat_Decomposition |  |
| `opposite Schubert variety` | 반대 슈베르트 다양체 | Lie_Theory/2026-06-08-Bruhat_Decomposition |  |
| `orbit` | 궤도 | Algebraic_Structures/2023-02-14-Group_Actions |  |
| `pairwise comaximal` | 쌍마다 공최대 | Ring_Theory/2025-04-11-Chinese_Remainder_Theorem |  |
| `parameter ideal` | 매개변수 아이디얼 | Commutative_Algebra/2025-01-19-System_of_Parameters | 같은 글 2회 출현 — 첫 정의 박스만 병기(뒤는 의도적 재사용) |
| `partial mapping` | 편사상 | Set_Theory/2022-11-23-Operation_of_Functions |  |
| `path homotopic` | 경로 호모토픽 | Algebraic_Topology/2025-07-09-Homotopy |  |
| `perfect closure` | 완전 폐포 | Field_Theory/2025-04-11-Fields |  |
| `perfect ring` | 완전환 | Field_Theory/2025-04-11-Fields |  |
| `perverse t-structure` | perverse t-구조 | Sheaf_Theory/2026-07-01-Perverse_Sheaves |  |
| `Peterson variety` | 피터슨 다양체 | Lie_Theory/2026-06-09-Richardson_Peterson_Variety |  |
| `plus construction` | plus 구성 | Stacks/2026-07-01-Grothendieck_Topology |  |
| `Plücker embedding` | 플뤼커 매장 | Algebraic_Varieties/2026-03-24-Grassmannians |  |
| `polynomial algebra` | 다항식 대수 | Algebraic_Structures/2024-08-30-Algebras |  |
| `positive nilpotent subalgebra` | 양의 멱영 부분대수 | Lie_Theory/2026-06-21-Highest_Weight_Modules |  |
| `positive norm` | 양의 노름 | Ring_Theory/2025-04-01-Integral_Domains |  |
| `positive root` | 양의 근 | Lie_Theory/2025-11-12-Root_Systems |  |
| `prime filter` | 소필터 | Set_Theory/2022-05-01-Filter_and_Ideal |  |
| `principal Cartier divisor` | 주 카르티에 인자 | Algebraic_Varieties/2026-03-25-Divisors |  |
| `principal cycle` | 주순환 | Algebraic_Varieties/2026-05-11-Chow_Groups | 기병기(2차 정규화 선반영) — terms 등록만 |
| `principal open set` | 주열린집합 | Algebraic_Varieties/2026-03-12-Affine_Varieties |  |
| `pseudoholomorphic` | 유사정칙 | Symplectic_Geometry/2023-06-01-J_Holomorphic_Curves |  |
| `pullback sieve` | 당김 체 | Stacks/2026-07-01-Grothendieck_Topology |  |
| `Quadratic relation` | 이차 관계식 | Lie_Theory/2025-01-07-Kazhdan_Lusztig_Polynomial |  |
| `Quotient bundle` | 몫다발 | Algebraic_Varieties/2026-03-25-Line_Bundles |  |
| `R-polynomial` | $R$-다항식 | Lie_Theory/2025-01-07-Kazhdan_Lusztig_Polynomial |  |
| `rank r vector bundle` | 랭크 $r$ 벡터다발 | Algebraic_Varieties/2026-03-25-Line_Bundles |  |
| `rational` | 유리 | Toric_Geometry/2026-06-21-Delzant_Construction |  |
| `rationally equivalent` | 유리 동치 | Algebraic_Varieties/2026-05-11-Chow_Groups | 기병기(2차 정규화 선반영) — terms 등록만 |
| `regular sequence` | 정칙렬 | Gromov_Witten_Theory/2026-07-10-Refined_Gysin |  |
| `relative homology` | 상대 호몰로지 | Algebraic_Topology/2025-08-05-Computation_of_Homology |  |
| `relative trace` | 상대 trace | Multilinear_Algebra/2025-05-07-Symmetric_Tensors |  |
| `representing object` | 표현 대상 | Scheme_Theory/2026-06-21-Functor_of_Points |  |
| `restricted sum` | 제한합 | Algebraic_Structures/2023-01-09-Restricted_Sums |  |
| `restriction map` | 제한 사상 | Topology/2024-11-19-Presheaves |  |
| `Richardson variety` | 리처드슨 다양체 | Lie_Theory/2026-06-09-Richardson_Peterson_Variety |  |
| `Riemann–Roch dimension` | 리만-로흐 차원 | Algebraic_Varieties/2026-04-22-Riemann_Roch_Theorem |  |
| `right almost split` | 오른쪽 거의 분할 | Representation_Theory/2026-06-20-Auslander-Reiten_Theory |  |
| `right compatible` | 오른쪽 호환 | Algebraic_Structures/2021-09-02-Algebraic_Structures |  |
| `right exact` | 오른쪽 완전 | Category_Theory/2024-08-29-Abelian_Categories |  |
| `root` | 근 | Lie_Theory/2025-11-12-Root_Systems |  |
| `root system` | 근계 | Lie_Theory/2025-11-12-Root_Systems |  |
| `Schubert cell` | 슈베르트 셀 | Lie_Theory/2026-06-08-Bruhat_Decomposition |  |
| `second countable` | 제2 가산 | Topology/2024-12-11-Filter_Convergence |  |
| `semi-locally simply connected` | 반국소 단순연결 | Algebraic_Topology/2025-07-27-Covering_Spaces |  |
| `semigroup algebra` | 반군 대수 | Toric_Geometry/2026-03-05-Affine_Toric_Varieties |  |
| `semisimple` | 반단순 | Lie_Theory/2025-11-12-Root_Systems |  |
| `semistable` | 반안정 | Scheme_Theory/2026-03-11-Algebraic_Groups |  |
| `separable element` | 분리가능 원소 | Field_Theory/2025-05-15-Separable_Extensions |  |
| `Serre fibration` | 세르 올뭉치 | Algebraic_Topology/2026-07-01-Fibrations |  |
| `Serre relation` | 세르 관계식 | Lie_Theory/2026-06-21-Serre_Relations |  |
| `sheaf Hom` | 층 $\Hom$ | Scheme_Theory/2026-06-21-Quasicoherent_Sheaves |  |
| `sheaf of relative differentials` | 상대 미분층 | Scheme_Theory/2026-06-21-Sheaf_of_Differentials |  |
| `sheafification functor` | 층화 함자 | Topology/2023-11-01-Sheaves |  |
| `shift functor` | 이동 함자 | Homological_Algebra/2026-04-13-Derived_Categories | 같은 글 2회 출현 — 첫 정의 박스만 병기(뒤는 의도적 재사용) |
| `simple normal crossing divisor` | 단순 정규교차 인자 | Toric_Geometry/2026-05-20-Logarithmic_Differentials |  |
| `simplicial identity` | 단체 항등식 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `simplicial module` | 단체 가군 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `simplicial object` | 단체 대상 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `simplicial set` | 단체 집합 | Derived_Algebraic_Geometry/2026-07-01-Animated_Rings |  |
| `singular` | 특이 | Lie_Theory/2026-02-24-Torus_Action | defs에 AV/Tangent_Spaces 정의 11 겸용 등록 |
| `skew field` | 비가환체 | Ring_Theory/2026-06-20-Division_Rings |  |
| `small quantum product` | 작은 양자 곱 | Symplectic_Geometry/2023-06-15-Gromov_Witten_Invariants |  |
| `specialization` | 특수화 | Scheme_Theory/2025-02-03-Topology_of_Schemes |  |
| `stalk-local` | 줄기-국소 | Scheme_Theory/2025-02-03-Topology_of_Schemes |  |
| `standard étale` | 표준 에탈 | Scheme_Theory/2026-06-21-Smooth_and_Etale_Morphisms |  |
| `strongly convex` | 강하게 볼록 | Toric_Geometry/2026-03-05-Affine_Toric_Varieties |  |
| `subsheaf` | 부분층 | Topology/2023-11-01-Sheaves |  |
| `symmetor` | 대칭자 | Category_Theory/2024-06-12-Monoidal_Categories |  |
| `symmetric Euler form` | 대칭 오일러 형식 | Representation_Theory/2026-06-21-Reflection_Functors |  |
| `symmetric power` | 대칭 거듭제곱 | Multilinear_Algebra/2025-05-07-Symmetric_Tensors |  |
| `symplectic complement` | 사교 여공간 | Symplectic_Geometry/2023-04-28-Linear_Symplectic_Geometry |  |
| `symplectic subspace` | 사교 부분공간 | Symplectic_Geometry/2023-04-28-Linear_Symplectic_Geometry |  |
| `symplectic vector space` | 사교벡터공간 | Symplectic_Geometry/2023-04-28-Linear_Symplectic_Geometry |  |
| `symplectomorphism` | 사교동형사상 | Symplectic_Geometry/2023-05-08-Symplectic_Manifold |  |
| `tangent cone` | 접뿔 | Algebraic_Varieties/2026-03-22-Tangent_Spaces_and_Smoothness |  |
| `tangent covector` | 여접벡터 | Manifolds/2022-06-16-Examples_of_Differentials |  |
| `Tautological bundle` | 보편 선다발 | Algebraic_Varieties/2026-03-25-Line_Bundles |  |
| `tautological line bundle` | 보편 선다발 | Algebraic_Varieties/2026-03-25-Line_Bundles |  |
| `topological manifold of dimension $m$` | $m$차원 위상다양체 | Topology/2024-12-15-Compactness |  |
| `total Chern class` | 전체 천 특성류 | Algebraic_Topology/2025-10-07-Characteristic_Classes |  |
| `total complex` | 전복합체 | Homological_Algebra/2022-09-10-Homology |  |
| `trace map` | 대각합 사상 | Multilinear_Algebra/2024-08-30-Hom_and_Tensor |  |
| `Triangulated category` | 삼각 분할 범주 | Homological_Algebra/2026-04-13-Derived_Categories |  |
| `trivial extension` | 자명한 확장 | Group_Theory/2025-03-29-Extensions |  |
| `twisted inverse image` | 비틀린 역상 | Sheaf_Theory/2026-07-01-Six_Functors |  |
| `two-variable adjunction` | 이변수 수반 | Category_Theory/2023-05-29-Adjoints |  |
| `uniformizing parameter` | 균등화원 | Commutative_Algebra/2025-01-24-Divisors |  |
| `universal $\delta$-functor` | 보편 $\delta$-함자 | Homological_Algebra/2024-11-03-Derived_Functors |  |
| `universal $A$-derivation` | 보편 $A$-미분 | Commutative_Algebra/2024-12-26-Differentials |  |
| `universal element` | 보편 원소 | Category_Theory/2023-06-22-Representable_Functors |  |
| `upper adjoint` | 위 수반 | Set_Theory/2022-05-01-Filter_and_Ideal |  |
| `vanishing scheme` | 영점 스킴 | Scheme_Theory/2025-02-18-Closed_Subschemes |  |
| `Verdier dual` | 베르디에 쌍대 | Sheaf_Theory/2026-07-01-Verdier_Duality |  |
| `weak direct product` | 약한 직접곱 | Algebraic_Structures/2023-01-09-Restricted_Sums |  |
| `weight decomposition` | 무게 분해 | Lie_Theory/2026-02-24-Torus_Action |  |
| `weight space` | 무게 공간 | Lie_Theory/2026-02-24-Torus_Action |  |
| `Whitney sum formula` | 휘트니 합 공식 | Algebraic_Varieties/2026-05-12-Chern_Classes |  |

## 인명 한글 전환 (적용 gloss 내부, 전역 룰링)

| 용어 | 권고 gloss | 최종 gloss | 근거 |
| --- | --- | --- | --- |
| `Coxeter functor` | Coxeter 함자 | 콕세터 함자 | 확정 예 |
| `Gauss-Manin connection` | Gauss-Manin 접속 | 가우스-마닌 접속 | 확정 예 |
| `Novikov variable` | Novikov 변수 | 노비코프 변수 | 확정 예 |
| `Lichtenbaum–Schlessinger functor` | Lichtenbaum–Schlessinger 함자 | 리히텐바움-슐레진저 함자 | 확정 예 |
| `effective Cartier divisor` | 유효 Cartier 인자 | 유효 카르티에 인자 | 확정 예(Cartier) |
| `principal Cartier divisor` | 주 Cartier 인자 | 주 카르티에 인자 | 확정 예(Cartier) |
| `Serre relation` | Serre 관계식 | 세르 관계식 | 세르 — 표준 표기(장피에르 세르), 같은 배치 슈발레-세르와 정합 |
| `Deligne–Mumford stack` | Deligne–Mumford 스택 | 들리뉴-멈퍼드 스택 | ko위키 피에르 들리뉴·데이비드 멈퍼드 |
| `log Calabi-Yau pair` | 로그 Calabi-Yau 쌍 | 로그 칼라비-야우 쌍 | ko위키 칼라비-야우 다양체 |
| `Plücker embedding` | Plücker 매장 | 플뤼커 매장 | 표준 표기(플뤼커 좌표) |
| `Verdier dual` | Verdier 쌍대 | 베르디에 쌍대 | ko위키 베르디에 쌍대성 |
| `Cox ring` | Cox 환 | 콕스 환 | 표준 표기(데이비드 콕스) |
| `Hessenberg variety` | Hessenberg 다양체 | 헤센베르크 다양체 | 표준 표기(독일어 Hessenberg) |
| `Iwahori–Hecke algebra` | Iwahori–Hecke 대수 | 이와호리-헤케 대수 | 표준 표기(이와호리·헤케) |

로마자 유지 + 보고 2건:
- `big Givental $J$-function`: Givental — 코퍼스 병기 <sub>Givental J-함수</sub> 전례(로마자)와 충돌, 한글 표기 미확립
- `Auslander–Reiten sequence`: Auslander–Reiten — 한글 표기 미확립(아우스랜더/오슬랜더 등 분분), 같은 글 AR 변환 병기와 공존

## ko-빈 등록 21건

- `Auslander–Reiten quiver` — Representation_Theory/2026-06-20-Auslander-Reiten_Theory
- `Bar involution` — Lie_Theory/2025-01-07-Kazhdan_Lusztig_Polynomial
- `category fibered in groupoids` — Stacks/2026-07-01-Fibered_Categories_and_Stacks
- `charge matrix` — Mirror_Symmetry/2026-05-18-Mirror_Symmetry_Overview
- `comodule structure` — Scheme_Theory/2026-03-11-Algebraic_Groups
- `derived Deligne–Mumford stack` — Derived_Algebraic_Geometry/2026-07-01-Derived_Schemes
- `derived prestack` — Derived_Algebraic_Geometry/2026-07-01-Derived_Schemes
- `descendant Gromov-Witten invariant` — Symplectic_Geometry/2023-06-15-Gromov_Witten_Invariants
- `Distinguished triangle` — Homological_Algebra/2026-04-13-Derived_Categories
- `gravitational descendant` — Mirror_Symmetry/2026-05-28-Givental_J_Function
- `left unitor` — Category_Theory/2024-06-12-Monoidal_Categories
- `linearly disjoint` — Field_Theory/2025-04-26-Algebraic_Extensions
- `monodromy functor` — Algebraic_Topology/2025-07-27-Covering_Spaces
- `naive cotangent complex` — Multilinear_Algebra/2024-05-11-Cotangent_Complex
- `normal fan` — Toric_Geometry/2026-05-17-Toric_Varieties
- `parabolic subgroup` — Lie_Theory/2026-06-08-Bruhat_Decomposition
- `right unitor` — Category_Theory/2024-06-12-Monoidal_Categories
- `scheme-theoretic image` — Scheme_Theory/2025-02-18-Closed_Subschemes
- `sifted colimit completion` — Derived_Algebraic_Geometry/2026-07-01-Animated_Rings
- `simply-laced` — Lie_Theory/2026-02-28-Borel_Subgroup
- `superpotential` — Mirror_Symmetry/2026-05-18-Mirror_Symmetry_Overview

## skip 39건 (gloss_skip.yml 등록)

`ambient`, `annihilate`, `central`, `CFG`, `cosupport 조건`, `de Rham 미분`, `DM stack`, `dominant`, `equivariant`, `fiberwise Gromov–Witten 불변량`, `fpqc 위상`, `Genus $g$, $n$-marked, $\beta$-class stable map`, `geometric`, `Grothendieck 위상`, `Hamiltonian $G$-공간`, `Hermitian`, `homologous`, `IC 층`, `intersection cohomology 층`, `Laplace 방정식`, `LCH space`, `locally $P$`, `locally principal`, `non-degenerate pairing`, `open (resp. closed)`, `primary`, `properly intersect`, `pure codimension $1$`, `reductive`, `Riemann 적분가능`, `set-값 moduli functor`, `Sink에서의 reflection functor`, `small`, `SNC divisor`, `Source에서의 reflection functor`, `uniform하게`, `unimodular`, `virtual 차원`, `weight $\lambda$의 weight space`

## 보류·사용자 역어 25건 (무조치)

`associate`, `associate in $A$`, `cocone`, `commutation factor`, `contracted`, `general anticanonical section`, `global frame`, `initial form`, `invariant ring`, `left cancellable`, `linearly reductive`, `local frame`, `local on target`, `Mirror domain`, `nilpotency class`, `oriented vector bundle`, `perfectly $T_4$-space`, `perfectly normal space`, `reduced scheme structure`, `related family`, `right cancellable`, `semi-perfect ring`, `solvability class`, `transport map`, `transversely intersect`

## 실패 목록

- 적용 실패: **0건** (346항목 전부 해결)
- 특이: `multiplication`·`GIT quotient`·`parameter ideal`·`shift functor`·`augmentation map`은
  같은 글 안 두 번째 출현이 무병기로 남음 — 첫 박스만 병기하는 정책의 의도적 잔존
  (terms.yml 등록으로 이후 gloss_stage가 REUSE 처리).

## 부수 sweep (다이제스트 1·8)

1. 받침→지지 (2곳):
   - Sheaf_Theory/Six_Functors: `<sub>콤팩트 받침 코호몰로지</sub>` → `<sub>콤팩트 지지 코호몰로지</sub>`
   - Manifolds/Integration 정의 1: `support<sub>받침</sub>` → `support<sub>지지</sub>`
   - terms.yml ko 동기화 대상: 없음 (받침 포함 entry 부재)
   - **추가 발견(미변경·보고)**: Toric_Geometry/Toric_Cohomology 53행 `support set<sub>받침 집합</sub>` —
     룰링이 명시한 2곳 밖의 세 번째 병기. 통일하려면 별도 확인 필요.
   - prose '받침' 사용처(미변경, 43회 — Six_Functors 병기 주변 다수 포함): Algebraic_Topology/Characteristic_Classes,
     Algebraic_Varieties/Dimension, Mirror_Symmetry/Mirror_Symmetry_Overview, Set_Theory/Limits,
     Sheaf_Theory/Perverse_Sheaves·Verdier_Duality·Six_Functors, Toric_Geometry/Toric_Cohomology
2. moduli→모듈라이 (2곳, Stacks/Moduli_Problems):
   - `<sub>성긴 moduli 공간</sub>` → `<sub>성긴 모듈라이 공간</sub>`
   - `<sub>섬세한 moduli 공간</sub>` → `<sub>섬세한 모듈라이 공간</sub>`
   - terms.yml ko 동기화 대상: 없음
   - ko-primary 혼성 병기(대상 아님·보고): 같은 글 `*moduli 문제<sub>moduli problem</sub>*`(28행),
     `*moduli stack<sub>moduli stack</sub>*`(119행)

## 기타 확인 사항 (룰링 지시 보고)

- `multiplication` 관련 코퍼스 '승법' 1회의 실체: Analysis/Linear_ODE 67행 '열등승법적'
  (submultiplicative) — **다른 단어**라 미치환 (사용자 재확인 대기).
- cartesian '카테시안' 코퍼스 출현: **0건** 재확인 완료 — 추가 조치 없음.
- GW 카테고리(gitignore local-only) 글 3건에 병기·terms 등록 포함: Log_Structures(로그 스킴),
  Log_Stable_Maps(기본 모노이드), Refined_Gysin(정칙렬).

## 추가 룰링 2 — 기존 병기 로마자 인명 소급 sweep

ko 글 `<sub>` 내부(한글 포함 병기만) 25건 / 8개 파일 + terms.yml ko 1건. 전환표:
호지(Hodge)·호지-드람 라플라스(Hodge–de Rham Laplace)·자리스키(Zariski)·리만 쌍선형(Riemann)·
켈러(Kähler)·에르미트(Hermitian)·하우스홀더(Householder)·렙셰츠(Lefschetz) + 확인 후 확정 2건:
**네이엔하위스**(Nijenhuis — ko위키 '알버르트 네이엔하위스'·개복소다양체 문서 '네이엔하위스 텐서' 실확인),
**귀진**(Gysin — ko위키 문서 제목 '귀진 완전열' 실확인).

| 파일 | 치환 |
| --- | --- |
| Algebraic_Varieties/2026-03-22-Tangent_Spaces_and_Smoothness | Zariski 접공간 → 자리스키 접공간 |
| Complex_Geometry/2026-06-22-Almost_Complex_Structures | Nijenhuis 텐서 → 네이엔하위스 텐서 |
| Complex_Geometry/2026-06-22-Dolbeault_Cohomology | Hodge 수 → 호지 수 |
| Complex_Geometry/2026-06-22-Hodge_Theory | Hodge 별작용소 → 호지 별작용소; Hodge–de Rham Laplace 작용소 → 호지-드람 라플라스 작용소; Hodge 수 → 호지 수; Lefschetz 연산자 → 렙셰츠 연산자 |
| Complex_Geometry/2026-06-22-Kahler_Manifolds | Hermitian 계량 → 에르미트 계량; Hermitian 다양체 → 에르미트 다양체; Hermitian 형식 → 에르미트 형식; Kähler 다양체 → 켈러 다양체; Kähler 계량 → 켈러 계량; Kähler 형식 → 켈러 형식; Kähler 류 → 켈러 류; Kähler 퍼텐셜 → 켈러 퍼텐셜 |
| Complex_Geometry/2026-06-22-Kodaira_Embedding_Theorem | Hermitian 계량 → 에르미트 계량; Hermitian 선다발 → 에르미트 선다발; 정수 Kähler 형식 → 정수 켈러 형식; 정수 Kähler 류 → 정수 켈러 류; Hodge 다양체 → 호지 다양체; Riemann 쌍선형 관계 → 리만 쌍선형 관계 |
| Gromov_Witten_Theory/2026-07-10-Refined_Gysin | Gysin 사상 → 귀진 사상; 정련된 Gysin 사상 → 정련된 귀진 사상 |
| Linear_Algebra/2026-06-23-Complex_Inner_Product_Spaces | Hermitian 내적 → 에르미트 내적; Householder 반사 → 하우스홀더 반사 |
| _data/terms.yml (ko 값) | Zariski 접공간 → 자리스키 접공간 |

잔존(한글 sub 안 대상 인명): 0. prose·영어 이탤릭 쪽은 룰링대로 불변.

## 검증

- terms.yml YAML 파싱 정상, 항목 938 → 1219 (+281 = 신규 등록 수와 일치). 쓰기 게이트 통과.
- `terms_lint.py`: 에러 40 → 40 (**신규 에러 0**). 경고 76 → 193 (+117: 신규 entry의
  UNPUB(초안 defs)·ko-빈 SCHEMA W — 전부 W-레벨, DEFS_ORDER류는 04:20 cron 몫, --fix 미실행).
- md_lint CLI 무작위 10개: 출력된 경고는 전부 legacy prose + primary:en 신규 등록에 따른
  tier1 확장분. 137개 수정 파일 전수에서 전/후 텍스트로 diff-감응 검사
  (added_patterns·deprecated_terms)를 비교 — **내 변경 기인 신규 경고 0**
  (병기 삽입은 검사에서 `<sub>` 제거 후 계수되므로 구조적으로도 불가).
- 수정 글 137개 전수 diff 감사: 변경이 의도된 라인의 `<sub>` 삽입/치환(+ alternating 키 정정
  1건)뿐임을 스냅샷 대조로 확인. $ 짝수성 전후 불변, `<sub>`/`</sub>` 짝 일치.
- 재탐지: 적용 용어의 무병기 출현이 파일마다 정확히 1 감소.

