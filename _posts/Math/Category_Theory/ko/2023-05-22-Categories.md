---
title: "범주"
excerpt: "카테고리의 정의와 기본개념들"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2023-05-22
last_modified_at: 2023-05-28
weight: 1

---

기본적으로 어떤 분야가 수학의 한 갈래라면 당연하게 갖고 있는 개념들이 있다. 우리가 다루고자 하는 <em_ko>대상</em_ko>들과, 이 대상들 사이의 <em_ko>사상</em_ko>들이 그러하다. 범주론은 이러한 구조를 추상화하여 살펴보는 학문이므로, 각 분야의 특정한 정리들이 범주론에서의 예시가 될 수 있다. 그렇다고 해서 범주론을 공부하기 위해 이 분야들을 모두 공부해야 한다는 뜻은 아니며, 우리는 최대한 건조하게 범주론을 공부하고 대부분의 예시는 해당하는 분야를 공부할 때 따로 공부하는 것을 목표로 한다. 

## 범주의 정의와 예시

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *Category<sub>범주</sub>* $\mathcal{A}$는 다음과 같은 데이터로 이루어진다.

- *대상<sub>object</sub>*들의 모임 $\obj(\mathcal{A})$,
- *정의역<sub>domain</sub>* $A_1\in\obj(\mathcal{A})$에서 *공역<sub>codomain</sub>* $A_2\in\obj(\mathcal{A})$로의 *morphism<sub>사상</sub>*들의 모임 $\Hom\_\mathcal{A}(A_1,A_2)$,
- 두 morphism $f\in\Hom\_\mathcal{A}(A_1,A_2)$, $g\in\Hom\_\mathcal{A}(A_2,A_3)$의 *합성<sub>composition</sub>* 

  $$\circ:\Hom_\mathcal{A}(A_1,A_2)\times\Hom_\mathcal{A}(A_2,A_3)\rightarrow\Hom_\mathcal{A}(A_1,A_3);\qquad (f,g)\mapsto g\circ f$$

추가적으로, 이들은 다음의 조건을 만족한다.

- Morphism들의 합성은 결합법칙을 만족한다. 즉, $(f\circ g)\circ h=f\circ(g\circ h)$가 성립한다.
- 각각의 $A\in\obj(\mathcal{A})$마다 $\id_A\in\Hom\_\mathcal{A}(A,A)$가 존재하여, 모든 $f\in\Hom\_\mathcal{A}(A,A_1)$ 그리고 모든 $g\in\Hom\_\mathcal{A}(A_2,A)$에 대하여
  
  $$f\circ{\id_A}=f,\qquad {\id_A}\circ g=g$$

  이 성립한다.

</div>

지금까지 우리가 알고 있던 많은 것들이 이 언어로 쓰여질 수 있다. 가령 집합들의 category $\Set$은 다음과 같은 데이터로 이루어진다.

- $\Set$의 대상들은 집합들이다.
- 두 대상 $A_1,A_2\in\obj(\mathcal{A})$에 대하여, $A_1$에서 $A_2$로의 morphism은 집합 $A_1$에서 $A_2$로의 함수이다. ([\[집합론\] §함수, ⁋정의 1](/ko/math/set_theory/functions#def1))
- 두 morphism의 합성은 함수의 합성으로 정의한다. ([\[집합론\] §함수들 사이의 연산, ⁋명제 1](/ko/math/set_theory/operation_of_functions#prop1)) 이 합성이 결합법칙을 만족하는 것은 [\[집합론\] §이항관계들 사이의 연산, ⁋명제 5](/ko/math/set_theory/operation_of_binary_relations#prop5)에서 살펴보았다.
- 임의의 대상 $A\in\obj(\mathcal{A})$에 대하여, $\id_A\in\Hom_\Set(A,A)$는 항등함수 $\id_A$이다. ([\[집합론\] §함수, ⁋정의 2](/ko/math/set_theory/functions#def2)) 항등함수가 위의 [정의 1](#def1)의 두 조건을 만족하는 것은 [\[집합론\] §이항관계들 사이의 연산, ⁋정의 9](/ko/math/set_theory/operation_of_binary_relations#def9) 이후에 살펴보았다.

비슷한 방식으로 다음이 모두 category의 예시가 되는 것을 볼 수 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (Concrete categories)**</ins> 다음은 모두 category의 예시들이다.

- 집합들과 함수들의 category $\Set$
- Monoid들과 monoid homomorphism들의 category $\Mon$
- Group들과 group homomorphism들의 category $\Grp$
- Abelian group들과 group homomorphism들의 category $\Ab$
- Ring들과 ring homomorphism들의 category $\Ring$
- Field들과 field extension들의 category $\Field$
- Left, right $G$-set들과 $G$-set homomorphism들의 category $\lset{G},\rset{G}$
- Left, right $R$-module들과 $R$-module homomorphism들의 category $\lMod{R},\rMod{R}$
- $k$-벡터공간들과 linear map들의 category $\Vect_k$
- 유한차원 $k$-벡터공간들과 linear map들의 category $\FVect_k$
- 위상공간들과 연속함수들의 category $\Top$
- $C^k$-manifold들과 $C^k$-map들의 category $\Man^k$
- $R$-module들의 chain complex와 chain map들의 category $\Ch(R)$
- Pointed set들과 pointed function들의 category $\Set_\ast$
- Pointed topological space들과 pointed continuous map들의 category $\Top_\ast$

여기서 pointed set은 집합 $S$와, $S$의 원소 $x$가 고정된 쌍 $(S,x)$를 뜻하며, $(S,x)$에서 $(S',x')$로의 pointed function은 $f:S \rightarrow S'$ 가운데 $f(x)=x'$를 만족하는 것이다. 이와 비슷하게 pointed topological space와 pointed continuous map을 정의할 수 있다. 

</div>

위의 예시에서의 모든 category의 대상들은 집합 위에 추가적인 구조를 부여한 것이다. 이러한 꼴의 category를 *concrete category*라 부른다. Category들 중에서는 concrete category가 아닌 것들도 많이 존재한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 임의의 preordered set $(S,\preceq)$를 다음과 같은 과정을 통해 category로 생각할 수 있다. ([\[집합론\] §순서관계의 정의, ⁋정의 7](/ko/math/set_theory/order_relations#def7)) 

- $\obj(S)=S$이다.
- 임의의 $x,y\in S$에 대하여, 만일 $x\preceq y$라면 유일한 morphism $x \rightarrow y$가 존재하고, 그렇지 않다면 $\Hom_S(x,y)$는 공집합이다.

두 morphism $x \rightarrow y$와 $y \rightarrow z$의 합성은 morphism $x \rightarrow z$로 주어진다. 이 때 morphism $x \rightarrow z$가 존재한다는 것은 $\preceq$의 transitivity로부터 나온다. 그럼

$$((x \rightarrow y) \rightarrow z)\rightarrow w=x \rightarrow y \rightarrow z \rightarrow y=x \rightarrow (y \rightarrow (z \rightarrow w))$$

으로부터 결합법칙이 나온다. 또, $\preceq$의 reflexivity에 의하여 임의의 $x\in S$에 대해 $\Hom_\mathcal{S}(x,x)$는 유일한 morphism $x \rightarrow x$를 가지며 이것이 $\id_x$의 역할을 하는 것을 확인할 수 있다.

</div>

앞선 정의에서 $\obj(\mathcal{A})$를 대상들의 <em_ko>집합</em_ko> 대신, <em_ko>모임</em_ko>이라 지칭한 것은 이들의 모임이 실제로 집합이 되지 않을 수도 있기 때문이다. 보통은 이러한 대상들을 *class<sub>클래스</sub>*라 부른다. 모든 집합은 class지만, class들 중에서는 집합이 아닌 것들이 존재한다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Category $\mathcal{A}$가 주어졌다 하자.

- $\mathcal{A}$가 *small category<sub>작은 범주</sub>*라는 것은 $\mathcal{A}$에 속하는 모든 morphism들의 모임 $\Hom(\mathcal{A})$이 집합인 것이다. 
- $\mathcal{A}$가 *locally small category<sub>국소적으로 작은 범주</sub>*라는 것은 임의의 대상 $A_1,A_2\in\mathcal{A}$가 고정될 때마다 $\Hom_\mathcal{A}(A_1,A_2)$가 집합인 것이다.

</div>

정의에 의하여 임의의 small category는 locally small이기도 하다. 또, 임의의 small category $\mathcal{A}$에 대하여 $\obj(\mathcal{A})$는 반드시 집합이다. 이는 임의의 $A\in\obj(\mathcal{A})$에 대하여, $\id_A$는 항상 $\mathcal{A}$의 morphism이 되며, 따라서 $\obj(\mathcal{A})$를 집합 $\Hom(\mathcal{A})$의 부분집합으로 생각할 수 있기 때문이다.

예시들을 소개할 때 우리는 이러한 부분을 신경쓰지 않았으며, 앞으로도 그럴 것이다. 다만 안전을 위해 앞으로 나오는 category는 모두 locally small인 것으로 가정한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Category $\mathcal{C}$에 대하여, $\mathcal{C}$의 *subcategory<sub>부분범주</sub>*라는 것은 $\mathcal{C}$의 대상들과 morphism들의 subcollection으로 이루어진 데이터가 그 자체로 category가 되는 것이다.

</div>

## 동형사상

일반적으로 우리가 수학적인 대상들을 배우고 나면, 이들 대상을 언제 같은 것으로 볼 수 있는지를 신경쓴다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 임의의 category $\mathcal{A}$가 주어졌다 하고, $A_1,A_2\in\obj(\mathcal{A})$라 하자. $A_1$과 $A_2$가 *isomorphic<sub>동형</sub>*이라는 것은 $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_2,A_1)$가 존재하여 두 조건

$$f\circ g=\id_{A_2},\qquad g\circ f=\id_{A_1}$$

가 성립하는 것이다. 이 때, $f$와 $g$를 *isomorphism<sub>동형사상</sub>*이라 부르고 이들을 각각의 *inverse<sub>역사상</sub>*라 부른다. 

</div>

위의 정의와 같은 상황에서, 두 조건

$$f\circ g'=\id_{A_2},\qquad g'\circ f=\id_{A_1}$$

을 만족하는 또 다른 $g'\in\Hom_\mathcal{A}(A_2,A_1)$가 존재한다 하자. 그럼

$$g=g\circ\id_{A_2}=g\circ(f\circ g')=(g\circ f)\circ g'=\id_{A_1}\circ g'=g'$$

으로부터 $g=g'$임을 안다. 따라서 임의의 $f\in\Hom_\mathcal{A}(A_1,A_2)$가 주어졌을 때, [정의 8](#def8)의 두 조건을 만족하는 $g\in\Hom_\mathcal{A}(A_2,A_1)$는 존재한다면 유일하고, 따라서 이를 $g=f^{-1}$으로 적을 수 있다.

많은 예시에서 isomorphism은 bijective인 morphism과 같은 말이지만, 항상 그런 것은 아니다. ([\[위상수학\] §연속함수, ⁋예시 5](/ko/math/topology/continuous_functions#ex5)) 애초에 임의의 category의 morphism들이 반드시 함수라는 보장도 없으므로 morphism이 bijection이라는 것은 애초부터 말이 되지 않는다. 대신 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Category $\mathcal{A}$와, morphism $f:A_1\rightarrow A_2$를 생각하자. 

- $f$가 *monomorphism<sub>단사사상</sub>*이라는 것은 임의의 두 morphism $g_1,g_2:A_0\rightarrow A_1$가 $f\circ g_1=f\circ g_2$를 만족한다면 $g_1=g_2$가 성립하는 것이다.
- $f$가 *epimorphism<sub>전사사상</sub>*이라는 것은 임의의 두 morphism $h_1,h_2:A_2\rightarrow A_3$가 $h_1\circ f=h_2\circ f$를 만족한다면 $h_1=h_2$가 성립하는 것이다.
- $f$가 *bimorphism<sub>전단사사상</sub>*이라는 것은 $f$가 monomorphism이면서 epimorphism인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 임의의 isomorphism은 bimorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f:A_1\rightarrow A_2$가 isomorphism이라 가정하자. 만일 $g_1,g_2:A_0\rightarrow A_1$가 $f\circ g_1=f\circ g_2$를 만족한다면 다음 식

$$g_1=\id_{A_1}\circ g_1=(f^{-1}\circ f)\circ g_1=f^{-1}\circ(f\circ g_1)=f^{-1}\circ(f\circ g_2)=\id_{A_1}\circ g_2=g_2$$

로부터 $f$가 monomorphism임을 안다. 동일한 논증에 의해 $f$는 epimorphism이기도 하고 따라서 $f$는 bimorphism이다.

</details>

## $\End(A)$와 $\Aut(A)$

임의의 category $\mathcal{A}$가 주어졌다 하자. 두 morphism $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_3,A_4)$에 대하여, 합성 $g\circ f$가 잘 정의되기 위해서는 반드시 $A_2=A_3$이어야 한다. 즉 category $\mathcal{A}$의 임의의 두 morphism이 항상 합성가능한 것은 아니다.

반면 고정된 $A\in\obj(\mathcal{A})$에 대하여, $\Hom_\mathcal{A}(A,A)$의 원소들은 모두 정의역과 공역이 $A$이므로 이들은 원하는만큼 합성이 가능하다. 이러한 원소들을 *endomorphism*이라 부르고, 특별히 isomorphism인 endomorphism을 *automorphism*이라 부른다. 앞서 설명한 것과 같이 $\Hom_\mathcal{A}(A,A)$는 단순히 집합일 뿐만 아니라, 이 위에 특정한 연산 $\circ$가 주어진 대수적인 구조로 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 임의의 category $\mathcal{A}$와 object $A\in\obj(\mathcal{A})$를 고정하자.

- $A$에 대한 *endomorphism monoid<sub>자기준동형사상 모노이드</sub>*는 집합 $\End_\mathcal{A}(A)=\Hom_\mathcal{A}(A,A)$과 합성 $\circ$으로 이루어진 데이터이다.
- $A$에 대한 *automorphism group<sub>자기동형사상 군</sub>*은 $\End_\mathcal{A}(A)$의 원소들 중 isomorphism만을 모아둔 집합 $\Aut_\mathcal{A}(A)$와 합성 $\circ$으로 이루어진 데이터이다.

</div>

어렵지 않게 $\End(A)$와 $\Aut(A)$가 대수적으로 정의된 monoid와 group의 조건을 만족하는 것을 알 수 있다. ([\[대수적 구조\] §반군, 모노이드, 군, ⁋정의 3](/ko/math/algebraic_structures/groups#def3)과 [⁋정의 11](/ko/math/algebraic_structures/groups#def11)) 범주론에서는 monoid와 group을 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 대상이 하나 뿐인 category를 *monoid*라 부른다. 모든 morphism이 isomorphism인 monoid를 *group*이라 부른다. 

</div>

더 일반적으로 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 모든 morphism이 isomorphism인 category를 *groupoid<sub>준군</sub>*라 부른다. 

</div>

이는 그저 group의 모든 성질들이 성립하지만, group operation이 모든 원소들에 대해 정의되는 대신 특정한 원소들의 쌍에 대해서만 정의되어도 충분하다는 뜻이다. 

## 카테고리의 예시들

이제 이미 존재하는 category로부터 새로운 category들을 만드는 방법을 살펴본다. 


<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> 두 category $\mathcal{A},\mathcal{B}$가 주어졌다 하자. 이들의 *product category<sub>곱 카테고리</sub>* $\mathcal{A}\times \mathcal{B}$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}\times \mathcal{B})$의 대상들은 쌍 $(A,B)$의 꼴이다.
- 임의의 $(A_1,B_1),(A_2,B_2)\in\obj(\mathcal{A}\times \mathcal{B})$에 대하여, $\Hom_{\mathcal{A}\times \mathcal{B}}((A_1,B_1),(A_2,B_2))$는 $f\in\Hom_\mathcal{A}(A_1,A_2),g\in\Hom_\mathcal{B}(B_1,B_2)$에 대해 $(f,g)$의 꼴이다. 
- 임의의 $A\times B\in \mathcal{A}\times \mathcal{B}$에 대하여, $A\times B$에서의 identity는 $(\id_A,\id_B)$로 주어진다.
- 임의의 $(f_1,g_1):(A_1,B_1)\rightarrow(A_2,B_2)$, $(f_2,g_2):(A_2,B_2)\rightarrow(A_3,B_3)$에 대해, 이들의 합성은 $(f_2\circ f_1,g_2\circ g_1)\in\Hom((A_1,B_1),(A_3,B_3))$으로 주어진다. 

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> Category $\mathcal{A}$가 주어졌다 하고, $A\in\obj(\mathcal{A})$를 고정하자. 

- $\mathcal{A}$의 *slice category over $A$<sub>$A$ 위에서의 조각 범주</sub>* $A_{/\mathcal{A}}$는 다음과 같은 데이터로 주어진다.
  - $\mathcal{A}_{/A}$의 object들은 $\mathcal{A}$의 morphism들 $f:A_1\rightarrow A$이다.
  - 임의의 $(A\_1\overset{f\_1}{\longrightarrow}A)\in\obj(\mathcal{A}\_{/A})$와 $(A\_2\overset{f\_2}{\longrightarrow}A)\in\obj(\mathcal{A}\_{/A})$에 대하여, $f_1$에서 $f_2$로의 morphism은 $f_1=g\circ f_2$가 성립하도록 하는 $g:A_1\rightarrow A_2$이다.
- $\mathcal{A}$의 *slice category under $A$<sub>$A$ 위에서의 쌍대 조각 범주</sub>* ${}_{A/}\mathcal{A}$는 다음과 같은 데이터로 주어진다.
  - ${}_{A/}\mathcal{A}$의 object들은 $\mathcal{A}$의 morphism들 $f:A\rightarrow A_1$이다.
  - 임의의 $(A\overset{f\_1}{\longrightarrow}A\_1)\in\obj({}\_{A/}\mathcal{A})$와 $(A\overset{f\_2}{\longrightarrow}A\_2)\in\obj({}\_{A/}\mathcal{A})$에 대하여, $f_1$에서 $f_2$로의 morphism은 $f_2=g\circ f_1$가 성립하도록 하는 $g:A_1\rightarrow A_2$이다.

</div>

---

**참고문헌**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---