---
title: "Smooth Manifolds"
description: "We define a differential structure through the compatibility of coordinate charts on a topological manifold, and based on this, we discuss the concept of a smooth manifold."
excerpt: "Definition of smooth manifolds"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/smooth_manifolds
sidebar: 
    nav: "manifolds-en"

date: 2022-06-06
weight: 1
translated_at: 2026-06-01T04:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-19T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We defined the notion of a topological manifold in topology; in this series of posts we deal with differentiable manifolds, and in particular smooth manifolds.

## Notation

Since we will frequently work with coordinate systems of dimension $m$, we fix the following notation. For $\mathbb{R}^m$, we denote the $i$-th projection $\pr_i$ by $r^i$. Similarly, for any set $X$ and function $f:X\rightarrow\mathbb{R}^m$, $f$'s $i$-th *component function* is defined by the formula $f^i=r^i\circ f$.

Now let $f$ be a function from $\mathbb{R}^m$ to $\mathbb{R}$. Then we define the partial derivative of $f$ with respect to the $i$-th variable by the formula

$$\frac{\partial}{\partial r^i}\bigg\vert_t f=\frac{\partial f}{\partial r^i}\bigg\vert_t=\lim_{h\rightarrow 0}\frac{f(t^1,\ldots, t^{i-1}, t^i+h, t^{i+1},\ldots, t^m)-f(t^1,\ldots, t^m)}{h}$$

As in the notation above, following **[Lee]**, for the $i$-th component, instead of $x_i$, we write $x^i$.

If each component function is $k$-times differentiable and the result is continuous, we say the function $f$ is $C^k$. For example, that a function $f:\mathbb{R}^2\rightarrow\mathbb{R}$ is $C^2$ means that the following partial derivatives

$$\frac{\partial^2 f}{\partial x^2},\quad\frac{\partial^2 f}{\partial x\partial y},\quad\frac{\partial^2 f}{\partial y\partial x},\quad\frac{\partial^2 f}{\partial y^2}$$

all exist and are continuous. If a function $f$, for every natural number $k$, is $C^k$, we call it $C^\infty$.

## Differentiable Manifolds

Unlike general topological spaces, a topological manifold locally resembles $\mathbb{R}^n$, so we can import the notion of differentiation defined there to $M$. This is possible because differentiability is essentially a local property.

::: Definition 1
Let a topological manifold $M$ be given. For $0\leq k\leq\infty$, coordinate charts $(U,\varphi)$ and $(V,\psi)$ are *$C^k$-compatible* if both *transition maps*

$$\psi\circ\varphi^{-1}:\varphi(U\cap V)\rightarrow\psi(U\cap V),\qquad\varphi\circ\psi^{-1}:\psi(U\cap V)\rightarrow\varphi(U\cap V)$$

are $C^k$. If a collection of $C^k$-compatible charts $\mathcal{A}=\{(U_\lambda, \varphi_\lambda)\}_{\lambda\in\Lambda}$ satisfies $M=\bigcup U_\lambda$, then $\mathcal{A}$ is called a *$C^k$-atlas*.

On $M$, an atlas that is maximal with respect to inclusion among $C^k$-atlases is called a *$C^k$-differentiable structure*, and in this case $M$ is called a *$C^k$-differentiable manifold*. In particular, in the case where $k=\infty$, $M$ is called a *smooth differentiable manifold* or more simply a *differentiable manifold*.
:::

The reason we think of a *maximal* atlas as giving a differentiable structure in this definition is that it is entirely possible for two non-maximal atlases to give essentially the same differentiable structure. For example, $\mathbb{R}$ has the following $C^\infty$-atlas

$$\mathcal{A}=\{(\mathbb{R}, \id_\mathbb{R})\}$$

but also has another atlas

$$\mathcal{A}'=\{((-\infty, 1), \id_{(-\infty, 1)}), ((-1, \infty),\id_{(-1,\infty)})\}$$

However, as can be seen in [Proposition 3](#prop3){: data-lid="umryd" }, if any atlas is given, the maximal atlas containing it is uniquely determined, so in an essential sense this is not such a big difference.

On the other hand, to understand an object in mathematics, it suffices to know the functions defined on it. Henceforth, all manifolds are considered to be smooth differentiable manifolds.

::: Definition 2
Consider a manifold $M$ and a point $p\in M$. For $p$, on a suitable open neighborhood $W$, that a function $f$ defined thereon is at $p$ $C^\infty$ means that, containing $p$ and belonging to the differentiable structure of $M$, for some coordinate chart $(U,\varphi)$, the function $f\circ\varphi^{-1}:\varphi(U\cap W)\rightarrow \mathbb{R}$ is at the point $\varphi(p)$ $C^\infty$.
:::

Suppose that on another open neighborhood of the point $p$, a coordinate chart $(V,\psi)$ is defined. If $f\circ\varphi^{-1}$ is at $\varphi(p)$ $C^\infty$, but $f\circ\psi^{-1}$ is not so at $\psi(p)$, then this definition is not a good definition. However, on $\psi(U\cap V)$, since

$$f\circ\psi^{-1}=(f\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

holds, $f\circ\psi^{-1}$ is at the point $\psi(p)$ $C^\infty$. By a similar argument, one can show the following.

::: Proposition 3
On a topological manifold $M$, let a $C^k$-atlas $\mathcal{A}$ be given. Then, containing $\mathcal{A}$, a maximal $C^k$-atlas exists uniquely. Therefore, any $C^k$-atlas $\mathcal{A}$ defines on $M$ a unique $C^k$-differentiable structure. 
:::

::: Proof
It suffices to define $\mathcal{A}'$ by the formula

$$\mathcal{A}'=\{(V,\psi)\mid\psi\circ\varphi_\lambda^{-1}, \varphi_\lambda\circ\psi^{-1}\text{ are $C^k$ for all $\varphi_\lambda\in\mathcal{A}$}\}$$

. Then $\mathcal{A}'$ contains $\mathcal{A}$, and therefore covers $M$ by coordinate charts. Meanwhile, if $(V,\psi)$ and $(V',\psi')$ are elements of $\mathcal{A}'$ and $V\cap V'\neq\emptyset$, then the transition map

$$\psi'\circ\psi^{-1}:\psi(V\cap V')\rightarrow\psi'(V\cap V')$$

is $C^k$. This is because for any $q\in V\cap V'$, if, satisfying $q\in U$, we choose $(U,\varphi)\in\mathcal{A}$, then on $\psi(U\cap V\cap V')$

$$\psi'\circ\psi^{-1}=(\psi'\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

so that $\psi'\circ\psi^{-1}$ is at the point $\psi(q)$ $C^k$. Since the point $q$ was chosen arbitrarily, this shows that $\psi'\circ\psi^{-1}$ is $C^k$. Of course, reversing the roles of $(V,\psi)$ and $(V',\psi')$, one can show that the transition map in the opposite direction is also $C^k$.

Naturally, by definition $\mathcal{A}'$ becomes a maximal $C^k$-atlas, and one can easily verify that it is unique. 
:::

::: Example 4
On the set of real numbers $\mathbb{R}$, let us give two atlases

$$\mathcal{A}_1=\{(\mathbb{R},\id_\mathbb{R})\},\qquad \mathcal{A}_2=\{(\mathbb{R}, x\mapsto x^3)\}$$

. Since these are atlases consisting of a single chart, they are naturally $C^\infty$. By the preceding [Proposition 3](#prop3){: data-lid="sa09h" }, there exists a differentiable structure containing each of them. However, they are not equal to each other. This is because the two charts $(\mathbb{R},\id_\mathbb{R})$ and $(\mathbb{R}, x\mapsto x^3)$ are not $C^\infty$-compatible with each other. (While $x\mapsto x^3$ is a $C^\infty$ function, its inverse function $x\mapsto x^{1/3}$ is not.)
:::

However, although the two atlases in [Example 4](#ex4){: data-lid="zz7kp" } do not give the *same* differentiable structure, they give differentiable structures that are *diffeomorphic* to each other. 

## Smooth partition of unity

Although it was possible to show that on any topological manifold a continuous partition of unity exists ([\[Topology\] §Paracompact Spaces and Partitions of Unity, ⁋Theorem 11](/en/math/topology/paracompact_spaces#thm11){: data-lid="89v4f" }), when dealing with differentiable manifolds a continuous partition of unity is of little help. For example, if we multiply an arbitrary $C^\infty$ function by a partition of unity that is only continuous, the degree of differentiability of this function will immediately be weakened.

Therefore we need to construct a smooth partition of unity, and for this it suffices to prove the following lemma.

::: Lemma 5 ($C^\infty$ Urysohn lemma)
Let real numbers $a'<a<b<b'$ be given. Then, on $[a,b]$ equal to $1$ and outside $(a',b')$ equal to $0$, there exists a $C^\infty$ function $\psi:\mathbb{R}\rightarrow[0,1]$.
:::

::: Proof
We may assume without loss of generality that $a'=-2,a=-1,b=1,b'=2$. First, define a function $f$ by

$$f(t)=\begin{cases}e^{-1/t}&t>0\\0&t\leq 0\end{cases}$$

Then in particular $f$ is always non-negative and is $C^\infty$. Now define

$$g(t)=\frac{f(t)}{f(t)+f(1-t)}$$

The denominator $f(t)+f(1-t)$ is nowhere 0 because if $t\leq 0$ then $f(1-t)>0$, if $t\geq 1$ then $f(t)>0$, and if $0<t<1$ then both are positive; therefore $g$ is $C^\infty$. Then $g$ is likewise always non-negative, its value is always less than or equal to 1, and in particular, when $t\geq 1$ the function value is identically 1, and when $t\leq 0$ the function value is identically 0. Therefore, it suffices to define $\psi$ by the formula

$$\psi(t)=g(t+2)g(2-t)$$
:::

Using the above $C^\infty$ Urysohn lemma in place of the general Urysohn lemma, we can construct a smooth partition of unity on a differentiable manifold.

---

**References**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013

---
