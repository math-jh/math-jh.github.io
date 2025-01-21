---

title: "등급환"
excerpt: ""

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/graded_rings
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Graded_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-08-11
last_modified_at: 2024-08-11
weight: 106

---

## 등급환

Index set $I$가 commutative monoid일 경우, 우리는 ablian group들의 family $(A\_i)\_{i\in I}$들의 direct sum $\bigoplus\_{i\in I} A\_i$를 *graded abelian group*이라 부르기로 하였다. 당시에는 $A\_i$ 위에 어떠한 조건도 없었기 때문에 이는 별로 흥미로운 정의가 아니었으나, 이제는 $A\_i$ 위에 곱셈구조가 더해져 있으므로 이 정의가 더 의미를 갖게 된다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Commutative monoid $I$와 $I$-indexed family of abelian groups $(A\_i)\_{i\in I}$가 주어졌다 하자. 만일 $\bigoplus\_{i\in I} A\_i$ 위에 정의된 곱셈구조가 이를 ring으로 만들고, 추가적으로 다음 조건

$$A_i A_j\subseteq A_{i+j}\qquad\text{for all $i,j\in I$}$$

을 만족한다면 $A$를 $I$로 index가 주어진 *graded ring<sub>등급환</sub>*이라 부른다. $A_i$에 속한 원소를 *homogeneous element<sub>동차원소</sub>*라 부른다.

</div>

정의에 의하여, $A$의 임의의 원소들은 homogeneous element들의 유한한 합으로 유일하게 표현할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 만일 $I$의 임의의 원소가 cancellable이고 $\bigoplus\_{i\in I} A\_i$가 graded ring이라 하자. 그럼 $A_0$은 $A$의 subring이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A_0A_0\subseteq A_0$으로부터 $A_0$이 곱셈에 대해 닫혀있음은 자명하다. 따라서 $A=\bigoplus A\_i$의 곱셈에 대한 항등원 $1$이 $A_0$에 속함을 보이면 충분하다. $1=\sum\_{i\in I} \epsilon_i$라 하자. 그럼 임의의 $\alpha\in A\_j$에 대하여, 

$$\alpha=1\alpha=\sum_{i\in I} \epsilon_i\alpha\in A_j$$

이고, 따라서 모든 $i\neq 0$에 대하서는 $\epsilon_i\alpha=0$이고, $i=0$에 대해서만 $\epsilon_0\alpha=\alpha$가 성립한다. 이제 $A$의 임의의 원소는 homogeneous element들의 합으로 나타낼 수 있으므로 증명이 완료된다. 

</details>

대부분의 경우 우리가 관심있는 것은 $I=\mathbb{Z}$이거나 $I= \mathbb{N}$인 경우이다. 따라서 [명제 2](#prop2)의 전제조건이 만족된다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 abelian group $G$에 대하여, $A$에 의해 생성되는 free ring $F(G)$는 $\mathbb{N}$-graded ring이다. 

</div>

## 등급환 준동형사상

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Commutative monoid $I$와 두 $I$-graded ring $A,A'$에 대하여, ring homomorphism $\phi:A \rightarrow A'$가 *graded homomorphism*이라는 것은 임의의 $i\in I$에 대하여 $\phi(A_i)\subseteq A_i'$이 모든 $i\in I$에 대해 성립하는 것이다.

</div>

어렵지 않게 $I$-graded ring과 $I$-graded homomorphism이 category $\bgr_I\Ring$을 이루는 것을 안다. 

## 동차아이디얼과 등급환의 몫

Graded ring $A=\bigoplus_{i\in I} A_i$에 대해, $A$의 ideal $\mathfrak{a}$에 대한 quotient ring $A/\mathfrak{a}$가 항상 graded ring이 되지는 않을 수도 있다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> Ring $A$를 고정하고, $A$의 원소들을 계수로 가지는 *polynomial ring*

$$A[\x]=\{\alpha_n\x^n+\cdots+\alpha_1\x+\alpha_0: \alpha_i\in A\}$$

을 생각하자. 그럼 이는 다음의 decomposition

$$A[\x]=\bigoplus_{n\geq 0} A\x^n$$

에 의하여 graded ring의 구조를 갖는다. 한편 $\x-1$로 생성된 ideal $(\x-1)$을 생각하자. 그럼 ring으로서

$$A[\x]/(\x-1)\cong A$$

이며, 명시적으로 이 isomorphism은

$$\alpha_n\x^n +\cdots+\alpha_1\x+\alpha_0\quad \mapsto\quad \alpha_n+\cdots+\alpha_1+\alpha_0$$

으로 정의된 evaluation map에 first isomorphism theorem을 적용하여 얻어진다. 그러나 위의 homomorphism은 graded homomorphism이 아니다.

</div>

이를 피하기 위해 *homogeneous ideal*의 개념을 도입한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $I$-graded ring $A=\bigoplus\_{i\in I} A\_i$와 $A$의 ideal $\mathfrak{a}$에 대하여 다음이 모두 동치이다. 

1. $\mathfrak{a}$는 $\mathfrak{a}\cap A_i$들의 합이다.
2. $\mathfrak{a}$의 임의의 원소를 homogeneous element로 분해하면, 각각의 원소들도 모두 $\mathfrak{a}$에 속한다. 
3. $\mathfrak{a}$는 homogeneous element로 생성된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$A$의 원소로서, $\mathfrak{a}$의 모든 원소들은 homogeneous element들의 합으로 유일하게 나타난다. 따라서 처음 두 조건이 동치인 것은 자명하며, 1번 조건이 3번 조건을 함의하는 것 또한 자명하다. 이제 세 번째 조건을 가정하고 두 번째 조건을 증명한다. $\mathfrak{a}$가 homogeneous element들 $(x_j)_{j\in J}$로 생성된다 가정하자. 그럼 임의의 $x\in \mathfrak{a}$가 다음의 식

$$x=\sum_{j\in J} \alpha_j x_j,\qquad\text{$(\alpha_j)_{j\in J}$ finitely supported}$$

으로 나타난다. 이제 $\alpha_j$들 각각은 다시 $A$의 원소로서 homogeneous element들의 합

$$\alpha_j=\sum_{k\in K_j} \alpha_{jk},\qquad \text{$(\alpha_{jk})_{k\in K_j}$ finitely supported}$$

으로 나타난다. 따라서

$$x=\sum_{j\in J}\sum_{k\in K_j}\alpha_{jk}x_j,\qquad \text{$(\alpha_{jk})_{j\in J,k\in K_j}$ finitely supported}$$

이고, $\alpha_{jk}x_j$들은 모두 각각 homogeneous element들이며 모두 $\mathfrak{a}$에 속한다. 이로부터 2번 조건을 보일 수 있다.

</details>

위의 동치조건을 만족하는 ideal을 *homogeneous ideal<sub>동차 아이디얼</sub>*이라 부른다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Homogeneous ideal $\mathfrak{a}$에 대하여, $A/\mathfrak{a}$가 graded ideal이며, 그 decomposition이 다음 식

$$A/\mathfrak{a}=\bigoplus_{i\in I}A_i/(\mathfrak{a}\cap A_i)$$

으로 주어진다.

</div>

이에 대한 증명은 자명하므로 생략한다.