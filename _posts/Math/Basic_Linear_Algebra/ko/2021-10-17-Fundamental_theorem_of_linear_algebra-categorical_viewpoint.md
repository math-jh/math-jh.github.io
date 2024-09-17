---

title: "기본정리: categorical viewpoint<sup>†</sup>"
excerpt: "선형대수학의 기본정리와 범주론"

categories: [Math / Basic Linear Algebra]
permalink: /ko/math/basic_linear_algebra/ftla_categorical_viewpoint
sidebar: 
    nav: "basic_linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Basic_Linear_Algebra/Fundamental_theorem_of_linear_algebra-categorical_viewpoint.png
    overlay_filter: 0.5

date: 2021-10-17
last_modified_at: 2022-08-07

weight: 13

---

선형대수학의 기본정리는 강력한 정리이지만 지난 글에서 살펴본 것만으로는 왜 이 정리가 강력한 도구인지가 잘 와닿지 않는다. 이번 글에서는 약간의 category theory를 동원하여 선형대수학의 기본정리가 갖는 의미를 좀 더 자세히 살펴본다.

## 대수적인 구조들

우리는 지금까지 많은 대수적인 구조를 살펴봤다. 이들을 간단하게 리뷰해보면 다음과 같다.

우선 집합이 있다. $\mathbf{Set}$을 집합들의 모임이라 하자. 이 모임의 대상들 사이에는 *함수*라 불리는 것들이 있다. 특별히 두 집합 $A,B$ 사이에 *전단사함수*라 불리는 특별한 함수가 정의된다면 우리는 이 두 집합 $A,B$를 동등하게 취급하여도 큰 문제가 없다. 이 때, $f:A\rightarrow B$가 전단사함수라는 것은 적당한 $g:B\rightarrow A$가 존재하여 다음의 두 식

$$f\circ g=\id_B,\qquad g\circ f=\id_A$$

이 성립하는 것이다.

집합 위에 특정한 조건들을 만족하는 연산을 추가하여 우리는 *group*을 정의할 수 있다. ([§가환군과 체, ⁋정의 1](/ko/math/basic_linear_algebra/fields#def1)) $\mathbf{Grp}$을 group들의 모임이라 하자. 두 group $G,H$가 주어졌다 하고, 이들의 연산을 더하기로 표기하자. 함수 $f:G\rightarrow H$가 *group homomorphism<sub>군 준동형사상</sub>*이라는 것은 임의의 $x,y\in G$에 대해 다음의 식

$$f(x+y)=f(x)+f(y)$$

이 성립하는 것이다. 특별히 두 group $G,H$ 사이에 *group isomorphism*이라는 특별한 group homomorphism이 정의된다면 $G$와 $H$는 동등한 group으로 취급된다. 이 때, $f:G\rightarrow H$가 group isomorphism이라는 것은 적당한 $g:H\rightarrow G$가 존재하여 다음의 두 식

$$f\circ g=\id_B,\qquad g\circ f=\id_A$$

이 성립하는 것이다. 특별히 연산이 교환법칙을 만족하는 것들은 *abelian group*이라 부르는데, abelian group들의 모임 위에도 위와 같이 group homomorphism과 group isomorphism을 정의할 수 있다. 이들 모임을 $\mathbf{Ab}$으로 적는다.

우리가 지금 관심을 갖고 살펴보고 있는 대상은 고정된 field $\mathbb{k}$ 위에서 정의된 벡터공간들[^1]의 모임, 곧 $\mathbf{Vect}_F$이다. 두 벡터공간 사이에는 *linear map*이라는 것이 존재하며, 만일 두 벡터공간 $V,W$ 사이에 *isomorphism*이라는 것이 존재하면 이 두 벡터공간을 동등한 것으로 취급한다. 이 때 $L:V\rightarrow W$가 isomorphism이라는 것은 적당한 $L':W\rightarrow V$가 존재하여 다음의 두 식

$$L\circ L'=\id_W,\qquad L'\circ L=\id_V$$

이 성립하는 것이다.

## Category

위의 예시들 $\mathbf{Set}$, $\mathbf{Vect}_F$, $\mathbf{Ab}$ 등은 공통적인 특징을 가지고 있다. 이들은 어떠한 대수적인 대상들의 모임이며, 대상들 사이에는 특정한 함수들 (함수, group homomorphism, linear map 등)이 정의된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *Category<sub>범주</sub>* $\mathcal{C}$는 다음 정보들로 이루어진 대상이다.

- $\mathcal{C}$의 *대상<sub>object</sub>*들 $X,Y,Z,\ldots$로 이루어진 모임 $\obj(\mathcal{C})$
- 각각의 $X,Y\in \obj(\mathcal{C})$마다 대응되는 *morphism<sub>사상</sub>*들의 모임 $\Mor(X,Y)$
- 각각의 $X,Y,Z\in\obj(\mathcal{C})$에 대해, $\Mor(X,Y)$와 $\Mor(Y,Z)$의 원소들의 쌍을 $\Mor(X,Z)$로 보내는 *composition*, $\circ: (f,g)\mapsto g\circ f$.

이들은 다음의 조건을 만족해야 한다. 

- Composition은 결합법칙을 만족한다. 
- 각각의 $X\in\obj(\mathcal{C})$마다 *identity morphism* $\id\_X\in\Mor(X,X)$가 존재하여, 임의의 $f\in\Mor(X,Y)$와 $g\in\Mor(Z,X)$에 대하여 $f\circ \id\_X=f$이고 $\id\_X\circ g=g$이다.

</div>

이 정의 하에서, 전단사함수나 group isomorphism, (linear) isomorphism 등은 다음과 같이 일반화된다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Category $\mathcal{C}$와 임의의 $f\in \Mor(X,Y)$에 대하여, 만일 적당한 $g\in\Mor(Y,X)$가 존재하여 $f\circ g=\id_Y$이고 $g\circ f=\id_X$라면 $f$가 *isomorphism*이라 하고, $X$와 $Y$가 *isomorphic*하다고 한다.

</div>

약간의 예시를 더 살펴보자. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 우선, <em_ko>유한차원</em_ko> $\mathbb{k}$-벡터공간들의 category $\mathbf{FVect}_F$가 있다. 이 category는 $\mathbf{Vect}_F$의 모든 정의를 공유하지만, category의 대상들을 모든 $\mathbb{k}$-벡터공간들 대신 유한차원의 $\mathbb{k}$-벡터공간으로만 제한했다는 점이 다르다. 이를 *subcategory*라 부르면 적절할 것이다.

</div>

Category는 보편적으로 어떠한 대수적인 구조들과 그들 사이의 특정한 함수들이 장착된 모임이라 생각할 수 있지만, 얼마든지 더 추상적인 category를 만들 수 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> Category $\mathbf{Mat}_F$를 다음과 같이 정의한다.

- $\mathbf{Mat}_F$의 대상들은 자연수들 $0,1,2,\ldots$이다.
- 각각의 $m,n$에 대하여, morphism $\Mor(m,n)$은 $m\times n$ 행렬들의 모임 $\Mat\_{m\times n}(F)$로 주어진다.
- 마지막으로, morphism들의 합성은 행렬의 곱으로 주어진다. 즉 만일 $A\in\Mor(m,n)=\Mat\_{m\times n}(F)$이고, $B\in\Mor(n,k)=\Mat\_{n\times k}(F)$라면 이들의 합성 $(A,B)\mapsto B\circ A$는 단순히 행렬의 곱 $BA\in\Mat\_{m\times k}(F)=\Mor(m,k)$으로 정의된다.

자연수들 $1,2,3,\ldots$들 각각을 집합론적으로 $\\{0\\},\\{0,1\\},\ldots$ 등과 같이 취급하지 않는 이상, $\mathbf{Mat}_F$의 object들은 모두 어떠한 대수적인 대상도 아니다. 또 임의의 $A\in \Mor(m,n)$ 또한 기존의 morphism들과는 다르다. 즉, $A$를 어떤 대수적인 대상 $m$에서 또 다른 대상 $n$으로 가는 함수라고 생각할 수도 없다. 

</div>

물론 $\mathbf{Mat}_F$의 대상들 $1,2,3,\ldots$을 Euclidean $\mathbb{k}$-벡터공간들 $F^1, F^2,F^3,\ldots$으로 보면 위의 $\mathbf{Mat}_F$를 기존의 category들과 거의 동일하게 취급할 수 있지만, 어쨌든 category의 정의 중 어떠한 것도 대상들 혹은 morphism들의 모양을 강제하지 않는다.

## Functor

Category에서 모든 대상은 morphism을 통해 다른 대상과 연결되어 있다. Category도 어쨌거나 대수적인 대상이므로, 이들을 살펴보기 위해서는 category $\mathcal{C}$에서 다른 category $\mathcal{D}$로의 morphism을 생각해야 한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 두 개의 category $\mathcal{C}$, $\mathcal{D}$가 주어졌다 하자. $F:\mathcal{C}\rightarrow\mathcal{D}$가 이들 사이의 *functor<sub>함자</sub>*라는 것은,

1. $\mathbb{k}$는 $\mathcal{C}$의 대상을 $\mathcal{D}$의 대상으로 옮긴다. 즉, 임의의 $A\in\obj(\mathcal{C})$에 대하여 $F(A)\in\obj(\mathcal{D})$가 성립한다.
2. $\mathbb{k}$는 $\mathcal{C}$의 morphism을 $\mathcal{D}$의 morphism으로 옮긴다. 즉, 임의의 $f:A\rightarrow B$는 $\mathbb{k}$에 의해 $F(f): F(A)\rightarrow F(B)$로 옮겨진다.
3. $\mathbb{k}$는 합성과 identity morphism을 잘 보존한다. 즉, $F(\id\_A)=\id\_{F(A)}$가 성립하고, 또 임의의 $g\circ f$에 대하여 $F(g\circ f)=F(g)\circ F(f)$이다.

</div>

Category들 사이의 functor가 *isomorphism*이라는 것은 위의 예시들과 같이 정의하면 된다. 그러나 category의 대상들 간의 등호($=$)보다는 isomorphism이 더 적절한 <em_ko>같음</em_ko>의 기준을 주듯이, 두 category 사이의 <em_ko>같음</em_ko>의 개념은 isomorphism 대신 *equivalence*의 개념을 사용하는 것이 더 적절하다.

흔히 사용하는 equivalence의 정의는 따로 있지만, homotopy의 개념을 배우기 전까지는 이와 동치인 다음의 정의를 사용하는 것이 조금 더 직관적으로 와닿는다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 두 개의 category $\mathcal{C}$, $\mathcal{D}$ 그리고 functor $F:\mathcal{C}\rightarrow\mathcal{D}$가 주어졌다 하자. 고정된 $A,B\in\obj(\mathcal{C})$에 대해, 함수

$$F_{A,B}:\Mor_\mathcal{C}\rightarrow\Mor_\mathcal{D}(F(A),F(B))$$

가 잘 정의된다. 만일

1. 임의의 $A,B\in\obj(\mathcal{C})$에 대해 $F_{A,B}$가 injective라면 $\mathbb{k}$가 *faithful*이라 한다.
2. 임의의 $A,B\in\obj(\mathcal{C})$에 대해 $F_{A,B}$가 surjective라면 $\mathbb{k}$가 *full*이라 한다.
3. 임의의 $A,B\in\obj(\mathcal{C})$에 대해 $F_{A,B}$가 bijective라면 $\mathbb{k}$가 *fully faithful*이라 한다.

또, 만일 임의의 $C\in\obj(\mathcal{D})$에 대하여 적당한 $A\in\obj(\mathcal{C})$가 존재하여 $C$와 $F(A)$가 isomorphic한 대상이라면, $\mathbb{k}$가 *essentially surjective*라 한다.

Essentially surjective한 fully faithful functor $\mathbb{k}$를 $\mathcal{C}$에서 $\mathcal{D}$로의 *equivalence*라 부르고, 이 때 $\mathcal{C}$와 $\mathcal{D}$가 *equivalent*하다고 한다. 

</div>

우리가 알고 있는 category가 많지 않아 이에 대한 구체적인 예시를 들 수는 없지만, equivalent한 두 개의 category는 category의 언어로 쓰일 수 있는 대부분의 성질을 공유한다. 직관적으로 두 category가 equivalent하다는 것은 두 category 각각에서 isomorphic한 대상들을 하나로 합치고 나면 남는 것이 동등하다고 생각할 수 있다.

## 선형대수학의 기본정리

이제 위에서 정의한 용어를 사용하면, 선형대수학의 기본정리는 

> 두 category $\mathbf{FVect}_F$와 $\mathbf{Mat}_F$가 equivalent하다.

는 것으로 줄여쓸 수 있다. 여기에서 equivalence $D:\mathbf{FVect}_F\rightarrow\mathbf{Mat}_F$는 다음과 같이 주어진다.

1. 우선 $\mathbf{FVect}_F$의 대상인 유한차원 $\mathbb{k}$-벡터공간 $V$는 $D$에 의하여 $\dim V\in\obj(\mathbf{Mat}_F)$으로 옮겨진다.
2. $\mathbf{FVect}\_F$의 임의의 morphism $L\in\Mor(V,W)$는 $D$에 의하여 $[L]^\mathcal{B}\_\mathcal{C}$로 옮겨진다. 

그럼 $D$는 $\mathbf{FVect}_F$에서 $\mathbf{Mat}_F$로의 functor이다. ([§선형대수학의 기본정리, ⁋정리 5](/ko/math/basic_linear_algebra/ftla#thm5)) 뿐만 아니라, $D$는 fully faithful이기도 하다. ([§선형대수학의 기본정리, ⁋정리 4](/ko/math/basic_linear_algebra/ftla#thm4)) 마지막으로 임의의 $n\in\mathbf{Mat}_F$에 대하여, $n$차원 $\mathbb{k}$-벡터공간이 존재하는 것은 자명하므로 $D$는 essentially surjective이기도 하다.[^2] 따라서 $D$는 두 category 사이의 equivalence를 정의한다.

당연히 두 category 사이의 equivalence는 동치관계가 된다. 이 말은 $\mathbf{FVect}_F$에서 $\mathbf{Mat}_F$로의 equivalence 뿐만 아니라, $\mathbf{Mat}_F$에서 $\mathbf{FVect}_F$로의 equivalence 또한 있다는 의미이다. 이는 $I:\mathbf{Mat}_F\rightarrow\mathbf{FVect}_F$를 

1. 임의의 $n\in\mathbf{Mat}_F$는 $I$를 통해 $\mathbf{FVect}_F$의 원소인 $F^n$으로 옮겨진다. (이 때, $F^n$은 standard basis $\mathcal{E}_n$이 주어진 것으로 생각한다.)
2. $\mathbf{Mat}_F$의 임의의 morphism $A\in\Mor(m,n)$은 $I$를 통해 $L_A:F^m\rightarrow F^n$으로 옮겨진다. ([§선형대수학의 기본정리, ⁋예시 1](/ko/math/basic_linear_algebra/ftla#ex1))

으로 정의하면 된다. $I$가 equivalence라는 것은 $D$가 equivalence라는 것과 아주 크게 다르지는 않으므로 생략한다. 

---

[^1]: 각각의 벡터공간은 basis의 선택이 이루어진 상태라 생각한다. 즉, 집합으로서 동일한 벡터공간 $V$라 하더라도 다른 basis를 택했다면 <em_ko>다른</em_ko> 벡터공간으로 취급하자. 물론 이러한 벡터공간들은 isomorphic하다.
[^2]: 사실, 이 경우엔 *essentially* surjective보다 차라리 그냥 surjective라 부르는 것이 정확해보이기도 한다.