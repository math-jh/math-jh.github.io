---
title: "A-model과 B-model: Mirror Symmetry의 기초"
excerpt: "Mirror symmetry의 핵심 개념인 A-model과 B-model의 차이점과 대응 관계"

categories: [Math / Mirror Symmetry]
permalink: /ko/mirror_symmetry/01-a-model-b-model

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/a-model-b-model.png
    overlay_filter: 0.5

date: 2026-03-05
last_modified_at: 2026-03-05
weight: 1
---

## A-model과 B-model

Mirror symmetry는 하나의 복소 다양체 $X$에 대해 서로 다른 두 물리학적 모델(A-model, B-model)이 서로 같은 정보를 담고 있다는 이론이다. 이 섹션에서는 이 두 모델의 기본적인 차이점과 대응 관계를 살펴볼 것이다.

<div class="proposition" markdown="1">
<ins id="def1">**정의 1**</ins> $X$를 컴팩트한 사각형(symplectic) 다양체라고 하자. A-model은 $X$ 위의 **사각형 기하학(symplectic geometry)**을 다루는 물리학적 모델이고, B-model은 $X$ 위의 **복소 기하학(complex geometry)**을 다루는 모델이다.
</div>

---

### A-model (Symplectic Model)

A-model은 $X$ 위의 **Gromov-Witten invariant**을 통해 다양한 형태의 램프(ramified cover)의 계수를 셈으로서 계산한다. 이 모델의 핵심은 **양자 코호몰로지(quantum cohomology)**을 이용하는 것이다.

<div class="proposition" markdown="1">
<ins id="prop1">**명제 1**</ins> A-model에서 중요한 데이터들은 다음과 같다:
- $QH^\ast(X)$: 양자 코호몰로지 군
- $GW_n(X)$: 차수 $n$의 Gromov-Witten invariant
</div>

이 모델에서 우리는 **유리 곡선(rational curve)**의 개수를 셈으로서, 다양한 기하학적 데이터를 얻는다.

---

### B-model (Complex Model)

B-model은 $X$ 위의 **변형의 호지 구조(variation of Hodge structure)**를 다룬다. 이 모델은 주로 **특이점 이론(singularity theory)**과 연결된다.

<div class="proposition" markdown="1">
<ins id="prop2">**명제 2**</ins> B-model에서 중요한 데이터들은 다음과 같다:
- $VH^\ast(X)$: 변형의 호지 구조
- $W(X)$: superpotential
- Oscillating integrals
</div>

이 모델은 복소 다양체의 구조적 정보를 다루며, 특히 특이점 근처의 토폴로지 변화를 포착한다.

---

### Mirror Symmetry의 핵심 아이디어

Mirror symmetry의 핵심은 다음과 같다: **A-model의 데이터가 B-model의 데이터로 대응**된다.

<div class="theorem" markdown="1">
<ins id="thm1">**정리 1**</ins> (Mirror Symmetry의 핵심) $X$를 복소 다양체라고 할 때, A-model의 Gromov-Witten invariants와 B-model의 osculating integral 사이에 다음과 같은 대응이 존재한다.

$$S(q) = \sum_{\lambda} \left(\oint e^{\frac{1}{\hbar}W_q} p_\lambda \omega\right) PD(\sigma^\lambda)$$

이 함수 $S(q)$는 A-model의 flat section equation을 만족한다.
</div>

이 정리는 A-model의 양자 코호몰로지 계수를 B-model의 superpotential를 통해 계산 가능하게 만든다.

---

### A-model vs B-model 비교

다음 표는 A-model과 B-model의 주요 차이점을 요약한 것이다.

| 특징 | A-model | B-model |
|------|---------|---------|
| **기하학적 성질** | 사각형 기하학 (symplectic geometry) | 복소 기하학 (complex geometry) |
| **핵심 데이터** | Gromov-Witten invariant, 양자 코호몰로지 | 변형의 호지 구조, superpotential |
| **계산 방법** | 유리 곡선의 개수 셈 | 특이점 이론 |
| **quantum parameter** | $q$ (Kähler parameter) | $q$ (quantum parameter) |
| **구조** | cohomological | D-module |

---

## 응용

Mirror symmetry는 다양한 분야에서 응용될 수 있다.

<div class="example" markdown="1">
<ins id="ex1">**예시 1**</ins> Grassmannian $Gr_{n-k}(\mathbb{C}^n)$의 A-model 데이터를 B-model 데이터로 변환할 수 있다. 이를 통해 양자 코호몰로지의 구조를 명시적으로 계산할 수 있다.
</div>

<div class="example" markdown="1">
<ins id="ex2">**예시 2** | String theory에서, A-model은 2D string theory, B-model은 2D sigma model에 대응한다. 이 두 모델은 물리적으로 같은 진폭을 계산하므로, 서로 다른 접근 방법을 제공한다.
</div>

---

## 다음 단계

다음 섹션에서는 **Dubrovin connection**을 배울 것이다. 이는 A-model의 flat connection을 정의하는 중요한 도구다.

[\[Mirror Symmetry\] §Dubrovin Connection, ⁋정의 1](/ko/mirror_symmetry/02-dubrovin-connection#def1)

---

**참고문헌**

**[MR]** Andrei Marsh, Kenji Rietsch. *A mirror construction for G/P*. 2004.

**[Dub]** Viktor Dubrovin. *Geometry of 2D topological field theories*. Lecture Notes in Mathematics, 1620. Springer, 1996.
