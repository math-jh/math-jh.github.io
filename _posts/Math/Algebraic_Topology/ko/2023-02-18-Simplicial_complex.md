---

title: "심플렉스 복합체"
excerpt: "Simplex의 정의와 성질들"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/simplicial_complex
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Simplicial_complex.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2023-02-18
last_modified_at: 2023-02-18
weight: 1

---

## Introduction

만일 두 위상공간 $X,Y$가 동형이라면, $X$와 $Y$의 compactness, connectedness와 같은 위상적 성질들이 모두 일치해야 한다. 거꾸로 이야기하면, 이러한 아이디어를 바탕으로 우리는 위상적인 성질들을 사용해 위상공간들이 동형인지 아닌지를 밝혀낼 수 있다.

[위상수학](/ko/math/topology/)에서 우리는 다양한 위상적인 성질들을 살펴보았다. [대수적 위상수학](/ko/math/algebraic_topology/)에서 살펴볼 위상적인 불변량들은 이들 사이에 연산이 가능하다는 점에서 특별하다. 더 정확히 이야기하자면, 대수적 위상수학에서 하는 일은 카테고리 $\mathbf{Top}$에서 $\Group$, $\Ab$, $\lmod{R}$ 등의 대수적인 카테고리로 가는 functor $F$를 찾는 것이다. 일반적으로 $F$는 faithful이 아니기 때문에 두 위상공간 $X,Y$에 대해 $F(X)\cong F(Y)$가 성립한다 해도 $X$와 $Y$가 homeomorphic한 것은 아니지만, 이러한 방식으로 정의된 동치관계 또한 충분히 흥미로운 결과를 준다.

## 심플렉스

대수적 위상수학은 크게 호모토피 이론과 호몰로지 이론으로 나눌 수 있는데, 우리는 호몰로지 이론부터 시작한다. 지금 소개할 심플렉스는 호몰로지 이론을 전개할 때 직관적인 이해에 도움을 준다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 자연수 $k$에 대하여, 일반적인 방식으로 배열된 $k+1$개의 점 $v_0,\ldots, v_k\in\mathbb{R}^d$가 주어졌다 하자. 그럼 이들로 만들어지는 *$k$-simplex<sub>$k$-심플렉스, $k$-단체</sub>*는 집합 $\\{v_0,\ldots, v_k\\}$을 포함하는 볼록집합 중 가장 작은 것이다.

</div>

여기서 $k+1$개의 꼭짓점들이 일반적으로 배열되었다는 것은 이들 점들이 $k$차원보다 작은 임의의 초평면에 포함되지 않는 것이다. 바꿔말하면 $k$개의 벡터

$$v_1-v_0,\ldots, v_k-v_0$$

이 linearly independent인 것으로도 이해할 수 있다. 예를 들어 $0$-simplex는 점이고, $1$-simplex는 두 꼭짓점을 잇는 선분, $2$-simplex는 세 점을 잇는 삼각형이며 $3$-simplex는 사면체이다. 특별히 $\mathbb{R}^{n+1}$에서, $n+1$개의 꼭짓점들

$$(1,0,\ldots, 0),\qquad\cdots,\qquad (0,0,\ldots,1)$$

로 만들어진 $n$-simplex를 standard simplex라 부르고, $\Delta^n$으로 적는다. 

일반적으로 simplex들의 꼭짓점이 배열된 순서가 중요하므로, $v_0,\ldots, v_k$으로 만들어진 $k$-simplex를

$$[v_0,\ldots, v_k]$$

처럼 적는다. 

사면체의 한 면이 삼각형이고, 삼각형의 한 변이 선분이듯, 일반적으로 $k$-simplex의 한 <em_ko>면</em_ko>은 $(k-1)$-simplex가 된다. 수학적으로 이는 $k+1$개의 꼭짓점들의 집합에서 하나를 빼고 얻어진 $k$개의 꼭짓점으로 새로운 $(k-1)$-simplex를 얻는 것과 같다. 표기상의 편의를 위해 이렇게 얻어진 새로운 simplex를

$$[v_0,\ldots,\hat{v}_i,\ldots, v_k]=[v_0,\ldots, v_{i-1},v_{i+1},\ldots, v_k]$$

으로 적는다. 

## 심플렉스 복합체

위상공간 $X$ 위에서의 simplex는 standard simplex $\Delta^n$의 적당한 함수에 의한 image로 생각할 수 있다. 물론 모든 함수가 허용된다면 simplex의 모양이 변할 수도 있으므로 함수가 만족해야 할 조건들이 존재한다. 

우리의 목표는 $X$를 simplex들로 쪼개어, 이들의 성질을 통해 $X$를 살펴보는 것이므로 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 위상공간 $X$에 대하여, 이 위에 주어진 *$\Delta$-complex 구조*는 다음과 같이 정의된 함수 $\sigma_\alpha:\Delta^{n(\alpha)}\rightarrow X$들의 모임이다.

1. $\sigma_\alpha$를 $\interior(\Delta^{n(\alpha)})$로 제한한 것이 단사이며, $X$의 임의의 점 $x$에 대해 $x\in \sigma\_\alpha(\interior(\Delta^{n(\alpha)}))$를 만족하는 $\alpha$가 정확하게 하나 존재한다.
2. $\sigma_\alpha$를 $\Delta^{n(\alpha)}$의 한 면으로 제한한 $\sigma\_\alpha\|\_{\Delta^{n(\alpha)-1}}:\Delta^{n(\alpha)-1}\rightarrow X$ 또한 이 함수들의 모임에 속한다.
3. $A\subseteq X$가 $X$에서 열린집합인 것과, 각각의 $\alpha$에 대하여 $\sigma_\alpha^{-1}(A)$가 $\Delta^{n(\alpha)}$에서 열린집합인 것이 동치이다.

</div>

가령 standard simplex $\Delta^2$는 자명하게 $\Delta$-complex 구조를 갖는데, 명시적으로 이 구조를 주는 함수들은

$$\operatorname{id}_{\Delta^2}:\Delta^2\rightarrow\Delta^2$$

와, $1$-simplex $\Delta^1$을 각 변으로 보내는 세 개의 함수 $\sigma^1_1,\sigma^1_2,\sigma^1_3$, 그리고 $0$-simplex $\Delta^0$을 각 꼭짓점으로 보내는 세 개의 함수 $\sigma_1^0,\sigma_2^0,\sigma_3^0$으로 이루어진다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 예를 들어, 2차원 torus $T^2$는 다음의 그림

![Torus](/assets/images/Math/Algebraic_Topology/Simplicial_complex-1.png){:width="700px" class="invert" .align-center}

과 같이 나타날 수 있으며, 이 그림은 동시에 $T^2$에 $\Delta$-complex의 구조를 준다.

</div>

--- 

**참고문헌**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.

---