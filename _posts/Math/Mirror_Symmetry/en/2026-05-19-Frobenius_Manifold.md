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
last_polished_at: 2026-10-21T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Mirror Symmetry: An Overview](/en/math/mirror_symmetry/overview){: data-lid="d668d" } we saw that the mirror symmetry of a toric Fano variety $X_\Sigma$ is summarized by an isomorphism 

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

between the Jacobi ring and quantum cohomology. However, as we also observed in that post, quantum cohomology carries more structure than this ring isomorphism captures, because the product itself deforms as the Novikov parameter $q$ varies. The structure capable of capturing such a deformation is the Frobenius manifold; in this post, we first review the definition of a finite-dimensional Frobenius algebra, and then examine Dubrovin's notion of a Frobenius manifold and the WDVV equation in turn.

## Frobenius Algebras

Intuitively, a Frobenius manifold is a manifold that has a Frobenius algebra structure at each point.

::: Definition 1
Let $A$ be a finite-dimensional commutative, associative, unital $\mathbb{C}$-algebra equipped with a non-degenerate symmetric bilinear form $\eta: A \otimes A \rightarrow \mathbb{C}$. If for all elements $x,y,z\in A$ the identity

$$\eta(x \cdot y,z) = \eta(x,y \cdot z)$$

holds, then this pair $(A, \eta)$ is called a *Frobenius algebra*.
:::

This condition means that the multiplication $\cdot : A \otimes A \rightarrow A$ of $A$ and the bilinear form $\eta$ are compatible, defining a trilinear form $c(x,y,z) := \eta(x \cdot y,z)$ that is symmetric in all three arguments. Indeed, from commutativity,

$$c(x,y,z) = \eta(x \cdot y,z) = \eta(y \cdot x,z) = c(y,x,z)$$

and from the Frobenius condition,

$$c(x,y,z) = \eta(x,y \cdot z) = \eta(y \cdot z, x) = c(y,z,x)$$

holds. Therefore, $c$ is completely symmetric in its three variables, and this trilinear form encodes all the information of the Frobenius structure.

::: Example 2
The cohomology ring $H^\ast(X, \mathbb{C})$ of a compact Kähler manifold $X$ with $H^{\mathrm{odd}}(X, \mathbb{C}) = 0$ is a Frobenius algebra with respect to the cup product and the Poincaré pairing

$$\eta(\alpha, \beta) = \int_X \alpha \smile \beta$$

. This means that the identity

$$\eta(\alpha \smile \beta, \gamma) = \eta(\alpha, \beta \smile \gamma)$$

holds for all $\alpha,\beta,\gamma$, which follows from the associativity of the cup product.
:::

Meanwhile, in the examples of [§Mirror Symmetry: An Overview](/en/math/mirror_symmetry/overview){: data-lid="pfswh" } we introduced the Landau–Ginzburg model, which consists of a holomorphic function $W$ on a given manifold $\check{X}$; the Jacobi ring containing the critical points of $W$ carried the information of the B-model. Locally this is written as follows.

::: Definition 3
A holomorphic function $f : \mathbb{C}^n \rightarrow \mathbb{C}$ is said to have an *isolated hypersurface singularity* at the origin if the following two conditions hold.

1. $f(0) = 0$, $\dd{f}(0) = 0$.
2. The origin is *isolated* among the critical points of $f$, i.e., in some neighborhood of the origin the only solution to $\dd{f} = 0$ is the origin itself.
:::

A standard example is $f(\x) = \x^{k+1}$ ($k \geq 1$), which we call an $A_k$-type singularity.

Now suppose every critical point of a polynomial $f:\mathbb{C}^n \rightarrow \mathbb{C}$ is isolated. Then we may consider its *Jacobi ring*

$$\Jac(f) = \mathbb{C}[\x_1, \ldots, \x_n]/(\partial_1 f, \ldots, \partial_n f)$$

. Its dimension $\mu(f)=\dim \Jac(f)$ counts the number of singularities of $f$ including multiplicity; intuitively, one may also think of it as having $\mu(f)$ simple critical points through a small perturbation. In singularity theory this $\mu(f)$ is called the *Milnor number* of $f$.

::: Example 4
On the Jacobi ring $\Jac(f)$ of a polynomial $f : \mathbb{C}^n \rightarrow \mathbb{C}$ all of whose critical points are isolated, the *residue pairing* $\eta$ is defined by the formula

$$\eta(g, h) := \frac{1}{(2\pi i)^n} \oint_{\Gamma_\epsilon} \frac{g(\x) h(\x) \dd{\x_1} \wedge \cdots \wedge \dd{\x_n}}{\partial_1 f \cdots \partial_n f}$$

Here, the integration path $\Gamma_\epsilon$ is taken along a small contour surrounding all points of $\Crit(f)=\{\dd{f}=0\}$, and this integral can be thought of as the value of the integral at those points when the critical points are viewed as fat points containing multiplicity information.

In other words, intuitively this can be thought of as localizing the integral $\int_X$ over the entire manifold in [Example 2](#ex2){: data-lid="z4ug9" } to integrals at the (finitely many) points of the critical scheme, and that $(\Jac(f), \eta)$ is indeed a Frobenius algebra can also be shown in a manner similar to that example.

In general, when all critical points of $f$ are *non-degenerate*, that is, when the Hessian $\Hess_p(f) = (\partial_i \partial_j f(p))_{ij}$ is invertible at each $p \in \Crit(f)$, the above integral can be simply computed as

$$\eta(g, h) = \sum_{p \in \Crit(f)} \frac{g(p) h(p)}{\det \Hess_p(f)}$$

and more fundamentally, $\Jac(f)$ itself decomposes as

$$\Jac(f)=\bigoplus_{p\in \Crit(f)}\mathbb{C}$$

and one can verify that with respect to this basis, the residue pairing is diagonalized on the critical point basis as $\operatorname{diag}(1/\det \Hess_p(f))$.

As a special example, considering the Hori-Vafa superpotential of $\mathbb{P}^1$ seen in [§Mirror Symmetry: An Overview, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5){: data-lid="qz850" }

$$W_q = \x + \frac{q}{\x}$$

its critical points are the two points $\x_\pm = \pm\sqrt{q}$.

One point to be somewhat careful about is that the ambient space $\check{X}$ is not an affine space but an algebraic torus, so the differential form defined on it is not simply $\dd{\x}$. In fact, the differential form on it is given by $\dd{\x}/\x$ by [\[Toric Geometry\] §Logarithmic Differential Forms on Toric Varieties, ⁋Definition 1](/en/math/toric_geometry/logarithmic_differentials#def1), which can be viewed as the coordinate on the torus being given by $\u=\log\x$. Then $d\u=\dd{\x}/\x$ and $\partial_\u=\x\partial_\x$, and computing the successive derivatives of $W_q$ in this coordinate to calculate the Hessian yields

$$\partial_\u W_q = \x \partial_\x W_q = \x - q/\x, \qquad \partial_\u^2 W_q = \partial_\u(\x - q/\x) = \x + q/\x$$

and at the critical points $\x_\pm = \pm\sqrt{q}$, it becomes

$$\Hess_{\x_\pm}(W_q)=\partial_\u^2 W_q \big\vert_{\x_\pm} = \x_\pm + q/\x_\pm = 2\x_\pm = \pm 2\sqrt{q}$$

Applying the above formula to the two critical points, the residue pairing becomes

$$\eta(g, h) = \frac{g(\sqrt{q}) h(\sqrt{q})}{2\sqrt{q}} + \frac{g(-\sqrt{q}) h(-\sqrt{q})}{-2\sqrt{q}}$$

Now, computing this directly on the basis $\{1, \x\}$ of $\Jac(W_q) = \mathbb{C}[\x^{\pm 1}, q^{\pm 1}]/(\x^2 - q)$, we obtain

$$\eta(1, 1) = \frac{1}{2\sqrt{q}} + \frac{1}{-2\sqrt{q}} = 0, \qquad \eta(1, \x) = \frac{\sqrt{q}}{2\sqrt{q}} + \frac{-\sqrt{q}}{-2\sqrt{q}} = 1, \qquad \eta(\x, \x) = \frac{q}{2\sqrt{q}} + \frac{q}{-2\sqrt{q}} = 0$$

so the matrix representation of $\eta$ with respect to this basis is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$. This coincides exactly with the classical Poincaré pairing of $\mathbb{P}^1$, showing that the ring isomorphism $\Jac(W_q) \cong QH^\ast(\mathbb{P}^1)$ was in fact a Frobenius algebra isomorphism.

In the same way, consider the Hori-Vafa superpotential of $\mathbb{P}^2$ seen in [§Mirror Symmetry: An Overview, ⁋Example 6](/en/math/mirror_symmetry/overview#ex6){: data-lid="3jl2x" }

$$W_q = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}$$

In the log coordinates $\u_i = \log \z_i$, computing the derivatives of $W_q$ gives

$$\partial_{\u_1} W_q = \z_1 - q/(\z_1 \z_2), \qquad \partial_{\u_2} W_q = \z_2 - q/(\z_1 \z_2)$$

and setting both to $0$ requires $\z_1 = \z_2 = \z$ and $\z^3 = q$, so the critical points are given by the three points

$$\z_k = \omega^k q^{1/3},\qquad k = 0, 1, 2$$

($\omega = e^{2\pi i/3}$), and $\Jac(W_q) \cong \mathbb{C}[\z, q^{\pm 1}]/(\z^3 - q)$ has the basis $\{1, \z, \z^2\}$. Collecting the second derivatives of $W_q$ in log coordinates to compute the Hessian,

$$\Hess(W_q) = \begin{pmatrix} \z_1 + \frac{q}{\z_1 \z_2} & \frac{q}{\z_1 \z_2} \\ \frac{q}{\z_1 \z_2} & \z_2 + \frac{q}{\z_1 \z_2} \end{pmatrix}$$

and at the critical points, $q/(\z_1 \z_2) = \z^3/\z^2 = \z$, so

$$\Hess_{\z_k}(W_q) = \begin{pmatrix} 2\z_k & \z_k \\ \z_k & 2\z_k \end{pmatrix}, \qquad \det \Hess_{\z_k}(W_q) = 3\z_k^2$$

Applying the above formula to the three critical points, the residue pairing is

$$\eta(\z^a, \z^b) = \sum_{k=0}^{2} \frac{(\omega^k q^{1/3})^{a+b}}{3 (\omega^k q^{1/3})^2} = \frac{q^{(a+b-2)/3}}{3} \sum_{k=0}^{2} \omega^{k(a+b-2)}$$

and

$$\sum_{k=0}^{2} \omega^{km} = 3\iff m \equiv 0 \pmod{3}$$

while in all other cases this value is $0$. That is, for $0 \leq a, b \leq 2$, we have $\eta(\z^a, \z^b) = 1$ only when $a + b = 2$, and $0$ otherwise. That is, one can confirm that the matrix representation of $\eta$ with respect to this basis is, in this case as well, given by the following matrix, which coincides with the classical Poincaré pairing of $\mathbb{P}^2$:

$$\begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$$

:::

## Frobenius Manifolds

In the previous section, we defined Frobenius algebras and verified that this upgrades the mirror symmetry ring isomorphism $\Jac(W_q) \cong QH^\ast(X_\Sigma)$ to the level of Frobenius algebras. However, the mirror symmetry isomorphism

$$\Jac(W_q)\cong QH^\ast(X)$$

is still not stated in its full power: the naturalness of mirror symmetry lies in the fact that this isomorphism also possesses a kind of naturality. That is, this isomorphism defines a family of isomorphisms that deform smoothly along the variation of $q$, and to actually realize this, we must first consider the situation where a Frobenius algebra is parametrized by a specific variable ($q$).

To this end, we define the notion of a Frobenius manifold. Naturally, a Frobenius manifold would be a manifold whose tangent space at each point is a Frobenius algebra, but that is not all; naturally, this structure must move smoothly along the base manifold.

First, for the tangent bundle $TM$ defined on a Frobenius manifold $M$, since each fiber of $TM$ must be a Frobenius algebra, at each point $p\in M$ the space $T_pM$ requires a multiplication $\circ$ as an algebra, an identity element $e$ for this multiplication, and the pairing $\eta$ of a Frobenius algebra. For these to constitute a smooth structure, $\circ$ should be a map $\circ_p:T_pM\otimes T_pM\rightarrow T_pM$ that varies smoothly with respect to $p$, and $\eta$ should be a smooth non-degenerate bilinear form. In addition, the identity element must be a (smooth) section of $TM$, that is, a vector field.

In differential geometry, what allowed us to compare different tangent spaces was a connection. ([\[Riemannian Geometry\] §Connection, ⁋Definition 1](/en/math/riemannian_geometry/connection#def1){: data-lid="d6d4l" }) In general, on any pseudo-Riemannian manifold $M$ there always exists a compatible Levi-Civita connection $\nabla$ ([\[Riemannian Geometry\] §Levi-Civita Connection, ⁋Theorem 4](/en/math/riemannian_geometry/Levi-Civita_connection#thm4)), so it is sufficient to use this.

On the other hand, given any connection $\nabla$, there existed *parallel transport* connecting the starting point $x_0$ and the endpoint $x_1$ of a curve along a curve $\gamma$ lying on $M$. ([\[Riemannian Geometry\] §Levi-Civita Connection, ⁋Definition 8](/en/math/riemannian_geometry/Levi-Civita_connection#def8)) To deform the Frobenius algebra using the points of the manifold as parameters, we must use this parallel transport; if this deformation depended on the curve taking one point to another, this would not be a very good situation. ([\[Riemannian Geometry\] §Riemann Curvature, ⁋Example 1](/en/math/riemannian_geometry/curvature#ex1)) That is, we want this $\nabla$ to be *flat*. ([\[Riemannian Geometry\] §Riemann Curvature, ⁋Definition 6](/en/math/riemannian_geometry/curvature#def6))

Finally, since $QH^\ast(X)$ is already endowed with a grading, additional data are needed to reflect this. Here, recall that the grading of $QH^\ast(X)$ was obtained by adding to the classical cohomology $H^\ast(X)$ the grading coming from the grading of the Novikov ring. That is, when $QH^\ast(X) = H^\ast(X) \otimes_\mathbb{C} \Lambda$, the degree of any generator $T_\alpha \otimes q^\beta$ was given by $\deg(T_\alpha \otimes q^\beta) = \deg T_\alpha + 2c_1 \cdot \beta$. ([\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 2](/en/math/symplectic_geometry/quantum_cohomology#def2))

Encoding such grading data as a *vector field* on the manifold $M$ yields the *Euler vector field* $E$. When the multiplication $\circ$ is flowed along the flow of $E$, its *infinitesimal deformation* is given by the Lie derivative $\mathcal{L}_E(\circ)$; the fact that the quantum product examined in [\[Symplectic Geometry\] §Quantum Cohomology](/en/math/symplectic_geometry/quantum_cohomology) respects degrees can be expressed by the equation

$$\mathcal{L}_E(\circ) = \circ$$

Similarly, in our intuition $\eta$ is the Poincaré pairing ([Example 2](#ex2){: data-lid="341lo" }), and since this survives only in the top degree, this degree condition translates to

$$\mathcal{L}_E(\eta) = (2 - d)\eta$$

Now the Euler vector field is an *affine* vector field satisfying $\nabla^2 E=0$, and these two conditions are all that is required of $E$.

Now we have completed all the ingredients for defining a Frobenius manifold.

::: Definition 5
$(M, \eta, \circ, e, E)$ is called a *Frobenius manifold* if the following conditions all hold. 

1. On $TM$, the Levi-Civita connection induced by the symmetric non-degenerate bilinear form $\eta$ is flat. 
2. For each $p\in M$, there exists a commutative associative product $\circ_p: T_p M \otimes T_p M \rightarrow T_p M$ that is smooth with respect to $p$. 
3. For the multiplication $\circ$, there exists a vector field $e$ that is the identity element at every point, and $\nabla e = 0$.
4. Satisfying the affine condition $\nabla^2 E=0$, there exists a vector field $E$ such that for a suitable constant $d\in \mathbb{C}$,
    
    $$\mathcal{L}_E(\circ)=\circ,\qquad \mathcal{L}_E(\eta)=(2-d)\eta$$

    holds.
5. For all vector fields $X,Y,Z$, $\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$ holds.
6. (Potentiality) The trilinear form $c(X,Y,Z):=\eta(X\circ Y, Z)$ defines a $4$-tensor $\nabla c$ that is symmetric in all four variables. 
:::

## WDVV equation

The reason the last condition of [Definition 5](#def5){: data-lid="zvo4a" } is called potentiality is that it expresses the trilinear form $c$ as the third derivatives of a suitable scalar function $F:M \rightarrow \mathbb{C}$. 

::: Proposition 6
For a Frobenius manifold $(M, \eta, \circ, e, E)$ with flat coordinates $t^1, \ldots, t^n$, there exists on $M$ a (locally) defined holomorphic function $F: M \rightarrow \mathbb{C}$ such that

$$c_{\alpha\beta\gamma}(t) := \eta(\partial_{t^\alpha} \circ \partial_{t^\beta}, \partial_{t^\gamma}) = \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\gamma}$$

holds for all $\alpha, \beta, \gamma$. 
:::

::: Proof
For flat coordinates $t^\alpha$, the covariant derivative $\nabla_{\partial_{t^\delta}}$ coincides with the ordinary partial derivative $\partial_{t^\delta}$, so the potentiality condition of [Definition 5](#def5){: data-lid="k6ngz" } means that

$$\partial_{t^\delta} c_{\alpha\beta\gamma} = \partial_{t^\alpha} c_{\delta\beta\gamma}$$

holds symmetrically in all four indices. Meanwhile, since $c$ itself is symmetric in three indices, putting these together shows that the 1-form $\omega_{\beta\gamma} := \sum_\alpha c_{\alpha\beta\gamma} \dd{t}^\alpha$ is closed. By the Poincaré lemma, there locally exist functions $G_{\beta\gamma}$ such that $\partial_{t^\alpha} G_{\beta\gamma} = c_{\alpha\beta\gamma}$; from the symmetry of $c$, $G_{\beta\gamma} - G_{\gamma\beta}$ is constant, so by adjusting the constants of integration we can set $G_{\beta\gamma} = G_{\gamma\beta}$, and $\partial_{t^\alpha} G_{\beta\gamma} = \partial_{t^\beta} G_{\alpha\gamma}$ also holds. Applying the Poincaré lemma once more, there exist functions $H_\gamma$ such that $\partial_{t^\beta} H_\gamma = G_{\beta\gamma}$, and from the symmetry of $H_\gamma$, $\partial_{t^\delta} H_\gamma = \partial_{t^\gamma} H_\delta$, finally there exists a scalar function $F$ such that $\partial_{t^\gamma} F = H_\gamma$ holds. Altogether, $\partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F = c_{\alpha\beta\gamma}$.
:::

Such an $F$ is called the *potential* of the Frobenius manifold. From this, if we choose flat coordinates and let $\eta^{\alpha\beta}$ be the inverse matrix of $\eta_{\alpha\beta}$, the structure constants of the multiplication are given by

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_{\gamma, \delta} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^\delta} \eta^{\delta\gamma} \partial_{t^\gamma}$$

However, since this multiplication $\circ$ is associative, calculating this directly using structure constants yields the following.

::: Proposition 7 (Witten–Dijkgraaf–Verlinde–Verlinde)
The potential $F$ of [Proposition 6](#prop6){: data-lid="5flln" } satisfies the following equation for all $\alpha, \beta, \gamma, \delta$:

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}$$
:::

::: Proof
Let us write out the associativity of the multiplication $\circ$, namely $(\partial_{t^\alpha} \circ \partial_{t^\beta}) \circ \partial_{t^\gamma} = \partial_{t^\alpha} \circ (\partial_{t^\beta} \circ \partial_{t^\gamma})$, in terms of structure constants. Defining $C_{\alpha\beta}{}^\gamma := \sum_\delta c_{\alpha\beta\delta} \eta^{\delta\gamma}$, the multiplication is

$$\partial_{t^\alpha} \circ \partial_{t^\beta} = \sum_\gamma C_{\alpha\beta}{}^\gamma \partial_{t^\gamma}\tag{1}$$

and associativity is expressed as

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta$$

Substituting into this the result $c_{\alpha\beta\gamma} = \partial_{t^\alpha} \partial_{t^\beta} \partial_{t^\gamma} F$ of [Proposition 6](#prop6){: data-lid="fku6d" }, we obtain

$$\sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\beta \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\gamma \partial t^\delta} = \sum_{e, f} \frac{\partial^3 F}{\partial t^\alpha \partial t^\gamma \partial t^e} \eta^{ef} \frac{\partial^3 F}{\partial t^f \partial t^\beta \partial t^\delta}$$

Conversely, the multiplication defined from $F$ satisfying this system of PDEs is automatically associative, so the WDVV equation is a condition precisely equivalent to the associativity of the Frobenius manifold.
:::

The WDVV equation is a quadratic relation among the third derivatives of $F$, and for $F$ itself it is a system of third-order nonlinear partial differential equations. On the A-model side of mirror symmetry, the Gromov–Witten potential of quantum cohomology is a representative example satisfying this equation, which is reflected in the *splitting axiom* ([\[Symplectic Geometry\] §Gromov–Witten Invariants, ⁋Proposition 6](/en/math/symplectic_geometry/gromov_witten#prop6){: data-lid="jjmrt" }).

As the proof above shows, in the language of Frobenius manifolds the WDVV equation is essentially the associativity of $\circ$; note, however, that on the A-model side it takes the less obvious form of the splitting axiom. On the other hand, in the B-model the associativity of $\circ$ is obtained trivially because $\Jac(W)$ is a quotient of a ring. Conversely, in the A-model it is transparent that the Gromov–Witten potential plays the role of $F$, whereas in the B-model constructing it requires considerable work. This is again an illustration of the philosophy of mirror symmetry: a difficult problem on one side becomes relatively easy when transferred to the opposite model via the mirror.

## Examples

The following example is the most basic Frobenius manifold, and serves as a benchmark for the more complicated quantum cohomology examples that follow.

::: Example 8
On $M = \mathbb{C}^n$, introduce coordinates $t^1, \ldots, t^n$ and set

$$\eta = \sum_{i=1}^n \dd{t}^i \otimes \dd{t}^i,\qquad \partial_{t^i} \circ \partial_{t^j} = \delta_{ij} \partial_{t^i}$$

This is simply the definition of Euclidean space lifted to $\mathbb{C}$; facts such as that $\eta$ is flat, that the $t^i$ form flat coordinates, and that $e=\sum \partial_{t^i}$ is the unit for the multiplication are obtained almost trivially.

Now the Euler vector field of this manifold is precisely the vector field $\sum_i t^i\partial_{t^i}$ that we call the Euler vector field in calculus. Indeed, since $E(t^i)=t^i$ in flat coordinates, computing the Lie derivatives gives

$$\mathcal{L}_E(\dd{t}^i)=\dd{(E(t^i))}=\dd{t}^i,\qquad \mathcal{L}_E(\partial_{t^i})=[E, \partial_{t^i}]=-\partial_{t^i}$$

from which we see that

$$\mathcal{L}_E(\eta) = \sum_i \bigl( \mathcal{L}_E(\dd{t}^i) \otimes \dd{t}^i + \dd{t}^i \otimes \mathcal{L}_E(\dd{t}^i) \bigr) = 2 \sum_i \dd{t}^i \otimes \dd{t}^i = 2\eta$$

Similarly, for the multiplication, writing $\circ=\sum \dd{t}^i\otimes \dd{t}^i\otimes\partial_{t^i}$ and performing a similar computation shows that $\mathcal{L}_E(\circ)=\circ$.

Potentiality is obtained almost trivially; working backwards to find what function yields $\delta_{ijk}$ when differentiated successively in the $i,j,k$ directions, one can verify that (of course) setting

$$F=\frac{1}{6}\sum_i (t^i)^3$$

suffices. Since $\circ$ is associative, the WDVV equation will hold trivially; if one insists on computing it, using $\eta^{ef} = \delta_{ef}$ gives structure constants $C_{\alpha\beta}{}^e = \delta_{\alpha\beta}\delta_{\beta e}$, and one can verify once again that

$$\sum_e C_{\alpha\beta}{}^e C_{e\gamma}{}^\delta = \delta_{\alpha\beta}\delta_{\alpha\gamma}\delta_{\gamma\delta} = \delta_{\alpha\beta\gamma\delta} = \delta_{\alpha\gamma}\delta_{\alpha\beta}\delta_{\beta\delta} = \sum_e C_{\alpha\gamma}{}^e C_{e\beta}{}^\delta$$

holds trivially.
:::

In this example the coordinates $t^i$ are very nice: in these coordinates the multiplication $\circ$ is naturally diagonalized. In general, if the multiplication $\circ_p$ is represented as a direct sum of idempotents at a generic point, we call this a *semisimple* Frobenius manifold; [Example 8](#ex8){: data-lid="m8lbn" } is the simplest such example.

Let us now turn to what we originally intended to discuss in this post: understanding quantum cohomology as a Frobenius manifold. For a compact Kähler manifold $X$, we take the base to be the cohomology vector space itself,

$$M = H^\ast(X, \mathbb{C})$$

and, dual to a cohomology basis $\{\sigma^\alpha\}$, introduce formal coordinates $t = \sum_\alpha t^\alpha \sigma^\alpha$. Since $M$ is itself a vector space, the tangent space $T_tM$ at each point is canonically isomorphic to $H^\ast(X, \mathbb{C})$. Therefore endowing this with a Frobenius manifold structure is the same as endowing $T_tM\cong H^\ast(X, \mathbb{C})$ with a Frobenius product $\circ_t$, and (naturally) we choose this to be the multiplication $\circ_t$ of big quantum cohomology, i.e., the multiplication defined by the third derivatives of the GW potential $F(t)$. ([\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12){: data-lid="1zrzq" }) The next proposition shows that these data actually form a Frobenius manifold.

::: Proposition 9
Given $H^{\mathrm{odd}}(X, \mathbb{C}) = 0$ for a compact Kähler manifold $X$, if on $M = H^\ast(X, \mathbb{C})$ we define the big quantum product $\circ_t$ ([\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12)), the Poincaré pairing $\eta$, the unit $e = 1 \in H^0(X)$, and the Euler vector field

$$E = \sum_\alpha \Bigl(1 - \frac{1}{2}\deg \sigma^\alpha\Bigr) t^\alpha \partial_{t^\alpha} + \sum_\alpha r^\alpha \partial_{t^\alpha}, \qquad c_1(X) = \sum_\alpha r^\alpha \sigma^\alpha$$

then $(M, \eta, \circ_t, e, E)$ is a Frobenius manifold ([Definition 5](#def5){: data-lid="j7emg" }).
:::

::: Proof
We verify the six conditions of [Definition 5](#def5){: data-lid="j1m5q" } in order. 

1. First, the Poincaré pairing $\eta_{\alpha\beta} = \int_X \sigma_\alpha \smile \sigma_\beta$ is constant in the linear coordinates $t^\alpha$, so its Levi-Civita connection is flat and the $t^\alpha$ form flat coordinates. 
2. For the second condition, the multiplication $\circ_t$ is commutative and associative by [\[Symplectic Geometry\] §Quantum Cohomology, ⁋Theorem 6](/en/math/symplectic_geometry/quantum_cohomology#thm6), and smooth in $t$.
3. The unit for this multiplication is $1 \in H^0(X)$, which is a constant section in flat coordinates, so $\nabla e = 0$. 
4. Meanwhile, by [\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12), the structure constants are $c_{\alpha\beta\gamma}(t) = \eta(\partial_{t^\alpha} \circ_t \partial_{t^\beta}, \partial_{t^\gamma}) = \partial_{t^\alpha}\partial_{t^\beta}\partial_{t^\gamma} F$, so from the fact that this is symmetric in the three indices we obtain $\eta(X \circ Y, Z) = \eta(X, Y \circ Z)$.
5. Similarly, one checks that $\nabla c$ is symmetric in the four indices; under this potentiality, associativity is equivalent to the WDVV equation of [Proposition 7](#prop7){: data-lid="6j8s9" }, and on the A-model side it is guaranteed by the splitting axiom for GW invariants. 
6. Finally, the grading of [\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 2](/en/math/symplectic_geometry/quantum_cohomology#def2) translates, as seen in the text above, into $\mathcal{L}_E(\circ) = \circ$, $\mathcal{L}_E(\eta) = (2-d)\eta$, and the given $E$ satisfies this as an affine vector field with $\nabla^2 E = 0$.
:::

Meanwhile, considering our mirror symmetry statement

$$\Jac(W_q)\cong QH^\ast(X)$$

this ultimately depends on the deformation by the quantum parameter $q$, so if we consider only this level, big quantum cohomology is somewhat too large, and we need only consider the deformation in the $H^2$ direction, or small quantum cohomology. Even at a more general level, one could study mirror symmetry including big quantum cohomology and bulk deformations of $W_q$, but since this deviates from our primary goal, in most cases we shall consider only the deformation in the $H^2$ direction. In the following $\mathbb{P}^1$ example, excluding the unit direction $H^0$, $H^2$ is all of the cohomology (as there are no $\deg \ge 4$ directions), so big quantum cohomology coincides with small quantum cohomology; thus the computation below directly realizes [Proposition 9](#prop9){: data-lid="5xeem" }.

::: Example 10
To verify explicitly that the above multiplication $\circ_t$ varies with $t$, let us compute the case $X = \mathbb{P}^1$. Since the manifold $M = H^\ast(\mathbb{P}^1) = \mathbb{C}\langle 1, H\rangle$ is itself a vector space, coordinates on it are given by the dual of the cohomology basis $\{1, H\}$; let us denote these by $t^0, t^1$, respectively.

The Gromov–Witten potential of $\mathbb{P}^1$ is now given by

$$F(t^0, t^1) = \frac{1}{2}(t^0)^2 t^1 + e^{t^1}$$

([\[Symplectic Geometry\] §Quantum Cohomology, ⁋Definition 12](/en/math/symplectic_geometry/quantum_cohomology#def12){: data-lid="22snw" }). Here the first term is the contribution from the classical cup product, and the second term can be thought of as the contribution $\langle H, H, H\rangle_{0,3,1} = 1$ from the degree-$1$ rational curve of [§Mirror Symmetry: An Overview, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5){: data-lid="xphkx" }, accumulated exponentially along the $H^2$ direction coordinate $t^1$ (via the Euler vector field). The metric was already computed in [Example 4](#ex4){: data-lid="p30hw" }, and computing the third partial derivatives of $F$ from the above formula gives

$$\partial_{t^0}^3 F = 0,\qquad \partial_{t^0}^2\partial_{t^1} F = 1,\qquad \partial_{t^0}\partial_{t^1}^2 F = 0,\qquad \partial_{t^1}^3 F = e^{t^1}$$

. Since the inverse matrix of $\eta$ is itself anyway, calculating using (1) we obtain

$$\partial_{t^0} \circ_t \partial_{t^\alpha} = \partial_{t^\alpha}, \qquad \partial_{t^1} \circ_t \partial_{t^1} = e^{t^1} \partial_{t^0}$$

. The first equation then shows that $\partial_{t^0}$ plays the role of the unit $e$, and the fact that the right-hand side of the second equation depends on $t^1$ shows that the multiplication deforms over the manifold.

The Euler field is obtained by substituting $\deg 1 = 0$, $\deg H = 2$, and $c_1(\mathbb{P}^1) = 2H$ into the general formula above, giving

$$E = t^0 \partial_{t^0} + 2\partial_{t^1}$$

. Since $E(t^0) = t^0$ and $E(t^1) = 2$, the Lie derivatives of the components are

$$\mathcal{L}_E(\dd{t}^0) = \dd{t}^0, \quad \mathcal{L}_E(\dd{t}^1) = 0, \quad \mathcal{L}_E(\partial_{t^0}) = [E, \partial_{t^0}] = -\partial_{t^0}, \quad \mathcal{L}_E(\partial_{t^1}) = [E, \partial_{t^1}] = 0$$

; applying this to the metric $\eta = \dd{t}^0 \otimes \dd{t}^1 + \dd{t}^1 \otimes \dd{t}^0$, each term has weight $1 + 0 = 1$, so

$$\mathcal{L}_E(\eta) = \mathcal{L}_E(\dd{t}^0)\otimes \dd{t}^1 + \dd{t}^1 \otimes \mathcal{L}_E(\dd{t}^0) = \dd{t}^0 \otimes \dd{t}^1 + \dd{t}^1 \otimes \dd{t}^0 = \eta$$

, yielding $2 - d = 1$, which equals $\dim_\mathbb{C}\mathbb{P}^1$. By a similar computation, the nontrivial part of the multiplication $\circ$ is the tensor $e^{t^1}\dd{t}^1 \otimes \dd{t}^1 \otimes \partial_{t^0}$ (i.e., $\partial_{t^1} \circ \partial_{t^1} = e^{t^1}\partial_{t^0}$); since $\mathcal{L}_E(e^{t^1}) = E(e^{t^1}) = 2e^{t^1}$ (weight $2$), the two $\dd{t}^1$ have weight $0$, and $\partial_{t^0}$ has weight $-1$, we obtain

$$\mathcal{L}_E\bigl(e^{t^1}\dd{t}^1 \otimes \dd{t}^1 \otimes \partial_{t^0}\bigr) = (2 + 0 + 0 - 1) e^{t^1}\dd{t}^1 \otimes \dd{t}^1 \otimes \partial_{t^0} = e^{t^1}\dd{t}^1 \otimes \dd{t}^1 \otimes \partial_{t^0}$$

, so that $\mathcal{L}_E(\circ) = \circ$.

Now setting the Novikov variable to $q = e^{t^1}$, the second equation becomes $\partial_{t^1} \circ \partial_{t^1} = qe$, which translates back into cohomology language as $H \star H = q \cdot 1$, recovering the small quantum ring of [§Mirror Symmetry: An Overview, ⁋Example 5](/en/math/mirror_symmetry/overview#ex5){: data-lid="6xwdd" }. Moreover, this isomorphism is now parametrized by the variation of $q=e^{t^1}$, upgrading the previous mirror symmetry at the level of ring isomorphisms.
:::

Thus a Frobenius manifold provides the stage on which the ring structure of quantum cohomology can be treated consistently as a *function of the deformation parameter $t$*. From the next post onward we can now explore mirror symmetry in earnest.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
