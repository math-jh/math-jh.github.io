---
title: "Implicit Function Theorem"
description: "This post covers the implicit function theorem extended to differentiable manifolds, shows that every immersed submanifold is locally embedded, and derives the submersion level set theorem."
excerpt: "The implicit function theorem on differentiable manifolds and its consequences"

categories: [Math / Manifold]
permalink: /en/math/manifold/implicit_function_theorem
sidebar: 
    nav: "manifold-en"

date: 2022-06-19
last_modified_at: 2022-12-10
weight: 9
translated_at: 2026-06-01T07:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T07:00:04+00:00
---
First, let us define the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a manifold $$M$$ and a coordinate system $$(U,\varphi)$$ be given. Write $$\varphi=(x^i)_{i=1}^m$$, let $$0\leq k\leq m$$, and for $$p\in \varphi(U)$$ consider the set

$$S=\{q\in U\mid x^i(q)=r^i(p), k+1\leq i\leq m\}.$$

The manifold obtained by endowing $$S$$ with the subspace topology and the coordinate system $$(S, (x^j\vert_S)_{j=1}^k)$$ is called a *slice* of $$(U,\varphi)$$.

</div>

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Let an immersion $$F:M\rightarrow N$$ between two manifolds be given. Then for any $$p\in M$$, there exist a coordinate system $$(V,\varphi)$$ containing $$F(p)$$ and a suitable open neighborhood $$U$$ of $$p$$ such that $$F\vert_U$$ is injective and $$F(U)$$ is a slice of $$(V,\varphi)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

In the above lemma, one must take care to observe that for an open set $$U$$ in $$M$$, the statement concerns $$F(U)$$ being a slice of $$(V,\varphi)$$. For example, $$F(M)\cap V$$ is generally not a slice, and the same holds even when $$F$$ is a submanifold.

![counterexample](/assets/images/Math/Manifold/Implicit_Function_Theorem-1.png){:style="width:200px" class="invert" .align-center}

However, if $$M$$ is embedded, we may choose $$(V,\varphi)$$ appropriately so that $$F(M)\cap V$$ is a slice of $$V$$. From this perspective, the above lemma can be summarized as

> An immersed submanifold is locally embedded.

## The Implicit Function Theorem and Its Consequences

We are now ready to extend the implicit function theorem to differentiable manifolds.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Implicit Function Theorem)**</ins> Let $$U\subset\mathbb{R}^{m-n}\times\mathbb{R}^n$$ be an open set, and to distinguish the two factors, denote the coordinates of $$\mathbb{R}^{m-n}$$ by $$r^1,\ldots, r^{m-n}$$ and the coordinates of $$\mathbb{R}^n$$ by $$s^1,\ldots, s^n$$. Let $$f:U\rightarrow\mathbb{R}^n$$ be $$C^\infty$$, and suppose $$f(x_0,y_0)=0$$ for some point $$(x_0, y_0)\in U$$. If at the point $$(x_0,y_0)$$ the $$n\times n$$ submatrix

$$\begin{pmatrix}\partial f^1/\partial s^1&\partial f^1/\partial s^2&\cdots&\partial f^1/\partial s^n\\\partial f^2/\partial s^1&\partial f^2/\partial s^2&\cdots&\partial f^2/\partial s^n\\\vdots&\vdots&\ddots&\vdots\\\partial f^n/\partial s^1&\partial f^n/\partial s^2&\cdots&\partial f^n/\partial s^n\end{pmatrix}$$

of the Jacobian matrix

$$\begin{pmatrix}\partial f^1/\partial r^1&\partial f^1/\partial r^2&\cdots&\partial f^1/\partial r^{m-n}&\partial f^1/\partial s^1&\partial f^1/\partial s^2&\cdots&\partial f^1/\partial s^n\\\partial f^2/\partial r^1&\partial f^2/\partial r^2&\cdots&\partial f^2/\partial r^{m-n}&\partial f^2/\partial s^1&\partial f^2/\partial s^2&\cdots&\partial f^2/\partial s^n\\ \vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\ddots&\vdots\\\partial f^n/\partial r^1&\partial f^n/\partial r^2&\cdots&\partial f^n/\partial r^{m-n}&\partial f^n/\partial s^1&\partial f^n/\partial s^2&\cdots&\partial f^n/\partial s^n\end{pmatrix}$$

is nonsingular, then there exist a suitable open neighborhood $$V$$ of $$x_0$$, a suitable open neighborhood $$W$$ of $$y_0$$, and a $$C^\infty$$ function $$g:V\rightarrow W$$ such that $$V\times W\subseteq U$$ and for each $$(p,q)\in V\times W$$,

$$f(p,q)=0\iff q=g(p)$$

holds.

</div>

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4 (Submersion Level Set Theorem)**</ins> Let $$F:M\rightarrow N$$ be $$C^\infty$$, fix $$q\in F(M)$$, and let $$P=F^{-1}(q)$$. If for every $$p\in P$$ the differential $$dF_p:T_pM\rightarrow T_{F(p)}N$$ is surjective, then there exists a unique manifold structure on $$P$$ such that the canonical injection $$\iota:P\hookrightarrow M$$ is a submanifold.

Moreover, in this case $$\iota$$ is an embedding and the codimension $$\dim M-\dim P$$ of $$P$$ equals $$\dim N$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

The hypothesis of the next corollary is weaker than that of the preceding one, so it is more widely applicable.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5 (Constant-Rank Level Set Theorem)**</ins> Let $$F:M\rightarrow N$$ be $$C^\infty$$, and suppose that the differential $$dF_p:T_pM\rightarrow T_{F(p)}N$$ defined at each $$p\in P$$ has the same rank at every point $$p\in P$$. Then $$F:M\rightarrow N$$ is an embedded submanifold.

</div>

Using these theorems, one can show that certain subsets of a given manifold $$M$$ are embedded submanifolds. This typically follows an argument such as the one below.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Consider the function from $$\mathbb{R}^{n+1}$$ to $$\mathbb{R}$$ defined by

$$f(x)=\lvert x\rvert^2=\sum_{i=1}^{n+1} r^i(x)^2.$$

For any point $$x\in \mathbb{R}^{n+1}$$ and $$v\in T_x\mathbb{R}^{n+1}$$,

$$df_x(v)=v(f)=\sum v^i\frac{\partial f}{\partial r^i}\bigg|_{x}=2\sum r^i(x) v^i$$

holds, and from this we see that if $$x$$ is not the origin, then by adjusting $$v$$ we can make $$df_x(v)$$ take any real value. That is, since $$df_x$$ is always surjective away from the origin, there exists a unique manifold structure on $$f^{-1}(1)$$ making it a submanifold of $$\mathbb{R}^{n+1}$$. By uniqueness, this structure coincides with the manifold structure given on $$S^n$$, and again by [Corollary 5](#cor5) we can see that this structure is an embedded submanifold of $$\mathbb{R}^{n+1}$$.

</div>

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
