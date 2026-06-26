---
title: "Topological Manifolds"
description: "We examine the definition and properties of topological manifolds, and discuss examples of spaces that satisfy the second countable, Hausdorff, and locally Euclidean conditions."
excerpt: "The definition and properties of topological manifolds as locally Euclidean spaces"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/topological_manifolds
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-07-05
weight: 1
translated_at: 2026-06-26T08:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T08:30:01+00:00
---
In this category we cover homology, cohomology, and other concepts essential to the study of geometry. Although these notions are defined on general topological spaces, they behave well only when the spaces satisfy additional conditions, and a space meeting all of these requirements is precisely the topological manifold defined in [\[Topology\] §Compactness, ⁋Definition 9](/en/math/topology/compactness#def9). In this post we examine the properties and examples of topological manifolds, and in the next post we will gain a rough idea of what homology is through some illustrative examples. These two posts outline the broad direction of this category; the substantive content begins with the third post.

## Definition of a Topological Manifold

For ease of exposition, we repeat [\[Topology\] §Compactness, ⁋Definition 8](/en/math/topology/compactness#def8) and [\[Topology\] §Compactness, ⁋Definition 9](/en/math/topology/compactness#def9) below.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$M$$ is *locally Euclidean of dimension $$m$$* if for every $$x\in M$$ there exists an open neighborhood $$U$$ of $$x$$ such that $$U$$ is homeomorphic to an open subset of $$\mathbb{R}^m$$.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A space that is second countable, Hausdorff, and locally Euclidean of dimension $$m$$ is called a *topological manifold of dimension $$m$$*.

</div>

For convenience, we shall refer to a topological manifold of dimension $$m$$ as an *$$m$$-manifold*. Although it was not defined in [\[Topology\] §Compactness, ⁋Definition 8](/en/math/topology/compactness#def8), we sometimes also consider a *manifold with boundary* by replacing $$\mathbb{R}^m$$ in the above definition with the *half-space*

$$\mathbb{H}^m=\left\{(x_1,\ldots,x_m)\in \mathbb{R}^m\mid x_m\geq 0\right\}.$$

## Examples of Topological Manifolds

We have already learned many ways to construct new spaces from given ones in topology. Hence, if we begin with topological manifolds, it is natural to ask whether the resulting spaces remain topological manifolds.

<div class="example" markdown="1">

<ins id="ex3">**Example 3 (Open submanifold)**</ins> An open subspace $$U$$ of an $$m$$-manifold $$M$$ is again an $$m$$-manifold. Indeed, letting $$\mathcal{B}$$ be a base for $$M$$, the collection

$$\mathcal{B}_U=\left\{B\cap U\mid B\in \mathcal{B}\right\}$$

is a base for $$U$$, so $$U$$ is second-countable; a subspace of a Hausdorff space is always Hausdorff ([\[Topology\] §Hausdorff Spaces, §§Subspaces and Products of Hausdorff Spaces](/en/math/topology/Hausdorff_spaces#subspaces-and-products-of-hausdorff-spaces)); and if $$x\in U$$ is given arbitrarily, then by the assumption that $$M$$ is locally Euclidean we can choose an open neighborhood $$V$$ of $$x$$ in $$M$$ such that $$V$$ is homeomorphic to an open subset of $$\mathbb{R}^m$$, whence $$U\cap V$$ is an open neighborhood of $$x$$ in $$U$$ homeomorphic to an open subset of $$\mathbb{R}^m$$.

</div>

Similarly, the set appearing in [\[Topology\] §Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7) yields the following example of a topological manifold.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For an open set $$U\subseteq \mathbb{R}^n$$ and a continuous function $$f:U\rightarrow\mathbb{R}^k$$, the graph of $$f$$

$$\Gamma(f)=\left\{(x,f(x))\mid x\in U\right\}\subset \mathbb{R}^m\times \mathbb{R}^k$$

is an $$m$$-manifold. In fact, the two continuous maps

$$x\mapsto (x,f(x)),\qquad (x,f(x))\mapsto x$$

are inverses of each other, so $$\Gamma(f)$$ and $$U$$ are homeomorphic.

</div>

By [\[Topology\] §Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7), $$\Gamma(f)$$ is a closed subset of $$\mathbb{R}^{m+k}$$; thus this gives an example of a somewhat different character from [Example 3](#ex3).

For the product topology, the following also holds.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Product manifold)**</ins> Let $$M_1$$ and $$M_2$$ be topological manifolds of dimensions $$m_1$$ and $$m_2$$, respectively. Then $$M_1\times M_2$$ is an $$(m_1+m_2)$$-manifold. Indeed, letting $$\mathcal{B}_i$$ be a base for $$M_i$$, the collection

$$\mathcal{B}=\left\{B_1\times B_2\mid B_i\in \mathcal{B}_i\right\}$$

is a basis for $$M_1\times M_2$$, so $$M_1\times M_2$$ is second countable; the product of Hausdorff spaces is Hausdorff ([\[Topology\] §Hausdorff Spaces, ⁋Proposition 8](/en/math/topology/Hausdorff_spaces#prop8)); and for any $$(x_1,x_2)\in M_1\times M_2$$, if $$U_i$$ is a Euclidean neighborhood of $$x_i$$ in $$M_i$$, then $$U_1\times U_2$$ is a Euclidean neighborhood of $$(x_1,x_2)$$ in $$M_1\times M_2$$.

</div>

The last general construction we examine is the quotient space. However, as we saw in [\[Topology\] §Hausdorff Spaces, §§Quotient Spaces of Hausdorff Spaces](/en/math/topology/Hausdorff_spaces#quotient-spaces-of-hausdorff-spaces), an arbitrary quotient of a Hausdorff space need not be Hausdorff. Moreover, there is no guarantee that the quotient of a Euclidean space is Euclidean, so to show that a quotient space is a topological manifold one must verify the Hausdorff and locally Euclidean conditions separately. On the other hand, second countability follows from the locally Euclidean condition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For the quotient map $$X \rightarrow X/R$$, suppose $$X$$ is second-countable and $$X/R$$ is locally Euclidean. Then $$X/R$$ is second-countable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$X/R$$ is locally Euclidean, we can cover $$X/R$$ by Euclidean neighborhoods $$(U_i)_{i\in I}$$, and the collection of their preimages $$(\pi^{-1}(U_i))_{i\in I}$$ covers $$X$$. Now any second-countable space is Lindelöf ([§Compactness and Convergence of Filters, ⁋Proposition 12](/en/math/topology/filter_convergence#prop12)), so there exists a suitable countable subset $$J\subset I$$ such that $$(\pi^{-1}(U_i))_{i\in J}$$ is a countable open cover of $$X$$, and therefore the corresponding $$(U_i)_{i\in J}$$ form a countable cover of $$X/R$$. But each of these is a Euclidean neighborhood, so each again has a countable base, and since there are countably many of them, their union forms a countable base for $$X/R$$.

</details>

Viewed solely through the flow of this category, it would suffice to restrict our attention to topological manifolds; however, when dealing with the multiplicative structure of cohomology in particular, it is more convenient to keep in mind the notion of integration on smooth manifolds.
