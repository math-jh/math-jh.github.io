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

date: 2026-03-15
last_modified_at: 2026-04-02
weight: 13
---

([\[위상수학\] §층](/ko/math/topology/sheaves))에서 우리는 sheaf 개념을 정의하였다. Sheaf의 핵심 철학은 국소적 데이터를 전역적 데이터로 결합하는 것이었다. 가령 ([§선다발과 벡터다발](/ko/math/algebraic_geometry/line_bundles))에서 우리는 line bundle $\mathcal{L}$의 global section space $H^0(X, \mathcal{L})$을 정의하였고, 그 차원을 계산하는 것이 line bundle의 분류에 핵심적임을 살펴보았다.

그러나 sheaf가 우리에게 주는 유일한 정보가 global section뿐이라면 기하학적 도구로서의 활용도는 크지 않을 것이다. 우리의 철학에 따르면, 모든 기하학적 대상은 위상공간과 그 위에 정의된 sheaf의 pair이므로, sheaf 자체를 input으로 받아 새로운 불변량을 output으로 내놓는 기계가 필요하다. 이 글에서 우리는 sheaf의 *cohomology*를 정의하고, 이것이 바로 이러한 역할을 한다는 것을 살펴본다. Sheaf cohomology는 국소적 데이터(각 열린집합 위의 section)가 전역적으로 어떻게 결합되는지를 측정하는 도구이며, Riemann-Roch 정리와 Serre duality의 핵심적인 구성요소이다.

## Derived Functor로서의 정의

Sheaf cohomology를 정의하기 위해 우리는 먼저 global section functor의 성질을 살펴보아야 한다. Variety $$X$$ 위의 quasi-coherent sheaf들의 category $$\mathfrak{Qcoh}(X)$$에서 $$\mathbb{K}$$-vector space들의 category로의 global section functor

$$\Gamma(X, -): \mathfrak{Qcoh}(X) \to \mathrm{Vect}_\mathbb{K}, \qquad \mathcal{F} \mapsto \mathcal{F}(X)$$

는 left exact이다. 구체적으로, sheaf의 short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$에 $$\Gamma$$를 적용하면

$$0 \to \Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'')$$

는 exact이다. 이것이 성립하는 이유는, 각각의 exactness 조건이 점 $$x \in X$$에서의 exactness로부터 국소적으로 확인되기 때문이다. 예를 들어 $$\Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F})$$이 injective인 것은 $$\mathcal{F}' \to \mathcal{F}$$이 각 점에서 injective이므로 global section에서도 injective인 것으로부터 자명하다.

그러나 우변의 surjection $$\Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'') \to 0$$은 일반적으로 성립하지 않는다. ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))에서 우리는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 global section이 $$0$$뿐임을 보았는데, 이는 surjection $$\mathcal{O}_{\mathbb{P}^n}^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n}(1)$$을 생각하면 $$\Gamma$$를 적용한 후 surjectivity가 깨지는 구체적인 예시가 된다. 즉 $$\Gamma$$는 right exact하지 않으며, 이 "전역화에서 손실되는 정보"를 측정하는 것이 바로 sheaf cohomology의 역할이다.

이를 엄밀하게 구현하기 위해 우리는 homological algebra의 도구를 사용한다. Abelian category에서 left exact functor의 정보 손실을 측정하는 표준적인 방법은 right derived functor를 구성하는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Quasi-coherent sheaf $$\mathcal{F}$$의 *injective resolution*은 exact sequence

$$0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \mathcal{I}^2 \to \cdots$$

이다. 여기서 각 $$\mathcal{I}^i$$는 injective quasi-coherent sheaf이다.

</div>

Quasi-coherent sheaf의 category에는 충분한 injective object가 존재하므로, 임의의 quasi-coherent sheaf $$\mathcal{F}$$는 항상 injective resolution을 갖는다. 이제 global section functor $$\Gamma$$를 injective resolution에 적용하면 복합체(complex)

$$0 \to \Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1) \to \Gamma(X, \mathcal{I}^2) \to \cdots$$

를 얻는다. $$\Gamma$$가 left exact이므로 $$H^0(\Gamma(X, \mathcal{I}^\bullet)) = \ker(\Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1))$$은 원래의 $$\Gamma(X, \mathcal{F})$$와 동형이다. 일반적으로 이 복합체의 cohomology가 바로 sheaf cohomology를 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$ 위의 quasi-coherent sheaf $$\mathcal{F}$$에 대하여, $$i$$번째 *sheaf cohomology* $$H^i(X, \mathcal{F})$$를

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \to \Gamma(X, \mathcal{I}^{i+1}))}{\operatorname{im}(\Gamma(X, \mathcal{I}^{i-1}) \to \Gamma(X, \mathcal{I}^i))}$$

으로 정의한다. 여기서 $$\mathcal{I}^\bullet$$은 $$\mathcal{F}$$의 injective resolution이다.

</div>

이 정의가 잘 되려면 $$H^i$$가 injective resolution의 선택에 무관해야 하는데, 이는 homological algebra의 표준적인 논증으로부터 보장된다. 두 injective resolution은 chain homotopy equivalence 관계에 있으므로, $$\Gamma$$를 적용한 복합체의 cohomology는 동형이다.

$$i = 0$$인 경우, 위에서 논의한 대로 $$H^0(X, \mathcal{F}) \cong \Gamma(X, \mathcal{F})$$이다. $$i > 0$$인 경우, $$H^i$$는 전역 section의 "장애물"을 측정한다. 구체적으로, $$H^1(X, \mathcal{F})$$는 local section들을 전역적으로 "붙이는" 과정에서 나타나는 실패 정도를 나타낸다. 만약 $$H^1 = 0$$이면, 국소적 데이터가 항상 전역적으로 결합될 수 있다는 뜻이다. 더 높은 $$H^i$$들은 더 복잡한 국소-전역 장애물들을 측정한다.

## Čech Cohomology와의 관계

실제 계산에서는 derived functor 정의 대신 Čech cohomology를 사용한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Finite open cover $$\mathcal{U} = \{U_1, \ldots, U_r\}$$에 대하여, $$p$$-차 *Čech 복합체* $$C^p(\mathcal{U}, \mathcal{F})$$를

$$C^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

으로 정의한다. *Čech 미분* $$d^p: C^p \to C^{p+1}$$는 다음과 같이 주어진다. $$p$$-cochain $$\alpha = (\alpha_{i_0 \cdots i_p})$$에 대하여,

$$(d^p\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \widehat{i_k} \cdots i_{p+1}}\big|_{U_{i_0} \cap \cdots \cap U_{i_{p+1}}}$$

이다. 여기서 $$\widehat{i_k}$$는 index $$i_k$$를 생략한다는 의미이다. 즉, $$d^p\alpha$$의 각 성분은 $$\alpha$$의 $$(p+1)$$개의 성분들을 교대로 부호를 바꾸어 더한 것이다.

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

## $$\mathbb{P}^n$$에서의 Cohomology 계산

이제 우리는 Čech cohomology를 사용하여 $$\mathbb{P}^1$$ 위의 line bundle $$\mathcal{O}(k)$$의 cohomology를 직접 계산한다. 이를 위해 standard open cover $$U_0 = \{x_0 \ne 0\}$$, $$U_1 = \{x_1 \ne 0\}$$를 사용한다. 각각의 $$U_i$$에서 좌표함수를 $$t_i = x_{1-i}/x_i$$라 두자. 그럼 $$U_0 \cap U_1$$에서 $$t_0 = 1/t_1$$이고, $$\mathcal{O}(k)$$의 transition function은 $$g_{01} = (x_1/x_0)^k = t_0^{-k}$$이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **$$H^0(\mathbb{P}^1, \mathcal{O}(k))$$의 계산** Čech complex는

$$0 \to C^0 = \mathcal{O}(k)(U_0) \times \mathcal{O}(k)(U_1) \xrightarrow{d^0} C^1 = \mathcal{O}(k)(U_0 \cap U_1) \to 0$$

이다. 여기서 Čech 미분은 $$d^0(s_0, s_1) = s_1 - s_0$$으로 주어진다 ($$\mathcal{O}(k)$$의 section을 $$U_0$$의 좌표 $$t_0$$로 표현했을 때, $$U_1$$에서의 같은 section은 $$s_1 = t_0^{-k} \cdot s_0$$로 변환된다). $$H^0$$는 $$\ker d^0$$이므로, $$s_0$$과 $$s_1$$이 $$U_0 \cap U_1$$에서 일치하는 section의 공간이다. 이는 정확히 global section의 공간이다.

$$k \ge 0$$인 경우, $$\mathcal{O}(k)(U_0)$$는 $$t_0$$에 대한 다항식 $$\mathbb{K}[t_0]$$이고, $$\mathcal{O}(k)(U_1)$$은 $$t_1$$에 대한 다항식 $$\mathbb{K}[t_1]$$이다. Global section은 두 chart에서 모두 regular이어야 하므로, $$t_0$$에 대한 degree $$\le k$$인 다항식이다. 따라서 $$\dim H^0(\mathbb{P}^1, \mathcal{O}(k)) = k+1$$이다. ([§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16))

$$k < 0$$인 경우, $$\mathcal{O}(k)$$의 global section은 $$t_0$$에 대해 degree $$\ge 0$$이면서 $$t_0^{-k}$$의 배수이어야 하므로, 이를 만족하는 함수는 $$0$$뿐이다. 따라서 $$H^0(\mathbb{P}^1, \mathcal{O}(k)) = 0$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **$$H^1(\mathbb{P}^1, \mathcal{O}(k))$$의 계산** $$H^1$$은 $$C^1 / \operatorname{im} d^0$$이다. Čech complex에서 $$C^1 = \mathcal{O}(k)(U_0 \cap U_1) = \mathbb{K}[t_0, t_0^{-1}]$$이고, $$\operatorname{im} d^0$$는

$$\operatorname{im} d^0 = \{t_0^{-k} p(t_0^{-1}) - q(t_0) \mid p \in \mathbb{K}[t_0^{-1}],\; q \in \mathbb{K}[t_0]\}$$

이다. 여기서 $$s_0 \in \mathcal{O}(k)(U_0) = \mathbb{K}[t_0]$$은 $$U_0$$-좌표에서의 section이고, $$s_1 \in \mathcal{O}(k)(U_1) = \mathbb{K}[t_1] = \mathbb{K}[t_0^{-1}]$$은 $$U_1$$-좌표에서의 section이며, 이를 $$U_0$$-좌표로 변환하면 $$t_0^{-k}s_1$$이 된다.

$$k \ge 0$$인 경우, $$t_0^{-k}p(t_0^{-1})$$는 degree $$\le -k$$인 항들로 이루어지고, $$q(t_0)$$는 degree $$\ge 0$$인 항들로 이루어진다. 따라서 이들의 차 $$t_0^{-k}p - q$$는 임의의 Laurent 다항식을 만들 수 있으므로 $$\operatorname{im} d^0 = C^1$$이고 $$H^1(\mathbb{P}^1, \mathcal{O}(k)) = 0$$이다.

$$k < 0$$인 경우 (즉 $$-k > 0$$), $$t_0^{-k}p(t_0^{-1}) = t_0^{-k}(a_0 + a_1 t_0^{-1} + \cdots)$$는 degree $$\le -k$$인 항들을 제공하고, $$-q(t_0)$$는 degree $$\ge 0$$인 항들을 제공한다. 두 부분이 동시에 cover하는 degree는 $$\ge 0$$과 $$\le -k$$이며, 그 사이의 간격 $$-1, -2, \ldots, -(-k-1) = k+1$$에 해당하는 항들은 $$\operatorname{im} d^0$$로 표현할 수 없다. 이 간격의 크기가 정확히 $$-k - 1$$이므로 $$\dim H^1(\mathbb{P}^1, \mathcal{O}(k)) = -k - 1$$이다.

</div>

위의 계산을 종합하면 $$\mathbb{P}^1$$의 cohomology가 완전히 결정된다. $$H^0$$과 $$H^1$$의 차원이 서로 반대 방향으로 움직이는 것은 Serre duality의 초기 예시이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> **$$\mathbb{P}^n$$의 cohomology** $$\mathbb{P}^n$$ 위에서도 동일한 방법으로 Čech cohomology를 계산할 수 있다. Standard open cover $$U_i = \{x_i \ne 0\}$$를 사용하면, $$\mathbb{P}^n$$의 line bundle $$\mathcal{O}_{\mathbb{P}^n}(k)$$의 cohomology는 다음과 같다.

$$k \ge 0$$인 경우, $$\dim H^0(\mathbb{P}^n, \mathcal{O}(k)) = \binom{n+k}{k}$$이고 나머지 $$H^i = 0$$ ($$i > 0$$)이다. 여기서 $$H^0(\mathbb{P}^n, \mathcal{O}(k))$$는 degree $$k$$ 동차다항식들의 공간이며, 그 차원 $$\binom{n+k}{k}$$는 $$n+1$$개 변수의 degree $$k$$ 단항식의 개수와 일치한다.

$$k \le -n-1$$인 경우, $$\dim H^n(\mathbb{P}^n, \mathcal{O}(k)) = \binom{-k-1}{n}$$이고 나머지 $$H^i = 0$$ ($$i < n$$)이다. $$H^n$$이 nonzero가 되는 이유는, $$n+1$$개의 chart 중 $$n+1$$개가 겹치는 교차점에서만 nontrivial한 cocycle이 존재할 수 있기 때문이다.

마지막으로 $$-n \le k \le -1$$인 경우, 모든 $$H^i = 0$$이다.

</div>

## Serre Duality 미리보기

Sheaf cohomology의 가장 중요한 응용 중 하나는 ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))에서 도입한 canonical bundle $$\omega_X$$과 관련된 Serre duality이다. 위의 [예시 6](#ex6), [예시 7](#ex7)에서 살펴본 $$\mathbb{P}^1$$의 cohomology는 이미 Serre duality의 특수한 경우로 해석할 수 있다. $$\mathbb{P}^1$$의 canonical bundle은 $$\omega_{\mathbb{P}^1} = \mathcal{O}(-2)$$이며, Serre duality에 의해

$$H^i(\mathbb{P}^1, \mathcal{O}(k))^\ast \cong H^{1-i}(\mathbb{P}^1, \omega_{\mathbb{P}^1} \otimes \mathcal{O}(-k)) = H^{1-i}(\mathbb{P}^1, \mathcal{O}(-k-2))$$

이 성립한다. 이를 $$i=0$$에 적용하면 $$\dim H^0(\mathbb{P}^1, \mathcal{O}(k)) = \dim H^1(\mathbb{P}^1, \mathcal{O}(-k-2))$$을 얻고, [예시 6](#ex6)과 [예시 7](#ex7)의 결과와 정확히 일치하는 것을 확인할 수 있다. 일반적인 정리는 §Serre Duality에서 다룬다.

<div class="misc" markdown="1">
**미리보기 (Serre Duality).** Smooth projective variety $$X$$ of dimension $$n$$과 임의의 locally free sheaf $$\mathcal{E}$$에 대하여, 자연스러운 동형

$$H^i(X, \mathcal{E})^\ast \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$

이 존재한다고 알려져 있다. 특히 $$\mathcal{E} = \mathcal{O}_X$$인 경우 $$H^i(X, \mathcal{O}_X)^\ast \cong H^{n-i}(X, \omega_X)$$이고, $$i = n$$이면 $$H^n(X, \omega_X) \cong \mathbb{K}$$이다. 전체 증명과 응용은 §Serre Duality에서 다룬다.
</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
