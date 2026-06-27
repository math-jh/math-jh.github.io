---
title: "Quadratic Forms and Sylvester's Law of Inertia"
description: "We define quadratic forms from symmetric bilinear forms and show that over the real numbers, a suitable choice of basis reduces them to diagonal form. We then prove Sylvester's law of inertia, which asserts that the signature is independent of the choice of basis."
excerpt: "Classification of real symmetric bilinear forms"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/quadratic_forms
sidebar: 
    nav: "linear_algebra-en"


date: 2026-06-28

weight: 125
translated_at: 2026-06-27T21:00:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-27T21:00:03+00:00
---
What we have examined so far are various theorems derived from the inner product, through which we have confirmed that the inner product, and more generally bilinear forms, are useful. Now we change direction slightly and investigate how a symmetric bilinear form can be expressed in a simple form with respect to an appropriate basis when $$\mathbb{K}=\mathbb{R}$$. Throughout this post, all bilinear forms are assumed to be symmetric.

## Quadratic Forms

A symmetric bilinear form takes two vectors as input, but if we put the same vector in both inputs, we obtain a function of a single vector.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a symmetric bilinear form $$\langle -,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$, the function $$Q:V\rightarrow\mathbb{R}$$ defined by the formula

$$Q(v)=\langle v,v\rangle$$

is called the *quadratic form* corresponding to $$\langle-,-\rangle$$.

</div>

A quadratic form contains all the information of the original bilinear form. For any $$v,w\in V$$,

$$Q(v+w)=\langle v+w,v+w\rangle=\langle v,v\rangle+2\langle v,w\rangle+\langle w,w\rangle=Q(v)+2\langle v,w\rangle+Q(w)$$

and therefore the formula

$$\langle v,w\rangle=\frac{1}{2}\bigl(Q(v+w)-Q(v)-Q(w)\bigr)\tag{1}$$

holds. This formula is called the *polarization identity*. Thus over $$\mathbb{R}$$, a symmetric bilinear form and a quadratic form uniquely determine each other, and since we can freely move between the two, they are essentially the same thing. The fact that formula (1) holds essentially uses the fact that we can divide by $$2$$, i.e., that $$\ch\mathbb{R}\neq 2$$, which was already the situation in [§Bilinear Forms, ⁋Proposition 7](/en/math/linear_algebra/bilinear_form#prop7).

## Congruence and Diagonal Form

Suppose a symmetric bilinear form $$\langle -,-\rangle$$ is given on $$V$$, and choose a basis $$\mathcal{B}$$ of $$V$$. Then as seen in [§Bilinear Forms, §§Gram Matrix](/en/math/linear_algebra/bilinear_form#gram-matrix), for the Gram matrix $$G_\mathcal{B}$$ whose $$(i,j)$$ entry is $$\langle x_i,x_j\rangle$$, we have $$\langle v,w\rangle=[v]_\mathcal{B}^tG_\mathcal{B}[w]_\mathcal{B}$$, and since $$\langle-,-\rangle$$ is symmetric, $$G_\mathcal{B}$$ is a symmetric matrix. If we choose another basis $$\mathcal{C}$$, then for the change-of-basis matrix $$P=[\id]_\mathcal{C}^\mathcal{B}$$ we have seen that

$$G_\mathcal{C}=P^tG_\mathcal{B}P$$

holds. Two symmetric matrices $$G,G'$$ related by $$G'=P^tGP$$ for some invertible matrix $$P$$ are said to be *congruent*. That is, Gram matrices of the same bilinear form written with respect to different bases are congruent to each other. Our goal is to find the simplest representative among congruent matrices.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For any symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$, there exists an appropriate basis $$\{e_1,\ldots, e_n\}$$ of $$V$$ such that $$\langle e_i,e_j\rangle=0$$ when $$i\neq j$$, and each $$\langle e_i,e_i\rangle$$ is one of $$1$$, $$-1$$, or $$0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First we show the existence of an orthogonal basis by induction on $$\dim V$$. If $$\dim V=0$$ or if $$\langle-,-\rangle$$ is identically $$0$$, then any basis of $$V$$ satisfies the condition, so there is nothing to show. Otherwise, there exist $$u,v$$ with $$\langle u,v\rangle\neq 0$$, and from

$$2\langle u,v\rangle=\langle u+v,u+v\rangle-\langle u,u\rangle-\langle v,v\rangle$$

the left-hand side is nonzero, so at least one of the three terms on the right-hand side is nonzero. Thus there exists $$w\in V$$ with $$\langle w,w\rangle\neq 0$$. Now let $$W=\span w$$; then from $$\langle w,w\rangle\neq 0$$ we can write any $$v\in V$$ as

$$v=\frac{\langle v,w\rangle}{\langle w,w\rangle}w+\left(v-\frac{\langle v,w\rangle}{\langle w,w\rangle}w\right)$$

and see that $$V=W\oplus w^\perp$$. (This is the same as the proof of [§Bilinear Forms, ⁋Proposition 7](/en/math/linear_algebra/bilinear_form#prop7).) Here $$w^\perp=\{v\mid\langle v,w\rangle=0\}$$. The bilinear form restricted to $$w^\perp$$ is also symmetric, so by the inductive hypothesis there exists an orthogonal basis of $$w^\perp$$, and adding $$w$$ to it gives an orthogonal basis $$\{f_1,\ldots,f_n\}$$ of $$V$$.

Now we scale each $$f_i$$ appropriately so that $$\langle f_i,f_i\rangle$$ becomes one of $$1$$, $$-1$$, or $$0$$. If $$\langle f_i,f_i\rangle=0$$, set $$e_i=f_i$$; otherwise, for $$c=\sqrt{\lvert\langle f_i,f_i\rangle\rvert}$$ set $$e_i=f_i/c$$, then

$$\langle e_i,e_i\rangle=\frac{\langle f_i,f_i\rangle}{\lvert\langle f_i,f_i\rangle\rvert}=\pm 1$$

holds. Scalar multiplication preserves orthogonality, so $$\{e_1,\ldots,e_n\}$$ is a basis satisfying all the desired conditions.

</details>

The Gram matrix with respect to the basis of [Proposition 2](#prop2) is a diagonal matrix with diagonal entries $$1$$, $$-1$$, or $$0$$. By reordering the basis appropriately, we can make this diagonal matrix into the form with $$p$$ copies of $$1$$, $$q$$ copies of $$-1$$, and $$r$$ copies of $$0$$:

$$\begin{pmatrix}I_p&&\\&-I_q&\\&&0_r\end{pmatrix}$$

Therefore any real symmetric matrix is congruent to a matrix of this form. In this case, the quadratic form is expressed in terms of the coordinates $$v=\sum a_ie_i$$ with respect to this basis as

$$Q(v)=a_1^2+\cdots+a_p^2-a_{p+1}^2-\cdots-a_{p+q}^2$$

## Sylvester's Law of Inertia

[Proposition 2](#prop2) shows that by choosing an appropriate basis, a quadratic form can be reduced to a sum of signed squares, but it is not yet clear whether the numbers $$p,q,r$$ appearing in this process can vary depending on the choice of basis. The following theorem shows that these three numbers are actually invariants of the bilinear form itself.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3 (Sylvester's Law of Inertia)**</ins> For a symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$, the numbers $$p$$, $$q$$, and $$r$$ counting how many of the values $$\langle e_i,e_i\rangle$$ are $$1$$, $$-1$$, and $$0$$ respectively in a basis as in [Proposition 2](#prop2) are determined independently of the choice of basis.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let the basis of [Proposition 2](#prop2) be $$\{e_1,\ldots, e_n\}$$, and suppose it has been reordered so that there are $$p$$ copies of $$+1$$, $$q$$ copies of $$-1$$, and $$r$$ copies of $$0$$. The rank of a Gram matrix is invariant under congruence (since if $$P$$ is invertible, $$\rank(P^tGP)=\rank G$$), and the rank in this basis is $$p+q$$, so $$p+q$$ is independent of the choice of basis. Therefore $$r=n-(p+q)$$ is also independent. Now if we show that $$p$$ is invariant, then $$q$$ follows as well.

We show that $$p$$ can be characterized by the formula

$$p=\max\{\dim U\mid U\leq V,\ Q(v)>0\text{ for all nonzero }v\in U\}$$

Since the right-hand side is manifestly independent of the basis by definition, it suffices to show this.

First, consider $$U_+=\span\{e_1,\ldots, e_p\}$$; then for any $$0\neq v=\sum_{i=1}^p a_ie_i\in U_+$$,

$$Q(v)=\sum_{i=1}^p a_i^2>0$$

so $$Q$$ is positive definite on a subspace of dimension $$p$$. Thus the maximum above is at least $$p$$. Conversely, consider any subspace $$U$$ on which $$Q$$ is positive definite, and let $$U_-=\span\{e_{p+1},\ldots, e_n\}$$. For any $$v=\sum_{i=p+1}^n a_ie_i\in U_-$$,

$$Q(v)=-\sum_{i=p+1}^{p+q}a_i^2\leq 0$$

so if there existed $$0\neq v\in U\cap U_-$$, then $$Q(v)>0$$ and $$Q(v)\leq 0$$ would hold simultaneously, a contradiction. Therefore $$U\cap U_-=\{0\}$$, and by [§Dimension of Vector Spaces, ⁋Example 8](/en/math/linear_algebra/dimension#ex8),

$$\dim U+\dim U_-=\dim(U+U_-)\leq n$$

Since $$\dim U_-=n-p$$, we have $$\dim U\leq p$$. Thus the maximum is $$p$$, and this shows that $$p$$ is independent of the basis.

</details>

This makes the following definition meaningful.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$, the three numbers $$(p,q,r)$$ determined by [Theorem 3](#thm3) are called the *signature* of $$\langle-,-\rangle$$.

</div>

In the signature, $$p+q$$ is the rank of the Gram matrix, and $$r$$ is the degree of degeneracy of $$\langle-,-\rangle$$, i.e., the dimension of the subspace consisting of vectors orthogonal to all vectors. In particular, $$\langle-,-\rangle$$ being non-degenerate is equivalent to $$r=0$$.

Sylvester's law immediately gives a complete classification of real symmetric matrices up to congruence.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Two real symmetric matrices are congruent if and only if the bilinear forms they define have the same signature.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If two matrices $$G,G'$$ are congruent, then they are the same bilinear form written with respect to different bases, so their signatures are the same. Conversely, if the signature is $$(p,q,r)$$ for both, then by [Proposition 2](#prop2) both $$G$$ and $$G'$$ are congruent to the same diagonal matrix with $$p$$ copies of $$1$$, $$q$$ copies of $$-1$$, and $$r$$ copies of $$0$$, and since congruence is an equivalence relation, $$G$$ and $$G'$$ are congruent to each other.

</details>

## Positive Definiteness

The case where the signature is $$(n,0,0)$$, i.e., where $$\langle v,v\rangle>0$$ for all $$0\neq v\in V$$, is particularly important. This is the same as the Gram matrix being positive definite in the sense of [§Spectral Theorem, ⁋Definition 8](/en/math/linear_algebra/spectral_theorem#def8), and in this case we call $$\langle-,-\rangle$$ itself positive definite.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For a symmetric bilinear form $$\langle-,-\rangle$$ defined on an $$\mathbb{R}$$-vector space $$V$$, the following are all equivalent:

1. $$\langle-,-\rangle$$ is positive definite.
2. The signature of $$\langle-,-\rangle$$ is $$(n,0,0)$$.
3. $$\langle-,-\rangle$$ is an inner product on $$V$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For the basis $$\{e_1,\ldots, e_n\}$$ of [Proposition 2](#prop2), if $$v=\sum a_ie_i$$ then $$Q(v)=\sum_i\langle e_i,e_i\rangle a_i^2$$. If some $$\langle e_i,e_i\rangle$$ is $$-1$$ or $$0$$, then for $$v=e_i$$ we have $$Q(e_i)\leq 0$$, so it is not positive definite. Conversely, if all $$\langle e_i,e_i\rangle$$ are $$1$$, i.e., the signature is $$(n,0,0)$$, then for any $$0\neq v$$ we have $$Q(v)=\sum a_i^2>0$$. Thus 1 and 2 are equivalent.

On the other hand, the definition of an inner product is a symmetric bilinear form such that $$\langle v,v\rangle\geq 0$$ for all $$v$$ and equality holds only when $$v=0$$ ([§Inner Product Spaces, ⁋Definition 1](/en/math/linear_algebra/inner_product_spaces#def1)), which is exactly the condition of being positive definite. Thus 1 and 3 are equivalent.

</details>

That is, an inner product is nothing but a symmetric bilinear form with signature $$(n,0,0)$$, and from the perspective of Sylvester's law, an inner product space corresponds to the most special point among all possible signatures.

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.  
**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
