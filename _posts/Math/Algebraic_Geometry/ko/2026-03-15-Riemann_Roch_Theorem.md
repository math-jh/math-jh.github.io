---
title: "Riemann–Roch Theorem"
excerpt: "The Riemann–Roch theorem for curves and surfaces"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_theorem
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 12
published: false
---

([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))에서 우리는 canonical divisor $$K_X$$와 그에 대응하는 line bundle $$\omega_X$$를 도입하였다. 이제 우리는 이 두 객체를 이용해 **Riemann–Roch 정리**를 서술한다. 이 정리는 divisor와 line bundle 사이의 차원을 연결해 주며, $$\dim H^0(X,\mathcal{L})$$를 계산하는 강력한 도구이다.

Riemann–Roch 정리는 대수기하학에서 가장 중요하고 유명한 정리 중 하나이다. 이 정리는 divisor, line bundle, cohomology 등의 개념을 연결해 주며, 특히 curves와 surfaces에 대해 매우 강력한 결과를 제공한다.

## Riemann–Roch for Smooth Projective Curves

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해 **Riemann–Roch 차원**을
$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$
라고 정의한다.

</div>

이 차원은 $$D$$의 linear system $$\\lvert D \\rvert$$의 dimension과 같다. 즉, $$D$$와 linearly equivalent한 effective divisor들의 수이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> (Riemann–Roch for curves)
$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g,$$
여기서 $$g$$는 $$C$$의 genus, $$K_C$$는 canonical divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우리는 Serre duality ([§Canonical Bundle, ⁋명제 12](/ko/math/algebraic_geometry/canonical_bundle#prop12))를 이용한다.

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee.$$

Euler characteristic는
$$\chi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)).$$

또한 차원 논리를 이용해 $$\chi(\mathcal{O}_C(D)) = \deg D + 1 - g$$임을 알 수 있다 (Riemann–Roch for line bundles). 두 식을 합치면 명제가 얻어진다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> **$$\mathbb{P}^1$$**: $$g = 0$$, $$K_{\mathbb{P}^1} = -2H$$.
Divisor $$D = dH$$에 대해
$$\ell(dH) = d+1 \\quad (d \ge 0), \\qquad \ell(dH) = 0 \\quad (d < 0).$$
Riemann–Roch 식은 $$\ell(dH) - \ell(-2H-dH) = d+1$$를 만족한다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **Genus 1 curve (elliptic curve)**: $$g = 1$$, $$K_C \sim 0$$.
Divisor $$D$$에 대해
$$\ell(D) = \deg D + 1 \\quad (D \ge 0).$$

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> **Genus 2 curve**: $$g = 2$$이면 $$\deg K_C = 2g - 2 = 2$$이다. Canonical divisor $$K_C$$는 두 점의 linear equivalence class이다.
일반적인 점 $$p$$에 대해 $$D = d \cdot p$$라고 하자.
- $$d = 0$$: $$\ell(0) = 1$$ (상수함수만)
- $$d = 1$$: $$\ell(1) = 1$$ (Riemann-Roch: $$\ell(1) - \ell(K_C - 1) = 1 + 1 - 2 = 0$$)
- $$d = 2$$: $$\ell(2) = 2$$일 수 있음 (만약 $$2p \sim K_C$$이면 $$\ell(K_C) = g = 2$$)
- $$d \ge 3$$: $$\deg(K_C - D) = 2 - d < 0$$이므로 $$\ell(K_C - D) = 0$$, 따라서 $$\ell(d) = d - 1$$

</div>

## Riemann–Roch for Smooth Projective Surfaces

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Smooth projective surface $$S$$ 위의 divisor $$D$$에 대해 **Riemann–Roch 차원**을
$$\chi(\mathcal{O}_S(D)) = \sum_{i=0}^2 (-1)^i h^i(S, \mathcal{O}_S(D))$$
라고 정의한다.

</div>

여기서 $$\chi$$는 Euler characteristic이다. $$h^0$$는 global section의 수, $$h^1$$과 $$h^2$$는 cohomology의 dimension이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> (Riemann–Roch for surfaces)
$$\chi(\mathcal{O}_S(D)) = \frac{1}{2} D \cdot (D - K_S) + \chi(\mathcal{O}_S),$$
여기서 $$K_S$$는 canonical divisor, $$\chi(\mathcal{O}_S)=1-q+p_g$$이며 $$q = h^1(S,\mathcal{O}_S)$$, $$p_g = h^2(S,\mathcal{O}_S)$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Hirzebruch–Riemann–Roch theorem을 적용한다.

$$\chi(\mathcal{O}_S(D)) = \int_S \operatorname{ch}(\mathcal{O}_S(D)) \operatorname{td}(T_S).$$

$$\operatorname{ch}(\mathcal{O}_S(D)) = 1 + D + \\tfrac12 D^2$$이고, $$\operatorname{td}(T_S) = 1 + \\tfrac12 K_S + \\tfrac{1}{12}(c_1^2 + c_2)$$. 곱셈 후 차수 2 항만 적분하면 위 식이 얻어진다.

</details>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$\mathbb{P}^2$$**: $$K_{\mathbb{P}^2} = -3H$$, $$\chi(\mathcal{O}_{\mathbb{P}^2}) = 1$$.
Divisor $$D = dH$$에 대해
$$\chi(\mathcal{O}_{\mathbb{P}^2}(d)) = \frac12 d(d+3) + 1.$$
또한 $$h^0 = \binom{d+2}{2}$$, $$h^1 = h^2 = 0$$ for $$d \ge 0$$, 따라서 위 식과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Blow-up of $$\mathbb{P}^2$$**: $$\\pi: \\tilde{\mathbb{P}}^2 \to \mathbb{P}^2$$ at point $$p$$. Let $$E$$ be exceptional divisor.
$$K_{\\tilde{\mathbb{P}}^2} = \\pi^\ast K_{\mathbb{P}^2} + E = -3H + E$$.
$$D = dH - kE$$에 대해
$$\chi(\mathcal{O}_{\\tilde{\mathbb{P}}^2}(dH - kE)) = \frac12 d(d-3) + \frac12 k^2 + 1.$$

</div>

## Applications

### Genus Formula for Plane Curves

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Smooth plane curve $$C \subset \mathbb{P}^2$$ of degree $$d$$에 대해, Adjunction formula ([§Canonical Bundle, ⁋명제 10](/ko/math/algebraic_geometry/canonical_bundle#prop10))와 Riemann–Roch for curves를 조합하면
$$g(C) = \frac{(d-1)(d-2)}{2}.$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Adjunction formula: $$K_C = (d-3)H|_C$$.
Riemann–Roch for $$D = (d-1)H|_C$$:
$$\ell((d-1)H|_C) - \ell(K_C - (d-1)H|_C) = (d-1) + 1 - g.$$
Left side: $$\ell((d-1)H|_C) = \binom{d-1+2}{2} = \frac{d(d-1)}{2}$$ (hyperplane sections), $$K_C - (d-1)H|_C = -2H|_C \sim 0$$, so $$\ell(-2H|_C) = 1$$.
Right side: $$d - g$$.
Thus $$\frac{d(d-1)}{2} - 1 = d - g \\implies g = \frac{(d-1)(d-2)}{2}$$.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> **Degree 3 curve (cubic)**: $$g = \frac{2 \cdot 1}{2} = 1$$ (elliptic curve).
**Degree 4 curve (quartic)**: $$g = \frac{3 \cdot 2}{2} = 3$$.
**Degree 5 curve (quintic)**: $$g = \frac{4 \cdot 3}{2} = 6$$.

</div>

### Noether Formula

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> (Noether Formula) Smooth surface $$S$$에 대해
$$c_1(S)^2 + c_2(S) = 12 \\, \chi(\mathcal{O}_S).$$
이는 Riemann–Roch 식을 $$D=0$$에 적용한 결과와 $$\chi(\mathcal{O}_S)=1 - q + p_g$$를 사용하여 얻는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Hirzebruch–Riemann–Roch theorem을 $$D = 0$$에 적용한다.

$$\chi(\mathcal{O}_S) = \int_S \operatorname{td}(T_S).$$

Todd class는 $$\operatorname{td}(T_S) = 1 + \frac{1}{2}c_1 + \frac{1}{12}(c_1^2 + c_2)$$이고, 여기서 $$c_1 = K_S$$, $$c_2$$는 top Chern class이다. 차수 2 항만 적분하면

$$\chi(\mathcal{O}_S) = \frac{1}{12}(K_S^2 + c_2).$$

따라서 $$K_S^2 + c_2 = 12 \cdot \chi(\mathcal{O}_S)$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$$\mathbb{P}^2$$**: $$K_{\mathbb{P}^2}^2 = 9$$, $$\chi(\mathcal{O}_{\mathbb{P}^2}) = 1$$.
Noether formula: $$c_1^2 + c_2 = 12 \cdot 1 \\implies 9 + c_2 = 12 \\implies c_2 = 3$$. Indeed, $$\mathbb{P}^2$$ has $$c_2 = 3$$ (three lines in general position).

</div>

### Brill-Noether Theory

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> (Brill-Noether) Curve $$C$$ of genus $$g$$ with $$\ell(D) \ge r$$ for divisor $$D$$ of degree $$d$$:
If $$d \ge r + g$$, then $$\ell(D) \ge r$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch gives $$\ell(D) - \ell(K_C - D) = d + 1 - g$$. Since $$\ell(K_C - D) \ge 0$$, we have $$\ell(D) \ge d + 1 - g$$. Setting $$d \ge r + g$$ yields $$\ell(D) \ge r + 1 > r$$ (for $$r \ge 0$$). More refined arguments show equality can hold.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> **$$g=2$$에서의 Brill-Noether**: $$K_C$$는 degree 2를 갖는다. 
- $$d = 2$$, $$r = 1$$: $$d \ge r + g = 3$$이 아니므로 보장되지 않음. 하지만 $$D = K_C$$이면 $$\ell(D) = g = 2 \ge 1$$.
- $$d = 3$$, $$r = 1$$: $$d \ge r + g = 3$$이므로 $$\ell(D) \ge 1$$이 보장됨. 실제로 $$\ell(3) = 2$$ (Riemann-Roch: $$\ell(3) - 0 = 3 + 1 - 2 = 2$$).

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
