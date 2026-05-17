---
title: "토러스 인자와 선다발"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/toric_divisors

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Toric_Divisors_and_Line_Bundles.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-05-18
last_modified_at: 2026-05-18
weight: 3
published: false
---

이전 글에서 우리는 toric variety에 대해 살펴보았고, 이미 그 과정에서 torioc variety를 정의하는 fan의 조합론적인 데이터가 toric variety의 많은 성질을 결정함을 살펴보았다. 이번 글에서는 특히 toric variety 위에 정의된 (torus-invariant) divisor들을 살펴본다. 

## 토러스 불변 베유 인자

우리는 이미 toric variety $$X_\Sigma$$는 algebraic torus $$T_N \cong (\mathbb{C}^\ast)^n$$을 open dense subset으로 포함하는 것을 알고 있다. 그런데 이 위에서는 divisor가 자명한데, $$T_N$$의 coordinate ring을 생각해보면 이는 Laurent polynomial ring

$$\mathbb{C}[M] = \mathbb{C}[t_1^{\pm 1}, \ldots, t_n^{\pm 1}]$$

이므로 UFD이기 때문이다 ([\[환론\] §다항식환, ⁋정리 16](/ko/math/ring_theory/polynomial_rings#thm16)). UFD에서는 모든 height-1 prime ideal이 principal이므로 ([\[가환대수학\] §으뜸분해, ⁋정리 7](/ko/math/commutative_algebra/primary_decomposition#thm7)) 모든 codimension 1 irreducible subvariety가 단일 Laurent polynomial의 zero set이고, 따라서 모든 Weil divisor가 principal이 된다. 결과적으로 $$\Cl(T_N) = 0$$이 되므로 이 위에서는 divisor를 연구할 동기가 없다. 

바꿔말하면, $$X_\Sigma$$의 비자명한 divisor 정보는 모두 *boundary* $$X_\Sigma \setminus T_N$$에 모여 있는 셈이며, 이 boundary는 정확히 $$T_N$$의 작용에 의해 고정되는 part로 구성된다. 따라서 우리는 $$X_\Sigma$$ 위의 divisor 이론을 *torus-invariant* divisor들을 중심으로 전개하게 된다.

Fan $$\Sigma$$의 각 1차원 cone, 즉 *ray* $$\rho \in \Sigma(1)$$에 대해 primitive generator $$v_\rho \in N$$을 생각하자. Ray $$\rho$$는 $$X_\Sigma$$ 내의 codimension 1 torus orbit에 대응하며, 이의 Zariski closure가 하나의 irreducible divisor를 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 각 ray $$\rho \in \Sigma(1)$$에 대해, 대응하는 torus orbit의 Zariski closure를 $$D_\rho$$라 적는다. $$D_\rho$$는 $$X_\Sigma$$ 위의 irreducible Weil divisor이며, 이러한 $$D_\rho$$를 *torus-invariant prime divisor<sub>토러스 불변 소인자</sub>*라 부른다.

</div>

이 정의는 toric variety의 orbit 구조로부터 자연스럽게 유도된다. [§토릭 다양체의 정의, ⁋명제 5](/ko/math/toric_geometry/toric_varieties#prop5)에서 보았듯이, $$d$$-차원 cone은 차원 $$n-d$$의 torus orbit에 대응하므로 1차원 cone $$\rho$$는 차원 $$n-1$$의 orbit, 즉 codimension 1의 torus-invariant 부분다양체에 해당한다. 이 orbit의 Zariski closure는 자연스럽게 divisor가 된다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$X_\Sigma$$ 위의 torus-invariant Weil divisor들이 생성하는 free abelian group을 $$\Div_T(X_\Sigma)$$라 적는다. 즉,

$$\Div_T(X_\Sigma) = \bigoplus_{\rho \in \Sigma(1)} \mathbb{Z} \cdot D_\rho$$

이다. 임의의 torus-invariant Weil divisor는 $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$의 꼴로 유일하게 표현된다.

</div>

우리는 앞서 $$T_N$$의 divisor theory가 자명하다는 것을 살펴보았는데, 이를 사용하면 결국 toric variety에서 divisor를 보는 것은 torus-invariant divisor를 보는 것으로 충분하다는 것을 알 수 있다. 임의의 divisor $$D \in \Div(X_\Sigma)$$를 open dense subset $$T_N$$ 위로 제한하면 $$D \cap T_N$$은 $$T_N$$ 위의 divisor가 되는데, 여기서는 이것이 principal divisor $$\divisor(f)$$ 꼴이고, 따라서 $$D - \divisor(f)$$의 support는 boundary $$X_\Sigma \setminus T_N = \bigcup_{\rho \in \Sigma(1)} D_\rho$$ 안에 들어가게 되어 torus-invariant이기 때문이다. 이로부터 $$D$$는 어떤 torus-invariant divisor와 linearly equivalent하며, 더 형식적으로는 이를 통해 

$$\Div_T(X_\Sigma) \hookrightarrow \Div(X_\Sigma) \twoheadrightarrow \Cl(X_\Sigma)\tag{1}$$

이 surjective임을 확인할 수 있다. 즉, 본질적으로 $$\Div(X_\Sigma)$$ 대신 $$\Div_T(X_\Sigma)$$를 보는 것은 정보를 잃어버리는 종류의 trade-off가 아니다. 

## Principal divisors와 class group

우리의 궁극적 목표 중 하나는 $$\Cl(X_\Sigma)$$를 fan $$\Sigma$$의 조합론적 데이터로부터 명시적으로 계산하는 것이다. (1)이 surjection이므로 first isomorphism theorem에 의해 $$\Cl(X_\Sigma) \cong \Div_T(X_\Sigma) / \ker$$인데, $$\Div_T(X_\Sigma)$$는 이미 $$\bigoplus_{\rho \in \Sigma(1)} \mathbb{Z} D_\rho$$로 fan의 ray들이 결정하는 free abelian group으로 완전히 기술된다. 따라서 $$\Cl(X_\Sigma)$$를 알기 위해서는 (1)의 kernel을 fan의 데이터로 기술하는 일만 남는다.

정의에 의해 이 kernel은 $$\Div_T(X_\Sigma)$$의 원소 중 $$\Cl(X_\Sigma)$$에서 $$0$$이 되는 것들, 즉 *torus-invariant이면서 동시에 principal*한 divisor들의 모임이다. 그러므로 이는 결국 toric variety 위에서 어떤 rational function이 torus-invariant principal divisor를 정의하는지를 묻는 문제로 귀결된다.

그럼 가장 자연스러운 후보는 lattice $$M$$의 원소 $$m \in M$$에 대응하는 *character* $$\rchi^m$$이다. 각각의 $$m \in M$$에 대해, character $$\rchi^m: T_N \to \mathbb{C}^\ast$$는 $$T_N \subset X_\Sigma$$가 open dense이므로 $$X_\Sigma$$ 위의 유리함수로 볼 수 있다 ([§아핀 토릭 다양체, ⁋명제 8](/ko/math/toric_geometry/affine_toric_varieties#prop8)). 이 때,$$\rchi^m$$ 자체는 $$T_N$$의 작용 하에서 invariant하지 않지만, $$t \in T_N$$에 대해

$$(t \cdot \rchi^m)(x) = \rchi^m(t x) = \rchi^m(t) \cdot \rchi^m(x)$$

으로 ([§아핀 토릭 다양체, ⁋명제 8](/ko/math/toric_geometry/affine_toric_varieties#prop8)의 convention) 이들은 상수배만큼만 차이난다. 그런데 상수배는 zero와 pole을 변화시키지 않으므로, $$\rchi^m$$들 자체는 torus-invariant가 아니더라도 $$\divisor(\rchi^m)$$은 torus-invariant이고, $$\divisor(\rchi^m) \in \Div_T(X_\Sigma)$$이다. 우리의 첫 목표는 이 divisor를 fan의 데이터로 명시적으로 적는 것이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Character $$\rchi^m$$에 대응하는 principal divisor는 다음과 같이 주어진다.

$$\divisor(\rchi^m) = \sum_{\rho \in \Sigma(1)} \langle m, v_\rho \rangle D_\rho.$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X_\Sigma$$가 normal이므로 ([§토릭 다양체의 정의, ⁋명제 4](/ko/math/toric_geometry/toric_varieties#prop4)) 각 prime divisor $$D_\rho$$의 generic point에서의 local ring $$\mathcal{O}_{X_\Sigma, D_\rho}$$은 DVR이고, 이 위의 valuation을 $$v_{D_\rho}: \mathbb{C}(X_\Sigma)^\ast \to \mathbb{Z}$$로 적자. Principal divisor의 정의에 의해

$$\divisor(\rchi^m) = \sum_{\rho \in \Sigma(1)} v_{D_\rho}(\rchi^m) D_\rho$$

이므로 각 $$\rho \in \Sigma(1)$$에 대해 $$v_{D_\rho}(\rchi^m) = \langle m, v_\rho \rangle$$임을 보이면 충분하다. 이를 확인하기 위해 ray $$\rho$$에 해당하는 affine chart $$U_\rho = \Spec\mathbb{C}[\rho^\vee \cap M]$$를 생각한다. $$U_\rho$$ 위에서 $$D_\rho$$의 generic point에 대응하는 prime ideal은 $$\{u \in \rho^\vee \cap M : \langle u, v_\rho \rangle > 0\}$$이 생성하며, 이 prime에서 localize하면 character가 $$\rchi^u \mapsto \langle u, v_\rho \rangle$$로 매겨지는 DVR을 얻는다. 따라서 임의의 $$m \in M$$에 대해 $$v_{D_\rho}(\rchi^m) = \langle m, v_\rho \rangle$$이 성립한다.

</details>

이로부터 우리는 자연스러운 group homomorphism 

$$M \to \Div_T(X_\Sigma);\qquad m \mapsto \divisor(\rchi^m)$$

을 얻는다. 이 homomorphism의 image는 principal divisor들의 모임이며, 이것이 정확히 (1)의 kernel이라는 것이 우리의 주장이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Fan $$\Sigma$$의 ray들 $$\Sigma(1)$$이 $$N_\mathbb{R}$$를 span한다고 가정하자. 그러면 다음의 sequence는 exact하다:

$$0 \longrightarrow M \longrightarrow \Div_T(X_\Sigma) \longrightarrow \Cl(X_\Sigma) \longrightarrow 0.$$

여기서 첫 번째 화살표는 $$m \mapsto \divisor(\rchi^m)$$이고, 두 번째 화살표는 $$D \mapsto [D]$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$M \to \Div_T(X_\Sigma)$$가 injective임을 보인다. 만약 $$\divisor(\rchi^m) = 0$$이라면 모든 $$\rho \in \Sigma(1)$$에 대해 $$\langle m, v_\rho \rangle = 0$$이다. Fan $$\Sigma$$가 $$N_\mathbb{R}$$를 span한다고 가정하면, primitive generator들 $$\{v_\rho\}$$가 $$N_\mathbb{R}$$를 span하므로 $$m = 0$$이다.

다음으로 $$\Div_T(X_\Sigma) \to \Cl(X_\Sigma)$$의 kernel이 character들의 divisor들과 정확히 일치함을 보인다. 정의에 의해 kernel은 principal divisor이면서 동시에 $$T$$-invariant인 divisor들의 모임이다. $$D = \divisor(f)$$가 $$T$$-invariant라 하자. $$T$$-invariant divisor의 support는 boundary $$X_\Sigma \setminus T_N = \bigcup_{\rho \in \Sigma(1)} D_\rho$$에 들어가므로, $$f$$를 열린 조밀한 부분집합 $$T_N$$에 제한하면 $$\divisor(f \rvert_{T_N}) = 0$$이다. 따라서 $$f\rvert_{T_N}$$은 $$T_N$$의 좌표환 $$\mathbb{C}[M]$$의 unit이다. $$\mathbb{C}[M]$$의 unit은 정확히 $$c \cdot \rchi^m$$ ($$c \in \mathbb{C}^\ast$$, $$m \in M$$)의 꼴이므로, $$f\rvert_{T_N} = c \cdot \rchi^m$$이며 $$X_\Sigma$$의 정규성에 의해 $$f = c \cdot \rchi^m$$ on $$X_\Sigma$$이다. 그러므로 $$D = \divisor(\rchi^m)$$.

마지막으로 surjectivity를 보인다. 임의의 divisor $$D \in \Div(X_\Sigma)$$에 대해 $$T_N$$으로의 제한 $$D \cap T_N$$은 $$T_N \cong (\mathbb{C}^\ast)^n$$ 위의 divisor이다. $$T_N$$의 좌표환 $$\mathbb{C}[M]$$이 UFD이므로 이는 principal이며, 따라서 어떤 $$f \in \mathbb{C}(X_\Sigma)^\ast$$에 대해 $$D - \divisor(f)$$의 support가 $$X_\Sigma \setminus T_N = \bigcup_{\rho \in \Sigma(1)} D_\rho$$ 안에 들어가도록 할 수 있다. 우변은 torus-invariant divisor의 합으로 표현되므로, $$[D] = [D - \divisor(f)]$$는 torus-invariant representative를 갖는다.

</details>

이 exact sequence는 toric variety의 class group을 명시적으로 계산하는 강력한 도구가 된다. 가정 하에서 $$\Div_T(X_\Sigma) \cong \mathbb{Z}^{\Sigma(1)}$$은 rank $$\lvert \Sigma(1) \rvert$$의 free abelian group이고 $$M \cong \mathbb{Z}^n$$는 rank $$n$$의 free abelian group으로 그 안에 embed되므로, $$\Cl(X_\Sigma) \cong \mathbb{Z}^{\Sigma(1)} / M$$은 rank $$\lvert \Sigma(1) \rvert - n$$의 finitely generated abelian group이다. 다만 일반적으로 torsion을 가질 수 있다는 점을 주의하자—예컨대 $$\mathbb{P}(1,1,2)$$에서는 $$\Cl \cong \mathbb{Z} \oplus \mathbb{Z}/2$$이다.

## Cartier divisor

한편, divisor를 통해 line bundle의 이야기를 하기 위해서는 Cartier divisor를 살펴보아야 한다. 우리는 위에서 Weil divisor를 살펴보았고, smooth case에서는 Weil divisor와 Cartier divisor가 서로 같으므로 부분적으로 이는 완료되었지만, toric variety에서는 (smooth하지 않더라도) Cartier divisor를 기술하는 방법이 존재한다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Fan $$\Sigma$$의 *support* $$\lvert \Sigma \rvert = \bigcup_{\sigma \in \Sigma} \sigma$$ 위에 정의된 함수 $$\psi: \lvert \Sigma \rvert \to \mathbb{R}$$가 *piecewise linear function<sub>조각별 선형 함수</sub>*이라는 것은, 각각의 cone $$\sigma \in \Sigma$$에 대해 $$\psi\rvert_\sigma$$는 어떤 $$m_\sigma \in M_\mathbb{R}$$에 의해 $$\psi(v) = \langle m_\sigma, v \rangle$$의 꼴로 나타나는 것이다. Piecewise linear function $$\psi$$가 *integral<sub>정수형</sub>*이라는 것은 각각의 $$m_\sigma$$이 $$M$$에 속하는 것이다

</div>

Piecewise linear function들의 모임을 $$\PL(\Sigma, M_\mathbb{R})$$, 

이 글에서 등장하는 piecewise linear function들의 group을 다음과 같이 적기로 한다:

$$\PL(\Sigma, M) = \{\text{integral piecewise linear functions on } \lvert \Sigma \rvert\}, \qquad \PL(\Sigma, M_\mathbb{R}) = \{\text{piecewise linear functions on } \lvert \Sigma \rvert\}.$$

즉 두 번째 자리에 lattice $$M$$이 오면 *integral*함을 의미하고, $$M_\mathbb{R}$$이 오면 일반 (실수 계수) piecewise linear function들의 $$\mathbb{R}$$-vector space를 의미한다. 이하 본문에서 단순히 $$\PL(\Sigma, M)$$이라 적을 때는 integral인 것을 뜻하므로 별도의 형용사를 붙이지 않는다.

각 torus-invariant Cartier divisor $$D$$는 하나의 $$\psi_D \in \PL(\Sigma, M)$$을 결정한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Torus-invariant Cartier divisor $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$에 대해, 다음과 같이 정의된 함수 $$\psi_D: \lvert \Sigma \rvert \to \mathbb{R}$$는 $$\PL(\Sigma, M)$$의 원소이다:

$$\psi_D(v_\rho) = -a_\rho \quad \text{for all } \rho \in \Sigma(1).$$

구체적으로, 각 maximal cone $$\sigma \in \Sigma$$에 대해 $$D\rvert_{U_\sigma}$$가 principal divisor $$\divisor(\rchi^{-m_\sigma})$$로 주어질 때, $$\psi_D(v) = \langle m_\sigma, v \rangle$$ for $$v \in \sigma$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$D$$가 Cartier divisor라고 가정하자. 정의에 의해 각 maximal cone $$\sigma$$에 대해 열린 집합 $$U_\sigma$$ 위에서 $$D$$는 어떤 rational function의 divisor로 주어진다. Torus-invariant성에 의해 이 rational function은 character $$\rchi^{m_\sigma}$$의 꼴을 갖는다. 따라서 $$U_\sigma$$ 위에서

$$D\rvert_{U_\sigma} = \divisor(\rchi^{-m_\sigma}) = \sum_{\rho \in \sigma(1)} \langle -m_\sigma, v_\rho \rangle D_\rho$$

이므로 $$a_\rho = -\langle m_\sigma, v_\rho \rangle$$ for all $$\rho \in \sigma(1)$$이다. 이제 $$\psi_D(v) = \langle m_\sigma, v \rangle$$로 정의하면, 이는 $$\sigma$$ 위에서 선형이며 $$v_\rho$$에서는 원하는 값 $$-a_\rho$$를 갖는다. 두 maximal cone $$\sigma_1, \sigma_2$$의 공통 face $$\tau = \sigma_1 \cap \sigma_2$$ 위에서 $$\psi_D$$가 well-defined하려면 $$\langle m_{\sigma_1}, v\rangle = \langle m_{\sigma_2}, v\rangle$$ ($$v \in \tau$$)이 성립해야 하는데, 이는 $$U_\tau$$ 위에서 $$\rchi^{m_{\sigma_2} - m_{\sigma_1}}$$이 regular invertible function 즉 character $$\rchi^{m}$$ ($$m \in \tau^\perp \cap M$$)가 되어야 한다는 사실로부터 따라 나온다.

</details>

이 대응은 실제로 isomorphism을 이룬다. 즉 torus-invariant Cartier divisor의 group $$\CaDiv_T(X_\Sigma)$$는 $$\PL(\Sigma, M)$$과 자연스럽게 동형이다.

## Line bundles와 global sections

이제 divisor가 정의하는 line bundle을 살펴본다. [\[대수다양체\] §선다발과 벡터다발, ⁋정의 1](/ko/math/algebraic_varieties/line_bundles#def1)에서 정의한 것처럼, 임의의 Weil divisor $$D$$에 대해 sheaf $$\mathcal{O}_{X_\Sigma}(D)$$를 정의할 수 있다. 이는 $$X_\Sigma$$ 위의 reflexive sheaf of rank one이며, $$D$$가 Cartier일 때에만 line bundle, 즉 invertible sheaf가 된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Weil divisor $$D$$에 대해, sheaf $$\mathcal{O}_{X_\Sigma}(D)$$는 다음과 같이 정의된다: 각 열린 집합 $$U \subseteq X_\Sigma$$에 대해

$$\mathcal{O}_{X_\Sigma}(D)(U) = \{f \in \mathbb{C}(X_\Sigma)^\times \mid \divisor(f)\rvert_U + D\rvert_U \ge 0\} \cup \{0\}.$$

</div>

Toric variety에서 이 sheaf의 global section은 특히 아름다운 형태를 갖는다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Torus-invariant Weil divisor $$D = \sum_{\rho \in \Sigma(1)} a_\rho D_\rho$$에 대해, sheaf $$\mathcal{O}_{X_\Sigma}(D)$$의 global section space는 다음과 같이 주어진다:

$$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D)) = \bigoplus_{\substack{m \in M \\ \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho}} \mathbb{C} \cdot \rchi^m.$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Torus action에 의해 $$H^0(X_\Sigma, \mathcal{O}_{X_\Sigma}(D))$$는 weight space로 분해된다. 각 weight $$m \in M$$에 대해 character $$\rchi^m$$가 section이 되기 위한 조건은 $$\divisor(\rchi^m) + D \ge 0$$이다. 명제 3에 의해

$$\divisor(\rchi^m) + D = \sum_{\rho \in \Sigma(1)} (\langle m, v_\rho \rangle + a_\rho) D_\rho$$

이므로, 이 divisor가 effective하기 위한 필요충분조건은 모든 $$\rho$$에 대해 $$\langle m, v_\rho \rangle + a_\rho \ge 0$$, 즉 $$\langle m, v_\rho \rangle \ge -a_\rho$$가 성립하는 것이다. 이러한 $$m \in M$$들에 해당하는 character $$\rchi^m$$들이 basis를 이루며, 이들의 $$\mathbb{C}$$-linear span이 global section space를 이룬다.

</details>

이 결과는 toric variety 위의 line bundle의 global section이 lattice point들의 조합론적 조건으로 완전히 결정됨을 보여준다. 특히 $$D$$가 Cartier divisor일 때, 이 조건은 $$M_\mathbb{R}$$ 내의 polyhedron

$$\Delta_D = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

의 lattice points $$\Delta_D \cap M$$에 대응한다. 이 polyhedron은 bounded일 때 lattice polytope이 되며, 이는 normal fan의 구성에서 중요한 역할을 한다.

## Ample divisors와 strictly convex piecewise linear functions

Line bundle의 가장 중요한 성질 중 하나는 ample함이다. [\[대수다양체\] §선형계, ⁋정의 10](/ko/math/algebraic_varieties/linear_systems#def10)에서 정의한 것처럼, line bundle이 ample하다는 것은 해당 divisor가 projective 임베딩을 유도한다는 것이다. Toric variety에서 이 기하학적 조건은 piecewise linear function의 볼록성으로 완전히 기술된다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Piecewise linear function $$\psi: \lvert \Sigma \rvert \to \mathbb{R}$$가 *strictly convex<sub>엄격볼록</sub>*하다 함은 다음 조건을 만족할 때를 말한다: 임의의 서로 다른 두 maximal cone $$\sigma_1, \sigma_2 \in \Sigma$$와 각각에 대응하는 $$m_{\sigma_1}, m_{\sigma_2} \in M_\mathbb{R}$$에 대해,

$$\psi(v) = \langle m_{\sigma_1}, v \rangle \text{ for } v \in \sigma_1, \qquad \psi(v) = \langle m_{\sigma_2}, v \rangle \text{ for } v \in \sigma_2$$

이고, $$\sigma_1 \cap \sigma_2$$의 상대 내부를 제외한 $$\sigma_1$$의 임의의 점 $$v$$에 대해

$$\psi(v) > \langle m_{\sigma_2}, v \rangle$$

이 성립하는 것이다. 즉 $$\psi$$는 각 maximal cone에서 자신의 linear extension보다 엄격하게 위에 있다.

</div>

Strictly convex piecewise linear function은 fan의 구조를 완전히 결정하는 강력한 조건이다. 이는 다음 정리에서 ample divisor와의 정확한 대응을 제공한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Toric variety $$X_\Sigma$$가 complete일 때, torus-invariant Cartier divisor $$D$$가 ample인 것은 그에 대응하는 piecewise linear function $$\psi_D$$가 strictly convex인 것과 필요충분조건이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($$\Rightarrow$$) $$D$$가 ample하다고 가정하자. 정의에 의해 어떤 $$k > 0$$에 대해 $$kD$$는 very ample이므로 projective 임베딩 $$\phi_{kD}: X_\Sigma \hookrightarrow \mathbb{P}^N$$을 유도하며, 이 임베딩은 polytope $$\Delta_{kD} \cap M$$의 lattice points로 정의되는 monomial map과 일치한다 ([§토릭 다양체의 정의, ⁋명제 9](/ko/math/toric_geometry/toric_varieties#prop9)). $$X_\Sigma$$가 complete이므로 image $$\overline{\phi_{kD}(T_N)}$$는 $$\Delta_{kD}$$의 normal fan으로부터 얻어지는 projective toric variety와 동형이며 ([CLS] Theorem 6.2.1 참고), $$X_\Sigma$$와의 동형으로부터 $$\Delta_{kD}$$의 normal fan이 $$\Sigma$$와 일치함을 얻는다. 이는 $$\psi_{kD} = k\psi_D$$가 strictly convex함을 의미하며, 따라서 $$\psi_D$$ 역시 strictly convex이다.

($$\Leftarrow$$) 반대로 $$\psi_D$$가 strictly convex라고 가정하자. 이는 $$\Sigma$$가 어떤 lattice polytope의 normal fan임을 의미한다. 구체적으로, strictly convexity에 의해

$$\Delta_D = \{m \in M_\mathbb{R} \mid \langle m, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

은 bounded region이며 따라서 lattice polytope이다. 이 polytope의 normal fan이 $$\Sigma$$와 일치하므로, [§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)에 의해 $$X_\Sigma$$는 projective variety이다. 더 나아가 $$D$$에 대응하는 line bundle $$\mathcal{O}_{X_\Sigma}(D)$$가 very ample line bundle을 정의하므로 $$D$$는 ample이다.

</details>

이 명제는 toric variety의 projectivity criterion을 다시 한번 확인시켜 준다. [§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)에서 보았듯이, $$X_\Sigma$$가 projective인 것은 $$\Sigma$$가 어떤 lattice polytope의 normal fan인 것과 동치이다. 명제 10은 이 조합론적 조건이 piecewise linear function의 strictly convexity로 재해석됨을 보여준다.

## Toric variety의 Picard group

마지막으로 toric variety의 Picard group을 기술한다. Picard group은 line bundle들의 isomorphism class들이 tensor product에 의해 형성하는 group이며, Cartier divisor의 linear equivalence class들의 group과 동형이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Toric variety $$X_\Sigma$$에 대해 다음이 성립한다:

1. Picard group $$\Pic(X_\Sigma)$$는 torus-invariant Cartier divisor들의 linear equivalence class들의 group $$\CaDiv_T(X_\Sigma) / M$$과 동형이다.
2. $$X_\Sigma$$가 smooth이면 $$\Pic(X_\Sigma) \cong \Cl(X_\Sigma)$$이다.
3. 일반적으로 $$\Pic(X_\Sigma)$$는 $$\Cl(X_\Sigma)$$의 subgroup이며, 다음의 commutative diagram이 성립한다:

$$\begin{array}{ccccccccc}
0 & \longrightarrow & M & \longrightarrow & \CaDiv_T(X_\Sigma) & \longrightarrow & \Pic(X_\Sigma) & \longrightarrow & 0 \\
  &                 & \downarrow &                 & \downarrow &                 & \downarrow &                 &   \\
0 & \longrightarrow & M & \longrightarrow & \Div_T(X_\Sigma) & \longrightarrow & \Cl(X_\Sigma) & \longrightarrow & 0
\end{array}$$

여기서 세로 화살표들은 inclusion을 나타낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) 일반적인 대수다양체에서 Cartier divisor의 group $$\CaDiv(X)$$는 line bundle들의 group과 동형이며, principal divisor들로의 quotient가 Picard group을 준다. Toric variety에서 torus-invariant Cartier divisor만으로도 모든 linear equivalence class를 대표할 수 있으므로, $$\Pic(X_\Sigma) \cong \CaDiv_T(X_\Sigma) / M$$이 성립한다.

(2) Smooth variety 위에서는 모든 Weil divisor가 Cartier divisor이므로, $$\Div(X_\Sigma) = \CaDiv(X_\Sigma)$$이다. 따라서 $$\Cl(X_\Sigma) = \Pic(X_\Sigma)$$가 성립한다.

(3) $$M \to \Div_T(X_\Sigma)$$의 image $$\divisor(\rchi^m)$$은 principal divisor이므로 자동으로 Cartier이며, 따라서 이 화살표는 $$M \to \CaDiv_T(X_\Sigma)$$로 factor된다. 결과적으로 commutative diagram의 좌측 두 column은 동일한 $$M$$이고, quotient $$\Pic(X_\Sigma) = \CaDiv_T(X_\Sigma)/M$$이 $$\Cl(X_\Sigma) = \Div_T(X_\Sigma)/M$$의 부분군으로 자연스럽게 들어간다. Injectivity는 $$\CaDiv_T(X_\Sigma) \hookrightarrow \Div_T(X_\Sigma)$$가 injective이고 두 quotient가 동일한 $$M$$의 image로 나눈 것이라는 사실로부터 따라 나온다.

</details>

Toric variety의 Picard group은 piecewise linear function의 언어로 명시적으로 기술될 수 있다. $$\PL(\Sigma, M)$$에서 globally linear한 것들, 즉 전역적으로 하나의 $$m \in M$$에 의해 $$\psi(v) = \langle m, v \rangle$$로 주어지는 함수들을 quotient하면 Picard group을 얻는다. 이는 toric variety의 조합론적 불변량을 계산하는 강력한 방법을 제공한다.

특히 complete simplicial toric variety의 경우, Picard group은 free abelian group이며 그 rank는 $$\lvert \Sigma(1) \rvert - n$$이다. Nef cone과 ample cone 역시 piecewise linear function의 공간 내에서 polyhedral cone으로 기술되며, 이는 toric variety의 birational geometry를 연구하는 데 필수적인 도구가 된다.

## 예시: 사영공간의 초평면 인자

지금까지 정리한 도구들 — torus-invariant divisor, piecewise linear function, ample criterion, Picard group의 조합론적 기술 — 을 가장 익숙한 toric variety인 projective space $$\mathbb{P}^n$$에 적용해 보자. [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)에서 보았듯이, $$\mathbb{P}^n$$은 standard simplex $$\Delta_n$$의 normal fan $$\Sigma$$에 의해 정의되는 toric variety이다. Fan $$\Sigma$$는 원점을 중심으로 $$n+1$$개의 ray $$\rho_0, \rho_1, \ldots, \rho_n$$을 가지며, primitive generator는 $$v_0 = -e_1 - \cdots - e_n$$, $$v_1 = e_1$$, $$\ldots$$, $$v_n = e_n$$이다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$\mathbb{P}^n$$ 위의 torus-invariant prime divisor $$D_i = D_{\rho_i}$$는 각 coordinate hyperplane $$\{z_i = 0\}$$에 대응한다. 특히

$$D_0 = \{z_0 = 0\}, \quad D_1 = \{z_1 = 0\}, \quad \ldots, \quad D_n = \{z_n = 0\}$$

이다. 이들의 선형 결합 $$H = D_1$$은 hyperplane divisor를 정의하며, 이는 $$\mathbb{P}^n$$ 위의 very ample divisor의 generator이다.

Piecewise linear function $$\psi_H$$에 대응하는 $$m_\sigma$$들은 각 affine chart $$U_i = \{z_i \neq 0\} \cong \mathbb{A}^n$$ 위에서 $$H$$가 principal divisor $$\divisor(z_i/z_0)$$ 등으로 표현되는 방식에 의해 결정된다. Standard simplex의 구조에 의해 $$\psi_H$$는 strictly convex이며, 이는 $$H$$가 ample함을 재확인한다 ([명제 10](#prop10)).

</div>

$$\mathbb{P}^n$$의 경우 principal divisor의 공식

$$\divisor(\rchi^m) = \sum_{i=0}^n \langle m, v_i \rangle D_i$$

은 coordinate function들의 비에 대한 divisor를 계산할 때 나타난다. 예를 들어 $$m = e_1^\ast \in M$$에 대해 $$\rchi^m(t) = t_1$$이고,

$$\divisor(t_1) = \langle e_1^\ast, v_0 \rangle D_0 + \langle e_1^\ast, v_1 \rangle D_1 = -D_0 + D_1$$

이므로 $$D_1 \sim D_0$$이다. 유사하게 모든 $$D_i$$는 서로 linearly equivalent하다. $$\mathbb{P}^n$$이 smooth이므로 [명제 11](#prop11) (2)에 의해 $$\Pic(\mathbb{P}^n) \cong \Cl(\mathbb{P}^n) = \Div_T(\mathbb{P}^n)/M$$이며, 우변은 rank $$n+1$$인 free abelian group $$\bigoplus_{i=0}^n \mathbb{Z} D_i$$를 rank $$n$$인 $$M$$의 image (즉 $$D_i \sim D_0$$ 관계들)로 quotient한 것이므로 $$\mathbb{Z}$$와 동형이고, $$H = D_0$$가 그 generator가 된다.

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
**[Oda]** Tadao Oda, *Convex Bodies and Algebraic Geometry*, Ergebnisse der Mathematik und ihrer Grenzgebiete, Springer, 1988.
