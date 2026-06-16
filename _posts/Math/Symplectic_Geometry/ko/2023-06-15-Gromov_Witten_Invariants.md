---
title: "Gromov-Witten 불변량"
description: "Gromov-Witten 불변량을 evaluation map과 접선 다발의 첫 번째 Chern class로 정의하고, descendant 버전의 정의와 genus-0에서의 string, divisor, dilaton, splitting 공리들, 그리고 quantum cohomology 구성을 다룬다."
excerpt: "Stable map moduli로부터의 GW invariant 정의와 quantum cohomology"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/gromov_witten
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-06-15
weight: 7

published: false
---

[§Stable maps의 moduli space](/ko/math/symplectic_geometry/stable_maps)에서 우리는 stable map들의 moduli space $$\overline{\mathcal{M}}_{g, n}(X, \beta)$$와 그 위의 virtual fundamental class $$[\overline{\mathcal{M}}_{g, n}(X, \beta)]^{\mathrm{vir}}$$를 구성하였다. 이제 evaluation map과 cotangent line bundle의 first Chern class를 결합하여 *Gromov-Witten invariant*를 정의한다.

본 글에서는 GW invariant와 descendant 버전의 정의, genus-0의 핵심 axiom들 (string, divisor, dilaton, splitting/WDVV), 그리고 quantum cohomology의 구성을 다룬다.

## Gromov-Witten invariant의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$X$$를 compact symplectic manifold (또는 smooth projective variety), $$\beta \in H_2(X, \mathbb{Z})$$를 effective class, $$\alpha_1, \ldots, \alpha_n \in H^\ast(X, \mathbb{Q})$$를 cohomology class라 하자. *Genus $$g$$, $$n$$-point, degree $$\beta$$ Gromov-Witten invariant*

$$\langle \alpha_1, \ldots, \alpha_n \rangle_{g, n, \beta}^X := \int_{[\overline{\mathcal{M}}_{g,n}(X,\beta)]^{\mathrm{vir}}} \prod_{i=1}^n \mathrm{ev}_i^\ast \alpha_i$$

으로 정의된다. 여기서 $$\mathrm{ev}_i: \overline{\mathcal{M}}_{g, n}(X, \beta) \to X$$는 $$i$$번째 marked point에서의 evaluation map이다.

</div>

비유한 적분이 되려면 형식적으로 $$\sum_i \deg \alpha_i = 2\, \mathrm{vdim}_\mathbb{C}\, \overline{\mathcal{M}}_{g, n}(X, \beta)$$ ([§Stable maps의 moduli space, ⁋명제 5](/ko/math/symplectic_geometry/stable_maps#prop5))를 요구하며, 그 외에는 GW invariant가 정의상 $$0$$이다.

## Descendant Gromov-Witten invariant

Cotangent line bundle의 first Chern class $$\psi_i$$를 적분 안에 끼워 넣은 *descendant* 버전은 GW invariant의 풍부한 정합성 조건을 표현하는 데 필수적이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 비음정수 $$a_1, \ldots, a_n$$과 cohomology class $$\alpha_1, \ldots, \alpha_n$$에 대해 *descendant Gromov-Witten invariant*

$$\langle \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{g, n, \beta}^X := \int_{[\overline{\mathcal{M}}_{g,n}(X,\beta)]^{\mathrm{vir}}} \prod_{i=1}^n \psi_i^{a_i}\, \mathrm{ev}_i^\ast \alpha_i$$

으로 정의된다. 여기서 $$\psi_i$$는 $$i$$번째 marked point에서의 cotangent line bundle의 first Chern class이다.

</div>

$$a_i = 0$$이면 primary GW invariant ([정의 1](#def1))로 환원된다. $$\psi$$ class의 power는 *gravitational descendant*라 불리며, 물리에서 *gravitational coupling*의 quantum 보정과 관련된다.

## Genus-0 axiom: string, divisor, dilaton

Genus $$0$$의 primary GW invariant들은 *Kontsevich-Manin axiom*이라 불리는 일련의 정합성 조건을 만족한다. 여기서는 가장 사용 빈도가 높은 세 low-level axiom을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3** (String equation)</ins> 

$$\langle 1, \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{0, n+1, \beta}^X = \sum_{i=1}^n \langle \tau_{a_1}(\alpha_1), \ldots, \tau_{a_i - 1}(\alpha_i), \ldots, \tau_{a_n}(\alpha_n) \rangle_{0, n, \beta}^X$$

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

$$1 \in H^0(X)$$를 evaluate하는 marked point는 기하학적 제약을 주지 않으므로, $$\overline{\mathcal{M}}_{0, n+1}(X, \beta) \to \overline{\mathcal{M}}_{0, n}(X, \beta)$$의 forgetful map의 fiber 위에서 적분하면 cotangent line의 *비교 공식* (comparison)에 의해 $$\psi$$ class가 한 단계 내려간다. 자세한 계산은 [KM]의 string axiom 또는 [HKKPTVVZ Chapter 26]를 참조하라.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4** (Divisor equation)</ins> $$D \in H^2(X, \mathbb{Q})$$이고 $$\beta \neq 0$$일 때

$$\langle D, \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{0, n+1, \beta}^X = (D \cdot \beta)\, \langle \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{0, n, \beta}^X + (\text{lower } \psi \text{ corrections})$$

$$\beta = 0$$이고 $$n \geq 2$$인 경우 우변의 첫 항은 $$0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

[명제 3](#prop3)과 같은 forgetful map 분석에 더해, $$H^2$$ class $$D$$의 경우 evaluation map과의 합성 $$\mathrm{ev}_\ast(D \cap [\overline{\mathcal{M}}_{0, n+1}(X, \beta)]^{\mathrm{vir}})$$이 intersection number $$D \cdot \beta$$의 배수로 계산된다. 이로써 $$H^2$$ 방향의 deformation이 Novikov variable $$q$$로 흡수되는 메커니즘이 설명된다.

</details>

Divisor equation은 $$H^2$$의 marked point가 본질적으로 intersection number $$D \cdot \beta$$만큼 invariant를 곱한다는 statement이다. 이로 인해 $$H^2$$ 방향의 deformation은 *Novikov variable* $$q$$로 흡수된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5** (Dilaton equation)</ins> 

$$\langle \tau_1(1), \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{0, n+1, \beta}^X = (2g - 2 + n)\, \langle \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{0, n, \beta}^X$$

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

마찬가지로 forgetful map의 fiber 위에서 $$\tau_1(1) = \psi^1 \cdot 1$$ class를 적분한다. $$\psi$$의 fiber 적분은 $$2g - 2 + n$$ (Euler characteristic of pointed Riemann surface)이 된다. [KM] 또는 [HKKPTVVZ]의 dilaton axiom 참조.

</details>

## Splitting axiom과 WDVV equation

GW invariant의 가장 강력한 정합성 조건은 *splitting axiom*이며, 그것의 가장 사용 빈도 높은 결과가 *WDVV equation*이다. 도메인 curve의 nodal degeneration boundary에서 virtual class가 splitting되며, 그 결과 4-point GW invariant들이 두 가지 splitting pattern에 따라 두 가지 표현으로 분해되어야 한다는 정합 조건이 WDVV equation이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** (WDVV equation, genus-0)</ins> Gromov-Witten potential

$$F(t) := \sum_{n \geq 3,\, \beta} \frac{1}{n!} \langle t, \ldots, t \rangle_{0, n, \beta}^X\, q^\beta,\qquad t = \sum_\alpha t^\alpha T_\alpha \in H^\ast(X, \mathbb{C})$$

은 다음 *Witten-Dijkgraaf-Verlinde-Verlinde equation*을 만족한다.

$$\sum_{e, f} \partial_a \partial_b \partial_e F\, \eta^{ef}\, \partial_f \partial_c \partial_d F = \sum_{e, f} \partial_a \partial_c \partial_e F\, \eta^{ef}\, \partial_f \partial_b \partial_d F$$

여기서 $$\eta_{\alpha\beta} = \int_X T_\alpha \cup T_\beta$$는 Poincaré pairing이다.

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

증명은 moduli space $$\overline{\mathcal{M}}_{0, 4}(X, \beta)$$의 두 boundary divisor (각각 $$\{a, b\} \vert \{c, d\}$$ splitting과 $$\{a, c\} \vert \{b, d\}$$ splitting에 대응)의 cohomology class가 동일한 *forgetful image* 아래에서 같음에서 출발한다. 두 splitting에 대해 virtual class의 splitting axiom을 적용하면 두 가지 4-point invariant 합 표현이 얻어지고, 두 합이 같아야 함이 WDVV equation이 된다. 자세한 계산은 [KM Section 5], [RT Section 7] 참조.

</details>

WDVV equation의 의미는 다음과 같다. $$F$$의 세 번째 도함수가 정의하는 곱셈 $$\circ$$가 associative하다는 statement와 WDVV equation은 정확히 동치이다. 즉 WDVV는 곧 *quantum product의 결합법칙*이다.

## Quantum cohomology

WDVV equation의 가장 중요한 직접적 응용은 *quantum cohomology*의 구성이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7** (Quantum cohomology)</ins> $$X$$의 *big quantum product* $$\circ_t: H^\ast(X) \otimes H^\ast(X) \to H^\ast(X)$$은 다음으로 정의된다.

$$T_a \circ_t T_b := \sum_{c, d}\, \partial_a \partial_b \partial_c F(t)\, \eta^{cd}\, T_d$$

여기서 $$F(t)$$는 Gromov-Witten potential이고 $$\{ T_a \}$$는 $$H^\ast(X)$$의 basis이다. WDVV equation에 의해 $$\circ_t$$는 associative이며 commutative이다. $$t = 0$$ 근방의 *Novikov variable* $$q = e^{t_{(2)}}$$ 방향만 켠 specialization을 *small quantum product* $$\star_q$$라 부른다.

</div>

Quantum cohomology ring $$(H^\ast(X), \circ_t)$$은 $$t \in H^\ast(X)$$ 위에 매개되는 family of commutative, associative algebra를 이룬다. Classical cup product는 $$q \to 0$$의 극한에서 회복되며, $$\star_q$$의 비자명한 항들은 $$X$$ 위의 rational curve의 수를 부호화한다.

## $$\mathbb{P}^n$$의 GW invariant 예시

<div class="example" markdown="1">

<ins id="ex8">**예시 8** ($$X = \mathbb{P}^n$$)</ins> $$\mathbb{P}^n$$의 cohomology basis는 $$\{ 1, H, H^2, \ldots, H^n \}$$이고 effective curve class는 $$d H^\vee$$ ($$d \geq 0$$)로 매개된다. $$\overline{\mathcal{M}}_{0, n}(\mathbb{P}^n, d)$$의 expected dimension은 $$d(n+1) + n - 3 + n_{\text{marked}}$$이다.

가장 기본적인 GW invariant는 *line counting*이다. $$d = 1$$일 때, $$\mathbb{P}^n$$ 안의 직선 중 두 일반점을 지나는 것은 유일하다. 이는

$$\langle H^n, H^n \rangle_{0, 2, 1}^{\mathbb{P}^n} = 1$$

으로 표현된다 (두 점이 직선상에 있을 조건은 codimension $$n$$이므로 정확히 expected dim과 맞아 떨어진다).

$$\mathbb{P}^2$$에서 5개의 일반점을 지나는 conic ($$d = 2$$)의 개수는 고전적으로 $$1$$이며, 이를 GW invariant로 표현하면

$$\langle H^2, H^2, H^2, H^2, H^2 \rangle_{0, 5, 2}^{\mathbb{P}^2} = 1$$

이다. 일반적인 $$d$$에 대한 *Kontsevich's recursion formula*는 [명제 6](#prop6)의 WDVV equation으로부터 도출되며, $$\mathbb{P}^2$$의 rational curve counting을 모두 결정한다.

</div>

[명제 6](#prop6)의 WDVV equation에 의해 $$\mathbb{P}^2$$의 *모든* genus-0 rational curve count가 $$d = 1$$ case ($$= 1$$)과 4-point invariant들의 splitting으로부터 재귀적으로 결정된다는 것이 Kontsevich (1994)의 유명한 결과이다.

## 더 멀리: virtual class와 비-symplectic 확장

$$X$$가 Calabi-Yau ($$c_1(TX) = 0$$)일 때 expected dimension은 $$g, n$$에만 의존하며, 일반적으로 $$\dim X = 3$$이면 genus $$0$$ point-free invariant가 *유한 개의 rational curve*를 세는 enumerative 의미를 갖는다.

Higher genus 및 K-theoretic 확장 (Givental, Lee, Okounkov), open/relative GW invariant (Solomon, Joyce-Song), Donaldson-Thomas invariant와의 동치 (MNOP conjecture) 등은 본 글의 범위를 넘어선다.

---

**참고문헌**

**[KM]** M. Kontsevich, Yu. Manin, *Gromov-Witten classes, quantum cohomology, and enumerative geometry*, Comm. Math. Phys. **164** (1994), 525--562.

**[RT]** Y. Ruan, G. Tian, *A mathematical theory of quantum cohomology*, J. Differential Geom. **42** (1995), 259--367.

**[BF]** K. Behrend, B. Fantechi, *The intrinsic normal cone*, Invent. Math. **128** (1997), 45--88.

**[MS]** D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications **52**, 2nd ed., 2012.

**[HKKPTVVZ]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
