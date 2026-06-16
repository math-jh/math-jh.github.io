---
title: "Vector Spaces"
description: "A vector space generalizes the notion of coordinate space by adding scalar multiplication to an abelian group. This post covers fundamental properties and notation conventions, then proves additional properties derived from scalar multiplication."
excerpt: "The definition of vector spaces, simple properties, and examples"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/vector_spaces
sidebar: 
    nav: "linear_algebra-en"


date: 2022-07-28

weight: 2
translated_at: 2026-05-31T21:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T21:00:05+00:00
---
As we mentioned in the introduction to the previous post, the *vector space* is the central object of study in linear algebra, generalizing the coordinate spaces learned in high school. To prepare for this, we defined abelian groups and fields in the last post.

Many linear algebra textbooks avoid these definitions and consider only $$\mathbb{R}$$-vector spaces or $$\mathbb{C}$$-vector spaces, but the more general case is not at all more complicated, so there is no need to restrict our attention to special cases.

## Definition of Vector Spaces

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$\mathbb{K}$$ be a field and $$V$$ an abelian group. We say that $$V$$ is a *vector space over $$\mathbb{K}$$*, or simply a *$$\mathbb{K}$$-vector space*, if there is an additional operation (*scalar multiplication*) $$\cdot:\mathbb{K}\times V\rightarrow V$$ satisfying

1. $$\alpha\cdot(\beta\cdot u)=(\alpha\beta)\cdot u$$ for any $$\alpha,\beta\in\mathbb{K}$$ and any $$u\in V$$.
2. $$\alpha\cdot(u+_{\tiny V}v)=(\alpha\cdot u)+_{\tiny V}(\alpha\cdot v)$$ for any $$\alpha\in\mathbb{K}$$ and any $$u,v\in V$$.
3. $$(\alpha+_{\tiny \mathbb{K}}\beta)\cdot u=(\alpha\cdot u)+_{\tiny V}(\beta\cdot u)$$ for any $$\alpha,\beta\in\mathbb{K}$$ and any $$u\in V$$.
4. $$1\cdot u=u$$ for any $$u\in V$$, where $$1\in\mathbb{K}$$ is the multiplicative identity.

The elements of $$V$$ are called *vectors*.

</div>

As in the definition above, to avoid confusion we will write elements of the field $$\mathbb{K}$$ as $$\alpha,\beta,\ldots$$ and elements of a $$\mathbb{K}$$-vector space as $$u,v,\ldots$$. In the definition we distinguished $$+_{\tiny V}$$ and $$+_{\tiny \mathbb{K}}$$, but with this notation the elements around $$+$$ make it clear whether they belong to $$\mathbb{K}$$ or $$V$$, so we may simply write $$+$$ without risk of confusion.

Similarly, we will write $$\alpha u$$ instead of $$\alpha\cdot u$$. The only concern is that $$\alpha\beta u$$ could be read as either $$(\alpha\beta)u$$ or $$\alpha(\beta u)$$, but by the first condition of the definition both choices yield the same value, so this is not a problem.

A vector space is an abelian group $$V$$ equipped with the additional structure of $$\mathbb{K}$$-scalar multiplication. Therefore $$V$$ possesses all the properties of an abelian group. ([§Abelian Groups and Fields, ⁋Proposition 2](/en/math/linear_algebra/fields#prop2) and [§Abelian Groups and Fields, ⁋Corollary 3](/en/math/linear_algebra/fields#cor3))

The following properties are additional ones determined by the $$\mathbb{K}$$-scalar multiplication.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$V$$ be a $$\mathbb{K}$$-vector space. Then

1. $$\alpha 0=0$$ for any $$\alpha\in\mathbb{K}$$, and
2. $$0v=0$$ for any $$v\in V$$.

Conversely, if $$\alpha v=0$$, then either $$\alpha=0$$ or $$v=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first two claims proceed similarly to [§Abelian Groups and Fields, ⁋Proposition 6](/en/math/linear_algebra/fields#prop6). For example,

$$\alpha0+\alpha0=\alpha(0+0)=\alpha0$$

so $$\alpha0=0$$, and similarly

$$0v+0v=(0+0)v=0v$$

so $$0v=0$$. Finally, suppose $$\alpha v=0$$ and $$\alpha\neq 0$$. Then $$\alpha^{-1}\in\mathbb{K}$$ exists with $$\alpha\alpha^{-1}=1$$, and thus

$$v=1v=(\alpha^{-1}\alpha)v=\alpha^{-1}(\alpha v)=\alpha^{-1}0=0$$

so $$v=0$$, and the proposition follows.

</details>

The $$0$$ appearing in part 1 of the proposition and on the right-hand side of part 2 are elements of $$V$$, while the $$0$$ on the left-hand side of part 2 is an element of $$\mathbb{K}$$. Strictly speaking these should be distinguished as $$0_{\tiny V}$$ and $$0_{\tiny \mathbb{K}}$$, but context makes the distinction clear, so we write them all as $$0$$.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> For any element $$v$$ of a $$\mathbb{K}$$-vector space $$V$$, $$(-1)v=-v$$ always holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This follows immediately from the equation

$$(-1)v+v=(-1)v+1v=((-1)+1)v=0v=0$$

and the uniqueness of additive inverses in $$V$$.

</details>

## Examples of Vector Spaces

Let us now look at some examples of vector spaces.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The simplest example of a vector space is $$\{0\}$$. There is only one way to give this set an addition structure (namely $$0+0=0$$), and with this structure the set is an abelian group. Moreover, for any field $$\mathbb{K}$$ there is also only one way to define scalar multiplication on this set (namely $$\alpha 0=0$$), and this scalar multiplication makes $$\{0\}$$ a $$\mathbb{K}$$-vector space. We call this the *trivial space*.

A slightly less trivial example is the field itself. For any field $$\mathbb{K}$$, $$\mathbb{K}$$ is a $$\mathbb{K}$$-vector space. Since $$\mathbb{K}$$ is a field, it is trivially an abelian group under addition. We only need to give it a scalar multiplication structure, which is simply multiplication in $$\mathbb{K}$$, i.e. $$\mathbb{K}\times \mathbb{K}\rightarrow \mathbb{K}$$. One can verify that this scalar multiplication satisfies all the conditions of [Definition 1](#def1), and thus $$\mathbb{K}$$ is a $$\mathbb{K}$$-vector space in its own right.

More generally, let $$\mathbb{K}$$ be a field and suppose there is another field $$\mathbb{K}'$$ with $$\mathbb{K}'\supseteq \mathbb{K}$$. Then $$\mathbb{K}'$$ is a $$\mathbb{K}$$-vector space. Since $$\mathbb{K}'$$ is a field, it is an abelian group under addition as before, and scalar multiplication by an element $$\alpha\in\mathbb{K}$$ is given by viewing $$\alpha$$ as an element of $$\mathbb{K}'$$ and using the multiplication in $$\mathbb{K}'$$. For example, $$\mathbb{C}$$ is an $$\mathbb{R}$$-vector space, and $$\mathbb{R}$$ is a $$\mathbb{Q}$$-vector space.

</div>

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Now suppose a field $$\mathbb{K}$$ is given. The *Euclidean $$n$$-dimensional space* is the $$\mathbb{K}$$-vector space consisting of $$n$$-tuples

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix},\qquad a_i\in\mathbb{K}\text{ for all $i$}$$

Addition and scalar multiplication are defined by

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}+\begin{pmatrix}b_1\\b_2\\\vdots\\b_n\end{pmatrix}=\begin{pmatrix}a_1+b_1\\a_2+b_2\\\vdots\\a_n+b_n\end{pmatrix},\qquad \alpha\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}=\begin{pmatrix}\alpha a_1\\\alpha a_2\\\vdots\\\alpha a_n\end{pmatrix}$$

When $$\mathbb{K}=\mathbb{R}$$ and $$n=2,3$$, this gives the familiar coordinate plane and coordinate space.

</div>

Euclidean spaces will be especially important objects for us. In the example above we used column notation instead of the ordered pair $$(a_1, a_2, \ldots, a_n)$$, which is closely related to the fundamental theorem of linear algebra.

However, no matter how compelling the reason, insisting on this $$\begin{pmatrix}a_1\\a_2\\ \vdots\\a_n\end{pmatrix}$$ notation throughout the text would be foolish. Therefore, in the main text we will use notation such as $$(a_1\;a_2\;\cdots\;a_n)^t$$, or following high school convention, simply $$(a_1,a_2,\ldots, a_n)$$.

The two vector spaces examined above are fairly concrete examples. As the next example shows, vector spaces are not always visualizable like the coordinate plane or coordinate space.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Let $$I$$ be an interval and consider the set $$\Fun(I,\mathbb{R})$$ of functions from $$I$$ to $$\mathbb{R}$$. If we define addition and scalar multiplication on this set by

$$f+g:t\mapsto f(t)+g(t),\qquad \alpha f:t\mapsto \alpha f(t)$$

then one can verify that $$\Fun(I,\mathbb{R})$$ has a vector space structure. That is, $$f+g$$ is the function sending each $$t\in I$$ to $$f(t)+g(t)$$, and $$\alpha f$$ is the function sending each $$t\in I$$ to $$\alpha f(t)$$.

Moreover, various subsets of $$\Fun(I,\mathbb{R})$$ are also $$\mathbb{R}$$-vector spaces. For example, the set $$C(I)$$ of continuous functions from $$I$$ to $$\mathbb{R}$$ is an $$\mathbb{R}$$-vector space, and more generally one can verify that the set $$C^k(I)$$ of functions whose $$k$$th derivative is continuous is also an $$\mathbb{R}$$-vector space.

</div>

If we think of $$\Fun(I,\mathbb{R})$$ as the product set $$\mathbb{R}^I$$, then [Example 6](#ex6) can be viewed as a natural generalization of [Example 5](#ex5). ([\[Set Theory\] §Product of Sets, ⁋Definition 1](/en/math/set_theory/product_of_sets#def1))

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
