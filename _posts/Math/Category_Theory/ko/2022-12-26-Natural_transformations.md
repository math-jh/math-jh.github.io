---

title: "자연변환"
excerpt: "자연변환과 카테고리들 사이의 equivalence"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/natural_transformations
header:
    overlay_image: /assets/images/Category_Theory/Natural_transformations.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2022-12-26
last_modified_at: 2022-12-26
weight: 3

---

## 자연변환의 정의

이번 글에서 우리는 natural transformation을 정의하고, 이를 바탕으로 카테고리들 사이의 equivalence를 정의한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 카테고리 $\mathcal{A},\mathcal{B}$가 주어졌다 하고, $\mathcal{A}$에서 $\mathcal{B}$로의 두 functor $F,G$가 주어졌다 하자. 만일 $\obj(\mathcal{A})$를 index set으로 갖는 morphism들의 family 

$$\bigl(\alpha_A:F(A)\rightarrow G(A)\bigr)_{A\in\obj(\mathcal{A})}$$

이 각각의 $A,A'\in\obj(\mathcal{A})$마다 다음의 diagram

![natural_transformation](/assets/images/Category_Theory/Natural_transformations-1.png){:width="193.65px" class="invert" .align-center}

을 commute하도록 한다면, $\alpha=(\alpha\_A)\_{A\in\obj(\mathcal{A})}$를 *natural transformation<sub>자연변환</sub>*이라 부르고 이를 $\alpha:F\Rightarrow G$와 같이 표기한다.

만일 각각의 $\alpha_A$들이 모두 isomorphism이라면 이를 *natural isomorphism<sub>자연동형변환</sub>*이라 부르고, 두 functor $F,G$가 *naturally equivalent<sub>자연변환에 대해 동등</sub>*하다고 한다. 이를 $F\simeq G$로 표기한다.

</div>

Natural transformation의 개념을 처음 정의한 것은 **[ES]**에서인데, 다음 두 예시가 중요한 motivation으로 소개된다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (Double dual)**</ins> Field $k$를 고정하자. 그럼 *double dual functor* $(-)^{\ast\ast}$는 

- 대상 $V$에 대해서는 double dual $V^{\ast\ast}$,
- morphism $L:V\rightarrow W$에 대해서는 $L^{\ast\ast}:V^{\ast\ast}\rightarrow W^{\ast\ast}$

을 대응시키는 $\Vect{k}$에서 자기자신으로의 functor이다. 여기에서 $L^{\ast\ast}:V^{\ast\ast}\rightarrow W^{\ast\ast}$는 임의의 $v^{\ast\ast}\in V^{\ast\ast}$에 대하여, 다음의 식

$$(L^{\ast\ast}(v^{\ast\ast}))(w^\ast)=(v^{\ast\ast}\circ L^\ast)(w^\ast)=v^{\ast\ast}(w^\ast\circ L)\qquad\text{for all $w^\ast\in W^\ast$}$$

으로 정의되는 linear map이다. 그럼 identity functor $\id\_\Vect{k}$와 double dual functor $(-)^{\ast\ast}$이 naturally equivalent하다. 이는 임의의 $L:V\rightarrow W$에 대하여 다음 diagram

![naturality_of_double_dual](/assets/images/Category_Theory/Natural_transformations-2.png){:width="413.25px" class="invert" .align-center}

이 commute한다는 뜻이며, 이 사실은 임의의 $w^\ast\in W^\ast$에 대하여

$$(Lv)^{\ast\ast}(w^\ast)=w^\ast(Lv)=v^{\ast\ast}(w^\ast\circ L)$$

라는 사실로부터 자명하다.

</div>

반면 dual을 한 번만 취하는 functor $(-)^\ast$는 $\id\_\Vect{k}$와 naturally equivalent하지 않다. 이는 우선 $(-)^\ast$는 contravariant functor인데 반해 $\id\_\Vect{k}$는 covariant functor이기 때문이지만, 조금 더 자세히 살펴볼 수 있다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Dual functor)**</ins> Dual functor $(-)^\ast$를 나타내는 diagram은 다음과 같다.

![unnaturality_of_dual_functor](/assets/images/Category_Theory/Natural_transformations-3.png){:width="358.65px" class="invert" .align-center}

따라서, $(-)^\ast$에 요구될만한 "naturality"는 다음의 식

$$L^\ast\bigl((Lv)^\ast\bigr)=v^\ast$$

정도인데, 이 식의 양 변에 $v'\in V$를 적용해보면

$$v^\ast(v')=L^\ast\bigl((Lv)^\ast\bigr)(v')=(Lv)^\ast(Lv')=v^\ast(L^\ast L)v'$$

가 되고, $(\det L)^2\neq 1$인 $L$에 대하여 이 식은 성립하지 않는다.

</div>

이러한 관점에서, $(-)^{\ast\ast}$가 basis의 선택에 의존하지 않는 함수라는 것을 *자연스러운* 함수라고 했던 것이 어느정도 설명되는데, 만일 $v\mapsto v^{\ast\ast}$가 basis의 선택에 의존하는 함수였다면 [예시 2](#ex2)의 diagram의 두 수직방향 화살표 중 하나를 다른 basis로 바꾸어 commutativity를 깨뜨릴 수 있고, 따라서 [정의 1](#df1)의 조건이 만족되지 않았을 것이기 때문이다.

한편, 다음의 예시도 눈여겨볼만 하다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 

- 임의의 right $R$-module $M,M'$과 $R$-module homomorphism $f:M\rightarrow M'$이 주어졌다 하자. 그럼 각각의 $N\in\lmod{R}$에 대하여, 자연스러운 morphism $\alpha_N:M\otimes_RN\rightarrow M'\otimes_RN$이 존재한다. 이렇게 정의된 $\alpha=(\alpha_N)$은 natural transformation이 된다.
- 비슷하게, 위와 같은 상황에서 자연스러운 morphism $\beta_N:\Hom_R(M',N)\rightarrow \Hom_R(M,N)$을 정의할 수 있다. 이렇게 정의된 $\beta=(\beta_N)$은 두 $\Hom$ functor들 사이의 natural transformation을 정의한다.

</div>

## 동등한 카테고리들

자연변환의 또 다른 motivation 중 하나는 이 개념이 동등한 카테고리의 개념을 정의할 때 사용된다는 것이다. 대수적 위상수학에서 우리는 두 공간의 "뼈대"가 같으면 두 공간을 동등한 것으로 취급할 수 있었다.

img

이와 마찬가지로 두 카테고리의 "뼈대"가 동일하다면 두 카테고리를 동등한 것으로 취급할 수 있다. ([명제 8](#pp8)) 대수위상에서 이를 가능하게 해 주는 도구는 homotopy였는데, 카테고리에서 이 역할을 해 주는 것이 natural transformation이다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 카테고리 $\mathcal{A}$에서 $\mathcal{B}$로의 functor $F$가 *equivalence of category*라는 것은 적당한 functor $G:\mathcal{B}\rightarrow \mathcal{A}$가 존재하여 $\id_\mathcal{A}\simeq G\circ F$이고 $\id_\mathcal{B}\simeq F\circ G$인 것이다. 만일 $\mathcal{A}$에서 $\mathcal{B}$로의 equivalence가 존재한다면 이들 두 카테고리가 *equivalent<sub>동등</sub>*하다고 하고 $\mathcal{A}\simeq\mathcal{B}$으로 표기한다.

</div>

다음 정리의 증명은 쉽지만 길고 지루하다. 따라서 별도로 증명하지 않는다. 실은 다음 정리를 equivalent category의 정의로 보아도 크게 문제될 것이 없다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> Functor $F:\mathcal{A}\rightarrow\mathcal{B}$가 카테고리들 사이의 equivalence인 것은 $\mathcal{F}$가 fully faithful functor인 동시에, 다음과 같은 센스에서 *essentially surjective*한 것이다.

> 임의의 $B\in\obj(\mathcal{B})$마다 적당한 $A\in\mathcal{A}$가 존재하여 $F(A)\cong B$가 성립하도록 할 수 있다.

</div>

이를 받아들인다면 다음 따름정리 또한 자명하다.

<div class="proposition" markdown="1">

<ins id="crl7">**따름정리 7**</ins> 두 카테고리 $\mathcal{A}$와 $\mathcal{B}$가 동등한 것은 이들의 skeletal subcategory $\sk(\mathcal{A})$와 $\sk(\mathcal{B})$가 isomorphic한 카테고리인 것이다.

</div>

## Functor category

자연변환의 마지막 motivation은 다음의 functor category에서 이들이 morphism의 역할을 한다는 것이다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> 작은 카테고리 $\mathcal{A}$와 임의의 카테고리 $\mathcal{B}$에 대하여, 새로운 카테고리 $\mathcal{B}^\mathcal{A}$를

- 대상들은 $\mathcal{A}$에서 $\mathcal{B}$로의 functor들,
- $F,G\in\obj(\mathcal{B}^\mathcal{A})$에 대하여, $F$에서 $G$로의 morphism은 $F$에서 $G$로의 natural transformation들

으로 이루어진 카테고리로 정의한다. 이를 *functor category*라 부른다.

</div>

Natural transformation
Abelian category
Adjoint pair
Representables
Yoneda lemma
Limit
Monad
Operad
Kan extension
Higher category
Infinite category
A infinity category