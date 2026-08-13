---
title: "등급환"
description: "등급환의 정의와 동차원소의 성질을 다루고, 등급환 준동형사상과 동차아이디얼에 의한 몫환의 구조를 살펴본다."
excerpt: "Monoid로 index된 graded ring의 정의와 기본 성질"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/graded_rings
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-08-11
weight: 105
drift_needed: true

---

## 등급환

Index set $I$가 commutative monoid일 경우, 우리는 abelian group들의 family $(A_i)_{i\in I}$를 *graded abelian group*이라 부르기로 하였다. ([§가환군, ⁋정의 16](/ko/math/algebraic_structures/abelian_groups#def16)) 당시에는 $A_i$ 위에 어떠한 조건도 없었기 때문에 이는 별로 흥미로운 정의가 아니었으나, 이제는 $A_i$ 위에 곱셈구조가 더해져 있으므로 이 정의가 더 의미를 갖게 된다. 

::: 정의 1
Commutative monoid $I$와 $I$-indexed family of abelian groups $(A_i)_{i\in I}$가 주어졌다 하자. 만일 $A=\bigoplus_{i\in I} A_i$ 위에 정의된 곱셈구조가 이를 ring으로 만들고, 추가적으로 다음 조건

$$A_i A_j\subseteq A_{i+j}\qquad\text{for all $i,j\in I$}$$

을 만족한다면 $A$를 $I$로 index가 주어진 *graded ring<sub>등급환</sub>*이라 부른다. $A_i$에 속한 원소를 *homogeneous element<sub>동차원소</sub>*라 부른다.
:::

정의에 의하여, $A$의 임의의 원소들은 homogeneous element들의 유한한 합으로 유일하게 표현할 수 있다. 

::: 명제 2
만일 $I$의 임의의 원소가 cancellable이고 $A=\bigoplus_{i\in I} A_i$가 graded ring이라 하자. 그럼 $A_0$은 $A$의 subring이다. 
:::
::: 증명
$A_0A_0\subseteq A_0$으로부터 $A_0$은 곱셈에 대해 닫혀있다. 따라서 $A=\bigoplus A_i$의 곱셈에 대한 항등원 $1$이 $A_0$에 속함을 보이면 충분하다. $1=\sum_{i\in I} \epsilon_i$라 하자. 그럼 임의의 $\alpha\in A_j$에 대하여, 

$$\alpha=1\alpha=\sum_{i\in I} \epsilon_i\alpha\in A_j$$

이고, 따라서 모든 $i\neq 0$에 대해서는 $\epsilon_i\alpha=0$이고, $i=0$에 대해서만 $\epsilon_0\alpha=\alpha$가 성립한다. 이제 $A$의 임의의 원소는 homogeneous element들의 합으로 나타낼 수 있으므로 모든 $x\in A$에 대하여 $\epsilon_0x=x$가 성립하고, 여기에 $x=1$을 대입하면 $1=\epsilon_0\in A_0$을 얻는다. 
:::

대부분의 경우 우리가 관심있는 것은 $I=\mathbb{Z}$이거나 $I= \mathbb{N}$인 경우이다. 따라서 [명제 2](#prop2)의 전제조건이 만족된다. 

::: 예시 3
임의의 abelian group $G$에 대하여, $G$에 의해 생성되는 free ring $F(G)=\bigoplus_{n\geq 0} G^{\otimes n}$을 생각하자. $G^{\otimes m}$의 원소와 $G^{\otimes n}$의 원소의 곱은 $G^{\otimes (m+n)}$에 속하므로 $F(G)$는 $\mathbb{N}$-graded ring이다. ([§환의 정의, §§가환군 위에 정의된 자유환](/ko/math/algebraic_structures/rings#가환군-위에-정의된-자유환)) 
:::

## 등급환 준동형사상

::: 정의 4
Commutative monoid $I$와 두 $I$-graded ring $A,A'$에 대하여, ring homomorphism $\phi:A \rightarrow A'$가 *graded homomorphism*이라는 것은 임의의 $i\in I$에 대하여 $\phi(A_i)\subseteq A_i'$이 성립하는 것이다.
:::

어렵지 않게 $I$-graded ring과 $I$-graded homomorphism이 category $\bgr_I\Ring$을 이루는 것을 안다. 

## 동차아이디얼과 등급환의 몫

Graded ring $A=\bigoplus_{i\in I} A_i$와 $A$의 two-sided ideal $\mathfrak{a}$에 대하여, quotient ring $A/\mathfrak{a}$는 $A$의 grading을 물려받지 못할 수 있다. 즉 quotient map이 graded homomorphism이 되도록 하는 $A/\mathfrak{a}$의 grading이 존재하지 않을 수 있다. 

::: 예시 5
Commutative ring $A$를 고정하고, $A$의 원소들을 계수로 가지는 *polynomial ring*

$$A[\x]=\{\alpha_n\x^n+\cdots+\alpha_1\x+\alpha_0\mid n\in\mathbb{N}, \alpha_i\in A\}$$

을 생각하자. 그럼 이는 다음의 decomposition

$$A[\x]=\bigoplus_{n\geq 0} A\x^n$$

에 의하여 graded ring의 구조를 갖는다. 한편 $\x-1$로 생성된 ideal $(\x-1)$을 생각하자. 그럼 ring으로서

$$A[\x]/(\x-1)\cong A$$

이며, 명시적으로 이 isomorphism은

$$\alpha_n\x^n +\cdots+\alpha_1\x+\alpha_0\quad \mapsto\quad \alpha_n+\cdots+\alpha_1+\alpha_0$$

으로 정의된 evaluation map에 first isomorphism theorem을 적용하여 얻어진다. 그런데 이 때 quotient map $\pi:A[\x]\rightarrow A[\x]/(\x-1)$은 임의의 $n$에 대하여 $A\x^n$을 $A$ 전체로 보낸다. 따라서 $A\neq 0$이라면 $\pi(A\x^n)$들의 합은 direct sum이 될 수 없고, $\pi$를 graded homomorphism으로 만드는 grading은 $A[\x]/(\x-1)$에 존재하지 않는다.
:::

이를 피하기 위해 *homogeneous ideal*의 개념을 도입한다.

::: 명제 6
$I$-graded ring $A=\bigoplus_{i\in I} A_i$와 $A$의 two-sided ideal $\mathfrak{a}$에 대하여 다음이 모두 동치이다. 

1. $\mathfrak{a}$는 $\mathfrak{a}\cap A_i$들의 합이다.
2. $\mathfrak{a}$의 임의의 원소를 homogeneous element로 분해하면, 각각의 원소들도 모두 $\mathfrak{a}$에 속한다. 
3. $\mathfrak{a}$는 homogeneous element로 생성된다.
:::
::: 증명
$A$의 원소로서, $\mathfrak{a}$의 모든 원소들은 homogeneous element들의 합으로 유일하게 나타난다. 따라서 처음 두 조건은 서로 동치이며, 1번 조건 하에서 $\mathfrak{a}$는 homogeneous element인 $\mathfrak{a}\cap A_i$의 원소들로 생성되므로 1번 조건이 3번 조건을 함의한다. 이제 세 번째 조건을 가정하고 두 번째 조건을 증명한다. $\mathfrak{a}$가 homogeneous element들 $(x_j)_{j\in J}$로 생성된다 가정하자. 그럼 임의의 $x\in \mathfrak{a}$가 다음의 식

$$x=\sum_{k\in K} a_k x_{j(k)} b_k,\qquad\text{$K$ finite, $a_k,b_k\in A$}$$

으로 나타난다. 이제 $a_k$와 $b_k$ 각각은 다시 $A$의 원소로서 homogeneous element들의 합

$$a_k=\sum_{p} a_{kp},\qquad b_k=\sum_q b_{kq}$$

으로 나타나므로

$$x=\sum_{k\in K}\sum_{p,q}a_{kp}x_{j(k)}b_{kq}$$

를 얻는다. 이 때 $a_{kp}x_{j(k)}b_{kq}$들은 모두 각각 homogeneous element들이며 모두 $\mathfrak{a}$에 속한다. 이제 같은 degree를 갖는 항들끼리 모으면 그 합이 $x$의 각 homogeneous 성분이 되고, 이들이 모두 $\mathfrak{a}$에 속하므로 2번 조건을 얻는다.
:::

위의 동치조건을 만족하는 two-sided ideal을 *homogeneous ideal<sub>동차 아이디얼</sub>*이라 부른다. 그럼 다음이 성립한다.

::: 명제 7
Homogeneous ideal $\mathfrak{a}$에 대하여, $A/\mathfrak{a}$가 graded ring이며, 그 decomposition이 다음 식

$$A/\mathfrak{a}=\bigoplus_{i\in I}A_i/(\mathfrak{a}\cap A_i)$$

으로 주어진다.
:::
::: 증명
Quotient map을 $\pi:A\rightarrow A/\mathfrak{a}$라 하자. $A=\bigoplus_i A_i$이고 $\pi$가 전사이므로 $A/\mathfrak{a}$는 $\pi(A_i)$들의 합이며, $\pi$를 $A_i$로 제한한 것의 kernel이 $\mathfrak{a}\cap A_i$이므로 $\pi(A_i)\cong A_i/(\mathfrak{a}\cap A_i)$이다.

이 합이 direct sum인 것을 보이기 위해 우리는 finitely supported homogeneous element들의 family $(\alpha_i)$가 $\sum_i \pi(\alpha_i)=0$을 만족한다 가정하고 모든 $i$에 대해 $\pi(\alpha_i)=0$임을 보여야 한다. 가정에 의해 $\sum_i\alpha_i\in\mathfrak{a}$이므로, [명제 6](#prop6)의 둘째 조건에 의해 각 $\alpha_i$가 $\mathfrak{a}$에 속해야 하고, 따라서 $\mathfrak{a}\cap A_i$에 속한다. 즉 모든 $i$에 대해 $\pi(\alpha_i)=0$이다.

마지막으로 $A_iA_j\subseteq A_{i+j}$로부터 $\pi(A_i)\pi(A_j)\subseteq \pi(A_{i+j})$가 성립하므로, 이 decomposition은 $A/\mathfrak{a}$ 위에 graded ring의 구조를 준다.
:::

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
