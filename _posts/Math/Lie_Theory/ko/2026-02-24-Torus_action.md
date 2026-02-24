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

## Weight decomposition

우리의 주장은 $\rho(T)$가 simultaneously diagonalizable이라는 것이다. 이를 위해서는 $\rho(T)$의 각각의 원소들이 diagonalizable인 것을 보이면 충분하다. 이를 위해 임의의 finite-dimensional representation $\rho:G\rightarrow \Aut(V)$을 생각하고 이를 maximal torus $T$로 제한한 representation $\rho\vert_T$을 생각하자. 가장 먼저 확인할 수 있는 것은 $T$가 compact Lie group이라는 사실이다. 따라서 [\[표현론\] §유한군의 표현론, ⁋명제 6](/ko/math/representation_theory/representations_of_finite_groups#prop6)과 [\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)이 모두 성립한다. 

보다 자세하게 이들을 하나하나 써 보면, 우선 $\rho\vert_T$가 unitary representation이라는 사실로부터 우리는 다음의 irreducible decomposition

$$V=\bigoplus_i V_i$$

을 생각할 수 있다. 여기에서 각각의 $V_\lambda$는 irreducible $T$-representation들이다. 한편, $T$가 abelian이므로 임의의 $t\in T$에 대하여, $\rho(t)$은 $T$-action과 모두 commute하고, 따라서 각각의 $V_i$로 제한하였을 때 $\rho(t)$는 $T$-automorphism이다. 이제 [\[표현론\] §유한군의 표현론, ⁋보조정리 8](/ko/math/representation_theory/representations_of_finite_groups#lem8)의 두 번째 결과에 의하여 $\rho(t)$는 상수배

$$\rho(t)(v)=\lambda_i(t)v\qquad \lambda_i(t)\in \mathbb{C}^\times$$

로 주어진다. 그런데 이제 $V_i$ 위에서 $T$가 상수배들로 작용한다면, $V_i$의 임의의 부분공간은 $T$-invariant일 것이며 따라서 $V_i$가 irreducible이기 위해서는 반드시 $\dim V_i=1$이어야만 한다. 

이제 $\dim V_i=1$이므로 $\Aut(V_i)\cong \mathbb{C}^\times$이고, 우리는 위의 $\lambda_i: T\rightarrow \mathbb{C}^\times$가 정확하게 

배를 곱하는 상수배로 작용한다. 

우리는 하여 $T$의 임의의 representation은 1차원이라는 것을 안다. 즉, $T$의 원소들이 



## 





Lie algebra $\mathfrak{g}$의 임의의 원소 $X$를 택한 후, 이 방향으로의 exponential map이 그리는 one-parameter subgroup의 closure가 torus가 된다. 따라서 maximal torus의 존재성은 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)에 의해 자명하다. 그럼 임의의 representation $\rho:G \rightarrow \Aut(V)$와 $t\in T$에 대하여, $\rho(t)$들은 $\Aut(V)$에서 commute한다. 뿐만 아니라, 임의의 