---
title: "Uniqueness of Submanifolds"
excerpt: "The topological structure of immersed submanifolds and the factorization of smooth functions"

categories: [Math / Manifold]
permalink: /en/math/manifold/uniqueness_of_submanifold
header:
    overlay_image: /assets/images/Math/Manifold/Uniqueness_of_Submanifold.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-en"

date: 2023-01-12
last_modified_at: 2023-01-12
weight: 8
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
By definition, a submanifold of a manifold $$M$$ means an injective immersion. Let us denote this by $$\Phi:P\rightarrow M$$. Then the function $$\bar{\Phi}:P\rightarrow \Phi(P)$$ obtained by restricting the codomain of $$\Phi$$ is a bijection, so we can transfer the topology of $$P$$ directly onto $$\Phi(P)$$, and through this process a submanifold of $$M$$ can also be thought of as the inclusion of a subset $$\Phi(P)\hookrightarrow M$$. In this post we examine this in a bit more detail.

## Submanifolds and $$C^\infty$$ Functions

First, fix a manifold $$M$$ and its submanifold $$\Phi:P\rightarrow M$$. If another $$C^\infty$$ function $$F:N\rightarrow M$$ satisfies $$F(N)\subseteq\Phi(P)$$, then using $$\bar{\Phi}$$ defined as above we can define a new injective function $$F_0:N\rightarrow P$$ by the formula

$$F_0=\bar{\Phi}^{-1}\circ F$$

Naturally, one may ask whether the function $$F_0$$ defined in this way is an immersion.

If we view a submanifold simply as a subset of the original manifold, this question is the same as asking whether, whenever the image of an arbitrary $$C^\infty$$ function $$F:N\rightarrow M$$ satisfies $$F(N)\subseteq P\subseteq M$$, the restriction of the codomain of $$F$$ to $$P$$ is $$C^\infty$$. However, this question is not as simple as it looks, and in fact this does not always hold.

<div class="example" markdown="1">

<ins id="ex1">**Example 1**</ins> Suppose both manifolds $$N$$ and $$P$$ are $$\mathbb{R}$$ equipped with their natural manifold structures, and that $$M=\mathbb{R}^2$$ is also given its natural manifold structure. Define two submanifolds $$\Phi:N\rightarrow M$$ and $$\Psi:P\rightarrow M$$ as in the two figures below

![counterexample_1](/assets/images/Math/Manifold/Uniqueness_of_Submanifold-1.png){:style="width:200px" class="invert" .align-center}

and

![counterexample_2](/assets/images/Math/Manifold/Uniqueness_of_Submanifold-2.png){:style="width:200px" class="invert" .align-center}

Then $$\Phi(N)=\Psi(P)$$, and therefore the bijection $$\bar{\Psi}^{-1}\circ\Phi$$ from $$N$$ to $$P$$ is well defined.

Now consider a sufficiently small open neighborhood $$U$$ of the origin in $$N$$, and consider the image of $$U$$ under $$\bar{\Psi}^{-1}\circ\Phi$$. Then $$(\bar{\Psi}^{-1}\circ\Phi)(U)$$ is not an open set in $$P$$. 

![counterexample_3](/assets/images/Math/Manifold/Uniqueness_of_Submanifold-3.png){:style="width:300px" class="invert" .align-center}

That is, since $$(\bar{\Psi}^{-1}\circ\Phi)^{-1}$$ is not continuous, this function is not even a $$C^\infty$$ function.

</div>

However, the following proposition shows that what causes problems like the example above is purely topological data.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let a submanifold $$\Phi:P\rightarrow M$$ of a manifold $$M$$ be given. If an arbitrary $$C^\infty$$ function $$F:N\rightarrow M$$ satisfies $$F(N)\subseteq\Phi(P)$$, then for the function $$F_0:N\rightarrow P$$ defined by the formula

$$F_0=\bar{\Phi}^{-1}\circ F$$

the following hold.

1. If $$F_0$$ is continuous, then $$F_0$$ is $$C^\infty$$.
2. If $$\Phi$$ is an embedding, then $$F_0$$ is continuous.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The second claim is by definition, so it suffices to prove only the first claim.

Assume that $$F_0$$ is continuous, and let us show that $$F_0$$ is also $$C^\infty$$. That is, for arbitrary $$x\in N$$, we must show that there exists a coordinate system $$(U,\varphi)$$ centered at $$x$$ such that the restriction of $$F_0$$ to $$U$$ is $$C^\infty$$. But since we have assumed that $$F_0$$ is a continuous bijection, to show this it suffices to show that there exists a coordinate system $$(V,\psi)$$ containing arbitrary $$y\in P$$ such that the restriction of $$\psi\circ F_0$$ to the *open set* $$F_0^{-1}(V)$$ is $$C^\infty$$.

Now let $$y\in P$$ be given arbitrarily, and choose a coordinate system $$(W,z^1,\ldots, z^m)$$ of $$M$$ containing $$\Phi(y)$$. Then from [§Submanifolds and the Inverse Function Theorem, ⁋Corollary 10](/en/math/manifold/submanifolds#cor10) we know that restricting a subset of the set $$\{z^k\circ\Phi\mid 1\leq k\leq m\}$$ to a suitable open neighborhood $$V$$ forms a coordinate system at the point $$y\in P$$.

Now denote these by $$\{z^1\circ\Phi,\ldots,z^p\circ\Phi\}$$. Without loss of generality, if $$\gamma=(z^1,\ldots, z^m)$$ is a surjection onto $$\mathbb{R}^m$$, then the above claim is the same as saying that $$(V,\pi\circ\gamma\circ\Phi)$$ is a coordinate system at $$y$$ via the projection $$\pi:\mathbb{R}^m\rightarrow\mathbb{R}^p$$. Now

$$(\pi\circ\gamma\circ\Phi)\circ F_0|_{F_0^{-1}(V)}=\pi\circ\gamma\circ F|_{F_0^{-1}(V)}$$

and the right-hand side is a composition of $$C^\infty$$ functions, hence is $$C^\infty$$.

</details>

## Equivalence of Submanifolds

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> Let a manifold $$M$$ and two submanifolds $$\Phi_1:N_1\rightarrow M$$, $$\Phi_2:N_2\rightarrow M$$ be given. That these two are *equivalent* means that there exists a diffeomorphism $$\theta:N_1\rightarrow N_2$$ such that $$\Phi_1=\Phi_2\circ\theta$$ holds.

</div>

That the relation defined in this way induces an equivalence relation on the set of all submanifolds $$(N,\Phi)$$ of $$M$$ is obvious. Choose an arbitrary equivalence class $$[(N,\Phi)]$$. Then we can consider the pair

$$A=\Phi(N)\subseteq M, \qquad \iota:A\hookrightarrow M$$

as we examined at the beginning. Here, $$A$$ is a manifold endowed with the differentiable and topological structures of $$N$$ via the bijection $$\bar{\Phi}:N\rightarrow A$$. Then $$\bar{\Phi}$$ is a diffeomorphism between $$N$$ and $$A$$, so $$\bar{\Phi}^{-1}$$ is also a diffeomorphism and therefore the composition

$$\iota=\Phi\circ\bar{\Phi}^{-1}$$

is an immersion from $$A$$ into $$M$$. That is, $$(A,\iota)$$ is a submanifold of $$M$$. Moreover, the above equation shows that $$(N,\Phi)$$ and $$(A,\iota)$$ are equivalent.

Conversely, for a subset $$A\subseteq M$$ equipped with a manifold structure, if the inclusion $$\iota:A\hookrightarrow M$$ is an immersion, then $$(A,\iota)$$ is always a submanifold of $$M$$. This means that for arbitrary $$x\in A$$, $$d\iota_x:T_xA\rightarrow T_xM$$ is injective, so $$d\iota_x$$ induces a bijection between $$T_xA$$ and $$d\iota_x(T_xA)$$. Ignoring a slight notational issue, we can treat $$T_xA$$ as the same as $$d\iota_x(T_xA)$$.

## Uniqueness of Submanifolds

The pair $$(A,\iota)$$ defined in the section above is determined *uniquely* for each equivalence class $$[(N,\Phi)]$$. First, since $$\theta$$ in [Definition 3](#def3) is a diffeomorphism, it is in particular a bijection, and therefore

$$\Phi_2(N_2)=\Phi_1(\theta(N_2))=\Phi_1(N_1)$$

holds, so $$A$$ is uniquely determined. On the other hand, for the subset $$A$$ of $$M$$ determined in this way and the inclusion $$\iota:A\hookrightarrow M$$ to belong to $$[(N,\Phi)]$$, there must exist a diffeomorphism $$\theta$$ satisfying $$\iota=\Phi\circ\theta$$; taking $$\bar{\Phi}^{-1}$$ on both sides gives $$\theta=\bar{\Phi}^{-1}$$, so the manifold structure on $$A$$ must *necessarily* be defined in the same way as defined above.

On the other hand, given an arbitrary subset $$A\subseteq M$$ with the inclusion $$\iota:A\hookrightarrow M$$, a manifold structure on $$A$$ making $$(A,\iota)$$ a submanifold does not exist uniquely. For example, as in [Example 2](#ex2), if two submanifolds $$(N_1,\Phi_1),(N_2,\Phi_2)$$ of $$M$$ are not diffeomorphic to each other but satisfy $$\Phi_1(N_1)=\Phi_2(N_2)$$, then the two manifold structures on $$(A,\iota)$$ obtained from $$[(N_1,\Phi_1)]$$ and $$[(N_2,\Phi_2)]$$ through the above process must be different from each other.

Nevertheless, if additional conditions that $$(A,\iota)$$ must satisfy are imposed, then the structure of a submanifold on it may be determined uniquely. The results of the theorems to be introduced in the next post satisfy even this uniqueness, and in that case the following two propositions can be used.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Fix a subset $$A$$ of a manifold $$M$$ and a topology $$\mathcal{T}$$ defined on $$A$$. Then there exists at most one differentiable structure making $$(A,\iota)$$ a submanifold of $$M$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious from the first claim of [Proposition 2](#prop2).

</details>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let a subset $$A$$ of a manifold $$M$$ be given. If, when viewing $$A$$ as a subspace of $$M$$, there exists a differentiable structure making $$(A,\iota)$$ a submanifold of $$M$$, then this differentiable structure together with the subspace topology constitutes the unique manifold structure that can be given to $$(A,\iota)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, applying [Proposition 4](#prop4) to the subspace topology $$\mathcal{T}$$, the differentiable structure making $$(A,\mathcal{T},\iota)$$ a submanifold of $$M$$ is unique. Let us denote this by $$\mathcal{A}$$. Now suppose a topology $$\mathcal{T}'$$ and a differentiable structure $$\mathcal{A}'$$ making $$(A,\iota)$$ a submanifold of $$M$$ are given, and consider the following diagram.

![uniqueness](/assets/images/Math/Manifold/Uniqueness_of_Submanifold-4.png){:style="width:12.6em" class="invert" .align-center}

Here $$\iota$$ and $$\iota'$$ are both $$A\hookrightarrow M$$, but we have denoted them by different names for distinction. By definition $$(A,\mathcal{T},\mathcal{A})$$ is an embedded submanifold of $$M$$, so the vertical $$\iota$$ is an embedding and therefore $$\operatorname{id}$$ is $$C^\infty$$ by [Proposition 2](#prop2). Also, by the chain rule

$$d\iota'=d\iota\circ d(\id)$$

holds, and since $$d\iota'$$ is injective at every point, $$d(\id)$$ is also injective at every point. Therefore it suffices to show that $$d(\id)$$ is surjective at every point.

Suppose for contradiction that there exists a point $$a$$ at which $$d(\id)$$ is not surjective. Then considering the dimension of the tangent space at this point,

$$\dim(A,\mathcal{T}',\mathcal{A}')<\dim(A,\mathcal{T},\mathcal{A})$$

holds. Let $$d$$ be the dimension of $$(A,\mathcal{T},\mathcal{A})$$ and $$d'$$ be the dimension of $$(A,\mathcal{T}',\mathcal{A}')$$.

Let $$(U,\varphi)$$ be a coordinate system of $$(A,\mathcal{T},\mathcal{A})$$. Without loss of generality we may assume that the image of $$\varphi$$ is $$\mathbb{R}^d$$, and since $$\id$$ is a surjection, the image of the composition $$\varphi\circ\id$$ is also $$\mathbb{R}^d$$.

On the other hand, since $$(A,\mathcal{T}',\mathcal{A}')$$ is a manifold, we can cover it by *countable* coordinate systems $$(V,\sigma)$$ each homeomorphic to $$\mathbb{R}^{d'}$$. But $$\varphi\circ\id\circ\sigma^{-1}$$ is $$C^\infty$$, and as $$C^1$$ functions their images all have measure zero, so it is a contradiction that their images could be $$\mathbb{R}^d$$.

</details>

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
