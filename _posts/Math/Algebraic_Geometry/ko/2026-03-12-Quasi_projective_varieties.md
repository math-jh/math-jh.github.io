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

[§아핀다양체](/ko/math/algebraic_geometry/affine_varieties)와 [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 우리는 각각 아핀공간과 사영공간의 부분집합으로 정의되는 기하적 대상들을 살펴보았다. 그러나 대수기하학에서 가장 자연스러운 대상들은 이 둘을 모두 포함하는 더 큰 범주에 속한다. 이 절에서 우리는 *quasi-projective variety*를 정의하고, 이것이 affine variety와 projective variety를 모두 포함함을 보인다. 또 quasi-projective variety들 사이의 morphism을 정의하고 이들이 기존의 개념들과 맞아떨어짐을 보인다. 

## Quasi-projective variety의 정의

Projective space의 열린집합은 자연스러운 기하적 대상이다. 예를 들어, $$\mathbb{P}^2$$에서 직선 $$\x_0=0$$을 제거한 standard affine cover $$U_0$$은 projective variety가 아니지만, 여전히 다항식으로 정의되는 대상이며, 심지어 affine variety이기도 하다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Projective variety $$Y \subseteq \mathbb{P}^n$$의 열린부분집합 $$X \subseteq Y$$를 *quasi-projective variety<sub>준사영다양체</sub>*라 부른다.

</div>

물론 $$X$$는 $$Y$$의 위상구조를 물려받으며, 이러한 위상 또한 *Zariski topology*라 부른다. 정의에 의하여 quasi-projective variety는 projective variety들을 모두 포함하는 개념임이 자명하다. 우리의 첫 번째 명제는 임의의 affine variety가 quasi-projective라는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 affine variety는 quasi-projective variety이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 affine variety $$X\subseteq \mathbb{A}^n$$이 주어졌다 하자. 우리는 다음의 embedding

$$i:\mathbb{A}^n\rightarrow \mathbb{P}^n;\qquad (x_1,\ldots, x_n)\mapsto [1:x_1:\cdots:x_n]$$

이 존재함을 이미 알고 있다. ([§사영다양체, ⁋명제 9](/ko/math/algebraic_geometry/projective_varieties#prop9)) 이제 $$X$$의 $$\mathbb{P}^n$$에서의 image $$i(X)$$를 생각하고, $$i(X)$$의 $$\mathbb{P}^n$$에서의 closure $$\overline{i(X)}$$를 생각하자. 그럼 $$\overline{i(X)}$$는 projective variety이며, 이 안에서 $$X$$는

$$X=\overline{i(X)}\cap U_0$$

으로 나타나므로 열린집합이다. 이로부터 증명이 완료된다. 

</details>

위의 증명을 뜯어보면, 어렵지 않게 quasi-projective variety에서 정의한 Zariski topology가 기존 affine variety에서 정의한 Zariski topology와 맞아 떨어지는 것을 알고, projective variety의 경우에도 마찬가지이다. 

일반적으로, affine case에서와 projective case 모두에서 주어진 variety의 open subset은 affine variety 혹은 projective variety가 되지 않는 경우가 더 많았다. Quasi-projective variety는 이들보다 훨씬 넓은 범주로, 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Quasi-projective variety $$X$$의 열린집합은 quasi-projective variety이다. 또, $$X$$의 irreducible closed subset도 quasi-projective variety이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 projective variety $$Y\subset \mathbb{P}^n$$의 열린집합이라 하자. $$X$$의 열린집합은 $$Y$$의 열린집합이기도 하므로 $$X$$의 임의의 열린집합이 quasi-projective variety임은 자명하다. 따라서 $$X$$의 임의의 irreducible closed set이 quasi-projective임을 보이면 충분하다. 이를 위해

$$X=Y\cap U,\qquad \text{$U$ open in $\mathbb{P}^n$}$$

이라 하고, $$X$$의 임의의 irreducible closed set $$Z$$가 주어졌다 하자. 그럼 $$\mathbb{P}^n$$의 적당한 irreducible closed subset $$W$$이 존재하여

$$Z=X\cap W=(Y\cap U)\cap W=(Y\cap W)\cap U$$

이다. 이로부터 $$Z$$는 projective variety $$Y\cap W$$의 열린집합이다. 

</details>

## 정칙함수와 정칙사상

지금부터 별다른 언급이 없다면 variety는 항상 quasi-projective variety를 의미하는 것으로 생각하자. 우리의 기하학적 직관은 variety $$X$$의 임의의 점은 항상 affine open neighborhood를 갖는다는 것이다. 이는 affine case와 projective case 각각에서는 이미 증명하였으므로, 이를 quasi-projective case에 대해 확장하기만 하면 된다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 variety $$X$$와 임의의 $$x\in X$$에 대하여, affine variety들로 이루어진 $$X$$의 covering이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$X$$가 quasi-projective이므로, 적당한 projective variety $$Y\subset \mathbb{P}^n$$이 존재하여 $$X$$가 $$Y$$의 열린집합이도록 할 수 있다. 이제 $$X$$는 standard affine chart들을 사용하여 $$X\cap U_i$$들로 덮을 수 있고, 이 때 각각의 $$X\cap U_i$$들은 affine variety $$Y\cap U_i$$의 열린집합이다. ([§사영다양체, ⁋명제 10](/ko/math/algebraic_geometry/projective_varieties#prop10)) 이제 [§아핀다양체, ⁋명제 6](/ko/math/algebraic_geometry/affine_varieties#prop6)에 의해 affine variety의 임의의 열린집합은 principal open set으로 덮을 수 있으며, 이들은 [§아핀다양체, ⁋명제 7](/ko/math/algebraic_geometry/affine_varieties#prop7)에 의해 affine이므로 증명이 완료된다. 

</details>

이제 위의 명제에 의해, 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Quasi-projective variety $$X$$ 위의 함수 $$f: X \rightarrow \mathbb{K}$$가 *regular<sub>정칙</sub>*라는 것은 $$X$$의 open affine cover $$\{U_i\}$$가 존재하여, 각 $$i$$에 대해 restriction 

$$f\vert_{U_i}:U_i\rightarrow\mathbb{K}$$

가 affine variety $$U_i$$의 coordinate ring $$\mathbb{K}[U_i]$$의 원소인 것이다. $$X$$ 위의 모든 regular function들의 sheaf를 $$\mathscr{O}_X$$ 혹은 더 간단히 $$\mathscr{O}$$로 표기한다. ([\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1))

</div>

그럼 다음은 regular function의 예시들이다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Regular function의 예시들을 살펴보자.

1. Affine variety $$X$$에서 $$\mathcal{O}(X) = \mathbb{K}[X]$$이다. 
2. $$\mathbb{P}^n$$에서 $$\mathcal{O}(\mathbb{P}^n) = \mathbb{K}$$이다. 이를 확인하기 위해 standard open cover $$U_i = \{x_i \ne 0\}$$를 생각하자. 특히 $$U_0$$에서의 regular function은 $$\mathbb{K}[\x_1/\x_0, \ldots, \x_n/\x_0]$$의 원소이고, $$U_1$$에서의 regular function은 $$\mathbb{K}[\x_0/\x_1, \x_2/\x_1, \ldots, \x_n/\x_1]$$의 원소이다. 따라서 만일 어떠한 함수 $$f$$가 $$\mathbb{P}^n$$ 전체에서 regular라면, 이 함수는 $$U_0$$에서는 $$\mathrm{s}_i=\x_i/\x_0$$들에 대한 다항식이고 $$U_1$$에서는 $$\mathrm{t}_i=\x_i/\x_1$$에 대한 다항식이다. 그런데 $$U_0\cap U_1$$에서, 우리는 이들 좌표함수들이 다음 식  
    
    $$\mathrm{t}_0=\frac{1}{\mathrm{s}_1},\qquad \mathrm{t}_j=\frac{\mathrm{s}_j}{\mathrm{s}_1}$$

    을 만족하는 것을 안다. 따라서 만일

    $$f\vert_{U_0}=p(\mathrm{s}_1, \ldots, \mathrm{s}_n),\qquad f\vert_{U_1}=q(\mathrm{t}_0,\mathrm{t}_2,\ldots, \mathrm{t}_n)$$

    이라 하면 이들이 $$U_0\cap U_1$$에서 같은 함수를 정의해야 한다는 것과 위의 식에 의하여

    $$p(\mathrm{s}_1,\ldots, \mathrm{s}_n)=q\left(\frac{1}{\mathrm{s}_1},\frac{\mathrm{s}_2}{\mathrm{s}_1}, \ldots,\frac{\mathrm{s}_n}{\mathrm{s}_1}\right)$$

    이 성립해야 하는 것을 안다. 이제 우변의 식이 다항식이 되기 위해서는 반드시 $$q$$가 상수함수가 되어 분모의 $$\mathrm{s}_1$$들이 없어져야 하고 이로부터 $$p$$와 $$q$$는 상수함수여야 함을 안다. 비슷하게 모든 chart $$U_i,U_j$$에 대해서도 같은 논리를 적용하면 원하는 결과를 얻는다. 

</div>

이제 우리는 variety들 사이의 morphism, 즉 regular map을 정의한다. 

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

$$\varphi: X \to Y$$가 regular map이고 $$Z \subseteq Y$$가 닫힌집합이라 하자. $$\psi = \varphi\vert_{\varphi^{-1}(Z)}: \varphi^{-1}(Z) \to Z$$를 생각하자. $$f$$가 $$Z$$의 열린집합 $$V$$에서 regular function이라면, $$f$$는 $$Y$$의 어떤 열린집합 $$V' \supseteq V$$로 확장되어 regular function이 된다 (적어도 국소적으로). 구체적으로, $$V$$를 $$Z$$의 open affine cover로 교차하여 각 조각에서 regular function을 정의하면, 이들을 정칙적으로 이어붙여 $$Y$$의 열린근방 $$V'$$에서의 regular function을 얻을 수 있다. 이는 정칙함수가 본질적으로 유리함수의 국소적 표현이므로, affine chart 위에서의 정의가 Zariski 개방 덮개의 교집합에서도 일관되게 합쳐지기 때문이다. 그럼 $$f \circ \psi = (f \circ \varphi)\vert_{\varphi^{-1}(Z)}$$이고, $$f \circ \varphi$$는 $$\varphi^{-1}(V')$$에서 regular이므로 그 제한도 regular이다.

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
