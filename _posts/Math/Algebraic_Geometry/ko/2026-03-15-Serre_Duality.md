---
title: "Serre Duality"
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/serre_duality
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Serre_Duality.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 16
published: false
---

## 도입

Serre duality는 projective variety의 cohomology group 사이의 fundamental한 dualilty이다. 이는 finite-dimensional vector space $$V$$와 그 dual $$V^\ast$$ 사이의 관계를 cohomology로 확장한 것이다.

Serre duality는 Riemann-Roch theorem의 증명에 필수적이며, 많은 계산을 단순화한다.

## Statement

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Serre Duality)**</ins> $$n$$차원 smooth projective variety $$X$$ 위의 coherent sheaf $$\mathcal{F}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(X, \mathcal{F}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)^\ast$$

여기서 $$\omega_X$$는 canonical bundle이고 $$\mathcal{F}^\vee = \mathcal{H}om(\mathcal{F}, \mathcal{O}_X)$$는 dual sheaf이다.

</div>

<div class="corollary" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 특히 $$\mathcal{F} = \mathcal{O}_X$$에 대해:

$$H^i(X, \mathcal{O}_X) \cong H^{n-i}(X, \omega_X)^\ast$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Curve)**</ins> Genus $$g$$인 smooth curve $$C$$에 대해:

- $$H^0(C, \mathcal{O}_C) \cong H^1(C, \omega_C)^\ast$$
- $$H^1(C, \mathcal{O}_C) \cong H^0(C, \omega_C)^\ast$$

$$\dim H^0(C, \omega_C) = g$$이므로 $$\dim H^1(C, \mathcal{O}_C) = g$$이다.

</div>

## $$\mathbb{P}^n$$에서의 Serre Duality

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\mathbb{P}^n$$에서 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$이므로:

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$$

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^1$$에서:

$$H^0(\mathbb{P}^1, \mathcal{O}(d)) \cong H^1(\mathbb{P}^1, \mathcal{O}(-d-2))^\ast$$

- $$d = 0$$: $$H^0(\mathcal{O}) = \mathbb{K}$$, $$H^1(\mathcal{O}(-2)) = \mathbb{K}$$
- $$d = 1$$: $$H^0(\mathcal{O}(1)) = \mathbb{K}^2$$, $$H^1(\mathcal{O}(-3)) = \mathbb{K}^2$$

</div>

## Grothendieck Duality

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Grothendieck Duality)**</ins> Proper morphism $$f: X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해:

$$R^i f_\ast(\mathcal{F}) \cong R^{n-i} f_\ast(\mathcal{F} \otimes \omega_{X/Y})^\vee$$

여기서 $$\omega_{X/Y}$$는 relative dualizing sheaf이다.

</div>

<div class="remark" markdown="1">

<ins id="rem7">**참고 7**</ins> Serre duality는 $$Y = \operatorname{Spec}(\mathbb{K})$$인 특수한 경우이다.

</div>

## Trace Map

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> **Trace map** $$\operatorname{Tr}: H^n(X, \omega_X) \to \mathbb{K}$$는 Serre duality의 핵심 구조이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Serre duality isomorphism은 다음과 같이 명시적으로 주어진다:

$$H^i(X, \mathcal{F}) \to H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)^\ast$$

$$\alpha \mapsto \left( \beta \mapsto \operatorname{Tr}(\alpha \cup \beta) \right)$$

여기서 $$\cup$$은 cup product이다.

</div>

## 응용: Euler Characteristic

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Serre duality에 의해:

$$\chi(\mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Curve)**</ins> Curve $$C$$와 divisor $$D$$에 대해:

$$\chi(\mathcal{O}(D)) = \dim H^0(\mathcal{O}(D)) - \dim H^1(\mathcal{O}(D))$$

$$= \dim H^0(\mathcal{O}(D)) - \dim H^0(\omega_C \otimes \mathcal{O}(-D))$$

이것이 Riemann-Roch theorem의 핵심이다.

</div>

## Relative Duality

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Smooth projective morphism $$f: X \to Y$$에 대해:

$$R f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

</div>

이 정리는 relative situation에서도 "top cohomology of canonical sheaf = 1"이라는 직관을 일반화한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.
