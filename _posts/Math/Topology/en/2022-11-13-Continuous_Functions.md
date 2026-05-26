---
title: "Continuous Functions"
excerpt: "Properties of continuous functions"

categories: [Math / Topology]
permalink: /en/math/topology/continuous_functions
header:
    overlay_image: /assets/images/Math/Topology/Continuous_Functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-en"

date: 2022-11-13
last_modified_at: 2022-11-13
weight: 5
translated_at: 2026-05-23T01:30:01+00:00
translation_source: kimi-cli
---
## Continuous Functions

Now we define the notion of continuous functions. Intuitively, one can think of this as a function preserving topological structure, just as a homomorphism does in an algebraic setting.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A function $$f:X\rightarrow Y$$ between arbitrary topological spaces $$X$$ and $$Y$$ is *continuous* at $$x\in X$$ if for any neighborhood $$V$$ of $$f(x)\in Y$$, there exists a neighborhood $$U$$ of $$x$$ such that $$f(U)\subseteq V$$.

</div>

Since $$U\subseteq f^{-1}(f(U))$$ holds for any function $$f:X\rightarrow Y$$ between arbitrary sets $$X$$, $$Y$$ and any $$U\subseteq X$$, if an arbitrary set $$V\subseteq Y$$ satisfies $$f(U)\subseteq V$$, then

$$U\subseteq f^{-1}(f(U))\subseteq f^{-1}(V)$$

holds. Therefore, to prove that a function $$f:X\rightarrow Y$$ between two topological spaces is continuous at $$x\in X$$, it suffices to show that for any neighborhood $$V$$ of $$f(x)\in Y$$, $$f^{-1}(V)$$ is a neighborhood of $$x$$; more generally, it suffices to show that for a fixed local base $$\mathcal{B}(f(x))$$ of $$f(x)$$ and any $$V\in\mathcal{B}(f(x))$$, we have $$f^{-1}(V)\in\mathcal{N}(x)$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$f:X\rightarrow Y$$ be a function between two topological spaces $$X$$ and $$Y$$ that is continuous at a point $$x$$. If $$x\in\cl(A)$$ for some $$A\subseteq X$$, then $$f(x)\in\cl(A)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$V$$ be an arbitrary neighborhood of $$f(x)\in Y$$. Then $$f^{-1}(V)$$ is a neighborhood of $$x$$, so $$f^{-1}(V)\cap A\neq\emptyset$$ ([§Interior, Closure, and Boundary of Sets, ⁋Proposition 6](/en/math/topology/other_concepts#prop6)). If we let $$x'\in f^{-1}(V)\cap A$$, then $$f(x')\in V\cap f(A)$$. In particular, $$V\cap f(A)\neq\emptyset$$, so applying [§Interior, Closure, and Boundary of Sets, ⁋Proposition 6](/en/math/topology/other_concepts#prop6) again, we see that $$f(x)\in\cl(A)$$.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let topological spaces $$X$$, $$Y$$, $$Z$$ be given. If $$f:X\rightarrow Y$$ is continuous at a point $$x\in X$$ and $$g:Y\rightarrow Z$$ is continuous at $$f(x)$$, then their composition $$g\circ f$$ is also continuous.
</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$W$$ be an arbitrary neighborhood of $$(g\circ f)(x)$$. Then since $$g$$ is continuous at $$f(x)$$, $$g^{-1}(W)$$ is a neighborhood of $$f(x)$$. Again, since $$f$$ is continuous at $$x$$, $$f^{-1}(g^{-1}(W))$$ is a neighborhood of $$x$$. ([\[Set Theory\] §Operations of Binary Relations, ⁋Proposition 13](/en/math/set_theory/operation_of_binary_relations#prop6))

</details>

If $$f$$ is continuous at every point of $$X$$, we call $$f$$ a *continuous function*. The following theorem shows several equivalent ways to define continuous functions.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4**</ins> For two topological spaces $$X$$, $$Y$$ and a function $$f:X\rightarrow Y$$, the following are all equivalent.

1. $$f$$ is continuous.
2. For any subset $$A$$ of $$X$$, $$f(\cl A)\subset\cl f(A)$$ holds.
3. For any closed set $$C$$ of $$Y$$, $$f^{-1}(C)$$ is a closed set in $$X$$.
4. For any open set $$V$$ of $$Y$$, $$f^{-1}(V)$$ is an open set in $$X$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the first condition implies the second is a consequence of [Proposition 2](#prop2).

Now assume the second condition and show the third. For any closed set $$C$$ of $$Y$$, the inclusion

$$f(\cl(f^{-1}(C))\subseteq \cl(f(f^{-1}(C))\subseteq\cl(C)=C$$

holds, so from

$$\cl(f^{-1}(C))\subseteq f^{-1}(f(\cl(f^{-1}(C)))\subseteq f^{-1}(C)$$

we see that $$f^{-1}(C)$$ is a closed set. Since the identity $$(f^{-1}(A))^c=f^{-1}(A^c)$$ holds for any subset $$A\subseteq Y$$, it is obvious that the fourth condition follows as well.

Thus it suffices to assume the fourth condition and prove the first. Choose $$x\in X$$ arbitrarily, and let $$V$$ be any neighborhood of $$f(x)\in Y$$. Then there exists an <em-ko>open neighborhood</em-ko> $$V'$$ of $$f(x)$$ satisfying $$f(x)\subseteq V'\subseteq V$$. Now from the fourth condition, $$f^{-1}(V')$$ is an open neighborhood of $$x\in X$$, and from $$f^{-1}(V')\subseteq f(V)$$ we see that $$f(V)$$ becomes a neighborhood of $$x$$.

</details>

By [Proposition 3](#prop3), if two continuous functions $$f:X\rightarrow Y$$, $$g:Y\rightarrow Z$$ are given, we know that $$g\circ f$$ is also continuous.

Let a continuous function $$f:X\rightarrow Y$$ between two topological spaces $$(X,\mathcal{T}_X)$$, $$(Y,\mathcal{T}_Y)$$ be given. Then since $$f^{-1}(V)\in\mathcal{T}_X$$ holds for any $$V\in\mathcal{T}_Y$$, the formula

$$f^\mathcal{T}(V):=f^{-1}(V),\qquad V\in\mathcal{T}_Y$$

well-defines a function $$f^\mathcal{T}:\mathcal{T}_Y\rightarrow\mathcal{T}_X$$.

Now assume $$f$$ is a bijection and consider two distinct elements $$V_1$$, $$V_2$$ of $$\mathcal{T}_Y$$. Without loss of generality, if $$y\in V_1\setminus V_2$$, then

$$f^{-1}(y)\in f^\mathcal{T}(V_1)\setminus f^\mathcal{T}(V_2)$$

holds, so $$f^{\mathcal{T}}$$ is injective.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> In general, $$f^{\mathcal{T}}$$ need not be surjective. For example, let $$X_1$$ be the space $$\mathbb{N}$$ with the discrete topology $$\mathcal{T}_1$$, and $$X_2$$ be the space with the trivial topology $$\mathcal{T}_2$$; then considering the identity function $$\id:\mathbb{N}\rightarrow\mathbb{N}$$ as a set map, $$\id$$ is a continuous bijection but the function

$$\id^\mathcal{T}:\mathcal{T}_2\rightarrow\mathcal{T}_1$$

cannot be surjective. ([\[Set Theory\] §Operations of Cardinals, ⁋Proposition 10](/en/math/set_theory/operation_of_cardinals#prop10))

</div>

However, if the inverse function $$f^{-1}$$ of a bijection $$f$$ is also continuous, then $$(f^{-1})^\mathcal{T}:\mathcal{T}_X\rightarrow\mathcal{T}_Y$$ is well-defined, and from the definition it is obvious that

$$f^\mathcal{T}\circ (f^{-1})^\mathcal{T}=\id_{\mathcal{T}_X},\qquad (f^{-1})^\mathcal{T}\circ f^\mathcal{T}=\id_{\mathcal{T}_Y}$$

so $$f^\mathcal{T}$$ is also bijective. We define such a situation as follows.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A continuous function $$f:X\rightarrow Y$$ is a *homeomorphism* if there exists another continuous function $$g:Y\rightarrow X$$ such that $$f\circ g=\id_Y$$ and $$g\circ f=\id_X$$.

</div>

That is, two topological spaces $$X$$ and $$Y$$ are homeomorphic means not only that there exists a bijection between them as sets, but also that this bijection acts on the topological structures of the two sets, i.e., on their open sets, in exactly the same way. An example of a continuous bijection that is not a homeomorphism is precisely [Example 5](#ex5) above.

---

**References**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
