---

title: "옹골공간"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/compact_spaces
header:
    overlay_image: /assets/images/Math/Topology/Compact_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-03
last_modified_at: 2024-12-03
weight: 14

---

이제 우리는 옹골성의 개념을 정의한다.

## 옹골집합

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$가 *compact<sub>옹골</sub>*인 것은 $X$의 임의의 open covering $(U\_i)\_{i\in I}$가 주어질 때마다, 유한한 부분집합 $J\subseteq I$가 존재하여 $(U\_j)\_{j\in J}$가 여전히 $X$의 open covering인 것이다.

</div>

위상공간 $X$의 부분공간 $Y$를 생각하자. 그럼 $Y$ 또한 위상공간이므로, 이 위상공간이 compact인지를 살펴볼 수 있다. 다음 명제는 $Y$가 compact인 것을 따져보기 위해서는 $X$의 열린집합들로 이루어진 covering을 생각하면 된다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위상공간 $X$의 부분공간 $Y$를 생각하자. 그럼 $Y$가 compact인 것과, $X$의 열린집합들의 family $(U\_i)\_{i\in I}$가 $Y\subseteq\bigcup U_i$를 만족할 때마다 유한한 부분집합 $J\subseteq I$가 존재하여 $(U\_j)\_{j\in J}$의 합집합이 여전히 $Y$를 포함하는 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $Y$가 compact라 가정하고, $Y\subseteq\bigcup U_i$를 만족하는 $X$의 열린집합들의 family $(U\_i)\_{i\in I}$가 주어졌다 하자. 그럼 $Y\cap U_i$들은 $Y$에서 열린집합이고 따라서 $(U\_i\cap Y)\_{i\in I}$는 $Y$의 open covering이며, 이로부터 유한한 부분집합 $J$를 택하여 $(U\_j\cap Y)\_{i\in J}$가 여전히 $Y$의 open covering이도록 할 수 있다. 그럼 $(U\_j)$들의 합집합이 여전히 $Y$를 포함하는 것이 자명하다.

거꾸로 주어진 조건이 성립한다 하고, $Y$의 임의의 open covering $(V\_i)\_{i\in I}$이 주어졌다 하자. 그럼 $Y$의 위상구조의 정의에 의하여 $V\_i=U\_i\cap Y$이도록 하는 $X$의 열린집합들 $(U\_i)$가 존재하며, $\bigcup U\_i$는 $Y$를 포함한다. 따라서 유한한 부분집합 $J$가 존재하여 $(U\_j)\_{j\in J}$들의 합집합이 $Y$를 포함한다. 그럼 $(V\_j)\_{j\in J}$가 원하는 $(V\_i)\_{i\in I}$의 finite subcover이다.

</details>

위의 명제에 의하여, $Y$의 compactness를 증명하기 위해서는 $Y$를 포함하는 공간인 $X$에서의 열린집합들로 $Y$를 덮은 후, 이들이 [정의 1](#def1)의 조건을 만족함을 보이면 충분하다. 따라서, 약간의 남용을 통해 $Y\subseteq \bigcup U_i$를 만족하는 $X$의 열린집합들 $U_i$를 $Y$의 open cover라고 말하고, 혼동의 여지가 있는 경우만 이를 명확히 구별하기로 한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**보조정리 3**</ins> Compact space의 닫힌집합은 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Compact space $X$, $X$의 닫힌집합 $Y$가 주어졌다 하고 $Y$의 open covering $(U_i)$가 주어졌다 하자. 그럼 $X\setminus Y$는 열린집합이며, 이 집합을 $Y$의 open covering $(U_i)$에 추가해준 것은 $X$의 open covering이다. $X$는 compact이므로 이 새로운 covering의 finite subcover가 존재하며, 그 finite subcover에서 $X\setminus Y$를 다시 뺀 것도 $Y$의 covering이 되며 원래의 $(U_i)$의 finite subcover이다.

</details>

## 옹골 하우스도르프 공간

앞선 글에서 정의한 Hausdorff space의 경우, compact 조건이 추가되면 더 좋은 조건들을 만족한다. 이를 위해 우선 다음 보조정리를 보이자.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Hausdorff space $X$가 주어졌다 하고, $X$의 한 점 $x$, 그리고 $x$를 포함하지 않는 $X$의 compact subspace $Y$가 주어졌다 하자. 그럼 두 집합 $\\{x\\}$와 $Y$는 근방으로 분리가능하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X$가 Hausdorff space이므로, 각각의 $y\in A$마다 $x$의 열린근방 $U_{xy}$, $y$의 열린근방 $V_y$가 존재하여 $U_{xy}\cap V_y=\emptyset$이다. 이제 [보조정리 3](#lem3)에 의하여 $(V\_y)\_{y\in Y}$의 finite subcover $V\_{y\_1},\ldots,V\_{y\_n}$이 존재하여 여전히

$$Y\subseteq V_{y_1}\cup\cdots\cup V_{y_n}$$

이 성립하도록 할 수 있다. 이제

$$U_{xy_1}\cap \cdots\cap U_{xy_n}$$

은 $\bigcup\_{i=1}^n V\_{y\_i}$와 서로소인 $\\{x\\}$의 열린근방이다.

</details>

특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> Hausdorff space $X$의 compact subset $Y$는 닫힌집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[보조정리 4](#lem4)의 증명에서 

$$U_x=U_{xy_1}\cap \cdots\cap U_{xy_n}$$

이라 하면 $X\setminus Y=\bigcup\_{x\not\in Y} U\_x$이다.

</details>

앞서 언급한 것과 같이, compact Hausdorff space는 다음의 추가적인 분리공리를 만족한다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Compact Hausdorff space는 regular space이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Compact Hausdorff space $X$를 고정하고, 한 점 $x\in X$와 $x$를 포함하지 않는 $X$의 닫힌집합 $Y$가 주어졌다 하자. 그럼 $Y$는 [보조정리 3](#lem3)에 의해 compact이고 따라서 원하는 결과는 [보조정리 4](#lem4)로부터 자명하다. 

</details>

뿐만 아니라, 이를 한 번 더 적용하여 다음 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Compact Hausdorff space는 normal space이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Compact Hausdorff space의 서로소인 임의의 두 닫힌집합 $A,B$가 주어졌다 하자. 그럼 각각의 $a\in A$에 대하여, [보조정리 6](#lem6)에 의해 $a$의 열린근방 $U_a$, $B$의 열린근방 $V_{a}$가 존재하여 $U_a\cap V_a=\emptyset$이다. 이제 [보조정리 4](#lem4)와 마찬가지 방식으로, $(U\_a)\_{a\in A}$는 $A$의 open covering이 되므로 다시 [보조정리 3](#lem3)에 의해 $(U\_a)$의 finite subcover $U\_{a\_1},\ldots, U\_{a\_n}$을 잡을 수 있고, 이제 두 열린집합

$$U_{a_1}\cup\cdots \cup U_{a_n},\qquad V_{a_1}\cap\cdots\cap V_{a_n}$$

이 두 닫힌집합 $A,B$를 분리하는 열린근방이다.

</details>

## 옹골공간과 연속함수

Compactness는 연속함수에 대해서도 잘 작동한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 연속함수 $f:X \rightarrow Y$와 $X$의 임의의 compact subspace $A$에 대하여 $f(A)$도 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f(A)$의 임의의 open covering $(U\_i)$에 대하여, $(f^{-1}(U\_i))$는 $A$의 covering이고 $A$가 compact이므로 finite subcover가 존재한다. 이에 해당되는 $U\_i$들이 $f(A)$를 덮는 finite open subcover가 된다.

</details>

한편, 우리는 전단사인 연속함수 $f:X \rightarrow Y$가 homeomorphism일 필요는 없다는 것을 살펴보았는데, 만일 $X$가 compact이고 $Y$가 Hausdorff라면 이것이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> $X$가 compact이고 $Y$가 Hausdorff라면 임의의 전단사인 연속함수 $f:X \rightarrow Y$는 homeomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 위해서는 $f^{-1}$이 연속임을 보여야 한다. [§연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)의 셋째 조건을 사용하자. 즉 $f$가 closed map인 것을 보여야 한다. 그런데 이는 $X$의 닫힌집합 $A$가 주어졌다 하고, [보조정리 3](#lem3), [명제 8](#prop8), 그리고 [따름정리 5](#cor5)를 순서대로 사용하면 된다.

</details>

## 유한 교집합 성질

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 집합 $X$의 부분집합들의 family $\mathcal{A}$가 *finite intersection property*를 갖는다는 것은 $\mathcal{A}$의 유한히 많은 임의의 원소들 $A_1,\ldots, A_n$에 대하여 

$$A_1\cap\cdots\cap A_n$$

이 공집합이 아닌 것이다.

</div>

그럼 특히 $\emptyset\not\in \mathcal{A}$가 성립한다. 또, 이 조건을 만족하는 family $\mathcal{A}$가 주어진다면, $\mathcal{A}$의 유한한 교집합들을 모두 추가하여 $X$의 filter base $\mathcal{B}$를 만들 수 있다. ([§위상공간의 다른 정의들, ⁋정의 6](/ko/math/topology/equivalent_formulations_of_topology#def6)) 이러한 이유로 $\mathcal{A}$를 $\uparrow \mathcal{B}$의 *subbase*라 부르기도 한다.

그럼 다음 명제는 compactness를 다른 방식으로 서술한 것이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 위상공간 $X$가 compact인 것은 finite intersection property를 만족하는 임의의 닫힌집합들의 family $\mathcal{A}$에 대하여, $\bigcap \mathcal{A}\neq\emptyset$인 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

여집합을 취하면 충분하다. 

</details>