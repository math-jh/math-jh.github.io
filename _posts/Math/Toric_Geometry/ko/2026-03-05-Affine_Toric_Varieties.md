---
title: "Affine toric varieties"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/affine_toric_varieties

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Affine_Toric_Varieties.png
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

으로 주어진다. 그럼 이 때 자연스러운 evaluation pairing $$M\times N \to \mathbb{Z}$$, $$(m, v) \mapsto m(v)$$를 *dual pairing<sub>쌍대 페어링</sub>*이라 부른다. 

</div>

논의의 편의를 위해 다음 두 표기

$$N_{\mathbb{R}} = N \otimes_{\mathbb{Z}} \mathbb{R},\qquad M_{\mathbb{R}} = M \otimes_{\mathbb{Z}} \mathbb{R}$$

을 도입하자. 이제 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$N_{\mathbb{R}}$$의 부분집합 $$\sigma$$가 다음 조건을 만족할 때, 이를 *strongly convex rational polyhedral cone<sub>강하게 볼록한 유리 다각형뿔</sub>*이라 한다:

1. $$\sigma$$는 원점을 꼭짓점으로 하는 cone이다. 즉 $$\lambda v \in \sigma$$가 모든 $$v \in \sigma$$, $$\lambda \ge 0$$에 대해 성립한다.
2. $$\sigma$$는 유한 개의 벡터 $$v_1, \ldots, v_s \in N$$의 $$\mathbb{R}_{\ge 0}$$-linear combination으로 생성된다. 즉 $$\sigma = \mathbb{R}_{\ge 0} v_1 + \cdots + \mathbb{R}_{\ge 0} v_s$$이라 할 수 있다.
3. $$\sigma$$는 *strongly convex*이다. 즉 $$\sigma \cap (-\sigma) = \{0\}$$이 성립한다.

</div>

여기서 세 번째 조건은 $$\sigma$$가 원점을 지나는 직선을 포함하지 않는다는 것을 의미한다. 한편 각각의 cone $$\sigma$$에 대하여, 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Cone $$\sigma$$의 *face<sub>면</sub>* $$\tau$$는 $$\sigma$$ 위에서 $$\langle u, v \rangle \ge 0$$이 모든 $$v \in \sigma$$에 대해 성립하는 어떤 $$u \in M_{\mathbb{R}}$$에 대해

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

$$S_\sigma = \sigma^\vee \cap M = \{ u \in M \mid \langle u, v \rangle \ge 0 \text{ for all } v \in \sigma \}$$

을 정의하고, 이를 통해 *semigroup algebra*

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\,{\rchi}^u \mid u \in S_\sigma]$$

을 정의한다. ([\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)) 여기서 $$\rchi^u$$는 $$M$$의 원소 $$u$$에 대응되는 단항식이다.

</div>

이를 풀어쓰면 다음과 같다. 그 정의에 의하여 $$S_\sigma$$는 덧셈에 대한 semigroup이며, semigroup algebra $$\mathbb{C}[S_\sigma]$$는 가장 깔끔하게는 집합 $$S_\sigma$$ 위의 자유 $$\mathbb{C}$$-벡터공간에 곱셈

$$\rchi^u\cdot\rchi^{u'}=\rchi^{u+u'}$$

을 부여한 것으로 기술된다. 즉 $$\mathbb{C}[S_\sigma]$$는 $$\{\rchi^u \mid u\in S_\sigma\}$$를 basis로 가지며, 위의 곱셈으로 생성되는 $$\mathbb{C}$$-algebra이다. 그럼 이 $$\mathbb{C}$$-algebra가 affine toric variety의 coordinate ring이 된다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Strongly convex rational polyhedral cone $$\sigma \subseteq N_{\mathbb{R}}$$에 대해, 이것이 정의하는 *affine toric variety<sub>아핀 토릭 다양체</sub>* $$U_\sigma$$를

$$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$

로 정의한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$\sigma = \{0\}$$인 경우, $$\sigma^\vee = M_{\mathbb{R}}$$이므로 $$S_\sigma = M$$이다. 따라서

$$\mathbb{C}[S_\sigma] = \mathbb{C}[M] = \mathbb{C}[\rchi^{\pm e_1^\ast}, \ldots, \rchi^{\pm e_n^\ast}]$$

이며, 이것은 $$(\mathbb{C}^\ast)^n$$의 coordinate ring에 해당한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$N = \mathbb{Z}^2$$에서 $$\sigma$$가 $$e_1$$과 $$e_2$$로 생성되는 경우를 생각하자. 그러면

$$\sigma^\vee = \mathbb{R}_{\ge 0} e_1^\ast + \mathbb{R}_{\ge 0} e_2^\ast$$

이므로 $$S_\sigma = \mathbb{Z}_{\ge 0}^2$$이고,

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\rchi^{e_1^\ast}, \rchi^{e_2^\ast}] = \mathbb{C}[\z_1, \z_2]$$

이다. 따라서 $$U_\sigma = \mathbb{C}^2$$이다.

</div>

## 토러스 작용

우리는 $$\Spec(\mathbb{C}[S_\sigma])$$ 위에 torus action을 정의하기 위해, 이미 친숙한 $$\mathbb{P}^N$$의 예시를 살펴본다. $$\mathbb{P}^N = \Proj(\mathbb{C}[\x_0, \ldots, \x_N])$$의 경우, $$\mathbb{C}^\ast$$가 scaling action을 하면 polynomial ring $$\mathbb{C}[\x_0, \ldots, \x_N]$$이 degree-by-degree로 분해된다. 각 homogeneous component $$\mathbb{C}[\x_0, \ldots, \x_N]_d$$는 $$\mathbb{C}^\ast$$-module로서 eigenspace를 형성한다.

이와 비슷하게, $$\mathbb{C}[S_\sigma]$$ 위에서도 $$M$$-grading이 weight decomposition을 제공한다. $$M$$-grading에 의해

$$\mathbb{C}[S_\sigma] = \bigoplus_{u \in S_\sigma} \mathbb{C} \cdot \rchi^u$$

라 하자. 여기서 각 $$\rchi^u$$는 weight $$u$$를 갖는 eigenvector이다. 즉, $$\mathbb{C}^\ast$$가 $$\mathbb{C}[S_\sigma]$$에 scaling을 하면, 각 $$\rchi^u$$는 eigenvalue $$\rchi^u(t) \in \mathbb{C}^\ast$$를 갖는다. 이 $$M$$-grading이 정확히 torus action에 대한 weight decomposition을 나타낸다.

한편 $$T_N$$을 다음과 같이 정의한다:

$$T_N = N \otimes_{\mathbb{Z}} \mathbb{C}^\ast.$$

이는 두 abelian group의 tensor product이지만, $$\mathbb{C}^\ast$$의 연산이 곱셈이므로 다소 헷갈릴 수 있다. 우선 집합으로서 $$T_N$$은 $$v \in N$$, $$z \in \mathbb{C}^\ast$$에 대하여 $$v \otimes z$$의 형태를 갖는 원소들의 유한합이며, 덧셈으로 구성된 abelian group이다. 이 때 bilinearity에 의해 다음의 관계들이 성립한다.

$$(v_1 + v_2) \otimes z = v_1 \otimes z + v_2 \otimes z,\qquad v \otimes (z_1 z_2) = v \otimes z_1 + v \otimes z_2,\qquad (k v) \otimes z = v \otimes z^k \quad (k \in \mathbb{Z})$$

여기서 두 번째 식의 좌변은 $$\mathbb{C}^\ast$$의 곱셈이고 우변은 $$T_N$$의 덧셈이라는 점에 주의하자. 즉 tensor product 안에서 $$\mathbb{C}^\ast$$의 곱셈은 $$T_N$$의 덧셈으로 옮겨진다.

이제 $$N$$의 basis $$e_1, \ldots, e_n$$을 도입하면, $$T_N$$의 임의의 원소는 다음과 같이 쓸 수 있다.

$$t = e_1 \otimes z_1 + \cdots + e_n \otimes z_n = (z_1, \ldots, z_n), \qquad z_i \in \mathbb{C}^\ast$$

그럼 이 표기 하에서 두 원소의 덧셈은

$$t + t' = e_1 \otimes (z_1 z_1') + \cdots + e_n \otimes (z_n z_n') = (z_1 z_1', \ldots, z_n z_n')$$

으로 주어지므로, $$T_N$$은 multiplicative group $$(\mathbb{C}^\ast)^n$$으로 자연스럽게 해석된다. 이제 $$M = \Hom(N, \mathbb{Z})$$의 원소 $$m$$에 대해 group homomorphism $$\rchi^m : T_N \to \mathbb{C}^\ast$$를 다음의 식

$$\rchi^m(t) := z^{m(v)}, \qquad t = v \otimes z \in T_N, \; m(v) \in \mathbb{Z}$$

으로 정의하자. 우리 주장은 이것이 잘 정의된 group homomorphism이라는 것이다. 먼저 $$T_N$$의 임의의 원소는 유한합 $$t = \sum_i v_i \otimes z_i$$의 꼴로 주어지며, 그럼 이 원소에 대해

$$\rchi^m(t) := \prod_i z_i^{m(v_i)}$$

으로 정의하면 이것이 위의 정의를 확장하는 well-defined function을 준다는 것을 안다. 한편 임의의 두 원소

$$t = \sum_i v_i \otimes z_i,\qquad t' = \sum_j v_j' \otimes z_j'$$

에 대하여,

$$\rchi^m(t + t') = \rchi^m\!\left(\sum_i v_i \otimes z_i + \sum_j v_j' \otimes z_j'\right) = \prod_i z_i^{m(v_i)} \prod_j (z_j')^{m(v_j')} = \rchi^m(t)\rchi^m(t')$$

가 성립하므로 $$\rchi^m$$은 group homomorphism이다. 더 구체적으로 $$N$$의 basis $$e_1, \ldots, e_n$$과 dual basis $$e_1^\ast, \ldots, e_n^\ast \in M$$을 도입하면, $$m \in M$$은 $$m = m_1 e_1^\ast + \cdots + m_n e_n^\ast$$로 쓸 수 있고, 이에 따라

$$\rchi^m(t) = z_1^{m_1} \cdots z_n^{m_n}$$

가 된다. 즉, *character group* $$\Hom(T_N, \mathbb{C}^\ast)$$는 dual lattice $$M$$과 isomorphic하다.

이제 위와 같이 torus에 대한 이해를 바탕으로 $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$ 위에 $$T_N$$-action을 정의한다. $$\Spec$$이 contravariant functor라는 사실로부터, geometric action $$T_N \times U_\sigma \to U_\sigma$$는 coordinate ring $$\mathbb{C}[S_\sigma]$$ 위의 comodule structure로 인코딩되며, 이 contravariance가 점 차원에서 어떻게 발현되는지는 [예시 12](#ex12)에서 직접 확인한다.

구체적으로, 다음의 $$\mathbb{C}$$-algebra homomorphism

$$\rho : \mathbb{C}[S_\sigma] \longrightarrow \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C}[M], \qquad \rchi^u \longmapsto \rchi^u \otimes \rchi^u.$$

을 정의하자. 여기서 $$\mathbb{C}[M] = \mathbb{C}[\rchi^m \mid m \in M]$$은 $$T_N$$의 coordinate ring이며, $$\rchi^u \in \mathbb{C}[S_\sigma]$$는 weight $$u$$를 갖는 eigenvector이다. $$\rho$$가 well-defined algebra homomorphism임은 bilinearity에 의해 직접 확인할 수 있다. 한편 tensor 순서 $$\mathbb{C}[S_\sigma] \otimes \mathbb{C}[M]$$은 Spec을 취했을 때 기하학적으로 $$U_\sigma \times T_N \to U_\sigma$$에 해당하므로, 엄밀히 말하면 이는 $$T_N$$의 right action의 comorphism이다. 그러나 $$T_N$$이 abelian이므로 right action과 left action을 같게 취급할 수 있고, 우리는 이를 left action $$T_N \times U_\sigma \to U_\sigma$$로 다룰 것이다. 그럼 이제 각각의 $$t\in T_N$$에 대하여, $$t$$는 $$\mathbb{C}[S_\sigma]$$ 위에 다음의 합성함수

$$\mathbb{C}[S_\sigma] \xrightarrow{\rho} \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C}[M] \xrightarrow{\id \otimes \ev_t} \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C} \cong \mathbb{C}[S_\sigma]$$

에 의해 주어지는 것이다. 이 합성함수를 $$\rchi^u$$에 적용하면,

$$(\id \otimes \ev_t)(\rchi^u \otimes \rchi^u) = \rchi^u \otimes \rchi^u(t) = \rchi^u(t) \rchi^u$$

이고, 구체적으로 $$t$$가 $$\rchi^u \in \mathbb{C}[S_\sigma]$$에 작용하는 결과는 $$\rchi^u(t) \rchi^u$$이다. 즉 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Algebraic torus $$T_N$$이 affine toric variety $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$ 위에 작용한다. 우선 coordinate ring $$\mathbb{C}[S_\sigma]$$ 위에 다음의 $$\mathbb{C}$$-algebra homomorphism $$\rho$$를 정의한다.

$$\rho : \mathbb{C}[S_\sigma] \longrightarrow \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C}[M], \qquad \rchi^u \longmapsto \rchi^u \otimes \rchi^u.$$

그럼 이 $$\rho$$가 $$U_\sigma$$ 위의 $$T_N$$-action을 정의하며, 각각의 $$t \in T_N$$에 대하여 $$t$$가 $$\rchi^u \in \mathbb{C}[S_\sigma]$$에 작용하는 결과는 다음과 같다:

$$t \cdot \rchi^u = \rchi^u(t) \rchi^u.$$

여기서 $$\rchi^u : T_N \to \mathbb{C}^\ast$$는 $$u \in M$$에 대응되는 character이며, $$\rchi^u(t) \in \mathbb{C}^\ast$$는 그 값이다.

</div>

다소 주의할 것은 지금까지의 논의에서 $$\rchi^u$$라는 기호가 두 가지 다른 의미로 쓰이고 있다는 것이다. 우선 $$\rchi^u$$는 그 정의에 의해 $$T_N$$에서 $$\mathbb{C}^\ast$$로의 group homomorphism이지만, 벡터공간 $$\mathbb{C}[S_\sigma]$$의 원소로서 $$\rchi^u$$를 생각할 때 우리는 이를 weight $$u$$를 갖는 eigenvector로 생각한다. 위의 식

$$t\cdot \rchi^u=\rchi^u(t)\rchi^u$$

가 바로 이 둘의 관계를 알려주며, 구체적으로 벡터공간 $$\mathbb{C}[S_\sigma]$$ 위에 $$T_N$$이 act할 때 $$\rchi^u$$는 이 작용의 eigenvector이며, 그에 해당하는 eigenvalue가 정확히 $$\rchi^u(t)$$로 주어지는 것이다. 

또한 위에서 정의한 $$T_N$$의 함수 위 작용 $$t\cdot f$$는 좀 더 정확히는 *pullback* $$(t\cdot f)(x) := f(t\cdot x)$$로 주어진 것이다. 임의의 대수군에 대해서는 함수 위의 left action을 표준적으로 $$(g\cdot f)(x) = f(g^{-1}\cdot x)$$로 정의하지만, $$T_N$$이 abelian이므로 위와 같이 inverse 없이 정의해도 여전히 left action이 된다. 이 convention의 장점은 $$\rchi^u$$가 정확히 weight $$u$$를 갖는 eigenvector가 된다는 점이며 (표준 convention을 따랐다면 weight는 $$-u$$가 되었을 것이다), 이는 [CLS, §1.1]의 convention과 일치한다. 곧 살펴볼 점 위의 작용이 inverse 없이 $$(t_1, t_2)\cdot(z_1, z_2) = (t_1 z_1, t_2 z_2)$$로 나오는 것도 같은 이유이다.

이 작용은 $$U_\sigma$$ 안에서 open dense torus orbit을 가지며, 이 orbit은 정확히 torus $$T_N$$ 자체이다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 모든 affine toric variety $$U_\sigma$$는 torus $$T_N$$을 열린 조밀한 부분집합으로 포함한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\sigma = \{0\}$$인 경우 $$\sigma^\vee = M_{\mathbb{R}}$$이므로 $$S_\sigma = M$$이고, 따라서 $$U_\sigma = \Spec(\mathbb{C}[M]) = T_N$$이다.

일반적인 경우 $$S_\sigma \subseteq M$$이므로 $$\mathbb{C}[S_\sigma] \subseteq \mathbb{C}[M]$$이고, 이는 자연스러운 dominant morphism

$$T_N = \Spec(\mathbb{C}[M]) \longrightarrow \Spec(\mathbb{C}[S_\sigma]) = U_\sigma$$

을 유도한다. 더욱이 $$\sigma$$가 strongly convex이므로 $$\sigma^\vee$$는 $$M_{\mathbb{R}}$$에서 full-dimensional cone이고, 그 내부에 lattice point $$u_0 \in M$$이 존재한다. 임의의 $$m \in M$$에 대해 충분히 큰 $$N$$을 잡으면 $$Nu_0$$과 $$Nu_0 + m$$이 모두 $$S_\sigma$$에 속하므로 $$m = (Nu_0 + m) - Nu_0$$로 $$S_\sigma$$가 group으로서 $$M$$ 전체를 생성하고, $$\mathbb{C}[S_\sigma]$$의 fraction field는 $$\mathbb{C}(M)$$과 일치한다. 따라서 $$T_N \hookrightarrow U_\sigma$$는 열린 조밀한 부분집합이 된다.

</details>

이어서 face 구조가 affine toric variety 위에서 어떻게 발현되는지 살펴본다. 이를 위해 다음 보조정리가 핵심적이다.

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10 (separation lemma)**</ins> Cone $$\sigma$$의 face $$\tau$$에 대하여 다음을 만족하는 $$u \in S_\sigma$$가 존재한다.

$$\tau = \sigma \cap u^{\perp}.$$

더욱이 이러한 $$u$$에 대해

$$\tau^\vee = \sigma^\vee + \mathbb{R}_{\ge 0}(-u)$$

가 성립한다. (증명은 [CLS] Proposition 1.2.13 및 1.2.10을 참조한다.)

</div>

이로부터 다음 명제가 따른다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Cone $$\sigma$$의 face $$\tau$$에 대하여, $$U_\tau$$는 $$U_\sigma$$의 principal open subset이다. ([\[대수다양체\] §아핀다양체, ⁋정의 5](/ko/math/algebraic_varieties/affine_varieties#def5)) 구체적으로, $$u \in S_\sigma$$를 $$\tau = \sigma \cap u^{\perp}$$를 만족하는 것으로 선택하면

$$U_\tau = \{ x \in U_\sigma \mid \rchi^u(x) \neq 0 \}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$u \in S_\sigma$$이고 $$\tau = \sigma \cap u^\perp$$라고 하자. [보조정리 10](#lem10)에 의해 $$\tau^\vee = \sigma^\vee + \mathbb{R}_{\ge 0}(-u)$$이 성립하므로,

$$S_\tau = \tau^\vee \cap M = (\sigma^\vee + \mathbb{R}_{\ge 0}(-u)) \cap M = S_\sigma + \mathbb{Z}_{\ge 0}(-u)$$

이다. 이로부터 semigroup algebra의 localization이

$$\mathbb{C}[S_\tau] = \mathbb{C}[S_\sigma + \mathbb{Z}_{\ge 0}(-u)] = \mathbb{C}[S_\sigma][\rchi^{-u}] = \mathbb{C}[S_\sigma]_{\rchi^u}$$

임을 얻는다. 여기서 $$\rchi^u \in \mathbb{C}[S_\sigma]$$이고 $$\rchi^{-u}$$는 $$\rchi^u$$의 역원이다. 따라서

$$U_\tau = \Spec(\mathbb{C}[S_\tau]) = \Spec(\mathbb{C}[S_\sigma]_{\rchi^u}) = (U_\sigma)_{\rchi^u} = \{ x \in U_\sigma \mid \rchi^u(x) \neq 0 \}$$

가 성립한다.

</details>

가령 [예시 7](#ex7)의 2차원 cone $$\sigma$$의 경우, $$\sigma$$의 face $$\tau_1=\mathbb{R}_{\geq 0}e_1$$과 $$\tau_2=\mathbb{R}_{\geq 0}e_2$$는 그 각각 또한 1차원 cone이 되며, 이들의 face는 원점이다. 이 구조 하에서 전체 $$U_\sigma$$ 안에서 $$U_{\tau_1}$$과 $$U_{\tau_2}$$ 각각은 principal open set이며, 이러한 face 구조에 따라 $$U_\sigma$$가 CW complex와 유사한 stratification을 가지게 된다. 

우리 주장은 위의 open embedding $$U_\tau \hookrightarrow U_\sigma$$는 $$T_N$$-equivariant라는 것이다. 즉, $$T_N$$이 $$U_\tau$$와 $$U_\sigma$$ 위에 각각 작용할 때, 이 작용들은 inclusion과 compatible하다. 이는 단순한 계산으로 보일 수 있으며, 따라서 위의 inclusion은 toric variety로서의 inclusion이기도 하다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> [예시 7](#ex7)에서 $$N = \mathbb{Z}^2$$이고 $$\sigma = \mathbb{R}_{\geq 0}e_1+ \mathbb{R}_{\geq 0}e_2$$일 때 $$U_\sigma = \mathbb{C}^2$$임을 보았다. 이제 torus $$T_N = (\mathbb{C}^\ast)^2$$가 $$U_\sigma = \mathbb{C}^2$$ 위에 어떻게 작용하는지 구체적으로 살펴보자.

우선 [예시 7](#ex7)에서 본 대로 $$\mathbb{C}[S_\sigma] = \mathbb{C}[\z_1, \z_2]$$이며 ($$\z_i = \rchi^{e_i^\ast}$$), $$U_\sigma = \Spec(\mathbb{C}[\z_1, \z_2]) = \mathbb{C}^2$$이다. 이제 [명제 8](#prop8)에 따르면, $$t = (t_1, t_2) \in T_N = (\mathbb{C}^\ast)^2$$는 coordinate ring 위에 다음의 식

$$t \cdot \z_i = \rchi^{e_i^\ast}(t) \z_i = t_i \z_i \qquad i = 1, 2$$

을 통해 작용한다. 이로부터 점 위의 작용을 읽어내기 위해, $$\mathbb{C}^2$$의 점 $$(z_1, z_2)$$가 $$\mathbb{C}[\z_1, \z_2]$$의 maximal ideal $$\mathfrak{m} = (\z_1 - z_1, \z_2 - z_2)$$에 대응한다는 사실을 떠올리자. 이 때 $$\mathfrak{m}$$의 generator에 ring map $$\sigma_t^\ast : \z_i \mapsto t_i \z_i$$를 단순히 적용해서 얻어지는 ideal $$(t_1\z_1 - z_1, t_2\z_2 - z_2) = (\z_1 - z_1/t_1, \z_2 - z_2/t_2)$$는 점 $$(z_1/t_1, z_2/t_2)$$에 대응하므로 inverse action처럼 보이는데, 이는 점 위의 작용이 forward image가 아니라 Spec functor의 contravariance에 따라 *preimage*로 주어지기 때문이다. 실제로 $$\sigma_t^\ast(\z_i - t_i z_i) = t_i(\z_i - z_i) \in \mathfrak{m}$$이므로 $$\z_i - t_i z_i \in (\sigma_t^\ast)^{-1}(\mathfrak{m})$$이고, 따라서 $$t \cdot (z_1, z_2)$$에 대응하는 maximal ideal은 $$(\z_1 - t_1 z_1, \z_2 - t_2 z_2)$$이며

$$(t_1, t_2) \cdot (z_1, z_2) = (t_1 z_1, t_2 z_2)$$

로 주어진다. 이는 $$(\mathbb{C}^\ast)^2$$의 각 성분이 $$\mathbb{C}^2$$의 대응하는 coordinate를 scaling하는 가장 자연스러운 작용이다.

이 작용의 궤도(orbit) 구조는 다음과 같다:

- **열린 조밀한 궤도**: $$(\mathbb{C}^\ast)^2 = \{(z_1, z_2) \mid z_1 \neq 0, z_2 \neq 0\}$$. 이는 torus $$T_N$$ 자체이며, $$U_\sigma$$에서 Zariski open dense subset을 이룬다.
- **1차원 궤도**: coordinate axis $$(\mathbb{C}^\ast) \times \{0\}$$과 $$\{0\} \times (\mathbb{C}^\ast)$$. 이들은 각각 한 개의 coordinate가 0이 되어 torus action의 "자유도"가 하나 줄어든 궤도이다.
- **고정점**: 원점 $$(0, 0)$$. 이는 torus의 모든 원소에 의해 고정되며, **0차원 궤도**이다.

이 예시는 torus action의 가장 기본적이고 대표적인 예시이다. [예시 7](#ex7)에서 살펴본 $$\sigma = \cone(e_1, e_2)$$에 대응하는 아핀 토릭 다양체 $$U_\sigma = \mathbb{C}^2$$ 위에서, torus는 단순히 좌표축 방향으로 scaling함으로써 작용하며, 이로부터 자연스럽게 궤도 분해가 이루어진다. 이러한 구조는 일반적인 affine toric variety에서도 동일한 패턴을 따르며, cone의 face들에 대응하는 궤도들이 차원이 낮아지는 방식으로 배열된다.

</div>

## 기본 성질

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> 아핀 토릭 다양체 $$U_\sigma$$에 대해 다음이 성립한다:

1. $$U_\sigma$$는 **정규(normal)** 다양체이다.
2. $$U_\sigma$$는 **기약(irreducible)**이다.
3. $$U_\sigma$$의 차원은 $$n$$이다 (여기서 $$N \cong \mathbb{Z}^n$$).

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**1. 정규성(Normality).** Gordan의 보조정리(Gordan's lemma)에 의해 $$S_\sigma = \sigma^\vee \cap M$$은 finitely generated semigroup이다. 더욱이 $$S_\sigma$$는 *saturated*이다: 즉 $$k \cdot u \in S_\sigma$$인 $$k \in \mathbb{Z}_{>0}$$와 $$u \in M$$에 대해 $$u \in S_\sigma$$이다. 이는 $$\langle u, v \rangle \ge 0$$가 $$\sigma$$ 위에서 성립함을 의미한다. Affine semigroup algebra가 normal domain이 되는 것은 그 semigroup이 saturated인 것과 동치이므로 ([CLS] Theorem 1.3.5 참조), $$\mathbb{C}[S_\sigma]$$는 normal domain이고 그 스펙트럼인 $$U_\sigma$$는 정규 다양체이다.

**2. 기약성(Irreducibility).** $$S_\sigma$$는 torsion-free abelian group $$M$$의 부분 semigroup이므로, $$\mathbb{C}[S_\sigma]$$에는 zero divisor가 존재하지 않는다. 따라서 $$\mathbb{C}[S_\sigma]$$는 integral domain이고 $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$는 기약 다양체이다.

**3. 차원(Dimension).** $$\mathbb{C}[S_\sigma] \subseteq \mathbb{C}[M]$$이므로 fraction field는 $$\mathbb{C}(M)$$에 포함된다. 한편 $$\sigma$$가 strongly convex이므로 $$\sigma^\vee$$는 $$M_{\mathbb{R}}$$에서 full-dimensional cone이며, 따라서 $$\sigma^\vee$$ 내부에 lattice point $$u_0 \in M$$이 존재한다. 임의의 $$m \in M$$에 대해 충분히 큰 $$N$$을 잡으면 $$Nu_0$$과 $$Nu_0 + m$$이 모두 $$S_\sigma$$에 속하므로 $$m = (Nu_0 + m) - Nu_0$$로 $$S_\sigma$$가 group으로서 $$M$$ 전체를 생성하고, $$\mathbb{C}[S_\sigma]$$의 fraction field는 정확히 $$\mathbb{C}(M)$$과 일치한다. $$M \cong \mathbb{Z}^n$$이므로 $$\mathbb{C}(M)$$의 transcendence degree는 $$n$$이고, 이로부터 $$\dim U_\sigma = n$$이 성립한다.

</details>

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
