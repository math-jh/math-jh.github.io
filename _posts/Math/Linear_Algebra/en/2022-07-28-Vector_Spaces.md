---
title: "Vector Spaces"
excerpt: "Definition of vector spaces, simple properties, and examples"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/vector_spaces
sidebar: 
    nav: "linear_algebra-en"

header:
    overlay_image: /assets/images/Math/Linear_Algebra/Vector_Spaces.png
    overlay_filter: 0.5

date: 2022-07-28
last_modified_at: 2022-07-28

weight: 2
translated_at: 2026-05-21T02:30:01+00:00
translation_source: kimi-cli
---
As we mentioned in the opening of the previous post, the *vector space* is the space studied in linear algebra; it is a concept generalizing the coordinate space learned in high school. For this purpose, we defined abelian groups and fields in the previous post.

Many linear algebra textbooks avoid these definitions and simply consider only $$\mathbb{R}$$-vector spaces or $$\mathbb{C}$$-vector spaces, but the more general case is not at all complicated, so there is no need to restrict our attention to special cases.

## Definition

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$\mathbb{K}$$ be a field and let $$V$$ be an abelian group. We say that $$V$$ is a *vector space over $$\mathbb{K}$$*, or simply a *$$\mathbb{K}$$-vector space*, if there exists an additional operation (*scalar multiplication*) $$\cdot:\mathbb{K}\times V\rightarrow V$$ such that

1. for any $$\alpha,\beta\in\mathbb{K}$$ and any $$u\in V$$, we have $$\alpha\cdot(\beta\cdot u)=(\alpha\beta)\cdot u$$.
2. for any $$\alpha\in\mathbb{K}$$ and any $$u,v\in V$$, we have $$\alpha\cdot(u+_{\tiny V}v)=(\alpha\cdot u)+_{\tiny V}(\alpha\cdot v)$$.
3. for any $$\alpha,\beta\in\mathbb{K}$$ and any $$u\in V$$, we have $$(\alpha+_{\tiny \mathbb{K}}\beta)\cdot u=(\alpha\cdot u)+_{\tiny V}(\beta\cdot u)$$.
4. for the multiplicative identity $$1\in\mathbb{K}$$ of $$\mathbb{K}$$, we have $$1\cdot u=u$$ for any $$u\in V$$.

all hold. The elements of $$V$$ are called *vectors*.

</div>

As in the definition above, from now on we shall write elements of the field $$\mathbb{K}$$ as $$\alpha,\beta,\ldots$$ and elements of a $$\mathbb{K}$$-vector space as $$u,v,\ldots$$ in order to avoid confusion. In the above definition we distinguished $$+_{\tiny V}$$ and $$+_{\tiny \mathbb{K}}$$, but if we separate them as in the notation we just introduced, it is clear whether the elements around $$+$$ belong to $$\mathbb{K}$$ or to $$V$$, so there is no danger of confusion in writing them simply as $$+$$.

Likewise, we shall write the scalar multiplication as $$\alpha u$$ instead of $$\alpha\cdot u$$. The only concern in this case is that when we write $$\alpha\beta u$$, it may be unclear whether this means $$(\alpha\beta)u$$ or $$\alpha(\beta u)$$; however, by the first condition of the above definition the value is the same no matter which interpretation we choose, so this is nothing to worry about.

A vector space is an abelian group $$V$$ equipped with the additional structure of $$\mathbb{K}$$-scalar multiplication. Therefore $$V$$ has all the properties that an abelian group has. ([§Abelian Groups and Fields, ⁋Proposition 2](/en/math/linear_algebra/fields#prop2) and [§Abelian Groups and Fields, ⁋Corollary 3](/en/math/linear_algebra/fields))

The following are additional properties determined by the $$\mathbb{K}$$-scalar multiplication.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let a $$\mathbb{K}$$-vector space $$V$$ be given. Then

1. for any $$\alpha\in\mathbb{K}$$, we have $$\alpha0=0$$, and
2. for any $$v\in V$$, we have $$0v=0$$.

Conversely, if $$\alpha v=0$$, then either $$\alpha=0$$ or $$v=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first two claims proceed similarly to [§Abelian Groups and Fields, ⁋Proposition 5](/en/math/linear_algebra/fields#prop5). For example,

$$\alpha0+\alpha0=\alpha(0+0)=\alpha0$$

so $$\alpha0=0$$, and similarly

$$0v+0v=(0+0)v=0v$$

so $$0v=0$$. Finally, suppose $$\alpha v=0$$ and $$\alpha\neq 0$$. Then there exists $$\alpha^{-1}\in\mathbb{K}$$ with $$\alpha\alpha^{-1}=1$$, and therefore

$$v=1v=(\alpha^{-1}\alpha)v=\alpha^{-1}(\alpha v)=\alpha^{-1}0=0$$

so $$v=0$$, and the given proposition holds.

</details>

The $$0$$ appearing in item 1 of the above proposition and the $$0$$ on the right-hand side of item 2 are both elements of $$V$$, while the $$0$$ on the left-hand side of item 2 is an element of $$\mathbb{K}$$. To be rigorous we ought to distinguish them as $$0_{\tiny V}$$ and $$0_{\tiny \mathbb{K}}$$, but in context they can be clearly distinguished, so we write them simply as $$0$$.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> For any element $$v$$ of a $$\mathbb{K}$$-vector space $$V$$, we always have $$(-1)v=-v$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is immediate from the identity

$$(-1)v+v=(-1)v+1v=((-1)+1)v=0v=0$$

and the uniqueness of additive inverses in $$V$$.

</details>

## Examples

Now let us look at some examples of vector spaces.

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> The simplest example of a vector space is $$\{0\}$$. There is only one way to endow this set with an addition structure (namely $$0+0=0$$), and under this structure the set has the structure of an abelian group. Moreover, no matter which field $$\mathbb{K}$$ we take, there is also only one way to define a scalar multiplication on this set (namely $$\alpha 0=0$$), and the scalar multiplication thus defined makes $$\{0\}$$ into a $$\mathbb{K}$$-vector space. This is called the *trivial space*.

A slightly less trivial example is the field itself. For any field $$\mathbb{K}$$, $$\mathbb{K}$$ is a $$\mathbb{K}$$-vector space. Since $$\mathbb{K}$$ is a field, it is obvious that it is an abelian group under addition. We only need to give it a scalar multiplication structure, which is simply given by the multiplication in $$\mathbb{K}$$, $$\mathbb{K}\times \mathbb{K}\rightarrow \mathbb{K}$$. One can check that with this definition the scalar multiplication satisfies all the conditions of [Definition 1](#def1), and therefore $$\mathbb{K}$$ is itself a $$\mathbb{K}$$-vector space.

More generally, let $$\mathbb{K}$$ be a field and suppose there exists another field $$\mathbb{K}'$$ with $$\mathbb{K}'\supseteq \mathbb{K}$$. Then $$\mathbb{K}'$$ becomes a $$\mathbb{K}$$-vector space. Since $$\mathbb{K}'$$ is a field, it forms an abelian group under addition just as before, and the scalar multiplication by an element $$\alpha\in\mathbb{K}$$ is given by treating $$\alpha$$ as an element of $$\mathbb{K}'$$ and using the multiplication structure of $$\mathbb{K}'$$. For example, $$\mathbb{C}$$ is an $$\mathbb{R}$$-vector space, and $$\mathbb{R}$$ is a $$\mathbb{Q}$$-vector space.

</div>

<div class="example" markdown="1">

<ins id="ex5">**Example 5**</ins> Now suppose a field $$\mathbb{K}$$ is given. Then the *Euclidean $$n$$-space* is the $$\mathbb{K}$$-vector space consisting of the following $$n$$-tuples

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix},\qquad a_i\in\mathbb{K}\text{ for all $i$}$$

Addition and scalar multiplication between them are defined respectively by

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}+\begin{pmatrix}b_1\\b_2\\\vdots\\b_n\end{pmatrix}=\begin{pmatrix}a_1+b_1\\a_2+b_2\\\vdots\\a_n+b_n\end{pmatrix},\qquad \alpha\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}=\begin{pmatrix}\alpha a_1\\\alpha a_2\\\vdots\\\alpha a_n\end{pmatrix}$$

When $$\mathbb{K}=\mathbb{R}$$ and $$n=2,3$$, this definition becomes the familiar coordinate plane and coordinate space.

</div>

Euclidean spaces are objects we shall encounter particularly often. In the above example we are using column notation instead of the notation $$(a_1, a_2, \ldots, a_n)$$ for ordered tuples, and this is closely related to the fundamental theorem of linear algebra.

But no matter how compelling the reason, it would be foolish to insist on this notation $$\begin{pmatrix}a_1\\a_2\\ \vdots\\a_n\end{pmatrix}$$ throughout the text. Therefore, in the body of the text we shall write $$(a_1\;a_2\;\cdots\;a_n)^t$$ or, following high-school notation, $$(a_1,a_2,\ldots, a_n)$$.

The two vector spaces examined above are fairly concrete examples. As the next example shows, vector spaces in general are not always representable visually like the coordinate plane or coordinate space.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Let $$I$$ be an interval and consider the collection $$\Fun(I,\mathbb{R})$$ of functions from $$I$$ to $$\mathbb{R}$$. Now define addition and scalar multiplication on this set by the formulas

$$f+g:t\mapsto f(t)+g(t),\qquad \alpha f:t\mapsto \alpha f(t)$$

then one can check that $$\Fun(I,\mathbb{R})$$ has the structure of a vector space. That is, $$f+g$$ is defined as the function sending any $$t\in I$$ to the value $$f(t)+g(t)$$, and $$\alpha f$$ is defined as the function sending any $$t\in I$$ to $$\alpha f(t)$$.

Moreover, various subsets of $$\Fun(I,\mathbb{R})$$ are also $$\mathbb{R}$$-vector spaces. For example, the collection $$C(I)$$ of continuous functions from $$I$$ to $$\mathbb{R}$$ is also an $$\mathbb{R}$$-vector space, and more generally one can check that the collections $$C^k(I)$$ of functions whose $$k$$-th derivatives are continuous are also $$\mathbb{R}$$-vector spaces.

</div>

Thinking of $$\Fun(I,\mathbb{R})$$ as the product set $$\mathbb{R}^I$$, [Example 6](#ex6) can also be viewed as a natural generalization of [Example 5](#ex5). ([\[Set Theory\] §Product of Sets, ⁋Definition 1](/en/math/set_theory/product_of_sets#def1))

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
