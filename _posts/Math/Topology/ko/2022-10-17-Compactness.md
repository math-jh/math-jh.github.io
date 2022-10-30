---

title: "컴팩트"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/compactness
header:
    overlay_image: /assets/images/Topology/Compactness.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-10-17
last_modified_at: 2022-10-17
weight: 15

published: false
    
---

이번 글에서 소개할 컴팩트의 개념은 그 동안 보아왔던 개념들에 비하면 그 정의가 인위적으로 느껴질 수 있지만, 수학의 모든 분야에서 중요하게 사용된다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1 (Borel-Lebesgue)**</ins> 위상공간 $X$가 *컴팩트<sub>compact</sub>*라는 것은 $X$의 임의의 open covering $\mathcal{A}$가 주어질 때마다, $\mathcal{A}$에 속한 열린집합 중 유한 개만 택하여 $X$를 덮을 수 있는 것이다.

</div>

예를 들어, 실수의 부분집합 $(0,1)$은 컴팩트 집합이 아니다. 이는 다음의 open covering

$$\mathcal{A}=\{(\epsilon, 1-\epsilon): 0<\epsilon<1/2\}$$

에 대하여,

$$\bigcup\mathcal{A}=(0,1)$$

이지만 $\mathcal{A}$의 원소들 중 유한 개를 택하여 $X$를 덮을 수 없기 때문이다. 결론에 반하여 $(0,1)$을 덮을 수 있는 $\mathcal{A}$의 유한 개의 원소들

$$(\epsilon_1,1-\epsilon_1),\cdots,(\epsilon_n,1-\epsilon_n)$$

이 존재한다 가정하자. $\epsilon_i$들 중 가장 작은 것을 택하여 이를 $\epsilon$이라 하면

$$(\epsilon,1-\epsilon)=\bigcup_{i=1}^n(\epsilon_i,1-\epsilon_i)$$

인데, $0<\epsilon/2<\epsilon$인 것으로부터

$$\frac{\epsilon}{2}\not\in(\epsilon,1-\epsilon)$$

이 되어 $(0,1)\not\subseteq(\epsilon,1-\epsilon)$이기 때문이다. 이와는 반대로 $[0,1]$은 컴팩트 집합이라는 것을 보일 수 있지만, 순수하게 $[0,1]$의 open cover $\mathcal{A}$가 주어졌다 하고 여기에서 항상 유한한 subcover라는 것을 보이는 것은 쉽지 않다. 

컴팩트성을 살펴보아야 할 이유 중 하나는 이것이 연속함수에 의하여 보존되는 성질이라는 것이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 연속함수 $f:X\rightarrow Y$와, $X$의 컴팩트 부분집합 $A$가 주어졌다 하자. 그럼 $f(A)$는 $Y$에서 컴팩트 집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f(A)$의 임의의 open cover $\mathcal{B}$가 주어졌다 하자. 그럼 다음의 집합

$$f^{-1}\mathcal{B}=\{f^{-1}(U):U\in\mathcal{B}\}$$

은 $A$의 open covering이 된다. 따라서 $A$의 컴팩트성에 의해 $f^{-1}\mathcal{B}$의 유한한 subcover가 존재하여 $A$를 덮을 수 있다. 이를 $\mathcal{A}$라 하면, 

$$f\mathcal{A}=\{U\in\mathcal{B}: f^{-1}(U)\in\mathcal{A}\}$$

이 $f(A)$를 덮는 $\mathcal{B}$의 유한한 subcover가 된다.

</details>

이제 우리는 컴팩트 집합의 몇몇 성질들을 살펴본다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 임의의 컴팩트 공간 $X$의 닫힌 부분집합 $A$는 컴팩트이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$를 덮는 임의의 open covering $\mathcal{A}$가 주어졌다 하자. 그럼 

$$\mathcal{A}'=\mathcal{A}\cup\{X\setminus A\}$$

는 $X$의 open covering이며, 따라서 $X$의 컴팩트성에 의해 $\mathcal{A}'$의 유한한 부분집합 $\mathcal{A}''$가 존재하여 

$$X=\bigcup_{B\in\mathcal{A}''}B$$

가 성립한다. 이제 $\mathcal{A}''\cap\mathcal{A}$는 $A$를 덮는 $\mathcal{A}$의 유한한 subcover가 된다.

</details>

<div class="proposition" markdown="1">

<ins id="crl4">**따름정리 4**</ins> 연속함수 $f:X\rightarrow Y$가 전단사이고, $X$가 컴팩트, $Y$가 Hausdorff라 하자. 그럼 $f$는 homeomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

위상공간 $X$를 열린집합 대신 닫힌집합들로 표현할 수 있듯, 컴팩트성 또한 닫힌집합의 언어로 표현할 수 있다. $X$의 부분집합들의 모임 $\mathcal{C}$가 *finite intersection property*를 갖는다는 것은 $\mathcal{C}$의 임의의 유한한 교집합이 항상 공집합이 아닌 것이다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 위상공간 $X$가 컴팩트인 것은 finite intersection property를 만족하는 임의의 collection $\mathcal{C}$에 대하여 $\bigcap_{C\in\mathcal{C}}C$ 또한 공집합이 아닌 것과 동치이다.

</div>

## 하이네-보렐 정리

이제 우리는 위에서 살펴본 집합 $[0,1]$이 실제로 $\mathbb{R}$ 컴팩트 부분집합이 된다는 것을 보인다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 임의의 실수 $a\leq b$에 대하여, 구간 $[a,b]$는 항상 컴팩트 집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

뿐만 아니라, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Heine-Borel)**</ins> $\mathbb{R}^n$의 부분공간이 컴팩트인 것은 이 집합이 닫힌 집합이고, standard metric $d$에 대하여 유계인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

우리는 미적분학에서부터 닫혀있고, 유계인 집합 위에서 정의된 연속함수는 항상 최댓값과 최솟값을 갖는다는 것을 알고 있다. 그러나 이 성질은 사실 컴팩트성의 성질이다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 컴팩트 공간 $X$에 대하여, 연속함수 $f:X\rightarrow Y$는 최댓값과 최솟값을 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>