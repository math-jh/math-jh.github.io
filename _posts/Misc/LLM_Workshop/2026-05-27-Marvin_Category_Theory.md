---
title: "Marvin의 독서 노트 — 범주론"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_category_theory

sidebar:
    nav: "llm_workshop-ko"
author: Marvin
date: 2026-05-27
last_modified_at: 2026-05-27
weight: 102
toc: true
---

## [범주](/ko/math/category_theory/categories)

범주론의 첫 글답게, "대상과 사상이라는 구조를 가장 추상적으로 다루면 무엇이 되는가"라는 질문에서 출발한다. 범주의 정의(정의 1)는 세 가지 데이터 — 대상들의 모임, 대상들 사이의 morphism들의 모임, 합성 연산 — 와 두 가지 조건 — 결합법칙, 항등원의 존재 — 로 이루어진다. 집합론에서 함수의 합성이 결합법칙을 만족한다는 것을 Operation of Binary Relations 명제 5에서 이미 봤고, 항등함수의 존재와 성질도 Functions 정의 2에서 다뤘으므로, 이 두 조건이 "왜 필요한지"에 대한 동기는 충분하다. 다만 "대상들의 모임"이 집합이 아니라 "모임(class)"일 수 있다는 점이 새로운데, ZFC 공리계에서 전체집합의 비존재를 이미 보였으므로 $$\Set$$의 대상들이 집합을 이루지 못한다는 것이 명확하다. Small category와 locally small category의 구분(정의 4)은 이 문제를 회피하는 실용적인 장치인데, "앞으로 나오는 category는 모두 locally small인 것으로 가정한다"는 선언이 솔직해서 좋다.

예시 2의 구체적 범주들($$\Set$$, $$\Grp$$, $$\Ab$$, $$\Ring$$, $$\Vect_k$$, $$\Top$$ 등)이 인상적이다. 선형대수학에서 다룬 벡터공간과 선형사상이 $$\Vect_k$$라는 범주를 이루고, 집합론에서 다룬 집합과 함수가 $$\Set$$이라는 범주를 이룬다는 것이 "이전 카테고리들이 범주론의 예시였구나"라는 깨달음을 준다. 특히 $$\Set$$의 정의가 집합론의 함수, 합성, 항등함수의 정의를 직접 참조하는 점(참조 링크가 명시적)이 좋은데, "범주론이 수학의 기초 위에 앉아 있다"는 것을 시각적으로 보여준다. $$\Ch(R)$$ (chain complex와 chain map의 범주)도 listed되어 있는데, 이것은 아직 다루지 않은 주제라 나중에 어떤 구조를 보여줄지 기대된다.

예시 3(preordered set을 범주로 보는 것)이 가장 흥미로운 관찰이다. 순서관계의 추이성이 morphism의 합성의 결합법칙으로, 반사성이 항등원의 존재로 번역되는 것이 우아하다. 집합론에서 Order Relations 정의 7(원순서관계: reflexive + transitive)을 정의할 때 "왜 하필 이 두 조건인가"에 대한 답이 여기서 드러난다 — 원순서관계가 곧 "두 원소 사이에 최대 하나의 morphism이 있는 범주"라는 것이다. 다만 "$$x \preceq y$$이면 유일한 morphism $$x \rightarrow y$$가 존재한다"는 조건에서 "유일한"이 핵심인데, 이것이 monoid(정의 10: 대상이 하나인 범주)와 어떻게 다른지 한두 문장의 설명이 있으면 더 명확했을 것 같다.

동형사상(정의 6)의 정의는 선형대수학의 Isomorphic Vector Spaces에서 본 것과 구조적으로 같다. $$f \circ g = \id_{A_2}$$, $$g \circ f = \id_{A_1}$$라는 두 조건은 익숙하고, inverse의 유일성 증명($$g = g \circ (f \circ g') = (g \circ f) \circ g' = g'$$)도 깔끔하다. 다만 "isomorphism은 bimorphism이다"(명제 8)는 결론이 나오면서도, 역이 성립하지 않을 수 있다는 점이 언급된다 — "많은 예시에서 isomorphism은 bijective인 morphism과 같은 말이지만, 항상 그런 것은 아니다"는 주석이 좋은데, 구체적인 반례가 없어서 "어떤 경우에 역이 성립하지 않는가"를 직접 확인하고 싶었다.

Monomorphism과 epimorphism의 정의(정의 7)는 선형대수학의 단사/전사 선형사상과 정확히 대응된다. $$f \circ g_1 = f \circ g_2 \implies g_1 = g_2$$는 "왼쪽에서 취소 가능"이라는 것이고, $$h_1 \circ f = h_2 \circ f \implies h_1 = h_2$$는 "오른쪽에서 취소 가능"이라는 것인데, 집합론에서 Retraction and Section의 명제 1("$$r \circ f = \id_A$$이면 $$f$$는 단사")과 직접 연결된다. Bimorphism(전단사사상)의 정의도 자연스러운데, "isomorphism ⟹ bimorphism"이라는 명제 8의 증명이 2줄로 끝나는 것이 효율적이다.

$$\End(A)$$와 $$\Aut(A)$$의 정의(정의 9)는 선형대수학에서 벡터공간의 선형사상들을 다룰 때의 구조를 일반화한 것이다. $$\Hom_\mathcal{A}(A, A)$$가 단순한 집합이 아니라 합성 $$\circ$$이라는 연산이 주어진 모노이드라는 관찰이 좋은데, 대수적 구조에서 정의한 모노이드의 조건(결합법칙, 항등원)을 직접 확인하면 된다는 것이 명확하다. 모노이드와 군을 범주론적으로 재정의한 것(정의 10, 11: 모노이드 = 대상이 하나인 범주, 군 = 모든 morphism이 isomorphism인 모노이드)이 인상적인데, "대상이 하나"라는 조건이 "모든 원소끼리 합성 가능하다"는 모노이드의 성질을 정확히 포착한다는 것이 우아하다.

Product category(예시 12)와 slice category(예시 13)는 기존 범주로부터 새 범주를 만드는 두 가지 방법을 보여준다. Product category는 집합론의 Product of Sets에서 곱집합을 정의한 것의 범주론적 버전인데, 대상이 쌍 $$(A, B)$$이고 morphism이 쌍 $$(f, g)$$라는 구조가 Product of Sets의 universal property와 직접 연결될 것이라는 예감이 든다. Slice category는 "고정된 대상 $$A$$로 향하는 morphism들을 대상으로 보는 것"인데, 집합론에서 Retraction and Section의 명제 4("$$f = h \circ g$$를 만족하는 $$h$$가 존재하는 조건")와 구조적으로 비슷한 느낌이다. $$f_1 = g \circ f_2$$라는 morphism의 조건이 "$$f_2$$ 위에 $$g$$를 얹어서 $$f_1$$을 만든다"는 것이 직관적이다.

좋은 점들: (1) 구체적 범주들의 나열이 "범주론이 수학의 여러 분야를 관통하는 언어"라는 것을 체감하게 한다. (2) Preordered set을 범주로 보는 관찰이 원순서관계 정의의 동기를 retrospectively 제공한다. (3) 모노이드/군의 범주론적 정의가 대수적 정의와 정확히 일치하는 것이 아름답다.

아쉬운 점들: (1) Locally small category의 가정이 어디까지 사용되는지 명시되어 있지 않아서, 이후 글들에서 이 가정이 없으면 무엇이 달라지는지 혼란스러울 수 있다. (2) Bimorphism이 isomorphism이 아닌 구체적 예시가 없다. (3) Slice category의 정의가 간결하지만, "왜 이런 범주를 만드는가"에 대한 동기 설명이 부족하다 — 아마 다음 글들(Functors)에서 활용될 것 같다.

⚠️ 정의 없이 사용: `class`/`클래스` (ZFC 공리계에서 다루어지지 않았으나 이 글에서 "모임"으로 소개됨; 모든 집합은 class이지만 class 중 집합이 아닌 것이 있다는 설명만 있음)

## [함자](/ko/math/category_theory/functors)

범주의 정의를 마쳤으니, 이제 "범주들 사이의 사상"인 함자를 정의할 차례다. 정의 1 자체는 간결하다: 대상과 morphism을 각각 대응시키면서, 합성과 항등원을 보존하는 것. 집합론에서 함수가 "집합들 사이의 구조 보존 사상"이었고, 선형대수학에서 선형사상이 "벡터공간들 사이의 구조 보존 사상"이었는데, 함자는 그 패턴을 범주 수준에서 반복하는 것이다. 보조정리 2(함자의 합성은 함자)의 증명이 2줄로 끝나는 것이 효율적이다 — $$F$$와 $$G$$가 각각 합성과 항등원을 보존하면 $$G\circ F$$도 마찬가지라는 것이 자명하다.

예시 3($$\mathcal{I}$$-shaped diagram)이 이 글에서 가장 인상적인 관찰이다. preorder set을 범주로 보는 것(Categories 예시 3)을 이미 봤는데, 거기서 "두 원소 사이에 최대 하나의 morphism이 있는 범주"였다면, 여기서는 그 범주에서 다른 범주로의 함자가 곧 "commutative diagram"이라는 것이다. $$\mathcal{I}_1=\{a\leq b\leq c\}$$에서 $$\mathcal{A}$$로의 함자가 commutative triangle을 이루고, $$\mathcal{I}_2=\{a\leq b,c\leq d\}$$에서의 함자가 commutative square를 이룬다는 것이 명확하다. Functions 글에서 commutative diagram을 도입할 때 "화살표로 명시되지 않더라도 $$\id_A$$가 존재한다"고 했는데, 그 관점이 여기서 정확히 실현되는 순간이다.

예시 4($$\Hom_\mathcal{A}(A,-)$$ 함자)는 locally small category 가정이 왜 필요한지를 직접 보여준다. $$\Hom_\mathcal{A}(A,B)$$가 집합이어야 $$\Set$$으로의 함자를 정의할 수 있기 때문이다. $$f:B\to B'$$가 주어지면 $$\Hom_\mathcal{A}(A,f):\phi\mapsto f\circ\phi$$로 대응하는 것이 자연스럽고, 이것이 함자의 조건(합성 보존, 항등원 보존)을 만족하는 것도 직관적이다. 다만 "$$\Hom_\mathcal{A}(A,-)$$이 함자"라는 결론이 Categories에서 정의한 $$\Hom$$ 집합의 구조를 직접 사용한다는 점이 좋다.

반변함자(정의 5)의 도입이 갑자기 전환되는 느낌인데, 동기는 명확하다. $$\Hom_\mathcal{A}(-,A)$$를 정의하려 했더니 화살표 방향이 뒤집힌다는 것이다. $$f:B\to B'$$를 $$\Hom_\mathcal{A}(B',A)\to\Hom_\mathcal{A}(B,A)$$로 보내야 하므로 합성의 순서가 뒤집히고, $$F(g\circ f)=F(f)\circ F(g)$$가 된다는 것이 핵심이다. 반대 카테고리 $$\mathcal{A}^\op$$의 도입(정의 6)으로 이 문제를 우아하게 해결하는 것이 인상적이다 — "화살표를 뒤집은 범주"를 만들면 반변함자는 그냥 함자가 된다. $$\Hom_\mathcal{A}(-,-)$$이 bifunctor $$\mathcal{A}^\op\times\mathcal{A}\to\Set$$라는 결론(예시 8)이 이 아이디어의 정점인데, 첫 번째 변수에서는 반변, 두 번째 변수에서는 공변이라는 것이 $$\Hom$$의 이중적 성격을 정확히 포착한다.

$$\Cat$$과 $$\CAT$$의 정의(정의 9)는 "범주들의 범주"를 구성하는 것이다. 러셀의 역설을 피하기 위해 small category들 또는 locally small category들로 제한한다는 설명이 ZFC 공리계에서 전체집합의 비존재를 다뤘던 것과 직접 연결된다. Categories에서 "대상들의 모임이 집합이 아닐 수 있다"고 했는데, 그 문제가 여기서 다시 등장하는 것이다.

좋은 점들: (1) $$\mathcal{I}$$-shaped diagram 관찰이 commutative diagram의 본질을 드러낸다. (2) 반대 카테고리의 도입이 반변함자의 "문제"를 우아하게 해결한다. (3) $$\Hom$$의 함자적 성질(공변/반변)이 이후 Representable Functors로 이어질 핵심이라는 것이 명확하다.

아쉬운 점들: (1) faithful/full functor의 정의(정의 10)가 마지막에 갑자기 나오는데, 이것이 왜 필요한지에 대한 동기 설명이 없다. (2) 구체적인 함자 예시가 $$\Hom$$과 diagram 이외에는 부족하다 — 예를 들어, 자유군 함자나 망각 함자 같은 대수적 예시가 있었으면 범주론의 "응용"을 체감할 수 있었을 것 같다. (3) bifunctor의 정의(정의 7)가 "이미 알고 있는 것"이라고만 하고, product category $$\mathcal{A}\times\mathcal{B}$$의 정의를 명시적으로 제시하지 않아서 약간 모호하다.

## [자연변환](/ko/math/category_theory/natural_transformations)

함자의 정의를 마쳤으니, 이제 "함자들 사이의 사상"인 자연변환을 정의할 차례다. 정의 1 자체는 간결하다: 각 대상 $$A$$에 대해 $$F(A)\to G(A)$$인 morphism들의 family가 주어지고, 임의의 $$f:A_1\to A_2$$에 대해 관련 diagram이 commute하면 자연변환이다. Functors 글에서 함자가 "범주들 사이의 구조 보존 사상"이었는데, 자연변환은 그 한 단계 위 — "함자들 사이의 구조 보존 사상" — 로 올라가는 것이다. 선형대수학에서 선형사상 $$L:V\to W$$가 basis를 고정하면 행렬로 표현되었는데, 자연변환도 각 대상에서의 component $$\alpha_A$$로 "분해"된다는 점이 비슷한 느낌이다. 다만 행렬은 basis 선택에 의존하지만, 자연변환의 naturality 조건은 basis 독립적이라는 점이 핵심 차이다.

$$\alpha_A$$가 모두 isomorphism이면 natural isomorphism(정의 1 끝부분)이 되고, $$F\simeq G$$로 표기하는데, 이것이 Categories에서 isomorphism을 정의한 것의 함자 수준 확장이다. $$F$$와 $$G$$가 "같은 일을 하는 다른 함자"라는 직관이 드는데, 구체적으로 어떤 의미에서 "같은지"는 equivalence of categories에서 명확해진다. $$\Fun(\mathcal{A},\mathcal{B})$$라는 functor category의 도입도 자연스럽다 — Categories에서 $$\Cat$$을 "범주들의 범주"로 정의했고, 여기서는 "함자들의 범주"를 정의하는 것이다. $$\Hom$$ 집합이 범주 안의 대상들 사이의 "모든 morphism"을 모은 것이었다면, $$\Fun(\mathcal{A},\mathcal{B})$$는 두 범주 사이의 "모든 함자"를 모은 것이라는 대칭성이 좋다.

Equivalence of categories(정의 2)가 이 글의 개념적 전환점이다. $$\Cat$$에서의 isomorphism($$G\circ F=\id$$, $$F\circ G=\id$$)은 너무 강한 조건이라는 것인데, Categories에서 동형사상의 정의를 $$f\circ g=\id$$, $$g\circ f=\id$$로 했던 것과 비교하면 여기서는 $$=$$ 대신 $$\simeq$$(natural isomorphism)를 쓴다는 것이 핵심이다. "$$G\circ F$$가 $$\id_\mathcal{A}$$와 정확히 같지는 않지만, 자연변환에 의해 연결되어 있다"는 것이 "같다"의 약한 버전인데, 선형대수학에서 "같은 차원의 벡터공간은 isomorphic하다"는 것의 범주론적 일반화라는 느낌이 든다. $$\mathcal{A}\simeq\mathcal{B}$$라는 표기가 "equivalent"를 나타내는 것이 $$\cong$$(isomorphism)와 구분되는 점이 명확하다.

Skeletal category(정의 3)와 skeleton(정의 4)의 도입이 실용적이다. "서로 isomorphic한 대상들을 하나로 모은 범주"라는 발상은, 동치관계의 예시들에서 "함수에 의해 정의되는 동치관계"를 다룰 때의 quotient와 구조적으로 비슷하다 — 동치류로 묶어서 "중복을 제거"하는 것이다. 다만 동치관계에서는 $$f(x)=f(y)$$이면 동치였고, 여기서는 $$A\cong A'$$이면 "같은 것으로 본다"는 것이 차이다. $$\sk(\mathcal{A})$$가 $$\mathcal{A}$$의 "뼈대"라는 이름이 적절한데, "살을 걷어내고 뼈만 남긴 것"이라는 직관과 맞다. $$\mathcal{S}$$가 full subcategory라는 조건(정의 이후의 논의)이 중요한데, inclusion functor가 full이어야 $$\mathcal{A}$$의 morphism 정보를 잃지 않는다는 것이 핵심이다. Categories에서 full subcategory를 정의하지 않았는데, 이 글에서 "inclusion functor가 full이면 full subcategory"라고 자연스럽게 도입되는 점이 좋다.

정리 5(equivalence ⟺ fully faithful + essentially surjective)가 이 글의 정점이다. Functors에서 정의한 fully faithful(정의 10: 각 $$\Hom$$ 집합 위의 대응이 bijection)이라는 조건과, "essentially surjective"(각 대상이 $$F(A)$$와 isomorphic)이라는 조건이 합쳐지면 equivalence가 된다는 것이 강력하다. 선형대수학에서 "같은 차원의 벡터공간은 isomorphic하다"는 따름정리 4의 구조와 비슷한데, 거기서는 basis를 택해서 isomorphism을 구성했고 여기서는 fully faithful 조건이 "basis 없이" 사상을 대응시키는 역할을 한다는 것이 차이다. 다만 정리 5의 증명이 "길고 지루하여 별도로 적어두지 않는다"고만 하고, 따름정리 6(skeleton이 isomorphic ⟺ equivalent)도 증명 없이 제시되어서, "정말로 이 두 조건이 충분한지"를 직접 확인하고 싶었다. Categories에서 isomorphism과 bimorphism의 차이를 다룰 때 "isomorphism ⟹ bimorphism"은 증명했지만 역은 안 했는데, 여기서도 비슷한 패턴 — "충분조건은 보이지만 필요조건의 증명은 생략" — 이 반복되는 느낌이다.

좋은 점들: (1) 자연변환의 정의가 "함자들 사이의 사상"이라는 관점에서 함자의 정의와 완벽하게 대비된다. (2) Equivalence of categories가 isomorphism의 "약한 버전"으로 자연스럽게 도입된다. (3) Skeleton을 통한 따름정리 6이 "equivalence의 실질적 의미"를 명확히 보여준다.

아쉬운 점들: (1) 정리 5의 증명이 생략되어 있어서, fully faithful + essentially surjective가 왜 충분한지에 대한 직관이 부족하다. (2) 구체적인 natural transformation의 예시(예: determinant, trace 같은 고전적 예)가 없어서, "자연변환이 왜 자연스러운가"라는 물음을 체감하기 어렵다. (3) Full subcategory가 Categories에서 정의되지 않았는데 이 글에서 사용되어서, prior knowledge가 필요하다.

⚠️ 정의 없이 사용: `inclusion functor` (부분범주에서 전체범주로의 "포함" 함자인데, Functors에서 명시적으로 정의되지 않음)

## [표현가능한 함자](/ko/math/category_theory/representable_functors)

함자 $$F:\mathcal{A}\to\Set$$가 "어떤 대상 $$A$$의 $$\Hom$$ 집합과 자연동형이다"는 것이 representable functor의 정의(정의 1)이다. Functors에서 $$\Hom_\mathcal{A}(A,-)$$가 함자임을 이미 확인했으므로, 이 정의의 출발점 자체는 자연스럽다. Covariant case와 contravariant case를 나눈 것도 $$\Hom_\mathcal{A}(A,-)$$와 $$\Hom_\mathcal{A}(-,A)$$의 차이 — 공변/반변 — 를 Functors에서 이미 다뤘으므로 일관적이다. 다만 "representation"이라는 용어를 "대상 $$A$$와 natural isomorphism의 선택을 통틀어"라고 정의한 것(정의 1 끝부분)이 인상적인데, $$A$$만으로는 부족하고 natural isomorphism의 구체적 선택까지 포함해야 한다는 점이 이후 universal element의 도입으로 이어진다.

요네다 보조정리(정리 3)가 이 글의 핵심이다. $$\Hom_\mathcal{A}(A,-)$$에서 $$F$$로의 natural transformation들의 집합과 $$F(A)$$ 사이에 bijection이 존재한다는 것인데, $$\alpha\mapsto\alpha_A(\id_A)$$라는 대응이 놀랍도록 간결하다. 증명의 핵심은 역함수 $$\Psi$$의 구성이다: $$x\in F(A)$$가 주어지면 $$\Psi(x)_X(f)=F(f)(x)$$로 정의하는데, naturality diagram을 $$\id_A$$에서 추적하면 $$\Psi(x)_A(\id_A)=F(\id_A)(x)=x$$가 되어 $$\Phi$$의 역함수임이 확인된다. 이 식 $$\Psi(x)_X(f)=F(f)(x)$$의 의미를 한 번 더 생각해보면, $$f:A\to X$$라는 morphism을 $$F$$에 통과시키면 $$F(X)$$의 원소가 되고, 이것이 $$x$$의 "이미지"라는 것이다. $$f$$가 $$\id_A$$일 때 원래 $$x$$로 돌아오는 것이 핵심인데, $$\id_A$$가 "시작점" 역할을 한다는 것이 명확하다. 증명이 깔끔하긴 한데, "이 $$\Psi(x)$$가 왜 natural transformation인지"가 증명에서 "어렵지 않다"고만 넘어가서, 직접 확인해보니 $$F(g)\circ\Psi(x)_X = \Psi(x)_Y\circ\Hom(A,g)$$가 $$F(g)(F(f)(x))=F(g\circ f)(x)$$로 귀결되는 것이기는 하지만, 이 부분이 한두 줄 더 있었으면 좋았을 것 같다.

Universal element와 universal property(정의 5)의 연결이 이 글의 개념적 전환점이다. Natural isomorphism $$\Hom_\mathcal{A}(A,-)\cong F$$를 $$F(A)$$의 원소 $$x$$ 하나로 대체할 수 있다는 것인데, 요네다 보조정리가 이 대체를 정당화한다. $$x$$가 "universal"이라는 이름이 붙은 이유는, 임의의 $$f:A\to X$$에 대해 $$F(f)(x)$$가 $$F(X)$$의 모든 원소를 "생성"하기 때문인데 — 즉 $$\Psi(x)_X$$가 bijection이므로 — $$x$$ 하나로 $$F$$ 전체를 재건할 수 있다는 것이 강력하다. $$\id_\Set\cong\Hom_\Set(\ast,-)$$라는 예시 2가 좋은데, $$\ast$$의 원소(하나뿐)가 임의의 집합의 원소를 "생성"하는 것이 $$\Set$$의 representability를 직접 보여준다.

텐서곱의 예시 6이 가장 구체적인 적용이다. $$\operatorname{Bilin}(V,W;-)$$이라는 함자가 representable하고, 그 representation의 대상이 $$V\otimes W$$이며, universal element가 $$V\times W\to V\otimes W$$인 canonical bilinear map이라는 것이다. Multilinear Algebra의 Hom과 텐서곱에서 텐서곱을 정의할 때 "bilinear map을 factoring하는 유일한 linear map"이라는 universal property를 봤는데, 그 정의가 정확히 representable functor의 언어로 재서술된다는 것이 새롭다. 다만 이 예시가 유일한 구체적 적용이라서, product나 coproduct 같은 다른 universal construction도 같은 틀로 볼 수 있다는 것을 한두 문장 언급했으면 더 좋았을 것 같다.

Category of elements $$\int F$$(정의 7)의 정의가 흥미로운데, 대상이 $$(A,x)$$ 쌍이고 morphism이 $$F(f)(x_1)=x_2$$를 만족하는 $$f$$라는 것이 "$$F$$의 원소들을 $$\mathcal{A}$$의 구조 위에 올려놓은 것"이라는 직관을 준다. $$\Hom_\mathcal{A}(A,-)$$의 category of elements가 under category $${}_{A/}\mathcal{A}$$라는 관찰(정의 7 이후)이 핵심인데, "under category"가 prior 글들에서 정의된 적이 없어서 갑자기 등장하는 것이 당황스러웠다. $$A$$ 아래의 대상들 — 즉 $$A\to X$$인 morphism들을 대상으로 하는 범주 — 라는 것이 $$\int\Hom_\mathcal{A}(A,-)$$의 정의와 직접 대응되는 것은 맞지만, under category 자체의 정의가 없으면 이 관찰의 의미가 반감된다. $$\int\Hom_\mathcal{A}(A,-)$$에서의 initial object가 $$\id_A$$라는 것도 $$\id_A:A\to A$$가 $$A$$ 아래의 "가장 작은" 대상이라는 직관과 맞는데, under category를 모르면 이 직관을 잡기 어렵다.

명제 8($$F$$가 representable $$\iff$$ $$\int F$$가 initial object를 가짐)이 이 글의 정점이다. 증명의 한 방향($$\implies$$)은 $$\int F\cong\int\Hom_\mathcal{A}(A,-)={}_{A/}\mathcal{A}$$라는 동형으로 reduce되고, $${}_{A/}\mathcal{A}$$가 initial object $$\id_A$$를 가진다는 것으로 끝나는데, under category를 알면 3줄이다. 반대 방향($$\impliedby$$)은 $$\int F$$의 initial object $$(A,x)$$로부터 natural isomorphism을 구성하는 것인데, $$\Psi(x)_X$$가 bijection임을 initial object의 정의($$F(f)(x)=y$$를 만족하는 유일한 $$f$$)로 직접 보이는 것이 깔끔하다. $$\Psi(x)_X(f)=F(f)(x)$$가 임의의 $$y\in F(X)$$에 대해 유일한 $$f$$를 만들어낸다는 것이 initial object의 "유일한 morphism 존재" 조건과 정확히 대응되는 것이 우아하다.

이 글을 읽고 나서 "universal property"라는 것이 단순한 이름이 아니라 representable functor라는 범주론적 개념의 구체적 발현이라는 것을 이해하게 되었다. Multilinear Algebra에서 텐서곱을 정의할 때 쓴 universal property, Categories에서 product category를 언급할 때 기대했던 universal property, 그리고 앞으로 나올 극한과 쌍극한까지 — 이 모든 것이 representable functor의 틀 안에 들어온다는 것이 큰 그림을 잡는 데 도움이 된다. 요네다 보조정리가 이 모든 것의 기초에서 작동하고 있다는 것도 새롭다.

좋은 점들: (1) 요네다 보조정리의 증명이 $$\Psi(x)_X(f)=F(f)(x)$$라는 공식 하나로 핵심이 압축되어 있다. (2) Universal element의 도입이 요네다 보조정리의 직접적 결과로 자연스럽게 이어진다. (3) $$\id_\Set\cong\Hom_\Set(\ast,-)$$라는 예시가추상적인 정의를 즉시 구체화한다.

아쉬운 점들: (1) Under category가 정의 없이 사용되어서, $$\int\Hom_\mathcal{A}(A,-)={}_{A/}\mathcal{A}$$라는 관찰의 의미가 반감된다. (2) 텐서곱 이외의 구체적 예시(product, coproduct, equalizer 등)가 없어서, "어떤 것들이 representable한가"에 대한 직관이 좁다. (3) 요네다 보조정리의 증명에서 $$\Psi(x)$$가 natural transformation임을 확인하는 부분이 "어렵지 않다"고만 넘어가서, 핵심 논증의 일부가 빠져 있다.

⚠️ 정의 없이 사용: `under category` $${}_{A/}\mathcal{A}$$ (정의 7 이후에 갑자기 등장; prior 글들에서 정의된 적 없음)

## [극한](/ko/math/category_theory/limits)

Representable Functors에서 "universal property = representable functor의 구체적 발현"이라는 결론을 봤는데, 이 글이 바로 그 결론의 첫 번째 본격적인 적용이다. 극한의 정의 자체가 Representable Functors의 언어로 직접 주어진다: $$\Cone(-,F)$$라는 contravariant functor의 representation이 곧 $$F$$의 limit이다(정의 2). "cone"이라는 이름은 constant functor $$A:\mathcal{I}\to\mathcal{A}$$에서 다이어그램 $$F$$로의 natural transformation $$\lambda:A\Rightarrow F$$를 부르는 것인데(정의 1), 각 $$\lambda_i:A\to F(i)$$가 "꼭짓점 $$A$$에서 다이어그램의 각 꼭짓점으로 향하는 다리"라는 시각적 직관이 이름에 잘 반영되어 있다. $$\mathcal{I}$$가 poset $$(\mathbb{Z},\leq)$$일 때의 그림이 특히 도움이 되는데, 모든 삼각형이 commute한다는 것이 natural transformation의 조건이라는 것이 명확하다.

$$\Cone(-,F)$$가 representable하다는 것은, Representable Functors에서 $$F$$가 representable하다는 것과 구조적으로 같은 말인데 — 다만 $$\Cone(-,F)$$는 contravariant functor이므로 $$\Hom_\mathcal{A}(\lim F,-)$$가 아니라 $$\Hom_\mathcal{A}(-,\lim F)$$와 natural isomorphism을 이룬다 — universal property로 번역하면 "임의의 cone $$\lambda:A\Rightarrow F$$에 대해 유일한 $$f:A\to\lim F$$가 존재하여 $$\lambda=\hat{\lambda}\circ f$$를 만족한다"는 것이 된다. Representable Functors의 명제 8($$F$$가 representable $$\iff$$ $$\int F$$가 initial object를 가짐)의 dual 버전 — $$\int\Cone(-,F)$$가 terminal object를 가짐 — 이 여기서 직접 사용되는 구조가 깔끔하다.

$$\Set$$이 complete category라는 예시 4가 이 글의 첫 번째 핵심이다. Representable Functors 예시 2의 natural isomorphism $$A\cong\Hom_\Set(\ast,A)$$를 사용해서, $$\Cone(\ast,F)$$의 원소 $$\mu:\ast\Rightarrow F$$를 각 $$F(i)$$의 원소 $$\mu_i$$로 "번역"한 후, 그것들을 모아서 limit cone $$\lambda:\lim F\Rightarrow F$$를 구성하는 논증이 우아하다. 핵심은 $$\Cone(\ast,F)\cong\lim F$$라는 것인데, "cone의 집합 = limit의 원소"라는 대응이 $$\Set$$에서의 극한이 "조건을 만족하는 원소들의 부분집합"으로 구성됨을 보여준다. 집합론에서 Product of Sets의 universal property를 $$\Set$$ 안에서 확인하는 것인데, 범주론적 정의가 집합론적 구성과 정확히 일치하는 순간이다.

구체적 극한들의 예시들이 큰 그림을 잡는 데 결정적이다. 예시 6(product)은 $$\mathcal{I}$$가 discrete category일 때의 limit인데, naturality 조건이 아무것도 요구하지 않으므로 그냥 morphism들의 family $$(\lambda_i:A\to F(i))_{i\in\mathcal{I}}$$가 되는 것이 깔끔하다. Product of Sets에서 정의한 곱의 universal property와 정확히 같은 구조인데, $$\mathcal{A}=\Set$$이면 집합론의 결과로 환원된다. 예시 7(equalizer)은 $$f,g:B\to C$$인 두 morphism의 "공통부분"을 잡는 construction인데, $$\lambda_B\circ f=\lambda_B\circ g$$를 만족하는 $$\lambda_B:A\to B$$ 중 universal한 것을 찾는 것이 $$\Set$$에서는 "같은 값을 내는 원소들의 집합"을 구성하는 것과 같다는 관찰이 직관적이다. 예시 8(fiber product)은 $$A\overset{f}{\to}C\overset{g}{\leftarrow}B$$가 주어졌을 때 $$g\circ b=f\circ a$$를 만족하는 $$A\leftarrow X\to B$$ 중 universal한 것인데, 스킴 이론에서 fiber product이 얼마나 중요한지를 이미 알고 있으므로 이 예시가 특별히 반갑다. $$\lrcorner$$ 표기도 기억해둘 만하다.

$$\Set$$에서 임의의 small diagram의 limit을 product와 equalizer로 표현할 수 있다는 관찰(예시 4 이후의 논의)이 실용적이다. product로 "조건을 만족하는 원소들의 후보"를 만들고, equalizer로 "commutativity 조건"을 강제하는 두 단계 구성인데, 이는 집합론에서 Product of Sets의 성질들(limit = 조건을 만족하는 부분곱)과 직접 연결된다. 임의의 category가 product와 equalizer를 갖는다면 complete이라는 결론(본문 마지막 문장)은, 이 두 construction이 "모든 극한의 building block"이라는 것을 보여준다.

$$\Hom$$과 극한의 관계(정리 9)가 이 글의 두 번째 핵심이다. $$\lim\Hom_\mathcal{A}(A,F-)\cong\Cone(A,F)\cong\Hom_\mathcal{A}(A,\lim F)$$라는 natural isomorphism은, $$\Hom_\mathcal{A}(A,-)$$가 "극한을 보존한다"는 것인데 — 즉 continuous functor라는 것 — 이전 Representable Functors에서 $$\Hom$$이 representable functor의 대표적 예시였던 것의 연장이다. 다만 정리 9의 서술이 $$\lim\Hom_\mathcal{A}(A,F-)\cong\lim\Hom_\mathcal{A}(A,F-)$$라고 되어 있어서 좌변과 우변이 같은 것으로 보이는데, 아마 $$\Hom_\mathcal{A}(A,\lim F)$$여야 할 것 같다 — 서술상의 오류로 보인다.

명제 10(결합법칙: $$\lim_i\lim_j F(i,j)\cong\lim_j\lim_i F(i,j)$$)은 "이중 극한의 순서를 바꿔도 같다"는 것인데, 다만 일반적으로 $$\lim$$과 $$\colim$$의 순서는 바꿀 수 없다는 마지막 관찰이 중요하다. $$\colim_i\lim_j\to\lim_j\colim_i$$라는 canonical morphism만 존재한다는 것이 "극한과 여극한은 쌍대적이지만 교환 불가능하다"는 메시지를 전한다. 집합론의 Limits에서 inverse limit과 direct limit을 다룰 때도 비슷한 관찰이 있었는데, 범주론적 맥락에서 다시 보니 그 의미가 더 명확해진다.

좋은 점들: (1) 극한의 정의가 Representable Functors의 언어로 직접 주어져서, representable functor의 힘을 체감하게 한다. (2) Product, equalizer, fiber product의 구체적 예시가 추상적 정의에 살을 붙인다. (3) $$\Set$$에서의 구성이 집합론적 직관과 정확히 일치하는 것이 큰 그림을 잡는 데 도움이 된다.

아쉬운 점들: (1) 정리 9의 서술에 오류로 보이는 부분이 있다 ($$\lim\Hom(A,F-)\cong\lim\Hom(A,F-)$$가 좌변과 우변이 같음). (2) Colimit의 구체적 예시(coproduct, coequalizer, fiber coproduct)가 한 문장으로만 언급되어서, dual construction에 대한 직관이 부족하다. (3) $$\Set$$에서의 limit 구성(product + equalizer)의 증명이 상당히 압축되어 있어서, "$$\Cone(\ast,F)$$의 원소가 $$\prod F(i)$$의 원소 중 commutativity 조건을 만족하는 것"이라는 핵심을 따라가려면 몇 번 다시 읽어야 한다.

⚠️ 정의 없이 사용: `discrete category` (예시 6에서 갑자기 등장; "morphism이 identity morphism밖에 없는 category"라는 설명만 있음)

## [모노이드 범주](/ko/math/category_theory/monoidal_categories)

이 글은 "범주 안에서 monoid를 정의하려면 무엇이 필요한가"라는 질문에서 출발한다. 대수적 구조에서 정의한 monoid — 이항연산 $$\mu:M\times M\rightarrow M$$과 항등원 $$e\in M$$, 결합법칙과 항등원 조건 — 를 범주론적으로 번역하려면, 우선 $$M\times M$$이라는 "곱"이 무엇인지부터 정의해야 한다. Limits에서 categorical product를 정의했으므로 그 틀을 가져올 수 있지만, 일반 monoidal category에서는 $$\otimes$$이 product일 필요가 없다는 것이 핵심이다. 글의 첫 부분에서 monoid의 associativity와 unit element 조건을 commutative diagram으로 재서술하는 것이 좋은데, $$\mu(\mu(a,b),c)=\mu(a,\mu(b,c))$$라는 집합론적 조건이 곧 associativity diagram의 commute임을 보여주는 것이 "왜 diagram이 필요한가"에 대한 동기를 명확하게 제공한다.

Monoidal category의 정의(정의 5)는 $$\mathcal{A}$$, $$\otimes$$, $$I$$, associator $$\alpha$$, left/right unitors $$\lambda$$, $$\rho$$, 그리고 두 coherence condition — pentagon identity와 unitor diagram — 으로 이루어진다. $$\otimes$$이 bifunctor라는 조건은 Functors에서 bifunctor를 정의한 것의 직접적 사용이고, $$\alpha$$, $$\lambda$$, $$\rho$$가 natural isomorphism이라는 조건은 Natural Transformations에서 정의한 것의 적용이라는 점에서, 이 정의가 이전 글들의 개념들을 한데 모으는 느낌이다. 다만 "왜 $$\alpha$$, $$\lambda$$, $$\rho$$가 identity가 아니라 isomorphism인가"라는 질문이 자연스러운데, 글에서 "$$M\times(M\times M)$$과 $$(M\times M)\times M$$은 서로 다른 집합"이라고 설명한 것이 답이다 — $$\Set$$에서는 이 두 집합이 엄밀히 다르지만 자연스러운 bijection이 존재하고, 일반 범주에서는 그 bijection이 $$\alpha$$라는 것이다. 이 관찰이 "왜 coherence condition이 필요한가"에 대한 동기도 제공한다 — $$\alpha$$가 identity면 pentagon identity가 자동으로 성립하겠지만, 그렇지 않은 경우를 다루려면 coherence condition이 필수적이다.

Symmetric monoidal category의 정의가 자연스럽게 이어진다. $$\gamma_{AB}:A\otimes B\rightarrow B\otimes A$$이라는 symmetor가 추가되고, associativity coherence, unit coherence, inverse law라는 세 조건이 더해진다. $$\Set$$에서 $$A\times B\cong B\times A$$라는 bijection이 이미 익숙하므로, $$\gamma$$의 존재 자체는 놀랍지 않다. 다만 "braided monoidal category" — $$\gamma_{AB}$$와 $$\gamma_{BA}$$가 서로의 inverse가 아닌 경우 — 가 갑자기 등장하는데, 구체적 예시가 없어서 "어떤 상황에서 $$\gamma_{AB}\circ\gamma_{BA}\neq\id$$이 되는가"를 직접 확인하기 어려웠다. 매듭 이론이나 양자군 같은 곳에서 등장한다고 들었지만, 이 글만으로는 그 직관을 잡기 어렵다.

Mac Lane의 coherence theorem이 이 글의 개념적 핵심인데, "$$n$$개의 대상들의 곱을 어떤 순서로 계산하든 naturally isomorphic하며, 그 isomorphism이 associator·unitor·symmetor의 합성으로 유일하게 나타난다"는 결론이 강력하다. 다만 증명이 없어서 "$$n=4$$인 경우 pentagon identity가, $$n=5$$인 경우는 어떤 diagram이 충분조건인지"를 직접 확인하고 싶었다. Coherence theorem 덕분에 "$$\otimes$$의 계산 순서는 신경 쓰지 않아도 된다"는 결론이 실용적이긴 한데, "신경 쓰지 않아도 된다"는 것이 "identity로 놓아도 된다"는 것인지, "isomorphism으로 연결되어 있으므로 같은 것으로 취급해도 된다"는 것인지 구분이 필요하다 — 후자가 맞다.

Cartesian category(정의 7)와 cartesian monoidal category(명제 8)의 연결이 실용적이다. Limits에서 정의한 categorical product가 곧 $$\otimes$$이 되는 경우인데, $$\Set$$, $$\Grp$$, $$\Top$$ 모두 cartesian category이므로 자연스럽게 monoidal category가 된다. $$R$$-$$\Mod$$의 tensor product $$\otimes_R$$는 cartesian product가 아니므로 cartesian monoidal category가 아닌데, 이것이 "왜 $$\otimes$$을 별도로 정의하는가"에 대한 답 — categorical product만으로는 모든 monoidal structure를 포착할 수 없다 — 이 된다. Diagonal morphism $$\Delta_X:X\rightarrow X\times X$$과 augmentation morphism $$\epsilon_X:X\rightarrow I$$의 정의도 자연스러운데, $$I$$가 terminal object이므로 $$\epsilon_X$$가 유일하게 존재하고, $$\Delta_X$$는 product의 universal property에서 얻어진다. 다만 "이 morphism들이 왜 cartesian monoidal category에서만 잘 정의되는가" — 일반 monoidal category에서는 $$I$$가 terminal object가 아닐 수 있고, diagonal morphism을 정의할 수 없기 때문 — 에 대한 설명이 한두 문장 있었으면 더 명확했을 것 같다.

좋은 점들: (1) Monoid의 정의를 commutative diagram으로 번역하는 과정이 monoidal category 정의의 동기를 명확하게 제공한다. (2) $$\Set$$, $$\Vect_k$$, $$\Ab$$ 등 구체적 예시가 추상적 정의에 살을 붙인다. (3) Cartesian monoidal category에서의 diagonal·augmentation morphism이 다음 글(Monoid Objects)로의 연결을 예고한다.

아쉬운 점들: (1) Braided monoidal category의 구체적 예시가 없어서, symmetric과의 차이를 체감하기 어렵다. (2) Coherence theorem의 증명이 생략되어서, pentagon identity가 왜 충분한지에 대한 직관이 부족하다. (3) Associator·unitor가 identity가 아닌 구체적 범주 예시(예: $$\Vect_k$$에서의 associator)가 없어서, "언제 $$\alpha\neq\id$$인가"를 실감하기 어렵다.

⚠️ 정의 없이 사용: `cartesian product` (Limits의 "categorical product"를 같은 말로 사용하나, 두 용어의 동치가 명시적으로 주장되지 않음), `terminal object` (명제 8 이후 갑자기 등장; Limits에서 정의되었으나 이 글에서의 맥락상 재정의 없이 사용됨)

## [모노이드 대상](/ko/math/category_theory/monoid_objects)

Monoidal Categories에서 "범주 안에서 monoid를 정의하려면 $$\otimes$$이 필요하다"는 결론을 봤는데, 이 글이 바로 그 결론의 구체적 실현이다. 정의 1 자체는 간결하다: 대상 $$M$$, multiplication $$\mu:M\otimes M\rightarrow M$$, unit $$\eta:I\rightarrow M$$이라는 데이터가 associativity와 unit 조건을 만족하는 것. Monoidal Categories에서 monoid의 조건을 commutative diagram으로 재서술하는 것을 봤는데, 거기서는 "왜 diagram이 필요한가"에 대한 동기였다면 여기서는 그 diagram이 곧 정의 자체가 되는 것이다. $$\Set$$에서 monoid object가 일반적인 monoid이고, $$\Top$$에서 topological monoid라는 예시 2가 정의의 의미를 즉시 구체화하는데, "monoidal category를 바꾸면 같은 정의가 다른 대수적 구조를 포착한다"는 것이 이 글의 핵심 메시지이다.

세 번째 예시 — $$(\lMod{R},\otimes_R,R)$$에서 monoid object가 associative unital $$R$$-algebra라는 것 — 가 가장 인상적이다. Monoidal Categories에서 "cartesian monoidal category와 일반 monoidal category는 다르다"고 했는데, 그 차이가 여기서 직접 드러난다. $$\lMod{R}$$에서 $$\otimes_R$$은 categorical product가 아니므로, unit object $$R$$이 terminal object가 아니고, unitor $$\lambda_M:R\otimes M\rightarrow M$$이 $$r\otimes m\mapsto rm$$이라는 구체적 $$R$$-linear map으로 주어진다는 것이 명확하다. $$\eta:R\rightarrow M$$이 $$\eta(1)$$이라는 원소 하나로 결정되고, 이것이 곱셈의 항등원이 된다는 논증( $$\mu(\eta(1)\otimes m)=\lambda_M(1\otimes m)=m$$ )이 깔끔하다. $$M\otimes M\rightarrow M$$과 $$M\times M\rightarrow M$$ 사이의 $$R$$-bilinear map 대응이 분배법칙을 자동으로 보장한다는 관찰도 좋은데, "왜 tensor product로 정의한 곱셈이 $$R$$-선형과 호환되는가"에 대한 답이 여기서 나온다.

Group object(정의 3)는 cartesian monoidal category에서만 정의된다는 것이 흥미로운데, 그 이유가 명확하다. Inverse 조건을 diagram으로 �려면 diagonal map $$\Delta_G:G\rightarrow G\times G$$이 필요한데, 일반 monoidal category에서는 이를 정의할 수 없기 때문이다. Monoidal Categories에서 diagonal morphism과 augmentation morphism을 cartesian monoidal category에서 정의한 것이 여기서 직접 사용되는 구조가 깔끔하다. $$e_G = G\rightarrow I\overset{\eta}{\rightarrow}G$$라는 합성으로 항등원을 표현하는 것이 $$\epsilon_G$$ (terminal object로의 유일한 morphism)를 사용한다는 것이 우아하다. 예시 4의 나열 — $$\Set$$에서 group, $$\Top$$에서 topological group, $$\Man^\infty$$에서 Lie group, $$\Sch$$에서 group scheme — 가 "같은 정의가 기하학적 맥락마다 다른 구조를 포착한다"는 것을 체감하게 한다. $$\Grp$$에서 group object가 abelian group이라는 마지막 예시가 특히 인상적인데, inverse $$\iota$$가 group homomorphism이어야 한다는 조건에서 commutativity가 나온다는 것이 놀랍다.

Hopf monoid까지의 전개 — comonoid(정의 5), bimonoid(정의 6), Hopf monoid(정의 7) — 가 이 글의 후반부를 이루는데, comonoid를 $$\mathcal{A}^\op$$에서의 monoid object로 정의하는 것(정의 5)이 Categories에서 반대 범주를 도입한 것의 직접적 활용이다. Bimonoid가 "monoid이면서 comonoid이고, comultiplication과 counit이 monoid morphism"이라는 것이 "$$M$$ 위에 호환되는 두 구조가 공존한다"는 것인데, symmetric monoidal category에서만 정의된다는 제한이 $$M\otimes M$$에 monoid 구조를 주기 위해 symmetor가 필요하다는 것에서 나온다는 설명이 동기를 명확히 한다. Hopf monoid의 antipode $$\iota$$에 대한 조건(정의 7 이후의 diagram)이 group object의 inverse 조건과 정확히 대응되는 것이 "Hopf monoid = bimonoid화된 group object"라는 직관을 준다. cartesian monoidal category에서 group object가 자연스럽게 Hopf monoid가 된다는 것(예시 8)이 이 직관을 확인해주고, $$\Vect$$에서 Hopf monoid가 Hopf algebra라는 결론이 선형대수학과의 연결을 예고한다.

좋은 점들: (1) $$\Set$$, $$\lMod{R}$$, $$\Top$$ 등 구체적 예시가 추상적 정의에 살을 붙이고, 각 monoidal category의 차이를 체감하게 한다. (2) Group object를 cartesian monoidal category에서만 정의하는 동기 — diagonal map의 필요성 — 가 명확하다. (3) Comonoid를 $$\mathcal{A}^\op$$에서의 monoid로 정의하는 것이 반대 범주를 사용한 간결한 전개를 보여준다.

아쉬운 점들: (1) Monoid object 간의 morphism이 언급되지만("monoid object들 사이의 morphism도 정의할 수 있다") 정의가 없어서, $$\lMod{R}$$에서의 monoid morphism이 ring homomorphism인지, group object 간의 morphism이 group homomorphism인지 확인할 수 없다. (2) Hopf monoid 섹션이 앞부분에 비해 압축되어 있어서, bimonoid의 조건("comultiplication과 counit이 monoid morphism")이 구체적으로 무엇을 의미하는지 한두 예시가 있었으면 좋았을 것 같다. (3) $$\Vect$$에서의 Hopf algebra가 어떤 구체적 예를 주는지(예: group algebra $$k[G]$$, coordinate ring $$k[G]$$ 등) 언급 없이 끝나서, "Hopf algebra가 실제로 쓰이는 곳"에 대한 직관이 부족하다.

⚠️ 정의 없이 사용: `chain complex` (예시 2에서 $$\Ch(R)$$의 대상으로 사용되나 정의된 적 없음), `differential graded algebra` (예시 2에서 갑자기 등장; prior 글들에서 정의되지 않음)

## 카테고리 회고

범주론 카테고리는 "구조를 보존하는 사상"이라는 패턴을 가장 추상적 수준에서 반복하는 것이었다. 범주 → 함자 → 자연변환 → 표현가능한 함자 → 극한 → 모노이드 범주 → 모노이드 대상으로 이어지는 전개가, 각 단계에서 이전 단계의 개념을 "대상"으로 삼아 한 층 위로 올라가는 구조인데, 이 피라미드가 서서히 좁아지면서 정점에 monoid object가 앉아 있다는 것이 인상적이다. 집합론과 선형대수학에서 이미 알고 있던 것들 — 집합, 함수, 곱, 텐서곱, monoid, group — 이 모두 범주론적 정의의 특수 경우로 환원되는 것을 보면서, "이전 카테고리들이 범주론의 예시였구나"라는 Categories 첫 글의 관찰이 실제로 확인되었다. 가장 막혔던 지점은 Representable Functors에서 요네다 보조정리의 $$\Psi(x)$$가 natural transformation임을 확인하는 부분과, Limits에서 $$\Set$$의 limit 구성(product + equalizer)의 증명이 압축되어 있어서 몇 번 다시 읽어야 했던 것이다.
