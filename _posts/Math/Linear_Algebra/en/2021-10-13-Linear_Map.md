---
title: "Linear Maps"
description: "Defines linear maps as functions between vector spaces that preserve addition and scalar multiplication, and covers their composition and basic properties."
excerpt: "The definition and examples of linear maps"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/linear_map
sidebar: 
    nav: "linear_algebra-en"


date: 2021-10-13

weight: 6
translated_at: 2026-05-31T19:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T19:00:06+00:00
---
In this post, we define functions between vector spaces, namely *linear maps*.

## Linear Maps

Since a vector space is at its core a set, a function between two vector spaces $$V,W$$ exists simply as a function between sets. However, unlike an ordinary set, a vector space comes equipped with addition of elements and scalar multiplication by elements of $$\mathbb{K}$$, so we are only interested in those functions between vector spaces (as sets) that preserve these operations.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let two $$\mathbb{K}$$-vector spaces $$V,W$$ be given. A function $$L:V\rightarrow W$$ is called a *linear map* if

1. for any $$\alpha\in\mathbb{K}$$ and $$v\in V$$, $$L(\alpha v)=\alpha L(v)$$, and
2. for any $$v_1,v_2\in V$$, $$L(v_1+v_2)=L(v_1)+L(v_2)$$.

</div>

In the special case where $$V=W$$, we call these *linear operators*. The following propositions are almost immediate from the definition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$,

1. $$L(0)=0$$.
2. For any $$v\in V$$, $$L(-v)=-L(v)$$.
3. For any $$u,v\in V$$, $$L(u-v)=L(u)-L(v)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since a linear map preserves scalar multiplication, the first and second claims follow respectively from [§Vector Spaces, ⁋Proposition 2](/en/math/linear_algebra/vector_spaces#prop2) and [§Vector Spaces, ⁋Corollary 3](/en/math/linear_algebra/vector_spaces#cor3). Now, using the fact that a linear map preserves vector addition together with the second claim, we have

$$L(u-v)=L\bigl(u+(-v)\bigr)=L(u)+L(-v)=L(u)+\bigl(-L(v)\bigr)=L(u)-L(v)$$

so the third claim also holds.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$, a linear map $$L:V\rightarrow W$$, scalars $$\alpha_1,\ldots,\alpha_n$$, and vectors $$v_1,\ldots, v_n$$ in $$V$$,

$$L\left(\sum_{i=1}^k\alpha_i v_i\right)=\sum_{i=1}^kL(\alpha_iv_i)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This is obvious by induction on $$k$$.

</details>

Just as the composition of functions is a function, the composition of linear maps is also a linear map. Moreover, as we will verify later, if a linear map has an inverse, then its inverse is automatically a linear map.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For three $$\mathbb{K}$$-vector spaces $$U,V,W$$ and linear maps $$L_1:U\rightarrow V$$, $$L_2:V\rightarrow W$$, the composition $$L_2\circ L_1:U\rightarrow W$$ is linear.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$\alpha\in\mathbb{K}$$ and $$u\in U$$,

$$(L_2\circ L_1)(\alpha u)=L_2(L_1(\alpha u))=L_2(\alpha L_1(u))=\alpha(L_2(L_1(u)))=\alpha(L_2\circ L_1)(u)$$

Similarly, one can show that $$(L_2\circ L_1)(u_1+u_2)=(L_2\circ L_1)(u_1)+(L_2\circ L_1)(u_2)$$ holds for vectors.
</details>

## Kernel and Image of a Linear Map

Now let us define the following.

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$,

1. if $$v_1=v_2$$ whenever $$L(v_1)=L(v_2)$$, then $$L$$ is said to be *injective*.
2. if for every $$w\in W$$ there exists $$v\in V$$ satisfying $$L(v)=w$$, then $$L$$ is said to be *surjective*. 

</div>

In general, the definitions above are almost the only tools available when dealing with injective or surjective functions. However, when the objects under consideration are not mere sets but are equipped with some operations, as in the present situation, algebraic tools can also be brought to bear.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$, the *kernel* $$\ker L$$ of $$L$$ is the set defined by the formula

$$\ker L=\{v\in V\mid L(v)=0\}$$

Also, the *image* $$\im L$$ of $$L$$ is the set defined by the formula

$$\im L=\{w\in W\mid L(v)=w\text{ for some $v\in V$}\}$$

</div>

The following can be checked without difficulty.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$, we have $$\ker L\leq V$$ and $$\im L\leq W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, $$\ker L$$ is a subspace of $$V$$. For any $$\alpha\in\mathbb{K}$$ and $$v\in\ker L$$,

$$L(\alpha v)=\alpha L(v)=\alpha\cdot 0=0$$

and similarly for any $$v_1$$, $$v_2\in \ker L$$,

$$L(v_1+v_2)=L(v_1)+L(v_2)=0+0=0$$

so $$\alpha v\in\ker L$$ and $$v_1+v_2\in\ker L$$.

Likewise, $$\im L$$ is a subspace of $$W$$. Take arbitrary $$w,w_1,w_2\in W$$ and $$\alpha\in\mathbb{K}$$; then by definition there exist $$v,v_1,v_2\in V$$ satisfying

$$L(v)=w,\quad L(v_1)=w_1,\quad L(v_2)=w_2$$

and therefore

$$\alpha w=\alpha L(v)=L(\alpha v)\in\im L$$

and

$$w_1+w_2=L(v_1)+L(v_2)=L(v_1+v_2)\in \im L$$

</details>

We can now determine whether $$L$$ is injective or surjective by means of $$\ker L$$ and $$\im L$$.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$,

1. $$L$$ is injective if and only if $$\ker L=\{0\}$$, and
2. $$L$$ is surjective if and only if $$\im L=W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The second claim is a tautology.

If $$L$$ is injective, then the $$v$$ satisfying $$L(v)=0$$ must be unique, and by [Proposition 2](#prop2), $$0$$ satisfies this equation, so we must have $$\ker L=\{0\}$$. Thus, for the first claim it suffices to show

> $$\ker L=\{0\}\implies\text{$L$ is injective}$$

Assume $$v_1,v_2\in V$$ are given with $$L(v_1)=L(v_2)$$. Then by [Proposition 3](#prop3),

$$0=L(v_1)-L(v_2)=L(v_1-v_2)$$

so $$v_1-v_2\in\ker L$$. Since $$\ker L=\{0\}$$, we have $$v_1-v_2=0$$, and therefore $$L$$ is injective.

</details>

Speaking loosely, the smaller $$\ker L$$ is, the closer $$L$$ is to being injective, and the larger $$\im L$$ is, the closer $$L$$ is to being surjective.

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> Let two $$\mathbb{K}$$-vector spaces $$V,W$$ and a linear map $$L:V\rightarrow W$$ be given.

1. If $$L$$ is injective, then for any linearly independent subset $$S\subset V$$, the image $$L(S)$$ is also linearly independent in $$W$$.
2. If $$L$$ is surjective, then for any $$S\subset V$$ satisfying $$\langle S\rangle=V$$, the image $$L(S)$$ also satisfies $$\span L(S)=W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. For elements $$L(x_1),\ldots, L(x_k)$$ of $$L(S)$$, if

    $$\sum_{i=1}^k\alpha_i L(x_i)=0$$

    then by [Proposition 3](#prop3),

    $$0=L\left(\sum_{i=1}^k\alpha_ix_i\right)$$

    so by the preceding proposition we must have $$\sum\alpha_ix_i=0$$. Since $$S$$ is a linearly independent subset, $$\alpha_i=0$$ holds for every $$i$$.

2. Let any $$w\in W$$ be given. Then since $$\im L=W$$, there exists a suitable $$v\in V$$ with $$L(v)=w$$. On the other hand, since $$\langle S\rangle=V$$, we can express $$v$$ as a linear combination of elements of $$S$$:

    $$v=\sum_{i=1}^n\alpha_ix_i$$
    
    Applying $$L$$ to both sides and using [Proposition 3](#prop3),
    
    $$w=L(v)=L\left(\sum_{i=1}^n\alpha_ix_i\right)=\sum_{i=1}^n\alpha_i L(x_i)$$
    
    Thus every $$w\in W$$ can be expressed as a linear combination of elements of $$L(S)$$.
 
</details>

In fact, the converses of the two statements in the above corollary also hold, and their proofs are not difficult, but we omit them since we will have no occasion to use them.

## Examples of Linear Maps

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> For arbitrary $$\mathbb{K}$$-vector spaces $$V$$ and $$W$$, the map $$L:V\rightarrow W$$ defined by the formula

$$L(v)=0\text{ for all $v\in V$}$$

is linear. In this case, $$\im L=\{0\}$$ and $$\ker L=V$$.

</div>

The function defined in the above example is itself sometimes denoted by $$0$$. This notation may cause confusion with the additive identity $$0$$, but this function is *actually* the identity element in an appropriate vector space. The proof of this is not difficult, but we postpone it.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> Let an arbitrary $$\mathbb{K}$$-vector space $$V$$ and a subspace $$W\leq V$$ be given. The map $$\iota:W\rightarrow V$$ defined by the formula

$$\iota(w)=w\text{ for all $w\in W$}$$

is a linear map. In this case, $$\im\iota=W$$ and $$\ker \iota=\{0\}$$. That is, $$\iota$$ is injective.

</div>

In the above example, in the special case where $$W=V$$, the map $$\iota$$ becomes the identity function $$\id_V$$. ([\[Set Theory\] §Operations on Functions, ⁋Example 3](/en/math/set_theory/operation_of_functions#ex3)) 

<div class="example" markdown="1">

<ins id="ex12">**Example 12**</ins> Consider arbitrary $$\mathbb{K}$$-vector spaces $$V$$, $$W$$, and their product $$V\times W$$. Then the map $$\pr_1:V\times W\rightarrow V$$ defined by the formula

$$\pr_1((v,w))=v$$

is a linear map. We can easily check that $$\im\pr_1=V$$ and

$$\ker \pr_1=\{(0,w)\mid w\in W\}$$

Of course, $$\pr_2:V\times W\rightarrow W$$ can be defined similarly, and this can be extended to ordered $$n$$-tuples. In particular, for Euclidean space $$\mathbb{K}^n$$,

$$\pr_i((a_1,\ldots, a_n))=a_i$$

defines a linear map $$\pr_i:\mathbb{K}^n\rightarrow \mathbb{K}$$.

</div>

$$\pr$$ is the initial letter of projection, and is sometimes written simply as $$p$$ or $$\pi$$.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Let the function $$D:\mathbb{K}[\x]\rightarrow \mathbb{K}[\x]$$ on $$\mathbb{K}[\x]$$ be defined by the formula

$$D\left(\sum_{i=0}^\infty a_i\x^i\right)=\sum_{i=1}^\infty ia_i\x^{i-1}$$

(Here $$(a_i)$$ is finitely supported.) Then $$D$$ is linear, and $$\im D= \mathbb{K}[\x]$$. Also, $$\ker D$$ is the set of all constant polynomials.

</div>

The last example is not merely a simple example; it can be thought of as the prototype of the isomorphism that we will examine in the next post.

<div class="example" markdown="1">

<ins id="ex14">**Example 14**</ins> Let an arbitrary $$n$$-dimensional $$\mathbb{K}$$-vector space $$V$$ be given, and let $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ be a basis of $$V$$. That is, for any $$v\in V$$, there always exist scalars $$v_1,\ldots, v_n$$ such that

$$v=\sum_{i=1}^n v_i x_i$$

and these scalars are uniquely determined. Therefore, we can define a function $$L:V\rightarrow \mathbb{K}^n$$ by the formula $$v\mapsto (v_1,v_2,\ldots, v_n)\in\mathbb{K}^n$$.

Then $$L$$ is linear. For any $$v,w\in V$$, writing

$$v=\sum_{i=1}^n v_i x_i,\quad w=\sum_{i=1}^n w_i x_i$$

for any $$\alpha\in\mathbb{K}$$ we have

$$\alpha L(v)=\alpha(v_1,v_2,\ldots,v_n)=(\alpha v_1,\alpha v_2,\ldots,\alpha v_n)$$

while

$$\alpha v=\alpha\sum_{i=1}^nv_i x_i=\sum_{i=1}^n\alpha v_i x_i$$

so the value of $$L(\alpha v)$$ is the same as that of $$\alpha L(v)$$. Similarly, comparing the values of $$L(v)+L(w)$$ and $$L(v+w)$$,

$$L(v)+L(w)=(v_1+w_1,v_2+w_2,\ldots,v_n+w_n)=L(v+w)$$

holds.

$$\ker L$$ becomes $$\{0\}$$ because $$\mathcal{B}$$ is linearly independent. On the other hand, for any $$(\alpha_1,\ldots,\alpha_n)\in\mathbb{K}^n$$ the linear combination

$$\sum_{i=1}^n\alpha_i x_i$$

obviously belongs to $$V$$, so $$L$$ is injective.

</div>


---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---
