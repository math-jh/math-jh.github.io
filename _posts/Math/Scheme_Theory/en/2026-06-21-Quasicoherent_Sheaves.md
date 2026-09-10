---
title: "Quasi-Coherent Sheaves"
description: "We introduce sheaves of modules over the structure sheaf of a scheme and show that the associated sheaf functor on affine schemes yields an equivalence between the category of modules and the category of quasi-coherent sheaves. We then verify that quasi-coherence is an affine-local property and discuss locally free sheaves, pullback and pushforward operations, and ideal sheaves of closed subschemes."
excerpt: "Sheaves of modules, equivalence on affine schemes, and quasi-coherence"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/quasicoherent_sheaves
sidebar: 
    nav: "scheme_theory-en"

date: 2026-06-21
weight: 16
translated_at: 2026-09-06T15:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
The structure sheaf $\mathcal{O}_X$ of a scheme $X$ is itself a sheaf of rings, but we often need to deal with sheaves of modules defined over $\mathcal{O}_X$. For example, the objects we are interested in on an affine scheme $\Spec A$, namely $A$-modules $M$, naturally connect to geometry only after being turned into sheaves on $\Spec A$; ideal sheaves and line bundles are also examples of such sheaves. However, an arbitrary $\mathcal{O}_X$-module is too wild to be reduced to algebraic data on affine schemes. In this post, we define sheaves constructed directly from modules on affine schemes, and from these introduce the notion of a *quasi-coherent sheaf*.

## $\mathcal{O}_X$-modules

First, we define sheaves of modules on a general ringed space $(X, \mathcal{O}_X)$ ([§Affine Scheme, ⁋Definition 1](/en/math/scheme_theory/affine_schemes#def1){: data-relation="weak" }).

::: Definition 1
A sheaf of abelian groups $\mathcal{F}$ on a ringed space $(X, \mathcal{O}_X)$ is an *$\mathcal{O}_X$-module* if, for every open set $U$, $\mathcal{F}(U)$ has the structure of an $\mathcal{O}_X(U)$-module, and this module structure is compatible with restriction maps. That is, for $V\subseteq U$, $a\in \mathcal{O}_X(U)$, and $s\in \mathcal{F}(U)$,

$$(a\cdot s)\vert_V=(a\vert_V)\cdot (s\vert_V)$$

holds. A *morphism* between two $\mathcal{O}_X$-modules $\mathcal{F}, \mathcal{G}$ is a morphism of sheaves $\varphi:\mathcal{F} \rightarrow \mathcal{G}$ such that for each $U$, $\varphi(U):\mathcal{F}(U) \rightarrow \mathcal{G}(U)$ is an $\mathcal{O}_X(U)$-module homomorphism.
:::

That is, an $\mathcal{O}_X$-module is one where scalar multiplication followed by restriction agrees with restriction followed by scalar multiplication, and a morphism of $\mathcal{O}_X$-modules is one that preserves this scalar multiplication. These data form a category of $\mathcal{O}_X$-modules, which we denote by $\rMod{\mathcal{O}_X}$. The most basic example is $\mathcal{O}_X$ itself, which is the $\mathcal{O}_X$-module obtained by regarding each $\mathcal{O}_X(U)$ as a free module of rank $1$ over itself. Moreover, an $\mathcal{O}_X$-module inherits a module structure at the stalk level as well. That is, for any $x\in X$, the stalk $\mathcal{F}_x=\varinjlim\mathcal{F}(U)$ becomes a module over $\mathcal{O}_{X,x}=\varinjlim\mathcal{O}_X(U)$.

Meanwhile, linear algebraic operations on general modules carry over directly to $\mathcal{O}_X$-modules.

::: Definition 2
For two $\mathcal{O}_X$-modules $\mathcal{F}, \mathcal{G}$ and an integer $r\geq 0$,

1. The *direct sum* $\mathcal{F}\oplus \mathcal{G}$ is the $\mathcal{O}_X$-module given on each open set by $U\mapsto \mathcal{F}(U)\oplus \mathcal{G}(U)$.
2. The *tensor product* $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$ is the sheafification of the presheaf $U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$.
3. The *sheaf Hom* $\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$ is the $\mathcal{O}_X$-module given on each open set by $U\mapsto \Hom_{\mathcal{O}_X\vert_U}(\mathcal{F}\vert_U, \mathcal{G}\vert_U)$.
4. The *exterior power* $\bigwedge^r\mathcal{F}$ is the sheafification of the presheaf $U\mapsto \bigwedge^r_{\mathcal{O}_X(U)}\bigl(\mathcal{F}(U)\bigr)$. ([\[Multilinear Algebra\] §Tensor Algebra, ⁋Definition 10](/en/math/multilinear_algebra/tensor_algebras#def10){: data-relation="weak" })
:::

Above, in the cases of the direct sum and sheaf Hom, the assignment on each open set directly forms a sheaf; however, for the tensor product, the presheaf

$$U\mapsto \mathcal{F}(U)\otimes_{\mathcal{O}_X(U)}\mathcal{G}(U)$$

may fail to satisfy the sheaf condition, so it is defined via sheafification. ([\[Topology\] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2){: data-relation="weak" }) The exterior power requires sheafification for the same reason. The global sections of the sheaf Hom $\sHom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$ are $\Hom_{\mathcal{O}_X}(\mathcal{F}, \mathcal{G})$, and in particular, $\sHom_{\mathcal{O}_X}(\mathcal{O}_X, \mathcal{F})\cong \mathcal{F}$ holds.

The items in [Definition 2](#def2){: data-relation="weak" } are merely the ones we will use going forward; any linear algebraic construction on modules carries over in the same way. Specifically, we apply the construction to the $\mathcal{O}_X(U)$-modules on each open set, and if the resulting presheaf is not a sheaf, take its sheafification. For example, this is the case for the tensor power $\mathcal{F}^{\otimes r}$ and symmetric power $\Sym^r\mathcal{F}$, as well as the tensor algebra $\T(\mathcal{F})$, symmetric algebra $\S(\mathcal{F})$, and exterior algebra $\bigwedge\mathcal{F}$ that assemble them ([\[Multilinear Algebra\] §Tensor Algebra, ⁋Definition 1](/en/math/multilinear_algebra/tensor_algebras#def1){: data-relation="weak" }), and similarly for direct sums and direct products over arbitrary index sets. As such, $\mathcal{O}_X$-modules share formal properties similar to general modules, but they are too general in themselves to be reduced to algebraic data on affine schemes. What we actually want to work with are the sheaves constructed directly from modules on affine schemes.

## Associated Sheaves on Affine Schemes

Now fix an affine scheme $\Spec A$, and suppose an $A$-module $M$ is given. We want to construct an $\mathcal{O}_{\Spec A}$-module on $\Spec A$ from $M$. The construction closely mirrors that of the structure sheaf $\mathcal{O}_{\Spec A}$: just as the structure sheaf was given on a principal open set $D(f)$ by the localization $A_f$, we glue the localizations of the module $M_f=S_f^{-1}M$ in the same manner. ([§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-relation="required" })

::: Lemma 3
For an $A$-module $M$, define on the base $\{D(f)\}_{f\in A}$ of $\Spec A$

$$\widetilde M(D(f))=M_f$$

and define the restriction map for $D(f)\subseteq D(g)$ to be the canonical localization map $M_g \rightarrow M_f$. Then this data satisfies the two conditions of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8){: data-relation="required" } and uniquely extends to a sheaf on $\Spec A$, which is an $\mathcal{O}_{\Spec A}$-module.
:::
::: Proof
First, we show that the restriction map is well-defined when $D(f)\subseteq D(g)$. By the same argument as in [§Affine Scheme, ⁋Lemma 5](/en/math/scheme_theory/affine_schemes#lem5){: data-relation="required" }, $D(f)\subseteq D(g)$ is equivalent to the image of $g$ being a unit in $A_f$, so by the universal property of $A_g$, the map $M_g=M\otimes_A A_g \rightarrow M\otimes_A A_f=M_f$ is uniquely determined. That this map satisfies the restriction conditions of [\[Topology\] §Presheaves, ⁋Definition 2](/en/math/topology/presheaves#def2){: data-relation="required" } is clear from the functoriality of localization.

Now we show the two sheaf conditions of [\[Topology\] §Sheaves, ⁋Proposition 8](/en/math/topology/sheaves#prop8){: data-relation="required" }. The proof follows the proof of [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-relation="required" } verbatim, replacing the ring $A$ that appears there with the module $M$. Specifically, fix $\Spec A=\bigcup_{i\in I}D(f_i)$. To show separability, suppose an element $s\in M$ is $0$ in all $M_{f_i}$; then for each $i$ there exists $m_i$ such that $f_i^{m_i}s=0$, and from $\Spec A=\bigcup D(f_i^{m_i})$, if we choose $a_i\in A$ such that $1=\sum a_i f_i^{m_i}$, we have

$$s=\Bigl(\sum_i a_if_i^{m_i}\Bigr)s=\sum_i a_i(f_i^{m_i}s)=0$$

. For gluing, if sections $s_i=a_i/f_i^{m_i}\in M_{f_i}$ given on each $D(f_i)$ agree on the overlaps, then in the same manner as in the proof of [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-relation="required" }, using a partition of unity of the form $1=\sum b_i a_i f_i^{Nm_i+m_i}$, we verify that $s=\sum b_i a_i f_i^{Nm_i}\in M$ restricts to $s_i$ on every $D(f_i)$. In this argument, all calculations are identical except that multiplication in $A$ is replaced by the scalar action on $M$.

Finally, each $\widetilde M(D(f))=M_f$ is a module over $\mathcal{O}_{\Spec A}(D(f))=A_f$, and since the restriction maps are compatible with the scalar action, $\widetilde M$ is an $\mathcal{O}_{\Spec A}$-module.
:::

::: Definition 4
For an $A$-module $M$, the $\mathcal{O}_{\Spec A}$-module $\widetilde M$ on $\Spec A$ defined in [Lemma 3](#lem3){: data-relation="required" } is called the *associated sheaf* of $M$.
:::

By definition, $\widetilde A=\mathcal{O}_{\Spec A}$, and the global sections of $\widetilde M$ are $\widetilde M(\Spec A)=\widetilde M(D(1))=M_1=M$. The following proposition shows that the associated sheaf has the same local properties as the structure sheaf, which is the module version of [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-relation="weak" }.

::: Proposition 5
For an $A$-module $M$, the following hold:

1. For any $\mathfrak{p}\in \Spec A$, the stalk is $\widetilde M_\mathfrak{p}\cong M_\mathfrak{p}$.
2. For any $f\in A$, $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$. Here, the right-hand side is the associated sheaf of the $A_f$-module $M_f$ on $\Spec A_f\cong D(f)$.
:::
::: Proof
For the first statement, since the $D(f)$ form a base of $\Spec A$ ([\[Topology\] §Bases of a Topological Space, ⁋Proposition 5](/en/math/topology/topological_bases#prop5){: data-relation="required" }),

$$\widetilde M_\mathfrak{p}=\varinjlim_{D(f)\ni \mathfrak{p}}\widetilde M(D(f))=\varinjlim_{f\not\in \mathfrak{p}}M_f$$

holds. Meanwhile, in the same way as showing $\varinjlim_{f\not\in \mathfrak{p}}A_f\cong A_\mathfrak{p}$ in the proof of [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-relation="required" }, from the universal properties of localization and direct limits we obtain $\varinjlim_{f\not\in \mathfrak{p}}M_f\cong M_\mathfrak{p}$.

For the second statement, by [§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2){: data-relation="required" } we have $D(f)\cong \Spec A_f$, and under this isomorphism, principal open sets of $\Spec A_f$ are of the form $D(fg)$ for $g\in A$. Then

$$\widetilde M\vert_{D(f)}(D(fg))=\widetilde M(D(fg))=M_{fg}\cong (M_f)_g=\widetilde{M_f}(D(g))$$

and since these isomorphisms are compatible with the restriction maps, the two sheaves coincide on the base, and thus $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$.
:::

In particular, from the first statement, since the stalks of $\widetilde M$ are all given by localizations of $M$, $\widetilde M$ contains all local information of $M$.

## Categorical equivalence

We now show that the assignment of taking the associated sheaf of a module on an affine scheme gives an equivalence between the category of modules and an appropriate category of sheaves. First, we verify that this assignment is an exact functor.

::: Proposition 6
The correspondence $M\mapsto \widetilde M$ defines a functor $\widetilde{(-)}:\rMod{A} \rightarrow \rMod{\mathcal{O}_{\Spec A}}$, which is exact. That is, a short exact sequence of $A$-modules

$$0 \rightarrow M' \rightarrow M \rightarrow M'' \rightarrow 0$$

induces a short exact sequence of $\mathcal{O}_{\Spec A}$-modules

$$0 \rightarrow \widetilde{M'} \rightarrow \widetilde M \rightarrow \widetilde{M''} \rightarrow 0$$
:::
::: Proof
Given an $A$-module homomorphism $\phi:M \rightarrow N$, for each $f\in A$ a localization $\phi_f:M_f \rightarrow N_f$ is induced, and since these are compatible with the restriction maps, they define a morphism of sheaves $\widetilde\phi:\widetilde M \rightarrow \widetilde N$. That this assignment preserves composition and identity morphisms is clear from the functoriality of localization, so $\widetilde{(-)}$ is a functor.

To show exactness, we use the fact that a sequence of sheaves is exact if and only if it is exact at every stalk. Taking stalks at an arbitrary $\mathfrak{p}$ by [Proposition 5](#prop5){: data-relation="required" }, the given sequence becomes

$$0 \rightarrow M'_\mathfrak{p} \rightarrow M_\mathfrak{p} \rightarrow M''_\mathfrak{p} \rightarrow 0$$

and since localization is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-relation="required" }), this sequence is exact. Therefore, it is exact at the stalk level, which implies that it is also exact at the sheaf level.
:::

The associated sheaf functor is also compatible with tensor products and localization. That is, $\widetilde{M\otimes_A N}\cong \widetilde M\otimes_{\mathcal{O}_{\Spec A}}\widetilde N$, and for any $f$, the isomorphism $\widetilde M\vert_{D(f)}\cong \widetilde{M_f}$ seen in [Proposition 5](#prop5){: data-relation="required" } holds. The first compatibility follows from the fact that the stalks on both sides coincide as $(M\otimes_A N)_\mathfrak{p}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}N_\mathfrak{p}$.

Now, for one direction of the categorical equivalence that is the result of this section, we need to know how an arbitrary $\mathcal{O}_{\Spec A}$-module is recovered from a module. The following theorem is key.

::: Theorem 7
On an affine scheme $\Spec A$, the natural isomorphism

$$\Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)\cong \Hom_A(M, N)$$

holds for any $A$-modules $M, N$. That is, the functor $\widetilde{(-)}:\rMod{A} \rightarrow \rMod{\mathcal{O}_{\Spec A}}$ is fully faithful.
:::
::: Proof
By [Proposition 6](#prop6){: data-relation="required" }, the assignment $\phi\mapsto \widetilde\phi$ gives a map $\Hom_A(M, N) \rightarrow \Hom_{\mathcal{O}_{\Spec A}}(\widetilde M, \widetilde N)$. Conversely, given a morphism $\psi:\widetilde M \rightarrow \widetilde N$, taking it on global sections

$$\psi(\Spec A):\widetilde M(\Spec A)=M \rightarrow N=\widetilde N(\Spec A)$$

yields an $A$-module homomorphism $\phi=\psi(\Spec A)$. It suffices to show that these two assignments are inverses of each other.

First, starting from $\phi\in \Hom_A(M, N)$, the global section of $\widetilde\phi$ is again $\phi$ by definition, so one direction is trivial. Conversely, suppose $\psi:\widetilde M \rightarrow \widetilde N$ is given and let $\phi=\psi(\Spec A)$. We must show that $\widetilde \phi=\psi$, and for the two morphisms to agree, it suffices that they agree on the base $\{D(f)\}$. For any $f\in A$, since $\psi$ is a sheaf morphism, the diagram

{% diagram Math/Scheme_Theory/Quasicoherent_Sheaves-1.svg width="6.60em" alt="localization square" %}

commutes, where the vertical morphisms are localization maps. On the other hand, since $\psi(D(f))$ is an $A_f$-module homomorphism, the condition that it commutes with $\phi$ in the top row along with $A_f$-linearity completely determines it for any $m/f^n\in M_f$ by

$$\psi(D(f))\Bigl(\frac{m}{f^n}\Bigr)=\frac{1}{f^n}\psi(D(f))\Bigl(\frac{m}{1}\Bigr)=\frac{1}{f^n}\frac{\phi(m)}{1}=\frac{\phi(m)}{f^n}=\widetilde\phi(D(f))\Bigl(\frac{m}{f^n}\Bigr)$$

Therefore, $\psi(D(f))=\widetilde\phi(D(f))$ holds for all $f$, which implies $\psi=\widetilde\phi$.
:::

[Theorem 7](#thm7){: data-relation="required" } shows that the associated sheaf functor is fully faithful. However, since not every $\mathcal{O}_{\Spec A}$-module is of the form of an associated sheaf, an appropriate restriction on the category of sheaves is necessary to obtain the right kind of categorical equivalence. 

::: Definition 8
On a scheme $X$, an $\mathcal{O}_X$-module $\mathcal{F}$ is a *quasi-coherent sheaf* if for each $x\in X$, $x$ has an affine open neighborhood $U\cong \Spec A$ such that for some $A$-module $M$, we have $\mathcal{F}\vert_U\cong \widetilde M$.
:::

That is, by definition, quasi-coherent sheaves are those that locally appear as associated sheaves. The quasi-coherent sheaves on $X$ and morphisms between them form a full subcategory of $\rMod{\mathcal{O}_X}$, denoted by $\QCoh(X)$. From this, we can promote [Theorem 7](#thm7){: data-relation="required" } to an equivalence over affine schemes.

::: Theorem 9
For an affine scheme $\Spec A$, the functor

$$\widetilde{(-)}:\rMod{A} \rightarrow \QCoh(\Spec A)$$

is a categorical equivalence.
:::
::: Proof
Since $\widetilde{(-)}$ is fully faithful by [Theorem 7](#thm7){: data-relation="required" }, it suffices to show that it is essentially surjective ([\[Category Theory\] §Natural Transformations, ⁋Theorem 5](/en/math/category_theory/natural_transformations#thm5){: data-relation="required" }). That is, we must show that any quasi-coherent sheaf $\mathcal{F}\in \QCoh(\Spec A)$ is isomorphic to the associated sheaf of some $A$-module.

Let $M=\mathcal{F}(\Spec A)$; we claim that $\mathcal{F}\cong \widetilde M$. From the restriction maps, for each $f\in A$, a map $M=\mathcal{F}(\Spec A) \rightarrow \mathcal{F}(D(f))$ is induced, and since its image is invertible under the action of $f$, the universal property of $A_f$ determines an $A_f$-module homomorphism

$$\theta_f:M_f \rightarrow \mathcal{F}(D(f))$$

On the base $\{D(f)\}$, these define a morphism $\theta:\widetilde M \rightarrow \mathcal{F}$, so it suffices to show that $\theta$ is an isomorphism on each stalk.

To this end, we use the quasi-coherence of $\mathcal{F}$. For each point $\mathfrak{p}$, we have $\mathfrak{p}\in D(g)$ and $\mathcal{F}\vert_{D(g)}\cong \widetilde N$ for some $g$ and some $A_g$-module $N$. Here, the reason we can shrink the affine open neighborhood in [Definition 8](#def8){: data-relation="required" } to a principal open set is that, as in the proof of [§Schemes, ⁋Lemma 3](/en/math/scheme_theory/schemes#lem3){: data-relation="required" }, we can choose inside that neighborhood a neighborhood that is simultaneously a principal open set of $\Spec A$ and a principal open set of the neighborhood itself, on which it is again an associated sheaf by the second result of [Proposition 5](#prop5){: data-relation="required" }. Then $N=\mathcal{F}(D(g))$, and by [Proposition 5](#prop5){: data-relation="required" }, restricted to $D(g)$, $\theta$ is of the form $\widetilde{M_g} \rightarrow \widetilde N$. Since a morphism between two associated sheaves is determined by its morphism on global sections by [Theorem 7](#thm7){: data-relation="required" }, this restriction being an isomorphism is equivalent to the natural localization morphism $M_g=\mathcal{F}(\Spec A)_g \rightarrow \mathcal{F}(D(g))=N$ being an isomorphism. We now verify that this morphism is an isomorphism. Because $\Spec A$ is quasi-compact, by taking opens on which $\mathcal{F}$ is an associated sheaf, finitely many principal open sets $D(h_1),\ldots,D(h_m)$ can cover $\Spec A$, and the sheaf condition yields the exact sequence

$$0 \rightarrow \mathcal{F}(\Spec A) \rightarrow \prod_i \mathcal{F}(D(h_i)) \rightarrow \prod_{i,j}\mathcal{F}(D(h_ih_j))$$

On each $D(h_i)$ and $D(h_ih_j)$, since $\mathcal{F}$ is an associated sheaf, its sections are $A$-modules, and since the products are finite, the exact functor of localization $(-)\otimes_A A_g$ not only preserves the exactness of this sequence but also passes through the direct products. As a result, localizing the above sequence at $g$ yields an exact sequence that coincides precisely with the sheaf condition for the covering $\{D(h_ig)\}$ on $D(g)$, and we obtain $M_g\cong \mathcal{F}(D(g))=N$. Here, the quasi-compactness of $\Spec A$ was essentially used to guarantee a finite covering. Therefore, $\theta$ is an isomorphism on each $D(g)$, and hence is an isomorphism at every stalk; thus $\theta:\widetilde M \rightarrow \mathcal{F}$ is an isomorphism of sheaves.
:::

[Theorem 9](#thm9){: data-relation="forward" } tells us that working with quasi-coherent sheaves on an affine scheme is equivalent to working with modules. That is, every quasi-coherent sheaf on $\Spec A$ is completely recovered from its module of global sections $M=\Gamma(\Spec A, \mathcal{F})$, and this correspondence identifies the algebra of modules with the algebra of sheaves through the exactness from [Proposition 6](#prop6){: data-relation="weak" } and the compatibility with tensor products mentioned above.

## Affine-Local Property of Quasi-Coherence

All that [Definition 8](#def8){: data-relation="required" } requires is finding a suitable affine open neighborhood for each point and verifying that it is an associated sheaf on that neighborhood. However, as the following theorem shows, this condition implies a much stronger property, namely that it is an associated sheaf on any affine open subset of $X$. In this sense, quasi-coherence is an affine-local property.

::: Theorem 10
For an $\mathcal{O}_X$-module $\mathcal{F}$ on a scheme $X$, the following are equivalent.

1. $\mathcal{F}$ is a quasi-coherent sheaf.
2. For every affine open subset $U\cong \Spec A$ of $X$, the associated sheaf of the $A$-module $M_U=\mathcal{F}(U)$ gives $\mathcal{F}\vert_U\cong \widetilde{M_U}$.
:::
::: Proof
That the second condition implies the first is trivial from [Definition 8](#def8){: data-relation="required" }, so we prove the converse. Suppose $\mathcal{F}$ is a quasi-coherent sheaf, and fix an arbitrary affine open subset $U=\Spec A$. If we show that $\mathcal{F}\vert_U$ is a quasi-coherent sheaf on $\Spec A$, then by [Theorem 9](#thm9){: data-relation="required" } it follows that $\mathcal{F}\vert_U\cong \widetilde{M_U}$ (where $M_U=\mathcal{F}(U)$).

By the quasi-coherence of $\mathcal{F}$, each point of $U$, say $x$, admits an affine open neighborhood $V\cong \Spec B$ (in $X$) and a $B$-module $N$ such that $\mathcal{F}\vert_V\cong \widetilde N$. As in the proof of [§Schemes, ⁋Lemma 3](/en/math/scheme_theory/schemes#lem3){: data-relation="required" }, $U\cap V$ is covered in $U$ by principal open sets $D(f)$ ($f\in A$), and also in $V$ by principal open sets $D(g)$ ($g\in B$). Taking this small enough to satisfy both simultaneously, we obtain an open set containing $x$ which is a principal open set of both $U$ and $V$, namely an affine open $W=\Spec A_f=\Spec B_g$.

Now, since $\mathcal{F}\vert_V\cong \widetilde N$, by [Proposition 5](#prop5){: data-relation="required" } we have $\mathcal{F}\vert_W\cong \widetilde N\vert_{D(g)}\cong \widetilde{N_g}$, and viewed via $W=\Spec A_f$, this is the associated sheaf of the $A_f$-module $N_g$. Therefore, each point of $U=\Spec A$ has a principal open neighborhood on which $\mathcal{F}\vert_U$ is an associated sheaf, and from this, $\mathcal{F}\vert_U$ is a quasi-coherent sheaf on $\Spec A$.
:::

Therefore, merely checking that it is an associated sheaf on some affine cover guarantees quasi-coherence, and as a consequence, it automatically becomes an associated sheaf on every affine open subset. Thanks to this affine-locality, many propositions concerning quasi-coherent sheaves can be proven by reducing them to statements about associated sheaves.

Among quasi-coherent sheaves, we specifically distinguish those that correspond to finitely generated modules or finitely presented modules over affines. This works best under the Noetherian hypothesis.

::: Definition 11
On a scheme $X$, a quasi-coherent sheaf $\mathcal{F}$ is said to be of *finite type* if each point has an affine open neighborhood $U\cong \Spec A$ such that $\mathcal{F}\vert_U\cong \widetilde M$ and $M$ is a finitely generated $A$-module. If, in addition, each point has such an affine open neighborhood on each of which $M$ can be chosen to be a finitely presented $A$-module, we call $\mathcal{F}$ a *coherent sheaf*.
:::

On a locally Noetherian scheme, finitely generated and finitely presented coincide, so in this case a coherent sheaf is simply a quasi-coherent sheaf of finite type. The coherent sheaves on $X$ form a full subcategory of $\QCoh(X)$, denoted $\Coh(X)$. The simplest example is $\mathcal{O}_X$ itself; on an affine it is $\widetilde A$, and since $A$ is a free module over itself, it is a coherent sheaf.

The finite type condition spreads generation at a single point to its neighborhood. Suppose $\mathcal{F}$ is of finite type, and on the affine open neighborhood $U=\Spec A$ given by [Definition 11](#def11){: data-relation="required" }, let $\mathcal{F}\vert_U\cong\widetilde M$. Given a point $x\in U$, let $\mathfrak{p}$ be the corresponding prime. If the images of $m_1,\ldots, m_r\in M$ generate the stalk $M_\mathfrak{p}$, then since $N=M/\sum_iAm_i$ is finitely generated with $N_\mathfrak{p}=0$, each generator of $N$ is annihilated by an element outside $\mathfrak{p}$, and since $\mathfrak{p}$ is prime, their product $f$ also does not belong to $\mathfrak{p}$, so from $fN=0$ we have $N_f=0$. In other words, over the neighborhood $D(f)$ of that point, sections generating the stalk always generate the whole of $\mathcal{F}$.

## Locally Free Sheaves and Invertible Sheaves

Among quasi-coherent sheaves, those that locally correspond to free modules are especially important as the algebraic-geometric counterparts of vector bundles.

::: Definition 12
On a scheme $X$, an $\mathcal{O}_X$-module $\mathcal{E}$ is a *locally free sheaf of rank $r$* if for each point $x\in X$ there exists an open neighborhood $U$ such that $\mathcal{E}\vert_U\cong \mathcal{O}_U^{\oplus r}$. A locally free sheaf of rank $1$ is called an *invertible sheaf*.
:::

A locally free sheaf is always a quasi-coherent sheaf. Indeed, shrinking the neighborhood of each point to an affine $\Spec A$, we have $\mathcal{E}\vert_{\Spec A}\cong \mathcal{O}_{\Spec A}^{\oplus r}=\widetilde{A^{\oplus r}}$, so this is the associated sheaf of the free module $A^{\oplus r}$. Moreover, if the rank is finite, $A^{\oplus r}$ is finitely presented, so a locally free sheaf is also a coherent sheaf.

In [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 23](/en/math/algebraic_varieties/line_bundles#def23){: data-relation="weak" }, we defined a vector bundle of rank $r$ on a variety by the data of local trivializations, and showed that in the case of rank $1$, its section sheaf is an invertible sheaf. ([\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Proposition 5](/en/math/algebraic_varieties/line_bundles#prop5){: data-relation="required" }) For general rank as well, since local trivializations identify the section sheaf on each $U_i$ with $\mathcal{O}_{U_i}^{\oplus r}$, in the language of schemes a locally free sheaf corresponds precisely to the section sheaf of this vector bundle, and in particular an invertible sheaf corresponds to a line bundle. ([\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 1](/en/math/algebraic_varieties/line_bundles#def1){: data-relation="weak" }) As its name suggests, an invertible sheaf has an inverse with respect to the tensor product.

The analogue of the fiber of a vector bundle over each point also translates directly into the language of sheaves. For an $\mathcal{O}_X$-module $\mathcal{F}$ and a point $x\in X$, using the residue field $\kappa(x)=\mathcal{O}_{X,x}/\mathfrak{m}_x$ defined in [§Schemes](/en/math/scheme_theory/schemes){: data-relation="required" }, we define the *fiber* of $\mathcal{F}$ at $x$ to be

$$\mathcal{F}\otimes\kappa(x)=\mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\kappa(x)=\mathcal{F}_x/\mathfrak{m}_x\mathcal{F}_x$$

This is an object distinct from the stalk: whereas the stalk $\mathcal{F}_x$ remembers all germs around $x$ as an $\mathcal{O}_{X,x}$-module, the fiber is a $\kappa(x)$-vector space obtained by reducing modulo the maximal ideal to retain only the value at that point. For instance, the stalk of $\mathcal{O}_X$ is the entire local ring $\mathcal{O}_{X,x}$, but its fiber is $\kappa(x)$; and if $\mathcal{E}$ is a locally free sheaf of rank $r$, then on a neighborhood trivializing it the stalk is $\mathcal{O}_{X,x}^{\oplus r}$ and the fiber is $\kappa(x)^{\oplus r}$, recovering the fiber of the corresponding vector bundle over $x$. Of course, for a general quasi-coherent sheaf, the dimension of the fibers may vary as one moves from point to point, and the fact that this dimension is upper semicontinuous for a finitely generated module over an affine is [§Flat Morphisms, ⁋Proposition 22](/en/math/scheme_theory/flat_morphisms#prop22){: data-relation="weak" }.

::: Proposition 13
For an invertible sheaf $\mathcal{L}$, $\mathcal{L}^\vee=\sHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X)$ is also an invertible sheaf, and $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$.
:::
::: Proof
Since the question is local, it suffices to check whenever $\mathcal{L}\vert_U\cong \mathcal{O}_U$ on an open set $U$. On this set, since

$$\mathcal{L}^\vee\vert_U=\sHom_{\mathcal{O}_U}(\mathcal{O}_U, \mathcal{O}_U)\cong \mathcal{O}_U$$

$\mathcal{L}^\vee$ is an invertible sheaf. Also, on $U$,

$$(\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee)\vert_U\cong \mathcal{O}_U\otimes_{\mathcal{O}_U}\mathcal{O}_U\cong \mathcal{O}_U$$

holds, and since these local isomorphisms come from the naturally defined evaluation morphism $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee \rightarrow \mathcal{O}_X$ ($s\otimes \phi\mapsto \phi(s)$), they glue together to give a global isomorphism $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}^\vee\cong \mathcal{O}_X$.
:::

Therefore, the invertible sheaves form a group with tensor product as the operation, where the identity element is $\mathcal{O}_X$ and the inverse of $\mathcal{L}$ is $\mathcal{L}^\vee$. This is the scheme version of the Picard group $\Pic(X)$ defined in [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 9](/en/math/algebraic_varieties/line_bundles#def9){: data-relation="weak" }.

One of the most important ways to obtain an invertible sheaf is to take the exterior power of a locally free sheaf. First, since the exterior power commutes with base change ([\[Multilinear Algebra\] §Tensor Algebra, ⁋Proposition 14](/en/math/multilinear_algebra/tensor_algebras#prop14){: data-relation="required" }), for an $A$-module $M$ and $g\in A$ we have $\bigl(\bigwedge^rM\bigr)_g\cong \bigwedge^r(M_g)$, and thus if on $U=\Spec A$ we have $\mathcal{F}\vert_U\cong \widetilde M$, the local models are compatible with restriction so that

$$\bigl(\bigwedge\nolimits^r\mathcal{F}\bigr)\big\vert_U\cong \widetilde{\bigwedge\nolimits^rM}$$

holds ([Proposition 5](#prop5){: data-relation="required" }). Therefore, the exterior power of a quasi-coherent sheaf is again a quasi-coherent sheaf.

In particular, if $\mathcal{E}$ is a locally free sheaf of rank $n$, then whenever $\mathcal{E}\vert_U\cong \mathcal{O}_U^{\oplus n}$ on an open set $U$, the sheaf $\bigwedge^r\mathcal{E}\vert_U$ has, from the basis $e_1,\ldots, e_n$, the elements $e_J$ ($\lvert J\rvert=r$) as a basis, and is thus a free sheaf of rank $\binom{n}{r}$ ([\[Multilinear Algebra\] §Tensor Algebra, ⁋Proposition 13](/en/math/multilinear_algebra/tensor_algebras#prop13){: data-relation="required" }). That is, $\bigwedge^r\mathcal{E}$ is again a locally free sheaf, and in the case $r=n$, it has rank $1$, that is, it is an invertible sheaf. We call this last case the *determinant* of $\mathcal{E}$ and write $\det\mathcal{E}=\bigwedge^n\mathcal{E}$. Therefore, a locally free sheaf of rank $n$ determines an element of $\Pic(X)$ via its determinant.

## Pullback and Pushforward

We now examine two operations that transport quasi-coherent sheaves along a scheme morphism. Given a morphism $\varphi:X \rightarrow Y$, we define the pullback, which pulls a sheaf on $Y$ back to $X$, and the pushforward, which pushes a sheaf on $X$ forward to $Y$.

::: Definition 14
Let a scheme morphism $\varphi:X \rightarrow Y$ be given.

1. On $X$, for an $\mathcal{O}_X$-module $\mathcal{F}$, the *pushforward* $\varphi_\ast \mathcal{F}$ is given on each open set by $V\mapsto \mathcal{F}(\varphi^{-1}(V))$, defining on $Y$ an $\mathcal{O}_Y$-module ([\[Topology\] §Presheaves, ⁋Example 8](/en/math/topology/presheaves#ex8){: data-relation="weak" }). Its module structure is given through the sheaf morphism $\varphi^\sharp:\mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ of the morphism.
2. On $Y$, for an $\mathcal{O}_Y$-module $\mathcal{G}$, the *pullback* $\varphi^\ast \mathcal{G}$ is given by the formula

    $$\varphi^\ast \mathcal{G}=\varphi^{-1}\mathcal{G}\otimes_{\varphi^{-1}\mathcal{O}_Y}\mathcal{O}_X$$

    defining on $X$ an $\mathcal{O}_X$-module. Here, $\varphi^{-1}$ is the inverse image sheaf from [\[Topology\] §Sheaves, ⁋Definition 10](/en/math/topology/sheaves#def10){: data-relation="required" }.
:::

Both operations reduce on affine schemes to familiar operations on modules. If $\varphi$ comes from a morphism $\Spec B \rightarrow \Spec A$ between affine schemes, that is, from a ring homomorphism $\phi:A \rightarrow B$, then the pullback of an $A$-module $M$ is the extension of scalars $\widetilde{M\otimes_A B}$, and the pushforward of a $B$-module $N$ is the restriction of scalars $\widetilde{\phi^\ast N}$ ([\[Algebraic Structures\] §Change of Scalars, ⁋Definition 1](/en/math/algebraic_structures/change_of_base_ring#def1){: data-relation="required" }, [Change of Scalars, ⁋Definition 3](/en/math/algebraic_structures/change_of_base_ring#def3){: data-relation="required" }). Then the adjunction $\phi_!\dashv \phi^\ast$ of [\[Algebraic Structures\] §Change of Scalars, ⁋Proposition 6](/en/math/algebraic_structures/change_of_base_ring#prop6){: data-relation="required" } directly translates into $\varphi^\ast\dashv \varphi_\ast$.

Now the natural question is whether these two operations preserve quasi-coherence, and the answer differs between the two operations. That is, it is always preserved for the pullback, whereas additional conditions are required for the pushforward. Intuitively, this is because on an affine chart, quasi-coherence appears as a presentation of free $\mathcal{O}_X$-modules of the form

$$\mathcal{O}^{(J)} \rightarrow \mathcal{O}^{(I)} \rightarrow \mathcal{F} \rightarrow 0$$

and since $\varphi^\ast$ is a left adjoint, it preserves direct sums and cokernels, thereby carrying such a presentation over directly, whereas the right adjoint $\varphi_\ast$ does not.

::: Proposition 15
For a morphism of schemes $\varphi:X \rightarrow Y$ and a quasi-coherent sheaf $\mathcal{G}$ on $Y$, the pullback $\varphi^\ast \mathcal{G}$ is a quasi-coherent sheaf on $X$.
:::
::: Proof
Since quasi-coherence is an affine-local property ([Theorem 10](#thm10){: data-relation="required" }), it suffices to show the case where $X=\Spec B$ and $Y=\Spec A$. In this case, $\varphi$ comes from a ring homomorphism $\phi:A \rightarrow B$ ([§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11){: data-relation="required" }), and there exists an $A$-module $M$ such that $\mathcal{G}=\widetilde M$ ([Theorem 9](#thm9){: data-relation="required" }).

We claim that $\varphi^\ast \widetilde M\cong \widetilde{M\otimes_A B}$. To show this, we compare stalks. For any $\mathfrak{q}\in \Spec B$ and $\mathfrak{p}=\phi^{-1}(\mathfrak{q})$, since the inverse image and the tensor product are compatible with stalks,

$$(\varphi^\ast \widetilde M)_\mathfrak{q}=(\varphi^{-1}\widetilde M)_\mathfrak{q}\otimes_{(\varphi^{-1}\mathcal{O}_{\Spec A})_\mathfrak{q}}\mathcal{O}_{\Spec B,\mathfrak{q}}\cong \widetilde M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

([Proposition 5](#prop5){: data-relation="required" }), while the stalk of the base change module is

$$(\widetilde{M\otimes_A B})_\mathfrak{q}=(M\otimes_A B)_\mathfrak{q}\cong M\otimes_A B_\mathfrak{q}\cong M_\mathfrak{p}\otimes_{A_\mathfrak{p}}B_\mathfrak{q}$$

Since these isomorphisms are natural, we obtain an isomorphism of sheaves $\varphi^\ast \widetilde M\cong \widetilde{M\otimes_A B}$, and therefore $\varphi^\ast \mathcal{G}$ is an associated sheaf and thus a quasi-coherent sheaf.
:::

For the pushforward to preserve quasi-coherence, the morphism must be quasi-compact and quasi-separated. This is because when computing $\varphi_\ast \mathcal{F}(V)=\mathcal{F}(\varphi^{-1}(V))$ over an affine, one must be able to cover $\varphi^{-1}(V)$ by finitely many affines and also control their intersections to obtain a module structure compatible with localization.

::: Theorem 16
For a quasi-compact and quasi-separated morphism of schemes $\varphi:X \rightarrow Y$ and a quasi-coherent sheaf $\mathcal{F}$ on $X$, the pushforward $\varphi_\ast \mathcal{F}$ is a quasi-coherent sheaf on $Y$.
:::
::: Proof
Since quasi-coherence is an affine-local property ([Theorem 10](#thm10){: data-relation="required" }), it suffices to show the case $Y=\Spec A$. In this case, since $\varphi$ is quasi-compact, $X$ is covered by finitely many affine open subsets $U_i=\Spec B_i$ ($i=1,\ldots, n$). Moreover, since $\varphi$ is quasi-separated, each $U_i\cap U_j$ is also covered by finitely many affine open sets $U_{ijk}=\Spec C_{ijk}$.

Now let $M=\Gamma(X, \mathcal{F})=\varphi_\ast \mathcal{F}(\Spec A)$ and let us show that $\varphi_\ast \mathcal{F}\cong \widetilde M$. To do so, it suffices to verify that $\varphi_\ast \mathcal{F}(D(g))\cong M_g$ for each $D(g)\subseteq \Spec A$. By definition, $\varphi_\ast \mathcal{F}(D(g))=\mathcal{F}(\varphi^{-1}(D(g)))$, and from the sheaf condition (the sheaf axiom for general sheaves after [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-relation="weak" }), we obtain the equalizer

$$\mathcal{F}(\varphi^{-1}(D(g)))=\ker\Bigl(\prod_i \mathcal{F}(U_i\cap \varphi^{-1}(D(g))) \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk}\cap \varphi^{-1}(D(g)))\Bigr)$$

Meanwhile, $U_i\cap \varphi^{-1}(D(g))=\Spec (B_i)_{g}$ is a principal open set, and since $\mathcal{F}\vert_{U_i}$ is a quasi-coherent sheaf, setting $\mathcal{F}(U_i)=N_i$ yields by [Proposition 5](#prop5){: data-relation="required" }

$$\mathcal{F}(U_i\cap \varphi^{-1}(D(g)))=(N_i)_g\cong \mathcal{F}(U_i)\otimes_A A_g$$

and the same identity holds for $U_{ijk}$. Since localization $(-)\otimes_A A_g$ is an exact functor ([\[Commutative Algebra\] §Properties of Localization, ⁋Proposition 2](/en/math/commutative_algebra/properties_of_localization#prop2){: data-relation="required" }), it commutes with the equalizer above, and since it is defined over finite products, we obtain

$$\mathcal{F}(\varphi^{-1}(D(g)))\cong \ker\Bigl(\prod_i N_i \rightrightarrows \prod_{i,j,k}\mathcal{F}(U_{ijk})\Bigr)\otimes_A A_g=M\otimes_A A_g=M_g$$

Here, finiteness is used essentially for products and localization to commute, which is the reason quasi-compactness and quasi-separatedness are required. Therefore, $\varphi_\ast \mathcal{F}(D(g))\cong M_g$ holds for all $g$, so $\varphi_\ast \mathcal{F}\cong \widetilde M$, which is a quasi-coherent sheaf.
:::

The quasi-compact and quasi-separated conditions in [Theorem 16](#thm16){: data-relation="required" } are essential. For instance, in a morphism where infinitely many affines must be glued together, infinite products appear when computing sections over $\varphi^{-1}(D(g))$, which may fail to commute with localization. However, morphisms between Noetherian schemes, and in particular morphisms between affine schemes, always satisfy these conditions, so pushforward preserves quasi-coherence in situations frequently encountered in practice.

Finally, we see how pushforward is compatible with the tensor product. In general, $\varphi_\ast$ does not preserve tensor products, but if one of the two factors is pulled back from a locally free sheaf on the base, that factor can be pulled out of $\varphi_\ast$.

::: Proposition 17 (Projection formula)
For a scheme morphism $\varphi:X \rightarrow Y$, with $X$ equipped with a quasi-coherent sheaf $\mathcal{F}$, and $Y$ equipped with a finite rank locally free sheaf $\mathcal{L}$ ([Definition 12](#def12){: data-relation="required" }), the isomorphism

$$\varphi_\ast(\mathcal{F}\otimes_{\mathcal{O}_X}\varphi^\ast \mathcal{L})\cong \varphi_\ast \mathcal{F}\otimes_{\mathcal{O}_Y}\mathcal{L}$$

holds.
:::
::: Proof
First, for an arbitrary $\mathcal{O}_Y$-module $\mathcal{L}$, we construct a natural morphism. Since the pullback in [Definition 14](#def14){: data-relation="required" } is the composition of $\varphi^{-1}$ and the base change to $\mathcal{O}_X$, it commutes with the tensor product; hence, using the counit of the adjunction $\varphi^\ast\dashv \varphi_\ast$, $\varepsilon:\varphi^\ast\varphi_\ast \mathcal{F} \rightarrow \mathcal{F}$, we obtain

$$\varphi^\ast(\varphi_\ast \mathcal{F}\otimes \mathcal{L})\cong \varphi^\ast\varphi_\ast \mathcal{F}\otimes \varphi^\ast \mathcal{L}\xrightarrow{\varepsilon\otimes\id}\mathcal{F}\otimes \varphi^\ast \mathcal{L}$$

The adjoint of this morphism is our desired $\theta:\varphi_\ast \mathcal{F}\otimes \mathcal{L} \rightarrow \varphi_\ast(\mathcal{F}\otimes \varphi^\ast \mathcal{L})$, which is natural with respect to the choice of $\mathcal{L}$.

Now we show that when $\mathcal{L}$ is finite rank locally free, $\theta$ is an isomorphism. Since the pushforward commutes with restriction to open subsets of the base (that is, $\varphi_\ast \mathcal{G}\vert_V$ is the pushforward with respect to $\varphi^{-1}(V) \rightarrow V$), it suffices to check whether it is an isomorphism on open subsets covering $Y$. By assumption, we have $\mathcal{L}\vert_V\cong \mathcal{O}_V^{\oplus r}$ on open subsets $V$ that cover $Y$, and on such $V$ we have $\varphi^\ast \mathcal{L}\cong \mathcal{O}^{\oplus r}$. Meanwhile, the tensor product commutes with finite direct sums, and $\varphi_\ast$, also being a right adjoint, commutes with finite products and hence commutes with finite direct sums. ([\[Category Theory\] §Adjoint Functors, ⁋Theorem 9](/en/math/category_theory/adjoints#thm9){: data-relation="required" }) Thus, on $V$, both sides are $(\varphi_\ast \mathcal{F}\vert_V)^{\oplus r}$, and by the naturality of $\theta$, under this identification $\theta$ is the direct sum of $r$ identity morphisms. Consequently, $\theta$ is an isomorphism on each $V$, and therefore is an isomorphism.
:::

What [Proposition 17](#prop17){: data-relation="weak" } states is that $\varphi_\ast$ does not merely operate at the level of abelian sheaves, but respects the $\mathcal{O}_Y$-module structure. This is the algebraic geometry version of the identity given by the Gysin homomorphism $\pi_!$ in [\[Algebraic Topology\] §Characteristic Classes of Vector Bundles](/en/math/algebraic_topology/characteristic_classes){: data-relation="weak" },

$$\pi_!(\pi^\ast\alpha\smile\beta)=\alpha\smile\pi_!\beta$$

and both arise from the common idea that what is pulled back from the base can be factored out of the pushforward.

## Ideal Sheaves and Closed Subschemes

The most important application of the fact that the pushforward preserves quasi-coherence is the ideal sheaf determined by a closed subscheme. For an affine scheme $\Spec A$, an ideal $\mathfrak{a}\subseteq A$ is itself an $A$-module, and thus defines an associated sheaf $\widetilde{\mathfrak{a}}$, which is a subsheaf of $\mathcal{O}_{\Spec A}=\widetilde A$. For a general scheme $X$, a closed embedding $\iota:Z \rightarrow X$ defines an ideal sheaf $\mathcal{I}_{Z/X}=\ker\iota^\sharp$, which also gives an ideal on each affine open subset ([§Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5){: data-relation="weak" }), but whether these ideals are compatible with localization and glue into a single associated sheaf is a separate question. Since the localization condition required for gluing in [§Closed Subschemes, ⁋Proposition 6](/en/math/scheme_theory/closed_subschemes#prop6){: data-relation="required" } is precisely quasi-coherence, what needs to be checked is that $\mathcal{I}_{Z/X}$ is a quasi-coherent sheaf. This is obtained as an application of [Theorem 16](#thm16){: data-relation="required" }.

::: Proposition 18
For a closed embedding $\iota:Z \rightarrow X$ ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2){: data-relation="required" }), both $\iota_\ast \mathcal{O}_Z$ and the ideal sheaf $\mathcal{I}_{Z/X}$ are quasi-coherent sheaves on $X$.
:::
::: Proof
Among the three hypotheses of [Theorem 16](#thm16){: data-relation="required" }, the condition that $\mathcal{O}_Z$ is a quasi-coherent sheaf on $Z$ follows immediately from the fact that on each affine open subset $\Spec B\subseteq Z$, we have $\mathcal{O}_Z\vert_{\Spec B}=\widetilde B$. Therefore, it suffices to verify that $\iota$ is quasi-compact and quasi-separated. On $X$, fix an affine open subset $U\cong \Spec A$ and let $W=\iota^{-1}(U)$. Since $\iota$ is a homeomorphism between $Z$ and a closed subset of $X$ as a continuous map, $W$ is homeomorphic to a closed subset of $U$, namely $C=\iota(Z)\cap U$. However, affine schemes are quasi-compact ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-relation="required" }) and any closed subset of a quasi-compact space is quasi-compact, so $W$ is also quasi-compact. That is, $\iota$ is a quasi-compact morphism. ([§Properties of Scheme Morphisms, ⁋Definition 2](/en/math/scheme_theory/properties_of_scheme_morphisms#def2){: data-relation="required" })

Quasi-separatedness can also be verified solely from the topology of $C$. Since $\{D(f)\}_{f\in A}$ is a base for $U$, any open subset of $C$ is a union of sets of the form $C\cap D(f)$, and each $C\cap D(f)$ is quasi-compact because it is a closed subset of the quasi-compact space $D(f)\cong \Spec A_f$. Therefore, any quasi-compact open subset of $C$ can be written as a finite union of sets of the form $C\cap D(f)$, and the intersection of two such sets is a finite union of sets of the form $C\cap D(f)\cap D(g)=C\cap D(fg)$, which is again quasi-compact. That is, $W$ is a quasi-separated scheme, and since $U$ was an arbitrary affine open subset, $\iota$ is a quasi-separated morphism. ([§Properties of Scheme Morphisms, ⁋Definition 5](/en/math/scheme_theory/properties_of_scheme_morphisms#def5){: data-relation="required" }) Now by [Theorem 16](#thm16){: data-relation="required" }, $\iota_\ast \mathcal{O}_Z$ is a quasi-coherent sheaf on $X$.

It remains to consider $\mathcal{I}_{Z/X}=\ker\iota^\sharp$. Since quasi-coherence is affine-local ([Theorem 10](#thm10){: data-relation="required" }), it suffices to show this on $U=\Spec A$ fixed above. Setting $N=(\iota_\ast \mathcal{O}_Z)(U)$, [Theorem 10](#thm10){: data-relation="required" } yields $(\iota_\ast \mathcal{O}_Z)\vert_U\cong \widetilde N$, and therefore the restriction of $\iota^\sharp$ to $U$ is a morphism of the form $\widetilde A \rightarrow \widetilde N$, which by [Theorem 7](#thm7){: data-relation="required" } is induced by an $A$-module homomorphism $\phi:A \rightarrow N$ as the associated sheaf $\widetilde\phi$. Then, for the two short exact sequences

$$0 \rightarrow \ker\phi \rightarrow A \rightarrow \im\phi \rightarrow 0,\qquad 0 \rightarrow \im\phi \rightarrow N \rightarrow N/\im\phi \rightarrow 0$$

applying [Proposition 6](#prop6){: data-relation="required" } shows that $\widetilde{\im\phi} \rightarrow \widetilde N$ is injective and $\widetilde{\ker\phi}=\ker(\widetilde A \rightarrow \widetilde{\im\phi})$, so we ultimately obtain $\ker\widetilde\phi=\widetilde{\ker\phi}$. That is, $\mathcal{I}_{Z/X}\vert_U\cong \widetilde{\ker\phi}$ is an associated sheaf, from which it follows that $\mathcal{I}_{Z/X}$ is a quasi-coherent sheaf.
:::

Thus, the closed subschemes of $X$ correspond precisely to the quasi-coherent ideal sheaves of $\mathcal{O}_X$, that is, subsheaves of $\mathcal{O}_X$ that are quasi-coherent $\mathcal{O}_X$-modules. One direction is given by [Proposition 18](#prop18){: data-relation="weak" }. Conversely, given such an $\mathcal{I}$, for each affine open subset $\Spec A$, $\mathcal{I}(\Spec A)$ is an ideal of $A$, and since $\mathcal{I}(D(f))\cong \mathcal{I}(\Spec A)_f$ holds by [Theorem 10](#thm10){: data-relation="required" } and [Lemma 3](#lem3){: data-relation="required" }, $\mathcal{I}$ induces a unique closed subscheme of $X$ by [§Closed Subschemes, ⁋Proposition 6](/en/math/scheme_theory/closed_subschemes#prop6){: data-relation="required" }. This correspondence is nothing other than the correspondence between an ideal $\mathfrak{a}\subseteq A$ and the quotient $A/\mathfrak{a}$ in the affine setting. Moreover, [Proposition 18](#prop18){: data-relation="weak" } is also the fact used without proof in the proof of [§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-relation="forward" }.

## Affine Morphisms and the Relative Spectrum

A closed embedding could be completely described via a specific sheaf, namely the ideal sheaf of $\mathcal{O}_X$, and we saw above that this ideal sheaf is a quasi-coherent sheaf. Closed embeddings are not the only morphisms completely determined by a sheaf in this way, and we will see that affine morphisms also admit such a description. ([§Properties of Scheme Morphisms, ⁋Definition 8](/en/math/scheme_theory/properties_of_scheme_morphisms#def8){: data-relation="required" }) The crucial fact is that to define an affine morphism $X\rightarrow S$, it suffices to glue together affine open subschemes of $X$ (and maps from them to $S$). However, since affine subschemes are completely determined precisely by their coordinate rings, we can instead solve the problem of gluing these rings. In this setting, for an affine morphism $\varphi: X \rightarrow S$, each ring $\mathcal{O}_X(\varphi^{-1}(V))$ is equipped with a ring homomorphism from $\mathcal{O}_S(V)$ given by the structure morphism and is thus an $\mathcal{O}_S(V)$-algebra; hence all of this data is packaged into a single sheaf on $S$, namely $\varphi_\ast\mathcal{O}_X$, together with its algebra structure.

::: Definition 19
On a scheme $S$, an $\mathcal{O}_S$-module $\mathcal{A}$ is a *quasi-coherent $\mathcal{O}_S$-algebra* if $\mathcal{A}$ is a quasi-coherent sheaf ([Definition 8](#def8){: data-relation="required" }), and for each open set $V$, $\mathcal{A}(V)$ has the structure of a commutative $\mathcal{O}_S(V)$-algebra such that the restriction maps are algebra homomorphisms.
:::

As described above, given an affine morphism, we can always define a quasi-coherent $\mathcal{O}_S$-algebra in this way. Our claim is stronger than this: any quasi-coherent $\mathcal{O}_S$-algebra is always obtained in this manner.

::: Theorem 20
The following holds.

1. For an affine morphism $\varphi: X \rightarrow S$, $\varphi_\ast \mathcal{O}_X$ is a quasi-coherent $\mathcal{O}_S$-algebra, and on $S$, for any affine open subset $V$, we have $\varphi^{-1}(V)\cong \Spec (\varphi_\ast \mathcal{O}_X)(V)$.
2. For any quasi-coherent $\mathcal{O}_S$-algebra $\mathcal{A}$, there exist an affine morphism $\varphi: X \rightarrow S$ and an $\mathcal{O}_S$-algebra isomorphism $\alpha:\mathcal{A}\xrightarrow{\sim} \varphi_\ast \mathcal{O}_X$. Such a triple $(X, \varphi, \alpha)$ is unique up to unique isomorphism compatible with $\alpha$.
3. For two affine morphisms $\varphi: X \rightarrow S$ and $\varphi': Z \rightarrow S$, giving, over $S$, a morphism $X \rightarrow Z$ is equivalent to giving an $\mathcal{O}_S$-algebra morphism $(\varphi')_\ast \mathcal{O}_Z \rightarrow \varphi_\ast \mathcal{O}_X$.
:::
::: Proof
We first show the first claim. To show quasi-coherence, we use [Theorem 16](#thm16){: data-relation="required" } as before. First, on $S$, for an affine open subset $V$, $\varphi^{-1}(V)\cong \Spec A$ is an affine scheme and hence quasi-compact ([§The Spectrum, ⁋Lemma 12](/en/math/scheme_theory/spectrums#lem12){: data-relation="required" }). Also, since $\{D(f)\}$ is a base for $\Spec A$, any quasi-compact open set is always a union of finitely many $D(f)$, and since $D(f)\cap D(g)=D(fg)$, the intersection of two such open sets is again a union of finitely many sets of the form $D(fg)$, so they are quasi-separated. That is, $\varphi$ is a quasi-compact, quasi-separated morphism, so we can apply [Theorem 16](#thm16){: data-relation="required" }, and therefore $\varphi_\ast \mathcal{O}_X$ is a quasi-coherent sheaf on $S$. The algebra structure on this is given by the morphism $\varphi^\sharp:\mathcal{O}_S \rightarrow \varphi_\ast\mathcal{O}_X$ of structure sheaves. Finally, if $V$ is an affine open subset, then $\varphi^{-1}(V)$ itself is an affine scheme, so by [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-relation="required" }, we obtain $\varphi^{-1}(V)\cong \Spec \mathcal{O}_X(\varphi^{-1}(V))=\Spec (\varphi_\ast \mathcal{O}_X)(V)$.

The core is again the second claim. First, to show existence, choose an affine open covering of $S$, $\{V_i=\Spec B_i\}$. Now, setting $A_i=\mathcal{A}(V_i)$, since $\mathcal{A}$ is quasi-coherent, we have $\mathcal{A}\vert_{V_i}\cong \widetilde{A_i}$ by [Theorem 10](#thm10){: data-relation="required" }. Now, for $\mathcal{A}$, letting the ring homomorphism given by the $\mathcal{O}_S$-algebra structure be $\phi_i:B_i \rightarrow A_i$, we can set $X_i=\Spec A_i$ and, via $\phi_i$, define the morphism of schemes $\varphi_i:X_i \rightarrow V_i$. The claim is that we can glue the $X_{ij}=\varphi_i^{-1}(V_i\cap V_j)$. To verify this, for any $x\in V_i\cap V_j$, choose in both $V_i$ and $V_j$ a principal open subset $x\in W\subseteq V_i\cap V_j$ ([§The Topology of Schemes, ⁋Lemma 11](/en/math/scheme_theory/topology_of_schemes#lem11){: data-relation="required" }). If $W$ is written in $V_i$ of the form $D(f)$, then from $\mathcal{A}\vert_{V_i}\cong \widetilde{A_i}$ we have $\mathcal{A}(W)\cong (A_i)_{\phi_i(f)}$, and by definition of $W$, since $\varphi_i^{-1}(W)=D(\phi_i(f))$, we have

$$\varphi_i^{-1}(W)\cong \Spec (A_i)_{\phi_i(f)}\cong \Spec \mathcal{A}(W)\tag{$\ast$}$$

holds. The same calculation holds on the side of $V_j$ as well, so we obtain a canonical isomorphism $\varphi_i^{-1}(W)\cong \varphi_j^{-1}(W)$. Since this isomorphism is determined solely by $\mathcal{A}(W)$, these naturally glue over the overlaps and satisfy the cocycle condition. That is, they glue to a single scheme $X$ and a morphism $\varphi: X\rightarrow S$ on it. Here, since each $\varphi^{-1}(V_i)=X_i$ is affine, by [§Properties of Scheme Morphisms, ⁋Proposition 9](/en/math/scheme_theory/properties_of_scheme_morphisms#prop9){: data-relation="required" } $\varphi$ is an affine morphism, and since the identification $(\varphi_\ast\mathcal{O}_X)(V_i)=\Gamma(X_i,\mathcal{O}_{X_i})=A_i=\mathcal{A}(V_i)$ is compatible with restriction maps, they yield an $\mathcal{O}_S$-algebra isomorphism $\alpha:\mathcal{A}\xrightarrow{\sim}\varphi_\ast\mathcal{O}_X$. Uniqueness also essentially follows from $(\ast)$: if two triples $(X,\varphi,\alpha)$ and $(X',\varphi',\alpha')$ satisfy the conditions, then by this computation, on $S$, for any affine open subset $V$, we must have

$$\varphi^{-1}(V)\cong \Spec \mathcal{A}(V)\cong (\varphi')^{-1}(V)$$

which yields uniqueness.

As for the last claim, given on $S$ a morphism $\vartheta:X\rightarrow Z$, then on $S$, for each affine open subset $V$, $\vartheta$ induces a morphism $\varphi^{-1}(V)\rightarrow (\varphi')^{-1}(V)$, and since both are affine schemes by the first claim, this corresponds to an $\mathcal{O}_S(V)$-algebra homomorphism $((\varphi')_\ast\mathcal{O}_Z)(V)\rightarrow (\varphi_\ast\mathcal{O}_X)(V)$. Since these are compatible with restriction maps, we obtain an $\mathcal{O}_S$-algebra morphism $(\varphi')_\ast\mathcal{O}_Z\rightarrow \varphi_\ast\mathcal{O}_X$. Conversely, given such a morphism, the same correspondence gives $\varphi^{-1}(V)\rightarrow (\varphi')^{-1}(V)$ on each affine open subset, and since these agree on overlaps, by [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1){: data-relation="required" } they glue over $S$ to a morphism $X\rightarrow Z$; that these two constructions are inverses of each other can be checked on affines.
:::

That is, an affine morphism is precisely the same data as a quasi-coherent algebra on $S$, and the third claim of [Theorem 20](#thm20){: data-relation="required" } shows that this correspondence preserves morphisms as well. That is, between the category of affine schemes over $S$, $\AffSch_{/S}$, and the category of quasi-coherent $\mathcal{O}_S$-algebras, there exists a contravariant equivalence. We now give a name to one direction of this correspondence.

::: Definition 21
For a quasi-coherent $\mathcal{O}_S$-algebra $\mathcal{A}$, taking the affine morphism $\varphi:X\rightarrow S$ given by the second claim of [Theorem 20](#thm20){: data-relation="required" }, its domain $X$ is called the *relative spectrum* of $\mathcal{A}$ and denoted by $\rSpec_S(\mathcal{A})$.
:::

Intuitively, this is a relative version of $\Spec$ over a base; in particular, since a closed embedding $\iota:Z\rightarrow S$ is an affine morphism ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-relation="required" }), we can repeat the same construction. Naturally, the algebra obtained in this way is $\mathcal{O}_S/\mathcal{I}_{Z/S}$, meaning that the correspondence of ideal sheaves examined above is the application of the relative spectrum to this special case.

Furthermore, the relative spectrum behaves well under base change.

::: Proposition 22
For a scheme morphism $\varphi:S'\rightarrow S$ and a quasi-coherent $\mathcal{O}_S$-algebra $\mathcal{A}$, the pullback $\varphi^\ast\mathcal{A}$ is a quasi-coherent $\mathcal{O}_{S'}$-algebra, and

$$\rSpec_{S'}(\varphi^\ast\mathcal{A})\cong \rSpec_S(\mathcal{A})\times_SS'$$

holds.
:::
::: Proof
That $\varphi^\ast\mathcal{A}$ is a quasi-coherent sheaf is [Proposition 15](#prop15){: data-relation="required" }, and since the pullback is compatible with the tensor product, we can pull back the multiplication and identity of $\mathcal{A}$ to give it an $\mathcal{O}_{S'}$-algebra structure.

Now let $X=\rSpec_S(\mathcal{A})$ and consider the projection $p:X\times_SS'\rightarrow S'$. Pairs of affine open subsets satisfying $\varphi(V')\subseteq V$, with $V'=\Spec B'\subseteq S'$ and $V=\Spec B\subseteq S$, cover $S'$, and let the ring homomorphism corresponding to $\varphi\vert_{V'}:V'\rightarrow V$ be $\phi:B\rightarrow B'$. For such $V'$, from [§Fiber Products, ⁋Lemma 3](/en/math/scheme_theory/fiber_products#lem3){: data-relation="required" } and the associativity of fiber products, we have

$$p^{-1}(V')\cong X\times_SV'\cong (X\times_SV)\times_VV'$$

and by [§Fiber Products, ⁋Lemma 3](/en/math/scheme_theory/fiber_products#lem3){: data-relation="required" }, $X\times_SV$ is the preimage of $V$, which by the first assertion of [Theorem 20](#thm20){: data-relation="required" } is $\Spec \mathcal{A}(V)$. Therefore, by [§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2){: data-relation="required" }, we obtain

$$p^{-1}(V')\cong \Spec \mathcal{A}(V)\times_{\Spec B}\Spec B'\cong \Spec (\mathcal{A}(V)\otimes_BB')$$

On the other hand, by the proof of [Proposition 15](#prop15){: data-relation="required" }, we have $(\varphi^\ast\mathcal{A})\vert_{V'}\cong \widetilde{\mathcal{A}(V)\otimes_BB'}$, so by the first assertion of [Theorem 20](#thm20){: data-relation="required" }, $\rSpec_{S'}(\varphi^\ast\mathcal{A})$ over $V'$ is also $\Spec (\mathcal{A}(V)\otimes_BB')$. Since all these isomorphisms are canonically determined by $\phi:B\rightarrow B'$ and the structure of $\mathcal{A}(V)$ as a $B$-algebra, they agree on overlaps and glue to an isomorphism over $S'$.
:::

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate Texts in Mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
