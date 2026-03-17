---
title: "준사영다양체"
excerpt: "Quasi-projective varieties and regular maps"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/quasi_projective_varieties
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Quasi_Projective_Varieties.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-17
weight: 3

---

[§아핀다양체](/ko/math/algebraic_geometry/affine_varieties)와 [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 우리는 각각 아핀공간과 사영공간의 부분집합으로 정의되는 기하적 대상들을 살펴보았다. 그러나 대수기하학에서 가장 자연스러운 대상들은 이 둘을 모두 포함하는 더 큰 범주에 속한다. 이 절에서 우리는 *quasi-projective variety*를 정의하고, 이것이 affine variety와 projective variety를 모두 포함함을 보인다.

## Quasi-projective variety의 정의

Projective space의 열린집합은 자연스러운 기하적 대상이다. 예를 들어, $$\mathbb{P}^2$$에서 직선 $$\x_0=0$$을 제거한 standard affine cover $$U_0$$은 projective variety가 아니지만, 여전히 다항식으로 정의되는 대상이며, 심지어 affine variety이기도 하다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Projective variety $$Y \subseteq \mathbb{P}^n$$의 열린부분집합 $$X \subseteq Y$$를 *quasi-projective variety<sub>준사영다양체</sub>*라 부른다.

</div>

물론 $$X$$는 $$Y$$의 위상구조를 물려받는다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Standard affine open set $$U_i = \{x_i \ne 0\}$$는 $$\mathbb{P}^n$$의 열린부분집합이므로 quasi-projective variety이다. [§사영다양체, ⁋명제 9](/ko/math/algebraic_geometry/projective_varieties#prop9)에서 $$U_i \cong \mathbb{A}^n$$이므로, 모든 affine variety는 quasi-projective variety이다. 또 임의의 projective variety는 당연히 quasi-projective variety이다. 

</div>

일반적으로, affine case에서와 projective case 모두에서 주어진 variety의 open subset은 affine variety 혹은 projective variety가 되지 않는 경우가 더 많았다. Quasi-projective variety는 이들보다 훨씬 넓은 범주로, 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Quasi-projective variety $$X$$의 열린집합은 quasi-projective variety이다. 또, $$X$$의 irreducible closed subset도 quasi-projective variety이다.

</div>

여기서 irreducible space는 더 작은 두 개의 열린집합의 합집합으로 나타낼 수 없는 공간을 의미한다. 

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 projective variety $$Y\subset \mathbb{P}^n$$의 열린집합이라 하자.

1. **열린집합의 경우**: $$X$$의 열린집합 $$U$$는 $$Y$$의 열린집합이므로, 정의에 의해 quasi-projective variety이다.

2. **닫힌집합의 경우**: $$X$$의 닫힌집합 $$Z$$가 irreducible이라 하자. 그럼 적당한 $$\mathbb{P}^n$$의 닫힌집합 $$W$$가 존재하여 $$Z=X\cap W$$이다. 이때 $$Y \cap W$$는 $$\mathbb{P}^n$$의 닫힌집합이고, $$Z$$는 $$Y \cap W$$의 열린부분집합이다. 

   $$Z$$가 irreducible이므로, $$Z$$를 포함하는 $$Y \cap W$$의 irreducible component $$W'$$가 존재한다. 그럼 $$Z$$는 projective variety $$W'$$의 열린부분집합이므로 quasi-projective variety이다.

</details>

## 자리스키 위상

Quasi-projective variety $$X \subseteq Y \subseteq \mathbb{P}^n$$에는 $$Y$$로부터 물려받는 subspace topology가 존재한다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Quasi-projective variety $$X$$의 *Zariski topology*은 projective variety $$Y$$의 위상을 $$X$$로 제한한 것이다. 즉, $$X$$의 닫힌집합들은 projective variety $$Z\subset Y\subset\mathbb{P}^n$$에 대하여 $$X \cap Z$$의 꼴이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Zariski topology는 실제로 위상이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Zariski 위상이 위상의 공리를 만족함을 확인하자.

- 공집합과 전체집합: $$X \cap \emptyset = \emptyset$$, $$X \cap Y = X$$이므로 둘 다 $$X$$의 닫힌집합이다.
- 유한 교집합: $$X$$의 닫힌집합 $$Z_1, \ldots, Z_r$$이 $$Z_i = X \cap W_i$$ ($$W_i$$는 projective)로 표현된다면,

$$Z_1 \cap \cdots \cap Z_r = X \cap (W_1 \cap \cdots \cap W_r)$$

이고 $$W_1 \cap \cdots \cap W_r$$은 projective variety이므로 교집합도 닫힌집합이다.
- 임의의 합집합: $$Z_\alpha = X \cap W_\alpha$$들이 $$X$$의 닫힌집합들이라면,

$$\bigcup_\alpha Z_\alpha = X \cap \left(\bigcup_\alpha W_\alpha\right)$$

이고 $$\bigcup_\alpha W_\alpha$$는 projective variety들의 합집합으로, Zariski 위상에서 닫힌집합이다.

따라서 Zariski topology는 위상이다.

</details>

## Open Affine Cover

우리는 variety들 사이의 morphism을 다룰 때 미분다양체 등에서 하였듯 한 점 주변의 (affine) 열린근방을 찾아 계산을 수행할 것이다. 이를 위해 quasi-projective variety가 open affine cover를 갖는다는 것을 보이자. Open affine cover는 regular map의 국소적 성질을 분석하고, sheaf의 stalk을 정의하며, scheme으로의 일반화를 이해하는 데 필수적이다.

Projective variety $$Y \subseteq \mathbb{P}^n$$와 그 안의 quasi-projective variety $$X \subseteq Y$$가 주어졌다 하자. Standard affine open set $$U_i = \{x_i \ne 0\} \subseteq \mathbb{P}^n$$를 생각하자. Dehomogenization $$\x_j / \x_i$$를 통해 $$U_i \cong \mathbb{A}^n$$이고, $$Y \cap U_i$$는 $$\mathbb{A}^n$$ 안의 affine variety와 isomorphic하다. 따라서

$$Y = \bigcup_{i=0}^n (Y \cap U_i)$$

으로 적으면 각 $$Y \cap U_i$$는 affine variety이다. 따라서

$$X = \bigcup_{i=0}^n (X \cap U_i)$$

에서, 각 $$X \cap U_i$$는 affine variety $$Y \cap U_i$$의 열린부분집합이다. 이제 [§아핀다양체, ⁋명제 6](/ko/math/algebraic_geometry/affine_varieties#prop6)에 의하여 affine variety의 임의의 열린집합은 principal open set들의 합집합으로 표현되며, [§아핀다양체, ⁋명제 7](/ko/math/algebraic_geometry/affine_varieties#prop7)에 의하여 이들은 각각 affine이므로 $$X$$는 open affine cover를 갖는다.

## 정칙함수

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Quasi-projective variety $$X$$ 위의 함수 $$f: X \rightarrow \mathbb{K}$$가 *regular<sub>정칙</sub>*라는 것은 $$X$$의 open affine cover $$\{U_i\}$$가 존재하여, 각 $$i$$에 대해 restriction 

$$f\vert_{U_i}:U_i\rightarrow\mathbb{K}$$

가 affine variety $$U_i$$의 coordinate ring $$\mathbb{K}[U_i]$$의 원소인 것이다. $$X$$ 위의 모든 regular function들의 sheaf를 $$\mathscr{O}_X$$ 혹은 더 간단히 $$\mathscr{O}$$로 표기한다. 이 정의는 [§아핀다양체, ⁋정의 11](/ko/math/algebraic_geometry/affine_varieties#def11)에서 affine case를 포괄하며, projective variety 또한 quasi-projective이므로 이 정의가 적용된다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1))

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Regular function의 예시들을 살펴보자.

1. Affine variety $$X$$에서 $$\mathcal{O}(X) = \mathbb{K}[X]$$이다. 이는 [§아핀다양체, ⁋정의 11](/ko/math/algebraic_geometry/affine_varieties#def11)에서 coordinate ring의 원소들을 regular function이라 부른 것과 일치한다. Coordinate ring의 원소 $$f$$는 $$X$$ 자체가 affine cover이므로 정의 6의 조건을 만족한다.
2. $$\mathbb{P}^n$$에서 $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$$이다. Standard open cover $$U_i = \{x_i \ne 0\}$$를 생각하자. $$U_0$$에서의 regular function은 $$\mathbb{K}[\x_1/\x_0, \ldots, \x_n/\x_0]$$의 원소이고, $$U_1$$에서의 regular function은 $$\mathbb{K}[\x_0/\x_1, \x_2/\x_1, \ldots, \x_n/\x_1]$$의 원소이다. 이들의 교집합 $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}[\x_0/\x_1] \cap \mathbb{K}[\x_1/\x_0] = \mathbb{K}$$이다. 이는 projective space에서 상수함수만이 전역적으로 정의됨을 보여준다.
3. $$\mathbb{A}^2 \setminus \{(0,0)\}$$에서 $$\mathcal{O}(X) = \mathbb{K}[\x, \y]$$이다. 이는 [명제 8](#prop8)에서 일반적으로 증명할 것이다. 직관적으로, 여차원 2 이상의 닫힌집합을 제거하면 regular function이 변하지 않는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Affine variety $$X$$에서, 함수 $$f: X \to \mathbb{K}$$가 regular인 것은 [§아핀다양체, ⁋정의 11](/ko/math/algebraic_geometry/affine_varieties#def11)의 의미에서 regular (즉, $$\mathbb{K}[X]$$의 원소)인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f \in \mathbb{K}[X]$$이면 자명하게 [정의 6](#def6)의 조건을 만족한다 ($$X$$ 자체가 affine cover).

반대로 $$f$$가 [정의 6](#def6)의 의미에서 regular라 하자. 즉 open affine cover $$\{U_i\}$$가 존재하여 각 $$f\vert_{U_i} \in \mathcal{O}(U_i)$$이다. $$X$$가 Zariski 위상에서 quasi-compact이므로 (모든 affine variety는 Noetherian이고 따라서 quasi-compact), 유한개의 $$U_1, \ldots, U_r$$만으로 $$X$$를 덮을 수 있다. 각 $$U_i$$는 principal open set $$D(g_i) = \{g_i \ne 0\}$$의 형태이고, 따라서

$$f\vert_{U_i} = h_i / g_i^{n_i}$$

의 형태로 쓸 수 있다. 어차피 $$D(g_i)=D(g_i^{n_i})$$이므로, 편의상 $$f\vert_{U_i}=h_i/g_i$$라 하자.

이제 $$\bigcup_i D(g_i) = X$$이다. 이는 각 점 $$p \in X$$에 대해 어떤 $$g_i$$가 $$g_i(p) \ne 0$$임을 의미한다. 즉, ideal $$I = (g_1, \ldots, g_r) \subseteq \mathbb{K}[X]$$의 vanishing locus가 공집합이다. Hilbert Nullstellensatz에 의해 $$\sqrt{I} = \mathbb{K}[X]$$이고, 특히 $$1 \in I$$이다. 따라서 $$a_1 g_1 + \cdots + a_r g_r = 1$$을 만족하는 $$a_i \in \mathbb{K}[X]$$가 존재한다. 그럼

$$f = \sum_{i=1}^r a_i g_i f = \sum_{i=1}^r a_i g_i \cdot \frac{h_i}{g_i} = \sum_{i=1}^r a_i h_i \in \mathbb{K}[X]$$

이므로 증명이 완료된다.

</details>

Projective case에 대해서는 약간의 분석이 필요하다. Affine chart $$U_0 = \{x_0 \ne 0\}$$에서 homogeneous polynomial $$F$$ of degree $$d$$는 dehomogenization $$F(1, \x_1, \ldots, \x_n)$$을 통해 $$\mathbb{A}^n$$ 위의 다항식이 된다. 마찬가지로, 같은 차수의 homogeneous polynomial들의 비율 $$F/G$$는 $$F(1, \x_1, \ldots, \x_n) / G(1, \x_1, \ldots, \x_n)$$으로 표현된다 (단, $$G$$는 $$U_0$$에서 vanish하지 않음). 이는 [§사영다양체, ⁋명제 10](/ko/math/algebraic_geometry/projective_varieties#prop10)의 dehomogenization 과정이다.

## 정칙사상의 정의

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Quasi-projective variety $$X \subseteq \mathbb{P}^n$$과 $$Y \subseteq \mathbb{P}^m$$ 사이의 *morphism<sub>사상</sub>* (또는 *regular map<sub>정칙사상</sub>*) $$\varphi: X \to Y$$는 각 점 $$p \in X$$에 대해 다음을 만족하는 함수이다:

$$p$$의 적당한 열린근방 $$U \subseteq X$$와 homogeneous polynomials $$F_0, \ldots, F_m$$ of the same degree가 존재하여

$$\varphi(q) = [F_0(q) : \cdots : F_m(q)]$$

이 모든 $$q \in U$$에 대해 성립하고, $$F_i(q)$$들이 동시에 $$0$$이 아니다.

</div>

이 정의는 국소적으로 projective variety의 morphism과 같은 꼴이라는 것을 의미한다. 다음 명제는 이 정의가 regular function의 관점에서 자연스럽게 해석됨을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 함수 $$\varphi: X \to Y$$가 morphism인 필요충분조건은 $$Y$$의 임의의 열린부분집합 $$V$$와 regular function $$f \in \mathcal{O}(V)$$에 대해, $$f \circ \varphi: \varphi^{-1}(V) \to \mathbb{K}$$가 regular function인 것이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

생략. 핵심은 morphism이 국소적으로 homogeneous polynomials로 표현되므로, regular function (국소적으로 다항식의 비율)의 pullback도 다항식의 비율로 표현된다는 것이다. 구체적으로, $$f = F/G$$가 같은 차수의 homogeneous polynomials의 비율로 표현된다면, $$f \circ \varphi$$는 $$F(\varphi(x))/G(\varphi(x))$$로 표현되며, 이는 다항식들의 pullback의 비율이므로 여전히 다항식의 비율이다.

</details>

이 명제는 regular map이 regular function을 regular function으로 pullback한다는 것을 의미한다. 이 정의는 추상적이지만, coordinate ring homomorphism과 호환되므로 functoriality가 자연스럽게 보장된다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Affine variety와 projective variety의 경우, [정의 9](#def9)는 [§아핀다양체, ⁋정의 14](/ko/math/algebraic_geometry/affine_varieties#def14), [§사영다양체, ⁋정의 15](/ko/math/algebraic_geometry/projective_varieties#def15)와 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

**아핀다양체의 경우**: [§아핀다양체, ⁋명제 15](/ko/math/algebraic_geometry/affine_varieties#prop15)에서 morphism $$\varphi: X \to Y$$가 coordinate ring homomorphism $$\varphi^\ast: \mathbb{K}[Y] \to \mathbb{K}[X]$$를 유도함을 보였다. 이는 $$\varphi^\ast(\bar{g}) = \overline{g \circ \varphi}$$로 정의되므로, $$\varphi$$가 regular function을 pullback한다는 것과 같다. 즉, coordinate ring의 원소 $$\bar{g}$$가 regular function $$g$$일 때, $$\varphi^\ast(\bar{g})$$는 $$g \circ \varphi$$가 된다. 따라서 affine variety의 morphism은 정의 9의 regular map과 일치한다.

**사영다양체의 경우**: [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 morphism을 homogeneous polynomials로 표현되는 함수로 정의했다. 구체적으로, $$\varphi(p) = [F_0(p) : \cdots : F_m(p)]$$ where $$F_i$$ are homogeneous of the same degree. Regular function $$f$$ on $$V \subseteq Y$$는 국소적으로 다항식의 비율로 표현되므로, $$f \circ \varphi$$ 또한 다항식의 비율로 표현된다. 따라서 $$f \circ \varphi$$는 regular function이다. 이는 projective variety의 morphism이 regular map 조건을 만족함을 보여준다.

</details>

## 정칙사상의 기본 성질

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Regular map $$\varphi: X \to Y$$는 연속함수이다. (Zariski 위상에서)

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

<ins id="prop13">**명제 13**</ins> Regular map의 합성은 regular map이다. 항등사상은 regular map이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi: X \to Y$$, $$\psi: Y \to Z$$가 regular map이라 하자. $$W \subseteq Z$$가 열린집합이고 $$f \in \mathcal{O}(W)$$라면, $$\psi$$가 regular이므로 $$f \circ \psi \in \mathcal{O}(\psi^{-1}(W))$$이다. 이제 $$\varphi$$가 regular이므로 $$(f \circ \psi) \circ \varphi \in \mathcal{O}(\varphi^{-1}(\psi^{-1}(W)))$$이다. 즉,

$$f \circ (\psi \circ \varphi) \in \mathcal{O}((\psi \circ \varphi)^{-1}(W))$$

이므로 $$\psi \circ \varphi$$는 regular map이다.

항등사상 $$\text{id}_X: X \to X$$의 경우, $$f \circ \text{id}_X = f$$이므로 자명하게 regular map이다.

</details>

따라서 quasi-projective variety들과 regular map들은 category를 이룬다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> 닫힌집합으로의 regular map의 제한은 regular map이다. 열린집합으로의 regular map의 제한도 regular map이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi: X \to Y$$가 regular map이고 $$Z \subseteq Y$$가 닫힌집합이라 하자. $$\psi = \varphi\vert_{\varphi^{-1}(Z)}: \varphi^{-1}(Z) \to Z$$를 생각하자. $$f$$가 $$Z$$의 열린집합 $$V$$에서 regular function이라면, $$f$$는 $$Y$$의 어떤 열린집합 $$V' \supseteq V$$로 확장되어 regular function이 된다 (적어도 국소적으로). 그럼 $$f \circ \psi = (f \circ \varphi)\vert_{\varphi^{-1}(Z)}$$이고, $$f \circ \varphi$$는 $$\varphi^{-1}(V')$$에서 regular이므로 그 제한도 regular이다.

열린집합의 경우는 더 간단하다. $$U \subseteq Y$$가 열린집합이면, $$f$$가 $$V \subseteq U$$에서 regular이면 $$f \circ \varphi$$는 $$\varphi^{-1}(V)$$에서 regular이다.

</details>

## 동형사상

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Morphism $$\varphi: X \to Y$$가 *isomorphism<sub>동형사상</sub>*이라는 것은 역함수 $$\psi: Y \to X$$가 존재하여 $$\psi$$도 morphism인 것이다.

</div>

Isomorphism의 개념은 기하학적으로 두 다양체가 "같은 구조"를 갖는다는 것을 의미한다. 즉, isomorphic한 다양체들은 regular function의 관점에서 구별할 수 없다.

## 예시들

<div class="example" markdown="1">

<ins id="ex16">**예시 16**</ins> Projective variety와 affine variety들을 엮어주는 함수들이 새로운 것들이다. 가령 canonical surjection

$$\mathbb{A}^{n+1}\setminus\{(0,\ldots, 0)\}\rightarrow \mathbb{P}^n;\qquad (x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

은 quasi-projective variety들 사이의 morphism이다. 

</div>

<div class="example" markdown="1">

<ins id="ex17">**예시 17**</ins> **Projection, Inclusion, Veronese Embedding, Isomorphisms**:

1. **Projection**: $$\mathbb{A}^2 \to \mathbb{A}^1$$, $$(x, y) \mapsto x$$는 regular map이다. 이는 좌표함수 $$x$$가 $$\mathbb{K}[\x,\y]$$의 원소이므로 자명하다. 더 일반적으로, $$\mathbb{A}^n \to \mathbb{A}^m$$, $$(x_1, \ldots, x_n) \mapsto (f_1, \ldots, f_m)$$는 각 $$f_i$$가 다항식일 때 regular map이다.

2. **Inclusion**: $$\mathbb{A}^1 \hookrightarrow \mathbb{P}^1$$, $$t \mapsto [t : 1]$$는 regular map이다. 이는 $$\mathbb{P}^1$$의 standard affine open set $$U_1 = \{[x : y] \mid y \ne 0\}$$에 $$\mathbb{A}^1$$이 포함되고, $$U_1 \cong \mathbb{A}^1$$이기 때문이다. 일반적으로, quasi-projective variety의 열린부분집합으로의 inclusion은 regular map이다.

3. **Veronese embedding**: $$\mathbb{P}^n \to \mathbb{P}^N$$, $$[x_0 : \cdots : x_n] \mapsto [\cdots : x_i x_j : \cdots]$$는 regular map이다. 여기서 $$N = \binom{n+2}{2} - 1$$이고, 좌표들은 모든 2차 단항식 $$x_i x_j$$ ($$0 \le i \le j \le n$$)을 순서대로 나열한 것이다. 이 사상은 $$\mathbb{P}^n$$을 $$\mathbb{P}^N$$의 projective variety로 embedding하며, 그 image는 *Veronese variety*라 불린다. 예를 들어 $$n=1$$일 때, $$\mathbb{P}^1 \to \mathbb{P}^2$$, $$[x : y] \mapsto [x^2 : xy : y^2]$$는 image가 conic $$V(\x_0 \x_2 - \x_1^2)$$인 isomorphism을 정의한다.

4. **Isomorphisms**:
   - $$\mathbb{A}^1 \to V(\y - \x^2) \subset \mathbb{A}^2$$, $$t \mapsto (t, t^2)$$는 isomorphism이다. 역사상은 $$(x, y) \mapsto x$$로 주어진다.
   - $$\mathbb{P}^1 \to V(\x_0 \x_2 - \x_1^2) \subset \mathbb{P}^2$$, $$[x : y] \mapsto [x^2 : xy : y^2]$$는 isomorphism이다.
   - $$\mathbb{A}^1 \setminus \{0\} \to V(\x\y - 1) \subset \mathbb{A}^2$$, $$t \mapsto (t, 1/t)$$는 isomorphism이다.

</div>

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
