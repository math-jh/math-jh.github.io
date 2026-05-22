---
title: "Frobenius Manifolds"
excerpt: "Frobenius manifolds and the WDVV equation"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/frobenius_manifold
sidebar:
    nav: "mirror_symmetry-en"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/frobenius_manifold.png
    overlay_filter: 0.5

date: 2026-05-19
last_modified_at: 2026-05-19
weight: 3
translated_at: 2026-05-21T23:00:01+00:00
translation_source: kimi-cli
---
In [§Overview of Mirror Symmetry](/en/math/mirror_symmetry/overview) we saw that the mirror symmetry of a toric Fano variety $$X_\Sigma$$ is summarized by an isomorphism

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

between the Jacobi ring and quantum cohomology. However, as we also saw in that post, quantum cohomology possesses structure beyond what this ring isomorphism captures, because the product itself deforms as the Novikov parameter $$q$$ varies. The structure that encodes this deformation is Frobenius; in this post we first review the definition of a finite-dimensional Frobenius algebra and then examine Dubrovin's notion of a Frobenius manifold and the WDVV equation in turn.

## Frobenius Algebras

Intuitively, a Frobenius manifold is a manifold whose tangent space at each point carries a Frobenius algebra structure.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$A$$ be a finite-dimensional commutative, associative $$\mathbb{C}$$-algebra and let $$\eta: A \otimes A \to \mathbb{C}$$ be a non-degenerate symmetric bilinear form on it. If for all elements $$x,y,z\in A$$ the identity

$$\eta(x \cdot y,z) = \eta(x,y \cdot z)$$

holds, then we call the pair $$(A, \eta)$$ a *Frobenius algebra*.

</div>

This condition means that the multiplication $$\cdot : A \otimes A \to A$$ of $$A$$ and the bilinear form $$\eta$$ are compatible, defining a trilinear form $$c(x,y,z) := \eta(x \cdot y,z)$$ that is symmetric in all three arguments. Indeed, by commutativity

$$c(x,y,z) = \eta(x \cdot y,z) = \eta(y \cdot x,z) = c(y,x,z)$$

and by the Frobenius condition

$$c(x,y,z) = \eta(x,y \cdot z) = \eta(y \cdot z, x) = c(y,z,x).$$

Hence $$c$$ is completely symmetric in the three variables, and this trilinear form encodes all the information of the Frobenius structure.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> The cohomology ring $$H^\ast(X, \mathbb{C})$$ of a compact Kähler manifold $$X$$ is a Frobenius algebra under the cup product and the Poincaré pairing

$$\eta(\alpha, \beta) = \int_X \alpha \smile \beta.$$

This is the statement that the identity

$$\eta(\alpha \smile \beta, \gamma) = \eta(\alpha, \beta \smile \gamma)$$

holds for all $$\alpha,\beta,\gamma$$, and this identity follows from the associativity of the cup product.

</div>

Meanwhile, in the examples of [§Overview of Mirror Symmetry](/en/math/mirror_symmetry/overview) we introduced the Landau–Ginzburg model, which consists of a holomorphic function $$W$$ on a given manifold $$\check{X}$$; the Jacobi ring containing the critical points of $$W$$ carries the information of the B-model. Locally this is written as follows.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A holomorphic function $$f : \mathbb{C}^n \to \mathbb{C}$$ has an *isolated hypersurface singularity* at the origin if the following two conditions hold.

1. $$f(0) = 0$$, $$df(0) = 0$$.
2. The origin is *isolated* among the critical points of $$f$$, i.e., in some neighborhood of the origin the only solution of $$df = 0$$ is the origin itself.

</div>

The standard example is $$f(\x) = \x^{k+1}$$ ($$k \geq 1$$), which we call an $$A_k$$-type singularity.

Now suppose that every critical point of a polynomial $$f:\mathbb{C}^n \rightarrow \mathbb{C}$$ is an isolated hypersurface singularity. Then we may consider its *Jacobi ring*

$$\Jac(f) = \mathbb{C}[\x_1, \ldots, \x_n]/(\partial_1 f, \ldots, \partial_n f).$$

Its dimension $$\mu(f)=\dim \Jac(f)$$ counts the singularities of $$f$$ with multiplicities; intuitively, one may think of it as the number of simple critical points obtained by a small perturbation. In singularity theory this $$\mu(f)$$ is called the *Milnor number* of $$f$$.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For a polynomial $$f : \mathbb{C}^n \to \mathbb{C}$$ all of whose critical points are isolated hypersurface singularities, we define the *residue pairing* $$\eta$$ on the Jacobi ring $$\Jac(f)$$ by the formula

$$\eta(g, h) := \frac{1}{(2\pi i)^n} \oint_{\Gamma_\epsilon} \frac{g(\x) h(\x) \, d\x_1 \wedge \cdots \wedge d\x_n}{\partial_1 f \cdots \partial_n f}.$$

Here the integration contour $$\Gamma_\epsilon$$ is a small loop encircling all points of $$\Crit(f)=\{df=0\}$$; one may think of this integral as the sum of local contributions at each critical point regarded as a fat point containing multiplicity information.

Thus, intuitively, this can be thought of as localizing the global integral $$\int_X$$ of [Example 2](#ex2) to integrals over the (finitely many) points of the critical scheme, and one can show that $$(\Jac(f), \eta)$$ is actually a Frobenius algebra in a manner similar to that example.

In general, if all critical points of $$f$$ are *non-degenerate*, i.e., the Hessian $$\Hess_p(f) = (\partial_i \partial_j f(p))_{ij}$$ is invertible at each $$p \in \Crit(f)$$, then the above integral simplifies to

$$\eta(g, h) = \sum_{p \in \Crit(f)} \frac{g(p)\, h(p)}{\det \Hess_p(f)}.$$

More fundamentally, $$\Jac(f)$$ itself decomposes as

$$\Jac(f)=\bigoplus_{p\in \Crit(f)}\mathbb{C},$$

and with respect to this basis the residue pairing diagonalizes as $$\operatorname{diag}(1/\det \Hess_p(f))$$ on the critical-point basis.

As a special example, consider the Hori–Vafa superpotential of $$\mathbb{P}^1$$ seen in [§Overview of Mirror Symmetry, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5):

$$W_q = \x + \frac{q}{\x}.$$

Its critical points are the two points $$\x_\pm = \pm\sqrt{q}$$.

One should be a bit careful that the ambient space $$\check{X}$$ is not affine space but an algebraic torus, so the differential form defined on it is not simply $$d\x$$. In fact, by [\[Toric Geometry\] §Logarithmic Differential Forms on Toric Varieties, ⁋Definition 1](/en/math/toric_geometry/logarithmic_differentials#def1) the differential form on it is given by $$d\x/\x$$, which corresponds to the coordinate $$\u=\log\x$$ on the torus. Then $$d\u=d\x/\x$$ and $$\partial_\u=\x\partial_\x$$, and computing the derivatives of $$W_q$$ in these coordinates in order to obtain the Hessian gives

$$\partial_\u W_q = \x \partial_\x W_q = \x - q/\x, \qquad \partial_\u^2 W_q = \partial_\u(\x - q/\x) = \x + q/\x,$$

and at the critical points $$\x_\pm = \pm\sqrt{q}$$ we have

$$\Hess_{\x_\pm}(W_q)=\partial_\u^2 W_q \big\vert_{\x_\pm} = \x_\pm + q/\x_\pm = 2\x_\pm = \pm 2\sqrt{q}.$$

Applying the above formula to the two critical points, the residue pairing becomes

$$\eta(g, h) = \frac{g(\sqrt{q})\,h(\sqrt{q})}{2\sqrt{q}} + \frac{g(-\sqrt{q})\,h(-\sqrt{q})}{-2\sqrt{q}}.$$

Computing this directly on the basis $$\{1, \x\}$$ of $$\Jac(W_q) = \mathbb{C}[\x^{\pm 1}, q^{\pm 1}]/(\x^2 - q)$$ yields

$$\eta(1, 1) = \frac{1}{2\sqrt{q}} + \frac{1}{-2\sqrt{q}} = 0, \qquad \eta(1, \x) = \frac{\sqrt{q}}{2\sqrt{q}} + \frac{-\sqrt{q}}{-2\sqrt{q}} = 1, \qquad \eta(\x, \x) = \frac{q}{2\sqrt{q}} + \frac{q}{-2\sqrt{q}} = 0,$$

so the matrix representation of $$\eta$$ in this basis is $$\begin{pmatrix}0&1\\1&0\end{pmatrix}$$. This exactly coincides with the classical Poincaré pairing of $$\mathbb{P}^1$$, showing that the ring isomorphism $$\Jac(W_q) \cong QH^\ast(\mathbb{P}^1)$$ is in fact an isomorphism of Frobenius algebras.

In the same way, consider the Hori–Vafa superpotential of $$\mathbb{P}^2$$ seen in [§Overview of Mirror Symmetry, ⁋Example 6](/en/math/mirror_symmetry/overview#ex6):

$$W_q = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}.$$

In the log coordinates $$\u_i = \log \z_i$$ the derivatives of $$W_q$$ are

$$\partial_{\u_1} W_q = \z_1 - q/(\z_1 \z_2), \qquad \partial_{\u_2} W_q = \z_2 - q/(\z_1 \z_2).$$

Setting both to zero gives $$\z_1 = \z_2 = \z$$ with $$\z^3 = q$$, so the critical points are the three points

$$\z_k = \omega^k q^{1/3},\qquad k = 0, 1, 2,$$

and $$\Jac(W_q) \cong \mathbb{C}[\z, q^{\pm 1}]/(\z^3 - q)$$ has basis $$\{1, \z, \z^2\}$$. Collecting the second derivatives of $$W_q$$ in log coordinates to compute the Hessian gives

$$\Hess(W_q) = \begin{pmatrix} \z_1 + \frac{q}{\z_1 \z_2} & \frac{q}{\z_1 \z_2} \\ \frac{q}{\z_1 \z_2} & \z_2 + \frac{q}{\z_1 \z_2} \end{pmatrix},$$

and at a critical point we have $$q/(\z_1 \z_2) = \z^3/\z^2 = \z$$, so

$$\Hess_{\z_k}(W_q) = \begin{pmatrix} 2\z_k & \z_k \\ \z_k & 2\z_k \end{pmatrix}, \qquad \det \Hess_{\z_k}(W_q) = 3\z_k^2.$$

Applying the above formula to the three critical points, the residue pairing is

$$\eta(\z^a, \z^b) = \sum_{k=0}^{2} \frac{(\omega^k q^{1/3})^{a+b}}{3 (\omega^k q^{1/3})^2} = \frac{q^{(a+b-2)/3}}{3} \sum_{k=0}^{2} \omega^{k(a+b-2)},$$

and

$$\sum_{k=0}^{2} \omega^{km} = 3\iff m \equiv 0 \pmod 3,$$

while this sum is $$0$$ otherwise. Thus for $$0 \leq a, b \leq 2$$ we have $$\eta(\z^a, \z^b) = 1$$ only when $$a + b = 2$$, and it is $$0$$ otherwise. Hence the matrix representation of $$\eta$$ in this basis is

$$\begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix},$$

which again agrees with the classical Poincaré pairing of $$\mathbb{P}^2$$.

</div>

## Frobenius Manifolds

In the preceding section we defined Frobenius algebras and saw that they upgrade the ring isomorphism $$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$ of mirror symmetry to the level of Frobenius algebras. However, the mirror symmetry isomorphism

$$\Jac(W_q)\cong QH^\ast(X)$$

is still not stated in its full strength; the naturality of mirror symmetry lies in the fact that this isomorphism possesses a certain naturality. That is, this isomorphism defines a family of isomorphisms that deform smoothly as $$q$$ varies, and to realize this we must first consider the situation in which a Frobenius algebra is parametrized by a specific variable ($$q$$).

To this end we define the notion of a Frobenius manifold. Of course a Frobenius manifold should be a manifold whose tangent space at each point is a Frobenius algebra, but this is not the whole story; naturally this structure should move smoothly along the base manifold.

First consider the tangent bundle $$TM$$ over a Frobenius manifold $$M$$. Since each fiber of $$TM$$ must be a Frobenius algebra, at each point $$p\in M$$ the space $$T_pM$$ needs a multiplication $$\circ$$ as an algebra, an identity element $$e$$ for this multiplication, and the pairing $$\eta$$ of a Frobenius algebra. For these to constitute a smooth structure, $$\circ$$ must vary smoothly with $$p$$, i.e., $$\circ_p:T_pM\otimes T_pM\rightarrow T_pM$$, and $$\eta$$ must be a smooth non-degenerate bilinear form. Moreover, the identity element should be a (smooth) section of $$TM$$, i.e., a vector field.

In differential geometry it is a connection that enables us to compare different tangent spaces. ([\[Riemannian Geometry\] §Connections, ⁋Definition 1](/en/math/riemannian_geometry/connection#def1)) Since every pseudo-Riemannian manifold $$M$$ admits a compatible Levi-Civita connection $$\nabla$$ ([\[Riemannian Geometry\] §The Levi-Civita Connection, ⁋Theorem 4](/en/math/riemannian_geometry/Levi-Civita_connection#thm4)), it suffices to use this one.

Moreover, given any connection $$\nabla$$, there exists *parallel transport* along a curve $$\gamma$$ on $$M$$ joining the initial point $$x_0$$ to the final point $$x_1$$. ([\[Riemannian Geometry\] §The Levi-Civita Connection, ⁋Definition 7](/en/math/riemannian_geometry/Levi-Civita_connection#def7)) To deform a Frobenius algebra with the points of the manifold as parameters we must use this parallel transport, but if the deformation depended on the curve used to move from one point to another this would not be a desirable situation. ([\[Riemannian Geometry\] §Riemann Curvature, ⁋Example 1](/en/math/riemannian_geometry/curvature#ex1)) Hence we wish this $$\nabla$$ to be *flat*. ([\[Riemannian Geometry\] §Riemann Curvature, ⁋Definition 6](/en/math/riemannian_geometry/curvature#def6))

Finally, since $$QH^\ast(X)$$ already carries a grading, additional data reflecting this are needed. Recall that the grading on $$QH^\ast(X)$$ was obtained by adding to the classical cohomology grading $$H^\ast(X)$$ the grading coming from the Novikov ring. That is, writing $$QH^\ast(X) = H^\ast(X) \otimes_\mathbb{C} \Lambda$$, the degree of a generator $$T_\alpha \otimes q^\beta$$ was given by $$\deg(T_\alpha \otimes q^\beta) = p_\alpha + 2\, c_1 \cdot \beta$$. ([\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 2](/en/math/symplectic_geometry/quantum_cohomology#def2))

The data of this grading are encoded by a *vector field* on the manifold $$M$$ called the *Euler vector field* $$E$$. The *infinitesimal deformation* of the multiplication $$\circ$$ along the flow of $$E$$ is given by the Lie derivative $$\Lie_E(\circ)$$; the fact that the quantum product respects the degree, which we examined in [§Quantum Cohomology](/en/math/symplectic_geometry/quantum_cohomology), is expressed by the identity

$$\Lie_E(\circ) = \circ.$$

Similarly, in our intuition $$\eta$$ is the Poincaré pairing ([Example 2](#ex2)), which survives only in top degree, so this degree condition translates as

$$\Lie_E(\eta) = (2 - d)\eta.$$

The Euler vector field is an *affine* vector field satisfying $$\nabla^2 E=0$$, and *exactly* these two conditions determine $$E$$ completely.

Now we have assembled all the ingredients needed to define a Frobenius manifold.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> A tuple $$(M, \eta, \circ, e, E)$$ is called a *Frobenius manifold* if the following conditions all hold.

1. The Levi-Civita connection induced by the symmetric non-degenerate bilinear form $$\eta$$ on $$TM$$ is flat.
2. For each $$p\in M$$ there exists a commutative associative product $$\circ_p: T_p M \otimes T_p M \to T_p M$$, which is smooth in $$p$$.
3. There exists a vector field $$e$$ that is the identity element for the multiplication $$\circ$$ at every point, and $$\nabla e = 0$$.
4. There exists a vector field $$E$$ satisfying the affine condition $$\nabla^2 E=0$$ such that for a suitable constant $$d\in \mathbb{C}$$

    $$\Lie_E(\circ)=\circ,\qquad \Lie_E(\eta)=(2-d)\eta$$

    hold.
5. For all vector fields $$X,Y,Z$$ we have $$\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$$.
6. (Potentiality) The $$4$$-tensor $$\nabla c$$ defined by the trilinear form $$c(X,Y,Z):=\eta(X\circ Y, Z)$$ is symmetric in all four variables.

</div>

## WDVV Equation

The last condition of [Definition 5](#def5) is called potentiality because it allows the trilinear form $$c$$ to be expressed as the third derivatives of a suitable scalar function $$F:M \rightarrow \mathbb{C}$$.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a Frobenius manifold $$(M, \eta, \circ, e, E)$$ with flat coordinates $$t^1, \ldots, t^n$$, there exists (locally) a holomorphic function $$F: M \to \mathbb{C}$$ such that

$$c_{\alpha\beta\gamma}(t) := \eta(\partial_{t^\alpha} \circ \partial_{t^\beta}, \partial_{t^\gamma}) = \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\gamma}$$

holds for all $$\alpha, \beta, \gamma$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

In flat coordinates $$t^\alpha$$ the covariant derivative $$\nabla_{\partial_{t^\delta}}$$ coincides with the ordinary partial derivative $$\partial_{t^\delta}$$; hence the potentiality condition of [Definition 5](#def5) means that

$$\partial_{t^\delta} c_{\alpha\beta\gamma} = \partial_{t^\alpha} c_{\delta\beta\gamma}$$

holds symmetrically in the four indices. Since $$c$$ itself is symmetric in its three indices, putting these together shows that the 1-form $$\omega_{\beta\gamma} := \sum_\alpha c_{\alpha\beta\gamma} dt^\alpha$$ is closed. By the Poincaré lemma there exists locally a function $$G_{\beta\gamma}$$ with $$\partial_{t^\alpha} G_{\beta\gamma} = c_{\alpha\beta\gamma}$$; by the symmetry of $$c$$ we have $$G_{\beta\gamma} = G_{\gamma\beta}$$ and also $$\partial_{t^\alpha} G_{\beta\gamma} = \partial_{t^\beta} G_{\alpha\gamma}$$. Applying the Poincaré lemma once more, there exists a function $$H_\gamma$$ such that $$\partial_{t^\beta} H_\gamma = G_{\beta\gamma}$$, and from the symmetry $$\partial_{t^\delta} H_\gamma = \partial_{t^\gamma} H_\delta$$ of $$H_\gamma$$ we finally obtain a scalar function $$F$$ with $$\partial_{t^\gamma} F = H_\gamma$$. Altogether $$\partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F = c_{\alpha\beta\gamma}$$.

</details>

Such an $$F$$ is called the *potential* of the Frobenius manifold. Hence, choosing flat coordinates and letting $$\eta^{\alpha\beta}$$ be the inverse matrix of $$\eta_{\alpha\beta}$$, the structure constants of the multiplication are given by

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_{\gamma, \delta} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\delta} \eta^{\delta\gamma} \partial_{t^\gamma}.$$

Since this multiplication $$\circ$$ is associative, expressing this directly in terms of the structure constants yields the following.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Witten–Dijkgraaf–Verlinde–Verlinde)**</ins> The potential $$F$$ of [Proposition 6](#prop6) satisfies the following equation for all $$\alpha, \beta, \gamma, \delta$$:

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}.$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let us expand the associativity $$(\partial_{t^\alpha} \circ \partial_{t^\beta}) \circ \partial_{t^\gamma} = \partial_{t^\alpha} \circ (\partial_{t^\beta} \circ \partial_{t^\gamma})$$ of the multiplication $$\circ$$ in terms of structure constants. Defining $$C_{\alpha\beta}{}^\gamma := \sum_\delta c_{\alpha\beta\delta} \eta^{\delta\gamma}$$, the multiplication is

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_\gamma C_{\alpha\beta}{}^\gamma \partial_{t^\gamma}\tag{1}$$

and associativity is expressed as

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta.$$

Substituting the result $$c_{\alpha\beta\gamma} = \partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F$$ of [Proposition 6](#prop6) gives

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}.$$

Conversely, the multiplication defined from an $$F$$ satisfying this system of PDEs is automatically associative, so the WDVV equation is exactly equivalent to the associativity of the Frobenius manifold.

</details>

The WDVV equation is a quadratic relation among the third derivatives of $$F$$, and for $$F$$ itself it is a system of third-order nonlinear partial differential equations. On the A-model side of mirror symmetry the Gromov–Witten potential of quantum cohomology is a typical example satisfying this equation, and this is reflected in the *splitting axiom* ([\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Proposition 6](/en/math/symplectic_geometry/gromov_witten#prop6)).

As we see from the proof above, in the language of Frobenius manifolds the WDVV equation is essentially the associativity of $$\circ$$, but in the A-model it takes the less transparent form of the splitting axiom. On the other hand, in the B-model the associativity of $$\circ$$ is immediate because $$\Jac(W)$$ is a quotient ring. Conversely, in the A-model it is transparent that the Gromov–Witten potential plays the role of $$F$$, whereas in the B-model constructing it requires considerable work. This is again an illustration of the philosophy of mirror symmetry: a difficult problem on one side becomes a relatively easy one when transported via the mirror to the other model.

## Examples

The following example is the most basic Frobenius manifold and serves as a benchmark for the more complicated quantum cohomology examples that follow.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Introduce coordinates $$t^1, \ldots, t^n$$ on $$M = \mathbb{C}^n$$ and set

$$\eta = \sum_{i=1}^n dt^i \otimes dt^i,\qquad \partial_{t^i} \circ \partial_{t^j} = \delta_{ij} \partial_{t^i}.$$

This is nothing but the definition of Euclidean space lifted to $$\mathbb{C}$$; that $$\eta$$ is flat, the $$t^i$$ form flat coordinates, and $$e=\sum \partial_{t^i}$$ is the identity for the multiplication are all almost immediate.

Now the Euler vector field of this manifold is exactly the vector field $$\sum_i t^i\partial_{t^i}$$ that we call the Euler vector field in calculus. Indeed, in flat coordinates we have $$E(t^i)=t^i$$, so computing the Lie derivatives gives

$$\Lie_E(dt^i)=d(E(t^i))=dt^i,\qquad \Lie_E(\partial_{t^i})=[E, \partial_{t^i}]=-\partial_{t^i},$$

whence

$$\Lie_E(\eta) = \sum_i \bigl( \Lie_E(dt^i) \otimes dt^i + dt^i \otimes \Lie_E(dt^i) \bigr) = 2 \sum_i dt^i \otimes dt^i = 2\eta.$$

Similarly, for the multiplication, writing $$\circ=\sum dt^i\otimes dt^i\otimes\partial_{t^i}$$ and performing a similar computation shows that $$\Lie_E(\circ)=\circ$$.

Potentiality is obtained almost immediately, and working backwards to find a function whose third derivatives in the $$i,j,k$$ directions give $$\delta_{ijk}$$ yields (of course)

$$F=\frac{1}{6}\sum_i (t^i)^3.$$

Since $$\circ$$ is associative, the WDVV equation holds trivially; nevertheless, if one wishes to check it directly, using $$\eta^{ef} =
