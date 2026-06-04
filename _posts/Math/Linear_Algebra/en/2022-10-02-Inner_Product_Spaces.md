---
title: "Inner Product Spaces"
description: "We define inner products and norms on vector spaces, prove the Cauchy-Schwarz inequality, and examine the properties of the norm induced by an inner product."
excerpt: "Properties of inner products defined over the real numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-10-02
last_modified_at: 2022-10-02

weight: 117
translated_at: 2026-06-01T02:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T02:30:04+00:00
---
## Inner Products and Norms

We now consider a more special case.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$ is called an *inner product* if $$\langle v,v\rangle\geq 0$$ for all $$v\in V$$, with equality holding only when $$v=0$$. A space $$V$$ equipped with an inner product is simply called an *inner product space*.

</div>

Examining the definition, we see that the condition $$\langle v,v\rangle\geq 0$$ in the definition of an inner product requires the field $$\mathbb{K}$$ to possess an ordering, so it is not well defined for a general field $$\mathbb{K}$$. Therefore, we develop the theory only over $$\mathbb{R}$$, where an ordering is well defined, and in the next post we use this to define inner products over $$\mathbb{C}$$ as well. To avoid confusion, from now on we write an inner product space defined over the real numbers as an $$\mathbb{R}$$-inner product space.

A representative example of an inner product is the *dot product* defined on $$\mathbb{R}^n$$:

$$\langle v,w\rangle=\sum_{i=1}^n v_iw_i$$

We already know that this is a non-degenerate bilinear form on $$\mathbb{R}^n$$, and that $$\langle -,-\rangle$$ is symmetric is also obvious from the definition. Finally, for any $$v$$,

$$\langle v,v\rangle=\sum_{i=1}^n v_i^2\geq 0$$

and equality holds only when $$v=0$$.

Meanwhile, if an inner product is defined on an $$\mathbb{R}$$-vector space, one of the best consequences is that the *magnitude* of a vector is well defined.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A *norm* on an $$\mathbb{R}$$-vector space $$V$$ is a function $$\lVert -\rVert:V\rightarrow\mathbb{R}$$ satisfying the following conditions.

1. $$\lVert v\rVert\geq 0$$ for all $$v$$, with equality holding only when $$v=0$$.
2. For any $$\alpha\in\mathbb{R}$$ and $$v\in V$$, $$\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$$.
3. (Triangle inequality) For any $$u,v\in V$$, $$\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$$.

</div>

The following proposition is one we have been familiar with since high school.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Cauchy–Schwarz)**</ins> For any vectors $$v,w$$ in an $$\mathbb{R}$$-inner product space $$V$$, the inequality

$$\lvert \langle v,w\rangle\rvert\leq\sqrt{\langle u,u\rangle}\sqrt{\langle v,v\rangle}$$

holds. Equality holds when there exists a constant $$\lambda$$ such that $$u=\lambda v$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$v=0$$, then both sides are 0, so the inequality holds. Assume $$v\neq 0$$. Then $$\langle v,v\rangle\neq 0$$. Now define

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}$$

Then expanding the right-hand side of

$$0\leq \langle u-\lambda v, u-\lambda v\rangle$$

gives

$$0\leq \langle u,u\rangle-2\lambda\langle u,v\rangle+\lambda^2\langle v,v\rangle=\langle u,u\rangle-\frac{2\langle u,v\rangle^2}{\langle v,v\rangle}+\frac{\langle u,v\rangle^2}{\langle v,v\rangle}=\langle u,u\rangle-\frac{\langle u,v\rangle^2}{\langle v,v\rangle}$$

Equality holds exactly when $$u-\lambda v=0$$. From this we obtain the desired inequality.

</details>


<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For an $$\mathbb{R}$$-inner product space $$V$$, the function $$\lVert-\rVert:V\rightarrow \mathbb{R}$$ defined by

$$\lVert v\rVert:=\sqrt{\langle v,v\rangle}$$

is a norm.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the above expression $$\lVert v\rVert$$ is a function into $$\mathbb{R}$$. This is because $$(v,v)\geq 0$$ always holds.

The first and second conditions for a norm are obvious, so it suffices to show only the triangle inequality. For any $$u,v\in V$$,

$$\lVert u+v\rVert=\sqrt{\langle u+v,u+v\rangle}=\sqrt{\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle}$$

and applying the Cauchy–Schwarz inequality,

$$\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle\leq \lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=(\lVert u\rVert+\lVert v\rVert)^2$$

so the triangle inequality follows from this.

</details>

However, the converse of the above proposition does not hold in general. That is, while an inner product defined on $$V$$ determines a norm, a norm given on $$V$$ does not necessarily come from an inner product.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$V$$ be an $$\mathbb{R}$$-inner product space. If $$\lVert -\rVert$$ is the norm obtained from the inner product of $$V$$ by the formula in [Proposition 4](#prop4), then the *parallelogram law*

$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$

holds for all $$u,v$$.

</div>

The proof of this is easily obtained by a simple calculation. Also, through this we can find an example of a norm that is not defined by an inner product.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> On $$\mathbb{R}^n$$, define $$\lVert-\rVert_1:\mathbb{R}^n\rightarrow\mathbb{R}$$ by the formula

$$\lVert v\rVert_1=\sum_{i=1}^n \lvert v_i\rvert$$

Then $$\lVert-\rVert_1$$ satisfies all the conditions of a norm. If there existed an inner product $$\langle-,-\rangle_1$$ such that $$\lVert -\rVert_1$$ could be written in the form

$$\lVert v\rVert_1=\sqrt{\langle v,v\rangle_1}$$

then by [Proposition 5](#prop5), the equality

$$\lVert u+v\rVert_1^2+\lVert u-v\rVert_1^2=2\lVert u\rVert^2_1+2\lVert v\rVert^2_1$$

would have to hold. However, substituting $$u=(1,0,\ldots, 0)$$ and $$v=(0,1,\ldots, 0)$$ shows that the parallelogram law is not satisfied. Therefore $$\lVert -\rVert_1$$ is not induced by an inner product.

</div>

In fact, the converse of [Proposition 5](#prop5) also holds. That is, if $$\lVert-\rVert$$ satisfies the parallelogram law, then the form $$\langle-,-\rangle$$ defined by

$$\langle u,v\rangle:=\frac{1}{4}\left(\lVert u+v\rVert^2-\lVert u-v\rVert^2\right)$$

is an inner product. The proof of this is not very difficult, but it requires using the fact that $$V$$ is given a topological structure via the norm $$\lVert-\rVert$$. We will not need this result now, so we omit the proof.

## Orthonormal Bases

Since we know that $$\ch\mathbb{R}=0$$, from [§Bilinear Forms, ⁋Proposition 7](/en/math/linear_algebra/bilinear_form#prop7) we know that any $$\mathbb{R}$$-inner product space $$V$$ has an orthogonal basis.

Let an arbitrary $$\mathbb{R}$$-inner product space $$V$$ be given, and let a basis $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ of $$V$$ be given. First define

$$\hat{x}_1:=x_1$$

Then define

$$\hat{x}_k:=x_k-\sum_{i=1}^{k-1}\frac{\langle x_i,x_k\rangle}{\langle x_i,x_i\rangle}x_i$$

One can check that the set $$\{\hat{x}_1,\ldots, \hat{x}_n\}$$ obtained at the end of this process is an orthogonal basis. This method of obtaining an orthogonal basis from an arbitrary basis is called the *Gram–Schmidt process*. Sometimes we also want each element of the basis thus obtained to have size 1, and to achieve this we simply divide each vector by its own magnitude. A basis satisfying this property is called an *orthonormal basis*. If $$\mathcal{B}=\{x_1, \ldots, x_n\}$$ is an orthonormal basis, then for any $$v\in V$$, the components $$v_i$$ of

$$v=v_1x_1+\cdots+v_nx_n$$

can be found by taking $$\langle -, x_i\rangle$$. The left-hand side becomes $$\langle v, x_i\rangle$$, and since $$\langle x_j,x_i\rangle=\delta_{ij}$$, only $$v_i\langle x_i,x_i\rangle=v_i$$ remains on the right-hand side. That is,

$$v=\langle v, x_1\rangle x_1+\cdots+\langle v, x_n\rangle x_n$$

always holds. If $$\mathcal{B}$$ were merely an orthogonal basis, we would have had to take appropriate constant multiples to find these coefficients.

## Orthogonal Matrices

Consider an $$\mathbb{R}$$-inner product space $$V$$. Consider a linear map $$L:V\rightarrow V$$ and its adjoint. In this case, it is customary to write the adjoint of $$L$$ as $$L^t$$ instead of $$L^\ast$$. Then since

$$\langle v,Lw\rangle=\langle L^t v, w\rangle$$

always holds, if any linear map $$L$$ preserves $$\langle-,-\rangle$$, then for any $$v,w$$,

$$\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v, L^t Lw\rangle$$

holds, and therefore $$L^t L=I$$ holds. Thus we define as follows.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For any $$A\in\Mat_n(\mathbb{R})$$, if

$$A^tA=AA^t=I$$

holds, then $$A$$ is called an *orthogonal matrix*.

</div>

From the rank-nullity theorem, we know that if $$A^tA=I$$ then necessarily $$AA^t=I$$ also holds. Therefore, the matrix representation of any linear map preserving $$\langle-,-\rangle$$ is an orthogonal matrix.

Consider two orthonormal bases $$\mathcal{B}=\{x_1,\ldots, x_n\}$$, $$\mathcal{C}=\{x'_1,\ldots, x'_n\}$$ given on $$V$$. Then the $$i$$-th column of the matrix $$[\id]_\mathcal{C}^\mathcal{B}$$ is the same as the matrix representation of $$x_i$$ with respect to $$\mathcal{C}$$. Now from

$$x_i=\langle x_i, x'_1\rangle x'_1+\cdots+\langle x_i, x'_n\rangle x'_n$$

we obtain

$$[\id]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\langle x_1,x'_1\rangle&\langle x_2, x'_1\rangle&\cdots&\langle x_n,x'_1\rangle\\ \langle x_1,x'_2\rangle&\langle x_2,x'_2\rangle&\cdots&\langle x_n,x'_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x_1, x'_n\rangle&\langle x_2, x'_n\rangle&\cdots&\langle x_n,x'_n\rangle\end{pmatrix}$$

If we interchange the roles of $$\mathcal{B}$$ and $$\mathcal{C}$$, then

$$[\id]_\mathcal{B}^\mathcal{C}=\begin{pmatrix}\langle x'_1,x_1\rangle&\langle x'_2, x_1\rangle&\cdots&\langle x'_n,x_1\rangle\\ \langle x'_1,x_2\rangle&\langle x'_2,x_2\rangle&\cdots&\langle x'_n,x_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x'_1, x_n\rangle&\langle x'_2, x_n\rangle&\cdots&\langle x'_n,n\rangle\end{pmatrix}$$

so, from the condition that $$\langle-,-\rangle$$ is symmetric, we can verify that the change-of-basis matrix between two orthonormal bases is always an orthogonal matrix. Conversely, any orthogonal matrix can always be interpreted as a change-of-basis matrix between orthonormal bases.

## Projection Theorem

Now let $$V$$ be an $$\mathbb{R}$$-inner product space, and let $$U\subseteq V$$ be a subspace. If $$U\neq \{0\}$$, then for any $$u\in U$$ with $$u\neq 0$$, we have $$\langle u,u\rangle>0$$, so in particular the restriction of the inner product $$\langle -,-\rangle$$ of $$V$$ to $$U$$ is non-degenerate and thus defines a bilinear form on $$U$$. That this bilinear form has the properties of an inner product is almost obvious, so any subspace of an $$\mathbb{R}$$-inner product space always has a natural $$\mathbb{R}$$-inner product space structure. Therefore, there exists an orthonormal basis $$\mathcal{B}=\{x_1,\ldots, x_k\}$$ of $$U$$. Moreover, if we choose a basis of $$V$$ containing $$\mathcal{B}$$ and then apply the Gram–Schmidt process starting from $$x_1,\ldots, x_k$$, we can also verify that there exists an orthonormal basis of $$V$$ containing $$\mathcal{B}$$.

Now for any $$v\in V$$, define the *projection* $$\proj_U v$$ of $$v$$ onto $$U$$ by the formula

$$\proj_U v=\sum_{i=1}^k \langle v, x_i\rangle x_i$$

For this definition to make sense, the above vector must be defined independently of the choice of orthonormal basis $$\mathcal{B}$$ of $$U$$.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> In the above situation, if $$\mathcal{B}=\{x_1,\ldots, x_k\},\mathcal{B}'=\{x_1',\ldots, x_k'\}$$ are two orthonormal bases of $$U$$, then for any $$v\in V$$,

$$\sum_{i=1}^k \langle v, x_i\rangle x_i=\sum_{i=1}^k\langle v, x'_i\rangle x_i'$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is simply another expression of the equation

$$[v]_\mathcal{B}=[\id]^{\mathcal{B}'}_{\mathcal{B}}[v]_{\mathcal{B}'}$$

</details>

The following *projection theorem* tells us that the vector $$\proj_Uv$$ thus defined is the element of $$U$$ closest to $$v$$.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> Consider an $$\mathbb{R}$$-inner product space $$V$$ and its subspace $$U\subseteq V$$. Then for any $$v\in V$$, $$\proj_Uv$$ satisfies

$$\lVert \proj_Uv-v\rVert=\min_{w\in U}\lVert v-w\rVert$$

and moreover, the only vector satisfying the above equation is $$\proj_Uv$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$u,u'\in U$$ both minimize $$\lVert v-w\rVert$$. Then by minimality,

$$\lVert v-u\rVert=\lVert v-u'\rVert\leq\left\lVert v-\frac{u+u'}{2}\right\rVert$$

Therefore,

$$\lVert v-u\rVert+\lVert v-u'\rVert=\lVert (v-u)+(v-u')\rVert$$

From the equality condition of the triangle inequality, we know that there exists a constant $$\lambda$$ satisfying

$$v-u=\lambda (v-u')$$

In particular,

$$(1-\lambda)v=u-\lambda u'\in U$$

holds. From this, either $$\lambda=1$$ or $$v\in U$$. If $$\lambda=1$$, then from $$v-u=v-u'$$ we get $$u=u'$$, and if $$v\in U$$, then the only $$w$$ minimizing $$\lVert v-w\rVert$$ is $$w=v$$, so in this case also $$u=u'$$. Therefore the vector minimizing this expression is unique.

Now we must actually show that $$\proj_Uv$$ indeed minimizes $$\lVert v-w\rVert$$. Choose a basis $$\{x_1,\ldots, x_k\}$$ of $$U$$, and let $$\{x_1,\ldots, x_n\}$$ be an orthonormal basis of $$V$$ containing it. Then from $$v=\sum_{i=1}^n v_i x_i$$ and $$w=\sum_{i=1}^k w_i x_i$$,

$$\lVert v-w\rVert=\left\lVert\sum_{i=1}^k(v_i-w_i)x_i+\sum_{i=k+1}^n v_ix_i\right\rVert=\sum_{i=1}^k (v_i-w_i)^2+\sum_{i=k+1}^n v_i^2\geq \sum_{i=k+1}^n v_i^2$$

and equality holds when $$v_i=w_i$$ for all $$1\leq i\leq k$$. Then

$$\proj_Uv=\sum_{i=1}^k v_ix_i=\sum_{i=1}^k w_ix_i=w$$

so we obtain the desired conclusion.

</details>

Moreover, by the definition of $$\proj_Uv$$, it is obvious that $$v-\proj_Uv$$ is a vector perpendicular to $$U$$. This fact will be used usefully in the next post.
