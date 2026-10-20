---
title: "Submanifolds and the Inverse Function Theorem"
description: "We explain the definition of submanifolds in terms of immersions and submersions, and discuss the difference between immersed and embedded submanifolds from the perspective of subspace topology with illustrated examples."
excerpt: "Substructures of smooth manifolds"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/submanifolds
sidebar: 
    nav: "manifolds-en"

date: 2022-06-17
weight: 7
translated_at: 2026-08-19T18:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-20T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definition of Submanifolds

::: Definition 1
Let two manifolds $M,N$ and a $C^\infty$ function $F:N\rightarrow M$ be given.

1. That $F$ is an *immersion* means that for every $p\in N$, $\dd{F_p}$ is injective; similarly, that $F$ is a *submersion* means that for every $p\in N$, $\dd{F_p}$ is surjective.
2. If $F$ is an immersion and also an injective function, we call $F$ a *submanifold* of $M$.
3. If $F$ is not only a submanifold of $M$, but also defines a homeomorphism between $F(N)\subseteq M$ equipped with the subspace topology and $N$, we call $F$ an *embedding*, or, matching the definition in 2, an *embedded submanifold*.
:::

To distinguish it more clearly from the embedded submanifold in 3, the notion in 2 is sometimes called an *immersed submanifold*. Exactly as in the definition above, we use the unqualified term submanifold in the sense of immersed submanifold, and use embedded submanifold as is without abbreviation.

Intuitively, that a function $F:N\rightarrow M$ is a submanifold can be thought of as $F$ playing the role of the inclusion $N\hookrightarrow M$. Here, there are two ways to endow the image of $F$, $F(N)\subseteq M$, with a topological structure: one is to transfer, via the bijective function $F:N\rightarrow F(N)$, the topology of $N$, and the other is to bring the topological structure given on $M$ via the subspace topology. If these two topologies are identical to each other, we call $F$ an *embedded* submanifold; otherwise, we simply call it a submanifold.

{% diagram Math/Manifolds/Submanifolds-1.svg width="30.02em" alt="Immersion, submanifold, embedded submanifold" %}

For example, in the figure above, $N=\mathbb{R}$, $M=\mathbb{R}^2$, and (a) is an immersion but not a submanifold, (b) is a submanifold but not an embedded submanifold, and (c) is an embedded submanifold. For convenience, in (b), if as $t\rightarrow \infty$ the point that $F(t)$ approaches is called $F(0)$, then in $\mathbb{R}$, $(-1,1)$ is an open set, but in the subspace topology given on $F(N)$, $F\bigl((-1,1)\bigr)$ cannot be an open set.


::: Example 2
For a manifold $M$ and its open submanifold $U$, $\iota:U\hookrightarrow M$ is an embedded submanifold of $M$. That for every $p\in U$, $\dd{\iota_p}$ is injective is clear from [§Differentials, ⁋Proposition 8](/en/math/manifolds/differentials#prop8){: data-lid="1knle" }, that is, the fact that $\dd{\iota_p}$ is an isomorphism between $T_pU$ and $T_{\iota(p)}M$, and also by the definition of an open submanifold, the subspace topology is given on $\iota(U)$.
:::

::: Example 3
Consider two manifolds $M,N$ and their product $M\times N$. Then for any $q\in N$, the subset $M\times\{q\}$, diffeomorphic to $M$, is an embedded submanifold of $M\times N$; similarly, for any $p\in M$, the subset $\{p\}\times N$, diffeomorphic to $N$, is an embedded submanifold, where the embeddings here are given by $x\mapsto (x,q)$ and $y\mapsto (p,y)$ respectively.

More generally, let two manifolds $M,N$ and, defined on an open submanifold $U\subseteq M$, a $C^\infty$ function $f:U\rightarrow N$ be given. Then the graph of $f$,

$$\graph(f)=\{(x,y)\in M\times N\mid x\in U, y=f(x)\}$$

is also an embedded submanifold, and the embedding here is naturally given by $x\mapsto (x,f(x))$.
:::


## Inverse Function Theorem and Its Consequences

Now we will bring the inverse function theorem and the implicit function theorem in Euclidean space each to the setting of manifolds. First, the inverse function theorem in Euclidean space is as follows.

::: Theorem 4 (Inverse function theorem)
Let $U\subseteq\mathbb{R}^m$ be an open set, and let $f:U\rightarrow\mathbb{R}^m$ be a $C^\infty$ function. If at an arbitrary point $p_0\in U$ the following Jacobian matrix

$$\begin{pmatrix}\partial(r^1\circ f)/\partial r^1&\partial(r^1\circ f)/\partial r^2&\cdots&\partial(r^1\circ f)/\partial r^m\\\partial(r^2\circ f)/\partial r^1&\partial(r^2\circ f)/\partial r^2&\cdots&\partial(r^2\circ f)/\partial r^m\\\vdots&\vdots&\ddots&\vdots\\\partial(r^m\circ f)/\partial r^1&\partial(r^m\circ f)/\partial r^2&\cdots&\partial(r^m\circ f)/\partial r^m\end{pmatrix}$$

is nonsingular, then there exists, satisfying $p_0\in V\subseteq U$, a suitable open set $V$ such that $f\vert_V$ defines a diffeomorphism between $V$ and $f(V)$.
:::

Through this, we can prove theorems about functions between general manifolds. 

::: Corollary 5
Let $F:M\rightarrow N$ be a $C^\infty$ function between manifolds and let $p\in M$. If $\dd{F_p}:T_pM\rightarrow T_{F(p)}N$ is an isomorphism, then there exists a suitable open set $U\subseteq M$ such that $p\in U$ and $F\vert_U:U\rightarrow F(U)$ defines a diffeomorphism between $U$ and $F(U)$.
:::
::: Proof
First, from the fact that $\dd{F_p}$ is an isomorphism, we obtain $\dim M=\dim T_pM=\dim T_{F(p)}N=\dim N$. Now take, containing the point $F(p)$, a coordinate system $(W,\tau)$, and, so as to satisfy $F(V)\subseteq W$, take containing $p$ a coordinate system $(V,\varphi)$. Then the function $(\tau\circ F\circ\varphi^{-1})\vert_{\varphi(V)}$ is a function between Euclidean spaces having the same dimension, and from the fact that $\dd{F_p}$ is an isomorphism, we know that the Jacobian matrix of this function at the point $\varphi(p)$ is nonsingular. 

Therefore, by the inverse function theorem, there exists, satisfying $\varphi(p)\in U'\subseteq\varphi(V)$, an open set $U'$ such that $(\tau\circ F\circ\varphi^{-1})\vert_{U'}$ defines a diffeomorphism between $U'$ and $\tau\circ F\circ\varphi^{-1}(U')$. Now, if we take $U=\varphi^{-1}(U')$, the function

$$\tau^{-1}\circ\bigl((\tau\circ F\circ\varphi^{-1})\vert_{U'}\bigr)\circ\varphi$$

defines a diffeomorphism between $U$ and $F(U)$. 
:::

For a manifold $M$ and $p\in M$, let elements of $\mathcal{C}_{M,p}^\infty$, $y^1, \ldots, y^k$, be given. If their differentials $\dd{y}^i$ form a linearly independent subset of $T_p^\ast M$, they are called *independent functions* at the point $p$. 

::: Corollary 6
Consider an $m$-dimensional manifold $M$. If $y^1, \ldots, y^m$ are independent at a point $p_0\in M$, then $(y^1, \ldots, y^m)$ forms a coordinate system in a neighborhood of $p_0$.
:::
::: Proof
First, considering the dimension of $T_{p_0}^\ast M$, we see that the differentials of the given functions form a basis of $T_{p_0}^\ast M$.

Suppose the $m$ functions $y^i$ are all defined on an open neighborhood of $p_0$, $U$.[^1] If, as given, we define $\varphi:U\rightarrow\mathbb{R}^m$ by

$$\varphi(p)=(y^1(p),\ldots, y^m(p))$$

then since each component function $y^i$ is $C^\infty$, $\varphi$ is also $C^\infty$. Now consider $(\dd{\varphi_{p_0}})^\ast:T_{\varphi(p_0)}^\ast\mathbb{R}^m\rightarrow T_{p_0}^\ast M$. Applying $(\dd{\varphi_{p_0}})^\ast$ to $\dd{r}^i\vert_{\varphi(p_0)}$, we have

$$\left(\dd{\varphi_{p_0}}\right)^\ast\left(\dd{r}^i\vert_{\varphi(p_0)}\right)=\left(\dd{r}^i\vert_{\varphi(p_0)}\right)\circ\left(\dd{\varphi_{p_0}}\right)=\dd{(r^i\circ\varphi)_{p_0}}=\dd{y}^i\vert_{p_0}$$

and since in $T_{\varphi(p_0)}^\ast\mathbb{R}^m$, the basis elements $\dd{r}^i\vert_{\varphi(p_0)}$ are all mapped respectively to the basis of $T_{p_0}^\ast M$, $(\dd{\varphi_{p_0}})^\ast$ is an isomorphism. Hence $\dd{\varphi_{p_0}}$ is also an isomorphism, and therefore, applying [Corollary 5](#cor5){: data-lid="mpnrb" }, we see that there exists, satisfying $p_0\in V\subseteq U$, a suitable $V$ such that $\varphi\vert_V:V\rightarrow\varphi(V)$ is a coordinate system.
:::

Obtaining the following two corollaries from the above corollary is essentially undergraduate linear algebra.

::: Corollary 7
For an $m$-dimensional manifold $M$, $p_0\in M$, and an integer $0<k<m$, let elements of $\mathcal{C}_{M,p_0}^\infty$, $y^1,\ldots, y^k$, be independent functions at $p_0$. Then there exist suitable functions $x^{k+1},\ldots, x^{m}$ such that $(y^1,\ldots, y^k, x^{k+1}, \ldots, x^m)$ defines a coordinate system in a neighborhood of $p_0$.
:::
::: Proof
Let a coordinate system about the point $p_0$, $(U,\varphi)$, $\varphi=(x^i)_{i=1}^{m}$, be given. Then the $\dd{x}^i$ form a basis of $T_{p_0}^\ast M$. Now, just as in the proof of [\[Linear Algebra\] §Dimension of Vector Spaces, ⁋Lemma 2](/en/math/linear_algebra/dimension#lem2){: data-lid="5ywiv" }, we insert the $\dd{y}^i$ one by one and remove the $\dd{x}^j$ one by one, adjusting indices appropriately.
:::

::: Corollary 8
For an $m$-dimensional manifold $M$ and a point $p_0\in M$, let elements of $\mathcal{C}_{M,p_0}^\infty$, $y^1,\ldots, y^k$, be given. If the $\dd{y}^i$ span $T_{p_0}^\ast M$, then a suitable subset of the set $\{y^1,\ldots, y^k\}$ forms a coordinate system in a neighborhood of $p_0$.
:::
::: Proof
If we find a basis of $T_{p_0}^\ast M$ that is a suitable subset of the set $\{\dd{y}^1,\ldots, \dd{y}^k\}$, this subset must necessarily consist of $m$ elements. Therefore, applying [Corollary 6](#cor6){: data-lid="77ij8" } suffices.
:::

The following two corollaries will be used frequently in what follows under the name *rank theorem*.

::: Corollary 9 (Rank theorem, Submersion case)
For an $m$-dimensional manifold $M$, an $n$-dimensional manifold $N$, a $C^\infty$ function $F:M\rightarrow N$, and a point $p\in M$, suppose $\dd{F_p}$ is surjective. Then for a coordinate system defined in a neighborhood of the point $F(p)$, $\psi=(y^j)_{j=1}^n$, there exist suitable functions $x^{n+1},\ldots, x^m$ such that the following functions

$$x^1=y^1\circ F,\quad x^2=y^2\circ F,\quad\ldots,\quad x^n=y^n\circ F,\qquad x^{n+1},\quad \ldots,\quad x^m$$

form a coordinate system in a neighborhood of $p$.
:::
::: Proof
Since $\dd{F_p}$ is surjective, its dual $(\dd{F_p})^\ast:T_{F(p)}^\ast N\rightarrow T_p^\ast M$ is injective. That is, the following elements

$$(\dd{F_p})^\ast(\dd{y}^j\vert_{F(p)})=\dd{y}^j\vert_{F(p)}\circ \dd{F_p}=\dd{(y^j\circ F)_p}=\dd{x}^j\vert_p$$

are linearly independent in $T_p^\ast M$. Therefore, by [Corollary 7](#cor7){: data-lid="69qwd" }, we obtain the desired result.
:::

::: Corollary 10 (Rank theorem, Immersion case)
For a manifold $M$, an $n$-dimensional manifold $N$, a $C^\infty$ function $F:M\rightarrow N$, and a point $p\in M$, suppose $\dd{F_p}$ is injective. Then for a coordinate system defined in a neighborhood of the point $F(p)$, $\psi=(y^j)_{j=1}^n$, a subset of the following set

$$\{x^j=y^j\circ F\mid j=1,\ldots, n\}$$

forms, in a neighborhood of the point $p$, a coordinate system of $M$.
:::
::: Proof
Since $\dd{F_p}$ is injective, its dual $(\dd{F_p})^\ast:T_{F(p)}^\ast N\rightarrow T_p^\ast M$ is surjective. That is, the following elements

$$(\dd{F_p})^\ast(\dd{y}^j\vert_{F(p)})=\dd{y}^j\vert_{F(p)}\circ \dd{F_p}=\dd{(y^j\circ F)_p}=\dd{x}^j\vert_p$$

must span $T_p^\ast M$, and therefore by [Corollary 8](#cor8){: data-lid="hrbko" }, a subset of the given set forms, in a neighborhood of $p$, a coordinate system of $M$.
:::


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---

[^1]: This is possible because there are finitely many $y^i$. That is, if each $y^i$ is defined on $U^i$, we may set $U=\bigcap U^i$.
