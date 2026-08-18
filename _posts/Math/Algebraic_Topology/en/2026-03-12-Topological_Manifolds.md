---
title: "Topological Manifolds"
description: "We examine the definition and properties of topological manifolds, and discuss examples of spaces satisfying second countability, Hausdorff, and locally Euclidean conditions."
excerpt: "Definition and properties of topological manifolds as locally Euclidean spaces"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/topological_manifolds
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-07-05
weight: 1
translated_at: 2026-08-18T12:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T12:45:05+00:00
---
We discuss homology, cohomology, and other concepts essential to the study of geometry in this category. Although these notions are defined on general topological spaces, they behave well only when the space satisfies additional properties; a space meeting all such requirements is precisely the topological manifold defined below. In this post we examine the properties and examples of topological manifolds, and in the next post we sketch what homology is through some examples. These two posts outline the broad direction of this category; the serious content begins with the third.

## Definition of a Topological Manifold

A topological manifold is defined as follows.

::: Definition 1
A topological space $M$ is *locally Euclidean of dimension $m$* if for every $x\in M$ there exists an open neighborhood $U$ of $x$ such that $U$ is homeomorphic to an open subset of $\mathbb{R}^m$.
:::

::: Definition 2
A space that is second countable, Hausdorff, and locally Euclidean of dimension $m$ is called a *topological manifold of dimension $m$*.
:::

For convenience, we call a topological manifold of dimension $m$ an *$m$-manifold*. Although [Definition 1](#def1) does not treat this, we sometimes replace $\mathbb{R}^m$ in the above definition by the *half-space*

$$\mathbb{H}^m=\left\{(x_1,\ldots,x_m)\in \mathbb{R}^m\mid x_m\geq 0\right\}$$

and consider a *manifold with boundary*.

## Examples of Topological Manifolds

We have already learned in topology many ways to construct new spaces from given ones. Hence, once topological manifolds are given, it is natural to ask whether the resulting spaces remain topological manifolds.

::: Example 3 (Open submanifold)
An open subspace $U$ of an $m$-manifold $M$ is again an $m$-manifold. Indeed, if $\mathcal{B}$ is a base for $M$, then the collection

$$\mathcal{B}_U=\left\{B\cap U\mid B\in \mathcal{B}\right\}$$

is a base for $U$, so $U$ is second-countable; a subspace of a Hausdorff space is always Hausdorff ([[Topology] §Hausdorff Spaces, §§Subspaces and Products of Hausdorff Spaces](/en/math/topology/Hausdorff_spaces#subspaces-and-products-of-hausdorff-spaces)); and if $x\in U$ is arbitrary, then since $M$ is locally Euclidean we can choose an open neighborhood $V$ of $x$ in $M$ with $V$ homeomorphic to an open subset of $\mathbb{R}^m$, whence $U\cap V$ is an open neighborhood of $x$ in $U$ homeomorphic to an open subset of $\mathbb{R}^m$.
:::

Similarly, the set appearing in [[Topology] §Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7) yields another example of a topological manifold.

::: Example 4
For an open set $U\subseteq \mathbb{R}^n$ and a continuous function $f:U\rightarrow\mathbb{R}^k$, the graph of $f$

$$\graph(f)=\left\{(x,f(x))\mid x\in U\right\}\subseteq \mathbb{R}^n\times \mathbb{R}^k$$

is an $n$-manifold. In fact, the two continuous maps

$$x\mapsto (x,f(x)),\qquad (x,f(x))\mapsto x$$

are inverse to each other, so $\graph(f)$ is homeomorphic to $U$.
:::

By [[Topology] §Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7), $\graph(f)$ is a closed subset of $U\times \mathbb{R}^k$, and in particular when $U=\mathbb{R}^n$ it is a closed subset of $\mathbb{R}^{n+k}$; thus this gives an example of a somewhat different character from [Example 3](#ex3).

The same holds for the product topology.

::: Example 5 (Product manifold)
Let $M_1$ and $M_2$ be topological manifolds of dimensions $m_1$ and $m_2$, respectively. Then $M_1\times M_2$ is an $(m_1+m_2)$-manifold. For if $\mathcal{B}_i$ is a base for $M_i$, then the collection

$$\mathcal{B}=\left\{B_1\times B_2\mid B_i\in \mathcal{B}_i\right\}$$

is a basis for $M_1\times M_2$, so $M_1\times M_2$ is second countable; a product of Hausdorff spaces is Hausdorff ([[Topology] §Hausdorff Spaces, ⁋Proposition 8](/en/math/topology/Hausdorff_spaces#prop8)); and for any $(x_1,x_2)\in M_1\times M_2$, if $U_i$ is a Euclidean neighborhood of $x_i$ in $M_i$, then $U_1\times U_2$ is a Euclidean neighborhood of $(x_1,x_2)$ in $M_1\times M_2$.
:::

Finally, the last general construction we examine is the quotient space. However, as we saw in [[Topology] §Hausdorff Spaces, §§Quotient Spaces of Hausdorff Spaces](/en/math/topology/Hausdorff_spaces#quotient-spaces-of-hausdorff-spaces), an arbitrary quotient of a Hausdorff space need not be Hausdorff. Moreover, there is no guarantee that a quotient of a Euclidean space is Euclidean, so to show that a quotient space is a topological manifold one must verify the Hausdorff and locally Euclidean conditions separately. On the other hand, second countability follows from the locally Euclidean condition.

::: Proposition 6
Let $\pi:X \rightarrow X/R$ be a quotient map, and suppose $X$ is second-countable and $X/R$ is locally Euclidean. Then $X/R$ is second countable.
:::
::: Proof
Since $X/R$ is locally Euclidean, we can cover $X/R$ by Euclidean neighborhoods $(U_i)_{i\in I}$; their preimages $(\pi^{-1}(U_i))_{i\in I}$ then cover $X$. Any second-countable space is Lindelöf ([[Topology] §Compactness and Convergence of Filters, ⁋Proposition 12](/en/math/topology/filter_convergence#prop12)), so there exists a countable subset $J\subseteq I$ such that $(\pi^{-1}(U_i))_{i\in J}$ is a countable open cover of $X$, and hence the corresponding $(U_i)_{i\in J}$ form a countable cover of $X/R$. But each of these is a Euclidean neighborhood and therefore has a countable base; since there are countably many of them, their union yields a countable base for $X/R$.
:::

Viewed solely within the flow of this category, it would suffice to restrict our attention to topological manifolds; however, when we treat the multiplicative structure of cohomology, it is more convenient to keep in mind the notion of integration on smooth manifolds.

---

**References**

**[Lee]** J. M. Lee, *Introduction to Topological Manifolds*, 2nd ed., Springer, 2011.  
**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.
