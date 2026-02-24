---

title: "원환면의 작용"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/torus_action
header:
    overlay_image: /assets/images/Math/Lie_Theory/Torus_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2026-02-24
last_modified_at: 2026-02-24
weight: 2

---

임의의 유한군 $G$가 주어졌을 때 이를 잘 살펴보는 방법 중 하나는 그 유한차원 representation 

$$\rho:G\rightarrow \Aut(V)$$

을 보는 것이다. $V$의 basis를 선택하고 나면 $\rho$에 의한 $G$의 image를 다루는 것은 선형대수에 불과하므로 우리는 $G$의 구조를 훨씬 쉽게 알아낼 수 있다. 

Lie group의 경우 이러한 표현론적 관점은 더 도움이 되는데, Lie group은 $\GL(n;\mathbb{R})$이나 $\Diff(M)$과 같이, 본질적으로 다른 대상 위에 작용하는 것이기 때문이다. 

다만 [\[표현론\] §유한군의 표현론, ⁋정의 1](/ko/math/representation_theory/representations_of_finite_groups#def1)에서처럼 $G$의 representation theory를 정의하면 Lie group $G$ 위에 있는 smooth structure는 놓치게 되므로, 다음과 같이 정의해주어야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lie group $G$에 대하여, $G$의 *representation<sub>표현</sub>*은 유한차원 벡터공간 $V$와, smooth map

$$\rho:G\rightarrow \Aut(V)$$

이 주어진 것이다. 

</div>

만일 $G$를 discrete topology와 자명한 smooth structure가 주어진 Lie group으로 본다면 이 정의는 [\[표현론\] §유한군의 표현론, ⁋정의 1](/ko/math/representation_theory/representations_of_finite_groups#def1)의 일반화라 생각할 수도 있다. 비슷하게 [\[표현론\] §유한군의 표현론, §§표현론의 기본 개념들](/ko/math/representation_theory/representations_of_finite_groups#표현론의-기본-개념들)에 있는 모든 정의를 Lie group에 대해서도 할 수 있다. 

이 글에서 중요한 역할을 했던 것은 group $G$가 유한군이라는 사실이었다. 가령 $G$의 모든 원소에 대해 평균을 내는 아이디어는 이러한 사실을 바탕으로 했다. 이를 Lie group으로 일반화하기 위해서는 $G$에 어떠한 종류의 유한성을 강제해야 한다. 

우리는 따라서 $G$가 *compact* Lie group인 경우를 종종 다루게 된다. 이 경우, locally compact Hausdorff space로서 $G$ 위에는 Haar measure가 존재하며 따라서 $G$의 원소들에 대한 합을 $G$ 전체에 대한 적분으로 바꿔 쓸 수 있다. 물론 이를 위해서는 $\delta_x$ 함수를 잘 정의하고, 함수공간을 적당한 공간으로 일반화하는 작업을 거쳐야 하지만 이러한 작업은 우리의 현재 목적이 아니므로 생략하기로 혼다. 중요한 것은 리 군의 표현론 또한 유한군의 표현론과 같은 방법론을 통해 접근할 수 있다는 것이다. 특히 임의의 finite-dimensional representation은 irreducible decomposition들의 direct sum으로 나타낼 수 있다. 

한편, 유한차원 representation $G\rightarrow\Aut(V)$가 주어졌다 할 때, 가장 좋은 점은 이들의 image $\rho(g)$들을 (basis의 선택을 통해) 행렬로 생각할 수 있다는 것이다. 따라서 이를 통해 우리는 행렬과 선형사상에 대한 우리의 도구들을 사용하여 이를 탐구할 수 있다. 

선형대수에서 가장 중요한 도구 중 하나는 대각화이다. 따라서 우리는 주어진 Lie group action $\rho:G \rightarrow \Aut(V)$에 대하여, $V$의 basis를 적당히 택하여 $\rho(g)$의 행렬표현을 대각행렬로 만드는 데에 관심이 있다. 만일 $G$가 유한군이었다면, 각각의 $g$에 대해 이러한 basis를 찾아줄 수 있었겠지만 현재는 $G$가 무한하므로 이러한 일을 하기 힘들다. 따라서 우리는 simultaneously diagonalizable인 원소들에 자연스럽게 관심을 갖게 된다. 그런데 [\[선형대수학\] §고유공간분해, ⁋명제 10](/ko/math/linear_algebra/eigenspace_decomposition#prop10)은 두 diagonalizable matrix가 simultaneously diagonalizable일 필요충분조건은 이들이 commute하는 것임을 알고 있으므로, 다음 정의를 내리는 것이 합당하다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Compact, connected Lie group $G$에 대하여, $G$의 subgroup $T$가 *maximal torus*라는 것은 $T$가 torus이고, 포함관계에 대하여 maximal인 것이다. 

</div>

Lie algebra $\mathfrak{g}$의 임의의 원소 $X$를 택한 후, 이 방향으로의 exponential map이 그리는 one-parameter subgroup의 closure가 torus가 된다. 따라서 maximal torus의 존재성은 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의해 자명하다. 

## Weight decomposition

우리의 주장은 $\rho(T)$가 simultaneously diagonalizable이라는 것이다. 이를 위해서는 $\rho(T)$의 각각의 원소들이 diagonalizable인 것을 보이면 충분하다. 이를 위해 임의의 finite-dimensional representation $\rho:G\rightarrow \Aut(V)$을 생각하고 이를 maximal torus $T$로 제한한 representation $\rho\vert_T$을 생각하자. 가장 먼저 확인할 수 있는 것은 $T$가 compact Lie group이라는 사실이다. 따라서 [\[표현론\] §유한군의 표현론, ⁋명제 6](/ko/math/representation_theory/representations_of_finite_groups#prop6)과 [\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)이 모두 성립한다. 

보다 자세하게 이들을 하나하나 써 보면, 우선 $\rho\vert_T$가 unitary representation이라는 사실로부터 우리는 다음의 irreducible decomposition

$$V=\bigoplus_i V_i$$

을 생각할 수 있다. 여기에서 각각의 $V_\lambda$는 irreducible $T$-representation들이다. 한편, $T$가 abelian이므로 임의의 $t\in T$에 대하여, $\rho(t)$은 $T$-action과 모두 commute하고, 따라서 각각의 $V_i$로 제한하였을 때 $\rho(t)$는 $T$-automorphism이다. 이제 [\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)의 두 번째 결과에 의하여 $\rho(t)$는 상수배

$$\rho(t)(v)=\lambda_i(t)v\qquad \lambda_i(t)\in \mathbb{C}^\times$$

로 주어진다. 그런데 이제 $V_i$ 위에서 $T$가 상수배들로 작용한다면, $V_i$의 임의의 부분공간은 $T$-invariant일 것이며 따라서 $V_i$가 irreducible이기 위해서는 반드시 $\dim V_i=1$이어야만 한다. 

이제 $\dim V_i=1$이므로 $\Aut(V_i)\cong \mathbb{C}^\times$이고, 우리는 위의 $\lambda_i: T\rightarrow \mathbb{C}^\times$가 정확하게 $\rho$의 character에 해당하고, 따라서 irreducible decomposition이 직접적으로 character $\lambda_i$에 의해 parametrize되는 것으로 생각할 수 있다. 즉 다음의 식

$$V=\bigoplus_\lambda V_\lambda;\qquad V_\lambda=\{t\cdot v=\lambda(t)v\text{ for all $t\in T$}\}$$

을 통해 irreducible decomposition이 주어진 것으로 생각하자. 그럼 각각의 $t\in T$에 대하여, $\rho(t)$는 바로 이 decomposition에 의하여 대각화되고, 각각의 eigenspace $V_\lambda$에 해당하는 고유값은 $\lambda(t)$이다. 이와 다른 $t$의 선택은 위의 decomposition은 그대로 두고, 각각의 eigenspace $V_\lambda$에 해당하는 고유값만 바뀌는 것이다. 

직관적으로 $t\mapsto e^{2\pi i\lambda_i(X)}$를 각속도 $\lambda_i(X)$를 갖는 각운동이라 생각할 수 있고, 이러한 관점을 도입하면 우리는 각각의 $X\in \mathfrak{t}$가 주어졌을 때, 이 방향으로의 각속도 $\lambda_i(X)$가 얼마인지를 통해 이 torus action을 설명할 수 있다는 것을 안다. 이 때 각각의 $\lambda_i$들을 우리는 *weight*라 부른다. 그럼 우리는 각각의 weight $\lambda_i$마다 적당한 $V_i$가 존재하여, 이 위에서는 torus action이 $t\cdot v=\rchi_{\lambda_i}(t)v$로 작동하는 것을 안다. 이러한 $V_i$를 *weight space*라 부른다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 특별한 예시로, 1차원 torus

$$S^1\cong T \cong \mathbb{R}/\mathbb{Z}$$

을 생각하면, $S^1$은 다음의 집합

$$S^1=\left\{e^{2\pi i t}\mid t\in \mathbb{R}/\mathbb{Z}\right\}$$

으로 생각할 수 있다. 이제 이 집합이 2차원 벡터공간 $\mathbb{C}^2$ 위에 다음의 식

$$e^{2\pi i t}\cdot (z_1,z_2)=(e^{4\pi i t}z_1, e^{-2\pi i t}z_2)$$

으로 act한다고 하자. 이 action은 작위적으로 보이지만, 위에서 살펴본 것과 같이 임의의 torus $T$와 임의의 representation $V$가 주어졌다면 $V$의 irreducible decomposition을 생각하고 각각의 irreducible component의 basis $e_i$들을 택하면 모든 torus action은 (적당한 basis의 선택에 의해) 이러한 꼴로 나타나는 것을 안다. 

이를 행렬로 나타내면, 위의 action은 $\GL(2;\mathbb{C})$의 원소(들의 family)

$$\begin{pmatrix}e^{4\pi i t}&0\\0&e^{-2\pi i t}\end{pmatrix}$$

로 나타낼 수 있다. 이 때 이 행렬의 trace $e^{4\pi i t}+e^{-2\pi i t}$가 바로 이 representation의 character이다. 

이 action의 weight space는 $\span(e_1), \span(e_2)$임이 자명하며, 가령 $\span(e_1)$에 해당하는 weight는 다음의 식

$$\rchi_{\lambda_1}(\exp (X))=e^{2\pi i \lambda_1(X)}\qquad\text{for all $X\in \mathfrak{t}$}$$

을 만족하는 linear functional $\lambda_1:\mathfrak{t}\rightarrow \mathbb{C}$으로 주어진다. 이는 당연히 $1\in \mathbb{R}$을 $2$로 보내는 $\lambda_1(t)=2t$에 의해 정의되며 따라서 이 weight space에 해당하는 weight는 (약간의 abuse of notation을 통해) $2$라 할 수 있다. 이 때 $\lambda$가 위의 식을 만족하기 위해서는, $e^{2\pi i}=1$이므로, 반드시 $\lambda(1)\in \mathbb{\mathbb{Z}}$여야 한다. 

더 일반적으로 만일 $r$차원 torus의 action이 주어졌다면 $\mathfrak{t}$는 $\mathbb{R}^r$일 것이며, 이 때 torus $T$를

$$T^r=\left\{(e^{2\pi i t_1}, \ldots e^{2\pi i t_r})\mid t_i\in \mathbb{R}/\mathbb{Z}\right\}$$

으로 쓴다면 그 Lie algebra $\mathfrak{t}\cong \mathbb{R}^r$ 중 weight가 될 수 있는 것은 $\mathbb{Z}^r$에 속하는 원소이며 따라서 weight $\lambda$는 다음의 $r$-tuple

$$\lambda=(n_1, \ldots, n_r)$$

로 주어질 것이다. 명시적으로 이 weight는 임의의 $X=(x_1,\ldots, x_r)\in \mathfrak{t}$가 주어졌을 때 $n_1x_1+\cdots+n_rx_r$을 내놓는 linear functional이다.  

</div>

선형대수학에서의 eigenspace decomposition에서와 마찬가지로, 각각의 weight에 대한 중복도가 $1$일 필요는 없다. 가령 다음의 torus action

$$e^{2\pi i t}\cdot(z_1, z_2)=(e^{4\pi i t}z_1, e^{4\pi i t} z_2)$$

를 생각하면 이번에는 2차원 공간 $\mathbb{C}^2$ 위에서 $T$가 weight $2$를 갖는 것처럼 행동하기 때문이다. 이와 같이 서로 같은 weight $\lambda$들을 갖는 성분들을 한데 모아 이를 $V_\lambda$라 하면, 우리는 *weight space decomposition* $V=\bigoplus V_\lambda$를 얻는다. 지금까지의 논의를 엄밀하게 정의로 적으면 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Torus $T$와 complex $T$-module $V$가 주어졌다 하자. Irreducible character $\rchi_\lambda: T \rightarrow S^1$와 그에 해당하는 linear functional $\lambda:\mathfrak{t}\rightarrow\mathbb{C}$에 대하여, $\lambda$가 $V$의 *weight*이라는 것은 다음 집합

$$V_\lambda=\left\{v\in V\mid t\cdot v=\rchi_\lambda(t)v\text{ for all $t\in T$}\right\}$$

이 nontrivial인 것이다. 이 때, $V_\lambda$를 $\lambda$의 *weight space*라 하며, decomposition

$$V=\bigoplus_\lambda V_\lambda$$

을 $V$의 *weight decomposition*이라 부른다. 

</div>

## Weyl group

Maximal torus의 중요성은 다음 정리에서도 나타난다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Compact connected Lie group $G$에 대해 다음이 성립한다.

1. $G$의 임의의 두 maximal torus는 conjugate이다.
2. $G$의 임의의 원소는 어떠한 maximal torus에 포함되어 있다. 

</div>

따라서 우리는 임의의 compact connected Lie group $G$와 maximal torus $T$에 대하여, 다음의 decomposition

$$G=\bigcup_{g\in G}gTg^{-1}$$

을 얻는다. 이를 *Cartan decomposition*이라 부른다. 

물론 이 decomposition이 완전한 것은 아니다. 가령 이는 disjoint union이 아니므로 어떤 의미에서는 완전한 decomposition이라 보기 힘들다. 이를 더 잘 쓰기 위해 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Compact, connected Lie group $G$와 maximal torus $T$, 그리고 $T$의 normalizer

$$N(T)=\{g\in G\mid gTg^{-1}=T\}$$

에 대하여, group $W=N(T)/T$를 $G$의 *Weyl group<sub>바일 군</sub>*으로 정의한다. 

</div>

