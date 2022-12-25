---

title: "카테고리"
excerpt: "Category의 기본 정의"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/categories
header:
    overlay_image: /assets/images/Category_theory/Categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2021-09-21
last_modified_at:
weight: 1


---

범주론은 수학의 다른 분야들에 비해 최근에 나타났지만 수학 전반에 끼친 영향은 아주 지대해서, 집합론과 함께 현대수학의 근간을 이루고 있다고 해도 될 정도이다. 다만 이들 둘은 추구하는 방향이나 철학이 매우 다른데, 집합론은 수학을 단단하게 떠받치는 역할을 한다면 범주론은 수학의 분야들을 관통하는 더 큰 그림을 보는 학문에 가깝다. 때문에 범주론을 공부하기 위해서는 다른 분야들 전반에 대한 얕더라도 넓은 이해가 필요하다. 

## 카테고리의 정의

수학을 공부하다 보면 분명 서로 다른 분야임에도 불구하고 똑같은 일을 반복하는 경우가 흔하다. 예컨대 [집합론](/ko/set_theory/)에서 우리는 집합들 간의 함수를 정의하고 이를 분해하거나, 집합의 곱, 합, 몫 등을 정의하고 이들의 성질을 탐구했는데 이는 [대수적 구조](/ko/algebraic_structures/)를 다룰 때에도 동일하게 반복했던 일이다. 물론 [위상수학](/ko/topology/)이나 [미분다양체](/ko/manifold/)를 다룰 때에도 마찬가지였다. 카테고리는 이러한 개념들, 즉 어떠한 수학적인 <em_ko>대상</em_ko>들과 이들 사이의 <em_ko>함수</em_ko> 등을 가장 추상적인 방법으로 일반화한 것이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> *카테고리<sub>category</sub>* $\mathcal{C}$는 다음과 같은 데이터로 이루어진다.

- *대상<sub>object</sub>*들의 모임 $\obj(\mathcal{C})$,
- *정의역<sub>domain</sub>* $A\in\obj(\mathcal{C})$에서 *공역<sub>codomain</sub>* $B\in\obj(\mathcal{C})$로의 *morphism<sub>사상</sub>*들의 모임 $\Mor\_\mathcal{C}(A,B)$,
- 두 morphism $f\in\Mor\_\mathcal{C}(A,B)$, $g\in\Mor\_\mathcal{C}(B,C)$의 *합성<sub>composition</sub>* 

  $$\circ:\Mor_\mathcal{C}(A,B)\times\Mor_\mathcal{C}(B,C)\rightarrow\Mor_\mathcal{C}(A,C);\qquad (f,g)\mapsto g\circ f$$

추가적으로, 이들은 다음의 조건을 만족한다.

- Morphism들의 합성은 결합법칙을 만족한다. 즉, $(f\circ g)\circ h=f\circ(g\circ h)$가 성립한다.
- 각각의 $A\in\obj(\mathcal{C})$마다 $\id_A\in\Mor\_\mathcal{C}(A,A)$가 존재하여, 모든 $f\in\Mor\_\mathcal{C}(A,B)$ 그리고 모든 $g\in\Mor\_\mathcal{C}(C,A)$에 대하여
  
  $$f\circ{\id_A}=f,\qquad {\id_A}\circ g=g$$

  이 성립한다.

</div>

위의 정의에서 우리는 의도적으로 $\obj(\mathcal{C})$와 $\Mor\_\mathcal{C}(A,B)$들을 <em_ko>모임</em_ko>이라 불렀는데, 이는 대다수의 경우 이 모임들이 집합이 아니기 때문이다. 일반적으로 카테고리 $\mathcal{C}$의 <em_ko>모든</em_ko> morphism들을 모아둔 것이 집합이 된다면 $\mathcal{C}$를 *작은 카테고리<sub>small category</sub>*라 부르고, $A,B\in\obj(\mathcal{C})$가 고정될 때마다 $\Mor\_\mathcal{C}(A,B)$가 집합을 이룬다면 이를 *국소적으로 작은 카테고리<sub>locally small category</sub>*라 부른다. 어쨌든 우리는 집합론적인 이슈에 대해서는 덜 신경쓰기로 한다.

## 카테고리의 예시들

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (대수적 구조들)**</ins> 집합들의 카테고리 $\mathbf{Set}$이 존재한다. $\mathbf{Set}$의 대상들은 집합들이며, 두 집합 $A,B$ 사이의 morphism은 함수들이다. 두 morphism의 합성은 함수의 합성으로 주어진다.

이와 비슷하게, 마그마들의 카테고리 $\mathbf{Magma}$가 존재한다. $\mathbf{Magma}$의 대상들은 마그마들이며, 두 마그마 $A,B$ 사이의 morphism은 magma homomorphism이다. 마찬가지로 semigroup들의 카테고리 $\mathbf{Semigroup}$이나 monoid들의 카테고리 $\mathbf{Mon}$, group들의 카테고리 $\mathbf{Group}$ 등이 존재한다. 

Ring을 다룰 때는 약간의 컨벤션이 있는데, 보통 $\mathbf{Ring}$은 항등원 (**i**dentity)을 갖는 ring들의 카테고리를 뜻하고, 항등원을 갖지 않는 ring들의 카테고리는 $\mathbf{Rng}$로 적는다. 이 때 $\mathbf{Ring}$의 morphism들은 항등원 또한 보존하는 ring homomorphism들의 모임이다.

그 외 다른 대수적 구조들에 대한 카테고리들 $\mathbf{Field}$, $\mathbf{Vect}_K$, $\mathbf{Mod}_R$ 등이 정의된다.

</div>

서두에서 언급한 것과 같이, 대수적인 구조들 뿐만 아니라 다른 구조들도 카테고리의 언어로 쓸 수 있다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 위상공간들의 카테고리 $\mathbf{Top}$이 존재한다. $\mathbf{Top}$의 대상들은 위상공간들이며, 두 위상공간 $X,Y$ 사이의 morphism은 연속함수들이다. 비슷하게 (smooth) manifold들의 카테고리 $\mathbf{Man}$이 존재한다. 이들 사이의 morphism은 smooth map들이다.

</div>

앞선 예시들에서는 카테고리의 대상들이 모두 특정한 구조들이 주어져있는 집합이고, morphism들은 이 구조를 보존하는 함수들이었으나 [정의 1](#df1)의 어떠한 조건도 이를 강제하지는 않는다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 예를 들어, 임의의 ordered set $(S,\leq)$이 주어졌다 하자. 카테고리 $\mathbf{S}$를 다음과 같이 정의한다.

- $\obj(\mathbf{S})=S$이다. 즉, $\mathbf{S}$의 대상들은 $S$의 원소들이다.
- $\Mor\_\mathbf{S}(a,b)$의 경우, 만일 $a\leq b$라면 $\Mor\_\mathbf{S}(a,b)$가 하나의 원소를 갖는 것으로, 그렇지 않다면 $\Mor\_\mathbf{S}(a,b)$가 공집합인 것으로 생각한다. 논의의 편의를 위해 $\Mor\_\mathbf{S}(a,b)$의 (존재한다면) 유일한 원소를 $a\rightarrow b$로 적자.
- 두 모임 $\Mor\_\mathbf{S}(a,b)$와 $\Mor\_\mathbf{S}(b,c)$은 각각 $a\rightarrow b$, $b\rightarrow c$ 하나의 원소만 가지므로, 합성을 정의하기 위해서는 이들 둘의 합성을 정의하면 된다. 이는 $(a\rightarrow b, b\rightarrow c)\mapsto (a\rightarrow c)$로 정의한다.

그럼 $\id\_a$의 존재성은 $\leq$가 reflexive하다는 것으로부터 얻어지며, 위에서 정의한 합성이 잘 정의된다는 것은 $\leq$의 transitivity로부터 얻어진다. 또 $\Mor\_\mathbf{S}(a,a)$의 유일한 원소 $a\rightarrow a$가 실제로 $\id\_a$의 역할을 한다는 것이 자명하다.

</div>

## 동형사상

[예시 2](#ex2)의 대상들을 공부할 때 우리는 보통 전단사인 homomorphism이 곧 isomorphism이 되는 것을 확인할 수 있었다. 이를 정의로 채택하지 않은 것은 카테고리의 언어로부터 오는 것이다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Morphism $f:X\rightarrow Y$가 카테고리 $\mathcal{C}$에서의 *isomorphism<sub>동형사상</sub>*이라는 것은 적당한 morphism $g:Y\rightarrow X$가 존재하여 $\id\_X=g\circ f$이고 $\id\_Y=f\circ g$인 것이다.

이 경우, 두 대상 $X,Y$가 *isomophic*하다고 하고 $X\cong Y$로 표기한다.

</div>

가령, $\mathbf{Top}$에서는 전단사인 연속함수가 homeomorphism이 되지는 않았었다. 이러한 반례가 없었더라도, [예시 4](#ex4)와 같이 *전단사*라는 개념을 정의할 수 없는 morphism들도 존재하므로 isomorphism을 정의하는 방식은 위의 방식이 올바르다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> [예시 2](#ex2)에서, 집합들의 카테고리 $\mathbf{Set}$에서의 isomorphism은 bijection을 의미하고, 그 외 대수적 구조들에서의 isomorphism은 원래 정의했었던 isomorphism들과 같다.

[예시 3](#ex3)에서, $\mathbf{Top}$의 isomorphism은 homeomorphism이고, $\mathbf{Man}$의 isomorphism은 diffeomorphism이다.

마지막으로 [예시 4](#ex4)의 카테고리 $\mathbf{S}$의 유일한 isomorphism은 $\id_a=a\rightarrow a$들 뿐이다. 이는 $\leq$의 antisymmetry로부터 얻어진다.

</div>

## 부분카테고리

언제나와 같이 특정한 구조를 정의한 후에는 그 부분구조를 정의해야 한다. 카테고리 또한 예외가 아니다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 카테고리 $\mathcal{D}$가 카테고리 $\mathcal{C}$의 *부분카테고리<sub>subcategory</sub>*라는 것은 $\mathcal{D}$의 대상들과 morphism들이 모두 $\mathcal{C}$에 속하는 것이다.

</div>

가령, $\mathbf{Group}$은 $\mathbf{Mon}$의 부분카테고리이고, $\mathbf{Mon}$은 $\mathbf{Semigroup}$의 부분카테고리이다. Group 두 개 사이의 monoid homomorphism은 항상 group homomorphism이 되지만, monoid 둘 사이의 semigroup homomorphism이 반드시 monoid homomorphism이 되는 것은 아니다. 이러한 차이는 다음 글에서 자세히 살펴본다.

## 쌍대성

우리는 앞서 카테고리의 부분카테고리를 정의했는데, 그 동안의 흐름대로라면 카테고리들 사이의 morphism을 정의해야 할 차례다. 그 전에 우리는 간단하게 duality에 대하여 살펴본다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 카테고리 $\mathcal{C}$의 *opposite category<sub>반대 카테고리</sub>*는 다음과 같이 정의된 카테고리 $\mathcal{C}^\op$를 의미한다.

- $\mathcal{C}^\op$의 대상들은 $\mathcal{C}$의 대상들과 같다.
- $\mathcal{C}^\op$의 두 대상 $A,B$에 대하여, $\Mor\_{\mathcal{C}^\op}(A,B)=\Mor\_{\mathcal{C}}(B,A)$이다.
- $\mathcal{C}^\op$의 두 morphism $f^\op,g^\op$의 합성은 $(g\circ f)^\op$로 주어진다.

</div>

일반적으로 $\mathcal{C}$의 대상들은 점으로, morphism들은 화살표로 표현되므로, opposite category $\mathcal{C}^\op$는 $\mathcal{C}$의 대상들은 그대로 둔 채, 화살표의 방향만 거꾸로 뒤집은 것으로 이해할 수 있다. 이렇게 정의할 경우, 임의의 $A\in\obj\mathcal{C}$에 해당하는 항등사상 $\id\_A$를 거꾸로 뒤집은 $\id\_A^\op$가 $\mathcal{C}^\op$에서의 $A$의 항등사상 역할을 한다는 것을 쉽게 확인할 수 있다. 

## Monomorphism과 epimorphism

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> Category $\mathcal{C}$의 morphism $f:X\rightarrow Y$가 *monomorphism*이라는 것은 임의의 $Z\in\obj(\mathcal{C})$와 두 morphism $g_1,g_2:Z\rightarrow X$에 대하여 

$$f\circ g_1=f\circ g_2\implies g_1=g_2$$

이 성립하는 것이다. 또, $f:X\rightarrow Y$가 *epimorphism*이라는 것은 임의의 $Z\in\obj(\mathcal{C})$와 두 morphism $h_1,h_2:Y\rightarrow Z$에 대하여

$$h_1\circ f=h_2\circ f\implies h_1=h_2$$

이 성립하는 것이다.

</div>

정의로부터, $f$가 $\mathcal{C}$에서 monomorphism이라면 $f^\op$는 $\mathcal{C}^\op$에서 epimorphism이고, $f$가 $\mathcal{C}$에서 epimorphism이라면 $f^\op$는 $\mathcal{C}^\op$에서 monomorphism이다. 

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> Category $\mathbf{Set}$에서 monomorphism은 정확히 단사함수들이고, epimorphism은 정확히 전사함수들이다.

</div>

[\[집합론\] §Retraction과 section](/ko/math/set_theory/retraction_and_section)에서 우리는 retraction과 section을 정의했었는데, 이들 또한 서로의 정의에서 <em_ko>화살표를 뒤집어서</em_ko> 얻어지므로 해당 글의 모든 명제들이 전사함수와 단사함수 각각에서 성립했던 것은 duality에 의한 것으로 생각할 수 있다.

한편, 집합에서는 retraction과 section의 존재성이 각각 monomorphism과 epimorphism과 동치였는데, 일반적인 카테고리에서 이는 성립하지 않는다. 또, 집합에서는 monomorphism인 동시에 epimorphism인 morphism은 isomorphism이었지만 일반적인 카테고리에서는 이 또한 성립하지 않는다. 

---

**참고문헌**

**[Rie]** E. Riehl. <i>Category Theory in Context</i>. Dover Publications, 2017. (Also available in her [website](https://emilyriehl.github.io/files/context.pdf))

---