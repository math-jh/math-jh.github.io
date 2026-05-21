---
title: "An Overview of Mirror Symmetry"
excerpt: "Historical background and the Hori-Vafa mirror"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/overview
sidebar: 
    nav: "mirror_symmetry-en"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Overview.png
    overlay_filter: 0.5

date: 2026-05-18
last_modified_at: 2026-05-18
weight: 1
translated_at: 2026-05-21T22:30:01+00:00
translation_source: kimi-cli
---
## Historical Background

Mirror symmetry is not a field that arose naturally within the mathematical framework, but rather is based on string theory. According to string theory, the world we live in starts from the single assumption that its fundamental degrees of freedom are not *point particles* but *one-dimensional strings*. Then the trajectory of a particle in spacetime as it moves along the time axis is no longer a $$1$$-dimensional worldline but a $$2$$-dimensional worldsheet, and its equation of motion is determined as a specific action-minimizing solution, just as in [\[Symplectic Geometry\] §Classical Mechanics, §§Principle of Least Action](/en/math/symplectic_geometry/classical_mechanics#최소작용의-원리). To reconcile this description with the framework of conventional quantum mechanics, spacetime is forced to be $$10$$-dimensional, so physicists consider this 10-dimensional spacetime as the product of $$4$$-dimensional Minkowski spacetime and a compact manifold $$M$$ accounting for the remaining $$6$$ dimensions. Writing down the physical conditions that this space $$X$$ must satisfy, we find that $$X$$ should be a *Calabi-Yau threefold*.

Meanwhile, 10-dimensional superstring theory is divided into five types according to the choice of boundary conditions and quantum conditions that the worldsheet must satisfy. Among these, the direct stage for mirror symmetry is Type IIA and Type IIB superstring theory, which are, as their names suggest, closely related to each other. Type IIA string theory gives a Kähler structure and a complex structure on a Calabi-Yau threefold $$X$$, while in Type IIB string theory these two structures are interchanged, defining a new Calabi-Yau threefold $$\check{X}$$. 

Therefore, if two different Calabi-Yau threefolds $$X$$ and $$\check{X}$$ appear as Type IIA/IIB manifestations of a single theory, they will yield a relationship between the Kähler structure of $$X$$ and the complex structure of $$\check{X}$$. We call such a pair $$(X, \check{X})$$ a *mirror pair*, and the symmetry between them *mirror symmetry*.

This relationship was backed almost entirely by the intuition of physicists and had not been formulated in mathematical language, so initially it was not a very interesting problem for mathematicians other than mathematical physicists. The situation changed at a mirror symmetry workshop held at MSRI in May 1991, where Candelas, de la Ossa, Green, and Parkes carried out the computation of the number of degree $$d$$ rational curves on a quintic Calabi-Yau threefold by translating it into a calculation on $$\check{X}$$ via the mirror symmetry assumption. There is an interesting anecdote here: at first, the values predicted by algebraic geometers through intersection theory differed from those predicted by physicists through this method. Subsequently, a bug was found in the code of the algebraic geometers, and after fixing it and recalculating, the physicists' computation turned out to be correct, causing mirror symmetry to emerge as a core research area in mathematics as well.

However, since the intuition of physicists fundamentally came from results in quantum mechanics, it was impossible to formalize this mathematically, and bringing it into mathematics required an appropriate formalism. The canonical framework that mathematicians generally accept is the Givental formalism, which roughly speaking packages the A-model invariants, the Gromov-Witten invariants, into data called the $$J$$-function, and similarly packages the B-model invariant, the oscillating integral, into the $$I$$-function; these are then equal under an appropriate change of variables.

In the posts in this category, we will explain these A-model and B-model separately and, based on this, explore topics in mirror symmetry. In the remainder of this post, as motivation for this, we will examine duality in toric varieties.

## Hori-Vafa Mirror Construction

In the case of toric varieties ([\[Toric Geometry\] §Definition of Toric Varieties, ⁋Definition 3](/en/math/toric_geometry/toric_varieties#def3)), mirror symmetry takes a very concrete form, so before beginning the full story we will examine how mirror symmetry works in this setting.

Let $$\Sigma$$ be the fan of a smooth projective toric variety $$X=X_\Sigma$$, and let $$v_1, \ldots, v_N \in N \cong \mathbb{Z}^n$$ be the primitive generators of its one-dimensional cones. If $$\Sigma$$ is a complete fan, the $$v_i$$ span $$N_\mathbb{R}$$. However, since $$N>n$$, they are $$\mathbb{Z}$$-linearly dependent, and therefore there exist $$r=N-n$$ integral equations among them.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The *charge matrix* of $$X_\Sigma$$ is the integer matrix

$$Q = (Q_{ji}) \in \Mat_{r \times N}(\mathbb{Z})$$

consisting of the coefficients of the integral relations

$$\sum_{i=1}^N Q_{ji}\, v_i = 0,\qquad j = 1, \ldots, r$$

among the above rays.

</div>

Although the charge matrix is simply the matrix collecting the coefficients of the ray relations, if we write $$X_\Sigma$$ via the Cox construction as the GIT quotient

$$X_\Sigma \;=\; \big(\mathbb{C}^N \setminus Z\big) \,\big/\!/\, (\mathbb{C}^\ast)^r$$

then the $$j$$-th $$(\mathbb{C}^\ast)$$ factor acts on the Cox ring variables $$\x_i$$ with weight $$Q_{ji}$$, and these become the important numbers determining the geometry of the toric variety.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> Write the rays of $$\mathbb{P}^n$$ as

$$v_0=-e_1-\cdots-e_n,\quad v_i=e_i\qquad (i=1,\ldots, n).$$

There is a unique relation $$v_0 + v_1 + \cdots + v_n = 0$$ among them, and thus the charge matrix is given by the $$1\times(n+1)$$ matrix

$$Q = (1,\, 1,\, \ldots,\, 1) \in \Mat_{1 \times (n+1)}(\mathbb{Z}).$$

According to the above explanation, this encodes the information of the standard scaling action of the torus defined on $$\mathbb{P}^n$$,

$$t\cdot(\x_0,\ldots, \x_n)=(t \x_0, \ldots, t \x_n).$$

As a slightly nontrivial example, consider $$\mathbb{P}^1\times \mathbb{P}^1$$. Its rays are given by $$(\pm 1, 0)$$, $$(0, \pm 1)$$, and since the relations are $$(1,0)+(-1,0)=0$$ and $$(0,1)+(0,-1)=0$$, the charge matrix becomes

$$Q = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}.$$

This encodes the information that the torus acts by the standard scaling action on the first and second $$\mathbb{P}^1$$ factors, respectively.

</div>

From the perspective of mirror symmetry, the charge matrix encodes the data of the $$B$$-model. Something to be careful about is that the situation we are currently dealing with is more general than the Calabi-Yau manifold described in the introduction. In general, a smooth projective toric variety $$X_\Sigma$$ is given as a Fano variety rather than a Calabi-Yau, and in this case the mirror dual of $$X_\Sigma$$ is expressed not as a Calabi-Yau but as a *Landau-Ginzburg model*.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> A *Landau-Ginzburg model* is given by a pair $$(\check{X}, W)$$ of a complex manifold $$\check{X}$$ and a holomorphic function $$W : \check{X} \to \mathbb{C}$$ defined on it. In this case, $$W$$ is called the *superpotential*.

</div>

The purpose of this post is to examine this phenomenon through light computations before formally defining the concepts of mirror symmetry. Therefore, instead of explaining the data on both sides precisely, we replace this with brief ideas and intuition. First, from the $$B$$-model side, the charge matrix defines the *Jacobi ring* $$\Jac(W_q)$$, which can be viewed as the classical limit of the oscillating integral mentioned earlier. For a given Landau-Ginzburg model $$(\check{X}, W)$$, its Jacobi ring is given by

$$\Jac(W) = \frac{\mathcal{O}(\check{X})}{(\partial_1 W, \ldots, \partial_n W)}$$

by definition. Here, $$\x_1, \ldots, \x_n$$ are local coordinates on $$\check{X}$$, and $$\partial_i$$ are the partial derivatives with respect to them. Geometrically, $$\Jac(W)$$ is the coordinate ring of the *critical scheme* $$\Crit(W) = \{dW = 0\} \subset \check{X}$$ of $$W$$. Then the mirror symmetry statement is that the Jacobi ring of the Hori-Vafa mirror of [Definition 4](#def4) recovers the data of the original A-side model.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a smooth projective toric Fano variety $$X_\Sigma$$ and additional data $$q=(q_1,\ldots, q_r)\in \mathbb{C}^r$$, the *Hori-Vafa mirror* defined by this means the following Landau-Ginzburg model.

1. The *mirror domain* $$\check{X}$$ is the submanifold of the algebraic torus $$(\mathbb{C}^\ast)^N$$ defined as the set of points satisfying the $$r$$ restrictions

    $$\x_1^{Q_{j1}} \cdots \x_N^{Q_{jN}} = q_j\in \mathbb{C}^\ast \qquad (j = 1, \ldots, r)$$

    given by the charge matrix $$Q$$.
2. The *superpotential* on $$\check{X}$$ is defined as the sum of the local coordinates

    $$W_q : \check{X} \to \mathbb{C}, \qquad W_q(\x_1, \ldots, \x_N) = \x_1 + \x_2 + \cdots + \x_N.$$

</div>

Here, $$q = (q_1, \ldots, q_r) \in (\mathbb{C}^\ast)^r$$ is the variable carrying the complex structure of the mirror LG model. The complex structure of the mirror domain $$\check{X}$$ itself is always the same affine torus $$(\mathbb{C}^\ast)^n$$, but the superpotential $$W_q$$ placed on it is determined by $$q$$. In other words, for each value of $$q$$ a unique LG model $$(\check{X}, W_q)$$ is determined, and it is more accurate to say that the entire family $$\{(\check{X}, W_q)\}_q$$ appears as the mirror of $$X_\Sigma$$. Here, the complex structure $$q$$ appears as the Novikov parameter $$q$$ in the A-model.

To write down the mirror symmetry statement, we must define the (small) *quantum cohomology* of $$X$$. Specifically, one of the tools needed when examining the symplectic and complex structures of $$X$$ is $$J$$-holomorphic curves. Using these, we can define the *quantum cup product* on the cohomology $$H^\ast(X, \mathbb{C})$$ of $$X$$ by the following formula

$$\alpha \star_q \beta \;=\; \alpha \smile \beta + \sum_{\beta_0} q^{\beta_0} \sum_\gamma \langle \alpha, \beta, \gamma^\vee \rangle_{0, 3, \beta_0}\, \gamma$$

and this structure gives the (small) *quantum cohomology* $$QH^\ast(X)$$ of $$X$$. Intuitively, in the above formula, if $$\alpha\smile \beta$$ contains information about the intersection of the two classes $$\alpha, \beta$$, then the remaining terms together account for the "quantum" intersections that do not actually occur but meet via the curve class $$\beta_0$$.

The mirror symmetry statement now asserts that

$$\Jac(W_q) \cong QH^\ast(X_\Sigma).$$

Let us verify that this actually holds in the two simple cases of $$\mathbb{P}^1$$ and $$\mathbb{P}^2$$.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 ($$\mathbb{P}^1$$ case)**</ins> We verified in [Example 2](#ex2) that the charge matrix of $$\mathbb{P}^1$$ is $$Q = (1, 1)$$. Therefore, the domain $$\check{X}$$ of the Hori-Vafa mirror is the submanifold of $$(\mathbb{C}^\ast)^2$$ satisfying the equation

$$\x_0 \x_1 = q.$$

On this, since $$\x_0 = q/\x_1$$, the superpotential can be written as

$$W_q(\x_1) = \x_1 + \frac{q}{\x_1}$$

and its critical points are the solutions of

$$\partial_{\x_1} W_q = 1 - \frac{q}{\x_1^2} = 0,$$

namely the two points $$\x_1 = \pm\sqrt{q}$$. From this, we can check that the Jacobi ring is given by

$$\Jac(W_q) = \mathbb{C}[\x_1^\pm, q^\pm] / (\partial_{\x_1} W_q) \;\cong\; \mathbb{C}[H, q^\pm]/(H^2 - q),\qquad H := \x_1.$$

Meanwhile, the small quantum cohomology on the A-side is simple: since there is only one $$\mathbb{P}^1$$ passing through three points, $$\langle H, H, H \rangle_{0,3,1}^{\mathbb{P}^1} = 1$$, and the classical cup product $$H\smile H$$ becomes $$0$$ for dimensional reasons. That is, the quantum cup product becomes $$H \star_q H = q$$, and from this the quantum cohomology becomes the graded $$\mathbb{C}[q]$$-polynomial algebra

$$QH^\ast(\mathbb{P}^1) = \mathbb{C}[H, q] \big/ (H^2 - q), \qquad \deg H = 2,\;\; \deg q = 4.$$

Now forgetting the grading and allowing $$q$$ to be invertible, we can check that it becomes exactly the same $$\mathbb{C}$$-algebra as the Jacobi ring above.

</div>

As a slightly more complicated example, let us look at $$\mathbb{P}^2$$.

<div class="example" markdown="1">

<ins id="ex6">**Example 6 ($$\mathbb{P}^2$$ case)**</ins> The mirror dual of $$\mathbb{P}^2$$ satisfies the equation

$$\x_0 \x_1 \x_2 = q$$

and the superpotential is given by

$$W_q(\z_1, \z_2) = \z_1 + \z_2 + \frac{q}{\z_1 \z_2}.$$

The critical points are obtained by solving

$$\partial_{\z_1} W_q = 1 - \frac{q}{\z_1^2 \z_2} = 0, \qquad \partial_{\z_2} W_q = 1 - \frac{q}{\z_1 \z_2^2} = 0,$$

and the solutions are given by the three points satisfying $$\z_1=\z_2$$, $$\z_1^3=q$$. Computing the Jacobi ring explicitly now gives

$$\Jac(W_q) = \mathbb{C}[\z_1^\pm, \z_2^\pm, q^\pm] \big/ (\partial_{\z_1} W_q, \partial_{\z_2} W_q) \;\cong\; \mathbb{C}[H, q^\pm]/(H^3 - q).$$

Meanwhile, to compute the quantum cohomology in the A-model, it suffices to use the following Gromov-Witten invariant

$$\langle H, H^2, H^2 \rangle_{0,3,1}^{\mathbb{P}^2} = 1.$$

Geometrically, this reflects the fact that (i) there is a unique $$\mathbb{P}^1 \subset \mathbb{P}^2$$ passing through two generic points $$P_1, P_2 \in \mathbb{P}^2$$, (ii) this line meets a generic line $$H_1 \subset \mathbb{P}^2$$ at exactly one point, and (iii) the three points thus obtained uniquely determine $$f : \mathbb{P}^1 \xrightarrow{\sim} L$$. Through this, we know that the quantum cohomology is determined as the graded $$\mathbb{C}[q]$$-polynomial algebra

$$QH^\ast(\mathbb{P}^2) = \mathbb{C}[H, q] \big/ (H^3 - q), \qquad \deg H = 2,\;\; \deg q = 6.$$

In this case as well, we can check that the isomorphism we expected works well.

</div>

More generally, the above two examples hold for an arbitrary smooth projective toric Fano variety. In the next post, we will examine the Batyrev mirror, which extends this to Calabi-Yau hypersurfaces inside toric varieties.

---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[HV]** K. Hori, C. Vafa, *Mirror symmetry*, arXiv:hep-th/0002222.
