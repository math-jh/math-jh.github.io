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
last_modified_at: 2026-03-15
weight: 5

---

[§준사영다양체, ⁋정의 7](/ko/math/algebraic_geometry/quasi_projective_varieties#def7)에서 우리는 준사영다양체 사이의 함수인 regular map을 정의하였다. 무엇보다 이는 정의역의 모든 점에서 정의되는 함수로, 설령 [§아핀다양체, ⁋정의 13](/ko/math/algebraic_geometry/affine_varieties#def13)와 같은 형태로 $$D(f)$$ 위에서 유리식 형태로 써 주더라도 그 분모에 들어갈 수 있는 것은 $$f$$의 거듭제곱꼴 뿐이기 때문에 모든 점에서 정의된다. 

그러나, 여전히 많은 종류의 함수들이 regular map이 아닌 형태로 주어진다. 예를 들어, $$(x, y) \mapsto [x : y]$$는 원점에서 정의되지 않으므로 regular map이 아니지만 충분히 자연스러운 함수처럼 보인다. 이 글에서 우리는 <em-ko>대부분의 점에서</em-ko> 정의되는 함수인 *유리사상*을 살펴본다. 

## 유리함수

Regular map을 정의할 때와 마찬가지로, 우리는 유리사상을 정의하기에 앞서 유리함수의 개념을 먼저 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위의 *rational function<sub>유리함수</sub>*는 $$X$$의 공집합이 아닌 열린집합 $$U$$와 그 위에서 정의된 regular funcction $$f:U \rightarrow \mathbb{K}$$의 pair $$(U,f)$$를 의미한다. 두 유리함수 $$(U,f)$$, $$(V,g)$$가 equivalent하다는 것은 이들이 $$U\cap V$$에서 일치하는 것이다. 

</div>

이에 대한 직관은 다음과 같다. Zariski topology 상에서 닫힌집합은 작고, 열린집합은 크다. 따라서 rational function은 작은 집합에서 정의되지 않지만, 나머지 대부분의 점에서는 정의되는 함수이다. 가령, 본질적으로 Zariski topology 상에서 열린집합은 $$D(g)$$ 꼴의 집합들이라 생각해도 되는데, 이 위에서 정의된 regular function $$f/g$$들을 이제 우리는 함수로 생각하는 것이다. ([§아핀다양체, ⁋정의 13](/ko/math/algebraic_geometry/affine_varieties#def13)) 물론 $$g$$가 $$0$$이 되는 점에서 이 함수는 정의되지 않겠지만, 정확히 그것이 우리가 열린집합 $$U$$에서 정의되는 함수들을 생각하는 이유이며, 어쨌든 $$g$$가 $$0$$이 되는 점들은 공간 전체에서 보면 작다. 

$$X$$ 위의 모든 rational function들의 집합을 $$\mathbb{K}(X)$$로 표기한다. 두 rational function의 합과 곱은 정의되는 영역의 교집합에서 정의되며, 0이 아닌 rational function의 역은 그 함수가 0이 아닌 점들에서 정의된다. 따라서 $$\mathbb{K}(X)$$는 field가 되며, 우리는 이를 *function field*라 부른다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Affine variety $$X$$에 대하여, $$\mathbb{K}(X)=\Frac\mathbb{K}[X]$$이 성립한다.

</div>

이 명제의 핵심적인 부분은 임의의 열린집합 $$U$$와 그 위에서 정의된 임의의 regular function $$f:U\rightarrow \mathbb{K}$$를 실제로 분수꼴로 나타내는 것인데, 어차피 $$U$$는 $$D(f)$$들의 합집합으로 나타낼 수 있고 ([§아핀다양체, ⁋명제 6](/ko/math/algebraic_geometry/affine_varieties#prop6)) 이 위의 regular function은 $$f$$의 거듭제곱을 분모로 갖는 유리식의 꼴이므로 증명이 어렵지 않다.

중요한 것은, 이 명제가 rational function을 계산하는 실질적인 방법을 제공한다는 것이다. 예를 들어, $$X = V(\y - \x^2)$$의 coordinate ring은 $$\mathbb{K}[\x, \y]/(\y - \x^2) \cong \mathbb{K}[\x]$$이고, 따라서 $$\mathbb{K}(X) = \operatorname{Frac}(\mathbb{K}[\x]) = \mathbb{K}(\x)$$이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 

Variety $$X$$와 공집합이 아닌 열린집합 $$U$$에 대하여, $$\mathbb{K}(U) = \mathbb{K}(X)$$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 inclusion $$\iota: U \hookrightarrow X$$가 function field의 embedding $$\iota^\ast: \mathbb{K}(X)\rightarrow \mathbb{K}(U)$$를 유도하는 것은 자명하다. 임의의 nonzero field homomorphism은 inclusion이므로, 우리는 $$\iota^\ast$$가 surjective임을 보이면 충분하다. ([\[체론\] §체, ⁋명제 2](/ko/math/field_theory/fields#prop2))

그런데 임의의 $$f \in \mathbb{K}(U)$$에 대하여, $$f$$는 $$U$$의 어떤 nonempty open subset $$V$$에서의 regular function이며, 그럼 이 $$V$$는 $$X$$의 열린집합이기도 하므로 이 pair $$(V,f)$$는 $$\mathbb{K}(X)$$에 속한다. 

</details>
<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 
$$\mathbb{P}^n$$의 function field $$\mathbb{K}(\mathbb{P}^n)$$을 생각하면, [명제 3](#prop3)에 의해 $$\mathbb{P}^n$$의 open set $$U_0$$에서의 function field를 계산하면 충분하다. 그런데 $$U_0$$은 affine variety이므로, [명제 2](#prop2)에 의해 $$\mathbb{K}[U_0]$$의 fraction field와 같고 따라서 $$\mathbb{P}^n$$의 function field는 $$n$$개의 indeterminate로 생성되는 field $$\mathbb{K}(\t_1,\ldots, \t_n)$$와 같다. 

구체적으로, 이는 $$\mathbb{P}^n$$의 원소를 $$[x_0:\cdots: x_n]$$과 같이 표현하고 $$i$$번째 좌표를 읽어오는 좌표함수를 $$\x_i$$라 했을 때, $$\t_i=\x_i/\x_0$$로 두어 얻어진다. 만일 다른 open set $$U_j$$를 잡았다면 $$\t_i=\x_i/\x_j$$를 통해 비슷한 꼴의 유리함수들이 정의되었을 것이며, 따라서 일반적으로 $$\mathbb{P}^n$$의 rational function들은 같은 차수의 homogeneous polynomial들의 비율 $$F/G$$ 형태로 나타난다는 것을 안다. 

</div>

## 유리사상

이제 regular function으로부터 regular map을 어떻게 정의했는지를 생각하면, rational function으로부터 rational map을 어떻게 정의해야 하는지는 자명하다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 두 variety $$X, Y$$ 사이의 *rational map<sub>유리사상</sub>*은 $$X$$의 공집합이 아닌 열린집합 $$U$$와 그 위에서 정의된 regular map $$\varphi: U \to Y$$의 pair $$(U,\varphi)$$를 말한다. 

</div>

앞서와 마찬가지로 두 rational map $$\varphi: U \to Y$$와 $$\psi: V \to Y$$는 $$U \cap V$$에서 일치할 때 같은 것으로 본다. Rational map은 보통 $$\varphi: X \dashrightarrow Y$$로 표기하며, 점선은 <em-ko>모든 점에서 정의되지 않을 수 있음</em-ko>을 나타낸다. 정의되지 않는 점들을 *base points*라 부른다. 

한편 rational map $$\varphi:U\rightarrow Y$$에 대하여, 우리는 $$(U,\varphi)$$와 equivalent한 rational function들을 생각할 수 있다. 그럼 이들 rational function들의 domain을 모두 합집합하면 우리는 $$\varphi$$가 정의될 수 있는 <em-ko>가장 큰</em-ko> 열린집합을 얻는다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Rational map $$\varphi: X\dashrightarrow Y$$에 대하여, 위의 과정으로 얻어진 열린집합을 $$\dom(\varphi)$$으로 적는다. 

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Rational map의 대표적인 예시 중 하나는 한 점으로부터의 projection이다. 가령 $$\mathbb{P}^2$$에서의 직선 $$\{\x_2=0\}$$을 생각하면 이는 $$\mathbb{P}^2$$ 안에 있는 projective line $$\mathbb{P}^1$$로 생각할 수 있다. 이제 점 $$[0:0:1]$$은 이 직선 위에 있지 않은 점이며, 이 점과 임의의 점 $$[x_0:x_1:x_2]$$를 잇는 직선의 방정식은

$$x_1\x_0-x_0\x_1=0$$

이다. 그럼 이 직선이 위의 $$\mathbb{P}^1$$과 만나는 점은 정확히 $$[x_0:x_1:0]$$이며 따라서 다음의 projection

$$[x_0:x_1:x_2]\mapsto [x_0:x_1]$$

은 이러한 projection을 통해 얻어진다. 

</div>

## 쌍유리동치

Regular map의 isomorphism이 두 variety가 완전히 같은 구조를 갖는다는 것을 의미한다면, birational equivalence는 두 variety가 대체로 같은 구조를 갖는다는 것을 의미한다. 많은 기하학적 성질들은, isomorphic한 variety에서 보존되는 것 뿐만 아니라 birationally equivalent한 variety들 사이에서도 보존된다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Rational map $$\varphi: X \dashrightarrow Y$$가 *dominant*라는 것은 $$\varphi$$의 image가 $$Y$$에서 dense한 것이다. 즉, $$\overline{\varphi(X)} = Y$$이 성립한다.

</div>

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Rational map $$\varphi: X \dashrightarrow Y$$가 *birational map*이라는 것은 또다른 rational map $$\psi: Y \dashrightarrow X$$가 존재하여 $$\psi \circ \varphi = \operatorname{id}_X$$와 $$\varphi \circ \psi = \operatorname{id}_Y$$가 (정의되는 곳에서) 성립하는 것이다. 두 variety $$X, Y$$가 *birationally equivalent*라는 것은 둘 사이에 birational map이 존재하는 것이다.

</div>

Birationally equivalent한 두 variety들은 "대부분의 점에서" isomorphic하다. 구체적으로, 다음 명제에서 보듯 두 variety의 isomorphic한 열린집합들이 존재한다. 이는 birational equivalence가 isomorphism보다 약하지만 여전히 강력한 관계임을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 두 variety $$X, Y$$에 대하여 다음이 동치이다.

1. $$X$$와 $$Y$$는 birationally equivalent하다.
2. $$\mathbb{K}(X) \cong \mathbb{K}(Y)$$이 성립한다.
3. $$X$$와 $$Y$$의 isomorphic한 비어있지 않은 열린부분집합들이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$X, Y$$가 birationally equivalent하다고 하자. 그럼 birational map $$\varphi: X\dashrightarrow Y$$의 정의역 $$\dom(\varphi)$$를 생각하면 $$\varphi$$가 유도하는 function field의 homomorphism $$\varphi^\ast: \mathbb{K}(Y)\rightarrow \mathbb{K}(\dom(\varphi))$$가 존재한다. 비슷한 방식으로 $$\varphi$$의 birational inverse $$\psi: Y\dashrightarrow X$$는 $$\psi^\ast: \mathbb{K}(X)\rightarrow \mathbb{K}(\dom(\psi))$$를 정의한다. 이제 [명제 3](#prop3)에 의해 $$\mathbb{K}(\dom(\varphi))=\mathbb{K}(X)$$, $$\mathbb{K}(\dom(\psi))=\mathbb{K}(Y)$$이므로 이를 사용하면 $$\mathbb{K}(X)\cong \mathbb{K}(Y)$$임을 안다.

이제 field isomorphism $$\Phi: \mathbb{K}(X) \rightarrow \mathbb{K}(Y)$$가 주어졌다 하자. $$X$$의 임의의 affine open subset $$U \subseteq X$$에 대하여, coordinate ring $$\mathbb{K}[U]$$는 $$\mathbb{K}(X)$$의 finitely generated $$\mathbb{K}$$-subalgebra이다. 이제 이들의 generator들의 $$\phi$$에 대한 image들이 모두 regular이도록 하는 $$Y$$의 affine open subset $$V\subseteq Y$$를 잡고, 이를 통해 $$\Phi\vert_{\mathbb{K}[U]}:\mathbb{K}[U]\rightarrow \mathbb{K}[V]$$를 정의할 수 있다. 한편, 비슷한 방식으로 $$\Phi^{-1}$$을 이용해 $$\Phi^{-1}\vert_{\mathbb{K}[V]}:\mathbb{K}[V]\rightarrow \mathbb{K}[U']$$를 잡을 수 있고, 이 때 $$U'\subset U$$가 성립한다. 이제 $$\Phi$$가 isomorphism이라는 가정으로부터 $$\mathbb{K}[U]=\mathbb{K}[U']$$이고 $$\mathbb{K}[U]\cong \mathbb{K}[V]$$여야 한다.

마지막 조건이 첫째 조건을 함의하는 것은 [명제 3](#prop3)에 의해 자명하다. 

</details>

이 정리는 birational equivalence를 판별하기 위해서는 function field를 보면 충분하다는 것을 보여준다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\mathbb{P}^1 \times \mathbb{P}^1$$과, $$\mathbb{P}^3$$에서의 quadric surface $$Q = V(\x\y - \z\w)$$의 function field를 계산해 보자.

우선 $$\mathbb{P}^1 \times \mathbb{P}^1$$의 경우, [명제 3](#prop3)에 의해 각 factor의 product open set $$U_0 \times U_0$$에서 계산하면 충분하다. 첫 번째 factor $$\mathbb{P}^1$$의 function field는 [예시 4](#ex4)에서 보았듯 $$\mathbb{K}(\t_1)$$이고, 두 번째 factor도 마찬가지로 $$\mathbb{K}(\t_2)$$이다. 그럼 이를 통해 이들의 function field는 $$\mathbb{K}(\t_1,\t_2)$$로 주어짐을 안다.

이제 quadric surface $$Q = V(\x\y - \z\w) \subset \mathbb{P}^3$$를 생각하자. 마찬가지로 [명제 3](#prop3)에 의해 affine patch $$\{\w \ne 0\}$$에서 계산하면 충분하다. 이 patch에서 $$\x' = \x/\w$$, $$\y' = \y/\w$$, $$\z' = \z/\w$$로 두면, 방정식 $$\x\y - \z\w = 0$$은 $$\x'\y' - \z' = 0$$이 된다. 따라서 $$\z' = \x'\y'$$이고, 이 patch의 coordinate ring은 $$\mathbb{K}[\x', \y', \z']/(\x'\y' - \z') \cong \mathbb{K}[\x', \y']$$이다. [명제 2](#prop2)에 의해 $$\mathbb{K}(Q) = \operatorname{Frac}(\mathbb{K}[\x', \y']) = \mathbb{K}(\x', \y') \cong \mathbb{K}(\t_1, \t_2)$$이다.

따라서 $$\mathbb{K}(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{K}(Q) \cong \mathbb{K}(\t_1, \t_2)$$이므로, [명제 10](#prop10)에 의해 두 다양체는 birationally equivalent하다. 실은, [§사영다양체, ⁋예시 16](/ko/math/algebraic_geometry/projective_varieties#ex16)에서 다루는 Segre embedding $$\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$, $$([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$$의 image가 정확히 $$V(\x\y - \z\w)$$이다. 즉, 이 경우 birational equivalence는 실제로 isomorphism을 이룬다. 이 예시는 birational equivalence가 isomorphism보다 약하지만, isomorphism을 포함함을 보여준다.

</div>

## Blow-up

Rational map은 base point들에서 정의되지 않는다는 한계가 있다. 이 한계를 해결하는 대표적인 도구가 *blow-up*이다. 이에 대한 motivation은 우리가 가장 처음 살펴본 함수 $$(x,y)\mapsto [x:y]$$이다. 이 함수는 $$\mathbb{A}^2$$의 점 $$(x,y)$$를 넣으면, 이 점과 원점 $$(0,0)\in \mathbb{A}^2$$를 잇는 직선의 기울기를 주는 함수로, 이것이 원점에서 정의되지 않는 이유는 직선을 정의하기 위해서는 서로 다른 두 점이 필요하기 때문이다. 이런 경우, 우리는 보통 원점 $$(0,0)$$을 고정해두고, 다른 점 $$(x,y)$$를 $$(0,0)$$을 향해 가도록 취해서 그 극한값을 계산하겠지만 이 경우 $$(0,0)$$으로 향하는 방향이 무한히 많으므로 극한이 잘 정의되지 않는다. 

Blowup의 아이디어는 간단하다. $$(0,0)$$으로 향하는 방향을 모두 따로 기록하는 것이다. 

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> 다음의 variety

$$\Bl_{(0,0)} \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

을 생각하자. 이 집합은 $$\mathbb{A}^2 \times \mathbb{P}^1$$의 closed subvariety이다. 조건 $$xv = yu$$는 점 $$(x, y)$$와 직선 $$[u : v]$$이 <em-ko>같은 방향</em-ko>에 있음을 의미한다. 즉, 

- $$\mathbb{A}^2$$의 원점이 아닌 점 $$(x,y)$$에 대해서는, 조건 $$xv=yu$$를 통해 $$\mathbb{P}^1$$의 점 $$[u:v]$$를 유일하게 결정할 수 있으며, 이를 통해 $$\Bl_{(0,0)}\mathbb{A}^2$$의 점이 유일하게 결정된다. 
- $$\mathbb{A}^2$$의 원점 $$(0,0)$$에는 모든 $$\mathbb{P}^1$$의 점이 존재할 수 있다. 

![Blowup](/assets/images/Math/Algebraic_Geometry/Rational_maps-1.png){:style="width:32em" class="invert" .align-center}
<cap markdown="1">[Har1] p.29. Fig. 3.</cap>

구체적으로, projection $$\pi_1: \operatorname{Bl}_{(0,0)} \mathbb{A}^2 \to \mathbb{A}^2$$를 $$\pi((x, y), [u : v]) = (x, y)$$로 정의하면, 원점이 아닌 모든 점의 preimage는 한 점이며, 원점의 preimage는 $$\mathbb{P}^1$$이다. 이를 *exceptional divisor*라 부른다.

이로부터 원점을 제외한 평면의 나머지 부분에서는 두 variety $$\mathbb{A}^2$$와 $$\Bl_{(0,0)}\mathbb{A}^2$$가 isomorphic하므로 $$\pi$$는 birational map이다. 

이제 앞서 언급한 rational map $$\varphi: \mathbb{A}^2 \dashrightarrow \mathbb{P}^1$$, $$(x, y) \mapsto [x : y]$$를 생각하자. 이는 원점 $$(0, 0)$$에서 정의되지 않지만, 그러나 blow-up $$\operatorname{Bl}_{(0,0)} \mathbb{A}^2$$에서 보면 이는 그저 $$\mathbb{P}^1$$ factor로의 projection $$\pr_2$$에 불과하며 특히 이는 regular map이다. 이러한 방식으로 우리는 birational map이 정의되지 않는 base point를 해소해줄 수 있다. 

</div>

---

**참고문헌**

**[Har1]** R. Hartshorne, *Algebraic Geometry*, Springer, 1977.  
**[Har2]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
