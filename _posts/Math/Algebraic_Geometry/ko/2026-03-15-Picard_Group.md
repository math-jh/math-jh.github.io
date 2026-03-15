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

Picard group은 다양체의 "twisting structure"를 분류하는 중요한 불변량이다. 예를 들어, $\operatorname{Pic}(\mathbb{A}^n) = 0$이지만 $\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$이다. 이는 affine space가 "twist가 없는" 공간인 반면, projective space는 "twist"를 허용한다는 것을 보여준다.

## Picard Group의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 다양체 $X$의 *Picard group* $\operatorname{Pic}(X)$는 $X$ 위의 line bundle들의 isomorphism class들의 집합이다. Group 연산은 tensor product $[\mathcal{L}] \cdot [\mathcal{M}] = [\mathcal{L} \otimes \mathcal{M}]$으로 주어진다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $\operatorname{Pic}(X)$는 abelian group이다. 항등원은 $[\mathcal{O}_X]$이고, $[\mathcal{L}]$의 역원은 $[\mathcal{L}^\vee]$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

- **항등원**: [\[Line Bundles\] §명제 6](/ko/math/algebraic_geometry/line_bundles#prop6)에서 $\mathcal{L} \otimes \mathcal{O}_X \cong \mathcal{L}$이다.
- **역원**: [\[Line Bundles\] §명제 8](/ko/math/algebraic_geometry/line_bundles#prop8)에서 $\mathcal{L} \otimes \mathcal{L}^\vee \cong \mathcal{O}_X$이다.
- **교환법칙**: Tensor product는 commutative이므로 $\mathcal{L} \otimes \mathcal{M} \cong \mathcal{M} \otimes \mathcal{L}$이다.

</details>

## 예시들

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$\mathbb{A}^n$의 Picard group**: $\operatorname{Pic}(\mathbb{A}^n) = 0$이다. 모든 line bundle이 trivial이기 때문이다. 이는 [\[Line Bundles\] §예시 11](/ko/math/algebraic_geometry/line_bundles#ex11)에서 이미 보였다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **$\mathbb{P}^n$의 Picard group**: $\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$이다. 생성원은 hyperplane bundle $\mathcal{O}_{\mathbb{P}^n}(1)$이다. 임의의 line bundle은 $\mathcal{O}_{\mathbb{P}^n}(d)$ for some $d \in \mathbb{Z}$와 동형이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **곡선의 Picard group**: 기약 projective curve $C$에 대해, $\operatorname{Pic}(C)$는 $C$ 위의 점들로 생성되는 group이다. Degree map $\deg: \operatorname{Pic}(C) \to \mathbb{Z}$가 존재하며, 그 kernel은 *Jacobian variety* $J(C)$라 부른다.

</div>

## Picard Group과 Divisor Class Group

[\[Line Bundles\] §명제 16](/ko/math/algebraic_geometry/line_bundles#prop16)에서 우리는 smooth variety $X$에 대해 $\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$임을 보였다. 이 절에서는 이 동형의 구체적인 의미를 살펴보자.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Cartier divisor $D = \{(U_i, f_i)\}$에 대하여, line bundle $\mathcal{O}_X(D)$의 transition functions은 $g_{ij} = f_i/f_j$이다. 이 대응 $D \mapsto \mathcal{O}_X(D)$은 $\operatorname{Cl}(X)$에서 $\operatorname{Pic}(X)$로의 group isomorphism을 유도한다.

</div>

이 동형의 의미는 다음과 같다. Divisor $D$는 "다양체를 나누는 hypersurface"이고, $\mathcal{O}_X(D)$는 "이 hypersurface에 수직인 line bundle"이다. Principal divisor $\operatorname{div}(f)$는 trivial bundle에 대응되고, 일반적인 divisor는 nontrivial bundle에 대응된다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **$\mathbb{P}^n$에서의 대응**: Hyperplane divisor $H = V(\x_0)$에 대응하는 line bundle은 $\mathcal{O}_{\mathbb{P}^n}(1)$이다. 일반적으로 divisor $dH$에 대응하는 line bundle은 $\mathcal{O}_{\mathbb{P}^n}(d)$이다. 이는 [\[Divisors\] §예시 10](/ko/math/algebraic_geometry/divisors#ex10)에서 $\operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$임과 일치한다.

</div>

## Pullback of Line Bundles

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Morphism $\varphi: X \to Y$와 $Y$ 위의 line bundle $\mathcal{L}$에 대하여, *pullback* $\varphi^\ast \mathcal{L}$은 $X$ 위의 line bundle이다. 그 transition functions은 $\{g_{ij} \circ \varphi\}$이다. 여기서 $\{g_{ij}\}$는 $\mathcal{L}$의 transition functions이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Pullback $\varphi^\ast \mathcal{L}$은 sheaf pullback $\varphi^{-1} \mathcal{L} \otimes_{\varphi^{-1} \mathcal{O}_Y} \mathcal{O}_X$으로 정의된다. Local trivialization $\phi_i: \mathcal{L}|_{U_i} \to \mathcal{O}_{U_i}$에 대해, $\varphi^\ast \mathcal{L}|_{\varphi^{-1}(U_i)} \to \mathcal{O}_{\varphi^{-1}(U_i)}$가 자연스럽게 정의된다. Transition function은 $g_{ij} \circ \varphi$이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Pullback은 group homomorphism $\varphi^\ast: \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$를 유도한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\varphi^\ast(\mathcal{L} \otimes \mathcal{M}) \cong \varphi^\ast \mathcal{L} \otimes \varphi^\ast \mathcal{M}$이고 $\varphi^\ast \mathcal{O}_Y \cong \mathcal{O}_X$이므로, pullback은 group homomorphism이다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **Embedding의 pullback**: Embedding $i: C \hookrightarrow \mathbb{P}^n$에 대해, $i^\ast \mathcal{O}_{\mathbb{P}^n}(1)$은 curve $C$ 위의 line bundle이다. 이를 $C$ 위의 *hyperplane bundle*이라 부르며, $\mathcal{O}_C(1)$로 표기한다.

</div>

## Picard Group의 계산

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Affine variety $X = \operatorname{Spec} A$에 대해, $\operatorname{Pic}(X) \cong \operatorname{Cl}(X)$이다. 만약 $A$가 unique factorization domain이면 $\operatorname{Pic}(X) = 0$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$A$가 UFD이면 모든 height 1 prime ideal은 principal이다. 따라서 모든 Weil divisor가 principal divisor와 동치이고, $\operatorname{Cl}(X) = 0$이다. [\[Line Bundles\] §명제 16](/ko/math/algebraic_geometry/line_bundles#prop16)에 의해 $\operatorname{Pic}(X) \cong \operatorname{Cl}(X) = 0$이다.

</details>

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> **Smooth quadric surface**: $X = V(\x_0 \x_3 - \x_1 \x_2) \subset \mathbb{P}^3$는 $\mathbb{P}^1 \times \mathbb{P}^1$과 isomorphic하다. 따라서

$$\operatorname{Pic}(X) \cong \operatorname{Pic}(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z} \oplus \mathbb{Z}$$

이다. 두 생성원은 각각 $\mathbb{P}^1 \times \{\text{point}\}$와 $\{\text{point}\} \times \mathbb{P}^1$에 대응하는 line bundle들이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
