---
title: "정칙사상"
excerpt: "Regular maps between quasi-projective varieties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/regular_maps
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Regular_Maps.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-13
weight: 4

---

[§준사영다양체](/ko/math/algebraic_geometry/quasi_projective_varieties)에서 우리는 affine variety와 projective variety를 모두 포함하는 quasi-projective variety의 개념을 정의했으며, 이에 대한 motivation 중 하나는 이들 quasi-projective variety들 사이의 morphism을 미분다양체 스타일로 affine-local하게 살펴볼 수 있다는 것이었다. 이번 글에서 우리는 regular function과 regular map을 정의하고, 이들이 기존 정의 [§아핀다양체, ⁋정의 10](/ko/math/algebraic_geometry/affine_varieties#def10) 및 [§사영다양체, ⁋정의 13](/ko/math/algebraic_geometry/projective_varieties#def13)와 맞아떨어짐을 보인다. 

## 정칙함수

[\[준사영다양체\]](/ko/math/algebraic_geometry/quasi_projective_varieties)에서 우리는 quasi-projective variety가 open affine cover를 갖는다는 것을 보았다. 이를 엄밀하게 보이자. 

Projective variety $$Y \subseteq \mathbb{P}^n$$가 주어졌다 하자. [\[사영다양체\] ⁋명제 10, 11](/ko/math/algebraic_geometry/projective_varieties#prop10)에 의하여 $$Y = \bigcup_{i=0}^n (Y \cap U_i)$$이고, 각 $$Y \cap U_i$$는 affine variety이다. 이제 quasi-projective variety $$X \subseteq Y$$의 각 점 $$p$$가 affine open neighborhood를 갖음을 보이자.

$$p \in X$$라 하면, $$p \in Y \cap U_i$$인 $$i$$가 존재한다. $$Y \cap U_i$$는 affine variety이고, $$X \cap U_i$$는 그 안에서 열린부분집합이다. Affine variety에서 열린부분집합은 principal open set들의 합집합으로 쓰이므로, $$p \in D(f) \subseteq X \cap U_i$$인 principal open set $$D(f)$$가 존재한다. Principal open set $$D(f)$$는 affine variety이므로 ([\[아핀다양체\] ⁋명제 6](/ko/math/algebraic_geometry/affine_varieties#prop6)), $$p$$의 affine open neighborhood를 얻는다. 따라서 모든 quasi-projective variety는 open affine cover를 갖는다.

이를 이용하여 quasi-projective variety 위의 함수를 국소적으로 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> quasi-projective variety $$X$$ 위의 함수 $$f: X \to \mathbb{K}$$가 *regular<sub>정칙</sub>*라는 것은 $$X$$의 open affine cover $$\{U_i\}$$가 존재하여, 각 $$i$$에 대해 restriction $$f\vert_{U_i} \in \mathcal{O}(U_i)$$인 것이다. $$X$$ 위의 모든 regular function들의 집합을 $$\mathcal{O}(X)$$ 또는 $$\mathcal{O}_X(X)$$로 표기한다.

</div>

이 정의는 미분다양체에서의 smooth function 정의와 비슷하다. 미분다양체에서 각 점 $$p$$의 열린근방이 $$\mathbb{R}^n$$과 동형인 chart $$\varphi: U \to \mathbb{R}^n$$을 갖고, 함수 $$f: M \to \mathbb{R}$$가 smooth인 것은 $$f \circ \varphi^{-1}: \mathbb{R}^n \to \mathbb{R}$$이 smooth함으로 정의된다. Quasi-projective variety의 경우, 각 점 $$p$$가 어떤 affine chart $$U_i$$에 속하고, 함수 $$f$$가 regular인 것은 이 affine chart에서 coordinate ring $$\mathcal{O}(U_i)$$의 원소로 표현됨으로 정의된다. 

Projective variety의 경우를 더 자세히 살펴보자. Affine chart $$U_0 = \{x_0 \ne 0\}$$에서 homogeneous polynomial $$F$$ of degree $$d$$는 dehomogenization $$F(1, \x_1, \ldots, \x_n)$$을 통해 $$\mathbb{A}^n$$ 위의 다항식이 된다. 마찬가지로, 같은 차수의 homogeneous polynomial들의 비율 $$F/G$$는 $$F(1, \x_1, \ldots, \x_n) / G(1, \x_1, \ldots, \x_n)$$으로 표현된다 (단, $$G$$는 $$U_0$$에서 vanish하지 않음). 이는 [\[사영다양체\] ⁋명제 11](/ko/math/algebraic_geometry/projective_varieties#prop11)의 dehomogenization 과정이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Regular function의 예시들을 살펴보자.

1. Affine variety $$X$$에서 $$\mathcal{O}(X) = \mathbb{K}[X]$$이다. 이는 [\[아핀다양체\] ⁋정의 8](/ko/math/algebraic_geometry/affine_varieties#def8)에서 coordinate ring의 원소들을 regular function이라 부른 것과 일치한다. Coordinate ring의 원소 $$f$$는 $$X$$ 자체가 affine cover이므로 정의 1의 조건을 만족한다.
2. $$\mathbb{P}^n$$에서 $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$$이다. Standard open cover $$U_i = \{x_i \ne 0\}$$를 생각하자. $$U_0$$에서의 regular function은 $$\mathbb{K}[\x_1/\x_0, \ldots, \x_n/\x_0]$$의 원소이고, $$U_1$$에서의 regular function은 $$\mathbb{K}[\x_0/\x_1, \x_2/\x_1, \ldots, \x_n/\x_1]$$의 원소이다. 이들의 교집합 $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}[\x_0/\x_1] \cap \mathbb{K}[\x_1/\x_0] = \mathbb{K}$$이다. 이는 projective space에서 상수함수만이 전역적으로 정의됨을 보여준다.
3. $$\mathbb{A}^2 \setminus \{(0,0)\}$$에서 $$\mathcal{O}(X) = \mathbb{K}[\x, \y]$$이다. 이는 [명제 3](#prop3)에서 일반적으로 증명할 것이다. 직관적으로, 여차원 2 이상의 닫힌집합을 제거하면 regular function이 변하지 않는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Arapura Lemma 3.2.1) Affine variety $$X$$에서, 함수 $$f: X \to \mathbb{K}$$가 정의 1의 의미에서 regular인 것은 [\[아핀다양체\] ⁋정의 8](/ko/math/algebraic_geometry/affine_varieties#def8)의 의미에서 regular (즉, $$\mathbb{K}[X]$$의 원소)인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f \in \mathbb{K}[X]$$이면 자명하게 정의 1의 조건을 만족한다 ($$X$$ 자체가 affine cover). 

반대로 $$f$$가 정의 1의 의미에서 regular라 하자. Open affine cover $$\{U_i\}$$가 존재하여 각 $$f\vert_{U_i} \in \mathcal{O}(U_i)$$이다. $$X$$가 Noetherian이므로 유한개의 $$U_1, \ldots, U_r$$만으로 $$X$$를 덮을 수 있다. 각 $$U_i$$는 principal open set $$D(g_i) = \{g_i \ne 0\}$$의 형태이고, $$f\vert_{U_i} = h_i / g_i^{n_i}$$ for some $$h_i \in \mathbb{K}[X]$$. $$n_i = 1$$이라 가정하자 (필요하면 $$g_i$$를 $$g_i^{n_i}$$로 대체).

$$\bigcup_i D(g_i) = X$$이므로, ideal $$(g_1, \ldots, g_r) = \mathbb{K}[X]$$이다. 따라서 $$a_1 g_1 + \cdots + a_r g_r = 1$$ for some $$a_i \in \mathbb{K}[X]$$이다. 그럼

$$f = \sum_{i=1}^r a_i g_i f = \sum_{i=1}^r a_i g_i \cdot \frac{h_i}{g_i} = \sum_{i=1}^r a_i h_i \in \mathbb{K}[X]$$

이다.

</details>

## 정칙사상의 정의

Regular function을 정의했으니, 이제 quasi-projective variety 사이의 사상을 정의할 수 있다. 여기서 핵심 아이디어는 사상이 regular function을 "보존"해야 한다는 점이다. 즉, 사상의 pullback이 regular function을 얻어야 한다는 것이다. 이는 category theory에서 functor의 의미와 비슷하다. 사상은 다양체를 하나에서 다른 곳으로 보내지만, 동시에 coordinate ring을 다른 ring으로 보내는 것이므로, natural하게 regular function들을 pullback한다고 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> quasi-projective variety $$X, Y$$ 사이의 *regular map<sub>정칙사상</sub>* (또는 *morphism*) $$\varphi: X \to Y$$는 다음 조건을 만족하는 함수이다:

$$Y$$의 임의의 열린부분집합 $$V$$와 regular function $$f \in \mathcal{O}(V)$$에 대해, $$f \circ \varphi: \varphi^{-1}(V) \to \mathbb{K}$$는 regular function이다.

</div>

즉, regular map은 regular function을 pullback하는 함수이다. 이 정의는 추상적이지만, 다음 명제에서 보듯 아핀 및 사영 경우의 구체적인 정의와 일치한다. 이 정의는 또한 coordinate ring homomorphism과 호환되므로, functoriality가 자연스럽게 보장된다. 이는 아주 중요한 정의이므로, 다양한 관점에서 이해해야 한다. 한편으로, 이 정의는 "다항식 사상"을 formalize한 것이고, 다른 한편으로는 coordinate ring의 homomorphism과 대응한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> affine variety와 사영다양체의 경우, 위 정의는 이전의 morphism 정의와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**affine variety의 경우**: [§아핀다양체, ⁋명제 11](/ko/math/algebraic_geometry/affine_varieties#prop11)에서 morphism $$\varphi: X \to Y$$가 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도함을 보였다. 이는 $$\varphi^\ast(\bar{g}) = \overline{g \circ \varphi}$$로 정의되므로, $$\varphi$$가 regular function을 pullback한다는 것과 같다. 즉, coordinate ring의 원소 $$\bar{g}$$가 regular function $$g$$일 때, $$\varphi^\ast(\bar{g})$$는 $$g \circ \varphi$$가 된다. 따라서 affine variety의 morphism은 정의 3의 regular map과 일치한다.

**사영다양체의 경우**: [§사영다양체, ⁋정의 13](/ko/math/algebraic_geometry/projective_varieties#def13)에서 morphism을 homogeneous polynomials로 표현되는 함수로 정의했다. 구체적으로, $$\varphi(p) = [F_0(p) : \cdots : F_m(p)]$$ where $$F_i$$ are homogeneous of the same degree. Regular function $$f$$ on $$V \subseteq Y$$는 국소적으로 다항식의 비율로 표현되므로, $$f \circ \varphi$$ 또한 다항식의 비율로 표현된다. 따라서 $$f \circ \varphi$$는 regular function이다. 이는 projective variety의 morphism이 regular map 조건을 만족함을 보여준다.

</details>

## 정칙사상의 기본 성질

Regular map의 가장 기본적인 성질은 연속성이다. 이는 regular map이 "기하학적"이라는 것을 보여준다. 즉, 다양체 위의 위상구조와 natural하게 연결된다. 이는 regular map을 단순히 함수가 아니라 "geometric map"으로 볼 수 있게 한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Regular map $$\varphi: X \to Y$$는 연속함수이다. (Zariski 위상에서)

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$Z \subseteq Y$$가 닫힌집합이라면, $$Z$$는 $$Y$$의 어떤 열린덮개 $$\{V_\alpha\}$$에서 각 $$V_\alpha$$마다 regular function들 $$f_{\alpha,1}, \ldots, f_{\alpha,k_\alpha}$$이 존재하여

$$Z \cap V_\alpha = \{y \in V_\alpha \mid f_{\alpha,1}(y) = \cdots = f_{\alpha,k_\alpha}(y) = 0\}$$

이다. 그럼

$$\varphi^{-1}(Z) \cap \varphi^{-1}(V_\alpha) = \{x \in \varphi^{-1}(V_\alpha) \mid f_{\alpha,1}(\varphi(x)) = \cdots = f_{\alpha,k_\alpha}(\varphi(x)) = 0\}$$

이다. $$\varphi$$가 regular map이므로 각 $$f_{\alpha,i} \circ \varphi$$는 $$\varphi^{-1}(V_\alpha)$$에서 regular function이다. 따라서 $$\varphi^{-1}(Z) \cap \varphi^{-1}(V_\alpha)$$는 $$\varphi^{-1}(V_\alpha)$$의 닫힌집합이고, $$\{\varphi^{-1}(V_\alpha)\}$$가 $$X$$의 열린덮개이므로 $$\varphi^{-1}(Z)$$는 $$X$$의 닫힌집합이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Regular map의 합성은 regular map이다. 항등사상은 regular map이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi: X \to Y$$, $$\psi: Y \to Z$$가 regular map이라 하자. $$W \subseteq Z$$가 열린집합이고 $$f \in \mathcal{O}(W)$$라면, $$\psi$$가 regular이므로 $$f \circ \psi \in \mathcal{O}(\psi^{-1}(W))$$이다. 이제 $$\varphi$$가 regular이므로 $$(f \circ \psi) \circ \varphi \in \mathcal{O}(\varphi^{-1}(\psi^{-1}(W)))$$이다. 즉,

$$f \circ (\psi \circ \varphi) \in \mathcal{O}((\psi \circ \varphi)^{-1}(W))$$

이므로 $$\psi \circ \varphi$$는 regular map이다. 합성 연산이 associative하기 때문에, regular map들과 합성 연산에 의해 quasi-projective variety들의 category를 형성한다.

항등사상 $$\text{id}_X: X \to X$$의 경우, $$f \circ \text{id}_X = f$$이므로 자명하게 regular map이다. 이는 category의 axioms를 만족한다.

</details>

따라서 quasi-projective variety들과 regular map들은 category를 이룬다. 이 category에서의 isomorphism을 정의할 수 있다. 이는 category theory의 기본적인 개념이지만, 기하학적으로 중요한 의미를 갖는다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Regular map $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 regular map인 것이다.

</div>

Isomorphism의 개념은 기하학적으로 두 다양체가 "같은 구조"를 갖는다는 것을 의미한다. 즉, isomorphic한 다양체들은 regular function의 관점에서 구별할 수 없다. 이는 category theory의 isomorphism과 같지만, geometric interpretation이 추가된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 닫힌집합으로의 regular map의 제한은 regular map이다. 열린집합으로의 regular map의 제한도 regular map이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi: X \to Y$$가 regular map이고 $$Z \subseteq Y$$가 닫힌집합이라 하자. $$\psi = \varphi\vert_{\varphi^{-1}(Z)}: \varphi^{-1}(Z) \to Z$$를 생각하자. $$f$$가 $$Z$$의 열린집합 $$V$$에서 regular function이라면, $$f$$는 $$Y$$의 어떤 열린집합 $$V' \supseteq V$$로 확장되어 regular function이 된다 (적어도 국소적으로). 그럼 $$f \circ \psi = (f \circ \varphi)\vert_{\varphi^{-1}(Z)}$$이고, $$f \circ \varphi$$는 $$\varphi^{-1}(V')$$에서 regular이므로 그 제한도 regular이다.

열린집합의 경우는 더 간단하다. $$U \subseteq Y$$가 열린집합이면, $$f$$가 $$V \subseteq U$$에서 regular이면 $$f \circ \varphi$$는 $$\varphi^{-1}(V)$$에서 regular이다. 이는 open set이 regular function들의 local algebra라고 생각하면 자명하다.

</details>

## 정칙사상의 예시들

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **Projection**: $$\mathbb{A}^2 \to \mathbb{A}^1$$, $$(x, y) \mapsto x$$는 regular map이다. 이는 좌표함수 $$x$$가 $$\mathbb{K}[\x,\y]$$의 원소이므로 자명하다. 더 일반적으로, $$\mathbb{A}^n \to \mathbb{A}^m$$, $$(x_1, \ldots, x_n) \mapsto (f_1, \ldots, f_m)$$는 각 $$f_i$$가 다항식일 때 regular map이다. 이는 coordinate functions가 regular map을 정의하는 기본적인 도구임을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Inclusion**: $$\mathbb{A}^1 \hookrightarrow \mathbb{P}^1$$, $$t \mapsto [t : 1]$$는 regular map이다. 이는 $$\mathbb{P}^1$$의 standard affine open set $$U_1 = \{[x : y] \mid y \ne 0\}$$에 $$\mathbb{A}^1$$이 포함되고, $$U_1 \cong \mathbb{A}^1$$이기 때문이다. 일반적으로, quasi-projective variety의 열린부분집합으로의 inclusion은 regular map이다. 이는 projective space가 affine space가 아님에도 불구하고, projective space 안에 affine charts가 존재함을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Veronese embedding**: $$\mathbb{P}^n \to \mathbb{P}^N$$, $$[x_0 : \cdots : x_n] \mapsto [\cdots : x_i x_j : \cdots]$$는 regular map이다. 여기서 $$N = \binom{n+2}{2} - 1$$이고, 좌표들은 모든 2차 단항식 $$x_i x_j$$ ($$0 \le i \le j \le n$$)을 순서대로 나열한 것이다. 이 사상은 $$\mathbb{P}^n$$을 $$\mathbb{P}^N$$의 projective variety로 embedding하며, 그 image는 *Veronese variety*라 불린다. 예를 들어 $$n=1$$일 때, $$\mathbb{P}^1 \to \mathbb{P}^2$$, $$[x : y] \mapsto [x^2 : xy : y^2]$$는 image가 conic $$V(\x_0 \x_2 - \x_1^2)$$인 isomorphism을 정의한다. 이는 smooth conic이 projective line과 isomorphic함을 보여준다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **Isomorphism들의 예시**:

1. $$\mathbb{A}^1 \to V(\y - \x^2) \subset \mathbb{A}^2$$, $$t \mapsto (t, t^2)$$는 isomorphism이다. 역사상은 $$(x, y) \mapsto x$$로 주어진다. 기하학적으로, 이는 parabola가 직선과 isomorphic함을 보여준다. 이는 projective case에서 conic이 $$\mathbb{P}^1$$과 isomorphic함과 유사한 idea이다.
2. $$\mathbb{P}^1 \to V(\x_0 \x_2 - \x_1^2) \subset \mathbb{P}^2$$, $$[x : y] \mapsto [x^2 : xy : y^2]$$는 isomorphism이다. 이는 Veronese embedding의 $$n=1$$ 경우이며, smooth conic이 $$\mathbb{P}^1$$과 isomorphic함을 보여준다. 이 예시는 projective geometry에서의 powerful fact를 보여준다.
3. $$\mathbb{A}^1 \setminus \{0\} \to V(\x\y - 1) \subset \mathbb{A}^2$$, $$t \mapsto (t, 1/t)$$는 isomorphism이다. 역사상은 $$(x, y) \mapsto x$$로 주어진다. 이는 hyperbola가 원점을 제외한 직선과 isomorphic함을 보여준다. 이 예시는 affine case에서도 isomorphism이 발생함을 보여준다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
