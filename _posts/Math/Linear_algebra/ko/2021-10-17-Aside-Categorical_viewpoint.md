---
layout: single
date: 2021-10-17
title: "기본정리: categorical viewpoint<sup>†</sup>"
categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/ftla_categorical_viewpoint
header:
    overlay_image: /assets/images/Linear_algebra/Basis_and_dimension.png
    overlay_filter: 0.5
toc: true
toc_sticky: true
comments: true
sidebar: 
    nav: "preliminaries"
excerpt: "Matrix"
lang: ko
weight: 8
---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


약간 과한 감은 있지만, 우리는 이미 많은 대수적 구조를 알고 있으므로 살짝 category를 소개해도 괜찮을 것 같다. 엄밀한 정의를 소개하기 전에 우리가 이미 친숙한 몇 가지 예시들을 살펴보자.

## 대수적인 구조들

가장 단순한 대수적인 구조는 집합이다. 집합들의 모임[^1] $\mathbf{Set}$을 생각하자. 집합들 사이에는 이들 사이의 관계를 나타내어 주는 *함수*라는 것이 존재하며, 두 집합 간의 함수들 중 특별히 *bijection*들은 이 두 집합을 집합론적으로 동등하게 취급해도 된다는 것을 보여준다. 특히, 임의의 집합 $A$에 대하여 $\operatorname{id}_A:A\rightarrow A$는 bijection이다. 또, $f:A\rightarrow B$가 bijection이라면 적당한 $g:B\rightarrow A$가 존재하여 $f\circ g=\operatorname{id}_B$이고 $g\circ f=\operatorname{id}_A$이고, 그 역도 성립한다.

또, 우리가 지금 살펴보고 있는 구조인 벡터공간이 있다. 고정된 체 $F$에 대하여, $F$-벡터공간들의 모임 $\mathbf{Vect}_F$를 생각하자. 두 $F$-벡터공간들 사이에는 *선형사상*이라는 것이 존재하며, 두 벡터공간들 간의 선형사상 중 특별히 *동형사상*들은 이 두 벡터공간을 동일하게 취급해도 된다는 것을 보여준다. 당연히 임의의 $F$-벡터공간 $V$에 대하여 $\operatorname{id}_V$는 동형사상이고, 어떤 선형사상 $L:V\rightarrow W$가 동형사상이라는 것은 적당한 $M:W\rightarrow V$가 존재하여 $L\circ M=\operatorname{id}_W$이고 $M\circ L=\operatorname{id}_V$인 것과 동치이다.

제대로 다루진 않았지만 우리는 가환군이라는 대수적인 구조도 알고 있다. ([§Basic definition, 정의 1](/ko/math/linear_algebra/basic_definition#df1)) 이들의 모임을 $\mathbf{Ab}$이라 하자. 두 가환군 $G$, $H$가 주어졌을 때, 다음의 식

$$f(x+y)=f(x)+f(y)$$

을 만족하는 $f:G\rightarrow H$를 *군 준동형사상*이라 부른다. 이들 가운데 bijective한 군 준동형사상들을 우리는 *군 동형사상* 혹은 간단히 *동형사상*이라 부른다. 임의의 가환군 $G$에 대하여 $\operatorname{id}_G$는 동형사상이고, 또 어렵지 않게 $f:G\rightarrow H$가 동형사상인 것이 적당한 $g:H\rightarrow G$가 존재하여 $f\circ g=\operatorname{id}_H$이고 $g\circ f=\operatorname{id}_G$가 성립하는 것과 동치임을 확인할 수 있다.

## Category

위의 예시들 $\mathbf{Set}$, $\mathbf{Vect}_F$, $\mathbf{Ab}$ 등은 공통적인 특징을 가지고 있다. 이들은 어떠한 대수적인 *대상*들의 모임이고, 이 대상들의 성질을 보존하는 특정한 함수들이 존재한다. 또, 두 대상을 같은 것으로 취급할 수 있도록 하는 더욱 특별한 함수들 (bijection, 동형사상 등)이 존재한다. 이를 바탕으로 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> *Category* $\mathcal{C}$는 다음 정보들로 이루어진 대상이다.

- $\mathcal{C}$의 *object*들 $X,Y,Z,\ldots$로 이루어진 모임 $\operatorname{obj}(\mathcal{C})$
- 각각의 $X,Y\in \operatorname{obj}(\mathcal{C})$마다 대응되는 *morphism*들의 모임 $\operatorname{Mor}(X,Y)$
- 각각의 $X,Y,Z\in\operatorname{obj}(\mathcal{C})$에 대해, $\operatorname{Mor}(X,Y)$와 $\operatorname{Mor}(Y,Z)$의 원소들의 쌍을 $\operatorname{Mor}(X,Z)$로 보내는 *composition*, $\circ: (f,g)\mapsto g\circ f$.

이들은 다음의 조건을 만족해야 한다. 

- Composition은 결합법칙을 만족한다. 
- 각각의 $X\in\operatorname{obj}(\mathcal{C})$마다 *identity morphism* $\operatorname{id}\_X\in\operatorname{Mor}(X,X)$가 존재하여, 임의의 $f\in\operatorname{Mor}(X,Y)$와 $g\in\operatorname{Mor}(Z,X)$에 대하여 $f\circ \operatorname{id}\_X=f$이고 $\operatorname{id}\_X\circ g=g$이다.

</div>

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Category $\mathcal{C}$와 임의의 $f\in \operatorname{Mor}(X,Y)$에 대하여, 만일 적당한 $g\in\operatorname{Mor}(Y,X)$가 존재하여 $f\circ g=\operatorname{id}_Y$이고 $g\circ f=\operatorname{id}_X$라면 $f$가 *isomorphism*이라 하고, $X$와 $Y$가 *isomorphic*하다고 한다.

</div>

앞서 소개한 예시들은 모두 위의 두 정의와 잘 어울린다. 약간의 예시를 더 살펴보자. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 우선, *유한차원* $F$-벡터공간들의 category $\mathbf{FVect}_F$가 있다. 이 category는 $\mathbf{Vect}_F$의 모든 정의를 공유하지만, object들을 모든 $F$-벡터공간들 대신 유한차원의 $F$-벡터공간으로만 제한했다는 점이 다르다. 이를 *subcategory*라 부르면 적절할 것이다.

</div>

Category는 보편적으로 어떠한 대수적인 구조들과 그들 사이의 특정한 함수들이 장착된 모임이라 생각할 수 있지만, 얼마든지 더 추상적인 category를 만들 수 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> Category $\mathbf{Mat}_F$를 다음과 같이 정의한다.

- $\mathbf{Mat}_F$의 object들은 자연수들 $0,1,2,\ldots$이다.
- 각각의 $m,n$에 대하여, $\operatorname{Mor}(m,n)$은 $m\times n$ 행렬들의 모임 $\operatorname{Mat}\_{m\times n}(F)$로 주어진다.
- 마지막으로, composition map은 matrix의 곱으로 주어진다. 즉 만일 $A\in\operatorname{Mor}(m,n)=\operatorname{Mat}\_{m\times n}(F)$이고, $B\in\operatorname{Mor}(n,k)=\operatorname{Mat}\_{n\times k}(F)$라면 composition $(A,B)\mapsto B\circ A$는 단순히 행렬의 곱 $BA\in\operatorname{Mat}\_{m\times k}(F)=\operatorname{Mor}(m,k)$으로 정의된다.

자연수들 $1,2,3,\ldots$들 각각을 집합론적으로 $\\{0\\},\\{0,1\\},\ldots$ 등과 같이 취급하지 않는 이상, $\mathbf{Mat}_F$의 object들은 모두 어떠한 대수적인 대상도 아니다. 또 임의의 $A\in \operatorname{Mor}(m,n)$ 또한 기존의 morphism들과는 다르다. 즉, $A$를 어떤 대수적인 대상 $m$에서 또 다른 대상 $n$으로 가는 함수라고 생각할 수도 없다. 

</div>

물론 $\mathbf{Mat}_F$의 object들 $1,2,3,\ldots$을 Euclidean $F$-벡터공간들 $F^1, F^2,F^3,\ldots$으로 보면 위의 $\mathbf{Mat}_F$를 기존의 category들과 거의 동일하게 취급할 수 있지만, 어쨌든 category의 정의 중 어떠한 것도 object들 혹은 morphism들의 모양을 강제하지 않는다.

## Functor

Category에서 모든 대상은 morphism을 통해 다른 대상과 연결되어 있다. Category도 어쨌거나 대수적인 대상이므로, 이들을 살펴보기 위해서는 category $\mathcal{C}$에서 다른 category $\mathcal{D}$로의 morphism을 생각해야 한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 두 개의 category $\mathcal{C}$, $\mathcal{D}$가 주어졌다 하자. $F:\mathcal{C}\rightarrow\mathcal{D}$가 이들 사이의 *functor*라는 것은,

1. $F$는 $\mathcal{C}$의 object를 $\mathcal{D}$의 object로 옮긴다. 즉, 임의의 $A\in\operatorname{obj}(\mathcal{C})$에 대하여 $F(A)\in\operatorname{obj}(\mathcal{D})$가 성립한다.
2. $F$는 $\mathcal{C}$의 morphism을 $\mathcal{D}$의 morphism으로 옮긴다. 즉, 임의의 $f:A\rightarrow B$는 $F$에 의해 $F(f): F(A)\rightarrow F(B)$로 옮겨진다.
3. $F$는 composition과 identity를 잘 보존한다. 즉, $F(\operatorname{id}\_A)=\operatorname{id}\_{F(A)}$가 성립하고, 또 임의의 $g\circ f$에 대하여 $F(g\circ f)=F(g)\circ F(f)$이다.

</div>

위의 정의는 covariant functor의 정의이고, 사실은 contravaiant functor도 존재하지만 앞으로 할 내용에서 contravariant는 사용되지 않으므로 무시하기로 한다. 

Category들 사이의 functor가 *isomorphism*이라는 것을 정의하는 것은 언제나와 같이 하면 된다. 하지만 많은 경우에 isomorphic한 두 개의 category는 너무 과하기 때문에 이보다 약한 *equivalence*라는 개념을 정의한다. 

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 두 개의 category $\mathcal{C}$, $\mathcal{D}$ 그리고 functor $F:\mathcal{C}\rightarrow\mathcal{D}$가 주어졌다 하자. 고정된 $A,B\in\operatorname{obj}(\mathcal{C})$에 대해, 함수

$$F_{A,B}:\operatorname{Mor}_\mathcal{C}\rightarrow\operatorname{Mor}_\mathcal{D}(F(A),F(B))$$

가 잘 정의된다. 만일

1. 임의의 $A,B\in\in\operatorname{obj}(\mathcal{C})$에 대해 $F_{A,B}$가 injective라면 $F$가 *faithful*이라 한다.
2. 임의의 $A,B\in\in\operatorname{obj}(\mathcal{C})$에 대해 $F_{A,B}$가 surjective라면 $F$가 *full*이라 한다.
3. 임의의 $A,B\in\in\operatorname{obj}(\mathcal{C})$에 대해 $F_{A,B}$가 bijective라면 $F$가 *fully faithful*이라 한다.

또, 만일 임의의 $C\in\operatorname{obj}(\mathcal{D})$에 대하여 적당한 $A\in\operatorname{obj}(\mathcal{C})$가 존재하여 $C$와 $F(A)$가 isomorphic한 object라면, $F$가 *essentially surjective*라 한다.

Essentially surjective한 fully faithful functor $F$를 $\mathcal{C}$에서 $\mathcal{D}$로의 *equivalence*라 부르고, 이 때 $\mathcal{C}$와 $\mathcal{D}$가 *equivalent*하다고 한다. 

</div>



## 선형대수학의 기본정리

이제 다시 선형대수로 돌아오자. 우리가 주로 살펴볼 category는 $\mathbf{Mat}_F$와 $\mathbf{FVect}_F$이다. 우리는 앞으로 논의의 편의 상 $\mathbf{FVect}_F$의 원소들인 유한차원 벡터공간들은 항상 기저가 고정된 상태라고 생각한다. 즉, $(V,\mathcal{B})$와 $(V,\mathcal{B}')$는 기저 $\mathcal{B}$와 $\mathcal{B}'$가 다르게 주어졌으므로 다른 벡터공간으로 취급할 것이다. 

각각을 diagram으로 나타내자면, category $\mathbf{Mat}_F$는 다음과 같다.

![category_of_matrices](/assets/images/Linear_algebra/Aside-Categorical_viewpoint-1.png){:width="360px" class="invert" .align-center}

위의 diagram에서, $m$에서 $n$으로 가는 화살표 각각은 $\operatorname{Mat}\_{m\times n}(F)$, 즉 $m\times n$ 행렬 하나씩을 의미한다. 여백 때문에 $2$와 $3$에는 별다른 표기를 하지 않았지만, $2$나 $3$ 각각에도 당연히 자기 자신으로의 map이 존재할 것이며, 그 중에는 identity map도 존재할 것이다. Identity map의 경우는 명백한 inverse가 존재하므로 $\leftrightarrow$로 표기했다.

한편, $\mathbf{FVect}_F$는 더 복잡하다. $\mathbf{Mat}_F$의 경우에는 서로 다른 object들 사이의 isomorphism이 존재하지는 않지만 ([§선형사상과 행렬표현, 정의 9 직후의 remark](/ko/math/linear_algebra/matrix#df9)) 서로 다르지만 동형인 유한차원 벡터공간은 얼마든지 있기 때문이다. 

따라서 이 경우 diagram은 대략적으로 다음과 같은 모양이 된다.

![category_fvect](/assets/images/Linear_algebra/Aside-Categorical_viewpoint-2.png){:width="240px" class="invert" .align-center}

이들 두 category는 분명 다르지만, $\mathbf{FVect}_F$의 도여형인 벡터공간들을 따로 분류한 후, 이들을 하나의 평면으로 정사영시킨다고 하면 그 결과물은 $\mathbf{Mat}_F$과 수상쩍을 정도로 비슷해보인다.

![projection](/assets/images/Linear_algebra/Aside-Categorical_viewpoint-3.png){:width="360px" class="invert" .align-center}

이를 조금 더 수학적으로 표현한 것이 바로 선형대수학의 기본정리다. 위에서 이야기한 *정사영*은 물론 $\mathbf{FVect}_F$에서 $\mathbf{Mat}_F$로의 functor를 의미한다. 이는 다음과 같이 정의된다.

1. 우선 object의 경우, $V$는 이 functor에 의해 $V\mapsto \dim V$로 옮겨진다.
2. Morphism의 경우, 임의의 $L\in\operatorname{Mor}(V,W)$는 $L\mapsto [L]^\mathcal{B}_\mathcal{C}$로 옮겨진다. 여기서 $\mathcal{B}$와 $\mathcal{C}$는 각각 $V$와 $W$에 장착되어있는 basis를 뜻한다.

이것이 실제로 functor가 된다는 것은 어렵지 않게 확인할 수 있다. 즉, 선형대수학의 기본정리는 별다른 것이 아니라 

> 좌표표현(행렬과 좌표표현 모두의)은 $\mathbf{FVect}_F$에서 $\mathbf{Mat}_F$로의 functor

임을 풀어 쓴 것일 뿐이다. 

한편, 우리는 $\mathbf{Mat}_F$의 object들을 $F^n$으로 취급할 수도 있다고 했는데, 이 경우 $F^n$들은 물론 표준기저 $\mathcal{E}_n$이 장착된 공간들로 보는 것이 적절할 것이다. 그럼 이들은 모두 유한차원 $F$-벡터공간이기도 하므로 자연스러운 inclusion morphism $\mathbf{Mat}_F\hookrightarrow\mathbf{FVect}_F$가 존재한다. 어렵지 않게 이 morphism이 essentially surjective한 fully faithful functor임을 알 수 있으므로, 두 category $\mathbf{Mat}_F$와 $\mathbf{FVect}_F$는 정말로 같은 것으로 취급해도 된다.





---
**Reference**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005

---

[^1]: 엄밀히 말하자면, 모든 집합들의 집합은 존재하지 않으므로 이는 proper class가 된다. 나머지 예시들도 마찬가지다.
