---
title: "아핀 토릭 다양체"
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

여기서 첫 번째 조건만으로는 $$\sigma$$가 convex일 보장이 없지만, 두 번째 조건의 $$\mathbb{R}_{\ge 0}$$-linear combination 형태에 의해 $$\sigma$$가 closed convex cone이 됨이 자동으로 따른다. 또한 세 번째 조건은 $$\sigma$$가 원점을 지나는 직선을 포함하지 않는다는 것을 의미한다. 한편 각각의 cone $$\sigma$$에 대하여, 다음을 정의할 수 있다.

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

을 부여한 것으로 기술된다. 즉 $$\mathbb{C}[S_\sigma]$$는 $$\{\rchi^u \mid u\in S_\sigma\}$$를 basis로 가지며, 위의 곱셈으로 생성되는 $$\mathbb{C}$$-algebra이다. 한편 $$S_\sigma$$가 finitely generated semigroup임은 *Gordan's lemma* ([Wikipedia](https://en.wikipedia.org/wiki/Gordan%27s_lemma))에 의해 알려져 있으며, 따라서 $$\mathbb{C}[S_\sigma]$$는 finitely generated $$\mathbb{C}$$-algebra가 된다. 그럼 이 $$\mathbb{C}$$-algebra가 affine toric variety의 coordinate ring이 된다. 

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

## 매끄러움

위의 [예시 6](#ex6)의 $$\sigma = \{0\}$$과 [예시 7](#ex7)의 standard quadrant $$\sigma = \mathrm{cone}(e_1, e_2)$$에서 $$U_\sigma$$가 각각 $$T_N$$, $$\mathbb{C}^2$$로 모두 smooth algebraic variety였다. 이제 우리는 이것이 우연이 아닐 뿐만 아니라 $$U_\sigma$$의 smoothness가 cone $$\sigma$$의 조합론적 데이터만으로 완전히 판정된다는 것을 살펴볼 것이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Strongly convex rational polyhedral cone $$\sigma \subset N_{\mathbb{R}}$$가 *smooth<sub>매끄러운</sub>* (또는 *regular*, *nonsingular*) cone이라는 것은, $$\sigma$$의 primitive ray generator들 $$v_1, \ldots, v_k$$ ($$k = \dim \sigma$$)이 lattice $$N$$의 어떤 $$\mathbb{Z}$$-basis의 일부를 이루는 것이다.

</div>

정의 자체는 다소 추상적으로 보일 수 있지만, 실용적으로는 다음의 두 조건이 합쳐진 것과 동치이다.

1. $$\sigma$$가 *simplicial*이다. 즉 ray 수와 차원이 일치한다.
2. ($$\sigma$$가 full-dimensional인 경우) primitive ray generator $$v_1, \ldots, v_n$$들을 열로 모은 행렬 $$[v_1 \mid \cdots \mid v_n] \in \mathrm{Mat}_n(\mathbb{Z})$$의 determinant가 $$\pm 1$$이다.

특히 $$N = \mathbb{Z}^2$$에서 2차원 cone에 대해서는 두 ray generator로 만든 $$2 \times 2$$ 행렬의 determinant가 $$\pm 1$$인지만 확인하면 되고, 실제로 [예시 6](#ex6)과 [예시 7](#ex7)은 이를 만족한다. 

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Affine toric variety $$U_\sigma$$가 smooth algebraic variety인 것은 $$\sigma$$가 smooth cone인 것과 필요충분조건이다. 더 구체적으로, $$\sigma$$가 smooth이고 $$k = \dim \sigma$$이면

$$U_\sigma \cong \mathbb{C}^k \times (\mathbb{C}^\ast)^{n-k}$$

가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($$\Leftarrow$$) $$\sigma$$가 smooth라 하자. 정의에 의해 ray generator $$v_1, \ldots, v_k$$가 $$N$$의 어떤 기저 $$\{v_1, \ldots, v_n\}$$의 일부를 이룬다. 이 기저의 dual basis $$\{v_1^\ast, \ldots, v_n^\ast\} \subset M$$를 택하면,

$$\sigma^\vee = \{u \in M_{\mathbb{R}} \mid \langle u, v_i\rangle \ge 0,\ i = 1, \ldots, k\} = \mathbb{R}_{\ge 0}\langle v_1^\ast, \ldots, v_k^\ast\rangle + \mathbb{R}\langle v_{k+1}^\ast, \ldots, v_n^\ast\rangle$$

이고 따라서

$$S_\sigma = \sigma^\vee \cap M = \mathbb{Z}_{\ge 0}\langle v_1^\ast, \ldots, v_k^\ast\rangle \oplus \mathbb{Z}\langle v_{k+1}^\ast, \ldots, v_n^\ast\rangle$$

이 된다. 그럼

$$\mathbb{C}[S_\sigma] = \mathbb{C}[\rchi^{v_1^\ast}, \ldots, \rchi^{v_k^\ast}, \rchi^{\pm v_{k+1}^\ast}, \ldots, \rchi^{\pm v_n^\ast}] \cong \mathbb{C}[x_1, \ldots, x_k, x_{k+1}^{\pm 1}, \ldots, x_n^{\pm 1}]$$

이므로 $$U_\sigma \cong \mathbb{C}^k \times (\mathbb{C}^\ast)^{n-k}$$가 smooth이다.

($$\Rightarrow$$) 역방향은 $$U_\sigma$$의 unique torus-fixed point (orbit-cone correspondence에서 $$\sigma$$ 자신에 대응)에서 cotangent space 차원이 ray 수 $$\lvert \sigma(1) \rvert$$와 같음을 보이는 데서 출발한다. $$U_\sigma$$가 smooth이면 이 차원이 $$n = \dim U_\sigma$$여야 하므로 ray 수가 $$n$$, 즉 $$\sigma$$가 simplicial이고 또한 $$N$$의 $$\mathbb{Z}$$-기저를 이뤄야 한다.

</details>

가령 $$N = \mathbb{Z}^2$$에서 $$\sigma = \mathrm{cone}(e_2,\ 2e_1 - e_2)$$를 잡으면, 두 ray의 primitive generator로 만든 행렬

$$\begin{vmatrix} 0 & 2 \\ 1 & -1 \end{vmatrix} = -2$$

이므로 $$\sigma$$는 simplicial이지만 smooth가 아니다. 실제로 $$S_\sigma$$의 minimal generator를 계산하면 $$u_1 = e_1^\ast$$, $$u_2 = e_1^\ast + e_2^\ast$$, $$u_3 = 2 e_1^\ast + e_2^\ast$$의 세 원소이고 관계식 $$u_1 u_3 = u_2^2$$가 성립하므로

$$\mathbb{C}[S_\sigma] \cong \mathbb{C}[x, y, z]/(xz - y^2)$$

이 되어, $$U_\sigma$$는 원점에 $$A_1$$ 특이점을 갖는 affine toric variety가 된다. 일반적으로 행렬식이 $$\pm d$$이면 $$U_\sigma$$는 원점에 $$\mathbb{Z}/d$$ quotient singularity를 갖는다.

## 토러스 작용

우리는 $$\Spec(\mathbb{C}[S_\sigma])$$ 위에 torus action을 정의하기 위해, 이미 친숙한 $$\mathbb{P}^N$$의 예시를 살펴본다. $$\mathbb{P}^N = \Proj(\mathbb{C}[\x_0, \ldots, \x_N])$$의 경우, $$\mathbb{C}^\ast$$가 scaling action을 하면 polynomial ring $$\mathbb{C}[\x_0, \ldots, \x_N]$$이 degree-by-degree로 분해된다. 각 homogeneous component $$\mathbb{C}[\x_0, \ldots, \x_N]_d$$는 $$\mathbb{C}^\ast$$-module로서 eigenspace를 형성한다.

이와 비슷하게, $$\mathbb{C}[S_\sigma]$$ 위에서도 자연스러운 $$M$$-grading

$$\mathbb{C}[S_\sigma] = \bigoplus_{u \in S_\sigma} \mathbb{C} \cdot \rchi^u$$

이 존재하며, 곧 정의할 $$n$$차원 algebraic torus $$T_N$$이 $$\mathbb{C}[S_\sigma]$$ 위에 act할 때 각 1차원 부분공간 $$\mathbb{C}\cdot\rchi^u$$가 weight $$u \in M$$의 eigenspace가 된다. 즉 임의의 $$t \in T_N$$에 대해 $$\rchi^u$$는 eigenvalue $$\rchi^u(t) \in \mathbb{C}^\ast$$를 갖는 eigenvector이다. 이 $$M$$-grading이 정확히 torus action에 대한 weight decomposition을 나타낸다.

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

으로 정의하면 이것이 위의 정의를 확장하는 well-defined function을 준다는 것을 확인할 수 있다. 한편 임의의 두 원소

$$t = \sum_i v_i \otimes z_i,\qquad t' = \sum_j v_j' \otimes z_j'$$

에 대하여,

$$\rchi^m(t + t') = \rchi^m\!\left(\sum_i v_i \otimes z_i + \sum_j v_j' \otimes z_j'\right) = \prod_i z_i^{m(v_i)} \prod_j (z_j')^{m(v_j')} = \rchi^m(t)\rchi^m(t')$$

가 성립하므로 $$\rchi^m$$은 group homomorphism이다. 더 구체적으로 $$N$$의 basis $$e_1, \ldots, e_n$$과 dual basis $$e_1^\ast, \ldots, e_n^\ast \in M$$을 도입하면, $$m \in M$$은 $$m = m_1 e_1^\ast + \cdots + m_n e_n^\ast$$로 쓸 수 있고, 이에 따라

$$\rchi^m(t) = z_1^{m_1} \cdots z_n^{m_n}$$

가 된다. 즉, *character group* $$\Hom(T_N, \mathbb{C}^\ast)$$는 dual lattice $$M$$과 isomorphic하다.

이제 위와 같이 torus에 대한 이해를 바탕으로 $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$ 위에 $$T_N$$-action을 정의한다. $$\Spec$$이 contravariant functor라는 사실로부터, geometric action $$T_N \times U_\sigma \to U_\sigma$$는 coordinate ring $$\mathbb{C}[S_\sigma]$$ 위의 comodule structure로 인코딩되며, 이 contravariance가 점 차원에서 어떻게 발현되는지는 [예시 14](#ex14)에서 직접 확인한다.

구체적으로, 다음의 $$\mathbb{C}$$-algebra homomorphism

$$\rho : \mathbb{C}[S_\sigma] \longrightarrow \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C}[M], \qquad \rchi^u \longmapsto \rchi^u \otimes \rchi^u.$$

을 정의하자. 여기서 $$\mathbb{C}[M] = \mathbb{C}[\rchi^m \mid m \in M]$$은 $$T_N$$의 coordinate ring이며, $$\rchi^u \in \mathbb{C}[S_\sigma]$$는 weight $$u$$를 갖는 eigenvector이다. $$\rho$$가 well-defined algebra homomorphism임은 bilinearity에 의해 직접 확인할 수 있다. 

엄밀히 말하면 $$\mathbb{C}[S_\sigma] \otimes \mathbb{C}[M]$$은 Spec을 취했을 때 기하학적으로 $$U_\sigma \times T_N \to U_\sigma$$에 해당하므로, 이는 $$T_N$$의 right action의 comorphism이다. 그러나 $$T_N$$이 abelian이므로 right action과 left action을 같게 취급할 수 있고, 우리는 이를 left action $$T_N \times U_\sigma \to U_\sigma$$로 다룰 것이다. 그럼 이제 각각의 $$t\in T_N$$에 대하여, $$t$$는 $$\mathbb{C}[S_\sigma]$$ 위에 다음의 합성함수

$$\mathbb{C}[S_\sigma] \xrightarrow{\rho} \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C}[M] \xrightarrow{\id \otimes \ev_t} \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C} \cong \mathbb{C}[S_\sigma]$$

에 의해 주어지는 것이다. 이 합성함수를 $$\rchi^u$$에 적용하면,

$$(\id \otimes \ev_t)(\rchi^u \otimes \rchi^u) = \rchi^u \otimes \rchi^u(t) = \rchi^u(t) \rchi^u$$

이고, 구체적으로 $$t$$가 $$\rchi^u \in \mathbb{C}[S_\sigma]$$에 작용하는 결과는 $$\rchi^u(t) \rchi^u$$이다. Basis 원소 $$\rchi^u$$에 대해 counitality $$(\id \otimes \ev_e)\circ\rho = \id$$와 coassociativity $$(\rho \otimes \id)\circ\rho = (\id\otimes\Delta)\circ\rho$$가 직접 확인되므로 $$\rho$$는 $$\mathbb{C}[M]$$-comodule structure를 정의하며, 이는 $$U_\sigma$$ 위의 algebraic $$T_N$$-action에 정확히 대응한다. 따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Algebraic torus $$T_N$$이 affine toric variety $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$ 위에 작용한다. 우선 coordinate ring $$\mathbb{C}[S_\sigma]$$ 위에 다음의 $$\mathbb{C}$$-algebra homomorphism $$\rho$$를 정의한다.

$$\rho : \mathbb{C}[S_\sigma] \longrightarrow \mathbb{C}[S_\sigma] \otimes_{\mathbb{C}} \mathbb{C}[M], \qquad \rchi^u \longmapsto \rchi^u \otimes \rchi^u.$$

그럼 이 $$\rho$$가 $$U_\sigma$$ 위의 $$T_N$$-action을 정의하며, 각각의 $$t \in T_N$$에 대하여 $$t$$가 $$\rchi^u \in \mathbb{C}[S_\sigma]$$에 작용하는 결과는 다음과 같다:

$$t \cdot \rchi^u = \rchi^u(t) \rchi^u.$$

여기서 $$\rchi^u : T_N \to \mathbb{C}^\ast$$는 $$u \in M$$에 대응되는 character이며, $$\rchi^u(t) \in \mathbb{C}^\ast$$는 그 값이다.

</div>

다소 주의할 것은 지금까지의 논의에서 $$\rchi^u$$라는 기호가 두 가지 다른 의미로 쓰이고 있다는 것이다. 우선 $$\rchi^u$$는 그 정의에 의해 $$T_N$$에서 $$\mathbb{C}^\ast$$로의 group homomorphism이지만, 벡터공간 $$\mathbb{C}[S_\sigma]$$의 원소로서 $$\rchi^u$$를 생각할 때 우리는 이를 weight $$u$$를 갖는 eigenvector로 생각한다. 위의 식

$$t\cdot \rchi^u=\rchi^u(t)\rchi^u$$

가 바로 이 둘의 관계를 알려주며, 구체적으로 벡터공간 $$\mathbb{C}[S_\sigma]$$ 위에 $$T_N$$이 act할 때 $$\rchi^u$$는 이 작용의 eigenvector이며, 그에 해당하는 eigenvalue가 정확히 $$\rchi^u(t)$$로 주어지는 것이다. 

또 다른 미묘한 점은 위에서 정의한 $$T_N$$의 함수 위 작용 $$t\cdot f$$는 좀 더 정확히는 *pullback* 

$$(t\cdot f)(x) := f(t\cdot x)$$

로 주어졌다는 것이다. 일반적으로, 임의의 group algebra에 대해서는 함수 위의 left action을

$$(g\cdot f)(x) = f(g^{-1}\cdot x)$$

와 같이 정의하는 것이 표준적이지만, $$T_N$$이 abelian이므로 위와 같이 inverse 없이 정의해도 여전히 left action이 된다. 이 convention의 장점은 $$\rchi^u$$가 정확히 weight $$u$$를 갖는 eigenvector가 된다는 점으로, 만일 표준 convention을 따랐다면 $$\rchi^u$$의 weight는 $$-u$$가 되었을 것이다. 곧 살펴볼 점 위의 작용이 inverse 없이 $$(t_1, t_2)\cdot(z_1, z_2) = (t_1 z_1, t_2 z_2)$$로 나오는 것도 같은 이유이다.

어쨌든 위에서 정의한 torus action은 $$U_\sigma$$ 안에서 open dense torus orbit을 가지며, 이 orbit은 정확히 torus $$T_N$$ 자체이다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 모든 affine toric variety $$U_\sigma$$는 torus $$T_N$$을 open dense subset으로 포함한다.

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

<ins id="lem12">**보조정리 12 (Separation lemma)**</ins> Cone $$\sigma$$의 face $$\tau$$에 대하여 다음을 만족하는 $$u \in S_\sigma$$가 존재한다.

$$\tau = \sigma \cap u^{\perp}.$$

더욱이 이러한 $$u$$에 대해

$$\tau^\vee = \sigma^\vee + \mathbb{R}_{\ge 0}(-u)$$

가 성립한다.

</div>

이로부터 다음 명제가 따른다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Cone $$\sigma$$의 face $$\tau$$에 대하여, $$U_\tau$$는 $$U_\sigma$$의 principal open subset이다. ([\[대수다양체\] §아핀다양체, ⁋정의 5](/ko/math/algebraic_varieties/affine_varieties#def5)) 구체적으로, $$u \in S_\sigma$$를 $$\tau = \sigma \cap u^{\perp}$$를 만족하는 것으로 선택하면

$$U_\tau = \{ x \in U_\sigma \mid \rchi^u(x) \neq 0 \}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$u \in S_\sigma$$이고 $$\tau = \sigma \cap u^\perp$$라고 하자. [보조정리 12](#lem12)에 의해 $$\tau^\vee = \sigma^\vee + \mathbb{R}_{\ge 0}(-u)$$이 성립하므로,

$$S_\tau = \tau^\vee \cap M = (\sigma^\vee + \mathbb{R}_{\ge 0}(-u)) \cap M = S_\sigma + \mathbb{Z}_{\ge 0}(-u)$$

이다. 마지막 등호는 $$u \in S_\sigma$$와 $$-u \in M$$이라는 사실로부터, $$\sigma^\vee + \mathbb{R}_{\ge 0}(-u)$$의 임의의 lattice point가 어떤 $$w \in S_\sigma$$와 $$k \in \mathbb{Z}_{\ge 0}$$에 대해 $$w - ku$$ 꼴로 표현됨을 확인하면 얻어진다. 이로부터 semigroup algebra의 localization이

$$\mathbb{C}[S_\tau] = \mathbb{C}[S_\sigma + \mathbb{Z}_{\ge 0}(-u)] = \mathbb{C}[S_\sigma][\rchi^{-u}] = \mathbb{C}[S_\sigma]_{\rchi^u}$$

임을 얻는다. 여기서 $$\rchi^u \in \mathbb{C}[S_\sigma]$$이고 $$\rchi^{-u}$$는 $$\rchi^u$$의 역원이다. 따라서

$$U_\tau = \Spec(\mathbb{C}[S_\tau]) = \Spec(\mathbb{C}[S_\sigma]_{\rchi^u}) = (U_\sigma)_{\rchi^u} = \{ x \in U_\sigma \mid \rchi^u(x) \neq 0 \}$$

가 성립한다.

</details>

가령 [예시 7](#ex7)의 2차원 cone $$\sigma$$의 경우, $$\sigma$$의 face $$\tau_1=\mathbb{R}_{\geq 0}e_1$$과 $$\tau_2=\mathbb{R}_{\geq 0}e_2$$는 그 각각 또한 1차원 cone이 되며, 이들의 face는 원점이다. 이 구조 하에서 전체 $$U_\sigma$$ 안에서 $$U_{\tau_1}$$과 $$U_{\tau_2}$$ 각각은 principal open set이며, 이러한 face 구조에 따라 $$U_\sigma$$가 CW complex와 유사한 stratification을 가지게 된다. 

우리 주장은 위의 open embedding $$U_\tau \hookrightarrow U_\sigma$$는 $$T_N$$-equivariant라는 것이다. 즉, $$T_N$$이 $$U_\tau$$와 $$U_\sigma$$ 위에 각각 작용할 때, 이 작용들은 inclusion과 compatible하다. 이는 단순한 계산으로 보일 수 있으며, 따라서 위의 inclusion은 toric variety로서의 inclusion이기도 하다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> [예시 7](#ex7)에서 $$N = \mathbb{Z}^2$$이고 $$\sigma = \mathbb{R}_{\geq 0}e_1+ \mathbb{R}_{\geq 0}e_2$$일 때 $$U_\sigma = \mathbb{C}^2$$임을 보았다. 이제 torus $$T_N = (\mathbb{C}^\ast)^2$$가 $$U_\sigma = \mathbb{C}^2$$ 위에 어떻게 작용하는지 구체적으로 살펴보자.

우선 [예시 7](#ex7)에서 본 대로 $$\mathbb{C}[S_\sigma] = \mathbb{C}[\z_1, \z_2]$$이며 ($$\z_i = \rchi^{e_i^\ast}$$), $$U_\sigma = \Spec(\mathbb{C}[\z_1, \z_2]) = \mathbb{C}^2$$이다. 이제 [명제 10](#prop10)에 따르면, $$t = (t_1, t_2) \in T_N = (\mathbb{C}^\ast)^2$$는 coordinate ring 위에 다음의 식

$$t \cdot \z_i = \rchi^{e_i^\ast}(t) \z_i = t_i \z_i \qquad i = 1, 2$$

을 통해 작용한다. 이로부터 점 위의 작용을 읽어내기 위해, $$\mathbb{C}^2$$의 점 $$(z_1, z_2)$$가 $$\mathbb{C}[\z_1, \z_2]$$의 maximal ideal $$\mathfrak{m} = (\z_1 - z_1, \z_2 - z_2)$$에 대응한다는 사실을 떠올리자. 이 때 $$\mathfrak{m}$$의 generator에 ring map $$\sigma_t^\ast : \z_i \mapsto t_i \z_i$$를 적용해서 얻어지는 ideal은

$$(t_1\z_1 - z_1, t_2\z_2 - z_2) = (\z_1 - z_1/t_1, \z_2 - z_2/t_2)$$

인데, 이는 점 $$(z_1/t_1, z_2/t_2)$$에 대응하는 것이다. $$\Spec$$을 취했을 때는 contravariance에 의해 $$(z_1/t_1, z_2/t_2)$$이 $$(z_1,z_2)$$로 옮겨지는 것으로 해석되며, 따라서 점에서 이를 계산하면 torus action은

$$(t_1, t_2) \cdot (z_1, z_2) = (t_1 z_1, t_2 z_2)$$

로 주어진다. 이는 $$(\mathbb{C}^\ast)^2$$의 각 성분이 $$\mathbb{C}^2$$의 대응하는 coordinate를 scaling하는 가장 자연스러운 작용이다.

이제 이 action의 orbit 구조를 살펴보자. [명제 11](#prop11)이 주는 open dense orbit은 

$$(\mathbb{C}^\ast)^2 = \{(z_1, z_2) \mid z_1 \neq 0, z_2 \neq 0\}$$

으로, 이는 $$2$$차원 torus $$T_N$$ 자체이다. 또 흥미로운 것은 이보다 낮은 차원의 orbit들로, coordinate axis들 $$(\mathbb{C}^\ast) \times \{0\}$$과 $$\{0\} \times (\mathbb{C}^\ast)$$이 이에 해당한다. 이들은 각각 한 개의 coordinate가 0이 되어 torus action의 자유도가 하나 줄어든 궤도이다. 마찬가지로 원점 $$(0, 0)$$는 torus action의 fixed point로, 형식적으로는 $$0$$차원 orbit으로 생각할 수 있다. 

</div>

마지막으로 affine toric variety의 기본적인 성질을 증명하며 이 글을 마친다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Affine toric variety $$U_\sigma$$에 대해 다음이 성립한다:

1. $$U_\sigma$$는 normal variety이다.
2. $$U_\sigma$$는 irreducible이다.
3. $$U_\sigma$$는 $$n$$-dimensional variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. Normality의 경우, Gordan's lemma에 의해 $$S_\sigma = \sigma^\vee \cap M$$은 finitely generated semigroup이다. 더욱이 $$S_\sigma$$는 *saturated*이다: 즉 $$k \cdot u \in S_\sigma$$인 $$k \in \mathbb{Z}_{>0}$$와 $$u \in M$$에 대해 $$u \in S_\sigma$$이다. 이는 $$\langle u, v \rangle \ge 0$$가 $$\sigma$$ 위에서 성립함을 의미한다. Affine semigroup algebra가 normal domain이 되는 것은 그 semigroup이 saturated인 것과 동치이므로, $$\mathbb{C}[S_\sigma]$$는 normal domain이고 그 스펙트럼인 $$U_\sigma$$는 normal이다.
2. Irreducibility의 경우, $$S_\sigma$$는 torsion-free abelian group $$M$$의 부분 semigroup이므로, $$\mathbb{C}[S_\sigma]$$에는 zero divisor가 존재하지 않는다. 따라서 $$\mathbb{C}[S_\sigma]$$는 integral domain이고 $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$는 irreducible이다.
3. $$\mathbb{C}[S_\sigma] \subseteq \mathbb{C}[M]$$이므로 fraction field는 $$\mathbb{C}(M)$$에 포함된다. 한편 $$\sigma$$가 strongly convex이므로 $$\sigma^\vee$$는 $$M_{\mathbb{R}}$$에서 full-dimensional cone이며, 따라서 $$\sigma^\vee$$ 내부에 lattice point $$u_0 \in M$$이 존재한다. 임의의 $$m \in M$$에 대해 충분히 큰 $$N$$을 잡으면 $$Nu_0$$과 $$Nu_0 + m$$이 모두 $$S_\sigma$$에 속하므로 $$m = (Nu_0 + m) - Nu_0$$로 $$S_\sigma$$가 group으로서 $$M$$ 전체를 생성하고, $$\mathbb{C}[S_\sigma]$$의 fraction field는 정확히 $$\mathbb{C}(M)$$과 일치한다. $$M \cong \mathbb{Z}^n$$이므로 $$\mathbb{C}(M)$$의 transcendence degree는 $$n$$이고, 이로부터 $$\dim U_\sigma = n$$이 성립한다.

</details>

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
