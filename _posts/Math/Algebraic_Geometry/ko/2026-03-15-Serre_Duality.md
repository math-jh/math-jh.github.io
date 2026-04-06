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

## 동기

Cohomology는 sheaf를 국소적으로 주어진 자료로부터 전역적으로 재구성하려는 시도의 '실패'를 측정하는 도구이다. ([§Sheaf Cohomology, ⁋명제 2](/ko/math/algebraic_geometry/sheaf_cohomology#prop2)) Sheaf cohomology $$H^i(X, \mathcal{E})$$가 nonzero라는 것은, $$\mathcal{E}$$가 $$X$$ 위에서 국소 trivial해도 전역적으로는 gluing이 불가능함을 의미한다.

이 관점에서 $$\mathbb{P}^n$$ 위에서 $$H^n(\mathbb{P}^n, \mathcal{O}(d))$$의 행동을 살펴보자. $$n$$차 cohomology는 $$d \leq -n-1$$에서만 nonzero이며, 이 threshold는 $$\omega_{\mathbb{P}^n} = \mathcal{O}(-n-1)$$에 의해 정확히 결정된다. 즉, top cohomology가 nonzero가 되는 조건이 canonical bundle과 직접적으로 연결되어 있다.

더 일반적으로 $$n$$차원 smooth projective variety $$X$$ 위에서 $$H^n(X, \omega_X \otimes \mathcal{E}^\vee)$$는 $$\mathcal{E}$$의 global section $$H^0(X, \mathcal{E})$$와 쌍대적이다. Canonical bundle $$\omega_X$$는 top cohomology와 global section 사이의 교량 역할을 하며, 이것이 Serre duality의 본질이다. Duality를 이해한다는 것은, $$\omega_X$$가 왜 이런 교량 역할을 하는지, 그리고 trace map이 이 관계를 어떻게 구체적으로 구현하는지를 이해하는 것이다.

## Statement

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1 (Serre Duality)**</ins> Field $$\mathbb{K}$$ 위의 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

여기서 $$\omega_X$$는 canonical bundle ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))이고 $$\mathcal{E}^\vee = \mathcal{H}om(\mathcal{E}, \mathcal{O}_X)$$는 dual sheaf이다.

</div>

Locally free sheaf $$\mathcal{E}$$에 대해서는 $$\mathcal{H}om(\mathcal{E}, \omega_X) \cong \omega_X \otimes \mathcal{E}^\vee$$가 성립하므로 ([§선다발과 벡터다발, ⁋명제 7](/ko/math/algebraic_geometry/line_bundles#prop7)), 명제의 우변을 $$H^{n-i}(X, \mathcal{H}om(\mathcal{E}, \omega_X))^\ast$$와 같이 쓸 수도 있다. 일반적인 coherent sheaf $$\mathcal{F}$$에 대해서는 $$\omega_X \otimes \mathcal{F}^\vee$$ 대신 Ext group $$\operatorname{Ext}^i(\mathcal{F}, \omega_X)$$를 사용하여 $$\operatorname{Ext}^{n-i}(\mathcal{F}, \omega_X) \cong H^i(X, \mathcal{F})^\ast$$의 형태로 동일한 duality가 성립하지만, 본 글에서는 locally free sheaf에 대한 버전을 다룬다. 또한 Hartshorne의 고전적 증명에서는 $$\mathbb{K}$$가 algebraically closed field라고 가정하지만, Grothendieck duality를 사용하면 임의의 field에 대해 동일한 결과가 성립한다.

Serre duality의 증명은 깊은 정리로, 여러 가지 접근법이 존재한다. 대표적으로, projective space에서의 계산을 바탕으로 finite morphism을 통해 일반적인 variety로 확장하는 방법과, derived category에서 $$\omega_X = f^! \mathcal{O}_{\operatorname{Spec}(\mathbb{K})}$$로 정의한 뒤 derived adjunction으로 duality를 얻는 방법이 있다. 두 방법 모두 본질적으로 동일한 핵심 사실에 기반한다. 즉, $$n$$차 cohomology $$H^n(X, \omega_X)$$와 기저필드 $$\mathbb{K}$$ 사이에 isomorphism (trace map)이 존재하며, 이를 통해 cup product pairing이 완벽한 쌍대성을 이룬다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 특히 $$\mathcal{E} = \mathcal{O}_X$$에 대해:

$$H^i(X, \mathcal{O}_X) \cong H^{n-i}(X, \omega_X)^\ast$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{O}_X^\vee = \mathcal{H}om(\mathcal{O}_X, \mathcal{O}_X) \cong \mathcal{O}_X$$이므로, [명제 1](#prop1)에서 $$\mathcal{E} = \mathcal{O}_X$$를 대입하면 $$\omega_X \otimes \mathcal{O}_X^\vee \cong \omega_X$$를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Curve)**</ins> Genus $$g$$인 smooth curve $$C$$를 생각하자. 여기서 genus는 $$g = \dim H^1(C, \mathcal{O}_C)$$로 정의된다. $$C$$는 $$1$$차원이므로 [명제 2](#prop2)에서 $$n = 1$$을 대입하면 다음을 얻는다.

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

## Derived Category

Grothendieck duality를 기술하기 위해서는 derived category의 기본 개념이 필요하다. 이 섹션에서는 그 핵심 아이디어를 소개한다.

### Exact functor의 문제와 derived functor의 동기

우리는 이미 short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$에 왼쪽 exact functor를 적용하면 오른쪽에서 exactness가 깨지는 현상을 알고 있다. 대표적인 예가 sheaf pushforward $$f_\ast$$이다. $$f_\ast$$를 적용하면 $$0 \to f_\ast \mathcal{F}' \to f_\ast \mathcal{F} \to f_\ast \mathcal{F}''$$는 exact하지만, $$f_\ast \mathcal{F}'' \to 0$$에서 사상이 일반적으로 surjective하지 않다. 이 gap을 측정하는 것이 바로 higher direct image $$R^i f_\ast$$이며, long exact sequence

$$0 \to f_\ast \mathcal{F}' \to f_\ast \mathcal{F} \to f_\ast \mathcal{F}'' \xrightarrow{\delta} R^1 f_\ast \mathcal{F}' \to R^1 f_\ast \mathcal{F} \to \cdots$$

를 얻는다. 그런데 $$R^i f_\ast$$는 각 차수마다 따로따로 정의된 sheaf이다. Vanishing과 non-vanishing이 여러 차수에서 동시에 발생하며, 이들을 개별적으로 추적하는 것은 복잡하고 불편하다. 예를 들어 $$R^2 f_\ast \mathcal{F} = 0$$이라는 사실이 $$R^3 f_\ast \mathcal{F}$$의 계산에 어떻게 영향을 미치는지를 한 차수씩 따지는 것은 비효율적이다.

더 근본적으로, sheaf 하나가 아니라 **complex 전체**를 functor에 입력하고 싶은 상황이 자연스럽게 발생한다. Cohomology를 계산할 때 우리는 이미 암묵적으로 이를 하고 있다. $$\mathcal{F}$$의 cohomology를 계산하기 위해 injective resolution $$0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \cdots$$을 만들고, 각 $$\mathcal{I}^i$$에 $$f_\ast$$를 적용한 뒤, 전체 complex의 cohomology를 취한다. 즉 우리의 관심 대상은 개별 sheaf가 아니라 complex 그 자체에 있다. 이것이 derived category를 도입하는 핵심 동기이다.

### Complex와 cohomology

<div class="definition" markdown="1">

<ins id="def6">**정의 6 (Complex와 Quasi-isomorphism)**</ins> Abelian category $$\mathcal{A}$$ 위의 *complex* $$\mathcal{F}^\bullet$$은 $$\mathcal{A}$$의 사상들 $$d^i \colon \mathcal{F}^i \to \mathcal{F}^{i+1}$$로 이루어진 열 $$(\cdots \to \mathcal{F}^{-1} \to \mathcal{F}^0 \to \mathcal{F}^1 \to \cdots)$$로, $$d^{i+1} \circ d^i = 0$$을 만족하는 것이다. Complex $$\mathcal{F}^\bullet$$의 $$i$$차 cohomology는 $$H^i(\mathcal{F}^\bullet) = \ker d^i / \operatorname{im} d^{i-1}$$이다. 두 complex 사이의 사상 $$f \colon \mathcal{F}^\bullet \to \mathcal{G}^\bullet$$이 모든 차수에서 cohomology에 isomorphism을 유도하면, 이를 *quasi-isomorphism*이라 부른다.

</div>

Complex라는 개념은 생각보다 친숙하다. Sheaf $$\mathcal{F}$$의 injective resolution $$0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \cdots$$도 complex이다. 이 complex의 cohomology는 $$H^0(\mathcal{I}^\bullet) = \mathcal{F}$$이고, $$i \geq 1$$에 대해서는 $$H^i(\mathcal{I}^\bullet) = 0$$이다. 즉 resolution은 $$\mathcal{F}$$를 유일하게 남기고 나머지 차수의 cohomology를 모두 0으로 만드는 complex이다. 마찬가지로 Čech complex도 complex의 예시이며, 이 complex의 cohomology는 Čech cohomology group과 일치한다.

Quasi-isomorphism은 cohomology의 관점에서 볼 때 본질적으로 isomorphism과 같다. 두 complex가 cohomology group이 모두 같다면, 우리가 관심을 갖는 정보는 동일하다. 그러나 category의 구조상 quasi-isomorphism의 역사상이 존재하지 않을 수 있다. 예를 들어 어떤 complex가 다른 complex의 resolution일 때, resolution에서 원래 complex로 돌아가는 사상은 일반적으로 존재하지 않는다. 이 문제를 해결하기 위해 quasi-isomorphism을 강제로 invert하여 얻은 category가 derived category이다.

### Derived category와 resolution의 대체

<div class="definition" markdown="1">

<ins id="def7">**정의 7 (Derived Category)**</ins> Abelian category $$\mathcal{A}$$의 *derived category* $$D(\mathcal{A})$$는 $$\mathcal{A}$$ 위의 complex들이 이루는 category에서 quasi-isomorphism을 형식적으로 invert하여 얻은 category이다.

</div>

"Quasi-isomorphism을 invert한다"는 것의 구체적인 의미는 다음과 같다. Category $$\mathcal{C}$$에서 어떤 사상 $$f$$의 역사상을 강제로 추가하는 것은, 선대수학에서 $$f$$를 포함하는 분모로 localize하는 것과 같다. 이렇게 하면 quasi-isomorphism인 사상은 derived category에서 genuine isomorphism이 된다.

이것의 가장 중요한 결과는 **resolution으로 대체할 수 있다**는 점이다. Sheaf $$\mathcal{F}$$와 그 injective resolution $$\mathcal{F} \to \mathcal{I}^\bullet$$ 사이에는 quasi-isomorphism이 존재하므로, derived category에서 $$\mathcal{F}$$와 $$\mathcal{I}^\bullet$$은 isomorphism이다. 따라서 $$\mathcal{F}$$를 직접 다루는 대신 $$\mathcal{I}^\bullet$$을 다루어도 결과가 같다. 이것이 derived functor의 기본 아이디어이다: exact하지 않은 functor를 다룰 때, 대상을 resolution으로 치환한 뒤 functor를 적용하면 정보 손실 없이 결과를 얻을 수 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8 (Shift Functor)**</ins> Derived category $$D(\mathcal{A})$$ 위의 *shift functor* $$[n]\colon D(\mathcal{A}) \to D(\mathcal{A})$$는 complex $$\mathcal{F}^\bullet$$을 $$n$$칸 이동시키는 것이다. 구체적으로 $$(\mathcal{F}[n])^i = \mathcal{F}^{i+n}$$이고, 미분 사상의 부호가 $$(-1)^n$$만큼 바뀐다. Cohomology에 대해서는 $$H^i(\mathcal{F}[n]) = H^{i+n}(\mathcal{F})$$가 성립한다.

</div>

Shift functor는 Serre duality를 이해하는 데 필수적이다. 예를 들어 $$n$$차원 smooth variety $$X$$ 위에서 $$f^! \mathcal{O}_Y$$는 sheaf $$\omega_X$$가 아니라 complex $$\omega_X[n]$$이다. 여기서 $$[n]$$의 의미는 cohomology 차수를 $$n$$만큼 밀어올리는 것으로, 이 shift가 있어야지만 Serre duality의 isomorphism $$H^i(\mathcal{E}) \cong H^{n-i}(\omega_X \otimes \mathcal{E}^\vee)^\ast$$의 차수가 맞게 떨어진다. 구체적으로, $$\mathbf{R}\mathcal{H}om(\mathcal{E}, \omega_X[n])$$의 cohomology는 $$H^{-i}(\mathbf{R}\mathcal{H}om(\mathcal{E}, \omega_X[n])) = H^{-i}(\mathbf{R}\mathcal{H}om(\mathcal{E}, \omega_X)[n]) = H^{n-i}(\mathbf{R}\mathcal{H}om(\mathcal{E}, \omega_X))$$가 되어, $$i$$와 $$n-i$$의 관계가 자연스럽게 나타난다.

### Derived functor

Derived category에서 exact하지 않은 functor를 다루는 표준적인 방법은 derived functor이다. Sheaf pushforward $$f_\ast$$가 왼쪽 exact하므로, 이를 확장한 *right derived functor* $$R f_\ast$$를 정의한다. 구체적으로, complex $$\mathcal{F}^\bullet$$을 injective resolution $$\mathcal{F}^\bullet \to \mathcal{I}^\bullet$$로 치환한 뒤 $$f_\ast$$를 차수별로 적용하여 $$R f_\ast(\mathcal{F}^\bullet) = f_\ast \mathcal{I}^\bullet$$를 얻는다. 여기서 $$\mathcal{F}^\bullet$$이 단일 sheaf $$\mathcal{F}$$ (즉 $$\mathcal{F}$$가 $$0$$번째 차수에만 있고 나머지는 $$0$$인 complex)라면, cohomology를 취했을 때 $$H^i(R f_\ast \mathcal{F}) = R^i f_\ast \mathcal{F}$$가 성립하며, 이는 우리가 이미 알고 있는 higher direct image sheaf이다. 즉 $$R f_\ast$$는 $$R^i f_\ast$$를 모든 차수에서 동시에 포착하는 complex 수준의 functor이다.

마찬가지로, sheaf Hom $$\mathcal{H}om(-, -)$$도 첫 번째 변수에 대해 왼쪽 exact하므로 derived version인 $$\mathbf{R}\mathcal{H}om$$을 정의한다. $$\mathcal{F}$$를 injective resolution로 치환한 뒤 $$\mathcal{H}om$$을 적용하면 된다. Ext group과의 관계는 다음과 같다. $$\mathbf{R}\mathcal{H}om(\mathcal{F}, \mathcal{G})$$는 일반적으로 nonzero인 여러 차수에 걸쳐 nonzero cohomology를 갖는 complex이며, $$\operatorname{Ext}^i(\mathcal{F}, \mathcal{G})$$는 이 complex의 $$-i$$차 cohomology이다. 즉

$$\operatorname{Ext}^i(\mathcal{F}, \mathcal{G}) = H^{-i}(\mathbf{R}\mathcal{H}om(\mathcal{F}, \mathcal{G}))$$

이다. 예를 들어 $$\mathcal{F} = \mathcal{G} = \mathcal{O}_X$$이면 $$\mathbf{R}\mathcal{H}om(\mathcal{O}_X, \mathcal{O}_X)$$는 $$\mathcal{O}_X$$만 남는 complex이므로 $$\operatorname{Ext}^0(\mathcal{O}_X, \mathcal{O}_X) = \mathbb{K}$$이고 $$i \geq 1$$에서 $$\operatorname{Ext}^i = 0$$이다. Locally free sheaf $$\mathcal{E}$$에 대해서는 $$\mathbf{R}\mathcal{H}om(\mathcal{E}, \mathcal{G}) \cong \mathcal{E}^\vee \otimes \mathcal{G}$$가 성립하므로 역시 단일 차수에만 nonzero cohomology를 갖는다.

Derived category에서 derived functor를 다루는 장점은 단일 차수의 정보가 아니라 **complex 전체**를 하나의 대상으로 취급할 수 있다는 점이다. 특히 adjunction 같은 범주론적 구조가 complex 수준에서 훨씬 깔끔하게 성립한다.

### Triangulated category

Derived category $$D(\mathcal{A})$$는 단순한 category가 아니라 *triangulated category*이다. 이 구조는 abelian category에서 short exact sequence가 하던 역할을 derived category에서 대신한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9 (Distinguished Triangle)**</ins> Derived category $$D(\mathcal{A})$$에서 *distinguished triangle*은 다음 형태의 삼각형이다.

$$A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} A[1]$$

여기서 $$C$$는 사상 $$f$$의 *mapping cone*이라 불리며, $$f$$가 "얼마나 isomorphism에서 벗어나는지"를 측정한다.

</div>

Distinguished triangle의 직관은 short exact sequence의 "derived version"이라는 것이다. Abelian category에서 short exact sequence $$0 \to \mathcal{F}' \xrightarrow{f} \mathcal{F} \xrightarrow{g} \mathcal{F}'' \to 0$$이 있으면 long exact sequence

$$\cdots \to H^i(\mathcal{F}') \xrightarrow{H^i(f)} H^i(\mathcal{F}) \xrightarrow{H^i(g)} H^i(\mathcal{F}'') \xrightarrow{\delta} H^{i+1}(\mathcal{F}') \to \cdots$$

를 얻는다. Mapping cone은 이 연결 사상 $$\delta$$를 범주론적으로 내재화한 것이다. $$f$$가 isomorphism이면 mapping cone의 cohomology는 모두 $$0$$이 되고, $$f$$가 isomorphism에서 멀수록 mapping cone의 cohomology가 커진다. 예를 들어, short exact sequence에서 $$\mathcal{F}' \to \mathcal{F}$$의 mapping cone은 $$\mathcal{F}''[0]$$과 quasi-isomorphic하며, 이것이 long exact sequence를 유도하는 근원이다.

Mapping cone을 더 구체적으로 이해해보자. 두 complex 사이의 사상 $$f \colon A^\bullet \to B^\bullet$$이 주어졌을 때, mapping cone $$C^\bullet$$은 차수별로 $$C^i = B^i \oplus A^{i+1}$$이고 미분 사상이 $$(b, a) \mapsto (d_B b + f(a), -d_A a)$$로 주어지는 complex이다. 이 정의에서 $$f = 0$$이면 $$C^\bullet \cong B^\bullet \oplus A^\bullet[1]$$이 되어 cohomology가 단순히 합쳐지고, $$f$$가 isomorphism이면 $$C^\bullet$$의 cohomology가 $$0$$이 된다. 일반적인 경우에는 cohomology long exact sequence가 나타난다.

Triangulated 구조의 중요성은 다음과 같다. Derived functor가 exact functor처럼 "triangles을 triangles으로 보낸다"는 성질이 성립한다. 즉 $$T$$가 triangulated functor이고 $$A \to B \to C \to A[1]$$가 distinguished triangle이면, $$T(A) \to T(B) \to T(C) \to T(A)[1]$$도 distinguished triangle이다. 이 성질은 derived adjunction을 논의할 때 핵심적인 역할을 한다.

### Adjunction in derived category

Sheaf category에서 이미 다음 adjunction을 알고 있다. Proper morphism $$f \colon X \to Y$$에 대해

$$\mathcal{H}om(f^\ast \mathcal{F}, \mathcal{G}) \cong \mathcal{H}om(\mathcal{F}, f_\ast \mathcal{G})$$

가 성립한다. 그러나 $$f_\ast$$는 exact하지 않으므로, derived version을 생각하면 이 adjunction의 형태가 달라진다. Derived category에서 $$f^\ast$$의 derived version $$Lf^\ast$$는 여전히 왼쪽 adjoint이지만, $$f_\ast$$의 derived version $$R f_\ast$$의 오른쪽 adjoint는 단순한 $$f^!$$가 아니라 별도의 functor $$f^!$$로 주어진다. 즉

$$\operatorname{Hom}_{D(Y)}(R f_\ast \mathcal{F}, \mathcal{G}) \cong \operatorname{Hom}_{D(X)}(\mathcal{F}, f^! \mathcal{G})$$

가 성립한다. 이 adjoint $$f^!$$는 derived category에서만 정의되며, sheaf category 수준에서는 올바른 의미를 갖지 않는다.

$$f^!$$가 왜 "special"한지를 이해해보자. 보통 adjoint의 존재는 까다롭다. $$f^\ast \dashv f_\ast$$의 adjunction에서 $$f_\ast$$가 exact하지 않기 때문에, derived category로 넘어가면 $$R f_\ast$$의 right adjoint가 $$f^\ast$$가 아닌 전혀 다른 functor $$f^!$$가 된다. 직관적으로 $$f^!$$는 "$$R f_\ast$$에 의해 손실된 정보를 복원하는" functor이다. 특히 $$Y = \operatorname{Spec}(\mathbb{K})$$인 경우, 구조 사상 $$f \colon X \to \operatorname{Spec}(\mathbb{K})$$에 대해 $$f^! \mathcal{O}_Y = \omega_X[n]$$이 성립하며, 여기서 $$\omega_X$$는 canonical bundle이고 $$n = \dim X$$이다. 즉 canonical bundle은 이 derived adjunction에 의해 자연스럽게 정의된다. 이것이 Serre duality에서 $$\omega_X$$가 등장하는 근본적인 이유이다.

## Grothendieck Duality

Serre duality는 variety $$X$$를 하나의 점 $$\operatorname{Spec}(\mathbb{K})$$로 보내는 상사상에 대한 특수한 경우이다. Grothendieck는 이를 임의의 proper morphism으로 일반화하였다. Proper morphism $$f \colon X \to Y$$는 위상수학적으로 compact map의 대수기하학적 대응물로, 임의의 base change에 대해 닫힌 사상이 되는 사상이다.

Serre duality에서 canonical bundle $$\omega_X$$가 핵심적인 역할을 하였듯이, relative 상황에서는 relative dualizing sheaf $$\omega_{X/Y}$$가 그 역할을 담당한다. 이는 섬유 $$f^{-1}(y)$$ 각각에서 canonical sheaf를 일관되게 모아둔 것이며, Serre duality에서 $$\omega_X$$가 하던 역할을 상대적인 상황으로 옮긴 것이다. 구체적으로 $$\omega_{X/Y}$$는 derived pullback $$f^!$$에 의해 $$\omega_{X/Y} = f^! \mathcal{O}_Y$$로 정의된다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (Grothendieck Duality)**</ins> Smooth projective variety 사이의 proper morphism $$f \colon X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해, derived category에서 다음 isomorphism이 성립한다:

$$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

여기서 $$f^!$$는 $$R f_\ast$$의 right adjoint이고, $$\mathcal{G}$$는 $$Y$$ 위의 coherent sheaf의 bounded below complex이다. 특히 $$f$$가 smooth morphism of relative dimension $$n$$이면 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$이고, 여기서 $$\omega_{X/Y}$$는 relative canonical sheaf이다.

</div>

이 정리의 의미를 직관적으로 이해해보자. $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G})$$는 $$\mathcal{F}$$와 $$f^! \mathcal{G}$$ 사이의 '모든 가능한 Hom'을 모은 complex이며, $$R f_\ast$$를 적용하면 이를 $$Y$$ 위로 pushforward한다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$는 pushforward된 $$\mathcal{F}$$와 $$\mathcal{G}$$ 사이의 '모든 가능한 Hom'이다. 즉, 'pushforward 후 Hom'과 'Hom 후 pushforward'가 같다는 뜻이다. 본 글에서는 정리의 형태만 소개하며, 증명과 상세한 논의는 추후 별도의 글에서 다룬다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$Y = \operatorname{Spec}(\mathbb{K})$$이고 $$X$$가 $$n$$차원 smooth projective variety인 경우를 생각하자. 구조 사상 $$f \colon X \to \operatorname{Spec}(\mathbb{K})$$에 대해 $$R f_\ast \mathcal{F}$$의 cohomology는 단순히 cohomology group $$H^i(X, \mathcal{F})$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{O}_Y)$$의 cohomology는 dual vector space $$H^i(X, \mathcal{F})^\ast$$이다. 또한 $$f$$는 smooth of relative dimension $$n$$이므로 $$f^! \mathcal{O}_Y \cong \omega_X[n]$$이다. 따라서 [명제 10](#prop10)에서 $$\mathcal{G} = \mathcal{O}_Y$$, $$\mathcal{F}$$를 locally free sheaf로 취하면 cohomology 수준에서 $$H^i(X, \omega_X \otimes \mathcal{E}^\vee) \cong H^{n-i}(X, \mathcal{E})^\ast$$을 얻으며, 이는 정확히 [명제 1](#prop1)의 Serre duality이다. 즉 Serre duality는 Grothendieck duality의 특수한 경우이다.

</div>

## Trace Map

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> *Trace map* $$\operatorname{Tr} \colon H^n(X, \omega_X) \to \mathbb{K}$$는 Serre duality의 isomorphism을 실제로 구현하는 핵심 구조이다. 이는 $$H^n(X, \omega_X)$$에서 $$\mathbb{K}$$로의 isomorphism으로, Serre duality가 $$\mathcal{E} = \mathcal{O}_X$$인 경우 $$H^0(X, \omega_X) \cong H^n(X, \mathcal{O}_X)^\ast$$를 얻고, $$\mathcal{E} = \omega_X$$인 경우 $$H^n(X, \omega_X) \cong H^0(X, \mathcal{O}_X)^\ast \cong \mathbb{K}$$를 얻는 것과 양립하여야 한다. 즉 trace map은 $$H^n(X, \omega_X) \cong \mathbb{K}$$라는 사실을 구체적으로 실현하는 것이다.

직관적으로 trace map은 미분기하학에서 적분에 해당하는 연산이다. $$n$$차원 variety $$X$$ 위에서 $$\omega_X$$는 differential form들의 bundle이므로 ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24)), $$H^n(X, \omega_X)$$는 $$X$$ 전체에 걸쳐 "적분할 수 있는" top-degree form들의 공간이며, trace map은 이 적분을 기저필드 $$\mathbb{K}$$의 원소로 평가하는 것이다. 복소기하학에서 $$X$$가 compact complex manifold이면 trace map은 실제로 적분 $$\eta \mapsto \int_X \eta$$로 주어진다.

</div>

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Serre duality의 isomorphism은 trace map과 cup product를 사용하여 다음과 같이 명시적으로 주어진다.

$$H^i(X, \mathcal{E}) \to H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast;\quad \alpha \mapsto \left( \beta \mapsto \operatorname{Tr}(\alpha \smile \beta) \right)$$

여기서 $$\smile$$은 cup product로, $$\alpha \in H^i(X, \mathcal{E})$$와 $$\beta \in H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$로부터 $$\alpha \smile \beta \in H^n(X, \mathcal{E} \otimes (\omega_X \otimes \mathcal{E}^\vee))$$를 만들어낸다. 여기에 자연스러운 평가 사상 $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_X$$를 적용하면 $$H^n(X, \omega_X)$$의 원소를 얻으며, trace map을 적용하여 최종적으로 $$\operatorname{Tr}(\alpha \smile \beta) \in \mathbb{K}$$를 얻는다. 이 쌍선형 형식의 비퇴화성이 곧 Serre duality의 isomorphism을 준다.

</div>

Cup product의 구성을 구체적으로 살펴보자. Coherent sheaf cohomology에서 cup product는 sheaf resolution의 수준에서 정의된다. 구체적으로, $$\mathcal{E}$$와 $$\omega_X \otimes \mathcal{E}^\vee$$의 injective resolution을 이용하여 $$\alpha \smile \beta \in H^n(X, \mathcal{E} \otimes (\omega_X \otimes \mathcal{E}^\vee))$$를 구성한다. 여기에 evaluation map $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_X$$를 tensor하여 $$H^n(X, \omega_X \otimes \mathcal{O}_X) \cong H^n(X, \omega_X)$$의 원소를 얻고, trace map으로 $$\mathbb{K}$$의 원소를 얻는다. 이 전체 과정이 [명제 13](#prop13)의 쌍선형 형식을 구성한다.

## 응용: Euler Characteristic

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Serre duality에 의해 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 다음이 성립한다.

$$\rchi(\mathcal{E}) = (-1)^n \rchi(\omega_X \otimes \mathcal{E}^\vee)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euler characteristic의 정의와 [명제 1](#prop1)에 의해

$$\rchi(\mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$

이다. 여기서 치환 $$j = n - i$$를 적용하면

$$\sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee) = \sum_{j=0}^{n} (-1)^{n-j} \dim H^j(X, \omega_X \otimes \mathcal{E}^\vee) = (-1)^n \rchi(\omega_X \otimes \mathcal{E}^\vee)$$

을 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex15">**예시 15 (Curve)**</ins> Curve $$C$$와 line bundle $$\mathcal{L}$$에 대해, [명제 14](#prop14)에서 $$n = 1$$을 대입하면

$$\rchi(\mathcal{L}) = -\rchi(\omega_C \otimes \mathcal{L}^\vee)$$

이다. 한편 Euler characteristic의 정의에 의해 $$\rchi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^1(C, \mathcal{L})$$이고, Serre duality에 의해 $$\dim H^1(C, \mathcal{L}) = \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$이므로

$$\rchi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$

이다. 이 공식은 Riemann-Roch theorem의 출발점이 된다.

</div>

## Relative Duality

Smooth projective morphism $$f \colon X \to Y$$는 임의의 점 $$y \in Y$$에 대해 섬유 $$f^{-1}(y)$$가 smooth projective variety가 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 이런 상황에서 섬유별 canonical sheaf를 일관되게 모은 것이며, 각 섬유 $$X_y$$에서 $$\omega_{X/Y}\vert_{X_y} \cong \omega_{X_y}$$가 성립한다. 앞서 명제 10에서 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$으로 정의하였다.

Serre duality에서 $$H^n(X, \omega_X) \cong \mathbb{K}$$였던 사실은, relative situation에서 다음과 같이 일반화된다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Smooth projective morphism $$f \colon X \to Y$$에서 $$n = \dim X - \dim Y$$라 하자. 그럼

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

이며, $$i \neq n$$에 대해서는 $$R^i f_\ast \omega_{X/Y} = 0$$이다.

</div>

이 정리는 relative situation에서도 "top cohomology of canonical sheaf = 1"이라는 직관이 그대로 성립함을 보여준다. 실제로 [명제 10](#prop10)에서 $$\mathcal{F} = \mathcal{O}_X$$, $$\mathcal{G} = \mathcal{O}_Y$$를 대입하면 $$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \omega_{X/Y}[n]$$이므로 좌변은 $$R f_\ast \omega_{X/Y}[n]$$이 된다. 이 complex의 $$0$$차 cohomology sheaf를 취하면 $$R^n f_\ast \omega_{X/Y}$$를 얻는다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$의 $$0$$차 cohomology는 $$\mathcal{H}om_{\mathcal{O}_Y}(f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이며, smooth projective morphism에서는 섬유가 geometrically integral이므로 $$f_\ast \mathcal{O}_X = \mathcal{O}_Y$$가 성립하여 이는 $$\mathcal{O}_Y$$가 되어 [명제 16](#prop16)의 첫 번째 주장을 얻는다. Relative duality의 증명과 응용에 대해서는 추후 별도의 글에서 다룬다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.