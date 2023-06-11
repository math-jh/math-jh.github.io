---
title: "카테고리와 함자"
excerpt: "카테고리와 함자의 정의"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/categories_and_functors
header:
    overlay_image: /assets/images/Math/Category_Theory/Categories_and_functors.png
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
- *정의역<sub>domain</sub>* $A\in\obj(\mathcal{A})$에서 *공역<sub>codomain</sub>* $B\in\obj(\mathcal{A})$로의 *morphism<sub>사상</sub>*들의 모임 $\Hom\_\mathcal{A}(A,B)$,
- 두 morphism $f\in\Hom\_\mathcal{A}(A,B)$, $g\in\Hom\_\mathcal{A}(B,C)$의 *합성<sub>composition</sub>* 

  $$\circ:\Hom_\mathcal{A}(A,B)\times\Hom_\mathcal{A}(B,C)\rightarrow\Hom_\mathcal{A}(A,C);\qquad (f,g)\mapsto g\circ f$$

추가적으로, 이들은 다음의 조건을 만족한다.

- Morphism들의 합성은 결합법칙을 만족한다. 즉, $(f\circ g)\circ h=f\circ(g\circ h)$가 성립한다.
- 각각의 $A\in\obj(\mathcal{A})$마다 $\id_A\in\Hom\_\mathcal{A}(A,A)$가 존재하여, 모든 $f\in\Hom\_\mathcal{A}(A,B)$ 그리고 모든 $g\in\Hom\_\mathcal{A}(C,A)$에 대하여
  
  $$f\circ{\id_A}=f,\qquad {\id_A}\circ g=g$$

  이 성립한다.

</div>

위의 정의에서, $\obj(\mathcal{A})$를 대상들의 <em_ko>집합</em_ko> 대신, <em_ko>모임</em_ko>이라 지칭한 것은 이들의 모임이 실제로 집합이 되지 않을 수도 있기 때문이다. 보통은 이러한 대상들을 *class<sub>클래스</sub>*라 부른다. 모든 집합은 class지만, class들 중에서는 집합이 아닌 것들이 존재한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 카테고리 $\mathcal{A}$가 주어졌다 하자.

- $\mathcal{A}$가 *small category<sub>작은 카테고리</sub>*라는 것은 $\mathcal{A}$에 속하는 모든 morphism들의 모임 $\Hom(\mathcal{A})$이 집합인 것이다. 
- $\mathcal{A}$가 *locally small category<sub>국소적으로 작은 카테고리</sub>*라는 것은 임의의 대상 $A,B\in\mathcal{A}$가 고정될 때마다 $\Hom_\mathcal{A}(A,B)$가 집합인 것이다.

</div>

정의에 의하여 임의의 small category는 locally small이기도 하다. 또, 임의의 small category $\mathcal{A}$에 대하여 $\obj(\mathcal{A})$는 반드시 집합이다. 이는 임의의 $A\in\obj(\mathcal{A})$에 대하여, $\id_A$는 항상 $\mathcal{A}$의 morphism이 되며, 따라서 $\obj(\mathcal{A})$를 집합 $\Hom(\mathcal{A})$의 부분집합으로 생각할 수 있기 때문이다.

앞으로 별다른 말이 없을 경우, 모든 카테고리는 locally small category인 것으로 생각한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 카테고리 $\mathcal{A}$가 주어졌다 하고, $A,B\in\obj(\mathcal{A})$라 하자. $A$와 $B$가 *isomorphic<sub>동형</sub>*이라는 것은 $f\in\Hom_\mathcal{A}(A,B)$, $g\in\Hom_\mathcal{A}(B,A)$가 존재하여 두 조건

$$f\circ g=\id_B,\qquad g\circ f=\id_A$$

가 성립하는 것이다. 이 때, $f$와 $g$를 *isomorphism<sub>동형사상</sub>*이라 부르고 이들을 각각의 *inverse<sub>역사상</sub>*라 부른다. 

</div>

위의 정의와 같은 상황에서, 두 조건

$$f\circ g'=\id_B,\qquad g'\circ f=\id_A$$

을 만족하는 또 다른 $g'\in\Hom_\mathcal{A}(B,A)$가 존재한다 하자. 그럼

$$g=g\circ\id_B=g\circ(f\circ g')=(g\circ f)\circ g'=\id_A\circ g'=g'$$

으로부터 $g=g'$임을 안다. 따라서 임의의 $f\in\Hom_\mathcal{A}(A,B)$가 주어졌을 때, [정의 3](#def3)의 두 조건을 만족하는 $g\in\Hom_\mathcal{A}(B,A)$는 존재한다면 유일하고, 따라서 이를 $g=f^{-1}$으로 적을 수 있다.

## $\End(A)$와 $\Aut(A)$

임의의 카테고리 $\mathcal{A}$가 주어졌다 하자. 두 morphism $f\in\Hom_\mathcal{A}(A,B)$, $g\in\Hom_\mathcal{A}(C,D)$에 대하여, 합성 $g\circ f$가 잘 정의되기 위해서는 반드시 $B=C$여야 한다. 즉 카테고리 $\mathcal{A}$의 임의의 두 morphism이 항상 합성가능한 것은 아니다.

반면 고정된 $A\in\obj(\mathcal{A})$에 대하여, $\Hom_\mathcal{A}(A,A)$의 원소들은 모두 정의역과 공역이 $A$이므로 이들은 원하는만큼 합성이 가능하다. 즉, $\Hom_\mathcal{A}(A,A)$는 단순히 집합일 뿐만 아니라, 이 위에 특정한 연산 $\circ$가 주어진 대수적인 구조로 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 임의의 카테고리 $\mathcal{A}$와 object $A\in\obj(\mathcal{A})$를 고정하자.

- $A$에 대한 *endomorphism monoid<sub>자기준동형사상 모노이드</sub>*는 집합 $\End_\mathcal{A}(A)=\Hom_\mathcal{A}(A,A)$과 합성 $\circ$으로 이루어진 데이터이다.
- $A$에 대한 *automorphism group<sub>자기동형사상 군</sub>*은 $\End_\mathcal{A}(A)$의 원소들 중 isomorphism만을 모아둔 집합 $\Aut_\mathcal{A}(A)$와 합성 $\circ$으로 이루어진 데이터이다.

</div>

문맥상 카테고리 $\mathcal{A}$가 명확할 경우, 이들을 각각 $\End(A)$와 $\Aut(A)$로 적기도 한다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 카테고리 $\mathcal{A}$와 임의의 object $A$에 대하여, $\End(A)$는 monoid이고 $\Aut(A)$는 group이다. ([\[대수적 구조\], §준군, 모노이드, 군, ⁋정의 3](/ko/math/algebraic_structures/group#def3)과 [⁋정의 10](/ko/math/algebraic_structures/group#def10))

</div>

## 범주의 예시들

다음 두 예시는 카테고리들이 주어졌을 때, 그로부터 새로운 카테고리를 만드는 법을 보여준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 카테고리 $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$의 *opposite category<sub>반대 카테고리</sub>* $\mathcal{A}^\op$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}^\op)=\obj(\mathcal{A})$이다.
- 임의의 $A,B\in \obj(\mathcal{A}^\op)=\obj(\mathcal{A})$에 대하여, $\Hom_{\mathcal{A}^\op}(A,B)=\Hom_{\mathcal{A}}(B,A)$가 성립한다.
- 임의의 $A\in\obj(\mathcal{A})$에 대하여, $\mathcal{A}^\op$에서의 identity $\id_A$는 $\mathcal{A}$에서의 identity와 동일한 것으로 주어진다.
- 임의의 $f\in\Hom_{\mathcal{A}^\op}(A,B),g\in\Hom_{\mathcal{A}^\op}(B,C)$에 대하여, 이들의 합성 $g\circ^\op f$는 $f,g$를 $\mathcal{A}$의 morphism들로 본 후, 이를 $\mathcal{A}$에서 합성한 것으로 정의된다.   
  즉, $f\in \Hom_\mathcal{A}(B,A),g\in\Hom_\mathcal{A}(C,B)$에 대하여, $f$와 $g$의 $\mathcal{A}^\op$에서의 합성 $g\circ^\op f$는 
    
    $$g\circ^\op f= f\circ g\in\Hom_{\mathcal{A}}(C,A)=\Hom_{\mathcal{A}^\op}(A,C)$$

  으로 정의된다. 

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 두 카테고리 $\mathcal{A},\mathcal{B}$가 주어졌다 하자. 이들의 *product category<sub>곱 카테고리</sub>* $\mathcal{A}\times \mathcal{B}$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}\times \mathcal{B})$의 대상들은 쌍 $(A,B)$의 꼴이다.
- 임의의 $(A_1,B_1),(A_2,B_2)\in\obj(\mathcal{A}\times \mathcal{B})$에 대하여, $\Hom_{\mathcal{A}\times \mathcal{B}}((A_1,B_1),(A_2,B_2))$는 $f\in\Hom_\mathcal{A}(A_1,A_2),g\in\Hom_\mathcal{B}(B_1,B_2)$에 대해 $(f,g)$의 꼴이다. 
- 임의의 $A\times B\in \mathcal{A}\times \mathcal{B}$에 대하여, $A\times B$에서의 identity는 $(\id_A,\id_B)$로 주어진다.
- 임의의 $(f_1,g_1):(A_1,B_1)\rightarrow(A_2,B_2)$, $(f_2,g_2):(A_2,B_2)\rightarrow(A_3,B_3)$에 대해, 이들의 합성은 $(f_2\circ f_1,g_2\circ g_1)\in\Hom((A_1,B_1),(A_3,B_3))$으로 주어진다. 

</div>

다음 예시는 실제로 범주론이 대부분의 곳에서 사용된다는 것을 보여준다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 다음은 모두 카테고리의 예시들이다.

- 집합들과 함수들의 카테고리 $\Set$ ([\[집합론\] §함수들 사이의 연산, ⁋따름정리 2](ko/math/set_theory/operation_of_functions#cor2))
- Monoid들과 monoid homomorphism들의 카테고리 $\Grp$ ([\[대수적 구조\] §준군, 모노이드, 군, ⁋명제 5](/ko/math/algebraic_structures/group#prop5))
- Group들과 group homomorphism들의 카테고리 $\Grp$ ([\[대수적 구조\] §준군, 모노이드, 군, ⁋명제 12](/ko/math/algebraic_structures/group#prop12))
- Abelian group들과 group homomorphism들의 카테고리 $\Ab$ ([\[대수적 구조\] §준군, 모노이드, 군, ⁋명제 12](/ko/math/algebraic_structures/group#prop12))
- Ring들과 ring homomorphism들의 카테고리 $\Ring$ ()
- Field들과 field extension들의 카테고리 $\Field$ ()
- Left, right $G$-set들과 $G$-set homomorphism들의 카테고리 $\lset{G},\rset{G}$ ()
- Left, right $R$-module들과 $R$-module homomorphism들의 카테고리 $\lmod{R},\rmod{R}$ ()
- $k$-벡터공간들과 linear map들의 카테고리 $\Vect_k$
- 유한차원 $k$-벡터공간들과 linear map들의 카테고리 $\FVect_k$
- 위상공간들과 연속함수들의 카테고리 $\Top$
- Pointed topological space들과 pointed continuous map들의 카테고리 $\Top_\ast$
- 위상공간들과 homotopy class들의 카테고리 $\hTop$
- $C^k$-manifold들과 $C^k$-map들의 카테고리 $\Man^k$

</div>

## 함자의 정의

수학에서 다루는 모든 대상들과 이들 사이의 morphism들의 모임을 카테고리로 보겠다는 범주론의 철학을 받아들이기로 한다면, 자연스럽게 우리가 정의한 수학적인 대상, 즉 카테고리들을 대상으로 갖는 카테고리를 생각할 수도 있다. 이를 위해서는 우선 카테고리들 사이의 morphism이 무엇인지부터 정의해야 한다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 두 카테고리 $\mathcal{A},\mathcal{B}$ 사이의 *functor<sub>함자</sub>* $F:\mathcal{A}\rightarrow\mathcal{B}$는 다음과 같은 정보로 구성된다.

- 각각의 $A\in\obj(\mathcal{A})$마다 대응되는 object $F(A)\in\obj(\mathcal{B})$,
- 각각의 $f\in\Mor_\mathcal{A}(A,A')$마다 대응되는 morphism $F(f)\in\Mor_\mathcal{B}(F(A),F(A'))$

이들은 다음 조건들을 만족한다.

- 두 morphism의 합성을 $F$로 보낸 것은 각각의 morphism을 $F$로 보낸 후 합성한 것과 같다. 즉 $F(g\circ f)=F(g)\circ F(f)$가 성립한다.
- 임의의 object $A\in\obj(\mathcal{A})$에 대하여, $F(\id_A)=\id_{F(A)}$가 성립한다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 임의의 카테고리 $\mathcal{A}$에 대하여, $\mathcal{A}$에서 자기 자신으로의 *identity functor<sub>항등함자</sub>* $\id_\mathcal{A}:\mathcal{A}\rightarrow \mathcal{A}$는 

- 임의의 $A\in\mathcal{A}$에 대하여, $\id_\mathcal{A}(A)=A$,
- 임의의 $f\in\Hom_\mathcal{A}(A,A')$에 대하여, $\id_\mathcal{A}(f)=f$

으로 주어지는 functor이다.

</div>

어렵지 않게 functor들의 합성이 functor인 것을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="lem11">**보조정리 11**</ins> 임의의 카테고리들 $\mathcal{A},\mathcal{B},\mathcal{C}$와 두 functor $F:\mathcal{A}\rightarrow \mathcal{B}, G:\mathcal{B}\rightarrow \mathcal{C}$에 대하여, $G\circ F:\mathcal{A} \rightarrow \mathcal{C}$를

- 임의의 $A\in \mathcal{A}$에 대하여, $(G\circ F)(A)=G(F(A))$,
- 임의의 $f\in\Hom_\mathcal{A}(A,A')$에 대하여, $(G\circ F)(f)=G(F(f))$

으로 정의하면 $G\circ F$는 functor가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Functor가 만족해야 하는 두 조건만 보이면 충분하며, 이는

$$(G\circ F)(g\circ f)=G(F(g\circ f))=G(F(g)\circ F(f))=G(F(g))\circ G(F(f))=(G\circ F)(g)\circ(G\circ F)(f)$$

그리고

$$(G\circ F)(\id_A)=G(F(\id_A))=G(\id_{F(A)})=\id_{G(F(A))}=\id_{(G\circ F)(A)}$$

으로부터 자명하다.

</details>

이를 통해 카테고리들의 카테고리를 정의할 수 있다. 다만 이전에 언급했던 러셀의 역설과 관련된 문제를 피하기 위해 우리는 보편적으로 모든 카테고리들의 카테고리 대신, 모든 small category들의 카테고리를 생각한다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 카테고리 $\Cat$는 다음의 데이터로 이루어진다.

- $\Cat$의 대상들은 small category들이다.
- 임의의 $\mathcal{A},\mathcal{B}\in\obj(\Cat)$에 대하여, $\Hom_\Cat(\mathcal{A},\mathcal{B})$는 $\mathcal{A}$에서 $\mathcal{B}$로의 functor들의 모임이다.

</div>

이들 데이터가 실제로 카테고리가 된다는 것이 정확히 [예시 10](#ex10)과 [보조정리 11](#lem11)의 내용이다. 마지막으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Functor $F:\mathcal{A}\rightarrow \mathcal{B}$가 *faithful<sub>충실</sub>*하다는 것은 임의의 $A,A'\in\obj(\mathcal{A})$에 대하여, 대응

$$\Hom_\mathcal{A}(A,A')\rightarrow\Hom_{\mathcal{B}}(F(A),F(A'));\qquad f\mapsto F(f)$$

이 injective인 것이다. 만일 이 대응이 surjective라면 $F$가 *full<sub>충만</sub>*이라 한다.

</div>

마지막으로 functor의 예시들 또한 존재한다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> 

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> 

</div>

---

**참고문헌**

**[Lei]**

---

[^1]: 별 말이 없다면 모든 ring은 $1$을 갖는 unital ring인 것으로 가정한다. $1$을 갖지 않을 수도 있는 ring들의 카테고리 $\Rng$가 존재하지만, 잘 쓸 일은 없다.