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

이를 풀어쓰면 다음과 같다. 우선 우리는 그 정의에 의하여 $$S_\sigma$$가 덧셈 $$+$$에 대한 semigroup이 되는 것을 안다. 이 semigroup에 대한 semigroup algebra를 생각하는 것은, 함수들 $$S_\sigma\rightarrow \mathbb{C}$$의 모임에 convolution product를 주는 것과 같고, 이 때 semigroup $$S_\sigma$$가 finitely genedrated이므로 이 semigroup algebra는 $$S_\sigma$$의 특정한 원소를 보내는 delta function들로 주어진다. $$u\in S_\sigma$$를 $$1$$로 보내는 함수를 $$\rchi^u$$로 적으면, $$\mathbb{C}[S_\sigma]$$는 $$u\in S_\sigma$$들에 대하여 $$\rchi^u$$들을 basis로 하여 생성되는 $$\mathbb{C}$$-algebra이며, 이 때 basis의 원소들의 곱은

$$\rchi^u\ast\rchi^{u'}=\rchi^{u+u'}$$

으로 주어지게 된다. 그럼 이 $$\mathbb{C}$$-algebra가 affine toric variety의 polynomial ring이 된다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Strongly convex rational polyhedral cone $$\sigma \subseteq N_{\mathbb{R}}$$에 대해, 이것이 정의하는 *affine toric variety<sub>아핀 토릭 다양체</sub>* $$U_\sigma$$를

$$U_\sigma = \operatorname{Spec}(\mathbb{C}[S_\sigma])$$

로 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$\sigma = \{0\}$$인 경우, $$\sigma^\vee = M_{\mathbb{R}}$$이므로 $$S_\sigma = M$$이다. 따라서

$$\mathbb{C}[S_\sigma] = \mathbb{C}[M] = \mathbb{C}[\rchi^{\pm e_1^\ast}, \ldots, \rchi^{\pm e_n^\ast}]$$

이며, 이것은 algebraic torus $$T_N = N \otimes_{\mathbb{Z}} \mathbb{C}^\ast \cong (\mathbb{C}^\ast)^n$$의 coordinate ring에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$N = \mathbb{Z}^2$$에서 $$\sigma$$가 $$e_1$$과 $$e_2$$로 생성되는 경우를 생각하자. 그러면

$$\sigma^\vee = \mathbb{R}_{\ge 0} e_1^\ast + \mathbb{R}_{\ge 0} e_2^\ast$$

이므로 $$S_\sigma = \mathbb{Z}_{\ge 0}^2$$이고,

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\chi^{e_1^\ast}, \chi^{e_2^\ast}] = \mathbb{C}[X, Y]$$

이다. 따라서 $$U_\sigma = \mathbb{C}^2$$이다.

</div>

## 토러스 작용

위에서 정의한 $$\Spec(\mathbb{C}[S_\sigma])$$가 affine *toric* variety라 불리는 이유는 이 위에 자연스러운 torus action이 존재하기 때문이다. 이를 위해 다음의 algebraic torus

$$T_N=N\otimes_\mathbb{Z}\mathbb{C}^\ast$$

을 생각하자. 

Torus $$T_N$$의 원소 $$t$$와 $$M$$의 원소 $$u$$에 대하여, $$\chi^u(t)$$를 다음과 같이 정의하자. 우선 $$t = n \otimes c \in N \otimes_{\mathbb{Z}} \mathbb{C}^\ast = T_N$$이고 $$u \in M = \Hom(N, \mathbb{Z})$$일 때,

$$\chi^u(t) = c^{u(n)} \in \mathbb{C}^\ast$$

로 정의한다. **이 정의는 basis의 선택에 의존하지 않으며**, $$\chi^u: T_N \to \mathbb{C}^\ast$$는 torus의 *character<sub>문자</sub>*가 된다.

계산의 편의를 위해 $$N$$의 basis $$e_1, \ldots, e_n$$을 선택하자. 그럼 $$N \cong \mathbb{Z}^n$$이므로 $$T_N \cong (\mathbb{C}^\ast)^n$$이고, $$M \cong \mathbb{Z}^n$$이다. 이 때 $$t = (t_1, \ldots, t_n) \in (\mathbb{C}^\ast)^n$$이고 $$u = (a_1, \ldots, a_n) \in \mathbb{Z}^n$$으로 쓸 수 있으며, 이 경우

$$\chi^u(t) = t_1^{a_1} \cdots t_n^{a_n}$$

으로 표현된다.

이제 $$\mathbb{C}[S_\sigma] = \bigoplus_{u \in S_\sigma} \mathbb{C} \cdot \chi^u$$가 $$M$$-graded algebra라는 점을 이용하여, 이 위에 torus action을 정의하자. $$T_N$$이 $$\mathbb{C}[S_\sigma]$$의 각 graded component에 작용하여

$$t \cdot \chi^u = \chi^u(t) \cdot \chi^u$$

를 만족하도록 정의한다. 이 action은 $$\mathbb{C}$$-algebra automorphism을 유도하므로, $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$ 위의 torus action에 해당한다. 구체적으로, 이 action에 의해 $$t \in T_N$$이 $$\mathbb{C}[S_\sigma]$$의 automorphism $$\phi_t: \mathbb{C}[S_\sigma] \to \mathbb{C}[S_\sigma]$$를 결정하고, 이것이 $$U_\sigma$$의 automorphism으로 내려온다. 요약하면:

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> $$\mathbb{C}[S_\sigma]$$의 $$M$$-grading으로부터 유도되는 torus action은 $$U_\sigma$$ 위에 다음과 같이 작용한다:

$$t \cdot \chi^u = \chi^u(t) \cdot \chi^u$$

여기서 $$t \in T_N$$이고 $$\chi^u(t)$$는 위에서 정의한 문자이다.

</div>

이 작용은 Lie theory에서의 torus action과 같은 방식으로 이해할 수 있다. [\[\] §원환면의 작용, §§Weight decomposition]에서 살펴본 것처럼, torus action은 coordinate ring 위에 weight decomposition을 유도한다. 사실 우리는 이미 $$\mathbb{C}[S_\sigma]$$를

$$\mathbb{C}[S_\sigma] = \bigoplus_{u \in S_\sigma} \mathbb{C} \cdot \chi^u$$

으로 분해하였으며, 명제 1의 작용 하에서 각각의 $$\chi^u$$는 정확히

$$t \cdot \chi^u = \chi^u(t) \chi^u$$

을 만족하므로, $$\chi^u$$는 weight $$u$$를 갖는 eigenvector이다. 즉, **$$M$$-grading이 정확히 torus action에 대한 weight decomposition**이다.

여기서 $$\chi^u$$라는 기호가 **두 가지 다른 의미**로 쓰이고 있음에 주의하자:

1. **$$\chi^u \in \mathbb{C}[S_\sigma]$$**: Coordinate ring의 basis 원소 (각 weight space $$V_u = \mathbb{C} \cdot \chi^u$$의 generator)
2. **$$\chi^u: T_N \to \mathbb{C}^\ast$$**: Character 함수, $$t \mapsto \chi^u(t)$$

이 두 가지가 같은 기호를 쓰는 이유는, $$\chi^u \in \mathbb{C}[S_\sigma]$$가 weight $$u$$를 갖는 eigenvector이며, 그 eigenvalue가 **정확히 character $$\chi^u(t)$$**이기 때문입니다.

정리하면 다음과 같습니다:

| 개념 | Toric variety에서의 실체 |
|------|------------------------|
| **Weight** | $$u \in S_\sigma \subseteq M$$ (lattice 원소) |
| **Character** | $$\chi^u: T_N \to \mathbb{C}^\ast$$, $$t \mapsto \chi^u(t)$$ |
| **Eigenvector** | $$\chi^u \in \mathbb{C}[S_\sigma]$$, $$t \cdot \chi^u = \chi^u(t) \cdot \chi^u$$ |
| **Weight space** | $$V_u = \mathbb{C} \cdot \chi^u$$ (1차원) |

**Toric variety의 특별한 성질**: weight $$u$$, character $$\chi^u$$, eigenvector $$\chi^u$$가 **모두 같은 $$u$$**에 의해 parametrize됩니다.

이 작용은 $$U_\sigma$$ 안에 **열린 조밀한(dense open)** 토러스 궤도(orbit)를 가진다. 이 궤도는 정확히 토러스 $$T_N$$ 자체이며, coordinate ring의 weight decomposition에 의해 모든 point는 weight space $$V_u = \mathbb{C} \cdot \chi^u$$ 위에 있습니다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\tau$$가 $$\sigma$$의 면일 때, $$U_\tau$$는 $$U_\sigma$$의 **주 열린 부분집합(principal open subset)**이다. 구체적으로, $$u \in S_\sigma$$를 $$\tau = \sigma \cap u^{\perp}$$를 만족하는 것으로 선택하면

$$U_\tau = \{ x \in U_\sigma \mid \chi^u(x) \neq 0 \}$$

이다.

</div>

이 명제는 작은 콘이 더 작은 열린 집합에 대응된다는 것을 보여준다. 이것이 바로 $$N$$에서의 기하학이 $$M$$에서의 기하학보다 선호되는 이유이다.

한편, 위의 open embedding $$U_\tau \hookrightarrow U_\sigma$$는 $$T_N$$-equivariant이다. 즉, $$T_N$$이 $$U_\tau$$와 $$U_\sigma$$ 위에 각각 작용할 때, 이 작용들은 inclusion과 compatible하다. 이것이 의미하는 것은, 여러 affine toric variety들을 face 관계를 통해 glue할 때, 이 glue가 torus action을 보존한다다는 것이다. 결과적으로 일반적인 toric variety는 자연스러운 torus action을 가지며, 이것이 toric variety의 핵심적인 성질이 된다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (구면의 회전)**</ins> Torus action을 직관적으로 이해하기 위해, 2차원 구면 $$S^2$$이 자전축 중심으로 회전하는 상황을 생각하자.

$$S^2$$을 $$\mathbb{C} \times \mathbb{R}$$의 부분집합

$$S^2 = \{(z, x_3) \in \mathbb{C} \times \mathbb{R} \mid |z|^2 + x_3^2 = 1\}$$

으로 생각하자. 1차원 torus $$S^1 = \{e^{i\theta} \mid \theta \in \mathbb{R}/2\pi\mathbb{Z}\}$$가 다음과 같이 작용한다:

$$e^{i\theta} \cdot (z, x_3) = (e^{i\theta}z, x_3)$$

이 작용 하에서:

- **궤도(Orbits)**: 같은 위도에 있는 모든 점들이 하나의 궤도를 이룬다. 예를 들어 적도 $$\{(z, 0) \mid |z| = 1\}$$은 하나의 원 모양 궤도이고, 북위 45° 선도 마찬가지로 하나의 궤도이다.
  
- **고정점(Fixed points)**: 북극 $$(0, 1)$$과 남극 $$(0, -1)$$은 회전해도 그 자리에 남는다. 이들은 0차원 궤도이다.

- **Orbit space**: $$S^2 / S^1 \cong [-1, 1]$$로, 각 위도 $$x_3 \in [-1, 1]$$이 하나의 궤도를 대표한다. 이것이 **moment polytope**의 가장 간단한 예시이다.

사실 $$S^2 \cong \mathbb{P}^1$$이며, $$\mathbb{P}^1$$은 가장 기본적인 (projective) toric variety이다. 이 예시에서 볼 수 있듯이, torus action은 다양체를 궤도들로 나누고, 각 궤도의 차원은 그 점에서의 torus action의 "자유도"에 의해 결정된다.

이제 위에서 정의한 canonical한 torus action이 이 예시에서 어떻게 작동하는지 확인해보자. $$\mathbb{P}^1$$의 경우 $$N = \mathbb{Z}$$이고 $$M = \Hom(\mathbb{Z}, \mathbb{Z}) \cong \mathbb{Z}$$이다. 따라서 $$T_N = \mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{C}^\ast \cong \mathbb{C}^\ast$$이며, $$S^1 \subset \mathbb{C}^\ast$$가 그 안에 포함된다.

$$\mathbb{P}^1$$의 한 affine patch $$U_1 = \{[1:w] \mid w \in \mathbb{C}\}$$를 생각하면, 그 coordinate ring은 $$\mathbb{C}[w]$$이다. 단항식 $$w^n$$에 대해, $$t \in \mathbb{C}^\ast$$가 다음과 같이 작용한다:

$$t \cdot w^n = \chi^n(t) \cdot w^n$$

여기서 canonical 정의에 따라 $$\chi^n(t)$$를 계산해보자. $$t = 1 \otimes c \in T_N = \mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{C}^\ast$$ (즉 $$c = t$$)이고 $$n \in M = \mathbb{Z}$$이므로

$$\chi^n(t) = c^{n(1)} = t^n$$

이다. 따라서 $$t \cdot w^n = t^n \cdot w^n$$이고, 특히 $$S^1 \subset \mathbb{C}^\ast$$의 원소 $$e^{i\theta}$$에 대해서는

$$e^{i\theta} \cdot w^n = e^{i\theta n} \cdot w^n$$

이다. 이것이 정확히 $$\mathbb{C}[w] = \bigoplus_{n \geq 0} \mathbb{C} \cdot w^n$$에서의 weight decomposition이며, 각 $$w^n$$은 weight $$n \in M$$을 갖는 eigenvector이다.

</div>

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
