---

title: "기저"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/basis_of_free_module
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Basis_of_free_module.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-08-18
last_modified_at: 2024-08-18
weight: 101

---

[\[대수적 구조\]](/ko/algebraic_structures/)에서 우리는 임의의 ring $A$ 위에 정의된 $A$-module을 정의하고, 이에 대한 기본적인 성질들을 살펴보았다. 이제 우리는 (left) $A$-module들에 대한 성질을 더 살펴본다.

## 기저

임의의 집합 $X$에 대하여, $X$에 의해 정의되는 free $A$-module은 다음의 식

$$F(X)=\bigoplus_{x\in X} Ax$$

으로 주어지는 것을 살펴보았다. ([\[대수적 구조\] §가군의 곱과 합, 텐서곱, ⁋명제 3](/ko/math/algebraic_structures/operations_of_modules#prop3)) 

더 일반적으로 임의의 $A$-module $M$이 주어졌다 하고, $M$의 원소들의 family $(x\_i)\_{i\in I}$들이 주어졌다 하자. 함수 $e:I \rightarrow M$을 $e(i)=x_i$로 정의한다면 adjunction $F\dashv U$에 의하여 유일한 $A$-linear map $\varepsilon:F(I) \rightarrow M$이 존재한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 $A$-module $M$과, $M$의 원소들의 family $(x\_i)\_{i\in I}$가 주어졌다 하자. 위에서 정의한 $A$-linear map $\varepsilon:F(I) \rightarrow M$에 대하여, 다음을 정의한다.

1. Family $(x\_i)\_{i\in I}$가 *일차독립<sub>linearly independent</sub>*라는 것은 $\varepsilon$이 injective인 것이다.
2. Family $(x\_i)\_{i\in I}$가 $M$을 *생성<sub>generate</sub>*하는 것은 $\varepsilon$이 surjective인 것이다.
3. Family $(x\_i)\_{i\in I}$가 $M$의 *basis<sub>기저</sub>*라는 것은 $\varepsilon$이 bijective인 것이다.

일차독립이 아닌 family를 *일차종속<sub>linearly dependent</sub>*라 한다. 임의의 $A$-module $M$과 $M$의 원소들의 family $(x\_i)\_{i\in I}$에 대하여, $(x\_i)\_{i\in I}$가 생성하는 $M$의 submodule을 $\langle (x\_i)\_{i\in I}\rangle$으로 표기한다.

</div>

앞서 [\[대수적 구조\] §가군, ⁋정의 2](/ko/math/algebraic_structures/modules#def2)에서 family $(x\_i)\_{i\in I}$가 $M$을 셍상하는 것이 어떤 것인지를 정의했었는데, 해당 글에서의 정의와 위의 정의가 동일하다는 것이 자명하다. 또, $A$-module $M$이 free module인 것과 $M$이 basis를 갖는 것이 동치이다. 

Basis의 중요한 성질 중 하나는 basis의 원소에서의 함수값들이 linear map을 완전히 결정짓는다는 것이다. 이를 확인하기 위해 free $A$-module $M$을 하나 고정하고, $(x\_i)\_{i\in I}$가 $M$의 basis라 하자. 즉 집합들 사이의 함수 $e_i: i\mapsto x\_i$가 $A$-module isomorphism $\varepsilon:F(I)\cong M$을 유도한다. 한편 또 다른 $A$-module $N$이 주어졌다 하고, $N$의 원소들의 family $(y\_i)\_{i\in I}$가 주어졌다 하면 함수들 $e_i': i\mapsto y\_i$가 $\varepsilon': F(I) \rightarrow N$을 유도한다. 그럼 $f(x\_i)=y\_i$를 만족하는 유일환 $A$-linear map $f:M \rightarrow N$이 존재하며, 명시적으로 이는 $f=\varepsilon'\circ\varepsilon^{-1}$으로 쓸 수 있다. 

임의의 $A$-module $M$은 항상 생성집합을 갖는다. 이는 적어도 $M$의 원소들을 전부 모아두면 이것이 $M$을 생성하기 때문이다. 따라서 위의 정의로부터 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 $A$-module $M$은 적당한 free $A$-module의 quotient와 isomorphic하다.

</div>

그럼 $M$이 finitely generated인 것은 이러한 free $A$-module이 유한한 개수의 basis를 갖도록 택할 수 있는 것과 동치이다. 

## 불변기저수

앞서 언급한 것과 같이 임의의 $A$-module $M$은 $M$ 자기 자신으로 생성된다. 그러나 이러한 자명한 케이스는 당연히 우리의 관심대상이 아니다. 우리는 가능한 한 작은 생성집합에 관심이 있고, 이러한 관점에서 $M$의 생성집합 중 가장 작은 것의 크기를 $M$의 불변량으로 정의하고자 한다. 그러나 이것이 말이 되기 위해서는 우선 다음의 정의를 내려야 한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 ring $A$에 대하여, $A^m\cong A^n$인 것과 $m=n$인 것이 항상 동치일 경우, $A$가 *invariant basis number property<sub>불변 기저수 성질</sub>*을 만족한다고 한다. 

</div>

예를들어, $A=0$은 이 성질을 만족하지 않는다. 임의의 $m,n$에 대해 $0^m\cong 0^n$이기 때문이다. 그러나 다음 정리가 잘 알려져 있다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 임의의 commutative ring $A\neq 0$은 IBN property을 만족한다.

</div>

IBN을 만족하는 또 다른 중요한 예시들로는 (left 혹은 right) noetherian ring, semilocal ring 등이 있다. 

어쩼든 IBN을 갖는 임의의 ring $A$에 대하여 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Ring $A$가 IBN을 만족한다 하자. 그럼 임의의 free $A$-module $M$에 대하여, $M$의 basis의 크기를 $M$의 *rank<sub>랭크</sub>*라 한다. 

</div>

편의상 $M$의 basis $(x\_i)\_{i\in I}$가 주어졌을 때, 이를 통해 얻어지는 free module $F(I)$를 $A^{\oplus I}$와 같이 나타내고, 특별히 $I$가 유한집합이면 $A^m$과 같이 나타내기도 한다. 이 표기법들은 $A$가 IBN property를 갖는다는 보장이 없을 때 사용할 경우 표기법 상의 문제가 있지만, 약간의 표기법의 남용을 통해 이를 눈감기로 한다.