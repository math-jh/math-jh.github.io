---
title: "Bilinear Forms"
excerpt: "Bilinear forms and dual spaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/bilinear_form
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Bilinear_Form.png
    overlay_filter: 0.5

date: 2022-09-28
last_modified_at: 2022-09-28

weight: 116
translated_at: 2026-05-21T11:30:02+00:00
translation_source: kimi-cli
---
In the previous post, we defined the dual space $$V^\ast$$ of a vector space $$V$$, and saw that if $$V$$ is finite-dimensional, then $$V$$ is isomorphic to $$V^{\ast\ast}$$, the double dual of $$V^\ast$$. The key fact used in this process was that a non-degenerate pairing $$\langle -,-\rangle:V\times W \rightarrow \mathbb{K}$$ defines injective linear maps from $$V$$ to $$W^\ast$$ and from $$W$$ to $$V^\ast$$. We applied this fact to the canonical pairing

$$\langle -,-\rangle:V\times V^\ast\rightarrow \mathbb{K};\quad (v,f)\mapsto f(v)$$

and, considering dimensions, saw that $$V$$ and $$V^{\ast\ast}$$ are isomorphic. To describe this induced map $$V\rightarrow V^{\ast\ast}$$, we did not need to choose a basis of $$V$$.

Meanwhile, we mentioned at the beginning of the previous post that $$V$$ and $$V^\ast$$ also have the same dimension, but unlike the natural isomorphism $$V\rightarrow V^{\ast\ast}$$ above, this requires choosing a specific basis $$\{x_1,\ldots, x_n\}$$ of $$V$$, then taking its dual basis $$\{\xi^1,\ldots, \xi^n\}$$, and defining the map via $$x_i\mapsto \xi^i$$.

## Bilinear Forms

Now we focus on the case $$V=W$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For any pairing $$\langle -,-\rangle:V\times W\rightarrow \mathbb{K}$$, if $$W=V$$, we call this pairing a *bilinear form* defined on $$V$$. We say that $$\langle -,-\rangle$$ is a *non-degenerate bilinear form* if it is non-degenerate as a pairing.

</div>

Suppose a bilinear form on $$V$$ is given. Then by the same argument as above, we obtain linear maps from $$V$$ to $$V^\ast$$

$$v\mapsto \langle v,-\rangle,\qquad v\mapsto \langle -,v\rangle$$

In general these two need not be equal, but we can make the following definition.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For any bilinear form $$\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$$, if the identity

$$\langle v,w\rangle=\langle w,v\rangle$$

holds for all $$v,w\in V$$, we say that this form is *symmetric*. If the identity

$$\langle v,w\rangle=-\langle w,v\rangle$$

holds for all $$v,w\in V$$, we say that this form is *alternating*.

</div>

## Non-Degenerate Bilinear Forms

Let a finite-dimensional $$\mathbb{K}$$-vector space $$V$$ be given, and consider the canonical pairing $$\langle-,-\rangle:V\times V^\ast\rightarrow \mathbb{K}$$ mentioned above. If a non-degenerate pairing $$\langle -,-\rangle:V\times V\rightarrow \mathbb{K}$$ is given on $$V$$, then from [§Dual Spaces, ⁋Corollary 5](/en/math/linear_algebra/dual_space#cor5) we know that $$\langle -,-\rangle$$ defines an isomorphism

$$V\rightarrow V^\ast;\qquad v\mapsto \langle -,v\rangle\tag{1}$$

For convenience, we henceforth assume that $$\langle -,-\rangle$$ is a symmetric non-degenerate bilinear form from the outset. Then $$\langle -,-\rangle$$ has the isomorphism defined by equation (1), which can be written as follows.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Consider a finite-dimensional $$\mathbb{K}$$-vector space $$V$$ equipped with a symmetric non-degenerate bilinear form $$\langle -,-\rangle$$. For any given $$f\in V^\ast$$, there exists a unique $$w\in V$$ such that

$$f(v)=\langle v,w\rangle\qquad\text{for all $v\in V$}$$

holds.

</div>

Then in particular we can bring the notion of orthogonal complement defined in the previous post into $$V$$. That is, we define as follows.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Consider a finite-dimensional $$\mathbb{K}$$-vector space $$V$$ equipped with a symmetric non-degenerate bilinear form $$\langle -,-\rangle$$. For any $$v\in V$$, the set of all $$w\in V$$ satisfying $$\langle w,v\rangle=0$$ is called the *orthogonal complement* of $$v$$, denoted $$v^\perp$$. More generally, for any set $$S$$, we define the set

$$S^\perp=\bigcap_{v\in S}v^\perp$$

as the orthogonal complement of $$S$$.

</div>

Of course, even if $$\langle -,-\rangle$$ were not symmetric, we could make the same definition, and in fact, once we choose whether to send $$v$$ to $$\langle -,v\rangle$$ or to $$\langle v,-\rangle$$ and stick to this choice consistently, we obtain the same result. In any case, to avoid possible confusion we maintain the condition that $$\langle -,-\rangle$$ is symmetric.

The vector $$w\in V$$ uniquely determines $$f\in V^\ast$$ by [Corollary 3](#cor3), and the above definition means that if $$f$$ obtained in this way is the orthogonal complement of $$v$$ in the sense of [§Dual Spaces, ⁋Definition 7](/en/math/linear_algebra/dual_space#def7), then we think of $$w$$ as being orthogonal to $$v$$, and regard the collection of such $$w$$ as the orthogonal complement. Through this process, we can bring all the results of [§Dual Spaces](/en/math/linear_algebra/dual_space) into $$V$$. In the remainder of this post, we examine this process in detail.

First, suppose symmetric non-degenerate bilinear forms $$\langle -,-\rangle_V$$ and $$\langle -,-\rangle_W$$ are given on two finite-dimensional $$\mathbb{K}$$-vector spaces $$V$$ and $$W$$. Also, for convenience of discussion, let us denote the isomorphisms determined by these bilinear forms as

$$\varphi_V:V^\ast\rightarrow V,\qquad \varphi_W:W^\ast\rightarrow W$$

respectively.

If two bases $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ and $$\mathcal{C}=\{y_1,\ldots, y_m\}$$ are given on $$V$$ and $$W$$ respectively, then the dual bases

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

are well-defined. Now consider the bases

$$\mathcal{B}'=\{\varphi_V(\xi^1),\ldots,\varphi_V(\xi^n)\},\qquad\mathcal{C}'=\{\varphi_W(\upsilon^1),\ldots,\varphi_W(\upsilon^m)\}$$

obtained by transferring these along $$\varphi_V$$ and $$\varphi_W$$. In other words, these are elements of $$V$$ and $$W$$ defined by the formulas

$$\langle x_i,\varphi_V(\xi^j)\rangle=\delta_{ij},\qquad\langle y_i,\varphi_W(\upsilon^j)\rangle=\delta_{ij}$$

Now for any $$L:V\rightarrow W$$, suppose

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

If we think of the dual map $$L^\ast:W^\ast\rightarrow V^\ast$$ as a map from $$W$$ to $$V$$ via the above identifications $$\varphi$$, that is, if we consider $$L':W\rightarrow V$$ defined by the following diagram

![identification](/assets/images/Math/Linear_Algebra/Bilinear_Form-1.png){:style="width:7em" class="invert" .align-center}

then we can verify that the matrix representation of this linear map with respect to the two bases $$\mathcal{C}'$$ and $$\mathcal{B}'$$ is $$[L']_{\mathcal{B}'}^{\mathcal{C}'}$$.

Meanwhile, we can see that $$L':W\rightarrow V$$ defined in this way satisfies the equation

$$\langle Lv, w\rangle_W=\langle v,L'w\rangle_V\qquad\text{for all $v\in V$ and $w\in W$}\tag{1}$$

This can be checked from

$$\langle Lv,w\rangle=(\varphi^{-1}(w))(Lv)=(\varphi^{-1}_W(w)\circ L)(v)=(L^\ast(\varphi^{-1}_W(w))(v)=(\varphi^{-1}_V(v)\circ L')(w)=(\varphi^{-1}_V(v))(L'w)=\langle v,L'w\rangle$$

We call such an $$L'$$ satisfying this equation the *adjoint* of the linear map $$L$$, and with a slight abuse of notation, also write it as $$L^\ast$$.

The results of [§Dual Spaces, §§Orthogonal Complements](/en/math/linear_algebra/dual_space#직교여공간) were all obtained from the equation $$(Lv,f)=(v,L^\ast f)$$ for the canonical pairing. Therefore, replacing this with equation (1) for the non-degenerate bilinear forms $$\langle -,-\rangle$$ obtained above, we get the following results.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Suppose two $$\mathbb{K}$$-vector spaces $$V$$ and $$W$$ equipped with symmetric non-degenerate bilinear forms, a linear map $$L:V\rightarrow W$$, and its adjoint $$L^\ast:W\rightarrow V$$ are given. Then

1. For any subspace $$U\subseteq V$$, we have $$L(U)^\perp=(L^\ast)^{-1}(U^\perp)$$.
2. For any subspace $$U\subseteq W$$, we have $$L^\ast(U)^\perp=L^{-1}(U^\perp)$$.
3. We have $$(\im L)^\perp=\ker(L^\ast)$$.
4. We have $$(\im L^\ast)^\perp=\ker L$$.

</div>

In particular, the subspaces

$$\ker L, \quad(\ker L)^\perp, \quad\im L,\quad(\im L)^\perp$$

of $$V$$ and $$W$$ obtained from 3 and 4 are sometimes called the *four fundamental subspaces* determined by $$L$$. In particular, they satisfy

$$V=\ker L\oplus(\ker L)^\perp,\qquad W=\im L\oplus(\im L)^\perp$$

## Orthogonal Bases

Now consider a $$\mathbb{K}$$-vector space $$V$$ equipped with a symmetric non-degenerate bilinear form. Then a subset $$\{v_1,\ldots, v_n\}$$ of $$V$$ is called an *orthogonal set* if $$\langle v_i,v_j\rangle=0$$ whenever $$i\neq j$$. If a basis $$\mathcal{B}$$ of $$V$$ is also an orthogonal set, we call it an *orthogonal basis*.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> If a field $$\mathbb{K}$$ satisfies the condition

$$\underbrace{1+1+\cdots+1}_\text{$p$ times}=0$$

then we say that the *characteristic* of $$\mathbb{K}$$ is $$p$$, and write $$\ch \mathbb{K}=p$$. If there is no natural number $$p$$ satisfying the above formula, we consider $$\mathbb{K}$$ to have characteristic 0.

</div>

For example, $$\mathbb{R}$$ has characteristic 0. If we define addition and multiplication on $$\mathbb{F}_2=\{0,1\}$$ by the formulas

$$0+0=0,\quad 0+1=1,\quad 1+0=1,\quad 1+1=2$$

and

$$0\cdot 0=0,\quad 0\cdot 1=0,\quad 1\cdot 0=0,\quad 1\cdot 1=1$$

respectively, then we can verify that $$\mathbb{F}_2$$ satisfies the field axioms, and in this case $$\ch\mathbb{F}_2=2$$.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For a field $$\mathbb{K}$$ with $$\ch \mathbb{K}\neq 2$$, a $$\mathbb{K}$$-vector space $$V$$ equipped with a symmetric non-degenerate bilinear form always has an orthogonal basis.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we prove a simple lemma. For an arbitrarily fixed $$v\in V$$, there exists $$u\in V$$ such that $$\langle u,v\rangle\neq 0$$. Then

$$2\langle u,v\rangle=\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle$$

and by the two conditions $$\langle u,v\rangle\neq 0$$ and $$\ch \mathbb{K}\neq 2$$, the left-hand side is nonzero. Therefore, at least one of the three terms $$\langle u+v,u+v\rangle$$, $$\langle u,u\rangle$$, $$\langle v,v\rangle$$ on the right-hand side is nonzero. Thus,

> In any $$\mathbb{K}$$-vector space equipped with a non-degenerate symmetric bilinear form, there necessarily exists a vector $$w$$ satisfying $$\langle w,w\rangle\neq 0$$.

We prove the original proposition by induction on the dimension of $$V$$. There is nothing to prove when $$\dim V=0$$. Now assume the proof is complete for the case $$\dim V=k$$. Then for any vector space $$V$$ with $$\dim V=k+1$$, there exists a vector $$w$$ satisfying $$\langle w,w\rangle\neq 0$$.

Now let $$W=\span w$$ and consider $$W^\perp$$. Then for any $$v\in V$$, from the formula

$$v=\frac{\langle v,w\rangle}{\langle w,w\rangle}w+\left(v-\frac{\langle v,w\rangle}{\langle w,w\rangle}w\right)$$

we know that any element of $$V$$ can be expressed as a sum of elements from $$W$$ and $$W^\perp$$. Also, since $$\langle w,w\rangle\neq 0$$ by assumption, we have $$W\cap W^\perp=\{0\}$$. Therefore, by [§Dimension of Vector Spaces, ⁋Example 8](/en/math/linear_algebra/dimension#ex8),

$$k+1=\dim V=\dim(W+W^\perp)=\dim W+\dim W^\perp-\dim(W\cap W^\perp)$$

from which we know that $$\dim W^\perp=k$$. Moreover, for any $$v\in W^\perp$$, for $$u$$ satisfying $$\langle u,v\rangle\neq 0$$,

$$u'=u-\frac{\langle u,w\rangle}{\langle w,w\rangle}w\in W^\perp$$

is an element of $$W^\perp$$ and satisfies

$$\langle u',v\rangle=\langle u,v\rangle\neq 0$$

That is, $$W^\perp$$ is also non-degenerate with respect to $$\langle-,-\rangle$$, and so by the inductive hypothesis, there exists an orthogonal basis $$\mathcal{B}$$ of $$W^\perp$$. Now $$\mathcal{B}\cup\{v\}$$ is an orthogonal basis of $$V$$, so we obtain the desired result.

</details>

## Gram Matrix

Let an arbitrary bilinear form $$\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$$ be given. If a basis $$\{x_1,\ldots, x_n\}$$ of $$V$$ is fixed, then for any $$v=\sum v_ix_i$$ and $$w=\sum w_jx_j$$ the formula

$$\langle v,w\rangle=\left\langle\sum_{i=1}^nv_ix_i,\sum_{j=1}^n w_jx_j\right\rangle=\sum_{i,j=1}^n v_iw_j\langle x_i,x_j\rangle$$

holds. For a moment, let $$G$$ denote the $$n\times n$$ matrix whose $$(i,j)$$-entry is $$\langle x_i,x_j\rangle$$; then the above formula can be written simply as

$$\langle v,w\rangle=v^t Gw$$

In this case, we call $$G$$ the *Gram matrix* with respect to the basis $$\mathcal{B}$$.

Consider two bases $$\mathcal{B}$$ and $$\mathcal{C}$$ given on $$V$$. Let us denote their Gram matrices by $$G_\mathcal{B}$$ and $$G_\mathcal{C}$$ respectively, and write the above formula precisely; then we can say

$$\langle v,w\rangle=[v]^t_\mathcal{B}G_\mathcal{B}[w]_\mathcal{B}=[v]^t_\mathcal{C}G_\mathcal{C}[w]_\mathcal{C}$$

Now since $$[v]_\mathcal{C}=[\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}$$, the rightmost side of the above formula becomes

$$[v]_\mathcal{C}^tG_\mathcal{C}[w]_\mathcal{C}=\left([\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}\right)^tG_\mathcal{B}\left([\id]_\mathcal{C}^\mathcal{B}[w]_\mathcal{B}\right)=[v]_\mathcal{B}^t\left(([\id]_\mathcal{C}^\mathcal{B})^t G_\mathcal{B}[\id]_\mathcal{C}^\mathcal{B}\right)[w]_\mathcal{B}$$

---

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
