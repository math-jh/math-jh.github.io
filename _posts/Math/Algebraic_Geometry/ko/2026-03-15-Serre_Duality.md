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
last_modified_at: 2026-03-31
weight: 16
published: false
---

## 도입

Serre duality는 projective variety의 cohomology group 사이의 fundamental한 duality이다. 이는 finite-dimensional vector space $$V$$와 그 dual $$V^\ast$$ 사이의 관계를 cohomology로 확장한 것이다. 구체적으로, $$n$$차원 variety $$X$$ 위에서 $$i$$차 cohomology $$H^i(X, \mathcal{F})$$와 $$(n-i)$$차 cohomology $$H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$ 사이에 자연스러운 쌍대성이 성립한다는 것이 Serre duality의 핵심이다. 여기서 canonical bundle $$\omega_X$$가 $$i$$와 $$n-i$$를 연결하는 "교량" 역할을 하며, trace map이 이 쌍대성을 실제로 구현한다.

Serre duality는 Riemann-Roch theorem의 증명에 필수적이며, 많은 계산을 단순화한다. Coherent sheaf cohomology의 기본이 되는 도구이며 ([§Sheaf Cohomology](/ko/math/algebraic_geometry/sheaf_cohomology)), 본 글에서는 그 정의와 주요 응용을 다룬다.

## Statement

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Serre Duality)**</ins> $$n$$차원 smooth projective variety $$X$$ 위의 coherent sheaf $$\mathcal{F}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(X, \mathcal{F}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)^\ast$$

여기서 $$\omega_X$$는 canonical bundle ([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))이고 $$\mathcal{F}^\vee = \mathcal{H}om(\mathcal{F}, \mathcal{O}_X)$$는 dual sheaf이다.

</div>

Serre duality의 증명은 매우 깊은 정리로, 여러 가지 접근법이 존재한다. 대표적으로, Čech cohomology와 Godement resolution을 결합하여 trace map을 명시적으로 구성하는 Hartshorne의 방법과, derived category에서 $$\omega_X = f^! \mathcal{O}_{\operatorname{Spec}(\mathbb{K})}$$로 정의한 뒤 derived adjunction $$(f^\ast, f^!)$$으로 자연스럽게 duality를 얻는 Grothendieck-Verdier의 방법이 있다. 두 방법 모두 본질적으로 "위에서 $$n$$차 cohomology를 취하면 기저필드 $$\mathbb{K}$$로 가는 비퇴화 쌍선형 형식이 존재한다"는 사실을 핵심으로 삼는다.

<div class="corollary" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 특히 $$\mathcal{F} = \mathcal{O}_X$$에 대해:

$$H^i(X, \mathcal{O}_X) \cong H^{n-i}(X, \omega_X)^\ast$$

</div>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Curve)**</ins> Genus $$g$$인 smooth curve $$C$$에 대해. 여기서 genus는 $$g = h^1(C, \mathcal{O}_C)$$로 정의된다.

- $$H^0(C, \mathcal{O}_C) \cong H^1(C, \omega_C)^\ast$$
- $$H^1(C, \mathcal{O}_C) \cong H^0(C, \omega_C)^\ast$$

$$\dim H^0(C, \omega_C) = g$$이므로 $$\dim H^1(C, \mathcal{O}_C) = g$$이다.

</div>

## $$\mathbb{P}^n$$에서의 Serre Duality

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\mathbb{P}^n$$에서 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$ ([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))이므로:

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$$

**증명.** $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$이므로 $$\omega_{\mathbb{P}^n} \otimes \mathcal{O}(d)^\vee \cong \mathcal{O}(-n-1-d)$$이다. [명제 1](#prop1)에 의해

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$$

을 얻는다. 오른쪽의 차원은 [§Cohomology of Line Bundles on projective spaces](/ko/math/algebraic_geometry/cohomology_of_line_bundles)의 Bott's formula로 계산할 수 있다. $$\square$$

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^1$$에서:

$$H^0(\mathbb{P}^1, \mathcal{O}(d)) \cong H^1(\mathbb{P}^1, \mathcal{O}(-d-2))^\ast$$

- $$d = 0$$: $$H^0(\mathcal{O}) = \mathbb{K}$$, $$H^1(\mathcal{O}(-2)) = \mathbb{K}$$
- $$d = 1$$: $$H^0(\mathcal{O}(1)) = \mathbb{K}^2$$, $$H^1(\mathcal{O}(-3)) = \mathbb{K}^2$$

</div>

## Grothendieck Duality

Serre duality는 $$Y = \operatorname{Spec}(\mathbb{K})$$로의 상사상에 대한 특수한 경우이다. Grothendieck는 이를 임의의 proper morphism으로 일반화하였다. Proper morphism $$f \colon X \to Y$$는 위상수학적으로 compact map의 대수기하학적 대응물로, 임의의 base change에 대해 닫힌 사상(closed map)이 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 $$X \to Y$$의 "canonical sheaf"로, Serre duality에서 $$\omega_X$$가 하던 역할을 상대적인 상황으로 옮긴 것이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Grothendieck Duality)**</ins> Proper morphism $$f: X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해:

$$R^i f_\ast(\mathcal{F}) \cong R^{n-i} f_\ast(\mathcal{F} \otimes \omega_{X/Y})^\vee$$

여기서 $$\omega_{X/Y}$$는 relative dualizing sheaf이다.

</div>

Grothendieck duality는 Serre duality보다 훨씬 더 일반적인 정리로, derived category의 언어로 가장 자연스럽게 표현된다. 본 글에서는 정리의 형태만 소개하며, 증명과 상세한 논의는 추후 별도의 글에서 다룬다.

<div class="remark" markdown="1">

<ins id="rem7">**참고 7**</ins> Serre duality는 $$Y = \operatorname{Spec}(\mathbb{K})$$인 특수한 경우이다.

</div>

## Trace Map

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> **Trace map** $$\operatorname{Tr} \colon H^n(X, \omega_X) \to \mathbb{K}$$는 Serre duality의 핵심 구조이다.

Serre duality의 isomorphism이 실제로 작동하려면, $$i = n$$일 때 $$H^n(X, \omega_X)$$와 $$\mathbb{K}$$ 사이의 비퇴화 쌍선형 형식이 필요하다. Trace map은 정확히 이 역할을 한다. 직관적으로, $$H^n(X, \omega_X)$$는 variety $$X$$ 전체에 걸쳐 "적분"을 수행하는 공간이며, trace map은 이 적분을 기저필드 $$\mathbb{K}$$의 원소로 평가하는 것이다. 이 쌍선형 형식의 비퇴화성이 Serre duality 전체를 떠받치는 기둥이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Serre duality isomorphism은 다음과 같이 명시적으로 주어진다:

$$H^i(X, \mathcal{F}) \to H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)^\ast$$

$$\alpha \mapsto \left( \beta \mapsto \operatorname{Tr}(\alpha \cup \beta) \right)$$

여기서 $$\cup$$은 **cup product**로, cohomology class $$\alpha \in H^i(X, \mathcal{F})$$와 $$\beta \in H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$로부터 $$H^n(X, \omega_X)$$의 원소를 만들어내는 쌍선형 곱셈이다. Coherent sheaf cohomology의 cup product는 sheaf resolution의 수준에서 정의되며, $$\mathcal{F} \otimes \mathcal{F}^\vee \to \mathcal{O}_X$$라는 평가 사상(evalutation map)을 거쳐 $$\omega_X$$의 $$n$$차 cohomology에 도달한다.

</div>

## 응용: Euler Characteristic

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Serre duality에 의해:

$$\chi(\mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{F}) = \sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$

**증명.** [명제 1](#prop1)에 의해 $$\dim H^i(X, \mathcal{F}) = \dim H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$이므로, 치환 $$j = n - i$$를 적용하면

$$\sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee) = \sum_{j=0}^{n} (-1)^{n-j} \dim H^j(X, \omega_X \otimes \mathcal{F}^\vee) = (-1)^n \chi(\omega_X \otimes \mathcal{F}^\vee)$$

이고, Serre duality의 대칭성으로부터 $$\chi(\mathcal{F}) = (-1)^n \chi(\omega_X \otimes \mathcal{F}^\vee)$$임이 알려져 있으므로 양변이 일치한다. $$\square$$

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Curve)**</ins> Curve $$C$$와 divisor $$D$$에 대해:

$$\chi(\mathcal{O}(D)) = \dim H^0(\mathcal{O}(D)) - \dim H^1(\mathcal{O}(D))$$

$$= \dim H^0(\mathcal{O}(D)) - \dim H^0(\omega_C \otimes \mathcal{O}(-D))$$

이것이 Riemann-Roch theorem의 핵심이다.

</div>

## Relative Duality

Smooth projective morphism $$f \colon X \to Y$$는 임의의 점 $$y \in Y$$에 대해 섬유 $$f^{-1}(y)$$가 smooth projective variety가 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 이런 상황에서 섬유별 canonical sheaf를 일관되게 모아둔 것이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Smooth projective morphism $$f: X \to Y$$에 대해:

$$R f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

</div>

이 정리는 relative situation에서도 "top cohomology of canonical sheaf = 1"이라는 직관을 일반화한다. $$R f_\ast$$는 derived pushforward로, [명제 6](#prop6)의 $$R^i f_\ast$$를 모아둔 것이다. Relative duality의 증명과 응용에 대해서는 추후 별도의 글에서 다룬다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.
