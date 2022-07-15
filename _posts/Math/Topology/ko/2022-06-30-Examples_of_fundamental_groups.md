---

title: "기본군의 예시들"
excerpt: "Fundamental group"

categories: [Math / Topology]
permalink: /ko/math/topology/examples_of_fundamental_groups
header:
    overlay_image: /assets/images/Topology/Examples_of_fundamental_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-06-30
last_modified_at: 2022-06-30
weight: 102
    
---

이제 우리는 특정 공간들의 기본군을 직접 계산해본다. 우선 $\mathbb{R}^n$의 부분집합 중 볼록집합들은 항상 simply connected이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $\mathbb{R}^n$의 부분집합 $S$가 *볼록집합<sub>convex set</sub>*이라는 것은 임의의 $x,y\in S$와 실수 $t\in [0,1]$에 대하여 $tx+(1-t)y$ 또한 $S$의 원소인 것이다.

</div>

직관적으로 이는 $x,y$가 $S$에 속할 때마다, 이들을 잇는 선분 또한 $S$에 속한다는 뜻이다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 볼록집합은 항상 simply connected이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## $S^1$의 fundamental group

자명하지 않은 예시들 중 가장 핵심적인 것은 $S^1$이다. 이를 다루기 위해서는 다음 글에서 사용할 정의를 살짝 끌어다 쓸 필요가 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $X$에 대하여, $p:\tilde{X}\rightarrow X$가 *covering space<sub>피복공간</sub>*이라는 것은 각각의 $x\in X$마다 적당한 열린근방 $U$가 존재하여 $p^{-1}(U)$가 $U$와 homeomorphic한 여러 개의 slice들의 disjoint union으로 표현할 수 있는 것이다.

</div>

다음 명제도 마찬가지로 다음 글에서 중요하게 사용할 명제인데, $S^1$의 fundamental group을 계산하기 위해서는 필요하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Covering space $p:\tilde{X}\rightarrow X$가 주어졌다 하고, $f_0, f_1:Y\rightarrow X$ 사이의 homotopy $(f\_t)\_{0\leq t\leq 1}$가 주어졌다 하자. 만일 $\tilde{f}\_0:Y\rightarrow\tilde{X}$가 $p\circ\tilde{f}\_0=f\_0$을 만족한다면, $p\circ\tilde{f}\_t=f\_t$를 만족하는 homotopy $(\tilde{f}\_t)\_{0\leq t\leq 1}$이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>


<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $\pi_1(S^1)\cong\mathbb{Z}$이며, 이 때 $S^1$을 따라 한 바퀴 도는 loop가 $\pi_1(S^1)$의 generator가 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

이로부터 $S^1$은 $D^2$의 retract가 아니라는 것을 알 수 있다. 즉, $S^1$에 제한하였을 때 항등함수가 되는 연속함수 $r:D^2\rightarrow S^1$은 존재하지 않는다. 만약 그러한 연속함수가 존재한다면, $i:S^1\rightarrow D^2$로부터 유도되는 함수 $i_\ast$는 $\pi\_1(S^1, x_0)\cong\mathbb{Z}$에서 $\pi\_1(D^2, x_0)=0$으로의 injection이 되어 모순이기 때문이다. 

## Fundamental group of product space

위에서 열심히 계산한 $S^1$의 fundamental group이 중요한 예시인 이유는 이를 통해 다양한 위상공간의 fundamental group을 계산할 수 있기 때문이다. 이는 다음의 명제를 통해 이뤄진다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 두 위상공간 $X,Y$가 path-connected라 하자. 그럼 $\pi_1(X\times Y)$는 $\pi_1(X)\times\pi_1(Y)$와 isomorphic하다. 

</div>

예를 들어, torus $T_1$은 $S^1\times S^1$과 같다. 따라서 $\pi_1(S^1\times S^1)$은 위의 명제에 의해 $\mathbb{Z}\times\mathbb{Z}$와 동일하다. 이 때 $\pi_1(T_1)$의 두 generator는 적도를 따라 한 바퀴 감는 고리와, 도넛에 수직인 방향의 단면을 감는 고리로 이루어진다.

![](/assets/images//.png){:width="250px" class="invert" .align-center}

이 때 위의 계산은 특히 $\pi_1(S^1\times S^1)$의 fundamental group이 abelian group이라는 것을 보여주며, 따라서 위의 두 고리를 각각 $\alpha,\beta$라 하면 $[\alpha][\beta]=[\beta][\alpha]$가 성립한다. 이는 두 고리 $\alpha\cdot\beta$와 $\beta\cdot\alpha$ 사이의 homotopy가 존재한다는 의미이다. 

