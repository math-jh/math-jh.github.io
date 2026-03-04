---
title: "A-model과 B-model: Mirror Symmetry의 기초"
excerpt: "Mirror symmetry의 핵심 개념인 A-model과 B-model의 차이점과 대응 관계"

categories: [Math / Mirror Symmetry]
permalink: /ko/mirror_symmetry/01-a-model-b-model

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/a-model-b-model.png
    overlay_filter: 0.5

sidebar:
    nav: "mirror_symmetry-ko"

date: 2026-03-05
last_modified_at: 2026-03-05
weight: 1
---

## A-model과 B-model: Mirror Symmetry의 기초

우리는 **Mirror Symmetry**를 연구하고 있습니다. 이 개념은 물리학, 대수기하학, 위상수학 사이의 놀라운 연결을 보여주며, 최근에는 Calabi-Yau 다양체의 모델링 등 다양한 응용 분야로 확장되고 있습니다. Mirror symmetry의 핵심은 **하나의 대수적 다양체에 대해 서로 다른 두 물리학적 모델이 서로 같은 정보를 담고 있다**는 것입니다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> **Mirror Symmetry**는 두 대수적 다양체 $(X, \check X)$가 서로 mirror pair라고 할 때, $X$의 A-model의 물리량이 $\check X$의 B-model의 물리량과 대응한다는 관계를 말합니다.

</div>

이 개념을 이해하기 위해 A-model과 B-model이라는 두 개의 물리학적 모델을 정의해야 합니다.

### A-model: Symplectic side

A-model은 **symplectic manifold**에 대한 모델입니다. Grassmannian 같은 대수적 다양체 위에 정의될 때, A-model은 다음과 같은 수학적 개념들을 다룹니다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> **Gromov-Witten invariant**은 두 대수적 다양체 사이에 존재하는 **초구 곡선(meromorphic curves)**의 수를 세는 수량입니다.

</div>

구체적으로, Grassmannian $X = Gr_{n-k}(\mathbb{C}^n)$ 위에 대해, A-model은 다음과 같은 데이터를 다룹니다.

- **Quantum cohomology**: 일반적인 cohomology ring을 quantum deformation하여 얻은 구조
- **Rational curves counting**: 특정 차원의 rational curve들의 계수를 나타내는 수량

수학적으로, A-model의 quantum cohomology ring은 다음과 같이 정의됩니다.

$$
H^*(X)^\mathbb{Q}[t] \to H^*(X)^\mathbb{Q}[t], \quad
\alpha \star_q \beta = \sum_{\gamma, d} \langle \alpha, \beta, \gamma \rangle_d \cdot t^d \cdot [\gamma]
$$

여기서 $\langle \cdot, \cdot, \cdot \rangle_d$는 degree $d$의 Gromov-Witten invariant입니다.

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> Grassmannian $Gr_{2}(\mathbb{C}^5)$에서, 차원 2의 rational curve의 수를 세는 Gromov-Witten invariant은 다음과 같이 계산됩니다.

$$
\langle \sigma_1, \sigma_1, \sigma_1 \rangle_2 = 1
$$

여기서 $\sigma_1$은 hyperplane class를 나타냅니다.

</div>

### B-model: Complex side

반면, B-model은 **complex algebraic variety**에 대한 모델입니다. B-model은 singularity theory와 variation of Hodge structure을 다룹니다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> **Variation of Hodge structure**는 하나의 다양체 위의 Hodge 구조가 주어진 구간에서 어떻게 변하는지를 나타내는 기구입니다.

</div>

B-model의 핵심은 다음과 같습니다.

- **Landau-Ginzburg model**: Singularity을 다루는 모델
- **Superpotential**: 이 모델에서의 중요한 함수
- **Oscillating integral**: B-model의 자질량을 계산하는 방법

수학적으로, B-model은 다음과 같은 방정식으로 정의됩니다.

$$
W: Y \to \mathbb{C}
$$

여기서 $Y$는 affine variety이고, $W$는 superpotential입니다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> **Mirror Symmetry의 핵심 아이디어**: A-model의 Gromov-Witten invariants가 B-model의 oscilating integral를 통해 명시적으로 계산 가능하다는 것입니다.

</div>

### Main Theorem의 의미

Marsh-Rietsch 논문에서는 A-model과 B-model 사이의 대응을 D-module 이론을 통해 증명합니다.

<details class="proof" markdown="1>
<summary>증명 개요</summary>

주어진 Grassmannian $X = Gr_{n-k}(\mathbb{C}^n)$에 대해, A-model connection $(\mathcal{H}_A, \nabla^A)$과 B-model connection $(\mathcal{H}_B, \nabla^B)$를 구성합니다. 여기서 $\nabla^A$는 Dubrovin connection이고, $\nabla^B$는 B-model connection입니다.

우리는 $\mathcal{H}_A$와 $\mathcal{H}_B$ 사이에 **D-module isomorphism**을 찾습니다. 이 isomorphism을 통해 A-model의 flat section $S(q)$가 B-model의 oscilating integral로 표현됩니다.

$$
S(q) = \sum_{\lambda} \left( \oint_{e^{\frac{1}{\hbar}W_q}/2\pi i} e^{\frac{1}{\hbar}W_q} p_\lambda \omega \right) PD(\sigma^\lambda)
$$

여기서 $\lambda$는 Plücker coordinate, $p_\lambda$는 Plücker coordinate의 지표입니다.
</details>

<div class="corollary" markdown="1">

<ins id="cor1">**따름정리 1**</ins> 이 isomorphism을 통해 Gromov-Witten invariants를 B-model의 superpotential를 통해 계산할 수 있습니다.

</div>

### Buch-Kresch-Tamvakis와의 비교

이 개념은 Buch, Kresch, Tamvakis의 이전 연구와도 연결됩니다. 두 논문 모두 Grassmannian의 Gromov-Witten invariants를 계산하지만 접근 방식이 다릅니다.

| 측면 | Buch et al. | Marsh-Rietsch |
|------|-------------|---------------|
| GW invariant 계산 | Explicit formula | Mirror symmetry 이용 |
| 배경 | Schubert calculus | Frobenius manifolds |
| 결과 | Classical intersection과 연결 | B-model과 연결 |

---

**참고문헌**

**[MR]** Rigoberto F. S. Miranda, Mark Hamilton, "A model for Gr(m,n) and G/P using quantum cohomology", 2003
**[DG]** Victor Guillemin, Shlomo Sternberg, "Symplectic Techniques in Physics"
**[IKP]** Givental, "Homological Geometry I"
**[Iritani]** Tatsuki Iritani, "Quantum cohomology and periods"
**[BKT]** Bertold, "The mirror of the Grassmannian"
