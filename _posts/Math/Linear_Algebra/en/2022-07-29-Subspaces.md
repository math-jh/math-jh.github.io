---
title: "Subspaces"
description: "We define the conditions under which a subset of a vector space becomes a subspace, and show that closure under addition and scalar multiplication alone suffices to determine whether a subset is a subspace. The concept of linear combinations is also covered."
excerpt: "Subspaces of vector spaces and linear combinations of vectors"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/subspaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-07-29

weight: 3
translated_at: 2026-08-27T23:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-27T23:45:05+00:00
---
## Subspaces

As seen in [§Vector Spaces, ⁋Example 6](/en/math/linear_algebra/vector_spaces#ex6), a subset of a vector space often forms a vector space in its own right. Let us define this notion as follows.

::: Definition 1
For a $\mathbb{K}$-vector space $V$, a subset $W$ of $V$ is called a *subspace* of $V$ if the operations obtained by restricting the addition and scalar multiplication defined on $V$ to $W$ again define a $\mathbb{K}$-vector space on $W$. We denote this by $W\leq V$.
:::

By definition, $C^k(I)$ is a subspace of $C(I)$, and $C(I)$ is a subspace of $\Fun(I,\mathbb{R})$.

To check directly from the definition whether an arbitrary subset $W$ of $V$ is a subspace, we would have to verify that its addition forms an abelian group, that scalar multiplication satisfies all the conditions of [§Vector Spaces, ⁋Definition 1](/en/math/linear_algebra/vector_spaces#def1), and so on. However, since the addition and scalar multiplication on $W$ are inherited from $V$, some properties need not be checked.

For example, for arbitrary $w_1,w_2\in W$, there is no need to check whether

$$w_1+w_2=w_2+w_1$$

holds. This is because the two elements $w_1,w_2$ are elements of $V$ before they are elements of $W$, and the addition $+$ on $W$ is the restriction of the addition on $V$ to $W$. Taking this into account, the properties we do need to check are as follows.

1. We must check separately whether $W$ is closed under addition.
2. Similarly, we must check whether $W$ contains the additive identity and additive inverses. Of course $V$ contains $0$ and $-w$, but there is no guarantee that these belong to $W$.
3. Also, for an arbitrary scalar $\alpha\in\mathbb{K}$ and $w\in W$, we must check whether $\alpha w\in W$.

But the conditions can be trimmed down a bit further here. If $W$ is closed under scalar multiplication alone, then by [§Vector Spaces, ⁋Proposition 2](/en/math/linear_algebra/vector_spaces#prop2) and [§Vector Spaces, ⁋Corollary 3](/en/math/linear_algebra/vector_spaces#cor3), the second condition can be omitted entirely. Indeed, since $W$ is closed under scalar multiplication, we must have $0w\in W$ and $(-1)w\in W$, and these are precisely $0$ and $-w$, respectively. Thus we have just proved the following proposition.

::: Proposition 2
For a $\mathbb{K}$-vector space $V$, a nonempty subset $W$ of $V$ is a subspace of $V$ if and only if $W$ is closed under addition and scalar multiplication.
:::

However, since the easiest way to show that $W$ is nonempty is to show that $0\in W$, in practice there is little difference in usefulness between the three conditions presented earlier and the preceding proposition.

## Linear Combinations

Consider a $\mathbb{K}$-vector space $V$ and a subspace $W$ of it. Since the sum of any two elements of $W$ is again an element of $W$, by induction any *finite* sum is again an element of $W$. More generally, the following holds.

::: Proposition 3
Let $V$ be a $\mathbb{K}$-vector space and let $W$ be a subspace of $V$. For elements $w_1,\ldots, w_n$ of $W$ and scalars $\alpha_1,\ldots,\alpha_n$, the finite sum

$$\sum_{i=1}^n\alpha_i w_i=\alpha_1w_1+\alpha_2w_2+\cdots+\alpha_nw_n\tag{1}$$

is an element of $W$.
:::
::: Proof
We proceed by induction. The case $n=1$ gives $\alpha_1w_1\in W$ by [Proposition 2](#prop2). Now consider the case $n=2$. In this case, by [Proposition 2](#prop2), each of $\alpha_1w_1,\alpha_2w_2$ is an element of $W$, and hence their sum $\alpha_1w_1+\alpha_2w_2$ is also an element of $W$.

For a general $n$, since addition on $W$ satisfies the associative law,

$$\alpha_1w_1+\alpha_2w_2+\cdots+\alpha_nw_n=(\alpha_1w_1+\cdots+\alpha_{n-1}w_{n-1})+\alpha_nw_n$$

holds. Now by the inductive hypothesis, each of $\alpha_1w_1+\cdots+\alpha_{n-1}w_{n-1}$ and $\alpha_nw_n$ is an element of $W$, and therefore their sum $\sum_{i=1}^n\alpha_iw_i$ is also an element of $W$.
:::

In general, a vector of the form (1) in the above proposition is given the following name.

::: Definition 4
For a $\mathbb{K}$-vector space $V$ and its elements $v_1,\ldots, v_n$, a *linear combination* of them is a vector of the form

$$\alpha_1v_1+\cdots+\alpha_nv_n$$

.
:::

More generally, when infinitely many elements $(v_i)_{i\in I}$ of $V$ are given, a linear combination of them is defined as

$$\sum_{i\in I}\alpha_iv_i\qquad\text{$\alpha_i=0$ for all but finitely many $i$}$$

. For example, if we regard $\mathbb{R}$ as a $\mathbb{Q}$-vector space as in [§Vector Spaces, ⁋Example 4](/en/math/linear_algebra/vector_spaces#ex4), then $\sqrt2-1=0.4142\ldots$ is *not* a linear combination of the vectors

$$0.1,\quad 0.01,\quad0.001,\quad\cdots$$

. Following the decimal expansion, we can write $\sqrt2-1=4\cdot0.1+1\cdot0.01+4\cdot0.001+\cdots$ as an infinite sum, but since this infinite sum has infinitely many nonzero coefficients, it is not a linear combination in the sense defined above. Moreover, since all the listed vectors are rational, any finite linear combination of them is always rational, and the irrational number $\sqrt2-1$ cannot be expressed as a linear combination of them in any way. In a similar vein, let us look at the following example.

::: Example 5
Define the set $\mathbb{K}[\x]$ as

> the set of polynomials in $\x$ with coefficients in $\mathbb{K}$

. That is, each element of $\mathbb{K}[\x]$ is of the form

$$p(\x)=\alpha_n\x^n+\alpha_{n-1}\x^{n-1}+\cdots+\alpha_1\x+\alpha_0$$

for some natural number $n$ and scalars $\alpha_i\in\mathbb{K}$. If $\alpha_n\neq0$, we call $n$ the *degree* of $p(\x)$, and in this case $\alpha_n\x^n$ is called the *leading term*. The degree of the zero polynomial $0$ is either left undefined or formally regarded as $-\infty$; accordingly, when we speak of polynomials of degree at most $n$, we agree to include $0$ as well. A polynomial whose leading coefficient is 1 is called a *monic polynomial*. Now suppose another element of $\mathbb{K}[\x]$

$$q(\x)=\beta_m\x^m+\beta_{m-1}\x^{m-1}+\cdots+\beta_1\x+\beta_0$$

is given. Then their sum is defined, if $m>n$, by

$$\sum_{i=0}^n\alpha_i\x^i+\sum_{i=0}^m\beta_i\x^i=\sum_{i=0}^m \gamma_i\x^i,\qquad \gamma_i=\begin{cases}\alpha_i+\beta_i&\text{if $0\leq i\leq n$}\\ \beta_i&\text{if $n < i\leq m$}\end{cases}$$

and in the opposite case by

$$\sum_{i=0}^n\alpha_i\x^i+\sum_{i=0}^m\beta_i\x^i=\sum_{i=0}^n \gamma_i'\x^i,\qquad \gamma_i'=\begin{cases}\alpha_i+\beta_i&\text{if $0\leq i\leq m$}\\ \alpha_i&\text{if $m < i\leq n$}\end{cases}$$

, and for an arbitrary scalar $\gamma\in\mathbb{K}$, scalar multiplication is defined by

$$\gamma p(\x)=\gamma\alpha_n\x^n+\gamma\alpha_{n-1}\x^{n-1}+\cdots+\gamma\alpha_1\x+\gamma\alpha_0$$

. It is not difficult to verify that these definitions endow $\mathbb{K}[\x]$ with the structure of a $\mathbb{K}$-vector space.

Now we can check that the set $$\mathbb{K}[\x]_\text{degree\scriptsize$\leq n$}$$ of polynomials of degree at most $n$ is a subspace of $\mathbb{K}[\x]$. On the other hand, the set of polynomials of *exactly* degree $n$ is not a subspace since it does not contain $0$, and when $n\geq1$, even after adjoining $0$ it is still not a subspace because it is not closed under addition, as the sum of $\x^n$ and $1-\x^n$ shows.
:::

::: Example 6
This time, let the set $\mathbb{K}[[\x]]$ be

> the set of *formal power series* in $\x$ with coefficients in $\mathbb{K}$

. If we define addition and scalar multiplication in exactly the same way as in the preceding [Example 5](#ex5), then $\mathbb{K}[[\x]]$ likewise becomes a $\mathbb{K}$-vector space.
:::

By definition, $\mathbb{K}[\x]$ is a subspace of $\mathbb{K}[[\x]]$. Also, every element of $\mathbb{K}[\x]$ can be expressed as a linear combination of vectors from the set $\{1,\x,\x^2,\ldots\}$, but $\mathbb{K}[[\x]]$ has elements that cannot be expressed in that way.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
