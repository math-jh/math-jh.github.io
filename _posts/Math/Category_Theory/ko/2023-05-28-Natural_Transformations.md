---
title: "자연변환"
description: "함자 사이의 사상인 자연변환을 정의하고, 이를 바탕으로 함자 카테고리와 카테고리의 동등 개념을 소개한다."
excerpt: "Natural transformation과 category들 사이의 equivalence"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/natural_transformations
sidebar: 
    nav: "category_theory-ko"

date: 2023-05-28
weight: 3
published: false
revising: true
drift_needed: true

---

## 자연변환의 정의

우리는 앞서 category들의 category가 존재한다는 것을 보았다. 역시 모든 것이 category라는 믿음을 가지면, 두 category $\mathcal{A},\mathcal{B}$가 주어졌을 때 $\mathcal{A}$에서 $\mathcal{B}$로의 functor들의 category $\Fun(\mathcal{A},\mathcal{B})$가 존재한다는 사실도 어느정도 믿을 수 있다. 우리가 대답해야 할 질문은, 그럼 두 functor $F,G:\mathcal{A}\rightarrow \mathcal{B}$가 주어졌을 때 $F$에서 $G$로의 morphism은 무엇인지이고, 그것이 바로 이번 글에서 정의할 natural transformation이다.

::: 정의 1
두 category $\mathcal{A},\mathcal{B}$가 주어졌다 하고, $\mathcal{A}$에서 $\mathcal{B}$로의 두 functor $F,G$가 주어졌다 하자. 만일 $\obj(\mathcal{A})$를 index set으로 갖는 morphism들의 family 

$$\bigl(\alpha_A:F(A)\rightarrow G(A)\bigr)_{A\in\obj(\mathcal{A})}$$

이 각각의 $A_1,A_2\in\obj(\mathcal{A})$와 임의의 $f\in\Hom_\mathcal{A}(A_1,A_2)$마다 다음의 diagram

{% diagram Math/Category_Theory/Natural_Transformations-1.svg width="10.28em" alt="natural_transformation" %}

을 commute하도록 한다면, $\alpha=(\alpha_A)_{A\in\obj(\mathcal{A})}$를 *natural transformation<sub>자연변환</sub>*이라 부르고 이를 $\alpha:F\Rightarrow G$와 같이 표기한다.

만일 각각의 $\alpha_A$들이 모두 isomorphism이라면 이를 *natural isomorphism<sub>자연동형변환</sub>*이라 부르고, 두 functor $F,G$가 *naturally equivalent<sub>자연변환에 대해 동등</sub>*하다고 한다. 이를 $F\simeq G$로 표기한다.
:::

이를 바탕으로 category $\mathcal{A}$로부터 $\mathcal{B}$로의 *functor category<sub>함자 카테고리</sub>* $\Fun(\mathcal{A},\mathcal{B})$를 정의할 수 있다. 이는 $\mathcal{A}$에서 $\mathcal{B}$로의 functor들로 이루어진 category로, morphism들은 functor들 사이의 natural transformation이다. 합성은 성분별로 $(\beta\circ\alpha)_A=\beta_A\circ\alpha_A$와 같이 주어지고, functor $F$의 identity morphism은 $(\id_F)_A=\id_{F(A)}$로 주어진다. 이 category에서의 isomorphism은 natural isomorphism으로 주어진다.

## 동등한 카테고리들

Category 사이에서 자주 사용하는 <em-ko>동등하다</em-ko>는 개념은 $\Cat$에서의 isomorphism으로 주어지지 않는다. ([§함자, ⁋정의 9](/ko/math/category_theory/functors#def9)) 이는 category들 사이의 isomorphism은 너무 강한 조건이어서, 충분히 비슷해보이는 두 category도 다른 것으로 취급되기 때문이다. 

::: 정의 2
Category $\mathcal{A}$에서 $\mathcal{B}$로의 functor $F$가 *equivalence of categories<sub>동등함자</sub>*라는 것은 적당한 functor $G:\mathcal{B}\rightarrow \mathcal{A}$가 존재하여 $\id_\mathcal{A}\simeq G\circ F$이고 $\id_\mathcal{B}\simeq F\circ G$인 것이다. 만일 $\mathcal{A}$에서 $\mathcal{B}$로의 equivalence가 존재한다면 이들 두 category가 *equivalent<sub>동등</sub>*하다고 하고 $\mathcal{A}\simeq\mathcal{B}$으로 표기한다.
:::

이렇게 정의한 category들 사이의 equivalence라는 개념이 어떤 의미에서 충분히 좋은 <em-ko>같다</em-ko>는 개념을 주는지 살펴보자. 이를 위해서는 우선 다음을 정의해야 한다.

::: 정의 3
Category $\mathcal{A}$가 *skeletal category<sub>뼈대 카테고리</sub>*라는 것은 임의의 $A\in\obj(\mathcal{A})$에 대하여, $A$와 isomorphic한 $\mathcal{A}$의 object가 자기 자신뿐인 것이다.
:::

$\mathcal{A}$가 small category라 하자. 그럼 집합 $\obj(\mathcal{A})$에서 서로 isomorphic한 대상들을 같은 것으로 본 후, 서로 다른 것들만을 뽑아 $\obj(\mathcal{A})$의 부분집합 $\mathcal{S}$를 만들 수 있다. 임의의 $S_1,S_2\in\mathcal{S}$에 대하여, $\Hom_\mathcal{S}(S_1,S_2)=\Hom_\mathcal{A}(S_1,S_2)$로 두자. 정의로부터 $\mathcal{S}$는 $\mathcal{A}$의 subcategory이고, 자명하게 정의되는 inclusion functor $\mathcal{S}\hookrightarrow\mathcal{A}$가 faithful functor가 된다. ([§범주, ⁋정의 5](/ko/math/category_theory/categories#def5)) 만일 이 functor가 full이기도 하다면 $\mathcal{S}$를 *full subcategory<sub>충만한 부분카테고리</sub>*라 부른다. ([§함자, ⁋정의 10](/ko/math/category_theory/functors#def10))

앞선 논증과 같이 small category $\mathcal{A}$로부터 subcategory $\mathcal{S}$를 만들 경우, $\mathcal{S}$가 $\mathcal{A}$를 설명하기에 충분한 정보를 가지고 있는지가 당연한 의문이 된다. 가령 $\mathcal{A}$에서는 morphism $f:A_1\rightarrow A_2$가 존재하지만, $A_1,A_2$와 isomorphic한 대상들 $A_1',A_2'$를 택할 경우 morphism $A_1'\rightarrow A_2'$가 존재하지 않는다면 $\mathcal{S}$는 $\mathcal{A}$가 갖고 있는 정보를 잃어버렸다고 할 수 있을 것이다. 하지만 조금만 생각을 해 보면, 이러한 일은 절대로 일어나지 않는다는 것을 알 수 있다. Morphism $f:A_1\rightarrow A_2$가 주어질 때마다, isomorphism들 $A_1'\rightarrow A_1$, $A_2\rightarrow A_2'$와 $f$를 합성하여 $A_1'\rightarrow A_2'$를 만들어낼 수 있기 때문이다.

이러한 관점에서 위에서 만들어낸 category $\mathcal{S}$는 본질적으로 $\mathcal{A}$의 모든 정보를 담고 있는 것으로 생각할 수 있다. 물론 isomorphic한 대상들 중 어떤 것을 뽑는지에 따라 $\mathcal{S}$ 자체는 달라지겠지만, 다른 선택으로 얻어지는 category도 반드시 $\mathcal{S}$와 isomorphic하다는 것은 쉽게 증명할 수 있다. 

::: 정의 4
Category $\mathcal{A}$의 *skeleton<sub>뼈대</sub>*은 $\mathcal{A}$의 full subcategory 중 skeletal category이면서 임의의 $A\in\obj(\mathcal{A})$가 그 subcategory의 어떤 object와 isomorphic하도록 하는 것을 의미한다. 이를 $\sk(\mathcal{A})$으로 적는다.
:::

다음 정리의 증명은 길고 지루하여 별도로 적어두지 않는다. 증명에 별도의 아이디어가 필요하지는 않으나, fully faithful이면서 essentially surjective인 functor $F:\mathcal{A}\rightarrow\mathcal{B}$로부터 [정의 2](#def2)의 조건을 만족하는 $G:\mathcal{B}\rightarrow\mathcal{A}$를 만드는 방향에서는 각각의 $B\in\obj(\mathcal{B})$마다 $F(A)\cong B$인 $A\in\obj(\mathcal{A})$와 그 isomorphism을 하나씩 골라야 하므로 선택공리를 쓴다. 많은 경우에는 equivalence의 정의를 아예 이것으로 받아들이기도 한다.

::: 정리 5
Functor $F:\mathcal{A}\rightarrow\mathcal{B}$가 category들 사이의 equivalence인 것은 $F$가 fully faithful functor이면서, 다음과 같은 센스에서 *essentially surjective<sub>본질적 전사 함자</sub>*인 것과 동치이다.

> 임의의 $B\in\obj(\mathcal{B})$마다 적당한 $A\in\obj(\mathcal{A})$가 존재하여 $F(A)\cong B$가 성립하도록 할 수 있다.
:::

$\mathcal{A}$의 skeleton을 생각하면, inclusion functor $\sk(\mathcal{A})\hookrightarrow\mathcal{A}$는 full subcategory의 inclusion이므로 fully faithful이고, [정의 4](#def4)의 마지막 조건이 곧 이 functor가 essentially surjective라는 것이다. 따라서 [정리 5](#thm5)에 의하여 이 inclusion은 equivalence이고, $\mathcal{A}\simeq\sk(\mathcal{A})$가 성립한다. 이로부터 다음을 얻는다.

::: 따름정리 6
두 small category $\mathcal{A}$와 $\mathcal{B}$가 equivalent한 것은 이들의 skeletal subcategory $\sk(\mathcal{A})$와 $\sk(\mathcal{B})$가 isomorphic한 것이다.
:::

만일 $\sk(\mathcal{A})\cong\sk(\mathcal{B})$라면 category들 사이의 isomorphism은 equivalence이기도 하고 equivalence들의 합성 또한 equivalence이므로 $\mathcal{A}\simeq\sk(\mathcal{A})\simeq\sk(\mathcal{B})\simeq\mathcal{B}$를 얻는다. 역으로 $\mathcal{A}\simeq\mathcal{B}$인 경우, [정의 2](#def2)의 조건이 두 functor에 대하여 대칭이므로 $\sk(\mathcal{A})\simeq\mathcal{A}\simeq\mathcal{B}\simeq\sk(\mathcal{B})$이고, 따라서 equivalence $F:\sk(\mathcal{A})\rightarrow\sk(\mathcal{B})$가 존재한다. 이때 $F(S_1)$에서 $F(S_2)$로의 isomorphism이 주어지면, $F$가 full이므로 이 isomorphism과 그 inverse는 각각 적당한 $g:S_1\rightarrow S_2$와 $h:S_2\rightarrow S_1$에 대하여 $F(g)$와 $F(h)$의 꼴로 적히고, $F(h\circ g)=F(\id_{S_1})$과 $F(g\circ h)=F(\id_{S_2})$에 $F$의 faithfulness를 적용하면 $g$가 isomorphism임을 얻는다. 그럼 $\sk(\mathcal{A})$가 skeletal이므로 $S_1=S_2$이다. 또 $F$가 essentially surjective이므로 임의의 $T\in\obj(\sk(\mathcal{B}))$마다 $F(S)\cong T$인 $S$가 존재하고, $\sk(\mathcal{B})$가 skeletal이므로 $F(S)=T$이다. 그럼 $F$는 object에 대하여 전단사이면서 fully faithful이므로 두 category 사이의 isomorphism이다.

---

**참고문헌**

**[Rie]** Emily Riehl. *Category Theory in Context*. Dover Publications, 2016.

---