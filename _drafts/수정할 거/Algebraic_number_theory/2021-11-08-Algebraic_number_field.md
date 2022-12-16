---

title: "Algebraic number fields"
excerpt: "Fractional ideals and the Class group"

categories: [Math / Algebraic Number Theory]
permalink: /ko/math/algebraic_number_theory/algebraic_number_fields
header:
    overlay_image: /assets/images/Algebraic_number_theory/Algebraic_number_fields.png
    overlay_filter: 0.5
sidebar: 
    nav: "further_topics"

date: 2021-11-08
last_modified_at: 
weight: 6

published: false

---

<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


우리는 그동안 대수적 정수론에서 자주 사용할 도구들을 만들었다. 이제 이번 글에서는 우리가 그동안 예시로만 살펴봤던 $\mathbb{Q}$의 extension을 살펴본다. 앞선 주제와 마찬가지로, 여기에서도 $R$은 Dedekind domain, $K$는 $R$의 quotient field, $R'$은 finite-dimensional separable extension $L/K$에서의 $R$의 integral closure이다. 

## Norm of ideals

우리는 이미 특정한 원소의 norm을 주는 $N_{L/K}$라는 함수를 만든 적이 있다. 이 파트에서 $L/K$는 항상 고정되어 있으므로 간략히 이를 $N$이라 표기하기로 하자.

한편, 우리는 $L/K$의 integral basis $x_1,\ldots, x_n$이 주어졌을 때, 이들의 discriminant 또한 정의했었다. 물론 $x_i$들이 integral element가 아니어도 discriminant element를 정의하는 데에는 큰 문제는 없지만, integral basis에 대해서는 discriminant가 항상 $R$에 포함되고, 따라서 integral basis들 전체에 대해 discriminant가 취할 수 있는 값들을 모아두면 $R$의 ideal이 되었다. 이와 유사하게 ideal $\mathfrak{A}$의 *norm*을 정의한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $R'$의 ideal $\mathfrak{A}$에 대하여, $\mathfrak{A}$의 *norm*은 임의의 $a\in\mathfrak{A}$에 대하여, $N(a)$들로 generate되는 $R$의 ideal이다. 즉, $N(\mathfrak{A})=\sum_{a\in\mathfrak{A}}RN(a)$이다.

</div>

그럼 norm의 성질에서 다음과 같은 명제들을 얻는다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 다음이 항상 성립한다.

1. $N(ab)=N(a)N(b)$
2. $N(R'a)=RN(a)$
3. $N(\mathfrak{A})_S=N(\mathfrak{A}_S)$
4. $N(\mathfrak{A}\mathfrak{B})=N(\mathfrak{A})N(\mathfrak{B})$

</div>

다시 한 번 강조하자면, $N(\mathfrak{A})$는 $R$의 ideal이다. 따라서, 앞선 명제의 네 번째 조건은 ideal $N(\mathfrak{A}\mathfrak{B})$가 두 개의 ideal들의 product $N(\mathfrak{A})N(\mathfrak{B})$으로 분해될 수 있다는 것을 의미한다. 우리가 익숙한 Dedekind domain에서, 임의의 ideal은 항상 prime ideal들의 곱으로 표현할 수 있으므로, 이 factorization이 norm과 어떤 관계가 있는지 살펴보고 싶은 것이 당연한 바람일 것이다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $R'$의 nonzero prime ideal $\mathfrak{P}$와, $\mathfrak{p}=R\cap\mathfrak{P}$를 생각하자. 그럼 

$$N(\mathfrak{P})=\mathfrak{p}^f$$

가 성립한다. 여기서 $f$는 $\mathfrak{P}$의 relative degree $f(\mathfrak{P}/R)$이다.

</div>

따라서, 만일 $\mathfrak{A}$가 $R'$에서 prime ideal로의 factorization $\mathfrak{A}=\prod\mathfrak{P}_i^{a_i}$를 갖는다면 $\mathfrak{p}_i=\mathfrak{P}_i\cap R$, 그리고 $f_i=f(\mathfrak{P}/R)$에 대해 $N(\mathfrak{A})=\prod\mathfrak{p}_i^{a_if_i}$가 성립한다.

특별히 $K=\mathbb{Q}$이고 $R=\mathbb{Z}$인 경우를 생각하자. 그럼 $\operatorname{char}\mathbb{Q}=0$이므로 임의의 extension은 항상 separable이다. $L/\mathbb{Q}$가 finite dimensional extension이고, $R'$이 여기에서의 $\mathbb{Z}$의 integral closure라 하면 $\mathbb{Z}$는 PID이므로 $N(\mathfrak{A})$는 $R'$의 임의의 ideal $\mathfrak{A}$에 대하여 항상 principal ideal $m\mathbb{Z}$가 된다. $m$의 choice는 (up to multiple $-1$) 유일하고, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 위와 같은 상황에서, $N(\mathfrak{A})$는 $R'/\mathfrak{A}$의 element들의 갯수와 같다. 

</div>

그리고 많은 경우에 우리는 이와 같이 $K=\mathbb{Q}$이고 $R=\mathbb{Z}$, $L/\mathbb{Q}$는 finite dimensional인 경우를 생각할 것이다. 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $\mathbb{Q}$의 finite-dimensional extension $L$을 *algebraic number field*라 부르고, $L$의 원소들 중 $\mathbb{Z}$에 대해 integral인 원소들을 *algebraic integer*, 그리고 이들의 모임을 *ring of algebraic integers in $L$*이라 부른다. 

</div>

$\mathbb{Z}$는 Dedekind domain이므로, 우리는 $R'$ 또한 Dedekind domain이 된다는 것을 알고 있다. 우리는 추가적으로 $R'$이 explicit하게 어떻게 생겼는지도 알 수 있다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $L=\mathbb{Q}(\theta)$가 $\mathbb{Q}$의 $n$-dimensional extension이고, $\theta$가 algebraic integer라 하자. 또, $m=\lvert\Delta(1,\theta,\ldots,\theta^{n-1})\rvert$이라 하자. 그럼 $R'$은 $\theta$와, 다음의 집합

$$\left\{\frac{a_0+a_1\theta+\cdots+a_{n-1}\theta^{n-1}}{m}:0\leq a_i<m\right\}$$

의 원소들의 모임으로 generate된다. 

</div>

---

**References**

[Jan] Gerald J. Janusz. *Algebraic Number Fields*, American  Mathematical Soc., 1995

---
