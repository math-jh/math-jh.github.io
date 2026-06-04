---
title: "Morphisms of Schemes"
description: "A scheme morphism is defined as a continuous map together with a morphism of structure sheaves, and morphisms between affine schemes correspond to ring homomorphisms. General scheme morphisms can be understood by gluing together local morphisms over an affine open cover."
excerpt: "Four perspectives on scheme morphisms as morphisms of locally ringed spaces"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/morphism_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-19
last_modified_at: 2025-02-19
weight: 7
translated_at: 2026-06-02T05:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T05:00:02+00:00
---
By definition, $$\Sch$$ is a full subcategory of $$\LRS$$. ([§Schemes, ⁋Definition 1](/en/math/scheme_theory/schemes#def1)) That is, given two schemes $$X,Y$$, a scheme morphism from $$X$$ to $$Y$$ is given by a continuous map $$\varphi: X \rightarrow Y$$ together with a morphism of structure sheaves $$\varphi^\sharp: \mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$, where $$\varphi^\sharp$$ must restrict to a local homomorphism on each stalk. ([§Affine Schemes, ⁋Definition 2](/en/math/scheme_theory/affine_schemes#def2)) 

Thus, a scheme morphism $$f:X \rightarrow Y$$ is fundamentally an object we have already defined. In the next post we will examine properties of scheme morphisms; before doing so, we present four perspectives for understanding them. 

## Gluing Ring Homomorphisms

The first perspective is a fairly natural one. A scheme is essentially constructed by gluing affine schemes, and by the categorical equivalence $$\AffSch\cong\cRing^\op$$, a morphism between affine schemes is essentially a ring homomorphism. Therefore, one should be able to understand a scheme morphism as gluing morphisms between affine schemes. That is, it is reasonable to expect the following proposition.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Let a scheme morphism $$\varphi: X \rightarrow Y$$ be given. If $$X$$ has an affine open subset $$U\cong\Spec A$$ and $$Y$$ has an affine open subset $$V\cong\Spec B$$ satisfying $$\varphi(U)\subseteq V$$, then the restriction $$\varphi\vert_U: U \rightarrow V$$ is a morphism of affine schemes. 

Conversely, let two affine open coverings $$\{U_i\}$$ of $$X$$ and $$\{V_j\}$$ of $$Y$$ be given, and let morphisms of affine schemes $$\varphi_{ij}: U_i \rightarrow V_j$$ be given. If these satisfy the gluing condition on each intersection and are thereby well defined, then the $$\varphi_{ij}$$ define a scheme morphism $$\varphi: X \rightarrow Y$$. 

</div>

One direction is merely a new version of the assertion that $$\AffSch$$ is a full subcategory of $$\LRS$$, by [§Affine Schemes, ⁋Proposition 11](/en/math/scheme_theory/affine_schemes#prop11), and the gluing for the converse is also obtained in an obvious manner. 

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> As an example of a scheme morphism that is not a morphism between affine schemes, consider the map

$$\varphi:\mathbb{A}_\mathbb{K}^{n+1}\setminus \{0\} \rightarrow \mathbb{P}^n_\mathbb{K}$$

that first appeared for motivation in [§Projective Schemes, §§Projective Space](/en/math/scheme_theory/projective_schemes#projective-space). This formula was traditionally used to construct projective space, but it did not appear in [§Projective Schemes, ⁋Example 12](/en/math/scheme_theory/projective_schemes#ex12) when translating classical projective space into the language of algebraic geometry. Of course this morphism satisfies the formula $$(x_0,\ldots, x_n)\mapsto [x_0:\cdots:x_n]$$, but the points of $$\mathbb{A}^{n+1}_\mathbb{K}$$ are not merely of this form, and moreover this formula carries no information about the structure sheaf, so it would be inappropriate to call it a scheme morphism.

To define $$\varphi$$ as a scheme morphism, consider the affine open subscheme of $$\mathbb{P}^n_{\mathbb{K}}$$

$$D_+(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{(\x_i)}\cong \Spec \mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]/(\x_{i/i}-1)$$

([§Projective Schemes, ⁋Example 12](/en/math/scheme_theory/projective_schemes#ex12)). Also consider the affine space

$$\mathbb{A}^{n+1}_\mathbb{K}=\Spec \mathbb{K}[\x_0,\ldots, \x_n]$$

Then

$$\mathbb{A}^{n+1}_\mathbb{K}\setminus \{0\}=\bigcup_{i=0}^n D(\x_i)$$

and $$D(\x_i)\cong \Spec \mathbb{K}[\x_0,\ldots, \x_n]_{\x_i}$$. For each $$i$$, the map $$\varphi_i: D(\x_i) \rightarrow D_+(\x_i)$$ is a morphism of affine schemes, hence corresponds to a ring homomorphism. Then the affine scheme morphism $$\varphi_i$$ obtained by applying the first isomorphism theorem to the formula

$$\phi_i:\mathbb{K}[\x_{0/i},\ldots, \x_{n/i}]\rightarrow\mathbb{K}[\x_0,\ldots, \x_n]_{\x_i};\qquad \x_{k/i}\mapsto  \frac{\x_k}{\x_i}$$

is the desired morphism. That these satisfy the conditions of [Proposition 1](#prop1) can also be checked by a short calculation. Now, borrowing the notation from [§Projective Schemes, §§Projective Space](/en/math/scheme_theory/projective_schemes#projective-space), on each $$D(\x_i)$$ they are given by the formula

$$(x_0,\ldots, x_n) \rightarrow \left[\frac{x_0}{x_i}:\cdots:\frac{x_{i-1}}{x_i}:1:\frac{x_{i+1}}{x_i}:\cdots:\frac{x_n}{x_i} \right]$$

so it is appropriate to denote this as

$$(x_0,\ldots, x_n)\rightarrow [x_0:\cdots:x_n]$$

</div>

We shall regard this perspective almost as the definition, and the remaining three perspectives introduced below are better understood as ways of interpreting it. 

## Schemes over a Scheme

First we define the following. 

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For any scheme $$S$$, we call the slice category $$\Sch_{/S}$$ over $$S$$ the category of *$$S$$-schemes*. ([[Category Theory] §Categories, ⁋Example 13](/en/math/category_theory/categories#ex13)) 

</div>

That is, an $$S$$-scheme is another name for a scheme morphism $$X \rightarrow S$$ to $$S$$, which is also called the *structure morphism*. 

This becomes a little more intuitive when we look at the following example.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> Consider affine $$n$$-space $$\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$$. Then $$\mathbb{K}[\x_1,\ldots, \x_n]$$ is a $$\mathbb{K}$$-algebra, and this means that a $$\mathbb{K}$$-algebra structure is given via the structure morphism

$$\mathbb{K}\hookrightarrow \mathbb{K}[\x_1,\ldots, \x_n]$$

([[Algebraic Structures] §Algebras, ⁋Definition 1](/en/math/algebraic_structures/algebras#def1) and the argument following it.)

Then through this structure morphism we may view $$\mathbb{A}^n_\mathbb{K}$$ as a $$\Spec\mathbb{K}$$-scheme

$$\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \Spec \mathbb{K}$$

</div>

As above, when $$S$$ is an affine scheme $$S=\Spec A$$, it is common by a slight abuse of language to call an $$S$$-scheme $$X$$ an $$A$$-scheme. Then by [§Affine Schemes, ⁋Theorem 13](/en/math/scheme_theory/affine_schemes#thm13), fixing an arbitrary ring $$A$$ and giving an $$A$$-scheme structure on a scheme $$X$$ is precisely the same as

$$\Hom_\Sch(X, \Spec A)=\Hom_\LRS(X, \Spec A)\cong \Hom_\cRing(A, \Gamma(X, \mathscr{O}_X))$$

That is, giving an $$A$$-scheme structure on a scheme $$X$$ is algebraically equivalent to giving an $$A$$-algebra structure on $$\Gamma(X, \mathscr{O}_X)$$. In particular, when $$A=\mathbb{Z}$$, since $$\mathbb{Z}$$ is the initial object of $$\cRing$$, every scheme can be regarded as a $$\mathbb{Z}$$-scheme in a unique way. 

Now let us look at the following example, which generalizes [Example 2](#ex2) further.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Consider a ring $$A$$ and an $$A$$-scheme $$X$$, let functions $$f_0,\ldots, f_n\in \Gamma(X, \mathscr{O}_X)$$ defined on $$X$$ be given, and let $$X=\bigcup U_j$$ be an affine open covering of $$X$$. Then

$$U_{ij}:=D(f_i)\cap U_j=D(f_i\vert_{U_j})\subseteq U_j$$

form an affine open covering of $$X$$. On the other hand, consider the projective space over $$A$$

$$\mathbb{P}^n_A=\Proj A[\x_0,\ldots, \x_n]$$

and its open covering $$D_+(\x_i)$$. Now for each pair $$i,j$$, define the map $$\varphi_{ij}: U_{ij} \rightarrow D_+(\x_i)$$ via the ring homomorphism

$$A[\x_{0/i},\ldots, \x_{n/i}]\rightarrow \Gamma(U_{ij});\qquad \x_{k/i}\mapsto \frac{f_k\vert_{U_{ij}}}{f_i\vert_{U_{ij}}}$$

Then by definition it is obvious that these satisfy the gluing condition of [Proposition 1](#prop1), and hence they define a scheme morphism

$$X \rightarrow \mathbb{P}^n_A$$

Explicitly, this scheme morphism is given, in the same way as in [Example 2](#ex2), by

$$x\mapsto [f_0(x):\cdots: f_n(x)]$$

</div>

## Points

Next, we define the following.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> We call a scheme morphism $$f: X \rightarrow Y$$ an *$$X$$-point* of $$Y$$. 

</div>

Again, it helps intuitively to examine the case where $$X$$ is an affine scheme.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Consider an algebraically closed field $$\mathbb{K}$$, the affine $$n$$-space $$Y=\mathbb{A}^n_\mathbb{K}=\Spec \mathbb{K}[\x_1,\ldots, \x_n]$$ defined over it, and $$X=\Spec \mathbb{K}$$. Then a scheme morphism $$X \rightarrow Y$$ is a morphism of affine schemes

$$\Spec \mathbb{K} \rightarrow \Spec \mathbb{K}[\x_1,\ldots, \x_n]$$

and thus corresponds to a ring homomorphism

$$\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}$$

This ring homomorphism must be surjective, because by the definition of a ring homomorphism $$\phi(1)=1$$ and therefore $$\phi(x)=x$$ for any $$x\in \mathbb{K}$$. Hence by the first isomorphism theorem

$$\mathbb{K}[\x_1,\ldots, \x_n]/\ker\phi\cong \mathbb{K}$$

Then by the fourth result of [[Algebraic Structures] §Quotient Rings, Ring Homomorphisms, ⁋Theorem 3](/en/math/algebraic_structures/quotient_rings#thm3), $$\ker\phi$$ must be a maximal ideal of $$\mathbb{K}[\x_1,\ldots, \x_n]$$, and therefore by [[Commutative Algebra] §Nullstellensatz, ⁋Lemma 5](/en/math/commutative_algebra/nullstellensatz#lem5)

$$\ker\phi=(\x_1-x_1,\ldots, \x_n-x_n)$$

for some $$x=(x_1,\ldots, x_n)$$, and $$\phi$$ becomes the evaluation homomorphism $$\ev_x$$ at the point $$x$$. Moreover, considering the proof of that lemma, we also see that $$x_i=\phi(\x_i)$$. Thus there exist the following two mutually inverse bijections

$$\begin{aligned}\{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}&\rightarrow \{\text{points $(x_1,\ldots, x_n)\in \mathbb{A}^n_\mathbb{K}$}\}\\\Spec\phi&\mapsto (\phi(\x_1),\ldots,\phi(\x_n))\end{aligned}$$

and

$$\begin{aligned}\{\text{points $(x_1,\ldots, x_n)\in \mathbb{A}^n_\mathbb{K}$}\}&\rightarrow \{\text{$\mathbb{K}$-point $\Spec \phi:\Spec\mathbb{K}\rightarrow \mathbb{A}^n_\mathbb{K}$}\}\\a=(a_1,\ldots, a_n)&\mapsto \Spec \ev_a\end{aligned}$$

</div>

As above, if $$X$$ is of the form $$\Spec A$$, we simply call it an $$A$$-point. The usefulness of this concept can also be seen in the following example.

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Let a $$\mathbb{C}$$-scheme $$X=\Spec\frac{\mathbb{C}[\x_1,\ldots, \x_n]}{(f_1,\ldots, f_r)}$$ be given, and consider the $$\mathbb{Q}$$-points of this scheme. Then from [[Commutative Algebra] §Nullstellensatz, ⁋Lemma 5](/en/math/commutative_algebra/nullstellensatz#lem5) and the calculation of [Example 6](#ex6), we know that there exists a one-to-one correspondence between the $$\mathbb{Q}$$-points $$\Spec\phi: \Spec \mathbb{Q}\rightarrow X$$ of $$X$$ and the rational solutions of

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

Similarly, the integer solutions of the above equations correspond exactly to the $$\mathbb{Z}$$-points of $$X$$. 

</div>

Based on this perspective we define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> We call the functor $$\Hom_\Sch(-,X): \Sch^\op \rightarrow \Set$$ the *functor of points of $$X$$*. 

</div>

Then $$\Hom_\Sch(-,X)$$ is the functor that takes a scheme $$S$$ and returns the set of $$S$$-valued points of $$X$$. 

## Families of Schemes

The final perspective is one for which our present language is still insufficient to give a rigorous definition, so we shall only explain the geometric intuition. We call a scheme morphism $$f:X \rightarrow S$$ a *family parametrized by $$S$$*, or simply an $$S$$-family. Therefore by definition $$\Sch_{/S}$$ can be thought of as the category of families parametrized by $$S$$. 

For geometric intuition, it basically suffices to consider the following (non-scheme) situation.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Consider the sphere $$S:x^2+y^2+z^2=1$$ defined in the coordinate space $$\mathbb{R}^3$$, and the projection $$\pi: S \rightarrow \mathbb{R}_x$$ onto the $$x$$-axis. Then for any $$x_0\in \mathbb{R}_x$$,

$$\pi^{-1}(x_0)=\{(x_0,y,z)\in \mathbb{R}: y^2+z^2=1-x_0^2\}$$

Geometrically, this can be viewed as a situation in which to each $$x_0\in \mathbb{R}_x$$ there corresponds a circle $$y^2+z^2=1-x_0^2$$, and therefore we may think of $$\pi$$ as <em-ko>a family of circles parametrized by the $x$-axis</em-ko>. 

</div>

Among the reasons why this example cannot be immediately represented in the language of schemes, the less essential one is that $$S$$ is a closed subset of $$\mathbb{R}^3$$ and we do not yet know how to put a scheme structure on a closed subset. This will be resolved in [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes). The more subtle and essential point is that there is no way to represent the fiber $$\pi^{-1}(x_0)$$ of the function $$\pi$$ at a point $$x_0$$. Of course a scheme morphism is basically a continuous map, so one could regard this as the fiber of a continuous map; but even if we do so, there is no way to give $$\pi^{-1}(x_0)$$ a scheme structure (even assuming the contents of [§Closed Subschemes](/en/math/scheme_theory/closed_subschemes)). We will have to wait a little longer to explain this. 

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
