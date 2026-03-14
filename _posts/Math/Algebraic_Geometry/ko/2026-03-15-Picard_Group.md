---
title: "Picard Group"
excerpt: "The Picard group and its relation to line bundles and divisors"

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

## 도입

[§Line Bundles](/ko/math/algebraic_geometry/line_bundles)에서 우리는 line bundle의 개념을 소개하고, smooth variety에서 line bundle과 divisor의 대응을 살펴보았다. 이제 우리는 line bundle들의 "동형류"들이 이루는 군인 **Picard group**을 자세히 연구한다.

Picard group은 다양체 $X$의 중요한 불변량이다. 예를 들어 $\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$이고, $\operatorname{Pic}(\mathbb{A}^n) = 0$이다. 이 차이는 projective space와 affine space의 근본적인 차이를 반영한다.

## Picard Group의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $X$의 **Picard group<sub>Picard 군</sub>** $\operatorname{Pic}(X)$는 $X$ 위의 line bundle들의 isomorphism class들로 구성된 abelian group이다. 연산은 tensor product이고:

- 단위원: trivial line bundle $\mathcal{O}_X$
- 역원: $[L]^{-1} = [L^\ast]$

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $\operatorname{Pic}(X)$는 well-defined abelian group이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Tensor product가 line bundle의 isomorphism class에 대해 well-defined임을 확인해야 한다. $L_1 \cong L_1'$이고 $L_2 \cong L_2'$이면 $L_1 \otimes L_2 \cong L_1' \otimes L_2'$이다.

Associativity: $(L_1 \otimes L_2) \otimes L_3 \cong L_1 \otimes (L_2 \otimes L_3)$
Commutativity: $L_1 \otimes L_2 \cong L_2 \otimes L_1$
Identity: $L \otimes \mathcal{O}_X \cong L$
Inverse: $L \otimes L^\ast \cong \mathcal{O}_X$

</details>

## Exact Sequence

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 다음의 exact sequence가 존재한다:

$$1 \to \mathcal{O}(X)^\ast \to \mathbb{K}(X)^\ast \xrightarrow{\operatorname{div}} \operatorname{Div}(X) \to \operatorname{Pic}(X) \to 0$$

여기서:
- $\mathcal{O}(X)^\ast$는 $X$ 위의 nowhere-vanishing 정칙함수들
- $\mathbb{K}(X)^\ast$는 $X$ 위의 유리함수들
- $\operatorname{div}(f)$는 $f$의 principal divisor

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1. **$\mathcal{O}(X)^\ast \to \mathbb{K}(X)^\ast$가 injective**: 자명하다.

2. **$\operatorname{div}(f) = 0$인 것과 $f \in \mathcal{O}(X)^\ast$인 것은 동치**: $\operatorname{div}(f) = 0$이면 $f$는 영점도 극점도 없으므로 nowhere-vanishing 정칙함수이다.

3. **$\operatorname{div}$의 image가 $\operatorname{Div}(X) \to \operatorname{Pic}(X)$의 kernel**: $D = \operatorname{div}(f)$이면 $\mathcal{O}(D) \cong \mathcal{O}$이다. 반대로 $\mathcal{O}(D) \cong \mathcal{O}$이면 $D = \operatorname{div}(f)$인 $f$가 존재한다.

4. **$\operatorname{Div}(X) \to \operatorname{Pic}(X)$가 surjective**: Smooth variety에서 각 line bundle은 어떤 divisor에 대응한다.

</details>

## 예시들

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (Affine varieties)**</ins> $\mathcal{O}(\mathbb{A}^n)^\ast = \mathbb{K}^\ast$이고 $\operatorname{Cl}(\mathbb{A}^n) = 0$이므로 $\operatorname{Pic}(\mathbb{A}^n) = 0$이다.

더 일반적으로, 모든 smooth affine variety $X$에 대해 $\operatorname{Pic}(X)$는 유한 생성 abelian group이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (Projective space)**</ins> $\mathcal{O}(\mathbb{P}^n)^\ast = \mathbb{K}^\ast$이고 $\operatorname{Cl}(\mathbb{P}^n) \cong \mathbb{Z}$이므로 $\operatorname{Pic}(\mathbb{P}^n) \cong \mathbb{Z}$이다.

생성원은 $\mathcal{O}(1)$이고, 각 $d \in \mathbb{Z}$에 대응하는 line bundle은 $\mathcal{O}(d)$이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (Product)**</ins> $\operatorname{Pic}(X \times Y) \cong \operatorname{Pic}(X) \oplus \operatorname{Pic}(Y)$가 성립하지 않는다!

예: $\operatorname{Pic}(\mathbb{P}^1 \times \mathbb{P}^1) \cong \mathbb{Z} \oplus \mathbb{Z}$이지만, 이는 $\operatorname{Pic}(\mathbb{P}^1) \oplus \operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z} \oplus \mathbb{Z}$와 우연히 일치한다.

더 일반적으로, $\operatorname{Pic}(X \times Y)$는 $\operatorname{Pic}(X) \oplus \operatorname{Pic}(Y)$뿐 아니라 $X$와 $Y$ 사이의 "interaction"을 포함할 수 있다.

</div>

## Functoriality

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Morphism $\varphi: X \to Y$에 대해 pullback map $\varphi^\ast: \operatorname{Pic}(Y) \to \operatorname{Pic}(X)$가 존재한다. 이는 $\varphi^\ast(L) = \varphi^{-1}(L) \otimes_{\varphi^{-1}(\mathcal{O}_Y)} \mathcal{O}_X$로 정의된다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> Embedding $i: \mathbb{P}^1 \hookrightarrow \mathbb{P}^2$에 대해 $i^\ast(\mathcal{O}_{\mathbb{P}^2}(1)) = \mathcal{O}_{\mathbb{P}^1}(1)$이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
