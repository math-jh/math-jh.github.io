---
title: "Complete Intersections"
description: "We study vanishing schemes defined by families of global sections and show that the codimension of a local complete intersection cut out by a regular sequence equals the number of defining equations. From the local free resolution given by the Koszul complex, we obtain that the conormal sheaf is a locally free sheaf of rank k, and for global complete intersections in projective space we compute the Hilbert polynomial and verify that its degree equals the product of the degrees of the defining equations."
excerpt: "Codimension of local complete intersections, Koszul resolutions, and Hilbert polynomials"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/complete_intersections
sidebar: 
    nav: "scheme_theory-en"

date: 2025-03-08
weight: 20
translated_at: 2026-08-10T22:05:29+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-10T22:05:29+00:00
---
One of the important examples of closed subschemes is the vanishing scheme defined in [§Closed Subschemes, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes#def7). Its motivation is, of course, the hypersurface $f=0$ in Euclidean space $\mathbb{R}^n$, defined as $f^{-1}(0)$ for a function $f: \mathbb{R}^n \rightarrow \mathbb{R}$.

More generally, we are also interested in the vanishing scheme $Z(s_1,\ldots, s_k)$ defined by a (finite) family of global sections $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$. Intuitively, this is obtained by first forming the vanishing scheme $\iota_1:Z(s_1)\hookrightarrow X$ using the global section $s_1$ on $X$, then finding the vanishing scheme of $s_2\vert_{Z(s_1)}$ on $Z(s_1)$ via the global section

$$s_2\vert_{Z(s_1)}=\iota_1^\sharp(X)(s_2)\in\bigl((\iota_1)_\ast \mathcal{O}_{Z(s_1)}\bigr)(X)=\Gamma(Z(s_1), \mathcal{O}_{Z(s_1)})$$

and repeating this process; of course, for this to be well-defined, the procedure must yield the same scheme regardless of the order of $s_1, \ldots, s_k$.

The case $k=1$, i.e., the case cut out by a single equation, was already treated under the name of effective Cartier divisor in [§Divisors and Linear Systems](/en/math/scheme_theory/divisors_and_linear_systems). In this post, we extend this to multiple equations to define local complete intersections, and we show that their codimension exactly matches the number of cutting equations. We then lift the results of [\[Commutative Algebra\] §Koszul Complex](/en/math/commutative_algebra/koszul_complex) to associated sheaves to obtain a locally free resolution of the structure sheaf, and from this we derive the characteristic property of local complete intersections: the conormal sheaf $\mathcal{I}/\mathcal{I}^2$ is a locally free sheaf of rank $k$. Finally, when cut out globally inside projective space, this resolution glues into a single global resolution, so we can compute the Euler characteristic using [§Sheaf Cohomology of Schemes](/en/math/scheme_theory/sheaf_cohomology_of_schemes) and read off the Hilbert polynomial and degree.

## Codimension and Complete Intersections

Let a scheme $X$ and global sections $s_1,\ldots, s_k\in \Gamma(X, \mathcal{O}_X)$ be given. On each affine open set $U=\Spec A$, the $s_i$ restrict to elements $s_i\vert_U$ of $A$, and we can consider the closed subscheme of $U$ defined by the ideal $(s_1\vert_U,\ldots, s_k\vert_U)$. These glue together as $U$ varies to define a closed subscheme of $X$, which we denote by $Z(s_1,\ldots, s_k)$ and call the *vanishing scheme* of $s_1,\ldots, s_k$. The defining ideal $(s_1,\ldots, s_k)$ is independent of the order of the $s_i$, so $Z(s_1,\ldots, s_k)$ is also order-independent; thus the process of finding the vanishing scheme of $s_2$ on $Z(s_1)$ is exactly realized as the scheme-theoretic intersection

$$Z(s_1,\ldots, s_k)=Z(s_1)\cap \cdots\cap Z(s_k)$$

because on each affine open we have $(s_1,\ldots, s_k)=\sum_{i=1}^k(s_i)$.

One of the things we expect from closed subschemes cut out in this way is their codimension. That is, it is natural to expect that if a given vanishing scheme is cut out by $k$ equations, then its codimension will be $k$. However, this does not hold in general. For example, in $\mathbb{A}^3_\mathbb{K}=\Spec\mathbb{K}[\x,\y,\z]$, the closed subscheme $Z(\x\y, \x\z)$ cut out by two equations might be expected to have codimension $2$, but in fact analyzing this scheme shows that it has two irreducible components $Z(\x)$ and $Z(\y,\z)$, whose respective codimensions are $1$ and $2$.

Intuitively, this is because if we consider the closed subscheme $Z(\x\y)$ cut out by the first equation $\x\y=0$ in $\mathbb{K}[\x,\y,\z]$, this subscheme has two components $Z(\x)$ and $Z(\y)$, and on $Z(\x)$ the second equation $\x\z$ already vanishes identically, so considering $Z(\x,\x\z)$ gives nothing more to cut out and we just get $Z(\x)$, while only on the second component $Z(\y)$ does $Z(\y,\x\z)$ acquire meaning, and computing the value on this component actually gives

$$Z(\y,\x\z)=Z(\y)\cap (Z(\x)\cup Z(\z))=Z(\x,\y)\cup Z(\y,\z)$$

and among these, $Z(\x,\y)$ is already contained in the first component $Z(\x)$, so the only thing that effectively remains is $Z(\y,\z)$, yielding the above description. The corresponding algebraic explanation is that in the coordinate ring $\mathbb{K}[\x,\y,\z]/(\x\y)$ of the closed subscheme cut out by the first equation, we have $\x\z\cdot\y=0$ while $\y\neq 0$, i.e., $\x\z$ is a zerodivisor. Therefore, to resolve this, it suffices to require that each equation remains a non-zerodivisor even after passing through the preceding equations. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Definition 2](/en/math/commutative_algebra/regular_local_rings#def2))

::: Definition 1
A closed embedding $\iota:Z\hookrightarrow X$ of a locally Noetherian scheme $X$ is called a *local complete intersection* of codimension $k$, or a *regular embedding* of codimension $k$, if there exists an affine open cover $\{U_i=\Spec A_i\}$ of $X$ such that whenever $Z\cap U_i\neq\emptyset$, we have $Z\cap U_i=Z(s_{i,1},\ldots, s_{i,k})$ and $(s_{i,1},\ldots, s_{i,k})$ is an $A_i$-regular sequence.
:::

Let us recall that the condition of being a regular sequence generally depended on the order in which the elements were listed. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Definition 2](/en/math/commutative_algebra/regular_local_rings#def2)) However, this dependence does not remain in [Definition 1](#def1), because if $\mathfrak{p}$ is a prime ideal of $A_i$ containing $(s_{i,1},\ldots, s_{i,k})$, then since localization is exact, $(s_{i,1},\ldots, s_{i,k})$ is an $(A_i)_\mathfrak{p}$-regular sequence, and in a Noetherian local ring a regular sequence contained in the maximal ideal remains a regular sequence under arbitrary reordering. ([\[Commutative Algebra\] §Koszul Complex, ⁋Corollary 10](/en/math/commutative_algebra/koszul_complex#cor10)) The reordered sequence may not again be a regular sequence over all of $A_i$, but since each module appearing at each stage has finitely many associated primes, we can choose $f\notin \mathfrak{p}$ avoiding all those not contained in $\mathfrak{p}$ at once, and then this holds over $(A_i)_f$; since [Definition 1](#def1) allows us freedom in choosing the cover, such a refined cover satisfies the condition.

Now let us justify our intuition before introducing this. One direction holds without any condition, because the codimension of a minimal prime containing an ideal generated by $k$ elements is always at most $k$. ([\[Commutative Algebra\] §Dimension, ⁋Theorem 7](/en/math/commutative_algebra/Krull_dimension#thm7)) Thus what we actually need to show is that the codimension does not become smaller than $k$.

::: Proposition 2
Every irreducible component of a local complete intersection $\iota:Z\hookrightarrow X$ of codimension $k$ has codimension $k$ in $X$.
:::
::: Proof
Fix an irreducible component $W$ of $Z$ and choose $U=\Spec A$ among the cover of [Definition 1](#def1) that meets $W$. Then there exists an appropriate $A$-regular sequence $s_1,\ldots, s_k$ satisfying $Z\cap U=Z(s_1,\ldots, s_k)$, and since $X$ is locally Noetherian, $A$ is a Noetherian ring. ([§The Topological Structure of Schemes, ⁋Lemma 13](/en/math/scheme_theory/topology_of_schemes#lem13)) On the other hand, by the correspondence of [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15), $W\cap U$ is an irreducible component of $Z\cap U$, and since the generic point of $W$ is dense in $W$, it lies in the nonempty open set $W\cap U$ and is dense there as well. That is, it is also the generic point of $W\cap U$, and letting $\mathfrak{p}$ be the prime ideal of $A$ corresponding to this point, $\mathfrak{p}$ is a minimal prime of $A/(s_1,\ldots, s_k)$, so

$$\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim\bigl(A/(s_1,\ldots, s_k)\bigr)_\mathfrak{p}=0$$

holds. ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8))

On the other hand, by [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8) we have $\codim_X W=\dim A_\mathfrak{p}$, so what we need to prove is that $\dim A_\mathfrak{p}$ equals $k$. Since we have seen from the above equation that $\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=0$, it suffices to show that the process of cutting by the $s_i$ lowers the dimension by exactly $1$ each time. First, since $\mathfrak{p}$ contains $(s_1,\ldots, s_k)$, the ideal $(s_1,\ldots, s_k)A_\mathfrak{p}$ is proper, and since localization is exact it preserves non-zerodivisors, so $(s_1,\ldots, s_k)$ is an $A_\mathfrak{p}$-regular sequence. That is, letting $R_i=A_\mathfrak{p}/(s_1,\ldots, s_i)$, each $R_i$ is a nonzero Noetherian local ring, the image of $s_{i+1}$ is a non-zerodivisor in the maximal ideal of $R_i$, and $R_i/s_{i+1}R_i=R_{i+1}$.

Now the inequality $\dim R_{i+1}\geq \dim R_i-1$ in one direction follows immediately from [\[Commutative Algebra\] §System of Parameters, ⁋Corollary 7](/en/math/commutative_algebra/system_of_parameters#cor7). For the opposite direction, which uses the fact that $s_{i+1}$ is a non-zerodivisor, first $s_{i+1}$ does not belong to any associated prime of $R_i$, so a prime ideal of $R_i$ containing $s_{i+1}$ is not minimal. ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)) Then for any chain of prime ideals of $R_{i+1}$, taking the preimage under the quotient map $R_i \rightarrow R_{i+1}$ of each term yields a chain of prime ideals of $R_i$ of the same length, each containing $s_{i+1}$. ([\[Commutative Algebra\] §Basic Notions, ⁋Proposition 11](/en/math/commutative_algebra/basic_notions#prop11)) The smallest term $\mathfrak{q}$ of this chain contains $s_{i+1}$, so it is not minimal, and thus we can append a prime ideal $\mathfrak{q}'\subsetneq \mathfrak{q}$ of $R_i$ below the chain to obtain a chain in $R_i$ that is one longer. Hence $\dim R_{i+1}+1\leq \dim R_i$.

From the above we have $\dim R_{i+1}=\dim R_i-1$, and applying this successively for $i=0,1,\ldots, k-1$ yields

$$0=\dim A_\mathfrak{p}/(s_1,\ldots, s_k)=\dim A_\mathfrak{p}-k$$

so $\dim A_\mathfrak{p}=k$, i.e., $\codim_X W=k$.
:::

Now let us look at some simple examples.

::: Example 3
1. Consider affine space $\mathbb{A}^n_\mathbb{K}=\Spec\mathbb{K}[\x_1,\ldots, \x_n]$ and a nonconstant polynomial $f$. Since $\mathbb{K}[\x_1,\ldots, \x_n]$ is an integral domain, $0\neq f$ is a non-zerodivisor, and thus the hypersurface $Z(f)\hookrightarrow\mathbb{A}^n_\mathbb{K}$ is an effective Cartier divisor, i.e., a local complete intersection of codimension $1$.

2. Consider the closed embedding $Z(\x_{n-k+1},\ldots, \x_n)\hookrightarrow \mathbb{A}^n_\mathbb{K}$. For each $i$,

	$$\mathbb{K}[\x_1,\ldots, \x_n]/(\x_{n-k+1},\ldots, \x_{n-k+i})\cong\mathbb{K}[\x_1,\ldots, \x_{n-k},\x_{n-k+i+1},\ldots, \x_n]$$

	is an integral domain, so $\x_{n-k+i+1}$ is a non-zerodivisor in this ring. That is, $(\x_{n-k+1},\ldots, \x_n)$ is a regular sequence, and $Z(\x_{n-k+1},\ldots, \x_n)$ is a local complete intersection of codimension $k$. Consistently with [Proposition 2](#prop2), the codimension of this closed subscheme is exactly $k$.
:::

Conversely, having codimension $k$ does not imply being a local complete intersection. For example, the union $Z(\x_1,\x_2)\cup Z(\x_3,\x_4)$ of two planes meeting only at the origin in $\mathbb{A}^4_\mathbb{K}$ has codimension $2$ but is not a local complete intersection. Each plane is cut out by two equations, but near the origin where they meet two equations are insufficient, and we verify this in the discussion after [Proposition 5](#prop5).

## Koszul Complex and Normal Bundle

What [Definition 1](#def1) requires is that locally a single regular sequence cuts out $Z$, and the tool used to handle this condition is the Koszul complex. For elements $x_1,\ldots, x_n$ of a ring $A$, their *Koszul complex* $K(x_1,\ldots, x_n)$ is the complex whose $j$-th term is $A^{\oplus\binom{n}{j}}$

$$0 \rightarrow A^{\oplus\binom{n}{n}} \rightarrow A^{\oplus\binom{n}{n-1}} \rightarrow \cdots \rightarrow A^{\oplus\binom{n}{1}} \rightarrow A \rightarrow 0$$

Here the $j$-th term has basis elements $e_{i_1}\wedge\cdots\wedge e_{i_j}$ corresponding to indices satisfying $i_1<\cdots<i_j$, and the differential is given on each basis element by the alternating sum of deleting each $e_{i_k}$ and multiplying by $x_{i_k}$:

$$\dd{(e_{i_1}\wedge\cdots\wedge e_{i_j})}=\sum_{k=1}^j(-1)^{k-1}x_{i_k}e_{i_1}\wedge\cdots\wedge\widehat{e_{i_k}}\wedge\cdots\wedge e_{i_j}$$

Since the homology of this complex contains everything we need, we introduce the basic results of [\[Commutative Algebra\] §Koszul Complex](/en/math/commutative_algebra/koszul_complex).

First, the homology at both ends of this complex are familiar objects: $H_0$ is the quotient $A/(x_1,\ldots, x_n)$ and $H_n$ is the set of elements annihilated by all the $x_i$. Also, Koszul homology is always annihilated by $(x_1,\ldots, x_n)$, so in the extreme case where the cutting equations generate the unit ideal, all homology vanishes. The most important fact is that if $x_1,\ldots, x_n$ is a regular sequence, then $H_i$ vanishes for all $i\geq 1$, and as a result $K(x_1,\ldots, x_n)$ becomes a finite free resolution of $A/(x_1,\ldots, x_n)$. Intuitively, looking at the simplest case $n=1$, in the complex

$$0 \rightarrow A\overset{x_1}{\longrightarrow}A \rightarrow 0$$

we have

$$H_1=\ker(A\overset{x_1}{\longrightarrow}A)=\{a\in A\mid x_1a=0\}$$

so the vanishing of $H_1$ is exactly the condition that $x_1$ is a non-zerodivisor, and the Koszul complex is the lifting of this to all degrees and sequences of arbitrary length. Transporting this to the associated sheaf means that the structure sheaf of a local complete intersection has an explicit finite free resolution on each chart.

::: Proposition 4
Let $\iota:Z\hookrightarrow X$ be a codimension $k$ local complete intersection in a locally Noetherian scheme $X$, and let $U=\Spec A$ be an affine open subset meeting $Z$ nontrivially, with $Z\cap U=Z(s_1,\ldots, s_k)$ where $s_1,\ldots, s_k$ is an $A$-regular sequence. Then the sequence of $\mathcal{O}_U$-modules

$$0 \rightarrow \mathcal{O}_U^{\oplus\binom{k}{k}} \rightarrow \mathcal{O}_U^{\oplus\binom{k}{k-1}} \rightarrow \cdots \rightarrow \mathcal{O}_U^{\oplus\binom{k}{1}} \rightarrow \mathcal{O}_U \rightarrow (\iota_\ast\mathcal{O}_Z)\vert_U \rightarrow 0$$

is exact. Here $\mathcal{O}_U^{\oplus\binom{k}{j}}$ is the sheaf associated to the $j$-th term of the Koszul complex $K(s_1,\ldots, s_k)$, and the differential is also the one obtained by passing the differential of that complex to the associated sheaf.
:::
::: Proof
We have previously seen that if $s_1,\ldots, s_k$ is an $A$-regular sequence, then $K(s_1,\ldots, s_k)$ becomes a free resolution of $A/(s_1,\ldots, s_k)$. Since the associated sheaf functor is exact ([§Quasi-coherent Sheaves, ⁋Proposition 6](/en/math/scheme_theory/quasicoherent_sheaves#prop6)), passing to the associated sheaf preserves this exactness, which gives the first part of the proposition. For the last term, since $Z\cap U=Z(s_1,\ldots, s_k)$ is $\Spec A/(s_1,\ldots, s_k)$ and pushing forward its structure sheaf along the closed embedding gives the associated sheaf, we have $(\iota_\ast\mathcal{O}_Z)\vert_U\cong \widetilde{A/(s_1,\ldots, s_k)}$.
:::

For the ideal sheaf $\mathcal{I}=\mathcal{I}_{Z/X}$ of $Z$, $\mathcal{I}$ acts trivially on $\mathcal{I}/\mathcal{I}^2$, so its $\mathcal{O}_X$-module structure is given via $\mathcal{O}_X/\mathcal{I}\cong\iota_\ast\mathcal{O}_Z$, and thus $\mathcal{I}/\mathcal{I}^2$ can be regarded as a quasi-coherent sheaf on $Z$. Geometrically this is the conormal sheaf of $Z$, and we show that for a local complete intersection this sheaf becomes a locally free sheaf of rank $k$, hence a conormal *bundle*.

Let us first look at the fiber of this sheaf at each point. Take an affine open subset $\Spec A$ containing an arbitrary point $z\in Z$, let $\mathfrak{a}$ be the ideal corresponding to $\mathcal{I}$ and $\mathfrak{p}$ the prime corresponding to $z$. Then the stalk of $\mathcal{I}$ is $\mathfrak{a}_\mathfrak{p}$ and the maximal ideal of $\mathcal{O}_{Z,z}=A_\mathfrak{p}/\mathfrak{a}_\mathfrak{p}$ is $\mathfrak{p}A_\mathfrak{p}/\mathfrak{a}_\mathfrak{p}$, so the fiber at $z$ is

$$(\mathcal{I}/\mathcal{I}^2)\otimes\kappa(z)=\mathfrak{a}_\mathfrak{p}/(\mathfrak{a}_\mathfrak{p}^2+\mathfrak{p}\mathfrak{a}_\mathfrak{p})=\mathfrak{a}_\mathfrak{p}/\mathfrak{p}\mathfrak{a}_\mathfrak{p}$$

where the last equality is algebraic: if $z\in Z$ then $\mathfrak{a}\subseteq \mathfrak{p}$, hence $\mathfrak{a}_\mathfrak{p}^2\subseteq \mathfrak{p}\mathfrak{a}_\mathfrak{p}$. Then by the second result of [\[Commutative Algebra\] §Integral Extensions, ⁋Lemma 8](/en/math/commutative_algebra/integral_extension#lem8), the elements of $\mathfrak{a}_\mathfrak{p}$ generating this ideal is equivalent to their images spanning the $\kappa(z)$-vector space $\mathfrak{a}_\mathfrak{p}/\mathfrak{p}\mathfrak{a}_\mathfrak{p}$, so the dimension of the fiber equals the minimum number of elements needed to generate $\mathcal{I}_z$. The Jacobson radical condition required by this lemma is automatically satisfied in the local ring $A_\mathfrak{p}$ where $J(A_\mathfrak{p})=\mathfrak{p}A_\mathfrak{p}$.

This count has been measured at a single point $z$ for now, but its value can be thought of as measured in a neighborhood of $z$. Since $X$ is locally Noetherian, $A$ is Noetherian and hence $\mathfrak{a}$ is finitely generated, so $\mathcal{I}$ is of finite type; consequently, as we saw in [§Quasi-coherent Sheaves](/en/math/scheme_theory/quasicoherent_sheaves), sections generating the stalk at a point generate the whole sheaf in some neighborhood of that point. That is, the dimension of the fiber is the minimum number of equations needed to cut out $Z$ in a neighborhood of $z$.

For a local complete intersection, our main point is that this number is controlled to be exactly one value. For one inequality, what [Definition 1](#def1) requires is that $Z$ is locally cut out by $k$ equations, so the fiber dimension is at most $k$ at every point of $Z$. For the opposite inequality, this count cannot drop below the codimension: taking an irreducible component $W$ of $Z$ passing through $z$ and letting $\mathfrak{q}$ be the prime of $A$ corresponding to its generic point, $\mathfrak{q}A_\mathfrak{p}$ is a minimal prime containing $\mathfrak{a}_\mathfrak{p}$ and by [Proposition 2](#prop2) and [§Dimension, ⁋Proposition 8](/en/math/scheme_theory/dimension#prop8) its codimension is $\codim_XW=k$, so [\[Commutative Algebra\] §Dimension, ⁋Theorem 7](/en/math/commutative_algebra/Krull_dimension#thm7) tells us that the number of elements generating $\mathfrak{a}_\mathfrak{p}$ is at least $k$. Thus the conormal sheaf of a local complete intersection has fiber of dimension exactly $k$ at every point. However, having constant fiber dimension does not by itself make a sheaf locally free: for example, the module $A/(\x)$ over $A=\mathbb{K}[\x]/(\x^2)$ has $1$-dimensional fiber at the unique point of $\Spec A$ but is not a free $A$-module. What resolves this is the regular sequence condition: the vanishing of $H_1(K(s_1,\ldots, s_k))$ used in [Proposition 4](#prop4) means that relations $\sum_ia_is_i=0$ are all combinations of the trivial relations $s_ie_j-s_je_i$, and the $a_i$ appearing in such relations all lie in $\mathfrak{a}$, so on $\mathfrak{a}/\mathfrak{a}^2$ no relations remain among the $s_i$ and freeness is guaranteed.

Writing this observation precisely on each chart gives the following.

::: Proposition 5
For a codimension $k$ local complete intersection $\iota:Z\hookrightarrow X$ in a locally Noetherian scheme $X$ with ideal sheaf $\mathcal{I}=\mathcal{I}_{Z/X}$, the sheaf $\mathcal{I}/\mathcal{I}^2$ is a locally free sheaf of rank $k$ on $Z$.
:::
::: Proof
Since the claim is local, it suffices to consider the case $X=\Spec A$, $\mathfrak{a}=\mathcal{I}(X)=(s_1,\ldots, s_k)$ where $s_1,\ldots, s_k$ is an $A$-regular sequence. In this case $\mathcal{I}=\widetilde{\mathfrak{a}}$ and $\mathcal{I}^2=\widetilde{\mathfrak{a}^2}$, so we ultimately need to show that $\mathfrak{a}/\mathfrak{a}^2$ is a free $A/\mathfrak{a}$-module of rank $k$.

Define an $A/\mathfrak{a}$-linear map $\psi:(A/\mathfrak{a})^{\oplus k} \rightarrow \mathfrak{a}/\mathfrak{a}^2$ by $e_i\mapsto s_i+\mathfrak{a}^2$. Since $\mathfrak{a}$ is generated by the $s_i$, the map $\psi$ is surjective. To show injectivity, suppose $a_1,\ldots, a_k\in A$ satisfy $\sum_ia_is_i\in \mathfrak{a}^2$. Since $\mathfrak{a}^2$ is generated by the products $s_is_j$, there exist $b_{ij}\in A$ such that $\sum_ia_is_i=\sum_{i,j}b_{ij}s_is_j$, and setting $c_i=a_i-\sum_jb_{ij}s_j$ gives $\sum_ic_is_i=0$. Then as seen above, the vanishing of $H_1(K(s_1,\ldots, s_k))$ gives $c_i\in \mathfrak{a}$ for all $i$, so $a_i=c_i+\sum_jb_{ij}s_j\in \mathfrak{a}$, and hence $\sum_ia_ie_i=0$ in $(A/\mathfrak{a})^{\oplus k}$, so $\psi$ is injective.
:::

Thus the $k$ equations cutting out $Z$ locally form a basis of the conormal sheaf, and the normal direction of $Z$ has exactly as many degrees of freedom as the number of cutting equations.

We can now also verify the claim deferred just after [Example 3](#ex3). For $A=\mathbb{K}[\x_1,\ldots, \x_4]$, consider the union of two planes in $\mathbb{A}^4_\mathbb{K}=\Spec A$ meeting only at the origin, $Z=Z(\x_1,\x_2)\cup Z(\x_3,\x_4)$. If $Z$ were a local complete intersection of codimension $k$, then by [Proposition 2](#prop2) both irreducible components would have codimension $k$, so $k=2$, and by [Proposition 5](#prop5) the fiber of the conormal sheaf would have dimension $2$ at every point of $Z$. Hence finding a point where this dimension jumps would show that $Z$ is not a local complete intersection. First, the ideal defining $Z$ is

$$\mathfrak{a}=(\x_1,\x_2)\cap(\x_3,\x_4)=(\x_1\x_3, \x_1\x_4, \x_2\x_3, \x_2\x_4)$$

Every point of $Z$ other than the origin lies in one of the four charts $D(\x_i)$; for instance, in $A_{\x_1}$ we have $\x_3=\x_1^{-1}(\x_1\x_3)$ and $\x_4=\x_1^{-1}(\x_1\x_4)$ both in $\mathfrak{a}A_{\x_1}$, and the remaining two generators $\x_2\x_3, \x_2\x_4$ lie in the ideal generated by these two, so $\mathfrak{a}A_{\x_1}=(\x_3,\x_4)A_{\x_1}$. Here $A_{\x_1}$ and $A_{\x_1}/(\x_3)$ are both integral domains, so $\x_3,\x_4$ is a regular sequence, and the same calculation holds for the other three coordinates; thus away from the origin, $Z$ is a local complete intersection of codimension $2$, and by [Proposition 5](#prop5) the fiber dimension there is $2$.

The problematic point is the origin. Let $\mathfrak{m}=(\x_1,\x_2,\x_3,\x_4)$ be the corresponding maximal ideal; then the homogeneous elements of $\mathfrak{m}\mathfrak{a}$ all have degree at least $3$, whereas the four generators of $\mathfrak{a}$ all have degree $2$, so among their $\mathbb{K}$-linear combinations only $0$ lies in $\mathfrak{m}\mathfrak{a}$, and hence $\mathfrak{a}/\mathfrak{m}\mathfrak{a}$ is $4$-dimensional. This vector space is already annihilated by $\mathfrak{m}$ and elements of $A\setminus \mathfrak{m}$ act on it as elements of $\mathbb{K}^\times$, so localizing at $\mathfrak{m}$ does not change it; thus the fiber at the origin $\mathfrak{a}_\mathfrak{m}/\mathfrak{m}\mathfrak{a}_\mathfrak{m}$ is also $4$-dimensional. Therefore $Z$ is not a local complete intersection, and this is simultaneously an example where $\mathcal{I}/\mathcal{I}^2$ is not locally free.

## Hilbert Polynomial and Degree

What [Definition 1](#def1) requires is a local condition, but when homogeneous polynomials forming a single regular sequence in projective space cut out a subscheme globally, the local $\mathcal{O}_X$-module resolution of [Proposition 4](#prop4) glues into a single global resolution. In this section the ambient is always projective space, so we change notation: the symbol $X$ used for the ambient up to the previous section will here denote a closed subscheme of $\mathbb{P}^n$.

::: Proposition 6
Let $\mathbb{P}^n=\Proj S_\bullet$ ($S_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$) be projective space over a field $\mathbb{K}$, and let $f_1,\ldots, f_k$ be homogeneous polynomials of respective degrees $d_i>0$ forming an $S_\bullet$-regular sequence. Let $X=V_+(f_1,\ldots, f_k)$ and $\iota:X\hookrightarrow \mathbb{P}^n$ be its closed embedding ([§Closed Subschemes of Projective Space, ⁋Proposition 1](/en/math/scheme_theory/closed_subschemes_of_projective_spaces#prop1)). Then the following hold.

1. $\iota$ is a local complete intersection of codimension $k$, and for the affine open cover in [Definition 1](#def1) we may take the standard charts $\{D_+(\x_m)\}_{m=0}^n$.
2. Writing $d_J=\sum_{i\in J}d_i$ for $J\subseteq \{1,\ldots, k\}$, the sequence of $\mathcal{O}_{\mathbb{P}^n}$-modules

	$$0 \rightarrow \bigoplus_{\lvert J\rvert=k}\mathcal{O}(-d_J) \rightarrow \cdots \rightarrow \bigoplus_{\lvert J\rvert=1}\mathcal{O}(-d_J) \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow \iota_\ast\mathcal{O}_X \rightarrow 0$$

	is exact. Here the component from the summand with $\lvert J\rvert=j$ to the summand with $\lvert J'\rvert=j-1$ is multiplication by $f_i$ with the sign from the Koszul differential when $J'=J\setminus\{i\}$, and $0$ otherwise.
:::
::: Proof
Fix a chart $D_+(\x_m)=\Spec S_{(\x_m)}$ and set $g_i=f_i/\x_m^{d_i}\in S_{(\x_m)}$; then we know $X\cap D_+(\x_m)=Z(g_1,\ldots, g_k)$.

First, decomposing $S_{\x_m}$ by degree gives

$$S_{\x_m}=\bigoplus_{j\in\mathbb{Z}}\x_m^jS_{(\x_m)}$$

and each $\x_m^jS_{(\x_m)}$ is an $S_{(\x_m)}$-module isomorphic to $S_{(\x_m)}$. Since the $g_i$ have degree $0$, the ideal they generate is compatible with this decomposition, so for any $i$

$$S_{\x_m}/(g_1,\ldots, g_i)=\bigoplus_j\x_m^j\bigl(S_{(\x_m)}/(g_1,\ldots, g_i)\bigr)$$

and since $g_{i+1}$ has degree $0$, multiplication by $g_{i+1}$ preserves each component. Thus to check whether multiplication by $g_{i+1}$ is injective on $S_{\x_m}/(g_1,\ldots, g_i)$, it suffices to check this on $S_{(\x_m)}/(g_1,\ldots, g_i)$; moreover, since vanishing of the above direct sum is equivalent to vanishing of each component, $(g_1,\ldots, g_i)S_{\x_m}$ being a proper ideal is equivalent to $(g_1,\ldots, g_i)S_{(\x_m)}$ being a proper ideal.

Now suppose $X\cap D_+(\x_m)\neq\emptyset$, and let us show that $g_1,\ldots, g_k$ is an $S_{(\x_m)}$-regular sequence. ([\[Commutative Algebra\] §Regular Local Rings, ⁋Definition 2](/en/math/commutative_algebra/regular_local_rings#def2)) Then $Z(g_1,\ldots, g_k)\neq \emptyset$, so $(g_1,\ldots, g_k)$ is a proper ideal of $S_{(\x_m)}$, and by the degree decomposition above $(g_1,\ldots, g_k)S_{\x_m}$ is also proper. On the other hand, since $\x_m$ is a unit in $S_{\x_m}$, for each $i$ we have $(f_1,\ldots, f_i)S_{\x_m}=(g_1,\ldots, g_i)S_{\x_m}$ and $f_{i+1}$ and $g_{i+1}$ differ only by a unit. In particular $(f_1,\ldots, f_k)S_{\x_m}$ is a proper ideal, and since localization is exact, by hypothesis $f_1,\ldots, f_k$ is also an $S_{\x_m}$-regular sequence, and hence so is $g_1,\ldots, g_k$. Then as examined in the degree decomposition above, $g_1,\ldots, g_k$ is an $S_{(\x_m)}$-regular sequence. Now the standard affine charts $\{D_+(\x_m)\}_{m=0}^n$ form an affine open cover of $\mathbb{P}^n$, and for each of them $X\cap D_+(\x_m)$ is either empty or cut out by the regular sequence just obtained, so we get the first result.

For the second result, trivializing the summand $\mathcal{O}(-d_J)$ corresponding to $J$ with $\lvert J\rvert=j$ over the chart $D_+(\x_m)$ by the generating section $\x_m^{-d_J}$, the map $\mathcal{O}(-d_J) \rightarrow \mathcal{O}(-d_{J\setminus\{i\}})$ given by multiplication by $f_i$ becomes $\x_m^{-d_J}a\mapsto \x_m^{-d_{J\setminus\{i\}}}g_ia$, which is the same as multiplication by $g_i$ on this chart. That is, the restriction of the above sequence to $D_+(\x_m)$ is the associated sheaf of $K(g_1,\ldots, g_k)$ with $\widetilde{S_{(\x_m)}/(g_1,\ldots, g_k)}$ appended, and on charts meeting $X$ the exactness of this follows by applying [Proposition 4](#prop4) with ambient $D_+(\x_m)$ and closed subscheme $X\cap D_+(\x_m)$, together with the regular sequence property just obtained. On charts not meeting $X$, we have $(g_1,\ldots, g_k)=S_{(\x_m)}$ is the unit ideal, so all Koszul homology vanishes, and in particular $H_0=S_{(\x_m)}/(g_1,\ldots, g_k)=0$ so the last term also becomes $0$, and the sequence is again exact. Exactness is checked on stalks, and since these charts cover $\mathbb{P}^n$, the above sequence is exact.
:::

In such a case, each term of the Koszul complex is a finite direct sum of line bundles on projective space. The alternating sum of Euler characteristics vanishes on a finite exact sequence, and the Euler characteristic of twisting sheaves on projective space has already been computed explicitly, so from this single decomposition the Hilbert polynomial of $X$ is determined solely by the degrees of the cutting equations, and from that the dimension and degree follow. ([§Sheaf Cohomology of Schemes, ⁋Theorem 16](/en/math/scheme_theory/sheaf_cohomology_of_schemes#thm16))

::: Corollary 7
In the situation of [Proposition 6](#prop6), assume $X\neq \emptyset$. Then $k\leq n$, and the Hilbert polynomial of $X$ is

$$P_{\mathcal{O}_X}(t)=\sum_{J\subseteq\{1,\ldots, k\}}(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}.$$

Moreover, $\dim X=n-k$ and $\deg X=d_1\cdots d_k$.
:::
::: Proof
Tensoring the exact sequence of [Proposition 6](#prop6) with the invertible sheaf $\mathcal{O}(t)$ preserves exactness, and for a closed embedding we have $(\iota_\ast\mathcal{O}_X)\otimes\mathcal{O}(t)\cong \iota_\ast(\mathcal{O}_X(t))$, with cohomology preserved under $\iota_\ast$. (See the observation just before [§Sheaf Cohomology of Schemes, ⁋Theorem 8](/en/math/scheme_theory/sheaf_cohomology_of_schemes#thm8).) Hence $\rchi(X,\mathcal{O}_X(t))=\rchi(\mathbb{P}^n,\iota_\ast\mathcal{O}_X(t))$, and applying part 2 of [§Sheaf Cohomology of Schemes, ⁋Proposition 14](/en/math/scheme_theory/sheaf_cohomology_of_schemes#prop14) to this finite exact sequence and then computing each term via [§Sheaf Cohomology of Schemes, ⁋Corollary 15](/en/math/scheme_theory/sheaf_cohomology_of_schemes#cor15) yields

$$\rchi(X,\mathcal{O}_X(t))=\sum_{j=0}^k(-1)^j\sum_{\lvert J\rvert=j}\rchi\bigl(\mathbb{P}^n,\mathcal{O}(t-d_J)\bigr)=\sum_J(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n}.$$

By [§Sheaf Cohomology of Schemes, ⁋Theorem 16](/en/math/scheme_theory/sheaf_cohomology_of_schemes#thm16), the left-hand side is $P_{\mathcal{O}_X}(t)$.

It remains only to read off the degree and leading coefficient of this polynomial. First, for a polynomial $p$ of degree $m\geq 1$ with leading coefficient $c\neq 0$ and for $d>0$, one computes that $p(t)-p(t-d)$ has degree $m-1$ and leading coefficient $cmd$. If $p$ is constant, then $p(t)-p(t-d)=0$.

Now set $p_0(t)=\binom{n+t}{n}$ and define $p_i(t)=p_{i-1}(t)-p_{i-1}(t-d_i)$. By induction on $i$ one can show that

$$p_i(t)=\sum_{J\subseteq\{1,\ldots, i\}}(-1)^{\lvert J\rvert}\binom{n+t-d_J}{n},$$

and from this we see that $p_k$ is the polynomial obtained above. Here $p_0$ has degree $n$ and leading coefficient $1/n!$. If $k>n$, then by the above observation $p_n$ is constant and $p_{n+1}=0$, so $p_k=0$ and the degree of this polynomial would be $-\infty$; but since $X\neq\emptyset$ we have $\mathcal{O}_X\neq 0$, so by [§Sheaf Cohomology of Schemes, ⁋Theorem 16](/en/math/scheme_theory/sheaf_cohomology_of_schemes#thm16) the degree of $P_{\mathcal{O}_X}$ is $\dim X\geq 0$, a contradiction. Therefore $k\leq n$.

Then for each step $i=1,\ldots, k$, the degree $n-i+1$ of $p_{i-1}$ is at least $1$, so the above observation applies directly, and $p_i$ has degree $n-i$ with leading coefficient

$$\frac{1}{n!}\cdot nd_1\cdot (n-1)d_2\cdots (n-i+1)d_i=\frac{d_1\cdots d_i}{(n-i)!}.$$

Setting $r=n-k$, we see that $P_{\mathcal{O}_X}$ has degree $r$ and leading coefficient $d_1\cdots d_k/r!$; hence by [§Sheaf Cohomology of Schemes, ⁋Theorem 16](/en/math/scheme_theory/sheaf_cohomology_of_schemes#thm16) again we have $\dim X=r=n-k$, and by [§Sheaf Cohomology of Schemes, ⁋Definition 17](/en/math/scheme_theory/sheaf_cohomology_of_schemes#def17) we obtain $\deg X=r!\cdot d_1\cdots d_k/r!=d_1\cdots d_k$.
:::

For $k=1$, [Corollary 7](#cor7) says that a hypersurface of degree $e$ has $\deg X=e$, which agrees with the direct computation after [§Sheaf Cohomology of Schemes, ⁋Definition 17](/en/math/scheme_theory/sheaf_cohomology_of_schemes#def17). For general $k$, this is the simplest form of Bézout's theorem: the degree of the variety cut out by equations forming a regular sequence is the product of the degrees of those equations.

::: Example 8
1. Consider $X=V_+(f_1,f_2)$ cut out by two quadrics $f_1,f_2$ forming an $S_\bullet$-regular sequence inside $\mathbb{P}^3_\mathbb{K}=\Proj S_\bullet$. Since $n=3$, $k=2$, $d_1=d_2=2$, [Corollary 7](#cor7) gives

	$$P_{\mathcal{O}_X}(t)=\binom{3+t}{3}-2\binom{1+t}{3}+\binom{t-1}{3}=\frac{(t+3)(t+2)(t+1)-2(t+1)t(t-1)+(t-1)(t-2)(t-3)}{6}=4t.$$

	Hence $\dim X=1$ and $\deg X=1!\cdot 4=4$, and the arithmetic genus is $p_a(X)=(-1)^1\bigl(P_{\mathcal{O}_X}(0)-1\bigr)=1$. ([§Sheaf Cohomology of Schemes, ⁋Definition 17](/en/math/scheme_theory/sheaf_cohomology_of_schemes#def17))

2. Consider the twisted cubic $C$ in $\mathbb{P}^3_\mathbb{K}=\Proj \mathbb{K}[\x_0,\x_1,\x_2,\x_3]$. This is given by the morphism $\varphi:\mathbb{P}^1 \rightarrow \mathbb{P}^3_\mathbb{K}$ defined by the invertible sheaf $\mathcal{O}_{\mathbb{P}^1}(3)$ on $\mathbb{P}^1=\Proj \mathbb{K}[\y_0,\y_1]$ and its globally generating sections $\y_0^3, \y_0^2\y_1, \y_0\y_1^2, \y_1^3$. On the standard affine chart $D_+(\x_j)$, the corresponding ring homomorphism for $\varphi$ is $\x_i/\x_j\mapsto \y_0^{3-i}\y_1^i/\y_0^{3-j}\y_1^j$, and to show first that $C$ is a closed embedding we show that this ring homomorphism is surjective. For notational convenience we write $\t=\y_1/\y_0$.

	First, $\varphi^{-1}(D_+(\x_0))=D_+(\y_0)=\Spec\mathbb{K}[\t]$ and the coordinates $\s_1=\x_1/\x_0$, $\s_2=\x_2/\x_0$, $\s_3=\x_3/\x_0$ on $D_+(\x_0)$ map to $\t$, $\t^2$, $\t^3$ respectively, so the corresponding ring homomorphism is surjective, and from the isomorphism

	$$\mathbb{K}[\s_1,\s_2,\s_3]/(\s_2-\s_1^2, \s_3-\s_1^3)\cong\mathbb{K}[\s_1]\cong \mathbb{K}[\t]$$

	defined by $\s_1\mapsto \t$ we see that its kernel is exactly $(\s_2-\s_1^2, \s_3-\s_1^3)$. Similarly, on

	$$\varphi^{-1}(D_+(\x_1))=D_+(\y_0\y_1)=\Spec\mathbb{K}[\t,\t^{-1}]$$

	the coordinates $\s_1'=\x_0/\x_1$, $\s_2'=\x_2/\x_1$, $\s_3'=\x_3/\x_1$ on $D_+(\x_1)$ map to $\t^{-1}$, $\t$, $\t^2$ respectively, giving a surjection, and from the isomorphism

	$$\mathbb{K}[\s_1',\s_2',\s_3']/(\s_3'-{\s_2'}^2, \s_1'\s_2'-1)\cong\mathbb{K}[\s_2',{\s_2'}^{-1}]\cong \mathbb{K}[\t,\t^{-1}]$$

	defined by $\s_2'\mapsto \t$ we know the kernel of this ring homomorphism is $(\s_3'-{\s_2'}^2, \s_1'\s_2'-1)$. For the remaining two charts, renaming $\x_i'=\x_{3-i}$ and $\y_0'=\y_1$, $\y_1'=\y_0$, $\t'=\t^{-1}$ puts $\varphi$ in the same form $\x_i'\mapsto {\y_0'}^{3-i}{\y_1'}^i$, and since $D_+(\x_0')=D_+(\x_3)$ and $D_+(\x_1')=D_+(\x_2)$, the two calculations above carry over directly. Now the standard affine charts form an affine open cover of $\mathbb{P}^3_\mathbb{K}$, and the proof of [§Closed Subschemes, ⁋Proposition 3](/en/math/scheme_theory/closed_subschemes#prop3) showed that it suffices to verify this condition on a single affine open cover, so $\varphi$ is a closed embedding and therefore $C\cong\mathbb{P}^1$ with $\mathcal{O}_C(1)=\varphi^\ast\mathcal{O}(1)\cong \mathcal{O}_{\mathbb{P}^1}(3)$.

	Moreover, in the above calculations, in both cases the ambient is an integral domain and the quotients $\mathbb{K}[\s_1,\s_3]$ and $\mathbb{K}[\s_1',\s_2']$ by the first generator are also integral domains, so the two generators of each kernel form a regular sequence. That is, $C$ is a local complete intersection of codimension $2$, and from this

	$$P_{\mathcal{O}_C}(t)=\rchi\bigl(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(3t)\bigr)=\binom{1+3t}{1}=3t+1$$

	we obtain $\dim C=1$ and $\deg C=1!\cdot 3=3$.

	Our claim is that $C$ is *not* of the form $C=V_+(f_1,f_2)$ for two homogeneous polynomials $f_1,f_2$ forming an $S_\bullet$-regular sequence. If $C$ were of this form, then by [Corollary 7](#cor7) we would have $d_1d_2=3$. Then one of the two would have degree $1$, which would mean $C$ lies in a hyperplane $V_+(H)$. But pulling $H=\sum_ia_i\x_i$ back to $C\cong\mathbb{P}^1$ gives $\sum_ia_i\y_0^{3-i}\y_1^i$, and since $\y_0^3,\y_0^2\y_1,\y_0\y_1^2,\y_1^3$ are linearly independent in $\Gamma(\mathbb{P}^1,\mathcal{O}_{\mathbb{P}^1}(3))$, all $a_i$ must be zero. Hence no such $H$ can exist. On the other hand, as long as $C=V_+(f_1,f_2)$, the regular sequence hypothesis follows automatically: since $\dim C=1$, both $f_1$ and $f_2$ have positive degree, and if they had a non-constant common factor then the hypersurface it defines would be contained in $C$, giving the wrong dimension, so they are coprime; and since $S_\bullet$ is a UFD, $f_1\mid f_2g$ implies $f_1\mid g$, so $f_2$ is a non-zerodivisor in $S_\bullet/(f_1)$. Thus $C$ is an example of a local complete intersection of codimension $2$ that is not cut out globally by two homogeneous polynomials.
:::

---

**References**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 
