---
title: "Vector Spaces"
description: "A vector space is a generalization of coordinate space, consisting of an abelian group equipped with scalar multiplication. This post summarizes the basic properties and notational conventions, and proves additional properties derived from scalar multiplication."
excerpt: "Definition, basic properties, and examples of vector spaces"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/vector_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-07-28

weight: 2
translated_at: 2026-08-27T23:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-27T23:15:05+00:00
---
As mentioned at the beginning of the previous post, the *vector space*, the space studied in linear algebra, is a concept generalizing the coordinate space we learn in high school. To this end, we defined abelian groups and fields in the previous post.

Many linear algebra textbooks avoid these definitions and consider only $\mathbb{R}$-vector spaces or $\mathbb{C}$-vector spaces, but since the general case is not at all more complicated, there is no need to restrict our attention to special cases.

## Definition of a Vector Space

::: Definition 1
Let $\mathbb{K}$ be a field and $V$ an abelian group. We say that $V$ is a *vector space over $\mathbb{K}$*, or simply a *$\mathbb{K}$-vector space*, if it carries an additional operation (*scalar multiplication*) $\cdot:\mathbb{K}\times V\rightarrow V$ satisfying all of the following:

1. for all $\alpha,\beta\in\mathbb{K}$ and all $u\in V$, we have $\alpha\cdot(\beta\cdot u)=(\alpha\beta)\cdot u$;
2. for all $\alpha\in\mathbb{K}$ and all $u,v\in V$, we have $\alpha\cdot(u+_{\tiny V}v)=(\alpha\cdot u)+_{\tiny V}(\alpha\cdot v)$;
3. for all $\alpha,\beta\in\mathbb{K}$ and all $u\in V$, we have $(\alpha+_{\tiny \mathbb{K}}\beta)\cdot u=(\alpha\cdot u)+_{\tiny V}(\beta\cdot u)$;
4. for the multiplicative identity $1\in\mathbb{K}$ of $\mathbb{K}$, we have $1\cdot u=u$ for all $u\in V$.

In this case, the elements of $V$ are called *vectors*.
:::

As in the definition above, from now on we will write elements of the field $\mathbb{K}$ as $\alpha,\beta,\ldots$ and elements of a $\mathbb{K}$-vector space as $u,v,\ldots$, to avoid confusion. In the definition above, we wrote $+_{\tiny V}$ and $+_{\tiny \mathbb{K}}$ separately, but under the convention we just adopted it is always clear whether the elements surrounding a $+$ belong to $\mathbb{K}$ or to $V$, so there is no risk of confusion even if we write both simply as $+$.

Likewise, we will write scalar multiplication as $\alpha u$ instead of $\alpha\cdot u$. The only worry in this case is that when we write $\alpha\beta u$, one might be unsure whether it means $(\alpha\beta)u$ or $\alpha(\beta u)$; but by the first condition of the definition above, both choices give the same value, so there is nothing to worry about.

A vector space is an abelian group $V$ equipped with the additional structure of $\mathbb{K}$-scalar multiplication. Therefore $V$ enjoys all the properties that abelian groups have. ([§Abelian Groups and Fields, ⁋Proposition 2](/en/math/linear_algebra/fields#prop2) and [§Abelian Groups and Fields, ⁋Corollary 3](/en/math/linear_algebra/fields#cor3))

The following are additional properties determined by the $\mathbb{K}$-scalar multiplication.

::: Proposition 2
Let $V$ be a $\mathbb{K}$-vector space. Then

1. for every $\alpha\in\mathbb{K}$, we have $\alpha0=0$, and
2. for every $v\in V$, we have $0v=0$.

Conversely, if $\alpha v=0$, then either $\alpha=0$ or $v=0$.
:::
::: Proof
The first two claims proceed similarly to [§Abelian Groups and Fields, ⁋Proposition 6](/en/math/linear_algebra/fields#prop6). For example, since

$$\alpha0+\alpha0=\alpha(0+0)=\alpha0$$

we have $\alpha0=0$, and similarly, since

$$0v+0v=(0+0)v=0v$$

we have $0v=0$. Finally, suppose that $\alpha v=0$ and $\alpha\neq 0$. Then there exists $\alpha^{-1}\in\mathbb{K}$ with $\alpha\alpha^{-1}=1$, and hence

$$v=1v=(\alpha^{-1}\alpha)v=\alpha^{-1}(\alpha v)=\alpha^{-1}0=0$$

so $v=0$, and the proposition follows.
:::

The $0$ appearing in part 1 of the proposition above and the $0$ on the right-hand side of part 2 are both elements of $V$, while the $0$ on the left-hand side of part 2 is an element of $\mathbb{K}$. To be rigorous, we should distinguish these as $0_{\tiny V}$ and $0_{\tiny \mathbb{K}}$, but since they can be clearly told apart from the context, we write them all simply as $0$.

::: Corollary 3
For every element $v$ of a $\mathbb{K}$-vector space $V$, we always have $(-1)v=-v$.
:::
::: Proof
This is immediate from the identity

$$(-1)v+v=(-1)v+1v=((-1)+1)v=0v=0$$

together with the uniqueness of additive inverses in $V$.
:::

## Examples of Vector Spaces

Let us now look at a few examples of vector spaces.

::: Example 4
The simplest example of a vector space is $\{0\}$. There is only one way to give this set an addition structure (namely $0+0=0$), and under this structure the set is an abelian group. Moreover, no matter which field $\mathbb{K}$ we take, there is also only one way to define scalar multiplication on this set (namely $\alpha 0=0$), and the scalar multiplication so defined makes $\{0\}$ into a $\mathbb{K}$-vector space. This is called the *trivial space*.

A slightly less trivial example is a field itself. For any field $\mathbb{K}$, $\mathbb{K}$ is a $\mathbb{K}$-vector space. Since $\mathbb{K}$ is a field, it is trivially an abelian group under addition. It suffices to give it a scalar multiplication structure, which we can do simply by taking multiplication in $\mathbb{K}$, $\mathbb{K}\times \mathbb{K}\rightarrow \mathbb{K}$. With this definition, one can check that scalar multiplication satisfies all the conditions of [Definition 1](#def1), and therefore $\mathbb{K}$ is a $\mathbb{K}$-vector space in its own right.

More generally, suppose that $\mathbb{K}$ is a field and that there is another field $\mathbb{K}'$ which contains $\mathbb{K}$ as a subset and whose operations, restricted to $\mathbb{K}$, agree with the operations of $\mathbb{K}$. (Such a $\mathbb{K}'$ is called an *extension* of $\mathbb{K}$.) Then $\mathbb{K}'$ is a $\mathbb{K}$-vector space. Since $\mathbb{K}'$ is a field, it forms an abelian group under addition as before, and scalar multiplication by an element $\alpha\in\mathbb{K}$ can be defined by treating $\alpha$ as an element of $\mathbb{K}'$ and using the multiplication structure of $\mathbb{K}'$. For example, $\mathbb{C}$ is an $\mathbb{R}$-vector space, and $\mathbb{R}$ is a $\mathbb{Q}$-vector space.
:::

::: Example 5
This time, suppose a field $\mathbb{K}$ is given. Then the *Euclidean $n$-space* is the $\mathbb{K}$-vector space consisting of the $n$-tuples

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix},\qquad a_i\in\mathbb{K}\text{ for all $i$}$$

Addition and scalar multiplication among them are defined respectively by

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}+\begin{pmatrix}b_1\\b_2\\\vdots\\b_n\end{pmatrix}=\begin{pmatrix}a_1+b_1\\a_2+b_2\\\vdots\\a_n+b_n\end{pmatrix},\qquad \alpha\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}=\begin{pmatrix}\alpha a_1\\\alpha a_2\\\vdots\\\alpha a_n\end{pmatrix}$$

We write this vector space as $\mathbb{K}^n$. When $\mathbb{K}=\mathbb{R}$ and $n=2,3$, this definition recovers the coordinate plane and the coordinate space that we know well.
:::

Euclidean space is an object we will deal with especially often. In the example above, instead of the notation $(a_1, a_2, \ldots, a_n)$ for ordered tuples, we used a column notation, which is closely related to the fundamental theorem of linear algebra.

But no matter how plausible the reason, it would be foolish to insist on the notation $\begin{pmatrix}a_1\\a_2\\ \vdots\\a_n\end{pmatrix}$ in the main text. Therefore, in the text we will use a notation such as $(a_1\quad a_2\quad \cdots\quad a_n)^t$, or, following the high school convention, write $(a_1,a_2,\ldots, a_n)$.

The two vector spaces we examined above are fairly concrete examples. As the next example shows, in general a vector space need not be visually representable like the coordinate plane or coordinate space.

::: Example 6
Let $I$ be an interval, and consider the collection $\Fun(I,\mathbb{R})$ of functions from $I$ to $\mathbb{R}$. Now define addition and scalar multiplication on this set by the formulas

$$f+g:t\mapsto f(t)+g(t),\qquad \alpha f:t\mapsto \alpha f(t)$$

Then one can verify that $\Fun(I,\mathbb{R})$ has the structure of a vector space. That is, $f+g$ is defined as the function sending each $t\in I$ to the value $f(t)+g(t)$, and $\alpha f$ is defined as the function sending each $t\in I$ to $\alpha f(t)$.

Moreover, various subsets of $\Fun(I,\mathbb{R})$ are also $\mathbb{R}$-vector spaces. For example, the collection $C(I)$ of continuous functions from $I$ to $\mathbb{R}$ is also an $\mathbb{R}$-vector space, and more generally one can check that the collection $C^k(I)$ of functions whose $k$-th derivative is continuous is also an $\mathbb{R}$-vector space.
:::

If we think of $\Fun(I,\mathbb{R})$ as the product set $\mathbb{R}^I$, [Example 6](#ex6) can also be regarded as a natural generalization of [Example 5](#ex5). ([\[Set Theory\] §Product of Sets, ⁋Definition 1](/en/math/set_theory/product_of_sets#def1))

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
