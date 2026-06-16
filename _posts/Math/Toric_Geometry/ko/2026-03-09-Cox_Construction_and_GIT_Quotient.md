---
title: "Cox 구성과 GIT quotient"
description: "fan과 homogeneous coordinate ring을 통해 toric variety를 재구성하는 Cox의 방법을 다루며, toric variety 위의 line bundle과 coherent sheaf를 이해하는 데 핵심적인 GIT quotient의 역할을 설명한다."
excerpt: "토릭 다양체의 homogeneous coordinate ring과 GIT quotient 표현"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/cox_construction

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-09
weight: 5
published: false
---

Projective space $$\mathbb{P}^n$$은 homogeneous coordinate를 통해

$$\mathbb{P}^n = (\mathbb{C}^{n+1} \setminus \{0\}) / \mathbb{C}^\ast$$

로 나타낼 수 있다. 이 구성은 사영공간 위의 대수적 구조를 다루는 데 매우 유용하며, 가령 closed subvariety는 homogeneous ideal에 의해 정의되고 coherent sheaf는 graded module에 대응한다. Cox는 이러한 구성을 임의의 toric variety로 일반화하였다. 본 글에서는 fan $$\Sigma$$로부터 toric variety $$X_\Sigma$$를 homogeneous coordinate ring과 *GIT quotient*로 재구성하는 Cox의 방법을 설명한다. 이 구성은 toric variety 위의 line bundle이나 coherent sheaf를 다루는 데 필수적인 도구이며, 마지막에 짧게 짚을 secondary fan을 통한 birational geometry의 이해에도 직결된다. 

GIT의 기초 — reductive group, invariant ring, affine GIT quotient $$X/\!/G = \Spec A^G$$, linearization, (semi)stable 점, projective GIT quotient — 는 이미 [§대수적 군](/ko/math/scheme_theory/algebraic_groups)에서 다루었다. 본 글은 그 결과를 자유롭게 사용하며, 추가로 Cox 구성에 본질적으로 필요한 *categorical quotient vs geometric quotient*의 구분만 한 절 분량으로 정리한 뒤 본 주제로 들어간다. 이하에서 $$N \cong \mathbb{Z}^n$$은 rank $$n$$의 free abelian group, $$M = \Hom_\mathbb{Z}(N, \mathbb{Z})$$는 그 dual lattice, $$\Sigma$$는 $$N_\mathbb{R}$$ 위의 rational polyhedral fan으로 $$N_\mathbb{R}$$를 span한다고 가정한다. 각 $$\rho \in \Sigma(1)$$에 대해 $$u_\rho \in N$$은 $$\rho$$의 primitive generator이다.

## Categorical quotient와 geometric quotient

군 작용에 대한 quotient를 정의하는 방식은 *어떤 보편 성질을 만족하는 morphism인가*와 *집합으로서 어떤 동치류를 잡는가*의 두 관점으로 갈린다. 전자는 categorical, 후자는 set-theoretic 관점이며, GIT의 핵심 통찰은 이 둘이 일반적으로 일치하지 않는다는 점이다. 가령 $$\mathbb{C}^\ast$$가 $$\mathbb{C}^2$$ 위에 $$t\cdot(z_1, z_2) = (tz_1, tz_2)$$로 작용할 때, 원점은 닫힌 궤도이지만 나머지 모든 궤도의 폐포가 원점을 포함하므로 set-theoretic quotient $$\mathbb{C}^2/\mathbb{C}^\ast$$에는 분리 성질이 결여된다. 이러한 상황을 체계적으로 다루기 위해 다음 두 개념을 분리한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Algebraic group $$G$$가 작용하는 variety $$X$$에 대해, morphism $$\varphi: X \to Y$$가 *categorical quotient<sub>범주적 몫</sub>*라 함은 다음 두 조건을 만족함을 의미한다:

1. $$\varphi$$는 $$G$$-invariant이다. 즉 모든 $$g \in G$$에 대해 $$\varphi \circ g = \varphi$$.
2. $$G$$-invariant morphism $$f: X \to Z$$가 주어질 때마다 유일한 morphism $$\tilde{f}: Y \to Z$$가 존재하여 $$f = \tilde{f} \circ \varphi$$.

</div>

이는 보편 성질이므로 $$Y$$가 존재한다면 유일성은 자동이다. 다만 정의는 $$Y$$가 한 점으로 붕괴할 가능성을 배제하지 않으며, 위에서 본 $$\mathbb{C}^\ast$$의 scaling 예시에서는 실제로 categorical quotient가 한 점에 불과하다 ([예시 5](#ex5)). 즉 categorical quotient는 *너무 적은 정보*를 담을 수 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Categorical quotient $$\varphi: X \to Y$$가 *geometric quotient<sub>기하학적 몫</sub>*라 함은 추가로 다음 조건이 성립함을 의미한다:

1. $$\varphi$$는 surjective이고, 각 $$y \in Y$$의 fiber $$\varphi^{-1}(y)$$는 정확히 하나의 $$G$$-궤도이다.
2. $$\varphi$$는 submersion. 즉, $$U \subseteq Y$$가 열린 집합인 것과 $$\varphi^{-1}(U) \subseteq X$$가 열린 $$G$$-불변 집합인 것은 동치이다.
3. 구조층의 차원에서 $$\mathcal{O}_Y = (\varphi_\ast \mathcal{O}_X)^G$$.

</div>

Geometric quotient는 통상 $$Y = X/G$$로 표기하며, $$Y$$의 점은 정확히 $$X$$의 $$G$$-궤도와 일대일 대응한다. Categorical quotient는 닫힌 궤도들을 한 점으로 묶을 뿐이지만 ([명제 3](#prop3)), geometric quotient는 모든 궤도를 분리한다. 직관적으로 두 개념 사이의 간극은 $$X$$ 안에 *다른 궤도의 폐포에 포함되는 궤도*가 있을 때 발생한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Reductive group $$G$$가 affine variety $$X = \Spec A$$ 위에 작용한다고 하자. 그러면 invariant subring $$A^G \subseteq A$$ ([\[스킴\] §대수적 군, ⁋정의 14](/ko/math/scheme_theory/algebraic_groups#def14))는 finitely generated이며, 자연스러운 morphism

$$\varphi : X \longrightarrow X /\!/ G := \Spec(A^G)$$

는 categorical quotient이다 ([\[스킴\] §대수적 군, ⁋정의 17](/ko/math/scheme_theory/algebraic_groups#def17)). 더욱이 두 점 $$x, x' \in X$$가 $$\varphi$$에 의해 같은 상을 가질 필요충분조건은 두 궤도 폐포 $$\overline{G\cdot x}$$와 $$\overline{G\cdot x'}$$가 교차하는 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$A^G$$의 유한생성성은 *Hilbert finiteness theorem*의 결과이다. $$G$$가 reductive이므로 모든 rational $$G$$-module은 완전가약(completely reducible)이고 ([\[스킴\] §대수적 군, ⁋정의 15](/ko/math/scheme_theory/algebraic_groups#def15)), 그 결과 $$A$$는 trivial한 invariant 성분과 그 보충 $$G$$-불변 부분공간 $$A_0$$로 분해된다:

$$A = A^G \oplus A_0.$$

이로부터 $$A^G$$ 방향으로의 *Reynolds operator* $$R: A \to A^G$$가 정의된다. Reynolds operator는 $$A^G$$-module homomorphism이며 $$A^G$$ 위에서 항등이다. 이를 이용하면 임의의 $$G$$-불변 ideal $$I \subseteq A$$의 inverse image와 $$R(I) = I \cap A^G$$의 관계로부터 $$A^G$$의 ideal에 관한 ascending chain condition이 $$A$$의 그것에서 따라나오므로, $$A$$가 Noetherian이면 $$A^G$$도 Noetherian이다. 더 강한 finite generation은 $$A$$가 finitely generated $$\mathbb{C}$$-algebra일 때 $$A^G$$가 적당한 $$G$$-stable finitely generated subalgebra의 invariants와 일치함을 보임으로써 얻어진다 ([Mum] §1.1 또는 [New] §3.4).

이제 $$\varphi$$의 categorical quotient 성질을 본다. $$G$$-invariant morphism $$f: X \to Z = \Spec B$$가 주어지면 이에 대응하는 ring homomorphism $$f^\sharp: B \to A$$의 상은 $$G$$-invariant element로 이루어지므로 $$A^G$$에 포함된다. 따라서 $$f^\sharp$$는 $$B \to A^G$$를 거쳐 분해되고, 이는 $$f$$가 $$\varphi$$를 통해 유일하게 분해됨을 뜻한다. 일반적인 $$Z$$에 대해서는 affine cover로 환원하면 동일한 결론이 따른다.

두 점이 같은 상을 가질 조건을 보인다. 두 궤도 폐포가 교차하면 그 교집합 위에서 모든 $$G$$-invariant 함수는 두 점에서 같은 값을 가지므로, 임의의 $$f \in A^G$$에 대해 $$f(x) = f(x')$$이다. 역으로 $$\overline{G \cdot x} \cap \overline{G \cdot x'} = \emptyset$$이라 가정하자. 두 닫힌 $$G$$-불변 부분집합이 disjoint이므로 그 ideal들 $$I_x, I_{x'} \subseteq A$$에 대해 $$I_x + I_{x'} = A$$이다. Reductivity로부터 $$I_x^G + I_{x'}^G = A^G$$가 성립하며, 이로부터 $$f(x) = 0$$, $$f(x') = 1$$인 $$f \in A^G$$가 존재한다. 따라서 $$\varphi(x) \ne \varphi(x')$$이다.

</details>

위 명제의 두 번째 부분이 categorical quotient와 geometric quotient의 차이를 정량화한다. 즉 $$X/\!/G$$의 한 점은 $$X$$의 *$$G$$-궤도들의 동치류*에 대응하되, 그 동치관계는 *궤도 폐포가 사슬로 연결됨*이다. 모든 궤도가 이미 닫혀 있다면 이 동치류는 곧 궤도 자체이고 이 경우 categorical quotient는 geometric quotient가 된다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 명제의 finite generation 부분은 $$G$$가 reductive라는 가정을 본질적으로 사용한다. Nagata는 unipotent group의 작용에 대해 invariant ring이 finitely generated가 아닐 수 있음을 보여 Hilbert의 14번째 문제의 반례를 제시하였다. 본 글에서 $$G$$를 reductive로 제한하는 것은 단순한 편의가 아니라 GIT가 성립하기 위한 핵심 가정이다.

</div>

## $$\mathbb{P}^n$$을 GIT quotient로 보기

Cox 구성으로 본격적으로 들어가기 전에, 가장 간단한 toric variety인 $$\mathbb{P}^n$$이 어떻게 GIT quotient로 자연스럽게 나타나는지를 살펴보자. 이 예시는 *어떤 linearization을 택하느냐에 따라 quotient가 달라진다*는 GIT의 본질을 명확히 보여주며, 이후 일반 toric variety의 Cox 구성으로 곧장 일반화된다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$G = \mathbb{C}^\ast$$가 $$X = \mathbb{C}^2$$ 위에 scaling

$$t \cdot (z_1, z_2) = (tz_1, tz_2)$$

으로 작용한다고 하자. 우선 자명한 linearization, 즉 character $$\chi = 1$$의 경우 affine GIT을 본다. 좌표환 $$A = \mathbb{C}[\z_1, \z_2]$$ 위의 $$G$$-작용은 (이 글에서는 자매 글인 [§아핀 토릭 다양체](/ko/math/toric_geometry/affine_toric_varieties)의 *inverse 없는* convention $$t \cdot f = f \circ t$$와는 반대로, 표준 GIT 컨벤션을 따라 $$(t \cdot f)(x) = f(t^{-1} x)$$를 채택한다) $$\z_i$$를 $$t^{-1}\z_i$$로 보내며, 임의의 monomial $$\z_1^a \z_2^b$$는 $$t^{-(a+b)}$$ 배가 된다. 따라서

$$A^G = \mathbb{C}$$

이고, [명제 3](#prop3)에 의해

$$\mathbb{C}^2 /\!/ \mathbb{C}^\ast = \Spec \mathbb{C} = \{\mathrm{pt}\}$$

으로 한 점으로 붕괴한다. 모든 비원점 궤도의 폐포가 원점을 포함하여 [명제 3](#prop3)에 의해 모든 점이 같은 동치류에 속한 결과이다.

이제 비자명 character $$\chi(t) = t$$로 자명 line bundle $$L = X \times \mathbb{C}$$를 linearize ([\[스킴\] §대수적 군, ⁋정의 18](/ko/math/scheme_theory/algebraic_groups#def18))하면 invariant section은

$$H^0(X, L^{\otimes n})^{G, \chi^n} = \{f \in \mathbb{C}[\z_1, \z_2] \mid f(tz_1, tz_2) = t^n f(z_1, z_2)\} = \mathbb{C}[\z_1, \z_2]_n,$$

즉 $$n$$차 동차다항식들의 공간이다. 따라서

$$\bigoplus_{n \ge 0} H^0(X, L^{\otimes n})^{G, \chi^n} = \mathbb{C}[\z_1, \z_2]$$

이고, projective GIT quotient ([\[스킴\] §대수적 군, ⁋정의 20](/ko/math/scheme_theory/algebraic_groups#def20))는

$$\mathbb{C}^2 /\!/_\chi \mathbb{C}^\ast = \Proj \mathbb{C}[\z_1, \z_2] = \mathbb{P}^1$$

이다. Semistable 집합을 직접 확인하면 $$(z_1, z_2) \ne (0, 0)$$인 모든 점이 semistable이며 (양의 차수 동차다항식 중 0이 아닌 값을 주는 것이 존재), 원점은 unstable이다. 즉

$$X^{\mathrm{ss}}(L_\chi) = X^{\mathrm{s}}(L_\chi) = \mathbb{C}^2 \setminus \{0\}$$

이며, GIT quotient는 익숙한 geometric quotient

$$(\mathbb{C}^2 \setminus \{0\}) / \mathbb{C}^\ast = \mathbb{P}^1$$

과 일치한다. 같은 variety, 같은 군의 작용임에도 linearization의 character 선택에 따라 quotient가 한 점에서 $$\mathbb{P}^1$$로 달라진다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 같은 계산이 차원 $$n$$에서 그대로 일반화된다. $$G = \mathbb{C}^\ast$$가 $$X = \mathbb{C}^n$$ 위에 표준 scaling으로 작용하고 character $$\chi(t) = t$$로 linearize하면

$$\mathbb{C}^n /\!/_\chi \mathbb{C}^\ast = \Proj \mathbb{C}[\z_1, \ldots, \z_n] = \mathbb{P}^{n-1}$$

이고, semistable 집합은 $$\mathbb{C}^n \setminus \{0\}$$이다. 이는 통상의 사영공간 정의

$$\mathbb{P}^{n-1} = (\mathbb{C}^n \setminus \{0\}) / \mathbb{C}^\ast$$

가 GIT quotient의 특수한 경우임을 명시한다. 곧 살펴볼 Cox 구성은 이 시점을 임의의 toric variety로 확장한 것이다.

</div>

## Homogeneous coordinate ring과 irrelevant ideal

Projective space의 homogeneous coordinate ring은 $$\mathbb{C}[\x_0, \ldots, \x_n]$$으로, 각 변수가 $$\mathbb{P}^n$$의 coordinate hyperplane에 대응한다. Cox는 이를 toric variety로 확장하기 위해, fan의 1차원 cone 각각에 변수를 대응시킨다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Toric variety $$X_\Sigma$$의 *homogeneous coordinate ring* 혹은 *Cox ring*은 다음과 같이 정의된다:

$$S = \mathbb{C}[\x_\rho \mid \rho \in \Sigma(1)].$$

</div>

Cox ring $$S$$는 polynomial ring이므로 특히 UFD이다. 이로써 toric variety의 좌표환은 일반 variety보다 훨씬 단순한 형태로 인코딩된다 — 실제로 toric variety가 아닌 일반 variety에 대해서도 Cox ring을 정의할 수 있으나, polynomial ring이 되는 것은 toric의 경우뿐이다.

이제 $$S$$ 위의 grading을 도입한다. [§토러스 인자와 선다발, ⁋정의 1](/ko/math/toric_geometry/toric_divisors#def1)에서 살펴본 torus-invariant prime divisor $$D_\rho$$에 대해, [§토러스 인자와 선다발, ⁋명제 4](/ko/math/toric_geometry/toric_divisors#prop4)에서 우리는 Weil divisor class group $$\Cl(X_\Sigma)$$가 exact sequence

$$0 \longrightarrow M \longrightarrow \bigoplus_{\rho \in \Sigma(1)} \mathbb{Z} \cdot D_\rho \longrightarrow \Cl(X_\Sigma) \longrightarrow 0$$

로부터 얻어짐을 확인하였다 (첫 번째 화살표는 [§토러스 인자와 선다발, ⁋명제 3](/ko/math/toric_geometry/toric_divisors#prop3)에 의해 $$m \mapsto \sum_\rho \langle m, u_\rho \rangle D_\rho$$). 이 exact sequence에 $$\Hom_\mathbb{Z}(-, \mathbb{C}^\ast)$$를 적용하면

$$1 \longrightarrow G \longrightarrow (\mathbb{C}^\ast)^{\Sigma(1)} \longrightarrow T_N \longrightarrow 1$$

을 얻으며, 여기서 $$G = \Hom_\mathbb{Z}(\Cl(X_\Sigma), \mathbb{C}^\ast)$$, $$T_N = N \otimes_\mathbb{Z} \mathbb{C}^\ast$$는 $$X_\Sigma$$의 dense torus이다. 따라서 $$G$$는 $$(\mathbb{C}^\ast)^{\Sigma(1)}$$의 subgroup으로서, 자연스럽게 affine space $$\mathbb{C}^{\Sigma(1)} = \Spec S$$ 위에 diagonal action을 한다.

Cox ring $$S$$ 위의 $$\Cl(X_\Sigma)$$-grading은 다음과 같이 정의된다: $$\beta \in \Cl(X_\Sigma)$$에 대해 그 inverse image $$\sum_\rho a_\rho D_\rho$$를 잡고, monomial $$\prod_\rho \x_\rho^{a_\rho}$$의 degree를 $$\beta$$로 정한다. 이 grading은 $$G$$의 character group과 일치하며, 따라서 $$G$$의 작용에 의한 invariant theory와 자연스럽게 연결된다.

다음으로, 사영공간 구성에서 원점 $$\{0\}$$을 제거하던 것에 해당하는 exceptional subset을 정의한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 각 cone $$\sigma \in \Sigma$$에 대해 monomial $$\hat{\x}_\sigma$$를

$$\hat{\x}_\sigma = \prod_{\rho \not\subset \sigma} \x_\rho$$

로 정의한다. *Irrelevant ideal* $$B(\Sigma)$$는 이들 monomial로 생성되는 ideal

$$B(\Sigma) = \langle \hat{\x}_\sigma \mid \sigma \in \Sigma \rangle \subseteq S$$

이며, *exceptional set* $$Z(\Sigma) = V(B(\Sigma)) \subseteq \mathbb{C}^{\Sigma(1)}$$은 그 zero locus이다.

</div>

명칭의 유래는 $$\mathbb{P}^n$$의 경우 $$B(\Sigma) = \langle \x_0, \ldots, \x_n \rangle$$이 되어 usual homogeneous coordinate ring의 irrelevant ideal과 일치하는 데 있다. 실제로 $$\mathbb{P}^n$$의 fan은 $$n+1$$개의 1차원 cone을 가지며, 각 maximal cone은 그 중 $$n$$개를 포함하므로 $$\hat{\x}_\sigma$$는 변수 하나만 빼고 곱한 것이 된다. 모든 maximal cone에 대해 모으면 $$\langle \x_0, \ldots, \x_n \rangle$$이 생성된다.

## Toric variety를 GIT quotient로 재구성하기

이제 toric variety $$X_\Sigma$$를 affine space $$\mathbb{C}^{\Sigma(1)}$$에서 exceptional set $$Z(\Sigma)$$를 제거한 뒤 군 $$G$$로 몫을 취함으로써 재구성할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Toric variety $$X_\Sigma$$는 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$에 대한 $$G$$의 작용의 categorical quotient로

$$X_\Sigma \cong (\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)) /\!/ G$$

로 나타난다. 더욱이 $$\Sigma$$가 *simplicial* fan일 때 — 즉 각 cone이 그 차원만큼의 $$\mathbb{R}$$-linearly independent한 ray generator로 생성될 때 — 이 quotient는 geometric quotient가 된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cox의 원래 논문의 증명을 따라간다. 먼저 $$G$$가 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$ 위에 잘 정의된 작용을 가짐을 본다: $$Z(\Sigma)$$는 coordinate subspace들의 union이며 $$G$$의 작용은 $$(\mathbb{C}^\ast)^{\Sigma(1)}$$의 작용으로부터 유도된 diagonal action이므로 coordinate subspace들을 보존한다.

각 cone $$\sigma \in \Sigma$$에 대해 $$U_\sigma = \Spec \mathbb{C}[\sigma^\vee \cap M]$$는 toric variety의 affine chart이다. 이제 $$\hat{\x}_\sigma$$에 의해 localize한 ring $$S_{\hat{\x}_\sigma}$$의 $$0$$차 부분 $$(S_{\hat{\x}_\sigma})^{(0)}$$은 $$G$$-invariant element들로 구성되며, Cox는 이것이 $$\mathbb{C}[\sigma^\vee \cap M]$$와 isomorphic함을 보였다:

$$(S_{\hat{\x}_\sigma})^{(0)} \cong \mathbb{C}[\sigma^\vee \cap M].$$

이로부터 $$U_\sigma$$가 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$의 $$G$$-invariant open subset에 대한 quotient로 얻어진다. 이러한 affine chart들이 fan의 조합론에 따라 적절히 glueing되어 전체 $$X_\Sigma$$가 categorical quotient로서 얻어진다.

Simplicial인 경우, 각 cone이 simplicial이므로 local chart $$U_\sigma$$에 대한 작용의 stabilizer가 유한군이 되어 ([명제 3](#prop3)의 orbit closure 기준이 단순화됨) geometric quotient가 된다. 역으로 geometric quotient이려면 stabilizer가 유한해야 하고, 이는 각 cone이 simplicial임을 의미한다.

</details>

명제 9의 geometric quotient 버전은 매우 중요하다. Simplicial toric variety의 경우 점들이 실제로 $$G$$의 궤도로 대응되므로 homogeneous coordinate의 직관적 이해가 가능하다. Non-simplicial 경우에는 categorical quotient에 그치므로 점들이 $$G$$-orbit과 일대일 대응하지는 않지만, 여전히 좋은 geometric interpretation을 제공한다.

## 예시

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (사영공간)**</ins> $$\mathbb{P}^n$$의 fan $$\Sigma$$는 원점을 중심으로 하는 $$n+1$$개의 1차원 cone $$\rho_0, \ldots, \rho_n$$으로 구성되며, primitive generator는 $$u_0, \ldots, u_{n-1}$$이 표준기저이고 $$u_n = -u_0 - \cdots - u_{n-1}$$이다. 각 maximal cone $$\sigma_i = \mathrm{cone}(u_0, \ldots, \hat{u}_i, \ldots, u_n)$$에 대해

$$\hat{\x}_{\sigma_i} = \x_i$$

이므로 irrelevant ideal은 $$B(\Sigma) = \langle \x_0, \ldots, \x_n \rangle$$이고 exceptional set은 $$Z(\Sigma) = \{0\}$$이다. 한편 Weil divisor의 exact sequence는

$$0 \longrightarrow \mathbb{Z}^n \longrightarrow \mathbb{Z}^{n+1} \longrightarrow \Cl(\mathbb{P}^n) = \mathbb{Z} \longrightarrow 0$$

이므로 $$G = \Hom_\mathbb{Z}(\mathbb{Z}, \mathbb{C}^\ast) = \mathbb{C}^\ast$$이고, 그 작용은 diagonal scaling

$$t \cdot (\x_0, \ldots, \x_n) = (t\x_0, \ldots, t\x_n)$$

이다. 그러므로 [명제 9](#prop9)는 익숙한

$$\mathbb{P}^n = (\mathbb{C}^{n+1} \setminus \{0\}) / \mathbb{C}^\ast$$

를 재현한다. 이는 [예시 6](#ex6)에서 본 GIT 시점과 정확히 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (사영선의 곱)**</ins> $$X = \mathbb{P}^1 \times \mathbb{P}^1$$의 fan은 1차원 cone 4개 $$\rho_1, \rho_2, \rho_3, \rho_4$$를 가지며 primitive generator는 보통 $$u_1 = (1, 0)$$, $$u_2 = (0, 1)$$, $$u_3 = (-1, 0)$$, $$u_4 = (0, -1)$$이다. Maximal cone 4개는 각각 인접한 두 cone으로 생성되며, 예컨대 $$\sigma_{12} = \mathrm{cone}(u_1, u_2)$$에 대해 $$\hat{\x}_{\sigma_{12}} = \x_3 \x_4$$이다. 모든 maximal cone에 대해 계산하면

$$B(\Sigma) = \langle \x_1 \x_3,\, \x_1 \x_4,\, \x_2 \x_3,\, \x_2 \x_4 \rangle = \langle \x_1, \x_2 \rangle \cap \langle \x_3, \x_4 \rangle$$

이고 exceptional set은

$$Z(\Sigma) = \{\x_1 = \x_2 = 0\} \cup \{\x_3 = \x_4 = 0\}$$

이다. Divisor class group은 $$\Cl(\mathbb{P}^1 \times \mathbb{P}^1) = \mathbb{Z} \oplus \mathbb{Z}$$이므로 $$G = (\mathbb{C}^\ast)^2$$이고, 그 작용은

$$(t_1, t_2) \cdot (\x_1, \x_2, \x_3, \x_4) = (t_1 \x_1, t_1 \x_2, t_2 \x_3, t_2 \x_4)$$

으로 각 $$\mathbb{P}^1$$ 인자에 독립적으로 scaling한다. 이로부터

$$\mathbb{P}^1 \times \mathbb{P}^1 = (\mathbb{C}^4 \setminus Z(\Sigma)) / (\mathbb{C}^\ast)^2$$

를 얻는다.

</div>

## Cox ring과 line bundle의 대응

사영공간에서 homogeneous coordinate ring의 graded component가 twisted structure sheaf의 global section과 대응했듯, Cox ring에서도 같은 대응이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Toric variety $$X_\Sigma$$가 simplicial이라고 하자. $$\beta \in \Cl(X_\Sigma)$$에 대해 $$S$$의 $$\beta$$차 성분 $$S_\beta$$는 다음과 같은 isomorphism을 갖는다:

$$S_\beta \cong H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)).$$

여기서 $$D$$는 class $$\beta$$에 속하는 임의의 Weil divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cox ring $$S$$의 $$\beta$$차 성분은 monomial $$\prod_\rho \x_\rho^{a_\rho}$$들로 생성되며, 여기서 $$\sum_\rho a_\rho D_\rho$$가 class $$\beta$$를 갖는다. 한편 [§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)에 의해 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$는 $$\langle m, u_\rho \rangle \ge -a_\rho$$를 만족하는 lattice point $$m \in M$$에 대응하는 character $$\chi^m$$들로 이루어진다. 이 조건은 $$\beta$$차 monomial의 정의와 정확히 일치하며, 각 lattice point $$m$$에 대응하는 monomial $$\prod_\rho \x_\rho^{\langle m, u_\rho \rangle + a_\rho}$$의 degree가 $$\sum_\rho (\langle m, u_\rho \rangle + a_\rho) D_\rho = \sum_\rho a_\rho D_\rho + \divisor(\chi^m) = \beta$$가 되므로 ($$\divisor(\chi^m)$$은 principal divisor이므로 class group에서 사라짐) 자연스러운 isomorphism이 얻어진다.

</details>

명제 12는 Cox ring이 toric variety의 모든 line bundle의 global section을 동시에 인코딩한다는 것을 의미한다. 이는 사영공간에서 $$\mathbb{C}[\x_0, \ldots, \x_n]$$이 모든 $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 global section을 담고 있는 것과 정확히 일치한다. 이 관점에서 Cox ring은 toric variety의 divisor class group으로 graded된 "universal" coordinate ring이다.

더 나아가 coherent sheaf에 대한 대응도 존재한다. Simplicial toric variety $$X_\Sigma$$ 위의 coherent sheaf $$\mathcal{F}$$에 대해 graded $$S$$-module $$\Gamma_\ast(\mathcal{F})$$를 적절히 정의하면, quasi-coherent sheaf의 category와 graded $$S$$-module의 category 사이에 equivalence가 성립한다. 이는 사영공간에서의 Serre correspondence를 일반화하는 결과이다.

## Secondary fan과 birational geometry

Cox 구성은 toric variety의 birational geometry를 이해하는 데도 강력한 도구이다. [§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)에서 보았듯이 lattice polytope으로부터 projective toric variety가 구성되며, Cox 구성의 관점에서 이러한 polytope의 변화는 GIT quotient에서 linearization의 변화에 정확히 대응한다.

구체적으로, Cox ring $$S$$와 군 $$G$$를 고정하면 서로 다른 linearization은 서로 다른 ample line bundle의 선택, 즉 character space의 chamber 선택에 대응한다. Effective cone $$\mathrm{Eff}(X_\Sigma)$$ — divisor class group에서 pseudo-effective divisor들이 이루는 cone — 은 유한 개의 rational polyhedral chamber로 분해되며, 각 chamber 내부에서는 GIT quotient가 같은 birational type의 toric variety를 준다. 이 chamber 분해를 *secondary fan*이라 부른다.

Secondary fan은 toric variety의 moduli space를 이해하는 데 중요하며, 특히 toric Mori theory와 밀접하게 연관된다. Wall crossing은 birational contraction이나 flip에 대응하여 toric variety의 minimal model program을 구체적으로 기술할 수 있게 한다. 자세한 논의는 본 글의 범위를 벗어나므로 [CLS] Chapter 14 및 [Mum] §2를 참고한다.

---

**참고문헌**

**[CLS]** D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
**[Cox95]** D. Cox, "The homogeneous coordinate ring of a toric variety", *J. Algebraic Geom.* **4** (1995), no. 1, 17--50.  
**[Mum]** D. Mumford, J. Fogarty, F. Kirwan, *Geometric Invariant Theory*, 3rd ed., Ergebnisse der Mathematik, Springer, 1994.  
**[New]** P. E. Newstead, *Introduction to Moduli Problems and Orbit Spaces*, Tata Institute Lecture Notes, 1978.  
**[Ful]** W. Fulton, *Introduction to Toric Varieties*, Princeton University Press, 1993.
