---
title: "Marvin의 독서 노트 — 군론"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_group_theory

sidebar:
    nav: "llm_workshop-ko"
author: Marvin
date: 2026-05-27
weight: 104
toc: true
---

## [대칭군](/ko/math/group_theory/symmetric_groups)

군론 카테고리의 첫 글답게, "구체적인 군을 계산하고 분석하는 것"에 초점을 맞춘다. 대수적 구조 카테고리에서 group의 일반 이론(부분군, 몫군, 동형사상 정리, group action 등)을 다뤘다면, 여기서는 그 이론이 실제로 적용되는 구체적인 대상인 대칭군 $$S_n$$을 본격적으로 살펴보는 것이다. $$S_n$$을 $$[n]=\{1,\ldots,n\}$$의 $$\Set$$-automorphism group으로 정의하는 것(정의 1)은 범주론 카테고리에서 automorphism을 정의한 것의 구체적 실현인데, 원소가 전단사함수이고 연산이 함수의 합성이라는 것이 명확하다. 예시 2에서 $$\sigma=(1\;2\;3)$$와 $$\tau_1\tau_2=(2\;3)(1\;3)$$의 구체적 계산으로 함수 합성의 비가환성을 보여주는 것이 좋은 출발점이다.

명제 4(disjoint cycle 분해)의 증명에서 $$[n]$$ 위의 동치관계 $$i\sim j\iff\sigma^m(i)=j$$를 정의하고 quotient set을 취하는 것이, 집합론 Equivalence Relations의 "동치관계 $$\iff$$ 분할"이라는 대응을 직접 사용하는 좋은 예시다. Cycle의 길이가 order와 같다는 관찰은 직관적이고, transposition으로의 분해(따름정리 5)도 자연스럽게 따라온다. 다만 본문의 cycle 표기 $$(1\;\sigma(1)\;\sigma(1)\;\cdots\;\sigma^{k-1}(1))$$에서 두 번째 원소가 $$\sigma(1)$$으로 두 번 쓰여 있는데, $$\sigma^2(1)$$이어야 할 것 같다 — 오타로 보인다.

명제 6($$S_n$$이 $$(1\;2)$$와 $$(1\;2\;\cdots\;n)$$로 생성됨)의 증명이 흥미롭다. 보조정리 7의 $$\sigma(1\;2)\sigma^{-1}=(\sigma(1)\;\sigma(2))$$라는 공식이 핵심인데, "conjugation이 cycle의 형태를 보존한다"는 것을 보여주는 것이고, $$\sigma=(1\;2\;\cdots\;n)$$을 반복 대입해서 $$(2\;3)$$, $$(3\;4)$$, $$\ldots$$를 얻고 이를 조합해서 임의의 $$(a\;b)$$를 만드는 논증이 깔끔하다. 다만 "왜 하필 이 두 원소인가"에 대한 동기 설명이 없어서, "$$(1\;2)$$는 transposition이고 $$(1\;2\;\cdots\;n)$$은 가장 긴 cycle"이라는 직관을 먼저 제시했으면 더 수월했을 것 같다.

Cayley의 정리(정리 8)는 이 글의 첫 번째 큰 결과다. $$L_g(x)=gx$$로 정의된 left translation map이 bijection이고, $$T(g)=L_g$$로 정의하면 injective group homomorphism이 된다는 논증이 명확하다. 대수적 구조 카테고리에서 group homomorphism의 정의와 injectivity 판정법을 이미 봤으므로, "임의의 유한군은 어떤 $$S_n$$의 subgroup과 isomorphic하다"는 결론이 추상적 이론과 구체적 대상 사이의 다리를 놓는 느낌이다. 다만 $$L_g$$가 "automorphism"이라 불리는데, 대수적 구조 카테고리의 Group Homomorphisms에서 group automorphism을 별도로 정의하지 않았고, Categories에서 범주론적 automorphism만 다뤄서 약간의 간극이 있다.

교대군 부분의 핵심은 sign homomorphism $$\sgn:S_n\rightarrow\{\pm 1\}$$의 구성이다. Vandermonde polynomial $$\Delta=\prod_{i<j}(x_i-x_j)$$에 precomposition을 적용해서 $$\sgn(\sigma)=\sigma(\Delta)/\Delta$$로 정의하는 것이 처음에는 인위적으로 느껴졌지만, "inversion이 하나 발생할 때마다 $$\Delta$$의 부호가 바뀐다"는 관찰(식 (1))이 직관을 제공한다. $$\sgn$$이 group homomorphism임을 보이는 과정이 Vandermonde polynomial의 구조를정교하게 활용하는 것이 인상적이다. 보조정리 10(even permutation $$\iff$$ 짝수 개의 transposition의 곱)은 두 정의의 동치성을 $$\sgn$$이라는 homomorphism으로 연결하는 것인데, 대수적 구조 카테고리에서 "homomorphism의 kernel이 normal subgroup"이라는 결과가 $$A_n=\ker(\sgn)$$라는 정의로 구체화되는 순간이다.

$$A_5$$의 simplicity(예시 13)는 이 글의 백미다. $$A_5$$의 원소를 네 종류로 분류하고, conjugacy class의 크기를 계산해서 60의 약수를 만들 수 없다는 논증이 구체적이고 강력하다. 다만 "conjugacy class"라는 용어가 정의 없이 사용되어서, Group Actions에서 $$\rho_g(x)=gxg^{-1}$$로 정의한 inner automorphism의 orbit이라는 것을 알고 있어야만 따라갈 수 있다. 또한 "normal subgroup이 conjugacy class들의 합집합으로 나타나야 한다"는 주장이 증명 없이 사용되었는데, Group Actions의 orbit-stabilizer 정리를 떠올리면 "conjugacy class = inner automorphism의 orbit"이라는 연결은 가능하지만, 그것이 normal subgroup의 조건과 어떻게 관련되는지는 명시적으로 설명되지 않아서 한두 번 다시 읽었다.

좋은 점들: (1) disjoint cycle 분해의 증명에서 동치관계와 quotient set을 사용하는 것이 집합론의 도구를 group 이론에 적용하는 좋은 예시다. (2) 보조정리 7의 conjugation 공식이 명제 6과 $$A_5$$ simplicity 증명에서 반복 활용되어서, "하나의 기술적 도구가 여러 결과를 증명하는" 구조가 체계적이다. (3) Vandermonde polynomial을 이용한 sign homomorphism의 구성이 독창적이고, transposition 분해 정의와의 동치성 증명이 깔끔하다.

아쉬운 점들: (1) "conjugacy class"가 정의 없이 사용되어서, Group Actions의 내용을 모르면 $$A_5$$ simplicity 증명을 따라가기 어렵다. (2) 명제 6의 증명에서 "왜 하필 $$(1\;2)$$와 $$(1\;2\;\cdots\;n)$$인가"에 대한 동기 설명이 부족하다. (3) Cayley의 정리에서 "automorphism"이라는 표현이 나오지만, group automorphism이 prior notes에서 정의된 적이 없어서 약간의 간극이 있다.

⚠️ 정의 없이 사용: `conjugacy class` (예시 13에서 갑자기 등장; Group Actions에서 $$\rho_g(x)=gxg^{-1}$$로 정의한 inner automorphism의 orbit으로 유추되지만, 이전 Marvin 노트 어디에서도 정의되지 않음)

## [군의 확장](/ko/math/group_theory/extensions)

이 글은 "어떤 group $$G$$가 주어졌을 때, $$G$$를 구성하는 '조각들'을 어떻게 복원할 수 있는가"라는 질문에서 출발한다. 짧은 완전열 $$F\overset{i}{\hookrightarrow}E\overset{p}{\twoheadrightarrow}G$$로서 group extension을 정의하는 것(정의 1)은, 대수적 구조 카테고리에서 짧은 완전열을 이미 다뤘으므로 자연스럽다. $$\ker p=\im i$$라는 조건이 "중간에 정보가 새지 않는다"는 것을 보장한다는 직관은 명확한데, $$G\cong E/\im i$$라는 것은 first isomorphism theorem로부터 바로 따라오지만, 그렇다고 $$E\cong (E/i(F))\oplus i(F)$$가 성립하지는 않는다는 관찰이 이 글 전체의 동기를 만들어낸다 — "직접곱으로 분해할 수 없는 경우가 있다"는 것이 핵심이다.

trivial extension의 세 가지 동치 조건(명제 4)이 이 글에서 가장 구조적인 결과다. $$\mathcal{E}$$가 trivial이 되려면 (1) $$F\rightarrow F\oplus G\rightarrow G$$와 isomorphic하거나, (2) retraction $$r:E\rightarrow F$$가 존재하거나, (3) section $$s:G\rightarrow E$$가 존재하면서 $$s(G)$$가 $$i(F)$$의 centralizer에 포함되거나 — 이 셋이 동치라는 것이다. 집합론 카테고리에서 Retraction과 Section을 정의할 때 "함수"로서 다뤘는데, 여기서는 group homomorphism으로서의 retraction과 section이 등장한다는 것이 차이다. 증명에서 $$\mathcal{E}$$가 trivial이면 $$u:F\oplus G\rightarrow E$$라는 isomorphism으로부터 retraction과 section을 각각 $$\pr_1\circ u$$와 $$u^{-1}\circ\iota_2$$로 만드는 것이 깔끔하고, 역방향도 $$s(G)$$와 $$i(F)$$의 관계로부터 weak direct product를 구성하는 논증이 자연스럽다. 다만 centralizer라는 용어가 대수적 구조 카테고리의 Group Actions에서 정의된 것인데, 이 글에서는 별도의 설명 없이 사용되어서 prior knowledge에 의존해야 했다.

central extension(정의 5)은 $$i(F)\subseteq C(E)$$라는 조건으로 정의되는데, 이는 "$$F$$의 원소들이 $$E$$의 모든 원소와 가환한다"는 것이고, 이 가정 하에서는 section의 조건이 단순화될 것이라는 관찰(명제 4 뒤의 설명)이 직관적이다. $$i(F)$$가 $$E$$의 center에 포함되면 $$s(G)$$와 $$i(F)$$의 관계를 무시해도 좋다는 것은, central extension이 "거의 직접곱에 가까운" 구조라는 것을 시사한다.

semidirect product(정의 6)가 이 글의 핵심 construction이다. $$N\rtimes_\tau H$$의 연산 $$(x_1,y_1)(x_2,y_2)=(x_1\tau(y_1)(x_2), y_1y_2)$$에서 $$\tau:H\rightarrow\Aut(N)$$가 "$$H$$의 원소가 $$N$$을 어떻게 뒤집는가"를 나타낸다는 것이 직관인데, $$\tau(y_1)$$이 $$x_2$$에 작용하는 것이 "왼쪽에서 $$H$$가 $$N$$을 조작한다"는 느낌이다. 대수적 구조 카테고리에서 $$\Aut(A)=\Hom_\mathcal{A}(A,A)^\times$$로 정의한 것을 여기서 직접 사용하는데, automorphism group이라는 개념이 group action과 연결되어 $$\rho:H\rightarrow\Aut(N)$$을 정의할 수 있다는 것이 명제 7의 출발점이다. $$N\rtimes_\tau H$$가 항상 trivial extension이라는 결론(명제 7)은 $$s(y)=(e_N,y)$$로 section을 만들면 $$p\circ s=\id_H$$가 되고, $$s(G)$$가 $$i(N)$$의 centralizer에 포함된다는 확인으로부터 따라오는데, 계산 자체는 간단하지만 "semidirect product는 항상 분해 가능하다"는 결론이 강력하다.

internal과 external semidirect product의 구분(따름정리 8 앞의 설명)은 솔직하게 "차이가 중요하지 않다"고 말하는 것이 좋다. $$N\cap H=\{e_G\}$$이고 $$NH=G$$이면 $$G\cong N\rtimes_\rho H$$라는 결론은, "이미 $$G$$ 안에 $$N$$과 $$H$$가 들어있는 상황에서 그 관계를 semidirect product로 읽어내는 것"인데, 이것이 group extension의 역문제 — "$$G$$가 주어졌을 때 $$N$$과 $$H$$를 찾아라" — 에 대한 하나의 해답이라는 것이 큰 그림이다.

이 글의 내용은 대수적 구조 카테고리의 Group Actions에서 다룬 group action의 구체적 활용이라는 느낌이 강하다. $$\tau:H\rightarrow\Aut(N)$$이라는 homomorphism이 group action의 한 형태이고, semidirect product의 연산이 그 action으로부터 파생된다는 것이 명확하다. 다만 "왜 $$\tau(y_1)$$이 $$x_2$$에 작용하는지가 아니라 $$x_1$$에 작용하는지"에 대한 직관이 부족해서, 정의 6의 연산 공식을 처음 봤을 때 한두 번 다시 읽었다. $$x_1$$은 "이미 왼쪽에 있는" 원소이고 $$x_2$$는 "오른쪽에서 들어오는" 원소이므로, $$H$$의 action이 $$x_2$$에 가하는 것이 자연스럽다는 것은 계산을 해보고 나서야 이해했다.

## [군의 열](/ko/math/group_theory/series_of_groups)

이 글은 commutator의 성질을 정리하는 것으로 시작해서, 두 종류의 series — lower central series와 derived series — 를 정의하고 이를 통해 nilpotent group과 solvable group을 각각 정의한다. 마지막으로 composition series와 Jordan-Hölder 정리를 다루는데, 전체적으로 "group을 더 작은 조각들로 분해하는 여러 방법"을 체계적으로 나열하는 구조다.

commutator 부분(보조정리 1, 명제 2)은 대수적 구조 카테고리의 Abelian Groups에서 $$[G,G]$$만 다뤘던 것을 임의의 $$[H,H']$$로 확장한 것이다. 보조정리 1의 일곱 개 항등식은 "단순히 전개하면 되는" 것이라고 넘어가지만, 실제로 $$[x,yz]=[x,z][x,y]^z$$ 같은 공식은 나중에 명제 2와 명제 5의 증명에서 핵심적으로 쓰이므로 가볍게 볼 것이 아니다. 특히 명제 2의 셋째 결과인 $$[H,[H',H'']]\subseteq[H'',[H',H]][H',[H'',H]]$$ — Witt 공식이라 불리는 것 — 은 lower central series의 inclusion $$[C_m(G),C_n(G)]\subseteq C_{m+n}(G)$$를 증명하는 데 필요한데, 증명에서 $$u=h^{(h')^{-1}}$$로 치환하는 기법이 예상치 못한 방향이라서 한두 번 다시 읽었다.

lower central series $$C_n(G)$$의 정의(정의 3) 자체는 $$C_{n+1}(G)=[G,C_n(G)]]$$라는 재귀식으로 간단하지만, 이것이 "center를 반복적으로 취하는 것"이라는 직관이 명제 7에서 명확해진다: nilpotent group of class $$\leq n$$은 $$G$$의 center에 포함되는 subgroup $$A$$를 quotient 해서 class $$\leq n-1$$의 nilpotent group을 얻을 수 있다는 characterization이 그것이다. 이 직관대로라면 nilpotent group은 $$\{e\}$$에서 시작해서 central extension을 $$n$$번 반복해서 얻어지는 것이고, 이는 Extensions 글의 central extension 정의와 자연스럽게 연결된다.

derived series $$D_n(G)$$의 정의(정의 9)는 $$D_{n+1}(G)=[D_n(G),D_n(G)]]$$로, "commutator를 반복 취하는" 것인데, $$D_1(G)=[G,G]=C_2(G)$$이고 $$D_n(G)\subseteq C_{2^n}(G)$$라는 포함관계(명제 5 뒤의 설명)가 성립하므로 nilpotent $$\implies$$ solvable이 자연스럽게 따라온다. 반면 solvable $$\not\implies$$ nilpotent라는 것도 직관적으로 납득이 가는데, $$S_3$$이 solvable하지만 nilpotent가 아닌 전형적인 예시라는 것을 알고 있으니 — 비록 이 글에서는 명시적으로 다루지 않지만 — "non-abelian simple group이 없는 것이 solvable의 조건이고, center가 충분히 큰 것이 nilpotent의 조건"이라는 차이가 느껴진다.

Jordan-Hölder 정리(정리 16)는 이 글의 백미다. Zassenhaus 보조정리(보조정리 14)의 lattice 다이어그램이 핵심인데, $$H'(H\cap K)$$와 $$K'(K\cap H)$$의 관계를 $$H\cap K$$의 normal subgroup들의 교차로 읽어내는 것이 대수적 구조 카테고리의 Isomorphism Theorems를 직접 활용하는 좋은 예다. Schreier 정리(명제 15)가 "임의의 두 subnormal series를 동등한 refinement로 만들 수 있다"는 것이고, 여기서 composition series의 존재 가정을 붙이면 Jordan-Hölder가 나오는 구조가 깔끔하다. 다만 Zassenhaus 보조정리의 증명이 "$$H\cap K$$의 normal subgroup들의 교차"라는 핵심 아이디어는 명확한데, $$H'(H\cap K')=H'(H'\cap K)(K'\cap H)$$라는 등식(식 (1) 부근)이 Isomorphism Theorems의 어떤 결과로부터 오는지 한참 찾았다 — 본문에서 [\[대수적 구조\] §군 동형사상, ⁋정리 5](/ko/math/algebraic_structures/isomorphism_theorems#thm5)를 인용하고 있지만, 그 정리의 정확한 형태를 모르면 이 부분이 막힌다.

좋은 점들: (1) commutator의 일반적 성질부터 시작해서 lower central series → derived series → composition series로 이어지는 진행이 "점점 일반화하는" 구조라서, 각 정의가 이전 것의 특수화라는 것이 명확하다. (2) 명제 7과 명제 12의 동치 조건 구조가 대칭적이라서 nilpotent와 solvable의 차이를 한눈에 비교할 수 있다. (3) Jordan-Hölder 정리의 증명 전개(Zassenhaus → Schreier → Jordan-Hölder)가 "보조정리들을 쌓아서 큰 정리를 만드는" 전형적인 대수학적 방법론을 잘 보여준다.

아쉬운 점들: (1) Witt 공식(명제 2 셋째)의 증명에서 $$u=h^{(h')^{-1}}$$로 치환하는 동기가 불명확하다 — "왜 갑자기 conjugation을 하나"라는 질문에 대한 답이 없다. (2) Zassenhaus 보조정리의 lattice 다이어그램이 있긴 하지만, $$H'(H\cap K')=H'(H'\cap K)(K'\cap H)$$라는 핵심 등식의 유도 과정이 압축되어 있어서 Isomorphism Theorems의 내용을 정확히 기억하지 못하면 막힌다. (3) nilpotent group의 예시가 전혀 없어서, "실제로 어떤 group이 nilpotent이고 어떤 것이 아닌지"에 대한 감을 잡기 어렵다 — $$p$$-group이 nilpotent라는 사실은 Sylow 정리 글에서 나오지만, 이 글만으로는 그 연결을 알 수 없다.

## [실로우 정리](/ko/math/group_theory/Sylow_theorems)

이 글은 유한군의 $$p$$-subgroup을 체계적으로 분석하는 Sylow의 세 정리를 다룬다. 정의 1에서 $$p$$-group을 "$$p$$의 거듭제곱 크기의 유한군"으로 정의하는 것은 간단하지만, 보조정리 2의 $$p$$-group action 고정점 공식 $$\lvert E^G\rvert\equiv\lvert E\rvert\pmod{p}$$가 이 글 전체의 기술적 핵심이다. Group Actions에서 orbit-stabilizer 정리와 orbit의 크기가 subgroup의 index라는 결과를 이미 봤으므로, "orbit의 크기가 $$p$$의 거듭제곱이고 고정점이 아닌 원소들의 합집합은 이들의 합"이라는 논증은 깔끔하게 따라온다. 특히 $$E=G$$에 inner action을 적용하면 $$E^G=C(G)$$가 되어 $$p$$-group의 center가 non-trivial이라는 결론(정리 3 앞의 관찰)이 나오는데, 이는 Series of Groups에서 nilpotent group의 center가 non-trivial이라는 것과 직접 연결된다.

정리 3($$p$$-group에 대한 central series의 존재)의 증명 구조가 인상적이다. 귀납법을 사용하면서, $$C(G)\neq\{e\}$$에서 order $$p$$의 원소를 찾아서 quotient하고, 귀납적 가정을 적용한 뒤 inverse image를 취하는 것인데, 이는 Series of Groups의 명제 7("$$G/Z(G)$$가 class $$\leq n-1$$이면 $$G$$는 class $$\leq n$$")과 정확히 같은 논리다. 이를 통해 $$p$$-group이 항상 nilpotent라는 결론이 나오고, 이는 Series of Groups에서 nilpotent의 동치 조건 중 하나를 확인하는 것이어서 두 글 사이의 연결이 자연스럽다. 다만 이 증명에서 "왜 order $$p$$인 원소를 $$C(G)$$에서 찾는지"에 대한 동기가 약간 생략되어 있는데, center의 원소를 quotient하면 정확히 $$C(G/H)$$ 안에서 원래 center의 흔적을 추적할 수 있다는 직관을 한 문장이라도 추가했으면 좋았을 것 같다.

명제 4는 $$p$$-group의 subgroup 구조를 제약하는 결과인데, $$H\subsetneq G$$이면 $$N_G(H)\supsetneq H$$라는 것이 "$$p$$-group에서는 자기 자신을 정규화하는 원소가 항상 더 있다"는 뜻이고, 이는 nilpotent group의 특성을 보여주는 좋은 예다. 다만 normalizer라는 용어가 대수적 구조 카테고리의 Group Actions에서 정의된 것인데, 이 글에서는 별도 설명 없이 사용된다.

Sylow $$p$$-subgroup의 정의(정의 5)는 "$$p$$-group이면서 index가 $$p$$의 배수가 아닌 subgroup"인데, $$\lvert G\rvert=p^rm$$ ($$p\nmid m$$)일 때 order가 정확히 $$p^r$$인 subgroup이라는 것이 핵심이다. 정리 7(존재성)의 증명이 이 글에서 가장 기술적으로 복잡한 부분이다. 보조정리 6에서 $$\binom{n}{p^r}\not\equiv 0\pmod{p}$$를 보이는 것이 첫 번째 고비인데, $$G\times S$$의 크기 $$p^r$$짜리 부분집합들의 집합 $$E$$ 위에 $$G$$가 left translation으로 act하는 구조를 생각하는 것이 창의적이다. $$E^G$$의 원소가 $$G\times\{s\}$$ 꼴이라는 관찰이 핵심인데, "부분집합이 $$G$$의 action에 의해 고정되려면 $$G$$ 전체를 포함해야 한다"는 것이 직관이다. 이로부터 $$\lvert E\rvert\equiv m\not\equiv 0\pmod{p}$$를 얻고, orbit-stabilizer를 적용해서 order $$p^r$$의 stabilizer를 찾는 논증이 이어진다. 계산 자체는 따라갔지만, "$$G\times S$$라는 곱집합을 왜 갑자기 도입하는가"에 대한 직관이 없어서 처음 읽을 때 한두 번 멈췄다 — $$G$$ 자신을 사용하면 action이 regular해서 고정점이 없으므로, "외부의 $$m$$개 원소를 붙여서 action의 fixed point를 만들어낸다"는 것이 아이디어라는 것을 나중에야 파악했다.

정리 8이 Sylow 정리의 핵심이다. 첫째, Sylow $$p$$-subgroup들은 서로 conjugate하다는 것의 증명에서 $$E=G/P$$ 위에 $$H$$가 act하는 것을 생각하는 것이 좋은데, orbit-stabilizer를 사용해서 $$H\subseteq gPg^{-1}$$을 보이고, $$H$$가 Sylow이면 크기가 같으므로 같다는 논증이 간결하다. 둘째, 모든 $$p$$-group이 어떤 Sylow에 포함된다는 것도 같은 방법으로 따라온다. "$$n_p\equiv 1\pmod{p}$$"라는 뒷부분의 증명이 특히 흥미로운데, $$\Syl_p(G)$$ 위에 $$P$$가 inner automorphism으로 act하는 것을 생각하고, $$P$$ 자신이 유일한 fixed point임을 보이는 것이 핵심이다. $$Q$$가 다른 fixed point라면 $$P\subseteq N_G(Q)$$이고, $$P$$와 $$Q$$가 모두 $$N_G(Q)$$의 Sylow이므로 conjugate해야 한다는 논증이 깔끔하다. 다만 "왜 $$N_G(Q)$$ 안에서의 conjugacy가 $$G$$ 안에서의 conjugacy를 주는지"에 대한 한 줄의 설명이 있었으면 더 좋았을 것 같다.

예시 13($$\lvert G\rvert=15$$인 group의 분류)은 Sylow 정리의 전형적인 활용이다. $$n_3\equiv 1\pmod{3}$$이고 $$5\mid n_3$$이면 $$n_3=1$$이라는 것, $$n_5\equiv 1\pmod{5}$$이고 $$3\mid n_5$$이면 $$n_5=1$$이라는 것이 모두 간단한 수론적 계산인데, 이로부터 $$P_3$$와 $$P_5$$가 모두 normal이고 교차가 trivial이므로 $$G\cong\mathbb{Z}/3\mathbb{Z}\times\mathbb{Z}/5\mathbb{Z}$$라는 결론이 나온다. Extensions에서 다룬 semidirect product의 관점에서 보면, $$\Aut(\mathbb{Z}/5\mathbb{Z})\cong\mathbb{Z}/4\mathbb{Z}$$이고 homomorphism $$\mathbb{Z}/3\mathbb{Z}\to\mathbb{Z}/4\mathbb{Z}$$는 trivial이므로 semidirect product가 자동으로 direct product가 되는 것인데, 이 연결을 명시했으면 Extensions 글과의 관계가 더 명확했을 것 같다.

좋은 점들: (1) 보조정리 2라는 하나의 기술적 도구가 $$p$$-group의 center non-triviality, Sylow 존재성, $$n_p\equiv 1\pmod{p}$$ 등 이 글의 모든 주요 결과를 증명하는 데 사용되어서 구조가 매우 깔끔하다. (2) orbit-stabilizer 정리가 Group Actions에서 이미 다뤄진 것을 여기서 반복 활용하는 것이 "이전 글의 도구를 구체적 문제에 적용하는" 좋은 예다. (3) 예시 13이 Sylow 정리의 실제 활용을 보여주어서, 추상적 정리의 동기를 제공한다.

아쉬운 점들: (1) 보조정리 6의 증명에서 $$G\times S$$를 도입하는 동기가 불명확하다 — "왜 $$G$$ 자체를 사용하지 않고 외부 집합 $$S$$를 붙이는지"에 대한 직관적 설명이 없다. (2) 정리 8의 뒷부분 증명에서 $$N_G(Q)$$ 안에서의 conjugacy가 $$G$$ 안에서의 conjugacy를 주는 논증이 압축되어 있다. (3) $$p$$-group의 실제 예시(예: quaternion group $$Q_8$$, dihedral group $$D_4$$)가 없어서, "어떤 $$p$$-group이 non-abelian이고 어떤 구조를 가지는지"에 대한 감을 잡기 어렵다.

### 카테고리 회고

군론 카테고리는 대수적 구조에서 다룬 추상적 group 이론이 구체적인 대상에서 어떻게 작동하는지를 보여주는 네 글로 구성되었다. 대칭군에서 구체적 계산과 Cayley의 정리로 시작해서, group extension과 semidirect product를 통해 "group을 조립하는 방법"을 익히고, series of groups로 nilpotent/solvable이라는 분류 개념을 잡고, Sylow 정리로 유한군의 $$p$$-subgroup 구조를 완전히 장악하는 흐름이 잘 짜여 있다. 가장 막혔던 지점은 Sylow 정리 증명에서 $$G\times S$$를 도입하는 동기 파악이었고, Witt 공식의 conjugation 치환 기법이 왜 작동하는지 이해하는 데 시간이 걸렸다. 다음 환론 카테고리에서는 group의 "덧셈" 쪽 구조인 ring으로 넘어가는데, group extension에서 본 exact sequence의 아이디어가 ring에서도 반복될 것이라는 기대가 있다.
