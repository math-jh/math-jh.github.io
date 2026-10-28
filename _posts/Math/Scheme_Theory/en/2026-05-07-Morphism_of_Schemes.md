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
last_polished_at: 2026-10-28T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
By definition, $\Sch$ is a full subcategory of $\LRS$. ([§Schemes, ⁋Definition 1](/en/math/scheme_theory/schemes#def1){: data-lid="9q0g3" }) That is, given two schemes $X,Y$, a scheme morphism from $X$ to $Y$ is given by a continuous map $\varphi: X \rightarrow Y$ and a morphism $\varphi^\sharp: \mathcal{O}_Y \rightarrow \varphi_\ast \mathcal{O}_X$ of structure sheaves, where $\varphi^\sharp$ must be a local homomorphism when restricted to each stalk. ([§Affine Scheme, ⁋Definition 2](/en/math/scheme_theory/affine_schemes#def2){: data-lid="plezh" })

Thus, a scheme morphism $\varphi:X \rightarrow Y$ is fundamentally an object we have already defined. In the next post, we will examine properties of scheme morphisms; before that, we present four ways to understand scheme morphisms.

## Gluing of Ring Homomorphisms

The first perspective is quite natural. A scheme is essentially built by gluing affine schemes, and by the categorical equivalence $\AffSch\cong\cRing^\op$, a morphism between affine schemes is essentially a ring homomorphism. Therefore, a scheme morphism should also be understood as being formed by gluing morphisms between affine schemes. That is, it is reasonable to expect the following proposition.

::: Proposition 1
Let a scheme morphism $\varphi: X \rightarrow Y$ be given. If an affine open subset $U\cong\Spec A$ of $X$ and an affine open subset $V\cong\Spec B$ of $Y$ satisfy $\varphi(U)\subseteq V$, then

$$(\varphi\vert_U)\vert^V: U \rightarrow V$$

obtained by restricting the domain of $\varphi$ to $U$ and viewing the codomain as $V$ is a morphism between affine schemes, that is, a ring homomorphism $B \rightarrow A$.

Conversely, let an affine open covering $\{U_i\}$ of $X$ be given, and suppose that for each $i$, an affine open subset $V_i$ of $Y$ and a morphism $\varphi_i: U_i \rightarrow V_i$ between affine schemes are given. If these satisfy the gluing condition

$$\varphi_i\vert_{U_i\cap U_k}=\varphi_k\vert_{U_i\cap U_k}\qquad\text{(as morphisms $U_i\cap U_k \rightarrow Y$)}$$

for all $i,k$, then the $\varphi_i$ glue to a unique scheme morphism $\varphi: X \rightarrow Y$.
:::
::: Proof
For the first claim, for any open subset $W\subseteq V$, the maps

$$\mathcal{O}_Y(W) \rightarrow \varphi_\ast \mathcal{O}_X(W)=\mathcal{O}_X(\varphi^{-1}(W)) \rightarrow \mathcal{O}_X(\varphi^{-1}(W)\cap U)$$

obtained by composing $\varphi^\sharp(W):\mathcal{O}_Y(W)\rightarrow\varphi_\ast \mathcal{O}_X(W)$ with the restriction map to $U$ define the sheaf morphism $\mathcal{O}_Y\vert_V \rightarrow ((\varphi\vert_U)\vert^V)_\ast(\mathcal{O}_X\vert_U)$ that we must examine. The map this induces on the stalk at any $x\in U$ is determined by germs alone, so it coincides with the map $\mathcal{O}_{Y,\varphi(x)} \rightarrow \mathcal{O}_{X,x}$ induced by the original $\varphi$, and hence is a local homomorphism. Thus $(\varphi\vert_U)\vert^V$ is a morphism of $\LRS$, and since $U$ and $V$ are affine schemes, by [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11){: data-lid="tcnxb" } it is induced from a unique ring homomorphism $B \rightarrow A$.

For the second claim, by the gluing condition the continuous maps $\varphi_i: U_i \rightarrow V_i\hookrightarrow Y$ agree on overlaps, so by [\[Topology\] §Presheaves, ⁋Lemma 1](/en/math/topology/presheaves#lem1){: data-lid="as1eh" } they glue to a continuous map $\varphi: X \rightarrow Y$. We now must define the sheaf morphism $\varphi^\sharp$. Consider the sections

$$s_i:=\varphi_i^\sharp(W\cap V_i)(s\vert_{W\cap V_i})\in \mathcal{O}_X(\varphi^{-1}(W)\cap U_i)$$

obtained whenever an open subset $W\subseteq Y$ and $s\in \mathcal{O}_Y(W)$ are given. Then these also agree on overlaps for the same reason, and since $\{\varphi^{-1}(W)\cap U_i\}$ is an open covering of $\varphi^{-1}(W)$, by the two conditions of [\[Topology\] §Sheaves, ⁋Definition 1](/en/math/topology/sheaves#def1){: data-lid="lyupd" } there exists a unique glued section $s'\in \mathcal{O}_X(\varphi^{-1}(W))$. Now if we define $\varphi^\sharp(W): s\mapsto s'$, it suffices to check compatibility with restriction maps on each $U_i$, and since the map induced by $\varphi^\sharp$ on the stalk at $x\in U_i$ is equal to that induced by $\varphi_i^\sharp$, it is a local homomorphism. Therefore $\varphi$ is a scheme morphism, and since the condition $(\varphi\vert_{U_i})\vert^{V_i}=\varphi_i$ completely determines $\varphi$, such $\varphi$ is unique.
:::

The first claim is nothing more than applying the fact from [§Affine Scheme, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11){: data-lid="safzr" } that $\AffSch$ is a full subcategory of $\LRS$ directly to the local picture of a scheme morphism. However, one should note that the gluing condition in the second claim is not written as a condition between ring homomorphisms. This is because when $V_i\neq V_k$, we cannot compare $\varphi_i$ and $\varphi_k$ within a single affine scheme and must compare them inside $Y$, and moreover $U_i\cap U_k$ is generally not an affine scheme. That is, while the data given to glue scheme morphisms are ring homomorphisms, the condition determining whether they glue is not.

::: Example 2
As an example of a scheme morphism that is not a morphism between affine schemes, for $n\geq 1$, there is the map

$$\varphi:\mathbb{A}_\mathbb{K}^{n+1}\setminus \{0\} \rightarrow \mathbb{P}^n_\mathbb{K}$$

that first appeared for motivation in [§Projective Space and the Proj Construction, §§Projective Space](/en/math/scheme_theory/projective_schemes#projective-space){: data-lid="6ddu1" }. This formula was traditionally used to construct projective space, but it did not appear in [§Projective Space and the Proj Construction, ⁋Example 12](/en/math/scheme_theory/projective_schemes#ex12){: data-lid="gbgyj" } when traditional projective space was translated into the language of schemes. This morphism of course satisfies the formula

$$(x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

but the points of $\mathbb{A}^{n+1}_\mathbb{K}$ are not only of this form, and moreover this formula encodes no information about the structure sheaf, so it would be inappropriate to call it a scheme morphism.

Now, to define $\varphi$ as a scheme morphism, consider the affine open subscheme

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)}\cong \Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)$$

of $\mathbb{P}^n_{\mathbb{K}}$ ([§Projective Space and the Proj Construction, ⁋Example 12](/en/math/scheme_theory/projective_schemes#ex12){: data-lid="318ks" }). Also consider the affine space

$$\mathbb{A}^{n+1}_\mathbb{K}=\Spec \mathbb{K}[\x_0,\ldots, \x_n]$$

Then

$$\mathbb{A}^{n+1}_\mathbb{K}\setminus \{0\}=\bigcup_{i=0}^n D(\x_i)$$

and $D(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{\x_i}$. Now for each $i$, since $\varphi_i: D(\x_i) \rightarrow D_+(\x_i)$ is a morphism between affine schemes, it is the same as a ring homomorphism. Then the morphism $\varphi_i$ between affine schemes defined by applying the first isomorphism theorem to the formula

$$\phi_i:\mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]\rightarrow\mathbb{K}[\x_0,\ldots, \x_n]_{\x_i};\qquad \x_{k/i}\mapsto  \frac{\x_k}{\x_i}$$

is the desired morphism. That these satisfy the conditions of [Proposition 1](#prop1){: data-lid="03eu8" } can also be verified by a brief computation. Now borrowing the notation from [§Projective Space and the Proj Construction, §§Projective Space](/en/math/scheme_theory/projective_schemes#projective-space){: data-lid="e5kt5" } again, on each $D(\x_i)$ these are given by the formula

$$(x_0,\ldots, x_n) \mapsto \left[\frac{x_0}{x_i}:\cdots:\frac{x_{i-1}}{x_i}:1:\frac{x_{i+1}}{x_i}:\cdots:\frac{x_n}{x_i} \right]$$

so denoting this by

$$(x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$

would be appropriate.
:::

We shall take this perspective almost as the definition, and the three perspectives to be introduced in the remainder are closer to ways of interpreting it.

## Schemes over a Scheme

First we define the following.

::: Definition 3
For an arbitrary scheme $S$, we call the slice category $\Sch_{/S}$ over $S$ the category of *$S$-schemes*. ([\[Category Theory\] §Category, ⁋Example 13](/en/math/category_theory/categories#ex13){: data-lid="f0alh" })
:::

That is, an $S$-scheme is another name for a scheme morphism $X \rightarrow S$ to $S$, and this is also called the *structure morphism*. This becomes slightly more intuitive upon examining the following example.

::: Example 4
Consider the affine $n$-space $\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$. Then $\mathbb{K}[\x_1,\ldots, \x_n]$ is a $\mathbb{K}$-algebra, and it is via the structure morphism

$$\mathbb{K}\hookrightarrow \mathbb{K}[\x_1,\ldots, \x_n]$$

that this $\mathbb{K}$-algebra structure is given (the argument following [\[Algebraic Structures\] §Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1){: data-lid="wvskh" }).

Then via this structure morphism, we can view $\mathbb{A}^n_\mathbb{K}$ as a $\Spec\mathbb{K}$-scheme

$$\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \Spec \mathbb{K}$$
:::

As above, when $S$ is an affine scheme $S=\Spec A$, it is common to call an $S$-scheme $X$ an $A$-scheme by a slight abuse of language. Then by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="v168l" }, fixing an arbitrary ring $A$, giving a scheme $X$ an $A$-scheme structure is precisely the same as

$$\Hom_\Sch(X, \Spec A)=\Hom_\LRS(X, \Spec A)\cong \Hom_\cRing(A, \Gamma(X, \mathcal{O}_X))$$

That is, giving a scheme $X$ an $A$-scheme structure is algebraically equivalent to giving $\Gamma(X, \mathcal{O}_X)$ an $A$-algebra structure. In particular, when $A=\mathbb{Z}$, since $\mathbb{Z}$ is the initial object of $\cRing$, every scheme can be regarded as a $\mathbb{Z}$-scheme in a unique way. 

Now let us see the following example, which generalizes [Example 2](#ex2){: data-lid="otmft" } further.

::: Example 5
Consider a ring $A$ and an $A$-scheme $X$, and suppose that on $X$, functions $f_0,\ldots, f_n\in \Gamma(X, \mathcal{O}_X)$ are given. Assume that the ideal sheaf generated by these is all of $\mathcal{O}_X$, that is, they satisfy $X=\bigcup_i D(f_i)$. Also consider an affine open covering of $X$, $X=\bigcup U_j$. Then

$$U_{ij}:=D(f_i)\cap U_j=D(f_i\vert_{U_j})\subseteq U_j$$

is an affine open covering of $X$. Meanwhile, consider the projective space defined over $A$

$$\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$$

and consider the open covering $D_+(\x_i)$ of this space. Now, whenever a pair $i,j$ is given, define the function $\varphi_{ij}: U_{ij} \rightarrow D_+(\x_i)$ via the $A$-algebra homomorphism

$$A[\x_0,\ldots, \x_n]_{(\x_i)}\rightarrow \Gamma(U_{ij});\qquad \x_{k/i}\mapsto \frac{f_k\vert_{U_{ij}}}{f_i\vert_{U_{ij}}}$$

Then by definition it is obvious that these morphisms satisfy the gluing condition of [Proposition 1](#prop1){: data-lid="scunk" }, and therefore they define a scheme morphism

$$X \rightarrow \mathbb{P}^n_A$$

Explicitly, this scheme morphism is given, in the same manner as [Example 2](#ex2){: data-lid="y7vov" }, by

$$x\mapsto [f_0(x):\cdots: f_n(x)]$$
:::

## Points

We also define the following.

::: Definition 6
A scheme morphism $\varphi: X \rightarrow Y$ is called, for $Y$, an *$X$-point*. 
:::

Similarly, examining the case where $X$ is an affine scheme is intuitively helpful.

::: Example 7
Consider a field $\mathbb{K}$ and the affine $n$-space $Y=\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$ defined over it. As seen in [Example 4](#ex4){: data-lid="8ylnu" }, $Y$ is a $\Spec\mathbb{K}$-scheme. According to [Definition 6](#def6){: data-lid="tmyaf" }, a $\mathbb{K}$-point of $Y$ is an arbitrary scheme morphism $\Spec\mathbb{K}\rightarrow Y$; but since $Y$ is a $\Spec\mathbb{K}$-scheme, among these we are interested in sections of the structure morphism $Y\rightarrow\Spec\mathbb{K}$, that is, morphisms $X=\Spec\mathbb{K}\rightarrow Y$ over $\Spec\mathbb{K}$. Since this is a $\mathbb{K}$-morphism between affine schemes

$$\Spec \mathbb{K} \rightarrow \Spec \mathbb{K}[\x_1,\ldots, \x_n]$$

it corresponds to a $\mathbb{K}$-algebra homomorphism

$$\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}$$

Now $\mathbb{K}[\x_1,\ldots, \x_n]$ is a polynomial algebra over $\mathbb{K}$, so by the universal property of [\[Algebraic Structures\] §Algebras, ⁋Proposition 8](/en/math/algebraic_structures/algebras#prop8){: data-lid="n2ub2" }, such a $\phi$ is uniquely determined by the image $x_i=\phi(\x_i)\in \mathbb{K}$ of each variable, and conversely any $x=(x_1,\ldots, x_n)\in \mathbb{K}^n$ yields an evaluation homomorphism $\ev_x$. That is, $\phi=\ev_x$, and in particular

$$\ker\phi=(\x_1-x_1,\ldots, \x_n-x_n)$$

since the quotient by the right-hand side is already $\mathbb{K}$. That is, the following two mutually inverse bijections

$$\begin{aligned}\{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}&\rightarrow \{\text{points $(x_1,\ldots, x_n)\in \mathbb{K}^n$}\}\\\Spec\phi&\mapsto (\phi(\x_1),\ldots,\phi(\x_n))\end{aligned}$$

and

$$\begin{aligned}\{\text{points $(x_1,\ldots, x_n)\in \mathbb{K}^n$}\}&\rightarrow \{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}\\a=(a_1,\ldots, a_n)&\mapsto \Spec \ev_a\end{aligned}$$

exist. 
:::

As above, if $X$ is of the form $\Spec A$, we simply call this an $A$-point. The usefulness of this concept can also be seen in the following example.

::: Example 8
Consider the $\mathbb{Z}$-scheme $X=\Spec\mathbb{Z}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)$ defined by polynomials $f_1,\ldots, f_r\in\mathbb{Z}[\x_1,\ldots, \x_n]$ with integer coefficients. Then by [§Affine Scheme, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13){: data-lid="6x8ro" }, a $\mathbb{Q}$-point $\Spec\phi: \Spec \mathbb{Q}\rightarrow X$ of $X$ corresponds to a ring homomorphism

$$\phi:\mathbb{Z}[\x_1,\ldots, \x_n]/(f_1,\ldots, f_r)\rightarrow\mathbb{Q}$$

and since $\phi$ is canonically given over $\mathbb{Z}$, this in turn is in one-to-one correspondence with the rational solutions $(x_1,\ldots, x_n)\in\mathbb{Q}^n$ of

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

Similarly, integer solutions of the above equation correspond exactly to $\mathbb{Z}$-points of $X$.
:::

Based on this perspective, we define the following.

::: Definition 9
We call the functor $\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$ the *functor of points of $X$*.
:::

Then $\Hom_\Sch(-,X)$ is the functor that takes a scheme $S$ and returns the set of $S$-valued points of $X$.

## Families of Schemes

Since the language we have is not yet sufficient to define the final perspective rigorously, we will only explain the geometric intuition. We call a scheme morphism $\varphi:X \rightarrow S$ a *family parametrized by $S$*, or simply an $S$-family. Thus by definition, $\Sch_{/S}$ can be regarded as the category of families parametrized by $S$.

For geometric intuition, one can basically consider the following (non-scheme) situation.

::: Example 10
Consider the sphere $S:x^2+y^2+z^2=1$ defined in the coordinate space $\mathbb{R}^3$, and the projection $\pi: S \rightarrow \mathbb{R}_x$ onto the $x$-axis. Then for any $x_0\in \mathbb{R}_x$,

$$\pi^{-1}(x_0)=\{(x_0,y,z)\in \mathbb{R}^3\mid y^2+z^2=1-x_0^2\}$$

Geometrically, this can be viewed as a situation in which, for each $x_0\in \mathbb{R}_x$, a circle $y^2+z^2=1-x_0^2$ corresponds; hence we may regard $\pi$ as a <em>family of circles parametrized by the $x$-axis</em>. Of course, if $\lvert x_0\rvert>1$ this fiber is empty, and if $x_0=\pm 1$ it is a single point, so it is a circle only when $\lvert x_0\rvert<1$. The manner in which members of a family degenerate in this way will become an issue again when we treat flatness later.
:::

Among the reasons we cannot directly represent this example as a scheme, the less essential one is that $S$ is a closed subset of $\mathbb{R}^3$ and we do not know how to give a closed subset a scheme structure. This will be resolved in [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes){: data-lid="rrapx" }. The more subtle and essential part is that for the function $\pi$ at a point $x_0$, there is no way to represent the fiber $\pi^{-1}(x_0)$. A scheme morphism is of course basically a continuous map, so we could view this as the fiber of a continuous map; but even in that case, there is no way to give $\pi^{-1}(x_0)$ a scheme structure (even assuming the content of [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes){: data-lid="nh8tr" }). To explain this, we must wait a little longer.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

---
