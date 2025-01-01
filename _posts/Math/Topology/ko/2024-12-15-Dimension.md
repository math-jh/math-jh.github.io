---

title: "차원"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/dimension
header:
    overlay_image: /assets/images/Math/Topology/Dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
last_modified_at: 2024-12-15
weight: 19

---

이번 글에서 우리는 위상공간의 차원을 정의한다. 우선 우리는 일반적으로 사용하는 차원을 정의한 후, [대수기하학](/ko/algebraic_geometry)에서 사용할 차원의 개념을 따로 정의한다. 

## Covering dimension

편의상 **[Mun]**을 따라 이 절에서는 compact space의 차원만 정의한다. 기본적인 아이디어는 $X$의 점이 열린집합들로 몇 번 덮이는지를 재는 것인데, 물론 $X$는 하나의 열린집합 $X$로만 덮이므로, 이를 임의의 open covering을 이용해서 정의해야 할 것이며, open covering을 아무렇게나 주면 점 하나를 원하는만큼 많은 열린집합들로 덮을 수 있으므로 어떠한 종류의 최소성을 담보해야 할 것이다. 

우선 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $X$의 부분집합들의 family $(U\_i)\_{i\in I}$가 $m+1$의 *order*를 갖는다는 것은 $X$의 어떠한 점도 $m+1$개 이상의 $U_i$에 속하지 않으며, $X$의 어떠한 점 하나는 정확히 $m+1$개의 $U_i$들에 속하는 것이다.

</div>

그럼 공간 $X$의 차원을 다음과 같이 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 공간 $X$가 *유한차원<sub>finite dimensional</sub>*이라는 것은 적당한 $m$이 존재하여, 임의의 open covering $(U\_i)\_{i\in I}$가 주어질 때마다, order $m+1$짜리 $(U\_i)$의 open refinement $(V\_j)\_{j\in J}$가 항상 존재하는 것이다. 이것이 가능하도록 하는 최소의 $m$을 $X$의 *차원<sub>dimension</sub>*으로 정의하고 $\dim X$로 적는다. 

</div>

다소 주의할만한 것은 위상공간은 다음 그림과 같이 상당히 웃기게 생길 수 있으며, 이 때 우리는 이 위상공간의 차원을 두 성분의 차원 중 큰 것이 되도록 정의했다는 것이다.

img

한편 우리가 차원에 기대함직한 성질이 몇 가지 있는데, 그들 중 일부는 다음과 같다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $X$가 유한차원 위상공간이고 $Y$가 $X$의 closed subspace라면, $Y$도 유한차원이고 $\dim Y\leq\dim X$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

다음 명제는 [정의 2](#def2) 이후에 언급한 주의점을 더 수학적으로 다듬은 것이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 만일 위상공간 $X$의 두 유한차원 닫힌 부분공간 $Y,Z$가 존재하여 $X=Y\cup Z$라면, $\dim X=\max(\dim Y,\dim Z)$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

그리고 물론 우리는 $\mathbb{R}^n$의 차원이 $n$차원이기를 바란다. 그러나 이를 보이는 것은 쉽지는 않은데, 이는 기본적으로 현재 우리가 $\mathbb{R}^n$과 $\mathbb{R}^m$이 homeomorphic하지 않다는 것조차 보이기가 힘들기 때문이다. 그 대신 이보다 약한 다음의 명제는 정의로부터 쉽게 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $\mathbb{R}^n$의 임의의 compact subspace는 항상 $n$차원 이하이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## Krull dimension

한편 우리는 대수기하학에서 사용하는 차원의 개념을 정의할 것인데, 대수기하학에서 관심을 갖는 공간은 일반적으로 생각하는 위상구조와는 다른 위상구조가 주어져 있어서 이 정의는 다소 비직관적이다. 특히, 일상적인 위상구조가 주어진 $\mathbb{R}^n$은 항상 $0$차원이다. 그러나 어쨌든 이 정의를 위상수학의 언어로 할 수 있는 것은 사실이므로 이 페이지에 같이 적어두기로 한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위상공간 $X$가 *irreducible<sub>기약</sub>*이라는 것은 $X=A\cup B$이도록 하는 $X$의 비자명한 닫힌집합이 존재하지 않는 것이다. 

</div>

그럼 다음이 모두 동치이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위상공간 $X$에 대하여 다음이 모두 동치이다.

1. $X$가 irreducible이다.
2. 공집합이 아닌 $X$의 임의의 열린집합 $U,V$에 대하여, $U\cap V\neq\emptyset$이다.
3. 공집합이 아닌 $X$의 임의의 열린집합 $U$에 대하여, $\cl U=X$이다.
4. $X$의 임의의 열린집합이 connected이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

특히 irreducible space는 Hausdorff가 아니다. 위의 명제의 마지막 동치 때문에 irreducible space는 *hyperconnected space*라 부르기도 한다.

Connected component와 비슷하게 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 위상공간 $X$의 부분집합 $A$에 대하여, $A$를 포함하는 *irreducible component*는 $A$를 포함하는 irreducible subset 중 가장 큰 것을 의미한다. 

</div>

그럼 대수기하학의 언어에서, 앞선 그림 ([##ref##]())은 두 개의 irreducible component들로 쪼개진다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 위상공간 $X$에 대하여, $X$의 irreducible closed subset들의 strictly descending chain

$$A_n\supsetneq\cdots\supsetneq A_0$$

의 *length<sub>길이</sub>*를 $n$으로 정의한다. 그럼 $X$의 *Krull dimension<sub>크룰 차원</sub>*을 다음의 식

$$\dim X=\sup\{\text{length of strictly descending chains of irreducible closed subsets}\}$$

으로 정의한다. 만일 무한한 길이의 strictly descending chain이 존재한다면 $\dim X=\infty$로 정의하고, $X=\emptyset$인 경우 $\dim X=-\infty$로 정의한다. 

</div>

그럼 다음과 같은 상황에서는 $X$의 Krull dimension은 항상 유한하다. 특히, 일반적인 위상이 주어졌을 때 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 위상공간 $X$가 *noetherian<sub>뇌터 공간</sub>*이라는 것은 임의의 닫힌집합들의 chain

$$A_1\supseteq A_2\supseteq\cdots$$

이 주어질 때마다, 적당한 $n$이 존재하여 $A_n=A_{n+1}=\cdots$이도록 할 수 있는 것이다.

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Noetherian topological space $X$에 대하여, 다음이 성립한다.

1. $X$의 임의의 부분공간은 noetherian이다.
2. $X$는 유한히 많은 irreducible component를 가진다. 
3. $X$의 각각의 irreducible component는 공집합이 아닌 $X$의 열린집합을 포함한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

한편 위의 결과를 확인하고 나면, 서로 다른 차원을 갖는 irreducible component가 여럿 주어졌을 때 $X e$의 차원은 [명제 4](#prop4)와 비슷한 다음 결과를 만족하는 것도 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> 만일 위상공간 $X$의 두 유한차원 닫힌 부분공간 $Y,Z$가 존재하여 $X=Y\cup Z$라면, 이들의 Krull dimension 또한 식 $\dim X=\max(\dim Y,\dim Z)$을 만족한다.

</div>