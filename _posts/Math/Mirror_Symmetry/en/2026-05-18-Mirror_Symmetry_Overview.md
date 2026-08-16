---
title: "Mirror Symmetry: An Overview"
description: "Mirror symmetry, originating from string theory, is a duality between Type IIA and Type IIB string theories that exchanges the Kähler and complex structures of Calabi–Yau threefolds. It first drew widespread attention in 1991 when physicists used it to solve a curve-counting problem that had stumped algebraic geometers."
excerpt: "Historical background and the Hori–Vafa mirror"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/overview
sidebar: 
    nav: "mirror_symmetry-en"

date: 2026-05-18
weight: 1
translated_at: 2026-08-16T06:48:07+00:00
translation_source: kimi-cli
---
## Historical Background

Mirror symmetry did not arise naturally within the mathematical framework itself; rather, it is rooted in superstring theory. According to superstring theory, our world is built on the single assumption that the fundamental degrees of freedom are not *point particles* but *one-dimensional strings*. Consequently, when a particle moves along the time axis, its trajectory in spacetime is no longer a $1$-dimensional worldline but a $2$-dimensional worldsheet, and its equation of motion is determined by a specific action-minimizing solution, just as in [[Symplectic Geometry] §Classical Mechanics, §§Principle of Least Action](/en/math/symplectic_geometry/classical_mechanics#principle-of-least-action). To reconcile this interpretation with the existing framework of quantum mechanics, spacetime is forced to be $10$-dimensional; thus physicists regard this $10$-dimensional spacetime as the product of a $4$-dimensional Minkowski spacetime and a compact manifold $X$ that resolves the remaining $6$ dimensions. Writing out the physical conditions that this space $X$ must satisfy, one finds that $X$ must be a *Calabi-Yau threefold*.

Meanwhile, $10$-dimensional superstring theory splits into five types according to the choice of boundary conditions and quantum-mechanical conditions that the worldsheet must satisfy. Among these, the direct stage for mirror symmetry is Type IIA and Type IIB superstring theory, which, as their names suggest, are closely related. Type IIA superstring theory endows a Calabi-Yau threefold $X$ with a Kähler structure and a complex structure, while Type IIB superstring theory interchanges these two structures and defines a new Calabi-Yau threefold $\check{X}$.

Therefore, if two different Calabi-Yau threefolds $X$ and $\check{X}$ appear as the Type IIA/IIB manifestations of a single theory, they should yield a relationship between the Kähler structure of $X$ and the complex structure of $\check{X}$. We call such a pair $(X, \check{X})$ a *mirror pair*, and the symmetry between them *mirror symmetry*.

This relationship was supported almost entirely by the intuition of physicists and had not been formulated in mathematical language, so in its early days it was not a particularly interesting problem for mathematicians other than mathematical physicists. The situation changed at the mirror symmetry workshop held at MSRI in May 1991, when Candelas, de la Ossa, Green, and Parkes used the mirror symmetry assumption to transfer the computation of the number of degree $d$ rational curves on a quintic Calabi-Yau threefold to a calculation on $\check{X}$. There is an interesting anecdote here: at first, the values predicted by algebraic geometers via intersection theory differed from those predicted by the physicists. Subsequently, a bug was found in the algebraic geometers' code, and after correcting it and recalculating, the physicists' computation turned out to be correct, causing mirror symmetry to emerge as a central research area in mathematics as well.

However, since the physicists' intuition fundamentally came from results in quantum mechanics, it was impossible to formalize this mathematically, and an appropriate formalism was needed to bring it into mathematics. The canonical framework universally accepted by mathematicians is the Givental formalism, which, briefly put, packages the Gromov-Witten invariants (the A-model invariants) into data called the $J$-function, and similarly packages the oscillating integrals (the B-model invariants) into the $I$-function; these are then equal to each other via an appropriate change of variables.

In the posts of this category we will explain these A-model and B-model respectively, and based on this we will explore topics in mirror symmetry. In the remainder of this post, as motivation for this, we examine duality in toric varieties.

## Hori-Vafa Mirror Construction

In the case of toric varieties ([[Toric Geometry] §Definition of Toric Varieties, ⁋Definition 3](/en/math/toric_geometry/toric_varieties#def3)), mirror symmetry takes a very concrete form, so before embarking on the full story we examine how mirror symmetry works in this setting.

Let the fan of a smooth projective toric variety $X=X_\Sigma$ be $\Sigma$, and let the primitive generators of its $1$-dimensional cones be $v_1, \ldots, v_m \in \mathbb{Z}^n$. If $\Sigma$ is a complete fan, then the $v_i$ span $\mathbb{R}^n$. However, since $m>n$, they are $\mathbb{Z}$-linearly dependent, and hence there exist $r=m-n$ integral equations among them.

::: Definition 1
The *charge matrix* of $X_\Sigma$ is the integer matrix formed from the coefficients of the integral relations

$$\sum_{i=1}^m Q_{ji} v_i = 0,\qquad j = 1, \ldots, r$$

among the rays above:

$$Q = (Q_{ji}) \in \Mat_{r \times m}(\mathbb{Z}).$$

Here the rows of $Q$ are chosen to form a $\mathbb{Z}$-basis of the kernel, i.e. the relation lattice, of the morphism $\mathbb{Z}^m \rightarrow \mathbb{Z}^n$ defined by the $v_i$; consequently $Q$ is uniquely determined up to left multiplication by $\GL_r(\mathbb{Z})$.
:::

Although the charge matrix is simply the matrix collecting the coefficients of the ray relations, when we write $X_\Sigma$ via the Cox construction as a GIT quotient

$$X_\Sigma = \big(\mathbb{C}^m \setminus Z\big) \big/\big/ (\mathbb{C}^\ast)^r,$$

the $j$-th $(\mathbb{C}^\ast)$ factor acts on the Cox ring variables $\x_i$ with weight $Q_{ji}$, and from this arise the important numbers determining the geometry of the toric variety.

::: Example 2
Write the rays of $\mathbb{P}^n$ as

$$v_0=-e_1-\cdots-e_n,\quad v_i=e_i\qquad (i=1,\ldots, n).$$

Among these there is a unique relation $v_0 + v_1 + \cdots + v_n = 0$, and hence the charge matrix is the $1\times(n+1)$ matrix

$$Q = (1, 1, \ldots, 1) \in \Mat_{1 \times (n+1)}(\mathbb{Z}).$$

According to the explanation above, this encodes the standard scaling action of the torus defined on $\mathbb{P}^n$,

$$t\cdot(\x_0,\ldots, \x_n)=(t \x_0, \ldots, t \x_n).$$

As a slightly nontrivial example, consider $\mathbb{P}^1\times \mathbb{P}^1$. Its rays are given by $(\pm 1, 0)$, $(0, \pm 1)$, and the relations are $(1,0)+(-1,0)=0$ and $(0,1)+(0,-1)=0$, two in total; hence the charge matrix becomes

$$Q = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}.$$

This encodes the information that the torus acts by the standard scaling action on each of the first and second $\mathbb{P}^1$ factors.
:::

From the perspective of mirror symmetry, the charge matrix carries the data of the $B$-model. Something to be careful about is that the situation we are currently dealing with is more general than the Calabi-Yau manifolds explained in the introduction. A smooth projective toric variety $X_\Sigma$ can never be Calabi-Yau, and in this post we treat among them the Fano case. In this case the mirror dual of $X_\Sigma$ is represented not by a Calabi-Yau but by a *Landau-Ginzburg model*.

::: Definition 3
A *Landau-Ginzburg model* is a pair $(\check{X}, W)$ consisting of a complex manifold $\check{X}$ and a holomorphic function $W : \check{X} \rightarrow \mathbb{C}$ defined on it. Here $W$ is called the *superpotential*.
:::

The purpose of this post is to examine this phenomenon through light computations before defining the concepts of mirror symmetry in earnest. Therefore, instead of explaining the data on both sides precisely, we replace this with brief ideas and intuition. First, from the $B$-model side, the charge matrix defines the *Jacobi ring* $\Jac(W_q)$, which can be viewed as the classical limit of the oscillating integral mentioned above. For a given Landau-Ginzburg model $(\check{X}, W)$, its Jacobi ring is given by definition as

$$\Jac(W) = \frac{\mathcal{O}(\check{X})}{(\partial_1 W, \ldots, \partial_n W)}.$$

Here $\x_1, \ldots, \x_n$ are local coordinates on $\check{X}$ and $\partial_i$ are the partial derivatives with respect to these. Geometrically $\Jac(W)$ is the coordinate ring of the *critical scheme* $\Crit(W) = \{\dd{W} = 0\} \subseteq \check{X}$ of $W$. Then the mirror symmetry statement is that the Jacobi ring of the Hori-Vafa mirror of [Definition 4](#def4) recovers the data of the original A-side model.

::: Definition 4
For a smooth projective toric Fano variety $X_\Sigma$ and additional data $q=(q_1,\ldots, q_r)\in (\mathbb{C}^\ast)^r$, the *Hori-Vafa mirror* defined by this means the following Landau-Ginzburg model.

1. The *mirror domain* $\check{X}$ is the submanifold of the algebraic torus $(\mathbb{C}^\ast)^m$ defined by the points satisfying the $r$ restrictions imposed by the charge matrix $Q$,
    
    $$\x_1^{Q_{j1}} \cdots \x_m^{Q_{jm}} = q_j\in \mathbb{C}^\ast \qquad (j = 1, \ldots, r).$$
    
2. The *superpotential* on $\check{X}$ is defined as the sum of local coordinates
    
    $$W_q : \check{X} \rightarrow \mathbb{C}, \qquad W_q(\x_1, \ldots, \x_m) = \x_1 + \x_2 + \cdots + \x_m.$$
    
:::

Here $q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$ is the variable carrying the complex structure of the mirror LG model. The complex structure of the mirror domain $\check{X}$ itself is always the same affine torus $(\mathbb{C}^\ast)^n$, but the superpotential $W_q$ placed on top of it is determined by $q$. That is, for each value of $q$ a unique LG model $(\check{X}, W_q)$ is determined, and it is more accurate to say that the entire family $\{(\check{X}, W_q)\}_q$ appears as the mirror of $X_\Sigma$. Here the complex structure $q$ appears as the Novikov parameter $q$ in the A-model.

We explained mirror symmetry earlier as a symmetry between complex structure and symplectic structure, and the Novikov parameter described above is precisely what carries the symplectic structure. Specifically, given a compact Kähler manifold $X$ we define its *Kähler form* $\omega\in H^2(X, \mathbb{R})$ as the symplectic form of $X$. Since this is a real form and it is somewhat cumbersome to consider a moduli space, we choose $B\in H^2(X, \mathbb{R})$ and form the *complexified Kähler class*

$$t = B + i\omega \in H^2(X, \mathbb{C}).$$

Intuitively this fills the Kähler form $\omega$ in the complex direction to perform a complexification, and physically it means the $B$-field appearing in superstring theory. Now the Novikov parameter is exactly the exponential of this $t$, given for a curve class $\beta_0 \in H_2(X)$ by

$$q^{\beta_0} = e^{2\pi i \int_{\beta_0} t} = e^{2\pi i \int_{\beta_0} B} e^{-2\pi \int_{\beta_0} \omega}.$$

Then the magnitude $\lvert q^{\beta_0}\rvert = e^{-2\pi \int_{\beta_0} \omega}$ of $q^{\beta_0}$ carries the *symplectic volume* $\int_{\beta_0} \omega$ of the curve class $\beta_0$, and the phase $\arg q^{\beta_0} = 2\pi \int_{\beta_0} B$ carries the $B$-field. Hence in the situation where the symplectic volume goes to $0$, the magnitude of $q$ goes to $1$ so that quantum effects appear in full, while conversely in the situation where the symplectic volume goes to infinity, the magnitude of $q$ goes to $0$ so that quantum effects disappear.

Now in the computation above, fixing a single $q$ is the same as determining the complexified Kähler class $t$, i.e. fixing the $B$-field and $\omega$ respectively. Then from the formula above $B$ has period $1$, and $\omega$ determines the radius in the direction fixed by $B$, so the moduli space of $q$ (or the moduli space of $t$) becomes the algebraic torus $(\mathbb{C}^\ast)^r$ with $r=\dim_\mathbb{R} H^2(X, \mathbb{R})$. However, since $\omega$ is a Kähler form it must lie inside the *Kähler cone* (for an effective curve class $\beta_0$ we have $\int_{\beta_0} \omega > 0$, i.e. $\lvert q^{\beta_0}\rvert < 1$), so strictly speaking the moduli is not the whole torus but an open region near the large volume limit where $q = 0$, and $(\mathbb{C}^\ast)^r$ is the ambient algebraic torus containing this.

On the B-side, $q$ appeared as the coefficient of the superpotential as we saw above. Thinking intuitively of the case where the critical point equation obtained from this is of the form $\x^k=q$, the solutions of $\x^k=q$, i.e. the critical points, degenerate to a single point as $q$ goes to $0$, and for the remaining cases one gets singularities that are appropriately separated.

To write the mirror symmetry statement well, we now need to define the (small) *quantum cohomology* of $X$. Specifically, among the tools needed to examine the symplectic structure and complex structure of $X$ are $J$-holomorphic curves. Using these, we can define the *quantum cup product* on the cohomology $H^\ast(X, \mathbb{C})$ of $X$ by the following formula

$$\alpha \star_q \beta = \alpha \smile \beta + \sum_{\beta_0 \neq 0} q^{\beta_0} \sum_\gamma \langle \alpha, \beta, \gamma^\vee \rangle_{0, 3, \beta_0} \gamma$$

and this structure gives the (small) *quantum cohomology* $QH^\ast(X)$ of $X$. Intuitively, if $\alpha\smile \beta$ in the formula above carries information about the intersection of the two classes $\alpha, \beta$, then the remaining terms together take into account the "quantum" intersections that do not actually occur but meet via the curve class $\beta_0$ as mediator.

Now the mirror symmetry statement claims that

$$\Jac(W_q) \cong QH^\ast(X_\Sigma).$$

This statement matches the picture we already knew in several respects; for example, in the *classical limit* where $q\rightarrow 0$, the quantum cohomology ring returns to the classical cohomology ring, which from the viewpoint of $\Jac(W_q)$ is the same as the singularities clumping together to produce a degenerate non-reduced singularity. Or, conversely, introducing quantum effects can be thought of on the A-side as resolving the classical cohomology using the Novikov variable $q$, and on the B-side as smoothing out the clumped singularities.

In general, examining the $QH^\ast(X_\Sigma)$ on the right-hand side of the above isomorphism amounts to counting curves passing through given classes simultaneously, which is regarded as a relatively complex and difficult task, but mirror symmetry reduces this to a simple ring computation. Let us verify that this actually holds in the two simple cases $\mathbb{P}^1$, $\mathbb{P}^2$.

::: Example 5 ($\mathbb{P}^1$ case)
In [Example 2](#ex2) we checked that the charge matrix of $\mathbb{P}^1$ is $Q = (1, 1)$. Hence the domain $\check{X}$ of the Hori-Vafa mirror is the submanifold of $(\mathbb{C}^\ast)^2$ satisfying the equation

$$\x_0 \x_1 = q.$$

On this we have $\x_0 = q/\x_1$, so the superpotential can be written as

$$W_q(\x_1) = \x_1 + \frac{q}{\x_1}$$

and its critical points are the solutions of

$$\partial_{\x_1} W_q = 1 - \frac{q}{\x_1^2} = 0,$$

namely the two points $\x_1 = \pm\sqrt{q}$. From this one can check that the Jacobi ring is given by

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, q^\pm] / (\partial_{\x_1} W_q) \cong \mathbb{C}[H, q^\pm]/(H^2 - q),\qquad H := \x_1.$$

Meanwhile the small quantum cohomology on the A-side is simple: since there is exactly one $\mathbb{P}^1$ passing through three points, we have $\langle H, H, H \rangle_{0,3,1}^{\mathbb{P}^1} = 1$, and the classical cup product $H\smile H$ is $0$ for dimensional reasons. Hence the quantum cup product becomes $H \star_q H = q$, and from this the quantum cohomology becomes the graded $\mathbb{C}[q]$-polynomial algebra

$$QH^\ast(\mathbb{P}^1) = \mathbb{C}[H, q] \big/ (H^2 - q), \qquad \deg H = 2,\quad \deg q = 4.$$

Now forgetting the grading and making $q$ invertible, one can check that this becomes exactly the same $\mathbb{C}$-algebra as the Jacobi ring above.
:::

As a slightly more complicated example, consider $\mathbb{P}^2$.

::: Example 6 ($\mathbb{P}^2$ case)
The mirror dual of $\mathbb{P}^2$ satisfies the equation

$$\x_0 \x_1 \x_2 = q$$

and the superpotential is given by

$$W_q(\x_1, \x_2) = \x_1 + \x_2 + \frac{q}{\x_1 \x_2}.$$

Now the critical points are obtained by solving

$$\partial_{\x_1} W_q = 1 - \frac{q}{\x_1^2 \x_2} = 0, \qquad \partial_{\x_2} W_q = 1 - \frac{q}{\x_1 \x_2^2} = 0,$$

and their solutions are given by the three points satisfying $\x_1=\x_2$, $\x_1^3=q$. Now computing the Jacobi ring explicitly gives

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, \x_2^\pm, q^\pm] \big/ (\partial_{\x_1} W_q, \partial_{\x_2} W_q) \cong \mathbb{C}[H, q^\pm]/(H^3 - q).$$

Meanwhile, to compute the quantum cohomology in the A-model it suffices to use the following Gromov-Witten invariant:

$$\langle H, H^2, H^2 \rangle_{0,3,1}^{\mathbb{P}^2} = 1.$$

Geometrically this reflects the facts that (i) there exists a unique line $L \cong \mathbb{P}^1 \subseteq \mathbb{P}^2$ passing through two generic points $P_1, P_2 \in \mathbb{P}^2$, (ii) this line meets a generic line $H_1 \subseteq \mathbb{P}^2$ at exactly one point, and (iii) the three points thus obtained uniquely determine $f : \mathbb{P}^1 \xrightarrow{\sim} L$. From this one knows that the quantum cohomology is determined as the graded $\mathbb{C}[q]$-polynomial algebra

$$QH^\ast(\mathbb{P}^2) = \mathbb{C}[H, q] \big/ (H^3 - q), \qquad \deg H = 2,\quad \deg q = 6.$$

In this case as well, one can check that the isomorphism we expected works well.
:::

More generally, the two examples above hold for an arbitrary smooth projective toric Fano variety. In the next post we will examine the Batyrev mirror, which extends this to Calabi-Yau hypersurfaces inside toric varieties.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
