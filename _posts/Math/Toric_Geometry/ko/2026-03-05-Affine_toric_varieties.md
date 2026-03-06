---
title: "Affine toric varieties"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/affine_toric_varieties

header:
    overlay_image: /assets/images/Math/Toric_Geometry/affine_toric_varieties.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-05
last_modified_at: 2026-03-05
weight: 1
---

## Toric geometry

Toric geometry는 말 그대로 toric variety라 불리는 특별한 대수다양체를 연구하는 분야이다. 일반적인 대수다양체에 비해 toric variety가 가지는 장점은 이것이 본질적으로 조합론적인 정보로 만들어지므로 더 손에 잡히는 계산을 수행하기 용이하다는 것이다. 우리는 이 글에서 먼저 가장 간단한 toric variety, 즉 affine toric variety를 살펴본다. 

## 격자와 뿔

직관적으로, toric variety는 $$\mathbb{A}^k_\mathbb{C}$$들을 이어붙여 $$\mathbb{P}^k_\mathbb{C}$$를 얻어내는 과정을 일반화하여 얻어진다고 할 수 있다. 이제는 이들을 이어붙이는 방법들을 *lattice들* 안에 기록해두게 된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathbb{Z}^n$$과 isomorphic한 abelian group $$N$$을 *lattice<sub>격자</sub>*라 부른다. Lattice $$N$$의 *dual lattice<sub>쌍대 격자</sub>*는 다음의 식

$$M = \Hom(N, \mathbb{Z})$$

으로 주어진다. 그럼 이 때 Kronecker pairing $$M\times N \to \mathbb{Z}$$를 *dual pairing<sub>쌍대 페어링</sub>*이라 부른다. 

</div>

논의의 편의를 위해 다음 두 표기

$$N_{\mathbb{R}} = N \otimes_{\mathbb{Z}} \mathbb{R},\qquad M_{\mathbb{R}} = M \otimes_{\mathbb{Z}} \mathbb{R}$$

을 도입하자. 이제 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$N_{\mathbb{R}}$$의 부분집합 $$\sigma$$가 다음 조건을 만족할 때, 이를 *strongly convex rational polyhedral cone<sub>강하게 볼록한 유리 다각형뿔</sub>*이라 한다:

1. $$\sigma$$는 원점을 꼭짓점으로 하는 cone이다: $$\lambda v \in \sigma$$ for all $$v \in \sigma$$, $$\lambda \ge 0$$
2. $$\sigma$$는 유한 개의 벡터 $$v_1, \ldots, v_s \in N$$의 $$\mathbb{R}_{\ge 0}$$-linear combination으로 생성된다. 즉 $$\sigma = \mathbb{R}_{\ge 0} v_1 + \cdots + \mathbb{R}_{\ge 0} v_s$$이라 할 수 있다.
3. $$\sigma$$는 *strongly convex*이다. 즉 $$\sigma \cap (-\sigma) = \{0\}$$이 성립한다.

</div>

여기서 세 번째 조건은 $$\sigma$$가 원점을 지나는 직선을 포함하지 않는다는 것을 의미한다. 한편 각각의 cone $$\sigma$$에 대하여, 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Cone $$\sigma$$의 **face<sub>면</sub>** $$\tau$$는 어떤 $$u \in M_{\mathbb{R}}$$에 대해

$$\tau = \sigma \cap u^{\perp} = \{ v \in \sigma \mid \langle u, v \rangle = 0 \}$$

로 얻어진다. $$\tau$$가 $$\sigma$$의 face일 때, 이를 $$\tau \prec \sigma$$라고 쓴다.

</div>

우리가 정의할 toric variety는 우선, 각각의 cone을 affine chart처럼 가지고, 이들 cone이 face에서 어떻게 만나는지를 통해 gluing data가 결정되는 것이다. 이를 엄밀히 쓰기 위해 이번 글에서 우리는 affine toric variety에 대해 살펴본다.

## 아핀 토릭 다양체

Cone $$\sigma$$가 주어졌다 하고, 그 *dual cone<sub>쌍대뿔</sub>*

$$\sigma^\vee = \{ u \in M_{\mathbb{R}} \mid \langle u, v \rangle \ge 0 \text{ for all } v \in \sigma \}$$

을 생각하자.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Cone $$\sigma$$에 대하여, 다음의 semigroup

$$S_\sigma = \sigma^\vee \cap M=\{u\in M\mid \langle u,v\rangle \geq 0\text{ for all $v\in\sigma$}\}$$

을 정의하고, 이를 통해 semigroup algebra

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\,{\rchi}^u \mid u \in S_\sigma]$$

을 정의한다. ([\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)) 여기서 $$\rchi^u$$는 $$M$$의 원소 $$u$$에 대응되는 단항식이다.

</div>



<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 강한 정초 유리 다면체 콘 $$\sigma \subseteq N_{\mathbb{R}}$$에 대해, **아핀 토릭 다양체(affine toric variety)** $$U_\sigma$$를

$$U_\sigma = \operatorname{Spec}(\mathbb{C}[S_\sigma])$$

로 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> $$\sigma = \{0\}$$인 경우, $$\sigma^\vee = M_{\mathbb{R}}$$이므로 $$S_\sigma = M$$이다. 따라서

$$\mathbb{C}[S_\sigma] = \mathbb{C}[M] = \mathbb{C}[\chi^{\pm e_1^\ast}, \ldots, \chi^{\pm e_n^\ast}]$$

이며, 이것은 **대수적 토러스(algebraic torus)** $$T_N = N \otimes_{\mathbb{Z}} \mathbb{C}^\ast \cong (\mathbb{C}^\ast)^n$$의 좌표환에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$N = \mathbb{Z}^2$$에서 $$\sigma$$가 $$e_1$$과 $$e_2$$로 생성되는 경우를 생각하자. 그러면

$$\sigma^\vee = \mathbb{R}_{\ge 0} e_1^\ast + \mathbb{R}_{\ge 0} e_2^\ast$$

이므로 $$S_\sigma = \mathbb{Z}_{\ge 0}^2$$이고,

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\chi^{e_1^\ast}, \chi^{e_2^\ast}] = \mathbb{C}[X, Y]$$

이다. 따라서 $$U_\sigma = \mathbb{C}^2$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (이차 원뿔)**</ins> $$N = \mathbb{Z}^2$$에서 $$\sigma$$가 $$e_2$$와 $$2e_1 - e_2$$로 생성되는 경우를 생각하자.

쌍대 콘 $$\sigma^\vee$$를 구하기 위해, $$u = ae_1^\ast + be_2^\ast \in M_{\mathbb{R}}$$이 $$\sigma^\vee$$에 속할 조건을 생각하자. $$\langle u, e_2 \rangle = b \ge 0$$이고 $$\langle u, 2e_1 - e_2 \rangle = 2a - b \ge 0$$이어야 한다. 따라서 $$b \ge 0$$이고 $$2a \ge b$$이다.

$$\sigma^\vee$$의 극소 생성원은 $$e_1^\ast$$와 $$2e_1^\ast + e_2^\ast$$이다. Gordan의 보조정리에 의해 $$S_\sigma = \sigma^\vee \cap M$$의 생성원은 $$e_1^\ast$$, $$e_1^\ast + e_2^\ast$$, $$e_1^\ast + 2e_2^\ast$$이다.

따라서

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\chi^{e_1^\ast}, \chi^{e_1^\ast + e_2^\ast}, \chi^{e_1^\ast + 2e_2^\ast}] = \mathbb{C}[X, XY, XY^2]$$

이다. 이것을 $$U = X$$, $$V = XY$$, $$W = XY^2$$로 두면 $$V^2 = UW$$이므로,

$$\mathbb{C}[S_\sigma] \cong \mathbb{C}[U, V, W] / (V^2 - UW)$$

이다. 따라서 $$U_\sigma$$는 **이차 원뿔(quadric cone)**이다.

</div>

## 토러스 작용

아핀 토릭 다양체의 중요한 성질 중 하나는 대수적 토러스의 자연스러운 작용이다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 아핀 토릭 다양체 $$U_\sigma$$ 위에 대수적 토러스 $$T_N = N \otimes_{\mathbb{Z}} \mathbb{C}^\ast$$가 다음과 같이 작용한다:

$$t \cdot \chi^u = \chi^u(t) \cdot \chi^u$$

여기서 $$t \in T_N$$이고 $$\chi^u(t)$$는 문자 $$\chi^u$$의 $$t$$에서의 값이다.

</div>

이 작용은 $$U_\sigma$$ 안에 **열린 조밀한(dense open)** 토러스 궤도(orbit)를 가진다. 이 궤도는 정확히 토러스 $$T_N$$ 자체이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\tau$$가 $$\sigma$$의 면일 때, $$U_\tau$$는 $$U_\sigma$$의 **주 열린 부분집합(principal open subset)**이다. 구체적으로, $$u \in S_\sigma$$를 $$\tau = \sigma \cap u^{\perp}$$를 만족하는 것으로 선택하면

$$U_\tau = \{ x \in U_\sigma \mid \chi^u(x) \neq 0 \}$$

이다.

</div>

이 명제는 작은 콘이 더 작은 열린 집합에 대응된다는 것을 보여준다. 이것이 바로 $$N$$에서의 기하학이 $$M$$에서의 기하학보다 선호되는 이유이다.

## 기본 성질

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 아핀 토릭 다양체 $$U_\sigma$$에 대해 다음이 성립한다:

1. $$U_\sigma$$는 **정규(normal)** 다양체이다. (증명은 Gordan의 보조정리를 사용한다.)
2. $$U_\sigma$$는 **기약(irreducible)**이다.
3. $$U_\sigma$$의 차원은 $$n$$이다 (여기서 $$N \cong \mathbb{Z}^n$$).

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 모든 아핀 토릭 다양체 $$U_\sigma$$는 토러스 $$T_N$$을 열린 조밀한 부분집합으로 포함한다.

</div>

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
