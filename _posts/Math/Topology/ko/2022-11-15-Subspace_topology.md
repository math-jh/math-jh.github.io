---

title: "부분공간"
excerpt: "부분공간의 성질들"

categories: [Math / Topology]
permalink: /ko/math/topology/subspace
header:
    overlay_image: /assets/images/Topology/Subspace.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-15
last_modified_at: 2022-11-15
weight: 7

---

대수적인 구조를 다룰 때와 마찬가지로, 집합 $X$ 위에 위상구조를 준 후에는 이 구조가 부분집합 $A\subseteq X$에는 어떠한 방식으로 제한되는지를 살펴보는 것이 자연스럽다. 가장 먼저 드는 생각은 $X$의 열린집합들 가운데, $A$에 포함된 열린집합들만 추려 이들을 위상공간 $A$의 열린집합들로 정의하는 것이다. 그러나 이 시도는 실패할 수밖에 없는데, $A$가 $X$에서 열린집합이 아니라면, 전체집합 $A$부터가 이 모임에 속하지 않기 때문이다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $(X,\mathcal{T})$와, $X$의 부분집합 $A$가 주어졌다 하자. 이 때, $\iota:A\hookrightarrow X$에 의해 $A$ 위에 정의되는 initial topology를 *$A$ 위에 정의된 부분위상<sub>subspace topology</sub>*이라 부른다.

</div>

$X$의 임의의 열린집합 $U$에 대하여, $\iota^{-1}(U)=U\cap A$이고, 임의의 열린집합들의 family $(U\_i)\_{i\in I}$에 대해

$$\iota^{-1}\left(\bigcup_{i\in I} U_i\right)=\left(\bigcup_{i\in I} U_i\right)\cap A=\bigcup_{i\in I} (U_i\cap A)=\bigcup_{i\in I} \iota^{-1}(U)$$

그리고 열린집합들의 유한한 family $(U\_i)\_{i\in I}$에 대하여

$$\iota^{-1}\left(\bigcap_{i\in I} U_i\right)=\left(\bigcap_{i\in I} U_i\right)\cap A=\bigcap_{i\in I} (U_i\cap A)=\bigcap_{i\in I} \iota^{-1}(U)$$

이 성립하므로 [§Initial topology와 final topology, 명제 2](/ko/math/topology/initial_and_final_topology#pp2)에 의하여 부분위상 $\mathcal{T}_A$는 다음의 식

$$\mathcal{T}_A=\{U\cap A: U\in\mathcal{T}\}$$

으로 주어진다는 것을 알 수 있다. **[Mun]**과 같은 책에서는 아예 이를 부분공간의 정의로 삼기도 한다. 이로부터 만약 $A\subseteq B\subseteq X$라면, $A$를 $X$의 부분공간으로 생각하든, 혹은 부분위상이 주어진 $B\subseteq X$의 부분공간으로 생각하든 동일한 공간이 된다는 것을 알 수 있다.

부분공간을 다룰 때 주의해야 하는 것은 어떤 집합이 $\mathcal{T}_A$에서 열린집합이라 하더라도 $\mathcal{T}$에서는 열린집합이 아닐 수 있다는 것이다.

![open_in_subspace_but_not_in_whole](/assets/images/Topology/Constructing_topologies-1.png){:width="250px"  class="invert" .align-center}

이러한 상황은 $A$가 열린집합이었다면 쉽게 해결된다.

<div class="proposition" markdown="1">

<ins id="lem2" markdown="1">**보조정리 2**</ins> 위상공간 $X$의 부분공간 $A$에 대하여, $A$의 모든 열린집합이 $X$에서도 열린집합일 필요충분조건은 $A$가 $X$의 열린집합인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$는 $A$에서 열린집합이므로 한쪽 방향은 자명하다.

반대 방향의 경우, $A$의 임의의 열린집합을 택하면 이를 $U\cap A$로 쓸 수 있도록 하는 $X$의 열린집합 $U$가 존재하는데, $A$ 또한 열린집합이므로 $U\cap A$도 열린집합이 된다.

</details>

어렵지 않게 부분공간 $A$에서의 닫힌집합은 정확하게 $X$의 닫힌집합 $C$에 대하여, $A\cap C$의 꼴로 나타나는 집합들임을 알 수 있다. 닫힌집합의 경우에도 위의 예시와 같은 상황이 생길 수 있는데, 이를 해결하는 방법 또한 마찬가지로 간단하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위상공간 $X$의 부분공간 $A$에 대하여, $A$의 모든 닫힌집합이 $X$에서도 닫힌집합일 필요충분조건은 $A$가 $X$의 닫힌집합인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$는 $A$에서 닫힌집합이므로 한쪽 방향은 자명하다.

반대 방향의 경우, $A$의 임의의 닫힌집합을 택하면 이를 $U\cap A$로 쓸 수 있도록 하는 $X$의 닫힌집합 $U$가 존재하는데, $A$ 또한 닫힌집합이므로 $U\cap A$도 닫힌집합이 된다.

</details>

우리는 지금까지 모든 위상적 성질을 근방이라는 개념을 통해 정의해왔었는데, 이 또한 위의 보조정리들과 마찬가지로 올바르게 수정해줄 수 있다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> 위상공간 $X$의 부분공간 $A$와 임의의 $x\in A$에 대하여, 모든 $A$에서의 $x$의 근방이 $X$에서도 $x$의 근방일 필요충분조건은 $A$가 $X$에서 $x$의 근방인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$는 $A$에서 $x$의 근방이므로 한쪽 방향은 자명하다.

반대 방향의 경우, $x$의 $A$에서의 임의의 근방 $U$을 택하자. 그럼 $U$에 포함되는 $x$의 ($A$에서의) 열린근방 $U'$가 존재한다. 한편 $A$가 $X$에서 $x$의 근방이라면, $A$에 포함되는 ($X$에서의) $x$의 열린근방 $V$가 존재한다. 이제 $U'\cap V$는 공집합이 아닌 부분집합이고, $U'\cap V\subseteq V$이고 $U'\cap V$는 $X$에서 $x$의 열린근방이므로 $V$는 $X$에서의 $x$의 근방이다.

</details>

이 보조정리들을 통하여 지금까지 살펴본 개념들을 부분공간으로 제한할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 위상공간 $X$와 부분집합들 $A\subseteq B\subseteq X$를 생각하자. 그럼 $B$에 대한 $A$의 closure $\operatorname{cl}_BA$는 

$$\operatorname{cl}_BA=B\cap\operatorname{cl}_XA$$

와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x\in B$에 대하여, $x$의 $B$에서의 근방은 항상 $x$의 $X$에서의 적당한 근방 $V$에 대하여 $V\cap B$의 형태로 쓰여진다. 이제 $V\cap A=(V\cap B)\cap A$와 [§집합의 내부, 폐포, 경계, 명제 6](/ko/math/topology/other_concepts#pp6)을 사용하면 원하는 결과를 얻는다.

</details>