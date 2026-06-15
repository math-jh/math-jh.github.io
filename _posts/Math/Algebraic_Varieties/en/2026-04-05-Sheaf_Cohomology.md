---
title: "Sheaf Cohomology"
description: "To capture the information of a sheaf more precisely beyond global sections of a line bundle, we define sheaf cohomology as a derived functor and explore its properties."
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/sheaf_cohomology
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-05
last_modified_at: 2026-04-20
weight: 12
translated_at: 2026-05-30T04:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-30T04:00:03+00:00
---
We have seen that line bundles can be used to construct various invariants. For example, in [§Line Bundles and Vector Bundles](/en/math/algebraic_varieties/line_bundles) we defined the global section space $$\Gamma(X, \mathcal{L})$$ of a line bundle $$\mathcal{L}$$. In particular, in [§Linear Systems, ⁋Definition 9](/en/math/algebraic_varieties/linear_systems#def9) we saw that the dimension of this space plays a key role in determining the dimension of the complete linear system, and hence the projective embedding of the variety.

We have mainly used the language of line bundles for geometric intuition, but as we observed right after [§Canonical Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1), passing to the section sheaf of a line bundle allows us to rephrase everything fundamentally in the language of sheaves. In this post we define the notion of sheaf cohomology.

## Definition as a Derived Functor

Although sheaves are a powerful tool for systematically describing all the information of a topological space, they have appeared front and center in our discussion only once before: in [§Linear Systems](/en/math/algebraic_varieties/linear_systems), when we saw that the global section space $$\Gamma(X, \mathcal{L})$$ determines the projective embedding of the complete linear system.

However, if global sections were our only concern, there would be no need to think about sheaves at all; we could simply have considered the global section functor. In fact, the global section functor does not capture all the information contained in a sheaf. For example, consider the global section functor

$$\Gamma(X, -): \QCoh(X) \to \Vect_\mathbb{K}; \qquad \mathcal{F} \mapsto \mathcal{F}(X).$$

Recall that when we defined quasi-coherent sheaves in [§Canonical Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1), our motivation was that the category $$\Bun(X)$$ of vector bundles is not an abelian category, so we wanted to consider a larger category where kernels and cokernels exist; from this perspective, it is not surprising that $$\QCoh(X)$$ is an abelian category. [^1]

If $$\Gamma(X,-)$$ lost no information whatsoever, this functor would have to be exact. That is, given a short exact sequence of (quasi-coherent) sheaves

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$

applying $$\Gamma(X,-)$$ should again yield a short exact sequence. However, this functor is only left exact. In other words, exactness of

$$0 \to \Gamma(X, \mathcal{F}') \to \Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'')$$

is guaranteed, but the surjection

$$\Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{F}'') \to 0$$

fails in general. For a concrete example, consider the Euler sequence

$$0 \to \Omega^1_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \to \mathcal{O}_{\mathbb{P}^n} \to 0$$

([§Canonical Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7)). Applying $$\Gamma(\mathbb{P}^n, -)$$ to this short exact sequence gives

$$0 \to \Gamma(\mathbb{P}^n, \Omega^1_{\mathbb{P}^n}) \to \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) \to \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}).$$

However, as we saw in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), the global sections of $$\mathcal{O}_{\mathbb{P}^n}(-1)$$ vanish, so

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) = 0,$$

while $$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})=\mathbb{K}$$; hence surjectivity on the right cannot hold.

The standard way to resolve this is to consider the right derived functor ([\[Homological Algebra\] §Derived Functors, ⁋Definition 9](/en/math/homological_algebra/derived_functors#def9)). Specifically, since $$\lMod{A}$$ has enough injectives, one can show that $$\QCoh(X)$$ also has enough injective objects; thus any quasi-coherent sheaf $$\mathcal{F}$$ admits an injective resolution $$\mathcal{I}^\bullet$$, and from the resulting complex

$$0 \to \Gamma(X, \mathcal{I}^0) \to \Gamma(X, \mathcal{I}^1) \to \Gamma(X, \mathcal{I}^2) \to \cdots$$

we can define sheaf cohomology as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a quasi-coherent sheaf $$\mathcal{F}$$ on a variety $$X$$, the $$i$$th *sheaf cohomology* $$H^i(X, \mathcal{F})$$ is defined by

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \to \Gamma(X, \mathcal{I}^{i+1}))}{\im(\Gamma(X, \mathcal{I}^{i-1}) \to \Gamma(X, \mathcal{I}^i))}$$

where $$\mathcal{I}^\bullet$$ is an injective resolution of $$\mathcal{F}$$.

</div>

More generally, one can show that $$\Sh(X)$$ also has enough injectives by choosing injective objects stalkwise and then sheafifying, but our main interest is always in quasi-coherent sheaves, so we restrict our attention to the category $$\QCoh(X)$$.

That this is independent of the choice of $$\mathcal{I}^\bullet$$, and so on, all follow from standard arguments in homological algebra.

Earlier, when we introduced the global section space $$\Gamma(X, \mathcal{L})$$, we mentioned that another common notation for this space is $$H^0(X, \mathcal{L})$$; we now see that this notation is justified by the definition above.

The following proposition is also a standard result that follows immediately from homological algebra ([\[Homological Algebra\] §Derived Functors, ⁋Proposition 8](/en/math/homological_algebra/derived_functors#prop8)).

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a short exact sequence of sheaves

$$0 \to \mathcal{F}' \to \mathcal{F} \to \mathcal{F}'' \to 0$$

there exists a long exact sequence

$$0 \to H^0(X, \mathcal{F}') \to H^0(X, \mathcal{F}) \to H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \to \cdots$$

where $$\delta$$ is the *connecting homomorphism*.

</div>

## Čech Cohomology

While [Definition 1](#def1) is a rigorous definition of sheaf cohomology, explicitly constructing an injective resolution is generally very difficult. Therefore, in actual computations we use the Čech approach, which defines cohomology from a different perspective.

Intuitively, Čech cohomology $$\check{H}^i(X, \mathcal{F})$$ is a tool that measures the failure of gluing local information. That is, $$\check{H}^0(X, \mathcal{F})$$ is exactly the global section space, and $$\check{H}^1(X, \mathcal{F})$$ tells us how much the process of gluing local sections together to obtain a global section fails. To define this rigorously, we begin with the following.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Given a topological space $$X$$, an open cover $$\mathcal{U} = \{U_i\}_{i \in I}$$, and a sheaf $$\mathcal{F}$$, fix an arbitrary total order $$<$$ on $$I$$. Then the *Čech complex* $$C^\bullet(\mathcal{U}, \mathcal{F})$$ of this data is defined as follows:

$$\check{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

Here, the *coboundary map* $$d: \check{C}^p \to \check{C}^{p+1}$$ is defined by the formula

$$(d\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0}\cap \cdots \cap U_{i_{p+1}}}$$

where $$\hat{i_k}$$ means omitting the index $$i_k$$.

</div>

As with sheaf cohomology, this definition makes sense for arbitrary sheaves, but we are mainly concerned with $$\QCoh(X)$$.

For this definition to be well-defined—that is, for $$\check{C}^\bullet(\mathcal{U}, \mathcal{F})$$ to actually be a complex—the coboundary map must satisfy $$d^2=0$$. This can be verified directly by expanding the above formula and checking the sign cancellations. Consequently, $$\check{C}^\bullet(\mathcal{U}, \mathcal{F})$$ is a cochain complex, and thus we can define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The *Čech cohomology* $$\check{H}^p(\mathcal{U}, \mathcal{F})$$ defined by the above data is the cohomology of the Čech complex:

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\check{C}^\bullet(\mathcal{U}, \mathcal{F})).$$

</div>

We said earlier that Čech cohomology measures the failure of gluing; this is encoded in the coboundary map. Let us verify the intuitive meaning of the coboundary map in low degrees $$p = 0, 1$$.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 ($$p = 0$$)**</ins> By the definition of the Čech complex, $$\check{C}^0(\mathcal{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$$, and the coboundary map from $$\check{C}^0$$ to $$\check{C}^1$$ is

$$(ds)_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}.$$

Therefore,

$$\check{H}^0(\mathcal{U}, \mathcal{F}) = \ker(d: \check{C}^0 \to \check{C}^1) = \left\{(s_i) \in \prod_i \mathcal{F}(U_i) \mid s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\right\}.$$

By the gluing condition for sheaves ([\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1)), such a family of sections coincides exactly with a section over all of $$X$$, that is, with $$\Gamma(X, \mathcal{F})$$. Thus $$\check{H}^0(\mathcal{U}, \mathcal{F}) = H^0(X, \mathcal{F})$$, and this is independent of the choice of open cover.

</div>

We will soon show that in favorable situations, Čech cohomology and sheaf cohomology always agree as above. For now, let us see how the case $$p=1$$ measures the failure of gluing.

<div class="example" markdown="1">

<ins id="ex6">**Example 6 ($$p = 1$$)**</ins> A 1-cochain is a collection of sections $$s_{ij} \in \mathcal{F}(U_i \cap U_j)$$ on each $$U_i \cap U_j$$, and a 1-cocycle is one satisfying the cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \qquad\text{on}\quad U_i \cap U_j \cap U_k.$$

On the other hand, a 1-coboundary is one induced from a 0-cochain $$(t_i)$$, that is, of the form $$s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$$.

Thus, a nontrivial element of $$\check{H}^1(\mathcal{U}, \mathcal{F})$$ reflects the discrepancy that appears when trying to glue these three pieces of data $$s_{ij}, s_{jk}, s_{ik}$$ together, and this is precisely the failure of gluing mentioned above.

</div>

So far we have defined Čech cohomology $$\check{H}^p(\mathcal{U}, \mathcal{F})$$ for a single open cover $$\mathcal{U}$$. However, different open covers can generally give different Čech cohomology groups. For example, for the cover consisting of a single open set $$U_0 = X$$, all intersections are $$X$$, so $$\check{H}^p$$ is nonzero only for $$p = 0$$. Since finer covers capture more topological information, we need to understand the relationships between open covers and synthesize the information from all of them. That is, we impose an ordering on *all* open covers using refinement. Then for a refinement $$\mathcal{V} \preceq \mathcal{U}$$, it is obvious that a natural map $$\check{H}^p(\mathcal{U}, \mathcal{F}) \to \check{H}^p(\mathcal{V}, \mathcal{F})$$ exists, and thus we can define a direct system $$\check{H}^p(\mathcal{U}, \mathcal{F})$$ indexed by all open covers. From this we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> The *Čech cohomology* of $$X$$ is defined as the direct limit over all open covers:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathcal{U}} \check{H}^p(\mathcal{U}, \mathcal{F}).$$

</div>

To put the above argument more simply: we take open covers that are progressively finer, combine all the additional cohomology data that appears, and define this as $$\check{H}(X, \mathcal{F})$$.

In general, it is not guaranteed that the $$\check{H}^p(X, \mathcal{F})$$ of [Definition 7](#def7) is isomorphic to the $$H^p(X, \mathcal{F})$$ of [Definition 1](#def1), but fortunately for most sheaves that appear in algebraic geometry, the two agree. Showing this requires some technical machinery.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a sheaf $$\mathcal{F}$$ on a variety $$X$$, we define the following:

1. $$\mathcal{F}$$ is *acyclic* if $$H^i(X, \mathcal{F}) = 0$$ for all $$i > 0$$.
2. An injective object $$\mathcal{F}$$ in $$\Sh(X)$$ is called an *injective sheaf*.
3. If the restriction map $$\mathcal{F}(U) \rightarrow \mathcal{F}(V)$$ is surjective for any open sets $$V\subset U$$, then $$\mathcal{F}$$ is called a *flasque sheaf*.

</div>

Of course, the condition we want at the cohomology level is the first one. Let us first examine the relationships among the concepts above.

<div class="proposition" markdown="1">

<ins id="lem9">**Lemma 9**</ins> An injective sheaf $$\mathcal{F}$$ is flasque.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, $$\mathcal{F}$$ being injective means that for any monomorphism $$\mathcal{A} \hookrightarrow \mathcal{B}$$, the map $$\Hom_{\Sh(X)}(\mathcal{B}, \mathcal{F}) \to \Hom_{\Sh(X)}(\mathcal{A}, \mathcal{F})$$ is surjective ([\[Homological Algebra\] §Resolutions, ⁋Definition 1](/en/math/homological_algebra/resolutions#def1)). We now show that for any open sets $$V \subset U \subset X$$, the restriction $$\mathcal{F}(U) \to \mathcal{F}(V)$$ is surjective.

This map is a morphism of abelian groups, not a sheaf morphism, and the tools we have are sheaf morphisms, so we need to rephrase this condition in terms of sheaf morphisms. To this end, we introduce the open embeddings

$$i^U: U \hookrightarrow X,\qquad i^V: V \hookrightarrow X$$

and the sheaves $$i^U_!\mathbb{Z}_U, i^V_!\mathbb{Z}_V$$ obtained by extension by zero from these. Here $$\mathbb{Z}_U, \mathbb{Z}_V$$ are constant sheaves, and since $$V \subset U$$ by assumption, there is a natural monomorphism $$i^V_!\mathbb{Z}_V \to i^U_!\mathbb{Z}_U$$.

First, let us verify that $$\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \mathcal{F}(U)$$. Since extension by zero $$i^U_!$$ is left adjoint to restriction $$\mathcal{G} \mapsto \mathcal{G}\vert_U$$ ([\[Topology\] §Sheaves, ⁋Example 14](/en/math/topology/sheaves#ex14)),

$$\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U)$$

holds. Now $$\mathbb{Z}_U$$ is the constant sheaf on $$U$$, so for any open set $$W \subset U$$ we have $$\mathbb{Z}_U(W) = \mathbb{Z}$$, and every section is given by restriction of a constant function. Thus a sheaf morphism $$\varphi: \mathbb{Z}_U \to \mathcal{F}\vert_U$$ is completely determined by the image of the global section $$\varphi_U(1) \in \mathcal{F}(U)$$. Conversely, for any $$s \in \mathcal{F}(U)$$, defining $$n \mapsto n \cdot s\vert_W$$ on each $$W \subset U$$ gives a well-defined sheaf morphism. Therefore

$$\Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U) \cong \Hom_{\Ab}(\mathbb{Z}, \mathcal{F}(U)) \cong \mathcal{F}(U)$$

holds. Similarly $$\Hom_{\Sh(X)}(i^V_!\mathbb{Z}_V, \mathcal{F}) \cong \mathcal{F}(V)$$, and by naturality the map between these coincides exactly with the restriction $$\mathcal{F}(U)\rightarrow \mathcal{F}(V)$$. Since $$\mathcal{F}$$ is injective by assumption, this is surjective, completing the proof.

</details>

<div class="proposition" markdown="1">

<ins id="lem10">**Lemma 10**</ins> A flasque sheaf $$\mathcal{F}$$ is Čech-acyclic for any open cover $$\mathcal{U}$$. That is, $$\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$$ for all $$p > 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the augmented Čech complex

$$0 \to \mathcal{F}(U) \xrightarrow{\epsilon} \check{C}^0(\mathcal{U}, \mathcal{F}) \xrightarrow{d^0} \check{C}^1(\mathcal{U}, \mathcal{F}) \xrightarrow{d^1} \cdots$$

We need to show that this is exact for $$p>0$$, so it suffices to show that the identity chain map is nullhomotopic. To do this, for each $$p\geq 1$$ we must explicitly construct a homotopy operator $$s^p : \check{C}^p(\mathcal{U}, \mathcal{F}) \to \check{C}^{p-1}(\mathcal{U}, \mathcal{F})$$.

To define this function, we need to explain how each component

$$s^p(t)_{j_0<\cdots< j_{p-1}}$$

is defined when given

$$t=(t_{j_0<\cdots< j_p})\in \check{C}^p(\mathcal{U}, \mathcal{F}).$$

Essentially, as is always the case when defining a chain homotopy, we want to fix an index $$i_0$$ and insert it into $$j_0<\cdots< j_{p-1}$$ (for convenience, assume $$i_0< j_0<\cdots< j_{p-1}$$), defining

$$s^p(t)_{j_0<\cdots< j_{p-1}}=t_{i_0< j_0<\cdots < j_{p-1}}\tag{$\ast$}$$

Note that $$s^p(t)_{j_0<\cdots< j_{p-1}}$$ is by definition a section over $$U_{j_0}\cap\cdots\cap U_{j_{p-1}}$$, but the right-hand side $$t_{i_0< j_0<\cdots < j_{p-1}}$$ is a section over the smaller set $$U_{i_0}\cap U_{j_0}\cap\cdots\cap U_{j_{p-1}}$$. For a general $$\mathcal{F}$$ this definition would be impossible, but we are assuming that $$\mathcal{F}$$ is flasque, so we can always extend this function to obtain a section over $$U_{j_0}\cap\cdots\cap U_{j_{p-1}}$$, and equation ($$\ast$$) should be understood in this way. Then the fact that $$s^p$$ so defined is actually a chain homotopy can be checked by direct calculation: in $$d^{p-1}s^p$$ the term omitting $$i_0$$ and in $$s^{p+1}d^p$$ the term inserting $$i_0$$ cancel each other out with opposite signs.

A slight technical issue is that the fixed index $$i_0$$ might be contained in $$j_0<\cdots< j_{p-1}$$. To handle this, instead of the usual Čech complex we use the *non-alternating* Čech complex, which uses coordinates given by $$p+1$$ elements $$i_0,\ldots, i_{p+1}\in I$$. This is quasi-isomorphic to the original Čech complex, so this detour is justified.

</details>

<div class="proposition" markdown="1">

<ins id="thm11">**Theorem 11 (Leray)**</ins> For a sheaf $$\mathcal{F}$$ on a topological space $$X$$ and an open cover $$\mathcal{U} = \{U_i\}$$, if $$\mathcal{F}$$ is acyclic on every finite intersection

$$U_{i_0 \cdots i_p}=U_{i_0}\cap \cdots\cap U_{i_p}$$

then there is an isomorphism

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \to H^p(X, \mathcal{F}).$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Fix an injective resolution $$0 \to \mathcal{F} \to \mathcal{I}^0 \to \mathcal{I}^1 \to \cdots$$ of $$\mathcal{F}$$, and construct the double complex

$$K^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q).$$

In this double complex, the horizontal differential $$d_h$$ is the Čech differential, and the vertical differential $$d_v$$ is the differential coming from the injective resolution. As we saw in [\[Homological Algebra\] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11), the two filtrations

$$F_v^p\Tot(K)^\bullet,\qquad F_h^p\Tot(K)^\bullet$$

on the total complex $$\Tot(K)^\bullet$$ converge to the same filtered homology $$H^\bullet(\Tot(K))$$.

So let us consider the spectral sequences given by each filtered complex. First, for the vertical filtration, on the $$E_1$$ page we have $$E_1^{p,q} = H^q(K^{p,\bullet})$$, and $$K^{p,\bullet} = \check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$$. Now $$\check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$$, looking at each component, restricts the injective resolution to each intersection $$U_{i_0 \cdots i_p}$$ and then takes cohomology, so this equals the $$q$$th sheaf cohomology of $$\mathcal{F}$$ on $$U_{i_0\cdots i_p}$$, and thus by the acyclicity assumption on $$\mathcal{F}$$ we have $$E_1^{p,q}=0$$ for all $$q>0$$. Also, by definition $$E_1=\check{C}^p(\mathcal{U}, \mathcal{F})$$. Now the $$E_2$$ page is given by the cohomology of $$E_1^{p,0}$$ with respect to the horizontal differential $$d_h$$, so

$$E_2^{p,q}=\begin{cases}\check{H}^p(\mathcal{U}, \mathcal{F})&\text{$q=0$}\\0&\text{otherwise}\end{cases}$$

and $$E_2^{p,q}=E_\infty^{p,q}$$.

Now looking in the horizontal filtration direction, on the $$E_1$$ page we have $$E_1^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{I}^q)$$. But we showed earlier in [Lemma 9](#lem9) and [Lemma 10](#lem10) that injective sheaves are Čech-acyclic, so $$E_1^{p,q} = 0$$ for $$p > 0$$, and the remaining cohomology with respect to the vertical differential at $$p=0$$ is sheaf cohomology, so

$$E_2^{p,q}=\begin{cases}H^q(X, \mathcal{F})&\text{$p=0$}\\0&\text{otherwise}\end{cases}$$

and $$E_2^{p,q}=E_\infty^{p,q}$$. Since the two spectral sequences converge to the same $$H^\bullet(\Tot(K))$$, we conclude that

$$\check{H}^n(\mathcal{U}, \mathcal{F}) \cong H^n(X, \mathcal{F}).$$

</details>

Then the only obstacle to our intuition is how demanding this acyclicity condition is, but fortunately it is a more generous condition than one might think.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For a quasi-coherent sheaf $$\mathcal{F} = \widetilde{M}$$ on an affine variety $$X$$, we have $$H^i(X, \mathcal{F}) = 0$$ for all $$i > 0$$.

</div>

The proof of this is as follows: letting $$A$$ be the coordinate ring of $$X$$, if we find an injective resolution $$I^\bullet$$ of $$M$$ in the category $$\lMod{A}$$, this gives $$\widetilde{I^\bullet}$$ (which is a resolution in $$\QCoh(X)$$), and the sheaf given by an injective module is always flasque and hence acyclic.

Now consider an arbitrary variety $$X$$ and a quasi-coherent sheaf $$\mathcal{F}$$ defined on it, and suppose an affine open cover $$\mathcal{U}$$ of $$\mathcal{F}$$ is given. For this data to satisfy the hypotheses of [Theorem 11](#thm11), every finite intersection of elements of $$\mathcal{U}$$ must again be affine. If the diagonal

$$\Delta_X\hookrightarrow X\times X$$

is a *closed* immersion in $$X\times X$$, then we can show that this condition holds, and in this case $$X$$ is called a *separated* variety. As can be seen from its definition, this can be regarded as the Zariski topology version of the Hausdorff condition, and it is a reasonable condition; if by variety we mean quasi-projective variety, as in our current definition, then this condition is automatically satisfied. That is, in our current language, this argument says that Čech cohomology and sheaf cohomology agree for any quasi-coherent sheaf defined on any variety, and moreover, if we choose an open cover $$\mathcal{U}$$ satisfying the hypotheses of [Theorem 11](#thm11), it suffices to compute the Čech cohomology for that open cover without taking a direct limit.

## Godement Resolution

In [Definition 1](#def1) we defined sheaf cohomology via injective resolution, but since directly computing an injective resolution is generally difficult, we saw one solution to this problem by using the result [Theorem 11](#thm11) that Čech cohomology and sheaf cohomology are isomorphic.

The Godement resolution, which we examine in this section, also starts from the same problem. That is, computing sheaf cohomology in general is a very complicated task, so [Definition 1](#def1) is conceptually clean but somewhat lacking in practicality. We now define a concrete resolution. This is not an injective resolution, but a flasque resolution, and for our purposes this is sufficient.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> For a sheaf $$\mathcal{F}$$ on a topological space $$X$$, the *Godement sheaf* $$C^0(\mathcal{F})$$ is defined for each open set $$U \subset X$$ by

$$C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x$$

where $$\mathcal{F}_x$$ is the stalk of $$\mathcal{F}$$ at $$x$$.

</div>

Then for each $$x\in X$$, the identity $$\mathcal{F}_x\rightarrow \mathcal{F}_x$$ on the stalk induces a canonical morphism $$\mathcal{F}\rightarrow C^0(\mathcal{F})$$ that is well-defined. Also, the fact that $$C^0(\mathcal{F})$$ is a sheaf follows almost trivially from the definition.

Intuitively, $$C^0(\mathcal{F})$$ can be thought of as the collection of functions that choose an element of $$\mathcal{F}_x$$ at each point $$x\in X$$ with no constraints whatsoever; from this perspective it is sometimes called the *sheaf of discontinuous sections*. The following is a basic property of this sheaf.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> The Godement sheaf $$C^0(\mathcal{F})$$ is a flasque sheaf. Moreover, $$\mathcal{F} \mapsto C^0(\mathcal{F})$$ is an exact functor.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First we show that the given sheaf is flasque. For open sets $$V \subset U$$, the restriction map $$C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x \to \prod_{x \in V} \mathcal{F}_x = C^0(\mathcal{F})(V)$$ is a projection, hence surjective. Therefore $$C^0(\mathcal{F})$$ is flasque.

Exactness is clear because the stalk functor $$\mathcal{F} \mapsto \mathcal{F}_x$$ is exact and $$C^0(\mathcal{F})$$ is merely a product of stalks.

</details>

Now consider the cokernel exact sequence induced by the canonical map $$0\rightarrow\mathcal{F}\rightarrow C^0(\mathcal{F})$$:

$$0\rightarrow \mathcal{F}\rightarrow C^0(\mathcal{F})\rightarrow \mathcal{Q}^1\rightarrow 0$$

Intuitively, $$\mathcal{Q}^1$$ collects the purely discontinuous parts, and from this perspective, the more we repeat this construction, the finer the information about discontinuity that is captured. That is, applying $$C^0$$ to the sheaf $$\mathcal{Q}^1$$ gives the next cokernel exact sequence

$$0 \rightarrow \mathcal{Q}^1\rightarrow C^0(\mathcal{Q}^1)\rightarrow\mathcal{Q}^2\rightarrow 0$$

and by splicing we obtain the complex

$$0 \rightarrow C^0(\mathcal{F}) \rightarrow C^0(\mathcal{Q}^1) \rightarrow C^0 (\mathcal{Q}^2)\rightarrow \cdots$$

We call this complex the *Godement resolution* of $$\mathcal{F}$$, and denote its terms by

$$0 \to \mathcal{F} \to \mathcal{G}^0(\mathcal{F}) \to \mathcal{G}^1(\mathcal{F}) \to \cdots$$

Then by [Proposition 14](#prop14), the following holds.

<div class="proposition" markdown="1">

<ins id="prop15">**Proposition 15**</ins> The Godement resolution $$\mathcal{G}^\bullet(\mathcal{F})$$ is a flasque resolution of $$\mathcal{F}$$.

</div>

The most essential advantage of this construction is that there are no choices made in the process, so in some sense it is canonical. This can also be seen again from the functoriality of the Godement resolution: in general, to show functoriality in sheaf cohomology one must use the argument that a sheaf morphism at the $$0$$th stage of an augmented complex induces sheaf morphisms at stages $$i>0$$ to produce a chain map, and such chain maps are identical up to chain homotopy equivalence, so they induce the same value in cohomology ([\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6)). However, in the case of the Godement resolution, the functions are induced purely at the chain level without any kind of equivalence. Nevertheless, the Godement resolution exactly captures the information of sheaf cohomology.

To show this, we first prove more generally that flasque resolution computes the same sheaf cohomology as injective resolution. For this we first show the following.

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> A flasque sheaf $$\mathcal{F}$$ is $$\Gamma(X, -)$$-acyclic. That is, $$H^i(X, \mathcal{F}) = 0$$ for all $$i > 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed by induction on $$i$$. First consider the case $$i=1$$. To show this, embed $$\mathcal{F}$$ into an injective sheaf $$\mathcal{I}$$ and consider the cokernel exact sequence

$$0 \rightarrow \mathcal{F}\rightarrow\mathcal{I}\rightarrow\mathcal{Q}\rightarrow0$$

Our claim is that $$\mathcal{Q}$$ is flasque, which can be shown by a diagram chase in the following commutative diagram for arbitrary open sets $$V\subset U$$:

![Commutative diagram](/assets/images/Math/Algebraic_Varieties/Sheaf_Cohomology-1.svg){:style="width:23.07em" class="invert" .align-center}

Here $$\mathcal{F}$$ is flasque by assumption and $$\mathcal{I}$$ is injective and hence flasque. Now for arbitrary $$s\in \mathcal{Q}(V)$$, since $$\mathcal{I}(V)\rightarrow \mathcal{Q}(V)$$ is surjective we can lift $$s$$ to $$t\in \mathcal{I}(V)$$, then use that $$\mathcal{I}$$ is flasque to lift $$t$$ to $$\overline{t}\in\mathcal{I}(U)$$, and map this to $$\mathcal{Q}$$ to define $$\overline{s}\in \mathcal{Q}(U)$$. Now the element $$\overline{s}\vert_V-s$$ in $$\mathcal{Q}(V)$$ comes from an element of $$\mathcal{F}(V)$$, and again by flasqueness of $$\mathcal{F}$$ there exists suitable $$h\in \mathcal{F}(U)$$ with $$h\vert_V=\overline{s}\vert_V-s$$. From this, $$\overline{s}-h$$ restricts exactly to $$s\in \mathcal{Q}(V)$$, yielding the flasqueness of $$\mathcal{Q}$$.

Now apply $$\Gamma(X, -)$$ to obtain the long exact sequence

$$0 \to \Gamma(X, \mathcal{F}) \to \Gamma(X, \mathcal{I}) \to \Gamma(X, \mathcal{Q}) \xrightarrow{\delta} H^1(X, \mathcal{F}) \to H^1(X, \mathcal{I}) = 0$$

Since $$\mathcal{I}$$ is injective, $$H^1(X, \mathcal{I}) = 0$$. Thus

$$H^1(X, \mathcal{F}) \cong \coker(\Gamma(X, \mathcal{I}) \to \Gamma(X, \mathcal{Q}))$$

and to show this is $$0$$ we need to show that $$\Gamma(X, \mathcal{I})\rightarrow \Gamma(X, \mathcal{Q})$$ is surjective. So let $$s\in \Gamma(X, \mathcal{Q})$$ be given. Then for any $$x\in X$$, since $$\mathcal{I}\rightarrow \mathcal{Q}$$ is surjective at the stalk level, for each $$x\in X$$ there exists suitable $$t_x\in \mathcal{I}_x$$ mapping to $$s_x\in \mathcal{Q}_x$$. Now choose a representative of $$t_x$$ and think of $$t_x$$ as an element of $$\mathcal{I}(U_x)$$; since $$\mathcal{I}$$ is flasque we can extend each of these to global sections $$T_x$$ on $$X$$, and then $$T_x\mid_{U_x}=s\mid_{U_x}$$.

Now let $$S_x$$ be the image of $$T_x$$ in $$\Gamma(X,\mathcal{Q})$$. Then $$S_x-S_y$$ is identically zero on $$U_x\cap U_y$$, so we can lift this to a section $$f_{xy}$$ of $$\mathcal{F}$$ over $$U_x\cap U_y$$. Using flasqueness of $$\mathcal{F}$$ again, we can extend this to $$f_x\in \mathcal{F}(U_x)$$ and $$f_y\in \mathcal{F}(U_y)$$ respectively, and then replacing $$T_x$$ by $$T'_x=T_x-f_x$$ in this situation satisfies the compatibility condition, so we know that gluing these gives a preimage of $$s$$.

Finally, by the long exact sequence,

$$H^i(X, \mathcal{F})\cong H^{i-1}(X, \mathcal{Q})$$

and since $$\mathcal{Q}$$ is flasque, we obtain the desired result by induction.

</details>

In particular, by [Proposition 16](#prop16), each term $$\mathcal{G}^p(\mathcal{F})$$ of the Godement resolution is flasque and hence $$\Gamma(X, -)$$-acyclic. That is, $$H^i(X, \mathcal{G}^p(\mathcal{F})) = 0$$ for all $$i > 0$$. To reach our conclusion, the result we need is the following.

<div class="proposition" markdown="1">

<ins id="prop17">**Proposition 17 (Acyclic Resolution)**</ins> Given a $$\Gamma(X, -)$$-acyclic resolution $$0 \to \mathcal{F} \to \mathcal{A}^0 \to \mathcal{A}^1 \to \cdots$$, we have

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(X, \mathcal{F})$$

for all $$q \geq 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Fix an injective resolution $$0 \to \mathcal{F} \to \mathcal{I}^\bullet$$ of $$\mathcal{F}$$. By the comparison theorem ([\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6)), there exists a chain map $$f\colon \mathcal{A}^\bullet \to \mathcal{I}^\bullet$$ between the acyclic resolution and the injective resolution. Consider the *mapping cone* $$C(f)^\bullet$$ of $$f$$. In each degree,

$$C(f)^n = \mathcal{A}^{n+1} \oplus \mathcal{I}^n$$

and since $$\mathcal{I}^n$$ is injective, it is flasque by [Lemma 9](#lem9), and in particular $$\Gamma(X, -)$$-acyclic. Thus considering the canonical short exact sequence

$$0 \to \mathcal{I}^n \to C(f)^n \to \mathcal{A}^{n+1} \to 0$$

the two end terms are $$\Gamma(X, -)$$-acyclic, so from the long exact sequence we see that $$C(f)^n$$ is also $$\Gamma(X, -)$$-acyclic.

On the other hand, since $$f$$ is a quasi-isomorphism, $$C(f)^\bullet$$ is an exact complex ([\[Homological Algebra\] §The Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9)). Moreover, as we saw above, $$C(f)^\bullet$$ is $$\Gamma(X,-)$$-acyclic, so applying $$\Gamma(X,-)$$ yields the exact complex $$\Gamma(X, C(f)^\bullet)$$, and applying [\[Homological Algebra\] §The Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9) again converts this to the condition that the chain map

$$\Gamma(X, f)\colon \Gamma(X, \mathcal{A}^\bullet) \to \Gamma(X, \mathcal{I}^\bullet)$$

is a quasi-isomorphism. From this we obtain

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(\Gamma(X, \mathcal{I}^\bullet)) = H^q(X, \mathcal{F}).$$

</details>

[Proposition 17](#prop17) together with [Proposition 16](#prop16) guarantees that the Godement resolution is indeed sufficient for computing sheaf cohomology. That is, the cohomology of the complex $$\Gamma(X, \mathcal{G}^\bullet(\mathcal{F}))$$ obtained by taking global sections of the flasque resolution $$\mathcal{G}^\bullet(\mathcal{F})$$ coincides with $$H^\bullet(X, \mathcal{F})$$.

## Spectral Sequence

One of the most powerful applications of sheaf cohomology is the computation of cohomology via spectral sequences. In this section we conclude this post with concrete computations. The propositions we introduce now hold in a general topological setting, but since we mainly have in mind applications to varieties and quasi-coherent sheaves, we have placed them in this category.

Fix a continuous map $$f : X \to Y$$ and a sheaf $$\mathcal{F}$$. Then from [\[Topology\] §Sheaves, ⁋Lemma 11](/en/math/topology/sheaves#lem11) and [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9), we know that the direct image functor $$f_\ast: \Sh(X)\rightarrow \Sh(Y)$$ is a left exact functor. Thus, just as in [\[Homological Algebra\] §Derived Functors](/en/math/homological_algebra/derived_functors), we can define the right derived functor of $$f_\ast$$ by

$$R^q f_\ast \mathcal{F} := H^q(f_\ast \mathcal{I}^\bullet)$$

where $$\mathcal{I}^\bullet$$ is an injective resolution of $$\mathcal{F}$$. By definition, when $$q=0$$ we have $$R^0 f_\ast \mathcal{F}=f_\ast \mathcal{F}$$, and if $$\mathcal{F}$$ is injective then $$\mathcal{F}$$ itself forms an injective resolution, so $$R^qf_\ast \mathcal{F}=0$$.

Now consider the Godement resolution $$\mathcal{G}^\bullet(\mathcal{F})$$ of $$\mathcal{F}$$. Intuitively, what we want to do is to choose an injective resolution for each $$\mathcal{G}^p(\mathcal{F})$$, and then use [\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6) to define the horizontal differential from the differential $$\mathcal{G}^p(\mathcal{F})\rightarrow \mathcal{G}^{p+1}(\mathcal{F})$$ of the Godement resolution.

<div class="definition" markdown="1">

<ins id="def18">**Definition 18 (Cartan-Eilenberg Resolution)**</ins> In an abelian category, a *Cartan-Eilenberg resolution* of a cochain complex $$K^\bullet$$ is data consisting of a double complex $$I^{p,q}$$ and an augmentation $$K^\bullet \to I^{\bullet,0}$$ satisfying the following conditions:

1. Each column $$I^{p,\bullet}$$ is an injective resolution of $$K^p$$.
2. The cohomology of each row $$H^p(I^{\bullet,q})$$ forms an injective resolution of $$H^p(K^\bullet)$$. That is, the chain complex

    $$\cdots \to H^p(I^{\bullet,q-1}) \to H^p(I^{\bullet,q}) \to H^p(I^{\bullet,q+1}) \to \cdots$$

    is an injective resolution of $$H^p(K^\bullet)$$.

</div>

The key point of this definition is that the intuition mentioned above is not enough to obtain a Cartan-Eilenberg resolution; in particular, the condition that the cohomology of each row forms a horizontal resolution of $$H^p(K^\bullet)$$ is an essential element in the proof of existence. We do not separately prove the existence of Cartan-Eilenberg resolutions, but basically they can be obtained by repeatedly applying [\[Homological Algebra\] §Resolutions, ⁋Lemma 7](/en/math/homological_algebra/resolutions#lem7).

Now fix a Cartan-Eilenberg resolution $$\mathcal{I}^{p,q}$$ of the complex $$f_\ast\mathcal{G}^\bullet(\mathcal{F})$$. Then by definition each column $$\mathcal{I}^{p,\bullet}$$ is an injective resolution of $$f_\ast\mathcal{G}^p(\mathcal{F})$$, and the horizontal cohomology of each row $$H^p(\mathcal{I}^{\bullet,q})$$ forms an injective resolution of $$H^p(f_\ast\mathcal{G}^\bullet(\mathcal{F})) = R^p f_\ast\mathcal{F}$$.

Since this spectral sequence lies in the first quadrant, we know that it converges to the cohomology of the total complex $$\Tot(\mathcal{I})^\bullet$$. For a concrete computation, let us filter by $$p$$ in the Godement direction. Then we can first write the $$E_1$$ page as

$$\mathcal{H}^{p,q} := H^p(\mathcal{I}^{\bullet, q}).$$

Here the vertical differential is the map $$\mathcal{H}^{p,q}\rightarrow \mathcal{H}^{p,q+1}$$ induced by the differential of the injective resolution descending to the cohomology level, and the $$E_2$$ page is the cohomology sheaf of this vertical complex:

$$E_2^{p,q} = H^q(\mathcal{H}^{p,\bullet}).$$

On the other hand, since $$\mathcal{I}^{\bullet,\bullet}$$ is a Cartan resolution, we know that each $$\mathcal{H}^{p,\bullet}$$ is an injective resolution of $$R^p f_\ast \mathcal{F}$$. We call this spectral sequence the *Leray spectral sequence*.

Now if we consider the spectral sequence coming from filtration in the $$q$$ direction, its $$E_1$$ page is given by

$$E_1^{p,q} = H^q(\mathcal{I}^{p,\bullet}).$$

Here, for each $$p$$, $$\mathcal{I}^{p,\bullet}$$ is an injective resolution of $$f_\ast \mathcal{G}^p(\mathcal{F})$$, so by exactness of injective resolution,

$$E_1^{p,q} = \begin{cases} f_\ast \mathcal{G}^p(\mathcal{F}) & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

and the $$d_1$$-differential is the map from $$E_1^{p,0} = f_\ast \mathcal{G}^p(\mathcal{F})$$ to $$E_1^{p+1,0} = f_\ast \mathcal{G}^{p+1}(\mathcal{F})$$, corresponding to the differential $$f_\ast \mathcal{G}^p(\mathcal{F}) \to f_\ast \mathcal{G}^{p+1}(\mathcal{F})$$ of the Godement resolution. That is, the $$E_2$$ page is the cohomology sheaf of the complex

$$0 \to f_\ast \mathcal{F} \to f_\ast \mathcal{G}^0(\mathcal{F}) \to f_\ast \mathcal{G}^1(\mathcal{F}) \to \cdots$$

and by the definition of $$R^q f_\ast$$ this is given by

$$E_2^{p,q} = \begin{cases} R^p f_\ast \mathcal{F} & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

Thus the cohomology of the total complex of $$\mathcal{I}^{\bullet,\bullet}$$ must converge to $$R^n f_\ast \mathcal{F}$$.

Now let us apply the global section functor $$\Gamma(Y,-)$$ to this result and revisit the above discussion. That is, we consider the double complex

$$\mathcal{J}^{p,q}=\Gamma(Y, \mathcal{I}^{p,q})$$

and its total complex $$\Tot(\mathcal{J})^\bullet$$. Then by the same computation as above, the filtration in the $$p$$ direction gives on the $$E_1$$ page

$$E_1^{p,q}=H^p(\mathcal{J}^{\bullet, q})=\Gamma(Y, \mathcal{H}^{p,q})$$

and since $$\mathcal{H}^{p,q}$$ is an injective resolution of $$R^pf_\ast \mathcal{F}$$, its cohomology comes out as $$H^q(Y, R^p f_\ast \mathcal{F})$$.

On the other hand, for the filtration in the $$q$$ direction, the $$E_1$$ page is

$$E_1^{p,q}=H^q(\Gamma(Y, \mathcal{I}^{p,\bullet}))$$

and here each $$\mathcal{I}^{p,\bullet}$$ is an injective resolution by the definition of Cartan-Eilenberg resolution, hence flasque ([Lemma 9](#lem9)), and since flasque sheaves are $$\Gamma$$-acyclic, the terms with $$q>0$$ vanish and what remains is

$$E_1^{p,0}=\Gamma(Y, f_\ast \mathcal{G}^p (\mathcal{F}))=\Gamma(X, \mathcal{G}^p(\mathcal{F}))$$

with the Godement differential. Thus the $$E_2$$ page is

$$E_2^{n,0}=H^n(\Gamma(X, \mathcal{G}^\bullet(\mathcal{F}))=H^n(X, \mathcal{F})$$

and therefore we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop19">**Proposition 19 (Leray Spectral Sequence)**</ins> For a continuous map $$f : X \to Y$$ and a sheaf $$\mathcal{F}$$, there exists a spectral sequence with $$E_2$$ page

$$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F}).$$

</div>

Geometrically, this is most transparent when $$f:X\rightarrow Y$$ is a fibration; in this case what the spectral sequence says is that to compute the cohomology on $$X$$, we first compute the cohomology on $$Y$$, then remember the cohomology on the fiber over each point as the higher sheaf $$R^q f_\ast \mathcal{F}$$, and finally compose these over $$Y$$.

In the lowest dimensions of the Leray spectral sequence, we obtain the following exact sequence.

<div class="proposition" markdown="1">

<ins id="cor20">**Corollary 20 (Five-Term Exact Sequence)**</ins> For a continuous map $$f : X \to Y$$ and a sheaf $$\mathcal{F}$$, from the Leray spectral sequence we obtain the exact sequence

$$0 \to H^1(Y, f_\ast \mathcal{F}) \to H^1(X, \mathcal{F}) \to H^0(Y, R^1 f_\ast \mathcal{F}) \overset{d_2}{\to} H^2(Y, f_\ast \mathcal{F}) \to H^2(X, \mathcal{F}).$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the terms with $$p+q \leq 2$$ on the $$E_2$$ page of the Leray spectral sequence $$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$$. By [\[Homological Algebra\] §Spectral Sequences, ⁋Definition 5](/en/math/homological_algebra/spectral_sequences#def5) we know that

$$E_\infty^{p,q} \cong \gr^p H^{p+q} = F^p H^{p+q}/F^{p+1}H^{p+q}$$

In particular, since this is a first quadrant spectral sequence, for sufficiently large $$r$$ we have $$E_r^{p,q} = E_\infty^{p,q}$$ ([\[Homological Algebra\] §Spectral Sequences, ⁋Proposition 6](/en/math/homological_algebra/spectral_sequences#prop6)).

First, looking at the components with $$p+q = 1$$, there are only two terms $$E_2^{1,0}$$ and $$E_2^{0,1}$$. But considering degrees, all differentials into or out of $$E_2^{1,0}$$ are zero, so $$E_2^{1,0} = E_\infty^{1,0}$$. On the other hand, the $$d_2$$ from $$E_2^{0,1}$$ to $$E_2^{2,0}$$ may be nontrivial, so $$E_\infty^{0,1} = \ker(d_2: E_2^{0,1} \to E_2^{2,0})$$. Then by the filtration,

$$0 \to E_\infty^{1,0} \to H^1(X, \mathcal{F}) \to E_\infty^{0,1} \to 0$$

is exact, and since $$E_\infty^{1,0} = E_2^{1,0}$$ and $$E_\infty^{0,1} = \ker(d_2) \hookrightarrow E_2^{0,1}$$, combining these gives the exact sequence

$$0 \to E_2^{1,0} \to H^1(X, \mathcal{F}) \to E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

To complete the proof, now look at the components $$E_2^{2,0}$$, $$E_2^{1,1}$$, $$E_2^{0,2}$$ with $$p+q = 2$$. For the same reason, the only possibly nontrivial differential is $$d_2 : E_2^{0,1} \to E_2^{2,0}$$, and on the $$E_3$$ page defined by this differential,

$$E_3^{0,2} = \ker(d_2 : E_2^{0,2} \to E_2^{2,1}), \qquad E_3^{2,0} = \operatorname{coker}(d_2 : E_2^{0,1} \to E_2^{2,0})$$

and again analyzing degrees, $$E_3^{p,q} = E_\infty^{p,q}$$, so

$$E_\infty^{2,0} = E_3^{2,0} = \operatorname{coker}(d_2 : E_2^{0,1} \to E_2^{2,0})$$

We have so far shown that the exact sequence

$$0 \to E_2^{1,0} \to H^1(X, \mathcal{F}) \to E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

exists, and from the above computation,

$$E_\infty^{2,0} = E_3^{2,0} = \operatorname{coker}(d_2: E_2^{0,1} \to E_2^{2,0})$$

so putting this into $$F^2 H^2 \hookrightarrow H^2(X, \mathcal{F})$$ through the filtration,

$$E_2^{0,1} \overset{d_2}{\to} E_2^{2,0} \to H^2(X, \mathcal{F})$$

is exact. Combining these gives the desired result.

</details>

This exact sequence shows what constraints the existence of the $$d_2$$-differential imposes on cohomology computations, and in favorable cases it justifies the intuition that $$H^i(X, \mathcal{F}) \cong H^i(Y, f_\ast \mathcal{F})$$.

Finally, we can describe the relationship between Čech cohomology and derived functor cohomology using a spectral sequence.

<div class="proposition" markdown="1">

<ins id="prop21">**Proposition 21 (Čech-to-Derived Functor Spectral Sequence)**</ins> For a sheaf $$\mathcal{F}$$ on a topological space $$X$$ and an open cover $$\mathcal{U}$$, there exists a spectral sequence

$$E_2^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) \Rightarrow H^{p+q}(X, \mathcal{F})$$

where $$\mathcal{H}^q(\mathcal{F})$$ is the sheafification of the presheaf $$U \mapsto H^q(U, \mathcal{F})$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Take the Godement resolution $$\mathcal{G}^\bullet(\mathcal{F})$$ of $$\mathcal{F}$$ and construct the double complex $$C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{G}^q(\mathcal{F}))$$. That the two spectral sequences obtained from the two filtrations converge to the same total cohomology $$H^{p+q}(X, \mathcal{F})$$ follows from [\[Homological Algebra\] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11), and since the Godement sheaf $$\mathcal{G}^q(\mathcal{F})$$ is flasque, it is Čech-acyclic by [Lemma 10](#lem10), so we can use the same vanishing as in the computation above.

</details>

This spectral sequence allows us to understand [Theorem 11](#thm11) in a broader context. If $$\mathcal{F}$$ is acyclic on all finite intersections of $$\mathcal{U}$$, then $$\mathcal{H}^q(\mathcal{F}) = 0$$ for all $$q > 0$$, so all terms with $$q > 0$$ on the $$E_2$$ page vanish and we obtain $$E_2^{p,0} = \check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$$. That is, the Čech-to-derived functor spectral sequence is a more general result that includes [Theorem 11](#thm11).

## Classification of Line Bundles

Earlier we saw that a line bundle is determined by transition functions $$g_{ij} \in \mathcal{O}_X^\ast(U_i \cap U_j)$$ ([§Line Bundles and Vector Bundles, ⁋Proposition 2](/en/math/algebraic_varieties/line_bundles#prop2)). Transition functions satisfy the cocycle condition $$g_{ij}g_{jk} = g_{ik}$$, which corresponds exactly to the Čech 1-cocycle condition written in multiplicative notation. Also, isomorphism of line bundles corresponds to transition functions changing as $$g_{ij} \mapsto h_i g_{ij} h_j^{-1}$$ via functions $$h_i \in \mathcal{O}_X^\ast(U_i)$$ on each $$U_i$$, which again matches the equivalence relation given by Čech 1-coboundaries. That is, the isomorphism class of a line bundle corresponds naturally to an element of $$\check{H}^1(X, \mathcal{O}_X^\ast)$$.

Organizing this observation rigorously, we obtain the following. The point to note here is that since $$\mathcal{O}_X^\ast$$ is a sheaf of (abelian) groups with multiplicative structure, the coboundary relation in Čech cohomology is expressed multiplicatively rather than additively. Specifically, a 1-coboundary is of the form $$(g_{ij}) = (h_i \cdot h_j^{-1})$$.

<div class="proposition" markdown="1">

<ins id="prop22">**Proposition 22**</ins> $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \Pic(X)$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First we define a map from $$\check{H}^1(X, \mathcal{O}_X^\ast)$$ to $$\Pic(X)$$. Given a Čech 1-cocycle $$(g_{ij}) \in \check{Z}^1(\mathcal{U}, \mathcal{O}_X^\ast)$$, we construct a line bundle $$\mathcal{L}$$ having this as its transition function. To do this, we take the trivial bundle $$U_i \times \mathbb{A}^1$$ on each $$U_i$$, and glue over $$U_i \cap U_j$$ by $$(p, t) \mapsto (p, g_{ij}(p)t)$$. Then by the cocycle condition $$g_{ij}g_{jk} = g_{ik}$$, this gluing is consistent, so we obtain a well-defined line bundle.

On the other hand, given two cocycles that are equivalent by a coboundary, $$g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$$, we can define an isomorphism between the corresponding two line bundles by $$\varphi_i: \mathcal{L}\vert_{U_i} \to \mathcal{M}\vert_{U_i}$$, $$v \mapsto h_i^{-1} v$$. Then the compatibility of $$\varphi_i$$ and $$\varphi_j$$ on $$U_i \cap U_j$$ can be checked from

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

and thus the map $$\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \to \Pic(X)$$ is well-defined.

Conversely, any line bundle $$\mathcal{L}$$ is represented by transition functions $$g_{ij}$$ over a suitable open cover $$\mathcal{U}$$ ([§Line Bundles and Vector Bundles, ⁋Definition 1](/en/math/algebraic_varieties/line_bundles#def1)), and these form a Čech 1-cocycle. Since line bundle isomorphism corresponds exactly to the equivalence relation given by coboundaries, the kernel of this map consists of coboundaries. Thus $$\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \to \Pic(X)$$ is injective. Now taking the direct limit gives $$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \Pic(X)$$.

</details>

This proposition shows that the classification of line bundles reduces to a cohomology computation. That is, the problem of classifying elements of $$\Pic(X)$$ now becomes the problem of classifying $$\mathcal{O}_X^\ast$$-valued Čech 1-cocycles, which is encouraging in that explicit computation is possible. In the next post, [§Cohomology of Projective Space](/en/math/algebraic_varieties/cohomology_of_projective_spaces), we compute the cohomology of the line bundle $$\mathcal{O}(d)$$ on $$\mathbb{P}^n$$.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
**[Wei]** C. A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38, Cambridge University Press, 1994.

---

[^1]: More generally, as we saw in [\[Topology\] §Sheaves, §§The Abelian Category of Sheaves](/en/math/topology/sheaves#the-abelian-category-of-sheaves), the category $$\Sh(X)$$ of sheaves defined on an arbitrary topological space $$X$$ forms an abelian category.
