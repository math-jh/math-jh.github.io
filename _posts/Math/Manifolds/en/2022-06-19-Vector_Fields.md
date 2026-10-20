---
title: "Vector Fields"
description: "A vector field is defined as a section of a vector bundle, and the smoothness condition for a vector field as a section of the tangent bundle is expressed as equivalent conditions from the perspectives of coordinate systems and functions."
excerpt: "Vector fields"

categories: [Math / Manifolds]
permalink: /en/math/manifolds/vector_fields
sidebar: 
    nav: "manifolds-en"

date: 2022-06-19
weight: 11
translated_at: 2026-06-01T08:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-20T15:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Vector Fields

We defined vector bundles in the previous post partly for later use, but also because we needed them immediately to define vector fields.

::: Definition 1
For any vector bundle $\pi:E\rightarrow M$, a map $\sigma:M\rightarrow E$ satisfying $\pi\circ\sigma=\id_M$ is called a *section* of the vector bundle $E\rightarrow M$. 
:::

This definition merely says that $\sigma$ is a function taking each point $p$ to an element of $E_p$. Meanwhile, since $E$ is itself a manifold, any section $\sigma:M\rightarrow E$ is a map between two manifolds, and thus the smoothness of $\sigma$ is well-defined. We denote the collection of smooth sections of the vector bundle $E\rightarrow M$ by $\Gamma(E)$. 

In particular, for the tangent bundle $\pi:TM\rightarrow M$, a section $X$ is called a *vector field*, and at a point $p$, the value of $X$ is often written as $X_p$. Then, since $X_p\in T_pM$, near $p$, for a function $f$ defined in a neighborhood, the real number $X_p(f)$ is well-defined. In particular, if $f$ is defined on an open set $U$, the assignment sending $p\in U$ to the real number $X_p(f)$, as a function $U\rightarrow\mathbb{R}$, is denoted by $X(f)$.

::: Proposition 2
On a manifold $M$, consider a vector field $X$. The following are all equivalent.

1. $X$ is $C^\infty$.
2. For any coordinate system $(U,\varphi)$, $\varphi=(x^i)_{i=1}^m$, the functions $a^i:U\rightarrow\mathbb{R}$ defined by the formula
    
    $$(X\vert_U)_p=\sum_{i=1}^m a^i(p)\frac{\partial}{\partial x^i}\bigg\vert_p$$

    are all functions defined on $U$ that are $C^\infty$. 
3. For any open set $V\subseteq M$ and, on $V$, any $C^\infty$ function $f:V\rightarrow\mathbb{R}$, $X(f)$ is also $C^\infty$.
:::
::: Proof
First, if $X$ is $C^\infty$, then it is clear that $X\vert_U$ is $C^\infty$. Meanwhile, as functions defined on $TM$, the $\dd{x}^i$ are component functions of the coordinate system $\tilde{\varphi}:\pi^{-1}(U)\rightarrow\mathbb{R}^{2m}$, so they are likewise $C^\infty$, and therefore their composition

$$a^i(p)=\dd{x}^i\left(\sum_{j=1}^m a^j(p)\frac{\partial}{\partial x^j}\bigg\vert_p\right),\qquad\text{즉}\quad a^i=\dd{x}^i\circ(X\vert_U)$$

is also clearly $C^\infty$. 

Assume condition 2 holds. Since we must show, for any $p\in V$, that $X(f)$, at $p$, is $C^\infty$, for this it suffices to show that, on a neighborhood of $p$ with $U\subseteq V$, for a suitable coordinate system $(U,\varphi)$, $X(f)$, at $p$, is $C^\infty$. Now by condition 2,

$$(X\vert_U)_pf=\sum_{i=1}^m a^i(p)\frac{\partial f}{\partial x^i}(p)$$

and then the right-hand side is, on $U$, a $C^\infty$ function, so $X(f)$ is a $C^\infty$ function.

Finally, assume condition 3 and let us show 1. To show that $X:M\rightarrow TM$ is $C^\infty$, it suffices to show that for any coordinate system $(U,\varphi)$, the map $X\circ\varphi^{-1}$ from $\varphi(U)$ to $TM$ is a $C^\infty$ function; considering the coordinate system on $TM$, this in turn amounts to showing that the following functions

$$x^i\circ\pi\circ (X\vert_U),\quad \dd{x}^i\circ(X\vert_U)$$

are $C^\infty$. However, a direct computation shows that

$$x^i\circ\pi\circ (X\vert_U)=x^i\circ\id_U=x^i,\qquad \dd{x}^i\circ(X\vert_U)=X(x^i)$$

holds, so they are all $C^\infty$.
:::

For $M$, we denote the collection of $C^\infty$ vector fields by $\mathfrak{X}(M)$, and henceforth assume all vector fields are $C^\infty$. Meanwhile, by a partition of unity, a vector field on $M$ defined only on an open set $U$ can be made to coincide, on a sufficiently small neighborhood of each point $p\in U$, with a vector field defined on all of $M$. ([§Tangent Space, ⁋footnote 1](/en/math/manifolds/tangent_space#fn:1){: data-lid="h3g4f" })

## Local frame

For the space $\mathfrak{X}(M)$, the addition of two elements $X,Y$ is well-defined as follows:

$$(X+Y)_p=X_p+Y_p$$

Also, if for any real number $\alpha\in\mathbb{R}$ we define

$$(\alpha X)_p=\alpha\cdot X_p$$

then $\alpha X$ is also an element of $\mathfrak{X}(M)$, so $\mathfrak{X}(M)$ becomes an $\mathbb{R}$-vector space. However, as an $\mathbb{R}$-vector space, $\mathfrak{X}(M)$ is too large.

::: Example 3
Let $M=\mathbb{R}$. Here we consider $M$ as being given a manifold structure via a single chart $(\mathbb{R},\id)$. Then at each point $p$, the tangent space $T_pM$ is a 1-dimensional vector space spanned by $d/\dd{x}\vert_p$, and thus the correspondence

$$X:M\rightarrow TM;\qquad p\mapsto \frac{d}{\dd{x}}\bigg\vert_p$$

is an element of $\mathfrak{X}(M)$. However, for any $C^\infty$ function $f:\mathbb{R}\rightarrow\mathbb{R}$,

$$fX:M\rightarrow TM;\qquad p\mapsto f(p)\frac{d}{\dd{x}}\bigg\vert_p$$

also belongs to $\mathfrak{X}(M)$ ([Proposition 2](#prop2){: data-lid="6qzn8" }), and unless $f$ is a constant function, $fX$ cannot be expressed as a constant multiple of $X$. Furthermore, since $C^\infty(M)$ is an infinite-dimensional vector space over $\mathbb{R}$, $\mathfrak{X}(M)$ is also an infinite-dimensional vector space.
:::

In a situation such as the above, viewing $\mathfrak{X}(M)$ as a $C^\infty(M)$-module makes it relatively easier to handle $\mathfrak{X}(M)$.

Above, $\mathfrak{X}(M)$ was generated by the vector field $d/\dd{x}$, but in general, since $C^\infty(M)$ is not a field, there can very well exist $C^\infty(M)$-modules that do not have a basis. For example, the well-known [hairy ball theorem](https://en.wikipedia.org/wiki/Hairy_ball_theorem) shows that for any continuous vector field defined on the unit sphere $S^2$ in 3-dimensional space, there necessarily exists a point where it is $0$.

{% diagram Math/Manifolds/Vector_Fields-1.png width="200px" alt="Hairy_ball" %}

Suppose that on the $2$-manifold $M=S^2$, two vector fields $X_1,X_2$ generate $\mathfrak{X}(M)$ as a $C^\infty(M)$-module. Then from the hairy ball theorem, there exists a point satisfying $X_1(p)=0$, $p\in S^2$. Then $T_pM$ must be generated by $\{0,X_2(p)\}$, which contradicts that $T_pM$ is 2-dimensional. Therefore, $\mathfrak{X}(M)$ cannot be generated by the two vector fields $\{X_1,X_2\}$.

On the other hand, for a sufficiently small open set $U$, the collection of vector fields defined on $U$, $\mathfrak{X}(U)$, can be regarded as being generated by $m$ vector fields as a $C^\infty(U)$-module. For the tangent bundle $\pi: TM\rightarrow M$, if we take the open set $U$ sufficiently small, we can find a local trivialization $h:U\times\mathbb{R}^m\rightarrow\pi^{-1}(U)$; if we define the vector fields $X_1,\ldots, X_m$ by

$$X_1(p)=h(p, e_1),\quad X_2(p)=h(p,e_2),\quad\ldots,\quad X_m(p)=h(p,e_m)\tag{1}$$

they generate $\mathfrak{X}(U)$.

::: Definition 4
Suppose a manifold $M$ is given, and let $\dim M=m$.

- That $X_1,\ldots, X_k$, on a subset of $M$, $A$, are *linearly independent* means that for each $p\in A$, the vectors in $T_pM$, $X_1(p),\ldots, X_k(p)$, are linearly independent.
- That $X_1,\ldots, X_k$, on a subset of $M$, $A$, *span* the tangent bundle $TM$ means that for each $p\in A$, the vectors in $T_pM$, $X_1(p),\ldots, X_k(p)$, span $T_pM$.
- If, on an open set $U\subseteq M$, linearly independent vector fields $X_1,\ldots, X_k$ span the tangent bundle on $U$, they are called a *local frame* of $M$.
- If in the above definition we can take $U=M$, these vector fields are called a *global frame* of $M$.
:::

Therefore, from the discussion above, we see that a parallelizable manifold has a global frame. Conversely, if a manifold $M$ has a global frame $X_1,\ldots, X_m$, then by defining a map $TM\rightarrow M\times\mathbb{R}^m$ by

$$(p,a_1X_1(p)+\cdots+a_mX_m(p))\mapsto (p,a_1e_1+\cdots+a_me_m)$$

we can verify that $M$ is a parallelizable manifold.


## Integral flow

::: Definition 5
On a manifold $M$, a $C^\infty$ curve $\sigma$ is said to be an *integral flow* of $X\in\mathfrak{X}(M)$ if $\sigma'(t)=X(\sigma(t))$ holds for all $t$.
:::

The following theorem is easily obtained from ordinary differential equations, but since the proof itself lies outside our interest, we omit it. Also, from item 4 of the theorem onward, a few additional definitions are required.

::: Theorem 6
Consider a manifold $M$ and $X\in\mathfrak{X}(M)$. Whenever an arbitrary $p\in M$ is given, there exist suitable constants $a(p), b(p)$ (including $\pm\infty$) and a $C^\infty$ curve $\phi_p: \bigl(a(p),b(p)\bigr)\rightarrow M$ satisfying the following conditions. 

1. $0\in \bigl(a(p),b(p)\bigr)$, $\phi_p(0)=p$.
2. $\phi_p$ is an integral flow of $X$.
3. If $\mu:(c,d)\rightarrow M$ is a $C^\infty$ function satisfying the above two conditions, then $(c,d)\subseteq \bigl(a(p),b(p)\bigr)$, and $\mu$ is identical to the restriction of $\phi_p$ to $(c,d)$.
4. For each $p\in M$, there exist a suitable open neighborhood $V$ and a positive number $\epsilon$ such that $(t,p)\mapsto \phi^{t}(p):=\phi_p(t)$ is well-defined, and this function is a $C^\infty$ function from $(-\epsilon,\epsilon)\times V$ to $M$.
5. For any $t$, $\mathcal{D}_t=\left\{p\in M\mid t\in\bigl(a(p),b(p)\bigr)\right\}$ is an open set.
6. $\bigcup_{t>0}\mathcal{D}_t=M$.
7. $\phi^{t}:\mathcal{D}_t\rightarrow\mathcal{D}_{-t}$ is a diffeomorphism, and its inverse is $\phi^{-t}$.
8. The domain of $\phi^s\circ \phi^t$ is contained in $\mathcal{D}_{s+t}$, and in particular, when $s$ and $t$ have the same sign, the domain of this function is exactly identical to $\mathcal{D}_{s+t}$. Also, on this domain, $\phi^s\circ \phi^t=\phi^{t+s}$.
:::

Even if the proof is omitted, it is necessary to completely understand what this theorem means. 

First, the contents of items 1 through 3 of the above theorem show that for each $p\in M$, a maximal integral flow corresponds, and this is uniquely determined except for the setting of time $t$. 

To understand the remainder of the theorem, an additional explanation of the notation is needed. First, the function $\phi^{t}(p)$ in condition 4 is a function defined, as in the definition, by 

$$\phi^{t}(p)=\phi_p(t)$$

where the initial value means that when time is $0$, it is fixed to $\phi_p(0)=p$. In this case, we denote the domain of $\phi^{t}$ by  

$$\mathcal{D}_t=\left\{p\in M\mid t\in\bigl(a(p),b(p)\bigr)\right\}$$

That is, $\phi^{t}$ can be thought of as a function representing the position where a point that, at time $0$, was at point $p$ will be after $t$ seconds when moving along the integral flow, and $\mathcal{D}_t$ is the collection of points for which it is possible to move for $t$ seconds along the integral flow in this way. 

Now, setting aside the technical results 4 and 5, the next result that appears is result 6, which is in fact nothing more than stating the existence of integral flows in a different way. The result of 7 shows that integral flows do not mix with each other. 

The result of 8 also has a somewhat technical aspect: if $s$ and $t$ had different signs, say $s=-2$ and $t=1$, then the domain of $\phi^s\circ\phi^t$ would not simply be $\mathcal{D}_{-1}$, but rather the set consisting only of those points among the elements of $\mathcal{D}_{-1}$ for which it is also possible to proceed along $\phi_p$ for 1 second.


::: Definition 7
We say that $X\in\mathfrak{X}(M)$ is *complete* if for all $t$, $\mathcal{D}_t=M$. In this case, the $\phi^t$ form a group under $\circ$, which is called the *one-parameter group* of $X$. 
:::

If $X$ is not complete, there is a slight problem with the domains of the $\phi^t$ as above, making it difficult to think of them as a group. A more subtle case is when the original vector field $X$ varies with time, but since this case is not yet our concern, we pass over it.


---

**References**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012

---
