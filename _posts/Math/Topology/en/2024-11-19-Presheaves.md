---
title: "Presheaves"
description: "This post introduces the notion of a sheaf as a contravariant functor assigning continuous functions on open sets of a topological space, and discusses the conditions for extending continuous functions on a family of subsets to the whole space via the gluing lemma."
excerpt: "The gluing lemma and the definition of a presheaf"

categories: [Math / Topology]
permalink: /en/math/topology/presheaves
sidebar: 
    nav: "topology-en"

date: 2024-11-19
last_modified_at: 2025-02-18
weight: 8
translated_at: 2026-06-03T06:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-03T06:30:02+00:00
---
## Gluing lemma

As we saw in [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8), given a continuous function $$f:X \rightarrow Y$$, restricting it to a family of subsets satisfying one of the two conditions in [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6) yields a continuous map. Specifically, these conditions correspond to the following two cases:

1. $$(A_i)$$ is an open covering of $$X$$, or
2. $$(A_i)$$ is a locally finite closed covering of $$X$$.

Conversely, given such a family $$(A_i)$$ and continuous functions $$f_i$$ defined on them, we may ask whether they determine a continuous function on $$X=\bigcup A_i$$.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> Let $$X$$ be a set and $$(A_i)$$ a family of subsets satisfying one of the two conditions in [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6). If a family of continuous functions $$(f_i: A_i \rightarrow Y)$$ satisfies

$$f_i\vert_{A_i\cap A_j}=f_j\vert_{A_i\cap A_j}\qquad\text{for all $i,j$}$$

then the function $$f:X \rightarrow Y$$ obtained by gluing them together is continuous.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the function $$f$$ is obtained from [\[Set Theory\] §Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2). Its continuity follows from [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8).

</details>

## Presheaves of continuous functions

Many structures studied in mathematics, especially in geometry, are spaces equipped with additional data defined over a topological space. To handle such structures, we need tools that manage the above process.

Define the category $$\Open(X)$$ as the category associated to the ordered set $$(\mathcal{T}, \subseteq)$$. That is, its objects are open sets, and for each $$U\subseteq V$$ there is a unique arrow $$U\hookrightarrow V$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a topological space $$X$$, a contravariant functor $$\mathscr{F}:\Open(X)^\op \rightarrow \Set$$ is called a *presheaf* of sets on $$X$$.

</div>

By convention, presheaves are commonly denoted by $$\mathcal{F}$$ or $$\mathscr{F}$$; between these, the calligraphic $$\mathcal{F}$$ is slightly more natural. However, since we are already using this font for topological structures, we adopt the script font in the topology category.

Since $$\mathscr{F}$$ is contravariant, each inclusion $$U\hookrightarrow V$$ of open sets yields a morphism $$\rho_{VU}: \mathscr{F}(V)\rightarrow \mathscr{F}(U)$$, and because $$\mathscr{F}$$ preserves composition, whenever $$U\hookrightarrow V\hookrightarrow W$$ we must have $$\rho_{WU}=\rho_{VU}\circ\rho_{WV}$$.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let $$X, Y$$ be two topological spaces, and define $$\mathscr{F}$$ as follows.

- For any open set $$U$$, set $$\mathscr{F}(U)=\Hom_\Top(U, Y)$$.
- For open sets $$U\subseteq V$$, let $$\rho_{VU}:\mathscr{F}(V) \rightarrow \mathscr{F}(U)$$ be the restriction map sending a continuous function on $$V$$ to its restriction to $$U$$.

Then $$\mathscr{F}$$ is a presheaf.

</div>

In particular, this definition can be applied when a projection $$p:Y \rightarrow X$$ is given, by considering the presheaf $$\mathscr{F}$$ of continuous sections from $$X$$ to $$Y$$ ([\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2)). Generalizing this, we make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let $$\mathscr{F}$$ be a presheaf defined on a topological space $$X$$.

- For any open set $$U\subseteq X$$, the elements of $$\mathscr{F}(U)$$ are called *sections* over $$U$$. In particular, elements of $$\mathscr{F}(X)$$ are called *global sections*.
- For open sets $$U\subseteq V$$, the map $$\rho_{VU}:\mathscr{F}(V) \rightarrow \mathscr{F}(U)$$ is called the *restriction map* from $$V$$ to $$U$$.
- In particular, for open sets $$U\subseteq V$$ and $$s\in \mathscr{F}(V)$$, we write $$\rho_{VU}(s)\in \mathscr{F}(U)$$ simply as $$s\vert_U$$.

</div>

Meanwhile, in [Definition 2](#def2) above, $$\Set$$ can be replaced by an appropriate category, such as $$\Ab$$. For instance, in [Example 3](#ex3), if $$Y=\mathbb{R}$$, we could use addition on $$\mathbb{R}$$ to define addition of continuous functions, and then $$\mathscr{F}(U)$$ would carry the structure of an abelian group. In such a case, $$\mathscr{F}$$ is called a presheaf of abelian groups on $$X$$. For convenience, we shall call a presheaf $$\mathscr{F}: \Open(X)^\op \rightarrow \mathcal{A}$$ an $$\mathcal{A}$$-valued presheaf. Among presheaves, those satisfying the gluing condition ([Lemma 1](#lem1)) are called sheaves; we define these in the next post.

## Examples of presheaves

Next, we examine several examples of presheaves.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Skyscraper sheaf)**</ins> Fix a topological space $$X$$ and a point $$i_x:\{x\}\hookrightarrow X$$, and fix an object $$A\in \mathcal{A}$$. Then defining

$$(i_x)_\ast A(U)=\begin{cases}A&\text{if $x\in U$,}\\T&\text{if $x\not\in U$,}\end{cases}\qquad \text{$T$ a terminal object in $\mathcal{A}$}$$

and giving restriction maps as $$\id_A$$ or via the terminal object $$T$$ defines a presheaf. This is called the *skyscraper sheaf*.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6 (Constant presheaf)**</ins> Now fix a topological space $$X$$ and an object $$A\in \mathcal{A}$$, assign $$A$$ to every open set, and let all restriction maps be $$\id_A$$. This defines a presheaf, called the *constant presheaf*.

</div>

The following examples show ways to obtain new presheaves from an arbitrary presheaf.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Given a presheaf $$\mathscr{F}$$ on $$X$$, for any open set $$U$$ we can define $$\mathscr{F}\vert_U$$ by

$$\mathscr{F}\vert_U(V)=\mathscr{F}(V)\quad\text{for all open $V\subseteq U$}$$

Then $$\mathscr{F}\vert_U$$ is a presheaf. ([§Subspaces, ⁋Lemma 2](/en/math/topology/subspaces#lem2))

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8 (Pushforward)**</ins> Fix a continuous function $$f:X \rightarrow Y$$, and let $$\mathscr{F}$$ be a presheaf on $$X$$. The *pushforward* $$f_\ast \mathscr{F}$$ of $$\mathscr{F}$$ along $$f$$ is defined by

$$f_\ast \mathscr{F}(U)=\mathscr{F}(f^{-1}(U))$$

</div>

## Stalks

Of course, what determines a function defined on $$X$$ is its value at each point $$x\in X$$. What distinguishes this from a function on $$X$$ as a set is that, thanks to the topological structure on $$X$$, we can also examine what happens in a neighborhood of the point $$x$$. Based on this intuition, we define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Let $$\mathscr{F}$$ be a presheaf on a topological space $$X$$. For any point $$x\in X$$, the *stalk* $$\mathscr{F}_x$$ at $$x$$ is defined by

$$\mathscr{F}_x=\varinjlim_{x\in U}\mathscr{F}(U)$$

The elements of $$\mathscr{F}_x$$ are called *germs* at $$x$$.

</div>

In particular, if $$\mathscr{F}$$ is a presheaf valued in a complete category, then $$\mathscr{F}_x$$ is always well-defined. Meanwhile, writing out the limit explicitly in a concrete category, we have

$$\mathscr{F}_x=\{(s,U)\mid x\in U\in\mathscr{T},s\in\mathscr{F}(U)\}/\mathnormal{\sim}$$

where the equivalence relation $$\sim$$ is defined by

$$(s,U)\sim(t,V)\iff\text{$\exists$ open neighborhood $W\subseteq U\cap V$ of $x$ satisfying $\rho_{UW}(s)=\rho_{VW}(t)$}$$

That is, intuitively, the elements $$(s,U)$$ of $$\mathscr{F}_x$$ can be thought of as the value $$s(x)$$ at $$x$$ together with additional local information[^1] about $$s$$ near $$x$$. For convenience, for any $$s\in \mathscr{F}(U)$$, we write the image of $$s$$ under $$\mathscr{F}(U) \rightarrow \mathscr{F}_x$$ as $$s_x$$.

For now, a presheaf is more of an object with additional algebraic information than a geometric one, but it is possible to make it into a geometric object. Consider a presheaf $$\mathscr{F}$$ on a topological space $$X$$ and the set

$$\Spe(\mathscr{F})=\coprod_{x\in X} \mathscr{F}_x=\{(x,\xi)\mid x\in X, \xi\in \mathscr{F}_x\}$$

Then for any open set $$U\subseteq X$$ and any $$s\in \mathscr{F}(U)$$, the functions

$$\tilde{s}:U \rightarrow \Spe(\mathscr{F}); \quad x\mapsto (x,s_x)$$

exist. We endow $$\Spe(\mathscr{F})$$ with the final topology defined by this family of functions ([§Initial and Final Topology, ⁋Definition 4](/en/math/topology/initial_and_final_topology#def4)), and call this space the *étalé space* of $$\mathscr{F}$$.

## Morphisms of presheaves

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> Let $$\mathscr{F}, \mathscr{G}:\Open(X) \rightarrow \mathcal{A}$$ be two presheaves on a fixed topological space $$X$$. A natural transformation between them is called a *presheaf morphism*.

</div>

Thus the category of $$\mathcal{A}$$-valued presheaves on $$X$$ is the functor category $$[\Open(X)^\op, \mathcal{A}]$$. We denote this by $$\PSh(X, \mathcal{A})$$, and when there is no risk of confusion from context, we simply write $$\PSh(X)$$. As a side note, the $$f_\ast$$ from [Example 8](#ex8) is a functor $$\PSh(X, \mathcal{A})\rightarrow \PSh(Y, \mathcal{A})$$.

Thinking of the intuitive [Example 3](#ex3), for an open set $$U$$ the map $$\phi(U):\mathscr{F}(U) \rightarrow \mathscr{G}(U)$$ can be thought of as the function obtained by restricting $$\phi:\mathscr{F}\rightarrow \mathscr{G}$$ to $$U$$, so we sometimes write $$\phi\vert_U$$ instead of $$\phi(U)$$.

Meanwhile, by the universal property of the limit cone, the following proposition holds.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Let $$\phi:\mathscr{F}\rightarrow\mathscr{G}$$ be a morphism of presheaves on a topological space $$X$$. Then for any $$x\in X$$, a morphism $$\phi_x:\mathscr{F}_x\rightarrow\mathscr{G}_x$$ between stalks is naturally induced.

</div>

The following examples should have appeared under [Examples of presheaves](#examples-of-presheaves) above, but were postponed because we had not yet defined presheaf morphisms.

<div class="example" markdown="1">

<ins id="ex12">**Example 12 (Sheaf Hom)**</ins> Fix two presheaves $$\mathscr{F}, \mathscr{G}$$ and define, for any $$U$$,

$$\mathscr{Hom}(\mathscr{F},\mathscr{G})(U)=\Hom_{\PSh(U)}(\mathscr{F}\vert_U, \mathscr{G}\vert_U)$$

</div>

<div class="example" markdown="1">

<ins id="ex13">**Example 13 (Product)**</ins> For a family of presheaves $$(\mathscr{F}_i:\Open(X) \rightarrow \Set)_{i\in I}$$ on a topological space $$X$$, their product $$\prod_{i\in I} \mathscr{F}_i$$ can be defined by

$$\left(\prod_{i\in I} \mathscr{F}_i\right)(U)=\prod_{i\in I} \mathscr{F}_i(U)$$

</div>

Using definitions as above, structures defined in a category $$\mathcal{A}$$—for example products, coproducts, limits, colimits, monoidal products, etc.—can be transferred to $$\PSh(X, \mathcal{A})$$. In particular, $$\PSh(X, \Ab)$$ inherits the monoidal structure $$(\Ab,\otimes, \mathbb{Z})$$, and the monoidal objects here are $$\PSh(X, \Ring)$$. In the same vein, the following example can be understood.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> For a $$\Ring$$-valued presheaf $$\mathscr{O}_X$$ on a topological space $$X$$, a left $$\mathscr{O}_X$$-module object $$\mathscr{F}\in\PSh(X,\Ab)$$ is simply called an $$\mathscr{O}_X$$-module.

</div>

## Abelian presheaves

Until now we have ignored the category in which a presheaf takes values; now we focus on presheaves valued in the category $$\Ab$$.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> For a topological space $$X$$, a contravariant functor $$\Open(X)\rightarrow\Ab$$ is called an *abelian presheaf*.

</div>

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> Let $$\phi:\mathscr{F}\rightarrow\mathscr{G}$$ be a morphism of abelian presheaves on a topological space $$X$$. The *presheaf kernel* $$\ker\phi$$ of $$\phi$$ is the data consisting of:

- For each open set $$U\subseteq X$$, the assignment $$U\mapsto \ker(\phi(U))$$;
- For each inclusion $$U\subseteq V$$ of open sets, the restriction map $$\rho_{VU}:\ker(\phi(V))\rightarrow\ker(\phi(U))$$ uniquely determined by the following diagram:
  
  ![presheaf_kernel-1](/assets/images/Math/Topology/Presheaves-1.png){:style="width:18em" class="invert" .align-center}

</div>

In this definition, $$\rho_{VU}$$ is the restriction map uniquely determined by the universal property of $$\ker(\phi(U))$$.

<div class="proposition" markdown="1">

<ins id="lem17">**Lemma 17**</ins> The $$\ker\phi$$ defined above is an (abelian) presheaf on $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is immediate from the following diagram and the universal property of kernels:

![presheaf_kernel-2](/assets/images/Math/Topology/Presheaves-2.png){:style="width:18em" class="invert" .align-center}

</details>

In the same way, one can define *presheaf cokernel*, *presheaf image*, *presheaf coimage*, *presheaf quotient*, and so on. Therefore, the category $$\PSh(X,\Ab)$$ of abelian presheaves on a given topological space $$X$$ is an abelian category.
  
---
**References**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---

[^1]: For example, if $$X=\mathbb{R}$$, then to define the derivative of a function at a point $$x$$ of $$\mathbb{R}$$, it suffices to know the values of $$f$$ in an arbitrarily small neighborhood of $$x$$. From this perspective, $$f'(x)$$ can be regarded as one of the pieces of local information that $$x$$ carries.
