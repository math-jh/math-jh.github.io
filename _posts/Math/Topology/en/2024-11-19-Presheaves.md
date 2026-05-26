---
title: "Presheaves"
excerpt: "The gluing lemma and the definition of a presheaf"

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
translated_at: 2026-05-25T06:30:01+00:00
translation_source: kimi-cli
---
## Gluing lemma

As we saw in [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8), if a continuous function $$f:X \rightarrow Y$$ is given, then its restriction to any family of subsets satisfying one of the two conditions from [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6) is continuous. In particular, these conditions correspond to the following two cases:

1. $$(A_i)$$ is an open covering of $$X$$, or
2. $$(A_i)$$ is a locally finite closed covering of $$X$$.

Conversely, given a family $$(A_i)$$ satisfying such a condition and continuous functions $$f_i$$ defined on them, we may ask whether they specify a continuous function on $$X=\bigcup A_i$$.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> Let a set $$X$$ and a family of subsets $$(A_i)$$ satisfying one of the two conditions from [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6) be given. If a family of continuous functions $$(f_i: A_i \rightarrow Y)$$ satisfies the condition

$$f_i\vert_{A_i\cap A_j}=f_j\vert_{A_i\cap A_j}\qquad\text{for all $i,j$}$$

then the function $$f:X \rightarrow Y$$ obtained by extending them is continuous.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the function $$f$$ is obtained by [\[Set Theory\] §Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2). Its continuity follows from [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8).

</details>

## Presheaves of continuous functions

Many structures studied in mathematics, especially in geometry, are structures obtained by equipping a topological space with additional data. To handle these, we need tools that deal with processes like the one above.

Define the category $$\Open(X)$$ as the ordered set $$(\mathcal{T}, \subseteq)$$ viewed as a category. That is, its objects are open sets, and whenever $$U\subseteq V$$ there exists a unique arrow $$U\hookrightarrow V$$.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For a topological space $$X$$, a contravariant functor $$\mathscr{F}:\Open(X)^\op \rightarrow \Set$$ defined on $$X$$ is called a *presheaf* of sets on $$X$$.

</div>

By the way, presheaves are commonly denoted by $$\mathcal{F}$$ or $$\mathscr{F}$$; between these, the calligraphic $$\mathcal{F}$$ is slightly more natural. However, since we are already using this font to denote topological structures, we shall use the script font in the topology category.

Now since $$\mathscr{F}$$ is contravariant, whenever an inclusion $$U\hookrightarrow V$$ of open sets is given, a morphism $$\rho_{VU}: \mathscr{F}(V)\rightarrow \mathscr{F}(U)$$ is given, and since $$\mathscr{F}$$ preserves composition, if $$U\hookrightarrow V\hookrightarrow W$$ is given then $$\rho_{WU}=\rho_{VU}\circ\rho_{WV}$$ must hold.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Let two topological spaces $$X, Y$$ be given, and define $$\mathscr{F}$$ as follows.

- For any open set $$U$$, $$\mathscr{F}(U)=\Hom_\Top(U, Y)$$.
- When open sets $$U\subseteq V$$ are given, $$\rho_{VU}:\mathscr{F}(V) \rightarrow \mathscr{F}(U)$$ is the restriction map that restricts a continuous function defined on $$V$$ to $$U$$.

Then $$\mathscr{F}$$ is a presheaf.

</div>

In particular, this definition can be applied when a projection $$p:Y \rightarrow X$$ is given, by considering the collection of continuous sections from $$X$$ to $$Y$$ ([\[Set Theory\] §Retractions and Sections, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2)) as a presheaf $$\mathscr{F}$$. Generalizing this, we make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let a presheaf $$\mathscr{F}$$ defined on a topological space $$X$$ be given.

- For any open set $$U\subseteq X$$, the elements of $$\mathscr{F}(U)$$ are called *sections* over $$U$$. In particular, the elements of $$\mathscr{F}(X)$$ are called *global sections*.
- For open sets $$U\subseteq V$$, the map $$\rho_{VU}:\mathscr{F}(V) \rightarrow \mathscr{F}(U)$$ is called the *restriction map* from $$V$$ to $$U$$.
- In particular, for open sets $$U\subseteq V$$ and $$s\in \mathscr{F}(V)$$, we write $$\rho_{UV}(f)\in \mathscr{F}(U)$$ simply as $$s\vert_U$$.

</div>

Meanwhile, in [Definition 2](#def2) above, $$\Set$$ may be replaced by an appropriate category, for example $$\Ab$$. For instance, if in [Example 3](#ex3) we had $$Y=\mathbb{R}$$, then we could have defined addition of continuous functions using the addition defined on $$\mathbb{R}$$, and then $$\mathscr{F}(U)$$ would have had the structure of an abelian group. In this case we call $$\mathscr{F}$$ a presheaf of abelian groups on $$X$$. For convenience, from now on we shall call a presheaf $$\mathscr{F}: \Open(X)^\op \rightarrow \mathcal{A}$$ an $$\mathcal{A}$$-valued presheaf. Among presheaves, those satisfying the gluing condition above ([Lemma 1](#lem1)) are called sheaves; we define these in the next post.

## Examples of presheaves

Next we examine several examples of presheaves.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Skyscraper sheaf)**</ins> Let a fixed topological space $$X$$ and a point $$i_x:\{x\}\hookrightarrow X$$ be given, and fix an object $$A\in \mathcal{A}$$. Then defining

$$(i_x)_\ast A(U)=\begin{cases}A&\text{if $x\in U$,}\\T&\text{if $x\not\in U$,}\end{cases}\qquad \text{$T$ a terminal object in $\mathcal{A}$}$$

and giving the restriction map as $$\id_A$$ or using the terminal object $$T$$ defines a presheaf. This is called a *skyscraper sheaf*.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6 (Constant presheaf)**</ins> Now fix a topological space $$X$$ and an object $$A\in \mathcal{A}$$, and assign $$A$$ to every open set with all restriction maps given as $$\id_A$$. Then this defines a presheaf, called the *constant presheaf*.

</div>

The following examples show methods of obtaining new presheaves from arbitrary presheaves.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> When a presheaf $$\mathscr{F}$$ defined on $$X$$ is given, for any open set $$U$$ we can define $$\mathscr{F}\vert_U$$ by the formula

$$\mathscr{F}\vert_U(V)=\mathscr{F}(V)\quad\text{for all open $V\subseteq U$}$$

Then $$\mathscr{F}\vert_U$$ is a presheaf. ([§Subspaces, ⁋Lemma 2](/en/math/topology/subspaces#lem2))

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8 (Pushforward)**</ins> Fix a continuous function $$f:X \rightarrow Y$$, and let a presheaf $$\mathscr{F}$$ defined on $$X$$ be given. Then the *pushforward* $$f_\ast \mathscr{F}$$ of $$\mathscr{F}$$ along $$f$$ is defined by the formula

$$f_\ast \mathscr{F}(U)=\mathscr{F}(f^{-1}(U))$$

</div>

## Stalks

Of course, what determines a function defined on $$X$$ is its value at each point $$x\in X$$. What distinguishes this from a function on $$X$$ as a set is that, due to the topological structure defined on $$X$$, we can also examine what happens in a neighborhood of this point $$x$$. Based on this intuition, we define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Consider a presheaf $$\mathscr{F}$$ defined on a topological space $$X$$. For any point $$x\in X$$, the *stalk* $$\mathscr{F}_x$$ at the point $$x$$ is defined by

$$\mathscr{F}_x=\varinjlim_{x\in U}\mathscr{F}(U)$$

The elements of $$\mathscr{F}_x$$ are called *germs* at the point $$x$$.

</div>

In particular, if $$\mathscr{F}$$ is a complete category valued presheaf, then $$\mathscr{F}_x$$ is always well-defined. Meanwhile, directly expressing the limit in a concrete category gives

$$\mathscr{F}_x=\{(s,U)\mid x\in U\in\mathscr{T},s\in\mathscr{F}(U)\}/\mathnormal{\sim}$$

where the equivalence relation $$\sim$$ is defined by

$$(s,U)\sim(t,V)\iff\text{$\exists$ open neighborhood $W\subseteq U\cap V$ of $x$ satisfying $\rho_{UW}(s)=\rho_{VW}(t)$}$$

That is, intuitively the elements $$(s,U)$$ of $$\mathscr{F}_x$$ can be thought of as objects that carry not only the function value $$s(x)$$ at $$x$$ but also additional local information[^1] of $$s$$ in a neighborhood of $$x$$. For convenience, for any $$s\in \mathscr{F}(U)$$, we write the image of $$s$$ under $$\mathscr{F}(U) \rightarrow \mathscr{F}_x$$ as $$s_x$$.

For now, a presheaf is more an object with additional algebraic information than a geometric one, but it is possible to make it into a geometric object. Consider a topological space $$X$$ and a presheaf $$\mathscr{F}$$ defined on it, and consider the set

$$\Spe(\mathscr{F})=\coprod_{x\in X} \mathscr{F}_x=\{(x,\xi)\mid x\in X, \xi\in \mathscr{F}_x\}$$

Then for any open set $$U\subseteq X$$ and any $$s\in \mathscr{F}(U)$$, the functions

$$\tilde{s}:U \rightarrow \Spe(\mathscr{F}); \quad x\mapsto (x,s_x)$$

exist. Now we endow $$\Spe(\mathscr{F})$$ with the final topology defined by this family of functions ([§Initial and Final Topologies, ⁋Definition 4](/en/math/topology/initial_and_final_topology#def4)) and call this space the *étalé space* of $$\mathscr{F}$$.

## Morphisms of presheaves

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A natural transformation between two presheaves $$\mathscr{F}, \mathscr{G}:\Open(X) \rightarrow \mathcal{A}$$ defined on a fixed topological space $$X$$ is called a *presheaf morphism*.

</div>

That is, the category of $$\mathcal{A}$$-valued presheaves defined on $$X$$ is the functor category $$[\Open(X)^\op, \mathcal{A}]$$. We denote this by $$\PSh(X, \mathcal{A})$$, and when there is no risk of confusion from context, we may write simply $$\PSh(X)$$. Incidentally, the $$f_\ast$$ from [Example 8](#ex8) is a functor $$\PSh(X, \mathcal{A})\rightarrow \PSh(Y, \mathcal{A})$$.

Thinking of the intuitive [Example 2](#ex2), for an open set $$U$$ the map $$\phi(U):\mathscr{F}(U) \rightarrow \mathscr{G}(U)$$ can be thought of as the function obtained by restricting $$\phi:\mathscr{F}\rightarrow \mathscr{G}$$ to the open set $$U$$, so we sometimes write $$\phi\vert_U$$ instead of $$\phi(U)$$.

Meanwhile, the following proposition holds by the universal property of the limit cone.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Let a morphism $$\phi:\mathscr{F}\rightarrow\mathscr{G}$$ between presheaves defined on a topological space $$X$$ be given. Then for any $$x\in X$$, a morphism $$\phi_x:\mathscr{F}_x\rightarrow\mathscr{G}_x$$ between stalks is naturally induced.

</div>

The following examples should have been placed under [Examples of Presheaves](#examples-of-presheaves) above, but were deferred because we had not yet defined presheaf morphisms.

<div class="example" markdown="1">

<ins id="ex12">**Example 12 (Sheaf Hom)**</ins> Fix two presheaves $$\mathscr{F}, \mathscr{G}$$ and define for any $$U$$

$$\mathscr{Hom}(\mathscr{F},\mathscr{G})(U)=\Hom_{\PSh(U)}(\mathscr{F}\vert_U, \mathscr{G}\vert_U)$$

</div>

<div class="example" markdown="1">

<ins id="ex13">**Example 13 (Product)**</ins> For a family of presheaves $$(\mathscr{F}_i:\Open(X) \rightarrow \Set)_{i\in I}$$ defined on a topological space $$X$$, we can define their product $$\prod_{i\in I} \mathscr{F}_i$$ by

$$\left(\prod_{i\in I} \mathscr{F}_i\right)(U)=\prod_{i\in I} \mathscr{F}_i(U)$$

</div>

Using definitions like the above, we can lift structures defined in a category $$\mathcal{A}$$, such as products, coproducts, limits, colimits, monoidal products, etc., to $$\PSh(X, \mathcal{A})$$. In particular, $$\PSh(X, \Ab)$$ inherits the monoidal structure $$(\Ab,\otimes, \mathbb{Z})$$ defined on $$\Ab$$, and the monoidal objects here are $$\PSh(X, \Ring)$$. In the same vein, the following example can be understood.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> For a $$\Ring$$-valued presheaf $$\mathscr{O}_X$$ defined on a topological space $$X$$, we simply call a left $$\mathscr{O}_X$$-module object $$\mathscr{F}\in\PSh(X,\Ab)$$ an $$\mathscr{O}_X$$-module.

</div>

## Abelian presheaves

Until now we have ignored which category a presheaf takes values in; now we examine presheaves taking values in the category $$\Ab$$ in particular.

<div class="definition" markdown="1">

<ins id="def15">**Definition 15**</ins> For a topological space $$X$$, a contravariant functor $$\Open(X)\rightarrow\Ab$$ is called an *abelian presheaf*.

</div>

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> Let a morphism $$\phi:\mathscr{F}\rightarrow\mathscr{G}$$ between abelian presheaves defined on a topological space $$X$$ be given. Then the *presheaf kernel* $$\ker\phi$$ of $$\phi$$ is the data consisting of:

- For each open set $$U\subseteq X$$, the assignment $$U\mapsto \ker(\phi(U))$$
- For each pair of open sets $$U\subseteq V$$, the restriction map $$\rho_{VU}:\ker(\phi(V))\rightarrow\ker(\phi(U))$$ uniquely determined by the following diagram

  ![presheaf_kernel-1](/assets/images/Math/Topology/Presheaves-1.png){:style="width:18em" class="invert" .align-center}

</div>

In this definition, $$\rho_{VU}$$ is the restriction map uniquely determined by the universal property of $$\ker(\phi(U))$$.

<div class="proposition" markdown="1">

<ins id="lem17">**Lemma 17**</ins> The $$\ker\phi$$ defined above is an (abelian) presheaf on $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious from the following diagram

![presheaf_kernel-2](/assets/images/Math/Topology/Presheaves-2.png){:style="width:18em" class="invert" .align-center}

and the universal property of the kernel.

</details>

In the same manner, we can define *presheaf cokernel*, *presheaf image*, *presheaf coimage*, *presheaf quotient*, and so on. Therefore the category $$\PSh(X,\Ab)$$ of abelian presheaves defined on a given topological space $$X$$ is an abelian category.

---
**References**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---

[^1]: For example, if $$X=\mathbb{R}$$, then to define the derivative of $$\mathbb{R}$$ at a point $$x$$ it suffices to know the values of $$f$$ in a very small neighborhood of $$x$$. From this point of view, $$f'(x)$$ can be said to be one of the pieces of local information that $$x$$ carries.
