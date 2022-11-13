---

title: "위상공간의 다른 정의들"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/equivalent_formulation_of_topology
header:
    overlay_image: /assets/images/Topology/Equivalent_formulation_of_topology.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-09
last_modified_at: 2022-11-09
weight: 4

---

우리는 지금까지 위상수학의 기초적인 내용을 다뤘다. 역사적으로 보았을 때, 열린집합들의 모임 $\mathcal{T}$를 위상공간으로 정의하는 것은 그렇게까지 오래되지는 않았고, 여러 정의가 존재해왔다. 현재에도 연구분야에 따라 이들 정의들이 유용할 때가 있다. 이번 글에서는 지금까지 살펴본 개념들을 사용하여 다른 방식으로 위상수학을 정의하는 법을 살펴본다. 

## 닫힌집합

[§집합의 내부, 폐포, 경계, 명제 2](/ko/math/topology/other_concepts#pp2)에 의하여, 집합 $X$ 위에 <em_ko>어떠한 집합이 닫힌 집합인지</em_ko>를 알려주는 집합들의 모임 $\mathcal{C}$를 정의하는 것으로 $X$에 위상구조를 줄 수 있다. 이는 원래의 정의와 거의 다르지 않지만, 특히 대수기하학에서 Zariski topology를 정의할 때 유용하게 사용할 수 있다.

## Closure axiom

<div class="definition" markdown="1">

<ins id="df1">**정의 1 (Kuratowski closure axiom)**</ins> 임의의 <em_ko>집합</em_ko> $X$에 대하여, 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 다음의 조건들을 모두 만족한다 하자.

- $A\subset\operatorname{cl}(A)$
- $\operatorname{cl}(\operatorname{cl}(A))=\operatorname{cl}(A)$
- $\operatorname{cl}(A\cup B)=\operatorname{cl}(A)\cup\operatorname{cl}(B)$
- $\operatorname{cl}(\emptyset)=\emptyset$

이 조건들을 만족하는 함수를 *closure operator*라 부른다. ([집합론, §필터와 아이디얼, 갈루아 대응, 정의 8](/ko/math/set_theory/filter_and_ideal#df8))

</div>

세 번째 조건으로부터, 만일 $A\subseteq B$라면

$$\operatorname{cl}(A)\subset\operatorname{cl}(A)\cup\operatorname{cl}(B)=\operatorname{cl}(A\cup B)=\operatorname{cl}(B)$$

임을 알 수 있다. 

임의의 위상공간 $X$에 대하여, $X$의 임의의 부분집합 $A$를 $A$의 closure로 보내는 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 위의 조건을 만족한다는 것은 자명하다. 

거꾸로 임의의 집합 $X$ 위에 위의 조건을 만족하는 closure operator $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$이 주어졌다 하자. 이제 $\mathcal{P}(X)$의 원소들 중 $\operatorname{cl}(C)=C$를 만족하는 집합들의 모임을 $\mathcal{C}$로 적자. 그러면

- $\operatorname{cl}(\emptyset)=\emptyset$이므로, $\emptyset\in\mathcal{C}$이다. 한편 $X\subset\operatorname{cl}(X)$이므로 $\operatorname{cl}(X)=X$이고 따라서 $X\in\mathcal{C}$이다.
- 임의의 $A,B\in\mathcal{C}$에 대하여, $A\cup B=\operatorname{cl}(A)\cup\operatorname{cl}(B)=\operatorname{cl}(A\cup B)$가 성립하므로 $A\cup B\in\mathcal{C}$가 성립한다. 
- 임의의 index set $I$와 $A_i\in\mathcal{C}$들에 대하여, $\bigcap A_i\subset\operatorname{cl}(\bigcap A_i)$이고, 또 $\bigcap A_i\subseteq A_i$으로부터 

  $$\operatorname{cl}(\bigcap A_i)\subset\operatorname{cl}(A_i)=A_i$$

  가 성립하므로 $\operatorname{cl}(\bigcap A_i)\subset\bigcap A_i$ 또한 성립한다.

이로부터 다음의 정리가 얻어진다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> [정의 1](#df1)의 조건을 모두 만족하는 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 주어졌다 하자. $\mathcal{C}$를 <phrase>$\operatorname{cl}(C)=C$를 만족하는 모든 $C$들의 모임</phrase>으로 정의하면, $\mathcal{C}$는 [§집합의 내부, 폐포, 경계, 명제 2](/ko/math/topology/other_concepts#pp2)의 조건을 모두 만족하며 따라서 유일한 위상구조를 정의한다.

</div>

물론 집합의 interior를 이용하여도 어렵지 않게 위상구조를 하나 정의할 수 있다. 이 경우, interior operator $\operatorname{int}$가 만족해야 할 공리들은 다음과 같다.

<div class="misc" markdown="1">

**Interior axiom.** 임의의 집합 $X$에 대하여, 함수 $\operatorname{int}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 다음의 조건들을 만족한다 하자.

- $\operatorname{int}(A)\subseteq A$
- $\operatorname{int}(\operatorname{int}(A))=\operatorname{int}(A)$
- $\operatorname{int}(A\cap B)=\operatorname{int}(A)\cap\operatorname{int}(B)$
- $\operatorname{int}(X)=X$

이 조건들을 만족하는 함수를 *interior operator*라 부른다.

</div>

## Neighborhood filter

우리는 [§열린집합, 명제 6](/ko/math/topology/open_sets#pp6)에서 각 점 $x$마다 *neighborhood filter* $\mathcal{N}(x)$를 주면, 이 정보 또한 유일한 방식으로 $X$에 위상구조를 준다는 것을 확인했다. 해당 명제에서 $\mathcal{N}(x)$가 만족해야 할 첫 번째부터 세 번째 조건은 filter의 조건이며, 다음 정의 또한 이미 정의하였던 것이지만 나중의 reference를 위해 남겨둔다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 집합 $X$ 위에서 정의된 *filter*라는 것은 다음의 세 조건을 만족하는 $\mathcal{P}(X)$의 부분집합 $\mathcal{F}$를 뜻한다.

1. $\mathcal{F}$의 원소를 포함하는 $X$의 부분집합은 $\mathcal{F}$에 속한다.
2. $\mathcal{F}$의 원소들의 유한한 교집합은 $\mathcal{F}$에 속한다.
3. $\emptyset\not\in\mathcal{F}$이다.

</div>

Ordered set $(\mathcal{P}(X),\subseteq)$를 생각하면, 위 정의는 [집합론, §필터와 아이디얼, 갈루아 대응, 정의 1](/ko/math/set_theory/filter_and_ideal#df1)에서 정의한 것과 동일하지만 조건 $\emptyset\not\in\mathcal{F}$가 추가된 것으로 생각할 수 있다. 그럼 $\mathcal{N}(x)$가 만족해야 할 네 가지 조건 중 앞의 세 가지는 $\mathcal{N}(x)$가 모든 $x$에 대하여 filter 구조를 갖는다는 것으로 축약할 수 있다. 네 번째 조건은 별도로 이름을 갖는다.

<div class="misc" markdown="1">

**Neighborhood axiom.** 임의의 $z\in X$와, 각각의 원소가 $z$를 포함하는 $X$의 filter $\mathcal{N}(z)$가 주어졌다 하자. 그럼 임의의 $S\in\mathcal{N}(z)$마다 적당한 $S'\in\mathcal{N}(z)$가 존재하여, <phrase>임의의 $x\in S'$마다 $S\in\mathcal{N}(x)$</phrase>가 성립하도록 할 수 있다.

</div>

뿐만 아니라, $\mathcal{N}(x)$를 local base와 같은 역할을 한다고 생각하면, 이를 통해 위상공간이 basis $\mathcal{B}$를 통해서도 정의됨을 보일 수 있었다. ([§위상공간의 기저, 따름정리 6](/ko/math/topology/topological_basis#crl6))

서두에서 말한 것과 같이, 이번 글은 본질적으로는 우리가 그 동안 다뤄왔던 개념들을 다른 방식으로 적은 것에 불과하다. 다른 분야, 특히 해석학에서 많이 쓰이는 일반화는 지금까지 살펴본 내용과는 별개의 것이며 이를 제대로 살펴보기 위해서는 약간 더 기다릴 필요가 있다. <#ref#>

