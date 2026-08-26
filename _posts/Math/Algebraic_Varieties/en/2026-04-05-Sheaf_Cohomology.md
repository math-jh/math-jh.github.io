---
title: "Sheaf Cohomology"
description: "Beyond global sections of vector bundles, we define sheaf cohomology using derived functors to capture finer information about sheaves and explore its properties."
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/sheaf_cohomology
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-05
weight: 13
translated_at: 2026-08-18T23:45:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T23:45:04+00:00
---
We have verified that line bundles can be used to construct various invariants. For instance, in [§Line Bundles and Vector Bundles](/en/math/algebraic_varieties/line_bundles), we defined the global section space $\Gamma(X, \mathcal{L})$ of a line bundle $\mathcal{L}$. In particular, in [§Linear Systems, ⁋Definition 9](/en/math/algebraic_varieties/linear_systems#def9), we saw that the dimension of this space plays a key role in determining the dimension of the complete linear system and, further, the projective embedding of the variety.

Although we have primarily used the language of line bundles for geometric intuition, as noted right after [§Canonical Line Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1), thinking in terms of the section sheaf of a line bundle means that this can fundamentally be rephrased in the language of sheaves. In this post, we define the notion of sheaf cohomology.

## Definition as a Derived Functor

While sheaves are a powerful tool for systematically describing all the information on a topological space, they have appeared front and center in our discussion only once before: in [§Linear Systems](/en/math/algebraic_varieties/linear_systems), when we observed that the global section space $\Gamma(X, \mathcal{L})$ determines the projective embedding of the complete linear system.

However, if global sections were our only concern, there would be no need to think about sheaves at all; we could have simply considered the global section functor. In fact, the global section functor does not capture all the information contained in a sheaf. For example, consider the global section functor

$$\Gamma(X, -): \QCoh(X) \rightarrow \Vect_\mathbb{K}; \qquad \mathcal{F} \mapsto \mathcal{F}(X).$$

When we defined quasi-coherent sheaves in [§Canonical Line Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1), our motivation was that the category $\Bun(X)$ of vector bundles is not an abelian category, so we considered a larger category that adds kernels and cokernels; from this perspective, it is not surprising that $\QCoh(X)$ becomes an abelian category. [^1]

If $\Gamma(X,-)$ did not lose any information, this functor would have to be exact. That is, given a short exact sequence of (quasi-coherent) sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0,$$

applying $\Gamma(X,-)$ should also yield a short exact sequence. However, this functor is only left exact. That is, the exactness of

$$0 \rightarrow \Gamma(X, \mathcal{F}') \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{F}'')$$

is guaranteed, but the surjection

$$\Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{F}'') \rightarrow 0$$

is not guaranteed in general. For a concrete example, consider the Euler sequence

$$0 \rightarrow \Omega^1_{\mathbb{P}^n} \rightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow 0$$

([§Canonical Line Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7)). Applying $\Gamma(\mathbb{P}^n, -)$ to this short exact sequence gives

$$0 \rightarrow \Gamma(\mathbb{P}^n, \Omega^1_{\mathbb{P}^n}) \rightarrow \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) \rightarrow \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}).$$

But as we saw in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), the global sections of $\mathcal{O}_{\mathbb{P}^n}(-1)$ are zero, so

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) = 0,$$

whereas $\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})=\mathbb{K}$, so surjectivity on the right cannot hold.

The standard way to remedy this is to consider the right derived functor ([§Derived Functors, ⁋Definition 9](/en/math/homological_algebra/derived_functors#def9)). Specifically, the category $\Sh(X)$ of sheaves of abelian groups on $X$ has enough injectives, since one can take products of skyscraper sheaves built from injective abelian groups stalkwise; thus every sheaf $\mathcal{F}$ always has an injective resolution $\mathcal{I}^\bullet$, and from this we can define sheaf cohomology via

$$0 \rightarrow \Gamma(X, \mathcal{I}^0) \rightarrow \Gamma(X, \mathcal{I}^1) \rightarrow \Gamma(X, \mathcal{I}^2) \rightarrow \cdots.$$

::: Definition 1
For a sheaf $\mathcal{F}$ on a variety $X$, we define the $i$th *sheaf cohomology* $H^i(X, \mathcal{F})$ by

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1}))}{\im(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i))},$$

where $\mathcal{I}^\bullet$ is an injective resolution of $\mathcal{F}$ in $\Sh(X)$.
:::

That this is independent of the choice of $\mathcal{I}^\bullet$, and so on, all follow from standard arguments in homological algebra.

Earlier, when we introduced the global section space $\Gamma(X, \mathcal{L})$, we mentioned that one of its other popular notations is $H^0(X, \mathcal{L})$; we now see that this notation is justified by the definition above.

The following proposition is also a standard consequence of homological algebra. ([§Derived Functors](/en/math/homological_algebra/derived_functors))

::: Proposition 2
For a short exact sequence of sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0,$$

there exists a long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow \cdots.$$

Here $\delta$ is the *connecting homomorphism*.
:::

## Čech Cohomology

[Definition 1](#def1) is a rigorous definition of sheaf cohomology, but explicitly constructing an injective resolution is generally very difficult. Therefore, in actual computations, we use the Čech approach, which defines cohomology from a different perspective.

Intuitively, Čech cohomology $\check{H}^i(X, \mathcal{F})$ is a tool that measures the failure of gluing local information. That is, $\check{H}^0(X, \mathcal{F})$ is exactly the global section space, and $\check{H}^1(X, \mathcal{F})$ tells us how much the process of patching local sections together to obtain a global section fails. To make this precise, we begin with the following.

::: Definition 3
Let an open cover $\mathcal{U} = \{U_i\}_{i \in I}$ of a topological space $X$ and a sheaf $\mathcal{F}$ be given, and fix an arbitrary total order $<$ on $I$. Then the *Čech complex* $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ of this data is defined as follows:

$$\check{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p}).$$

The *coboundary map* $d: \check{C}^p \rightarrow \check{C}^{p+1}$ is defined by the formula

$$(\dd{\alpha})_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0}\cap \cdots \cap U_{i_{p+1}}}.$$

Here $\hat{i_k}$ means that the index $i_k$ is omitted.
:::

For this definition to be well-defined, that is, for $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ to actually be a complex, the coboundary map must actually be a coboundary map: we need $d^2=0$. This can be checked directly by expanding the above formula and observing the sign cancellations. Consequently, $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ is a cochain complex, and so we can make the following definition.

::: Definition 4
We define the *Čech cohomology* $\check{H}^p(\mathcal{U}, \mathcal{F})$ determined by the above data to be the cohomology of the Čech complex:

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\check{C}^\bullet(\mathcal{U}, \mathcal{F})).$$
:::

We said earlier that Čech cohomology measures the failure of gluing; this is encoded in the coboundary map. Let us examine the intuitive meaning of the coboundary map in low degrees $p = 0, 1$.

::: Example 5 ($p = 0$)
By the definition of the Čech complex, $\check{C}^0(\mathcal{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$, and the coboundary map from $\check{C}^0$ to $\check{C}^1$ is

$$(\dd{s})_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}.$$

Therefore,

$$\check{H}^0(\mathcal{U}, \mathcal{F}) = \ker(d: \check{C}^0 \rightarrow \check{C}^1) = \left\{(s_i) \in \prod_i \mathcal{F}(U_i) \mid s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\right\}.$$

By the gluing condition of [§Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1), such a family of sections coincides exactly with a section over all of $X$, that is, with $\Gamma(X, \mathcal{F})$. Hence $\check{H}^0(\mathcal{U}, \mathcal{F}) = H^0(X, \mathcal{F})$, and this is independent of the choice of open cover.
:::

We will soon show that, in favorable situations, Čech cohomology and sheaf cohomology always agree as above. For now, let us see how the $p=1$ case measures the failure of gluing.

::: Example 6 ($p = 1$)
A 1-cochain is a collection of sections $s_{ij} \in \mathcal{F}(U_i \cap U_j)$ over each $U_i \cap U_j$, and a 1-cocycle is one satisfying the cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \qquad\text{on}\quad U_i \cap U_j \cap U_k.$$

On the other hand, a 1-coboundary is one induced from a 0-cochain $(t_i)$, that is, of the form $s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$.

Thus, a nontrivial element of $\check{H}^1(\mathcal{U}, \mathcal{F})$ reflects the discrepancy that appears when trying to glue these three pieces of data $s_{ij}, s_{jk}, s_{ik}$ together, and this is precisely the failure of gluing mentioned above.
:::

So far, we have defined Čech cohomology $\check{H}^p(\mathcal{U}, \mathcal{F})$ for a single open cover $\mathcal{U}$. However, different open covers can generally give different Čech cohomologies. For example, for the cover consisting of a single open set $U_0 = X$, all intersections are $X$, so $\check{H}^p$ is nonzero only at $p = 0$. The finer the cover, the more topological information we can capture, so we need to understand the relationship between open covers and synthesize the information over all open covers. That is, we impose an order relation on *all* open covers using refinement. Then, for a refinement $\mathcal{V} = \{V_j\}_{j \in J} \preceq \mathcal{U} = \{U_i\}_{i \in I}$, choosing a function $\lambda: J \rightarrow I$ such that $V_j \subseteq U_{\lambda(j)}$ for each $j$ yields a cochain-level map $\lambda^\ast: \check{C}^p(\mathcal{U}, \mathcal{F}) \rightarrow \check{C}^p(\mathcal{V}, \mathcal{F})$ defined by

$$(\lambda^\ast\alpha)_{j_0 \cdots j_p} = \alpha_{\lambda(j_0) \cdots \lambda(j_p)}\vert_{V_{j_0} \cap \cdots \cap V_{j_p}}.$$

This map depends on the choice of $\lambda$, but for another $\mu: J \rightarrow I$ satisfying the same condition,

$$h(\alpha)_{j_0 \cdots j_{p-1}} = \sum_{k=0}^{p-1} (-1)^k \alpha_{\lambda(j_0) \cdots \lambda(j_k) \mu(j_k) \cdots \mu(j_{p-1})}\vert_{V_{j_0} \cap \cdots \cap V_{j_{p-1}}}$$

gives a chain homotopy between $\lambda^\ast$ and $\mu^\ast$, so at the cohomology level a single map $\check{H}^p(\mathcal{U}, \mathcal{F}) \rightarrow \check{H}^p(\mathcal{V}, \mathcal{F})$ is determined independent of the choice. For the same reason, these maps are compatible with composition of refinements, and hence we can define a direct system $\check{H}^p(\mathcal{U}, \mathcal{F})$ indexed by all open covers. From this we make the following definition.

::: Definition 7
We define the *Čech cohomology* of $X$ to be the direct limit over all open covers:

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathcal{U}} \check{H}^p(\mathcal{U}, \mathcal{F}).$$
:::

To explain the above argument more simply, the meaning is that we take increasingly finer open covers and amalgamate all the additional cohomology data that appears, defining this to be $\check{H}(X, \mathcal{F})$.

In general, it is not guaranteed that the $\check{H}^p(X, \mathcal{F})$ of [Definition 7](#def7) is isomorphic to the $H^p(X, \mathcal{F})$ of [Definition 1](#def1), but fortunately, for most sheaves that arise in algebraic geometry, the two coincide. Showing this requires some technical machinery.

::: Definition 8
For a sheaf $\mathcal{F}$ on a variety $X$, we define the following.

1. A sheaf $\mathcal{F}$ is called *acyclic* if $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
2. An injective object $\mathcal{F}$ of $\Sh(X)$ is called an *injective sheaf*.
3. If the restriction map $\mathcal{F}(U) \rightarrow \mathcal{F}(V)$ is surjective for every open set $V\subseteq U$, then $\mathcal{F}$ is called a *flasque sheaf*.
:::

Of course, the condition we want at the cohomology level is the first one. We first examine the relationships among the above concepts.

::: Lemma 9
An injective sheaf $\mathcal{F}$ is flasque.
:::

::: Proof
By definition, $\mathcal{F}$ being injective means that for any monomorphism $\mathcal{A} \hookrightarrow \mathcal{B}$, the map $\Hom_{\Sh(X)}(\mathcal{B}, \mathcal{F}) \rightarrow \Hom_{\Sh(X)}(\mathcal{A}, \mathcal{F})$ is surjective. ([[Homological Algebra] §Resolutions, ⁋Definition 1](/en/math/homological_algebra/resolutions#def1)) We now show that for any open sets $V \subseteq U \subseteq X$, the restriction $\mathcal{F}(U) \rightarrow \mathcal{F}(V)$ is surjective.

This map is not a sheaf morphism but a morphism of abelian groups, and since our tools are sheaf morphisms, we must recast this condition in terms of sheaf morphisms. To do this, we introduce the open embeddings

$$i^U: U \hookrightarrow X,\qquad i^V: V \hookrightarrow X$$

and the sheaves $i^U_!\mathbb{Z}_U, i^V_!\mathbb{Z}_V$ obtained by extension by zero. Here $\mathbb{Z}_U, \mathbb{Z}_V$ are constant sheaves, and since $V \subseteq U$ by assumption, there is a natural monomorphism $i^V_!\mathbb{Z}_V \rightarrow i^U_!\mathbb{Z}_U$.

First, let us verify that $\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \mathcal{F}(U)$. Since extension by zero $i^U_!$ is left adjoint to restriction $\mathcal{G} \mapsto \mathcal{G}\vert_U$ ([[Topology] §Sheaves, ⁋Example 14](/en/math/topology/sheaves#ex14)),

$$\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U)$$

holds. Now $\mathbb{Z}_U$ is the sheafification of the constant presheaf $\underline{\mathbb{Z}}$ assigning $\mathbb{Z}$ to each open set, and sheafification is left adjoint to the inclusion $\Sh(U) \rightarrow \PSh(U)$, so

$$\Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U) \cong \Hom_{\PSh(U)}(\underline{\mathbb{Z}}, \mathcal{F}\vert_U)$$

holds. However, since the restriction maps of $\underline{\mathbb{Z}}$ are all the identity on $\mathbb{Z}$, a presheaf morphism $\varphi: \underline{\mathbb{Z}} \rightarrow \mathcal{F}\vert_U$ must satisfy $\varphi_W(1) = \varphi_U(1)\vert_W$ for each $W \subseteq U$, and is thus completely determined by $\varphi_U(1) \in \mathcal{F}(U)$. Conversely, for any $s \in \mathcal{F}(U)$, defining $n \mapsto n \cdot s\vert_W$ on each $W \subseteq U$ yields a presheaf morphism. Therefore

$$\Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U) \cong \mathcal{F}(U)$$

holds. Similarly $\Hom_{\Sh(X)}(i^V_!\mathbb{Z}_V, \mathcal{F}) \cong \mathcal{F}(V)$, and by naturality the induced map between them is exactly the restriction $\mathcal{F}(U)\rightarrow \mathcal{F}(V)$. Since $\mathcal{F}$ is injective by assumption, this is surjective, completing the proof.
:::

::: Lemma 10
A flasque sheaf $\mathcal{F}$ is Čech-acyclic for any open cover $\mathcal{U}$. That is, $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for all $p > 0$.
:::

::: Proof
Let us lift the Čech complex to the sheaf level. That is, for each open set $V \subseteq X$, define the sheaf $\mathcal{C}^p$ by

$$\mathcal{C}^p(V) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(V \cap U_{i_0} \cap \cdots \cap U_{i_p})$$

Then by definition $\Gamma(X, \mathcal{C}^p) = \check{C}^p(\mathcal{U}, \mathcal{F})$, and the Čech coboundary map is defined by the same formula on each $V$, giving a sheaf morphism $\mathcal{C}^p \rightarrow \mathcal{C}^{p+1}$. Also, taking the collection of restrictions $\epsilon : \mathcal{F} \rightarrow \mathcal{C}^0$ as the augmentation, we obtain the complex

$$0 \rightarrow \mathcal{F} \xrightarrow{\epsilon} \mathcal{C}^0 \xrightarrow{d^0} \mathcal{C}^1 \xrightarrow{d^1} \cdots$$

What we need to show is that applying $\Gamma(X,-)$ to this yields exactness at $p>0$.

First, let us show that this complex itself is exact. Fix an index $i_0 \in I$ and consider only open sets $V \subseteq U_{i_0}$. Then for each $t \in \mathcal{C}^p(V)$, we obtain a map $s^p : \mathcal{C}^p(V) \rightarrow \mathcal{C}^{p-1}(V)$ defined by

$$s^p(t)_{j_0 < \cdots < j_{p-1}} = t_{i_0 j_0 \cdots j_{p-1}}\tag{$\ast$}$$

The right-hand side is a section over $V \cap U_{i_0} \cap U_{j_0} \cap \cdots \cap U_{j_{p-1}}$, but since $V \subseteq U_{i_0}$, this set equals $V \cap U_{j_0} \cap \cdots \cap U_{j_{p-1}}$, which is where the left-hand side should live; thus no extension is involved in formula ($\ast$). That this $s^p$ gives a chain homotopy can be checked by direct computation: in $d^{p-1}s^p$ the term omitting $i_0$ and in $s^{p+1}d^p$ the term inserting $i_0$ cancel with opposite signs. Hence the complex of sections over such $V$ is exact, and since $\mathcal{U}$ covers $X$, every point has such a neighborhood $V$, giving exactness at every stalk. A slight technical issue is that the fixed index $i_0$ might appear among $j_0<\cdots< j_{p-1}$. To handle this, we use the *non-alternating* Čech complex with coordinates given by $p+1$ elements $i_0,\ldots, i_p\in I$ of $I$, instead of the usual Čech complex. This is quasi-isomorphic to the original Čech complex, so this detour is justified.

Now we use the assumption that $\mathcal{F}$ is flasque. The restriction map of each $\mathcal{C}^p$ is a product of restriction maps of $\mathcal{F}$, hence surjective, so $\mathcal{C}^p$ is also flasque. Thus $\mathcal{C}^\bullet$ is a flasque resolution of $\mathcal{F}$, and by [Proposition 16](#prop16) each term is $\Gamma(X,-)$-acyclic, while by [Proposition 17](#prop17)

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\Gamma(X, \mathcal{C}^\bullet)) \cong H^p(X, \mathcal{F})$$

Since $\mathcal{F}$ is flasque, the right-hand side vanishes for $p>0$ by [Proposition 16](#prop16). The proofs of the two propositions used here do not depend on this lemma.
:::

::: Theorem 11 (Leray)
For a sheaf $\mathcal{F}$ on a topological space $X$ and an open cover $\mathcal{U} = \{U_i\}$, if $\mathcal{F}$ is acyclic on every finite intersection

$$U_{i_0 \cdots i_p}=U_{i_0}\cap \cdots\cap U_{i_p}$$

then there is an isomorphism

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \rightarrow H^p(X, \mathcal{F})$$
:::

::: Proof
Fix an injective resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^0 \rightarrow \mathcal{I}^1 \rightarrow \cdots$ of $\mathcal{F}$, and form the double complex

$$K^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q)$$

In this double complex, the horizontal differential $d_h$ is the Čech differential, and the vertical differential $d_v$ comes from the injective resolution. As we saw in [[Homological Algebra] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11), the two filtrations on the total complex $\Tot(K)^\bullet$

$$F_v^p\Tot(K)^\bullet,\qquad F_h^p\Tot(K)^\bullet$$

converge to the same filtered homology $H^\bullet(\Tot(K))$.

Consider the spectral sequences given by each filtered complex. First, for the vertical filtration, the $E_1$ page has $E_1^{p,q} = H^q(K^{p,\bullet})$, where $K^{p,\bullet} = \check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$. Now $\check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$, looking at each component, restricts the injective resolution to each intersection $U_{i_0 \cdots i_p}$ and then takes cohomology, so it equals the $q$-th sheaf cohomology of $\mathcal{F}$ on $U_{i_0\cdots i_p}$; hence by the acyclicity assumption $E_1^{p,q}=0$ for all $q>0$. Also, by definition $E_1^{p,0}=\check{C}^p(\mathcal{U}, \mathcal{F})$. The $E_2$ page is then the cohomology of $E_1^{p,0}$ with respect to the horizontal differential $d_h$, so

$$E_2^{p,q}=\begin{cases}\check{H}^p(\mathcal{U}, \mathcal{F})&\text{$q=0$}\\0&\text{otherwise}\end{cases}$$

and $E_2^{p,q}=E_\infty^{p,q}$.

Now consider the horizontal filtration direction. On the $E_1$ page, $E_1^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{I}^q)$. But by [Lemma 9](#lem9) and [Lemma 10](#lem10) above, injective sheaves are Čech-acyclic, so $E_1^{p,q} = 0$ for $p > 0$, and the remaining cohomology with respect to the vertical differential at $p=0$ is sheaf cohomology, so

$$E_2^{p,q}=\begin{cases}H^q(X, \mathcal{F})&\text{$p=0$}\\0&\text{otherwise}\end{cases}$$

and $E_2^{p,q}=E_\infty^{p,q}$. Since the two spectral sequences converge to the same $H^\bullet(\Tot(K))$, we obtain

$$\check{H}^n(\mathcal{U}, \mathcal{F}) \cong H^n(X, \mathcal{F})$$
:::

Then the only obstacle to our intuition is how demanding this acyclicity condition is, but fortunately it is a more generous condition than one might think.

::: Proposition 12
For a quasi-coherent sheaf $\mathcal{F} = \widetilde{M}$ on an affine variety $X$, we have $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
:::

The proof of this is as follows: letting $A$ be the coordinate ring of $X$, if we find an injective resolution $I^\bullet$ of $M$ in the category $\lMod{A}$, this gives a resolution $\widetilde{I^\bullet}$ of sheaves on $X$, and since $A$ is a finitely generated $\mathbb{K}$-algebra it is Noetherian, and the sheaf given by an injective module over a Noetherian ring is always flasque, so by [Proposition 16](#prop16) and [Proposition 17](#prop17) below this flasque resolution computes $H^i(X, \mathcal{F})$. The proofs of the two propositions cited here do not use this proposition.

Now consider an arbitrary variety $X$ and a quasi-coherent sheaf $\mathcal{F}$ defined on it, and suppose an affine open cover $\mathcal{U}$ of $X$ is given. For these data to satisfy the hypotheses of [Theorem 11](#thm11), every finite intersection of members of $\mathcal{U}$ must again be affine. If the diagonal

$$\Delta_X\hookrightarrow X\times X$$

is a *closed* embedding in $X\times X$, then we can show that this condition holds, and in this case we call $X$ a *separated* variety. As can be seen from its definition, this is the Zariski topology analogue of the Hausdorff condition, and is a reasonable condition; moreover, if we define a variety to be quasi-projective as we do now, this condition is automatically satisfied. Thus, in our present language, this argument shows that for any quasi-coherent sheaf on any variety, Čech cohomology and sheaf cohomology agree, and moreover, if we choose an open cover $\mathcal{U}$ satisfying the hypotheses of [Theorem 11](#thm11), it suffices to compute the Čech cohomology for that open cover without taking a direct limit.

## Godement Resolution

In [Definition 1](#def1) we defined sheaf cohomology via injective resolution, but since injective resolutions are generally difficult to compute directly, we examined one solution: using the result of [Theorem 11](#thm11) that Čech cohomology and sheaf cohomology are isomorphic.

The Godement resolution, which we examine in this section, also starts from the same problem. That is, computing sheaf cohomology in general is a very complicated task, so [Definition 1](#def1) is conceptually clean but somewhat lacking in practicality. We now define a concrete resolution. It is not an injective resolution, but it is a flasque resolution, and for our purposes this is sufficient.

::: Definition 13
For a sheaf $\mathcal{F}$ on a topological space $X$, the *Godement sheaf* $C^0(\mathcal{F})$ is defined for each open set $U \subseteq X$ by

$$C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x$$

where $\mathcal{F}_x$ is the stalk of $\mathcal{F}$ at $x$.
:::

Then for each $x\in X$, the identity $\mathcal{F}_x\rightarrow \mathcal{F}_x$ on the stalk gives a well-defined canonical morphism $\mathcal{F}\rightarrow C^0(\mathcal{F})$. Also, that $C^0(\mathcal{F})$ is a sheaf is almost obvious.

Intuitively, $C^0(\mathcal{F})$ can be thought of as the collection of functions choosing an element of $\mathcal{F}_x$ at each point $x\in X$ with no constraints whatsoever; from this perspective it is sometimes called the *sheaf of discontinuous sections*. The following is a basic property of this sheaf.

::: Proposition 14
The Godement sheaf $C^0(\mathcal{F})$ is a flasque sheaf. Moreover, $\mathcal{F} \mapsto C^0(\mathcal{F})$ is an exact functor.
:::

::: Proof
First we show that the given sheaf is flasque. For open sets $V \subseteq U$, the restriction map $C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x \rightarrow \prod_{x \in V} \mathcal{F}_x = C^0(\mathcal{F})(V)$ is a projection, hence surjective. Therefore $C^0(\mathcal{F})$ is flasque.

Exactness is obvious because the stalk functor $\mathcal{F} \mapsto \mathcal{F}_x$ is exact and $C^0(\mathcal{F})$ is merely a product of stalks.
:::

Now consider the cokernel exact sequence induced by the canonical map $0\rightarrow\mathcal{F}\rightarrow C^0(\mathcal{F})$:

$$0\rightarrow \mathcal{F}\rightarrow C^0(\mathcal{F})\rightarrow \mathcal{Q}^1\rightarrow 0$$

Intuitively, $\mathcal{Q}^1$ collects the purely discontinuous parts, and from this perspective, repeating this construction captures finer and finer information about discontinuity. That is, applying $C^0$ to the sheaf $\mathcal{Q}^1$, we obtain the next cokernel exact sequence

$$0 \rightarrow \mathcal{Q}^1\rightarrow C^0(\mathcal{Q}^1)\rightarrow\mathcal{Q}^2\rightarrow 0$$

and by splicing we obtain the complex

$$0 \rightarrow C^0(\mathcal{F}) \rightarrow C^0(\mathcal{Q}^1) \rightarrow C^0 (\mathcal{Q}^2)\rightarrow \cdots$$

We call this complex the *Godement resolution* of $\mathcal{F}$, and denote its terms by

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{G}^0(\mathcal{F}) \rightarrow \mathcal{G}^1(\mathcal{F}) \rightarrow \cdots$$

Then by [Proposition 14](#prop14) the following holds.

::: Proposition 15
The Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ is a flasque resolution of $\mathcal{F}$.
:::

The most essential advantage of this construction is that no choices are made in the process, so in some sense it is canonical. This can also be seen again from the functoriality of the Godement resolution: in general, to show functoriality in sheaf cohomology one must use the argument that a sheaf morphism at the $0$-th stage of an augmented complex induces sheaf morphisms at stages $i>0$ giving a chain map, and such chain maps are the same up to chain homotopy equivalence, hence induce the same map on cohomology. ([[Homological Algebra] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6)) However, for the Godement resolution, the maps are induced purely at the chain level without any equivalence of any kind. Nevertheless, the Godement resolution exactly captures the information of sheaf cohomology.

To show this, we first prove more generally that a flasque resolution gives the same sheaf cohomology as an injective resolution. For this we first show the following.

::: Proposition 16
A flasque sheaf $\mathcal{F}$ is $\Gamma(X, -)$-acyclic. That is, $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
:::

::: Proof
We proceed by induction on $i$. First, let us treat the case $i=1$. To this end, embed $\mathcal{F}$ into an injective sheaf $\mathcal{I}$ and consider the cokernel exact sequence

$$0 \rightarrow \mathcal{F}\rightarrow\mathcal{I}\rightarrow\mathcal{Q}\rightarrow0$$

Our claim is that for any open set $V$, the map $\mathcal{I}(V)\rightarrow \mathcal{Q}(V)$ is surjective, and that $\mathcal{Q}$ is therefore flasque as well. The latter follows from the former by a diagram chase in the following commutative diagram for arbitrary open sets $V\subseteq U$:

{% diagram Math/Algebraic_Varieties/Sheaf_Cohomology-1.svg width="23.07em" alt="Commutative diagram" %}

Here $\mathcal{F}$ is flasque by hypothesis, and $\mathcal{I}$ is injective, hence flasque. Now for any $s\in \mathcal{Q}(V)$, the surjectivity we claimed allows us to lift $s$ to some $t\in \mathcal{I}(V)$; using again that $\mathcal{I}$ is flasque, we extend $t$ to $\overline{t}\in\mathcal{I}(U)$ and push it down to $\mathcal{Q}$ to define $\overline{s}\in \mathcal{Q}(U)$. Since $\overline{t}$ extends $t$, we have $\overline{t}\vert_V=t$, and hence $\overline{s}\vert_V$ equals the image of $t$ in $\mathcal{Q}(V)$, namely $s$. Thus $\overline{s}$ restricts exactly to $s\in \mathcal{Q}(V)$, yielding the flasqueness of $\mathcal{Q}$.

Now apply $\Gamma(X, -)$ to obtain the long exact sequence

$$0 \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{Q}) \xrightarrow{\delta} H^1(X, \mathcal{F}) \rightarrow H^1(X, \mathcal{I}) = 0$$

Since $\mathcal{I}$ is injective, $H^1(X, \mathcal{I}) = 0$. Therefore

$$H^1(X, \mathcal{F}) \cong \coker(\Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{Q}))$$

and to see that this vanishes we must show that $\Gamma(X, \mathcal{I})\rightarrow \Gamma(X, \mathcal{Q})$ is surjective. We prove this for an arbitrary open set. That is, let $U\subseteq X$ be open and $s\in \mathcal{Q}(U)$ be given; consider the collection $P$ of pairs $(V, t)$ where $V$ is an open subset of $U$ and $t\in \mathcal{I}(V)$ maps to $s\vert_V$ in $\mathcal{Q}(V)$. Define $(V, t)\leq (V', t')$ by $V\subseteq V'$ and $t'\vert_V=t$; then $P$ becomes a partially ordered set. Since $\mathcal{I}\rightarrow \mathcal{Q}$ is surjective at the stalk level, there exists a lift of $s$ over a suitable neighborhood of each point, so $P$ is non-empty; moreover, the $t$'s belonging to a chain in $P$ agree on overlaps, so by the gluing axiom for $\mathcal{I}$ they patch together to give an upper bound for that chain. Hence by Zorn's lemma $P$ admits a maximal element $(V, t)$.

It remains to show that $V=U$. If there existed $x\in U\setminus V$, we could choose a neighborhood $W\subseteq U$ of $x$ and $t'\in \mathcal{I}(W)$ mapping to $s\vert_W$. Then $t\vert_{V\cap W}-t'\vert_{V\cap W}$ vanishes in $\mathcal{Q}(V\cap W)$, so it comes from some $f\in \mathcal{F}(V\cap W)$; because $\mathcal{F}$ is flasque, we can extend this to $\widetilde{f}\in \mathcal{F}(W)$. Replacing $t'$ by $t'+\widetilde{f}$ gives another lift of $s\vert_W$ which agrees with $t$ on $V\cap W$, so the two patch to a lift of $s$ over $V\cup W$. This contradicts the maximality of $(V, t)$, and therefore $V=U$. In particular, the case $U=X$ is the surjectivity of $\Gamma(X, \mathcal{I})\rightarrow \Gamma(X, \mathcal{Q})$ that we needed, and at the same time we obtain the flasqueness of $\mathcal{Q}$ deferred above.

Finally, for $i\geq 2$, the terms $H^{i-1}(X, \mathcal{I})$ and $H^i(X, \mathcal{I})$ flanking the desired group vanish by the injectivity of $\mathcal{I}$, so

$$H^i(X, \mathcal{F})\cong H^{i-1}(X, \mathcal{Q})$$

and since $\mathcal{Q}$ is flasque, the desired result follows by induction.
:::

In particular, by [Proposition 16](#prop16), each term $\mathcal{G}^p(\mathcal{F})$ of the Godement resolution is flasque, hence $\Gamma(X, -)$-acyclic. That is, $H^i(X, \mathcal{G}^p(\mathcal{F})) = 0$ for all $i > 0$. To reach our conclusion, the result we need is the following.

::: Proposition 17 (Acyclic Resolution)
Given a $\Gamma(X, -)$-acyclic resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{A}^0 \rightarrow \mathcal{A}^1 \rightarrow \cdots$, we have

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(X, \mathcal{F})$$

for all $q \geq 0$.
:::

::: Proof
Fix an injective resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$ of $\mathcal{F}$. By [\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6), there exists a chain map $f\colon \mathcal{A}^\bullet \rightarrow \mathcal{I}^\bullet$ between the acyclic resolution and the injective resolution. Consider the *mapping cone* $C(f)^\bullet$ of $f$. In each degree,

$$C(f)^n = \mathcal{A}^{n+1} \oplus \mathcal{I}^n$$

and since $\mathcal{I}^n$ is injective, it is flasque by [Lemma 9](#lem9), hence in particular $\Gamma(X, -)$-acyclic. Therefore, looking at the canonical short exact sequence

$$0 \rightarrow \mathcal{I}^n \rightarrow C(f)^n \rightarrow \mathcal{A}^{n+1} \rightarrow 0$$

the two outer terms are $\Gamma(X, -)$-acyclic, so from the long exact sequence we see that $C(f)^n$ is also $\Gamma(X, -)$-acyclic.

On the other hand, $f$ is a quasi-isomorphism, so $C(f)^\bullet$ is an exact complex. ([\[Homological Algebra\] §Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9)) Moreover, as observed above, $C(f)^\bullet$ is $\Gamma(X,-)$-acyclic, so applying $\Gamma(X,-)$ yields an exact complex $\Gamma(X, C(f)^\bullet)$; applying [\[Homological Algebra\] §Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9) again, this translates into the condition that the chain map

$$\Gamma(X, f)\colon \Gamma(X, \mathcal{A}^\bullet) \rightarrow \Gamma(X, \mathcal{I}^\bullet)$$

is a quasi-isomorphism. From this we obtain

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(\Gamma(X, \mathcal{I}^\bullet)) = H^q(X, \mathcal{F})$$

as desired.
:::

Together with [Proposition 16](#prop16), [Proposition 17](#prop17) guarantees that the Godement resolution is indeed sufficient for computing sheaf cohomology. That is, the cohomology of the complex $\Gamma(X, \mathcal{G}^\bullet(\mathcal{F}))$ obtained by taking global sections of the flasque resolution $\mathcal{G}^\bullet(\mathcal{F})$ agrees with $H^\bullet(X, \mathcal{F})$.

## Spectral Sequence

One of the most powerful applications of sheaf cohomology is the computation of cohomology via spectral sequences. In this section we conclude the post with concrete calculations. The propositions introduced now hold in a general topological setting, but since we mainly have in mind applications to varieties and quasi-coherent sheaves, we place them in this category.

Fix a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$. Then from [\[Topology\] §Sheaves, ⁋Lemma 11](/en/math/topology/sheaves#lem11) and [\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9) we know that the direct image functor $f_\ast: \Sh(X)\rightarrow \Sh(Y)$ is left exact. Hence, just as in [\[Homological Algebra\] §Derived Functors](/en/math/homological_algebra/derived_functors), we can define the right derived functors of $f_\ast$ by

$$R^q f_\ast \mathcal{F} := H^q(f_\ast \mathcal{I}^\bullet)$$

where $\mathcal{I}^\bullet$ is an injective resolution of $\mathcal{F}$. By definition, $R^0 f_\ast \mathcal{F}=f_\ast \mathcal{F}$ when $q=0$, and if $\mathcal{F}$ is injective then $\mathcal{F}$ itself forms an injective resolution, so $R^qf_\ast \mathcal{F}=0$ for all $q>0$.

Now consider the Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ of $\mathcal{F}$. Intuitively, what we would like to do is to choose an injective resolution for each $\mathcal{G}^p(\mathcal{F})$, and then use [\[Homological Algebra\] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6) to define the horizontal differentials from the differentials $\mathcal{G}^p(\mathcal{F})\rightarrow \mathcal{G}^{p+1}(\mathcal{F})$ of the Godement resolution.

::: Definition 18 (Cartan-Eilenberg Resolution)
In an abelian category, a *Cartan-Eilenberg resolution* of a cochain complex $K^\bullet$ is the data consisting of a double complex $I^{p,q}$ and an augmentation $K^\bullet \rightarrow I^{\bullet,0}$ satisfying the following conditions.

1. Each column $I^{p,\bullet}$ is an injective resolution of $K^p$.
2. The cohomology $H^p(I^{\bullet,q})$ of each row forms an injective resolution of $H^p(K^\bullet)$. That is, the chain complex

    $$0 \rightarrow H^p(K^\bullet) \rightarrow H^p(I^{\bullet,0}) \rightarrow H^p(I^{\bullet,1}) \rightarrow \cdots$$

    is an injective resolution of $H^p(K^\bullet)$.
3. Likewise, for each $p$, the complexes $B^p(I^{\bullet,q})$ and $Z^p(I^{\bullet,q})$ arranged along $q$ form injective resolutions of $B^p(K^\bullet)$ and $Z^p(K^\bullet)$, respectively.
:::

The heart of this definition is that the intuition described above is not enough to produce a Cartan-Eilenberg resolution; in particular, the requirement that the cohomology of each row form a horizontal resolution of $H^p(K^\bullet)$ is a key ingredient in the existence proof. We do not prove the existence of Cartan-Eilenberg resolutions separately here, but it can be obtained essentially by repeatedly applying [\[Homological Algebra\] §Resolutions, ⁋Lemma 7](/en/math/homological_algebra/resolutions#lem7).

Meanwhile, the third condition ensures that the two short exact sequences of each row,

$$0\rightarrow Z^p(I^{\bullet,q})\rightarrow I^{p,q}\rightarrow B^{p+1}(I^{\bullet,q})\rightarrow 0$$

$$0\rightarrow B^p(I^{\bullet,q})\rightarrow Z^p(I^{\bullet,q})\rightarrow H^p(I^{\bullet,q})\rightarrow 0$$

have left-hand terms $Z^p(I^{\bullet,q})$ and $B^p(I^{\bullet,q})$ injective, so both sequences split and each row decomposes into a direct sum of injective objects; this is the reason why a left exact functor commutes with row-wise cohomology below.

Now fix a Cartan-Eilenberg resolution $\mathcal{I}^{p,q}$ of the complex $f_\ast\mathcal{G}^\bullet(\mathcal{F})$. Then by definition each column $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast\mathcal{G}^p(\mathcal{F})$, and the horizontal cohomology $H^p(\mathcal{I}^{\bullet,q})$ of each row forms an injective resolution of $H^p(f_\ast\mathcal{G}^\bullet(\mathcal{F})) = R^p f_\ast\mathcal{F}$.

Since this spectral sequence lies in the first quadrant, we know that it converges to the cohomology of the total complex $\Tot(\mathcal{I})^\bullet$. For the concrete computation, let us filter by the Godement index $p$. Then we can first write the $E_1$ page as

$$\mathcal{H}^{p,q} := H^p(\mathcal{I}^{\bullet, q})$$

Here the vertical differential is the morphism $\mathcal{H}^{p,q}\rightarrow \mathcal{H}^{p,q+1}$ induced by the differential of the injective resolution at the cohomology level, and the $E_2$ page is the cohomology sheaf of this vertical complex:

$$E_2^{p,q} = H^q(\mathcal{H}^{p,\bullet})$$

On the other hand, since $\mathcal{I}^{\bullet,\bullet}$ is a Cartan resolution, we know that each $\mathcal{H}^{p,\bullet}$ is an injective resolution of $R^p f_\ast \mathcal{F}$.

Now consider the spectral sequence arising from the filtration in the $q$ direction; its $E_1$ page is given by

$$E_1^{p,q} = H^q(\mathcal{I}^{p,\bullet})$$

Since for each $p$, the complex $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast \mathcal{G}^p(\mathcal{F})$, the exactness of injective resolutions yields

$$E_1^{p,q} = \begin{cases} f_\ast \mathcal{G}^p(\mathcal{F}) & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

and the $d_1$-differential is the morphism from $E_1^{p,0} = f_\ast \mathcal{G}^p(\mathcal{F})$ to $E_1^{p+1,0} = f_\ast \mathcal{G}^{p+1}(\mathcal{F})$, corresponding to the differential $f_\ast \mathcal{G}^p(\mathcal{F}) \rightarrow f_\ast \mathcal{G}^{p+1}(\mathcal{F})$ of the Godement resolution. Thus the $E_2$ page is the cohomology sheaf of the complex

$$0 \rightarrow f_\ast \mathcal{G}^0(\mathcal{F}) \rightarrow f_\ast \mathcal{G}^1(\mathcal{F}) \rightarrow \cdots$$

and by the definition of $R^q f_\ast$ this is given by

$$E_2^{p,q} = \begin{cases} R^p f_\ast \mathcal{F} & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

Hence we know that the cohomology of the total complex of $\mathcal{I}^{\bullet,\bullet}$ must converge to $R^n f_\ast \mathcal{F}$.

Now let us revisit the above discussion after applying the global section functor $\Gamma(Y,-)$. That is, we consider the double complex

$$\mathcal{J}^{p,q}=\Gamma(Y, \mathcal{I}^{p,q})$$

and its total complex $\Tot(\mathcal{J})^\bullet$. Then by the same computation as above, the filtration in the $p$ direction gives on the $E_1$ page

$$E_1^{p,q}=H^p(\mathcal{J}^{\bullet, q})=\Gamma(Y, \mathcal{H}^{p,q})$$

Here the second equality holds because, by the third condition of [Definition 18](#def18), each row splits into injective objects so that $\Gamma(Y,-)$ commutes with row-wise cohomology. Moreover, since $\mathcal{H}^{p,q}$ is an injective resolution of $R^pf_\ast \mathcal{F}$, its cohomology comes out as $H^q(Y, R^p f_\ast \mathcal{F})$.

On the other hand, for the filtration in the $q$ direction, the $E_1$ page is

$$E_1^{p,q}=H^q(\Gamma(Y, \mathcal{I}^{p,\bullet}))$$

and since each $\mathcal{I}^{p,\bullet}$ is, by definition of a Cartan-Eilenberg resolution, an injective resolution of $f_\ast \mathcal{G}^p(\mathcal{F})$, we have $E_1^{p,q}=H^q(Y, f_\ast \mathcal{G}^p(\mathcal{F}))$. Now $\mathcal{G}^p(\mathcal{F})$ is flasque and $f_\ast$ preserves flasqueness, so $f_\ast \mathcal{G}^p(\mathcal{F})$ is also flasque; hence by [Proposition 16](#prop16) the terms with $q>0$ vanish, leaving only

$$E_1^{p,0}=\Gamma(Y, f_\ast \mathcal{G}^p (\mathcal{F}))=\Gamma(X, \mathcal{G}^p(\mathcal{F}))$$

with the Godement differential. Therefore the $E_2$ page is

$$E_2^{n,0}=H^n(\Gamma(X, \mathcal{G}^\bullet(\mathcal{F})))=H^n(X, \mathcal{F})$$

Meanwhile, the $E_2$ page from the filtration in the $p$ direction was $E_2^{p,q}=H^q(Y, R^p f_\ast \mathcal{F})$, so in what follows we shall follow standard notation and interchange the names of the two indices. The spectral sequence obtained in this way is called the *Leray spectral sequence*, and thus we obtain the following.

::: Proposition 19 (Leray Spectral Sequence)
For a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$, there exists a spectral sequence with the following $E_2$ page.

$$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F}).$$
:::

Geometrically, this is most transparent when $f:X\rightarrow Y$ is a fibration. In this case, what the spectral sequence says is that to compute cohomology on $X$, we first compute cohomology on $Y$, then remember the cohomology on each fiber as the higher sheaf $R^q f_\ast \mathcal{F}$, and finally assemble these over $Y$.

In the lowest dimensions of the Leray spectral sequence, we obtain the following exact sequence.

::: Corollary 20 (Five-Term Exact Sequence)
For a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$, the Leray spectral sequence yields the exact sequence

$$0 \rightarrow H^1(Y, f_\ast \mathcal{F}) \rightarrow H^1(X, \mathcal{F}) \rightarrow H^0(Y, R^1 f_\ast \mathcal{F}) \overset{d_2}{\rightarrow} H^2(Y, f_\ast \mathcal{F}) \rightarrow H^2(X, \mathcal{F}).$$
:::

::: Proof
Consider the terms with $p+q \leq 2$ on the $E_2$ page of the Leray spectral sequence $E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$. By [\[Homological Algebra\] §Spectral Sequences, ⁋Definition 5](/en/math/homological_algebra/spectral_sequences#def5), we know that

$$E_\infty^{p,q} \cong \gr^p H^{p+q} = F^p H^{p+q}/F^{p+1}H^{p+q}.$$

In particular, since this is a first quadrant spectral sequence, we have $E_r^{p,q} = E_\infty^{p,q}$ for sufficiently large $r$. ([\[Homological Algebra\] §Spectral Sequences, ⁋Proposition 6](/en/math/homological_algebra/spectral_sequences#prop6))

First, looking at the components with $p+q = 1$, there are only two terms $E_2^{1,0}$ and $E_2^{0,1}$. Considering degrees, all differentials into or out of $E_2^{1,0}$ are zero, so $E_2^{1,0} = E_\infty^{1,0}$. On the other hand, the $d_2$ from $E_2^{0,1}$ to $E_2^{2,0}$ may be nontrivial, so $E_\infty^{0,1} = \ker(d_2: E_2^{0,1} \rightarrow E_2^{2,0})$. Then by the filtration,

$$0 \rightarrow E_\infty^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_\infty^{0,1} \rightarrow 0$$

is exact, and since $E_\infty^{1,0} = E_2^{1,0}$ and $E_\infty^{0,1} = \ker(d_2) \hookrightarrow E_2^{0,1}$, combining these gives the exact sequence

$$0 \rightarrow E_2^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}.$$

To complete the proof, we now look at the components $E_2^{2,0}$, $E_2^{1,1}$, $E_2^{0,2}$ with $p+q = 2$. For the same reason, $d_2 : E_2^{0,1} \rightarrow E_2^{2,0}$ is the only possibly nontrivial differential, and on the $E_3$ page defined by this differential,

$$E_3^{0,2} = \ker(d_2 : E_2^{0,2} \rightarrow E_2^{2,1}), \qquad E_3^{2,0} = \coker(d_2 : E_2^{0,1} \rightarrow E_2^{2,0})$$

and again analyzing degrees, $E_3^{p,q} = E_\infty^{p,q}$, so

$$E_\infty^{2,0} = E_3^{2,0} = \coker(d_2 : E_2^{0,1} \rightarrow E_2^{2,0}).$$

We have shown so far that the exact sequence

$$0 \rightarrow E_2^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

exists, and from the above computation,

$$E_\infty^{2,0} = E_3^{2,0} = \coker(d_2: E_2^{0,1} \rightarrow E_2^{2,0})$$

so inserting this via the filtration as $F^2 H^2 \hookrightarrow H^2(X, \mathcal{F})$,

$$E_2^{0,1} \overset{d_2}{\rightarrow} E_2^{2,0} \rightarrow H^2(X, \mathcal{F})$$

is exact. Combining these gives the desired result.
:::

This exact sequence shows what constraints the existence of the $d_2$-differential imposes on cohomology computations, and in good cases it justifies the intuition that $H^i(X, \mathcal{F}) \cong H^i(Y, f_\ast \mathcal{F})$.

Finally, we can describe the relation between Čech cohomology and derived functor cohomology via a spectral sequence.

::: Proposition 21 (Čech-to-Derived Functor Spectral Sequence)
For a sheaf $\mathcal{F}$ on a topological space $X$ and an open cover $\mathcal{U}$, there exists a spectral sequence

$$E_2^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) \Rightarrow H^{p+q}(X, \mathcal{F}).$$

Here $\mathcal{H}^q(\mathcal{F})$ is the presheaf $U \mapsto H^q(U, \mathcal{F})$.
:::

::: Proof
Take the Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ of $\mathcal{F}$ and form the double complex $C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{G}^q(\mathcal{F}))$. That the two spectral sequences obtained from the two filtrations converge to the same total cohomology $H^{p+q}(X, \mathcal{F})$ follows from [\[Homological Algebra\] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11), and since the Godement sheaf $\mathcal{G}^q(\mathcal{F})$ is flasque, it is Čech-acyclic by [Lemma 10](#lem10), so the same vanishing as in the computation above applies.
:::

This spectral sequence allows us to understand [Theorem 11](#thm11) in a broader context. If $\mathcal{F}$ is acyclic on all finite intersections of $\mathcal{U}$, then $\check{C}^\bullet(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) = 0$ for all $q > 0$, so all terms with $q > 0$ vanish on the $E_2$ page and we obtain $E_2^{p,0} = \check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$. That is, the Čech-to-derived functor spectral sequence is a more general result that includes [Theorem 11](#thm11).

## Classification of Line Bundles

Earlier we saw that a line bundle is determined by transition functions $g_{ij} \in \mathcal{O}_X^\times(U_i \cap U_j)$ ([\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Proposition 2](/en/math/algebraic_varieties/line_bundles#prop2)). The transition functions satisfy the cocycle condition $g_{ij}g_{jk} = g_{ik}$, which precisely corresponds to the Čech 1-cocycle condition written in multiplicative notation. Moreover, an isomorphism of line bundles changes the transition function by $g_{ij} \mapsto h_i g_{ij} h_j^{-1}$ via functions $h_i \in \mathcal{O}_X^\times(U_i)$ on each $U_i$, which also matches the equivalence relation given by Čech 1-coboundaries. That is, the isomorphism class of a line bundle corresponds naturally to an element of $\check{H}^1(X, \mathcal{O}_X^\times)$.

Making this observation precise yields the following. The point to note is that since $\mathcal{O}_X^\times$ is a sheaf of (abelian) groups with multiplicative structure, the coboundary relation in Čech cohomology is expressed multiplicatively rather than additively. Specifically, a 1-coboundary is of the form $(g_{ij}) = (h_i \cdot h_j^{-1})$.

::: Proposition 22
$\check{H}^1(X, \mathcal{O}_X^\times) \cong \Pic(X)$.
:::

::: Proof
First we define a map from $\check{H}^1(X, \mathcal{O}_X^\times)$ to $\Pic(X)$. Given a Čech 1-cocycle $(g_{ij}) \in \check{Z}^1(\mathcal{U}, \mathcal{O}_X^\times)$, we construct a line bundle $\mathcal{L}$ with these as transition functions. To do this, we take the trivial bundle $U_i \times \mathbb{A}^1$ on each $U_i$, and glue them over $U_i \cap U_j$ by $(p, t) \mapsto (p, g_{ij}(p)t)$. Then the cocycle condition $g_{ij}g_{jk} = g_{ik}$ ensures that this gluing is consistent, so we obtain a well-defined line bundle.

On the other hand, given two cocycles equivalent by a coboundary $g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$, we can define an isomorphism between the corresponding two line bundles by $\varphi_i: \mathcal{L}\vert_{U_i} \rightarrow \mathcal{M}\vert_{U_i}$, $v \mapsto h_i^{-1} v$. Then the compatibility of $\varphi_i$ and $\varphi_j$ on $U_i \cap U_j$ can be checked from

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

and thus the map $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\times) \rightarrow \Pic(X)$ is well-defined.

Conversely, any line bundle $\mathcal{L}$ is represented by transition functions $g_{ij}$ on a suitable open cover by [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 1](/en/math/algebraic_varieties/line_bundles#def1), and these form a Čech 1-cocycle. Since a line bundle isomorphism corresponds exactly to the equivalence relation by coboundaries, the kernel of this map consists of coboundaries. Therefore $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\times) \rightarrow \Pic(X)$ is injective. Taking the direct limit now yields $\check{H}^1(X, \mathcal{O}_X^\times) \cong \Pic(X)$.
:::

This proposition shows that the classification of line bundles reduces to a cohomology computation. That is, the problem of classifying elements of $\Pic(X)$ now becomes the problem of classifying $\mathcal{O}_X^\times$-valued Čech 1-cocycles, which is encouraging in that explicit computation is possible after all. In the next post [§Cohomology of Projective Space](/en/math/algebraic_varieties/cohomology_of_projective_spaces), we compute the cohomology of the line bundle $\mathcal{O}(d)$ on $\mathbb{P}^n$.

---

**References**

**[Hart]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.  
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.  
**[Wei]** C. A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38, Cambridge University Press, 1994.

---

[^1]: More generally, as seen in [\[Topology\] §Sheaves, §§The Abelian Category of Sheaves](/en/math/topology/sheaves#the-abelian-category-of-sheaves), the category $\Sh(X)$ of sheaves defined on an arbitrary topological space $X$ is an abelian category.
