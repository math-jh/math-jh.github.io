---
title: "Cohomology of Line Bundles on P^n"
excerpt: "Bott's formula and the cohomology of $$\mathcal{O}(d)$$ on projective space"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/cohomology_of_line_bundles
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Cohomology_of_Line_Bundles.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 18
---

## 도입

Projective space $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$의 cohomology는 완전히 계산된다. 이 계산은 대수기하학의 기본적인 도구이며, Serre duality, Riemann-Roch theorem 등의 응용에서 필수적이다.

## Bott's Formula

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Bott's Formula)**</ins> $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}(d)$$의 cohomology는 다음과 같다:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) = \begin{cases}
\mathbb{K}[x_0, \ldots, x_n]_d & q = 0, d \geq 0 \\
\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1} & q = n, d \leq -n-1 \\
0 & \text{otherwise}
\end{cases}$$

</div>

<div class="remark" markdown="1">

<ins id="rem2">**참고 2**</ins> 위 식에서 $$\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_{-d-n-1}$$은 degree $$-d-n-1$$의 "negative degree" monomial들의 공간이다. 예를 들어:

$$\mathbb{K}[x_0^{-1}, \ldots, x_n^{-1}]_k = \operatorname{Span}\{x_0^{a_0} \cdots x_n^{a_n} : a_i < 0, \sum a_i = k\}$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 ($$\mathbb{P}^1$$)**</ins>

- $$H^0(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[x_0, x_1]_d$$ for $$d \geq 0$$ (dimension $$d+1$$)
- $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = 0$$ for $$d \geq -1$$
- $$H^1(\mathbb{P}^1, \mathcal{O}(d)) = \mathbb{K}[x_0^{-1}, x_1^{-1}]_{-d-2}$$ for $$d \leq -2$$ (dimension $$-d-1$$)

예: $$H^1(\mathbb{P}^1, \mathcal{O}(-3))$$은 basis $$\{x_0^{-2}x_1^{-1}, x_0^{-1}x_1^{-2}\}$$를 갖고 dimension 2이다.

</div>

## Euler Characteristic

<div class="corollary" markdown="1">

<ins id="cor4">**따름정리 4**</ins> $$\mathbb{P}^n$$ 위의 $$\mathcal{O}(d)$$의 Euler characteristic:

$$\chi(\mathbb{P}^n, \mathcal{O}(d)) = \binom{n+d}{n}$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Bott's formula에서 $$H^0$$만 non-zero인 경우를 고려하면:

$$\chi(\mathcal{O}(d)) = \dim H^0(\mathcal{O}(d)) = \dim \mathbb{K}[x_0, \ldots, x_n]_d = \binom{n+d}{n}$$

$$H^n$$이 non-zero인 경우도 Euler characteristic에는 같은 formula가 적용된다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^2$$ 위의 $$\mathcal{O}(d)$$에 대해:

$$\chi(\mathcal{O}(d)) = \frac{(d+1)(d+2)}{2}$$

- $$\chi(\mathcal{O}(0)) = 1$$
- $$\chi(\mathcal{O}(1)) = 3$$
- $$\chi(\mathcal{O}(2)) = 6$$

</div>

## Čech Cohomology를 통한 계산

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\mathbb{P}^n$$의 standard affine cover $$\mathfrak{U} = \{U_0, \ldots, U_n\}$$을 사용하면:

$$H^q(\mathbb{P}^n, \mathcal{O}(d)) \cong \check{H}^q(\mathfrak{U}, \mathcal{O}(d))$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 intersection $$U_{i_0 \cdots i_p} = U_{i_0} \cap \cdots \cap U_{i_p}$$는 affine이고, $$\mathcal{O}(d)$$는 quasi-coherent이므로 Leray's theorem에 의해 Čech cohomology가 sheaf cohomology와 일치한다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Explicit calculation for $$\mathbb{P}^1$$)**</ins>

$$\mathfrak{U} = \{U_0, U_1\}$$에 대해:

- $$C^0 = \mathcal{O}(d)(U_0) \oplus \mathcal{O}(d)(U_1)$$
- $$C^1 = \mathcal{O}(d)(U_0 \cap U_1)$$

$$U_0 \cong \mathbb{A}^1$$이고 coordinate $$t = x_1/x_0$$를 사용하면 $$\mathcal{O}(d)(U_0 \cap U_1)$$는 $$\mathbb{K}[t, t^{-1}] \cdot t^{-d}$$이다.

Coboundary map을 계산하면 Bott's formula를 얻는다.

</div>

## Regularity

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Coherent sheaf $$\mathcal{F}$$ on $$\mathbb{P}^n$$이 **$$m$$-regular**라는 것은 $$i > 0$$에 대해 $$H^i(\mathbb{P}^n, \mathcal{F}(m-i)) = 0$$인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Castelnuovo-Mumford Regularity)**</ins> $$\mathcal{F}$$가 $$m$$-regular이면:
1. $$\mathcal{F}(m)$$은 globally generated
2. $$H^i(\mathbb{P}^n, \mathcal{F}(k)) = 0$$ for $$i > 0$$ and $$k \geq m - i$$

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Bot]** R. Bott, *Homogeneous vector bundles*, Annals of Mathematics, 1957.
