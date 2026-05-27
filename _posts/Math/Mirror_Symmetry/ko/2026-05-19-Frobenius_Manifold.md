---title: "프로베니우스 다양체"
description: "프로베니우스 대수의 정의를 시작으로, 각 점에서 프로베니우스 대수 구조를 갖는 프로베니우스 다양체의 개념과 WDVV 방정식을 살펴보며, 거울대칭과 양자 코호몰로지, 야코비 환과의 관계를 다룬다."
excerpt: "Frobenius manifold와 WDVV equation"

categories: [Math / Mirror Symmetry]
permalink: /ko/math/mirror_symmetry/frobenius_manifold
sidebar:
    nav: "mirror_symmetry-ko"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/frobenius_manifold.png
    overlay_filter: 0.5

date: 2026-05-19
last_modified_at: 2026-05-19
weight: 3

---

우리는 [§거울대칭 개요](/ko/math/mirror_symmetry/overview)에서 toric Fano variety $$X_\Sigma$$의 mirror symmetry가 Jacobi ring과 quantum cohomology 사이의 isomorphism 

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

로 요약된다는 것을 살펴보았다. 그러나 해당 글에서도 살펴보았듯 quantum cohomology는 이 ring 동형이 잡아내는 것 이상의 구조를 갖는데, 이는 Novikov parameter $$q$$의 변화에 따라 product 자체가 변형되기 때문이다. 이러한 deformation을 담아낼 수 있는 구조가 Frobenius로, 이번 글에서 우리는 우선 finite-dimensional Frobenius algebra의 정의를 짚은 뒤 Dubrovin의 Frobenius manifold 개념과 WDVV equation을 차례로 살펴본다.

## 프로베니우스 대수

Frobenius manifold는 직관적으로 각 점에서 Frobenius algebra structure를 갖는 manifold이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Finite-dimensional commutative, associative $$\mathbb{C}$$-algebra $$A$$와 그 위에 정의된 non-degenerate symmetric bilinear form $$\eta: A \otimes A \to \mathbb{C}$$가 주어졌다 하자. 만일 모든 원소 $$x,y,z\in A$$에 대하여 다음의 식

$$\eta(x \cdot y,z) = \eta(x,y \cdot z)$$

이 성립한다면, 이 pair $$(A, \eta)$$를 *Frobenius algebra<sub>프로베니우스 대수</sub>*라 부른다.

</div>

위 조건은 $$A$$의 곱셈 $$\cdot : A \otimes A \to A$$와 bilinear form $$\eta$$가 호환되어, 세 인수 모두에 대해 대칭인 trilinear form $$c(x,y,z) := \eta(x \cdot y,z)$$를 정의함을 의미한다. 실제로 commutativity로부터 

$$c(x,y,z) = \eta(x \cdot y,z) = \eta(y \cdot x,z) = c(y,x,z)$$

이고, Frobenius 조건으로부터 

$$c(x,y,z) = \eta(x,y \cdot z) = \eta(y \cdot z, x) = c(y,z,x)$$

이다. 따라서 $$c$$는 세 변수에 대해 완전히 symmetric하며, 이 trilinear form이 Frobenius structure의 모든 정보를 담고 있다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Compact Kähler manifold $$X$$의 cohomology ring $$H^\ast(X, \mathbb{C})$$는 cup product와 Poincaré pairing

$$\eta(\alpha, \beta) = \int_X \alpha \smile \beta$$

에 대해 Frobenius algebra이다. 이는 다음의 식

$$\eta(\alpha \smile \beta, \gamma) = \eta(\alpha, \beta \smile \gamma)$$

이 모든 $$\alpha,\beta,\gamma$$에 대해 성립한다는 것이며, 이 식은 cup product의 결합법칙으로 얻어지는 것이다. 

</div>

한편, 우리는 [§거울대칭 개요](/ko/math/mirror_symmetry/overview)의 예시에서 Landau-Ginzburg model을 소개했는데, 이는 주어진 manifold $$\check{X}$$ 위에 주어진 holomorphic function $$W$$로 이루어지며, $$W$$의 critical point들을 담고 있는 Jacobi ring이 B-model의 정보를 들고 있었다. 국소적으로 이는 다음과 같이 적힌다. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Holomorphic function $$f : \mathbb{C}^n \to \mathbb{C}$$가 원점에서 *isolated hypersurface singularity*를 갖는다는 것은 다음의 두 조건이 성립하는 것이다.

1. $$f(0) = 0$$, $$df(0) = 0$$.
2. 원점이 $$f$$의 critical point들 중 *isolated*인 것, 즉 원점의 어떤 근방 안에서 $$df = 0$$의 해가 원점 하나뿐이다.

</div>

표준적인 예시는 $$f(\x) = \x^{k+1}$$ ($$k \geq 1$$)이며, 우리는 이를 $$A_k$$-type singularity라 부른다. 

이제 다항식 $$f:\mathbb{C}^n \rightarrow \mathbb{C}$$의 모든 critical point가 isolated hypersurface singularity라 하자. 그럼 우리는 그 *Jacobi ring*

$$\Jac(f) = \mathbb{C}[\x_1, \ldots, \x_n]/(\partial_1 f, \ldots, \partial_n f)$$

을 생각할 수 있다. 그 차원 $$\mu(f)=\dim \Jac(f)$$는 $$f$$의 singularity의 개수를 order를 포함해서 센 것으로, 직관적으로는 약간의 perturbation을 통하여 $$\mu(f)$$개의 simple critical point들을 갖는 것으로 생각할 수도 있다. Singularity theory에서는 이 $$\mu(f)$$를 $$f$$의 *Milnor number*라 부른다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 모든 critical point가 isolated hypersurface singularity인 다항식 $$f : \mathbb{C}^n \to \mathbb{C}$$의 Jacobi ring $$\Jac(f)$$ 위에 *residue pairing* $$\eta$$를 다음의 식

$$\eta(g, h) := \frac{1}{(2\pi i)^n} \oint_{\Gamma_\epsilon} \frac{g(\x) h(\x) \, d\x_1 \wedge \cdots \wedge d\x_n}{\partial_1 f \cdots \partial_n f}$$

으로 정의한다. 여기서 적분경로 $$\Gamma_\epsilon$$은 $$\Crit(f)=\{df=0\}$$의 모든 점을 둘러싸는 작은 contour 위에서 이루어지는 것으로, 이 적분은 critical point를 multiplicity 정보가 포함된 fat point로 봤을 때 해당 점에서의 적분값이라 생각할 수 있다. 

즉, 직관적으로 이는 [예시 2](#ex2)의 manifold 전체 적분 $$\int_X$$를 critical scheme의 (유한 개) 점들에서의 적분으로 localize한 것으로 생각할 수 있으며, $$(\Jac(f), \eta)$$가 실제로 Frobenius algebra가 되는 것도 해당 예시에서와 비슷한 방식으로 보일 수 있다.

일반적으로 $$f$$의 모든 critical point가 *non-degenerate*인 경우, 즉 각 $$p \in \Crit(f)$$에서 Hessian $$\Hess_p(f) = (\partial_i \partial_j f(p))_{ij}$$가 invertible한 경우, 위의 적분은

$$\eta(g, h) = \sum_{p \in \Crit(f)} \frac{g(p)\, h(p)}{\det \Hess_p(f)}$$

로 간단히 계산할 수 있으며, 더 근본적으로는 $$\Jac(f)$$ 자체가

$$\Jac(f)=\bigoplus_{p\in \Crit(f)}\mathbb{C}$$

로 분해되며, 이 basis에 대하여 residue pairing은 critical point basis 위에서 $$\operatorname{diag}(1/\det \Hess_p(f))$$로 대각화되는 것을 확인할 수 있다. 

특별한 예시로 [§거울대칭 개요, ⁋예시 5](/ko/math/mirror_symmetry/overview#ex5)에서 본 $$\mathbb{P}^1$$의 Hori-Vafa superpotential

$$W_q = \x + \frac{q}{\x}$$

를 생각하면, 그 critical point는 $$\x_\pm = \pm\sqrt{q}$$ 두 점이다. 

다소 주의할 것은 ambient space $$\check{X}$$은 affine space가 아니라 algebraic torus라는 것으로, 이 위에 정의된 differential form은 단순히 $$d\x$$가 아니라는 것이다. 실제로 이 위의 differential form은 [\[토릭 기하학\] §토릭 다양체 위의 로그 미분형식, ⁋정의 1](/ko/math/toric_geometry/logarithmic_differentials#def1)에 의하여 $$d\x/\x$$로 주어지며, 이는 torus 위의 좌표가 $$\u=\log\x$$로 주어진 것이라 보면 된다. 그럼 $$d\u=d\x/\x$$이고 $$\partial_\u=\x\partial_\x$$가 되며, Hessian을 계산하기 위해 이 좌표에서 $$W_q$$의 도함수를 차례로 구하면

$$\partial_\u W_q = \x \partial_\x W_q = \x - q/\x, \qquad \partial_\u^2 W_q = \partial_\u(\x - q/\x) = \x + q/\x$$

가 되며, critical point $$\x_\pm = \pm\sqrt{q}$$에서는

$$\Hess_{\x_\pm}(W_q)=\partial_\u^2 W_q \big\vert_{\x_\pm} = \x_\pm + q/\x_\pm = 2\x_\pm = \pm 2\sqrt{q}$$

가 된다. 위 식을 두 critical point에 대해 적용하면 residue pairing은

$$\eta(g, h) = \frac{g(\sqrt{q})\,h(\sqrt{q})}{2\sqrt{q}} + \frac{g(-\sqrt{q})\,h(-\sqrt{q})}{-2\sqrt{q}}$$

가 된다. 이제 이를 $$\Jac(W_q) = \mathbb{C}[\x^{\pm 1}, q^{\pm 1}]/(\x^2 - q)$$의 basis $$\{1, \x\}$$ 위에서 직접 계산하면

$$\eta(1, 1) = \frac{1}{2\sqrt{q}} + \frac{1}{-2\sqrt{q}} = 0, \qquad \eta(1, \x) = \frac{\sqrt{q}}{2\sqrt{q}} + \frac{-\sqrt{q}}{-2\sqrt{q}} = 1, \qquad \eta(\x, \x) = \frac{q}{2\sqrt{q}} + \frac{q}{-2\sqrt{q}} = 0$$

이 되어, 이 basis에 대한 $$\eta$$의 행렬표현은 $$\begin{pmatrix}0&1\\1&0\end{pmatrix}$$이다. 이는 정확히 $$\mathbb{P}^1$$의 classical Poincaré pairing과 일치하며, ring isomorphism $$\Jac(W_q) \cong QH^\ast(\mathbb{P}^1)$$이 실은 Frobenius algebra isomorphism이었음을 보여준다.

같은 방식으로 [§거울대칭 개요, ⁋예시 6](/ko/math/mirror_symmetry/overview#ex6)에서 본 $$\mathbb{P}^2$$의 Hori-Vafa superpotential

$$W_q = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}$$

를 생각하자. Log coordinate $$\u_i = \log \z_i$$에서 $$W_q$$의 도함수를 구하면

$$\partial_{\u_1} W_q = \z_1 - q/(\z_1 \z_2), \qquad \partial_{\u_2} W_q = \z_2 - q/(\z_1 \z_2)$$

이고, 둘 모두가 $$0$$이라 하면 $$\z_1 = \z_2 = \z$$이고 $$\z^3 = q$$여야 하므로 critical point는 세 점

$$\z_k = \omega^k q^{1/3},\qquad k = 0, 1, 2$$

으로 주어지며 $$\Jac(W_q) \cong \mathbb{C}[\z, q^{\pm 1}]/(\z^3 - q)$$는 basis $$\{1, \z, \z^2\}$$를 갖는다. Hessian을 계산하기 위해 log coordinate에서 $$W_q$$의 이계 도함수를 모으면

$$\Hess(W_q) = \begin{pmatrix} \z_1 + \frac{q}{\z_1 \z_2} & \frac{q}{\z_1 \z_2} \\ \frac{q}{\z_1 \z_2} & \z_2 + \frac{q}{\z_1 \z_2} \end{pmatrix}$$

이며, critical point에서는 $$q/(\z_1 \z_2) = \z^3/\z^2 = \z$$이므로

$$\Hess_{\z_k}(W_q) = \begin{pmatrix} 2\z_k & \z_k \\ \z_k & 2\z_k \end{pmatrix}, \qquad \det \Hess_{\z_k}(W_q) = 3\z_k^2$$

가 된다. 위 식을 세 critical point에 대해 적용하면 residue pairing은

$$\eta(\z^a, \z^b) = \sum_{k=0}^{2} \frac{(\omega^k q^{1/3})^{a+b}}{3 (\omega^k q^{1/3})^2} = \frac{q^{(a+b-2)/3}}{3} \sum_{k=0}^{2} \omega^{k(a+b-2)}$$

이고, 

$$\sum_{k=0}^{2} \omega^{km} = 3\iff m \equiv 0 \pmod 3$$

이며 그 외의 경우에는 이 값이 $$0$$이 된다. 즉, $$0 \leq a, b \leq 2$$에서는 $$a + b = 2$$일 때만 $$\eta(\z^a, \z^b) = 1$$이며 그 외의 경우에는 $$0$$이다. 즉 이 basis에 대한 $$\eta$$의 행렬표현은 이번 경우에도 $$\mathbb{P}^2$$의 classical Poincaré pairing과 일치하는 다음의 행렬

$$\begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$$

로 주어지는 것을 확인할 수 있다.

</div>

## 프로베니우스 다양체

앞선 절에서 우리는 프로베니우스 대수를 정의하고, 이것이 mirror symmetry의 ring isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$를 Frobenius algebra 차원으로 격상시킨다는 것을 확인하였다. 그러나 mirror symmetry isomorphism

$$\Jac(W_q)\cong QH^\ast(X)$$

는 여전히 그 full power로 state된 게 아닌데, mirror symmetry의 자연스러움이 isomorphism은 일종의 naturality 또한 가진다는 데에 있다. 즉, 이 isomorphism은 $$q$$의 변화를 따라 매끄럽게 변형되는 isomorphism들의 family를 정의하며, 이를 실제로 구현하려면 우선 Frobenius algebra가 특정한 변수 ($$q$$)로 parametrize되는 상황을 생각해야 한다.

이를 위해 우리는 Frobenius manifold의 개념을 정의한다. 당연히 Frobenius manifold는 각 점에서의 tangent space가 Frobenius algebra인 manifold겠지만, 그것이 전부는 아니며, 당연히 이 구조가 base manifold를 따라 매끄럽게 움직여야 한다. 

우선 Frobenius manifold $$M$$ 위에 정의된 tangent bundle $$TM$$에 대하여, $$TM$$의 각 점이 Frobenius algebra여야 하므로, 각각의 점 $$p\in M$$에서 $$T_pM$$은 algebra로서의 곱셈 $$\circ$$, 이 곱셈에 대한 항등원 $$e$$, 그리고 Frobenius algebra의 pairing $$\eta$$가 필요하다. 이들이 smooth structure를 구성하기 위해서는 $$\circ$$는 $$p$$에 대해 smooth하게 변하는 $$\circ_p:T_pM\otimes T_pM\rightarrow T_pM$$이며, $$\eta$$는 smooth non-degenerate bilinear form $$\eta$$가 되어야 할 것이다. 또, 항등원은 $$TM$$의 (smooth) section, 즉 vector field가 되어야 한다. 

미분기하학에서 서로 다른 tangent space를 비교하게 해 주는 것은 connection이었다. ([\[리만기하학\] §접속, ⁋정의 1](/ko/math/riemannian_geometry/connection#def1)) 일반적으로 임의의 pseudo-Riemannian manifold $$M$$ 위에는 항상 그에 호환되는 Levi-Civita connection $$\nabla$$가 존재하므로 ([\[리만기하학\] §레비-치비타 접속, ⁋정리 4](/ko/math/riemannian_geometry/Levi-Civita_connection#thm4)) 이를 사용하면 충분하다. 

한편, 임의의 connection $$\nabla$$가 주어진다면, $$M$$ 위에 놓여진 곡선 $$\gamma$$를 통해 곡선의 시작점 $$x_0$$과 $$x_1$$을 이어주는 *parallel transport*가 존재했다. ([\[리만기하학\] §레비-치비타 접속, ⁋정의 7](/ko/math/riemannian_geometry/Levi-Civita_connection#def7)) Manifold의 점을 parameter로 삼아 Frobenius algebra를 변형하려면 우리는 이 parallel transport를 사용해야 하는데, 이 변형이 한 점에서 다른 점으로 옮기는 곡선에 의존한다면 이는 별로 좋은 상황은 아닐 것이다. ([\[리만기하학\] §리만 곡률, ⁋예시 1](/ko/math/riemannian_geometry/curvature#ex1)) 즉, 우리는 이 $$\nabla$$가 *flat*이기를 바란다. ([\[리만기하학\] §리만 곡률, ⁋정의 6](/ko/math/riemannian_geometry/curvature#def6))

마지막으로 $$QH^\ast(X)$$에는 이미 grading이 주어져있으므로 이를 반영할 데이터가 추가로 필요하다. 여기서 $$QH^\ast(X)$$의 grading은 classical cohomology $$H^\ast(X)$$에 Novikov ring의 grading으로부터 나오는 grading을 더하여 얻어졌던 것을 기억하자. 즉 $$QH^\ast(X) = H^\ast(X) \otimes_\mathbb{C} \Lambda$$라 할 때, 임의의 generator $$T_\alpha \otimes q^\beta$$의 degree는 $$\deg(T_\alpha \otimes q^\beta) = p_\alpha + 2\, c_1 \cdot \beta$$로 주어졌었다. ([\[사교기하학\] §양자 코호몰로지, ⁋정의 2](/ko/math/symplectic_geometry/quantum_cohomology#def2))

이러한 grading 자료를 manifold $$M$$ 위의 *vector field*로 부호화한 것이 *Euler vector field* $$E$$이다. $$E$$의 flow를 따라 곱셈 $$\circ$$를 흘려보냈을 때 그 *무한소 deformation*이 Lie derivative $$\Lie_E(\circ)$$로 주어지는데, [\[사교기하학\] §양자 코호몰로지](/ko/math/symplectic_geometry/quantum_cohomology)에서 살펴본 quantum product가 degree를 respect한다는 사실은 이 deformation이 정확히 $$\circ$$ 자기 자신과 같다는 식

$$\Lie_E(\circ) = \circ$$

으로 나타낼 수 있다. 비슷하게, 우리의 직관에서 $$\eta$$는 Poincaré pairing이며 ([예시 2](#ex2)), 이는 오직 top degree에서만 살아남으므로 이 degree 조건은 

$$\Lie_E(\eta) = (2 - d)\eta$$

로 번역된다. 이제 Euler vector field는 $$\nabla^2 E=0$$을 만족하는 *affine* vector field로, <em-ko>정확하게</em-ko> 이들 두 조건이 $$E$$를 완전하게 결정한다. 

이제 우리는 Frobenius manifold를 정의하기 위한 모든 재료를 완성했다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 쌍 $$(M, \eta, \circ, e, E)$$가 *Frobenius manifold<sub>프로베니우스 다양체</sub>*라는 것은 다음의 조건이 모두 성립하는 것이다. 

1. $$TM$$ 위의 symmetric non-degenerate bilinear form $$\eta$$가 유도하는 Levi-Civita connection이 flat이다. 
2. 각 $$p\in M$$마다 commutative associative product $$\circ_p: T_p M \otimes T_p M \to T_p M$$이 존재하며 이는 $$p$$에 대해 smooth이다. 
3. 모든 점에서 곱셈 $$\circ$$의 항등원이 되는 vector field $$e$$가 존재하며 $$\nabla e = 0$$이다.
4. Affine 조건 $$\nabla^2 E=0$$을 만족하는 vector field $$E$$가 존재하여, 적당한 상수 $$d\in \mathbb{C}$$에 대해
    
    $$\Lie_E(\circ)=\circ,\qquad \Lie_E(\eta)=(2-d)\eta$$

    가 성립한다.
5. 모든 vector field $$X,Y,Z$$에 대해 $$\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$$가 성립한다.
6. (Potentiality) Trilinear form $$c(X,Y,Z):=\eta(X\circ Y, Z)$$가 정의하는 $$4$$-tensor $$\nabla c$$는 네 변수에 대하여 모두 대칭이다. 

</div>

## WDVV equation

[정의 5](#def5)의 마지막 조건이 potentiality라 불리는 이유는 이것이 trilinear form $$c$$를 적절한 scalar function $$F:M \rightarrow \mathbb{C}$$의 삼계도함수로 표현해주기 때문이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Frobenius manifold $$(M, \eta, \circ, e, E)$$의 flat coordinate $$t^1, \ldots, t^n$$에 대해, $$M$$ 위에 (국소적으로) 정의된 holomorphic function $$F: M \to \mathbb{C}$$가 존재하여

$$c_{\alpha\beta\gamma}(t) := \eta(\partial_{t^\alpha} \circ \partial_{t^\beta}, \partial_{t^\gamma}) = \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\gamma}$$

가 모든 $$\alpha, \beta, \gamma$$에 대해 성립한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Flat coordinate $$t^\alpha$$에 대해 $$\nabla_{\partial_{t^\delta}}$$는 단순한 편미분 $$\partial_{t^\delta}$$와 일치하므로, [정의 5](#def5)의 potentiality 조건은

$$\partial_{t^\delta} c_{\alpha\beta\gamma} = \partial_{t^\alpha} c_{\delta\beta\gamma}$$

가 네 인덱스에 대해 대칭으로 성립한다는 의미이다. 한편 $$c$$ 자체가 세 인덱스에 대해 대칭이므로, 이를 함께 모으면 1-form $$\omega_{\beta\gamma} := \sum_\alpha c_{\alpha\beta\gamma} dt^\alpha$$가 closed임을 얻는다. Poincaré lemma로부터 국소적으로 함수 $$G_{\beta\gamma}$$가 존재해 $$\partial_{t^\alpha} G_{\beta\gamma} = c_{\alpha\beta\gamma}$$이며, $$c$$의 대칭성으로부터 $$G_{\beta\gamma} = G_{\gamma\beta}$$이고 또한 $$\partial_{t^\alpha} G_{\beta\gamma} = \partial_{t^\beta} G_{\alpha\gamma}$$가 성립한다. 다시 Poincaré lemma를 한 단계 더 적용하면 함수 $$H_\gamma$$가 존재해 $$\partial_{t^\beta} H_\gamma = G_{\beta\gamma}$$이고, $$H_\gamma$$의 대칭성 $$\partial_{t^\delta} H_\gamma = \partial_{t^\gamma} H_\delta$$로부터 마지막으로 scalar function $$F$$가 존재해 $$\partial_{t^\gamma} F = H_\gamma$$가 성립한다. 종합하면 $$\partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F = c_{\alpha\beta\gamma}$$이다.

</details>

이러한 $$F$$를 Frobenius manifold의 *potential*이라 부른다. 이로부터 만일 flat coordinate을 잡고, $$\eta^{\alpha\beta}$$를 $$\eta_{\alpha\beta}$$의 역행렬이라 하면 곱셈의 structure constant는

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_{\gamma, \delta} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\delta} \eta^{\delta\gamma} \partial_{t^\gamma}$$

로 주어진다. 그런데 이 곱셈 $$\circ$$는 associative이므로, 이를 structure constant로 직접 계산하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Witten-Dijkgraaf-Verlinde-Verlinde)**</ins> [명제 6](#prop6)의 potential $$F$$는 모든 $$\alpha, \beta, \gamma, \delta$$에 대해 다음의 방정식

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}$$

을 만족한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

곱셈 $$\circ$$의 associativity $$(\partial_{t^\alpha} \circ \partial_{t^\beta}) \circ \partial_{t^\gamma} = \partial_{t^\alpha} \circ (\partial_{t^\beta} \circ \partial_{t^\gamma})$$을 structure constant로 풀어 쓰자. $$C_{\alpha\beta}{}^\gamma := \sum_\delta c_{\alpha\beta\delta} \eta^{\delta\gamma}$$로 정의하면 곱셈은

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_\gamma C_{\alpha\beta}{}^\gamma \partial_{t^\gamma}\tag{1}$$

이고, associativity는

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta$$

로 표현된다. 여기에 [명제 6](#prop6)의 결과 $$c_{\alpha\beta\gamma} = \partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F$$를 대입하면

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}$$

를 얻는다. 역으로 이 PDE 시스템을 만족하는 $$F$$로부터 정의된 곱셈은 자동으로 associative하므로 WDVV equation은 Frobenius manifold의 associativity와 정확히 동치인 조건이 된다.

</details>

WDVV equation은 $$F$$의 삼계도함수들 사이의 quadratic relation이며, $$F$$ 자체에 대해서는 3차 비선형 편미분방정식 시스템이다. Mirror symmetry의 A-model 측에서 quantum cohomology의 Gromov-Witten potential은 이 equation을 만족하는 대표적 예시로, 이는 *splitting axiom* ([\[사교기하학\] §Gromov-Witten 불변량, ⁋명제 6](/ko/math/symplectic_geometry/gromov_witten#prop6))에 반영되어 있다. 

위의 증명에서 알 수 있듯 Frobenius manifold의 언어에서 WDVV equation은 본질적으로 $$\circ$$의 associativity이지만, A-model에서는 이와 같이 덜 자명한 splitting axiom의 형태를 띤다는 것에 주목하자. 반면 B-model에서 $$\circ$$의 associativity는, $$\Jac(W)$$이 ring의 quotient이므로, 자명하게 얻어지는 것이다. 반대로, A-model에서는 Gromov-Witten potential이 $$F$$의 역할을 하는 것이 투명하게 보이지만 B-model에서 이를 만들기 위해서는 꽤나 많은 작업이 필요하다. 이는 mirror symmetry의 철학을 다시 보여주는 예시로, 한쪽에서는 어려운 문제를 mirror를 통해 반대쪽 모델로 옮기면 상대적으로 쉬운 문제로 바뀐다는 것이다. 

## 예시

다음 예시는 가장 기본적인 Frobenius manifold이며, 이후의 더 복잡한 quantum cohomology 예시와 비교 기준이 된다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$M = \mathbb{C}^n$$ 위에 좌표 $$t^1, \ldots, t^n$$을 도입하고

$$\eta = \sum_{i=1}^n dt^i \otimes dt^i,\qquad \partial_{t^i} \circ \partial_{t^j} = \delta_{ij} \partial_{t^i}$$

으로 두자. 이는 그냥 Euclidean space 정의를 $$\mathbb{C}$$로 올리기만 한 것으로, $$\eta$$가 flat이고, $$t^i$$들이 flat coordinate을 이루고, $$e=\sum \partial_{t^i}$$가 곱셈에 대한 단위원이라는 등의 사실은 거의 자명하게 얻어진다. 

이제 이 manifold의 Euler vector field는 우리가 미적분학 시간에 Euler vector field라 부르는 바로 그 vector field $$\sum_i t^i\partial_{t^i}$$가 된다. 실제로, flat coordinate들에서 $$E(t^i)=t^i$$이므로 Lie derivative들을 구해보면

$$\Lie_E(dt^i)=d(E(t^i))=dt^i,\qquad \Lie_E(\partial_{t^i})=[E, \partial_{t^i}]=-\partial_{t^i}$$

가 되며, 이로부터

$$\Lie_E(\eta) = \sum_i \bigl( \Lie_E(dt^i) \otimes dt^i + dt^i \otimes \Lie_E(dt^i) \bigr) = 2 \sum_i dt^i \otimes dt^i = 2\eta$$

임을 안다. 비슷하게 곱셈의 경우, $$\circ=\sum dt^i\otimes dt^i\otimes\partial_{t^i}$$로 쓴 후 위와 비슷한 계산을 수행하면 $$\Lie_E(\circ)=\circ$$임을 확인할 수 있다. 

Potentiality는 거의 자명하게 얻을 수 있으며, $$i,j,k$$ 방향으로 순서대로 미분했을 때 $$\delta_{ijk}$$가 나오는 함수가 무엇일지 역산해보면 (당연히) 

$$F=\frac{1}{6}\sum_i (t^i)^3$$

으로 두면 되는 것을 확인할 수 있다. $$\circ$$가 associative이므로, WDVV equation은 자명하게 성립할 것이나, 굳이 계산해본다면 $$\eta^{ef} = \delta_{ef}$$을 사용하면 structure constant가 $$C_{\alpha\beta}{}^e = \delta_{\alpha\beta}\delta_{\beta e}$$가 되어

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \delta_{\alpha\beta}\delta_{\alpha\gamma}\delta_{\gamma\delta} = \delta_{\alpha\beta\gamma\delta} = \delta_{\alpha\gamma}\delta_{\alpha\beta}\delta_{\beta\delta} = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta$$

로 자명하게 성립하는 것을 다시 확인할 수 있다. 

</div>

이 예시에서 좌표들 $$t^i$$는 몹시 좋은데, 이들 좌표에서는 곱셈 $$\circ$$이 자연스레 대각화된다. 일반적으로 우리는 곱셈 $$\circ_p$$가 generic point에서 idempotent들의 direct sum으로 나타나는 경우 이를 *semisimple* Frobenius manifold라 부르는데, [예시 8](#ex8)은 그러한 것들 중 가장 단순한 예시라 할 수 있다.

이제 우리가 이 글에서 본래 다루고자 한 것, 곧 quantum cohomology를 Frobenius manifold로 이해하는 것으로 넘어가자. Compact Kähler manifold $$X$$에 대해 base를 cohomology vector space 자체

$$M = H^\ast(X, \mathbb{C})$$

로 잡고, cohomology basis $$\{\sigma^\alpha\}$$의 dual로 formal coordinate $$t = \sum_\alpha t^\alpha \sigma^\alpha$$를 도입하자. $$M$$이 그 자체로 벡터공간이므로 각 점에서의 tangent space $$T_tM$$은 $$H^\ast(X, \mathbb{C})$$와 canonically isomorphic하다. 따라서 여기에 Frobenius manifold 구조를 주는 것은 $$T_tM\cong H^\ast(X, \mathbb{C})$$ 위에 Frobenius product $$\circ_t$$를 주는 것과 같고, (당연히) 이를 big quantum cohomology의 곱셈 $$\circ_t$$, 즉 GW potential $$F(t)$$의 삼계도함수가 정의하는 곱셈으로 택할 것이다. ([\[사교기하학\] §양자 코호몰로지, ⁋정의 12](/ko/math/symplectic_geometry/quantum_cohomology#def12)) 다음 명제는 이 데이터가 실제로 Frobenius manifold를 이룬다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Compact Kähler manifold $$X$$에 대하여, $$M = H^\ast(X, \mathbb{C})$$ 위에 big quantum product $$\circ_t$$ ([\[사교기하학\] §양자 코호몰로지, ⁋정의 12](/ko/math/symplectic_geometry/quantum_cohomology#def12)), Poincaré pairing $$\eta$$, 항등원 $$e = 1 \in H^0(X)$$, 그리고 Euler vector field

$$E = \sum_\alpha \Bigl(1 - \frac{1}{2}\deg \sigma^\alpha\Bigr) t^\alpha \partial_{t^\alpha} + \sum_\alpha r^\alpha \partial_{t^\alpha}, \qquad c_1(X) = \sum_\alpha r^\alpha \sigma^\alpha$$

를 두면 $$(M, \eta, \circ_t, e, E)$$는 Frobenius manifold ([정의 5](#def5))이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정의 5](#def5)의 여섯 조건을 차례로 확인한다. 

1. 우선 Poincaré pairing $$\eta_{\alpha\beta} = \int_X \sigma_\alpha \smile \sigma_\beta$$는 linear coordinate $$t^\alpha$$에서 상수이므로 그 Levi-Civita connection이 flat이고 $$t^\alpha$$가 flat coordinate을 이룬다. 
2. 두 번째 조건의 경우, 곱셈 $$\circ_t$$는 [\[사교기하학\] §양자 코호몰로지, ⁋정리 6](/ko/math/symplectic_geometry/quantum_cohomology#thm6)에 의해 commutative associative이며 $$t$$에 대해 smooth이다.
3. 이 곱셈의 항등원은 $$1 \in H^0(X)$$이며, 이는 flat coordinate에서 constant section이므로 $$\nabla e = 0$$이다. 
4. 한편 [\[사교기하학\] §양자 코호몰로지, ⁋정의 12](/ko/math/symplectic_geometry/quantum_cohomology#def12)에 의해 structure constant는 $$c_{\alpha\beta\gamma}(t) = \eta(\partial_{t^\alpha} \circ_t \partial_{t^\beta}, \partial_{t^\gamma}) = \partial_{t^\alpha}\partial_{t^\beta}\partial_{t^\gamma} F$$이므로, 이것이 세 index에 대해 대칭이라는 사실로부터 $$\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$$를 얻는다.
5. 비슷하게 $$\nabla c$$가 네 index에 대해 대칭이라는 것을 확인할 수 있으며, 이 potentiality 아래에서 associativity는 [명제 7](#prop7)의 WDVV equation과 동치이며, A-model 측에서는 GW invariant의 splitting axiom으로 보장된다. 
6. 마지막으로 quantum cohomology의 grading ([\[사교기하학\] §양자 코호몰로지, ⁋정의 2](/ko/math/symplectic_geometry/quantum_cohomology#def2))이 위 본문에서 본 대로 $$\Lie_E(\circ) = \circ$$, $$\Lie_E(\eta) = (2-d)\eta$$로 번역되고, 주어진 $$E$$가 $$\nabla^2 E = 0$$인 affine vector field로서 이를 만족한다.

</details>

한편 우리의 mirror symmetry statement

$$\Jac(W_q)\cong QH^\ast(X)$$

을 생각하면, 결국 이는 quantum parameter $$q$$의 deformation에 의존하는 것이며, 따라서 이 수준에서만 고려한다면 big quantum cohomology는 다소 큰 것이며 우리는 $$H^2$$ 방향의 deformation, 혹은 small quantum cohomology만 생각하면 된다. 더 일반적인 수준에서도, big quantum cohomology와 $$W_q$$의 bulk deformation을 포함하여 mirror symmetry를 연구할 수는 있지만, 이는 우리의 일차적인 목표에서 벗어나므로 대부분의 경우 우리는 $$H^2$$ 방향의 deformation만 고려하기로 한다. 다음 $$\mathbb{P}^1$$ 예시에서는 unit 방향 $$H^0$$를 빼면 $$H^2$$가 cohomology의 전부라 ($$\deg \ge 4$$ 방향이 없어) big quantum cohomology가 곧 small과 일치하므로, 아래 계산이 [명제 9](#prop9)를 그대로 실현한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 위 곱셈 $$\circ_t$$가 $$t$$에 따라 변한다는 것을 명시적으로 확인하기 위해 $$X = \mathbb{P}^1$$인 경우를 계산하자. Manifold $$M = H^\ast(\mathbb{P}^1) = \mathbb{C}\langle 1, H\rangle$$는 그 자체가 vector space이므로, 그 위의 좌표는 cohomology basis $$\{1, H\}$$의 dual로 주어진다. 이를 각각 $$t^0, t^1$$이라 하자. 

이제 $$\mathbb{P}^1$$의 Gromov-Witten potential은

$$F(t^0, t^1) = \frac{1}{2}(t^0)^2 t^1 + e^{t^1}$$

로 주어진다. ([\[사교기하학\] §양자 코호몰로지, ⁋정의 12](/ko/math/symplectic_geometry/quantum_cohomology#def12)) 여기서 첫째 항은 classical cup product의 기여이고, 둘째 항은 [§거울대칭 개요, ⁋예시 5](/ko/math/mirror_symmetry/overview#ex5)에서의 degree-$$1$$ rational curve의 기여 $$\langle H, H, H\rangle_{0,3,1} = 1$$이 $$H^2$$ 방향 좌표 $$t^1$$에 대해 (Euler vector field를 타고) 지수함수로 누적된 것으로 생각할 수 있다. Metric은 이미 [예시 4](#ex4)에서 계산하였으며, 위의 식을 따라 $$F$$의 삼계도함수들을 계산하면

$$\partial_{t^0}^3 F = 0,\qquad \partial_{t^0}^2\partial_{t^1} F = 1,\qquad \partial_{t^0}\partial_{t^1}^2 F = 0,\qquad \partial_{t^1}^3 F = e^{t^1}$$

이다. 이제 $$\eta$$의 inverse matrix는 어차피 자기자신이므로, (1)를 사용해 계산하면 

$$\partial_{t^0} \circ_t \partial_{t^\alpha} = \partial_{t^\alpha}, \qquad \partial_{t^1} \circ_t \partial_{t^1} = e^{t^1}\, \partial_{t^0}$$

을 얻는다. 그럼 첫째 식은 $$\partial_{t^0}$$가 항등원 $$e$$ 역할을 한다는 것을 보여주며, 둘째 식의 우변이 $$t^1$$에 의존한다는 것이 곧 곱셈이 manifold 위에서 변형됨을 보여준다. 

Euler field는 위 일반식에 $$\deg 1 = 0$$, $$\deg H = 2$$, $$c_1(\mathbb{P}^1) = 2H$$를 대입하여

$$E = t^0 \partial_{t^0} + 2\partial_{t^1}$$

로 주어진다. $$E(t^0) = t^0$$, $$E(t^1) = 2$$이므로 각 성분의 Lie derivative는

$$\Lie_E(dt^0) = dt^0, \quad \Lie_E(dt^1) = 0, \quad \Lie_E(\partial_{t^0}) = [E, \partial_{t^0}] = -\partial_{t^0}, \quad \Lie_E(\partial_{t^1}) = [E, \partial_{t^1}] = 0$$

이며, 이를 metric $$\eta = dt^0 \otimes dt^1 + dt^1 \otimes dt^0$$에 적용하면 각 항이 weight $$1 + 0 = 1$$이므로

$$\Lie_E(\eta) = \Lie_E(dt^0)\otimes dt^1 + dt^1 \otimes \Lie_E(dt^0) = dt^0 \otimes dt^1 + dt^1 \otimes dt^0 = \eta$$

가 되어 $$2 - d = 1$$을 얻고, 이는 즉 $$\dim_\mathbb{C}\mathbb{P}^1$$의 값과 같다. 비슷한 계산으로, 곱셈 $$\circ$$의 비자명한 부분은 tensor $$e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0}$$ (즉 $$\partial_{t^1} \circ \partial_{t^1} = e^{t^1}\partial_{t^0}$$) 이며, $$\Lie_E(e^{t^1}) = E(e^{t^1}) = 2e^{t^1}$$ (weight $$2$$), $$dt^1$$ 둘이 weight $$0$$, $$\partial_{t^0}$$이 weight $$-1$$이므로

$$\Lie_E\bigl(e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0}\bigr) = (2 + 0 + 0 - 1)\, e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0} = e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0}$$

가 되어 $$\Lie_E(\circ) = \circ$$이다.

이제 Novikov variable을 $$q = e^{t^1}$$로 두면, 둘째 식은 $$\partial_{t^1} \circ \partial_{t^1} = qe$$가 되며, 이는 다시 cohomology 언어로 옮겨오면 $$H \star H = q \cdot 1$$이므로 [§거울대칭 개요, ⁋예시 5](/ko/math/mirror_symmetry/overview#ex5)에서의 small quantum ring을 복원한다. 뿐만 아니라, 이제 이 isomorphism은 $$q=e^{t^1}$$의 변화에 따라 parametrize되어 기존의 ring isomorphism 수준에서의 mirror symmetry를 더 업그레이드한 것이다.

</div>

이렇듯 Frobenius manifold는 quantum cohomology의 ring structure를 *deformation parameter $$t$$의 함수*로서 일관성 있게 다룰 수 있는 무대를 제공한다. 다음 글부터 우리는 이제 본격적인 mirror symmetry를 탐구할 수 있다. 

---

**참고문헌**

**[Dub]** B. Dubrovin, *Geometry of $$2$$D topological field theories*, Integrable systems and quantum groups (Montecatini Terme, 1993), Lecture Notes in Math. **1620**, Springer, 1996, 120--348.

**[Her]** C. Hertling, *Frobenius Manifolds and Moduli Spaces for Singularities*, Cambridge Tracts in Mathematics **151**, Cambridge University Press, 2002.

**[Man]** Yu. I. Manin, *Frobenius Manifolds, Quantum Cohomology, and Moduli Spaces*, American Mathematical Society Colloquium Publications **47**, AMS, 1999.

**[HM]** C. Hertling, Yu. Manin, *Weak Frobenius manifolds*, Internat. Math. Res. Notices **1999**, no. 6, 277--286.
