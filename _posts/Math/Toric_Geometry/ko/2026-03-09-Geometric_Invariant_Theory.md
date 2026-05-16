---
title: "Geometric invariant theory 입문"
excerpt: "Reductive group action에 대한 quotient를 정의하는 GIT의 기초를 다룬다."

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/geometric_invariant_theory

header:
    overlay_image: /assets/images/Math/Toric_Geometry/geometric_invariant_theory.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-09
last_modified_at: 2026-03-09
weight: 5
published: false
---

대수기하학에서 군이 다양체에 작용할 때 그 quotient를 어떻게 다양체로 실현할 것인가는 본질적인 어려움을 동반한다. 가령 $$\mathbb{C}^\ast$$가 $$\mathbb{C}^2$$ 위에 $$t\cdot(z_1,z_2)=(tz_1,tz_2)$$로 작용할 때, 원점은 닫힌 궤도이지만 다른 모든 궤도는 그 폐포에 원점을 포함하므로 set-theoretic quotient $$\mathbb{C}^2/\mathbb{C}^\ast$$에는 Hausdorff에 해당하는 분리 성질이 결여된다. Mumford의 *geometric invariant theory<sub>기하학적 불변량이론</sub>* (이하 GIT)는 이러한 상황에서 *어떤 점을 제거해야 잘 정의된 quotient를 얻는가*라는 물음에 체계적으로 답한다. 본 글에서는 toric variety의 Cox construction([§Cox construction과 GIT quotient](/ko/math/toric_geometry/cox_construction))으로 나아가기 위한 사전지식으로서 reductive group action의 quotient 이론의 핵심 개념을 정리한다.

이하에서 $$G$$는 $$\mathbb{C}$$ 위의 *reductive algebraic group<sub>약화군</sub>*, 즉 unipotent radical이 자명한 affine algebraic group을 의미하며 ([\[스킴\] §대수적 군, ⁋정의 15](/ko/math/scheme_theory/algebraic_groups#def15)), 대표적으로 $$\mathbb{C}^\ast$$, $$(\mathbb{C}^\ast)^k$$, $$\GL_n$$, $$\SL_n$$ 등이 이에 속한다 ([\[스킴\] §대수적 군, ⁋예시 16](/ko/math/scheme_theory/algebraic_groups#ex16)). $$X$$는 $$\mathbb{C}$$ 위의 algebraic variety이며, $$G$$의 algebraic action $$G\times X\to X$$가 주어졌다 하자 ([\[스킴\] §대수적 군, ⁋정의 4](/ko/math/scheme_theory/algebraic_groups#def4)).

## Quotient의 두 정의

군 작용에 대한 quotient를 정의하는 방식은 *어떤 보편 성질을 만족하는 morphism인가*와 *집합으로서 어떤 동치류를 잡는가*의 두 관점으로 갈린다. 전자는 categorical, 후자는 set-theoretic 관점이며, GIT의 핵심 통찰은 이 두 관점이 일반적으로 일치하지 않는다는 점에 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$G$$가 작용하는 variety $$X$$에 대하여, morphism $$\varphi : X \to Y$$가 *categorical quotient<sub>범주적 몫</sub>*라 함은 다음 두 조건을 만족함을 의미한다:

1. $$\varphi$$는 $$G$$-invariant이다. 즉 모든 $$g \in G$$에 대해 $$\varphi\circ g = \varphi$$가 성립한다.
2. $$G$$-invariant morphism $$f : X \to Z$$가 주어질 때마다 유일한 morphism $$\tilde{f} : Y \to Z$$가 존재하여 $$f = \tilde{f}\circ \varphi$$를 만족한다.

</div>

위 정의는 보편 성질 그 자체로서, $$Y$$가 존재한다면 유일성은 자동으로 따른다. 다만 정의는 $$Y$$가 점으로 붕괴할 가능성을 배제하지 않으며, 실제로 $$\mathbb{C}^\ast$$의 $$\mathbb{C}^2$$ 위 scaling action의 경우 categorical quotient는 한 점에 불과하다 ([예시 9](#ex9)). 이는 모든 $$G$$-invariant 정칙 함수가 상수임을 반영한다. 즉 categorical quotient는 *너무 적은 정보*를 담을 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Categorical quotient $$\varphi : X \to Y$$가 *geometric quotient<sub>기하학적 몫</sub>*라 함은 추가로 다음 조건이 성립함을 의미한다:

1. $$\varphi$$는 surjective이며, 각 $$y \in Y$$의 fiber $$\varphi^{-1}(y)$$는 정확히 하나의 $$G$$-궤도이다.
2. $$\varphi$$는 submersion, 즉 $$U\subseteq Y$$가 열린 집합인 것과 $$\varphi^{-1}(U)\subseteq X$$가 열린 $$G$$-불변 집합인 것은 동치이다.
3. 구조층의 차원에서 $$\mathcal{O}_Y = (\varphi_\ast \mathcal{O}_X)^G$$가 성립한다.

</div>

Geometric quotient는 통상 $$Y = X/G$$로 표기하며, 이때 $$Y$$의 점은 정확히 $$X$$의 $$G$$-궤도와 일대일 대응한다. Categorical quotient는 닫힌 궤도들을 한 점으로 묶을 뿐이지만 ([명제 3](#prop3)), geometric quotient는 모든 궤도를 분리한다. 직관적으로 두 개념 사이의 간극은 $$X$$ 안에 *나쁜 궤도*, 즉 다른 궤도의 폐포에 포함되는 궤도가 있을 때 발생한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Reductive group $$G$$가 affine variety $$X = \Spec A$$ ([\[스킴\] §스펙트럼, ⁋정의 1](/ko/math/scheme_theory/spectrums#def1)) 위에 작용한다고 하자. 그러면 invariant subring $$A^G \subseteq A$$ ([\[스킴\] §대수적 군, ⁋정의 14](/ko/math/scheme_theory/algebraic_groups#def14))는 finitely generated이며, 자연스러운 morphism

$$\varphi : X \longrightarrow X /\!/ G := \Spec(A^G)$$

는 categorical quotient이다. 더욱이 두 점 $$x, x' \in X$$가 $$\varphi$$에 의해 같은 상을 가질 필요충분조건은 두 궤도 폐포 $$\overline{G\cdot x}$$와 $$\overline{G\cdot x'}$$ ([\[대수적 구조\] §군의 작용, ⁋정의 13](/ko/math/algebraic_structures/group_actions#def13))가 교차하는 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$A^G$$의 유한생성성은 *Hilbert's finiteness theorem*의 결과이다. $$G$$가 reductive이므로 모든 rational $$G$$-module은 완전가약(completely reducible)이고, 그 결과 $$A$$는 trivial한 invariant 성분과 그 보충 $$G$$-불변 부분공간 $$A_0$$로 분해된다:

$$A = A^G \oplus A_0.$$

이로부터 $$A^G$$ 방향으로의 *Reynolds operator* $$R : A \to A^G$$가 정의된다. Reynolds operator는 $$A^G$$-module homomorphism이며 $$A^G$$ 위에서 항등이다. 이를 이용하면 임의의 $$G$$-불변 ideal $$I \subseteq A$$의 inverse image와 $$R(I) = I \cap A^G$$의 관계로부터 $$A^G$$의 ideal에 관한 *ascending chain condition*이 $$A$$의 그것에서 따라나오므로, $$A$$가 Noetherian이면 $$A^G$$도 Noetherian이다. 더 강한 finite generation은 $$A$$가 finitely generated $$\mathbb{C}$$-algebra일 때 별도의 논증이 필요하며, $$A^G$$가 적당한 $$G$$-stable finitely generated subalgebra의 invariants와 일치함을 보임으로써 얻어진다. ([Mum] §1.1 또는 [New] §3.4)

이제 $$\varphi$$의 categorical quotient 성질을 본다. $$G$$-invariant morphism $$f : X \to Z = \Spec B$$가 주어지면 이에 대응하는 ring homomorphism $$f^\sharp : B \to A$$의 상은 $$G$$-invariant element로 이루어지므로 $$A^G$$에 포함된다. 따라서 $$f^\sharp$$는 $$B \to A^G$$를 거쳐 분해되고, 이는 $$f$$가 $$\varphi$$를 통해 유일하게 분해됨을 뜻한다. 일반적인 affine이 아닌 $$Z$$에 대해서도 affine cover로 환원하면 동일한 결론이 따른다.

두 점이 같은 상을 가질 조건을 보인다. 두 궤도 폐포가 교차한다면 그 교집합 위에서 모든 $$G$$-invariant 함수는 두 점에서 같은 값을 가지므로, 임의의 $$f \in A^G$$에 대해 $$f(x) = f(x')$$이다. 역으로 $$\overline{G\cdot x} \cap \overline{G\cdot x'} = \emptyset$$이라 가정하자. 두 닫힌 $$G$$-불변 부분집합은 disjoint이므로 그 ideal들 $$I_x, I_{x'} \subseteq A$$에 대해 $$I_x + I_{x'} = A$$이다. Reductivity로부터 $$I_x^G + I_{x'}^G = A^G$$가 성립하며 ([Mum] §1.2의 명제), 이로부터 $$f \in A^G$$로서 $$f(x) = 0$$, $$f(x') = 1$$인 것이 존재한다. 따라서 $$\varphi(x) \ne \varphi(x')$$이다.

</details>

위 명제의 두 번째 부분이 categorical quotient와 geometric quotient의 차이를 정량화한다. 즉, $$X/\!/G$$의 한 점은 $$X$$의 *G-궤도들의 동치류*에 대응하되, 그 동치관계는 *궤도 폐포가 사슬로 연결됨*이다. 모든 궤도가 이미 닫혀 있다면 동치류는 곧 궤도 자체이고 이 경우 categorical quotient는 geometric quotient가 된다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 명제의 finite generation 부분은 $$G$$가 reductive라는 가정을 본질적으로 사용한다. Nagata는 unipotent group의 작용에 대해 invariant ring이 finitely generated가 아닐 수 있음을 보여 Hilbert의 14번째 문제의 반례를 제시하였다. 본 글에서 $$G$$를 reductive로 제한하는 것은 단순한 편의가 아니라 GIT 자체가 성립하기 위한 핵심 가정이다.

</div>

## Linearization

Affine variety에 대한 quotient는 위와 같이 invariant ring을 통해 깔끔하게 기술되지만, 일반적인 (projective 혹은 quasi-projective) variety에 대해서는 global regular function이 너무 적기 때문에 (가령 projective variety에서는 상수뿐) 직접적인 invariant ring 접근이 통하지 않는다. Mumford의 해법은 line bundle의 section ring을 invariant ring의 자리에 놓는 것이며, 이를 위해 필요한 추가 자료가 *linearization*이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$G$$가 작용하는 variety $$X$$ 위의 line bundle $$L \to X$$ ([\[대수다양체\] §선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_varieties/line_bundles#def1))에 대하여, *$$G$$-linearization*이란 $$L$$ 위의 $$G$$-action $$G\times L \to L$$로서 다음 두 조건을 만족하는 것을 의미한다:

1. 사영 $$L \to X$$는 $$G$$-equivariant이다. 즉 $$g\cdot(L_x) \subseteq L_{g\cdot x}$$가 모든 $$g\in G$$, $$x\in X$$에 대해 성립한다.
2. 각 $$g\in G$$에 대해 유도되는 fiber map $$L_x \to L_{g\cdot x}$$는 $$\mathbb{C}$$-linear isomorphism이다.

이때 쌍 $$(L, \text{linearization})$$을 *linearized line bundle*이라 부른다.

</div>

Linearization이 주어지면 $$G$$는 자연스럽게 $$H^0(X, L^{\otimes n})$$ 위에 작용한다. 구체적으로 section $$s : X \to L^{\otimes n}$$과 $$g\in G$$에 대해 $$(g\cdot s)(x) := g\cdot s(g^{-1}\cdot x)$$로 정의하면 이는 다시 $$L^{\otimes n}$$의 section이며, 이 작용은 graded ring

$$R(X, L) = \bigoplus_{n\ge 0} H^0(X, L^{\otimes n})$$

위에 graded $$G$$-action을 부여한다. 따라서 invariant subring $$R(X, L)^G$$가 잘 정의되며, 우리는 이로부터 quotient 후보 $$\Proj R(X, L)^G$$를 구성할 수 있다. 이때 $$L^{\otimes n}$$의 작용이 *서로 다른* character로 비틀려 정의될 수도 있으므로, 같은 line bundle이라 하더라도 어떤 linearization을 택했느냐에 따라 invariant section의 공간이 달라진다는 점에 주의해야 한다.

<div class="remark" markdown="1">

<ins id="rmk6">**참고 6**</ins> Torus $$G = (\mathbb{C}^\ast)^k$$가 affine variety $$X = \Spec A$$ 위에 작용하는 경우, 자명 line bundle $$L = X\times \mathbb{C}$$ 위의 linearization은 정확히 $$G$$의 character $$\chi : G \to \mathbb{C}^\ast$$ ([\[스킴\] §대수적 군, ⁋정의 10](/ko/math/scheme_theory/algebraic_groups#def10)) 하나로 결정된다: $$g\cdot(x, z) = (g\cdot x, \chi(g)z)$$. 이때 $$H^0(X, L^{\otimes n}) = A$$ 위의 작용은 $$g\cdot f = \chi(g)^n\,(g\cdot f)$$로 비틀리며, 이에 대한 invariant는

$$A^{G,\chi^n} = \{ f\in A \mid g\cdot f = \chi(g)^{-n} f \text{ for all } g\in G\}$$

라는 *semi-invariant<sub>준 불변량</sub>*의 공간이 된다. Cox construction에서 등장하는 character chamber의 의미는 이 character 선택과 직결된다.

</div>

## (Semi)stable 점과 GIT quotient

Linearization $$L$$이 주어지면, $$X$$의 각 점을 invariant section을 통해 *유효하게* 분리할 수 있느냐에 따라 분류할 수 있다. 이 분류가 GIT 안정성 이론의 출발점이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Linearized line bundle $$L$$이 주어진 상황에서, 점 $$x\in X$$가

1. *semistable<sub>준안정</sub>*이라 함은 $$n>0$$인 어떤 $$n$$과 어떤 invariant section $$s\in H^0(X, L^{\otimes n})^G$$가 존재하여 $$s(x)\ne 0$$이고 $$X_s := \{y\in X\mid s(y)\ne 0\}$$이 affine open이 되는 것을 의미한다.
2. *stable<sub>안정</sub>*이라 함은 위에 더해 $$x$$의 $$G$$-궤도가 $$X_s$$ 안에서 닫혀 있으며, $$x$$의 stabilizer $$G_x$$가 유한군임을 추가로 만족함을 의미한다.

Semistable point들의 집합을 $$X^{\mathrm{ss}}(L)$$, stable point들의 집합을 $$X^{\mathrm{s}}(L)$$로 표기한다. Semistable이 아닌 점은 *unstable<sub>불안정</sub>*이라 부른다.

</div>

정의에서 $$X_s$$가 affine으로 요구되는 것은 invariant ring을 통한 affine GIT을 local하게 적용하기 위함이다. $$L$$이 ample하다면 ([\[대수다양체\] §선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)) 충분히 큰 $$n$$에 대해 $$X_s$$는 자동으로 affine이 되므로, ample linearization을 가정하는 통상의 setup에서는 이 조건은 본질적인 제약이 아니다. 한편 $$X^{\mathrm{s}}(L) \subseteq X^{\mathrm{ss}}(L)$$이 정의에서 자명히 따르며, 두 집합은 모두 $$X$$의 Zariski 열린 부분집합이다 ([명제 8](#prop8)).

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$X^{\mathrm{ss}}(L)$$과 $$X^{\mathrm{s}}(L)$$은 모두 $$X$$의 $$G$$-불변 Zariski 열린 부분집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X^{\mathrm{ss}}(L)$$의 정의는 각 점에 대해 $$X_s$$ 꼴의 열린 affine 근방의 존재를 요구하므로, $$X^{\mathrm{ss}}(L)$$ 자체가 그러한 $$X_s$$들의 합집합이 되어 열려 있다. 또한 $$s$$가 invariant이면 $$X_s$$는 $$G$$-불변이고, 따라서 합집합도 $$G$$-불변이다.

$$X^{\mathrm{s}}(L)$$의 경우, 한 점 $$x\in X^{\mathrm{s}}(L)$$에 대해 위와 같은 $$s$$를 잡으면 $$X_s$$ 안에서 $$G\cdot x$$가 닫혀 있고 stabilizer가 유한하다. 같은 $$X_s$$ 위에서 작용은 properly discontinuous에 가깝게 행동하며, 궤도가 닫혀 있다는 조건과 stabilizer 유한 조건은 모두 $$X_s$$의 열린 부분집합 위에서 보존된다. 구체적으로, stabilizer 차원이 0이 되는 점들의 집합은 dimension semicontinuity에 의해 열려 있으며, 궤도가 닫혀 있는 점들도 같은 fiber dimension을 갖는 점들의 집합으로 표현되어 열린 조건이 된다. 따라서 $$X^{\mathrm{s}}(L)$$도 열려 있다. $$G$$-불변성은 정의 자체에서 즉시 따른다.

</details>

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9**</ins> 실제 계산에서 (semi)stable 점을 판정하는 표준 도구는 *Hilbert–Mumford numerical criterion*이다. 이는 모든 1-parameter subgroup $$\lambda : \mathbb{C}^\ast \to G$$에 대해 $$\lambda$$가 $$x$$ 위에서 정의하는 *Mumford weight* $$\mu^L(x, \lambda)$$의 부호로 stability를 판정한다는 결과이다. 즉

$$x \in X^{\mathrm{ss}}(L) \iff \mu^L(x, \lambda) \ge 0 \text{ for all } \lambda,\qquad x \in X^{\mathrm{s}}(L) \iff \mu^L(x, \lambda) > 0 \text{ for all } \lambda \ne 1.$$

본 글에서는 이 numerical criterion의 자세한 증명을 다루지 않으며, 자세한 내용은 [Mum] §2 또는 [New] §4를 참조한다.

</div>

이제 GIT quotient의 정의를 내릴 준비가 끝났다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Reductive group $$G$$가 작용하는 variety $$X$$와 ample linearized line bundle $$L$$에 대하여, *GIT quotient<sub>GIT 몫</sub>*는 다음과 같이 정의되는 사영 사상이다 ([\[스킴\] §사영스킴, ⁋정의 1](/ko/math/scheme_theory/projective_schemes#def1)).

$$X /\!/_L G := \Proj\!\bigoplus_{n\ge 0} H^0(X, L^{\otimes n})^G,\qquad X^{\mathrm{ss}}(L) \longrightarrow X /\!/_L G.$$

</div>

GIT quotient는 두 단계로 이해된다. 우선 invariant section ring $$R(X,L)^G$$의 $$\Proj$$를 취함으로써 우리는 $$X^{\mathrm{ss}}(L)$$ 위에 정의되는 categorical quotient를 얻는다. 둘째로 $$X^{\mathrm{s}}(L) \subseteq X^{\mathrm{ss}}(L)$$의 상은 $$X /\!/_L G$$의 열린 부분집합을 이루며, 그 위로 제한된 사상은 geometric quotient

$$X^{\mathrm{s}}(L) \longrightarrow X^{\mathrm{s}}(L)/G \subseteq X/\!/_L G$$

가 된다. 일반적으로 두 집합 $$X^{\mathrm{ss}}(L)$$과 $$X^{\mathrm{s}}(L)$$이 일치하면 (이를 *strict GIT* 상황이라 부른다) GIT quotient 전체가 geometric quotient가 되며, 이는 toric Cox construction의 simplicial 가정 하에서 정확히 발생하는 현상이다. 두 집합의 차이는 GIT quotient에서 *S-equivalence class*로 묶이는 strictly semistable 궤도들의 폐포가 한 점으로 식별되는 정도를 측정한다.

## 표준적 예시

가장 간단하지만 GIT의 모든 핵심 현상을 보여주는 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$G = \mathbb{C}^\ast$$가 $$X = \mathbb{C}^2$$ 위에 scaling

$$t\cdot(z_1, z_2) = (tz_1, tz_2)$$

으로 작용하는 경우를 생각하자. 우선 자명한 linearization, 즉 character $$\chi=1$$을 택한 경우의 affine GIT은 어떻게 보이는지 본다. 좌표환 $$A = \mathbb{C}[\z_1, \z_2]$$ 위의 $$G$$-작용은 $$\z_i$$를 $$t^{-1}\z_i$$로 보내며 (점 위 작용의 contravariance에 의함), 임의의 monomial $$\z_1^a \z_2^b$$는 $$t^{-(a+b)}$$ 배가 된다. 따라서

$$A^G = \mathbb{C}$$

이고, [명제 3](#prop3)에 의해 affine categorical quotient는

$$\mathbb{C}^2 /\!/ \mathbb{C}^\ast = \Spec \mathbb{C} = \{\text{pt}\}$$

한 점으로 붕괴한다. 이는 모든 비원점 궤도의 폐포가 원점을 포함하기 때문이며, 명제 3의 두 번째 부분에 따라 모든 점이 같은 동치류에 속하게 된 결과이다.

이제 비자명 character $$\chi(t) = t$$로 자명 line bundle $$L = X\times \mathbb{C}$$를 linearize하자. 그러면 invariant section은

$$H^0(X, L^{\otimes n})^{G,\chi^n} = \{ f\in \mathbb{C}[\z_1, \z_2] \mid f(tz_1, tz_2) = t^n f(z_1, z_2)\} = \mathbb{C}[\z_1, \z_2]_n,$$

즉 $$n$$차 동차다항식들의 공간이 된다. 따라서

$$\begin{aligned}
\bigoplus_{n\ge 0} H^0(X, L^{\otimes n})^{G,\chi^n} &= \bigoplus_{n\ge 0} \mathbb{C}[\z_1, \z_2]_n = \mathbb{C}[\z_1, \z_2]
\end{aligned}$$

이고, 이는 $$\mathbb{P}^1$$의 homogeneous coordinate ring과 일치한다. 그러므로

$$\mathbb{C}^2 /\!/_{\chi} \mathbb{C}^\ast = \Proj \mathbb{C}[\z_1, \z_2] = \mathbb{P}^1$$

이 된다. 한편 semistable 집합을 직접 확인하면, $$(z_1, z_2) \ne (0,0)$$인 경우 적당한 $$n$$과 $$\z_1^a \z_2^b$$ ($$a+b=n$$) 중 0이 아닌 값을 주는 것이 항상 존재하므로 모든 비원점 점은 semistable이다. 반면 원점에서는 모든 양의 차수 동차다항식이 0이므로 unstable이다. 즉

$$X^{\mathrm{ss}}(L_\chi) = \mathbb{C}^2 \setminus \{0\},\qquad X^{\mathrm{s}}(L_\chi) = \mathbb{C}^2 \setminus \{0\}$$

이며 (stabilizer가 유한하고 궤도가 닫힘은 비원점에서 직접 확인된다), 따라서 strict GIT 상황이고 GIT quotient는 geometric quotient

$$(\mathbb{C}^2 \setminus \{0\})/\mathbb{C}^\ast = \mathbb{P}^1$$

과 일치한다. 같은 variety $$\mathbb{C}^2$$, 같은 $$G$$의 작용이지만 linearization의 character 선택에 따라 quotient가 한 점에서 $$\mathbb{P}^1$$로 달라지는 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> 위 예시는 차원 $$n$$에서도 그대로 일반화된다. $$G = \mathbb{C}^\ast$$가 $$X = \mathbb{C}^n$$ 위에 표준 scaling $$t\cdot(z_1,\ldots,z_n) = (tz_1, \ldots, tz_n)$$으로 작용하고, character $$\chi(t) = t$$로 자명 line bundle을 linearize하면, 같은 계산에 의해

$$\bigoplus_{m\ge 0} H^0(\mathbb{C}^n, L^{\otimes m})^{G,\chi^m} = \mathbb{C}[\z_1, \ldots, \z_n]$$

이고

$$\mathbb{C}^n /\!/_\chi \mathbb{C}^\ast = \Proj \mathbb{C}[\z_1, \ldots, \z_n] = \mathbb{P}^{n-1}$$

이다. Semistable 점은 정확히 $$\mathbb{C}^n \setminus \{0\}$$이며, 이는 GIT quotient가 통상의 사영공간 정의

$$\mathbb{P}^{n-1} = (\mathbb{C}^n\setminus\{0\})/\mathbb{C}^\ast$$

와 일치함을 보여준다. 이는 [§아핀 토릭 다양체, ⁋예시 6](/ko/math/toric_geometry/affine_toric_varieties#ex6)에서 본 torus 자체의 description과는 다른 시점이며, 곧 살펴볼 Cox construction은 이 GIT 시점을 일반 toric variety로 확장한 것이다.

</div>

위 두 예시가 보여주는 패턴은 GIT의 본질적 메시지이다. *Categorical quotient는 닫힌 궤도들을 너무 거칠게 식별할 수 있으므로*, 적절한 linearization을 도입해 *unstable orbit을 제거*한 뒤 *남은 semistable 영역의 invariant section ring으로 $$\Proj$$를 취해야* 비로소 기하학적으로 의미 있는 quotient를 얻는다. Linearization의 선택은 toric 세계에서 character chamber, 즉 secondary fan의 chamber에 정확히 대응하며, chamber를 가로지르면 GIT quotient도 birational하게 변화한다. 이러한 *variation of GIT*가 toric variety의 birational geometry를 통제하는 골격이 된다.

---

**참고문헌**

**[Mum]** D. Mumford, J. Fogarty, F. Kirwan, *Geometric Invariant Theory*, 3rd ed., Ergebnisse der Mathematik, Springer, 1994.  
**[New]** P. E. Newstead, *Introduction to Moduli Problems and Orbit Spaces*, Tata Institute Lecture Notes, 1978.  
**[CLS]** D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011, Chapter 14.  
**[Hos]** V. Hoskins, *Geometric Invariant Theory and Symplectic Quotients*, Lecture notes, Freie Universität Berlin, 2015.
