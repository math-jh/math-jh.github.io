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
last_polished_at: 2026-10-30T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
[§Quasi-Coherent Sheaves](/en/math/scheme_theory/quasicoherent_sheaves){: data-lid="o3wyy" } having defined quasi-coherent sheaves and invertible sheaves, we can now begin on schemes the calculations of divisors and line bundles that we did on varieties. The goal of this post is to lift the contents covered in [\[Algebraic Varieties\] §Divisors](/en/math/algebraic_varieties/divisors){: data-lid="tj0r1" }, [\[Algebraic Varieties\] §Line Bundles and Vector Bundles](/en/math/algebraic_varieties/line_bundles){: data-lid="uaeuj" }, and [\[Algebraic Varieties\] §Linear Systems](/en/math/algebraic_varieties/linear_systems){: data-lid="ixpqe" } to the language of schemes.

## Cartier Divisors

In [\[Algebraic Varieties\] §Divisors](/en/math/algebraic_varieties/divisors){: data-lid="cn9k7" }, we defined Weil divisors first and examined Cartier divisors afterward. This was because Cartier divisors generalized the space on which the object is defined by adding the condition that it is cut out locally by a single equation, thanks to which we could use a divisor theory that works on singular varieties. Since schemes are a more general setting than varieties in many respects, rather than treating Weil divisors from the start, we choose to use Cartier divisors, which we will mainly use.

::: Definition 1
A closed embedding $\iota: Z \hookrightarrow X$ is called an *effective Cartier divisor* if there exists an affine open cover $\{U_i=\Spec A_i\}$ of $X$ such that for each closed embedding

$$\iota\vert^{U_i}:\iota^{-1}(U_i) \rightarrow U_i$$

there exists a suitable non-zerodivisor $s_i\in A_i=\Gamma(U_i, \mathcal{O}_X)$ such that the two closed embeddings $\iota\vert^{U_i}$ and the vanishing scheme of $s_i$, $Z(s_i)\hookrightarrow U_i$, are isomorphic. ([§Closed Subschemes, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes#def7){: data-lid="l0cle" })
:::

Since all the definition requires of $s_i$ is that it be a non-zerodivisor, $Z$ can be non-reduced. In an algebraic variety, a closed subvariety is always reduced, so in order to capture multiplicity, one had to formally attach integer coefficients using formal sums as in [\[Algebraic Varieties\] §Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1){: data-lid="bss27" }. Now that $Z$ itself has multiplicity, such coefficients are not needed in the effective case. For example, for $X=\Spec \mathbb{K}[\x]$ and $s=\x^2$, since $\x^2$ is a non-zerodivisor, $Z(s)=\Spec \mathbb{K}[\x]/(\x^2)$ is an effective Cartier divisor, which is a non-reduced scheme supported at the single point of the origin and has multiplicity $2$.

The above definition is essentially a condition defined on each open set and depends on the cover, but it can be simply converted into a property of the ideal sheaf defining the closed subscheme. ([§Closed Subschemes, ⁋Definition 5](/en/math/scheme_theory/closed_subschemes#def5){: data-lid="q21yk" })

::: Proposition 2
A closed embedding $\iota: Z\hookrightarrow X$ is an effective Cartier divisor if and only if its ideal sheaf $\mathcal{I}_{Z/X}$ is an invertible sheaf. ([§Quasi-Coherent Sheaves, ⁋Definition 12](/en/math/scheme_theory/quasicoherent_sheaves#def12){: data-lid="1mq58" })
:::
::: Proof
On an affine open subset $U=\Spec A$, the restriction of $\iota$ to the codomain is the closed embedding $Z(\mathfrak{a})\hookrightarrow U$ defined by the ideal $\mathfrak{a}=\mathcal{I}_{Z/X}(U)$, and two distinct ideals define two distinct closed subschemes. ([§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3){: data-lid="m90t8" }) Hence $\iota\vert^U$ being isomorphic to $Z(s)\hookrightarrow U$ is equivalent to $\mathfrak{a}=(s)$.

Now consider the map $A \rightarrow (s)$, $a\mapsto as$ for $s\in A$. This is always surjective and its kernel is $\ann(s)$, so this map being an isomorphism is equivalent to $s$ being a non-zerodivisor. Now suppose $\iota$ is an effective Cartier divisor and choose the affine open cover $\{U_i=\Spec A_i\}$ from [Definition 1](#def1){: data-lid="zavux" }. Then $\mathcal{I}_{Z/X}(U_i)=(s_i)\cong A_i$. On the other hand, $\mathcal{I}_{Z/X}$ is a quasi-coherent sheaf ([§Quasi-Coherent Sheaves, ⁋Proposition 18](/en/math/scheme_theory/quasicoherent_sheaves#prop18){: data-lid="r3n2t" }) and quasi-coherence is affine-local, so by [§Quasi-Coherent Sheaves, ⁋Theorem 10](/en/math/scheme_theory/quasicoherent_sheaves#thm10){: data-lid="ltclw" } we have $\mathcal{I}_{Z/X}\vert_{U_i}\cong \widetilde{\mathcal{I}_{Z/X}(U_i)}$. Therefore the above isomorphism yields

$$\mathcal{I}_{Z/X}\vert_{U_i}\cong \widetilde{(s_i)}\cong \widetilde{A_i}=\mathcal{O}_{U_i}$$

That is, $\mathcal{I}_{Z/X}$ is a locally free sheaf of rank $1$.

Conversely, suppose $\mathcal{I}_{Z/X}$ is an invertible sheaf. For any point $x$, choose an open neighborhood $V$ with $\mathcal{I}_{Z/X}\vert_V\cong \mathcal{O}_V$, and then choose an affine open subset $U=\Spec A$ inside $V$ containing $x$; then $\mathcal{I}_{Z/X}(U)\cong A$. Under this isomorphism, letting $s$ be the image of $1\in A$, we have $\mathcal{I}_{Z/X}(U)=(s)$, and since $\ann(s)=0$, $s$ is a non-zerodivisor. Such $U$ cover $X$, so the condition of [Definition 1](#def1){: data-lid="dvvn9" } is satisfied.
:::

The map $A\rightarrow \mathcal{I}_{Z/X}(U)$ used in the proof clearly separates the two requirements of [Definition 1](#def1){: data-lid="lfc44" }. That this map is surjective requires that the ideal $\mathcal{I}_{Z/X}(U)$ is generated by a single $s$, that is, that $Z$ is cut out by a single equation on $U$. Here, the non-zerodivisor condition above becomes $\ann(s)=0$, and this map then becomes injective, yielding $\mathcal{I}_{Z/X}\vert_U\cong \mathcal{O}_U$. If we omit this non-zerodivisor condition, then each $s_i$ can be chosen as an arbitrary element of $A_i$, and the condition obtained in this way is called *locally principal*. That is, an effective Cartier divisor is one among locally principal ones whose local equation can be chosen to be a non-zerodivisor.

The most basic property of an effective Cartier divisor is that its codimension is always $1$.

::: Proposition 3
For an effective Cartier divisor $\iota:Z\hookrightarrow X$ on a locally Noetherian scheme $X$, every irreducible component of $Z$ has codimension $1$ in $X$.
:::
::: Proof
Since codimension is computed locally, it suffices to choose one open set from the affine open cover $\{U_i=\Spec A_i\}$ in [Definition 1](#def1){: data-lid="z1p7n" } and consider the case where $Z\cap U_i=Z(s_i)$ with $s_i\in A_i$ a non-zerodivisor. If an irreducible component $W$ of $Z$ meets $U_i$, then $W\cap U_i$ is an irreducible component of $Z(s_i)$. By [§Dimension, ⁋Proposition 13](/en/math/scheme_theory/dimension#prop13){: data-lid="plfq0" }, every component of $Z(s_i)$ has codimension $0$ or $1$ in $U_i$; a component of codimension $0$ corresponds to an irreducible component of $U_i$ itself, i.e., to a minimal prime ideal $\mathfrak{p}$ of $A_i$. If $W\cap U_i$ were such a component, then $s_i$ would vanish on it, so $s_i\in \mathfrak{p}$. However, in a Noetherian ring a non-zerodivisor does not belong to any minimal prime ideal ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="k7grl" }), contradicting the assumption that $s_i$ is a non-zerodivisor. Hence the codimension of $W\cap U_i$ is $1$, and by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8){: data-lid="x72h2" } the codimension of $W$ in $X$ is also $1$.
:::

The only place in the proof where the requirement that $s_i$ be a non-zerodivisor was used was that $s_i$ does not belong to any minimal prime ideal of $A_i$. Geometrically, this means $s_i$ does not vanish identically on any irreducible component of $X$. If we remove this requirement from [Definition 1](#def1){: data-lid="3u7vz" }, then the equation $s_i$ can swallow an entire component instead of cutting it, and then $Z$ becomes a component of $X$ itself rather than having codimension $1$. Let us examine this situation in the following example.

::: Example 4
Let $X=\Spec \mathbb{K}[\x,\y]/(\x\y)$ be the union of the two coordinate axes in the plane, and let $Z=Z(\x)$. Since this is the vanishing scheme of a single global section $\x$, taking $X$ itself as a cover shows that $Z\hookrightarrow X$ is locally principal.

However, this is not an effective Cartier divisor. Since $\mathbb{K}[\x,\y]/(\x\y,\x)\cong\mathbb{K}[\y]$, $Z$ is the $\y$-axis, which is one of the two irreducible components of $X$, so it has codimension $0$ in $X$. But by [Proposition 3](#prop3){: data-lid="yij5e" }, an irreducible component of an effective Cartier divisor must have codimension $1$.

Algebraically, [Proposition 2](#prop2){: data-lid="9wme8" } tells us the same thing. No matter how we choose an affine open subset $U=\Spec A$ containing the origin, $U$ meets both coordinate axes, so in $A$, $\y$ is not $0$, and the generator of $\mathcal{I}_{Z/X}(U)$, $\x$, is a zerodivisor killing it. Hence this ideal can never be a free module.
:::

The reason codimension did not behave as expected in the above example was that $\x$ was contained in a minimal prime ideal. Requiring an element to be a non-zerodivisor allows us to avoid not only such minimal prime ideals but all associated prime ideals; for example, in the scheme

$$A=\mathbb{K}[\x,\y]/(\x^2,\x\y)$$

we have $(\x^2,\x\y)=(\x)\cap(\x^2,\y)$, so $\Ass(A)=\{(\x),(\x,\y)\}$, which is a scheme with the origin as an embedded point on the $\y$-axis. Here, $\y$ does not belong to the unique minimal prime ideal $(\x)$, so $Z(\y)$ does not swallow any component and has codimension $1$, but since $\x\y=0$ and $\x\neq 0$, $\y$ is a zerodivisor and $\ann(\y)=(\x)$. Therefore $Z(\y)\hookrightarrow \Spec A$ has codimension $1$ but is not an effective Cartier divisor, which also means that the converse of [Proposition 3](#prop3){: data-lid="gybkf" } does not hold in general.

In both examples, the problem was that the local ring at the relevant point was not even a domain. If we exclude this situation, the converse of [Proposition 3](#prop3){: data-lid="8x03f" } holds.

::: Proposition 5
Let $X$ be a locally Noetherian integral scheme that is factorial. ([§Algebraic Structure of Schemes, ⁋Definition 7](/en/math/scheme_theory/algebra_of_schemes#def7){: data-lid="u85mp" }) Then any codimension $1$ integral closed subscheme $\iota:Z\hookrightarrow X$ is an effective Cartier divisor.
:::
::: Proof
Since $X$ is integral, for any affine open subset $U=\Spec A$, $A$ is a Noetherian domain, and in particular, every element of $A$ other than $0$ is a non-zerodivisor.

There is nothing to check at points not meeting $Z$. Since $Z$ is a closed set, such a point has an affine open neighborhood disjoint from $Z$, and on it $Z$ is $Z(1)=\emptyset$, so the condition of [Definition 1](#def1){: data-lid="5t9k7" } is satisfied with $s=1$.

Now choose $z\in Z$, and take, containing $z$, an affine open subset $U=\Spec A$. Since $Z$ is integral, $\mathfrak{p}=\mathcal{I}_{Z/X}(U)$ is a prime ideal, and by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8){: data-lid="yoa91" }, $Z$ having codimension $1$ means that $\mathfrak{p}$ has codimension $1$. If we let the prime ideal corresponding to $z$ be $\mathfrak{q}\supseteq \mathfrak{p}$, then by the assumption that $X$ is factorial, $A_\mathfrak{q}=\mathcal{O}_{X,z}$ is a Noetherian local UFD, and $\mathfrak{p}A_\mathfrak{q}$ is a prime ideal of codimension $1$. Then by part 1 of [\[Commutative Algebra\] §Homological Criterion for Regularity, ⁋Lemma 8](/en/math/commutative_algebra/homological_criterion_for_regularity#lem8){: data-lid="oekvy" }, $\mathfrak{p}A_\mathfrak{q}$ is principal.

Let $\mathfrak{p}A_\mathfrak{q}=(t)$; since elements outside $\mathfrak{q}$ are units in $A_\mathfrak{q}$, we can arrange that $t=f/1$ by choosing $f\in A$. Since $\mathfrak{p}A_\mathfrak{q}\cap A=\mathfrak{p}$, we have $f\in \mathfrak{p}$. On the other hand, since $A$ is Noetherian, $\mathfrak{p}$ is generated by finitely many elements $p_1,\ldots, p_n$, and since each $p_i/1$ belongs to $(f)A_\mathfrak{q}$, there exists $g_i\notin \mathfrak{q}$ such that $g_ip_i\in (f)$. Setting $g=g_1\cdots g_n$, since $\mathfrak{q}$ is prime, we have $g\notin\mathfrak{q}$, and in $A_g$, $\mathfrak{p}A_g=(f)$.

Then $D(g)$ is an affine open neighborhood of $z$ on which $Z$ is $Z(f)$, and since $A_g$ is a domain and $f\neq 0$, $f$ is a non-zerodivisor. The open sets obtained in this way cover $X$, so by [Definition 1](#def1){: data-lid="y2exg" }, $\iota$ is an effective Cartier divisor.
:::

That is, under the above hypotheses, the topological condition of codimension $1$ alone is enough to recover a single equation, and since it is generally known that any scheme all of whose local rings are regular local rings is factorial, this result holds in particular for regular objects. In general we cannot expect such a recovery, so we take the local equation data itself as our object and collect them together. Here each equation need not be a function on $U_i$; only its ratio on overlaps is controlled, and below $K(U)$ denotes the total quotient ring of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12){: data-lid="h3mv2" }.

::: Definition 6
A *Cartier divisor* on a locally Noetherian scheme $X$ is, given an affine open cover of $X$, $\{U_i\}$, and each $f_i\in K(U_i)^\times$, a datum $\{(U_i,f_i)\}$ such that for any $i,j$, $f_i/f_j$ is, on $U_i\cap U_j$, a section of $\mathcal{O}_X^\times$. Here, two data $\{(U_i,f_i)\}$ and $\{(V_j,g_j)\}$ are regarded as the same Cartier divisor when for any $i,j$, $f_i/g_j$ is, on $U_i\cap V_j$, a section of $\mathcal{O}_X^\times$. These form a group under addition

$$\{(U_i,f_i)\}+\{(V_j,g_j)\}=\{(W, (f_ig_j)\vert_W)\}$$

where $W$ ranges over affine open subsets contained in each $U_i\cap V_j$. We denote this group by $\CaDiv(X)$.
:::

This is the same definition as the one examined in [\[Algebraic Varieties\] §Divisors, ⁋Definition 12](/en/math/algebraic_varieties/divisors#def12){: data-lid="njfvd" }, differing only in that each $f_i$ comes, for each $U_i$, from $K(U_i)^\times$ rather than from a single function field. The associated points of an open subset $W\subseteq U$ are those associated points of $U$ lying in $W$ ([§Algebraic Structure of Schemes, ⁋Definition 8](/en/math/scheme_theory/algebra_of_schemes#def8){: data-lid="72n58" }), so there is a restriction $K(U)^\times\rightarrow K(W)^\times$, and through this we can refine data; hence below we also read data written on covers that are not affine in the same way.

A Cartier divisor for which each $f_i$ lies in $\Gamma(U_i,\mathcal{O}_X)$ is called *effective*, and one easily checks that this is compatible with the above equivalence relation. This is because if $f_i$ lies in $\Gamma(U_i,\mathcal{O}_X)$ and $f_i/g_j$ is an invertible section on $U_i\cap V_j$, then $g_j=f_i\cdot(f_i/g_j)^{-1}$ is also a section of $\mathcal{O}_X$ there, and since these $U_i\cap V_j$ cover $V_j$, $g_j$ also lies in $\Gamma(V_j,\mathcal{O}_X)$. That this algebraically defined notion coincides with the one in [Definition 1](#def1){: data-lid="4r0j5" } is the first result about $\CaDiv(X)$.

::: Proposition 7
For a locally Noetherian scheme $X$, effective Cartier divisors $\iota:Z\hookrightarrow X$ and effective elements of $\CaDiv(X)$ are in one-to-one correspondence.
:::
::: Proof
Suppose an effective $D=\{(U_i,f_i)\}$ is given. That $f_i\in \Gamma(U_i,\mathcal{O}_X)$ is an element of $K(U_i)^\times$ means that $f_i$ is a non-zerodivisor. If we consider the ideal $(f_i)$ on each $U_i$, since $f_i/f_j$ is a unit on overlaps, these define the same ideal sheaf on overlaps, and hence, by [§Closed Subschemes, ⁋Proposition 6](/en/math/scheme_theory/closed_subschemes#prop6){: data-lid="l08fk" }, glue to a single closed subscheme of $X$, $Z$. This $Z$ satisfies the condition of [Definition 1](#def1){: data-lid="t5hog" } by construction.

Conversely, suppose an effective Cartier divisor $\iota:Z\hookrightarrow X$ and the data $\{(U_i,s_i)\}$ of [Definition 1](#def1){: data-lid="yyacd" } are given. Since $s_i$ is a non-zerodivisor, we have $s_i\in K(U_i)^\times$. On overlaps, $\mathcal{I}_{Z/X}$ is generated by both $s_i$ and $s_j$, so at each point we have $s_i=us_j$ for a local unit $u$, and this $u$ is uniquely determined from $s_i$ and $s_j$ being non-zerodivisors and glues to a section over the entire overlap. Thus $\{(U_i,s_i)\}$ is an effective Cartier divisor. That the two constructions are mutual inverses is immediately verified since either way we are passing back and forth between elements that locally generate $\mathcal{I}_{Z/X}$.
:::

From this, we do not distinguish between an effective Cartier divisor and an effective element of $\CaDiv(X)$. For a general Cartier divisor, since on each $U_i$ one can write $f_i$ as the ratio of two non-zerodivisors, it is locally the difference of two effective Cartier divisors; in this sense, $\CaDiv(X)$ is locally generated by the closed subschemes of [Definition 1](#def1){: data-lid="viz71" }.

For a single $f\in K(X)^\times$, we write the Cartier divisor of the form $\{(X,f)\}$ that it defines as $\divisor(f)$ and call it a *principal divisor*. By definition a Cartier divisor is always given locally by a single function, so the issue here is whether this local data can be assembled into a single global function. Denoting the subgroup they form by $\Prin(X)$, the quotient group

$$\CaCl(X)=\CaDiv(X)/\Prin(X)$$

is defined, and when the difference of two Cartier divisors is principal, we call them *linearly equivalent*.

## $\mathcal{O}_X(D)$ and the Picard Group

The data $\{(U_i,f_i)\}$ of a Cartier divisor specifies a function on each piece and controls only their ratio on overlaps. This is precisely the way an invertible sheaf is described by local trivializations and transition functions, so we can associate an invertible sheaf to a divisor. In this section, let $X$ be an *integral* Noetherian scheme. Then the local ring at the generic point, $K(X)$, is a field, and for any non-empty open set, $\Gamma(V,\mathcal{O}_X)$ is a subring of it; hence below we can treat rational functions inside a single $K(X)$.

::: Definition 8
For an integral Noetherian scheme $X$ and a Cartier divisor $D=\{(U_i,f_i)\}$, we define on $X$ the $\mathcal{O}_X$-module $\mathcal{O}_X(D)$ by setting, for each non-empty open subset $V$,

$$\Gamma(V,\mathcal{O}_X(D))=\{g\in K(X)\mid gf_i\in \Gamma(V\cap U_i,\mathcal{O}_X)\text{ for all $i$}\}$$

and setting $\Gamma(\emptyset,\mathcal{O}_X(D))=0$. Here, the restriction maps between non-empty open subsets are given by sending elements of $K(X)$ to themselves.
:::

This is what we already covered in [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Definition 17](/en/math/algebraic_varieties/line_bundles#def17){: data-lid="d3tpy" }: we constructed a line bundle using $f_i/f_j$ as transition functions and then verified that its sections are the rational functions satisfying $\divisor(g)+D\geq 0$. [Definition 8](#def8){: data-lid="ocao8" } also defines the sheaf $\mathcal{O}_X(D)$ in the same way as that definition; here $\Gamma(V,\mathcal{O}_X(D))$ is the collection of rational functions allowing poles only to the extent specified by $D$.

Since the condition in the definition is checked in a neighborhood of each point, $\mathcal{O}_X(D)$ is indeed a sheaf closed under multiplication by $\mathcal{O}_X$. Moreover, this sheaf is independent of the choice of data representing $D$. This is because if another datum $\{(V_j,g_j)\}$ gives the same Cartier divisor, then $f_i/g_j$ is an invertible section on the overlap, so $gf_i$ being a section of $\mathcal{O}_X$ and $gg_j$ being so are the same condition on each $V\cap U_i\cap V_j$. If $D$ is effective, then $\mathcal{O}_X\subseteq \mathcal{O}_X(D)$, and for $-D$ it conversely becomes the sheaf of functions vanishing on $D$, that is, the ideal sheaf of the closed subscheme given by [Proposition 7](#prop7){: data-lid="e1jz2" }.

::: Proposition 9
For an integral Noetherian scheme $X$ and Cartier divisors $D,D'$, the following hold.

1. $\mathcal{O}_X(D)$ is an invertible sheaf, and $\mathcal{O}_X(D)\vert_{U_i}$ is generated by $f_i^{-1}$.
2. Multiplication inside $K(X)$ gives an isomorphism $\mathcal{O}_X(D)\otimes_{\mathcal{O}_X}\mathcal{O}_X(D')\cong \mathcal{O}_X(D+D')$.
3. $\mathcal{O}_X(D)\cong \mathcal{O}_X$ if and only if $D$ is principal.
:::
::: Proof
For (1), for an open subset $V\subseteq U_i$, since $f_j=f_i\cdot(f_j/f_i)$ and $f_j/f_i$ is an invertible section on $U_i\cap U_j$, if $gf_i\in \Gamma(V,\mathcal{O}_X)$ then automatically $gf_j\in\Gamma(V\cap U_j,\mathcal{O}_X)$. Hence

$$\Gamma(V,\mathcal{O}_X(D))=f_i^{-1}\Gamma(V,\mathcal{O}_X)$$

and since $f_i\in K(X)^\times$, the map $g\mapsto gf_i$ is an isomorphism $\mathcal{O}_X(D)\vert_{U_i} \rightarrow \mathcal{O}_{U_i}$. That is, $\mathcal{O}_X(D)$ is a locally free sheaf of rank $1$.

For (2), letting $D'=\{(V_j,g_j)\}$ and computing $D+D'$ as $\{(U_i\cap V_j, f_ig_j)\}$, by (1) the three sheaves on $U_i\cap V_j$ are free modules generated by $f_i^{-1}$, $g_j^{-1}$, and $(f_ig_j)^{-1}$ respectively. Multiplication $\mathcal{O}_X(D)\otimes \mathcal{O}_X(D') \rightarrow \mathcal{O}_X(D+D')$ sends a generator to a generator, so it is an isomorphism on each piece and therefore an isomorphism globally.

For (3), if $D=\divisor(h)$, then $\mathcal{O}_X(D)=h^{-1}\mathcal{O}_X\cong \mathcal{O}_X$. Conversely, suppose an isomorphism $\psi:\mathcal{O}_X \rightarrow \mathcal{O}_X(D)$ is given, and let $h=\psi(1)\in \Gamma(X,\mathcal{O}_X(D))\subseteq K(X)$. Then $h$ generates $\mathcal{O}_X(D)$ on each $U_i$, so comparing with (1), $h$ and $f_i^{-1}$ differ by a section of $\mathcal{O}_X^\times$, i.e., $f_i/h^{-1}=hf_i$ is an invertible section on $U_i$. Hence by the equivalence relation of [Definition 6](#def6){: data-lid="a2few" }, $\{(U_i,f_i)\}$ and $\{(X,h^{-1})\}$ define the same Cartier divisor, so $D=\divisor(h^{-1})$.
:::

By the above proposition, the correspondence $D\mapsto \mathcal{O}_X(D)$ gives a group homomorphism $\CaDiv(X)\rightarrow\Pic(X)$, and its kernel is precisely $\Prin(X)$. Therefore we know that the image of this correspondence is isomorphic to $\CaCl(X)=\CaDiv(X)/\Prin(X)$. The following theorem completes this result, showing that this correspondence is surjective and thus gives a canonical isomorphism $\CaCl(X)\cong \Pic(X)$.

::: Theorem 10
For an integral Noetherian scheme $X$, the map $D\mapsto \mathcal{O}_X(D)$ induces an isomorphism $\CaCl(X)\cong\Pic(X)$.
:::
::: Proof
By [Proposition 9](#prop9){: data-lid="5x1a4" }, since the induced homomorphism is injective, it suffices to show surjectivity. Suppose we are given an invertible sheaf $\mathcal{L}$ and its trivializations $\psi_i:\mathcal{O}_{U_i} \rightarrow \mathcal{L}\vert_{U_i}$. Since trivializations are preserved under restriction to open subsets, by refining the cover by covering each $U_i$ with affine open subsets, we may assume from the outset that $\{U_i\}$ is an affine open cover. Now let $t_i=\psi_i(1)$ be the generating section of $\mathcal{L}$ over $U_i$. Then on overlaps, sections $g_{ij}\in \Gamma(U_i\cap U_j,\mathcal{O}_X)^\times$ such that $t_j=g_{ij}t_i$ are uniquely determined, and these satisfy $g_{ij}g_{jk}=g_{ik}$.

First observe that $g_{ii}=1$ and $g_{ji}=g_{ij}^{-1}$, fix a non-empty $U_{i_0}$, and set $f_i=g_{ii_0}\in \Gamma(U_i\cap U_{i_0},\mathcal{O}_X)^\times$. Since $X$ is integral, this is an element of $K(X)^\times$, and by the cocycle condition, $f_i/f_j=g_{ii_0}g_{i_0j}=g_{ij}$ on $U_i\cap U_j\cap U_{i_0}$. But since $X$ is irreducible, this open set is a dense open subset of $U_i\cap U_j$, and since $\Gamma(U_i\cap U_j,\mathcal{O}_X)$ embeds into $K(X)$, this equality holds on all of $U_i\cap U_j$. In particular, $f_i/f_j$ is an invertible section on overlaps, so $D=\{(U_i,f_i)\}$ is a Cartier divisor.

Now we show that $\mathcal{O}_X(D)\cong \mathcal{L}$. By [Proposition 9](#prop9){: data-lid="16615" }, $\mathcal{O}_X(D)\vert_{U_i}$ is generated by $f_i^{-1}$, so on $V\subseteq U_i$ we have $gf_i\in \Gamma(V,\mathcal{O}_X)$, and

$$\varphi_i:\mathcal{O}_X(D)\vert_{U_i} \rightarrow \mathcal{L}\vert_{U_i};\qquad g\mapsto (gf_i)\cdot t_i$$

is an isomorphism. On overlaps, $t_i=g_{ji}t_j$ and $g_{ji}=f_j/f_i$, so

$$\varphi_i(g)=(gf_i)\cdot\frac{f_j}{f_i}t_j=(gf_j)\cdot t_j=\varphi_j(g)$$

and these glue to a single isomorphism $\mathcal{O}_X(D)\cong\mathcal{L}$.
:::

Thus, on an integral Noetherian scheme, dealing with invertible sheaves is the same as dealing with Cartier divisors keeping track of them only up to linear equivalence, and the same correspondence at the variety level is [\[Algebraic Varieties\] §Line Bundles and Vector Bundles, ⁋Proposition 19](/en/math/algebraic_varieties/line_bundles#prop19){: data-lid="r4lfs" }.

## Weil Divisors

Now, before examining linear systems, we briefly look at Weil divisors. As briefly mentioned above, Weil divisors were defined only on better spaces than Cartier divisors, and how to bring this into the language of schemes is the first subject of our discussion. First, in order for Weil divisors to be defined, we must be able to define the order of zeros and poles of a rational function at each codimension $1$ part, and for that to happen, the local ring at that point must be a discrete valuation ring. However, what this condition actually entails is somewhat unclear, so we assume normality. ([§Algebraic Structure of Schemes, ⁋Definition 6](/en/math/scheme_theory/algebra_of_schemes#def6){: data-lid="m16bz" }) Then in [Lemma 11](#lem11){: data-lid="hnya7" } we will verify that this assumption makes the local ring a DVR at codimension $1$ parts.

Therefore, consider a normal, integral Noetherian scheme $X$. Since $X$ is integral, any affine open subset is the spectrum of a domain, so the only associated point of $X$ is the generic point $\xi$. Then the total quotient ring of [§Algebraic Structure of Schemes, ⁋Definition 12](/en/math/scheme_theory/algebra_of_schemes#def12){: data-lid="6ism9" } becomes the function field

$$K(X)=\mathcal{O}_{X,\xi}$$

defined in [§Properties of Scheme Morphisms, §§Rational Maps](/en/math/scheme_theory/properties_of_scheme_morphisms#rational-maps){: data-lid="h2w86" }, and for any non-empty open subset $V$, we can view $\Gamma(V,\mathcal{O}_X)$ as a subring of $K(X)$. In particular, the local ring $\mathcal{O}_{X,x}$ at any point $x$ is also a subring of $K(X)$ and its fraction field is $K(X)$. Moreover, since these embeddings are compatible with taking restrictions and germs, one easily checks that the equality

$$\Gamma(V,\mathcal{O}_X)=\bigcap_{x\in V}\mathcal{O}_{X,x}$$

holds inside $K(X)$. That is, we can determine whether a rational function is regular on an open set from the local ring at each point.

::: Lemma 11
For a normal integral Noetherian scheme $X$, the following hold.

1. In $X$, for a codimension $1$ irreducible closed subset $Y$ and its generic point $\eta$, $\mathcal{O}_{X,\eta}$ is a discrete valuation ring.
2. For any $f\in K(X)^\times$, the valuation of $f$ at $\mathcal{O}_{X,\eta}$ is not $0$ for only finitely many codimension $1$ irreducible closed subsets $Y$.
:::
::: Proof
For (1), since $X$ is normal, $R=\mathcal{O}_{X,\eta}$ is a normal domain, and since $X$ is locally Noetherian, it is Noetherian. Also, by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8){: data-lid="0ut8h" } we have $\dim R=\codim_X Y=1$, so the maximal ideal of $R$ is a prime ideal of codimension $1$. On the other hand, applying [\[Commutative Algebra\] §Regular Local Rings, ⁋Theorem 10](/en/math/commutative_algebra/regular_local_rings#thm10){: data-lid="4odxe" } to the normal domain $R$ itself gives the (R1) condition, i.e., that localization at a codimension $1$ prime ideal is a discrete valuation ring. Applying this to the maximal ideal of $R$ and using that $R$ is a local ring, $R$ itself is a discrete valuation ring.

To show (2), using the Noetherian hypothesis on $X$, let finitely many affine open subsets $U_1,\ldots, U_r$ cover $X$. Each $Y$ meets some $U_k$, and then $Y\cap U_k$ is an irreducible closed subset of $U_k$ of codimension $1$ with the same generic point $\eta$, so it suffices to fix a single $U=\Spec A$ and show finiteness on it. Here, $A$ is a Noetherian domain and $\Frac(A)=K(X)$, so we can write $f=a/b$ with $a,b\in A\setminus\{0\}$. Letting the prime ideal corresponding to $Y\cap U$, of codimension $1$, be $\mathfrak{p}$, we have $\mathcal{O}_{X,\eta}=A_\mathfrak{p}$, and if $a,b\notin \mathfrak{p}$, then both $a$ and $b$ are units in $A_\mathfrak{p}$, so the valuation of $f$ is $0$. Therefore, if the valuation is not $0$, $\mathfrak{p}$ contains $(a)$ or $(b)$, and from the condition of codimension $1$, these are minimal prime ideals containing $(a)$ or $(b)$. However, in the Noetherian ring $A$, for an ideal $\mathfrak{a}$, since $\mathfrak{a}=\ann(A/\mathfrak{a})$, all minimal prime ideals containing $\mathfrak{a}$ belong to $\Ass(A/\mathfrak{a})$, and this set is finite. ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7){: data-lid="y74eg" }, part 1) Therefore, there are also only finitely many such $\mathfrak{p}$.
:::

For $Y$ and its generic point $\eta$ satisfying part 1 of [Lemma 11](#lem11){: data-lid="o67lo" }, if we choose for the DVR $\mathcal{O}_{X, \eta}$ a uniformizer $\pi$, any $f\in K(X)^\times$ can be written uniquely as

$$f=\pi^nu,\qquad u\in \mathcal{O}_{X,\eta}^\times$$

and this integer $n$ is independent of the choice of $\pi$. We denote this by $\ord_Y(f)$. Since exponents add under multiplication of two elements, $\ord_Y:K(X)^\times \rightarrow \mathbb{Z}$ is a group homomorphism, which is precisely the discrete valuation of $\mathcal{O}_{X,\eta}$.

::: Definition 12
For a normal integral Noetherian scheme $X$, a codimension $1$ irreducible closed subset is called a *prime divisor*, and an element of the free abelian group $\Div(X)$ generated by prime divisors is called a *Weil divisor* on $X$. A Weil divisor $D=\sum_Y n_YY$ is called *effective* if all $n_Y$ are non-negative, and this is written as $D\geq 0$.
:::

That is, a Weil divisor is a formal sum with integer coefficients of codimension $1$ closed sets, where each coefficient records the order of a zero or pole that a function has at the corresponding prime divisor. This is the translation of the Weil divisor of [\[Algebraic Varieties\] §Divisors, ⁋Definition 1](/en/math/algebraic_varieties/divisors#def1){: data-lid="blauc" } into the language of schemes, and the following definition actually performs this recording.

::: Definition 13
For a normal integral Noetherian scheme $X$ and $f\in K(X)^\times$, we again call

$$\divisor(f)=\sum_Y \ord_Y(f)\cdot Y\in \Div(X)$$

the principal divisor of $f$. Two Weil divisors $D_1,D_2$ are linearly equivalent if $D_1-D_2=\divisor(f)$ for some $f\in K(X)^\times$, and the quotient group

$$\Cl(X)=\Div(X)/\{\divisor(f)\mid f\in K(X)^\times\}$$

is called the *divisor class group* of $X$.
:::

The second result of [Lemma 11](#lem11){: data-lid="xivpg" } guarantees the finiteness of this sum. Also, since each $\ord_Y$ is a group homomorphism, $\divisor:K(X)^\times \rightarrow \Div(X)$ is also a group homomorphism, so the principal divisors form a subgroup of $\Div(X)$ and $\Cl(X)$ is well-defined.

As mentioned at the beginning of this post, in [\[Algebraic Varieties\] §Divisors](/en/math/algebraic_varieties/divisors){: data-lid="opt9e" } we saw that Weil divisors and Cartier divisors are basically the same thing, differing only in that Cartier divisors are defined by a slightly stronger condition and therefore are defined on worse spaces. Here, that these two notions are *basically the same* is the result of [\[Algebraic Varieties\] §Divisors, ⁋Proposition 14](/en/math/algebraic_varieties/divisors#prop14){: data-lid="zb7j3" }, and the scheme version of this proposition is as follows.

::: Proposition 14
Let $X$ be a normal integral Noetherian scheme, and for each Cartier divisor $\{(U_i, f_i)\}$ and prime divisor $Y$, choose $i$ so that $Y\cap U_i\neq\emptyset$. Then the formula

$$\{(U_i,f_i)\}\mapsto \sum_Y \ord_Y(f_i)\cdot Y$$

defines an injective group homomorphism $\CaDiv(X) \rightarrow \Div(X)$ sending principal divisors to principal divisors. If $X$ is factorial, this is an isomorphism, and hence $\CaCl(X)\cong \Cl(X)$.
:::
::: Proof
First, the above formula is independent of the choice of $i$. If $Y$ meets both $U_i$ and $U_j$, then $Y\cap U_i$ and $Y\cap U_j$ are two non-empty open subsets of the irreducible space $Y$, so they intersect, and since the generic point $\eta$ belongs to every non-empty open subset of $Y$, we have $\eta\in U_i\cap U_j$. Over this, since $f_i/f_j$ is a section of $\mathcal{O}_X^\times$, $f_i/f_j$ is a unit in $\mathcal{O}_{X,\eta}$, which yields $\ord_Y(f_i)=\ord_Y(f_j)$. That this sum is a finite sum follows from part 2 of [Lemma 11](#lem11){: data-lid="227wl" } and the fact that $X$ is covered by finitely many $U_i$. Since addition of Cartier divisors is multiplication of the $f_i$ and each $\ord_Y$ is a group homomorphism, this correspondence is a group homomorphism, and that the image of $\divisor(f)=\{(X,f)\}$ is the $\divisor(f)$ of [Definition 13](#def13){: data-lid="qamdv" } is immediate from the definition.

Let us show injectivity. If the image of $D=\{(U_i,f_i)\}$ is $0$, then for each $i$, whenever $U_i$ meets a prime divisor $Y$, we have $\ord_Y(f_i)=0$. We show that $f_i$ is an invertible section on $U_i$. Applying the equality $\Gamma(V,\mathcal{O}_X)=\bigcap_{x\in V}\mathcal{O}_{X,x}$ seen at the beginning of this section to $f_i$ and $f_i^{-1}$, it suffices to show that for each $x\in U_i$, we have $f_i\in \mathcal{O}_{X,x}^\times$.

The ring $R=\mathcal{O}_{X,x}$ is a Noetherian normal local domain, and a codimension $1$ prime ideal of $R$, $\mathfrak{p}$, corresponds to a prime divisor passing through $x$ and meeting $U_i$, namely $Y$, and $R_\mathfrak{p}=\mathcal{O}_{X,\eta_Y}$. Then, by the (S2) condition of [\[Commutative Algebra\] §Regular Local Rings, ⁋Theorem 10](/en/math/commutative_algebra/regular_local_rings#thm10){: data-lid="f5pss" }, the associated primes of a principal ideal generated by a non-zerodivisor of $R$ all have codimension $1$, so the right-hand side of the equality

$$R=\bigcap_{\text{\scriptsize $\mathfrak{p}$ associated to a non-zerodivisor}}R_\mathfrak{p}$$

given by [\[Commutative Algebra\] §Regular Local Rings, ⁋Proposition 7](/en/math/commutative_algebra/regular_local_rings#prop7){: data-lid="mmbxe" } contains the intersection over codimension $1$ primes $\mathfrak{p}$. By assumption, $\ord_Y(f_i)=0$, so $f_i$ and $f_i^{-1}$ belong to the localization at every codimension $1$ prime ideal, and hence, both being elements of $R$, we have $f_i\in R^\times$. That is, every $f_i$ is an invertible section on $U_i$, and by the equivalence relation of [Definition 6](#def6){: data-lid="7e6ps" }, $D$ is the same Cartier divisor as $\{(U_i,1)\}$, namely the identity in $\CaDiv(X)$.

Now suppose $X$ is factorial, and we show surjectivity. Suppose a Weil divisor $D=\sum_Y n_YY$ is given, and fix a point $x\in X$. Since $D$ is a finite sum, among prime divisors passing through $x$, only finitely many $Y$ have $n_Y\neq0$, and to each there corresponds in $\mathcal{O}_{X,x}$ a codimension $1$ prime ideal $\mathfrak{p}_Y$. Since $X$ is factorial, $\mathcal{O}_{X,x}$ is a UFD, and by part 1 of [\[Commutative Algebra\] §Homological Criterion for Regularity, ⁋Lemma 8](/en/math/commutative_algebra/homological_criterion_for_regularity#lem8), $\mathfrak{p}_Y=(g_Y)$ is principal.

Set $f_x=\prod_Y g_Y^{n_Y}\in K(X)^\times$. The product is taken over the prime divisors passing through $x$, of which there are finitely many $Y$. Then $E=\divisor(f_x)-D$ is a sum of finitely many prime divisors, and by construction no prime divisor passing through $x$ appears in $E$. Indeed, for a prime divisor passing through $x$, denoted $Y'$, $\ord_{Y'}(g_Y)$ is, when $Y'=Y$, $1$, and otherwise $0$, because for $g_Y$ as a prime element of $\mathcal{O}_{X,x}$, belonging to $\mathfrak{p}_{Y'}$ is equivalent to $\mathfrak{p}_{Y'}=\mathfrak{p}_Y$. Therefore, the union of prime divisors appearing in $E$ is a closed set not containing $x$, and on its complement $U_x$, $\divisor(f_x)$ and $D$ agree.

Shrink these obtained open sets to be affine to obtain an affine open cover of $X$, $\{U_x\}$. Then since both $\divisor(f_x)$ and $\divisor(f_{x'})$ agree on $U_x\cap U_{x'}$ with $D$, the quotient $f_x/f_{x'}$ has $\ord$ equal to $0$ on every prime divisor meeting the overlap, and applying the injectivity argument above to the open set $U_x\cap U_{x'}$ shows that this is a section of $\mathcal{O}_X^\times$. Thus $\{(U_x,f_x)\}$ is a Cartier divisor whose image is $D$. Finally, since principal divisors correspond to each other, an isomorphism between the quotients $\CaCl(X)\cong\Cl(X)$ is induced.
:::

The final claim of [Proposition 14](#prop14){: data-lid="i6dq8" } is that the two divisor theories agree on a factorial scheme, which extends [Proposition 5](#prop5){: data-lid="zglcf" }, which applied to the effective case, to arbitrary coefficients. Combining this with [Theorem 10](#thm10){: data-lid="wdumy" }, in the factorial case we obtain $\Cl(X)\cong\CaCl(X)\cong\Pic(X)$. On a general normal scheme, the image of $\CaDiv(X)$ can be a proper subgroup of $\Div(X)$, and the difference measures the extent to which singularities of $X$ prevent a codimension $1$ part from being cut out locally by a single equation.

## Linear Systems

We now quickly review the content of [\[Algebraic Varieties\] §Linear Systems](/en/math/algebraic_varieties/linear_systems){: data-lid="a7yj9" }. Given a divisor $D$, the natural question is which effective divisors lie in its linear equivalence class, and [Definition 8](#def8){: data-lid="7lxzt" } turns this question into one about global sections of $\mathcal{O}_X(D)$.

::: Proposition 15
For an integral Noetherian scheme $X$ and a Cartier divisor $D$, for each $0\neq s\in \Gamma(X,\mathcal{O}_X(D))$, $D+\divisor(s)$ is an effective Cartier divisor, and this correspondence is a surjection onto all effective Cartier divisors linearly equivalent to $D$. Moreover, two sections $s,s'$ give the same divisor if and only if $s'/s\in \Gamma(X,\mathcal{O}_X)^\times$.
:::
::: Proof
Let $D=\{(U_i,f_i)\}$. That $s\in\Gamma(X,\mathcal{O}_X(D))$ means that for all $i$, $sf_i\in \Gamma(U_i,\mathcal{O}_X)$, and since $D+\divisor(s)=\{(U_i,sf_i)\}$, this means precisely that $D+\divisor(s)$ is effective. Conversely, if $D'$ is effective and $D'-D=\divisor(h)$, then $D'=\{(U_i,hf_i)\}$, so $hf_i\in\Gamma(U_i,\mathcal{O}_X)$, hence $h\in \Gamma(X,\mathcal{O}_X(D))$ and its image is $D'$.

Finally, $D+\divisor(s)=D+\divisor(s')$ is equivalent to $\divisor(s'/s)=0$, and by the equivalence relation of [Definition 6](#def6){: data-lid="4i7sk" }, this means that $s'/s$ is, on each $U_i$, a section of $\mathcal{O}_X^\times$, that is, $s'/s\in \Gamma(X,\mathcal{O}_X)^\times$.
:::

Therefore, effective divisors linearly equivalent to $D$ are in one-to-one correspondence with sections of $\Gamma(X,\mathcal{O}_X(D))$ other than $0$ modulo the action of $\Gamma(X,\mathcal{O}_X)^\times$. When $X$ is a scheme over a field $\mathbb{K}$ and $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$, this quotient becomes the projectivization of a vector space, recovering [\[Algebraic Varieties\] §Linear Systems, ⁋Definition 2](/en/math/algebraic_varieties/linear_systems#def2){: data-lid="tsnz6" }.

::: Definition 16
Over a field $\mathbb{K}$, let $X$ be an integral scheme satisfying $\Gamma(X,\mathcal{O}_X)=\mathbb{K}$. For an invertible sheaf $\mathcal{L}$, its *complete linear system* is

$$\lvert \mathcal{L}\rvert=\mathbb{P}(\Gamma(X,\mathcal{L}))$$

and a *linear system* of $\mathcal{L}$ is the system defined by a subspace $V\subseteq \Gamma(X,\mathcal{L})$ as $\mathbb{P}(V)\subseteq \lvert\mathcal{L}\rvert$.
:::

By [Proposition 15](#prop15){: data-lid="ol2ws" }, when $\mathcal{L}=\mathcal{O}_X(D)$, $\lvert\mathcal{L}\rvert$ is identified with the set of effective divisors linearly equivalent to $D$, and in this case we also write this as $\lvert D\rvert$. For a linear system $\mathbb{P}(V)$, the set of points where all sections of $V$ vanish is called its *base locus*, and a linear system with empty base locus gave a morphism to projective space. ([\[Algebraic Varieties\] §Linear Systems, ⁋Definition 5](/en/math/algebraic_varieties/linear_systems#def5){: data-lid="oe4s1" }) Our final section is about this. 

## Ample invertible sheaf

An $\mathcal{O}_X$-module $\mathcal{F}$ is called *globally generated* if for each point $x$, the stalk $\mathcal{F}_x$ is generated as an $\mathcal{O}_{X,x}$-module by the germs of global sections. This is the scheme-theoretic translation of the condition that the evaluation map is surjective in [\[Algebraic Varieties\] §Cohomology of Projective Space, ⁋Definition 4](/en/math/algebraic_varieties/cohomology_of_projective_spaces#def4){: data-lid="3zs54" }, and for an invertible sheaf $\mathcal{L}$, the condition that a linear system $\mathbb{P}(V)$ has empty base locus is the same as the condition that the sections of $V$ globally generate $\mathcal{L}$.

Generating sections determine a morphism to projective space. Over a ring $A$, let a scheme $X$, an invertible sheaf $\mathcal{L}$, and sections $s_0,\ldots, s_n\in \Gamma(X,\mathcal{L})$ globally generating it be given. For each $i$,

$$X_{s_i}=\{x\in X\mid \text{$(s_i)_x$ generates $\mathcal{L}_x$}\}$$

is an open set. This is because on a trivializing open set of $\mathcal{L}$, $s_i$ corresponds to a single function, and the set of points where that function is a unit is an open set. Also, since the $s_i$ globally generate $\mathcal{L}$, $\{X_{s_i}\}$ is an open cover of $X$, and on $X_{s_i}$, $s_i$ gives a trivialization of $\mathcal{L}$, so for each $j$, $s_j/s_i\in \Gamma(X_{s_i},\mathcal{O}_X)$ is well-defined. Now $D_+(\x_i)$ is isomorphic to $\Spec A[\x_0,\ldots,\x_n]_{(\x_i)}$ ([§Projective Space and the Proj Construction, ⁋Theorem 10](/en/math/scheme_theory/projective_schemes#thm10){: data-lid="lunk6" }), so the ring homomorphism

$$A[\x_0,\ldots, \x_n]_{(\x_i)} \rightarrow \Gamma(X_{s_i},\mathcal{O}_X);\qquad \frac{\x_j}{\x_i}\mapsto \frac{s_j}{s_i}$$

gives a morphism $X_{s_i} \rightarrow D_+(\x_i)$ by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="cidwz" }. On intersections, these morphisms agree with each other by $s_k/s_i=(s_k/s_j)(s_j/s_i)$, so applying [§Morphisms of Schemes, ⁋Proposition 1](/en/math/scheme_theory/morphism_of_schemes#prop1){: data-lid="v87x4" } to an affine open cover of $X$ obtained by covering each $X_{s_i}$ with affine open subsets, they define a single morphism

$$\varphi:X \rightarrow \mathbb{P}^n_A$$

That is, choosing generating sections of $\mathcal{L}$ is choosing a way to represent $X$ inside projective space.

Here $\mathcal{L}$ itself is recovered from $\varphi$. Namely, $\mathcal{L}\cong \varphi^\ast\mathcal{O}(1)$, and this isomorphism sends $s_i$ to $\varphi^\ast\x_i$. Indeed, $\x_i$ on $D_+(\x_i)$ generates $\mathcal{O}(1)$, and $\varphi$ sends $X_{s_i}$ into $D_+(\x_i)$, so $\varphi^\ast\x_i$ on $X_{s_i}$ trivializes $\varphi^\ast\mathcal{O}(1)$, while $s_i$ trivializes $\mathcal{L}$ on the same open set. On the overlap $X_{s_i}\cap X_{s_j}$, the transition functions of the two trivializations are $s_j/s_i$ and $\varphi^\ast(\x_j/\x_i)$, respectively, and since the construction of $\varphi$ set these two to be equal, the isomorphisms given by $s_i\mapsto \varphi^\ast\x_i$ on each $X_{s_i}$ agree on the overlap and glue to an isomorphism on all of $X$.

::: Definition 17
For a Noetherian ring $A$ and a finite type $A$-scheme $X$, an invertible sheaf $\mathcal{L}$ is called *very ample* if there exist finitely many sections globally generating $\mathcal{L}$, $s_0,\ldots, s_n\in \Gamma(X,\mathcal{L})$, such that the morphism $\varphi:X \rightarrow \mathbb{P}^n_A$ they define is a locally closed embedding. ([§Closed Subschemes, ⁋Definition 8](/en/math/scheme_theory/closed_subschemes#def8){: data-lid="11qus" })
:::

Thus a very ample invertible sheaf is data realizing $X$ as a subspace of projective space, and even if $X$ does not itself lie in projective space, we can assign coordinates to it through this.

However, in general, $\mathcal{L}$ being globally generated is a strong condition. For example, if sections fail to globally generate $\mathcal{L}$, then $\varphi$ itself is not defined. To solve this problem, what we used was tensoring $\mathcal{L}$ multiple times. Multiplication $\Gamma(X,\mathcal{L})^{\otimes m} \rightarrow \Gamma(X,\mathcal{L}^{\otimes m})$ produces, from sections of $\mathcal{L}$, sections of $\mathcal{L}^{\otimes m}$, and since sections generally exist outside its image as well, the larger $m$ becomes, the more sections we have to work with. For example, on $\mathbb{P}^n$, $\Gamma(\mathcal{O}(1))$ is the $n+1$-dimensional space of linear polynomials, while $\Gamma(\mathcal{O}(m))$ is the space of degree $m$ homogeneous polynomials, of dimension $\binom{n+m}{n}$.

Then we can ask whether $\mathcal{L}^{\otimes m}$ is very ample for some $m>0$, and [\[Algebraic Varieties\] §Linear Systems, ⁋Definition 10](/en/math/algebraic_varieties/linear_systems#def10){: data-lid="6esw5" } actually took this as the definition of ample. However, this description passes through an ambient projective space and cannot be used without the assumption that $X$ is a finite type scheme over a Noetherian ring. Instead, we choose a definition that works for arbitrary Noetherian schemes by taking as the condition only how well twisting spreads out a sheaf.

::: Definition 18
On a Noetherian scheme $X$, an invertible sheaf $\mathcal{L}$ is called *ample* if for every coherent sheaf $\mathcal{F}$ ([§Quasi-Coherent Sheaves, ⁋Definition 11](/en/math/scheme_theory/quasicoherent_sheaves#def11){: data-lid="34vt8" }) there exists $n_0$ such that for all $n\geq n_0$, $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{L}^{\otimes n}$ is globally generated.
:::

This definition only demands the existence of sections and does not directly mention a morphism to projective space. Requiring the condition for all coherent sheaves is essential: if we required it only for $\mathcal{F}=\mathcal{O}_X$, that is, only that $\mathcal{L}^{\otimes n}$ is globally generated, this would contain no information about $X$ at all. On the other hand, requiring it for arbitrary $\mathcal{F}$ asks whether twisting by $\mathcal{L}$ lifts all local data on $X$ to global sections, and this becomes a condition strong enough to substitute for the existence of an embedding. The following are properties that are obtained immediately from this definition.

::: Proposition 19
On a Noetherian scheme $X$, for an invertible sheaf $\mathcal{L}$, the following hold.

1. If $X$ is affine, then $\mathcal{L}$ is always ample.
2. For $m\geq 1$, $\mathcal{L}$ is ample if and only if $\mathcal{L}^{\otimes m}$ is ample.
3. If $\mathcal{L}$ is ample and an invertible sheaf $\mathcal{M}$ is globally generated, then $\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{M}$ is also ample.
:::
::: Proof
For (1), let $X=\Spec A$ and choose a coherent sheaf $\mathcal{F}$. Since $\mathcal{L}$ is an invertible sheaf, $\mathcal{L}^{\otimes n}$ is isomorphic to $\mathcal{O}_X$ on an open neighborhood of each point, and so $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is isomorphic to $\mathcal{F}$ on that neighborhood. Since quasi-coherence is a local condition, from this $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is a quasi-coherent sheaf, and hence is, for some $A$-module $M$, the associated sheaf $\widetilde{M}$. ([§Quasi-Coherent Sheaves, ⁋Theorem 10](/en/math/scheme_theory/quasicoherent_sheaves#thm10){: data-lid="cs38j" }) But the stalk of $\widetilde{M}$ is $M_\mathfrak{p}$ ([§Quasi-Coherent Sheaves, ⁋Proposition 5](/en/math/scheme_theory/quasicoherent_sheaves#prop5){: data-lid="5aeut" }), and this is generated by the image of the global section module $M$, so $\widetilde{M}$ is globally generated. Hence we can take $n_0=0$.

In (2), if $\mathcal{L}$ is ample, for a coherent sheaf $\mathcal{F}$, choose $n_0$ so that for each $n\geq n_0$, $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated. Then for $k\geq n_0$, we have $mk\geq n_0$, so $\mathcal{F}\otimes(\mathcal{L}^{\otimes m})^{\otimes k}$ is globally generated. Conversely, suppose $\mathcal{L}^{\otimes m}$ is ample. For each $j=0,1,\ldots, m-1$, the sheaf $\mathcal{F}\otimes\mathcal{L}^{\otimes j}$ is also coherent, so there exists $k_j$ such that for each $k\geq k_j$, $\mathcal{F}\otimes\mathcal{L}^{\otimes j}\otimes(\mathcal{L}^{\otimes m})^{\otimes k}$ is globally generated. Setting $k_\ast=\max_jk_j$, for any $n\geq mk_\ast$, $n$ can be written as $n=mk+j$ ($k\geq k_\ast$, $0\leq j<m$), so $\mathcal{F}\otimes\mathcal{L}^{\otimes n}$ is globally generated.

For (3), we first observe that the tensor product of two globally generated $\mathcal{O}_X$-modules $\mathcal{F},\mathcal{G}$ is again globally generated. This is because the stalk $(\mathcal{F}\otimes\mathcal{G})_x\cong \mathcal{F}_x\otimes_{\mathcal{O}_{X,x}}\mathcal{G}_x$ is generated by tensors of generators of $\mathcal{F}_x$ and $\mathcal{G}_x$, and these are tensors of germs of global sections. Now for a coherent sheaf $\mathcal{F}$, by the ampleness of $\mathcal{L}$, choose $n_0$; then for $n\geq n_0$,

$$\mathcal{F}\otimes(\mathcal{L}\otimes\mathcal{M})^{\otimes n}\cong(\mathcal{F}\otimes\mathcal{L}^{\otimes n})\otimes\mathcal{M}^{\otimes n}$$

where the first factor is globally generated and the second factor is a tensor power of a globally generated sheaf, hence globally generated. Therefore the left-hand side is also globally generated.
:::

By part 1 of [Proposition 19](#prop19){: data-lid="sdzx1" }, any invertible sheaf on an affine scheme is ample, so this condition filters nothing out when $X$ is affine. Ampleness actually distinguishes objects when $X$ is not affine; in particular, when $X$ is projective over a Noetherian ring $A$, $\mathcal{L}$ is ample if and only if, for some $m>0$, $\mathcal{L}^{\otimes m}$ is very ample.

---

**References**

**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).
