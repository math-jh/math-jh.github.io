---
title: "Toric divisors와 line bundles"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/toric_divisors

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Toric_Divisors_and_Line_Bundles.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-08
last_modified_at: 2026-03-08
weight: 4
published: false
---

Toric variety의 가장 강력한 특징 중 하나는 다양체 위의 divisor와 line bundle이 fan의 조합론적 데이터로 완전히 기술된다는 것이다. 우리는 이 글에서 torus-invariant divisor의 구조부터 시작하여, 이들이 정의하는 line bundle과 그 global section, 그리고 ample cone의 기하학적 의미를 조합론적 언어로 재해석한다.

## Torus-invariant Weil divisors

Toric variety $$X_\Sigma$$는 algebraic torus $$T_N$$을 열린 조밀한 부분집합으로 포함하며, $$T_N$$ 위에서는 divisor의 개념이 trivial하다. 따라서 $$X_\Sigma$$ 위에서 의미 있는 divisor는 $$T_N$$의 작용으로 고정되는, 즉 *torus-invariant*인 divisor들을 중심으로 이해할 수 있다.

Fan $$\Sigma$$의 각 1차원 cone, 즉 *ray* $$\rho \in \Sigma(1)$$에 대해 primitive generator $$v_\rho \in N$$을 생각하자. Ray $$\rho$$는 $$X_\Sigma$$ 내의 codimension 1 torus orbit에 대응하며, 이의 Zariski closure가 하나의 irreducible divisor를 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 각 ray $$\rho \in \Sigma(1)$$에 대해, 대응하는 torus orbit의 Zariski closure를 $$D_\rho$$라 적는다. $$D_\rho$$는 $$X_\Sigma$$ 위의 irreducible Weil divisor이며, 이를 **torus-invariant prime divisor**라 부른다.

</div>

이 정의는 toric variety의 궤도 구조로부터 자연스럽게 유도된다. [§Normal fan과 projective toric variety, ⁋명제 5](/ko/math/toric_geometry/normal_fan_projective_toric#prop5)에서 보았듯이, $$d$$-차원 cone은 차원 $$n-d$$의 torus orbit에 대응하므로 1차원 cone $$\rho$$는 차원 $$n-1$$의 궤도, 즉 codimension 1의 torus-invariant 부분다양체에 해당한다. 이 궤도의 Zariski closure는 자연스럽게 divisor가 된다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$X_\Sigma$$ 위의 torus-invariant Weil divisor들이 생성하는 free abelian group을 $$\Div_T(X_\Sigma)$$라 적는다. 즉,

$$\Div_T(X_\Sigma) = \bigoplus_{\rho \in \Sigma(1)} \mathbb{Z} \cdot D_\rho$$

이다. 임의의 torus-invariant Weil divisor는 $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$의 꼴로 유일하게 표현된다.

</div>

Torus action에 의해 고정되지 않는 임의의 divisor는 torus-invariant divisor와 linearly equivalent하므로, toric variety 위의 divisor 이론을 연구할 때 torus-invariant divisor만을 고려하는 것은 본질적인 제한이 아니다. 더 정확히 말하면, $$X_\Sigma$$의 전체 Weil divisor group $$\Div(X_\Sigma)$$에서 torus-invariant divisor들로의 제한은 isomorphism을 유도한다.

## Principal divisors와 class group

이제 character가 정의하는 principal divisor를 살펴 본다. 각각의 $$m \in M$$에 대해, character $$\chi^m: T_N \to \mathbb{C}^\ast$$는 $$X_\Sigma$$ 위의 유리함수로 볼 수 있다. [§Affine toric varieties, ⁋명제 8](/ko/math/toric_geometry/affine_toric_varieties#prop8)에서 보았듯이, $$\chi^m$$은 $$T_N$$ 위에서 eigenvalue $$\chi^m(t)$$를 갖는 rational function이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Character $$\chi^m$$에 대응하는 principal divisor는 다음과 같이 주어진다:

$$\div(\chi^m) = \sum_{\rho \in \Sigma(1)} \langle m, v_\rho \rangle D_\rho.$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 ray $$\rho \in \Sigma(1)$$에 대응하는 affine chart를 생각하자. Ray $$\rho$$를 포함하는 maximal cone $$\sigma$$에 대해 $$U_\sigma$$는 smooth한 국소환경이며, $$D_\rho \cap U_\sigma$$는 하나의 국소좌표 초평면으로 주어진다. Character $$\chi^m$$이 이 국소좌표에서 zeros와 poles를 갖는 방식은 pairing $$\langle m, v_\rho \rangle$$에 의해 결정된다. 구체적으로, $$\chi^m$$은 $$D_\rho$$를 따라서 order $$\langle m, v_\rho \rangle$$의 zero를 갖거나, 이 값이 음수일 때는 같은 크기의 pole을 갖는다. 모든 ray에 대해 이를 합하면 principal divisor의 정의에 의해 원하는 식이 얻어진다.

</details>

이제 자연스러운 group homomorphism $$M \to \Div_T(X_\Sigma)$$, $$m \mapsto \div(\chi^m)$$을 얻는다. 이 homomorphism의 image는 principal divisor들의 모임이며, [\[대수다양체\] §인자, ⁋정의 1](/ko/math/algebraic_varieties/divisors#def1)에서 정의한 것처럼 Weil divisor class group은 이 principal divisor들로의 quotient로 주어진다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 다음의 sequence는 exact하다:

$$0 \longrightarrow M \longrightarrow \Div_T(X_\Sigma) \longrightarrow \Cl(X_\Sigma) \longrightarrow 0.$$

여기서 첫 번째 화살표는 $$m \mapsto \div(\chi^m)$$이고, 두 번째 화살표는 $$D \mapsto [D]$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$M \to \Div_T(X_\Sigma)$$가 injective임을 보인다. 만약 $$\div(\chi^m) = 0$$이라면 모든 $$\rho \in \Sigma(1)$$에 대해 $$\langle m, v_\rho \rangle = 0$$이다. Fan $$\Sigma$$가 $$N_\mathbb{R}$$를 span한다고 가정하면, primitive generator들 $$\{v_\rho\}$$가 $$N_\mathbb{R}$$를 span하므로 $$m = 0$$이다.

다음으로 $$\Div_T(X_\Sigma) \to \Cl(X_\Sigma)$$의 kernel이 principal divisor들의 image와 정확히 일치함을 보인다. 정의에 의해 kernel은 principal divisor들의 모임이며, toric variety 위에서는 임의의 principal divisor가 character의 divisor로부터 온다. 이는 $$T_N$$이 $$X_\Sigma$$의 열린 조밀한 부분집합이므로, $$X_\Sigma$$ 위의 rational function은 $$T_N$$ 위의 rational function으로 제한되며, $$T_N \cong (\mathbb{C}^\ast)^n$$ 위의 regular invertible function들은 정확히 character들 $$c \cdot \chi^m$$의 꼴을 갖기 때문이다.

마지막으로 surjectivity를 보인다. 임의의 Weil divisor class는 torus-invariant representative를 갖는다. 왜냐하면 $$T_N$$의 작용이 $$X_\Sigma$$를 이동시키므로, 임의의 divisor는 torus action을 취한 후 평균을 내어 torus-invariant divisor와 linearly equivalent하게 만들 수 있다. 따라서 $$\Div_T(X_\Sigma) \to \Cl(X_\Sigma)$$는 surjective이다.

</details>

이 exact sequence는 toric variety의 class group을 명시적으로 계산하는 강력한 도구가 된다. 특히 $$\Sigma(1)$$이 $$N_\mathbb{R}$$를 span할 때, $$\Cl(X_\Sigma) \cong \Div_T(X_\Sigma) / M$$이며 이는 $$\lvert \Sigma(1) \rvert - n$$의 rank를 갖는 free abelian group의 quotient로 주어진다.

## Cartier divisors와 support functions

Weil divisor 중에서도 더 좋은 성질을 갖는 것이 Cartier divisor이다. [\[대수다양체\] §인자, ⁋정의 3](/ko/math/algebraic_varieties/divisors#def3)에서 정의한 것처럼, Cartier divisor는 국소적으로 principal divisor로 주어지는 divisor이다. Toric variety의 경우 이 조합론적 조건은 support function이라는 개념으로 완전히 기술된다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Fan $$\Sigma$$의 *support* $$\lvert \Sigma \rvert = \bigcup_{\sigma \in \Sigma} \sigma$$ 위에 정의된 함수 $$\psi: \lvert \Sigma \rvert \to \mathbb{R}$$가 다음 조건을 만족할 때, 이를 **support function**이라 부른다: 각 cone $$\sigma \in \Sigma$$에 대해, $$\psi\rvert_\sigma$$는 어떤 $$m_\sigma \in M_\mathbb{R}$$에 의해 $$\psi(v) = \langle m_\sigma, v \rangle$$의 꼴로 주어진다. 즉 $$\psi$$는 각 cone 위에서 선형이다.

Support function $$\psi$$가 **integral**하다 함은 각 $$m_\sigma \in M$$일 때를 말한다.

</div>

각 torus-invariant Cartier divisor $$D$$는 하나의 integral support function $$\psi_D$$를 결정한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Torus-invariant Cartier divisor $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$에 대해, 다음과 같이 정의된 함수 $$\psi_D: \lvert \Sigma \rvert \to \mathbb{R}$$는 integral support function이다:

$$\psi_D(v_\rho) = -a_\rho \quad \text{for all } \rho \in \Sigma(1).$$

구체적으로, 각 maximal cone $$\sigma \in \Sigma$$에 대해 $$D\rvert_{U_\sigma}$$가 principal divisor $$\div(\chi^{-m_\sigma})$$로 주어질 때, $$\psi_D(v) = \langle m_\sigma, v \rangle$$ for $$v \in \sigma$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D$$가 Cartier divisor라고 가정하자. 정의에 의해 각 maximal cone $$\sigma$$에 대해 열린 집합 $$U_\sigma$$ 위에서 $$D$$는 어떤 rational function의 divisor로 주어진다. Torus-invariant성에 의해 이 rational function은 character $$\chi^{m_\sigma}$$의 꼴을 갖는다. 따라서 $$U_\sigma$$ 위에서

$$D\rvert_{U_\sigma} = \div(\chi^{-m_\sigma}) = \sum_{\rho \in \sigma(1)} \langle -m_\sigma, v_\rho \rangle D_\rho$$

이므로 $$a_\rho = \langle m_\sigma, v_\rho \rangle$$ for all $$\rho \in \sigma(1)$$이다. 이제 $$\psi_D(v) = \langle m_\sigma, v \rangle$$로 정의하면, 이는 $$\sigma$$ 위에서 선형이며 $$v_\rho$$에서는 원하는 값 $$-a_\rho$$를 갖는다. 두 cone $$\sigma_1, \sigma_2$$의 공통 face 위에서 정의된 $$m_{\sigma_1}$$과 $$m_{\sigma_2}$$가 동일한 값을 줌은 $$D$$가 well-defined한 divisor임으로부터 따라 나온다.

</details>

이 대응은 실제로 isomorphism을 이룬다. 즉 torus-invariant Cartier divisor의 group $$\CDiv_T(X_\Sigma)$$는 integral support function들의 group $$\SF(\Sigma)$$와 자연스럽게 동형이다.

## Line bundles와 global sections

이제 divisor가 정의하는 line bundle을 살펴본다. [\[대수다양체\] §선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_varieties/line_bundles#def1)에서 정의한 것처럼, 임의의 Weil divisor $$D$$에 대해 sheaf $$\mathcal{O}_{X_\Sigma}(D)$$를 정의할 수 있다. 이는 $$X_\Sigma$$ 위의 reflexive sheaf of rank one이며, $$D$$가 Cartier일 때에만 line bundle, 즉 invertible sheaf가 된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Weil divisor $$D$$에 대해, sheaf $$\mathcal{O}_{X_\Sigma}(D)$$는 다음과 같이 정의된다: 각 열린 집합 $$U \subseteq X_\Sigma$$에 대해

$$\mathcal{O}_{X_\Sigma}(D)(U) = \{f \in \mathbb{C}(X_\Sigma)^\times \mid \div(f)\rvert_U + D\rvert_U \ge 0\} \cup \{0\}.$$

</div>

Toric variety에서 이 sheaf의 global section은 특히 아름다운 형태를 갖는다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Torus-invariant Weil divisor $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$에 대해, sheaf $$\mathcal{O}_{X_\Sigma}(D)$$의 global section space는 다음과 같이 주어진다:

$$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = \bigoplus_{\substack{m \in M \\ \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho}} \mathbb{C} \cdot \chi^m.$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Torus action에 의해 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$는 weight space로 분해된다. 각 weight $$m \in M$$에 대해 character $$\chi^m$$가 section이 되기 위한 조건은 $$\div(\chi^m) + D \ge 0$$이다. 명제 3에 의해

$$\div(\chi^m) + D = \sum_{\rho \in \Sigma(1)} (\langle m, v_\rho \rangle + a_\rho) D_\rho$$

이므로, 이 divisor가 effective하기 위한 필요충분조건은 모든 $$\rho$$에 대해 $$\langle m, v_\rho \rangle + a_\rho \ge 0$$, 즉 $$\langle m, v_\rho \rangle \ge -a_\rho$$가 성립하는 것이다. 이러한 $$m \in M$$들에 해당하는 character $$\chi^m$$들이 basis를 이루며, 이들의 $$\mathbb{C}$$-linear span이 global section space를 이룬다.

</details>

이 결과는 toric variety 위의 line bundle의 global section이 lattice point들의 조합론적 조건으로 완전히 결정됨을 보여준다. 특히 $$D$$가 Cartier divisor일 때, 이 조건은 $$M_\mathbb{R}$$ 내의 polyhedron

$$\Delta_D = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

의 lattice points $$\Delta_D \cap M$$에 대응한다. 이 polyhedron은 bounded일 때 lattice polytope이 되며, 이는 normal fan의 구성에서 중요한 역할을 한다.

## Ample divisors와 strictly convex support functions

Line bundle의 가장 중요한 성질 중 하나는 ample함이다. [\[대수다양체\] §선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)에서 정의한 것처럼, line bundle이 ample하다는 것은 해당 divisor가 projective 임베딩을 유도한다는 것이다. Toric variety에서 이 기하학적 조건은 support function의 볼록성으로 완전히 기술된다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Support function $$\psi: \lvert \Sigma \rvert \to \mathbb{R}$$가 **strictly convex**하다 함은 다음 조건을 만족할 때를 말한다: 임의의 서로 다른 두 maximal cone $$\sigma_1, \sigma_2 \in \Sigma$$와 각각에 대응하는 $$m_{\sigma_1}, m_{\sigma_2} \in M_\mathbb{R}$$에 대해,

$$\psi(v) = \langle m_{\sigma_1}, v \rangle \text{ for } v \in \sigma_1, \qquad \psi(v) = \langle m_{\sigma_2}, v \rangle \text{ for } v \in \sigma_2$$

이고, $$\sigma_1 \cap \sigma_2$$의 상대 내부를 제외한 $$\sigma_1$$의 임의의 점 $$v$$에 대해

$$\psi(v) > \langle m_{\sigma_2}, v \rangle$$

이 성립하는 것이다. 즉 $$\psi$$는 각 maximal cone에서 자신의 linear extension보다 엄격하게 위에 있다.

</div>

Strictly convex support function은 fan의 구조를 완전히 결정하는 강력한 조건이다. 이는 다음 정리에서 ample divisor와의 정확한 대응을 제공한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Toric variety $$X_\Sigma$$가 complete일 때, torus-invariant Cartier divisor $$D$$가 ample인 것은 그에 대응하는 support function $$\psi_D$$가 strictly convex인 것과 필요충분조건이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($\Rightarrow$) $$D$$가 ample하다고 가정하자. 정의에 의해 어떤 $$k > 0$$에 대해 $$kD$$는 very ample이므로 projective 임베딩 $$\phi_{kD}: X_\Sigma \to \mathbb{P}^N$$을 유도한다. 이 임베딩은 monomial map으로 주어지며, 그 image는 lattice polytope $$\Delta_{kD}$$에 의해 결정된다. Very ample line bundle에 의한 projective 임베딩의 표준적인 성질에 의해, $$\Delta_{kD}$$의 normal fan이 정확히 $$\Sigma$$와 일치함을 알 수 있다. 이는 $$\psi_{kD} = k\psi_D$$가 strictly convex함을 의미하며, 따라서 $$\psi_D$$ 역시 strictly convex이다.

($\Leftarrow$) 반대로 $$\psi_D$$가 strictly convex라고 가정하자. 이는 $$\Sigma$$가 어떤 lattice polytope의 normal fan임을 의미한다. 구체적으로, strictly convexity에 의해

$$\Delta_D = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

은 bounded region이며 따라서 lattice polytope이다. 이 polytope의 normal fan이 $$\Sigma$$와 일치하므로, [§Normal fan과 projective toric variety, ⁋명제 9](/ko/math/toric_geometry/normal_fan_projective_toric#prop9)에 의해 $$X_\Sigma$$는 projective variety이다. 더 나아가 $$D$$에 대응하는 line bundle $$\mathcal{O}_{X_\Sigma}(D)$$가 very ample line bundle을 정의하므로 $$D$$는 ample이다.

</details>

이 명제는 toric variety의 projectivity criterion을 다시 한번 확인시켜 준다. [§Normal fan과 projective toric variety, ⁋명제 9](/ko/math/toric_geometry/normal_fan_projective_toric#prop9)에서 보았듯이, $$X_\Sigma$$가 projective인 것은 $$\Sigma$$가 어떤 lattice polytope의 normal fan인 것과 동치이다. 명제 10은 이 조합론적 조건이 support function의 strictly convexity로 재해석됨을 보여준다.

## 예시: 사영공간의 초평면 인자

가장 기본적인 예시로 projective space $$\mathbb{P}^n$$을 생각하자. [§Normal fan과 projective toric variety, ⁋예시 11](/ko/math/toric_geometry/normal_fan_projective_toric#ex11)에서 보았듯이, $$\mathbb{P}^n$$은 standard simplex $$\Delta_n$$의 normal fan $$\Sigma$$에 의해 정의되는 toric variety이다. Fan $$\Sigma$$는 원점을 중심으로 $$n+1$$개의 ray $$\rho_0, \rho_1, \ldots, \rho_n$$을 가지며, primitive generator는 $$v_0 = -e_1 - \cdots - e_n$$, $$v_1 = e_1$$, $$\ldots$$, $$v_n = e_n$$이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$\mathbb{P}^n$$ 위의 torus-invariant prime divisor $$D_i = D_{\rho_i}$$는 각 coordinate hyperplane $$\{z_i = 0\}$$에 대응한다. 특히

$$D_0 = \{z_0 = 0\}, \quad D_1 = \{z_1 = 0\}, \quad \ldots, \quad D_n = \{z_n = 0\}$$

이다. 이들의 선형 결합 $$H = D_1$$은 hyperplane divisor를 정의하며, 이는 $$\mathbb{P}^n$$ 위의 very ample divisor의 generator이다. 더 정확히는 $$\Pic(\mathbb{P}^n) \cong \mathbb{Z}$$이며, $$H$$가 이 group의 generator가 된다.

Support function $$\psi_H$$에 대응하는 $$m_\sigma$$들은 각 affine chart $$U_i = \{z_i \neq 0\} \cong \mathbb{A}^n$$ 위에서 $$H$$가 principal divisor $$\div(z_i/z_0)$$ 등으로 표현되는 방식에 의해 결정된다. Standard simplex의 구조에 의해 $$\psi_H$$는 strictly convex이며, 이는 $$H$$가 ample함을 재확인한다.

</div>

$$\mathbb{P}^n$$의 경우 principal divisor의 공식

$$\div(\chi^m) = \sum_{i=0}^n \langle m, v_i \rangle D_i$$

은 coordinate function들의 비에 대한 divisor를 계산할 때 나타난다. 예를 들어 $$m = e_1^\ast \in M$$에 대해 $$\chi^m(t) = t_1$$이고,

$$\div(t_1) = \langle e_1^\ast, v_0 \rangle D_0 + \langle e_1^\ast, v_1 \rangle D_1 = -D_0 + D_1$$

이므로 $$D_1 \sim D_0$$이다. 유사하게 모든 $$D_i$$는 서로 linearly equivalent하며, 이들이 정의하는 divisor class가 hyperplane class를 생성한다.

## Toric variety의 Picard group

마지막으로 toric variety의 Picard group을 기술한다. Picard group은 line bundle들의 isomorphism class들이 tensor product에 의해 형성하는 group이며, Cartier divisor의 linear equivalence class들의 group과 동형이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Toric variety $$X_\Sigma$$에 대해 다음이 성립한다:

1. Picard group $$\Pic(X_\Sigma)$$는 torus-invariant Cartier divisor들의 linear equivalence class들의 group $$\CDiv_T(X_\Sigma) / M$$과 동형이다.
2. $$X_\Sigma$$가 smooth이면 $$\Pic(X_\Sigma) \cong \Cl(X_\Sigma)$$이다.
3. 일반적으로 $$\Pic(X_\Sigma)$$는 $$\Cl(X_\Sigma)$$의 subgroup이며, 다음의 commutative diagram이 성립한다:

$$\begin{array}{ccccccccc}
0 & \longrightarrow & M & \longrightarrow & \CDiv_T(X_\Sigma) & \longrightarrow & \Pic(X_\Sigma) & \longrightarrow & 0 \\
  &                 & \downarrow &                 & \downarrow &                 & \downarrow &                 &   \\
0 & \longrightarrow & M & \longrightarrow & \Div_T(X_\Sigma) & \longrightarrow & \Cl(X_\Sigma) & \longrightarrow & 0
\end{array}$$

여기서 세로 화살표들은 inclusion을 나타낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) 일반적인 대수다양체에서 Cartier divisor의 group $$\CDiv(X)$$는 line bundle들의 group과 동형이며, principal divisor들로의 quotient가 Picard group을 준다. Toric variety에서 torus-invariant Cartier divisor만으로도 모든 linear equivalence class를 대표할 수 있으므로, $$\Pic(X_\Sigma) \cong \CDiv_T(X_\Sigma) / M$$이 성립한다.

(2) Smooth variety 위에서는 모든 Weil divisor가 Cartier divisor이므로, $$\Div(X_\Sigma) = \CDiv(X_\Sigma)$$이다. 따라서 $$\Cl(X_\Sigma) = \Pic(X_\Sigma)$$가 성립한다.

(3) 자연스러운 inclusion $$\CDiv_T(X_\Sigma) \hookrightarrow \Div_T(X_\Sigma)$$는 quotient에 의해 $$\Pic(X_\Sigma) \to \Cl(X_\Sigma)$$를 유도한다. 이 homomorphism은 injective이다. 왜냐하면 $$\CDiv_T(X_\Sigma) \cap M = M$$이고, $$\Pic(X_\Sigma) = \CDiv_T(X_\Sigma)/M$$, $$\Cl(X_\Sigma) = \Div_T(X_\Sigma)/M$$이므로 induced map의 kernel은 $$M/M = 0$$이다. 위의 commutative diagram은 자연스러운 inclusion으로부터 유도된다.

</details>

Toric variety의 Picard group은 support function의 언어로 명시적으로 기술될 수 있다. Integral support function들의 group $$\SF(\Sigma)$$에서 principal support function, 즉 전역적으로 하나의 $$m \in M$$에 의해 $$\psi(v) = \langle m, v \rangle$$로 주어지는 함수들을 quotient하면 Picard group을 얻는다. 이는 toric variety의 조합론적 불변량을 계산하는 강력한 방법을 제공한다.

특히 complete simplicial toric variety의 경우, Picard group은 free abelian group이며 그 rank는 $$\lvert \Sigma(1) \rvert - n$$이다. Nef cone과 ample cone 역시 support function의 공간 내에서 polyhedral cone으로 기술되며, 이는 toric variety의 birational geometry를 연구하는 데 필수적인 도구가 된다.

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
**[Oda]** Tadao Oda, *Convex Bodies and Algebraic Geometry*, Ergebnisse der Mathematik und ihrer Grenzgebiete, Springer, 1988.
