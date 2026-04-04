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
weight: 15
published: false
---

Finite-dimensional vector space $$V$$와 그 dual $$V^\ast$$ 사이에는 자연스러운 쌍대성이 존재한다. Serre duality는 이 관계를 cohomology로 확장한 것이다. 구체적으로, field $$\mathbb{K}$$ 위의 $$n$$차원 smooth projective variety $$X$$ 위에서 $$i$$차 cohomology $$H^i(X, \mathcal{E})$$와 $$(n-i)$$차 cohomology $$H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$ 사이에 자연스러운 쌍대성이 성립한다. 여기서 canonical bundle $$\omega_X$$가 $$i$$와 $$n-i$$를 연결하는 교량 역할을 하며, trace map이 이 쌍대성을 실제로 구현한다.

이 duality는 Riemann-Roch theorem의 증명에 필수적이며, cohomology group의 계산을 크게 단순화한다. 본 글에서는 Serre duality의 정의와 그 주요 응용을 다룬다. ([§Sheaf Cohomology, ⁋정의 2](/ko/math/algebraic_geometry/sheaf_cohomology#def2))

## Statement

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Serre Duality)**</ins> Field $$\mathbb{K}$$ 위의 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

여기서 $$\omega_X$$는 canonical bundle ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))이고 $$\mathcal{E}^\vee = \mathcal{H}om(\mathcal{E}, \mathcal{O}_X)$$는 dual sheaf이다.

</div>

Locally free sheaf $$\mathcal{E}$$에 대해서는 $$\mathcal{H}om(\mathcal{E}, \omega_X) \cong \omega_X \otimes \mathcal{E}^\vee$$가 성립하므로 ([§선다발과 벡터다발, ⁋명제 7](/ko/math/algebraic_geometry/line_bundles#prop7)), 명제의 우변을 $$H^{n-i}(X, \mathcal{H}om(\mathcal{E}, \omega_X))^\ast$$와 같이 쓸 수도 있다. 일반적인 coherent sheaf $$\mathcal{F}$$에 대해서는 $$\omega_X \otimes \mathcal{F}^\vee$$ 대신 Ext group $$\operatorname{Ext}^i(\mathcal{F}, \omega_X)$$를 사용하여 $$\operatorname{Ext}^{n-i}(\mathcal{F}, \omega_X) \cong H^i(X, \mathcal{F})^\ast$$의 형태로 동일한 duality가 성립하지만, 본 글에서는 locally free sheaf에 대한 버전을 다룬다. 또한 Hartshorne의 고전적 증명에서는 $$\mathbb{K}$$가 algebraically closed field라고 가정하지만, Grothendieck duality를 사용하면 임의의 field에 대해 동일한 결과가 성립한다.

Serre duality의 증명은 깊은 정리로, 여러 가지 접근법이 존재한다. 대표적으로, projective space에서의 계산을 바탕으로 finite morphism을 통해 일반적인 variety로 확장하는 방법과, derived category에서 $$\omega_X = f^! \mathcal{O}_{\operatorname{Spec}(\mathbb{K})}$$로 정의한 뒤 derived adjunction으로 duality를 얻는 방법이 있다. 두 방법 모두 본질적으로 동일한 핵심 사실에 기반한다. 즉, $$n$$차 cohomology $$H^n(X, \omega_X)$$와 기저필드 $$\mathbb{K}$$ 사이에 isomorphism (trace map)이 존재하며, 이를 통해 cup product pairing이 완벽한 쌍대성을 이룬다는 것이다.

<div class="corollary" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 특히 $$\mathcal{E} = \mathcal{O}_X$$에 대해:

$$H^i(X, \mathcal{O}_X) \cong H^{n-i}(X, \omega_X)^\ast$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{O}_X^\vee = \mathcal{H}om(\mathcal{O}_X, \mathcal{O}_X) \cong \mathcal{O}_X$$이므로, [명제 1](#prop1)에서 $$\mathcal{E} = \mathcal{O}_X$$를 대입하면 $$\omega_X \otimes \mathcal{O}_X^\vee \cong \omega_X$$를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Curve)**</ins> Genus $$g$$인 smooth curve $$C$$를 생각하자. 여기서 genus는 $$g = \dim H^1(C, \mathcal{O}_C)$$로 정의된다. $$C$$는 $$1$$차원이므로 [따름정리 2](#cor2)에서 $$n = 1$$을 대입하면 다음을 얻는다.

$$H^0(C, \mathcal{O}_C) \cong H^1(C, \omega_C)^\ast$$이고 $$H^1(C, \mathcal{O}_C) \cong H^0(C, \omega_C)^\ast$$이다.

첫 번째 동형에서 $$\dim H^0(C, \mathcal{O}_C) = 1$$이므로 $$\dim H^1(C, \omega_C) = 1$$이고, 두 번째 동형에서 $$\dim H^0(C, \omega_C) = \dim H^1(C, \mathcal{O}_C)^\ast = g$$이다. 즉 canonical bundle $$\omega_C$$의 global section의 차원이 정확히 genus $$g$$와 같다. 이는 Riemann-Roch theorem의 기초가 되는 관측이다.

</div>

## $$\mathbb{P}^n$$에서의 Serre Duality

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\mathbb{P}^n$$에서 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$ ([§Canonical Bundle, ⁋예시 8](/ko/math/algebraic_geometry/canonical_bundle#ex8))이므로:

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$$

**증명.** $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$이므로 $$\mathcal{O}(d)^\vee \cong \mathcal{O}(-d)$$이고, 따라서 $$\omega_{\mathbb{P}^n} \otimes \mathcal{O}(d)^\vee \cong \mathcal{O}(-n-1) \otimes \mathcal{O}(-d) \cong \mathcal{O}(-d-n-1)$$이다. [명제 1](#prop1)에 의해

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$$

을 얻는다. 오른쪽의 차원은 ([§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1))의 Bott's formula로 계산할 수 있다. $$\square$$

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^1$$에서 [명제 4](#prop4)에 의해 $$H^0(\mathbb{P}^1, \mathcal{O}(d)) \cong H^1(\mathbb{P}^1, \mathcal{O}(-d-2))^\ast$$이다. $$d = 0$$이면 $$H^0(\mathcal{O}) = \mathbb{K}$$이고 $$H^1(\mathcal{O}(-2)) = \mathbb{K}$$이며, $$d = 1$$이면 $$H^0(\mathcal{O}(1)) = \mathbb{K}^2$$이고 $$H^1(\mathcal{O}(-3)) = \mathbb{K}^2$$이다. 양쪽의 차원이 일치함을 확인할 수 있다.

</div>

## Grothendieck Duality

Serre duality는 variety $$X$$를 하나의 점 $$\operatorname{Spec}(\mathbb{K})$$로 보내는 상사상에 대한 특수한 경우이다. Grothendieck는 이를 임의의 proper morphism으로 일반화하였다. Proper morphism $$f \colon X \to Y$$는 위상수학적으로 compact map의 대수기하학적 대응물로, 임의의 base change에 대해 닫힌 사상이 되는 사상이다.

Serre duality에서 canonical bundle $$\omega_X$$가 핵심적인 역할을 하였듯이, relative 상황에서는 relative dualizing sheaf $$\omega_{X/Y}$$가 그 역할을 담당한다. 이는 섬유 $$f^{-1}(y)$$ 각각에서 canonical sheaf를 일관되게 모아둔 것이며, Serre duality에서 $$\omega_X$$가 하던 역할을 상대적인 상황으로 옮긴 것이다. 구체적으로 $$\omega_{X/Y}$$는 derived pullback $$f^!$$에 의해 $$\omega_{X/Y} = f^! \mathcal{O}_Y$$로 정의된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (Grothendieck Duality)**</ins> Noetherian scheme 사이의 proper morphism $$f \colon X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해, derived category에서 다음 isomorphism이 성립한다:

$$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

여기서 $$f^!$$는 right adjoint of $$R f_\ast$$이고, $$\mathcal{G}$$는 $$Y$$ 위의 bounded below complex of quasi-coherent sheaf이다. 특히 $$f$$가 smooth morphism of relative dimension $$n$$이면 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$이고, 여기서 $$\omega_{X/Y}$$는 relative canonical sheaf이다.

</div>

이 정리의 의미를 직관적으로 이해해보자. $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G})$$는 $$\mathcal{F}$$와 $$f^! \mathcal{G}$$ 사이의 '모든 가능한 Hom'을 모은 complex이며, $$R f_\ast$$를 적용하면 이를 $$Y$$ 위로 pushforward한다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$는 pushforward된 $$\mathcal{F}$$와 $$\mathcal{G}$$ 사이의 '모든 가능한 Hom'이다. 즉, 'pushforward 후 Hom'과 'Hom 후 pushforward'가 같다는 뜻이다. 본 글에서는 정리의 형태만 소개하며, 증명과 상세한 논의는 추후 별도의 글에서 다룬다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$Y = \operatorname{Spec}(\mathbb{K})$$이고 $$X$$가 $$n$$차원 smooth projective variety인 경우를 생각하자. 구조 사상 $$f \colon X \to \operatorname{Spec}(\mathbb{K})$$에 대해 $$R f_\ast \mathcal{F}$$의 cohomology는 단순히 cohomology group $$H^i(X, \mathcal{F})$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{O}_Y)$$의 cohomology는 dual vector space $$H^i(X, \mathcal{F})^\ast$$이다. 또한 $$f$$는 smooth of relative dimension $$n$$이므로 $$f^! \mathcal{O}_Y \cong \omega_X[n]$$이다. 따라서 [명제 6](#prop6)에서 $$\mathcal{G} = \mathcal{O}_Y$$, $$\mathcal{F}$$를 locally free sheaf로 취하면 cohomology 수준에서 $$H^i(X, \omega_X \otimes \mathcal{E}^\vee) \cong H^{n-i}(X, \mathcal{E})^\ast$$을 얻으며, 이는 정확히 [명제 1](#prop1)의 Serre duality이다. 즉 Serre duality는 Grothendieck duality의 특수한 경우이다.

</div>

## Trace Map

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> *Trace map* $$\operatorname{Tr} \colon H^n(X, \omega_X) \to \mathbb{K}$$는 Serre duality의 isomorphism을 실제로 구현하는 핵심 구조이다. 이는 $$H^n(X, \omega_X)$$에서 $$\mathbb{K}$$로의 isomorphism으로, Serre duality가 $$\mathcal{E} = \mathcal{O}_X$$인 경우 $$H^0(X, \omega_X) \cong H^n(X, \mathcal{O}_X)^\ast$$를 얻고, $$\mathcal{E} = \omega_X$$인 경우 $$H^n(X, \omega_X) \cong H^0(X, \mathcal{O}_X)^\ast \cong \mathbb{K}$$를 얻는 것과 양립하여야 한다. 즉 trace map은 $$H^n(X, \omega_X) \cong \mathbb{K}$$라는 사실을 구체적으로 실현하는 것이다.

직관적으로 trace map은 미분기하학에서 적분에 해당하는 연산이다. $$n$$차원 variety $$X$$ 위에서 $$\omega_X$$는 differential form들의 bundle이므로 ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24)), $$H^n(X, \omega_X)$$는 $$X$$ 전체에 걸쳐 "적분할 수 있는" top-degree form들의 공간이며, trace map은 이 적분을 기저필드 $$\mathbb{K}$$의 원소로 평가하는 것이다. 복소기하학에서 $$X$$가 compact complex manifold이면 trace map은 실제로 적분 $$\eta \mapsto \int_X \eta$$로 주어진다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Serre duality의 isomorphism은 trace map과 cup product를 사용하여 다음과 같이 명시적으로 주어진다.

$$H^i(X, \mathcal{E}) \to H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast;\quad \alpha \mapsto \left( \beta \mapsto \operatorname{Tr}(\alpha \cup \beta) \right)$$

여기서 $$\cup$$은 cup product로, $$\alpha \in H^i(X, \mathcal{E})$$와 $$\beta \in H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$로부터 $$\alpha \cup \beta \in H^n(X, \mathcal{E} \otimes (\omega_X \otimes \mathcal{E}^\vee))$$를 만들어낸다. 여기에 자연스러운 평가 사상 $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_X$$를 적용하면 $$H^n(X, \omega_X)$$의 원소를 얻으며, trace map을 적용하여 최종적으로 $$\operatorname{Tr}(\alpha \cup \beta) \in \mathbb{K}$$를 얻는다. 이 쌍선형 형식의 비퇴화성이 곧 Serre duality의 isomorphism을 준다.

</div>

Cup product의 구성을 구체적으로 살펴보자. Coherent sheaf cohomology에서 cup product는 sheaf resolution의 수준에서 정의된다. 구체적으로, $$\mathcal{E}$$와 $$\omega_X \otimes \mathcal{E}^\vee$$의 injective resolution을 이용하여 $$\alpha \cup \beta \in H^n(X, \mathcal{E} \otimes (\omega_X \otimes \mathcal{E}^\vee))$$를 구성한다. 여기에 evaluation map $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_X$$를 tensor하여 $$H^n(X, \omega_X \otimes \mathcal{O}_X) \cong H^n(X, \omega_X)$$의 원소를 얻고, trace map으로 $$\mathbb{K}$$의 원소를 얻는다. 이 전체 과정이 [명제 9](#prop9)의 쌍선형 형식을 구성한다.

## 응용: Euler Characteristic

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Serre duality에 의해 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 다음이 성립한다.

$$\chi(\mathcal{E}) = (-1)^n \chi(\omega_X \otimes \mathcal{E}^\vee)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euler characteristic의 정의와 [명제 1](#prop1)에 의해

$$\chi(\mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$

이다. 여기서 치환 $$j = n - i$$를 적용하면

$$\sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee) = \sum_{j=0}^{n} (-1)^{n-j} \dim H^j(X, \omega_X \otimes \mathcal{E}^\vee) = (-1)^n \chi(\omega_X \otimes \mathcal{E}^\vee)$$

을 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Curve)**</ins> Curve $$C$$와 line bundle $$\mathcal{L}$$에 대해, [명제 10](#prop10)에서 $$n = 1$$을 대입하면

$$\chi(\mathcal{L}) = -\chi(\omega_C \otimes \mathcal{L}^\vee)$$

이다. 한편 Euler characteristic의 정의에 의해 $$\chi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^1(C, \mathcal{L})$$이고, Serre duality에 의해 $$\dim H^1(C, \mathcal{L}) = \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$이므로

$$\chi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$

이다. 이 공식은 Riemann-Roch theorem의 출발점이 된다.

</div>

## Relative Duality

Smooth projective morphism $$f \colon X \to Y$$는 임의의 점 $$y \in Y$$에 대해 섬유 $$f^{-1}(y)$$가 smooth projective variety가 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 이런 상황에서 섬유별 canonical sheaf를 일관되게 모은 것이며, 각 섬유 $$X_y$$에서 $$\omega_{X/Y}\vert_{X_y} \cong \omega_{X_y}$$가 성립한다. 앞서 명제 6에서 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$으로 정의하였다.

Serre duality에서 $$H^n(X, \omega_X) \cong \mathbb{K}$$였던 사실은, relative situation에서 다음과 같이 일반화된다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Smooth projective morphism $$f \colon X \to Y$$에서 $$n = \dim X - \dim Y$$라 하자. 그럼

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

이며, $$i \neq n$$에 대해서는 $$R^i f_\ast \omega_{X/Y} = 0$$이다.

</div>

이 정리는 relative situation에서도 "top cohomology of canonical sheaf = 1"이라는 직관이 그대로 성립함을 보여준다. 실제로 [명제 6](#prop6)에서 $$\mathcal{F} = \mathcal{O}_X$$, $$\mathcal{G} = \mathcal{O}_Y$$를 대입하면 $$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \omega_{X/Y}[n]$$이므로 좌변은 $$R f_\ast \omega_{X/Y}[n]$$이 된다. 이 complex의 $$0$$차 cohomology sheaf를 취하면 $$R^n f_\ast \omega_{X/Y}$$를 얻는다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$의 $$0$$차 cohomology는 $$\mathcal{H}om_{\mathcal{O}_Y}(f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이며, smooth projective morphism에서는 섬유가 geometrically integral이므로 $$f_\ast \mathcal{O}_X = \mathcal{O}_Y$$가 성립하여 이는 $$\mathcal{O}_Y$$가 되어 [명제 12](#prop12)의 첫 번째 주장을 얻는다. Relative duality의 증명과 응용에 대해서는 추후 별도의 글에서 다룬다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.
