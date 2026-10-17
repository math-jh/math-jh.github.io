---
title: "Inner Product Spaces"
description: "We define inner products and norms on vector spaces, prove the Cauchy-Schwarz inequality, and examine the properties of norms induced by inner products."
excerpt: "Properties of inner products defined over the real numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-10-02

weight: 21
translated_at: 2026-06-25T06:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-17T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Inner Products and Norms

We now consider a more special case.

::: Definition 1
On an $\mathbb{R}$-vector space $V$, a symmetric bilinear form $\langle-,-\rangle$ is called an *inner product* if for all $v\in V$, $\langle v,v\rangle\geq 0$, where equality holds only when $v=0$. A space $V$ equipped with an inner product is simply called an *inner product space*.
:::

Examining the definition, we see that the condition $\langle v,v\rangle\geq 0$ in the definition of an inner product requires the field $\mathbb{K}$ to have a notion of order, and so it is not well-defined over a general field $\mathbb{K}$. Therefore, we develop the theory only over $\mathbb{R}$, a field in which order is well-defined, and in the next post we use this to define an inner product over $\mathbb{C}$ as well. To avoid confusion, from now on we write an inner product space defined over the real numbers as an $\mathbb{R}$-inner product space.

A representative example of an inner product is the *dot product* defined on $\mathbb{R}^n$:

$$\langle v,w\rangle=\sum_{i=1}^n v_iw_i$$

We already know that this is a non-degenerate bilinear form on $\mathbb{R}^n$, and it is also obvious from the definition that $\langle -,-\rangle$ is symmetric. Finally, for any $v$,

$$\langle v,v\rangle=\sum_{i=1}^n v_i^2\geq 0$$

and equality holds only when $v=0$.

On the other hand, once an inner product is defined on an $\mathbb{R}$-vector space, one of the best consequences is that the *size* of a vector is well-defined.

::: Definition 2
A *norm* defined on an $\mathbb{R}$-vector space $V$ is a function $\lVert -\rVert:V\rightarrow\mathbb{R}$ satisfying the following conditions.

1. $\lVert v\rVert\geq 0$ holds for all $v$, and in particular, equality holds only when $v=0$.
2. For any $\alpha\in\mathbb{R}$ and $v\in V$, $\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$ holds.
3. (Triangle inequality) For any $u,v\in V$, $\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$ holds.
:::

The following proposition is something we have been familiar with since high school.

::: Proposition 3 (Cauchy-Schwarz)
In an $\mathbb{R}$-inner product space $V$, for any vectors $u,v$, the inequality

$$\lvert \langle u,v\rangle\rvert\leq\sqrt{\langle u,u\rangle}\sqrt{\langle v,v\rangle}$$

holds. Equality holds when $u=\lambda v$ is satisfied by some constant $\lambda$.
:::
::: Proof
If $v=0$, then both sides are 0, so the inequality holds. Assume $v\neq 0$. Then $\langle v,v\rangle\neq 0$. Now if we define

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}$$

and expand the right-hand side of

$$0\leq \langle u-\lambda v, u-\lambda v\rangle$$

we obtain

$$0\leq \langle u,u\rangle-2\lambda\langle u,v\rangle+\lambda^2\langle v,v\rangle=\langle u,u\rangle-\frac{2\langle u,v\rangle^2}{\langle v,v\rangle}+\frac{\langle u,v\rangle^2}{\langle v,v\rangle}=\langle u,u\rangle-\frac{\langle u,v\rangle^2}{\langle v,v\rangle}$$

Equality holds exactly when $u-\lambda v=0$. From this we obtain the desired inequality.
:::


::: Proposition 4
For an $\mathbb{R}$-inner product space $V$, the formula

$$\lVert v\rVert:=\sqrt{\langle v,v\rangle}$$

defines a function $\lVert-\rVert:V\rightarrow \mathbb{R}$, which is a norm.
:::
::: Proof
First, the expression $\lVert v\rVert$ above is a function into $\mathbb{R}$, because $\langle v,v\rangle\geq 0$ always holds.

Among the conditions for a norm, the first and second conditions are obvious, so it suffices to verify only the triangle inequality. For any $u,v\in V$,

$$\lVert u+v\rVert=\sqrt{\langle u+v,u+v\rangle}=\sqrt{\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle}$$

and applying the Cauchy-Schwarz inequality gives

$$\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle\leq \lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=(\lVert u\rVert+\lVert v\rVert)^2$$

from which the triangle inequality is proved.
:::

However, the converse of the above proposition does not hold in general. That is, an inner product defined on $V$ defines a norm, but conversely, having a given norm does not mean that an inner product can be defined.

::: Proposition 5
Let $V$ be an $\mathbb{R}$-inner product space. If $\lVert -\rVert$ is the norm obtained from the inner product of $V$ via the formula in [Proposition 4](#prop4){: data-lid="dtbso" }, then the *parallelogram law*

$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$

holds for all $u,v$.
:::

This can be easily proved by a simple computation. Moreover, this allows us to find an example of a norm that is not defined via an inner product.

::: Example 6
On $\mathbb{R}^n$, via the formula

$$\lVert v\rVert_1=\sum_{i=1}^n \lvert v_i\rvert$$

let us define $\lVert-\rVert_1:\mathbb{R}^n\rightarrow\mathbb{R}$. Then $\lVert-\rVert_1$ satisfies all the conditions of a norm. If there existed a suitable inner product $\langle-,-\rangle_1$ such that $\lVert -\rVert_1$ could be written in the form

$$\lVert v\rVert_1=\sqrt{\langle v,v\rangle_1}$$

then by [Proposition 5](#prop5){: data-lid="kb94f" }, the identity

$$\lVert u+v\rVert_1^2+\lVert u-v\rVert_1^2=2\lVert u\rVert^2_1+2\lVert v\rVert^2_1$$

would have to hold. However, substituting $u=(1,0,\ldots, 0)$ and $v=(0,1,\ldots, 0)$ shows that the parallelogram law is not satisfied. Therefore, $\lVert -\rVert_1$ is not induced by an inner product.
:::

In fact, the converse of [Proposition 5](#prop5){: data-lid="7ic9l" } also holds. That is, if $\lVert-\rVert$ satisfies the parallelogram law, then via the formula

$$\langle u,v\rangle:=\frac{1}{4}\left(\lVert u+v\rVert^2-\lVert u-v\rVert^2\right)$$

the resulting $\langle-,-\rangle$ so defined is an inner product. The proof of this is not very difficult, but it requires using the fact that $V$ is equipped with a topological structure via the norm $\lVert-\rVert$. Since we will not need to use this result right now, we move on without proving it.

## Orthonormal Bases

Since we know that $\ch\mathbb{R}=0$, we know from [§Bilinear Forms, ⁋Proposition 12](/en/math/linear_algebra/bilinear_form#prop12){: data-lid="67ck0" } that every $\mathbb{R}$-inner product space $V$ admits an orthogonal basis.

Suppose an arbitrary $\mathbb{R}$-inner product space $V$ is given, and on $V$ a basis $\mathcal{B}=\{x_1,\ldots, x_n\}$ is given. First, let us define

$$\hat{x}_1:=x_1$$

and then define

$$\hat{x}_k:=x_k-\sum_{i=1}^{k-1}\frac{\langle \hat{x}_i,x_k\rangle}{\langle \hat{x}_i,\hat{x}_i\rangle}\hat{x}_i$$

so that at the end of this process, one can verify that the resulting set $\{\hat{x}_1,\ldots, \hat{x}_n\}$ is an orthogonal basis. This method of obtaining an orthogonal basis from an arbitrary basis is called the *Gram–Schmidt process*. Sometimes we also want each element of the basis obtained in this way to have norm 1, and for this it suffices to divide each vector by its own norm. A basis satisfying this property is called an *orthonormal basis*. If $\mathcal{B}=\{x_1, \ldots, x_n\}$ is an orthonormal basis, then for any $v\in V$, in

$$v=v_1x_1+\cdots+v_nx_n$$

each component $v_i$ can be found by taking $\langle -, x_i\rangle$. This is because the left-hand side becomes $\langle v, x_i\rangle$, and on the right-hand side, since $\langle x_j,x_i\rangle=\delta_{ij}$, only $v_i\langle x_i,x_i\rangle=v_i$ remains. That is,

$$v=\langle v, x_1\rangle x_1+\cdots+\langle v, x_n\rangle x_n$$

always holds. If $\mathcal{B}$ had been merely an orthogonal basis, we would have had to take appropriate scalar multiples when finding these coefficients.

## Orthogonal Matrices

Consider an $\mathbb{R}$-inner product space $V$ and a linear operator $L:V\rightarrow V$ on it. In [§Dual Space](/en/math/linear_algebra/dual_space){: data-lid="c78fo" }, for $L$, we defined its dual $L^\ast:V^\ast\rightarrow V^\ast$ with respect to the canonical pairing $(-,-)$ to be the linear operator satisfying

$$(Lv,f)=(v,L^\ast f)\qquad\text{for all $v\in V$, $f\in V^\ast$}$$

On the other hand, if an inner product is given on $V$, then for any $0\neq v\in V$ we have $\langle v,v\rangle>0$, so the inner product is non-degenerate; therefore, by [§Dual Space, ⁋Proposition 4](/en/math/linear_algebra/dual_space#prop4){: data-lid="ef1g9" }, the assignment

$$v\mapsto\langle v,-\rangle$$

defines an injective map $V\rightarrow V^\ast$. Since $\dim V=\dim V^\ast$, this is an isomorphism, and through this isomorphism the inner product identifies $V$ with its dual space $V^\ast$. Now, what is obtained by transferring $L^\ast$ back to an operator on $V$ via this isomorphism is called the *adjoint* of $L$, and to distinguish it from the notation $L^\ast$ for the dual, it is customary to write it as $L^t$. That is, $L^t:V\rightarrow V$ is the operator defined so that for any $v\in V$,

$$\langle L^t v,-\rangle=L^\ast\bigl(\langle v,-\rangle\bigr)$$

Since the right-hand side is the functional $\langle v,-\rangle\circ L$, namely $w\mapsto\langle v,Lw\rangle$, this is equivalent to

$$\langle v,Lw\rangle=\langle L^t v,w\rangle$$

holding for all $v,w\in V$.

In particular, if for $V$ we choose an orthonormal basis $\mathcal{B}=\{x_1,\ldots, x_n\}$, then since $\langle x_i,x_j\rangle=\delta_{ij}$, the set $\{\langle x_1,-\rangle,\ldots,\langle x_n,-\rangle\}$ is precisely the dual basis of $\mathcal{B}$. Thus the above isomorphism sends an orthonormal basis to its dual basis, so the matrix representation of $L^t$ with respect to $\mathcal{B}$ coincides with the matrix representation of $L^\ast$ with respect to the dual basis. As we saw in [§Dual Space](/en/math/linear_algebra/dual_space){: data-lid="yr4si" }, the latter is the transpose of $[L]_\mathcal{B}^\mathcal{B}$; hence, with respect to an orthonormal basis, the matrix of the adjoint $L^t$ is the transpose of the matrix of $L$. The notation $L^t$ originates from this.

Now, if an arbitrary linear map $L$ preserves $\langle-,-\rangle$, then for any $v,w$,

$$\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v, L^t Lw\rangle$$

holds, and therefore $L^t L=I$ holds. Thus we make the following definition.

::: Definition 7
For any $A\in\Mat_n(\mathbb{R})$, if the equation

$$A^tA=AA^t=I$$

holds, then $A$ is called an *orthogonal matrix*.
:::

From the rank-nullity theorem, we know that if $A^tA=I$ holds, then necessarily $AA^t=I$ holds as well. Therefore, the matrix representation of any linear map preserving $\langle-,-\rangle$ is an orthogonal matrix.

In $V$, consider two given orthonormal bases $\mathcal{B}=\{x_1,\ldots, x_n\}$, $\mathcal{C}=\{x'_1,\ldots, x'_n\}$. Then in the matrix $[\id]_\mathcal{C}^\mathcal{B}$, the $i$-th column equals the matrix representation of $x_i$ with respect to $\mathcal{C}$. Now, from

$$x_i=\langle x_i, x'_1\rangle x'_1+\cdots+\langle x_i, x'_n\rangle x'_n$$

we have

$$[\id]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\langle x_1,x'_1\rangle&\langle x_2, x'_1\rangle&\cdots&\langle x_n,x'_1\rangle\\ \langle x_1,x'_2\rangle&\langle x_2,x'_2\rangle&\cdots&\langle x_n,x'_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x_1, x'_n\rangle&\langle x_2, x'_n\rangle&\cdots&\langle x_n,x'_n\rangle\end{pmatrix}$$

Interchanging the roles of $\mathcal{B}$ and $\mathcal{C}$ gives

$$[\id]_\mathcal{B}^\mathcal{C}=\begin{pmatrix}\langle x'_1,x_1\rangle&\langle x'_2, x_1\rangle&\cdots&\langle x'_n,x_1\rangle\\ \langle x'_1,x_2\rangle&\langle x'_2,x_2\rangle&\cdots&\langle x'_n,x_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x'_1, x_n\rangle&\langle x'_2, x_n\rangle&\cdots&\langle x'_n,x_n\rangle\end{pmatrix}$$

so from the condition that $\langle-,-\rangle$ is symmetric, we can verify that the change-of-basis matrix between two orthonormal bases is always an orthogonal matrix. Conversely, any orthogonal matrix can always be interpreted as a change-of-basis matrix between orthonormal bases.

## Projection theorem

Now suppose $V$ is an $\mathbb{R}$-inner product space and a subspace $U\subseteq V$ is given. If $U\neq \{0\}$, then for every $u\neq 0$ with $u\in U$ we have $\langle u,u\rangle>0$, so in particular restricting $V$'s inner product $\langle -,-\rangle$ to $U$ is non-degenerate and therefore defines a bilinear form on $U$. That the bilinear form defined in this way has the properties of an inner product is almost obvious, so any subspace of an $\mathbb{R}$-inner product space always has a natural $\mathbb{R}$-inner product space structure. Therefore, $U$ has an orthonormal basis $\mathcal{B}=\{x_1,\ldots, x_k\}$. Moreover, after choosing a basis containing $\mathcal{B}$ for $V$ and repeating the Gram–Schmidt process starting from $x_1,\ldots, x_k$, we can also verify that there exists an orthonormal basis containing $\mathcal{B}$ for $V$.

Now for any $v\in V$, let us define the *projection* of $v$ onto $U$, $\proj_U v$, by the equation

$$\proj_U v=\sum_{i=1}^k \langle v, x_i\rangle x_i$$

For this definition to make sense, the above vector must be defined independently of the choice of $U$'s orthonormal basis $\mathcal{B}$.

::: Lemma 8
In the above situation, if $\mathcal{B}=\{x_1,\ldots, x_k\},\mathcal{B}'=\{x_1',\ldots, x_k'\}$ are two orthonormal bases of $U$, then for any $v\in V$,

$$\sum_{i=1}^k \langle v, x_i\rangle x_i=\sum_{i=1}^k\langle v, x'_i\rangle x_i'$$

holds.
:::
::: Proof
This is simply another expression of the formula

$$[v]_\mathcal{B}=[\id]^{\mathcal{B}'}_{\mathcal{B}}[v]_{\mathcal{B}'}$$
:::

The following *projection theorem* tells us that the vector $\proj_Uv$ defined in this way is the element closest to $v$ in $U$.

::: Theorem 9
Consider an $\mathbb{R}$-inner product space $V$ and a subspace $U\subseteq V$. Then for any $v\in V$, $\proj_Uv$ satisfies

$$\lVert \proj_Uv-v\rVert=\min_{w\in U}\lVert v-w\rVert$$

and moreover, the only vector satisfying the above equation is $\proj_Uv$.
:::
::: Proof
First, suppose that both $u,u'\in U$ minimize $\lVert v-w\rVert$. Then by minimality, we obtain

$$\lVert v-u\rVert=\lVert v-u'\rVert\leq\left\lVert v-\frac{u+u'}{2}\right\rVert$$

Therefore,

$$\lVert v-u\rVert+\lVert v-u'\rVert=\lVert (v-u)+(v-u')\rVert$$

Now, by the equality condition of the triangle inequality, we know that the following equation

$$v-u=\lambda (v-u')$$

is satisfied by some constant $\lambda$. In particular,

$$(1-\lambda)v=u-\lambda u'\in U$$

holds. From this, either $\lambda=1$ or $v\in U$. If $\lambda=1$, then from $v-u=v-u'$ we have $u=u'$; if $v\in U$, then $\lVert v-w\rVert$ is minimized by $w$ only when $w=v$, so in this case as well, $u=u'$. Therefore, the vector that minimizes this expression is unique.

Now we must show that $\proj_Uv$ is indeed the vector that minimizes $\lVert v-w\rVert$. Choose for $U$ an orthonormal basis $\{x_1,\ldots, x_k\}$, and let an orthonormal basis of $V$ containing it be $\{x_1,\ldots, x_n\}$. Then from $v=\sum_{i=1}^n v_i x_i$ and $w=\sum_{i=1}^k w_i x_i$,

$$\lVert v-w\rVert^2=\left\lVert\sum_{i=1}^k(v_i-w_i)x_i+\sum_{i=k+1}^n v_ix_i\right\rVert^2=\sum_{i=1}^k (v_i-w_i)^2+\sum_{i=k+1}^n v_i^2\geq \sum_{i=k+1}^n v_i^2$$

and equality holds when, for all $1\leq i\leq k$, we have $v_i=w_i$. Then

$$\proj_Uv=\sum_{i=1}^k v_ix_i=\sum_{i=1}^k w_ix_i=w$$

so we obtain the desired conclusion.
:::

Moreover, by the definition of $\proj_Uv$, it is obvious that $v-\proj_Uv$ is a vector perpendicular to $U$. This fact will be used in the next post.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
