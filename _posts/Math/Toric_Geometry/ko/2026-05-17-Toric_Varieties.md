---
title: "토릭 다양체의 정의"
description: "강체 볼록 다리뿔뿔 cone에 대응하는 affine 토릭 다양체를 공유하는 face를 통해 붙여 일반적인 토릭 다양체를 구성하는 과정을 다룬다. 조합론적 구조인 fan의 정의와 성질을 함께 살펴본다."
excerpt: "Fan으로부터 아핀 토릭 다양체들을 이어붙여 얻는 일반적 토릭 다양체"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/toric_varieties

sidebar:
    nav: "toric_geometry-ko"

date: 2026-05-17
weight: 2

---

[§아핀 토릭 다양체, ⁋정의 5](/ko/math/toric_geometry/affine_toric_varieties#def5)에서 정의한 affine toric variety는 하나의 strongly convex rational polyhedral cone $$\tau$$에 대응하는 대수다양체 $$U_\tau$$이다. 이는 [§아핀 토릭 다양체, ⁋예시 14](/ko/math/toric_geometry/affine_toric_varieties#ex14)에서 살펴봤듯, torus action 구조를 가지고 있는 algebraic variety인 것으로 생각할 수 있으며 그 정의에 의해 적당한 ring의 $$\Spec$$이므로 affine variety이다. 

이번 글에서 우리는 affine toric variety들을 붙여 일반적인 toric variety를 얻어내는 과정을 살펴볼 것이다. 구체적으로, 우리는 cone $$\sigma$$의 face $$\tau$$에 해당하는 affine toric variety $$U_\tau$$가 $$U_\sigma$$의 principal open set인 것을 보았는데 ([§아핀 토릭 다양체, ⁋명제 13](/ko/math/toric_geometry/affine_toric_varieties#prop13)), 바꿔말하면 두 cone이 하나의 face를 공유한다면 이는 각각의 cone이 정의하는 affine toric variety들로의 inclusion 또한 정의할 것이고, 따라서 이를 통해 gluing을 해 줄 수 있게 된다.

## Fan의 정의

위와 같이 affine toric variety들을 이어붙이기 위해서는 각각의 cone들이 서로 어떻게 만나는지를 제어하는 조합론적인 구조가 필요하다. 이를 위해 우리는 *fan*을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lattice $$N$$에 대해, $$N_\mathbb{R}$$에 정의된 *fan* $$\Sigma$$는 다음 조건을 만족하는 strongly convex rational polyhedral cone들의 모임이다:

1. $$\Sigma$$에 속하는 임의의 cone $$\tau$$의 face도 $$\Sigma$$에 속한다.
2. $$\Sigma$$에 속하는 임의의 두 cone $$\tau_1, \tau_2$$의 교집합 $$\tau_1 \cap \tau_2$$는 각각의 face이다.

</div>

둘째 조건은 [정의 3](#def3)에서 위의 과정을 통해 gluing을 할 때 필요한 것으로, 서로 다른 두 cone $$\tau_1, \tau_2$$가 그들의 공통 face에서만 만나도록 강제해준다. 한편 첫 번째 조건은 fan이 각 cone의 모든 면을 포함하므로, 일종의 closedness를 요구하는 것으로 볼 수 있다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$N = \mathbb{Z}^2$$에서 원점을 중심으로 방사형으로 세 개의 2차원 cone $$\tau_0, \tau_1, \tau_2$$가 $$\mathbb{R}^2$$를 덮는 fan을 생각할 수 있다. 가령 세 개의 벡터 $$e_1, e_2, -e_1-e_2$$를 생각한 후, 이들이 만드는 세 개의 cone을 생각하자.

![$$\mathbb{P}^2$$의 fan](/assets/images/Math/Toric_Geometry/Toric_Varieties-1.svg){:style="width:20em" class="invert" .align-center}

각각의 cone은 두 개의 반직선 원소 $$\rho_i, \rho_{i+1}$$에 의해 생성되며, 이러한 반직선들은 1차원 cone들이 된다. 원점 $$\{0\}$$ 자체는 0차원 cone으로서 모든 fan에 포함된다. 이 fan은 $$\mathbb{P}^2$$의 toric variety를 정의하는 가장 기본적인 예시이다.

</div>

## 토릭 다양체의 정의

이제 우리는 fan $$\Sigma$$가 주어졌을 때 이로부터 algebraic variety $$X_\Sigma$$를 정의할 수 있다. 사실 이를 위한 기본적인 도구는 이미 전부 설명했던 것이며, 오직 [정의 1](#def1)의 언어만이 추가로 필요했던 것이다. 이를 만드는 흐름을 명확한 수학적 언어로 정리하자면, fan $$\Sigma$$가 주어졌다 하고, 각각의 cone $$\tau \in \Sigma$$에 대하여 [§아핀 토릭 다양체, ⁋정의 5](/ko/math/toric_geometry/affine_toric_varieties#def5)에 의해 affine toric variety $$U_\tau$$를 얻는다. 이 때, 두 cone $$\tau_1, \tau_2 \in \Sigma$$가 공통 face $$\tau_1 \cap \tau_2$$를 가질 때, [§아핀 토릭 다양체, ⁋명제 13](/ko/math/toric_geometry/affine_toric_varieties#prop13)에 의해 $$U_{\tau_1 \cap \tau_2}$$는 $$U_{\tau_1}$$과 $$U_{\tau_2}$$ 모두의 principal open subset이 되며, 따라서 이들 사이의 isomorphism, inclusion

$$U_{\tau_1} \supset U_{\tau_1 \cap \tau_2} \cong U_{\tau_2 \cap \tau_1} \subset U_{\tau_2}$$

이 존재하며, 이를 통해 $$U_\tau$$들을 이어붙일 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Fan $$\Sigma$$에 대하여, affine toric variety들 $$\{U_\tau\}_{\tau \in \Sigma}$$를 위에서 기술한 방식으로 이어붙여 얻어지는 algebraic variety를 $$\Sigma$$가 정의하는 *toric variety<sub>토릭 다양체</sub>*라 하며, $$X_\Sigma$$로 적는다.

</div>

그럼 다음은 [§아핀 토릭 다양체, ⁋명제 15](/ko/math/toric_geometry/affine_toric_varieties#prop15)을 일반화하는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Toric variety $$X_\Sigma$$는 normal, separated algebraic variety이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$X_\Sigma$$의 normality는 각 affine chart $$U_\tau$$가 [§아핀 토릭 다양체, ⁋명제 15](/ko/math/toric_geometry/affine_toric_varieties#prop15)에 의해 normal이고, 이 성질이 gluing에 의해 보존되기 때문에 얻어진다. Separatedness를 보이기 위해서는 diagonal morphism $$\Delta: X_\Sigma \to X_\Sigma \times X_\Sigma$$의 image가 닫힌 집합임을 확인하면 된다. 각 affine chart 위에서 이는 두 cone의 교집합이 face임을 보장하는 fan의 두 번째 조건에 의해 성립한다. 

</details>

Toric variety $$X_\Sigma$$가 affine toric variety로부터 물려받는 중요한 성질 중 하나는 algebraic torus $$T_N$$을 열린 조밀한 부분집합으로 포함한다는 것이다. ([§아핀 토릭 다양체, ⁋명제 11](/ko/math/toric_geometry/affine_toric_varieties#prop11)) 실제로, 0차원 cone $$\{0\} \in \Sigma$$에 대응하는 affine chart $$U_{\{0\}}$$는 $$T_N$$과 동형이며, 다른 모든 $$U_\tau$$는 이를 열린 부분집합으로 포함한다. 따라서 $$T_N \subset X_\Sigma$$는 open dense embedding을 정의한다.

[§아핀 토릭 다양체, ⁋명제 10](/ko/math/toric_geometry/affine_toric_varieties#prop10)에서 보았듯이, 각 affine toric variety $$U_\tau$$ 위에는 algebraic torus $$T_N$$의 작용이 자연스럽게 정의된다. 우리는 해당 글에서, cone의 inclusion이 유도하는 affine toric variety들 사이의 inclusion이 torus action에 대해 invariant하다는 것을 살펴보았으므로, 이 작용은 gluing을 통해 $$X_\Sigma$$ 전체로 확장된다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 fan $$\Sigma$$에 대하여 toric variety $$X_\Sigma$$ 위에는 algebraic torus $$T_N$$의 작용이 자연스럽게 정의된다. 이 작용 하에서 $$T_N \subset X_\Sigma$$는 open dense $$T_N$$-invariant subset이며, 이 위에서 정의된 $$T_N$$의 자기 자신 위의 action이 $$X_\Sigma$$ 위의 작용으로 확장된다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각각의 cone $$\tau \in \Sigma$$에 대해, $$U_\tau$$ 위의 $$T_N$$-action은 [§아핀 토릭 다양체, ⁋명제 10](/ko/math/toric_geometry/affine_toric_varieties#prop10)에 의해 정의된다. 두 affine chart $$U_{\tau_1}$$과 $$U_{\tau_2}$$의 교집합 $$U_{\tau_1 \cap \tau_2}$$ 위에서 이들 작용은 일치하므로, 이들은 $$X_\Sigma$$ 전체에서 well-defined한 $$T_N$$-action을 정의한다. 한편 $$\{0\} \in \Sigma$$에 대응하는 chart $$U_{\{0\}} \cong T_N$$은 열린 조밀한 부분집합이며, $$T_N$$의 자기작용은 이 chart 위에서 left multiplication으로 주어지므로 $$X_\Sigma$$ 위의 작용으로 자연스럽게 확장된다. 

</details>

만일 fan $$\Sigma$$가 $$\bigcup_{\tau \in \Sigma} \tau = N_\mathbb{R}$$을 만족한다면 우리는 이를 *complete<sub>완전</sub>* fan이라 부른다. 이 경우 $$X_\Sigma$$는 *complete<sub>완비</sub>* algebraic variety, 즉 $$\Spec(\mathbb{C})$$ 위에서 proper한 variety가 됨이 알려져 있다. Completeness는 대수기하에서 compactness에 대응하는 개념이므로, 우리는 이 경우 $$X_\Sigma$$를 $$T_N$$의 *equivariant compactification*이라 부른다.

이 작용에 의한 orbit들의 구조는 fan의 조합론과 밀접하게 연관된다. 구체적으로, $$d$$-차원 cone $$\tau \in \Sigma$$에 대응하는 orbit $$O(\tau)$$는 차원 $$n-d$$의 torus $$(\mathbb{C}^\ast)^{n-d}$$와 isomorphic하며, 특히 $$n$$-차원 cone, 즉 maximal cone에 대응하는 orbit는 0차원, 즉 $$T_N$$-action의 fixed point가 된다.

## Normal fan과 projective toric variety

지금까지는 임의의 fan $$\Sigma$$로부터 toric variety $$X_\Sigma$$를 구성하는 방법을 살펴보았다. 이제 우리는 특별한 종류의 fan, 즉 polytope으로부터 자연스럽게 얻어지는 *normal fan*에 대해 논의한다. 이는 projective toric variety를 만드는 핵심적인 방법이다.

Lattice $$M$$의 dual lattice가 $$N$$이고, $$M_\mathbb{R}$$의 full-dimensional convex lattice polytope $$P$$를 생각하자. $$P$$의 각 facet $$F^\prime$$에 대하여, $$F^\prime$$이 결정하는 hyperplane에 수직이고 polytope $$P$$의 내부를 향하는 $$N$$의 원소들 중, $$v = k v^\prime$$ ($$k > 1$$ 정수, $$v^\prime \in N$$) 꼴로 분해되지 않는 유일한 lattice vector를 $$F^\prime$$의 *primitive inner normal vector* $$u_{F^\prime} \in N$$이라 부른다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Polytope $$P$$의 *normal fan* $$\Sigma_P$$는, $$P$$의 각 면 $$F$$에 대해 $$F$$를 포함하는 모든 facet $$F^\prime$$의 primitive inner normal vector $$u_{F^\prime}$$들이 생성하는 cone $$\tau_F$$를 모은 것

$$\Sigma_P = \{\tau_F \mid F \text{ is a face of } P\}$$

으로 정의된다.

</div>

우리의 첫 번째 주장은 이것이 실제로 fan이 되고, 따라서 toric variety를 정의한다는 것이다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위의 정의에 의해 얻어진 $$\Sigma_P$$는 실제로 fan이다. 즉, $$\Sigma_P$$는 정의 1의 두 조건을 모두 만족한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Sigma_P$$의 임의의 원소 $$\tau_F$$는 primitive inner normal vector들의 $$\mathbb{R}_{\ge 0}$$-linear combination으로 생성되므로 strongly convex rational polyhedral cone이다. 먼저 face 조건을 확인하자. $$\tau_F$$의 face는 $$F$$의 상위 면 $$F^\prime \supseteq F$$에 대응하며, 이는 $$\tau_{F^\prime} \in \Sigma_P$$가 되므로 첫 번째 조건이 만족된다. 두 cone $$\tau_{F_1}, \tau_{F_2} \in \Sigma_P$$의 교집합을 생각하자. $$\tau_{F_1} \cap \tau_{F_2}$$는 $$F_1$$과 $$F_2$$의 교집합을 포함하는 가장 작은 면 $$F$$에 대응하는 cone $$\tau_F$$와 같다. 이는 $$\tau_{F_1}$$과 $$\tau_{F_2}$$ 모두의 face가 되므로, 두 번째 조건도 만족된다.

</details>

따라서 normal fan은 toric variety $$X_{\Sigma_P}$$를 정의한다. 우리가 다음으로 살펴볼 것은 이렇게 얻어진 toric variety가 단순한 toric variety가 아닌 *projective* variety가 된다는 점이며, 더 나아가 projective인 toric variety는 사실상 모두 이 방식으로 얻어진다는 것이다. 이러한 양방향 대응을 정확히 기술하기 위해서는 toric variety 위의 line bundle과 polytope 사이의 관계를 먼저 정리해두는 것이 좋다.

이미 [명제 5](#prop5) 직후에 살펴본 것처럼, $$X_\Sigma$$의 stratum 구조는 fan $$\Sigma$$의 cone들과 대응된다. 특히 0차원 cone $$\{0\}$$은 open dense torus $$T_N \subset X_\Sigma$$에, 1차원 cone $$\rho \in \Sigma(1)$$들 (여기서 $$\Sigma(1)$$은 $$\Sigma$$의 1차원 cone들의 집합)은 각각 codimension 1의 $$T_N$$-invariant prime divisor $$D_\rho \subset X_\Sigma$$에 대응된다. 따라서 free abelian group $$\bigoplus_\rho \mathbb{Z} D_\rho$$가 $$X_\Sigma$$ 위의 $$T_N$$-invariant Weil divisor 전체를 기술한다.

우리가 관심있는 것은 toric variety의 line bundle이므로, 우리는 *Cartier* divisor들에 집중해야 한다. Cartier divisor를 piecewise linear function의 언어로 기술하고 line bundle과 잇는 자세한 논의는 다음 글인 [§토러스 인자와 선다발](/ko/math/toric_geometry/toric_divisors)에서 다룰 것이지만, 이번 글에서의 논의를 위해 우리는 우선 [§토러스 인자와 선다발, ⁋명제 6](/ko/math/toric_geometry/toric_divisors#prop6)의 결과를 먼저 번역해오기로 한다. 

이에 따르면 $$T_N$$-invariant Weil divisor $$D = \sum_\rho a_\rho D_\rho$$가 Cartier일 필요충분조건은, 각 maximal cone $$\sigma \in \Sigma$$에 대해 어떤 $$m_\sigma \in M$$이 존재하여 $$\sigma$$의 모든 ray $$\rho$$에 대해 $$a_\rho = -\langle m_\sigma, v_\rho \rangle$$이 성립하는 것이다. 여기서 $$v_\rho$$는 $$\rho$$의 primitive generator이다. 이러한 Cartier divisor $$D$$에 대해 polytope $$P_D \subset M_\mathbb{R}$$을

$$P_D = \{u \in M_\mathbb{R} \mid \langle u, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

으로 정의하면, 위 compatibility는 정확히 $$P_D$$의 vertex들이 lattice element $$m_\sigma$$로 주어지는 것에 대응되며, 따라서 $$P_D$$는 lattice polytope이 된다. 거꾸로 lattice polytope $$P$$로부터 normal fan $$\Sigma_P$$를 얻는 과정은 [정의 6](#def6)에서 본 것과 같다. 이 양방향이 toric variety의 projectivity와 polytope 사이를 잇는 다리가 된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Toric variety $$X_\Sigma$$가 projective variety인 것은 $$\Sigma$$가 어떤 full-dimensional lattice polytope $$P$$의 normal fan, 즉 $$\Sigma = \Sigma_P$$인 것과 필요충분조건이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($$\Rightarrow$$) $$X_\Sigma$$가 projective라면 그 위에 very ample line bundle $$\mathcal{L}$$이 존재하며, 위의 대응에 의해 이는 $$T_N$$-invariant Cartier divisor $$D$$로 표현된다. 앞서 본 바, 이로부터 얻어지는 $$P_D$$는 lattice polytope이며, $$\mathcal{L}$$이 ample (특히 very ample)이므로 [§토러스 인자와 선다발, ⁋명제 9](/ko/math/toric_geometry/toric_divisors#prop9)에 의해 대응되는 piecewise linear function $$\psi_D$$는 strictly convex이다. 이로부터 $$P_D$$의 normal fan이 $$\Sigma$$와 일치함을 얻는다.

($$\Leftarrow$$) $$\Sigma = \Sigma_P$$라 하자. Polytope $$P$$의 데이터 — 즉 각 ray $$\rho$$에 대해 $$a_\rho = -\min_{u \in P}\langle u, v_\rho\rangle$$ — 로부터 $$T_N$$-invariant divisor $$D_P = \sum_\rho a_\rho D_\rho$$를 얻는다. 여기서 $$P$$의 각 vertex가 lattice point라는 사실이 정확히 앞의 compatibility 조건을 충족시켜 $$D_P$$가 Cartier가 되며, 충분히 큰 $$k > 0$$에 대해 $$kD_P$$가 very ample이 된다. 이때 $$kP$$의 lattice point들로 정의되는 monomial map $$\phi_{kP}: T_N \to \mathbb{P}^s$$의 image의 Zariski closure가 $$X_\Sigma$$와 동형이므로 ([명제 9](#prop9) 참고), $$X_\Sigma$$는 projective이다.

</details>

이러한 동치조건을 만족하는 toric variety $$X_\Sigma = X_{\Sigma_P}$$를 *projective toric variety*라 부르며, polytope $$P$$를 강조하여 $$X_P$$로 적기도 한다. 이 결과는 toric variety의 기하학적 성질이 fan의 조합론적 성질로 완전히 기술됨을 보여주는 대표적인 예시이다.

한편, polytope $$P$$로부터 projective toric variety $$X_P$$를 구성하는 또 다른 방법은 monomial map을 통해 명시적인 embedding을 주는 것이다. 핵심적인 아이디어는 $$X_P$$ 안에 $$T_N$$이 open dense subset으로 들어있다는 것이며, 따라서 $$T_N$$만 $$\mathbb{P}^s$$에 적당히 넣어주면 나머지 부분이 가야 할 곳은 자동으로 정해진다는 것이다. 

$$P \subset M_\mathbb{R}$$의 lattice point들, 즉 $$P \cap M = \{m_0, m_1, \ldots, m_s\}$$를 생각하자. 이들을 통해 monomial map

$$\phi_P: T_N \longrightarrow \mathbb{P}^s, \qquad t \longmapsto [\rchi^{m_0}(t) : \rchi^{m_1}(t) : \cdots : \rchi^{m_s}(t)]$$

을 정의할 수 있다. 여기서 $$\rchi^m: T_N \to \mathbb{C}^\ast$$는 $$m \in M$$에 대응하는 character이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 위에서 정의한 $$\phi_P$$의 image의 Zariski closure가 $$X_P$$와 isomorphic다. 즉, $$X_P \cong \overline{\phi_P(T_N)}$$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$P$$가 very ample lattice polytope일 때 (즉, $$X_P$$ 위에서 대응되는 divisor $$D_P$$가 very ample line bundle을 정의할 때), 각 vertex $$v$$에 대응하는 affine chart는 monomial들 $$\rchi^{m_i - m_v}$$들로 생성되는 coordinate ring을 갖는다. 여기서 $$m_v$$는 vertex $$v$$에 대응하는 lattice point이다. 이러한 affine chart들은 $$\mathbb{P}^s$$의 표준 affine chart들과 자연스럽게 호환되며, 이들의 gluing이 $$\overline{\phi_P(T_N)}$$를 정의한다. 일반적인 경우 $$kP$$가 very ample이 되도록 하는 $$k > 0$$를 선택하면, polytope을 양의 정수배로 확대해도 normal fan은 변하지 않으므로 $$\Sigma_{kP} = \Sigma_P$$, 따라서 $$X_{kP} = X_P$$이며 embedding은 $$kP$$를 사용하여 위와 같이 정의된다.

</details>

이 embedding은 toric variety의 조합론적 정의와 대수기하학적 정의 사이의 연결고리를 다시 한 번 보여준다. 즉, polytope $$P$$의 lattice point의 개수는 (projective) toric variety를 projective space로 embed했을 때 그 ambient projective space $$\mathbb{P}^s$$의 차원을 결정하는 것이다. 

이제 우리는 가장 기본적인 projective toric variety, 즉 projective space $$\mathbb{P}^n$$의 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> Lattice $$M = \mathbb{Z}^n$$에서 *standard simplex* $$\Delta_n \subset M_\mathbb{R}$$를

$$\Delta_n = \{(x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge 0,\; x_1 + \cdots + x_n \le 1\}$$

으로 정의한다. 이 polytope의 꼭짓점은 $$0, e_1, \ldots, e_n$$이며, facet들은 좌표 초평면 $$\{x_i = 0\}$$과 $$\{x_1 + \cdots + x_n = 1\}$$로 주어진다. 각 facet의 primitive inner normal vector는 dual lattice $$N = \mathbb{Z}^n$$의 원소로

$$v_i = e_i \quad (i = 1, \ldots, n), \qquad v_0 = -e_1 - \cdots - e_n$$

이다. 따라서 normal fan $$\Sigma_{\Delta_n}$$의 ray는 $$\rho_i = \mathbb{R}_{\ge 0} v_i$$ ($$i = 0, 1, \ldots, n$$)으로 $$n+1$$개이며, 그 maximal cone들은 이들 $$n+1$$개 ray 중 $$n$$개를 골라 생성되는 $$n$$차원 cone들이며, $$n=2$$인 경우는 [예시 2](#ex2)에서 그림과 함께 살펴보았다. 

이들의 gluing을 직접 확인하여 이것이 $$\mathbb{P}^n$$이 나오는 것을 직접 확인할 수 있으나, 그 대신 $$\Delta_n$$의 lattice points를 관찰하자. $$\Delta_n$$의 lattica point들은 정확히 꼭짓점들 $$\{0, e_1, \ldots, e_n\}$$이므로, 대응하는 monomial map은

$$\phi_{\Delta_n}: (\mathbb{C}^\ast)^n \longrightarrow \mathbb{P}^n, \qquad (t_1, \ldots, t_n) \longmapsto [1 : t_1 : \cdots : t_n]$$

가 되는 것을 확인할 수 있다.

</div>

## 매끄러움과 특이점 분해

한편 [§아핀 토릭 다양체, ⁋명제 9](/ko/math/toric_geometry/affine_toric_varieties#prop9)에서 affine toric variety $$U_\sigma$$의 smoothness가 cone $$\sigma$$의 조합론적 조건으로 판정됨을 보았다. $$X_\Sigma$$는 affine chart $$U_\tau$$의 gluing이므로, 이는 곧바로 일반 toric variety의 판정으로 일반화할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Toric variety $$X_\Sigma$$가 smooth algebraic variety인 것은 fan $$\Sigma$$의 모든 cone $$\tau \in \Sigma$$가 smooth cone인 것과 필요충분조건이다. 

</div>

혹은 더 간단하게 $$\Sigma$$의 모든 *maximal* cone이 smooth임을 확인하면 나머지 face의 smoothness는 이로부터 따라오게 된다. 

가령 [예시 2](#ex2)의 $$\mathbb{P}^2$$의 fan에서 세 maximal cone은 인접한 두 ray ($$\{e_1, e_2\}, \{e_2, -e_1-e_2\}, \{-e_1-e_2, e_1\}$$)로 만든 $$2 \times 2$$ 행렬의 determinant가 모두 $$\pm 1$$이므로 $$\mathbb{P}^2$$는 smooth이다. 반면 같은 lattice $$\mathbb{Z}^2$$에서 ray $$(-1,-1), (2,-1), (-1,2)$$ 세 개로 만든 fan을 생각하면 인접한 두 ray의 행렬식이 $$\pm 3$$으로, 그 toric variety는 세 maximal cone마다 $$\mathbb{Z}/3$$ quotient singularity를 갖는다.

이러한 singular toric variety에 대한 *resolution of singularities* 또한 fan의 refinement로 명시적이고 조합론적인 방식으로 이뤄진다. 우선 fan $$\Sigma'$$가 $$\Sigma$$의 *refinement*라는 것은 두 fan의 support가 같고 $$\Sigma'$$의 모든 cone이 $$\Sigma$$의 어떤 cone에 포함되는 것이다. 이 경우 자연스러운 toric morphism 

$$\pi: X_{\Sigma'} \to X_\Sigma$$

가 proper birational map으로 정의되며, 만일 $$\Sigma'$$가 모두 smooth cone으로만 구성된다면 $$\pi$$는 *toric resolution of singularities*가 된다. 임의의 fan에 대해 이러한 refinement는 항상 존재하며, 그 구성의 핵심은 다음과 같다.

1. Non-simplicial cone은 *star subdivision* 으로 simplicial하게 만들 수 있다. 이는 내부 lattice point에서 적절하게 cone을 나눠주는 것으로 생각하면 된다. 
2. Simplicial이지만 determinant가 $$\pm 1$$이 아닌 cone $$\sigma$$는 적절한 lattice point를 새 ray로 추가하여 더 작은 cone들로 쪼개면 각 부분의 determinant가 줄어들며, 유한 번의 반복으로 모두 smooth cone이 된다.

위 $$\mathbb{P}^2/(\mathbb{Z}/3)$$의 예에서는, 세 maximal cone 각각의 내부에 위치한 lattice point $$e_1, e_2, -e_1-e_2$$를 새 ray로 추가하면 모든 maximal cone의 행렬식이 모두 $$\pm 1$$로 떨어지며 결과는 정확히 $$\mathbb{P}^2$$의 표준 fan이 된다. 즉 $$\mathbb{P}^2 \to \mathbb{P}^2/(\mathbb{Z}/3)$$가 이 quotient의 (minimal) toric resolution이다.

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.