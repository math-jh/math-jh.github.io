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

우리는 이 카테고리의 글들에서 이들 A-model과 B-model을 각각 설명하고, 이를 바탕으로 mirror symmetry의 토픽들을 살펴볼 것이다. 이번 글의 나머지 부분에서는 이에 대한 motivation으로 toric variety에서의 duality를 살펴보기로 한다. 

## Hori-Vafa Mirror Construction

Toric variety ([\[토릭 기하학\] §토릭 다양체의 정의, ⁋정의 3](/ko/math/toric_geometry/toric_varieties#def3))의 경우 mirror symmetry는 매우 구체적인 형태를 띄므로, 본격적인 이야기를 시작하기 전에 mirror symmetry가 어떻게 작동하는지를 이 위에서 살펴보기로 한다. 

Smooth projective toric variety $$X=X_\Sigma$$의 fan을 $$\Sigma$$, 그 1차원 cone의 primitive generator들을 $$v_1, \ldots, v_N \in N \cong \mathbb{Z}^n$$이라 하자. $$\Sigma$$가 complete fan이라면 $$v_i$$들은 $$N_\mathbb{R}$$을 span한다. 그러나 $$N>n$$이므로, 이들은 $$\mathbb{Z}$$-linearly indepenent하며 따라서 이들 사이의 $$r=N-n$$개의 integral equation이 존재한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$X_\Sigma$$의 *charge matrix*는 위 ray 사이의 integral relation들

$$\sum_{i=1}^N Q_{ji}\, v_i = 0,\qquad j = 1, \ldots, r$$

의 계수로 이루어진 정수 행렬

$$Q = (Q_{ji}) \in \Mat_{r \times N}(\mathbb{Z})$$

이다.

</div>

Charge matrix는 단순히 ray 관계식의 계수를 모은 행렬이지만, $$X_\Sigma$$를 Cox construction을 통해 GIT quotient

$$X_\Sigma \;=\; \big(\mathbb{C}^N \setminus Z\big) \,\big/\!/\, (\mathbb{C}^\ast)^r$$

로 적으면 $$j$$번째 $$(\mathbb{C}^\ast)$$ factor가 Cox ring의 변수 $$\x_i$$에 weight $$Q_{ji}$$로 작용하며, 이로부터 toric variety의 기하를 결정하는 중요한 숫자들이 된다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{P}^n$$의 ray들을

$$v_0=-e_1-\cdots-e_n,\quad v_i=e_i\qquad (i=1,\ldots, n)$$

로 적자. 이들 사이에는 유일한 관계식 $$v_0 + v_1 + \cdots + v_n = 0$$이 존재하며, 따라서 charge matrix는 $$1\times(n+1) matrix$$

$$Q = (1,\, 1,\, \ldots,\, 1) \in \Mat_{1 \times (n+1)}(\mathbb{Z}).$$

로 주어진다. 위의 설명에 따르면, 이는 $$\mathbb{P}^n$$ 위에 정의된 torus의 standard scaling action 

$$t\cdot(\x_0,\ldots, \x_n)=(t \x_0, \ldots, t \x_n)$$

의 정보를 담고 있는 것이다.

조금 nontrivial한 예시로 $$\mathbb{P}^1\times \mathbb{P}^1$$을 보자. 이들의 ray들은 $$(\pm 1, 0)$$, $$(0, \pm 1)$$로 주어지며, 그 관계식은 $$(1,0)+(-1,0)=0$$과 $$(0,1)+(0,-1)=0$$ 두 개이므로 charge matrix는

$$Q = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}$$

가 된다. 이는 torus가 앞선 factor와 나중 factor $$\mathbb{P}^1$$ 각각에 standard scaling action으로 작용한다는 정보를 담고 있다. 

</div>

Mirror symmetry의 관점에서 charge matrix는 $$B$$-model의 데이터를 담고 있다. 다소 주의할 것은 현재 우리가 다루고 있는 상황은 도입부에서 설명한 Calabi-Yau manifold보다 일반적인 상황이라는 사실이다. 일반적으로 smooth projective toric variety $$X_\Sigma$$는 Calabi-Yau가 아니라 Fano variety로 주어지며, 이 경우 $$X_\Sigma$$의 mirror dual은 Calabi-Yau가 아니라 *Landau-Ginzburg model*로 표현된다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> *Landau-Ginzburg model<sub>란다우-긴즈부르크 모델</sub>*은 complex manifold $$\check{X}$$와 그 위에 정의된 holomorphic function $$W : \check{X} \to \mathbb{C}$$의 쌍 $$(\check{X}, W)$$로 주어진다. 이 때, $$W$$를 *superpotential*이라 부른다.

</div>

이번 글의 목적은 mirror symmetry의 개념들을 본격적으로 정의하기 전에 가벼운 계산을 통해 이 현상을 살펴보는 것이다. 따라서 우리는 양쪽의 데이터를 정확하게 설명하는 대신, 간략한 아이디어와 직관으로 이를 대체한다. 우선 $$B$$-model 측면에서, charge matrix는 *Jacobi ring* $$\Jac(W_q)$$를 정의하며 이는 앞서 언급한 oscillating integral의 classical limit으로 볼 수 있다. 주어진 Landau-Ginzburg model $$(\check{X}, W)$$에 대하여, 이것의 Jacobi ring은 그 정의에 의해

$$\Jac(W) = \frac{\mathcal{O}(\check{X})}{(\partial_1 W, \ldots, \partial_n W)}$$

으로 주어진다. 여기서 $$\x_1, \ldots, \x_n$$들은 $$\check{X}$$의 local coordinate이며 $$\partial_i$$들은 이에 대한 partial derivative들이다. 기하학적으로 $$\Jac(W)$$는 $$W$$의 *critical scheme* $$\Crit(W) = \{dW = 0\} \subset \check{X}$$의 coordinate ring이다. 그럼 [정의 4](#def4)의 Hori-Vafa mirror의 Jacobi ring이 원래의 A-side model의 데이터를 복원한다는 것이 mirror symmetry statement이다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Smooth projective toric Fano variety $$X_\Sigma$$와 추가적인 데이터 $$q=(q_1,\ldots, q_r)\in \mathbb{C}^r$$에 대하여, 이것이 정의하는 *Hori-Vafa mirror*는 다음의 Landau-Ginzburg model을 의미한다.

1. *Mirror domain* $$\check{X}$$는 algebraic torus $$(\mathbb{C}^\ast)^N$$의 부분다양체로, charge matrix $$Q$$가 부여하는 $$r$$개의 restriction
    
    $$\x_1^{Q_{j1}} \cdots \x_N^{Q_{jN}} = q_j\in \mathbb{C}^\ast \qquad (j = 1, \ldots, r)$$

    을 만족하는 점들로 정의된다. 
2. $$\check{X}$$ 위의 *superpotential*은 local coordinate들의 합
    
    $$W_q : \check{X} \to \mathbb{C}, \qquad W_q(\x_1, \ldots, \x_N) = \x_1 + \x_2 + \cdots + \x_N$$
    
    으로 정의된다.

</div>

여기서 $$q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$$은 mirror LG model의 complex structure를 담는 변수이다. Mirror domain $$\check{X}$$ 자체의 complex structure는 항상 같은 affine torus $$(\mathbb{C}^\ast)^n$$이지만, 그 위에 얹는 superpotential $$W_q$$가 $$q$$에 의해 결정된다. 즉, 한 $$q$$ 값마다 하나의 LG model $$(\check{X}, W_q)$$가 유일하게 결정되며, 이 family $$\{(\check{X}, W_q)\}_q$$ 전체가 $$X_\Sigma$$의 mirror로 등장한다는 것이 더 맞는 말이다. 이 때 complex structure $$q$$는 A-model에서는 Novikov parameter $$q$$로 등장한다. 

이제 mirror symmetry statement를 적기 위해서는 $$X$$의 (small) *quantum cohomology*를 정의해야 한다. 구체적으로, $$X$$의 symplectic structure와 complex structure를 살펴볼 때 필요한 도구 중 하나는 $$J$$-holomorphic curve들이다. 이들을 이용하면, $$X$$의 cohomology $$H^\ast(X, \mathbb{C})$$ 위에 다음의 식

$$\alpha \star_q \beta \;=\; \alpha \smile \beta + \sum_{\beta_0} q^{\beta_0} \sum_\gamma \langle \alpha, \beta, \gamma^\vee \rangle_{0, 3, \beta_0}\, \gamma$$

으로 *quantum cup product*를 정의할 수 있고, 이 구조가 $$X$$의 (small) *quantum cohomology* $$QH^\ast(X)$$를 준다. 직관적으로, 위의 식에서 $$\alpha\smile \beta$$가 두 class $$\alpha, \beta$$의 intersection에 대한 정보를 담는다면, 그 뒤의 항들은 이 intersection이 실제로 일어나지 않고, curve class $$\beta_0$$을 매개로 만나는 "quantum" intersection들을 함께 고려하는 것이다. 

이제 mirror symmetry statement는

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

임을 주장한다. 단순한 두 경우 $$\mathbb{P}^1$$, $$\mathbb{P}^2$$에서 이것이 실제로 성립함을 확인하자. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$\mathbb{P}^1$$)**</ins> [예시 2](#ex2)에서 본 $$\mathbb{P}^1$$의 charge matrix는 $$Q = (1, 1)$$이므로 [정의 4](#def4)의 constraint는

$$\x_0 \x_1 = q$$

이며 ($$q = e^t$$), 이로부터 $$\x_0 = q/\x_1$$로 풀린다. Superpotential은

$$W_q(\x_1) = \x_1 + \frac{q}{\x_1}$$

이고, 그 임계점은 $$\partial_{\x_1} W_q = 1 - q/\x_1^2 = 0$$, 즉 $$\x_1 = \pm\sqrt{q}$$의 두 점이다. 임계점의 개수 $$2$$가 정확히 $$\dim_\mathbb{C} H^\ast(\mathbb{P}^1, \mathbb{C}) = 2$$와 일치하며, 더 나아가 Jacobi ring은

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, q^\pm] / (\partial_{\x_1} W_q) \;\cong\; \mathbb{C}[H, q^\pm]/(H^2 - q),\qquad H := \x_1$$

이 되어 $$\mathbb{P}^1$$의 small quantum cohomology $$QH^\ast(\mathbb{P}^1) \cong \mathbb{C}[H]/(H^2 - q)$$와 일치한다. Quantum 보정 $$H^2 = q$$는 *$$\mathbb{P}^1$$의 한 점을 지나는 유일한 직선이 자기 자신*이라는 고전 enumerative 사실 $$\langle [\mathrm{pt}], [\mathrm{pt}] \rangle_{0,2,1} = 1$$에서 비롯된다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6** ($$\mathbb{P}^2$$의 Hori-Vafa mirror)</ins> $$\mathbb{P}^2$$의 charge matrix는 $$Q = (1, 1, 1)$$이므로 constraint는

$$\x_0 \x_1 \x_2 = q.$$

$$\x_0 = q/(\x_1 \x_2)$$로 풀어 $$\z_1 = \x_1$$, $$\z_2 = \x_2$$로 좌표를 잡으면

$$W_q(\z_1, \z_2) = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}$$

이며, 이는 $$(\mathbb{C}^\ast)^2$$ 위의 Laurent polynomial이다. 임계점 방정식

$$\partial_{\z_1} W_q = 1 - \frac{q}{\z_1^2 \z_2} = 0, \qquad \partial_{\z_2} W_q = 1 - \frac{q}{\z_1 \z_2^2} = 0$$

으로부터 $$\z_1 = \z_2$$, 그리고 $$\z_1^3 = q$$를 얻으므로 임계점은 세 개 ($$\dim_\mathbb{C} H^\ast(\mathbb{P}^2, \mathbb{C}) = 3$$과 일치). Jacobi ring을 명시적으로 계산하면

$$\Jac(W_q) = \mathbb{C}[\z_1^\pm, \z_2^\pm, q^\pm] \big/ (\partial_{\z_1} W_q, \partial_{\z_2} W_q) \;\cong\; \mathbb{C}[H, q^\pm]/(H^3 - q)$$

이며 ($$H := \z_1$$로 두면 critical equation에서 $$\z_2 = H$$이고, constraint로부터 $$\x_0 = q/H^2 = H$$), 이는 $$\mathbb{P}^2$$의 small quantum cohomology

$$QH^\ast(\mathbb{P}^2) \cong \mathbb{C}[H]/(H^3 - q)$$

와 정확히 일치한다. 이 동형에서 $$H^3$$의 classical 값은 $$0$$ ($$\codim\, [H]^3 > \dim_\mathbb{C} \mathbb{P}^2$$이므로 $$H^3 = 0$$) 이지만, quantum 보정 $$H^3 = q$$는 *$$\mathbb{P}^2$$의 두 generic 점을 지나는 유일한 직선이 존재한다*는 enumerative 사실 $$\langle [\mathrm{pt}], [\mathrm{pt}], H\rangle_{0,3,1} = 1$$에서 비롯된다.

</div>

두 예시에서 본 동형 $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$은 일반 smooth projective toric Fano variety에 대해 성립한다 (Batyrev 1993, Givental 1996). 바로 이어지는 글 [§Reflexive Polytope과 Batyrev Mirror](/ko/math/mirror_symmetry/toric_geometry_batyrev)에서는 본 글에서 살펴본 *ambient toric Fano variety*의 Hori-Vafa mirror 처방을 *toric variety 안의 Calabi-Yau hypersurface*로 확장하여, 두 reflexive polytope의 짝지음으로 Calabi-Yau mirror pair $$(X, \check{X})$$를 명시적으로 구성한다.

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[HV]** K. Hori, C. Vafa, *Mirror symmetry*, arXiv:hep-th/0002222.
