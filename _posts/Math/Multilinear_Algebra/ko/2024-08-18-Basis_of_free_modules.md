---

title: "기저"
excerpt: ""

categories: [Math / Multilinear Algebra]
permalink: /ko/math/multilinear_algebra/basis_of_free_modules
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Basis_of_free_modules.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-ko"

date: 2024-08-18
last_modified_at: 2024-09-23
weight: 3

---

임의의 집합 $X$에 대하여, $X$에 의해 정의되는 free $A$-module은 다음의 식

$$F(X)=\bigoplus_{x\in X} A$$

으로 주어지는 것을 살펴보았다. ([\[대수적 구조\] §가군의 작접곱과 직합, 텐서곱, ⁋명제 3](/ko/math/algebraic_structures/operations_of_modules#prop3)) 이번 글에서 우리는 free $A$-module의 성질을 조금 더 자세히 살펴본다. 

## 기저

이제 임의의 $A$-module $M$이 주어졌다 하고, $M$의 원소들의 family $(x\_i)\_{i\in I}$들이 주어졌다 하자. 함수 $e:I \rightarrow M$을 $e(i)=x_i$로 정의한다면 adjunction $F\dashv U$에 의하여 유일한 $A$-linear map $\varepsilon:F(I) \rightarrow M$이 존재한다. 만일 $(x\_i)\_{i\in I}$가 $M$의 generating set이었다면, $\varepsilon$이 surjective여야 하고, 그 역 또한 성립한다. 이와 비슷한 맥락에서 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 $A$-module $M$과, $M$의 원소들의 family $(x\_i)\_{i\in I}$가 주어졌다 하자. 위에서 정의한 $A$-linear map $\varepsilon:F(I) \rightarrow M$에 대하여, 다음을 정의한다.

1. Family $(x\_i)\_{i\in I}$가 *free family<sub>자유족</sub>*라는 것은 $\varepsilon$이 injective인 것이다.
2. Family $(x\_i)\_{i\in I}$가 $M$을 *generate<sub>생성</sub>*하는 것은 $\varepsilon$이 surjective인 것이다.
3. Family $(x\_i)\_{i\in I}$가 $M$의 *basis<sub>기저</sub>*라는 것은 $\varepsilon$이 bijective인 것이다.

Free family가 아닌 family를 *related family*라 부른다.

</div>

Free family는 벡터공간에서의 일차독립의 개념을 일반화한 것이다. 즉, $A$가 field이고, $M$이 $A$ 위에 정의된 벡터공간이었다면 $M$의 원소들의 family $(x\_i)\_{i\in I}$가 free family라는 것은 $x\_i$들이 일차독립인 것과 동치이다. ([\[선형대수학\] §벡터공간의 기저, ⁋정의 5](/ko/math/linear_algebra/basis#def5)) 이러한 관점에서 related family의 원소들은 서로 *linearly dependent<sub>일차종속</sub>*이라 부른다. 

한편, 임의의 $A$-module $M$은 항상 생성집합을 갖는다. 이는 적어도 $M$의 원소들을 전부 모아두면 이것이 $M$을 생성하기 때문이다.  이로부터 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 $A$-module $M$은 적당한 free $A$-module의 quotient와 isomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $A$-module $M$에 대하여, $M$의 생성집합을 $X$라 하자. 그럼 $F(X)$와 $M$ 사이의 surjective $A$-linear map $\varepsilon:F(X) \rightarrow M$이 존재한다. 이 때, $F(X)$의 kernel은 $A$-module이므로, $M\cong F(X)/\ker\varepsilon$이다. 

</details>

$M$이 finitely generated $A$-module인 것은 이러한 family를 유한하게 택할 수 있는 것과 동치이며, 이 경우 위의 증명에서의 free $A$-module도 유한한 basis를 갖도록 택할 수 있다. 더 특수한 경우로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $A$-module $M$이 *monogenous<sub>단일생성</sub>*이라는 것은 $M$이 $A$-module로서 하나의 원소 $x$에 의해 생성되는 것이다.

</div>

주의할 점은 $x$가 free element일 필요가 없다는 것이다. 즉, 어떠한 $\alpha\neq 0$이 존재하여 $\alpha x=0$이 될 수도 있으며, 이것이 [\[선형대수학\]]()에서 다루던 것과 다른 점이다. 

## 불변기저수

우선 우리는 다음의 일반적인 명제를 증명한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $M=\bigoplus_{i\in I} N_i$이고, $I$가 무한집합이고 $N_i\neq 0$이라 하자. 그럼 $E$의 임의의 generating set $X$에 대하여, $\card X\geq \card I$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

[정의 3](#def3)의 상황에서, $M$의 임의의 원소는 적당한 $\alpha\in A$에 대하여 $\alpha x$의 꼴로 쓸 수 있다. 따라서 이러한 경우 $M$을 $Ax$와 같이 표기하기도 한다. 이 표기를 이용하면, 임의의 $A$-module $M$과 그 원소들의 family $(x_i)\_{i\in I}$에 대하여,

- $(x\_i)\_{i\in I}$가 $M$의 generating family인 것은 $M=\sum_{i\in I}Ax_i$인 것과 동치이다.
- $(x\_i)\_{i\in I}$가 $M$의 basis인 것은 위의 sum $\sum_{i\in I}Ax_i$가 direct sum이고, 각각의 $x_i$가 모두 free element인 것과 동치이다.

이를 통해 [명제 4](#prop4)을 각각의 $N_i$가 monogeneous이고 free element인 경우로 한정하면, 임의의 free $A$-module $M$가 무한한 basis를 갖는다면 $A$의 모든 basis는 같은 cardinality를 갖는다는 것을 안다. 그러나 유한한 basis를 갖는 경우 이것이 항상 성립하는 것은 아니다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 임의의 ring $A$에 대하여, $A^m\cong A^n$인 것과 $m=n$인 것이 항상 동치일 경우, $A$가 *invariant basis number property<sub>불변 기저수 성질</sub>*을 만족한다고 한다. 

</div>

예를들어, $A=0$은 이 성질을 만족하지 않는다. 임의의 $m,n$에 대해 $0^m\cong 0^n$이기 때문이다. 

[\[선형대수학\] §벡터공간의 차원, ⁋보조정리 2](/ko/math/linear_algebra/dimension#lem2)에 의해, 임의의 field는 invariant basis number property를 갖는다. 이를 사용하면 다음의 더 일반적인 명제를 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Ring $A$에 대하여, 적당한 field $\mathbb{K}$와 homomorphism $\phi: A \rightarrow \mathbb{K}$가 존재한다 하자. 그럼 $A$는 IBN property를 가진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 free $A$-module $M$이 주어졌다 하자. 그럼 다음의 isomorphism

$$M\cong \bigoplus_{i\in I} Ax_i$$

이 존재하고, $x_i$들 각각은 free element이다. 한편 $\phi^\ast:\lMod{A} \rightarrow \mathbb{K}$는 left adjoint이므로 다음 식

$$\phi^\ast M\cong\phi^\ast\left(\bigoplus_{i\in I} Ax_i\right)\cong \bigoplus_{i\in I}\phi^\ast Ax_i$$

이 성립한다. ([\[대수적 구조\] §스칼라의 변환, ⁋명제 6](/ko/math/algebraic_structures/change_of_base_ring#prop6)) 또, $x_i$가 free element라는 사실로부터 $Ax_i\cong A$이고, $\phi^\ast A\cong \mathbb{K}$이므로 $\phi^\ast M\cong \bigoplus_{i\in I}\mathbb{K}$이다. 이제 [\[선형대수학\] §벡터공간의 차원, ⁋보조정리 2](/ko/math/linear_algebra/dimension#lem2)를 적용하면 원하는 결과를 얻는다.

</details>

[\[선형대수학\] §무한차원 벡터공간<sup>†</sup>, ⁋정리 4](/ko/math/linear_algebra/infinite_dimensional_vector_space#thm4)에서 우리는 $\mathbb{K}$가 commutative라는 성질을 사용하지 않았으므로, 위의 명제는 더 일반적으로 $\mathbb{K}$를 division ring $D$로 바꾸어도 성립한다. 한편 임의의 commutative ring은 $A \rightarrow \Frac A$가 존재하므로 항상 IBN property를 갖는다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Ring $A$가 IBN을 만족한다 하자. 그럼 임의의 free $A$-module $M$에 대하여, $M$의 basis의 크기를 $M$의 *rank<sub>랭크</sub>*라 한다. 

</div>

편의상 $M$의 basis $(x\_i)\_{i\in I}$가 주어졌을 때, 이를 통해 얻어지는 free module $F(I)$를 $A^{\oplus I}$와 같이 나타내고, 특별히 $I$가 유한집합이면 $A^m$과 같이 나타내기도 한다. 이 표기법들은 $A$가 IBN property를 갖는다는 보장이 없을 때 사용할 경우 표기법 상의 문제가 있지만, 약간의 표기법의 남용을 통해 이를 눈감기로 한다. 

Basis의 중요한 성질 중 하나는 basis의 원소에서의 함수값들이 linear map을 완전히 결정짓는다는 것이다. 이를 확인하기 위해 free $A$-module $M$을 하나 고정하고, $(x\_i)\_{i\in I}$가 $M$의 basis라 하자. 즉 집합들 사이의 함수 $e_i: i\mapsto x\_i$가 $A$-module isomorphism $\varepsilon:F(I)\cong M$을 유도한다. 한편 또 다른 $A$-module $N$이 주어졌다 하고, $N$의 원소들의 family $(y\_i)\_{i\in I}$가 주어졌다 하면 함수들 $e_i': i\mapsto y\_i$가 $\varepsilon': F(I) \rightarrow N$을 유도한다. 그럼 $u(x\_i)=y\_i$를 만족하는 유일환 $A$-linear map $u:M \rightarrow N$이 존재하며, 명시적으로 이는 $u=\varepsilon'\circ\varepsilon^{-1}$으로 쓸 수 있다. 

## 대수의 기저

이제 우리는 대수의 기저에 대해 살펴보자. [선형대수학](/ko/linear_algebra) 카테고리에서 우리의 주된 관심사는 $A$-module이기는 하지만, 고정된 $A$-module의 endomorphism algebra를 살펴볼 때는 $A$-algebra를 생각하게 된다. 

앞서 $A$-algebra를 이야기할 때에는 항상 $A$가 commutative인 것을 가정했었다는 것을 기억하자.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 임의의 $A$-algebra $E$에 대하여, $E$의 basis는 $E$를 $A$-module로 취급했을 때의 basis를 의미한다. 

</div>

주의해야 할 점은, $E$의 basis는 $E$를 $A$-module로서 생성할 때는 최소이지만, $A$-algebra로서 생성하기 위해서는 더 작은 집합만이 필요할 수도 있다는 것이다. 가령 polynomial algebra $A[\x]$를 $A$-module로서 생성하기 위해서는 원소들 $1,\x,\x^2,\cdots$이 필요하지만, 이를 $A$-algebra로서 생성하기 위해서는 $1$과 $\x$만 있으면 충분하다. 

어쨌든 $E$의 basis $(e\_i)\_{i\in I}$는 여전히 $E$에 대한 모든 정보를 담고 있는데, 특히 $E$에 정의된 곱셈에 대한 정보를 basis들을 이용해 서술할 수 있다. 임의의 $i,j\in I$에 대하여, $e\_ie\_j$ 또한 $E$의 원소이므로 다음의 합

$$e_ie_j=\sum_{k\in I} \gamma_{ij}^k e_k$$

으로 나타낼 수 있다. 여기에서 $(\gamma\_{ij}^k)\_{i,j,k\in I}$는 $i,j$가 고정될 때마다 $\gamma_{ij}^k\neq 0$인 $k$가 오직 유한 개 뿐이다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 위에서 정의한 family $(\gamma_{ij}^k)\_{i,j,k\in I}$를 $E$의 *structure constant<sub>구조상수</sub>*라 부른다. 

</div>

그럼 임의의 $x,y\in E$에 대하여, 이들을 basis $(e\_i)$를 사용하여

$$x=\sum_{i\in I} x_i e_i,\qquad y=\sum_{j\in I} y_j e_j$$

로 적으면, 

$$xy=\sum_{i,j\in I} x_i y_j e_ie_j=\sum_{i,j,k\in I} x_i y_j \gamma_{ij}^k e_k$$

로 적을 수 있다. 거꾸로 위에서 설명한 유한성을 만족하는 family $(\gamma_{ij}^k)_{i,j,k\in I}$가 주어진다면, 이를 통해 임의의 $A$-module $E$ 위에 $A$-algebra 구조를 줄 수 있다. 

뿐만 아니라, $E$의 곱셈이 결합법칙과 교환법칙을 만족할 조건도 basis를 이용하여 표현할 수 있다. 위와 같은 식으로 $x,y,z$를 각각 basis를 이용하여 표현한 후, $(xy)z$와 $x(yz)$를 각각 나타내보면

$$(xy)z=\sum_{i,j,k\in I}x_i y_jz_k(e_ie_j)e_k,\qquad x(yz)=\sum_{i,j,k\in I} x_i y_j z_k e_i(e_je_k)$$

이므로 결합법칙이 성립하기 위해서는 basis를 구성하는 원소들 사이의 결합법칙이 성립하는 것만 확인하면 충분하다. 마찬가지 이유로 $E$의 곱셈이 교환법칙을 만족하려면 basis를 구성하는 원소들 사이의 교환법칙이 성립하는 것만 확인하면 충분하다.