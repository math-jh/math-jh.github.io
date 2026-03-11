---
title: "아핀다양체"
excerpt: "Affine varieties and their basic properties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_Varieties.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-12
weight: 1

---

대수기하학에서 우리의 목표는 다항식으로 정의되는 기하적 대상들을 연구하는 것이다. 구체적으로, field $$\mathbb{K}$$와 자연수 $$n$$이 주어졌을 때, 우리는 다음의 식

$$V(f)= \{(a_1, \ldots, a_n) \in \mathbb{A}^n \mid f(a_1, \ldots, a_n) = 0\},\qquad f\in \mathbb{K}[\x_1,\ldots, \x_n]$$

으로 주어지는 집합들에 관심이 있다. 일반적으로 $$\mathbb{K}=\mathbb{C}$$로 두지만, 대부분의 경우 이렇게 가정하는 것이 큰 도움이 되지는 않으므로 우리는 더 일반적인 세팅을 사용하기로 한다. 또, 혼동을 방지하기 위하여 다항식 $$f$$의 변수는 정자 $$\x$$와 같은 식으로 표기할 것이다. 

## 아핀다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field $$\mathbb{K}$$ 위에 정의된 *affine $n$-space<sub>$n$차원 아핀공간</sub>* $$\mathbb{A}^n_\mathbb{K}$$는 $$n$$차원 벡터공간 $$\mathbb{K}^n$$을 의미한다.

</div>

맥락상 $$\mathbb{K}$$를 생략해도 될 때는 $$\mathbb{A}^n$$과 같이 적는다. 우리는 affine space

$$\mathbb{A}^n=\{(a_1,\ldots, a_n)\mid a_i\in \mathbb{K}\}$$

의 원소를 *점<sub>point</sub>*이라 부르고, 각각의 좌표 $$a_i$$를 *$i$번째 좌표*라 부른다. 위에서 언급했듯, 우리가 살펴볼 기하적인 대상들은 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$의 zero set $$V(f)$$로 나타나는 대상들이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$f_1, \ldots, f_k \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, 이들이 정의하는 *affine variety<sub>아핀다양체</sub>* $$V(f_1, \ldots, f_k)$$를

$$V(f_1, \ldots, f_k) = \{(a_1, \ldots, a_n) \in \mathbb{A}^n \mid f_1(a) = \cdots = f_k(a) = 0\}$$

으로 정의한다.

</div>

즉, 아핀다양체는 여러 다항식들 $$f_1,\ldots, f_k$$의 common zero들의 모임이다. 더 일반적으로, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 부분집합 $$I$$에 대하여 $$V(I)$$를 위의 정의와 비슷하게 정의할 수 있다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 우리가 아는 대다수의 기하학적인 대상들은 다항식으로 나타나므로, 이들이 모두 affine variety의 예시가 된다.

1. $$\mathbb{A}^2$$ 안에서 정의된 affine variety $$V(\x^2+\y^2-1)$$을 생각하자. 정의에 의해, 이 집합은 식 $$\x^2+\y^2-1=0$$을 만족하는 $$\mathbb{A}^2$$의 점들의 모임이므로, 단위원을 나타낸다.
2. 일반적으로, 임의의 affine space $$\mathbb{A}^n$$와 임의의 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여, $$V(f)$$는 *초곡면<sub>hypersurface</sub>*을 정의한다.
3. 또 다른 중요한 예시로, $$\mathbb{A}^3$$ 위에 정의된 *twisted cubic*이 있다. 이는 $$\mathbb{A}^3$$ 위에 정의된 두 다항식 $$\y-\x^2$$, $$\z-\x^3$$으로 정의되는 곡선으로, 매개화 $$(t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 일대일로 대응된다.
4. Affine space $$\mathbb{A}^n$$ 자기자신과 공집합은 affine variety이다. 이는 $$V(0)=\mathbb{A}^n$$, $$V(1)=\emptyset$$으로부터 자명하다. 이는 [명제 4](#prop4)에서 Zariski topology를 정의할 때 중요하게 사용된다. 

</div>

위의 예시에서 우리는 친숙한 기하학적 대상들이 모두 집합으로서는 affine variety로 쓰여질 수 있음을 보았다. 그러나 이를 기하학적 대상이라 생각하기 위해서는 그 위에 위상구조가 존재해야 한다. 우리의 유일한 도구는 다항식이므로, 이를 사용하여 위상구조를 정의할 것이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음이 성립한다.

1. $$V(0) = \mathbb{A}^n$$,
2. $$V(1) = \emptyset$$,
3. $$I \subseteq J \implies V(J) \subseteq V(I)$$,
4. $$\displaystyle\bigcap_{\alpha} V(I_\alpha) = V\left(\sum_\alpha I_\alpha\right)$$,
5. $$V(I) \cup V(J) = V(I \cap J) = V(IJ)$$.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 명제는 [예시 3](#ex3)에서 이미 살펴보았다. 세 번째 결과를 증명하기 위해 $$p\in V(J)$$라 하자. 그럼 모든 $$f \in J$$에 대해 $$f(p) = 0$$이고, $$I \subseteq J$$이므로 특히 모든 $$g \in I$$에 대해서도 $$g(p) = 0$$이다. 즉 $$p \in V(I)$$이다.

네 번째 결과의 경우, 점 $$p$$가 모든 $$V(I_\alpha)$$에 속한다는 것은 모든 $$\alpha$$와 모든 $$f \in I_\alpha$$에 대해 $$f(p) = 0$$이라는 것이다. 이는 $$\sum_\alpha I_\alpha$$의 모든 원소가 $$p$$에서 0이라는 것과 동치이다.

마지막 주장을 보이기 위해 우선 $$V(I) \cup V(J) \subseteq V(I \cap J)$$를 보이자. $$p \in V(I) \cup V(J)$$라면 $$p \in V(I)$$이거나 $$p \in V(J)$$이다. 어느 경우이든 $$I \cap J$$의 모든 원소는 $$p$$에서 0이므로 $$p \in V(I \cap J)$$이다. 거꾸로 $$p \in V(I \cap J)$$라 하자. 만약 $$p \notin V(I)$$라면 어떤 $$f \in I$$가 존재하여 $$f(p) \neq 0$$이다. 그런데 $$IJ \subseteq I \cap J$$이므로 $$p \in V(I \cap J) \subseteq V(IJ)$$이고, 따라서 모든 $$g \in J$$에 대해 $$(fg)(p) = f(p)g(p) = 0$$이다. $$f(p) \neq 0$$이므로 $$g(p) = 0$$이고, 즉 $$p \in V(J)$$이다.

</details>

특히 위의 명제는 affine variety들의 모임을 닫힌집합으로 갖는 위상이 존재함을 보여준다. ([\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)) 우리는 이러한 위상을 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다. 예를 들어 $$\mathbb{A}^1$$에서 Zariski topology는 vofinite topology와 같다는 것을 확인할 수 있으며, 특히 이는 하우스도르프가 아니다.

## 영점정리

위의 $$V$$는 대수적인 대상들 (다항식들)을 기하적인 대상으로 보내준다. 거꾸로 우리는 기하적인 대상을 받아 대수적인 대상들을 대응시켜줄 수도 있다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 부분집합 $$X \subseteq \mathbb{A}^n$$에 대하여, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 부분집합 $$I(X)$$를

$$I(X) = \{f \in \mathbb{K}[\x_1, \ldots, \x_n] \mid f(a) = 0 \text{ for all } a \in X\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\mathbb{A}^n$$의 부분집합들 $$X,Y$$, $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 임의의 부분집합 $$I$$에 대하여 다음이 성립한다. 

1. $$X \subseteq Y$$라면 $$I(Y) \subseteq I(X)$$이다.
2. $$I(\emptyset) = \mathbb{K}[\x_1, \ldots, \x_n]$$이다.
3. $$\mathbb{K}$$가 무한하다면 $$I(\mathbb{A}^n) = (0)$$이다.
4. $$X \subseteq V(I(X))$$가 항상 성립한다.
5. $$I \subseteq I(V(I))$$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. $$X \subseteq Y$$이고 $$f \in I(Y)$$라면, 모든 $$a \in Y$$에 대해 $$f(a) = 0$$이다. 특히 모든 $$a \in X$$에 대해 $$f(a) = 0$$이므로 $$f \in I(X)$$이다.
2. 공집합의 조건을 만족하는 함수는 모든 다항식이다.
3. $$\mathbb{K}$$가 무한체이면, 모든 점에서 0인 다항식은 영다항식뿐이다.
4. $$a \in X$$이고 $$f \in I(X)$$라면 $$f(a) = 0$$이다. 즉 $$a \in V(I(X))$$이다.
5. $$f \in I$$이고 $$a \in V(I)$$라면 $$f(a) = 0$$이다. 즉 $$f \in I(V(I))$$이다.

</details>

즉, $$V$$와 $$I$$는 antitone Galois connection을 정의한다. ([\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋정의 6](/ko/math/set_theory/filter_and_ideal#def6)) 따라서 두 operator의 합성 $$VI$$와 $$IV$$ 각각은 closure operator를 정의한다. $$VI$$의 경우, 이 closure는 실제로 Zariski topology에서의 closure가 된다. 이는 만일 $$X \subseteq Y = V(J)$$이면 $$I(V(J)) \subseteq I(X)$$이고, [명제 6](#prop6)의 5번 조건에서 $$J \subseteq I(V(J))$$이므로 $$VI(X) \subseteq V(J) = Y$$가 되워, $$VI(X)$$가 $$X$$를 포함하는 Zariski closed set 중 가장 작은 것이 되기 때문이다. $$IV$$의 경우에는 바로 보이지 않는데, 이를 위해서는 다음 정리가 필요하다. 

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> (Hilbert Nullstellensatz) $$\mathbb{K}$$가 대수적으로 닫힌 체이고 $$I \subseteq \mathbb{K}[\x_1, \ldots, \x_n]$$이 ideal이라 하자. 그럼

$$I(V(I)) = \sqrt{I}$$

이다. 여기서 $$\sqrt{I}$$는 $$I$$의 radical이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[가환대수학\] §영점정리, ⁋명제 6](/ko/math/commutative_algebra/nullstellensatz#prop6)

</details>

즉, closure operator $$IV$$는 ideal을 받아 이 아이디얼의 radical ideal을 주는 함수이다. 이로부터 $$\mathbb{K}[\x_1,\ldots, \x_n]$$의 radical ideal들과 $$\mathbb{A}^n$$의 closed set들 사이의 Galois correspondence가 존재함을 안다. 

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> 다음이 성립한다.

1. $$V(I) = \emptyset$$인 것과 $$I = (1)$$인 것이 동치이다.
2. $$V(I) = V(J)$$인 것과 $$\sqrt{I} = \sqrt{J}$$인 것이 동치이다. 

</div>

## Coordinate Ring

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 아핀다양체 $$X = V(I) \subseteq \mathbb{A}^n$$의 *coordinate ring<sub>좌표환</sub>* $$\mathbb{K}[X]$$를

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n] / I(X)$$

으로 정의한다. 이 원소들을 $$X$$ 위의 *regular function*이라 부른다.

</div>

Coordinate ring $$\mathbb{K}[X]$$의 원소들은 $$X$$ 위에서 정의된 함수들로 생각할 수 있다. 구체적으로, 각 $$\bar{f} \in \mathbb{K}[X]$$는 함수 $$X \to \mathbb{K}$$, $$a \mapsto f(a)$$로 생각할 수 있다. 이것이 well-defined인 이유는 $$f, g \in \mathbb{K}[\x_1, \ldots, \x_n]$$가 $$\mathbb{K}[X]$$에서 같은 원소를 나타낸다면 $$f - g \in I(X)$$이고, 따라서 $$f - g$$는 $$X$$ 위에서 identically zero이기 때문이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> [예시 3](#ex3)에서 살펴본 affine variety들의 경우, ideal들 $$(\x^2+\y^2-1)$$ 그리고 $$(\y-\x^2,\z-\x^3)$$은 radical임을 보일 수 있다. 따라서 단위원 $$X = V(\x^2+\y^2-1)$$의 coordinate ring은 $$\mathbb{K}[X] = \mathbb{K}[\x, \y]/(\x^2+\y^2-1)$$이고 twisted cubic $$C$$의 coordinate ring은 $$\mathbb{K}[C] = \mathbb{K}[\x, \y, \z]/(\y-\x^2, \z-\x^3) \cong \mathbb{K}[t]$$이다.

그러나 일반적으로 초곡면 $$V(f)$$의 coordinate ring은 $$\mathbb{K}[V(f)] = \mathbb{K}[\x_1, \ldots, \x_n]/I(V(f)) = \mathbb{K}[\x_1, \ldots, \x_n]/\sqrt{(f)}$$이므로, coordinate ring을 계산할 때는 주어진 ideal이 radical인지를 판단하여야 한다.

</div>

## 아핀다양체 사이의 사상

Affine variety들은 다항식으로 정의되는 기하학적 대상들이므로, 이들 사이의 함수 또한 다항식으로 나타나는 것들이어야 함이 타당하다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 두 affine variety들 $$X \subseteq \mathbb{A}^n$$과 $$Y \subseteq \mathbb{A}^m$$ 사이의 *morphism<sub>사상</sub>* (또는 *regular map*)이란 함수 $$\varphi: X \to Y$$로서, 다항식 $$f_1, \ldots, f_m \in \mathbb{K}[\x_1, \ldots, \x_n]$$들이 존재하여

$$\varphi(a_1, \ldots, a_n) = (f_1(a), \ldots, f_m(a))$$

를 만족하는 것이다.

</div>

예를 들어, 우리는 [예시 3](#ex3)에서 twisted cubic이 $$t\mapsto (t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 대응됨을 보였는데, 위의 정의는 이것이 affine variety들 사이의 morphism이라는 것을 보여준다. 

직관적으로 $$\mathbb{K}[X]$$들은 $$X$$ 위에 정의된 함수이므로, 만일 morphism $$X\rightarrow Y$$가 주어졌다면 이 morphism과의 합성을 통해 $$Y$$의 regular function들을 $$X$$로 옮겨올 수 있을 것이다. 

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 구체적으로, $$\bar{g} \in \mathbb{K}[Y]$$에 대하여

$$\varphi^\ast(\bar{g}) = \overline{g \circ \varphi}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\varphi^\ast$$가 well-defined임을 보여야 한다. $$g, h \in \mathbb{K}[\y_1, \ldots, \y_m]$$가 $$Y$$ 위에서 같은 함수를 정의한다면, $$g - h \in I(Y)$$이다. $$\varphi(X) \subseteq Y$$이므로, 모든 $$a \in X$$에 대해

$$(g \circ \varphi)(a) - (h \circ \varphi)(a) = (g - h)(\varphi(a)) = 0$$

이다. 즉 $$g \circ \varphi - h \circ \varphi \in I(X)$$이고, 따라서 $$\overline{g \circ \varphi} = \overline{h \circ \varphi}$$이다.

이제 $$\varphi^\ast$$가 ring homomorphism임은 자명하다.

</details>

즉, morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 이는 $$X\mapsto \mathbb{K}[X]$$가 affine variety들의 category에서 $$\Ring$$으로의 contravariant functor임을 의미한다. 

한편 morphism의 개념을 정의했다면, 당연히 isomorphism의 개념이 존재한다. 

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Morphism $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 morphism인 것이다.

</div>

예를 들어, $$\mathbb{A}^1$$에서 twisted cubic $$C$$로의 morphism $$t\mapsto (t, t^2, t^3)$$은 isomorphism이다. 이는 $$(x,y,z)\mapsto x$$가 inverse를 정의하기 때문이다. 

위에서 살펴봤듯, $$X\mapsto \mathbb{K}[X]$$는 affine variety들의 category에서 $$\Ring$$으로의 contravariant functor를 정의하므로, isomorphic한 affine variety들은 isomorphic한 coordinate ring을 갖는 것이 자명하다. 다음 명제는 그 역도 성립함을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Morphism $$\varphi: X \to Y$$가 isomorphism일 필요충분조건은 $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$가 ring isomorphism인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

반대방향만 보이면 충분하다. $$\varphi^\ast$$가 isomorphism이라 하자. 그럼 $$\psi^\ast = (\varphi^\ast)^{-1}: \mathbb{K}[X] \to \mathbb{K}[Y]$$가 존재한다.

이제 $$\psi^\ast$$로부터 morphism $$\theta: Y \to X$$를 정의하자. 

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n]/I(X)$$

의 각 원소 $$\bar{\x}_i$$에 대하여, $$\psi^\ast(\bar{\x}_i) \in \mathbb{K}[Y]$$를 생각할 수 있다. 이를 $$\bar{g}_i$$라 적고, 이들의 어떠한 representative들 $$g_i$$들을 생각하자. 그럼 $$\theta: Y \to \mathbb{A}^n$$을 $$\theta(y) = (g_1(y), \ldots, g_n(y))$$으로 정의할 수 있으며, $$\mathbb{K}[Y]$$의 정의에 의해 이는 representative $$g_i$$의 선택에 의존하지 않는다. 이제 $$\psi^\ast$$가 well-defined이므로 $$\theta(Y) \subseteq X$$이고, 따라서 $$\theta: Y \to X$$는 morphism이다. 나머지 부분은 단순 계산이다.

</details>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.