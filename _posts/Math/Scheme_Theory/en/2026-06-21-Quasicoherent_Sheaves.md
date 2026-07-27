---
title: "Quasi-coherent Sheaves"
description: "We introduce module sheaves over the structure sheaf of a scheme, and show that the associated sheaf of a module gives an equivalence between the category of modules and the category of quasi-coherent sheaves on an affine scheme. Through this, we verify that quasi-coherence is an affine-local property, and discuss locally free sheaves, pullback and pushforward, and the ideal sheaf of a closed subscheme."
excerpt: "Sheaf of O_X-modules, equivalence on affine schemes, and quasi-coherence"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/quasicoherent_sheaves
sidebar: 
    nav: "scheme_theory-en"

date: 2026-06-21
weight: 16
translated_at: 2026-07-27T20:45:02+00:00
translation_source: kimi-cli
---
The structure sheaf $\mathcal{O}_X$ of a scheme $X$ is itself a sheaf of rings, but we often need to deal with sheaves of modules defined over $\mathcal{O}_X$. For instance, on an affine scheme $\Spec A$, the objects of interest—namely, an $A$-module $M$—must be converted into a sheaf on $\Spec A$ in order to connect naturally with geometry; ideal sheaves and line bundles are also examples of such sheaves. However, an arbitrary $\mathcal{O}_X$-module is too coarse to be reduced to algebraic information on an affine. In this post, we define the sheaf constructed directly from a module on an affine, and from this introduce the notion of a *quasi-coherent sheaf*.

## $\mathcal{O}_X$-module

First, we define sheaves of modules on a general ringed space $(X, \mathcal{O}_X)$ ([§Affine Schemes, ⁋Definition 1](/en/math/scheme_theory/affine_schemes#def1)).

::: Definition 1
An abelian group sheaf $\mathcal{F}$ on a ringed space $(X, \mathcal{O}_X)$ is called an *$\mathcal{O}_X$-module* if, for every open set $U$, $\mathcal{F}(U)$ carries the structure of an $\mathcal{O}_X(U)$-module, and this module structure is compatible with the restriction maps. That is, for $V\subseteq U$ and $a\in \mathcal{O}_X(U)$, $s\in \mathcal{F}(U)$, we have

$$(a\cdot s)\vert_V=(a\vert_V)\cdot (s\vert_V)$$

A *morphism* between two $\mathcal{O}_X$-modules $\mathcal{F}, \mathcal{G}$ is a morphism of sheaves $\varphi:\mathcal{F} \rightarrow \mathcal{G}$ such that, for each $U$, the map $\varphi(U):\mathcal{F}(U) \rightarrow \mathcal{G}(U)$ is an $\mathcal{O}_X(U)$-module homomorphism.
:::

In other words, an $\mathcal{O}_X$-module is one for which scalar multiplication followed by restriction coincides with restriction followed by scalar multiplication, and a morphism of $\mathcal{O}_X$-modules is one that preserves this scalar multiplication. These data form the category of $\mathcal{O}_X$-modules, which we denote by $\rMod{\mathcal{O}_X}$. The most basic example is $\mathcal{O}_X$ itself, obtained by viewing each $\mathcal{O}_X(U)$ as a rank $1$ free module over itself. Moreover, an $\mathcal{O}_X$-module inherits a module structure at the level of stalks: for any $x\in X$, the stalk $\mathcal{F}_x=\varinjlim\mathcal{F}(U)$ becomes a module over $\mathcal{O}_{X,x}=\varinjlim\mathcal{O}_X(U)$.

Meanwhile, the standard linear-algebraic operations on general modules carry over directly to $\mathcal{O}_X$-modules.

::: Definition 2
For two $\mathcal{O}_X$-modules $\mathcal{F}, \mathcal{G}$,

1. The *direct sum* $\mathcal{F}\oplus \mathcal{G}$ is the $\mathcal{O}_X$-module given by $U\mapsto \mathcal{F}(U)\oplus \mathcal{G}(U)$ on each open set.
2. The *tensor product* $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$ is the sheafification of the presheaf $U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$.
3. The *Sheaf Hom* $\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$ is the $\mathcal{O}_X$-module given by $U\mapsto \Hom_{\mathcal{O}_X\vert_U}(\mathcal{F}\vert_U, \mathcal{G}\vert_U)$ on each open set.
:::

In the above, for the direct sum and sheaf Hom, the assignment on each open set immediately forms a sheaf, but for the tensor product the presheaf

$$U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$$

may fail to satisfy the sheaf condition, so it is defined via sheafification. ([\[Topology\] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2)) The global sections of the sheaf Hom $\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$ are $\Hom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$, and in particular we have $\sHom_{\mathcal{O}_X}(\mathcal{O}_X, \mathcal{F})\cong \mathcal{F}$.

Thus, although $\mathcal{O}_X$-modules share many formal properties with ordinary modules, they are too general in themselves to be reduced to algebraic information on an affine. What we actually want to handle are the sheaves constructed directly from modules on an affine.

## Associated sheaf on an affine scheme

Now fix an affine scheme $\Spec A$, and suppose an $A$-module $M$ is given. We wish to construct an $\mathcal{O}_{\Spec A}$-module on $\Spec A$ from $M$. The construction is modeled directly on that of the structure sheaf $\mathcal{O}_{\Spec A}$: just as the structure sheaf is given by the localization $A_f$ on a principal open set $D(f)$, we attach the module localization $M_f=S_f^{-1}M$ in the same way. ([§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6))

::: Lemma 3
For an $A$-module $M$, define on the base $\{D(f)\}_{f\in A}$ of $\Spec A$

$$\widetilde M(D(f))=M_f$$

and define the restriction map for $D(f)\subseteq D(g)$ to be the canonical localization map $M_g \rightarrow M_f$. Then these data satisfy the two conditions of [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6), so they extend uniquely to a sheaf on $\Spec A$, and this sheaf is an $\mathcal{O}_{\Spec A}$-module.
:::
::: Proof
First, we verify that the restriction map is well defined when $D(f)\subseteq D(g)$. By the same argument as in [§Affine Schemes, ⁋Lemma 5](/en/math/scheme_theory/affine_schemes#lem5), the inclusion $D(f)\subseteq D(g)$ is equivalent to the image of $g$ being a unit in $A_f$, so by the universal property of $A_g$ the map $M_g=M\otimes_A A_g \rightarrow M\otimes_A A_f=M_f$ is uniquely determined. That this map satisfies the restriction condition of [\[Topology\] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2) is immediate from the functoriality of localization.

We now verify the two sheaf conditions of [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6). The proof follows that of [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6) verbatim, except reading the ring $A$ as the module $M$. Concretely, fix $\Spec A=\bigcup_{i\in I}D(f_i)$. For separation, suppose an element $s\in M$ is zero in every $M_{f_i}$; then for each $i$ there exists $m_i$ such that $f_i^{m_i}s=0$, and from $\Spec A=\bigcup D(f_i^{m_i})$ we obtain $a_i\in A$ with $1=\sum a_i f_i^{m_i}$, so

$$s=\Bigl(\sum_i a_if_i^{m_i}\Bigr)s=\sum_i a_i(f_i^{m_i}s)=0$$

For gluing, if sections $s_i=a_i/f_i^{m_i}\in M_{f_i}$ given on each $D(f_i)$ agree on overlaps, then as in the proof of [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6) we use a partition of unity of the form $1=\sum b_i a_i f_i^{Nm_i+m_i}$ to check that $s=\sum b_i a_i f_i^{Nm_i}\in M$ restricts to $s_i$ on every $D(f_i)$. Apart from replacing the multiplication in $A$ by the scalar action on $M$, all calculations are identical.

Finally, each $\widetilde M(D(f))=M_f$ is a module over $\mathcal{O}_{\Spec A}(D(f))=A_f$, and since the restriction maps are compatible with the scalar action, $\widetilde M$ is an $\mathcal{O}_{\Spec A}$-module.
:::

::: Definition 4
For an $A$-module $M$, the $\mathcal{O}_{\Spec A}$-module $\widetilde M$ on $\Spec A$ defined in [Lemma 3](#lem3) is called the *associated sheaf* of $M$.
:::

By definition, $\widetilde A=\mathcal{O}_{\Spec A}$, and the global sections of $\widetilde M$ are $\widetilde M(\Spec A)=\widetilde M(D(1))=M_1=M$. The following proposition shows that the associated sheaf enjoys the same local properties as the structure sheaf; it is the module version of [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8).

::: Proposition 5
For an $A$-module $M$, the following hold.

1. For any $\mathfrak{p}\in \Spec A$, the stalk is $\widetilde M_\mathfrak{p}\cong M_\mathfrak{p}$.
2. For any $f\in A$, we have $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$. Here the right-hand side is the associated sheaf of the $A_f$-module $M_f$ on $\Spec A_f\cong D(f)$.
:::
::: Proof
For the first result, since the $D(f)$ form a base for $\Spec A$ ([\[Topology\] §Bases of Topological Spaces, ⁋Proposition 5](/en/math/topology/topological_bases#prop5)), we have

$$\widetilde M_\mathfrak{p}=\varinjlim_{D(f)\ni \mathfrak{p}}\widetilde M(D(f))=\varinjlim_{f\not\in \mathfrak{p}}M_f$$

On the other hand, exactly as in the proof of [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8) where $\varinjlim_{f\not\in \mathfrak{p}}A_f\cong A_\mathfrak{p}$ was shown, the universal properties of localization and direct limit yield $\varinjlim_{f\not\in \mathfrak{p}}M_f\cong M_\mathfrak{p}$.

For the second result, [§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2) gives $D(f)\cong \Spec A_f$, and under this isomorphism the principal open sets of $\Spec A_f$ are of the form $D(fg)$ for $g\in A$. Then

$$\widetilde M\vert_{D(f)}(D(fg))=\widetilde M(D(fg))=M_{fg}\cong (M_f)_g=\widetilde{M_f}(D(g))$$

and since these isomorphisms are compatible with the restriction maps, the two sheaves agree on the base, hence $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$.
:::

In particular, from the first result, since all stalks of $\widetilde M$ are given by localizations of $M$, the sheaf $\widetilde M$ encodes all local information of $M$.

## Categorical equivalence

We now show that taking the associated sheaf of a module on an affine scheme yields an equivalence between the category of modules and a suitable category of sheaves. First, we verify that this correspondence is an exact functor.

::: Proposition 6
The correspondence $M\mapsto \widetilde M$ defines a functor $\widetilde{(-)}:\rMod{A} \rightarrow \rMod{\mathcal{O}_{\Spec A}}$, and this functor is exact. That is, a short exact sequence of $A$-modules

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

induces a short exact sequence of $\mathcal{O}_{\Spec A}$-modules

$$0 \rightarrow \widetilde{M'} \rightarrow \widetilde M \rightarrow \widetilde{M''} \rightarrow 0$$
:::
::: Proof
Given an $A$-module homomorphism $\phi:M \rightarrow N$, for each $f\in A$ the localization $\phi_f:M_f \rightarrow N_f$ is induced, and these are compatible with the restriction maps, so they define a morphism of sheaves $\widetilde\phi:\widetilde M \rightarrow \widetilde N$. That this correspondence preserves composition and identity maps is immediate from the functoriality of localization, so $\widetilde{(-)}$ is a functor.

To show exactness, we use the fact that a sequence of sheaves is exact if and only if it is exact at every stalk. By [Proposition 5](#prop5), taking stalks at any $\mathfrak{p}$ turns the given sequence into

$$0 \rightarrow M'_\mathfrak{p} \rightarrow M_\mathfrak{p} \rightarrow M''_\mathfrak{p} \rightarrow 0$$

and since localization is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2)), this sequence is exact. Hence it is exact at the stalk level, and therefore also at the sheaf level.
:::

The associated sheaf functor is also compatible with tensor products and localization. That is, $\widetilde{M\otimes_A N}\cong \widetilde M\otimes_{\mathcal{O}_{\Spec A}}\widetilde N$, and for any $f$ we have $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$ as seen in [Proposition 5](#prop5). The first compatibility follows from the fact that the stalks of both sides are $(M\otimes_A N)_\mathfrak{p}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}N_\mathfrak{p}$.

To obtain one direction of the categorical equivalence that is the main result of this section, we need to know how an arbitrary $\mathcal{O}_{\Spec A}$-module is recovered from a module. The following theorem is the key.

::: Theorem 7
On an affine scheme $\Spec A$, the natural isomorphism

$$\Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)\cong \Hom_A(M, N)$$

holds for any $A$-modules $M, N$. That is, the functor $\widetilde{(-)}:\rMod{A} \rightarrow \rMod{\mathcal{O}_{\Spec A}}$ is fully faithful.
:::
::: Proof
The correspondence $\phi\mapsto \widetilde\phi$ gives $\Hom_A(M, N) \rightarrow \Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)$ by [Proposition 6](#prop6). Conversely, given a morphism $\psi:\widetilde M \rightarrow \widetilde N$, taking global sections yields

$$\psi(\Spec A):\widetilde M(\Spec A)=M \rightarrow N=\widetilde N(\Spec A)$$

giving an $A$-module homomorphism $\phi=\psi(\Spec A)$. It suffices to show that these two correspondences are mutually inverse.

First, starting from $\phi\in \Hom_A(M, N)$, the global section of $\widetilde\phi$ is again $\phi$ by definition, so one direction is trivial. Conversely, suppose $\psi:\widetilde M \rightarrow \widetilde N$ is given and let $\phi=\psi(\Spec A)$. We must show $\widetilde \phi=\psi$; since two morphisms agree if they agree on the base $\{D(f)\}$, it is enough to check on each $D(f)$. For any $f\in A$, because $\psi$ is a sheaf morphism, the following diagram

{% diagram Math/Scheme_Theory/Quasicoherent_Sheaves-1.svg width="6.60em" alt="localization square" %}

commutes, where the vertical morphisms are the localization maps. On the other hand, since $\psi(D(f))$ is an $A_f$-module homomorphism, the condition that it commutes with $\phi$ in the top row and the $A_f$-linearity completely determine the value on any $m/f^n\in M_f$:

$$\psi(D(f))\Bigl(\frac{m}{f^n}\Bigr)=\frac{1}{f^n}\psi(D(f))\Bigl(\frac{m}{1}\Bigr)=\frac{1}{f^n}\frac{\phi(m)}{1}=\frac{\phi(m)}{f^n}=\widetilde\phi(D(f))\Bigl(\frac{m}{f^n}\Bigr)$$

Hence $\psi(D(f))=\widetilde\phi(D(f))$ for all $f$, and therefore $\psi=\widetilde\phi$.
:::

[Theorem 7](#thm7) shows that the associated sheaf functor is fully faithful. However, not every $\mathcal{O}_{\Spec A}$-module is of the form $\widetilde M$, so to obtain the correct categorical equivalence we need a suitable restriction on the sheaf side.

::: Definition 8
An $\mathcal{O}_X$-module $\mathcal{F}$ on a scheme $X$ is called a *quasi-coherent sheaf* if, for every $x\in X$, there exists an affine open neighborhood $U\cong \Spec A$ of $x$ and an $A$-module $M$ such that $\mathcal{F}\vert_U\cong \widetilde M$.
:::

Thus, by definition, a quasi-coherent sheaf is one that is locally an associated sheaf. The quasi-coherent sheaves on $X$ and their morphisms form a full subcategory of $\rMod{\mathcal{O}_X}$, which we denote by $\QCoh(X)$. From this, we can lift [Theorem 7](#thm7) to an equivalence on affines.

::: Theorem 9
For an affine scheme $\Spec A$, the functor

$$\widetilde{(-)}:\rMod{A} \rightarrow \QCoh(\Spec A)$$

is a categorical equivalence.
:::
::: Proof
By [Theorem 7](#thm7), $\widetilde{(-)}$ is fully faithful, so ([\[Category Theory\] §Natural Transformations, ⁋Theorem 5](/en/math/category_theory/natural_transformations#thm5)) it suffices to show that it is essentially surjective. That is, we must show that any quasi-coherent sheaf $\mathcal{F}\in \QCoh(\Spec A)$ is isomorphic to the associated sheaf of some $A$-module.

Let $M=\mathcal{F}(\Spec A)$; we claim $\mathcal{F}\cong \widetilde M$. From the restriction maps, for each $f\in A$ we obtain $M=\mathcal{F}(\Spec A) \rightarrow \mathcal{F}(D(f))$, and since this image is invertible under the action of $f$, the universal property of $A_f$ yields an $A_f$-module homomorphism

$$\theta_f:M_f \rightarrow \mathcal{F}(D(f))$$

These define a morphism $\theta:\widetilde M \rightarrow \mathcal{F}$ on the base $\{D(f)\}$, so it remains to show that $\theta$ is an isomorphism on every stalk.

For this we use the quasi-coherence of $\mathcal{F}$. For each point $\mathfrak{p}$, there exist $g$ with $\mathfrak{p}\in D(g)$ and an $A_g$-module $N$ such that $\mathcal{F}\vert_{D(g)}\cong \widetilde N$. (That the affine open neighborhood in [Definition 8](#def8) can be taken to be a principal open set is because these form a base.) Then $N=\mathcal{F}(D(g))$, and by [Proposition 5](#prop5) the restriction of $\theta$ to $D(g)$ is of the form $\widetilde{M_g} \rightarrow \widetilde N$. Since a morphism between two associated sheaves is determined by its morphism on global sections by [Theorem 7](#thm7), this restriction being an isomorphism is equivalent to the natural localization morphism $M_g=\mathcal{F}(\Spec A)_g \rightarrow \mathcal{F}(D(g))=N$ being an isomorphism. We now verify that this morphism is indeed an isomorphism. Since $\Spec A$ is quasi-compact, we can cover it with finitely many principal opens $D(h_1),\ldots,D(h_m)$ on which $\mathcal{F}$ is an associated sheaf, and the sheaf condition gives the exact sequence

$$0 \rightarrow \mathcal{F}(\Spec A) \rightarrow \prod_i \mathcal{F}(D(h_i)) \rightarrow \prod_{i,j}\mathcal{F}(D(h_ih_j))$$

Since on each $D(h_i)$ and $D(h_ih_j)$ the sheaf $\mathcal{F}$ is an associated sheaf, its sections are $A$-modules and the product is finite, so the complete localization $(-)\otimes_A A_g$ not only preserves the exactness of this sequence but also passes through the product. As a result, localizing the above sequence at $g$ yields an exact sequence that exactly matches the sheaf condition on $D(g)$ for the covering $\{D(h_ig)\}$, giving $M_g\cong \mathcal{F}(D(g))=N$. Here the quasi-compactness of $\Spec A$ was essentially used to guarantee a finite covering. Hence $\theta$ is an isomorphism on each $D(g)$, and therefore an isomorphism on all stalks, so $\theta:\widetilde M \rightarrow \mathcal{F}$ is an isomorphism of sheaves.
:::

[Theorem 9](#thm9) tells us that dealing with quasi-coherent sheaves on an affine scheme is the same as dealing with modules. That is, every quasi-coherent sheaf on $\Spec A$ is completely recovered from its global section module $M=\Gamma(\Spec A, \mathcal{F})$, and this correspondence matches the algebra of modules with the algebra of sheaves via the exactness of [Proposition 6](#prop6) and the compatibility with tensor products mentioned above.

## The affine-local nature of quasi-coherence

What [Definition 8](#def8) requires is only that for each point we can find a suitable affine open neighborhood on which the sheaf is an associated sheaf. However, as the following theorem shows, this condition implies a much stronger property: namely, that the sheaf becomes an associated sheaf on *any* affine open subset of $X$. In this sense, quasi-coherence is an affine-local property.

::: Theorem 10
For an $\mathcal{O}_X$-module $\mathcal{F}$ on a scheme $X$, the following are equivalent.

1. $\mathcal{F}$ is a quasi-coherent sheaf.
2. For every affine open subset $U\cong \Spec A$ of $X$, the associated sheaf of the $A$-module $M_U=\mathcal{F}(U)$ satisfies $\mathcal{F}\vert_U\cong \widetilde{M_U}$.
:::
::: Proof
That the second condition implies the first is immediate from [Definition 8](#def8), so we prove the converse. Suppose $\mathcal{F}$ is a quasi-coherent sheaf and fix an arbitrary affine open subset $U=\Spec A$. We show that $\mathcal{F}\vert_U$ is a quasi-coherent sheaf on $\Spec A$, and then [Theorem 9](#thm9) gives $\mathcal{F}\vert_U\cong \widetilde{M_U}$ (where $M_U=\mathcal{F}(U)$).

By the quasi-coherence of $\mathcal{F}$, for each point $x$ of $U$ there exists an affine open neighborhood $V\cong \Spec B$ (in $X$) and a $B$-module $N$ such that $\mathcal{F}\vert_V\cong \widetilde N$. As in the proof of [§Schemes, ⁋Lemma 3](/en/math/scheme_theory/schemes#lem3), the intersection $U\cap V$ is covered by principal open sets $D(f)$ ($f\in A$) inside $U$, and also by principal open sets $D(g)$ ($g\in B$) inside $V$. Taking these sufficiently small, we obtain an affine open $W=\Spec A_f=\Spec B_g$ containing $x$ that is principal open in both $U$ and $V$.

Now since $\mathcal{F}\vert_V\cong \widetilde N$, by [Proposition 5](#prop5) we have $\mathcal{F}\vert_W\cong \widetilde N\vert_{D(g)}\cong \widetilde{N_g}$, and viewing $W=\Spec A_f$, this is the associated sheaf of the $A_f$-module $N_g$. Hence every point of $U=\Spec A$ has a principal open neighborhood on which $\mathcal{F}\vert_U$ is an associated sheaf, and therefore $\mathcal{F}\vert_U$ is a quasi-coherent sheaf on $\Spec A$.
:::

Thus, verifying that a sheaf is an associated sheaf on a single affine cover is enough to guarantee quasi-coherence, and as a result it automatically becomes an associated sheaf on every affine open subset. Thanks to this affine-locality, many propositions about quasi-coherent sheaves can be reduced to propositions about associated sheaves.

Among quasi-coherent sheaves, those corresponding on affines to finitely generated modules or finitely presented modules are distinguished separately. This works best under a Noetherian hypothesis.

::: Definition 11
A quasi-coherent sheaf $\mathcal{F}$ on a scheme $X$ is of *finite type* if each point has an affine open neighborhood $U\cong \Spec A$ such that $\mathcal{F}\vert_U\cong \widetilde M$ and $M$ is a finitely generated $A$-module. If, moreover, on every affine open $M$ can be taken to be a finitely presented module, then $\mathcal{F}$ is called a *coherent sheaf*.
:::

On a locally Noetherian scheme, finitely generated and finitely presented coincide, so in this case a coherent sheaf is precisely a finite type quasi-coherent sheaf. The coherent sheaves on $X$ form a full subcategory $\Coh(X)$ of $\QCoh(X)$. The simplest example is $\mathcal{O}_X$ itself, which on an affine is $\widetilde A$ and $A$ is a free module over itself, hence a coherent sheaf.

## Locally free sheaf and invertible sheaf

Among quasi-coherent sheaves, those locally corresponding to free modules are especially important as the algebro-geometric counterparts of vector bundles.

::: Definition 12
An $\mathcal{O}_X$-module $\mathcal{E}$ on a scheme $X$ is called a *locally free sheaf of rank $r$* if, for each point $x\in X$, there exists an open neighborhood $U$ such that $\mathcal{E}\vert_U\cong \mathcal{O}_U^{\oplus r}$. A locally free sheaf of rank $1$ is called an *invertible sheaf*.
:::

A locally free sheaf is always quasi-coherent. Indeed, shrinking each point's neighborhood to an affine $\Spec A$, we have $\mathcal{E}\vert_{\Spec A}\cong \mathcal{O}_{\Spec A}^{\oplus r}=\widetilde{A^{\oplus r}}$, which is the associated sheaf of the free module $A^{\oplus r}$. Moreover, if the rank is finite, then $A^{\oplus r}$ is finitely presented, so a locally free sheaf is also coherent.

In [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 23](/en/math/algebraic_varieties/line_bundles#def23), we defined a rank $r$ vector bundle on a variety in terms of local trivialization data, and for rank $1$ we saw that its sheaf of sections is an invertible sheaf. ([\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Proposition 5](/en/math/algebraic_varieties/line_bundles#prop5)) In general rank as well, a local trivialization makes the sheaf of sections into $\mathcal{O}_{U_i}^{\oplus r}$ on each $U_i$, so in the language of schemes a locally free sheaf corresponds exactly to the sheaf of sections of a vector bundle, and in particular an invertible sheaf corresponds to a line bundle. ([\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 1](/en/math/algebraic_varieties/line_bundles#def1)) As the name suggests, an invertible sheaf has an inverse under tensor product.

::: Proposition 13
For an invertible sheaf $\mathcal{L}$, the dual $\mathcal{L}^\vee=\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$ is also an invertible sheaf, and $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$.
:::
::: Proof
Since the problem is local, it suffices to check on an open set $U$ where $\mathcal{L}\vert_U\cong \mathcal{O}_U$. On such a set,

$$\mathcal{L}^\vee\vert_U=\sHom_{\mathcal{O}_U}(\mathcal{O}_U, \mathcal{O}_U)\cong \mathcal{O}_U$$

so $\mathcal{L}^\vee$ is an invertible sheaf. Also, on $U$,

$$(\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee)\vert_U\cong \mathcal{O}_U\otimes_{\mathcal{O}_U}\mathcal{O}_U\cong \mathcal{O}_U$$

and since these local isomorphisms arise from the naturally defined evaluation morphism $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee \rightarrow \mathcal{O}_X$ (given by $s\otimes \phi\mapsto \phi(s)$), they glue to a global isomorphism $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$.
:::

Hence the invertible sheaves form a group under tensor product, with identity $\mathcal{O}_X$ and inverse of $\mathcal{L}$ given by $\mathcal{L}^\vee$. This is the scheme version of the Picard group $\Pic(X)$ defined in [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 9](/en/math/algebraic_varieties/line_bundles#def9).

## Pullback and pushforward

We now examine two operations that move quasi-coherent sheaves along a scheme morphism. Given a morphism $\varphi:X \rightarrow Y$, we define the pushforward, which pushes a sheaf on $X$ to $Y$, and the pullback, which pulls a sheaf on $Y$ back to $X$.

::: Definition 14
Let a scheme morphism $\varphi:X \rightarrow Y$ be given.

1. For an $\mathcal{O}_X$-module $\mathcal{F}$ on $X$, the *pushforward* $\varphi_\ast \mathcal{F}$ is the $\mathcal{O}_Y$-module on $Y$ given by $V\mapsto \mathcal{F}(\varphi^{-1}(V))$ on each open set. ([\[Topology\] §Presheaves, ⁋Example 8](/en/math/topology/presheaves#ex8)) Its module structure is given via the sheaf morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ of the morphism.
2. For an $\mathcal{O}_Y$-module $\mathcal{G}$ on $Y$, the *pullback* $\varphi^\ast \mathcal{G}$ is the $\mathcal{O}_X$-module on $X$ given by the formula

    $$\varphi^\ast \mathcal{G}=\varphi^{-1}\mathcal{G}\otimes_{\varphi^{-1}\mathcal{O}_Y}\mathcal{O}_X$$

    Here $\varphi^{-1}$ is the inverse image sheaf of [\[Topology\] §Sheaves, ⁋Definition 10](/en/math/topology/sheaves#def10).
:::

Both operations reduce on affines to familiar operations on modules. If $\varphi$ comes from a morphism $\Spec B \rightarrow \Spec A$ between affine schemes, that is, from a ring homomorphism $\phi:A \rightarrow B$, then the pullback of an $A$-module $M$ is the extension of scalars $\widetilde{M\otimes_A B}$, and the pushforward of a $B$-module $N$ is the restriction of scalars $\widetilde{\phi^\ast N}$. ([\[Algebraic Structures\] §Change of Base Ring, ⁋Definition 1](/en/math/algebraic_structures/change_of_base_ring#def1), [⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3)) Then the adjunction $\phi_!\dashv \phi^\ast$ of [\[Algebraic Structures\] §Change of Base Ring, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6) translates directly into $\varphi^\ast\dashv \varphi_\ast$.

The natural question now is whether these two operations preserve quasi-coherence, and the answer differs between the two. Pullback always preserves quasi-coherence, but pushforward requires additional conditions. Intuitively, this is because quasi-coherence on an affine chart arises from a presentation of the form

$$\mathcal{O}^{(J)} \rightarrow \mathcal{O}^{(I)} \rightarrow \mathcal{F} \rightarrow 0$$

as a free $\mathcal{O}_X$-module; since $\varphi^\ast$ is a left adjoint, it preserves direct sums and cokernels and thus carries such a presentation over directly, whereas the right adjoint $\varphi_\ast$ does not.

::: Proposition 15
For a scheme morphism $\varphi:X \rightarrow Y$ and a quasi-coherent sheaf $\mathcal{G}$ on $Y$, the pullback $\varphi^\ast \mathcal{G}$ is a quasi-coherent sheaf on $X$.
:::
::: Proof
Since quasi-coherence is an affine-local property ([Theorem 10](#thm10)), it suffices to treat the case $X=\Spec B$, $Y=\Spec A$. Then $\varphi$ comes from a ring homomorphism $\phi:A \rightarrow B$ ([§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11)), and there exists an $A$-module $M$ with $\mathcal{G}=\widetilde M$ ([Theorem 9](#thm9)).

We claim $\varphi^\ast \widetilde M\cong \widetilde{M\otimes_A B}$. To show this, we compare stalks. For any $\mathfrak{q}\in \Spec B$ and $\mathfrak{p}=\phi^{-1}(\mathfrak{q})$, since inverse image and tensor product commute with stalks,

$$(\varphi^\ast \widetilde M)_\mathfrak{q}=(\varphi^{-1}\widetilde M)_\mathfrak{q}\otimes_{(\varphi^{-1}\mathcal{O}_{\Spec A})_\mathfrak{q}}\mathcal{O}_{\Spec B,\mathfrak{q}}\cong \widetilde M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

and ([Proposition 5](#prop5)) on the other hand the stalk of the base change module is

$$(\widetilde{M\otimes_A B})_\mathfrak{q}=(M\otimes_A B)_\mathfrak{q}\cong M\otimes_A B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

Since these isomorphisms are natural, we obtain a sheaf isomorphism $\varphi^\ast \widetilde M\cong \widetilde{M\otimes_A B}$, and hence $\varphi^\ast \mathcal{G}$ is an associated sheaf and therefore quasi-coherent.
:::

For pushforward, quasi-coherence is preserved only when the morphism is quasi-compact and quasi-separated. This is because when computing $\varphi_\ast \mathcal{F}(V)=\mathcal{F}(\varphi^{-1}(V))$ on an affine, one needs to cover $\varphi^{-1}(V)$ with finitely many affines and also control their intersections in order to obtain a module structure compatible with localization.

::: Theorem 16
For a quasi-compact and quasi-separated scheme morphism $\varphi:X \rightarrow Y$ and a quasi-coherent sheaf $\mathcal{F}$ on $X$, the pushforward $\varphi_\ast \mathcal{F}$ is a quasi-coherent sheaf on $Y$.
:::
::: Proof
Since quasi-coherence is an affine-local property ([Theorem 10](#thm10)), it suffices to consider the case $Y=\Spec A$. Since $\varphi$ is quasi-compact, $X$ is covered by finitely many affine open subsets $U_i=\Spec B_i$ ($i=1,\ldots, n$). Also, since $\varphi$ is quasi-separated, each intersection $U_i\cap U_j$ is again covered by finitely many affine opens $U_{ijk}=\Spec C_{ijk}$.

Now let $M=\Gamma(X, \mathcal{F})=\varphi_\ast \mathcal{F}(\Spec A)$; we show $\varphi_\ast \mathcal{F}\cong \widetilde M$. For this, we must verify $\varphi_\ast \mathcal{F}(D(g))\cong M_g$ for each $D(g)\subseteq \Spec A$. By definition, $\varphi_\ast \mathcal{F}(D(g))=\mathcal{F}(\varphi^{-1}(D(g)))$, and by the sheaf condition ([§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6) and the general sheaf axiom for sheaves) we obtain the equalizer

$$\mathcal{F}(\varphi^{-1}(D(g)))=\ker\Bigl(\prod_i \mathcal{F}(U_i\cap \varphi^{-1}(D(g))) \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk}\cap \varphi^{-1}(D(g)))\Bigr)$$

On the other hand, $U_i\cap \varphi^{-1}(D(g))$ is a principal open set of the form $\Spec (B_i)_{g}$, and since $\mathcal{F}\vert_{U_i}$ is quasi-coherent, writing $\mathcal{F}(U_i)=N_i$ we have by [Proposition 5](#prop5)

$$\mathcal{F}(U_i\cap \varphi^{-1}(D(g)))=(N_i)_g\cong \mathcal{F}(U_i)\otimes_A A_g$$

and the same holds for $U_{ijk}$. Since localization $(-)\otimes_A A_g$ is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2)), it commutes with the above equalizer, and since it is defined on a finite product,

$$\mathcal{F}(\varphi^{-1}(D(g)))\cong \ker\Bigl(\prod_i N_i \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk})\Bigr)\otimes_A A_g=M\otimes_A A_g=M_g$$

Here finiteness was essentially used to commute the product with localization, and this is why quasi-compactness and quasi-separatedness are needed. Hence $\varphi_\ast \mathcal{F}(D(g))\cong M_g$ for all $g$, so $\varphi_\ast \mathcal{F}\cong \widetilde M$, which is a quasi-coherent sheaf.
:::

The quasi-compact and quasi-separated hypotheses in [Theorem 16](#thm16) are essential. For instance, for a morphism that requires gluing infinitely many affines, computing sections on $\varphi^{-1}(D(g))$ may involve infinite products, breaking the commutation with localization. However, morphisms between Noetherian schemes, and in particular morphisms between affine schemes, always satisfy these conditions, so in practice pushforward preserves quasi-coherence in most commonly encountered situations.

## Ideal sheaf and closed subscheme

The most important application of the fact that pushforward preserves quasi-coherence is the ideal sheaf determined by a closed subscheme. An ideal $\mathfrak{a}\subseteq A$ of an affine scheme $\Spec A$ is itself an $A$-module, so we can define its associated sheaf $\widetilde{\mathfrak{a}}$, and this is a subsheaf of $\mathcal{O}_{\Spec A}=\widetilde A$. For a general scheme $X$, the ideal sheaf $\mathcal{I}_{Z/X}=\ker\iota^\sharp$ defined by a closed embedding $\iota:Z \rightarrow X$ also gives an ideal on each affine open subset ([§Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5)), but whether these ideals are compatible under localization so that they glue into a single associated sheaf is a separate question. The localization condition required for gluing in [§Closed Subschemes, ⁋Proposition 6](/en/math/scheme_theory/closed_subschemes#prop6) is precisely quasi-coherence, so what needs to be checked is that $\mathcal{I}_{Z/X}$ is a quasi-coherent sheaf. This follows as an application of [Theorem 16](#thm16).

::: Proposition 17
For a closed embedding $\iota:Z \rightarrow X$ ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2)), both $\iota_\ast \mathcal{O}_Z$ and the ideal sheaf $\mathcal{I}_{Z/X}$ are quasi-coherent sheaves on $X$.
:::
::: Proof
Among the three hypotheses of [Theorem 16](#thm16), the fact that $\mathcal{O}_Z$ is a quasi-coherent sheaf on $Z$ follows immediately from $\mathcal{O}_Z\vert_{\Spec B}=\widetilde B$ on each affine open subset $\Spec B\subseteq Z$. Hence we only need to verify that $\iota$ is quasi-compact and quasi-separated. Fix an affine open subset $U\cong \Spec A$ of $X$ and let $W=\iota^{-1}(U)$. Since $\iota$ is a continuous map that is a homeomorphism between $Z$ and a closed subset of $X$, $W$ is homeomorphic to the closed subset $C=\iota(Z)\cap U$ of $U$. But an affine scheme is quasi-compact ([§Spectra, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12)), and a closed subset of a quasi-compact space is quasi-compact, so $W$ is also quasi-compact. That is, $\iota$ is a quasi-compact morphism. ([§Properties of Scheme Morphisms, ⁋Definition 2](/en/math/scheme_theory/properties_of_scheme_morphisms#def2))

Quasi-separatedness is also checked from the topology of $C$ alone. Since $\{D(f)\}_{f\in A}$ is a base for $U$, any open subset of $C$ is a union of sets of the form $C\cap D(f)$, and each $C\cap D(f)$ is a closed subset of $D(f)\cong \Spec A_f$ which is quasi-compact, hence quasi-compact. Thus any quasi-compact open subset of $C$ can be written as a finite union of such $C\cap D(f)$, and the intersection of two such sets is a finite union of sets of the form $C\cap D(f)\cap D(g)=C\cap D(fg)$, which is again quasi-compact. That is, $W$ is a quasi-separated scheme, and since $U$ was an arbitrary affine open subset, $\iota$ is a quasi-separated morphism. ([§Properties of Scheme Morphisms, ⁋Definition 5](/en/math/scheme_theory/properties_of_scheme_morphisms#def5)) By [Theorem 16](#thm16), $\iota_\ast \mathcal{O}_Z$ is a quasi-coherent sheaf on $X$.

It remains to treat $\mathcal{I}_{Z/X}=\ker\iota^\sharp$. Since quasi-coherence is affine-local ([Theorem 10](#thm10)), it suffices to check on the fixed $U=\Spec A$ above. Let $N=(\iota_\ast \mathcal{O}_Z)(U)$; then by [Theorem 10](#thm10) we have $(\iota_\ast \mathcal{O}_Z)\vert_U\cong \widetilde N$, so the restriction of $\iota^\sharp$ to $U$ is a morphism $\widetilde A \rightarrow \widetilde N$, which by [Theorem 7](#thm7) is the associated sheaf $\widetilde\phi$ of some $A$-module homomorphism $\phi:A \rightarrow N$. Then applying [Proposition 6](#prop6) to the two short exact sequences

$$0 \rightarrow \ker\phi \rightarrow A \rightarrow \im\phi \rightarrow 0,\qquad 0 \rightarrow \im\phi \rightarrow N \rightarrow N/\im\phi \rightarrow 0$$

we obtain that $\widetilde{\im\phi} \rightarrow \widetilde N$ is injective and $\widetilde{\ker\phi}=\ker(\widetilde A \rightarrow \widetilde{\im\phi})$, hence ultimately $\ker\widetilde\phi=\widetilde{\ker\phi}$. That is, $\mathcal{I}_{Z/X}\vert_U\cong \widetilde{\ker\phi}$ is an associated sheaf, and therefore $\mathcal{I}_{Z/X}$ is a quasi-coherent sheaf.
:::

Thus, the closed subschemes of $X$ correspond exactly to the quasi-coherent ideal sheaves of $\mathcal{O}_X$, that is, to quasi-coherent subsheaves of $\mathcal{O}_X$-modules. One direction is given by [Proposition 17](#prop17); conversely, given such an $\mathcal{I}$, for each affine open subset $\Spec A$ the module $\mathcal{I}(\Spec A)$ is an ideal of $A$, and by [Theorem 10](#thm10) and [Lemma 3](#lem3) we have $\mathcal{I}(D(f))\cong \mathcal{I}(\Spec A)_f$, so by [§Closed Subschemes, ⁋Proposition 6](/en/math/scheme_theory/closed_subschemes#prop6) the ideal sheaf $\mathcal{I}$ induces a unique closed subscheme of $X$. This correspondence is none other than the correspondence between an ideal $\mathfrak{a}\subseteq A$ and the quotient $A/\mathfrak{a}$ on an affine. Moreover, [Proposition 17](#prop17) is also the fact that was used without proof in the proof of [§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3).

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
