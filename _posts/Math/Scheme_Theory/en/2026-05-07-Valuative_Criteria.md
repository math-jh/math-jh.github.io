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
translated_at: 2026-07-14T02:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T02:00:01+00:00
---
In this post we define separated morphisms and proper morphisms. It is helpful to think of them as the algebraic-geometric transplants of the Hausdorff and compactness conditions from topology.

In previous posts we defined open subschemes ([§Schemes, ⁋Definition 4](/en/math/scheme_theory/schemes#def4)), examined closed embeddings and the resulting closed subschemes, and studied ideal sheaves ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2), [⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5)). We now add the following concepts.

::: Definition 1
Let a scheme morphism $f: X \rightarrow Y$ be given.

1. $f$ is called an *open immersion* if it induces an isomorphism between $X$ and an open subscheme of $Y$.
2. $f$ is called *projective* if for some suitable $n$, $f$ can be factored as a composition of a closed embedding and a projection of the form $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$. ([§Projective Schemes](/en/math/scheme_theory/projective_schemes))
3. $f$ is called *quasi-projective* if it can be factored as a composition of a suitable open immersion $X \rightarrow X'$ and a projective morphism $X' \rightarrow Y$.
:::

The first definition is trivial, and the second and third are also [\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3) and [\[Algebraic Varieties\] §Quasi-Projective Varieties, ⁋Definition 1](/en/math/algebraic_varieties/quasi_projective_varieties#def1) treated in their relative version, that is, in $\Sch_{/Y}$.

Before starting the main discussion, it is helpful to examine the following example.

::: Example 2
Let a ring $A$ be a discrete valuation ring as a subring of a field $K$. That is, for every $x\in K^\times$ either $x\in A$ or $x^{-1}\in A$, and $A$ is Noetherian with principal maximal ideal $\mathfrak{m}$. ([[Commutative Algebra] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5)) Since every $x\in K^\times$ is expressed as a ratio of elements of $A$ via $x$ or $x^{-1}$, we have $K=\Frac(A)$. Moreover $A$ is a local ring with $\mathfrak{m}$ as its unique maximal ideal ([[Commutative Algebra] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6)), and choosing a uniformizer $\pi$, every $f\in K^\times$ is uniquely expressed as $f=\pi^nu$ for an integer $n$ and a unit $u$ ([[Commutative Algebra] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8)), so every nonzero ideal of $A$ is of the form $(\pi^n)$. In particular $A$ is a principal ideal domain whose prime ideals are exactly $(0)$ and $\mathfrak{m}=(\pi)$.

Then $\Spec A$ consists of the two points $(0)$ and $\mathfrak{m}$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $\Spec A$ is

$$D(\pi)=\Spec A\setminus Z(\mathfrak{m})=\{(0)\}.$$

Then by [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6)

$$\mathcal{O}(D(\pi))\cong A_\pi\cong K.$$

Of course $\mathcal{O}(\Spec A)\cong A$.

The two points of $\Spec A$ can be viewed geometrically through their respective residue fields. Using [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8), from

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong K,\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

we obtain

$$\kappa((0))=K, \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong A/\mathfrak{m}.$$
:::

Let us examine the example a little more geometrically. Since $Z((0))=\Spec A$, the closure of $(0)$ is all of $\Spec A$, so $(0)$ becomes the generic point of this space. Such a situation is seen especially intuitively when $\mathcal{O}_{C,p}$ is a discrete valuation ring for a curve $C$ and a point $p$ on it. Concretely, the stalk

$$\mathcal{O}_{C,p}=\varprojlim_{U\supset p} \mathcal{O}(U)$$

may be viewed as the germ at the point $p$, and the generic point $(0)$ of $\Spec \mathcal{O}_{C,p}$ is precisely what carries this data. Then the remaining (unique) point $\mathfrak{m}$ corresponds exactly to the point $p$, and the fact that it is a specialization of $(0)$ reflects that in defining a germ we look at neighborhoods arbitrarily close to $p$.

The role of $\Spec K$ in this picture is revealed by looking at the side of functions. The functions on $\Spec A$ are $A$ itself, that is, the germs regular at $p$, while the elements of $K\cong A_\pi$, the functions on the only nontrivial open subset $D(\pi)=\{(0)\}$, are those obtained by allowing the form $f=\pi^nu$ down to negative degrees $n$. ([[Commutative Algebra] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8), item 2) That is, these are the functions having a pole at $p$ of finite order, in other words those regular on the whole neighborhood once $p$ alone is removed; hence $\Spec K$ is this germ with its center $p$ removed, a space that has lost the information at $p$ and retains only the information about a neighborhood of $p$, and the canonical morphism $\Spec K \rightarrow \Spec A$ is exactly the inclusion that this picture defines.

Then a morphism $\Spec K \rightarrow X$ is a punctured curve germ mapping into $X$, and extending it to $\Spec A \rightarrow X$ amounts to recovering the missing point inside $X$ and gluing the curve back together, i.e., finding the limit of the curve. The statement that there is at most one such extension is separatedness, and that there is exactly one is properness; this is the content of the two criteria we will see below. Topologically this corresponds exactly to the fact that limits are unique in a Hausdorff space ([[Topology] §Hausdorff Spaces, ⁋Proposition 4](/en/math/topology/Hausdorff_spaces#prop4)) and that limits always exist in a compact space. ([[Topology] §Compactness and Paracompactness, ⁋Lemma 1](/en/math/topology/compactness#lem1))

## Separated Morphisms

::: Definition 3
For a scheme morphism $f:X \rightarrow Y$, the unique morphism induced by two copies of $\id_X$ through the universal property of the fiber product, namely the dashed arrow $\Delta: X \rightarrow X \times_Y X$ in the diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-1.svg width="13.51em" alt="diagonal_morphism" %}

is called the *diagonal morphism* of $f$. ([§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1)) If $\Delta$ is a closed embedding, we call $f$ *separated*, and say $X$ is *separated* over $Y$. If $X$ is separated over $\Spec \mathbb{Z}$, we simply call $X$ a *separated* scheme.
:::

When the morphism whose diagonal is meant has to be specified, we write $\Delta_{X/Y}$ instead of $\Delta$. By definition the two projections $p_1,p_2: X\times_YX \rightarrow X$ satisfy $p_1\circ\Delta=p_2\circ\Delta=\id_X$, a fact used repeatedly below. In particular $\Delta$ is injective and the restriction of $p_1$ to $\Delta(X)$ furnishes a continuous inverse, so $\Delta$ is always a homeomorphism onto $\Delta(X)$. Asking whether $\Delta$ is a closed embedding therefore amounts to asking whether $\Delta(X)$ is closed and whether every function on $X$ arises by restricting a function on $X\times_YX$. ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2))

In algebraic geometry, separatedness is regarded as the property replacing Hausdorffness. Recalling that a topological space $T$ is Hausdorff precisely when the diagonal is closed in $T\times T$ ([[Topology] §Hausdorff Spaces, ⁋Lemma 5](/en/math/topology/Hausdorff_spaces#lem5)), the reason becomes clear in the following proposition.

::: Proposition 4
The following are equivalent for $f:X \rightarrow Y$: $f$ is separated, and the image of $X$ under the diagonal morphism $\Delta: X \rightarrow X\times_YX$ is a closed set.
:::
::: Proof
By definition, if $f$ is separated then $\Delta(X)$ is closed is obvious. Thus we assume $\Delta(X)$ is closed and show that $\Delta$ is a closed embedding. As seen above, $\Delta$ is always a homeomorphism onto $\Delta(X)$, so together with the assumption the topological condition is already secured and it remains only to show that $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$ is surjective. This can be checked on stalks.

First, there is nothing to check at a point $q\notin\Delta(X)$. Since $\Delta(X)$ is closed by assumption, there is an open neighborhood $W$ of $q$ with $W\cap\Delta(X)=\emptyset$, and then $\Delta^{-1}(W)=\emptyset$, so

$$(\Delta_\ast\mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$$

and hence $(\Delta_\ast\mathcal{O}_X)_q=0$. The open neighborhoods chosen below do not cover points outside $\Delta(X)$, so this is precisely where the assumption is used.

Now consider a point of the form $\Delta(p)$. For an arbitrary $p\in X$ we can choose an open affine subset $U$ containing $p$, and if necessary restrict $U$ so that $f(U)$ lies in some open affine subset $V$ of $Y$. Then $U\times_VU$ is an open subset of $X\times_YX$ and an open neighborhood of $\Delta(p)$, and since $p_1\circ\Delta=p_2\circ\Delta=\id_X$ we have $\Delta^{-1}(U\times_VU)=U$. On it $\Delta: U \rightarrow U\times_VU$ is a closed embedding by the following [Lemma 5](#lem5), so $\mathcal{O}_{U\times_VU} \rightarrow \Delta_\ast\mathcal{O}_U$ is surjective and in particular the morphism between the stalks at $\Delta(p)$ is surjective.
:::

::: Lemma 5
Any morphism between affine schemes is always separated.
:::
::: Proof
If $X=\Spec A$ and $Y=\Spec B$, then $X\times_YX=\Spec(A\otimes_BA)$ ([§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2)) and $\Delta$ is induced by the ring homomorphism

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

This ring homomorphism sends $a\otimes 1$ to $a$, hence is surjective, and therefore $\Delta$ is a closed embedding. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))
:::

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10). For convenience, let us denote this scheme by $X$. As it is a scheme over $\mathbb{K}$, what we look at is $X\times_\mathbb{K}X$. Since $X$ is obtained by gluing two copies of $\mathbb{A}^1_\mathbb{K}$ away from the origin, $X\times_\mathbb{K}X$ is obtained by gluing four copies of $\mathbb{A}^2_\mathbb{K}$, so a point with both coordinates nonzero appears once, a point with exactly one coordinate zero appears twice, and the origin appears four times. Now the image of $\Delta$ is the usual diagonal away from the origin, and the two origins $0_1,0_2$ of $X$ go to $(0_1,0_1)$ and $(0_2,0_2)$ among the four origins. That is, the remaining two origins $(0_1,0_2)$ and $(0_2,0_1)$ do not belong to $\Delta(X)$. However, inside the chart $\mathbb{A}^2_\mathbb{K}$ containing them, $\Delta(X)$ is the diagonal with the origin removed and its closure is the whole diagonal, so these two points do belong to the closure of $\Delta(X)$. Hence $\Delta(X)$ is not closed and by [Proposition 4](#prop4) $X$ is not separated. This space was, as expected, an example of a non-Hausdorff space in topology.

Let us now turn to the criterion for separatedness. Unlike in [Example 2](#ex2), the criterion is required for all valuation rings, discrete or not, that is, for every subring $A$ of a field $K$ satisfying only the condition that $x\in A$ or $x^{-1}\in A$ for each $x\in K^\times$. ([[Commutative Algebra] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5)) Also, below $j:\Spec K \rightarrow \Spec A$ always denotes the morphism induced by the inclusion $A\hookrightarrow K$.

::: Theorem 6
For a Noetherian scheme $X$ and a scheme morphism $f:X \rightarrow Y$, the following are equivalent: $f$ is separated; and for every valuation ring $A$ and its quotient field $K=\Frac(A)$, given any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.27em" alt="valuative_criterion" %}

with the outer square given, there is at most one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
That the outer square is given means that morphisms $u:\Spec K \rightarrow X$ and $v: \Spec A \rightarrow Y$ are given such that $f\circ u=v\circ j$; a lifting of this square means a $g:\Spec A \rightarrow X$ satisfying $g\circ j=u$ and $f\circ g=v$.

Throughout the proof we use two standard facts. The first is the existence theorem for valuation rings: given a field $K$ and a local subring $\mathcal{O}$ inside it, there exists a valuation ring $A$ with $\Frac(A)=K$, $\mathcal{O}\subseteq A$, and $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$. In this case we say $A$ *dominates* $\mathcal{O}$, and such an $A$ is obtained by applying Zorn's lemma to the collection of local subrings of $K$ dominating $\mathcal{O}$. This is a result in commutative algebra not treated in this post, so we use it without proof and defer the details to **[AM]**. The second is that for a field $K$, a morphism $\Spec K \rightarrow X$ corresponds bijectively to a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. This follows from the fact that when $X=\Spec B$, a ring homomorphism $B \rightarrow K$ gives the pair of its kernel, a prime ideal $\mathfrak{p}$, and $\kappa(\mathfrak{p}) \rightarrow K$; the general case is handled by choosing an affine open neighborhood of $x$.

First assume $f$ is separated, and suppose two liftings $g_1, g_2$ of the above square are given. Since $f\circ g_1=f\circ g_2=v$, by the universal property of the fiber product there exists a unique $h:\Spec A \rightarrow X\times_YX$ such that $p_1\circ h=g_1$, $p_2\circ h=g_2$. Here $p_1,p_2$ are the two projections. Now since $\Delta$ is a closed embedding, the base change

$$Z=\Spec A\times_{X\times_YX}X \longrightarrow \Spec A$$

is also a closed embedding. That closed embeddings are stable under base change follows from the affine-local fact that the base change of $B \rightarrow B/\mathfrak{b}$ is $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$, which is still surjective. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))

On the other hand $p_1\circ h\circ j=g_1\circ j=u$ and $p_2\circ h\circ j=g_2\circ j=u$, and $p_1\circ \Delta\circ u=u$ and $p_2\circ\Delta\circ u=u$, so by the uniqueness in the universal property we have $h\circ j=\Delta\circ u$. Therefore $j$ factors through the pullback $Z$, and in particular the image of $Z \rightarrow \Spec A$ is a closed set containing the image of $j$, namely the zero ideal $(0)$ of $A$. Since $A$ is a domain, $(0)$ is the generic point of $\Spec A$ ([§The Topological Structure of Schemes, ⁋Example 5](/en/math/scheme_theory/topology_of_schemes#ex5)), and thus the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself. Then $Z$ is a closed subscheme of $\Spec A$ of the form $\Spec(A/\mathfrak{a})$ for some ideal $\mathfrak{a}\subseteq A$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and the fact that its image is all of $\Spec A$ means that $\mathfrak{a}$ is contained in every prime ideal of $A$, i.e.,

$$\mathfrak{a}\subseteq \mathfrak{N}(A)=(0).$$

The last equality comes from the fact that $A$ is a domain. Therefore $Z \rightarrow \Spec A$ is an isomorphism, which means that $h$ factors through $\Delta$, i.e., $h=\Delta\circ g$ for some $g:\Spec A \rightarrow X$. Then

$$g_1=p_1\circ h=p_1\circ \Delta\circ g=g,\qquad g_2=p_2\circ h=p_2\circ\Delta\circ g=g$$

so $g_1=g_2$. In this direction the assumption that $X$ is Noetherian is not used.

Conversely, assume that for every square there is at most one lifting. By [Proposition 4](#prop4) it suffices to show that $\Delta(X)$ is a closed subset of $X\times_YX$.

First we observe that every point of $\cl(\Delta(X))$ is a specialization of some point of $\Delta(X)$. Since $X$ is a Noetherian scheme, it is also Noetherian as a topological space ([§The Topological Structure of Schemes, ⁋Definition 14](/en/math/scheme_theory/topology_of_schemes#def14)), and thus has finitely many irreducible components $X_1,\ldots, X_r$. ([[Topology] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13)) Each $X_i$ is an irreducible closed subset, so it has a generic point $\eta_i$ ([§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)), and $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$. Now since $\Delta$ is continuous, $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$ and the right-hand side is a finite union hence closed; conversely each $\Delta(\eta_i)$ lies in $\Delta(X)$, so we obtain

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\}).$$

That is, every point of $\cl(\Delta(X))$ is a specialization of some $\Delta(\eta_i)\in \Delta(X)$. ([§The Topological Structure of Schemes, ⁋Definition 2](/en/math/scheme_theory/topology_of_schemes#def2)) Therefore, if we show that $\Delta(X)$ is closed under specialization, then $\Delta(X)=\cl(\Delta(X))$ and the proof is finished.

Let $\xi=\Delta(x)\in \Delta(X)$ and $\eta\in\cl(\{\xi\})$. Giving the closed set $T=\cl(\{\xi\})$ a reduced scheme structure ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)), $T$ is an integral scheme with generic point $\xi$. Choose an affine open subset $\Spec B\subseteq T$ containing $\eta$. Since the generic point belongs to every nonempty open set, $\Spec B$ also contains $\xi$, and $B$ is a domain and $\xi$ corresponds to the zero ideal of $B$, so

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

where $\mathfrak{q}$ is the prime ideal corresponding to $\eta$. In particular $\mathcal{O}$ is a local domain with $\Frac(\mathcal{O})=K$. Choosing a valuation ring $A$ of $K$ dominating $\mathcal{O}$ by the existence theorem quoted above, the local homomorphism $\mathcal{O} \rightarrow A$ induces a morphism

$$q:\Spec A \longrightarrow \Spec \mathcal{O} \longrightarrow T \hookrightarrow X\times_YX$$

which sends the generic point $(0)$ of $\Spec A$ to $\xi$ and the closed point $\mathfrak{m}_A$ to $\eta$.

Now set $g_1=p_1\circ q$, $g_2=p_2\circ q$, and since $f\circ p_1=f\circ p_2$ we have a well-defined $w=f\circ g_1=f\circ g_2:\Spec A \rightarrow Y$. As seen in the proof of [Proposition 4](#prop4), choosing an affine open neighborhood $U$ of $x$ and an affine open subset $V$ of $Y$ containing $f(U)$, we have that $U\times_VU$ is an open neighborhood of $\xi$ in $X\times_YX$ and on it $\Delta$ is a closed embedding ([Lemma 5](#lem5)), so the map on stalks $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$ is surjective and therefore $\kappa(\xi) \rightarrow \kappa(x)$ is also surjective. On the other hand $p_1\circ\Delta=\id_X$, so the composition $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$ is the identity, and thus the two maps are inverse isomorphisms of each other. Hence $K=\kappa(\xi)\cong\kappa(x)$. Under this identification, let $u:\Spec K \rightarrow X$ be the canonical morphism defined by the point $x$ and $\kappa(x)\cong K$; then $\Delta\circ u$ is the canonical morphism defined by the point $\xi$ and $\kappa(\xi)\cong K$, and this equals $q\circ j$. Indeed, $q\circ j$ has image $\xi$ and induces the identity on $K$ on residue fields because $\kappa(\xi)=\Frac(\mathcal{O})=K$. Therefore

$$g_1\circ j=p_1\circ q\circ j=p_1\circ \Delta\circ u=u,\qquad g_2\circ j=p_2\circ q\circ j=p_2\circ\Delta\circ u=u$$

and $f\circ g_1=f\circ g_2=w$, so $g_1$ and $g_2$ are two liftings of the square given by $u$ and $w$. By assumption $g_1=g_2$, and then $\Delta\circ g_1$ and $q$ give $g_1$ and $g_2=g_1$ respectively when composed with $p_1$, $p_2$, so by the universal property of the fiber product $q=\Delta\circ g_1$. Therefore

$$\eta=q(\mathfrak{m}_A)=\Delta(g_1(\mathfrak{m}_A))\in \Delta(X)$$

and $\Delta(X)$ is closed under specialization. Combined with the previous observation, $\Delta(X)=\cl(\Delta(X))$, so $\Delta(X)$ is a closed set, and by [Proposition 4](#prop4) $f$ is separated.
:::

On the other hand, if $Y$ is Noetherian and $f$ is a finite type morphism, then in the above theorem one may replace arbitrary valuation rings by arbitrary discrete valuation rings. This requires a limit argument handling an arbitrary valuation ring by Noetherian approximation and lies beyond the scope of this post, so we accept the fact without proof and defer it to **[Stacks]**. The $\Spec$ of a general valuation ring has its prime ideals forming a longer chain and so escapes the two-point picture of [Example 2](#ex2), but once we pass to discrete valuation rings that picture survives intact and the theorem can be read in terms of curve germs. That is, the theorem above says that given a way of placing the punctured germ $\Spec K$ inside $X$, there is at most one way of filling it up to the whole germ $\Spec A$.

Let us confirm this picture in practice.

::: Example 7
We confirmed earlier with [Proposition 4](#prop4) that the line with double origin $X$ is not separated, but with [Theorem 6](#thm6) the same fact appears directly in the language of limits of curves. The ring $A=\mathbb{K}[t]_{(t)}$ is a discrete valuation ring with uniformizer $t$ and $K=\Frac(A)=\mathbb{K}(t)$, and we set $Y=\Spec\mathbb{K}$. Consider the morphism $u:\Spec K \rightarrow X$ defined by the ring homomorphism $\mathbb{K}[\x_0] \rightarrow K$, $\x_0\mapsto t$. Since $t$ is a unit of $K$, the image of $u$ lies in the open subset where the two charts overlap. As everything lies over $\mathbb{K}$, the morphism $u$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form an outer square.

Now the two morphisms into the charts $X_0=\Spec\mathbb{K}[\x_0]$ and $X_1=\Spec\mathbb{K}[\x_1]$

$$g_0:\Spec A \longrightarrow X_0\subseteq X,\qquad g_1:\Spec A \longrightarrow X_1\subseteq X$$

defined by $\x_0\mapsto t$ and $\x_1\mapsto t$ respectively are both well defined since $t\in A$. The two charts were glued by identifying $\x_0$ and $\x_1$ away from the origin, so $g_0\circ j=g_1\circ j=u$ and hence both are liftings of this square. However $g_0$ sends $\mathfrak{m}_A=(t)$ to the origin $0_1$ of the first chart while $g_1$ sends it to the origin $0_2$ of the second, so $g_0\neq g_1$. That is, the punctured curve germ has two limits, and this is why $X$ fails to be separated.
:::

On the other hand, from [Theorem 6](#thm6) we obtain the following.

::: Corollary 8
For Noetherian schemes,

1. Open immersions and closed embeddings are both separated.
2. The composition of two separated morphisms is separated.
3. Separated morphisms are preserved under base change.
4. Separated morphisms are preserved under fiber products.
5. If $f:X \rightarrow Y$, $g:Y \rightarrow Z$ are scheme morphisms and $g\circ f$ is a separated morphism, then $f$ is also a separated morphism.
:::
::: Proof
Item 1 is checked directly from the definition. If $f$ is a closed embedding, then for each affine open subset $V=\Spec B$ of $Y$ we have $f^{-1}(V)=\Spec A$ with $B \rightarrow A$ surjective ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and collecting all such $V$ the sets $f^{-1}(V)\times_Vf^{-1}(V)$ cover $X\times_YX$. On each of them $\Delta$ is a closed embedding by the computation of [Lemma 5](#lem5), and since being a closed embedding is affine-local on the target, $\Delta$ itself is a closed embedding. If $f$ is an open immersion, regard $X$ as an open subscheme of $Y$ and consider the affine open subsets $V=\Spec B$ of $Y$ together with the basic open subsets $\Spec B_b$ of $X$ contained in them. Then the sets $\Spec B_b\times_V\Spec B_{b'}$ cover $X\times_YX$, and since

$$B_b\otimes_BB_{b'}\cong B_{bb'}=\mathcal{O}(\Spec B_b\cap \Spec B_{b'})$$

$\Delta$ is an isomorphism on each of them, in particular a closed embedding.

The rest follows from the criterion of [Theorem 6](#thm6); we only have to check that uniqueness of liftings is inherited.

For item 2, let an outer square $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Z$ for $g\circ f$ and two liftings $h_1,h_2:\Spec A \rightarrow X$ be given. Then $f\circ h_1$ and $f\circ h_2$ are two liftings of the square for $g$ given by $u'=f\circ u$ and $v$, so $f\circ h_1=f\circ h_2$; and then $h_1,h_2$ are two liftings of the square for $f$ given by $u$ and $f\circ h_1$, so $h_1=h_2$.

For item 3, let $Y' \rightarrow Y$, $X'=X\times_YY'$ and $f':X' \rightarrow Y'$ be given, together with a square for $f'$ and two liftings $g_1',g_2':\Spec A \rightarrow X'$. Composing them with $X' \rightarrow X$ yields two liftings of a square for $f$, hence they agree; the two composites to $Y'$ are also the same morphism given by the square, so $g_1'=g_2'$ by the uniqueness in the universal property of the fiber product.

For item 5, given a square for $f$ and two liftings $g_1,g_2$, composing $\Spec A \rightarrow Y$ with $g$ produces a square for $g\circ f$ of which $g_1,g_2$ are two liftings, so $g_1=g_2$.

Finally, for item 4, given separated morphisms $f:X \rightarrow Y$ and $f':X' \rightarrow Y'$ of $S$-schemes, $f\times f'$ factors as the composition

$$X\times_SX' \longrightarrow Y\times_SX' \longrightarrow Y\times_SY'$$

whose two morphisms are base changes of $f$ and $f'$ respectively, so the claim follows from items 3 and 2.
:::

In particular, combining items 2 and 5 shows that when $Y$ is a separated scheme, a $Y$-scheme $X$ is a separated scheme if and only if its structure morphism $X \rightarrow Y$ is separated. Affine schemes are always separated schemes by [Lemma 5](#lem5), so for instance separatedness of a scheme over an affine scheme can be decided by looking at the structure morphism alone.

## Proper Morphisms

We now turn to the property corresponding to compactness. In topology we saw that compactness can be rephrased as the condition of being universally closed ([[Topology] §Proper Maps, ⁋Theorem 6](/en/math/topology/proper_maps#thm6)), and in algebraic geometry this condition, with products replaced by fiber products, becomes the definition itself.

::: Definition 9
A morphism $f:X \rightarrow Y$ is called *universally closed* if $f$ is a closed map and for every $Y' \rightarrow Y$, the map $X\times_Y Y' \rightarrow Y'$ is also closed. A finite type morphism that is separated and universally closed is called a *proper morphism*.
:::

Setting $Y'=Y$ makes the second condition contain the first, so the substantive condition is the single requirement that every base change be a closed map. On the other hand, since we work in the category of Noetherian schemes throughout this section, when verifying universal closedness we shall only consider base changes $Y' \rightarrow Y$ along Noetherian schemes. That the condition for an arbitrary $Y'$ follows from this is obtained by restricting $Y'$ to an affine scheme and writing its coordinate ring as a filtered colimit of finitely generated subalgebras; this limit argument lies beyond the scope of this post, so we defer it to **[Stacks]**.

A proper morphism demands the separated condition and the universally closed condition together, so the criterion likewise splits into two pieces. [Theorem 6](#thm6) decided separatedness by the uniqueness of liftings, so what remains is that the existence of liftings decides universal closedness.

::: Proposition 10
For a finite type scheme morphism $f:X \rightarrow Y$ between Noetherian schemes, the following are equivalent: $f$ is universally closed; and for every valuation ring $A$ and its quotient field $K=\Frac(A)$, given any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.27em" alt="valuative_criterion" %}

with the outer square given, there exists at least one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
As in the proof of [Theorem 6](#thm6), we write the outer square as $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$, $j:\Spec K \rightarrow \Spec A$, and continue to use the two standard facts cited in that proof. Namely, every local subring in a field $K$ is dominated by a valuation ring $A$ with $\Frac(A)=K$, and a morphism $\Spec K \rightarrow X$ is the same as a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. To this we add the following maximality of valuation rings. If a local subring $\mathcal{O}\subseteq K$ is given that dominates a valuation ring $A$ of $K$, then $\mathcal{O}=A$. Indeed, if $c\in\mathcal{O}$ is nonzero and $c\notin A$, then by the definition of a valuation ring $c^{-1}\in A$, and since $c\notin A$, $c^{-1}$ is not a unit of $A$. Hence $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$, but $c\in\mathcal{O}$ so $c^{-1}$ is a unit of $\mathcal{O}$, a contradiction. Therefore $\mathcal{O}\subseteq A$, and by the definition of domination $A\subseteq\mathcal{O}$, so $\mathcal{O}=A$.

First assume $f$ is universally closed and let us construct a lifting. Base changing along $v$, we obtain $X_A=X\times_Y\Spec A$ and the projection $\pi:X_A \rightarrow \Spec A$, which is a closed map. ([Definition 9](#def9)) On the other hand, $u$ and $j$ induce by the universal property of the fiber product a morphism $\tilde{u}:\Spec K \rightarrow X_A$ over $\Spec A$, and finding an extension of $\tilde{u}$ to a section of $\pi$ of the form $\Spec A \rightarrow X_A$ and projecting it to $X$ gives the desired lifting.

Let $\xi\in X_A$ be a point in the image of $\tilde{u}$ and give $Z=\cl(\{\xi\})$ a reduced scheme structure. ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)) Since $\pi\circ\tilde{u}=j$, $\pi(\xi)$ is the generic point $(0)$ of $\Spec A$, and since $\pi$ is a closed map, $\pi(Z)$ is a closed set containing $(0)$, hence all of $\Spec A$. Therefore there exists $z\in Z$ with $\pi(z)=\mathfrak{m}_A$.

Let us examine the residue fields. The map $\kappa((0))=K \rightarrow K$ induced by $\pi\circ \tilde{u}=j$ at $(0)$ is the identity, and this is the composition of the map $K\rightarrow\kappa(\xi)$ induced by $\pi$ and the map $\kappa(\xi) \rightarrow K$ induced by $\tilde{u}$, so the two maps are inverse isomorphisms of each other. Hence $\kappa(\xi)\cong K$. Then since $Z$ is an integral scheme with generic point $\xi$, as in the proof of [Theorem 6](#thm6) we choose an affine open subset containing $z$ and know that

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K.$$

Also the map $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$ induced by $\pi\vert_Z$ is a local homomorphism, and since the map $K \rightarrow \kappa(\xi)=K$ it induces at the generic point is the identity, this map is an inclusion of subrings of $K$. That is, $\mathcal{O}$ is a local subring of $K$ dominating $A$, and by the maximality above we have $\mathcal{O}_{Z,z}=A$.

Then we obtain the canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$, and its composition with $\pi$ corresponds to the identity on $A$ at the ring level, so it is a section of $\pi$. The restriction of this section to $\Spec K$ has image $\xi$ and induces the identity on $K$ on residue fields because $\kappa(\xi)=K$, so it equals $\tilde{u}$. Therefore projecting this section to $X$ gives $g:\Spec A \rightarrow X$ with $g\circ j=u$ and $f\circ g=v$.

Conversely, assume the existence part holds. Following the convention stated after [Definition 9](#def9), we consider only base changes $Y' \rightarrow Y$ along Noetherian schemes.

First, the existence part is stable under base change. Suppose $Y' \rightarrow Y$ and $X'=X\times_YY'$, $f':X' \rightarrow Y'$ are given, and $\Spec K \rightarrow X'$ and $\Spec A \rightarrow Y'$ form an outer square for $f'$. Composing these with $X' \rightarrow X$, $Y' \rightarrow Y$ gives an outer square for $f$, so there is a lifting $g:\Spec A \rightarrow X$, and $g$ and $\Spec A \rightarrow Y'$ give a unique $g':\Spec A \rightarrow X'$ by the universal property. $g'\circ j$ and the given $\Spec K \rightarrow X'$ are equal because they give the same result when composed with $X' \rightarrow X$ and $X' \rightarrow Y'$, so $g'$ is a lifting for $f'$. On the other hand, finite type morphisms are stable under base change and a finite type scheme over a Noetherian scheme is again Noetherian, so $X'$ is Noetherian and $f'$ is of finite type. Therefore, if we show that $f$ is a closed map whenever a Noetherian scheme $X$ and a finite type morphism $f:X \rightarrow Y$ satisfy the existence part of the criterion, then applying this to all base changes finishes the proof.

To show this, choose a closed subset $T$ of $X$ and give it a reduced scheme structure. The closed embedding $T\hookrightarrow X$ is a finite morphism, so ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)) it is of finite type, and thus $T$ is a Noetherian scheme and $f\vert_T:T \rightarrow Y$ is also of finite type. Moreover $f\vert_T$ inherits the existence part of the criterion. Indeed, if $\Spec K \rightarrow T$ and $\Spec A \rightarrow Y$ form a square for $f\vert_T$, applying the criterion to $\Spec K \rightarrow T\hookrightarrow X$ gives a lifting $g_0:\Spec A \rightarrow X$. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so $g_0(\Spec A)\subseteq \cl(\{g_0((0))\})\subseteq T$, and since $\Spec A$ is reduced, $g_0$ factors through $T$. The last fact is obtained as follows. Suppose the image of a morphism $\varphi:S \rightarrow X$ from a reduced scheme $S$ lies in a closed subset $T$, and choose an affine open subset $\Spec B$ of $X$ and an affine open subset $\Spec R$ of $\varphi^{-1}(\Spec B)$. If $T\cap \Spec B=Z(\mathfrak{b})$ ($\mathfrak{b}$ a radical ideal), then the reduced structure of $T$ is $\Spec (B/\mathfrak{b})$ on it, and the corresponding ring homomorphism $\psi:B \rightarrow R$ satisfies $\mathfrak{b}\subseteq \psi^{-1}(\mathfrak{p})$ for every prime ideal $\mathfrak{p}\subseteq R$, so

$$\psi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\mathfrak{N}(R)=(0).$$

That is, $\psi$ uniquely factors through $B/\mathfrak{b}$, and these local factorizations glue by uniqueness.

Therefore it suffices to show that $f(T)=f\vert_T(T)$ is a closed set, and ultimately it is enough to show that the image $f(X)$ of a finite type morphism $f:X \rightarrow Y$ (with $X$ Noetherian) satisfying the existence part of the criterion is closed.

First we show that $f(X)$ is closed under specialization. Let $y_1=f(x_1)\in f(X)$ and $y_0\in\cl(\{y_1\})$. Giving $W=\cl(\{y_1\})$ a reduced scheme structure, $W$ is an integral scheme with generic point $y_1$, and as before $\mathcal{O}=\mathcal{O}_{W,y_0}$ is a local domain with $\Frac(\mathcal{O})=\kappa(y_1)$. Now set $K=\kappa(x_1)$ and view $\mathcal{O}$ as a local subring of $K$ via the field homomorphism $\kappa(y_1)\hookrightarrow K$ induced by $f$. Then there exists a valuation ring $A$ of $K$ dominating $\mathcal{O}$, and from this we obtain two morphisms

$$\Spec A \longrightarrow \Spec\mathcal{O} \longrightarrow W\hookrightarrow Y,\qquad u:\Spec K \longrightarrow X$$

where $u$ is the canonical morphism defined by the point $x_1$ and $\kappa(x_1)=K$. These form an outer square because the two compositions $\Spec K \rightarrow Y$ are both the canonical morphism defined by the point $y_1$ and the field homomorphism $\kappa(y_1)\hookrightarrow K$. By the existence part of the criterion there is a lifting $g_0:\Spec A \rightarrow X$, and since $\Spec A \rightarrow \Spec\mathcal{O}$ comes from a local homomorphism, $\mathfrak{m}_A$ maps to $\mathfrak{m}_\mathcal{O}$, i.e., to $y_0$. Therefore $f(g_0(\mathfrak{m}_A))=y_0$ and $y_0\in f(X)$.

Finally we repeat the topological observation from the proof of [Theorem 6](#thm6) verbatim. If $\eta_1,\ldots,\eta_r$ are the generic points of the irreducible components $X_1,\ldots,X_r$ of $X$, then $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$, so

$$\cl(f(X))=\bigcup_{i=1}^r\cl(\{f(\eta_i)\})$$

and thus every point of $\cl(f(X))$ is a specialization of a point of $f(X)$. Since we showed above that $f(X)$ is closed under specialization, we have $f(X)=\cl(f(X))$.
:::

Combining the two pieces then yields the criterion for properness.

::: Theorem 11
For a finite type scheme morphism $f:X \rightarrow Y$ between Noetherian schemes, the following are equivalent: $f$ is proper; and for every valuation ring $A$ and its quotient field $K=\Frac(A)$, given any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.27em" alt="valuative_criterion" %}

with the outer square given, there exists exactly one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
Since $f$ is assumed to be of finite type, by [Definition 9](#def9) $f$ is proper if and only if $f$ is separated and universally closed. By [Theorem 6](#thm6), $f$ is separated if and only if every outer square admits at most one lifting, and by [Proposition 10](#prop10), $f$ is universally closed if and only if every outer square admits at least one lifting. The two conditions holding together is exactly the statement that every square admits exactly one lifting.
:::

It is worth seeing the criterion fail. [Example 7](#ex7) was a case where uniqueness breaks; the following is a case where existence breaks.

::: Example 12
The scheme $\mathbb{A}^1_\mathbb{K}=\Spec\mathbb{K}[\x]$ is not proper over $\Spec\mathbb{K}$. Take $A=\mathbb{K}[t]_{(t)}$ and $K=\Frac(A)=\mathbb{K}(t)$, and consider the morphism $u:\Spec K \rightarrow \mathbb{A}^1_\mathbb{K}$ defined by the ring homomorphism

$$\mathbb{K}[\x] \longrightarrow K;\qquad \x\mapsto 1/t$$

As everything lies over $\mathbb{K}$, the morphism $u$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form an outer square. If a lifting $g:\Spec A \rightarrow \mathbb{A}^1_\mathbb{K}$ existed, it would correspond to a ring homomorphism $\mathbb{K}[\x] \rightarrow A$, and the condition $g\circ j=u$ says that composing it with $A\hookrightarrow K$ sends $\x$ to $1/t$. That is, we would need $1/t\in A$, which is impossible since $t$ is a uniformizer of $A$. Hence no lifting exists, and by [Theorem 11](#thm11) the morphism $\mathbb{A}^1_\mathbb{K} \rightarrow \Spec\mathbb{K}$ is not proper.

Geometrically this $u$ is a curve germ running off to infinity at the origin, and the criterion simply reads off that $\mathbb{A}^1_\mathbb{K}$ contains no limit for it. Carrying out the same computation on $\mathbb{P}^1_\mathbb{K}$, the element $1/t$ becomes $t$ in the chart corresponding to infinity and a lifting does exist; this is generalized in [Theorem 15](#thm15).
:::

Similarly, the following corollary holds.

::: Corollary 13
For Noetherian schemes,

1. A closed embedding is proper.
2. The composition of proper morphisms is proper.
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber products.
5. If $f:X \rightarrow Y$, $g:Y \rightarrow Z$ are scheme morphisms, $g$ is separated and $g\circ f$ is a proper morphism, then $f$ is also a proper morphism.
:::
::: Proof
For item 1, a closed embedding is separated by item 1 of [Corollary 8](#cor8), and it is a finite morphism ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)) hence of finite type. Moreover a closed embedding is a closed map and is stable under base change (see the proof of [Theorem 6](#thm6)), so it is universally closed.

For item 2, separatedness is item 2 of [Corollary 8](#cor8) and the composition of finite type morphisms is of finite type, so only universal closedness remains. Given $Z' \rightarrow Z$, we have $X\times_ZZ'=X\times_Y(Y\times_ZZ')$, so the two morphisms in

$$X\times_ZZ' \longrightarrow Y\times_ZZ' \longrightarrow Z'$$

are base changes of $f$ and $g$ respectively and hence both closed maps. The composition of closed maps is a closed map, so $X\times_ZZ' \rightarrow Z'$ is also closed.

For item 3, separatedness is item 3 of [Corollary 8](#cor8), finite type is stable under base change, and universal closedness follows immediately from the definition since a base change of a base change is again a base change. Item 4 then follows by applying the same factorization as in item 4 of [Corollary 8](#cor8) to items 2 and 3.

Finally we prove item 5. Consider the graph morphism $\Gamma_f:X \rightarrow X\times_ZY$ induced by $\id_X$ and $f$, so that $f=p_2\circ\Gamma_f$. The square formed by $\Gamma_f$ and $f\times\id_Y: X\times_ZY \rightarrow Y\times_ZY$ is cartesian with $\Delta_{Y/Z}:Y \rightarrow Y\times_ZY$ as its base. Indeed, for an arbitrary $T$, matching the two morphisms to $Y\times_ZY$ amounts to choosing among pairs $a:T \rightarrow X$ and $b:T \rightarrow Y$ those with $f\circ a=b$, and such a pair is determined by $a$ alone. Then the assumption that $g$ is separated makes $\Delta_{Y/Z}$ a closed embedding, so $\Gamma_f$ is a closed embedding as well, and it is proper by item 1. On the other hand $p_2:X\times_ZY \rightarrow Y$ is the base change of $g\circ f$ along $g$, hence proper by item 3. Therefore $f=p_2\circ\Gamma_f$ is proper by item 2.
:::

The hypothesis that $g$ be separated in item 5 is there because the reason $\Gamma_f$ is a closed embedding in the proof is precisely that $\Delta_{Y/Z}$ is one. Without this hypothesis $\Gamma_f$ is merely an immersion and the argument breaks down. Item 5 of [Corollary 8](#cor8) needed no such hypothesis, so one must note that the two items have different shapes.

On the other hand, item 1 of [Corollary 13](#cor13) is a special case of the following. This is the most typical illustration of how the criterion is actually used: existence comes out of the single fact that a valuation ring is integrally closed.

::: Corollary 14
A finite morphism between Noetherian schemes is proper.
:::
::: Proof
A finite morphism $f:X \rightarrow Y$ is an affine morphism, so $f^{-1}(V)$ is affine for every affine open subset $V\subseteq Y$, and hence $f$ is separated by [Lemma 5](#lem5) together with the affine-local criterion for closed embeddings ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)). Moreover a finite morphism is of finite type. ([§Properties of Scheme Morphisms, ⁋Proposition 15](/en/math/scheme_theory/properties_of_scheme_morphisms#prop15)) Therefore by [Theorem 11](#thm11) we only need to verify the existence of liftings.

Suppose an outer square $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$ is given. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so choosing an affine open subset $V=\Spec B$ of $Y$ containing $v(\mathfrak{m}_A)$, this $V$ also contains $v((0))$ and hence $v$ factors through $V$. Then the image of $u$ lies in $f^{-1}(V)=\Spec C$, where $C$ is finitely generated as a $B$-module. The problem is now to produce a ring homomorphism $C \rightarrow A$ compatible with the given

$$B \longrightarrow A,\qquad C \longrightarrow K$$

Every $c\in C$ is integral over $B$, so it satisfies

$$c^n+b_{n-1}c^{n-1}+\cdots+b_0=0$$

for suitable $b_i\in B$. Transporting this relation along $C \rightarrow K$, the image of $c$ is integral over the image of $B$, and since the image of $B$ lies in $A$, the image of $c$ is integral over $A$. But a valuation ring is always integrally closed ([[Commutative Algebra] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6), item 2), so the image of $c$ lies in $A$. That is, $C \rightarrow K$ factors through $A$, and this gives the desired lifting.
:::

::: Theorem 15
A projective morphism between Noetherian schemes is a proper morphism, and a quasi-projective morphism is a separated, finite type morphism.
:::
::: Proof
The heart of the proof is that $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ is proper, which is obtained by directly verifying the criterion of [Theorem 11](#thm11). First, $\mathbb{P}^n_\mathbb{Z}$ is obtained by gluing $n+1$ affine charts

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

along $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$. Here $\x_i/\x_i=1$, so each $U_i$ is the spectrum of an $n$-variable polynomial ring over $\mathbb{Z}$. In particular each $U_i$ is the spectrum of a Noetherian ring, and since there are finitely many charts, $\mathbb{P}^n_\mathbb{Z}$ is a Noetherian scheme, and $\pi$ is of finite type. ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14))

That $\pi$ is separated is checked directly on the charts. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$ is covered by affine open subsets $U_i\times_\mathbb{Z}U_j$ and since $p_1\circ\Delta=p_2\circ\Delta=\id$, we have $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$. Now looking at the ring homomorphism induced by $\Delta$ on this,

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \longrightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

the right-hand side is generated over $\mathbb{Z}$ by the $\x_l/\x_i$ and $(\x_j/\x_i)^{-1}=\x_i/\x_j$; the former come from the first factor and the latter from the second, so this map is surjective. Therefore $\Delta$ is a closed embedding on each $U_i\times_\mathbb{Z}U_j$, and since closed embeddings are affine-local on the target ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), $\Delta$ itself is a closed embedding.

Since $\Spec \mathbb{Z}$ is a terminal object in the category of schemes, giving the outer square for a valuation ring $A$ and $K=\Frac(A)$ is the same as giving a morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$. The uniqueness of the lifting follows from $\pi$ being separated and [Theorem 6](#thm6), so we only need to show existence. Since $\Spec K$ is a single point, the image of the given morphism lies in some chart $U_i$, and thus this morphism corresponds to a ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \longrightarrow K.$$

Let the image of $\x_j/\x_i$ be $a_j\in K$; then $a_i=1$. Now define $s\preceq t$ on $K^\times$ by $t/s\in A$; then by the definition of a valuation ring, for any $s,t$ either $s\preceq t$ or $t\preceq s$, and if $t/s\in A$ and $r/t\in A$ then $r/s=(r/t)(t/s)\in A$, so $\preceq$ is a total preorder on $K^\times$. Since $a_i=1\neq 0$, the finite set $\{a_j \mid a_j\neq 0\}$ is nonempty, and thus we can choose a minimal element $a_k$ of this set. That is, for every $j$

$$b_j:=a_j/a_k\in A.$$

(If $a_j=0$, then $b_j=0\in A$.) In particular $b_k=1$, so the ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \longrightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

is defined and gives a morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$. To show that this is a lifting, it suffices to check that its composition with $A\hookrightarrow K$ equals the originally given morphism. Since $a_k\neq 0$, the original ring homomorphism sends $\x_k/\x_i$ to the unit $a_k$ of $K$, and thus the image of the original morphism lies in $D(\x_k/\x_i)=U_i\cap U_k$. Then on $U_k$ this morphism is given by $\x_j/\x_k\mapsto a_j/a_k=b_j$ via the transition relation

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1},$$

so it exactly equals the restriction to $\Spec K$ of the $\Spec A \rightarrow U_k$ constructed above. Hence the existence part of the criterion holds, and by [Theorem 11](#thm11) $\pi$ is proper.

For any Noetherian scheme $Y$, we have $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$. This is because when $Y=\Spec B$, the chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$ of $\mathbb{P}^n_B$ coincides with $U_i\times_{\Spec\mathbb{Z}}\Spec B$, and for general $Y$ we glue these. Therefore by [Corollary 13](#cor13) $\mathbb{P}^n_Y \rightarrow Y$ is proper, and in particular of finite type, so $\mathbb{P}^n_Y$ is a Noetherian scheme.

Now if $f:X \rightarrow Y$ is projective, then $f$ is the composition of a closed embedding $X\hookrightarrow \mathbb{P}^n_Y$ and the projection $\mathbb{P}^n_Y \rightarrow Y$. ([Definition 1](#def1)) Closed embeddings are proper and the composition of two proper morphisms is proper ([Corollary 13](#cor13)), so $f$ is proper.

Finally, suppose $f:X \rightarrow Y$ is quasi-projective, and factor it as a composition $f=g\circ\iota$ of an open immersion $\iota: X \rightarrow X'$ and a projective morphism $g:X' \rightarrow Y$. ([Definition 1](#def1)) By what we just showed, $g$ is proper, hence separated and of finite type. On the other hand, open immersions are separated and the composition of two separated morphisms is separated ([Corollary 8](#cor8)), so $f$ is separated. Also an open immersion is locally of finite type, and since $X$ is Noetherian, the preimage of any affine open subset of $X'$ under $\iota$ is quasi-compact as an open subset of a Noetherian space. That is, $\iota$ is of finite type ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14)), and the composition of two finite type morphisms is of finite type, so $f$ is also of finite type.
:::

This yields the classical consequence of the criterion. A proper morphism is by definition a closed map, so the image of a morphism out of a projective scheme is always closed.

::: Corollary 16
For a projective scheme $X$ over $\mathbb{K}$, a separated finite type $\mathbb{K}$-scheme $Z$, and a $\mathbb{K}$-morphism $\varphi:X \rightarrow Z$, the image $\varphi(X)$ is a closed subset of $Z$.
:::
::: Proof
The structure morphism $X \rightarrow \Spec\mathbb{K}$ is projective, hence proper by [Theorem 15](#thm15), and $Z \rightarrow \Spec\mathbb{K}$ is separated by assumption. Applying item 5 of [Corollary 13](#cor13) to $\varphi$ and $Z \rightarrow \Spec\mathbb{K}$ shows that $\varphi$ is proper, and in particular $\varphi$ is a closed map, so $\varphi(X)$ is closed since $X$ is a closed subset of itself.
:::

This is why in classical algebraic geometry a projective variety is called *complete*, and it is also the geometric form of elimination theory. Contrasting with [Example 12](#ex12), the statement fails on $\mathbb{A}^1_\mathbb{K}$: projecting the hyperbola $Z(\x\y-1)$ in $\mathbb{A}^2_\mathbb{K}$ onto the first coordinate has image $\mathbb{A}^1_\mathbb{K}\setminus\{0\}$, which is not closed.

Finally, let us note why these criteria are called *valuative*. The name valuation ring itself comes from its being the ring of elements on which a valuation $\nu:K^\times \rightarrow G$ takes nonnegative values ([[Commutative Algebra] §Regular Local Rings, ⁋Definition 7](/en/math/commutative_algebra/regular_local_rings#def7)), and as seen in [Example 2](#ex2) the generic point and the closed point of $\Spec A$ correspond respectively to the locus where $\nu$ vanishes and the locus where $\nu>0$. Thus finding a lifting $\Spec A \rightarrow X$ means finding a point of $X$ that serves as the center of the valuation $\nu$, and the criteria translate the uniqueness and the existence of such a center into separatedness and universal closedness respectively.

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison-Wesley, 1969.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).
