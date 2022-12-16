---

title: "위상공간의 기저"
excerpt: "위상공간의 기저와 부분기저, 국소기저"

categories: [Math / Topology]
permalink: /ko/math/topology/topological_basis
header:
    overlay_image: /assets/images/Topology/Topological_structures.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-08
last_modified_at: 2022-11-08
weight: 2

---

## 위상공간의 기저와 부분기저

위상공간을 표현하는 가장 확실한 방법은 열린집합을 모두 나열하여 위상구조 $\mathcal{T}$를 주는 것이지만, 이를 위해서 $\mathcal{T}$ 전체가 필요하지는 않다. 가령, 어떠한 열린집합 $U=\bigcup U_i$이고, 모든 $i$에 대해 $U\neq U_i$이며 $U_i\in\mathcal{T}$임이 알려져 있다면 $U\in\mathcal{T}$라는 정보는 불필요하게 중복되는 정보라 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $(X,\mathcal{T})$에 대하여, $\mathcal{T}$의 부분집합 $\mathcal{B}$가 $\mathcal{T}$의 *basis<sub>기저</sub>*라는 것은 임의의 $U\in\mathcal{T}$에 대하여, $U=\bigcup\_{i\in I} B\_i$를 만족하는 $\mathcal{B}$의 원소들의 family $(B\_i)\_{i\in I}$가 존재하는 것이다.

</div>

특별히 $X\in\mathcal{T}$이므로 $\mathcal{B}$는 $X$의 covering이기도 하다. ([집합론, §집합의 합, 정의 1](/ko/math/set_theory/sum_of_sets#df1)) 정의에 의해 $\mathcal{B}$의 원소들은 모두 열린집합들이니, 이를 $\mathcal{B}$가 $X$의 *open covering<sub>열린덮개</sub>*이라고 표현하면 적절할 것이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위상공간 $(X,\mathcal{T})$에 대하여, $\mathcal{B}$가 $\mathcal{T}$의 basis인 것은 세 가지 조건

1. 각각의 $x\in X$에 대하여, 적어도 하나의 $B\in \mathcal{B}$가 존재하여 $x\in B$이고,
2. 만일 $x$를 포함하는 $\mathcal{B}$의 두 원소 $B\_1$, $B\_2$가 존재한다면, 또 다른 $B\_3\in\mathcal{B}$가 존재하여 $x\in B\_3$이고 $B\_3\subseteq B\_1\cap B\_2$를 만족하고,
3. 각각의 $U\in\mathcal{T}$와 $x\in U$에 대하여, $x\in B\subseteq U$를 만족하는 $B\in\mathcal{B}$가 존재한다.

을 만족하는 것과 동치이다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathcal{B}$가 $\mathcal{T}$의 basis라 가정하자. 그럼 $\mathcal{B}$는 $X$의 open covering이므로, 1번 조건이 자명하게 성립된다. 

한편, $B\_1$, $B\_2$가 2번 조건과 같이 주어졌다면, $B\_1\cap B\_2$도 열린집합이므로 $B\_1\cap B\_2=\bigcup\_{i\in I} B\_i$를 만족하는 $\mathcal{B}$의 원소들의 family $(B\_i)\_{i\in I}$가 존재한다. 이 때, $(B\_i)\_{i\in I}$는 $B\_1\cap B\_2$의 open covering이므로, 1번 조건과 마찬가지로 2번 조건도 자명하게 성립된다. 여기에서 $B\_1\cap B\_2$를 임의의 열린집합 $U$로 바꾸면 3번을 얻는다.

거꾸로 세 개의 조건이 만족된다고 가정하고, 임의의 열린집합 $U$를 택하자. 그럼 $x\in U$에 대해, 3번 조건에 의해 $x\in B\_x\subseteq U$를 만족하는 $B\_x\in\mathcal{B}$가 존재한다. 이제 $U=\bigcup\_{x\in U} B\_x$이므로, 증명 끝.  

</details>

위의 명제로부터 다음과 같은 질문이 자연스럽게 따라온다.

> 임의의 <em_ko>집합</em_ko> $X$에 앞선 조건들을 만족하는 $\mathcal{P}(X)$의 부분집합 $\mathcal{B}$가 주어졌다 하자. 그럼 $X$ 위에 위상 $\mathcal{T}$를 부여하여, $(X,\mathcal{T})$를 basis $\mathcal{B}$를 갖는 위상공간으로 생각할 수 있는가?

이 질문에 대한 답은 긍정적이며, **[Mun]**에서는 이를 직접 증명했지만 우리는 local basis를 정의한 후 더 간단한 방식으로 증명하기로 한다.

한편 [정의 1](#df1)을 더 다듬어서 다음과 같이 *subbasis*를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $(X,\mathcal{T})$의 *subbasis<sub>부분기저</sub>* $\mathcal{S}$는 임의의 $U\in\mathcal{T}$에 대하여, $S\subseteq U$인 $S\in\mathcal{S}$가 존재하는 $X$의 open covering을 의미한다.

</div>

$\mathcal{S}$의 원소들의 유한한 교집합들을 모아 새로운 모임 $\mathcal{B}$를 만들 수 있다. 이 모임이 basis인지를 체크하는 데 필요한 것은 오직 2번 조건 뿐인데, 어차피 $\mathcal{B}$의 원소들은 $\mathcal{S}$의 유한한 교집합으로 얻어지고, 따라서 $B\_1\cap B\_2$를 해봐야 $\mathcal{S}$의 원소들의 유한한 교집합이므로 $\mathcal{B}$가 basis가 된다. 

## 위상공간의 국소기저

[§열린집합, 명제 6](/ko/math/topology/open_sets#pp6)은 위상공간 $X$와 한 점 $x$에 대하여, $x$를 중심으로 하는 neighborhood filter $\mathcal{N}(x)$를 묘사할 수 있다면 $X$의 위상구조를 완전히 복원할 수 있다는 것을 보여준다. 한편 $\mathcal{N}(x)$는 [§열린집합, 명제 6](/ko/math/topology/open_sets#pp6)의 조건들, 특히 첫째 조건을 만족하므로 이 집합을 묘사하는 데에는 $\mathcal{N}(x)$가 모두 필요하지는 않다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 위상공간 $X$와 부분집합 $A$에 대하여, $A$에서의 *local basis<sub>국소기저</sub>*는 $(\mathcal{N}(A),\subseteq)$의 coinitial subset을 의미한다. ([집합론, §순서집합의 원소들](/ko/math/set_theory/elements_in_ordered_set))

</div>

[§열린집합, 정의 4](/ko/math/topology/open_sets#df4)와 마찬가지로, $A$가 한점집합 $\\{x\\}$일 경우, $A$의 local basis를 점 $x$에서의 local basis라 부른다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 위상공간 $(X,\mathcal{T})$가 주어졌다 하자. 그럼 $\mathcal{T}$의 부분집합 $\mathcal{B}$가 $X$의 basis인 것은 각각의 $x\in X$에 대하여 <phrase>$x$를 포함하는 $\mathcal{B}$의 원소들</phrase>이 $x$에서의 local basis를 정의하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편의상 $\mathcal{B}$의 원소들 중 $x$를 포함하는 것들을 모두 모아 이들을 $\mathcal{B}(x)$라 적자. 

우선 $\mathcal{B}$가 $X$의 basis라 하고, 임의의 점 $x\in X$와 근방 $V$를 택하자. 그럼 $x\in U\subseteq V$이도록 하는 열린집합 $U$가 존재한다. 이제 $\mathcal{B}$는 $X$의 basis이므로, $U=\bigcup U_i$이도록 하는 $U_i\in\mathcal{B}$들이 존재한다. $x\in U$이므로, 어떤 $i$에 대해 $x\in U_i$이고 따라서 $U_i\in\mathcal{B}(x)$이다. 

거꾸로 주어진 조건을 만족하는 $\mathcal{B}$가 주어졌다 하고, 임의의 열린집합 $U$가 주어졌다 하자. 그럼 임의의 $x\in U$에 대하여 $U\in\mathcal{N}(x)$이므로, 주어진 조건으로부터 적당한 $V(x)\in\mathcal{B}(x)$가 존재하여 $x\in V(x)\subseteq U$이도록 할 수 있다. 이제 $U=\bigcup V(x)$이므로 원하는 결과를 얻는다.

</details>

앞서 [명제 2](#pp2)의 첫 번째와 두 번째 조건을 만족하는 임의의 모임이 주어졌을 때, 이를 basis로 갖는 $X$의 위상이 존재하느냐는 질문을 던졌었는데, 이는 위 명제의 쉬운 따름정리가 된다.

<div class="proposition" markdown="1">

<ins id="crl6">**따름정리 6**</ins> 집합 $X$가 주어졌다 하고, $\mathcal{P}(X)$의 부분집합 $\mathcal{B}$가 다음의 두 조건을 만족한다 가정하자.

1. 각각의 $x$에 대하여, 적어도 하나의 $B\in\mathcal{B}$가 존재하여 $x\in B$이다.
2. $x$를 포함하는 $B_1,B_2\in\mathcal{B}$가 존재한다면, 또 다른 $B_3\in\mathcal{B}$가 존재하여 $x\in B_3\subseteq B_1\cap B_2$이다.

그럼 $X$ 위에 정의된 유일한 위상 $\mathcal{T}$가 존재하여, $\mathcal{B}$가 이 위상 $\mathcal{T}$의 basis이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{B}(x)$를 앞선 명제의 증명에서와 같이 <phrase>$\mathcal{B}$의 원소들 중 $x$를 포함하는 것들의 모임</phrase>으로 정의하자. 또,

$$\mathcal{N}(x)=\mathop{\uparrow}\mathcal{B}(x):=\bigcup_{B\in\mathcal{B}}\mathop{\uparrow}B$$

으로 정의하자. 즉 $\mathcal{N}(x)$는 주어진 $x\in X$를 포함하는 $\mathcal{B}$의 원소, 그리고 이 원소보다 큰 $\mathcal{P}(X)$의 원소들을 모두 포함하는 모임이다.

- 임의의 $V\in\mathcal{N}(x)$에 대하여, $V\subseteq V'$라 하자. $\mathcal{N}(x)$의 정의에 의하여, $U\subseteq V$를 만족하는 $U\in\mathcal{B}(x)$가 존재하며, 이러한 $U$에 대해 $U\subseteq V'$이므로 $V'\in\mathcal{N}(x)$이다.
- $\mathcal{N}(x)$의 원소들 $V_1,\ldots, V_n$이 주어졌다 하자. 그럼 $U_i\subseteq V_i$를 만족하는 $U_i\in\mathcal{B}(x)$들이 존재한다. [명제 2](#pp2)의 두 번째 조건을 귀납적으로 사용하면, 적당한 $U\in\mathcal{B}(x)$가 존재하여 $U\subseteq U_1\cap\cdots\cap U_n$임을 알 수 있다. 특히 $U\subseteq V_1\cap\cdots\cap V_n$이므로, $V_1\cap\cdots\cap V_n\in\mathcal{N}(x)$이다.
- $\mathcal{N}(x)$의 임의의 원소 $V$에 대하여, $W\subseteq V$를 만족하는 $W\in\mathcal{B}(x)$가 존재하므로 $x\in V$이다.
- $\mathcal{N}(x)$의 임의의 원소 $V$에 대하여, $W\subseteq V$를 만족하는 $W\in\mathcal{B}(x)$를 택하자. 그럼 임의의 $W\in\mathcal{B}$이며, 따라서 임의의 $y\in W$에 대해 $W\in\mathcal{B}(y)$이다. $W\subseteq V$이므로, 이로부터 $V\in\mathcal{N}(y)$가 모든 $y$에 대해 성립함을 안다.

이제 [§열린집합, 명제 6](/ko/math/topology/open_sets#pp6)을 적용하여 위상공간 $\mathcal{T}$를 얻을 수 있고, 이 위상공간에서 $\mathcal{B}(x)$는 $x$에서의 local basis가 되므로 [명제 5](#pp5)에 의해 $\mathcal{B}$는 $\mathcal{T}$의 basis가 된다.

</details>

이 과정을 통해 $\mathcal{B}$로부터 얻어지는 위상을 $\mathcal{B}$에 의해 생성된 위상이라 부르며, 비슷하게 subbasis $\mathcal{S}$로부터 basis를 만들고, 이 basis를 통해 생성된 위상을 $\mathcal{S}$로부터 얻어지는 위상이라 부른다.

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.  
**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---