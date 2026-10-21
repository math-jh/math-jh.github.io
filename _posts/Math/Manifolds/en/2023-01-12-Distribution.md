---
title: "Distribution"
description: "This post defines distributions on manifolds and the concept of integral manifolds, and discusses how the Frobenius theorem characterizes integrable distributions through the involutivity condition."
excerpt: "The definition of a distribution and the Frobenius theorem"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/distribution
sidebar: 
    nav: "manifolds-en"

date: 2023-01-12
weight: 14
translated_at: 2026-06-01T10:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-21T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Distribution and Integral Flow

Previously, in [§Vector Fields](/en/math/manifolds/vector_fields){: data-lid="njw4z" }, we saw that for a given manifold $M$ and any $C^\infty$ vector field $X$ defined on it, there exists a sufficiently small $\epsilon>0$ such that the following equation

$$\sigma'(t)=X(\sigma(t)),\qquad \sigma(0)=p\tag{1}$$

is satisfied by a curve $\sigma:(-\epsilon,\epsilon)\rightarrow M$. If $X_p\neq 0$, then for the curve $\sigma$ defined in this way, its image in $M$, $S$, can be viewed as a submanifold of $M$ containing the point $p$.

Meanwhile, equation (1) above enforces not only the image of $\sigma$ but also the way it is parametrized. In contrast, since the submanifold $S$ is determined independently of the parametrization of $\sigma$, it is determined not by the vector $X_p$, but solely by the 1-dimensional subspace of $T_pM$, $\span(X_p)$.

::: Definition 1
Suppose an $m$-dimensional manifold $M$ is given, and, satisfying $1\leq k\leq m$, an integer $k$ is given. A function that assigns to each $p\in M$ a subspace of $T_pM$, namely a $k$-dimensional subspace $\mathcal{D}(p)$, via $p\mapsto\mathcal{D}(p)$, is called a *$k$-dimensional distribution*.

A $k$-dimensional distribution $\mathcal{D}$ is $C^\infty$ if for each $p\in M$, there exist a suitable open neighborhood $U$ and $C^\infty$ vector fields $X_1,\ldots, X_k$ defined on it such that for each $x\in U$, the following equation

$$\mathcal{D}(x)=\span\{(X_1)_x,\ldots, (X_k)_x\}$$

holds.
:::

A nowhere-vanishing vector field $X$, as examined above, defines a 1-dimensional distribution through the map $p\mapsto\span(X_p)\subseteq T_pM$. Then the submanifold $S$ is determined so as to satisfy the following equation

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

Therefore, we define as follows.

::: Definition 2
On $M$, for a $k$-dimensional distribution $\mathcal{D}$ defined on it, a manifold satisfying the following equation

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

namely $S$, is called an *integral manifold* of $\mathcal{D}$.
:::

If for each $p\in M$, there exists an integral manifold containing $p$, it is called an *integrable* distribution.

## Frobenius Theorem

The following theorem is well known.

::: Theorem 3 (Frobenius)
On a manifold $M$, consider a $k$-dimensional $C^\infty$ distribution $\mathcal{D}$. Then $\mathcal{D}$ is integrable if and only if, for any $X,Y\in\mathcal{D}$, $[X,Y]\in\mathcal{D}$ holds.

Moreover, for any $k$-dimensional involutive distribution, the following holds:

1. For each $p\in M$, there exists, containing $p$, an integral manifold of $\mathcal{D}$.
2. Furthermore, by suitably choosing a coordinate system centered at $p$, $(U,\varphi)$, the slices defined by the following equations
    
    $$x^i=\text{constant},\qquad i>k$$

   can be made to be integral manifolds of $\mathcal{D}$.
3. Finally, if $\Phi:N\rightarrow M$ is a connected integral manifold and $\Phi(N)\subseteq U$, then $\Phi(N)$ is contained in only one of the slices from (2).
:::

A distribution satisfying the latter condition is called *involutive*. Therefore, the Frobenius theorem can be stated in short as saying that a distribution $\mathcal{D}$ is integrable if and only if it is involutive.

One direction of this theorem can be proved quite easily.

::: Lemma 4
On a manifold $M$, suppose that a smooth distribution $\mathcal{D}$ is integrable. Then $\mathcal{D}$ is an involutive distribution.
:::
::: Proof
Let $X,Y\in\mathcal{D}$ and pick a point $p\in M$. We must show that $[X,Y]_p\in\mathcal{D}(p)$. 

Since $\mathcal{D}$ is an integrable distribution, containing $p$, there exists an integral submanifold of $\mathcal{D}$, $\Phi:S\rightarrow M$. Let $s\in S$ be a point satisfying $\Phi(s)=p$. For any $x\in S$, since

$$\dd{\Phi_x}:T_xS\rightarrow\mathcal{D}(\Phi(x))$$

is an isomorphism, we can find, satisfying

$$\dd{\Phi_s}(\tilde{X}_s)=X_p,\qquad \dd{\Phi_s}(\tilde{Y}_s)=Y_p$$

two vector fields $\tilde{X},\tilde{Y}$. Then, since these and $X,Y$ are $\Phi$-related vector fields respectively, by [§Lie Derivative, ⁋Proposition 9](/en/math/manifolds/Lie_derivative#prop9){: data-lid="ikjb9" }, $[\tilde{X},\tilde{Y}]$ and $[X,Y]$ are $\Phi$-related. Therefore

$$[X,Y]_p=\dd{\Phi_s}([\tilde{X},\tilde{Y}]_s)\in\mathcal{D}(p)$$

holds. 
:::

Thus, the difficult part of the proof of [Theorem 3](#thm3){: data-lid="th7n7" } is the converse direction. This proceeds by induction on the dimension $k$ of the distribution.

::: Lemma 5
Let an $m$-dimensional manifold $M$, a point $p\in M$, and, satisfying $X_p\neq 0$, a vector field $X$ be given. Then, containing $p$, there exists a suitable coordinate system $(U,\varphi), \varphi=(x^1,\ldots, x^m)$ such that

$$X\vert_U=\frac{\partial}{\partial x^1}\bigg\vert_U$$

holds.
:::
::: Proof
Centered at the point $p$, choose a coordinate system $(V,\tau), \tau=(y^1,\ldots, y^m)$ such that

$$X_p=\frac{\partial}{\partial y^1}\bigg\vert_p$$

holds. Without loss of generality, we may assume that $V$ is sufficiently small so that for a suitable $\epsilon>0$, the function

$$(-\epsilon,\epsilon)\times V\rightarrow M;\qquad(t,q)\mapsto \phi^t(q)$$

is well-defined and $C^\infty$. ([§Vector Fields, ⁋Theorem 6](/en/math/manifolds/vector_fields#thm6){: data-lid="672vd" }) Moreover, if we choose $\epsilon>0$ and $W$ small enough that the inclusion

$$\phi^t(\tau^{-1}(\{0\}\times W))\subseteq V\quad(\lvert t\rvert<\epsilon),\qquad \text{$W$ is an open neighborhood of the origin in $\mathbb{R}^{m-1}$}$$

holds, then the function

$$\sigma: (-\epsilon,\epsilon)\times W\rightarrow M;\qquad (t,a^2,\ldots, a^m)\mapsto \phi^t(\tau^{-1}(0,a^2,\ldots, a^m))$$

is well-defined. But since

$$\dd{\sigma}\left(\frac{\partial}{\partial r^1}\bigg\vert_0\right)=\frac{\partial}{\partial y^1}\bigg\vert_p=X_p\neq 0,\qquad \dd{\sigma}\left(\frac{\partial}{\partial r^i}\bigg\vert_0\right)=\frac{\partial}{\partial y^i}\bigg\vert_p$$

holds, $\sigma$ is nonsingular at the origin, and thus $\sigma^{-1}$ defines a coordinate map.
:::

::: Proof (Theorem 3)
Assume that the theorem holds for all $k-1$-dimensional distributions, and let $\mathcal{D}$ be a $k$-dimensional distribution. For a point $p\in M$, we may assume that $\mathcal{D}$ is, in a neighborhood of $p$, spanned by $k$ vector fields $X_1,\ldots, X_k$. Now, applying [Lemma 5](#lem5){: data-lid="p5zb1" }, so that

$$X_1\vert_V=\frac{\partial}{\partial y^1}$$

holds, we can find, centered at $p$, a coordinate system $(V,\tau),\tau=(y^1,\ldots, y^m)$.

Now let us define $k$ vector fields $Y_1,\ldots, Y_k$ by the equations

$$Y_1=X_1,\qquad Y_i=X_i-(X_i(y^1))X_1\quad(i\geq 2)$$

. Since the $X_i$ are mutually independent, so are the $Y_i$.

Now let $S$ be the slice defined by $y^1=0$. Then, by restricting $Y_2,\ldots, Y_k$ to $S$, we obtain the vector fields

$$Z_i=Y_i\vert_S \qquad (i\geq 2)$$

. At this time, since the equation

$$Z_i(y^1)=Y_i(y^1)=0$$

holds, we see that the $Z_i$ are independent vector fields contained in the tangent space of $S$. Therefore, on $S$, they span a $k-1$-dimensional distribution.

Now, in order to use the induction hypothesis, let us show that this distribution is involutive. That is, we must show that for any $i,j$, $[Z_i,Z_j]\in\span(Z_2,\ldots, Z_k)$ holds.

Consider the inclusion $\iota:S\rightarrow M$. Then since the $Z_i$ and $Y_i$ are $\iota$-related, it suffices to show that $[Y_i,Y_j]\in\span(Y_2,\ldots, Y_k)$. However,

$$Y_i(y^1)=X_i(y^1)-X_i(y^1)X_1(y^1)=X_i(y^1)-X_i(y^1)=0$$

holds for all $i\geq 2$, and therefore $[Y_i,Y_j]y^1=0$. On the other hand, since $\mathcal{D}$ is involutive, we can write $[Y_i,Y_j]=\sum_{l=1}^kc_lY_l$, and applying $y^1$ to this, from $Y_1(y^1)=1$ we obtain $c_1=0$. From this we see that the $[Y_i,Y_j]$ actually belong to $\span(Y_2,\ldots, Y_k)$.

Now, applying the second assertion of the theorem to the involutive distribution on $S$, $\span(Z_2,\ldots, Z_k)$, we can choose, centered at $p\in S$, a coordinate system $(w^2,\ldots, w^m)$ such that the slices obtained from the equations

$$w^i=\text{constant},\qquad i>k$$

become integral submanifolds of $\span(Z_2,\ldots, Z_k)$.

To complete the proofs of the first and second assertions, let us define $m$ functions

$$x^1=y^1,\quad x^j=w^j\circ\pi$$

where $\pi:V\rightarrow S$ is the projection that eliminates the $y^1$ component. Now, since the $(x^i)$ are independent functions, we know that there exists a coordinate system $(U,\varphi)$ having them as component functions. Then the coordinate system defined this way satisfies the second assertion. That is, the slices defined by the equations

$$x^i=\text{constant},\qquad i>k$$

become integral manifolds of $\mathcal{D}$. To show this, it suffices to show that for each $x^{k+1},\ldots, x^m$, the $Y_i(x^{k+j})$ are all $0$.

First, from the definition of the $x^i$, we know that $\partial x^j/\partial y^1=\delta_{j1}$ holds, and therefore on $U$,

$$Y_1=\frac{\partial}{\partial x^1}$$

holds. For the remaining $Y_2,\ldots, Y_k$, first using the equation

$$\frac{\partial}{\partial x^1}Y_i(x^{k+j})=Y_1(Y_i(x^{k+j}))=[Y_1,Y_i]x^{k+j}$$

, from the condition that $\mathcal{D}$ is involutive, if we apply

$$[Y_1,Y_i]=\sum_{l=1}^k c_{il}Y_l$$

to the right-hand side, we see that

$$\frac{\partial}{\partial x^1}(Y_i(x^{k+j}))=\sum_{l=2}^k c_{il}Y_l(x^{k+j})$$

holds. Now, for a fixed slice $W$, the $Y_i(x^{k+j})$ are single-variable functions of $x^1$, and therefore the above equations become $k-1$ linear homogeneous ODEs, so the solution is uniquely determined by the initial values.

The slices obtained this way meet $S\cap U$ at only a single point, and since

$$Y_i(x^{k+j})=Z_i(w^{k+j})=0$$

holds here, the proofs of the first and second assertions are complete.

Finally, we must show the third assertion. This time, let $\pi$ be the projection from $\mathbb{R}^m$ onto the last $m-k$ coordinates. Then since the image of $\mathcal{D}$ under $\dd{(\pi\circ\varphi)}$ is $0$,

$$\dd{(\pi\circ\varphi\circ\Phi)}\equiv 0$$

holds for any $y\in N$. But since $N$ is connected, $\pi\circ\varphi\circ\Phi$ is a constant function, and therefore $\Phi(N)$ is contained in a single slice.
:::

---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
