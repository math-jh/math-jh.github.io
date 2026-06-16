---
title: "J-holomorphic curves"
description: "심플렉틱 다양체 위의 거의 복소구조와 호환성을 정의하고, J-홀로모픽 곡선의 개념과 에너지 등식, 제거 가능한 특이점, 그로프 압축 정리를 개괄한다."
excerpt: "Almost complex structure에 대한 holomorphic curve와 Gromov compactness"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/j_holomorphic_curves
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-06-01
weight: 5

published: false
---

[§사교다양체](/ko/math/symplectic_geometry/symplectic_manifold)에서 우리는 symplectic form $$\omega$$로 부여된 manifold $$(M, \omega)$$의 기본 성질을 살펴 보았다. 1985년 M. Gromov는 *almost complex structure* $$J$$를 도입하여, 두 종류의 기하학—complex 측면과 symplectic 측면—을 한 다양체 위에서 *맞물려* 다룰 수 있는 framework을 제시하였다. 그 결과 등장하는 *J-holomorphic curve*는 Gromov-Witten 이론과 Floer 이론의 근간이 되는 객체이다.

본 글에서는 compatible almost complex structure의 정의로부터 출발하여, J-holomorphic curve의 정의와 그 기본 성질 (energy identity, removable singularity), 그리고 Gromov compactness theorem의 statement까지 개괄한다.

## Compatible almost complex structure

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Manifold $$M$$의 *almost complex structure<sub>거의 복소구조</sub>*란 tangent bundle 위의 endomorphism $$J: TM \to TM$$로 $$J^2 = -\mathrm{id}_{TM}$$을 만족하는 것이다. $$(M, J)$$를 *almost complex manifold*라 부른다.

</div>

Symplectic manifold $$(M, \omega)$$ 위에서는 $$J$$가 $$\omega$$와 어떤 *호환성*을 가질 때 특히 유용하다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$(M, \omega)$$를 symplectic manifold라 하자. Almost complex structure $$J$$가 $$\omega$$와 *compatible* (또는 *$$\omega$$-tame*)하다는 것은 다음 두 조건을 만족함을 의미한다.

1. **Tameness:** 임의의 nonzero $$v \in TM$$에 대해 $$\omega(v, Jv) > 0$$.
2. **Compatibility:** $$\omega(Jv, Jw) = \omega(v, w)$$가 모든 $$v, w \in TM$$에 대해 성립.

Tameness만 만족하는 경우 *$$\omega$$-tame*이라 하고, 두 조건 모두 만족하면 *$$\omega$$-compatible* (또는 *$$\omega$$-calibrated*)이라 한다.

</div>

Compatible $$J$$가 주어지면

$$g_J(v, w) := \omega(v, J w)$$

은 symmetric positive-definite bilinear form, 즉 *Riemannian metric*이 된다. 이로써 $$(M, \omega, J)$$는 *almost Kähler structure*를 갖는다. 만약 $$J$$가 integrable이면 (즉 Nijenhuis tensor $$N_J = 0$$이면) $$(M, \omega, J, g_J)$$는 Kähler manifold이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 symplectic manifold $$(M, \omega)$$ 위에는 compatible almost complex structure $$J$$가 존재한다. 더욱이 compatible $$J$$들의 공간 $$\mathcal{J}(M, \omega)$$는 contractible (특히 path-connected) 하다.

</div>

<details class="proof" markdown="1">
<summary>증명 개요</summary>

각 점 $$p \in M$$의 tangent space $$T_p M$$ 위에서는 [§사교벡터공간](/ko/math/symplectic_geometry/linear_symplectic_geometry)의 결과에 의해 compatible linear complex structure가 존재하며, 그 공간이 contractible임이 알려져 있다 (이는 본질적으로 $$\mathrm{Sp}(2n, \mathbb{R})/U(n)$$이 contractible이라는 것과 동치이다). 이 fiberwise compatible $$J$$들을 partition of unity로 patch하면 global compatible $$J$$가 얻어진다.

</details>

[명제 3](#prop3)은 J-holomorphic curve 이론에서 핵심적인 출발점이다. $$J$$를 자유롭게 *섭동*할 수 있다는 사실 덕분에, J-holomorphic curve의 moduli space를 generic $$J$$에 대해 잘 통제된 manifold (또는 orbifold) 로 만들 수 있다.

## J-holomorphic curve의 정의

이제 도메인 측은 Riemann surface로 둔다. $$(\Sigma, j)$$를 $$j^2 = -\mathrm{id}$$를 만족하는 almost complex structure가 부여된 (실 2차원) closed surface라 하자.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Almost complex manifold $$(M, J)$$와 Riemann surface $$(\Sigma, j)$$에 대해, smooth map $$u: \Sigma \to M$$이 *J-holomorphic* (또는 *pseudoholomorphic*) 이라 함은 nonlinear *Cauchy-Riemann equation*

$$\bar\partial_J u := \tfrac{1}{2}\big(du + J \circ du \circ j\big) = 0$$

을 만족함을 말한다. 등가적으로, $$u$$의 differential $$du: T\Sigma \to TM$$이 $$J$$-linear, 즉 $$du \circ j = J \circ du$$를 만족함을 말한다.

</div>

Local coordinate $$z = s + it$$를 $$\Sigma$$에 도입하고 $$u = u(s, t)$$로 쓰면 Cauchy-Riemann equation은

$$\frac{\partial u}{\partial s} + J(u) \frac{\partial u}{\partial t} = 0$$

의 형태가 된다. $$J$$가 integrable한 (즉 complex structure를 정의하는) 표준적인 경우 이는 통상적인 holomorphic map의 조건과 일치하며, 따라서 J-holomorphic curve는 holomorphic curve의 *almost complex* 일반화이다.

## Energy identity

J-holomorphic curve의 분석에서 핵심적인 양은 *energy<sub>에너지</sub>*이다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Smooth map $$u: \Sigma \to M$$의 *energy*는

$$E(u) := \frac{1}{2}\int_\Sigma \lvert du \rvert^2_J\, d\mathrm{vol}_\Sigma$$

으로 정의된다. 여기서 $$\lvert du \rvert_J$$는 $$g_J$$로 유도되는 Hilbert-Schmidt norm이고, $$d\mathrm{vol}_\Sigma$$는 어떤 적절한 metric에 대한 면적 form이다.

</div>

J-holomorphic curve의 결정적 성질은 energy가 *topological data*만으로 결정된다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** (Energy identity)</ins> $$u: \Sigma \to M$$이 $$J$$-holomorphic이면

$$E(u) = \int_\Sigma u^\ast \omega = \omega \cdot u_\ast [\Sigma]$$

이 성립한다. 즉, energy는 $$u$$가 represent하는 homology class $$\beta := u_\ast [\Sigma] \in H_2(M, \mathbb{Z})$$에 대한 symplectic area $$\omega \cdot \beta$$와 일치한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Compatibility $$\omega(Jv, Jw) = \omega(v, w)$$를 사용하면 임의의 vector $$v \in T_p \Sigma$$에 대해

$$\lvert du(v) \rvert^2_J = \omega(du(v), J du(v)) = \omega(du(v), du(jv))$$

이며, 마지막 등식에서 $$J \circ du = du \circ j$$ (J-holomorphicity)을 사용하였다. $$\Sigma$$의 local orthonormal frame $$\{ e_1, e_2 = je_1 \}$$를 잡으면

$$\lvert du \rvert^2_J = \lvert du(e_1) \rvert^2_J + \lvert du(e_2) \rvert^2_J = 2\,\omega(du(e_1), du(e_2)) = 2\, u^\ast \omega(e_1, e_2)$$

이고, $$d\mathrm{vol}_\Sigma(e_1, e_2) = 1$$이므로 양변을 $$d\mathrm{vol}_\Sigma$$로 적분하면

$$E(u) = \int_\Sigma u^\ast \omega$$

이다. 우변은 cohomology class만에 의존하므로 $$= \omega \cdot u_\ast [\Sigma]$$이다.

</details>

[명제 6](#prop6)의 직접적 결과는, 고정된 homology class $$\beta$$를 represent하는 J-holomorphic curve들은 모두 *uniformly bounded energy*를 가진다는 것이다. 이 사실이 moduli space의 compactness 분석의 출발점이 된다.

## Removable singularity

$$\Sigma$$의 한 점 $$p$$ 근방에서만 정의된 J-holomorphic map의 경우, 다음 *removable singularity* 정리는 끝점에서 그 map이 매끄럽게 확장됨을 보장한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7** (Removable singularity, Gromov)</ins> Punctured disk $$D^\ast := \{ 0 < \lvert z \rvert < 1 \}$$에서 정의된 J-holomorphic map $$u: D^\ast \to M$$이 finite energy $$E(u) < \infty$$를 가지면, $$u$$는 origin $$0$$까지 $$C^\infty$$-매끄럽게 확장된다.

</div>
<details class="proof" markdown="1">
<summary>증명 개요</summary>

핵심 단계는 다음과 같다. 우선 $$g_J$$에 대한 *mean value inequality*에 의해, J-holomorphic map은 작은 ball 위에서의 energy를 알면 image 직경을 ball 반지름의 함수로 통제할 수 있다. 즉 $$E(u\vert_{B_r(z)}) < \varepsilon_0$$이면 $$\mathrm{diam}(u(B_{r/2}(z)))$$는 $$C\sqrt{E(u\vert_{B_r})}$$ 이하이다. Finite energy 가정에 의해 $$z\to 0$$일 때 작은 annulus 위의 energy가 $$0$$으로 수렴하므로, 위 부등식으로부터 $$u$$가 $$0$$에서 어떤 점 $$x_0\in M$$으로 연속적으로 확장됨이 얻어진다.

매끄러움은 elliptic regularity로부터 따른다. $$M$$ 위 $$x_0$$ 근방의 Darboux 좌표에서 J-holomorphic equation $$\bar\partial_J u = 0$$은 변형 Cauchy-Riemann equation이며, 그 leading symbol이 elliptic이므로 $$u$$의 $$L^\infty$$ boundedness와 weak J-holomorphic 조건으로부터 $$C^\infty$$ regularity가 점 $$0$$까지 확장된다. 자세한 estimate는 **[MS]** §4.5를 참조한다.

</details>

[명제 7](#prop7)은 J-holomorphic curve의 *bubble* 형성 시 중요한 역할을 한다. Sequence of J-holomorphic curves가 한 점으로 energy를 집중시키면, *rescaling*을 통해 $$\mathbb{C} \to M$$의 J-holomorphic map을 얻고, [명제 7](#prop7)에 의해 이는 $$\mathbb{P}^1 = \mathbb{C} \cup \{\infty\} \to M$$의 J-holomorphic *sphere*로 확장된다. 이 sphere를 *bubble*이라 부른다.

## Gromov compactness

J-holomorphic curve 이론의 중심 정리는 다음 *Gromov compactness theorem*이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8** (Gromov compactness)</ins> $$(M, \omega)$$를 compact symplectic manifold, $$\beta \in H_2(M, \mathbb{Z})$$를 고정하자. Sequence of J-holomorphic curves $$u_n: \Sigma \to M$$이 모두 homology class $$\beta$$를 represent하고, $$\Sigma$$가 fixed Riemann surface (genus $$g$$, $$n$$개의 marked points 부착)일 때, $$\{ u_n \}$$은 부분수열 추출 후 *stable map*으로 수렴한다.

</div>

Stable map이란 nodal Riemann surface $$\widehat\Sigma \to M$$의 J-holomorphic map으로, 각 component가 $$\mathbb{P}^1$$ (또는 더 일반 genus) 의 $$J$$-holomorphic curve이고 *stability* 조건 (자동 동형군이 유한) 을 만족하는 것이다. 정확한 정의와 그 moduli space의 구성은 [§Stable maps의 moduli space](/ko/math/symplectic_geometry/stable_maps)에서 다룬다.

Gromov compactness의 의미: J-holomorphic curve들의 sequence가 limit을 가질 때, 그 limit은 *smooth* J-holomorphic curve가 아닐 수 있으며 *bubble*들이 떨어져 나가는 nodal 구조가 형성될 수 있다. 그러나 이 nodal 구조가 *유한히 많은* bubble만 가지며 *총 homology class는 보존*된다 ($$\sum_i \beta_i = \beta$$). 이 사실이 moduli space의 compactification—즉 *moduli space of stable maps* $$\overline{\mathcal{M}}_{g, n}(M, \beta)$$—을 가능하게 만든다.

## 응용: Gromov-Witten 이론과 Floer 이론

J-holomorphic curve의 가장 영향력 있는 응용은 [§Gromov-Witten 불변량](/ko/math/symplectic_geometry/gromov_witten)이다. 거기서 우리는 stable map의 moduli space 위에 정의된 *virtual fundamental class*에 cohomology class를 evaluate하여 enumerative invariant를 얻는다. 이로부터 *quantum cohomology* 구조가 유도된다.

또 다른 응용은 *Floer homology*이다. 특정 Lagrangian submanifold 사이의 J-holomorphic strip을 세어 만든 chain complex의 homology가 Lagrangian Floer homology이며, symplectic topology의 주요 도구로 사용된다.

---

**참고문헌**

**[Gro85]** M. Gromov, *Pseudo-holomorphic curves in symplectic manifolds*, Invent. Math. **82** (1985), 307--347.

**[MS]** D. McDuff, D. Salamon, *J-holomorphic Curves and Symplectic Topology*, AMS Colloquium Publications **52**, 2nd ed., 2012.

**[Hum]** C. Hummel, *Gromov's Compactness Theorem for Pseudoholomorphic Curves*, Progr. Math. **151**, Birkhäuser, 1997.
