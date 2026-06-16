---
title: "Projective Schemes"
description: "We construct projective space by gluing affine lines in a suitable way, and generalize this to define projective schemes. We understand projective spaces from a topological viewpoint and examine how to glue affine lines via stereographic projection and the cocycle condition."
excerpt: "The Proj construction from a graded ring and projective schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/projective_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-02
last_modified_at: 2025-02-03
weight: 13
translated_at: 2026-06-02T05:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T05:30:01+00:00
---
In [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) we glued two affine lines $$\mathbb{A}^1=\Spec \mathbb{K}[\x]$$ together in a suitable way to construct the projective space $$\mathbb{P}^1$$. In this post we generalize this construction to define projective schemes.

## Projective Space

Generalizing [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) directly, it is not difficult to define $$\mathbb{P}^n$$ as a scheme. However, in order to generalize this to define projective schemes, it helps to understand $$\mathbb{P}^n$$ intuitively, so let us unpack it more carefully.

First we briefly review the projective space defined in topology. To construct the topological space $$\mathbb{P}^n$$, we considered the topological space $$\mathbb{R}^{n+1}\setminus \{0\}$$. On this we define the following equivalence relation:

$$(x_0,\ldots, x_n)\sim (y_0,\ldots, y_n)\iff\text{$x_i=\lambda y_i$ for some $\lambda\neq 0$, for all $i$}$$

Then projective space $$\mathbb{P}^n$$ is defined as the quotient space $$(\mathbb{R}^{n+1}\setminus \{0\})/{\sim}$$, and the equivalence class containing $$(x_0,\ldots, x_n)$$ is denoted $$[x_0:x_1:\cdots:x_n]$$ for notational convenience.

Now consider the canonical projection $$\pi:\mathbb{R}^{n+1}\setminus\{0\}\rightarrow \mathbb{P}^n$$. The fiber over a point $$[x_0:x_1:\cdots:x_n]$$ in $$\mathbb{P}^n$$ is by definition

$$\{(y_0,\ldots, y_n)\mid\text{$x_i=\lambda y_i$ for some $\lambda\neq 0$, for all $i$}\}$$

that is, the set of points on the line through the origin and $$(x_0,\ldots, x_n)$$, excluding the origin itself. For this reason, $$\mathbb{P}^n$$ is often thought of as the space of lines in $$\mathbb{R}^{n+1}$$.

Meanwhile, in $$\mathbb{R}^{n+1}$$, any plane $$P$$ and any line not parallel to $$P$$ must meet at a single point. Thus, defining the plane $$P_i$$ as

$$P_i=\{\x_i=1\}=\{(x_0,\ldots, x_n)\mid x_i=1\}$$

the points of $$\mathbb{P}^n$$ excluding those corresponding to lines perpendicular to the $$\x_i$$-axis are in one-to-one correspondence with points of $$P_i$$, while the remaining points are lines in the $$\x_0\x_1\cdots\x_{i-1}\x_{i+1}\cdots\x_n$$-plane, i.e., lines in $$\mathbb{R}^n$$, so we obtain the decomposition

$$\mathbb{P}^n=\mathbb{R}^n\coprod \mathbb{P}^{n-1}$$

This process is illustrated in the following figure for the case $$n=2$$.

![stereographic_projection](/assets/images/Math/Scheme_Theory/Projective_Schemes-1.svg){:style="width:31.18em" class="invert" .align-center}

Writing this in formulas, for a point $$[x_0:\cdots:x_n]$$ in $$\mathbb{P}^n$$, if $$x_i\neq 0$$ then within the equivalence class of $$[x_0:\cdots:x_n]$$ we can (uniquely) find the point whose $$i$$-th coordinate is $$1$$; regarding this point as a point of $$P_i$$, we can identify the subset

$$U_i=\{[x_0:\cdots:x_n]\in \mathbb{P}^n\mid x_i\neq 0\}$$

with $$P_i\cong \mathbb{R}^n$$. On the other hand, the points in the complement of $$U_i$$ are exactly those with $$x_i=0$$, so by simply omitting the $$i$$-th coordinate we can understand them as points of $$\mathbb{P}^{n-1}$$.

Explicitly, the above identification $$U_i\cong P_i$$ is expressed by the formula

$$[x_0:\cdots:x_n]\text{ in $U_i\subseteq \mathbb{P}^n$}\leftrightarrow\left(\frac{x_0}{x_i},\ldots, \frac{x_{i-1}}{x_i},1,\frac{x_{i+1}}{x_i},\ldots, \frac{x_n}{x_i}\right)\text{ in $P_i\subseteq \mathbb{R}^{n+1}$}$$

Meanwhile, the procedure of [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) reverses this process. That is, we are first given $$n+1$$ copies of $$n$$-dimensional planes $$P_0,\ldots, P_n$$ and we glue them via isomorphisms satisfying the cocycle condition. How the cocycle condition should be written is obtained by examining how a point of $$\mathbb{P}^n$$ is written in different $$P_i$$ and $$P_j$$ under the above identification. Let us examine this. First, arbitrary points of $$P_i$$ and $$P_j$$ can be written in the form

$$(x_{0/i},\ldots, x_{(i-1)/i}, 1, x_{(i+1)/i}, \ldots, x_{n/i})\in P_i,\qquad (x_{0/j},\ldots, x_{(j-1)/j}, 1, x_{(j+1)/j}, \ldots, x_{n/j})\in P_j$$

Now, if we assume that these points come from some point of $$\mathbb{P}^n$$, then that point must lie in $$U_i\cap U_j$$, and in this set we must have $$x_i,x_j\neq 0$$, hence $$x_{j/i}, x_{i/j}\neq 0$$. For notational convenience assume $$j>i$$; using this,

$$[x_{0/i}:\ldots: x_{(i-1)/i}: 1: x_{(i+1)/i}: \ldots: x_{j/i}:\ldots, x_{n/i}]=\left[\frac{x_{0/i}}{x_{j/i}}:\ldots: \frac{x_{(i-1)/i}}{x_{j/i}}: \frac{1}{x_{j/i}}: \frac{x_{(i+1)/i}}{x_{j/i}}: \ldots: 1:\ldots, \frac{x_{n/i}}{x_{j/i}}\right]$$

Therefore, for the point on the right-hand side to equal

$$[x_{0/j}:\ldots: x_{(j-1)/j}: 1: x_{(j+1)/j}: \ldots: x_{n/j}]$$

the following formulas

$$x_{k/i}/x_{j/i}=x_{k/j}\quad\text{for all $k\neq i,j$},\qquad\text{and}\qquad x_{i/j}=1/x_{j/i}$$

must hold. Similarly, matching a point of $$P_j$$ to a point of $$P_i$$ would also yield formulas like $$x_{k/j}/x_{i/j}=x_{k/i}$$, but because of $$x_{i/j}=1/x_{j/i}$$ this is not a new formula.

Now let us generalize [§Schemes, ⁋Example 10](/en/math/scheme_theory/schemes#ex10) based on this computation. First, consider $$n+1$$ affine $$n$$-spaces

$$P_i=\Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(x_{i/i}-1)=\Spec A^i$$

Then the isomorphisms $$\varphi_{ij}:P_{ij} \rightarrow P_{ji}$$ defined via the open subschemes $$P_{ij}=D(\x_{j/i})=(A^i)_{\x_{j/i}}$$ of $$P_i$$ and the ring homomorphism

$$(A^i)_{\x_{j/i}} \rightarrow (A^j)_{\x_{i/j}};\qquad \x_{k/i}\mapsto \x_{k/j}/\x_{i/j}\quad\text{for all $k\neq i,j$},\qquad\text{and}\qquad \x_{j/i}\mapsto 1/\x_{i/j}$$

almost trivially satisfy the cocycle condition of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), and therefore define a unique scheme $$\mathbb{P}^n$$; if we write elements of $$\mathbb{P}^n$$ in the form $$[x_0:\ldots:x_n]$$, then $$U_i$$ is exactly the set of points satisfying $$x_i\neq 0$$.

## Projective Schemes

As it stands, the above explanation has some incomplete parts. For example, that the $$U_i$$ are open subschemes of $$\mathbb{P}^n$$ is a consequence of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), but by its very definition it seems that it should be an open set because it is the set where the function $$\x_i$$ is nonzero. However, the problem is that $$\x_i$$ is not a function on $$\mathbb{P}^n$$. Indeed, even in the case $$n=1$$ we have checked that $$\mathcal{O}_{\mathbb{P}^1}(\mathbb{P}^1)\cong \mathbb{K}$$. This can also be verified purely from the topological construction: the function $$\x_i: \mathbb{R}^{n+1}\setminus\{0\} \rightarrow \mathbb{R}$$ that takes a point $$(x_0,\ldots, x_n)$$ of $$\mathbb{R}^{n+1}\setminus \{0\}$$ and returns $$x_i$$ is not compatible with $$\sim$$, and therefore does not define a function on $$\mathbb{P}^n$$. As another example, if a function $$f: \mathbb{R}^2\setminus\{0\} \rightarrow \mathbb{R}$$ defined on $$\mathbb{R}^2\setminus\{0\}$$ is given by the formula

$$f(x_0,x_1)=x_0^2-x_1$$

then

$$f(\lambda x_0,\lambda x_1)=\lambda^2x_0^2-\lambda x_1\neq f(x_0,x_1)$$

so $$f$$ is not well defined. Instead, if we take $$f$$ to be a *homogeneous polynomial*, then even though $$f$$ itself is not well defined as a function, its zero locus $$Z(f)$$ is well defined. This is because of the formula

$$f(\lambda x_0,\ldots, \lambda x_n)=\lambda^{\deg f} f(x_0,\ldots, x_n),\qquad \lambda\neq 0$$

In other words, to describe $$\mathbb{P}^n$$ in a manner similar to the spectrum, we should not view $$\mathbb{A}^{n+1}$$ simply as the spectrum of the ring $$\mathbb{K}[\x_0,\ldots, \x_n]$$, but add degree information to regard it as a *graded* ring, and look at the zero loci of *homogeneous* elements rather than arbitrary elements. Then, recalling [[Algebraic Structures] §Graded Rings, ⁋Proposition 6](/en/math/algebraic_structures/graded_rings#prop6), our interest should also be in *homogeneous* ideals.

In the remainder of this post we follow the process of taking $$\Proj$$ of a graded ring to obtain a projective scheme. To this end we fix some notation.

<div class="remark" markdown="1">

Unless stated otherwise, a graded ring is always assumed to be $$\mathbb{N}_{\geq0}$$-graded. That is, the ring of interest is always of the form

$$A_\bullet=\bigoplus_{i=0}^\infty A_i=A_0\oplus A_1\oplus\cdots$$

Here, since $$A_0$$ is itself a ring, $$A_\bullet$$ can be regarded as a graded $$A_0$$-algebra, and for this reason we call $$A_0$$ the *base ring*. Also, when we occasionally forget the grading structure on $$A_\bullet$$ and regard it as an ordinary ring, we shall simply write $$A$$.

</div>

Let a graded ring $$A_\bullet$$ be given. Then the subset

$$A_+=\bigoplus_{i=1}^\infty A_i=A_1\oplus A_2\oplus\cdots$$

is trivially a homogeneous ideal of $$A_\bullet$$. However, if we consider the case $$A_\bullet=\mathbb{K}[\x_0,\ldots, \x_n]$$, the point at which the function values of all elements of $$A_+$$ vanish, that is, the point that is identically zero for all polynomials, is only the origin. Since the origin is the point omitted in constructing $$\mathbb{P}^n$$, it is appropriate to exclude from our discussion any ideal containing the ideal $$A_+$$. From this viewpoint we call $$A_+$$ the *irrelevant ideal*.

Now, as a set, $$\Proj A_\bullet$$ is defined as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a graded ring $$A_\bullet$$, $$\Proj A_\bullet$$ is the set

$$\Proj A_\bullet =\{\mathfrak{p}\in \Spec A\mid\text{$\mathfrak{p}$ is homogeneous and $A_+\not\subset \mathfrak{p}$}\}$$

</div>

By definition $$\Proj A_\bullet$$ is a subset of $$\Spec A$$. That is, the points of $$\Proj A_\bullet$$ are also points of $$\Spec A$$. This would be somewhat awkward if we had used $$\mSpec A$$ instead of $$\Spec A$$, but $$\Spec A$$ contains points corresponding to prime ideals in addition to traditional points. For example, considering the ideal $$(\x_1-\x_2)$$ of $$A=\mathbb{K}[\x_1,\x_2]$$, we have $$\mathbb{K}[\x_1,\x_2]/(\x_1-\x_2)\cong \mathbb{K}[\x_1]$$, so this ideal is a prime ideal. Moreover, when we regard $$\mathbb{K}[\x_1,\x_2]$$ as a graded ring $$A_\bullet$$, this ideal is a homogeneous prime ideal not containing $$A_+$$, so it is also a point of $$\Proj A_\bullet$$.

So far $$\Proj A_\bullet$$ is only a set. To give it a topological structure we must use the zero locus of functions, and as observed above, we must use the zero locus of *homogeneous* polynomials.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let a graded ring $$A_\bullet$$ be given. For a homogeneous ideal $$\mathfrak{a}$$ of $$A_\bullet$$, define

$$Z_+(\mathfrak{a})=\{\mathfrak{p}\in\Proj A_\bullet\mid \mathfrak{a}\subseteq \mathfrak{p}\}$$

</div>

Then, using the third result of [[Commutative Algebra] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2), we can prove the following lemma, similar to [§Spectra, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6) and [§Spectra, ⁋Proposition 5](/en/math/scheme_theory/spectrums#prop5).

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> For a graded ring $$A_\bullet$$, the following hold.

1. For any homogeneous ideals $$\mathfrak{a},\mathfrak{b}$$, we have $$Z_+(\mathfrak{a}\mathfrak{b})=Z_+(\mathfrak{a})\cup Z_+(\mathfrak{b})$$.
2. For any family $$\{\mathfrak{a}_i\}$$ of homogeneous ideals, we have $$Z_+(\sum \mathfrak{a}_i)=\bigcap Z_+(\mathfrak{a}_i)$$.
3. For any homogeneous ideal $$\mathfrak{a}$$, we have $$Z_+(\sqrt{\mathfrak{a}})=Z_+(\mathfrak{a})$$.
4. For any homogeneous ideal $$\mathfrak{a}$$, we have $$Z_+(\mathfrak{a})=Z_+(\mathfrak{a}\cap A_+)$$.

</div>

Of course, it is obvious that $$\mathfrak{a}\mathfrak{b}$$, $$\sqrt{\mathfrak{a}}$$, and $$\sum \mathfrak{a}_i$$ appearing in the above lemma are homogeneous. The first through third results are already observed in the case of spectra; only the fourth is new.

<details class="proof--alone" markdown="1">
<summary>Proof of Lemma 3</summary>

1. It is obvious that a homogeneous prime ideal $$\mathfrak{p}$$ containing $$\mathfrak{a}$$ or $$\mathfrak{b}$$ also contains the smaller homogeneous ideal $$\mathfrak{ab}$$, so it suffices to show the reverse inclusion. Assume $$\mathfrak{p}\supset \mathfrak{ab}$$. If $$\mathfrak{p}\not\supseteq \mathfrak{b}$$, then we can find an element $$b\in\mathfrak{b}$$ with $$b\not\in \mathfrak{p}$$. Since $$\mathfrak{b}$$ is homogeneous, we can decompose it into a sum of homogeneous elements

$$b=b_1+\cdots b_n,\qquad \text{$b_i\in \mathfrak{b}$ homogeneous}$$

Meanwhile, for any homogeneous element $$a\in \mathfrak{a}$$, we have $$ab\in \mathfrak{ab}\subseteq \mathfrak{p}$$. Consider the element

$$ab=ab_1+\cdots+ab_n$$

of $$\mathfrak{ab}\subseteq \mathfrak{p}$$; since $$\mathfrak{p}$$ is homogeneous, all the $$ab_i$$ are elements of $$\mathfrak{p}$$. On the other hand, by the previous assumption $$b\not\in \mathfrak{p}$$, so there exists an $$i$$ satisfying $$b_i\not\in \mathfrak{p}$$, and then $$ab_i$$ is a homogeneous element belonging to $$\mathfrak{p}$$ with $$b_i\not\in \mathfrak{p}$$, so by [[Commutative Algebra] §Localization of Graded Rings, ⁋Lemma 2](/en/math/commutative_algebra/localization_of_graded_rings#lem2) we have $$a\in \mathfrak{p}$$. Therefore $$\mathfrak{a}\subseteq \mathfrak{p}$$.
2. This is obvious because $$\sum \mathfrak{a}_i$$ is defined as the smallest ideal containing all the ideals $$\mathfrak{a}_i$$.
3. [[Commutative Algebra] §Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8).
4. By definition $$Z_+(\mathfrak{a})\subseteq Z_+(\mathfrak{a}\cap A_+)$$ is obvious, so it suffices to show the reverse direction. That is, suppose $$\mathfrak{p}$$ is a prime ideal containing all homogeneous elements of $$\mathfrak{a}$$ of positive degree but not containing $$A_+$$ as a whole; let us show that $$\mathfrak{a}\subseteq \mathfrak{p}$$. To do this, it suffices to show that for any $$a\in \mathfrak{a}\cap A_0$$, the above assumption implies that $$a$$ also belongs to $$\mathfrak{p}$$. 

Now, since $$A_+\not\subset\mathfrak{p}$$, there exists a homogeneous element $$f$$ not belonging to $$\mathfrak{p}$$. Then $$af\in \mathfrak{a}\cap A_+\subseteq \mathfrak{p}$$, and since $$f\not\in \mathfrak{p}$$, we have $$a\in \mathfrak{p}$$.

</details>

From the results of this lemma, the first and second results allow us to define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a graded ring $$A_\bullet$$ be given. The unique topology on $$\Proj A_\bullet$$ having the sets of the form $$Z_+(\mathfrak{a})$$ as closed sets is called the *Zariski topology*.

</div>

Also, by the fourth result of this lemma, we know that in defining $$\Proj A_\bullet$$ it suffices to consider only homogeneous ideals contained in $$A_+$$. This is intuitively obvious: if we set $$A=\mathbb{K}[\x_0,\ldots, \x_n]$$, the elements in $$A_0$$ are constant functions anyway.

Now we define the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For any homogeneous element $$f$$ of a graded ring $$A_\bullet$$, we write $$D_+(f)$$ for the complement of $$Z_+(f)$$ in $$\Proj A_\bullet$$.

</div>

The following corollary follows immediately from the first result of [Lemma 3](#lem3).

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> We have $$D_+(f)\cap D_+(g)=D_+(fg)$$.

</div>

Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> The collection of $$D_+(f)$$ forms a base for $$\Proj A_\bullet$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Writing an arbitrary homogeneous ideal $$\mathfrak{a}$$ of $$A$$ using homogeneous generators as $$\mathfrak{a}=\sum_{i\in I} (f_i)$$,

$$Z_+(\mathfrak{a})=\bigcap_{i\in I} Z_+((f_i))$$

and therefore

$$D_+(\mathfrak{a})=\bigcup_{i\in I} D_+(f_i)$$

</details>

Meanwhile, we have seen that in the spectrum $$\Spec A$$ of a ring $$A$$, for any element $$f\in A$$, the set $$D(f)$$ is isomorphic (as a scheme) to $$\Spec A_f$$. A similar result holds for $$D_+(f)$$.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> For a graded ring $$A_\bullet$$ and any homogeneous element $$f\in A_\bullet$$, define a function $$D_+(f) \rightarrow \Spec A_{(f)}$$ by the formula

$$\mathfrak{p}\mapsto \mathfrak{p}A_f\cap A_{(f)}$$

then this function is a homeomorphism. ([[Commutative Algebra] §Localization of Graded Rings, ⁋Definition 5](/en/math/commutative_algebra/localization_of_graded_rings#def5))

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since $$f\not\in \mathfrak{p}$$, via the localization $$A \rightarrow A_f$$, $$\mathfrak{p}$$ is carried to the prime ideal $$\mathfrak{p}A_f$$ of $$A_f$$. ([[Commutative Algebra] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)) Now the right-hand side of the claim is the preimage of $$\mathfrak{p}A_f$$ under the inclusion $$i: A_{(f)} \rightarrow A_f$$, so it becomes a prime ideal of $$A_{(f)}$$.

Now let us define the inverse function $$\Spec A_{(f)} \rightarrow D_+(f)$$ of this correspondence. Given an arbitrary prime ideal $$\mathfrak{q}\in\Spec A_{(f)}$$, consider the homogeneous ideal $$\mathfrak{p}$$ of $$A$$ generated by those homogeneous elements $$x$$ of $$A$$ satisfying the condition

$$\frac{x^{\deg f}}{f^{\deg x}}\in \mathfrak{q}$$

Then for any homogeneous elements $$x,y\in \mathfrak{p}$$,

$$xy\in \mathfrak{p}\iff \frac{x^{\deg f}}{f^{\deg x}}\frac{y^{\deg f}}{f^{\deg y}}\in \mathfrak{q}$$

so from the fact that $$\mathfrak{q}$$ is a prime ideal, we know that $$\mathfrak{p}$$ is a prime ideal. Now one can easily check that the correspondences $$\mathfrak{p}\mapsto \mathfrak{p}A_f\cap A_{(f)}$$ and $$\mathfrak{q}\mapsto \mathfrak{p}$$ are inverse to each other, and for any homogeneous ideal $$\mathfrak{a}$$ of $$A_\bullet$$, the closed set $$Z_+(\mathfrak{a})\cap D_+(f)$$ of $$D_+(f)$$ is carried by this function to the closed set $$Z(\mathfrak{a}A_f\cap A_{(f)})$$ of $$\Spec A_{(f)}$$, so we see that this is a homeomorphism.

</details>

Then the way to give a scheme structure to $$\Proj A_\bullet$$ is now obvious. The proof of the following lemma is almost identical to [Lemma 8](#lem8).

<div class="proposition" markdown="1">

<ins id="lem9">**Lemma 9**</ins> For a graded ring $$A_\bullet$$ and nonzero homogeneous elements $$f,g$$, there exists an isomorphism

$$\Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})\subseteq \Spec A_{(f)}$$

</div>

Therefore, there exists an isomorphism between the principal open set $$D(f^{\deg g}/g^{\deg f})\subseteq \Spec A_{(f)}$$ of $$\Spec A_{(g)}$$ and the principal open set $$\Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})$$ of $$\Spec A_{(f)}$$. Now the following theorem is a simple computation.

<div class="proposition" markdown="1">

<ins id="thm10">**Theorem 10**</ins> The $$\Spec A_{(f)}$$ defined above, the open subschemes $$D(g^{\deg f}/f^{\deg g})$$, and the isomorphisms

$$D(f^{\deg g}/g^{\deg f})\cong \Spec A_{(fg)}\cong D(g^{\deg f}/f^{\deg g})$$

all satisfy the conditions of [§Schemes, ⁋Lemma 9](/en/math/scheme_theory/schemes#lem9), and therefore give a unique scheme structure on $$\Proj A_\bullet$$.

</div>

In particular, since $$\Proj A_\bullet$$ is a locally ringed space, for any $$\mathfrak{p}\in \Proj A_\bullet$$ the stalk $$\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}$$ is a local ring. But anyway, since $$\mathfrak{p}$$ can be placed in a suitable affine open neighborhood, the following can be shown by essentially the same procedure as [§Affine Schemes, ⁋Lemma 8](/en/math/scheme_theory/affine_schemes#lem8).

<div class="proposition" markdown="1">

<ins id="lem11">**Lemma 11**</ins> For a graded ring $$A_\bullet$$ and any $$\mathfrak{p}\in \Proj A_\bullet$$, there exists an isomorphism

$$\mathcal{O}_{\Proj A_\bullet,\mathfrak{p}}\cong A_{(\mathfrak{p})}$$

</div>

One slightly tricky point is that, unlike $$\Spec$$, $$\Proj$$ does not define a functor from $$\bgr_{\mathbb{N}_{\geq 0}}\cRing^\op$$ to $$\LRS$$. This is because even if a graded ring homomorphism $$\phi_\bullet:A_\bullet \rightarrow B_\bullet$$ and an arbitrary homogeneous ideal $$\mathfrak{q}$$ of $$B$$ do not contain $$B_+$$, their inverse image $$\phi^{-1}(\mathfrak{q})$$ may contain $$A_+$$.

Finally, we translate the projective space we examined at the very beginning for motivation into the language of algebraic geometry (almost) completely.

<div class="example" markdown="1">

<ins id="ex12">**Example 12**</ins> In algebraic geometry, $$\mathbb{P}^n_\mathbb{K}$$ is defined by the formula

$$\mathbb{P}^n_\mathbb{K}=\Proj \mathbb{K}[\x_0,\ldots, \x_n]$$

Here the polynomial algebra $$\mathbb{K}[\x_0,\ldots, \x_n]$$ is of course a graded ring with the grading given by degree.

Then the $$n+1$$ open cover of projective space can be thought of in this language as

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_{0},\ldots, \x_{n}]_{(\x_{i})}$$

by [[Commutative Algebra] §Localization of Graded Rings, ⁋Proposition 6](/en/math/commutative_algebra/localization_of_graded_rings#prop6)

$$\mathbb{K}[\x_{0},\ldots, \x_{n}]_{(\x_{i})}\cong \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)$$

explicitly this isomorphism is obtained by applying the first isomorphism theorem to the ring homomorphism

$$\mathbb{K}[\x_{0/i}, \ldots, \x_{n/i}]\rightarrow \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)};\qquad \x_{k/i}\mapsto \frac{\x_k}{\x_i}$$

Now any $$\mathfrak{p}\in \mathbb{P}^n_\mathbb{K}$$ is contained in some $$D_+(\x_i)$$. Suppose that via the above isomorphism the point $$\mathfrak{p}$$ of $$D_+(\x_i)$$ is carried to a point $$\mathfrak{q}$$ of $$U_i=\Spec \mathbb{K}[\x_{0/i}, \ldots, \x_{n/i}]/(\x_{i/i}-1)$$. Then in this case we naturally expect the isomorphism

$$\mathcal{O}_{\mathbb{P}^n_\mathbb{K},\mathfrak{p}}\cong \mathcal{O}_{U_i, \mathfrak{q}}$$

And of course this holds. ([[Commutative Algebra] §Localization of Graded Rings, ⁋Proposition 8](/en/math/commutative_algebra/localization_of_graded_rings#prop8))

</div>

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---
