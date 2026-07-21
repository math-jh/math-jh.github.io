# gloss 백필 REVIEW 346건 — 사전 권고 판정 (2026-07-21)

사용 방법: 아래 권고 그대로 적용해도 되는 항목은 그냥 두고, **이탈할 항목만**
체크박스에 표시하거나 옆에 한 줄로 적어 주세요. `(파생 — 확인 필수)` 태그와
`보류` 항목은 특히 봐주세요. 룰링이 오면 일괄 적용 후 term_extract cron을
재개합니다. (판정 휴리스틱: 코퍼스 전례 > 품사 일치 > 사전투 잔재 제거 >
동음이의 의심 시 보류, 임의 번역 금지.)

# 판정: REVIEW — 다중 정의처 / KMS 복수후보 미확정 (gloss_backfill_review.md 87–108행)

## REVIEW — 다중 정의처 / KMS 복수후보 미확정 — 권고 21건
요약: 수용 0 · 조정 20 · skip 0 · ko-빈 1 · 사용자역어 0 · 보류 0

일러두기: 이 구획은 단일 제안 gloss가 없던 항목들이라 `조정: <gloss>`가 곧 확정안이다.
다중 정의처 판정 기준 = categories.yml subjects 순서(커리큘럼 spine; Topology#16 < AT#17 <
Manifolds#18 < Lie#19 < AV#22 < Scheme#23 < Toric#24 < DAG#27 < SG#28 < GW#29 < MS#30) +
동일 카테고리 내 weight. **교양수학(calculus·linear_algebra) 정의처는 21건 중 0건 — '정식 거처'
룰링(GEN_ED_CATS) 해당 없음.** `파생 제안 — 사용자 확인 필수` 표시 4건, KMS 후보 밖 선택 1건(node).

- [v "지지"로 진행] `compactly supported` → 조정: 콤팩트 받침 — 정의처=Algebraic_Topology/Poincare_Duality 정의 12 (spine AT#17 < Manifolds#18; Manifolds/Integration 정의 1은 재사용 처리). 근거: 코퍼스 정확-복합 전례 *compactly supported cohomology<sub>콤팩트 받침 코호몰로지</sub>* (Sheaf_Theory/Six_Functors) + Integration 정의 1의 *support<sub>받침</sub>* + KMS 'compactly supported function=콤팩트받침함수'. FYI: 코퍼스에 지지/지지집합 병기도 3곳 혼재(Abelian_Groups·Schemes·Topology/Compactness) — 받침/지지 통일은 별도 sweep 사안
- [ ] `conjugate representation` → 조정: 켤레표현 — 코퍼스 conjugate→켤레 일관(켤레점·켤레전치·조화켤레 등 병기 5건, 본문 켤레 76회, 공액 0회) → 후보 중 '켤레표현' 선택, '공액표현' 기각. decisions.json 등록 대상
- [ ] `derivation` → 조정: 미분 — 같은 정의 박스(Multilinear_Algebra/Derivations 정의 2)에 기존 병기 *$(A,\varepsilon)$-derivation<sub>$(A,\varepsilon)$-미분</sub>*이 이미 있어 '미분'만이 글 내 정합. '미분작용소'는 differential operator와 충돌 소지. decisions.json 등록 대상
- [ ] `descendant Gromov-Witten invariant` → ko-빈 — 정의처=Symplectic_Geometry/Gromov_Witten_Invariants 정의 2 (spine SG#28 < MS#30이며, MS/Givental_J_Function 정의 1이 "[[사교기하학] §Gromov-Witten 불변량, ⁋정의 2] 본 글의 표기에 맞춰 짧게 정리" — 원 정의처를 명시 인용). gloss는 소스 없음: KMS 'descendant=내림'은 타 분야 뜻, 코퍼스는 전부 영문 descendant 유지 → epimorphism 전례로 ko 빈 값 색인. (SG 글이 published:false 초안이나 기적용 전례 있음 — APPLIED의 'Stability'가 같은 카테고리 초안에 등록됨)
- [ ] `inversion` → 조정: 반전 — 문맥=순열의 inversion(Group_Theory/Symmetric_Groups 정의 9). 코퍼스 반전 27회(뫼비우스 변환의 반전 $z\mapsto 1/z$ 등 동일 영어 어원 용법 포함), '뒤집기'는 1회(정의 아닌 prose, dihedral 반사 서술) → '반전' 선택. decisions.json 등록 대상
- [ ] `left translation` → 조정: 좌평행이동 — 코퍼스가 이미 사용(Stacks/Fibered_Categories·Algebraic_Stacks에 좌평행이동 3회+우평행이동 1회) + 같은 글(Lie_Groups)에 'left invariant→좌불변' 기적용 — 좌- 접두 일관. '왼쪽평행이동' 기각. decisions.json 등록 대상
- [ ] `locally Euclidean of dimension $m$` → 조정: $m$차원 국소 유클리드 (파생 제안 — 사용자 확인 필수) — 정의처=Topology/Compactness 정의 30 (spine Topology#16 < AT#17; AT/Topological_Manifolds 정의 1은 재사용 처리, 발행일도 Topology 쪽이 앞섬 2024-12 < 2025-07). 구성 요소 전례: 국소(국소적·국소화·국소 모형 다수)+유클리드(유클리드 공간)+$m$차원 관용. 파생이 무리라 보면 ko-빈이 차선
- [ ] `model` → 조정: 모델 — 그 글(AT/Acyclic_Models_Theorem) prose가 이미 "각 모델 $\Delta^n$"로 사용 → 글 내 용법 우선(중심확장 전례). 코퍼스 '모형'은 주로 '국소 모형(local model)' 세트구 용법이라 별개. decisions.json 등록 대상
- [코퍼스 "승법"을 곱셈으로 고칠것] `multiplication` → 조정: 곱셈 — 코퍼스 곱셈 485회 vs 승법 1회, 문맥(monoid object의 구조 사상 $\mu$)에도 자연. '승법' 기각. decisions.json 등록 대상
- [확인, 이대로 진행] `node` → 조정: 노드 (**KMS 후보 밖 — 사용자 확인 필수**) — 정의 박스 등장=Symplectic_Geometry/Stable_Maps_Moduli 정의 1 (prestable curve, 국소 모형 $xy=0$). 코퍼스 GW 글들이 '노드' 35회 상용("노드의 log smoothing", "노드가 $\ell$개인 곡선" 등) → 코퍼스 전례 최우선 룰로 마디점·결절점 모두 코퍼스와 충돌. 단 후보 밖 선택이라 decisions.json membership 검증을 통과 못 함 — 수동 적용 필요. 파이프라인 순수성을 원하면 차선은 '결절점'(대수기하 관례)이나 GW 초안들과 어긋남
- [ ] `nonsingular` → 조정: 비특이 — 정의처=Algebraic_Varieties/Tangent_Spaces_and_Smoothness 정의 11 (spine AV#22 < Toric#24; Toric/Affine_Toric 정의 8의 등장은 smooth<sub>매끄러운</sub>의 동의어 나열이라 재사용 처리). 근거: 코퍼스 prose 전례 비특이 4회(Riemannian/Comparison_Theorems). KMS '정칙' 기각(코퍼스 정칙=holomorphic 계열: 쌍정칙), 'nonsingular variety=비퇴화 다양체' 기각(코퍼스 비퇴화=nondegenerate, 사교형식)
- [ ] `orbit` → 조정: 궤도 — 정의처=Algebraic_Structures/Group_Actions 정의 13 (spine AS#5 ≪ Scheme#23; Scheme/Algebraic_Groups의 등장은 재사용 처리). 근거: KMS exact 'orbit=궤도' + 그 글 절 제목 "궤도-안정자 정리" + 코퍼스 궤도 20여회
- [ ] `prime filter` → 조정: 소필터 — 코퍼스 prime→소 확립(*prime ideal<sub>소아이디얼</sub>*·*prime field<sub>소체</sub>*, 소아이디얼 48회). '으뜸'은 코퍼스에서 primary 전용(으뜸분해·으뜸부분가군, Commutative_Algebra) — '으뜸필터' 채택 시 prime/primary 구분 붕괴. decisions.json 등록 대상
- [ ] `principal open set` → 조정: 주열린집합 (파생 제안 — 사용자 확인 필수) — 정의처=Algebraic_Varieties/Affine_Varieties 정의 5 (spine AV#22 < Scheme#23; Scheme/Spectrums 정의 10은 재사용 처리). 구성 요소 전례: principal→주 일관(주다발·주곡률·주순환·주방향·주인자·주아이디얼정역·주부)+열린집합 표준. KMS·위키 직접 소스 없음
- [ ] `Quotient bundle` → 조정: 몫다발 — 코퍼스 몫- 계열 확립(몫군·몫공간·몫가군·몫환·몫대수 등 병기 9건+) + '속→다발' 2차 룰링(자명한 벡터다발·보편다발) → '몫다발' 선택, '상속' 기각. decisions.json 등록 대상
- [ ] `root` → 조정: 근 — 문맥=Lie_Theory/Root_Systems 정의 5 (root system의 root). 코퍼스 *simple root<sub>단순근</sub>*(같은 글 기룰링)·*Chern root<sub>천 근</sub>*·제곱근 전례 → '근' 선택, '해' 기각(방정식 해 어감). decisions.json 등록 대상
- [ ] `singular` → 조정: 특이 — 정의처=Lie_Theory/Torus_Action 정의 12 (spine Lie#19 < AV#22). KMS exact 'singular=특이한'의 어미 정리(쌍정칙 전례) + 코퍼스 특이점·특이한 다수. 유의: Lie 쪽(torus 원소의 특이)과 AV/Tangent_Spaces 정의 11(다양체의 특이)은 별개 개념이나 한국어 '특이'가 양쪽 관례라 gloss 충돌 없음 — terms.yml defs에 AV 정의 11도 함께 등록 권장(동음이의 겸용)
- [ ] `skew field` → 조정: 비가환체 — ko 위키백과 '나눗셈환' 문서가 "나눗셈환(division ring) 또는 비가환체(非可換體, skew field)"로 직접 대응(소스 근거). '꼬인 체'는 코퍼스·위키 전례 없음. 유의: 그 글 정의상 skew field는 commutative 포함 가능하나 '비가환체'는 '가환을 가정하지 않는 체'라는 표준 관례어로 통용. decisions.json 등록 대상
- [ldsmra,SG가 맞음] `symplectic vector space` → 조정: 사교벡터공간 — 정의처=**Symplectic_Geometry/Linear_Symplectic_Geometry 정의 1 (spine 기계 적용과 이탈 — 사용자 확인 필수)**. 기계적 spine은 DAG#27 < SG#28로 DAG/Shifted_Symplectic 정의 4를 가리키나: (a) SG 글 제목 자체가 "사교벡터공간"이고 코퍼스 상호참조 4곳이 [§사교벡터공간, ⁋정의 1]로 이 정의를 지시, (b) DAG 박스는 "이 선형대수적 조건을 먼저 분리해 두자"로 고전 개념의 재정리임을 자인, (c) DAG 글은 published:false 초안. gloss 근거: 글 제목+코퍼스 사교벡터공간 4회, 사교- 계열(사교형식·사교다양체) 확립
- [ ] `topological manifold of dimension $m$` → 조정: $m$차원 위상다양체 (파생 제안 — 사용자 확인 필수) — 정의처=Topology/Compactness 정의 31 (locally Euclidean과 동일 쌍, spine Topology#16 < AT#17; AT/Topological_Manifolds 정의 2는 재사용 처리). 근거: KMS 'topological manifold=위상다양체' + 코퍼스 위상다양체 25회, '$m$차원' 수식은 자연 도출(복소차원·짝수차원 관용)
- [ ] `total Chern class` → 조정: 전체 천 특성류 (파생 제안 — 사용자 확인 필수) — 정의처=Algebraic_Topology/Characteristic_Classes 정의 6 (spine AT#17 < AV#22; AV/Chern_Classes 정의 1의 등장은 재사용 처리, AV 글은 published:false). 근거: 코퍼스 천 특성류 13회 확립(KMS '천 류' 기각 — AV 글 제목·병기 전례), total의 코퍼스 접두 전례는 전-(전공간·전순서집합·전비연결)이나 '전 천 특성류'는 '전천' 음운 충돌로 가독 저해 → '전체'로 완화한 파생. ko 위키 '천 특성류' 문서엔 total 대응어 부재. 파생이 무리라 보면 ko-빈이 차선

검수: 처리 21건 / 구획 기대치 21건 — 일치

# gloss 권고 — 위키만 도출됨 구획 (110–307행, 196건)

판정 소스 요약: 코퍼스 `<sub>` 전수 덤프(1,622종) + 대상 글 직접 문맥 확인 + kms_cache.json + ko위키 3건 실확인(삼각 분할 범주·교환자 부분군·원환 다양체). "파생·확인"은 브리프 규칙 7의 `파생 제안 — 사용자 확인 필수` 표시.

## REVIEW — 위키만 도출됨 (형태 조정 필요, 미적용) — 권고 196건
요약: 수용 19 · 조정 140 · skip 15 · ko-빈 4 · 사용자역어 0 · 보류 18

- [ ] `abelian presheaf` → 조정: 아벨 준층 — 파생·확인 (corpus 준층·분리 준층·핵 준층 + 아벨 카테고리; 대안 '가환군 준층'. 제안 '층 (수학)'은 sheaf 문서라 개념 불일치)
- [ ] `abelianization` → 조정: 아벨화 — ko위키 교환자 부분군 본문 "이를 **아벨화**라고 한다" 실확인 (문서 제목이 부분군이라 제안이 어긋났던 것)
- [ ] `acyclic on $\mathcal{M}$` → 조정: $\mathcal{M}$ 위에서 비순환 — 파생·확인 (corpus 비순환 + KMS acyclic=비순환(적); langlink 초그래프는 타분야 오연결)
- [ ] `affine algebraic group` → 조정: 아핀 대수적 군 — 같은 글이 algebraic group을 '대수적 군'으로 병기 + corpus 아핀 (제안 '선형 대수군'은 표면 불일치)
- [ ] `affine-local property` → 조정: 아핀-국소 성질 — 파생·확인 (corpus 아핀·국소적·보편성질 패턴; langlink 아핀 공간은 상위 개념)
- [ ] `algebraic $k$-cycle` → 조정: 대수적 $k$-순환 — corpus 병기 전례 그대로 (같은 글 `<sub>대수적 $k$-순환</sub>` 존재; 제안 '대수적 순환'에 $k$ 복원)
- [v 교대 2-형식 으로 진행.] `alternating $2$-형식` → skip — 혼합 표기 키(영+한)로 추출 이상 + langlink 쓰레기(슈퍼주니어); 원문 이탤릭 범위 점검 후 필요시 `alternating` 단독 재추출 권고
- [ ] `ambient` → skip — 단독 형용사(휴리스틱 5) + langlink 동음이의 문서; Batyrev 글에서 문맥어로만 쓰임
- [ ] `ample` → 조정: 풍부한 — corpus 전례 매우 풍부한×2(Complex_Geometry very ample 병기); 형용사이므로 문서명 '풍부한 가역층'에서 명사부 제거
- [ ] `associate in $A$` → 보류 — langlink 쓰레기(전문학사); '소스 없음' 구획의 `associate`와 동일 개념이므로 그쪽 판정과 통합 처리 권고
- [ ] `B-model connection` → 조정: B-model 접속 — 그 글이 B-model을 원어 유지 + 같은 글이 두브로빈 접속 참조(corpus 접속 계열); langlink(구조방정식 모델링) 쓰레기
- [ ] `basepoint-free` → 조정: 기저점 없음 — corpus 전례 그대로 (Complex_Geometry `기저점 없음<sub>base-point freeness</sub>`); 제안 '풍부한 가역층'은 다른 개념
- [ ] `basic monoid` → 조정: 기본 모노이드 — 파생·확인 (corpus 기본·모노이드; ACGS 전문용어 'basic'의 뉘앙스 사용자 판단)
- [ ] `big Givental $J$-function` → 조정: 큰 Givental $J$-함수 — corpus `Givental J-함수` 병기 + 작은 양자 코호몰로지 환의 작은/큰 전례
- [ ] `big quantum product` → 조정: 큰 양자 곱 — 파생 (corpus 작은 양자 코호몰로지 환 + 곱); 제안 '양자 코호몰로지'는 상위 문서 제목
- [ ] `Braid relation` → 조정: 꼬임 관계식 — 파생·확인 (위키 꼬임군 (위상수학) + corpus 관계식; 단 corpus 꼬임층=torsion sheaf와 표기 충돌 소지 — 땋임 대안 포함 사용자 확인)
- [ ] `canonical divisor` → 조정: 표준 인자 — 파생 (corpus 표준 선다발·표준 여과 + 카르티에 인자·베유 인자·주인자); 제안 '표준 선다발'은 divisor가 아님
- [ ] `canonical holomorphic volume form` → 조정: 표준 정칙 부피 형식 — 파생·확인 (그 글 description '부피 형식' + corpus 표준·정칙; 그 글의 '홀로모피'는 corpus 정칙과 불일치라 정칙 권고)
- [ ] `cardinal sum` → 조정: 기수 합 — 그 글 prose가 기수 사용; 문서명 '기수 (수학)'에서 용어형 도출
- [ ] `Cartan matrix` → 수용 — corpus 일반화 카르탕 행렬 병기 전례와 정합
- [v 다른 cartesian이 카테시안으로 되어있을 수 있음. 확인하고 맞추기 ] `cartesian category` → 조정: 데카르트 범주 — corpus 데카르트 병기 + 범주; 제안 '데카르트 닫힌 범주'는 closed가 붙은 다른 개념
- [ ] `Casimir operator` → 조정: 카시미르 연산자 — corpus 카시미르 원소 + 연산자 계열(축약 연산자·선형연산자); operator≠element 표면 보정
- [ ] `category fibered in groupoids` → ko-빈 — 역어 무소스('준군 올범주' 파생은 부자연); Stacks 시리즈 중심 용어라 색인 가치, epimorphism 전례로 ko 빈 값 등록
- [v 모델을 갖는 범주 (acyclic models thm에서 파생) ] `Category with models` → 보류 — langlink '모형 범주'=Quillen model category 문서로 동명이개념 오연결 (Eilenberg 'category with models'는 별개); KMS model=모형 참고해 '모형을 갖는 범주' 파생 가능하나 확인 필요
- [ ] `Cauchy` → 조정: 코시 — corpus 코시 수열 병기 전례; 제안 '오귀스탱 루이 코시'는 인물 문서 전체 제목
- [ ] `Cauchy-Riemann equation` → 수용 — 위키 exact, corpus 충돌 없음
- [ ] `central` → skip — 단독 형용사 + langlink 동음이의; 같은 글에 central idempotent<sub>중심 멱등원</sub> 병기 이미 존재
- [ ] `CFG` → skip — 그 글 자체가 정의한 약어("(이하 *CFG*)"); 병기 무의미
- [ ] `Chern polynomial` → 조정: 천 다항식 — 파생 (corpus 천 특성류·천 지표 + 특성다항식·슈어 다항식); langlink 천-사이먼스 이론은 오연결
- [ ] `Chevalley–Serre presentation` → 조정: 슈발레-세르 표시 — 같은 글 슈발레 기저 병기 + corpus 표시·최소 사영 표시; 확인: 같은 글 제목은 'Serre 관계식'(라틴 표기)이라 인명 표기 비일관 — 사용자 결정. langlink(부르바키) 쓰레기
- [ ] `Chow ring` → 조정: 저우 환 — corpus 저우 군 병기×2 + 같은 글이 §저우 군 참조; ring 표면 보정
- [ ] `closed symmetric monoidal category` → 조정: 닫힌 대칭 모노이드 범주 — corpus 대칭 모노이드 범주 병기 + 닫힌 계열; 제안에서 closed 누락 복원
- [ moduli를 모듈라이로, 나머지 단어의 moduli도 마찬가지] `coarse moduli functor` → 조정: 성긴 moduli 함자 — 같은 글 `coarse moduli space<sub>성긴 moduli 공간</sub>` 병기 전례의 혼합 표기 관례 그대로
- [ ] `cocontinuous functor` → 조정: 여연속 함자 — 파생·확인 (corpus 여완비범주(cocomplete)·여차원 등 co-=여- 계열 + 연속); langlink는 극한 문서
- [ ] `codegeneracy` → 조정: 여퇴화 — 파생·확인 (같은 글 '퇴화한' 서술 + co-=여- 계열)
- [ ] `coface` → 조정: 여면 — 파생·확인 (같은 글 face='면' 서술 + co-=여- 계열); langlink(프랑스 보험사) 쓰레기
- [ ] `cohomology functor` → 조정: 코호몰로지 함자 — 파생 (corpus 체흐/동변 코호몰로지 + 함자 다수); 제안 '유도 함자'는 다른 개념
- [ ] `coisotropic subspace` → 조정: 여등방 부분공간 — 같은 글(선형대수 쪽) coisotropic<sub>여등방적</sub> 병기 전례 + 부분공간
- [ ] `continuous functor` → 조정: 연속 함자 — 그 글이 정의하는 용어; 연속·함자 모두 코퍼스 일반 전례. langlink는 극한 문서
- [ ] `contracted` → 보류 — corpus에 수축(=retract)·축약(=tensor 축약 연산자)이 타 의미로 분점, stable map 성분 수축 의미의 확립 역어 부재
- [ ] `covering map` → 조정: 피복 사상 — corpus 피복공간 병기 + 사상; 문서명 '피복 공간'에서 map 표면 보정
- [ ] `degeneracy map` → 조정: 퇴화 사상 — 같은 글 prose "낮은 차원의 단체를 퇴화한 …로 밀어 넣는다" + 사상
- [v ko-빈 ] `derived Deligne–Mumford stack` → 조정: 유도 Deligne–Mumford stack — 확인 (corpus `유도 stack`·`아틴 stack` 혼합 표기 전례 그대로; 제안 '스택 (수학)'은 상위 문서)
- [ ] `derived pullback` → 조정: 유도 당김 — corpus 유도 스킴·유도 stack + 당김 병기 전례
- [ ] `derived sheaf-Hom` → 조정: 유도 층 $\Hom$ — 파생·확인 (유도+층+$\Hom$; `sheaf Hom` 항목과 정합)
- [ ] `diagonalize` → 수용 — corpus 대각화가능·동시대각화가능 전례와 정합; 그 글 '대각화한다' 활용 자연
- [v ko-빈 ] `Distinguished triangle` → 조정: 특별 삼각형 — ko위키 삼각 분할 범주 본문 "이 모임의 원소를 **특별 삼각형**이라고 한다" 실확인
- [ ] `DM stack` → skip — 약어 (CFG·LCH와 동일 처리); 본문에 Deligne–Mumford stack 원형 존재
- [ ] `Dubrovin connection` → 조정: 두브로빈 접속 — 그 글 제목이 '두브로빈 접속'; langlink는 양자 코호몰로지 상위 문서
- [ ] `Dynkin diagram` → 수용 — 위키 exact(딘킨 도표); corpus 한글 전례 없음, 충돌 없음
- [ ] `Eilenberg-Steenrod axiom` → 조정: 에일렌베르크-스틴로드 공리 — 표준 전사 + corpus 공리 계열(분리공리·짝 공리); langlink는 인물 문서. ko위키 해당 문서 존재는 미확인
- [ ] `embedded point` → 조정: 매장점 — 파생·확인 (corpus 매장·매장된 부분다양체 + 동반점(associated point) 조어 패턴; 제안 '으뜸 분해'는 상위 문서)
- [ ] `enough injective` → 조정: 충분한 단사 대상 — 파생·확인 (같은 글 단사 대상 병기 + '…를 갖는다' 구문)
- [ ] `enough projective` → 조정: 충분한 사영 대상 — 파생·확인 (같은 글 사영 대상 병기)
- [ ] `exact functor` → 수용 — 위키 exact(완전 함자); corpus 완전·함자 계열 정합
- [ ] `exterior $k$-bundle` → 조정: $k$차 외대수다발 — 파생·확인 (그 글 description 외대수다발 + corpus $k$차 미분형식 패턴; '$k$차' 수식이 의미상 근사임을 사용자 판단)
- [ ] `exterior algebra bundle` → 조정: 외대수다발 — 그 글 description이 '외대수다발' 사용; 문서명 '외대수'에 bundle 복원
- [ ] `face map` → 조정: 면 사상 — 같은 글 prose "…$i$번째 면을 취하며" + corpus 면; 제안 '단체 집합'은 상위 문서
- [ ] `fan` → 조정: 부채 — ko위키 원환 다양체 문서가 fan을 '부채'로 서술(웹 확인); langlink는 동음이의 문서로 빠졌던 것. 그 글은 fan 원어 유지 중 — 채택 여부 확인
- [ ] `field of rational functions` → 조정: 유리함수체 — corpus 유리함수×3 + 분수체 패턴; 제안 '분수체'는 일반 개념
- [ ] `filtered complex` → 조정: 여과 복합체 — 파생 (corpus 감소 여과·$I$-여과 + 코쥴/체흐 복합체); 제안 '스펙트럼 열'은 오연결
- [ ] `first countable` → 조정: 제1 가산 — 형용사 용어라 문서명에서 '공간' 제거; corpus 가산공리·가산 부분덮개 전례
- [ ] `Fixed point set` → 조정: 고정점 집합 — 위키 고정점 + corpus 받침 집합·지지집합 패턴
- [ ] `free animated ring` → 조정: 자유 애니메이트 환 — corpus `애니메이트 가환환` 병기 + 자유 계열; langlink(반지의 제왕) 쓰레기
- [ ] `free on $\mathcal{M}$` → 조정: $\mathcal{M}$ 위에서 자유 — 파생·확인 (corpus 자유군·자유 $A$-가군); langlink(깁스 자유 에너지) 쓰레기
- [ ] `general anticanonical section` → 보류 — anticanonical 역어 무전례; corpus에서 반-은 semi-(반단순·반군)와 contra-(반변)에 이미 과부하라 '반표준' 파생 충돌 위험
- [ ] `generalized eigenspace` → 조정: 일반화 고유공간 — 위키 일반화 고유벡터 + corpus 일반화 병기; eigenspace 표면 보정
- [ ] `generic fiber` → 조정: 일반 올 — corpus 일반점(generic point) 병기 + 올(올곱 제목) 전례
- [ ] `Genus $g$, $n$-point, degree $\beta$ Gromov-Witten invariant` → 수용 — 위키 그로모프-위튼 불변량이 head 개념과 일치; 매개변수 접두부는 병기에서 생략됨을 명시
- [ ] `geometric` → skip — 단독 형용사 + langlink '기하학' 일반 문서
- [ ] `GIT quotient` → 조정: GIT 몫 — 같은 글 기하학적 몫·범주적 몫 병기 + GIT 원어 유지 관례; 위키 전체 풀이형('기하 불변량 이론 몫')은 장황
- [ ] `global section functor` → 조정: 전역 단면 함자 — corpus 전역 방향·전역생성 + 단면 + 함자; 제안 '층 (수학)'은 상위 문서
- [ ] `globally generated` → 조정: 전역생성 — corpus 병기 전례 그대로(`<sub>전역생성</sub>` 존재); 제안 '풍부한 가역층'은 다른 개념
- [ ] `Godement sheaf` → 조정: 고드망 층 — 파생·확인 (층 + 표준 전사 고드망); 제안 '층 (수학)'은 상위 문서
- [ ] `good pair` → 조정: 좋은 쌍 — 파생·확인 (corpus 쌍 계열 + 직역; langlink(PGP) 쓰레기)
- [ ] `graded abelian group` → 조정: 등급 가환군 — corpus 등급환·등급부분가군 + 가환군×2 (같은 글 계열); 제안 '등급 대수'는 표면 불일치
- [ ] `graded homomorphism of degree $i$` → 조정: 차수 $i$의 등급 준동형 — 파생 (corpus 차수·등급·준동형 모두 전례)
- [ ] `grading operator` → 조정: 등급 연산자 — 파생 (corpus 등급 계열 + 연산자); langlink(컬러 그레이딩) 쓰레기
- [ ] `Gromov-Witten potential` → 조정: 그로모프-위튼 퍼텐셜 — 위키 그로모프-위튼 표기 + corpus Kähler 퍼텐셜; 제안 '양자 코호몰로지'는 상위 문서
- [ ] `Grothendieck pretopology` → 조정: 그로텐디크 준위상 — 파생·확인 (corpus pre-=준-(준층) + 그로텐디크 토포스 전사; 제안 '그로텐디크 위상'은 pretopology가 아님)
- [ ] `Hamiltonian vector field` → 수용 — corpus 해밀턴 작용 + 기본 벡터장 전례와 정합
- [ ] `Hartogs number` → 수용 — 위키 exact(하르톡스 수)
- [ ] `Hermitian` → skip — 단독 형용사 + corpus는 Hermitian을 원어 유지(Hermitian 계량·내적·다양체 병기 다수) — '에르미트' 병기 시 코퍼스 표기와 충돌
- [ ] `homogeneous prime ideal` → 조정: 동차 소아이디얼 — corpus 동차 아이디얼 + 소아이디얼 병기 조합; 제안 '사영 다형체'는 오연결
- [ ] `homotopy category` → 수용 — 위키 exact; corpus 호모토피 계열 정합
- [ ] `Hori-Vafa mirror` → 조정: 호리-바파 거울 — 파생·확인 (그 글 거울대칭 + 표준 전사); langlink는 인물(캄란 바파) 문서
- [ ] `Hurewicz fibration` → 조정: 후레비치 올뭉치 — 파생·확인 (위키 올뭉치 + 전사 후레비치; 그 글은 원어 유지 중)
- [ ] `IC 층` → skip — 혼합 표기 키 + IC는 약어; langlink(성남시) 쓰레기
- [ ] `inductive` → 조정: 귀납적 — corpus 귀납적 극한 병기 전례; 품사 일치(형용사). langlink '인덕션' 쓰레기
- [ ] `initial form` → 보류 — 역어 소스 부재 (corpus 주부=principal part는 타 개념, KMS 무항목); langlink '이니셜' 쓰레기
- [ ] `injective sheaf` → 수용 — 위키 exact(단사층); corpus 단사 계열 정합
- [ ] `internal $\Hom$` → 조정: 내부 $\Hom$ — 파생·확인 (corpus 내부곱 + $\Hom$ 원어 유지 관례); 제안 'Hom 함자'는 다른 개념
- [ ] `invertible sheaf` → 수용 — 위키 exact(가역층); 그 글이 invertible sheaf를 정의, corpus 가역 계열 정합
- [ ] `isotropic subspace` → 조정: 등방 부분공간 — 같은 글 isotropic<sub>등방적</sub> 병기 전례 + 부분공간; 제안 '등방성 이차 형식'은 이차형식 문서
- [ ] `J-holomorphic` → 조정: $J$-정칙 — corpus 정칙 계열(정칙함수·정칙사상); 형용사라 문서명 '정칙 함수'에서 명사부 제거
- [ ] `Killing form` → 수용 — 위키 exact(킬링 형식); 그 글은 원어 유지라 corpus 충돌 없음
- [ ] `Lagrangian subspace` → 조정: 라그랑지안 부분공간 — corpus 라그랑지안·라그랑지안 부분다양체 병기 전례
- [ ] `LCH space` → skip — 그 글 자체가 정의한 약어("줄여 *LCH space*라 적기로 한다")
- [ ] `left cancellable` → 보류 — langlink '영인자'는 zero divisor 문서로 개념 불일치; '왼쪽 소거가능' 파생은 소거 무전례(코퍼스·KMS) — ko위키 소거 법칙 확인 필요
- [ ] `left exact` → 조정: 왼쪽 완전 — 파생·확인 (corpus 왼쪽 수반함자·왼쪽 유도함자 계열 + 완전; '좌완전' 대안은 좌불변 전례 — 표기 사용자 결정)
- [ ] `left unitor` → ko-빈 — unitor 역어 무소스; 모노이드 범주 구조 용어라 색인 가치
- [ ] `limit point compact` → 조정: 극한점 옹골 — 같은 글 limit point<sub>극한점</sub> 병기 + 옹골 계열(옹골·준옹골); 확인: 같은 글 description은 '극점 옹골성' 표기 — 극한점/극점 통일 사용자 결정
- [ ] `linear system` → 수용 — 그 글 제목이 '선형계' (브리프의 자연 도출 예시 그대로)
- [ ] `linearly reductive` → 보류 — reductive 역어 미확립: 제안 '가약군'의 가약은 corpus에서 reducible(가약·완전가약) — 동음이의 충돌 (환원적 등 대안 포함 사용자 결정 필요)
- [ ] `local frame` → 보류 — frame 역어 무전례(코퍼스·KMS); '국소 틀' 파생은 임의 번역 수준. langlink '아틀라스'는 다른 개념
- [ ] `local homology group` → 조정: 국소 호몰로지 군 — 파생 (corpus 국소·호몰로지·군 모두 전례); 제안 '상대 호몰로지'는 다른 개념
- [ ] `local on target` → 보류 — target 역어 무전례('목표/공역' 파생 부자연); 속성 구절이라 skip 대안도 병기
- [ ] `locally free sheaf of rank $r$` → 조정: 랭크 $r$ 국소 자유층 — 파생·확인 (corpus rank<sub>랭크</sub> + 자유 계열 + 층; 제안 '연접층'은 다른 개념)
- [ ] `lower adjoint` → 조정: 아래 수반 — 파생·확인 (같은 글 갈루아 연결 병기 + corpus 수반, 아래로/위로 유계 패턴)
- [ ] `maximal spectrum` → 조정: 극대 스펙트럼 — corpus 극대 아이디얼·스펙트럼 병기 조합; 제안 '극대 아이디얼'은 표면 불일치
- [ ] `maximal torus` → 수용 — 그 글(원환면의 작용) 섹션 제목이 '극대 원환면'과 정확히 일치; 단 Toric 쪽 corpus는 토러스(대수적 토러스) 표기라 카테고리 간 이원 표기임을 부기
- [ ] `minimal projective presentation` → 조정: 최소 사영 표시 — 같은 글 병기 전례 그대로(`<sub>최소 사영 표시</sub>` 존재); 제안 '분해 (대수학)'은 오연결
- [ ] `Mirror domain` → 보류 — 그 글의 국소 조어(LG mirror의 정의역 $\check{X}$)로 표준 역어 부재; langlink(퍼블릭 도메인) 쓰레기
- [ ] `moduli functor` → 조정: moduli 함자 — 같은 글 '성긴 moduli 공간' 혼합 표기 관례 + 함자; 제안 '모듈라이 공간'은 corpus 무전례 표기
- [ ] `monoid of fraction` → 조정: 분수 모노이드 — corpus 분수환·분수체·분수아이디얼 패턴 + 모노이드; 제안 '반군'은 오연결
- [ ] `mutually left adjoint` → 조정: 서로 왼쪽 수반 — 파생·확인 (같은 글 수반함자 계열; langlink 자기 수반 작용소는 해석학 오연결)
- [ ] `mutually right adjoint` → 조정: 서로 오른쪽 수반 — 위와 동일
- [v ko-빈 ] `naive cotangent complex` → 조정: 소박한 여접 복합체 — 파생·확인 (같은 글 여접 복합체 병기 + naive=소박한(ko위키 소박한 집합론 전례)); langlink(헤론 공식) 쓰레기
- [ ] `nilpotency class` → 보류 — class 역어 무전례 (corpus 멱영지수는 타 개념); '멱영 계급' 파생 미확정
- [ ] `nonsingular point` → 조정: 비특이점 — corpus 특이점 병기 + 비- 계열(비순환·비퇴화·비분기); 제안은 singular 쪽 문서 제목
- [ ] `open (resp. closed)` → skip — 'resp.' 구문이 통째로 추출된 이상 키; 병기 부적합
- [ ] `open refinement` → 조정: 열린 세분 — 같은 글 세분<sub>refinement</sub> 병기 전례 + 열린 계열
- [ ] `open Richardson variety` → 조정: 열린 리처드슨 다양체 — 파생·확인 (corpus 열린 계열 + 다양체 + 표준 전사; langlink는 배우 문서)
- [v cell은 "셀"로. ] `opposite Schubert cell` → 보류 — cell 역어 무전례(그 글도 cell 원어 유지); 슈베르트 다양체 전례는 있으나 '세포/칸' 결정 필요
- [ ] `opposite Schubert variety` → 조정: 반대 슈베르트 다양체 — corpus Schubert variety<sub>슈베르트 다양체</sub> + 반대 계열(반대 카테고리·반대환); langlink는 배우 문서
- [ ] `pairwise comaximal` → 조정: 쌍마다 공최대 — 같은 글(CRT) comaximal<sub>공최대</sub> 병기 전례 그대로 + pairwise=쌍마다·확인; 제안 '서로소 아이디얼'은 정수 서로소 문서 오연결
- [ ] `parameter ideal` → 조정: 매개변수 아이디얼 — 파생·확인 (같은 글 매개계 병기 + 아이디얼; 제안 '매개계'는 system of parameters 쪽)
- [ ] `path homotopic` → 조정: 경로 호모토픽 — corpus 호모토픽×2 + 경로 병기; 제안 '호모토피'는 품사 불일치
- [ ] `perfect closure` → 조정: 완전 폐포 — corpus 완전체(perfect field) + 대수적 폐포·분리가능폐포 패턴
- [ ] `perfect ring` → 조정: 완전환 — 그 글 섹션 제목이 '## 완전환'; langlink '반완전환'은 모듈론(Bass) 문서로 오연결
- [ ] `perfectly $T_4$-space` → 보류 — corpus `완전 $T_4$-공간`은 **completely** $T_4$의 병기(실확인)라 perfectly에 재사용하면 충돌; perfectly 계열 역어 미확정
- [ ] `perfectly normal space` → 보류 — 위와 동일 (corpus 완전정규공간=completely normal space 병기와 충돌)
- [ ] `Peterson variety` → 조정: 피터슨 다양체 — 파생·확인 (다양체 + 표준 전사; langlink는 배우 문서)
- [ ] `polynomial algebra` → 조정: 다항식 대수 — 파생 (corpus 군대수·몫대수·$A$-대수 + 다항식 계열); 제안 '다항식환'은 ring 쪽 표면
- [ ] `positive nilpotent subalgebra` → 조정: 양의 멱영 부분대수 — 파생 (corpus 양의·멱영·부분대수 모두 전례); 제안 '카르탕 부분 대수'는 다른 개념
- [ ] `positive root` → 조정: 양의 근 — 파생 (corpus 양의 병기 + 단순근 전례의 근); 제안 '근계'는 상위 문서
- [ ] `primary` → skip — 단독 형용사 + langlink 동음이의 문서
- [ ] `principal cycle` → 조정: 주순환 — 같은 글 병기 전례 그대로(`principal cycle<sub>주순환</sub>` 존재); langlink(달의 위상) 쓰레기
- [ ] `pullback sieve` → 조정: 당김 체 — 같은 글 sieve<sub>체</sub>·covering sieve<sub>덮개 체</sub> 병기 전례 + corpus 당김
- [ ] `Quadratic relation` → 조정: 이차 관계식 — 파생 (corpus 관계식 + 이차 표준 어휘); 제안 '이차 방정식'은 equation 오연결
- [ ] `R-polynomial` → 조정: $R$-다항식 — 파생 (corpus 최소다항식·특성다항식·슈어 다항식 계열)
- [ ] `rank r vector bundle` → 조정: 랭크 $r$ 벡터다발 — corpus rank<sub>랭크</sub> + 벡터다발 병기·확인 (그 글은 rank 원어 유지 중); 제안은 $r$ 상실
- [ ] `rational` → 조정: 유리 — corpus '강하게 볼록한 유리 다각형뿔' 병기의 유리 전례 (Delzant 조건 rational과 동일 용법); langlink '합리성'은 비수학 오연결
- [ ] `reductive` → skip — 단독 형용사 + 역어 미확립(linearly reductive 참조); langlink '리덕션' 쓰레기
- [ ] `regular sequence` → 수용 — 위키 exact(정칙렬); corpus 정칙 계열 정합
- [ ] `relative homology` → 수용 — 위키 exact; corpus 상대 호모토피 군 전례 정합
- [ ] `representing object` → 조정: 표현 대상 — corpus 표현 가능한 함자·표현가능 + 대상 계열(시작/끝/단사/사영 대상); 제안은 functor 쪽 문서
- [ ] `restricted sum` → 조정: 제한합 — 그 글 제목이 '제한합'; langlink(아이버슨 괄호) 쓰레기
- [ ] `Richardson variety` → 조정: 리처드슨 다양체 — 파생·확인 (다양체 + 표준 전사; langlink는 배우 문서)
- [ ] `Riemann–Roch dimension` → 조정: 리만-로흐 차원 — 파생 (위키 리만-로흐 표기 + corpus 차원); 제안 '리만-로흐 정리'는 표면 불일치
- [ ] `right almost split` → 조정: 오른쪽 거의 분할 — 같은 글 거의 분할 수열 병기 + 오른쪽 계열; langlink(극우 정치) 쓰레기
- [ ] `right cancellable` → 보류 — left cancellable과 동일 사유
- [ ] `right exact` → 조정: 오른쪽 완전 — left exact와 동일·확인
- [ ] `right unitor` → ko-빈 — left unitor와 동일
- [ ] `root system` → 수용 — 그 글 제목·섹션이 '근계'
- [ ] `second countable` → 조정: 제2 가산 — first countable과 동일 (공간 제거, 품사 일치)
- [ ] `semi-perfect ring` → 보류 — 그 글 정의는 표수 $p$ Frobenius 전사 의미인데 langlink '반완전환'은 모듈론 Bass semiperfect 문서(동명이개념); '반완전환' 파생 시 색인 충돌 여부 사용자 판단
- [ ] `semigroup algebra` → 조정: 반군 대수 — corpus 반군 병기 + 군대수 패턴; 제안 '반군'은 algebra 상실
- [ ] `separable element` → 조정: 분리가능 원소 — 그 글 제목 분리가능확대체 + corpus 분리가능차수·분리가능폐포 계열; 확인: corpus에 분해가능확대 표기 혼재. 제안 '분해 가능 확대'는 extension 쪽
- [ ] `Serre fibration` → 조정: 세르 올뭉치 — 파생·확인 (위키 올뭉치 + 전사; 그 글은 원어 유지 중)
- [ ] `Serre relation` → 조정: Serre 관계식 — 그 글 제목 'Serre 관계식' 그대로 (세르 관계식 전면 한글화는 사용자 결정); 제안 '반단순 리 대수'는 상위 문서
- [ ] `sheaf Hom` → 조정: 층 $\Hom$ — 파생·확인 (corpus 층 + $\Hom$ 원어 유지 혼합 표기 전례); 제안 '층 (수학)'은 상위 문서
- [ ] `sheaf of relative differentials` → 조정: 상대 미분층 — 파생·확인 (corpus 상대 계열 + 캘러 미분가군·아이디얼층 패턴); 제안 '켈러 미분'은 표면 불일치
- [ ] `shift functor` → 조정: 이동 함자 — 파생·확인 (같은 글 prose "$n$칸 이동시키는" + 함자; ko위키 삼각 분할 범주는 '자기 동치'로만 지칭해 소스 없음)
- [ ] `simplicial identity` → 조정: 단체 항등식 — 같은 글 단체 표기 전례 + 항등식; 제안 '단체 집합'은 다른 개념
- [ ] `simplicial module` → 조정: 단체 가군 — 같은 글 단체 표기 + corpus 가군; 제안 '단체 가환환'은 표면 불일치
- [ ] `simplicial object` → 조정: 단체 대상 — 같은 글 단체 표기 + corpus 대상 계열
- [ ] `simplicial set` → 수용 — 위키 exact(단체 집합); 같은 글이 단체 표기 사용
- [ ] `simply-laced` → ko-빈 — 역어 무소스(제안 '딘킨 도표'는 상위 문서); 그 글이 정의하는 용어라 색인 가치
- [ ] `small` → skip — 단독 형용사; corpus 작은 범주 병기는 small category 전체에 대한 것
- [ ] `small quantum product` → 조정: 작은 양자 곱 — corpus 작은 양자 코호몰로지 환 병기 + 곱; 제안은 상위 문서 제목
- [ ] `solvability class` → 보류 — nilpotency class와 동일 사유 (class 역어 무전례); langlink(단간론파) 쓰레기
- [ ] `stalk-local` → 조정: 줄기-국소 — 파생·확인 (corpus 줄기(stalk) 병기 + 국소); langlink(스토커 게임) 쓰레기
- [ ] `standard étale` → 조정: 표준 에탈 — corpus 표준 계열 + 에탈 병기; 제안 '에탈 사상'에서 standard 복원·사상 제거
- [ ] `strongly convex` → 조정: 강하게 볼록 — corpus '강하게 볼록한 유리 다각형뿔' 병기 전례 그대로; langlink '볼록 함수'는 해석학 강볼록으로 오연결
- [ ] `subsheaf` → 조정: 부분층 — corpus 부분- 계열(부분군·부분환·부분가군) + 층; langlink '초함수' 쓰레기
- [ ] `symmetric Euler form` → 조정: 대칭 오일러 형식 — 같은 글 Euler form<sub>오일러 형식</sub> 병기 + 대칭 계열; langlink(유체 오일러 방정식) 쓰레기
- [ ] `symplectic complement` → 조정: 사교 여공간 — 그 글 제목 사교벡터공간(사교 표기) + corpus 직교여공간 패턴
- [ ] `symplectic subspace` → 조정: 사교 부분공간 — 그 글 사교 표기 + 부분공간
- [ ] `tangent covector` → 조정: 여접벡터 — 같은 글 여접공간 병기 + corpus 접벡터; 제안 '공변접다발'은 corpus 여접 계열(여접공간·여접다발)과 충돌
- [ ] `Tautological bundle` → 조정: 보편 선다발 — 파생·확인 (그 글 line bundle=선다발 표기 + 위키 보편- 계열; '가역층'은 corpus에서 invertible sheaf 전용. 단 universal bundle=보편다발과 표기 근접 — 사용자 확인)
- [ ] `tautological line bundle` → 조정: 보편 선다발 — 위와 동일 (같은 글의 같은 대상 $\mathcal{O}(-1)$)
- [ ] `total complex` → 조정: 전복합체 — 파생·확인 (corpus 전공간(total space) 패턴 + 복합체; 대안 '전체 복합체'. langlink 전허 수체는 쓰레기)
- [ ] `trace map` → 조정: 대각합 사상 — corpus `대각합<sub>trace</sub>` 병기 전례(선형대수) + 사상; langlink 동음이의 문서
- [ ] `transversely intersect` → 보류 — transversal 역어 무전례(그 글도 원어 유지, KMS 무항목); langlink '엇각'은 초등기하 오연결
- [ ] `Triangulated category` → 수용 — 위키 exact(삼각 분할 범주); corpus 삼각 분해는 리 대수 쪽 타 개념이라 충돌 없음
- [ ] `two-variable adjunction` → 조정: 이변수 수반 — 파생·확인 (corpus 수반 계열 + 쌍함자 패턴); langlink(모나드) 쓰레기
- [ ] `uniformizing parameter` → 조정: 균등화원 — 같은 글이 동의어 uniformizer를 '균등화원'으로 병기한 전례 그대로; 제안 '이산 값매김환'은 DVR 문서
- [ ] `uniform하게` → skip — 혼합 표기 키(추출 이상); langlink(트와이스) 쓰레기
- [ ] `universal $A$-derivation` → 조정: 보편 $A$-미분 — corpus `$(A,\varepsilon)$-미분` 병기 + KMS derivation=미분 + 보편 계열; langlink(보편적 건강보장) 쓰레기
- [ ] `universal element` → 조정: 보편 원소 — 파생 (corpus 보편성질·보편다발 + 원소); 제안 '표현 가능 함자'는 상위 문서
- [ ] `upper adjoint` → 조정: 위 수반 — lower adjoint와 동일·확인
- [ ] `vanishing scheme` → 조정: 영점 스킴 — 파생·확인 (corpus 스킴 + 영점은 표준 어휘이나 코퍼스 병기 무전례); langlink(폰지 사기) 쓰레기
- [ ] `virtual 차원` → skip — 혼합 표기 키; corpus는 virtual을 원어 유지(virtual relative dimension 병기 전례)
- [ ] `weight decomposition` → 조정: 무게 분해 — corpus 무게·최고무게·무게 가군 계열 + 분해 계열; 그 글(원환면의 작용)이 정의하는 용어. 제안 '분해'는 동음이의 문서
- [ ] `Whitney sum formula` → 조정: 휘트니 합 공식 — corpus 슈티펠-휘트니 특성류 병기 + 합·공식; langlink(만-위트니 U 검정) 쓰레기

검수: 처리 196건 / 구획 기대치 196건

## 특기 사항 (사용자 이탈 체크 우선 대상)

1. **perfectly 계열 충돌 발견**: corpus `완전 $T_4$-공간`·`완전정규공간`은 *completely* $T_4$/*completely* normal의 병기였다 (Separation 계열 글에서 실확인). perfectly normal에 '완전'을 재사용하면 completely와 충돌 → 두 건 모두 보류.
2. **ko위키 실확인 3건**: distinguished triangle=특별 삼각형, abelianization=아벨화, fan=부채(원환 다양체 문서). shift functor는 ko위키에 고유 명칭 없음('자기 동치').
3. **langlink 쓰레기 다수**(슈퍼주니어·성남시·트와이스·폰지 사기 등): 대부분 corpus 파생으로 구제했고, 구제 불가한 것만 보류/skip.
4. **동명이개념 오연결 보류**: Category with models(≠Quillen model category), semi-perfect ring(표수 p ≠ Bass), linearly reductive(가약=reducible 충돌), strongly convex는 corpus 전례로 구제.
5. **혼합 표기 키 4건 skip**: `alternating $2$-형식`·`IC 층`·`uniform하게`·`virtual 차원` — 추출 이상, 원문 이탤릭 범위 점검 권고.

# REVIEW — 소스 없음 — 권고 129건

요약: 수용 0 · 조정 82 · skip 25 · ko-빈 12 · 사용자역어 8 · 보류 2

파생 표기 원칙: `(파생 — 확인 필수)`가 붙은 조정안은 전부 코퍼스 전례 조합으로만 만든 것.
직접 전례(글 자체 병기·prose 사용례)가 있는 항목은 태그 없이 전례를 인용.

- [ ] `almost split sequence` → 조정: 거의 분할 수열 — 글 자체가 이미 `<sub>거의 분할 수열</sub>` 병기 (AR 이론 글).
- [ ] `annihilate` → skip — 동사 용법("$\mathcal{D}$를 annihilate한다"), 병기 어색 부류. 코퍼스 '소멸' prose는 vanish 뜻이라 유용 불가.
- [v 보류 ] `associate` → 조정: 동반원 (파생 — 확인 필수) — associated→동반은 `associated prime ideal<sub>동반소아이디얼</sub>` 전례, 원=원소.
- [ ] `associated graded` → 조정: 동반 등급 (파생 — 확인 필수) — 동반소아이디얼(associated→동반) + `graded ring<sub>등급환</sub>`. '연관 등급'이 통용어이나 코퍼스 전례는 동반.
- [ ] `associated graded module` → 조정: 동반 등급가군 (파생 — 확인 필수) — 위 + '등급환 위의 등급가군' (등급환 글 description).
- [ ] `associated graded ring` → 조정: 동반 등급환 (파생 — 확인 필수) — 위와 동일 조합. 3항목 일괄 결정 필요.
- [ ] `associator` → 조정: 결합자 (파생 — 확인 필수) — `commutator<sub>교환자</sub>`의 -자 패턴 + '결합법칙을 만족한다' 병기 전례.
- [ ] `augmentation map` → 조정: 첨가 사상 (파생 — 확인 필수) — 선형대수 글들의 '첨가행렬'(augmented matrix) + 사상.
- [ ] `Auslander–Reiten quiver` → ko-빈 — quiver 역어 부재 (코퍼스는 "quiver, 곧 유향그래프" — quiver 영어 유지). 색인 가치는 있음.
- [ ] `Auslander–Reiten sequence` → 조정: Auslander–Reiten 수열 (파생 — 확인 필수) — 'Cauchy 수열' PropName+수열 패턴 + 같은 문장의 거의 분할 수열 병기.
- [ ] `Auslander–Reiten translate` → 조정: AR 변환 — 글 자체가 이미 `<sub>AR 변환</sub>` 병기.
- [v ko-빈 ] `Bar involution` → 조정: bar 대합 (파생 — 확인 필수) — `involutive<sub>대합적</sub>` + 'pullback 함자'류 라틴+한글 혼성 패턴.
- [기저점? 따로 이야기하자.] `base locus` → 사용자 역어 필요 — 코퍼스 '자취'는 곡선 자취(calculus) 용법뿐, base 쪽 역어(기저/기점) 미정 — 파생 무리.
- [ ] `bimonoid` → 조정: 쌍모노이드 (파생 — 확인 필수) — bi→쌍은 `biregular<sub>쌍정칙</sub>` 전례 + `monoid<sub>모노이드</sub>`.
- [ ] `birational map` → 조정: 쌍유리 사상 (파생 — 확인 필수) — `biregular morphism<sub>쌍정칙사상</sub>` + 유리함수. 오늘 쌍정칙 룰링과 정합.
- [ ] `birationally equivalent` → 조정: 쌍유리 동치 (파생 — 확인 필수) — 위 + Chow 군 글의 `<sub>유리 동치</sub>` 병기.
- [ ] `cardinal product` → 조정: 기수 곱 (파생 — 확인 필수) — 그 글 스스로 "기수들 사이의 합과 곱"·§기수들 사이의 연산.
- [ ] `category of elements` → 조정: 원소들의 범주 (파생 — 확인 필수) — 원소·범주 모두 코퍼스 편재 (해당 글 prose는 '카테고리' — 표기 통일 겸사 확인).
- [ ] `charge matrix` → ko-빈 — 물리 유래 MS 연구 용어, '전하' 코퍼스 미출현.
- [ ] `classifying stack` → 조정: 분류 스택 (파생 — 확인 필수) — `classifying space<sub>분류공간</sub>` + `stack<sub>스택</sub>`.
- [ ] `cocone` → 사용자 역어 필요 — co- 접두 처리 미확정 (코퍼스는 여핵·여접 대 쌍대- 병존), cone→뿔과의 결합('여뿔')이 모두 어색.
- [ ] `commutation factor` → 보류: factor 역어 '인자'가 코퍼스에서 divisor 전용(베유 인자·주인자) — '교환 인자' 파생 시 교차 충돌 의심.
- [ ] `comodule structure` → ko-빈 — comodule 역어 부재 ('여가군' 조어는 전례 없음), GIT 글 색인 가치.
- [ ] `compact form` → 조정: 콤팩트 형식 (파생 — 확인 필수) — prose '콤팩트 Kähler'류 + '(p,q)-형식'. 위상 글들의 '옹골'과 이원 표기인 점 유의.
- [ ] `compactifiable` → 조정: 옹골화 가능 (파생 — 확인 필수) — `one-point compactification<sub>일점 옹골화</sub>`.
- [ ] `complete linear system` → 조정: 완비 선형계 (파생 — 확인 필수) — `complete<sub>완비</sub>` + 선형계(오늘 위키 구획 수용분). '완전 선형계' 대안 있음 — complete→완비 코퍼스 매핑을 따랐음.
- [ ] `cosupport 조건` → skip — 용어 자체가 이미 한국어 혼성 표기, 병기 대상 아님.
- [ ] `Cox ring` → 조정: Cox 환 (파생 — 확인 필수) — 'Chow 환'·'valuation 환' PropName+환 패턴.
- [ ] `Coxeter functor` → 조정: Coxeter 함자 — 코퍼스에 "Coxeter 함자" 사용례가 이미 존재 (reflection functor 글).
- [ ] `de Rham 미분` → skip — 이미 한국어 혼성 표기.
- [ ] `Deligne–Mumford stack` → 조정: Deligne–Mumford 스택 (파생 — 확인 필수) — `stack<sub>스택</sub>` + PropName 패턴.
- [ ] `derived prestack` → ko-빈 — `prestack<sub>준스택</sub>`은 전례 있으나 DAG의 derived 역어 부재(유도범주 미출현, 코퍼스도 derived 영어 유지).
- [ ] `dominant` → skip — 형용사 조건 단독어 (smooth·proper 부류), 코퍼스 역어 없음.
- [ ] `dual representation` → 조정: 쌍대 표현 (파생 — 확인 필수) — `dual basis<sub>쌍대기저</sub>` + `representation<sub>표현</sub>`·부분표현.
- ["카르티에" ] `effective Cartier divisor` → 조정: 유효 Cartier 인자 (파생 — 확인 필수) — `effective<sub>유효</sub>` + `Weil divisor<sub>베유 인자</sub>` 패턴.
- [ ] `equivariant` → skip — 형용사 조건 단독어, '등변' 코퍼스 미출현.
- [ ] `exact` → 조정: 완전 — 단독 형용사이나 완전열·'완전 교차' 등 코퍼스 확립 역어 있음 (휴리스틱 5 단서).
- [ ] `fiberwise Gromov–Witten 불변량` → skip — 이미 한국어 혼성 표기 (연구 스트림 용어).
- [ ] `filter base` → 조정: 필터 기저 (파생 — 확인 필수) — [집합론] §필터와 아이디얼 + `basis<sub>기저</sub>`.
- [ ] `flag variety` → 조정: 깃발 다양체 (파생 — 확인 필수) — `flag<sub>깃발</sub>` + 'Toric 다양체'·슈베르트 다양체 패턴.
- [ ] `fpqc 위상` → skip — 이미 한국어 혼성 표기.
- [ ] `functor of points of $X$` → 조정: $X$의 점 함자 (파생 — 확인 필수) — `point<sub>점</sub>` + 'Hom 함자' 패턴; terms.yml 변수 포함 전례($A$-대수) 있음.
- [ ] `fundamental groupoid` → 조정: 기본 준군 (파생 — 확인 필수) — 기본군 + `groupoid<sub>준군</sub>`.
- [ ] `Gauss-Manin connection` → 조정: Gauss-Manin 접속 (파생 — 확인 필수) — 'Levi-Civita 접속'·'Chern 접속' 직접 패턴.
- [ ] `Genus $g$, $n$-marked, $\beta$-class stable map` → skip — 변수 나열 정의구, 용어형 부적합 (stable map 자체는 별도 색인 대상).
- [ ] `global frame` → 사용자 역어 필요 — `orientation<sub>전역 방향</sub>`으로 global→전역은 전례 있으나 frame 역어(틀) 미출현; local frame과 짝으로 결정 필요.
- [ ] `gravitational descendant` → ko-빈 — GW 연구 용어, 국문 역어 관례 부재.
- [ ] `Grothendieck 위상` → skip — 이미 한국어 혼성 표기.
- [ ] `Hamiltonian $G$-공간` → skip — 이미 한국어 혼성 표기.
- [ ] `Hessenberg variety` → 조정: Hessenberg 다양체 (파생 — 확인 필수) — 'Hermitian 다양체'·`Schubert variety<sub>슈베르트 다양체</sub>` 패턴.
- [ ] `homogeneous coordinate ring` → 조정: 동차 좌표환 (파생 — 확인 필수) — `동차원소`·`동차 아이디얼` + `coordinate ring<sub>좌표환</sub>`.
- [ ] `homological $\delta$-functor` → 조정: 호몰로지 $\delta$-함자 (파생 — 확인 필수) — [호몰로지 대수학] 분야명 + 'Ext 함자'류 혼성 패턴.
- [ ] `homologous` → skip — 이 글의 자체 용법(호몰로지가 동형인 두 공간)이 표준 어법과 달라 역어 고정 부적절, 형용사 조건.
- [ ] `internal weak direct product` → 조정: 내부 약한 직접곱 (파생 — 확인 필수) — `inner automorphism<sub>내부자기동형사상</sub>` + 군의 직접곱 + prose '약한'.
- [ ] `intersection cohomology 층` → skip — 이미 한국어 혼성 표기 (IC 층 병기 존재).
- [ ] `intersection form` → 조정: 교차 형식 (파생 — 확인 필수) — prose '완전 교차'(complete intersection) + '(p,q)-형식'.
- [ ] `invariant ring` → 사용자 역어 필요 — '불변환'은 '변환' 오독 위험, 불변식환 등 대안 중 사용자 결정 필요 (좌불변 전례만으로 파생 무리).
- [ ] `inverse image sheaf` → 조정: 역상층 (파생 — 확인 필수) — `preimage<sub>역상</sub>`·예외 역상 + 준연접층류 합성.
- [ ] `Irrelevant ideal` → 조정: 무관 아이디얼 (파생 — 확인 필수) — prose '무관' + `two-sided ideal<sub>양쪽 아이디얼</sub>`·동차 아이디얼.
- [ ] `isolated hypersurface singularity` → 조정: 고립 초곡면 특이점 (파생 — 확인 필수) — `isolated singularity<sub>고립특이점</sub>` + `hypersurface<sub>초곡면</sub>`.
- [ ] `Isom presheaf` → 조정: Isom 준층 (파생 — 확인 필수) — [위상수학] §준층 + 기호 접두 혼성 패턴(t-구조·Hom 함자).
- [ ] `Iwahori–Hecke algebra` → 조정: Iwahori–Hecke 대수 (파생 — 확인 필수) — 'Hall 대수'·'Lie 대수' PropName+대수 패턴.
- [ ] `Jordan block` → 조정: 조르당 블록 — 같은 글 prose에 "조르당 블록" 사용례 이미 존재.
- [ ] `Laplace 방정식` → skip — 이미 한국어 혼성 표기.
- [ ] `lattice polytope` → 조정: 격자 다면체 (파생 — 확인 필수) — `lattice<sub>격자</sub>` + `reflexive polytope<sub>반사 다면체</sub>`.
- [ ] `left almost split` → 조정: 왼쪽 거의 분할 (파생 — 확인 필수) — `left coset<sub>왼쪽 잉여류</sub>` + 같은 글의 거의 분할 수열 병기.
- [ ] `left compatible` → 조정: 왼쪽 호환 (파생 — 확인 필수) — prose '서로 호환되는' + 왼쪽 아이디얼·왼쪽 잉여류. 형용사 조건이라 skip 대안도 가능.
- [ ] `Lichtenbaum–Schlessinger functor` → 조정: Lichtenbaum–Schlessinger 함자 (파생 — 확인 필수) — 'Coxeter 함자' 사용례 패턴.
- [ ] `linearly disjoint` → ko-빈 — 체론 색인 가치는 있으나 '일차 서로소'류 파생이 모두 어색 (일차독립·서로소 전례는 각각 존재).
- [ ] `local coefficient system` → 조정: 국소 계수 체계 (파생 — 확인 필수) — `directed system<sub>유향체계</sub>`의 system→체계 + prose '계수'.
- [ ] `locally $P$` → skip — 변수 포함 형용사 조건, 용어형 부적합.
- [ ] `locally closed embedding` → 조정: 국소 닫힌 매장 (파생 — 확인 필수) — prose '열린 매장' 다수 + 닫힌집합.
- [ ] `locally principal` → skip — 형용사 조건('국소 주' 병기 어색), 주인자 전례는 있으나 서술어로만 쓰임.
- [ ] `log Calabi-Yau pair` → 조정: 로그 Calabi-Yau 쌍 (파생 — 확인 필수) — `log structure<sub>로그 구조</sub>` + 같은 글 prose "쌍 $(Y,D)$".
- [ ] `log scheme` → 조정: 로그 스킴 (파생 — 확인 필수) — `<sub>로그 구조</sub>` + [스킴] 분야명.
- [ ] `mapping cone` → 조정: 사상뿔 (파생 — 확인 필수) — `morphism<sub>사상</sub>` + 원뿔·`affine cone<sub>아핀 뿔</sub>`.
- [ ] `minimal length coset representatives` → 조정: 최소 길이 잉여류 대표원 (파생 — 확인 필수) — 최소다항식·`length<sub>길이</sub>`·왼쪽 잉여류·prose '대표원' 전례 전부 존재.
- [ ] `monodromy functor` → ko-빈 — '모노드로미' 코퍼스 미출현, 음차 단독 신설은 회피 (색인 가치는 있음).
- [ ] `negative nilpotent subalgebra` → 조정: 음의 멱영 부분대수 (파생 — 확인 필수) — prose '음의 방향' + `nilpotent<sub>멱영</sub>` + 카르탕 부분대수.
- [ ] `non-degenerate pairing` → skip — 직전 문장에서 도입된 요소들의 조합 용어라 병기 중복; pairing은 코퍼스가 영어 유지.
- [ ] `nondegeneracy` → 조정: 비퇴화성 (파생 — 확인 필수) — `non-degenerate<sub>비퇴화</sub>` + -성 명사화(반단순성·가해성 prose 전례). 명사 용법이라 ~성 적합.
- [ ] `normal fan` → ko-빈 — fan 역어 부재 (코퍼스 전체가 fan 영어 유지), 토릭 색인 가치.
- [ ] `Novikov variable` → 조정: Novikov 변수 — 코퍼스에 "Novikov 변수" 사용례 이미 존재.
- [ ] `open submanifold` → 조정: 열린 부분다양체 (파생 — 확인 필수) — 열린집합 + `embedded submanifold<sub>매장된 부분다양체</sub>`.
- [ ] `oriented vector bundle` → 보류: 코퍼스 '유향'은 directed 전용(유향그래프·유향체계)이라 '유향 벡터다발' 파생 시 충돌 의심 — 그 글 prose는 '방향'(전역 방향) 사용, 방향/유향 중 사용자 판단 필요.
- [ ] `parabolic subgroup` → ko-빈 — 색인 가치 크나 '포물' 파생은 코퍼스 포물선(곡선) 동음이의 위험 (휴리스틱 4).
- [ ] `partial mapping` → 조정: 편사상 (파생 — 확인 필수) — 편미분의 partial=편(한 변수 고정, 뜻 일치); '부분 사상'은 부분정의 함수 뜻과 혼동 위험.
- [ ] `perverse t-structure` → 조정: perverse t-구조 (파생 — 확인 필수) — `perverse 층<sub>perverse sheaf</sub>` 혼성 전례 + `t-structure<sub>t-구조</sub>`.
- [ ] `plus construction` → 조정: plus 구성 (파생 — 확인 필수) — prose '구성'(자유곱의 구성 등) + 라틴+한글 혼성 패턴. 근거 약한 편 — ko-빈 대안 가능.
- [ ] `Plücker embedding` → 조정: Plücker 매장 (파생 — 확인 필수) — `embedding<sub>매장</sub>` + PropName 패턴.
- [ ] `positive norm` → 조정: 양의 노름 (파생 — 확인 필수) — prose '양의 방향' + `norm<sub>노름</sub>`.
- [ ] `principal Cartier divisor` → 조정: 주 Cartier 인자 (파생 — 확인 필수) — `principal divisor<sub>주인자</sub>` + 베유 인자 패턴.
- [ ] `properly intersect` → skip — 동사구 병기 어색 부류 (`proper direct image<sub>고유 받음</sub>`으로 proper→고유 전례는 있음).
- [ ] `pseudoholomorphic` → 조정: 유사정칙 (파생 — 확인 필수) — `Moore-Penrose pseudoinverse<sub>유사역행렬</sub>`(pseudo→유사) + `holomorphic function<sub>정칙함수</sub>`.
- [ ] `pure codimension $1$` → skip — 변수 포함 형용사 조건, 용어형 부적합.
- [ ] `rationally equivalent` → 조정: 유리 동치 — 글 자체가 이미 `<sub>유리 동치</sub>` 병기.
- [ ] `reduced scheme structure` → 사용자 역어 필요 — reduced 역어 미확립 (스킴·구조는 전례 있으나 reduced 결정이 여러 용어에 파급).
- [ ] `related family` → 사용자 역어 필요 — Bourbaki 용어, related 역어 부재 (족·자유 전례만으로 파생 무리).
- [ ] `relative trace` → 조정: 상대 trace (파생 — 확인 필수) — `relative homotopy group<sub>상대 호모토피 군</sub>` + trace는 코퍼스가 영어 유지("trace의 교대합") — 혼성 유지가 코퍼스 정합.
- [ ] `restriction map` → 조정: 제한 사상 — 코퍼스 prose 사용례 이미 존재 ("첫 줄의 제한 사상 $\rho$").
- [ ] `Riemann 적분가능` → skip — 이미 한국어 혼성 표기.
- [ ] `right compatible` → 조정: 오른쪽 호환 (파생 — 확인 필수) — left compatible과 일괄 (오른쪽 잉여류·오른쪽 아이디얼).
- [ ] `scheme-theoretic image` → ko-빈 — '~론적' 조어(스킴론적)는 무리 (범주론적 전례는 분야명 한정), 색인 가치.
- [ ] `Schubert cell` → 사용자 역어 필요 — 슈베르트 다양체 전례로 '슈베르트'는 확정이나 cell 역어(세포 등) 코퍼스 미출현.
- [ ] `semi-locally simply connected` → 조정: 반국소 단순연결 (파생 — 확인 필수) — semi→반(반단순·반안정) + 단순연결공간.
- [ ] `semisimple` → 조정: 반단순 — 코퍼스 prose 확립 ("반단순 Lie algebra"·반단순성 판정법). 단독 형용사지만 확립 역어 단서 적용.
- [ ] `semistable` → 조정: 반안정 — 코퍼스 prose "안정·반안정 bundle로 제한" 사용례.
- [ ] `set-값 moduli functor` → skip — 이미 한국어 혼성 표기 (주 용어 coarse moduli functor 쪽에서 처리).
- [ ] `sheafification functor` → 조정: 층화 함자 (파생 — 확인 필수) — `sheafification<sub>층화</sub>` + 함자.
- [ ] `sifted colimit completion` → ko-빈 — ∞-범주 연구 용어, 역어 관례 부재.
- [ ] `simple normal crossing divisor` → 조정: 단순 정규교차 인자 (파생 — 확인 필수) — `simple<sub>단순</sub>`·정규(정규공간·정규환)·교차·인자 조합. crossing→교차가 intersection→교차와 겹치는 점만 유의.
- [ ] `Sink에서의 reflection functor` → skip — 이미 한국어 혼성 표기.
- [ ] `SNC divisor` → skip — 약어 (본 용어 항목에서 처리, 약어 병기 무의미).
- [ ] `Source에서의 reflection functor` → skip — 이미 한국어 혼성 표기.
- [ ] `specialization` → 조정: 특수화 — 코퍼스 prose 사용례 다수 + 같은 문장 짝 용어 `generalization<sub>일반화</sub>` 병기와 대구.
- [ ] `superpotential` → ko-빈 — MS 연구 용어; 코퍼스 '초'는 hyper(초곡면) 전용이라 super 파생 근거 없음.
- [ ] `symmetor` → 조정: 대칭자 (파생 — 확인 필수) — 교환자 -자 패턴 + `symmetric<sub>대칭적</sub>`. 영어 원어 자체가 비표준 조어라 ko-빈 대안도 가능.
- [ ] `symmetric power` → 조정: 대칭 거듭제곱 (파생 — 확인 필수) — 같은 글 `<sub>대칭텐서</sub>` + prose '거듭제곱'. 통용어 '대칭멱'은 멱 단독 전례 부족(멱영뿐).
- [ ] `symplectomorphism` → 조정: 사교동형사상 (파생 — 확인 필수) — 사교다양체·사교기하 prose + `diffeomorphism<sub>미분동형사상</sub>` 형성 평행.
- [ ] `tangent cone` → 조정: 접뿔 (파생 — 확인 필수) — 접공간·여접다발(tangent→접) + 원뿔·아핀 뿔(cone→뿔).
- [ ] `transport map` → 사용자 역어 필요 — '수송' 코퍼스 미출현, 파생 근거 없음.
- [ ] `trivial extension` → 조정: 자명한 확장 (파생 — 확인 필수) — prose '자명' 편재 + [군론] §군의 확장. 오늘 중심확장 룰링(확장)과 정합.
- [ ] `twisted inverse image` → 조정: 비틀린 역상 (파생 — 확인 필수) — prose '비틀어'·'뒤틀린' + 역상. 같은 문장의 주 역어는 예외 역상이라 skip(동의어 무병기) 대안도 가능.
- [ ] `unimodular` → skip — 형용사 조건 단독어, 같은 절에서 smooth의 동의어로만 제시됨.
- [ ] `universal $\delta$-functor` → 조정: 보편 $\delta$-함자 (파생 — 확인 필수) — '보편 포락 대수'·보편 성질 + Ext 함자 혼성 패턴.
- [ ] `Verdier dual` → 조정: Verdier 쌍대 (파생 — 확인 필수) — 푸앵카레 쌍대성·쌍대기저 + PropName 패턴.
- [ ] `weak direct product` → 조정: 약한 직접곱 (파생 — 확인 필수) — prose '약한' + 군의 직접곱·가군의 직접곱.
- [ ] `weight $\lambda$의 weight space` → skip — 이미 한국어 혼성 + 변수 포함 (weight space 본 항목에서 처리).
- [ ] `weight space` → 조정: 무게 공간 (파생 — 확인 필수) — `weight<sub>무게</sub>`·최고무게 + 공간.

검수: 처리 129건 / 구획 기대치 129건
