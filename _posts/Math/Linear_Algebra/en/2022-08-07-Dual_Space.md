---
title: "Dual Space"
excerpt: "Dual spaces, dual maps, and orthogonal complements"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/dual_space
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Dual_Space.png
    overlay_filter: 0.5

date: 2022-08-05
last_modified_at: 2022-08-05

weight: 115
translated_at: 2026-05-23T07:30:01+00:00
translation_source: kimi-cli
---
## Dual Basis

Let $$V$$ be a finite-dimensional $$\mathbb{K}$$-vector space. From [§Spaces of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5), taking $$W=\mathbb{K}$$, we know that $$V^\ast=\Hom(V,\mathbb{K})$$ has the same dimension as $$V$$. In particular, if $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ is a basis of $$V$$, then the collection of linear maps $$\xi^i$$ that send only $$x_i$$ to 1 and the remaining $$x_j$$ to 0

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\}$$

forms a basis of $$V^\ast$$. We call this the *dual basis* of $$\mathcal{B}$$.

Even if $$V$$ is infinite-dimensional, for a basis $$\mathcal{B}$$, the linear independence of the set $$\mathcal{B}^\ast$$ defined as above can be shown using exactly the same proof as in [§Spaces of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5), without any modification. Thus $$\dim V\leq\dim V^\ast$$ always holds, and in fact, if $$V$$ is infinite-dimensional then $$\dim V<\dim V^\ast$$ necessarily holds. To see this, it suffices to check that the function obtained by extending the map sending every element of an arbitrary $$\mathcal{B}$$ to $$1$$ cannot be expressed as a linear combination of elements of $$\mathcal{B}^\ast$$.

## Double Dual Space

When $$V$$ is finite-dimensional, $$V$$ and $$V^\ast$$ have the same dimension, and therefore the dual space $$V^{\ast\ast}$$ of $$V^\ast$$ is also a $$\mathbb{K}$$-vector space with the same dimension as $$V^\ast$$. We call this the *double dual* of $$V$$.

To show that $$V$$ and $$V^\ast$$ are isomorphic, we had to choose a specific basis. On the other hand, we can construct an injective linear map from $$V$$ to $$V^{\ast\ast}$$ that is *independent of the choice of basis*. Since $$V$$ and $$V^{\ast\ast}$$ have the same dimension, this injective linear map must be an isomorphism.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Given three $$\mathbb{K}$$-vector spaces $$U,V,W$$, a function $$f:U\times V\rightarrow W$$ is called *bilinear* if for any $$u,u_1,u_2\in U$$, $$v,v_1,v_2\in V$$, and scalar $$\alpha$$,

$$f(u_1+u_2,v)=f(u_1,v)+f(u_2,v),\qquad f(u,v_1+v_2)=f(u,v_1)+f(u,v_2),\qquad f(\alpha u,v)=\alpha f(u,v)=f(u,\alpha v)$$

hold.

</div>

In other words, this means that for any $$u\in U$$, the function $$f(u,-):V\rightarrow W$$ is linear, and for any $$v\in V$$, the function $$f(-,v):U\rightarrow W$$ is also linear.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Given two $$\mathbb{K}$$-vector spaces $$V,W$$, a *pairing* of $$V$$ and $$W$$ is a bilinear map $$(-,-):V\times W\rightarrow \mathbb{K}$$. If for every nonzero $$v\in V$$, the linear map

$$(v,-): W\rightarrow \mathbb{K}$$

is never the zero function, then this pairing is called *non-degenerate on the left*, and similarly, if for every nonzero $$w\in W$$,

$$(-,w):U\rightarrow \mathbb{K}$$

is never the zero function, then this pairing is called *non-degenerate on the right*. A pairing that is non-degenerate on both the left and the right is simply called a *non-degenerate pairing*.

</div>

The notation $$(-,-)$$ is the same as the notation for ordered pairs, so there may be some confusion, but it is not difficult to distinguish the two from context, and it is convenient, so we use this notation.

For example, the dot product of vectors $$(-,-):\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}$$ defined on $$V=W=\mathbb{R}^n$$ is a non-degenerate pairing. First,

$$(v,w_1+w_2)=(v,w_1)+(v,w_2),\qquad (v_1+v_2,w)=(v_1,w)+(v_2,w),\qquad (\alpha v,w)=\alpha(v,w)=(v,\alpha w)$$

hold trivially. Thus the dot product is a pairing. Moreover, for any nonzero vector $$v$$, we have $$(v,v)=\lVert v\rVert^2\neq 0$$, so the non-degenerate condition is also satisfied.

When $$V=W$$ as above, a pairing is sometimes called a *bilinear form*. The example we will use in this post is the following.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> For any $$\mathbb{K}$$-vector space $$V$$ and its dual space $$V^\ast$$, define $$(-,-):V\times V^\ast\rightarrow \mathbb{K}$$ by the formula

$$(v,f)=f(v)$$

Then $$(-,-)$$ is a non-degenerate pairing. First, for fixed $$v\in V$$ and arbitrary $$f,g\in V^\ast$$,

$$(v,f+g)=(f+g)(v)=f(v)+g(v)=(v,f)+(v,g)$$

and for fixed $$f\in V^\ast$$ and arbitrary $$v_1,v_2\in V$$,

$$(v_1+v_2,f)=f(v_1+v_2)=f(v_1)+f(v_2)=(v_1,f)+(v_2,f)$$

hold. Similarly, for any scalar $$\alpha$$,

$$(\alpha v,f)=f(\alpha v)=\alpha f(v)=(\alpha f)(v)=(v,\alpha f)$$

holds, so $$(-,-)$$ is a pairing. Moreover, $$(-,-)$$ is non-degenerate. First, if any $$f\in V^\ast$$ is nonzero, then there exists $$v$$ such that $$f(v)\neq 0$$, so it is obvious that $$(-,-)$$ is non-degenerate on the right. Also, for any nonzero vector $$v$$, find a basis $$\mathcal{B}$$ containing $$v$$, and then construct the dual basis as above; for the element $$\xi$$ of the dual basis corresponding to $$v$$, we have $$(v,\xi)=1$$, so $$(-,-)$$ is also non-degenerate on the left.

From this we see that $$(-,-)$$ is a non-degenerate pairing. We call this the *canonical pairing*.

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

That these functions are linear maps is obvious since $$(-,-)$$ is linear in each component. That these functions are injective is exactly the statement that $$(-,-)$$ is non-degenerate on the left and on the right.

</details>

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Two *finite-dimensional* $$\mathbb{K}$$-vector spaces $$V,W$$ with a non-degenerate pairing $$(-,-):V\times W\rightarrow \mathbb{K}$$ are isomorphic.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The two inequalities

$$\dim V\leq\dim W^\ast=\dim W,\qquad \dim W\leq\dim V^\ast=\dim V$$

make this obvious.

</details>

In this sense, a non-degenerate pairing between two finite-dimensional vector spaces is sometimes called a *perfect pairing*. Applying this corollary to the canonical pairing of [Example 3](#ex3) with $$W=V^\ast$$, we obtain an isomorphism from $$V$$ to $$V^{\ast\ast}$$. Explicitly, this function is, for any $$f\in V^\ast$$,

$$\ev_v:f\mapsto f(v)$$

the *evaluation map*. The above discussion shows that the map $$V\rightarrow V^{\ast\ast}$$ defined by $$v\mapsto \ev_v$$ is an isomorphism.

## Dual Map

Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces and let $$L:V\rightarrow W$$ be a linear map. Then we can define a function $$L^\ast:W^\ast\rightarrow V^\ast$$ by the formula

$$L^\ast(f)=f\circ L$$

In terms of a diagram, this is as follows.

![dual_map](/assets/images/Math/Linear_Algebra/Dual_Space-1.png){:style="width:6em" class="invert" .align-center}

Or, according to the canonical pairing defined above, $$L^\ast$$ can be said to be defined by the formula

$$(Lv, f)=(v,L^\ast f)\qquad\text{for all $v\in V$ and $f\in W^\ast$}\tag{1}$$

Of course, the $$(-,-)$$ on the left-hand side is the canonical pairing of $$W$$, and the $$(-,-)$$ on the right-hand side is the canonical pairing of $$V$$.

In particular, suppose $$V,W$$ are both finite-dimensional $$\mathbb{K}$$-vector spaces. Let the basis of $$V$$ be $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ and the basis of $$W$$ be $$\mathcal{C}=\{y_1,\ldots, y_m\}$$, and let their dual bases be

$$\mathcal{B}^\ast=\{\xi^1,\ldots,\xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

respectively. By [§The Fundamental Theorem of Linear Algebra](/en/math/linear_algebra/ftla), every linear map can be represented as a matrix once a choice of basis is given, so we can represent $$L^\ast$$ as a matrix with respect to the two bases $$\mathcal{C}^\ast$$ and $$\mathcal{B}^\ast$$.

First, suppose $$L$$ is represented by the following matrix with respect to the bases $$\mathcal{B},\mathcal{C}$$:

$$[L]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}$$

That is,

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

holds. To represent $$L^\ast$$ as a matrix, we need to know where each element of $$\mathcal{C}^\ast$$ is mapped. For any $$\upsilon^k\in\mathcal{C}^\ast$$, we have $$L^\ast(\upsilon^k)=\upsilon^k\circ L$$, and as an element of $$V^\ast$$, this function is expressed as a linear combination of elements of $$\mathcal{B}^\ast$$.

$$\begin{aligned}L^\ast(\upsilon^1)&=\beta_{11}\xi^1+\beta_{21}\xi^2+\cdots+\beta_{n1}\xi^n\\L^\ast(\upsilon^2)&=\beta_{12}\xi^1+\beta_{22}\xi^2+\cdots+\beta_{n2}\xi^n\\&\phantom{a}\vdots\\L^\ast(\upsilon^m)&=\beta_{1m}\xi^1+\beta_{2m}\xi^2+\cdots+\beta_{nm}\xi^n\end{aligned}$$

Suppose so. To find the coefficients $$\beta_{lk}$$, we substitute $$x_l$$ into both sides of the equation

$$L^\ast(\upsilon^k)=\beta_{1k}\xi^1+\cdots+\beta_{lk}\xi^l+\cdots+\beta_{nk}\xi^n$$

Doing so, the right-hand side yields $$\beta_{lk}$$, and the left-hand side becomes

$$L^\ast(\upsilon^k)(x_l)=\upsilon^k(L(x_l))=\upsilon^k(\alpha_{1l}y_1+\cdots+\alpha_{ml}y_m)=\alpha_{kl}$$

Thus $$\beta_{lk}=\alpha_{kl}$$ holds, and the matrix representation of $$L^\ast$$ is

$$[L^\ast]_{\mathcal{B}^\ast}^{\mathcal{C}^\ast}=\begin{pmatrix}\alpha_{11}&\alpha_{21}&\cdots&\alpha_{m1}\\\alpha_{12}&\alpha_{22}&\cdots&\alpha_{m2}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{1n}&\alpha_{2n}&\cdots&\alpha_{mn}\end{pmatrix}=\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}^t=\bigl([L]_\mathcal{C}^\mathcal{B}\bigr)^t$$

In other words, the transpose matrix is nothing other than the matrix corresponding to the matrix representation of the dual map.

## Orthogonal Complement

First, the following proposition holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual.

1. If $$L$$ is injective, then $$L^\ast$$ is surjective.
2. If $$L$$ is surjective, then $$L^\ast$$ is injective.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Both claims are obvious by [§Spaces of Linear Maps, ⁋Corollary 2](/en/math/linear_algebra/space_of_linear_maps#cor2).

1. If $$L$$ is injective, then there exists $$R:W\rightarrow V$$ satisfying $$R\circ L=\id_V$$. Thus for any $$f\in V^\ast$$, $$f\circ R$$ is a function from $$W$$ to $$\mathbb{K}$$, that is, an element of $$W^\ast$$, and

    $$L^\ast(f\circ R)=(f\circ R)\circ L=f\circ(R\circ L)=f\circ\id_V=f$$
    
    is satisfied, so $$L^\ast$$ is surjective.
2. If $$L$$ is surjective, then there exists $$S:W\rightarrow V$$ satisfying $$L\circ S=\id_W$$. Thus, if some $$f\in W^\ast$$ satisfies $$L^\ast(f)=0$$,

    $$L^\ast(f)=f\circ L=0\implies 0=(f\circ L)\circ S=f\circ(L\circ S)=f\circ\id_W=f$$

    so $$L^\ast$$ is injective.

</details>

This proposition suggests that there is a specific relationship between $$\ker L$$ and $$\im L^\ast$$, and between $$\im L$$ and $$\ker L^\ast$$. Let us first define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> Let $$V$$ be a $$\mathbb{K}$$-vector space with canonical pairing $$(-,-)$$, and consider an arbitrary subset $$S\subseteq V$$. The collection of $$f\in V^\ast$$ satisfying $$(v,f)=0$$ for all $$v\in S$$ is called the *orthogonal complement* or *annihilator* of $$S$$, and is denoted by $$S^\perp$$.

Similarly, let an arbitrary subset $$T\subseteq V^\ast$$ be given. Then the collection of $$v\in V$$ satisfying $$(v,f)=0$$ for all $$f\in T$$ is called the orthogonal complement of $$T$$ and is denoted by $$T^\perp$$.

</div>

In particular, when $$S$$ or $$T$$ is a singleton, we sometimes write $$v^\perp$$ or $$f^\perp$$.

That $$v^\perp$$ is a subspace of $$V^\ast$$ for any $$v\in V$$ is obvious from the fact that $$(-,-)$$ is bilinear. Now, from the equality

$$S^\perp=\bigcap_{v\in S}v^\perp$$

and [§Bases of Vector Spaces, ⁋Lemma 3](/en/math/linear_algebra/basis#lem3), we see that $$S^\perp$$ is a subspace of $$V^\ast$$. Similarly, for any $$T\subseteq V^\ast$$, $$T^\perp$$ is a subspace of $$V$$.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. For any subspace $$U\subseteq V$$ and its orthogonal complement $$U^\perp$$,

$$L(U)^\perp=(L^\ast)^{-1}(U^\perp)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Using equation (1), which defines the dual map $$L^\ast$$ via the canonical pairing, for any $$\upsilon\in W^\ast$$,

$$\upsilon\in L(U)^\perp\iff (L(u),\upsilon)=0\text{ for all $u\in U$}\iff (u, L^\ast(\upsilon))\text{ for all $u\in U$}\iff L^\ast(\upsilon)\in U^\perp$$

holds.

</details>

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. Then $$(\im L)^\perp=\ker(L^\ast)$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to take $$U=V$$ in [Proposition 8](#prop8). From the non-degenerate condition of the canonical pairing $$(-,-)$$, we get $$U^\perp=\{0\}$$, yielding the desired result.

</details>

In [Proposition 8](#prop8), we could have started with $$U\subseteq W^\ast$$ instead of $$U\subseteq V$$. In this case we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. For any subspace $$U\subseteq W^\ast$$ and its orthogonal complement $$U^\perp$$,

$$\bigl(L^\ast(U)\bigr)^\perp=L^{-1}(U^\perp)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This too follows from equation (1): for any $$x\in V$$,

$$x\in \bigl(L^\ast(U)\bigr)^\perp\iff (x, L^\ast(\upsilon))=0\text{ for all $\upsilon\in U$}\iff (L(x),\upsilon)=0\text{ for all $\upsilon\in U$}\iff L(x)\in U^\perp$$

so it is obvious.

</details>

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces, and let $$L:V\rightarrow W$$ be a linear map and $$L^\ast:W^\ast\rightarrow V^\ast$$ its dual. Then $$\bigl(\im L^\ast\bigr)^\perp=\ker L$$ holds.

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
