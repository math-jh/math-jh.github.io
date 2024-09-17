---

title: "완전열"
excerpt: ""

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/exact_sequences
header:
    overlay_image: /assets/images/Math/Linear_Algebra/Exact_sequences.png
    overlay_filter: 0.5
sidebar: 
    nav: "linear_algebra-ko"

date: 2024-09-17
last_modified_at: 2024-09-17
weight: 1

---

[\[선형대수학\]](/ko/linear_algebra/) 카테고리에서 우리는 module의 성질에 대해 살펴본다. [\[대수적 구조\]](/ko/algebraic_structures/)에서 우리는 module의 성질을 살펴보긴 하였으나, 해당 카테고리에서는 일반적인 대수적인 구조들에서 공통적으로 정의하고 증명할 수 있는 것들에 초점을 두었다면, 이 카테고리에서는 조금 더 module만이 갖는 성질에 집중한다는 차이가 있다. 

예컨대 특별히 field $\mathbb{k}$ 위에 정의된 module들, 즉 $\mathbb{k}$-벡터공간들에 대한 결과들은 [\[기초 선형대수학\]](/ko/basic_linear_algebra/)에서 살펴보았었는데, 여기에서 $\mathbb{k}$-벡터공간들의 기저를 잡거나 이를 사용하여 linear map을 행렬로 표현하는 등의 일들은 일반적인 대수적 구조에서 기대하기는 힘든 일들이다. 

이와 같은 관점에서[\[선형대수학\]](/ko/linear_algebra/) 카테고리의 가장 큰 목표는 [\[기초 선형대수학\]](/ko/basic_linear_algebra/)에서의 결과들을 $\mathbb{k}$ 대신 일반적인 ring $A$로 바꾸어 최대한 일반화하는 것이라 할 수 있다. 한편 해당 카테고리의 글들은 비전공자 혹은 저년차 학부생을 염두에 두고 작성한 글들로 특히 [\[범주론\]](/ko/category_theory)의 언어를 거의 사용하지 않았었는데, 이와 같이 [\[기초 선형대수학\]](/ko/basic_linear_algebra/)의 내용들을 현대적인 언어로 바꾸는 것 또한 목표 중 하나이다. 

이 카테고리의 글들에서 $A$-module은 항상 left $A$-module을 뜻하며, 적절한 방식으로 동일한 논증을 right $A$-module에 대해서도 펼칠 수 있다. 같은 글 안에 left $A$-module과 right $A$-module이 동시에 등장해야 할 경우에는 혼동을 피하기 위해 이렇게 생략하지 않지만, 이러한 경우에도 left $A$-module을 right $A$-module로, right $A$-module을 left $A$-module로 서로 바꾸면 동일한 논증을 펼칠 수 있다.

## 가군의 합

우선 다음의 간단한 보조정리부터 시작한다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> $A$-module $M$의 submodule들의 family $(N_i)\_{i\in I}$에 대하여, 교집합 $\bigcap_{i\in I} N\_i$는 $M$의 submodule이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[기초 선형대수학\] §벡터공간의 기저, ⁋보조정리 3](/ko/math/basic_linear_algebra/basis#lem3)의 증명은 $\mathbb{k}$가 field라는 사실을 사용하지 않았으므로 해당 증명을 동일하게 사용하면 된다.

</details>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $A$-module $M$의 부분집합 $X$가 주어졌다 하자. 그럼 $X$를 포함하는 $M$의 submodule 중 가장 작은 것을 $\langle X\rangle$로 적고, 이를 $X$에 의해 생성되는 submodule이라 부른다. 이 경우 $X$를 $\langle X\rangle$의 *생성집합<sub>generating set</sub>*이라 부른다. 

만일 $M$의 어떤 submodule $N$에 대하여, $N=\langle X\rangle$이도록 하는 유한집합 $X$를 찾을 수 있다면 $N$이 *finitely generated<sub>유한생성</sub>*이라 부른다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $A$-module $M$의 임의의 부분집합 $X$에 대하여, $\langle X\rangle$은 $X$의 원소들로 이루어진 임의의 일차결합들의 집합과 같다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[기초 선형대수학\] §벡터공간의 기저, ⁋보조정리 4](/ko/math/basic_linear_algebra/basis#lem4)과 동일하게 증명하면 된다.

</details>

특별히 $A$-module $M$의 submodule들의 family $(N_i)_{i\in I}$가 주어졌다 하자. 그럼 $M$의 부분집합 $\bigcup N_i$로 생성된 $M$의 submodule $\left\langle \bigcup N_i\right\rangle$을 $\sum N_i$로 표기한다. 이제 각각의 $i$에 대하여, $N_i$는 $M$의 submodule이므로 inclusion들 $N_i \hookrightarrow M$이 존재한다. 이로부터 다음의 canonical morphism

$$\bigoplus_{i\in I} N_i \rightarrow M$$

이 존재한다. 한편 $\bigoplus N_i$는 canonical inclusion들 $N_i\hookrightarrow\bigoplus_{i\in I}N_i$의 합집합에 의해 생성되고, 위의 canonical morphism에 의한 이 합집합의 image가 $\bigoplus N_i$이므로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 위에서 정의한 canonical morphism $\bigoplus N_i \rightarrow M$의 image가 $\sum N_i$이다. 

</div>

즉 다음의 exact sequence

$$\bigoplus_{i\in I} N_i \rightarrow M \rightarrow M\bigg/\sum_{i\in I} N_i \rightarrow 0$$

가 존재한다.




앞서 우리는 $A$-module의 성질들을 정의하며 exact sequence와 exact functor의 개념을 사용했다. 이번 글에서는 몇가지 exact sequence들을 도입한다.

## 가군의 합

우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $A$-module $M$의 부분집합 $X$가 주어졌다 하자. 그럼 $X$의 원소들의 일차결합들로 이루어진 $M$의 부분집합을 $\langle X\rangle$으로 적는다.

</div>

그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $A$-module $M$과 그 부분집합 $X$가 주어졌다 하자. 그럼 $\langle X\rangle$은 $M$의 submodule이며, 

</div>



어렵지 않게 $X$를 포함하는 $M$의 submoule 중 가장 작은 것이 정확히 $\langle X\rangle$가 된다는 것을 확인할 수 있다. 특별히 $M$의 submodule들 $(N\_i)\_{i\in I}$에 대하여, 집합 $\bigcup_i N_i$로 generate되는 $M$의 submodule $\left\langle \bigcup N_i\right\rangle$를 $\sum N_i$로 적는다. 

이 submodule은 direct sum과도 어느정도 관련이 있다. 위의 family $(N_i)$에 대하여, canonical inclusion들 $N_i \rightarrow M$을 통해 얻어지는 canonical $A$-linear map $\bigoplus N_i \rightarrow M$의 image를 $N_i$들의 $M$에서의 direct sum이라 하고, 약간의 표기법의 남용을 통해 이를 $\bigoplus N_i$로 적는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위와 같은 상황에서 다음이 모두 동치이다.

1. $\sum_{i\in I} N_i=\bigoplus_{i\in I} N_i$이다.
2. 만일 $x_i\in N_i$를 만족하는 $x_i$들에 대하여 $\sum_{i\in I} x_i=0$이라면 모든 $i$에 대하여 $x_i=0$이다.
3. 임의의 $j\in I$에 대하여, $N_j$와 $\sum_{i\neq j} N_i$의 교집합이 $0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 조건의 동치관계는 자명하며, 또 $\bigoplus N_i$를 좌표별로 써 보면 첫 번째 조건이 마지막 조건을 함의하는 것도 자명하다. 이제 마지막 조건을 가정하고 두 번째 조건을 보이자. $\sum x_i=0$을 만족하는 $x_i\in N_i$들이 주어졌다 하자. 그럼 임의의 $j\in I$에 대하여,

$$x_j=\sum_{i\neq j}(-x_i)$$

이고, 마지막 조건을 가정한다면 위의 식으로부터 $x_j=0$이어야 하므로 증명이 완료된다.

</details>


$A$-module $M$을 고정하고, $M$의 submodule들의 family $(N_i)\_{i\in I}$가 주어졌다 하자. 그럼 $\bigcap N_i$는 $M$의 submodule이라는 것을 안다. 한편 각각의 $i$에 대하여, canonical homomorphism $M \rightarrow M/N_i$를 통해 얻어지는

$$\phi: M \rightarrow \prod_{i\in I} M/N_i$$

를 생각하자. 그럼 어렵지 않게 $\ker\phi=\bigcap N_i$라는 것을 확인할 수 있고, 그럼 다음의 exact sequence

$$0 \rightarrow \bigcap_{i\in I} N_i \rightarrow M  \rightarrow \prod_{i\in I} M/N_i$$

가 얻어진다. 특히 만일 $\bigcap_{i\in I} N_i=0$이라면 위의 sequence는 isomorphisom $M\cong\prod M/N_i$를 준다. 