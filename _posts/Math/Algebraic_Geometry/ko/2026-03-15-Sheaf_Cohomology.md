---
title: "Sheaf Cohomology"
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/sheaf_cohomology
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Sheaf_Cohomology.png
    overlay_filter: 0.5

date: 2026-03-12
last_modified_at: 2026-03-31
weight: 13

published: false
---

([§층](/ko/math/topology/sheaves))에서 우리는 sheaf 개념을 정의하였다. 이제 sheaf의 *cohomology*를 정의한다. Sheaf cohomology는 국소적 데이터(각 열린집합 위의 section)가 전역적으로 어떻게 결합되는지를 측정하는 도구이다. 이는 특히 ([§Line Bundles](/ko/math/algebraic_geometry/line_bundles))에서 도입한 global section space $$H^0(X, \mathcal{L})$$의 고차 일반화이며, Riemann-Roch 정리와 Serre duality의 핵심적인 구성요소이다.

## Derived Functor로서의 정의

Sheaf cohomology는 sheaf의 global section functor의 derived functor로 정의된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1** Variety $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F}$$에 대하여, $$i$$번째 *sheaf cohomology* $$H^i(X, \mathcal{F})$$는 global section functor $$\Gamma(X, -) = H^0(X, -)$$의 $$i$$번째 right derived functor이다.

$$H^i(X, \mathcal{F}) = R^i\Gamma(X, \mathcal{F})$$

</div>

Global section functor $$\Gamma(X, -)$$는 left exact이다: sheaf의 short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$에서 $$\Gamma$$를 적용하면 section의 값을 점단위로 취하는 것과 같으므로, $$0 \to \Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'')$$는 exact이다. 그러나 우변의 $$\Gamma(X, \mathcal{F}'') \to 0$$은 일반적으로 exact하지 않으므로, $$\Gamma$$는 right exact하지 않다. Right derived functor는 이 "전역화에서 손실되는 정보"를 측정한다.

$$i = 0$$인 경우, $$H^0(X, \mathcal{F})$$는 $$\mathcal{F}$$의 global section space $$\Gamma(X, \mathcal{F})$$와 일치한다. $$i > 0$$인 경우, $$H^i$$는 "전역 section의 장애물"을 측정한다.

<div class="misc" markdown="1">
**직관.** 직관적으로, $$H^1(X, \mathcal{F})$$는 local section들을 전역적으로 "붙이는" 과정에서 나타나는 실패 정도를 나타낸다. 만약 $$H^1 = 0$$이면, 국소적 데이터가 항상 전역적으로 결합될 수 있다는 뜻이다.
</div>

## Čech Cohomology와의 관계

실제 계산에서는 derived functor 정의 대신 Čech cohomology를 사용한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2** Finite open cover $$\mathcal{U} = \{U_1, \ldots, U_r\}$$에 대하여, $$p$$-차 *Čech 복합체* $$C^p(\mathcal{U}, \mathcal{F})$$를

$$C^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

으로 정의한다. *Čech 미분* $$d^p: C^p \to C^{p+1}$$는 교대 합으로 주어진다.

</div>

<div class="definition" markdown="1">

<ins id="def3">**정의 3** Open cover $$\mathcal{U}$$에 대한 *Čech cohomology* $$\check{H}^p(\mathcal{U}, \mathcal{F})$$를

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = \frac{\ker d^p}{\operatorname{im} d^{p-1}}$$

으로 정의한다. *Čech cohomology* $$\check{H}^p(X, \mathcal{F})$$는 모든 open cover에 대한 direct limit이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4** (Leray 정리) Open cover $$\mathcal{U} = \{U_i\}$$가 다음 조건을 만족하면, Čech cohomology가 sheaf cohomology와 동형이다:

$$H^p(U_{i_0} \cap \cdots \cap U_{i_q}, \mathcal{F}) = 0 \quad \text{for all } p > 0, \text{ all finite intersections}$$

즉, 이 조건 하에서 $$\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Leray 정리는 spectral sequence의 degeneration에 의해 증명된다. Cover $$\mathcal{U}$$에 대해 double complex $$C^p(\mathcal{U}, \mathcal{I}^q)$$ (여기서 $$\mathcal{I}^\bullet$$는 injective resolution)를 구성하여 얻는 Čech-to-derived functor spectral sequence의 $$E_2$$ 페이지는 $$E_2^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F}))$$이다. Acyclicity 조건에 의해 $$q > 0$$인 열이 모두 소멸하므로 $$E_2$$에서 이미 degenerate하고, $$\check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$를 얻는다.

</details>

## Long Exact Sequence

Sheaf cohomology의 핵심 도구 중 하나는 short exact sequence에서 유도되는 long exact sequence이다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5** Sheaf의 short exact sequence

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$

에 대하여, 긴 완전열

$$0 \to H^0(X, \mathcal{F}') \to H^0(X, \mathcal{F}) \to H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \to \cdots$$

이 존재한다. 여기서 $$\delta$$는 *connecting homomorphism*이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이 long exact sequence는 derived functor의 일반적 성질로부터 얻어진다. Global section functor $$\Gamma$$에 short exact sequence를 적용한 resolution $$0 \to \Gamma(\mathcal{I}') \to \Gamma(\mathcal{I}) \to \Gamma(\mathcal{I}'')$$에 snake lemma를 적용하면 connecting homomorphism $$\delta$$를 얻을 수 있다: $$\mathcal{F}''$$의 global section을 local section으로 잘라 $$\mathcal{F}$$에서 lift한 뒤, 교차점에서의 차이를 $$\mathcal{F}'$$의 cohomology class로 읽는 것이 $$\delta$$의 본질적인 구성이다.

</details>

## 구체적 계산 예시

<div class="example" markdown="1">

<ins id="ex6">**예시 6** **$$\mathbb{P}^1$$에서의 line bundle cohomology**: $$\mathbb{P}^1$$ 위의 line bundle $$\mathcal{O}(k)$$의 cohomology를 계산하면, $$k \ge 0$$일 때:

$$H^0(\mathbb{P}^1, \mathcal{O}(k)) = k + 1, \quad H^1(\mathbb{P}^1, \mathcal{O}(k)) = 0$$

을 의미한다. 한편 $$k < 0$$일 때:

$$H^0(\mathbb{P}^1, \mathcal{O}(k)) = 0, \quad H^1(\mathbb{P}^1, \mathcal{O}(k)) = -k - 1$$

이다. $$H^0$$과 $$H^1$$의 차원이 서로 반대 방향으로 움직이는 것이 Serre duality의 초기 예시이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7** **$$\mathbb{P}^n$$의 cohomology (Bott 공식)**: §Cohomology of Line Bundles에서 다룰 Bott 공식에 따르면, $$\mathbb{P}^n$$ 위의 line bundle $$\mathcal{O}_{\mathbb{P}^n}(k)$$의 cohomology는 다음과 같다:

- $$k \ge 0$$: $$H^0(\mathbb{P}^n, \mathcal{O}(k)) = \binom{n+k}{k}$$, 나머지 $$H^i = 0$$ ($$i > 0$$)
- $$k \le -n-1$$: $$H^n(\mathbb{P}^n, \mathcal{O}(k)) = \binom{-k-1}{n}$$, 나머지 $$H^i = 0$$ ($$i < n$$)
- $$-n \le k \le -1$$: 모든 $$H^i = 0$$

</div>

## Serre Duality 미리보기

Sheaf cohomology의 가장 중요한 응용 중 하나는 ([§Canonical Bundle](/ko/math/algebraic_geometry/canonical_bundle))에서 도입한 canonical bundle $$\omega_X$$과 관련된 Serre duality이다. 이는 §Serre Duality에서 자세히 다루지만, 핵심 정리만 미리 서술하면 다음과 같다.

<div class="misc" markdown="1">
**미리보기 (Serre Duality).** Smooth projective variety $$X$$ of dimension $$n$$과 임의의 coherent sheaf $$\mathcal{F}$$에 대하여, 자연스러운 동형

$$H^i(X, \mathcal{F})^\ast \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$

이 존재한다고 알려져 있다. 특히 $$H^n(X, \omega_X) \cong \mathbb{K}$$이다. 전체 증명과 응용은 §Serre Duality에서 다룬다.
</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
