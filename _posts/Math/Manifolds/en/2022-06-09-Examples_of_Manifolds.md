---
title: "Examples of Differentiable Manifolds"
description: "This post explores various examples of differentiable manifolds defined on different topological spaces. It examines the standard smooth structure on Euclidean space, manifold structures on vector and matrix spaces, and open submanifolds."
excerpt: "Various examples of differentiable manifolds"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/examples_of_manifolds
sidebar: 
    nav: "manifolds-en"

date: 2022-06-09
weight: 2
toc: false
translated_at: 2026-06-01T04:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-19T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In the previous post we examined two different ways of endowing $\mathbb{R}$ with a manifold structure. In this post we consider various examples of more general topological spaces equipped with manifold structures.

Since a manifold is a structure that locally resembles $\mathbb{R}^m$, the simplest example is of course $\mathbb{R}^m$ itself.

::: Example 1
The *standard differentiable structure* on $\mathbb{R}^m$ with the standard topology is given by the atlas $\{(\mathbb{R}^m,\id_{\mathbb{R}^m})\}$. 
:::

As in the example from the previous post, it is also possible to equip $\mathbb{R}^m$ with different differentiable structures. 

::: Example 2
More generally, let an $m$-dimensional $\mathbb{R}$-vector space $V$ be given. For $V$, choose a basis $\mathcal{B}$, and consider the coordinate representation with respect to $\mathcal{B}$, $\varphi_\mathcal{B}:v\mapsto [v]_{\mathcal{B}}$. Since this linear map is an isomorphism, it is a bijection, and therefore through it we can transfer both the topology and the differentiable structure of $\mathbb{R}^m$ to $V$. Transferring via $\varphi_\mathcal{B}$ the differentiable structure of $\mathbb{R}^m$ is the same as defining a differentiable structure on $(V,\mathcal{B})$ through a single coordinate system $(V,\varphi_{\mathcal{B}})$. 

Of course, these functions themselves depend on the choice of basis, but the topological structure and differentiable structure defined in this way are independent of the choice of basis.  

First, a norm on $V$ defined in this manner yields an equivalent metric structure regardless of the choice of basis, so given different bases $\mathcal{B}$ and $\mathcal{C}$, the vector spaces $(V,\mathcal{B})$ and $(V,\mathcal{C})$ have the same topological structure. 
Meanwhile, they also have the same differentiable structure. To see this, it suffices to show that for $(V,\varphi_\mathcal{B})$ and $(V,\varphi_\mathcal{C})$, the transition maps $\varphi_\mathcal{B}\circ\varphi_\mathcal{C}^{-1}$ and $\varphi_\mathcal{C}\circ\varphi_\mathcal{B}^{-1}$ are both $C^\infty$; these are in fact matrices, and hence polynomials, so they are naturally $C^\infty$.

As special cases of this, 

1. the set of $n\times n$ matrices $\Mat_n(\mathbb{R})$ is an $n^2$-dimensional vector space, so it carries a differentiable structure;
2. $\mathbb{C}^n$ can be regarded as a $2n$-dimensional $\mathbb{R}$-vector space, so it also carries a differentiable structure.
:::

To give further examples, we first need to define the following.

::: Definition 3
Let a manifold $M$ be given. If we endow an open subset of $M$, $V$, with the following two structures:

1. the subspace topology given by the topology of $M$,
2. for the differentiable structure defined on $M$, $\mathcal{A}$, 
    
    $$\mathcal{A}_V=\{(U_\alpha\cap V,\varphi_\alpha\vert_{U_\alpha\cap V})\mid(U_\alpha,\varphi_\alpha)\in\mathcal{A}\}$$

then $V$ becomes a manifold of the same dimension as $M$. We call such a manifold structure an *open submanifold* of $M$. 
:::

Of course, for this definition to be well defined, the subspace topology must satisfy the locally Euclidean, second countable, and Hausdorff conditions, and the elements of $\mathcal{A}_V$ must be pairwise $C^\infty$-compatible. However, the Hausdorff and second countability properties are both preserved by the subspace topology, and the locally Euclidean property also follows from the fact that $V$ is an open set. Moreover, the transition maps between elements of $\mathcal{A}_V$ are restrictions of $C^\infty$ functions, so they are also $C^\infty$.

::: Example 4
Among the elements of $\Mat_{n}(\mathbb{R})$, the set of invertible $n\times n$ matrices, $\GL(n;\mathbb{R})$, is the collection of matrices satisfying $\det(A)\neq 0$. Regarding the determinant $\det$ as a function from $\Mat_n(\mathbb{R})$ to $\mathbb{R}$, this function is a polynomial, hence continuous, and therefore, being the preimage of the open set $\mathbb{R}\setminus\{0\}$, $\GL(n;\mathbb{R})$ is also an open subset of $\Mat_n(\mathbb{R})$. Thus $\GL(n;\mathbb{R})$ is an $n^2$-dimensional manifold. 

On the other hand, $\GL(n;\mathbb{R})$ is the disjoint union of the matrices with $\det A>0$ and those with $\det A<0$, and each of these sets is open for the same reason as above, so $\GL(n;\mathbb{R})$ is not connected.
:::

::: Example 5
For an open set $U\subseteq\mathbb{R}^m$ and a $C^\infty$ function $f:U\rightarrow\mathbb{R}^n$, define the *graph* of $f$, $\graph(f)$, to be the set

$$\graph(f)=\{(x,y)\in\mathbb{R}^m\times\mathbb{R}^n\mid \text{$x\in U$, $y=f(x)$}\}$$

Then $\tilde{f}:U\rightarrow\graph(f)$, $\tilde{f}(x)=(x,f(x))$ and the projection onto the first $m$ coordinates, $\pr:\graph(f)\rightarrow U$, are both continuous and are inverses of each other, so $\graph(f)$ and $U$ are homeomorphic. Therefore $\graph(f)$ is a topological manifold, and in particular the projection $\pr:\graph(f)\rightarrow U$ forms an atlas consisting of a single chart $\{(\graph(f),\pr)\}$, so it also carries a natural (differentiable) manifold structure. 
:::

In all the examples so far, we have given the differentiable structure via an atlas consisting of only a single chart, which means that the manifold not only locally resembles $\mathbb{R}^m$ but also globally resembles $\mathbb{R}^m$, so in fact this is not a particularly interesting situation.

::: Example 6
In $\mathbb{R}^{n+1}$, consider the $n$-dimensional sphere $S^n$. If we endow $S^n$ with the subspace topology, the Hausdorff and second countability conditions are both satisfied. However, since $S^n$ is not an open set, verifying the locally Euclidean condition is more involved than in the case of an open submanifold. 

Pick any $p\in S^n$. Since $0\not\in S^n$, some coordinate of $p$ must be nonzero. Without loss of generality, let this coordinate be the $n+1$-th coordinate, and assume it is positive. That is, $p$ is an element of the following set:

$$U_{n+1}^+=\{(x^1, x^2, \ldots, x^{n+1})\in S^n\mid x^{n+1}>0\}$$

From the picture, it is almost obvious that $U_{n+1}^+$ and the open unit ball $D^n=\{x\in\mathbb{R}^n\mid\lvert x\rvert<1\}$ are homeomorphic.

{% diagram Math/Manifolds/Examples_of_Manifolds-1.png width="300px" alt="sphere_chart" %}
<cap markdown="1">[Lee], p.6. Fig. 1.3.</cap>


To write this down rigorously, for each point in $D^n$, $x=(x^1,\ldots, x^n)$, let us define a function $f:D^n\rightarrow\mathbb{R}$ by the following formula:

$$f(x)=\sqrt{1-\lvert x\rvert^2}$$

Then $f$ on $D^n$ is $C^\infty$, and moreover it defines a homeomorphism between $D^n$ and $\graph(f)=U_{n+1}^+$. Therefore the locally Euclidean condition holds. 

Furthermore, collecting these $U_i^\pm$ and the projections omitting the $i$-th coordinate onto the $n$ coordinates, $\varphi_i^\pm$, the following set

$$\mathcal{A}=\{(U_i^\pm, \varphi_i^\pm)\mid i=1,2,\ldots, n+1\}$$

forms an atlas. To show this, we must show that the charts constituting the above atlas are all $C^\infty$-compatible. Since $U_i^+$ and $U_i^-$ do not meet, they are trivially $C^\infty$-compatible with each other. Suppose two charts with distinct indices $i,j$, namely $(U_i^\pm, \varphi_i^\pm)$ and $(U_j^\pm,\varphi_j^\pm)$, are given. Without loss of generality, let $j<i$. Then first, under $(\varphi_i^\pm)^{-1}$,

$$(x^1, x^2, \ldots, x^n)\mapsto (x^1, x^2, \ldots, x^{i-1}, \pm \sqrt{1-\lvert x\rvert^2}, x^i, \ldots, x^n)$$

and subsequently under $\varphi_j^\pm$,

$$(x^1, x^2, \ldots, x^{i-1}, \pm \sqrt{1-\lvert x\rvert^2}, x^i, \ldots, x^n)\mapsto (x^1, x^2, \ldots, \hat{x}^j, \ldots, x^{i-1},  \pm \sqrt{1-\lvert x\rvert^2}, x^i, \ldots, x^n)$$

. Here, $\hat{x}^j$ means that the $j$-th component is omitted. In this case, since each component of the expression on the right-hand side is, in the $x^i$, a $C^\infty$ function, $(\varphi_j^{\pm})\circ(\varphi_i^\pm)^{-1}$ is $C^\infty$, and similarly one can verify that $(\varphi_i^{\pm})\circ(\varphi_j^\pm)^{-1}$ is also $C^\infty$. Therefore, the above set $\mathcal{A}$ defines a differentiable structure on $S^n$.
:::

The differentiable structure defined on $S^n$ is a typical example of a manifold. The next example endows $S^n$ with the (same) differentiable structure by a method different from the above example; after defining the differential, one can further generalize this example to give a manifold structure. 

::: Example 7
Let an open subset of $\mathbb{R}^n$, $U$, a function on $U$ of class $C^\infty$, $F:U\rightarrow\mathbb{R}$, and $c\in\mathbb{R}$ be given. Then the *level set* $M=F^{-1}(c)$ is well-defined. Suppose in addition that the following *Jacobian matrix* 

$$\begin{pmatrix}\frac{\partial F}{\partial x^1}&\frac{\partial F}{\partial x^2}&\cdots&\frac{\partial F}{\partial x^n}\end{pmatrix}$$

is nowhere zero. That is, for each point $a\in M$, there exists some $i$ such that $\frac{\partial F}{\partial x^i}$ is not $0$. Then by the implicit function theorem, for the point $a$, in a suitable open neighborhood $V$, $M$ is the graph 

$$x^i=f(x^1,\ldots, \hat{x}^i,\ldots, x^n)$$

of a function $f$. 

Now, just as in [Example 6](#ex6){: data-lid="6r0bl" }, if we give $M$ the subspace topology and construct charts using the $(V, f)$ just obtained, we can verify that $M$ becomes an $(n-1)$-dimensional manifold.
:::

Using [Example 7](#ex7){: data-lid="gkahj" }, we can view $S^n$ as the zero set of the function on $\mathbb{R}^{n+1}$

$$F(x^1,\ldots, x^{n+1})=(x^1)^2+(x^2)^2+\cdots+(x^{n+1})^2-1$$

; hence [Example 6](#ex6){: data-lid="l4dsp" } can be seen as a special case of the above example.

::: Example 8
Suppose that on the set $\mathbb{R}^{n+1}\setminus\{0\}$, a relation defined by $x\sim y\iff \exists\lambda\in\mathbb{R}\setminus\{0\}(x=\lambda y)$ is given. It is not hard to check that $\sim$ is an equivalence relation. Now consider the quotient set $\RP^n=(\mathbb{R}^{n+1}\setminus\{0\})/\sim$ with the quotient topology defined via the canonical projection $\pi:\mathbb{R}^{n+1}\setminus\{0\}\rightarrow \RP^n$, and for $x\in\mathbb{R}^{n+1}\setminus\{0\}$, write $[x]$ for its equivalence class. 

For each $i=1,\ldots, n+1$, consider the open subset of $\mathbb{R}^{n+1}\setminus\{0\}$

$$\tilde{U}_i=\{(x^1,\ldots, x^{n+1})\mid x^i\neq 0\}$$

. Then since $\tilde{U}_i$ is a saturated open set, by [\[Topology\] §Quotient Spaces, ⁋Proposition 7](/en/math/topology/quotient_spaces#prop7){: data-lid="h9ulk" } the quotient map $\pi$ restricts well to $\tilde{U}_i$. Therefore, setting $U_i=\pi(\tilde{U}_i)$, if we define the function $\varphi_i:U_i\rightarrow\mathbb{R}^n$ by

$$\varphi_i[x^1,\ldots, x^{n+1}]=\left(\frac{x^1}{x^i},\ldots,\frac{x^{i-1}}{x^i},\frac{x^{i+1}}{x^i},\ldots, \frac{x^{n+1}}{x^i}\right)$$

then[^1] the function $\varphi_i\circ\pi\vert_{\tilde{U}_i}$ is continuous, and hence by [\[Topology\] §Quotient Spaces, ⁋Proposition 4](/en/math/topology/quotient_spaces#prop4){: data-lid="3wmw5" } $\varphi_i$ is also continuous. 

{% diagram Math/Manifolds/Examples_of_Manifolds-2.svg width="7.46em" alt="quotient_map" %}

Moreover, since the following continuous function

$$\psi_i:(u^1, \ldots, u^n)\mapsto [u^1, \ldots, u^{i-1}, 1, u^i,\ldots, u^n]$$

is easily seen to be the inverse of $\varphi_i$, these $U_i$ are all homeomorphic to $\mathbb{R}^n$. That is, $\RP^n$ is $n$-dimensional locally Euclidean. Since from the properties of the quotient topology it can be seen that $\RP^n$ is Hausdorff and second countable, $\RP^n$ becomes a topological manifold.

On the other hand, considering the transition maps between these $(U_i,\varphi_i),(U_j,\varphi_j)$, first under $\varphi_j^{-1}$,

$$(u^1, \ldots, u^n)\mapsto [u^1, \ldots, u^{j-1}, 1, u^j,\ldots, u^n]$$

and then applying $\varphi_i$, the result depends on the relative sizes of $i$ and $j$. If $i<j$,

$$[u^1, \ldots, u^{j-1}, 1, u^j,\ldots, u^n]\mapsto \left(\frac{u^1}{u^i},\ldots,\frac{u^{i-1}}{u^i},\frac{u^{i+1}}{u^i},\ldots,\frac{u^{j-1}}{u^i}, \frac{1}{u^i}, \frac{u^j}{u^i},\ldots, \frac{u^n}{u^i}\right)$$

while if $i>j$,

$$[u^1, \ldots, u^{j-1}, 1, u^j,\ldots, u^n]\mapsto \left(\frac{u^1}{u^{i-1}},\ldots,\frac{u^{j-1}}{u^{i-1}}, \frac{1}{u^{i-1}}, \frac{u^j}{u^{i-1}},\ldots, \frac{u^{i-2}}{u^{i-1}},\frac{u^i}{u^{i-1}},\ldots, \frac{u^n}{u^{i-1}}\right)$$

so in either case they are $C^\infty$-compatible.
:::

Finally, let us look at a slightly more general example.

::: Example 9
Suppose manifolds of dimensions $m,n$ respectively, $(M,\mathcal{A}_M),(N,\mathcal{A}_N)$, are given. Then their *product manifold* is the manifold obtained by giving $M\times N$ the product topology, whose differentiable structure is defined via

$$\mathcal{A}=\{(U_\alpha\times V_\beta,\varphi_\alpha\times\psi_\beta)\mid (U_\alpha,\varphi_\alpha)\in\mathcal{A}_M,(V_\beta,\psi_\beta)\in\mathcal{A}_N\}$$

.
:::


---

**References**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013

---

[^1]: In fact, since this function is a map from a subset of $\RP^n$ to $\mathbb{R}^n$, we must show that the result on the right-hand side does not depend on the choice of representative. That is, even if $(\lambda x^1,\ldots, \lambda x^{n+1})$ were chosen as the representative, the same result must come out, and this is clear from the formula.
