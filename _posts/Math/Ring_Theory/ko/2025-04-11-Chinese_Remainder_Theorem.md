---
title: "중국인의 나머지정리"
description: "정수의 합동 문제에서 출발해 comaximal ideal 조건으로 일반화한 중국인의 나머지정리를 증명한다. 가환환에서 pairwise comaximal ideal의 교차가 곱과 같아진다는 사실을 핵심 도구로 쓰며, 곱분해와 중심 idempotent 분해의 대응까지 다룬다."
excerpt: "Comaximal ideal에 대한 중국인의 나머지정리와 중심 idempotent 분해"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/chinese_remainder_theorem
sidebar: 
    nav: "ring_theory-ko"

date: 2025-04-11
weight: 3

---

중국인의 나머지정리는 정수론의 고전 결과로, 이 결과의 본질은 ring isomorphism 

$$\mathbb{Z}/mn\mathbb{Z}\cong \mathbb{Z}/m\mathbb{Z}\times \mathbb{Z}/n\mathbb{Z},\qquad \text{$m,n$ coprime}$$

이다. ([\[정수론\] §중국인의 나머지 정리, ⁋정리 1](/ko/math/number_theory/chinese_remainder_theorem#thm1)) 즉, 어떤 정수를 $mn$으로 나눈 나머지는 $m$으로 나눈 나머지와 $n$으로 나눈 나머지 각각을 알면 완벽하게 구할 수 있다는 뜻이며, 이를 임의의 ring $A$로 확장하는 것이 이 글의 목표이다. 

간략하게 이야기해서, 이 일반화는 우선 $m\mathbb{Z}$와 $n\mathbb{Z}$를 ring $A$의 ideal로 일반화하고, $mn\mathbb{Z}$를 이 두 ideal의 교집합으로 이해하여 얻어진다. 다만 이 일반화가 임의의 ideal에 대해 되는 것은 아니며, 위 $m,n$이 서로소라는 조건에 해당하는 조건 또한 필요하다. 이에 해당하는 ideal의 조건은 *comaximal*로, 그럼 ring theory에서 일반화된 정리는 pairwise comaximal ideal들 $\mathfrak{a}_i$에 대하여 ring isomorphism

$$A\Big/\Big(\bigcap_i \mathfrak{a}_i\Big)\cong \prod_i A/\mathfrak{a}_i$$

가 성립한다는 형태이고, $A$가 가환환이라면 뒤에 보일 등식 $\bigcap_i\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$에 의해 $A/\mathfrak{a}_1\cdots\mathfrak{a}_n\cong\prod_i A/\mathfrak{a}_i$로도 쓸 수 있다.

## Ideal의 곱

::: 정의 1
Ring $A$의 두 two-sided ideal $\mathfrak{a},\mathfrak{b}$에 대하여, 이들의 *곱<sub>product</sub>* $\mathfrak{a}\mathfrak{b}$는 다음 집합

$$\mathfrak{a}\mathfrak{b}=\{x_1y_1+x_2y_2+\cdots+x_ny_n\mid x_i\in \mathfrak{a}, y_i\in \mathfrak{b}, n\geq 1\}$$

을 의미한다. 
:::

$\mathfrak{a}\mathfrak{b}$이 $A$의 덧셈에 대한 subgroup임은 자명하다. 한편 $\mathfrak{a}\mathfrak{b}$의 임의의 원소 $x_1y_1+\cdots+x_ny_n$와, $A$의 임의의 원소 $x$에 대하여,

$$x(x_1y_1+\cdots+x_ny_n)=xx_1y_1+\cdots xx_ny_n$$

이고 $xx_i\in \mathfrak{a}$이므로 $x(x_1y_1+\cdots+x_ny_n)\in \mathfrak{a}\mathfrak{b}$이다. $x$를 오른쪽에 곱해도 비슷한 논증이 성립하므로, $\mathfrak{a}\mathfrak{b}$는 $A$의 two-sided ideal인 것을 확인할 수 있다.

::: 명제 2
위와 같이 정의된 곱셈에 대하여, $A$의 two-sided ideal들의 모임은 항등원을 $A$로 하는 monoid 구조를 가진다 ([\[대수적 구조\] §반군, 모노이드, 군, ⁋정의 3](/ko/math/algebraic_structures/groups#def3)). 뿐만 아니라, 분배법칙

$$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c},\quad (\mathfrak{a}+\mathfrak{b})\mathfrak{c}=\mathfrak{a}\mathfrak{c}+\mathfrak{b}\mathfrak{c}$$

도 성립한다.
:::
::: 증명
세 two-sided ideal $\mathfrak{a},\mathfrak{b},\mathfrak{c}$가 주어졌다 하자. 그럼 $(\mathfrak{a}\mathfrak{b})\mathfrak{c}$의 임의의 원소는

$$\left(\sum_{i=1}^{n_1} x_i^{(1)}y_i^{(1)}\right)z_1+\cdots+\left(\sum_{i=1}^{n_k}x_i^{(k)}y_i^{(k)}\right)z_k$$

의 꼴로 쓰일 수 있으며, 분배법칙을 이용하여 이를 모두 풀어준 후 오른쪽 두 개를 묶어주면 이 원소가 $\mathfrak{a}(\mathfrak{b}\mathfrak{c})$에 속하는 것을 알 수 있다. 반대 방향 포함관계도 똑같은 방식으로 증명할 수 있으므로, 곱셈이 associative하다. 또, 임의의 two-sided ideal $\mathfrak{a}$에 대해 $A \mathfrak{a}=\mathfrak{a}A=\mathfrak{a}$임이 자명하다. 

마지막으로 임의의 $b_1+c_1,\ldots, b_n+c_n\in \mathfrak{b}+\mathfrak{c}$에 대하여 

$$a_1(b_1+c_1)+\cdots a_n(b_n+c_n)$$

을 분배법칙을 사용하여 풀어주면 $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})\subset \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$를 쉽게 보일 수 있다. 거꾸로 임의의

$$a_1b_1+\cdots a_nb_n + a_1'c_1+\cdots +a_m'c_m\in \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$

에 대하여, $b_i$들과 $c_i$들이 모두 $\mathfrak{b}+\mathfrak{c}$의 원소이므로 위의 원소는 $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})$의 원소이다. 비슷하게 오른쪽 분배법칙도 증명할 수 있다.
:::

임의의 두 two-sided ideal $\mathfrak{a},\mathfrak{b}$에 대하여, 다음 두 식

$$\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}A\subset \mathfrak{a},\quad \mathfrak{a}\mathfrak{b}\subset A \mathfrak{b}\subset \mathfrak{b}$$

이 모두 성립하므로 $\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}\cap \mathfrak{b}$이 성립한다. 일반적으로 등호가 성립할 필요는 없다.

::: 정의 3
Ring $A$의 두 two-sided ideal $\mathfrak{a},\mathfrak{b}$가 $\mathfrak{a}+\mathfrak{b}=A$를 만족할 때 *comaximal<sub>공최대</sub>*이라 부른다. 여러 ideal $\mathfrak{a}_1,\ldots,\mathfrak{a}_n$이 *pairwise comaximal<sub>쌍마다 공최대</sub>*이라 함은 모든 $i\ne j$에 대하여 $\mathfrak{a}_i+\mathfrak{a}_j=A$임을 뜻한다.
:::

여기서 조건 $\mathfrak{a}+\mathfrak{b}=A$는 항등원 $1$이 

$$1=u+v,\qquad\text{$u\in\mathfrak{a}$, $v\in\mathfrak{b}$}$$

꼴로 표현된다는 것과 동치이며, 이는 정수론에서 서로소인 두 정수 $m,n$에 대하여 Bézout 항등식 $mu+nv=1$이 존재하는 것과 정확히 대응한다. ([\[정수론\] §유클리드 호제법과 Bézout 항등식, ⁋정리 3](/ko/math/number_theory/euclidean_algorithm#thm3)) 따라서 $\mathbb{Z}$에서는 서로소인 두 정수 $m,n$의 ideal $m\mathbb{Z},n\mathbb{Z}$가 comaximal이 된다. 

한편, 일반적으로는 성립하지 않던 등식 $\mathfrak{a}\mathfrak{b}=\mathfrak{a}\cap\mathfrak{b}$가 두 ideal이 comaximal일 때는 성립한다. 이를 보이기 위한 결과는 다음과 같다. 

::: 명제 4
$A$의 two-sided ideal들 $\mathfrak{a},\mathfrak{b}_1,\ldots, \mathfrak{b}_n$이 주어졌다 하고, $A=\mathfrak{a}+\mathfrak{b}_i$가 모든 $i$에 대해 성립한다 가정하자. 그럼

$$A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n=\mathfrak{a}+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n)$$

이 성립한다. 
:::
::: 증명
어차피 $\mathfrak{b}_1\cdots \mathfrak{b}_n\subset \mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n$이므로 등식 $A=\mathfrak{a}+\mathfrak{b}_1\cdots \mathfrak{b}_n$만 보이면 충분하다. 또, 귀납적으로 증명이 가능하므로 $n=2$인 경우만 생각하면 충분하다. 즉 $A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$라 하고, $A=\mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$임을 보이자. 

우선 $A=\mathfrak{a}+\mathfrak{b}_1=\mathfrak{a}+\mathfrak{b}_2$로부터, $1=a+b_1=a'+b_2$를 만족하는 $a,a'\in \mathfrak{a}, b_i\in \mathfrak{b}_i$를 택할 수 있다. 그럼

$$1=a'+b_2=a'+1b_2=a'+(a+b_1)b_2=(a+a'b_2)+b_1b_2\in \mathfrak{a}+\mathfrak{b}_1 \mathfrak{b}_2$$

이 성립한다. 
:::

Commutative ring의 경우, 이를 사용하여 다음을 증명할 수 있다. 

::: 명제 5
Commutative ring $A$의 ideal들 $\mathfrak{b}_1,\ldots, \mathfrak{b}_n$이 pairwise comaximal이라 하자. 즉 $i\neq j$에 대하여 $\mathfrak{b}_i+\mathfrak{b}_j=A$이다. 그럼

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

이 성립한다.
:::
::: 증명
귀납법으로 증명한다. 항상 $\mathfrak{b}_1\cdots\mathfrak{b}_n\subseteq \mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$이므로 반대방향만 보이면 된다.

우선 $n=2$이고 $\mathfrak{b}_1+\mathfrak{b}_2=A$라 하자. $1=u+v$ ($u\in\mathfrak{b}_1, v\in\mathfrak{b}_2$)로 두면, 임의의 $x\in\mathfrak{b}_1\cap\mathfrak{b}_2$에 대하여 $A$가 commutative라는 사실을 사용하면

$$x=x\cdot 1=x(u+v)=xu+xv\in \mathfrak{b}_2 \mathfrak{b}_1+\mathfrak{b}_1 \mathfrak{b}_2=\mathfrak{b}_1 \mathfrak{b}_2$$

이다. 따라서 $\mathfrak{b}_1\cap\mathfrak{b}_2=\mathfrak{b}_1\mathfrak{b}_2$이다.

이제 $n>2$라 하자. 두 ideal $\mathfrak{a}=\mathfrak{b}_n$과 $\mathfrak{b}_1,\ldots,\mathfrak{b}_{n-1}$이 pairwise comaximal임은 자명하므로, 여기에 [명제 4](#prop4)를 적용하면

$$A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})$$

이고, 귀납가정으로 $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}=\mathfrak{b}_1\cdots \mathfrak{b}_{n-1}$이다. 이제 $n=2$의 결과를 comaximal인 두 ideal $\mathfrak{b}_n$과 $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}$에 적용하면

$$\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

을 얻는다.
:::

## 중국인의 나머지 정리

이제 우리는 이 글의 핵심 정리를 살펴본다.

Ring $A$와, $A$의 two-sided ideal들 $\mathfrak{a}_i$가 주어졌다 하자. 그럼 각 몫환으로의 projection들 $\pi_i:A \rightarrow A/\mathfrak{a}_i$이 존재하며, 이들로부터 ring homomorphism $\pi:A \rightarrow\prod A/\mathfrak{a}_i$가 정의된다. 이 morphism이 언제 isomorphism이 되는지가 중국인의 나머지정리의 핵심이다.

::: 명제 6
Ring $A$와, $A$의 pairwise comaximal two-sided ideal들 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$이 주어졌다 하자. 그럼 위에서 정의한 $\pi:A \rightarrow \prod_1^n A/\mathfrak{a}_i$는 surjective이고, 이 map의 kernel은 $\bigcap \mathfrak{a}_i$와 같다.
:::
::: 증명
$\ker\pi=\bigcap_i \mathfrak{a}_i$인 것은 거의 자명하므로 surjectivity만 보이면 충분하다. 즉 임의의 원소

$$(x_1+\mathfrak{a}_1,\ldots,x_n+\mathfrak{a}_n)\in\prod A/\mathfrak{a}_i$$

에 대하여, 적절한 representative를 잡으면 이것이 $\pi$의 image에 들어있어야 한다. 

이를 위해서는 각각의 index $i$마다 $i$번째 자리만 $1$이고 다른 자리는 $0$인 역할을 할 원소

$$e_i\equiv 1\pmod{\mathfrak{a}_i},\qquad e_i\equiv 0 \pmod{\mathfrak{a}_j}\quad(j\neq i)$$

를 만들어주면 충분하며, 이를 보장하는 조건이 ideal들의 pairwise comaximal 조건이다. 고정된 $i$에 대하여 각 $j\ne i$마다 $\mathfrak{a}_i+\mathfrak{a}_j=A$이므로 $1=u_{ij}+v_{ij}$ ($u_{ij}\in\mathfrak{a}_i,\ v_{ij}\in\mathfrak{a}_j$)인 원소를 택할 수 있다. 이제

$$e_i=\prod_{j\ne i}v_{ij}$$

라 하자. 그럼 우선 각각의 $j\neq i$에 대하여, $e_i$는 $v_{ij}\in \mathfrak{a}_j$와 다른 원소들의 곱이므로 $e_i\in \mathfrak{a}_j$임이 자명하다. Index $i$에 대해서는, 

$$v_{ij}=1-u_{ij}\equiv 1\pmod{\mathfrak{a}_i}$$

이므로 $e_i\equiv 1\pmod{\mathfrak{a}_i}$이 성립한다. 이로부터 원하는 결과를 얻는다. 
:::

따라서, first isomorphism theorem에 의하여 다음의 canonical isomorphism

$$A\Big/\left(\bigcap_{i=1}^n \mathfrak{a}_i\right)\cong \prod_{i=1}^n A/\mathfrak{a}_i$$

이 존재한다. 만일 $A$가 commutative라면 [명제 5](#prop5)에 의하여 교집합을 곱으로 바꾸어 쓸 수 있으므로

$$A/\mathfrak{a}_1\cdots \mathfrak{a}_n\cong\prod_{i=1}^n A/\mathfrak{a}_i$$

이 되며, 특히 만일 $\bigcap \mathfrak{a}_i=0$이라면 isomorphism $A\cong\prod A/\mathfrak{a}_i$를 얻는다. 

도입부에서 언급한 정수 버전은 $A=\mathbb{Z}$인 특수한 경우이다. 즉, pairwise coprime인 $n_1,\ldots, n_r$에 대해 $\mathfrak{a}_i=n_i \mathbb{Z}$라 하고 $n=n_1\cdots n_r$이라 두면, 서로소 조건이 곧 comaximal 조건 $\mathfrak{a}_i+\mathfrak{a}_j=\mathbb{Z}$이 되므로 위 명제는 isomorphism $\mathbb{Z}/n \mathbb{Z}\cong\prod \mathbb{Z}/n_i \mathbb{Z}$을 준다. 

한편, [명제 6](#prop6)의 isomorphism $A\cong\prod A/\mathfrak{a}_i$는 ring $A$가 더 작은 ring들의 곱으로 쪼개진다는 강한 사실로, 이는 다음의 동치명제를 통해 깔끔하게 표현할 수 있다. 

::: 명제 7
Ring $A$와 그 center $C(A)$, 그리고 two-sided ideal들 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$이 주어졌다 하자. 다음이 모두 동치이다.

1. 위에서 정의한 $\pi:A \rightarrow \prod A/\mathfrak{a}_i$가 isomorphism이다.
2. 모든 $i\neq j$에 대하여 $\mathfrak{a}_i+\mathfrak{a}_j=A$이고 $\bigcap \mathfrak{a}_i=0$이다.
3. $C(A)$의 원소들 $e_1,\ldots, e_n$이 존재하여 $\sum e_i=1$이며, 모든 $i$에 대하여 $e_i^2=e_i$, 모든 $i\neq j$에 대하여 $e_ie_j=0$이 성립하고, 모든 $i$에 대해 $\mathfrak{a}_i=A(1-e_i)$이다.
:::
::: 증명
우선 처음 두 조건이 동치임은 [명제 6](#prop6)의 결과이다. 이제 둘째 조건을 가정하고 셋째 조건을 보이자. [명제 6](#prop6) 증명에서 힌트를 얻어, $\prod A/\mathfrak{a}_i$에서 $i$번째 성분만 $1+\mathfrak{a}_i$이고 나머지는 모두 $0$인 원소를 $\bar{e}_i$라 하자. 그럼 

$$\sum\bar{e}_i=\bar{1},\qquad \bar{e}_i^2=\bar{e}_i,\qquad \bar{e}_i\bar{e}_j=0$$

이 성립한다. 또, 각 성분이 quotient ring $A/\mathfrak{a}_i$의 항등원 또는 $0$이므로 $\bar{e}_i$가 $\prod A/\mathfrak{a}_i$의 center에 속하는 것도 자명하다. 이제 $e_i:=\pi^{-1}(\bar{e}_i)$라 두면 이들이 셋째 조건의 모든 등식들을 만족하는 것은 위의 식으로부터 자명하다. 등식 $\mathfrak{a}_i=A(1-e_i)$의 경우, $a\in\mathfrak{a}_i$라 하면 $a=ae_i+a(1-e_i)$인데, $ae_i$의 모든 성분이 $0$이 되어 $ae_i\in\bigcap\mathfrak{a}_i=0$이므로 $a=a(1-e_i)\in A(1-e_i)$이다. 반대로 $\bar{e}_i$의 $i$번째 성분이 $1+\mathfrak{a}_i$이므로 $1-e_i\in\mathfrak{a}_i$이고, 따라서 $A(1-e_i)\subseteq\mathfrak{a}_i$이다. 그러므로 $\mathfrak{a}_i=A(1-e_i)$이다.

마지막으로 셋째 조건을 가정하고 첫째 조건을 보이자. 우선 우리는 $A=\bigoplus_i Ae_i$임을 보인다. 이는 우선 임의의 $a\in A$에 대하여

$$a=a\cdot 1=a\sum_i e_i=\sum_i ae_i$$

이고, 만일 $x\in Ae_i\cap\sum_{j\neq i}Ae_j$라면 $x$는 $ae_i$꼴인 동시에 $\sum_{j\neq i} a_j e_j$ 꼴이며, 이를 만족할 수 있는 $x$는 $0$뿐이므로 이것이 direct sum을 준다는 것에서 얻어진다. 이제 $e_i\in C(A)$이므로 각 $Ae_i$는 항등원 $e_i$를 갖는 ring이며, morphism 

$$A\rightarrow Ae_i;\qquad a\mapsto ae_i$$

는 전사이고 그 kernel은 $A(1-e_i)=\mathfrak{a}_i$이므로 $A/\mathfrak{a}_i\cong Ae_i$이다. 이를 합치면, [\[대수적 구조\] §환의 곱, 쌍대곱, 텐서곱, ⁋정의 3](/ko/math/algebraic_structures/operations_of_rings#def3)에서 정의한 direct sum이 유한 지표에서는 direct product와 같으므로 

$$\bigoplus_{i=1}^n A/\mathfrak{a}_i\cong \prod_{i=1}^n A/\mathfrak{a}_i\cong\prod_{i=1}^n Ae_i\cong A$$

이며, 이 합성이 원래의 $\pi$와 일치하므로 $\pi$는 isomorphism이다.
:::

추가로, 만일 $A$가 commutative이면 [명제 5](#prop5)에 의하여 $\bigcap\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$이므로, 둘째 조건의 $\bigcap\mathfrak{a}_i=0$은 $\mathfrak{a}_1\cdots\mathfrak{a}_n=0$으로 바꾸어 써도 같다. 

## 비가환의 경우

[명제 5](#prop5)에서 commutative라는 가정은 교집합 $\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$이 단일한 곱 $\mathfrak{b}_1\cdots\mathfrak{b}_n$으로 떨어지는 것을 보장하기 위해 쓰였다. 이를 가정하지 않으면 여러 순서의 곱이 서로 다른 ideal이 될 수 있어, 교집합은 그 모든 순서의 곱을 더한 symmetric sum으로 나타나며, 다음 명제가 그 일반화된 버전을 준다.

::: 명제 8
Ring $A$의 two-sided ideal들 $\mathfrak{b}_1,\ldots, \mathfrak{b}_n$이 pairwise comaximal이라 하자. 그럼

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\sum_{\sigma\in S_n} \mathfrak{b}_{\sigma(1)}\cdots \mathfrak{b}_{\sigma(n)}$$

이 성립한다. 특히 $A$가 가환환이면 모든 순서의 곱이 같아지므로 [명제 5](#prop5)를 회복한다.
:::
::: 증명
[명제 5](#prop5)와 마찬가지로 귀납법으로 증명한다. 항상 $\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n)}\subseteq\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$이므로 역포함만 보이면 된다.

우선 $n=2$라 하자. pairwise comaximal 조건에서 $1=b_1+b_2$ ($b_i\in\mathfrak{b}_i$)인 원소를 택하면, 임의의 $x\in\mathfrak{b}_1\cap\mathfrak{b}_2$에 대하여

$$x=x\cdot 1=x(b_1+b_2)=xb_1+xb_2\in \mathfrak{b}_1\mathfrak{b}_2+\mathfrak{b}_2\mathfrak{b}_1$$

이다.

이제 $n>2$라 하자. [명제 4](#prop4)를 $\mathfrak{a}=\mathfrak{b}_n$, $(\mathfrak{b}_1,\ldots,\mathfrak{b}_{n-1})$에 적용하면 $A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})$이므로, 두 ideal $\mathfrak{b}_n$과 $\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1}$은 comaximal이다. 여기에 $n=2$의 결과를 적용하면

$$\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})\mathfrak{b}_n+\mathfrak{b}_n(\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1})$$

이다. 귀납가정 $\mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_{n-1}=\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}$을 대입하면 우변은

$$\left(\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}\right)\mathfrak{b}_n+\mathfrak{b}_n\left(\sum_{\sigma\in S_{n-1}}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n-1)}\right)$$

이며, 우변의 각 항이 $\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n)}$에 포함되므로 원하는 역포함을 얻는다.
:::

[명제 6](#prop6)의 kernel $\bigcap_i\mathfrak{a}_i$에 [명제 8](#prop8)을 적용하면, non-commutative case에서의 중국인의 나머지정리 역시

$$A\Big/\left(\sum_{\sigma\in S_n}\mathfrak{a}_{\sigma(1)}\cdots\mathfrak{a}_{\sigma(n)}\right)\cong \prod_{i=1}^n A/\mathfrak{a}_i$$

의 형태로 성립한다. 이는 본질적으로 [명제 6](#prop6)과 동일한 정보를 담고 있는 것으로, 차이는 commutative인 경우 이 kernel이 단일한 곱 $\mathfrak{a}_1\cdots\mathfrak{a}_n$으로 떨어져 그 형태가 단순해진다는 것뿐이다.

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---