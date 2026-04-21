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
last_modified_at: 2026-04-21
weight: 15
published: false
---

기하적으로 좋은 경우 dimension $$k$$의 cohomology와 codimension $$k$$ cohomology 사이에는 자연스러운 쌍대성이 존재한다. 이를 증명하기 위해 우리는 perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

을 사용했으며, 이를 통해 [\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정리 11](/ko/math/algebraic_topology/Poincare_duality#thm11)와 같은 결과를 얻었다. 더 구체적으로, 이 pairing은 cap product와 fundamental class $$[M] \in H_n(M;R)$$를 통해 구성되므로 위상수학에서 duality의 원천은 orientation class $$[M]$$이라 할 수 있다. 

이번 글에서 우리는 대수기하학 버전의 duality인 Serre duality를 살펴본다. 

## 사영공간에서의 Serre Duality

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

어쨌든, cup product pairing에 의하여 우리는 임의의 locally free sheaf $$\mathcal{E}$$와 $$\omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee$$의 cocycle에 대하여 다음의 biliinear map

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

을 얻은 후, isomorphism $$\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$$과 위에서의 trace map을 활용하여 bilinear form

$$H^k{\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}$$

를 얻는다. 우리는 이를 $$\mathcal{O}(d)$$의 경우에 

여기서 $$U_{i_0,\ldots,i_{i+j}} = U_{i_0} \cap \cdots \cap U_{i_{i+j}}$$이다. Cocycle $$\alpha \in Z^i(\mathcal{U}, \mathcal{F})$$, $$\beta \in Z^j(\mathcal{U}, \mathcal{G})$$에 대해 $$\alpha \smile \beta$$는 $$C^{i+j}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$의 cocycle이 되며, coboundary에 대해 well-defined이므로 cohomology class $$\smile \colon \check{H}^i(\mathcal{U}, \mathcal{F}) \times \check{H}^j(\mathcal{U}, \mathcal{G}) \to \check{H}^{i+j}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$를 유도한다. $$\mathcal{U}$$가 $$\mathbb{P}^n$$에서 임의의 quasi-coherent sheaf에 대해 acyclic cover이므로, 이 Čech cohomology는 sheaf cohomology와 일치한다. 이 구성은 [\[대수적 위상수학\] §합곱, ⁋정의 1](/ko/math/algebraic_topology/cup_products#def1)에서 정의한 singular cohomology의 cup product와 정확히 같은 패턴을 따르며, [\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정의 14](/ko/math/algebraic_topology/Poincare_duality#def14)의 twisted coefficient cohomology와의 관계를 통해 sheaf cohomology로 자연스럽게 확장된다. Locally free sheaf $$\mathcal{E}$$와 $$\omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee$$의 Čech cocycle을 이용하여 $$\alpha \smile \beta \in H^n(\mathbb{P}^n, \mathcal{E} \otimes (\omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee))$$를 구성한 뒤, evaluation map $$\mathcal{E} \otimes \mathcal{E}^\vee \to \mathcal{O}_{\mathbb{P}^n}$$을 tensor하여 $$H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n})$$의 원소를 얻고 trace map으로 $$\mathbb{K}$$의 원소를 얻는다. 이 전체 과정이 쌍선형 형식

$$H^i(\mathbb{P}^n, \mathcal{E}) \times H^{n-i}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \to \mathbb{K};\quad (\alpha, \beta) \mapsto \operatorname{Tr}(\alpha \smile \beta)$$

을 구성한다. 이 pairing의 nondegeneracy를 $$\mathcal{E} = \mathcal{O}(d)$$인 경우에 엄밀하게 확인하자. $$\omega_{\mathbb{P}^n} \cong \mathcal{O}(-n-1)$$이므로 $$\omega_{\mathbb{P}^n} \otimes \mathcal{O}(d)^\vee \cong \mathcal{O}(-d-n-1)$$이고, pairing은 구체적으로

$$H^i(\mathbb{P}^n, \mathcal{O}(d)) \times H^{n-i}(\mathbb{P}^n, \mathcal{O}(-d-n-1)) \to \mathbb{K}$$

이 된다. $$\mathcal{E} = \mathcal{O}(d)$$인 경우에 대해 이 pairing의 nondegeneracy를 Čech cocycle 수준에서 직접 확인하자.

$$i = 0, d \geq 0$$인 경우를 생각하자. $$H^0(\mathbb{P}^n, \mathcal{O}(d))$$의 basis는 차수 $$d$$의 monomial $$\{x_0^{a_0} \cdots x_n^{a_n} \mid a_i \geq 0,\; a_0 + \cdots + a_n = d\}$$이며, $$H^n(\mathbb{P}^n, \mathcal{O}(-d-n-1))$$의 basis는 $$\{x_0^{-1-a_0'} \cdots x_n^{-1-a_n'} \mid a_i' \geq 0,\; a_0' + \cdots + a_n' = d\}$$이다. 여기서 각 지수가 $$-1$$ 이하임이 Čech cocycle 조건에 의해 보장된다. Basis 원소 $$\alpha = x_0^{a_0} \cdots x_n^{a_n}$$와 $$\beta = x_0^{-1-a_0'} \cdots x_n^{-1-a_n'}$$에 대해 cup product $$\alpha \smile \beta$$는 Čech cocycle $$x_0^{a_0-a_0'-1} \cdots x_n^{a_n-a_n'-1}$$이며, trace map은 이것의 계수를 취한다. 이 monomial의 차수는 $$(a_0 - a_0' - 1) + \cdots + (a_n - a_n' - 1) = d - d - (n+1) = -n-1$$이며, 모든 지수가 $$-1$$일 때—즉 $$a_i = a_i'$$일 때만—$$\operatorname{Tr}(\alpha \smile \beta) \neq 0$$이다. 이는 dual basis 조건이며, 따라서 pairing matrix가 항등행렬이 되어 nondegenerate이다. $$i = n, d \leq -n-1$$인 경우도 동일하게 확인된다. 그 외의 $$i$$에 대해서는 양변이 모두 0이므로 pairing이 자명하게 perfect이다.

일반적인 locally free sheaf $$\mathcal{E}$$의 경우, $$\mathbb{P}^n$$ 위에서 Hilbert syzygy theorem에 의해 $$\mathcal{E}$$는 line bundle들의 direct sum으로 이루어진 유한 resolution을 갖는다. Cup product에 의한 pairing은 $$\mathcal{E}$$에 대해 functorial이므로, 이 resolution에 대해 유도된 long exact sequence와 함께 five lemma를 적용하면 line bundle case에서 증명한 nondegeneracy로부터 일반적인 case의 nondegeneracy가 따라나온다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\mathbb{P}^n$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 쌍선형 형식

$$H^i(\mathbb{P}^n, \mathcal{E}) \times H^{n-i}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \to \mathbb{K};\quad (\alpha, \beta) \mapsto \operatorname{Tr}(\alpha \smile \beta)$$

은 perfect pairing이다.

</div>

### Serre duality isomorphism

Perfect pairing이 성립하면 각 $$H^i(\mathbb{P}^n, \mathcal{E})$$는 그 dual space와 자연스럽게 동형이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Projective space에서의 Serre Duality)**</ins> $$\mathbb{P}^n$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(\mathbb{P}^n, \mathcal{E}) \cong H^{n-i}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee)^\ast$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)의 perfect pairing에 의해 linear map $$H^i(\mathbb{P}^n, \mathcal{E}) \to H^{n-i}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee)^\ast$$가 $$\alpha \mapsto (\beta \mapsto \operatorname{Tr}(\alpha \smile \beta))$$로 정의된다. Perfect pairing의 nondegeneracy에 의해 이 사상은 injective이며, [명제 2](#prop2)에서 Čech cocycle 수준으로 확인한 explicit nondegeneracy에 의해 surjective이다. 유한차원 vector space 사이의 injective이면서 surjective인 선형사상은 isomorphism이다.

</details>

이로써 $$\mathbb{P}^n$$ 위에서 Serre duality가 성립함을 엄밀하게 증명하였다. 이 결과는 단순히 차원만 맞는 것이 아니라, trace map과 cup product라는 구체적인 구성을 통해 perfect pairing이 성립한다는 강한 결과이다.

## 일반적인 Smooth Projective Variety에서의 Serre Duality

$$\mathbb{P}^n$$에서 확립된 Serre duality는 임의의 smooth projective variety로 자연스럽게 일반화된다. 이 일반화의 핵심은 임의의 smooth projective variety가 finite morphism을 통해 $$\mathbb{P}^n$$과 연결된다는 사실에 기반한다.

### Canonical sheaf와 top cohomology

$$n$$차원 smooth projective variety $$X$$에 대해 [§표준선다발, ⁋정의 5](/ko/math/algebraic_geometry/canonical_bundle#def5)에서 canonical sheaf $$\omega_X = \bigwedge^{\!n} \Omega_X^1$$를 정의하였고, [§표준선다발, ⁋정의 6](/ko/math/algebraic_geometry/canonical_bundle#def6)에서 canonical divisor $$K_X$$를 $$\omega_X \cong \mathcal{O}_X(K_X)$$를 만족하는 divisor class로 정의하였다. Smooth variety에서 $$\omega_X$$는 국소적으로 자명한 line bundle이므로 $$\omega_X$$와 $$\mathcal{O}_X(K_X)$$는 동일한 line bundle을 기술한다. 즉 $$\omega_X \cong \mathcal{O}_X(K_X)$$이며, 이 동형 아래에서 $$\omega_X$$의 section은 canonical divisor $$K_X$$에 대응하는 rational differential form으로 해석된다.

일반적인 $$X$$에서 $$H^n(X, \omega_X)$$가 1차원임을 보이기 위해 Noether 정리에 의해 존재하는 finite surjective morphism $$f \colon X \to \mathbb{P}^n$$을 사용한다. $$f$$가 degree $$d$$의 finite surjective morphism일 때 $$f_\ast \omega_X$$는 $$\omega_{\mathbb{P}^n}$$과 관련된 sheaf이며, projection formula와 [명제 1](#prop1)의 $$\mathbb{P}^n$$에서의 계산으로부터 $$H^n(X, \omega_X) \neq 0$$이고 실제로 그 차원은 정확히 $$1$$이다. 복소기하학에서 이 사실은 $$\omega_X$$의 section들이 volume form이고, compact manifold 위에서의 적분 $$\int_X \eta \neq 0$$이 존재한다는 사실과 일치한다.

Trace map $$\operatorname{Tr} \colon H^n(X, \omega_X) \xrightarrow{\sim} \mathbb{K}$$도 $$\mathbb{P}^n$$에서의 구성으로부터 얻어진다. Finite surjective morphism $$f \colon X \to \mathbb{P}^n$$에 대해 $$\mathbb{P}^n$$에서의 trace map과 functor $$f^!$$를 결합하여 $$X$$ 위의 trace map을 정의한다. 복소기하학에서 $$X$$가 compact complex manifold이면 trace map은 적분 $$\eta \mapsto \int_X \eta$$로 주어지며, 이는 Čech적 구성이 미분기하학적으로 자연스러운 적분 연산과 일치함을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$n$$차원 smooth projective variety $$X$$에 대해 $$\omega_X \cong \mathcal{O}_X(K_X)$$이고 $$H^n(X, \omega_X) \cong \mathbb{K}$$이다.

</div>

### Serre Duality 정리

이제 일반적인 smooth projective variety에 대한 Serre duality를 서술한다. $$\mathbb{P}^n$$에서와 동일한 구성 — trace map과 cup product를 통한 쌍선형 형식 — 이 일반 variety에서도 perfect pairing을 이룬다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Serre Duality)**</ins> Field $$\mathbb{K}$$ 위의 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 자연스러운 isomorphism이 존재한다:

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

여기서 $$\omega_X$$는 canonical bundle ([§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24))이고 $$\mathcal{E}^\vee = \mathcal{H}om(\mathcal{E}, \mathcal{O}_X)$$는 dual sheaf이다. 이 isomorphism은 trace map과 cup product를 사용하여 $$\alpha \mapsto (\beta \mapsto \operatorname{Tr}(\alpha \smile \beta))$$로 명시적으로 주어진다.

</div>

Locally free sheaf $$\mathcal{E}$$에 대해서는 $$\mathcal{H}om(\mathcal{E}, \omega_X) \cong \omega_X \otimes \mathcal{E}^\vee$$가 성립하므로 ([§선다발과 벡터다발, ⁋명제 7](/ko/math/algebraic_geometry/line_bundles#prop7)), 명제의 우변을 $$H^{n-i}(X, \mathcal{H}om(\mathcal{E}, \omega_X))^\ast$$와 같이 쓸 수도 있다. 일반적인 coherent sheaf $$\mathcal{F}$$에 대해서는 $$\omega_X \otimes \mathcal{F}^\vee$$ 대신 Ext group $$\operatorname{Ext}^i(\mathcal{F}, \omega_X)$$를 사용하여 $$\operatorname{Ext}^{n-i}(\mathcal{F}, \omega_X) \cong H^i(X, \mathcal{F})^\ast$$의 형태로 동일한 duality가 성립하지만, 본 글에서는 locally free sheaf에 대한 버전을 다룬다. 또한 Hartshorne의 고전적 증명에서는 $$\mathbb{K}$$가 algebraically closed field라고 가정하지만, Grothendieck duality를 사용하면 임의의 field에 대해 동일한 결과가 성립한다.

Serre duality의 증명은 $$\mathbb{P}^n$$에서의 결과를 바탕으로 finite morphism을 통해 일반적인 variety로 확장하는 방법과, derived category에서 $$\omega_X = f^! \mathcal{O}_{\operatorname{Spec}(\mathbb{K})}$$로 정의한 뒤 derived adjunction으로 duality를 얻는 방법이 있다. 두 방법 모두 본질적으로 동일한 핵심 사실에 기반한다. 즉, trace map과 cup product가 완벽한 쌍대성을 이룬다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 특히 $$\mathcal{E} = \mathcal{O}_X$$에 대해:

$$H^i(X, \mathcal{O}_X) \cong H^{n-i}(X, \omega_X)^\ast$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathcal{O}_X^\vee = \mathcal{H}om(\mathcal{O}_X, \mathcal{O}_X) \cong \mathcal{O}_X$$이므로, [명제 5](#prop5)에서 $$\mathcal{E} = \mathcal{O}_X$$를 대입하면 $$\omega_X \otimes \mathcal{O}_X^\vee \cong \omega_X$$를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Curve)**</ins> Genus $$g$$인 smooth curve $$C$$를 생각하자. 여기서 genus는 $$g = \dim H^1(C, \mathcal{O}_C)$$로 정의된다. $$C$$는 $$1$$차원이므로 [명제 6](#prop6)에서 $$n = 1$$을 대입하면 다음을 얻는다.

$$H^0(C, \mathcal{O}_C) \cong H^1(C, \omega_C)^\ast$$이고 $$H^1(C, \mathcal{O}_C) \cong H^0(C, \omega_C)^\ast$$이다.

첫 번째 동형에서 $$\dim H^0(C, \mathcal{O}_C) = 1$$이므로 $$\dim H^1(C, \omega_C) = 1$$이고, 두 번째 동형에서 $$\dim H^0(C, \omega_C) = \dim H^1(C, \mathcal{O}_C)^\ast = g$$이다. 즉 canonical bundle $$\omega_C$$의 global section의 차원이 정확히 genus $$g$$와 같다. 이는 Riemann-Roch theorem의 기초가 되는 관측이다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$\mathbb{P}^1$$에서 $$\omega_{\mathbb{P}^1} \cong \mathcal{O}(-2)$$이므로 [명제 5](#prop5)에 의해 $$H^0(\mathbb{P}^1, \mathcal{O}(d)) \cong H^1(\mathbb{P}^1, \mathcal{O}(-d-2))^\ast$$이다. $$d = 0$$이면 $$H^0(\mathcal{O}) = \mathbb{K}$$이고 $$H^1(\mathcal{O}(-2)) = \mathbb{K}$$이며, $$d = 1$$이면 $$H^0(\mathcal{O}(1)) = \mathbb{K}^2$$이고 $$H^1(\mathcal{O}(-3)) = \mathbb{K}^2$$이다. 양쪽의 차원이 일치함을 확인할 수 있다.

</div>

## 응용: Euler Characteristic

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Serre duality에 의해 $$n$$차원 smooth projective variety $$X$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 다음이 성립한다.

$$\rchi(\mathcal{E}) = (-1)^n \rchi(\omega_X \otimes \mathcal{E}^\vee)$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euler characteristic의 정의와 [명제 5](#prop5)에 의해

$$\rchi(\mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^i(X, \mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)$$

이다. 여기서 치환 $$j = n - i$$를 적용하면

$$\sum_{i=0}^{n} (-1)^i \dim H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee) = \sum_{j=0}^{n} (-1)^{n-j} \dim H^j(X, \omega_X \otimes \mathcal{E}^\vee) = (-1)^n \rchi(\omega_X \otimes \mathcal{E}^\vee)$$

을 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (Curve)**</ins> Curve $$C$$와 line bundle $$\mathcal{L}$$에 대해, [명제 9](#prop9)에서 $$n = 1$$을 대입하면

$$\rchi(\mathcal{L}) = -\rchi(\omega_C \otimes \mathcal{L}^\vee)$$

이다. 한편 Euler characteristic의 정의에 의해 $$\rchi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^1(C, \mathcal{L})$$이고, Serre duality에 의해 $$\dim H^1(C, \mathcal{L}) = \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$이므로

$$\rchi(\mathcal{L}) = \dim H^0(C, \mathcal{L}) - \dim H^0(C, \omega_C \otimes \mathcal{L}^\vee)$$

이다. 이 공식은 Riemann-Roch theorem의 출발점이 된다.

</div>

## Relative Duality

Smooth projective morphism $$f \colon X \to Y$$는 임의의 점 $$y \in Y$$에 대해 섬유 $$f^{-1}(y)$$가 smooth projective variety가 되는 사상이다. Relative dualizing sheaf $$\omega_{X/Y}$$는 이런 상황에서 섬유별 canonical sheaf를 일관되게 모은 것이며, 각 섬유 $$X_y$$에서 $$\omega_{X/Y}\vert_{X_y} \cong \omega_{X_y}$$가 성립한다.

Serre duality에서 $$H^n(X, \omega_X) \cong \mathbb{K}$$였던 사실은 relative situation에서 다음과 같이 일반화된다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Smooth projective morphism $$f \colon X \to Y$$에서 $$n = \dim X - \dim Y$$라 하자. 그럼

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

이며, $$i \neq n$$에 대해서는 $$R^i f_\ast \omega_{X/Y} = 0$$이다.

</div>

이 정리는 relative situation에서도 "top cohomology of canonical sheaf = 1"이라는 직관이 그대로 성립함을 보여준다. 실제로 [명제 12](#prop12)에서 $$\mathcal{F} = \mathcal{O}_X$$, $$\mathcal{G} = \mathcal{O}_Y$$를 대입하면 $$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{O}_X, \omega_{X/Y}[n]) \cong \omega_{X/Y}[n]$$이므로 좌변은 $$R f_\ast \omega_{X/Y}[n]$$이 된다. 이 complex의 $$0$$차 cohomology sheaf를 취하면 $$R^n f_\ast \omega_{X/Y}$$를 얻는다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$의 $$0$$차 cohomology는 $$\mathcal{H}om_{\mathcal{O}_Y}(f_\ast \mathcal{O}_X, \mathcal{O}_Y)$$이며, smooth projective morphism에서는 섬유가 geometrically integral이므로 $$f_\ast \mathcal{O}_X = \mathcal{O}_Y$$가 성립하여 이는 $$\mathcal{O}_Y$$가 되어 [명제 11](#prop11)의 첫 번째 주장을 얻는다. Relative duality의 증명과 응용에 대해서는 추후 별도의 글에서 다룬다.

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

<ins id="prop12">**명제 12 (Grothendieck Duality)**</ins> Smooth projective variety 사이의 proper morphism $$f \colon X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해, derived category에서 다음 isomorphism이 성립한다:

$$R f_\ast \mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong \mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

여기서 $$R f_\ast$$는 derived pushforward ([§유도카테고리, ⁋정의 6](/ko/math/homological_algebra/derived_categories#def6)), $$\mathbf{R}\mathcal{H}om$$은 derived Hom ([§유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10)), 그리고 $$f^!$$는 $$R f_\ast$$의 right adjoint ([§유도카테고리, ⁋명제 13](/ko/math/homological_algebra/derived_categories#prop13))이다. $$\mathcal{G}$$는 $$Y$$ 위의 coherent sheaf의 bounded below complex ([§유도카테고리, ⁋정의 4](/ko/math/homological_algebra/derived_categories#def4))이다. 특히 $$f$$가 smooth morphism of relative dimension $$n$$이면 $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$이고, 여기서 $$\omega_{X/Y}$$는 relative canonical sheaf이다.

</div>

이 정리의 의미를 직관적으로 이해해보자. $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G})$$는 $$\mathcal{F}$$와 $$f^! \mathcal{G}$$ 사이의 '모든 가능한 Hom'을 모은 complex이며, $$R f_\ast$$를 적용하면 이를 $$Y$$ 위로 pushforward한다. 우변 $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$는 pushforward된 $$\mathcal{F}$$와 $$\mathcal{G}$$ 사이의 '모든 가능한 Hom'이다. 즉, 'pushforward 후 Hom'과 'Hom 후 pushforward'가 같다는 뜻이다. 본 글에서는 정리의 형태만 소개하며, 증명과 상세한 논의는 추후 별도의 글에서 다룬다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $$Y = \operatorname{Spec}(\mathbb{K})$$이고 $$X$$가 $$n$$차원 smooth projective variety인 경우를 생각하자. 구조 사상 $$f \colon X \to \operatorname{Spec}(\mathbb{K})$$에 대해 $$R f_\ast \mathcal{F}$$의 cohomology는 단순히 cohomology group $$H^i(X, \mathcal{F})$$이고, $$\mathbf{R}\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{O}_Y)$$의 cohomology는 dual vector space $$H^i(X, \mathcal{F})^\ast$$이다. 또한 $$f$$는 smooth of relative dimension $$n$$이므로 $$f^! \mathcal{O}_Y \cong \omega_X[n]$$이다. 따라서 [명제 12](#prop12)에서 $$\mathcal{G} = \mathcal{O}_Y$$, $$\mathcal{F}$$를 locally free sheaf로 취하면 cohomology 수준에서 $$H^i(X, \omega_X \otimes \mathcal{E}^\vee) \cong H^{n-i}(X, \mathcal{E})^\ast$$을 얻으며, 이는 정확히 [명제 5](#prop5)의 Serre duality이다. 즉 Serre duality는 Grothendieck duality의 특수한 경우이다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.