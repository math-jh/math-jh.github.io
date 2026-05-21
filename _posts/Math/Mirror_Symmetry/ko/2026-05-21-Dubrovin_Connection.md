---
title: "두브로빈 접속"
excerpt: "Frobenius manifold 위 spectral parameter를 갖는 flat connection"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/dubrovin_connection
sidebar: 
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Dubrovin_Connection.png
    overlay_filter: 0.5

date: 2026-05-21
last_modified_at: 2026-05-21
weight: 4

published: false
---
이전 글에서 우리는 quantum cohomology $$QH^\ast(X)$$ 혹은 Jacobi ring $$\Jac(X)$$가 Frobenius algebra 구조를 갖는다는 것을 살펴보고, 이들 isomorphism의 $$q$$-parameter 방향의 naturality를 담기 위해 이들을 Frobenius manifold 구조로 집어넣었다. Frobenius manifold $$M$$ 위에 정의된 데이터는 다음의 데이터들

- Metric $$\eta$$ ($$QH^\ast(X)$$에서는 Poincaré pairing)과 그로부터 나오는 Levi-Civita connection,
- Frobenius algebra의 product $$\circ$$ ($$QH^\ast(X)$$에서는 quantum cup product),
- Euler vector field $$E$$ (degree 정보)

이 담겨있었으며, 이 때 $$\circ$$의 associativity가 WDVV equation으로 표현된다는 사실을 확인하였다. ([§프로베니우스 다양체, ⁋명제 7](/ko/math/mirror_symmetry/frobenius_manifold#prop7)) 이번 글에서 다룰 Dubrovin connection은 여기서 더 나아가, $$\eta$$와 $$\circ$$, 더 정확하게는 $$\nabla$$와 $$\circ$$이 서로 깊은 관계가 있음을 보여준다. 

## 두브로빈 접속

Dubrovin에 따르면 $$\nabla$$와 $$\circ$$은 *Dubrovin connection*이라 부르는, $$M\times \mathbb{C}^\ast$$ 위의 flat connection $$\nabla^z$$로 연결되며, 이 connection은 $$z\rightarrow 0$$일 때 $$\circ$$을, $$z\rightarrow\infty$$일 때 $$\nabla$$를 복원한다. 이것이 말이 되기 위해서는 $$\circ$$을 connection처럼 취급하는 것이 어떤 것인지를 다소 정당화해야 한다.

일반적으로 connection은 local frame에서 $$\nabla_{\partial_\alpha} = \partial_\alpha + A_\alpha$$ 꼴로 적히며, 여기서 $$A_\alpha$$는 fiber 위의 endomorphism인 connection $$1$$-form이다. ([\[리만기하학\] §접속, ⁋정의 3](/ko/math/riemannian_geometry/connection#def3)) 핵심적인 관찰은 product $$\circ$$가 각 방향 $$\partial_\alpha$$에 대해 "$$\partial_\alpha$$를 곱하는" endomorphism $$\mathcal{C}_\alpha = \partial_\alpha \circ -$$을 생각하면 그 행렬 성분이 바로 product의 구조상수 $$c_{\alpha\beta}^\gamma$$라는 점이다. 즉, 엄밀히는 $$\circ$$ 그 자체가 connection인 것이 아니라, 그 구조상수들이 Christoffel symbol의 역할을 맡는 것이다. ([\[리만기하학\] §레비-치비타 접속, ⁋명제 6](/ko/math/riemannian_geometry/Levi-Civita_connection#prop6))

실제로, (flat) coordinate $$\{ t^\alpha \}$$를 택하면

$$\mathcal{C}_\alpha(\partial_\beta) = \partial_\alpha \circ \partial_\beta = \sum_\gamma c_{\alpha\beta}^\gamma\, \partial_\gamma$$

임을 바로 확인할 수 있다. 따라서, 이 둘을 잇는 connection

$$\nabla^z_{\partial_\alpha} = \partial_\alpha + \frac{1}{z}\, \mathcal{C}_\alpha$$

를 생각하면, $$z \to \infty$$에서는 Levi-Civita connection $$\nabla$$로 수렴하고 $$z \to 0$$에서는 product $$\circ$$의 classical limit으로 발산하는 하나의 family로 묶을 수 있으며, 실제로 $$z\rightarrow 0$$인 계산을 할 때는 이를 rescale하여 $$z\nabla^z_{\partial_\alpha} = z\partial_\alpha + \mathcal{C}_\alpha$$의 $$z \to 0$$ leading term으로 빼내면 된다. 어쨌든, 이러한 의미에서 $$\nabla^z$$는 두 구조를 연결하는 *flat pencil of connections*이며, 물리적으로는 이를 string coupling constant로 해석한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Frobenius manifold $$M$$과 auxiliary complex parameter $$z \in \mathbb{C}^\ast$$를 생각하자. 그럼 *Dubrovin connection* $$\nabla^z$$는 projection

$$\pr_1: M\times \mathbb{C}^\ast \rightarrow M$$

을 통해 정의되는 pullback bundle $$\pr_1^\ast TM$$ 위에 정의되는 connection으로, $$M$$의 flat coordinate $$\{ t^\alpha \}$$에 대하여 다음의 식

$$\nabla^z_{\partial_\alpha} = \partial_\alpha + \frac{1}{z}\, \mathcal{C}_\alpha, \qquad \mathcal{C}_\alpha(X) := \partial_\alpha \circ X$$

으로 주어지는 것이다. 여기서 $$\mathcal{C}_\alpha$$는 위에서 정의한 endomorphism $$\partial_\alpha\circ-$$이다. 남은 방향인 $$z$$ 방향으로의 connection 성분은 다음의 식

$$\nabla^z_{\partial_z} = \partial_z - \frac{1}{z^2}E\circ(-) + \frac{1}{z}\mu$$

으로 주어진다. 여기서 $$E$$는 Euler vector field ([§프로베니우스 다양체, ⁋정의 5](/ko/math/mirror_symmetry/frobenius_manifold#def5))이고, $$\mu$$는 *grading operator*로, flat coordinate $$t^\alpha$$에 대응하는 cohomology class $$\sigma^\alpha$$의 절반 차수 $$d_\alpha = \tfrac{1}{2}\deg\sigma^\alpha$$와 conformal dimension $$d$$로부터 $$\mu(\partial_\alpha) = (d_\alpha - d/2)\, \partial_\alpha$$로 정의된다.

</div>

앞서 [§프로베니우스 다양체, ⁋정의 5](/ko/math/mirror_symmetry/frobenius_manifold#def5)에서 Frobenius manifold를 정의할 때, 각 점에서의 Frobenius algebra의 grading structure를 담기 위해 $$E$$를 도입했던 것을 기억하자. 구체적으로, 

$$\Lie_E(\circ)=\circ,\qquad \Lie_E(\eta)=(2-d)\eta$$

는 quantum product가 degree를 respect한다는 사실과 Poincaré pairing이 top degree에 concentrate된다는 사실을 각각 반영하는 것이었다. 위의 식에서 Euler vector field $$E$$가 base $$M$$ 위에서 좌표의 rescaling을 생성하는 grading이라면, $$\mu$$는 같은 grading을 fiber $$T_tM \cong H^\ast(X)$$ 위의 endomorphism으로 본 것으로, 둘은

$$\mu = \frac{2-d}{2}I - \nabla E$$

로 연결된다. 여기서 $$I$$는 $$H^\ast(X)$$ 위의 항등행렬이다. 이를 더 직관적으로 보기 위해 $$\nabla$$에 대한 flat coordinate에서 직접 적어보면, $$E$$는

$$E = \sum_\alpha (1-d_\alpha)t^\alpha \partial_\alpha + \text{(constant terms)}$$

이므로, $$\nabla E$$는 eigenvector $$\partial_\alpha$$에 대응되는 eigenvalue $$1-d_\alpha$$를 갖는다는 것을 안다. 이제 이를 $$\mu = \frac{2-d}{2}I - \nabla E$$에 대입하면, 

$$\mu(\partial_\alpha) = \frac{2-d}{2} - (1-d_\alpha) = d_\alpha - d/2$$

이므로 $$\mu$$ 또한 eigenvalue $$d_\alpha-d/2$$를 갖는다. 여기서 $$\frac{2-d}{2}$$만큼의 이동은 $$\mu$$를 $$\eta$$에 대해 skew-symmetric하게 만들기 위한 것으로, $$\eta$$가 차수 $$d_\alpha$$인 class를 차수 $$d - d_\alpha$$인 것과 짝짓는 데서 비롯한다.

Dubrovin connection의 가장 중요한 성질은 이것이 모든 $$z$$에 대해 flat이라는 것이다. 이를 확인하기 위해 곡률 $$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}]$$을 계산하자. Flat coordinate에서 $$\nabla^z_{\partial_\alpha} = \partial_\alpha + z^{-1}\mathcal{C}_\alpha$$이고, $$[\partial_\alpha, \partial_\beta] = 0$$이며 Leibniz 법칙에 의해 $$[\partial_\alpha, \mathcal{C}_\beta] = \partial_\alpha \mathcal{C}_\beta$$ ($$\mathcal{C}_\beta$$의 성분을 미분한 endomorphism)이므로,

$$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}] = [\partial_\alpha + z^{-1}\mathcal{C}_\alpha,\ \partial_\beta + z^{-1}\mathcal{C}_\beta] = \frac{1}{z}\,(\partial_\alpha \mathcal{C}_\beta - \partial_\beta \mathcal{C}_\alpha) + \frac{1}{z^2}\,[\mathcal{C}_\alpha, \mathcal{C}_\beta]$$

로 전개된다. 이 곡률이 모든 $$z$$에서 vanish하려면 $$z^{-1}$$과 $$z^{-2}$$의 계수가 각각 사라져야 하는데, $$z^{-1}$$ 항은 $$\mathcal{C}$$의 *potentiality* $$\partial_\alpha\mathcal{C}_\beta = \partial_\beta\mathcal{C}_\alpha$$에서, $$z^{-2}$$ 항은 product의 *associativity* $$[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$$에서 사라진다. 

뿐만 아니라 다음 명제는 이러한 connection들의 flatness가 *정확하게* 이 두 조건과 동치임을 보여준다. 이들은 Frobenius manifold ([§프로베니우스 다양체, ⁋정의 5](/ko/math/mirror_symmetry/frobenius_manifold#def5))의 공리들이었으며, 따라서 $$\nabla^z$$의 $$M$$-방향 flatness는 단순히 moduli를 맞추기 위한 결과가 아니라 Frobenius structure 그 자체라 할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Frobenius manifold $$M$$ 위의 connection $$\nabla^z$$ ([정의 1](#def1))를 생각하자. Product $$\circ$$가 commutative라는 가정 아래, $$\nabla^z$$가 모든 $$z$$에 대해 $$M$$-방향 (즉 $$\partial_\alpha$$ 방향들 사이)으로 flat인 것은 다음 두 조건이 모두 성립하는 것과 동치이다.

1. **Potentiality:** $$\partial_\alpha\, c_{\beta\gamma}^\delta = \partial_\beta\, c_{\alpha\gamma}^\delta$$. 즉 $$c_{\alpha\beta}^\delta$$가 어떤 potential $$F$$의 세 번째 도함수이다.
2. **Associativity (WDVV):** $$[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$$, 성분으로는 $$\sum_\delta c_{\alpha\beta}^\delta\, c_{\delta\gamma}^\epsilon = \sum_\delta c_{\beta\gamma}^\delta\, c_{\alpha\delta}^\epsilon$$. 즉 $$\circ$$가 associative이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위에서 한쪽 방향은 이미 보있으므로 역방향만 확인하면 된다. $$\nabla^z$$가 모든 $$z \in \mathbb{C}^\ast$$에 대해 flat이라 하자. 곡률

$$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}] = \frac{1}{z}\,(\partial_\alpha\mathcal{C}_\beta - \partial_\beta\mathcal{C}_\alpha) + \frac{1}{z^2}\,[\mathcal{C}_\alpha, \mathcal{C}_\beta]$$

은 $$z^{-1}$$과 $$z^{-2}$$에 대한 Laurent polynomial이므로, 이것이 모든 $$z$$에서 vanish하는 것은 두 계수가 따로 vanish하는 것과 동치이다. $$z^{-1}$$ 계수의 vanishing은 곧 첫째 조건 $$\partial_\alpha\mathcal{C}_\beta = \partial_\beta\mathcal{C}_\alpha$$이며, $$z^{-2}$$ 계수의 vanishing $$[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$$을 성분으로 적으면 $$\sum_\delta (c_{\alpha\delta}^\epsilon c_{\beta\gamma}^\delta - c_{\beta\delta}^\epsilon c_{\alpha\gamma}^\delta) = 0$$인데, $$\circ$$가 commutative라는 가정 아래 이것은 정확히 associativity, 즉 WDVV equation과 동치이다. ([§프로베니우스 다양체, ⁋명제 7](/ko/math/mirror_symmetry/frobenius_manifold#prop7))

</details>

한편 $$z$$-방향의 flatness $$[\nabla^z_{\partial_z}, \nabla^z_{\partial_\alpha}] = 0$$은 Euler vector field $$E$$와 grading operator $$\mu$$가 product와 호환된다는 조건, 즉 Frobenius manifold의 homogeneity (또는 conformal) condition을 요구한다. 이 조건은 [§프로베니우스 다양체, ⁋정의 5](/ko/math/mirror_symmetry/frobenius_manifold#def5)의 네 번째 조건으로 이미 우리의 정의 안에 들어 있으므로, 우리의 정의에서는  $$z$$-방향까지 포함한 $$\nabla^z$$의 온전한 flatness가 얻어진다.

## D-module

Connection $$\nabla$$는 본질적으로 section을 *미분*하는 도구이다. Vector bundle을 $$\mathcal{O}_X$$-module로 볼 때 우리가 가진 연산은 함수와의 곱셈뿐이지만, 미분까지 할 수 있게 되면 그 bundle은 함수에 더해 미분연산자들의 작용까지 받는 대상, 곧 *$$\mathcal{D}_X$$-module*이 되며, 이것이 flat이어야 그 정의가 말이 될 것이다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Complex manifold $$B$$ 위에서, *$$B$$ 위 미분 연산자들의 sheaf of rings* $$\mathcal{D}_B$$는 structure sheaf $$\mathcal{O}_B$$와 vector field들 ($$\mathcal{O}_B$$ 위의 derivation, [\[가환대수학\] §미분, ⁋정의 1](/ko/math/commutative_algebra/differentials#def1))이 생성하는 operator들의 sheaf이다. 이 때, vector field $$\partial$$과 함수 $$f$$는 다음의 관계식

$$[\partial, f] = \partial(f)$$

를 만족한다. 이제 $$\mathcal{D}_B$$-action이 정의된 $$\mathcal{O}_B$$-module $$\mathcal{M}$$을 *$$\mathcal{D}_B$$-module*이라 부른다. 

</div>

$$\mathcal{M}$$ 위에 $$\mathcal{O}_B$$-module 구조는 보편적으로 함수 $$f\in \mathcal{O}_B$$와의 곱셈으로 생각한다. 그럼 임의의 section $$s\in \mathcal{M}$$에 대하여, 관계식 $$[\partial, f]=\partial(f)$$는 다음의 Leibniz 법칙

$$\partial(f s) = (\partial f)\, s + f\, \partial s \qquad (f \in \mathcal{O}_B,\ s \in \mathcal{M})$$

을 만족하는 것을 확인할 수 있다. 

구체적인 예시로, flat connection $$\nabla$$가 주어진 vector bundle $$E\rightarrow B$$가 주어지면, vector field $$\partial$$의 action을 $$\nabla_\partial$$로 정의하면 $$E$$는 $$\mathcal{D}_B$$-module이 되며, 이 예시에서 $$\nabla$$의 flatness $$[\nabla_\partial, \nabla_{\partial'}] = \nabla_{[\partial, \partial']}$$가 정확히 $$\mathcal{D}_B$$-module의 정의가 요구하는 commutator relation이 된다. 

특별히 우리는 Dubrovin connection $$\nabla^z$$가 flat인 것을 보았으므로 ([명제 2](#prop2)) 이로부터 $$\pr_1^\ast TM$$이 $$\mathcal{D}_{M\times \mathbb{C}^\ast}$$-module이 됨을 확인할 수 있다. 이를 *quantum $$D$$-module*이라 부른다. 이 때, $$\mathcal{D}$$-module의 horizontal section, 즉 $$\nabla^z s=0$$을 만족하는 함수들을 flat coordinate을 이용해 $$s=\sum_\alpha s^\alpha\partial_\alpha$$로 적으면 다음의 미분방정식

$$\partial_\alpha s^\beta + \frac{1}{z} \sum_\gamma c_{\alpha\gamma}^\beta\, s^\gamma = 0$$

을 얻고, 이를 *quantum differential equation*이라 부른다. 한편 위의 방정식은 first order linear ODE이므로, base point $$b_0$$와 초기조건 $$s(b_0)$$이 주어지면 경로를 따라 그 해가 유일하게 결정되고, $$\nabla^z$$가 flat이므로 이 parallel transport가 경로에 무관하여 $$b_0$$의 simply connected neighborhood에서 well-defined horizontal section을 준다. 따라서 위의 QDE의 solution space는 다발의 rank와 일치하는 $$\dim_\mathbb{C} M$$차원이 되며, base $$M \times \mathbb{C}^\ast$$의 $$\pi_1$$이 평행이동을 통해 이 해 공간에 작용하여 monodromy representation을 준다. 특히 $$z$$-방향 $$\mathbb{C}^\ast$$의 loop ($$\pi_1 \cong \mathbb{Z}$$)은 $$z = 0, \infty$$의 irregular singularity 둘레 monodromy를, Novikov 좌표 $$q = e^t$$의 $$q$$-방향 loop은 quantum monodromy를 준다. 

특히 $$M = H^\ast(X, \mathbb{C})$$이고 $$c_{\alpha\beta}^\gamma$$가 small quantum product $$\star_q$$의 구조상수일 때 QDE는

$$z\, q_a \partial_{q_a} s = -\,(T_a \star_q s), \qquad a = 1, \ldots, r$$

의 형태가 된다. 여기서 $$\{ T_a \}$$는 $$H^2(X, \mathbb{C})$$의 basis, $$q_a = e^{t^a}$$는 대응하는 Novikov variable이며, 우변의 부호는 [정의 1](#def1)의 $$+z^{-1}\mathcal{C}_\alpha$$ 약속을 따른 것이다. 이 QDE의 fundamental solution이 Gromov-Witten invariant들의 생성함수로 명시적으로 풀린다는 것이 Givental formalism의 핵심이며, 이는 ([§Givental J-function과 Mirror Theorem](/ko/math/mirror_symmetry/givental_j_function))에서 다룬다.

이처럼 quantum $$D$$-module은 주로 $$X$$의 Gromov-Witten 이론, 즉 A-model 데이터로 해석되므로 *A-model $$D$$-module*이라 부르기도 한다.

같은 일이 mirror의 B-model 측에서도 일어난다. $$X$$의 mirror를 $$\check{X}$$로 적자 (Fano $$X$$의 경우 Landau-Ginzburg model $$(\check{X}, W_q)$$). 거기에는 quantum $$D$$-module과 비슷한 역할을 하는 flat connection, 곧 *Gauss-Manin connection* $$\nabla^{GM}$$이 있어, $$\check{X}$$의 Jacobi ring $$\Jac(W_q)$$가 deformation parameter $$q$$를 따라 이루는 family에 작용하여 이를 하나의 $$\mathcal{D}$$-module, 곧 *Gauss-Manin system*으로 만든다. 이 connection과 그 flat section을 이루는 oscillating integral의 구체적 구성은 ([§Oscillating Integral과 Gauss–Manin System](/ko/math/mirror_symmetry/oscillating_integral))에서 다룬다.

이로써 mirror symmetry를 한 단계 끌어올릴 수 있다. [§거울대칭 개요](/ko/math/mirror_symmetry/overview)에서 본 ring isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$는, 이제 두 $$\mathcal{D}$$-module — A-model quantum $$D$$-module과 B-model Gauss-Manin system — 이 connection까지 호환되며 isomorphic하다는 더 강한 진술로 격상된다.

<div class="proposition" markdown="1">

<ins id="conj4">**주장 4** (Mirror theorem, $$D$$-module form)</ins> Mirror pair $$(X, \check{X})$$에 대해 A-model state space $$H_A := H^\ast(X, \mathbb{C}[z^{\pm 1}, q^{\pm 1}])$$와 B-model state space $$H_B := H^n_{dR}(\check{X})[z^{\pm 1}, q^{\pm 1}]$$ 사이의 *mirror isomorphism*

$$\Phi: H_A \xrightarrow{\sim} H_B$$

가 존재하여, $$\Phi$$가 Dubrovin connection과 Gauss-Manin connection을 호환시킨다.

$$\Phi \circ \nabla^z = \nabla^{GM} \circ \Phi$$

</div>

두 state space가 어떻게 생겼는지는 $$\mathbb{P}^1$$로 보면 분명하다. $$H_A$$는 cohomology $$H^\ast(X)$$를 spectral parameter $$z$$와 Novikov variable $$q$$의 Laurent 다항식 환 $$\mathbb{C}[z^{\pm 1}, q^{\pm 1}]$$ 위로 확장한 자유 가군, 곧 quantum $$D$$-module의 state space이고, $$H_B$$는 mirror 측 Jacobi ring(relative de Rham cohomology)을 같은 환 위에서 본 것이다. 예컨대 $$X = \mathbb{P}^1$$이면 $$H^\ast(\mathbb{P}^1) = \langle 1, H\rangle$$이 rank $$2$$이고, mirror $$\check{X}$$의 superpotential $$W_q = x + q/x$$의 Jacobi ring $$\Jac(W_q) = \mathbb{C}[x^{\pm 1}]/(1 - q/x^2)$$ 또한 critical point $$x = \pm\sqrt{q}$$ 두 개에 대응하여 rank $$2$$이다. 일반적으로 두 state space는 모두 $$\dim_\mathbb{C} H^\ast(X)$$ (= $$W_q$$의 critical point 수)를 rank로 갖는 자유 가군이며, *mirror isomorphism* $$\Phi$$는 이 둘을 connection까지 호환되도록 식별한다.

[주장 4](#conj4)는 일반적인 statement로서 *각 mirror pair에 대해* 별도로 증명되어야 한다. 가장 먼저 증명된 경우는 Calabi-Yau hypersurface in toric variety로, Givental [Giv]과 Lian-Liu-Yau가 *mirror theorem*으로 증명하였고, 그 핵심은 Givental의 $$J$$-function이 oscillating integral의 stationary phase asymptotic과 일치한다는 것이다. Toric Fano variety의 경우 Givental은 이 isomorphism의 명시적 construction을 제시하였고, Iritani는 이것이 integral structure(Gamma class)와도 호환됨을 보였다 [Iri].

$$z \to 0$$ limit을 취하면 $$\nabla^z$$의 leading term은 product $$\circ$$가 되고 $$\nabla^{GM}$$의 leading term은 superpotential $$W_q$$의 derivative가 되므로, [주장 4](#conj4) isomorphism의 leading term은 정확히 위의 ring isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$이다. 이러한 의미에서 $$D$$-module 동형은 ring 동형의 *full quantum-level extension*이다.

한편 $$\nabla^z$$는 $$z = 0$$과 $$z = \infty$$에서 irregular singularity를 가진다. $$z \to 0$$은 앞서 본 product $$\circ$$로의 classical limit이고, $$z = \infty$$ 쪽은 grading operator $$\mu$$가 monodromy를 지배한다. 특히 semisimple Frobenius manifold에서 fundamental solution은 $$\Psi(z) \sim \Psi_0\, e^{U/z}$$ ($$U$$는 critical value들의 대각행렬) 꼴의 stationary-phase asymptotic을 가지며, 이것이 B-model oscillating integral $$\int_\Gamma e^{W_q/z}\omega$$의 asymptotic과 일치한다는 것이 [주장 4](#conj4)를 구체적으로 실현하는 길이다. 이를 명시적으로 적은 것이 Givental의 $$J$$-function으로, ([§Givental J-function과 Mirror Theorem](/ko/math/mirror_symmetry/givental_j_function))에서 다룬다.

---

**참고문헌**

**[Dub]** B. Dubrovin, *Geometry of $$2$$D topological field theories*, Integrable systems and quantum groups (Montecatini Terme, 1993), Lecture Notes in Math. **1620**, Springer, 1996, 120--348.

**[Giv]** A. Givental, *Equivariant Gromov-Witten invariants*, Internat. Math. Res. Notices **1996**, no. 13, 613--663.

**[Iri]** H. Iritani, *An integral structure in quantum cohomology and mirror symmetry for toric orbifolds*, Adv. Math. **222** (2009), no. 3, 1016--1079.

**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.
