---
title: "Dimension of Vector Spaces"
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
translated_at: 2026-05-21T05:00:01+00:00
translation_source: kimi-cli
---
## Dimension of Vector Spaces

From [§Bases of Vector Spaces, ⁋Example 9](/en/math/linear_algebra/basis#ex9) and [§Bases of Vector Spaces, ⁋Example 11](/en/math/linear_algebra/basis#ex11), we see that a basis of a vector space $$V$$ need not be unique. However, looking at these examples, we can also verify that the number of elements in each basis remains the same. This is not a coincidence.

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1**</ins> For a $$\mathbb{K}$$-vector space $$V$$, if two bases $$\mathcal{B}_1$$, $$\mathcal{B}_2$$ of $$V$$ are given, then $$\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$$ holds.

</div>

This theorem also includes the case where $$\mathcal{B}_1$$, $$\mathcal{B}_2$$ are infinite. To show this, three steps are needed.

1. First, if *any* basis of $$V$$ is infinite, then all other bases must also be infinite and have the same cardinality.
2. Therefore, if any basis of $$V$$ is finite, then all other bases must also be finite.
3. Finally, if two finite bases of $$V$$ are given, then the number of elements in these two bases is the same.

Of course, there is nothing preventing us from proving this theorem now, but like [§Bases of Vector Spaces, ⁋Theorem 10](/en/math/linear_algebra/basis#thm10), proving it requires a bit of set-theoretic knowledge, so we separate it into another post. However, the last step can be proved without much background knowledge.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> For a $$\mathbb{K}$$-vector space $$V$$, if $$\mathcal{B}_1$$ and $$\mathcal{B}_2$$ are both bases of $$V$$ and finite, then $$\lvert \mathcal{B}_1\rvert=\lvert \mathcal{B}_2\rvert$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathcal{B}_1=\{x_1,x_2,\ldots, x_m\}$$, and $$\mathcal{B}_2=\{y_1,y_2,\ldots, y_n\}$$; we must show $$m=n$$. Suppose for contradiction that $$m>n$$.

First, since $$x_1\in V$$, we can express $$x_1$$ as a linear combination of $$y_1$$, $$y_2$$, $$\ldots$$, $$y_n$$. Thus, by [§Bases of Vector Spaces, ⁋Proposition 6](/en/math/linear_algebra/basis#prop6), the set $$\{x_1,y_1,y_2,\ldots, y_n\}$$ is linearly dependent. That is, there exist scalars $$\beta_1$$, $$\alpha_1$$, $$\alpha_2$$, $$\ldots$$, $$\alpha_n$$, not all zero, such that

$$\beta_1x_1+\alpha_1y_1+\alpha_2y_2+\cdots+\alpha_n y_n=0\tag{1}$$

holds. It is obvious that $$\beta_1$$ cannot be zero. If $$\beta_1=0$$, then the above equation becomes

$$\alpha_1y_1+\alpha_2y_2+\cdots+\alpha_ny_n=0$$

which contradicts the assumption that $$y_1$$, $$y_2$$, $$\ldots$$, $$y_n$$ are linearly independent. Also, if all $$\alpha_i$$ are zero, then $$\beta_1x_1=0$$, and since $$\beta_1\neq 0$$, we have $$x_1=0$$. In this case $$\{x_1, x_2, \ldots, x_m\}$$ would be trivially linearly dependent, so we may assume that some $$\alpha_i$$ is nonzero. Then we can rearrange equation (1) to obtain the equation

$$y_i=\frac{\beta_1}{\alpha_i}x_1-\frac{\alpha_1}{\alpha_i}y_1-\cdots-\frac{\alpha_{i-1}}{\alpha_i}y_{i-1}-\frac{\alpha_{i+1}}{\alpha_i}y_{i+1}-\cdots-\frac{\alpha_n}{\alpha_i}y_n$$

Therefore, even if we remove $$y_i$$ from the set $$\{x_1, y_1, y_2, \ldots, y_n\}$$, this set still spans $$V$$.  

On the other hand, this set is linearly independent. For any scalars $$\beta_1'$$, $$\alpha_1'$$, $$\ldots$$, $$\alpha_n'$$, if

$$\beta_1'x_1+\alpha_1'y_1+\alpha_2'y_2+\cdots+\alpha_{i-1}'y_{i-1}+\alpha_{i+1}'y_{i+1}+\cdots+\alpha_n'y_n=0$$

then by the same reasoning as above, $$\beta_1'\neq 0$$, and therefore

$$x_1=-\frac{\alpha_1'}{\beta_1'}y_1-\frac{\alpha_2'}{\beta_1'}y_2-\cdots-\frac{\alpha_{i-1}'}{\beta_1'}y_{i-1}-\frac{\alpha_{i+1}'}{\beta_1'}y_{i+1}-\cdots-\frac{\alpha_n'}{\beta_1'}y_n$$

substituting this into the previous equation gives

$$0=\left(\frac{\alpha_1'\beta_1}{\alpha_i\beta_1'}+\frac{\alpha_1}{\alpha_i}\right)y_1+\cdots+\left(\frac{\alpha_{i-1}'\beta_1}{\alpha_i\beta_{i-1}'}+\frac{\alpha_{i-1}}{\alpha_i}\right)y_{i+1}+y_i+\left(\frac{\alpha_{i+1}'\beta_{i+1}}{\alpha_i\beta_{i+1}'}+\frac{\alpha_{i+1}}{\alpha_i}\right)y_{i+1}+\cdots+\left(\frac{\alpha_n'\beta_n}{\alpha_i\beta_n'}+\frac{\alpha_n}{\alpha_i}\right)y_n$$

Since the coefficient of $$y_i$$ is not zero, this contradicts the assumption that $$\{y_1,y_2,\ldots,y_n\}$$ is linearly independent.

Thus we have obtained a new basis $$\{x_1,y_1,y_2,\ldots,y_{i-1}, y_{i+1},\ldots, y_n\}$$ of $$V$$. Without loss of generality, if the vector we removed was $$y_n$$, then this new basis is $$\{x_1, y_1, \ldots, y_{n-1}\}$$. Now add $$x_2$$ to this basis again and consider $$\{x_2, x_1, y_1, y_2, \ldots, y_n\}$$.

If

$$\beta_2x_2+\beta_1x_1+\alpha_1y_1+\alpha_2y_2+\ldots+\alpha_{n-1}y_{n-1}=0$$

then by the same logic as above, $$\beta_2\neq 0$$, and excluding the case $$x_2=0$$, there exists a nonzero coefficient among $$\beta_1$$, $$\alpha_1$$, $$\ldots$$, $$\alpha_{n-1}$$. 

Here, if $$\beta_1$$ is the unique nonzero coefficient, then the above equation becomes $$\beta_2x_2+\beta_1x_1=0$$, so $$\{x_1,x_2\}$$ is linearly dependent and the proof is complete.  

Otherwise, if some $$\alpha_i\neq 0$$ exists, we repeat the same process to obtain a new basis $$\{x_2,x_1,y_1,y_2,\ldots,y_{n-2}\}$$.

Repeating this process, there are two possibilities. 

1. If this process stops somewhere,

    $$\beta_kx_k+\beta_{k-1}x_{k-1}+\cdots+\beta_1x_1=0$$
    
    then this becomes $$\beta_kx_k+\beta_{k-1}x_{k-1}+\cdots+\beta_1x_1=0$$, so $$\{x_1,x_2,\ldots,x_m\}$$ is linearly dependent. 
2. Otherwise, after repeating $$n$$ times, we will completely replace the original basis $$\{y_1,y_2,\ldots, y_n\}$$ with a new basis $$\{x_1, x_2, \ldots, x_n\}$$. In this case, $$x_{n+1}\in V$$ can be expressed as a linear combination of $$\{x_1, x_2, \ldots, x_n\}$$, so $$\{x_1,x_2,\ldots, x_{n+1}\}$$ is linearly dependent, and hence so is $$\{x_1,x_2,\ldots, x_m\}$$. 

In either case, $$\{x_1,x_2,\ldots, x_m\}$$ is linearly dependent and therefore cannot be a basis, which is a contradiction.

</details>

In fact, the proof of the above proposition actually proves the following slightly stronger proposition than the original:

> Let a $$\mathbb{K}$$-vector space $$V$$ have a finite basis $$\mathcal{B}$$. Then any subset of $$V$$ having more elements than $$\mathcal{B}$$ must be linearly dependent.

Anyway, by [Theorem 1](#thm1), all bases of $$V$$ have the same size, so the following definition makes sense.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a $$\mathbb{K}$$-vector space $$V$$, the cardinality of a basis of $$V$$ is called the *dimension* of $$V$$, denoted $$\dim V$$, or $$\dim_\mathbb{K}V$$ when we need to emphasize $$\mathbb{K}$$. If $$\dim V$$ is finite, then $$V$$ is a *finite-dimensional* vector space; otherwise, $$V$$ is an *infinite-dimensional* vector space.

</div>

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> 

1. The basis of the trivial vector space $$\{0\}$$ is $$\emptyset$$, so the dimension of this space is $$\lvert\emptyset\rvert=0$$.
2. For any field $$\mathbb{K}$$, $$\mathbb{K}$$ itself is a 1-dimensional $$\mathbb{K}$$-vector space.
3. For any field $$\mathbb{K}$$, the dimension of the Euclidean $$n$$-space $$\mathbb{K}^n$$ is $$\dim \mathbb{K}^n=n$$.
4. $$\dim_\mathbb{R}\mathbb{C}=2$$. 
5. $$\mathbb{K}[\x]$$ is an infinite-dimensional vector space.

</div>

In what follows, we always assume that the vector spaces we treat are finite-dimensional.
{: .remark}

Sometimes results for finite-dimensional vector spaces also hold in infinite dimensions, and sometimes they do not. For example, the following proposition can be extended to the infinite-dimensional case, but in this post we shall restrict ourselves to the finite-dimensional case.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and any linearly independent subset $$S$$ of $$V$$, there exists a basis $$\mathcal{B}$$ of $$V$$ containing $$S$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$\langle S\rangle=V$$, there is nothing more to prove. Otherwise, there exists $$v\in V$$ with $$v\not\in\langle S\rangle$$. Now set $$S_1=S\cup\{v\}$$. Then $$S_1$$ is linearly independent. Obviously $$v\neq 0$$, and now for any linear combination of $$S_1$$

$$\sum_{x\in S_1} \alpha_xx=\sum_{x\in S}\alpha_xx+\alpha_vv=0$$  

if this equals zero, then in the case $$\alpha_v\neq 0$$, moving $$\alpha_vv$$ to the other side and multiplying by $$-\alpha_v^{-1}$$ would allow us to express $$v$$ as a linear combination of elements of $$S$$, which contradicts the choice of $$v$$. Therefore $$\alpha_v=0$$, and then since the elements of $$S$$ are linearly independent, $$\alpha_x=0$$ holds for all $$x\in S$$. Hence $$\alpha_x=0$$ holds for all $$x\in S_1$$.

Now if $$\langle S\rangle_1=V$$, the proof is again complete; otherwise, we can define $$S_2=S_1\cup\{v'\}$$ in the same way and repeat. Of course we must show that $$S_2$$ is linearly independent, but since $$v'$$ was chosen from $$V\setminus\langle S\rangle_1$$, this is possible by exactly the same logic as shown above. 

By the preceding [Lemma 3](#lem3), this process terminates in at most $$\dim V$$ steps, and when this process ends we obtain the desired basis $$S_n$$.

</details>

A basis of $$V$$ is a set that is both linearly independent and spans $$V$$. The above proposition says that we can add vectors appropriately to a linearly independent set so that it spans $$V$$. Conversely, if there is a set that spans $$V$$, we can remove some redundant elements appropriately so that the linear independence condition is also satisfied. The basic idea of the proof of this proposition is the same as that of [Proposition 5](#prop5), but since $$S$$ may be an infinite set, the proof does not work by removing elements from $$S$$ one by one.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and a subset $$S$$ that spans $$V$$, some subset of $$S$$ is a basis of $$V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$S_0=\emptyset$$. Then $$\langle S\rangle_0=\{0\}$$. Now choose an element $$x_1$$ from $$S\setminus\langle S\rangle_0$$ and set $$S_1=\{x_1\}=S_0\cup\{x_1\}$$, and similarly choose an element $$x_2$$ from $$S\setminus\langle S\rangle_1$$ and repeat the process of making $$S_2=\{x_1,x_2\}=S_1\cup \{x_2\}$$.

The sets $$S_i$$ obtained in this way are linearly independent subsets by construction, and as long as $$\langle S\rangle_i$$ is not equal to $$S$$, the number of elements in $$S_{i+1}$$ is always one more than in $$S_i$$. Therefore it suffices to show that $$S\setminus\langle S\rangle_i$$ is nonempty for all $$i < n = \dim V$$. 

Choose a natural number $$m$$ such that $$S\setminus\langle S\rangle_m=\emptyset$$. That is, $$S\subseteq\langle S\rangle_m$$. Now from [§Bases of Vector Spaces, ⁋Lemma 4](/en/math/linear_algebra/basis#lem4), taking the $$\span$$ preserves inclusion relations between sets, so

$$\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)$$

holds, and since $$\langle S\rangle_m$$ on the right-hand side is already a subspace of $$V$$, from [§Bases of Vector Spaces, ⁋Lemma 3](/en/math/linear_algebra/basis#lem3) we know that $$\span\bigl(\langle S\rangle\bigr)=\langle S\rangle_m$$. Therefore

$$V=\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)=\langle S\rangle_m$$

from $$V=\langle S\rangle\subseteq\span\bigl(\langle S\rangle_m\bigr)=\langle S\rangle_m$$ we know that $$\langle S\rangle_m=V$$. 

</details>

Finally, let us look at two slightly more general examples.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> Let two $$\mathbb{K}$$-vector spaces $$V$$, $$W$$ be given. Then their *product* $$V\times W$$ is the vector space consisting of vectors of the form $$(v,w)$$ for arbitrary $$v\in V$$, $$w\in W$$. Their operations are given by

$$(v_1, w_1)+(v_2,w_2)=(v_1+v_2,w_1+w_2),\quad\alpha(v,w)=(\alpha v,\alpha w)$$

respectively. It is not difficult to check that if $$\mathcal{B}_1$$, $$\mathcal{B}_2$$ are bases of $$V$$, $$W$$ respectively, then the subset

$$\mathcal{B}=\{(x, y)\mid x\in \mathcal{B}_1\text{ and }y\in \mathcal{B}_2\}$$

of $$V\times W$$ is a basis of $$V\times W$$. In particular, if $$V$$, $$W$$ are both finite-dimensional, then so is $$V\times W$$, and $$\dim(V\times W)$$ equals $$(\dim V)+(\dim W)$$.

</div>

<div class="example" markdown="1">

<ins id="ex8">**Example 8**</ins> Now let a $$\mathbb{K}$$-vector space $$V$$ be given, and let $$W_1$$, $$W_2$$ be two subspaces of $$V$$. Then the subspace $$W_1+W_2$$ of $$V$$ is defined as

> the smallest subspace of $$V$$ containing both subspaces $$W_1$$, $$W_2$$.

In symbols, we can write $$W_1+W_2=\span(W_1\cup W_2)$$. Now assuming that $$W_1,W_2$$ are both finite-dimensional,

$$\dim(W_1+W_2)=\dim W_1+\dim W_2-\dim(W_1\cap W_2)$$

holds.

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$W_1,W_2$$ have dimensions $$m$$, $$n$$ respectively, and let $$W_1\cap W_2$$ have dimension $$k$$. Then there exists a basis $$\mathcal{B}_0=\{x_1,\ldots, x_k\}$$ of $$W_1\cap W_2$$. Since this set is a linearly independent subset of both $$W_1$$ and $$W_2$$, there exist bases of $$W_1$$ and $$W_2$$ respectively containing this set. Let these be $$\mathcal{B}_1$$ and $$\mathcal{B}_2$$. Then

$$\mathcal{B}_1=\{y_1,\ldots, y_m\},\quad \mathcal{B}_2=\{z_1,\ldots, z_n\},\qquad y_1=z_1=x_1,\ldots, y_k=z_k=x_k$$

we may write. Now the set

$$\mathcal{B}_1\cup\mathcal{B}_2=\{x_1=y_1,\ldots, x_k=y_k, \quad y_{k+1}, \ldots, y_m,\quad z_{k+1},\ldots, z_n\}$$

spans $$W_1+W_2$$. Moreover, this set is linearly independent. To show this, suppose

$$\alpha_1x_1+\cdots+\alpha_kx_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m+\gamma_{k+1}z_{k+1}+\cdots+\gamma_{n}z_n=0\tag{2}$$

For any scalars $$\beta_i$$, $$\gamma_i$$ ($$i\leq k$$) satisfying $$\alpha_i=\beta_i+\gamma_i$$,

$$\beta_1y_1+\cdots+\beta_ky_k+\beta_{k+1}y_{k+1}+\cdots+\beta_{m}y_m=-\gamma_1z_1-\cdots-\gamma_kz_k-\gamma_{k+1}z_{k+1}-\cdots-\gamma_{n}z_n$$

writing this equation, the left-hand side is an element of $$W_1$$ and the right-hand side is an element of $$W_2$$, so this common vector is an element of $$W_1\cap W_2$$. Since $$\mathcal{B}_0$$ is a basis of $$W_1\cap W_2$$, choosing suitable scalars $$\alpha_i'$$,

$$\beta_1y_1+\cdots+\beta_my_m=\alpha_1'x_1+\cdots+\alpha_k'x_k=-\gamma_1z_1-\cdots-\gamma_nz_n$$

we can write. In the first equation, moving the $$\alpha_i'x_i$$ terms back to the left-hand side and combining with the $$\beta_iy_i$$ terms,

$$(\beta_1-\alpha_1')y_1+\cdots+(\beta_k-\alpha_k')y_k+\beta_{k+1}y_{k+1}+\cdots+\beta_my_m=0$$

we obtain zero, so by the linear independence of $$\mathcal{B}_1$$ all coefficients are zero, and in particular $$\beta_{k+1}=\cdots=\beta_m=0$$. Similarly, from the second equation $$\gamma_{k+1}=\cdots=\gamma_n=0$$, then the only remaining equation from (2) is $$\alpha_1x_1+\cdots+\alpha_kx_k=0$$, and since $$x_1,\ldots,x_k$$ form a basis of $$W_1\cap W_2$$, they are all zero again by linear independence. Thus, $$\mathcal{B}_1\cup\mathcal{B}_2$$ is a linearly independent subset spanning $$W_1+W_2$$, and therefore a basis of $$W_1+W_2$$. Now

$$\dim(W_1+W_2)=\lvert\mathcal{B}_1\cup\mathcal{B}_2\rvert=\lvert\mathcal{B}_1\rvert+\lvert\mathcal{B}_2\rvert-\lvert\mathcal{B}_0\rvert=\dim W_1+\dim W_2-\dim(W_1\cap W_2).$$

</details>

</div>

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
