---
title: "Reflexive polytope와 Fano variety"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/reflexive_polytope_fano

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Reflexive_Polytope_and_Fano_Variety.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 3
published: false
---

[§Normal fan과 projective toric variety](/ko/math/toric_geometry/normal_fan_projective_toric)에서 우리는 lattice polytope $$P \subset M_{\mathbb{R}}$$의 normal fan $$\Sigma_P$$을 통해 projective toric variety $$X_P$$를 구성하는 방법을 살펴 보았다. 이 구성에서 $$P$$의 기하학적 성질이 $$X_P$$의 대수기하학적 성질로 변환되는 여러 경로가 존재하며, 그 중에서도 특별한 위치를 차지하는 것이 *reflexive polytope*이다. Reflexive polytope는 1994년 Batyrev에 의해 도입되어 toric Fano variety의 분류와 mirror symmetry의 조합론적 기반을 제공하는 핵심적인 도구가 되었다. 우리는 이 글에서 reflexive polytope의 정의와 이것이 Gorenstein Fano variety 및 anticanonical divisor와 어떻게 대응하는지를 살펴 본다.

## Reflexive polytope와 dual polytope

우선 lattice $$M$$과 그 쌍대 lattice $$N = \Hom(M, \mathbb{Z})$$를 고정하고, $$\langle -, - \rangle : M_{\mathbb{R}} \times N_{\mathbb{R}} \to \mathbb{R}$$를 자연스러운 쌍대 페어링이라 하자. 다음은 reflexive polytope의 정의이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$M_{\mathbb{R}}$$의 $$d$$차원 *lattice polytope* $$\Delta$$가 다음 두 조건을 만족할 때, 이를 *reflexive polytope<sub>반사 다면체</sub>*라 부른다:

1. 원점 $$0$$이 $$\Delta$$의 낮부에 포함된다: $$0 \in \operatorname{int}(\Delta)$$.
2. $$\Delta$$의 *dual polytope*<sub>쌍대 다면체</sub>

$$\Delta^\circ = \{ v \in N_{\mathbb{R}} \mid \langle u, v \rangle \ge -1 \text{ for all } u \in \Delta \}$$

이 다시 lattice polytope가 된다. 즉 $$\Delta^\circ$$의 모든 꼭짓점이 lattice $$N$$에 속한다.

</div>

Dual polytope의 정의에서 부등호 $$\langle u, v \rangle \ge -1$$는 원점이 $$\Delta$$의 낮부에 있을 때 $$\Delta^\circ$$가 bounded set이 됨을 보장한다. 만약 $$0$$이 $$\Delta$$의 boundary 위에 놓인다면 $$\Delta^\circ$$는 unbounded하게 되어 polytope가 아니게 된다. 따라서 reflexive polytope를 논의할 때 $$0 \in \operatorname{int}(\Delta)$$라는 조건은 필수적이다.

Reflexive polytope의 가장 기본적인 성질은 dual 연산 $$\Delta \mapsto \Delta^\circ$$이 reflexive polytope들의 모임 위에서 초대합(involution)을 이룬다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Bipolar theorem)**</ins> $$\Delta \subset M_{\mathbb{R}}$$가 reflexive polytope이면 $$\Delta^\circ \subset N_{\mathbb{R}}$$도 reflexive polytope이며, $$(\Delta^\circ)^\circ = \Delta$$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$가 reflexive이므로 $$\Delta^\circ$$는 정의에 의해 lattice polytope이다. $$\Delta$$의 모든 원소 $$u$$에 대해 $$\langle u, v \rangle \ge -1$$이 모든 $$v \in \Delta^\circ$$에서 성립하므로, $$\Delta \subseteq (\Delta^\circ)^\circ$$는 정의로부터 직접 확인할 수 있다. 반대로 $$w \in (\Delta^\circ)^\circ$$라 하면, $$w$$는 모든 $$v \in \Delta^\circ$$에 대해 $$\langle w, v \rangle \ge -1$$을 만족한다. 이것이 $$w \in \Delta$$를 함의함을 보이기 위해, $$\Delta$$의 각 facet $$\Theta$$를 생각한다. $$\Theta$$는 $$\Delta$$의 boundary 위의 $$(d-1)$$차원 면이며, reflexive polytope의 정의에 의해 $$\Theta$$는 방정식 $$\langle u, v_\Theta \rangle = -1$$으로 주어진다. 여기서 $$v_\Theta \in N$$은 $$\Theta$$에 대응하는 primitive inner normal vector이다. 그런데 $$v_\Theta \in \Delta^\circ$$의 꼭짓점이 되므로, $$\langle w, v_\Theta \rangle \ge -1$$이 성립한다. 이는 $$w$$가 $$\Delta$$의 모든 facet을 정의하는 반평면들의 교집합에 포함됨을 의미하며, 따라서 $$w \in \Delta$$이다. 이로부터 $$(\Delta^\circ)^\circ = \Delta$$를 얻는다. 마지막으로 $$(\Delta^\circ)^\circ = \Delta$$가 lattice polytope이므로 $$\Delta^\circ$$도 reflexive이다.

</details>

이 명제는 reflexive polytope의 대칭성을 보여준다. $$\Delta$$와 $$\Delta^\circ$$는 서로 다른 vector space $$M_{\mathbb{R}}$$와 $$N_{\mathbb{R}}$$에 놓이지만, 동일한 조합론적 대상의 두 가지 측면을 제공한다.

## Gorenstein Fano variety

대수기하학에서 *Fano variety*는 anticanonical divisor $$-K_X$$가 ample한 normal projective variety $$X$$를 의미한다. 만약 $$-K_X$$가 추가로 Cartier divisor라면 $$X$$를 *Gorenstein Fano variety*라 부른다. Toric variety의 맥락에서 이 조건은 매우 명시적인 조합론적 조건으로 번역된다.

[§Normal fan과 projective toric variety, ⁋정의 8](/ko/math/toric_geometry/normal_fan_projective_toric#def8)에서 기술한 것처럼, lattice polytope $$P \subset M_{\mathbb{R}}$$에 대해 그 normal fan $$\Sigma_P$$을 통해 toric variety $$X_P = X_{\Sigma_P}$$를 구성할 수 있다. 이제 $$P = \Delta$$가 reflexive polytope라고 가정하자.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Complete fan $$\Sigma$$가 주어졌을 때, toric variety $$X_\Sigma$$의 *anticanonical divisor*는 boundary divisor들의 합

$$-K_{X_\Sigma} = \sum_{\rho \in \Sigma(1)} D_\rho$$

으로 정의된다. 여기서 $$\Sigma(1)$$은 $$\Sigma$$의 1차원 cone들의 집합이고, 각 $$D_\rho$$는 $$\rho$$에 대응하는 torus-invariant prime divisor이다.

</div>

Toric variety에서 divisor $$D=\sum a_\rho D_\rho$$에 대응하는 **support function** $$\psi_D$$는 각 ray generator $$v_\rho$$에서 $$\psi_D(v_\rho)=-a_\rho$$의 값을 가지는 함수이다. divisor가 Cartier이기 위해서는 각 maximal cone $$\sigma \in \Sigma$$에 대해 lattice point $$m_\sigma \in M$$이 존재하여, 이 support function이 $$\sigma$$ 위에서 $$u \mapsto \langle m_\sigma, u \rangle$$의 형태로 주어져야 한다. Anticanonical divisor $$-K_{X_\Sigma}$$에 대응하는 support function $$\psi_{-K}$$는 각 ray generator $$v_\rho$$에 대해 $$\psi_{-K}(v_\rho) = -1$$의 값을 갖는 piecewise linear function이다. 따라서 $$-K_{X_\Sigma}$$가 Cartier인 것은 각 maximal cone $$\sigma$$에 대해 $$m_\sigma \in M$$이 존재하여 $$\langle m_\sigma, v_\rho \rangle = -1$$ for all $$\rho \in \sigma(1)$$인 것과 동치이다. 이 조건이 reflexive polytope의 dual $$\Delta^\circ$$의 꼭짓점 조건과 정확히 일치함을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$에 대해, $$\Delta$$의 normal fan을 $$\Sigma_\Delta$$라 하고 대응하는 toric variety를 $$X_\Delta = X_{\Sigma_\Delta}$$라 적으면, $$X_\Delta$$는 Gorenstein Fano variety이다. 역으로, 어떤 complete toric variety $$X_\Sigma$$가 Gorenstein Fano이면 $$\Sigma$$는 어떤 reflexive polytope의 normal fan이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$가 reflexive polytope라고 하자. $$\Sigma_\Delta$$의 각 maximal cone $$\sigma$$에 대해, $$\sigma$$는 $$\Delta$$의 어떤 꼭짓점 $$u_\sigma$$에 대응하며, 이 대응은 normal fan의 정의에 의해 다음 성질을 갖는다: $$\sigma$$의 ray generator $$v_\rho$$들은 $$\langle u_\sigma, v_\rho \rangle \ge \langle u, v_\rho \rangle$$ for all $$u \in \Delta$$를 만족한다. 특히 $$\Delta$$의 facet 방정식이 $$\langle u, v_\Theta \rangle = -1$$의 형태이므로, $$\sigma$$의 각 ray generator $$v_\rho$$에 대해 $$\langle u_\sigma, v_\rho \rangle = -1$$이 성립한다. 따라서 $$m_\sigma = u_\sigma \in M$$을 선택하면 $$\langle m_\sigma, v_\rho \rangle = -1$$ for all $$\rho \in \sigma(1)$$이 되며, 이는 $$-K_{X_\Delta}$$가 Cartier임을 의미한다. 한편 $$-K_{X_\Delta}$$의 ample성은 $$\psi_{-K}(v_\rho) = -1$$인 support function이 strictly convex함으로부터 얻어진다. **strictly convex**한 support function은 서로 다른 maximal cone 위에서 서로 다른 선형 함수를 가지며, 이에 대응하는 divisor가 ample이다. 이는 $$\Sigma_\Delta$$가 projective fan임을 보장하며, $$-K_{X_\Delta}$$가 ample divisor임을 의미한다.

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

으로 정의되며, [§Normal fan과 projective toric variety, ⁋명제 9](/ko/math/toric_geometry/normal_fan_projective_toric#prop9)의 증명에서 언급된 바와 같이 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$의 basis는 $$P_D \cap M$$의 원소들에 대응하는 characters $$\chi^u$$들로 주어진다. Anticanonical divisor $$-K_{X_\Delta}$$의 경우 $$a_\rho = 1$$ for all $$\rho$$이므로,

$$P_{-K} = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma_\Delta(1) \}$$

이다. 그런데 $$\Sigma_\Delta$$가 $$\Delta$$의 normal fan이므로, 위의 부등식들이 정의하는 polytope는 정확히 $$\Delta$$와 일치한다. 따라서 $$P_{-K} = \Delta$$이고, 원하는 동형이 성립한다.

</details>

이 결과는 reflexive polytope의 lattice point 개수가 Gorenstein Fano variety의 anticanonical 선다발의 해들의 차원, 즉 *anticanonical degree*를 결정함을 의미한다. 특히 $$\Delta \cap M$$의 원소 개수는 $$h^0(X_\Delta, \mathcal{O}(-K_{X_\Delta}))$$와 같다.

## 예시: Projective space

가장 기본적인 reflexive polytope의 예시는 projective space $$\mathbb{P}^n$$에 대응하는 simplex이다. [§Normal fan과 projective toric variety, ⁋예시 11](/ko/math/toric_geometry/normal_fan_projective_toric#ex11)에서 standard simplex $$\Delta_n$$의 normal fan이 $$\mathbb{P}^n$$의 표준 fan임을 보았다. 그러나 $$\Delta_n$$의 꼭짓점 중 하나가 원점이므로 $$0 \notin \operatorname{int}(\Delta_n)$$이다. 따라서 $$\Delta_n$$ 자체는 reflexive polytope가 아니다. 대신, 적절한 변형을 통해 원점을 내부로 옮긴 polytope를 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Lattice $$M = \mathbb{Z}^n$$에서 다음의 polytope를 정의한다:

$$\Delta = \{ (x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge -1 \text{ for all } i, \; x_1 + x_2 + \cdots + x_n \le 1 \}.$$

이 polytope는 standard simplex를 원점 방향으로 확장한 형태이며, 그 꼭짓점은 $$(-1, -1, \ldots, -1)$$과 $$(n, -1, \ldots, -1), \ldots, (-1, \ldots, -1, n)$$이다. 각 facet은 방정식 $$x_i = -1$$ 또는 $$x_1 + \cdots + x_n = 1$$으로 주어지며, 이들에 대응하는 primitive inner normal vector는 각각 $$e_i \in N$$과 $$-(e_1 + \cdots + e_n) \in N$$이다. 따라서 $$\Delta$$의 dual polytope는

$$\Delta^\circ = \operatorname{conv}\{ e_1, e_2, \ldots, e_n, -(e_1 + e_2 + \cdots + e_n) \}$$

가 되어 다시 lattice polytope가 된다. 즉 $$\Delta$$는 reflexive polytope이다. 한편 $$\Delta$$의 normal fan은 [§Normal fan과 projective toric variety, ⁋예시 11](/ko/math/toric_geometry/normal_fan_projective_toric#ex11)에서 확인한 $$\mathbb{P}^n$$의 표준 fan과 일치하므로 $$X_\Delta \cong \mathbb{P}^n$$이 성립한다.

이 예시에서 $$\Delta$$의 lattice points는 꼭짓점 외에도 boundary와 낮부 위에 여러 lattice point들이 존재할 수 있다. 예를 들어 $$n=2$$일 때 $$\Delta = \operatorname{conv}\{(-1,-1), (2,-1), (-1,2)\}$$의 lattice points는

$$(-1,-1), (-1,0), (-1,1), (-1,2), (0,-1), (0,0), (0,1), (1,-1), (1,0), (2,-1)$$

으로 총 $$10$$개이며, 이는 $$h^0(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(3)) = 10$$과 일치함을 확인할 수 있다.

</div>

위의 예시에서 주목할 점은 $$\Delta$$와 $$\Delta^\circ$$가 동일한 combinatorial type을 가질 수도 있지만, 일반적으로는 서로 다른 모양을 가진다는 것이다. $$n=2$$인 경우 $$\Delta^\circ = \operatorname{conv}\{(1,0), (0,1), (-1,-1)\}$$이 되어 $$\Delta$$와 다른 모양을 가진다. 그러나 이들이 정의하는 toric variety는 모두 $$\mathbb{P}^2$$에 해당한다.

## Mirror symmetry와 Batyrev construction

Reflexive polytope가 대수기하학에서 특별한 관심을 받는 이유는 이것이 mirror symmetry와 깊이 연결되어 있기 때문이다. 1994년 Batyrev는 reflexive polytope $$\Delta$$와 그 dual $$\Delta^\circ$$를 이용하여 Calabi-Yau variety(canonical class가 0인 compact Kähler 다양체)들의 mirror pair를 조합론적으로 구성하는 방법을 제시하였다.

구체적으로, reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$에 대해 $$\Delta^\circ \subset N_{\mathbb{R}}$$도 reflexive이다. $$\Delta$$의 normal fan $$\Sigma_\Delta$$에 대응하는 toric variety $$X_\Delta$$는 Gorenstein Fano variety이며, $$\Delta^\circ$$의 normal fan에 대응하는 toric variety $$X_{\Delta^\circ}$$도 마찬가지이다. 이때 $$\Delta$$에 내재된 정보로부터 $$X_\Delta$$ 위의 anticanonical divisor의 일반적인 단면 $$Y_\Delta$$를 정의할 수 있고, 이는 적절한 crepant resolution(canonical divisor를 보존하는 특이점 해소)을 거친 후 Calabi-Yau variety가 된다. 마찬가지로 $$\Delta^\circ$$로부터 $$X_{\Delta^\circ}$$ 위의 Calabi-Yau variety $$Y_{\Delta^\circ}$$를 얻는다. Batyrev는 이 두 Calabi-Yau variety $$Y_\Delta$$와 $$Y_{\Delta^\circ}$$가 mirror symmetry의 관계에 놓여 있음을 제안하였다.

이 구성의 핵심은 reflexive polytope의 dual 연산 $$\Delta \leftrightarrow \Delta^\circ$$이 Calabi-Yau variety들 사이의 mirror involution을 유도한다는 점이다. 특히 이 mirror pair의 Hodge number(Dolbeault cohomology 차원 $$h^{p,q} = \dim H^{p,q}$$)들은 다음과 같은 대칭성을 보인다:

$$h^{p,q}(Y_\Delta) = h^{d-1-p,q}(Y_{\Delta^\circ}).$$

이러한 Batyrev construction은 이후 Borisov에 의해 complete intersection으로 확장되어 nef-partition(여러 개의 nef divisor로 이루어진 분할)의 이론으로 발전하였으며, 오늘날까지도 toric mirror symmetry의 기본적인 틀로 자리 잡고 있다.

---

**참고문헌**

**[Bat]** V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces in toric varieties*, J. Algebraic Geom. 3 (1994), 493--535.

**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.
