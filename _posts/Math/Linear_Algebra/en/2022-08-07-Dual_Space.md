---
title: "Dual Space"
description: "Starting with the definitions of dual spaces and dual bases, this post compares the dimension relationships in finite and infinite dimensions, and covers the natural injective map into the double dual space. It also examines the concepts of bilinear maps and non-degenerate pairings."
excerpt: "Dual spaces, dual maps, and orthogonal complements"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/dual_space
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-05

weight: 19
translated_at: 2026-05-31T23:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-16T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Dual Basis

Let $V$ be a finite-dimensional $\mathbb{K}$-vector space. From [§Space of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5){: data-lid="uyyak" }, taking $W=\mathbb{K}$, we know that $V^\ast=\Hom(V,\mathbb{K})$ has the same dimension as $V$. In particular, if $\mathcal{B}=\{x_1,\ldots, x_n\}$ is a basis of $V$, then for the linear maps sending only $x_i$ to 1 and the remaining $x_j$ to 0, denoted $\xi^i$, we know that their collection

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\}$$

forms a basis of $V^\ast$. We call this the *dual basis* of $\mathcal{B}$.

Even when $V$ is infinite-dimensional, for a basis $\mathcal{B}$, the fact that the set $\mathcal{B}^\ast$ defined as above is linearly independent follows from the exact same proof as in [§Space of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5){: data-lid="uwc13" }, without any modification. Hence $\dim V\leq\dim V^\ast$ always holds. However, if $V$ is infinite-dimensional, $\mathcal{B}^\ast$ fails to be a basis of $V^\ast$. To see this, it suffices to verify that the function obtained by extending the function that sends every element of an arbitrary $\mathcal{B}$ to $1$ cannot be expressed as a linear combination of elements of $\mathcal{B}^\ast$. In fact, in this case, necessarily $\dim V<\dim V^\ast$.

## Double Dual Space

When $V$ is finite-dimensional, $V$ and $V^\ast$ have the same dimension, and therefore the dual space of $V^\ast$, $V^{\ast\ast}$, also has the same dimension as $V^\ast$ as a $\mathbb{K}$-vector space. We call this the *double dual* of $V$.

To show that $V$ and $V^\ast$ are isomorphic, we had to choose a specific basis. By contrast, we can construct an injective linear map from $V$ to $V^{\ast\ast}$ that is *independent of the choice of basis*. Since $V$ and $V^{\ast\ast}$ have the same dimension, this injective linear map must be an isomorphism.

::: Definition 1
Given three $\mathbb{K}$-vector spaces $U,V,W$, a function $f:U\times V\rightarrow W$ is called *bilinear* if for any $u,u_1,u_2\in U$, $v,v_1,v_2\in V$, and scalar $\alpha$,

$$f(u_1+u_2,v)=f(u_1,v)+f(u_2,v),\qquad f(u,v_1+v_2)=f(u,v_1)+f(u,v_2),\qquad f(\alpha u,v)=\alpha f(u,v)=f(u,\alpha v)$$

hold.
:::

In other words, for any $u\in U$ the function $f(u,-):V\rightarrow W$ is linear, and for any $v\in V$, $f(-,v):U\rightarrow W$ is also linear.

::: Definition 2
Given two $\mathbb{K}$-vector spaces $V,W$, a *pairing* of $V$ and $W$ is a bilinear map $(-,-):V\times W\rightarrow \mathbb{K}$. If for every nonzero $v\in V$ the linear map

$$(v,-): W\rightarrow \mathbb{K}$$

is never the zero function, then this pairing is called *non-degenerate on the left*; similarly, if for every nonzero $w\in W$ the map

$$(-,w):V\rightarrow \mathbb{K}$$

is never the zero function, then this pairing is called *non-degenerate on the right*. A pairing that is non-degenerate on both the left and the right is simply called a *non-degenerate pairing*.
:::

The notation $(-,-)$ coincides with that for ordered pairs, which may cause some confusion, but we use this notation because it is convenient and the two are not difficult to distinguish from context.

For example, on $V=W=\mathbb{R}^n$, the dot product of vectors $(-,-):\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}$ is a non-degenerate pairing. First, it is obvious that the equations

$$(v,w_1+w_2)=(v,w_1)+(v,w_2),\qquad (v_1+v_2,w)=(v_1,w)+(v_2,w),\qquad (\alpha v,w)=\alpha(v,w)=(v,\alpha w)$$

hold. Therefore, the dot product of vectors is a pairing. Meanwhile, for any nonzero vector $v$ we have $(v,v)=\lVert v\rVert^2\neq 0$, so the non-degeneracy condition is also satisfied.

When $V=W$ as above, a pairing is sometimes specifically called a *bilinear form*. The example we will use in this post is the following.

::: Example 3
For any $\mathbb{K}$-vector space $V$ and $V$'s dual space $V^\ast$, if we define $(-,-):V\times V^\ast\rightarrow \mathbb{K}$ by the formula

$$(v,f)=f(v)$$

then $(-,-)$ is a non-degenerate pairing. First, for fixed $v\in V$ and arbitrary $f,g\in V^\ast$,

$$(v,f+g)=(f+g)(v)=f(v)+g(v)=(v,f)+(v,g)$$

and, also for fixed $f\in V^\ast$ and arbitrary $v_1,v_2\in V$,

$$(v_1+v_2,f)=f(v_1+v_2)=f(v_1)+f(v_2)=(v_1,f)+(v_2,f)$$

hold. Similarly, for any scalar $\alpha$,

$$(\alpha v,f)=f(\alpha v)=\alpha f(v)=(\alpha f)(v)=(v,\alpha f)$$

holds, so $(-, -)$ is a pairing.

Furthermore, $(-,-)$ is non-degenerate. First, if an arbitrary $f\in V^\ast$ is not 0, then $f(v)\neq 0$ for some $v$, so it is obvious that $(-,-)$ is non-degenerate on the right. Also, for any nonzero vector $v$, after finding a basis containing $v$, $\mathcal{B}$, and constructing the dual basis as above, for $v$'s corresponding element $\xi$ of the dual basis we have $(v,\xi)=1$, so $(-,-)$ is also non-degenerate on the left.

From this, we see that $(-,-)$ is a non-degenerate pairing. We call this the *canonical pairing*.
:::

::: Proposition 4
Given a non-degenerate pairing $(-,-):V\times W\rightarrow \mathbb{K}$ on two $\mathbb{K}$-vector spaces $V,W$, the formula

$$v\mapsto (v,-)$$

defines a function $V\rightarrow W^\ast$ that is an injective linear map. Similarly, the formula

$$w\mapsto (-,w)$$

defines a function $W\rightarrow V^\ast$ that is also an injective linear map.
:::
::: Proof
That this function is a linear map is obvious since $(-,-)$ is linear in each component. That these functions are injective is exactly the statement that $(-,-)$ is non-degenerate on the left and on the right.
:::

::: Corollary 5
Given a non-degenerate pairing $(-,-):V\times W\rightarrow \mathbb{K}$, two *finite-dimensional* $\mathbb{K}$-vector spaces $V,W$ are isomorphic.
:::
::: Proof
From the two inequalities

$$\dim V\leq\dim W^\ast=\dim W,\qquad \dim W\leq\dim V^\ast=\dim V$$

this is immediate.
:::

In this sense, a non-degenerate pairing between two finite-dimensional vector spaces is sometimes called a *perfect pairing*. In particular, applying this corollary to the canonical pairing with $W=V^\ast$ from [Example 3](#ex3){: data-lid="df5k7" }, we obtain an isomorphism from $V$ to $V^{\ast\ast}$. Explicitly, for any $f\in V^\ast$, the formula

$$\ev_v:f\mapsto f(v)$$

defines the *evaluation map*, in terms of which this function may be understood. The discussion above shows that, defined by $v\mapsto \ev_v$, the map $V\rightarrow V^{\ast\ast}$ is an isomorphism.

## Dual Map

Suppose we are given two $\mathbb{K}$-vector spaces $V,W$ and a linear map $L:V\rightarrow W$. Then we can define a function $L^\ast:W^\ast\rightarrow V^\ast$ by the formula

$$L^\ast(f)=f\circ L$$

In diagram form, this is as follows.

{% diagram Math/Linear_Algebra/Dual_Space-1.svg width="5.84em" alt="dual_map" %}

Alternatively, according to the canonical pairing defined above, $L^\ast$ can be regarded as being defined by the formula

$$(Lv, f)=(v,L^\ast f)\qquad\text{for all $v\in V$ and $f\in W^\ast$}\tag{1}$$

Of course, $(-,-)$ on the left-hand side is the canonical pairing on $W$, and $(-,-)$ on the right-hand side is the canonical pairing on $V$.

Now suppose in particular that $V,W$ are both finite-dimensional $\mathbb{K}$-vector spaces. For $V$, let $\mathcal{B}=\{x_1,\ldots, x_n\}$ be a basis, and for $W$, let $\mathcal{C}=\{y_1,\ldots, y_m\}$ be a basis, and let their respective dual bases be

$$\mathcal{B}^\ast=\{\xi^1,\ldots,\xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

By [§Fundamental Theorem of Linear Algebra](/en/math/linear_algebra/ftla){: data-lid="6p4pa" }, every linear map can be represented by a matrix once bases are chosen; hence we can represent $L^\ast$ as a matrix with respect to the two bases $\mathcal{C}^\ast$ and $\mathcal{B}^\ast$. First, suppose $L$ is represented with respect to the bases $\mathcal{B},\mathcal{C}$ by the matrix

$$[L]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}$$

That is,

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

holds. Now, to represent $L^\ast$ as a matrix, it suffices to know where each element of $\mathcal{C}^\ast$ is sent. For any $\upsilon^k\in\mathcal{C}^\ast$, we have $L^\ast(\upsilon^k)=\upsilon^k\circ L$, and as an element of $V^\ast$, this function is expressed as a linear combination of the elements of $\mathcal{B}^\ast$.

$$\begin{aligned}L^\ast(\upsilon^1)&=\beta_{11}\xi^1+\beta_{21}\xi^2+\cdots+\beta_{n1}\xi^n\\L^\ast(\upsilon^2)&=\beta_{12}\xi^1+\beta_{22}\xi^2+\cdots+\beta_{n2}\xi^n\\&\phantom{a}\vdots\\L^\ast(\upsilon^m)&=\beta_{1m}\xi^1+\beta_{2m}\xi^2+\cdots+\beta_{nm}\xi^n\end{aligned}$$

Suppose these relations hold. Then, to find the coefficients $\beta_{lk}$, we consider the equation

$$L^\ast(\upsilon^k)=\beta_{1k}\xi^1+\cdots+\beta_{lk}\xi^l+\cdots+\beta_{nk}\xi^n$$

and substitute $x_l$ into both sides. Doing so, the right-hand side yields $\beta_{lk}$, while the left-hand side becomes

$$L^\ast(\upsilon^k)(x_l)=\upsilon^k(L(x_l))=\upsilon^k(\alpha_{1l}y_1+\cdots+\alpha_{ml}y_m)=\alpha_{kl}$$

Thus $\beta_{lk}=\alpha_{kl}$ holds, and the matrix representation of $L^\ast$ satisfies the equation

$$[L^\ast]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}=\begin{pmatrix}\alpha_{11}&\alpha_{21}&\cdots&\alpha_{m1}\\\alpha_{12}&\alpha_{22}&\cdots&\alpha_{m2}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{1n}&\alpha_{2n}&\cdots&\alpha_{mn}\end{pmatrix}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}^t=\bigl([L]_\mathcal{C}^\mathcal{B}\bigr)^t$$

In other words, the transpose matrix is nothing other than the matrix corresponding to the matrix representation of the dual map.

## Orthogonal Complement

First, the following proposition holds.

::: Proposition 6
Suppose we are given two $\mathbb{K}$-vector spaces $V,W$, a linear map $L:V\rightarrow W$, and its dual $L^\ast:W^\ast\rightarrow V^\ast$.

1. If $L$ is injective, then $L^\ast$ is surjective.
2. If $L$ is surjective, then $L^\ast$ is injective.
:::
::: Proof
Both claims are immediate from [§Space of Linear Maps, ⁋Corollary 2](/en/math/linear_algebra/space_of_linear_maps#cor2){: data-lid="tuwru" }.

1. If $L$ is injective, then $R\circ L=\id_V$ holds for some $R:W\rightarrow V$. Therefore, for any $f\in V^\ast$, the composition $f\circ R$ is a function from $W$ to $\mathbb{K}$, i.e., an element of $W^\ast$, and satisfies

    $$L^\ast(f\circ R)=(f\circ R)\circ L=f\circ(R\circ L)=f\circ\id_V=f$$
    
    so $L^\ast$ is surjective.
2. If $L$ is surjective, then $L\circ S=\id_W$ holds for some $S:W\rightarrow V$. Therefore, if some $f\in W^\ast$ satisfies $L^\ast(f)=0$, then

    $$L^\ast(f)=f\circ L=0\implies 0=(f\circ L)\circ S=f\circ(L\circ S)=f\circ\id_W=f$$

    so $L^\ast$ is injective.
:::

This proposition suggests a specific relationship between $\ker L$ and $\im L^\ast$, and between $\im L$ and $\ker L^\ast$. First, we make the following definition.

::: Definition 7
Suppose a canonical pairing $(-,-)$ is given on a $\mathbb{K}$-vector space $V$, and consider an arbitrary subset $S\subseteq V$. The collection of all elements that for every $v\in S$ satisfy $(v,f)=0$, where $f\in V^\ast$, is called the *orthogonal complement* or *annihilator* of $S$, and is denoted by $S^\perp$.

Similarly, suppose we are given an arbitrary subset $T\subseteq V^\ast$. Then the collection of all elements that for every $f\in T$ satisfy $(v,f)=0$, where $v\in V$, is called the orthogonal complement of $T$ and is denoted by $T^\perp$.
:::

In particular, when $S$ or $T$ is a singleton, we also write this as $v^\perp$ or $f^\perp$.

For any $v\in V$, the fact that $v^\perp$ is a subspace of $V^\ast$ is obvious from the bilinearity of $(-,-)$. Now, using the equality

$$S^\perp=\bigcap_{v\in S}v^\perp$$

and [§Basis of a Vector Space, ⁋Lemma 3](/en/math/linear_algebra/basis#lem3){: data-lid="ymlyq" }, we see that $S^\perp$ is a subspace of $V^\ast$. Similarly, for any $T\subseteq V^\ast$, the set $T^\perp$ is a subspace of $V$.

::: Proposition 8
Suppose we are given two $\mathbb{K}$-vector spaces $V,W$, a linear map $L:V\rightarrow W$, and its dual $L^\ast:W^\ast\rightarrow V^\ast$. For any subspace $U\subseteq V$ and its orthogonal complement $U^\perp$,

$$L(U)^\perp=(L^\ast)^{-1}(U^\perp)$$

holds.
:::
::: Proof
If we use equation (1), which defines the dual map $L^\ast$ via the canonical pairing, then for any $\upsilon\in W^\ast$,

$$\upsilon\in L(U)^\perp\iff (L(u),\upsilon)=0\text{ for all $u\in U$}\iff (u, L^\ast(\upsilon))=0\text{ for all $u\in U$}\iff L^\ast(\upsilon)\in U^\perp$$

holds.
:::

::: Corollary 9
Suppose we are given two $\mathbb{K}$-vector spaces $V,W$, a linear map $L:V\rightarrow W$, and its dual $L^\ast:W^\ast\rightarrow V^\ast$. Then $(\im L)^\perp=\ker(L^\ast)$ holds.
:::
::: Proof
It suffices to take $U=V$ in [Proposition 8](#prop8){: data-lid="xy9rh" }. From the non-degeneracy condition of the canonical pairing $(-,-)$, we have $U^\perp=\{0\}$, yielding the desired result.
:::

In [Proposition 8](#prop8){: data-lid="dbwpx" }, instead of $U\subseteq V$, we could have started with $U\subseteq W^\ast$. In this case, we obtain the following proposition.

::: Proposition 10
Suppose we are given two $\mathbb{K}$-vector spaces $V,W$, a linear map $L:V\rightarrow W$, and its dual $L^\ast:W^\ast\rightarrow V^\ast$. For any subspace $U\subseteq W^\ast$ and its orthogonal complement $U^\perp$,

$$\bigl(L^\ast(U)\bigr)^\perp=L^{-1}(U^\perp)$$

holds.
:::
::: Proof
This too is immediate using equation (1), since for any $x\in V$,

$$x\in \bigl(L^\ast(U)\bigr)^\perp\iff (x, L^\ast(\upsilon))=0\text{ for all $\upsilon\in U$}\iff (L(x),\upsilon)=0\text{ for all $\upsilon\in U$}\iff L(x)\in U^\perp$$
:::

::: Corollary 11
Suppose we are given two $\mathbb{K}$-vector spaces $V,W$, a linear map $L:V\rightarrow W$, and its dual $L^\ast:W^\ast\rightarrow V^\ast$. Then $\bigl(\im L^\ast\bigr)^\perp=\ker L$.
:::
::: Proof
It suffices to take $U=W^\ast$ in [Proposition 10](#prop10){: data-lid="jzl2f" }. From the non-degeneracy condition of the canonical pairing $(-,-)$, we have $U^\perp=\{0\}$, which yields the desired result.
:::

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Bou]** Bourbaki, N. *Algebra I*, Elements of Mathematics. Springer-Verlag Berlin, 1998.

---
