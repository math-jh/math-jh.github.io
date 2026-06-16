---
title: "Space of Linear Maps"
description: "A linear map is uniquely determined by its values on a basis. This post also covers the matrix representation of linear maps in finite-dimensional vector spaces."
excerpt: "Hom and Dual Space"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/space_of_linear_maps
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-05

weight: 10
translated_at: 2026-05-31T23:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T23:00:06+00:00
---
## Extension by linearity

<div class="proposition" markdown="1">

<ins id="thm1">**Theorem 1 (Extension by linearity)**</ins> Let $$V$$ be an arbitrary $$\mathbb{K}$$-vector space with basis $$\mathcal{B}$$. For any other $$\mathbb{K}$$-vector space $$W$$, whenever a function $$g:\mathcal{B}\rightarrow W$$ is given, there exists a unique linear map $$G:V\rightarrow W$$ such that $$g=G\circ\iota$$.

</div>

Here $$\iota:\mathcal{B}\rightarrow V$$ denotes the inclusion $$\mathcal{B}\hookrightarrow V$$.

<details class="proof" markdown="1">
<summary>Proof</summary>

For a given function $$g$$, it is clear that a linear map $$G$$ satisfying the condition must be unique. Indeed, if $$G':V\rightarrow W$$ is another linear map satisfying the given condition, then for any $$v\in V$$, writing

$$v=\sum_{x\in \mathcal{B}}v_xx$$

we have

$$\begin{aligned}(G-G')\left(\sum_{x\in \mathcal{B}}v_xx\right)&=\sum_{x\in\mathcal{B}}v_x(G-G')(x)=\sum_{x\in\mathcal{B}}v_x(G-G')(\iota(x))\\&=\sum_{x\in\mathcal{B}}v_x(G\circ \iota-G'\circ\iota)(x)=\sum_{x\in\mathcal{B}}v_x(g-g)(x)=0\end{aligned}$$

as claimed.

Now we must actually construct $$G$$. Naturally, for any $$v=\sum_{x\in\mathcal{B}}v_xx$$, we *define*

$$G(v)=\sum_{x\in\mathcal{B}} v_xg(x)$$

Since the expression of $$v$$ as a linear combination of elements of $$\mathcal{B}$$ is unique, $$G$$ is well-defined, and one can easily verify that $$G$$ is a linear map.

</details>

That is, we can always find $$G:V\rightarrow W$$ making the following diagram commute.

![extend_by_linearity](/assets/images/Math/Linear_Algebra/Space_of_Linear_Maps-1.svg){:style="width:5.88em" class="invert" .align-center}

Conversely, given any linear map $$G:V\rightarrow W$$, we may restrict it to $$\mathcal{B}$$ to define a function $$g=G\circ\iota$$, and by the uniqueness part of the theorem above, $$G$$ is the only linear map satisfying this equation. Thus there is a bijection between the following two sets:

$$\{\text{functions from $\mathcal{B}$ to $W$}\}\longleftrightarrow\{\text{linear maps from $V$ to $W$}\}$$

In other words, a linear map from $$V$$ to $$W$$ is completely determined by how it acts on the basis $$\mathcal{B}$$, and if $$V$$ is finite-dimensional, this means that the linear map is determined solely by its values at finitely many elements.

In particular, assume that the codomain $$W$$ is also a finite-dimensional $$\mathbb{K}$$-vector space, and fix a basis $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ of $$V$$ and a basis $$\mathcal{C}=\{y_1,\ldots,y_m\}$$ of $$W$$. Then by the preceding argument, a linear map $$L$$ from $$V$$ to $$W$$ is completely determined by the $$n$$ vectors in $$W$$

$$L(x_1),L(x_2)\ldots, L(x_n)$$

and as elements of $$W$$, these can again be expressed as linear combinations of elements of $$\mathcal{C}$$

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}\tag{1}$$

Then the value of $$L$$ at an arbitrary element of $$V$$ can be expressed as a linear combination with respect to the basis $$\mathcal{C}$$, using the scalars $$\alpha_{i,j}$$ together with the scalars $$v_1,\ldots, v_n$$ appearing in the coordinate expression $$v=\sum_{i=1}^n v_ix_i$$.

$$\begin{aligned}L(v_1x_1)&=\alpha_{11}v_1y_1+\alpha_{21}v_1y_2+\cdots+\alpha_{m1}v_1y_m\\L(v_2x_2)&=\alpha_{12}v_2y_1+\alpha_{22}v_2y_2+\cdots+\alpha_{m2}v_2y_m\\&\phantom{a}\vdots\\L(v_nx_n)&=\alpha_{1n}v_ny_1+\alpha_{2n}v_ny_2+\cdots+\alpha_{mn}v_ny_m\end{aligned}$$

Thus, adding the corresponding sides, the left-hand side becomes

$$L(v_1x_1)+L(v_2x_2)+\cdots+L(v_nx_n)=L(v_1x_1+v_2x_2+\cdots+v_nx_n)=L(v)$$

and the right-hand side becomes

$$(\alpha_{11}v_1+\alpha_{12}v_2+\cdots+\alpha_{1n}v_n)y_1+(\alpha_{21}v_1+\alpha_{22}v_2+\cdots+\alpha_{2n}v_n)y_2+\cdots+(\alpha_{m1}v_1+\alpha_{m2}v_2+\cdots+\alpha_{mn}v_n)y_m$$

Therefore $$L$$ can be understood as the correspondence

$$v=\sum_{i=1}^n v_ix_i\quad\mapsto\quad \sum_{j=1}^m\left(\sum_{i=1}^n\alpha_{ji}v_i\right)y_j=L(v)$$

Using the theorem above, we can prove the following proposition corresponding to [\[Set Theory\] §Retraction and Section, ⁋Proposition 1](/en/math/set_theory/retraction_and_section#prop1).

<div class="proposition" markdown="1">

<ins id="cor2">**Corollary 2**</ins> Let $$V,W$$ be two $$\mathbb{K}$$-vector spaces and let $$L:V\rightarrow W$$ be a linear map.

1. If $$L$$ is injective, there exists a linear map $$R:W\rightarrow V$$ such that $$R\circ L=\id_V$$.
2. If $$L$$ is surjective, there exists a linear map $$S:W\rightarrow V$$ such that $$L\circ S=\id_W$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. First suppose $$L$$ is injective, and choose a basis $$x_1,\ldots,x_n$$ of $$V$$. Then $$L(x_1),\ldots, L(x_n)$$ are linearly independent, and therefore we can find a basis $$\mathcal{B}$$ of $$W$$ containing them. Now define a function $$r:\mathcal{B}\rightarrow V$$ by
    
    $$r(v)=\begin{cases}x_i&\text{if $v=L(x_i)$}\\0&\text{otherwise}\end{cases}$$

    and apply [Theorem 1](#thm1) to obtain a linear map, which we call $$R$$. Then for any element $$x_i$$ of the basis $$\{x_1,\ldots,x_n\}$$ of $$V$$, we have $$(R\circ L)(x_i)=x_i$$, and hence by the uniqueness part of Theorem 1, $$R\circ L=\id_V$$.

2. Suppose $$L$$ is surjective, and choose a basis $$x_1,\ldots,x_n$$ of $$V$$. Then $$L(x_1),\ldots, L(x_n)$$ span $$W$$, so we can select some of these vectors to form a basis $$\mathcal{B}$$ of $$W$$. Without loss of generality, let $$\mathcal{B}=\{L(x_1),\ldots, L(x_m)\}$$ ($$m\leq n$$). Define a function $$s:\mathcal{B}\rightarrow V$$ by
    
    $$s(v)=x_k\qquad v=L(x_k)$$

    and apply [Theorem 1](#thm1) to obtain a linear map, which we call $$S$$. Now for any element $$L(x_k)$$ of the basis $$\mathcal{B}$$ of $$W$$, we have $$(L\circ S)(L(x_k))=L(x_k)$$, so again by the uniqueness part of Theorem 1, $$L\circ S=\id_W$$.

</details>

## Space of Linear Maps

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> Let $$V$$ and $$W$$ be $$\mathbb{K}$$-vector spaces. If $$L,L_1,L_2$$ are linear maps from $$V$$ to $$W$$ and $$\alpha\in\mathbb{K}$$, then

$$L_1+L_2:v\mapsto L_1(v)+L_2(v),\qquad \alpha L:v\mapsto \alpha L(v)$$

are also linear.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$v, v_1,v_2\in V$$ and $$\alpha\in\mathbb{K}$$. Then

$$\begin{aligned}
        (L_1+L_2)(v_1+v_2)&=L_1(v_1+v_2)+L_2(v_1+v_2)\\
        &=L_1(v_1)+L_1(v_2)+L_2(v_1)+L_2(v_2)\\
        &=L_1(v_1)+L_2(v_1)+L_1(v_2)+L_2(v_2)\\
        &=(L_1+L_2)(v_1)+(L_1+L_2)(v_2)
    \end{aligned}$$

and

$$\begin{aligned}
        (L_1+L_2)(\alpha v)&=L_1(\alpha v)+L_2(\alpha v)=\alpha L_1(v)+\alpha L_2(v)\\
        &=\alpha(L_1(v)+L_2(v))\\
        &=\alpha (L_1+L_2)(v).
    \end{aligned}$$
    
Therefore $$L_1+L_2$$ is a linear map. The second claim can be shown similarly.

</details>

Thus we may make the following definition.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For two $$\mathbb{K}$$-vector spaces $$V,W$$, the $$\mathbb{K}$$-vector space obtained by equipping the set of linear maps from $$V$$ to $$W$$ with the operations from [Lemma 3](#lem3) is denoted $$\Hom_\mathbb{K}(V,W)$$, or simply $$\Hom(V,W)$$ when the field $$\mathbb{K}$$ is clear from context.

In particular, when $$W=\mathbb{K}$$, we call $$\Hom(V,\mathbb{K})$$ the *dual space* of $$V$$ and denote it by $$V^\ast$$. The elements of $$V^\ast$$ are called *linear functionals*.

</div>

The zero vector in the vector space $$\Hom(V,W)$$ is the function $$0$$ sending every element to 0. ([§Linear Maps, ⁋Example 10](/en/math/linear_algebra/linear_map#ex10)) When referring to this function, we shall call it the zero function for convenience.

Suppose both spaces $$V,W$$ are finite-dimensional, and let $$\mathcal{B}=\{x_1,\ldots, x_n\}$$ and $$\mathcal{C}=\{y_1,\ldots, y_m\}$$ be bases of $$V$$ and $$W$$, respectively. Consider the $$mn$$ functions from $$\mathcal{B}$$ to $$W$$

$$f_i^j(x)=\begin{cases}y_j&\text{if $x=x_i$}\\0&\text{otherwise}\end{cases}$$

That is, $$f_i^j$$ is the function sending only $$x_i$$ to $$y_j$$ and everything else to 0. Then by [Theorem 1](#thm1), there exists a unique linear map $$B_i^j$$ such that $$f_i^j=B_i^j\circ\iota$$.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$V,W$$ be two finite-dimensional $$\mathbb{K}$$-vector spaces with bases $$\{x_1,\ldots,x_n\}$$ and $$\{y_1,\ldots,y_m\}$$, respectively. Then $$\Hom(V,W)$$ is an $$mn$$-dimensional vector space, and the $$mn$$ linear maps $$B_i^j$$ defined above form a basis of $$\Hom(V,W)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to prove the claim about the basis.

First, the $$B_i^j$$ are linearly independent. For scalars $$\alpha_{11},\ldots,\alpha_{mn}$$, suppose

$$\alpha_{11}B_1^1+\alpha_{12}B_2^1+\cdots+\alpha_{mn}B_n^m=0$$

That is, both sides are the zero function from $$V$$ to $$W$$, and therefore for any $$v\in V$$ the equation

$$\alpha_{11}B_1^1(v)+\alpha_{12}B_2^1(v)+\cdots+\alpha_{mn}B_n^m(v)=0$$

holds. In particular, this equation also holds for $$v=x_1,\ldots, x_n$$, and then

$$\alpha_{11}B_1^1(x_k)+\alpha_{12}B_2^1(x_k)+\cdots+\alpha_{mn}B_n^m(x_k)=0$$

But by the definition of $$B_i^j$$, the value $$B_i^j(x_k)$$ is $$y_j$$ only when $$i=k$$, so the above equation becomes

$$\alpha_{1k}y_1+\alpha_{2k}y_2+\cdots+\alpha_{mk}y_k=0$$

Now $$y_1,\ldots,y_k$$ are linearly independent, so $$\alpha_{1k},\ldots,\alpha_{mk}$$ are all $$0$$. Since $$k$$ was arbitrary, $$\alpha_{11},\ldots,\alpha_{mn}$$ are all 0, and the $$B_i^j$$ are linearly independent.

On the other hand, these $$B_i^j$$ span $$\Hom(V,W)$$. Given an arbitrary $$L\in\Hom(V,W)$$, we can find scalars $$\alpha_{11},\ldots,\alpha_{mn}$$ satisfying equation (1) from the introduction. Now the map defined by

$$L'(v)=\sum_{i,j}\alpha_{ji}B_i^j(v)$$

is a linear map. Moreover, substituting $$v=x_k$$ gives

$$L'(x_k)=\sum_{i,j}\alpha_{ji}B_i^j(x_k)=\sum_{j=1}^m\alpha_{jk}B_k^j(x_k)=\sum_{j=1}^m\alpha_{jk}y_j=L(x_k)$$

Hence by the uniqueness part of [Theorem 1](#thm1), we have $$L'=L$$.

</details>
