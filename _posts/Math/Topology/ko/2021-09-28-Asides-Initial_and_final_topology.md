---

title: "Initial and final topology<sup>†</sup>"
excerpt: "Initial topology와 final topology"

lang: ko

categories: [Math / Topology]
permalink: /ko/math/topology/initial_and_final_topology
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-28
last_modified_at: 2022-04-07
weight: 12
    
---

우리는 앞서 부분공간, 곱공간, 몫공간을 생각했었는데, 이들은 모두 initial topology와 final topology라 불리는 위상들의 특수한 경우이다.  

## Initial topology

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $X$, 그리고 위상공간들의 family $(Y\_i,\mathcal{T}\_i)\_{i\in I}$들이 주어졌다 하고, 각각의 $i$마다 함수 $f_i:X\rightarrow Y_i$들이 주어졌다 하자. 함수 $f_i$들을 모두 연속으로 만드는 집합 $X$ 위의 위상 중 가장 약한 것을 *$f_i$들에 의해 정의된 initial topology*라 부른다. 

</div>

집합 $X$ 위에 정의된 위상들의 family $(\mathcal{T}_i')$에 대하여, $\bigcap\mathcal{T}_i'$가 $X$ 위의 위상이 된다는 것을 쉽게 확인할 수 있다. 또, discrete topology를 정의역으로 삼는 임의의 함수는 항상 연속이므로 initial topology가 항상 존재한다는 것은 자명하다. 이런 종류의 논증이 항상 그렇듯이, 이는 initial topology의 존재성을 보여주는 데에는 흠잡을 곳 없는 논증이 되지만 initial topology가 어떻게 생겼는지를 살펴보는데는 별 도움이 되지 않는다. 때문에 조금 더 구체적으로 상황을 살펴볼 필요가 있다.

함수 $f_i$가 연속이기 위해서는 $Y_i$의 임의의 열린집합 $U_i$에 대하여 $f_i^{-1}(U_i)$가 $X$에서 열린집합이어야 하므로, 우리가 정의할 initial topology는 $f_i^{-1}(U_i)$꼴의 원소들을 모두 가지고 있어야 한다. 한편, 이들 원소들을 포함하는 위상공간은 이들의 유한한 교집합과 임의의 합집합도 포함해야 한다. 따라서 다음의 명제를 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> [정의 1](#df1)의 initial topology는 정확하게 다음의 집합

$$\mathcal{S}=\{f_i^{-1}(U_i): \text{$U_i$ open in $Y_i$}\}$$

을 subbasis로 하여 생성된 위상과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Initial topology를 $\mathcal{T}\_\mathrm{ini}$으로 적고, $\mathcal{S}$를 subbasis로 하여 생성된 위상을 $\mathcal{T}$로 적자. $\mathcal{T}$는 정의에 의해 $f_i$들을 모두 연속으로 만들기 때문에, $\mathcal{T}\_\mathrm{ini}$는 $\mathcal{T}$보다 약한 위상이다. 따라서 $\mathcal{T}$가 $\mathcal{T}\_\mathrm{ini}$보다 약한 위상이라는 것만 보이면 충분한데, 이는 $\mathcal{T}$가 $\mathcal{S}$를 포함하는 위상 중 가장 약한 위상이기 때문에 자명하다.

</details>

Initial topology는 다음과 같은 성질을 갖는다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> [정의 1](#df1)의 상황에서, 추가로 위상공간 $Z$와 $g:Z\rightarrow X$가 주어졌다 하자. 그럼 $g$가 연속인 것은 각각의 $f_i\circ g$가 연속인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $g$가 연속이라면 $f_i\circ g$는 연속함수들의 합성이므로 자명하게 연속이다. 따라서 반대방향만 보이자.

각각의 함수 $f_i\circ g$가 연속이라 하자. $X$의 임의의 열린 진부분집합 $U$에 대하여, [명제 2](#pp2)에 의해 

$$U=\bigcap_{j=1}^n f_j^{-1}(U_j)$$

가 성립하도록 하는 $U_j$들이 존재한다. 따라서

$$g^{-1}(U)=g^{-1}\left(\bigcap f_j^{-1}(U_j)\right)=\bigcap_{j=1}^n(f_j\circ g)^{-1}(U_j)$$

이고 가정에 의해 $(f_j\circ g)^{-1}(U_j)$는 열린집합이므로 $g^{-1}(U)$ 또한 열린집합이어야 한다. 즉, $g$는 연속이다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 집합 $X$, 위상공간 $Y$와 함수 $f:X\rightarrow Y$가 주어졌다 하자. 그럼 $f$에 의해 정의되는 initial topology는 정확히 $Y$의 열린집합들의 preimage를 모아둔 것과 같다. 특히 만일 $X\subset Y$이고 $X\rightarrow Y$가 canonical inclusion이었다면 이렇게 만들어지는 initial topology는 subspace topology와 동일하다. 

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 위상공간들의 family $(Y\_i,\mathcal{T}\_i)\_{i\in I}$들이 주어졌다 하고, product set $X=\prod Y_i$를 생각하자. 그럼 canonical projection들 $\operatorname{pr}\_i:X\rightarrow Y\_i$들에 대한 initial topology는 정확히 $X$ 위에 정의된 product topology와 동일하게 된다. 

</div>

## Final topology

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 집합 $X$와, 위상공간들의 family $(Y\_i,\mathcal{T}\_i)\_{i\in I}$들이 주어졌다 하고, 각각의 $i$마다 함수 $f_i:Y_i\rightarrow X$가 주어졌다 하자. $f_i$들이 모두 연속이도록 하는 $X$ 위의 위상 중 가장 강한 것을 $f_i$들에 의해 만들어지는 *final topology*라 부른다. 

</div>

$X$에 trivial topology가 주어졌다 하면, $X$로의 임의의 함수는 항상 연속이다. 하지만 일반적으로 위상의 합집합이 위상이 되지는 않기 때문에, initial topology와는 다르게 존재성 증명이 다음 명제에 강하게 의존하게 된다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> [정의 6](#df6)의 위상은 다음의 집합

$$\mathcal{T}_\mathrm{fin}=\{U\subset X:f^{-1}_i(U)\text{ is open in $Y_i$ for all $i$}\}$$

으로 정의된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 위상 $\mathcal{T}\_\mathrm{fin}$가 실제로 위상이 된다는 것은 쉽게 확인할 수 있다. 따라서 $\mathcal{T}\_\mathrm{fin}$가 [정의 6](#df6)의 조건을 모두 만족한다는 것만 보이면 충분하다. 

우선, 임의의 $U\in\mathcal{T}\_\mathrm{fin}$와, 임의의 $i$에 대하여 $f_i^{-1}(U)$가 $Y_i$에서 open인 것은 $\mathcal{T}\_\mathrm{fin}$의 정의로부터 명확하다. 한편, $X$ 위에 주어진 조건을 만족하는 또 다른 topology $\mathcal{T}$가 주어졌다 하자. 그럼 임의의 $U\in\mathcal{T}$에 대하여, $f^{-1}_i(U)$가 $Y_i$에서 연속이어야 한다. 따라서, $\mathcal{T}\_\mathrm{fin}$의 정의에 의해 $U\in\mathcal{T}\_\mathrm{fin}$이고 따라서 $\mathcal{T}\_\mathrm{fin}$가 $\mathcal{T}$보다 강하다.

</details>

역시 마찬가지로 final topology 또한 initial topology와 비슷한 다음의 성질을 만족한다. 증명 또한 크게 다를 것이 없고, 사실은 [앞선 글](/ko/math/topology/quotient_topology)에서도 비슷한 증명을 하였으니 다음 명제의 증명은 생략한다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> [정의 6](#df6)의 상황에서, 추가로 위상공간 $Z$와 $g:X\rightarrow Z$가 주어졌다 하자. 그럼 $g$가 연속인 것은 각각의 $g\circ f_i$가 연속인 것과 동치이다. 

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 위상공간 $X$와 $X$ 위의 equivalence relation $R$이 주어졌다 하고, $Y=X/R$, 그리고 $p:X\rightarrow Y$가 canonical이라 하자. 그럼 $Y$ 위에 정의된 quotient topology는 정확히 $p$에 의해 정의되는 final topology와 동일하다. 

</div>

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
