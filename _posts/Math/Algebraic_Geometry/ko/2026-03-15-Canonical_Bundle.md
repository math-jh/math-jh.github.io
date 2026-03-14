---
title: "Canonical Bundle"
excerpt: "The canonical bundle, canonical divisor, and differential forms"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/canonical_bundle
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Canonical_Bundle.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 13
---

## 도입

미분기하학에서 manifold $M$의 cotangent bundle $T^\ast M$은 중요한 역할을 한다. 대수기하학에서도 비슷하게 **canonical bundle** $\omega_X$를 정의할 수 있으며, 이는 variety $X$의 fundamental invariant이다.

Canonical bundle은 Serre duality, Riemann-Roch theorem 등 핵심적인 정리들에서 등장한다. Smooth curve의 경우 canonical bundle은 genus를 결정하고, higher dimension에서는 variety의 classification에 중요한 정보를 제공한다.

## Differential Forms

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth variety $X$의 점 $p$에서의 **cotangent space** $\Omega_{X,p}$는 $\mathfrak{m}_p / \mathfrak{m}_p^2$의 dual space이다. 여기서 $\mathfrak{m}_p$는 $p$에서의 maximal ideal이다.

</div>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $X$의 **sheaf of differential 1-forms<sub>미분 1형식의 층</sub>** $\Omega_X^1$을 각 점 $p$에서 $\Omega_{X,p}$를 붙여서 얻는 locally free sheaf로 정의한다.

**Sheaf of differential $k$-forms** $\Omega_X^k = \bigwedge^k \Omega_X^1$이다.

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 ($\mathbb{A}^n$)**</ins> $\Omega_{\mathbb{A}^n}^1$은 $dx_1, \ldots, dx_n$으로 생성된 free $\mathcal{O}_{\mathbb{A}^n}$-module이다.

$$\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n} \langle dx_1, \ldots, dx_n \rangle$$

</div>

## Canonical Bundle

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $n$차원 smooth variety $X$의 **canonical bundle<sub>표준 선다발</sub>** $\omega_X$를 top exterior power로 정의한다:

$$\omega_X = \bigwedge^n \Omega_X^1 = \Omega_X^n$$

</div>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> **Canonical divisor<sub>표준 인자</sub>** $K_X$는 $\omega_X \cong \mathcal{O}(K_X)$를 만족하는 divisor이다. 이는 linear equivalence modulo로 well-defined된다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($\mathbb{P}^n$)**</ins> $\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$이다. 따라서 $K_{\mathbb{P}^n} \sim -(n+1)H$이다.

**증명 (sketch)**: $\mathbb{A}^{n+1} \setminus \{0\}$ 위의 differential form $\omega = \sum_{i=0}^{n} (-1)^i x_i dx_0 \wedge \cdots \wedge \widehat{dx_i} \wedge \cdots \wedge dx_n$을 생각하자. 이 form은 $\mathbb{P}^n$ 위에서 pole of order $n+1$을 갖는다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Curve)**</ins> Genus $g$인 smooth projective curve $C$에 대해 $\deg K_C = 2g - 2$이다.

- $g = 0$ (rational curve): $K_C \sim -2p$ (negative degree)
- $g = 1$ (elliptic curve): $K_C \sim 0$ (trivial)
- $g \geq 2$ (general type): $K_C$ is ample

</div>

## Adjunction Formula

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Adjunction Formula)**</ins> Smooth variety $X$의 smooth hypersurface $Y$에 대해:

$$\omega_Y \cong \omega_X|_Y \otimes \mathcal{O}(Y)|_Y$$

또는 divisor level에서:

$$K_Y \sim (K_X + Y)|_Y$$

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($\mathbb{P}^2$ 안의 curve)**</ins> Degree $d$인 smooth curve $C \subset \mathbb{P}^2$에 대해:

$$K_C \sim (K_{\mathbb{P}^2} + C)|_C \sim (-3H + dH)|_C = (d-3)H|_C$$

따라서 $\deg K_C = d(d-3)$이고, genus $g = \frac{(d-1)(d-2)}{2}$이다.

</div>

## Canonical Ring

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> $X$의 **canonical ring<sub>표준환</sub>** $R(X, K_X)$를 다음과 같이 정의한다:

$$R(X, K_X) = \bigoplus_{m \geq 0} \Gamma(X, \omega_X^{\otimes m})$$

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Canonical ring의 성질:
1. $X$가 general type (즉 $\omega_X$가 ample)이면 $R(X, K_X)$는 finitely generated이다.
2. $\dim \operatorname{Proj}(R(X, K_X))$를 $X$의 **Kodaira dimension**이라 한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
