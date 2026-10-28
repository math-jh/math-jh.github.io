---
title: "Valuation Rings"
description: "We define separated and proper morphisms, and examine how they generalize the Hausdorff and compactness conditions from topology to algebraic geometry. The structure of discrete valuation rings is also discussed."
excerpt: "Valuative criteria for separatedness and properness"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/valuative_criteria
sidebar: 
    nav: "scheme_theory-en"

date: 2024-05-24
weight: 15
translated_at: 2026-07-27T19:45:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-27T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In this post, we define separated morphisms and proper morphisms. In previous posts, we defined open subschemes ([§Schemes, ⁋Definition 4](/en/math/scheme_theory/schemes#def4){: data-lid="vg435" }), and examined closed embeddings, the closed subschemes obtained from them, and ideal sheaves ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2){: data-lid="8omth" }, [Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5){: data-lid="ol61e" }). To these, we add the following concepts.

::: Definition 1
Let a scheme morphism $\varphi: X \rightarrow Y$ be given.

1. If $\varphi$ induces an isomorphism between $X$ and an open subscheme of $Y$, we call $\varphi$ an *open embedding*.
2. We say $\varphi$ is *projective* if for some suitable $n$, $\varphi$ can be factored as a composition of a closed embedding and a projection $X\hookrightarrow \mathbb{P}^n_Y \rightarrow Y$. ([§Projective Space and the Proj Construction](/en/math/scheme_theory/projective_schemes){: data-lid="upx9k" })
3. We say $\varphi$ is *quasi-projective* if it can be factored as a composition of a suitable open embedding $X \rightarrow X'$ and a projective morphism $X' \rightarrow Y$.
:::

The first definition is obvious, and the second and third definitions also treat [\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 3](/en/math/algebraic_varieties/projective_varieties#def3){: data-lid="u6fm8" } and [\[Algebraic Varieties\] §Quasi-Projective Varieties, ⁋Definition 1](/en/math/algebraic_varieties/quasi_projective_varieties#def1){: data-lid="e5gu1" } in the relative version, that is, in $\Sch_{/Y}$.

Before beginning the main discussion, it is worth examining the following example.

::: Example 2
Let a ring $A$ be a discrete valuation ring as a subring of a field $K$. That is, for any $x\in K^\times$, either $x\in A$ or $x^{-1}\in A$, $A$ is Noetherian, and its maximal ideal $\mathfrak{m}$ is principal. ([\[Commutative Algebra\] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5){: data-lid="5yi44" }) Since any $x\in K^\times$ is expressed as a ratio of elements of $A$ via $x$ or $x^{-1}$, we have $K=\Frac(A)$. Also, $A$ is a local ring having $\mathfrak{m}$ as its unique maximal ideal ([\[Commutative Algebra\] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6){: data-lid="0zgoz" }), and if we choose a uniformizer $\pi$, any $f\in K^\times$ is uniquely expressed as $f=\pi^nu$ for an integer $n$ and a unit $u$ ([\[Commutative Algebra\] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8){: data-lid="pcvzo" }); hence all nonzero ideals of $A$ are of the form $(\pi^n)$. In particular, $A$ is a principal ideal domain, and its only prime ideals are $(0)$ and $\mathfrak{m}=(\pi)$.

From this, $\Spec A$ consists of the two points $(0)$, $\mathfrak{m}$, and since

$$Z((0))=\{(0),\mathfrak{m}\},\quad Z(\mathfrak{m})=\{\mathfrak{m}\}$$

the only nontrivial open subset of $\Spec A$ is

$$D(\pi)=\Spec A\setminus Z(\mathfrak{m})=\{(0)\}$$

Then by [§Affine Scheme, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6){: data-lid="rg5e6" },

$$\mathcal{O}(D(\pi))\cong A_\pi\cong K$$

Of course, $\mathcal{O}(\Spec A)\cong A$.

Meanwhile, the two points of $\Spec A$ can be examined geometrically through their respective residue fields. Using [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-lid="k291x" }, from

$$\mathcal{O}_{(0)}\cong A_{(0)}\cong K,\qquad \mathcal{O}_\mathfrak{m}\cong A_\mathfrak{m}$$

we obtain

$$\kappa((0))=K, \qquad \kappa(\mathfrak{m})=A_\mathfrak{m}/\mathfrak{m}A_\mathfrak{m}\cong A/\mathfrak{m}$$
:::

Let us examine the example a bit more geometrically. Since $Z((0))=\Spec A$, the closure of $(0)$ is all of $\Spec A$, so $(0)$ is the generic point of this space. This situation is seen particularly intuitively when, for a curve $C$ and a point $p$ on it, $\mathcal{O}_{C,p}$ is a discrete valuation ring. Specifically, the stalk

$$\mathcal{O}_{C,p}=\varinjlim_{U\ni p} \mathcal{O}(U)$$

can be viewed as germs at the point $p$, and the generic point $(0)$ of $\Spec \mathcal{O}_{C,p}$ is precisely what contains this data. Then the remaining (unique) point $\mathfrak{m}$ corresponds exactly to the point $p$, and the fact that this is a specialization of $(0)$ reflects that in defining a germ we examine neighborhoods arbitrarily close to $p$.

In this picture, the role of $\Spec K$ is revealed by looking at the function side. The functions on $\Spec A$ are $A$ itself, that is, germs regular at $p$, and the functions on the unique nontrivial open set $D(\pi)=\{(0)\}$, namely the elements of $K\cong A_\pi$, allow the form $f=\pi^nu$ up to negative order $n$. ([\[Commutative Algebra\] §Divisors, ⁋Proposition 8](/en/math/commutative_algebra/divisors#prop8){: data-lid="6ebri" }, item 2) That is, this means functions having a pole at $p$ but of finite order, namely functions regular on the entire neighborhood except at $p$ alone; thus $\Spec K$ is the space that removes the center $p$ from this germ, losing the information of $p$ while retaining only information about a neighborhood of $p$, and the canonical morphism $\Spec K \rightarrow \Spec A$ is exactly the inclusion morphism defined by this picture.

Then a morphism $\Spec K \rightarrow X$ is a germ of a curve with a missing point going into $X$, and extending this to $\Spec A \rightarrow X$ amounts to recovering that missing point inside $X$ and gluing the curve back together, that is, finding the limit of the curve. That this extension exists in at most one way is separatedness, and that it exists in exactly one way is properness; this is the content of the two criteria we will see. Topologically, this is the algebro-geometric analogue of the facts that limits are unique in a Hausdorff space ([\[Topology\] §Hausdorff Spaces, ⁋Proposition 4](/en/math/topology/Hausdorff_spaces#prop4){: data-lid="s2kho" }), and limits always exist in a compact space ([\[Topology\] §Compactness and Convergence of Filters, ⁋Lemma 18](/en/math/topology/filter_convergence#lem18){: data-lid="ul5hp" }).

## Separated Morphisms

As examined above, the idea of a separated morphism is that, given a germ of a curve, there exists at most one way to fill in its center point $p$. To describe this, the following definition is needed.

::: Definition 3
For a scheme morphism $\varphi:X \rightarrow Y$, the unique morphism induced by two copies of $\id_X$ via the universal property of the fiber product, namely the dashed arrow $\Delta: X \rightarrow X \times_Y X$ in the following diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-1.svg width="13.58em" alt="diagonal_morphism" %}

is called the *diagonal morphism* of $\varphi$. ([§Fiber Products, ⁋Definition 1](/en/math/scheme_theory/fiber_products#def1){: data-lid="sp26e" }) If $\Delta$ is a closed embedding, we call $\varphi$ *separated*, and say $X$ is *separated* over $Y$. If $X$ is separated over $\Spec \mathbb{Z}$, we simply call $X$ a *separated* scheme.
:::

When we need to clarify which morphism's diagonal it is, instead of $\Delta$ we write $\Delta_{X/Y}$. From the definition, for the two projections $\pi_1,\pi_2: X\times_YX \rightarrow X$, it is obvious that $\pi_1\circ\Delta=\pi_2\circ\Delta=\id_X$. Also, $\Delta$ is injective, and since the restriction of $\pi_1$ to $\Delta(X)$ gives a continuous inverse to $\Delta$, $\Delta$ is always a homeomorphism onto $\Delta(X)$. Therefore, asking whether $\Delta$ is a closed embedding amounts to asking whether $\Delta(X)$ is closed and whether all functions on $X$ are obtained by restricting functions on $X\times_YX$. ([§Closed Subschemes, ⁋Definition 2](/en/math/scheme_theory/closed_subschemes#def2){: data-lid="0cxe5" })

As explained above, in algebraic geometry we regard separatedness as the property replacing Hausdorff. Recalling that for a topological space $T$ to be Hausdorff was equivalent to the diagonal being closed in $T\times T$ ([\[Topology\] §Hausdorff Spaces, ⁋Lemma 5](/en/math/topology/Hausdorff_spaces#lem5){: data-lid="vh1dz" }), it is natural to expect the following proposition.

::: Proposition 4
$\varphi:X \rightarrow Y$ is separated if and only if, under the diagonal morphism $\Delta: X \rightarrow X\times_YX$, the image of $X$ is a closed set.
:::
::: Proof
By definition, if $\varphi$ is separated, it is obvious that $\Delta(X)$ is closed. Therefore, we assume that $\Delta(X)$ is closed and show that $\Delta$ is a closed embedding. As seen earlier, $\Delta$ is always a homeomorphism onto $\Delta(X)$, so together with the assumption the topological condition is already secured, and we only need to show that $\mathcal{O}_{X\times_YX} \rightarrow \Delta_\ast \mathcal{O}_X$ is surjective. This can be checked on stalks.

First, there is nothing to check at points $q\notin \Delta(X)$. From the assumption that $\Delta(X)$ is closed, there exists an open neighborhood of $q$, $W$, such that $W\cap\Delta(X)=\emptyset$, and then $\Delta^{-1}(W)=\emptyset$, so

$$(\Delta_\ast\mathcal{O}_X)(W)=\mathcal{O}_X(\emptyset)=0$$

and thus $(\Delta_\ast\mathcal{O}_X)_q=0$. Since the open neighborhoods to be chosen below cannot cover points outside $\Delta(X)$, this is precisely where the assumption is actually used.

Now consider points of the form $\Delta(p)$. For any $p\in X$, we can choose an open affine subset containing $p$, $U$, and if necessary restrict $U$ so that $\varphi(U)$ is contained in some open affine subset of $Y$, $V$. Then $U\times_VU$, as an open subset of $X\times_YX$, is an open neighborhood of $\Delta(p)$, and since $\pi_1\circ\Delta=\pi_2\circ\Delta=\id_X$, we have $\Delta^{-1}(U\times_VU)=U$. On this, $\Delta: U \rightarrow U\times_VU$ is a closed embedding by [Lemma 5](#lem5){: data-lid="6k7kg" } below, so $\mathcal{O}_{U\times_VU} \rightarrow \Delta_\ast\mathcal{O}_U$ is surjective, and in particular the morphism between stalks at $\Delta(p)$ is surjective.
:::

Then from this we obtain the following.

::: Lemma 5
Any morphism $\varphi:X \rightarrow Y$ between affine schemes is always separated.
:::
::: Proof
If $X=\Spec A$ and $Y=\Spec B$, then $X\times_YX=\Spec(A\otimes_BA)$ ([§Fiber Products, ⁋Lemma 2](/en/math/scheme_theory/fiber_products#lem2){: data-lid="km0dh" }), and $\Delta$ is induced by the ring homomorphism

$$A\otimes_BA \rightarrow A;\quad a\otimes a'\mapsto aa'$$

This ring homomorphism sends $a\otimes 1$ to $a$, so it is surjective, and hence $\Delta$ is a closed embedding. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="mk5eq" })
:::

An example of a non-separated scheme is the line with double origin constructed in [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10){: data-lid="vabl4" }. For convenience, let us call this scheme $X$ and the two charts constituting it $X_1=\Spec\mathbb{K}[\x_1]$, $X_2=\Spec\mathbb{K}[\x_2]$. Since these are glued along $D(\x_1)$ and $D(\x_2)$ by identifying $\x_1$ and $\x_2$, the intersection of the two charts is

$$X_1\cap X_2=X\setminus \{0_1,0_2\}=\Spec\mathbb{K}[t,1/t]$$

with the two origins removed. Here, $t$ is the coordinate to which both $\x_1$ and $\x_2$ correspond under this gluing. Since $X$ is a scheme over $\mathbb{K}$, what we consider is $X\times_\mathbb{K}X$, and since the fiber product can be computed by restricting each factor to open subsets ([§Fiber Products, ⁋Lemma 4](/en/math/scheme_theory/fiber_products#lem4){: data-lid="7y891" }), this is obtained by gluing the four charts

$$X_a\times_\mathbb{K}X_b=\Spec\bigl(\mathbb{K}[\x_a]\otimes_\mathbb{K}\mathbb{K}[\x_b]\bigr)=\Spec\mathbb{K}[\x_a,\x_b]\cong \mathbb{A}^2_\mathbb{K}\qquad (a,b\in \{1,2\})$$

In this process, points where both coordinates are nonzero become the same point in all four charts and appear once each; points where only one coordinate is zero appear twice; and the origin where both coordinates are zero appears four times.

Now since $\pi_1\circ\Delta=\pi_2\circ\Delta=\id_X$, we have $\Delta^{-1}(X_a\times_\mathbb{K}X_b)=X_a\cap X_b$. That is, if $a=b$, this is all of $X_a$, and by [Lemma 5](#lem5){: data-lid="hs77d" }, $\Delta$ is a closed embedding on it; in particular, the two origins of $X$ go to $(0_1,0_1)$ and $(0_2,0_2)$ among the four origins. On the other hand, if $a\neq b$, then $\Delta$ is the morphism induced on $X_1\cap X_2=\Spec\mathbb{K}[t,1/t]$ by the ring homomorphism

$$\mathbb{K}[\x_1,\x_2] \rightarrow \mathbb{K}[t,1/t];\qquad \x_1,\x_2\mapsto t$$

so within the chart $X_1\times_\mathbb{K}X_2\cong \mathbb{A}^2_\mathbb{K}$, the image $\Delta(X)$ is $Z(\x_1-\x_2)\cap D(\x_1)$, the diagonal with the origin removed. The closure of this set is the entire diagonal $Z(\x_1-\x_2)$, and its origin is exactly $(0_1,0_2)$, so $(0_1,0_2)$ does not belong to $\Delta(X)$ while belonging to its closure. Therefore $\Delta(X)$ is not closed, and by [Proposition 4](#prop4){: data-lid="94env" }, $X$ is not separated. This space is also a standard example of a space that is not topologically Hausdorff.

Now let us see the criterion for separatedness. Unlike in [Example 2](#ex2){: data-lid="6d5yq" }, the criterion is required for all valuation rings, which need not be discrete, that is, for all subrings $A$ of a field $K$ satisfying only the condition that for any $x\in K^\times$, either $x\in A$ or $x^{-1}\in A$. ([\[Commutative Algebra\] §Divisors, ⁋Definition 5](/en/math/commutative_algebra/divisors#def5){: data-lid="385vf" }) Also, below, $\iota:\Spec K \rightarrow \Spec A$ always denotes the morphism induced by the inclusion $A\hookrightarrow K$.

::: Theorem 6
For a Noetherian scheme $X$ and a scheme morphism $\varphi:X \rightarrow Y$, $\varphi$ is separated if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, whenever any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the outer square of the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

are given, there is at most one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
That the outer square is given means morphisms $\alpha:\Spec K \rightarrow X$ and $\beta: \Spec A \rightarrow Y$ are given such that $\varphi\circ \alpha=\beta\circ \iota$ holds, and a lifting of this square means a morphism satisfying $\gamma\circ \iota=\alpha$ and $\varphi\circ \gamma=\beta$, namely $\gamma:\Spec A \rightarrow X$.

Throughout the proof we use two standard facts. The first is the existence theorem for valuation rings: whenever a field $K$ and a local subring $\mathcal{O}$ inside it are given, there exists, with $\Frac(A)=K$, $\mathcal{O}\subseteq A$, and $\mathfrak{m}_A\cap \mathcal{O}=\mathfrak{m}_\mathcal{O}$, a valuation ring $A$. In this case we say $A$ *dominates* $\mathcal{O}$, and the existence of such $A$ is obtained by applying Zorn's lemma to the collection of local subrings dominating $\mathcal{O}$ in $K$. The second is that for a field $K$, a morphism $\Spec K \rightarrow X$ corresponds bijectively to a pair of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. This follows from the case $X=\Spec B$ where a ring homomorphism $B \rightarrow K$ gives a pair of its kernel prime ideal $\mathfrak{p}$ and $\kappa(\mathfrak{p}) \rightarrow K$, and for the general case one chooses an affine open neighborhood of $x$.

First assume $\varphi$ is separated, and suppose two liftings $\gamma_1, \gamma_2$ of the above square are given. Since $\varphi\circ \gamma_1=\varphi\circ \gamma_2=\beta$, by the universal property of the fiber product there exists a unique $\theta:\Spec A \rightarrow X\times_YX$ such that $\pi_1\circ \theta=\gamma_1$ and $\pi_2\circ \theta=\gamma_2$. Here $\pi_1,\pi_2$ are the two projections. Now since $\Delta$ is a closed embedding, the base change

$$Z=\Spec A\times_{X\times_YX}X \rightarrow \Spec A$$

is also a closed embedding. That closed embeddings are stable under base change is obtained affine-locally from the fact that the base change of $B \rightarrow B/\mathfrak{b}$ is $C \rightarrow C\otimes_B(B/\mathfrak{b})\cong C/\mathfrak{b}C$, which remains surjective. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="fstql" })

Meanwhile, $\pi_1\circ \theta\circ \iota=\gamma_1\circ \iota=\alpha$ and $\pi_2\circ \theta\circ \iota=\gamma_2\circ \iota=\alpha$, and $\pi_1\circ \Delta\circ \alpha=\alpha$ and $\pi_2\circ\Delta\circ \alpha=\alpha$, so by uniqueness in the universal property, $\theta\circ \iota=\Delta\circ \alpha$. Therefore $\iota$ factors through the pullback $Z$, and in particular the image of $Z \rightarrow \Spec A$ is a closed set containing the image of $\iota$, that is, the zero ideal $(0)$ of $A$. Since $A$ is a domain, $(0)$ is the generic point of $\Spec A$ ([§The Topology of Schemes, ⁋Example 5](/en/math/scheme_theory/topology_of_schemes#ex5){: data-lid="4yxw9" }), and therefore the only closed subset of $\Spec A$ containing $(0)$ is $\Spec A$ itself. Then $Z$, as a closed subscheme of $\Spec A$, is for some ideal $\mathfrak{a}\subseteq A$ of the form $\Spec(A/\mathfrak{a})$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="2idz8" }), and that its image is the whole of $\Spec A$ means that $\mathfrak{a}$ is contained in every prime ideal of $A$, that is, that

$$\mathfrak{a}\subseteq \mathfrak{N}(A)=(0)$$

holds. The last equality comes from the fact that $A$ is a domain. Therefore $Z \rightarrow \Spec A$ is an isomorphism, which means that $\theta$ factors through $\Delta$, that is, for some $\gamma:\Spec A \rightarrow X$, we have $\theta=\Delta\circ \gamma$. Then

$$\gamma_1=\pi_1\circ \theta=\pi_1\circ \Delta\circ \gamma=\gamma,\qquad \gamma_2=\pi_2\circ \theta=\pi_2\circ\Delta\circ \gamma=\gamma$$

so $\gamma_1=\gamma_2$. In this direction the assumption that $X$ is Noetherian is not used.

Conversely, assume that for any square there exists at most one lifting. By [Proposition 4](#prop4){: data-lid="e3n7c" }, it suffices to show that $\Delta(X)$ is a closed subset of $X\times_YX$.

First we observe that every point of $\cl(\Delta(X))$ is a specialization of some point of $\Delta(X)$. Since $X$ is a Noetherian scheme, it is also Noetherian as a topological space ([§The Topology of Schemes, ⁋Definition 14](/en/math/scheme_theory/topology_of_schemes#def14){: data-lid="w96fv" }), and thus has finitely many irreducible components $X_1,\ldots, X_r$. ([\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13){: data-lid="y6vhy" }) Each $X_i$ is an irreducible closed subset, so if, meeting $X_i$, we choose an affine open subset $U=\Spec C\subseteq X$, then $X_i\cap U$ is an irreducible closed subset of $U$ and hence has a generic point $\eta_i$ ([§The Spectrum, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16){: data-lid="9tzoq" }); since $X_i\cap U$ is dense in $X_i$, we have $\cl(\{\eta_i\})=X_i$, that is, $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$. Now since $\Delta$ is continuous, $\Delta(X)\subseteq \bigcup_{i=1}^r \cl(\{\Delta(\eta_i)\})$, and the right-hand side is a finite union hence closed; conversely each $\Delta(\eta_i)$ belongs to $\Delta(X)$, so we obtain

$$\cl(\Delta(X))=\bigcup_{i=1}^r\cl(\{\Delta(\eta_i)\})$$

That is, any point of $\cl(\Delta(X))$ is a specialization of some $\Delta(\eta_i)\in \Delta(X)$. ([§The Topology of Schemes, ⁋Definition 2](/en/math/scheme_theory/topology_of_schemes#def2){: data-lid="2jflw" }) Therefore if we show that $\Delta(X)$ is closed under specialization, then $\Delta(X)=\cl(\Delta(X))$, and the proof is complete.

Let $\xi=\Delta(x)\in \Delta(X)$ and $\eta\in\cl(\{\xi\})$. Giving the reduced scheme structure to the closed set $T=\cl(\{\xi\})$ ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14){: data-lid="u2358" }), $T$ is an integral scheme with generic point $\xi$. Containing $\eta$, choose an affine open subset $\Spec B\subseteq T$. Since the generic point belongs to every nonempty open set, $\Spec B$ also contains $\xi$, and $B$ is a domain with $\xi$ corresponding to the zero ideal of $B$, so

$$K:=\kappa(\xi)=\mathcal{O}_{T,\xi}=\Frac(B), \qquad \mathcal{O}:=\mathcal{O}_{T,\eta}=B_\mathfrak{q}\subseteq K$$

where $\mathfrak{q}$ is the prime ideal corresponding to $\eta$. In particular $\mathcal{O}$ is a local domain with $\Frac(\mathcal{O})=K$. By the existence theorem cited above, if we choose, dominating $\mathcal{O}$, a valuation ring of $K$, denoted $A$, the morphism induced by the local homomorphism $\mathcal{O} \rightarrow A$

$$\chi:\Spec A \rightarrow \Spec \mathcal{O} \rightarrow T \hookrightarrow X\times_YX$$

sends the generic point of $\Spec A$, $(0)$, to $\xi$ and the closed point $\mathfrak{m}_A$ to $\eta$.

Now let $\gamma_1=\pi_1\circ \chi$, $\gamma_2=\pi_2\circ \chi$, and since $\varphi\circ \pi_1=\varphi\circ \pi_2$, consider the well-defined $\omega=\varphi\circ \gamma_1=\varphi\circ \gamma_2:\Spec A \rightarrow Y$. As seen in the proof of [Proposition 4](#prop4){: data-lid="z4612" }, if we choose, around $x$, an affine open neighborhood $U$, and containing $\varphi(U)$, an affine open subset of $Y$, denoted $V$, then $U\times_VU$ is an open neighborhood in $X\times_YX$ of $\xi$, and on it $\Delta$ is a closed embedding ([Lemma 5](#lem5){: data-lid="ibtdv" }), so the morphism between stalks $\mathcal{O}_{X\times_YX,\xi} \rightarrow \mathcal{O}_{X,x}$ is surjective and thus $\kappa(\xi) \rightarrow \kappa(x)$ is also surjective. Meanwhile since $\pi_1\circ\Delta=\id_X$, the composition $\kappa(x) \rightarrow \kappa(\xi) \rightarrow \kappa(x)$ is the identity map, and therefore the two morphisms are inverse isomorphisms of each other. That is, $K=\kappa(\xi)\cong\kappa(x)$. Under this identification, letting the canonical morphism defined by the point $x$ and $\kappa(x)\cong K$ be $\alpha:\Spec K \rightarrow X$, then $\Delta\circ \alpha$ is the canonical morphism defined by the point $\xi$ and $\kappa(\xi)\cong K$, and this equals $\chi\circ \iota$. Indeed, $\chi\circ \iota$ has $\xi$ as image and induces the identity map of $\kappa(\xi)=\Frac(\mathcal{O})=K$ on residue fields. Therefore

$$\gamma_1\circ \iota=\pi_1\circ \chi\circ \iota=\pi_1\circ \Delta\circ \alpha=\alpha,\qquad \gamma_2\circ \iota=\pi_2\circ \chi\circ \iota=\pi_2\circ\Delta\circ \alpha=\alpha$$

and $\varphi\circ \gamma_1=\varphi\circ \gamma_2=\omega$, so $\gamma_1$ and $\gamma_2$ are two liftings of the square given by $\alpha$ and $\omega$. By assumption $\gamma_1=\gamma_2$, and then since $\Delta\circ \gamma_1$ and $\chi$, when composed with $\pi_1, \pi_2$, give $\gamma_1$ and $\gamma_2=\gamma_1$ respectively, by the universal property of the fiber product we have $\chi=\Delta\circ \gamma_1$. Therefore

$$\eta=\chi(\mathfrak{m}_A)=\Delta(\gamma_1(\mathfrak{m}_A))\in \Delta(X)$$

and $\Delta(X)$ is closed under specialization. Combined with the previous observation, $\Delta(X)=\cl(\Delta(X))$, so $\Delta(X)$ is a closed set, and by [Proposition 4](#prop4){: data-lid="w9o38" }, $\varphi$ is separated.
:::

Intuitively, $\Spec A$ consists of the generic point $(0)$ and the closed point $\mathfrak{m}_A$ to which it specializes, and among these, the generic point must go, by the condition $\gamma\circ \iota=\alpha$, to the image of $\alpha$, namely $\xi$; thus giving a lifting $\gamma:\Spec A \rightarrow X$ is specifying a point with $\eta\in \cl(\{\xi\})$, namely $\eta=\gamma(\mathfrak{m}_A)$, that is, choosing a limit of the given germ inside $X$. Therefore, that there is at most one lifting means that a single germ does not split into two different limits, and as the proof shows, this is precisely the topological condition that $\Delta(X)$ is closed under specialization. Conversely, the existence theorem for valuation rings used in the proof realizes any specialization inside $X$ as such a germ, and this is why the criterion is required for arbitrary valuation rings, not just discrete ones. However, the $\Spec$ of a general valuation ring has prime ideals forming longer chains, departing from the two-point picture of [Example 2](#ex2){: data-lid="tkfvl" }; if $Y$ is Noetherian and $\varphi$ is a finite type morphism, then the above theorem can be replaced by one for arbitrary discrete valuation rings, so that picture survives intact. We omit the proof of this fact as it cannot be done in our current state.

Let us check this picture in an actual example.

::: Example 7
Earlier we checked that the line with double origin $X$ is not separated using [Proposition 4](#prop4){: data-lid="181gq" }, but using [Theorem 6](#thm6){: data-lid="x8rqr" } the same fact is revealed directly in terms of limits of curves. Let $A=\mathbb{K}[t]_{(t)}$ be a discrete valuation ring with uniformizer $t$ and $K=\Frac(A)=\mathbb{K}(t)$, and let $Y=\Spec\mathbb{K}$. Now consider the morphism defined by the ring homomorphism $\mathbb{K}[\x_1] \rightarrow K$, $\x_1\mapsto t$, namely $\alpha:\Spec K \rightarrow X$. Since $t$ is a unit of $K$, the image of $\alpha$ lies in the open set where the two charts overlap. Since everything is over $\mathbb{K}$, $\alpha$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form the outer square.

Now as before let the two charts be $X_1=\Spec\mathbb{K}[\x_1]$, $X_2=\Spec\mathbb{K}[\x_2]$, and define two morphisms into them,

$$\gamma_1:\Spec A \rightarrow X_1\subseteq X,\qquad \gamma_2:\Spec A \rightarrow X_2\subseteq X$$

by $\x_1\mapsto t$ and $\x_2\mapsto t$ respectively; both are well-defined since $t\in A$. Since the two charts are glued by identifying $\x_1$ and $\x_2$ outside the origin, we have $\gamma_1\circ \iota=\gamma_2\circ \iota=\alpha$, so both are liftings of this square. However, $\gamma_1$ sends $\mathfrak{m}_A=(t)$ to the origin $0_1$ of the first chart, while $\gamma_2$ sends it to the origin $0_2$ of the second chart, so $\gamma_1\neq \gamma_2$. That is, the germ of a curve missing a point has two limits, and this is why $X$ is not separated.
:::

Meanwhile, from [Theorem 6](#thm6){: data-lid="wqkn1" } we obtain the following.

::: Corollary 8
For Noetherian schemes,

1. Open embeddings and closed embeddings are both separated.
2. The composition of two separated morphisms is separated.
3. Separated morphisms are preserved under base change.
4. Separated morphisms are preserved under fiber products.
5. If $\varphi:X \rightarrow Y$, $\psi:Y \rightarrow Z$ are scheme morphisms and $\psi\circ \varphi$ is a separated morphism, then $\varphi$ is also a separated morphism.
:::
::: Proof
Item 1 is checked directly from the definition. If $\varphi$ is a closed embedding, then for each affine open subset $V=\Spec B$ of $Y$, we have $\varphi^{-1}(V)=\Spec A$ and $B \rightarrow A$ is surjective ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="5rcoh" }), and collecting all such $V$, the $\varphi^{-1}(V)\times_V\varphi^{-1}(V)$ cover $X\times_YX$. On each of these, $\Delta$ is a closed embedding by the computation of [Lemma 5](#lem5){: data-lid="3kf0n" }, and since closed embeddings are affine-local on the target, $\Delta$ itself is a closed embedding. If $\varphi$ is an open embedding, viewing $X$ as an open subscheme of $Y$, consider affine open subsets $V=\Spec B$ of $Y$ and basic open subsets $\Spec B_b$ of $X$ contained in them. Then the $\Spec B_b\times_V\Spec B_{b'}$ cover $X\times_YX$, and since

$$B_b\otimes_BB_{b'}\cong B_{bb'}=\mathcal{O}(\Spec B_b\cap \Spec B_{b'})$$

$\Delta$ is an isomorphism on each and in particular a closed embedding.

The rest is obtained from the criterion of [Theorem 6](#thm6){: data-lid="w0ats" }. That is, we only need to check that the uniqueness of liftings is inherited.

For item 2, suppose an outer square $\alpha:\Spec K \rightarrow X$, $\beta:\Spec A \rightarrow Z$ for $\psi\circ \varphi$ and two liftings $\gamma_1,\gamma_2:\Spec A \rightarrow X$ are given. Then $\varphi\circ \gamma_1$ and $\varphi\circ \gamma_2$ are two liftings of the square for $\psi$ given by $\alpha' = \varphi\circ \alpha$ and $\beta$, so $\varphi\circ \gamma_1=\varphi\circ \gamma_2$, and then $\gamma_1,\gamma_2$ are two liftings of the square for $\varphi$ given by $\alpha$ and $\varphi\circ \gamma_1$, so $\gamma_1=\gamma_2$.

For item 3, for $Y' \rightarrow Y$ and $X'=X\times_YY'$, $\varphi':X' \rightarrow Y'$, suppose a square for $\varphi'$ and its two liftings $\gamma_1',\gamma_2':\Spec A \rightarrow X'$ are given. Their compositions with $X' \rightarrow X$ are two liftings of the square for $\varphi$ and are therefore equal to each other, and since the two compositions to $Y'$ are also the same morphism given by the square, by the uniqueness in the universal property of the fiber product, $\gamma_1'=\gamma_2'$.

For item 5, if a square for $\varphi$ and two liftings $\gamma_1,\gamma_2$ are given, composing $\Spec A \rightarrow Y$ with $\psi$ yields a square for $\psi\circ \varphi$, and since $\gamma_1,\gamma_2$ are its two liftings, $\gamma_1=\gamma_2$.

Finally, for item 4, for separated morphisms $\varphi:X \rightarrow Y$, $\varphi':X' \rightarrow Y'$ between $S$-schemes, $\varphi\times \varphi'$ decomposes as the composition

$$X\times_SX' \rightarrow Y\times_SX' \rightarrow Y\times_SY'$$

and since the two morphisms are base changes of $\varphi$ and $\varphi'$ respectively, this follows from items 3 and 2.
:::

In particular, using items 2 and 5 together, we see that when $Y$ is a separated scheme, a $Y$-scheme $X$ is a separated scheme if and only if its structure morphism $X \rightarrow Y$ is separated. Since an affine scheme is always a separated scheme by [Lemma 5](#lem5){: data-lid="5oqw5" }, for instance, for a scheme over an affine scheme, separatedness can be determined by looking only at the structure morphism.

Separatedness is also used to determine when two morphisms are equal. Suppose given a reduced scheme $X$, a separated scheme $Y$, and two morphisms $\varphi,\psi: X \rightarrow Y$ that agree on a dense open subset $W$ of $X$. Then for the morphism $\theta: X \rightarrow Y\times_{\Spec \mathbb{Z}}Y$ induced by $\varphi$ and $\psi$, the locus where $\varphi$ and $\psi$ agree is given by the base change of $\Delta$ along $\theta$, and since the base change of a closed embedding is again a closed embedding (proof of [Theorem 6](#thm6){: data-lid="r5pq9" }), this is a closed subscheme of $X$. Since this closed subscheme contains $W$ and is topologically all of $X$, the ideal sheaf defining it is contained in $\mathfrak{N}(A)=0$ on each affine open subset $\Spec A$ of $X$ ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="4pwe3" }), and therefore $\varphi=\psi$. Applying this to [§Properties of Scheme Morphisms, ⁋Definition 22](/en/math/scheme_theory/properties_of_scheme_morphisms#def22){: data-lid="10i9t" }, when $Y$ is separated and $X$ is reduced, the equivalence relation on rational maps becomes the condition that two representatives agree on all of $U\cap V$. In that post, this was verified for the case where $Y$ is affine, and since affine schemes are always separated, this is a special case of the argument above.

## Proper Morphisms

Now we turn to the property corresponding to compactness. In topology, we saw that compactness can be rewritten as the condition of being universally closed ([\[Topology\] §Proper Maps, ⁋Theorem 6](/en/math/topology/proper_maps#thm6){: data-lid="zoub8" }), and in algebraic geometry, this condition with products replaced by fiber products directly becomes the definition.

::: Definition 9
We say $\varphi:X \rightarrow Y$ is *universally closed* if $\varphi$ is a closed map and for any $Y' \rightarrow Y$, $X\times_Y Y' \rightarrow Y'$ is also closed. A separated, universally closed finite type morphism is called a *proper morphism*.
:::

Setting $Y'=Y$, the second condition includes the first, so the only substantive condition is that every base change is a closed map. Meanwhile, since we work within the category of Noetherian schemes in this section, when checking universal closedness below we only consider base changes $Y' \rightarrow Y$ for Noetherian schemes. That the condition for arbitrary $Y'$ follows from this is obtained by a limit argument writing the coordinate ring as a filtered colimit of finitely generated subalgebras after restricting $Y'$ to be affine, but since this is beyond the scope of this post, we omit it.

Since a proper morphism requires both the separated condition and the universally closed condition, the criterion also splits into two pieces. Since [Theorem 6](#thm6){: data-lid="n623r" } tested separatedness by the uniqueness of liftings, what remains is that the existence of liftings tests universal closedness.

::: Proposition 10
For a finite type scheme morphism $\varphi:X \rightarrow Y$ between Noetherian schemes, $\varphi$ is universally closed if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, whenever any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the outer square of the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

are given, there exists at least one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
As in the proof of [Theorem 6](#thm6){: data-lid="aiq7l" }, write the outer square as $\alpha:\Spec K \rightarrow X$, $\beta:\Spec A \rightarrow Y$, $\iota:\Spec K \rightarrow \Spec A$, and continue using the two standard facts cited in that proof. That is, a local subring in a field $K$ is always dominated by a valuation ring with $\Frac(A)=K$, namely $A$, and a morphism $\Spec K \rightarrow X$ is the same as a pair consisting of a point $x\in X$ and a field homomorphism $\kappa(x) \rightarrow K$. To this we add the following maximality of valuation rings. If a valuation ring of $K$, $A$, is dominated by a local subring $\mathcal{O}\subseteq K$, then $\mathcal{O}=A$. Indeed, if $c\in\mathcal{O}$ is not $0$ and $c\notin A$, then by definition of a valuation ring $c^{-1}\in A$, and since $c\notin A$, $c^{-1}$ is not a unit of $A$. That is, $c^{-1}\in\mathfrak{m}_A\subseteq \mathfrak{m}_\mathcal{O}$, but since $c\in\mathcal{O}$, $c^{-1}$ is a unit of $\mathcal{O}$, a contradiction. Therefore $\mathcal{O}\subseteq A$, and since $A\subseteq\mathcal{O}$ by definition of domination, $\mathcal{O}=A$.

First, suppose $\varphi$ is universally closed and construct a lifting. Base changing along $\beta$, we obtain $X_A=X\times_Y\Spec A$ and the projection $\pi:X_A \rightarrow \Spec A$, and $\pi$ is a closed map. ([Definition 9](#def9){: data-lid="lxunk" }) Meanwhile, by the universal property of the fiber product, $\alpha$ and $\iota$ induce a morphism over $\Spec A$, $\tilde{\alpha}:\Spec K \rightarrow X_A$, and if we find a section of the form $\Spec A \rightarrow X_A$ of $\pi$ extending $\tilde{\alpha}$, then projecting this to $X$ gives the desired lifting.

Let $\xi\in X_A$ be the point that is the image of $\tilde{\alpha}$, and give the reduced scheme structure to $Z=\cl(\{\xi\})$. ([§Closed Subschemes, ⁋Definition 14](/en/math/scheme_theory/closed_subschemes#def14){: data-lid="digg0" }) Since $\pi\circ\tilde{\alpha}=\iota$, $\pi(\xi)$ is the generic point of $\Spec A$, $(0)$, and since $\pi$ is a closed map, $\pi(Z)$ is a closed set containing $(0)$, namely all of $\Spec A$. Therefore, there exists a point with $\pi(z)=\mathfrak{m}_A$, namely $z\in Z$.

Let us examine the residue fields. The morphism that $\pi\circ \tilde{\alpha}=\iota$ induces at $(0)$, namely $\kappa((0))=K \rightarrow K$, is the identity map; since this is the composition of the morphism induced by $\pi$, $K\rightarrow\kappa(\xi)$, and the morphism induced by $\tilde{\alpha}$, $\kappa(\xi) \rightarrow K$, the two morphisms are isomorphisms that are inverses of each other. That is, $\kappa(\xi)\cong K$. Then, since $Z$ is an integral scheme with generic point $\xi$, as in the proof of [Theorem 6](#thm6){: data-lid="0skwb" } we choose an affine open subset containing $z$ to find that

$$\mathcal{O}:=\mathcal{O}_{Z,z}\subseteq \kappa(\xi)=K,\qquad \Frac(\mathcal{O})=K$$

holds. Also, the morphism induced by $\pi\vert_Z$, $A=\mathcal{O}_{\Spec A,\mathfrak{m}_A} \rightarrow \mathcal{O}_{Z,z}$, is a local homomorphism, and since the morphism it induces at the generic point, $K \rightarrow \kappa(\xi)=K$, is the identity, this morphism is an inclusion between subrings of $K$. That is, $\mathcal{O}$ is a local subring dominating $A$ in $K$, and by the maximality above, $\mathcal{O}_{Z,z}=A$.

Then we obtain the canonical morphism $\Spec A=\Spec\mathcal{O}_{Z,z} \rightarrow Z \hookrightarrow X_A$, and since its composition with $\pi$ corresponds to the identity map on $A$ at the ring level, it is a section of $\pi$. The restriction of this section to $\Spec K$ has $\xi$ as its image and induces the identity map on $\kappa(\xi)=K$ on residue fields, so it equals $\tilde{\alpha}$. Therefore, projecting this section to $X$, we obtain a morphism satisfying $\gamma\circ \iota=\alpha$ and $\varphi\circ \gamma=\beta$, namely $\gamma:\Spec A \rightarrow X$.

Conversely, assume that the existence part holds. Following the convention stated after [Definition 9](#def9){: data-lid="sw2of" }, we only consider base changes $Y' \rightarrow Y$ by Noetherian schemes.

First, the existence part is stable under base change. Suppose $Y' \rightarrow Y$, $X'=X\times_YY'$, and $\varphi':X' \rightarrow Y'$ are given, and suppose $\Spec K \rightarrow X'$ and $\Spec A \rightarrow Y'$ form an outer square for $\varphi'$. Composing these with $X' \rightarrow X$ and $Y' \rightarrow Y$ gives an outer square for $\varphi$, so there exists a lifting $\gamma:\Spec A \rightarrow X$, and $\gamma$ together with $\Spec A \rightarrow Y'$ yields a unique $\gamma':\Spec A \rightarrow X'$ by the universal property. The morphisms $\gamma'\circ \iota$ and the given $\Spec K \rightarrow X'$ are equal because their compositions with $X' \rightarrow X$ and $X' \rightarrow Y'$ are respectively equal; hence $\gamma'$ is a lifting for $\varphi'$. Meanwhile, finite type morphisms are stable under base change, and a finite type scheme over a Noetherian scheme is again Noetherian, so $X'$ is Noetherian and $\varphi'$ is of finite type. Therefore, if we show that whenever a Noetherian scheme $X$ and a finite type morphism $\varphi:X \rightarrow Y$ satisfy the existence part of the criterion, $\varphi$ is a closed map, applying this to all base changes will complete the proof.

To show this, choose a closed subset of $X$, $T$, and give it the reduced scheme structure. Since the closed embedding $T\hookrightarrow X$ is a finite morphism ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4){: data-lid="alkct" }), it is of finite type, and hence $T$ is a Noetherian scheme and $\varphi\vert_T:T \rightarrow Y$ is also of finite type. Also, $\varphi\vert_T$ inherits the existence part of the criterion. Indeed, if $\Spec K \rightarrow T$ and $\Spec A \rightarrow Y$ form a square for $\varphi\vert_T$, applying the criterion to $\Spec K \rightarrow T\hookrightarrow X$ gives a lifting $\gamma_0:\Spec A \rightarrow X$. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so $\gamma_0(\Spec A)\subseteq \cl(\{\gamma_0((0))\})\subseteq T$, and since $\Spec A$ is reduced, $\gamma_0$ factors through $T$. Here, the last fact is obtained as follows. Suppose that for a reduced scheme $S$, the image of a morphism $\psi:S \rightarrow X$ is contained in a closed set $T$, and choose an affine open subset of $X$, $\Spec B$, and an affine open subset of $\psi^{-1}(\Spec B)$, $\Spec R$. If $T\cap \Spec B=Z(\mathfrak{b})$ ($\mathfrak{b}$ a radical ideal), then the reduced structure of $T$ on it is $\Spec (B/\mathfrak{b})$, and the corresponding ring homomorphism $\phi:B \rightarrow R$ satisfies $\mathfrak{b}\subseteq \phi^{-1}(\mathfrak{p})$ for any prime ideal $\mathfrak{p}\subseteq R$, so

$$\phi(\mathfrak{b})\subseteq \bigcap_{\mathfrak{p}\in\Spec R}\mathfrak{p}=\mathfrak{N}(R)=(0)$$

holds. That is, $\phi$ uniquely factors through $B/\mathfrak{b}$, and the local factorizations thus obtained glue by uniqueness.

Therefore, it suffices to show that $\varphi(T)=\varphi\vert_T(T)$ is a closed set, and ultimately it suffices to show that for a finite type morphism $\varphi:X \rightarrow Y$ (where $X$ is Noetherian) satisfying the existence part of the criterion, the image $\varphi(X)$ is closed.

We first show that $\varphi(X)$ is closed under specialization. Let $y_1=\varphi(x_1)\in \varphi(X)$ and $y_0\in\cl(\{y_1\})$. Giving the reduced scheme structure to $W=\cl(\{y_1\})$, $W$ is an integral scheme with generic point $y_1$, and as before, $\mathcal{O}=\mathcal{O}_{W,y_0}$ is a local domain with $\Frac(\mathcal{O})=\kappa(y_1)$. Now let $K=\kappa(x_1)$, and via the field homomorphism induced by $\varphi$, $\kappa(y_1)\hookrightarrow K$, view $\mathcal{O}$ as a local subring of $K$. Then there exists, dominating $\mathcal{O}$, a valuation ring of $K$, namely $A$, and from this, two morphisms

$$\Spec A \rightarrow \Spec\mathcal{O} \rightarrow W\hookrightarrow Y,\qquad \alpha:\Spec K \rightarrow X$$

are obtained. Here $\alpha$ is the canonical morphism defined by the point $x_1$ and $\kappa(x_1)=K$. These two form an outer square, because both compositions to $\Spec K \rightarrow Y$ are the canonical morphism defined by the point $y_1$ and the field homomorphism $\kappa(y_1)\hookrightarrow K$. By existence in the criterion, there exists a lifting $\gamma_0:\Spec A \rightarrow X$, and since $\Spec A \rightarrow \Spec\mathcal{O}$ comes from a local homomorphism, $\mathfrak{m}_A$ maps to $\mathfrak{m}_\mathcal{O}$, that is, $y_0$. Therefore $\varphi(\gamma_0(\mathfrak{m}_A))=y_0$ and $y_0\in \varphi(X)$.

Finally, we repeat verbatim the topological observation from the proof of [Theorem 6](#thm6){: data-lid="o4z6c" }. If we let the generic points of the irreducible components of $X$, denoted $X_1,\ldots,X_r$, be $\eta_1,\ldots,\eta_r$, then since $X=\bigcup_{i=1}^r\cl(\{\eta_i\})$,

$$\cl(\varphi(X))=\bigcup_{i=1}^r\cl(\{\varphi(\eta_i)\})$$

holds, and therefore every point of $\cl(\varphi(X))$ is a specialization of a point of $\varphi(X)$. Since we showed above that $\varphi(X)$ is closed under specialization, $\varphi(X)=\cl(\varphi(X))$.
:::

Then, combining the two pieces, we obtain the criterion for properness.

::: Theorem 11
For a finite type scheme morphism $\varphi:X \rightarrow Y$ between Noetherian schemes, $\varphi$ is proper if and only if for any valuation ring $A$ and its quotient field $K=\Frac(A)$, whenever any scheme morphisms $\Spec A \rightarrow Y$, $\Spec K \rightarrow X$ and the outer square of the following commutative diagram

{% diagram Math/Scheme_Theory/Valuative_Criteria-2.svg width="8.34em" alt="valuative_criterion" %}

are given, there exists exactly one $\Spec A \rightarrow X$ making the whole diagram commute.
:::
::: Proof
Since $\varphi$ is assumed to be of finite type, by [Definition 9](#def9){: data-lid="y3pol" } $\varphi$ is proper if and only if $\varphi$ is separated and universally closed. By [Theorem 6](#thm6){: data-lid="pfj5u" }, $\varphi$ is separated if and only if any outer square has at most one lifting, and by [Proposition 10](#prop10){: data-lid="evq3p" }, $\varphi$ is universally closed if and only if any outer square has at least one lifting. Both conditions holding together is precisely that every square has exactly one lifting.
:::

It is good to see what the criterion looks like when it fails. If [Example 7](#ex7){: data-lid="9lx40" } was the case where uniqueness fails, the following is the case where existence fails.

::: Example 12
$\mathbb{A}^1_\mathbb{K}=\Spec\mathbb{K}[\x]$ is not proper over $\Spec\mathbb{K}$. Choose $A=\mathbb{K}[t]_{(t)}$ and $K=\Frac(A)=\mathbb{K}(t)$, and consider the morphism $\alpha:\Spec K \rightarrow \mathbb{A}^1_\mathbb{K}$ defined by the ring homomorphism

$$\mathbb{K}[\x] \rightarrow K;\qquad \x\mapsto 1/t$$

Since everything is over $\mathbb{K}$, $\alpha$ and the structure morphism $\Spec A \rightarrow \Spec\mathbb{K}$ form the outer square. If a lifting $\gamma:\Spec A \rightarrow \mathbb{A}^1_\mathbb{K}$ exists, it corresponds to a ring homomorphism $\mathbb{K}[\x] \rightarrow A$, and the condition $\gamma\circ \iota=\alpha$ means the composition of this homomorphism with $A\hookrightarrow K$ sends $\x$ to $1/t$. That is, $1/t\in A$ must hold, but since $t$ is a uniformizer of $A$, this is impossible. Therefore no lifting exists, and by [Theorem 11](#thm11){: data-lid="a9w1f" }, $\mathbb{A}^1_\mathbb{K} \rightarrow \Spec\mathbb{K}$ is not proper.

Geometrically, this $\alpha$ is a germ of a curve escaping to infinity from the origin, and the criterion reads off directly that this limit does not exist in $\mathbb{A}^1_\mathbb{K}$. Doing the same calculation in $\mathbb{P}^1_\mathbb{K}$, $1/t$ becomes $t$ in the chart corresponding to infinity, so a lifting exists, and this is generalized in [Theorem 15](#thm15){: data-lid="jd08w" }.
:::

Similarly, the following corollary holds.

::: Corollary 13
For Noetherian schemes,

1. A closed embedding is proper.
2. The composition of proper morphisms is proper. 
3. Proper morphisms are preserved under base change.
4. Proper morphisms are preserved under fiber products.
5. If $\varphi:X \rightarrow Y$ and $\psi:Y \rightarrow Z$ are scheme morphisms, $\psi$ is separated, and $\psi\circ \varphi$ is a proper morphism, then $\varphi$ is also a proper morphism.
:::
::: Proof
For item 1, a closed embedding is separated by item 1 of [Corollary 8](#cor8){: data-lid="rgpb4" }, and since it is a finite morphism ([§Closed Subschemes, ⁋Proposition 4](/en/math/scheme_theory/closed_subschemes#prop4){: data-lid="zx1p0" }), it is of finite type. Also, a closed embedding is a closed map and is stable under base change (proof of [Theorem 6](#thm6){: data-lid="4vyh4" }), so it is universally closed.

For item 2, separatedness is item 2 of [Corollary 8](#cor8){: data-lid="mp4yr" }, and since the composition of morphisms of finite type is of finite type, it suffices to show that it is universally closed. Given $Z' \rightarrow Z$, since $X\times_ZZ'=X\times_Y(Y\times_ZZ')$, the two morphisms in

$$X\times_ZZ' \rightarrow Y\times_ZZ' \rightarrow Z'$$

are the base changes of $\varphi$ and $\psi$ respectively, and thus both are closed maps. Since the composition of closed maps is a closed map, $X\times_ZZ' \rightarrow Z'$ is also closed.

For item 3, separatedness is item 3 of [Corollary 8](#cor8){: data-lid="nkost" }, finite type is stability under base change, and universally closed follows immediately from the definition from the fact that a base change of a base change is again a base change. Next, for item 4, we may apply the same decomposition as in item 4 of [Corollary 8](#cor8){: data-lid="t17og" } to items 2 and 3.

Finally, consider item 5. Consider the graph morphism $\Gamma_\varphi:X \rightarrow X\times_ZY$ induced by $\id_X$ and $\varphi$; then $\varphi=\pi_2\circ\Gamma_\varphi$. Here, the square formed by $\Gamma_\varphi$ and $\varphi\times\id_Y: X\times_ZY \rightarrow Y\times_ZY$ is a cartesian square with base $\Delta_{Y/Z}:Y \rightarrow Y\times_ZY$. Indeed, for any $T$, matching two morphisms to $Y\times_ZY$ amounts to choosing, among pairs $\alpha:T \rightarrow X$ and $\beta:T \rightarrow Y$, one such that $\varphi\circ \alpha=\beta$, and such a pair is determined by $\alpha$ alone. Then, since $\Delta_{Y/Z}$ is a closed embedding by the assumption that $\psi$ is separated, $\Gamma_\varphi$ is also a closed embedding, and by item 1 it is proper. Meanwhile, $\pi_2:X\times_ZY \rightarrow Y$ is the base change of $\psi\circ \varphi$ along $\psi$, so by item 3 it is proper. Therefore, by item 2, $\varphi=\pi_2\circ\Gamma_\varphi$ is proper.
:::

The reason the assumption that $\psi$ is separated is included in item 5 is that the justification for $\Gamma_\varphi$ being a closed embedding in the proof is precisely that $\Delta_{Y/Z}$ is a closed embedding. Without this assumption, the guarantee that $\Gamma_\varphi$ is a closed embedding disappears and the argument does not work. Since such an assumption was not necessary in item 5 of [Corollary 8](#cor8){: data-lid="oyrqc" }, one should note that the two items have different forms.

Since the first of the results above is often used, it is useful to examine it in a little more detail. First, since it is obvious that a closed embedding is a monomorphism, by the first result of the corollary above a closed embedding is a proper monomorphism. What is important is that the converse of this statement also holds: that is, a proper monomorphism is precisely a closed embedding. However, since this claim requires Zariski's main theorem in its proof, we omit its proof.

Meanwhile, this first result can also be viewed as a special case of the following. This is the most typical example showing how the criterion is actually used, where existence follows from the single fact that a valuation ring is integrally closed.

::: Corollary 14
A finite morphism between Noetherian schemes is proper.
:::
::: Proof
A finite morphism $\varphi:X \rightarrow Y$ is an affine morphism, so for any affine open subset $V\subseteq Y$, $\varphi^{-1}(V)$ is affine, and hence by [Lemma 5](#lem5){: data-lid="pvdpg" } and the affine-local criterion for closed embeddings ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="wadgf" }), $\varphi$ is separated. Also, a finite morphism is of finite type. ([§Properties of Scheme Morphisms, ⁋Proposition 15](/en/math/scheme_theory/properties_of_scheme_morphisms#prop15){: data-lid="jgfwg" }) Therefore, by [Theorem 11](#thm11){: data-lid="8wfql" }, it suffices to check the existence of a lifting.

Suppose an outer square $\alpha:\Spec K \rightarrow X$, $\beta:\Spec A \rightarrow Y$ is given. Every point of $\Spec A$ is a specialization of the generic point $(0)$ and morphisms preserve specialization, so if we choose an affine open subset $V=\Spec B$ of $Y$ containing $\beta(\mathfrak{m}_A)$, then $V$ also contains $\beta((0))$ and hence $\beta$ factors through $V$. Then the image of $\alpha$ lies in $\varphi^{-1}(V)=\Spec C$, and $C$ is finitely generated as a $B$-module. Now the problem becomes, given the following ring homomorphisms

$$B \rightarrow A,\qquad C \rightarrow K$$

to construct $C \rightarrow A$ compatible with them.

Since any $c\in C$ is integral over $B$, it satisfies

$$c^n+b_{n-1}c^{n-1}+\cdots+b_0=0$$

for suitable $b_i\in B$. Applying $C \rightarrow K$ to this equation, the image of $c$ is integral over the image of $B$, and since the image of $B$ lies in $A$, the image of $c$ is integral over $A$. But a valuation ring is always integrally closed ([\[Commutative Algebra\] §Divisors, ⁋Proposition 6](/en/math/commutative_algebra/divisors#prop6){: data-lid="rxxtj" }, item 2), so the image of $c$ belongs to $A$. That is, $C \rightarrow K$ factors through $A$, and this gives the desired lifting.
:::

The same criterion gives a much larger result. A projective morphism is by definition a composition of a closed embedding and a projection $\mathbb{P}^n_Y \rightarrow Y$ ([Definition 1](#def1){: data-lid="2nr2q" }), and since the closed embedding part is already handled by item 1 of [Corollary 13](#cor13){: data-lid="f125a" }, ultimately the only thing to check is that projective space is proper over the base. And via base change, this reduces to $\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ alone.

::: Theorem 15
A projective morphism between Noetherian schemes is a proper morphism, and a quasi-projective morphism is a separated, finite type morphism.
:::
::: Proof
The heart of the proof is that $\pi:\mathbb{P}^n_\mathbb{Z} \rightarrow \Spec\mathbb{Z}$ is proper, which is obtained by directly verifying the criterion of [Theorem 11](#thm11){: data-lid="cmkgi" }. First, $\mathbb{P}^n_\mathbb{Z}$ is obtained by gluing $n+1$ affine charts

$$U_i=\Spec \mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\qquad (i=0,\ldots,n)$$

along $U_i\cap U_j=D(\x_j/\x_i)\subseteq U_i$. Here since $\x_i/\x_i=1$, each $U_i$ is the spectrum of an $n$-variable polynomial ring over $\mathbb{Z}$. In particular each $U_i$ is the spectrum of a Noetherian ring and the number of charts is finite, so $\mathbb{P}^n_\mathbb{Z}$ is a Noetherian scheme, and $\pi$ is finite type. ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14){: data-lid="ucjii" })

That $\pi$ is separated is checked directly on charts. $\mathbb{P}^n_\mathbb{Z}\times_\mathbb{Z}\mathbb{P}^n_\mathbb{Z}$ is covered by affine open subsets $U_i\times_\mathbb{Z}U_j$ and $\pi_1\circ\Delta=\pi_2\circ\Delta=\id$, so $\Delta^{-1}(U_i\times_\mathbb{Z}U_j)=U_i\cap U_j$. Now looking at the ring homomorphism induced by $\Delta$ on this,

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]\otimes_\mathbb{Z}\mathbb{Z}[\x_0/\x_j,\ldots,\x_n/\x_j] \rightarrow \mathcal{O}(U_i\cap U_j)=\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i]_{\x_j/\x_i}$$

the right-hand side is generated over $\mathbb{Z}$ by the $\x_l/\x_i$ and $(\x_j/\x_i)^{-1}=\x_i/\x_j$; the former come from the first factor and the latter from the second, so this morphism is surjective. Therefore $\Delta$ is a closed embedding on each $U_i\times_\mathbb{Z}U_j$, and since closed embeddings are affine-local on the target ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="4xuyx" }), $\Delta$ itself is a closed embedding.

Since $\Spec \mathbb{Z}$ is a terminal object in the category of schemes, giving an outer square for a valuation ring $A$ and $K=\Frac(A)$ is the same as giving a morphism $\Spec K \rightarrow \mathbb{P}^n_\mathbb{Z}$. Uniqueness of liftings follows from $\pi$ being separated and [Theorem 6](#thm6){: data-lid="63wcp" }, so we only need to show existence. Since $\Spec K$ is a single point, the image of the given morphism lies in some chart $U_i$, and hence this morphism corresponds to a ring homomorphism

$$\mathbb{Z}[\x_0/\x_i,\ldots,\x_n/\x_i] \rightarrow K$$

Let the image of $\x_j/\x_i$ be $a_j\in K$; then $a_i=1$. Now defining $s\preceq t$ on $K^\times$ by $t/s\in A$, by definition of a valuation ring for any $s,t$ either $s\preceq t$ or $t\preceq s$, and if $t/s\in A$ and $r/t\in A$ then $r/s=(r/t)(t/s)\in A$, so $\preceq$ is a total preorder on $K^\times$. Since $a_i=1\neq 0$, the finite set $\{a_j \mid a_j\neq 0\}$ is nonempty, so we can choose a minimal element $a_k$ of this set. That is, for all $j$,

$$b_j:=a_j/a_k\in A$$

holds. (If $a_j=0$ then $b_j=0\in A$.) In particular $b_k=1$, so the ring homomorphism

$$\mathbb{Z}[\x_0/\x_k,\ldots,\x_n/\x_k] \rightarrow A;\qquad \x_j/\x_k\mapsto b_j$$

is defined, and this gives a morphism $\Spec A \rightarrow U_k\subseteq\mathbb{P}^n_\mathbb{Z}$. To show this is a lifting, we need to check that its composition with $A\hookrightarrow K$ equals the originally given morphism. Since $a_k\neq 0$, the original ring homomorphism sends $\x_k/\x_i$ to the unit $a_k$ of $K$, and hence the image of the original morphism lies in $D(\x_k/\x_i)=U_i\cap U_k$. Then on $U_k$, by the transition relation

$$\x_j/\x_k=(\x_j/\x_i)\cdot(\x_k/\x_i)^{-1}$$

this morphism is given by $\x_j/\x_k\mapsto a_j/a_k=b_j$, so restricting the $\Spec A \rightarrow U_k$ constructed above to $\Spec K$ gives exactly the same thing. That is, existence in the criterion holds, and by [Theorem 11](#thm11){: data-lid="wmpbt" }, $\pi$ is proper.

For any Noetherian scheme $Y$, we have $\mathbb{P}^n_Y=\mathbb{P}^n_\mathbb{Z}\times_{\Spec\mathbb{Z}}Y$. This is because when $Y=\Spec B$, the chart $\Spec B[\x_0/\x_i,\ldots,\x_n/\x_i]$ of $\mathbb{P}^n_B$ coincides with $U_i\times_{\Spec\mathbb{Z}}\Spec B$, and for general $Y$ we glue these. Therefore by [Corollary 13](#cor13){: data-lid="71esr" }, $\mathbb{P}^n_Y \rightarrow Y$ is proper, and in particular finite type, so $\mathbb{P}^n_Y$ is a Noetherian scheme.

Now if $\varphi:X \rightarrow Y$ is projective, then $\varphi$ is a composition of a closed embedding $X\hookrightarrow \mathbb{P}^n_Y$ and the projection $\mathbb{P}^n_Y \rightarrow Y$. ([Definition 1](#def1){: data-lid="4u0j5" }) A closed embedding is proper and the composition of two proper morphisms is proper ([Corollary 13](#cor13){: data-lid="6gk09" }), so $\varphi$ is proper.

Finally, let $\varphi:X \rightarrow Y$ be quasi-projective, and decompose it as $\varphi=\psi\circ\lambda$ where $\lambda: X \rightarrow X'$ is an open embedding and $\psi:X' \rightarrow Y$ is a projective morphism. ([Definition 1](#def1){: data-lid="on8fx" }) By what we just showed, $\psi$ is proper, hence separated and finite type. Meanwhile an open embedding is separated, and the composition of two separated morphisms is separated ([Corollary 8](#cor8){: data-lid="pi4hp" }), so $\varphi$ is separated. Also an open embedding is locally of finite type, and since $X$ is Noetherian, the preimage by $\lambda$ of any affine open subset of $X'$ is quasi-compact as an open subset of a Noetherian space. That is, $\lambda$ is finite type ([§Properties of Scheme Morphisms, ⁋Definition 14](/en/math/scheme_theory/properties_of_scheme_morphisms#def14){: data-lid="i1ubv" }), and since the composition of two finite type morphisms is finite type, $\varphi$ is also finite type.
:::

Thus we obtain the classical consequence of the criterion. Since a proper morphism is a closed map by definition, the image of a morphism from a projective scheme is always closed.

::: Corollary 16
Over $\mathbb{K}$, for a projective scheme $X$, a separated finite type $\mathbb{K}$-scheme $Z$, and a $\mathbb{K}$-morphism $\varphi:X \rightarrow Z$, $\varphi(X)$ is a closed subset of $Z$.
:::
::: Proof
The structure morphism $X \rightarrow \Spec\mathbb{K}$ is projective, so by [Theorem 15](#thm15){: data-lid="tlmbe" } it is proper, and $Z \rightarrow \Spec\mathbb{K}$ is separated by assumption. Then applying part 5 of [Corollary 13](#cor13){: data-lid="25sfw" } to $\varphi$ and $Z \rightarrow \Spec\mathbb{K}$, we obtain that $\varphi$ is proper, and in particular, since $\varphi$ is a closed map, from the fact that $X$ itself is a closed subset of $X$, $\varphi(X)$ is closed.
:::

---

**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
