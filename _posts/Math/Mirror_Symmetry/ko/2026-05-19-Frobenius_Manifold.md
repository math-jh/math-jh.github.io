---
title: "Frobenius manifold"
excerpt: "WDVV equation과 flat structure를 갖는 manifold로서, Dubrovin connection의 기반이 된다."

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/frobenius_manifold
sidebar:
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/frobenius_manifold.png
    overlay_filter: 0.5

date: 2026-05-19
last_modified_at: 2026-05-19
weight: 3

published: false
---

우리는 [§Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)에서 toric Fano variety $$X_\Sigma$$의 mirror symmetry가 Jacobi ring과 quantum cohomology 사이의 isomorphism 

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

로 요약된다는 것을 살펴보았다. 그러나 해당 글에서도 살펴보았듯 quantum cohomology는 이 ring 동형이 잡아내는 것 이상의 구조를 갖는데, 이는 Novikov parameter $$q$$의 변화에 따라 product 자체가 변형되기 때문이다. 이러한 deformation을 담아낼 수 있는 구조가 Frobenius로, 이번 글에서 우리는 우선 finite-dimensional Frobenius algebra의 정의를 짚은 뒤 Dubrovin의 Frobenius manifold 개념과 WDVV equation을 차례로 살펴본다.

## Frobenius algebra

Frobenius manifold는 직관적으로 각 점에서 Frobenius algebra structure를 갖는 manifold이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Finite-dimensional commutative, associative $$\mathbb{C}$$-algebra $$A$$와 그 위에 정의된 non-degenerate symmetric bilinear form $$\eta: A \otimes A \to \mathbb{C}$$가 주어졌다 하자. 만일 모든 원소 $$x,y,z\in A$$에 대하여 다음의 식

$$\eta(x \cdot y,z) = \eta(x,y \cdot z)$$

이 성립한다면, 이 pair $$(A, \eta)$$를 *Frobenius algebra<sub>프로베니우스 대수</sub>*라 부른다.

</div>

위 조건은 $$A$$의 곱셈 $$\cdot : A \otimes A \to A$$와 bilinear form $$\eta$$가 호환되어, 세 인수 모두에 대해 대칭인 trilinear form $$c(x,y,z) := \eta(x \cdot y,z)$$를 정의함을 의미한다. 실제로 commutativity로부터 

$$c(x,y,z) = \eta(x \cdot y,z) = \eta(y \cdot x,z) = c(y,x,z)$$

이고, Frobenius 조건으로부터 

$$c(x,y,z) = \eta(x,y \cdot z) = \eta(y \cdot z, x) = c(y,z,x)$$

이다. 따라서 $$c$$는 세 변수에 대해 완전히 symmetric하며, 이 trilinear form이 Frobenius structure의 모든 정보를 담고 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Compact Kähler manifold $$X$$의 cohomology ring $$H^\ast(X, \mathbb{C})$$는 cup product와 Poincaré pairing

$$\eta(\alpha, \beta) = \int_X \alpha \cup \beta$$

에 대해 Frobenius algebra이다. 이는 다음의 식

$$\eta(\alpha \cup \beta, \gamma) = \eta(\alpha, \beta \cup \gamma)$$

이 모든 $$\alpha,\beta,\gamma$$에 대해 성립한다는 것이며, 이 식은 cup product의 결합법칙으로 얻어지는 것이다. 

</div>

한편, 우리는 [§Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)의 예시에서 Landau-Ginzburg model을 소개했는데, 이는 주어진 manifold $$\check{X}$$ 위에 주어진 holomorphic function $$W$$로 이루어지며, $$W$$의 critical point들을 담고 있는 Jacobi ring이 B-model의 정보를 들고 있었다. 국소적으로 이는 다음과 같이 적힌다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Holomorphic function $$f : \mathbb{C}^n \to \mathbb{C}$$가 원점에서 *isolated hypersurface singularity*를 갖는다는 것은 다음의 두 조건이 성립하는 것이다.

1. $$f(0) = 0$$, $$df(0) = 0$$.
2. 원점이 $$f$$의 critical point들 중 *isolated*인 것, 즉 원점의 어떤 근방 안에서 $$df = 0$$의 해가 원점 하나뿐이다.

</div>

표준적인 예시는 $$f(\x) = \x^{k+1}$$ ($$k \geq 1$$)이며, 우리는 이를 $$A_k$$-type singularity라 부른다. 

[정의 3](#def3)이 한 점에서의 *국소* 개념인 반면, polynomial ring을 ideal로 quotient한 다음의 *전역* 객체는 $$f$$의 모든 critical point를 동시에 본다. 다항식 $$f : \mathbb{C}^n \to \mathbb{C}$$의 모든 critical point가 (적절한 좌표 평행이동 후 원점에서) [정의 3](#def3)의 의미로 isolated일 때, 그 *Milnor ring*을

$$\Jac(f) = \mathbb{C}[\x_1, \ldots, \x_n]/(\partial_1 f, \ldots, \partial_n f)$$

로 정의한다. 이는 critical scheme $$\Crit(f) = \{df = 0\}$$의 (전역) coordinate ring에 해당하며, "모든 critical point가 isolated"라는 조건은 정확히 $$\Jac(f)$$가 $$\mathbb{C}$$ 위에서 유한차원이라는 조건과 동치이다. 그 차원 $$\mu(f) := \dim_\mathbb{C} \Jac(f)$$를 *Milnor number*라 부르며, 직관적으로 $$\mu(f)$$는 $$f$$를 generic하게 살짝 변형했을 때 흩어지는 simple critical point들의 총 개수이다 (각 critical point에서의 국소 Milnor number의 합과 같다).

엄밀하게는 싱귤러리티 이론의 *국소* Milnor ring은 위의 polynomial ring 대신 원점에서의 수렴 멱급수환 $$\mathbb{C}\{\x_1, \ldots, \x_n\}$$ (또는 formal 멱급수환 $$\mathbb{C}[[\x_1, \ldots, \x_n]]$$)을 $$(\partial_i f)$$로 modulo한 것이며, 우리가 쓴 polynomial 버전은 *전역* Jacobi ring으로서 모든 critical point에서의 국소 Milnor ring들의 직합으로 분해된다. 다항식 $$f$$가 원점을 유일한 critical point로 가지는 경우 두 ring이 일치하므로, 이 글에서는 [§Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)의 Laurent polynomial 표기 $$\mathcal{O}(\check{X}) / (\partial_i W)$$와 정합되도록 polynomial 버전을 채택한다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> Isolated hypersurface singularity $$f : \mathbb{C}^n \to \mathbb{C}$$의 Milnor ring $$\Jac(f)$$ 위에 다음의 *residue pairing*

$$\eta(g, h) := \frac{1}{(2\pi i)^n} \oint_{\Gamma_\epsilon} \frac{g(\x) h(\x) \, d\x_1 \wedge \cdots \wedge d\x_n}{\partial_1 f \cdots \partial_n f}$$

을 정의하자. 여기서 적분은 원점 근방의 작은 contour $$\Gamma_\epsilon = \{\lvert\partial_i f\rvert = \epsilon\}_{i=1,\ldots,n}$$ 위에서 이루어지며, 이는 Grothendieck residue라 불리는 표준 구성으로 [정의 3](#def3)의 isolated 조건이 정확히 contour $$\Gamma_\epsilon$$이 잘 정의되도록 보장한다. 직관적으로 이는 [예시 2](#ex2)의 manifold 전체 적분 $$\int_X$$를 critical scheme이라는 *한 점*에서의 적분으로 국소화한 것에 해당한다.

그럼 $$(\Jac(f), \eta)$$가 Frobenius algebra가 되는 것을 다음과 같이 확인할 수 있다. Non-degeneracy는 isolated 조건과 동치이며 ($$\Jac(f)$$가 유한차원 Gorenstein local algebra라는 표준 사실), Frobenius 호환성 $$\eta(g \cdot h, k) = \eta(g, h \cdot k)$$는 residue 식에서 $$ghk$$의 결합 순서가 contour 적분과 무관하다는 cyclic symmetry로부터 자동 성립한다.

</div>

이상의 구성은 [§Mirror Symmetry 개요](/ko/math/mirror_symmetry/overview)에서 등장한 superpotential $$W$$의 Jacobi ring $$\Jac(W)$$의 (affine 공간 위의) 추상적 모형에 해당한다. Hori-Vafa mirror $$(\check{X}, W_q)$$의 경우 ambient space가 algebraic torus $$(\mathbb{C}^\ast)^n$$이고 $$W_q$$가 그 위의 Laurent polynomial로 주어지지만, 본질적 구조는 동일하다. $$W_q$$는 $$(\mathbb{C}^\ast)^n$$ 위에서 *여러* isolated critical point들을 가지며 (Overview ex5의 $$\mathbb{P}^1$$에선 $$\x = \pm\sqrt{q}$$ 두 점, ex6의 $$\mathbb{P}^2$$에선 $$\z_1^3 = q$$의 세 점), 위에서 언급한 전역-국소 분해에 의해 $$\Jac(W_q)$$는 각 critical point에서의 국소 Milnor ring들의 직합이며, residue pairing도 그 직합 구조로 자연스럽게 분해된다.

## Frobenius manifold의 정의

Frobenius algebra가 점 한 곳에 부여된 대수적 구조라면, Frobenius manifold는 이를 manifold 전체에 걸쳐 부드럽게 변형되는 family로 확장한 것이다. Dubrovin의 정의는 각 접공간에 Frobenius algebra 구조를 부여하되, 그것이 manifold 위에서 *flat*한 metric과 *potential*에 의해 통제되는 형태로 변형되어야 한다는 요구로 요약된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Smooth manifold $$M$$ 위에 다음의 자료들이 주어졌다고 하자.

1. 접다발 $$TM$$ 위의 symmetric non-degenerate bilinear form $$\eta$$이며, 그 Levi-Civita connection $$\nabla$$가 *flat*하다. 즉 $$\eta$$의 곡률이 $$0$$이다.
2. 각 점 $$p \in M$$의 접공간 $$T_p M$$ 위에 commutative associative product $$\circ_p : T_p M \otimes T_p M \to T_p M$$이 부여되어, $$p$$에 대해 smooth하게 변한다.
3. 모든 점에서 곱셈 $$\circ$$의 항등원이 되는 vector field $$e$$가 존재하며, $$\nabla e = 0$$이다.
4. *Euler vector field* $$E$$가 존재한다. 구체적으로 $$E$$는 $$\nabla \nabla E = 0$$을 만족하며 (즉, $$\eta$$의 flat coordinate에 대해 affine), 어떤 상수 $$d \in \mathbb{C}$$에 대해 $$\operatorname{Lie}_E(\circ) = \circ$$와 $$\operatorname{Lie}_E(\eta) = (2 - d) \eta$$를 만족한다.
5. (Frobenius 조건) 모든 vector field $$X, Y, Z$$에 대해 $$\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$$가 성립한다.
6. (Potentiality) 4-tensor $$\nabla c$$이 네 변수에 대해 완전히 대칭이다. 여기서 $$c(X, Y, Z) := \eta(X \circ Y, Z)$$는 곱셈으로부터 정의되는 symmetric trilinear form이다.

이 자료를 갖춘 manifold $$(M, \eta, \circ, e, E)$$를 *Frobenius manifold<sub>프로베니우스 다양체</sub>*라 부른다.

</div>

이 정의에 등장하는 각 조건을 정리해 두자. 첫째와 둘째 조건이 *Frobenius algebra의 family*로서의 기본 자료를 제공한다. 즉 [정의 1](#def1)의 조건이 각 접공간에서 성립하며, 여기에 더해 $$\eta$$가 *flat metric*이라는 강한 강체조건이 부과된다. $$\nabla$$가 flat이라는 사실은 적당한 좌표계 $$t^1, \ldots, t^n$$를 잡아 $$\eta_{\alpha\beta} = \eta(\partial_{t^\alpha}, \partial_{t^\beta})$$가 상수가 되도록 할 수 있음을 의미하며, 이러한 좌표를 *flat coordinate*라 부른다. 항등원 vector field $$e$$가 flat이라는 조건은 적절한 flat coordinate 선택을 통해 $$e = \partial_{t^1}$$로 정규화할 수 있음을 의미한다. Euler field $$E$$는 곱셈과 metric의 grading을 통제하는 vector field로, $$d$$는 *conformal dimension*이라 부르며 mirror symmetry에서는 $$X$$의 복소 차원과 관련된다.

다섯째 조건은 [정의 1](#def1)의 Frobenius 조건이 각 접공간에서 성립함을 요구하며, 여섯째 조건이 가장 비자명하다. Trilinear form $$c$$가 점마다 대칭이라는 사실은 다섯째 조건과 곱셈의 commutativity로부터 따라온다. 그런데 여섯째 조건은 *공변미분* $$\nabla c$$ 역시 네 변수에 대해 대칭이라는 것을 요구하는데, 이것이 바로 $$c$$가 어떤 *potential function*의 세 번째 도함수로 표현될 수 있도록 만드는 적분 가능성 조건이다.

<div class="remark" markdown="1">

<ins id="rmk6">**참고 6**</ins> 위 정의는 Dubrovin [Dub] §1에서의 원형을 따르며, 문헌에 따라 약간씩 다른 표현이 등장한다. 예를 들어 Hertling [Her]에서는 $$\circ$$의 commutativity와 Frobenius 조건이 $$c$$의 대칭성으로 묶여 표현되고, Manin [Man]은 super-grading을 포함한 더 일반적인 정의를 도입한다. 또한 일부 저자는 Euler field 조건을 *conformal Frobenius manifold*로 분리하여 다루며, 이 경우 conformal 조건이 빠진 manifold를 *weak Frobenius manifold*라 부르기도 한다. 본 글에서는 Dubrovin의 conformal 정의를 표준으로 채택한다.

</div>

## Potential과 WDVV equation

[정의 5](#def5)의 potentiality 조건이 가지는 직접적 결과는 trilinear form $$c$$가 단일 scalar function의 세 번째 도함수로 표현될 수 있다는 것이다. 다음 명제가 그것을 정확하게 진술한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Frobenius manifold $$(M, \eta, \circ, e, E)$$의 flat coordinate $$t^1, \ldots, t^n$$에 대해, $$M$$ 위에 (국소적으로) 정의된 holomorphic function $$F: M \to \mathbb{C}$$가 존재하여

$$c_{\alpha\beta\gamma}(t) := \eta(\partial_{t^\alpha} \circ \partial_{t^\beta}, \partial_{t^\gamma}) = \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\gamma}$$

가 모든 $$\alpha, \beta, \gamma$$에 대해 성립한다. 이러한 $$F$$를 Frobenius manifold의 *potential*이라 부른다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Flat coordinate $$t^\alpha$$에 대해 $$\nabla_{\partial_{t^\delta}}$$는 단순한 편미분 $$\partial_{t^\delta}$$와 일치하므로, [정의 5](#def5)의 potentiality 조건은

$$\partial_{t^\delta} c_{\alpha\beta\gamma} = \partial_{t^\alpha} c_{\delta\beta\gamma}$$

가 네 인덱스에 대해 대칭으로 성립한다는 의미이다. 한편 $$c$$ 자체가 세 인덱스에 대해 대칭이므로, 이를 함께 모으면 1-form $$\omega_{\beta\gamma} := \sum_\alpha c_{\alpha\beta\gamma} dt^\alpha$$가 closed임을 얻는다. Poincaré lemma로부터 국소적으로 함수 $$G_{\beta\gamma}$$가 존재해 $$\partial_{t^\alpha} G_{\beta\gamma} = c_{\alpha\beta\gamma}$$이며, $$c$$의 대칭성으로부터 $$G_{\beta\gamma} = G_{\gamma\beta}$$이고 또한 $$\partial_{t^\alpha} G_{\beta\gamma} = \partial_{t^\beta} G_{\alpha\gamma}$$가 성립한다. 다시 Poincaré lemma를 한 단계 더 적용하면 함수 $$H_\gamma$$가 존재해 $$\partial_{t^\beta} H_\gamma = G_{\beta\gamma}$$이고, $$H_\gamma$$의 대칭성 $$\partial_{t^\delta} H_\gamma = \partial_{t^\gamma} H_\delta$$로부터 마지막으로 scalar function $$F$$가 존재해 $$\partial_{t^\gamma} F = H_\gamma$$가 성립한다. 종합하면 $$\partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F = c_{\alpha\beta\gamma}$$이다.

</details>

이로써 Frobenius manifold의 곱셈은 단일 potential $$F$$의 세 번째 도함수로 압축적으로 부호화된다. 즉 flat coordinate를 잡고 $$\eta^{\alpha\beta}$$를 $$\eta_{\alpha\beta}$$의 역행렬이라 하면, 곱셈의 structure constant는

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_{\gamma, \delta} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\delta} \eta^{\delta\gamma} \partial_{t^\gamma}$$

로 주어진다. 이제 결정적인 관찰은 곱셈 $$\circ$$가 associative라는 사실이 $$F$$에 대한 비선형 미분방정식으로 번역된다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (WDVV equation)**</ins> [명제 7](#prop7)의 potential $$F$$는 모든 $$\alpha, \beta, \gamma, \delta$$에 대해 다음의 *Witten-Dijkgraaf-Verlinde-Verlinde equation*을 만족한다.

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곱셈 $$\circ$$의 associativity $$(\partial_{t^\alpha} \circ \partial_{t^\beta}) \circ \partial_{t^\gamma} = \partial_{t^\alpha} \circ (\partial_{t^\beta} \circ \partial_{t^\gamma})$$을 structure constant로 풀어 쓰자. $$C_{\alpha\beta}{}^\gamma := \sum_\delta c_{\alpha\beta\delta} \eta^{\delta\gamma}$$로 정의하면 곱셈은

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_\gamma C_{\alpha\beta}{}^\gamma \partial_{t^\gamma}$$

이고, associativity는

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta$$

로 표현된다. 여기에 [명제 7](#prop7)의 결과 $$c_{\alpha\beta\gamma} = \partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F$$를 대입하면

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}$$

를 얻는다. 역으로 이 PDE 시스템을 만족하는 $$F$$로부터 정의된 곱셈은 자동으로 associative하므로 WDVV equation은 Frobenius manifold의 associativity와 정확히 동치인 조건이 된다.

</details>

WDVV equation은 $$F$$의 세 번째 도함수들 사이의 quadratic relation이며, $$F$$ 자체에 대해서는 3차 비선형 편미분방정식 시스템이다. Mirror symmetry의 A-model 측에서 quantum cohomology의 Gromov-Witten potential은 이 equation을 만족하는 대표적 예시이며, 이는 양변의 두 합 표현이 결국 동일한 enumerative 의미 (4-point Gromov-Witten invariant의 두 가지 splitting을 따라 계산한 결과)를 가짐을 반영한다. Frobenius 조건은 항등원 $$e = \partial_{t^1}$$에 대해 $$\partial_{t^1} \partial_{t^\alpha} \partial_{t^\beta} F = \eta_{\alpha\beta}$$로 정규화되며, Euler field 조건은 $$F$$가 적절한 weight를 갖는 *quasi-homogeneous* function임을 의미한다.

## 예시

다음 예시는 가장 기본적인 Frobenius manifold이며, 이후의 더 복잡한 quantum cohomology 예시와 비교 기준이 된다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$M = \mathbb{C}^n$$ 위에 좌표 $$t^1, \ldots, t^n$$을 도입하고

$$\eta = \sum_{i=1}^n dt^i \otimes dt^i,\qquad \partial_{t^i} \circ \partial_{t^j} = \delta_{ij} \partial_{t^i}$$

으로 두자. 이 때 항등원은 $$e = \sum_i \partial_{t^i}$$이고, Euler field는 $$E = \sum_i t^i \partial_{t^i}$$이다. 곱셈은 각 점에서 $$n$$개의 idempotent로 분해되며, 이를 *semisimple Frobenius manifold*의 표준 예시라 부른다. Potential은

$$F = \frac{1}{6} \sum_{i=1}^n (t^i)^3$$

으로 잡을 수 있으며, 직접 미분하면 $$\partial_{t^i} \partial_{t^j} \partial_{t^k} F = \delta_{ijk}$$이 곱셈의 structure constant $$c_{ijk}$$와 일치한다. WDVV equation의 양변은 모두 $$\delta_{\alpha\beta\delta} \cdot \delta_{\gamma\beta\delta}$$ 형태의 곱들의 합으로 계산되며 자명하게 동일하다.

</div>

위 예시에서 좌표 $$t^i$$는 *canonical coordinate*라 불리는 것으로, 이들 좌표에서 곱셈이 대각화되는 특별한 좌표계이다. 일반적으로 semisimple Frobenius manifold란 generic point에서 곱셈 $$\circ_p$$가 semisimple, 즉 $$n$$개의 idempotent의 직합으로 분해되는 경우를 말하며, [예시 9](#ex9)은 그 가장 단순한 모형이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> Compact Kähler manifold $$X$$의 cohomology vector space $$H^\ast(X, \mathbb{C})$$ 위에 (formal) coordinate $$t = \sum_\alpha t^\alpha \sigma^\alpha$$를 도입하면, Gromov-Witten potential

$$F(t) = \sum_{n \ge 3} \sum_\beta \frac{1}{n!} \langle t, \ldots, t \rangle_{0, n, \beta}^X$$

는 ([Dub], [Man]) WDVV equation을 만족하는 formal power series이다. 그 세 번째 도함수가 정의하는 곱셈 $$\circ_t$$는 quantum product $$\star$$의 *big* 버전이며, [정의 1](#def1)의 의미에서 각 $$T_t H^\ast(X)$$를 Frobenius algebra로 만든다. Metric은 Poincaré pairing $$\eta(\alpha, \beta) = \int_X \alpha \cup \beta$$이며, 항등원은 cohomology의 unit $$1 \in H^0(X)$$, Euler field는 $$X$$의 first Chern class와 grading을 함께 부호화한다. $$t = 0$$에서의 곱셈은 cup product로 환원되며 ([예시 2](#ex2)), 이로부터 quantum cohomology의 small 버전 $$QH^\ast(X)$$는 이 Frobenius manifold의 $$t = 0$$ 근방을 *Novikov variable* 방향으로만 제한한 부분구조로 이해된다.

특히 $$X = \mathbb{P}^n$$의 경우, Schubert basis $$\sigma^0 = 1, \sigma^1, \ldots, \sigma^n$$에 대응하는 좌표 $$t^0, \ldots, t^n$$를 잡으면 Gromov-Witten 계산을 통해 potential의 명시적인 closed form을 얻을 수 있으며, 그로부터 small quantum cohomology ring $$QH^\ast(\mathbb{P}^n) = \mathbb{C}[\sigma, q]/(\sigma^{n+1} - q)$$가 복원된다. 즉 Frobenius manifold 구조는 small quantum ring을 한 차원 더 큰 deformation 안에 자리잡게 하는 것이다.

</div>

이렇듯 Frobenius manifold는 quantum cohomology의 ring structure를 *deformation parameter $$t$$의 함수*로서 일관성 있게 다룰 수 있는 무대를 제공한다. 이어지는 [§Dubrovin Connection](/ko/math/mirror_symmetry/dubrovin_connection)에서는 이 manifold 위에 자연스럽게 정의되는 flat pencil of connections, 즉 Dubrovin connection을 도입하고, 그것이 quantum differential equation을 통해 mirror symmetry의 B-model 측 Gauss-Manin system과 정확히 대응함을 살펴본다.

---

**참고문헌**

**[Dub]** B. Dubrovin, *Geometry of $$2$$D topological field theories*, Integrable systems and quantum groups (Montecatini Terme, 1993), Lecture Notes in Math. **1620**, Springer, 1996, 120--348.

**[Her]** C. Hertling, *Frobenius Manifolds and Moduli Spaces for Singularities*, Cambridge Tracts in Mathematics **151**, Cambridge University Press, 2002.

**[Man]** Yu. I. Manin, *Frobenius Manifolds, Quantum Cohomology, and Moduli Spaces*, American Mathematical Society Colloquium Publications **47**, AMS, 1999.

**[HM]** C. Hertling, Yu. Manin, *Weak Frobenius manifolds*, Internat. Math. Res. Notices **1999**, no. 6, 277--286.
