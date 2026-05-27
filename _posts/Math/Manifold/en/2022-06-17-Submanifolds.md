---
title: "Submanifolds and the Inverse Function Theorem"
excerpt: "Substructures of differentiable manifolds"

categories: [Math / Manifold]
permalink: /en/math/manifold/submanifolds
header:
    overlay_image: /assets/images/Math/Manifold/Submanifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2022-06-17
last_modified_at: 2022-12-09
weight: 7
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Definition of Submanifolds

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let two manifolds $$M,N$$ and a $$C^\infty$$ function $$F:N\rightarrow M$$ be given.

1. We say that $$F$$ is an *immersion* if $$dF_p$$ is injective for every $$p\in N$$; similarly, we say that $$F$$ is a *submersion* if $$dF_p$$ is surjective for every $$p\in N$$.
2. If $$F$$ is an immersion and also an injective function, we call $$F$$ a *submanifold* of $$M$$.
3. If $$F$$ is not only a submanifold of $$M$$ but also defines a homeomorphism between $$N$$ and $$F(N)\subseteq M$$ equipped with the subspace topology, we call $$F$$ an *embedding*, or to match the definition in 2, an *embedded submanifold*.

</div>

To distinguish it more clearly from the embedded submanifold in 3, item 2 is sometimes called an *immersed submanifold*. Following the definition above, we use the unqualified term submanifold to mean an immersed manifold, and we use embedded submanifold in full without abbreviation.

Intuitively, saying that a function $$F:N\rightarrow M$$ is a submanifold means that $$F$$ plays the role of the inclusion $$N\hookrightarrow M$$. In this case, there are two ways to give a topological structure to the image $$F(N)\subseteq M$$: one is to transport the topology of $$N$$ via the bijection $$F:N\rightarrow F(N)$$, and the other is to induce it from the topology on $$M$$ via the subspace topology. If these two topologies are identical, we call $$F$$ an *embedded* submanifold; otherwise, we simply call it a submanifold.

![Immersion, submanifold, immersion](/assets/images/Math/Manifold/Submanifolds-1.png){:style="width:500px" class="invert" .align-center}

For example, in the figure above, $$N=\mathbb{R}$$, $$M=\mathbb{R}^2$$, (a) is an immersion but not a submanifold, (b) is a submanifold but not an embedded submanifold, and (c) is an embedded submanifold. For convenience, in (b), if we denote by $$F(0)$$ the point that $$F(t)$$ approaches as $$t\rightarrow\infty$$, then $$(-1,1)$$ is an open set in $$\mathbb{R}$$, but in the subspace topology $$F\bigl((-1,1)\bigr)$$ cannot be an open set.


<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For a manifold $$M$$ and its open submanifold $$U$$, the inclusion $$\iota:U\hookrightarrow M$$ is an embedded submanifold of $$M$$. That $$d\iota_p$$ is injective for every $$p\in U$$ follows from the fact that $$T_pU$$ and $$T_{\iota(p)}M$$ are isomorphic, and by the definition of an open submanifold, $$\iota(U)$$ is equipped with the subspace topology.

</div>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> Consider two manifolds $$M,N$$ and their product $$M\times N$$. Then for any $$q\in N$$, the subset $$M\times\{q\}$$ is an embedded submanifold of $$M\times N$$ diffeomorphic to $$M$$; similarly, for any $$p\in M$$, the subset $$\{p\}\times N$$ is an embedded submanifold diffeomorphic to $$N$$. The embeddings are given by $$x\mapsto (x,q)$$ and $$y\mapsto (p,y)$$ respectively.

More generally, let two manifolds $$M,N$$ and a $$C^\infty$$ function $$f:U\rightarrow N$$ defined on an open submanifold $$U\subseteq M$$ be given. Then the graph of $$f$$

$$\graph(f)=\{(x,y)\in M\times N\mid x\in U, y=f(x)\}$$

is also an embedded submanifold, and the embedding is of course given by $$x\mapsto (x,f(x))$$.

</div>


## The Inverse Function Theorem and Its Consequences

Now we will lift the inverse function theorem and the implicit function theorem from Euclidean spaces to the setting of manifolds. First, the inverse function theorem in Euclidean space is as follows.

<div class="proposition" markdown="1">

<ins id="thm4">**Theorem 4 (Inverse Function Theorem)**</ins> Let $$U\subset\mathbb{R}^m$$ be an open set and let $$f:U\rightarrow\mathbb{R}^m$$ be a $$C^\infty$$ function. If the following Jacobian matrix at an arbitrary point $$p_0\in U$$

$$\begin{pmatrix}\partial(r^1\circ f)/\partial r^1&\partial(r^1\circ f)/\partial r^2&\cdots&\partial(r^1\circ f)/\partial r^m\\\partial(r^2\circ f)/\partial r^1&\partial(r^2\circ f)/\partial r^2&\cdots&\partial(r^2\circ f)/\partial r^m\\\vdots&\vdots&\ddots&\vdots\\\partial(r^m\circ f)/\partial r^1&\partial(r^m\circ f)/\partial r^2&\cdots&\partial(r^m\circ f)/\partial r^m\end{pmatrix}$$

is nonsingular, then there exists a suitable open set $$V$$ satisfying $$p_0\in V\subseteq U$$ such that $$f\vert_V$$ defines a diffeomorphism between $$V$$ and $$f(V)$$.

</div>

Using this, we can prove theorems for functions between general manifolds. 

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Let $$F:M\rightarrow N$$ be a $$C^\infty$$ function between manifolds and let $$p\in M$$. If $$dF_p:T_pM\rightarrow T_{F(p)}N$$ is an isomorphism, then there exists a suitable open set $$U\subseteq M$$ such that $$p\in U$$ and $$F\vert_U:U\rightarrow F(U)$$ defines a diffeomorphism between $$U$$ and $$F(U)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, from the fact that $$dF_p$$ is an isomorphism, we obtain $$\dim M=\dim T_pM=\dim T_{F(p)}N=\dim N$$. Now take a coordinate system $$(W,\tau)$$ containing the point $$F(p)$$, and a coordinate system $$(V,\varphi)$$ containing $$p$$ such that $$F(V)\subseteq W$$. Then the function $$(\tau\circ F\circ\varphi^{-1})\vert_{\varphi(V)}$$ is a map between Euclidean spaces of the same dimension, and since $$dF_p$$ is an isomorphism, we know that the Jacobian matrix of this function at the point $$\varphi(p)$$ is nonsingular. 

Therefore, by the inverse function theorem, there exists an open set $$U'$$ satisfying $$\varphi(p)\in U'\subset\varphi(V)$$ such that $$(\tau\circ F\circ\varphi^{-1})\vert_{U'}$$ defines a diffeomorphism between $$U'$$ and $$\tau\circ F\circ\varphi^{-1}(U')$$. Now setting $$U=\varphi^{-1}(U)$$, the function

$$\tau^{-1}\circ\bigl((\tau\circ F\circ\varphi^{-1})|_{U'}\bigr)\circ\varphi$$

defines a diffeomorphism between $$U$$ and $$F(U)$$. 

</details>

Let elements $$y^1, \ldots, y^k$$ of $$C_p^\infty(M)$$ be given for a manifold $$M$$ and $$p\in M$$. If their differentials $$dy^i$$ form a linearly independent subset of $$T_p^\ast M$$, then we call them functions independent at the point $$p$$. 

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> Consider an $$m$$-dimensional manifold $$M$$. If $$y^1, \ldots, y^m$$ are independent at a point $$p_0\in M$$, then $$(y^1, \ldots, y^m)$$ forms a coordinate system in a neighborhood of $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, considering the dimension of $$T_p^\ast M$$, we see that the differentials of the given functions form a basis of $$T_p^\ast M$$.

Suppose the $$m$$ functions $$y^i$$ are all defined on an open neighborhood $$U$$ of $$p_0$$.[^1] As given, define $$\varphi:U\rightarrow\mathbb{R}^m$$ by

$$\varphi(p)=(y^1(p),\ldots, y^m(p))$$

Then since each component function $$y^i$$ is $$C^\infty$$, $$\varphi$$ is also $$C^\infty$$. Now consider $$(d\varphi_{p_0})^\ast:T_{\varphi(p_0)}^\ast\mathbb{R}^m\rightarrow T_{p_0}^\ast M$$. Applying $$(d\varphi_{p_0})^\ast$$ to $$dr^i\vert_{\varphi(p_0)}$$, we have

$$d\varphi_{p_0}\left(dr^i|_{\varphi(p_0)}\right)=\left(dr^i|_{\varphi(p_0)}\right)\circ\left(d\varphi_{p_0}\right)=d(r^i\circ\varphi)_{p_0}=dy^i|_{p_0}$$

Thus the basis elements $$dr^i\vert_{\varphi(p_0)}$$ of $$T_{\varphi(p_0)}^\ast\mathbb{R}^m$$ are mapped to a basis of $$T_{p_0}^\ast M$$, and therefore $$(d\varphi_{p_0})^\ast$$ is an isomorphism. Hence $$d\varphi_{p_0}$$ is also an isomorphism, and thus applying [Corollary 5](#cor5), we see that there exists a suitable $$V$$ satisfying $$p_0\in V\subseteq U$$ such that $$\varphi\vert_V:V\rightarrow\varphi(V)$$ is a coordinate system.

</details>

Obtaining the following two corollaries from the above corollary is essentially an exercise in undergraduate linear algebra.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> Consider an $$m$$-dimensional manifold $$M$$, a point $$p_0\in M$$, and an integer $$0<k<m$$. Let $$y^1,\ldots, y^k$$ be elements of $$\mathcal{C}_{M,p_0}^\infty$$ that are independent functions at $$p_0$$. Then there exist suitable functions $$x^{k+1},\ldots, x^{m}$$ such that $$(y^1,\ldots, y^k, x^{k+1}, \ldots, x^m)$$ defines a coordinate system in a neighborhood of $$p_0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let a coordinate system $$(U,\varphi)$$, $$\varphi=(x^i)_{i=1}^{m}$$, about the point $$p_0$$ be given. Then the $$dx^i$$ form a basis of $$T_{p_0}^\ast M$$. Now, just as in the proof of [\[Linear Algebra\] §Dimension of Vector Spaces, ⁋Lemma 2](/en/math/linear_algebra/dimension#cor2), we insert the $$dy^i$$ one by one and remove the $$dx^j$$ one by one, adjusting the indices appropriately.

</details>

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8**</ins> Let elements $$y^1,\ldots, y^k$$ of $$\mathcal{C}_{M,p_0}^\infty$$ be given for an $$m$$-dimensional manifold $$M$$ and a point $$p_0\in M$$. If the $$dy^i$$ span $$T_{p_0}^\ast M$$, then a suitable subset of $$\{y_1,\ldots, y_k\}$$ forms a coordinate system in a neighborhood of $$p_0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If we find a suitable subset of $$\{dy^1,\ldots, dy^k\}$$ that forms a basis of $$T_{p_0}^\ast M$$, this subset must consist of exactly $$m$$ elements. Therefore, it suffices to apply [Corollary 6](#cor6).

</details>

The following two corollaries will be used frequently hereafter under the name *rank theorem*. 

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9 (Rank theorem, Submersion case)**</ins> Let $$M,N$$ be two manifolds and $$F:M\rightarrow N$$ a $$C^\infty$$ function, and suppose $$dF_p$$ is surjective. Then for a coordinate system $$\psi=(y^j)_{j=1}^n$$ defined in a neighborhood of $$F(p)$$, there exist suitable functions $$x^{n+1},\ldots, x^m$$ such that the functions

$$x^1=y^1\circ F,\quad x^2=y^2\circ F,\quad\ldots,\quad x^n=y^n\circ F,\qquad x^{n+1},\quad \ldots,\quad x^m$$

form a coordinate system in a neighborhood of $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$dF_p$$ is surjective, its dual $$(dF_p)^\ast:T_{F(p)}^\ast N\rightarrow T_p^\ast M$$ is injective. That is, the elements

$$(dF_p)^\ast(dy^i|_{F(p)})=dy^i|_{F(p)}\circ dF_p=d(y^i\circ F)_p=dx^j|_p$$

are linearly independent in $$T_p^\ast M$$. Therefore, we obtain the desired result by [Corollary 7](#cor7). 

</details>

<div class="proposition" markdown="1">

<ins id="cor10">**Corollary 10 (Rank theorem, Immersion case)**</ins> Let $$M,N$$ be two manifolds and $$F:M\rightarrow N$$ a $$C^\infty$$ function, and suppose $$dF_p$$ is injective. Then for a coordinate system $$\psi=(y^j)_{j=1}^n$$ defined in a neighborhood of $$F(p)$$, a subset of

$$\{x^j=y^j\circ F\mid j=1,\ldots, n\}$$

forms a coordinate system of $$M$$ in a neighborhood of $$p$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$dF_p$$ is injective, its dual $$(dF_p)^\ast:T_{F(p)}^\ast N\rightarrow T_p^\ast M$$ is surjective. That is, the elements

$$(dF_p)^\ast(dy^i|_{F(p)})=dy^i|_{F(p)}\circ dF_p=d(y^i\circ F)_p=dx^j|_p$$

must span $$T_p^\ast M$$, and therefore by [Corollary 8](#cor8) a subset of the given set forms a coordinate system of $$M$$ in a neighborhood of $$p$$. 

</details>


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: This is possible because the $$y^i$$ are finite in number. That is, if the $$y^i$$ are each defined on $$U^i$$, we may take $$U=\bigcap U^i$$.
