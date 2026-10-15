---
title: "Space of Linear Maps"
description: "This post shows that a linear map is uniquely determined by its values on a basis and covers the structure of the matrix representation of linear maps in finite-dimensional vector spaces."
excerpt: "Hom and Dual Space"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/space_of_linear_maps
sidebar: 
    nav: "linear_algebra-en"


date: 2022-08-05

weight: 10
translated_at: 2026-05-31T23:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-15T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Extension by linearity

::: Theorem 1 (Extension by linearity)
Let $V$ be an arbitrary $\mathbb{K}$-vector space with basis $\mathcal{B}$. For any other $\mathbb{K}$-vector space $W$, whenever a *function* $g:\mathcal{B}\rightarrow W$ is given, so that $g=G\circ\iota$ holds, there exists a unique *linear map* $G:V\rightarrow W$.
:::

Here $\iota:\mathcal{B}\rightarrow V$ denotes the inclusion $\mathcal{B}\hookrightarrow V$.

::: Proof
For a given function $g$, it is clear that a linear map $G$ satisfying the condition must be unique. Indeed, if $G':V\rightarrow W$ is another linear map satisfying the given condition, then for any $v\in V$, writing

$$v=\sum_{x\in \mathcal{B}}v_xx$$

we have

$$\begin{aligned}(G-G')\left(\sum_{x\in \mathcal{B}}v_xx\right)&=\sum_{x\in\mathcal{B}}v_x(G-G')(x)=\sum_{x\in\mathcal{B}}v_x(G-G')(\iota(x))\\&=\sum_{x\in\mathcal{B}}v_x(G\circ \iota-G'\circ\iota)(x)=\sum_{x\in\mathcal{B}}v_x(g-g)(x)=0\end{aligned}$$

as claimed.

Now we must actually construct $G$. Of course, for any $v=\sum_{x\in\mathcal{B}}v_xx$, it is natural to *define*

$$G(v)=\sum_{x\in\mathcal{B}} v_xg(x)$$

Since the way of writing $v$ as a linear combination of elements of $\mathcal{B}$ is unique by [§Basis of a Vector Space, ⁋Proposition 6](/en/math/linear_algebra/basis#prop6){: data-lid="7rkvp" }, $G$ is well-defined. Moreover, for $v=\sum_{x\in\mathcal{B}}v_xx$, $w=\sum_{x\in\mathcal{B}}w_xx$, and $\alpha\in\mathbb{K}$, we have $v+\alpha w=\sum_{x\in\mathcal{B}}(v_x+\alpha w_x)x$, so $G(v+\alpha w)=\sum_{x\in\mathcal{B}}(v_x+\alpha w_x)g(x)=G(v)+\alpha G(w)$, and therefore $G$ is a linear map.
:::

That is, we can always find $G:V\rightarrow W$ making the following diagram commute.

{% diagram Math/Linear_Algebra/Space_of_Linear_Maps-1.svg width="5.88em" alt="extend_by_linearity" %}

Conversely, given any linear map $G:V\rightarrow W$, we may restrict it to $\mathcal{B}$ to define a function $g=G\circ\iota$, and by the uniqueness part of the theorem above, $G$ is the only linear map satisfying this equation. Thus there is a bijection between the following two sets:

$$\{\text{functions from $\mathcal{B}$ to $W$}\}\leftrightarrow\{\text{linear maps from $V$ to $W$}\}$$

In other words, from $V$ to $W$, a linear map $L$ is completely determined by how it acts on the basis $\mathcal{B}$, and if $V$ is finite-dimensional, this means that the linear map $L$ is determined solely by its values at *finitely many* elements.

In particular, assume that the codomain $W$ is also a finite-dimensional $\mathbb{K}$-vector space, and fix for $V$ a basis $\mathcal{B}=\{x_1,\ldots, x_n\}$ and for $W$ a basis $\mathcal{C}=\{y_1,\ldots,y_m\}$. Then by the preceding argument, from $V$ to $W$, a linear map $L$ is completely determined in $W$ by the $n$ vectors

$$L(x_1),L(x_2),\ldots, L(x_n)$$

and as elements of $W$, these can again be expressed as linear combinations of elements of $\mathcal{C}$

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}\tag{1}$$

Then at an arbitrary element of $V$, the value of $L$ can be expressed using the scalars $\alpha_{ji}$ and the scalars appearing in the coordinate expression $v=\sum_{i=1}^n v_ix_i$, namely $v_1,\ldots, v_n$, as a linear combination with respect to the basis $\mathcal{C}$.

$$\begin{aligned}L(v_1x_1)&=\alpha_{11}v_1y_1+\alpha_{21}v_1y_2+\cdots+\alpha_{m1}v_1y_m\\L(v_2x_2)&=\alpha_{12}v_2y_1+\alpha_{22}v_2y_2+\cdots+\alpha_{m2}v_2y_m\\&\phantom{a}\vdots\\L(v_nx_n)&=\alpha_{1n}v_ny_1+\alpha_{2n}v_ny_2+\cdots+\alpha_{mn}v_ny_m\end{aligned}$$

Thus, adding the corresponding sides, the left-hand side becomes

$$L(v_1x_1)+L(v_2x_2)+\cdots+L(v_nx_n)=L(v_1x_1+v_2x_2+\cdots+v_nx_n)=L(v)$$

and the right-hand side becomes

$$(\alpha_{11}v_1+\alpha_{12}v_2+\cdots+\alpha_{1n}v_n)y_1+(\alpha_{21}v_1+\alpha_{22}v_2+\cdots+\alpha_{2n}v_n)y_2+\cdots+(\alpha_{m1}v_1+\alpha_{m2}v_2+\cdots+\alpha_{mn}v_n)y_m$$

Therefore $L$ can be understood as the correspondence

$$v=\sum_{i=1}^n v_ix_i\quad\mapsto\quad \sum_{j=1}^m\left(\sum_{i=1}^n\alpha_{ji}v_i\right)y_j=L(v)$$

Using the theorem above, we can prove the following proposition corresponding to [\[Set Theory\] §Retraction and Section, ⁋Proposition 1](/en/math/set_theory/retraction_and_section#prop1){: data-lid="7jn0o" }.

::: Corollary 2
Suppose we are given two $\mathbb{K}$-vector spaces $V,W$ and a linear map $L:V\rightarrow W$.

1. If $L$ is injective, there exists a linear map $R:W\rightarrow V$ such that $R\circ L=\id_V$.
2. If $L$ is surjective, there exists a linear map $S:W\rightarrow V$ such that $L\circ S=\id_W$.
:::
::: Proof
1. First suppose $L$ is injective, and for $V$ choose a basis $x_1,\ldots,x_n$. Then $L(x_1),\ldots, L(x_n)$ are linearly independent, and therefore by [§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5){: data-lid="q0iky" } we can find for $W$ a basis $\mathcal{B}$ containing them. Now define a function $r:\mathcal{B}\rightarrow V$ by
    
    $$r(v)=\begin{cases}x_i&\text{if $v=L(x_i)$}\\0&\text{otherwise}\end{cases}$$

    and apply [Theorem 1](#thm1){: data-lid="a3qxb" } to it to obtain a linear map, which we call $R$. Then in the basis of $V$, $\{x_1,\ldots,x_n\}$, for any element $x_i$ we have $(R\circ L)(x_i)=x_i$, and hence by the uniqueness part of Theorem 1, $R\circ L=\id_V$.

2. Suppose $L$ is surjective, and for $V$ choose a basis $x_1,\ldots,x_n$. Then $L(x_1),\ldots, L(x_n)$ span $W$, so by [§Dimension of Vector Spaces, ⁋Proposition 6](/en/math/linear_algebra/dimension#prop6){: data-lid="5ghj2" } we can select some of these vectors to find for $W$ a basis $\mathcal{B}$. Without loss of generality, let $\mathcal{B}=\{L(x_1),\ldots, L(x_m)\}$ ($m\leq n$). Define a function $s:\mathcal{B}\rightarrow V$ by
    
    $$s(v)=x_k\qquad v=L(x_k)$$

    and apply [Theorem 1](#thm1){: data-lid="jlj1s" } to it to obtain a linear map, which we call $S$. Now in the basis of $W$, $\mathcal{B}$, for any element $L(x_k)$ we have $(L\circ S)(L(x_k))=L(x_k)$, so again by the uniqueness part of Theorem 1, $L\circ S=\id_W$.
:::

## Space of Linear Maps

::: Lemma 3
Consider two $\mathbb{K}$-vector spaces $V$ and $W$. If $L,L_1,L_2$ are linear maps from $V$ to $W$ and $\alpha\in\mathbb{K}$, then

$$L_1+L_2:v\mapsto L_1(v)+L_2(v),\qquad \alpha L:v\mapsto \alpha L(v)$$

are also linear.
:::
::: Proof
Let $v, v_1,v_2\in V$ and $\alpha\in\mathbb{K}$. Then

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
    
so $L_1+L_2$ is a linear map. Also, for any $\beta\in\mathbb{K}$, since $(\alpha L)(v_1+v_2)=\alpha L(v_1+v_2)=\alpha L(v_1)+\alpha L(v_2)=(\alpha L)(v_1)+(\alpha L)(v_2)$ and $(\alpha L)(\beta v)=\alpha L(\beta v)=\alpha\beta L(v)=\beta(\alpha L)(v)$, $\alpha L$ is also a linear map.
:::

Thus we may make the following definition.

::: Definition 4
For two $\mathbb{K}$-vector spaces $V,W$, when the set of linear maps from $V$ to $W$ is equipped with the operations from [Lemma 3](#lem3){: data-lid="sg0kl" }, the resulting $\mathbb{K}$-vector space is denoted by $\Hom_\mathbb{K}(V,W)$, or when the field $\mathbb{K}$ is clear from context, by $\Hom(V,W)$.

In particular, when $W=\mathbb{K}$, we call $\Hom(V,\mathbb{K})$ the *dual space* of $V$ and denote it by $V^\ast$. The elements of $V^\ast$ are called *linear functionals*.
:::

The zero vector in the vector space $\Hom(V,W)$ is the function $0$ sending every element to 0. ([§Linear Maps, ⁋Example 10](/en/math/linear_algebra/linear_map#ex10){: data-lid="a7fkx" }) When referring to this function, we shall call it the zero function for convenience.

Suppose both spaces $V,W$ are finite-dimensional, and let $\mathcal{B}=\{x_1,\ldots, x_n\}$ and $\mathcal{C}=\{y_1,\ldots, y_m\}$ be bases of $V,W$, respectively. From $\mathcal{B}$ to $W$, consider the $mn$ functions

$$f_i^j(x)=\begin{cases}y_j&\text{if $x=x_i$}\\0&\text{otherwise}\end{cases}$$

That is, $f_i^j$ is the function sending *only* the single element $x_i$ to $y_j$ and everything else to 0. Then by [Theorem 1](#thm1){: data-lid="bbbep" }, for $f_i^j=B_i^j\circ\iota$ to hold, there exists a unique linear map $B_i^j$.

::: Proposition 5
Suppose two finite-dimensional $\mathbb{K}$-vector spaces $V,W$ have bases $\{x_1,\ldots,x_n\}$ and $\{y_1,\ldots,y_m\}$, respectively. Then $\Hom(V,W)$ is an $mn$-dimensional vector space, and in this case the $mn$ linear maps $B_i^j$ above form a basis of $\Hom(V,W)$.
:::
::: Proof
It suffices to prove the claim about the basis.

First, the $B_i^j$ are linearly independent. For scalars $\alpha_{11},\ldots,\alpha_{mn}$, suppose

$$\alpha_{11}B_1^1+\alpha_{12}B_2^1+\cdots+\alpha_{mn}B_n^m=0$$

That is, both sides are the zero function from $V$ to $W$, and therefore for any $v\in V$ the equation

$$\alpha_{11}B_1^1(v)+\alpha_{12}B_2^1(v)+\cdots+\alpha_{mn}B_n^m(v)=0$$

holds. In particular, this equation also holds when $v=x_1,\ldots, x_n$, in which case

$$\alpha_{11}B_1^1(x_k)+\alpha_{12}B_2^1(x_k)+\cdots+\alpha_{mn}B_n^m(x_k)=0$$

But by the definition of $B_i^j$, $B_i^j(x_k)$ takes, only when $i=k$, the value $y_j$, so the above equation becomes

$$\alpha_{1k}y_1+\alpha_{2k}y_2+\cdots+\alpha_{mk}y_m=0$$

Now $y_1,\ldots,y_m$ are linearly independent, so $\alpha_{1k},\ldots,\alpha_{mk}$ are all $0$. Since $k$ can be chosen arbitrarily, $\alpha_{11},\ldots,\alpha_{mn}$ are all 0, and the $B_i^j$ are linearly independent.

On the other hand, these $B_i^j$ span $\Hom(V,W)$. Suppose an arbitrary $L\in\Hom(V,W)$ is given. Then we can find scalars $\alpha_{11},\ldots,\alpha_{mn}$ satisfying equation (1) from the introduction. Now, defined by the equation

$$L'(v)=\sum_{i,j}\alpha_{ji}B_i^j(v)$$

$L'$ is a linear map. Moreover, substituting $v=x_k$ gives

$$L'(x_k)=\sum_{i,j}\alpha_{ji}B_i^j(x_k)=\sum_{j=1}^m\alpha_{jk}B_k^j(x_k)=\sum_{j=1}^m\alpha_{jk}y_j=L(x_k)$$

Now by the uniqueness part of [Theorem 1](#thm1){: data-lid="nfvf9" }, $L'=L$ holds.
:::

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---
