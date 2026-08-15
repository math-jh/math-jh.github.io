---
title: "등급가군"
description: "등급환 위의 등급가군의 개념과 등급 준동형사상의 정의를 다루며, 등급부분가군의 기본 성질을 살펴본다."
excerpt: "Graded ring 위에 정의되는 graded module의 정의"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/graded_modules
sidebar: 
    nav: "algebraic_structures-ko"

date: 2024-08-12
weight: 204

---

이제 우리는 graded module의 개념을 정의한다.

## 등급가군

::: 정의 1
Commutative monoid $I$에 대해, $A=\bigoplus_{i\in I}A_i$가 $I$-graded ring이라 하고, $M$이 left $A$-module이면서 동시에 $I$-graded abelian group $M=\bigoplus_{i\in I}M_i$라 하자. 그럼 $M$이 *$I$-graded left $A$-module<sub>$I$-등급 왼쪽가군</sub>*이라는 것은 임의의 $i,j\in I$에 대하여 

$$A_iM_j\subseteq M_{i+j}$$

이 성립하는 것이다. 
:::

비슷하게 $I$-graded right $A$-module도 또한 정의한다. 특별히 $A$를 $A$ 자기 자신에 대한 left $A$-module로 본다면, [정의 1](#def1)에 의해 모든 graded ring은 자기 자신에 대한 graded (left) $A$-module이다. 만일 $I$의 덧셈에 대하여, 모든 원소가 cancellable이라면 [§등급환, ⁋명제 2](/ko/math/algebraic_structures/graded_rings#prop2)에 의하여 $A_0$은 ring이다. 그럼 위의 식으로부터 각각의 $M_j$들이 $A_0$-module이 되는 것이 자명하다. 

::: 정의 2
두 $I$-graded left $A$-module $M,M'$에 대하여, $A$-linear map $u:M \rightarrow M'$이 *graded homomorphism*이라는 것은 $u(M_i)\subseteq M_i'$이 항상 성립하는 것이다.
:::

이를 통해 $I$-graded left $A$-module들의 category $\bgr_I\lMod{A}$를 정의할 수 있다. 더 일반적으로 다음을 정의한다. 

::: 정의 3
 두 $I$-graded left $A$-module $M,M'$에 대하여, $A$-linear map $u:M \rightarrow M'$이 *graded homomorphism of degree $i$<sub>차수 $i$의 등급 준동형</sub>*라는 것은 $u(M_j)\subseteq M_{i+j}'$이 항상 성립하는 것이다.
:::

그럼 [정의 2](#def2)의 graded homomorphism들은 모두 graded homomorphism of degree $0$에 불과하다. 만일 $I$의 모든 원소들이 cancellable이라면, 우리는 *graded homomorphism of degree $-i$*를 다음 조건

$$u(M_{i+j})\subseteq M_j',\qquad u(M_k)=0\text{ if $k-i\not\in I$}$$

으로 정의할 수도 있다. 다만 이러한 방식으로 정의할 때 주의할 점은 bijective graded homomorphism of degree $i$는 $i\neq 0$일 경우, 일반적으로 $I$-graded left $A$-module들 사이의 isomorphism으로 생각하지 않는다는 것이다. 

이러한 방식의 일반화는 homological algebra에서 더 자세히 다룬다.

## 등급부분가군

::: 명제 4
$I$-graded left $A$-module $M=\bigoplus_{i\in I} M_i$가 주어졌다 하자. 그럼 $M$의 submodule $N$에 대하여, 다음이 모두 동치이다.

1. $N$은 $N\cap M_i$들의 합이다.
2. $N$의 임의의 원소를 homogeneous element들로 분해하면, 각각의 원소들도 모두 $N$에 속한다. 
3. $N$은 homogeneous element들로 생성된다.
:::

이 명제는 [§등급환, ⁋명제 6](/ko/math/algebraic_structures/graded_rings#prop6)의 일반화이며, 그 증명 또한 동일하다. 이 동치조건을 만족하는 submodule들을 *graded submodule<sub>등급부분가군</sub>*이라 부른다. 한편 graded submodule $N$에 대하여 [§등급환, ⁋명제 7](/ko/math/algebraic_structures/graded_rings#prop7)의 증명이 그대로 옮겨가, quotient module $M/N$은 다음의 decomposition

$$M/N=\bigoplus_{i\in I}M_i/(N\cap M_i)$$

을 통해 graded module이 된다. 그럼 다음이 성립한다.

::: 명제 5
Degree $d$의 graded $A$-homomorphism $u:M \rightarrow N$에 대하여, 다음이 성립한다.

1. $\im(u)$는 $N$의 graded submodule이다.
2. 만일 $d$가 cancellable이라면, $\ker(u)$는 $M$의 graded submodule이다.
3. $d=0$이라면 canonical bijection $M/\ker(u)\cong\im(u)$는 graded module들 사이의 isomorphism을 정의한다. 
:::
::: 증명
1번의 경우, $M=\bigoplus_j M_j$이므로 $\im(u)$는 homogeneous element $u(x_j)\in N_{d+j}$들로 생성되고, 따라서 [명제 4](#prop4)의 셋째 조건에 의해 graded submodule이다.

2번의 경우, $x=\sum_j x_j\in\ker(u)$라 하면 $0=u(x)=\sum_j u(x_j)$이고 각 $u(x_j)$는 $N_{d+j}$에 속한다. $d$가 cancellable이므로 $j\mapsto d+j$는 단사이고, 따라서 이 합의 항들이 서로 다른 degree에 놓여 성분별로 $u(x_j)=0$을 얻는다. 즉 각 $x_j$가 $\ker(u)$에 속하므로 [명제 4](#prop4)의 둘째 조건이 성립한다.

3번의 경우, 임의의 $y\in\im(u)\cap N_i$에 대하여 $y=u(x)$인 $x=\sum_j x_j$를 택하면 $d=0$이므로 $u(x)$의 $N_i$-성분은 $u(x_i)$이고, 따라서 $\im(u)\cap N_i=u(M_i)$이다. 그럼 canonical bijection $M/\ker(u)\rightarrow\im(u)$가 $M_i/(\ker(u)\cap M_i)$를 $\im(u)\cap N_i$로 보내므로, 위에서 준 $M/\ker(u)$의 grading에 대하여 degree를 보존한다.
:::

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
