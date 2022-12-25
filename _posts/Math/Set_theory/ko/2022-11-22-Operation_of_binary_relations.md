---

title: "이항관계들 사이의 연산"
excerpt: "이항관계의 역과 합성"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/operation_of_binary_relations

header:
    overlay_image: /assets/images/Set_theory/Operation_of_binary_relations.png
    overlay_filter: 0.5

sidebar: 
    nav: "set-ko"

date: 2022-11-22
last_modified_at: 2022-11-22

weight: 4

---

우리는 이제 이항관계의 역, 그리고 이들의 합성을 정의한다.

## 이항관계의 역

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $R$이 이항관계라 하자. 그럼 $(x,y)\in R$를 만족하는 모든 $(y,x)$들로 이루어진 이항관계를 $R$의 *역<sub>inverse</sub>*이라 부르고 이를 $R^{-1}$로 표기한다. 또, 집합 $R^{-1}(X)$를 $X$의 *preimage<sub>역상</sub>*라 부른다. 만일 $R^{-1}=R$라면 $R$이 *symmetric<sub>대칭적</sub>*하다고 한다.

</div>

명시적으로 $R^{-1}$은 다음의 식

$$(x,y)\in R\iff (y,x)\in R^{-1}$$

이 성립하도록 하는 집합이다. 

집합 $R^{-1}(X)$는 이항관계 $R$에 의한 $X$의 preimage로 보거나, 혹은 $R$의 역관계 $R^{-1}$에 의한 $X$의 image로 볼 수 있다. 그러나 $R^{-1}$의 정의에 의하여 이들 중 어떠한 관점을 택하더라도 동일한 집합을 얻으므로 혼동의 여지가 없다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> $R^{-1}$의 역은 $R$이다. 또, $\pr_1R^{-1}=\pr_2R$이고 $\pr_2R^{-1}=\pr_1R$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 주장은 다음의 식

$$(x,y)\in R\iff (y,x)\in R^{-1}\iff (x,y)\in (R^{-1})^{-1}$$ 

에 의해 자명하다. 

둘째 주장을 보자. 만일 $x\in\pr_1R^{-1}$라면, 어떠한 $y$가 존재하여 $(x,y)\in R^{-1}$이다. 이제 $(y,x)\in R$이므로 $x\in\pr_2R$가 성립한다. 이 논증을 뒤집으면 $\pr_2R\subset\pr_1R^{-1}$임을 증명할 수 있다.

아직 보이지 않은 $\pr_2R^{-1}=\pr_1R$의 경우, 방금 주장의 $R$ 자리에 대신 $R^{-1}$을 넣으면 된다.   

</details>

주어진 집합 $A,B$에 대하여, $A\times B$는 $A$를 source로, $B$를 target으로 갖는 가장 큰 이항관계였다. 따라서 두 개의 식

$$\pr_1(A\times B)^{-1}=\pr_2(A\times B)=B,\qquad \pr_2(A\times B)^{-1}=\pr_1(A\times B)=A$$

에서, $(A\times B)^{-1}\subseteq B\times A$이다. 반대로, 만일 $(y,x)\in B\times A$라면 $x\in A$, $y\in B$이므로 $(x,y)\in A\times B$이고, 따라서 $(y,x)\in (A\times B)^{-1}$이므로 $(A\times B)^{-1}=B\times A$가 성립한다.

## 이항관계의 합성

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $R\_1$과 $R\_2$이 이항관계라 하자. 이 두 이항관계의 *합성<sub>composition</sub>* $R\_2\circ R\_1$는 $(x,y)\in R\_1$이고 $(y,z)\in R\_2$이도록 하는 $y$가 존재하는 순서쌍들 $(x,z)$의 집합이다.

</div>

이렇게 정의한 이항관계의 합성이 위에서 정의한 역과 어떠한 관계가 있는지 궁금한 것이 당연하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $R\_1$, $R\_2$가 이항관계라 하자. 그럼 $R\_2\circ R\_1$의 역은 $R\_2^{-1}\circ R\_1^{-1}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(z,x)\in (R\_2\circ R\_1)^{-1}$인 것은 $(x,z)\in R\_2\circ R\_1$인 것과 동치이다. 그리고 이는 다시 <phrase>어떠한 $y$가 존재하여 $(x,y)\in R_1$이고 $(y,z)\in R_2$인 것</phrase>과 동치이다. 이 조건을 만족하는 $y$는 <phrase>$(y,x)\in R_1^{-1}$이고 $(z,y)\in R_2^{-1}$</phrase> 또한 만족하므로, 합성의 정의에 의해 $(z,x)\in R\_2^{-1}\circ R\_1^{-1}$이 성립한다. 반대방향도 동일하게 보일 수 있다.

</details>

또한, 이항관계의 합성은 결합법칙을 만족한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 이항관계의 합성은 결합법칙을 만족한다. 즉, 세 이항관계 $R\_1,R\_2,R\_3$에 대하여 

$$(R_3\circ R_2)\circ R_1=R_3\circ(R_2\circ R_1)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $(x,w)$가 $(R\_3\circ R\_2)\circ R\_1$의 원소인 것과 $R\_3\circ(R\_2\circ R\_1)$의 원소임이 동치임을 보이면 충분하다.  

우선 $(x,w)\in (R\_3\circ R\_2)\circ R\_1$은 <phrase>어떠한 $y$가 존재하여 $(x,y)\in R_1$이고 $(y,w)\in R_3\circ R_2$</phrase>와 동치이다. 그런데 뒤의 조건은 다시 <phrase>어떠한 $z$가 존재하여 $(y,z)\in R_2$이고 $(z,w)\in R_3$</phrase>과 동치이므로, 이 조건은 <phrase>$(x,z)\in R_2\circ R_1$이고 $(z,w)\in R_3$</phrase>과 동치이다. 따라서 이는 <phrase>$(x,w)\in R_3\circ(R_2\circ R_1)$</phrase>과 동치이다.

</details>

따라서 이 공통의 결과인 $(R\_3\circ R\_2)\circ R\_1=R\_3\circ(R\_2\circ R\_1)$을 괄호 없이 $R\_3\circ R\_2\circ R\_1$로 표현해도 아무런 문제가 없다. 

이제 남은 명제들은 위에서 정의한 이항관계의 역, 그리고 이항관계의 합성에 대하여 집합의 image가 어떻게 변하는지를 다룬다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $R\_1$, $R\_2$가 이항관계이고 $A$가 집합이라 하자. 그럼

$$(R_2\circ R_1)(A)=R_2(R_1(A))$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 명제와 같이 진행한다. 

어떠한 $z$에 대하여 $z\in (R\_2\circ R\_1)(A)$인 것은 <phrase>어떠한 $x\in X$가 존재하여 $(x,z)\in R_2\circ R_1$인 것</phrase>과 동치이다. 그런데 이는 다시 <phrase>어떠한 $y$가 존재하여 $(x,y)\in R_1$이고 $(y,z)\in R_2$인 것</phrase>과 동치이다. $y\in R\_1(A)$이므로, $z\in R\_2(R\_1(A))$이다. 이 논리를 거꾸로 뒤집으면 반대방향의 증명이 된다.

</details>

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 이항관계 $(R,A,B)$에 대하여 $X\subseteq A$, $Y\subseteq B$라 하자. 그럼 

1. $R^{-1}(R(X))\supset X\cap\pr_1R$  
2. $R(R^{-1}(Y))\supset Y\cap\pr_2R$  

가 각각 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

본격적으로 증명을 시작하기 전에, 위의 두 식은 <em_ko>모든</em_ko> $R$에 대해 성립해야 하므로, $R$ 자리에 $R^{-1}$을 집어넣어도 성립해야 한다. 따라서, 1만 보이면 2는 [명제 2](#pp2)에 의해 자명하다.  

이제 $x\in X\cap\pr\_1R$라 하자. 그럼 $x\in\pr\_1R$에서, 어떠한 $y$가 존재하여 $(x,y)\in R$이고, $x\in X$이므로 이 $y$는 $y\in R(X)$를 만족한다. 이제 $(y,x)\in R^{-1}$이므로, $x\in R^{-1}(R(X))$이다.

</details>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $R\_1$, $R\_2$가 이항관계라 하자. 그럼 다음의 두 식이 성립한다.

$$ \pr_1(R_2\circ R_1)=R_1^{-1}(\pr_1R_2),\quad \pr_2(R_2\circ R_1)=R_2(\pr_2R_1).$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음 implication들의 chain

$$\begin{aligned}
    x\in\pr_1(R_2\circ R_1)&\iff \exists z\big((x,z)\in R_2\circ R_1\big)\\
    &\iff\exists y,z\big(((x,y)\in R_1)\wedge((y,z)\in R_2)\big)\\
    &\iff\exists y\big(((x,y)\in R_1)\wedge(y\in\pr_1R_2)\big)\\
    &\iff x\in R_1^{-1}(\pr_1 R_2).
\end{aligned}$$

에 의해 자명하다. 두 번째 식도 마찬가지로 보일 수 있다.

</details>

마지막으로, 특별한 이항관계를 소개한다.

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 집합 $A$에 대하여, $\Delta_A$는 이항관계

$$\Delta_A=\{(x,x): x\in A\}$$

를 뜻한다. 이를 $A\times A$의 *diagonal<sub>대각집합</sub>*이라 부른다.

</div>

정의에 의해 $\pr_1\Delta_A=\pr_2\Delta_A=A$이므로, 이를 이항관계

$$\left(\Delta_A,A,A\right)$$

로 생각할 수 있다. 다음 글에서 이 관계가 함수가 된다는 것을 보일 수 있으며, 이를 집합 $A$ 위에 정의된 *항등함수*라 부른다. $A$를 source로 갖는 이항관계 $R\_1$ 혹은, $A$를 target으로 갖는 이항관계 $R\_2$에 대하여 두 식

$$R_1\circ\Delta_A=R_1,\qquad \Delta_A\circ R_2=R_2$$

이 항상 성립하므로 $(\Delta_A,A,A)$를 항등함수라고 부르는 것이 어색하지 않다.

---
**참고문헌**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---