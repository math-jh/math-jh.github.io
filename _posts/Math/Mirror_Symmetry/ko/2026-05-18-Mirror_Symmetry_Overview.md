---
title: "Mirror Symmetry 개요"
excerpt: "A-model과 B-model의 대응, 그리고 Hori-Vafa mirror construction을 중심으로 한 mirror symmetry의 직관적 소개"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/overview
sidebar: 
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Overview.png
    overlay_filter: 0.5

date: 2026-05-18
last_modified_at: 2026-05-18
weight: 1

published: false
---

Mirror symmetry는 수학 체계 안에서 자연스럽게 생겨난 분야가 아니라, 초끈이론을 그 기반으로 한다. 초끈이론에 따르면 우리가 살고 있는 세상은 그 기본 자유도가 *점 입자*가 아닌 *1차원 string*이라는 한 줄의 가정에서 출발한다. 그럼 입자가 시간축을 따라 움직일 때의 시공간 상에서의 궤적은 더 이상 $$1$$차원 worldline이 아니라 $$2$$차원 worldsheet가 되며, 그 운동방정식은 [\[사교기하학\] §고전역학, §§최소작용의 원리](/ko/math/symplectic_geometry/classical_mechanics#최소작용의-원리)에서와 마찬가지로 특정 한 action-minimizing solution으로 결정된다. 이 해석을 기존의 양자역학의 프레임에 일치시키기 위해서는 시공간이 $$10$$차원으로 강제되므로, 물리학자들은 이 10차원 시공간을 $$4$$차원 Minkowski 시공간과, 나머지 $$6$$차원을 해결해주는 compact manifold $$M$$의 곱으로 생각한다. 물리적으로 이 공간 $$X$$가 만족해야 하는 조건들을 써 보면, $$X$$는 *Calabi-Yau threefold*가 되어야 하는 것을 알 수 있다.

한편, 10차원 superstring에는 worldsheet가 만족해야 할 boundary 조건과 양자역학적 조건의 선택에 따라 다섯 종류의 타입으로 나뉜다. 이들 중 mirror symmetry의 직접적인 무대가 되는 것은 Type IIA와 Type IIB superstring theory로, 이들은 그 이름에서 알 수 있듯 서로 밀접한 관련이 있다. Type IIA 초끈이론은 Calabi-Yau threefold $$X$$ 위에서 Kähler structure와 complex structure를 주며, Type IIB 초끈이론은 이들 두 구조가 바뀌어 들어가며 새로운 Calabi-Yau threefold $$\check{X}$$를 정의하게 된다. 

따라서, 만일 서로 다른 두 Calabi-Yau threefold $$X$$와 $$\check{X}$$가 단일한 이론의 Type IIA/IIB로 나타나는 것들이라면, $$X$$의 Kähler structure와 $$\check{X}$$의 complex structure 사이의 관계를 줄 것이다. 이러한 쌍 $$(X, \check{X})$$를 우리는 *mirror pair*라 부르고, 이들 사이의 대칭성을 *mirror symmetry*라 한다.

이 관계는 거의 대부분 물리학자들의 직관으로 뒷받침되고, 수학적인 언어로 기술되지는 않았기 때문에 초기에는 수리물리학자들을 제외한 다른 수학자들에게는 그리 흥미로운 문제가 아니었다. 상황이 바뀐 것은 1991년 5월에 MSRI에서 열린 mirror symmetry 워크샵으로, Candelas, de la Ossa, Green, Parkes가 quintic Calabi-Yau threefold 위의 degree $$d$$ rational curve들의 개수를 mirror symmetry 가정을 통해 $$\check{X}$$에서의 계산으로 옮겨 수행해냈다. 여기에는 흥미로운 일화가 존재하는데, 처음에는 기존 대수기하학자들이 intersection theory를 통해 예측한 값과 물리학자들이 이를 통해 예측한 값이 달랐다. 이후 대수기하학자들의 코드에서 버그가 발견되었고, 이를 수정하여 재계산한 결과 물리학자들의 계산이 맞았던 것으로 판명되며 수학계에서도 mirror symmetry가 핵심적인 연구분야로 부상하게 된다. 

그러나 물리학자들의 직관은 근본적으로 양자역학의 결과들로부터 온 것이기 때문에 이를 수학적으로 formalize하는 것은 불가능했고, 이를 수학적으로 가져오기 위해서는 적당한 formalism이 필요했다. 수학자들이 보편적으로 받아들이는 정석적인 framework는 Givental formalism으로, 이는 간략히 말하자면 A-model의 불변량인 Gromov-Witten invariant들을 $$J$$-function이라는 데이터로 묶어주고, 비슷하게 B-model의 불변량인 oscillating integral을 $$I$$-function으로 묶어준다면 이들은 적절한 변수변환을 통해 서로 같다는 것이다.

본 글의 나머지에서는 이 framework이 가장 명시적으로 실현되는 *toric variety*의 mirror, 즉 *Hori-Vafa mirror construction*을 살펴보고 $$\mathbb{P}^1, \mathbb{P}^2$$의 구체적인 예시를 통해 mirror symmetry가 어떻게 *enumerative 결과*로 실현되는지를 확인한다. 본격적인 A-model / B-model의 framework은 본 시리즈의 후속 글들에서 다룬다.

## Hori-Vafa Mirror Construction

toric variety의 경우 mirror symmetry는 매우 구체적인 형태를 띤다. Hori와 Vafa는 gauged linear sigma model (GLSM)의 T-duality를 통해 toric variety의 mirror를 체계적으로 구성하는 방법을 제시하였다. 이 construction은 toric variety의 combinatorial data로부터 직접 mirror Landau-Ginzburg model을 얻을 수 있도록 한다.

compact toric variety $$X_\Sigma$$가 charge matrix $$Q = (Q_{ij})$$를 갖는 toric variety라 하자. Hori-Vafa mirror는 algebraic torus 위에 정의되는 superpotential $$W$$로 주어진다. 구체적으로, charge matrix $$Q$$에 의해 정의되는 monomial constraint

$$\x_1^{Q_{1j}} \cdots \x_n^{Q_{nj}} = e^{t_j} \quad (1 \le j \le r)$$

를 만족하는 $$(\mathbb{C}^\ast)^n$$의 부분다양체 위에 superpotential

$$W = \x_1 + \cdots + \x_n$$

을 정의한다. 이 Landau-Ginzburg model $$(\bar{X}, W)$$가 원래 toric variety $$X_\Sigma$$의 mirror가 된다.

$$\mathbb{P}^1$$의 경우를 살펴 보자. $$\mathbb{P}^1$$은 charge matrix $$(1, 1)$$을 갖는 toric variety이므로, Hori-Vafa construction에 의해 constraint는 $$\x_0 \x_1 = q$$가 되며, 여기서 $$q = e^t$$이다. 이로부터 $$\x_0 = q / \x_1$$이고, superpotential은

$$W = \x_0 + \x_1 = \x_1 + \frac{q}{\x_1}$$

로 주어진다. 이는 $$(\mathbb{C}^\ast)^1$$ 위의 함수이며, $$\partial W / \partial \x_1 = 1 - q / \x_1^2 = 0$$으로부터 임계점은 $$\x_1 = \pm \sqrt{q}$$ 두 개가 존재한다. 이는 $$\mathbb{P}^1$$의 cohomology 차원 $$H^\ast(\mathbb{P}^1, \mathbb{C}) = \mathbb{C}^2$$과 일치함을 확인할 수 있다.

$$\mathbb{P}^2$$의 경우는 더 흥미롭다. $$\mathbb{P}^2$$의 charge matrix는 $$(1, 1, 1)$$이므로 constraint $$\x_0 \x_1 \x_2 = q$$가 주어지며, mirror domain은 $$(\mathbb{C}^\ast)^2$$이다. Constraint를 이용해 $$\x_0 = q/(\x_1 \x_2)$$로 두고 $$\z_1 = \x_1$$, $$\z_2 = \x_2$$로 좌표를 잡으면 superpotential은

$$W = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}$$

이다. 임계점 방정식

$$\frac{\partial W}{\partial \z_1} = 1 - \frac{q}{\z_1^2 \z_2} = 0, \qquad \frac{\partial W}{\partial \z_2} = 1 - \frac{q}{\z_1 \z_2^2} = 0$$

으로부터 $$\z_1 = \z_2$$를 얻고, 이를 첫 식에 대입하면 $$\z_1^3 = q$$를 얻는다. 따라서 Jacobi ring은

$$\operatorname{Jac}(W) = \mathbb{C}[\z_1^{\pm 1}, \z_2^{\pm 1}, q^{\pm 1}]\Big/\Big(\textstyle\frac{\partial W}{\partial \z_1}, \frac{\partial W}{\partial \z_2}\Big) \cong \mathbb{C}[H, q^{\pm 1}]/(H^3 - q)$$

이며 ($$H := \z_1$$로 두면 $$\z_2 = H$$, $$\z_3 = q/H^2 = H$$), 이는 $$\mathbb{P}^2$$의 small quantum cohomology ring과 동형이다:

$$QH^\ast(\mathbb{P}^2) \cong \mathbb{C}[H]/(H^3 - q).$$

이 동형에서 $$H^3$$의 classical 값은 $$0$$ ($$\operatorname{codim} > \dim$$이라 $$H^3 = 0$$)인데 양자보정으로 $$q$$를 얻는데, 이는 *$$\mathbb{P}^2$$의 두 generic 점을 지나는 유일한 직선이 존재한다*는 enumerative 사실 $$\langle [\mathrm{pt}], [\mathrm{pt}], H\rangle_{0,3,1} = 1$$에서 오는 양자 보정이다.

## 본 시리즈의 흐름

본 글에서 살펴본 Hori-Vafa의 toric mirror 처방은 *ambient toric Fano variety*의 mirror를 LG model로 명시적으로 적어주는 처방이다. 바로 이어지는 글 [§Reflexive Polytope과 Batyrev Mirror](/ko/math/mirror_symmetry/toric_geometry_batyrev)에서는 이 처방을 *toric variety 안의 Calabi-Yau hypersurface*로 확장하여, 두 reflexive polytope의 짝지음으로 Calabi-Yau mirror pair $$(X, \check{X})$$를 명시적으로 구성한다. 이후 본 시리즈는 두 stream으로 나뉜다.

**Orthodox stream (weight 1–9): A-model / B-model의 정석 framework**

A-model 측의 algebra 구조 (quantum cohomology와 WDVV) 를 manifold 차원에서 정식화하는 [§Frobenius manifold](/ko/math/mirror_symmetry/frobenius_manifold)에서 출발해, spectral parameter $$z$$를 도입한 [§Dubrovin Connection](/ko/math/mirror_symmetry/dubrovin_connection), 그 fundamental solution인 [§Givental $$J$$-function과 Mirror Theorem](/ko/math/mirror_symmetry/givental_j_function), B-model에서 짝을 이루는 [§Oscillating Integral과 Gauss–Manin System](/ko/math/mirror_symmetry/oscillating_integral), 두 측의 ring 차원 동형을 명시하는 [§Jacobi Ring과 Quantum Cohomology의 동형](/ko/math/mirror_symmetry/jacobi_ring)이 순서대로 전개된다. 이 stream의 main result는 toric Fano $$X$$와 그 Hori-Vafa mirror $$(Y, W_q)$$에 대해 A-model의 $$J$$-function이 B-model의 oscillating integral $$\int e^{W_q/z}\omega$$와 mirror map 후 일치하며, 그 동치가 두 connection의 $$D$$-module 동형으로 강화된다는 *mirror theorem*이다.

**Marsh-Rietsch stream (weight 20–25): Grassmannian 특화**

Grassmannian $$\operatorname{Gr}(k, n)$$은 toric이 아니므로 Hori-Vafa construction을 직접 적용할 수 없다. Marsh와 Rietsch는 이 경우의 mirror symmetry를 *Langlands 쌍대성*의 관점에서 해결하여, mirror가 Langlands 쌍대 Grassmannian의 anti-canonical divisor 보충집합 위 Landau-Ginzburg model이며 그 superpotential이 Plücker coordinate으로 명시적으로 표현됨을 보였다. 이 stream의 글들은 다음과 같다.

- Lie theory 측 prerequisite: [§Postnikov diagram과 plabic graph](/ko/math/mirror_symmetry/postnikov_plabic), [§Cluster algebra와 $$W_q$$의 Laurent expansion](/ko/math/mirror_symmetry/cluster_algebra)
- LG model: [§Marsh–Rietsch의 Plücker coordinate superpotential](/ko/math/mirror_symmetry/marsh_rietsch_superpotential)
- Mirror correspondence의 핵심: [§Marsh-Rietsch Mirror Theorem](/ko/math/mirror_symmetry/mr_mirror_theorem) — Plücker↔Lie superpotential 동치, critical locus와 Peterson variety의 일치, Dale Peterson 정리로 이어지는 세 단계 증명, ring 동형, $$D$$-module 동형 (Theorem 4.1), A-series conjecture의 해소
- 응용·확장: [§Cluster monomial basis와 Schubert correspondence](/ko/math/mirror_symmetry/cluster_monomial_basis), [§Newton–Okounkov body와 cluster duality](/ko/math/mirror_symmetry/newton_okounkov)

Lie theory 측 prerequisite (Bruhat decomposition, Richardson variety, Peterson variety, Kazhdan-Lusztig basis) 의 본격적 전개는 [Lie Theory 카테고리](/ko/math/lie_theory)에서 별도로 다룬다.

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[HV]** K. Hori, C. Vafa, *Mirror symmetry*, arXiv:hep-th/0002222.

**[MR]** R. J. Marsh, K. Rietsch, *The B-model connection and mirror symmetry for Grassmannians*, Adv. Math. **366** (2020), 107027, 131 pp.

**[Voi]** C. Voisin, *Mirror symmetry*, SMF/AMS Texts and Monographs **1**, 1999.
