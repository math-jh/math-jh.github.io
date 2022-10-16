---

title: "경로연결공간"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/path_connectedness
header:
    overlay_image: /assets/images/Topology/Path_connectedness.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-10-16
last_modified_at: 2022-10-16
weight: 14

published: false
    
---

앞선 글에서 정의한 connected space의 정의는 그렇게까지 직관적인 것은 아니다. 아마도 더 직관적인 정의는 다음의 정의가 될 것이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 *path-connected<sub>경로연결</sub>*이라는 것은 임의의 $x,y\in X$마다 적당한 path $\gamma:[0,1]\rightarrow X$가 존재하여 $\gamma(0)=x$이고 $\gamma(1)=y$이도록 할 수 있는 것이다.

</div>

물론 $\gamma$는 연속이어야 한다. 또, 우리는 편의상 $\gamma$의 정의역을 $[0,1]$로 제한했지만 사실은 임의의 폐구간으로 정의할 수도 있었다. 임의의 폐구간 $[a,b]$에서 $[0,1]$로 가는 homeomorphism이 존재하기 때문이다.

[§연결공간](/ko/math/topology/connectedness)의 흐름을 따라 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 위상공간 $X$와 한 점 $x\in X$에 대하여, $x$를 포함하는 $X$의 path-connected subspace 가운데 가장 큰 것을 $x$를 포함하는 *path component*라 정의한다.

</div>

이를 위해서는 다음 보조정리를 보여야 한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 임의의 점 $x\in X$와 $x$를 포함하는 path-connected subspace들의 모임 $\\{A\_i\\}\_{i\in I}$에 대하여, $A=\bigcup A\_i$는 $X$의 path-connected subspace이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 두 점 $y_1,y_2\in A$가 주어졌다 하자. 그럼 적당한 $i,j\in I$에 대하여 $y_1\in A_i,y_2\in A_j$이다. 이제 $A_i,A_j$ 각각이 path-connected이고, 이들은 $x$를 포함하므로 적당한 path $\gamma_1:[0,1]\rightarrow A_i$, $\gamma_2:[1,2]\rightarrow A_j$가 존재하여

$$\gamma_1(0)=y_1,\quad\gamma_1(1)=x,\quad\gamma_2(1)=x,\quad\gamma_2(2)=y_2$$

이도록 할 수 있다. 이제 [§부분공간, 명제 8](/ko/math/topology/subspace_topology#pp8)을 적용하면 새로운 path $\gamma:[0,2]\rightarrow A$를 얻으며, $\gamma$가 $y_1,y_2$를 잇는 path가 된다. 

</details>

Path-connected space와 connected space 사이에는 다음과 같은 관계가 존재한다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 임의의 path-connected space는 connected이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

그러나 [명제 4](#pp4)의 역은 성립하지 않는다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (위상수학자의 사인 곡선)**</ins> 

</div>

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 위상공간 $X$가 *locally path-connected*라는 것은 임의의 점 $x\in X$와 $x$의 neighborhood $U$가 주어질 때마다, $U$에 포함되는 $x$의 path-connected neighborhood가 존재하는 것이다. 

</div>

이제 [§연결공간, 명제 8](/ko/math/topology/connectedness#pp8)과 마찬가지로 다음 명제를 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 위상공간 $X$가 locally path-connected인 것은 임의의 열린집합 $U$에 대하여, $U$의 path component들이 $X$의 부분집합으로서도 열린집합인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

[명제 4](#pp4)의 결과에 의하여, 위상공간 $X$의 path component는 반드시 $X$의 어떤 component에 포함되어야 함이 자명하다. 만일 $X$가 locally path-connected라면 임의의 path component는 그 자체로 component가 된다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> Locally path-connected space $X$에 대하여, $X$의 component와 path-component는 동일하다.

</div>
