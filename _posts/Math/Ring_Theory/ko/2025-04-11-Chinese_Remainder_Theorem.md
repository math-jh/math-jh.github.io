---
title: "중국인의 나머지정리"
description: "정수의 합동 문제에서 출발해 comaximal ideal 조건으로 일반화한 중국인의 나머지정리를 증명한다. 가환환에서 쌍별 comaximal ideal의 교차가 곱과 같아진다는 사실을 핵심 도구로 쓰며, 곱분해와 중심 idempotent 분해의 대응까지 다룬다."
excerpt: "Comaximal ideal에 대한 중국인의 나머지정리와 중심 idempotent 분해"

categories: [Math / Ring Theory]
permalink: /ko/math/ring_theory/chinese_remainder_theorem
sidebar: 
    nav: "ring_theory-ko"

date: 2025-04-11
weight: 3

---

중국인의 나머지정리는 정수의 합동에 대한 오래된 결과로 출발한다. 서로소인 두 정수 $m,n$과 정수 $a,b$에 대하여, 연립 합동식 $x\equiv a \pmod m$, $x\equiv b \pmod n$을 만족하는 정수 $x$가 법 $mn$에 대해 정확히 하나 존재한다는 것이다. 이 사실은 환 동형 $\mathbb{Z}/mn\mathbb{Z}\cong \mathbb{Z}/m\mathbb{Z}\times \mathbb{Z}/n\mathbb{Z}$와 본질적으로 같은데, 각 정수가 $\bmod m$에서의 나머지와 $\bmod n$에서의 나머지의 순서쌍으로 완벽히 복원되기 때문이다. 가령 $x\equiv 2\pmod 3$, $x\equiv 3\pmod 5$를 만족하는 $x$는 $\bmod{15}$에서 $x\equiv 8$로 유일하게 결정된다.

이를 임의의 환 $A$의 ideal로 일반화하는 것이 이 글의 목표이다. 여기서 "서로소"에 해당하는 ideal의 조건은 *comaximal*이다. 두 ideal $\mathfrak{a},\mathfrak{b}$가 $\mathfrak{a}+\mathfrak{b}=A$를 만족할 때 comaximal이라 부르는데, 이는 $1=u+v$ ($u\in\mathfrak{a}, v\in\mathfrak{b}$)꼴의 표현이 존재한다는 뜻이며 정수의 $1=\gcd(m,n)$·Bézout 표현과 정확히 대응한다. 일반화된 정리는 쌍별 comaximal인 ideal들 $\mathfrak{a}_i$에 대하여 환 동형

$$A/\Big(\bigcap_i \mathfrak{a}_i\Big)\cong \prod_i A/\mathfrak{a}_i$$

가 성립한다는 형태이고, $A$가 가환환이라면 뒤에 보일 교차-곱 등식 $\bigcap_i\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$에 의해 $A/\mathfrak{a}_1\cdots\mathfrak{a}_n\cong\prod_i A/\mathfrak{a}_i$로도 쓸 수 있다.

이 마지막 등식 $\bigcap\mathfrak{a}_i=\prod\mathfrak{a}_i$는 comaximal 조건이 있어야만, 그리고 가환이어야만 성립하는 미묘한 사실이다. 정리 본증명에 앞서 ideal의 곱을 정의하고 이 등식부터 확보하자.

## Ideal의 곱

::: 정의 1
Ring $A$의 두 two-sided ideal $\mathfrak{a},\mathfrak{b}$에 대하여, 이들의 *곱<sub>product</sub>* $\mathfrak{a}\mathfrak{b}$는 다음 집합

$$\mathfrak{a}\mathfrak{b}=\{x_1y_1+x_2y_2+\cdots+x_ny_n: x_i\in \mathfrak{a}, y_i\in \mathfrak{b}, n\geq 1\}$$

을 의미한다. 
:::

$\mathfrak{a}\mathfrak{b}$이 $A$의 덧셈에 대한 subgroup임은 자명하다. 한편 $\mathfrak{a}\mathfrak{b}$의 임의의 원소 $x_1y_1+\cdots+x_ny_n$와, $A$의 임의의 원소 $x$에 대하여,

$$x(x_1y_1+\cdots+x_ny_n)=xx_1y_1+\cdots xx_ny_n$$

이고 $xx_i\in \mathfrak{a}$이므로 $x(x_1y_1+\cdots+x_ny_n)\in \mathfrak{a}\mathfrak{b}$이다. $x$를 오른쪽에 곱해도 비슷한 논증이 성립하므로, $\mathfrak{a}\mathfrak{b}$는 $A$의 two-sided ideal인 것을 확인할 수 있다.

::: 명제 2
위와 같이 정의된 곱셈에 대하여, $A$의 two-sided ideal들의 모임은 항등원을 $A$로 하는 monoid 구조를 가진다. 뿐만 아니라, 분배법칙

$$\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c},\quad (\mathfrak{a}+\mathfrak{b})\mathfrak{c}=\mathfrak{a}\mathfrak{c}+\mathfrak{b}\mathfrak{c}$$

도 성립한다.
:::
::: 증명
세 two-sided ideal $\mathfrak{a},\mathfrak{b},\mathfrak{c}$가 주어졌다 하자. 그럼 $(\mathfrak{a}\mathfrak{b})\mathfrak{c}$의 임의의 원소는

$$\left(\sum_{i=1}^{n_1} x_i^{(1)}y_i^{(1)}\right)z_1+\cdots+\left(\sum_{i=1}^{n_k}x_i^{(k)}y_i^{(k)}\right)z_k$$

의 꼴로 쓰일 수 있으며, 분배법칙을 이용하여 이를 모두 풀어준 후 오른쪽 두 개를 묶어주면 이 원소가 $\mathfrak{a}(\mathfrak{b}\mathfrak{c})$에 속하는 것을 알 수 있다. 반대 방향 포함관계도 똑같은 방식으로 증명할 수 있으므로, 곱셈이 결합법칙을 만족한다. 또, 임의의 two-sided ideal $\mathfrak{a}$에 대해 $A \mathfrak{a}=\mathfrak{a}A=\mathfrak{a}$임이 자명하다. 

마지막으로 임의의 $b_1+c_1,\ldots, b_n+c_n\in \mathfrak{b}+\mathfrak{c}$에 대하여 

$$a_1(b_1+c_1)+\cdots a_n(b_n+c_n)$$

을 분배법칙을 사용하여 풀어주면 $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})\subset \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$를 쉽게 보일 수 있다. 거꾸로 임의의

$$a_1b_1+\cdots a_nb_n + a_1'c_1+\cdots +a_m'c_m\in \mathfrak{a}\mathfrak{b}+\mathfrak{a}\mathfrak{c}$$

에 대하여, $b_i$들과 $c_i$들이 모두 $\mathfrak{b}+\mathfrak{c}$의 원소이므로 위의 원소는 $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})$의 원소이다. 비슷하게 오른쪽 분배법칙도 증명할 수 있다.
:::

임의의 두 two-sided ideal $\mathfrak{a},\mathfrak{b}$에 대하여, 다음 두 식

$$\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}A\subset \mathfrak{a},\quad \mathfrak{a}\mathfrak{b}\subset A \mathfrak{b}\subset \mathfrak{b}$$

이 모두 성립하므로 $\mathfrak{a}\mathfrak{b}\subset \mathfrak{a}\cap \mathfrak{b}$이 성립한다. 일반적으로 등호가 성립할 필요는 없지만, comaximal한 경우에는 놀랍게도 등호가 성립한다. 이를 위해 먼저 다음 보조 결과를 보인다.

::: 명제 3
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

이제 가환환에서 쓸 핵심 도구를 얻는다.

::: 명제 4
가환환 $A$의 ideal들 $\mathfrak{b}_1,\ldots, \mathfrak{b}_n$이 쌍별로 comaximal, 즉 $i\neq j$에 대하여 $\mathfrak{b}_i+\mathfrak{b}_j=A$를 만족한다 하자. 그럼

$$\mathfrak{b}_1\cap \cdots\cap \mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

이 성립한다.
:::
::: 증명
귀납법으로 증명한다. 항상 $\mathfrak{b}_1\cdots\mathfrak{b}_n\subseteq \mathfrak{b}_1\cap\cdots\cap\mathfrak{b}_n$이므로 역포함만 보이면 된다.

우선 $n=2$이고 $\mathfrak{b}_1+\mathfrak{b}_2=A$라 하자. $1=u+v$ ($u\in\mathfrak{b}_1, v\in\mathfrak{b}_2$)로 두면, 임의의 $x\in\mathfrak{b}_1\cap\mathfrak{b}_2$에 대하여 $A$가 가환이라는 사실을 써서

$$x=x\cdot 1=x(u+v)=xu+xv\in \mathfrak{b}_2 \mathfrak{b}_1+\mathfrak{b}_1 \mathfrak{b}_2=\mathfrak{b}_1 \mathfrak{b}_2$$

이다. 따라서 $\mathfrak{b}_1\cap\mathfrak{b}_2=\mathfrak{b}_1\mathfrak{b}_2$이다.

이제 $n>2$라 하자. [명제 3](#prop3)을 $\mathfrak{a}=\mathfrak{b}_n$과 $\mathfrak{b}_1,\ldots,\mathfrak{b}_{n-1}$에 적용하면 (이들이 쌍별 comaximal임은 자명하다) 

$$A=\mathfrak{b}_n+(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})$$

이고, 귀납가정으로 $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}=\mathfrak{b}_1\cdots \mathfrak{b}_{n-1}$이다. 이제 $n=2$의 결과를 comaximal인 두 ideal $\mathfrak{b}_n$과 $\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1}$에 적용하면

$$\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\cap \mathfrak{b}_n=(\mathfrak{b}_1\cap\cdots\cap \mathfrak{b}_{n-1})\mathfrak{b}_n=\mathfrak{b}_1\cdots \mathfrak{b}_n$$

을 얻는다.
:::

(참고로 $A$가 가환이 아닐 때는 교차가 $\mathfrak{b}_1\cdots\mathfrak{b}_n$ 한 항이 아니라 모든 순서의 곱을 더한 대칭합 $\sum_{\sigma\in S_n}\mathfrak{b}_{\sigma(1)}\cdots\mathfrak{b}_{\sigma(n)}$과 같아지며, 가환일 때 비로소 이것이 단일한 곱으로 수렴한다. 이 글의 본론인 가환 경우에서는 위 등식으로 충분하다.)

## 중국인의 나머지 정리

Ring $A$와, $A$의 two-sided ideal들 $\mathfrak{a}_i$가 주어졌다 하자. 그럼 각 몫환으로의 projection들 $\pi_i:A \rightarrow A/\mathfrak{a}_i$이 존재하며, 이들로부터 ring homomorphism $\pi:A \rightarrow\prod A/\mathfrak{a}_i$가 정의된다. 이 사상이 언제 동형이 되는지가 중국인의 나머지정리의 핵심이다.

::: 명제 5
Ring $A$와, $A$의 two-sided ideal들 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$이 주어졌다 하자. 만일 $i\neq j$에 대하여 $\mathfrak{a}_i+\mathfrak{a}_j=A$가 항상 성립한다면 위에서 정의한 $\pi:A \rightarrow \prod_1^n A/\mathfrak{a}_i$는 surjective이고, 이 map의 kernel은 $\bigcap \mathfrak{a}_i$와 같다.
:::
::: 증명
명백히 $\ker\pi=\bigcap_i \mathfrak{a}_i$이므로 전사성만 보이면 충분하다. 임의의 목표값 $(x_1+\mathfrak{a}_1,\ldots,x_n+\mathfrak{a}_n)\in\prod A/\mathfrak{a}_i$에 대하여 이를 $\pi$의 image에서 실현하는 원소를 직접 만들어보자.

각 $i$마다 $i$번째 자리만 $1$이고 다른 자리는 $0$인 역할을 할 원소 $e_i\in A$, 즉 $e_i\equiv 1\pmod{\mathfrak{a}_i}$이고 $e_i\equiv 0\pmod{\mathfrak{a}_j}$ ($j\ne i$)를 만족하는 것을 찾으면 $x=\sum_i x_i e_i$가 모든 자리의 목표값을 한꺼번에 맞춘다. 쌍별 comaximal 조건에서 이러한 $e_i$를 명시적으로 구성하자. 고정된 $i$에 대하여 각 $j\ne i$마다 $\mathfrak{a}_i+\mathfrak{a}_j=A$이므로 $1=u_{ij}+v_{ij}$ ($u_{ij}\in\mathfrak{a}_i,\ v_{ij}\in\mathfrak{a}_j$)인 원소를 택할 수 있고, 

$$e_i=\prod_{j\ne i}v_{ij}$$

라 두자. 각 $j\ne i$에 대하여 $e_i$의 인자 중 $v_{ij}\in\mathfrak{a}_j$가 있으므로 $e_i\in\mathfrak{a}_j$이고, 반면 $\mathfrak{a}_i$에 대해서는 $v_{ij}=1-u_{ij}\equiv 1\pmod{\mathfrak{a}_i}$이므로 $e_i\equiv 1\pmod{\mathfrak{a}_i}$이다. 그러므로 $x=\sum_i x_i e_i$는 $\pi_i(x)=x_i+\mathfrak{a}_i$를 만족하여 $\pi$는 전사이다.
:::

따라서, first isomorphism theorem에 의하여 다음의 canonical isomorphism

$$\frac{A}{\bigcap_{i=1}^n \mathfrak{a}_i}\cong \prod_{i=1}^n A/\mathfrak{a}_i$$

이 존재한다. 만일 $A$가 가환환이라면 [명제 4](#prop4)에 의하여 교차를 곱으로 바꾸어 쓸 수 있어

$$A/\mathfrak{a}_1\cdots \mathfrak{a}_n\cong\prod_{i=1}^n A/\mathfrak{a}_i$$

이 되며, 특히 $\bigcap \mathfrak{a}_i=0$이라면 isomorphism $A\cong\prod A/\mathfrak{a}_i$를 얻는다. 

원래의 정수 버전은 $A=\mathbb{Z}$인 특수한 경우이다. 쌍마다 서로소인 $n_1,\ldots, n_r$에 대해 $\mathfrak{a}_i=n_i \mathbb{Z}$라 하고 $n=n_1\cdots n_r$이라 두면, 서로소 조건이 곧 comaximal 조건 $\mathfrak{a}_i+\mathfrak{a}_j=\mathbb{Z}$이 되므로 위 명제는 isomorphism $\mathbb{Z}/n \mathbb{Z}\cong\prod \mathbb{Z}/n_i \mathbb{Z}$을 준다. 다시 말해 임의의 나머지들의 순서쌍 $(a_i \bmod n_i)_i$에 대하여 이를 동시에 실현하는 정수가 법 $n$에서 유일하게 존재한다는 것이고, 이것이 고전적인 중국인의 나머지정리이다.

명제 5의 동형 $A\cong\prod A/\mathfrak{a}_i$는 환 $A$가 더 작은 환들의 곱으로 쪼개진다는 강한 사실이다. 이러한 곱분해는 환의 *center에 놓인 idempotent*들로 깔끔하게 기술되며, 이는 다음 동치 명제의 내용이다. (idempotent를 본격적으로 다루는 것은 다음 글의 주제이므로 여기서는 짧게 언급만 한다.)

::: 명제 6
Ring $A$와 그 center $C(A)$, 그리고 two-sided ideal들 $\mathfrak{a}_1,\ldots, \mathfrak{a}_n$이 주어졌다 하자. 다음이 모두 동치이다.

1. 위에서 정의한 $\pi:A \rightarrow \prod A/\mathfrak{a}_i$가 isomorphism이다.
2. 모든 $i\neq j$에 대하여 $\mathfrak{a}_i+\mathfrak{a}_j=A$이고 $\bigcap \mathfrak{a}_i=0$이다.
3. $C(A)$의 원소들 $e_1,\ldots, e_n$이 존재하여 $\sum e_i=1$이며, 모든 $i$에 대하여 $e_i^2=e_i$, 모든 $i\neq j$에 대하여 $e_ie_j=0$이 성립하고, 모든 $i$에 대해 $\mathfrak{a}_i=A(1-e_i)$이다.
:::
::: 증명
세 조건이 (1)$\Leftrightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(1)의 순환으로 동치임을 보인다.

(1)$\Leftrightarrow$(2): [명제 5](#prop5)에 의해 $\pi$가 전사인 것은 쌍별 comaximal 조건과 동치이고, 항상 $\ker\pi=\bigcap\mathfrak{a}_i$이므로, $\pi$가 동형인 것은 (2)와 동치이다.

(2)$\Rightarrow$(3): (2)에 의해 $\pi$는 동형이다. $\prod A/\mathfrak{a}_i$에서 $i$번째 성분만 $1+\mathfrak{a}_i$이고 나머지는 모두 $0$인 원소를 $\bar{e}_i$라 하자. 그럼 $\sum\bar{e}_i=\bar{1}$, $\bar{e}_i^2=\bar{e}_i$, $\bar{e}_i\bar{e}_j=0$이 성립하며, 각 성분이 몫환의 항등원 또는 $0$이므로 $\bar{e}_i$는 $\prod A/\mathfrak{a}_i$의 center에 속한다. $e_i:=\pi^{-1}(\bar{e}_i)$라 두면, $\pi$가 동형인 덕분에 $e_i\in C(A)$이며 $e_i$들은 위 idempotent·직교 관계를 그대로 계승한다. 또한 $\bar{e}_i$의 $i$번째 성분이 $1$이므로 $1-e_i$는 $\pi_i$ 아래 $0$으로 가고, 따라서 $1-e_i\in\ker\pi_i=\mathfrak{a}_i$이다. 그래서 $A(1-e_i)\subseteq \mathfrak{a}_i$이다. 역으로 $a\in\mathfrak{a}_i$라 하면 $a=ae_i+a(1-e_i)$인데, $ae_i$의 모든 성분이 $0$이 되어($i$번째는 $\pi_i(a)\pi_i(e_i)=0\cdot 1=0$, 나머지 성분에서 $\bar{e}_i$는 $0$) $ae_i\in\bigcap\mathfrak{a}_i=0$이므로 $a=a(1-e_i)\in A(1-e_i)$이다. 즉 $\mathfrak{a}_i=A(1-e_i)$이다.

(3)$\Rightarrow$(1): $e_i\in C(A)$이고 이들이 직교 idempotent이며 $\sum e_i=1$을 이루므로 $A=\bigoplus_i Ae_i$이다. 사상 $A\to Ae_i$, $a\mapsto ae_i$는 전사이고 그 kernel은 $A(1-e_i)=\mathfrak{a}_i$이므로 $A/\mathfrak{a}_i\cong Ae_i$이다. 이를 합치면 $\prod A/\mathfrak{a}_i\cong\prod Ae_i\cong A$이며, 이 합성이 원래 사상 $\pi$와 일치하므로 $\pi$는 동형이다.
:::

$A$가 가환환이면 [명제 4](#prop4)에 의하여 $\bigcap\mathfrak{a}_i=\mathfrak{a}_1\cdots\mathfrak{a}_n$이므로, 조건 2의 $\bigcap\mathfrak{a}_i=0$은 $\mathfrak{a}_1\cdots\mathfrak{a}_n=0$으로 바꾸어 써도 같다. 
