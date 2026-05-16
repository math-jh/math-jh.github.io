---
title: "Cox construction과 GIT quotient"
excerpt: "Toric variety를 homogeneous coordinate ring과 GIT quotient로 구성하는 Cox의 방법을 소개한다."
categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/cox_construction
sidebar: { nav: "toric_geometry-ko" }
header: { overlay_image: /assets/images/Math/Toric_Geometry/cox_construction.png, overlay_filter: 0.5 }
date: 2026-03-09
last_modified_at: 2026-03-09
weight: 6
published: false
---

Projective space $$\mathbb{P}^n$$은 homogeneous coordinate를 통해

$$\mathbb{P}^n = (\mathbb{C}^{n+1} \setminus \{0\}) / \mathbb{C}^\ast$$

로 나타낼 수 있다. 이 construction은 사영공간 위의 대수적 구조를 다루는 데 매우 유용하며, 예를 들어 closed subvariety는 homogeneous ideal에 의해 정의되고 coherent sheaf는 graded module에 대응한다. Cox는 이러한 construction을 임의의 toric variety로 일반화하였다. 본 글에서는 fan $$\Sigma$$로부터 toric variety $$X_\Sigma$$를 homogeneous coordinate ring과 GIT quotient로 재구성하는 Cox의 방법을 설명한다. 이 construction은 toric variety 위의 선다발이나 coherent sheaf를 다루는 데 필수적인 도구이며, 뒤에서 소개할 secondary fan을 통한 birational geometry의 이해에도 기여한다.

우리는 이 글에서 $$N \cong \mathbb{Z}^n$$을 rank $$n$$인 free abelian group, $$M = \operatorname{Hom}_\mathbb{Z}(N, \mathbb{Z})$$를 그 dual, $$\Sigma$$를 $$N_\mathbb{R} = N \otimes_\mathbb{Z} \mathbb{R}$$ 위의 rational polyhedral fan이라 하고, $$\Sigma$$가 $$N_\mathbb{R}$$를 span한다고 가정한다. 또한 $$\Sigma(1)$$은 $$\Sigma$$의 1-dimensional cone들의 집합을 의미하며, 각 $$\rho \in \Sigma(1)$$에 대해 $$u_\rho$$는 $$\rho$$의 primitive generator이다.

## Homogeneous coordinate ring과 irrelevant ideal

Projective space의 homogeneous coordinate ring은 $$\mathbb{C}[\x_0, \ldots, \x_n]$$으로, 각 변수가 $$\mathbb{P}^n$$의 coordinate hyperplane에 대응한다. Cox는 이를 toric variety로 확장하기 위해, fan의 1-dimensional cone 각각에 변수를 대응시킨다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Toric variety $$X_\Sigma$$의 **homogeneous coordinate ring**<sub>homogeneous coordinate ring</sub> 혹은 **Cox ring**<sub>Cox ring</sub>은 다음과 같이 정의된다.

$$S = \mathbb{C}[\x_\rho \mid \rho \in \Sigma(1)]$$

</div>

Cox ring $$S$$는 polynomial ring이므로 특히 unique factorization domain이다. 이 점에서 Cox ring은 toric variety의 대수적 특성을 반영하는 중요한 불변량이다. 실제로 toric variety가 아닌 일반 variety에 대해서도 Cox ring을 정의할 수 있으나, toric variety의 경우에만 Cox ring이 polynomial ring이 된다.

이제 $$S$$ 위의 grading을 도입해야 한다. [§Toric divisors와 line bundles, ⁋정의 1](/ko/math/toric_geometry/toric_divisors#def1)에서 살펴 보았듯이, 각 $$\rho \in \Sigma(1)$$에 대응하는 torus-invariant divisor $$D_\rho$$를 생각할 수 있다. 이들의 정리에 의해 Weil divisor class group $$\operatorname{Cl}(X_\Sigma)$$는 다음 exact sequence로부터 얻어진다.

$$0 \longrightarrow M \longrightarrow \bigoplus_{\rho \in \Sigma(1)} \mathbb{Z} \cdot D_\rho \longrightarrow \operatorname{Cl}(X_\Sigma) \longrightarrow 0$$

여기서 첫 번째 화살표는 $$m \mapsto \sum_{\rho} \langle m, u_\rho \rangle D_\rho$$로 주어진다. 이 exact sequence에 $$\operatorname{Hom}_\mathbb{Z}(-, \mathbb{C}^\ast)$$를 적용하면 다음 exact sequence를 얻는다.

$$1 \longrightarrow G \longrightarrow (\mathbb{C}^\ast)^{\Sigma(1)} \longrightarrow T_N \longrightarrow 1$$

여기서 $$G = \operatorname{Hom}_\mathbb{Z}(\operatorname{Cl}(X_\Sigma), \mathbb{C}^\ast)$$이고 $$T_N = N \otimes_\mathbb{Z} \mathbb{C}^\ast$$는 $$X_\Sigma$$ 위의 dense torus이다. 이로부터 $$G$$가 $$(\mathbb{C}^\ast)^{\Sigma(1)}$$의 subgroup으로 작용하며, 이는 자연스럽게 affine space $$\mathbb{C}^{\Sigma(1)} = \operatorname{Spec}(S)$$ 위에 diagonal action을 유도한다.

Cox ring $$S$$ 위의 $$\operatorname{Cl}(X_\Sigma)$$-grading은 다음과 같이 정의된다. $$\beta \in \operatorname{Cl}(X_\Sigma)$$에 대해, $$\beta$$의 inverse image in $$\bigoplus_{\rho} \mathbb{Z} \cdot D_\rho$$를 $$\sum_\rho a_\rho D_\rho$$라 하면, monomial $$\prod_\rho \x_\rho^{a_\rho}$$의 degree를 $$\beta$$로 정한다. 이 grading은 $$G$$의 character group과 일치하며, 따라서 $$G$$의 action에 의한 invariant theory와 자연스럽게 연결된다.

다음으로, projective space의 construction에서 origin $$\{0\}$$을 제거하는 것에 해당하는 exceptional subset을 정의해야 한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 각 cone $$\sigma \in \Sigma$$에 대해 monomial $$\hat{\x}_\sigma$$를 다음과 같이 정의한다.

$$\hat{\x}_\sigma = \prod_{\rho \not\subset \sigma} \x_\rho$$

**Irrelevant ideal**<sub>irrelevant ideal</sub> $$B(\Sigma)$$는 이들 monomial로 생성되는 ideal이다.

$$B(\Sigma) = \langle \hat{\x}_\sigma \mid \sigma \in \Sigma \rangle \subseteq S$$

또한 exceptional set $$Z(\Sigma)$$는 $$B(\Sigma)$$의 zero locus로 정의된다.

$$Z(\Sigma) = V(B(\Sigma)) \subseteq \mathbb{C}^{\Sigma(1)}$$

</div>

Irrelevant ideal의 이름은 projective space의 경우 $$B(\Sigma) = \langle \x_0, \ldots, \x_n \rangle$$이 되어, usual homogeneous coordinate ring에서의 irrelevant ideal과 일치하기 때문에 붙여졌다. 실제로 $$\mathbb{P}^n$$의 fan은 $$n+1$$개의 1-dimensional cone을 가지며, 각 maximal cone은 $$n$$개의 cone을 포함하므로 $$\hat{\x}_\sigma$$는 하나의 변수만을 제외한 곱이 된다. 모든 maximal cone에 대해 이를 취하면 $$\langle \x_0, \ldots, \x_n \rangle$$이 생성된다.

## GIT quotient construction

본 절에서 사용하는 *categorical quotient<sub>범주적 몫</sub>*, *geometric quotient<sub>기하학적 몫</sub>*, *linearization<sub>선형화</sub>*, *(semi)stable<sub>(준)안정</sub> 점*과 GIT quotient $$X\sslash_L G$$의 정의는 [§Geometric invariant theory 입문](/ko/math/toric_geometry/geometric_invariant_theory)에서 다룬다. 이하에서는 그 결과를 자유롭게 사용한다.

이제 우리는 toric variety $$X_\Sigma$$를 affine space $$\mathbb{C}^{\Sigma(1)}$$에서 exceptional set $$Z(\Sigma)$$를 제거한 뒤, 군 $$G$$로 몫을 취함으로써 재구성할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Toric variety $$X_\Sigma$$는 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$에 대한 $$G$$의 작용의 categorical quotient로서 다음과 같이 나타난다.

$$X_\Sigma \cong (\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)) \sslash G$$

또한 $$X_\Sigma$$가 simplicial, 즉 $$\Sigma$$가 simplicial fan일 때에만 이 quotient는 geometric quotient가 된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cox의 원래 논문에서 제시된 증명을 따라간다. 먼저 $$G$$가 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$ 위에 잘 정의된 작용을 가짐을 보여야 한다. $$Z(\Sigma)$$는 coordinate subspace들의 union으로 구성되며, $$G$$의 작용은 $$(\mathbb{C}^\ast)^{\Sigma(1)}$$의 작용으로부터 유도된 diagonal action이므로 coordinate subspace들을 보존한다. 따라서 $$G$$는 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$ 위에 작용한다.

각 cone $$\sigma \in \Sigma$$에 대해, $$U_\sigma = \operatorname{Spec}(\mathbb{C}[\sigma^\vee \cap M])$$는 toric variety의 affine chart이다. 이제 $$\x^{\hat{\sigma}}$$에 의해 localizing한 ring $$S_{\x^{\hat{\sigma}}}$$를 생각하자. 이 ring의 $$0$$차 부분 $$S_{\x^{\hat{\sigma}}}^{(0)}$$은 $$G$$-invariant element들로 구성되며, Cox는 이것이 $$\mathbb{C}[\sigma^\vee \cap M]$$와 isomorphic함을 보였다. 즉,

$$(S_{\x^{\hat{\sigma}}})^{(0)} \cong \mathbb{C}[\sigma^\vee \cap M]$$

이로부터 $$U_\sigma$$는 $$\mathbb{C}^{\Sigma(1)} \setminus Z(\Sigma)$$의 $$G$$-invariant open subset에 대한 quotient로 얻어진다. 이러한 affine chart들이 fan의 combinatorial structure에 따라 적절히 glueing되므로, 전체 $$X_\Sigma$$가 categorical quotient로서 얻어진다.

Simplicial의 경우, 각 cone이 simplicial이므로 local chart $$U_\sigma$$에 대한 작용의 stabilizer가 finite group이 되어 geometric quotient가 된다. 역으로 geometric quotient가 된다면 stabilizer가 finite해야 하고, 이는 각 cone이 simplicial임을 의미한다.

</details>

명제 3의 geometric quotient 버전은 매우 중요하다. Simplicial toric variety의 경우, 점들은 실제로 $$G$$의 궤도로 대응되므로 homogeneous coordinate의 직관적 이해가 가능하다. Non-simplicial의 경우에는 categorical quotient이므로 점들이 $$G$$-orbit에 일대일 대응하지는 않지만, 여전히 좋은 geometric interpretation을 제공한다.

## 예시

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Projective space**

$$\mathbb{P}^n$$의 fan $$\Sigma$$는 $$\mathbb{R}^n$$에서 원점을 중심으로 하는 $$n+1$$개의 1-dimensional cone $$\rho_0, \ldots, \rho_n$$으로 구성되며, 각 primitive generator는 $$u_0, \ldots, u_n$$이다. 여기서 $$u_0, \ldots, u_{n-1}$$은 표준기저이고 $$u_n = -u_0 - \cdots - u_{n-1}$$이다. 각 maximal cone은 $$n$$개의 1-dimensional cone을 포함하므로, 예를 들어 $$\sigma_i = \operatorname{cone}(u_0, \ldots, \hat{u}_i, \ldots, u_n)$$에 대해

$$\hat{\x}_{\sigma_i} = \x_i$$

이다. 따라서 irrelevant ideal은

$$B(\Sigma) = \langle \x_0, \x_1, \ldots, \x_n \rangle$$

이 되고, exceptional set은

$$Z(\Sigma) = \{0\}$$

이다. 한편, Weil divisor들의 exact sequence는

$$0 \longrightarrow \mathbb{Z}^n \longrightarrow \mathbb{Z}^{n+1} \longrightarrow \operatorname{Cl}(\mathbb{P}^n) = \mathbb{Z} \longrightarrow 0$$

이므로 $$G = \operatorname{Hom}_\mathbb{Z}(\mathbb{Z}, \mathbb{C}^\ast) = \mathbb{C}^\ast$$이다. $$G$$의 작용은 diagonal scaling이 되어,

$$t \cdot (\x_0, \x_1, \ldots, \x_n) = (t\x_0, t\x_1, \ldots, t\x_n)$$

이 된다. 이로부터 명제 3은 well-known한 quotient construction을 재현한다.

$$\mathbb{P}^n = (\mathbb{C}^{n+1} \setminus \{0\}) / \mathbb{C}^\ast$$

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Product of projective lines**

$$X = \mathbb{P}^1 \times \mathbb{P}^1$$의 경우를 생각하자. Fan은 $$\mathbb{R}^2$$에서 원점을 중심으로 하며, 1-dimensional cone은 4개 $$\rho_1, \rho_2, \rho_3, \rho_4$$를 가진다. Primitive generator는 보통 $$u_1 = (1,0), u_2 = (0,1), u_3 = (-1,0), u_4 = (0,-1)$$로 선택된다. Maximal cone은 4개이며, 각각 인접한 두 1-dimensional cone으로 생성된다. 예를 들어 $$\sigma_{12} = \operatorname{cone}(u_1, u_2)$$에 대해

$$\hat{\x}_{\sigma_{12}} = \x_3 \x_4$$

이다. 모든 maximal cone에 대해 같은 계산을 하면,

$$B(\Sigma) = \langle \x_1 \x_3, \x_1 \x_4, \x_2 \x_3, \x_2 \x_4 \rangle = \langle \x_1, \x_2 \rangle \cap \langle \x_3, \x_4 \rangle$$

이다. 따라서 exceptional set은

$$Z(\Sigma) = \{\x_1 = \x_2 = 0\} \cup \{\x_3 = \x_4 = 0\}$$

이 된다. 한편 divisor class group은

$$\operatorname{Cl}(\mathbb{P}^1 \times \mathbb{P}^1) = \mathbb{Z} \oplus \mathbb{Z}$$

이므로 $$G = (\mathbb{C}^\ast)^2$$이다. $$G$$의 작용은

$$(t_1, t_2) \cdot (\x_1, \x_2, \x_3, \x_4) = (t_1 \x_1, t_1 \x_2, t_2 \x_3, t_2 \x_4)$$

이 되어, 각 $$\mathbb{P}^1$$ 요소에 대한 독립적인 scaling에 해당한다. 이로부터

$$\mathbb{P}^1 \times \mathbb{P}^1 = (\mathbb{C}^4 \setminus Z(\Sigma)) / (\mathbb{C}^\ast)^2$$

를 얻는다.

</div>

## Cox ring과 line bundle의 대응

Projective space에서 homogeneous coordinate ring의 graded component는 twisted structure sheaf의 global section과 대응한다. Cox ring에서도 유사한 대응이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Toric variety $$X_\Sigma$$가 simplicial이라고 하자. $$\beta \in \operatorname{Cl}(X_\Sigma)$$에 대해, $$S$$의 $$\beta$$차 성분 $$S_\beta$$는 다음과 같은 isomorphism을 갖는다.

$$S_\beta \cong H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$

여기서 $$D$$는 class $$\beta$$에 속하는 임의의 Weil divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cox ring $$S = \mathbb{C}[\x_\rho \mid \rho \in \Sigma(1)]$$의 $$\beta$$차 성분은 monomial $$\prod_\rho \x_\rho^{a_\rho}$$들로 생성되며, 여기서 $$\sum_\rho a_\rho D_\rho$$가 class $$\beta$$를 가진다. 한편, [§Toric divisors와 line bundles, ⁋명제 8](/ko/math/toric_geometry/toric_divisors#prop8)에 의해, $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$의 원소는 lattice point $$m \in M$$에 대응하는 character $$\chi^m$$들로 이루어지며, 이들은 $$\langle m, u_\rho \rangle \geq -a_\rho$$를 만족한다. 이 조건은 $$\beta$$차 monomial의 정의와 정확히 일치하므로, 각 lattice point $$m \in M$$에 대응하는 monomial $$\prod_\rho \x_\rho^{\langle m, u_\rho\rangle + a_\rho}$$의 degree는 $$\sum_\rho (\langle m, u_\rho\rangle + a_\rho)D_\rho = \sum_\rho a_\rho D_\rho + \operatorname{div}(\chi^m) = \beta$$가 되어 principal divisor에 의해 $$\beta$$가 됨을 알 수 있다. 따라서 자연스러운 isomorphism이 존재한다.

</details>

명제 6은 Cox ring이 toric variety의 모든 line bundle들의 global section을 동시에 encode함을 의미한다. 이는 projective space에서 $$\mathbb{C}[\x_0, \ldots, \x_n]$$이 모든 $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 global section을 담고 있는 것과 정확히 일치한다. 이러한 관점에서 Cox ring은 toric variety의 Picard group 혹은 divisor class group에 의해 graded된 "universal" coordinate ring으로 이해할 수 있다.

더 나아가, coherent sheaf에 대한 대응도 존재한다. Simplicial toric variety $$X_\Sigma$$ 위의 coherent sheaf $$\mathcal{F}$$에 대해, graded $$S$$-module $$\Gamma_\ast(\mathcal{F})$$를 적절히 정의하면, quasi-coherent sheaf의 category와 graded $$S$$-module의 category 사이에 equivalence가 성립한다. 이는 projective space에서의 Serre correspondence를 일반화하는 결과이다.

## Birational geometry와 secondary fan

Cox construction은 toric variety의 birational geometry를 이해하는 데에도 강력한 도구를 제공한다. [§Normal fan과 projective toric variety, ⁋명제 10](/ko/math/toric_geometry/normal_fan_projective_toric#prop10)에서 보았듯이, lattice polytope으로부터 projective toric variety를 구성할 수 있다. Cox construction의 관점에서, 이러한 polytope들의 변화는 GIT quotient에서 linearization의 변화에 대응한다.

구체적으로, Cox ring $$S$$와 군 $$G$$를 고정하면, different linearizations of the $$G$$-action correspond to different choices of ample line bundles, 즉 character space에서 GIT equivalence classes에 해당하는 chamber decomposition, 즉 **secondary fan**의 다른 chamber를 선택하는 것에 대응한다. Effective cone $$\operatorname{Eff}(X_\Sigma)$$는 divisor class group에서 pseudo-effective divisor들의 cone이며, 이 cone은 finitely many rational polyhedral chamber로 분해된다. 각 chamber의 interior에서는 GIT quotient가 동일한 birational type의 toric variety를 준다. 이러한 chamber decomposition을 *secondary fan*<sub>secondary fan</sub>이라 부른다.

Secondary fan은 toric variety의 moduli space를 이해하는 데 중요한 역할을 하며, 특히 toric Mori theory와 밀접하게 연관된다. Secondary fan의 wall crossing은 birational contraction이나 flip에 대응하며, 이는 toric variety의 minimal model program을 구체적으로 기술할 수 있게 한다. 다만 secondary fan에 대한 자세한 논의는 본 글의 범위를 벗어나므로, 여기서는 이러한 방향성만을 언급하고 넘어간다.

---

**참고문헌**

**[CLS]** D. Cox, J. Little, H. Schenck, *Toric varieties*, American Mathematical Society, 2011.

**[Cox95]** D. Cox, "The homogeneous coordinate ring of a toric variety", *J. Algebraic Geom.* **4** (1995), no. 1, 17--50.

**[Ful]** W. Fulton, *Introduction to toric varieties*, Princeton University Press, 1993.
