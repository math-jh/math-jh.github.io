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

기하적으로 좋은 경우 dimension $$k$$의 cohomology와 codimension $$k$$ cohomology 사이에는 자연스러운 쌍대성이 존재한다. 이를 증명하기 위해 우리는 perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

을 사용했으며, 이를 통해 [\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정리 11](/ko/math/algebraic_topology/Poincare_duality#thm11)와 같은 결과를 얻었다. 더 구체적으로, 이 pairing은 cap product와 fundamental class $$[M] \in H_n(M;R)$$를 통해 구성되므로 즉 위상수학에서 duality의 원천은 orientation class $$[M]$$이라 할 수 있다. 

이번 글에서 우리는 대수기하학 버전의 duality를 살펴본다. 이를 위해서는 orientation class $$[M]$$에 대응하는 대상을 찾아야 한다. 직관적으로 대수기하학에서 $$\Omega_X$$가 differential form들의 sheaf이고, 이 sheaf의 top exterior power가 $$\omega_X$$이므로 $$\omega_X$$의 section들은 volume form, 즉 orientation class라 할 수 있다. 이를 통해 우리는 다음의 cup product pairing

$$H^k(X, \mathcal{E})\times H^{n-k}(X, \omega_X\otimes \mathcal{E}^\vee)\rightarrow H^n(X, \omega_X)$$

을 정의할 수 있으며 이를 trace map $$\operatorname{Tr}:H^n(X, \omega_X)\rightarrow \mathbb{K}$$로 보내 duality를 얻어낸다. 이 pairing을 엄밀하게 정의하기 위해 먼저 trace map을 소개하고, 이후 $$\mathbb{P}^n$$에서 duality를 확인한 뒤 일반적인 정리를 서술한다.

## Trace Map

$$n$$차원 smooth projective variety $$X$$ 위에서 *trace map*은 canonical isomorphism $$\operatorname{Tr} \colon H^n(X, \omega_X) \xrightarrow{\sim} \mathbb{K}$$이다. 이는 임의로 선택할 수 있는 isomorphism이 아니라 구체적으로 구성된다. 가장 기본적인 경우인 $$\mathbb{P}^n$$에서 그 구성을 살펴보자. $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$이므로 ([§표준선다발, ⁋예시 8](/ko/math/algebraic_geometry/canonical_bundle#ex8)), 표준 아핀 열린덮개 $$U_i = D_+(x_i)$$에 대한 Čech complex에서 $$H^n(\mathbb{P}^n, \mathcal{O}(-n-1))$$은 공간 $$\Gamma(U_0 \cap \cdots \cap U_n, \mathcal{O}(-n-1))$$과 같다. 이 공간은 homogeneous coordinate $$x_0, \ldots, x_n$$에 대해 차원 $$-n-1$$의 원소들로 이루어지며, 유일한 monomial $$x_0^{-1} \cdots x_n^{-1}$$의 상수배로 생성되는 1차원 vector space이다. Trace map은 cocycle $$c \cdot x_0^{-1} \cdots x_n^{-1}$$을 그 계수 $$c \in \mathbb{K}$$로 보내는 사상으로 정의된다.

일반적인 smooth projective variety $$X$$에서는 Noether 정리에 의해 finite surjective morphism $$f \colon X \to \mathbb{P}^n$$이 존재하며, $$\mathbb{P}^n$$에서의 trace map과 functor $$f^!$$를 결합하여 $$X$$ 위의 trace map을 얻는다. 즉 trace map의 정의는 본질적으로 $$\mathbb{P}^n$$에서의 구성에 기반하며, 다른 variety에 대한 확장은 functorial한 방식으로 이루어진다. 복소기하학에서 $$X$$가 compact complex manifold이면 trace map은 실제로 적분 $$\eta \mapsto \int_X \eta$$로 주어지며, 이는 앞선 Čech적 구성이 미분기하학적으로 자연스러운 적분 연산과 일치함을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Serre duality의 isomorphism은 trace map과 cup product를 사용하여 다음과 같이 명시적으로 주어진다.

$$H^i(X, \mathcal{E}) \to H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast;\quad \alpha \mapsto \left( \beta \mapsto \operatorname{Tr}(\alpha \smile \beta) \right)$$

여기서 $$\smile$$은 cup product로, $$\alpha \in H^i(X, \mathcal{E})$$와 $$\beta \in H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$로부터 $$\alpha \smile \beta \in H^n(X, \mathcal{E} \otimes (\omega_X \otimes \mathcal{E}^\vee))$$를 만들어낸다. 여기에 자연스러운 평가 사상 $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_X$$를 적용하면 $$H^n(X, \omega_X)$$의 원소를 얻으며, trace map을 적용하여 최종적으로 $$\operatorname{Tr}(\alpha \smile \beta) \in \mathbb{K}$$를 얻는다. 이 쌍선형 형식의 비퇴화성이 곧 Serre duality의 isomorphism을 준다.

</div>

Cup product의 구성을 구체적으로 살펴보자. Coherent sheaf cohomology에서 cup product는 sheaf resolution의 수준에서 정의된다. 구체적으로, $$\mathcal{E}$$와 $$\omega_X \otimes \mathcal{E}^\vee$$의 injective resolution을 이용하여 $$\alpha \smile \beta \in H^n(X, \mathcal{E} \otimes (\omega_X \otimes \mathcal{E}^\vee))$$를 구성한다. 여기에 evaluation map $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_X$$를 tensor하여 $$H^n(X, \omega_X \otimes \mathcal{O}_X) \cong H^n(X, \omega_X)$$의 원소를 얻고, trace map으로 $$\mathbb{K}$$의 원소를 얻는다. 이 전체 과정이 [명제 1](#prop1)의 쌍선형 형식을 구성한다.

Trace map이 정의되었으니, 가장 먼저 $$\mathbb{P}^n$$에서 Serre duality가 성립하는지 확인해보자. 앞선 글에서 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$임을 보였으므로 ([§표준선다발, ⁋예시 8](/ko/math/algebraic_geometry/canonical_bundle#ex8)), 서론에서 구성한 pairing은 구체적으로

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \times H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1)) \to H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \to \mathbb{K}$$

이 된다. 이제 ([§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1))의 Bott's formula에 의해 각 cohomology group의 차원을 계산하여 양쪽이 대칭임을 보이자. Bott's formula에 따르면 $$H^i(\mathbb{P}^n, \mathcal{O}(d))$$는 $$i = 0, d \geq 0$$일 때 차원이 $$\binom{d+n}{n}$$이고, $$i = n, d \leq -n-1$$일 때 차원이 $$\binom{-d-1}{n}$$이며, 그 외에는 0이다. 세 가지 경우로 나누어 확인한다.

- $$i = 0, d \geq 0$$: 좌변의 차원은 $$\binom{d+n}{n}$$이고, 우변은 $$H^n(\mathbb{P}^n, \mathcal{O}(-d-n-1))$$로서 $$-d-n-1 \leq -n-1$$이므로 차원이 $$\binom{d+n}{n}$$이다.
- $$i = n, d \leq -n-1$$: 좌변의 차원은 $$\binom{-d-1}{n}$$이고, 우변은 $$H^0(\mathbb{P}^n, \mathcal{O}(-d-n-1))$$로서 $$-d-n-1 \geq 0$$이므로 차원이 $$\binom{-d-1+n}{n} = \binom{-d-1}{n}$$이다.
- 그 외의 모든 $$i$$에 대해서는 양변이 모두 0이다.

따라서 $$\mathbb{P}^n$$에서 $$H^i(\mathbb{P}^n, \mathcal{O}(d)) \cong H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1))^\ast$$이 성립한다. 더 일반적으로, 임의의 smooth projective variety 위에서도 동일한 duality가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Serre Duality)**</ins> Field $$\mathbb{K}$$ 위의 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

여기서 $$\omega_X$$는 canonical bundle ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))이고 $$\mathcal{E}^\vee = \mathcal{H}om(\mathcal{E}, \mathcal{O}_X)$$는 dual sheaf이다.

</div>

Locally free sheaf $$\mathcal{E}$$에 대해서는 $$\mathcal{H}om(\mathcal{E}, \omega_X) \cong \omega_X \otimes \mathcal{E}^\vee$$가 성립하므로 ([§선다발과 벡터다발, ⁋명제 7](/ko/math/algebraic_geometry/line_bundles#prop7)), 명제의 우변을 $$H^{n-i}(X, \mathcal{H}om(\mathcal{E}, \omega_X))^\ast$$와 같이 쓸 수도 있다. 일반적인 coherent sheaf $$\mathcal{F}$$에 대해서는 $$\omega_X \otimes \mathcal{F}^\vee$$ 대신 Ext group $$\operatorname{Ext}^i(\mathcal{F}, \omega_X)$$를 사용하여 $$\operatorname{Ext}^{n-i}(\mathcal{F}, \omega_X) \cong H^i(X, \mathcal{F})^\ast$$의 형태로 동일한 duality가 성립하지만, 본 글에서는 locally free sheaf에 대한 버전을 다룬다. 또한 Hartshorne의 고전적 증명에서는 $$\mathbb{K}$$가 algebraically closed field라고 가정하지만, Grothendieck duality를 사용하면 임의의 field에 대해 동일한 결과가 성립한다.

Serre duality의 증명은 깊은 정리로, 여러 가지 접근법이 존재한다. 대표적으로, projective space에서의 계산을 바탕으로 finite morphism을 통해 일반적인 variety로 확장하는 방법과, derived category에서 $$\omega_X = f^! \mathcal{O}_{\operatorname{Spec}(\mathbb{K})}$$로 정의한 뒤 derived adjunction으로 duality를 얻는 방법이 있다. 두 방법 모두 본질적으로 동일한 핵심 사실에 기반한다. 즉, trace map과 [명제 1](#prop1)의 cup product가 완벽한 쌍대성을 이룬다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 특히 $$\mathcal{E} = \mathcal{O}_X$$에 대해:

$$H^i(X, \mathcal{O}_X) \cong H^{n-i}(X, \omega_X)^\ast$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{O}_X^\vee = \mathcal{H}om(\mathcal{O}_X, \mathcal{O}_X) \cong \mathcal{O}_X$$이므로, [명제 2](#prop2)에서 $$\mathcal{E} = \mathcal{O}_X$$를 대입하면 $$\omega_X \otimes \mathcal{O}_X^\vee \cong \omega_X$$를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (Curve)**</ins> Genus $$g$$인 smooth curve $$C$$를 생각하자. 여기서 genus는 $$g = \dim H^1(C, \mathcal{O}_C)$$로 정의된다. $$C$$는 $$1$$차원이므로 [명제 3](#prop3)에서 $$n = 1$$을 대입하면 다음을 얻는다.

$$H^0(C, \mathcal{O}_C) \cong H^1(C, \omega_C)^\ast$$이고 $$H^1(C, \mathcal{O}_C) \cong H^0(C, \omega_C)^\ast$$이다.

첫 번째 동형에서 $$\dim H^0(C, \mathcal{O}_C) = 1$$이므로 $$\dim H^1(C, \omega_C) = 1$$이고, 두 번째 동형에서 $$\dim H^0(C, \omega_C) = \dim H^1(C, \mathcal{O}_C)^\ast = g$$이다. 즉 canonical bundle $$\omega_C$$의 global section의 차원이 정확히 genus $$g$$와 같다. 이는 Riemann-Roch theorem의 기초가 되는 관측이다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\mathbb{P}^1$$에서 $$\omega_{\mathbb{P}^1} \cong \mathcal{O}(-2)$$이므로 [명제 2](#prop2)에 의해 $$H^0(\mathbb{P}^1, \mathcal{O}(d)) \cong H^1(\mathbb{P}^1, \mathcal{O}(-d-2))^\ast$$이다. $$d = 0$$이면 $$H^0(\mathcal{O}) = \mathbb{K}$$이고 $$H^1(\mathcal{O}(-2)) = \mathbb{K}$$이며, $$d = 1$$이면 $$H^0(\mathcal{O}(1)) = \mathbb{K}^2$$이고 $$H^1(\mathcal{O}(-3)) = \mathbb{K}^2$$이다. 양쪽의 차원이 일치함을 확인할 수 있다.

</div>

## 응용: Euler Characteristic

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Serre duality에 의해 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 다음이 성립한다.

$$\rchi(\mathcal{E}) = (-1)^n \rchi(\omega_X \otimes \mathcal{E}^\vee)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euler characteristic의 정의와 [명제 2](#prop2)에 의해

$$\rchi(\mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$

이다. 여기서 치환 $$j = n - i$$를 적용하면

$$\sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee) = \sum_{j=0}^{n} (-1)^{n-j} \dim H^j(X, \omega_X \otimes \mathcal{E}^\vee) = (-1)^n \rchi(\omega_X \otimes \mathcal{E}^\vee)$$

을 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Curve)**</ins> Curve $$C$$와 line bundle $$\mathcal{L}$$에 대해, [명제 6](#prop6)에서 $$n = 1$$을 대입하면

$$\rchi(\mathcal{L}) = -\rchi(\omega_C \otimes \mathcal{L}^\vee)$$

이다. 한편 Euler characteristic의 정의에 의해 $$\rchi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^1(C, \mathcal{L})$$이고, Serre duality에 의해 $$\dim H^1(C, \mathcal{L}) = \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$이므로

$$\rchi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$

이다. 이 공식은 Riemann-Roch theorem의 출발점이 된다.

</div>

## Relative Duality

Smooth projective morphism $$f \colon X \to Y$$는 임의의 점 $$y \in Y$$에 대해 섬유 $$f^{-1}(y)$$가 smooth projective variety가 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 이런 상황에서 섬유별 canonical sheaf를 일관되게 모은 것이며, 각 섬유 $$X_y$$에서 $$\omega_{X/Y}\vert_{X_y} \cong \omega_{X_y}$$가 성립한다.

Serre duality에서 $$H^n(X, \omega_X) \cong \mathbb{K}$$였던 사실은, relative situation에서 다음과 같이 일반화된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Smooth projective morphism $$f \colon X \to Y$$에서 $$n = \dim X - \dim Y$$라 하자. 그럼

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

이며, $$i \neq n$$에 대해서는 $$R^i f_\ast \omega_{X/Y} = 0$$이다.

</div>

이 정리는 relative situation에서도 "top cohomology of canonical sheaf = 1"이라는 직관이 그대로 성립함을 보여준다. 실제로 [명제 9](#prop9)에서 $$\mathcal{F} = \mathcal{O}_X$$, $$\mathcal{G} = \mathcal{O}_Y$$를 대입하면 $$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \omega_{X/Y}[n]$$이므로 좌변은 $$R f_\ast \omega_{X/Y}[n]$$이 된다. 이 complex의 $$0$$차 cohomology sheaf를 취하면 $$R^n f_\ast \omega_{X/Y}$$를 얻는다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$의 $$0$$차 cohomology는 $$\mathcal{H}om_{\mathcal{O}_Y}(f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이며, smooth projective morphism에서는 섬유가 geometrically integral이므로 $$f_\ast \mathcal{O}_X = \mathcal{O}_Y$$가 성립하여 이는 $$\mathcal{O}_Y$$가 되어 [명제 8](#prop8)의 첫 번째 주장을 얻는다. Relative duality의 증명과 응용에 대해서는 추후 별도의 글에서 다룬다.

## Grothendieck Duality

Serre duality는 variety $$X$$를 하나의 점 $$\operatorname{Spec}(\mathbb{K})$$로 보내는 상사상에 대한 특수한 경우이다. Grothendieck는 이를 임의의 proper morphism으로 일반화하였다. Proper morphism $$f \colon X \to Y$$는 위상수학적으로 compact map의 대수기하학적 대응물로, 임의의 base change에 대해 닫힌 사상이 되는 사상이다.

Serre duality에서 canonical bundle $$\omega_X$$가 핵심적인 역할을 하였듯이, relative 상황에서는 relative dualizing sheaf $$\omega_{X/Y}$$가 그 역할을 담당한다. 이는 섬유 $$f^{-1}(y)$$ 각각에서 canonical sheaf를 일관되게 모아둔 것이며, Serre duality에서 $$\omega_X$$가 하던 역할을 상대적인 상황으로 옮긴 것이다. 구체적으로 $$\omega_{X/Y}$$는 derived pullback $$f^!$$에 의해 $$\omega_{X/Y} = f^! \mathcal{O}_Y$$로 정의된다. 여기서 $$f^!$$는 $$R f_\ast$$의 right adjoint로 ([§유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)), derived category에서만 자연스럽게 정의된다.

### Derived functor 개념

Grothendieck duality를 기술하려면 derived category 위에서 정의되는 여러 functor가 필요하다. ([§유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)) 여기서는 각 functor가 왜 필요한지, 그리고 구성적으로 어떻게 정의되는지를 설명한다.

**$$\mathcal{H}om$$** ([§선다발과 벡터다발, ⁋명제 7](/ko/math/algebraic_geometry/line_bundles#prop7)). 이것은 module category의 $$\operatorname{Hom}$$과 다른 개념이다. $$\mathcal{H}om(\mathcal{F}, \mathcal{G})$$는 각 열린집합 $$U$$마다 $$\operatorname{Hom}_{\mathcal{O}_X(U)}(\mathcal{F}(U), \mathcal{G}(U))$$를 취한 뒤, 이 presheaf를 sheafify하여 얻은 sheaf이다. 즉 open set마다 독립적으로 Hom을 계산하고 이를 sheaf로 모은 것이다.

**$$\mathbf{R}\mathcal{H}om$$** ([§유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10)). $$\mathcal{H}om$$은 covariant 인수에서 left exact, contravariant 인수에서도 left exact하지만 right exact가 아니므로, 이 functor를 그대로 사용하면 정보가 손실된다. 예를 들어 short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$에 대해 $$\mathcal{H}om(-, \mathcal{G})$$를 적용하면 오른쪽에서 exactness가 깨진다. 따라서 두 인수 모두에서 derived functor가 필요하다. 구체적으로, contravariant 인수에 injective resolution을 취해 $$\mathcal{F} \to \mathcal{I}^\bullet$$로 치환한 뒤, covariant 인수에도 injective resolution을 취해 $$\mathcal{G} \to \mathcal{J}^\bullet$$로 치환하고 $$\mathcal{H}om(\mathcal{I}^\bullet, \mathcal{J}^\bullet)$$을 적용한다. 이 complex의 cohomology가 $$\operatorname{Ext}^i(\mathcal{F}, \mathcal{G})$$를 준다.

**$$R f_\ast$$** ([§유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)). Pushforward $$f_\ast$$는 left exact functor이다: $$0 \to f_\ast \mathcal{F}' \to f_\ast \mathcal{F} \to f_\ast \mathcal{F}''$$는 exact하지만 오른쪽에서는 $$f_\ast \mathcal{F}''$$로의 surjectivity가 보장되지 않는다. 따라서 right derived functor $$R f_\ast$$가 필요하다. Sheaf $$\mathcal{F}$$에 injective resolution $$\mathcal{F} \to \mathcal{I}^\bullet$$을 취한 뒤 $$f_\ast \mathcal{I}^\bullet$$을 적용한다. 이 complex의 cohomology가 higher direct image $$R^i f_\ast$$를 준다.

**$$L f^\ast$$** ([§유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)). Pullback $$f^\ast$$는 right exact functor이다. 이는 $$f^\ast$$가 $$f^{-1}(-) \otimes_{f^{-1}\mathcal{O}_Y} \mathcal{O}_X$$와 같은 tensor product의 형태이기 때문이다: tensor product는 항상 right exact하지만 left exact가 아니다. 따라서 left derived functor $$L f^\ast$$가 필요하며, flat resolution로 치환한 뒤 pullback을 적용한다.

**$$f^!$$** ([§유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)). 이 functor는 $$R f_\ast$$의 right adjoint로 derived category에서만 자연스럽게 정의된다. Sheaf category $$\operatorname{Coh}(X)$$의 수준에서는 $$f^!$$에 올바른 의미를 부여할 수 없다: $$R f_\ast$$가 complex 수준의 functor이므로, 그 adjoint 역시 complex 수준에서 존재해야 한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (Grothendieck Duality)**</ins> Smooth projective variety 사이의 proper morphism $$f \colon X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해, derived category에서 다음 isomorphism이 성립한다:

$$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

여기서 $$R f_\ast$$는 derived pushforward ([§유도카테고리, ⁋정의 6](/ko/math/homological_algebra/derived_categories#def6)), $$\mathbf{R}\mathcal{H}om$$은 derived Hom ([§유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10)), 그리고 $$f^!$$는 $$R f_\ast$$의 right adjoint ([§유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13))이다. $$\mathcal{G}$$는 $$Y$$ 위의 coherent sheaf의 bounded below complex ([§유도카테고리, ⁋정의 4](/ko/math/homological_algebra/derived_categories#def4))이다. 특히 $$f$$가 smooth morphism of relative dimension $$n$$이면 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$이고, 여기서 $$\omega_{X/Y}$$는 relative canonical sheaf이다.

</div>

이 정리의 의미를 직관적으로 이해해보자. $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G})$$는 $$\mathcal{F}$$와 $$f^! \mathcal{G}$$ 사이의 '모든 가능한 Hom'을 모은 complex이며, $$R f_\ast$$를 적용하면 이를 $$Y$$ 위로 pushforward한다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$는 pushforward된 $$\mathcal{F}$$와 $$\mathcal{G}$$ 사이의 '모든 가능한 Hom'이다. 즉, 'pushforward 후 Hom'과 'Hom 후 pushforward'가 같다는 뜻이다. 본 글에서는 정리의 형태만 소개하며, 증명과 상세한 논의는 추후 별도의 글에서 다룬다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$Y = \operatorname{Spec}(\mathbb{K})$$이고 $$X$$가 $$n$$차원 smooth projective variety인 경우를 생각하자. 구조 사상 $$f \colon X \to \operatorname{Spec}(\mathbb{K})$$에 대해 $$R f_\ast \mathcal{F}$$의 cohomology는 단순히 cohomology group $$H^i(X, \mathcal{F})$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{O}_Y)$$의 cohomology는 dual vector space $$H^i(X, \mathcal{F})^\ast$$이다. 또한 $$f$$는 smooth of relative dimension $$n$$이므로 $$f^! \mathcal{O}_Y \cong \omega_X[n]$$이다. 따라서 [명제 9](#prop9)에서 $$\mathcal{G} = \mathcal{O}_Y$$, $$\mathcal{F}$$를 locally free sheaf로 취하면 cohomology 수준에서 $$H^i(X, \omega_X \otimes \mathcal{E}^\vee) \cong H^{n-i}(X, \mathcal{E})^\ast$$을 얻으며, 이는 정확히 [명제 2](#prop2)의 Serre duality이다. 즉 Serre duality는 Grothendieck duality의 특수한 경우이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.