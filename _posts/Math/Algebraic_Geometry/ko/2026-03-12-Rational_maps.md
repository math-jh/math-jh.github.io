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

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{P}^n$$의 function field $$\mathbb{K}(\mathbb{P}^n)$$은 $$\mathbb{K}(\x_1/\x_0,\ldots, \x_n/\x_0)$$과 같다. 

</div>

## 유리사상

이제 regular function으로부터 regular map을 어떻게 정의했는지를 생각하면, rational function으로부터 rational map을 어떻게 정의해야 하는지는 자명하다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 두 variety $$X, Y$$ 사이의 *rational map<sub>유리사상</sub>*은 $$X$$의 공집합이 아닌 열린집합 $$U$$와 그 위에서 정의된 regular map $$\varphi: U \to Y$$의 pair $$(U,\varphi)$$를 말한다. 

</div>

앞서와 마찬가지로 두 rational map $$\varphi: U \to Y$$와 $$\psi: V \to Y$$는 $$U \cap V$$에서 일치할 때 같은 것으로 본다. Rational map은 보통 $$\varphi: X \dashrightarrow Y$$로 표기하며, 점선은 <em-ko>모든 점에서 정의되지 않을 수 있음</em-ko>을 나타낸다. 정의되지 않는 점들을 *base points*라 부른다. 

한편 rational map $$\varphi:U\rightarrow Y$$에 대하여, 우리는 $$(U,\varphi)$$와 equivalent한 rational function들을 생각할 수 있다. 그럼 이들 rational function들의 domain을 모두 합집합하면 우리는 $$\varphi$$가 정의될 수 있는 <em-ko>가장 큰</em-ko> 열린집합을 얻는다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Rational map $$\varphi: X\dashrightarrow Y$$에 대하여, 위의 과정으로 얻어진 열린집합을 $$\dom(\varphi)$$으로 적는다. 

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Rational map의 대표적인 예시 중 하나는 한 점으로부터의 projection이다. 가령 $$\mathbb{P}^2$$에서의 직선 $$\{\x_2=0\}$$을 생각하면 이는 $$\mathbb{P}^2$$ 안에 있는 projective line $$\mathbb{P}^1$$로 생각할 수 있다. 이제 점 $$[0:0:1]$$은 이 직선 위에 있지 않은 점이며, 이 점과 임의의 점 $$[x_0:x_1:x_2]$$를 잇는 직선의 방정식은

$$x_1\x_0-x_0\x_1=0$$

이다. 그럼 이 직선이 위의 $$\mathbb{P}^1$$과 만나는 점은 정확히 $$[x_0:x_1:0]$$이며 따라서 다음의 projection

$$[x_0:x_1:x_2]\mapsto [x_0:x_1]$$

은 이러한 projection을 통해 얻어진다. 비슷하게, 도입부에서 생각한 함수 

$$\mathbb{A}^2\rightarrow \mathbb{P}^1; \qquad (x,y)\mapsto [x:y]$$

는 $$(0,0)$$에서 점 $$(x,y)$$로의 projection으로 생각할 수 있다. 이러한 방식으로 얻어지는 projection map들은, projection을 시작하는 점을 어디로 보낼지가 정해지지 않으므로, 이 점을 제외한 나머지 모든 점에서 정의되는 rational map이 된다. 

</div>

## 쌍유리동치

Regular map의 isomorphism이 두 다양체가 완전히 같은 구조를 갖는다는 것을 의미한다면, birational equivalence는 두 다양체가 대체로 같은 구조를 갖는다는 것을 의미한다. 많은 기하학적 성질들은, isomorphic한 variety에서 보존되는 것 뿐만 아니라 birationally equivalent한 variety들 사이에서도 보존된다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Rational map $$\varphi: X \dashrightarrow Y$$가 *birational map*이라는 것은 또다른  rational map $$\psi: Y \dashrightarrow X$$가 존재하여 $$\psi \circ \varphi = \operatorname{id}_X$$와 $$\varphi \circ \psi = \operatorname{id}_Y$$가 (정의되는 곳에서) 성립하는 것이다. 두 다양체 $$X, Y$$가 *birationally equivalent*라는 것은 둘 사이에 birational map이 존재하는 것이다.

</div>

Birationally equivalent한 두 다양체는 "대부분의 점에서" isomorphic하다. 구체적으로, 다음 명제에서 보듯 두 다양체의 isomorphic한 열린부분집합들이 존재한다. 이는 birational equivalence가 isomorphism보다 약하지만 여전히 강력한 관계임을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 두 variety $$X, Y$$에 대하여 다음이 동치이다.

1. $$X$$와 $$Y$$는 birationally equivalent하다.
2. $$\mathbb{K}(X) \cong \mathbb{K}(Y)$$이 성립한다.
3. $$X$$와 $$Y$$의 isomorphic한 비어있지 않은 열린부분집합들이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

jb

**(1) $$\Rightarrow$$ (2)**: Birational map $$\varphi: X \dashrightarrow Y$$는 $$\operatorname{dom}(\varphi) \subseteq X$$에서 정의된다. $$\varphi$$가 regular이므로, $$\varphi$$에 의해 유도되는 coordinate ring 사이의 homomorphism인 pullback $$\varphi^\ast: \mathbb{K}(Y) \to \mathbb{K}(\operatorname{dom}(\varphi))$$가 존재한다. $$\mathbb{K}(\operatorname{dom}(\varphi)) = \mathbb{K}(X)$$이고 (irreducible variety에서 열린부분집합 위의 rational function field는 전체 variety의 것과 같음), $$\varphi$$가 birational이므로 $$\varphi^\ast$$는 field isomorphism이다.

**(2) $$\Rightarrow$$ (3)**: Field isomorphism $$\Phi: \mathbb{K}(X) \xrightarrow{\sim} \mathbb{K}(Y)$$이 주어졌다 하자. $$X$$의 affine open (다양체의 열린부분집합 가운데 그 자체가 affine variety인 것) $$U \subseteq X$$을 고르면, $$U$$의 [coordinate ring](/ko/math/algebraic_geometry/affine_varieties#def11) $$\mathbb{K}[U]$$는 $$\mathbb{K}(X)$$의 부분환이다. $$\Phi$$에 의해 $$\mathbb{K}[U]$$의 원소들은 $$\mathbb{K}(Y)$$의 원소로 보내지며, 이들은 $$Y$$의 어떤 affine open $$V$$에서 동시에 정의되는 regular function이 된다. 구체적으로, $$\mathbb{K}[U]$$의 생성원들의 image가 분모를 가지는 principal open set들의 교집합을 $$V$$로 취하면, $$\Phi$$는 ring homomorphism $$\mathbb{K}[U] \to \mathbb{K}[V]$$를 유도한다. 역으로 $$\Phi^{-1}$$에 같은 논의를 적용하면, $$\Phi$$와 $$\Phi^{-1}$$은 $$U$$의 부분열린집합과 $$V$$의 부분열린집합 사이의 ring isomorphism을 정의하고, 이에 대응하는 isomorphism $$U' \xrightarrow{\sim} V'$$이 존재한다.

**(3) $$\Rightarrow$$ (1)**: $$U \subseteq X$$와 $$V \subseteq Y$$가 isomorphic하다면, isomorphism $$\varphi: U \to V$$를 rational map $$X \dashrightarrow Y$$로 볼 수 있다. 그 inverse 또한 rational map이므로 birational map이다.

</details>

이 정리는 birational equivalence를 판별하는 세 가지 방법을 제공한다. 특히 (2)는 함수체를 계산함으로써 birational equivalence를 판별할 수 있음을 보여준다. 이는 매우 실용적인 방법이다. 예를 들어, 두 다양체의 함수체가 $$\mathbb{K}(t_1, t_2)$$로 같다면, 이들은 birationally equivalent하다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Quadric surface와 $$\mathbb{P}^1 \times \mathbb{P}^1$$**: $$\mathbb{P}^1 \times \mathbb{P}^1$$과 $$V(\x\y - \z\w) \subset \mathbb{P}^3$$은 birationally equivalent하다. 둘 다 rational function field $$\mathbb{K}(t_1, t_2)$$를 갖기 때문이다. 사실 이 둘은 isomorphic하다. [사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 다루는 Segre embedding $$\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$$, $$([x : y], [u : v]) \mapsto [xu : xv : yu : yv]$$의 image가 정확히 $$V(\x\y - \z\w)$$이다. 이 예시는 birational equivalence가 isomorphism보다 약하지만, isomorphism을 포함함을 보여준다.

</div>

## Blow-up과 유리사상

Rational map은 "대부분의 점에서" 정의되지만, base points에서 정의되지 않는다는 한계가 있다. 이 한계를 해결하는 대표적인 도구가 *blow-up*이다. Blow-up은 base point가 있는 곳을 "폭발"시켜 새로운 다양체를 만들고, 이 과정에서 rational map을 regular map으로 바꿀 수 있게 한다. Blow-up은 birational map의 가장 기본적인 예시이자, birational geometry에서 가장 중요한 연산 중 하나이다. 이는 다양체의 특이점을 "해소"하거나 다양체의 구조를 단순화하는 데 사용되며, 국소적으로는 간단하지만 전역적으로는 매우 강력한 도구이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **Blow-up of $$\mathbb{A}^2$$ at origin**: 

$$\operatorname{Bl}_0 \mathbb{A}^2 = \{((x, y), [u : v]) \in \mathbb{A}^2 \times \mathbb{P}^1 \mid xv = yu\}$$

이 집합은 $$\mathbb{A}^2 \times \mathbb{P}^1$$의 닫힌부분다양체이다. 조건 $$xv = yu$$는 점 $$(x, y)$$와 직선 $$[u : v]$$이 "같은 방향"에 있음을 의미한다. 즉, 원점이 아닌 점 $$(x, y)$$에 대해서는 유일한 직선 $$[x : y]$$이 존재하고, 원점 $$(0, 0)$$에 대해서는 모든 직선 $$[u : v]$$가 가능하다.

Projection $$\pi: \operatorname{Bl}_0 \mathbb{A}^2 \to \mathbb{A}^2$$를 $$\pi((x, y), [u : v]) = (x, y)$$로 정의하자. 그럼:

- $$\pi$$는 원점이 아닌 모든 점에서 isomorphism이다. 구체적으로, $$(x, y) \ne (0, 0)$$이면 $$\pi^{-1}(x, y) = \{((x, y), [x : y])\}$$이다.
- 원점 위의 fiber는 $$\pi^{-1}(0, 0) = \{((0, 0), [u : v]) \mid [u : v] \in \mathbb{P}^1\} \cong \mathbb{P}^1$$이다. 이를 *exceptional divisor*라 부른다.

따라서 $$\pi$$는 birational map이다. 기하학적으로, blow-up은 원점을 "폭발"시켜 원점을 지나는 모든 직선들의 공간 $$\mathbb{P}^1$$으로 대체한다. 이는 원점에서의 "특이성"을 $$\mathbb{P}^1$$이라는 매끄러운 다양체로 "펼쳐놓는" 과정이다.

</div>

Blow-up의 중요성은 여러 관점에서 드러난다. 우선, 많은 특이점들은 적절한 blow-up을 통해 매끄러운 다양체로 바뀐다. 예를 들어, 평면 곡선의 node (곡선의 자기교차점, singular point의 일종)는 blow-up을 통해 두 개의 매끄러운 점으로 분리된다. 또한 임의의 birational map은 blow-up과 blow-down의 합성으로 분해될 수 있다는 것이 알려져 있는데[^1], 이를 통해 복잡한 birational 관계를 기본적인 blow-up 연산으로 분석할 수 있다. 마지막으로, 모든 다양체를 적절한 blow-down을 통해 "minimal model"으로 축소시키려는 minimal model program[^2]에서 blow-up은 핵심적인 역할을 한다.

---

[^1]: *Weak factorization theorem* (Włodarczyk 2003): 임의의 birational map은 blow-up과 그 역인 blow-down의 유한 합성으로 분해할 수 있다는 정리. Birational geometry의 기본 정리 중 하나이다.
[^2]: *Minimal model program* (Mori, Kawamata, Shokurov 등): 모든 대수다양체를 blow-down을 통해 더 "간단한" 모델로 축소시키는 프로그램. 3차원까지는 성공적으로 완성되었으며, 고차원에서는 여전히 활발히 연구 중이다.

---

**참고문헌**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
