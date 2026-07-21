---
title: "Sheaf Cohomology"
description: "Beyond global sections of vector bundles, we define sheaf cohomology using derived functors and explore its properties to capture the information of sheaves more precisely."
excerpt: "Sheaf cohomology and its applications"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/sheaf_cohomology
sidebar:
    nav: "algebraic_varieties-en"

date: 2026-04-05
weight: 12
translated_at: 2026-07-11T07:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-11T07:30:02+00:00
---
We have seen that line bundles can be used to define various invariants. For example, in [§Line Bundles and Vector Bundles](/en/math/algebraic_varieties/line_bundles) we defined the global section space $\Gamma(X, \mathcal{L})$ of a line bundle $\mathcal{L}$. In particular, in [§Linear Systems, ⁋Definition 9](/en/math/algebraic_varieties/linear_systems#def9) we observed that this dimension plays a crucial role in determining the dimension of the complete linear system, and hence the projective embedding of the variety.

So far we have mainly used the language of line bundles for geometric intuition, but as we saw right after [§Canonical Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1), thinking in terms of the section sheaf of a line bundle means that this can fundamentally be recast in the language of sheaves. In this post we define the notion of sheaf cohomology.

## Definition as a Derived Functor

While sheaves are a powerful tool for systematically describing all the information on a topological space, in our discussion so far sheaves have appeared front and center only in [§Linear Systems](/en/math/algebraic_varieties/linear_systems), when we observed that the global section space $\Gamma(X, \mathcal{L})$ determines the projective embedding of a complete linear system.

However, if global sections were our only concern, there would be no need to think about sheaves at all—we could simply consider the global section functor. In fact, the global section functor does not capture all the information contained in a sheaf. Consider the global section functor

$$\Gamma(X, -): \QCoh(X) \rightarrow \Vect_\mathbb{K}; \qquad \mathcal{F} \mapsto \mathcal{F}(X)$$

When we defined quasi-coherent sheaves in [§Canonical Bundle, ⁋Definition 1](/en/math/algebraic_varieties/canonical_bundle#def1), our motivation was that the category $\Bun(X)$ of vector bundles is not an abelian category, so we wanted to consider a larger category that includes kernels and cokernels. From this perspective, it is not surprising that $\QCoh(X)$ becomes an abelian category. [^1]

If $\Gamma(X,-)$ did not lose any information, it would have to be an exact functor. That is, given a short exact sequence of (quasi-coherent) sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

applying $\Gamma(X,-)$ should again yield a short exact sequence. However, this functor is only left exact. That is, the exactness of

$$0 \rightarrow \Gamma(X, \mathcal{F}') \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{F}'')$$

is guaranteed, but the surjection

$$\Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{F}'') \rightarrow 0$$

is not guaranteed in general. For a concrete example, consider the Euler sequence

$$0 \rightarrow \Omega^1_{\mathbb{P}^n} \rightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow 0$$

([§Canonical Bundle, ⁋Proposition 7](/en/math/algebraic_varieties/canonical_bundle#prop7)). Applying $\Gamma(\mathbb{P}^n, -)$ to this short exact sequence gives

$$0 \rightarrow \Gamma(\mathbb{P}^n, \Omega^1_{\mathbb{P}^n}) \rightarrow \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) \rightarrow \Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})$$

But as we saw in [§Line Bundles and Vector Bundles, ⁋Example 16](/en/math/algebraic_varieties/line_bundles#ex16), the global sections of $\mathcal{O}_{\mathbb{P}^n}(-1)$ are zero, so

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}) = 0$$

while $\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n})=\mathbb{K}$, so surjectivity on the right cannot hold.

The standard way to resolve this is to consider the right derived functor. ([[Homological Algebra] §Derived Functors, ⁋Definition 9](/en/math/homological_algebra/derived_functors#def9)). Specifically, since $\lMod{A}$ has enough injectives, we can show that $\QCoh(X)$ also has enough injective objects, so any quasi-coherent sheaf $\mathcal{F}$ always has an injective resolution $\mathcal{I}^\bullet$, and from this we can define sheaf cohomology via

$$0 \rightarrow \Gamma(X, \mathcal{I}^0) \rightarrow \Gamma(X, \mathcal{I}^1) \rightarrow \Gamma(X, \mathcal{I}^2) \rightarrow \cdots$$

::: Definition 1
For a quasi-coherent sheaf $\mathcal{F}$ on a variety $X$, we define the $i$th *sheaf cohomology* $H^i(X, \mathcal{F})$ as

$$H^i(X, \mathcal{F}) = \frac{\ker(\Gamma(X, \mathcal{I}^i) \rightarrow \Gamma(X, \mathcal{I}^{i+1}))}{\im(\Gamma(X, \mathcal{I}^{i-1}) \rightarrow \Gamma(X, \mathcal{I}^i))}$$

where $\mathcal{I}^\bullet$ is an injective resolution of $\mathcal{F}$.
:::

More generally, for any sheaf on $X$, one can show that $\Sh(X)$ has enough injectives by taking injective objects stalk-wise and then sheafifying, but our primary interest is always in quasi-coherent sheaves, so we restrict our attention to the category $\QCoh(X)$.

That this is independent of the choice of $\mathcal{I}^\bullet$, and so on, all follow from standard arguments in homological algebra.

We previously introduced the global section space $\Gamma(X, \mathcal{L})$ and mentioned that another common notation for this space is $H^0(X, \mathcal{L})$; we now see that this notation is justified by the definition above.

The following proposition is also a standard result that follows immediately from homological algebra. ([[Homological Algebra] §Derived Functors](/en/math/homological_algebra/derived_functors))

::: Proposition 2
For a short exact sequence of sheaves

$$0 \rightarrow \mathcal{F}' \rightarrow \mathcal{F} \rightarrow \mathcal{F}'' \rightarrow 0$$

there exists a long exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}') \rightarrow H^0(X, \mathcal{F}) \rightarrow H^0(X, \mathcal{F}'') \xrightarrow{\delta} H^1(X, \mathcal{F}') \rightarrow \cdots$$

where $\delta$ is the *connecting homomorphism*.
:::

## Čech Cohomology

While [Definition 1](#def1) is a rigorous definition of sheaf cohomology, explicitly constructing an injective resolution is generally very difficult. Therefore, in actual computations we use a different approach to defining cohomology, the Čech approach.

Intuitively, Čech cohomology $\check{H}^i(X, \mathcal{F})$ is a tool that measures the failure of gluing local information. That is, $\check{H}^0(X, \mathcal{F})$ is precisely the global section space, and $\check{H}^1(X, \mathcal{F})$ tells us how much the process of gluing local sections to obtain a global section fails. To define this rigorously, we begin with the following.

::: Definition 3
Given a topological space $X$, an open cover $\mathcal{U} = \{U_i\}_{i \in I}$, and a sheaf $\mathcal{F}$, fix an arbitrary total order $<$ on $I$. Then the *Čech complex* $C^\bullet(\mathcal{U}, \mathcal{F})$ of this data is defined as follows.

$$\check{C}^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_p})$$

The *coboundary map* $d: \check{C}^p \rightarrow \check{C}^{p+1}$ is defined by the formula

$$(d\alpha)_{i_0 \cdots i_{p+1}} = \sum_{k=0}^{p+1} (-1)^k \alpha_{i_0 \cdots \hat{i_k} \cdots i_{p+1}}\vert_{U_{i_0}\cap \cdots \cap U_{i_{p+1}}}$$

where $\hat{i_k}$ means omitting the index $i_k$.
:::

As with sheaf cohomology, this definition makes sense for arbitrary sheaves, but we are mainly concerned with $\QCoh(X)$.

For this definition to be well-defined, that is, for $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ to actually be a complex, the coboundary map must actually be a coboundary map: we need $d^2=0$. This can be verified directly by expanding the above formula and checking the sign differences. In conclusion, $\check{C}^\bullet(\mathcal{U}, \mathcal{F})$ is a cochain complex, and thus we can define the following.

::: Definition 4
We define the *Čech cohomology* $\check{H}^p(\mathcal{U}, \mathcal{F})$ determined by the above data as the cohomology of the Čech complex

$$\check{H}^p(\mathcal{U}, \mathcal{F}) = H^p(\check{C}^\bullet(\mathcal{U}, \mathcal{F}))$$
:::

We previously said that Čech cohomology is a tool that measures the failure of gluing; this is encoded in the coboundary map. Let us verify the intuitive meaning of the coboundary map in low dimensions $p = 0, 1$.

::: Example 5 ($p = 0$)
By the definition of the Čech complex, $\check{C}^0(\mathcal{U}, \mathcal{F}) = \prod_i \mathcal{F}(U_i)$, and the coboundary map from $\check{C}^0$ to $\check{C}^1$ is

$$(ds)_{ij} = s_j\vert_{U_i \cap U_j} - s_i\vert_{U_i \cap U_j}$$

Therefore

$$\check{H}^0(\mathcal{U}, \mathcal{F}) = \ker(d: \check{C}^0 \rightarrow \check{C}^1) = \left\{(s_i) \in \prod_i \mathcal{F}(U_i) \mid s_i\vert_{U_i \cap U_j} = s_j\vert_{U_i \cap U_j} \text{ for all } i, j\right\}$$

By the gluing condition of [[Topology] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1), such a family of sections coincides exactly with a section over all of $X$, that is, with $\Gamma(X, \mathcal{F})$. Thus, $\check{H}^0(\mathcal{U}, \mathcal{F}) = H^0(X, \mathcal{F})$, and this is independent of the choice of open cover.
:::

We will soon show that in good situations, Čech cohomology and sheaf cohomology always agree as above. For now, let us first see how this measures the failure of gluing in the case $p=1$.

::: Example 6 ($p = 1$)
A 1-cochain is a collection of sections $s_{ij} \in \mathcal{F}(U_i \cap U_j)$ on each $U_i \cap U_j$, and a 1-cocycle is one satisfying the cocycle condition

$$s_{ij} + s_{jk} = s_{ik} \qquad\text{on}\quad U_i \cap U_j \cap U_k$$

On the other hand, a 1-coboundary is one induced from a 0-cochain $(t_i)$, that is, of the form $s_{ij} = t_j\vert_{U_i \cap U_j} - t_i\vert_{U_i \cap U_j}$.

Therefore, a nontrivial element of $\check{H}^1(\mathcal{U}, \mathcal{F})$ reflects the discrepancy that appears when trying to glue these three pieces of data $s_{ij}, s_{jk}, s_{ik}$ together, and this is what we call the failure of gluing mentioned above.
:::

So far we have defined Čech cohomology $\check{H}^p(\mathcal{U}, \mathcal{F})$ for a single open cover $\mathcal{U}$. However, different open covers generally give different Čech cohomologies. For example, for the cover consisting of a single open set $U_0 = X$, all intersections are $X$, so $\check{H}^p$ is nonzero only for $p = 0$. The finer the cover, the more topological information we can capture, so we need to clarify the relationship between open covers and synthesize the information over all open covers. That is, we impose an ordering on <em>all</em> open covers using refinement. Then for a refinement $\mathcal{V} \preceq \mathcal{U}$, there is a natural map $\check{H}^p(\mathcal{U}, \mathcal{F}) \rightarrow \check{H}^p(\mathcal{V}, \mathcal{F})$, and thus we can define a direct system $\check{H}^p(\mathcal{U}, \mathcal{F})$ indexed by all open covers. From this we define the following.

::: Definition 7
We define the *Čech cohomology* of $X$ as the direct limit over all open covers

$$\check{H}^p(X, \mathcal{F}) = \varinjlim_{\mathcal{U}} \check{H}^p(\mathcal{U}, \mathcal{F})$$
:::

To put the above argument more simply, the meaning is that we take finer and finer open covers and combine all the additional cohomology data that appears, defining this as $\check{H}(X, \mathcal{F})$.

In general, the $\check{H}^p(X, \mathcal{F})$ of [Definition 7](#def7) and the $H^p(X, \mathcal{F})$ of [Definition 1](#def1) are not guaranteed to be isomorphic, but fortunately for most sheaves that appear in algebraic geometry, the two coincide. Showing this requires some technical machinery.

::: Definition 8
For a sheaf $\mathcal{F}$ on a variety $X$, we define the following.

1. A sheaf $\mathcal{F}$ is *acyclic* if $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
2. An injective object $\mathcal{F}$ in $\Sh(X)$ is called an *injective sheaf*.
3. If for any open sets $V\subset U$, the restriction map $$\mathcal{F}(U)
\rightarrow \mathcal{F}(V)$$ is surjective, then $\mathcal{F}$ is called a *flasque sheaf*.
:::

The condition we want at the cohomology level is of course the first one. Let us first examine the relationship between these concepts.

::: Lemma 9
An injective sheaf $\mathcal{F}$ is flasque.
:::

::: Proof
By definition, $\mathcal{F}$ being injective means that for any monomorphism $\mathcal{A} \hookrightarrow \mathcal{B}$, the map $\Hom_{\Sh(X)}(\mathcal{B}, \mathcal{F}) \rightarrow \Hom_{\Sh(X)}(\mathcal{A}, \mathcal{F})$ is surjective. ([[Homological Algebra] §Resolutions, ⁋Definition 1](/en/math/homological_algebra/resolutions#def1)) We now show that for any open sets $V \subset U \subset X$, the restriction $\mathcal{F}(U) \rightarrow \mathcal{F}(V)$ is surjective.

This map is a morphism of abelian groups, not a sheaf morphism, and the tools we have are sheaf morphisms, so we need to rephrase this condition in terms of sheaf morphisms. To this end, we introduce the open embeddings

$$i^U: U \hookrightarrow X,\qquad i^V: V \hookrightarrow X$$

and the sheaves $i^U_!\mathbb{Z}_U, i^V_!\mathbb{Z}_V$ obtained from these by extension by zero. Here $\mathbb{Z}_U, \mathbb{Z}_V$ are constant sheaves, and since $V \subset U$ by assumption, there is a natural monomorphism $i^V_!\mathbb{Z}_V \rightarrow i^U_!\mathbb{Z}_U$.

First, let us verify that $\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \mathcal{F}(U)$ holds. Since extension by zero $i^U_!$ is the left adjoint of restriction $\mathcal{G} \mapsto \mathcal{G}\vert_U$ ([[Topology] §Sheaves, ⁋Example 14](/en/math/topology/sheaves#ex14)), we have

$$\Hom_{\Sh(X)}(i^U_!\mathbb{Z}_U, \mathcal{F}) \cong \Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U)$$

Now $\mathbb{Z}_U$ is the constant sheaf on $U$, so for any open set $W \subset U$ we have $\mathbb{Z}_U(W) = \mathbb{Z}$, and every section is given by the restriction of a constant function. Therefore, a sheaf morphism $\varphi: \mathbb{Z}_U \rightarrow \mathcal{F}\vert_U$ is completely determined by the image of the global section $\varphi_U(1) \in \mathcal{F}(U)$. Conversely, for any $s \in \mathcal{F}(U)$, defining $\mathbb{Z}_U(W) \rightarrow \mathcal{F}(W),\; n \mapsto n \cdot s\vert_W$ for each $W \subset U$ gives a well-defined sheaf morphism. Thus

$$\Hom_{\Sh(U)}(\mathbb{Z}_U, \mathcal{F}\vert_U) \cong \Hom_{\Ab}(\mathbb{Z}, \mathcal{F}(U)) \cong \mathcal{F}(U)$$

Similarly, $\Hom_{\Sh(X)}(i^V_!\mathbb{Z}_V, \mathcal{F}) \cong \mathcal{F}(V)$, and by naturality the map between these coincides exactly with the restriction $\mathcal{F}(U)\rightarrow \mathcal{F}(V)$. Since $\mathcal{F}$ is injective by assumption, this is surjective, completing the proof.
:::

::: Lemma 10
A flasque sheaf $\mathcal{F}$ is Čech-acyclic for any open cover $\mathcal{U}$. That is, $\check{H}^p(\mathcal{U}, \mathcal{F}) = 0$ for all $p > 0$.
:::

::: Proof
Consider the augmented Čech complex

$$0 \rightarrow \mathcal{F}(U) \xrightarrow{\epsilon} \check{C}^0(\mathcal{U}, \mathcal{F}) \xrightarrow{d^0} \check{C}^1(\mathcal{U}, \mathcal{F}) \xrightarrow{d^1} \cdots$$

What we need to show is that this is exact for $p>0$, so it suffices to show that the identity chain map is nullhomotopic. To do this, for each $p\geq 1$ we need to explicitly construct a homotopy operator $s^p : \check{C}^p(\mathcal{U}, \mathcal{F}) \rightarrow \check{C}^{p-1}(\mathcal{U}, \mathcal{F})$.

To define this function, we need to explain how each component

$$s^p(t)_{j_0<\cdots< j_{p-1}}$$

is defined when given

$$t=(t_{j_0<\cdots< j_p})\in \check{C}^p(\mathcal{U}, \mathcal{F})$$

Essentially, what we want to do is, as is always the case when defining a chain homotopy, fix an index $i_0$ and insert it into $j_0<\cdots< j_{p-1}$ (for convenience, assume $i_0< j_0<\cdots< j_{p-1}$), defining

$$s^p(t)_{j_0<\cdots< j_{p-1}}=t_{i_0< j_0<\cdots < j_{p-1}}\tag{$\ast$}$$

Now, $s^p(t)_{j_0<\cdots< j_{p-1}}$ is by definition a section over $U_{j_0}\cap\cdots\cap U_{j_{p-1}}$, but note that the right-hand side $t_{i_0< j_0<\cdots < j_{p-1}}$ is a section over the smaller set $U_{i_0}\cap U_{j_0}\cap\cdots\cap U_{j_{p-1}}$. For a general $\mathcal{F}$ this would be impossible to define in this way, but since we are assuming $\mathcal{F}$ is flasque, we can always extend this function to make it a section over $U_{j_0}\cap\cdots\cap U_{j_{p-1}}$, and equation ($\ast$) should be understood in this manner. Then the fact that $s^p$ defined this way is actually a chain homotopy can be verified by direct calculation: in $d^{p-1}s^p$ the term omitting $i_0$ and in $s^{p+1}d^p$ the term inserting $i_0$ cancel each other out with opposite signs.

A slight technical issue is that the fixed index $i_0$ may be contained in $j_0<\cdots< j_{p-1}$. To handle this, instead of the usual Čech complex we use the *non-alternating* Čech complex, which uses coordinates given by $p+1$ elements $i_0,\ldots, i_{p+1}\in I$. This is quasi-isomorphic to the original Čech complex, so this detour is justified.
:::

::: Theorem 11 (Leray)
For a sheaf $\mathcal{F}$ on a topological space $X$ and an open cover $\mathcal{U} = \{U_i\}$, if $\mathcal{F}$ is acyclic on all finite intersections

$$U_{i_0 \cdots i_p}=U_{i_0}\cap \cdots\cap U_{i_p}$$

then there is an isomorphism

$$\check{H}^p(\mathcal{U}, \mathcal{F}) \rightarrow H^p(X, \mathcal{F})$$
:::

::: Proof
Fix an injective resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^0 \rightarrow \mathcal{I}^1 \rightarrow \cdots$ of the sheaf $\mathcal{F}$, and construct the double complex

$$K^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{I}^q)$$

In this double complex, the horizontal differential $d_h$ is the Čech differential, and the vertical differential $d_v$ is the differential coming from the injective resolution. As we saw in [[Homological Algebra] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11), the two filtrations

$$F_v^p\Tot(K)^\bullet,\qquad F_h^p\Tot(K)^\bullet$$

defined on the total complex $\Tot(K)^\bullet$ of this double complex converge to the same filtered homology $H^\bullet(\Tot(K))$.

Therefore, consider the spectral sequences given by each filtered complex. First, for the vertical filtration, on the $E_1$ page we have $E_1^{p,q} = H^q(K^{p,\bullet})$, and $K^{p,\bullet} = \check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$. Now, looking at each component, $\check{C}^p(\mathcal{U}, \mathcal{I}^\bullet)$ is obtained by restricting the injective resolution to each intersection $U_{i_0 \cdots i_p}$ and then taking cohomology, so it equals the $q$th sheaf cohomology of $\mathcal{F}$ on $U_{i_0\cdots i_p}$, and thus by the assumption that $\mathcal{F}$ is acyclic we have $E_1^{p,q}=0$ for all $q>0$. Also, by definition $E_1=\check{C}^p(\mathcal{U}, \mathcal{F})$. Now the $E_2$ page is given by the cohomology of $E_1^{p,0}$ with respect to the horizontal differential $d_h$, so

$$E_2^{p,q}=\begin{cases}\check{H}^p(\mathcal{U}, \mathcal{F})&\text{$q=0$}\\0&\text{otherwise}\end{cases}$$

and $E_2^{p,q}=E_\infty^{p,q}$.

Now looking in the horizontal filtration direction, on the $E_1$ page we have $E_1^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{I}^q)$. But since we showed earlier in [Lemma 9](#lem9) and [Lemma 10](#lem10) that injective sheaves are Čech-acyclic, we have $E_1^{p,q} = 0$ for $p > 0$, and the remaining cohomology with respect to the vertical differential at $p=0$ is sheaf cohomology, so

$$E_2^{p,q}=\begin{cases}H^q(X, \mathcal{F})&\text{$p=0$}\\0&\text{otherwise}\end{cases}$$

and $E_2^{p,q}=E_\infty^{p,q}$. Since the two spectral sequences converge to the same $H^\bullet(\Tot(K))$, we conclude that

$$\check{H}^n(\mathcal{U}, \mathcal{F}) \cong H^n(X, \mathcal{F})$$
:::

Then the only obstacle to our intuition is how demanding this acyclicity condition is, but fortunately it is a more lenient condition than one might think.

::: Proposition 12
For a quasi-coherent sheaf $\mathcal{F} = \widetilde{M}$ on an affine variety $X$, $H^i(X, \mathcal{F}) = 0$ holds for all $i > 0$.
:::

The proof of this is that if we let $A$ be the coordinate ring of $X$ and find an injective resolution $I^\bullet$ of $M$ in the category $\lMod{A}$, this gives $\widetilde{I^\bullet}$ (which is a resolution in $\QCoh(X)$), and the sheaf given by an injective module is always flasque and hence acyclic.

Now consider an arbitrary variety $X$ and a quasi-coherent sheaf $\mathcal{F}$ defined on it, and suppose an affine open cover $\mathcal{U}$ of $\mathcal{F}$ is given. Then for these data to satisfy the hypotheses of [Theorem 11](#thm11), every finite intersection of $\mathcal{U}$ must again be affine. If the diagonal

$$\Delta_X\hookrightarrow X\times X$$

is a *closed* immersion in $X\times X$, then we can show that this condition holds, and in this case we call $X$ a *separated* variety. This is, as can be seen from its definition, the Zariski topology version of the Hausdorff condition, and is a reasonable condition; if we define a variety to be quasi-projective as we currently do, this condition is automatically satisfied. That is, in our current language, this argument means that Čech cohomology and sheaf cohomology coincide for quasi-coherent sheaves defined on any variety, and moreover, if we choose an open cover $\mathcal{U}$ satisfying the hypotheses of [Theorem 11](#thm11), it suffices to compute the Čech cohomology for that open cover without taking the direct limit.

## Godement Resolution

We defined sheaf cohomology via injective resolution in [Definition 1](#def1), but since directly computing an injective resolution is generally difficult, we examined one solution to this: using the result [Theorem 11](#thm11) that Čech cohomology and sheaf cohomology are isomorphic.

The Godement resolution that we examine in this section also starts from the same problem. That is, computing sheaf cohomology in general is a very complicated task, so [Definition 1](#def1) is conceptually clean but somewhat lacking in practicality. We now define a specific resolution. This is not an injective resolution, but a flasque resolution, and for our purposes this is sufficient.

::: Definition 13
For a sheaf $\mathcal{F}$ on a topological space $X$, we define the *Godement sheaf* $C^0(\mathcal{F})$ by

$$C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x$$

for each open set $U \subset X$. Here $\mathcal{F}_x$ is the stalk of $\mathcal{F}$ at $x$.
:::

Then for each $x\in X$, the identity $\mathcal{F}_x\rightarrow \mathcal{F}_x$ on the stalk gives a well-defined canonical morphism $\mathcal{F}\rightarrow C^0(\mathcal{F})$. Also, the fact that $C^0(\mathcal{F})$ is a sheaf is almost trivially defined.

Intuitively, $C^0(\mathcal{F})$ can be thought of as the collection of functions that choose an element of $\mathcal{F}_x$ at each point $x\in X$ with no constraints whatsoever; from this perspective it is sometimes called the *sheaf of discontinuous sections*. The following is a basic property of this sheaf.

::: Proposition 14
The Godement sheaf $C^0(\mathcal{F})$ is a flasque sheaf. Moreover, $\mathcal{F} \mapsto C^0(\mathcal{F})$ is an exact functor.
:::

::: Proof
First, we show that the given sheaf is flasque. For open sets $V \subset U$, the restriction map $C^0(\mathcal{F})(U) = \prod_{x \in U} \mathcal{F}_x \rightarrow \prod_{x \in V} \mathcal{F}_x = C^0(\mathcal{F})(V)$ is a projection, so it is surjective. Therefore $C^0(\mathcal{F})$ is flasque.

Exactness is trivial because the stalk functor $\mathcal{F} \mapsto \mathcal{F}_x$ is exact and $C^0(\mathcal{F})$ is just a product of stalks.
:::

Now consider the cokernel exact sequence induced by the canonical map $0\rightarrow\mathcal{F}\rightarrow C^0(\mathcal{F})$

$$0\rightarrow \mathcal{F}\rightarrow C^0(\mathcal{F})\rightarrow \mathcal{Q}^1\rightarrow 0$$

Intuitively, $\mathcal{Q}^1$ is the collection of purely discontinuous parts, and from this perspective, the more we repeat this construction, the finer the information about discontinuity that is captured. That is, applying $C^0$ to the sheaf $\mathcal{Q}^1$ gives the next cokernel exact sequence

$$0 \rightarrow \mathcal{Q}^1\rightarrow C^0(\mathcal{Q}^1)\rightarrow\mathcal{Q}^2\rightarrow 0$$

and by splicing we obtain the complex

$$0 \rightarrow C^0(\mathcal{F}) \rightarrow C^0(\mathcal{Q}^1) \rightarrow C^0 (\mathcal{Q}^2)\rightarrow \cdots$$

We call this complex the *Godement resolution* of $\mathcal{F}$, and denote its components by

$$0 \rightarrow \mathcal{F} \rightarrow \mathcal{G}^0(\mathcal{F}) \rightarrow \mathcal{G}^1(\mathcal{F}) \rightarrow \cdots$$

Then by [Proposition 14](#prop14) the following holds.

::: Proposition 15
The Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ is a flasque resolution of $\mathcal{F}$.
:::

The most essential advantage of this construction is that there is no choice involved in this process, so in some sense it is canonical. This can also be reconfirmed from the functoriality of the Godement resolution: in general, to show functoriality in sheaf cohomology, one must use the argument that a sheaf morphism at the 0th stage of the augmented complex induces sheaf morphisms at the $i>0$ stages to give a chain map, and such chain maps are the same up to chain homotopy equivalence, so they induce the same value in cohomology. ([[Homological Algebra] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6)) However, in the case of the Godement resolution, the functions are induced purely at the chain level without any kind of equivalence. Nevertheless, the Godement resolution exactly captures the information of sheaf cohomology.

To show this, we first show more generally that a flasque resolution gives the same sheaf cohomology as an injective resolution. For this we first show the following.

::: Proposition 16
A flasque sheaf $\mathcal{F}$ is $\Gamma(X, -)$-acyclic. That is, $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
:::

::: Proof
We proceed by induction on $i$. First, consider the case $i=1$. To show this, embed $\mathcal{F}$ into an injective sheaf $\mathcal{I}$, and consider the cokernel exact sequence

$$0 \rightarrow \mathcal{F}\rightarrow\mathcal{I}\rightarrow\mathcal{Q}\rightarrow0$$

Our claim is that $\mathcal{Q}$ is flasque, which can be shown by a diagram chase in the following commutative diagram for any open sets $V\subset U$

![Commutative diagram](/assets/images/Math/Algebraic_Varieties/Sheaf_Cohomology-1.svg){:style="width:23.07em" class="invert" .align-center}

Here $\mathcal{F}$ is flasque by assumption and $\mathcal{I}$ is injective and hence flasque. Now for any $s\in \mathcal{Q}(V)$, since $\mathcal{I}(V)\rightarrow \mathcal{Q}(V)$ is surjective we can lift $s$ to $t\in \mathcal{I}(V)$, and then using that $\mathcal{I}$ is flasque we can lift $t$ to $\overline{t}\in\mathcal{I}(U)$ and push this down to $\mathcal{Q}$ to define $\overline{s}\in \mathcal{Q}(U)$. Now the element $\overline{s}\vert_V-s$ in $\mathcal{Q}(U)$ is an element of $\mathcal{F}(V)$, and again by the flasqueness of $\mathcal{F}$ there exists an appropriate $h\in \mathcal{F}(U)$ such that $h\vert_V=\overline{s}\vert_V-s$. From this, $\overline{s}-h$ restricts exactly to $s\in \mathcal{Q}(V)$, and we obtain the flasqueness of $\mathcal{Q}$.

Now applying $\Gamma(X, -)$ gives the long exact sequence

$$0 \rightarrow \Gamma(X, \mathcal{F}) \rightarrow \Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{Q}) \xrightarrow{\delta} H^1(X, \mathcal{F}) \rightarrow H^1(X, \mathcal{I}) = 0$$

Here $H^1(X, \mathcal{I}) = 0$ because $\mathcal{I}$ is injective. Thus

$$H^1(X, \mathcal{F}) \cong \coker(\Gamma(X, \mathcal{I}) \rightarrow \Gamma(X, \mathcal{Q}))$$

and to show that this is $0$ we need to show that $\Gamma(X, \mathcal{I})\rightarrow \Gamma(X, \mathcal{Q})$ is surjective. To this end, let $s\in \Gamma(X, \mathcal{Q})$ be given. Then for any $x\in X$, since $\mathcal{I}\rightarrow \mathcal{Q}$ is surjective at the stalk level, for each $x\in X$ there exists an appropriate $t_x\in \mathcal{I}_x$ such that $t_x$ maps to $s_x\in \mathcal{Q}_x$. Now choose a representative of $t_x$ and think of $t_x$ as an element of $\mathcal{I}(U_x)$; since $\mathcal{I}$ is flasque we can extend each of these to global sections $T_x$ on $X$, and then $T_x\mid_{U_x}=s\mid_{U_x}$.

Now let $S_x$ be the image of $T_x$ in $\Gamma(X,\mathcal{Q})$. Then $S_x-S_y$ is identically zero on $U_x\cap U_y$, so we can lift this to a section $f_{xy}$ of $\mathcal{F}$ on $U_x\cap U_y$. Using the flasqueness of $\mathcal{F}$ again, we can extend this to $f_x\in \mathcal{F}(U_x)$ and $f_y\in \mathcal{F}(U_y)$ respectively, and then replacing $T_x$ by $T'_x=T_x-f_x$ in this situation satisfies the compatibility condition, so we know that gluing these gives a preimage of $s$.

Finally, by the long exact sequence,

$$H^i(X, \mathcal{F})\cong H^{i-1}(X, \mathcal{Q})$$

and since $\mathcal{Q}$ is flasque, we obtain the desired result by induction.
:::

In particular, by [Proposition 16](#prop16), each term $\mathcal{G}^p(\mathcal{F})$ of the Godement resolution is flasque and hence $\Gamma(X, -)$-acyclic. That is, $H^i(X, \mathcal{G}^p(\mathcal{F})) = 0$ for all $i > 0$. To reach our conclusion, the result we need is the following.

::: Proposition 17 (Acyclic Resolution)
Given a $\Gamma(X, -)$-acyclic resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{A}^0 \rightarrow \mathcal{A}^1 \rightarrow \cdots$,

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(X, \mathcal{F})$$

holds for all $q \geq 0$.
:::

::: Proof
Fix an injective resolution $0 \rightarrow \mathcal{F} \rightarrow \mathcal{I}^\bullet$ of $\mathcal{F}$. By [[Homological Algebra] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6), there exists a chain map $f\colon \mathcal{A}^\bullet \rightarrow \mathcal{I}^\bullet$ between the acyclic resolution and the injective resolution. Consider the *mapping cone* $C(f)^\bullet$ of $f$. In each degree,

$$C(f)^n = \mathcal{A}^{n+1} \oplus \mathcal{I}^n$$

and since $\mathcal{I}^n$ is injective, it is flasque by [Lemma 9](#lem9) and in particular $\Gamma(X, -)$-acyclic. Therefore, considering the canonical short exact sequence

$$0 \rightarrow \mathcal{I}^n \rightarrow C(f)^n \rightarrow \mathcal{A}^{n+1} \rightarrow 0$$

since both end terms are $\Gamma(X, -)$-acyclic, the long exact sequence shows that $C(f)^n$ is also $\Gamma(X, -)$-acyclic.

On the other hand, since $f$ is a quasi-isomorphism, $C(f)^\bullet$ is an exact complex. ([[Homological Algebra] §Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9)) Moreover, since $C(f)^\bullet$ is $\Gamma(X,-)$-acyclic as we saw above, applying $\Gamma(X,-)$ gives an exact complex $\Gamma(X, C(f)^\bullet)$, and applying [[Homological Algebra] §Long Exact Sequence, ⁋Corollary 9](/en/math/homological_algebra/long_exact_sequence#cor9) again converts this to the condition that the chain map

$$\Gamma(X, f)\colon \Gamma(X, \mathcal{A}^\bullet) \rightarrow \Gamma(X, \mathcal{I}^\bullet)$$

is a quasi-isomorphism. From this we obtain

$$H^q(\Gamma(X, \mathcal{A}^\bullet)) \cong H^q(\Gamma(X, \mathcal{I}^\bullet)) = H^q(X, \mathcal{F})$$
:::

[Proposition 17](#prop17) together with [Proposition 16](#prop16) guarantees that the Godement resolution is actually sufficient for computing sheaf cohomology. That is, the cohomology of the complex $\Gamma(X, \mathcal{G}^\bullet(\mathcal{F}))$ obtained by taking global sections of the flasque resolution $\mathcal{G}^\bullet(\mathcal{F})$ coincides with $H^\bullet(X, \mathcal{F})$.

## Spectral Sequence

One of the most powerful applications of sheaf cohomology is the computation of cohomology via spectral sequences. We will conclude this post with concrete computations in this section. The propositions we introduce now hold in a general topological setting, but since we mainly have in mind applications to varieties and quasi-coherent sheaves, we have placed them in this category.

Fix a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$. Then from [[Topology] §Sheaves, ⁋Lemma 11](/en/math/topology/sheaves#lem11) and [[Category Theory] §Adjoints, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9), we know that the direct image functor $f_\ast: \Sh(X)\rightarrow \Sh(Y)$ is a left exact functor. Therefore, just as in [[Homological Algebra] §Derived Functors](/en/math/homological_algebra/derived_functors), we can define the right derived functor of $f_\ast$ as

$$R^q f_\ast \mathcal{F} := H^q(f_\ast \mathcal{I}^\bullet)$$

where $\mathcal{I}^\bullet$ is an injective resolution of $\mathcal{F}$. By definition, when $q=0$ we have $R^0 f_\ast \mathcal{F}=f_\ast \mathcal{F}$, and if $\mathcal{F}$ is injective then $\mathcal{F}$ itself forms an injective resolution, so $R^qf_\ast \mathcal{F}=0$ holds.

Now consider the Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ of $\mathcal{F}$. Intuitively, what we want to do is take an injective resolution of each $\mathcal{G}^p(\mathcal{F})$ and then use the differential $\mathcal{G}^p(\mathcal{F})\rightarrow \mathcal{G}^{p+1}(\mathcal{F})$ of the Godement resolution to define a horizontal differential via [[Homological Algebra] §Resolutions, ⁋Theorem 6](/en/math/homological_algebra/resolutions#thm6).

::: Definition 18 (Cartan-Eilenberg Resolution)
In an abelian category, a *Cartan-Eilenberg resolution* of a cochain complex $K^\bullet$ is data consisting of a double complex $I^{p,q}$ and an augmentation $K^\bullet \rightarrow I^{\bullet,0}$ satisfying the following conditions.

1. Each column $I^{p,\bullet}$ is an injective resolution of $K^p$.
2. The cohomology of each row $H^p(I^{\bullet,q})$ forms an injective resolution of $H^p(K^\bullet)$. That is, the chain complex

    $$\cdots \rightarrow H^p(I^{\bullet,q-1}) \rightarrow H^p(I^{\bullet,q}) \rightarrow H^p(I^{\bullet,q+1}) \rightarrow \cdots$$

    is an injective resolution of $H^p(K^\bullet)$.
:::

The key point of this definition is that the intuition mentioned above does not by itself yield a Cartan-Eilenberg resolution; in particular, the fact that the cohomology of each row forms a horizontal resolution of $H^p(K^\bullet)$ is the key element in the proof of existence. We do not separately prove the existence of Cartan-Eilenberg resolutions, but basically it can be obtained by repeatedly applying [[Homological Algebra] §Resolutions, ⁋Lemma 7](/en/math/homological_algebra/resolutions#lem7).

Now fix a Cartan-Eilenberg resolution $\mathcal{I}^{p,q}$ of the complex $f_\ast\mathcal{G}^\bullet(\mathcal{F})$. Then by definition, each column $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast\mathcal{G}^p(\mathcal{F})$, and the horizontal cohomology of each row $H^p(\mathcal{I}^{\bullet,q})$ forms an injective resolution of $H^p(f_\ast\mathcal{G}^\bullet(\mathcal{F})) = R^p f_\ast\mathcal{F}$.

Since this spectral sequence lies in the first quadrant, we know that it converges to the cohomology of the total complex $\Tot(\mathcal{I})^\bullet$. For a concrete computation, let us filter by $p$ in the Godement direction. Then we can first write the $E_1$ page as

$$\mathcal{H}^{p,q} := H^p(\mathcal{I}^{\bullet, q})$$

Here the vertical differential is the map $\mathcal{H}^{p,q}\rightarrow \mathcal{H}^{p,q+1}$ induced by the differential of the injective resolution descending to the cohomology level, and the $E_2$ page is the cohomology sheaf of this vertical complex

$$E_2^{p,q} = H^q(\mathcal{H}^{p,\bullet})$$

On the other hand, since $\mathcal{I}^{\bullet,\bullet}$ is a Cartan resolution, we know that each $\mathcal{H}^{p,\bullet}$ is an injective resolution of $R^p f_\ast \mathcal{F}$. We call this spectral sequence the *Leray spectral sequence*.

Now considering the spectral sequence coming from the $q$ direction filtration, its $E_1$ page is

$$E_1^{p,q} = H^q(\mathcal{I}^{p,\bullet})$$

Now, for each $p$, $\mathcal{I}^{p,\bullet}$ is an injective resolution of $f_\ast \mathcal{G}^p(\mathcal{F})$, so by the exactness of injective resolution,

$$E_1^{p,q} = \begin{cases} f_\ast \mathcal{G}^p(\mathcal{F}) & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

and the $d_1$-differential is the map from $E_1^{p,0} = f_\ast \mathcal{G}^p(\mathcal{F})$ to $E_1^{p+1,0} = f_\ast \mathcal{G}^{p+1}(\mathcal{F})$, which corresponds to the differential $f_\ast \mathcal{G}^p(\mathcal{F}) \rightarrow f_\ast \mathcal{G}^{p+1}(\mathcal{F})$ of the Godement resolution. That is, the $E_2$ page is the cohomology sheaf of the complex

$$0 \rightarrow f_\ast \mathcal{F} \rightarrow f_\ast \mathcal{G}^0(\mathcal{F}) \rightarrow f_\ast \mathcal{G}^1(\mathcal{F}) \rightarrow \cdots$$

and by the definition of $R^q f_\ast$ this is given by

$$E_2^{p,q} = \begin{cases} R^p f_\ast \mathcal{F} & \text{if $q = 0$} \\ 0 & \text{if $q > 0$} \end{cases}$$

Therefore, we know that the cohomology of the total complex of $\mathcal{I}^{\bullet,\bullet}$ must converge to $R^n f_\ast \mathcal{F}$.

Now let us re-examine the above discussion by applying the global section functor $\Gamma(Y,-)$ to this result. That is, we consider the double complex

$$\mathcal{J}^{p,q}=\Gamma(Y, \mathcal{I}^{p,q})$$

and its total complex $\Tot(\mathcal{J})^\bullet$. Then by the same computation as above, the $p$ direction filtration gives on the $E_1$ page

$$E_1^{p,q}=H^p(\mathcal{J}^{\bullet, q})=\Gamma(Y, \mathcal{H}^{p,q})$$

and since $\mathcal{H}^{p,q}$ is an injective resolution of $R^pf_\ast \mathcal{F}$, its cohomology comes out as $H^q(Y, R^p f_\ast \mathcal{F})$.

On the other hand, for the $q$ direction filtration, the $E_1$ page is

$$E_1^{p,q}=H^q(\Gamma(Y, \mathcal{I}^{p,\bullet}))$$

and since each $\mathcal{I}^{p,\bullet}$ is an injective resolution by the definition of Cartan-Eilenberg resolution, it is flasque ([Lemma 9](#lem9)), and since a flasque sheaf is $\Gamma$-acyclic, the terms for $q>0$ vanish, leaving

$$E_1^{p,0}=\Gamma(Y, f_\ast \mathcal{G}^p (\mathcal{F}))=\Gamma(X, \mathcal{G}^p(\mathcal{F}))$$

with the Godement differential. Therefore the $E_2$ page is

$$E_2^{n,0}=H^n(\Gamma(X, \mathcal{G}^\bullet(\mathcal{F}))=H^n(X, \mathcal{F})$$

and thus we obtain the following.

::: Proposition 19 (Leray Spectral Sequence)
For a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$, there exists a spectral sequence with the following $E_2$ page.

$$E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F}).$$
:::

Geometrically, this is most transparent when $f:X\rightarrow Y$ is a fibration; in this case, what this spectral sequence means is that to compute the cohomology on $X$, we first compute the cohomology on $Y$, then remember the cohomology on the fiber at each point as the higher sheaf $R^q f_\ast \mathcal{F}$, and finally compose these over $Y$.

Now in the lowest dimensions of the Leray spectral sequence, we can obtain the following exact sequence.

::: Corollary 20 (Five-Term Exact Sequence)
For a continuous map $f : X \rightarrow Y$ and a sheaf $\mathcal{F}$, from the Leray spectral sequence we obtain the exact sequence

$$0 \rightarrow H^1(Y, f_\ast \mathcal{F}) \rightarrow H^1(X, \mathcal{F}) \rightarrow H^0(Y, R^1 f_\ast \mathcal{F}) \overset{d_2}{\rightarrow} H^2(Y, f_\ast \mathcal{F}) \rightarrow H^2(X, \mathcal{F})$$
:::

::: Proof
Consider the terms with $p+q \leq 2$ on the $E_2$ page of the Leray spectral sequence $E_2^{p,q} = H^p(Y, R^q f_\ast \mathcal{F}) \Rightarrow H^{p+q}(X, \mathcal{F})$. By [[Homological Algebra] §Spectral Sequences, ⁋Definition 5](/en/math/homological_algebra/spectral_sequences#def5), we know that

$$E_\infty^{p,q} \cong \gr^p H^{p+q} = F^p H^{p+q}/F^{p+1}H^{p+q}$$

In particular, since this is a first quadrant spectral sequence, $E_r^{p,q} = E_\infty^{p,q}$ for sufficiently large $r$. ([[Homological Algebra] §Spectral Sequences, ⁋Proposition 6](/en/math/homological_algebra/spectral_sequences#prop6))

First, looking at the components with $p+q = 1$, there are only two terms $E_2^{1,0}$ and $E_2^{0,1}$. But considering the degrees, all differentials entering or leaving $E_2^{1,0}$ are 0, so $E_2^{1,0} = E_\infty^{1,0}$. On the other hand, the $d_2$ from $E_2^{0,1}$ to $E_2^{2,0}$ may be nontrivial, so $E_\infty^{0,1} = \ker(d_2: E_2^{0,1} \rightarrow E_2^{2,0})$. Then by the filtration,

$$0 \rightarrow E_\infty^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_\infty^{0,1} \rightarrow 0$$

is exact, and since $E_\infty^{1,0} = E_2^{1,0}$ and $E_\infty^{0,1} = \ker(d_2) \hookrightarrow E_2^{0,1}$, combining these gives the exact sequence

$$0 \rightarrow E_2^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

To complete the proof, consider the components $E_2^{2,0}$, $E_2^{1,1}$, $E_2^{0,2}$ with $p+q = 2$. For the same reason, the only possibly nontrivial differential is $d_2 : E_2^{0,1} \rightarrow E_2^{2,0}$, and on the $E_3$ page defined by this differential,

$$E_3^{0,2} = \ker(d_2 : E_2^{0,2} \rightarrow E_2^{2,1}), \qquad E_3^{2,0} = \operatorname{coker}(d_2 : E_2^{0,1} \rightarrow E_2^{2,0})$$

and again analyzing degrees, $E_3^{p,q} = E_\infty^{p,q}$, so

$$E_\infty^{2,0} = E_3^{2,0} = \operatorname{coker}(d_2 : E_2^{0,1} \rightarrow E_2^{2,0})$$

We have shown so far that the exact sequence

$$0 \rightarrow E_2^{1,0} \rightarrow H^1(X, \mathcal{F}) \rightarrow E_2^{0,1} \xrightarrow{d_2} E_2^{2,0}$$

exists, and from the above computation,

$$E_\infty^{2,0} = E_3^{2,0} = \operatorname{coker}(d_2: E_2^{0,1} \rightarrow E_2^{2,0})$$

so inserting this into $H^2(X, \mathcal{F})$ via the filtration gives that

$$E_2^{0,1} \overset{d_2}{\rightarrow} E_2^{2,0} \rightarrow H^2(X, \mathcal{F})$$

is exact. Combining these gives the desired result.
:::

This exact sequence shows what constraints the existence of the $d_2$-differential imposes on cohomology computations, and justifies the intuition that $H^i(X, \mathcal{F}) \cong H^i(Y, f_\ast \mathcal{F})$ in good cases.

Finally, we can describe the relationship between Čech cohomology and derived functor cohomology using a spectral sequence.

::: Proposition 21 (Čech-to-Derived Functor Spectral Sequence)
For a sheaf $\mathcal{F}$ on a topological space $X$ and an open cover $\mathcal{U}$, there exists a spectral sequence

$$E_2^{p,q} = \check{H}^p(\mathcal{U}, \mathcal{H}^q(\mathcal{F})) \Rightarrow H^{p+q}(X, \mathcal{F})$$

where $\mathcal{H}^q(\mathcal{F})$ is the sheafification of the presheaf $U \mapsto H^q(U, \mathcal{F})$.
:::

::: Proof
Take the Godement resolution $\mathcal{G}^\bullet(\mathcal{F})$ of $\mathcal{F}$ and construct the double complex $C^{p,q} = \check{C}^p(\mathcal{U}, \mathcal{G}^q(\mathcal{F}))$. That the two spectral sequences obtained from the two filtrations converge to the same total cohomology $H^{p+q}(X, \mathcal{F})$ is by [[Homological Algebra] §Spectral Sequences, ⁋Example 11](/en/math/homological_algebra/spectral_sequences#ex11), and since the Godement sheaf $\mathcal{G}^q(\mathcal{F})$ is flasque, it is Čech-acyclic by [Lemma 10](#lem10), so the same vanishing as in the above computation can be used.
:::

This spectral sequence allows us to understand [Theorem 11](#thm11) in a broader context. If $\mathcal{F}$ is acyclic on all finite intersections of $\mathcal{U}$, then $\mathcal{H}^q(\mathcal{F}) = 0$ for all $q > 0$, so all terms with $q > 0$ on the $E_2$ page vanish, giving $E_2^{p,0} = \check{H}^p(\mathcal{U}, \mathcal{F}) \cong H^p(X, \mathcal{F})$. That is, the Čech-to-derived functor spectral sequence is a more general result that includes [Theorem 11](#thm11).

## Classification of Line Bundles

Earlier we saw that a line bundle is determined by transition functions $g_{ij} \in \mathcal{O}_X^\ast(U_i \cap U_j)$ ([§Line Bundles and Vector Bundles, ⁋Proposition 2](/en/math/algebraic_varieties/line_bundles#prop2)). Transition functions satisfy the cocycle condition $g_{ij}g_{jk} = g_{ik}$, which corresponds exactly to the Čech 1-cocycle condition written in multiplicative notation. Also, an isomorphism of line bundles changes the transition function by $g_{ij} \mapsto h_i g_{ij} h_j^{-1}$ via functions $h_i \in \mathcal{O}_X^\ast(U_i)$ on each $U_i$, which again matches the equivalence relation given by Čech 1-coboundaries. That is, the isomorphism class of a line bundle naturally corresponds to an element of $\check{H}^1(X, \mathcal{O}_X^\ast)$.

Organizing this observation rigorously gives the following. Note that here $\mathcal{O}_X^\ast$ is a sheaf of (abelian) groups with multiplicative structure, so in Čech cohomology the coboundary relation is expressed multiplicatively rather than additively. Specifically, a 1-coboundary is of the form $(g_{ij}) = (h_i \cdot h_j^{-1})$.

::: Proposition 22
$\check{H}^1(X, \mathcal{O}_X^\ast) \cong \Pic(X)$.
:::

::: Proof
First, we define a map from $\check{H}^1(X, \mathcal{O}_X^\ast)$ to $\Pic(X)$. Given a Čech 1-cocycle $(g_{ij}) \in \check{Z}^1(\mathcal{U}, \mathcal{O}_X^\ast)$, we construct a line bundle $\mathcal{L}$ with this as the transition function. To do this, we take the trivial bundle $U_i \times \mathbb{A}^1$ on each $U_i$, and on $U_i \cap U_j$ we glue by $(p, t) \mapsto (p, g_{ij}(p)t)$. Then by the cocycle condition $g_{ij}g_{jk} = g_{ik}$, this gluing is consistent, so we obtain a well-defined line bundle.

On the other hand, given two cocycles that are equivalent by a coboundary, $g_{ij}^{\mathcal{L}} = h_i g_{ij}^{\mathcal{M}} h_j^{-1}$, we can define an isomorphism between the corresponding two line bundles by $\varphi_i: \mathcal{L}\vert_{U_i} \rightarrow \mathcal{M}\vert_{U_i}$, $v \mapsto h_i^{-1} v$. Then the compatibility of $\varphi_i$ and $\varphi_j$ on $U_i \cap U_j$ is verified by

$$g_{ij}^{\mathcal{M}} \cdot \varphi_j(v) = g_{ij}^{\mathcal{M}} h_j^{-1} v = h_i^{-1} (h_i g_{ij}^{\mathcal{M}} h_j^{-1}) v = h_i^{-1} g_{ij}^{\mathcal{L}} v = \varphi_i(g_{ij}^{\mathcal{L}} v)$$

and thus the map $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \rightarrow \Pic(X)$ is well-defined.

Conversely, any line bundle $\mathcal{L}$ is represented by transition functions $g_{ij}$ on an appropriate open cover $\mathcal{U}$ by [§Line Bundles and Vector Bundles, ⁋Definition 1](/en/math/algebraic_varieties/line_bundles#def1), and these form a Čech 1-cocycle. Since a line bundle isomorphism corresponds exactly to the equivalence relation by coboundaries, the kernel of this map consists of coboundaries. Therefore $\check{H}^1(\mathcal{U}, \mathcal{O}_X^\ast) \rightarrow \Pic(X)$ is injective. Now taking the direct limit gives $\check{H}^1(X, \mathcal{O}_X^\ast) \cong \Pic(X)$.
:::

This proposition shows that the classification of line bundles reduces to a cohomology computation. That is, the problem of classifying elements of $\Pic(X)$ becomes the problem of classifying $\mathcal{O}_X^\ast$-valued Čech 1-cocycles, which is encouraging in that it is at least amenable to explicit computation. In the next post [§Cohomology of Projective Spaces](/en/math/algebraic_varieties/cohomology_of_projective_spaces) we compute the cohomology of the line bundle $\mathcal{O}(d)$ on $\mathbb{P}^n$.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.
**[God]** R. Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.
**[Wei]** C. A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38, Cambridge University Press, 1994.

---

[^1]: More generally, as we saw in [[Topology] §Sheaves, §§The Abelian Category of Sheaves](/en/math/topology/sheaves#the-abelian-category-of-sheaves), the category $$\Sh(X)$$ of sheaves defined on an arbitrary topological space $$X$$ forms an abelian category.
