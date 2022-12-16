---

title: "Categories and Functors"
excerpt: "Category의 기본 정의"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/categories_and_functors
header:
    overlay_image: /assets/images/Background/Set-Theory_ZFC-axioms.png
    overlay_filter: 0.5
sidebar: 
    nav: "foundation"

date: 2021-09-21
last_modified_at:
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

## Introduction

Category theory는 집합론과 함께, 현대 수학의 근간을 이루는 분야 중 하나다. 어떻게 보면 집합론보다도 강력하다고 생각할 수도 있는데, 기본적으로 집합론은 집합 위에 어떠한 연산이나, 구조도 주어지지 않은 상태만 공부하지만 category theory에서는 특정한 연산이나 구조들(없을수도 있고)이 주어진 집합들[^1], 그리고 그러한 대상들 사이의 관계에 대해 공부하기 때문이다. 

우리의 목적은 **[Rie]**의 챕터 4까지를 공부하는 것이다. 다만, category theory라는 것은 기본적으로 수학의 모든 분야들을 하나의 통합된 관점으로 보려는 생각으로 만들어진 것이기 때문에, 중간중간의 예시들은 다른 분야의 것들이 많이 등장할 것이다. 그렇기 때문에, 이걸 공부하기 위해서는 학부 2~3학년 정도까지 배우는 과목들 (현대대수라던가, 위상수학이라던가 등등) 정도는 기억을 해 두는 것이 좋다.

## Basic definition of category

우선 정의로 시작하자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> *Category* $\mathcal{C}$는 다음 정보들로 이루어진 대상이다.

- $\mathcal{C}$의 *object*들 $X,Y,Z,\ldots$로 이루어진 모임 $\operatorname{obj}(\mathcal{S})$
- 각각의 $X,Y\in \operatorname{obj}(\mathcal{C})$마다 대응되는 *morphism*들의 모임 $\operatorname{Mor}(X,Y)$
- 각각의 $X,Y,Z\in\operatorname{obj}(\mathcal{C})$에 대해, $\operatorname{Mor}(X,Y)$와 $\operatorname{Mor}(Y,Z)$의 원소들의 쌍을 $\operatorname{Mor}(X,Z)$로 보내는 *composition* $\circ: (f,g)\mapsto g\circ f$.

이들은 다음의 조건을 만족해야 한다. 

- Composition은 associative하다.
- 각각의 $X\in\operatorname{obj}(\mathcal{C})$마다 *identity morphism* $\operatorname{id}\_X\in\operatorname{Mor}(X,X)$가 존재하여, 임의의 $f\in\operatorname{Mor}(X,Y)$와 $g\in\operatorname{Mor}(Z,X)$에 대하여 $f\circ \operatorname{id}\_X=f$이고 $\operatorname{id}\_X\circ g=g$이다.

</div>

<div class="warning" markdown="1">

<ins id="ex2">**예시 2**</ins> 예를 들어, $\mathbf{Set}$은 object들이 집합들이고, morphism은 집합 간의 함수로 이루어진 category이다. 한편, *pointed set*들의 category $\mathbf{Set}\_\*$들은 <span class="border-highlight">집합 $X$와 $X$의 한 원소 $x$의 pair $(X,x)$들</span>을 object들로 갖고, 이들 사이의 basepoint-preserving[^2] function $f$들을 morphism으로 갖는 category이다. 

</div>

위 예시에서는 미묘한 문제가 있다. $\operatorname{obj}(\mathbf{Set})$은 *모든 집합들의 모임*이고, 우리는 이러한 모임이 집합이 되지 못한다는 것을 알고 있다. ([Set Theory, §ZFC 공리계, 예시 4](/ko/math/set_theory/zfc_system#pp4)) 그러나 우리는 해당 예시에서 (strongly) inaccessible cardinal의 존재를 가정한다면 이런 문제를 피해갈 수 있다는 것을 아주 간략하게 언급하기도 했었다. 그 때와 마찬가지로, 우리는 이번에도 이런 집합론적인 문제들은 무시하고 지나가기로 한다.

마저 예시를 살펴보자.

<div class="warning" markdown="1">

<ins id="ex<#number#>">**예시 <#number#>**</ins> <#content#>

</div>

<div class="warning" markdown="1">

<ins id="ex3">**예시 3**</ins> $\mathbf{Top}$은 topological space들을 각각의 object들로, 그리고 이들 사이의 continuous map들을 morphism으로 갖는 category이다. 또, $\mathbf{Top}\_\*$ 또한 위의 [예시 2](#ex2)와 같이 정의된다.

</div>




---

**Reference**

**[Rie]** E. Riehl. <i>Category Theory in Context</i>. Aurora: Dover Modern Math Originals. Dover Publications, 2017.  
   (Also available in her [website](https://emilyriehl.github.io/files/context.pdf))

---

[^1]: 심지어 집합이 아닐 수도 있다.
[^2]: 여기서 $f$가 basepoint-preserving이라는 것은, $(X,x)$와 $(Y,y)$가 주어진 object일 때, $f(x)=y$가 성립한다는 것을 뜻한다.
