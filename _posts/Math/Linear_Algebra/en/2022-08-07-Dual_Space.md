---
title: "Dual Space"
description: "Starting with the definitions of dual spaces and dual bases, this post compares the dimension relationships in finite and infinite dimensions, and covers the natural injective map into the double dual space. It also examines the concepts of bilinear maps and non-degenerate pairings."
excerpt: "Dual spaces, dual maps, and orthogonal complements"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/dual_space
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-05
last_modified_at: 2022-08-05

weight: 115
translated_at: 2026-05-31T23:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T23:30:04+00:00
---
## Dual Basis

Let $$V$$ be a finite-dimensional $$\mathbb{K}$$-vector space. From [§Space of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5), taking $$W=\mathbb{K}$$, we know that $$V^\ast=\Hom(V,\mathbb{K})$$ has the same dimension as $$V$$. In particular, if $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ is a basis of $$V$$, then the collection of linear maps $$\xi^i$$ sending $$x_i$$ to 1 and every other $$x_j$$ to 0

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\}$$

forms a basis of $$V^\ast$$. We call this the *dual basis* of $$\mathcal{B}$$.

Even when $$V$$ is infinite-dimensional, the linear independence of the set $$\mathcal{B}^\ast$$ defined as above for any basis $$\mathcal{B}$$ follows from exactly the same proof as in [§Space of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5), without any modification. Hence $$\dim V\leq\dim V^\ast$$ always holds, and in fact, if $$V$$ is infinite-dimensional then necessarily $$\dim V<\dim V^\ast$$. To see this, it suffices to verify that the function obtained by extending the map sending every element of an arbitrary $$\mathcal{B}$$ to $$1$$ cannot be expressed as a linear combination of elements of $$\mathcal{B}^\ast$$.

## Double Dual Space

When $$V$$ is finite-dimensional, $$V$$ and $$V^\ast$$ have the same dimension, and therefore the dual space $$V^{\ast\ast}$$ of $$V^\ast$$ is also a $$\mathbb{K}$$-vector space with the same dimension as $$V^\ast$$. We call this the *double dual* of $$V$$.

To show that $$V$$ and $$V^\ast$$ are isomorphic, we had to choose a specific basis. By contrast, we can construct an injective linear map from $$V$$ to $$V^{\ast\ast}$$ that is *independent of the choice of basis*. Since $$V$$ and $$V^{\ast\ast}$$ have the same dimension, this injective linear map must be an isomorphism.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Given three $$\mathbb{K}$$-vector spaces $$U,V,W$$, a function $$f:U\times V\rightarrow W$$ is called *bilinear* if for any $$u,u_1,u_2\in U$$, $$v,v_1,v_2\in V$$, and scalar $$\alpha$$,

$$f(u_1+u_2,v)=f(u_1,v)+f(u_2,v),\qquad f(u,v_1+v_2)=f(u,v_1)+f(u,v_2),\qquad f(\alpha u,v)=\alpha f(u,v)=f(u,\alpha v)$$

hold.

</div>

In other words, for any $$u\in U$$ the function $$f(u,-):V\rightarrow W$$ is linear, and for any $$v\in V$$ the function $$f(-,v):U\rightarrow W$$ is also linear.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Given two $$\mathbb{K}$$-vector spaces $$V,W$$, a *pairing* of $$V$$ and $$W$$ is a bilinear map $$(-,-):V\times W\rightarrow \mathbb{K}$$. If for every nonzero $$v\in V$$ the linear map

$$(v,-): W\rightarrow \mathbb{K}$$

is never the zero function, then this pairing is called *non-degenerate on the left*; similarly, if for every nonzero $$w\in W$$ the map

$$(-,w):U\rightarrow \mathbb{K}$$

is never the zero function, then this pairing is called *non-degenerate on the right*. A pairing that is non-degenerate on both the left and the right is simply called a *non-degenerate pairing*.

</div>

The notation $$(-,-)$$ coincides with that for ordered pairs, which may cause some confusion, but the two are easily distinguished from context, and the notation is convenient; we therefore adopt it.

For example, the dot product of vectors $$(-,-):\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}$$ on $$V=W=\mathbb{R}^n$$ is a non-degenerate pairing. First,

$$(v,w_1+w_2)=(v,w_1)+(v,w_2),\qquad (v_1+v_2,w)=(v_1,w)+(v_2,w),\qquad (\alpha v,w)=\alpha(v,w)=(v,\alpha w)$$

hold trivially, so the dot product is indeed a pairing. Moreover, for any nonzero vector $$v$$ we have $$(v,v)=\lVert v\rVert^2\neq 0$$, so the non-degeneracy condition is also satisfied.

When $$V=W$$ as above, a pairing is sometimes called a *bilinear form*. The example we use in this post is the following.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> For any $$\mathbb{K}$$-vector space $$V$$ and its dual space $$V^\ast$$, define $$(-,-):V\times V^\ast\rightarrow \mathbb{K}$$ by

$$(v,f)=f(v)$$

Then $$(-,-)$$ is a non-degenerate pairing. First, for fixed $$v\in V$$ and arbitrary $$f,g\in V^\ast$$,

$$(v,f+g)=(f+g)(v)=f(v)+g(v)=(v,f)+(v,g)$$

and for fixed $$f\in V^\ast$$ and arbitrary $$v_1,v_2\in V$$,

$$(v_1+v_2,f)=f(v_1+v_2)=f(v_1)+f(v_2)=(v_1,f)+(v_2,f)$$

hold. Similarly, for any scalar $$\alpha$$,

$$(\alpha v,f)=f(\alpha v)=\alpha f(v)=(\alpha f)(v)=(v,\alpha f)$$

holds, so $$(-,-)$$ is a pairing. Furthermore, $$(-,-)$$ is non-degenerate. If any $$f\in V^\ast$$ is nonzero, then there exists $$v$$ with $$f(v)\neq 0$$, so $$(-,-)$$ is non-degenerate on the right. Also, for any nonzero vector $$v$$, choose a basis $$\mathcal{B}$$ containing $$v$$ and construct its dual basis as above; for the element $$\xi$$ of the dual basis corresponding to $$v$$, we have $$(v,\xi)=1$$, so $$(-,-)$$ is also non-degenerate on the left.

Thus $$(-,-)$$ is a non-degenerate pairing. We call this the *canonical pairing*.

</div>

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Given two $$\mathbb{K}$$-vector spaces $$V,W$$ with a non-degenerate pairing $$(-,-):V\times W\rightarrow \mathbb{K}$$, the function $$V\rightarrow W^\ast$$ defined by

$$v\mapsto (v,-)$$

is an injective linear map. Similarly, the function $$W\rightarrow V^\ast$$ defined by

$$w\mapsto (-,w)$$

is also an injective linear map.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That these functions are linear maps is obvious since $$(-,-)$$ is linear in each argument. That they are injective is exactly the statement that $$(-,-)$$ is non-degenerate on the left and on the right.

</details>

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Two *finite-dimensional* $$\mathbb{K}$$-vector spaces $$V,W$$ with a non-degenerate pairing $$(-,-):V\times W\rightarrow \mathbb{K}$$ are isomorphic.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is immediate from the two inequalities

$$\dim V\leq\dim W^\ast=\dim W,\qquad \dim W\leq\dim V^\ast=\dim V.$$

</details>

In this sense, a non-degenerate pairing between two finite-dimensional vector spaces is sometimes called a *perfect pairing*. Applying this corollary to the canonical pairing of [Example 3](#ex3) with $$W=V^\ast$$, we obtain an isomorphism from $$V$$ to $$V^{\ast\ast}$$. Explicitly, this function is the *evaluation map*

$$\ev_v:f\mapsto f(v)$$

for any $$f\in V^\ast$$. The discussion above shows that the map $$V\rightarrow V^{\ast\ast}$$ defined by $$v\mapsto \ev_v$$ is an isomorphism.

## Dual Map

Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces and let $$L:V\rightarrow W$$ be a linear map. Then we can define a function $$L^\ast:W^\ast\rightarrow V^\ast$$ by

$$L^\ast(f)=f\circ L$$

In diagram form, this is as follows.

![dual_map](/assets/images/Math/Linear_Algebra/Dual_Space-1.png){:style="width:6em" class="invert" .align-center}

Equivalently, by the canonical pairing defined above, $$L^\ast$$ can be characterized by

$$(Lv, f)=(v,L^\ast f)\qquad\text{for all $v\in V$ and $f\in W^\ast$}\tag{1}$$

Here the pairing $$(-,-)$$ on the left-hand side is the canonical pairing of $$W$$, and the pairing $$(-,-)$$ on the right-hand side is the canonical pairing of $$V$$.

Now suppose in particular that $$V$$ and $$W$$ are both finite-dimensional $$\mathbb{K}$$-vector spaces. Let $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ be a basis of $$V$$ and $$\mathcal{C}=\{y_1,\ldots, y_m\}$$ a basis of $$W$$, with dual bases

$$\mathcal{B}^\ast=\{\xi^1,\ldots,\xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

respectively. By [§Fundamental Theorem of Linear Algebra](/en/math/linear_algebra/ftla), every linear map can be represented by a matrix once bases are chosen; hence we can represent $$L^\ast$$ as a matrix with respect to the bases $$\mathcal{C}^\ast$$ and $$\mathcal{B}^\ast$$.

First, suppose $$L$$ is represented by the following matrix with respect to $$\mathcal{B}$$ and $$\mathcal{C}$$:

$$[L]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}$$

That is,

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

holds. To represent $$L^\ast$$ as a matrix, we need to know the image of each element of $$\mathcal{C}^\ast$$. For any $$\upsilon^k\in\mathcal{C}^\ast$$, we have $$L^\ast(\upsilon^k)=\upsilon^k\circ L$$, and as an element of $$V^\ast$$ this function is expressed as a linear combination of elements of $$\mathcal{B}^\ast$$:

$$\begin{aligned}L^\ast(\upsilon^1)&=\beta_{11}\xi^1+\beta_{21}\xi^2+\cdots+\beta_{n1}\xi^n\\L^\ast(\upsilon^2)&=\beta_{12}\xi^1+\beta_{22}\xi^2+\cdots+\beta_{n2}\xi^n\\&\phantom{a}\vdots\\L^\ast(\upsilon^m)&=\beta_{1m}\xi^1+\beta_{2m}\xi^2+\cdots+\beta_{nm}\xi^n\end{aligned}$$

To find the coefficients $$\beta_{lk}$$, substitute $$x_l$$ into both sides of

$$L^\ast(\upsilon^k)=\beta_{1k}\xi^1+\cdots+\beta_{lk}\xi^l+\cdots+\beta_{nk}\xi^n$$

The right-hand side yields $$\beta_{lk}$$, while the left-hand side becomes

$$L^\ast(\upsilon^k)(x_l)=\upsilon^k(L(x_l))=\upsilon^k(\alpha_{1l}y_1+\cdots+\alpha_{ml}y_m)=\alpha_{kl}$$

Thus $$\beta_{lk}=\alpha_{kl}$$, and the matrix representation of $$L^\ast$$ is

$$[L^\ast]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}=\begin{pmatrix}\alpha_{11}&\alpha_{21}&\cdots&\alpha_{m1}\\\alpha_{12}&\alpha_{22}&\cdots&\alpha_{m2}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{1n}&\alpha_{2n}&\cdots&\alpha_{mn}\end{pmatrix}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}^t=\bigl([L]_\mathcal{C}^\mathcal{B}\bigr)^t$$

In other words, the transpose of a matrix is precisely the matrix representing the dual map.

## Orthogonal Complement

First, the following proposition holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual.

1. If $$L$$ is injective, then $$L^\ast$$ is surjective.
2. If $$L$$ is surjective, then $$L^\ast$$ is injective.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Both claims are immediate from [§Space of Linear Maps, ⁋Corollary 2](/en/math/linear_algebra/space_of_linear_maps#cor2).

1. If $$L$$ is injective, there exists $$R:W\rightarrow V$$ satisfying $$R\circ L=\id_V$$. Then for any $$f\in V^\ast$$, the composition $$f\circ R$$ is a function from $$W$$ to $$\mathbb{K}$$, i.e., an element of $$W^\ast$$, and

    $$L^\ast(f\circ R)=(f\circ R)\circ L=f\circ(R\circ L)=f\circ\id_V=f$$
    
    so $$L^\ast$$ is surjective.
2. If $$L$$ is surjective, there exists $$S:W\rightarrow V$$ satisfying $$L\circ S=\id_W$$. Thus, if some $$f\in W^\ast$$ satisfies $$L^\ast(f)=0$$,

    $$L^\ast(f)=f\circ L=0\implies 0=(f\circ L)\circ S=f\circ(L\circ S)=f\circ\id_W=f$$

    so $$L^\ast$$ is injective.

</details>

This proposition suggests a specific relationship between $$\ker L$$ and $$\im L^\ast$$, and between $$\im L$$ and $$\ker L^\ast$$. We begin with the following definition.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $$V$$ be a $$\mathbb{K}$$-vector space with canonical pairing $$(-,-)$$, and consider an arbitrary subset $$S\subseteq V$$. The collection of $$f\in V^\ast$$ satisfying $$(v,f)=0$$ for all $$v\in S$$ is called the *orthogonal complement* or *annihilator* of $$S$$, and is denoted by $$S^\perp$$.

Similarly, given an arbitrary subset $$T\subseteq V^\ast$$, the collection of $$v\in V$$ satisfying $$(v,f)=0$$ for all $$f\in T$$ is called the orthogonal complement of $$T$$ and is denoted by $$T^\perp$$.

</div>

In particular, when $$S$$ or $$T$$ is a singleton we sometimes write $$v^\perp$$ or $$f^\perp$$.

That $$v^\perp$$ is a subspace of $$V^\ast$$ for any $$v\in V$$ is obvious from the bilinearity of $$(-,-)$$. Now, from the equality

$$S^\perp=\bigcap_{v\in S}v^\perp$$

and [§Basis of a Vector Space, ⁋Lemma 3](/en/math/linear_algebra/basis#lem3), we see that $$S^\perp$$ is a subspace of $$V^\ast$$. Similarly, for any $$T\subseteq V^\ast$$, the set $$T^\perp$$ is a subspace of $$V$$.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. For any subspace $$U\subseteq V$$ and its orthogonal complement $$U^\perp$$,

$$L(U)^\perp=(L^\ast)^{-1}(U^\perp)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Using equation (1), which defines the dual map $$L^\ast$$ via the canonical pairing, for any $$\upsilon\in W^\ast$$ we have

$$\upsilon\in L(U)^\perp\iff (L(u),\upsilon)=0\text{ for all $u\in U$}\iff (u, L^\ast(\upsilon))=0\text{ for all $u\in U$}\iff L^\ast(\upsilon)\in U^\perp$$

as desired.

</details>

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. Then $$(\im L)^\perp=\ker(L^\ast)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to take $$U=V$$ in [Proposition 8](#prop8). From the non-degeneracy of the canonical pairing $$(-,-)$$, we have $$U^\perp=\{0\}$$, yielding the desired result.

</details>

In [Proposition 8](#prop8), we could instead start with $$U\subseteq W^\ast$$ rather than $$U\subseteq V$$. In that case we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. For any subspace $$U\subseteq W^\ast$$ and its orthogonal complement $$U^\perp$$,

$$\bigl(L^\ast(U)\bigr)^\perp=L^{-1}(U^\perp)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This too follows from equation (1): for any $$x\in V$$,

$$x\in \bigl(L^\ast(U)\bigr)^\perp\iff (x, L^\ast(\upsilon))=0\text{ for all $\upsilon\in U$}\iff (L(x),\upsilon)=0\text{ for all $\upsilon\in U$}\iff L(x)\in U^\perp$$

which gives the claim.

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. Then $$\bigl(\im L^\ast\bigr)^\perp=\ker L$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to take $$U=W^\ast$$ in [Proposition 10](#prop10).

</details>

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Bou]** Bourbaki, N. *Algebra I*, Elements of Mathematics. Springer-Verlag Berlin, 1998.  

---
