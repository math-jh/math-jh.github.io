---
title: "Bilinear Forms"
description: "This post reviews the dual spaces and canonical isomorphisms of finite-dimensional vector spaces, and outlines the definition, symmetry, alternating properties, and nondegeneracy conditions of bilinear forms."
excerpt: "Bilinear forms and dual spaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/bilinear_form
sidebar: 
    nav: "linear_algebra-en"


date: 2022-09-28

weight: 20
translated_at: 2026-09-25T07:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we defined for a vector space $V$ its dual space $V^\ast$, and saw that if $V$ is finite-dimensional, the dual space of $V^\ast$, namely $V^{\ast\ast}$, is isomorphic to $V$. The key fact used in this process was that a non-degenerate pairing $\langle -,-\rangle:V\times W \rightarrow \mathbb{K}$ defines injective linear maps from $V$ to $W^\ast$, and from $W$ to $V^\ast$. We applied this fact to the canonical pairing

$$\langle -,-\rangle:V\times V^\ast\rightarrow \mathbb{K};\quad (v,f)\mapsto f(v)$$

and, considering dimensions, saw that $V$ and $V^{\ast\ast}$ are isomorphic. To describe the map $V\rightarrow V^{\ast\ast}$ induced in this way, there was no need to choose a basis for $V$.

Meanwhile, at the beginning of the previous post, we mentioned that $V$ and $V^\ast$ also have the same dimension; however, unlike the natural isomorphism $V\rightarrow V^{\ast\ast}$ above, there was the difference that it had to be defined by choosing a specific basis $\{x_1,\ldots, x_n\}$, choosing their dual basis $\{\xi^1,\ldots, \xi^n\}$, and setting $x_i\mapsto \xi^i$.

## Bilinear Forms

Now we focus on the case where $V=W$.

::: Definition 1
For any pairing $\langle -,-\rangle:V\times W\rightarrow \mathbb{K}$, if $W=V$, then this pairing is called a *bilinear form* defined on $V$. That $\langle -,-\rangle$ is a *non-degenerate bilinear form* means that $\langle-,-\rangle$ is non-degenerate as a pairing.
:::

Suppose a bilinear form is given on $V$. Then through the same argument as above, we obtain linear maps from $V$ to $V^\ast$:

$$v\mapsto \langle v,-\rangle,\qquad v\mapsto \langle -,v\rangle$$

In general, these two need not be the same, but we can define the following.

::: Definition 2
For any bilinear form $\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$, if the equation

$$\langle v,w\rangle=\langle w,v\rangle$$

holds for all $v,w\in V$, the form is said to be *symmetric*. If for all $v,w\in V$ the equation

$$\langle v,w\rangle=-\langle w,v\rangle$$

holds, the form is said to be *alternating*.
:::

## Non-degenerate Bilinear Forms

Suppose we are given a finite-dimensional $\mathbb{K}$-vector space $V$, and consider the canonical pairing $\langle-,-\rangle:V\times V^\ast\rightarrow \mathbb{K}$ mentioned earlier. If $V$ is equipped with a non-degenerate pairing $\langle -,-\rangle:V\times V\rightarrow \mathbb{K}$, we know from [§Dual Space, ⁋Proposition 4](/en/math/linear_algebra/dual_space#prop4){: data-lid="73s9i" } and $\dim V=\dim V^\ast$ that $\langle -,-\rangle$ defines an isomorphism

$$V\rightarrow V^\ast;\qquad v\mapsto \langle -,v\rangle\tag{1}$$

The isomorphism in (1) can be rewritten as follows.

::: Corollary 3
Given a non-degenerate bilinear form $\langle -,-\rangle$ on a finite-dimensional $\mathbb{K}$-vector space $V$, for every $f\in V^\ast$, there exists a unique $w\in V$ such that

$$f(v)=\langle v,w\rangle\qquad\text{for all $v\in V$}$$

holds.
:::

Then, in particular, we can bring the notion of orthogonal complement defined in the previous post to $V$. That is, we define as follows.

::: Definition 4
Given a non-degenerate bilinear form $\langle -,-\rangle$ on a finite-dimensional $\mathbb{K}$-vector space $V$, for any $v\in V$, the collection of elements satisfying the equation $\langle w,v\rangle=0$ among all $w\in V$ is called the *orthogonal complement* of $v$, and is denoted by $v^\perp$. More generally, for any subset $S\subseteq V$, we define the set

$$S^\perp=\bigcap_{v\in S}v^\perp$$

to be the orthogonal complement of $S$.
:::

The vector $w\in V$ uniquely determines, by [Corollary 3](#cor3){: data-lid="xwfq2" }, an element $f\in V^\ast$; the definition above means that if the $f$ thus obtained belongs, in the sense of [§Dual Space, ⁋Definition 7](/en/math/linear_algebra/dual_space#def7){: data-lid="hvju7" }, to the orthogonal complement of $v$, we regard $w$ as orthogonal to $v$, and take the collection of such $w$ to be the orthogonal complement. Through this process, all results of [§Dual Space](/en/math/linear_algebra/dual_space){: data-lid="qrjjp" } can be transferred to $V$. In the remainder of this post, we examine this process in detail.

For a general bilinear form, using $\langle w,v\rangle=0$ to define $v^\perp$ and using $\langle v,w\rangle=0$ may give different results, so the definition of $W^\perp$ can vary depending on whether it is defined from the left or from the right. To avoid such a phenomenon, it is wise to consider the following property.

::: Definition 5
When a bilinear form $\langle-,-\rangle$ satisfies that for any $v,w\in V$, $\langle v,w\rangle=0$ and $\langle w,v\rangle=0$ are equivalent to each other, $\langle-,-\rangle$ is said to be *reflexive*.
:::

That a symmetric form is reflexive is trivial, but the converse does not hold. For instance, an alternating form also satisfies

$$\langle v,w\rangle=-\langle w,v\rangle$$

and is therefore reflexive. Remarkably, reflexive forms are precisely these two, namely forms that are either symmetric or alternating.

::: Proposition 6
On a finite-dimensional $\mathbb{K}$-vector space $V$, a bilinear form $\langle-,-\rangle$ is reflexive if and only if it is symmetric or alternating.
:::

::: Proof
Since we have already seen one direction, it suffices to assume that $\langle-,-\rangle$ is reflexive and show the converse. For any $u,v,w$, we have

$$\langle u,\langle u,w\rangle v-\langle u,v\rangle w\rangle=\langle u,w\rangle\langle u,v\rangle-\langle u,v\rangle\langle u,w\rangle=0$$

and so by reflexivity, $\langle\langle u,w\rangle v-\langle u,v\rangle w,u\rangle=0$. Expanding this in the same manner yields

$$\langle u,w\rangle\langle v,u\rangle=\langle u,v\rangle\langle w,u\rangle\tag{$\ast$}$$

for all $u,v,w$.

Now if for all $u$ we have $\langle u,u\rangle=0$, then

$$0=\langle u+v,u+v\rangle=\langle u,v\rangle+\langle v,u\rangle$$

shows that $\langle-,-\rangle$ is alternating.

Otherwise, since $\langle u_0,u_0\rangle\neq 0$ for some $u_0$, evaluating $(\ast)$ at $w=u=u_0$ gives

$$\langle u_0,u_0\rangle\bigl(\langle v,u_0\rangle-\langle u_0,v\rangle\bigr)=0$$

so we see that for all $v$, $\langle v,u_0\rangle=\langle u_0,v\rangle$ holds. Therefore, evaluating $(\ast)$ again at $v=u_0$ yields

$$\langle u,u_0\rangle\bigl(\langle u,w\rangle-\langle w,u\rangle\bigr)=0$$

Here $u,w$ can be arbitrary vectors, and two cases arise. First, if $\langle u,u_0\rangle\neq 0$, then immediately $\langle u,w\rangle=\langle w,u\rangle$. If $\langle u,u_0\rangle=0$, setting $u'=u+u_0$ gives $\langle u', u_0\rangle=\langle u_0,u_0\rangle\neq 0$, and thus for all $w$, $\langle u', w\rangle=\langle w,u'\rangle$ holds. But we have already shown above that $\langle u_0,w\rangle=\langle w,u_0\rangle$ for all vectors, from which the conclusion follows.
:::

Therefore, the forms whose orthogonal complement does not depend on left or right are precisely symmetric forms and alternating forms. In what follows, results on subspaces are developed for non-degenerate reflexive forms encompassing both cases, which in particular apply directly to non-degenerate alternating forms as well. We add a few definitions.

::: Definition 7
Given a finite-dimensional $\mathbb{K}$-vector space $V$ equipped with a non-degenerate reflexive bilinear form, for a subspace $W\leq V$, we define the following:

1. The intersection $W\cap W^\perp$ is called the *radical* of $W$.
2. If the radical is $\{0\}$, $W$ is called *non-degenerate*.
3. When $W\subseteq W^\perp$, the restriction of $\langle-,-\rangle$ to $W$ is identically $0$, in which case $W$ is said to be *isotropic*.
4. When $W^\perp\subseteq W$, $W$ is said to be *coisotropic*.
5. A space with $W=W^\perp$ is called *Lagrangian*.
:::

Since the radical of $W$ is the set of vectors in $W$ orthogonal to all of $W$, $W$ being non-degenerate is precisely equivalent to the restriction of $\langle-,-\rangle$ to $W$ being non-degenerate again.

::: Proposition 8
Given a finite-dimensional $\mathbb{K}$-vector space $V$ equipped with a non-degenerate reflexive bilinear form, for any subspace $W\leq V$, the following hold:

1. $\dim W+\dim W^\perp=\dim V$.
2. $(W^\perp)^\perp=W$.
3. $W$ being non-degenerate, $W^\perp$ being non-degenerate, and $V=W\oplus W^\perp$ are equivalent.
:::
::: Proof
The dual of the inclusion map $W\hookrightarrow V$, namely the restriction $V^\ast\rightarrow W^\ast$, is surjective ([§Dual Space, ⁋Proposition 6](/en/math/linear_algebra/dual_space#prop6){: data-lid="oz8n9" }). Meanwhile, since $\langle-,-\rangle$ is non-degenerate, $v\mapsto\langle v,-\rangle$ is injective, and since dimensions are equal, it defines an isomorphism $V\rightarrow V^\ast$. Therefore, composing this with the restriction above,

$$V\rightarrow W^\ast;\qquad v\mapsto\langle v,-\rangle\vert_W$$

is also surjective, and by definition its kernel is $W^\perp$. Therefore, by [§Isomorphisms, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7){: data-lid="t06p5" }, we have $\dim W^\perp=\dim V-\dim W^\ast=\dim V-\dim W$, so the first equality holds. For the second claim, reflexivity gives $W\subseteq(W^\perp)^\perp$, and thus applying the first equality twice yields

$$\dim(W^\perp)^\perp=\dim V-\dim W^\perp=\dim W$$

so the two spaces coincide.

Finally, combining [§Dimension of Vector Spaces, ⁋Example 8](/en/math/linear_algebra/dimension#ex8){: data-lid="rv0el" } with part 1,

$$\dim(W+W^\perp)=\dim W+\dim W^\perp-\dim(W\cap W^\perp)=\dim V-\dim(W\cap W^\perp)$$

holds. Therefore, the radical of $W$, namely $W\cap W^\perp$, being $\{0\}$ is equivalent to $W+W^\perp=V$, and in this case, dimension counting implies that the sum is automatically direct, so $V=W\oplus W^\perp$. Meanwhile, by the second claim, $W\cap W^\perp=W^\perp\cap(W^\perp)^\perp$ is also the radical of $W^\perp$, so $W$ being non-degenerate is equivalent to $W^\perp$ being non-degenerate.
:::

For a non-degenerate subspace satisfying the conditions above, the orthogonal complement defined in this way is canonically isomorphic to the quotient space.

::: Proposition 9
Given a finite-dimensional $\mathbb{K}$-vector space $V$ equipped with a non-degenerate reflexive bilinear form, for any non-degenerate subspace $W\leq V$, the restriction of the natural projection $p:V\rightarrow V/W$ from [§Quotient Spaces, ⁋Definition 3](/en/math/linear_algebra/quotient_space#def3){: data-lid="azhkf" } to $W^\perp$,

$$p\vert_{W^\perp}:W^\perp\rightarrow V/W$$

is an isomorphism.
:::
::: Proof
Since $W$ is non-degenerate, $V=W\oplus W^\perp$ by [Proposition 8](#prop8){: data-lid="xualb" }. The natural projection satisfies $\ker p=W$, so the kernel of $p\vert_{W^\perp}$ is $W^\perp\cap W=\{0\}$, which means it is injective; since $V=W+W^\perp$, for any $v=w+w'$ ($w\in W$, $w'\in W^\perp$), we have $p(w')=w'+W=v+W$, so it is surjective. Therefore, $p\vert_{W^\perp}$ is an isomorphism.
:::

In other words, in the direct sum $V=W\oplus W^\perp$, collapsing $W$ allows $W^\perp$ to realize precisely the quotient $V/W$. In general, while the quotient space $V/W$ is a canonical object defined without $\langle-,-\rangle$, the object realizing it inside $V$, namely $W^\perp$, depends on the form, and such a representation is impossible without the non-degeneracy of [Proposition 8](#prop8){: data-lid="cym0t" }. For example, if $W\neq\{0\}$ is isotropic, then $W\cap W^\perp\neq\{0\}$, so $p\vert_{W^\perp}$ fails to be injective.

## Four Fundamental Subspaces

Now suppose that two finite-dimensional $\mathbb{K}$-vector spaces $V,W$ are equipped with non-degenerate bilinear forms $\langle -,-\rangle_V$ and $\langle -,-\rangle_W$. In principle, the contents of this section can be developed even if these bilinear forms are reflexive, but to express them more neatly in a form like equation (2) below, it is convenient for them to be symmetric, so we assume this. In addition, for convenience of discussion, let us denote the inverses of the isomorphisms in equation (1) defined by these bilinear forms by

$$\varphi_V:V^\ast\rightarrow V,\qquad \varphi_W:W^\ast\rightarrow W$$

respectively.

If $V,W$ are given two bases $\mathcal{B}=\{x_1,\ldots, x_n\}$ and $\mathcal{C}=\{y_1,\ldots, y_m\}$ respectively, the dual bases

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

are well-defined. Now consider the bases

$$\mathcal{B}'=\{\varphi_V(\xi^1),\ldots,\varphi_V(\xi^n)\},\qquad\mathcal{C}'=\{\varphi_W(\upsilon^1),\ldots,\varphi_W(\upsilon^m)\}$$

obtained by transferring these along $\varphi_V,\varphi_W$. That is, these are elements of $V,W$ defined by the equations

$$\langle x_i,\varphi_V(\xi^j)\rangle=\delta_{ij},\qquad\langle y_i,\varphi_W(\upsilon^j)\rangle=\delta_{ij}.$$

Now, for any $L:V\rightarrow W$, let

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m.\end{aligned}$$

If we view the dual map $L^\ast:W^\ast\rightarrow V^\ast$ via the identifications $\varphi$ above as a map from $W$ to $V$, that is, if we consider $L':W\rightarrow V$ defined by the diagram

{% diagram Math/Linear_Algebra/Bilinear_Form-1.svg width="8.27em" alt="identification" %}

then one can verify that the matrix representation of this linear map with respect to the two bases $\mathcal{C}'$ and $\mathcal{B}'$ is $[L']_{\mathcal{B}'}^{\mathcal{C}'}=\bigl([L]_\mathcal{C}^\mathcal{B}\bigr)^t$.

Meanwhile, one can see that $L':W\rightarrow V$ defined in this way satisfies the following equation:

$$\langle Lv, w\rangle_W=\langle v,L'w\rangle_V\qquad\text{for all $v\in V$ and $w\in W$}\tag{2}$$

This can be verified from

$$\langle Lv,w\rangle=(\varphi^{-1}_W(w))(Lv)=(\varphi^{-1}_W(w)\circ L)(v)=(L^\ast(\varphi^{-1}_W(w)))(v)=(\varphi^{-1}_V(v)\circ L')(w)=(\varphi^{-1}_V(v))(L'w)=\langle v,L'w\rangle.$$

We call $L'$ satisfying this equation the *adjoint* of the linear map $L$, and by a slight abuse of notation, we also write it as $L^\ast$.

The results of [§Dual Space, §§Orthogonal Complement](/en/math/linear_algebra/dual_space#orthogonal-complement){: data-lid="pbhto" } were all obtained from the relation $(Lv,f)=(v,L^\ast f)$ for the canonical pairing. Therefore, replacing this with equation (2) for the non-degenerate bilinear forms $\langle -,-\rangle$ obtained above, we obtain the following results.

::: Proposition 10
Suppose we are given two finite-dimensional $\mathbb{K}$-vector spaces $V,W$ equipped with symmetric non-degenerate bilinear forms, a linear map $L:V\rightarrow W$, and its adjoint $L^\ast:W\rightarrow V$. Then

1. For any subspace $U\subseteq V$, $L(U)^\perp=(L^\ast)^{-1}(U^\perp)$ holds.
2. For any subspace $U\subseteq W$, $L^\ast(U)^\perp=L^{-1}(U^\perp)$ holds.
3. $(\im L)^\perp=\ker(L^\ast)$ holds.
4. $(\im L^\ast)^\perp=\ker L$ holds.
:::

In particular, the subspaces of $V$ and $W$ obtained in 3 and 4,

$$\ker L, \quad(\ker L)^\perp, \quad\im L,\quad(\im L)^\perp$$

are sometimes called the *four fundamental subspaces* determined by $L$. If $\ker L$ and $\im L$ are non-degenerate in the sense of [Definition 7](#def7){: data-lid="0zj3a" }, then by [Proposition 8](#prop8){: data-lid="g0dgy" }, they are orthogonally decomposed as

$$V=\ker L\oplus(\ker L)^\perp,\qquad W=\im L\oplus(\im L)^\perp$$

and in particular, if $\langle-,-\rangle$ is positive-definite, then every subspace is non-degenerate, so this decomposition always holds.

## Orthogonal Basis

Now consider a $\mathbb{K}$-vector space $V$ equipped with a symmetric non-degenerate bilinear form. Then a subset of $V$, $\{v_1,\ldots, v_n\}$, is said to be an *orthogonal set* if whenever $i\neq j$, $\langle v_i,v_j\rangle=0$ holds. If a basis of $V$, $\mathcal{B}$, is also an orthogonal set, we call it an *orthogonal basis*.

::: Definition 11
If for a field $\mathbb{K}$, the condition

$$\underbrace{1+1+\cdots+1}_\text{$p$ times}=0$$

is satisfied by some natural number $p$, then the smallest such number is called the *characteristic* of $\mathbb{K}$ and denoted by $\ch \mathbb{K}=p$. If no natural number $p$ satisfying the above equation exists, we consider $\mathbb{K}$ to have characteristic 0.
:::

For example, $\mathbb{R}$ has characteristic 0. If on $\mathbb{F}_2=\{0,1\}$ we define addition and multiplication by

$$0+0=0,\quad 0+1=1,\quad 1+0=1,\quad 1+1=0$$

and

$$0\cdot 0=0,\quad 0\cdot 1=0,\quad 1\cdot 0=0,\quad 1\cdot 1=1$$

respectively, we can verify that $\mathbb{F}_2$ satisfies the conditions of a field, and in this case $\ch\mathbb{F}_2=2$.

::: Proposition 12
Assuming $\ch \mathbb{K}\neq 2$ for a field $\mathbb{K}$, any finite-dimensional $\mathbb{K}$-vector space $V$ equipped with a symmetric non-degenerate bilinear form always has an orthogonal basis.  
:::
::: Proof
First, we prove a simple lemma. For any fixed non-$0$ $v\in V$, we must have $\langle u,v\rangle\neq 0$ for some $u\in V$. Then

$$2\langle u,v\rangle=\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle$$

and from the two conditions $\langle u,v\rangle\neq 0$ and $\ch \mathbb{K}\neq 2$, the left-hand side is not 0. Thus, at least one of the three terms $\langle u+v,u+v\rangle, \langle u,u\rangle,\langle v,v\rangle$ on the right-hand side is not 0. Therefore,

> In any non-$\{0\}$ $\mathbb{K}$-vector space equipped with a non-degenerate symmetric bilinear form, we must have $\langle w,w\rangle\neq 0$ for some $w$.

We prove the original proposition by induction on the dimension of $V$. The case $\dim V=0$ requires no proof. Now assume that the proof is complete in the case $\dim V=k$. Then, whenever $\dim V=k+1$ for a vector space $V$, we have $\langle w,w\rangle\neq 0$ for some vector $w$. 

Now let $W=\span w$. Since $\langle w,w\rangle\neq 0$, we have $w\notin W^\perp$, and since $W$ is $1$-dimensional, $W\cap W^\perp=\{0\}$; that is, $W$ is non-degenerate in the sense of [Definition 7](#def7){: data-lid="2dxia" }. Therefore, by [Proposition 8](#prop8){: data-lid="i7zbg" }, $V=W\oplus W^\perp$, $W^\perp$ is also non-degenerate, and $\dim W^\perp=\dim V-1=k$. Applying the induction hypothesis to the $k$-dimensional space $W^\perp$ equipped with the non-degenerate form, there exists an orthogonal basis $\mathcal{B}$, and since $W=\span w$ is orthogonal to $W^\perp$, $\mathcal{B}\cup\{w\}$ is an orthogonal basis of $V$.
:::

## Gram matrix

Suppose an arbitrary bilinear form $\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$ is given. If a basis of $V$, $\mathcal{B}=\{x_1,\ldots, x_n\}$, is fixed, then for any $v=\sum v_ix_i, w=\sum w_jx_j$, the following identity holds:

$$\langle v,w\rangle=\left\langle\sum_{i=1}^nv_ix_i,\sum_{j=1}^n w_jx_j\right\rangle=\sum_{i,j=1}^n v_iw_j\langle x_i,x_j\rangle$$

If we denote the matrix whose $(i,j)$-entry is $\langle x_i,x_j\rangle$ for now as the $n\times n$ matrix $G$, the equation above can be simply written as

$$\langle v,w\rangle=v^t Gw$$

Here, $G$ is called the *Gram matrix* with respect to the basis $\mathcal{B}$.

On $V$, consider two bases $\mathcal{B},\mathcal{C}$. Denoting the Gram matrices with respect to these by $G_\mathcal{B},G_\mathcal{C}$ respectively, we may write the equation above precisely as

$$\langle v,w\rangle=[v]^t_\mathcal{B}G_\mathcal{B}[w]_\mathcal{B}=[v]^t_\mathcal{C}G_\mathcal{C}[w]_\mathcal{C}$$

Now, since $[v]_\mathcal{C}=[\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}$, the rightmost side of the above equation becomes

$$[v]_\mathcal{C}^tG_\mathcal{C}[w]_\mathcal{C}=\left([\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}\right)^tG_\mathcal{C}\left([\id]_\mathcal{C}^\mathcal{B}[w]_\mathcal{B}\right)=[v]_\mathcal{B}^t\left(([\id]_\mathcal{C}^\mathcal{B})^t G_\mathcal{C}[\id]_\mathcal{C}^\mathcal{B}\right)[w]_\mathcal{B}$$

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
