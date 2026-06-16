---
title: "파노 다양체"
description: "반사 다면체의 정의와 쌍대 다면체의 성질을 살펴보고, bipolar theorem을 통해 파노 다양체의 기하학적 구조를 이해하는 방법을 다룬다."
excerpt: "Reflexive polytope과 그에 대응하는 Gorenstein Fano 토릭 다양체"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/reflexive_polytope_fano

sidebar:
    nav: "toric_geometry-ko"

date: 2026-05-18
weight: 4
---

[§토릭 다양체의 정의](/ko/math/toric_geometry/toric_varieties)에서 우리는 lattice polytope $$P \subset M_{\mathbb{R}}$$의 normal fan $$\Sigma_P$$을 통해 projective toric variety $$X_P$$를 구성하는 방법을 살펴 보았다. 이 구성에서 $$P$$의 기하학적 성질이 $$X_P$$의 대수기하학적 성질로 변환되는 여러 경로가 존재하며, 그 중에서도 특별한 위치를 차지하는 것이 *reflexive polytope*이다. 

## 반사 다면체

우선 lattice $$M$$과 그 dual lattice $$N = \Hom(M, \mathbb{Z})$$를 고정하고, $$\langle -, - \rangle : M_{\mathbb{R}} \times N_{\mathbb{R}} \to \mathbb{R}$$를 자연스러운 dual pairing이라 하자. 그럼 이 pairing을 통해 주어진 polytope을 반대쪽 dual lattice로 옮길 수 있다. 그 정의에 의해 *reflexive polytope*은 그 결과 또한 lattice polytope으로 떨어지는 것이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$M_{\mathbb{R}}$$의 $$d$$차원 *lattice polytope* $$\Delta$$가 다음 두 조건을 만족할 때, 이를 *reflexive polytope<sub>반사 다면체</sub>*라 부른다:

1. 원점 $$0$$이 $$\Delta$$의 내부에 포함된다.
2. $$\Delta$$의 *dual polytope*<sub>쌍대 다면체</sub>

$$\Delta^\circ = \{ v \in N_{\mathbb{R}} \mid \langle u, v \rangle \ge -1 \text{ for all } u \in \Delta \}$$

이 다시 lattice polytope가 된다. 즉 $$\Delta^\circ$$의 모든 꼭짓점이 lattice $$N$$에 속한다.

</div>

두 번째 조건은 뜻하는 바가 꽤나 투명하지만, 첫째 조건은 다소 쓸모없는 것처럼 느껴질 수 있다. 직관적으로, 만일 $$\Delta$$가 원점을 포함하지 않는다면 $$\Delta$$ 내부의 어떤 벡터의 <em-ko>반대방향</em-ko> 벡터가 존재하지 않으므로 이 벡터와 pairing했을 때 양이 되는 방향의 dual vector를 하나 잡은 후 이를 계속 늘리면 $$\Delta^\circ$$을 정의하는 조건이 unbounded하게 정의된다. 때문에 우리는 위와 같은 두 조건을 필수로 요구하게 된다. 

그 이름에 걸맞게, reflexive polytope의 가장 기본적인 성질은 dual 연산 $$\Delta \mapsto \Delta^\circ$$이 reflexive polytope들의 모임 위에서 involution을 이룬다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Bipolar theorem)**</ins> $$\Delta \subset M_{\mathbb{R}}$$가 reflexive polytope이면 $$\Delta^\circ \subset N_{\mathbb{R}}$$도 reflexive polytope이며, $$(\Delta^\circ)^\circ = \Delta$$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$가 reflexive이므로 $$\Delta^\circ$$는 정의에 의해 lattice polytope이다. $$\Delta$$의 모든 원소 $$u$$에 대해 $$\langle u, v \rangle \ge -1$$이 모든 $$v \in \Delta^\circ$$에서 성립하므로, $$\Delta \subseteq (\Delta^\circ)^\circ$$는 정의로부터 직접 확인할 수 있다. 

이제 반대방향을 보이기 위해 $$w \in (\Delta^\circ)^\circ$$라 하면, $$w$$는 모든 $$v \in \Delta^\circ$$에 대해 $$\langle w, v \rangle \ge -1$$을 만족한다. 이제 $$\Delta$$의 각 facet $$\Theta$$를 생각하면, $$\Theta$$는 $$\Delta$$의 boundary 위의 $$(d-1)$$차원 면이며, reflexive polytope의 정의에 의해 $$\Theta$$는 방정식 $$\langle u, v_\Theta \rangle = -1$$으로 주어진다. 여기서 $$v_\Theta \in N$$은 $$\Theta$$에 대응하는 primitive inner normal vector이다. 그런데 $$v_\Theta \in \Delta^\circ$$의 꼭짓점이 되므로, $$\langle w, v_\Theta \rangle \ge -1$$이 성립한다. 이는 $$w$$가 $$\Delta$$의 모든 facet을 정의하는 반평면들의 교집합에 포함됨을 의미하며, 따라서 $$w \in \Delta$$이다. 이로부터 $$(\Delta^\circ)^\circ = \Delta$$를 얻는다. 마지막으로 $$(\Delta^\circ)^\circ = \Delta$$가 lattice polytope이므로 $$\Delta^\circ$$도 reflexive이다.

</details>

이 명제는 reflexive polytope의 대칭성을 보여준다. $$\Delta$$와 $$\Delta^\circ$$는 서로 다른 vector space $$M_{\mathbb{R}}$$와 $$N_{\mathbb{R}}$$에 놓이지만, 동일한 조합론적 대상의 두 가지 측면을 제공한다.

## 파노 다양체

대수기하학에서 *Fano variety*는 anticanonical divisor $$-K_X$$가 ample인 normal projective variety $$X$$를 의미한다. 여기서 canonical divisor $$K_X$$는 canonical bundle에 대응하는 divisor class이며 ([\[대수다양체\] §표준선다발, ⁋정의 6](/ko/math/algebraic_varieties/canonical_bundle#def6)), $$-K_X$$는 그 역원이다. 만약 $$-K_X$$가 추가로 Cartier divisor라면 $$X$$를 *Gorenstein Fano variety*라 부른다. Toric variety의 맥락에서 이 조건은 매우 명시적인 조합론적 조건으로 번역된다.

[§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)에서 보았듯, lattice polytope $$P \subset M_{\mathbb{R}}$$이 주어지면 이것이 정의하는 normal fan $$\Sigma_P$$을 통해 projective toric variety $$X_P = X_{\Sigma_P}$$를 구성할 수 있다. 이제 $$P = \Delta$$가 reflexive polytope라고 가정하자.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Toric variety $$X_\Sigma$$의 anticanonical divisor $$-K_{X_\Sigma}$$, 즉 canonical divisor의 역원은 모든 boundary divisor의 합으로 주어진다.

$$-K_{X_\Sigma} = \sum_{\rho \in \Sigma(1)} D_\rho.$$

여기서 $$\Sigma(1)$$은 $$\Sigma$$의 1차원 cone들의 집합이고, 각 $$D_\rho$$는 $$\rho$$에 대응하는 torus-invariant prime divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[\[대수다양체\] §표준선다발, ⁋정의 6](/ko/math/algebraic_varieties/canonical_bundle#def6)에서 canonical divisor $$K_X$$는 canonical bundle $$\omega_X = \det \Omega^1_X$$에 대응하는 divisor class로 정의되었다. 우리는 $$K_{X_\Sigma} = -\sum_\rho D_\rho$$임을 보여 그 역원이 위의 형태가 되는 것을 증명한다.

Open dense torus $$T_N = \operatorname{Spec} \mathbb{C}[M] \subset X_\Sigma$$ 위에서, $$M$$의 기저 $$m_1, \ldots, m_n$$을 잡으면 character $$\chi^{m_i}$$들이 torus의 좌표가 되고, top form

$$\omega = \frac{d\chi^{m_1}}{\chi^{m_1}} \wedge \cdots \wedge \frac{d\chi^{m_n}}{\chi^{m_n}}$$

이 $$\Omega^n_{T_N}$$을 trivialize한다. 이는 $$M$$의 기저 선택과 무관한 $$T_N$$-invariant top form이며, $$X_\Sigma$$ 위의 rational $$n$$-form으로 자연스럽게 확장된다.

이제 각 boundary divisor $$D_\rho$$ 위에서 $$\omega$$의 vanishing degree를 계산하자. Ray $$\rho \in \Sigma(1)$$의 primitive generator $$v_\rho \in N$$을 첫 번째 기저로 하는 $$N$$의 적절한 기저를 잡고 그 dual로 $$M$$의 기저 $$m_1, \ldots, m_n$$을 택하면, $$\rho$$를 face로 갖는 affine chart $$U_\sigma$$에서 $$D_\rho$$의 local equation은 $$\chi^{m_1} = 0$$이다. 그럼 위 표현에서 $$d\chi^{m_1}/\chi^{m_1}$$ 항이 $$D_\rho$$를 따라 정확히 1차 pole을 만들고, 다른 인자들은 $$D_\rho$$ 근방에서 regular하므로 $$\omega$$는 $$D_\rho$$를 따라 정확히 1차 pole을 갖는다. 따라서

$$\operatorname{div}(\omega) = -\sum_{\rho \in \Sigma(1)} D_\rho$$

이며, $$K_{X_\Sigma}$$는 이 divisor의 class이므로 $$-K_{X_\Sigma} = \sum_\rho D_\rho$$이다. 

</details>

이 등식 자체는 임의의 fan에 대해 잘 정의되지만, 우리가 관심을 갖는 *ample* 조건은 (그리고 Fano 조건은) $$X_\Sigma$$가 complete일 때 의미를 가지므로 이하에서는 $$\Sigma$$가 complete fan임을 가정한다.

Anticanonical divisor $$-K_{X_\Sigma}$$가 Cartier divisor일 때 그에 대응하는 piecewise linear function $$\psi_{-K} \in \PL(\Sigma, M)$$은 정확히 $$\psi_{-K}(v_\rho) = -1$$가 모든 $$\rho \in \Sigma(1)$$에 대해 성립하는 함수이다. 또, 우리는 [§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6)에서 maximal cone에서만 이 조건을 체크해도 될 뿐만 아니라, 해당 조건이 정확하게 주어진 divisor가 Cartier divisor일 조건과 일치하는 것을 살펴보았다. 이제 이 조건이 reflexive polytope의 dual $$\Delta^\circ$$의 꼭짓점 조건과 정확히 일치한다는 것이 다음 명제의 핵심이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$에 대해, $$\Delta$$의 normal fan을 $$\Sigma_\Delta$$라 하고 대응하는 toric variety를 $$X_\Delta = X_{\Sigma_\Delta}$$라 적으면, $$X_\Delta$$는 Gorenstein Fano variety이다. 역으로, 어떤 complete toric variety $$X_\Sigma$$가 Gorenstein Fano이면 $$\Sigma$$는 어떤 reflexive polytope의 normal fan이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$가 reflexive polytope라고 하자. $$\Sigma_\Delta$$의 각 maximal cone $$\sigma$$는 [§토릭 다양체의 정의, ⁋정의 6](/ko/math/toric_geometry/toric_varieties#def6)에 의해 $$\Delta$$의 어떤 꼭짓점 $$u_\sigma$$에 대응하며, $$\sigma$$의 ray generator $$v_\rho$$들은 정확히 $$u_\sigma$$를 포함하는 facet들의 inner primitive normal이다. $$\Delta$$의 facet 방정식이 $$\langle u, v_\Theta \rangle = -1$$이므로, $$u_\sigma$$는 $$\Delta$$ 위 $$\langle -, v_\rho\rangle$$의 최솟값을 정확히 $$-1$$로 달성한다. 즉

$$\langle u_\sigma, v_\rho\rangle = -1 \le \langle u, v_\rho\rangle \quad \text{for all } u \in \Delta, \rho \in \sigma(1)$$

이며 등호는 $$u \in F_\rho$$ (facet)일 때만 성립한다. 따라서 $$m_\sigma = u_\sigma \in M$$이 [§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6)의 Cartier compatibility를 만족하며 $$-K_{X_\Delta}$$는 Cartier이다.

한편 $$-K_{X_\Delta}$$의 ample성을 보이려면 piecewise linear function $$\psi_{-K}$$가 strictly convex임을 확인하면 충분하다 ([§토러스 인자와 선다발, ⁋명제 9](/ko/math/toric_geometry/toric_divisors#prop9)). 즉 서로 다른 두 maximal cone $$\sigma, \sigma'$$와 그에 대응하는 $$u_\sigma, u_{\sigma'}$$에 대해 $$\langle u_{\sigma'}, v\rangle$$이 $$v \in \sigma$$ 위에서 $$\psi_{-K}(v) = \langle u_\sigma, v\rangle$$의 upper bound가 되며, 등호가 정확히 $$v \in \sigma \cap \sigma'$$에서만 성립하는 것을 보이면 된다.

$$v \in \sigma$$를 $$v = \sum_{\rho \in \sigma(1)} c_\rho v_\rho$$ ($$c_\rho \ge 0$$)로 분해하자. 각 $$\rho \in \sigma(1)$$에 대해 $$u_{\sigma'} \in \Delta$$이므로 $$\langle u_{\sigma'}, v_\rho \rangle \ge -1$$이고, 또 $$u_\sigma \in F_\rho$$이므로 $$\langle u_\sigma, v_\rho\rangle = -1$$이다. 따라서

$$\langle u_{\sigma'}, v\rangle = \sum_{\rho \in \sigma(1)} c_\rho \langle u_{\sigma'}, v_\rho\rangle \ge -\sum_{\rho \in \sigma(1)} c_\rho = \langle u_\sigma, v\rangle$$

이며, 등호는 $$c_\rho > 0$$인 모든 $$\rho$$에 대해 $$\langle u_{\sigma'}, v_\rho\rangle = -1$$, 즉 $$u_{\sigma'} \in F_\rho$$일 때만 정확하게 성립한다. 그런데 facet의 vertex 구조에 의해 "$$u_{\sigma'} \in F_\rho$$"는 "$$\rho \in \sigma'(1)$$"과 동치이므로, 등호 성립 조건은 $$v$$가 $$\sigma \cap \sigma'$$의 ray들만으로 결합된다는 것이고 이는 정확히 $$v \in \sigma \cap \sigma'$$이다. 이로써 strict convexity가 증명된다.

반대로 $$X_\Sigma$$가 Gorenstein Fano라고 가정하자. $$-K_{X_\Sigma}$$가 Cartier이므로 각 maximal cone $$\sigma$$에 대해 $$m_\sigma \in M$$이 존재하여 $$\langle m_\sigma, v_\rho \rangle = -1$$ for all $$\rho \in \sigma(1)$$이다. 이제

$$\Delta = \{ u \in M_{\mathbb{R}} \mid \langle u, v_\rho \rangle \ge -1 \text{ for all } \rho \in \Sigma(1) \}$$

으로 정의하면, $$\Delta$$는 lattice polytope이며 $$0 \in \operatorname{int}(\Delta)$$이다. $$\Delta$$의 dual은 $$\Delta^\circ = \operatorname{conv}\{v_\rho \mid \rho \in \Sigma(1)\}$$가 되고, 이는 lattice polytope이므로 $$\Delta$$는 reflexive이다. $$\Sigma$$가 $$\Delta$$의 normal fan임은 정의로부터 확인할 수 있다.

</details>

한편, reflexive polytope $$\Delta$$와 Gorenstein Fano variety $$X_\Delta$$ 사이의 대응은 단순히 variety의 존재를 넘어, 그 위에 놓인 line bundle의 해들 사이의 대응으로도 확장된다. 구체적으로, anticanonical divisor $$-K_{X_\Delta}$$에 대응하는 line bundle $$\mathcal{O}_{X_\Delta}(-K_{X_\Delta})$$의 global section들은 reflexive polytope $$\Delta$$ 내부의 lattice point들과 일대일로 대응한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Reflexive polytope $$\Delta \subset M_{\mathbb{R}}$$와 대응하는 toric variety $$X_\Delta$$에 대해, 다음의 $$\mathbb{C}$$-vector space isomorphism이 성립한다.

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

이 결과는 reflexive polytope의 lattice point 개수가 Gorenstein Fano variety의 anticanonical line bundle의 해들의 차원, 즉 *anticanonical degree*를 결정함을 의미한다. 특히 $$\Delta \cap M$$의 원소 개수는 $$h^0(X_\Delta, \mathcal{O}(-K_{X_\Delta}))$$와 같다.

역시 가장 기본적인 reflexive polytope의 예시는 projective space $$\mathbb{P}^n$$에 대응하는 simplex이다. [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 standard simplex $$\Delta_n$$의 normal fan이 $$\mathbb{P}^n$$의 표준 fan임을 보았다. 그러나 $$\Delta_n$$의 꼭짓점 중 하나가 원점이므로 $$0 \notin \operatorname{int}(\Delta_n)$$이다. 따라서 $$\Delta_n$$ 자체는 reflexive polytope가 아니다. 대신, 이 polytope의 각 변을 적절히 늘려 원점을 내부로 옮긴 (닮음인) polytope를 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> Lattice $$M = \mathbb{Z}^n$$에서 다음의 polytope

$$\Delta = \{ (x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge -1 \;\text{for all}\; i,\; x_1 + x_2 + \cdots + x_n \le 1 \}$$

을 정의하자. 이 polytope는 standard simplex를 원점 방향으로 확장한 형태이며, 그 꼭짓점은 $$(-1, -1, \ldots, -1)$$과 $$(n, -1, \ldots, -1), \ldots, (-1, \ldots, -1, n)$$이다. 각 facet은 방정식 $$x_i = -1$$ 또는 $$x_1 + \cdots + x_n = 1$$으로 주어지며, 이들에 대응하는 primitive inner normal vector는 각각 $$e_i \in N$$과 $$-(e_1 + \cdots + e_n) \in N$$이다. 따라서 $$\Delta$$의 dual polytope는

$$\Delta^\circ = \operatorname{conv}\{ e_1, e_2, \ldots, e_n, -(e_1 + e_2 + \cdots + e_n) \}$$

가 되어 다시 lattice polytope가 된다. 즉 $$\Delta$$는 reflexive polytope이다. 한편 $$\Delta$$의 normal fan은 [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 확인한 $$\mathbb{P}^n$$의 표준 fan과 일치하므로 $$X_\Delta \cong \mathbb{P}^n$$이 성립한다.

이 예시에서 우리는 $$\Delta$$의 크기를 키웠으므로 이제 $$\Delta$$는 꼭짓점 외에도 boundary와 내부 위에 여러 lattice point들을 가질 수 있다. 예를 들어 $$n=2$$일 때 $$\Delta = \operatorname{conv}\{(-1,-1), (2,-1), (-1,2)\}$$의 lattice points는

$$(-1,-1), (-1,0), (-1,1), (-1,2), (0,-1), (0,0), (0,1), (1,-1), (1,0), (2,-1)$$

으로 총 $$10$$개이며, 이는 $$h^0(\mathbb{P}^2, \mathcal{O}_{\mathbb{P}^2}(3)) = 10$$과 일치함을 확인할 수 있다.

</div>

## 거울 대칭

위의 [예시 6](#ex6)을 다시 들여다보면 흥미로운 현상이 보이는데, $$\Delta$$와 $$\Delta^\circ$$는 동일한 reflexive 데이터의 두 측면이지만, 그로부터 만들어지는 toric variety $$X_\Delta$$와 $$X_{\Delta^\circ}$$는 일반적으로 서로 매우 다르다는 것이다. 가령 $$n=2$$의 standard simplex 변형의 경우, $$X_\Delta \cong \mathbb{P}^2$$인 반면 $$\Delta^\circ = \mathrm{conv}\{(1,0), (0,1), (-1,-1)\}$$의 normal fan의 인접한 ray들의 determinant를 계산해보면 그 값은 $$\pm3$$으로 smooth variety조차 되지 않는다. ([§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11)) 실제로 $$X_{\Delta^\circ}$$은 세 maximal cone마다 $$\mathbb{Z}/3$$ quotient singularity를 갖는 singular Gorenstein Fano surface $$\mathbb{P}^2/(\mathbb{Z}/3)$$이다. 

자연스러운 질문은 이들 두 variety들 $$X_\Delta$$와 $$X_{\Delta^\circ}$$ 사이에 기하학적 관계가 있느냐는 것이다. 위의 간단한 예시에서 보았듯, 일반적으로 $$X_\Delta$$와 $$X_{\Delta^\circ}$$ 사이에는 직접적인 morphism이나 birational 동형이 존재하지 않는다. 대신 둘 사이의 진정한 연결은 anticanonical hypersurface를 매개로 드러난다. 그 출발점은 다음의 고전적인 adjunction 결과이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Smooth Fano variety $$X$$의 anticanonical linear system $$\lvert -K_X \rvert$$ 안의 smooth divisor $$V \subset X$$는 trivial canonical bundle을 갖는다. 즉 $$K_V = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[\[대수다양체\] §표준선다발](/ko/math/algebraic_varieties/canonical_bundle)에서의 adjunction formula $$K_V = (K_X + V)\vert_V$$를 사용한다. $$V \in \lvert -K_X \rvert$$이므로 $$V \sim -K_X$$이고 따라서

$$K_V = (K_X + V)\vert_V = (K_X - K_X)\vert_V = 0$$

이 성립한다.

</details>

위에서 언급했듯 $$X_\Delta$$와 $$X_{\Delta^\circ}$$ 사이의 관계는 쉽게 드러나는 종류의 것이 아니며, 이 글의 남은 부분에서 이를 엄밀하게 설명하는 것 또한 불가능하다. 이 둘은 mirror symmetry를 통해 서로 관련되어 있는데, 이는 한 마디로, 두 개의 (보통 isomorphic하지 않은) Calabi-Yau variety가 Hodge 데이터의 특정 대칭을 통해 *짝지어진다*는 가설이다.

[명제 7](#prop7)의 결론 $$K_V = 0$$은 (거의) 정확히 *Calabi-Yau variety*를 특징짓는 대수적인 조건이라는 점에서, $$V$$가 이 mirror symmetry의 무대 위로 올라올 여지를 준다. 마찬가지로 동일한 construction을 $$X_{\Delta^\circ}$$에서도 반복하면 우리는 이 $$V$$의 "mirror pair" $$V^\circ$$ 또한 정의할 수 있을 것이다. 

그러나 일반적으로 reflexive polytope $$\Delta$$로부터 만들어진 $$X_\Delta$$는 singular하며, 이로 인해 두 가지 미묘한 문제가 생긴다.

1. Codimension $$1$$인 $$V$$가 $$X_\Delta$$의 singular locus와 만나는 경우, $$V$$ 자신이 그 점에서 singular하게 된다. 우리 예시인 $$\mathbb{P}^2/(\mathbb{Z}/3)$$에서는 singular locus가 isolated된 세 점이므로 generic cubic curve $$V$$는 이를 피해 smooth하게 잡아줄 수 있지만, 차원이 커질수록 singular locus가 양의 차원이 되어 $$V$$가 반드시 이를 가로지르는 현상이 나타난다. 따라서 [명제 7](#prop7)의 결론을 *singular* $$V$$에 그대로 적용할 수 없다.
2. 따라서, singular한 $$V$$로부터 진정한 smooth Calabi-Yau를 얻으려면 적절한 resolution $$\pi: \widetilde{V} \to V$$가 필요한데, 일반적인 resolution은 canonical class를 보존하지 않는다. 구체적으로, normal Gorenstein variety $$V$$의 임의의 resolution은 다음의 *discrepancy formula*
    
    $$K_{\tilde V} = \pi^\ast K_V + \sum_i a_i E_i$$
    
    를 만족한다는 것이 알려져 있다. 여기서 $$E_i$$는 $$\pi$$의 exceptional divisor이며, $$a_i \in \mathbb{Q}$$는 *discrepancy*라 부르는 유리수이다. 이 식은 $$\pi^\ast K_V$$가 $$\tilde V$$ 위 differential form의 vanishing/pole 구조를 정확히 잡아내지 못하는 부분을 $$a_i E_i$$로 보정한 것으로, $$a_i$$의 부호와 크기가 $$V$$의 특이점 종류를 분류해주는 표준적인 invariant가 된다.
    
    이제 $$V$$가 adjunction에 의해 $$K_V \sim 0$$를 만족한다 하더라도, 임의의 resolution에서
    
    $$K_{\tilde V} = \pi^\ast \cdot 0 + \sum_i a_i E_i = \sum_i a_i E_i$$
    
    이고 generic하게는 $$a_i > 0$$인 항이 존재하여 $$K_{\tilde V} \not\sim 0$$, 즉 $$\tilde V$$가 Calabi-Yau 성질을 잃어버린다. 

따라서 Calabi-Yau 성질을 *보존하는* 유일한 종류의 resolution은 모든 $$a_i = 0$$인 것이며, 이러한 resolution을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Normal Gorenstein variety $$X$$의 resolution of singularities $$\pi: \tilde{X} \to X$$ — 즉, $$\tilde{X}$$가 smooth이고 $$\pi$$가 proper birational morphism — 가

$$K_{\tilde{X}} = \pi^\ast K_X$$

를 만족할 때, 이를 *crepant resolution<sub>크레펀트 분해</sub>*이라 부른다.

</div>

즉 crepant resolution은 dis-crepancy가 없는 resolution이다. 그럼 이 조건이 정확히 [명제 7](#prop7)의 결론을 singular setting까지 끌고 가는 데 필요한 조건이라는 것을 즉시 확인할 수 있고, 이로부터 $$\widetilde{V}$$가 진정한 (smooth) Calabi-Yau가 된다.

Toric setting에서 crepant resolution은 매우 명시적인 격자 데이터로 번역된다. 일반적인 toric resolution이 fan의 refinement (즉 동일 support 위의 더 세밀한 fan)로 주어진다는 사실은 이미 [§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11) 이후의 논의에서 살펴보았다. 그렇다면 이 resolution이 언제 crepant인지가 진정한 의문일텐데, 역시 이 또한 fan의 조합론적 성질로 나타낼 수 있다. 구체적으로, birational morphism $$\pi: X_{\Sigma'} \to X_\Delta$$가 crepant일 필요충분조건은 새로 추가된 ray $$v$$들이 모두 $$\Delta^\circ$$의 *경계* 위에 놓인 lattice point라는 것이다. 

직관적으로 이는 [명제 3](#prop3)의 증명에서 본 anticanonical piecewise linear function $$\psi_{-K}$$가 새 ray $$v$$에 대해서도 여전히 $$\psi_{-K}(v) = -1$$를 만족해야 한다는 것으로 생각할 수 있다. 이는 $$v$$가 cone $$\sigma$$ (vertex $$u_\sigma$$)의 내부에 들어오면 $$\psi_{-K}(v) = \langle u_\sigma, v\rangle = -1$$은 정확히 $$v$$가 $$\Delta^\circ$$의 facet $$F_{u_\sigma}$$ 위에 있다는 것과 동치이기 때문이다. 가령, $$\mathbb{P}^2/(\mathbb{Z}/3)$$의 fan에서 인접 두 ray 사이의 lattice point $$(1,0), (0,1), (-1,-1)$$를 새 ray로 추가하면 세 $$\mathbb{Z}/3$$ 특이점이 동시에 해소되며, 결과는 smooth $$\mathbb{P}^2$$의 fan이 된다.

다만 crepant resolution이 항상 존재하지는 않는다. Toric Gorenstein variety의 경우, $$n \le 3$$에서는 항상 crepant resolution이 존재한다는 것이 알려져 있지만 $$n \ge 4$$에서는 일반적으로 모든 특이점을 동시에 해소할 수 없다. 이제 남는 quotient 특이점의 cohomology 기여를 흡수하기 위해 도입된 것이 아래 mirror 진술에 등장하는 *stringy* Hodge number이며, 이 보정 덕분에 mirror symmetry가 singular한 잔여 부분과 무관하게 reflexive 데이터의 함수로 깔끔히 표현된다. 

Batyrev의 핵심 통찰은 두 Calabi-Yau family $$V, V^\circ$$가 서로 *mirror dual*을 이룬다는 것이다. 보다 구체적으로, reflexive pair $$(\Delta, \Delta^\circ)$$로부터 만들어지는 두 family

$$\bigl\{ V \subset X_\Delta : V \in \lvert -K_{X_\Delta}\rvert \bigr\}, \qquad \bigl\{ V^\circ \subset X_{\Delta^\circ} : V^\circ \in \lvert -K_{X_{\Delta^\circ}}\rvert \bigr\}$$

의 generic member들의 stringy Hodge number는 $$n \ge 4$$일 때 다음의 mirror 대칭

$$h^{p,q}_{\mathrm{st}}(V) = h^{n-1-p,\, q}_{\mathrm{st}}(V^\circ)$$

을 만족한다. 즉 $$X_\Delta$$와 $$X_{\Delta^\circ}$$ 자체가 동치라는 의미는 아니지만, 그 위의 Calabi-Yau hypersurface family들이 mirror symmetry를 통해 짝지어진다는 것이 reflexive duality의 기하학적 내용이다. 

---

**참고문헌**

**[Bat]** V. V. Batyrev, *Dual polyhedra and mirror symmetry for Calabi-Yau hypersurfaces in toric varieties*, J. Algebraic Geom. 3 (1994), 493--535.

**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.
