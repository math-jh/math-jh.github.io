---
title: "Sheaf Cohomology"
description: "Beyond global sections of line bundles, we define sheaf cohomology using derived functors to capture finer information about sheaves and explore its properties."
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/sheaf_cohomology
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-05
weight: 13
translated_at: 2026-08-18T23:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-27T11:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We have seen that we can consider various invariants using line bundles. For instance, in [§Line Bundles and Vector Bundles](/en/math/algebraic_varieties/line_bundles){: data-lid="8zh7f" }, we defined the global section space $\Gamma(X, \mathcal{L})$ of a line bundle $\mathcal{L}$. In particular, in [§Linear Systems, ⁋Definition 9](/en/math/algebraic_varieties/linear_systems#def9){: data-lid="373yx" }, we saw that this dimension plays a key role in determining the dimension of the complete linear system and, further, the projective embedding of the variety.

Although we have primarily used the language of line bundles for geometric intuition so far, as we saw right after [§Canonical Line Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1){: data-lid="wgjdg" }, considering the section sheaf of a line bundle means that this can fundamentally be rewritten in the language of sheaves. In this post, we define the notion of sheaf cohomology.

## Definition as a Derived Functor

While sheaves are a tool that can systematically describe all the information of a topological space, in our discussion so far, the only time sheaves came to the fore was when we saw in [§Linear Systems](/en/math/algebraic_varieties/linear_systems){: data-lid="nv806" } that the global section space $\Gamma(X, \mathcal{L})$ determines the projective embedding of the complete linear system.

However, if global sections were our only concern, there would be no need to think about sheaves; we could have simply considered the global section functor. In fact, the global section functor does not capture all the information contained in a sheaf. For example, consider the global section functor

$$\Gamma(X, -): \QCoh(X) \rightarrow \Vect_\mathbb{K}; \qquad \mathcal{F} \mapsto \mathcal{F}(X)$$

When we defined quasi-coherent sheaves in [§Canonical Line Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1){: data-lid="sxw6t" }, our motivation was that the category $\Bun(X)$ of vector bundles is not an abelian category, so we considered a larger category that adds kernels and cokernels; from this perspective, it is not surprising that $\QCoh(X)$ becomes an abelian category. [^1]

If $\Gamma(X,-)$ did not lose any information, this functor would have to be an exact functor. That is, given a short exact sequence of (quasi-coherent) sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

its image under $\Gamma(X,-)$ should also be a short exact sequence. However, this functor is only a left exact functor. That is, the exactness of

$$0 \rightarrow \Gamma(X, \mathcal{F}') \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{F}'')$$

is guaranteed, but the surjection

$$\Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{F}'') \rightarrow 0$$

is not guaranteed in general. For a concrete example, consider the Euler sequence

$$0 \rightarrow \Omega^1_{\mathbb{P}^n} \rightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow 0$$

([§Canonical Line Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7){: data-lid="fssau" }). Applying $\Gamma(\mathbb{P}^n, -)$ to this short exact sequence, we obtain

$$0 \rightarrow \Gamma(\mathbb{P}^n, \Omega^1_{\mathbb{P}^n}) \rightarrow \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) \rightarrow \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})$$

However, as we saw in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16){: data-lid="xniuo" }, the global sections of $\mathcal{O}_{\mathbb{P}^n}(-1)$ are only 0, so

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) = 0$$

yet $\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})=\mathbb{K}$, so surjectivity on the right cannot hold.

The standard way to resolve this is to consider right derived functors ([\[Homological Algebra\] §Derived Functors, ⁋Definition 9](/en/math/homological_algebra/derived_functors#def9){: data-lid="j8feh" }). Specifically, since it can be shown that the category $\Sh(X)$ of sheaves of abelian groups on $X$ has enough injectives by choosing an injective abelian group at each stalk and taking the product of skyscraper sheaves, any sheaf $\mathcal{F}$ always has an injective resolution $\mathcal{I}^\bullet$, and from this, via the following

$$0 \rightarrow \Gamma(X, \mathcal{I}^0) \rightarrow \Gamma(X, \mathcal{I}^1) \rightarrow \Gamma(X, \mathcal{I}^2) \rightarrow \cdots$$

we can define the following sheaf cohomology.

::: Definition 1
For a sheaf $\mathcal{F}$ on a variety $X$, we define the $i$th *sheaf cohomology* $H^i(X, \mathcal{F})$ by

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1}))}{\im(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i))}$$

where $\mathcal{I}^\bullet$ is an injective resolution of $\mathcal{F}$ in $\Sh(X)$.
:::

That this is independent of the choice of $\mathcal{I}^\bullet$, and so on, all follow from standard arguments in homological algebra.

Earlier, when introducing the global section space $\Gamma(X, \mathcal{L})$, we mentioned that another popular notation for this space is $H^0(X, \mathcal{L})$; we see that this notation is justified directly by the definition above.

The following proposition is also a standard proposition that follows directly from homological algebra. ([\[Homological Algebra\] §Derived Functors](/en/math/homological_algebra/derived_functors){: data-lid="v0qc5" })

::: Proposition 2
For a short exact sequence of sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

there exists a long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow \cdots$$

Here $\delta$ is the *connecting homomorphism*.
:::

## Čech Cohomology

[Definition 1](#def1){: data-lid="tmrot" } is rigorous as a definition of sheaf cohomology, but explicitly constructing an injective resolution is generally very difficult. Therefore, in actual computations, we use the Čech approach, which defines cohomology from a different perspective.

Intuitively, Čech cohomology $\check{H}^i(X, \mathcal{F})$ is a tool that measures the failure of gluing local information. That is, $\check{H}^0(X, \mathcal{F})$ is precisely the global section space, and $\check{H}^1(X, \mathcal{F})$ tells us how much the process of gluing local sections to obtain a global section fails. To define this rigorously, we begin with the following.

::: Definition 3
Let an open cover $\mathcal{U} = \{U_i\}_{i \in I}$ of a topological space $X$ and a sheaf $\mathcal{F}$ be given, and fix an arbitrary total order $<$ on $I$. Then the *Čech complex* $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ of this data is defined as follows:

$$\check{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

Here, the *coboundary map* $d: \check{C}^p \rightarrow \check{C}^{p+1}$ is defined by the formula

$$(\dd{\alpha})_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0}\cap \cdots \cap U_{i_{p+1}}}$$

where $\hat{i_k}$ means that the index $i_k$ is omitted.
:::

For this definition to be well-defined, that is, for $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ to actually be a complex, the coboundary map must actually be a coboundary map; that is, we must have $d^2=0$. This can be verified directly from the sign differences upon expanding the formula above. Consequently, $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ is a cochain complex, and therefore we can define the following.

::: Definition 4
We define the *Čech cohomology* $\check{H}^p(\mathcal{U}, \mathcal{F})$ defined by the above data to be the cohomology of the Čech complex:

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\check{C}^\bullet(\mathcal{U}, \mathcal{F}))$$
:::

We said earlier that Čech cohomology is a tool that measures the failure of gluing; this is contained in the coboundary map. Let us examine the intuitive meaning of the coboundary map in low dimensions $p = 0, 1$.

::: Example 5 ($p = 0$)
By the definition of the Čech complex, $\check{C}^0(\mathcal{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$, and the coboundary map from $\check{C}^0$ to $\check{C}^1$ is

$$(\dd{s})_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}$$

Therefore,

$$\check{H}^0(\mathcal{U}, \mathcal{F}) = \ker(d: \check{C}^0 \rightarrow \check{C}^1) = \left\{(s_i) \in \prod_i \mathcal{F}(U_i) \mid s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\right\}$$

By the gluing condition of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1){: data-lid="zrxe8" }, such a family of sections coincides exactly with a section over all of $X$, that is, with $\Gamma(X, \mathcal{F})$. That is, $\check{H}^0(\mathcal{U}, \mathcal{F}) = H^0(X, \mathcal{F})$, and this is independent of the choice of open cover.
:::

We will soon show that, in favorable situations, Čech cohomology and sheaf cohomology always agree as above. For now, let us first see how this measures the failure of gluing in the case $p=1$.

::: Example 6 ($p = 1$)
A 1-cochain is a collection of sections $s_{ij} \in \mathcal{F}(U_i \cap U_j)$ over each $U_i \cap U_j$, and a 1-cocycle is one satisfying the cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \qquad\text{on}\quad U_i \cap U_j \cap U_k$$

On the other hand, a 1-coboundary is one induced from a 0-cochain $(t_i)$, that is, of the form $s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$.

Thus, a nontrivial element of $\check{H}^1(\mathcal{U}, \mathcal{F})$ reflects the discrepancy that appears when trying to glue these three pieces of data $s_{ij}, s_{jk}, s_{ik}$ together, and this can be regarded as the failure of gluing mentioned above.
:::

So far, we have defined Čech cohomology $\check{H}^p(\mathcal{U}, \mathcal{F})$ for a single open cover $\mathcal{U}$. However, different open covers can generally give different Čech cohomologies. For example, for a cover consisting of a single open set $U_0 = X$, all intersections are $X$, so $\check{H}^p$ is nonzero only at $p = 0$. The finer the cover, the more topological information we can capture, so we need to understand the relationship between open covers and synthesize the information over all open covers. That is, let us impose an order relation on *all* open covers using refinement. Then, for a refinement $\mathcal{V} = \{V_j\}_{j \in J} \preceq \mathcal{U} = \{U_i\}_{i \in I}$, choosing a function $\lambda: J \rightarrow I$ such that $V_j \subseteq U_{\lambda(j)}$ for each $j$ yields a cochain-level map $\lambda^\ast: \check{C}^p(\mathcal{U}, \mathcal{F}) \rightarrow \check{C}^p(\mathcal{V}, \mathcal{F})$ defined by

$$(\lambda^\ast\alpha)_{j_0 \cdots j_p} = \alpha_{\lambda(j_0) \cdots \lambda(j_p)}\vert_{V_{j_0} \cap \cdots \cap V_{j_p}}$$

This map depends on the choice of $\lambda$, but for another $\mu: J \rightarrow I$ satisfying the same condition,

$$h(\alpha)_{j_0 \cdots j_{p-1}} = \sum_{k=0}^{p-1} (-1)^k \alpha_{\lambda(j_0) \cdots \lambda(j_k) \mu(j_k) \cdots \mu(j_{p-1})}\vert_{V_{j_0} \cap \cdots \cap V_{j_{p-1}}}$$

gives a chain homotopy between $\lambda^\ast$ and $\mu^\ast$, so at the cohomology level a single map $\check{H}^p(\mathcal{U}, \mathcal{F}) \rightarrow \check{H}^p(\mathcal{V}, \mathcal{F})$ is determined independent of the choice. For the same reason, these maps are compatible with composition of refinements, and hence we can define a direct system $\check{H}^p(\mathcal{U}, \mathcal{F})$ indexed by all open covers. From this we make the following definition.

::: Definition 7
We define the *Čech cohomology* of $X$ to be the direct limit over all open covers:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathcal{U}} \check{H}^p(\mathcal{U}, \mathcal{F})$$
:::

To explain the above argument more simply, it means that we take increasingly finer open covers, combine all the additional cohomology data, and define this to be $\check{H}(X, \mathcal{F})$.

In general, it is not guaranteed that $\check{H}^p(X, \mathcal{F})$ of [Definition 7](#def7){: data-lid="n8o30" } and $H^p(X, \mathcal{F})$ of [Definition 1](#def1){: data-lid="9mwzo" } are isomorphic, but fortunately, for most sheaves that arise in algebraic geometry, the two coincide. Showing this requires rather technical machinery.

::: Definition 8
For a sheaf $\mathcal{F}$ on a variety $X$, we define the following.

1. The sheaf $\mathcal{F}$ is *acyclic* if $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
2. An injective object $\mathcal{F}$ of $\Sh(X)$ is called an *injective sheaf*.
3. If the restriction map $\mathcal{F}(U) \rightarrow \mathcal{F}(V)$ is surjective for every open set $V\subseteq U$, then $\mathcal{F}$ is called a *flasque sheaf*.
:::

Of course, the condition we want at the cohomology level is the first one. We first examine the relationships among the above concepts.

::: Lemma 9
An injective sheaf $\mathcal{F}$ is flasque.
:::

::: Proof
By definition, $\mathcal{F}$ being injective means that for any monomorphism $\mathcal{A} \hookrightarrow \mathcal{B}$, the map $\Hom_{\Sh(X)}(\mathcal{B}, \mathcal{F}) \rightarrow \Hom_{\Sh(X)}(\mathcal{A}, \mathcal{F})$ is surjective. ([\[Homological Algebra\] §Resolutions, ⁋Definition 1](/en/math/homological_algebra/resolutions#def1){: data-lid="z0js2" }) We now show that for any open sets $V \subseteq U \subseteq X$, the restriction $\mathcal{F}(U) \rightarrow \mathcal{F}(V)$ is surjective.

This map is not a sheaf morphism but a morphism of abelian groups, and since our tools are sheaf morphisms, we must recast this condition in terms of sheaf morphisms. To do this, let us introduce the open embeddings

$$i^U: U \hookrightarrow X,\qquad i^V: V \hookrightarrow X$$

and the sheaves $i^U_!\mathbb{Z}_U, i^V_!\mathbb{Z}_V$ obtained by their extension by zero. Here $\mathbb{Z}_U, \mathbb{Z}_V$ are each constant sheaves, and since $V \subseteq U$ by assumption, there exists a natural monomorphism $i^V_!\mathbb{Z}_V \rightarrow i^U_!\mathbb{Z}_U$.

First, let us verify that $\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \mathcal{F}(U)$ holds. Since extension by zero $i^U_!$ is left adjoint to restriction $\mathcal{G} \mapsto \mathcal{G}\vert_U$ ([\[Topology\] §Sheaves, ⁋Example 14](/en/math/topology/sheaves#ex14){: data-lid="bbfh1" }),

$$\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U)$$

holds. Now $\mathbb{Z}_U$ is the sheafification of the constant presheaf $\underline{\mathbb{Z}}$ assigning $\mathbb{Z}$ to each open set, and sheafification is left adjoint to the inclusion $\Sh(U) \rightarrow \PSh(U)$, so

$$\Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U) \cong \Hom_{\PSh(U)}(\underline{\mathbb{Z}}, \mathcal{F}\vert_U)$$

holds. However, since the restriction maps of $\underline{\mathbb{Z}}$ are all the identity on $\mathbb{Z}$, a presheaf morphism $\varphi: \underline{\mathbb{Z}} \rightarrow \mathcal{F}\vert_U$ must satisfy $\varphi_W(1) = \varphi_U(1)\vert_W$ for each $W \subseteq U$, and is thus completely determined by $\varphi_U(1) \in \mathcal{F}(U)$. Conversely, for any $s \in \mathcal{F}(U)$, defining $n \mapsto n \cdot s\vert_W$ on each $W \subseteq U$ yields a presheaf morphism. Therefore

$$\Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U) \cong \mathcal{F}(U)$$

holds. Similarly, $\Hom_{\Sh(X)}(i^V_!\mathbb{Z}_V, \mathcal{F}) \cong \mathcal{F}(V)$, and now from naturality we see that the map between them coincides exactly with the restriction $\mathcal{F}(U)\rightarrow \mathcal{F}(V)$. Now, since $\mathcal{F}$ is injective by assumption, this is surjective, which completes the proof.
:::

::: Lemma 10
A flasque sheaf $\mathcal{F}$ is Čech-acyclic for any open cover $\mathcal{U}$. That is, $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for all $p > 0$.
:::

::: Proof
Let us lift the Čech complex to the sheaf level. That is, if we consider the sheaf $\mathcal{C}^p$ defined for each open set $V \subseteq X$ by

$$\mathcal{C}^p(V) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(V \cap U_{i_0} \cap \cdots \cap U_{i_p})$$

then by definition $\Gamma(X, \mathcal{C}^p) = \check{C}^p(\mathcal{U}, \mathcal{F})$, and the Čech coboundary map is defined by the same formula on each $V$, giving a sheaf morphism $\mathcal{C}^p \rightarrow \mathcal{C}^{p+1}$. Also, taking the collection of restrictions $\epsilon : \mathcal{F} \rightarrow \mathcal{C}^0$ as the augmentation, we obtain the complex

$$0 \rightarrow \mathcal{F} \xrightarrow{\epsilon} \mathcal{C}^0 \xrightarrow{d^0} \mathcal{C}^1 \xrightarrow{d^1} \cdots$$

What we need to show is that applying $\Gamma(X,-)$ to this yields exactness for $p>0$.

First, let us show that this complex itself is exact. If we fix an index $i_0 \in I$ and consider only open sets $V \subseteq U_{i_0}$, then for each $t \in \mathcal{C}^p(V)$ we obtain a map $s^p : \mathcal{C}^p(V) \rightarrow \mathcal{C}^{p-1}(V)$ defined by

$$s^p(t)_{j_0 < \cdots < j_{p-1}} = t_{i_0 j_0 \cdots j_{p-1}}\tag{$\ast$}$$

The right-hand side is a section over $V \cap U_{i_0} \cap U_{j_0} \cap \cdots \cap U_{j_{p-1}}$, but since $V \subseteq U_{i_0}$, this set equals $V \cap U_{j_0} \cap \cdots \cap U_{j_{p-1}}$, which is where the left-hand side should lie; thus no extension is involved in formula ($\ast$). That the $s^p$ defined in this way is a chain homotopy can be checked by direct computation: in $d^{p-1}s^p$ the term omitting $i_0$ and in $s^{p+1}d^p$ the term inserting $i_0$ cancel with opposite signs. That is, the complex of sections of the above complex over $V$ is exact, and since $\mathcal{U}$ covers $X$, every point has such a $V$ as a neighborhood, giving exactness at every stalk. A slight technical issue is that the fixed index $i_0$ might appear among $j_0<\cdots< j_{p-1}$. To handle this, instead of the usual Čech complex, we simply use the *non-alternating* Čech complex with coordinates given by $p+1$ elements $i_0,\ldots, i_p\in I$ of $I$. This is quasi-isomorphic to the original Čech complex, so this detour is justified.

Now we use the assumption that $\mathcal{F}$ is flasque. The restriction map of each $\mathcal{C}^p$ is a product of restriction maps of $\mathcal{F}$, hence surjective, so $\mathcal{C}^p$ is also flasque. Thus $\mathcal{C}^\bullet$ is a flasque resolution of $\mathcal{F}$, so each term is $\Gamma(X,-)$-acyclic by [Proposition 16](#prop16){: data-lid="s5x68" }, and by [Proposition 17](#prop17){: data-lid="lyjc0" }

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\Gamma(X, \mathcal{C}^\bullet)) \cong H^p(X, \mathcal{F})$$

Again, since $\mathcal{F}$ is flasque, the right-hand side vanishes for $p>0$ by [Proposition 16](#prop16){: data-lid="x20ht" }. The proofs of the two propositions used here do not depend on this lemma.
:::

::: Theorem 11 (Leray)
For a topological space $X$, a sheaf $\mathcal{F}$ on $X$, and an open cover $\mathcal{U} = \{U_i\}$, if on every finite intersection

$$U_{i_0 \cdots i_p}=U_{i_0}\cap \cdots\cap U_{i_p}$$

$\mathcal{F}$ is acyclic, then an isomorphism

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \rightarrow H^p(X, \mathcal{F})$$

exists.
:::

::: Proof
Fix an injective resolution of the sheaf $\mathcal{F}$, $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^0 \rightarrow \mathcal{I}^1 \rightarrow \cdots$, and construct the double complex

$$K^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q)$$

Then, in this double complex, the horizontal differential $d_h$ is the Čech differential, and the vertical differential $d_v$ is the differential coming from the injective resolution. Now, as we saw in [\[Homological Algebra\] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11){: data-lid="70p2x" }, we know that the two filtrations defined on the total complex $\Tot(K)^\bullet$ of this double complex,

$$F_v^p\Tot(K)^\bullet,\qquad F_h^p\Tot(K)^\bullet$$

converge to the same filtered homology $H^\bullet(\Tot(K))$.

Therefore, let us consider the spectral sequences given by each filtered complex. First, in the case of the vertical filtration, on the $E_1$ page we have $E_1^{p,q} = H^q(K^{p,\bullet})$, and $K^{p,\bullet} = \check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$. However, looking at each component, $\check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$ is obtained by restricting the injective resolution to each intersection $U_{i_0 \cdots i_p}$ and then taking cohomology, which on $U_{i_0\cdots i_p}$ is equal to the sheaf cohomology of $\mathcal{F}$ in degree $q$; thus, from the assumption that $\mathcal{F}$ is acyclic, for all $q>0$ we have $E_1^{p,q}=0$. Also, by definition, $E_1^{p,0}=\check{C}^p(\mathcal{U}, \mathcal{F})$. Now, since the $E_2$ page is given by the cohomology of $E_1^{p,0}$ with respect to the horizontal differential $d_h$,

$$E_2^{p,q}=\begin{cases}\check{H}^p(\mathcal{U}, \mathcal{F})&\text{$q=0$}\\0&\text{otherwise}\end{cases}$$

and $E_2^{p,q}=E_\infty^{p,q}$.

Now, looking at the direction of the horizontal filtration, on the $E_1$ page we have $E_1^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{I}^q)$. However, since we previously showed in [Lemma 9](#lem9){: data-lid="4c0dj" } and [Lemma 10](#lem10){: data-lid="xgmwo" } that injective sheaves are Čech-acyclic, for $p > 0$ we have $E_1^{p,q} = 0$, and since the remaining cohomology with respect to the vertical differential at $p=0$ is sheaf cohomology,

$$E_2^{p,q}=\begin{cases}H^q(X, \mathcal{F})&\text{$p=0$}\\0&\text{otherwise}\end{cases}$$

and $E_2^{p,q}=E_\infty^{p,q}$. Now, since the two spectral sequences converge to the same $H^\bullet(\Tot(K))$, we know that

$$\check{H}^n(\mathcal{U}, \mathcal{F}) \cong H^n(X, \mathcal{F})$$
:::

Then the only obstacle to our intuition is how demanding this acyclicity condition is, but fortunately it is a more generous condition than one might think.

::: Proposition 12
On an affine variety $X$, for a quasi-coherent sheaf $\mathcal{F} = \widetilde{M}$, we have $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
:::

The proof of this is that, letting the coordinate ring of $X$ be $A$, if in the category $\lMod{A}$ we find for $M$ an injective resolution $I^\bullet$, this gives on $X$ a resolution $\widetilde{I^\bullet}$ of sheaves; here, since $A$ is a finitely generated $\mathbb{K}$-algebra, it is Noetherian, and because the sheaf given by an injective module over a Noetherian ring is always flasque, by [Proposition 16](#prop16){: data-lid="swaxp" } and [Proposition 17](#prop17){: data-lid="kpqv8" } below, this flasque resolution computes $H^i(X, \mathcal{F})$. The proofs of the two propositions cited here do not use this proposition.

Now consider an arbitrary variety $X$ and a quasi-coherent sheaf $\mathcal{F}$ defined on it, and suppose that on $X$ an affine open cover $\mathcal{U}$ is given. Then for these data to satisfy the hypotheses of [Theorem 11](#thm11){: data-lid="j8xt7" }, any finite intersection of members of $\mathcal{U}$ must again be affine. If the diagonal

$$\Delta_X\hookrightarrow X\times X$$

is a *closed* embedding into $X\times X$, then this condition can be shown to hold, and in this case we call $X$ a *separated* variety. As can be seen from its definition, this is the Zariski topology analogue of the Hausdorff condition and is just as reasonable a condition; moreover, if, as in our present definition, we call a quasi-projective variety a variety, this condition is automatically satisfied. That is, in our present language, this argument means that for a quasi-coherent sheaf defined on an arbitrary variety, Čech cohomology and sheaf cohomology agree, and furthermore shows that if we choose an open cover $\mathcal{U}$ satisfying the hypotheses of [Theorem 11](#thm11){: data-lid="1gqve" }, it suffices to compute the Čech cohomology for that open cover without having to compute the direct limit.

## Godement Resolution

In [Definition 1](#def1){: data-lid="6im7c" } we defined sheaf cohomology via injective resolutions, but since injective resolutions are generally difficult to compute directly, as one solution to this we examined using the earlier result, [Theorem 11](#thm11){: data-lid="czunm" }, that Čech cohomology and sheaf cohomology are isomorphic.

The Godement resolution, which we examine in this section, also starts from the same problem. That is, computing sheaf cohomology in general is a very complicated task, so while [Definition 1](#def1){: data-lid="g68m8" } is conceptually clean, its practicality is somewhat lacking. We now define a concrete resolution. It is not an injective resolution, but it is a flasque resolution, and for our purposes this is sufficient.

::: Definition 13
For a topological space $X$ and a sheaf $\mathcal{F}$ on it, the *Godement sheaf* $C^0(\mathcal{F})$ is defined for each open set $U \subseteq X$ by

$$C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x$$

where $\mathcal{F}_x$ is the stalk of $\mathcal{F}$ at $x$.
:::

Then for each $x\in X$, from the identity $\mathcal{F}_x\rightarrow \mathcal{F}_x$ on the stalk, a canonical morphism $\mathcal{F}\rightarrow C^0(\mathcal{F})$ is well-defined. Also, that $C^0(\mathcal{F})$ is a sheaf is almost obvious.

Intuitively, $C^0(\mathcal{F})$ can be thought of as the collection of functions choosing, at each point $x\in X$, an element of $\mathcal{F}_x$ with no constraints whatsoever; from this perspective it is sometimes called the *sheaf of discontinuous sections*. The following is a basic property of this sheaf.

::: Proposition 14
The Godement sheaf $C^0(\mathcal{F})$ is a flasque sheaf. Moreover, $\mathcal{F} \mapsto C^0(\mathcal{F})$ is an exact functor.
:::

::: Proof
First we show that the given sheaf is flasque. For open sets $V \subseteq U$, the restriction map $C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x \rightarrow \prod_{x \in V} \mathcal{F}_x = C^0(\mathcal{F})(V)$ is a projection, hence surjective. Therefore $C^0(\mathcal{F})$ is flasque.

Exactness is obvious because the stalk functor $\mathcal{F} \mapsto \mathcal{F}_x$ is exact and $C^0(\mathcal{F})$ is merely a product of stalks.
:::

Now consider the cokernel exact sequence induced by the canonical map $0\rightarrow\mathcal{F}\rightarrow C^0(\mathcal{F})$:

$$0\rightarrow \mathcal{F}\rightarrow C^0(\mathcal{F})\rightarrow \mathcal{Q}^1\rightarrow 0$$

Intuitively, $\mathcal{Q}^1$ collects the purely discontinuous parts, and from this perspective, repeating this construction captures finer and finer information about discontinuity. That is, applying $C^0$ to the sheaf $\mathcal{Q}^1$, we obtain the following cokernel exact sequence

$$0 \rightarrow \mathcal{Q}^1\rightarrow C^0(\mathcal{Q}^1)\rightarrow\mathcal{Q}^2\rightarrow 0$$

and by splicing we obtain the complex

$$0 \rightarrow C^0(\mathcal{F}) \rightarrow C^0(\mathcal{Q}^1) \rightarrow C^0 (\mathcal{Q}^2)\rightarrow \cdots$$

We call this complex the *Godement resolution* of $\mathcal{F}$, and denote its terms by

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{G}^0(\mathcal{F}) \rightarrow \mathcal{G}^1(\mathcal{F}) \rightarrow \cdots$$

Then by [Proposition 14](#prop14){: data-lid="lm8wi" } the following holds.

::: Proposition 15
The Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ is a flasque resolution of $\mathcal{F}$.
:::

The most essential advantage of this construction is that no choices are made in the process, so in some sense it is canonical. This can also be seen again from the functoriality of the Godement resolution: in general, to show functoriality in sheaf cohomology one must use the argument that a sheaf morphism at the $0$-th stage of an augmented complex induces sheaf morphisms at stages $i>0$ giving a chain map, and such chain maps are the same up to chain homotopy equivalence, hence induce the same map on cohomology. ([\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6){: data-lid="mm0qw" }) However, for the Godement resolution, the maps are induced purely at the chain level without any kind of equivalence. Nevertheless, the Godement resolution exactly captures the information of sheaf cohomology.

To show this, we prove more generally that a flasque resolution gives the same sheaf cohomology as that computed by an injective resolution. For this, we first show the following.

::: Proposition 16
A flasque sheaf $\mathcal{F}$ is $\Gamma(X, -)$-acyclic. That is, for all $i > 0$, $H^i(X, \mathcal{F}) = 0$.
:::

::: Proof
We proceed by induction on $i$. First, let us show the case $i=1$. To this end, after embedding $\mathcal{F}$ into an injective sheaf $\mathcal{I}$, we consider the cokernel exact sequence

$$0 \rightarrow \mathcal{F}\rightarrow\mathcal{I}\rightarrow\mathcal{Q}\rightarrow0$$

Our claim is that for any open set $V$, the map $\mathcal{I}(V)\rightarrow \mathcal{Q}(V)$ is surjective, and that from this $\mathcal{Q}$ is also flasque. For the latter, granting the former, it suffices to do a diagram chase in the following commutative diagram for any open sets $V\subseteq U$:

{% diagram Math/Algebraic_Varieties/Sheaf_Cohomology-1.svg width="23.07em" alt="Commutative diagram" %}

Here $\mathcal{F}$ is flasque by hypothesis, and $\mathcal{I}$ is injective, hence flasque. Now for any $s\in \mathcal{Q}(V)$, by our claimed surjectivity we can lift $s$ to $t\in \mathcal{I}(V)$, and using again that $\mathcal{I}$ is flasque, we can extend $t$ to $\overline{t}\in\mathcal{I}(U)$ and then map this to $\mathcal{Q}$ to define $\overline{s}\in \mathcal{Q}(U)$. Since $\overline{t}$ is an extension of $t$, we have $\overline{t}\vert_V=t$, and therefore $\overline{s}\vert_V$ is what $t$ maps to in $\mathcal{Q}(V)$, namely $s$. Thus $\overline{s}$ restricts precisely to $s\in \mathcal{Q}(V)$, and from this we obtain the flasqueness of $\mathcal{Q}$.

Now applying $\Gamma(X, -)$, let us obtain the long exact sequence

$$0 \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{Q}) \xrightarrow{\delta} H^1(X, \mathcal{F}) \rightarrow H^1(X, \mathcal{I}) = 0$$

Here, since $\mathcal{I}$ is injective, $H^1(X, \mathcal{I}) = 0$. Therefore

$$H^1(X, \mathcal{F}) \cong \coker(\Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{Q}))$$

and to show that this is $0$, we must show that $\Gamma(X, \mathcal{I})\rightarrow \Gamma(X, \mathcal{Q})$ is surjective. We show this for an arbitrary open set. That is, suppose that an open set $U\subseteq X$ and $s\in \mathcal{Q}(U)$ are given; for an open subset of $U$, $V$, and an element mapping in $\mathcal{Q}(V)$ to $s\vert_V$, $t\in \mathcal{I}(V)$, consider the collection of pairs $(V, t)$, $P$. Defining on this $(V, t)\leq (V', t')$ to mean $V\subseteq V'$ and $t'\vert_V=t$, $P$ becomes a partially ordered set. Since $\mathcal{I}\rightarrow \mathcal{Q}$ is surjective at the stalk level, there exists a lift of $s$ on a suitable neighborhood of each point, so $P$ is not empty; and for pairs belonging to a chain in $P$, their $t$'s agree with each other on overlaps, so gluing them by the gluing axiom of $\mathcal{I}$ yields an upper bound of that chain. Therefore, by Zorn's lemma, $P$ admits a maximal element $(V, t)$.

Now it suffices to show that $V=U$. If there exists $x\in U\setminus V$, we can choose a suitable neighborhood of $x$, $W\subseteq U$, and an element that maps to $s\vert_W$, $t'\in \mathcal{I}(W)$. Then the image of $t\vert_{V\cap W}-t'\vert_{V\cap W}$ in $\mathcal{Q}(V\cap W)$ is $0$, so it comes from some $f\in \mathcal{F}(V\cap W)$, and since $\mathcal{F}$ is flasque, we can extend this to $\widetilde{f}\in \mathcal{F}(W)$. Now replacing $t'$ with $t'+\widetilde{f}$, this also maps to $s\vert_W$ while agreeing on $V\cap W$ with $t$, so gluing the two together yields on $V\cup W$ a lift of $s$. This contradicts the maximality of $(V, t)$, so $V=U$. In particular, the case $U=X$ is the surjectivity of $\Gamma(X, \mathcal{I})\rightarrow \Gamma(X, \mathcal{Q})$ that we needed, and at the same time the flasqueness of $\mathcal{Q}$ deferred above is also obtained.

Finally, in the case $i\geq 2$, since $H^{i-1}(X, \mathcal{I})$ and $H^i(X, \mathcal{I})$ on both sides in the long exact sequence vanish by the injectivity of $\mathcal{I}$, we have

$$H^i(X, \mathcal{F})\cong H^{i-1}(X, \mathcal{Q})$$

and since $\mathcal{Q}$ is flasque, we obtain the desired result by induction.
:::

In particular, by [Proposition 16](#prop16){: data-lid="8104t" }, each term $\mathcal{G}^p(\mathcal{F})$ of the Godement resolution is flasque, hence $\Gamma(X, -)$-acyclic. That is, for all $i > 0$, $H^i(X, \mathcal{G}^p(\mathcal{F})) = 0$. Now, what we need in order to reach the conclusion is the following result.

::: Proposition 17 (Acyclic Resolution)
Given a $\Gamma(X, -)$-acyclic resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{A}^0 \rightarrow \mathcal{A}^1 \rightarrow \cdots$,

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(X, \mathcal{F})$$

holds for all $q \geq 0$.
:::

::: Proof
For $\mathcal{F}$, fix an injective resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$. By [\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6){: data-lid="p7hq1" }, there exists a chain map $f\colon \mathcal{A}^\bullet \rightarrow \mathcal{I}^\bullet$ between the acyclic resolution and the injective resolution. Consider the *mapping cone* of $f$, $C(f)^\bullet$. In each degree,

$$C(f)^n = \mathcal{A}^{n+1} \oplus \mathcal{I}^n$$

and since $\mathcal{I}^n$ is injective, it is flasque by [Lemma 9](#lem9){: data-lid="bwpel" }, hence in particular $\Gamma(X, -)$-acyclic. Therefore, considering the canonical short exact sequence

$$0 \rightarrow \mathcal{I}^n \rightarrow C(f)^n \rightarrow \mathcal{A}^{n+1} \rightarrow 0$$

since both outer terms are $\Gamma(X, -)$-acyclic, we see from the long exact sequence that $C(f)^n$ is also $\Gamma(X, -)$-acyclic.

Meanwhile, since $f$ is a quasi-isomorphism, $C(f)^\bullet$ is an exact complex. ([\[Homological Algebra\] §Long Exact Sequences, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9){: data-lid="9h6b9" }) Moreover, as seen above, $C(f)^\bullet$ is $\Gamma(X,-)$-acyclic, so applying $\Gamma(X,-)$ yields an exact complex $\Gamma(X, C(f)^\bullet)$, and applying [\[Homological Algebra\] §Long Exact Sequences, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9){: data-lid="glpcn" } again translates this into the condition that the chain map

$$\Gamma(X, f)\colon \Gamma(X, \mathcal{A}^\bullet) \rightarrow \Gamma(X, \mathcal{I}^\bullet)$$

is a quasi-isomorphism. From this, we obtain

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(\Gamma(X, \mathcal{I}^\bullet)) = H^q(X, \mathcal{F})$$
:::

[Proposition 17](#prop17){: data-lid="zqd90" }, together with [Proposition 16](#prop16){: data-lid="pq5eq" }, guarantees that the Godement resolution is indeed sufficient for computing sheaf cohomology. That is, taking global sections of the flasque resolution $\mathcal{G}^\bullet(\mathcal{F})$ yields the complex $\Gamma(X, \mathcal{G}^\bullet(\mathcal{F}))$, whose cohomology agrees with $H^\bullet(X, \mathcal{F})$.

## Spectral Sequence

One of the most powerful applications of sheaf cohomology is the computation of cohomology via spectral sequences. In this section, we conclude this post with concrete calculations. The propositions introduced now hold in a general topological setting, but since we mainly have in mind applications to varieties and quasi-coherent sheaves, we have included them in this category.

Fix a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$. Then from [\[Topology\] §Sheaves, ⁋Lemma 11](/en/math/topology/sheaves#lem11){: data-lid="5r71v" } and [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9){: data-lid="7bq5d" }, we know that the direct image functor $f_\ast: \Sh(X)\rightarrow \Sh(Y)$ is a left exact functor. Hence, just as in [\[Homological Algebra\] §Derived Functors](/en/math/homological_algebra/derived_functors){: data-lid="vr02n" }, we can define the right derived functors of $f_\ast$ by

$$R^q f_\ast \mathcal{F} := H^q(f_\ast \mathcal{I}^\bullet)$$

where $\mathcal{I}^\bullet$ is an injective resolution of $\mathcal{F}$. By definition, when $q=0$ we have $R^0 f_\ast \mathcal{F}=f_\ast \mathcal{F}$, and if $\mathcal{F}$ is injective, then $\mathcal{F}$ itself forms an injective resolution, so $R^qf_\ast \mathcal{F}=0$ holds for all $q>0$.

Now, for $\mathcal{F}$, consider the Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$. Intuitively, what we want to do is to choose an injective resolution for each $\mathcal{G}^p(\mathcal{F})$, and then, from the differential $\mathcal{G}^p(\mathcal{F})\rightarrow \mathcal{G}^{p+1}(\mathcal{F})$ of the Godement resolution, define the horizontal differential via [\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6){: data-lid="9d7bm" }.

::: Definition 18 (Cartan-Eilenberg Resolution)
In an abelian category, a *Cartan-Eilenberg resolution* of a cochain complex $K^\bullet$ is the data consisting of a double complex $I^{p,q}$ and an augmentation $K^\bullet \rightarrow I^{\bullet,0}$ satisfying the following conditions.

1. Each column $I^{p,\bullet}$ is an injective resolution of $K^p$.
2. The cohomology $H^p(I^{\bullet,q})$ of each row forms an injective resolution of $H^p(K^\bullet)$. That is, the chain complex

    $$0 \rightarrow H^p(K^\bullet) \rightarrow H^p(I^{\bullet,0}) \rightarrow H^p(I^{\bullet,1}) \rightarrow \cdots$$

    is an injective resolution of $H^p(K^\bullet)$.
3. Likewise, for each $p$, $B^p(I^{\bullet,q})$ and $Z^p(I^{\bullet,q})$ arranged along $q$ form injective resolutions of $B^p(K^\bullet)$ and $Z^p(K^\bullet)$, respectively.
:::

The heart of this definition is that the intuition mentioned above alone does not yield a Cartan-Eilenberg resolution; in particular, that the cohomology of each row forms a horizontal resolution of $H^p(K^\bullet)$ is a key element in the proof of existence. We do not prove the existence of Cartan-Eilenberg resolutions separately, but basically it can be obtained by repeatedly applying [\[Homological Algebra\] §Resolutions, ⁋Lemma 7](/en/math/homological_algebra/resolutions#lem7){: data-lid="bk3u3" }.

Meanwhile, the third condition ensures that the left-hand terms $Z^p(I^{\bullet,q})$ and $B^p(I^{\bullet,q})$ of the two short exact sequences of each row,

$$0\rightarrow Z^p(I^{\bullet,q})\rightarrow I^{p,q}\rightarrow B^{p+1}(I^{\bullet,q})\rightarrow 0$$

$$0\rightarrow B^p(I^{\bullet,q})\rightarrow Z^p(I^{\bullet,q})\rightarrow H^p(I^{\bullet,q})\rightarrow 0$$

are injective, so that both sequences split and each row decomposes into a direct sum of injective objects; this provides the basis below for a left exact functor to commute with row-wise cohomology.

Now fix a Cartan-Eilenberg resolution $\mathcal{I}^{p,q}$ of the complex $f_\ast\mathcal{G}^\bullet(\mathcal{F})$. Then by definition each column $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast\mathcal{G}^p(\mathcal{F})$, and the horizontal cohomology $H^p(\mathcal{I}^{\bullet,q})$ of each row forms an injective resolution of $H^p(f_\ast\mathcal{G}^\bullet(\mathcal{F})) = R^p f_\ast\mathcal{F}$.

Since this spectral sequence lies in the first quadrant, we know that it converges to the cohomology of the total complex $\Tot(\mathcal{I})^\bullet$. For the concrete computation, let us impose a filtration by $p$ in the Godement direction. Then we can first write the $E_1$ page as

$$\mathcal{H}^{p,q} := H^p(\mathcal{I}^{\bullet, q})$$

Here the vertical differential is the morphism $\mathcal{H}^{p,q}\rightarrow \mathcal{H}^{p,q+1}$ induced by the differential of the injective resolution descending to the cohomology level, and the $E_2$ page is the cohomology sheaf of this vertical complex:

$$E_2^{p,q} = H^q(\mathcal{H}^{p,\bullet})$$

On the other hand, since $\mathcal{I}^{\bullet,\bullet}$ is a Cartan resolution, we know that each $\mathcal{H}^{p,\bullet}$ is an injective resolution of $R^p f_\ast \mathcal{F}$.

Meanwhile, considering the spectral sequence arising from the filtration in the $q$ direction, its $E_1$ page is given by

$$E_1^{p,q} = H^q(\mathcal{I}^{p,\bullet})$$

Here, since for each $p$, $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast \mathcal{G}^p(\mathcal{F})$, by the exactness of injective resolutions we have

$$E_1^{p,q} = \begin{cases} f_\ast \mathcal{G}^p(\mathcal{F}) & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

and the $d_1$-differential is the morphism from $E_1^{p,0} = f_\ast \mathcal{G}^p(\mathcal{F})$ to $E_1^{p+1,0} = f_\ast \mathcal{G}^{p+1}(\mathcal{F})$, which corresponds to the differential $f_\ast \mathcal{G}^p(\mathcal{F}) \rightarrow f_\ast \mathcal{G}^{p+1}(\mathcal{F})$ of the Godement resolution. That is, the $E_2$ page is the cohomology sheaf of the complex

$$0 \rightarrow f_\ast \mathcal{G}^0(\mathcal{F}) \rightarrow f_\ast \mathcal{G}^1(\mathcal{F}) \rightarrow \cdots$$

and by the definition of $R^q f_\ast$ this is given by

$$E_2^{p,q} = \begin{cases} R^p f_\ast \mathcal{F} & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

Therefore, we know that the cohomology of the total complex of $\mathcal{I}^{\bullet,\bullet}$ must converge to $R^n f_\ast \mathcal{F}$.

Now let us apply the global section functor $\Gamma(Y,-)$ to this result and revisit the above discussion. That is, we consider the double complex

$$\mathcal{J}^{p,q}=\Gamma(Y, \mathcal{I}^{p,q})$$

and its total complex $\Tot(\mathcal{J})^\bullet$. Then by the same computation as above, the filtration in the $p$ direction yields on the $E_1$ page

$$E_1^{p,q}=H^p(\mathcal{J}^{\bullet, q})=\Gamma(Y, \mathcal{H}^{p,q})$$

Here the second equality holds because, by the third condition of [Definition 18](#def18){: data-lid="kfhav" }, each row splits into injective objects so that $\Gamma(Y,-)$ commutes with row-wise cohomology. Also, since $\mathcal{H}^{p,q}$ is an injective resolution of $R^pf_\ast \mathcal{F}$, we know that its cohomology comes out as $H^q(Y, R^p f_\ast \mathcal{F})$.

On the other hand, in the case of the filtration in the $q$ direction, the $E_1$ page is

$$E_1^{p,q}=H^q(\Gamma(Y, \mathcal{I}^{p,\bullet}))$$

and here, since each $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast \mathcal{G}^p(\mathcal{F})$ by the definition of a Cartan-Eilenberg resolution, we have $E_1^{p,q}=H^q(Y, f_\ast \mathcal{G}^p(\mathcal{F}))$. But $\mathcal{G}^p(\mathcal{F})$ is flasque and $f_\ast$ preserves flasqueness, so $f_\ast \mathcal{G}^p(\mathcal{F})$ is also flasque; hence by [Proposition 16](#prop16){: data-lid="zqwu3" }, the terms at $q>0$ vanish and what remains is

$$E_1^{p,0}=\Gamma(Y, f_\ast \mathcal{G}^p (\mathcal{F}))=\Gamma(X, \mathcal{G}^p(\mathcal{F}))$$

and the differential here is the Godement differential. Therefore the $E_2$ page is

$$E_2^{n,0}=H^n(\Gamma(X, \mathcal{G}^\bullet(\mathcal{F})))=H^n(X, \mathcal{F})$$

Meanwhile, since the $E_2$ page given earlier by the filtration in the $p$ direction was $E_2^{p,q}=H^q(Y, R^p f_\ast \mathcal{F})$, in what follows we follow standard notation and interchange the names of the two indices. The spectral sequence obtained in this way is called the *Leray spectral sequence*, and thus we obtain the following.

::: Proposition 19 (Leray Spectral Sequence)
For a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$, there exists a spectral sequence with the following $E_2$ page.

$$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F}).$$
:::

Geometrically, its meaning is clearest when $f:X\rightarrow Y$ is a fibration. In this case, what this spectral sequence means is that to compute the cohomology on $X$, we first compute the cohomology on $Y$, remember the cohomology on the fiber at each point as the higher sheaf $R^q f_\ast \mathcal{F}$, and then assemble them over $Y$.

Now, in the lowest dimensions of the Leray spectral sequence, we can obtain the following exact sequence.

::: Corollary 20 (Five-Term Exact Sequence)
For a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$, from the Leray spectral sequence we obtain the following exact sequence

$$0 \rightarrow H^1(Y, f_\ast \mathcal{F}) \rightarrow H^1(X, \mathcal{F}) \rightarrow H^0(Y, R^1 f_\ast \mathcal{F}) \overset{d_2}{\rightarrow} H^2(Y, f_\ast \mathcal{F}) \rightarrow H^2(X, \mathcal{F})$$
:::

::: Proof
Consider the terms with $p+q \leq 2$ on the $E_2$ page of the Leray spectral sequence $E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$. By [\[Homological Algebra\] §Spectral Sequences, ⁋Definition 5](/en/math/homological_algebra/spectral_sequences#def5){: data-lid="bv2sl" }, we know that

$$E_\infty^{p,q} \cong \gr^p H^{p+q} = F^p H^{p+q}/F^{p+1}H^{p+q}$$

In particular, since this is a first quadrant spectral sequence, we have $E_r^{p,q} = E_\infty^{p,q}$ for sufficiently large $r$. ([\[Homological Algebra\] §Spectral Sequences, ⁋Proposition 6](/en/math/homological_algebra/spectral_sequences#prop6){: data-lid="ezytt" })

First, looking at the components with $p+q = 1$, only two terms, $E_2^{1,0}$ and $E_2^{0,1}$, exist. However, considering degrees, all differentials entering or leaving $E_2^{1,0}$ are zero, so $E_2^{1,0} = E_\infty^{1,0}$. On the other hand, $d_2$ from $E_2^{0,1}$ to $E_2^{2,0}$ may be nontrivial, so $E_\infty^{0,1} = \ker(d_2: E_2^{0,1} \rightarrow E_2^{2,0})$. Then by the filtration,

$$0 \rightarrow E_\infty^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_\infty^{0,1} \rightarrow 0$$

is exact, and since here $E_\infty^{1,0} = E_2^{1,0}$ and $E_\infty^{0,1} = \ker(d_2) \hookrightarrow E_2^{0,1}$, combining these yields the following exact sequence

$$0 \rightarrow E_2^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

Now, to complete the proof, let us look at the components $E_2^{2,0}$, $E_2^{1,1}$, $E_2^{0,2}$ with $p+q = 2$. For the same reason, $d_2 : E_2^{0,1} \rightarrow E_2^{2,0}$ is the only nontrivial differential, and on the $E_3$ page defined by this differential,

$$E_3^{0,2} = \ker(d_2 : E_2^{0,2} \rightarrow E_2^{2,1}), \qquad E_3^{2,0} = \coker(d_2 : E_2^{0,1} \rightarrow E_2^{2,0})$$

and analyzing degrees again, $E_3^{p,q} = E_\infty^{p,q}$, so

$$E_\infty^{2,0} = E_3^{2,0} = \coker(d_2 : E_2^{0,1} \rightarrow E_2^{2,0})$$

We have shown so far that the exact sequence

$$0 \rightarrow E_2^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

exists, and since from the above computation

$$E_\infty^{2,0} = E_3^{2,0} = \coker(d_2: E_2^{0,1} \rightarrow E_2^{2,0})$$

inserting this via the filtration into $F^2 H^2 \hookrightarrow H^2(X, \mathcal{F})$ gives that

$$E_2^{0,1} \overset{d_2}{\rightarrow} E_2^{2,0} \rightarrow H^2(X, \mathcal{F})$$

is exact. Combining these gives the desired result.
:::

This exact sequence shows what constraints the existence of the $d_2$-differential imposes on the computation of cohomology, and in good cases it justifies the intuition that $H^i(X, \mathcal{F}) \cong H^i(Y, f_\ast \mathcal{F})$.

Finally, we can describe the relationship between Čech cohomology and derived functor cohomology via a spectral sequence.

::: Proposition 21 (Čech-to-Derived Functor Spectral Sequence)
On a topological space $X$, for a sheaf $\mathcal{F}$ and an open cover $\mathcal{U}$, there exists a spectral sequence

$$E_2^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) \Rightarrow H^{p+q}(X, \mathcal{F})$$

Here $\mathcal{H}^q(\mathcal{F})$ is the presheaf $U \mapsto H^q(U, \mathcal{F})$.
:::

::: Proof
For $\mathcal{F}$, take the Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ and form the double complex $C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{G}^q(\mathcal{F}))$. That the two spectral sequences obtained from the two filtrations converge to the same total cohomology $H^{p+q}(X, \mathcal{F})$ follows from [\[Homological Algebra\] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11){: data-lid="259se" }, and since the Godement sheaf $\mathcal{G}^q(\mathcal{F})$ is flasque, it is Čech-acyclic by [Lemma 10](#lem10){: data-lid="7ukmj" }, so one can use the same vanishing as in the computation above.
:::

This spectral sequence allows us to understand [Theorem 11](#thm11){: data-lid="07flk" } in a broader context. If on all finite intersections of $\mathcal{U}$, $\mathcal{F}$ is acyclic, then $\check{C}^\bullet(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) = 0$ holds for all $q > 0$, so on the $E_2$ page all terms with $q > 0$ vanish and we obtain $E_2^{p,0} = \check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$. That is, the Čech-to-derived functor spectral sequence is a more general result that includes [Theorem 11](#thm11){: data-lid="13man" }.

## Classification of Line Bundles

Earlier we saw that a line bundle is determined by transition functions $g_{ij} \in \mathcal{O}_X^\times(U_i \cap U_j)$ ([\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Proposition 2](/en/math/algebraic_varieties/line_bundles#prop2){: data-lid="s5ryd" }). The transition functions satisfy the cocycle condition $g_{ij}g_{jk} = g_{ik}$, which precisely corresponds to the Čech 1-cocycle condition written in multiplicative notation. Moreover, since an isomorphism of line bundles means that on each $U_i$, functions $h_i \in \mathcal{O}_X^\times(U_i)$ change the transition functions by $g_{ij} \mapsto h_i g_{ij} h_j^{-1}$, this also coincides with the equivalence relation given by Čech 1-coboundaries. That is, the isomorphism class of a line bundle corresponds naturally to an element of $\check{H}^1(X, \mathcal{O}_X^\times)$.

Making this observation precise yields the following. The point to note here is that since $\mathcal{O}_X^\times$ is a sheaf of (abelian) groups with multiplicative structure, the coboundary relation in Čech cohomology is expressed multiplicatively rather than additively. Specifically, a 1-coboundary is of the form $(g_{ij}) = (h_i \cdot h_j^{-1})$.

::: Proposition 22
$\check{H}^1(X, \mathcal{O}_X^\times) \cong \Pic(X)$.
:::

::: Proof
First we define a map from $\check{H}^1(X, \mathcal{O}_X^\times)$ to $\Pic(X)$. Given a Čech 1-cocycle $(g_{ij}) \in \check{Z}^1(\mathcal{U}, \mathcal{O}_X^\times)$, we construct a line bundle $\mathcal{L}$ with these as transition functions. To do this, we take the trivial bundle $U_i \times \mathbb{A}^1$ on each $U_i$, and glue them over $U_i \cap U_j$ by $(p, t) \mapsto (p, g_{ij}(p)t)$. Then the cocycle condition $g_{ij}g_{jk} = g_{ik}$ ensures that this gluing is consistent, so we obtain a well-defined line bundle.

On the other hand, given two cocycles equivalent by a coboundary $g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$, we can define an isomorphism between the corresponding two line bundles by $\varphi_i: \mathcal{L}\vert_{U_i} \rightarrow \mathcal{M}\vert_{U_i}$, $v \mapsto h_i^{-1} v$. Then the compatibility of $\varphi_i$ and $\varphi_j$ on $U_i \cap U_j$ can be checked from

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

and thus the map $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\times) \rightarrow \Pic(X)$ is well-defined.

Conversely, any line bundle $\mathcal{L}$ is represented by transition functions $g_{ij}$ on a suitable open cover by [§Line Bundles and Vector Bundles, ⁋Definition 1](/en/math/algebraic_varieties/line_bundles#def1){: data-lid="2et1k" }, and these form a Čech 1-cocycle. Since a line bundle isomorphism corresponds exactly to the equivalence relation by coboundaries, the kernel of this map consists of coboundaries. Therefore $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\times) \rightarrow \Pic(X)$ is injective. Taking the direct limit now yields $\check{H}^1(X, \mathcal{O}_X^\times) \cong \Pic(X)$.
:::

This proposition shows that the classification of line bundles reduces to a cohomology computation. That is, the problem of classifying elements of $\Pic(X)$ now becomes the problem of classifying $\mathcal{O}_X^\times$-valued Čech 1-cocycles, which is encouraging in that explicit computation is possible after all. In the next post [§Cohomology of Projective Space](/en/math/algebraic_varieties/cohomology_of_projective_spaces){: data-lid="ski5z" }, we compute the cohomology of the line bundle $\mathcal{O}(d)$ on $\mathbb{P}^n$.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.  
**[Wei]** C. A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38, Cambridge University Press, 1994.

---

[^1]: More generally, as seen in [\[Topology\] §Sheaves, §§Abelian Category of Sheaves](/en/math/topology/sheaves#abelian-category-of-sheaves){: data-lid="efvi0" }, the category $\Sh(X)$ of sheaves defined on an arbitrary topological space $X$ is an abelian category.
