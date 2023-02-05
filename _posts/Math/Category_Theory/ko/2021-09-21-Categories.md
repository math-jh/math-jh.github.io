---

title: "카테고리"
excerpt: "Category의 기본 정의"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2021-09-21
last_modified_at:
weight: 1


---

범주론은 수학의 다른 분야들에 비해 최근에 나타났지만 수학 전반에 끼친 영향은 아주 지대해서, 집합론과 함께 현대수학의 근간을 이루고 있다고 해도 될 정도이다. 다만 이들 둘은 추구하는 방향이나 철학이 매우 다른데, 집합론은 수학을 단단하게 떠받치는 역할을 한다면 범주론은 수학의 분야들을 관통하는 더 큰 그림을 보는 학문에 가깝다. 때문에 범주론을 공부하기 위해서는 다른 분야들 전반에 대한 얕더라도 넓은 이해가 필요하다. 

## 카테고리의 정의

수학을 공부하다 보면 분명 서로 다른 분야임에도 불구하고 똑같은 일을 반복하는 경우가 흔하다. 예컨대 [집합론](/ko/set_theory)에서 우리는 집합들 간의 함수를 정의하고 이를 분해하거나, 집합의 곱, 합, 몫 등을 정의하고 이들의 성질을 탐구했는데 이는 [대수적 구조](/ko/algebraic_structures)를 다룰 때에도 동일하게 반복했던 일이다. 물론 [위상수학](/ko/topology)이나 [미분다양체](/ko/manifold)를 다룰 때에도 마찬가지였다. 카테고리는 이러한 개념들, 즉 어떠한 수학적인 <em_ko>대상</em_ko>들과 이들 사이의 <em_ko>함수</em_ko> 등을 가장 추상적인 방법으로 일반화한 것이다.

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

위의 정의에서 우리는 의도적으로 $\obj(\mathcal{C})$와 $\Mor\_\mathcal{C}(A,B)$들을 <em_ko>모임</em_ko>이라 불렀는데, 이는 대다수의 경우 이 모임들이 집합이 아니기 때문이다. 일반적으로 카테고리 $\mathcal{C}$의 <em_ko>모든</em_ko> morphism들을 모아둔 것이 집합이 된다면 $\mathcal{C}$를 *작은 카테고리<sub>small category</sub>*라 부르고, $A,B\in\obj(\mathcal{C})$가 고정될 때마다 $\Mor\_\mathcal{C}(A,B)$가 집합을 이룬다면 이를 *국소적으로 작은 카테고리<sub>locally small category</sub>*라 부른다. 

[집합론](/ko/set_theory)의 글들과 마찬가지로, [범주론](/ko/category_theory)의 글들 또한 범주론 자체를 공부하는 내용이 아니라, 다른 분야들을 다룰 때 카테고리의 언어를 사용하려는 것이 주된 목적이므로 이렇게 미묘한 부분들은 건드리지 않고 넘어가기로 한다. 또, 편의상 앞으로는 $f\in\Mor_\mathcal{C}(A,B)$와 같은 표기보다는 $f:X\rightarrow Y$와 같은 표현을 사용한다.

## 카테고리의 예시들

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (대수적 구조들)**</ins> 

- 집합들의 카테고리 $\Set$이 존재한다. $\Set$의 대상들은 집합들이며, 임의의 두 대상 $A,B\in\obj(\Set)$에 대하여 $\Mor_\Set(A,B)=\Fun(A,B)$으로 정의된다. 두 morphism들의 합성은 함수의 합성과 같다. ([\[집합론\] §함수들 사이의 연산, ⁋명제 1](/ko/math/set_theory/operation_of_functions#pp1)) Identity morphism은 정확히 항등함수와 같다.
- Group들의 카테고리 $\Group$이 존재한다. $\Group$의 대상들은 group들이며, 임의의 두 대상 $G,H\in\obj(\Group)$에 대하여 $\Mor_\Group(G,H)$는 $G$에서 $H$로의 group homomorphism들의 모임으로 정의된다. 두 morphism들의 합성과 identity morphism은 위와 마찬가지로 정의된다. ([\[대수적 구조\] §준동형사상, 명제 1](/ko/math/algebraic_structures/group_homomorphisms#pp1))
- Abelian group들의 카테고리 $\Ab$이 존재한다. $\Ab$의 대상들은 abelian group들이며, 임의의 두 대상 $G,H\in\obj(\Ab)$에 대하여 $\Mor_\Ab(G,H)$는 $G$에서 $H$로의 group homomorphism들의 모임이다. 두 morphism들의 합성과 identity morphism은 위와 마찬가지로 정의된다.
- (항등원을 갖는) ring들의 카테고리 $\Ring$이 잘 정의된다. $\Ring$의 대상들은 항등원을 갖는 ring들이며, 두 대상 $R,S\in\obj(\Ring)$에 대하여 $\Mor_\Ring(R,S)$는 $R$에서 $S$로의 *unital* ring homomorphism들의 모임으로 정의된다.
- 카테고리 $\Rng$는 항등원 (**i**dentity)을 가질 수도, 갖지 않을 수도 있는 ring들의 카테고리다. 따라서 두 "rng"들 사이의 morphism은 ring homomorphism들이며, 설령 정의역 $R$과 공역 $S$가 모두 항등원을 갖는다 하더라도 $\Mor_\Rng(R,S)$의 원소들은 항등원을 보존할 필요가 없다.
- 카테고리 $\Field$가 잘 정의된다.
- 고정된 ring $R$에 대하여, $\lmod{R}$은 left $R$-module들의 카테고리이다. 두 대상 $M,N\in\obj(\lmod{R})$에 대하여, $\Mor_\lmod{R}(M,N)$은 $R$-module homomorphism들의 모임이다. 비슷하게 right $R$-module들의 카테고리 $\rmod{R}$ 또한 정의된다.
- 특별히 $R=k$가 field인 경우, 카테고리 $\lmod{k}$은 $k$-벡터공간들의 카테고리 $\Vect{k}$과 같다. *유한차원* $k$-벡터공간들의 카테고리는 $\FVect{k}$으로 적는다.
</div>

서두에서 언급한 것과 같이, 대수적인 구조들 뿐만 아니라 다른 구조들도 카테고리의 언어로 쓸 수 있다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 

- 위상공간들의 카테고리 $\Top$이 존재한다. $\Top$의 대상들은 위상공간들이며, 두 대상 $X,Y\in\obj(\Top)$에 대하여 $\Mor_\Top(X,Y)$는 $X$에서 $Y$로의 연속함수들의 모임이다. ([\[위상수학\] §연속함수, ⁋명제 3](/ko/math/topology/continuous_functions#pp3))
- 카테고리 $\Man$은 (smooth) manifold들의 모임이다. 이들 사이의 morphism들은 smooth map들이다. ([\[미분다양체\] §미분사상, ⁋명제 5](/ko/math/manifold/differentials#pp3))

</div>

앞선 예시들에서는 카테고리의 대상들이 모두 특정한 구조들이 주어져있는 집합이고, morphism들은 이 구조를 보존하는 함수들이었다. 이러한 카테고리들을 *concrete category*라 부른다. 그러나 [정의 1](#df1)의 어떠한 조건도 이를 강제하지는 않는다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 예를 들어, 임의의 ordered set $(S,\leq)$이 주어졌다 하자. 카테고리 $\mathbf{S}$를 다음과 같이 정의한다.

- $\obj(\mathbf{S})=S$이다. 즉, $\mathbf{S}$의 대상들은 $S$의 원소들이다.
- $\Mor\_\mathbf{S}(a,b)$의 경우, 만일 $a\leq b$라면 $\Mor\_\mathbf{S}(a,b)$가 하나의 원소를 갖는 것으로, 그렇지 않다면 $\Mor\_\mathbf{S}(a,b)$가 공집합인 것으로 생각한다. 논의의 편의를 위해 $\Mor\_\mathbf{S}(a,b)$의 (존재한다면) 유일한 원소를 $a\rightarrow b$로 적자.
- 두 모임 $\Mor\_\mathbf{S}(a,b)$와 $\Mor\_\mathbf{S}(b,c)$은 각각 $a\rightarrow b$, $b\rightarrow c$ 하나의 원소만 가지므로, 합성을 정의하기 위해서는 이들 둘의 합성을 정의하면 된다. 이는 $(a\rightarrow b, b\rightarrow c)\mapsto (a\rightarrow c)$로 정의한다.

그럼 $\id\_a$의 존재성은 $\leq$가 reflexive하다는 것으로부터 얻어지며, 위에서 정의한 합성이 잘 정의된다는 것은 $\leq$의 transitivity로부터 얻어진다. 또 $\Mor\_\mathbf{S}(a,a)$의 유일한 원소 $a\rightarrow a$가 실제로 $\id\_a$의 역할을 한다는 것이 자명하다.

</div>

## 동형사상

[예시 2](#ex2)와 [예시 3](#ex3)의 카테고리들의 대상들 간에는 *isomorphism*들이 존재한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Morphism $f:X\rightarrow Y$가 카테고리 $\mathcal{C}$에서의 *isomorphism<sub>동형사상</sub>*이라는 것은 적당한 morphism $g:Y\rightarrow X$가 존재하여 $\id\_X=g\circ f$이고 $\id\_Y=f\circ g$인 것이다.

이 경우, 두 대상 $X,Y$가 *isomophic*하다고 하고 $X\cong Y$로 표기한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 

- [예시 2](#ex2)에서, 집합들의 카테고리 $\mathbf{Set}$에서의 isomorphism은 전단사함수를 의미하고, 그 외 대수적 구조들에서의 isomorphism은 원래 정의했었던 isomorphism들과 같다.
- [예시 3](#ex3)에서, $\mathbf{Top}$의 isomorphism은 homeomorphism이고, $\mathbf{Man}$의 isomorphism은 diffeomorphism이다.
- 마지막으로 [예시 4](#ex4)의 카테고리 $\mathbf{S}$의 유일한 isomorphism은 $\id_a=a\rightarrow a$들 뿐이다. 이는 $\leq$의 antisymmetry로부터 얻어진다.

</div>

## Monomorphism과 epimorphism

한편, [예시 2](#ex2)에서의 isomorphism들은 보편적으로 "전단사인 morphism"들이라 할 수 있다. Concrete category가 아닌 이상 <em_ko>전단사</em_ko>의 개념을 잘 정의할 수 없지만, 다음 정의는 모든 카테고리에서 잘 정의된다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 임의의 카테고리 $\mathcal{C}$의 morphism $f:X\rightarrow Y$가 *monomorphism*이라는 것은 임의의 $Z\in\obj(\mathcal{C})$와 두 morphism $g_1,g_2:Z\rightarrow X$에 대하여 

$$f\circ g_1=f\circ g_2\implies g_1=g_2$$

이 성립하는 것이다. 또, $f:X\rightarrow Y$가 *epimorphism*이라는 것은 임의의 $Z\in\obj(\mathcal{C})$와 두 morphism $h_1,h_2:Y\rightarrow Z$에 대하여

$$h_1\circ f=h_2\circ f\implies h_1=h_2$$

이 성립하는 것이다. 

마지막으로 $f:X\rightarrow Y$가 *bimorphism*이라는 것은 $f$가 monomorphism인 동시에 epimorphism인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 

- 카테고리 $\Set$에서 monomorphism들은 정확히 단사함수들이고, epimorphism들은 정확히 전사함수들이며 따라서 bimorphism들은 정확히 전단사함수들이다. 즉, $\Set$에서는 bimorphism과 isomorphism이 동일한 개념이다.
- 카테고리 $\Ring$에서 monomorphism들은 마찬가지로 정확히 단사인 ring homomorphism들이다. 그러나 epimorphism은 전사인 ring homomorphism을 의미하지 <em_ko>않는다</em_ko>. 가령 $\mathbb{Z}\hookrightarrow\mathbb{Q}$가 epimorphism이라는 것이 바로 localization의 universal property이다. 이는 $\Ring$에서 bimorphism이지만 isomorphism은 아닌 예시가 존재함을 보여준다.

</div>


## 쌍대성

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 카테고리 $\mathcal{C}$의 *opposite category<sub>반대 카테고리</sub>*는 다음과 같이 정의된 카테고리 $\mathcal{C}^\op$를 의미한다.

- $\mathcal{C}^\op$의 대상들은 $\mathcal{C}$의 대상들과 같다.
- $\mathcal{C}^\op$의 두 대상 $A,B$에 대하여, $\Mor\_{\mathcal{C}^\op}(A,B)=\Mor\_{\mathcal{C}}(B,A)$이다.
- $\mathcal{C}^\op$의 두 morphism $f^\op,g^\op$의 합성은 $f^\op\circ g^\op=(g\circ f)^\op$로 주어진다.

</div>

일반적으로 $\mathcal{C}$의 대상들은 점으로, morphism들은 화살표로 표현되므로, opposite category $\mathcal{C}^\op$는 $\mathcal{C}$의 대상들은 그대로 둔 채, 화살표의 방향만 거꾸로 뒤집은 것으로 이해할 수 있다. 이렇게 정의할 경우, 임의의 $A\in\obj(\mathcal{C})$에 해당하는 항등사상 $\id\_A$를 거꾸로 뒤집은 $\id\_A^\op$가 $\mathcal{C}^\op$에서의 $A$의 항등사상 역할을 한다는 것을 쉽게 확인할 수 있다. 

정의로부터, $f$가 $\mathcal{C}$에서 monomorphism이라면 $f^\op$는 $\mathcal{C}^\op$에서 epimorphism이고, $f$가 $\mathcal{C}$에서 epimorphism이라면 $f^\op$는 $\mathcal{C}^\op$에서 monomorphism이다. 

한편, [\[집합론\] §Retraction과 section](/ko/math/set_theory/retraction_and_section)에서 우리는 retraction과 section을 정의했었는데, 이들 또한 서로의 정의에서 <em_ko>화살표를 뒤집어서</em_ko> 얻어지므로 해당 글의 모든 명제들이 전사함수와 단사함수 각각에서 성립했던 것은 duality에 의한 것으로 생각할 수 있다. 

---

**참고문헌**

**[Rie]** E. Riehl. <i>Category Theory in Context</i>. Dover Publications, 2017. [링크](https://emilyriehl.github.io/files/context.pdf)

---