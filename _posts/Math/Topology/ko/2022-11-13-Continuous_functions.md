---

title: "연속함수"
excerpt: "연속함수의 성질들"

categories: [Math / Topology]
permalink: /ko/math/topology/continuous_functions
header:
    overlay_image: /assets/images/Topology/Continuous_functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-11-13
last_modified_at: 2022-11-13
weight: 5

---

## 연속함수

이제 우리는 연속함수의 개념을 정의한다. 직관적으로 이는 대수적인 설정에서의 homomorphism과 마찬가지로 위상구조를 보존하는 함수라 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 위상공간 $X$, $Y$ 사이의 함수 $f:X\rightarrow Y$가 $x\in X$에서 *연속<sub>continuous</sub>*이라는 것은 $f(x)\in Y$의 임의의 근방 $V$에 대하여, $f(U)\subseteq V$이도록 하는 $x$의 근방 $U$가 존재하는 것이다. 

</div>

임의의 집합 $X,Y$ 사이의 함수 $f:X\rightarrow Y$와 임의의 $U\subseteq X$에 대하여 $U\subseteq f^{-1}(f(U))$가 성립하므로, 임의의 집합 $V\subseteq Y$가 $f(U)\subseteq V$를 만족한다면 

$$U\subseteq f^{-1}(f(U))\subseteq f^{-1}(V)$$

이 성립한다. 따라서 두 위상공간 사이의 함수 $f:X\rightarrow Y$가 $x\in X$에서 연속이라는 것을 증명하기 위해서는 $f(x)\in Y$의 임의의 근방 $V$에 대하여 $f^{-1}(V)$가 $x$의 근방이 된다는 것을 보이면 충분하며, 더 일반적으로는 고정된 $f(x)$의 local base $\mathcal{B}(f(x))$와 임의의 $V\in\mathcal{B}(f(x))$에 대하여 $f^{-1}(V)\in\mathcal{N}(x)$임을 보이면 충분하다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 두 위상공간 $X,Y$ 사이의 함수 $f:X\rightarrow Y$가 점 $x$에서 연속이라 하자. 만일 어떠한 $A\subseteq B$에 대하여 $x\in\cl(A)$라면, $f(x)\in\cl(A)$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f(x)\in Y$의 임의의 근방 $V$를 택하자. 그럼 $f^{-1}(V)$는 $x$의 근방이므로 $f^{-1}(V)\cap A\neq\emptyset$이고 ([§집합의 내부, 폐포, 경계, ⁋명제 6](/ko/math/topology/other_concepts#pp6)), $x'\in f^{-1}(V)\cap A$라 하면 $f(x')\in V\cap f(A)$이다. 특히 $V\cap f(A)\neq\emptyset$이므로, 다시 [§집합의 내부, 폐포, 경계, ⁋명제 6](/ko/math/topology/other_concepts#pp6)를 적용하면 $f(x)\in\cl(A)$임을 안다.

</details>

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 위상공간들 $X,Y,Z$가 주어졌다고 하자. 만일 $f:X\rightarrow Y$가 점 $x\in X$에서 연속이고, $g:Y\rightarrow Z$가 $f(x)$에서 연속이라면 그 합성 $g\circ f$ 또한 연속이다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(g\circ f)(x)$의 임의의 근방 $W$를 택하자. 그럼 $g$가 $f(x)$에서 연속이므로, $g^{-1}(W)$은 $f(x)$의 근방이다. 다시 $f$는 $x$에서 연속이므로, $f^{-1}(g^{-1}(W))$는 $x$의 근방이다. ([\[집합론\] §이항관계의 그래프, ⁋명제 13](/ko/math/set_theory/binary_relation#pp13))

</details>

만일 $f$가 $X$의 모든 점에서 연속이라면, $f$를 *연속함수<sub>continuous function</sub>*라 부른다. 다음 정리는 연속함수를 정의하는 여러 방법을 보여준다.

<div class="proposition" markdown="1">

<ins is="thm4">**정리 4**</ins> 두 위상공간 $X,Y$와 함수 $f:X\rightarrow Y$에 대하여, 다음이 모두 동치이다.

1. $f$가 연속이다. 
2. $X$의 임의의 부분집합 $A$에 대하여, $f(\cl A)\subset\cl f(A)$가 성립한다.
3. $Y$의 임의의 닫힌집합 $C$에 대하여, $f^{-1}(C)$가 $X$에서 닫힌집합이다.
4. $Y$의 임의의 열린집합 $V$에 대하여, $f^{-1}(V)$가 $X$에서 열린집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 조건이 성립하면 두 번째 조건 또한 성립한다는 것은 [명제 2](#pp2)의 결과이다.

이제 둘째 조건을 가정하고 세 번째 조건을 보이자. $Y$의 임의의 닫힌집합 $C$에 대하여, 다음 포함관계

$$f(\cl(f^{-1}(C))\subseteq \cl(f(f^{-1}(C))\subseteq\cl(C)=C$$

가 성립하므로,

$$\cl(f^{-1}(C))\subseteq f^{-1}(f(\cl(f^{-1}(C)))\subseteq f^{-1}(C)$$

로부터 $f^{-1}(C)$가 닫힌집합이라는 것을 안다. 식 $(f^{-1}(A))^c=f^{-1}(A^c)$가 임의의 부분집합 $A\subseteq Y$에 대해 성립하므로, 이로부터 넷째 조건 또한 얻어진다는 것이 자명하다. 

따라서 넷째 조건을 가정하고 첫 번째 조건을 보이면 충분하다. $x\in X$를 임의로 택하고, $f(x)\in Y$의 임의의 근방 $V$가 주어졌다 하자. 그럼 $f(x)\subseteq V'\subseteq V$를 만족하는 $f(x)$의 <em_ko>열린근방</em_ko> $V'$이 존재한다. 이제 넷째 조건으로부터, $f^{-1}(V')$는 $x\in X$의 열린근방이고, $f^{-1}(V')\subseteq f(V)$로부터 $f(V)$가 $x$의 근방이 됨을 안다.

</details>

[명제 3](#pp3)에 의하여, 두 연속함수 $f:X\rightarrow Y$, $g:Y\rightarrow Z$가 주어진다면 $g\circ f$ 또한 연속이라는 것을 안다. 

두 위상공간 $(X,\mathcal{T}\_X), (Y,\mathcal{T}\_Y)$ 사이의 연속함수 $f:X\rightarrow Y$가 주어졌다 하자. 그럼 임의의 $V\in\mathcal{T}\_Y$에 대하여 $f^{-1}(V)\in\mathcal{T}\_X$가 성립하므로, 다음의 식

$$f^\mathcal{T}(V):=f^{-1}(V),\qquad V\in\mathcal{T}_Y$$

이 함수 $f^\mathcal{T}:\mathcal{T}_Y\rightarrow\mathcal{T}_X$를 잘 정의한다.

이제 $f$가 전단사함수라 가정하고 $\mathcal{T}\_Y$의 서로 다른 두 원소 $V\_1,V\_2$를 생각하자. 일반성을 잃지 않고 $y\in V\_1\setminus V\_2$라 하면 

$$f^{-1}(y)\in f^\mathcal{T}(V_1)\setminus f^\mathcal{T}(V_2)$$

가 성립하므로 $f^{\mathcal{T}}$는 단사함수가 된다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 일반적으로 $f^{\mathcal{T}}$가 전사함수가 될 필요는 없다. 가령 $\mathbb{N}$에 discrete topology를 준 공간을 $X$, trivial topology를 준 공간을 $Y$라 한 후, 집합으로서의 항등함수 $\id:\mathbb{N}\rightarrow\mathbb{N}$을 생각하면 $\id$는 연속인 전단사함수이지만 함수

$$\id^\mathcal{T}:\mathcal{T}_Y\rightarrow\mathcal{T}_X$$

는 전사함수가 될 수 없다. ([\[집합론\] §기수, ⁋명제 15](/ko/math/set_theory/cardinals#pp15))

</div>

그러나 만일 전단사함수 $f$의 역함수 $f^{-1}$ 또한 연속함수라면 $(f^{-1})^\mathcal{T}:\mathcal{T}_X\rightarrow\mathcal{T}_Y$가 잘 정의되며 정의로부터

$$f^\mathcal{T}\circ (f^{-1})^\mathcal{T}=\id_{\mathcal{T}_X},\qquad (f^{-1})^\mathcal{T}\circ f^\mathcal{T}=\id_{\mathcal{T}_Y}$$

임이 자명하므로 $f^\mathcal{T}$ 또한 전단사함수가 된다. 이와 같은 상황을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 연속함수 $f:X\rightarrow Y$가 *homeomorphism<sub>위상동형사상</sub>*이라는 것은, 또 다른 연속함수 $g:Y\rightarrow X$가 존재하여 $f\circ g=\id_Y$이고 $g\circ f=\id_X$인 것이다.
</div>

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
