---

title: "옹골성"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/compactness
header:
    overlay_image: /assets/images/Math/Topology/Compactness.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
last_modified_at: 2024-12-15
weight: 16

---

이제 우리는 옹골성과 관련된 남은 결과들 및 이 정의의 변주들을 살펴본다. 

## Tychonoff theorem

Compact space의 임의의 product는 다시 compact space가 된다. 만일 이 product가 유한이라면 이 결과는 보다 직관적인 방식으로 보일 수 있지만, 이 product가 무한하다면 이를 위해서는 다음 보조정리가 필요하다. 이는 [§옹골성과 필터의 수렴, ⁋명제 5](/ko/math/topology/filter_convergence#prop5)를 filter의 언어로 일반화한 것이다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 위상공간 $X$가 compact인 것은 임의의 ultrafilter가 수렴하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$가 compact라 가정하고, 임의의 ultrafilter $\mathcal{F}$가 주어졌다 하자. 결론에 반하여 $\mathcal{F}$의 limit point가 존재하지 않는다 하자. 즉, 어떠한 $x\in X$에 대해서도 열린근방 $U_x$가 존재하여 $U_x\not\in \mathcal{F}$이도록 할 수 있다. 그럼 $X$의 compactness에 의하여 $X$의 유한한 subcover $U_{x\_1},\ldots, U_{x\_n}$이 존재한다. 

한편 [\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋명제 5](/ko/math/set_theory/filter_and_ideal#prop5)에 의하여 $\mathcal{F}$는 prime이다. 즉, 임의의 부분집합 $A\subseteq X$에 대하여, $A\in \mathcal{F}$ 혹은 $X\setminus A\in \mathcal{F}$ 중 정확히 하나가 성립한다. 그럼 이제 임의의 $A\in \mathcal{F}$에 대하여,

$$A=A\cap X=(A\cap U_{x_1})\cup \cdots\cup (A\cap U_{x_n})\in \mathcal{F}$$

이며, 가정에 의하여 $U_{x\_i}\not\in \mathcal{F}$이므로 각각의 $A\cap U_{x\_i}$들도 $\mathcal{F}$에 속하지 않으며 $\mathcal{F}$가 maximal이므로 $X\setminus (A\cap U\_{x_i})\in \mathcal{F}$여야 한다. 그럼 이들의 유한한 교집합

$$X\setminus A=(X\setminus (A\cap U_{x_1}))\cap\cdots\cap (X\setminus (A\cap U_{x_n}))$$

도 $\mathcal{F}$에 속해야 하므로, 이는 $\mathcal{F}$가 maximal이라는 가정에 모순이다. 

거꾸로 임의의 ultrafilter $\mathcal{F}$가 주어질 때마다 limit point $x$를 찾을 수 있다 하고, finite intersection property를 만족하는 $X$의 닫힌집합들의 family $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$에 의해 생성되는 filter를 포함하는 ultrafilter $\mathcal{F}$를 생각할 수 있으며, 가정에 의해 $\mathcal{F}$는 limit point $x$를 가진다. 즉 $\mathcal{N}(x)\subseteq \mathcal{F}$이며, 따라서 임의의 $F\in \mathcal{F}$마다 적당한 $x$의 근방 $U$가 존재하여 $U\cap F\neq\emptyset$이다. 특히 임의의 $A\in \mathcal{A}$에 대하여 $A\cap U\neq\emptyset$이도록 할 수 있는 $x$의 근방 $U$가 존재하며, 따라서 $x\in \cl(A)=A$가 항상 성립한다. 이로부터 $x\in\bigcap_{A\in \mathcal{A}}A$임을 알고, 따라서 [§옹골공간, ⁋명제 11](/ko/math/topology/compact_spaces#prop11)에 의해 원하는 결과를 얻는다.

</details>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Tychonoff)**</ins> Compact space들 $(X\_i)\_{i\in I}$의 product $X=\prod_{i\in I} X\_i$는 compact이다. 거꾸로, 만일 product space $X$가 compact라면, 각각의 $X\_i$들이 모두 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $X$가 compact라면, 각각의 $X\_i$들이 모두 compact라는 것은 $\pr\_i$의 연속성과 [§옹골공간, ⁋명제 8](/ko/math/topology/compact_spaces#prop8)에 의해 자명하다.

반대 방향은 $X$ 위에 정의된 임의의 ultrafilter $\mathcal{F}$에 대하여, $\pr\_i(\mathcal{F})$가 $X\_i$의 ultrafilter base를 정의한다는 것을 확인한 후, $X\_i$가 compact라는 가정과 [보조정리 1](#lem1)로부터 이 ultrafilter의 limit point $x\_i$를 얻고, $x=(x\_i)\_{i\in I}$가 $\mathcal{F}$의 limit point임을 보일 수 있으므로 다시 [보조정리 1](#lem1)에 의해 증명이 완료된다. 

</details>

## 국소적 옹골공간

공간 $X$가 compact인 것은 너무나 좋은 성질이라 우리가 다루는 공간들이 compact가 아닌 경우가 많다. 가령 실수집합 $\mathbb{R}$만 보아도, $(n,n+2)$로 이루어진 open cover들을 생각하면 compact가 아니다. 따라서 이 조건은 다소 약화시킬 필요가 있다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 위상공간 $X$가 점 $x\in X$에서 *locally compact<sub>국소적으로 옹골</sub>*라는 것은 $x$를 포함하는 $X$의 compact neighborhood $A$가 존재하는 것이다. 만일 $X$가 모든 점에서 locally compact라면, 이를 *locally compact space<sub>국소적 옹골공간</sub>*이라 부른다. 

</div>

그럼 [§옹골공간, ⁋보조정리 6](/ko/math/topology/compact_spaces#lem6)과 비슷한 증명으로 임의의 locally compact Hausdorff space는 regular라는 것을 보일 수 있다. 다음 정리는 locally compact Hausdorff space에 대한 중요한 정보를 준다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Alexandroff)**</ins> Locally compact Hausdorff space $X$가 주어졌다 하자. 그럼 compact Hausdorff space $X'$와 한 점 $\ast_{X'}\in X'$, 그리고 homeomorphism $f: X \rightarrow X'\setminus\\{\ast_{X'}\\}$가 존재한다. 뿐만 아니라, 만일 이 조건을 만족하는 또 다른 데이터 $g: X \rightarrow X''\setminus\\{\ast_{X''}\\}$가 주어졌다 하면, 유일한 homeomorphism $h: X' \rightarrow X''$가 존재하여 $g=h\circ f$이도록 할 수 있다. 

</div>

증명을 조금 더 직관적으로 하기 위해 주장을 조금 덜 엄밀한 방법으로 이야기하자면, locally compact Hausdorff space가 주어진다면 여기에 한 점을 더해 이를 compact Hausdorff space로 만들 수 있으며, 이렇게 한 점을 추가하는 방법은 유일하다고 할 수 있다. 이렇게 얻어진 새로운 공간을 $X$의 *one-point compactification*이라 부르기도 한다.

<details class="proof--alone" markdown="1">
<summary>정리 4의 증명</summary>

우선 유일성을 보이자. $h$는 당연히 $X'\setminus\\{\ast\_{X'}\\}$에서는 $f(x)$를 $g(x)$로 보내고, $\ast\_{X'}$는 $\ast_{X''}$로 보내도록 정의하는 것이 자연스러울 것이다. 그럼 $h$는 연속이다. 이를 증명하기 위해 $X''$의 임의의 열린집합 $V$가 주어졌다 하자. 만일 $V$가 $\ast_{X''}$를 포함하지 않는다면, 정의에 의하여

$$h^{-1}(V)=f(g^{-1}(V))$$

이며 $f$가 homeomorphism이므로 $h^{-1}(V)$는 $X'\setminus\\{\ast\_{X'}\\}$안에서 열린집합이다. 한편 $X'\setminus\\{\ast\_{X'}\\}$는 $X'$가 Hausdorff space라는 가정으로부터 열린집합이므로 [§부분공간, ⁋보조정리 2](/ko/math/topology/subspaces#lem2)에 의하여 $h^{-1}(V)$는 $X'$의 열린집합이다. 

만일 $V$가 $\ast_{X'}$를 포함한다면, $X''\setminus V$는 $X''$의 닫힌집합이므로 compact인 부분집합이고, 따라서 $f(X)$의 compact인 부분집합이기도 하다. 이제 $g$가 homeomorphism인 것으로부터 $g^{-1}(X''\setminus V)$는 $X$의 compact subspace이고, 따라서 다음 집합

$$h^{-1}(X''\setminus V)=f(g^{-1}(X''\setminus V))$$

은 $X'$의 compact subspace이므로 닫힌집합이다. ([§옹골공간, ⁋따름정리 5](/ko/math/topology/compact_spaces#cor5)) 따라서 [§연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)의 세 번째 조건으로부터 $h$가 연속임을 안다.

위의 증명으로부터, 만일 주어진 조건을 만족하는 위상공간 $X'=X\cup \\{\ast_{X'}\\}$가 존재한다면, $X'$의 열린집합은 다음의 두 종류

$$f(U)\quad\text{for $U$ open in $X$},\qquad X'\setminus f(C)\quad\text{for $C$ compact in $X$}$$

의 꼴이어야 한다는 것을 안다. 그럼 실제로 이것이 [§열린집합, ⁋정의 1](/ko/math/topology/open_sets#def1)의 조건을 만족하는 것을 쉽게 보일 수 있다. 남은 것은 이렇게 주어진 위상구조가 compact Hausdorff임을 보이는 것 뿐이다. 

우선 $X'$가 compact라는 것을 보이자. $X'$의 임의의 open covering $(U_i)\_{i\in I}$이 주어진다면, 이 family에는 $\ast_{X'}$를 포함하는 열린집합 $U_j$이 존재해야 하며, 위에서 정의한 위상구조에 의하여 이는 $X$의 compact subset $C$에 대해 $U_j=X'\setminus C$로 적을 수 있다. 한편, $X$의 열린집합들의 모임 $(f^{-1}(U_i))\_{i\neq j}$를 생각하자. 그럼 $(U\_i)\_{i\neq j}$들이 $f(C)$를 덮어야 하므로 $(f^{-1}(U_i))\_{i\neq j}$는 $C$의 open covering이고, $C$가 compact라는 가정으로부터 finite subcover를 택하여 이로부터 $X'$의 open covering $(U_i)\_{i\in I}$의 finite subcover를 얻을 수 있다.

이제 $X'$가 Hausdorff임을 보이기 위해 $X'$의 임의의 두 점 $x,y\in X'$가 주어졌다 하자. 이들 둘이 모두 $f(X)$에 속한다면 증명할 것이 없으므로, $y=\ast_{X'}$라 가정할 수 있다. 그럼 $x$를 포함하는 $X$의 compact neighborhood $C$와 $C$에 속하는 $x$의 열린근방 $U$가 존재하므로, $f(U)$와 $X'\setminus f(C)$가 $x,y$를 분리하는 열린집합이 된다.

</details>

## 위상다양체

이번에는 옹골성에서 요구하는 유한성을 다소 약화시켜보자. 가령 위상공간 $X$의 임의의 open covering이 *locally* finite open subcover를 갖는 상황을 생각할 수 있다. ([§집합의 내부, 폐포, 경계, ⁋정의 3](/ko/math/topology/other_concepts#def3)) 그런데 약간의 말장난을 통해 이 조건은 사실 $X$의 compactness와 동치임을 보일 수 있으므로 이것만으로는 새로운 정의가 나오지 않는다. 이제 우리는 위상공간 두 open cover $(U\_i)\_{i\in I}$와 $(V\_j)\_{j\in J}$에 대하여, 임의의 $V\_j$를 온전히 포함하는 $U\_i$가 항상 존재한다면 $(V\_j)\_{j\in J}$가 $(U\_i)\_{i\in I}$의 *(open) refinement*라 부르기로 한다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 위상공간 $X$가 *paracompact*라는 것은 $X$의 임의의 open covering이 locally finite open refinement를 갖는 것이다. 

</div>

만일 $X$가 compact라면, 임의의 open covering의 finite subcover가 곧 locally finite open refinment가 되므로 임의의 compact space는 paracompact이다. 

우리가 다루는 거의 모든 공간은 Hausdorff space이다. 별도로 증명을 하지는 않지만, paracompact Hausdorff space를 특징짓는 중요한 성질 중 하나는 *partition of unity*의 존재성이다. ([정리 7](#thm7))

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 위상공간 $X$가 주어졌다 하자. 그럼 연속함수들의 집합

$$\Phi=\{\phi:X \rightarrow [0,1]\mid \text{$\phi$ continuous}\}$$

이 *partition of unity<sub>단위분할</sub>*이라는 것은 다음의 두 조건

1. 임의의 $x\in X$에 대하여, 적당한 열린근방 $U$가 존재하여 $\phi\vert_U\neq 0$을 만족하는 $\phi\in \Phi$가 오직 유한 개 뿐이도록 할 수 있다.
2. 임의의 $x\in X$에 대하여, $\sum_{\phi\in \Phi} \phi(x)=1$이 성립한다.

이 성립하는 것이다. 특별히 $X$의 open covering $(U\_i)\_{i\in I}$에 대하여, $\supp \phi_i\subseteq U_i$를 만족하는 partition of unity $\Phi=(\phi\_i)\_{i\in I}$를 *partition of unity subordinate to $(U_i)$*라 부른다. 

</div>

즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 위상공간 $X$가 paracompact Hausdorff space인 것과, $X$의 임의의 open cover $(U_i)$에 대하여 partition of unity subordinate to $(U_i)$가 존재하는 것이 동치이다.

</div>

이에 대한 증명은 [위키피디아](https://en.wikipedia.org/wiki/Paracompact_space)에서 확인할 수 있다. 이를 그대로 옮겨적는 대신 이것이 어떠한 방식으로 사용되는지를 간략히 살펴보자. 이를 위해 우선 위상다양체를 정의한다. 위상다양체의 모델은 우리가 잘 알고 있는 공간, 곧 Euclidean space $\mathbb{R}^m$이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 위상공간 $M$이 *locally Euclidean of dimension $m$*이라는 것은 임의의 $x\in M$이 주어질 때마다 $x$의 적당한 열린근방 $U$가 존재하여 $U$가 $\mathbb{R}^m$의 열린집합과 homeomorphic한 것이다. 

</div>

이 조건이 위상다양체의 본질이지만, 생각보다는 약한 조건이므로 우리는 여기에 몇몇 조건을 추가한다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Second countable, Hausdorff, locally Euclidean of dimension $m$인 공간을 *topological manifold of dimension $m$*이라 부른다. 

</div>

그럼 증명없이 언급할 또 다른 정리로 다음이 있다. 

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> 임의의 Hausdorff locally Euclidean topological space $M$에 대하여, $M$이 second-countable인 것과, $M$이 paracompact이고 countable하게 많은 connected component를 갖는 것이 동치이다. ([§연결공간, ⁋정의 7](/ko/math/topology/connected_spaces#def7))

</div>

우리는 아직 connected component가 무엇인지 정의하지 않았지만, 어쨌든 위의 정리는 논리적으로 임의의 topological manifold $M$은 paracompact Hausdorff이고, 따라서 topological manifold $M$의 임의의 open cover $(U_i)$에 대하여 partition of unity subordinate to $(U_i)$가 존재한다는 것을 함의한다. 특히 우리는 locally Euclidean 조건을 활용하여 open cover $(U_i)$를 Euclidean space로 볼 수 있는데, 그럼 이 위에서 정의된 $\mathbb{R}$로의 연속함수라는 것은 우리가 미적분학을 배울 때부터 알고 있는 대상이다. 그럼 다음의 식 

$$f=\sum \phi_i f_i$$

을 통해 $M$ 전체에서 정의된 연속함수 $f$를 정의할 수 있으며 거꾸로 $M$ 전체에서 정의된 연속함수 $f$가 주어졌다 하면 각각의 $\phi_i f$가 $U_i$ 위에서 정의된 연속함수이다. 대부분의 경우 topological manifold는 단 하나의 connected component를 갖는 것으로 생각해도 별 문제가 없으므로, 사실상 paracompactness가 manifold를 다룰 때 필수적인 조건이라 생각할 수 있다. 