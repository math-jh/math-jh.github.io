---
title: "Dubrovin Connection"
description: "We define the Dubrovin connection, which unifies the Levi-Civita connection and quantum product of a Frobenius manifold into a flat pencil of connections, and examine its flatness and significance in topological quantum field theory."
excerpt: "A flat connection on a Frobenius manifold with a spectral parameter"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/dubrovin_connection
sidebar: 
    nav: "mirror_symmetry-en"

date: 2026-05-21
weight: 4
translated_at: 2026-06-01T13:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-22T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post we examined how quantum cohomology $QH^\ast(X)$ or the Jacobi ring $\Jac(W_q)$ carries a Frobenius algebra structure, and we embedded them into a Frobenius manifold structure in order to capture the naturality of these isomorphisms in the $q$-parameter direction. The data defined on a Frobenius manifold $M$ consisted of the following data:

- the metric $\eta$ (in $QH^\ast(X)$, the Poincaré pairing) and the Levi-Civita connection arising from it,
- the product $\circ$ of the Frobenius algebra (in $QH^\ast(X)$, the quantum cup product),
- the Euler vector field $E$ (degree information)

and we verified that the associativity of $\circ$ is expressed by the WDVV equation. ([§Frobenius Manifolds, ⁋Proposition 7](/en/math/mirror_symmetry/frobenius_manifold#prop7){: data-lid="7yny0" }) The Dubrovin connection, which we treat in this post, goes further: it reveals that $\eta$ and $\circ$, or more precisely $\nabla$ and $\circ$, are deeply related.

## Dubrovin Connection

According to Dubrovin, $\nabla$ and $\circ$ are linked by a flat connection $\nabla^z$ on $M\times \mathbb{C}^\ast$ called the *Dubrovin connection*; this connection recovers $\circ$ as $z\rightarrow 0$ and $\nabla$ as $z\rightarrow\infty$. For this to make sense, we must justify to some extent what it means to treat $\circ$ as a connection.

In general, a connection is written in a local frame as $\nabla_{\partial_\alpha} = \partial_\alpha + A_\alpha$, where $A_\alpha$ is a connection $1$-form, an endomorphism on the fiber whose components are the connection coefficients of [\[Riemannian Geometry\] §Connection, ⁋Definition 3](/en/math/riemannian_geometry/connection#def3){: data-lid="livj4" }. The key observation is that for the product $\circ$, if we consider the endomorphism $\mathcal{C}_\alpha = \partial_\alpha \circ -$ of "multiplication by $\partial_\alpha$" in each direction $\partial_\alpha$, its matrix entries are precisely the structure constants $c_{\alpha\beta}^\gamma$ of the product. In other words, strictly speaking $\circ$ itself is not a connection; rather, its structure constants play the role of Christoffel symbols. ([\[Riemannian Geometry\] §Levi-Civita Connection, ⁋Proposition 6](/en/math/riemannian_geometry/Levi-Civita_connection#prop6){: data-lid="0dhqm" })

Indeed, choosing (flat) coordinates $\{ t^\alpha \}$, we immediately verify that

$$\mathcal{C}_\alpha(\partial_\beta) = \partial_\alpha \circ \partial_\beta = \sum_\gamma c_{\alpha\beta}^\gamma \partial_\gamma$$

Thus, considering the connection

$$\nabla^z_{\partial_\alpha} = \partial_\alpha + \frac{1}{z} \mathcal{C}_\alpha$$

connecting the two, we can package them into a single family that converges to the Levi-Civita connection $\nabla$ as $z \rightarrow \infty$ and diverges to multiplication by $\circ$ as $z \rightarrow 0$; in practice, when performing calculations with $z\rightarrow 0$, one can rescale this to extract the leading term of $z\nabla^z_{\partial_\alpha} = z\partial_\alpha + \mathcal{C}_\alpha$ as $z \rightarrow 0$. In any case, in this sense $\nabla^z$ is a *flat pencil of connections* joining the two structures, and physically this is interpreted as the string coupling constant.

::: Definition 1
Consider a Frobenius manifold $M$ and an auxiliary complex parameter $z \in \mathbb{C}^\ast$. Then the *Dubrovin connection* $\nabla^z$ is the connection defined on the pullback bundle $\pr_1^\ast TM$ via the projection

$$\pr_1: M\times \mathbb{C}^\ast \rightarrow M$$

given, with respect to flat coordinates on $M$, $\{ t^\alpha \}$, by the formula

$$\nabla^z_{\partial_\alpha} = \partial_\alpha + \frac{1}{z} \mathcal{C}_\alpha, \qquad \mathcal{C}_\alpha(X) := \partial_\alpha \circ X$$

Here $\mathcal{C}_\alpha$ is the endomorphism $\partial_\alpha\circ-$ defined above. The connection component in the remaining $z$ direction is given by the formula

$$\nabla^z_{\partial_z} = \partial_z - \frac{1}{z^2}E\circ(-) + \frac{1}{z}\mu$$

Here $E$ is the Euler vector field of [§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5){: data-lid="cgb1z" }, and $\mu$ is the *grading operator*, defined, for the flat coordinate $t^\alpha$ and the corresponding cohomology class $\sigma^\alpha$, from the half-degree $d_\alpha = (\deg\sigma^\alpha)/2$ and the conformal dimension $d$ by $\mu(\partial_\alpha) = (d_\alpha - d/2) \partial_\alpha$.
:::

Recall that earlier, when defining a Frobenius manifold in [§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5){: data-lid="klvpt" }, we introduced $E$ to encode the grading structure of the Frobenius algebra at each point. Specifically,

$$\mathcal{L}_E(\circ)=\circ,\qquad \mathcal{L}_E(\eta)=(2-d)\eta$$

reflected the fact that the quantum product respects degree and that the Poincaré pairing is concentrated in top degree, respectively. In particular, in the case of [§Frobenius Manifolds, ⁋Proposition 9](/en/math/mirror_symmetry/frobenius_manifold#prop9){: data-lid="dipji" }, which is our object of interest, if the Euler vector field $E$ in the formula above is the grading generating the rescaling of coordinates on the base $M$, then $\mu$ views the same grading as an endomorphism on the fiber $T_tM \cong H^\ast(X)$, and the two are related by

$$\mu = \frac{2-d}{2}I - \nabla E$$

Here $I$ is the identity matrix on $H^\ast(X)$. To see this more intuitively, writing it out directly in flat coordinates for $\nabla$, $E$ is

$$E = \sum_\alpha (1-d_\alpha)t^\alpha \partial_\alpha + \text{(constant terms)}$$

so we know that $\nabla E$ has the eigenvector $\partial_\alpha$ with corresponding eigenvalue $1-d_\alpha$. Now, substituting this into $\mu = \frac{2-d}{2}I - \nabla E$,

$$\mu(\partial_\alpha) = \left(\frac{2-d}{2} - (1-d_\alpha)\right)\partial_\alpha = (d_\alpha - d/2)\partial_\alpha$$

so $\mu$ also has the eigenvalue $d_\alpha-d/2$. Here, the shift by $\frac{2-d}{2}$ is to make $\mu$ skew-symmetric with respect to $\eta$, which arises from the fact that $\eta$ pairs a class of degree $d_\alpha$ with one of degree $d - d_\alpha$.

The most important property of the Dubrovin connection is that it is flat for all $z$. To verify this, let us compute the curvature $[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}]$. In flat coordinates, $\nabla^z_{\partial_\alpha} = \partial_\alpha + z^{-1}\mathcal{C}_\alpha$, and since $[\partial_\alpha, \partial_\beta] = 0$ and by the Leibniz rule $[\partial_\alpha, \mathcal{C}_\beta] = \partial_\alpha \mathcal{C}_\beta$ (the endomorphism obtained by differentiating the components of $\mathcal{C}_\beta$), it expands as

$$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}] = [\partial_\alpha + z^{-1}\mathcal{C}_\alpha,\ \partial_\beta + z^{-1}\mathcal{C}_\beta] = \frac{1}{z}(\partial_\alpha \mathcal{C}_\beta - \partial_\beta \mathcal{C}_\alpha) + \frac{1}{z^2}[\mathcal{C}_\alpha, \mathcal{C}_\beta]$$

For this curvature to vanish for all $z$, the coefficients of $z^{-1}$ and $z^{-2}$ must each vanish; the $z^{-1}$ term vanishes from the *potentiality* of $\mathcal{C}$, $\partial_\alpha\mathcal{C}_\beta = \partial_\beta\mathcal{C}_\alpha$, and the $z^{-2}$ term vanishes from the *associativity* of the product, $[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$.

Furthermore, the following proposition shows that the flatness of these connections is *exactly* equivalent to these two conditions. These were the axioms of a Frobenius manifold ([§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5){: data-lid="b2dwj" }), and therefore the flatness of $\nabla^z$ in the $M$-direction is not merely a consequence of adjusting moduli, but can be said to be the Frobenius structure itself.

::: Proposition 2
On a Frobenius manifold $M$, consider the connection $\nabla^z$ ([Definition 1](#def1){: data-lid="td83y" }). Under the assumption that the product $\circ$ is commutative, $\nabla^z$ being flat for every $z$ in the $M$-directions (i.e. among the $\partial_\alpha$ directions) is equivalent to the following two conditions both holding.

1. *Potentiality*: $\partial_\alpha c_{\beta\gamma}^\delta = \partial_\beta c_{\alpha\gamma}^\delta$. That is, $c_{\alpha\beta}^\delta$ is the third derivative of some potential $F$.
2. *Associativity (WDVV)*: $[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$, or in components $\sum_\delta c_{\alpha\beta}^\delta c_{\delta\gamma}^\epsilon = \sum_\delta c_{\beta\gamma}^\delta c_{\alpha\delta}^\epsilon$. That is, $\circ$ is associative.
:::

::: Proof
We have already shown one direction above, so we need only check the converse. Suppose $\nabla^z$ is flat for all $z \in \mathbb{C}^\ast$. The curvature

$$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}] = \frac{1}{z}(\partial_\alpha\mathcal{C}_\beta - \partial_\beta\mathcal{C}_\alpha) + \frac{1}{z^2}[\mathcal{C}_\alpha, \mathcal{C}_\beta]$$

is a Laurent polynomial in $z^{-1}$ and $z^{-2}$, so its vanishing for all $z$ is equivalent to the two coefficients vanishing separately. The vanishing of the $z^{-1}$ coefficient is exactly the first condition $\partial_\alpha\mathcal{C}_\beta = \partial_\beta\mathcal{C}_\alpha$, and writing the vanishing of the $z^{-2}$ coefficient, $[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$, in components gives $\sum_\delta (c_{\alpha\delta}^\epsilon c_{\beta\gamma}^\delta - c_{\beta\delta}^\epsilon c_{\alpha\gamma}^\delta) = 0$, which under the assumption that $\circ$ is commutative is exactly associativity, i.e. the WDVV equation. ([§Frobenius Manifolds, ⁋Proposition 7](/en/math/mirror_symmetry/frobenius_manifold#prop7){: data-lid="y6o0z" })
:::

On the other hand, flatness in the $z$-direction, $[\nabla^z_{\partial_z}, \nabla^z_{\partial_\alpha}] = 0$, requires the condition that the Euler vector field $E$ and the grading operator $\mu$ are compatible with the product, i.e. the homogeneity (or conformal) condition of the Frobenius manifold. Since this condition is already built into our definition as the fourth condition in [§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5){: data-lid="aseki" }, in our definition, including the $z$-direction, the full flatness of $\nabla^z$ is obtained.

## D-module

A connection $\nabla$ is essentially a tool for *differentiating* sections. When we view a vector bundle as an $\mathcal{O}_X$-module, the only operation we have is multiplication by functions, but once differentiation is also possible, that bundle becomes an object receiving the action of differential operators in addition to functions, namely a *$\mathcal{D}_X$-module*, and it must be flat for this definition to make sense.

::: Definition 3
On a complex manifold $B$, the sheaf of rings $\mathcal{D}_B$ of differential operators on $B$ is the sheaf of operators generated by the structure sheaf $\mathcal{O}_B$ and vector fields, that is, derivations on $\mathcal{O}_B$ ([\[Commutative Algebra\] §Differentials, ⁋Definition 1](/en/math/commutative_algebra/differentials#def1){: data-lid="gk2xq" }). Here, a vector field $\partial$ and a function $f$ satisfy the relation

$$[\partial, f] = \partial(f)$$

Now, an $\mathcal{O}_B$-module $\mathcal{M}$ equipped with a $\mathcal{D}_B$-action is called a *$\mathcal{D}_B$-module*.
:::

The $\mathcal{O}_B$-module structure on $\mathcal{M}$ is commonly thought of as multiplication by a function $f\in \mathcal{O}_B$. Then, for any section $s\in \mathcal{M}$, one can verify that the relation $[\partial, f]=\partial(f)$ satisfies the following Leibniz rule

$$\partial(f s) = (\partial f) s + f \partial s \qquad (f \in \mathcal{O}_B,\ s \in \mathcal{M})$$

As a concrete example, given a vector bundle $V\rightarrow B$ equipped with a flat connection $\nabla$, defining the action of a vector field $\partial$ to be $\nabla_\partial$ makes $V$ a $\mathcal{D}_B$-module; in this example, the flatness $[\nabla_\partial, \nabla_{\partial'}] = \nabla_{[\partial, \partial']}$ of $\nabla$ is precisely the commutator relation required by the definition of a $\mathcal{D}_B$-module.

In particular, since we have seen that the Dubrovin connection $\nabla^z$ is flat ([Proposition 2](#prop2){: data-lid="0jlyp" }), we can verify from this that $\pr_1^\ast TM$ becomes a $\mathcal{D}_{M\times \mathbb{C}^\ast}$-module. This is called the *quantum $D$-module*. Here, writing horizontal sections of the $\mathcal{D}$-module, that is, sections satisfying $\nabla^z s=0$, as $s=\sum_\alpha s^\alpha\partial_\alpha$ using flat coordinates, we obtain the differential equation

$$\partial_\alpha s^\beta + \frac{1}{z} \sum_\gamma c_{\alpha\gamma}^\beta s^\gamma = 0$$

which is called the *quantum differential equation*. Meanwhile, since the above equation is a first-order linear ODE, given a base point $b_0$ and an initial condition $s(b_0)$, the solution is uniquely determined along a path, and since $\nabla^z$ is flat, this parallel transport is independent of the path, giving a well-defined horizontal section in a simply connected neighborhood of $b_0$. Therefore, the solution space of the above QDE is $\dim_\mathbb{C} M$-dimensional, matching the rank of the bundle, and the $\pi_1$ of the base $M \times \mathbb{C}^\ast$ acts on this solution space via parallel transport, yielding a monodromy representation. In particular, a loop in the $z$-direction $\mathbb{C}^\ast$ ($\pi_1 \cong \mathbb{Z}$) gives the monodromy around the irregular singularity at $z = 0$ and the regular singularity at $z = \infty$, while a loop in the $q$-direction, arising after exponentiating the $H^2$ direction with the Novikov parameter $q = e^t$, gives the quantum monodromy.

A representative example of a Frobenius manifold was the case $M = H^\ast(X, \mathbb{C})$, which contains the deformations of quantum cohomology. ([§Frobenius Manifolds, ⁋Proposition 9](/en/math/mirror_symmetry/frobenius_manifold#prop9){: data-lid="gxlnt" }) Let us examine the Dubrovin connection in this case in detail. First, the base manifold is $M \times \mathbb{C}^\ast$, and a point of this manifold can be written as $(t,z)\in M\times \mathbb{C}^\ast$. By definition, the fiber over a point $(t,z)$ is $(\pr_1^\ast TM)_{(t,z)}\cong T_tM$, and since $M$ was originally a vector space, this fiber is canonically isomorphic to $H^\ast(X, \mathbb{C})$; endowing each of these with the big quantum product $\circ_t$ defined by $t$ is the Frobenius manifold structure. On this bundle, the Dubrovin connection is given by $\nabla^z_{\partial_\alpha} = \partial_\alpha + z^{-1}\mathcal{C}_\alpha$, where $\mathcal{C}_\alpha = \partial_\alpha \circ_t -$ is the endomorphism given by multiplication in the big quantum product. Taking the entire $M = H^\ast(X)$ as the base in this way gives the quantum $D$-module corresponding to big quantum cohomology. As we saw in the previous post, our primary interest lies in the deformation in the $H^2$ direction corresponding to small quantum cohomology among these; in particular, letting $\{T_a\}$ be a basis of $H^2(X)$, the connection constant in this direction is $\mathcal{C}_a=T_a\qtimes -$. Therefore, the QDE in this direction becomes

$$z q_a \partial_{q_a} s = -(T_a \qtimes s), \qquad a = 1, \ldots, r$$

and as examined above, the solution space of this equation is $\dim_\mathbb{C} H^\ast(X)$-dimensional. An explicit expression for the fundamental solution of this system is Givental's $J$-function, which contains the data of the A-side. As such, when the connection is the Dubrovin connection $\nabla^z$, its quantum $D$-module contains the A-model data of $X$, and so it is also called the *A-model $D$-module*.

Since from the manifold $M\times \mathbb{C}^\ast$ we have kept only the torus in the $H^2$ direction of $M$, the effective base on the A-side that we now treat is the $(r+1)$-dimensional algebraic torus

$$M_A := (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast_z = \Spec\mathbb{C}[q_1^{\pm}, \ldots, q_r^\pm, z^\pm]$$

The fiber over this $M_A$ is still the same as the fiber of $\pr_1^\ast TM$, namely $H^\ast(X)$, and therefore the bundle over it is given by the formula

$$H_A=H^\ast(X)\otimes_\mathbb{C}\mathbb{C}[q^\pm, z^\pm]=H^\ast(X, \mathbb{C}[z^\pm, q^\pm])$$

This is called the *A-model state space*.

Similarly, in the next post we show that the Jacobi rings $\Jac(W_q)$ defined by the mirror dual $\check{X}$ of $X$ can also be made into fibers defined over a suitable manifold $M_B$. Moreover, there exists a *Gauss-Manin connection* $\nabla^{GM}$ making this into a $\mathcal{D}$-module, and we will prove that the sections of this $D$-module constitute the B-model state space $H_B$. Then our mirror symmetry statement is elevated to the following claim.

::: misc Claim 4 (Mirror theorem, $D$-module form) {#conj4}
For a mirror pair $(X, \check{X})$, there exists a *mirror isomorphism* between the A-model state space $H_A$ and the B-model state space $H_B$ introduced above,

$$\Phi: H_A \xrightarrow{\sim} H_B$$

such that $\Phi$ makes the Dubrovin connection and the Gauss-Manin connection compatible:

$$\Phi \circ \nabla^z = \nabla^{GM} \circ \Phi$$
:::

A point of caution is that this claim is, strictly speaking, not a proven fact, but rather a philosophy. It has been proved separately for various mirror pairs; for example, the case of Calabi-Yau hypersurfaces in toric varieties, proved by Givental, was historically the first to be proved, which was later extended to toric Fano varieties, and subsequently extended to toric stacks by Coates-Corti-Iritani-Tseng. As a generalization in a slightly different direction, there is the path of moving to homogeneous spaces, in particular partial flag varieties $G/P$, instead of toric varieties. In this direction, LG superpotentials for Grassmannians and flag varieties were first constructed physically by Eguchi-Hori-Xiong, and studied Lie-theoretically by Rietsch; exploring this is one of the main purposes of this category.

Meanwhile, mirror symmetry takes various forms besides this $\mathcal{D}$-module isomorphism, among which a representative one is Kontsevich's *homological mirror symmetry*. This is a perspective that formulates a mirror pair as an equivalence of two derived categories $D^b\mathrm{Fuk}(X) \simeq D^b\Coh(\check{X})$, and has been proved for elliptic curves, abelian varieties, K3, Calabi-Yau hypersurfaces, etc. *SYZ mirror symmetry* is a form that geometrically realizes this with a mirror pair as the dual of a special Lagrangian torus fibration.


---

**References**

**[CK]** D. A. Cox, S. Katz, *Mirror Symmetry and Algebraic Geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.  
**[MS]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
