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
last_polished_at: 2026-05-31T20:30:05+00:00
---
Our central question is this: given a matrix $$A$$, what information obtainable from $$A$$ determines $$A$$ uniquely up to $$\sim$$—that is, as a linear operator? The answer lies (almost entirely) in the eigenvalues and eigenvectors of the matrix, and to define these we must first define the determinant.

## Definition of the Determinant

The determinant we will define is a scalar $$\det A$$ associated to an $$n\times n$$ square matrix $$A$$. Algebraically, the determinant can be viewed as the scalar that determines whether $$A^{-1}$$ exists according to whether its value is zero or nonzero. There are several ways to compute the determinant, and some of these are taken as definitions, but none of them captures the essential meaning of the determinant. We first give the proper definition of the determinant, and then introduce its computation in the course of proving existence.

The determinant is a function from $$\Mat_n(\mathbb{K})$$ to $$\mathbb{K}$$. Regarding each matrix in $$\Mat_n(\mathbb{K})$$ as a collection of $$n$$ vectors in $$\mathbb{K}^n$$, the determinant becomes a function from $$(\mathbb{K}^n)^n$$—that is, the $$n$$-fold product of the vector space $$\mathbb{K}^n$$—to $$\mathbb{K}$$. Thus, for any matrix $$A\in\Mat_n(\mathbb{K})$$, we denote the determinant of $$A$$ by $$\det(A)$$, and simultaneously write $$\det(A_1,\ldots, A_n)$$ using the column vectors of $$A$$. This is equivalent to identifying the two $$n^2$$-dimensional $$\mathbb{K}$$-vector spaces $$\Mat_n(\mathbb{K})$$ and $$(\mathbb{K}^n)^n\cong \mathbb{K}^{n^2}$$ via the isomorphism

$$A=(A_1\;A_2\;\cdots\;A_n)\cong (A_1, A_2, \cdots, A_n)\cong \bigl((A_{11}, A_{21}, \ldots, A_{n1}), (A_{12},A_{22},\ldots, A_{n2}),\ldots, (A_{1n},A_{2n},\ldots, A_{nn})\bigr)$$

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For $$\mathbb{K}$$-vector spaces $$V,W$$, a function

$$f:\underbrace{V\times\cdots\times V}_\text{ {\footnotesize $n$} times}\rightarrow W$$

is called a *multilinear map* if $$f$$ is linear in each component.

</div>

In particular, when $$n=2$$, we say $$f$$ is *bilinear*.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Let two $$\mathbb{K}$$-vector spaces $$V,W$$ and a multilinear map

$$f: \underbrace{V\times\cdots\times V}_\text{ {\footnotesize $n$} times}\rightarrow W$$

be given. If for any $$v_1,\ldots, v_n$$ and any $$i\neq j$$ the identity

$$f(v_1,\ldots, v_i, \ldots, v_j,\ldots, v_n)=-f(v_1,\ldots, v_j,\ldots, v_i,\ldots, v_n)$$

always holds, then we call $$f$$ an *alternating multilinear map*.

</div>

As above, let a multilinear map $$f:V\times\cdots\times V\rightarrow W$$ be given. Then $$f$$ is *antisymmetric* if for any $$v_1,\ldots, v_n$$ and any $$i\neq j$$, whenever $$v_i=v_j$$ we have $$f(v_1,\ldots, v_n)=0$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> A multilinear map $$f:V\times\cdots\times V\rightarrow W$$ is alternating if and only if it is antisymmetric.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, assume that $$f$$ is alternating. Then for any $$v_1,\ldots, v_n\in V$$ satisfying $$v_i=v_j$$,

$$\begin{aligned}f(v_1,\ldots,v_i,\ldots, v_j,\ldots, v_n)&=f(v_1\ldots, v_j,\ldots,v_i,\ldots, v_n)\\&=-f(v_1,\ldots, v_i,\ldots, v_j,\ldots, v_n)\end{aligned}$$

holds, so $$f$$ is also antisymmetric. (The first equality uses $$v_i=v_j$$, and the second uses the fact that $$f$$ is alternating.)

Conversely, assume that $$f$$ is antisymmetric. For any $$v_1,\ldots, v_n$$ and any $$i\neq j$$, antisymmetry gives

$$f(v_1,\ldots, v_i+v_j,\ldots, v_i+v_j,\ldots, v_n)=0$$

where $$v_i+v_j$$ appears in the $$i$$th and $$j$$th components. Applying multilinearity, this becomes

$$\begin{aligned}0&=f(v_1,\ldots, v_i,\ldots, v_i,\ldots, v_n)+f(v_1,\ldots, v_i,\ldots, v_j,\ldots,v_n)\\&\phantom{==}+f(v_1,\ldots, v_j,\ldots, v_i,\ldots,v_n)+f(v_1,\ldots, v_j,\ldots, v_j,\ldots, v_n)\end{aligned}$$

and since $$f$$ is antisymmetric, the first and last terms—in which $$v_i$$ and $$v_j$$ each appear twice—vanish. The desired conclusion follows.

</details>

In particular, suppose $$f$$ is an alternating multilinear map in $$n$$ variables and one of $$v_1,\ldots, v_n$$ is a linear combination of the other $$n-1$$ vectors. Then applying multilinearity followed by the proposition above, we see that $$f(v_1,\ldots, v_n)=0$$.

We are now in a position to define the determinant.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> An alternating multilinear map $$D:(\mathbb{K}^n)^n\rightarrow \mathbb{K}$$ satisfying $$D(e_1,\ldots, e_n)=1$$ is called the *determinant*.

</div>

We have not yet shown that the determinant exists or is unique, so we have used the notation $$D$$ rather than $$\det$$. In the next post we introduce the computation of the determinant and prove both claims, after which we adopt the standard notation $$\det$$.

## Area and Volume

The area of a parallelogram is given by the length of its base multiplied by its height. Similarly, the volume of a parallelepiped is given by the area of its base multiplied by its height. It is not difficult to generalize this to higher dimensions as well. For convenience, we also refer to the <em-ko>hypervolume</em-ko> of figures in four or more dimensions simply as volume.

The above is likewise merely one way of computing the areas of these figures. Giving the correct definition of area and volume is what endows the determinant with geometric meaning.

Suppose $$n$$ linearly independent vectors in $$n$$-dimensional space are given. Then they span an $$n$$-dimensional parallelepiped. For example, when $$n=3$$, three vectors $$v_1,v_2,v_3$$ form a parallelepiped as follows.

![parallelepiped](/assets/images/Math/Linear_Algebra/Determinant-1.svg){:style="width:16em" class="invert" .align-center}

For convenience of exposition, all subsequent discussion will use area in the plane, but it is not difficult to generalize everything to $$n$$-dimensional space.

First, we must define which parallelogram has unit area 1. Of course there is considerable freedom here, but the most reasonable choice is to define a square of side length 1 as the parallelogram of unit area 1.

![Square](/assets/images/Math/Linear_Algebra/Determinant-2.svg){:style="width:5em" class="invert" .align-center}

On the other hand, it is clear that starting from the above square and applying the following two rules, we can obtain all[^1] parallelograms.

1. Shear: a transformation fixing one side of a parallelogram and translating the endpoint of the remaining side parallel to the fixed side.
2. A transformation that scales the length of the remaining side by a factor of $$k>0$$ while keeping one side fixed.

![Transformation](/assets/images/Math/Linear_Algebra/Determinant-3.svg){:style="width:22em" class="invert" .align-center}

Therefore, if we specify only how area changes under the deformations in rules 1 and 2, we have defined the area of all parallelograms. In case 1, we define the area to remain unchanged; in case 2, we define the area to be multiplied by $$k$$. With these definitions, the area of every parallelogram coincides with the familiar formula.[^2]

## Geometric Meaning of the Determinant

To lend geometric intuition to the determinant, in this section we take $$\mathbb{K}=\mathbb{R}$$. Apart from the fact that $$D$$ may take a negative sign, we may view $$D$$ as an area function. In this setting, the sign of $$D$$ represents <em-ko>orientation</em-ko>.

First, the initial condition that $$D$$ must satisfy—namely, <phrase>the area of the unit square is 1</phrase>—is immediate from the definition $$D(e_1,\ldots, e_n)=1$$.

In the usual notion of area, multiplying the length of one side of a parallelogram by $$-1$$ still yields a positive area. However, if we regard the resulting figure as having the opposite orientation from the original, we may view the area as negative; then one verifies that $$D$$ preserves arbitrary scalar multiplication of the length of one side, and considering shear transformations, $$D$$ also preserves the sum of two vectors corresponding to one side, as illustrated below.

![Multilinearity](/assets/images/Math/Linear_Algebra/Determinant-4.svg){:style="width:12em" class="invert" .align-center}

Moreover, considering shear transformations, for a fixed side $$v_n$$, adding to $$v_n$$ any linear combination of the $$n-1$$ base vectors $$v_1,\ldots, v_{n-1}$$ preserves the value of $$D$$. This means that if $$v_n$$ is a linear combination of $$v_1,\ldots, v_{n-1}$$ then $$D(v_1,\ldots, v_n)=0$$, and hence by [Proposition 3](#prop3) this is equivalent to $$D$$ being alternating.

We have not yet proved the uniqueness of the determinant, but we can verify that [Definition 4](#def4) completely determines it; thus we may think of the determinant as signed volume. From this picture, we can also see why the determinant being $$0$$ is equivalent to $$A$$ being non-invertible: in $$n$$-dimensional space, the volume of a parallelepiped of dimension less than $$n$$ is always 0.

In the next post we actually show that the determinant exists uniquely. Through this we will learn various computational methods for the determinant.

---

**References**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  

---

[^1]: Congruent parallelograms are treated as identical.
[^2]: Strictly speaking, we have not verified that area is well-defined. For example, even if there are several ways to produce a given parallelogram from the unit square through processes 1 and 2, we must check that the area defined above is the same in each case. We leave this to intuition.
