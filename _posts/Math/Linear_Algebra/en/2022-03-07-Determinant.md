---
title: "Determinant"
description: "We define the determinant through the properties of multilinear and alternating multilinear maps, and based on this, we explore the existence of a matrix inverse and the meaning of eigenvalues and eigenvectors."
excerpt: "The definition and geometric meaning of the determinant"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/determinant
sidebar: 
    nav: "linear_algebra-en"


date: 2022-03-07

weight: 13
translated_at: 2026-05-31T20:30:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-15T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Our central question is this: given a matrix $A$, what information obtainable from $A$ uniquely determines $A$ up to similarity, that is, as a linear operator? The answer lies (almost) in the eigenvalues and eigenvectors of the matrix, and to define these we must first define the determinant. 

## Definition of the Determinant

The determinant we will define is, for an $n$-th order square matrix $A$, the corresponding scalar $\det A$, and algebraically, the determinant can be viewed as a scalar that determines, according to whether its value is $0$ or not, the existence of $A^{-1}$. There are several ways to compute the determinant, and some of these are even taken as definitions, but none of them captures the essential meaning of the determinant. We first define the determinant properly, and then introduce its computation in the course of proving its existence.

The determinant is a function from $\Mat_n(\mathbb{K})$ to $\mathbb{K}$. Now, if we regard each matrix in $\Mat_n(\mathbb{K})$ as a collection of vectors in $\mathbb{K}^n$, $n$ in number, the determinant becomes a function from $(\mathbb{K}^n)^n$ (that is, the space obtained by taking the product of the vector space $\mathbb{K}^n$ $n$ times) to $\mathbb{K}$. Therefore, for any matrix $A\in\Mat_n(\mathbb{K})$, we denote the determinant of $A$ by $\det(A)$, and at the same time, using the column vectors of $A$, also denote it by $\det(A_1,\ldots, A_n)$. This is equivalent to identifying the two $n^2$-dimensional $\mathbb{K}$-vector spaces $\Mat_n(\mathbb{K})$ and $(\mathbb{K}^n)^n\cong \mathbb{K}^{n^2}$ via the following isomorphism

$$A=(A_1\quad A_2\quad\cdots\quad A_n)\cong (A_1, A_2, \cdots, A_n)\cong \bigl((A_{11}, A_{21}, \ldots, A_{n1}), (A_{12},A_{22},\ldots, A_{n2}),\ldots, (A_{1n},A_{2n},\ldots, A_{nn})\bigr)$$

::: Definition 1
For $\mathbb{K}$-vector spaces $V,W$, the following function

$$f:\underbrace{V\times\cdots\times V}_\text{ {\footnotesize $n$} times}\rightarrow W$$

is called a *multilinear map* if $f$ is linear in each component.
:::

In particular, when $n=2$, we call $f$ *bilinear*. 

::: Definition 2
Let two $\mathbb{K}$-vector spaces $V,W$ and a multilinear map 

$$f: \underbrace{V\times\cdots\times V}_\text{ {\footnotesize $n$} times}\rightarrow W$$

be given. If for any $v_1,\ldots, v_n$ and any $i\neq j$ we always have $f(v_1,\ldots, v_n)=0$ whenever $v_i=v_j$, then $f$ is called an *alternating multilinear map*.
:::

As above, let a multilinear map $f:V\times\cdots\times V\rightarrow W$ be given. Then $f$ is said to be *antisymmetric* if for any $v_1,\ldots, v_n$ and any $i\neq j$ the following equation

$$f(v_1,\ldots, v_i, \ldots, v_j,\ldots, v_n)=-f(v_1,\ldots, v_j,\ldots, v_i,\ldots, v_n)$$

holds.

::: Proposition 3
An alternating multilinear map is antisymmetric.
:::
::: Proof
Let $f$ be alternating. For any $v_1,\ldots, v_n$ and any $i\neq j$, the fact that $f$ is alternating gives the equation

$$f(v_1,\ldots, v_i+v_j,\ldots, v_i+v_j,\ldots, v_n)=0$$

where $v_i+v_j$ appears in the $i,j$-th components, respectively. Now applying multilinearity, the above equation becomes

$$\begin{aligned}0&=f(v_1,\ldots, v_i,\ldots, v_i,\ldots, v_n)+f(v_1,\ldots, v_i,\ldots, v_j,\ldots,v_n)\\&\phantom{==}+f(v_1,\ldots, v_j,\ldots, v_i,\ldots,v_n)+f(v_1,\ldots, v_j,\ldots, v_j,\ldots, v_n)\end{aligned}$$

and since $f$ is again alternating, the first and last terms (in which $v_i, v_j$ each appear twice) become $0$. From this, we obtain the desired conclusion.
:::

If $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, the converse of the above proposition also holds. Let $f$ be antisymmetric. Then for any $v_1,\ldots, v_n\in V$ with $v_i=v_j$,

$$\begin{aligned}f(v_1,\ldots,v_i,\ldots, v_j,\ldots, v_n)&=f(v_1,\ldots, v_j,\ldots,v_i,\ldots, v_n)\\&=-f(v_1,\ldots, v_i,\ldots, v_j,\ldots, v_n)\end{aligned}$$

holds, so $2f(v_1,\ldots, v_n)=0$, and dividing both sides by $2$ gives $f(v_1,\ldots, v_n)=0$. (The first equality uses the fact that $v_i=v_j$, and the second uses the fact that $f$ is antisymmetric.)

Meanwhile, suppose $f$ is an alternating multilinear map in $n$ variables and one of $v_1,\ldots, v_n$ is a linear combination of the other $n-1$ vectors. Then applying multilinearity expresses $f(v_1,\ldots, v_n)$ as a sum of terms in which some vector appears twice, so from the fact that $f$ is alternating we see that $f(v_1,\ldots, v_n)=0$.

We are now in a position to define the determinant.

::: Definition 4
An alternating multilinear map satisfying $D(e_1,\ldots, e_n)=1$, $D:(\mathbb{K}^n)^n\rightarrow \mathbb{K}$, is called the *determinant*.
:::

Since we have not yet shown that the determinant exists or that it is unique, instead of $\det$ we have used the notation $D$. In the next post we introduce the computation of the determinant and prove this, and thereafter we use the standard notation $\det$.

## Area and Volume

The area of a parallelogram is given by the length of its base multiplied by its height. Similarly, the volume of a parallelepiped is given by the area of its base multiplied by its height. It is also not difficult to generalize this to higher dimensions. For convenience, we also refer to the *hypervolume* of figures in four or more dimensions simply as volume.

The above definition is likewise merely one way of finding the area of these figures. Giving the correct definition of area and volume is what endows the determinant with geometric meaning.

Suppose $n$ linearly independent vectors in $n$-dimensional space are given. Then they form an $n$-dimensional parallelepiped. For example, when $n=3$, three vectors $v_1,v_2,v_3$ form a parallelepiped as follows.

{% diagram Math/Linear_Algebra/Determinant-1.svg width="16em" alt="parallelepiped" %}

For convenience of exposition, all subsequent discussion will be explained using area in two dimensions, but it is not difficult to generalize all of this to $n$-dimensional space.

First, we must define which parallelogram has unit area 1. Of course there is considerable freedom here, but the most reasonable way is to define a square of side length 1 as the parallelogram having unit area 1.

{% diagram Math/Linear_Algebra/Determinant-2.svg width="5em" alt="Square" %}

On the other hand, it is clear that starting from the above square and applying the following two rules, we can obtain all[^1] parallelograms.

1. Shear: a transformation fixing one side of a parallelogram and translating the endpoint of the remaining side in the direction of the fixed side.
2. A transformation that scales the length of the remaining side by a factor of $k>0$ while keeping one side fixed.

{% diagram Math/Linear_Algebra/Determinant-3.svg width="22em" alt="Transformation" %}

Therefore, if we define only how the area changes when a parallelogram is transformed according to rules 1 and 2, this defines the area of all parallelograms. In case 1, we define the area to remain unchanged; in case 2, we define the area to be multiplied by $k$. With this definition, the area of every parallelogram coincides with the area of a parallelogram as we previously knew it.[^2]

## Geometric Meaning of the Determinant

To lend geometric intuition to the determinant, in this section we take $\mathbb{K}=\mathbb{R}$. Apart from the fact that $D$ may take a negative sign, we may view $D$ as an area function. In this setting, the sign of $D$ represents *orientation*.

First, the first condition that $D$ must satisfy, namely that the area of the unit square is 1, is obtained from the definition of the determinant, $D(e_1,\ldots, e_n)=1$.

In the usual notion of area, multiplying the length of one side of a parallelogram by $-1$ still yields a positive area. However, if we regard this figure as having the opposite orientation from the original figure, we can also view the area as negative; then we can verify that $D$ preserves arbitrary scalar multiplication of the length of one side, and considering shear transformations, $D$ also preserves the result of adding two vectors corresponding to one side, as follows.

{% diagram Math/Linear_Algebra/Determinant-4.svg width="12em" alt="Multilinearity" %}

Moreover, considering shear transformations, for a fixed side $v_n$, adding a linear combination of the $n-1$ vectors $v_1,\ldots, v_{n-1}$ forming the base to $v_n$ preserves the value of $D$. This means that if $v_n$ is a linear combination of $v_1,\ldots, v_{n-1}$, then $D(v_1,\ldots, v_n)=0$, and this is equivalent to $D$ being alternating.

We have not yet proved the uniqueness of the determinant, but we can verify that [Definition 4](#def4){: data-lid="8h1fc" } completely determines it; thus we may think of the determinant as signed volume. Now in this picture, we can see that the reason the determinant being $0$ is equivalent to $A$ being non-invertible is that in $n$-dimensional space, the volume of a parallelepiped of dimension less than $n$ is always 0.

In the next post we actually show that the determinant exists uniquely. Through this we will learn various computational methods for the determinant.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  

---

[^1]: Congruent parallelograms are treated as identical.
[^2]: Strictly speaking, we have not verified that area is well-defined. For example, even if there are several ways to produce a given parallelogram from the unit square through processes 1 and 2, we must check that the area defined above is the same. We leave this to intuition and move on.
