---
title: "Projective Schemes"
description: "We construct projective space by gluing affine lines in a suitable way, and generalize this to define projective schemes. We understand projective space from a topological viewpoint and examine how to glue affine lines via stereographic projection and cocycle conditions."
excerpt: "The Proj construction from graded rings and projective spaces"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/projective_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-02
weight: 5
translated_at: 2026-07-27T15:16:31+00:00
translation_source: kimi-cli
---
In [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) we glued two copies of the affine line $\mathbb{A}^1=\Spec \mathbb{K}[\x]$ in a suitable way to produce the projective space $\mathbb{P}^1$. This time we generalize this and discuss the $\Proj$ construction, which produces a scheme $\Proj A_\bullet$ from a graded ring $A_\bullet$.

## Projective Space

Generalizing [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) directly, it is not difficult to define $\mathbb{P}^n$ as a scheme. However, in order to generalize this to the $\Proj$ construction, it is helpful to understand $\mathbb{P}^n$ intuitively, so let us examine it more carefully.

First, we briefly recall the projective space defined in topology. To construct the topological space $\mathbb{P}^n$, we considered the topological space $\mathbb{R}^{n+1}\setminus \{0\}$. Then, defining the following equivalence relation on it

$$(x_0,\ldots, x_n)\sim (y_0,\ldots, y_n)\iff\text{$x_i=\lambda y_i$ for some $\lambda\neq 0$, for all $i$}$$

the projective space $\mathbb{P}^n$ is the topological space defined as the quotient space $(\mathbb{R}^{n+1}\setminus \{0\})/{\sim}$, and for notational convenience we write the equivalence class containing $(x_0,\ldots, x_n)$ as $[x_0:x_1:\cdots:x_n]$.

Now consider the canonical projection $\pi:\mathbb{R}^{n+1}\setminus\{0\}\rightarrow \mathbb{P}^n$. Then the fiber over a point $[x_0:x_1:\cdots:x_n]$ of $\mathbb{P}^n$ is by definition

$$\{(y_0,\ldots, y_n)\mid\text{$x_i=\lambda y_i$ for some $\lambda\neq 0$, for all $i$}\}$$

that is, the set of points on the line through the origin and $(x_0,\ldots, x_n)$, excluding the origin itself. For this reason $\mathbb{P}^n$ is often thought of as the space of lines in $\mathbb{R}^{n+1}$.

On the other hand, in $\mathbb{R}^{n+1}$, any line not parallel to a given plane $P$ must meet $P$ at exactly one point. Thus, if we define the plane $P_i$ by

$$P_i=\{\x_i=1\}=\{(x_0,\ldots, x_n)\mid x_i=1\}$$

then among the points of $\mathbb{P}^n$, those not corresponding to lines perpendicular to the $\x_i$-axis are in one-to-one correspondence with points of $P_i$, and the remaining points are lines in the $\x_0\x_1\cdots\x_{i-1}\x_{i+1}\cdots\x_n$-plane, i.e. in $\mathbb{R}^n$, so we obtain the decomposition

$$\mathbb{P}^n=\mathbb{R}^n\coprod \mathbb{P}^{n-1}$$

This process is illustrated in the following figure for the case $n=2$.

{% diagram Math/Scheme_Theory/Projective_Schemes-1.svg width="31.18em" alt="stereographic_projection" %}

Writing this in formulas, for a point $[x_0:\cdots:x_n]$ of $\mathbb{P}^n$, if $x_i\neq 0$ then we can (uniquely) find a point in the equivalence class of $[x_0:\cdots:x_n]$ whose $i$-th coordinate is $1$, and viewing this point as a point of $P_i$ we can identify the subset

$$U_i=\{[x_0:\cdots:x_n]\in \mathbb{P}^n\mid x_i\neq 0\}$$

with $P_i\cong \mathbb{R}^n$. On the other hand, points in the complement of $U_i$ are exactly those with $x_i=0$, so simply omitting the $i$-th coordinate allows us to understand them as points of $\mathbb{P}^{n-1}$.

Explicitly, the above identification $U_i\cong P_i$ is expressed by the formula

$$[x_0:\cdots:x_n]\text{ in $U_i\subseteq \mathbb{P}^n$}\leftrightarrow\left(\frac{x_0}{x_i},\ldots, \frac{x_{i-1}}{x_i},1,\frac{x_{i+1}}{x_i},\ldots, \frac{x_n}{x_i}\right)\text{ in $P_i\subseteq \mathbb{R}^{n+1}$}$$

On the other hand, the procedure of [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) proceeds in the reverse direction. That is, we are first given $n+1$ copies of $n$-dimensional planes $P_0,\ldots, P_n$ and we transport them via isomorphisms satisfying the cocycle condition. Then how the cocycle condition should be written is obtained by examining how a point of $\mathbb{P}^n$ is written in different $P_i$ and $P_j$. Let us look at this. First, an arbitrary point of $P_i$ and $P_j$ can be written in the form

$$(x_{0/i},\ldots, x_{(i-1)/i}, 1, x_{(i+1)/i}, \ldots, x_{n/i})\in P_i,\qquad (x_{0/j},\ldots, x_{(j-1)/j}, 1, x_{(j+1)/j}, \ldots, x_{n/j})\in P_j$$

Now assuming these points come from some point of $\mathbb{P}^n$, that point must lie in $U_i\cap U_j$, and in this set $x_i,x_j\neq 0$, so $x_{j/i}, x_{i/j}\neq 0$. For notational convenience assume $j>i$; using this fact we have

$$[x_{0/i}:\ldots: x_{(i-1)/i}: 1: x_{(i+1)/i}: \ldots: x_{j/i}:\ldots, x_{n/i}]=\left[\frac{x_{0/i}}{x_{j/i}}:\ldots: \frac{x_{(i-1)/i}}{x_{j/i}}: \frac{1}{x_{j/i}}: \frac{x_{(i+1)/i}}{x_{j/i}}: \ldots: 1:\ldots, \frac{x_{n/i}}{x_{j/i}}\right]$$

Therefore, for the point on the right-hand side to equal

$$[x_{0/j}:\ldots: x_{(j-1)/j}: 1: x_{(j+1)/j}: \ldots: x_{n/j}]$$

the following formulas must hold:

$$x_{k/i}/x_{j/i}=x_{k/j}\quad\text{for all $k\neq i,j$},\qquad\text{and}\qquad x_{i/j}=1/x_{j/i}$$

Similarly, matching a point of $P_j$ to a point of $P_i$ would yield formulas like $x_{k/j}/x_{i/j}=x_{k/i}$, but this is not a new formula since it follows from $x_{i/j}=1/x_{j/i}$.

Now let us generalize [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) based on this computation. First consider $n+1$ copies of affine $n$-spaces

$$P_i=\Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)=\Spec A^i$$

Then the open subschemes $P_{ij}=D(\x_{j/i})\cong \Spec (A^i)_{\x_{j/i}}$ of $P_i$, and the isomorphisms $\varphi_{ij}:P_{ij} \rightarrow P_{ji}$ defined as the spectrum of the following ring homomorphism

$$(A^j)_{\x_{i/j}} \rightarrow (A^i)_{\x_{j/i}};\qquad \x_{k/j}\mapsto \x_{k/i}/\x_{j/i}\quad\text{for all $k\neq i,j$},\qquad\text{and}\qquad \x_{i/j}\mapsto 1/\x_{j/i}$$

almost trivially satisfy the cocycle condition of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), and thus a unique scheme $\mathbb{P}^n$ is defined. In this case, for points having coordinates consisting of elements of $\mathbb{K}$, that is, points that can be written in the form $[x_0:\ldots:x_n]$ as in the preceding topological discussion, $U_i$ is exactly the set satisfying the condition $x_i\neq 0$. Of course, just as for $\mathbb{A}^n$, there also exist points of $\mathbb{P}^n$ that cannot be written in such coordinates.

## Projective Schemes

As it stands, the above explanation has some incomplete parts. For example, the fact that the $U_i$ are open subschemes of $\mathbb{P}^n$ is a consequence of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), but it seems that by their very definition they should be open sets, being the set where the function $\x_i$ is nonzero. However, the problem is that $\x_i$ is not a function on $\mathbb{P}^n$. Even looking only at the case $n=1$, we have checked that $\mathcal{O}_{\mathbb{P}^1}(\mathbb{P}^1)\cong \mathbb{K}$. This can also be confirmed by the topological construction alone: the function $\x_i: \mathbb{R}^{n+1}\setminus\{0\} \rightarrow \mathbb{R}$ that takes a point $(x_0,\ldots, x_n)$ of $\mathbb{R}^{n+1}\setminus \{0\}$ and outputs $x_i$ is not compatible with $\sim$, and therefore does not define a function on $\mathbb{P}^n$. As another example, if a function $f: \mathbb{R}^2\setminus\{0\} \rightarrow \mathbb{R}$ on $\mathbb{R}^2\setminus\{0\}$ is given by the formula

$$f(x_0,x_1)=x_0^2-x_1$$

then

$$f(\lambda x_0,\lambda x_1)=\lambda^2x_0^2-\lambda x_1\neq f(x_0,x_1)$$

so $f$ is not well-defined. Instead, if we take $f$ to be a *homogeneous polynomial*, then although $f$ itself is not well-defined as a function, its zero locus $Z(f)$ is well-defined. This is because the formula

$$f(\lambda x_0,\ldots, \lambda x_n)=\lambda^{\deg f} f(x_0,\ldots, x_n),\qquad \lambda\neq 0$$

holds.

That is, in order to describe $\mathbb{P}^n$ in a manner similar to the spectrum, we should not view $\mathbb{A}^{n+1}$ simply as the spectrum of the ring $\mathbb{K}[\x_0,\ldots, \x_n]$, but rather add degree information to make it a *graded* ring, and look at the zero loci of *homogeneous* elements rather than arbitrary elements. Then, thinking of [[Algebraic Structures] §Graded Rings, ⁋Proposition 6](/en/math/algebraic_structures/graded_rings#prop6), our interest should also be in *homogeneous* ideals.

In the remainder of this post we follow the process of taking $\Proj$ of a graded ring to obtain a scheme. The $\Proj$ of an arbitrary graded ring is not necessarily a projective scheme. For example, if $A_\bullet=\mathbb{K}[\x_1,\x_2,\ldots]$, then $\Proj A_\bullet$ is not even quasi-compact, so the name projective scheme is defined separately with a finitely generated condition in [§Closed Subschemes of Projective Spaces, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes_of_projective_spaces#def7). For this we fix some notation.

::: remark Remark {#rmk}
Unless stated otherwise, a graded ring is always assumed to be $\mathbb{N}_{\geq0}$-graded. That is, the ring of interest is always of the form

$$A_\bullet=\bigoplus_{i=0}^\infty A_i=A_0\oplus A_1\oplus\cdots$$

In this case, since $A_0$ is itself a ring, $A_\bullet$ can be viewed as a graded $A_0$-algebra, and for this reason we call $A_0$ the *base ring*. Also, when we forget the grading structure on $A_\bullet$ and view it as an ordinary ring, we simply write it as $A$.
:::

Let a graded ring $A_\bullet$ be given. Then the subset

$$A_+=\bigoplus_{i=1}^\infty A_i=A_1\oplus A_2\oplus\cdots$$

is trivially a homogeneous ideal of $A_\bullet$. However, thinking of the case $A_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$, the point where the function values vanish for all elements of $A_+$, that is, the point that is identically zero for all polynomials, is only the origin. Since the origin is the point removed when making $\mathbb{P}^n$, it is appropriate to exclude from our discussion any ideal containing the ideal $A_+$. From this viewpoint we call $A_+$ the *irrelevant ideal*.

This can also be read somewhat more geometrically. By the above formula $f(\lambda x_0,\ldots,\lambda x_n)=\lambda^{\deg f}f(x_0,\ldots,x_n)$, the closed sets cut out by homogeneous polynomials in $\mathbb{A}^{n+1}$ are always closed under scalar multiplication, so they are affine cones, being collections of lines through the origin. ([[Algebraic Varieties] §Projective Varieties, ⁋Definition 12](/en/math/algebraic_varieties/projective_varieties#def12)) Now among affine cones there is also the cone consisting only of the origin, that is, the cone cut out by $A_+$, and for this cone removing the origin leaves only the empty set, so this cone must be excluded from our interest. For a homogeneous prime ideal $\mathfrak{p}$, the condition $A_+\subseteq \mathfrak{p}$ is equivalent to the cone cut out by $\mathfrak{p}$ being the origin, so we define $\Proj A_\bullet$ by excluding such $\mathfrak{p}$.

::: Definition 1
For a graded ring $A_\bullet$, $\Proj A_\bullet$ is defined as the set

$$\Proj A_\bullet =\{\mathfrak{p}\in \Spec A\mid\text{$\mathfrak{p}$ is homogeneous and $A_+\not\subseteq \mathfrak{p}$}\}$$
:::

By definition $\Proj A_\bullet$ is a subset of $\Spec A$. That is, all points of $\Proj A_\bullet$ are also points of $\Spec A$. This would be a somewhat awkward result if we had used $\MaxSpec A$ instead of $\Spec A$, but $\Spec A$ contains points corresponding to prime ideals in addition to traditional points. For example, considering the ideal $(\x_1-\x_2)$ of $A=\mathbb{K}[\x_1,\x_2]$, since $\mathbb{K}[\x_1,\x_2]/(\x_1-\x_2)\cong \mathbb{K}[\x_1]$, this ideal is a prime ideal. Moreover, when $\mathbb{K}[\x_1,\x_2]$ is viewed as a graded ring $A_\bullet$, this ideal is a homogeneous prime ideal not containing $A_+$, so it is also a point of $\Proj A_\bullet$.

So far $\Proj A_\bullet$ is merely a set. To give it a topological structure we must use zero loci of functions, and as observed above we must use zero loci of *homogeneous* polynomials.

::: Definition 2
Let a graded ring $A_\bullet$ be given. For a homogeneous ideal $\mathfrak{a}$ of $A_\bullet$, we define

$$Z_+(\mathfrak{a})=\{\mathfrak{p}\in\Proj A_\bullet\mid \mathfrak{a}\subseteq \mathfrak{p}\}$$
:::

Then using the third result of [[Commutative Algebra] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2), we can show the following lemma, similar to [§Spectrums, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6) and [§Spectrums, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5).

::: Lemma 3
For a graded ring $A_\bullet$, the following hold.

1. For any homogeneous ideals $\mathfrak{a},\mathfrak{b}$, we have $Z_+(\mathfrak{a}\mathfrak{b})=Z_+(\mathfrak{a})\cup Z_+(\mathfrak{b})$.
2. For any family of homogeneous ideals $\{\mathfrak{a}_i\}$, we have $Z_+(\sum \mathfrak{a}_i)=\bigcap Z_+(\mathfrak{a}_i)$.
3. For any homogeneous ideal $\mathfrak{a}$, we have $Z_+(\sqrt{\mathfrak{a}})=Z_+(\mathfrak{a})$.
4. For any homogeneous ideal $\mathfrak{a}$, we have $Z_+(\mathfrak{a})=Z_+(\mathfrak{a}\cap A_+)$.
:::

Of course, it is trivial that $\mathfrak{a}\mathfrak{b}$, $\sqrt{\mathfrak{a}}$, and $\sum \mathfrak{a}_i$ appearing in the above lemma are homogeneous. Then the first through third results are already observations from the spectrum, and only the fourth result is new.

::: Proof (Lemma 3)
1. It is trivial that a homogeneous prime ideal $\mathfrak{p}$ containing $\mathfrak{a}$ or $\mathfrak{b}$ also contains the smaller homogeneous ideal $\mathfrak{a}\mathfrak{b}$, so it suffices to show the reverse inclusion. Assume $\mathfrak{p}\supset \mathfrak{a}\mathfrak{b}$. If $\mathfrak{p}\not\supseteq \mathfrak{b}$, then we can find an element $b$ of $\mathfrak{b}$ with $b\not\in \mathfrak{p}$. Then since $\mathfrak{b}$ is homogeneous, decomposing it into a sum of homogeneous elements we can write

    $$b=b_1+\cdots b_n,\qquad \text{$b_i\in \mathfrak{b}$ homogeneous}$$

    On the other hand, for any homogeneous element $a\in \mathfrak{a}$, we have $ab\in \mathfrak{a}\mathfrak{b}\subseteq \mathfrak{p}$. Considering the element

    $$ab=ab_1+\cdots+ab_n$$

    of $\mathfrak{a}\mathfrak{b}\subseteq \mathfrak{p}$, since $\mathfrak{p}$ is homogeneous, all $ab_i$ are elements of $\mathfrak{p}$. On the other hand, by the preceding assumption $b\not\in \mathfrak{p}$, so there exists $i$ with $b_i\not\in \mathfrak{p}$, and then $ab_i$ is a homogeneous element belonging to $\mathfrak{p}$ with $b_i\not\in \mathfrak{p}$, so by [[Commutative Algebra] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2) we have $a\in \mathfrak{p}$. Therefore $\mathfrak{a}\subseteq \mathfrak{p}$ holds.
2. This is trivial since $\sum \mathfrak{a}_i$ is defined as the smallest ideal containing all the ideals $\mathfrak{a}_i$.
3. [[Commutative Algebra] §Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8).
4. By definition $Z_+(\mathfrak{a})\subseteq Z_+(\mathfrak{a}\cap A_+)$ is trivial, so it suffices to show the reverse inclusion. That is, let $\mathfrak{p}$ be a prime ideal containing all homogeneous elements of $\mathfrak{a}$ of positive degree but not containing $A_+$ entirely, and let us show $\mathfrak{a}\subseteq \mathfrak{p}$. For this it suffices to show that for any $a\in \mathfrak{a}\cap A_0$, the above assumption implies $a$ also belongs to $\mathfrak{p}$.

    Now since $A_+\not\subseteq\mathfrak{p}$, there exists a homogeneous element $f$ not belonging to $\mathfrak{p}$. Then $af\in \mathfrak{a}\cap A_+\subseteq \mathfrak{p}$, and since $f\not\in \mathfrak{p}$ we have $a\in \mathfrak{p}$.
:::

Looking at the results of this lemma, from the first and second results we can make the following definition.

::: Definition 4
Let a graded ring $A_\bullet$ be given. For any homogeneous ideal $\mathfrak{a}$, the unique topology on $\Proj A_\bullet$ having sets of the form $Z_+(\mathfrak{a})$ as closed sets is called the *Zariski topology*.
:::

Also, by the fourth result of this lemma, we know that in defining $\Proj A_\bullet$ we only need to consider homogeneous ideals contained in $A_+$. This is intuitively obvious as well: if $A=\mathbb{K}[\x_0,\ldots, \x_n]$, elements in $A_0$ are constant functions anyway.

Now we define the following.

::: Definition 5
For any homogeneous element $f$ of a graded ring $A_\bullet$, we write $D_+(f)$ for the complement of $Z_+(f)$ in $\Proj A_\bullet$.
:::

The following corollary follows immediately from the first result of [Lemma 3](#lem3).

::: Corollary 6
We have $D_+(f)\cap D_+(g)=D_+(fg)$.
:::

Moreover, the following holds.

::: Corollary 7
The collection of $D_+(f)$ forms a base for $\Proj A_\bullet$.
:::
::: Proof
Writing an arbitrary homogeneous ideal $\mathfrak{a}$ of $A$ using homogeneous generators as $\mathfrak{a}=\sum_{i\in I} (f_i)$, we have

$$Z_+(\mathfrak{a})=\bigcap_{i\in I} Z_+((f_i))$$

and therefore

$$D_+(\mathfrak{a})=\bigcup_{i\in I} D_+(f_i)$$
:::

On the other hand, on the spectrum $\Spec A$ of a ring $A$, we observed that for any element $f\in A$, the set $D(f)$ is isomorphic (as a scheme) to $\Spec A_f$. A similar result holds for $D_+(f)$.

::: Lemma 8
For a graded ring $A_\bullet$ and any nonzero homogeneous element $f$ of $A_+$, the map $D_+(f) \rightarrow \Spec A_{(f)}$ defined by the formula

$$\mathfrak{p}\mapsto \mathfrak{p}A_f\cap A_{(f)}$$

is a homeomorphism. ([[Commutative Algebra] §Localization of Graded Rings, ⁋Definition 5](/en/math/commutative_algebra/localization_of_graded_rings#def5))
:::
::: Proof
First, since $f\not\in \mathfrak{p}$, via the localization $A \rightarrow A_f$ the ideal $\mathfrak{p}$ is sent to the prime ideal $\mathfrak{p}A_f$ of $A_f$. ([[Commutative Algebra] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)) Now the right-hand side of the claim is the preimage of $\mathfrak{p}A_f$ under the inclusion $i: A_{(f)} \rightarrow A_f$, so this becomes a prime ideal of $A_{(f)}$.

Now let us define the inverse map $\Spec A_{(f)} \rightarrow D_+(f)$ of this correspondence as a function. Given an arbitrary prime ideal $\mathfrak{q}\in\Spec A_{(f)}$, consider the homogeneous ideal $\mathfrak{p}$ of $A$ generated by those homogeneous elements $x$ of $A$ satisfying the condition

$$\frac{x^{\deg f}}{f^{\deg x}}\in \mathfrak{q}$$

Here what needs to be checked is that the set of homogeneous elements satisfying the above condition already forms an ideal, that is, the sum of two elements of the same degree and the product with an arbitrary homogeneous element again satisfy the condition. The product case is trivial, and for the sum case one uses the binomial expansion of $(x+y)^{\deg f}$ together with the fact that the $\deg f$-th power of each term $x^ky^{\deg f-k}/f^{\deg x}$ becomes a product of powers of $x^{\deg f}/f^{\deg x}$ and $y^{\deg f}/f^{\deg y}$, and that $\mathfrak{q}$ is prime.

Then since the homogeneous elements of $\mathfrak{p}$ are exactly those satisfying the above condition, for any homogeneous elements $x,y\in A$ we have

$$xy\in \mathfrak{p}\iff \frac{x^{\deg f}}{f^{\deg x}}\frac{y^{\deg f}}{f^{\deg y}}\in \mathfrak{q}$$

and from $\mathfrak{q}$ being a prime ideal we see that $\mathfrak{p}$ is a prime ideal. Also $f^{\deg f}/f^{\deg f}=1\not\in \mathfrak{q}$ so $f\not\in \mathfrak{p}$, and therefore $\mathfrak{p}$ does not contain $A_+$ and $\mathfrak{p}\in D_+(f)$. Now one easily checks that this correspondence $\mathfrak{p}\mapsto \mathfrak{p}A_f\cap A_{(f)}$ and $\mathfrak{q}\mapsto \mathfrak{p}$ are inverse to each other, and for any homogeneous ideal $\mathfrak{a}$ of $A_\bullet$, the closed set $Z_+(\mathfrak{a})\cap D_+(f)$ of $D_+(f)$ is sent by this function to the closed set $Z(\mathfrak{a}A_f\cap A_{(f)})$ of $\Spec A_{(f)}$, so we see that this is a homeomorphism.
:::

Then the way to give $\Proj A_\bullet$ a scheme structure is now obvious. The proof of the following lemma is almost identical to that of [Lemma 8](#lem8).

::: Lemma 9
For a graded ring $A_\bullet$ and nonzero homogeneous elements $f,g$ of $A_+$, there exists an isomorphism

$$\Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})\subseteq \Spec A_{(f)}$$
:::
::: Proof
Since $\mathfrak{p}\in \Proj A_\bullet$ satisfies $A_+\not\subseteq \mathfrak{p}$, $\mathfrak{p}$ has a homogeneous element of $A_+$ not belonging to it. That is, the $D_+(f)$ given by nonzero homogeneous elements of $A_+$ cover $\Proj A_\bullet$, so restricting the assumption to such $f$ causes no loss for our purpose. Now writing $d=\deg f\geq 1$ and $e=\deg g\geq 1$, since $\deg (g^d)=de=\deg (f^e)$ we have

$$\theta=\frac{g^{\deg f}}{f^{\deg g}}=\frac{g^d}{f^e}$$

is an element of degree $0$ of $A_f$, that is, $\theta\in A_{(f)}$. ([[Commutative Algebra] §Localization of Graded Rings, ⁋Proposition 3](/en/math/commutative_algebra/localization_of_graded_rings#prop3)) On the other hand, $D(\theta)$ is an open subscheme of $\Spec A_{(f)}$ isomorphic to $\Spec (A_{(f)})_\theta$ ([§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2)), so it suffices for us to construct a ring isomorphism $(A_{(f)})_\theta\cong A_{(fg)}$.

First, since the localization $A_f \rightarrow A_{fg}$ preserves the grading, restricting to the degree $0$ part we obtain the canonical ring homomorphism

$$\rho: A_{(f)} \rightarrow A_{(fg)};\qquad \frac{a}{f^n}\mapsto \frac{ag^n}{(fg)^n}$$

At this point $f^e/g^d$ is an element of degree $0$ of $A_{fg}$ and

$$\frac{g^d}{f^e}\cdot\frac{f^e}{g^d}=1$$

so $\rho(\theta)$ is a unit of $A_{(fg)}$. Therefore by [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) there exists a unique ring homomorphism

$$\Phi:(A_{(f)})_\theta \rightarrow A_{(fg)};\qquad \frac{x}{\theta^n}\mapsto \rho(x)\left(\frac{f^e}{g^d}\right)^n$$

extending $\rho$.

Let us show that $\Phi$ is surjective. An arbitrary element of $A_{(fg)}$ can be written in the form $a/(fg)^n$ for a homogeneous element $a$ and $n\geq 0$, and since this element has degree $0$ we have $\deg a=n(d+e)$. Now setting

$$x=\frac{ag^{n(d-1)}}{f^{n(e+1)}}$$

the degree of the numerator is

$$n(d+e)+en(d-1)=n(d+ed)=nd(e+1)$$

and the degree of the denominator is $dn(e+1)$, which equals this, so $x\in A_{(f)}$. (Here $d\geq 1$ is used.) Then in $A_{fg}$

$$\Phi\left(\frac{x}{\theta^n}\right)=\frac{ag^{n(d-1)}}{f^{n(e+1)}}\cdot\frac{f^{ne}}{g^{nd}}=\frac{a}{f^ng^n}=\frac{a}{(fg)^n}$$

so $\Phi$ is surjective.

Now let us show that $\Phi$ is injective. Suppose an element $x/\theta^n$ of $(A_{(f)})_\theta$ is sent to $0$ by $\Phi$. Since $\Phi(\theta)$ is a unit, this is equivalent to $\rho(x)=0$. Writing $x=b/f^m$, here $b$ is a homogeneous element with $\deg b=md$, and $\rho(x)=0$ means $b/f^m=0$ in $A_{fg}$, so there exists $k\geq 0$ with $(fg)^kb=0$. Then since $d\geq 1$

$$f^k\cdot bg^{dk}=(f^kg^kb)g^{(d-1)k}=0$$

and therefore $bg^{dk}=0$ in $A_f$. From this in $A_{(f)}$

$$\theta^kx=\frac{g^{dk}}{f^{ek}}\cdot\frac{b}{f^m}=\frac{bg^{dk}}{f^{ek+m}}=0$$

so $x/\theta^n=0$ in $(A_{(f)})_\theta$. That is, $\Phi$ is injective, and from the above $\Phi$ is an isomorphism.

Finally, let us verify that this isomorphism is compatible with the homeomorphism of [Lemma 8](#lem8). Writing the image of $\mathfrak{p}\in D_+(f)$ as $\mathfrak{q}=\mathfrak{p}A_f\cap A_{(f)}$, since $f\not\in \mathfrak{p}$ we have

$$\theta=\frac{g^d}{f^e}\in \mathfrak{q}\iff g^d\in \mathfrak{p}\iff g\in \mathfrak{p}$$

Therefore the homeomorphism of [Lemma 8](#lem8) sends $D_+(fg)=D_+(f)\cap D_+(g)$ of [Corollary 6](#cor6) exactly onto $D(\theta)$.
:::

Therefore, there exists an isomorphism between the principal open set $D(f^{\deg g}/g^{\deg f})\subseteq \Spec A_{(g)}$ of $\Spec A_{(g)}$ and the principal open set $\Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})$ of $\Spec A_{(f)}$. Now the following theorem is a simple computation.

::: Theorem 10
The $\Spec A_{(f)}$, the open subschemes $D(g^{\deg f}/f^{\deg g})$, and the isomorphisms

$$D(f^{\deg g}/g^{\deg f})\cong \Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})$$

defined above satisfy all the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), and therefore give a unique scheme structure on $\Proj A_\bullet$.
:::
::: Proof
As the index set we take all nonzero homogeneous elements of $A_+$. For two elements $f,g$, as in the proof of [Lemma 9](#lem9) we write

$$\theta_{f,g}=\frac{g^{\deg f}}{f^{\deg g}}\in A_{(f)}$$

then what that proof gave us is that the canonical ring homomorphism $\rho_{f,fg}:A_{(f)} \rightarrow A_{(fg)}$ sends $\theta_{f,g}$ to a unit, and the induced

$$\Phi_{f,g}:(A_{(f)})_{\theta_{f,g}} \rightarrow A_{(fg)}$$

is an isomorphism extending $\rho_{f,fg}$. Now considering $X_f=\Spec A_{(f)}$ and its open subscheme $X_{fg}=D(\theta_{f,g})$, and noting that $A_{(fg)}=A_{(gf)}$, we define the isomorphism $\varphi_{fg}:X_{fg} \rightarrow X_{gf}$ as the spectrum of the ring isomorphism

$$\Phi_{f,g}^{-1}\circ \Phi_{g,f}:(A_{(g)})_{\theta_{g,f}} \rightarrow (A_{(f)})_{\theta_{f,g}}$$

Here, if $fg=0$ then $\theta_{f,g}=0$ and $\theta_{g,f}=0$, so $X_{fg}$ and $X_{gf}$ are both empty, and in this case we set $\varphi_{fg}$ to be the identity of the empty scheme. First, when $f=g$ we have $\theta_{f,f}=1$ so $X_{ff}=X_f$, and since $A_{f\cdot f}=A_f$, the map $\rho_{f,ff}$ is the identity and therefore $\varphi_{ff}=\id$.

Now let us verify the cocycle condition. Choose nonzero homogeneous elements $f,g,h\in A_+$ and let $d=\deg f$, $e=\deg g$, $m=\deg h$. Then in $A_{(f)}$

$$\theta_{f,g}\theta_{f,h}=\frac{g^d}{f^e}\cdot\frac{h^d}{f^m}=\frac{(gh)^d}{f^{e+m}}=\theta_{f,gh}$$

so the triple intersection inside $X_f$ is

$$X_{fg}\cap X_{fh}=D(\theta_{f,g})\cap D(\theta_{f,h})=D(\theta_{f,gh})$$

If $gh=0$ then $\theta_{f,gh}=0$ so this triple intersection is empty and the cocycle condition holds vacuously. The cases $fg=0$ or $fh=0$ are similar since $\theta_{f,g}=0$ or $\theta_{f,h}=0$, so in what follows we only treat the case where $fg$, $gh$, and $fh$ are all nonzero. Then applying [Lemma 9](#lem9) to $f$ and $gh$ we obtain the isomorphism

$$\Psi_f=\Phi_{f,gh}:(A_{(f)})_{\theta_{f,gh}} \rightarrow A_{(fgh)}$$

Similarly defining $\Psi_g=\Phi_{g,fh}$ and $\Psi_h=\Phi_{h,fg}$, these respectively extend the canonical homomorphisms $\rho_{f,fgh}$, $\rho_{g,fgh}$, $\rho_{h,fgh}$. On the other hand, since these canonical homomorphisms are all degree $0$ parts of localizations like $A_f \rightarrow A_{fg} \rightarrow A_{fgh}$, they satisfy transitivity such as

$$\rho_{fg,fgh}\circ\rho_{f,fg}=\rho_{f,fgh}$$

First let us verify that $\varphi_{fg}$ sends the triple intersection to the triple intersection. $\Phi_{f,g}$ and $\Phi_{g,f}$ send $\theta_{f,h}$ and $\theta_{g,h}$ respectively to the elements

$$u=\frac{h^d}{f^m},\qquad v=\frac{h^e}{g^m}$$

of $A_{(fg)}$, and in $A_{(fg)}$

$$u^e=\frac{h^{de}}{f^{me}}=\left(\frac{g^d}{f^e}\right)^m\cdot\frac{h^{de}}{g^{md}}=\rho_{f,fg}(\theta_{f,g})^mv^d$$

and $\rho_{f,fg}(\theta_{f,g})$ is a unit. Therefore $u^e$ and $v^d$ differ only by a unit multiple, and in $\Spec A_{(fg)}$ we have $D(u)=D(v)$, and localizing $A_{(fg)}$ at $u$ and at $v$ give the same ring. That is, $\varphi_{fg}$ sends $X_{fg}\cap X_{fh}$ onto $X_{gf}\cap X_{gh}$, and this restriction is the spectrum of the ring homomorphism

$$\alpha:(A_{(g)})_{\theta_{g,fh}} \rightarrow (A_{(f)})_{\theta_{f,gh}}$$

Here $\alpha$ is obtained by localizing $\Phi_{f,g}^{-1}\circ\Phi_{g,f}$. Then considering the composition

$$\tau: A_{(fg)}\overset{\Phi_{f,g}^{-1}}{\longrightarrow}(A_{(f)})_{\theta_{f,g}} \longrightarrow (A_{(f)})_{\theta_{f,gh}}\overset{\Psi_f}{\longrightarrow} A_{(fgh)}$$

since $\Phi_{f,g}$ and $\Psi_f$ respectively extend $\rho_{f,fg}$ and $\rho_{f,fgh}$, we have $\tau\circ\rho_{f,fg}=\rho_{f,fgh}$. However, since $A_{(fg)}$ is the localization of $A_{(f)}$ at $\theta_{f,g}$ via $\Phi_{f,g}$ and $\rho_{fg,fgh}$ also satisfies the same formula, by the uniqueness in [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) we have $\tau=\rho_{fg,fgh}$. From this

$$\Psi_f\circ\alpha\vert_{A_{(g)}}=\tau\circ \rho_{g,fg}=\rho_{fg,fgh}\circ\rho_{g,fg}=\rho_{g,fgh}=\Psi_g\vert_{A_{(g)}}$$

and applying the uniqueness of [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) again to the localization $(A_{(g)})_{\theta_{g,fh}}$ of $A_{(g)}$, we get $\Psi_f\circ\alpha=\Psi_g$, that is, $\alpha=\Psi_f^{-1}\circ\Psi_g$. Therefore

$$\varphi_{fg}\vert_{X_{fg}\cap X_{fh}}=\Spec(\Psi_f^{-1}\circ \Psi_g)$$

and applying the same argument to $(g,h)$ and $(f,h)$, on the triple intersection we have

$$\varphi_{gh}=\Spec(\Psi_g^{-1}\circ\Psi_h),\qquad \varphi_{fh}=\Spec(\Psi_f^{-1}\circ\Psi_h)$$

Since $\Spec$ is contravariant,

$$\varphi_{gh}\circ\varphi_{fg}=\Spec\left((\Psi_f^{-1}\circ\Psi_g)\circ(\Psi_g^{-1}\circ \Psi_h)\right)=\Spec(\Psi_f^{-1}\circ\Psi_h)=\varphi_{fh}$$

so the cocycle condition holds. Therefore by [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9) there exists a unique scheme $X$ having the $X_f$ as open subschemes with $X_f\cap X_g=X_{fg}$.

Finally, let us verify that the underlying topological space of $X$ is $\Proj A_\bullet$. [Lemma 8](#lem8) gives homeomorphisms $\psi_f: D_+(f) \rightarrow \Spec A_{(f)}=X_f$, and as checked in the proof of [Lemma 9](#lem9), $\psi_f$ sends $D_+(fg)$ onto $X_{fg}=D(\theta_{f,g})$. Moreover, for any $\mathfrak{p}\in D_+(fg)$ the preimage of $\mathfrak{p}A_{fg}\cap A_{(fg)}$ under $\rho_{f,fg}$ is $\mathfrak{p}A_f\cap A_{(f)}$ ([[Commutative Algebra] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)), so $\psi_f$ and $\psi_g$ are compatible with $\varphi_{fg}$. That is, $\psi_g=\varphi_{fg}\circ\psi_f$ holds on $D_+(fg)$. On the other hand, as observed above the $D_+(f)$ cover $\Proj A_\bullet$, so gluing the $\psi_f$ we obtain a homeomorphism between the underlying topological space of $X$ and $\Proj A_\bullet$. Through this $\Proj A_\bullet$ acquires a scheme structure, and by the uniqueness in [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9) this scheme structure is unique.
:::

In particular, since $\Proj A_\bullet$ is a locally ringed space, for any $\mathfrak{p}\in \Proj A_\bullet$ the stalk $\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}$ is a local ring. But since $\mathfrak{p}$ can be put into a suitable affine open neighborhood anyway, we can show the following by essentially the same procedure as [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8).

::: Lemma 11
For a graded ring $A_\bullet$ and any $\mathfrak{p}\in \Proj A_\bullet$, there exists an isomorphism

$$\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}\cong A_{(\mathfrak{p})}$$
:::
::: Proof
Since $\mathfrak{p}\in \Proj A_\bullet$, we have $A_+\not\subseteq \mathfrak{p}$, and therefore there exists a homogeneous element $f$ of $A_+$ not belonging to $\mathfrak{p}$. Let $d=\deg f\geq 1$. Then $\mathfrak{p}\in D_+(f)$, and by [Theorem 10](#thm10), $D_+(f)$ is an open subscheme of $\Proj A_\bullet$ isomorphic to $\Spec A_{(f)}$. Since the stalk of an open subscheme equals the stalk of the original scheme, for the point $\mathfrak{q}=\mathfrak{p}A_f\cap A_{(f)}$ to which [Lemma 8](#lem8) sends $\mathfrak{p}$, from [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8) we obtain

$$\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}\cong \mathcal{O}_{\Spec A_{(f)},\mathfrak{q}}\cong (A_{(f)})_\mathfrak{q}$$

Therefore it suffices to construct an isomorphism $(A_{(f)})_\mathfrak{q}\cong A_{(\mathfrak{p})}$.

Let $S$ be the multiplicative set consisting of homogeneous elements not belonging to $\mathfrak{p}$; then $A_{(\mathfrak{p})}=(S^{-1}A)_0$. ([[Commutative Algebra] §Localization of Graded Rings, ⁋Definition 5](/en/math/commutative_algebra/localization_of_graded_rings#def5)) Now since $f\in S$, the localization $A_f \rightarrow S^{-1}A$ exists, and since this preserves the grading, restricting to the degree $0$ part we obtain the canonical ring homomorphism

$$\sigma: A_{(f)} \rightarrow A_{(\mathfrak{p})};\qquad \frac{a}{f^n}\mapsto \frac{a}{f^n}$$

At this point $\sigma$ sends elements of $A_{(f)}\setminus \mathfrak{q}$ to units. Indeed, writing $x=a/f^n\in A_{(f)}$, here $a$ is a homogeneous element with $\deg a=nd$, and since $f\not\in \mathfrak{p}$, by [[Commutative Algebra] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)

$$x\in \mathfrak{q}\iff a\in \mathfrak{p}$$

Therefore if $x\not\in \mathfrak{q}$ then $a\in S$, and $f^n/a$ is an element of degree $0$ of $S^{-1}A$ that becomes the inverse of $\sigma(x)$. Now by [[Commutative Algebra] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6) there exists a unique ring homomorphism

$$\Theta:(A_{(f)})_\mathfrak{q} \rightarrow A_{(\mathfrak{p})}$$

extending $\sigma$.

Let us show that $\Theta$ is surjective. An arbitrary element of $A_{(\mathfrak{p})}$ is of the form $a/s$ for a homogeneous element $a$ and $s\in S$, and since this element has degree $0$ we have $l=\deg s=\deg a$. Now setting

$$u=\frac{as^{d-1}}{f^l},\qquad v=\frac{s^d}{f^l}$$

we have $\deg (as^{d-1})=l+l(d-1)=ld=\deg (f^l)$ and $\deg (s^d)=ld$, so $u,v\in A_{(f)}$. Also $s\not\in \mathfrak{p}$ and since $\mathfrak{p}$ is a prime ideal, $s^d\not\in \mathfrak{p}$, and therefore $v\not\in \mathfrak{q}$. Then in $S^{-1}A$

$$\Theta\left(\frac{u}{v}\right)=\frac{as^{d-1}}{f^l}\cdot\frac{f^l}{s^d}=\frac{a}{s}$$

so $\Theta$ is surjective.

Now let us show that $\Theta$ is injective. Suppose an element $x/v$ of $(A_{(f)})_\mathfrak{q}$ is sent to $0$ by $\Theta$. Since $\Theta(v)$ is a unit, $\sigma(x)=0$. Writing $x=a/f^n$, this means $a/f^n=0$ in $S^{-1}A$, so there exists a homogeneous element $t\in S$ with $ta=0$. Now since $\deg (t^d)=d\deg t=\deg (f^{\deg t})$

$$w=\frac{t^d}{f^{\deg t}}$$

is an element of $A_{(f)}$, and since $t\not\in \mathfrak{p}$ we have $w\not\in \mathfrak{q}$. On the other hand, since $d\geq 1$ we have $t^da=0$ and therefore in $A_{(f)}$

$$wx=\frac{t^da}{f^{\deg t+n}}=0$$

That is, $x=0$ in $(A_{(f)})_\mathfrak{q}$, so $x/v=0$, and $\Theta$ is injective. From the above $\Theta$ is an isomorphism.
:::

Something to be somewhat careful about is that unlike $\Spec$, $\Proj$ does not define a functor from $\bgr_{\mathbb{N}_{\geq 0}}\cRing^\op$ to $\LRS$. This is because even if a graded ring homomorphism $\phi_\bullet:A_\bullet \rightarrow B_\bullet$ and an arbitrary homogeneous ideal $\mathfrak{q}$ of $B$ do not contain $B_+$, its inverse image $\phi^{-1}(\mathfrak{q})$ may contain $A_+$.

Finally, we translate the projective space examined at the very beginning for motivation into the language of algebraic geometry (almost) completely.

::: Example 12
In algebraic geometry, $\mathbb{P}^n_\mathbb{K}$ is defined by the formula

$$\mathbb{P}^n_\mathbb{K}=\Proj \mathbb{K}[\x_0,\ldots, \x_n]$$

Here the polynomial algebra $\mathbb{K}[\x_0,\ldots, \x_n]$ is of course a graded ring with grading given by degree.

Then the $n+1$ open covers of projective space in this language can be thought of as

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_{0},\ldots, \x_{n}]_{(\x_{i})}$$

and by [[Commutative Algebra] §Localization of Graded Rings, ⁋Proposition 6](/en/math/commutative_algebra/localization_of_graded_rings#prop6)

$$\mathbb{K}[\x_{0},\ldots, \x_{n}]_{(\x_{i})}\cong \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)$$

and explicitly this isomorphism is obtained by applying the first isomorphism theorem to the ring homomorphism

$$\mathbb{K}[\x_{0/i}, \ldots, \x_{n/i}]\rightarrow \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)};\qquad \x_{k/i}\mapsto \frac{\x_k}{\x_i}$$

Now any $\mathfrak{p}\in \mathbb{P}^n_\mathbb{K}$ is contained in some $D_+(\x_i)$. Through the above isomorphism, suppose the point $\mathfrak{p}$ of $D_+(\x_i)$ is sent to a point $\mathfrak{q}$ of $U_i=\Spec \mathbb{K}[\x_{0/i}, \ldots, \x_{n/i}]/(\x_{i/i}-1)$. Then in this case it would be natural to expect the isomorphism

$$\mathcal{O}_{\mathbb{P}^n_\mathbb{K},\mathfrak{p}}\cong \mathcal{O}_{U_i, \mathfrak{q}}$$

And of course this holds. ([[Commutative Algebra] §Localization of Graded Rings, ⁋Proposition 8](/en/math/commutative_algebra/localization_of_graded_rings#prop8))
:::

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---
