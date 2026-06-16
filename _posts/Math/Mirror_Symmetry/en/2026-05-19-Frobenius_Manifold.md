---
title: "Frobenius Manifolds"
description: "Starting from the definition of a Frobenius algebra, this post explores the notion of Frobenius manifolds, which carry a Frobenius algebra structure at each point, examines the WDVV equations, and discusses connections to mirror symmetry, quantum cohomology, and Jacobi rings."
excerpt: "Frobenius manifolds and the WDVV equation"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/frobenius_manifold
sidebar:
    nav: "mirror_symmetry-en"

date: 2026-05-19
weight: 3
translated_at: 2026-06-01T12:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T12:30:04+00:00
---
In [§Overview of Mirror Symmetry](/en/math/mirror_symmetry/overview) we saw that the mirror symmetry of a toric Fano variety $$X_\Sigma$$ is summarized by an isomorphism

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

between the Jacobi ring and quantum cohomology. However, as we also observed in that post, quantum cohomology carries more structure than this ring isomorphism captures, because the product itself deforms as the Novikov parameter $$q$$ varies. The structure encoding this deformation is Frobenius; in this post we first review the definition of a finite-dimensional Frobenius algebra, then examine Dubrovin's notion of a Frobenius manifold and the WDVV equation in turn.

## Frobenius Algebras

Intuitively, a Frobenius manifold is a manifold whose tangent space at each point carries a Frobenius algebra structure.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$A$$ be a finite-dimensional commutative, associative $$\mathbb{C}$$-algebra equipped with a non-degenerate symmetric bilinear form $$\eta: A \otimes A \to \mathbb{C}$$. If for all elements $$x,y,z\in A$$ the identity

$$\eta(x \cdot y,z) = \eta(x,y \cdot z)$$

holds, then the pair $$(A, \eta)$$ is called a *Frobenius algebra*.

</div>

This condition means that the multiplication $$\cdot : A \otimes A \to A$$ and the bilinear form $$\eta$$ are compatible, defining a trilinear form $$c(x,y,z) := \eta(x \cdot y,z)$$ that is symmetric in all three arguments. Indeed, commutativity gives

$$c(x,y,z) = \eta(x \cdot y,z) = \eta(y \cdot x,z) = c(y,x,z)$$

and the Frobenius condition yields

$$c(x,y,z) = \eta(x,y \cdot z) = \eta(y \cdot z, x) = c(y,z,x).$$

Hence $$c$$ is completely symmetric in its three variables, and this trilinear form encodes all the information of the Frobenius structure.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The cohomology ring $$H^\ast(X, \mathbb{C})$$ of a compact Kähler manifold $$X$$, with the cup product and the Poincaré pairing

$$\eta(\alpha, \beta) = \int_X \alpha \smile \beta,$$

is a Frobenius algebra. This means that the identity

$$\eta(\alpha \smile \beta, \gamma) = \eta(\alpha, \beta \smile \gamma)$$

holds for all $$\alpha,\beta,\gamma$$, which follows from the associativity of the cup product.

</div>

Meanwhile, in the examples of [§Overview of Mirror Symmetry](/en/math/mirror_symmetry/overview) we introduced the Landau–Ginzburg model, which consists of a holomorphic function $$W$$ on a given manifold $$\check{X}$$; the Jacobi ring containing the critical points of $$W$$ carried the information of the B-model. Locally this is written as follows.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A holomorphic function $$f : \mathbb{C}^n \to \mathbb{C}$$ is said to have an *isolated hypersurface singularity* at the origin if the following two conditions hold.

1. $$f(0) = 0$$, $$df(0) = 0$$.
2. The origin is *isolated* among the critical points of $$f$$, i.e., in some neighborhood of the origin the only solution to $$df = 0$$ is the origin itself.

</div>

A standard example is $$f(\x) = \x^{k+1}$$ ($$k \geq 1$$), which we call an $$A_k$$-type singularity.

Now suppose every critical point of a polynomial $$f:\mathbb{C}^n \rightarrow \mathbb{C}$$ is an isolated hypersurface singularity. Then we may consider its *Jacobi ring*

$$\Jac(f) = \mathbb{C}[\x_1, \ldots, \x_n]/(\partial_1 f, \ldots, \partial_n f).$$

Its dimension $$\mu(f)=\dim \Jac(f)$$ counts the singularities of $$f$$ with multiplicity; intuitively, one may think of it as obtaining $$\mu(f)$$ simple critical points after a small perturbation. In singularity theory this $$\mu(f)$$ is called the *Milnor number* of $$f$$.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For a polynomial $$f : \mathbb{C}^n \to \mathbb{C}$$ all of whose critical points are isolated hypersurface singularities, the *residue pairing* $$\eta$$ on the Jacobi ring $$\Jac(f)$$ is defined by the formula

$$\eta(g, h) := \frac{1}{(2\pi i)^n} \oint_{\Gamma_\epsilon} \frac{g(\x) h(\x) \, d\x_1 \wedge \cdots \wedge d\x_n}{\partial_1 f \cdots \partial_n f}.$$

Here the integration path $$\Gamma_\epsilon$$ is a small contour surrounding all points of $$\Crit(f)=\{df=0\}$$; this integral can be thought of as the contribution at that point when the critical point is regarded as a fat point containing multiplicity information.

In other words, intuitively this can be viewed as localizing the global integral $$\int_X$$ of [Example 2](#ex2) to integrals over the (finitely many) points of the critical scheme, and one can show that $$(\Jac(f), \eta)$$ is indeed a Frobenius algebra in a manner similar to that example.

In general, if all critical points of $$f$$ are *non-degenerate*, i.e., the Hessian $$\Hess_p(f) = (\partial_i \partial_j f(p))_{ij}$$ is invertible at each $$p \in \Crit(f)$$, then the above integral simplifies to

$$\eta(g, h) = \sum_{p \in \Crit(f)} \frac{g(p)\, h(p)}{\det \Hess_p(f)};$$

more fundamentally, $$\Jac(f)$$ itself decomposes as

$$\Jac(f)=\bigoplus_{p\in \Crit(f)}\mathbb{C},$$

and with respect to this basis the residue pairing is diagonalized as $$\operatorname{diag}(1/\det \Hess_p(f))$$ in the critical-point basis.

As a special example, consider the Hori–Vafa superpotential of $$\mathbb{P}^1$$ seen in [§Overview of Mirror Symmetry, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5):

$$W_q = \x + \frac{q}{\x}.$$

Its critical points are the two points $$\x_\pm = \pm\sqrt{q}$$.

One must be careful that the ambient space $$\check{X}$$ is not affine space but an algebraic torus, so the differential form defined on it is not simply $$d\x$$. Indeed, the differential form on it is given by $$d\x/\x$$ according to [[Toric Geometry] §Logarithmic Differential Forms on Toric Varieties, ⁋Definition 1](/en/math/toric_geometry/logarithmic_differentials#def1), which corresponds to the coordinate $$\u=\log\x$$ on the torus. Then $$d\u=d\x/\x$$ and $$\partial_\u=\x\partial_\x$$; computing the derivatives of $$W_q$$ in this coordinate in order to find the Hessian yields

$$\partial_\u W_q = \x \partial_\x W_q = \x - q/\x, \qquad \partial_\u^2 W_q = \partial_\u(\x - q/\x) = \x + q/\x,$$

and at the critical points $$\x_\pm = \pm\sqrt{q}$$ we obtain

$$\Hess_{\x_\pm}(W_q)=\partial_\u^2 W_q \big\vert_{\x_\pm} = \x_\pm + q/\x_\pm = 2\x_\pm = \pm 2\sqrt{q}.$$

Applying the above formula to the two critical points gives the residue pairing

$$\eta(g, h) = \frac{g(\sqrt{q})\,h(\sqrt{q})}{2\sqrt{q}} + \frac{g(-\sqrt{q})\,h(-\sqrt{q})}{-2\sqrt{q}}.$$

Computing this directly on the basis $$\{1, \x\}$$ of $$\Jac(W_q) = \mathbb{C}[\x^{\pm 1}, q^{\pm 1}]/(\x^2 - q)$$ yields

$$\eta(1, 1) = \frac{1}{2\sqrt{q}} + \frac{1}{-2\sqrt{q}} = 0, \qquad \eta(1, \x) = \frac{\sqrt{q}}{2\sqrt{q}} + \frac{-\sqrt{q}}{-2\sqrt{q}} = 1, \qquad \eta(\x, \x) = \frac{q}{2\sqrt{q}} + \frac{q}{-2\sqrt{q}} = 0,$$

so the matrix representation of $$\eta$$ in this basis is $$\begin{pmatrix}0&1\\1&0\end{pmatrix}$$. This exactly coincides with the classical Poincaré pairing of $$\mathbb{P}^1$$, showing that the ring isomorphism $$\Jac(W_q) \cong QH^\ast(\mathbb{P}^1)$$ was in fact a Frobenius algebra isomorphism.

In the same way, consider the Hori–Vafa superpotential of $$\mathbb{P}^2$$ seen in [§Overview of Mirror Symmetry, ⁋Example 6](/en/math/mirror_symmetry/overview#ex6):

$$W_q = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}.$$

In the log coordinates $$\u_i = \log \z_i$$ the derivatives of $$W_q$$ are

$$\partial_{\u_1} W_q = \z_1 - q/(\z_1 \z_2), \qquad \partial_{\u_2} W_q = \z_2 - q/(\z_1 \z_2),$$

and setting both to $$0$$ gives $$\z_1 = \z_2 = \z$$ with $$\z^3 = q$$, so the critical points are the three points

$$\z_k = \omega^k q^{1/3},\qquad k = 0, 1, 2,$$

and $$\Jac(W_q) \cong \mathbb{C}[\z, q^{\pm 1}]/(\z^3 - q)$$ has basis $$\{1, \z, \z^2\}$$. Collecting the second derivatives of $$W_q$$ in log coordinates to compute the Hessian gives

$$\Hess(W_q) = \begin{pmatrix} \z_1 + \frac{q}{\z_1 \z_2} & \frac{q}{\z_1 \z_2} \\ \frac{q}{\z_1 \z_2} & \z_2 + \frac{q}{\z_1 \z_2} \end{pmatrix},$$

and at a critical point we have $$q/(\z_1 \z_2) = \z^3/\z^2 = \z$$, so

$$\Hess_{\z_k}(W_q) = \begin{pmatrix} 2\z_k & \z_k \\ \z_k & 2\z_k \end{pmatrix}, \qquad \det \Hess_{\z_k}(W_q) = 3\z_k^2.$$

Applying this formula to the three critical points gives the residue pairing

$$\eta(\z^a, \z^b) = \sum_{k=0}^{2} \frac{(\omega^k q^{1/3})^{a+b}}{3 (\omega^k q^{1/3})^2} = \frac{q^{(a+b-2)/3}}{3} \sum_{k=0}^{2} \omega^{k(a+b-2)},$$

and

$$\sum_{k=0}^{2} \omega^{km} = 3\iff m \equiv 0 \pmod 3,$$

while in all other cases this sum is $$0$$. Thus for $$0 \leq a, b \leq 2$$ we have $$\eta(\z^a, \z^b) = 1$$ only when $$a + b = 2$$, and $$0$$ otherwise. Hence the matrix representation of $$\eta$$ in this basis is again the matrix

$$\begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix},$$

which coincides with the classical Poincaré pairing of $$\mathbb{P}^2$$.

</div>

## Frobenius Manifolds

In the previous section we defined Frobenius algebras and verified that they upgrade the mirror symmetry ring isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$ to the level of Frobenius algebras. However, the mirror symmetry isomorphism

$$\Jac(W_q)\cong QH^\ast(X)$$

has still not been stated in its full strength: the power of mirror symmetry lies in the fact that this isomorphism possesses a certain naturality. That is, it defines a family of isomorphisms that deform smoothly as $$q$$ varies, and to realize this we must first consider the situation in which a Frobenius algebra is parametrized by a specific variable ($$q$$).

To this end we define the notion of a Frobenius manifold. A Frobenius manifold is, of course, a manifold whose tangent space at each point is a Frobenius algebra, but that is not the whole story; this structure must also vary smoothly over the base manifold.

First, for the tangent bundle $$TM$$ over a Frobenius manifold $$M$$, since each fiber of $$TM$$ must be a Frobenius algebra, at each point $$p\in M$$ the space $$T_pM$$ needs a multiplication $$\circ$$ as an algebra, a unit element $$e$$ for this multiplication, and the Frobenius algebra pairing $$\eta$$. For these to constitute a smooth structure, $$\circ$$ must vary smoothly with $$p$$, i.e., $$\circ_p:T_pM\otimes T_pM\rightarrow T_pM$$, and $$\eta$$ must be a smooth non-degenerate bilinear form. Moreover, the unit must be a (smooth) section of $$TM$$, i.e., a vector field.

In differential geometry it is a connection that allows us to compare different tangent spaces. ([[Riemannian Geometry] §Connections, ⁋Definition 1](/en/math/riemannian_geometry/connection#def1)) Since every pseudo-Riemannian manifold $$M$$ always admits a compatible Levi-Civita connection $$\nabla$$ ([[Riemannian Geometry] §Levi-Civita Connection, ⁋Theorem 4](/en/math/riemannian_geometry/Levi-Civita_connection#thm4)), it suffices to use this.

Moreover, given any connection $$\nabla$$, there exists *parallel transport* along a curve $$\gamma$$ on $$M$$ joining the starting point $$x_0$$ to the endpoint $$x_1$$. ([[Riemannian Geometry] §Levi-Civita Connection, ⁋Definition 7](/en/math/riemannian_geometry/Levi-Civita_connection#def7)) To deform a Frobenius algebra as we vary the point of the manifold, we must use this parallel transport; if the deformation depended on the curve used to move from one point to another, this would be unsatisfactory. ([[Riemannian Geometry] §Riemann Curvature, ⁋Example 1](/en/math/riemannian_geometry/curvature#ex1)) Hence we require this $$\nabla$$ to be *flat*. ([[Riemannian Geometry] §Riemann Curvature, ⁋Definition 6](/en/math/riemannian_geometry/curvature#def6))

Finally, since $$QH^\ast(X)$$ already carries a grading, additional data are needed to reflect this. Recall that the grading on $$QH^\ast(X)$$ was obtained by adding to the classical cohomology grading $$H^\ast(X)$$ the grading coming from the Novikov ring. That is, writing $$QH^\ast(X) = H^\ast(X) \otimes_\mathbb{C} \Lambda$$, the degree of any generator $$T_\alpha \otimes q^\beta$$ was given by $$\deg(T_\alpha \otimes q^\beta) = p_\alpha + 2\, c_1 \cdot \beta$$. ([[Symplectic Geometry] §Quantum Cohomology, ⁋Definition 2](/en/math/symplectic_geometry/quantum_cohomology#def2))

The data of this grading are encoded by a *vector field* on the manifold $$M$$ called the *Euler vector field* $$E$$. The *infinitesimal deformation* of the multiplication $$\circ$$ along the flow of $$E$$ is given by the Lie derivative $$\Lie_E(\circ)$$; the fact that the quantum product respects degrees, which we examined in [[Symplectic Geometry] §Quantum Cohomology](/en/math/symplectic_geometry/quantum_cohomology), is expressed by the equation

$$\Lie_E(\circ) = \circ.$$

Similarly, in our intuition $$\eta$$ is the Poincaré pairing ([Example 2](#ex2)), which survives only in the top degree, so this degree condition translates to

$$\Lie_E(\eta) = (2 - d)\eta.$$

The Euler vector field is then an *affine* vector field satisfying $$\nabla^2 E=0$$; precisely, these two conditions completely determine $$E$$.

We now have all the ingredients needed to define a Frobenius manifold.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A tuple $$(M, \eta, \circ, e, E)$$ is called a *Frobenius manifold* if the following conditions all hold.

1. The Levi-Civita connection induced by the symmetric non-degenerate bilinear form $$\eta$$ on $$TM$$ is flat.
2. At each $$p\in M$$ there exists a commutative associative product $$\circ_p: T_p M \otimes T_p M \to T_p M$$ that is smooth in $$p$$.
3. There exists a vector field $$e$$ that is the identity element for the multiplication $$\circ$$ at every point, and $$\nabla e = 0$$.
4. There exists a vector field $$E$$ satisfying the affine condition $$\nabla^2 E=0$$ such that for a suitable constant $$d\in \mathbb{C}$$,
    
    $$\Lie_E(\circ)=\circ,\qquad \Lie_E(\eta)=(2-d)\eta$$

    holds.
5. For all vector fields $$X,Y,Z$$ we have $$\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$$.
6. (Potentiality) The $$4$$-tensor $$\nabla c$$ defined by the trilinear form $$c(X,Y,Z):=\eta(X\circ Y, Z)$$ is symmetric in all four variables.

</div>

## The WDVV Equation

The last condition in [Definition 5](#def5) is called potentiality because it allows the trilinear form $$c$$ to be expressed as the third partial derivatives of a suitable scalar function $$F:M \rightarrow \mathbb{C}$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a Frobenius manifold $$(M, \eta, \circ, e, E)$$ with flat coordinates $$t^1, \ldots, t^n$$, there exists a holomorphic function $$F: M \to \mathbb{C}$$ (defined locally) such that

$$c_{\alpha\beta\gamma}(t) := \eta(\partial_{t^\alpha} \circ \partial_{t^\beta}, \partial_{t^\gamma}) = \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\gamma}$$

holds for all $$\alpha, \beta, \gamma$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For flat coordinates $$t^\alpha$$ the covariant derivative $$\nabla_{\partial_{t^\delta}}$$ coincides with the ordinary partial derivative $$\partial_{t^\delta}$$, so the potentiality condition in [Definition 5](#def5) means that

$$\partial_{t^\delta} c_{\alpha\beta\gamma} = \partial_{t^\alpha} c_{\delta\beta\gamma}$$

holds symmetrically in the four indices. Since $$c$$ itself is symmetric in three indices, putting these together shows that the 1-form $$\omega_{\beta\gamma} := \sum_\alpha c_{\alpha\beta\gamma} dt^\alpha$$ is closed. By the Poincaré lemma there locally exist functions $$G_{\beta\gamma}$$ with $$\partial_{t^\alpha} G_{\beta\gamma} = c_{\alpha\beta\gamma}$$; the symmetry of $$c$$ implies $$G_{\beta\gamma} = G_{\gamma\beta}$$, and moreover $$\partial_{t^\alpha} G_{\beta\gamma} = \partial_{t^\beta} G_{\alpha\gamma}$$ holds. Applying the Poincaré lemma once more, there exist functions $$H_\gamma$$ with $$\partial_{t^\beta} H_\gamma = G_{\beta\gamma}$$, and from the symmetry $$\partial_{t^\delta} H_\gamma = \partial_{t^\gamma} H_\delta$$ we finally obtain a scalar function $$F$$ such that $$\partial_{t^\gamma} F = H_\gamma$$. Altogether we obtain $$\partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F = c_{\alpha\beta\gamma}$$.

</details>

Such a function $$F$$ is called the *potential* of the Frobenius manifold. Hence, choosing flat coordinates and letting $$\eta^{\alpha\beta}$$ be the inverse matrix of $$\eta_{\alpha\beta}$$, the structure constants of the multiplication are given by

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_{\gamma, \delta} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\delta} \eta^{\delta\gamma} \partial_{t^\gamma}.$$

Since this multiplication $$\circ$$ is associative, writing this out in structure constants yields the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Witten–Dijkgraaf–Verlinde–Verlinde)**</ins> The potential $$F$$ of [Proposition 6](#prop6) satisfies the following equation for all $$\alpha, \beta, \gamma, \delta$$:

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let us expand the associativity $$(\partial_{t^\alpha} \circ \partial_{t^\beta}) \circ \partial_{t^\gamma} = \partial_{t^\alpha} \circ (\partial_{t^\beta} \circ \partial_{t^\gamma})$$ of the multiplication $$\circ$$ in structure constants. Defining $$C_{\alpha\beta}{}^\gamma := \sum_\delta c_{\alpha\beta\delta} \eta^{\delta\gamma}$$, the multiplication is

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_\gamma C_{\alpha\beta}{}^\gamma \partial_{t^\gamma}\tag{1}$$

and associativity is expressed as

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta.$$

Substituting the result $$c_{\alpha\beta\gamma} = \partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F$$ of [Proposition 6](#prop6) gives

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}.$$

Conversely, the multiplication defined from a function $$F$$ satisfying this system of PDEs is automatically associative, so the WDVV equation is exactly equivalent to the associativity of the Frobenius manifold.

</details>

The WDVV equation is a quadratic relation among the third derivatives of $$F$$, and for $$F$$ itself it is a system of third-order nonlinear partial differential equations. On the A-model side of mirror symmetry, the Gromov–Witten potential of quantum cohomology is a representative example satisfying this equation, which is reflected in the *splitting axiom* ([[Symplectic Geometry] §Gromov–Witten Invariants, ⁋Proposition 6](/en/math/symplectic_geometry/gromov_witten#prop6)). As the proof above shows, in the language of Frobenius manifolds the WDVV equation is essentially the associativity of $$\circ$$; note, however, that on the A-model side it takes the less obvious form of the splitting axiom. On the other hand, in the B-model the associativity of $$\circ$$ is immediate because $$\Jac(W)$$ is a quotient ring. Conversely, in the A-model it is transparent that the Gromov–Witten potential plays the role of $$F$$, whereas in the B-model constructing it requires considerable work. This is again an illustration of the philosophy of mirror symmetry: a difficult problem on one side becomes relatively easy when transferred to the opposite model via the mirror.

## Examples

The following example is the most basic Frobenius manifold, and serves as a benchmark for the more complicated quantum cohomology examples that follow.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Introduce coordinates $$t^1, \ldots, t^n$$ on $$M = \mathbb{C}^n$$ and set

$$\eta = \sum_{i=1}^n dt^i \otimes dt^i,\qquad \partial_{t^i} \circ \partial_{t^j} = \delta_{ij} \partial_{t^i}.$$

This is simply the definition of Euclidean space lifted to $$\mathbb{C}$$; the facts that $$\eta$$ is flat, the $$t^i$$ form flat coordinates, and $$e=\sum \partial_{t^i}$$ is the unit for the multiplication are almost obvious.

The Euler vector field of this manifold is exactly the vector field $$\sum_i t^i\partial_{t^i}$$ that we call the Euler vector field in calculus. Indeed, since $$E(t^i)=t^i$$ in flat coordinates, computing the Lie derivatives gives

$$\Lie_E(dt^i)=d(E(t^i))=dt^i,\qquad \Lie_E(\partial_{t^i})=[E, \partial_{t^i}]=-\partial_{t^i},$$

whence

$$\Lie_E(\eta) = \sum_i \bigl( \Lie_E(dt^i) \otimes dt^i + dt^i \otimes \Lie_E(dt^i) \bigr) = 2 \sum_i dt^i \otimes dt^i = 2\eta.$$

Similarly, for the multiplication, writing $$\circ=\sum dt^i\otimes dt^i\otimes\partial_{t^i}$$ and performing a similar computation shows that $$\Lie_E(\circ)=\circ$$.

Potentiality is obtained almost trivially; working backwards to find a function whose third partial derivatives in the $$i,j,k$$ directions give $$\delta_{ijk}$$ yields (of course)

$$F=\frac{1}{6}\sum_i (t^i)^3.$$

Since $$\circ$$ is associative, the WDVV equation holds trivially; if one insists on computing it, using $$\eta^{ef} = \delta_{ef}$$ gives structure constants $$C_{\alpha\beta}{}^e = \delta_{\alpha\beta}\delta_{\beta e}$$, and one can verify directly that

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \delta_{\alpha\beta}\delta_{\alpha\gamma}\delta_{\gamma\delta} = \delta_{\alpha\beta\gamma\delta} = \delta_{\alpha\gamma}\delta_{\alpha\beta}\delta_{\beta\delta} = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta$$

holds trivially.

</div>

In this example the coordinates $$t^i$$ are very nice: in these coordinates the multiplication $$\circ$$ is naturally diagonalized. In general, if the multiplication $$\circ_p$$ is represented as a direct sum of idempotents at a generic point, we call this a *semisimple* Frobenius manifold; [Example 8](#ex8) is the simplest such example.

Let us now turn to what we originally intended to discuss in this post: understanding quantum cohomology as a Frobenius manifold. For a compact Kähler manifold $$X$$ we take the base to be the cohomology vector space itself,

$$M = H^\ast(X, \mathbb{C}),$$

and introduce formal coordinates $$t = \sum_\alpha t^\alpha \sigma^\alpha$$ dual to a cohomology basis $$\{\sigma^\alpha\}$$. Since $$M$$ is itself a vector space, the tangent space $$T_tM$$ at each point is canonically isomorphic to $$H^\ast(X, \mathbb{C})$$. Therefore endowing this with a Frobenius manifold structure is the same as giving a Frobenius product $$\circ_t$$ on $$T_tM\cong H^\ast(X, \mathbb{C})$$, and (naturally) we choose this to be the multiplication $$\circ_t$$ of big quantum cohomology, i.e., the multiplication defined by the third derivatives of the GW potential $$F(t)$$. ([[Symplectic Geometry] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12)) The next proposition shows that these data actually form a Frobenius manifold.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> For a compact Kähler manifold $$X$$, the tuple $$(M, \eta, \circ_t, e, E)$$ with $$M = H^\ast(X, \mathbb{C})$$, the big quantum product $$\circ_t$$ ([[Symplectic Geometry] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12)), the Poincaré pairing $$\eta$$, the unit $$e = 1 \in H^0(X)$$, and the Euler vector field

$$E = \sum_\alpha \Bigl(1 - \frac{1}{2}\deg \sigma^\alpha\Bigr) t^\alpha \partial_{t^\alpha} + \sum_\alpha r^\alpha \partial_{t^\alpha}, \qquad c_1(X) = \sum_\alpha r^\alpha \sigma^\alpha$$

is a Frobenius manifold ([Definition 5](#def5)).

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We verify the six conditions of [Definition 5](#def5) in order.

1. First, the Poincaré pairing $$\eta_{\alpha\beta} = \int_X \sigma_\alpha \smile \sigma_\beta$$ is constant in the linear coordinates $$t^\alpha$$, so its Levi-Civita connection is flat and the $$t^\alpha$$ form flat coordinates.
2. For the second condition, the multiplication $$\circ_t$$ is commutative and associative by [[Symplectic Geometry] §Quantum Cohomology, ⁋Theorem 6](/en/math/symplectic_geometry/quantum_cohomology#thm6), and smooth in $$t$$.
3. The unit for this multiplication is $$1 \in H^0(X)$$, which is a constant section in flat coordinates, so $$\nabla e = 0$$.
4. Meanwhile, by [[Symplectic Geometry] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12) the structure constants are $$c_{\alpha\beta\gamma}(t) = \eta(\partial_{t^\alpha} \circ_t \partial_{t^\beta}, \partial_{t^\gamma}) = \partial_{t^\alpha}\partial_{t^\beta}\partial_{t^\gamma} F$$, and the symmetry of this expression in the three indices gives $$\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$$.
5. Similarly one checks that $$\nabla c$$ is symmetric in the four indices; under this potentiality, associativity is equivalent to the WDVV equation of [Proposition 7](#prop7), and on the A-model side it is guaranteed by the splitting axiom for GW invariants.
6. Finally, the grading of quantum cohomology ([[Symplectic Geometry] §Quantum Cohomology, ⁋Definition 2](/en/math/symplectic_geometry/quantum_cohomology#def2)) translates as described in the main text into $$\Lie_E(\circ) = \circ$$ and $$\Lie_E(\eta) = (2-d)\eta$$, and the given $$E$$ satisfies this as an affine vector field with $$\nabla^2 E = 0$$.

</details>

Considering our mirror symmetry statement

$$\Jac(W_q)\cong QH^\ast(X),$$

this ultimately depends on the deformation by the quantum parameter $$q$$, so if we only care about this level big quantum cohomology is somewhat too large, and we need only consider the deformation in the $$H^2$$ direction, or small quantum cohomology. At a more general level one can study mirror symmetry including bulk deformations of big quantum cohomology and of $$W_q$$, but this goes beyond our primary goal, so in most cases we shall consider only the deformation in the $$H^2$$ direction. In the following $$\mathbb{P}^1$$ example, apart from the unit direction $$H^0$$ the space $$H^2$$ is the whole cohomology (there are no classes of degree $$\ge 4$$), so big quantum cohomology coincides with small quantum cohomology; hence the computation below realizes [Proposition 9](#prop9) directly.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> To verify explicitly that the above multiplication $$\circ_t$$ varies with $$t$$, let us compute the case $$X = \mathbb{P}^1$$. Since the manifold $$M = H^\ast(\mathbb{P}^1) = \mathbb{C}\langle 1, H\rangle$$ is itself a vector space, coordinates on it are given by the dual of the cohomology basis $$\{1, H\}$$; let us denote these by $$t^0, t^1$$.

The Gromov–Witten potential of $$\mathbb{P}^1$$ is now given by

$$F(t^0, t^1) = \frac{1}{2}(t^0)^2 t^1 + e^{t^1}.$$ ([[Symplectic Geometry] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12))

Here the first term is the contribution from the classical cup product, and the second term can be thought of as the contribution $$\langle H, H, H\rangle_{0,3,1} = 1$$ from the degree-$$1$$ rational curve of [§Overview of Mirror Symmetry, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5), accumulated exponentially along the $$H^2$$ direction coordinate $$t^1$$ (via the Euler vector field). The metric was already computed in [Example 4](#ex4), and computing the third partial derivatives of $$F$$ from the above formula gives

$$\partial_{t^0}^3 F = 0,\qquad \partial_{t^0}^2\partial_{t^1} F = 1,\qquad \partial_{t^0}\partial_{t^1}^2 F = 0,\qquad \partial_{t^1}^3 F = e^{t^1}.$$

Since the inverse matrix of $$\eta$$ is itself, using (1) we obtain

$$\partial_{t^0} \circ_t \partial_{t^\alpha} = \partial_{t^\alpha}, \qquad \partial_{t^1} \circ_t \partial_{t^1} = e^{t^1}\, \partial_{t^0}.$$

The first equation shows that $$\partial_{t^0}$$ plays the role of the unit $$e$$, and the fact that the right-hand side of the second equation depends on $$t^1$$ shows that the multiplication deforms over the manifold.

The Euler field is obtained by substituting $$\deg 1 = 0$$, $$\deg H = 2$$, and $$c_1(\mathbb{P}^1) = 2H$$ into the general formula above, giving

$$E = t^0 \partial_{t^0} + 2\partial_{t^1}.$$

Since $$E(t^0) = t^0$$ and $$E(t^1) = 2$$, the Lie derivatives of the components are

$$\Lie_E(dt^0) = dt^0, \quad \Lie_E(dt^1) = 0, \quad \Lie_E(\partial_{t^0}) = [E, \partial_{t^0}] = -\partial_{t^0}, \quad \Lie_E(\partial_{t^1}) = [E, \partial_{t^1}] = 0;$$

applying this to the metric $$\eta = dt^0 \otimes dt^1 + dt^1 \otimes dt^0$$, each term has weight $$1 + 0 = 1$$, so

$$\Lie_E(\eta) = \Lie_E(dt^0)\otimes dt^1 + dt^1 \otimes \Lie_E(dt^0) = dt^0 \otimes dt^1 + dt^1 \otimes dt^0 = \eta,$$

yielding $$2 - d = 1$$, which equals $$\dim_\mathbb{C}\mathbb{P}^1$$.

By a similar computation, the nontrivial part of the multiplication $$\circ$$ is the tensor $$e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0}$$ (i.e., $$\partial_{t^1} \circ \partial_{t^1} = e^{t^1}\partial_{t^0}$$). Since $$\Lie_E(e^{t^1}) = E(e^{t^1}) = 2e^{t^1}$$ (weight $$2$$), the two $$dt^1$$ factors have weight $$0$$, and $$\partial_{t^0}$$ has weight $$-1$$, we obtain

$$\Lie_E\bigl(e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0}\bigr) = (2 + 0 + 0 - 1)\, e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0} = e^{t^1}\, dt^1 \otimes dt^1 \otimes \partial_{t^0},$$

so $$\Lie_E(\circ) = \circ$$.

Now setting the Novikov variable to $$q = e^{t^1}$$, the second equation becomes $$\partial_{t^1} \circ \partial_{t^1} = qe$$, which translates back into cohomology language as $$H \star H = q \cdot 1$$, recovering the small quantum ring of [§Overview of Mirror Symmetry, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5). Moreover, this isomorphism is now parametrized by the variation of $$q=e^{t^1}$$, upgrading the previous mirror symmetry at the level of ring isomorphisms.

</div>

Thus a Frobenius manifold provides the stage on which the ring structure of quantum cohomology can be treated consistently as a *function of the deformation parameter $$t$$*. From the next post onward we can now explore mirror symmetry in earnest.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.

**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
