---
title: "거울대칭 개요"
description: "초끈이론에서 유래한 거울대칭은 칼라비-야우 삼중 곡면의 켈러 구조와 복소 구조를 교환하는 Type IIA와 Type IIB의 이중성으로, 1991년 대수기하학자들이 풀지 못한 곡선 계수 문제를 물리학적 방법으로 해결한 사건을 통해 주목받았다."
excerpt: "역사적 배경과 Hori-Vafa mirror"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/overview
sidebar: 
    nav: "mirror_symmetry-ko"

date: 2026-05-18
last_modified_at: 2026-05-23
weight: 1

---

## 역사적 배경

Mirror symmetry는 수학 체계 안에서 자연스럽게 생겨난 분야가 아니라, 초끈이론을 그 기반으로 한다. 초끈이론에 따르면 우리가 살고 있는 세상은 그 기본 자유도가 *점 입자*가 아닌 *1차원 string*이라는 한 줄의 가정에서 출발한다. 그럼 입자가 시간축을 따라 움직일 때의 시공간 상에서의 궤적은 더 이상 $$1$$차원 worldline이 아니라 $$2$$차원 worldsheet가 되며, 그 운동방정식은 [\[사교기하학\] §고전역학, §§최소작용의 원리](/ko/math/symplectic_geometry/classical_mechanics#최소작용의-원리)에서와 마찬가지로 특정 한 action-minimizing solution으로 결정된다. 이 해석을 기존의 양자역학의 프레임에 일치시키기 위해서는 시공간이 $$10$$차원으로 강제되므로, 물리학자들은 이 10차원 시공간을 $$4$$차원 Minkowski 시공간과, 나머지 $$6$$차원을 해결해주는 compact manifold $$M$$의 곱으로 생각한다. 물리적으로 이 공간 $$X$$가 만족해야 하는 조건들을 써 보면, $$X$$는 *Calabi-Yau threefold*가 되어야 하는 것을 알 수 있다.

한편, 10차원 superstring에는 worldsheet가 만족해야 할 boundary 조건과 양자역학적 조건의 선택에 따라 다섯 종류의 타입으로 나뉜다. 이들 중 mirror symmetry의 직접적인 무대가 되는 것은 Type IIA와 Type IIB superstring theory로, 이들은 그 이름에서 알 수 있듯 서로 밀접한 관련이 있다. Type IIA 초끈이론은 Calabi-Yau threefold $$X$$ 위에서 Kähler structure와 complex structure를 주며, Type IIB 초끈이론은 이들 두 구조가 바뀌어 들어가며 새로운 Calabi-Yau threefold $$\check{X}$$를 정의하게 된다. 

따라서, 만일 서로 다른 두 Calabi-Yau threefold $$X$$와 $$\check{X}$$가 단일한 이론의 Type IIA/IIB로 나타나는 것들이라면, $$X$$의 Kähler structure와 $$\check{X}$$의 complex structure 사이의 관계를 줄 것이다. 이러한 쌍 $$(X, \check{X})$$를 우리는 *mirror pair*라 부르고, 이들 사이의 대칭성을 *mirror symmetry*라 한다.

이 관계는 거의 대부분 물리학자들의 직관으로 뒷받침되고, 수학적인 언어로 기술되지는 않았기 때문에 초기에는 수리물리학자들을 제외한 다른 수학자들에게는 그리 흥미로운 문제가 아니었다. 상황이 바뀐 것은 1991년 5월에 MSRI에서 열린 mirror symmetry 워크샵으로, Candelas, de la Ossa, Green, Parkes가 quintic Calabi-Yau threefold 위의 degree $$d$$ rational curve들의 개수를 mirror symmetry 가정을 통해 $$\check{X}$$에서의 계산으로 옮겨 수행해냈다. 여기에는 흥미로운 일화가 존재하는데, 처음에는 기존 대수기하학자들이 intersection theory를 통해 예측한 값과 물리학자들이 이를 통해 예측한 값이 달랐다. 이후 대수기하학자들의 코드에서 버그가 발견되었고, 이를 수정하여 재계산한 결과 물리학자들의 계산이 맞았던 것으로 판명되며 수학계에서도 mirror symmetry가 핵심적인 연구분야로 부상하게 된다. 

그러나 물리학자들의 직관은 근본적으로 양자역학의 결과들로부터 온 것이기 때문에 이를 수학적으로 formalize하는 것은 불가능했고, 이를 수학적으로 가져오기 위해서는 적당한 formalism이 필요했다. 수학자들이 보편적으로 받아들이는 정석적인 framework는 Givental formalism으로, 이는 간략히 말하자면 A-model의 불변량인 Gromov-Witten invariant들을 $$J$$-function이라는 데이터로 묶어주고, 비슷하게 B-model의 불변량인 oscillating integral을 $$I$$-function으로 묶어준다면 이들은 적절한 변수변환을 통해 서로 같다는 것이다.

우리는 이 카테고리의 글들에서 이들 A-model과 B-model을 각각 설명하고, 이를 바탕으로 mirror symmetry의 토픽들을 살펴볼 것이다. 이번 글의 나머지 부분에서는 이에 대한 motivation으로 toric variety에서의 duality를 살펴보기로 한다. 

## Hori-Vafa Mirror Construction

Toric variety ([\[토릭기하학\] §토릭 다양체의 정의, ⁋정의 3](/ko/math/toric_geometry/toric_varieties#def3))의 경우 mirror symmetry는 매우 구체적인 형태를 띄므로, 본격적인 이야기를 시작하기 전에 mirror symmetry가 어떻게 작동하는지를 이 위에서 살펴보기로 한다. 

Smooth projective toric variety $$X=X_\Sigma$$의 fan을 $$\Sigma$$, 그 1차원 cone의 primitive generator들을 $$v_1, \ldots, v_m \in \mathbb{Z}^n$$이라 하자. $$\Sigma$$가 complete fan이라면 $$v_i$$들은 $$\mathbb{R}^n$$을 span한다. 그러나 $$m>n$$이므로, 이들은 $$\mathbb{Z}$$-linearly dependent하며 따라서 이들 사이의 $$r=m-n$$개의 integral equation이 존재한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$X_\Sigma$$의 *charge matrix*는 위 ray 사이의 integral relation들

$$\sum_{i=1}^m Q_{ji}\, v_i = 0,\qquad j = 1, \ldots, r$$

의 계수로 이루어진 정수 행렬

$$Q = (Q_{ji}) \in \Mat_{r \times m}(\mathbb{Z})$$

이다.

</div>

Charge matrix는 단순히 ray 관계식의 계수를 모은 행렬이지만, $$X_\Sigma$$를 Cox construction을 통해 GIT quotient

$$X_\Sigma \;=\; \big(\mathbb{C}^m \setminus Z\big) \,\big/\!/\, (\mathbb{C}^\ast)^r$$

로 적으면 $$j$$번째 $$(\mathbb{C}^\ast)$$ factor가 Cox ring의 변수 $$\x_i$$에 weight $$Q_{ji}$$로 작용하며, 이로부터 toric variety의 기하를 결정하는 중요한 숫자들이 된다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\mathbb{P}^n$$의 ray들을

$$v_0=-e_1-\cdots-e_n,\quad v_i=e_i\qquad (i=1,\ldots, n)$$

로 적자. 이들 사이에는 유일한 관계식 $$v_0 + v_1 + \cdots + v_n = 0$$이 존재하며, 따라서 charge matrix는 $$1\times(n+1)$$ matrix

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

1. *Mirror domain* $$\check{X}$$는 algebraic torus $$(\mathbb{C}^\ast)^m$$의 submanifold로, charge matrix $$Q$$가 부여하는 $$r$$개의 restriction
    
    $$\x_1^{Q_{j1}} \cdots \x_m^{Q_{jm}} = q_j\in \mathbb{C}^\ast \qquad (j = 1, \ldots, r)$$

    을 만족하는 점들로 정의된다. 
2. $$\check{X}$$ 위의 *superpotential*은 local coordinate들의 합
    
    $$W_q : \check{X} \to \mathbb{C}, \qquad W_q(\x_1, \ldots, \x_m) = \x_1 + \x_2 + \cdots + \x_m$$
    
    으로 정의된다.

</div>

여기서 $$q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$$은 mirror LG model의 complex structure를 담는 변수이다. Mirror domain $$\check{X}$$ 자체의 complex structure는 항상 같은 affine torus $$(\mathbb{C}^\ast)^n$$이지만, 그 위에 얹는 superpotential $$W_q$$가 $$q$$에 의해 결정된다. 즉, 한 $$q$$ 값마다 하나의 LG model $$(\check{X}, W_q)$$가 유일하게 결정되며, 이 family $$\{(\check{X}, W_q)\}_q$$ 전체가 $$X_\Sigma$$의 mirror로 등장한다는 것이 더 맞는 말이다. 이 때 complex structure $$q$$는 A-model에서는 Novikov parameter $$q$$로 등장한다.

우리는 앞서 mirror symmetry를 complex structure와 symplectic structure의 대칭으로 설명하였는데, 위에서 설명한 Novikov parameter가 바로 symplectic structure를 담고 있다. 구체적으로, 우리는 compact Kähler manifold $$X$$가 주어졌을 때 그 *Kähler form* $$\omega\in H^2(X, \mathbb{R})$$를 $$X$$의 symplectic form으로 정의한다. 이는 real form이 되어 moduli space를 생각하는 것이 다소 귀찮으므로, $$B\in H^2(X, \mathbb{R})$$을 택하여 *complexified Kähler class*

$$t = B + i\omega \in H^2(X, \mathbb{C})$$

를 만든다. 이는 직관적으로 Kähler form $$\omega$$를 복소방향으로 채워 complexification을 하는 것이며, 물리적으로는 초끈이론에 등장하는 $$B$$-field를 의미한다. 이제 Novikov parameter는 바로 이 $$t$$를 지수화한 것으로, curve class $$\beta_0 \in H_2(X)$$에 대해

$$q^{\beta_0} = e^{2\pi i \int_{\beta_0} t} = e^{2\pi i \int_{\beta_0} B}\, e^{-2\pi \int_{\beta_0} \omega}$$

로 주어진다. 그럼 $$q^{\beta_0}$$의 크기 $$\lvert q^{\beta_0}\rvert = e^{-2\pi \int_{\beta_0} \omega}$$는 곡선 class $$\beta_0$$의 *symplectic volume* $$\int_{\beta_0} \omega$$를, phase $$\arg q^{\beta_0} = 2\pi \int_{\beta_0} B$$는 $$B$$-field를 담는다. 따라서 symplectic volume이 $$0$$으로 가는 상황에서는 $$q$$의 크기가 $$1$$로 가서 양자적인 효과가 full로 나타나며, 반대로 symplectic volume이 무한대로 가는 상황에서는 $$q$$의 크기가 $$0$$으로 가서 양자적인 효과가 사라진다. 

이제 위의 계산에서, $$q$$ 하나를 정하는 것은 complexified Kähler class $$t$$를 결정하는 것, 즉 $$B$$-field와 $$\omega$$를 각각 정해주는 것과 같다. 그럼 위의 식으로부터 $$B$$는 $$2\pi$$만큼의 주기를 가지고, $$\omega$$는 $$B$$가 정해주는 방향의 반지름을 정해주므로 $$q$$의 moduli space (혹은 $$t$$의 moduli space)는 $$r=\dim_\mathbb{R} H^2(X, \mathbb{R})$$인 algebraic torus $$(\mathbb{C}^\ast)^r$$가 된다. 다만 $$\omega$$는 Kähler form이라 *Kähler cone* 안에 있어야 하므로 (effective curve class $$\beta_0$$에 대해 $$\int_{\beta_0} \omega > 0$$, 곧 $$\lvert q^{\beta_0}\rvert < 1$$), 엄밀히는 moduli가 이 torus 전체가 아니라 $$q = 0$$인 large volume limit 근방의 열린 영역이고, $$(\mathbb{C}^\ast)^r$$은 이를 품는 ambient algebraic torus이다. 

B-side에서의 $$q$$는 위에서 살펴봤듯 superpotential의 계수로 나타났다. 직관적으로 이를 통해 얻어지는 critical point의 방정식이 $$\x^k=q$$ 꼴인 경우를 생각하면, $$\x^k=q$$의 해, 즉 critical point는 $$q$$가 $$0$$으로 갈 때 한 점으로 degenerate하고, 나머지 경우에는 적당히 분리되어 있는 singularity가 나온다. 

이제 mirror symmetry statement를 잘 적기 위해서는 $$X$$의 (small) *quantum cohomology*를 정의해야 한다. 구체적으로, $$X$$의 symplectic structure와 complex structure를 살펴볼 때 필요한 도구 중 하나는 $$J$$-holomorphic curve들이다. 이들을 이용하면, $$X$$의 cohomology $$H^\ast(X, \mathbb{C})$$ 위에 다음의 식

$$\alpha \star_q \beta \;=\; \alpha \smile \beta + \sum_{\beta_0} q^{\beta_0} \sum_\gamma \langle \alpha, \beta, \gamma^\vee \rangle_{0, 3, \beta_0}\, \gamma$$

으로 *quantum cup product*를 정의할 수 있고, 이 구조가 $$X$$의 (small) *quantum cohomology* $$QH^\ast(X)$$를 준다. 직관적으로, 위의 식에서 $$\alpha\smile \beta$$가 두 class $$\alpha, \beta$$의 intersection에 대한 정보를 담는다면, 그 뒤의 항들은 이 intersection이 실제로 일어나지 않고, curve class $$\beta_0$$을 매개로 만나는 "quantum" intersection들을 함께 고려하는 것이다. 

이제 mirror symmetry statement는

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

임을 주장한다. 이 statement는 여러 면에서 기존에 우리가 알고 있던 그림과 맞아떨어지는데, 가령 $$q\rightarrow 0$$인 *classical limit*에서 quantum cohomology ring은 classical cohomology ring으로 돌아가며 이는 $$\Jac(W_q)$$에서 보면 singularity들이 뭉쳐서 degenerate하는 non-reduced singularity를 만드는 것과 같다. 혹은, 거꾸로 말하면, 양자효과를 도입하는 것은 A-side에서는 classical cohomology를 Novikov variable $$q$$를 사용하여 풀어주는 것으로, B-side에서는 뭉쳐있던 singularity를 펴주는 것으로 각각 생각할 수 있다. 

일반적으로 위 isomorphism 우변의 $$QH^\ast(X_\Sigma)$$를 살펴보는 것은 주어진 class들을 동시에 지나는 curve를 세는 것으로, 상대적으로 복잡하고 어려운 일로 여겨지지만 mirror symmetry는 이를 단순한 ring의 계산으로 환원시킨다. 단순한 두 경우 $$\mathbb{P}^1$$, $$\mathbb{P}^2$$에서 이것이 실제로 성립함을 확인하자. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$\mathbb{P}^1$$ case)**</ins> [예시 2](#ex2)에서 본 $$\mathbb{P}^1$$의 charge matrix는 $$Q = (1, 1)$$임을 확인하였다. 따라서 Hori-Vafa mirror의 domain $$\check{X}$$은 다음의 식

$$\x_0 \x_1 = q$$

을 만족하는 $$(\mathbb{C}^\ast)^2$$의 submanifold이다. 이 위에서는 $$\x_0 = q/\x_1$$이므로, superpotential은

$$W_q(\x_1) = \x_1 + \frac{q}{\x_1}$$

으로 적을 수 있으며 그 critical point들은

$$\partial_{\x_1} W_q = 1 - \frac{q}{\x_1^2} = 0$$

의 해, 즉 두 점 $$\x_1 = \pm\sqrt{q}$$이다. 이로부터 Jacobi ring은

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, q^\pm] / (\partial_{\x_1} W_q) \;\cong\; \mathbb{C}[H, q^\pm]/(H^2 - q),\qquad H := \x_1$$

으로 주어지는 것을 확인할 수 있다.

한편 A-side의 small quantum cohomology는 간단한데, 세 점을 지나는 $$\mathbb{P}^1$$은 오직 하나만 존재하므로 $$\langle H, H, H \rangle_{0,3,1}^{\mathbb{P}^1} = 1$$이며 classical cup product $$H\smile H$$는 차원 문제로 $$0$$이 된다. 즉, quantum cup product는 $$H \star_q H = q$$가 되며, 이로부터 quantum cohomology는 graded $$\mathbb{C}[q]$$-polynomial algebra

$$QH^\ast(\mathbb{P}^1) = \mathbb{C}[H, q] \big/ (H^2 - q), \qquad \deg H = 2,\;\; \deg q = 4$$

가 된다. 이제 grading을 잊고 $$q$$를 invertible로 두면 위의 Jacobi ring과 정확히 같은 $$\mathbb{C}$$-algebra가 되는 것을 확인할 수 있다.

</div>

조금 더 복잡한 예시로 $$\mathbb{P}^2$$를 보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($$\mathbb{P}^2$$ case)**</ins> $$\mathbb{P}^2$$의 mirror dual은 다음의 식

$$\x_0 \x_1 \x_2 = q$$

을 만족하는 것이며 superpotential은 

$$W_q(\z_1, \z_2) = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}$$

로 주어진다. 이제 Critical point는 

$$\partial_{\z_1} W_q = 1 - \frac{q}{\z_1^2 \z_2} = 0, \qquad \partial_{\z_2} W_q = 1 - \frac{q}{\z_1 \z_2^2} = 0$$

을 풀어 얻어지며, 그 해는 $$\z_1=\z_2$$, $$\z_1^3=q$$를 만족하는 세 점으로 주어진다. 이제 Jacobi ring을 명시적으로 계산하면

$$\Jac(W_q) = \mathbb{C}[\z_1^\pm, \z_2^\pm, q^\pm] \big/ (\partial_{\z_1} W_q, \partial_{\z_2} W_q) \;\cong\; \mathbb{C}[H, q^\pm]/(H^3 - q)$$

이다.

한편, A-model에서 quantum cohomology를 계산하기 위해서는 다음의 Gromov-Witten invariant

$$\langle H, H^2, H^2 \rangle_{0,3,1}^{\mathbb{P}^2} = 1$$

를 사용하면 된다. 기하적으로 이는 (i) 두 generic 점 $$P_1, P_2 \in \mathbb{P}^2$$를 지나는 $$\mathbb{P}^1 \subset \mathbb{P}^2$$가 유일하게 존재하고, (ii) 이 직선이 generic line $$H_1 \subset \mathbb{P}^2$$과 정확히 한 점에서 만나며, (iii) 이를 통해 얻어지는 세 점이  $$f : \mathbb{P}^1 \xrightarrow{\sim} L$$을 유일하게 결정한다는 사실을 반영한다. 이를 통해 quantum cohomology가 graded $$\mathbb{C}[q]$$-polynomial algebra

$$QH^\ast(\mathbb{P}^2) = \mathbb{C}[H, q] \big/ (H^3 - q), \qquad \deg H = 2,\;\; \deg q = 6$$

로 결정되는 것을 안다. 이 경우에도 우리가 기대하던 isomorphism이 잘 작동하는 것을 확인할 수 있다.

</div>

더 일반적으로, 위의 두 예시는 임의의 smooth projective toric Fano variety에 대해서 성립한다. 우리는 다음 글에서 이를 toric variety 안의 Calabi-Yau hypersurface로 확장하는 Batyrev mirror를 살펴볼 것이다. 

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
