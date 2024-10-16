---

title: "부분공간"
excerpt: "벡터공간의 부분공간과 벡터들의 일차결합"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/subspaces
sidebar: 
    nav: "linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Subspaces.png
    overlay_filter: 0.5

date: 2022-07-29
last_modified_at: 2022-07-29

weight: 3

---

## 부분공간

[§벡터공간, ⁋예시 6](/ko/math/linear_algebra/vector_spaces#ex6)을 보면, 어떤 벡터공간의 부분집합이 그 자체로 벡터공간을 이루는 경우가 종종 있다는 것을 알 수 있다. 이를 다음과 같이 정의하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 어떤 $\mathbb{k}$-벡터공간 $V$에 대하여, $V$의 부분집합 $W$가 $V$의 *부분공간<sub>subspace</sub>*이라는 것은, $V$ 위에 정의된 덧셈과 스칼라곱을 $W$ 위로 제한하였을 때 얻어지는 연산들이 $W$ 위에 다시 $\mathbb{k}$-벡터공간을 정의하는 것이다. 이를 $W\leq V$와 같이 표현한다.

</div>

정의에 의해, $C^k(I)$는 $C(I)$의 부분공간이고, $C(I)$는 $\Fun(I,\mathbb{R})$의 부분공간이 된다.

정의를 그대로 사용하여 $V$의 임의의 부분집합 $W$가 부분공간인지를 체크하기 위해서는 이들의 덧셈이 abelian group을 이루는지, 그리고 스칼라곱이 [§벡터공간, ⁋정의 1](/ko/math/linear_algebra/vector_spaces#def1)의 조건을 모두 만족하는지 등을 모두 따져봐야 한다. 하지만, $W$ 위에 정의될 덧셈과 스칼라곱은 $V$로부터 받아오는 것이므로, 몇 가지 성질들은 굳이 체크할 필요가 없다. 

예를 들어, 임의의 $w\_1,w\_2\in W$에 대해

$$w_1+w_2=w_2+w_1$$

이 성립하는지는 굳이 따져볼 필요가 없다. 두 원소 $w\_1,w\_2$는 $W$의 원소이기 이전에 $V$의 원소이기도 한데, $W$에서의 덧셈 $+$는 $V$에서의 덧셈을 $W$로 제한한 것이기 때문이다. 이를 바탕으로 우리가 체크해봐야 할 성질들을 따져보면 다음과 같다.

1. $W$가 덧셈에 대해 닫혀있는지의 여부는 따로 체크해봐야 한다. 
2. 이와 비슷하게, $V$가 덧셈에 대한 항등원과 역원을 갖는지도 체크해봐야 한다. 물론 $V$는 $0$과 $-w$를 포함하지만, 이들이 $W$에 포함되리라는 보장은 없기 때문이다.
3. 또, 임의의 스칼라 $\alpha\in\mathbb{k}$와 $w\in W$에 대하여, $\alpha w\in W$인지의 여부도 체크해봐야 한다.

하지만 여기에서 조금 더 조건을 간추릴 수도 있다. 만일 $W$가 스칼라곱에 대해 닫혀있기만 하다면, [§벡터공간, ⁋명제 2](/ko/math/linear_algebra/vector_spaces#prop2)와 [벡터공간, ⁋따름정리 3](/ko/math/linear_algebra/vector_spaces#cor3)에 의해 두 번째 조건은 통째로 생략할 수 있다. $W$가 스칼라곱에 대해 닫혀있으므로, $0w\in W$이고 $(-1)w\in W$여야 하는데, 이들이 각각 $0$과 $-w$이기 때문이다. 따라서 방금 우리는 다음 명제를 증명했다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $\mathbb{k}$-벡터공간 $V$에 대하여, $V$의 공집합이 아닌 부분집합 $W$가 $V$의 부분공간인 것은, $W$가 덧셈과 스칼라곱에 대해 닫혀있는 것과 동치이다.

</div>

하지만 $W$가 공집합이 아닌 것을 보이기 위해서는 $0\in W$임을 보이는 것이 가장 쉽기 때문에 보편적으로 앞서 제시했던 세 가지 조건과 앞선 명제는 활용성에 있어 큰 차이는 없다.

## 일차결합

$\mathbb{k}$-벡터공간 $V$와 그 부분공간 $W$를 생각하자. $W$의 임의의 두 원소의 합은 다시 $W$의 원소이므로, 귀납법에 의해 <em_ko>유한한</em_ko> 합은 다시 $W$의 원소이다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $V$가 $\mathbb{k}$-벡터공간이고 $W$가 $V$의 부분공간이라 하자. $W$의 원소들 $w_1,\ldots, w_n$과 스칼라들 $\alpha_1,\ldots,\alpha_n$에 대하여 다음의 유한합

$$\sum_{i=1}^n\alpha_i w_i=\alpha_1w_1+\alpha_2w_2+\cdots+\alpha_nw_n\tag{1}$$

은 $W$의 원소이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

귀납법을 이용하여 진행한다. $n=1$인 경우는 보일 것이 없으므로 $n=2$인 경우부터 생각하자. 이 경우 [명제 2](#prop2)에 의하여 $\alpha\_1w\_1,\alpha\_2w\_2$ 각각은 $W$의 원소이고 따라서 이들의 합 $\alpha\_1w\_1+\alpha\_2w\_2$ 또한 $W$의 원소이다.

일반적인 $n$에 대하여, $W$에서의 덧셈은 결합법칙을 만족하므로

$$\alpha_1w_1+\alpha_2w_2+\cdots+\alpha_nw_n=(\alpha_1w_1+\cdots\alpha_{n-1}w_{n-1})+\alpha_nw_n$$

이 성립한다. 이제 귀납적 가정에 의하여 $\alpha_1w_1+\cdots\alpha_{n-1}w_{n-1}$과 $\alpha_nw_n$ 각각은 $W$의 원소이고, 따라서 이들의 합 $\sum\_{i=1}^n\alpha\_iw\_i$ 또한 $W$의 원소이다.

</details>

일반적으로 위 명제의 (1)과 같은 형태의 벡터를 다음과 같이 이름 붙인다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $\mathbb{k}$-벡터공간 $V$와 그 원소들 $v_1,\ldots, v_n$에 대하여, 이들의 *일차결합<sub>linear combination</sub>*은

$$\alpha_1v_1+\cdots+\alpha_nv_n$$

의 꼴로 나타나는 벡터를 의미한다. 

</div>

더 일반적으로, 무한히 많은 $V$의 원소들 $(v_i)\_{i\in I}$이 주어졌을 때, 이들의 일차결합은

$$\sum_{i\in I}\alpha_iv_i\qquad\text{$\alpha_i=0$ for all but finitely many $i$}$$

으로 정의된다. 예를 들어, [§벡터공간, ⁋예시 4](/ko/math/linear_algebra/vector_spaces#ex4)와 같이 $\mathbb{R}$을 $\mathbb{Q}$-벡터공간으로 본다면, $0.111\ldots$는 다음 벡터들

$$0.1,\quad 0.01,\quad0.001,\quad\cdots$$

의 일차결합이 <em_ko>아니다</em_ko>. 이들을 사용하여 $0.111\ldots$를 위와 같이 무한합으로 나타낸다면 그 계수들이 모두 $0$이 아니기 때문이다. 이와 비슷한 맥락에서 다음 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 집합 $\mathbb{k}[\x]$를 

> $\mathbb{k}$의 원소를 계수로 갖는 $\x$에 대한 다항식들의 집합

으로 정의하자. 즉, $\mathbb{k}[\x]$의 각각의 원소들은 적당한 자연수 $n$과 $\alpha\_i\in\mathbb{k}$들에 대해

$$p(\x)=\alpha_n\x^n+\alpha_{n-1}\x^{n-1}+\cdots+\alpha_1\x+\alpha_0$$

의 꼴이다. 이 때 자연수 $\max\supp(\alpha\_i)=n$은 $p(\x)$의 *차수<sub>degree</sub>*라 부르고, 이 때 $\alpha\_n\x^n$을 *최고차항<sub>leading term</sub>*이라 부른다. 최고차항의 계수가 1인 다항식은 *monic polynomial*이라 부른다. 한편 또 다른 $\mathbb{k}[\x]$의 원소 

$$q(\x)=\beta_m\x^m+\beta_{m-1}\x^{m-1}+\cdots+\beta_1\x+\beta_0$$

가 주어졌다 하자. 그럼 이들의 합은 만약 $m>n$이라면,  

$$\sum_{i=0}^na_i\x^i+\sum_{i=0}^mb_i\x^i=\sum_{i=0}^m c_i\x^i,\qquad c_i=\begin{cases}a_i+b_i&\text{if $0\leq i\leq n$}\\ b_i&\text{if $n < i\leq m$}\end{cases}$$

그리고 반대의 경우

$$\sum_{i=0}^na_i\x^i+\sum_{i=0}^mb_i\x^i=\sum_{i=0}^m c_i'\x^i,\qquad c_i'=\begin{cases}a_i+\beta_i&\text{if $0\leq i\leq m$}\\ a_i&\text{if $m < i\leq n$}\end{cases}.$$

으로 정의되며, 임의의 스칼라 $\gamma\in\mathbb{k}$에 대하여

$$\gamma p(\x)=\gamma\alpha_n\x^n+\gamma\alpha_{n-1}\x^{n-1}+\cdots+\gamma\alpha_1\x+\alpha_0$$

으로 정의된다. 어렵지 않게 이들 정의가 $\mathbb{k}[\x]$에 $\mathbb{k}$-벡터공간 구조를 부여한다는 것을 확인할 수 있다.

이제 $n$차 이하의 차수를 갖는 다항식들의 집합 $\mathbb{k}[\x]_\text{degree\scriptsize$\leq n$}$는 $\mathbb{k}[\x]$의 부분공간이라는 것을 확인할 수 있다. 반면, <em_ko>정확히</em_ko> 차수 $n$을 갖는 다항식들의 집합은 부분공간이 아니다. 

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 이번에는 집합 $\mathbb{k}[[\x]]$를 

>$\mathbb{k}$의 원소를 계수로 갖는 $\x$에 대한 *formal power series*들의 집합

이라 하자. 앞선 [예시 7](#ex7)와 동일한 방식으로 벡터 사이의 덧셈과 스칼라곱을 정의하면, $\mathbb{k}[[\x]]$는 마찬가지로 $\mathbb{k}$-벡터공간이 된다.  

</div>

정의에 의하여 $\mathbb{k}[\x]$는 $\mathbb{k}[[\x]]$의 부분공간이다. 또, $\mathbb{k}[\x]$의 모든 원소들은 집합 $\\{1,\x,\x^2,\ldots\\}$의 벡터들의 일차결합으로 표현할 수 있지만, $\mathbb{k}[[\x]]$의 원소들은 그렇지 않다.

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---