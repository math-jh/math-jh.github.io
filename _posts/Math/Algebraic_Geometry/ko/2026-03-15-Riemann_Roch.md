---
title: "Riemann-Roch Theorem"
excerpt: "The Riemann-Roch theorem for curves and surfaces"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 14
---

## 도입

**Riemann-Roch theorem**은 대수기하학에서 가장 중요한 정리 중 하나이다. 이 정리는 curve 위의 divisor $D$에 대해 $\dim |D|$를 계산하는 공식을 제공한다.

간단히 말해, Riemann-Roch는 다음 질문에 답한다: "주어진 divisor $D$에 대해, 얼마나 많은 section이 $\mathcal{O}(D)$에 존재하는가?"

## Curve를 위한 Riemann-Roch

<div class="theorem" markdown="1">

<ins id="thm1">**정리 1 (Riemann-Roch for Curves)**</ins> Genus $g$인 smooth projective curve $C$와 divisor $D$에 대해:

$$\dim |D| - \dim |K_C - D| = \deg D - g + 1$$

또는 equivalently:

$$\dim \Gamma(C, \mathcal{O}(D)) - \dim \Gamma(C, \omega_C \otimes \mathcal{O}(-D)) = \deg D - g + 1$$

</div>

<details class="proof" markdown="1">
<summary>증명 (Sketch)</summary>

Serre duality에 의해 $\Gamma(C, \omega_C \otimes \mathcal{O}(-D)) \cong \Gamma(C, \mathcal{O}(D))^\ast$이다. Euler characteristic을 사용하면:

$$\chi(\mathcal{O}(D)) = \dim \Gamma(C, \mathcal{O}(D)) - \dim H^1(C, \mathcal{O}(D))$$

그리고 Serre duality로부터:

$$\chi(\mathcal{O}(D)) = \deg D + 1 - g$$

이 두 식을 결합하면 Riemann-Roch를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex2">**예시 2 ($\deg D > 2g - 2$)**</ins> $\deg D > \deg K_C = 2g - 2$이면 $\deg(K_C - D) < 0$이므로 $|K_C - D| = \emptyset$이다. 따라서:

$$\dim |D| = \deg D - g + 1$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Rational curve)**</ins> $g = 0$이면 $K_C \sim -2p$이고 $\deg K_C = -2$이다.

- $\deg D \geq 0$이면 $\dim |D| = \deg D + 1$
- 예: $|p|$는 1차원 (점 하나를 지나는 "유일한" divisor 없음)
- $|2p|$는 2차원 → $\mathbb{P}^1 \to \mathbb{P}^2$ map 정의 가능

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (Elliptic curve)**</ins> $g = 1$이면 $K_C \sim 0$이다.

- $\deg D = 0$: $\dim |D| = 0$ 또는 $-1$
- $\deg D = 1$: $\dim |D| = 1$ (각 점 $p$에 대해 $|p| = \{p\}$)
- $\deg D \geq 2$: $\dim |D| = \deg D$

</div>

## Surface를 위한 Riemann-Roch

<div class="theorem" markdown="1">

<ins id="thm5">**정리 5 (Riemann-Roch for Surfaces)**</ins> Smooth projective surface $S$와 divisor $D$에 대해:

$$\chi(\mathcal{O}(D)) = \chi(\mathcal{O}_S) + \frac{1}{2}(D^2 - D \cdot K_S)$$

여기서:
- $D^2$는 self-intersection number
- $D \cdot K_S$는 canonical divisor와의 intersection
- $\chi(\mathcal{O}_S) = 1 - h^1(S, \mathcal{O}_S) + h^2(S, \mathcal{O}_S)$

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($\mathbb{P}^2$)**</ins> $\mathbb{P}^2$에 대해 $K_{\mathbb{P}^2} = -3H$이고 $\chi(\mathcal{O}_{\mathbb{P}^2}) = 1$이다.

Degree $d$인 curve $C = dH$에 대해:

$$\chi(\mathcal{O}(C)) = 1 + \frac{1}{2}(d^2 - d \cdot (-3)) = 1 + \frac{d(d+3)}{2}$$

</div>

## Serre Duality

<div class="theorem" markdown="1">

<ins id="thm7">**정리 7 (Serre Duality)**</ins> $n$차원 smooth projective variety $X$와 coherent sheaf $\mathcal{F}$에 대해:

$$H^i(X, \mathcal{F}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\ast)^\ast$$

</div>

<div class="corollary" markdown="1">

<ins id="cor8">**따름정리 8**</ins> Curve $C$와 divisor $D$에 대해:

$$H^1(C, \mathcal{O}(D)) \cong \Gamma(C, \omega_C \otimes \mathcal{O}(-D))^\ast$$

</div>

이 따름정리가 Riemann-Roch의 $\dim |K_C - D|$ 항을 설명한다.

## 응용: Canonical Embedding

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Genus $g \geq 2$인 curve $C$에 대해, $|K_C|$는 base-point-free이고 canonical map $\varphi_{|K_C|}: C \to \mathbb{P}^{g-1}$을 정의한다.

$C$가 hyperelliptic이 아니면 $\varphi_{|K_C|}$는 embedding이다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (Genus 3)**</ins> $g = 3$인 curve $C$에 대해:
- $\deg K_C = 4$
- $\dim |K_C| = 2$
- $\varphi_{|K_C|}: C \to \mathbb{P}^2$

$C$가 hyperelliptic이 아니면 이 map은 degree 4의 plane curve로 embedding한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Mir]** R. Miranda, *Algebraic Curves and Riemann Surfaces*, Graduate Studies in Mathematics, AMS, 1995.
