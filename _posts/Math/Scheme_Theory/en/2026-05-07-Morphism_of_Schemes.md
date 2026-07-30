---
title: "Morphisms of Schemes"
description: "A morphism of schemes is defined as a continuous map together with a morphism of structure sheaves, and morphisms between affine schemes correspond to ring homomorphisms. A general scheme morphism can be understood by gluing local morphisms over an affine open cover."
excerpt: "Four perspectives on scheme morphisms as locally ringed space morphisms"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/morphism_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-19
weight: 8
translated_at: 2026-07-27T00:45:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-27T00:45:02+00:00
---
By definition, $\Sch$ is a full subcategory of $\LRS$. ([§Schemes, ⁋Definition 1](/en/math/scheme_theory/schemes#def1)) That is, given two schemes $X,Y$, a scheme morphism from $X$ to $Y$ is given by a continuous map $\varphi: X \rightarrow Y$ and a morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ of structure sheaves, where $\varphi^\sharp$ must become a local homomorphism upon restriction to each stalk. ([§Affine Scheme, ⁋Definition 2](/en/math/scheme_theory/affine_schemes#def2))

Thus a scheme morphism $f:X \rightarrow Y$ is fundamentally an object we have already defined. In the next post we will examine properties of scheme morphisms; before that, we present four ways to understand them.

## Gluing Ring Homomorphisms

The first perspective is quite natural. A scheme is essentially built by gluing affine schemes, and by the categorical equivalence $\AffSch\cong\cRing^\op$, a morphism between affine schemes is essentially a ring homomorphism. Therefore a scheme morphism should also be understood as gluing morphisms between affine schemes. That is, the following proposition is to be expected.

::: Proposition 1
Let a scheme morphism $\varphi: X \rightarrow Y$ be given. If an affine open subset $U\cong\Spec A$ of $X$ and an affine open subset $V\cong\Spec B$ of $Y$ satisfy $\varphi(U)\subseteq V$, then the map

$$(\varphi\vert_U)\vert^V: U \rightarrow V$$

obtained by restricting the domain of $\varphi$ to $U$ and viewing the codomain as $V$ is a morphism between affine schemes, i.e. a ring homomorphism $B \rightarrow A$.

Conversely, let an affine open covering $\{U_i\}$ of $X$ be given, and suppose for each $i$ we are given an affine open subset $V_i$ of $Y$ and a morphism $\varphi_i: U_i \rightarrow V_i$ between affine schemes. If these satisfy the gluing condition

$$\varphi_i\vert_{U_i\cap U_k}=\varphi_k\vert_{U_i\cap U_k}\qquad\text{(as morphisms $U_i\cap U_k \rightarrow Y$)}$$

for all $i,k$, then the $\varphi_i$ glue to a unique scheme morphism $\varphi: X \rightarrow Y$.
:::
::: Proof
For the first claim, for any open subset $W\subseteq V$, the maps

$$\mathcal{O}_Y(W) \rightarrow \varphi_\ast \mathcal{O}_X(W)=\mathcal{O}_X(\varphi^{-1}(W)) \rightarrow \mathcal{O}_X(\varphi^{-1}(W)\cap U)$$

obtained by composing $\varphi^\sharp(W):\mathcal{O}_Y(W)\rightarrow\varphi_\ast \mathcal{O}_X(W)$ with the restriction to $U$ define the sheaf morphism $\mathcal{O}_Y\vert_V \rightarrow ((\varphi\vert_U)\vert^V)_\ast(\mathcal{O}_X\vert_U)$ that we must examine. The map this induces on the stalk at any $x\in U$ is determined by germs alone, so it coincides with $\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ induced by the original $\varphi$, and hence is a local homomorphism. Thus $(\varphi\vert_U)\vert^V$ is a morphism of $\LRS$, and since $U$ and $V$ are affine schemes, by [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11) it is induced from a unique ring homomorphism $B \rightarrow A$.

For the second claim, by the gluing condition the continuous maps $\varphi_i: U_i \rightarrow V_i\hookrightarrow Y$ agree on overlaps, so by [[Topology] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1) they glue to a continuous map $\varphi: X \rightarrow Y$. We now define the sheaf morphism $\varphi^\sharp$. Given an open subset $W\subseteq Y$ and $s\in \mathcal{O}_Y(W)$, consider the sections

$$s_i:=\varphi_i^\sharp(W)(s)\in \mathcal{O}_X(\varphi^{-1}(W)\cap U_i).$$

These also agree on overlaps for the same reason, and since $\{\varphi^{-1}(W)\cap U_i\}$ is an open covering of $\varphi^{-1}(W)$, the two conditions of [[Topology] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1) yield a unique glued section $s'\in \mathcal{O}_X(\varphi^{-1}(W))$. Defining $\varphi^\sharp(W): s\mapsto s'$, compatibility with restriction maps can be checked on each $U_i$, and the map induced by $\varphi^\sharp$ on the stalk at $x\in U_i$ coincides with that induced by $\varphi_i^\sharp$, so it is a local homomorphism. Hence $\varphi$ is a scheme morphism, and since the condition $(\varphi\vert_{U_i})\vert^{V_i}=\varphi_i$ completely determines $\varphi$, such a morphism is unique.
:::

The first claim is nothing more than applying the fact from [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11) that $\AffSch$ is a full subcategory of $\LRS$ to the local picture of a scheme morphism. However, one must be careful: the gluing condition in the second claim is not expressed as a condition between ring homomorphisms. When $V_i\neq V_k$, we cannot compare $\varphi_i$ and $\varphi_k$ within a single affine scheme, so we must compare them inside $Y$; moreover $U_i\cap U_k$ is generally not an affine scheme. Thus the data given for gluing scheme morphisms are ring homomorphisms, but the condition determining whether they glue is not.

::: Example 2
As an example of a scheme morphism that is not a morphism between affine schemes, for $n\geq 1$ consider the map

$$\varphi:\mathbb{A}_\mathbb{K}^{n+1}\setminus \{0\} \rightarrow \mathbb{P}^n_\mathbb{K}$$

that first appeared for motivation in [§Projective Schemes, §§Projective Space](/en/math/scheme_theory/projective_schemes#projective-space). This formula was traditionally used to construct projective space, but it did not appear in [§Projective Schemes, ⁋Example 12](/en/math/scheme_theory/projective_schemes#ex12) when the traditional projective space was translated into the language of schemes. This morphism of course satisfies the formula

$$(x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n],$$

but the points of $\mathbb{A}^{n+1}_\mathbb{K}$ are not merely of this form, and moreover this formula encodes no information about the structure sheaf, so it would be inappropriate to call it a scheme morphism.

To define $\varphi$ as a scheme morphism, consider the affine open subscheme of $\mathbb{P}^n_{\mathbb{K}}$

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)}\cong \Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1).$$

([§Projective Schemes, ⁋Example 12](/en/math/scheme_theory/projective_schemes#ex12)) Also consider the affine space

$$\mathbb{A}^{n+1}_\mathbb{K}=\Spec \mathbb{K}[\x_0,\ldots, \x_n].$$

Then

$$\mathbb{A}^{n+1}_\mathbb{K}\setminus \{0\}=\bigcup_{i=0}^n D(\x_i)$$

and $D(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{\x_i}$. Now for each $i$, since $\varphi_i: D(\x_i) \rightarrow D_+(\x_i)$ is a morphism between affine schemes, it is the same as a ring homomorphism. Then the formula

$$\phi_i:\mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]\rightarrow\mathbb{K}[\x_0,\ldots, \x_n]_{\x_i};\qquad \x_{k/i}\mapsto  \frac{\x_k}{\x_i}$$

defines, by the first isomorphism theorem, a morphism $\varphi_i$ between affine schemes that gives the desired morphism. That these satisfy the conditions of [Proposition 1](#prop1) can also be checked by a brief computation. Now borrowing the notation from [§Projective Schemes, §§Projective Space](/en/math/scheme_theory/projective_schemes#projective-space) again, on each $D(\x_i)$ these are given by the formula

$$(x_0,\ldots, x_n) \rightarrow \left[\frac{x_0}{x_i}:\cdots:\frac{x_{i-1}}{x_i}:1:\frac{x_{i+1}}{x_i}:\cdots:\frac{x_n}{x_i} \right],$$

so it is appropriate to denote this as

$$(x_0,\ldots, x_n)\rightarrow [x_0:\cdots:x_n].$$
:::

We shall essentially take this perspective as the definition; the three perspectives to be introduced in the remainder are closer to ways of interpreting it.

## Schemes over a Scheme

First we define the following.

::: Definition 3
For an arbitrary scheme $S$, we call the slice category $\Sch_{/S}$ over $S$ the category of *$S$-schemes*. ([[Category Theory] §Categories, ⁋Example 13](/en/math/category_theory/categories#ex13))
:::

That is, an $S$-scheme is simply another name for a scheme morphism $X \rightarrow S$, also called the *structure morphism*. This becomes slightly more intuitive upon examining the following example.

::: Example 4
Consider the affine $n$-space $\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$. Then $\mathbb{K}[\x_1,\ldots, \x_n]$ is a $\mathbb{K}$-algebra, which is to say that a $\mathbb{K}$-algebra structure is given via the structure morphism

$$\mathbb{K}\hookrightarrow \mathbb{K}[\x_1,\ldots, \x_n].$$

([[Algebraic Structures] §Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1) and the argument following it)

Then via this structure morphism we may regard $\mathbb{A}^n_\mathbb{K}$ as a $\Spec\mathbb{K}$-scheme

$$\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \Spec \mathbb{K}.$$
:::

As above, when $S$ is an affine scheme $S=\Spec A$, it is common to call an $S$-scheme an $A$-scheme by a slight abuse of language. Then by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), fixing an arbitrary ring $A$ and giving a scheme $X$ an $A$-scheme structure is precisely the same as

$$\Hom_\Sch(X, \Spec A)=\Hom_\LRS(X, \Spec A)\cong \Hom_\cRing(A, \Gamma(X, \mathcal{O}_X)).$$

That is, giving an $A$-scheme structure to a scheme $X$ is algebraically equivalent to giving an $A$-algebra structure to $\Gamma(X, \mathcal{O}_X)$. In particular, when $A=\mathbb{Z}$, since $\mathbb{Z}$ is the initial object of $\cRing$, every scheme can be regarded as a $\mathbb{Z}$-scheme in a unique way.

Now let us see the following example, which generalizes [Example 2](#ex2) further.

::: Example 5
Consider a ring $A$ and an $A$-scheme $X$, and suppose functions $f_0,\ldots, f_n\in \Gamma(X, \mathcal{O}_X)$ defined on $X$ are given. Assume that these generate the unit ideal, i.e. $(f_0,\ldots, f_n)=\mathcal{O}_X$. Also consider an affine open covering $X=\bigcup U_j$ of $X$. Then

$$U_{ij}:=D(f_i)\cap U_j=D(f_i\vert_{U_j})\subseteq U_j$$

is an affine open covering of $X$. On the other hand, consider the projective space over $A$

$$\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$$

and its open covering $D_+(\x_i)$. Now given a pair $i,j$, define the function $\varphi_{ij}: U_{ij} \rightarrow D_+(\x_i)$ via the ring homomorphism

$$A[\x_0,\ldots, \x_n]_{(\x_i)}\rightarrow \Gamma(U_{ij});\qquad \x_{k/i}\mapsto \frac{f_k\vert_{U_{ij}}}{f_i\vert_{U_{ij}}}.$$

Then by definition it is obvious that this morphism satisfies the gluing condition of [Proposition 1](#prop1), and hence these define a scheme morphism

$$X \rightarrow \mathbb{P}^n_A.$$

Explicitly, this scheme morphism is given, in the same manner as [Example 2](#ex2), by

$$x\mapsto [f_0(x):\cdots: f_n(x)].$$
:::

## Points

We also define the following.

::: Definition 6
We call a scheme morphism $f: X \rightarrow Y$ an *$X$-point* of $Y$.
:::

Similarly, examining the case where $X$ is an affine scheme is intuitively helpful.

::: Example 7
Consider a field $\mathbb{K}$ and the affine $n$-space $Y=\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$ defined over it. As we saw in [Example 4](#ex4), $Y$ is a $\Spec\mathbb{K}$-scheme. According to [Definition 6](#def6), a $\mathbb{K}$-point of $Y$ is an arbitrary scheme morphism $\Spec\mathbb{K}\rightarrow Y$; but since $Y$ is a $\Spec\mathbb{K}$-scheme, among these we are interested in sections of the structure morphism $Y\rightarrow\Spec\mathbb{K}$, that is, morphisms $X=\Spec\mathbb{K}\rightarrow Y$ over $\Spec\mathbb{K}$. This is a $\mathbb{K}$-morphism between affine schemes

$$\Spec \mathbb{K} \rightarrow \Spec \mathbb{K}[\x_1,\ldots, \x_n]$$

and hence corresponds to a $\mathbb{K}$-algebra homomorphism

$$\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}.$$

Now $\mathbb{K}[\x_1,\ldots, \x_n]$ is a polynomial algebra over $\mathbb{K}$, so by the universal property of [[Algebraic Structures] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8) such a $\phi$ is uniquely determined by the images $x_i=\phi(\x_i)\in \mathbb{K}$ of each variable, and conversely any $x=(x_1,\ldots, x_n)\in \mathbb{K}^n$ yields the evaluation homomorphism $\ev_x$. That is, $\phi=\ev_x$, and in particular

$$\ker\phi=(\x_1-x_1,\ldots, \x_n-x_n)$$

since the quotient by the right-hand side is already $\mathbb{K}$. Thus the following two mutually inverse bijections exist:

$$\begin{aligned}\{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}&\rightarrow \{\text{points $(x_1,\ldots, x_n)\in \mathbb{K}^n$}\}\\\Spec\phi&\mapsto (\phi(\x_1),\ldots,\phi(\x_n))\end{aligned}$$

and

$$\begin{aligned}\{\text{points $(x_1,\ldots, x_n)\in \mathbb{K}^n$}\}&\rightarrow \{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}\\a=(a_1,\ldots, a_n)&\mapsto \Spec \ev_a\end{aligned}$$
:::

As above, if $X$ is of the form $\Spec A$, we simply call this an $A$-point. The usefulness of this concept can also be seen in the following example.

::: Example 8
Consider the $\mathbb{Z}$-scheme $X=\Spec\mathbb{Z}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$ defined by integer-coefficient polynomials $f_1,\ldots, f_r\in\mathbb{Z}[\x_1,\ldots, \x_n]$. Then by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), a $\mathbb{Q}$-point $\Spec\phi: \Spec \mathbb{Q}\rightarrow X$ of $X$ corresponds to a ring homomorphism $\phi:\mathbb{Z}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)\rightarrow\mathbb{Q}$, and since $\phi$ is canonically given over $\mathbb{Z}$, this is again in bijection with the rational solutions $(x_1,\ldots, x_n)\in\mathbb{Q}^n$ of

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0.$$

Similarly, integer solutions of the above equation correspond exactly to $\mathbb{Z}$-points of $X$.
:::

Based on this perspective we define the following.

::: Definition 9
We call the functor $\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$ the *functor of points of $X$*.
:::

Then $\Hom_\Sch(-,X)$ is the functor that takes a scheme $S$ and returns the set of $S$-valued points of $X$.

## Families of Schemes

The final perspective cannot yet be defined rigorously because our language is insufficient, so we shall only explain the geometric intuition. We call a scheme morphism $f:X \rightarrow S$ a *family parametrized by $S$*, or simply an $S$-family. Thus by definition $\Sch_{/S}$ can be regarded as the category of families parametrized by $S$.

For geometric intuition, one should basically think of the following (non-scheme) situation.

::: Example 10
Consider the sphere $S:x^2+y^2+z^2=1$ defined in coordinate space $\mathbb{R}^3$, and the projection $\pi: S \rightarrow \mathbb{R}_x$ onto the $x$-axis. Then for any $x_0\in \mathbb{R}_x$,

$$\pi^{-1}(x_0)=\{(x_0,y,z)\in \mathbb{R}^3\mid y^2+z^2=1-x_0^2\}.$$

Geometrically, this can be viewed as a situation in which, for each $x_0\in \mathbb{R}_x$, a circle $y^2+z^2=1-x_0^2$ is assigned; hence we may regard $\pi$ as a <em>family of circles parametrized by the $x$-axis</em>. Of course if $\lvert x_0\rvert>1$ this fiber is empty, and if $x_0=\pm 1$ it is a single point, so it is a circle only when $\lvert x_0\rvert<1$. The manner in which members of a family degenerate in this way will become an issue again when we treat flatness later.
:::

Among the reasons we cannot directly represent this example as a scheme, the less essential one is that $S$ is a closed subset of $\mathbb{R}^3$ and we do not yet know how to endow a closed subset with a scheme structure. This will be resolved in [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes). The more subtle and essential difficulty is that there is no way to represent the fiber $\pi^{-1}(x_0)$ of the function $\pi$ at a point $x_0$. A scheme morphism is of course a continuous map, so we could view this as the fiber of a continuous map; but even doing so (even assuming the content of [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes)) there is no way to give $\pi^{-1}(x_0)$ a scheme structure. To explain this we must wait a little longer.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
