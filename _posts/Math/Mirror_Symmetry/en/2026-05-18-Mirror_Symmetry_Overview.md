---
title: "Mirror Symmetry: An Overview"
description: "Mirror symmetry, originating from superstring theory, is a duality between Type IIA and Type IIB that exchanges the Kähler and complex structures of Calabi-Yau threefolds. It drew attention through the 1991 event in which a curve-counting problem that algebraic geometers could not solve was solved using physical methods."
excerpt: "Historical background and the Hori-Vafa mirror"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/overview
sidebar: 
    nav: "mirror_symmetry-en"

date: 2026-05-18
weight: 1
translated_at: 2026-08-19T19:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-21T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Historical Background

Mirror symmetry did not arise naturally from within mathematics itself; rather, it has superstring theory as its foundation. According to superstring theory, one starts from the single-line assumption that the fundamental degrees of freedom of the world we live in are not *point particles* but *1-dimensional strings*. Then, the trajectory in spacetime when a particle moves along the time axis is no longer a $1$-dimensional worldline but a $2$-dimensional worldsheet, and its equation of motion is determined by a specific action-minimizing solution, just as in [\[Symplectic Geometry\] §Classical Mechanics, §§Principle of Least Action](/en/math/symplectic_geometry/classical_mechanics#principle-of-least-action){: data-lid="c1tlf" }. In order to reconcile this interpretation with the existing framework of quantum mechanics, spacetime is forced to be $10$-dimensional, so physicists think of this 10-dimensional spacetime as the product of a $4$-dimensional Minkowski spacetime and, to resolve the remaining $6$ dimensions, a compact manifold $X$. Writing out the conditions that this space $X$ must satisfy physically, one finds that $X$ must be a *Calabi-Yau threefold*.

Meanwhile, 10-dimensional superstring theory splits into five types according to the choice of boundary conditions and quantum-mechanical conditions that the worldsheet must satisfy. Among these, the direct setting for mirror symmetry is Type IIA and Type IIB superstring theory, which, as their names suggest, are closely related to each other. Type IIA superstring theory gives a Kähler structure and a complex structure on a Calabi-Yau threefold $X$, while Type IIB superstring theory interchanges these two structures to define a new Calabi-Yau threefold $\check{X}$.

Therefore, if two distinct Calabi-Yau threefolds $X$ and $\check{X}$ arise as Type IIA/IIB of a single theory, they will give a relationship between the Kähler structure of $X$ and the complex structure of $\check{X}$. We call such a pair $(X, \check{X})$ a *mirror pair*, and the symmetry between them *mirror symmetry*.

This relationship was supported almost entirely by physicists' intuition and was not described in mathematical language, so in the beginning it was not a particularly interesting problem for mathematicians other than mathematical physicists. The situation changed at the mirror symmetry workshop held at MSRI in May 1991, where Candelas, de la Ossa, Green, and Parkes, through the mirror symmetry assumption, transferred the computation of the number of degree $d$ rational curves on a quintic Calabi-Yau threefold to a calculation on $\check{X}$ and carried it out. An interesting anecdote surrounds this: initially, the values predicted by existing algebraic geometers via intersection theory differed from the values predicted by physicists through this. Subsequently, a bug was found in the algebraic geometers' code, and after correcting it and recalculating, the physicists' computation turned out to be correct, leading mirror symmetry to emerge as a central research area in mathematics as well.

However, because physicists' intuition fundamentally came from results in quantum mechanics, it was impossible to formalize this mathematically, and an appropriate formalism was needed to bring this into mathematics. The standard framework universally accepted by mathematicians is the Givental formalism, which, briefly put, states that if one packages the Gromov-Witten invariants, the invariants of the A-model, into data called the $J$-function, and similarly packages the oscillating integrals, the invariants of the B-model, into the $I$-function, then they are equal to each other via an appropriate change of variables.

In the posts of this category, we will explain each of the A-model and B-model, and based on this, explore topics in mirror symmetry. In the remainder of this post, as motivation for this, we examine duality in toric varieties.

## Hori-Vafa Mirror Construction

In the case of toric varieties ([\[Toric Geometry\] §Definition of Toric Varieties, ⁋Definition 3](/en/math/toric_geometry/toric_varieties#def3){: data-lid="s27qv" }), mirror symmetry takes a very concrete form, so before starting the main discussion we examine how mirror symmetry works on them.

Let the fan of a smooth projective toric variety $X=X_\Sigma$ be $\Sigma$, and let the primitive generators of its 1-dimensional cones be $v_1, \ldots, v_m \in \mathbb{Z}^n$. If $\Sigma$ is a complete fan, then the $v_i$ span $\mathbb{R}^n$. However, since $m>n$, they are $\mathbb{Z}$-linearly dependent, and hence there exist $r=m-n$ integral equations among them.

::: Definition 1
The *charge matrix* of $X_\Sigma$ is the integer matrix formed from the coefficients of the integral relations among the rays above,

$$\sum_{i=1}^m Q_{ji} v_i = 0,\qquad j = 1, \ldots, r$$

namely,

$$Q = (Q_{ji}) \in \Mat_{r \times m}(\mathbb{Z})$$

Here, the rows of $Q$ are chosen to form a $\mathbb{Z}$-basis of the kernel (that is, the relation lattice) of the morphism $\mathbb{Z}^m \rightarrow \mathbb{Z}^n$ defined by the $v_i$; consequently, $Q$ is uniquely determined up to left multiplication by $\GL_r(\mathbb{Z})$.
:::

Although the charge matrix is simply a matrix collecting the coefficients of the ray relations, when we write $X_\Sigma$ via the Cox construction as a GIT quotient

$$X_\Sigma = \big(\mathbb{C}^m \setminus Z\big) \big// (\mathbb{C}^\ast)^r$$

the $j$-th $(\mathbb{C}^\ast)$ factor acts on the Cox ring variable $\x_i$ with weight $Q_{ji}$, and from this they become important numbers determining the geometry of the toric variety.

::: Example 2
Write the rays of $\mathbb{P}^n$ as

$$v_0=-e_1-\cdots-e_n,\quad v_i=e_i\qquad (i=1,\ldots, n)$$

Among these, there is a unique relation $v_0 + v_1 + \cdots + v_n = 0$, and therefore the charge matrix is given by the $1\times(n+1)$ matrix

$$Q = (1, 1, \ldots, 1) \in \Mat_{1 \times (n+1)}(\mathbb{Z}).$$

According to the explanation above, this encodes the information of the standard scaling action of the torus defined on $\mathbb{P}^n$,

$$t\cdot(\x_0,\ldots, \x_n)=(t \x_0, \ldots, t \x_n)$$

As a slightly nontrivial example, consider $\mathbb{P}^1\times \mathbb{P}^1$. Their rays are given by $(\pm 1, 0)$, $(0, \pm 1)$, and since there are two relations, $(1,0)+(-1,0)=0$ and $(0,1)+(0,-1)=0$, the charge matrix becomes

$$Q = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}$$

This encodes the information that the torus acts by the standard scaling action on each of the former factor and the latter factor $\mathbb{P}^1$.
:::

From the perspective of mirror symmetry, the charge matrix contains the data of the $B$-model. A point of caution is that the situation we are currently treating is more general than the Calabi-Yau manifolds described in the introduction. A smooth projective toric variety $X_\Sigma$ can never be Calabi-Yau, and in this post we treat the Fano case among them. In this case, the mirror dual of $X_\Sigma$ is represented not by a Calabi-Yau but by a *Landau-Ginzburg model*.

::: Definition 3
A *Landau-Ginzburg model* is given by a complex manifold $\check{X}$ and a holomorphic function $W : \check{X} \rightarrow \mathbb{C}$ defined on it, in the form of a pair $(\check{X}, W)$. Here, $W$ is called the *superpotential*.
:::

The purpose of this post is to examine this phenomenon through light computations before defining the concepts of mirror symmetry in earnest. Therefore, instead of explaining the data on both sides precisely, we substitute brief ideas and intuition. First, from the $B$-model side, the charge matrix defines the *Jacobi ring* $\Jac(W_q)$, which can be viewed as the classical limit of the oscillating integral mentioned above. For a given Landau-Ginzburg model $(\check{X}, W)$, its Jacobi ring is, by definition, given by

$$\Jac(W) = \frac{\mathcal{O}(\check{X})}{(\partial_1 W, \ldots, \partial_n W)}$$

Here, $\x_1, \ldots, \x_n$ are local coordinates on $\check{X}$ and $\partial_i$ are the partial derivatives with respect to these. Geometrically, $\Jac(W)$ is the coordinate ring of the *critical scheme* of $W$, $\Crit(W) = \{\dd{W} = 0\} \subseteq \check{X}$. Then the mirror symmetry statement is that the Jacobi ring of the Hori-Vafa mirror in [Definition 4](#def4){: data-lid="5bbc3" } recovers the data of the original A-side model.

::: Definition 4
For a smooth projective toric Fano variety $X_\Sigma$ and additional data $q=(q_1,\ldots, q_r)\in (\mathbb{C}^\ast)^r$, the *Hori-Vafa mirror* defined by them refers to the following Landau-Ginzburg model.

1. The *mirror domain* $\check{X}$ is the submanifold of the algebraic torus $(\mathbb{C}^\ast)^m$ defined by the points satisfying the $r$ restrictions imposed by the charge matrix $Q$,
    
    $$\x_1^{Q_{j1}} \cdots \x_m^{Q_{jm}} = q_j\in \mathbb{C}^\ast \qquad (j = 1, \ldots, r)$$

2. The *superpotential* on $\check{X}$ is defined as the sum of the local coordinates
    
    $$W_q : \check{X} \rightarrow \mathbb{C}, \qquad W_q(\x_1, \ldots, \x_m) = \x_1 + \x_2 + \cdots + \x_m$$

:::

Here $q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$ is the variable carrying the complex structure of the mirror LG model. The complex structure of the mirror domain $\check{X}$ itself is always the same affine torus $(\mathbb{C}^\ast)^n$, but the superpotential $W_q$ placed on it is determined by $q$. That is, for each value of $q$ a unique LG model $(\check{X}, W_q)$ is determined, and it is more accurate to say that the entire family $\{(\check{X}, W_q)\}_q$ appears as the mirror of $X_\Sigma$. At this time, the complex structure $q$ appears as the Novikov parameter $q$ in the A-model.

Earlier we explained mirror symmetry as a symmetry between complex structure and symplectic structure, and the Novikov parameter described above is precisely what carries the symplectic structure. Specifically, given a compact Kähler manifold $X$, we define its *Kähler form* $\omega\in H^2(X, \mathbb{R})$ as the symplectic form of $X$. Since this is a real form, making it somewhat cumbersome to consider a moduli space, we choose $B\in H^2(X, \mathbb{R})$ and form the *complexified Kähler class*

$$t = B + i\omega \in H^2(X, \mathbb{C})$$

Intuitively, this performs a complexification by filling out the Kähler form $\omega$ in the complex direction, and physically it represents the $B$-field appearing in superstring theory. Now the Novikov parameter is precisely the exponentiation of this $t$, which for a curve class $\beta_0 \in H_2(X)$ is given by

$$q^{\beta_0} = e^{2\pi i \int_{\beta_0} t} = e^{2\pi i \int_{\beta_0} B} e^{-2\pi \int_{\beta_0} \omega}$$

Then the magnitude $\lvert q^{\beta_0}\rvert = e^{-2\pi \int_{\beta_0} \omega}$ of $q^{\beta_0}$ carries the *symplectic volume* $\int_{\beta_0} \omega$ of the curve class $\beta_0$, and the phase $\arg q^{\beta_0} = 2\pi \int_{\beta_0} B$ carries the $B$-field. Therefore, in the regime where the symplectic volume goes to $0$, the magnitude of $q$ goes to $1$ so that quantum effects appear in full, whereas conversely, in the regime where the symplectic volume goes to infinity, the magnitude of $q$ goes to $0$ so that quantum effects disappear.

Now in the computation above, specifying a single $q$ is equivalent to determining the complexified Kähler class $t$, that is, specifying the $B$-field and $\omega$ respectively. Then from the formula above, $B$ has period $1$, and $\omega$ determines the radius in the direction set by $B$, so the moduli space of $q$ (or the moduli space of $t$) becomes the algebraic torus $(\mathbb{C}^\ast)^r$ with $r=\dim_\mathbb{R} H^2(X, \mathbb{R})$. However, since $\omega$ is a Kähler form, it must lie inside the *Kähler cone* (for an effective curve class $\beta_0$, $\int_{\beta_0} \omega > 0$, hence $\lvert q^{\beta_0}\rvert < 1$), so strictly speaking the moduli space is not this entire torus, but an open region near the large volume limit $q = 0$, and $(\mathbb{C}^\ast)^r$ is the ambient algebraic torus containing it.

On the B-side, as seen above, $q$ appeared as the coefficient of the superpotential. Intuitively, considering the case where the equation for the critical points obtained from this is of the form $\x^k=q$, the solutions of $\x^k=q$ (that is, the critical points) degenerate to a single point as $q$ goes to $0$, while in the remaining cases one obtains appropriately separated singularities.

Now, in order to state the mirror symmetry statement properly, we need to define the (small) *quantum cohomology* of $X$. Specifically, one of the tools needed when examining the symplectic structure and complex structure of $X$ is $J$-holomorphic curves. Using these, on the cohomology $H^\ast(X, \mathbb{C})$ of $X$, one can define the *quantum cup product* by the formula

$$\alpha \star_q \beta = \alpha \smile \beta + \sum_{\beta_0 \neq 0} q^{\beta_0} \sum_\gamma \langle \alpha, \beta, \gamma^\vee \rangle_{0, 3, \beta_0} \gamma$$

and this structure gives the (small) *quantum cohomology* $QH^\ast(X)$ of $X$. Intuitively, while $\alpha\smile \beta$ in the formula above carries information about the intersection of the two classes $\alpha, \beta$, the terms that follow take into account the "quantum" intersections that do not actually occur, but meet mediated by the curve class $\beta_0$.

Now the mirror symmetry statement asserts that

$$\Jac(W_q) \cong QH^\ast(X_\Sigma)$$

This statement matches the picture we already knew in several respects; for example, in the *classical limit* where $q\rightarrow 0$, the quantum cohomology ring returns to the classical cohomology ring, which when viewed from $\Jac(W_q)$ is equivalent to the singularities clumping together and degenerating to form a non-reduced singularity. Or, stated conversely, introducing quantum effects can be thought of, respectively, on the A-side as unfolding the classical cohomology using the Novikov variable $q$, and on the B-side as smoothing out the clumped singularities.

In general, examining $QH^\ast(X_\Sigma)$ on the right-hand side of the above isomorphism amounts to counting curves passing through given classes simultaneously, which is regarded as a relatively complex and difficult task, but mirror symmetry reduces this to a simple ring computation. Let us verify that this actually holds in the two simple cases $\mathbb{P}^1$ and $\mathbb{P}^2$.

::: Example 5 ($\mathbb{P}^1$ case)
In [Example 2](#ex2){: data-lid="m391m" }, we checked that the charge matrix of $\mathbb{P}^1$ is $Q = (1, 1)$. Therefore, the domain $\check{X}$ of the Hori-Vafa mirror is the submanifold of $(\mathbb{C}^\ast)^2$ satisfying the equation

$$\x_0 \x_1 = q$$

On this, since $\x_0 = q/\x_1$, the superpotential can be written as

$$W_q(\x_1) = \x_1 + \frac{q}{\x_1}$$

and its critical points are the solutions of

$$\partial_{\x_1} W_q = 1 - \frac{q}{\x_1^2} = 0$$

namely the two points $\x_1 = \pm\sqrt{q}$. From this, one can check that the Jacobi ring is given by

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, q^\pm] / (\partial_{\x_1} W_q) \cong \mathbb{C}[H, q^\pm]/(H^2 - q),\qquad H := \x_1$$

Meanwhile, the small quantum cohomology on the A-side is simple: since there is only a single $\mathbb{P}^1$ passing through three points, we have $\langle H, H, H \rangle_{0,3,1}^{\mathbb{P}^1} = 1$, and the classical cup product $H\smile H$ is $0$ for dimensional reasons. That is, the quantum cup product becomes $H \star_q H = q$, and from this the quantum cohomology becomes the graded $\mathbb{C}[q]$-polynomial algebra

$$QH^\ast(\mathbb{P}^1) = \mathbb{C}[H, q] \big/ (H^2 - q), \qquad \deg H = 2, \quad \deg q = 4$$

Now, forgetting the grading and treating $q$ as invertible, one can check that this becomes exactly the same $\mathbb{C}$-algebra as the Jacobi ring above.
:::

As a slightly more complicated example, let us look at $\mathbb{P}^2$.

::: Example 6 ($\mathbb{P}^2$ case)
The mirror dual of $\mathbb{P}^2$ satisfies the equation

$$\x_0 \x_1 \x_2 = q$$

and the superpotential is given by

$$W_q(\x_1, \x_2) = \x_1 + \x_2 + \frac{q}{\x_1 \x_2}$$

Now, the critical points are obtained by solving

$$\partial_{\x_1} W_q = 1 - \frac{q}{\x_1^2 \x_2} = 0, \qquad \partial_{\x_2} W_q = 1 - \frac{q}{\x_1 \x_2^2} = 0$$

and their solutions are given by the three points satisfying $\x_1=\x_2$, $\x_1^3=q$. Now computing the Jacobi ring explicitly gives

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, \x_2^\pm, q^\pm] \big/ (\partial_{\x_1} W_q, \partial_{\x_2} W_q) \cong \mathbb{C}[H, q^\pm]/(H^3 - q)$$

Meanwhile, to compute the quantum cohomology in the A-model, one can use the following Gromov-Witten invariant:

$$\langle H, H^2, H^2 \rangle_{0,3,1}^{\mathbb{P}^2} = 1$$

Geometrically, this reflects the fact that (i) there exists a unique line $L \cong \mathbb{P}^1 \subseteq \mathbb{P}^2$ passing through two generic points $P_1, P_2 \in \mathbb{P}^2$, (ii) this line meets a generic line $H_1 \subseteq \mathbb{P}^2$ at exactly one point, and (iii) the three points obtained through this uniquely determine $f : \mathbb{P}^1 \xrightarrow{\sim} L$. Through this, we know that the quantum cohomology is determined as the graded $\mathbb{C}[q]$-polynomial algebra

$$QH^\ast(\mathbb{P}^2) = \mathbb{C}[H, q] \big/ (H^3 - q), \qquad \deg H = 2, \quad \deg q = 6$$

In this case as well, one can check that our expected isomorphism works well.
:::

More generally, the two examples above hold for an arbitrary smooth projective toric Fano variety. In the next post, we will examine the Batyrev mirror, which extends this to Calabi-Yau hypersurfaces inside toric varieties.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
