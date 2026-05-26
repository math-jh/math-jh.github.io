---
title: "Inner Product Spaces"
excerpt: "Properties of inner products defined over the real numbers"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/inner_product_spaces
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Inner_Product_Spaces.png
    overlay_filter: 0.5

date: 2022-10-02
last_modified_at: 2022-10-02

weight: 117
translated_at: 2026-05-21T12:30:01+00:00
translation_source: kimi-cli
---
## Inner Products and Norms

Now we consider a more specialized case.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$ is called an *inner product* if $$\langle v,v\rangle\geq 0$$ for all $$v\in V$$, and equality holds only when $$v=0$$. A space $$V$$ equipped with an inner product is simply called an *inner product space*.

</div>

Looking at the definition, we see that the condition $$\langle v,v\rangle\geq 0$$ in the definition of an inner product is not well defined for a general field $$\mathbb{K}$$, because the field $$\mathbb{K}$$ must have a notion of order. Therefore, we develop the theory only over the field $$\mathbb{R}$$, where order is well defined, and in the next post we use this to define inner products over $$\mathbb{C}$$ as well. To avoid confusion, from now on we write $$\mathbb{R}$$-inner product space for an inner product space defined over the real numbers.

A representative example of an inner product is the *dot product* defined on $$\mathbb{R}^n$$:

$$\langle v,w\rangle=\sum_{i=1}^n v_iw_i$$

We already know that this is a non-degenerate bilinear form on $$\mathbb{R}^n$$, and that $$\langle -,-\rangle$$ is symmetric is also clear from the definition. Finally, for any $$v$$,

$$\langle v,v\rangle=\sum_{i=1}^n v_i^2\geq 0$$

and equality holds only when $$v=0$$.

Meanwhile, if an inner product is defined on an $$\mathbb{R}$$-vector space, one of the best consequences is that the <em>length</em> of a vector is well defined.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A *norm* defined on an $$\mathbb{R}$$-vector space $$V$$ is a function $$\lVert -\rVert:V\rightarrow\mathbb{R}$$ satisfying the following conditions.

1. $$\lVert v\rVert\geq 0$$ holds for all $$v$$, and equality holds only when $$v=0$$.
2. For any $$\alpha\in\mathbb{R}$$ and $$v\in V$$, $$\lVert\alpha v\rVert=\lvert\alpha\rvert\lVert v\rVert$$ holds.
3. (Triangle inequality) For any $$u,v\in V$$, $$\lVert u+v\rVert\leq\lVert u\rVert+\lVert v\rVert$$ holds.

</div>

The following proposition is already familiar from high school.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3 (Cauchy–Schwarz)**</ins> For any vectors $$v,w$$ in an $$\mathbb{R}$$-inner product space $$V$$, the following inequality

$$\lvert \langle v,w\rangle\rvert\leq\sqrt{\langle u,u\rangle}\sqrt{\langle v,v\rangle}$$

holds. Equality holds when there exists a constant $$\lambda$$ satisfying $$u=\lambda v$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$v=0$$, then both sides are zero, so the inequality holds. Assume $$v\neq 0$$. Then $$\langle v,v\rangle\neq 0$$. Now define

$$\lambda=\frac{\langle u,v\rangle}{\langle v,v\rangle}$$

and expand the right-hand side of the following expression

$$0\leq \langle u-\lambda v, u-\lambda v\rangle$$

to obtain

$$0\leq \langle u,u\rangle-2\lambda\langle u,v\rangle+\lambda^2\langle v,v\rangle=\langle u,u\rangle-\frac{2\langle u,v\rangle^2}{\langle v,v\rangle}+\frac{\langle u,v\rangle^2}{\langle v,v\rangle}=\langle u,u\rangle-\frac{\langle u,v\rangle^2}{\langle v,v\rangle}$$

Equality holds precisely when $$u-\lambda v=0$$. From this we obtain the desired inequality.

</details>


<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For an $$\mathbb{R}$$-inner product space $$V$$, the function $$\lVert-\rVert:V\rightarrow \mathbb{R}$$ defined by the formula

$$\lVert v\rVert:=\sqrt{\langle v,v\rangle}$$

is a norm.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the above formula $$\lVert v\rVert$$ defines a function into $$\mathbb{R}$$. This is because $$\langle v,v\rangle\geq 0$$ always holds.

The first and second conditions for a norm are obvious, so it suffices to verify only the triangle inequality. For any $$u,v\in V$$,

$$\lVert u+v\rVert=\sqrt{\langle u+v,u+v\rangle}=\sqrt{\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle}$$

and applying the Cauchy–Schwarz inequality,

$$\langle u,u\rangle+2\langle u,v\rangle+\langle v,v\rangle\leq \lVert u\rVert^2+2\lVert u\rVert\lVert v\rVert+\lVert v\rVert^2=(\lVert u\rVert+\lVert v\rVert)^2$$

so the triangle inequality follows from this.

</details>

However, the converse of the above proposition does not hold in general. That is, an inner product defined on $$V$$ determines a norm, but conversely, a given norm does not necessarily come from an inner product.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$V$$ be an $$\mathbb{R}$$-inner product space. If $$\lVert -\rVert$$ is the norm obtained from the inner product on $$V$$ by the formula in [Proposition 4](#prop4), then the following *parallelogram law*

$$\lVert u+v\rVert^2+\lVert u-v\rVert^2=2\lVert u\rVert^2+2\lVert v\rVert^2$$

holds for all $$u,v$$.

</div>

The proof of this is easily carried out by a simple computation. Moreover, through this we can find an example of a norm that is not induced by an inner product.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Define $$\lVert-\rVert_1:\mathbb{R}^n\rightarrow\mathbb{R}$$ on $$\mathbb{R}^n$$ by the following formula:

$$\lVert v\rVert_1=\sum_{i=1}^n \lvert v_i\rvert$$

Then $$\lVert-\rVert_1$$ satisfies all the conditions for a norm. If there existed an inner product $$\langle-,-\rangle_1$$ such that $$\lVert -\rVert_1$$ could be written in the form

$$\lVert v\rVert_1=\sqrt{\langle v,v\rangle_1}$$

then by [Proposition 5](#prop5) the following formula

$$\lVert u+v\rVert_1^2+\lVert u-v\rVert_1^2=2\lVert u\rVert^2_1+2\lVert v\rVert^2_1$$

would have to hold. However, substituting $$u=(1,0,\ldots, 0)$$ and $$v=(0,1,\ldots, 0)$$, we see that the parallelogram law is not satisfied. Therefore $$\lVert -\rVert_1$$ is not induced by an inner product.

</div>

In fact, the converse of [Proposition 5](#prop5) also holds. That is, if $$\lVert-\rVert$$ satisfies the parallelogram law, then the bilinear form $$\langle-,-\rangle$$ defined by the following formula

$$\langle u,v\rangle:=\frac{1}{4}\left(\lVert u+v\rVert^2-\lVert u-v\rVert^2\right)$$

is an inner product. The proof of this is not very difficult, but one must use the fact that $$V$$ is equipped with a topological structure via the norm $$\lVert-\rVert$$. Since we will not need this result now, we omit the proof.

## Orthonormal Bases

Since we know that $$\ch\mathbb{R}=0$$, from [§Bilinear Forms, ⁋Proposition 7](/en/math/linear_algebra/bilinear_form#prop7) we know that any $$\mathbb{R}$$-inner product space $$V$$ has an orthogonal basis.

Let $$V$$ be an arbitrary $$\mathbb{R}$$-inner product space, and let $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ be a basis of $$V$$. First define

$$\hat{x}_1:=x_1$$

Then define

$$\hat{x}_k:=x_k-\sum_{i=1}^{k-1}\frac{\langle x_i,x_k\rangle}{\langle x_i,x_i\rangle}x_i$$

and one can verify that the set $$\{\hat{x}_1,\ldots, \hat{x}_n\}$$ obtained at the end of this process is an orthogonal basis. This method of obtaining an orthogonal basis from an arbitrary basis is called the *Gram-Schmidt process*. Sometimes we also want each element of the basis thus obtained to have length $$1$$, which can be achieved by dividing each vector by its own length. A basis satisfying this property is called an *orthonormal basis*. If $$\mathcal{B}=\{x_1, \ldots, x_n\}$$ is an orthonormal basis, then for any $$v\in V$$, the components $$v_i$$ of

$$v=v_1x_1+\cdots+v_nx_n$$

can be found by taking the inner product with $$x_i$$. The left-hand side becomes $$\langle v, x_i\rangle$$, and because the right-hand side gives $$\langle x_j,x_i\rangle=\delta_{ij}$$, only $$v_i\langle x_i,x_i\rangle=v_i$$ remains. That is,

$$v=\langle v, x_1\rangle x_1+\cdots+\langle v, x_n\rangle x_n$$

always holds. If $$\mathcal{B}$$ were merely an orthogonal basis, we would have had to take appropriate constant multiples when finding these coefficients.

## Orthogonal Matrices

Consider an $$\mathbb{R}$$-inner product space $$V$$. Consider a linear map $$L:V\rightarrow V$$ and its adjoint. In this case, it is customary to write the adjoint of $$L$$ as $$L^t$$ rather than $$L^\ast$$. Then since

$$\langle v,Lw\rangle=\langle L^t v, w\rangle$$

always holds, if a linear map $$L$$ preserves $$\langle-,-\rangle$$, then for any $$v,w$$,

$$\langle v,w\rangle=\langle Lv,Lw\rangle=\langle v, L^t Lw\rangle$$

holds, and therefore $$L^t L=I$$ holds. Thus we define as follows.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For any $$A\in\Mat_n(\mathbb{R})$$, if the formula

$$A^tA=AA^t=I$$

holds, then $$A$$ is called an *orthogonal matrix*.

</div>

From the rank-nullity theorem, we know that if $$A^tA=I$$ holds then $$AA^t=I$$ necessarily holds as well. Therefore, the matrix representation of any linear map preserving $$\langle-,-\rangle$$ is an orthogonal matrix.

Consider two orthonormal bases $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ and $$\mathcal{C}=\{x'_1,\ldots, x'_n\}$$ given on $$V$$. Then the $$i$$th column of the matrix $$[\id]_\mathcal{C}^\mathcal{B}$$ is the matrix representation of $$x_i$$ relative to $$\mathcal{C}$$. Now from

$$x_i=\langle x_i, x'_1\rangle x'_1+\cdots+\langle x_i, x'_n\rangle x'_n$$

we obtain

$$[\id]_\mathcal{C}^\mathcal{B}=\begin{pmatrix}\langle x_1,x'_1\rangle&\langle x_2, x'_1\rangle&\cdots&\langle x_n,x'_1\rangle\\ \langle x_1,x'_2\rangle&\langle x_2,x'_2\rangle&\cdots&\langle x_n,x'_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x_1, x'_n\rangle&\langle x_2, x'_n\rangle&\cdots&\langle x_n,x'_n\rangle\end{pmatrix}$$

Interchanging the roles of $$\mathcal{B}$$ and $$\mathcal{C}$$,

$$[\id]_\mathcal{B}^\mathcal{C}=\begin{pmatrix}\langle x'_1,x_1\rangle&\langle x'_2, x_1\rangle&\cdots&\langle x'_n,x_1\rangle\\ \langle x'_1,x_2\rangle&\langle x'_2,x_2\rangle&\cdots&\langle x'_n,x_2\rangle\\ \vdots&\vdots&\ddots&\vdots\\ \langle x'_1, x_n\rangle&\langle x'_2, x_n\rangle&\cdots&\langle x'_n,n\rangle\end{pmatrix}$$

so from the condition that $$\langle-,-\rangle$$ is symmetric, we can verify that the change-of-basis matrix between two orthonormal bases is always an orthogonal matrix. Conversely, any orthogonal matrix can always be interpreted as a change-of-basis matrix between orthonormal bases.

## Projection Theorem

Now let $$V$$ be an $$\mathbb{R}$$-inner product space, and let $$U\subseteq V$$ be its subspace. If $$U\neq \{0\}$$, then for any $$u\in U$$ with $$u\neq 0$$ we have $$\langle u,u\rangle>0$$, so in particular the restriction of the inner product $$\langle -,-\rangle$$ of $$V$$ to $$U$$ is non-degenerate, and thus defines a bilinear form on $$U$$. That this bilinear form has the properties of an inner product is almost obvious, so any subspace of an $$\mathbb{R}$$-inner product space always carries a natural $$\mathbb{R}$$-inner product space structure. Therefore, there exists an orthonormal basis $$\mathcal{B}=\{x_1,\ldots, x_k\}$$ of $$U$$. Moreover, if we choose a basis of $$V$$ containing $$\mathcal{B}$$ and run the Gram-Schmidt process starting from $$x_1,\ldots, x_k$$, we can also verify that there exists an orthonormal basis of $$V$$ containing $$\mathcal{B}$$.

Now for any $$v\in V$$, define the *projection* $$\proj_U v$$ of $$v$$ onto $$U$$ by the following formula:

$$\proj_U v=\sum_{i=1}^k \langle v, x_i\rangle x_i$$

For this definition to make sense, the above vector must be well defined independently of the choice of the orthonormal basis $$\mathcal{B}$$ of $$U$$.

<div class="proposition" markdown="1">

<ins id="lem8">**Lemma 8**</ins> In the above situation, if $$\mathcal{B}=\{x_1,\ldots, x_k\}$$ and $$\mathcal{B}'=\{x_1',\ldots, x_k'\}$$ are two orthonormal bases of $$U$$, then for any $$v\in V$$,

$$\sum_{i=1}^k \langle v, x_i\rangle x_i=\sum_{i=1}^k\langle v, x'_i\rangle x_i'$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is merely another expression of the formula

$$[v]_\mathcal{B}=[\id]^{\mathcal{B}'}_{\mathcal{B}}[v]_{\mathcal{B}'}$$

</details>

The following *projection theorem* tells us that the vector $$\proj_Uv$$ defined in this way is the element of $$U$$ closest to $$v$$.

<div class="proposition" markdown="1">

<ins id="thm9">**Theorem 9**</ins> Consider an $$\mathbb{R}$$-inner product space $$V$$ and its subspace $$U\subseteq V$$. Then for any $$v\in V$$, $$\proj_Uv$$ satisfies

$$\lVert \proj_Uv-v\rVert=\min_{w\in U}\lVert v-w\rVert$$

and moreover the only vector satisfying the above equation is $$\proj_Uv$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$u,u'\in U$$ both minimize $$\lVert v-w\rVert$$. Then by minimality we obtain

$$\lVert v-u\rVert=\lVert v-u'\rVert\leq\left\lVert v-\frac{u+u'}{2}\right\rVert$$

Therefore

$$\lVert v-u\rVert+\lVert v-u'\rVert=\lVert (v-u)+(v-u')\rVert$$

Now from the equality condition of the triangle inequality, we know that there exists a constant $$\lambda$$ satisfying

$$v-u=\lambda (v-u')$$

In particular,

$$(1-\lambda)v=u-\lambda u'\in U$$

holds. From this, either $$\lambda=1$$ or $$v\in U$$. If $$\lambda=1$$, then from $$v-u=v-u'$$ we get $$u=u'$$, and if $$v\in U$$, then the only $$w$$ minimizing $$\lVert v-w\rVert$$ is $$w=v$$, so likewise $$u=u'$$ in this case. Therefore, the vector minimizing this expression is unique.

Now we must show that $$\proj_Uv$$ actually minimizes $$\lVert v-w\rVert$$. Choose a basis $$\{x_1,\ldots, x_k\}$$ of $$U$$, and let $$\{x_1,\ldots, x_n\}$$ be an orthonormal basis of $$V$$ containing it. Then from $$v=\sum_{i=1}^n v_i x_i$$ and $$w=\sum_{i=1}^k w_i x_i$$,

$$\lVert v-w\rVert=\left\lVert\sum_{i=1}^k(v_i-w_i)x_i+\sum_{i=k+1}^n v_ix_i\right\rVert=\sum_{i=1}^k (v_i-w_i)^2+\sum_{i=k+1}^n v_i^2\geq \sum_{i=k+1}^n v_i^2$$

and equality holds when $$v_i=w_i$$ for all $$1\leq i\leq k$$. Then

$$\proj_Uv=\sum_{i=1}^k v_ix_i=\sum_{i=1}^k w_ix_i=w$$

so we obtain the desired conclusion.

</details>

Moreover, it is obvious from the definition of $$\proj_Uv$$ that $$v-\proj_Uv$$ is a vector perpendicular to $$U$$. We will make use of this fact in the next post.
