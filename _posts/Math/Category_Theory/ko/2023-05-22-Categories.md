---
title: "카테고리"
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

## 범주의 정의

범주론으로 모든 분야를 완벽하게 설명할 수 있는 것은 아니지만, 기본적으로 어떤 분야가 수학의 한 갈래라면 당연하게 갖고 있는 개념들이 있다. 우리가 다루고자 하는 <em_ko>대상</em_ko>들과, 이 대상들 사이의 <em_ko>사상</em_ko>들이 그러하다.

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

위의 정의에서, $\obj(\mathcal{A})$를 대상들의 <em_ko>집합</em_ko> 대신, <em_ko>모임</em_ko>이라 지칭한 것은 이들의 모임이 실제로 집합이 되지 않을 수도 있기 때문이다. 보통은 이러한 대상들을 *class<sub>클래스</sub>*라 부른다. 모든 집합은 class지만, class들 중에서는 집합이 아닌 것들이 존재한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Category $\mathcal{A}$가 주어졌다 하자.

- $\mathcal{A}$가 *small category<sub>작은 카테고리</sub>*라는 것은 $\mathcal{A}$에 속하는 모든 morphism들의 모임 $\Hom(\mathcal{A})$이 집합인 것이다. 
- $\mathcal{A}$가 *locally small category<sub>국소적으로 작은 카테고리</sub>*라는 것은 임의의 대상 $A_1,A_2\in\mathcal{A}$가 고정될 때마다 $\Hom_\mathcal{A}(A_1,A_2)$가 집합인 것이다.

</div>

정의에 의하여 임의의 small category는 locally small이기도 하다. 또, 임의의 small category $\mathcal{A}$에 대하여 $\obj(\mathcal{A})$는 반드시 집합이다. 이는 임의의 $A\in\obj(\mathcal{A})$에 대하여, $\id_A$는 항상 $\mathcal{A}$의 morphism이 되며, 따라서 $\obj(\mathcal{A})$를 집합 $\Hom(\mathcal{A})$의 부분집합으로 생각할 수 있기 때문이다.

앞으로 별다른 말이 없을 경우, 모든 category는 locally small category인 것으로 생각한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 category $\mathcal{A}$가 주어졌다 하고, $A_1,A_2\in\obj(\mathcal{A})$라 하자. $A_1$과 $A_2$가 *isomorphic<sub>동형</sub>*이라는 것은 $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_2,A_1)$가 존재하여 두 조건

$$f\circ g=\id_{A_2},\qquad g\circ f=\id_{A_1}$$

가 성립하는 것이다. 이 때, $f$와 $g$를 *isomorphism<sub>동형사상</sub>*이라 부르고 이들을 각각의 *inverse<sub>역사상</sub>*라 부른다. 

</div>

위의 정의와 같은 상황에서, 두 조건

$$f\circ g'=\id_{A_2},\qquad g'\circ f=\id_{A_1}$$

을 만족하는 또 다른 $g'\in\Hom_\mathcal{A}(A_2,A_1)$가 존재한다 하자. 그럼

$$g=g\circ\id_{A_2}=g\circ(f\circ g')=(g\circ f)\circ g'=\id_{A_1}\circ g'=g'$$

으로부터 $g=g'$임을 안다. 따라서 임의의 $f\in\Hom_\mathcal{A}(A_1,A_2)$가 주어졌을 때, [정의 3](#def3)의 두 조건을 만족하는 $g\in\Hom_\mathcal{A}(A_2,A_1)$는 존재한다면 유일하고, 따라서 이를 $g=f^{-1}$으로 적을 수 있다.

많은 예시에서 isomorphism은 bijective인 morphism과 같은 말이지만, 항상 그런 것은 아니다. ([\[위상수학\] §연속함수, ⁋예시 5](/ko/math/topology/continuous_functions#ex5)) 뿐만 아니라, 임의의 category의 morphism들이 반드시 함수라는 보장도 없으므로 morphism이 bijection이라는 것은 애초부터 말이 되지 않는다. 대신 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Category $\mathcal{A}$와, morphism $f:A_1\rightarrow A_2$를 생각하자. 

- $f$가 *monomorphism*이라는 것은 임의의 두 morphism $g_1,g_2:A_0\rightarrow A_1$가 $f\circ g_1=f\circ g_2$를 만족한다면 $g_1=g_2$가 성립하는 것이다.
- $f$가 *epimorphism*이라는 것은 임의의 두 morphism $h_1,h_2:A_2\rightarrow A_3$가 $h_1\circ f=h_2\circ f$를 만족한다면 $h_1=h_2$가 성립하는 것이다.
- $f$가 *bimorphism*이라는 것은 $f$가 monomorphism이면서 epimorphism인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 isomorphism은 bimorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f:A_1\rightarrow A_2$가 isomorphism이라 가정하자. 만일 $g_1,g_2:A_0\rightarrow A_1$가 $f\circ g_1=f\circ g_2$를 만족한다면 다음 식

$$g_1=\id_{A_1}\circ g_1=(f^{-1}\circ f)\circ g_1=f^{-1}\circ(f\circ g_1)=f^{-1}\circ(f\circ g_2)=\id_{A_1}\circ g_2=g_2$$

로부터 $f$가 monomorphism임을 안다. 동일한 논증에 의해 $f$는 epimorphism이기도 하고 따라서 $f$는 bimorphism이다.

</details>

그러나 일반적으로 그 역은 성립하지 않는다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Category $\Ring$에서의 morphism $\iota:\mathbb{Z}\hookrightarrow\mathbb{Q}$를 생각하자. ()

- 임의의 ring homomorphism들 $f_1,f_2:R\rightarrow\mathbb{Z}$가 $\iota\circ f_1=\iota\circ f_2$를 만족한다 가정하자. 그럼 임의의 $x\in R$에 대하여, 
    
    $$f_1(x)=(\iota\circ f_1)(x)=(\iota\circ f_2)(x)=f_2(x)$$

    이므로 $f_1=f_2$이다. 즉 $\iota$는 monomorphism이다.
- 임의의 ring homomorphism들 $g_1,g_2:\mathbb{Q}\rightarrow S$가 $g_1\circ\iota=g_2\circ\iota$를 만족한다 가정하자. 이 공통의 함수를 $g=g_1\circ\iota=g_2\circ\iota$라 한다면, $0$이 아닌 임의의 $\mathbb{Z}$의 원소는 항상 $S$에서 invertible하며 따라서 localization의 universal property로부터 $g=\bar{g}\circ\iota$를 만족하는 유일한 $\bar{g}:\mathbb{Q}\rightarrow S$가 존재한다. 이제 유일성으로부터 $\bar{g}=g_1=g_2$이므로, $\iota$는 epimorphism이다.

그러나 $\iota$가 $\Ring$에서의 isomorphism이 아닌 것은 자명하다.

</div>

## $\End(A)$와 $\Aut(A)$

임의의 category $\mathcal{A}$가 주어졌다 하자. 두 morphism $f\in\Hom_\mathcal{A}(A_1,A_2)$, $g\in\Hom_\mathcal{A}(A_3,A_4)$에 대하여, 합성 $g\circ f$가 잘 정의되기 위해서는 반드시 $A_2=A_3$이어야 한다. 즉 category $\mathcal{A}$의 임의의 두 morphism이 항상 합성가능한 것은 아니다.

반면 고정된 $A\in\obj(\mathcal{A})$에 대하여, $\Hom_\mathcal{A}(A,A)$의 원소들은 모두 정의역과 공역이 $A$이므로 이들은 원하는만큼 합성이 가능하다. 즉, $\Hom_\mathcal{A}(A,A)$는 단순히 집합일 뿐만 아니라, 이 위에 특정한 연산 $\circ$가 주어진 대수적인 구조로 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 임의의 category $\mathcal{A}$와 object $A\in\obj(\mathcal{A})$를 고정하자.

- $A$에 대한 *endomorphism monoid<sub>자기준동형사상 모노이드</sub>*는 집합 $\End_\mathcal{A}(A)=\Hom_\mathcal{A}(A,A)$과 합성 $\circ$으로 이루어진 데이터이다.
- $A$에 대한 *automorphism group<sub>자기동형사상 군</sub>*은 $\End_\mathcal{A}(A)$의 원소들 중 isomorphism만을 모아둔 집합 $\Aut_\mathcal{A}(A)$와 합성 $\circ$으로 이루어진 데이터이다.

</div>

문맥상 category $\mathcal{A}$가 명확할 경우, 이들을 각각 $\End(A)$와 $\Aut(A)$로 적기도 한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Category $\mathcal{A}$와 임의의 object $A$에 대하여, $\End(A)$는 monoid이고 $\Aut(A)$는 group이다. ([\[대수적 구조\] §준군, 모노이드, 군, ⁋정의 3](/ko/math/algebraic_structures/group#def3)과 [정의 10](/ko/math/algebraic_structures/group#def10))

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>




---

**참고문헌**

**[Lei]**

---