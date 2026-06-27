---
title: "Inner Product Spaces"
description: "We define inner products and norms on vector spaces, prove the Cauchy-Schwarz inequality, and examine the properties of norms induced by inner products."
excerpt: "Properties of inner products over the real numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-10-02

weight: 117
translated_at: 2026-06-25T06:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-25T06:00:04+00:00
---
## Inner Products and Norms

We now consider a more special case.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$ is called an *inner product* if $$\langle v,v\rangle\geq 0$$ for all $$v\in V$$, and equality holds only when $$v=0$$. A space $$V$$ equipped with an inner product is simply called an *inner product space*.

</div>

Examining the definition, we see that the condition $$\langle v,v\rangle\geq 0$$ is not well-defined over a general field $$\mathbb{K}$$, because the field must possess a notion of order. Therefore, we develop the theory only over $$\mathbb{R}$$, where order is well-defined, and in the next post we use this to define an inner product over $$\mathbb{C}$$ as well. To avoid confusion, from now on we write an inner product space defined over the real numbers as an $$\mathbb{R}$$-inner product space.

A representative example of an inner product is the *dot product* on $$\mathbb{R}^n$$:

$$\langle v,w\rangle=\sum_{i=1}^n v_iw_i$$

We already know that this is a non-degenerate bilinear form on $$\mathbb{R}^n$$, and its symmetry is immediate from the definition. Finally, for any $$v$$,

$$\langle v,v\rangle=\sum_{i=1}^n v_i^2\geq 0$$

and equality holds only when $$v=0$$.

On the other hand, once an inner product is defined on an $$\mathbb{R}$$-vector space, one of the best consequences is that the <em-ko>size</em-ko> of a vector is well-defined.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A *norm* on an $$\mathbb{R}$$-vector space $$V$$ is a function $$\lVert -\rVert:V\rightarrow\mathbb{R}$$ satisfying the following conditions.

1. $$\lVert v\rVert\geq 0$$ for all $$v$$, and equality holds only when $$v=0$$.
2. For any $$\alpha\in\mathbb{R}$$ and $$v\in V$$, $$\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$$.
3. (Triangle inequality) For any $$u,v\in V$$, $$\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$$.

</div>

The following proposition is something we have been familiar with since high school.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Cauchy–Schwarz)**</ins> For any vectors $$v,w$$ of an $$\mathbb{R}$$-inner product space $$V$$, the inequality

$$\lvert \langle v,w\rangle\rvert\leq\sqrt{\langle u,u\rangle}\sqrt{\langle v,v\rangle}$$

holds. Equality holds when there exists a constant $$\lambda$$ satisfying $$u=\lambda v$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$v=0$$, then both sides are 0, so the inequality holds. Assume $$v\neq 0$$. Then $$\langle v,v\rangle\neq 0$$. Define

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}$$

and expand the right-hand side of

$$0\leq \langle u-\lambda v, u-\lambda v\rangle$$

to obtain

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

First, the expression $$\lVert v\rVert$$ defines a function into $$\mathbb{R}$$, because $$(v,v)\geq 0$$ always holds.

The first and second conditions for a norm are obvious, so it suffices to verify only the triangle inequality. For any $$u,v\in V$$,

$$\lVert u+v\rVert=\sqrt{\langle u+v,u+v\rangle}=\sqrt{\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle}$$

and by the Cauchy–Schwarz inequality,

$$\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle\leq \lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=(\lVert u\rVert+\lVert v\rVert)^2$$

so the triangle inequality follows.

</details>

However, the converse of the above proposition does not hold in general. That is, an inner product on $$V$$ induces a norm, but a given norm need not arise from any inner product.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$V$$ be an $$\mathbb{R}$$-inner product space. If $$\lVert -\rVert$$ is the norm obtained from the inner product of $$V$$ via the formula in [Proposition 4](#prop4), then the *parallelogram law*

$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$

holds for all $$u,v$$.

</div>

The proof is a straightforward computation. Moreover, this lets us find examples of norms that are not induced by any inner product.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> On $$\mathbb{R}^n$$, define $$\lVert-\rVert_1:\mathbb{R}^n\rightarrow\mathbb{R}$$ by

$$\lVert v\rVert_1=\sum_{i=1}^n \lvert v_i\rvert$$

Then $$\lVert-\rVert_1$$ satisfies all the conditions of a norm. If there were an inner product $$\langle-,-\rangle_1$$ such that $$\lVert -\rVert_1$$ could be written as

$$\lVert v\rVert_1=\sqrt{\langle v,v\rangle_1}$$

then by [Proposition 5](#prop5) the identity

$$\lVert u+v\rVert_1^2+\lVert u-v\rVert_1^2=2\lVert u\rVert^2_1+2\lVert v\rVert^2_1$$

would have to hold. But substituting $$u=(1,0,\ldots, 0)$$ and $$v=(0,1,\ldots, 0)$$ shows that the parallelogram law fails. Therefore $$\lVert -\rVert_1$$ is not induced by any inner product.

</div>

In fact, the converse of [Proposition 5](#prop5) also holds: if $$\lVert-\rVert$$ satisfies the parallelogram law, then the form defined by

$$\langle u,v\rangle:=\frac{1}{4}\left(\lVert u+v\rVert^2-\lVert u-v\rVert^2\right)$$

is an inner product. The proof is not very difficult, but it requires the fact that $$V$$ is equipped with a topological structure via the norm $$\lVert-\rVert$$. Since we will not need this result now, we omit the proof.

## Orthonormal Bases

Since we know that $$\ch\mathbb{R}=0$$, from [§Bilinear Forms, ⁋Proposition 7](/en/math/linear_algebra/bilinear_form#prop7) we know that every $$\mathbb{R}$$-inner product space $$V$$ admits an orthogonal basis.

Let $$V$$ be an $$\mathbb{R}$$-inner product space, and let $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ be a basis of $$V$$. First define

$$\hat{x}_1:=x_1$$

and then define

$$\hat{x}_k:=x_k-\sum_{i=1}^{k-1}\frac{\langle x_i,x_k\rangle}{\langle x_i,x_i\rangle}x_i$$

At the end of this process, one can verify that the set $$\{\hat{x}_1,\ldots, \hat{x}_n\}$$ is an orthogonal basis. This method of obtaining an orthogonal basis from an arbitrary basis is called the *Gram–Schmidt process*. Sometimes we also want each element of the resulting basis to have size 1, and for this it suffices to divide each vector by its own norm. A basis satisfying this property is called an *orthonormal basis*. If $$\mathcal{B}=\{x_1, \ldots, x_n\}$$ is an orthonormal basis, then for any $$v\in V$$ written as

$$v=v_1x_1+\cdots+v_nx_n$$

we can recover each component $$v_i$$ by applying $$\langle -, x_i\rangle$$. The left-hand side yields $$\langle v, x_i\rangle$$, and since $$\langle x_j,x_i\rangle=\delta_{ij}$$, only $$v_i\langle x_i,x_i\rangle=v_i$$ remains. Hence

$$v=\langle v, x_1\rangle x_1+\cdots+\langle v, x_n\rangle x_n$$

always holds. If $$\mathcal{B}$$ were merely an orthogonal basis, we would have had to take appropriate constant multiples to find these coefficients.

## Orthogonal Matrices

Let $$V$$ be an $$\mathbb{R}$$-inner product space and consider a linear operator $$L:V\rightarrow V$$ on it. In [§Dual Spaces](/en/math/linear_algebra/dual_space) we defined the dual $$L^\ast:V^\ast\rightarrow V^\ast$$ of $$L$$ as the linear operator satisfying

$$(Lv,f)=(v,L^\ast f)\qquad\text{for all $v\in V$, $f\in V^\ast$}$$

with respect to the canonical pairing $$(-,-)$$. On the other hand, if an inner product is given on $$V$$, then for any $$0\neq v\in V$$ we have $$\langle v,v\rangle>0$$, so the inner product is non-degenerate; therefore by [§Dual Spaces, ⁋Proposition 4](/en/math/linear_algebra/dual_space#prop4),

$$v\mapsto\langle v,-\rangle$$

the map $$V\rightarrow V^\ast$$ defined by this is injective. Since $$\dim V=\dim V^\ast$$, this is an isomorphism, and through this isomorphism the inner product identifies $$V$$ with its dual space $$V^\ast$$. The operator on $$V$$ obtained by transferring $$L^\ast$$ back through this isomorphism is called the *adjoint* of $$L$$; by convention it is written as $$L^t$$ to distinguish it from the dual $$L^\ast$$. That is, $$L^t:V\rightarrow V$$ is the operator defined so that for any $$v\in V$$,

$$\langle L^t v,-\rangle=L^\ast\bigl(\langle v,-\rangle\bigr)$$

The right-hand side is the functional $$\langle v,-\rangle\circ L$$, i.e. $$w\mapsto\langle v,Lw\rangle$$, so this is equivalent to

$$\langle v,Lw\rangle=\langle L^t v,w\rangle$$

holding for all $$v,w\in V$$.

In particular, if we choose an orthonormal basis $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ of $$V$$, then since $$\langle x_i,x_j\rangle=\delta_{ij}$$, the set $$\{\langle x_1,-\rangle,\ldots,\langle x_n,-\rangle\}$$ is exactly the dual basis of $$\mathcal{B}$$. Thus the above isomorphism sends an orthonormal basis to its dual basis, so the matrix representation of $$L^t$$ with respect to $$\mathcal{B}$$ coincides with the matrix representation of $$L^\ast$$ with respect to the dual basis. As we saw in [§Dual Spaces](/en/math/linear_algebra/dual_space), the latter is the transpose of $$[L]_\mathcal{B}^\mathcal{B}$$; hence for an orthonormal basis, the matrix of the adjoint $$L^t$$ is the transpose of the matrix of $$L$$. The notation $$L^t$$ originates from this.

Now if an arbitrary linear map $$L$$ preserves $$\langle-,-\rangle$$, then for any $$v,w$$,

$$\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v, L^t Lw\rangle$$

holds, and therefore $$L^t L=I$$. Thus we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For any $$A\in\Mat_n(\mathbb{R})$$, if

$$A^tA=AA^t=I$$

holds, then $$A$$ is called an *orthogonal matrix*.

</div>

From the rank-nullity theorem, we know that if $$A^tA=I$$ then necessarily $$AA^t=I$$ as well. Therefore, the matrix representation of any linear map preserving $$\langle-,-\rangle$$ is an orthogonal matrix.

Consider two orthonormal bases $$\mathcal{B}=\{x_1,\ldots, x_n\}$$, $$\mathcal{C}=\{x'_1,\ldots, x'_n\}$$ of $$V$$. Then the $$i$$-th column of the matrix $$[\id]_\mathcal{C}^\mathcal{B}$$ is the coordinate vector of $$x_i$$ with respect to $$\mathcal{C}$$. From

$$x_i=\langle x_i, x'_1\rangle x'_1+\cdots+\langle x_i, x'_n\rangle x'_n$$

we obtain

$$[\id]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\langle x_1,x'_1\rangle&\langle x_2, x'_1\rangle&\cdots&\langle x_n,x'_1\rangle\\ \langle x_1,x'_2\rangle&\langle x_2,x'_2\rangle&\cdots&\langle x_n,x'_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x_1, x'_n\rangle&\langle x_2, x'_n\rangle&\cdots&\langle x_n,x'_n\rangle\end{pmatrix}$$

Interchanging the roles of $$\mathcal{B}$$ and $$\mathcal{C}$$,

$$[\id]_\mathcal{B}^\mathcal{C}=\begin{pmatrix}\langle x'_1,x_1\rangle&\langle x'_2, x_1\rangle&\cdots&\langle x'_n,x_1\rangle\\ \langle x'_1,x_2\rangle&\langle x'_2,x_2\rangle&\cdots&\langle x'_n,x_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x'_1, x_n\rangle&\langle x'_2, x_n\rangle&\cdots&\langle x'_n,n\rangle\end{pmatrix}$$

so from the symmetry of $$\langle-,-\rangle$$ we can verify that the change-of-basis matrix between two orthonormal bases is always an orthogonal matrix. Conversely, any orthogonal matrix can always be interpreted as a change-of-basis matrix between orthonormal bases.

## Projection Theorem

Now let $$V$$ be an $$\mathbb{R}$$-inner product space, and let $$U\subseteq V$$ be a subspace. If $$U\neq \{0\}$$, then for any $$u\in U$$ with $$u\neq 0$$ we have $$\langle u,u\rangle>0$$, so in particular the restriction of the inner product $$\langle -,-\rangle$$ of $$V$$ to $$U$$ is non-degenerate and therefore defines a bilinear form on $$U$$. That this bilinear form has the properties of an inner product is almost obvious, so any subspace of an $$\mathbb{R}$$-inner product space naturally inherits an $$\mathbb{R}$$-inner product space structure. Hence there exists an orthonormal basis $$\mathcal{B}=\{x_1,\ldots, x_k\}$$ of $$U$$. Moreover, if we choose a basis of $$V$$ containing $$\mathcal{B}$$ and then apply the Gram–Schmidt process starting from $$x_1,\ldots, x_k$$, we can also verify that there exists an orthonormal basis of $$V$$ containing $$\mathcal{B}$$.

Now for any $$v\in V$$, define the *projection* of $$v$$ onto $$U$$, $$\proj_U v$$, by

$$\proj_U v=\sum_{i=1}^k \langle v, x_i\rangle x_i$$

For this definition to be well-defined, the above vector must be independent of the choice of orthonormal basis $$\mathcal{B}$$ of $$U$$.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> In the above situation, if $$\mathcal{B}=\{x_1,\ldots, x_k\},\mathcal{B}'=\{x_1',\ldots, x_k'\}$$ are two orthonormal bases of $$U$$, then for any $$v\in V$$,

$$\sum_{i=1}^k \langle v, x_i\rangle x_i=\sum_{i=1}^k\langle v, x'_i\rangle x_i'$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is simply another expression of the formula

$$[v]_\mathcal{B}=[\id]^{\mathcal{B}'}_{\mathcal{B}}[v]_{\mathcal{B}'}$$

</details>

The following *projection theorem* tells us that the vector $$\proj_Uv$$ defined in this way is the element of $$U$$ closest to $$v$$.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> Let $$V$$ be an $$\mathbb{R}$$-inner product space and $$U\subseteq V$$ a subspace. Then for any $$v\in V$$, $$\proj_Uv$$ satisfies

$$\lVert \proj_Uv-v\rVert=\min_{w\in U}\lVert v-w\rVert$$

and moreover, the only vector satisfying the above formula is $$\proj_Uv$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose both $$u,u'\in U$$ minimize $$\lVert v-w\rVert$$. Then by minimality,

$$\lVert v-u\rVert=\lVert v-u'\rVert\leq\left\lVert v-\frac{u+u'}{2}\right\rVert$$

Therefore,

$$\lVert v-u\rVert+\lVert v-u'\rVert=\lVert (v-u)+(v-u')\rVert$$

By the equality condition of the triangle inequality, there exists a constant $$\lambda$$ satisfying

$$v-u=\lambda (v-u')$$

In particular,

$$(1-\lambda)v=u-\lambda u'\in U$$

holds. From this, either $$\lambda=1$$ or $$v\in U$$. If $$\lambda=1$$, then from $$v-u=v-u'$$ we get $$u=u'$$; if $$v\in U$$, then the only minimizer of $$\lVert v-w\rVert$$ is $$w=v$$, so in this case too $$u=u'$$. Therefore the minimizer is unique.

Now we must show that $$\proj_Uv$$ actually minimizes $$\lVert v-w\rVert$$. Choose a basis $$\{x_1,\ldots, x_k\}$$ of $$U$$, and let $$\{x_1,\ldots, x_n\}$$ be an orthonormal basis of $$V$$ containing it. Then from $$v=\sum_{i=1}^n v_i x_i$$ and $$w=\sum_{i=1}^k w_i x_i$$,

$$\lVert v-w\rVert=\left\lVert\sum_{i=1}^k(v_i-w_i)x_i+\sum_{i=k+1}^n v_ix_i\right\rVert=\sum_{i=1}^k (v_i-w_i)^2+\sum_{i=k+1}^n v_i^2\geq \sum_{i=k+1}^n v_i^2$$

and equality holds when $$v_i=w_i$$ for all $$1\leq i\leq k$$. Then

$$\proj_Uv=\sum_{i=1}^k v_ix_i=\sum_{i=1}^k w_ix_i=w$$

so we obtain the desired conclusion.

</details>

Moreover, from the definition of $$\proj_Uv$$ it is obvious that $$v-\proj_Uv$$ is a vector perpendicular to $$U$$. This fact will be useful in the next post.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  

---
