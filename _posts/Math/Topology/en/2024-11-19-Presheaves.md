---
title: "Presheaves"
excerpt: "The gluing lemma and the definition of presheaves"

categories: [Math / Topology]
permalink: /en/math/topology/presheaves
header:
    overlay_image: /assets/images/Math/Topology/Presheaves.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2024-11-19
last_modified_at: 2025-02-18
weight: 8
translated_at: 2026-05-23T05:00:02+00:00
translation_source: kimi-cli
---
## Gluing lemma

We saw in [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8) that when a continuous function $$f:X \rightarrow Y$$ is given, its restriction to a family of subsets satisfying one of the two conditions of [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6) is continuous. Specifically, this condition corresponds to the following two cases:

1. $$(A_i)$$ is an open covering of $$X$$, or
2. $$(A_i)$$ is a locally finite closed covering of $$X$$.

These are the two cases. Conversely, given a family $$(A_i)$$ satisfying such a condition and continuous functions $$f_i$$ defined on them, we can ask whether they specify a continuous function on $$X=\bigcup A_i$$.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> Let a set $$X$$ and a family $$(A_i)$$ of subsets satisfying one of the two conditions of [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6) be given. If a family of continuous functions $$(f_i: A_i \rightarrow Y)$$ satisfies the following condition

$$f_i\vert_{A_i\cap A_j}=f_j\vert_{A_i\cap A_j}\qquad\text{for all $i,j$}$$

then the function $$f:X \rightarrow Y$$ obtained by extending them is continuous.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the function $$f$$ is obtained from [[Set Theory] §Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2). That this function is continuous follows from [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8).

</details>

## Presheaves of Continuous Functions

Many of the structures studied in mathematics, particularly in geometry, are structures given by additional data over a topological space. To handle these, we need tools that deal with the above process.

Define the category $$\Open(X)$$ as the ordered set $$(\mathcal{T}, \subseteq)$$ viewed as a category. That is, its objects are open sets, and whenever $$U\subseteq V$$ there exists a unique arrow $$U\hookrightarrow V$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a topological space $$X$$, a contravariant functor $$\mathscr{F}:\Open(X)^\op \rightarrow \Set$$ is called a *presheaf* of sets defined on $$X$$.

</div>

For reference, presheaves are commonly denoted by $$\mathcal{F}$$ or $$\mathscr{F}$$, and of these the calligraphic $$\mathcal{F}$$ is slightly more natural. However, since we are already using this font for topological structures, we shall use the script font in the topology category.

Now since $$\mathscr{F}$$ is contravariant, whenever an inclusion $$U\hookrightarrow V$$ between open sets is given, a morphism $$\rho_{VU}: \mathscr{F}(V)\rightarrow \mathscr{F}(U)$$ is given, and since $$\mathscr{F}$$ preserves composition, if $$U\hookrightarrow V\hookrightarrow W$$ is given then $$\rho_{WU}=\rho_{VU}\circ\rho_{WV}$$ must hold.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let two topological spaces $$X, Y$$ be given, and define $$\mathscr{F}$$ as follows.

- For any open set $$U$$, $$\mathscr{F}(U)=\Hom_\Top(U, Y)$$.
- When open sets $$U\subseteq V$$ are given, $$\rho_{VU}:\mathscr{F}(V) \rightarrow \mathscr{F}(U)$$ is the restriction map that restricts a continuous function defined on $$V$$ to $$U$$.

Then $$\mathscr{F}$$ becomes a presheaf.

</div>

In particular, this definition can be applied by thinking of the collection of continuous sections from $$X$$ to $$Y$$ ([[Set Theory] §Retractions and Sections, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2)) as a presheaf $$\mathscr{F}$$ when a projection $$p:Y \rightarrow X$$ is given. Generalizing this, we give the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a presheaf $$\mathscr{F}$$ defined on a topological space $$X$$ be given.

- For any open set $$U\subseteq X$$, the elements of $$\mathscr{F}(U)$$ are called *sections* over $$U$$. In particular, the elements of $$\mathscr{F}(X)$$ are called *global sections*.
- For open sets $$U\subseteq V$$, the map $$\rho_{VU}:\mathscr{F}(V) \rightarrow \mathscr{F}(U)$$ is called the *restriction map* from $$V$$ to $$U$$.
- In particular, for open sets $$U\subseteq V$$ and $$s\in \mathscr{F}(V)$$, we write $$\rho_{UV}(f)\in \mathscr{F}(U)$$ simply as $$s\vert_U$$.

</div>

Meanwhile, in [Definition 2](#def2) above, $$\Set$$ can be replaced by an appropriate category, such as $$\Ab$$. For instance, if $$Y=\mathbb{R}$$ in [Example 3](#ex3), we could have defined addition of continuous functions using the addition defined on $$\mathbb{R}$$, and then $$\mathscr{F}(U)$$ would have had the structure of an abelian group. In such a case, $$\mathscr{F}$$ is called a presheaf of abelian groups on $$X$$. For convenience, we shall henceforth call a presheaf $$\mathscr{F}: \Open(X)^\op \rightarrow \mathcal{A}$$ an $$\mathcal{A}$$-valued presheaf. Among presheaves, those satisfying the above gluing condition ([Lemma 1](#lem1)) are called sheaves; we define these in the next post.

## Examples of Presheaves

Next, we look at several examples of presheaves.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Skyscraper sheaf)**</ins> Let a fixed topological space $$X$$ and a point $$i_x:\{x\}\hookrightarrow X$$ be given, and fix an object $$A\in \mathcal{A}$$. Then defining by the formula

$$(i_x)_\ast A(U)=\begin{cases}A&\text{if $x\in U$,}\\T&\text{if $x\not\in U$,}\end{cases}\qquad \text{$T$ a terminal object in $\mathcal{A}$}$$

and giving the restriction map as $$\id_A$$ or using the terminal object $$T$$, this defines a presheaf. This is called the *skyscraper sheaf*.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6 (Constant presheaf)**</ins> Now fix a topological space $$X$$ and an object $$A\in \mathcal{A}$$, assign $$A$$ to every open set, and let all restriction maps be $$\id_A$$. Then this defines a presheaf, which is called the *constant presheaf*.

</div>

The following examples show ways to obtain new presheaves from an arbitrary presheaf.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> When a presheaf $$\mathscr{F}$$ defined on $$X$$ is given, for any open set $$U$$ we can define $$\mathscr{F}\vert_U$$ by the formula

$$\mathscr{F}\vert_U(V)=\mathscr{F}(V)\quad\text{for all open $V\subseteq U$}$$

Then $$\mathscr{F}\vert_U$$ becomes a presheaf. ([§Subspaces, ⁋Lemma 2](/en/math/topology/subspaces#lem2))

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8 (Pushforward)**</ins> Fix a continuous function $$f:X \rightarrow Y$$, and let a presheaf $$\mathscr{F}$$ defined on $$X$$ be given. Then the *pushforward* $$f_\ast \mathscr{F}$$ of $$\mathscr{F}$$ along $$f$$ is defined by

$$f_\ast \mathscr{F}(U)=\mathscr{F}(f^{-1}(U))$$

.

</div>

## Stalks

Meanwhile, what determines a function defined on $$X$$ is of course its value at each $$x\in X$$. The difference between this and a function defined on $$X$$ as a set is that, due to the topological structure defined on $$X$$, we can also examine what happens in a neighborhood of this point $$x$$. Based on this intuition, we define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Consider a presheaf $$\mathscr{F}$$ defined on a topological space $$X$$. For any point $$x\in X$$, we define the *stalk* $$\mathscr{F}_x$$ at the point $$x$$ by

$$\mathscr{F}_x=\varinjlim_{x\in U}\mathscr{F}(U)$$

The elements of $$\mathscr{F}_x$$ are called *germs* at the point $$x$$.

</div>

In particular, if $$\mathscr{F}$$ is a complete category valued presheaf, then $$\mathscr{F}_x$$ is always well-defined. Meanwhile, writing out the limit expression directly in a concrete category,

$$\mathscr{F}_x=\{(s,U)\mid x\in U\in\mathscr{T},s\in\mathscr{F}(U)\}/\mathnormal{\sim}$$

and here the equivalence relation $$\sim$$ is defined by

$$(s,U)\sim(t,V)\iff\text{$\exists$ open neighborhood $W\subseteq U\cap V$ of $x$ satisfying $\rho_{UW}(s)=\rho_{VW}(t)$}$$

That is, intuitively, the elements $$(s,U)$$ of $$\mathscr{F}_x$$ can be thought of as objects that carry the value $$s(x)$$ at $$x$$ along with additional local information[^1] of $$s$$ in a neighborhood of $$x$$. For convenience, for any $$s\in \mathscr{F}(U)$$, we write the image of $$s$$ under $$\mathscr{F}(U) \rightarrow \mathscr{F}_x$$ as $$s_x$$.

As it stands, a presheaf may be said to be an object that supplies additional algebraic information rather than a geometric one, but it is also possible to turn it into a geometric object. Consider a presheaf $$\mathscr{F}$$ defined on a topological space $$X$$, and the set

$$\Spe(\mathscr{F})=\coprod_{x\in X} \mathscr{F}_x=\{(x,\xi)\mid x\in X, \xi\in \mathscr{F}_x\}$$

Then for any open set $$U\subseteq X$$ and any $$s\in \mathscr{F}(U)$$, there exist functions

$$\tilde{s}:U \rightarrow \Spe(\mathscr{F}); \quad x\mapsto (x,s_x)$$

Now we endow $$\Spe(\mathscr{F})$$ with the final topology defined by the family of these functions ([§Initial and Final Topologies, ⁋Definition 4](/en/math/topology/initial_and_final_topology#def6)), and call this space the *étalé space* of $$\mathscr{F}$$.

## Morphisms of Presheaves

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A natural transformation between two presheaves $$\mathscr{F}, \mathscr{G}:\Open(X) \rightarrow \mathcal{A}$$ defined on a fixed topological space $$X$$ is called a *presheaf morphism*.

</div>

That is, the category of $$\mathcal{A}$$-valued presheaves defined on $$X$$ is the functor category $$[\Open(X)^\op, \mathcal{A}]$$. We denote this by $$\PSh(X, \mathcal{A})$$, and when there is no risk of confusion from context, we also write simply $$\PSh(X)$$. Incidentally, the $$f_\ast$$ of [Example 8](#ex8) is a functor $$\PSh(X, \mathcal{A})\rightarrow \PSh(Y, \mathcal{A})$$.

Thinking of [Example 2](#ex2), which gives us intuition, the map $$\phi(U):\mathscr{F}(U) \rightarrow \mathscr{G}(U)$$ defined for an open set $$U$$ can be thought of as the function obtained by restricting $$\phi:\mathscr{F}\rightarrow \mathscr{G}$$ to the open set $$U$$, so we often write $$\phi\vert_U$$ instead of $$\phi(U)$$.

Meanwhile, the following proposition holds by the universal property of the limit cone.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Let a morphism $$\phi:\mathscr{F}\rightarrow\mathscr{G}$$ between presheaves defined on a topological space $$X$$ be given. Then for any $$x\in X$$, a morphism $$\phi_x:\mathscr{F}_x\rightarrow\mathscr{G}_x$$ between stalks is naturally induced.

</div>

The following examples should have appeared under [Examples of Presheaves](#examples-of-presheaves) above, but were postponed because we had not yet defined presheaf morphisms.

<div class="example" markdown="1">

<ins id="ex12">**Example 12 (Sheaf Hom)**</ins> Fix two presheaves $$\mathscr{F}, \mathscr{G}$$ and define

$$\mathscr{Hom}(\mathscr{F},\mathscr{G})(U)=\Hom_{\PSh(U)}(\mathscr{F}\vert_U, \mathscr{G}\vert_U)$$

for each $$U$$.

</div>

<div class="example" markdown="1">

<ins id="ex13">**Example 13 (Product)**</ins> For a family $$(\mathscr{F}_i:\Open(X) \rightarrow \Set)_{i\in I}$$ of presheaves defined on a topological space $$X$$, their product is given by

$$\left(\prod_{i\in I} \mathscr{F}_i\right)(U)=\prod_{i\in I} \mathscr{F}_i(U)$$

.

</div>

Using definitions as above, structures defined in the category $$\mathcal{A}$$, such as products, coproducts, limits, colimits, monoidal products, etc., can be carried over to $$\PSh(X, \mathcal{A})$$. In particular, $$\PSh(X, \Ab)$$ inherits the monoidal structure $$(\Ab,\otimes, \mathbb{Z})$$ defined on $$\Ab$$, and the monoidal objects here are $$\PSh(X, \Ring)$$. The following example can be understood in the same vein.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> For a $$\Ring$$-valued presheaf $$\mathscr{O}_X$$ defined on a topological space $$X$$, a left $$\mathscr{O}_X$$-module object $$\mathscr{F}\in\PSh(X,\Ab)$$ is simply called an $$\mathscr{O}_X$$-module.

</div>

## Abelian Presheaves

Until now we have ignored which category a presheaf takes values in, but now we examine presheaves taking values specifically in the category $$\Ab$$.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> For a topological space $$X$$, a contravariant functor $$\Open(X)\rightarrow\Ab$$ is called an *abelian presheaf*.

</div>

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> Let a morphism $$\phi:\mathscr{F}\rightarrow\mathscr{G}$$ between abelian presheaves defined on a topological space $$X$$ be given. Then the *presheaf kernel* $$\ker\phi$$ of $$\phi$$ is the data consisting of

- for each open set $$U\subseteq X$$, $$U\mapsto \ker(\phi(U))$$
- for each pair of open sets $$U\subseteq V$$, the restriction map $$\rho_{VU}:\ker(\phi(V))\rightarrow\ker(\phi(U))$$ uniquely determined by the following diagram

  ![presheaf_kernel-1](/assets/images/Math/Topology/Presheaves-1.png){:style="width:18em" class="invert" .align-center}

.

</div>

In this definition, $$\rho_{VU}$$ is the restriction map uniquely determined by the universal property of $$\ker(\phi(U))$$.

<div class="proposition" markdown="1">

<ins id="lem17">**Lemma 17**</ins> The $$\ker\phi$$ defined above is an (abelian) presheaf on $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The following diagram

![presheaf_kernel-2](/assets/images/Math/Topology/Presheaves-2.png){:style="width:18em" class="invert" .align-center}

and the universal property of the kernel make this obvious.

</details>

In the same way, *presheaf cokernel*, *presheaf image*, *presheaf coimage*, and
