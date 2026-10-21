---
title: "Uniqueness of Submanifolds"
description: "When a submanifold is defined as an injective immersion, the fact that the image of a function satisfies the submanifold condition does not guarantee that the codomain-restricted function is always an immersion. The uniqueness of the submanifold structure depends on topological conditions."
excerpt: "Topological structure of immersed submanifolds and factorization of smooth functions"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/uniqueness_of_submanifold
sidebar: 
    nav: "manifolds-en"

date: 2023-01-12
weight: 8
translated_at: 2026-06-01T10:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-21T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
By definition, a submanifold of a manifold $M$ means an injective immersion. Let us write this as $\Phi:P\rightarrow M$. Then the function $\bar{\Phi}:P\rightarrow \Phi(P)$ obtained by restricting the codomain of $\Phi$ is a bijection, so we can transfer the topological structure of $P$ directly onto $\Phi(P)$, and through this process a submanifold of $M$ can also be regarded as the inclusion of a subset $\Phi(P)\hookrightarrow M$. In this post, we examine this in a bit more detail.

## Submanifolds and $C^\infty$ Functions

First, fix a manifold $M$ and its submanifold $\Phi:P\rightarrow M$. If another $C^\infty$ function $F:N\rightarrow M$ satisfies $F(N)\subseteq\Phi(P)$, then using $\bar{\Phi}$ defined as above, we can define a new function $F_0:N\rightarrow P$ via the formula

$$F_0=\bar{\Phi}^{-1}\circ F$$

Naturally, one can ask whether the function $F_0$ defined in this way is a $C^\infty$ function.

If we view a submanifold simply as a subset of the original manifold, this question is simply equivalent to asking whether, when the range of an arbitrary $C^\infty$ function $F:N\rightarrow M$ satisfies $F(N)\subseteq P\subseteq M$, restricting the codomain of $F$ to $P$ is $C^\infty$. However, this question is not as simple as it looks, and in fact this does not always hold.

::: Example 1
Suppose both manifolds $N,P$ are $\mathbb{R}$ equipped with their natural manifold structures, and suppose $M=\mathbb{R}^2$ is also given its natural manifold structure. Define two submanifolds $\Phi:N\rightarrow M$ and $\Psi:P\rightarrow M$ as in the two figures below

{% diagram Math/Manifolds/Uniqueness_of_Submanifold-1.svg width="18.80em" alt="counterexample_1" %}

and

{% diagram Math/Manifolds/Uniqueness_of_Submanifold-2.svg width="18.80em" alt="counterexample_2" %}

Then $\Phi(N)=\Psi(P)$, and therefore the bijection $\bar{\Psi}^{-1}\circ\Phi$ from $N$ to $P$ is well-defined.

Now consider a sufficiently small open neighborhood $U$ of the origin in $N$, and consider the image of $U$ under $\bar{\Psi}^{-1}\circ\Phi$. Then $(\bar{\Psi}^{-1}\circ\Phi)(U)$ is not an open set in $P$.

{% diagram Math/Manifolds/Uniqueness_of_Submanifold-3.svg width="19.88em" alt="counterexample_3" %}

That is, since $(\bar{\Psi}^{-1}\circ\Phi)^{-1}$ is not continuous, this function is not even $C^\infty$.
:::

However, the following proposition shows that what causes problems like the example above is purely topological data.

::: Proposition 2
Given a manifold $M$, let $\Phi:P\rightarrow M$ be a submanifold. If an arbitrary $C^\infty$ function $F:N\rightarrow M$ satisfies $F(N)\subseteq\Phi(P)$, then for the function $F_0:N\rightarrow P$ defined by

$$F_0=\bar{\Phi}^{-1}\circ F$$

the following hold:

1. If $F_0$ is continuous, then $F_0$ is $C^\infty$.
2. If $\Phi$ is an embedding, then $F_0$ is continuous.
:::
::: Proof
Since the second claim follows from the definition, it suffices to prove only the first claim.

Assume that $F_0$ is continuous, and let us show that $F_0$ is also $C^\infty$. That is, for any $x\in N$, we must show that there exists a coordinate system $(U,\varphi)$ centered at $x$ such that the restriction of $F_0$ to $U$ is $C^\infty$. However, since we assumed that $F_0$ is continuous, to show this it suffices to show that for any $y\in P$, there exists a coordinate system $(V,\psi)$ containing $y$ such that the restriction of $\psi\circ F_0$ to the *open set* $F_0^{-1}(V)$ is $C^\infty$.

Now let $y\in P$ be given arbitrarily, and containing $\Phi(y)$, choose a coordinate system of $M$, $(W,z^1,\ldots, z^m)$. Then by [§Submanifolds and the Inverse Function Theorem, ⁋Corollary 10](/en/math/manifolds/submanifolds#cor10){: data-lid="lv5fb" }, we know that restricting a subset of the set $\{z^k\circ\Phi\mid 1\leq k\leq m\}$ to a suitable open neighborhood $V$ forms a coordinate system at the point $y\in P$.

Now let these be $\{z^1\circ\Phi,\ldots,z^p\circ\Phi\}$. Without loss of generality, assuming that $\gamma=(z^1,\ldots, z^m)$ is a surjection onto $\mathbb{R}^m$, the above claim is equivalent to saying that via the projection $\pi:\mathbb{R}^m\rightarrow\mathbb{R}^p$, $(V,\pi\circ\gamma\circ\Phi)$ is a coordinate system at $y$. Now

$$(\pi\circ\gamma\circ\Phi)\circ F_0\vert_{F_0^{-1}(V)}=\pi\circ\gamma\circ F\vert_{F_0^{-1}(V)}$$

and the right-hand side is a composition of $C^\infty$ functions, hence $C^\infty$.
:::

## Equivalence of Submanifolds

::: Definition 3
Let a manifold $M$ and two submanifolds $\Phi_1:N_1\rightarrow M$, $\Phi_2:N_2\rightarrow M$ be given. These two are said to be *equivalent* if there exists a diffeomorphism $\theta:N_1\rightarrow N_2$ such that $\Phi_1=\Phi_2\circ\theta$.
:::

That the relation thus defined induces an equivalence relation on the set of all submanifolds of $M$, $(N,\Phi)$, follows from the fact that the identity map is a diffeomorphism, and that the inverse of a diffeomorphism and the composition of two diffeomorphisms are also diffeomorphisms. Choose an arbitrary equivalence class $[(N,\Phi)]$. Then we may consider the pair

$$A=\Phi(N)\subseteq M, \qquad \iota:A\hookrightarrow M$$

just as examined at the outset. Here, $A$ is a manifold endowed, via the bijection $\bar{\Phi}:N\rightarrow A$, with the differentiable and topological structures of $N$. Then since $\bar{\Phi}$ is a diffeomorphism between $N$ and $A$, $\bar{\Phi}^{-1}$ is also a diffeomorphism, and therefore the composition

$$\iota=\Phi\circ\bar{\Phi}^{-1}$$

is an immersion from $A$ into $M$. That is, $(A,\iota)$ is a submanifold of $M$. Moreover, the above expression shows that $(N,\Phi)$ and $(A,\iota)$ are equivalent.

Conversely, for a subset $A\subseteq M$ equipped with a manifold structure, if the inclusion $\iota:A\hookrightarrow M$ is an immersion, then $(A,\iota)$ is always a submanifold of $M$. This means that for any $x\in A$, the differential $\dd{\iota_x}:T_xA\rightarrow T_xM$ is injective, so $\dd{\iota_x}$ induces a bijection between $T_xA$ and $\dd{\iota_x}(T_xA)$. Setting aside a slight notational issue, we may treat $T_xA$ as identical to $\dd{\iota_x}(T_xA)$.

## Uniqueness of Submanifolds

The pair $(A,\iota)$ defined in the section above is determined *uniquely* for each equivalence class $[(N,\Phi)]$. First, since $\theta$ in [Definition 3](#def3){: data-lid="z8657" } is a diffeomorphism, it is in particular bijective, and therefore

$$\Phi_2(N_2)=\Phi_1(\theta^{-1}(N_2))=\Phi_1(N_1)$$

holds, so $A$ is uniquely determined. On the other hand, for the subset of $M$ thus determined, $A$, and the inclusion $\iota:A\hookrightarrow M$ to belong to $[(N,\Phi)]$, there must exist, satisfying $\iota=\Phi\circ\theta$, a diffeomorphism $\theta$; taking $\bar{\Phi}^{-1}$ on the left of both sides yields $\theta=\bar{\Phi}^{-1}$, so the manifold structure on $A$ must *necessarily* be defined in the same way as defined above.

On the other hand, for an arbitrary subset of the manifold $M$, $\iota:A\hookrightarrow M$, a manifold structure that makes $(A,\iota)$ a submanifold does not exist uniquely on $A$. For instance, as in [Example 1](#ex1){: data-lid="40m7n" }, if two submanifolds of $M$, $(N_1,\Phi_1),(N_2,\Phi_2)$, are not equivalent to each other yet satisfy $\Phi_1(N_1)=\Phi_2(N_2)$, then the two manifold structures obtained from $[(N_1,\Phi_1)]$ and $[(N_2,\Phi_2)]$ via the above process must be distinct on $(A,\iota)$.

Nevertheless, if additional conditions that $(A,\iota)$ must satisfy are added, a submanifold structure on it may be uniquely determined. The results of the theorems to be introduced in the next post satisfy even this uniqueness, and here the following two propositions can be usefully applied.

::: Proposition 4
For a manifold $M$, fix a subset $A$, and on $A$ a topology $\mathcal{T}$. Then there exists at most one differentiable structure making $(A,\iota)$ a submanifold of $M$.
:::
::: Proof
This is immediate from the first claim of [Proposition 2](#prop2){: data-lid="zv4if" }.
:::

::: Proposition 5
Let a manifold $M$ and its subset $A$ be given. If, when $A$ is viewed as a subspace of $M$, there exists a differentiable structure making $(A,\iota)$ a submanifold of $M$, then this differentiable structure and the subspace topology constitute the unique structure making $(A,\iota)$ a submanifold.
:::
::: Proof
First, applying the preceding [Proposition 4](#prop4){: data-lid="k0mgi" } to the subspace topology $\mathcal{T}$, the differentiable structure making $(A,\mathcal{T},\iota)$ a submanifold of $M$ is unique. Let this be $\mathcal{A}$. Now suppose that to make $(A,\iota)$ a submanifold of $M$, a topology $\mathcal{T}'$ and a differentiable structure $\mathcal{A}'$ are given, and consider the following diagram.

{% diagram Math/Manifolds/Uniqueness_of_Submanifold-4.svg width="12.99em" alt="uniqueness" %}

Here $\iota$ and $\iota'$ are both $A\hookrightarrow M$, but we have denoted them by different names for distinction. By definition $(A,\mathcal{T},\mathcal{A})$ is an embedded submanifold of $M$, so the vertical $\iota$ is an embedding, and therefore by [Proposition 2](#prop2){: data-lid="am0a8" }, $\id$ is $C^\infty$. Also, by the chain rule

$$\dd{\iota}'=\dd{\iota}\circ \dd{(\id)}$$

holds, and since $\dd{\iota}'$ is injective at every point, $\dd{(\id)}$ is also injective at every point. Therefore it suffices to show that $\dd{(\id)}$ is surjective at every point.

Suppose for contradiction that $\dd{(\id)}$ is not surjective at some point $a$. Then considering the dimension of the tangent space at this point,

$$\dim(A,\mathcal{T}',\mathcal{A}')<\dim(A,\mathcal{T},\mathcal{A})$$

holds. Let the dimension of $(A,\mathcal{T},\mathcal{A})$ be $d$, and the dimension of $(A,\mathcal{T}',\mathcal{A}')$ be $d'$.

Let $(U,\varphi)$ be a coordinate system of $(A,\mathcal{T},\mathcal{A})$. Without loss of generality we may assume that the image of $\varphi$ is $\mathbb{R}^d$, and since $\id$ is surjective, the image of the composition $\varphi\circ\id$ is also $\mathbb{R}^d$.

On the other hand, since $(A,\mathcal{T}',\mathcal{A}')$ is a manifold, we can cover it by *countable* coordinate systems homeomorphic to $\mathbb{R}^{d'}$, $(V,\sigma)$. But $\varphi\circ\id\circ\sigma^{-1}$ is $C^\infty$, and as $C^1$ functions they all map the measure zero sets $\mathbb{R}^{d'}$ to measure zero sets, so it is a contradiction that their image is $\mathbb{R}^d$.
:::

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
