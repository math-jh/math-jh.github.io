---
title: "Dimension of Vector Spaces"
description: "Although the basis of a vector space is not unique, any two bases always have the same number of elements. This post proves the lemma that finite bases have equal cardinality and the theorem of dimension."
excerpt: "Bases and Dimension of Vector Spaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/dimension
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Dimension.png
    overlay_filter: 0.5

date: 2022-07-31
last_modified_at: 2022-07-31

weight: 5
translated_at: 2026-05-31T22:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T22:00:04+00:00
---
## Dimension of Vector Spaces

From [§Basis of a Vector Space, ⁋Example 9](/en/math/linear_algebra/basis#ex9) and [§Basis of a Vector Space, ⁋Example 11](/en/math/linear_algebra/basis#ex11), we see that a basis of a vector space $$V$$ need not be unique. Yet in these examples, the number of elements in each basis is the same. This is no coincidence.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> For a $$\mathbb{K}$$-vector space $$V$$, any two bases $$\mathcal{B}_1$$, $$\mathcal{B}_2$$ of $$V$$ satisfy $$\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$$.

</div>

This theorem covers the case where $$\mathcal{B}_1$$, $$\mathcal{B}_2$$ are infinite as well. The proof proceeds in three stages.

1. First, if *some* basis of $$V$$ is infinite, then every basis of $$V$$ is infinite and of the same cardinality.
2. Hence, if some basis of $$V$$ is finite, then every basis of $$V$$ must be finite.
3. Finally, given two finite bases of $$V$$, they have the same number of elements.

Of course, we could prove this theorem now, but as with [§Basis of a Vector Space, ⁋Theorem 10](/en/math/linear_algebra/basis#thm10), doing so requires a little set-theoretic background, so we defer it to a separate post. The last stage, however, can be proved without any additional machinery.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> For a $$\mathbb{K}$$-vector space $$V$$, if $$\mathcal{B}_1$$ and $$\mathcal{B}_2$$ are both finite bases of $$V$$, then $$\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathcal{B}_1=\{x_1,x_2,\ldots, x_m\}$$ and $$\mathcal{B}_2=\{y_1,y_2,\ldots, y_n\}$$; we must show $$m=n$$. Suppose for contradiction that $$m>n$$.

Since $$x_1\in V$$, we can express $$x_1$$ as a linear combination of $$y_1$$, $$y_2$$, $$\ldots$$, $$y_n$$. Thus, by [§Basis of a Vector Space, ⁋Proposition 6](/en/math/linear_algebra/basis#prop6), the set $$\{x_1,y_1,y_2,\ldots, y_n\}$$ is linearly dependent. That is, there exist scalars $$\beta_1$$, $$\alpha_1$$, $$\alpha_2$$, $$\ldots$$, $$\alpha_n$$, not all zero, such that

$$\beta_1x_1+\alpha_1y_1+\alpha_2y_2+\cdots+\alpha_n y_n=0\tag{1}$$

holds. It is clear that $$\beta_1$$ cannot be zero: if $$\beta_1=0$$, then the above equation becomes

$$\alpha_1y_1+\alpha_2y_2+\cdots+\alpha_ny_n=0$$

which contradicts the linear independence of $$y_1$$, $$y_2$$, $$\ldots$$, $$y_n$$. Moreover, if all $$\alpha_i$$ were zero, then $$\beta_1x_1=0$$, and since $$\beta_1\neq 0$$ we would have $$x_1=0$$, making $$\{x_1, x_2, \ldots, x_m\}$$ trivially linearly dependent. Hence some $$\alpha_i$$ is nonzero. Rearranging equation (1) yields

$$y_i=\frac{\beta_1}{\alpha_i}x_1-\frac{\alpha_1}{\alpha_i}y_1-\cdots-\frac{\alpha_{i-1}}{\alpha_i}y_{i-1}-\frac{\alpha_{i+1}}{\alpha_i}y_{i+1}-\cdots-\frac{\alpha_n}{\alpha_i}y_n$$

Therefore, even if we remove $$y_i$$ from the set $$\{x_1, y_1, y_2, \ldots, y_n\}$$, the resulting set still spans $$V$$.  

On the other hand, this set is linearly independent. For any scalars $$\beta_1'$$, $$\alpha_1'$$, $$\ldots$$, $$\alpha_n'$$, if

$$\beta_1'x_1+\alpha_1'y_1+\alpha_2'y_2+\cdots+\alpha_{i-1}'y_{i-1}+\alpha_{i+1}'y_{i+1}+\cdots+\alpha_n'y_n=0$$

then by the same reasoning $$\beta_1'\neq 0$$, and therefore

$$x_1=-\frac{\alpha_1'}{\beta_1'}y_1-\frac{\alpha_2'}{\beta_1'}y_2-\cdots-\frac{\alpha_{i-1}'}{\beta_1'}y_{i-1}-\frac{\alpha_{i+1}'}{\beta_1'}y_{i+1}-\cdots-\frac{\alpha_n'}{\beta_1'}y_n$$

Substituting this into the preceding equation gives

$$0=\left(\frac{\alpha_1'\beta_1}{\alpha_i\beta_1'}+\frac{\alpha_1}{\alpha_i}\right)y_1+\cdots+\left(\frac{\alpha_{i-1}'\beta_1}{\alpha_i\beta_{i-1}'}+\frac{\alpha_{i-1}}{\alpha_i}\right)y_{i+1}+y_i+\left(\frac{\alpha_{i+1}'\beta_{i+1}}{\alpha_i\beta_{i+1}'}+\frac{\alpha_{i+1}}{\alpha_i}\right)y_{i+1}+\cdots+\left(\frac{\alpha_n'\beta_n}{\alpha_i\beta_n'}+\frac{\alpha_n}{\alpha_i}\right)y_n$$

Since the coefficient of $$y_i$$ is nonzero, this contradicts the linear independence of $$\{y_1,y_2,\ldots,y_n\}$$.

Thus we obtain a new basis $$\{x_1,y_1,y_2,\ldots,y_{i-1}, y_{i+1},\ldots, y_n\}$$ of $$V$$. Without loss of generality, suppose the removed vector was $$y_n$$; then this new basis is $$\{x_1, y_1, \ldots, y_{n-1}\}$$. Now add $$x_2$$ to this basis and consider $$\{x_2, x_1, y_1, y_2, \ldots, y_n\}$$.

If

$$\beta_2x_2+\beta_1x_1+\alpha_1y_1+\alpha_2y_2+\ldots+\alpha_{n-1}y_{n-1}=0$$

then by the same logic $$\beta_2\neq 0$$, and excluding the case $$x_2=0$$, some coefficient among $$\beta_1$$, $$\alpha_1$$, $$\ldots$$, $$\alpha_{n-1}$$ is nonzero. 

If $$\beta_1$$ is the unique nonzero coefficient, then the above equation becomes $$\beta_2x_2+\beta_1x_1=0$$, so $$\{x_1,x_2\}$$ is linearly dependent and the proof is complete.  

Otherwise, if some $$\alpha_i\neq 0$$, we repeat the same process to obtain a new basis $$\{x_2,x_1,y_1,y_2,\ldots,y_{n-2}\}$$.

Repeating this process, two possibilities arise. 

1. If the process stops at some stage,

    $$\beta_kx_k+\beta_{k-1}x_{k-1}+\cdots+\beta_1x_1=0$$
    
    then $$\{x_1,x_2,\ldots,x_m\}$$ is linearly dependent. 
2. Otherwise, after $$n$$ iterations we will have completely replaced the original basis $$\{y_1,y_2,\ldots, y_n\}$$ with the new basis $$\{x_1, x_2, \ldots, x_n\}$$. In this case, $$x_{n+1}\in V$$ can be expressed as a linear combination of $$\{x_1, x_2, \ldots, x_n\}$$, so $$\{x_1,x_2,\ldots, x_{n+1}\}$$ is linearly dependent, and hence so is $$\{x_1,x_2,\ldots, x_m\}$$. 

In either case, $$\{x_1,x_2,\ldots, x_m\}$$ is linearly dependent and therefore cannot be a basis, a contradiction.

</details>

In fact, the proof above establishes a slightly stronger statement than the original proposition:

> Let a $$\mathbb{K}$$-vector space $$V$$ have a finite basis $$\mathcal{B}$$. Then any subset of $$V$$ with more elements than $$\mathcal{B}$$ is linearly dependent.

In any case, by [Theorem 1](#thm1) all bases of $$V$$ have the same cardinality, so the following definition is well-posed.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a $$\mathbb{K}$$-vector space $$V$$, the cardinality of a basis of $$V$$ is called the *dimension* of $$V$$, denoted $$\dim V$$, or $$\dim_\mathbb{K}V$$ when we wish to emphasize $$\mathbb{K}$$. If $$\dim V$$ is finite, then $$V$$ is a *finite-dimensional* vector space; otherwise, $$V$$ is an *infinite-dimensional* vector space.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> 

1. The basis of the trivial vector space $$\{0\}$$ is $$\emptyset$$, so its dimension is $$\lvert\emptyset\rvert=0$$.
2. For any field $$\mathbb{K}$$, $$\mathbb{K}$$ itself is a 1-dimensional $$\mathbb{K}$$-vector space.
3. For any field $$\mathbb{K}$$, the Euclidean $$n$$-space $$\mathbb{K}^n$$ has dimension $$\dim \mathbb{K}^n=n$$.
4. $$\dim_\mathbb{R}\mathbb{C}=2$$. 
5. $$\mathbb{K}[\x]$$ is an infinite-dimensional vector space.

</div>

In what follows, we always assume that the vector spaces under consideration are finite-dimensional.
{: .remark}

Results for finite-dimensional vector spaces sometimes extend to the infinite-dimensional case and sometimes do not. For instance, the following proposition can be extended to infinite dimensions, but in this post we restrict ourselves to the finite-dimensional case.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and any linearly independent subset $$S$$ of $$V$$, there exists a basis $$\mathcal{B}$$ of $$V$$ containing $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$\langle S\rangle=V$$, there is nothing more to prove. Otherwise, there exists $$v\in V$$ with $$v\not\in\langle S\rangle$$. Set $$S_1=S\cup\{v\}$$. Then $$S_1$$ is linearly independent. Clearly $$v\neq 0$$, and for any linear combination of elements of $$S_1$$

$$\sum_{x\in S_1} \alpha_xx=\sum_{x\in S}\alpha_xx+\alpha_vv=0$$  

if $$\alpha_v\neq 0$$, moving $$\alpha_vv$$ to the other side and multiplying by $$-\alpha_v^{-1}$$ would express $$v$$ as a linear combination of elements of $$S$$, contradicting the choice of $$v$$. Hence $$\alpha_v=0$$, and then since the elements of $$S$$ are linearly independent, $$\alpha_x=0$$ for all $$x\in S$$. Therefore $$\alpha_x=0$$ for all $$x\in S_1$$.

If $$\langle S\rangle_1=V$$, the proof is complete; otherwise, we define $$S_2=S_1\cup\{v'\}$$ in the same manner and repeat. We must verify that $$S_2$$ is linearly independent, but since $$v'$$ was chosen from $$V\setminus\langle S\rangle_1$$, this follows by exactly the same argument as above. 

By the preceding [Lemma 3](#lem3), this process terminates in at most $$\dim V$$ steps, and upon termination we obtain the desired basis $$S_n$$.

</details>

A basis of $$V$$ is a set that is both linearly independent and spans $$V$$. The above proposition says that we can adjoin vectors to a linearly independent set so that it spans $$V$$. Conversely, given a set that spans $$V$$, we can discard redundant elements so that the remaining set is also linearly independent. The basic idea of the proof is the same as that of [Proposition 5](#prop5), but since $$S$$ may be infinite, removing elements from $$S$$ one by one does not suffice.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and a subset $$S$$ that spans $$V$$, some subset of $$S$$ is a basis of $$V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$S_0=\emptyset$$. Then $$\langle S\rangle_0=\{0\}$$. Choose an element $$x_1$$ from $$S\setminus\langle S\rangle_0$$ and set $$S_1=\{x_1\}=S_0\cup\{x_1\}$$; similarly, choose $$x_2$$ from $$S\setminus\langle S\rangle_1$$ and form $$S_2=\{x_1,x_2\}=S_1\cup \{x_2\}$$, and repeat.

The sets $$S_i$$ obtained in this way are linearly independent by construction, and as long as $$\langle S\rangle_i\neq S$$, the set $$S_{i+1}$$ has exactly one more element than $$S_i$$. Hence it suffices to show that $$S\setminus\langle S\rangle_i$$ is nonempty for all $$i < n = \dim V$$. 

Suppose $$m$$ is a natural number such that $$S\setminus\langle S\rangle_m=\emptyset$$, i.e., $$S\subseteq\langle S\rangle_m$$. By [§Basis of a Vector Space, ⁋Lemma 4](/en/math/linear_algebra/basis#lem4), taking the span preserves inclusion relations between sets, so

$$\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)$$

holds, and since $$\langle S\rangle_m$$ is already a subspace of $$V$$, [§Basis of a Vector Space, ⁋Lemma 3](/en/math/linear_algebra/basis#lem3) gives $$\span\bigl(\langle S\rangle\bigr)=\langle S\rangle_m$$. Therefore

$$V=\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)=\langle S\rangle_m$$

and so $$\langle S\rangle_m=V$$. 

</details>

Finally, we examine two slightly more general examples.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let $$V$$ and $$W$$ be $$\mathbb{K}$$-vector spaces. Their *product* $$V\times W$$ is the vector space consisting of vectors of the form $$(v,w)$$ for arbitrary $$v\in V$$, $$w\in W$$. The operations are given by

$$(v_1, w_1)+(v_2,w_2)=(v_1+v_2,w_1+w_2),\quad\alpha(v,w)=(\alpha v,\alpha w)$$

It is straightforward to verify that if $$\mathcal{B}_1$$, $$\mathcal{B}_2$$ are bases of $$V$$, $$W$$ respectively, then the subset

$$\mathcal{B}=\{(x, y)\mid x\in \mathcal{B}_1\text{ and }y\in \mathcal{B}_2\}$$

of $$V\times W$$ is a basis of $$V\times W$$. In particular, if $$V$$ and $$W$$ are both finite-dimensional, then so is $$V\times W$$, and $$\dim(V\times W)=(\dim V)+(\dim W)$$.

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Now let $$V$$ be a $$\mathbb{K}$$-vector space, and let $$W_1$$, $$W_2$$ be subspaces of $$V$$. The subspace $$W_1+W_2$$ of $$V$$ is defined as

> the smallest subspace of $$V$$ containing both $$W_1$$ and $$W_2$$.

In symbols, $$W_1+W_2=\span(W_1\cup W_2)$$. Assuming that $$W_1$$ and $$W_2$$ are both finite-dimensional,

$$\dim(W_1+W_2)=\dim W_1+\dim W_2-\dim(W_1\cap W_2)$$

holds.

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$W_1$$ and $$W_2$$ have dimensions $$m$$ and $$n$$ respectively, and let $$W_1\cap W_2$$ have dimension $$k$$. Then there exists a basis $$\mathcal{B}_0=\{x_1,\ldots, x_k\}$$ of $$W_1\cap W_2$$. Since this set is linearly independent in both $$W_1$$ and $$W_2$$, there exist bases of $$W_1$$ and $$W_2$$ respectively containing it. Let these be $$\mathcal{B}_1$$ and $$\mathcal{B}_2$$. Then we may write

$$\mathcal{B}_1=\{y_1,\ldots, y_m\},\quad \mathcal{B}_2=\{z_1,\ldots, z_n\},\qquad y_1=z_1=x_1,\ldots, y_k=z_k=x_k$$

Now the set

$$\mathcal{B}_1\cup\mathcal{B}_2=\{x_1=y_1,\ldots, x_k=y_k, \quad y_{k+1}, \ldots, y_m,\quad z_{k+1},\ldots, z_n\}$$

spans $$W_1+W_2$$. Moreover, this set is linearly independent. To show this, suppose

$$\alpha_1x_1+\cdots+\alpha_kx_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m+\gamma_{k+1}z_{k+1}+\cdots+\gamma_{n}z_n=0\tag{2}$$

For any scalars $$\beta_i$$, $$\gamma_i$$ ($$i\leq k$$) satisfying $$\alpha_i=\beta_i+\gamma_i$$, we may write

$$\beta_1y_1+\cdots+\beta_ky_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m=-\gamma_1z_1-\cdots-\gamma_kz_k-\gamma_{k+1}z_{k+1}-\cdots-\gamma_{n}z_n$$

The left-hand side lies in $$W_1$$ and the right-hand side lies in $$W_2$$, so this common vector belongs to $$W_1\cap W_2$$. Since $$\mathcal{B}_0$$ is a basis of $$W_1\cap W_2$$, we can choose suitable scalars $$\alpha_i'$$ so that

$$\beta_1y_1+\cdots+\beta_my_m=\alpha_1'x_1+\cdots+\alpha_k'x_k=-\gamma_1z_1-\cdots-\gamma_nz_n$$

In the first equation, moving the $$\alpha_i'x_i$$ terms to the left-hand side and combining with the $$\beta_iy_i$$ terms yields

$$(\beta_1-\alpha_1')y_1+\cdots+(\beta_k-\alpha_k')y_k+\beta_{k+1}y_{k+1}+\cdots+\beta_my_m=0$$

By the linear independence of $$\mathcal{B}_1$$, all coefficients vanish; in particular $$\beta_{k+1}=\cdots=\beta_m=0$$. Similarly, from the second equation $$\gamma_{k+1}=\cdots=\gamma_n=0$$. Then the only remaining terms in (2) give $$\alpha_1x_1+\cdots+\alpha_kx_k=0$$, and since $$x_1,\ldots,x_k$$ form a basis of $$W_1\cap W_2$$, they too are all zero by linear independence. Thus $$\mathcal{B}_1\cup\mathcal{B}_2$$ is a linearly independent subset spanning $$W_1+W_2$$, and therefore a basis of $$W_1+W_2$$. Consequently

$$\dim(W_1+W_2)=\lvert\mathcal{B}_1\cup\mathcal{B}_2\rvert=\lvert\mathcal{B}_1\rvert+\lvert\mathcal{B}_2\rvert-\lvert\mathcal{B}_0\rvert=\dim W_1+\dim W_2-\dim(W_1\cap W_2).$$

</details>

</div>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
