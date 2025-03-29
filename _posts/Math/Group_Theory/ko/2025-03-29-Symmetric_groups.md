---

title: "대칭군"
excerpt: ""

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/symmetric_groups
header:
    overlay_image: /assets/images/Math/Group_Theory/Symmetric_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "group_theory-ko"

date: 2025-03-29
last_modified_at: 2025-03-29
weight: 1

---

[대수적 구조](/ko/algebraic_structures) 카테고리에서 우리는 다양한 대수적인 구조들이 갖는 공통적인 성질에 관심이 있었는데, 이러한 방식은 대수적인 이론들이 어떻게 전개되는지를 전체적인 관점에서 조망하기에는 좋지만 실제로 특정한 군을 계산하거나 하는 등의 세부적인 부분을 살펴볼 때에는 좋지 않다. 때문에 이 카테고리의 글에서 우리는 [대수적 구조](/ko/algebraic_structures) 카테고리에서 다루지 않은 group의 성질들에 대해 살펴본다. 

## 대칭군

[군론](/ko/group_theory) 카테고리에서 처음으로 살펴볼 것은 특정한 group들이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 집합 $[n]=\\{1,\ldots, n\\}$에 대하여, $[n]$의 $\Set$에서의 automorphism group $\Aut([n])$을 *symmetric group<sub>대칭군</sub>*이라 부르고 $S_n$으로 적는다.  

</div>

즉 $S_n$의 원소들은 집합 $[n]$에서 $[n]$으로 가는 전단사함수들이며, $S_n$의 연산은 함수의 합성으로 주어진다. $S_n$의 원소들은 *permutation*이라 부른다.

Permutation $\sigma: [n] \rightarrow [n]$이 주어졌다 하고, 집합 $[n]$의 $n+1$개의 원소들

$$1=\sigma^0(1), \quad\sigma(1)=\sigma^1(1),\quad\sigma^2(1),\quad\cdots, \quad\sigma^n(1)\tag{$\ast$}$$

을 생각하자. 비둘기집 원리에 의하여 서로 다른 적당한 두 정수 $0\leq k_1,k_2\leq n$가 존재하여 $\sigma^{k_1}(1)=\sigma^{k_2}(1)$이 성립하고, 편의상 $k_1< k_2$라 하면 이로부터 $\sigma^{k_2-k_1}(1)=0$임을 안다. 뿐만 아니라, $\sigma^k(1)=1$을 만족하는 가장 작은 자연수 $k$를 생각하면, 위의 결과로부터 $k\leq n$이며, 이를 바탕으로 다음의 표기

$$(1\quad \sigma(1)\quad \sigma(1)\quad\cdots\quad\sigma^{k-1}(1))$$

를 생각할 수 있다. 정의에 의해 이 표기는 $1$을 $\sigma(1)$로, $\sigma(1)$을 $\sigma^2(1)$로, $\ldots$, $\sigma^{k-2}(1)$을 $\sigma^{k-1}(1)$로, 그리고 $\sigma^{k-1}(1)$을 $\sigma^k(1)=1$로 보내는 함수를 의미하며, 더 일반적으로

$$(a_1\quad a_2\quad\cdots\quad a_{k})$$

은 $a_1$을 $a_2$로, $\ldots$, $a_{k-1}$을 $a_{k}$로, 그리고 $a_k$을 $a_1$로 보내고 나머지 원소들은 건드리지 않는 함수를 의미하며, 이를 길이 $k$의 *cycle*이라 부른다. 그럼 두 cycle $\sigma$, $\tau$에 대하여, $\sigma\tau$는 함수 $\sigma$와 $\tau$의 합성 $\sigma\circ\tau$를 의미한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 

</div>