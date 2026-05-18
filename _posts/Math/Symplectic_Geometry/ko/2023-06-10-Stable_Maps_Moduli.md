---

title: "Stable maps의 moduli space"
excerpt: "Stable map의 정의와 moduli space의 compactness, virtual fundamental class"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/stable_maps
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/Stable_Maps_Moduli.png
    overlay_filter: 0.5
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-06-10
last_modified_at: 2026-05-18
weight: 6

published: false
---

[§J-holomorphic curves, ⁋명제 8](/ko/math/symplectic_geometry/j_holomorphic_curves#prop8)의 Gromov compactness theorem은 J-holomorphic curve의 sequence가 일반적으로 smooth limit을 갖지 않으며 *nodal* limit이 발생할 수 있음을 시사한다. 이 nodal limit을 정합적으로 다루는 객체가 *stable map*이며, 그것이 만드는 moduli space $$\overline{\mathcal{M}}_{g, n}(X, \beta)$$가 Gromov-Witten 이론의 토대가 된다. Kontsevich-Manin (1994)에 의해 algebraic 측면에서, Li-Tian과 Fukaya-Ono (1996–1999)에 의해 symplectic 측면에서 정합적으로 구성되었다.

본 글에서는 stable map의 정의, moduli space의 compactness, expected dimension의 계산, 그리고 virtual fundamental class의 존재까지 간략히 정리한다.

## Stable nodal curve

먼저 도메인 측 도구를 정비한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Genus $$g$$, $$n$$개의 marked points를 갖는 *prestable curve* $$(C, p_1, \ldots, p_n)$$이란

- $$C$$는 connected complete (algebraic 또는 complex analytic) curve로, *node*만을 singularity로 가진다 (즉, 각 singular point의 local model이 $$\{xy = 0\} \subset \mathbb{C}^2$$).
- $$p_1, \ldots, p_n \in C$$는 distinct smooth points (즉 node가 아닌 점).
- $$g = h^1(C, \mathcal{O}_C) = p_a(C)$$가 arithmetic genus.

</div>

각 *irreducible component* $$C_i$$는 normalization하면 smooth curve이며, $$C$$의 dual graph는 vertex가 component, edge가 node인 graph이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Prestable curve $$(C, p_1, \ldots, p_n)$$이 *stable<sub>안정</sub>*이라 함은, automorphism group $$\mathrm{Aut}(C, p_1, \ldots, p_n)$$이 *유한*함을 의미한다. 등가적으로:

- Genus $$0$$ component $$C_i$$는 적어도 $$3$$개의 special points (marked points + node)를 가짐.
- Genus $$1$$ component는 적어도 $$1$$개의 special point를 가짐.

</div>

Stability 조건은 *moduli problem이 well-posed*하기 위한 최소 조건이다. Genus $$0$$의 경우 $$\mathrm{Aut}(\mathbb{P}^1) = \mathrm{PGL}_2(\mathbb{C})$$는 3-transitive하므로 3개의 점이 finiteness를 강제한다.

Deligne-Mumford는 1969년 stable curves의 moduli space $$\overline{\mathcal{M}}_{g, n}$$이 *Deligne-Mumford stack*임을 보였다. 그 dimension은 $$3g - 3 + n$$이다 ($$g \geq 2$$ 또는 $$g = 1$$ with $$n \geq 1$$ 또는 $$g = 0$$ with $$n \geq 3$$의 경우).

## Stable map의 정의

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Symplectic manifold (또는 smooth projective variety) $$X$$, genus $$g \geq 0$$, $$n \geq 0$$, homology class $$\beta \in H_2(X, \mathbb{Z})$$가 주어졌다고 하자. *Genus $$g$$, $$n$$-marked, $$\beta$$-class stable map*이란

$$(C, p_1, \ldots, p_n, f),\qquad f: C \to X$$

으로 다음 조건을 만족한다.

- $$(C, p_1, \ldots, p_n)$$은 genus $$g$$의 prestable curve.
- $$f$$는 $$J$$-holomorphic (또는 algebraic하게는 morphism).
- $$f_\ast [C] = \beta \in H_2(X, \mathbb{Z})$$.
- *Stability*: 모든 *contracted* component $$C_i$$ ($$f\vert_{C_i}$$가 상수 map)에 대해 $$\mathrm{Aut}(C_i, p_{i,\bullet})$$이 유한 (즉 prestable curve의 stability 조건을 $$C_i$$가 만족).

두 stable map $$(C, p_\bullet, f)$$와 $$(C', p'_\bullet, f')$$이 *isomorphic*이라 함은 marked points와 map을 보존하는 isomorphism $$\phi: C \xrightarrow{\sim} C'$$이 존재함을 말한다.

</div>

Stability 조건은 *non-contracted* component에서는 자동으로 성립한다 ($$f\vert_{C_i}$$가 non-constant면 그것이 finiteness를 보장). Contracted component에 대해서만 prestable curve의 stability 조건을 부과한다.

## Moduli space의 compactness

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4** (Compactness)</ins> $$(X, \omega)$$가 compact symplectic manifold일 때, *genus $$g$$, $$n$$-marked, $$\beta$$-class stable map들의 isomorphism class 집합*

$$\overline{\mathcal{M}}_{g, n}(X, \beta) := \big\{ (C, p_\bullet, f) \big\} \big/ \sim$$

은 compact (Hausdorff) topological space를 이룬다.

</div>

증명은 [§J-holomorphic curves, ⁋명제 8](/ko/math/symplectic_geometry/j_holomorphic_curves#prop8)의 Gromov compactness theorem의 직접적 적용이다. Stable map들의 sequence가 energy bound (homology class가 fixed이므로 자동) 하에서 reparametrization과 bubble formation 후 stable limit을 갖는다는 statement이다. Stability 조건이 *unique한* limit object를 보장한다.

## Evaluation map과 cotangent line bundle

$$\overline{\mathcal{M}}_{g, n}(X, \beta)$$ 위에는 두 가지 핵심 natural map이 있다.

**Evaluation map.** $$i$$번째 marked point에서의 evaluation

$$\mathrm{ev}_i: \overline{\mathcal{M}}_{g, n}(X, \beta) \to X,\qquad (C, p_\bullet, f) \mapsto f(p_i)$$

**Forgetful map.** Domain의 marked points를 forget하면 $$\overline{\mathcal{M}}_{g, n}(X, \beta) \to \overline{\mathcal{M}}_{g, n}$$이며 (stabilization을 거쳐), $$X$$측 forgetful은 $$\overline{\mathcal{M}}_{g, n}(X, \beta) \to \overline{\mathcal{M}}_{g, n-1}(X, \beta)$$이다.

**Cotangent line bundle (psi class).** $$i$$번째 marked point에서의 cotangent line의 first Chern class

$$\psi_i := c_1(\mathbb{L}_i) \in H^2(\overline{\mathcal{M}}_{g, n}(X, \beta), \mathbb{Q})$$

여기서 $$\mathbb{L}_i$$의 fiber over $$(C, p_\bullet, f)$$는 $$T^\ast_{p_i} C$$이다. $$\psi$$ class는 *gravitational descendant* Gromov-Witten invariant의 정의에 사용된다.

## Expected dimension

$$\overline{\mathcal{M}}_{g, n}(X, \beta)$$의 *expected* (또는 *virtual*) dimension은 deformation-obstruction theory로부터 계산된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5** (Expected dimension)</ins> $$X$$가 complex dimension $$d$$일 때

$$\mathrm{vdim}_\mathbb{C}\, \overline{\mathcal{M}}_{g, n}(X, \beta) = \int_\beta c_1(TX) + (d - 3)(1 - g) + n$$

이다.

</div>

증명 sketch: deformation의 tangent space와 obstruction space의 차원은 deformation theory에서

$$\dim H^0(C, f^\ast TX(-\sum p_i)) - \dim H^1(C, f^\ast TX(-\sum p_i)) + \dim \mathrm{Def}(C, p_\bullet)$$

으로 주어진다. Riemann-Roch on $$C$$를 사용하면 $$\chi(f^\ast TX) = \int_\beta c_1(TX) + d(1-g)$$이고, marked points의 $$-\sum p_i$$는 차원을 $$-nd$$만큼 감소시킨다. Prestable curve의 deformation 차원은 $$3g - 3 + n$$이다. 모두 더하면 위 공식이 나온다.

$$X$$가 Calabi-Yau ($$c_1 = 0$$) 이고 $$g = 0$$, $$n = 0$$이면 $$\mathrm{vdim} = d - 3$$이므로, $$d = 3$$ (Calabi-Yau 3-fold)에서 $$\mathrm{vdim} = 0$$이 되어 *유한 개의 점*을 세는 enumerative problem이 된다. 이것이 quintic 3-fold 위의 rational curve enumeration의 기원이다.

## Virtual fundamental class

$$\overline{\mathcal{M}}_{g, n}(X, \beta)$$은 일반적으로 *singular*이며 *actual* dimension이 expected dimension과 다를 수 있다 (예: excess intersection으로 더 큼). 그럼에도 불구하고, deformation-obstruction theory의 정교한 사용을 통해 *virtual fundamental class*

$$[\overline{\mathcal{M}}_{g, n}(X, \beta)]^{\mathrm{vir}} \in H_{2 \mathrm{vdim}}(\overline{\mathcal{M}}_{g, n}(X, \beta), \mathbb{Q})$$

가 정합적으로 construct된다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** (Virtual fundamental class)</ins> Li-Tian, Behrend-Fantechi (algebraic case), Fukaya-Ono, Ruan, Siebert (symplectic case) 등에 의해, moduli space $$\overline{\mathcal{M}}_{g, n}(X, \beta)$$ 위에 *virtual fundamental class* $$[\overline{\mathcal{M}}_{g, n}(X, \beta)]^{\mathrm{vir}}$$가 잘 정의되며, expected dimension의 homology class를 이룬다.

</div>

Virtual fundamental class의 정확한 construction은 매우 기술적이며, 본 글의 범위를 넘어선다 ([LT], [BF], [FO]). 핵심 idea: actual moduli space가 너무 큰 경우, *obstruction bundle*의 *Euler class*를 곱하여 expected dimension의 cycle을 인공적으로 만들어낸다. Smooth case에서는 $$[\overline{\mathcal{M}}_{g, n}(X, \beta)]^{\mathrm{vir}} = [\overline{\mathcal{M}}_{g, n}(X, \beta)]$$이다.

Virtual fundamental class는 다음의 핵심 성질을 만족한다.

- **Deformation invariance:** $$X$$의 complex/symplectic structure의 deformation 하에 invariant.
- **Splitting axiom:** 도메인 $$C$$의 node에서 분할에 호환.
- **Forgetful axiom:** 도메인의 marked point forget에 호환.

이 axiom들이 *Gromov-Witten 불변량*의 정합성을 보장한다.

## 응용

[§Gromov-Witten 불변량](/ko/math/symplectic_geometry/gromov_witten)에서 우리는 evaluation map $$\mathrm{ev}_i$$와 psi class $$\psi_i$$를 사용하여

$$\langle \tau_{a_1}(\alpha_1), \ldots, \tau_{a_n}(\alpha_n) \rangle_{g, \beta}^X := \int_{[\overline{\mathcal{M}}_{g,n}(X,\beta)]^{\mathrm{vir}}} \prod_i \psi_i^{a_i}\, \mathrm{ev}_i^\ast \alpha_i$$

으로 *descendant Gromov-Witten invariant*를 정의한다. 이로부터 quantum cohomology, Frobenius manifold ([\[거울 대칭\] §Frobenius manifold](/ko/math/mirror_symmetry/frobenius_manifold)), Givental의 $$J$$-function ([\[거울 대칭\] §Givental $$J$$-function과 Mirror Theorem](/ko/math/mirror_symmetry/givental_j_function)) 등 mirror symmetry의 모든 A-model 객체가 유도된다.

---

**참고문헌**

**[KM]** M. Kontsevich, Yu. Manin, *Gromov-Witten classes, quantum cohomology, and enumerative geometry*, Comm. Math. Phys. **164** (1994), 525--562.

**[LT]** J. Li, G. Tian, *Virtual moduli cycles and Gromov-Witten invariants of algebraic varieties*, J. Amer. Math. Soc. **11** (1998), 119--174.

**[BF]** K. Behrend, B. Fantechi, *The intrinsic normal cone*, Invent. Math. **128** (1997), 45--88.

**[FO]** K. Fukaya, K. Ono, *Arnold conjecture and Gromov-Witten invariant*, Topology **38** (1999), 933--1048.

**[MS]** D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications **52**, 2nd ed., 2012.
