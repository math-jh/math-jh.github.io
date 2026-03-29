---
title: "Canonical Bundle"
excerpt: "Canonical bundle and canonical divisor"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/canonical_bundle
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Canonical_Bundle.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-29
weight: 11

published: false
---

[§선형계](/ko/math/algebraic_geometry/linear_systems)에서 우리는 line bundle의 complete linear system이 정의하는 morphism을 통해 variety를 projective space에 embedded할 수 있음을 보았고, very ample line bundle이 이 embedding을 closed embedding으로 만드는 조건임을 확인하였다. 또한 ample line bundle이 projective variety의 분류와 embedding 문제에서 핵심적인 역할을 함을 논하였다. 이제 우리는 모든 smooth variety가 "자연스럽게" 갖는 line bundle인 *canonical bundle*을 정의하고, 그 성질들을 살펴본다.

Canonical bundle은 variety 위의 differential form들로 구성된 line bundle이다. 이는 Serre duality, Riemann-Roch theorem, adjunction formula 등 대수기하학의 가장 중요한 정리들에서 공통적으로 등장하며, variety의 기하학적 성질—곡률, 쌍대성, embedding 가능성 등—을 encoded하는 핵심적인 불변량이다. 또한, canonical bundle의 ampleness 여부에 따라 variety를 크게 세 부류로 나누는 birational geometry의 분류 체계에서도 중심적인 역할을 한다.

## Cotangent Sheaf

Canonical bundle을 정의하기 위해서는 먼저 variety 위의 cotangent sheaf를 도입해야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth variety $$X$$의 *cotangent sheaf* $$\Omega_X^1$$는 각 점 $$p \in X$$에서 Zariski cotangent space $$T_p^\ast X = \mathfrak{m}_p/\mathfrak{m}_p^2$$를 fiber로 갖는 sheaf이다. 여기서 $$\mathfrak{m}_p$$는 $$p$$에서의 maximal ideal이다.

</div>

이 정의가 local construction으로부터 sheaf를 얻는 올바른 방법인 것을 확인하자.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Affine variety $$X = \operatorname{Spec} A$$에서 $$\Omega_X^1$$는 Kähler differentials $$\Omega_{A/\mathbb{K}}^1$$ ([\[가환대수학\] §Differentials, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3))의 associated sheaf이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Kähler differentials $$\Omega_{A/\mathbb{K}}^1$$는 $$A$$-module로, 각 점 $$p \in X$$에서의 stalk은 $$(\Omega_{A/\mathbb{K}}^1)_p = \Omega_{A/\mathbb{K}}^1 \otimes_A \mathcal{O}_{X,p}$$이다. 이를 residue field $$\kappa(p) = \mathcal{O}_{X,p}/\mathfrak{m}_p$$로 tensor하면, Kähler differential의 기본 성질에 의해 $$(\Omega_{A/\mathbb{K}}^1)_p \otimes_{\mathcal{O}_{X,p}} \kappa(p) \cong \mathfrak{m}_p/\mathfrak{m}_p^2$$이 성립한다. 따라서 $$\Omega_X^1$$의 fiber가 cotangent space와 일치하므로, $$\Omega_X^1$$는 Kähler differentials의 sheafification으로 얻어짐을 알 수 있다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{A}^n$$의 cotangent sheaf는 $$\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$$이다. Coordinate ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$의 Kähler differentials은 free module $$\bigoplus_{i=1}^n \mathbb{K}[\x_1, \ldots, \x_n] \, d\x_i$$이므로, associated sheaf 역시 free sheaf of rank $$n$$이 된다.

</div>

$$X$$가 smooth variety of dimension $$n$$이면, 각 점 $$p \in X$$ 근방에서 $$\Omega_X^1$$은 locally free sheaf of rank $$n$$이다. 즉, cotangent sheaf는 vector bundle of rank $$n$$을 정의한다.

## Canonical Bundle의 정의

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Smooth variety $$X$$ of dimension $$n$$의 *canonical sheaf* (또는 *canonical bundle*) $$\omega_X$$는 cotangent sheaf의 top exterior power이다.

$$\omega_X = \bigwedge\nolimits^{\!n} \Omega_X^1$$

</div>

$$\Omega_X^1$$이 locally free of rank $$n$$이므로, 그 top exterior power는 locally free of rank $$1$$, 즉 invertible sheaf이다. 따라서 $$\omega_X$$는 ([§선다발과 벡터다발, ⁋정의 3](/ko/math/algebraic_geometry/line_bundles#def3))의 의미에서 line bundle이다.

Canonical bundle $$\omega_X$$의 global section $$s \in H^0(X, \omega_X)$$는 $$X$$ 위의 *regular $$n$$-form*이라 부른다. 국소적으로, $$X$$의 열린 부분집합 $$U$$ 위에서 $$\Omega_X^1$$은 $$\mathcal{O}_U^{\oplus n}$$과 동형인데, 각 $$n$$-form은 $$f \, d\x_1 \wedge \cdots \wedge d\x_n$$의 꼴로 표현되는 differential form이다. $$\mathbb{A}^n$$에서는 [예시 3](#ex3)에 의해 $$\omega_{\mathbb{A}^n} \cong \bigwedge^n \mathcal{O}_{\mathbb{A}^n}^{\oplus n} \cong \mathcal{O}_{\mathbb{A}^n}$$이며, $$d\x_1 \wedge \cdots \wedge d\x_n$$이 $$\omega_{\mathbb{A}^n}$$의 trivializing section이 된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Canonical bundle $$\omega_X$$에 대응하는 divisor class를 *canonical divisor*라 하고 $$K_X$$로 표기한다. 즉, $$\omega_X \cong \mathcal{O}_X(K_X)$$이다.

</div>

Canonical divisor는 linear equivalence class만이 잘 정의된다. 즉, $$K_X$$는 $$\operatorname{Cl}(X)$$의 원소이다. ([§인자, ⁋정의 6](/ko/math/algebraic_geometry/divisors#def6))

## 예시: $$\mathbb{P}^n$$의 Canonical Bundle

$$\mathbb{P}^n$$의 canonical bundle을 계산하기 위해, 우리는 *Euler exact sequence*를 사용한다. 이는 $$\mathbb{P}^n$$ 위의 cotangent sheaf를 더 단순한 sheaf들의 exact sequence 속에 위치시키는 강력한 도구이다.

$$\mathbb{P}^n$$을 자연스러운 projection $$\pi \colon \mathbb{A}^{n+1} \setminus \{0\} \to \mathbb{P}^n$$의 quotient로 생각하자. 점 $$p = [x_0 : \cdots : x_n] \in \mathbb{P}^n$$에 대해, $$\pi^{-1}(p)$$는 $$\mathbb{A}^{n+1}$$에서의 line $$L_p$$이며, $$T_p \mathbb{P}^n$$는 $$T_{\tilde{p}} \mathbb{A}^{n+1} / T_{\tilde{p}} L_p$$와 동형인데, 이로부터 cotangent space $$T_p^* \mathbb{P}^n$$는 $$T_{\tilde{p}}^* L_p$$의 orthogonal complement로 이해할 수 있다. 이 관계를 sheaf 수준에서 정리하면 다음 exact sequence를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> (Euler Exact Sequence) $$\mathbb{P}^n$$ 위에서 다음 exact sequence가 성립한다.

$$0 \to \Omega_{\mathbb{P}^n}^1 \to \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n} \to 0$$

</div>

이 exact sequence에서 두 번째 화살표는 각 $$i$$에 대해 $$d\x_i \mapsto \x_i$$로 주어지며, 세 번째 화살표는 $$(s_0, \ldots, s_n) \mapsto \sum_{i=0}^n \x_i s_i$$로 주어진다.

<details class="proof" markdown="1">
<summary>증명 (Exactness)</summary>

$$\mathbb{P}^n = (\mathbb{A}^{n+1} \setminus \{0\})/\mathbb{G}_m$$라는 quotient 구조를 활용한다. $$\mathbb{A}^{n+1} \setminus \{0\}$$ 위에서 coordinate function $$\x_0, \ldots, \x_n$$과 1-form $$d\x_0, \ldots, d\x_n$$을 갖는다. $$\mathbb{G}_m$$은 $$\lambda \cdot (\x_0, \ldots, \x_n) = (\lambda \x_0, \ldots, \lambda \x_n)$$로 작용하며, $$\mathbb{G}_m$$-invariant differential form들은 $$\mathbb{P}^n$$ 위의 differential form으로 내려온다.

**두 번째 화살표의 injectivity:** $$\Omega_{\mathbb{P}^n}^1$$은 locally free sheaf이므로, sheaf homomorphism이 stalk에서 injective이면 injective이다. 임의의 점 근방에서 $$d\x_i$$들은 $$\Omega_{\mathbb{A}^{n+1}}^1$$의 basis를 이루며, 이들 사이의 trivial relation만이 영벡터이다.

**세 번째 화살표의 surjectivity:** 임의의 점 $$p = [\x_0 : \cdots : \x_n]$$에서 적어도 하나의 $$\x_j(p) \neq 0$$이다. 열린 집합 $$U_j = \{\x_j \neq 0\}$$ 위에서 $$s_i = f \cdot (\x_i / \x_j)$$로 놓으면, 각 $$s_i$$는 $$\x_j$$로 나누어지므로 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 section이고, $$\sum_i \x_i s_i = f \sum_i \x_i^2 / \x_j = f \sum_i (\x_i/\x_j)^2$$가 된다. 더 간단히, $$s_i = 0$$ ($$i \neq j$$), $$s_j = f / \x_j$$로 놓으면 $$\sum_i \x_i s_i = f$$가 된다. $$f/\x_j \in \mathcal{O}_{\mathbb{P}^n}(-1)(U_j)$$이므로 임의의 $$f$$가 image에 들어간다.

**Ker(세 번째 화살표) $$\subset$$ Im(두 번째 화살표):** $$(s_0, \ldots, s_n)$$이 $$\sum_{i=0}^n \x_i s_i = 0$$을 만족한다고 하자. $$\omega = \sum_i s_i \, d\x_i$$를 $$\mathbb{A}^{n+1} \setminus \{0\}$$ 위의 1-form이라 하자. 각 $$s_i$$는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$의 section이므로 $$\mathbb{A}^{n+1} \setminus \{0\}$$ 위에서 $$\sum_i \x_i s_i$$로 나누어지는 regular function이라 생각할 수 있다. $$\omega$$가 $$\mathbb{G}_m$$-invariant인지 확인하자. $$\lambda \in \mathbb{G}_m$$이 $$\x_i \mapsto \lambda \x_i$$로 작용할 때, $$s_i \mapsto \lambda s_i$$ (degree $$-1$$), $$d\x_i \mapsto \lambda \, d\x_i$$이므로 $$\omega \mapsto \lambda^2 \omega$$이다. 반면, $$i_E \omega = \sum_i s_i \x_i = 0$$ (여기서 $$E = \sum_i \x_i \partial/\partial \x_i$$는 Euler vector field)이므로, Cartan 공식과 $$\mathcal{L}_E = d \circ i_E + i_E \circ d = 0$$ (homogeneous function에 대한 Euler의 정리)로부터 $$\omega$$가 $$\mathbb{G}_m$$-invariant임을 안다. 따라서 $$\omega$$는 $$\mathbb{P}^n$$ 위의 1-form, 즉 $$\Omega_{\mathbb{P}^n}^1$$의 section으로 내려오며, 이것이 $$\omega$$의 image에 $$(s_0, \ldots, s_n)$$을 갖음을 보여준다.

</details>

이제 determinant를 취하여 $$\mathbb{P}^n$$의 canonical bundle을 계산할 수 있다. Exact sequence에서 top exterior power를 취하면 다음 동형을 얻는다.

$$\det(\Omega_{\mathbb{P}^n}^1) \otimes \det(\mathcal{O}_{\mathbb{P}^n}) \cong \det(\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)})$$

$$\det(\mathcal{O}_{\mathbb{P}^n}) \cong \mathcal{O}_{\mathbb{P}^n}$$이고 $$\det(\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) \cong \mathcal{O}_{\mathbb{P}^n}(-1)^{\otimes(n+1)} \cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$이므로,

$$\omega_{\mathbb{P}^n} = \det(\Omega_{\mathbb{P}^n}^1) \cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$

를 얻는다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> $$\mathbb{P}^n$$의 canonical bundle은 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$이며, canonical divisor는 $$K_{\mathbb{P}^n} = -(n+1)H$$이다. 여기서 $$H$$는 hyperplane divisor이다. 특히 $$\omega_{\mathbb{P}^n}$$은 $$H^0(\mathbb{P}^n, \omega_{\mathbb{P}^n}) = 0$$이므로, $$\mathbb{P}^n$$ 위에는 nontrivial한 regular $$n$$-form이 존재하지 않는다.

이를 transition function 관점에서도 확인할 수 있다. $$\mathbb{P}^n$$의 standard open cover $$U_i = \{\x_i \neq 0\}$$ 위에서 affine coordinate을 $$y_j^{(i)} = \x_j / \x_i$$ ($$j \neq i$$)로 놓으면, $$U_i$$ 위의 $$n$$-form $$d y_1^{(i)} \wedge \cdots \wedge \widehat{d y_i^{(i)}} \wedge \cdots \wedge d y_n^{(i)}$$ (즉, $$j \neq i$$인 모든 $$j$$에 대한 $$d y_j^{(i)}$$의 wedge)을 생각할 수 있다. $$U_i \cap U_j$$ 위에서 $$y_k^{(j)} = \x_k / \x_j = (\x_k / \x_i) / (\x_j / \x_i) = y_k^{(i)} / y_j^{(i)}$$이므로, $$k \neq i, j$$에 대해 $$d y_k^{(j)} = d(y_k^{(i)} / y_j^{(i)}) = (y_j^{(i)} \, d y_k^{(i)} - y_k^{(i)} \, d y_j^{(i)}) / (y_j^{(i)})^2$$이다. 따라서 $$U_j$$ 위의 $$n$$-form은 $$U_i \cap U_j$$에서

$$\bigwedge_{k \neq j} d y_k^{(j)} = (y_j^{(i)})^{-(n+1)} \cdot \bigwedge_{k \neq i} d y_k^{(i)}$$

로 변환된다. 여기서 $$(y_j^{(i)})^{-(n+1)} = (\x_j / \x_i)^{-(n+1)}$$이므로, transition function이 $$g_{ij} = (\x_i / \x_j)^{-(n+1)}$$임을 확인할 수 있다. 이는 $$\mathcal{O}_{\mathbb{P}^n}(-n-1)$$의 transition function과 일치한다.

</div>

$$\mathbb{A}^n$$에서는 $$\omega_{\mathbb{A}^n} \cong \mathcal{O}_{\mathbb{A}^n}$$이 trivial이었지만, projective space에서는 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$이 nontrivial하다. 이는 projective space가 "at infinity에서 닫혀 있기 때문에" 발생하는 위상적 현상이라 생각할 수 있다.

## Smooth Curve의 Canonical Bundle

Smooth projective curve $$C$$의 경우, canonical bundle은 특히 구체적이고 풍부한 이론을 제공한다. 이 섹션에서는 $$C$$의 canonical bundle $$\omega_C = \Omega_C^1$$의 여러 가지 성질을 다룬다.

### 기본 성질

$$\omega_C$$의 global section $$s \in H^0(C, \omega_C)$$는 $$C$$ 위의 *regular 1-form*이다. $$C$$의 genus를 $$g$$라 할 때, Riemann-Roch theorem에 의해 $$h^0(C, \omega_C) = g$$이므로, regular 1-form의 공간은 $$g$$차원이다.

Canonical divisor $$K_C$$의 degree를 알아보자. [예시 7](#ex7)에서 $$\omega_{\mathbb{P}^n} \cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$임을 보았고, 뒤에서 증명할 adjunction formula ([명제 9](#prop9))에 의해 $$\mathbb{P}^2$$ 안의 smooth plane curve $$C$$ of degree $$d$$에 대해 $$\omega_C \cong \mathcal{O}_C(d-3)$$이 된다. 따라서 $$\deg K_C = d(d-3)$$이고, plane curve의 genus가 $$g = (d-1)(d-2)/2$$이므로 $$\deg K_C = 2g - 2$$를 얻는다. 이 결과는 임의의 smooth projective curve에 대해 성립한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Smooth projective curve $$C$$의 genus가 $$g$$이면 $$\deg K_C = 2g - 2$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann-Roch theorem에 의해, 임의의 divisor $$D$$에 대해 $$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$가 성립한다. $$D = 0$$을 대입하면 $$\ell(0) - \ell(K_C) = 1 - g$$이고, $$\ell(0) = 1$$, $$\ell(K_C) = h^0(C, \omega_C) = g$$이므로 자동으로 성립한다. $$D = K_C$$를 대입하면 $$\ell(K_C) - \ell(0) = \deg K_C + 1 - g$$, 즉 $$g - 1 = \deg K_C + 1 - g$$로부터 $$\deg K_C = 2g - 2$$를 얻는다.

</details>

### Genus에 따른 분류

Canonical divisor의 degree는 curve의 genus에 따라 본질적으로 다른 거동을 보인다. $$g = 0$$, 즉 $$C \cong \mathbb{P}^1$$의 경우, $$\deg K_C = -2 < 0$$이므로 $$K_C$$는 ample이 아니다. 사실 $$K_{\mathbb{P}^1} = -2P$$이므로 $$K_C$$는 negative degree를 갖는다. $$g = 1$$, 즉 elliptic curve의 경우, $$\deg K_C = 0$$이며 실제로 $$K_C \sim 0$$이므로 $$\omega_C \cong \mathcal{O}_C$$가 trivial하다. 따라서 $$K_C$$ 역시 ample이 아니다. $$g \ge 2$$의 경우, $$\deg K_C = 2g - 2 > 0$$이다. Curve에서 $$\deg \mathcal{L} > 0$$인 line bundle $$\mathcal{L}$$은 항상 ample이다. Riemann-Roch theorem에 의해 $$\dim H^0(C, \mathcal{L}^{\otimes m}) = m \cdot \deg \mathcal{L} - g + 1$$ ($$m$$가 충분히 클 때)이며, 이는 충분히 큰 $$m$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample section들을 충분히 많이 가짐을 의미하므로 ([§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10)), $$K_C$$는 ample이다.

### Hyperelliptic Curve에서의 Canonical Bundle

Genus $$g \ge 2$$인 hyperelliptic curve는 $$\mathbb{P}^1$$에 대한 degree 2 covering으로 정의된다. 구체적으로, $$C$$는 $$y^2 = f(\x)$$ ($$f$$는 서로 다른 근을 갖는 degree $$2g + 1$$ 또는 $$2g + 2$$ 다항식)에 의해 주어진 affine curve의 smooth completion이다.

이러한 $$C$$에서 canonical bundle $$K_C$$의 complete linear system $$|K_C|$$가 정의하는 morphism $$\varphi_{K_C} \colon C \to \mathbb{P}^{g-1}$$의 거동을 살펴보자. $$\deg K_C = 2g - 2$$이고 $$h^0(K_C) = g$$이므로, $$\varphi_{K_C}$$의 공역은 $$\mathbb{P}^{g-1}$$이다. 그러나 실제로 $$\varphi_{K_C}$$는 본래의 hyperelliptic double cover $$C \to \mathbb{P}^1$$로 분해되며, 2:1 covering map이 되므로 closed embedding이 아니다. 즉, $$\varphi_{K_C}$$의 image는 $$\mathbb{P}^{g-1}$$ 안의 $$\mathbb{P}^1$$로, Veronese embedding $$\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$$의 image에 들어간다. 이에 대한 증명은 [Har, IV.5.2]를 참조한다.

따라서 $$K_C$$는 ample이지만 very ample이 아닌 line bundle의 구체적인 예시를 제공한다. 이는 [§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10)에서 언급되었던 "ample but not very ample" 현상의 실현이다. Curve에서 $$\mathcal{L}$$이 very ample이기 위한 충분조건이 $$\deg \mathcal{L} \ge 2g + 1$$임이 알려져 있으며 ([Har, IV.3.2]), $$\deg K_C = 2g - 2 < 2g + 1$$이므로 이 조건을 만족하지 못함도 확인할 수 있다. 대신 $$K_C^{\otimes 2}$$의 degree는 $$4g - 4 \ge 2g + 1$$ (since $$g \ge 2$$)이므로, $$K_C^{\otimes 2}$$는 very ample이다. 이는 ample의 정의—어떤 거듭제곱이 very ample이면 ample—와 완벽하게 부합한다.

이와 대조적으로, $$g \ge 3$$인 non-hyperelliptic curve에서는 canonical map $$\varphi_{K_C} \colon C \to \mathbb{P}^{g-1}$$가 closed embedding이 되어, $$K_C$$ 자체가 very ample이다 ([Har, IV.5.4]).

## Adjunction Formula

Adjunction formula는 smooth variety $$X$$의 smooth divisor $$D$$의 canonical bundle을 ambient variety $$X$$의 canonical bundle으로 표현하는 정리이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> (Adjunction Formula) Smooth variety $$X$$의 smooth divisor $$D$$에 대해

$$\omega_D \cong \omega_X \otimes \mathcal{O}_X(D)|_D$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D$$를 $$X$$의 smooth divisor라 하자. $$D$$의 ideal sheaf를 $$\mathcal{I}_D$$라 하면, $$\mathcal{I}_D$$는 rank 1의 locally free sheaf이며 $$\mathcal{O}_X(-D) \cong \mathcal{I}_D$$가 성립한다. Smooth divisor에 대한 *conormal exact sequence*

$$0 \to \mathcal{I}_D / \mathcal{I}_D^2 \to \Omega_X^1|_D \to \Omega_D^1 \to 0$$

가 성립한다. 이 exact sequence에서 $$\mathcal{I}_D / \mathcal{I}_D^2 \cong \mathcal{O}_X(-D)|_D$$임을 확인하자. $$D$$가 smooth이므로, 각 점 $$p \in D$$ 근방에서 $$D$$는 단일 regular function $$f$$에 의해 잘려 나온다. 즉, $$\mathcal{I}_{D,p} = (f) \subset \mathcal{O}_{X,p}$$이다. 따라서 $$(\mathcal{I}_D / \mathcal{I}_D^2)_p \cong (f)/(f^2) \cong f \cdot \mathcal{O}_{D,p}$$로서 $$\mathcal{O}_{D,p}$$ 위의 free module of rank 1이다. 이는 전역적으로 $$\mathcal{I}_D / \mathcal{I}_D^2 \cong \mathcal{O}_X(-D)|_D$$임을 보여준다.

이제 conormal exact sequence에서 top exterior power를 취한다. $$\Omega_X^1|_D$$는 locally free of rank $$\dim X = n$$이고, $$\mathcal{I}_D/\mathcal{I}_D^2$$와 $$\Omega_D^1$$은 각각 locally free of rank $$1$$과 $$\dim D = n-1$$이다. 따라서

$$\bigwedge\nolimits^{\!n} (\Omega_X^1|_D) \cong \bigwedge\nolimits^{\!1} (\mathcal{I}_D/\mathcal{I}_D^2) \otimes \bigwedge\nolimits^{\!n-1} \Omega_D^1$$

즉, $$\omega_X|_D \cong \mathcal{O}_X(-D)|_D \otimes \omega_D$$이 되고, 이를 정리하면

$$\omega_D \cong \omega_X|_D \otimes (\mathcal{O}_X(-D)|_D)^{-1} \cong \omega_X|_D \otimes \mathcal{O}_X(D)|_D = \omega_X \otimes \mathcal{O}_X(D)|_D$$

를 얻는다.

</details>

Adjunction formula는 hypersurface의 canonical bundle을 계산하는 데 매우 유용하다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$C \subset \mathbb{P}^2$$가 degree $$d$$의 smooth curve라 하자. Adjunction formula에 의해

$$\omega_C \cong \omega_{\mathbb{P}^2}|_C \otimes \mathcal{O}_{\mathbb{P}^2}(C)|_C \cong \mathcal{O}_{\mathbb{P}^2}(-3)|_C \otimes \mathcal{O}_{\mathbb{P}^2}(d)|_C \cong \mathcal{O}_C(d-3)$$

이다. 따라서 $$K_C \sim (d-3)H|_C$$이며, $$\deg K_C = d(d-3) = 2g - 2$$이다. 특히 $$d = 3$$이면 $$K_C \sim 0$$이므로 $$C$$는 genus 1의 elliptic curve임을 알 수 있다.

</div>

## Serre Duality

Canonical bundle의 가장 중요한 응용 중 하나는 Serre duality이다. Smooth projective variety $$X$$ of dimension $$n$$에 대해, 임의의 coherent sheaf $$\mathcal{F}$$에 대하여

$$H^i(X, \mathcal{F})^\ast \cong H^{n-i}(X, \omega_X \otimes \mathcal{F}^\vee)$$

가 성립한다. 특히 $$H^n(X, \omega_X) \cong \mathbb{K}$$이다. 이 정리에 대한 증명과 응용은 [§Sheaf Cohomology](/ko/math/algebraic_geometry/sheaf_cohomology)에서 다룬다. Serre duality는 canonical bundle이 cohomology group 사이의 perfect pairing을 정의하는 dualizing object로서의 역할을 명확히 보여준다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977. (II.8. Differentials; III.7. The Dualizing Sheaf)
