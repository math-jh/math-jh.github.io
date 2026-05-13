---
title: "Normal fan과 projective toric variety"
excerpt: "Toric geometry"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/normal_fan_projective_toric

header:
    overlay_image: /assets/images/Math/Toric_Geometry/Normal_Fan_and_Projective_Toric_Variety.png
    overlay_filter: 0.5

sidebar:
    nav: "toric_geometry-ko"

date: 2026-03-06
last_modified_at: 2026-03-06
weight: 2
---

[§아핀 토릭 다양체, ⁋정의 5](/ko/math/toric_geometry/affine_toric_varieties#def5)에서 정의한 affine toric variety는 하나의 strongly convex rational polyhedral cone $\tau$에 대응하는 대수다양체 $U_\tau$이다. 그러나 $\tau$가 원점 $\{0\}$인 경우에만 $U_\tau$는 algebraic torus $T_N$과 같으며, 일반적인 cone에 대해서는 $U_\tau$는 적절한 방향으로 열린 부분공간의 형태를 띤다. 우리는 이러한 affine toric variety들을 여러 개 모아서 이어붙이는 방법을 찾고자 하며, 이를 통해 compact한 toric variety를 얻는 것이 이 글의 목표이다.

## Fan의 정의

Affine toric variety들을 이어붙이기 위해서는 각각의 cone들이 서로 어떻게 만나는지를 제어하는 조합론적인 구조가 필요하다. 이를 위해 우리는 *fan*을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lattice $N$에 대해, $N_\mathbb{R}$에 정의된 *fan* $\Sigma$는 다음 조건을 만족하는 strongly convex rational polyhedral cone들의 모임이다:

1. $\Sigma$에 속하는 임의의 cone $\tau$의 face도 $\Sigma$에 속한다.
2. $\Sigma$에 속하는 임의의 두 cone $\tau_1, \tau_2$의 교집합 $\tau_1 \cap \tau_2$는 각각의 face이다.

</div>

두 번째 조건이 중요한 이유는, 서로 다른 두 cone $\tau_1, \tau_2$가 만나는 방식이 그들의 공통 face에서만 일어나도록 강제하기 때문이다. 이는 훗날 $U_{\tau_1}$과 $U_{\tau_2}$를 이어붙일 때 그 교집합이 자연스럽게 정의되도록 보장한다. 한편 첫 번째 조건은 fan이 각 cone의 모든 면을 포함함으로써 닫혀 있음을 요구한다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $N = \mathbb{Z}^2$에서 원점을 중심으로 방사형으로 세 개의 2차원 cone $\tau_0, \tau_1, \tau_2$가 $\mathbb{R}^2$를 덮는 fan을 생각할 수 있다. 각각의 cone은 두 개의 반직선 원소 $\rho_i, \rho_{i+1}$에 의해 생성되며, 이러한 반직선들은 1차원 cone들이 된다. 원점 $\{0\}$ 자체는 0차원 cone으로서 모든 fan에 포함된다. 이 fan은 $\mathbb{P}^2$의 toric variety를 정의하는 가장 기본적인 예시이다.

</div>

## Toric variety의 정의

이제 fan $\Sigma$가 주어졌을 때, 이로부터 대수다양체 $X_\Sigma$를 구성하는 방법을 설명한다. 각각의 cone $\tau \in \Sigma$에 대하여 [§아핀 토릭 다양체, ⁋정의 5](/ko/math/toric_geometry/affine_toric_varieties#def5)에 의해 affine toric variety $U_\tau$를 얻는다. 두 cone $\tau_1, \tau_2 \in \Sigma$가 공통 face $\tau_1 \cap \tau_2$를 가질 때, [§아핀 토릭 다양체, ⁋명제 9](/ko/math/toric_geometry/affine_toric_varieties#prop9)에 의해 $U_{\tau_1 \cap \tau_2}$는 $U_{\tau_1}$과 $U_{\tau_2}$ 모두의 주 열린 부분집합이 된다. 따라서 이들 사이에 자연스러운 동형사상

$$U_{\tau_1} \supset U_{\tau_1 \cap \tau_2} \cong U_{\tau_2 \cap \tau_1} \subset U_{\tau_2}$$

이 존재하며, 이를 통해 $U_\tau$들을 이어붙일 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Fan $\Sigma$에 대하여, affine toric variety들 $\{U_\tau\}_{\tau \in \Sigma}$를 위에서 기술한 방식으로 이어붙여 얻어지는 대수다양체를 $\Sigma$가 정의하는 *toric variety*라 하며, $X_\Sigma$로 적는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Toric variety $X_\Sigma$는 normal이고 separated인 대수다양체이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$X_\Sigma$의 normality는 각 affine chart $U_\tau$가 [§아핀 토릭 다양체, ⁋명제 11](/ko/math/toric_geometry/affine_toric_varieties#prop11)에 의해 normal이고, 이 성질이 gluing에 의해 보존되기 때문이다. Separatedness를 보이기 위해서는 diagonal morphism $\Delta: X_\Sigma \to X_\Sigma \times X_\Sigma$의 image가 닫힌 집합임을 확인하면 된다. 각 affine chart 위에서 이는 두 cone의 교집합이 face임을 보장하는 fan의 두 번째 조건에 의해 성립한다. 

</details>

Toric variety $X_\Sigma$가 가지는 중요한 성질 중 하나는 algebraic torus $T_N$을 열린 조밀한 부분집합으로 포함한다는 것이다. 실제로, 0차원 cone $\{0\} \in \Sigma$에 대응하는 affine chart $U_{\{0\}}$는 $T_N$과 동형이며, 다른 모든 $U_\tau$는 이를 열린 부분집합으로 포함한다. 따라서 $T_N \subset X_\Sigma$는 열린 조밀한 임베딩을 정의한다.

## 토러스 작용과 궤도

[§아핀 토릭 다양체, ⁋명제 8](/ko/math/toric_geometry/affine_toric_varieties#prop8)에서 보았듯이, 각 affine toric variety $U_\tau$ 위에는 algebraic torus $T_N$의 작용이 자연스럽게 정의된다. 이 작용은 gluing을 통해 $X_\Sigma$ 전체로 확장되며, 이로부터 $X_\Sigma$는 $T_N$의 *equivariant compactification*이 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Toric variety $X_\Sigma$ 위에는 algebraic torus $T_N$의 작용이 자연스럽게 정의되며, 이 작용은 $X_\Sigma$를 $T_N$의 equivariant compactification으로 만든다. 즉, $T_N$은 $X_\Sigma$의 열린 조밀한 부분집합으로 포함되고, $T_N$의 자기작용은 $X_\Sigma$ 위의 작용으로 확장된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각각의 cone $\tau \in \Sigma$에 대해, $U_\tau$ 위의 $T_N$-action은 [§아핀 토릭 다양체, ⁋명제 8](/ko/math/toric_geometry/affine_toric_varieties#prop8)에 의해 정의된다. 두 affine chart $U_{\tau_1}$과 $U_{\tau_2}$의 교집합 $U_{\tau_1 \cap \tau_2}$ 위에서 이들 작용은 일치하므로, 이들은 $X_\Sigma$ 전체에서 well-defined한 $T_N$-action을 정의한다. 한편 $\{0\} \in \Sigma$에 대응하는 chart $U_{\{0\}} \cong T_N$은 열린 조밀한 부분집합이며, $T_N$의 자기작용은 이 chart 위에서 좌곱셈으로 주어지므로 $X_\Sigma$ 위의 작용으로 자연스럽게 확장된다.

</details>

이 작용에 의한 궤도들의 구조는 fan의 조합론과 밀접하게 연관된다. 구체적으로, $d$-차원 cone $\tau \in \Sigma$에 대응하는 궤도 $\mathcal{O}(\tau)$는 차원 $n-d$의 torus $(\mathbb{C}^\ast)^{n-d}$와 동형이다. 특히 $n$-차원 cone, 즉 maximal cone에 대응하는 궤도는 0차원이며 이는 $T_N$-action의 고정점이 된다.

## Normal fan과 projective toric variety

지금까지는 임의의 fan $\Sigma$로부터 toric variety $X_\Sigma$를 구성하는 방법을 살펴보았다. 이제 우리는 특별한 종류의 fan, 즉 polytope으로부터 자연스럽게 얻어지는 *normal fan*에 대해 논의한다. 이는 projective toric variety를 만드는 핵심적인 방법이다.

Lattice $M$의 dual lattice가 $N$이고, $M_\mathbb{R}$의 full-dimensional convex lattice polytope $P$를 생각하자. $P$의 각 면 $F \subseteq P$에 대하여, $F$를 포함하는 모든 facet $F^\prime$의 primitive inner normal vector $u_{F^\prime}$들로 생성되는 cone을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Polytope $P$의 *normal fan* $\Sigma_P$는 다음과 같이 정의된다. $P$의 각 면 $F$에 대해, $F$를 포함하는 모든 facet들의 primitive inner normal vector들이 생성하는 cone $\tau_F$를 생각하고,

$$\Sigma_P = \{\tau_F \mid F \text{ is a face of } P\}$$

로 정의한다.

</div>

여기서 primitive inner normal vector란, 해당 facet에 수직이고 polytope의 내부를 향하는 방향을 가리키며, lattice $N$에서 가장 짧은 길이를 갖는 벡터를 의미한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위의 정의에 의해 얻어진 $\Sigma_P$는 실제로 fan이다. 즉, $\Sigma_P$는 정의 1의 두 조건을 모두 만족한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\Sigma_P$의 임의의 원소 $\tau_F$는 primitive inner normal vector들의 $\mathbb{R}_{\ge 0}$-linear combination으로 생성되므로 strongly convex rational polyhedral cone이다. 먼저 face 조건을 확인하자. $\tau_F$의 face는 $F$의 상위 면 $F^\prime \supseteq F$에 대응하며, 이는 $\tau_{F^\prime} \in \Sigma_P$가 되므로 첫 번째 조건이 만족된다. 두 cone $\tau_{F_1}, \tau_{F_2} \in \Sigma_P$의 교집합을 생각하자. $\tau_{F_1} \cap \tau_{F_2}$는 $F_1$과 $F_2$의 교집합을 포함하는 가장 작은 면 $F$에 대응하는 cone $\tau_F$와 같다. 이는 $\tau_{F_1}$과 $\tau_{F_2}$ 모두의 face가 되므로, 두 번째 조건도 만족된다.

</details>

Normal fan의 중요한 성질은 polytope $P$와 그 normal fan $\Sigma_P$ 사이의 조합론적 쌍대성이다. 구체적으로, $P$의 $d$-차원 면 $F$는 $\Sigma_P$의 $(n-d)$-차원 cone $\tau_F$와 일대일로 대응하며, 이 대응은 포함관계를 뒤집는다. 즉, $F_1 \subseteq F_2$일 때 $\tau_{F_2} \subseteq \tau_{F_1}$이 성립한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Toric variety $X_\Sigma$가 *projective toric variety*라 함은, 어떤 full-dimensional lattice polytope $P$에 대해 $\Sigma = \Sigma_P$가 성립하는 경우를 말한다. 이 경우 $X_\Sigma$를 $X_P$로도 적는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Toric variety $X_\Sigma$가 projective variety인 것은 $\Sigma$가 어떤 lattice polytope의 normal fan인 것과 필요충분조건이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

($\Rightarrow$) $X_\Sigma$가 projective variety라고 가정하자. 그러면 $X_\Sigma$ 위에 very ample line bundle $\mathcal{L}$이 존재한다. Toric variety 위의 line bundle은 $T_N$-invariant Cartier divisor $D$에 의해 주어지며, 이 divisor에 대응하는 *polytope* $P_D$를 정의할 수 있다. 구체적으로,

$$P_D = \{u \in M_\mathbb{R} \mid \langle u, v_\rho \rangle \ge -a_\rho \text{ for all } \rho \in \Sigma(1)\}$$

로 정의한다. 여기서 $v_\rho$는 각 1차원 cone $\rho$의 primitive generator이고 $a_\rho$는 divisor $D$의 계수이다. 이렇게 정의된 $P_D$는 lattice polytope이며, 그 normal fan이 정확히 $\Sigma$와 일치함을 확인할 수 있다.

($\Leftarrow$) 반대로 $\Sigma = \Sigma_P$가 어떤 full-dimensional lattice polytope $P$의 normal fan이라고 하자. $kP$가 very ample이 되도록 하는 충분히 큰 $k > 0$를 선택할 수 있다. 이때 $kP$의 lattice points에 의한 monomial map $\phi_{kP}: T_N \to \mathbb{P}^s$의 image의 Zariski closure는 projective variety이며, 이는 정의에 의해 $X_{kP} = X_P = X_\Sigma$와 동형이다. 따라서 $X_\Sigma$는 projective variety이다.

</details>

이 명제는 toric variety의 기하학적 성질이 fan의 조합론적 성질로 완전히 기술됨을 보여주는 대표적인 결과이다. 특히, complete fan $\Sigma$에 대해 $X_\Sigma$가 projective인 것은 $\Sigma$가 normal fan이 될 필요충분조건이다.

## Toric embedding

Polytope $P$로부터 projective toric variety $X_P$를 구성하는 또 다른 방법은 monomial map을 통해 명시적인 임베딩을 주는 것이다. $P \subset M_\mathbb{R}$의 lattice point들, 즉 $P \cap M = \{m_0, m_1, \ldots, m_s\}$를 생각하자. 이들을 통해 monomial map

$$\phi_P: T_N \longrightarrow \mathbb{P}^s, \qquad t \longmapsto [\chi^{m_0}(t) : \chi^{m_1}(t) : \cdots : \chi^{m_s}(t)]$$

을 정의할 수 있다. 여기서 $\chi^m: T_N \to \mathbb{C}^\ast$는 $m \in M$에 대응하는 character이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 위에서 정의한 $\phi_P$의 image의 Zariski closure가 $X_P$와 동형이다. 즉, $X_P \cong \overline{\phi_P(T_N)}$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$P$가 very ample lattice polytope일 때, 각 vertex $v$에 대응하는 affine chart는 monomial들 $\chi^{m_i - m_v}$들로 생성되는 coordinate ring을 갖는다. 여기서 $m_v$는 vertex $v$에 대응하는 lattice point이다. 이러한 affine chart들은 $\mathbb{P}^s$의 표준 affine chart들과 자연스럽게 호환되며, 이들의 gluing이 $\overline{\phi_P(T_N)}$를 정의한다. 일반적인 경우, $kP$가 very ample이 되도록 하는 $k > 0$를 선택하면 $X_P$는 $X_{kP}$와 동일한 abstract variety이므로, 임베딩은 $kP$를 사용하여 정의된다.

</details>

이 임베딩은 toric variety의 조합론적 정의와 대수기하학적 정의 사이의 연결고리를 제공한다. Polytope $P$의 lattice point의 개수는 임베딩된 toric variety가 놓이는 projective space $\mathbb{P}^s$의 차원을 결정하며, $P$의 각 면의 구조는 $X_P$의 궤도 분해에 직접적으로 대응한다.

## 예시: 사영공간

가장 기본적인 projective toric variety는 projective space $\mathbb{P}^n$이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> Lattice $M = \mathbb{Z}^n$에서 *standard simplex* $\Delta_n$를 다음과 같이 정의한다:

$$\Delta_n = \{(x_1, \ldots, x_n) \in \mathbb{R}^n \mid x_i \ge 0,\; x_1 + \cdots + x_n \le 1\}.$$

이 polytope의 꼭짓점은 $0, e_1, \ldots, e_n$이며, 각 facet은 좌표 초평면들과 $x_1 + \cdots + x_n = 1$으로 주어진다. 각 facet의 primitive inner normal vector는 각각 $-e_1, \ldots, -e_n$과 $e_1 + \cdots + e_n$이다. 따라서 normal fan $\Sigma_{\Delta_n}$은 원점을 중심으로 하는 $n+1$개의 반직선들로 생성되는 cone들의 모임이 되며, 이는 $\mathbb{P}^n$의 표준 fan과 일치한다. 따라서

$$X_{\Delta_n} \cong \mathbb{P}^n$$

가 성립한다. 또한 $\Delta_n$의 lattice points는 $0, e_1, \ldots, e_n$이므로, 대응하는 monomial map은

$$\phi_{\Delta_n}: (\mathbb{C}^\ast)^n \longrightarrow \mathbb{P}^n, \qquad (t_1, \ldots, t_n) \longmapsto [1 : t_1 : \cdots : t_n]$$

가 되며, 이는 $\mathbb{P}^n$의 표준 affine chart들의 통합과 일치한다.

</div>

이 예시에서 볼 수 있듯이, standard simplex의 normal fan은 가장 단순한 complete fan이며, 이로부터 얻어지는 toric variety는 가장 기본적인 compact toric variety인 projective space가 된다. Standard simplex의 각 면은 $\mathbb{P}^n$의 coordinate subspace들과 대응하며, 이는 normal fan과 polytope 사이의 쌍대성을 구체적으로 보여준다.

---

**참고문헌**

**[Ful]** William Fulton, *Introduction to Toric Varieties*, Annals of Mathematics Studies, Princeton University Press, 1993.  
**[CLS]** David Cox, John Little, Hal Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.
