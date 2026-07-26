---
title: "Valuation Rings"
description: "We define separated and proper morphisms, and examine how they generalize the topological notions of Hausdorff and compactness into algebraic geometry. The structure of discrete valuation rings is also discussed."
excerpt: "Valuative criteria for separated and proper morphisms"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-en"

date: 2024-05-24
weight: 15
translated_at: 2026-07-26T20:45:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-26T20:45:03+00:00
---
In this post we define separated morphisms and proper morphisms. It is helpful to think of them as the algebraic-geometry translations of the Hausdorff and compactness conditions in topology.

In previous posts we defined open subschemes ([§Schemes, ⁋Definition 4](/en/math/scheme_theory/schemes#def4)), examined closed embeddings and the resulting closed subschemes, and looked at ideal sheaves ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2), [⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5)). We now add the following notions.

::: Definition 1
Let a scheme morphism $f: X \rightarrow Y$ be given.

1. If $f$ induces an isomorphism between open subschemes of $X$ and $Y$, we call $f$ an *open immersion*.
2. We say $f$ is *projective* if for some suitable $n$, $f$ can be factored as a composition of a closed embedding and a projection, of the form $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$. ([§Projective Schemes](/en/math/scheme_theory/projective_schemes))
3. We say $f$ is *quasi-projective* if it can be factored as a composition of a suitable open immersion $X \rightarrow X'$ and a projective morphism $X' \rightarrow Y$.
:::

The first definition is obvious, and the second and third are also the relative versions—i.e., treated in $\Sch_{/Y}$—of [\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3) and [\[Algebraic Varieties\] §Quasi-Projective Varieties, ⁋Definition 1](/en/math/algebraic_varieties/quasi_projective_varieties#def1).

Before diving into the main story, it is good to look at the following example.

::: Example 2
Let $A$ be a discrete valuation ring that is a subring of a field $K$. That is, for any $x\in K^\times$, either $x\in A$ or $x^{-1}\in A$; $A$ is Noetherian, and its maximal ideal $\mathfrak{m}$ is principal. ([\[Commutative Algebra\] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5)) Since any $x\in K^\times$ can be expressed as a ratio of elements of $A$ via $x$ or $x^{-1}$, we have $K=\Frac(A)$. Also, $A$ is a local ring with $\mathfrak{m}$ as its unique maximal ideal ([\[Commutative Algebra\] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6)), and choosing a uniformizer $\pi$, any $f\in K^\times$ is uniquely expressed as $f=\pi^nu$ for some integer $n$ and unit $u$ ([\[Commutative Algebra\] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8)); hence every nonzero ideal of $A$ is of the form $(\pi^n)$. In particular, $A$ is a principal ideal domain, and its only prime ideals are $(0)$ and $\mathfrak{m}=(\pi)$.

Hence $\Spec A$ consists of the two points $(0)$ and $\mathfrak{m}$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $\Spec A$ is

$$D(\pi)=\Spec A\setminus Z(\mathfrak{m})=\{(0)\}.$$

Then by [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6),

$$\mathcal{O}(D(\pi))\cong A_\pi\cong K.$$

Of course $\mathcal{O}(\Spec A)\cong A$.

On the other hand, the two points of $\Spec A$ can be understood geometrically through their residue fields. Using [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8),

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong K,\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

we obtain

$$\kappa((0))=K, \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong A/\mathfrak{m}.$$

:::

Let us examine the example a bit more geometrically. Since $Z((0))=\Spec A$, the closure of $(0)$ is the whole of $\Spec A$, so $(0)$ is the generic point of this space. Such a situation is seen especially intuitively when, for a curve $C$ and a point $p$ on it, $\mathcal{O}_{C,p}$ is a discrete valuation ring. Specifically, the stalk

$$\mathcal{O}_{C,p}=\varinjlim_{U\supset p} \mathcal{O}(U)$$

can be viewed as the germ at the point $p$, and the generic point $(0)$ of $\Spec \mathcal{O}_{C,p}$ is exactly what contains this data. Then the remaining (unique) point $\mathfrak{m}$ corresponds precisely to the point $p$, and the fact that this is a specialization of $(0)$ reflects exactly that in defining the germ we look at neighborhoods arbitrarily close to $p$.

In this picture, the role of $\Spec K$ is revealed when we look at the function side. The functions on $\Spec A$ are $A$ itself—that is, germs regular at $p$—and the elements of $K\cong A_\pi$, which are the functions on the unique nontrivial open set $D(\pi)=\{(0)\}$, are those allowing negative order $n$ in the expression $f=\pi^nu$. (Item 2 of [\[Commutative Algebra\] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8)) That is, these are functions having a pole at $p$ but of finite order—meaning functions regular on the whole neighborhood except at $p$—and thus $\Spec K$ is the space that extracts the center $p$ from this germ, losing the information of $p$ while retaining only the information about a neighborhood of $p$. The canonical morphism $\Spec K \rightarrow \Spec A$ is exactly the inclusion map defined by this picture.

Then a morphism $\Spec K \rightarrow X$ is a punctured curve germ mapping into $X$, and extending this to $\Spec A \rightarrow X$ is recovering the missing point inside $X$ and gluing the curve back together—that is, finding the limit of the curve. That this extension exists in at most one way is separatedness, and that it exists in exactly one way is properness; this is the content of the two criteria we will see next. Topologically, this corresponds exactly to the fact that limits are unique in a Hausdorff space ([\[Topology\] §Hausdorff Spaces, ⁋Proposition 4](/en/math/topology/Hausdorff_spaces#prop4)) and that limits always exist in a compact space ([\[Topology\] §Compactness and Paracompactness, ⁋Lemma 1](/en/math/topology/compactness#lem1)).

## Separated Morphism

As seen above, the idea of a separated morphism is that, given a germ of a curve, there is at most one way to fill in its center point $p$. To describe this, the following definition is needed.

::: Definition 3
For a scheme morphism $f:X \rightarrow Y$, the unique morphism induced by two copies of $\id_X$ via the universal property of the fiber product, i.e., the dashed arrow $\Delta: X \rightarrow X \times_Y X$ in the following diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-1.svg width="13.51em" alt="diagonal_morphism" %}

is called the *diagonal morphism* of $f$. ([§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1)) If $\Delta$ is a closed embedding, we call $f$ *separated*, and say $X$ is *separated* over $Y$. If $X$ is separated over $\Spec \mathbb{Z}$, we simply call $X$ a *separated* scheme.
:::

When we need to specify which morphism's diagonal we mean, we write $\Delta_{X/Y}$ instead of $\Delta$. By definition, it is obvious that for the two projections $p_1,p_2: X\times_YX \rightarrow X$, we have $p_1\circ\Delta=p_2\circ\Delta=\id_X$. Moreover, since $\Delta$ is injective and the restriction of $p_1$ to $\Delta(X)$ gives a continuous inverse of $\Delta$, the morphism $\Delta$ is always a homeomorphism onto $\Delta(X)$. Therefore, asking whether $\Delta$ is a closed embedding amounts to asking whether $\Delta(X)$ is closed and whether all functions on $X$ are obtained by restricting functions on $X\times_YX$. ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2))

In algebraic geometry, separatedness is regarded as the property that replaces Hausdorff. Recalling that a topological space $T$ is Hausdorff if and only if the diagonal is closed in $T\times T$ ([\[Topology\] §Hausdorff Spaces, ⁋Lemma 5](/en/math/topology/Hausdorff_spaces#lem5)), the following proposition is natural to expect.

::: Proposition 4
$f:X \rightarrow Y$ being separated is equivalent to the image of $X$ under the diagonal morphism $\Delta: X \rightarrow X\times_YX$ being a closed set.
:::
::: Proof
By definition, if $f$ is separated then $\Delta(X)$ is closed, which is trivial. So we assume $\Delta(X)$ is closed and show that $\Delta$ is a closed embedding. As we saw earlier, $\Delta$ is always a homeomorphism onto $\Delta(X)$, so the topological conditions are already satisfied by our assumption, and we only need to show that $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$ is surjective. We can check this on stalks.

First, there is nothing to see at a point $q\notin \Delta(X)$. By the assumption that $\Delta(X)$ is closed, there exists an open neighborhood $W$ of $q$ such that $W\cap\Delta(X)=\emptyset$, and then $\Delta^{-1}(W)=\emptyset$, so

$$(\Delta_\ast\mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$$

and hence $(\Delta_\ast\mathcal{O}_X)_q=0$. The open neighborhoods we will choose below cannot cover points outside $\Delta(X)$, so this is precisely where the assumption is actually used.

Now consider a point of the form $\Delta(p)$. For any $p\in X$ we can choose an open affine subset $U$ containing $p$, and if necessary restrict $U$ so that $f(U)$ lies in some open affine subset $V$ of $Y$. Then $U\times_VU$ is an open subset of $X\times_YX$ and an open neighborhood of $\Delta(p)$, and since $p_1\circ\Delta=p_2\circ\Delta=\id_X$, we have $\Delta^{-1}(U\times_VU)=U$. On this, $\Delta: U \rightarrow U\times_VU$ is a closed embedding by [Lemma 5](#lem5) below, so $\mathcal{O}_{U\times_VU} \rightarrow \Delta_\ast\mathcal{O}_U$ is surjective, and in particular the morphism between stalks at $\Delta(p)$ is surjective.
:::

::: Lemma 5
Any morphism $f:X \rightarrow Y$ between affine schemes is always separated.
:::
::: Proof
If $X=\Spec A$, $Y=\Spec B$, then $X\times_YX=\Spec(A\otimes_BA)$ ([§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2)), and $\Delta$ is induced from the ring homomorphism

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'.$$

This ring homomorphism sends $a\otimes 1$ to $a$, so it is surjective, and hence $\Delta$ is a closed embedding. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))
:::

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10). For convenience, let us denote this scheme by $X$. Since this is a scheme over $\mathbb{K}$, what we will look at is $X\times_\mathbb{K}X$. As $X$ is obtained by gluing two copies of $\mathbb{A}^1_\mathbb{K}$ away from the origin, $X\times_\mathbb{K}X$ is obtained by gluing four copies of $\mathbb{A}^2_\mathbb{K}$; thus a point where neither coordinate is zero appears once, a point where exactly one coordinate is zero appears twice, and the origin where both coordinates are zero appears four times. Now the image of $\Delta$ is the usual diagonal away from the origin, and the two origins $0_1,0_2$ of $X$ map to $(0_1,0_1)$ and $(0_2,0_2)$ among the four origins. Hence the remaining two origins $(0_1,0_2)$, $(0_2,0_1)$ do not belong to $\Delta(X)$. However, in the chart $\mathbb{A}^2_\mathbb{K}$ containing them, $\Delta(X)$ is the diagonal minus the origin and its closure is the whole diagonal, so these two points belong to the closure of $\Delta(X)$. Therefore $\Delta(X)$ is not closed, and by [Proposition 4](#prop4), $X$ is not separated. Again, in topology this space was an example of a non-Hausdorff space.

Now let us see a criterion for separatedness. Unlike in [Example 2](#ex2), the criterion is required for all valuation rings, not necessarily discrete ones; that is, for every subring $A$ of a field $K$ satisfying the condition that for any $x\in K^\times$, either $x\in A$ or $x^{-1}\in A$. ([\[Commutative Algebra\] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5)) Also, below, $j:\Spec K \rightarrow \Spec A$ always denotes the morphism induced by the inclusion $A\hookrightarrow K$.

::: Theorem 6
For a Noetherian scheme $X$ and a scheme morphism $f:X \rightarrow Y$, the condition that $f$ is separated is equivalent to the following: for any valuation ring $A$ with its quotient field $K=\Frac(A)$, and for any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ such that the outer square of the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.27em" alt="valuative_criterion" %}

is given, there is at most one morphism $\Spec A \rightarrow X$ making the entire diagram commute.
:::
::: Proof
The outer square being given means that morphisms $u:\Spec K \rightarrow X$ and $v: \Spec A \rightarrow Y$ are given satisfying $f\circ u=v\circ j$, and a lifting of this square means a morphism $g:\Spec A \rightarrow X$ satisfying $g\circ j=u$ and $f\circ g=v$.

Throughout the proof we use two standard facts. The first is the existence theorem for valuation rings: given a field $K$ and a local subring $\mathcal{O}$ inside it, there exists a valuation ring $A$ with $\Frac(A)=K$, $\mathcal{O}\subseteq A$, and $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$. In this case we say that $A$ *dominates* $\mathcal{O}$, and the existence of such $A$ is obtained by applying Zorn's lemma to the collection of local subrings of $K$ dominating $\mathcal{O}$. The second is that for a field $K$, a morphism $\Spec K \rightarrow X$ corresponds bijectively to a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. This follows from the fact that when $X=\Spec B$, a ring homomorphism $B \rightarrow K$ gives a pair of its kernel, a prime ideal $\mathfrak{p}$, and $\kappa(\mathfrak{p}) \rightarrow K$; the general case is handled by choosing an affine open neighborhood of $x$.

First assume $f$ is separated, and suppose two liftings $g_1, g_2$ of the above square are given. Since $f\circ g_1=f\circ g_2=v$, the universal property of the fiber product yields a unique $h:\Spec A \rightarrow X\times_YX$ such that $p_1\circ h=g_1$ and $p_2\circ h=g_2$. Here $p_1,p_2$ are the two projections. Now since $\Delta$ is a closed embedding, the base change

$$Z=\Spec A\times_{X\times_YX}X \longrightarrow \Spec A$$

is also a closed embedding. That closed embeddings are stable under base change follows from the affine-local fact that the base change of $B \rightarrow B/\mathfrak{b}$ is $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$, which remains surjective. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))

On the other hand $p_1\circ h\circ j=g_1\circ j=u$ and $p_2\circ h\circ j=g_2\circ j=u$, and $p_1\circ \Delta\circ u=u$ and $p_2\circ\Delta\circ u=u$, so by the uniqueness in the universal property we have $h\circ j=\Delta\circ u$. Therefore $j$ factors through the pullback $Z$, and in particular the image of $Z \rightarrow \Spec A$ contains the image of $j$, namely the zero ideal $(0)$ of $A$. Since $A$ is a domain, $(0)$ is the generic point of $\Spec A$ ([§Topology of Schemes, ⁋Example 5](/en/math/scheme_theory/topology_of_schemes#ex5)), and thus the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself. Then $Z$ is a closed subscheme of $\Spec A$ of the form $\Spec(A/\mathfrak{a})$ for some ideal $\mathfrak{a}\subseteq A$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and the fact that its image is all of $\Spec A$ means that $\mathfrak{a}$ is contained in every prime ideal of $A$, i.e.

$$\mathfrak{a}\subseteq \mathfrak{N}(A)=(0).$$

The last equality comes from $A$ being a domain. Therefore $Z \rightarrow \Spec A$ is an isomorphism, which means that $h$ factors through $\Delta$, i.e. $h=\Delta\circ g$ for some $g:\Spec A \rightarrow X$. Then

$$g_1=p_1\circ h=p_1\circ \Delta\circ g=g,\qquad g_2=p_2\circ h=p_2\circ\Delta\circ g=g$$

so $g_1=g_2$. In this direction the assumption that $X$ is Noetherian is not used.

Conversely, assume that for any square there is at most one lifting. By [Proposition 4](#prop4) it suffices to show that $\Delta(X)$ is a closed subset of $X\times_YX$.

First we observe that every point of $\cl(\Delta(X))$ is a specialization of some point of $\Delta(X)$. Since $X$ is a Noetherian scheme, it is also Noetherian as a topological space ([§Topology of Schemes, ⁋Definition 14](/en/math/scheme_theory/topology_of_schemes#def14)), and hence has finitely many irreducible components $X_1,\ldots, X_r$. ([\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13)) Each $X_i$ is an irreducible closed subset, so it has a generic point $\eta_i$ ([§Spectrums, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)), and $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$. Now since $\Delta$ is continuous, $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$ and the right-hand side is a finite union hence closed; conversely each $\Delta(\eta_i)$ lies in $\Delta(X)$, so we obtain

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\}).$$

That is, any point of $\cl(\Delta(X))$ is a specialization of some $\Delta(\eta_i)\in \Delta(X)$. ([§Topology of Schemes, ⁋Definition 2](/en/math/scheme_theory/topology_of_schemes#def2)) Therefore, if we show that $\Delta(X)$ is closed under specialization, then $\Delta(X)=\cl(\Delta(X))$ and the proof is complete.

Let $\xi=\Delta(x)\in \Delta(X)$ and $\eta\in\cl(\{\xi\})$. Giving the closed subset $T=\cl(\{\xi\})$ its reduced scheme structure ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)), $T$ is an integral scheme with generic point $\xi$. Choose an affine open subset $\Spec B\subseteq T$ containing $\eta$. Since a generic point belongs to every non-empty open set, $\Spec B$ also contains $\xi$, and $B$ is a domain with $\xi$ corresponding to the zero ideal of $B$, so

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

where $\mathfrak{q}$ is the prime ideal corresponding to $\eta$. In particular $\mathcal{O}$ is a local domain with $\Frac(\mathcal{O})=K$. By the existence theorem quoted above, choose a valuation ring $A$ of $K$ dominating $\mathcal{O}$; then the local homomorphism $\mathcal{O} \rightarrow A$ induces a morphism

$$q:\Spec A \longrightarrow \Spec \mathcal{O} \longrightarrow T \hookrightarrow X\times_YX$$

which sends the generic point $(0)$ of $\Spec A$ to $\xi$ and the closed point $\mathfrak{m}_A$ to $\eta$.

Now set $g_1=p_1\circ q$, $g_2=p_2\circ q$, and since $f\circ p_1=f\circ p_2$ we have a well-defined morphism $w=f\circ g_1=f\circ g_2:\Spec A \rightarrow Y$. As seen in the proof of [Proposition 4](#prop4), choosing an affine open neighborhood $U$ of $x$ and an affine open subset $V$ of $Y$ containing $f(U)$, we have that $U\times_VU$ is an open neighborhood of $\xi$ in $X\times_YX$ and on it $\Delta$ is a closed embedding ([Lemma 5](#lem5)), so the stalk morphism $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$ is surjective and hence $\kappa(\xi) \rightarrow \kappa(x)$ is also surjective. On the other hand $p_1\circ\Delta=\id_X$, so the composition $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$ is the identity, and therefore the two morphisms are inverse isomorphisms of each other. Thus $K=\kappa(\xi)\cong\kappa(x)$. Under this identification, let $u:\Spec K \rightarrow X$ be the canonical morphism defined by the point $x$ and $\kappa(x)\cong K$; then $\Delta\circ u$ is the canonical morphism defined by the point $\xi$ and $\kappa(\xi)\cong K$, and this equals $q\circ j$. Indeed $q\circ j$ has image $\xi$ and induces the identity on $K=\Frac(\mathcal{O})=\kappa(\xi)$ on residue fields. Therefore

$$g_1\circ j=p_1\circ q\circ j=p_1\circ \Delta\circ u=u,\qquad g_2\circ j=p_2\circ q\circ j=p_2\circ\Delta\circ u=u$$

and $f\circ g_1=f\circ g_2=w$, so $g_1$ and $g_2$ are two liftings of the square given by $u$ and $w$. By assumption $g_1=g_2$, and then $\Delta\circ g_1$ and $q$ give $g_1$ and $g_2=g_1$ respectively when composed with $p_1$, $p_2$, so by the universal property of the fiber product $q=\Delta\circ g_1$. Therefore

$$\eta=q(\mathfrak{m}_A)=\Delta(g_1(\mathfrak{m}_A))\in \Delta(X)$$

and $\Delta(X)$ is closed under specialization. Combining with the previous observation, $\Delta(X)=\cl(\Delta(X))$, so $\Delta(X)$ is a closed set, and by [Proposition 4](#prop4) $f$ is separated.
:::

On the other hand, if $Y$ is Noetherian and $f$ is a finite type morphism, then in the above theorem one may replace arbitrary valuation rings by arbitrary discrete valuation rings; however, we cannot give a proof of this fact at our present stage, so we pass over it. As in the proposition situation above, the $\Spec$ of a general valuation ring has prime ideals forming a longer chain, going beyond the two-point picture of [Example 2](#ex2); but once we restrict to a discrete valuation ring, that picture comes back to life and we can read the theorem as a statement about germs of curves. That is, the above theorem says that when a way of embedding the punctured germ $\Spec K$ into $X$ is given, there is at most one way to fill it in to the whole germ $\Spec A$.

Let us actually verify this picture.

::: Example 7
Earlier we verified that the line with double origin $X$ is not separated using [Proposition 4](#prop4), but using [Theorem 6](#thm6) the same fact is revealed directly as the statement that a curve has two limits. Let $A=\mathbb{K}[t]_{(t)}$ be a discrete valuation ring with uniformizer $t$, let $K=\Frac(A)=\mathbb{K}(t)$, and let $Y=\Spec\mathbb{K}$. Now consider the morphism $u:\Spec K \rightarrow X$ defined by the ring homomorphism $\mathbb{K}[\x_0] \rightarrow K$, $\x_0\mapsto t$. Since $t$ is a unit in $K$, the image of $u$ lies in the open set where the two charts overlap. Since everything is over $\mathbb{K}$, the morphism $u$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form the outer square.

Now define two morphisms into the two charts $X_0=\Spec\mathbb{K}[\x_0]$, $X_1=\Spec\mathbb{K}[\x_1]$,

$$g_0:\Spec A \longrightarrow X_0\subseteq X,\qquad g_1:\Spec A \longrightarrow X_1\subseteq X$$

by $\x_0\mapsto t$ and $\x_1\mapsto t$ respectively; both are well defined since $t\in A$. Since the two charts are glued by identifying $\x_0$ and $\x_1$ away from the origin, we have $g_0\circ j=g_1\circ j=u$, and thus both are liftings of this square. However, $g_0$ sends $\mathfrak{m}_A=(t)$ to the origin $0_1$ of the first chart, while $g_1$ sends it to the origin $0_2$ of the second chart, so $g_0\neq g_1$. Hence the germ of the curve with a point removed has two limits, and this is why $X$ is not separated.
:::

Meanwhile, from [Theorem 6](#thm6) we obtain the following.

::: Corollary 8
For Noetherian schemes,

1. Open immersions and closed embeddings are both separated.
2. The composition of two separated morphisms is separated.
3. Separatedness is preserved under base change.
4. Separatedness is preserved under fiber products.
5. If $f:X \rightarrow Y$ and $g:Y \rightarrow Z$ are scheme morphisms and $g\circ f$ is separated, then $f$ is also separated.
:::
::: Proof
The first statement follows directly from the definition. If $f$ is a closed embedding, then for every affine open subset $V=\Spec B$ of $Y$ we have $f^{-1}(V)=\Spec A$ and $B \rightarrow A$ is surjective ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)); collecting all such $V$, the $f^{-1}(V)\times_Vf^{-1}(V)$ cover $X\times_YX$. On each of these, $\Delta$ is a closed embedding by the computation in [Lemma 5](#lem5), and since closed embeddings are affine-local on the target, $\Delta$ itself is a closed embedding. If $f$ is an open immersion, we view $X$ as an open subscheme of $Y$ and consider affine open subsets $V=\Spec B$ of $Y$ together with basic open subsets $\Spec B_b$ of $X$ contained in them. Then the $\Spec B_b\times_V\Spec B_{b'}$ cover $X\times_YX$, and since

$$B_b\otimes_BB_{b'}\cong B_{bb'}=\mathcal{O}(\Spec B_b\cap \Spec B_{b'})$$

we see that $\Delta$ is an isomorphism on each of these, hence in particular a closed embedding.

The remaining statements are obtained from the criterion of [Theorem 6](#thm6). We only need to check that uniqueness of liftings is inherited.

For the second statement, suppose we are given the outer square for $g\circ f$ with $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Z$, and two liftings $h_1,h_2:\Spec A \rightarrow X$. Then $f\circ h_1$ and $f\circ h_2$ are two liftings for the square of $g$ given by $u' = f\circ u$ and $v$, so $f\circ h_1=f\circ h_2$; then $h_1,h_2$ are two liftings for the square of $f$ given by $u$ and $f\circ h_1$, so $h_1=h_2$.

For the third statement, given $Y' \rightarrow Y$ and $X'=X\times_YY'$, $f':X' \rightarrow Y'$, suppose a square for $f'$ and two liftings $g_1',g_2':\Spec A \rightarrow X'$ are given. Their compositions with $X' \rightarrow X$ are two liftings for the square of $f$, hence are equal, and their compositions to $Y'$ are also the same morphism given by the square; thus by the uniqueness in the universal property of the fiber product, $g_1'=g_2'$.

For the fifth statement, given a square for $f$ and two liftings $g_1,g_2$, compose $\Spec A \rightarrow Y$ with $g$ to obtain a square for $g\circ f$; then $g_1,g_2$ are two liftings of this, so $g_1=g_2$.

Finally, the fourth statement follows from the third and second: for separated morphisms $f:X \rightarrow Y$, $f':X' \rightarrow Y'$ of $S$-schemes, $f\times f'$ decomposes as the composition

$$X\times_SX' \longrightarrow Y\times_SX' \longrightarrow Y\times_SY'$$

and the two morphisms are base changes of $f$ and $f'$ respectively.
:::

In particular, combining statements 2 and 5, we see that when $Y$ is a separated scheme, a $Y$-scheme $X$ is separated if and only if its structure morphism $X \rightarrow Y$ is separated. Since affine schemes are always separated by [Lemma 5](#lem5), for a scheme over an affine scheme we can check separatedness by looking only at the structure morphism.

## Proper morphisms

We now turn to the property corresponding to compactness. In topology we saw that compactness can be rephrased as the condition of being universally closed ([\[Topology\] §Proper Maps, ⁋Theorem 6](/en/math/topology/proper_maps#thm6)), and in algebraic geometry this same condition, with products replaced by fiber products, serves directly as the definition.

::: Definition 9
$f:X \rightarrow Y$ is called *universally closed* if $f$ is a closed map and, for any $Y' \rightarrow Y$, the morphism $X\times_Y Y' \rightarrow Y'$ is also closed. A finite type morphism that is separated and universally closed is called a *proper morphism*.
:::

Taking $Y'=Y$ shows that the second condition already implies the first, so the essential requirement is simply that every base change is a closed map. Since we work in the category of Noetherian schemes in this section, we will only consider base changes $Y' \rightarrow Y$ where $Y'$ is Noetherian when verifying universal closedness. That the condition for arbitrary $Y'$ follows from this is obtained by a limit argument, writing the coordinate ring of an affine $Y'$ as a filtered colimit of finitely generated subalgebras; we omit this as it lies outside the scope of this post.

Because a proper morphism requires both the separated condition and the universally closed condition, the criterion also splits into two parts. [Theorem 6](#thm6) characterized separatedness by uniqueness of liftings, so what remains is that existence of liftings characterizes universal closedness.

::: Proposition 10
For a finite type scheme morphism $f:X \rightarrow Y$ between Noetherian schemes, $f$ is universally closed if and only if for every valuation ring $A$ with quotient field $K=\Frac(A)$, every scheme morphism $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$, and every commutative diagram of the outer square

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.27em" alt="valuative_criterion" %}

there exists at least one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
As in the proof of [Theorem 6](#thm6), we write the outer square as $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$, $j:\Spec K \rightarrow \Spec A$, and continue to use the two standard facts cited there. Namely, any local subring of a field $K$ is dominated by a valuation ring $A$ with $\Frac(A)=K$, and a morphism $\Spec K \rightarrow X$ is the same as a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. To this we add the following maximality property of valuation rings. If a local subring $\mathcal{O}\subseteq K$ dominates a valuation ring $A$ of $K$, then $\mathcal{O}=A$. Indeed, if $c\in\mathcal{O}$ is nonzero and $c\notin A$, then by definition of a valuation ring $c^{-1}\in A$, and since $c\notin A$, $c^{-1}$ is not a unit of $A$. Hence $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$, but $c\in\mathcal{O}$, so $c^{-1}$ would be a unit of $\mathcal{O}$, a contradiction. Thus $\mathcal{O}\subseteq A$, and by the definition of domination $A\subseteq\mathcal{O}$, so $\mathcal{O}=A$.

First, assume $f$ is universally closed and construct a lifting. Base changing along $v$, we obtain $X_A=X\times_Y\Spec A$ with projection $\pi:X_A \rightarrow \Spec A$, and $\pi$ is a closed map. ([Definition 9](#def9)) Meanwhile, $u$ and $j$ induce a morphism $\tilde{u}:\Spec K \rightarrow X_A$ over $\Spec A$ by the universal property of the fiber product, and if we find an extension of $\tilde{u}$ to a section of $\pi$ of the form $\Spec A \rightarrow X_A$, then projecting this to $X$ yields the desired lifting.

Let $\xi\in X_A$ be the image of $\tilde{u}$ and give $Z=\cl(\{\xi\})$ the reduced scheme structure. ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)) Since $\pi\circ\tilde{u}=j$, $\pi(\xi)$ is the generic point $(0)$ of $\Spec A$, and since $\pi$ is a closed map, $\pi(Z)$ is a closed set containing $(0)$, hence all of $\Spec A$. Therefore there exists $z\in Z$ with $\pi(z)=\mathfrak{m}_A$.

Let us examine the residue fields. The morphism $\kappa((0))=K \rightarrow K$ induced by $\pi\circ \tilde{u}=j$ at $(0)$ is the identity, and this is the composite of the morphisms $K\rightarrow\kappa(\xi)$ induced by $\pi$ and $\kappa(\xi) \rightarrow K$ induced by $\tilde{u}$, so the two morphisms are inverse isomorphisms of each other. Hence $\kappa(\xi)\cong K$. Then $Z$ is an integral scheme with generic point $\xi$, so as in the proof of [Theorem 6](#thm6) we may choose an affine open subset containing $z$ to obtain

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K.$$

Also, the morphism $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$ induced by $\pi\vert_Z$ is a local homomorphism, and since the $K \rightarrow \kappa(\xi)=K$ it induces at the generic point is the identity, this morphism is an inclusion of subrings of $K$. That is, $\mathcal{O}$ is a local subring of $K$ dominating $A$, and by the maximality above we have $\mathcal{O}_{Z,z}=A$.

Then we obtain the canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$, and its composition with $\pi$ corresponds to the identity of $A$ at the ring level, so it is a section of $\pi$. The restriction of this section to $\Spec K$ has image $\xi$ and induces the identity of $\kappa(\xi)=K$ on residue fields, so it equals $\tilde{u}$. Therefore, projecting this section to $X$ yields $g:\Spec A \rightarrow X$ with $g\circ j=u$ and $f\circ g=v$.

Conversely, assume the existence part holds. Following the convention stated after [Definition 9](#def9), we only consider base changes $Y' \rightarrow Y$ where $Y'$ is a Noetherian scheme.

First, the existence part is stable under base change. Given $Y' \rightarrow Y$ with $X'=X\times_YY'$ and $f':X' \rightarrow Y'$, suppose $\Spec K \rightarrow X'$ and $\Spec A \rightarrow Y'$ form an outer square for $f'$. Composing these with $X' \rightarrow X$ and $Y' \rightarrow Y$ gives an outer square for $f$, so a lifting $g:\Spec A \rightarrow X$ exists, and $g$ together with $\Spec A \rightarrow Y'$ gives a unique $g':\Spec A \rightarrow X'$ by the universal property. Since $g'\circ j$ and the given $\Spec K \rightarrow X'$ have the same composites with $X' \rightarrow X$ and $X' \rightarrow Y'$ respectively, they are equal, and thus $g'$ is a lifting for $f'$. On the other hand, finite type morphisms are stable under base change and a finite type scheme over a Noetherian scheme is again Noetherian, so $X'$ is Noetherian and $f'$ is of finite type. Therefore, if we show that $f$ is a closed map whenever a Noetherian scheme $X$ and a finite type morphism $f:X \rightarrow Y$ satisfy the existence part of the criterion, then applying this to every base change completes the proof.

To see this, choose a closed subset $T$ of $X$ and give it the reduced scheme structure. The closed embedding $T\hookrightarrow X$ is a finite morphism, hence ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)) of finite type, so $T$ is a Noetherian scheme and $f\vert_T:T \rightarrow Y$ is also of finite type. Moreover, $f\vert_T$ inherits the existence part of the criterion. Indeed, if $\Spec K \rightarrow T$ and $\Spec A \rightarrow Y$ form a square for $f\vert_T$, applying the criterion to $\Spec K \rightarrow T\hookrightarrow X$ yields a lifting $g_0:\Spec A \rightarrow X$. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and a morphism preserves specializations, so $g_0(\Spec A)\subseteq \cl(\{g_0((0))\})\subseteq T$, and since $\Spec A$ is reduced, $g_0$ factors through $T$. The last fact is obtained as follows. Let $\varphi:S \rightarrow X$ be a morphism from a reduced scheme $S$ whose image lies in a closed subset $T$, and choose an affine open subset $\Spec B$ of $X$ and an affine open subset $\Spec R$ of $\varphi^{-1}(\Spec B)$. If $T\cap \Spec B=Z(\mathfrak{b})$ with $\mathfrak{b}$ a radical ideal, then the reduced structure on $T$ is $\Spec (B/\mathfrak{b})$ there, and the corresponding ring homomorphism $\psi:B \rightarrow R$ satisfies $\mathfrak{b}\subseteq \psi^{-1}(\mathfrak{p})$ for every prime ideal $\mathfrak{p}\subseteq R$, so

$$\psi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\mathfrak{N}(R)=(0).$$

Hence $\psi$ uniquely factors through $B/\mathfrak{b}$, and these local factorizations glue by uniqueness.

Thus it suffices to show that $f(T)=f\vert_T(T)$ is closed, and ultimately it is enough to show that the image $f(X)$ is closed for a finite type morphism $f:X \rightarrow Y$ (with $X$ Noetherian) satisfying the existence part of the criterion.

We first show that $f(X)$ is closed under specialization. Let $y_1=f(x_1)\in f(X)$ and $y_0\in\cl(\{y_1\})$. Giving $W=\cl(\{y_1\})$ the reduced scheme structure, $W$ is an integral scheme with generic point $y_1$, and as before $\mathcal{O}=\mathcal{O}_{W,y_0}$ is a local domain with $\Frac(\mathcal{O})=\kappa(y_1)$. Now set $K=\kappa(x_1)$ and view $\mathcal{O}$ as a local subring of $K$ via the field homomorphism $\kappa(y_1)\hookrightarrow K$ induced by $f$. Then there exists a valuation ring $A$ of $K$ dominating $\mathcal{O}$, and from this we obtain the two morphisms

$$\Spec A \longrightarrow \Spec\mathcal{O} \longrightarrow W\hookrightarrow Y,\qquad u:\Spec K \longrightarrow X.$$

Here $u$ is the canonical morphism defined by the point $x_1$ and $\kappa(x_1)=K$. These form the outer square because both composites $\Spec K \rightarrow Y$ are the canonical morphism defined by the point $y_1$ and the field homomorphism $\kappa(y_1)\hookrightarrow K$. By the existence part of the criterion, a lifting $g_0:\Spec A \rightarrow X$ exists, and since $\Spec A \rightarrow \Spec\mathcal{O}$ comes from a local homomorphism, $\mathfrak{m}_A$ maps to $\mathfrak{m}_\mathcal{O}$, that is, to $y_0$. Therefore $f(g_0(\mathfrak{m}_A))=y_0$ and $y_0\in f(X)$.

Finally, we repeat the topological observation from the proof of [Theorem 6](#thm6) verbatim. If $\eta_1,\ldots,\eta_r$ are the generic points of the irreducible components $X_1,\ldots,X_r$ of $X$, then $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$, so

$$\cl(f(X))=\bigcup_{i=1}^r\cl(\{f(\eta_i)\}),$$

and thus every point of $\cl(f(X))$ is a specialization of a point of $f(X)$. Since we have shown that $f(X)$ is closed under specialization, we have $f(X)=\cl(f(X))$. 
:::

Putting the two pieces together, we obtain the valuative criterion for properness.

::: Theorem 11
For a finite type scheme morphism $f:X \rightarrow Y$ between Noetherian schemes, $f$ is proper if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, and for any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ making the outer square of the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.27em" alt="valuative_criterion" %}

there exists exactly one $\Spec A \rightarrow X$ such that the entire diagram commutes.
:::
::: Proof
Since $f$ is assumed to be of finite type, by [Definition 9](#def9), $f$ being proper is equivalent to $f$ being separated and universally closed. By [Theorem 6](#thm6), $f$ being separated means that any outer square has at most one lifting, and by [Proposition 10](#prop10), $f$ being universally closed means that any outer square has at least one lifting. These two conditions together mean that every square has exactly one lifting.
:::

It is good to see what the criterion looks like when it fails. If [Example 7](#ex7) was the case where uniqueness fails, the following is the case where existence fails.

::: Example 12
$\mathbb{A}^1_\mathbb{K}=\Spec\mathbb{K}[\x]$ is not proper over $\Spec\mathbb{K}$. Choose $A=\mathbb{K}[t]_{(t)}$ and $K=\Frac(A)=\mathbb{K}(t)$, and consider the morphism $u:\Spec K \rightarrow \mathbb{A}^1_\mathbb{K}$ defined by the ring homomorphism

$$\mathbb{K}[\x] \longrightarrow K;\qquad \x\mapsto 1/t.$$

Since everything is over $\mathbb{K}$, the morphisms $u$ and the structure map $\Spec A \rightarrow \Spec\mathbb{K}$ form the outer square. If a lifting $g:\Spec A \rightarrow \mathbb{A}^1_\mathbb{K}$ existed, it would correspond to a ring homomorphism $\mathbb{K}[\x] \rightarrow A$, and the condition $g\circ j=u$ means that the composition of this homomorphism with $A\hookrightarrow K$ sends $\x$ to $1/t$. Thus $1/t$ must lie in $A$, but this is impossible because $t$ is a uniformizer of $A$. Hence no lifting exists, and by [Theorem 11](#thm11), $\mathbb{A}^1_\mathbb{K} \rightarrow \Spec\mathbb{K}$ is not proper.

Geometrically, this $u$ is the germ of a curve escaping to infinity at the origin, and the criterion simply reads off that this limit does not exist inside $\mathbb{A}^1_\mathbb{K}$. The same calculation in $\mathbb{P}^1_\mathbb{K}$ makes $1/t$ become $t$ in the chart corresponding to infinity, so a lifting exists; this will be generalized in [Theorem 15](#thm15).
:::

Likewise, the following corollary holds.

::: Corollary 13
For Noetherian schemes,

1. A closed embedding is proper.
2. The composition of proper morphisms is proper.
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber product.
5. If $f:X \rightarrow Y$ and $g:Y \rightarrow Z$ are scheme morphisms, $g$ is separated, and $g\circ f$ is a proper morphism, then $f$ is also a proper morphism.
:::
::: Proof
For (1), a closed embedding is separated by (1) of [Corollary 8](#cor8), and it is a finite morphism, hence of finite type ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)). Also, a closed embedding is a closed map and is stable under base change, so it is universally closed (as in the proof of [Theorem 6](#thm6)).

For (2), separatedness follows from (2) of [Corollary 8](#cor8), and the composition of finite type morphisms is of finite type, so it suffices to show universally closed. Given $Z' \rightarrow Z$, we have $X\times_ZZ'=X\times_Y(Y\times_ZZ')$, so the two morphisms

$$X\times_ZZ' \longrightarrow Y\times_ZZ' \longrightarrow Z'$$

are the base changes of $f$ and $g$ respectively, and hence both are closed maps. Since the composition of closed maps is closed, $X\times_ZZ' \rightarrow Z'$ is also closed.

For (3), separatedness is (3) of [Corollary 8](#cor8), finite type is stable under base change, and universally closed follows immediately from the definition because a base change of a base change is again a base change. Then (4) follows by applying the same decomposition as in (4) of [Corollary 8](#cor8) to (2) and (3).

Finally, we prove (5). Consider the graph morphism $\Gamma_f:X \rightarrow X\times_ZY$ induced by $\id_X$ and $f$; then $f=p_2\circ\Gamma_f$. The square formed by $\Gamma_f$ and $f\times\id_Y: X\times_ZY \rightarrow Y\times_ZY$ is cartesian with bottom side $\Delta_{Y/Z}:Y \rightarrow Y\times_ZY$. Indeed, for any $T$, matching two morphisms into $Y\times_ZY$ amounts to choosing a pair $a:T \rightarrow X$ and $b:T \rightarrow Y$ with $f\circ a=b$, and such a pair is determined by $a$ alone. Then, since $g$ is separated by assumption, $\Delta_{Y/Z}$ is a closed embedding, so $\Gamma_f$ is also a closed embedding and hence proper by (1). On the other hand, $p_2:X\times_ZY \rightarrow Y$ is the base change of $g\circ f$ along $g$, so it is proper by (3). Therefore $f=p_2\circ\Gamma_f$ is proper by (2).
:::

The assumption that $g$ is separated in (5) is needed because the reason $\Gamma_f$ becomes a closed embedding in the proof is precisely that $\Delta_{Y/Z}$ is a closed embedding. Without this assumption, the guarantee that $\Gamma_f$ is a closed embedding disappears and the argument breaks down. Note that (5) of [Corollary 8](#cor8) did not require such an assumption, so one should be careful that the two statements have different shapes.

Meanwhile, (1) of [Corollary 13](#cor13) is the following special case. This is the most typical example showing how the criterion is actually used, where the existence follows from the single fact that a valuation ring is integrally closed.

::: Corollary 14
A finite morphism between Noetherian schemes is proper.
:::
::: Proof
A finite morphism $f:X \rightarrow Y$ is an affine morphism, so for any affine open subset $V\subseteq Y$, the inverse image $f^{-1}(V)$ is affine. Hence $f$ is separated by [Lemma 5](#lem5) and the affine-local criterion for closed embeddings ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)). Also, a finite morphism is of finite type ([§Properties of Scheme Morphisms, ⁋Proposition 15](/en/math/scheme_theory/properties_of_scheme_morphisms#prop15)). Therefore, by [Theorem 11](#thm11), it suffices to verify the existence of a lifting.

Suppose we are given the outer square $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$. Every point of $\Spec A$ is a specialization of the generic point $(0)$, and morphisms preserve specializations. Thus, choosing an affine open subset $V=\Spec B$ of $Y$ containing $v(\mathfrak{m}_A)$, we see that $V$ also contains $v((0))$, and hence $v$ factors through $V$. Then the image of $u$ lies in $f^{-1}(V)=\Spec C$, and $C$ is finitely generated as a $B$-module. Now the problem reduces to constructing a map $C \rightarrow A$ compatible with the given ring homomorphisms

$$B \longrightarrow A,\qquad C \longrightarrow K.$$

For any $c\in C$, since $c$ is integral over $B$, there exist suitable $b_i\in B$ such that

$$c^n+b_{n-1}c^{n-1}+\cdots+b_0=0.$$

Pushing this equation through $C \rightarrow K$, the image of $c$ is integral over the image of $B$. Since the image of $B$ lies inside $A$, the image of $c$ is integral over $A$. But valuation rings are always integrally closed ([\[Commutative Algebra\] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6), part 2), so the image of $c$ belongs to $A$. Hence $C \rightarrow K$ factors through $A$, and this gives the desired lifting.
:::

The same criterion yields a much stronger result. By definition, a projective morphism is a composition of a closed embedding and the projection $\mathbb{P}^n_Y \rightarrow Y$ ([Definition 1](#def1)), and the closed embedding part is already handled by part 1 of [Corollary 13](#cor13). Thus, ultimately we need only check that projective space is proper over the base. Moreover, by base change this reduces to the single morphism $\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$.

::: Theorem 15
A projective morphism between Noetherian schemes is proper, and a quasi-projective morphism is separated and of finite type.
:::
::: Proof
The heart of the proof is that $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ is proper, which follows from a direct verification of the criterion in [Theorem 11](#thm11). First, $\mathbb{P}^n_\mathbb{Z}$ is obtained by gluing $n+1$ affine charts

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

along $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$. Since $\x_i/\x_i=1$, each $U_i$ is the spectrum of an $n$-variable polynomial ring over $\mathbb{Z}$. In particular each $U_i$ is the spectrum of a Noetherian ring, and since there are finitely many charts, $\mathbb{P}^n_\mathbb{Z}$ is a Noetherian scheme and $\pi$ is of finite type. ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14))

That $\pi$ is separated is checked directly on the charts. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$ is covered by affine open subsets $U_i\times_\mathbb{Z}U_j$, and since $p_1\circ\Delta=p_2\circ\Delta=\id$, we have $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$. Now consider the ring homomorphism induced by $\Delta$ on this open set

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \longrightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

The right-hand side is generated over $\mathbb{Z}$ by the $\x_l/\x_i$ and by $(\x_j/\x_i)^{-1}=\x_i/\x_j$; the former come from the first factor and the latter from the second, so this morphism is surjective. Hence $\Delta$ is a closed embedding over each $U_i\times_\mathbb{Z}U_j$, and since closed embeddings are affine-local on the target ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), $\Delta$ itself is a closed embedding.

Since $\Spec \mathbb{Z}$ is a terminal object in the category of schemes, giving the outer square for a valuation ring $A$ and $K=\Frac(A)$ is the same as giving a morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$. Uniqueness of the lifting follows from $\pi$ being separated and [Theorem 6](#thm6), so we only need to show existence. Since $\Spec K$ is a single point, the image of the given morphism lies in some chart $U_i$, and thus this morphism corresponds to a ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \longrightarrow K$$

Let $a_j\in K$ be the image of $\x_j/\x_i$; then $a_i=1$. Now define $s\preceq t$ on $K^\times$ by $t/s\in A$; by the definition of a valuation ring, for any $s,t$ either $s\preceq t$ or $t\preceq s$, and if $t/s\in A$ and $r/t\in A$ then $r/s=(r/t)(t/s)\in A$, so $\preceq$ is a total preorder on $K^\times$. Since $a_i=1\neq 0$, the finite set $\{a_j \mid a_j\neq 0\}$ is non-empty, and therefore we can choose a minimal element $a_k$ of this set. Then for every $j$,

$$b_j:=a_j/a_k\in A$$

(If $a_j=0$, then $b_j=0\in A$.) In particular $b_k=1$, so the ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \longrightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

is defined, and this gives a morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$. To show that this is a lifting, it suffices to check that its composition with $A\hookrightarrow K$ equals the originally given morphism. Since $a_k\neq 0$, the original ring homomorphism sends $\x_k/\x_i$ to the unit $a_k$ of $K$, and hence the image of the original morphism lies in $D(\x_k/\x_i)=U_i\cap U_k$. Then on $U_k$ this morphism is given by $\x_j/\x_k\mapsto a_j/a_k=b_j$ via the transition relation

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1}$$

so it coincides exactly with the restriction of the $\Spec A \rightarrow U_k$ we constructed above to $\Spec K$. Thus the existence condition in the criterion holds, and by [Theorem 11](#thm11), $\pi$ is proper.

For any Noetherian scheme $Y$, we have $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$. When $Y=\Spec B$, the chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$ of $\mathbb{P}^n_B$ coincides with $U_i\times_{\Spec\mathbb{Z}}\Spec B$, and for general $Y$ we simply glue these. Therefore by [Corollary 13](#cor13), $\mathbb{P}^n_Y \rightarrow Y$ is proper, and in particular of finite type, so $\mathbb{P}^n_Y$ is a Noetherian scheme.

Now if $f:X \rightarrow Y$ is projective, then $f$ is the composition of a closed embedding $X\hookrightarrow \mathbb{P}^n_Y$ and the projection $\mathbb{P}^n_Y \rightarrow Y$. ([Definition 1](#def1)) A closed embedding is proper, and the composition of two proper morphisms is proper ([Corollary 13](#cor13)), so $f$ is proper.

Finally, suppose $f:X \rightarrow Y$ is quasi-projective, and decompose it as $f=g\circ\iota$ where $\iota: X \rightarrow X'$ is an open immersion and $g:X' \rightarrow Y$ is projective. ([Definition 1](#def1)) By what we have just shown, $g$ is proper, hence separated and of finite type. On the other hand, an open immersion is separated, and the composition of two separated morphisms is separated ([Corollary 8](#cor8)), so $f$ is separated. Also, an open immersion is locally of finite type, and since $X$ is Noetherian, the preimage of any affine open subset of $X'$ under $\iota$ is an open subset of a Noetherian space, hence quasi-compact. Thus $\iota$ is of finite type ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14)), and since the composition of two finite type morphisms is of finite type, $f$ is also of finite type.
:::

This gives us the classical corollary of the criterion. Since a proper morphism is by definition a closed map, the image of any morphism out of a projective scheme is always closed.

::: Corollary 16
For a projective scheme $X$ over $\mathbb{K}$, a separated finite type $\mathbb{K}$-scheme $Z$, and a $\mathbb{K}$-morphism $\varphi:X \rightarrow Z$, the image $\varphi(X)$ is a closed subset of $Z$.
:::
::: Proof
Since the structure morphism $X \rightarrow \Spec\mathbb{K}$ is projective, it is proper by [Theorem 15](#thm15), and $Z \rightarrow \Spec\mathbb{K}$ is separated by assumption. Applying item 5 of [Corollary 13](#cor13) to $\varphi$ and $Z \rightarrow \Spec\mathbb{K}$, we obtain that $\varphi$ is proper, and in particular $\varphi$ is a closed map; since $X$ itself is a closed subset of $X$, it follows that $\varphi(X)$ is closed.
:::

This is the reason why in classical algebraic geometry a projective variety is called *complete*, and it is also the geometric form of the compactness principle. In contrast with [Example 12](#ex12), this does not hold for $\mathbb{A}^1_\mathbb{K}$: for instance, projecting the hyperbola $Z(\x\y-1)$ in $\mathbb{A}^2_\mathbb{K}$ onto the first coordinate yields image $\mathbb{A}^1_\mathbb{K}\setminus\{0\}$, which is not closed.

Finally, let us note why these criteria are called *valuative*. The name valuation ring itself comes from the fact that it is the ring of elements whose values under a valuation $\nu:K^\times \rightarrow G$ are non-negative ([\[Commutative Algebra\] §Regular Local Rings, ⁋Definition 7](/en/math/commutative_algebra/regular_local_rings#def7)), and as we saw in [Example 2](#ex2), the generic point and the closed point of $\Spec A$ correspond respectively to the place where $\nu$ vanishes and the place where $\nu>0$. Thus, finding a lifting $\Spec A \rightarrow X$ means finding a point on $X$ that serves as the center of the valuation $\nu$, and the criteria translate the uniqueness and existence of such a center into separatedness and universal closedness respectively.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
