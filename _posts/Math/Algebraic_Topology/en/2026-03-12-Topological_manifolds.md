---

title: "Topological Manifolds"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/topological_manifolds
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Topological_manifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 1

---

In this category, we study homology, cohomology, and related concepts that are essential for geometry. While these concepts are defined on general topological spaces, for them to behave well, the space must satisfy additional properties. A space satisfying all these conditions is precisely the topological manifold defined in [\[Topology\] §Compactness, ⁋Definition 9](/en/math/topology/compactness#def9). In this article, we will explore the properties and examples of topological manifolds, and in the next article, we will examine what homology is through illustrative examples. These two articles serve to outline the direction of this category; the main content begins from the third article.

## Definition of Topological Manifolds

For convenience of exposition, we repeat [\[Topology\] §Compactness, ⁋Definition 8](/en/math/topology/compactness#def8) and [\[Topology\] §Compactness, ⁋Definition 9](/en/math/topology/compactness#def9) as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A topological space $$M$$ is said to be *locally Euclidean of dimension $$m$$* if, for any given $$x\in M$$, there exists an open neighborhood $$U$$ of $$x$$ such that $$U$$ is homeomorphic to an open set of $$\mathbb{R}^m$$.

</div>

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A space that is second countable, Hausdorff, and locally Euclidean of dimension $$m$$ is called a *topological manifold of dimension $$m$$*.

</div>

For convenience, let us refer to a topological manifold of dimension $$m$$ as an *$$m$$-manifold*. Although not defined in [\[Topology\] §Compactness, ⁋Definition 8](/en/math/topology/compactness#def8), we sometimes consider a *manifold with boundary* by replacing $$\mathbb{R}^m$$ in the above definition with the *half-space*

$$\mathbb{H}^m=\left\{(x_1,\ldots,x_m)\in \mathbb{R}^m\mid x_m\geq 0\right\}$$

## Examples of Topological Manifolds

We have already learned many methods in topology for constructing new spaces from given spaces. Therefore, it is natural to ask whether the resulting spaces remain topological manifolds when initial topological manifolds are given.

<div class="example" markdown="1">

<ins id="ex3">**Example 3 (Open submanifold)**</ins> An open subspace $$U$$ of an $$m$$-manifold $$M$$ is again an $$m$$-manifold. This follows because if we denote the base of $$M$$ by $$\mathcal{B}$$, then the collection

$$\mathcal{B}_U=\left\{B\cap U\mid B\in \mathcal{B}\right\}$$

forms a base for $$U$$, showing that $$U$$ is second-countable. Moreover, a subspace of a Hausdorff space is always Hausdorff ([\[Topology\] §Hausdorff Spaces, §§Subspaces and Products of Hausdorff Spaces](/en/math/topology/Hausdorff_spaces#subspaces-and-products-of-hausdorff-spaces)), and if $$x\in U$$ is given arbitrarily, then by the assumption that $$M$$ is locally Euclidean, we can choose an open neighborhood $$V$$ of $$x$$ in $$M$$ such that $$V$$ is homeomorphic to an open set of $$\mathbb{R}^m$$, and consequently $$U\cap V$$ is an open neighborhood of $$x$$ in $$U$$ that is homeomorphic to an open set of $$\mathbb{R}^m$$.

</div>

Similarly, the set from [\[Topology\] §Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7) also provides an example of a topological manifold as follows.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> For an open set $$U\subseteq \mathbb{R}^n$$ and a continuous function $$f:U\rightarrow\mathbb{R}^k$$, the graph of $$f$$

$$\Gamma(f)=\left\{(x,f(x))\mid x\in U\right\}\subset \mathbb{R}^m\times \mathbb{R}^k$$

is an $$m$$-manifold. Indeed, this is because the two continuous functions

$$x\mapsto (x,f(x)),\qquad (x,f(x))\mapsto x$$

are inverses of each other, making $$\Gamma(f)$$ homeomorphic to $$U$$.

</div>

By [\[Topology\] §Hausdorff Spaces, ⁋Corollary 7](/en/math/topology/Hausdorff_spaces#cor7), $$\Gamma(f)$$ is a closed subset of $$\mathbb{R}^{m+k}$$, so this provides an example of a somewhat different nature than [Example 3](#ex3).

On the other hand, the following also holds for product topology.

<div class="example" markdown="1">

<ins id="ex5">**Example 5 (Product manifold)**</ins> Let two topological manifolds $$M_1$$, $$M_2$$ be given, and suppose they have dimensions $$m_1$$ and $$m_2$$, respectively. Then $$M_1\times M_2$$ is an $$(m_1+m_2)$$-manifold. This follows because if we denote the base of $$M_i$$ by $$\mathcal{B}_i$$, then the collection

$$\mathcal{B}=\left\{B_1\times B_2\mid B_i\in \mathcal{B}_i\right\}$$

forms a basis for $$M_1\times M_2$$, making $$M_1\times M_2$$ second countable. Furthermore, the product of Hausdorff spaces is Hausdorff ([\[Topology\] §Hausdorff Spaces, ⁋Proposition 8](/en/math/topology/Hausdorff_spaces#prop8)), and for any $$(x_1,x_2)\in M_1\times M_2$$, if $$U_i$$ is a Euclidean neighborhood of $$x_i$$ in $$M_i$$, then $$U_1\times U_2$$ is a Euclidean neighborhood of $$(x_1,x_2)$$ in $$M_1\times M_2$$.

</div>

The final general construction we will examine is the quotient space. However, as discussed in [\[Topology\] §Hausdorff Spaces, §§Quotient Spaces of Hausdorff Spaces](/en/math/topology/Hausdorff_spaces#quotient-spaces-of-hausdorff-spaces), an arbitrary quotient space of a Hausdorff space need not be Hausdorff. Moreover, there is no guarantee that a quotient space of a Euclidean space is Euclidean, so to show that a quotient space is a topological manifold, at least the Hausdorff condition and the locally Euclidean condition must be verified separately. On the other hand, second countability follows from the locally Euclidean condition.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$X \rightarrow X/R$$ be a quotient map. Suppose $$X$$ is second-countable and $$X/R$$ is locally Euclidean. Then $$X/R$$ is second countable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$X/R$$ is locally Euclidean, we can cover $$X/R$$ with Euclidean neighborhoods $$(U_i)_{i\in I}$$, and the collection of their preimages $$(\pi^{-1}(U_i))_{i\in I}$$ covers $$X$$. Now, since any second-countable space is Lindelöf ([##ref##](countability)), there exists a countable subset $$J\subset I$$ such that $$(\pi^{-1}(U_i))_{i\in J}$$ is a countable open cover of $$X$$, and therefore the corresponding $$(U_i)_{i\in J}$$ is a countable cover of $$X/R$$. Since each of these is a Euclidean neighborhood, it again has a countable base, and since there are countably many such neighborhoods, collecting all of them yields a countable base for $$X/R$$.

</details>

If we consider only the flow of this category, our interest could be sufficiently limited to topological manifolds; however, especially when dealing with the multiplicative structure of cohomology, it is often more convenient to recall the notion of integration on differentiable manifolds.
