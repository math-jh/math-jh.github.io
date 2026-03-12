---
title: "유리사상"
excerpt: "Rational maps and birational equivalence"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/rational_maps
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Rational_Maps.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-13
weight: 5

---

[§정칙사상](/ko/math/algebraic_geometry/regular_maps)에서 우리는 준사영다양체 사이의 "다항식 사상"인 regular map을 정의했다. Regular map은 모든 점에서 정의되는 함수이므로, 이론적으로 깔끔하지만 실제로는 제약이 많다. 예를 들어, $$(x, y) \mapsto [x : y]$$는 원점에서 정의되지 않는다. 그러나 이 함수는 원점을 제외한 모든 점에서 잘 정의되며, 기하학적으로 매우 자연스러운 함수이다. 이 절에서 우리는 "대부분의 점에서" 정의되는 함수인 *유리사상*을 연구하고, 이를 통해 두 다양체가 "대부분 같은" 구조를 갖는지를 판별하는 *쌍유리동치*의 개념을 도입한다.

## 유리함수

Regular function이 모든 점에서 다항식으로 표현되는 함수라면, rational function은 "대부분의 점에서" 다항식의 비율로 표현되는 함수이다. 이는 마치 복소해석학에서 meromorphic function이 holomorphic function의 비율로 표현되는 것과 비슷하다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 준사영다양체 $$X$$ 위의 *rational function<sub>유리함수</sub>*란 $$X$$의 어떤 비어있지 않은 열린부분집합 $$U$$에서 정의된 regular function $$f: U \to \mathbb{K}$$를 말한다. 두 rational function $$f: U \to \mathbb{K}$$와 $$g: V \to \mathbb{K}$$는 $$U \cap V$$에서 일치할 때 같은 것으로 본다.

</div>

$$X$$ 위의 모든 rational function들의 집합을 $$\mathbb{K}(X)$$로 표기한다. 두 rational function의 합과 곱은 정의되는 영역의 교집합에서 정의되며, 0이 아닌 rational function의 역은 그 함수가 0이 아닌 점들에서 정의된다. 따라서 $$\mathbb{K}(X)$$는 field를 이룬다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 기약 아핀다양체 $$X$$에 대해 $$\mathbb{K}(X)$$는 coordinate ring $$\mathbb{K}[X]$$의 fraction field와 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{K}[X]$$의 원소는 $$X$$ 전체에서 정의되는 regular function이고, $$\mathbb{K}(X)$$의 원소는 $$X$$의 어떤 열린부분집합에서 정의되는 regular function이다.

먼저 $$\text{Frac}(\mathbb{K}[X]) \subseteq \mathbb{K}(X)$$임을 보이자. $$f/g \in \text{Frac}(\mathbb{K}[X])$$라면, $$g \ne 0$$이므로 $$X \setminus V(g)$$는 비어있지 않은 열린집합이다. $$f/g$$는 이 열린집합에서 정의되는 regular function이므로 $$\mathbb{K}(X)$$의 원소이다.

이제 $$\mathbb{K}(X) \subseteq \text{Frac}(\mathbb{K}[X])$$임을 보이자. $$h \in \mathbb{K}(X)$$라면, $$h$$는 어떤 열린집합 $$U$$에서 정의된다. 기약다양체에서 열린집합은 dense하므로, $$U$$는 principal open set들 $$X \setminus V(g_i)$$의 합집합으로 쓰일 수 있다. 각 $$X \setminus V(g_i)$$에서 $$h = f_i/g_i$$로 표현되고, $$X$$가 기약이므로 모든 $$f_i/g_i$$는 $$\text{Frac}(\mathbb{K}[X])$$에서 같은 원소를 나타낸다.

</details>

이 명제는 기약 아핀다양체의 경우, rational function을 coordinate ring의 원소들의 비율 $$f/g$$로 구체적으로 표현할 수 있음을 보여준다. 여기서 $$g \ne 0$$이면 $$f/g$$는 $$X \setminus V(g)$$에서 정의된다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Rational function field의 예시들을 살펴보자.

1. $$\mathbb{K}(\mathbb{A}^n) = \mathbb{K}(x_1, \ldots, x_n)$$이다. 이는 $$n$$변수 rational function field이며, $$x_i$$들은 $$\mathbb{A}^n$$의 좌표함수들이다. 예를 들어 $$x_1/x_2$$는 $$\{x_2 \ne 0\}$$에서 정의되는 rational function이다.
2. $$\mathbb{K}(\mathbb{P}^n) = \mathbb{K}(x_1/x_0, \ldots, x_n/x_0) \cong \mathbb{K}(t_1, \ldots, t_n)$$이다. 이는 $$\mathbb{P}^n$$의 rational function이 $$U_0 = \{x_0 \ne 0\} \cong \mathbb{A}^n$$에서의 rational function과 같음을 의미한다. 예를 들어 $$x_1/x_0$$은 $$U_0$$에서 첫 번째 좌표함수이다.
3. $$\mathbb{K}(V(\y - \x^2)) = \mathbb{K}(x)$$이다. Parabola $$V(\y - \x^2)$$의 coordinate ring은 $$\mathbb{K}[\x,\y]/(\y-\x^2) \cong \mathbb{K}[x]$$이고, 그 fraction field는 $$\mathbb{K}(x)$$이다. 기하학적으로, 이는 parabola가 직선과 birationally equivalent함을 시사한다.

</div>

## 유리사상의 정의

Rational function이 "대부분의 점에서" 정의되는 $$\mathbb{K}$$-값 함수라면, rational map은 "대부분의 점에서" 정의되는 다양체 사이의 함수이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 기약 준사영다양체 $$X, Y$$ 사이의 *rational map<sub>유리사상</sub>*이란 $$X$$의 어떤 비어있지 않은 열린부분집합 $$U$$에서 정의된 regular map $$\varphi: U \to Y$$를 말한다. 두 rational map $$\varphi: U \to Y$$와 $$\psi: V \to Y$$는 $$U \cap V$$에서 일치할 때 같은 것으로 본다.

</div>

Rational map은 보통 $$\varphi: X \dashrightarrow Y$$로 표기하며, 점선은 "모든 점에서 정의되지 않을 수 있음"을 나타낸다. 정의되지 않는 점들을 *base points*라 부른다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Rational map $$\varphi: X \dashrightarrow Y$$는 정의되는 점들의 집합 $$\text{dom}(\varphi)$$를 갖는다. 이는 $$X$$의 열린부분집합이며, $$\varphi$$는 $$\text{dom}(\varphi)$$ 전체에서 정의된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi$$가 $$U_1, U_2$$에서 각각 regular map으로 정의되고 $$U_1 \cap U_2 \ne \emptyset$$에서 일치한다면, $$\varphi$$는 $$U_1 \cup U_2$$에서 정의된다. 따라서 $$\varphi$$가 정의되는 모든 열린집합들의 합집합 $$\text{dom}(\varphi)$$에서 $$\varphi$$는 well-defined이다. 열린집합들의 합집합은 열린집합이므로 $$\text{dom}(\varphi)$$는 $$X$$의 열린부분집합이다.

</details>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **Projection from a point**: $$\mathbb{P}^2 \dashrightarrow \mathbb{P}^1$$, $$[x : y : z] \mapsto [x : y]$$는 rational map이다. 이 map은 $$[0 : 0 : 1]$$에서 정의되지 않는다. 기하학적으로, 이는 $$[0 : 0 : 1]$$에서 $$\mathbb{P}^2$$의 점들을 $$\mathbb{P}^1$$으로 투영하는 것이다. 직선 $$\{[0 : 0 : z]\}$$ 위의 모든 점이 $$[0 : 0 : 1]$$으로 "축소"되므로, 이 점에서 map이 정의되지 않는다. Domain은 $$\mathbb{P}^2 \setminus \{[0 : 0 : 1]\}$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$\mathbb{A}^2 \dashrightarrow \mathbb{P}^1$$, $$(x, y) \mapsto [x : y]$$는 rational map이다. 이 map은 원점 $$(0, 0)$$에서 정의되지 않는다. 기하학적으로, 이는 원점에서 $$\mathbb{A}^2$$의 점들의 "방향"을 $$\mathbb{P}^1$$으로 보내는 것이다. 원점에서는 방향이 정의되지 않으므로 base point가 된다. Domain은 $$\mathbb{A}^2 \setminus \{(0, 0)\}$$이다.

</div>

## 쌍유리동치

Regular map의 isomorphism이 두 다양체가 "완전히 같은" 구조를 갖는다는 것을 의미한다면, birational equivalence는 두 다양체가 "대부분 같은" 구조를 갖는다는 것을 의미한다. 이는 대수기하학에서 매우 중요한 개념이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Rational map $$\varphi: X \dashrightarrow Y$$가 *birational map*이라는 것은 역 rational map $$\psi: Y \dashrightarrow X$$가 존재하여 $$\psi \circ \varphi = \text{id}_X$$와 $$\varphi \circ \psi = \text{id}_Y$$가 (정의되는 곳에서) 성립하는 것이다. 두 다양체 $$X, Y$$가 *birationally equivalent*라는 것은 둘 사이에 birational map이 존재하는 것이다.

</div>

Birationally equivalent한 두 다양체는 "대부분의 점에서" isomorphic하다. 구체적으로, 다음 명제에서 보듯 두 다양체의 isomorphic한 열린부분집합들이 존재한다.

<div class="theorem" markdown="1">

<ins id="thm9">**정리 9**</ins> 기약 다양체 $$X, Y$$에 대하여 다음이 동치이다.

1. $$X$$와 $$Y$$는 birationally equivalent하다.
2. $$\mathbb{K}(X) \cong \mathbb{K}(Y)$$ (as fields)
3. $$X$$와 $$Y$$의 isomorphic한 비어있지 않은 열린부분집합들이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**(1) $$\Rightarrow$$ (2)**: Birational map $$\varphi: X \dashrightarrow Y$$는 $$\text{dom}(\varphi) \subseteq X$$에서 정의된다. $$\varphi$$가 regular이므로, pullback $$\varphi^\ast: \mathbb{K}(Y) \to \mathbb{K}(\text{dom}(\varphi))$$가 존재한다. $$\mathbb{K}(\text{dom}(\varphi)) = \mathbb{K}(X)$$이고 (기역다양체에서 열린집합의 rational function은 전체와 같음), $$\varphi$$가 birational이므로 $$\varphi^\ast$$는 field isomorphism이다.

**(2) $$\Rightarrow$$ (3)**: Field isomorphism $$\mathbb{K}(X) \cong \mathbb{K}(Y)$$를 생각하자. 이는 rational map $$\varphi: X \dashrightarrow Y$$를 정의한다. $$\varphi$$의 domain을 $$U$$라 하고, $$\varphi^{-1}$$의 domain을 $$V$$라 하자. 그럼 $$\varphi: U \cap \varphi^{-1}(V) \to V \cap \varphi(U)$$는 isomorphism이다.

**(3) $$\Rightarrow$$ (1)**: $$U \subseteq X$$와 $$V \subseteq Y$$가 isomorphic하다면, isomorphism $$\varphi: U \to V$$를 rational map $$X \dashrightarrow Y$$로 볼 수 있다. 그 inverse 또한 rational map이므로 birational map이다.

</details>

이 정리는 birational equivalence를 판별하는 세 가지 방법을 제공한다. 특히 (2)는 함수체를 계산함으로써 birational equivalence를 판별할 수 있음을 보여준다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **Quadric surface와 $$\mathbb{P}^1 \times \mathbb{P}^1$$**: $$\mathbb{P}^1 \times \mathbb{P}^1$$과 $$V(\x\y - \z\w) \subset \mathbb{P}^3$$은 birationally equivalent하다. 둘 다 rational function field $$\mathbb{K}(t_1, t_2)$$를 갖기 때문이다. 사실 이 둘은 isomorphic하다. Segre embedding $$\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$, $$([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$$의 image가 정확히 $$V(\x\y - \z\w)$$이다.

</div>

## Blow-up과 유리사상

Blow-up은 birational geometry에서 가장 중요한 연산 중 하나이다. 이는 다양체의 특이점을 "해소"하거나 다양체의 구조를 단순화하는 데 사용된다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Blow-up of $$\mathbb{A}^2$$ at origin**: 

$$\text{Bl}_0 \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

이 집합은 $$\mathbb{A}^2 \times \mathbb{P}^1$$의 닫힌부분다양체이다. 조건 $$xv = yu$$는 점 $$(x, y)$$와 직선 $$[u : v]$$이 "같은 방향"에 있음을 의미한다. 즉, 원점이 아닌 점 $$(x, y)$$에 대해서는 유일한 직선 $$[x : y]$$이 존재하고, 원점 $$(0, 0)$$에 대해서는 모든 직선 $$[u : v]$$가 가능하다.

Projection $$\pi: \text{Bl}_0 \mathbb{A}^2 \to \mathbb{A}^2$$를 $$\pi((x, y), [u : v]) = (x, y)$$로 정의하자. 그럼:

- $$\pi$$는 원점이 아닌 모든 점에서 isomorphism이다. 구체적으로, $$(x, y) \ne (0, 0)$$이면 $$\pi^{-1}(x, y) = \{((x, y), [x : y])\}$$이다.
- 원점 위의 fiber는 $$\pi^{-1}(0, 0) = \{((0, 0), [u : v]) \mid [u : v] \in \mathbb{P}^1\} \cong \mathbb{P}^1$$이다. 이를 *exceptional divisor*라 부른다.

따라서 $$\pi$$는 birational map이다. 기하학적으로, blow-up은 원점을 "폭발"시켜 원점을 지나는 모든 직선들의 공간 $$\mathbb{P}^1$$으로 대체한다.

</div>

Blow-up의 중요성은 다음과 같다:

1. **특이점 해소**: 많은 특이점들은 적절한 blow-up을 통해 매끄러운 다양체로 바뀐다.
2. **Birational map의 분해**: 임의의 birational map은 blow-up과 blow-down의 합성으로 분해될 수 있다 (weak factorization theorem).
3. **Minimal model program**: Birational classification의 핵심 도구이다.

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
