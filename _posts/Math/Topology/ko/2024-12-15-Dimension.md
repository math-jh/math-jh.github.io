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

$X$가 $d$차원 위상공간이라 하고, $Y$의 임의의 open covering $\\{V\_j\\}$이 주어졌다 하자. 그럼 각각의 $V\_j$마다 $V\_j=U\_j\cap Y$이도록 하는 $X$의 open subset $U\_j$가 존재한다. 이제 $X$는 $U\_j$들과, $X\setminus Y$로 덮을 수 있다. 그럼 이 covering의 order$\leq d+1$짜리 refinement가 존재하며, 이를 다시 $Y$와 교집합하면 $\\{V\_j\\}$의 order$\leq d+1$짜리 refinement를 얻는다. 

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

첫쨰 조건과 둘쨰 조건은 여집합을 생각하면 동치인 것이 자명하며, 둘째 조건과 셋째 조건이 동치인 것은 $X\setminus \cl U$와 $U$를 생각하면 자명하다. 마지막으로 둘째 조건과 넷째 조건이 정의에 의해 동치이다. 

</details>

특히 irreducible space는 Hausdorff가 아니다. 위의 명제의 마지막 동치 때문에 irreducible space는 *hyperconnected space*라 부르기도 한다. 비슷한 맥락에서 다음이 성립한다. (참고: [§연결공간, ⁋명제 3](/ko/math/topology/connected_spaces#prop3))

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 만일 $X$가 irreducible open subset들의 합집합

$$X=\bigcup_{i\in I} U_i$$

이고 $U_i\cap U_j\neq \emptyset$이 모든 $i,j$에 대해 성립한다 하자. 그럼 $X$는 irreducible이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 두 열린집합 $V, W$가 주어졌다 하고, $V\cap W\neq\emptyset$임을 보이자. 그럼 주어진 가정으로부터 우선 $U_i\cap V\neq\emptyset$ 그리고 $U_j\cap W\neq\emptyset$을 만족하는 $i,j$가 존재한다. 이제 [명제 7](#prop7)의 셋째 결과와 [§부분공간, ⁋명제 5](/ko/math/topology/subspaces#prop5)로부터 $U_i$도 irreducible이므로, $U_i$의 두 nonempty subset $U_i\cap V$와 $U_i\cap U_j$도 반드시 공집합이 아닌 교집합을 가져야 한다. 즉

$$(U_i\cap V)\cap (U_i\cap U_j)=U_i\cap U_j\cap V\neq\emptyset$$

이고, $U_i\cap U_j\cap V$를 $U_j$의 nonempty subset으로 보면 마찬가지로 $U_j$의 irreducibilty로부터 다음의 식

$$(U_i\cap U_j\cap V)\cap (U_j\cap W)=U_i\cap U_j\cap V\cap W\neq\emptyset$$

을 얻고 특히 $V\cap W\neq\emptyset$이다. 

</details>

Connected component와 비슷하게 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 위상공간 $X$의 부분집합 $A$에 대하여, $A$를 포함하는 *irreducible component*는 $A$를 포함하는 irreducible subset 중 가장 큰 것을 의미한다. 

</div>

그럼 [§연결공간, ⁋명제 2](/ko/math/topology/connected_spaces)과 비슷한 논증에 의하여, irreducible set의 closure는 irreducible인 것을 보일 수 있으므로 irreducible component는 반드시 closed subset이다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 위상공간 $X$에 대하여, $X$의 irreducible closed subset들의 strictly descending chain

$$A_n\supsetneq\cdots\supsetneq A_0$$

의 *length<sub>길이</sub>*를 $n$으로 정의한다. 그럼 $X$의 *Krull dimension<sub>크룰 차원</sub>*을 다음의 식

$$\dim X=\sup\{\text{length of strictly descending chains of irreducible closed subsets}\}$$

으로 정의한다. 만일 무한한 길이의 strictly descending chain이 존재한다면 $\dim X=\infty$로 정의하고, $X=\emptyset$인 경우 $\dim X=-\infty$로 정의한다. 

</div>

그럼 다음과 같은 상황에서는 $X$의 Krull dimension은 항상 유한하다. 특히 Hausdorff space에서는 오직 singleton만이 irreducible subset이므로 Hausdorff space의 Krull dimension은 $0$이다. 

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 위상공간 $X$가 *noetherian<sub>뇌터 공간</sub>*이라는 것은 임의의 닫힌집합들의 chain

$$A_1\supseteq A_2\supseteq\cdots$$

이 주어질 때마다, 적당한 $n$이 존재하여 $A_n=A_{n+1}=\cdots$이도록 할 수 있는 것이다.

</div>

Noetherian 조건은 강력한 유한성의 조건을 준다. 가령 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Noetherian space는 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Noetherian space $X$와 $X$의 open covering $\\{U\_i\\}\_{i\in I}$가 주어졌다 가정하자. 그럼

$$\mathcal{C}=\left\{\bigcup_{j\in J} U_j:\text{$J$ finite subset of $I$}\right\}$$

라 정의할 수 있다. 이제 $\mathcal{C}$의 임의의 totally ordered subset을 생각하면, 이는 그 여집합들로 이루어진 닫힌집합들의 descending chain과 동치이고 따라서 $X$가 noetherian이라는 가정으로부터 이는 언젠가 멈춰야 한다. 즉, $\mathcal{C}$는 [\[집합론\] §선택공리, ⁋정리 4](/ko/math/set_theory/axiom_of_choice#thm4)의 조건을 만족하고 따라서 $\mathcal{C}$는 maximal element $U\in \mathcal{C}$를 갖는다. 만일 $X\neq U$라면, $x\in X\setminus U$를 포함하는 $U_j$를 택할 수 있고 그럼 $U\cap U_j$는 $U$를 strict하게 포함하는 $\mathcal{C}$의 원소이므로 $U$의 maximality에 모순이다. 따라서 $U=X$이고 우리는 원하는 결과를 얻는다. 

</details>

추가적으로 noetherian space에 대해 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Noetherian topological space $X$에 대하여, 다음이 성립한다.

1. $X$의 임의의 부분공간은 noetherian이다.
2. $X$는 유한히 많은 irreducible component를 가진다. 
3. $X$의 각각의 irreducible component는 공집합이 아닌 $X$의 열린집합을 포함한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $X$의 임의의 부분공간 $Y$가 주어졌다 하고 $Y$의 임의의 닫힌집합들의 descending chain 
    
    $$A_1\supseteq A_2\supseteq \cdots$$

    가 주어졌다 하자. 그럼 $A_i=A_i' \cap Y$를 만족하는 $X$의 닫힌집합 $A_i'$들이 존재한다. 이제 $B_i=A_1'\cap\cdots\cap A_i'$라 하면, $B_i\cap Y=A_i$이고 $B_i$는 $X$의 닫힌집합들의 descending chain이다. 
2. $\mathcal{C}$를 $X$의 닫힌집합 중, 유한히 많은 irreducible component들의 합집합으로 나타낼 수 없는 집합들의 모임이라 하자. 그럼 $\mathcal{C}=\emptyset$임을 보이면 된다. 결론에 반하여 $\mathcal{C}$가 공집합이 아니라 하면, [명제 12](#prop12)의 증명에서와 마찬가지 방법으로 $\mathcal{C}$가 minimal element $A$를 갖는다는 것을 안다. 이제 $A$는 irreducible이 아니므로, 두 닫힌집합 $B_1,B_2$에 대해 $A=B_1\cup B_2$로 나타낼 수 있고 $B_1,B_2\not\in \mathcal{C}$라는 가정으로부터 이들 각각은 유한한 irreducible component를 갖는다. 약간의 계산을 통해 이 irreducible decomposition들을 사용하여 $A=B_1\cup B_2$의 유한한 irreducible decomposition을 찾을 수 있고, 이는 모순이므로 $\mathcal{C}=\emptyset$이어야 한다.
3. $X=A_1\cup\cdots\cup A_n$이 irreducible decomposition이라 하고, $X\setminus (A_2\cup\cdots\cup A_n)$을 생각하면 이 집합이 $A\_1$에 포함되는 공집합이 아닌 $X$의 열린집합이다. 

</details>

그럼 만일 $X$가 noetherian이라면, $X$의 irreducible decomposition

$$X=\bigcup_{i=1}^r X_i$$

이 존재하며, $X_i$들은 모두 닫힌집합이고, $X_i$의 여집합도 닫힌집합들의 유한한 합집합이므로 $X_i$는 열린집합이기도 하다. 

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 위상공간 $X$와 열린집합 $U$에 대하여, $U$와 만나는 $X$의 irreducible closed subset과, $U$의 irreducible closed subset 사이의 일대일대응이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $U\cap Z\neq\emptyset$을 만족하는 $X$의 irreducible subspace $Z$가 주어졌다 하고, $Z\cap U$의 공집합이 아닌 임의의 두 열린집합이 서로소가 아님을 보여야 한다. $Z\cap U$의 임의의 부분집합은 $Z$의 열린집합 $V_1, V_2$에 대하여 $V_1\cap U$, $V_2\cap U$의 꼴이므로, 다음의 식

$$(V_1\cap U)\cap (V_2\cap U)=(V_1\cap V_2)\cap U$$

으로부터 만일 $(V_1\cap U)\cap(V_2\cap U)\neq\emptyset$이라면 $V_1\cap V_2\neq\emptyset$이 되어 $Z$가 irreducible이라는 가정에 모순이다. 

거꾸로 $U$의 irreducible closed subset $Y\subseteq U$가 주어졌다 하면 $Y$의 closure 또한 irreducible이므로 $X$의 irreducible $\cl_X(Y)$가 $U$와 만나는 $X$의 irreducible subset이 된다. 즉 이로부터 두 함수

$$\{\text{irreducible closes subset of $X$ meeting $U$}\}\rightarrow \{\text{irreducible closed subset of $U$}\};\qquad Z\mapsto Z\cap U$$

그리고 

$$\{\text{irreducible closed subset of $U$}\} \rightarrow \{\text{irreducible closes subset of $X$ meeting $U$}\};\qquad Y\mapsto \cl_X(Y)$$

를 얻으며, 이들이 서로의 bijection임을 확인할 수 있다.

</details>

뿐만 아니라, 위의 증명에서의 두 함수는 inclusion-preserving이므로, $U$와 만나는 $X$의 irreducible component와 $U$의 irreducible component 사이의 일대일대응이 존재한다.

이제 다음 명제를 보이자.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> 만일 위상공간 $X$의 두 유한차원 닫힌 부분공간 $Y,Z$가 존재하여 $X=Y\cup Z$라면, 이들의 Krull dimension 또한 식 $\dim X=\max(\dim Y,\dim Z)$을 만족한다.

</div>