---
title: "Subspaces"
description: "A subset of a vector space is defined as a subspace if it is closed under addition and scalar multiplication. The concept of linear combinations is also discussed."
excerpt: "Subspaces of a vector space and linear combinations of vectors"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/subspaces
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Subspaces.png
    overlay_filter: 0.5

date: 2022-07-29
last_modified_at: 2022-07-29

weight: 3
translated_at: 2026-05-31T21:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T21:30:04+00:00
---
## Subspaces

Looking at [§Vector Spaces, ⁋Example 6](/en/math/linear_algebra/vector_spaces#ex6), we see that a subset of a vector space often itself forms a vector space. Let us define this as follows.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a $$\mathbb{K}$$-vector space $$V$$, a subset $$W$$ of $$V$$ is called a *subspace* of $$V$$ if the operations obtained by restricting the addition and scalar multiplication defined on $$V$$ to $$W$$ again define a $$\mathbb{K}$$-vector space on $$W$$. We denote this by $$W\leq V$$.

</div>

By definition, $$C^k(I)$$ is a subspace of $$C(I)$$, and $$C(I)$$ is a subspace of $$\Fun(I,\mathbb{R})$$.

To check whether an arbitrary subset $$W$$ of $$V$$ is a subspace using the definition directly, we would have to verify whether addition forms an abelian group, whether scalar multiplication satisfies all the conditions of [§Vector Spaces, ⁋Definition 1](/en/math/linear_algebra/vector_spaces#def1), and so on. However, since the addition and scalar multiplication on $$W$$ are inherited from $$V$$, several properties need not be checked separately.

For example, for arbitrary $$w_1,w_2\in W$$, we do not need to verify whether

$$w_1+w_2=w_2+w_1$$

holds. The two elements $$w_1,w_2$$ are elements of $$V$$ as well as elements of $$W$$, and the addition $$+$$ in $$W$$ is just the addition in $$V$$ restricted to $$W$$. Based on this, the properties we need to check are as follows.

1. We must separately check whether $$W$$ is closed under addition.
2. Similarly, we must check whether $$W$$ contains the identity element and additive inverses. Of course $$V$$ contains $$0$$ and $$-w$$, but there is no guarantee that these lie in $$W$$.
3. Also, for any scalar $$\alpha\in\mathbb{K}$$ and $$w\in W$$, we must check whether $$\alpha w\in W$$.

But we can simplify the conditions further. If $$W$$ is closed under scalar multiplication, then by [§Vector Spaces, ⁋Proposition 2](/en/math/linear_algebra/vector_spaces#prop2) and [Vector Spaces, ⁋Corollary 3](/en/math/linear_algebra/vector_spaces#cor3), the second condition can be omitted entirely. Since $$W$$ is closed under scalar multiplication, $$0w\in W$$ and $$(-1)w\in W$$ must hold, and these are $$0$$ and $$-w$$ respectively. Thus we have just proved the following proposition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a $$\mathbb{K}$$-vector space $$V$$, a nonempty subset $$W$$ of $$V$$ is a subspace of $$V$$ if and only if $$W$$ is closed under addition and scalar multiplication.

</div>

However, to show that $$W$$ is nonempty, showing that $$0\in W$$ is the easiest, so in practice there is little difference in utility between the three conditions presented earlier and the preceding proposition.

## Linear Combinations

Consider a $$\mathbb{K}$$-vector space $$V$$ and its subspace $$W$$. Since the sum of any two elements of $$W$$ is again an element of $$W$$, by induction a *finite* sum is again an element of $$W$$. More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$V$$ be a $$\mathbb{K}$$-vector space and $$W$$ be a subspace of $$V$$. For elements $$w_1,\ldots, w_n$$ of $$W$$ and scalars $$\alpha_1,\ldots,\alpha_n$$, the following finite sum

$$\sum_{i=1}^n\alpha_i w_i=\alpha_1w_1+\alpha_2w_2+\cdots+\alpha_nw_n\tag{1}$$

is an element of $$W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed by induction. The case $$n=1$$ is trivial, so we begin with $$n=2$$. In this case, by [Proposition 2](#prop2), $$\alpha_1w_1$$ and $$\alpha_2w_2$$ are each elements of $$W$$, and therefore their sum $$\alpha_1w_1+\alpha_2w_2$$ is also an element of $$W$$.

For general $$n$$, since addition in $$W$$ is associative,

$$\alpha_1w_1+\alpha_2w_2+\cdots+\alpha_nw_n=(\alpha_1w_1+\cdots\alpha_{n-1}w_{n-1})+\alpha_nw_n$$

holds. Now by the inductive hypothesis, $$\alpha_1w_1+\cdots\alpha_{n-1}w_{n-1}$$ and $$\alpha_nw_n$$ are each elements of $$W$$, and therefore their sum $$\sum_{i=1}^n\alpha_iw_i$$ is also an element of $$W$$.

</details>

Vectors of the form (1) in the above proposition are generally given the following name.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a $$\mathbb{K}$$-vector space $$V$$ and its elements $$v_1,\ldots, v_n$$, a *linear combination* of these elements is a vector of the form

$$\alpha_1v_1+\cdots+\alpha_nv_n$$

</div>

More generally, when infinitely many elements $$(v_i)_{i\in I}$$ of $$V$$ are given, their linear combination is defined as

$$\sum_{i\in I}\alpha_iv_i\qquad\text{$\alpha_i=0$ for all but finitely many $i$}$$

For example, if we view $$\mathbb{R}$$ as a $$\mathbb{Q}$$-vector space as in [§Vector Spaces, ⁋Example 4](/en/math/linear_algebra/vector_spaces#ex4), then $$0.111\ldots$$ is *not* a linear combination of the vectors

$$0.1,\quad 0.01,\quad0.001,\quad\cdots$$

Indeed, if we were to represent $$0.111\ldots$$ as the infinite sum above, all the coefficients would be nonzero. In a similar vein, let us consider the following example.

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Define the set $$\mathbb{K}[\x]$$ as

> the set of polynomials in $$\x$$ with coefficients in $$\mathbb{K}$$

That is, each element of $$\mathbb{K}[\x]$$ is of the form

$$p(\x)=\alpha_n\x^n+\alpha_{n-1}\x^{n-1}+\cdots+\alpha_1\x+\alpha_0$$

for some natural number $$n$$ and $$\alpha_i\in\mathbb{K}$$. In this case, the natural number $$\max\supp(\alpha_i)=n$$ is called the *degree* of $$p(\x)$$, and $$\alpha_n\x^n$$ is called the *leading term*. A polynomial whose leading coefficient is 1 is called a *monic polynomial*. Now suppose another element of $$\mathbb{K}[\x]$$

$$q(\x)=\beta_m\x^m+\beta_{m-1}\x^{m-1}+\cdots+\beta_1\x+\beta_0$$

is given. Then their sum is, if $$m>n$$,

$$\sum_{i=0}^na_i\x^i+\sum_{i=0}^mb_i\x^i=\sum_{i=0}^m c_i\x^i,\qquad c_i=\begin{cases}a_i+b_i&\text{if $0\leq i\leq n$}\\ b_i&\text{if $n < i\leq m$}\end{cases}$$

and in the opposite case

$$\sum_{i=0}^na_i\x^i+\sum_{i=0}^mb_i\x^i=\sum_{i=0}^m c_i'\x^i,\qquad c_i'=\begin{cases}a_i+\beta_i&\text{if $0\leq i\leq m$}\\ a_i&\text{if $m < i\leq n$}\end{cases}.$$

Also, for any scalar $$\gamma\in\mathbb{K}$$,

$$\gamma p(\x)=\gamma\alpha_n\x^n+\gamma\alpha_{n-1}\x^{n-1}+\cdots+\gamma\alpha_1\x+\alpha_0$$

It is not difficult to verify that these definitions give $$\mathbb{K}[\x]$$ the structure of a $$\mathbb{K}$$-vector space.

Now we can verify that the set $$\mathbb{K}[\x]_\text{degree\scriptsize$\leq n$}$$ of polynomials of degree at most $$n$$ is a subspace of $$\mathbb{K}[\x]$$. On the other hand, the set of polynomials of *exactly* degree $$n$$ is not a subspace because it does not contain $$0$$, but adjoining $$0$$ makes it a subspace.

</div>

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Now let $$\mathbb{K}[[\x]]$$ be the set

>of *formal power series* in $$\x$$ with coefficients in $$\mathbb{K}$$

Defining addition of vectors and scalar multiplication in the same way as in the preceding [Example 7](#ex7), $$\mathbb{K}[[\x]]$$ becomes a $$\mathbb{K}$$-vector space as well.

</div>

By definition, $$\mathbb{K}[\x]$$ is a subspace of $$\mathbb{K}[[\x]]$$. Also, all elements of $$\mathbb{K}[\x]$$ can be expressed as linear combinations of vectors in the set $$\{1,\x,\x^2,\ldots\}$$, but elements of $$\mathbb{K}[[\x]]$$ cannot.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
