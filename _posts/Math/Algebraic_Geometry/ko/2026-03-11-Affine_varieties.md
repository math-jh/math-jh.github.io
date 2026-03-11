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

우리의 목표는 다항식으로 정의되는 기하적 대상들을 연구하는 것이다. 구체적으로, 체 $$\mathbb{K}$$와 자연수 $$n$$이 주어졌을 때, 우리는 다음의 식

$$V(f)= \{(a_1, \ldots, a_n) \in \mathbb{A}^n \mid f(a_1, \ldots, a_n) = 0\},\qquad f\in \mathbb{K}[\x_1,\ldots, \x_n]$$

으로 주어지는 집합들을 연구할 것이다. 일반적으로 $$\mathbb{K}=\mathbb{C}$$로 두지만, 대부분의 경우 이렇게 가정하는 것이 큰 도움이 되지는 않으므로 우리는 더 일반적인 세팅을 사용하기로 한다.

## 아핀다양체의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 체 $$\mathbb{K}$$ 위에 정의된 *affine $n$-space<sub>$n$차원 아핀공간</sub>* $$\mathbb{A}^n_\mathbb{K}$$는 $$n$$차원 벡터공간 $$\mathbb{K}^n$$을 의미한다.

</div>

체 $$\mathbb{K}$$를 생략해도 될 때는 $$\mathbb{A}^n$$과 같이 적는다. 우리는 affine space

$$\mathbb{A}^n=\{(a_1,\ldots, a_n)\mid a_i\in \mathbb{K}\}$$

의 원소를 *점<sub>point</sub>*이라 부르고, 각각의 좌표 $$a_i$$를 *$i$번째 좌표*라 부른다. 우리가 살펴볼 기하적인 대상들은 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$의 zero set $$V(f)$$로 나타나는 대상들이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 다항식 $$f_1, \ldots, f_k \in \mathbb{K}[\x_1, \ldots, \x_n]$$에 대하여, 이들이 정의하는 *affine variety<sub>아핀다양체</sub>* $$V(f_1, \ldots, f_k)$$를

$$V(f_1, \ldots, f_k) = \{(a_1, \ldots, a_n) \in \mathbb{A}^n \mid f_1(a) = \cdots = f_k(a) = 0\}$$

으로 정의한다.

</div>

즉, 아핀다양체는 여러 다항식들 $$f_1,\ldots, f_k$$의 공통 zero set이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 우리가 아는 대다수의 기하학적인 대상들은 다항식으로 나타나므로, 이들이 모두 affine variety의 예시가 된다.

1. $$\mathbb{A}^2$$ 안에서 정의된 affine variety $$V(\x^2+\y^2-1)$$을 생각하자. 정의에 의해, 이 집합은 식 $$\x^2+\y^2-1=0$$을 만족하는 $$\mathbb{A}^2$$의 점들의 모임이므로, 단위원을 나타낸다.
2. 일반적으로, 임의의 affine space $$\mathbb{A}^n$$와 임의의 다항식 $$f\in \mathbb{K}[\x_1,\ldots, \x_n]$$에 대하여, $$V(f)$$는 *초곡면<sub>hypersurface</sub>*을 정의한다.
3. 또 다른 중요한 예시로, $$\mathbb{A}^3$$ 위에 정의된 *twisted cubic*이 있다. 이는 $$\mathbb{A}^3$$ 위에 정의된 두 다항식 $$\y-\x^2$$, $$\z-\x^3$$으로 정의되는 곡선으로, 매개화 $$(t,t^2,t^3)$$을 통해 $$\mathbb{A}^1$$과 일대일로 대응된다.
4. Affine space $$\mathbb{A}^n$$ 자기자신과 공집합은 affine variety이다. 이는 $$V(0)=\mathbb{A}^n$$, $$V(1)=\emptyset$$으로부터 자명하다.

</div>

## 자리스키 위상

[예시 3](#ex3)에서 우리는 친숙한 기하학적 대상들이 모두 집합으로서는 affine variety로 쓰여질 수 있음을 보았다. 그러나 이를 기하학적 대상이라 생각하기 위해서는 그 위에 위상구조가 존재해야 한다. 우리의 유일한 도구는 다항식이므로, 이를 사용하여 위상구조를 정의할 것이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음이 성립한다.

1. $$V(0) = \mathbb{A}^n$$
2. $$V(1) = \emptyset$$
3. $$I \subseteq J \implies V(J) \subseteq V(I)$$
4. $$\displaystyle\bigcap_{\alpha} V(I_\alpha) = V\left(\sum_\alpha I_\alpha\right)$$
5. $$V(I) \cup V(J) = V(I \cap J) = V(IJ)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$V(0) = \mathbb{A}^n$$: 영다항식은 모든 점에서 0이므로 자명하다.
2. $$V(1) = \emptyset$$: 상수다항식 1은 모든 점에서 1이므로 자명하다.
3. $$I \subseteq J \implies V(J) \subseteq V(I)$$: 만약 $$p \in V(J)$$라면, 모든 $$f \in J$$에 대해 $$f(p) = 0$$이다. $$I \subseteq J$$이므로 모든 $$g \in I$$에 대해서도 $$g(p) = 0$$이다. 즉 $$p \in V(I)$$이다.
4. $$\bigcap_\alpha V(I_\alpha) = V(\sum_\alpha I_\alpha)$$: 점 $$p$$가 모든 $$V(I_\alpha)$$에 속한다는 것은 모든 $$\alpha$$와 모든 $$f \in I_\alpha$$에 대해 $$f(p) = 0$$이라는 것이다. 이는 $$\sum_\alpha I_\alpha$$의 모든 원소가 $$p$$에서 0이라는 것과 동치이다.
5. $$V(I) \cup V(J) = V(I \cap J) = V(IJ)$$: 먼저 $$V(I) \cup V(J) \subseteq V(I \cap J)$$를 보이자. $$p \in V(I) \cup V(J)$$라면 $$p \in V(I)$$이거나 $$p \in V(J)$$이다. 어느 경우이든 $$I \cap J$$의 모든 원소는 $$p$$에서 0이므로 $$p \in V(I \cap J)$$이다. 역으로, $$p \in V(I \cap J)$$라 하자. 만약 $$p \notin V(I)$$라면 어떤 $$f \in I$$가 존재하여 $$f(p) \neq 0$$이다. 그런데 $$IJ \subseteq I \cap J$$이므로 $$p \in V(I \cap J) \subseteq V(IJ)$$이고, 따라서 모든 $$g \in J$$에 대해 $$(fg)(p) = f(p)g(p) = 0$$이다. $$f(p) \neq 0$$이므로 $$g(p) = 0$$이고, 즉 $$p \in V(J)$$이다.

</details>

따라서 아핀다양체들을 닫힌집합으로 갖는 위상을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$\mathbb{A}^n$$의 *Zariski 위상<sub>Zariski topology</sub>*은 아핀다양체들을 닫힌집합으로 갖는 위상이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$\mathbb{A}^1$$에서 Zariski 위상은 *여유한 위상<sub>cofinite topology</sub>*이다. 닫힌집합들은 $$\mathbb{A}^1$$ 자신과 유한집합들뿐이다.

</div>

<div class="remark" markdown="1">

**참고 7** Zariski 위상은 하우스도르프가 아니다. 예를 들어 $$\mathbb{A}^1$$에서 서로 다른 두 점 $$a \neq b$$를 분리하는 열린집합이 존재하지 않는다.

</div>

## 다양체의 이데알

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 부분집합 $$X \subseteq \mathbb{A}^n$$의 *ideal<sub>이데알</sub>* $$I(X)$$를

$$I(X) = \{f \in \mathbb{K}[\x_1, \ldots, \x_n] \mid f(a) = 0 \text{ for all } a \in X\}$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 다음이 성립한다.

1. $$I(X)$$는 $$\mathbb{K}[\x_1, \ldots, \x_n]$$의 ideal이다.
2. $$X \subseteq Y \implies I(Y) \subseteq I(X)$$
3. $$I(\emptyset) = \mathbb{K}[\x_1, \ldots, \x_n]$$
4. $$I(\mathbb{A}^n) = (0)$$ ($$\mathbb{K}$$가 무한체일 때)
5. $$X \subseteq V(I(X))$$
6. $$I \subseteq I(V(I))$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. $$I(X)$$가 ideal임은 정의로부터 자명하다. $$f, g \in I(X)$$이고 $$h \in \mathbb{K}[\x_1, \ldots, \x_n]$$이면, 모든 $$a \in X$$에 대해 $$f(a) = g(a) = 0$$이므로 $$(f+g)(a) = 0$$이고 $$(hf)(a) = h(a)f(a) = 0$$이다.
2. $$X \subseteq Y$$이고 $$f \in I(Y)$$라면, 모든 $$a \in Y$$에 대해 $$f(a) = 0$$이다. 특히 모든 $$a \in X$$에 대해 $$f(a) = 0$$이므로 $$f \in I(X)$$이다.
3. 공집합의 조건을 만족하는 함수는 모든 다항식이다.
4. $$\mathbb{K}$$가 무한체이면, 모든 점에서 0인 다항식은 영다항식뿐이다.
5. $$a \in X$$이고 $$f \in I(X)$$라면 $$f(a) = 0$$이다. 즉 $$a \in V(I(X))$$이다.
6. $$f \in I$$이고 $$a \in V(I)$$라면 $$f(a) = 0$$이다. 즉 $$f \in I(V(I))$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins>

1. $$I(\{(a_1, \ldots, a_n)\}) = (\x_1 - a_1, \ldots, \x_n - a_n)$$이다. 한쪽 방향은 자명하고, 역방향은 다항식을 $$\x_i - a_i$$들로 나누어 생각하면 된다.
2. 일반적으로 $$I(V(f)) = \sqrt{(f)}$$이다. 이는 [정리 12](#thm12)의 특수한 경우이다.
3. Twisted cubic $$C$$에 대해 $$I(C) = (\y - \x^2, \z - \x^3)$$이다.

</div>

## Hilbert 영점 정리

<div class="theorem" markdown="1">

<ins id="thm11">**정리 11**</ins> (Hilbert Nullstellensatz) $$\mathbb{K}$$가 대수적으로 닫힌 체이고 $$I \subseteq \mathbb{K}[\x_1, \ldots, \x_n]$$이 ideal이라 하자. 그럼

$$I(V(I)) = \sqrt{I} = \{f \mid f^m \in I \text{ for some } m \ge 1\}$$

이다.

</div>

이 정리에 의해 아핀다양체의 ideal은 항상 *radical ideal*이다.

<div class="corollary" markdown="1">

<ins id="cor12">**따름정리 12**</ins> 다음이 성립한다.

1. $$V(I) = \emptyset \iff I = (1)$$
2. $$V(I) = V(J) \iff \sqrt{I} = \sqrt{J}$$

</div>

## 좌표환

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 아핀다양체 $$X = V(I) \subseteq \mathbb{A}^n$$의 *좌표환<sub>coordinate ring</sub>* $$\mathbb{K}[X]$$를

$$\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n] / I(X)$$

으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 좌표환 $$\mathbb{K}[X]$$의 원소들은 $$X$$ 위에서 정의된 "다항식 함수"들이다. 즉, 각 $$\bar{f} \in \mathbb{K}[X]$$는 함수 $$X \to \mathbb{K}$$, $$a \mapsto f(a)$$로 생각할 수 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f, g \in \mathbb{K}[\x_1, \ldots, \x_n]$$가 $$\mathbb{K}[X]$$에서 같은 원소를 나타낸다면, $$f - g \in I(X)$$이다. 즉, 모든 $$a \in X$$에 대해 $$(f-g)(a) = 0$$이고, 따라서 $$f(a) = g(a)$$이다. 그러므로 $$\bar{f}$$는 $$X$$ 위에서 well-defined 함수를 정의한다.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins>

1. $$\mathbb{K}[\mathbb{A}^n] = \mathbb{K}[x_1, \ldots, x_n]$$이다.
2. $$\mathbb{K}[V(x)] = \mathbb{K}[x, y]/(x) \cong \mathbb{K}[y]$$이다.
3. Twisted cubic $$C$$의 좌표환은 $$\mathbb{K}[C] = \mathbb{K}[x, y, z]/(y-x^2, z-x^3) \cong \mathbb{K}[t]$$이다.

</div>

## 정칙함수

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> 아핀다양체 $$X$$ 위의 *regular function<sub>정칙함수</sub>*란 좌표환 $$\mathbb{K}[X]$$의 원소를 말한다.

</div>

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> 단위원 $$X = V(x^2 + y^2 - 1)$$ 위에서:

- $$f(x, y) = x + y$$는 regular function이다.
- $$g(x, y) = \dfrac{x}{1+y}$$는 $$y \ne -1$$인 점에서만 정의된다. 이는 rational function이지만 $$X$$ 전체에서 정의되지 않으므로 regular function이 아니다.
- $$\mathbb{K}[X] = \mathbb{K}[x, y]/(x^2 + y^2 - 1)$$이다.

</div>

## 아핀다양체 사이의 사상

<div class="definition" markdown="1">

<ins id="def18">**정의 18**</ins> 아핀다양체 $$X \subseteq \mathbb{A}^n$$과 $$Y \subseteq \mathbb{A}^m$$ 사이의 *morphism<sub>사상</sub>* (또는 *regular map*)이란 함수 $$\varphi: X \to Y$$로서, 다항식 $$f_1, \ldots, f_m \in \mathbb{K}[x_1, \ldots, x_n]$$들이 존재하여

$$\varphi(a_1, \ldots, a_n) = (f_1(a), \ldots, f_m(a))$$

를 만족하는 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex19">**예시 19**</ins>

1. **매개화**: $$\mathbb{A}^1 \to \mathbb{A}^3$$, $$t \mapsto (t, t^2, t^3)$$은 twisted cubic으로의 morphism이다.
2. **투영**: $$\mathbb{A}^3 \to \mathbb{A}^2$$, $$(x, y, z) \mapsto (x, y)$$는 morphism이다.
3. **항등사상**: $$\operatorname{id}: X \to X$$는 morphism이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop20">**명제 20**</ins> Morphism $$\varphi: X \to Y$$는 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도한다. 구체적으로, $$\bar{g} \in \mathbb{K}[Y]$$에 대하여

$$\varphi^\ast(\bar{g}) = \overline{g \circ \varphi}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\varphi^\ast$$가 well-defined임을 보여야 한다. $$g, h \in \mathbb{K}[y_1, \ldots, y_m]$$가 $$Y$$ 위에서 같은 함수를 정의한다면, $$g - h \in I(Y)$$이다. $$\varphi(X) \subseteq Y$$이므로, 모든 $$a \in X$$에 대해

$$(g \circ \varphi)(a) - (h \circ \varphi)(a) = (g - h)(\varphi(a)) = 0$$

이다. 즉 $$g \circ \varphi - h \circ \varphi \in I(X)$$이고, 따라서 $$\overline{g \circ \varphi} = \overline{h \circ \varphi}$$이다.

이제 $$\varphi^\ast$$가 ring homomorphism임은 자명하다.

</details>

## 동형사상

<div class="definition" markdown="1">

<ins id="def21">**정의 21**</ins> Morphism $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 morphism인 것이다.

</div>

<div class="example" markdown="1">

<ins id="ex22">**예시 22**</ins>

1. **Twisted cubic과 $$\mathbb{A}^1$$**: $$\varphi: \mathbb{A}^1 \to C$$, $$t \mapsto (t, t^2, t^3)$$은 isomorphism이다.
   - 역함수: $$(x, y, z) \mapsto x$$
   - 좌표환: $$\mathbb{K}[C] \cong \mathbb{K}[t]$$

2. **포물선과 $$\mathbb{A}^1$$**: $$\varphi: \mathbb{A}^1 \to V(y - x^2)$$, $$t \mapsto (t, t^2)$$는 isomorphism이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop23">**명제 23**</ins> Morphism $$\varphi: X \to Y$$가 isomorphism일 필요충분조건은 $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$가 ring isomorphism인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

만약 $$\varphi$$가 isomorphism이고 그 역이 $$\psi$$라면, $$\varphi^\ast \circ \psi^\ast = (\psi \circ \varphi)^\ast = \operatorname{id}^\ast = \operatorname{id}$$이고, 마찬가지로 $$\psi^\ast \circ \varphi^\ast = \operatorname{id}$$이다. 따라서 $$\varphi^\ast$$는 isomorphism이다.

역으로, $$\varphi^\ast$$가 isomorphism이라 하자. 그럼 $$\varphi$$는 전단사함수이다. 만약 $$\varphi(a) = \varphi(b)$$라면, 모든 $$\bar{g} \in \mathbb{K}[Y]$$에 대해 $$g(\varphi(a)) = g(\varphi(b))$$이고, 이는 $$\varphi^\ast$$가 injective임과 모순된다. 또한 $$\varphi^\ast$$가 surjective이므로, $$\varphi$$의 역을 정의할 수 있다.

</details>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[Ful]** W. Fulton, *Algebraic Curves*, 2008. (Available online)
