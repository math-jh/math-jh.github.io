---
title: "Projective Space and the Proj Construction"
description: "We construct projective space by gluing affine lines in a suitable way, and generalize this to cover the construction of taking Proj of an arbitrary graded ring. We understand projective space from a topological viewpoint and examine how to glue affine lines via stereographic projection and cocycle conditions."
excerpt: "The Proj construction from graded rings and projective spaces"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/projective_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-02
weight: 5
translated_at: 2026-07-27T15:45:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-27T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10){: data-lid="fbqr4" }, we glued two affine lines $\mathbb{A}^1=\Spec \mathbb{K}[\x]$ in a suitable way to produce the projective space $\mathbb{P}^1$. This time, generalizing this, we discuss obtaining from a graded ring $A_\bullet$ the scheme $\Proj A_\bullet$, that is, the $\Proj$ construction.

## Projective Space

Generalizing [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10){: data-lid="74zd9" } directly, it is not difficult to define $\mathbb{P}^n$ as a scheme. However, in order to generalize this to arrive at the $\Proj$ construction, it is helpful to understand $\mathbb{P}^n$ intuitively, so let us examine it a bit more carefully.

First, we briefly recall the projective space as previously defined in topology. To construct the topological space $\mathbb{P}^n$, we considered the topological space $\mathbb{R}^{n+1}\setminus \{0\}$. Then, defining the following equivalence relation on it

$$(x_0,\ldots, x_n)\sim (y_0,\ldots, y_n)\iff\text{$x_i=\lambda y_i$ for all $i$, for some $\lambda\neq 0$}$$

the projective space $\mathbb{P}^n$ is the topological space defined as the quotient space $(\mathbb{R}^{n+1}\setminus \{0\})/{\sim}$, and for notational convenience we write the equivalence class containing $(x_0,\ldots, x_n)$ as $[x_0:x_1:\cdots:x_n]$.

Now consider the canonical projection $\pi:\mathbb{R}^{n+1}\setminus\{0\}\rightarrow \mathbb{P}^n$. Then the fiber over a point of $\mathbb{P}^n$, $[x_0:x_1:\cdots:x_n]$, is by definition

$$\{(y_0,\ldots, y_n)\mid\text{$x_i=\lambda y_i$ for all $i$, for some $\lambda\neq 0$}\}$$

that is, the set of points on the line passing through the origin and $(x_0,\ldots, x_n)$, excluding the origin. For this reason, $\mathbb{P}^n$ is often thought of as the space of lines in $\mathbb{R}^{n+1}$.

Meanwhile, in $\mathbb{R}^{n+1}$, any plane $P$ and any line not parallel to $P$ necessarily meet at a single point. Therefore, if we define the plane $P_i$ by

$$P_i=\{\x_i=1\}=\{(x_0,\ldots, x_n)\mid x_i=1\}$$

then among the points of $\mathbb{P}^n$, those excluding the lines perpendicular to the $\x_i$-axis all correspond bijectively to points of $P_i$, and since the remaining points are lines in the $\x_0\x_1\cdots\x_{i-1}\x_{i+1}\cdots\x_n$-plane, that is, lines in $\mathbb{R}^n$, we obtain the following decomposition

$$\mathbb{P}^n=\mathbb{R}^n\coprod \mathbb{P}^{n-1}$$

This process is illustrated in the following figure for the case $n=2$.

{% diagram frozen/635a8f80/Math/Scheme_Theory/Projective_Schemes-1.svg width="31.18em" alt="stereographic_projection" %}

Writing this in formulas, for a point of $\mathbb{P}^n$, $[x_0:\cdots:x_n]$, if $x_i\neq 0$, then we can (uniquely) find a point in the equivalence class of $[x_0:\cdots:x_n]$ whose $i$-th coordinate is $1$, and viewing this point as a point of $P_i$, we can identify the following subset

$$U_i=\{[x_0:\cdots:x_n]\in \mathbb{P}^n\mid x_i\neq 0\}$$

with $P_i\cong \mathbb{R}^n$. On the other hand, since the points in the complement of $U_i$ are precisely the points with $x_i=0$, simply omitting the $i$-th coordinate allows us to understand them as points of $\mathbb{P}^{n-1}$.

Explicitly, the above identification $U_i\cong P_i$ is expressed by the formula

$$[x_0:\cdots:x_n]\text{ in $U_i\subseteq \mathbb{P}^n$}\leftrightarrow\left(\frac{x_0}{x_i},\ldots, \frac{x_{i-1}}{x_i},1,\frac{x_{i+1}}{x_i},\ldots, \frac{x_n}{x_i}\right)\text{ in $P_i\subseteq \mathbb{R}^{n+1}$}$$

Meanwhile, the procedure of [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10){: data-lid="6zpqi" } runs this process in reverse. That is, we suppose that $n+1$ $n$-dimensional planes $P_0,\ldots, P_n$ are given first, and we transition between them via isomorphisms satisfying the cocycle condition. Then how the cocycle condition must be written is obtained precisely by examining how a point of $\mathbb{P}^n$ is written in different planes $P_i$ and $P_j$ according to the above identification. Let us examine this. First, an arbitrary point of $P_i$ and $P_j$ can be written in the form

$$(x_{0/i},\ldots, x_{(i-1)/i}, 1, x_{(i+1)/i}, \ldots, x_{n/i})\in P_i,\qquad (x_{0/j},\ldots, x_{(j-1)/j}, 1, x_{(j+1)/j}, \ldots, x_{n/j})\in P_j$$

Now, if we assume that these points come from some point of $\mathbb{P}^n$, that point must belong to $U_i\cap U_j$, and since $x_i,x_j\neq 0$ on this set, we must have $x_{j/i}, x_{i/j}\neq 0$. For convenience of notation, let $j>i$; using this fact, we have

$$[x_{0/i}:\ldots: x_{(i-1)/i}: 1: x_{(i+1)/i}: \ldots: x_{j/i}:\ldots: x_{n/i}]=\left[\frac{x_{0/i}}{x_{j/i}}:\ldots: \frac{x_{(i-1)/i}}{x_{j/i}}: \frac{1}{x_{j/i}}: \frac{x_{(i+1)/i}}{x_{j/i}}: \ldots: 1:\ldots: \frac{x_{n/i}}{x_{j/i}}\right]$$

Therefore, in order for the point on the right-hand side to equal

$$[x_{0/j}:\ldots: x_{(j-1)/j}: 1: x_{(j+1)/j}: \ldots: x_{n/j}]$$

the equations

$$x_{k/i}/x_{j/i}=x_{k/j}\quad\text{for all $k\neq i,j$},\qquad\text{and}\qquad x_{i/j}=1/x_{j/i}$$

must hold. Similarly, matching the point of $P_j$ to the point of $P_i$ would yield equations such as $x_{k/j}/x_{i/j}=x_{k/i}$, but this is not a new equation by virtue of $x_{i/j}=1/x_{j/i}$.

Now, based on this computation, let us generalize [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10){: data-lid="4v3ha" }. First, consider the $n+1$ affine $n$-spaces

$$P_i=\Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)=\Spec A^i$$

Then, on $P_i$, the open subschemes $P_{ij}=D(\x_{j/i})\cong \Spec (A^i)_{\x_{j/i}}$ and the isomorphisms $\varphi_{ij}:P_{ij} \rightarrow P_{ji}$ defined by the spectrum of the following ring homomorphism

$$(A^j)_{\x_{i/j}} \rightarrow (A^i)_{\x_{j/i}};\qquad \x_{k/j}\mapsto \x_{k/i}/\x_{j/i}\quad\text{for all $k\neq i,j$},\qquad\text{and}\qquad \x_{i/j}\mapsto 1/\x_{j/i}$$

almost trivially satisfy the cocycle condition of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="7y8hq" }, and therefore a unique scheme $\mathbb{P}^n$ is defined. Here, restricted to points whose coordinates consist of elements of $\mathbb{K}$ (that is, points that can be written in the form $[x_0:\ldots:x_n]$ as in the preceding topological discussion), $U_i$ is precisely the set satisfying the condition $x_i\neq 0$. Of course, just as was the case for $\mathbb{A}^n$, there also exist points in $\mathbb{P}^n$ that cannot be written in such coordinates.

## Projective Schemes

For now, there are parts of the above explanation that are incomplete. For instance, although the fact that the $U_i$ are open subschemes of $\mathbb{P}^n$ is a consequence of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="62v1z" }, by their very definition they also seem like they should be open sets, being the sets where the function $\x_i$ does not become $0$. However, the problem lies in the fact that $\x_i$ is not a function on $\mathbb{P}^n$. Even looking only at the case $n=1$, we have verified that $\mathcal{O}_{\mathbb{P}^1}(\mathbb{P}^1)\cong \mathbb{K}$. This can be confirmed even from the topological construction alone: on $\mathbb{R}^{n+1}\setminus \{0\}$, the rule taking a point $(x_0,\ldots, x_n)$ and returning $x_i$, that is, the function $\x_i: \mathbb{R}^{n+1}\setminus\{0\} \rightarrow \mathbb{R}$, is not compatible with $\sim$, and therefore does not define a function on $\mathbb{P}^n$. As another example, if a function on $\mathbb{R}^2\setminus\{0\}$, $f: \mathbb{R}^2\setminus\{0\} \rightarrow \mathbb{R}$, is given by the formula

$$f(x_0,x_1)=x_0^2-x_1$$

then

$$f(\lambda x_0,\lambda x_1)=\lambda^2x_0^2-\lambda x_1\neq f(x_0,x_1)$$

so that $f$ is not well-defined. Instead, if we take $f$ to be a *homogeneous polynomial*, then even if $f$ as a function is not well-defined, the zero locus of $f$, $Z(f)$, is well-defined. This is because the equation

$$f(\lambda x_0,\ldots, \lambda x_n)=\lambda^{\deg f} f(x_0,\ldots, x_n),\qquad \lambda\neq 0$$

holds.

That is, in order to describe $\mathbb{P}^n$ in a way similar to the spectrum, rather than viewing $\mathbb{A}^{n+1}$ merely as the spectrum of the ring $\mathbb{K}[\x_0,\ldots, \x_n]$, we must add information about degrees to view it as a *graded* ring, and consider the zero loci of *homogeneous* elements rather than those of arbitrary elements. Then, considering [\[Algebraic Structures\] §Graded Rings, ⁋Proposition 6](/en/math/algebraic_structures/graded_rings#prop6){: data-lid="zjxhh" }, our objects of interest must also be *homogeneous* ideals.

In the remainder of this post, we follow the process of taking $\Proj$ of a graded ring to obtain a scheme. The $\Proj$ of an arbitrary graded ring is not necessarily a projective scheme. For instance, if we set $A_\bullet=\mathbb{K}[\x_1,\x_2,\ldots]$, then $\Proj A_\bullet$ is not even quasi-compact, so the term projective scheme is defined separately along with a finite generation condition in [§Closed Subschemes of Projective Space, ⁋Definition 7](/en/math/scheme_theory/closed_subschemes_of_projective_spaces#def7){: data-lid="t8ouc" }. For this purpose, we fix some notation.

::: remark Remark {#rmk}
Unless stated otherwise, a graded ring is always assumed to be $\mathbb{N}_{\geq0}$-graded. That is, the ring of our interest is always of the form

$$A_\bullet=\bigoplus_{i=0}^\infty A_i=A_0\oplus A_1\oplus\cdots$$

At this time, since $A_0$ is itself a ring, $A_\bullet$ can be regarded as a graded $A_0$-algebra, and for this reason $A_0$ is called the *base ring*. In addition, when we have occasion to forget the grading structure defined on $A_\bullet$ and view it as an ordinary ring, we agree to write it simply as $A$.
:::

Let a graded ring $A_\bullet$ be given. Then the following subset

$$A_+=\bigoplus_{i=1}^\infty A_i=A_1\oplus A_2\oplus\cdots$$

is trivially a homogeneous ideal of $A_\bullet$. However, if we consider the case $A_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$, the point where, for all elements of $A_+$, the function value is $0$ (that is, the point that is identically $0$ for all polynomials) is only the origin. Since the origin is the point removed when constructing $\mathbb{P}^n$, it is appropriate to exclude ideals containing the ideal $A_+$ from our discussion. From this point of view, $A_+$ is called the *irrelevant ideal*.

This can also be interpreted somewhat more geometrically. By the equation $f(\lambda x_0,\ldots,\lambda x_n)=\lambda^{\deg f}f(x_0,\ldots,x_n)$ above, the closed sets cut out in $\mathbb{A}^{n+1}$ by homogeneous polynomials are always closed under scalar multiplication, so they are collections of lines passing through the origin, namely affine cones. ([\[Algebraic Varieties\] §Projective Varieties, ⁋Definition 12](/en/math/algebraic_varieties/projective_varieties#def12){: data-lid="296n4" }) However, among affine cones there is also the cone consisting only of the origin, that is, the cone cut out by $A_+$, and in the case of this cone, removing the origin leaves only the empty set, so this cone should be excluded from our consideration. For a homogeneous prime ideal $\mathfrak{p}$, the condition $A_+\subseteq \mathfrak{p}$ is equivalent to the cone cut out by $\mathfrak{p}$ being the origin, so we exclude such $\mathfrak{p}$ and define $\Proj A_\bullet$.

::: Definition 1
For a graded ring $A_\bullet$, $\Proj A_\bullet$ is defined as the set

$$\Proj A_\bullet =\{\mathfrak{p}\in \Spec A\mid\text{$\mathfrak{p}$ is homogeneous and $A_+\not\subseteq \mathfrak{p}$}\}$$
:::

By definition, $\Proj A_\bullet$ is a subset of $\Spec A$. That is, all points of $\Proj A_\bullet$ are also points of $\Spec A$. This would be a somewhat awkward result if, instead of $\Spec A$, we had used $\MaxSpec A$, but $\Spec A$ contains points corresponding to prime ideals in addition to traditional points. For example, in $A=\mathbb{K}[\x_1,\x_2]$, if we consider the ideal $(\x_1-\x_2)$, since $\mathbb{K}[\x_1,\x_2]/(\x_1-\x_2)\cong \mathbb{K}[\x_1]$, this ideal is a prime ideal. Moreover, when $\mathbb{K}[\x_1,\x_2]$ is viewed as a graded ring $A_\bullet$, this ideal is a homogeneous prime ideal not containing $A_+$, so it is also a point of $\Proj A_\bullet$.

So far, $\Proj A_\bullet$ is merely a set. To give it a topological structure, we must use zero loci of functions, and as observed earlier, we must use zero loci of *homogeneous* polynomials.

::: Definition 2
Let a graded ring $A_\bullet$ be given. In $A_\bullet$, for a homogeneous ideal $\mathfrak{a}$, we define

$$Z_+(\mathfrak{a})=\{\mathfrak{p}\in\Proj A_\bullet\mid \mathfrak{a}\subseteq \mathfrak{p}\}$$
:::

Then, using the third result of [\[Commutative Algebra\] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2){: data-lid="zx79p" }, we can show the following lemma, similar to [§The Spectrum, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6){: data-lid="mjbfq" } and [§The Spectrum, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5){: data-lid="47fej" }.

::: Lemma 3
For a graded ring $A_\bullet$, the following hold.

1. For any homogeneous ideals $\mathfrak{a},\mathfrak{b}$, we have $Z_+(\mathfrak{a}\mathfrak{b})=Z_+(\mathfrak{a})\cup Z_+(\mathfrak{b})$.
2. For any family of homogeneous ideals $\{\mathfrak{a}_i\}$, we have $Z_+(\sum \mathfrak{a}_i)=\bigcap Z_+(\mathfrak{a}_i)$.
3. For any homogeneous ideal $\mathfrak{a}$, we have $Z_+(\sqrt{\mathfrak{a}})=Z_+(\mathfrak{a})$.
4. For any homogeneous ideal $\mathfrak{a}$, we have $Z_+(\mathfrak{a})=Z_+(\mathfrak{a}\cap A_+)$.
:::

Of course, it is trivial that $\mathfrak{a}\mathfrak{b}$, $\sqrt{\mathfrak{a}}$, and $\sum \mathfrak{a}_i$ appearing in the above lemma are homogeneous. Then the first through third results are results already observed in the spectrum, and only the fourth result is new.

::: Proof (Lemma 3)
1. Since it is trivial that a homogeneous prime ideal $\mathfrak{p}$ containing $\mathfrak{a}$ or $\mathfrak{b}$ also contains the smaller homogeneous ideal $\mathfrak{a}\mathfrak{b}$, it suffices to show the reverse inclusion. Assume $\mathfrak{p}\supset \mathfrak{a}\mathfrak{b}$. If $\mathfrak{p}\not\supseteq \mathfrak{b}$, we can find an element $b$ of $\mathfrak{b}$ such that $b\not\in \mathfrak{p}$. Then since $\mathfrak{b}$ is homogeneous, decomposing it into a sum of homogeneous elements we can write
    
    $$b=b_1+\cdots+b_n,\qquad \text{$b_i\in \mathfrak{b}$ homogeneous}$$

    On the other hand, for any homogeneous element $a\in \mathfrak{a}$, we have $ab\in \mathfrak{a}\mathfrak{b}\subseteq \mathfrak{p}$. Considering the element

    $$ab=ab_1+\cdots+ab_n$$

    of $\mathfrak{a}\mathfrak{b}\subseteq \mathfrak{p}$, since $\mathfrak{p}$ is homogeneous, all the $ab_i$ are elements of $\mathfrak{p}$. Meanwhile, by the preceding assumption $b\not\in \mathfrak{p}$, so there exists $i$ satisfying $b_i\not\in \mathfrak{p}$, and then $ab_i$ is a homogeneous element belonging to $\mathfrak{p}$ with $b_i\not\in \mathfrak{p}$, so from $\mathfrak{p}$ being a prime ideal we have $a\in \mathfrak{p}$. Therefore, by [\[Commutative Algebra\] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2), $\mathfrak{a}\subseteq \mathfrak{p}$ holds.
2. This is trivial since $\sum \mathfrak{a}_i$ is defined as the smallest ideal containing each of the ideals $\mathfrak{a}_i$.
3. [\[Commutative Algebra\] §Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8){: data-lid="pb4ln" }.
4. By definition $Z_+(\mathfrak{a})\subseteq Z_+(\mathfrak{a}\cap A_+)$ is trivial, so it suffices to show the reverse inclusion. That is, let $\mathfrak{p}$ be a prime ideal containing all homogeneous elements of $\mathfrak{a}$ of positive degree but not containing $A_+$ entirely, and let us show $\mathfrak{a}\subseteq \mathfrak{p}$. For this, it suffices to show that when choosing any $a\in \mathfrak{a}\cap A_0$, from the above assumption $a$ also belongs to $\mathfrak{p}$.  
    Now since $A_+\not\subseteq\mathfrak{p}$, there exists a homogeneous element $f$ not belonging to $\mathfrak{p}$. Then $af\in \mathfrak{a}\cap A_+\subseteq \mathfrak{p}$, and since $f\not\in \mathfrak{p}$ we have $a\in \mathfrak{p}$.
:::

Looking at the results of this lemma, from the first and second results we can define the following.

::: Definition 4
Let a graded ring $A_\bullet$ be given. For any homogeneous ideal $\mathfrak{a}$, the (unique) topology on $\Proj A_\bullet$ having sets of the form $Z_+(\mathfrak{a})$ as closed sets is called the *Zariski topology*.
:::

Also, by the fourth result of this lemma, we know that when defining the topology on $\Proj A_\bullet$, we only need to consider homogeneous ideals contained in $A_+$. This is intuitively obvious as well, because if we set $A=\mathbb{K}[\x_0,\ldots, \x_n]$, the elements in $A_0$ are constant functions anyway.

Now we define the following.

::: Definition 5
For a graded ring $A_\bullet$ and any homogeneous element $f$, we denote the complement of $Z_+(f)$ in $\Proj A_\bullet$, that is, $\Proj A_\bullet\setminus Z_+(f)$, by $D_+(f)$. Here, for a homogeneous element $f$, $Z_+(f)$ is an abbreviation for $Z_+((f))$, and similarly, for any homogeneous ideal $\mathfrak{a}$, we denote $\Proj A_\bullet\setminus Z_+(\mathfrak{a})$ by $D_+(\mathfrak{a})$.
:::

The following corollary follows immediately from the first result of [Lemma 3](#lem3){: data-lid="vh2lx" }.

::: Corollary 6
We have $D_+(f)\cap D_+(g)=D_+(fg)$.
:::

Moreover, the following holds.

::: Corollary 7
The collection of $D_+(f)$ forms a base for $\Proj A_\bullet$.
:::
::: Proof
For $A$, writing an arbitrary homogeneous ideal $\mathfrak{a}$ using homogeneous generators as $\mathfrak{a}=\sum_{i\in I} (f_i)$, we have

$$Z_+(\mathfrak{a})=\bigcap_{i\in I} Z_+((f_i))$$

and therefore

$$D_+(\mathfrak{a})=\bigcup_{i\in I} D_+(f_i)$$
:::

Meanwhile, we have seen that for a ring $A$, on the spectrum $\Spec A$, choosing any element $f\in A$ makes $D(f)$ isomorphic (as a scheme) to $\Spec A_f$. A similar result holds for $D_+(f)$.

::: Lemma 8
For a graded ring $A_\bullet$ and any nonzero homogeneous element of $A_+$, $f$, the map $D_+(f) \rightarrow \Spec A_{(f)}$ defined by the formula

$$\mathfrak{p}\mapsto \mathfrak{p}A_f\cap A_{(f)}$$

is a homeomorphism. ([\[Commutative Algebra\] §Localization of Graded Rings, ⁋Definition 5](/en/math/commutative_algebra/localization_of_graded_rings#def5){: data-lid="zt57y" })
:::
::: Proof
First, since $f\not\in \mathfrak{p}$, through the localization $A \rightarrow A_f$, the ideal $\mathfrak{p}$ is sent to the prime ideal of $A_f$, namely $\mathfrak{p}A_f$. ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="mqr3m" }) Now the right-hand side of the claim is the preimage under the inclusion $i: A_{(f)} \rightarrow A_f$ of $\mathfrak{p}A_f$, so this becomes a prime ideal of $A_{(f)}$.

Now let us define the inverse map $\Spec A_{(f)} \rightarrow D_+(f)$ of this correspondence as a function. Suppose that an arbitrary prime ideal $\mathfrak{q}\in\Spec A_{(f)}$ is given. In $A$, among the homogeneous elements $x$, consider the condition

$$\frac{x^{\deg f}}{f^{\deg x}}\in \mathfrak{q}$$

After collecting those $x$ satisfying this condition, consider the homogeneous ideal of $A$ generated by them, $\mathfrak{p}$. Here what needs to be checked is that the set of homogeneous elements satisfying the above condition already forms an ideal, that is, the sum of two elements of the same degree and the product with an arbitrary homogeneous element again satisfy that condition. The product case is trivial, and for the sum case one uses the fact that when $(x+y)^{\deg f}$ is expanded binomially, each term $x^ky^{\deg f-k}/f^{\deg x}$ raised to the $\deg f$-th power becomes a product of powers of $x^{\deg f}/f^{\deg x}$ and $y^{\deg f}/f^{\deg y}$, together with $\mathfrak{q}$ being prime.

Then since the homogeneous elements of $\mathfrak{p}$ are precisely those satisfying the above condition, for any homogeneous elements $x,y\in A$ we have

$$xy\in \mathfrak{p}\iff \frac{x^{\deg f}}{f^{\deg x}}\frac{y^{\deg f}}{f^{\deg y}}\in \mathfrak{q}$$

and from $\mathfrak{q}$ being a prime ideal together with the third result of [\[Commutative Algebra\] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2){: data-lid="ikvo3" }, we see that $\mathfrak{p}$ is a prime ideal. Also $f^{\deg f}/f^{\deg f}=1\not\in \mathfrak{q}$, so $f\not\in \mathfrak{p}$, and therefore $\mathfrak{p}$ does not contain $A_+$, so that $\mathfrak{p}\in D_+(f)$. Now it is easy to verify that this correspondence $\mathfrak{p}\mapsto \mathfrak{p}A_f\cap A_{(f)}$ and $\mathfrak{q}\mapsto \mathfrak{p}$ are inverse to each other, and for any homogeneous ideal of $A_\bullet$, $\mathfrak{a}$, the closed set in $D_+(f)$ given by $Z_+(\mathfrak{a})\cap D_+(f)$ is sent by this function to the closed set in $\Spec A_{(f)}$ given by $Z(\mathfrak{a}A_f\cap A_{(f)})$, from which we know that this is a homeomorphism.
:::

Then the way to give $\Proj A_\bullet$ a scheme structure is now obvious. The proof of the following lemma is almost identical to that of [Lemma 8](#lem8){: data-lid="1k0tn" }.

::: Lemma 9
For a graded ring $A_\bullet$ and nonzero homogeneous elements $f,g$ of $A_+$, there exists an isomorphism

$$\Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})\subseteq \Spec A_{(f)}$$
:::
::: Proof
In $\Proj A_\bullet$, any point $\mathfrak{p}$ satisfies $A_+\not\subseteq \mathfrak{p}$, so outside $\mathfrak{p}$ there is a homogeneous element of $A_+$. That is, since $\Proj A_\bullet$ is covered by the open sets given by nonzero homogeneous elements of $A_+$, namely $D_+(f)$, restricting the assumption to such $f$ causes no loss for our purpose. Now if we write $d=\deg f\geq 1$ and $e=\deg g\geq 1$, then since $\deg (g^d)=de=\deg (f^e)$,

$$\theta=\frac{g^{\deg f}}{f^{\deg g}}=\frac{g^d}{f^e}$$

is, in $A_f$, an element of degree $0$, that is, $\theta\in A_{(f)}$. ([\[Commutative Algebra\] §Localization of Graded Rings, ⁋Proposition 3](/en/math/commutative_algebra/localization_of_graded_rings#prop3){: data-lid="i1n9v" }) On the other hand, since $D(\theta)$ is isomorphic to $\Spec (A_{(f)})_\theta$ as an open subscheme of $\Spec A_{(f)}$ ([§Schemes, ⁋Lemma 2](/en/math/scheme_theory/schemes#lem2){: data-lid="jpe83" }), it suffices for us to construct a ring isomorphism $(A_{(f)})_\theta\cong A_{(fg)}$.

First, since the localization $A_f \rightarrow A_{fg}$ preserves the grading, restricting it to the degree $0$ part yields the canonical ring homomorphism

$$\rho: A_{(f)} \rightarrow A_{(fg)};\qquad \frac{a}{f^n}\mapsto \frac{ag^n}{(fg)^n}$$

Here, $f^e/g^d$ is, in $A_{fg}$, an element of degree $0$, and since

$$\frac{g^d}{f^e}\cdot\frac{f^e}{g^d}=1$$

$\rho(\theta)$ is a unit of $A_{(fg)}$. Therefore, by [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="kiuv5" }, there exists a unique ring homomorphism extending $\rho$,

$$\Phi:(A_{(f)})_\theta \rightarrow A_{(fg)};\qquad \frac{x}{\theta^n}\mapsto \rho(x)\left(\frac{f^e}{g^d}\right)^n$$

Let us show that $\Phi$ is surjective. Any element of $A_{(fg)}$ can be written, for a homogeneous element $a$ and $n\geq 0$, in the form $a/(fg)^n$, and since the degree of this element is $0$, we have $\deg a=n(d+e)$. Now setting

$$x=\frac{ag^{n(d-1)}}{f^{n(e+1)}}$$

the degree of the numerator is

$$n(d+e)+en(d-1)=n(d+ed)=nd(e+1)$$

and the degree of the denominator is $dn(e+1)$, which equals this, so $x\in A_{(f)}$. (Here $d\geq 1$ is used.) Then in $A_{fg}$,

$$\Phi\left(\frac{x}{\theta^n}\right)=\frac{ag^{n(d-1)}}{f^{n(e+1)}}\cdot\frac{f^{ne}}{g^{nd}}=\frac{a}{f^ng^n}=\frac{a}{(fg)^n}$$

so $\Phi$ is surjective.

Now let us show that $\Phi$ is injective. Suppose an element of $(A_{(f)})_\theta$, $x/\theta^n$, is sent by $\Phi$ to $0$. Since $\Phi(\theta)$ is a unit, this is equivalent to $\rho(x)=0$. If we write $x=b/f^m$, where $b$ is a homogeneous element with $\deg b=md$, then $\rho(x)=0$ means that in $A_{fg}$ we have $b/f^m=0$, so there exists $k\geq 0$ such that $(fg)^kb=0$. Then since $d\geq 1$,

$$f^k\cdot bg^{dk}=(f^kg^kb)g^{(d-1)k}=0$$

and therefore in $A_f$ we have $bg^{dk}=0$. From this, in $A_{(f)}$,

$$\theta^kx=\frac{g^{dk}}{f^{ek}}\cdot\frac{b}{f^m}=\frac{bg^{dk}}{f^{ek+m}}=0$$

so that in $(A_{(f)})_\theta$, $x/\theta^n=0$. That is, $\Phi$ is injective, and from the above, $\Phi$ is an isomorphism.

Finally, let us verify that this isomorphism is compatible with the homeomorphism of [Lemma 8](#lem8){: data-lid="c3pcn" }. Letting the image of $\mathfrak{p}\in D_+(f)$ be $\mathfrak{q}=\mathfrak{p}A_f\cap A_{(f)}$, since $f\not\in \mathfrak{p}$, we have

$$\theta=\frac{g^d}{f^e}\in \mathfrak{q}\iff g^d\in \mathfrak{p}\iff g\in \mathfrak{p}$$

Therefore, the homeomorphism of [Lemma 8](#lem8){: data-lid="d41xx" } sends $D_+(fg)=D_+(f)\cap D_+(g)$ of [Corollary 6](#cor6){: data-lid="8wg0r" } exactly onto $D(\theta)$.
:::

Therefore, there exists an isomorphism between the principal open set of $\Spec A_{(g)}$, $D(f^{\deg g}/g^{\deg f})\subseteq \Spec A_{(g)}$, and the principal open set of $\Spec A_{(f)}$, $\Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})$. Now the following theorem is a simple computation.

::: Theorem 10
The $\Spec A_{(f)}$, the open subschemes $D(g^{\deg f}/f^{\deg g})$, and the isomorphisms

$$D(f^{\deg g}/g^{\deg f})\cong \Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})$$

defined above satisfy all the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="6ghcs" }, and therefore give a unique scheme structure on $\Proj A_\bullet$.
:::
::: Proof
As the index set, we take all nonzero homogeneous elements of $A_+$. If for two elements $f,g$ we write, as in the proof of [Lemma 9](#lem9){: data-lid="zuz54" },

$$\theta_{f,g}=\frac{g^{\deg f}}{f^{\deg g}}\in A_{(f)}$$

what that proof showed is that the canonical ring homomorphism $\rho_{f,fg}:A_{(f)} \rightarrow A_{(fg)}$ sends $\theta_{f,g}$ to a unit, and the induced

$$\Phi_{f,g}:(A_{(f)})_{\theta_{f,g}} \rightarrow A_{(fg)}$$

is an isomorphism extending $\rho_{f,fg}$. Now considering $X_f=\Spec A_{(f)}$ and its open subscheme $X_{fg}=D(\theta_{f,g})$, and noting that $A_{(fg)}=A_{(gf)}$, we define the isomorphism $\varphi_{fg}:X_{fg} \rightarrow X_{gf}$ as the spectrum of the ring isomorphism

$$\Phi_{f,g}^{-1}\circ \Phi_{g,f}:(A_{(g)})_{\theta_{g,f}} \rightarrow (A_{(f)})_{\theta_{f,g}}$$

Here, if $fg=0$, then $\theta_{f,g}=0$ and $\theta_{g,f}=0$, so $X_{fg}$ and $X_{gf}$ are both empty, and in this case we set $\varphi_{fg}$ to be the identity of the empty scheme. First, when $f=g$, we have $\theta_{f,f}=1$ so $X_{ff}=X_f$, and since $A_{f\cdot f}=A_f$, the map $\rho_{f,ff}$ is the identity and therefore $\varphi_{ff}=\id$.

Now let us verify the cocycle condition. Choose nonzero homogeneous elements $f,g,h\in A_+$ and let $d=\deg f$, $e=\deg g$, $m=\deg h$. Then in $A_{(f)}$,

$$\theta_{f,g}\theta_{f,h}=\frac{g^d}{f^e}\cdot\frac{h^d}{f^m}=\frac{(gh)^d}{f^{e+m}}=\theta_{f,gh}$$

so the triple intersection inside $X_f$ is

$$X_{fg}\cap X_{fh}=D(\theta_{f,g})\cap D(\theta_{f,h})=D(\theta_{f,gh})$$

If $gh=0$, then $\theta_{f,gh}=0$, so this triple intersection is empty and the cocycle condition holds vacuously. The cases $fg=0$ or $fh=0$ are similar since $\theta_{f,g}=0$ or $\theta_{f,h}=0$, so in what follows we only treat the case where $fg$, $gh$, and $fh$ are all nonzero. Then applying [Lemma 9](#lem9){: data-lid="ouycv" } to $f$ and $gh$, we obtain the isomorphism

$$\Psi_f=\Phi_{f,gh}:(A_{(f)})_{\theta_{f,gh}} \rightarrow A_{(fgh)}$$

Similarly defining $\Psi_g=\Phi_{g,fh}$ and $\Psi_h=\Phi_{h,fg}$, these respectively extend the canonical homomorphisms $\rho_{f,fgh}$, $\rho_{g,fgh}$, $\rho_{h,fgh}$. On the other hand, since these canonical homomorphisms are all degree $0$ parts of localizations like $A_f \rightarrow A_{fg} \rightarrow A_{fgh}$, they satisfy transitivity such as

$$\rho_{fg,fgh}\circ\rho_{f,fg}=\rho_{f,fgh}$$

First, let us verify that $\varphi_{fg}$ sends the triple intersection to the triple intersection. $\Phi_{f,g}$ and $\Phi_{g,f}$ send $\theta_{f,h}$ and $\theta_{g,h}$ respectively to the elements

$$u=\frac{h^d}{f^m},\qquad v=\frac{h^e}{g^m}$$

of $A_{(fg)}$, and in $A_{(fg)}$,

$$u^e=\frac{h^{de}}{f^{me}}=\left(\frac{g^d}{f^e}\right)^m\cdot\frac{h^{de}}{g^{md}}=\rho_{f,fg}(\theta_{f,g})^mv^d$$

and $\rho_{f,fg}(\theta_{f,g})$ is a unit. Therefore $u^e$ and $v^d$ differ only by a unit multiple, so in $\Spec A_{(fg)}$ we have $D(u)=D(v)$, and localizing $A_{(fg)}$ at $u$ and at $v$ yields the same ring. That is, $\varphi_{fg}$ maps $X_{fg}\cap X_{fh}$ onto $X_{gf}\cap X_{gh}$, and this restriction is the spectrum of the ring homomorphism

$$\alpha:(A_{(g)})_{\theta_{g,fh}} \rightarrow (A_{(f)})_{\theta_{f,gh}}$$

Here $\alpha$ is obtained by localizing $\Phi_{f,g}^{-1}\circ\Phi_{g,f}$. If we consider the composition

$$\tau: A_{(fg)}\overset{\Phi_{f,g}^{-1}}{\rightarrow}(A_{(f)})_{\theta_{f,g}} \rightarrow (A_{(f)})_{\theta_{f,gh}}\overset{\Psi_f}{\rightarrow} A_{(fgh)}$$

then since $\Phi_{f,g}$ and $\Psi_f$ respectively extend $\rho_{f,fg}$ and $\rho_{f,fgh}$, we have $\tau\circ\rho_{f,fg}=\rho_{f,fgh}$. However, since $A_{(fg)}$ is the localization of $A_{(f)}$ at $\theta_{f,g}$ via $\Phi_{f,g}$ and $\rho_{fg,fgh}$ also satisfies the same equation, by the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="panmq" } we have $\tau=\rho_{fg,fgh}$. From this we obtain

$$\Psi_f\circ\alpha\vert_{A_{(g)}}=\tau\circ \rho_{g,fg}=\rho_{fg,fgh}\circ\rho_{g,fg}=\rho_{g,fgh}=\Psi_g\vert_{A_{(g)}}$$

and applying the uniqueness in [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="vquwv" } again to the localization $(A_{(g)})_{\theta_{g,fh}}$ of $A_{(g)}$, we get $\Psi_f\circ\alpha=\Psi_g$, that is, $\alpha=\Psi_f^{-1}\circ\Psi_g$. That is,

$$\varphi_{fg}\vert_{X_{fg}\cap X_{fh}}=\Spec(\Psi_f^{-1}\circ \Psi_g)$$

and applying the same argument to $(g,h)$ and $(f,h)$, on the triple intersection we have

$$\varphi_{gh}=\Spec(\Psi_g^{-1}\circ\Psi_h),\qquad \varphi_{fh}=\Spec(\Psi_f^{-1}\circ\Psi_h)$$

Since $\Spec$ is contravariant,

$$\varphi_{gh}\circ\varphi_{fg}=\Spec\left((\Psi_f^{-1}\circ\Psi_g)\circ(\Psi_g^{-1}\circ \Psi_h)\right)=\Spec(\Psi_f^{-1}\circ\Psi_h)=\varphi_{fh}$$

so the cocycle condition holds. Therefore by [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="y12iw" } there exists a unique scheme $X$ having the $X_f$ as open subschemes with $X_f\cap X_g=X_{fg}$.

Finally, let us verify that the underlying topological space of $X$ is $\Proj A_\bullet$. [Lemma 8](#lem8){: data-lid="01mup" } gives homeomorphisms $\psi_f: D_+(f) \rightarrow \Spec A_{(f)}=X_f$, and as checked in the proof of [Lemma 9](#lem9){: data-lid="ylfff" }, $\psi_f$ maps $D_+(fg)$ onto $X_{fg}=D(\theta_{f,g})$. Moreover, for any $\mathfrak{p}\in D_+(fg)$ the preimage of $\mathfrak{p}A_{fg}\cap A_{(fg)}$ under $\rho_{f,fg}$ is $\mathfrak{p}A_f\cap A_{(f)}$ ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="ejm2i" }), so $\psi_f$ and $\psi_g$ are compatible with $\varphi_{fg}$. That is, $\psi_g=\varphi_{fg}\circ\psi_f$ holds on $D_+(fg)$. On the other hand, as observed above, the $D_+(f)$ cover $\Proj A_\bullet$, so gluing the $\psi_f$ we obtain a homeomorphism between the underlying topological space of $X$ and $\Proj A_\bullet$. Through this, $\Proj A_\bullet$ acquires a scheme structure, and by the uniqueness in [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9){: data-lid="uxl9g" } this scheme structure is unique.
:::

In particular, since $\Proj A_\bullet$ is a locally ringed space, for any $\mathfrak{p}\in \Proj A_\bullet$ the stalk $\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}$ is a local ring. But since $\mathfrak{p}$ can be put into a suitable affine open neighborhood anyway, we can show the following by essentially the same procedure as [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-lid="7a2ho" }.

::: Lemma 11
For a graded ring $A_\bullet$ and any $\mathfrak{p}\in \Proj A_\bullet$, there exists an isomorphism

$$\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}\cong A_{(\mathfrak{p})}$$
:::
::: Proof
Since $\mathfrak{p}\in \Proj A_\bullet$, we have $A_+\not\subseteq \mathfrak{p}$, and therefore there exists a homogeneous element $f$ of $A_+$ not belonging to $\mathfrak{p}$. Let $d=\deg f\geq 1$. Then $\mathfrak{p}\in D_+(f)$, and by [Theorem 10](#thm10){: data-lid="s62c1" }, $D_+(f)$ is an open subscheme of $\Proj A_\bullet$ isomorphic to $\Spec A_{(f)}$. Since the stalk of an open subscheme equals the stalk of the original scheme, for the point $\mathfrak{q}=\mathfrak{p}A_f\cap A_{(f)}$ to which [Lemma 8](#lem8){: data-lid="eypnp" } sends $\mathfrak{p}$, from [§Affine Scheme, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8){: data-lid="v4h8x" } we obtain

$$\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}\cong \mathcal{O}_{\Spec A_{(f)},\mathfrak{q}}\cong (A_{(f)})_\mathfrak{q}$$

Therefore, it suffices to construct an isomorphism $(A_{(f)})_\mathfrak{q}\cong A_{(\mathfrak{p})}$.

Let $S$ be the multiplicative set consisting of homogeneous elements not belonging to $\mathfrak{p}$; then $A_{(\mathfrak{p})}=(S^{-1}A)_0$. ([\[Commutative Algebra\] §Localization of Graded Rings, ⁋Definition 5](/en/math/commutative_algebra/localization_of_graded_rings#def5){: data-lid="zcqst" }) Now since $f\in S$, the localization $A_f \rightarrow S^{-1}A$ exists, and since this preserves the grading, restricting to the degree $0$ part we obtain the canonical ring homomorphism

$$\sigma: A_{(f)} \rightarrow A_{(\mathfrak{p})};\qquad \frac{a}{f^n}\mapsto \frac{a}{f^n}$$

Here, $\sigma$ sends elements of $A_{(f)}\setminus \mathfrak{q}$ to units. Indeed, if $x=a/f^n\in A_{(f)}$, then $a$ is a homogeneous element with $\deg a=nd$, and since $f\not\in \mathfrak{p}$, by [\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="gybvt" },

$$x\in \mathfrak{q}\iff a\in \mathfrak{p}$$

Therefore, if $x\not\in \mathfrak{q}$, then $a\in S$, and $f^n/a$ is an element of degree $0$ in $S^{-1}A$ that becomes the inverse of $\sigma(x)$. Now by [\[Commutative Algebra\] §Localization, ⁋Proposition 6](/en/math/commutative_algebra/localization#prop6){: data-lid="7ngej" }, there exists a unique ring homomorphism

$$\Theta:(A_{(f)})_\mathfrak{q} \rightarrow A_{(\mathfrak{p})}$$

extending $\sigma$.

Let us show that $\Theta$ is surjective. An arbitrary element of $A_{(\mathfrak{p})}$ is of the form $a/s$ for a homogeneous element $a$ and $s\in S$, and since this element has degree $0$, we have $l=\deg s=\deg a$. Now if we set

$$u=\frac{as^{d-1}}{f^l},\qquad v=\frac{s^d}{f^l}$$

then $\deg (as^{d-1})=l+l(d-1)=ld=\deg (f^l)$ and $\deg (s^d)=ld$, so $u,v\in A_{(f)}$. Also, since $s\not\in \mathfrak{p}$ and $\mathfrak{p}$ is a prime ideal, we have $s^d\not\in \mathfrak{p}$, and therefore $v\not\in \mathfrak{q}$. Then in $S^{-1}A$,

$$\Theta\left(\frac{u}{v}\right)=\frac{as^{d-1}}{f^l}\cdot\frac{f^l}{s^d}=\frac{a}{s}$$

so $\Theta$ is surjective.

Now let us show that $\Theta$ is injective. Suppose an element $x/v$ of $(A_{(f)})_\mathfrak{q}$ is sent to $0$ by $\Theta$. Since $\Theta(v)$ is a unit, $\sigma(x)=0$. If we write $x=a/f^n$, this means $a/f^n=0$ in $S^{-1}A$, so there exists a homogeneous element $t\in S$ such that $ta=0$. Now, since $\deg (t^d)=d\deg t=\deg (f^{\deg t})$,

$$w=\frac{t^d}{f^{\deg t}}$$

is an element of $A_{(f)}$, and since $t\not\in \mathfrak{p}$, we have $w\not\in \mathfrak{q}$. On the other hand, since $d\geq 1$, we have $t^da=0$, and therefore in $A_{(f)}$,

$$wx=\frac{t^da}{f^{\deg t+n}}=0$$

That is, $x=0$ in $(A_{(f)})_\mathfrak{q}$, so $x/v=0$, and $\Theta$ is injective. From the above, $\Theta$ is an isomorphism.
:::

One should be somewhat careful that, unlike $\Spec$, $\Proj$ does not define a functor from $\bgr_{\mathbb{N}_{\geq 0}}\cRing^\op$ to $\LRS$. This is because, for a graded ring homomorphism $\phi_\bullet:A_\bullet \rightarrow B_\bullet$, even if a homogeneous ideal $\mathfrak{q}$ of $B$ does not contain $B_+$, its inverse image $\phi^{-1}(\mathfrak{q})$ may contain $A_+$.

Now finally, we translate the projective space examined at the very beginning for motivation (almost) completely into the language of algebraic geometry.

::: Example 12
In algebraic geometry, $\mathbb{P}^n_\mathbb{K}$ is defined by the formula

$$\mathbb{P}^n_\mathbb{K}=\Proj \mathbb{K}[\x_0,\ldots, \x_n]$$

Here, the polynomial algebra $\mathbb{K}[\x_0,\ldots, \x_n]$ is of course a graded ring with grading given by degree.

Then the $n+1$ open covers of projective space can in this language be thought of as

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_{0},\ldots, \x_{n}]_{(\x_{i})}$$

and by [\[Commutative Algebra\] §Localization of Graded Rings, ⁋Proposition 6](/en/math/commutative_algebra/localization_of_graded_rings#prop6){: data-lid="krf98" }, we have

$$\mathbb{K}[\x_{0},\ldots, \x_{n}]_{(\x_{i})}\cong \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)$$

and explicitly this isomorphism is obtained by applying the first isomorphism theorem to the ring homomorphism

$$\mathbb{K}[\x_{0/i}, \ldots, \x_{n/i}]\rightarrow \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)};\qquad \x_{k/i}\mapsto \frac{\x_k}{\x_i}$$

Now any $\mathfrak{p}\in \mathbb{P}^n_\mathbb{K}$ is contained in some $D_+(\x_i)$. Through the above isomorphism, suppose the point $\mathfrak{p}$ of $D_+(\x_i)$ is sent to a point $\mathfrak{q}$ of $U_i=\Spec \mathbb{K}[\x_{0/i}, \ldots, \x_{n/i}]/(\x_{i/i}-1)$. Then in this case it would be natural to expect the following isomorphism

$$\mathcal{O}_{\mathbb{P}^n_\mathbb{K},\mathfrak{p}}\cong \mathcal{O}_{U_i, \mathfrak{q}}$$

And of course this holds. ([\[Commutative Algebra\] §Localization of Graded Rings, ⁋Proposition 8](/en/math/commutative_algebra/localization_of_graded_rings#prop8){: data-lid="4l1um" }) 
:::

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---
