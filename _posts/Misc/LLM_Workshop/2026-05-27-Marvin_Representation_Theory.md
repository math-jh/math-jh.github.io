---
title: "Marvin의 독서 노트 — 표현론"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_representation_theory

author: Marvin
date: 2026-05-27
last_modified_at: 2026-05-27
weight: 110
toc: true
---

## [유한군의 표현론](/ko/math/representation_theory/representations_of_finite_groups)

표현론 카테고리의 첫 글은 "group이 벡터공간 위에서 어떻게 작용하는가"라는 질문에서 출발한다. 대수적 구조 카테고리에서 group action을 $$G\times X\rightarrow X$$로 정의할 때 $$X$$가 단순한 집합이었다면, 여기서는 $$X$$가 벡터공간 $$V$$이고 각 $$\rho(g,-)$$가 linear map이라는 추가 조건이 붙는 것이 representation의 정의(정의 1)다. 이 정의를 $$G\rightarrow\Aut(V)$$라는 homomorphism으로 읽는 것도 가능한데, 대수적 구조 카테고리에서 group homomorphism의 정의를 이미 봤으므로 "$$G$$의 원소가 $$V$$의 automorphism으로 대응된다"는 것이 자연스럽게 와닿는다. $$G$$-invariant subspace와 subrepresentation(정의 2)의 정의는 $$\mathbb{C}[G]$$-submodule이라는 관점에서 자연스럽게 이해할 수 있다 — $$V$$가 irreducible representation인 것은 $$\mathbb{C}[G]$$-module로서 simple module인 것과 동치하다. Representation 위의 연산들(정의 3) 중 tensor product와 $$\Hom$$의 $$G$$-action 정의가 처음에는 인위적으로 느껴졌는데, group algebra의 coproduct $$\mathbb{C}[G]\rightarrow\mathbb{C}[G]\otimes\mathbb{C}[G]$$와의 관계(명제 4 뒤의 설명)를 알고 나면 "왜 하필 이 공식인가"에 대한 답이 된다. 범주론 카테고리에서 coproduct를 다루긴 했지만, group algebra의 coproduct가 $$\delta_x\mapsto\delta_x\otimes\delta_x$$로 주어진다는 것은 이 글에서 처음 봤고, 이것이 convolution product와 연결된다는 것도 새롭게 알게 된 점이다. 특히 $$(\delta_x\ast\delta_y)\cdot v=\delta_x\cdot(\delta_y\cdot v)$$라는 식이 왜 convolution product를 선택해야 하는지에 대한 필연성을 보여줘서, 대수적 구조 카테고리에서 다룬 $$A$$-module의 일반 이론이 구체적으로 어떻게 작동하는지를 이해하는 데 도움이 됐다. $$\Rep_\mathbb{C}(G)\cong\lMod{\mathbb{C}[G]}$$라는 categorical equivalence(명제 4)는, 대수적 구조 카테고리에서 $$\lMod{A}$$의 정의를 이미 봤으므로 "$$G$$-representation을 다루는 것이 $$\mathbb{C}[G]$$-module을 다루는 것과 같다"는 결론이 자연스럽다. Maschke의 정리(따름정리 7)의 증명이 놀랍도록 간결하다 — $$G$$-invariant inner product의 존재(명제 6)로부터 orthogonal complement가 $$G$$-invariant이라는 것이 전부인데, 이 아이디어의 핵심은 "$$G$$의 작용들을 모두 평균내어 $$G$$-invariant한 대상을 얻는다"는 것이고, $$V^G$$로의 projection $$v\mapsto\frac{1}{|G|}\sum_{g\in G}g\cdot v$$에서 이미 이 아이디어가 나타나 있다. 선형대수 카테고리에서 $$\mathbb{C}^n$$의 직교보충萣리를 봤지만, 그것이 group action과 만나면 이렇게 강력한 결과가 된다는 것이 인상적이다. $$\mathbb{C}[G]$$가 semisimple ring이라는 결론은, 환론 카테고리에서 다뤘을 semisimple ring의 이론과 직접 연결된다 — 본문에서 Artin-Wedderburn 정리를 인용하고 있고, $$\mathbb{C}[G]\cong\bigoplus\Mat_{n_i}(\mathbb{C})$$라는 분해가 irreducible representation들의 정보를 담고 있다는 것이 다음 글(표현의 지표)로의 연결고리다. Schur의 보조정리(보조정리 8)의 증명은 kernel과 image를 사용하는 것이 대수적 구조 카테고리의 첫 동형사상 정리를 떠올리게 한다 — $$G$$-map의 kernel이 $$G$$-submodule이라는 것과 irreducible의 정의가 만나면 "zero이거나 isomorphism"이라는 결론이 바로 나온다. Isotypical summand와 multiplicity(정의 10)의 정의는 $$\Hom_G(W,V)$$가 $$W$$가 $$V$$ 안에 얼마나 들어있는지를 센다는 것인데, 이 $$\Hom_G$$가 정확히 group algebra $$\mathbb{C}[G]$$-module으로서의 $$\Hom$$이라는 것이 categorical equivalence의 또 다른 실현이다. 이 글의 흐름 전체가 "group action + 선형 구조 = representation"이라는 아이디어를 체계적으로 전개하는 것이고, group algebra라는 다리가 두 세계를 잇고 있다는 것이 큰 그림이다.

좋은 점들: (1) group algebra의 convolution product 도입이 $$G$$-representation의 연산들(특히 tensor product와 $$\Hom$$)을 설명하는 데 필수적이라는 것이 명확하게 드러나서, "왜 group algebra를 알아야 하는가"에 대한 답이 된다. (2) Maschke의 정리의 증명이 $$G$$-invariant inner product → orthogonal complement → direct sum이라는 세 단계로 압축되어 있어서, "평균내기"라는 아이디어가 어떻게 구체적으로 작동하는지를 보여준다. (3) $$\Rep_\mathbb{C}(G)\cong\lMod{\mathbb{C}[G]}$$라는 equivalence가 이 글의 모든 정의와 명제를 하나의 프레임워크로 묶어주는 역할을 한다.

아쉬운 점들: (1) group algebra의 정의가 별도의 글이나 섹션으로 분리되어 있지 않아서, convolution product의 유도 과정이 이 글 안에서 압축되어 있다 — 대수적 구조 카테고리의 Algebras에서 $$\mathbb{C}[G]$$를 다루긴 했지만, convolution product까지는 안 다룬 것으로 기억한다. (2) Artin-Wedderburn 정리가 인용되고 있지만(`$$\mathbb{C}[G]\cong\bigoplus\Mat_{n_i}(\mathbb{C})$$`, 식 (1)), 이것이 정확히 어떤 내용인지에 대한 설명이 없어서, commutative algebra 카테고리의 내용을 정확히 모르면 이 부분이 막힌다. (3) $$V^G$$로의 projection이 "averaging"이라는 아이디어인데, 이것이 왜 $$\mathbb{C}$$에서만 작동하는지(양의 특성 0 가정)에 대한 언급이 없어서, 다른 ground field에서는 Maschke가 실패할 수 있다는 것을 알 수 없다.

⚠️ Artin-Wedderburn 정리: 본문에서 `$$\mathbb{C}[G]\cong\bigoplus\Mat_{n_i}(\mathbb{C})$$`를 인용할 때 사용되지만, 이전 Marvin 노트에서 정의되었는지 불명확하다. Commutative Algebra 노트에서 다뤘을 가능성이 높으나 확인이 필요하다.

⚠️ `convolution product`: group algebra $$\mathbb{C}[G]$$의 곱셈으로 이 글 안에서 정의되지만, group algebra의 일반적인 맥락에서의 위치가 명확하지 않다.

⚠️ `simple module`: 본문에서 "irreducible representation = simple $$\mathbb{C}[G]$$-module"이라고 언급되지만, simple module 자체의 정의가 이전 Marvin 노트에서 명시적으로 다뤄졌는지 불명확하다.

## [표현의 지표](/ko/math/representation_theory/character_theory)

표현론의 두 번째 글로, character function을 정의하고 irreducible character들의 orthonormality를 증명한 뒤, regular representation의 decomposition을 character로 재도출한다. 출발점은 정의 1인데, representation $$\rho:G\rightarrow\Aut(V)$$에 대응하는 character $$\rchi_\rho(g)=\tr(\rho(g))$$를 정의하는 것이 전부다. trace라는 선형대수학의 불변량이 representation을 분류하는 데 이렇게 강력한 도구가 된다는 것이 놀랍다 — $$\rchi_\rho(e)=\dim V$$라는 관찰만으로도 character가 representation의 차원 정보를 담고 있다는 것이 명확하다. 명제 2의 세 가지 성질($$\rchi_{V\oplus W}=\rchi_V+\rchi_W$$, $$\rchi_{V\otimes W}=\rchi_V\rchi_W$$, $$\rchi_{V^\ast}=\overline{\rchi}_V$$)은 trace의 additivity와 multiplicativity로부터 바로 나오는데, 특히 tensor product의 character가 곱으로 주어진다는 것이 인상적이다 — 선형대수학 카테고리에서 tensor product의 trace가 $$\tr(A\otimes B)=\tr(A)\tr(B)$$라는 것을 봤으므로 자연스럽다. $$\rchi_\rho$$가 conjugacy class 위에서 상수라는 관찰(식 직전)은 $$\tr(ABA^{-1})=\tr(B)$$라는 선형대수학의 기본 사실로부터 나오고, 이것이 class function(정의 3)의 정의와 직결된다.

정의 4의 inner product $$\langle\rchi_1,\rchi_2\rangle=\frac{1}{|G|}\sum_{g\in G}\rchi_1(g)\overline{\rchi_2(g)}$$는 전 글에서 봤던 $$G$$-invariant averaging 아이디어의 직접적 활용이다. $$U^G$$의 차원을 $$\frac{1}{|G|}\sum\rchi(g)$$로 계산하는 식 (1)이 이 averaging의 trace 버전인데, $$\Hom_\mathbb{C}(V,W)^G=\Hom_G(V,W)$$라는 관찰과 결합되어 $$\dim\Hom_G(V,W)=\langle\rchi_W,\rchi_V\rangle$$라는 핵심 식을 만들어내는 과정이 우아하다. Schur의 보조정리(전 글 보조정리 8)를 적용하면 irreducible representation들의 character가 orthonormal set을 이룬다는 결론이 바로 나오는데, 이 orthonormality가 이후 이론 전체의 기초가 된다는 것을 실감한다. $$\mathbb{C}_\class(G)$$의 차원이 conjugacy class의 개수와 같으므로, irreducible representation의 수가 conjugacy class의 수를 초과할 수 없다는 부수적 결론도 얻어진다.

Regular representation의 character 계산(식 (2))이 이 글에서 가장 계산적으로 인상적인 부분이다. $$\mathbb{C}[G]$$를 basis $$\{\delta_g\}$$로 보고 각 $$\rho_\reg(g)$$를 행렬로 나타내면, $$g\neq e$$일 때 basis를 permutation하므로 diagonal이 모두 0이고, $$g=e$$일 때는 $$|G|$$라는 것이 핵심이다. 이 character를 irreducible character들로 분해하면 $$\rchi_{\mathbb{C}[G]}=\sum(\dim V_i)\rchi_{V_i}$$가 되고, 이것이 곧 $$\mathbb{C}[G]\cong\bigoplus V_i^{\dim V_i}$$라는 Artin-Wedderburn decomposition을 character로 재도출한 것이다 — 전 글에서 group algebra의 coproduct 구조로 증명했던 것과 같은 결론에 character라는 다른 도구로 도달하는 것이 수학의 다면성을 보여준다.

Projection formula(보조정리 5)의 증명이 이 글의 백미다. class function $$\phi$$와 representation $$V$$에 대해 $$\rho_\phi=\sum\phi(g)\rho(g)$$를 정의하면, $$\phi$$가 class function이라는 것과 $$\rho_\phi$$가 $$G$$-map이라는 것이 동치라는 결과인데, 증명이 $$hgh^{-1}$$에 대한 variable change 하나로 끝나는 것이 놀랍다. 여기에 Schur의 보조정리를 적용하면 $$\rho_{\overline{\phi}}$$가 $$\lambda\id_V$$라는 것이 나오고, $$\langle\rchi_V,\phi\rangle=0$$이면 $$\lambda=0$$이며, 이것이 모든 irreducible representation에서 $$0$$이면 regular representation에서도 $$0$$이므로 $$\phi=0$$이라는 논증 — irreducible character들이 $$\mathbb{C}_\class(G)$$의 basis를 이룬다는 결론이 깔끔하다. 이 증명의 핵심이 "averaging → $$G$$-map → Schur → regular representation"이라는 네 단계를 거치는 것인데, 전 글의 결과들이 모두 사용되는 종합적 논증이다.

$$S_3$$의 예시가 이론을 구체적으로 확인하는 데 좋다. 세 irreducible representation — trivial $$(1,1,1)$$, sign $$(1,-1,1)$$, standard $$(2,0,-1)$$ — 이 orthonormal이라는 확인과, regular representation의 character $$\rchi_{\mathbb{C}[S_3]}=\rchi_0+\rchi_\sgn+2\rchi_\std$$가 차원 공식 $$6=1^2+1^2+2^2$$와 일치하는 것이 이론의 구체적 실현이다. Standard representation의 character를 직접 계산하는 방법($$V_\std$$의 basis 위에서 행렬을 구하고 trace를 취하는 것)과 decomposition $$\rchi_\perm=\rchi_0+\rchi_\std$$를 이용하는 방법을 모두 보여주는 것이 좋은데, 후자가 character의 연산적 힘을 잘 보여준다.

좋은 점들: (1) $$\Hom_G(V,W)=\Hom_\mathbb{C}(V,W)^G$$라는 관찰이 averaging 아이디어와 character theory를 잇는 핵심 다리 역할을 하며, 식 (1)의 일반화가 자연스럽게 이루어진다. (2) Projection formula의 증명이 four step으로 압축되어 있어서 각 단계가 어디서 오는지 명확하다. (3) $$S_3$$의 예시가 이론의 모든 핵심 결과(orthonormality, regular representation의 decomposition, 차원 공식)를 한꺼번에 확인해준다.

아쉬운 점들: (1) $$\rchi_{V^\ast}=\overline{\rchi}_V$$의 증명에서 $$\rho(g)^\dagger=\rho(g)^{-1}$$를 사용하는데, 이것이 unitary representation을 가정하는 것인지, 아니면 Maschke의 정리로 인해 항상 unitary로 만들 수 있는 것인지 명시하지 않아서 — 전 글의 명제 6($$G$$-invariant inner product의 존재)을 떠올리면 후자라는 것을 알 수 있지만, 이 글만 읽으면 어떤 가정이 숨어있는지 불명확하다. (2) Projection formula의 증명 마지막 단계에서 "regular representation에서 $$\sum\overline{\phi(g)}g$$를 $$\delta_e$$에 작용시키면 $$\sum\overline{\phi(g)}g$$"라는 계산이 $$\mathbb{C}[G]$$의 원소를 $$G$$의 원소로 동일시하고 있는데, group algebra의 정의를 이 글에서 다시 언급하지 않아서 notation이 갑자기 바뀌는 느낌이 있다.

## 카테고리 회고

표현론은 두 글밖에 안 되지만, group algebra라는 다리가 group action과 선형 구조를 잇고 있다는 하나의 아이디어가 전체를 관통한다. 첫 글에서 $$\Rep_\mathbb{C}(G)\cong\lMod{\mathbb{C}[G]}$$라는 categorical equivalence를 세우고, 두 번째 글에서 character라는 불변량을 통해 이 equivalence의 구체적 계산을 수행하는 흐름이 깔끔하다. Prior 카테고리들 중 환론(group algebra의 ring 구조)과 선형대수학(trace, tensor product의 불변량)의 결과가 가장 직접적으로 사용되었고, 대수적 구조의 group action 이론이 representation의 정의에 내장되어 있다. 가장 막혔던 지점은 projection formula의 증명에서 regular representation으로의 reduction인데, group algebra의 원소와 $$G$$의 원소 사이의 notation 전환이 한 틱 늦게 따라갔다.
