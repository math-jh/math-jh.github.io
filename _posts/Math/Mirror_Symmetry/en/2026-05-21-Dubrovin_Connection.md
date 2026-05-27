---
title: "Dubrovin Connection"
excerpt: "A flat connection on a Frobenius manifold with a spectral parameter"

categories: [Math / Mirror Symmetry]
permalink: /en/math/mirror_symmetry/dubrovin_connection
sidebar: 
    nav: "mirror_symmetry-en"

header:
    overlay_image: /assets/images/Math/Mirror_Symmetry/Dubrovin_Connection.png
    overlay_filter: 0.5

date: 2026-05-21
last_modified_at: 2026-05-21
weight: 4
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
In the previous post we saw that quantum cohomology $$QH^\ast(X)$$ and the Jacobi ring $$\Jac(W_q)$$ carry Frobenius algebra structures, and we embedded them into a Frobenius manifold structure in order to capture the naturality of their isomorphisms in the $$q$$-parameter direction. The data carried by a Frobenius manifold $$M$$ consists of the following:

- The metric $$\eta$$ (in $$QH^\ast(X)$$ this is the Poincaré pairing) and the Levi-Civita connection derived from it,
- The product $$\circ$$ of the Frobenius algebra (in $$QH^\ast(X)$$ this is the quantum cup product),
- The Euler vector field $$E$$ (encoding degree information)

and we verified that the associativity of $$\circ$$ is expressed by the WDVV equation. ([§Frobenius Manifolds, ⁋Proposition 7](/en/math/mirror_symmetry/frobenius_manifold#prop7)) The Dubrovin connection, which we treat in this post, goes a step further and shows that $$\eta$$ and $$\circ$$, or more precisely $$\nabla$$ and $$\circ$$, are deeply related to each other.

## Dubrovin Connection

According to Dubrovin, $$\nabla$$ and $$\circ$$ are linked by a flat connection $$\nabla^z$$ on $$M\times \mathbb{C}^\ast$$ called the *Dubrovin connection*; this connection recovers $$\circ$$ as $$z\rightarrow 0$$ and $$\nabla$$ as $$z\rightarrow\infty$$. In order for this to make sense, we must somewhat justify what it means to treat $$\circ$$ as a connection.

Generally, a connection is written in a local frame in the form $$\nabla_{\partial_\alpha} = \partial_\alpha + A_\alpha$$, where $$A_\alpha$$ is a connection $$1$$-form, i.e. an endomorphism on the fiber. ([\[Riemannian Geometry\] §Connections, ⁋Definition 3](/en/math/riemannian_geometry/connection#def3)) The key observation is that, for the product $$\circ$$, considering the endomorphism $$\mathcal{C}_\alpha = \partial_\alpha \circ -$$ of "multiplication by $$\partial_\alpha$$" in each direction $$\partial_\alpha$$, its matrix entries are precisely the structure constants $$c_{\alpha\beta}^\gamma$$ of the product. In other words, strictly speaking $$\circ$$ itself is not a connection; rather, its structure constants play the role of Christoffel symbols. ([\[Riemannian Geometry\] §Levi-Civita Connection, ⁋Proposition 6](/en/math/riemannian_geometry/Levi-Civita_connection#prop6))

Indeed, choosing (flat) coordinates $$\{ t^\alpha \}$$, we can immediately verify that

$$\mathcal{C}_\alpha(\partial_\beta) = \partial_\alpha \circ \partial_\beta = \sum_\gamma c_{\alpha\beta}^\gamma\, \partial_\gamma$$

Thus, considering the connection

$$\nabla^z_{\partial_\alpha} = \partial_\alpha + \frac{1}{z}\, \mathcal{C}_\alpha$$

that joins the two, we can organize them into a one-parameter family converging to the Levi-Civita connection $$\nabla$$ as $$z \to \infty$$ and diverging to the classical limit of the product $$\circ$$ as $$z \to 0$$, and when computing at $$z\rightarrow 0$$ one simply rescales to extract the leading term of $$z\nabla^z_{\partial_\alpha} = z\partial_\alpha + \mathcal{C}_\alpha$$ in the $$z \to 0$$ limit. In any case, in this sense $$\nabla^z$$ is a *flat pencil of connections* joining the two structures, and physically it is interpreted as the string coupling constant.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$M$$ be a Frobenius manifold and $$z \in \mathbb{C}^\ast$$ an auxiliary complex parameter. Then the *Dubrovin connection* $$\nabla^z$$ is the connection on the pullback bundle defined via the projection

$$\pr_1: M\times \mathbb{C}^\ast \rightarrow M$$

given for flat coordinates $$\{ t^\alpha \}$$ on $$M$$ by the formula

$$\nabla^z_{\partial_\alpha} = \partial_\alpha + \frac{1}{z}\, \mathcal{C}_\alpha, \qquad \mathcal{C}_\alpha(X) := \partial_\alpha \circ X$$

Here $$\mathcal{C}_\alpha$$ is the endomorphism $$\partial_\alpha\circ-$$ defined above. The remaining connection component in the $$z$$ direction is given by the formula

$$\nabla^z_{\partial_z} = \partial_z - \frac{1}{z^2}E\circ(-) + \frac{1}{z}\mu$$

Here $$E$$ is the Euler vector field ([§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5)), and $$\mu$$ is the *grading operator*, defined by $$\mu(\partial_\alpha) = (d_\alpha - d/2)\, \partial_\alpha$$ from the half-degree $$d_\alpha = \tfrac{1}{2}\deg\sigma^\alpha$$ of the cohomology class $$\sigma^\alpha$$ corresponding to the flat coordinate $$t^\alpha$$ and the conformal dimension $$d$$.

</div>

Recall that in [§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5), when defining a Frobenius manifold, we introduced $$E$$ in order to encode the grading structure of the Frobenius algebra at each point. Specifically,

$$\Lie_E(\circ)=\circ,\qquad \Lie_E(\eta)=(2-d)\eta$$

reflect the fact that the quantum product respects degree and that the Poincaré pairing is concentrated in top degree, respectively. In particular, in the case of [§Frobenius Manifolds, ⁋Proposition 9](/en/math/mirror_symmetry/frobenius_manifold#prop9), which is our main object of interest, if the Euler vector field $$E$$ in the above formula generates the grading by rescaling coordinates on the base $$M$$, then $$\mu$$ is the same grading viewed as an endomorphism on the fiber $$T_tM \cong H^\ast(X)$$, and they are related by

$$\mu = \frac{2-d}{2}I - \nabla E$$

Here $$I$$ is the identity matrix on $$H^\ast(X)$$. To see this more intuitively, writing it out directly in flat coordinates for $$\nabla$$, $$E$$ is

$$E = \sum_\alpha (1-d_\alpha)t^\alpha \partial_\alpha + \text{(constant terms)}$$

so we know that $$\nabla E$$ has eigenvalue $$1-d_\alpha$$ corresponding to the eigenvector $$\partial_\alpha$$. Substituting this into $$\mu = \frac{2-d}{2}I - \nabla E$$,

$$\mu(\partial_\alpha) = \frac{2-d}{2} - (1-d_\alpha) = d_\alpha - d/2$$

so $$\mu$$ also has eigenvalue $$d_\alpha-d/2$$. The shift by $$\frac{2-d}{2}$$ is to make $$\mu$$ skew-symmetric with respect to $$\eta$$, arising from the fact that $$\eta$$ pairs a class of degree $$d_\alpha$$ with one of degree $$d - d_\alpha$$.

The most important property of the Dubrovin connection is that it is flat for every $$z$$. To verify this, let us compute the curvature $$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}]$$. In flat coordinates $$\nabla^z_{\partial_\alpha} = \partial_\alpha + z^{-1}\mathcal{C}_\alpha$$, and $$[\partial_\alpha, \partial_\beta] = 0$$, while by the Leibniz rule $$[\partial_\alpha, \mathcal{C}_\beta] = \partial_\alpha \mathcal{C}_\beta$$ (the endomorphism obtained by differentiating the components of $$\mathcal{C}_\beta$$), so

$$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}] = [\partial_\alpha + z^{-1}\mathcal{C}_\alpha,\ \partial_\beta + z^{-1}\mathcal{C}_\beta] = \frac{1}{z}\,(\partial_\alpha \mathcal{C}_\beta - \partial_\beta \mathcal{C}_\alpha) + \frac{1}{z^2}\,[\mathcal{C}_\alpha, \mathcal{C}_\beta]$$

For this curvature to vanish for all $$z$$, the coefficients of $$z^{-1}$$ and $$z^{-2}$$ must each vanish; the $$z^{-1}$$ term vanishes by the *potentiality* of $$\mathcal{C}$$, namely $$\partial_\alpha\mathcal{C}_\beta = \partial_\beta\mathcal{C}_\alpha$$, and the $$z^{-2}$$ term vanishes by the *associativity* of the product, $$[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$$.

Moreover, the following proposition shows that the flatness of these connections is *exactly* equivalent to these two conditions. These were the axioms of a Frobenius manifold ([§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5)), and therefore the $$M$$-direction flatness of $$\nabla^z$$ is not merely a by-product of adjusting moduli, but can be said to be the Frobenius structure itself.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Consider the connection $$\nabla^z$$ on a Frobenius manifold $$M$$ ([Definition 1](#def1)). Under the assumption that the product $$\circ$$ is commutative, $$\nabla^z$$ being flat in the $$M$$-directions (i.e. among the $$\partial_\alpha$$ directions) for every $$z$$ is equivalent to the following two conditions both holding.

1. **Potentiality:** $$\partial_\alpha\, c_{\beta\gamma}^\delta = \partial_\beta\, c_{\alpha\gamma}^\delta$$. That is, $$c_{\alpha\beta}^\delta$$ is the third derivative of some potential $$F$$.
2. **Associativity (WDVV):** $$[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$$, or in components $$\sum_\delta c_{\alpha\beta}^\delta\, c_{\delta\gamma}^\epsilon = \sum_\delta c_{\beta\gamma}^\delta\, c_{\alpha\delta}^\epsilon$$. That is, $$\circ$$ is associative.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We have already shown one direction above, so we need only check the converse. Suppose $$\nabla^z$$ is flat for all $$z \in \mathbb{C}^\ast$$. The curvature

$$[\nabla^z_{\partial_\alpha}, \nabla^z_{\partial_\beta}] = \frac{1}{z}\,(\partial_\alpha\mathcal{C}_\beta - \partial_\beta\mathcal{C}_\alpha) + \frac{1}{z^2}\,[\mathcal{C}_\alpha, \mathcal{C}_\beta]$$

is a Laurent polynomial in $$z^{-1}$$ and $$z^{-2}$$, so its vanishing for all $$z$$ is equivalent to the two coefficients vanishing separately. The vanishing of the $$z^{-1}$$ coefficient is exactly the first condition $$\partial_\alpha\mathcal{C}_\beta = \partial_\beta\mathcal{C}_\alpha$$, and writing the vanishing of the $$z^{-2}$$ coefficient, $$[\mathcal{C}_\alpha, \mathcal{C}_\beta] = 0$$, in components gives $$\sum_\delta (c_{\alpha\delta}^\epsilon c_{\beta\gamma}^\delta - c_{\beta\delta}^\epsilon c_{\alpha\gamma}^\delta) = 0$$, which under the assumption that $$\circ$$ is commutative is exactly associativity, i.e. the WDVV equation. ([§Frobenius Manifolds, ⁋Proposition 7](/en/math/mirror_symmetry/frobenius_manifold#prop7))

</details>

On the other hand, flatness in the $$z$$-direction, $$[\nabla^z_{\partial_z}, \nabla^z_{\partial_\alpha}] = 0$$, requires the condition that the Euler vector field $$E$$ and the grading operator $$\mu$$ are compatible with the product, i.e. the homogeneity (or conformal) condition of the Frobenius manifold. Since this condition is already built into our definition as the fourth condition in [§Frobenius Manifolds, ⁋Definition 5](/en/math/mirror_symmetry/frobenius_manifold#def5), in our definition we obtain the full flatness of $$\nabla^z$$ including the $$z$$-direction.

## D-module

A connection $$\nabla$$ is essentially a tool for *differentiating* sections. When we view a vector bundle as an $$\mathcal{O}_X$$-module, the only operation we have is multiplication by functions, but once differentiation is available, that bundle becomes an object receiving the action of differential operators in addition to functions, namely a *$$\mathcal{D}_X$$-module*, and flatness is required for the definition to be meaningful.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> On a complex manifold $$B$$, the sheaf of rings $$\mathcal{D}_B$$ of differential operators on $$B$$ is the sheaf of operators generated by the structure sheaf $$\mathcal{O}_B$$ and vector fields, i.e. derivations on $$\mathcal{O}_B$$ ([\[Commutative Algebra\] §Differentials, ⁋Definition 1](/en/math/commutative_algebra/differentials#def1)). In this case, a vector field $$\partial$$ and a function $$f$$ satisfy the relation

$$[\partial, f] = \partial(f)$$

An $$\mathcal{O}_B$$-module $$\mathcal{M}$$ equipped with a $$\mathcal{D}_B$$-action is called a *$$\mathcal{D}_B$$-module*.

</div>

The $$\mathcal{O}_B$$-module structure on $$\mathcal{M}$$ is generally thought of as multiplication by a function $$f\in \mathcal{O}_B$$. Then for any section $$s\in \mathcal{M}$$, the relation $$[\partial, f]=\partial(f)$$ yields the Leibniz rule

$$\partial(f s) = (\partial f)\, s + f\, \partial s \qquad (f \in \mathcal{O}_B,\ s \in \mathcal{M})$$

as can be verified. As a concrete example, given a vector bundle $$E\rightarrow B$$ equipped with a flat connection $$\nabla$$, defining the action of a vector field $$\partial$$ to be $$\nabla_\partial$$ makes $$E$$ a $$\mathcal{D}_B$$-module, and in this example the flatness of $$\nabla$$, $$[\nabla_\partial, \nabla_{\partial'}] = \nabla_{[\partial, \partial']}$$, becomes exactly the commutator relation required by the definition of a $$\mathcal{D}_B$$-module.

In particular, since we have seen that the Dubrovin connection $$\nabla^z$$ is flat ([Proposition 2](#prop2)), we can verify from this that $$\pr_1^\ast TM$$ becomes a $$\mathcal{D}_{M\times \mathbb{C}^\ast}$$-module. This is called the *quantum $$D$$-module*. Here, writing the horizontal sections of the $$\mathcal{D}$$-module, i.e. functions satisfying $$\nabla^z s=0$$, as $$s=\sum_\alpha s^\alpha\partial_\alpha$$ using flat coordinates, we obtain the differential equation

$$\partial_\alpha s^\beta + \frac{1}{z} \sum_\gamma c_{\alpha\gamma}^\beta\, s^\gamma = 0$$

which is called the *quantum differential equation*. Since the above equation is a first order linear ODE, once a base point $$b_0$$ and initial condition $$s(b_0)$$ are given, the solution is uniquely determined along a path, and because $$\nabla^z$$ is flat, this parallel transport is independent of the path, giving a well-defined horizontal section in a simply connected neighborhood of $$b_0$$. Therefore the solution space of the above QDE is $$\dim_\mathbb{C} M$$-dimensional, matching the rank of the bundle, and the $$\pi_1$$ of the base $$M \times \mathbb{C}^\ast$$ acts on this solution space via parallel transport, yielding a monodromy representation. In particular, a loop in the $$z$$-direction ($$\pi_1 \cong \mathbb{Z}$$) gives monodromy around the irregular singularities at $$z = 0, \infty$$, and a loop in the $$q$$-direction of the Novikov parameter $$q = e^t$$ gives quantum monodromy.

A representative example of a Frobenius manifold is $$M = H^\ast(X, \mathbb{C})$$, which encodes deformations of quantum cohomology. ([§Frobenius Manifolds, ⁋Proposition 9](/en/math/mirror_symmetry/frobenius_manifold#prop9)) Let us examine the Dubrovin connection in this case in detail. First, the base manifold is $$M \times \mathbb{C}^\ast$$, and we can write a point of this manifold as $$(t,z)\in M\times \mathbb{C}^\ast$$. By definition, the fiber over a point $$(t,z)$$ is $$(\pr_1^\ast TM)_{(t,z)}\cong T_tM$$, and since $$M$$ was a vector space from the outset, this fiber is canonically isomorphic to $$H^\ast(X, \mathbb{C})$$, and the Frobenius manifold structure is given by endowing each of these with the big quantum product $$\circ_t$$ defined by $$t$$. On this bundle the Dubrovin connection is given by $$\nabla^z_{\partial_\alpha} = \partial_\alpha + z^{-1}\mathcal{C}_\alpha$$, where $$\mathcal{C}_\alpha = \partial_\alpha \circ_t -$$ is the endomorphism given by multiplication by the big quantum product. The quantum $$D$$-module corresponding to big quantum cohomology is what we obtain by taking the whole $$M = H^\ast(X)$$ as the base in this way. As we saw in the previous post, our primary object of interest is the deformation in the $$H^2$$ direction, which corresponds to small quantum cohomology among these, so in particular, letting $$\{T_\alpha\}$$ be a basis of $$H^2(X)$$, the connection constant in this direction is $$\mathcal{C}_a=T_a\qtimes -$$. Therefore the QDE in this direction is

$$z\, q_a \partial_{q_a} s = -\,(T_a \qtimes s), \qquad a = 1, \ldots, r$$

and as we examined above, the solution space of this equation is $$\dim_\mathbb{C} H^\ast(X)$$-dimensional. Givental's $$J$$-function, which gives the explicit fundamental solution of this system, carries the A-side data. Thus, when the connection is the Dubrovin connection $$\nabla^z$$, its quantum $$D$$-module carries the A-model data of $$X$$, and it is also called the *A-model $$D$$-module*.

Since from the manifold $$M\times \mathbb{C}^\ast$$ we have kept only the torus in the $$H^2$$ direction of $$M$$, the effective base on the A-side that we now treat is the $$(r+1)$$-dimensional algebraic torus

$$M_A := (\mathbb{C}^\ast)^r \times \mathbb{C}^\ast_z = \operatorname{Spec}\mathbb{C}[q_1^{\pm}, \ldots, q_r^\pm, z^\pm]$$

The fiber over this $$M_A$$ is still the same as the fiber of $$\pr_1^\ast TM$$, namely $$H^\ast(X)$$, and therefore the bundle over it is given by the formula

$$H_A=H^\ast(X)\otimes_\mathbb{C}\mathbb{C}[q^\pm, z^\pm]=H^\ast(X, \mathbb{C}[z^\pm, q^\pm])$$

This is called the *A-model state space*.

Similarly, in the next post we will show that the Jacobi rings $$\Jac(W_q)$$ defined by the mirror dual $$\check{X}$$ of $$X$$ can also be made into fibers over a suitable manifold $$M_B$$. Moreover, there exists a *Gauss-Manin connection* $$\nabla^{GM}$$ making this into a $$\mathcal{D}$$-module, and we will prove that the sections of this $$D$$-module constitute the B-model state space $$H_B$$. Then our mirror symmetry statement is elevated to the following claim.

<div class="proposition" markdown="1">

<ins id="conj4">**Conjecture 4 (Mirror theorem, $$D$$-module form)**</ins> For a mirror pair $$(X, \check{X})$$, there exists a *mirror isomorphism* between the A-model state space $$H_A$$ and the B-model state space $$H_B$$ introduced above, such that $$\Phi$$ is compatible with the Dubrovin connection and the Gauss-Manin connection:

$$\Phi \circ \nabla^z = \nabla^{GM} \circ \Phi$$

</div>

It is worth noting carefully that this conjecture is not, strictly speaking, a proven fact, but rather a guiding philosophy. It has been proved separately for various mirror pairs, for example the case of Calabi-Yau hypersurfaces in toric varieties, proved by Givental, was historically the first, after which it was extended to toric Fano varieties, and then further extended to toric stacks by Coates-Corti-Iritani-Tseng. A generalization in a slightly different direction replaces toric varieties by homogeneous spaces, in particular by partial flag varieties $$G/P$$. In this direction, the LG superpotentials for Grassmannians and flag varieties were first constructed physically by Eguchi-Hori-Xiong, and studied Lie-theoretically by Rietsch, and exploring this is one of the main aims of this series.

Meanwhile, mirror symmetry takes many forms besides this $$\mathcal{D}$$-module isomorphism, and one of the most representative is Kontsevich's *homological mirror symmetry*. This formulates a mirror pair as an equivalence of derived categories $$D^b\mathrm{Fuk}(X) \simeq D^b\Coh(\check{X})$$, and has been proved in the cases of elliptic curves, abelian varieties, K3 surfaces, Calabi-Yau hypersurfaces, etc., and *SYZ mirror symmetry* is the framework that geometrically realizes this by viewing a mirror pair as the dual of a special Lagrangian torus fibration.


---

**References**

**[Dub]** B. Dubrovin, *Geometry of $$2$$D topological field theories*, Integrable systems and quantum groups (Montecatini Terme, 1993), Lecture Notes in Math. **1620**, Springer, 1996, 120--348.  
**[Giv]** A. Givental, *Equivariant Gromov-Witten invariants*, Internat. Math. Res. Notices **1996**, no. 13, 613--663.  
**[Iri]** H. Iritani, *An integral structure in quantum cohomology and mirror symmetry for toric orbifolds*, Adv. Math. **222** (2009), no. 3, 1016--1079.  
**[EHX]** T. Eguchi, K. Hori, C.-S. Xiong, *Gravitational quantum cohomology*, Internat. J. Modern Phys. A **12** (1997), no. 9, 1743--1782.  
**[Rie]** K. Rietsch, *A mirror symmetric construction of $$qH^\ast_T(G/P)_{(q)}$$*, Adv. Math. **217** (2008), no. 6, 2401--2442.  
**[MR]** R. Marsh, K. Rietsch, *The B-model connection and mirror symmetry for Grassmannians*, Adv. Math. **366** (2020), 107027.  
**[LT]** T. Lam, N. Templier, *The mirror conjecture for minuscule flag varieties*, Duke Math. J. **173** (2024), no. 1, 75--175.  
**[CCIT]** T. Coates, A. Corti, H. Iritani, H.-H. Tseng, *A mirror theorem for toric stacks*, Compos. Math. **151** (2015), no. 10, 1878--1912.  
**[Kon]** M. Kontsevich, *Homological algebra of mirror symmetry*, Proc. Int. Congr. Math. (Zürich, 1994), vol. 1, Birkhäuser, 1995, 120--139.  
**[SYZ]** A. Strominger, S.-T. Yau, E. Zaslow, *Mirror symmetry is $$T$$-duality*, Nuclear Phys. B **479** (1996), no. 1--2, 243--259.  
**[CK]** D. A. Cox, S. Katz, *Mirror symmetry and algebraic geometry*, Mathematical Surveys and Monographs **68**, AMS, 1999.
