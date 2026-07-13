---
title: "Bilinear Forms"
description: "We review the dual space of a finite-dimensional vector space and the natural isomorphism, then summarize the definition, symmetry, alternativity, and nondegeneracy conditions of bilinear forms."
excerpt: "Bilinear forms and dual spaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/bilinear_form
sidebar: 
    nav: "linear_algebra-en"


date: 2022-09-28

weight: 116
translated_at: 2026-07-05T17:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-05T17:00:02+00:00
---
In the previous post, we defined the dual space $V^\ast$ of a vector space $V$, and observed that if $V$ is finite-dimensional, then $V$ is isomorphic to $V^{\ast\ast}$, the dual of $V^\ast$. The key fact used in this process was that a non-degenerate pairing $\langle -,-\rangle:V\times W \rightarrow \mathbb{K}$ defines injective linear maps from $V$ to $W^\ast$ and from $W$ to $V^\ast$. We applied this to the canonical pairing

$$\langle -,-\rangle:V\times V^\ast\rightarrow \mathbb{K};\quad (v,f)\mapsto f(v)$$

and, taking dimensions into account, observed that $V$ and $V^{\ast\ast}$ are isomorphic. To describe the induced map $V\rightarrow V^{\ast\ast}$, no choice of basis for $V$ was necessary.

On the other hand, we mentioned at the beginning of the previous post that $V$ and $V^\ast$ also have the same dimension; this differs from the natural isomorphism $V\rightarrow V^{\ast\ast}$ above in that it requires choosing a specific basis $\{x_1,\ldots, x_n\}$ and then taking its dual basis $\{\xi^1,\ldots, \xi^n\}$, defining the map via $x_i\mapsto \xi^i$.

## Bilinear Forms

Now we focus on the case $V=W$.

::: Definition 1
For any pairing $\langle -,-\rangle:V\times W\rightarrow \mathbb{K}$, if $W=V$ then this pairing is called a *bilinear form* defined on $V$. We say that $\langle -,-\rangle$ is a *non-degenerate bilinear form* if $\langle-,-\rangle$ is non-degenerate as a pairing.
:::

Suppose a bilinear form on $V$ is given. Then by the same argument as above, we obtain linear maps from $V$ to $V^\ast$

$$v\mapsto \langle v,-\rangle,\qquad v\mapsto \langle -,v\rangle$$

In general these two need not be equal, but we can make the following definition.

::: Definition 2
For any bilinear form $\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$, if the equation

$$\langle v,w\rangle=\langle w,v\rangle$$

holds for all $v,w\in V$, we say this form is *symmetric*. If the equation

$$\langle v,w\rangle=-\langle w,v\rangle$$

holds for all $v,w\in V$, we say this form is *alternating*.
:::

## Non-degenerate Bilinear Forms

Let $V$ be a finite-dimensional $\mathbb{K}$-vector space, and consider the canonical pairing $\langle-,-\rangle:V\times V^\ast\rightarrow \mathbb{K}$ mentioned above. If a non-degenerate pairing $\langle -,-\rangle:V\times V\rightarrow \mathbb{K}$ on $V$ is given, then by [§Dual Space, ⁋Corollary 5](/en/math/linear_algebra/dual_space#cor5) we know that $\langle -,-\rangle$ defines an isomorphism

$$V\rightarrow V^\ast;\qquad v\mapsto \langle -,v\rangle\tag{1}$$

The isomorphism in equation (1) can be rewritten as follows.

::: Corollary 3
Let $V$ be a finite-dimensional $\mathbb{K}$-vector space with a non-degenerate bilinear form $\langle -,-\rangle$ given. For any $f\in V^\ast$, there exists a unique $w\in V$ such that

$$f(v)=\langle v,w\rangle\qquad\text{for all $v\in V$}$$

holds.
:::

Then in particular, we can bring the notion of orthogonal complement defined in the previous post into $V$. That is, we define as follows.

::: Definition 4
Let $V$ be a finite-dimensional $\mathbb{K}$-vector space with a non-degenerate bilinear form $\langle -,-\rangle$ given. For any $v\in V$, the set of all $w\in V$ satisfying the equation $\langle w,v\rangle=0$ is called the *orthogonal complement* of $v$, and denoted by $v^\perp$. More generally, for any set $S$, we define the set

$$S^\perp=\bigcap_{v\in S}v^\perp$$

as the orthogonal complement of $S$.
:::

By [Corollary 3](#cor3), a vector $w\in V$ uniquely determines $f\in V^\ast$, and the above definition means that if the $f$ obtained in this way is the orthogonal complement of $v$ in the sense of [§Dual Space, ⁋Definition 7](/en/math/linear_algebra/dual_space#def7), then we think of $w$ as being orthogonal to $v$, and collect all such $w$ to form the orthogonal complement. Through this process, all results from [§Dual Space](/en/math/linear_algebra/dual_space) can be brought into $V$. In the remainder of this post, we examine this process in detail.

For a general bilinear form, the $v^\perp$ defined by $\langle w,v\rangle=0$ and the one defined by $\langle v,w\rangle=0$ may differ, so the definition of $W^\perp$ may vary depending on whether it is defined from the left or from the right. To avoid this phenomenon, it is wise to consider the following property.

::: Definition 5
A bilinear form $\langle-,-\rangle$ is called *reflexive* if for any $v,w\in V$, the conditions $\langle v,w\rangle=0$ and $\langle w,v\rangle=0$ are equivalent.
:::

That a symmetric form is reflexive is obvious, but the converse does not hold. For example, an alternating form is also reflexive since

$$\langle v,w\rangle=-\langle w,v\rangle$$

Surprisingly, reflexive forms are exactly these two, that is, symmetric or alternating forms.

::: Proposition 6
For a bilinear form $\langle-,-\rangle$ on a finite-dimensional $\mathbb{K}$-vector space $V$, being reflexive is equivalent to being symmetric or alternating.
:::

::: Proof
One direction has already been seen, so it suffices to assume $\langle-,-\rangle$ is reflexive and show the converse. For any $u,v,w$,

$$\langle u,\langle u,w\rangle v-\langle u,v\rangle w\rangle=\langle u,w\rangle\langle u,v\rangle-\langle u,v\rangle\langle u,w\rangle=0$$

so by reflexivity, $\langle\langle u,w\rangle v-\langle u,v\rangle w,u\rangle=0$, and expanding in the same way gives

$$\langle u,w\rangle\langle v,u\rangle=\langle u,v\rangle\langle w,u\rangle\tag{$\ast$}$$

which holds for all $u,v,w$.

Now if $\langle u,u\rangle=0$ for all $u$, then

$$0=\langle u+v,u+v\rangle=\langle u,v\rangle+\langle v,u\rangle$$

so $\langle-,-\rangle$ is alternating.

Otherwise, there exists $u_0$ with $\langle u_0,u_0\rangle\neq 0$, and substituting $w=u=u_0$ into $(\ast)$ gives

$$\langle u_0,u_0\rangle\bigl(\langle v,u_0\rangle-\langle u_0,v\rangle\bigr)=0$$

so we know that $\langle v,u_0\rangle=\langle u_0,v\rangle$ holds for all $v$. Therefore, substituting $v=u_0$ into $(\ast)$ again gives

$$\langle u,u_0\rangle\bigl(\langle u,w\rangle-\langle w,u\rangle\bigr)=0$$

The above $u,w$ can be arbitrary vectors, and two cases exist. First, if $\langle u,u_0\rangle\neq 0$, then immediately $\langle u,w\rangle=\langle w,u\rangle$. If $\langle u,u_0\rangle=0$, setting $u'=u+u_0$ gives $\langle u', u_0\rangle=\langle u_0,u_0\rangle\neq 0$, so $\langle u', w\rangle=\langle w,u'\rangle$ holds for all $w$. But we have already shown above that $\langle u_0,w\rangle=\langle w,u_0\rangle$ for all vectors, and from this we obtain the conclusion.
:::

Thus, the forms for which the orthogonal complement is independent of left and right are exactly symmetric and alternating forms. In what follows, we develop results for subspaces in the setting of non-degenerate reflexive forms, which in particular applies directly to non-degenerate alternating forms as well. Let us add a few definitions.

::: Definition 7
For a subspace $W\leq V$ of a finite-dimensional $\mathbb{K}$-vector space $V$ with a non-degenerate reflexive bilinear form given, we define the following.

1. The intersection $W\cap W^\perp$ is called the *radical* of $W$.
2. If the radical is $\{0\}$, we say $W$ is *non-degenerate*.
3. If $W\subseteq W^\perp$, then the restriction of $\langle-,-\rangle$ to $W$ is identically zero, and in this case we say $W$ is *isotropic*.
4. If $W^\perp\subseteq W$, we say $W$ is *coisotropic*.
5. A space with $W=W^\perp$ is called *Lagrangian*.
:::

The radical of $W$ is the set of vectors in $W$ that are orthogonal to all of $W$, so $W$ being non-degenerate is exactly equivalent to the restriction of $\langle-,-\rangle$ to $W$ being again non-degenerate.

::: Proposition 8
For any subspace $W\leq V$ of a finite-dimensional $\mathbb{K}$-vector space $V$ with a non-degenerate reflexive bilinear form given, the following hold.

1. $\dim W+\dim W^\perp=\dim V$.
2. $(W^\perp)^\perp=W$.
3. The conditions that $W$ is non-degenerate, that $W^\perp$ is non-degenerate, and that $V=W\oplus W^\perp$ are all equivalent.
:::
::: Proof
The restriction $V^\ast\rightarrow W^\ast$, which is the dual of the inclusion map $W\hookrightarrow V$, is surjective. ([§Dual Space, ⁋Proposition 6](/en/math/linear_algebra/dual_space#prop6)) On the other hand, since $\langle-,-\rangle$ is non-degenerate, $v\mapsto\langle v,-\rangle$ is injective and has the same dimension, so it defines an isomorphism $V\rightarrow V^\ast$. Therefore, the composition of this with the above restriction

$$V\rightarrow W^\ast;\qquad v\mapsto\langle v,-\rangle\vert_W$$

is also surjective, and its kernel is $W^\perp$ by definition. Thus by [§Isomorphic Vector Spaces, ⁋Theorem 7](/en/math/linear_algebra/isomorphic_vector_spaces#thm7), we have $\dim W^\perp=\dim V-\dim W^\ast=\dim V-\dim W$, so the first equality holds. The second claim follows from reflexivity giving $W\subseteq(W^\perp)^\perp$, and thus applying the first equality twice gives

$$\dim(W^\perp)^\perp=\dim V-\dim W^\perp=\dim W$$

so the two spaces coincide, which is obvious.

Finally, combining [§Dimension of Vector Spaces, ⁋Example 8](/en/math/linear_algebra/dimension#ex8) with 1,

$$\dim(W+W^\perp)=\dim W+\dim W^\perp-\dim(W\cap W^\perp)=\dim V-\dim(W\cap W^\perp)$$

Thus the radical $W\cap W^\perp$ of $W$ being $\{0\}$ is equivalent to $W+W^\perp=V$, and in this case the sum automatically becomes a direct sum by dimension count, so $V=W\oplus W^\perp$. On the other hand, by the second claim, $W\cap W^\perp=W^\perp\cap(W^\perp)^\perp$ is also the radical of $W^\perp$, so $W$ being non-degenerate and $W^\perp$ being non-degenerate are equivalent.
:::

For non-degenerate subspaces satisfying the above condition, the orthogonal complement defined in this way is canonically isomorphic to the quotient space.

::: Proposition 9
For a non-degenerate subspace $W\leq V$ of a finite-dimensional $\mathbb{K}$-vector space $V$ with a non-degenerate reflexive bilinear form given, the restriction of the natural projection $p:V\rightarrow V/W$ ([§Quotient Space, ⁋Definition 3](/en/math/linear_algebra/quotient_space#def3)) to $W^\perp$

$$p\vert_{W^\perp}:W^\perp\rightarrow V/W$$

is an isomorphism.
:::
::: Proof
Since $W$ is non-degenerate, by [Proposition 8](#prop8) we have $V=W\oplus W^\perp$. The natural projection satisfies $\ker p=W$, so the kernel of $p\vert_{W^\perp}$ is $W^\perp\cap W=\{0\}$, hence it is injective; and since $V=W+W^\perp$, for any $v=w+w'$ ($w\in W$, $w'\in W^\perp$) we have $p(w')=w'+W=v+W$, so it is surjective. Therefore $p\vert_{W^\perp}$ is an isomorphism.
:::

Thus, from the direct sum $V=W\oplus W^\perp$, if we fold away $W$, then $W^\perp$ exactly realizes the quotient $V/W$. In general, the quotient space $V/W$ is a canonical object defined even without $\langle-,-\rangle$, whereas $W^\perp$, which realizes it inside $V$, depends on the form, and without the non-degeneracy of [Proposition 8](#prop8) such an expression is impossible. For example, if $W$ is isotropic, then $W\cap W^\perp\neq\{0\}$, so $p\vert_{W^\perp}$ cannot be injective.

## The Four Fundamental Subspaces

Now let $V,W$ be two finite-dimensional $\mathbb{K}$-vector spaces with non-degenerate bilinear forms $\langle -,-\rangle_V$ and $\langle -,-\rangle_W$ given. In principle, the contents of this section can be developed even if these bilinear forms are reflexive, but to express them more cleanly in a form like equation (2) below, it is convenient to assume they are symmetric, so we make that assumption. Also, for convenience of discussion, let us denote the isomorphisms determined by these bilinear forms as

$$\varphi_V:V^\ast\rightarrow V,\qquad \varphi_W:W^\ast\rightarrow W$$

If two bases $\mathcal{B}=\{x_1,\ldots, x_n\}$ and $\mathcal{C}=\{y_1,\ldots, y_m\}$ are given on $V,W$ respectively, then the dual bases

$$\mathcal{B}^\ast=\{\xi^1,\ldots, \xi^n\},\qquad\mathcal{C}^\ast=\{\upsilon^1,\ldots,\upsilon^m\}$$

are well-defined. Now consider the bases obtained by moving these along $\varphi_V,\varphi_W$

$$\mathcal{B}'=\{\varphi_V(\xi^1),\ldots,\varphi_V(\xi^n)\},\qquad\mathcal{C}'=\{\varphi_W(\upsilon^1),\ldots,\varphi_W(\upsilon^m)\}$$

That is, these are elements of $V,W$ defined by the equations

$$\langle x_i,\varphi_V(\xi^j)\rangle=\delta_{ij},\qquad\langle y_i,\varphi_W(\upsilon^j)\rangle=\delta_{ij}$$

Now for any $L:V\rightarrow W$, suppose

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

If we think of the dual map $L^\ast:W^\ast\rightarrow V^\ast$ as a map from $W$ to $V$ via the above identifications $\varphi$, that is, if we consider $L':W\rightarrow V$ defined by the following diagram

![identification](/assets/images/Math/Linear_Algebra/Bilinear_Form-1.svg){:style="width:8.27em" class="invert" .align-center}

then we can verify that the matrix representation of this linear map with respect to the two bases $\mathcal{C}'$, $\mathcal{B}'$ is $[L']_{\mathcal{B}'}^{\mathcal{C}'}$.

On the other hand, the $L':W\rightarrow V$ defined in this way satisfies the equation

$$\langle Lv, w\rangle_W=\langle v,L'w\rangle_V\qquad\text{for all $v\in V$ and $w\in W$}\tag{2}$$

This can be checked from

$$\langle Lv,w\rangle=(\varphi^{-1}(w))(Lv)=(\varphi^{-1}_W(w)\circ L)(v)=(L^\ast(\varphi^{-1}_W(w))(v)=(\varphi^{-1}_V(v)\circ L')(w)=(\varphi^{-1}_V(v))(L'w)=\langle v,L'w\rangle$$

We call such an $L'$ satisfying this equation the *adjoint* of the linear map $L$, and with slight abuse of notation, we also write it as $L^\ast$.

The results of [§Dual Space, §§Orthogonal Complement](/en/math/linear_algebra/dual_space#orthogonal-complement) were all obtained from the equation $(Lv,f)=(v,L^\ast f)$ for the canonical pairing. Therefore, replacing this with equation (2) for the non-degenerate bilinear forms $\langle -,-\rangle$ obtained above, we get the following results.

::: Proposition 10
Let $V,W$ be two $\mathbb{K}$-vector spaces with symmetric non-degenerate bilinear forms given, and let $L:V\rightarrow W$ be a linear map with adjoint $L^\ast:W\rightarrow V$. Then

1. For any subspace $U\subseteq V$, $L(U)^\perp=(L^\ast)^{-1}(U^\perp)$ holds.
2. For any subspace $U\subseteq W$, $L^\ast(U)^\perp=L^{-1}(U^\perp)$ holds.
3. $(\im L)^\perp=\ker(L^\ast)$ holds.
4. $(\im L^\ast)^\perp=\ker L$ holds.
:::

In particular, the subspaces of $V$ and $W$ obtained from 3 and 4

$$\ker L, \quad(\ker L)^\perp, \quad\im L,\quad(\im L)^\perp$$

are sometimes called the *four fundamental subspaces* determined by $L$. If $\ker L$ and $\im L$ are non-degenerate in the sense of [Definition 7](#def7), then by [Proposition 8](#prop8) they decompose orthogonally as

$$V=\ker L\oplus(\ker L)^\perp,\qquad W=\im L\oplus(\im L)^\perp$$

and in particular, if $\langle-,-\rangle$ is positive-definite, then all subspaces are non-degenerate, so this decomposition always holds.

## Orthogonal Basis

Now consider a $\mathbb{K}$-vector space $V$ with a symmetric non-degenerate bilinear form given. A subset $\{v_1,\ldots, v_n\}$ of $V$ is called an *orthogonal set* if $\langle v_i,v_j\rangle=0$ whenever $i\neq j$. If a basis $\mathcal{B}$ of $V$ is also an orthogonal set, we call it an *orthogonal basis*.

::: Definition 11
If a field $\mathbb{K}$ satisfies the condition

$$\underbrace{1+1+\cdots+1}_\text{$p$ times}=0$$

then we say the *characteristic* of $\mathbb{K}$ is $p$, and denote this by $\ch \mathbb{K}=p$. If no natural number $p$ satisfying the above equation exists, we consider $\mathbb{K}$ to have characteristic 0.
:::

For example, $\mathbb{R}$ has characteristic 0. If we define addition and multiplication on $\mathbb{F}_2=\{0,1\}$ by

$$0+0=0,\quad 0+1=1,\quad 1+0=1,\quad 1+1=2$$

and

$$0\cdot 0=0,\quad 0\cdot 1=0,\quad 1\cdot 0=0,\quad 1\cdot 1=1$$

respectively, then we can verify that $\mathbb{F}_2$ satisfies the field axioms, and in this case $\ch\mathbb{F}_2=2$.

::: Proposition 12
For a field $\mathbb{K}$ with $\ch \mathbb{K}\neq 2$, a $\mathbb{K}$-vector space $V$ with a symmetric non-degenerate bilinear form given always has an orthogonal basis.
:::
::: Proof
First let us show a simple lemma. For any fixed $v\in V$, there exists $u\in V$ such that $\langle u,v\rangle\neq 0$. Then

$$2\langle u,v\rangle=\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle$$

and from the two conditions $\langle u,v\rangle\neq 0$ and $\ch \mathbb{K}\neq 2$, the left-hand side is not zero. Therefore, among the three terms on the right-hand side, $\langle u+v,u+v\rangle, \langle u,u\rangle,\langle v,v\rangle$, at least one is not zero. Thus,

> For any $\mathbb{K}$-vector space with a non-degenerate symmetric bilinear form given, there always exists $w$ satisfying $\langle w,w\rangle\neq 0$.

We prove the original proposition by induction on the dimension of $V$. The case $\dim V=0$ is trivial. Now assume the proof is complete for $\dim V=k$. Then for any vector space $V$ with $\dim V=k+1$, there exists a vector $w$ satisfying $\langle w,w\rangle\neq 0$.

Now let $W=\span w$. Since $\langle w,w\rangle\neq 0$, we have $w\notin W^\perp$, and since $W$ is 1-dimensional, $W\cap W^\perp=\{0\}$, so $W$ is non-degenerate in the sense of [Definition 7](#def7). Therefore by [Proposition 8](#prop8), $V=W\oplus W^\perp$ and $W^\perp$ is also non-degenerate with $\dim W^\perp=\dim V-1=k$. Applying the induction hypothesis to the $k$-dimensional space $W^\perp$ with non-degenerate form, there exists an orthogonal basis $\mathcal{B}$, and since $W=\span w$ is orthogonal to $W^\perp$, $\mathcal{B}\cup\{w\}$ is an orthogonal basis for $V$.
:::

## Gram Matrix

Let a bilinear form $\langle-,-\rangle:V\times V\rightarrow \mathbb{K}$ be given. If a basis $\{x_1,\ldots, x_n\}$ of $V$ is fixed, then for any $v=\sum v_ix_i, w=\sum w_jx_j$, the equation

$$\langle v,w\rangle=\left\langle\sum_{i=1}^nv_ix_i,\sum_{j=1}^n w_jx_j\right\rangle=\sum_{i,j=1}^n v_iw_j\langle x_i,x_j\rangle$$

holds. Let us temporarily denote by $G$ the $n\times n$ matrix whose $(i,j)$ entry is $\langle x_i,x_j\rangle$; then the above equation can be written simply as

$$\langle v,w\rangle=v^t Gw$$

In this case, we call $G$ the *Gram matrix* with respect to the basis $\mathcal{B}$.

Consider two bases $\mathcal{B},\mathcal{C}$ given on $V$. Denote their Gram matrices by $G_\mathcal{B},G_\mathcal{C}$ respectively, and write the above equation precisely as

$$\langle v,w\rangle=[v]^t_\mathcal{B}G_\mathcal{B}[w]_\mathcal{B}=[v]^t_\mathcal{C}G_\mathcal{C}[w]_\mathcal{C}$$

Now since $[v]_\mathcal{C}=[\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}$, the rightmost side of the above equation becomes

$$[v]_\mathcal{C}^tG_\mathcal{C}[w]_\mathcal{C}=\left([\id]_\mathcal{C}^\mathcal{B}[v]_\mathcal{B}\right)^tG_\mathcal{B}\left([\id]_\mathcal{C}^\mathcal{B}[w]_\mathcal{B}\right)=[v]_\mathcal{B}^t\left(([\id]_\mathcal{C}^\mathcal{B})^t G_\mathcal{B}[\id]_\mathcal{C}^\mathcal{B}\right)[w]_\mathcal{B}$$

---

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
