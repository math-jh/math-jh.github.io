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

우리는 따라서 $G$가 *compact* Lie group인 경우를 종종 다루게 된다. 이 경우, locally compact Hausdorff space로서 $G$ 위에는 Haar measure가 존재하며 따라서 $G$의 원소들에 대한 합을 $G$ 전체에 대한 적분으로 바꿔 쓸 수 있다. 물론 이를 위해서는 $\delta_x$ 함수를 잘 정의하고, 함수공간을 적당한 공간으로 일반화하는 작업을 거쳐야 하지만 이러한 작업은 우리의 현재 목적이 아니므로 생략하기로 혼다. 중요한 것은 리 군의 표현론 또한 유한군의 표현론과 같은 방법론을 통해 접근할 수 있다는 것이다. 

한편, 유한차원 representation $G\rightarrow\Aut(V)$가 주어졌다 할 때, 가장 좋은 점은 이들의 image $\rho(g)$들을 (basis의 선택을 통해) 행렬로 생각할 수 있다는 것이다. 따라서 이를 통해 우리는 행렬과 선형사상에 대한 우리의 도구들을 사용하여 이를 탐구할 수 있다. 

선형대수에서 가장 중요한 도구 중 하나는 대각화이다. 따라서 우리는 주어진 Lie group action $\rho:G \rightarrow \Aut(V)$에 대하여, $V$의 basis를 적당히 택하여 $\rho(g)$의 행렬표현을 대각행렬로 만드는 데에 관심이 있다. 만일 $G$가 유한군이었다면, 각각의 $g$에 대해 이러한 basis를 찾아줄 수 있었겠지만 현재는 $G$가 무한하므로 이러한 일을 하기 힘들다. 따라서 우리는 simultaneously diagonalizable인 원소들에 자연스럽게 관심을 갖게 된다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 

</div>