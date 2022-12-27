---

title: "동치관계"
excerpt: "동치관계의 정의와 성질들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/equivalence_relations
header:
    overlay_image: /assets/images/Set_theory/Equivalence_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2021-08-22
last_modified_at: 2022-11-26
weight: 12

---

이제 우리는 동치관계에 대해 살펴본다. 

## 동치관계의 정의

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 이항관계 $(R,A,A)$가 *symmetric<sub>대칭적</sub>*이라는 것은 $x\mathrel{R}y$가 성립하면 $y\mathrel{R}x$도 성립하는 것이다. 만일 

$$(x\mathrel{R}y)\wedge(y\mathrel{R}z)\implies  x\mathrel{R}z$$

가 성립할 경우, 이를 *transitive<sub>추이적</sub>*라고 한다. 마지막으로 모든 $x$에 대하여 $x\mathrel{R}x$일 경우, $R$이 $A$ 위에서 *reflexive<sub>반사적</sub>*라고 한다. Reflexive, symmetric, transitive한 관계 $R$을 *동치관계<sub>equivalence relation</sub>*라 부른다. 
</div>

앞으로 $R$이 동치관계일 경우 $x\sim_{\tiny R}y$를 사용하기로 한다. 혼동의 여지가 없을 때에는 $x\sim y$ 혹은 $x\equiv y$와 같이 적기도 한다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 주어진 집합 $A$ 위에서 관계 <phrase>$x=y$</phrase>는 $A$ 위에서의 동치관계가 되며, 이 때 $R$은 집합 $\Delta_A$와 같다. 한편, 관계 <phrase>$x\in A$이고 $y\in A$</phrase>또한 $A$ 위에서의 동치관계가 된다는 것을 쉽게 확인할 수 있다. 이 관계를 나타내는 집합은 정확하게 $A\times A$와 같다.

집합 $A$ 위에 주어진 임의의 동치관계 $R$을 생각하자. $R$은 reflexive하므로 $\Delta_A\subseteq R$이며, 포함관계 $R\subseteq A\times A$가 성립하는 것은 자명하다. 따라서 위에서 든 두 가지의 예시 중 첫 번째는 $A$ 위에서 정의할 수 있는 동치관계 중 가장 작은 것이고, 두 번째는 가장 큰 것이다.

</div>

이를 식으로 정리하면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 이항관계 $(R,A,A)$가 동치관계인 것은 다음의 세 조건

$$\pr_1R=A,\qquad R=R^{-1},\qquad R\circ R=R$$

과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $R$이 동치관계라 가정하자.  
- 모든 $x\in A$에 대하여 $(x,x)\in R$이므로 $\pr\_1R=A$가 성립한다.  
- 또, $R$은 symmetric이므로 $x\sim_\tiny{R} y\iff y\sim_\tiny{R}x$가 성립하고 따라서
    
    $$(x,y)\in R\iff (y,x)\in R\iff (x,y)\in R^{-1}\tag{1}$$

    로부터 $R=R^{-1}$이 성립한다. 
- 마지막으로 $R\circ R=R$임을 보여야 한다. 우선 임의의 $(x,y)\in R$이 주어졌다 하자. $R$이 reflexive하므로 $(x,x)\in R$이고, 따라서 $(x,x)\in R$, $(x,y)\in R$로부터 $(x,y)\in R\circ R$이 성립한다는 것을 안다. 거꾸로 임의의 $(x,y)\in R\circ R$가 주어졌다 하자. 그럼 어떠한 $z\in A$가 존재하여 $(x,z)\in R$이고 $(z,y)\in R$이다. 이제 $R$의 transitivity에 의하여 $(x,y)\in R$이 성립한다. 

이제 주어진 세 조건을 만족하는 이항관계 $R$이 주어졌다 하자.

- $R=R^{-1}$이 성립하는 것으로부터, 식 (1)의 논리를 거꾸로 하여 $R$이 symmetric임을 안다.
- $x\mathrel{R}y$와 $y\mathrel{R}z$가 성립한다 가정하자. 그럼 $(x,z)\in R\circ R=R$이므로 $R$이 transitive임을 안다.
- 마지막으로 $\pr_1R=A$인 것으로부터 적당한 $y\in A$가 존재하여 $(x,y)\in R$임을 안다. 이제 $R$은 symmetric이므로 $y\mathrel{R}x$ 또한 성립하고, transitivity로부터 $(x\mathrel{R}y)\wedge(y\mathrel{R}x)\implies x\mathrel{R}x$가 성립한다. 즉 $R$은 reflexive하다.

</details>

이번 글에서는 동치관계의 핵심적인 성질을 살펴보고, 다음 글에서는 여러가지 상황에서 등장하는 동치관계를 살펴본다.

## 동치관계와 분할

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 동치관계 $(R,A,A)$를 생각하자. 임의의 $x\in A$에 대하여, $x$에서의 section $R(x)$를 $R$에서 $x$의 *equivalence class<sub>동치류</sub>*라 부른다. 이러한 equivalence class들의 모임을 $R$의 *quotient set<sub>몫집합</sub>*이라 부르고, $A/R$로 표기한다.

</div>

정의에 의하여 $R(x)$는 동치관계 $R$에 의해 $x$와 동등한 것으로 취급되는 원소들의 모임이다. 많은 경우 $x$를 포함하는 equivalence class를 $[x]_R$로 적기도 한다. 혼동의 여지가 없을 경우, 이들의 집합 $A/R$을 $A/\mathord{\sim}$으로 표기하기도 한다.

![Quotient_set](/assets/images/Set_theory/Equivalence_relations-1.png){:width="600px" class="invert" .align-center}

<cap>집합 $A$ (왼쪽), 그 위에 정의된 동치관계 $R$ (가운데), 몫집합 $A/R$ (오른쪽). $A/R$의 각 원소는 중간 그림의 equivalence class $[x]_R$이다.</cap>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 집합 $A$ 위에서 <phrase>$x=y$</phrase>는 동치관계가 됨을 이미 살펴보았다. 이 관계에서 $x$의 equivalence class는 집합 $\{x\}$이다. 한편 동일한 예시에서 <phrase>$x\in A$이고 $y\in A$</phrase> 또한 동치관계였는데, 이 경우 $x$의 equivalence class는 $A$ 전체가 된다. 

우리는 앞선 [예시 2](#ex2)에서 $\Delta_A$가 가장 <em_ko>작고</em_ko>, $A\times A$가 가장 <em_ko>크다</em_ko>고 말했는데, 이렇게 집합간의 포함관계를 따지기보다는 위의 관점에 따라 $\Delta_A$가 가장 *finer*한 동치관계이고, $A\times A$는 가장 *coarser*한 동치관계라고 하는 것이 일반적이다. ([§집합의 합, ⁋정의 1](/ko/math/set_theory/sum_of_sets#df1))

</div>

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 동치관계 $(R,A,A)$에 대하여 $p:A\rightarrow A/R$을 $x\mapsto [x]\_R$로 정의하자. 그럼 $p$는 함수이며, $x\sim\_{\tiny R} y$와 $p(x)=p(y)$는 서로 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 위의 식으로 정의된 $p$가 실제로 함수가 된다는 것은 어렵지 않게 보일 수 있다. 여기에서는 동치관계만 보인다.

우선 $x\sim\_{\tiny R} y$이라 가정하자. 그럼 $y\in [x]\_R=R(x)$로부터 $\\{y\\}\subseteq R(x)$이고, 따라서 [§이항관계들 사이의 연산, ⁋명제 6](/ko/math/set_theory/operation_of_binary_relations#pp6)과 [명제 3](#pp3)에 의하여

$$R(y)\subseteq R(R(x))=(R\circ R)(x)=R(x)$$

가 성립한다. $R$은 동치관계이므로 $x$와 $y$의 역할을 바꿀 수 있고 따라서 $R(x)=R(y)$가 성립한다.

반대로 만일 $[x]\_R=[y]\_R$이라면, $x\in [x]\_R=[y]\_R$로부터 $y\sim\_{\tiny R} x$를 얻고 따라서 보조정리가 성립한다.

</details>

위의 함수 $p$를 canonical projection이라 부른다. 그럼 $A$의 부분집합 $[x]\_R\subseteq A$는 몫집합의 원소 $[x]\_R\in A/R$의 함수 $p$에 대한 preimage이므로 equivalence class들은 서로소임을 안다. 즉 동치관계 $(R,A,A)$는 $A$의 분할을 유도한다.

다음 명제는 그 역 또한 성립한다는 것을 보여준다.

<div class="definition" markdown="1">

<ins id="pp7">**명제 7**</ins> $(A_i)\_{i\in I}$가 $A$의 분할이라 하자. 그럼 

> 어떤 $i$가 존재하여 $x,y\in A_i$이다

는 $x$, $y$에 대한 동치관계이다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위의 관계를 $R$이라 적자. 

- $R$이 $A$ 위에서 reflexive인 것은 자명하다. 
- $x$와 $y$가 같은 집합에 포함되면 $y$와 $x$도 같은 집합에 포함되므로 $x\mathrel{R}y$이면 $y\mathrel{R}x$이다. 즉 $R$은 symmetric하다. 
- 마지막으로 만일 $x\mathrel{R}y$이고 $y\mathrel{R}z$라면, $x,y\in A_i$이고 $y,z\in A_j$이다. 그런데 $y\in A_i\cap A_j$이고 $(A_i)_{i\in I}$가 분할이므로 $i=j$이다. 따라서 $x,z\in A_i$이고 명제가 성립한다.

</details>



---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

