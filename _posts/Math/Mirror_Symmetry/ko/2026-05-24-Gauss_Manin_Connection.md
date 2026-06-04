---
title: "가우스-마닌 접속"
description: "거울대칭의 두브로빈 접속에서 주장한 모듈 동형사상을 구체적으로 살펴보고, B-side의 진동 적분과 가우스-마닌 시스템을 중심으로 Landau-Ginzburg 모델의 홀로모피 부피 형식 구성까지 다룬다."
excerpt: "B-model의 D-module 구조와 oscillating integral, 그리고 cohomology 위의 Gauss-Manin connection"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/gauss-manin_connection
sidebar: 
    nav: "mirror_symmetry-ko"

date: 2026-05-24
last_modified_at: 2026-05-26
weight: 5
published: false
---

이번 글에서 우리는 [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)에서 주장한 $$D$$-module isomorphism을 구체적으로 살펴본다. 이를 위해서는 A-side와 B-side 모두를 보아야 한다. A-side의 경우는 이미 [\[사교기하학\] §양자 코호몰로지, ⁋정의 7](/ko/math/symplectic_geometry/quantum_cohomology#def7)에서 어느정도 다룬 것이므로, 우리는 우선 B-side, 즉 oscillating integral과 Gauss-Manin system에 대해 살펴본다. 

## Landau-Ginzburg model과 volume form

우선 우리는 B-model의 무대를 만들어야 한다. [§거울대칭 개요, ⁋정의 4](/ko/math/mirror_symmetry/overview#def4)에서 살펴보았듯, Landau-Ginzburg model $$(\check{X}, W_q)$$에서 $$\check{X}$$는 보통 algebraic torus $$(\mathbb{C}^\ast)^N$$ 혹은 그 안에 있는 subvariety이며, $$W_q$$는 *quantum parameter* $$q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$$로 parametrize되는 holomorphic function이다. 여기서 $$r$$은 A-side mirror $$X$$의 *complexified Kähler moduli*의 차원이었으며, Fano variety의 경우

$$r = \operatorname{rank}\,\operatorname{Pic}(X) = \dim_\mathbb{C} H^2(X; \mathbb{C})$$

로 주어졌다. 우리는 이 위에 oscillating integral을 정의하기 위해 우선 holomorphic volume form $$\omega$$를 정의한다.

일반적으로 compact (대수기하학에서는 complete) 공간에서는 form이 non-vanishing일 수 없으므로, volume form을 얻기 위해 우리는 이러한 점들을 임의로 제거해주어야 한다. 즉, $$\check{X}$$를 어떤 smooth projective variety $$Y$$의 open subset $$\check{X} = Y \setminus D$$로 본 후, $$Y$$의 divisor $$D$$를 $$\mathcal{K}_Y$$의 rational section의 bad locus를 정확히 흡수하는 divisor로 고르는 것이다. 구체적으로 anti-canonical class $$-K_Y$$의 effective representative $$D \geq 0$$ (즉 $$D \sim -K_Y$$)를 잡으면 $$\mathcal{K}_Y \otimes \mathcal{O}_Y(D) \cong \mathcal{O}_Y$$가 trivial이 되어 nowhere-vanishing global section

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

의 $$\mathbb{C}$$-basis가 된다. 여기서 rapid decay homology $$H_\ast(\check{X}, \{\Real(W_q/z) \ll 0\}; \mathbb{C})$$는 충분히 작은 $$\Real(W_q/z)$$를 갖는 점들로 이루어진 *rapid decay zone*

$$S_z=\{x \in \check{X} \mid \Real(W(x)/z) \ll 0\}$$

에 대해, boundary $$\partial \sigma$$가 $$S_z$$ 안에 들어가는 $$n$$-chain $$\sigma$$들을, $$S_z$$ 안에 완전히 들어가는 chain은 0으로 quotient하여 모은 것이다. 더 엄밀하게는

$$S_z^M=\{x \in \check{X} \mid \Real(W(x)/z) <-M\}$$

으로 두고, relative singular homology $$H_n(\check{X}, S_z^M; \mathbb{C})$$을 생각한 것으로, $$S_z^M$$은 물론 $$M$$의 값에 의존하지만 이 relative homology 자체는 $$M$$의 값이 커지면 stabilize한다는 것이 알려져 있다. 우리는 이 stabilize한 값을 rapid decay homology로 정의하는 것이다. 

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

$$\mathcal{I}_{\Gamma_p}(q, z) \sim (2\pi z)^{N/2} \frac{e^{W_q(p)/z}}{\sqrt{\det\Hess_p(W_q)}} \big(1 + O(z)\big)$$

이 성립한다. 여기서 $$N = \dim_\mathbb{C} \check{X}$$, $$\Hess_p$$는 $$p$$에서의 Hessian이며, $$\sqrt{}$$의 branch는 $$\Gamma_p$$의 orientation으로 결정된다.

</div>

증명의 핵심은 $$p$$ 근방에서 [\[사교기하학\] §Morse 이론과 stationary phase 근사, ⁋정리 6](/ko/math/symplectic_geometry/morse_stationary_phase#thm6)을 사용하여 $$W_q$$를 quadratic form으로 환원한 뒤 Gaussian 적분을 적용하는 것이다. 어쨌든 우리 상황에서 중요한 것은 $$z \to 0^+$$일 때 oscillating integral이 *각 critical point의 local data*, 즉 critical value $$W_q(p)$$와 Hessian determinant로 완전히 결정된다는 사실이다. 특히 mirror symmetry isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$ 관점에서, critical value들 $$\{ W_q(p) \}$$는 A-side에서는 quantum cohomology의 *canonical coordinate*로 해석된다.

## 가우스-마닌 접속

Oscillating integral의 $$(q, z)$$ 의존성을 추적하기 위해 *Gauss-Manin connection* $$\nabla^{GM}$$을 도입한다. 이를 정의하기 위해서는 우선 그 무대가 되는 vector bundle을 잡아야 한다. $$(q,z)$$ parameter들의 공간 $$B=(\mathbb{C}^\ast)^r\times \mathbb{C}^\ast$$를 base manifold로 하고, 그 위에 각 base point $$(q, z) \in B$$에 대해, 위에서 정의한 rapid decay homology의 dual인 *rapid decay relative cohomology*

$$\mathcal{H}_{(q, z)} := H^N(\check{X}, \{ \Real(W_q/z) \ll 0 \};\, \mathbb{C})$$

을 fiber로 할당하는 family

$$\{\mathcal{H}_{(q, z)}\}_{(q, z) \in B}$$

를 생각한다. 각각의 점 $$(q,z)$$에서 이들은 위의 cohomology의 원소로서, rapidly decay homology의 원소와 pairing되어 값을 주는 것이 그 본질이다. Rapid decay homology는 Lefschetz thimble들을 그 basis로 가지므로, [정의 2](#def2)를 생각하면 위의 cohomology의 원소는 $$[e^{W_q/z}\omega]$$로 그 representative를 잡는 것이 자연스럽다. 

이 family는 만일 $$W_q$$가 Morse type이라면 $$B$$ 위에 정의된 vector bundle $$\mathcal{H}$$를 정의한다는 것이 알려져 있다. 특히 이들 각각의 fiber가 잘 붙는다는 것은 앞서 Lefschetz thimble을 택할 때 $$(q,z)$$에 따라 continuously isotoped될 수 있는 것들을 모았기 때문에 가능하다. 즉, cycle $$\Gamma$$가 $$(q, z)$$의 변화에 따라 연속적으로 움직일 때 그와 pairing되는 cohomology class도 함께 "따라가도록" 평행 이동시킬 수 있고, 이 평행 이동을 connection 형태로 정리한 것이 *Gauss-Manin connection*이다.

<div class="definition" markdown="1"> 

<ins id="def4">**정의 4 (Gauss-Manin connection)**</ins> Vector bundle $$\mathcal{H} \to (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast$$ 위의 *Gauss-Manin connection* $$\nabla^{GM}$$은 다음 조건으로 유일하게 결정되는 flat connection이다.

> Section $$\mathbf{s}: (q, z) \mapsto [\alpha(q, z)] \in \mathcal{H}_{(q,z)}$$가 *$$\nabla^{GM}$$-flat*이라는 것은, [정의 2](#def2) 직후의 의미로 continuously isotoped된 *임의의* cycle family $$\{\Gamma(q, z)\}$$에 대해 *period*
> 
> $$\Pi_\Gamma(q, z) := \int_{\Gamma(q, z)} \alpha(q, z)$$
> 
> 이 $$(q, z)$$의 locally constant function이 되는 것과 동치이다.

</div>

위에서 언급했듯 cohomology fiber $$\mathcal{H}_{(q,z)}$$의 원소는 dual rapid decay homology의 cycle과의 integral pairing으로 완전히 결정된다. 이 때, 위의 local system 구조에서 fiber 사이의 canonical identification은 정확히 cycle들의 parallel transport의 dual로 결정되었다. 따라서, 위의 bundle의 section들을 이 identification을 통해 locally constant인지 확인하기 위해서는 모든 parallel transport된 cycle들과의 pairing 값이 locally constant인지 보면 되고, 이 값이 바로 period인 것이다. 약간의 계산을 거치면 이렇게 정의된 $$\nabla^{GM}$$이 유일하게 결정되며, $$\nabla^{GM}$$의 flatness 또한 확인할 수 있다. 

$$\nabla^{GM}$$의 representative form 차원에서의 계산은 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Class $$[e^{W_q/z}\, \omega] \in \mathcal{H}_{(q,z)}$$에 대해 Gauss-Manin connection은

$$\nabla^{GM}_{\partial_{q_i}} [e^{W_q/z}\, \omega] = \left[\frac{\partial_{q_i} W_q}{z}\, e^{W_q/z}\, \omega\right],\qquad \nabla^{GM}_{z \partial_z}[e^{W_q/z}\, \omega] = \left[-\frac{W_q}{z}\, e^{W_q/z}\, \omega\right]$$

으로 작용한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Cochain 차원에서 chain rule로 계산하면

$$\partial_{q_i}\!\left(e^{W_q/z}\,\omega\right) = \frac{\partial_{q_i} W_q}{z}\, e^{W_q/z}\, \omega,\qquad z\partial_z\!\left(e^{W_q/z}\,\omega\right) = -\frac{W_q}{z}\, e^{W_q/z}\, \omega$$

이다 ($$\omega$$는 $$q, z$$와 무관). $$\nabla^{GM}$$의 well-definedness는 cocycle 변형이 coboundary로 떨어진다는 사실, 즉 임의의 $$(N-1)$$-form $$\beta$$에 대해 $$d(e^{W_q/z}\beta) = e^{W_q/z}(d\beta + z^{-1} dW_q \wedge \beta)$$이 exact임에서 따라 나오며, flatness $$[\nabla^{GM}_{\partial_{q_i}}, \nabla^{GM}_{\partial_{q_j}}] = 0$$은 partial derivative들의 commutativity로부터 즉시 얻어진다.

</details>

## B-model connection

[§두브로빈 접속, ⁋정의 1](/ko/math/mirror_symmetry/dubrovin_connection#def1)의 A-model Dubrovin connection $$\nabla^z$$와 직접 비교 가능하도록, Gauss-Manin connection을 $$z$$만큼 rescaling한 *B-model connection*을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6 (B-model connection)**</ins> $$\mathcal{H}$$ 위에 *B-model connection* $$\nabla^z_B$$을

$$\nabla^z_B := z\nabla^{GM}$$

으로 정의한다. 

</div>

명시적으로, frame $$[e^{W_q/z}\omega]$$에 B-model connection을 적용해보면 [명제 5](#prop5)에서 

$$\nabla^z_{B, \partial_{q_i}}[e^{W_q/z}\omega] = \partial_{q_i} W_q \cdot [e^{W_q/z}\omega],\qquad \nabla^z_{B, z\partial_z}[e^{W_q/z}\omega] = -W_q \cdot [e^{W_q/z}\omega]$$

가 성립한다. 이 rescaling으로 [명제 5](#prop5)의 $$1/z$$ 인자가 흡수되므로, $$z \to 0$$ 극한에서 B-model connection의 connection 1-form은 정확하게 cohomology class에 대한 $$\partial_{q_i} W_q$$의 곱셈이 된다. 이는 앞서 [§두브로빈 접속, ⁋주장 4](/ko/math/mirror_symmetry/dubrovin_connection#conj4)에서 살펴본 것과 같은 맥락으로, $$z\rightarrow 0$$인 상황에서 Frobenius manifold $$M\times \mathbb{C}^\ast$$에서 $$z$$를 $$0$$으로 보낼 때 Frobenius algebra의 product 구조를 복원해내는 것과 동일한 상황이다.

위의 식은 cohomology class 차원의 statement이므로, 이를 구체적으로 계산하려면 임의의 Lefschetz thimble (즉 rapid decay homology의 basis)와 pair하여 실제 적분을 계산하면 된다. 그 결과는 다음의 

$$z\,\partial_{q_i}\mathcal{I}_\Gamma = \int_\Gamma \partial_{q_i}W_q\cdot e^{W_q/z}\,\omega,\qquad z^2\,\partial_z\mathcal{I}_\Gamma = -\int_\Gamma W_q\cdot e^{W_q/z}\,\omega \tag{$\ast$}$$

이다. 그런데 ($$\ast$$)의 우변은 우리가 알고 있는 형태 ([정의 2](#def2))와는 다른 것으로, 이를 해결하기 위해서는 $$f$$가 rapid decay homology의 decaying condition을 깨지 않는 한에서 $$f e^{W_q/z}\omega$$ 꼴로 integrand를 넓혀주어야 한다. Thimble $$\Gamma$$의 boundary 부근에서 $$\lvert e^{W_q/z}\rvert = e^{\Real(W_q/z)}$$가 지수적으로 $$0$$으로 사라지므로, $$f$$가 polynomial 정도의 성장만 한다면 충분히 컨트롤이 가능하며 따라서 자연스러운 함수 공간은 regular function들의 공간 $$\mathcal{O}(\check{X})$$이다. 

문제는 이렇게 정의할 경우 regular function들의 모임은 (벡터공간으로서) 무한차원이므로 이들을 모두 추가하는 것이 불가능하다는 것에 있다. 이를 해결하기 위해 우리는 period integral을 사용해서 pairing을 정의할 경우, 그 값이 cohomology class에만 의존한다는 것을 관찰한다. 이는 만일 $$f, g \in \mathcal{O}(\check{X})$$가 같은 cohomology class를 정의한다면, 즉 만일 적당한 rapid decay form $$\alpha$$에 대하여 다음의 식 $$(f-g)\cdot e^{W_q/z}\omega = d\alpha$$이 성립한다면, Stokes 정리로부터

$$\int_\Gamma (f-g)\cdot e^{W_q/z}\omega = \int_\Gamma d\alpha = \int_{\partial\Gamma}\alpha = 0$$

이고, 따라서 $$\mathcal{I}^f_\Gamma$$의 값은 $$f$$의 cohomology class $$[f\cdot e^{W_q/z}\omega] \in \mathcal{H}_{(q,z)}$$에만 의존함이 따라온다. 즉 우리가 다뤄야 하는 unknown 공간은 사실상 $$\mathcal{O}(\check{X})$$가 아니라 $$\mathcal{H}_{(q,z)}$$이고, $$\mathcal{H}_{(q,z)}$$만 유한차원이면 이 문제가 해결된다. 그리고 이는 실제로 성립하는데, $$W_q$$가 Morse type이면 rapid decay homology $$H_N(\check{X}, S_z;\mathbb{C})$$가 thimble basis $$\{[\Gamma_p]\}_{p\in\Crit(W_q)}$$를 가지고, 이것이 $$\mathcal{H}_{(q,z)}$$의 dual이므로

$$\dim_\mathbb{C}\mathcal{H}_{(q,z)} = \lvert\Crit(W_q)\rvert$$

이기 때문이다.

한편 $$\mathcal{H}_{(q,z)}$$는 또 다른 자연스러운 basis를 갖는데, $$\Jac(W_q)$$로부터 오는 것이 그것이다. 자연스러운 map

$$\Jac(W_q) \;\longrightarrow\; \mathcal{H}_{(q,z)},\qquad T \;\longmapsto\; [T\cdot e^{W_q/z}\omega]$$

을 생각하면, 차원 계산에 의해 이것이 isomorphism임을 보일 수 있고, 이로부터 $$\Jac(W_q)$$의 basis $$\{T_a\}$$들로부터 $$\mathcal{H}_{(q,z)}$$의 basis

$$\bigl\{\,e_a := [T_a\,e^{W_q/z}\omega]\,\bigr\}_{a=0,\ldots,\mu-1}$$

를 택할 수 있다. 즉 우리는 현재 rapid decay cohomology side의 basis $$\{e_a\}$$와 rapid decay homology side의 basis $$\{[\Gamma_p]\}_{p=0,\ldots,\mu-1}$$ (thimble을 critical point에 따라 indexing)를 가지고 있으며, 이들을 사용하면 *period matrix*

$$\mathcal{I}^a_p(q, z) \;:=\; \langle e_a,\,[\Gamma_p]\rangle \;=\; \int_{\Gamma_p} T_a\,e^{W_q/z}\,\omega$$

를 정의할 수 있다. 이제 위의 ($$\ast$$)는 이 행렬 상에서 다음과 같이 적힌다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Fundamental solution matrix)**</ins> 위의 setup에서 $$\Jac(W_q)$$ 안의 multiplication 행렬을

$$T_a\cdot \partial_{q_i}W_q = \sum_b (M_i)^a_b\, T_b,\qquad T_a\cdot W_q = \sum_b E^a_b\, T_b\quad\text{in}\;\Jac(W_q)$$

로 정의하면, period matrix $$\mathcal{I} = (\mathcal{I}^a_p)$$는 닫힌 ODE system

$$z\,\partial_{q_i}\mathcal{I}^a_p = \sum_b (M_i)^a_b\,\mathcal{I}^b_p,\qquad z^2\,\partial_z\mathcal{I}^a_p = -\sum_b E^a_b\,\mathcal{I}^b_p$$

을 만족한다. 특히 $$\mathcal{I}$$는 invertible matrix-valued function이며, frame $$\{e_a\}_a$$로 trivialize한 B-model connection $$\nabla^z_B$$의 *fundamental solution matrix*를 이룬다.

</div>

구체적으로, $$\{[\Gamma_p]\}$$의 dual basis $$\{f^p\}\subset\mathcal{H}_{(q,z)}$$는 [정의 4](#def4)에 의해 $$\nabla^z_B$$의 *horizontal sections*이고, $$\mathcal{H}$$ 안에서 non-flat frame $$\{e_a\}$$와 flat frame $$\{f^p\}$$ 사이의 change-of-basis가 정확히

$$e_a = \sum_p \mathcal{I}^a_p\,f^p,\qquad f^p = \sum_a (\mathcal{I}^{-1})^p_a\,e_a$$

이다. 따라서 $$\mathcal{I}^{-1}$$의 column들이 frame $$\{e_a\}$$로 표현한 $$\nabla^z_B$$의 horizontal sections이며, $$\mathcal{I}$$ 자체가 $$\nabla^z_B$$의 모든 데이터를 인코딩하게 되는 것이다. 이 fundamental solution matrix $$\mathcal{I}$$가 A-side에서는 quantum cohomology $$D$$-module의 fundamental solution($$J$$-function)과 일치한다는 것이 mirror theorem의 주장이며, 이는 다음 글에서 다룬다. 

## 예시: $$\mathbb{P}^n$$의 oscillating integral

<div class="example" markdown="1">

<ins id="ex8">**예시 8** ($$X = \mathbb{P}^n$$)</ins> 우리는 앞서 [§거울대칭 개요, ⁋예시 5](/ko/math/mirror_symmetry/overview#ex5)에서 $$\mathbb{P}^n$$의 Hori-Vafa mirror는

$$\check{X} = (\mathbb{C}^\ast)^n,\qquad W_q = \x_1 + \cdots + \x_n + \frac{q}{\x_1 \cdots \x_n},\qquad \omega = \frac{d\x_1 \wedge \cdots \wedge d\x_n}{\x_1 \cdots \x_n}$$

형태로 주어지는 것을 확인했다. 이 때, critical point를 계산하기 위해 미분을 해 보면

$$\partial_{\x_i}W_q =1 - \frac{1}{\x_i}\frac{q}{\x_1\cdots x_n} = 0$$

이고, 이것이 모든 $$i$$에 대해 성립해야 하므로 $$x_i=\zeta^kq^{1/(n+1)}$$을 만족하는 $$x$$들이 critical point들이다. Jacobi ring 관점에서는 위의 critical point들의 방정식이

$$\Jac(W_q) \;\cong\; \mathbb{C}[\x, \x^{-1}]\,/\,(\x^{n+1} - q)$$

을 주고, 위의 $$x$$의 계산으로부터 $$\Jac(W_q)$$의 basis를 $$\x^a$$들로 택할 수 있다. 한편 Jacobi ring 안에서 

$$\partial_qW_q = \x^{-n} = \x/q,\qquad W_q = n\x + q\cdot\x/q = (n+1)\x$$

이므로 multiplication matrices는

$$M_q = \begin{pmatrix} 0 & 1/q & & & \\ & 0 & 1/q & & \\ & & \ddots & \ddots & \\ & & & 0 & 1/q \\ 1 & & & & 0\end{pmatrix},\qquad E = (n+1)qM_q$$

이다. 이제 [명제 7](#prop7)에 따라 period matrix $$\mathcal{I}^a_p(q,z)$$는 

$$z\partial_q\mathcal{I}^a_p = \sum_b (M_q)^a_b\mathcal{I}^b_p$$

를 만족하므로, $$a<n$$인 $$a$$에 대해서는

$$z\partial_q\mathcal{I}_p^a=\frac{1}{q}\mathcal{I}_p^{a+1}$$

이 성립하므로 이로부터 $$\mathcal{I}_p^n=(qz\partial_q)^n \mathcal{I}_p^0$$이고, 첫째 column으로부터 얻어지는 식

$$z\partial_q\mathcal{I}_p^n=\mathcal{I}_p^0$$

과 이를 결합하면 우리는 $$\mathcal{I}_p^0$$이 만족하는 $$(n+1)$$-차 ODE

$$(z\partial_q)\bigl(qz\partial_q\bigr)^n\,\mathcal{I}^0_p = \mathcal{I}^0_p$$

를 얻으며, 이것이 곧 $$\mathbb{P}^n$$의 quantum differential equation이다. 

으로, A-side $$J$$-function이 만족하는 hypergeometric ODE와 동일하다. State phase asymptotic의 경우, $$x_\zeta$$에서 $$\partial_i\partial_j W_q$$는 대각 $$2/x_\zeta$$, 비대각 $$1/x_\zeta$$ ($$\mathbf{1} := (1,\ldots,1)^\top$$)이므로

$$\Hess_{x_\zeta}(W_q) = \tfrac{1}{x_\zeta}\bigl(I_n + \mathbf{1}\mathbf{1}^\top\bigr),\qquad \det \Hess_{x_\zeta}(W_q) = (n+1)\,(\zeta\,q^{1/(n+1)})^{-n}$$

이고 critical value $$W_q(x_\zeta) = (n+1)\,\zeta\,q^{1/(n+1)}$$이므로 [명제 3](#prop3)에 의해

$$\mathcal{I}_{\Gamma_{x_\zeta}}(q, z) \sim (2\pi z)^{n/2}\,\frac{\exp\bigl((n+1)\,\zeta\,q^{1/(n+1)}/z\bigr)}{\sqrt{(n+1)(\zeta\,q^{1/(n+1)})^{-n}}}\,(1 + O(z))$$

가 따른다.

</div>

---

**참고문헌**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.

---

[^1]: 여기서 $$m_1, \ldots, m_N$$은 character lattice $$M$$의 $$\mathbb{Z}$$-basis이다 ([\[토릭 기하학\] §토릭 다양체 위의 로그 미분형식, ⁋명제 13](/ko/math/toric_geometry/logarithmic_differentials#prop13)).