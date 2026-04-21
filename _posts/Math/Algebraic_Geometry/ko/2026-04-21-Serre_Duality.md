---
title: "세르 쌍대성"
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/serre_duality
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Serre_Duality.png
    overlay_filter: 0.5

date: 2026-04-21
last_modified_at: 2026-04-22
weight: 15
published: false
---

기하적으로 좋은 경우 dimension $$k$$의 cohomology와 codimension $$k$$ cohomology 사이에는 자연스러운 쌍대성이 존재한다. 이를 증명하기 위해 우리는 perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

을 사용했으며, 이를 통해 [\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정리 11](/ko/math/algebraic_topology/Poincare_duality#thm11)와 같은 결과를 얻었다. 더 구체적으로, 이 pairing은 cap product와 fundamental class $$[M] \in H_n(M;R)$$를 통해 구성되므로 위상수학에서 duality의 원천은 orientation class $$[M]$$이라 할 수 있다. 

이번 글에서 우리는 대수기하학 버전의 duality인 Serre duality를 살펴본다. 

## 사영공간에서의 세르 쌍대성

우리는 우선 $$X=\mathbb{P}^n$$인 경우만 엄밀하게 살펴본다. 우리는 $$\mathbb{P}^n$$ 위에 정의된 line bundle은 모두 $$\mathcal{O}(d)$$의 꼴인 것을 알고 있으며, 특히 [§표준선다발, ⁋명제 7](/ko/math/algebraic_geometry/canonical_bundle#prop7)에서 이것이 $$\mathcal{O}(-n-1)$$임을 살펴보았다. 그럼 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)에서 우리는 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Projective space $$X=\mathbb{P}^n$$ 위의 canonical line bundle $$\omega_X$$에 대하여, isomorphism

$$H^n(X, \omega_X)\cong \mathbb{K}$$

이 존재한다. 

</div>

일반적으로 이는 명시적으로 $$\x_0^{-1}\cdots\x_n^{-1}$$을 basis로 두는 isomorphism으로 이해되지만, scalar multiplication에 대해서만 유일하게 결정된다. 이렇게 normalization을 택하는 것은 구체적으로 *trace map* $$\tr:H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \to \mathbb{K}$$을 택하는 것과 같다. 

이제 duality pairing을 얻기 위해서는 cup product를 정의해야 한다. 편의상 Čech cohomology 레벨에서 생각하자. 임의의 위상공간 $$X$$와 $$X$$의 open cover $$\mathcal{U}$$, 그리고 $$X$$ 위에 정의된 sheaf $$\mathcal{F}$$, $$\mathcal{G}$$에 대하여, 두 Čech cochain $$\alpha \in \check{C}^i(\mathcal{U}, \mathcal{F})$$, $$\beta \in \check{C}^j(\mathcal{U}, \mathcal{G})$$의 cup product를 다음의 식

$$(\alpha \smile \beta)_{i_0, \ldots, i_{i+j}} = \alpha_{i_0,\ldots,i_i}\big\vert_{U_{i_0,\ldots,i_{i+j}}} \otimes \beta_{i_i,\ldots,i_{i+j}}\big\vert_{U_{i_0,\ldots,i_{i+j}}}\in \check{C}^{i+j}(\mathcal{U}, \mathcal{F}\otimes\mathcal{G})$$

으로 정의한다. 우리는 이것이 cohomology 레벨로 떨어진다는 것을 명시적으로 계산할 수 있으며, 이로부터 다음의 함수

$$\smile:\check{H}^i(\mathcal{U}, \mathcal{F}) \times \check{H}^j(\mathcal{U}, \mathcal{G}) \to \check{H}^{i+j}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$

가 정의된다. Sheaf cohomology 레벨에서도 $$\mathcal{F}$$와 $$\mathcal{G}$$의 injective resolution $$\mathcal{I}^\bullet$$, $$\mathcal{J}^\bullet$$을 각각 잡은 후, 이들의 tensor product complex (즉 각각의 성분이 $$\mathcal{I}^p\otimes \mathcal{J}^q$$인 double complex의 total complex)가 $$\mathcal{F}\otimes \mathcal{G}$$의 resolution을 정의한다는 사실을 이용하면 이를 정의할 수 있다. 

어쨌든, cup product pairing에 의하여 우리는 임의의 locally free sheaf $$\mathcal{E}$$와 $$\omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee$$의 cocycle에 대하여 다음의 bilinear map

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

을 얻은 후, isomorphism $$\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$$과 위에서의 trace map을 활용하여 bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}$$

를 얻는다. 우리는 이를 $$\mathcal{O}(d)$$의 경우에 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)에서 직접 계산하여 non-degeneracy를 보이고, syzygy theorem을 사용하여 이 non-degeneracy를 일반적인 locally free sheaf $$\mathcal{E}$$에 대하여 보일 수 있다.

지금까지의 논의에서 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Serre duality pairing, projective case)**</ins> $$\mathbb{P}^n$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E}) \times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \to \mathbb{K};\quad (\alpha, \beta) \mapsto \tr(\alpha \smile \beta)$$

은 perfect pairing이다.

</div>

더 명시적으로, 일반적으로 Serre duality는 이로부터 얻어지는 다음의 isomorphism

$$H^k(\mathbb{P}^n, \mathcal{E})\cong H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)^\ast$$

를 의미한다. 

더 일반적으로, Noether normalization theorem에 의해 임의의 $$n$$차원 smooth projective variety $$X$$에 대하여 finite surjective morphism $$f: X \to \mathbb{P}^n$$이 존재한다. 그럼 우리는 이 finite morphism $$f$$를 통해 $$\mathbb{P}^n$$에서 증명한 Serre duality를 $$X$$로 옮겨올 수 있으며, 이러한 세팅에서 Serre duality는 다음 isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

을 의미한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{P}^2$$에서 [명제 2](#prop2)가 어떻게 작동하는지 확인해보자. 우선 $$\omega_{\mathbb{P}^2} \cong \mathcal{O}(-3)$$이므로, Serre duality는 $$H^i(\mathbb{P}^2, \mathcal{O}(d)) \cong H^{2-i}(\mathbb{P}^2, \mathcal{O}(-d-3))^\ast$$을 준다.

$$d = 0$$인 경우를 생각하자. [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)에 의해 $$H^0(\mathbb{P}^2, \mathcal{O}) = \mathbb{K}$$, $$H^1(\mathbb{P}^2, \mathcal{O}) = 0$$, $$H^2(\mathbb{P}^2, \mathcal{O}) = 0$$이다. 한편 $$\mathcal{O}(-3)$$의 cohomology는 $$H^0(\mathbb{P}^2, \mathcal{O}(-3)) = 0$$, $$H^1(\mathbb{P}^2, \mathcal{O}(-3)) = 0$$, $$H^2(\mathbb{P}^2, \mathcal{O}(-3)) = \mathbb{K}$$이다. 따라서 Serre duality는 $$i = 0$$일 때 $$H^0(\mathcal{O}) = \mathbb{K} \cong H^2(\mathcal{O}(-3))^\ast = \mathbb{K}$$를, $$i = 1$$일 때 $$H^1(\mathcal{O}) = 0 \cong H^1(\mathcal{O}(-3))^\ast = 0$$을, $$i = 2$$일 때 $$H^2(\mathcal{O}) = 0 \cong H^0(\mathcal{O}(-3))^\ast = 0$$을 각각 준다. 모든 경우에 차원이 정확히 대응함을 확인할 수 있다.

$$d = 1$$인 경우도 살펴보자. Bott's formula에 의해 $$H^0(\mathbb{P}^2, \mathcal{O}(1)) = \mathbb{K}^3$$이고 나머지 cohomology는 모두 0이다. Serre duality에 의해 $$H^0(\mathcal{O}(1)) \cong H^2(\mathcal{O}(-4))^\ast$$이어야 하므로 $$\dim H^2(\mathcal{O}(-4)) = 3$$이다. 실제로 $$\mathcal{O}(-4)$$의 $$H^2$$는 $${n+q \choose n} = {2+(-4) \choose 2} = {-2 \choose 2} = 3$$로 계산되어 일치한다.

</div>

## 세르 쌍대성의 일반화

우리는 지금까지의 논의를 일반화시킨다. 가장 처음으로 할 수 있는 것은 locally free sheaf $$\mathcal{E}$$를 임의의 coherent sheaf $$\mathcal{E}$$로 확장하는 것이다. 이는 생각보다 어려운 일은 아닌데, smooth variety에서는 임의의 coherent sheaf가 finite length locally free resolution을 갖기 때문으로, Serre duality의 주장을 귀납적으로 사용하면 된다. ([§표준선다발, ⁋정의 1](/ko/math/algebraic_geometry/canonical_bundle#def1))

그 후 우리는 $$X$$에서 smooth 조건을 포기한다. 이 경우 크게 두 가지의 문제가 있는데, 처음으로 보이는 문제는 $$X$$가 canonical line bundle을 갖지 않는다는 사실이다. 또 다른 문제는 약간 미묘한 것으로, 우리는 perfect pairing에서 명시적인 isomorphism을 얻어낼 때 다소 implicit하게 다음의 isomorphism

$$\mathcal{H}om(\mathcal{E}, \mathcal{F})\cong \mathcal{E}^\vee\otimes \mathcal{F}$$

를 사용하였으나, 실제로 이는 $$\mathcal{E}$$가 locally free이기 때문에 가능한 것으로, 만일 $$\mathcal{E}$$가 coherent sheaf이고 $$X$$가 singular라면 $$\mathcal{E}$$가 finite length locally free resolution을 갖는다는 보장이 없으므로 이 isomorphism이 성립하지 않는다. 때문에 우리는 다시 derived functor를 도입하여, 다음의 식

$$\Ext^i_X(\mathcal{F},\omega_X)\cong H^{n-i}(X,\mathcal{F})^\vee$$

을 만족하는 $$\omega_X$$를 $$X$$의 *dualizing sheaf*라 부른다. 일반적으로 이는 Cohen-Macaulay variety of pure dimension $$n$$에 대하여는 그 존재성이 보장되며, 정의를 내리지는 않을 것이지만 Cohen-Macaulay condition은 직관적으로 차원 문제를 일으키지 않는 singular variety들을 포함하는 개념이라 생각하면 된다.[^1]

조금 덜 직관적인 버전의 일반화는 relative Serre duality이다. 우리는 그 동안 variety의 underlying field $$\mathbb{K}$$에 대해 신경을 쓰지 않은 것이 사실이지만, 이 맥락에서는 그 역할을 명확하게 하는 것이 도움이 된다. 우리는 



우선 더 직관적인 방향의 일반화는 $$X$$에서 smooth 조건을 포기하는 것이다. 이 경우, $$X$$는 canonical line bundle을 갖지 않으므로 Serre duality를 설명할 때 주의해야 한다. 

또 다른 주의사항 중 하나는, 일반적으로 smooth variety에서는 locally free sheaf $$\mathcal{E}$$에 대하여 


지금까지의 논의는 variety가 smooth할 때 성립하지만, $$X$$가 singular point를 갖는 경우에는 canonical line bundle $$\omega_X$$가 정의되지 않으므로, 이 경우에는 *dualizing sheaf*의 개념을 사용하여 Serre duality를 서술할 수 있다. 

$$\operatorname{Ext}^i_X(\mathcal{F}, \omega_X)\cong H^{n-i}(X, \mathcal{F})^\vee$$

를 만족하는 sheaf이며, $$X$$가 smooth일 때는 canonical bundle $$\omega_X$$가 정확히 이러한 역할을 해 준다. 

Smooth projective morphism $$f \colon X \to Y$$는 임의의 점 $$y \in Y$$에 대해 섬유 $$f^{-1}(y)$$가 smooth projective variety가 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 이런 상황에서 섬유별 canonical sheaf를 일관되게 모은 것이며, 각 섬유 $$X_y$$에서 $$\omega_{X/Y}\vert_{X_y} \cong \omega_{X_y}$$가 성립한다.

Serre duality에서 $$H^n(X, \omega_X) \cong \mathbb{K}$$였던 사실은 relative situation에서 다음과 같이 일반화된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Smooth projective morphism $$f \colon X \to Y$$에서 $$n = \dim X - \dim Y$$라 하자. 그럼

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

이며, $$i \neq n$$에 대해서는 $$R^i f_\ast \omega_{X/Y} = 0$$이다.

</div>



## Grothendieck Duality

Serre duality는 variety $$X$$를 하나의 점 $$\operatorname{Spec}(\mathbb{K})$$로 보내는 상사상에 대한 특수한 경우이다. Grothendieck는 이를 임의의 proper morphism으로 일반화하였다. Proper morphism $$f \colon X \to Y$$는 위상수학적으로 compact map의 대수기하학적 대응물로, 임의의 base change에 대해 닫힌 사상이 되는 사상이다.

Serre duality에서 canonical bundle $$\omega_X$$가 핵심적인 역할을 하였듯이, relative 상황에서는 relative dualizing sheaf $$\omega_{X/Y}$$가 그 역할을 담당한다. 이는 섬유 $$f^{-1}(y)$$ 각각에서 canonical sheaf를 일관되게 모아둔 것이며, Serre duality에서 $$\omega_X$$가 하던 역할을 상대적인 상황으로 옮긴 것이다. 구체적으로 $$\omega_{X/Y}$$는 derived pullback $$f^!$$에 의해 $$\omega_{X/Y} = f^! \mathcal{O}_Y$$로 정의된다. 여기서 $$f^!$$는 $$R f_\ast$$의 right adjoint로 ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)), derived category에서만 자연스럽게 정의된다.

### Derived functor 개념

Grothendieck duality를 기술하려면 derived category 위에서 정의되는 여러 functor가 필요하다. ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)) 여기서는 각 functor가 왜 필요한지, 그리고 구성적으로 어떻게 정의되는지를 설명한다.

**$$\mathcal{H}om$$**. 이것은 module category의 $$\operatorname{Hom}$$과 다른 개념이다. $$\mathcal{H}om(\mathcal{F}, \mathcal{G})$$는 각 열린집합 $$U$$마다 $$\operatorname{Hom}_{\mathcal{O}_X(U)}(\mathcal{F}(U), \mathcal{G}(U))$$를 취한 뒤, 이 presheaf를 sheafify하여 얻은 sheaf이다. 즉 open set마다 독립적으로 Hom을 계산하고 이를 sheaf로 모은 것이다.

**$$\mathbf{R}\mathcal{H}om$$** ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10)). $$\mathcal{H}om$$은 covariant 인수에서 left exact, contravariant 인수에서도 left exact하지만 right exact가 아니므로, 이 functor를 그대로 사용하면 정보가 손실된다. 예를 들어 short exact sequence $$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$에 대해 $$\mathcal{H}om(-, \mathcal{G})$$를 적용하면 오른쪽에서 exactness가 깨진다. 따라서 두 인수 모두에서 derived functor가 필요하다. 구체적으로, contravariant 인수에 injective resolution을 취해 $$\mathcal{F} \to \mathcal{I}^\bullet$$로 치환한 뒤, covariant 인수에도 injective resolution을 취해 $$\mathcal{G} \to \mathcal{J}^\bullet$$로 치환하고 $$\mathcal{H}om(\mathcal{I}^\bullet, \mathcal{J}^\bullet)$$을 적용한다. 이 complex의 cohomology가 $$\operatorname{Ext}^i(\mathcal{F}, \mathcal{G})$$를 준다.

**$$R f_\ast$$** ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)). Pushforward $$f_\ast$$는 left exact functor이다: $$0 \to f_\ast \mathcal{F}' \to f_\ast \mathcal{F} \to f_\ast \mathcal{F}''$$는 exact하지만 오른쪽에서는 $$f_\ast \mathcal{F}''$$로의 surjectivity가 보장되지 않는다. 따라서 right derived functor $$R f_\ast$$가 필요하다. Sheaf $$\mathcal{F}$$에 injective resolution $$\mathcal{F} \to \mathcal{I}^\bullet$$을 취한 뒤 $$f_\ast \mathcal{I}^\bullet$$을 적용한다. 이 complex의 cohomology가 higher direct image $$R^i f_\ast$$를 준다.

**$$L f^\ast$$** ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 8](/ko/math/homological_algebra/derived_categories#def8)). Pullback $$f^\ast$$는 right exact functor이다. 이는 $$f^\ast$$가 $$f^{-1}(-) \otimes_{f^{-1}\mathcal{O}_Y} \mathcal{O}_X$$와 같은 tensor product의 형태이기 때문이다: tensor product는 항상 right exact하지만 left exact가 아니다. 따라서 left derived functor $$L f^\ast$$가 필요하며, flat resolution로 치환한 뒤 pullback을 적용한다.

**$$f^!$$** ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13)). 이 functor는 $$R f_\ast$$의 right adjoint로 derived category에서만 자연스럽게 정의된다. Sheaf category $$\operatorname{Coh}(X)$$의 수준에서는 $$f^!$$에 올바른 의미를 부여할 수 없다: $$R f_\ast$$가 complex 수준의 functor이므로, 그 adjoint 역시 complex 수준에서 존재해야 한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Grothendieck Duality)**</ins> Smooth projective variety 사이의 proper morphism $$f \colon X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해, derived category에서 다음 isomorphism이 성립한다:

$$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

여기서 $$R f_\ast$$는 derived pushforward ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 6](/ko/math/homological_algebra/derived_categories#def6)), $$\mathbf{R}\mathcal{H}om$$은 derived Hom ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10)), 그리고 $$f^!$$는 $$R f_\ast$$의 right adjoint ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13))이다. $$\mathcal{G}$$는 $$Y$$ 위의 coherent sheaf의 bounded below complex ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 4](/ko/math/homological_algebra/derived_categories#def4))이다. 특히 $$f$$가 smooth morphism of relative dimension $$n$$이면 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$이고, 여기서 $$\omega_{X/Y}$$는 relative canonical sheaf이다.

</div>

이 정리의 의미를 직관적으로 이해해보자. $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G})$$는 $$\mathcal{F}$$와 $$f^! \mathcal{G}$$ 사이의 '모든 가능한 Hom'을 모은 complex이며, $$R f_\ast$$를 적용하면 이를 $$Y$$ 위로 pushforward한다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$는 pushforward된 $$\mathcal{F}$$와 $$\mathcal{G}$$ 사이의 '모든 가능한 Hom'이다. 즉, 'pushforward 후 Hom'과 'Hom 후 pushforward'가 같다는 뜻이다. 본 글에서는 정리의 형태만 소개하며, 증명과 상세한 논의는 추후 별도의 글에서 다룬다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$Y = \operatorname{Spec}(\mathbb{K})$$이고 $$X$$가 $$n$$차원 smooth projective variety인 경우를 생각하자. 구조 사상 $$f \colon X \to \operatorname{Spec}(\mathbb{K})$$에 대해 $$R f_\ast \mathcal{F}$$의 cohomology는 단순히 cohomology group $$H^i(X, \mathcal{F})$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{O}_Y)$$의 cohomology는 dual vector space $$H^i(X, \mathcal{F})^\ast$$이다. 또한 $$f$$는 smooth of relative dimension $$n$$이므로 $$f^! \mathcal{O}_Y \cong \omega_X[n]$$이다. 따라서 [명제 5](#prop5)에서 $$\mathcal{G} = \mathcal{O}_Y$$, $$\mathcal{F}$$를 locally free sheaf로 취하면 cohomology 수준에서 $$H^i(X, \omega_X \otimes \mathcal{E}^\vee) \cong H^{n-i}(X, \mathcal{E})^\ast$$을 얻으며, 이는 정확히 Serre duality이다. 즉 Serre duality는 Grothendieck duality의 특수한 경우이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.

---

[^1]: 가령 $$\x\y=0$$은 CM이 아니지만, $$\y^2-\x^3=0$$은 CM이다. 