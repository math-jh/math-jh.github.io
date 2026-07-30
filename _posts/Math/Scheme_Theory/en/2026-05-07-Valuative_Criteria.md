---
title: "Valuation Rings"
description: "We define separated and proper morphisms, and examine how they generalize the Hausdorff and compactness conditions from topology into algebraic geometry. The structure of discrete valuation rings is also discussed."
excerpt: "Valuative criteria for separated and proper morphisms"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-en"

date: 2024-05-24
weight: 15
translated_at: 2026-07-27T19:45:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T19:45:02+00:00
---
In this post we define separated morphisms and proper morphisms. In previous posts we defined open subschemes ([§Schemes, ⁋Definition 4](/en/math/scheme_theory/schemes#def4)), examined closed embeddings, the closed subschemes obtained from them, and ideal sheaves ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2), [Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5)). We now add the following concepts.

::: Definition 1
Let a scheme morphism $\varphi: X \rightarrow Y$ be given.

1. If $\varphi$ induces an isomorphism between open subschemes of $X$ and $Y$, we call $\varphi$ an *open immersion*.
2. We say $\varphi$ is *projective* if for some suitable $n$, $\varphi$ can be factored as a composition of a closed embedding and a projection $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$. ([§Projective Schemes](/en/math/scheme_theory/projective_schemes))
3. We say $\varphi$ is *quasi-projective* if it can be factored as a composition of a suitable open immersion $X \rightarrow X'$ and a projective morphism $X' \rightarrow Y$.
:::

The first definition is obvious; the second and third are relative versions—that is, in $\Sch_{/Y}$—of [\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3) and [\[Algebraic Varieties\] §Quasi-Projective Varieties, ⁋Definition 1](/en/math/algebraic_varieties/quasi_projective_varieties#def1).

Before beginning the main story, it is worth examining the following example.

::: Example 2
Let $A$ be a discrete valuation ring that is a subring of a field $K$. That is, for any $x\in K^\times$ either $x\in A$ or $x^{-1}\in A$, and $A$ is Noetherian with maximal ideal $\mathfrak{m}$ principal. ([\[Commutative Algebra\] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5)) Since any $x\in K^\times$ is represented as a ratio of elements of $A$ via $x$ or $x^{-1}$, we have $K=\Frac(A)$. Also $A$ is a local ring with $\mathfrak{m}$ as its unique maximal ideal ([\[Commutative Algebra\] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6)), and choosing a uniformizer $\pi$, any $f\in K^\times$ is uniquely expressed as $f=\pi^nu$ for some integer $n$ and unit $u$ ([\[Commutative Algebra\] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8)); hence every nonzero ideal of $A$ is of the form $(\pi^n)$. In particular $A$ is a principal ideal domain, and its only prime ideals are $(0)$ and $\mathfrak{m}=(\pi)$.

Hence $\Spec A$ consists of the two points $(0)$ and $\mathfrak{m}$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $\Spec A$ is

$$D(\pi)=\Spec A\setminus Z(\mathfrak{m})=\{(0)\}.$$

Then by [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6),

$$\mathcal{O}(D(\pi))\cong A_\pi\cong K.$$

Of course $\mathcal{O}(\Spec A)\cong A$.

Meanwhile, the two points of $\Spec A$ can be examined geometrically through their residue fields. Using [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8),

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong K,\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

we obtain

$$\kappa((0))=K, \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong A/\mathfrak{m}.$$
:::

Let us examine the example a bit more geometrically. Since $Z((0))=\Spec A$, the closure of $(0)$ is all of $\Spec A$, so $(0)$ is the generic point of this space. This situation is especially visible when, for a curve $C$ and a point $p$ on it, $\mathcal{O}_{C,p}$ is a discrete valuation ring. Specifically, the stalk

$$\mathcal{O}_{C,p}=\varinjlim_{U\ni p} \mathcal{O}(U)$$

can be viewed as germs at the point $p$, and the generic point $(0)$ of $\Spec \mathcal{O}_{C,p}$ is precisely what contains this data. Then the remaining (unique) point $\mathfrak{m}$ corresponds exactly to the point $p$, and the fact that this is a specialization of $(0)$ reflects that in defining a germ we look at neighborhoods arbitrarily close to $p$.

In this picture, the role of $\Spec K$ is revealed by looking at the function side. Functions on $\Spec A$ are $A$ itself, i.e., germs regular at $p$, and elements of $K\cong A_\pi$—the functions on the only nontrivial open set $D(\pi)=\{(0)\}$—are those allowing negative order $n$ in the form $f=\pi^nu$. ([\[Commutative Algebra\] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8), item 2) That is, these are functions having a pole at $p$ but of finite order, i.e., functions regular on the entire neighborhood except at $p$ alone; thus $\Spec K$ is the space obtained from this germ by extracting the center $p$, losing the information of $p$ while retaining only information about neighborhoods of $p$, and the canonical morphism $\Spec K \rightarrow \Spec A$ is exactly the inclusion map defined by this picture.

Then a morphism $\Spec K \rightarrow X$ is a germ of a curve missing a point entering into $X$, and extending this to $\Spec A \rightarrow X$ is recovering the missing point inside $X$ and attaching the curve, i.e., finding the limit of the curve. That this extension exists in at most one way is separatedness, and that it exists in exactly one way is properness; this is the content of the two criteria we will see below. Topologically, this is the algebraic-geometric analogue of the facts that in a Hausdorff space a limit is unique ([\[Topology\] §Hausdorff Spaces, ⁋Proposition 4](/en/math/topology/Hausdorff_spaces#prop4)) and that in a compact space a limit always exists ([\[Topology\] §Compactness and Paracompactness, ⁋Lemma 1](/en/math/topology/compactness#lem1)).

## Separated Morphisms

As examined above, the idea of a separated morphism is that, given a germ of a curve, there is at most one way to fill in its center point $p$. To describe this, the following definition is needed.

::: Definition 3
For a scheme morphism $\varphi:X \rightarrow Y$, the unique morphism induced by two copies of $\id_X$ from the universal property of the fiber product, i.e., the dashed arrow $\Delta: X \rightarrow X \times_Y X$ in the following diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-1.svg width="13.58em" alt="diagonal_morphism" %}

is called the *diagonal morphism* of $\varphi$. ([§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1)) If $\Delta$ is a closed embedding, we call $\varphi$ *separated*, and say $X$ is *separated* over $Y$. If $X$ is separated over $\Spec \mathbb{Z}$, we simply call $X$ a *separated* scheme.
:::

When we need to clarify which morphism's diagonal it is, we write $\Delta_{X/Y}$ instead of $\Delta$. From the definition, for the two projections $p_1,p_2: X\times_YX \rightarrow X$, it is obvious that $p_1\circ\Delta=p_2\circ\Delta=\id_X$. Also, $\Delta$ is injective and the restriction of $p_1$ to $\Delta(X)$ gives a continuous inverse to $\Delta$, so $\Delta$ is always a homeomorphism onto $\Delta(X)$. Therefore asking whether $\Delta$ is a closed embedding amounts to asking whether $\Delta(X)$ is closed and whether all functions on $X$ are obtained by restricting functions on $X\times_YX$. ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2))

As explained above, in algebraic geometry we regard separatedness as the property replacing Hausdorff. Recalling that a topological space $T$ is Hausdorff if and only if the diagonal is closed in $T\times T$ ([\[Topology\] §Hausdorff Spaces, ⁋Lemma 5](/en/math/topology/Hausdorff_spaces#lem5)), the following proposition is naturally expected.

::: Proposition 4
$\varphi:X \rightarrow Y$ is separated if and only if the image of $X$ under the diagonal morphism $\Delta: X \rightarrow X\times_YX$ is a closed set.
:::
::: Proof
By definition, if $\varphi$ is separated then $\Delta(X)$ is closed, which is obvious. Hence we assume $\Delta(X)$ is closed and show that $\Delta$ is a closed embedding. As seen before, $\Delta$ is always a homeomorphism onto $\Delta(X)$, so with this assumption the topological condition is already secured and we only need to show that $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$ is surjective. This can be checked on stalks.

First, there is nothing to see at points $q\notin \Delta(X)$. From the assumption that $\Delta(X)$ is closed, there exists an open neighborhood $W$ of $q$ such that $W\cap\Delta(X)=\emptyset$, and then $\Delta^{-1}(W)=\emptyset$ so

$$(\Delta_\ast\mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$$

and thus $(\Delta_\ast\mathcal{O}_X)_q=0$. The open neighborhoods chosen below cannot cover points outside $\Delta(X)$, so this is exactly where the assumption is actually used.

Now consider points of the form $\Delta(p)$. For any $p\in X$ we can choose an open affine subset $U$ containing $p$, and if necessary restrict $U$ so that $\varphi(U)$ is contained in some open affine subset $V$ of $Y$. Then $U\times_VU$ is an open subset of $X\times_YX$ and an open neighborhood of $\Delta(p)$, and since $p_1\circ\Delta=p_2\circ\Delta=\id_X$ we have $\Delta^{-1}(U\times_VU)=U$. On this, $\Delta: U \rightarrow U\times_VU$ is a closed embedding by [Lemma 5](#lem5) below, so $\mathcal{O}_{U\times_VU} \rightarrow \Delta_\ast\mathcal{O}_U$ is surjective, and in particular the morphism between stalks at $\Delta(p)$ is surjective.
:::

Then from this we obtain the following.

::: Lemma 5
Any morphism between affine schemes $\varphi:X \rightarrow Y$ is always separated.
:::
::: Proof
If $X=\Spec A$ and $Y=\Spec B$, then $X\times_YX=\Spec(A\otimes_BA)$ ([§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2)), and $\Delta$ is induced from the ring homomorphism

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'.$$

This ring homomorphism sends $a\otimes 1$ to $a$, so it is surjective, and hence $\Delta$ is a closed embedding. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))
:::

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10). For convenience let us call this scheme $X$ and its two charts $X_1=\Spec\mathbb{K}[\x_1]$, $X_2=\Spec\mathbb{K}[\x_2]$. Since these are glued along $D(\x_1)$ and $D(\x_2)$ by identifying $\x_1$ and $\x_2$, the intersection of the two charts is

$$X_1\cap X_2=X\setminus \{0_1,0_2\}=\Spec\mathbb{K}[t,1/t]$$

where $t$ is the coordinate corresponding to both $\x_1$ and $\x_2$ under this gluing. Since $X$ is a scheme over $\mathbb{K}$, what we look at is $X\times_\mathbb{K}X$, and since the fiber product can be computed by restricting each factor to open subsets ([§Fiber Products, ⁋Lemma 4](/en/math/scheme_theory/fiber_products#lem4)), this is obtained by gluing four charts

$$X_a\times_\mathbb{K}X_b=\Spec\bigl(\mathbb{K}[\x_a]\otimes_\mathbb{K}\mathbb{K}[\x_b]\bigr)=\Spec\mathbb{K}[\x_a,\x_b]\cong \mathbb{A}^2_\mathbb{K}\qquad (a,b\in \{1,2\}).$$

In this process, points where both coordinates are nonzero become the same point in all four charts and appear once each; points where only one coordinate is zero appear twice; and the origin where both coordinates are zero appears four times.

Now since $p_1\circ\Delta=p_2\circ\Delta=\id_X$, we have $\Delta^{-1}(X_a\times_\mathbb{K}X_b)=X_a\cap X_b$. That is, if $a=b$ this is all of $X_a$ and by [Lemma 5](#lem5) $\Delta$ is a closed embedding on it; in particular the two origins of $X$ go to $(0_1,0_1)$ and $(0_2,0_2)$ among the four origins. On the other hand, if $a\neq b$ then $\Delta$ is the morphism induced on $X_1\cap X_2=\Spec\mathbb{K}[t,1/t]$ by the ring homomorphism

$$\mathbb{K}[\x_1,\x_2] \longrightarrow \mathbb{K}[t,1/t];\qquad \x_1,\x_2\mapsto t$$

so within the chart $X_1\times_\mathbb{K}X_2\cong \mathbb{A}^2_\mathbb{K}$, the set $\Delta(X)$ is $Z(\x_1-\x_2)\cap D(\x_1)$, the diagonal with the origin removed. The closure of this set is the entire diagonal $Z(\x_1-\x_2)$, and its origin is exactly $(0_1,0_2)$, so $(0_1,0_2)$ does not belong to $\Delta(X)$ while belonging to its closure. Therefore $\Delta(X)$ is not closed, and by [Proposition 4](#prop4), $X$ is not separated. This space is also the standard example of a space that is not Hausdorff topologically.

Now let us see the criterion for separatedness. Unlike in [Example 2](#ex2), the criterion is required for all valuation rings, not necessarily discrete ones—i.e., for all subrings $A$ of a field $K$ satisfying only the condition that for any $x\in K^\times$ either $x\in A$ or $x^{-1}\in A$. ([\[Commutative Algebra\] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5)) Also, below $j:\Spec K \rightarrow \Spec A$ always denotes the morphism induced by the inclusion $A\hookrightarrow K$.

::: Theorem 6
For a Noetherian scheme $X$ and a scheme morphism $\varphi:X \rightarrow Y$, $\varphi$ is separated if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, whenever any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

with the outer square given, there is at most one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
That the outer square is given means morphisms $u:\Spec K \rightarrow X$ and $v: \Spec A \rightarrow Y$ are given with $\varphi\circ u=v\circ j$, and a lifting of this square means a $g:\Spec A \rightarrow X$ satisfying $g\circ j=u$ and $\varphi\circ g=v$.

Throughout the proof we use two standard facts. The first is the existence theorem for valuation rings: whenever a field $K$ and a local subring $\mathcal{O}$ inside it are given, there exists a valuation ring $A$ with $\Frac(A)=K$, $\mathcal{O}\subseteq A$, and $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$. In this case we say $A$ *dominates* $\mathcal{O}$, and the existence of such $A$ is obtained by applying Zorn's lemma to the collection of local subrings of $K$ dominating $\mathcal{O}$. The second is that for a field $K$, a morphism $\Spec K \rightarrow X$ corresponds one-to-one with a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. This follows from the case $X=\Spec B$ where a ring homomorphism $B \rightarrow K$ gives the pair of its kernel prime ideal $\mathfrak{p}$ and $\kappa(\mathfrak{p}) \rightarrow K$, and the general case is obtained by choosing an affine open neighborhood of $x$.

First assume $\varphi$ is separated, and suppose two liftings $g_1, g_2$ of the above square are given. Since $\varphi\circ g_1=\varphi\circ g_2=v$, by the universal property of the fiber product there exists a unique $h:\Spec A \rightarrow X\times_YX$ with $p_1\circ h=g_1$, $p_2\circ h=g_2$. Here $p_1,p_2$ are the two projections. Now since $\Delta$ is a closed embedding, the base change

$$Z=\Spec A\times_{X\times_YX}X \longrightarrow \Spec A$$

is also a closed embedding. That closed embeddings are stable under base change is obtained affine-locally from the fact that a base change of $B \rightarrow B/\mathfrak{b}$ is $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$, which remains surjective. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3))

Meanwhile $p_1\circ h\circ j=g_1\circ j=u$ and $p_2\circ h\circ j=g_2\circ j=u$, and $p_1\circ \Delta\circ u=u$ and $p_2\circ\Delta\circ u=u$, so by uniqueness in the universal property $h\circ j=\Delta\circ u$. Therefore $j$ factors through the pullback $Z$, and in particular the image of $Z \rightarrow \Spec A$ is a closed set containing the image of $j$, i.e., the zero ideal $(0)$ of $A$. Since $A$ is a domain, $(0)$ is the generic point of $\Spec A$ ([§The Topological Structure of Schemes, ⁋Example 5](/en/math/scheme_theory/topology_of_schemes#ex5)), and hence the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself. Then $Z$ is of the form $\Spec(A/\mathfrak{a})$ for some ideal $\mathfrak{a}\subseteq A$ as a closed subscheme of $\Spec A$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and that its image is all of $\Spec A$ means that $\mathfrak{a}$ is contained in every prime ideal of $A$, i.e.,

$$\mathfrak{a}\subseteq \mathfrak{N}(A)=(0).$$

The last equality comes from the fact that $A$ is a domain. Therefore $Z \rightarrow \Spec A$ is an isomorphism, and this means that $h$ factors through $\Delta$, i.e., $h=\Delta\circ g$ for some $g:\Spec A \rightarrow X$. Then

$$g_1=p_1\circ h=p_1\circ \Delta\circ g=g,\qquad g_2=p_2\circ h=p_2\circ\Delta\circ g=g$$

so $g_1=g_2$. In this direction the assumption that $X$ is Noetherian is not used.

Conversely, assume that for any square there exists at most one lifting. By [Proposition 4](#prop4) it suffices to show that $\Delta(X)$ is a closed subset of $X\times_YX$.

First we observe that every point of $\cl(\Delta(X))$ is a specialization of some point of $\Delta(X)$. Since $X$ is a Noetherian scheme, it is also Noetherian as a topological space ([§The Topological Structure of Schemes, ⁋Definition 14](/en/math/scheme_theory/topology_of_schemes#def14)), and thus has finitely many irreducible components $X_1,\ldots, X_r$. ([\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13)) Each $X_i$ is an irreducible closed subset, so it has a generic point $\eta_i$ ([§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)), and $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$. Now since $\Delta$ is continuous, $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$ and the right-hand side is a finite union hence closed; conversely each $\Delta(\eta_i)$ belongs to $\Delta(X)$, so we obtain

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\}).$$

That is, any point of $\cl(\Delta(X))$ is a specialization of some $\Delta(\eta_i)\in \Delta(X)$. ([§The Topological Structure of Schemes, ⁋Definition 2](/en/math/scheme_theory/topology_of_schemes#def2)) Therefore if we show that $\Delta(X)$ is closed under specialization, then $\Delta(X)=\cl(\Delta(X))$ and the proof is complete.

Let $\xi=\Delta(x)\in \Delta(X)$ and $\eta\in\cl(\{\xi\})$. Giving the reduced scheme structure to the closed set $T=\cl(\{\xi\})$ ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)), $T$ is an integral scheme with generic point $\xi$. Choose an affine open subset $\Spec B\subseteq T$ containing $\eta$. Since a generic point belongs to every nonempty open set, $\Spec B$ also contains $\xi$, and $B$ is a domain with $\xi$ corresponding to the zero ideal of $B$, so

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

where $\mathfrak{q}$ is the prime ideal corresponding to $\eta$. In particular $\mathcal{O}$ is a local domain with $\Frac(\mathcal{O})=K$. Choosing a valuation ring $A$ of $K$ dominating $\mathcal{O}$ by the existence theorem quoted above, the morphism

$$q:\Spec A \longrightarrow \Spec \mathcal{O} \longrightarrow T \hookrightarrow X\times_YX$$

induced by the local homomorphism $\mathcal{O} \rightarrow A$ sends the generic point $(0)$ of $\Spec A$ to $\xi$ and the closed point $\mathfrak{m}_A$ to $\eta$.

Now let $g_1=p_1\circ q$, $g_2=p_2\circ q$, and since $\varphi\circ p_1=\varphi\circ p_2$ we consider the well-defined $w=\varphi\circ g_1=\varphi\circ g_2:\Spec A \rightarrow Y$. As seen in the proof of [Proposition 4](#prop4), choosing an affine open neighborhood $U$ of $x$ and an affine open subset $V$ of $Y$ containing $\varphi(U)$, we have that $U\times_VU$ is an open neighborhood of $\xi$ in $X\times_YX$ and on it $\Delta$ is a closed embedding ([Lemma 5](#lem5)), so the stalk morphism $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$ is surjective and hence $\kappa(\xi) \rightarrow \kappa(x)$ is also surjective. Meanwhile since $p_1\circ\Delta=\id_X$, the composition $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$ is the identity, and therefore the two morphisms are inverse isomorphisms of each other. That is, $K=\kappa(\xi)\cong\kappa(x)$. Under this identification, let $u:\Spec K \rightarrow X$ be the canonical morphism defined by the point $x$ and $\kappa(x)\cong K$; then $\Delta\circ u$ is the canonical morphism defined by the point $\xi$ and $\kappa(\xi)\cong K$, and this equals $q\circ j$. Indeed $q\circ j$ has $\xi$ as image and induces the identity on $\kappa(\xi)=\Frac(\mathcal{O})=K$ on residue fields. Therefore

$$g_1\circ j=p_1\circ q\circ j=p_1\circ \Delta\circ u=u,\qquad g_2\circ j=p_2\circ q\circ j=p_2\circ\Delta\circ u=u$$

and $\varphi\circ g_1=\varphi\circ g_2=w$, so $g_1$ and $g_2$ are two liftings of the square given by $u$ and $w$. By assumption $g_1=g_2$, and then $\Delta\circ g_1$ and $q$ give $g_1$ and $g_2=g_1$ respectively when composed with $p_1$, $p_2$, so by the universal property of the fiber product $q=\Delta\circ g_1$. Therefore

$$\eta=q(\mathfrak{m}_A)=\Delta(g_1(\mathfrak{m}_A))\in \Delta(X)$$

and $\Delta(X)$ is closed under specialization. Combined with the previous observation, $\Delta(X)=\cl(\Delta(X))$, so $\Delta(X)$ is a closed set, and by [Proposition 4](#prop4), $\varphi$ is separated.
:::

Intuitively, $\Spec A$ consists of the generic point $(0)$ and the closed point $\mathfrak{m}_A$ to which it specializes; the generic point must go to the image $\xi$ of $u$ by the condition $g\circ j=u$, so giving a lifting $g:\Spec A \rightarrow X$ is specifying a point $\eta=g(\mathfrak{m}_A)$ with $\eta\in \cl(\{\xi\})$, i.e., choosing a limit of the given germ inside $X$. Thus that there is at most one lifting means that a single germ does not split into two different limits, and as the proof shows this is exactly the topological condition that $\Delta(X)$ is closed under specialization. Conversely, the existence theorem for valuation rings used in the proof realizes any specialization inside $X$ as such a germ, and this is why the criterion is required for arbitrary valuation rings, not just discrete ones. However, the $\Spec$ of a general valuation ring has prime ideals forming longer chains, departing from the two-point picture of [Example 2](#ex2); if $Y$ is Noetherian and $\varphi$ is a finite type morphism, then the above theorem can be replaced by one for arbitrary discrete valuation rings, so that picture survives intact. We omit the proof of this fact as it is beyond our current reach.

Let us actually verify this picture.

::: Example 7
Earlier we checked that the line with double origin $X$ is not separated using [Proposition 4](#prop4), but using [Theorem 6](#thm6) the same fact is revealed directly in terms of limits of curves. Let $A=\mathbb{K}[t]_{(t)}$ be a discrete valuation ring with uniformizer $t$ and $K=\Frac(A)=\mathbb{K}(t)$, and let $Y=\Spec\mathbb{K}$. Consider the morphism $u:\Spec K \rightarrow X$ defined by the ring homomorphism $\mathbb{K}[\x_1] \rightarrow K$, $\x_1\mapsto t$. Since $t$ is a unit of $K$, the image of $u$ lies in the open set where the two charts overlap. Since everything is over $\mathbb{K}$, $u$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form the outer square.

Now as before let the two charts be $X_1=\Spec\mathbb{K}[\x_1]$, $X_2=\Spec\mathbb{K}[\x_2]$, and define two morphisms

$$g_1:\Spec A \longrightarrow X_1\subseteq X,\qquad g_2:\Spec A \longrightarrow X_2\subseteq X$$

by $\x_1\mapsto t$ and $\x_2\mapsto t$ respectively; both are well-defined since $t\in A$. Since the two charts are glued by identifying $\x_1$ and $\x_2$ outside the origin, we have $g_1\circ j=g_2\circ j=u$, so both are liftings of this square. However, $g_1$ sends $\mathfrak{m}_A=(t)$ to the origin $0_1$ of the first chart, while $g_2$ sends it to the origin $0_2$ of the second chart, so $g_1\neq g_2$. That is, the germ of a curve missing a point has two limits, and this is why $X$ is not separated.
:::

Meanwhile from [Theorem 6](#thm6) we obtain the following.

::: Corollary 8
For Noetherian schemes,

1. Open immersions and closed embeddings are both separated.
2. The composition of two separated morphisms is separated.
3. Separated morphisms are preserved under base change.
4. Separated morphisms are preserved under fiber products.
5. If $\varphi:X \rightarrow Y$, $\psi:Y \rightarrow Z$ are scheme morphisms and $\psi\circ \varphi$ is a separated morphism, then $\varphi$ is also a separated morphism.
:::
::: Proof
Item 1 is checked directly from the definition. If $\varphi$ is a closed embedding, then for every affine open subset $V=\Spec B$ of $Y$ we have $\varphi^{-1}(V)=\Spec A$ with $B \rightarrow A$ surjective ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and collecting all such $V$, the $\varphi^{-1}(V)\times_V\varphi^{-1}(V)$ cover $X\times_YX$. On each of these $\Delta$ is a closed embedding by the computation of [Lemma 5](#lem5), and since closed embeddings are affine-local on the target, $\Delta$ itself is a closed embedding. If $\varphi$ is an open immersion, view $X$ as an open subscheme of $Y$ and consider affine open subsets $V=\Spec B$ of $Y$ and basic open subsets $\Spec B_b$ of $X$ contained in them. Then the $\Spec B_b\times_V\Spec B_{b'}$ cover $X\times_YX$, and

$$B_b\otimes_BB_{b'}\cong B_{bb'}=\mathcal{O}(\Spec B_b\cap \Spec B_{b'})$$

so $\Delta$ is an isomorphism on each and in particular a closed embedding.

The rest is obtained from the criterion of [Theorem 6](#thm6). That is, we only need to check that uniqueness of liftings is inherited.

For item 2, suppose for $\psi\circ \varphi$ an outer square $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Z$ and two liftings $h_1,h_2:\Spec A \rightarrow X$ are given. Then $\varphi\circ h_1$ and $\varphi\circ h_2$ are two liftings for $\psi$ with respect to $u' = \varphi\circ u$ and $v$, so $\varphi\circ h_1=\varphi\circ h_2$, and then $h_1,h_2$ are two liftings for $\varphi$ with respect to $u$ and $\varphi\circ h_1$, so $h_1=h_2$.

For item 3, given $Y' \rightarrow Y$ and $X'=X\times_YY'$, $\varphi':X' \rightarrow Y'$, suppose a square for $\varphi'$ and its two liftings $g_1',g_2':\Spec A \rightarrow X'$ are given. Their compositions with $X' \rightarrow X$ are two liftings for $\varphi$, so they are equal, and their compositions to $Y'$ are also the same morphism given by the square, so by uniqueness in the universal property of the fiber product $g_1'=g_2'$.

For item 5, if a square for $\varphi$ and two liftings $g_1,g_2$ are given, compose $\Spec A \rightarrow Y$ with $\psi$ to obtain a square for $\psi\circ \varphi$, and $g_1,g_2$ are its two liftings, so $g_1=g_2$.

Finally, item 4 follows for $S$-schemes from the fact that for separated morphisms $\varphi:X \rightarrow Y$, $\varphi':X' \rightarrow Y'$, the product $\varphi\times \varphi'$ decomposes as

$$X\times_SX' \longrightarrow Y\times_SX' \longrightarrow Y\times_SY'$$

and the two morphisms are base changes of $\varphi$ and $\varphi'$ respectively, so this follows from items 3 and 2.
:::

In particular, using items 2 and 5 together, we know that when $Y$ is a separated scheme, a $Y$-scheme $X$ is a separated scheme if and only if its structure morphism $X \rightarrow Y$ is separated. Since an affine scheme is always a separated scheme by [Lemma 5](#lem5), for a scheme over an affine scheme we can determine separatedness by looking only at the structure morphism.

Separatedness is also used to determine when two morphisms are equal. Let $X$ be a reduced scheme and $Y$ a separated scheme, and suppose two morphisms $\varphi,\psi: X \rightarrow Y$ agreeing on a dense open subset $W$ of $X$ are given. Then for the morphism $h: X \rightarrow Y\times_{\Spec \mathbb{Z}}Y$ induced by $\varphi$ and $\psi$, the locus where $\varphi$ and $\psi$ agree is given by base changing $\Delta$ along $h$, and the base change of a closed embedding is again a closed embedding, so (proof of [Theorem 6](#thm6)) this is a closed subscheme of $X$. This closed subscheme contains $W$ and is topologically all of $X$, so the ideal sheaf defining it is contained in $\mathfrak{N}(A)=0$ on each affine open subset $\Spec A$ of $X$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), and therefore $\varphi=\psi$. Applying this to [§Properties of Scheme Morphisms, ⁋Definition 22](/en/math/scheme_theory/properties_of_scheme_morphisms#def22), when $Y$ is separated and $X$ is reduced, the equivalence relation on rational maps becomes the condition that two representatives agree on all of $U\cap V$. In that post this was checked for $Y$ affine, and since affine schemes are always separated, this is a special case of the above argument.

## Proper Morphisms

Now we move to the property corresponding to compactness. In topology we saw that compactness can be rewritten as the condition of being universally closed ([\[Topology\] §Proper Maps, ⁋Theorem 6](/en/math/topology/proper_maps#thm6)), and in algebraic geometry this condition with products replaced by fiber products becomes the definition as is.

::: Definition 9
We say $\varphi:X \rightarrow Y$ is *universally closed* if $\varphi$ is a closed map and for any $Y' \rightarrow Y$, the map $X\times_Y Y' \rightarrow Y'$ is also closed. A separated, universally closed finite type morphism is called a *proper morphism*.
:::

Setting $Y'=Y$, the second condition includes the first, so the substantive condition is that every base change is a closed map. Meanwhile, since we work within the category of Noetherian schemes in this section, when checking universally closed below we only consider base changes $Y' \rightarrow Y$ for Noetherian schemes. That the condition for arbitrary $Y'$ follows from this is obtained by a limit argument writing the coordinate ring as a filtered colimit of finitely generated subalgebras after restricting $Y'$ to be affine, but this is beyond the scope of this post.

Since a proper morphism requires both the separated condition and the universally closed condition, the criterion also splits into two pieces. [Theorem 6](#thm6) tested separatedness by uniqueness of liftings, so what remains is that existence of liftings tests universal closedness.

::: Proposition 10
For a finite type scheme morphism $\varphi:X \rightarrow Y$ between Noetherian schemes, $\varphi$ is universally closed if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, whenever any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

with the outer square given, there exists at least one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
As in the proof of [Theorem 6](#thm6), write the outer square as $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$, $j:\Spec K \rightarrow \Spec A$, and continue using the two standard facts quoted in that proof. That is, a local subring in a field $K$ is always dominated by a valuation ring $A$ with $\Frac(A)=K$, and a morphism $\Spec K \rightarrow X$ is the same as a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. To this we add the following maximality of valuation rings. If a local subring $\mathcal{O}\subseteq K$ dominating a valuation ring $A$ of $K$ is given, then $\mathcal{O}=A$. Indeed, if $c\in\mathcal{O}$ is nonzero and $c\notin A$, then by definition of a valuation ring $c^{-1}\in A$, and since $c\notin A$, $c^{-1}$ is not a unit of $A$. That is, $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$, but $c\in\mathcal{O}$ so $c^{-1}$ becomes a unit of $\mathcal{O}$, a contradiction. Therefore $\mathcal{O}\subseteq A$, and by definition of domination $A\subseteq\mathcal{O}$, so $\mathcal{O}=A$.

First suppose $\varphi$ is universally closed and construct a lifting. Base changing along $v$, we obtain $X_A=X\times_Y\Spec A$ and the projection $\pi:X_A \rightarrow \Spec A$, which is a closed map. ([Definition 9](#def9)) Meanwhile $u$ and $j$ induce by the universal property of the fiber product a morphism $\tilde{u}:\Spec K \rightarrow X_A$ over $\Spec A$, and if we find an extension of $\tilde{u}$ as a section of $\pi$ of the form $\Spec A \rightarrow X_A$, then projecting this to $X$ gives the desired lifting.

Let $\xi\in X_A$ be the image of $\tilde{u}$ and give the reduced scheme structure to $Z=\cl(\{\xi\})$. ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14)) Since $\pi\circ\tilde{u}=j$, $\pi(\xi)$ is the generic point $(0)$ of $\Spec A$, and since $\pi$ is a closed map, $\pi(Z)$ is a closed set containing $(0)$, i.e., all of $\Spec A$. Therefore there exists $z\in Z$ with $\pi(z)=\mathfrak{m}_A$.

Let us examine the residue fields. The morphism $\kappa((0))=K \rightarrow K$ induced by $\pi\circ \tilde{u}=j$ at $(0)$ is the identity, and this is the composition of the morphism $K\rightarrow\kappa(\xi)$ induced by $\pi$ and the morphism $\kappa(\xi) \rightarrow K$ induced by $\tilde{u}$, so the two morphisms are inverse isomorphisms of each other. That is, $\kappa(\xi)\cong K$. Then since $Z$ is an integral scheme with generic point $\xi$, as in the proof of [Theorem 6](#thm6) we choose an affine open subset containing $z$ to obtain

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K.$$

Also the morphism $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$ induced by $\pi\vert_Z$ is a local homomorphism, and since the morphism it induces at the generic point $K \rightarrow \kappa(\xi)=K$ is the identity, this morphism is an inclusion map between subrings of $K$. That is, $\mathcal{O}$ is a local subring of $K$ dominating $A$, and by the maximality above $\mathcal{O}_{Z,z}=A$.

Then we obtain the canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$, and its composition with $\pi$ corresponds to the identity on $A$ at the ring level, so it is a section of $\pi$. The restriction of this section to $\Spec K$ has $\xi$ as image and induces the identity on $\kappa(\xi)=K$ on residue fields, so it equals $\tilde{u}$. Therefore projecting this section to $X$ gives $g:\Spec A \rightarrow X$ with $g\circ j=u$ and $\varphi\circ g=v$.

Conversely, assume the existence part holds. Following the convention stated after [Definition 9](#def9), we only consider base changes $Y' \rightarrow Y$ for Noetherian schemes.

First, the existence part is stable under base change. Given $Y' \rightarrow Y$ and $X'=X\times_YY'$, $\varphi':X' \rightarrow Y'$, suppose $\Spec K \rightarrow X'$ and $\Spec A \rightarrow Y'$ form an outer square for $\varphi'$. Composing these with $X' \rightarrow X$, $Y' \rightarrow Y$ gives an outer square for $\varphi$, so a lifting $g:\Spec A \rightarrow X$ exists, and $g$ with $\Spec A \rightarrow Y'$ give a unique $g':\Spec A \rightarrow X'$ by the universal property. $g'\circ j$ and the given $\Spec K \rightarrow X'$ are equal since their compositions with $X' \rightarrow X$, $X' \rightarrow Y'$ are respectively equal, so $g'$ is a lifting for $\varphi'$. Meanwhile finite type morphisms are stable under base change and a finite type scheme over a Noetherian scheme is again Noetherian, so $X'$ is Noetherian and $\varphi'$ is finite type. Therefore, to show that $\varphi$ is a closed map when a Noetherian scheme $X$ and finite type morphism $\varphi:X \rightarrow Y$ satisfy the existence part of the criterion, and then applying this to all base changes, the proof is complete.

To show this, choose a closed subset $T$ of $X$ and give it the reduced scheme structure. The closed embedding $T\hookrightarrow X$ is a finite morphism, so ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)) it is finite type, and hence $T$ is a Noetherian scheme and $\varphi\vert_T:T \rightarrow Y$ is also finite type. Also $\varphi\vert_T$ inherits the existence part of the criterion. Indeed, if $\Spec K \rightarrow T$ and $\Spec A \rightarrow Y$ form a square for $\varphi\vert_T$, applying the criterion to $\Spec K \rightarrow T\hookrightarrow X$ gives a lifting $g_0:\Spec A \rightarrow X$. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so $g_0(\Spec A)\subseteq \cl(\{g_0((0))\})\subseteq T$, and since $\Spec A$ is reduced, $g_0$ factors through $T$. Here the last fact is obtained as follows. For a morphism $\psi:S \rightarrow X$ from a reduced scheme $S$ whose image lies in a closed set $T$, choose an affine open subset $\Spec B$ of $X$ and an affine open subset $\Spec R$ of $\psi^{-1}(\Spec B)$. If $T\cap \Spec B=Z(\mathfrak{b})$ ($\mathfrak{b}$ a radical ideal), then the reduced structure of $T$ is $\Spec (B/\mathfrak{b})$ on it, and the corresponding ring homomorphism $\phi:B \rightarrow R$ satisfies $\mathfrak{b}\subseteq \phi^{-1}(\mathfrak{p})$ for any prime ideal $\mathfrak{p}\subseteq R$, so

$$\phi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\mathfrak{N}(R)=(0).$$

That is, $\phi$ uniquely factors through $B/\mathfrak{b}$, and these local factorizations glue by uniqueness.

Therefore it suffices to show that $\varphi(T)=\varphi\vert_T(T)$ is a closed set, and ultimately it suffices to show that the image $\varphi(X)$ is closed for a finite type morphism $\varphi:X \rightarrow Y$ (with $X$ Noetherian) satisfying the existence part of the criterion.

We first show that $\varphi(X)$ is closed under specialization. Let $y_1=\varphi(x_1)\in \varphi(X)$ and $y_0\in\cl(\{y_1\})$. Giving the reduced scheme structure to $W=\cl(\{y_1\})$, $W$ is an integral scheme with generic point $y_1$, and as before $\mathcal{O}=\mathcal{O}_{W,y_0}$ is a local domain with $\Frac(\mathcal{O})=\kappa(y_1)$. Now let $K=\kappa(x_1)$ and view $\mathcal{O}$ as a local subring of $K$ via the field homomorphism $\kappa(y_1)\hookrightarrow K$ induced by $\varphi$. Then there exists a valuation ring $A$ of $K$ dominating $\mathcal{O}$, and from this we obtain two morphisms

$$\Spec A \longrightarrow \Spec\mathcal{O} \longrightarrow W\hookrightarrow Y,\qquad u:\Spec K \longrightarrow X.$$

Here $u$ is the canonical morphism defined by the point $x_1$ and $\kappa(x_1)=K$. These two form the outer square, because both compositions to $\Spec K \rightarrow Y$ are the canonical morphism defined by the point $y_1$ and the field homomorphism $\kappa(y_1)\hookrightarrow K$. By existence in the criterion, a lifting $g_0:\Spec A \rightarrow X$ exists, and since $\Spec A \rightarrow \Spec\mathcal{O}$ comes from a local homomorphism, $\mathfrak{m}_A$ goes to $\mathfrak{m}_\mathcal{O}$, i.e., $y_0$. Therefore $\varphi(g_0(\mathfrak{m}_A))=y_0$ and $y_0\in \varphi(X)$.

Finally, we repeat the topological observation from the proof of [Theorem 6](#thm6) verbatim. If the generic points of the irreducible components $X_1,\ldots,X_r$ of $X$ are $\eta_1,\ldots,\eta_r$, then $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$, so

$$\cl(\varphi(X))=\bigcup_{i=1}^r\cl(\{\varphi(\eta_i)\})$$

and therefore every point of $\cl(\varphi(X))$ is a specialization of a point of $\varphi(X)$. Since we showed above that $\varphi(X)$ is closed under specialization, $\varphi(X)=\cl(\varphi(X))$.
:::

Then combining the two pieces we obtain the criterion for properness.

::: Theorem 11
For a finite type scheme morphism $\varphi:X \rightarrow Y$ between Noetherian schemes, $\varphi$ is proper if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, whenever any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

with the outer square given, there exists exactly one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
Since $\varphi$ is assumed finite type, by [Definition 9](#def9) $\varphi$ is proper if and only if $\varphi$ is separated and universally closed. By [Theorem 6](#thm6), $\varphi$ is separated if and only if any outer square has at most one lifting, and by [Proposition 10](#prop10), $\varphi$ is universally closed if and only if any outer square has at least one lifting. Both conditions holding together is exactly that every square has exactly one lifting.
:::

It is good to see what the criterion looks like when it fails. If [Example 7](#ex7) was the case where uniqueness fails, the following is the case where existence fails.

::: Example 12
$\mathbb{A}^1_\mathbb{K}=\Spec\mathbb{K}[\x]$ is not proper over $\Spec\mathbb{K}$. Choose $A=\mathbb{K}[t]_{(t)}$ and $K=\Frac(A)=\mathbb{K}(t)$, and consider the morphism $u:\Spec K \rightarrow \mathbb{A}^1_\mathbb{K}$ defined by the ring homomorphism

$$\mathbb{K}[\x] \longrightarrow K;\qquad \x\mapsto 1/t.$$

Since everything is over $\mathbb{K}$, $u$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form the outer square. If a lifting $g:\Spec A \rightarrow \mathbb{A}^1_\mathbb{K}$ existed, it would correspond to a ring homomorphism $\mathbb{K}[\x] \rightarrow A$, and the condition $g\circ j=u$ means the composition of this homomorphism with $A\hookrightarrow K$ sends $\x$ to $1/t$. That is, $1/t\in A$ must hold, but since $t$ is a uniformizer of $A$ this is impossible. Therefore no lifting exists, and by [Theorem 11](#thm11), $\mathbb{A}^1_\mathbb{K} \rightarrow \Spec\mathbb{K}$ is not proper.

Geometrically, this $u$ is a germ of a curve escaping to infinity from the origin, and the criterion reads off directly that this limit does not exist in $\mathbb{A}^1_\mathbb{K}$. Doing the same calculation in $\mathbb{P}^1_\mathbb{K}$, $1/t$ becomes $t$ in the chart corresponding to infinity, so a lifting exists, and this is generalized in [Theorem 15](#thm15).
:::

Similarly the following corollary holds.

::: Corollary 13
For Noetherian schemes,

1. A closed embedding is proper.
2. The composition of proper morphisms is proper.
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber products.
5. If $\varphi:X \rightarrow Y$, $\psi:Y \rightarrow Z$ are scheme morphisms, $\psi$ is separated, and $\psi\circ \varphi$ is a proper morphism, then $\varphi$ is also a proper morphism.
:::
::: Proof
For item 1, a closed embedding is separated by item 1 of [Corollary 8](#cor8), and is a finite morphism so ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4)) finite type. Also a closed embedding is a closed map and stable under base change (proof of [Theorem 6](#thm6)), so universally closed.

For item 2, separated is item 2 of [Corollary 8](#cor8) and the composition of finite type morphisms is finite type, so we only need to show universally closed. Given $Z' \rightarrow Z$, since $X\times_ZZ'=X\times_Y(Y\times_ZZ')$, the two morphisms

$$X\times_ZZ' \longrightarrow Y\times_ZZ' \longrightarrow Z'$$

are base changes of $\varphi$ and $\psi$ respectively, and hence both are closed maps. The composition of closed maps is a closed map, so $X\times_ZZ' \rightarrow Z'$ is also closed.

For item 3, separated is item 3 of [Corollary 8](#cor8), finite type is stable under base change, and universally closed follows immediately from the definition since a base change of a base change is again a base change. Then item 4 follows by applying the same decomposition as in item 4 of [Corollary 8](#cor8) to items 2 and 3.

Finally for item 5. Consider the graph morphism $\Gamma_\varphi:X \rightarrow X\times_ZY$ induced by $\id_X$ and $\varphi$; then $\varphi=p_2\circ\Gamma_\varphi$. The square formed by $\Gamma_\varphi$ and $\varphi\times\id_Y: X\times_ZY \rightarrow Y\times_ZY$ is a cartesian square with base $\Delta_{Y/Z}:Y \rightarrow Y\times_ZY$. Indeed for any $T$, matching two morphisms to $Y\times_ZY$ is choosing a pair $a:T \rightarrow X$ and $b:T \rightarrow Y$ with $\varphi\circ a=b$, and such a pair is determined by $a$ alone. Then since $\psi$ is separated by assumption, $\Delta_{Y/Z}$ is a closed embedding, so $\Gamma_\varphi$ is also a closed embedding, and by item 1 it is proper. Meanwhile $p_2:X\times_ZY \rightarrow Y$ is the base change of $\psi\circ \varphi$ along $\psi$, so by item 3 it is proper. Therefore by item 2, $\varphi=p_2\circ\Gamma_\varphi$ is proper.
:::

The assumption that $\psi$ is separated in item 5 is because the reason $\Gamma_\varphi$ becomes a closed embedding in the proof is exactly that $\Delta_{Y/Z}$ is a closed embedding. Without this assumption, the guarantee that $\Gamma_\varphi$ is a closed embedding disappears and the argument does not work. Note that item 5 of [Corollary 8](#cor8) did not require such an assumption, so the shapes of the two items differ.

Meanwhile item 1 of [Corollary 13](#cor13) is the following special case. This is the most typical example showing how the criterion is actually used, where existence comes from the single fact that a valuation ring is integrally closed.

::: Corollary 14
A finite morphism between Noetherian schemes is proper.
:::
::: Proof
A finite morphism $\varphi:X \rightarrow Y$ is an affine morphism, so for any affine open subset $V\subseteq Y$, $\varphi^{-1}(V)$ is affine, and hence by [Lemma 5](#lem5) and the affine-local criterion for closed embeddings ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), $\varphi$ is separated. Also a finite morphism is finite type. ([§Properties of Scheme Morphisms, ⁋Proposition 15](/en/math/scheme_theory/properties_of_scheme_morphisms#prop15)) Therefore by [Theorem 11](#thm11) we only need to check existence of liftings.

Suppose an outer square $u:\Spec K \rightarrow X$, $v:\Spec A \rightarrow Y$ is given. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so choosing an affine open subset $V=\Spec B$ of $Y$ containing $v(\mathfrak{m}_A)$, we have that $V$ also contains $v((0))$ and hence $v$ factors through $V$. Then the image of $u$ lies in $\varphi^{-1}(V)=\Spec C$, and $C$ is finitely generated as a $B$-module. Now the problem becomes: given ring homomorphisms

$$B \longrightarrow A,\qquad C \longrightarrow K$$

construct $C \rightarrow A$ compatible with these.

Any $c\in C$ is integral over $B$, so for suitable $b_i\in B$,

$$c^n+b_{n-1}c^{n-1}+\cdots+b_0=0$$

holds. Pushing this equation through $C \rightarrow K$, the image of $c$ is integral over the image of $B$, and since the image of $B$ lies in $A$, the image of $c$ is integral over $A$. But valuation rings are always integrally closed ([\[Commutative Algebra\] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6), item 2), so the image of $c$ belongs to $A$. That is, $C \rightarrow K$ factors through $A$, and this gives the desired lifting.
:::

The same criterion gives much larger results. A projective morphism is by definition a composition of a closed embedding and a projection $\mathbb{P}^n_Y \rightarrow Y$ ([Definition 1](#def1)), and the closed embedding side is already handled by item 1 of [Corollary 13](#cor13), so what remains to check is that projective space is proper over the base. And this reduces along base changes to $\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ alone.

::: Theorem 15
A projective morphism between Noetherian schemes is a proper morphism, and a quasi-projective morphism is a separated, finite type morphism.
:::
::: Proof
The heart of the proof is that $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ is proper, which is obtained by directly verifying the criterion of [Theorem 11](#thm11). First, $\mathbb{P}^n_\mathbb{Z}$ is obtained by gluing $n+1$ affine charts

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

along $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$. Here since $\x_i/\x_i=1$, each $U_i$ is the spectrum of an $n$-variable polynomial ring over $\mathbb{Z}$. In particular each $U_i$ is the spectrum of a Noetherian ring and the number of charts is finite, so $\mathbb{P}^n_\mathbb{Z}$ is a Noetherian scheme, and $\pi$ is finite type. ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14))

That $\pi$ is separated is checked directly on charts. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$ is covered by affine open subsets $U_i\times_\mathbb{Z}U_j$ and $p_1\circ\Delta=p_2\circ\Delta=\id$, so $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$. Now looking at the ring homomorphism induced by $\Delta$ on this,

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \longrightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

the right-hand side is generated over $\mathbb{Z}$ by the $\x_l/\x_i$ and $(\x_j/\x_i)^{-1}=\x_i/\x_j$; the former come from the first factor and the latter from the second, so this morphism is surjective. Therefore $\Delta$ is a closed embedding on each $U_i\times_\mathbb{Z}U_j$, and since closed embeddings are affine-local on the target ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)), $\Delta$ itself is a closed embedding.

Since $\Spec \mathbb{Z}$ is a terminal object in the category of schemes, giving an outer square for a valuation ring $A$ and $K=\Frac(A)$ is the same as giving a morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$. Uniqueness of liftings follows from $\pi$ being separated and [Theorem 6](#thm6), so we only need to show existence. Since $\Spec K$ is a single point, the image of the given morphism lies in some chart $U_i$, and hence this morphism corresponds to a ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \longrightarrow K.$$

Let the image of $\x_j/\x_i$ be $a_j\in K$; then $a_i=1$. Now defining $s\preceq t$ on $K^\times$ by $t/s\in A$, by definition of a valuation ring for any $s,t$ either $s\preceq t$ or $t\preceq s$, and if $t/s\in A$ and $r/t\in A$ then $r/s=(r/t)(t/s)\in A$, so $\preceq$ is a total preorder on $K^\times$. Since $a_i=1\neq 0$, the finite set $\{a_j \mid a_j\neq 0\}$ is nonempty, so we can choose a minimal element $a_k$ of this set. That is, for all $j$,

$$b_j:=a_j/a_k\in A.$$

(If $a_j=0$ then $b_j=0\in A$.) In particular $b_k=1$, so the ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \longrightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

is defined, and this gives a morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$. To show this is a lifting, we need to check that its composition with $A\hookrightarrow K$ equals the originally given morphism. Since $a_k\neq 0$, the original ring homomorphism sends $\x_k/\x_i$ to the unit $a_k$ of $K$, and hence the image of the original morphism lies in $D(\x_k/\x_i)=U_i\cap U_k$. Then on $U_k$, by the transition relation

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1}$$

this morphism is given by $\x_j/\x_k\mapsto a_j/a_k=b_j$, so restricting the $\Spec A \rightarrow U_k$ constructed above to $\Spec K$ gives exactly the same thing. That is, existence in the criterion holds, and by [Theorem 11](#thm11), $\pi$ is proper.

For any Noetherian scheme $Y$, we have $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$. This is because when $Y=\Spec B$, the chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$ of $\mathbb{P}^n_B$ coincides with $U_i\times_{\Spec\mathbb{Z}}\Spec B$, and for general $Y$ we glue these. Therefore by [Corollary 13](#cor13), $\mathbb{P}^n_Y \rightarrow Y$ is proper, and in particular finite type, so $\mathbb{P}^n_Y$ is a Noetherian scheme.

Now if $\varphi:X \rightarrow Y$ is projective, then $\varphi$ is a composition of a closed embedding $X\hookrightarrow \mathbb{P}^n_Y$ and the projection $\mathbb{P}^n_Y \rightarrow Y$. ([Definition 1](#def1)) A closed embedding is proper and the composition of two proper morphisms is proper ([Corollary 13](#cor13)), so $\varphi$ is proper.

Finally, let $\varphi:X \rightarrow Y$ be quasi-projective, and decompose it as $\varphi=\psi\circ\iota$ where $\iota: X \rightarrow X'$ is an open immersion and $\psi:X' \rightarrow Y$ is a projective morphism. ([Definition 1](#def1)) By what we just showed, $\psi$ is proper, hence separated and finite type. Meanwhile an open immersion is separated, and the composition of two separated morphisms is separated ([Corollary 8](#cor8)), so $\varphi$ is separated. Also an open immersion is locally of finite type, and since $X$ is Noetherian, the preimage by $\iota$ of any affine open subset of $X'$ is quasi-compact as an open subset of a Noetherian space. That is, $\iota$ is finite type ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14)), and since the composition of two finite type morphisms is finite type, $\varphi$ is also finite type.
:::

Thus we obtain the classical consequence of the criterion. Since a proper morphism is a closed map by definition, the image of a morphism going out from a projective scheme is always closed.

::: Corollary 16
For a projective scheme $X$ over $\mathbb{K}$, a separated finite type $\mathbb{K}$-scheme $Z$, and a $\mathbb{K}$-morphism $\varphi:X \rightarrow Z$, the set $\varphi(X)$ is a closed subset of $Z$.
:::
::: Proof
The structure morphism $X \rightarrow \Spec\mathbb{K}$ is projective, so by [Theorem 15](#thm15) it is proper, and $Z \rightarrow \Spec\mathbb{K}$ is separated by assumption. Then applying item 5 of [Corollary 13](#cor13) to $\varphi$ and $Z \rightarrow \Spec\mathbb{K}$, we obtain that $\varphi$ is proper, and in particular $\varphi$ is a closed map, so from $X$ itself being a closed subset of $X$, $\varphi(X)$ is closed.
:::

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
