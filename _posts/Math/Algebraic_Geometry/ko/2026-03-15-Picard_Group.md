---
title: "Picard Group"
excerpt: "The Picard group and its properties"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/picard_group
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Picard_Group.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 11

---

[\[Line Bundles\]](/ko/math/algebraic_geometry/line_bundles)에서 우리는 line bundle의 개념을 정의하고, line bundle들의 tensor product와 dual을 살펴보았다. 이제 우리는 line bundle들의 isomorphism class들이 자연스러운 group 구조를 갖는다는 것을 보일 것이다. 이 group을 *Picard group*이라 부르며, [\[Line Bundles\] §명제 16](/ko/math/algebraic_geometry/line_bundles#prop16)에서 보듯 divisor class group과 자연스럽게 동형이다.

Picard group은 다양체의 "twisting structure"를 분류하는 중요한 불변량이다. 예를 들어, $$\operatorname{Pic}(\mathbb{A}^n) = 0$$이지만 $$\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$이다. 이는 affine space가 "twist가 없는" 공간인 반면, projective space는 "twist"를 허용한다는 것을 보여준다.

## Picard Group의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $$X$$의 *Picard group* $$\operatorname{Pic}(X)$$는 $$X$$ 위의 line bundle들의 isomorphism class들의 집합이다. Group 연산은 tensor product $$[\mathcal{L}] \cdot [\mathcal{M}] = [\mathcal{L} \otimes \mathcal{M}]$$으로 주어진다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\operatorname{Pic}(X)$$는 abelian group이다. 항등원은 $$[\mathcal{O}_X]$$이고, $$[\mathcal{L}]$$의 역원은 $$[\mathcal{L}^\vee]$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

- **항등원**: [\[Line Bundles\] §명제 6](/ko/math/algebraic_geometry/line_bundles#prop6)에서 $$\mathcal{L} \otimes \mathcal{O}_X \cong \mathcal{L}$$이다.
- **역원**: [\[Line Bundles\] §명제 8](/ko/math/algebraic_geometry/line_bundles#prop8)에서 $$\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$$이다.
- **교환법칙**: Tensor product는 commutative이므로 $$\mathcal{L} \otimes \mathcal{M} \cong \mathcal{M} \otimes \mathcal{L}$$이다.

</details>

## 예시들

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$$\mathbb{A}^n$$의 Picard group**: $$\operatorname{Pic}(\mathbb{A}^n) = 0$$이다. 모든 line bundle이 trivial이기 때문이다. 이는 [\[Line Bundles\] §예시 11](/ko/math/algebraic_geometry/line_bundles#ex11)에서 이미 보였다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **$$\mathbb{P}^n$$의 Picard group**: $$\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$$이다. 생성원은 hyperplane bundle $$\mathcal{O}_{\mathbb{P}^n}(1)$$이다. 임의의 line bundle은 $$\mathcal{O}_{\mathbb{P}^n}(d)$$ for some $$d \in \mathbb{Z}$$와 동형이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **곡선의 Picard group**: 기약 projective curve $$C$$에 대해, $$\operatorname{Pic}(C)$$는 $$C$$ 위의 점들로 생성되는 group이다. Degree map $$\deg: \operatorname{Pic}(C) \to \mathbb{Z}$$가 존재하며, 그 kernel $$\operatorname{Pic}^0(C)$$는 $$C$$ 위의 degree 0인 divisor class들의 group이다. $$\operatorname{Pic}^0(C)$$는 본질적으로 $$C$$ 자체와 같은 "차원을 갖는" group이며, *Jacobian variety*[^jacobian]라 부른다. 이는 curve 자체와 같은 "차원"을 가진 group으로, degree 0인 divisor class들의 집합이 abelian variety를 이룬다는 사실은 매우 강력한 결과이다. 이 구조는 curve 위의 선형 계(linear system)를 이해하고, Riemann–Roch 정리를 통해 global sections의 차원을 계산하는 데 핵심적으로 사용된다.

[^jacobian]: *Jacobian variety* $$J(C)$$는 곡선 $$C$$에 대응되는 abelian variety로, $$\operatorname{Pic}^0(C)$$와 자연스럽게 동일시된다. 즉, degree 0인 divisor class들의 group이 곡선의 기하학적 성질을 반영하는 대수군(algebraic group)을 이룬다.

</div>

## Picard Group과 Divisor Class Group

[\[Line Bundles\] §명제 16](/ko/math/algebraic_geometry/line_bundles#prop16)에서 우리는 smooth variety $$X$$에 대해 $$\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$$임을 보였다. 이 동형의 구체적인 의미를 살펴보자. Cartier divisor $$D = \{(U_i, f_i)\}$$에 대응하는 line bundle $$\mathcal{O}_X(D)$$는 transition functions $$g_{ij} = f_i/f_j$$를 가지며, 이 대응 $$D \mapsto \mathcal{O}_X(D)$$은 group isomorphism $$\operatorname{Cl}(X) \xrightarrow{\sim} \operatorname{Pic}(X)$$을 유도한다[^cl-pic].

[^cl-pic]: 이 동형의 의미는 다음과 같다. Divisor $$D$$는 "다양체를 나누는 hypersurface"이고, $$\mathcal{O}_X(D)$$는 "이 hypersurface에 수직인 line bundle"이다. Principal divisor $$\operatorname{div}(f)$$는 trivial bundle에 대응되고, 일반적인 divisor는 nontrivial bundle에 대응된다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **$$\mathbb{P}^n$$에서의 대응**: Hyperplane divisor $$H = V(\x_0)$$에 대응하는 line bundle은 $$\mathcal{O}_{\mathbb{P}^n}(1)$$이다. 일반적으로 divisor $$dH$$에 대응하는 line bundle은 $$\mathcal{O}_{\mathbb{P}^n}(d)$$이다. 이는 [\[Divisors\] §예시 10](/ko/math/algebraic_geometry/divisors#ex10)에서 $$\operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$$임과 일치한다.

</div>

## Pullback of Line Bundles

기하학적으로, morphism $$\varphi: X \to Y$$를 따라 divisor class를 "가져오는" 연산은 매우 자연스럽다. 예를 들어, $$Y$$ 위의 hypersurface를 $$\varphi$$에 의해 $$X$$ 위로 당기면, 이에 대응하는 line bundle도 함께 당겨져야 한다. 이 pullback 연산은 언제나 잘 정의되며, $$\varphi^\ast$$는 $$\operatorname{Pic}(Y)$$에서 $$\operatorname{Pic}(X)$$로의 group homomorphism을 유도한다. 이는 특히 embedding의 경우 중요한데, ambient space의 line bundle을 부분다양체로 제한하는 것은 global sections의 자연스러운 추론으로 이어진다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Morphism $$\varphi: X \to Y$$와 $$Y$$ 위의 line bundle $$\mathcal{L}$$에 대하여, *pullback* $$\varphi^\ast \mathcal{L}$$은 $$X$$ 위의 line bundle이다. 그 transition functions은 $$\{g_{ij} \circ \varphi\}$$이다. 여기서 $$\{g_{ij}\}$$는 $$\mathcal{L}$$의 transition functions이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Line bundle $$\mathcal{L}$$이 open cover $$\{U_i\}$$ 위에서 transition functions $$\{g_{ij}\}$$로 주어졌다고 하자. Pullback $$\varphi^\ast \mathcal{L}$$은 open cover $$\{\varphi^{-1}(U_i)\}$$ 위에서 transition functions $$\{g_{ij} \circ \varphi\}$$로 정의된다. $$\varphi^\ast \mathcal{L}$$이 $$X$$ 위의 line bundle임을 확인하려면, transition function들이 cocycle 조건을 만족하면 된다.

$$$(g_{ik} \circ \varphi) = (g_{ij} \circ \varphi)(g_{jk} \circ \varphi)$$

이 식은 원래의 cocycle 조건 $$g_{ik} = g_{ij} \cdot g_{jk}$$에서 $$\varphi$$를 compose한 것과 동일하므로 성립한다.

</details>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Pullback은 group homomorphism $$\varphi^\ast: \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$$를 유도한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast \mathcal{L} \otimes \varphi^\ast \mathcal{M}$$이고 $$\varphi^\ast \mathcal{O}_Y \cong \mathcal{O}_X$$이므로, pullback은 group homomorphism이다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Embedding의 pullback**: Embedding $$i: C \hookrightarrow \mathbb{P}^n$$에 대해, $$i^\ast \mathcal{O}_{\mathbb{P}^n}(1)$$은 curve $$C$$ 위의 line bundle이다. 이를 $$C$$ 위의 *hyperplane bundle*이라 부르며, $$\mathcal{O}_C(1)$$로 표기한다.

</div>

## Picard Group의 계산

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Affine variety $$X$$에 대해, $$\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$$이다. 만약 $$X$$의 coordinate ring가 unique factorization domain이면 $$\operatorname{Pic}(X) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$의 coordinate ring가 UFD이면 모든 *height 1 prime ideal*[^height]은 principal이다. 따라서 모든 Weil divisor가 principal divisor와 동치이고, $$\operatorname{Cl}(X) = 0$$이다. [\[Line Bundles\] §명제 16](/ko/math/algebraic_geometry/line_bundles#prop16)에 의해 $$\operatorname{Pic}(X) \cong \operatorname{Cl}(X) = 0$$이다.

[^height]: Prime ideal $$\mathfrak{p}$$의 *height*는 $$\mathfrak{p}$$를 포함하는 prime ideal chain의 최대 길이이다. Height 1 prime ideal은 $$(0) \subsetneq \mathfrak{p}$$가 최대 chain인 prime ideal을 의미하며, 이는 기하학적으로 irreducible hypersurface에 대응된다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Smooth quadric surface**: $$X = V(\x_0 \x_3 - \x_1 \x_2) \subset \mathbb{P}^3$$는 $$\mathbb{P}^1 \times \mathbb{P}^1$$과 isomorphic하다. 따라서

$$\operatorname{Pic}(X) \cong \operatorname{Pic}(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z} \oplus \mathbb{Z}$$

이다. 두 생성원은 각각 $$\mathbb{P}^1 \times \{\text{point}\}$$와 $$\{\text{point}\} \times \mathbb{P}^1$$에 대응하는 line bundle들이다.

이 결과의 흥미로운 점은, quadric surface 위에는 서로 다른 방향의 두 family의 직선(ruling curve)이 존재하는데, 이 두 family의 divisor class가 서로 독립적이라는 것이다. 즉, 한 family의 line bundle은 다른 family와 직접적으로 얽혀 있지 않으며, 이 Picard group은 일종의 2차원 lattice 구조를 이룬다. 이는 한 가지만으로는 설명할 수 없는 기하학적 복잡성을 보여준다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
