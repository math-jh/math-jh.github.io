---

title: "연결공간"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/connected_spaces
header:
    overlay_image: /assets/images/Math/Topology/Connected_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
last_modified_at: 2025-02-08
weight: 18

---

이제 우리는 위상수학에서 중요한 개념 중 하나인 연결성에 대해 살펴본다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$가 *connected space<sub>연결공간</sub>*라는 것은 $X$가 두 개의 서로소인 열린집합의 합집합으로 나타날 수 없는 것이다. 더 일반적으로, $X$의 부분집합 $A$가 connected라는 것은 $A$에 subspace topology를 준 것이 connected인 것이다.

</div>

그럼 다음의 간단한 결과가 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Connected set $A\subseteq X$에 대해서, $A\subseteq B \subseteq \cl(A)$를 만족하는 $B$는 connected이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

주어진 상황에서, 

$$\cl_B(A)=B\cap \cl_X(A)=B$$

이므로 $A$는 $B$의 dense subset이다. ([§부분공간, ⁋명제 5](/ko/math/topology/subspaces#prop5)) 이제 결론에 반하여 $B$의 서로소인 두 열린집합 $U,V$가 존재하여 $U\cup V=B$라 하자. 그럼 $A$는 $B$의 dense subset이므로 $U\cap A, V\cap A$는 모두 공집합이 아니며 $U\cap V\cap A=\emptyset$이다. 이는 $A$가 connected라는 가정에 모순이다. 

</details>

또, 직관적으로 다음 명제 또한 납득할 만하다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Connected set들의 family $(A_i)$에 대하여, 만일 임의의 $i,j$마다 $A_i\cap A_j\neq\emptyset$이 성립한다면 $A=\bigcup A_i$도 connected이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 두 열린집합 $U,V$가 존재하여 두 조건

$$A=(U\cap A)\cup (V\cap A),\qquad U\cap V\cap A=\emptyset$$

이 성립한다 가정하자. 우선 임의의 $i$에 대하여, $A_i$는 connected이므로 두 식 $A_i\subseteq U$ 혹은 $A_i\subseteq V$ 중 정확히 하나만이 성립해야 한다. 한편, 만일 $A_i\subseteq U$이고 $A_j\subseteq V$라면

$$A_i\cap A_j\subseteq (U\cap A)\cap (V\cap A)=U\cap V\cap A=\emptyset$$

가 되어 모순이므로 $A_i$들은 모두 동시에 $U$에 속하거나 동시에 $V$에 속해야 한다. 그럼 $U\cap A=\emptyset$이거나 $V\cap A=\emptyset$이어야 한다. 

</details>

## 연결집합의 성질들

연결성은 연속함수에 의해 보존되는 성질이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 연속함수 $f:X \rightarrow Y$와 $X$의 connected subset $A\subseteq X$에 대하여, $f(A)$도 connected이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

결론에 반하여 $f(A)$가 connected가 아니라 하고, 

$$f(A)=(V_1\cap f(A))\cup (V_2\cap f(A)), \qquad V_1\cap V_2\cap f(A)=\emptyset$$

이도록 하는 $Y$의 열린집합 $V_1,V_2$를 택하자. 그럼 $f^{-1}(V_1),f^{-1}(V_2)$는 $X$의 열린집합이며, 

$$A=(A\cap f^{-1}(V_1))\cup (A\cap f^{-1}(V_2)),\qquad f^{-1}(V_1)\cap f^{-1}(V_2)\cap A=\emptyset$$

이다. 이제 $A$가 connected라는 가정으로부터 $V_1\cap f(A)=\emptyset$이거나 $V_2\cap f(A)=\emptyset$이어야 한다는 것을 안다. 

</details>

이로부터 다음 따름정리는 자명하다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> Connected space의 quotient space는 connected이다.

</div>

또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Connected space들의 product는 connected이다. 거꾸로, product가 connected라면 각각의 성분들도 connected이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

뒤쪽 방향은 $\pr_i$에 대해 [명제 4](#prop4)를 사용하면 되므로 증명할 것이 없다. 

따라서 각각의 $X_i$들이 connected라 하고, 결론에 반하여 $X=\prod X_i$가 connected가 아니라 하자. $X=U\cup V$이고 $U\cap V=\emptyset$, $U,V\neq\emptyset$이라 하면 

$$f(x)=\begin{cases}1&\text{if $x\in U$}\\0&\text{if $x\in V$}\end{cases}$$

으로 정의한 함수 $f:X \rightarrow \\{0,1\\}$은 연속이다. (여기서 $\\{0,1\\}$은 discrete topology가 주어진 공간이다.) 

이제 원소 $a=(a_i)\in X$를 고정하고, $\iota_i: X_i \rightarrow X$를 $i$번째 성분만 $x$이고, 나머지 성분은 $a$로부터 받아오는 함수로 정하자. 그럼 $f\circ\iota_i$는 $X_i$에서 $\\{0,1\\}$로의 연속함수이며, $X_i$가 connected라는 가정으로부터 $f_i$는 상수함수여야 하는 것을 안다. 따라서 귀납법에 의하여, 유한 개를 제외한 성분이 모두 $a$와 같은 $X$의 점 $x$들은 $f(x)=f(a)$를 만족해야 한다는 것을 안다. 이러한 점들은 $X$의 dense subset이므로, $f$는 $X$ 전체에서 상수함수여야 하고 이는 모순이다. 

</details>

## 연결성분

한편 고정된 $x\in X$에 대하여, $x$를 포함하는 connected set들의 모임은 [명제 3](#prop3)의 전제조건을 만족하고 따라서 $x$를 포함하는 가장 큰 connected set이 말이 된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $X$의 점 $x\in X$를 포함하는 *connected component<sub>연결성분</sub>*는 $x$를 포함하는 $X$의 connected subset 중 가장 큰 것이다. 만일 $X$의 임의의 점 $x$를 포함하는 connected componenet가 항상 $\\{x\\}$ 자기자신이라면 $X$를 *totally disconnected*라 부른다.

</div>

정의에 의하여, 만일 $X$가 connected라면 $X$는 유일한 connected component를 갖는다. 더 일반적으로 임의의 $X$는 connected component들의 합집합

$$X=\bigcup_{i\in I} U_i$$

으로 나타낼 수 있다. 한편 [명제 2](#prop2)에 의하여 각각의 $U_i$들은 반드시 닫힌집합이어야 한다. 만일 $I$가 유한집합이라면, $U_i$들은 모두 열린집합인 동시에 닫힌집합이어야 함을 안다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 위상공간 $X$ 위에 동치관계 $\sim$을

$$x\sim y\iff \text{$x$ and $y$ lies in the same component}$$

로 정의하자. 그럼 $X/{\sim}$은 totally disconnected이다.

</div>

이에 대한 증명은 자명하다.

## 국소연결공간

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 위상공간 $X$가 점 $x\in X$에서 *locally connected<sub>국소연결</sub>*이라는 것은 $x$의 임의의 근방 $U$가 주어질 때마다, $U$에 속하는 $x$의 connected neighborhood가 존재하는 것이다. 모든 점에서 locally connected인 공간을 간단히 locally connected space라 부른다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $X$가 locally connected인 것과, $X$의 열린집합을 포함하는 임의의 component가 항상 open인 것이 동치이다. 

</div>