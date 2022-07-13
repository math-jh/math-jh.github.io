---

title: "열린집합과 닫힌집합"
excerpt: "기본정의 1: 열린집합과 닫힌집합"

lang: ko

categories: [Math / Topology]
permalink: /ko/math/topology/basic_definition_1
header:
    overlay_image: /assets/images/Topology/Topological_structures.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-19
last_modified_at: 2022-04-07
weight: 1

---

## 위상공간

그 동안 탐구해온 대수적인 구조들은 벡터공간을 제외하면 우리가 알고 있는 일반적인 공간과는 큰 접점이 없었다. 우리에게 친숙한 <em_ko>공간</em_ko>의 개념은 지금부터 살펴볼 위상공간을 통해 수학적으로 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $X$ 위에 정의된 *위상<sub>topology</sub>*이라는 것은 다음의 조건을 만족하는 $\mathcal{P}(X)$의 부분집합 $\mathcal{T}$를 의미한다.

1. $\emptyset,X\in\mathcal{T}$가 성립한다.[^1]
2. $\mathcal{T}$의 원소들의 임의의 합집합은 $\mathcal{T}$에 속한다.
3. $\mathcal{T}$의 원소들의 <em_ko>유한한</em_ko> 교집합은 $\mathcal{T}$에 속한다.

이렇게 위상이 주어진 집합 $X$를 *위상공간<sub>topological space</sub>*이라고 부르고, 이 때 $X$의 원소들을 *점<sub>point</sub>*들, 그리고 $\mathcal{T}$의 원소들을 *열린집합<sub>open set</sub>*들이라 부른다.

</div>

이렇게 추상적인 정의가 어떤 방식으로 공간에 대한 정보를 주는지를 이해하는 것이 학부 위상수학의 첫 번째 목표라고 할 수 있다. 다음의 명제를 증명해보자.

> $X$의 부분집합 $U$가 열린집합인 것은 <box>$U$의 원소 $x$마다, $x$를 포함하고 $U$에 포함된 열린집합 $V_x$가 존재하는 것</box>과 동치이다.

먼저 $U$가 열린집합이라면, 임의의 $x$에 대하여 $U$가 $V_x$의 역할을 하므로 더 이상 증명할 것이 없다. 따라서 반대방향만 보이면 충분하다. 임의의 $x\in U$에 대하여, $V_x\subset U$가 모든 $x\in U$에 대해 성립하므로,

$$\bigcup_{x\in U}V_x\subset U$$

가 성립한다. 반대로 임의의 $x\in U$에 대하여, $x\in V_x\subset\bigcup_{x\in U} V_x$이므로

$$\bigcup_{x\in U}V_x= U$$

이다. 따라서 $U$는 열린집합들 $V_x$의 합집합이므로, 정의의 두 번째 조건에 의하여 열린집합이 된다.

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 위상공간을 다룰 때에는 전체집합이 $X$가 되어야 한다는 것이 명확하므로, $A^c$라 하면 항상 $X\setminus A$를 뜻하는 것으로 이해한다.

</div>

위상공간의 가장 자명한 예시는 다음의 예시일 것이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 임의의 집합 $X$에 대하여, $X$ 위에 정의된 위상 중 가장 작을 수 있는 것은 $\\{\emptyset,X\\}$이다. 실제로 이 집합으로 정의된 구조는 정의의 1번부터 3번 조건을 모두 만족하므로 위상공간이 된다. 이를 *trivial topology<sub>자명한 위상</sub>*라 부른다. 

반대로, $X$ 위에 정의된 위상 중 가장 클 수 있는 것은 $\mathcal{P}(X)$이다. 이 또한 위상공간을 이루며, 우리는 이를 *discrete topology<sub>이산위상</sub>*라 부른다.

</div>

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 어떤 집합 위에 두 위상 $\mathcal{T}\_1$, $\mathcal{T}\_2$가 주어졌고 이들이 $\subset$으로 비교가능하다고 하자. 만일 $\mathcal{T}\_1$, $\mathcal{T}\_2$에 대하여 $\mathcal{T}\_1\subset\mathcal{T}\_2$가 성립한다면 $\mathcal{T}\_2$가 $\mathcal{T}\_1$보다 *강한 위상<sub>stronger topology</sub>*이라고 하고, $\mathcal{T}\_1$은 $\mathcal{T}\_2$보다 *약한 위상<sub>weaker topology</sub>*이라고 한다. 
</div>

예를 들어, 집합 $X$ 위에 정의된 <em_ko>임의의</em_ko> 위상 $\mathcal{T}$는 $X$ 위의 discrete topology보다는 항상 약하고, $X$ 위의 trivial topology보다는 항상 강하다. 

$X$에 멀고 가까움의 개념을 주기 위해서 가장 좋은 도구는 <em_ko>거리</em_ko>지만, 거리를 줄 수 있는 공간은 매우 적기 때문에 더 일반화된 개념이 필요하다. $\mathcal{T}$에 의해 정의되는 일종의 멀고 가까움을 <box>두 점이 얼마나 많은 열린집합에 공통적으로 포함되는지</box>를 통해 살펴보면 거리가 주어진 것과 비슷한 이야기를 할 수 있다.[^2]

우선 trivial topology의 경우를 살펴보자. 만약 $X=\\{x,y\\}$이고 $X$에 trivial topology가 주어졌다면, $X$의 두 점 $x,y$는 위상공간의 관점에서는 완벽하게 동등하다. 이는 열린집합들을 이용해서 두 점 $x,y$를 구별할 수 없기 때문이다. 이렇게 어떠한 위상공간 $X$의 두 점 $x,y$가 정확히 동일한 열린집합들에 포함된다면 이 두 점이 *topologically indistinguishable<sub>위상적으로 구별불가능</sub>*이라고 말한다.

반면 동일한 집합 $X=\\{x,y\\}$에 다음과 같은 위상

$$\mathcal{T}=\{\emptyset, \{x\}, X\}$$

혹은 더 강력하게 discrete topology를 준다면 두 점 $x$와 $y$는 이 위상공간들에서는 구별이 가능해진다. 점 $x$는 포함하지만 $y$는 포함하지 않는 열린집합 $\\{x\\}$가 존재하기 때문이다. 더욱이 discrete topology에서는 $x$와 $y$를 각각 포함하는 두 열린집합 $\\{x\\}$, $\\{y\\}$가 존재하여 이들 둘을 분리할 수도 있다.[^3] 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 위상공간 $X$가 *Hausdorff space<sub>하우스도르프 공간</sub>*라는 것은 임의의 두 점 $x,y$에 대하여 $x\in U$이고 $y\in V$를 만족하는 두 열린집합 $U,V$가 존재하여 $U\cap V=\emptyset$이도록 할 수 있는 것이다.

</div>

위의 정의와 같이 특정한 점을 포함하는 열린집합은 앞으로도 계속 나오게 되므로, 불필요하게 말을 반복하기보다는 다음을 정의하는 것이 효율적이다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $X$의 임의의 원소 $x$에 대하여, $x$를 포함하는 열린집합 $U$를 $x$의 *열린근방<sub>open neighborhood</sub>*이라 부른다. $X$의 부분집합이 $x$의 어떤 open neighborhood를 포함한다면 이 부분집합을 $x$의 *근방<sub>neighborhood</sub>*이라 부른다.  

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 조금 덜 자명한 예시를 살펴보자.
   
임의의 집합 $X$에 대하여, $\mathcal{T}$를 다음의 집합

$$\mathcal{T}=\{U\subset X:\text{either $U^c$ is finite or $U=\emptyset$}\}$$

으로 정의하자. 그럼, 

1. $X^c=\emptyset$이 유한집합이므로 $X\in\mathcal{T}$이다. 또, $\emptyset$은 정의에 의해 $\mathcal{T}$의 원소이다.
2. 만일 $U\_i$들이 열린집합이라면, $(\bigcup U\_i)^c=\bigcap U\_i^c$이므로 $(\bigcup U\_i)^c$는 유한하고, 따라서 $\bigcup U\_i$도 열린집합이다.
3. 만일 $U\_i$들이 열린집합들의 *유한한* family라면, $(\bigcap U\_i)^c=\bigcup U\_i^c$이므로, $U\_i$ 중 하나가 $\emptyset$이 아닌 이상 $(\bigcap U\_i)^c$도 유한하고, 만일 어떤 $U\_i$가 $\emptyset$이라면 $(\bigcap U\_i)^c=X$이다. 어떤 경우든 $\bigcap U\_i$도 열린집합이다. 

따라서, $\mathcal{T}$는 $X$ 위에 위상공간 구조를 준다. 우리는 이를 *cofinite topology<sub>여유한위상</sub>*라 부른다. 

만일 $X$ 자체가 유한집합이라면, $X$의 임의의 부분집합은 유한집합이므로 $U^c$가 항상 유한이고 따라서 $X$가 유한한 경우 cofinite topology는 정확히 discrete topology와 동일하다. 

</div>

## 닫힌집합

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 위상공간 $X$에 대하여, 집합 $C$가 *닫힌집합<sub>closed set</sub>*이라는 것은 $C$의 여집합 $C^c$가 열린집합인 것이다.

</div>

$X$ 위의 임의의 위상 $\mathcal{T}$에서 $\emptyset$과 $X$는 열린집합인 동시에 닫힌집합이고, 아예 discrete topology를 주면 임의의 부분집합이 열린집합인 동시에 닫힌집합이 된다. 따라서 닫힌집합과 열린집합은 반대개념이 아니라, 오히려 같은 것을 다른 방식으로 표현한 것에 가깝다. 예컨대, 위상 $\mathcal{T}$는 사실 닫힌집합들을 이용하여 다음과 같이 정의할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> 집합 $X$ 위에 다음의 조건들을 만족하는 모임 $\mathcal{C}$가 주어졌다 하자.

1. $\emptyset$, $X\in\mathcal{C}$
2. $\mathcal{C}$는 임의의 교집합에 대하여 닫혀있다.
3. $\mathcal{C}$는 <em_ko>유한한</em_ko> 합집합에 대하여 닫혀있다.

그럼 $\mathcal{C}$의 각 원소들의 여집합을 열린집합으로 갖는 위상 $\mathcal{T}$가 유일하게 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음의 De Morgan 법칙 (<#ref#>)

$$\left(\bigcap C_i\right)^c=\bigcup C_i^c,\quad\left(\bigcup C_i\right)^c=\bigcap C_i^c$$

으로부터 자명하다.

</details>

---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

[^1]: 사실, index set을 공집합으로 두면 1번 조건은 2번과 3번 조건에서 유도되긴 한다.
[^2]: 나중에, 위상공간보다는 조금 더 직관적으로 가까움의 개념을 포함하는 (거리는 정의되지 않은) 공간을 살펴보게 된다.
[^3]: 위에서 예로 든 $\mathcal{T}$의 경우, $x$를 $y$에서 분리하는 것은 열린집합 $\\{x\\}$를 통해 가능하지만, $y$를 $x$에서 분리하는 것은 애매하다.
