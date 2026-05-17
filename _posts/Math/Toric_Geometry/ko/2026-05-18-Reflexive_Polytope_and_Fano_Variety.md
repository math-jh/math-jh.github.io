---
title: "파노 다양체"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/reflexive_polytope_fano

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Reflexive_Polytope_and_Fano_Variety.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-05-18
last_modified_at: 2026-05-18
weight: 4
published: false
---

[§토릭 다양체의 정의](/ko/math/toric_geometry/toric_varieties)에서 우리는 lattice polytope $$P \subset M_{\mathbb{R}}$$의 normal fan $$\Sigma_P$$을 통해 projective toric variety $$X_P$$를 구성하는 방법을 살펴 보았다. 이 구성에서 $$P$$의 기하학적 성질이 $$X_P$$의 대수기하학적 성질로 변환되는 여러 경로가 존재하며, 그 중에서도 특별한 위치를 차지하는 것이 *reflexive polytope*이다. Batyrev가 1994년 도입한 이 조합론적 대상은 toric variety가 *Gorenstein Fano variety* — anticanonical divisor가 ample이면서 Cartier인 매우 좋은 종류의 projective variety — 인 것과 정확히 대응되며, 따라서 reflexive polytope의 분류는 toric Fano variety의 분류와 동치이다. 이 글에서는 reflexive polytope의 정의와 기본 성질을 정리하고, reflexive polytope이 어떻게 Gorenstein Fano toric variety와 anticanonical divisor의 데이터를 동시에 결정하는지를 살펴 본다.

## 반사 다면체

우선 lattice $$M$$과 그 dual lattice $$N = \Hom(M, \mathbb{Z})$$를 고정하고, $$\langle -, - \rangle : M_{\mathbb{R}} \times N_{\mathbb{R}} \to \mathbb{R}$$를 자연스러운 쌍대 페어링이라 하자. 다음은 reflexive polytope의 정의이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$M_{\mathbb{R}}$$의 $$d$$차원 *lattice polytope* $$\Delta$$가 다음 두 조건을 만족할 때, 이를 *reflexive polytope<sub>반사 다면체</sub>*라 부른다:

1. 원점 $$0$$이 $$\Delta$$의 내부에 포함된다.
2. $$\Delta$$의 *dual polytope*<sub>쌍대 다면체</sub>

$$\Delta^\circ = \{ v \in N_{\mathbb{R}} \mid \langle u, v \rangle \ge -1 \text{ for all } u \in \Delta \}$$

이 다시 lattice polytope가 된다. 즉 $$\Delta^\circ$$의 모든 꼭짓점이 lattice $$N$$에 속한다.

</div>

정의 1의 첫 번째 조건 $$0 \in \operatorname{int}(\Delta)$$는 단순한 정규화가 아니라 dual $$\Delta^\circ$$가 polytope가 되기 위한 필수 조건이다. 이를 두 방향으로 확인해 보자.

먼저 $$0 \in \operatorname{int}(\Delta)$$일 때 $$\Delta^\circ$$가 bounded임을 보인다. 가정으로부터 어떤 $$\varepsilon > 0$$에 대해 ball $$B_\varepsilon(0) \subseteq \Delta$$이다. 임의의 $$v \in \Delta^\circ$$와 단위벡터 $$w$$에 대해 $$\varepsilon w \in \Delta$$이므로 정의에 의해 $$\langle \varepsilon w, v\rangle \ge -1$$, 즉 $$\langle w, v\rangle \ge -1/\varepsilon$$이다. 이 부등식을 $$w = -v/\lVert v \rVert$$에 적용하면 $$-\lVert v \rVert \ge -1/\varepsilon$$, 즉 $$\lVert v \rVert \le 1/\varepsilon$$을 얻으므로 $$\Delta^\circ \subseteq B_{1/\varepsilon}(0)$$이며 bounded이다.

반대로 $$0 \in \partial \Delta$$인 경우에는 $$\Delta^\circ$$가 unbounded가 된다. $$\Delta$$가 convex이므로 원점에서의 supporting hyperplane이 존재하며, 그 외향 normal vector를 $$w_0 \neq 0$$이라 하면 모든 $$u \in \Delta$$에 대해 $$\langle u, w_0\rangle \le \langle 0, w_0\rangle = 0$$이다. 이제 $$\lambda \ge 0$$에 대해 $$v = -\lambda w_0$$를 잡으면 모든 $$u \in \Delta$$에서

$$\langle u, -\lambda w_0\rangle = -\lambda \langle u, w_0\rangle \ge 0 \ge -1$$

이 성립하므로 $$-\lambda w_0 \in \Delta^\circ$$이다. 즉 $$\Delta^\circ$$는 ray $$\{-\lambda w_0 : \lambda \ge 0\}$$ 전체를 포함하여 unbounded하다. 따라서 reflexive polytope를 논의할 때 $$0 \in \operatorname{int}(\Delta)$$라는 조건은 필수적이다.

Reflexive polytope의 가장 기본적인 성질은 dual 연산 $$\Delta \mapsto \Delta^\circ$$이 reflexive polytope들의 모임 위에서 대합(involution)을 이룬다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Bipolar theorem)**</ins> $$\Delta \subset M_{\mathbb{R}}$$가 reflexive polytope이면 $$\Delta^\circ \subset N_{\mathbb{R}}$$도 reflexive polytope이며, $$(\Delta^\circ)^\circ = \Delta$$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$가 reflexive이므로 $$\Delta^\circ$$는 정의에 의해 lattice polytope이다. $$\Delta$$의 모든 원소 $$u$$에 대해 $$\langle u, v \rangle \ge -1$$이 모든 $$v \in \Delta^\circ$$에서 성립하므로, $$\Delta \subseteq (\Delta^\circ)^\circ$$는 정의로부터 직접 확인할 수 있다. 반대로 $$w \in (\Delta^\circ)^\circ$$라 하면, $$w$$는 모든 $$v \in \Delta^\circ$$에 대해 $$\langle w, v \rangle \ge -1$$을 만족한다. 이것이 $$w \in \Delta$$를 함의함을 보이기 위해, $$\Delta$$의 각 facet $$\Theta$$를 생각한다. $$\Theta$$는 $$\Delta$$의 boundary 위의 $$(d-1)$$차원 면이며, reflexive polytope의 정의에 의해 $$\Theta$$는 방정식 $$\langle u, v_\Theta \rangle = -1$$으로 주어진다. 여기서 $$v_\Theta \in N$$은 $$\Theta$$에 대응하는 primitive inner normal vector이다. 그런데 $$v_\Theta \in \Delta^\circ$$의 꼭짓점이 되므로, $$\langle w, v_\Theta \rangle \ge -1$$이 성립한다. 이는 $$w$$가 $$\Delta$$의 모든 facet을 정의하는 반평면들의 교집합에 포함됨을 의미하며, 따라서 $$w \in \Delta$$이다. 이로부터 $$(\Delta^\circ)^\circ = \Delta$$를 얻는다. 마지막으로 $$(\Delta^\circ)^\circ = \Delta$$가 lattice polytope이므로 $$\Delta^\circ$$도 reflexive이다.

</details>

이 명제는 reflexive polytope의 대칭성을 보여준다. $$\Delta$$와 $$\Delta^\circ$$는 서로 다른 vector space $$M_{\mathbb{R}}$$와 $$N_{\mathbb{R}}$$에 놓이지만, 동일한 조합론적 대상의 두 가지 측면을 제공한다.

## Gorenstein Fano variety

대수기하학에서 *Fano variety*는 anticanonical divisor $$-K_X$$가 ample한 ([\[대수다양체\] §선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)) normal projective variety $$X$$를 의미한다. 여기서 canonical divisor $$K_X$$는 canonical bundle에 대응하는 divisor class이며 ([\[대수다양체\] §표준선다발, ⁋정의 6](/ko/math/algebraic_varieties/canonical_bundle#def6)), $$-K_X$$는 그 역원이다. 만약 $$-K_X$$가 추가로 Cartier divisor라면 ([\[대수다양체\] §인자, ⁋정의 12](/ko/math/algebraic_varieties/divisors#def12)) $$X$$를 *Gorenstein Fano variety*라 부른다. Toric variety의 맥락에서 이 조건은 매우 명시적인 조합론적 조건으로 번역된다.

[§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)에서 보았듯, lattice polytope $$P \subset M_{\mathbb{R}}$$에 대해 그 normal fan $$\Sigma_P$$을 통해 projective toric variety $$X_P = X_{\Sigma_P}$$를 구성할 수 있다. 이제 $$P = \Delta$$가 reflexive polytope라고 가정하자.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Toric variety $$X_\Sigma$$의 *anticanonical divisor*는 boundary divisor들의 합

$$-K_{X_\Sigma} = \sum_{\rho \in \Sigma(1)} D_\rho$$

으로 정의된다. 여기서 $$\Sigma(1)$$은 $$\Sigma$$의 1차원 cone들의 집합이고, 각 $$D_\rho$$는 $$\rho$$에 대응하는 torus-invariant prime divisor이다.

</div>

이 정의 자체는 임의의 fan에 대해 well-defined하지만, 우리가 관심을 갖는 *ample* 조건은 (그리고 Fano 조건은) $$X_\Sigma$$가 complete일 때 의미를 가지므로 이하에서는 $$\Sigma$$가 complete fan임을 가정한다.

$$-K_{X_\Sigma}$$가 Cartier divisor일 때 그에 대응하는 piecewise linear function ([§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6)) $$\psi_{-K} \in \PL(\Sigma, M)$$은 정확히 $$\psi_{-K}(v_\rho) = -1$$ for all $$\rho \in \Sigma(1)$$인 함수이다. 따라서 [§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6)의 compatibility 조건에 의해 $$-K_{X_\Sigma}$$가 Cartier인 것은 각 maximal cone $$\sigma$$에 대해 $$m_\sigma \in M$$이 존재하여 $$\langle m_\sigma, v_\rho \rangle = -1$$ for all $$\rho \in \sigma(1)$$인 것과 동치이다. 이 조건이 reflexive polytope의 dual $$\Delta^\circ$$의 꼭짓점 조건과 정확히 일치함이 다음 명제의 핵심이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$에 대해, $$\Delta$$의 normal fan을 $$\Sigma_\Delta$$라 하고 대응하는 toric variety를 $$X_\Delta = X_{\Sigma_\Delta}$$라 적으면, $$X_\Delta$$는 Gorenstein Fano variety이다. 역으로, 어떤 complete toric variety $$X_\Sigma$$가 Gorenstein Fano이면 $$\Sigma$$는 어떤 reflexive polytope의 normal fan이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$가 reflexive polytope라고 하자. $$\Sigma_\Delta$$의 각 maximal cone $$\sigma$$는 inner normal fan ([§토릭 다양체의 정의, ⁋정의 6](/ko/math/toric_geometry/toric_varieties#def6))의 정의에 의해 $$\Delta$$의 어떤 꼭짓점 $$u_\sigma$$에 대응하며, $$\sigma$$의 ray generator $$v_\rho$$들은 정확히 $$u_\sigma$$를 포함하는 facet들의 inner primitive normal이다. $$\Delta$$의 facet 방정식이 $$\langle u, v_\Theta \rangle = -1$$ (그리고 $$\Delta$$ 위에서는 $$\langle u, v_\Theta\rangle \ge -1$$)이므로, $$u_\sigma$$는 $$\Delta$$ 위 $$\langle -, v_\rho\rangle$$의 최솟값을 정확히 $$-1$$로 달성한다. 즉

$$\langle u_\sigma, v_\rho\rangle = -1 \le \langle u, v_\rho\rangle \quad \text{for all } u \in \Delta, \rho \in \sigma(1)$$

이며 등호는 $$u \in F_\rho$$ (facet)일 때만 성립한다. 따라서 $$m_\sigma = u_\sigma \in M$$이 [§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6)의 Cartier compatibility를 만족하며 $$-K_{X_\Delta}$$는 Cartier이다.

한편 $$-K_{X_\Delta}$$의 ample성을 보이려면 piecewise linear function $$\psi_{-K}$$가 strictly convex ([§토러스 인자와 선다발, ⁋정의 8](/ko/math/toric_geometry/toric_divisors#def8))임을 확인하면 충분하다 ([§토러스 인자와 선다발, ⁋명제 9](/ko/math/toric_geometry/toric_divisors#prop9)). $$v$$가 $$\sigma$$의 interior에 있을 때 $$\psi_{-K}(v) = \langle u_\sigma, v\rangle$$이고, 위에서 본 minimum 성질이 $$\sigma$$의 interior 위에서는 strict로 강화된다 — 다른 cone $$\sigma' \neq \sigma$$의 vertex $$u_{\sigma'}$$에 대해 $$u_{\sigma'}$$는 $$u_\sigma$$를 포함하는 facet들 중 적어도 하나에 속하지 않으므로 $$\langle u_\sigma, v\rangle < \langle u_{\sigma'}, v\rangle$$이다. 즉 $$\psi_{-K}(v) < \langle m_{\sigma'}, v\rangle$$이 [§토러스 인자와 선다발, ⁋정의 8](/ko/math/toric_geometry/toric_divisors#def8)의 strict convexity 조건을 그대로 충족한다.

반대로 $$X_\Sigma$$가 Gorenstein Fano라고 가정하자. $$-K_{X_\Sigma}$$가 Cartier이므로 각 maximal cone $$\sigma$$에 대해 $$m_\sigma \in M$$이 존재하여 $$\langle m_\sigma, v_\rho \rangle = -1$$ for all $$\rho \in \sigma(1)$$이다. 이제

$$\Delta = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma(1) \}$$

으로 정의하면, $$\Delta$$는 lattice polytope이며 $$0 \in \operatorname{int}(\Delta)$$이다. $$\Delta$$의 dual은 $$\Delta^\circ = \operatorname{conv}\{v_\rho \mid \rho \in \Sigma(1)\}$$가 되고, 이는 lattice polytope이므로 $$\Delta$$는 reflexive이다. $$\Sigma$$가 $$\Delta$$의 normal fan임은 정의로부터 확인할 수 있다.

</details>

이 명제는 reflexive polytope와 Gorenstein toric Fano variety 사이의 일대일 대응을 확립한다. 이 대응은 Batyrev의 mirror symmetry 이론에서 핵심적인 역할을 한다.

## Anticanonical divisor와 lattice points

Reflexive polytope $$\Delta$$와 Gorenstein Fano variety $$X_\Delta$$ 사이의 대응은 단순히 variety의 존재를 넘어, 그 위에 놓인 선다발의 해들 사이의 대응으로도 확장된다. 구체적으로, anticanonical divisor $$-K_{X_\Delta}$$에 대응하는 선다발 $$\mathcal{O}_{X_\Delta}(-K_{X_\Delta})$$의 global section들은 reflexive polytope $$\Delta$$ 내부의 lattice points들과 일대일로 대응한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$와 대응하는 toric variety $$X_\Delta$$에 대해, 다음의 $$\mathbb{C}$$-vector space 동형이 성립한다:

$$H^0\bigl(X_\Delta, \mathcal{O}_{X_\Delta}(-K_{X_\Delta})\bigr) \cong \bigoplus_{u \in \Delta \cap M} \mathbb{C} \cdot \chi^u.$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Toric variety에서 $$T_N$$-invariant Cartier divisor $$D$$에 대응하는 polytope $$P_D$$는

$$P_D = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1) \}$$

으로 정의되며, [§토러스 인자와 선다발, ⁋명제 7](/ko/math/toric_geometry/toric_divisors#prop7)에서 보인 바와 같이 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$의 basis는 $$P_D \cap M$$의 원소들에 대응하는 characters $$\chi^u$$들로 주어진다. Anticanonical divisor $$-K_{X_\Delta}$$의 경우 $$a_\rho = 1$$ for all $$\rho$$이므로,

$$P_{-K} = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma_\Delta(1) \}$$

이다. 그런데 $$\Sigma_\Delta$$가 $$\Delta$$의 normal fan이므로, 위의 부등식들이 정의하는 polytope는 정확히 $$\Delta$$와 일치한다. 따라서 $$P_{-K} = \Delta$$이고, 원하는 동형이 성립한다.

</details>

이 결과는 reflexive polytope의 lattice point 개수가 Gorenstein Fano variety의 anticanonical 선다발의 해들의 차원, 즉 *anticanonical degree*를 결정함을 의미한다. 특히 $$\Delta \cap M$$의 원소 개수는 $$h^0(X_\Delta, \mathcal{O}(-K_{X_\Delta}))$$와 같다.

## 예시: Projective space

가장 기본적인 reflexive polytope의 예시는 projective space $$\mathbb{P}^n$$에 대응하는 simplex이다. [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 standard simplex $$\Delta_n$$의 normal fan이 $$\mathbb{P}^n$$의 표준 fan임을 보았다. 그러나 $$\Delta_n$$의 꼭짓점 중 하나가 원점이므로 $$0 \notin \operatorname{int}(\Delta_n)$$이다. 따라서 $$\Delta_n$$ 자체는 reflexive polytope가 아니다. 대신, 적절한 변형을 통해 원점을 내부로 옮긴 polytope를 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Lattice $$M = \mathbb{Z}^n$$에서 다음의 polytope를 정의한다:

$$\Delta = \{ (x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge -1 \;\text{for all}\; i,\; x_1 + x_2 + \cdots + x_n \le 1 \}.$$

이 polytope는 standard simplex를 원점 방향으로 확장한 형태이며, 그 꼭짓점은 $$(-1, -1, \ldots, -1)$$과 $$(n, -1, \ldots, -1), \ldots, (-1, \ldots, -1, n)$$이다. 각 facet은 방정식 $$x_i = -1$$ 또는 $$x_1 + \cdots + x_n = 1$$으로 주어지며, 이들에 대응하는 primitive inner normal vector는 각각 $$e_i \in N$$과 $$-(e_1 + \cdots + e_n) \in N$$이다. 따라서 $$\Delta$$의 dual polytope는

$$\Delta^\circ = \operatorname{conv}\{ e_1, e_2, \ldots, e_n, -(e_1 + e_2 + \cdots + e_n) \}$$

가 되어 다시 lattice polytope가 된다. 즉 $$\Delta$$는 reflexive polytope이다. 한편 $$\Delta$$의 normal fan은 [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 확인한 $$\mathbb{P}^n$$의 표준 fan과 일치하므로 $$X_\Delta \cong \mathbb{P}^n$$이 성립한다.

이 예시에서 $$\Delta$$의 lattice points는 꼭짓점 외에도 boundary와 내부 위에 여러 lattice point들이 존재할 수 있다. 예를 들어 $$n=2$$일 때 $$\Delta = \operatorname{conv}\{(-1,-1), (2,-1), (-1,2)\}$$의 lattice points는

$$(-1,-1), (-1,0), (-1,1), (-1,2), (0,-1), (0,0), (0,1), (1,-1), (1,0), (2,-1)$$

으로 총 $$10$$개이며, 이는 $$h^0(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(3)) = 10$$과 일치함을 확인할 수 있다.

</div>

위의 예시에서 주목할 점은 $$\Delta$$와 $$\Delta^\circ$$가 서로 다른 toric variety를 정의한다는 것이다. $$X_\Delta \cong \mathbb{P}^2$$ (smooth)인 반면, $$\Delta^\circ = \mathrm{conv}\{(1,0), (0,1), (-1,-1)\}$$의 normal fan을 구체적으로 계산해 보면 그 ray들이 $$(-1,-1)$$, $$(2,-1)$$, $$(-1,2)$$임을 알 수 있는데, 인접한 두 ray로 만든 행렬의 determinant가 $$\pm 1$$이 아닌 $$\pm 3$$이므로 $$X_{\Delta^\circ}$$는 smooth하지 않다 (사실 세 점에 $$\mathbb{Z}/3$$ 특이점을 갖는 singular Gorenstein Fano surface이다). 이 reflexive pair $$(\Delta, \Delta^\circ)$$이 곧 [§Reflexive Polytope과 Batyrev Mirror, ⁋예시 3](/ko/math/mirror_symmetry/toric_geometry_batyrev#ex3)에서 다루는 *Batyrev mirror pair*의 가장 작은 예시이며, 두 reflexive polytope이 서로 dual 관계를 이루는 데서 mirror symmetry가 발생한다.

본 글의 결과 — reflexive polytope ↔ Gorenstein Fano toric variety 대응과 $$\Delta \cap M$$이 결정하는 anticanonical sections — 는 정확히 [§Reflexive Polytope과 Batyrev Mirror](/ko/math/mirror_symmetry/toric_geometry_batyrev)에서 Calabi-Yau hypersurface의 mirror pair를 구성하기 위한 출발점이 된다. 그 글에서 Hodge number 대칭성과 $$\mathbb{P}^2$$ 예제의 자세한 계산을 다룬다.

---

**참고문헌**

**[Bat]** V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces in toric varieties*, J. Algebraic Geom. 3 (1994), 493--535.

**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.
