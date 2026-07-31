---
title: "Divisors and Linear Systems"
description: "We define Cartier divisors from closed subschemes cut out locally by one equation, and define Weil divisors and the divisor class group via codimension-one point valuations on a normal integral scheme, then compare the two divisor theories. We then obtain an isomorphism with the Picard group through the invertible sheaf defined by a Cartier divisor, and discuss linear systems and ample invertible sheaves."
excerpt: "Cartier and Weil divisors, the sheaf O_X(D), linear systems, and ampleness"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/divisors_and_linear_systems
sidebar: 
    nav: "scheme_theory-en"

date: 2026-07-27
weight: 17
translated_at: 2026-07-30T08:15:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-30T08:15:03+00:00
---
Having defined quasi-coherent sheaves and invertible sheaves in [§Quasi-coherent Sheaves](/en/math/scheme_theory/quasicoherent_sheaves), we can now begin computing divisors and line bundles on schemes, extending what we previously carried out on varieties. The goal of this post is to recast the material from [[Algebraic Varieties] §Divisors](/en/math/algebraic_varieties/divisors), [[Algebraic Varieties] §Line Bundles and Vector Bundles](/en/math/algebraic_varieties/line_bundles), and [[Algebraic Varieties] §Linear Systems](/en/math/algebraic_varieties/linear_systems) into the language of schemes.

## Cartier Divisors

In [[Algebraic Varieties] §Divisors](/en/math/algebraic_varieties/divisors), we defined Weil divisors first and examined Cartier divisors afterward. This was because Cartier divisors generalize the ambient spaces on which the theory operates by imposing the additional condition of being cut out locally by a single equation, thereby furnishing a divisor theory that remains valid on singular varieties. Since schemes are more general than varieties in many respects, we shall work primarily with Cartier divisors rather than Weil divisors from the outset.

::: Definition 1
A closed embedding $\iota: Z \hookrightarrow X$ is called an *effective Cartier divisor* if there exists an affine open cover $\{U_i=\Spec A_i\}$ of $X$ such that for each closed embedding

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

there is a non-zerodivisor $s_i\in A_i=\Gamma(U_i, \mathcal{O}_X)$ for which the two closed embeddings $\iota\vert^{U_i}$ and the vanishing scheme $Z(s_i)\hookrightarrow U_i$ of $s_i$ are isomorphic. ([§Closed Subschemes, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes#def7))
:::

The definition only requires each $s_i$ to be a non-zerodivisor, so $Z$ need not be reduced. In an algebraic variety, every closed subvariety is reduced, so to record multiplicities we had to attach formal integer coefficients using formal sums, as in [[Algebraic Varieties] §Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1). Now $Z$ itself carries multiplicity, so no such coefficients are needed in the effective case. For example, for $X=\Spec \mathbb{K}[\x]$ and $s=\x^2$, since $\x^2$ is a non-zerodivisor, $Z(s)=\Spec \mathbb{K}[\x]/(\x^2)$ is an effective Cartier divisor; it is a non-reduced scheme supported at a single point with multiplicity $2$.

The above definition is essentially a condition formulated on each open set and depends on the chosen cover, but it can be rephrased simply as a property of the ideal sheaf defining the closed subscheme. ([§Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5))

::: Proposition 2
A closed embedding $\iota: Z\hookrightarrow X$ is an effective Cartier divisor if and only if its ideal sheaf $\mathcal{I}_{Z/X}$ is an invertible sheaf. ([§Quasi-coherent Sheaves, ⁋Definition 12](/en/math/scheme_theory/quasicoherent_sheaves#def12))
:::
::: Proof
On an affine open subset $U=\Spec A$, the restriction of $\iota$ to the codomain is the closed embedding $Z(\mathfrak{a})\hookrightarrow U$ defined by the ideal $\mathfrak{a}=\mathcal{I}_{Z/X}(U)$, and two distinct ideals define two distinct closed subschemes. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3)) Hence $\iota\vert^U$ being isomorphic to $Z(s)\hookrightarrow U$ is equivalent to $\mathfrak{a}=(s)$.

Now consider the map $A \rightarrow (s)$, $a\mapsto as$ for $s\in A$. This is always surjective and its kernel is $\ann(s)$, so this map being an isomorphism is equivalent to $s$ being a non-zerodivisor. Now suppose $\iota$ is an effective Cartier divisor and choose the affine open cover $\{U_i=\Spec A_i\}$ from [Definition 1](#def1). Then $\mathcal{I}_{Z/X}(U_i)=(s_i)\cong A_i$. On the other hand, $\mathcal{I}_{Z/X}$ is a quasi-coherent sheaf ([§Quasi-coherent Sheaves, ⁋Proposition 18](/en/math/scheme_theory/quasicoherent_sheaves#prop18)) and quasi-coherence is affine-local, so by [§Quasi-coherent Sheaves, ⁋Theorem 10](/en/math/scheme_theory/quasicoherent_sheaves#thm10) we have $\mathcal{I}_{Z/X}\vert_{U_i}\cong \widetilde{\mathcal{I}_{Z/X}(U_i)}$. Therefore the above isomorphism yields

$$\mathcal{I}_{Z/X}\vert_{U_i}\cong \widetilde{(s_i)}\cong \widetilde{A_i}=\mathcal{O}_{U_i}.$$

That is, $\mathcal{I}_{Z/X}$ is a locally free sheaf of rank $1$.

Conversely, suppose $\mathcal{I}_{Z/X}$ is an invertible sheaf. For any point $x$, choose an open neighborhood $V$ with $\mathcal{I}_{Z/X}\vert_V\cong \mathcal{O}_V$, and then choose an affine open subset $U=\Spec A$ inside $V$ containing $x$; then $\mathcal{I}_{Z/X}(U)\cong A$. Let $s$ be the image of $1\in A$ under this isomorphism; then $\mathcal{I}_{Z/X}(U)=(s)$ and $\ann(s)=0$, so $s$ is a non-zerodivisor. Such $U$'s cover $X$, so the condition of [Definition 1](#def1) is satisfied.
:::

The map $A\rightarrow \mathcal{I}_{Z/X}(U)$ used in the proof clearly separates the two requirements of [Definition 1](#def1). That this map is surjective means the ideal $\mathcal{I}_{Z/X}(U)$ is generated by a single element $s$, i.e., $Z$ is cut out by a single equation over $U$. In this case, the non-zerodivisor condition above becomes $\ann(s)=0$, and then this map is injective, yielding $\mathcal{I}_{Z/X}\vert_U\cong \mathcal{O}_U$. If we drop this non-zerodivisor condition, then each $s_i$ can be chosen as an arbitrary element of $A_i$, and the resulting condition is called *locally principal*. That is, an effective Cartier divisor is exactly a locally principal subscheme for which the local equations can be taken to be non-zerodivisors.

The most basic property of an effective Cartier divisor is that its codimension is always $1$.

::: Proposition 3
For an effective Cartier divisor $\iota:Z\hookrightarrow X$ on a locally Noetherian scheme $X$, every irreducible component of $Z$ has codimension $1$ in $X$.
:::
::: Proof
Since codimension is computed locally, it suffices to take one of the affine open covers $\{U_i=\Spec A_i\}$ from [Definition 1](#def1) and consider the case where $Z\cap U_i=Z(s_i)$ with $s_i\in A_i$ a non-zerodivisor. If an irreducible component $W$ of $Z$ meets $U_i$, then $W\cap U_i$ is an irreducible component of $Z(s_i)$. By [§Dimension, ⁋Proposition 12](/en/math/scheme_theory/dimension#prop12), the components of $Z(s_i)$ have codimension $0$ or $1$ in $U_i$; a component of codimension $0$ corresponds to an irreducible component of $U_i$ itself, i.e., to a minimal prime ideal $\mathfrak{p}$ of $A_i$. If $W\cap U_i$ were such a component, then $s_i$ would vanish on it, so $s_i\in \mathfrak{p}$. However, in a Noetherian ring a non-zerodivisor does not belong to any minimal prime ideal ([[Commutative Algebra] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)), contradicting the assumption that $s_i$ is a non-zerodivisor. Hence the codimension of $W\cap U_i$ is $1$, and by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8) the codimension of $W$ in $X$ is also $1$.
:::

The only place in the proof where the requirement that $s_i$ be a non-zerodivisor was used was to ensure that $s_i$ does not belong to any minimal prime ideal of $A_i$. Geometrically, this means $s_i$ does not vanish identically on any irreducible component of $X$. If we remove this requirement from [Definition 1](#def1), then the equation $s_i$ can swallow an entire component instead of cutting it, and then $Z$ becomes a component of $X$ itself rather than having codimension $1$. Let us confirm this situation in the following example.

::: Example 4
Let $X=\Spec \mathbb{K}[\x,\y]/(\x\y)$ be the union of the two coordinate axes in the plane, and let $Z=Z(\x)$. This is the vanishing scheme of the global section $\x$, so taking $X$ itself as the cover, we see that $Z\hookrightarrow X$ is locally principal.

However, this is not an effective Cartier divisor. Since $\mathbb{K}[\x,\y]/(\x\y,\x)\cong\mathbb{K}[\y]$, $Z$ is the $\y$-axis, which is one of the two irreducible components of $X$, so it has codimension $0$ in $X$. But by [Proposition 3](#prop3), every irreducible component of an effective Cartier divisor must have codimension $1$.

Algebraically, [Proposition 2](#prop2) says the same thing. No matter how we choose an affine open subset $U=\Spec A$ containing the origin, $U$ meets both coordinate axes, so $\y\neq 0$ in $A$, and $\x$, which generates $\mathcal{I}_{Z/X}(U)$, is a zerodivisor killing $\y$. Hence this ideal can never be a free module.
:::

The reason codimension did not behave as expected in the above example was that $\x$ was contained in a minimal prime ideal. By requiring an element to be a non-zerodivisor, we avoid not only such minimal prime ideals but all associated prime ideals. For example, in the scheme

$$A=\mathbb{K}[\x,\y]/(\x^2,\x\y)$$

we have $(\x^2,\x\y)=(\x)\cap(\x^2,\y)$, so $\Ass(A)=\{(\x),(\x,\y)\}$; this is the scheme with the origin embedded as an embedded point on the $\y$-axis. Here $\y$ does not belong to the unique minimal prime ideal $(\x)$, so $Z(\y)$ does not swallow any component and has codimension $1$, but $\x\y=0$ and $\x\neq 0$, so $\y$ is a zerodivisor with $\ann(\y)=(\x)$. Therefore $Z(\y)\hookrightarrow \Spec A$ has codimension $1$ but is not an effective Cartier divisor, which also means the converse of [Proposition 3](#prop3) does not hold in general.

In both examples, the problem was that the local ring at the relevant point was not even a domain. If we exclude this situation, the converse of [Proposition 3](#prop3) holds.

::: Proposition 5
Let $X$ be a locally Noetherian integral scheme that is factorial. ([§Algebraic Structure of Schemes, ⁋Definition 7](/en/math/scheme_theory/algebra_of_schemes#def7)) Then any integral closed subscheme $\iota:Z\hookrightarrow X$ of codimension $1$ is an effective Cartier divisor.
:::
::: Proof
Since $X$ is integral, for any affine open subset $U=\Spec A$, the ring $A$ is a Noetherian domain; in particular, every nonzero element of $A$ is a non-zerodivisor.

There is nothing to check at points not meeting $Z$. Since $Z$ is a closed set, such a point has an affine open neighborhood disjoint from $Z$, and on it $Z$ is $Z(1)=\emptyset$, so the condition of [Definition 1](#def1) is satisfied with $s=1$.

Now choose $z\in Z$ and an affine open subset $U=\Spec A$ containing $z$. Since $Z$ is integral, $\mathfrak{p}=\mathcal{I}_{Z/X}(U)$ is a prime ideal, and by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8), $Z$ having codimension $1$ means $\mathfrak{p}$ has codimension $1$. Let $\mathfrak{q}\supseteq \mathfrak{p}$ be the prime ideal corresponding to $z$; then by the factoriality assumption, $A_\mathfrak{q}=\mathcal{O}_{X,z}$ is a Noetherian local UFD, and $\mathfrak{p}A_\mathfrak{q}$ is a prime ideal of codimension $1$. Hence by part 1 of [[Commutative Algebra] §Homological Criterion for Regularity, ⁋Lemma 8](/en/math/commutative_algebra/homological_criterion_for_regularity#lem8), $\mathfrak{p}A_\mathfrak{q}$ is principal.

Let $\mathfrak{p}A_\mathfrak{q}=(t)$; since elements outside $\mathfrak{q}$ are units in $A_\mathfrak{q}$, choose $f\in A$ so that $t=f/1$. Since $\mathfrak{p}A_\mathfrak{q}\cap A=\mathfrak{p}$, we have $f\in \mathfrak{p}$. On the other hand, since $A$ is Noetherian, $\mathfrak{p}$ is generated by finitely many elements $p_1,\ldots, p_n$, and each $p_i/1$ lies in $(f)A_\mathfrak{q}$, so there exists $g_i\notin \mathfrak{q}$ with $g_ip_i\in (f)$. Setting $g=g_1\cdots g_n$, we have $g\notin\mathfrak{q}$ because $\mathfrak{q}$ is prime, and $\mathfrak{p}A_g=(f)$ in $A_g$.

Then $D(g)$ is an affine open neighborhood of $z$ on which $Z$ is $Z(f)$; since $A_g$ is a domain and $f\neq 0$, $f$ is a non-zerodivisor. The open sets obtained in this way cover $X$, so by [Definition 1](#def1), $\iota$ is an effective Cartier divisor.
:::

Thus, under the above hypotheses, the topological condition of codimension $1$ alone is enough to recover a single equation, and since it is known that any scheme all of whose local rings are regular local rings is factorial, this result holds in particular for regular objects. In general we cannot expect such a recovery, so we take the local equation data itself as our object and collect them together. Here each equation need not be a function on $U_i$; only its ratio on overlaps is controlled, and below $K(U)$ denotes the total quotient ring of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12).

::: Definition 6
A *Cartier divisor* on a locally Noetherian scheme $X$ is a datum $\{(U_i,f_i)\}$ consisting of an affine open cover $\{U_i\}$ of $X$ and elements $f_i\in K(U_i)^\times$ such that for any $i,j$, the ratio $f_i/f_j$ is a section of $\mathcal{O}_X^\times$ on $U_i\cap U_j$. Two data $\{(U_i,f_i)\}$ and $\{(V_j,g_j)\}$ represent the same Cartier divisor if for any $i,j$, the ratio $f_i/g_j$ is a section of $\mathcal{O}_X^\times$ on $U_i\cap V_j$. These form a group under addition

$$\{(U_i,f_i)\}+\{(V_j,g_j)\}=\{(W, (f_ig_j)\vert_W)\}$$

where $W$ ranges over affine open subsets contained in each $U_i\cap V_j$. We denote this group by $\CaDiv(X)$.
:::

This is the same definition as the one examined in [[Algebraic Varieties] §Divisors, ⁋Definition 12](/en/math/algebraic_varieties/divisors#def12), differing only in that each $f_i$ comes from $K(U_i)^\times$ for its own $U_i$ rather than from a single function field. The associated points of an open subset $W\subseteq U$ are those associated points of $U$ lying in $W$ ([§Algebraic Structure of Schemes, ⁋Definition 8](/en/math/scheme_theory/algebra_of_schemes#def8)), so there is a restriction $K(U)^\times\rightarrow K(W)^\times$, and through this we can refine data; hence below we also read data written on covers that are not affine in the same way.

A Cartier divisor for which each $f_i$ lies in $\Gamma(U_i,\mathcal{O}_X)$ is called *effective*, and one easily checks that this is compatible with the above equivalence relation. If $f_i$ lies in $\Gamma(U_i,\mathcal{O}_X)$ and $f_i/g_j$ is an invertible section on $U_i\cap V_j$, then $g_j=f_i\cdot(f_i/g_j)^{-1}$ is also a section of $\mathcal{O}_X$ there, and since such $U_i\cap V_j$ cover $V_j$, $g_j$ also lies in $\Gamma(V_j,\mathcal{O}_X)$. That this algebraically defined notion coincides with the one in [Definition 1](#def1) is the first result about $\CaDiv(X)$.

::: Proposition 7
For a locally Noetherian scheme $X$, effective Cartier divisors $\iota:Z\hookrightarrow X$ are in one-to-one correspondence with effective elements of $\CaDiv(X)$.
:::
::: Proof
Given an effective $D=\{(U_i,f_i)\}$. That $f_i\in \Gamma(U_i,\mathcal{O}_X)$ is an element of $K(U_i)^\times$ means $f_i$ is a non-zerodivisor. Considering the ideal $(f_i)$ on each $U_i$, since $f_i/f_j$ is a unit on the overlap, these define the same ideal sheaf on overlaps, and hence glue to a single closed subscheme $Z$ of $X$ by [§Closed Subschemes, ⁋Proposition 6](/en/math/scheme_theory/closed_subschemes#prop6). This $Z$ satisfies the condition of [Definition 1](#def1) by construction.

Conversely, given an effective Cartier divisor $\iota:Z\hookrightarrow X$ with data $\{(U_i,s_i)\}$ from [Definition 1](#def1). Since $s_i$ is a non-zerodivisor, $s_i\in K(U_i)^\times$. On overlaps, $\mathcal{I}_{Z/X}$ is generated by both $s_i$ and $s_j$, so at each point there is a local unit $u$ with $s_i=us_j$, and such $u$ is uniquely determined from $s_i$ and $s_j$ being non-zerodivisors and glues to a section over the entire overlap. Hence $\{(U_i,s_i)\}$ is an effective Cartier divisor. That the two constructions are mutual inverses is immediate since either way we are passing back and forth between elements that locally generate $\mathcal{I}_{Z/X}$.
:::

Henceforth we do not distinguish between an effective Cartier divisor and an effective element of $\CaDiv(X)$. A general Cartier divisor can be written locally on each $U_i$ as the ratio of two non-zerodivisors, so it is locally the difference of two effective Cartier divisors; in this sense $\CaDiv(X)$ is generated locally by the closed subschemes of [Definition 1](#def1).

We write $\divisor(f)$ for the Cartier divisor of the form $\{(X,f)\}$ defined by a single element $f\in K(X)^\times$ and call it a *principal divisor*. By definition a Cartier divisor is always given locally by a single function, so the issue here is whether this local data can be assembled into a single global function. Denoting the subgroup they form by $\Prin(X)$, we define the quotient group

$$\CaCl(X)=\CaDiv(X)/\Prin(X)$$

and call two Cartier divisors *linearly equivalent* if their difference is principal.

## $\mathcal{O}_X(D)$ and the Picard Group

The data $\{(U_i,f_i)\}$ of a Cartier divisor specifies a function on each piece and controls only the ratio on overlaps. This is exactly the way an invertible sheaf is described by local trivializations and transition functions, so we can associate an invertible sheaf to a divisor. In this section we assume $X$ is an *integral* Noetherian scheme. Then the local ring at the generic point, $K(X)$, is a field, and for any non-empty open set we have $\Gamma(V,\mathcal{O}_X)$ as a subring of it; hence below we can treat rational functions inside a single $K(X)$.

::: Definition 8
For an integral Noetherian scheme $X$ and a Cartier divisor $D=\{(U_i,f_i)\}$, we define the $\mathcal{O}_X$-module $\mathcal{O}_X(D)$ on $X$ by setting, for each non-empty open subset $V$,

$$\Gamma(V,\mathcal{O}_X(D))=\{g\in K(X)\mid gf_i\in \Gamma(V\cap U_i,\mathcal{O}_X)\text{ for all $i$}\}$$

and $\Gamma(\emptyset,\mathcal{O}_X(D))=0$. Here the restriction maps between non-empty open subsets are given by sending elements of $K(X)$ to themselves.
:::

This is what we already covered in [[Algebraic Varieties] §Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17): we constructed a line bundle using $f_i/f_j$ as transition functions and then verified that its sections are the rational functions satisfying $\divisor(g)+D\geq 0$. [Definition 8](#def8) also defines the sheaf $\mathcal{O}_X(D)$ in the same way; here $\Gamma(V,\mathcal{O}_X(D))$ is the collection of rational functions allowing poles only to the extent specified by $D$.

Since the condition in the definition is checked in a neighborhood of each point, $\mathcal{O}_X(D)$ is indeed a sheaf closed under multiplication by $\mathcal{O}_X$. Moreover this sheaf is independent of the choice of data representing $D$. If another datum $\{(V_j,g_j)\}$ gives the same Cartier divisor, then $f_i/g_j$ is an invertible section on the overlap, so $gf_i$ being a section of $\mathcal{O}_X$ and $gg_j$ being so are the same condition on each $V\cap U_i\cap V_j$. If $D$ is effective then $\mathcal{O}_X\subseteq \mathcal{O}_X(D)$, and for $-D$ we conversely get the sheaf of functions vanishing on $D$, i.e., the ideal sheaf of the closed subscheme given by [Proposition 7](#prop7).

::: Proposition 9
For an integral Noetherian scheme $X$ and Cartier divisors $D,D'$, the following hold.

1. $\mathcal{O}_X(D)$ is an invertible sheaf, and $\mathcal{O}_X(D)\vert_{U_i}$ is generated by $f_i^{-1}$.
2. Multiplication inside $K(X)$ gives an isomorphism $\mathcal{O}_X(D)\otimes_{\mathcal{O}_X}\mathcal{O}_X(D')\cong \mathcal{O}_X(D+D')$.
3. $\mathcal{O}_X(D)\cong \mathcal{O}_X$ if and only if $D$ is principal.
:::
::: Proof
For (1), for an open subset $V\subseteq U_i$, since $f_j=f_i\cdot(f_j/f_i)$ and $f_j/f_i$ is an invertible section on $U_i\cap U_j$, if $gf_i\in \Gamma(V,\mathcal{O}_X)$ then automatically $gf_j\in\Gamma(V\cap U_j,\mathcal{O}_X)$. Hence

$$\Gamma(V,\mathcal{O}_X(D))=f_i^{-1}\Gamma(V,\mathcal{O}_X)$$

and since $f_i\in K(X)^\times$, the map $g\mapsto gf_i$ is an isomorphism $\mathcal{O}_X(D)\vert_{U_i} \rightarrow \mathcal{O}_{U_i}$. Thus $\mathcal{O}_X(D)$ is a locally free sheaf of rank $1$.

For (2), letting $D'=\{(V_j,g_j)\}$ and computing $D+D'$ as $\{(U_i\cap V_j, f_ig_j)\}$, by (1) the three sheaves are on $U_i\cap V_j$ the free modules generated by $f_i^{-1}$, $g_j^{-1}$, and $(f_ig_j)^{-1}$ respectively. The multiplication map $\mathcal{O}_X(D)\otimes \mathcal{O}_X(D') \rightarrow \mathcal{O}_X(D+D')$ sends generator to generator, so it is an isomorphism on each piece and hence globally.

For (3), if $D=\divisor(h)$ then $\mathcal{O}_X(D)=h^{-1}\mathcal{O}_X\cong \mathcal{O}_X$. Conversely, given an isomorphism $\psi:\mathcal{O}_X \rightarrow \mathcal{O}_X(D)$, let $h=\psi(1)\in \Gamma(X,\mathcal{O}_X(D))\subseteq K(X)$. Then $h$ generates $\mathcal{O}_X(D)$ on each $U_i$, so comparing with (1), $h$ and $f_i^{-1}$ differ by a section of $\mathcal{O}_X^\times$, i.e., $f_i/h^{-1}=hf_i$ is an invertible section on $U_i$. Hence by the equivalence relation of [Definition 6](#def6), $\{(U_i,f_i)\}$ and $\{(X,h^{-1})\}$ define the same Cartier divisor, so $D=\divisor(h^{-1})$.
:::

By the above proposition, the correspondence $D\mapsto \mathcal{O}_X(D)$ gives a group homomorphism $\CaDiv(X)\rightarrow\Pic(X)$, and its kernel is exactly $\Prin(X)$. Hence we know that its image is isomorphic to $\CaCl(X)=\CaDiv(X)/\Prin(X)$. The following theorem ties this result together, showing that this correspondence is surjective and thus yields a canonical isomorphism $\CaCl(X)\cong \Pic(X)$.

::: Theorem 10
For an integral Noetherian scheme $X$, the map $D\mapsto \mathcal{O}_X(D)$ induces an isomorphism $\CaCl(X)\cong\Pic(X)$.
:::
::: Proof
By [Proposition 9](#prop9) the induced homomorphism is injective, so it suffices to show surjectivity. Given an invertible sheaf $\mathcal{L}$ and trivializations $\psi_i:\mathcal{O}_{U_i} \rightarrow \mathcal{L}\vert_{U_i}$. Since trivializations are preserved under restriction to open subsets, we may refine by covering each $U_i$ with affine open subsets and assume from the outset that $\{U_i\}$ is an affine open cover. Let $t_i=\psi_i(1)$ be the generating section of $\mathcal{L}$ over $U_i$. Then on overlaps $t_j=g_{ij}t_i$ for uniquely determined $g_{ij}\in \Gamma(U_i\cap U_j,\mathcal{O}_X)^\times$, and these satisfy $g_{ij}g_{jk}=g_{ik}$.

First observe that $g_{ii}=1$ and $g_{ji}=g_{ij}^{-1}$, fix a non-empty $U_{i_0}$, and set $f_i=g_{ii_0}\in \Gamma(U_i\cap U_{i_0},\mathcal{O}_X)^\times$. Since $X$ is integral, this is an element of $K(X)^\times$, and from the cocycle condition we have $f_i/f_j=g_{ii_0}g_{i_0j}=g_{ij}$ on $U_i\cap U_j\cap U_{i_0}$. But since $X$ is irreducible, this open set is dense in $U_i\cap U_j$, and $\Gamma(U_i\cap U_j,\mathcal{O}_X)$ embeds into $K(X)$, so this equality holds on all of $U_i\cap U_j$. In particular $f_i/f_j$ is an invertible section on the overlap, so $D=\{(U_i,f_i)\}$ is a Cartier divisor.

Now we show $\mathcal{O}_X(D)\cong \mathcal{L}$. By [Proposition 9](#prop9), $\mathcal{O}_X(D)\vert_{U_i}$ is generated by $f_i^{-1}$, so for $V\subseteq U_i$ with $gf_i\in \Gamma(V,\mathcal{O}_X)$, the map

$$\varphi_i:\mathcal{O}_X(D)\vert_{U_i} \rightarrow \mathcal{L}\vert_{U_i};\qquad g\mapsto (gf_i)\cdot t_i$$

is an isomorphism. On overlaps $t_i=g_{ji}t_j$ and $g_{ji}=f_j/f_i$, so

$$\varphi_i(g)=(gf_i)\cdot\frac{f_j}{f_i}t_j=(gf_j)\cdot t_j=\varphi_j(g)$$

and these glue to a single isomorphism $\mathcal{O}_X(D)\cong\mathcal{L}$.
:::

Thus, on an integral Noetherian scheme, dealing with invertible sheaves is the same as dealing with Cartier divisors up to linear equivalence; the same correspondence at the variety level is [[Algebraic Varieties] §Line Bundles and Vector Bundles, ⁋Proposition 19](/en/math/algebraic_varieties/line_bundles#prop19).

## Weil Divisors

Before examining linear systems, we briefly review Weil divisors. As mentioned above, Weil divisors were defined only on better spaces than Cartier divisors, and our first topic is how to carry this over into the language of schemes. For Weil divisors to be defined, we must be able to define the order of zeros and poles of a rational function at each codimension $1$ part, which requires the local ring at that point to be a discrete valuation ring. However, what this condition actually entails is somewhat unclear, so we assume normality. ([§Algebraic Structure of Schemes, ⁋Definition 6](/en/math/scheme_theory/algebra_of_schemes#def6)) Then in [Lemma 11](#lem11) we will verify that this assumption makes the local ring a DVR at codimension $1$ parts.

Hence consider a normal, integral Noetherian scheme $X$. Since $X$ is integral, any affine open subset is the spectrum of a domain, so the only associated point of $X$ is the generic point $\xi$. Then the total quotient ring of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12) becomes the function field

$$K(X)=\mathcal{O}_{X,\xi}$$

defined in [§Properties of Scheme Morphisms, §§Rational Maps](/en/math/scheme_theory/properties_of_scheme_morphisms#rational-maps), and for any non-empty open subset $V$, we can view $\Gamma(V,\mathcal{O}_X)$ as a subring of $K(X)$. In particular, the local ring $\mathcal{O}_{X,x}$ at any point $x$ is also a subring of $K(X)$ and its fraction field is $K(X)$. Moreover, since these embeddings are compatible with taking restrictions and germs, one easily checks that the equality

$$\Gamma(V,\mathcal{O}_X)=\bigcap_{x\in V}\mathcal{O}_{X,x}$$

holds inside $K(X)$. That is, we can test whether a rational function is regular on an open set by checking at each point's local ring.

::: Lemma 11
For a normal integral Noetherian scheme $X$, the following hold.

1. For a codimension $1$ irreducible closed subset $Y$ of $X$ and its generic point $\eta$, the local ring $\mathcal{O}_{X,\eta}$ is a discrete valuation ring.
2. For any $f\in K(X)^\times$, there are only finitely many codimension $1$ irreducible closed subsets $Y$ for which the valuation of $f$ at $\mathcal{O}_{X,\eta}$ is non-zero.
:::
::: Proof
For (1), since $X$ is normal, $R=\mathcal{O}_{X,\eta}$ is a normal domain, and since $X$ is locally Noetherian, it is Noetherian. Also, by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8) we have $\dim R=\codim_X Y=1$, so the maximal ideal of $R$ is a prime ideal of codimension $1$. On the other hand, applying [[Commutative Algebra] §Regular Local Rings, ⁋Theorem 11](/en/math/commutative_algebra/regular_local_rings#thm11) to the normal domain $R$ itself gives the (R1) condition, i.e., that localization at a codimension $1$ prime ideal is a discrete valuation ring. Applying this to the maximal ideal of $R$ and using that $R$ is a local ring, we conclude that $R$ itself is a discrete valuation ring.

To show (2), use the Noetherian hypothesis on $X$ to cover it by finitely many affine open subsets $U_1,\ldots, U_r$. Each $Y$ meets some $U_k$, and then $Y\cap U_k$ is a codimension $1$ irreducible closed subset of $U_k$ with the same generic point $\eta$, so it suffices to fix a single $U=\Spec A$ and show finiteness there. Here $A$ is a Noetherian domain with $\Frac(A)=K(X)$, so we can write $f=a/b$ with $a,b\in A\setminus\{0\}$. Let $\mathfrak{p}$ be the codimension $1$ prime ideal corresponding to $Y\cap U$; then $\mathcal{O}_{X,\eta}=A_\mathfrak{p}$, and if $a,b\notin \mathfrak{p}$ then both $a$ and $b$ are units in $A_\mathfrak{p}$, so the valuation of $f$ is $0$. Hence prime ideals with non-zero valuation contain $(a)$ or $(b)$, and the codimension $1$ condition means they are minimal prime ideals containing $(a)$ or $(b)$. But for an ideal $\mathfrak{a}$ in a Noetherian ring $A$, we have $\mathfrak{a}=\ann(A/\mathfrak{a})$, so the minimal prime ideals containing $\mathfrak{a}$ all belong to $\Ass(A/\mathfrak{a})$, and this set is finite. ([[Commutative Algebra] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), part 1) Therefore there are only finitely many such $\mathfrak{p}$.
:::

For $Y$ and its generic point $\eta$ satisfying part 1 of [Lemma 11](#lem11), choosing a uniformizer $\pi$ of the DVR $\mathcal{O}_{X, \eta}$ allows us to write any $f\in K(X)^\times$ uniquely as

$$f=\pi^nu,\qquad u\in \mathcal{O}_{X,\eta}^\times$$

and this integer $n$ is independent of the choice of $\pi$. We denote it by $\ord_Y(f)$. Since exponents add under multiplication of two elements, $\ord_Y:K(X)^\times \rightarrow \mathbb{Z}$ is a group homomorphism, which is exactly the discrete valuation of $\mathcal{O}_{X,\eta}$.

::: Definition 12
A codimension $1$ irreducible closed subset of a normal integral Noetherian scheme $X$ is called a *prime divisor*, and an element of the free abelian group $\Div(X)$ generated by prime divisors is called a *Weil divisor* on $X$. A Weil divisor $D=\sum_Y n_YY$ is called *effective* if all $n_Y$ are non-negative, and we write this as $D\geq 0$.
:::

Thus a Weil divisor is a formal integer linear combination of codimension $1$ closed sets, where each coefficient records the order of zero or pole of a function at the corresponding prime divisor. This is the translation of the Weil divisor of [[Algebraic Varieties] §Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1) into the language of schemes, and the following definition actually performs this recording.

::: Definition 13
For a normal integral Noetherian scheme $X$ and $f\in K(X)^\times$, we again call

$$\divisor(f)=\sum_Y \ord_Y(f)\cdot Y\in \Div(X)$$

the principal divisor of $f$. Two Weil divisors $D_1,D_2$ are linearly equivalent if $D_1-D_2=\divisor(f)$ for some $f\in K(X)^\times$, and the quotient group

$$\Cl(X)=\Div(X)/\{\divisor(f)\mid f\in K(X)^\times\}$$

is called the *divisor class group* of $X$.
:::

The second result of [Lemma 11](#lem11) guarantees the finiteness of this sum. Also, since each $\ord_Y$ is a group homomorphism, $\divisor:K(X)^\times \rightarrow \Div(X)$ is also a group homomorphism, so principal divisors form a subgroup of $\Div(X)$ and $\Cl(X)$ is well-defined.

As mentioned in the introduction, in [[Algebraic Varieties] §Divisors](/en/math/algebraic_varieties/divisors) we saw that Weil divisors and Cartier divisors are basically the same thing, with Cartier divisors defined by a slightly stronger condition and hence defined on worse spaces. That these two notions are *basically the same* is the result of [[Algebraic Varieties] §Divisors, ⁋Proposition 14](/en/math/algebraic_varieties/divisors#prop14), and the scheme version of this proposition is as follows.

::: Proposition 14
Let $X$ be a normal integral Noetherian scheme, and for each Cartier divisor $\{(U_i, f_i)\}$ and prime divisor $Y$, choose $i$ so that $Y\cap U_i\neq\emptyset$. Then the formula

$$\{(U_i,f_i)\}\mapsto \sum_Y \ord_Y(f_i)\cdot Y$$

defines an injective group homomorphism $\CaDiv(X) \rightarrow \Div(X)$ sending principal divisors to principal divisors. If $X$ is factorial, this is an isomorphism, and hence $\CaCl(X)\cong \Cl(X)$.
:::
::: Proof
First, the above formula is independent of the choice of $i$. If $Y$ meets both $U_i$ and $U_j$, then $Y\cap U_i$ and $Y\cap U_j$ are non-empty open subsets of the irreducible space $Y$, so they meet each other, and since the generic point $\eta$ belongs to every non-empty open subset of $Y$, we have $\eta\in U_i\cap U_j$. There $f_i/f_j$ is a section of $\mathcal{O}_X^\times$, so $f_i/f_j$ is a unit in $\mathcal{O}_{X,\eta}$ and thus $\ord_Y(f_i)=\ord_Y(f_j)$. Also, the finiteness of this sum follows from part 2 of [Lemma 11](#lem11) and the fact that $X$ is covered by finitely many $U_i$. Since addition of Cartier divisors is multiplication of the $f_i$'s and each $\ord_Y$ is a group homomorphism, this correspondence is a group homomorphism, and that the image of $\divisor(f)=\{(X,f)\}$ is the $\divisor(f)$ of [Definition 13](#def13) is immediate from the definition.

For injectivity, suppose the image of $D=\{(U_i,f_i)\}$ is $0$; then for each $i$, $\ord_Y(f_i)=0$ for every prime divisor $Y$ meeting $U_i$. We show that $f_i$ is an invertible section on $U_i$. Applying the equality $\Gamma(V,\mathcal{O}_X)=\bigcap_{x\in V}\mathcal{O}_{X,x}$ seen at the beginning of this section to $f_i$ and $f_i^{-1}$, it suffices to show $f_i\in \mathcal{O}_{X,x}^\times$ for each $x\in U_i$.

Let $R=\mathcal{O}_{X,x}$; this is a Noetherian normal local domain. A codimension $1$ prime ideal $\mathfrak{p}$ of $R$ corresponds to a prime divisor $Y$ passing through $x$ and meeting $U_i$, and $R_\mathfrak{p}=\mathcal{O}_{X,\eta_Y}$. Then by the (S2) condition of [[Commutative Algebra] §Regular Local Rings, ⁋Theorem 11](/en/math/commutative_algebra/regular_local_rings#thm11), for a normal domain $R$ the associated primes of a principal ideal generated by a non-zerodivisor all have codimension $1$, so the equality

$$R=\bigcap_{\text{\scriptsize $\mathfrak{p}$ associated to a non-zerodivisor}}R_\mathfrak{p}$$

given by [[Commutative Algebra] §Regular Local Rings, ⁋Proposition 8](/en/math/commutative_algebra/regular_local_rings#prop8) includes the intersection over codimension $1$ primes $\mathfrak{p}$. By assumption $\ord_Y(f_i)=0$, so both $f_i$ and $f_i^{-1}$ belong to the localization at every codimension $1$ prime ideal, and hence both are elements of $R$, so $f_i\in R^\times$. Thus every $f_i$ is an invertible section on $U_i$, and by the equivalence relation of [Definition 6](#def6), $D$ is the same Cartier divisor as $\{(U_i,1)\}$, i.e., the identity in $\CaDiv(X)$.

Now suppose $X$ is factorial and show surjectivity. Given a Weil divisor $D=\sum_Y n_YY$ and a point $x\in X$. Since $D$ is a finite sum, there are only finitely many $Y$ passing through $x$ with $n_Y\neq0$, and to each corresponds a codimension $1$ prime ideal $\mathfrak{p}_Y$ of $\mathcal{O}_{X,x}$. Since $X$ is factorial, $\mathcal{O}_{X,x}$ is a UFD, and by part 1 of [[Commutative Algebra] §Homological Criterion for Regularity, ⁋Lemma 8](/en/math/commutative_algebra/homological_criterion_for_regularity#lem8), each $\mathfrak{p}_Y=(g_Y)$ is principal.

Set $f_x=\prod_Y g_Y^{n_Y}\in K(X)^\times$. The product is over the finitely many $Y$ passing through $x$. Then $E=\divisor(f_x)-D$ is a sum of finitely many prime divisors, and by construction no prime divisor passing through $x$ appears in $E$. Indeed, for a prime divisor $Y'$ passing through $x$, $\ord_{Y'}(g_Y)$ is $1$ if $Y'=Y$ and $0$ otherwise, because $g_Y$ being a prime element of $\mathcal{O}_{X,x}$ belonging to $\mathfrak{p}_{Y'}$ is equivalent to $\mathfrak{p}_{Y'}=\mathfrak{p}_Y$. Hence the union of prime divisors appearing in $E$ is a closed set not containing $x$, and on its complement $U_x$, $\divisor(f_x)$ and $D$ agree.

Shrink these open sets to be affine to obtain an affine open cover $\{U_x\}$ of $X$. Then since both $\divisor(f_x)$ and $\divisor(f_{x'})$ agree with $D$ on $U_x\cap U_{x'}$, the ratio $f_x/f_{x'}$ has order $0$ at every prime divisor meeting the overlap, and applying the injectivity argument above to the open subset $U_x\cap U_{x'}$ shows this is a section of $\mathcal{O}_X^\times$. Hence $\{(U_x,f_x)\}$ is a Cartier divisor whose image is $D$. Finally, since principal divisors correspond to each other, an isomorphism $\CaCl(X)\cong\Cl(X)$ on the quotients is induced.
:::

The final claim of [Proposition 14](#prop14) is that the two divisor theories agree on a factorial scheme, which extends [Proposition 5](#prop5) from the effective case to arbitrary coefficients. Combining this with [Theorem 10](#thm10), we obtain $\Cl(X)\cong\CaCl(X)\cong\Pic(X)$ in the factorial case. On a general normal scheme, the image of $\CaDiv(X)$ can be a proper subgroup of $\Div(X)$, and the difference measures the extent to which singularities of $X$ prevent a codimension $1$ part from being cut out locally by a single equation.

## Linear Systems

We now quickly review the content of [[Algebraic Varieties] §Linear Systems](/en/math/algebraic_varieties/linear_systems). Given a divisor $D$, the natural question is which effective divisors lie in its linear equivalence class, and [Definition 8](#def8) turns this question into one about global sections of $\mathcal{O}_X(D)$.

::: Proposition 15
For an integral Noetherian scheme $X$ and a Cartier divisor $D$, for each $0\neq s\in \Gamma(X,\mathcal{O}_X(D))$ the divisor $D+\divisor(s)$ is an effective Cartier divisor, and this correspondence is a surjection onto all effective Cartier divisors linearly equivalent to $D$. Moreover, two sections $s,s'$ give the same divisor if and only if $s'/s\in \Gamma(X,\mathcal{O}_X)^\times$.
:::
::: Proof
Let $D=\{(U_i,f_i)\}$. That $s\in\Gamma(X,\mathcal{O}_X(D))$ means $sf_i\in \Gamma(U_i,\mathcal{O}_X)$ for all $i$, and $D+\divisor(s)=\{(U_i,sf_i)\}$, so this is exactly the statement that $D+\divisor(s)$ is effective. Conversely, if $D'$ is effective and $D'-D=\divisor(h)$, then $D'=\{(U_i,hf_i)\}$, so $hf_i\in\Gamma(U_i,\mathcal{O}_X)$, hence $h\in \Gamma(X,\mathcal{O}_X(D))$ and its image is $D'$.

Finally, $D+\divisor(s)=D+\divisor(s')$ is equivalent to $\divisor(s'/s)=0$, and by the equivalence relation of [Definition 6](#def6) this means $s'/s$ is a section of $\mathcal{O}_X^\times$ on each $U_i$, i.e., $s'/s\in \Gamma(X,\mathcal{O}_X)^\times$.
:::

Hence effective divisors linearly equivalent to $D$ are in one-to-one correspondence with non-zero sections of $\Gamma(X,\mathcal{O}_X(D))$ modulo the action of $\Gamma(X,\mathcal{O}_X)^\times$. When $X$ is a scheme over a field $\mathbb{K}$ with $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$, this quotient becomes the projectivization of a vector space, recovering [[Algebraic Varieties] §Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2).

::: Definition 16
Let $X$ be an integral scheme over a field $\mathbb{K}$ satisfying $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$. For an invertible sheaf $\mathcal{L}$, its *complete linear system* is

$$\lvert \mathcal{L}\rvert=\mathbb{P}(\Gamma(X,\mathcal{L}))$$

and a *linear system* of $\mathcal{L}$ is a $\mathbb{P}(V)\subseteq \lvert\mathcal{L}\rvert$ defined by a subspace $V\subseteq \Gamma(X,\mathcal{L})$.
:::

By [Proposition 15](#prop15), when $\mathcal{L}=\mathcal{O}_X(D)$, $\lvert\mathcal{L}\rvert$ is identified with the set of effective divisors linearly equivalent to $D$, and we also write this as $\lvert D\rvert$. For a linear system $\mathbb{P}(V)$, the set of points where all sections of $V$ vanish is called its *base locus*, and a linear system with empty base locus gives a morphism to projective space. ([[Algebraic Varieties] §Linear Systems, ⁋Definition 5](/en/math/algebraic_varieties/linear_systems#def5)) Our final section is about this.

## Ample Invertible Sheaves

An $\mathcal{O}_X$-module $\mathcal{F}$ is called *globally generated* if for each point $x$, the stalk $\mathcal{F}_x$ is generated as an $\mathcal{O}_{X,x}$-module by the germs of global sections. This is the scheme-theoretic translation of the condition that the evaluation map is surjective in [[Algebraic Varieties] §Cohomology of Projective Spaces, ⁋Definition 6](/en/math/algebraic_varieties/cohomology_of_projective_spaces#def6), and for an invertible sheaf $\mathcal{L}$, the condition that a linear system $\mathbb{P}(V)$ has empty base locus is the same as the condition that the sections in $V$ globally generate $\mathcal{L}$.

Generating sections determine a morphism to projective space. Let $X$ be a scheme over a ring $A$, $\mathcal{L}$ an invertible sheaf on $X$, and $s_0,\ldots, s_n\in \Gamma(X,\mathcal{L})$ sections that globally generate $\mathcal{L}$. For each $i$,

$$X_{s_i}=\{x\in X\mid \text{$(s_i)_x$ generates $\mathcal{L}_x$}\}$$

is an open set. This is because on a trivializing open set for $\mathcal{L}$, $s_i$ corresponds to a single function, and the set of points where that function is a unit is open. Also, since the $s_i$ globally generate $\mathcal{L}$, $\{X_{s_i}\}$ is an open cover of $X$, and on $X_{s_i}$ the section $s_i$ gives a trivialization of $\mathcal{L}$, so for each $j$ the ratio $s_j/s_i\in \Gamma(X_{s_i},\mathcal{O}_X)$ is well-defined. Now $D_+(\x_i)$ is isomorphic to $\Spec A[\x_0,\ldots,\x_n]_{(\x_i)}$ ([§Projective Schemes, ⁋Theorem 10](/en/math/scheme_theory/projective_schemes#thm10)), so the ring homomorphism

$$A[\x_0,\ldots, \x_n]_{(\x_i)} \rightarrow \Gamma(X_{s_i},\mathcal{O}_X);\qquad \frac{\x_j}{\x_i}\mapsto \frac{s_j}{s_i}$$

gives a morphism $X_{s_i} \rightarrow D_+(\x_i)$ by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13). These morphisms agree on intersections because $s_k/s_i=(s_k/s_j)(s_j/s_i)$, so applying [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1) to an affine open cover of $X$ obtained by covering each $X_{s_i}$ with affine open subsets, they glue to a single morphism

$$\varphi:X \rightarrow \mathbb{P}^n_A.$$

That is, choosing generating sections of $\mathcal{L}$ is choosing a way to represent $X$ inside projective space.

Here $\mathcal{L}$ itself is recovered from $\varphi$: we have $\mathcal{L}\cong \varphi^\ast\mathcal{O}(1)$, and this isomorphism sends $s_i$ to $\varphi^\ast\x_i$. Indeed $\x_i$ generates $\mathcal{O}(1)$ on $D_+(\x_i)$ and $\varphi$ maps $X_{s_i}$ into $D_+(\x_i)$, so $\varphi^\ast\x_i$ trivializes $\varphi^\ast\mathcal{O}(1)$ on $X_{s_i}$, while $s_i$ trivializes $\mathcal{L}$ on the same open set. On the overlap $X_{s_i}\cap X_{s_j}$ the transition functions of the two trivializations are $s_j/s_i$ and $\varphi^\ast(\x_j/\x_i)$ respectively, and the construction of $\varphi$ made these two equal, so the isomorphisms on the $X_{s_i}$ given by $s_i\mapsto \varphi^\ast\x_i$ agree on overlaps and glue to an isomorphism on all of $X$.

::: Definition 17
An invertible sheaf $\mathcal{L}$ on a finite type $A$-scheme $X$ over a Noetherian ring $A$ is called *very ample* if there exist finitely many sections $s_0,\ldots, s_n\in \Gamma(X,\mathcal{L})$ that globally generate $\mathcal{L}$ such that the morphism $\varphi:X \rightarrow \mathbb{P}^n_A$ they define is a locally closed embedding. ([§Closed Subschemes, ⁋Definition 8](/en/math/scheme_theory/closed_subschemes#def8))
:::

Thus a very ample invertible sheaf is the data of realizing $X$ as a subspace of projective space, and even if $X$ is not itself embedded in projective space, we can assign coordinates to it through this.

However, in general $\mathcal{L}$ being globally generated is a strong condition. For example, if sections fail to globally generate $\mathcal{L}$, then $\varphi$ itself is not defined. To resolve this issue, we used tensor powers of $\mathcal{L}$. Multiplication $\Gamma(X,\mathcal{L})^{\otimes m} \rightarrow \Gamma(X,\mathcal{L}^{\otimes m})$ produces sections of $\mathcal{L}^{\otimes m}$ from sections of $\mathcal{L}$, and generally there exist sections outside its image as well, so the larger $m$ is, the more sections we have to work with. For example, on $\mathbb{P}^n$, $\Gamma(\mathcal{O}(1))$ is the $(n+1)$-dimensional space of linear forms, while $\Gamma(\mathcal{O}(m))$ is the $\binom{n+m}{n}$-dimensional space of degree $m$ homogeneous polynomials.

Then we can ask whether there exists $m>0$ such that $\mathcal{L}^{\otimes m}$ is very ample, and [[Algebraic Varieties] §Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10) actually took this as the definition of ample. However, this description passes through an ambient projective space and cannot be used without the assumption that $X$ is a finite type scheme over a Noetherian ring. Instead, we choose a definition that works for arbitrary Noetherian schemes by taking as the condition only how well twisting flattens a sheaf.

::: Definition 18
An invertible sheaf $\mathcal{L}$ on a Noetherian scheme $X$ is called *ample* if for every coherent sheaf $\mathcal{F}$ ([§Quasi-coherent Sheaves, ⁋Definition 11](/en/math/scheme_theory/quasicoherent_sheaves#def11)) there exists $n_0$ such that for all $n\geq n_0$, the sheaf $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n}$ is globally generated.
:::

This definition only demands the existence of sections and does not directly mention a morphism to projective space. Requiring the condition for all coherent sheaves is essential: if we required it only for $\mathcal{F}=\mathcal{O}_X$, i.e., only that $\mathcal{L}^{\otimes n}$ is globally generated, this would contain no information about $X$ at all. On the other hand, requiring it for arbitrary $\mathcal{F}$ asks whether twisting by $\mathcal{L}$ lifts all local data on $X$ to global sections, and this becomes a condition strong enough to substitute for the existence of an embedding. The following are properties that follow immediately from this definition.

::: Proposition 19
For an invertible sheaf $\mathcal{L}$ on a Noetherian scheme $X$, the following hold.

1. If $X$ is affine, then $\mathcal{L}$ is always ample.
2. For $m\geq 1$, $\mathcal{L}$ is ample if and only if $\mathcal{L}^{\otimes m}$ is ample.
3. If $\mathcal{L}$ is ample and an invertible sheaf $\mathcal{M}$ is globally generated, then $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{M}$ is also ample.
:::
::: Proof
For (1), let $X=\Spec A$ and choose a coherent sheaf $\mathcal{F}$. Since $\mathcal{L}$ is invertible, $\mathcal{L}^{\otimes n}$ is isomorphic to $\mathcal{O}_X$ on a neighborhood of each point, so $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is isomorphic to $\mathcal{F}$ on that neighborhood. Since quasi-coherence is a local condition, $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is a quasi-coherent sheaf, hence the associated sheaf $\widetilde M$ of some $A$-module $M$. ([§Quasi-coherent Sheaves, ⁋Theorem 10](/en/math/scheme_theory/quasicoherent_sheaves#thm10)) But the stalk of $\widetilde M$ is $M_\mathfrak{p}$ ([§Quasi-coherent Sheaves, ⁋Proposition 5](/en/math/scheme_theory/quasicoherent_sheaves#prop5)), and this is generated by the image of the global section module $M$, so $\widetilde M$ is globally generated. Hence we can take $n_0=0$.

For (2), if $\mathcal{L}$ is ample, choose $n_0$ for a coherent sheaf $\mathcal{F}$ so that $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated for $n\geq n_0$. Then for $k\geq n_0$, we have $mk\geq n_0$, so $\mathcal{F}\otimes(\mathcal{L}^{\otimes m})^{\otimes k}$ is globally generated. Conversely, suppose $\mathcal{L}^{\otimes m}$ is ample. For each $j=0,1,\ldots, m-1$, the sheaf $\mathcal{F}\otimes\mathcal{L}^{\otimes j}$ is also coherent, so there exists $k_j$ such that $\mathcal{F}\otimes\mathcal{L}^{\otimes j}\otimes(\mathcal{L}^{\otimes m})^{\otimes k}$ is globally generated for $k\geq k_j$. Setting $k_\ast=\max_jk_j$, any $n\geq mk_\ast$ can be written as $n=mk+j$ with $k\geq k_\ast$ and $0\leq j<m$, so $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated.

For (3), we first observe that the tensor product of two globally generated $\mathcal{O}_X$-modules $\mathcal{F},\mathcal{G}$ is again globally generated. The stalk $(\mathcal{F}\otimes\mathcal{G})_x\cong \mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\mathcal{G}_x$ is generated by tensors of generators of $\mathcal{F}_x$ and $\mathcal{G}_x$, and these are tensors of germs of global sections. Now for a coherent sheaf $\mathcal{F}$, choose $n_0$ from the ampleness of $\mathcal{L}$; then for $n\geq n_0$,

$$\mathcal{F}\otimes(\mathcal{L}\otimes\mathcal{M})^{\otimes n}\cong(\mathcal{F}\otimes\mathcal{L}^{\otimes n})\otimes\mathcal{M}^{\otimes n}$$

where the first factor is globally generated and the second factor is a tensor power of a globally generated sheaf, hence globally generated. Therefore the left-hand side is also globally generated.
:::

By part 1 of [Proposition 19](#prop19), any invertible sheaf on an affine scheme is ample, so this condition filters nothing out when $X$ is affine. Ampleness actually distinguishes objects when $X$ is not affine; in particular, when $X$ is projective over a Noetherian ring $A$, $\mathcal{L}$ being ample is equivalent to $\mathcal{L}^{\otimes m}$ being very ample for some $m>0$.

---

**References**

**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
