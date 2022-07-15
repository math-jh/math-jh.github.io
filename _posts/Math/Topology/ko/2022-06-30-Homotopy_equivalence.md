---

title: "Homotopy equivalence"
excerpt: "Fundamental group"

categories: [Math / Topology]
permalink: /ko/math/topology/Homotopy_equivalence
header:
    overlay_image: /assets/images/Topology/Homotopy_equivalence.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-06-30
last_modified_at: 2022-06-30
weight: 101
    
---

구멍이 뚫린 평면 $X=\mathbb{R}^2\setminus\\{0\\}$을 생각하자. 이 평면은 path connected이므로 fundamental group $\pi\_1(X)$가 잘 정의된다. 이 때 $\pi\_1(X)\neq0$임이, 즉 $X$가 simply connected가 아님이 자명하다. 원점 주변을 도는 임의의 고리는 constant loop로 변형시킬 수 없기 때문이다. 비슷하게, 속이 빈 원기둥이 주어졌다면 이 원기둥의 주변을 따라 도는 고리가 constant loop로 변형될 수 없으므로, 이 원기둥의 fundamental group 역시 0이 아니며, 사실 이 두 공간은 모두 $S^1$과 같은 fundamental group을 갖는다.

이번 글에서는 본격적으로 여러 fundamental group들을 계산하기 전에, 이들이 같은 fundamental group을 갖는 이유를 자세히 살펴본다.

## Retraction과 deformation retraction

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$와 부분공간 $i:A\hookrightarrow X$에 대하여, $X$에서 $A$로의 *retraction<sub>수축</sub>*은 $r\circ i=\operatorname{id}_A$를 만족하는 연속함수를 의미한다. ([집합론, §함수(2), 정의 2](/ko/math/set_theory/functions_2#df2)) 이 때 $A$가 $X$의 *retract*라 한다.

</div>

임의의 점 $x\_0\in A$을 고정하자. 만일 $X$에서 $A$로의 retraction $r:X\rightarrow A$가 존재한다면 

$$r_\ast\circ i_\ast=(\operatorname{id}_A)_\ast=\operatorname{id}_{\pi_1(A,x_0)}$$

이므로 $i_\ast$는 injective이다. ([집합론, §함수(2), 명제 1](/ko/math/set_theory/functions_2#pp1)) 

우리는 앞서 homeomorphism $f:X\rightarrow Y$에 대하여 유도되는 함수 $f\_\ast:\pi\_1(X,x\_0)\rightarrow\pi\_1(Y, y\_0)$이 isomorphism이 된다는 것을 보았고, 위의 간단한 논증은 $i:A\rightarrow X$가 retraction $r:X\rightarrow A$의 section이라면 $i\_\ast$가 injection임을 보여준다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 위상공간 $X$와 부분공간 $A$가 주어졌다 하자. 이 때, $A$가 $X$의 *deformation retract<sub>분해수축</sub>*라는 것은 $\operatorname{id}_X$에서 retraction $r:X\rightarrow A$로의 homotopy가 존재하는 것이다. 

</div>

$i:A\hookrightarrow X$가 $X$의 deformation retract라 하자. 즉, retraction $r_1:X\rightarrow A$와, $r_0=\operatorname{id}_X$ 사이의 homotopy $(r\_t)\_{0\leq t\leq 1}$이 존재한다. 그럼 임의의 $\sigma:I\rightarrow X$에 대하여 $r_t\circ\sigma$를 통해 $\sigma$와 $r_1\circ\sigma:I\rightarrow A$ 사이의 homotopy를 줄 수 있으므로 $[\sigma]$가 $\pi\_1(A,x\_0)$에도 속하게 된다. 지금까지의 논의를 정리하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 위상공간 $X$와 부분공간 $i:A\hookrightarrow X$가 주어졌다 하자.

1. 만일 $A$가 $X$의 retract라면, $i\_\ast:\pi\_1(A,x\_0)\rightarrow\pi\_1(X,x\_0)$이 injective이다.
2. 만일 $A$가 $X$의 deformation retract라면, $i\_\ast$는 isomorphism이다.

</div>

따라서 도입부에서 예시로 들었던 $\mathbb{R}^2\setminus\\{0\\}$과 원기둥의 경우, 둘 모두 $S^1$로 deformation retract하기 때문에 같은 fundamental group을 갖는다고 할 수 있다. 그러나 이들 중 어느 하나가 다른 하나의 deformation retract인 것은 아니다. 

## Homotopy equivalence

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 두 위상공간 $X,Y$와 연속함수 $f:X\rightarrow Y$, $g:Y\rightarrow X$에 대하여 $g\circ f$가 $\operatorname{id}_X$와, $f\circ g$가 $\operatorname{id}_Y$와 각각 homotopic하다면 이들을 *homotopy equivalence*라 부르고, 각각이 서로의 *homotopy inverse*라 부른다. 두 공간 사이에 homotopy equivalence가 존재한다면 이들이 *homotopy equivalent*하다, 혹은 같은 *homotopy type*을 갖는다고 한다. 

</div>

우리의 남은 목표는 homotopy equivalence에 의해 유도되는 fundamental group들 사이의 homomorphism이 isomorphism이 된다는 것인데, 이를 위해서는 간단한 보조정리가 필요하다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 두 위상공간 $X,Y$의 두 연속함수 $f_0,f_1:X\rightarrow Y$와 이들 사이의 homotopy $(f_t)$가 주어졌다 하자. 임의의 점 $x_0\in X$에 대하여, 곡선 $h:I\rightarrow Y$를 $t\mapsto f_t(x_0)$으로 정의하자. 그럼 다음의 diagram이 commute한다.

![](/assets/images//.png){:width="250px" class="invert" .align-center}

</div>

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 만일 $f:X\rightarrow Y$가 homotopy equivalence라면, 모든 $x_0\in X$에 대하여 induced map $f\_\ast:\pi\_1(X,x\_0)\rightarrow\pi\_1(Y, f(x\_0))$이 isomorphism이 된다.

</div>