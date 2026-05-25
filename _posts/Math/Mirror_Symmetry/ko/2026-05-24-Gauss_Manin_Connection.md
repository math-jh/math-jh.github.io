---
title: "가우스-마닌 접속"
excerpt: "B-model의 D-module 구조와 oscillating integral, 그리고 cohomology 위의 Gauss-Manin connection"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/gauss-manin_connection
sidebar: 
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Oscillating_Integral.png
    overlay_filter: 0.5

date: 2026-05-24
last_modified_at: 2026-05-26ㅇㅋ 
weight: 5
published: false
---

이번 글에서 우리는 [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)에서 주장한 $$D$$-module isomorphism을 구체적으로 살펴본다. 이를 위해서는 A-side와 B-side 모두를 보아야 한다. A-side의 경우는 이미 [\[사교기하학\] §양자 코호몰로지, ⁋정의 7](/ko/math/symplectic_geometry/quantum_cohomology#def7)에서 어느정도 다룬 것이므로, 우리는 우선 B-side, 즉 oscillating integral과 Gauss-Manin system에 대해 살펴본다. 

## Landau-Ginzburg model과 volume form

우선 우리는 B-model의 무대를 만들어야 한다. [§거울대칭 개요, ⁋정의 4](/ko/math/mirror_symmetry/overview#def4)에서 살펴보았듯, Landau-Ginzburg model $$(\check{X}, W_q)$$에서 $$\check{X}$$는 보통 algebraic torus $$(\mathbb{C}^\ast)^N$$ 혹은 그 안에 있는 subvariety이며, $$W_q$$는 $$q$$로 parametrize되는 holomorphic function이다. 우리는 이 위에 oscillating integral을 정의하기 위해 우선 holomorphic volume form $$\omega$$를 정의한다.

즉 우리의 $$\omega$$는 $$\check{X}$$ 위에서 영점도, pole도 가지지 않아야 한다. 일반적으로 이는 compact (대수기하학에서는 complete) 공간에서는 불가능한 일이었던 것을 기억하자. 이를 위해 우리는 이러한 점들을 임의로 제거해준다. 즉, $$\check{X}$$를 어떤 smooth projective variety $$Y$$의 open subset $$\check{X} = Y \setminus D$$로 본 후, $$Y$$의 divisor $$D$$를 $$\mathcal{K}_Y$$의 rational section의 bad locus를 정확히 흡수하는 divisor로 고르는 것이다. 구체적으로 anti-canonical class $$-K_Y$$의 effective representative $$D \geq 0$$ (즉 $$D \sim -K_Y$$)를 잡으면 $$\mathcal{K}_Y \otimes \mathcal{O}_Y(D) \cong \mathcal{O}_Y$$가 trivial이 되어 nowhere-vanishing global section

$$\Omega\in H^0(Y, \mathcal{K}_Y\otimes \mathcal{O}_Y(D))$$

가 존재하며, $$\Omega$$를 $$\mathcal{K}_Y$$의 rational section으로 보면 $$\divisor(\Omega)=-D$$가 되어, $$\omega=\Omega\vert_{\check{X}}$$가 정확히 우리가 원하는 volume form의 역할을 해 준다. 이는 smooth complete toric variety에서 anti-canonical divisor에 해당하는 boundary divisor $$D=\sum_\rho D_\rho$$를 뺀 후 거기에서의 canonical volume form

$$\omega = d\log \rchi^{m_1} \wedge \cdots \wedge d\log \rchi^{m_N}$$

을 만드는 구성[^1]의 일반화이다. 한편 이 구성이 작동하는 ambient 데이터 $$(Y, D)$$ 자체를 추상화하면 다음 정의의 log Calabi-Yau pair가 된다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective variety $$Y$$와 reduced SNC divisor ([\[토릭 기하학\] §토릭 다양체 위의 로그 미분형식, ⁋정의 5](/ko/math/toric_geometry/logarithmic_differentials#def5)) $$D \subset Y$$의 쌍 $$(Y, D)$$가 $$K_Y + D \sim 0$$을 만족할 때 이를 *log Calabi-Yau pair*라 부른다. 이 때, 위의 construction을 통해 얻어지는 non-vanihsing volume form $$\omega=\Omega\vert_{\check{X}}$$을 log CY pair의 *canonical holomorphic volume form*이라 부른다. 

</div>

기하적으로, 앞선 construction에서 $$\mathcal{K}_Y\otimes \mathcal{O}_Y(D)\cong \mathcal{O}_Y$$의 nowhere-vanishing global section을 통해 $$\omega$$를 택하는 것은 trivialization $$\Omega^N_Y(\log D)\cong\mathcal{O}_Y$$를 택하는 것과 같다. 특히 $$\check{X}=(\mathbb{C}^\ast)^N$$인 경우 standard affine coordinate들 $$\x_i$$에 대한 canonical volume form은

$$\omega = \frac{d\x_1 \wedge \cdots \wedge d\x_N}{\x_1 \cdots \x_N} = d\log \x_1 \wedge \cdots \wedge d\log \x_N$$

이다.

## Lefschetz thimble

Oscillating integral은 정직한 적분으로, 실제로 존재하는 적분경로를 따라 실제 함수를 적분하여 얻어진다. 구체적으로, superpotential $$W_q$$는 *Lefschetz thimble*이라 불리는 경로 $$\Gamma$$를 따라 다음의 *oscillating integral*

$$\mathcal{I}_\Gamma(q,z)=\int_\Gamma e^{W_q/z}\omega$$

으로 정의된다. 여기서 $$\omega$$는 위에서 정의한 $$\check{X}$$ 위의 volume form이며 $$q$$는 $$W_q$$를 parametrize하는 quantum parameter이고 $$z$$는 Dubrovin connection에서와 마찬가지로 $$z\rightarrow 0$$인 곳과 그렇지 않은 곳을 이어주는 spectral parameter이다. 여기서는 우선 $$z$$는 적당히 고정된 것으로 생각하면, 위의 적분이 잘 정의되기 위해서는 적분경로 $$\Gamma$$를 따를 때 지수에 있는 $$W_q/z$$가 $$-\infty$$로 가며 사라져주어야 한다. 

이를 위해 우리는 각각의 점 $$p\in \Crit(W_q)$$에 대하여 다음의 꼴

$$\Gamma_p := \left\{ x \in \check{X} \,\middle\vert\, \lim_{t \to +\infty} \Real\!\left(\frac{W_q(x(t))}{z}\right) = -\infty,\; x(0) = p \right\}$$

로 나타나는 cycle을 *Lefschetz thimble*이라 부른다. 만일 $$W_q$$가 Morse type이라면 $$\Gamma_p$$는 real dimension $$N$$의 cycle을 이룬다는 것이 알려져 있다 ([\[사교기하학\] §Morse 이론과 stationary phase 근사, ⁋정의 14](/ko/math/symplectic_geometry/morse_stationary_phase#def14)). 한편 [§거울대칭 개요](/ko/math/mirror_symmetry/overview)에서 살펴본 ring 동형 $$\Jac(W_q) \cong QH^\ast(X)$$로부터 critical point의 개수는 정확히 $$\dim_\mathbb{C} H^\ast(X, \mathbb{C})$$와 일치한다. 이 critical point에 대응하는 Lefschetz thimble들 $$\{\Gamma_p\}_{p \in \Crit(W_q)}$$는 *$$N$$th rapid decay homology*

$$H_N(\check{X}, \{\Real(W_q/z) \ll 0\}; \mathbb{C})$$

의 $$\mathbb{C}$$-basis가 된다. 여기서 rapid decay cohomology $$H_\ast(\check{X}, \{\Real(W_q/z) \ll 0\}; \mathbb{C})$$는 충분히 작은 $$\Real(W_q/z)$$를 갖는 점들로 이루어진 *rapid decay zone*

$$S_z=\{x \in \check{X} : \Real(W(x)/z) \ll 0\}$$

에 사는 chain들을 같은 것으로 보고, $$n$$-chain $$\sigma$$들을 이 rapid decay zone 안에 들어가는 것들만 모은 것이다. 더 엄밀하게는

$$S_z^M=\{x \in \check{X} : \Real(W(x)/z) <-M\}$$

으로 두고, relative singular homology $$H_n(\check{X}, S_z^M; \mathbb{C})$$을 생각한 것으로, $$S_z^M$$ 등은 물론 $$M$$의 값에 의존하지만 이 relative homology 자체는 $$M$$의 값이 커지면 stabilize한다는 것이 알려져 있다. 우리는 이 stabilize한 값을 rapid decay homology로 정의하는 것이다. 

이 식으로부터 $$z$$의 역할도 어느정도 보이는데, $$z\rightarrow 0$$인 경우 $$e^{W_q/z}$$는 $$W_q$$의 phase에 따라 급격히 진동하며, 따라서 적분의 dominant한 contribution은 stationary phase, 즉 $$p$$ 근처에서만 나타나게 된다. 우리는 mirror symmetry statement가 B-side에서는 $$W_q$$의 critical point에 대한 것임을 알고 있으므로 $$z$$의 역할은 명확하다. 

다만 주의할 것은 $$z$$가 실제로는 real parameter가 아니라 complex parameter라는 것이다. 실제로 만일 $$z$$의 argument가 변한다면 $$W_q$$ 또한 해당 방향에 맞춰서 정렬되어야 real part가 될 것이므로 위의 $$\Gamma_p$$의 정의가 살짝 달라질 것이다. 이렇게 $$z$$를 변경할 때는 Lefschetz thimble이 정의하는 basis 자체가 달라지게 되며, 이는 (해당 글에서 명시적으로 언급하지는 않았지만) A-side의 Dubrovin connection에 대해서도 마찬가지이다. 즉, $$\nabla^z$$들 또한 $$z$$가 달라질 때에는 그 값이 달라질 것이지만, 우리가 주목하지 않았던 것일 뿐이며 이를 $$\mathbb{C}^\ast$$에서 살펴보면 더 풍부한 구조가 드러난다. 요컨대 $$z \to 0^+$$의 stationary phase asymptote를 보는 것은 이 구조의 한 단면일 뿐으로, 우리는 이들이 담고 있는 데이터를 $$\mathbb{C}^\ast$$ 전체로 유지할 것이다. 

지금까지의 논의를 정리하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Landau-Ginzburg model $$(\check{X}, W_q)$$와 그 위에 정의된 holomorphic volume form $$\omega$$을 생각하자. 고정된 Lefschetz thimble $$\Gamma_p$$에 대하여, 이를 따르는 *oscillating integral*을

$$\mathcal{I}_{\Gamma_p}(q, z) := \int_{\Gamma_p} e^{W_q / z}\, \omega$$

으로 정의한다. 여기서 $$\Gamma_p$$는 $$q$$와 $$z$$의 변화에 따라 continuously isotoped될 수 있는 Lefschetz thimble로 선택된다.

</div>

여기서 $$\Gamma_p$$를 $$(q,z)$$의 변화에 따라 continuously isotoped 될 수 있도록 택하는 것은 $$(q,z)$$의 변화에 따라 critical point가 변하고, 따라서 thimble 또한 변형되는데 그 변형 정도가 연속이도록 해 주는 것이다. 즉 parameter $$(q,z)$$의 변화에 따라 cycle을 parallel하게 transport하는 것이며, 이것이 곧 정의할 Gauss-Manin connection의 base를 주게 된다. 

위에서 언급했듯, $$e^{W_q/z}$$는 $$W_q$$의 phase에 따라 급격히 진동하므로, 적분의 dominant contribution은 phase가 stationary한 점, 즉 critical point 근처에서만 발생한다. 다음 명제는 [\[사교기하학\] §Morse 이론과 stationary phase 근사, ⁋명제 16](/ko/math/symplectic_geometry/morse_stationary_phase#prop16)을 우리 세팅에 맞추어 다시 적어둔 것이다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Stationary phase asymptotic)**</ins> $$W_q$$의 non-degenerate critical point $$p$$와 이를 통과하는 Lefschetz thimble $$\Gamma_p$$에 대해, $$z \to 0^+$$에서

$$\mathcal{I}_{\Gamma_p}(q, z) \sim (2\pi z)^{N/2}\, \frac{e^{W_q(p)/z}}{\sqrt{\det\,\Hess_p(W_q)}}\, \big(1 + O(z)\big)$$

이 성립한다. 여기서 $$N = \dim_\mathbb{C} \check{X}$$, $$\Hess_p$$는 $$p$$에서의 Hessian이며, $$\sqrt{}$$의 branch는 $$\Gamma_p$$의 orientation으로 결정된다.

</div>

증명의 핵심은 $$p$$ 근방에서 [\[사교기하학\] §Morse 이론과 stationary phase 근사, ⁋정리 6](/ko/math/symplectic_geometry/morse_stationary_phase#thm6)을 사용하여 $$W_q$$를 quadratic form으로 환원한 뒤 Gaussian 적분을 적용하는 것이다. 어쨌든 우리 상황에서 중요한 것은 $$z \to 0^+$$일 때 oscillating integral이 *각 critical point의 local data*, 즉 critical value $$W_q(p)$$와 Hessian determinant로 완전히 결정된다는 사실이다. 특히 mirror symmetry isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$ 관점에서, critical value들 $$\{ W_q(p) \}$$는 A-side에서는 quantum cohomology의 *canonical coordinate*로 해석된다.

## 가우스-마닌 접속

Oscillating integral의 $$q, z$$ 의존성을 추적하기 위해 *Gauss-Manin connection* $$\nabla^{GM}$$을 도입한다. 도입 무대는 §Lefschetz thimble에서 본 rapid decay homology의 dual인 *rapid decay relative cohomology*

$$H^N(\check{X}, \{ \Real(W_q/z) \ll 0 \};\, \mathbb{C})$$

이다 (cycle을 평가하는 cocycle들의 cohomology; 각 fiber에서 dimension은 $$\lvert\Crit(W_q)\rvert = \dim_\mathbb{C} H^\ast(X, \mathbb{C})$$로 일정). Parameter $$(q, z) \in (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast$$가 변할 때 이 cohomology가 *local system*을 이루어 (dimension이 일정하고 fiber가 연속적으로 식별 가능) vector bundle $$\mathcal{H}$$이 되며 (**[Pha11]**, **[Sab08]**), $$\mathcal{H}$$ 위에는 cycle의 *parallel transport*로부터 비롯되는 자연스러운 flat connection이 존재한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4** (Gauss-Manin connection)</ins> Bundle $$\mathcal{H} \to (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast$$의 *Gauss-Manin connection* $$\nabla^{GM}$$은 각 fiber 사이의 *comparison isomorphism*에 의해 정의되는 flat connection이다. 즉, $$(q, z)$$가 작게 움직일 때 vanishing cycle의 homology class를 "parallel하게" 옮겨주는 connection이며, flatness $$\nabla^{GM} \circ \nabla^{GM} = 0$$이 성립한다.

</div>

$$\nabla^{GM}$$의 representative form 차원에서의 계산은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Class $$[e^{W_q/z}\, \omega] \in \mathcal{H}_{(q,z)}$$에 대해 Gauss-Manin connection은

$$\nabla^{GM}_{\partial_{q_a}} [e^{W_q/z}\, \omega] = \left[\frac{\partial_{q_a} W_q}{z}\, e^{W_q/z}\, \omega\right],\qquad \nabla^{GM}_{z \partial_z}[e^{W_q/z}\, \omega] = \left[-\frac{W_q}{z}\, e^{W_q/z}\, \omega\right]$$

으로 작용한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cochain 차원에서 chain rule로 계산하면

$$\partial_{q_a}\!\left(e^{W_q/z}\,\omega\right) = \frac{\partial_{q_a} W_q}{z}\, e^{W_q/z}\, \omega,\qquad z\partial_z\!\left(e^{W_q/z}\,\omega\right) = -\frac{W_q}{z}\, e^{W_q/z}\, \omega$$

이다 ($$\omega$$는 $$q, z$$와 무관). $$\nabla^{GM}$$의 well-definedness는 cocycle 변형이 coboundary로 떨어진다는 사실, 즉 임의의 $$(N-1)$$-form $$\beta$$에 대해 $$d(e^{W_q/z}\beta) = e^{W_q/z}(d\beta + z^{-1} dW_q \wedge \beta)$$이 exact임에서 따라 나오며, flatness $$[\nabla^{GM}_{\partial_{q_a}}, \nabla^{GM}_{\partial_{q_b}}] = 0$$은 partial derivative들의 commutativity로부터 즉시 얻어진다.

</details>

## B-model connection과 flat section equation

[§두브로빈 접속, ⁋정의 1](/ko/math/mirror_symmetry/dubrovin_connection#def1)의 A-model Dubrovin connection $$\nabla^z$$와 직접 비교 가능하도록, Gauss-Manin connection을 $$z$$만큼 rescaling한 **B-model connection**을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6** (B-model connection)</ins> $$\mathcal{H}$$ 위에 정의되는 *B-model connection* $$\nabla^z_B$$은

$$\nabla^z_B := z\, \nabla^{GM}$$

으로 정의된다. 명시적으로, frame $$[e^{W_q/z}\omega]$$를 기준으로 하면 [명제 5](#prop5)에서 $$\nabla^z_{B, \partial_{q_a}}[e^{W_q/z}\omega] = \partial_{q_a} W_q \cdot [e^{W_q/z}\omega]$$, $$\nabla^z_{B, z\partial_z}[e^{W_q/z}\omega] = -W_q \cdot [e^{W_q/z}\omega]$$로 작용한다 ($$\partial_{q_a} W_q$$, $$W_q$$는 cohomology class에 대한 multiplication operator).

</div>

이 rescaling은 [명제 5](#prop5)의 $$1/z$$ 인자를 흡수하여, $$z \to 0$$에서 B-model connection의 *symbol*이 $$\partial_{q_a} W_q$$의 Jacobi ring 안에서의 multiplication으로 well-defined classical limit을 가지며, 이는 A-model의 quantum product $$T_a\ast_q$$에 대응한다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7** (Period 미분 공식)</ins> 임의의 Lefschetz thimble $$\Gamma$$에 대응하는 oscillating integral $$\mathcal{I}_\Gamma$$는 다음 미분 관계식을 만족한다.

$$z\, \partial_{q_a} \mathcal{I}_\Gamma = \int_\Gamma \partial_{q_a} W_q \cdot e^{W_q/z}\, \omega,\qquad z^2 \partial_z \mathcal{I}_\Gamma = -\int_\Gamma W_q\, e^{W_q/z}\, \omega.$$

식의 *형태*는 $$\Gamma$$의 구체적 선택과 무관하며, 양변 모두 $$\Gamma$$에 한 번씩 의존한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\Gamma$$의 boundary 부근에서 $$\Real(W_q/z) \to -\infty$$이므로 $$e^{W_q/z} \to 0$$이고, differentiation under the integral sign이 boundary term 없이 정당화된다. Chain rule에 의해

$$\partial_{q_a} \mathcal{I}_\Gamma = \int_\Gamma \partial_{q_a}(e^{W_q/z})\, \omega = \frac{1}{z}\int_\Gamma \partial_{q_a} W_q \cdot e^{W_q/z}\, \omega,$$

$$\partial_z \mathcal{I}_\Gamma = \int_\Gamma \partial_z(e^{W_q/z})\, \omega = -\frac{1}{z^2}\int_\Gamma W_q \cdot e^{W_q/z}\, \omega$$

이며, 양변에 각각 $$z$$, $$z^2$$를 곱하면 정리의 식을 얻는다.

</details>

[정리 7](#thm7)은 oscillating integral이 단순한 적분이 아니라 B-model $$D$$-module의 horizontal section을 명시적으로 제공한다는 강력한 주장이다. Cohomology bundle $$\mathcal{H}$$ 위에서 [정의 6](#def6)의 B-model connection은 $$\nabla^z_B [e^{W_q/z}\omega] = [\partial_{q_a} W_q \cdot e^{W_q/z}\omega]$$로 작용하므로, $$\mathcal{I}_\Gamma$$ 자체는 closed equation을 따르지 않는다. 그러나 Jacobi ring basis $$\{T_\alpha\}$$ ([§거울대칭 개요](/ko/math/mirror_symmetry/overview)의 ring 동형 $$\Jac \cong QH^\ast$$를 통해 $$QH^\ast(X)$$의 basis에 대응)와 Lefschetz thimble basis $$\{\Gamma_b\}$$를 vectorize한 행렬

$$\mathcal{I}^\alpha_{\Gamma_b}(q, z) := \int_{\Gamma_b} T_\alpha\, e^{W_q/z}\, \omega$$

은 Jacobi ring 안에서 $$T_\alpha \cdot \partial_{q_a} W_q = \sum_\beta (M_a)^\alpha_\beta T_\beta$$의 multiplication matrix에 의해 닫힌 system

$$z\, \partial_{q_a} \mathcal{I}^\alpha_{\Gamma_b} = \sum_\beta (M_a)^\alpha_\beta\, \mathcal{I}^\beta_{\Gamma_b}$$

를 만족하며, 이 matrix가 정확히 B-model $$D$$-module의 *fundamental solution matrix*를 이룬다. 두 basis $$\{T_\alpha\}$$, $$\{\Gamma_b\}$$의 선택에 따라 matrix는 invertible 변환만큼 다르게 표현되므로 fundamental solution은 basis 선택에 covariant하며, D-module 구조 자체는 처음부터 $$\Gamma$$ 선택과 무관한 cohomology bundle $$\mathcal{H}$$와 $$\nabla^{GM}$$의 intrinsic 데이터이다.

## Mirror theorem과 $$J$$-function의 복원

[§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)의 D-module isomorphism

$$\Phi: H_A \xrightarrow{\sim} H_B$$

는 A-model의 horizontal section을 B-model의 horizontal section에 대응시킨다. 그 가장 명시적 form이 이후 [§Givental J-function과 Mirror Theorem](/ko/math/mirror_symmetry/givental_j_function)에서 다룰 mirror theorem으로,

$$J^a_X(q, z) = \frac{1}{(2\pi i z)^N}\int_{\Gamma_a} e^{W_q/z}\, \omega$$

의 형태이다 (적절한 normalization). $$z \to 0$$에서 좌변은 $$X$$의 classical cohomology의 basis로 수렴하고, 우변은 [명제 3](#prop3)에 의해 $$W_q$$의 critical points의 contribution으로 풀어진다. 두 limit이 같다는 것은 정확히 [§거울대칭 개요](/ko/math/mirror_symmetry/overview)에서 살펴본 ring 동형 $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$의 진술이다.

## 예시: $$\mathbb{P}^n$$의 oscillating integral

<div class="example" markdown="1">

<ins id="ex8">**예시 8** ($$X = \mathbb{P}^n$$)</ins> $$\mathbb{P}^n$$의 Hori-Vafa mirror는 [§거울대칭 개요, ⁋정의 4](/ko/math/mirror_symmetry/overview#def4)의 처방을 그대로 따라 ($$\mathbb{P}^1$$의 경우 [§거울대칭 개요, ⁋예시 5](/ko/math/mirror_symmetry/overview#ex5), $$\mathbb{P}^2$$의 경우 [§거울대칭 개요, ⁋예시 6](/ko/math/mirror_symmetry/overview#ex6) 참조)

$$\check{X} = (\mathbb{C}^\ast)^n,\qquad W_q = x_1 + \cdots + x_n + \frac{q}{x_1 \cdots x_n},\qquad \omega = \frac{dx_1 \wedge \cdots \wedge dx_n}{x_1 \cdots x_n}$$

이다. Oscillating integral은

$$\mathcal{I}_\Gamma(q, z) = \int_\Gamma \exp\!\left(\frac{x_1 + \cdots + x_n + q/(x_1\cdots x_n)}{z}\right)\, \frac{dx_1 \cdots dx_n}{x_1 \cdots x_n}$$

이다. $$W_q$$의 critical points는 $$x_1 = \cdots = x_n = x$$이고 $$x^{n+1} = q$$를 만족하는 $$n+1$$개의 점들이며, 각 critical point에서의 critical value는 $$W_q(x) = (n+1)\, x$$이다. $$x = \zeta\, q^{1/(n+1)}$$ ($$\zeta$$가 $$(n+1)$$-th root of unity)에서의 Hessian을 계산하자. Critical point에서 $$q/(x_1\cdots x_n) = x$$이므로 $$\partial_i \partial_j W_q$$는 대각 성분이 $$2/x$$, 비대각 성분이 $$1/x$$인 행렬, 즉 $$\Hess_p(W_q) = \tfrac{1}{x}\big(I_n + \mathbf{1}\mathbf{1}^\top\big)$$이다 (여기서 $$\mathbf{1}$$은 모든 성분이 $$1$$인 vector). $$\det(I_n + \mathbf{1}\mathbf{1}^\top) = n+1$$이므로

$$\det \Hess_p(W_q) = (n+1)\,(\zeta q^{1/(n+1)})^{-n}$$

이며, 따라서 stationary phase asymptotic은

$$\mathcal{I}_{\Gamma_p}(q, z) \sim (2\pi z)^{n/2}\, \frac{\exp\big( (n+1)\, \zeta\, q^{1/(n+1)} / z \big)}{\sqrt{\det \Hess_p(W_q)}}\,(1 + O(z))$$

이다.

한편 $$\mathbb{P}^n$$의 $$J$$-function은 (이후 [§Givental J-function과 Mirror Theorem](/ko/math/mirror_symmetry/givental_j_function)에서 다루듯)

$$J_{\mathbb{P}^n}(q, z) = e^{H \ln q/z} \sum_{d \geq 0} \frac{q^d}{\prod_{j=1}^d (H + jz)^{n+1}}$$

이다. $$H^{n+1} = q$$ relation을 사용하여 $$J$$-function의 $$z \to 0$$ stationary phase asymptotic을 풀면 정확히 위의 oscillating integral expansion이 복원된다. 이것이 $$\mathbb{P}^n$$에 대한 mirror theorem의 explicit form이다.

</div>

A-model과 B-model 양측의 connection-level 데이터를 이렇게 정리해두면, 이어지는 [§Jacobi Ring과 Quantum Cohomology의 동형](/ko/math/mirror_symmetry/jacobi_ring)에서 두 측면의 *ring-level* 골조에 해당하는 Jacobi ring과 quantum cohomology 사이의 isomorphism, 즉 $$z\to 0$$ 극한으로 볼 때 oscillating integral의 critical-point 분해와 Gromov-Witten 계산이 만나는 지점을 정밀하게 다룬다.

---

**참고문헌**

**[Giv96]** A. Givental, *Equivariant Gromov-Witten invariants*, Internat. Math. Res. Notices **1996**, no. 13, 613--663.

**[Pha11]** F. Pham, *Singularities of integrals*, Universitext, Springer, 2011.

**[Sab08]** C. Sabbah, *Isomonodromic deformations and Frobenius manifolds*, Springer, 2008.

**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[Iri]** H. Iritani, *An integral structure in quantum cohomology and mirror symmetry for toric orbifolds*, Adv. Math. **222** (2009), no. 3, 1016--1079.

---

[^1]: 여기서 $$m_1, \ldots, m_N$$은 character lattice $$M$$의 $$\mathbb{Z}$$-basis이다 ([\[토릭 기하학\] §토릭 다양체 위의 로그 미분형식, ⁋명제 13](/ko/math/toric_geometry/logarithmic_differentials#prop13)).