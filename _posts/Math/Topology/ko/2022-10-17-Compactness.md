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

이 되어 $(0,1)\not\subseteq(\epsilon,1-\epsilon)$이기 때문이다. 이와는 반대로 $[0,1]$은 컴팩트 집합이라는 것을 보일 수 있지만, 이는 그렇게 만만한 작업은 아니다. 

임의의 유한집합은 항상 컴팩트 집합이다. 그러나 위에서 살펴본 것과 같이, 어떤 집합이 컴팩트임은 집합의 크기와는 별 관련이 없다. 

따라서 우리는 우선 컴팩트 집합의 성질들을 먼저 탐구한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 공간 $X$가 컴팩트인 것은 $X$ 위에 정의된 임의의 ultrafilter가 수렴하는 것과 동치이다.

</div>