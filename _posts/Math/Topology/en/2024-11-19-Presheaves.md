---
title: "Presheaves"
description: "This post introduces the notion of a presheaf as a contravariant functor assigning collections of continuous functions corresponding to open sets of a topological space, and discusses the conditions for extending continuous functions on a family of subsets to the whole space via the gluing lemma."
excerpt: "The gluing lemma and the definition of a presheaf"

categories: [Math / Topology]
permalink: /en/math/topology/presheaves
sidebar: 
    nav: "topology-en"

date: 2024-11-19
weight: 8
translated_at: 2026-06-03T06:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-09T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Gluing lemma

[§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8){: data-lid="o5hv3" }, which we saw earlier, states that given a continuous function $f:X \rightarrow Y$, its restriction to a family of subsets satisfying one of the two conditions in [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6){: data-lid="ifhee" } is continuous. In particular, these conditions correspond to the following two cases:

1. $(A_i)$ is an open covering of $X$, or
2. $(A_i)$ is a locally finite closed covering of $X$.

Conversely, given $(A_i)$ satisfying such conditions and continuous functions $f_i$ defined on them, we may consider whether they determine a continuous function on $X=\bigcup A_i$.

::: Lemma 1
Let $X$ be a topological space, and let $(A_i)$ be a family of subsets satisfying one of the two conditions in [§Subspaces, ⁋Proposition 6](/en/math/topology/subspaces#prop6){: data-lid="btg09" }. If a family of continuous functions $(f_i: A_i \rightarrow Y)$ satisfies the condition

$$f_i\vert_{A_i\cap A_j}=f_j\vert_{A_i\cap A_j}\qquad\text{for all $i,j$}$$

then the function $f:X \rightarrow Y$ obtained by extending them is continuous.
:::
::: Proof
First, the function $f$ is obtained from [\[Set Theory\] §Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2){: data-lid="jm8pb" }. That this function is continuous follows from [§Subspaces, ⁋Proposition 8](/en/math/topology/subspaces#prop8){: data-lid="xv91t" }.
:::

## Presheaves of continuous functions

The structures examined in many parts of mathematics, especially in geometry, are structures where additional data is given on a topological space. For these, tools to handle the process above are needed.

Let us define the category $\Open(X)$ as the ordered set $(\mathcal{T}, \subseteq)$ viewed as a category. That is, its objects are open sets, and whenever $U\subseteq V$, there exists a unique arrow $U\hookrightarrow V$.

::: Definition 2
For a topological space $X$, a contravariant functor $\mathcal{F}:\Open(X) \rightarrow \Set$ is called a *presheaf* of sets defined on $X$.
:::

As a side note, presheaves are commonly denoted by $\mathcal{F}$ or $\mathcal{F}$, but between the two, the calligraphic $\mathcal{F}$ is slightly more natural. However, since we are already using this font to denote topological structures, we decide to use the script font within the topology category.

Now, since $\mathcal{F}$ is contravariant, whenever an inclusion $U\hookrightarrow V$ between open sets is given, a morphism $\rho_{VU}: \mathcal{F}(V)\rightarrow \mathcal{F}(U)$ is given, and since $\mathcal{F}$ preserves composition, if $U\hookrightarrow V\hookrightarrow W$ is given, then $\rho_{WU}=\rho_{VU}\circ\rho_{WV}$ must hold.

::: Example 3
Suppose two topological spaces $X, Y$ are given, and define $\mathcal{F}$ as follows.

- For any open set $U$, $\mathcal{F}(U)=\Hom_\Top(U, Y)$.
- When open sets $U\subseteq V$ are given, $\rho_{VU}:\mathcal{F}(V) \rightarrow \mathcal{F}(U)$ is the restriction map restricting a continuous function defined on $V$ to $U$.

Then $\mathcal{F}$ becomes a presheaf.
:::

In particular, this definition can be applied when a projection $p:Y \rightarrow X$ is given, by associating to each open set $U$ the collection, defined on $U$, of continuous sections of $p$ ([\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2){: data-lid="vr0o9" }), so as to consider a presheaf $\mathcal{F}$. Generalizing this, we make the following definition.

::: Definition 4
Given a topological space $X$, let $\mathcal{F}$ be a presheaf defined on it. 

- For any open set $U\subseteq X$, the elements of $\mathcal{F}(U)$ are called *sections* over $U$. In particular, the elements of $\mathcal{F}(X)$ are called *global sections*.
- For open sets $U\subseteq V$, the map $\rho_{VU}:\mathcal{F}(V) \rightarrow \mathcal{F}(U)$ is called the *restriction map* from $V$ to $U$. 
- In particular, for open sets $U\subseteq V$ and $s\in \mathcal{F}(V)$, we write $\rho_{VU}(s)\in \mathcal{F}(U)$ simply as $s\vert_U$.
:::

Meanwhile, in [Definition 2](#def2){: data-lid="yvxpx" } above, $\Set$ can also be replaced by an appropriate category, such as $\Ab$. For instance, in [Example 3](#ex3){: data-lid="tjnzz" }, if $Y=\mathbb{R}$, we could use the addition defined on $\mathbb{R}$ to define addition of continuous functions, and then $\mathcal{F}(U)$ would carry the structure of an abelian group. In such a case, $\mathcal{F}$ is called a presheaf of abelian groups defined on $X$. For convenience, from now on we shall call a presheaf $\mathcal{F}: \Open(X)^\op \rightarrow \mathcal{A}$ an $\mathcal{A}$-valued presheaf. Among presheaves, those satisfying the gluing condition of [Lemma 1](#lem1){: data-lid="9yqhp" } above are called sheaves; these will be defined in the next post. 

## Examples of presheaves

Next, we examine several examples of presheaves. 

::: Example 5 (Skyscraper sheaf)
Suppose a fixed topological space $X$ and a point $i_x:\{x\}\hookrightarrow X$ are given, and fix an object $A\in \mathcal{A}$. Then defining

$$(i_x)_\ast A(U)=\begin{cases}A&\text{if $x\in U$,}\\T&\text{if $x\not\in U$,}\end{cases}\qquad \text{$T$ a terminal object in $\mathcal{A}$}$$

and giving the restriction maps as $\id_A$ or via the terminal object $T$, this defines a presheaf. This is called the *skyscraper sheaf*.
:::

::: Example 6 (Constant presheaf)
This time, fix a topological space $X$ and an object $A\in \mathcal{A}$, assign $A$ to every open set, and let all restriction maps be $\id_A$. Then this defines a presheaf, called the *constant presheaf*. 
:::

The following examples show ways to obtain new presheaves from an arbitrary presheaf. 

::: Example 7
On $X$, given a presheaf $\mathcal{F}$, for any open set $U$ we can define $\mathcal{F}\vert_U$ by

$$\mathcal{F}\vert_U(V)=\mathcal{F}(V)\quad\text{for all open $V\subseteq U$}$$

Then $\mathcal{F}\vert_U$ is a presheaf. ([§Subspaces, ⁋Lemma 2](/en/math/topology/subspaces#lem2){: data-lid="9cnyb" }) 
:::

::: Example 8 (Pushforward)
Fix a continuous function $f:X \rightarrow Y$, and suppose that on $X$, a presheaf $\mathcal{F}$ is given. Then the *pushforward* of $\mathcal{F}$ along $f$, $f_\ast \mathcal{F}$, is defined by

$$f_\ast \mathcal{F}(U)=\mathcal{F}(f^{-1}(U))$$
:::

## Stalks

Meanwhile, what determines a function defined on $X$ is of course its value at $x\in X$. What distinguishes this from a function defined on $X$ as a set is that, due to the topological structure defined on $X$, we can also examine what happens in a neighborhood of this point $x$. Based on this intuition, we define the following.

::: Definition 9
On a topological space $X$, consider a presheaf $\mathcal{F}$. For any point $x\in X$, the *stalk* at $x$, $\mathcal{F}_x$, is defined by

$$\mathcal{F}_x=\varinjlim_{x\in U}\mathcal{F}(U)$$

The elements of $\mathcal{F}_x$ are called *germs* at $x$.
:::

In particular, if $\mathcal{F}$ is a cocomplete category valued presheaf, then $\mathcal{F}_x$ is always well-defined. Meanwhile, writing out the expression for the colimit directly in a concrete category, we have

$$\mathcal{F}_x=\{(s,U)\mid x\in U\in\mathcal{T},s\in\mathcal{F}(U)\}/\mathnormal{\sim}$$

where the equivalence relation $\sim$ is defined by

$$(s,U)\sim(t,V)\iff\text{$\exists$ open neighborhood $W\subseteq U\cap V$ of $x$ satisfying $\rho_{UW}(s)=\rho_{VW}(t)$}$$

That is, intuitively, the elements of $\mathcal{F}_x$, $(s,U)$, can be thought of as objects that have the function value at $x$, $s(x)$, and additionally possess, near $x$, local information[^1] about $s$. For convenience, for any $s\in \mathcal{F}(U)$, we write the image of $s$ under $\mathcal{F}(U) \rightarrow \mathcal{F}_x$ as $s_x$.

For now, a presheaf can be said to be an object with additional algebraic information rather than a geometric object, but it is also possible to make it into a geometric one. On a topological space $X$, consider a presheaf $\mathcal{F}$, and consider the following set

$$\Spe(\mathcal{F})=\coprod_{x\in X} \mathcal{F}_x=\{(x,\xi)\mid x\in X, \xi\in \mathcal{F}_x\}$$

Then for any open set $U\subseteq X$ and any $s\in \mathcal{F}(U)$, the following functions 
 
$$\tilde{s}:U \rightarrow \Spe(\mathcal{F}); \quad x\mapsto (x,s_x)$$

exist. Now we endow $\Spe(\mathcal{F})$ with the final topology defined by this family of functions ([§Initial and Final Topology, ⁋Definition 4](/en/math/topology/initial_and_final_topology#def4){: data-lid="ywi2i" }), and call this space the *étalé space* of $\mathcal{F}$.

## Morphisms of presheaves

::: Definition 10
On a fixed topological space $X$, a natural transformation between two presheaves $\mathcal{F}, \mathcal{G}:\Open(X) \rightarrow \mathcal{A}$ is defined as a *presheaf morphism*.
:::

That is, the category of presheaves on $X$ valued in $\mathcal{A}$ is the functor category $[\Open(X)^\op, \mathcal{A}]$. We denote this by $\PSh(X; \mathcal{A})$, and when there is no risk of confusion from context, we simply write $\PSh(X)$. As a side note, the $f_\ast$ from [Example 8](#ex8){: data-lid="9024c" } is a functor $\PSh(X; \mathcal{A})\rightarrow \PSh(Y; \mathcal{A})$.

Thinking of [Example 3](#ex3){: data-lid="sr494" }, which provides us with intuition, for an open set $U$, the map $\phi(U):\mathcal{F}(U) \rightarrow \mathcal{G}(U)$ can be thought of as the function obtained by restricting $\phi:\mathcal{F}\rightarrow \mathcal{G}$ to the open set $U$, so instead of $\phi(U)$, we often write $\phi\vert_U$.

Meanwhile, by the universal property of the colimit cone, the following proposition holds.

::: Proposition 11
On a topological space $X$, let $\phi:\mathcal{F}\rightarrow\mathcal{G}$ be a morphism between presheaves. Then for any $x\in X$, a morphism $\phi_x:\mathcal{F}_x\rightarrow\mathcal{G}_x$ between stalks is naturally induced.
:::

The following examples should have appeared under [Examples of presheaves](#examples-of-presheaves){: data-lid="mjdmf" } above, but were postponed because we had not yet defined presheaf morphisms.

::: Example 12 (Sheaf Hom)
Fix two presheaves $\mathcal{F}, \mathcal{G}$, and for any $U$, define

$$\sHom(\mathcal{F},\mathcal{G})(U)=\Hom_{\PSh(U)}(\mathcal{F}\vert_U, \mathcal{G}\vert_U)$$
:::

::: Example 13 (Product)
On a topological space $X$, for a family of presheaves $(\mathcal{F}_i:\Open(X) \rightarrow \Set)_{i\in I}$, their product $\prod_{i\in I} \mathcal{F}_i$ can be defined by

$$\left(\prod_{i\in I} \mathcal{F}_i\right)(U)=\prod_{i\in I} \mathcal{F}_i(U)$$
:::

Using definitions such as the above, structures defined in a category $\mathcal{A}$ (for example products, coproducts, limits, colimits, monoidal products, etc.) can be transferred to $\PSh(X; \mathcal{A})$. In particular, $\PSh(X; \Ab)$ inherits the monoidal structure defined on $\Ab$, $(\Ab,\otimes, \mathbb{Z})$, and the category of monoid objects here is $\PSh(X; \Ring)$. In the same vein, the following example can be understood.

::: Example 14
On a topological space $X$, for a $\Ring$-valued presheaf $\mathcal{O}_X$, a left $\mathcal{O}_X$-module object $\mathcal{F}\in\PSh(X;\Ab)$ is simply called an $\mathcal{O}_X$-module.
:::

## Abelian presheaves

Until now we have ignored the category in which a presheaf takes values; now we specifically examine presheaves taking values in the category $\Ab$.

::: Definition 15
For a topological space $X$, a contravariant functor $\Open(X)\rightarrow\Ab$ is called an *abelian presheaf*.
:::

::: Definition 16
On a topological space $X$, let $\phi:\mathcal{F}\rightarrow\mathcal{G}$ be a morphism between abelian presheaves. Then the *presheaf kernel* of $\phi$, $\ker\phi$, is the data consisting of:

- For each open set $U\subseteq X$, $U\mapsto \ker(\phi(U))$;
- For any two open sets $U\subseteq V$ in an inclusion relation, the restriction map $\rho_{VU}:\ker(\phi(V))\rightarrow\ker(\phi(U))$ uniquely determined by the following diagram:
  
  {% diagram Math/Topology/Presheaves-1.svg width="20.39em" alt="presheaf_kernel-1" %}
:::

In this definition, $\rho_{VU}$ is the restriction map uniquely determined by the universal property of $\ker(\phi(U))$.

::: Lemma 17
The $\ker\phi$ defined above is an (abelian) presheaf on $X$.
:::
::: Proof
By the following diagram

{% diagram Math/Topology/Presheaves-2.svg width="21.30em" alt="presheaf_kernel-2" %}

and the universal property of the kernel, for open sets $U\subseteq V\subseteq W$, both $\rho_{VU}\circ\rho_{WV}$ and $\rho_{WU}$ are morphisms factoring the composite $\ker\phi(W) \rightarrow \mathcal{F}(W) \rightarrow \mathcal{F}(U)$ through $\ker\phi(U)$, and hence they are equal to each other by uniqueness.
:::

In the same way, one can define the *presheaf cokernel*, *presheaf image*, *presheaf coimage*, *presheaf quotient*, and so on. Here, addition is given on each open set, and the morphism from the coimage to the image is also an isomorphism on each open set, so on a given topological space $X$, the category $\PSh(X;\Ab)$ of abelian presheaves becomes an abelian category.
  
---
**References**

**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/). 

---

[^1]: For example, if $X=\mathbb{R}$, then in $\mathbb{R}$, to define the derivative at a point $x$, it suffices to know, in an arbitrarily small neighborhood of $x$, only the values of $f$. In this respect, $f'(x)$ can be said to be one of the pieces of local information that $x$ carries.
