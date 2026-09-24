---
title: "Fundamental Theorem of Linear Algebra"
description: "Demonstrates that linear maps on Euclidean spaces and matrices not only have the same dimension, but actually form the same space through a natural isomorphism."
excerpt: "Fundamental theorem of linear algebra"

categories: [Math / Linear Algebra]
permalink: /en/math/linear_algebra/ftla
sidebar: 
    nav: "linear_algebra-en"


date: 2021-10-16

weight: 11
translated_at: 2026-09-24T23:15:05+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In the previous post, we saw that for two $\mathbb{K}$-vector spaces $V,W$ of dimension $n$ and $m$ respectively, $\Hom(V,W)$ is an $mn$-dimensional $\mathbb{K}$-vector space. Moreover, the space of $m\times n$ matrices $\Mat_{m\times n}(\mathbb{K})$ is also an $mn$-dimensional $\mathbb{K}$-vector space. Then, from [§Isomorphisms, ⁋Corollary 4](/en/math/linear_algebra/isomorphic_vector_spaces#cor4){: data-lid="vpa9k" }, we know that these two vector spaces are isomorphic.

The fundamental theorem of linear algebra[^1], which we will prove in this post, establishes that not only are they isomorphic simply because they are vector spaces of the same dimension, but there exists a *natural* isomorphism between them, proving that the two are in fact the same space.

## Fundamental Theorem: Euclidean Spaces

In [§Space of Linear Maps](/en/math/linear_algebra/space_of_linear_maps){: data-lid="wljxb" }, we agreed to understand a linear map $L$ satisfying the equations

$$\begin{aligned}L(x_1)&=\alpha_{11}y_1+\alpha_{21}y_2+\cdots+\alpha_{m1}y_m\\L(x_2)&=\alpha_{12}y_1+\alpha_{22}y_2+\cdots+\alpha_{m2}y_m\\&\phantom{a}\vdots\\L(x_n)&=\alpha_{1n}y_1+\alpha_{2n}y_2+\cdots+\alpha_{mn}y_m\end{aligned}$$

as the correspondence

$$v=\sum_{i=1}^n v_ix_i\quad\mapsto\quad \sum_{j=1}^m\left(\sum_{i=1}^n\alpha_{ji}v_i\right)y_j=L(v)\tag{1}$$

In particular, if $V=\mathbb{K}^n$, $W=\mathbb{K}^m$, and standard bases $\mathcal{E}_n=\{e_1,\ldots, e_n\},\mathcal{E}_m=\{e_1,\ldots,e_m\}$ are given on each of them, then the above correspondence can be written as

$$\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix}\quad\mapsto\quad\begin{pmatrix}\sum_{i=1}^n\alpha_{1i}v_i\\\sum_{i=1}^n\alpha_{2i}v_i\\\vdots\\\sum_{i=1}^n\alpha_{mi}v_i\end{pmatrix}$$

However, the right-hand side has precisely the form of the matrix-vector product

$$\begin{pmatrix}\alpha_{11}&\alpha_{12}&\cdots&\alpha_{1n}\\\alpha_{21}&\alpha_{22}&\cdots&\alpha_{2n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m1}&\alpha_{m2}&\cdots&\alpha_{mn}\end{pmatrix}\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix}\tag{2}$$

The $m\times n$ matrix in the equation above is called the *matrix representation* of $L$ with respect to $\mathcal{E}_n,\mathcal{E}_m$, and is denoted by $[L]^{\mathcal{E}_n}_{\mathcal{E}_m}$.

Conversely, we can verify that an $m\times n$ matrix specifies a linear map in the exact same manner.

::: Example 1
Consider the Euclidean $n$-space $\mathbb{K}^n$ and a matrix $A\in\Mat_{m\times n}(\mathbb{K})$. For any $x\in\mathbb{K}^n$, if we define $L_A(x)$ by the equation

$$L_A(x)=Ax$$

then $L_A$ becomes a linear map from $\mathbb{K}^n$ to $\mathbb{K}^m$.
:::

Suppose an arbitrary linear map $L$ from $\mathbb{K}^n$ to $\mathbb{K}^m$ is given. It is not difficult to check that $L=L_{[L]^{\mathcal{E}_n}_{\mathcal{E}_m}}$. Therefore, the following correspondence exists:

$$\{\text{linear maps from $\mathbb{K}^n$ to $\mathbb{K}^m$}\}\longleftrightarrow\Mat_{m\times n}(\mathbb{K})$$

More precisely, $L\mapsto [L]^{\mathcal{E}_n}_{\mathcal{E}_m}$ and $A\mapsto L_A$ (the definition in [Example 1](#ex1){: data-lid="ol3cg" }) are bijections that are inverses of each other.

However, since the set on the left is equal to $\Hom(\mathbb{K}^n, \mathbb{K}^m)$, we can ask whether this correspondence is a bijective linear map, that is, an isomorphism. The answer is affirmative, and together with [Theorem 3](#thm3){: data-lid="e4c78" } below, this result is called the fundamental theorem of linear algebra.

::: Theorem 2
$$\Hom(\mathbb{K}^n,\mathbb{K}^m)\cong\Mat_{m\times n}(\mathbb{K})$$
:::
::: Proof
We must show that the given map $L\mapsto[L]^{\mathcal{E}_n}_{\mathcal{E}_m}$ is linear.

Let $L_1,L_2$ both be elements of $\Hom(\mathbb{K}^n,\mathbb{K}^m)$. Then, for each $e_i\in\mathcal{E}_n$,

$$\begin{aligned}L_1(e_1)&=\alpha_{1,1}e_1+\alpha_{2,1}e_2+\cdots+\alpha_{m,1}e_m\\L_1(e_2)&=\alpha_{1,2}e_1+\alpha_{2,2}e_2+\cdots+\alpha_{m,2}e_m\\&\vdots\\L_1(e_n)&=\alpha_{1,n}e_1+\alpha_{2,n}e_2+\cdots+\alpha_{m,n}e_m\end{aligned}$$

and

$$\begin{aligned}L_2(e_1)&=\beta_{1,1}e_1+\beta_{2,1}e_2+\cdots+\beta_{m,1}e_m\\L_2(e_2)&=\beta_{1,2}e_1+\beta_{2,2}e_2+\cdots+\beta_{m,2}e_m\\&\vdots\\L_2(e_n)&=\beta_{1,n}e_1+\beta_{2,n}e_2+\cdots+\beta_{m,n}e_m\end{aligned}$$

for some families of scalars $(\alpha_{i,j})$ and $(\beta_{i,j})$. Now,

$$\begin{aligned}(L_1+L_2)(e_1)&=(\alpha_{1,1}+\beta_{1,1})e_1+(\alpha_{2,1}+\beta_{2,1})e_2+\cdots+(\alpha_{m,1}+\beta_{m,1})e_m\\(L_1+L_2)(e_2)&=(\alpha_{1,2}+\beta_{1,2})e_1+(\alpha_{2,2}+\beta_{2,2})e_2+\cdots+(\alpha_{m,2}+\beta_{m,2})e_m\\&\vdots\\(L_1+L_2)(e_n)&=(\alpha_{1,n}+\beta_{1,n})e_1+(\alpha_{2,n}+\beta_{2,n})e_2+\cdots+(\alpha_{m,n}+\beta_{m,n})e_m\end{aligned}$$

and hence the matrix representation of $L_1+L_2$, $[L_1+L_2]^{\mathcal{E}_n}_{\mathcal{E}_m}$, is precisely $[L_1]^{\mathcal{E}_n}_{\mathcal{E}_m}+[L_2]^{\mathcal{E}_n}_{\mathcal{E}_m}$. Similarly, this also holds for scalar multiplication.
:::

Furthermore, the product of matrices also has a special meaning in $\Hom(\mathbb{K}^n,\mathbb{K}^m)$.

::: Theorem 3
Let three Euclidean spaces $\mathbb{K}^n,\mathbb{K}^m,\mathbb{K}^k$ be given. Then for any $L_1:\mathbb{K}^n\rightarrow \mathbb{K}^m$ and $L_2:\mathbb{K}^m\rightarrow \mathbb{K}^k$,

$$[L_2\circ L_1]^{\mathcal{E}_n}_{\mathcal{E}_k}=[L_2]^{\mathcal{E}_m}_{\mathcal{E}_k}[L_1]^{\mathcal{E}_n}_{\mathcal{E}_m}$$

always holds. That is, the composition of linear maps corresponds to the product of matrices. 
:::
::: Proof
To determine $[L_2\circ L_1]^{\mathcal{E}_n}_{\mathcal{E}_k}$ on the left-hand side, we only need to check where $L_2\circ L_1$ sends the elements of $\mathcal{E}_n$, $e_i$. Suppose that $L_1$ and $L_2$ are given by the equations

$$[L_1]^{\mathcal{E}_n}_{\mathcal{E}_m}=\begin{pmatrix}\alpha_{1,1}&\alpha_{1,2}&\cdots&\alpha_{1,n}\\\alpha_{2,1}&\alpha_{2,2}&\cdots&\alpha_{2,n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m,1}&\alpha_{m,2}&\cdots&\alpha_{m,n}\end{pmatrix},\quad[L_2]^{\mathcal{E}_m}_{\mathcal{E}_k}=\begin{pmatrix}\beta_{1,1}&\beta_{1,2}&\cdots&\beta_{1,m}\\\beta_{2,1}&\beta_{2,2}&\cdots&\beta_{2,m}\\\vdots&\vdots&\ddots&\vdots\\\beta_{k,1}&\beta_{k,2}&\cdots&\beta_{k,m}\end{pmatrix}$$

With a short calculation,

$$\begin{aligned}(L_2\circ L_1)(e_i)&=L_2(\alpha_{1,i}e_1+\cdots+\alpha_{m,i}e_m)\\&=\alpha_{1,i}L_2(e_1)+\alpha_{2,i}L_2(e_2)+\cdots+\alpha_{m,i}L_2(e_m)\\&=\alpha_{1,i}(\beta_{1,1}e_1+\beta_{2,1}e_2+\cdots+\beta_{k,1}e_k)\\&\phantom{==}+\alpha_{2,i}(\beta_{1,2}e_1+\beta_{2,2}e_2+\cdots+\beta_{k,2}e_k)\\&\phantom{===}+\cdots\\&\phantom{====}+\alpha_{m,i}(\beta_{1,m}e_1+\beta_{2,m}e_2+\cdots+\beta_{k,m}e_k)\end{aligned}$$

Now grouping the above expression by the basis vectors of $\mathbb{K}^k$, $e_1,\ldots, e_k$,

$$(L_2\circ L_1)(e_i)=\left(\sum_{l=1}^m\alpha_{l,i}\beta_{1,l}\right)e_1+\cdots+\left(\sum_{l=1}^m\alpha_{l,i}\beta_{k,l}\right)e_k.$$

Because in $[L_2\circ L_1]^{\mathcal{E}_n}_{\mathcal{E}_k}$ the $i$-th column is the vector to which $e_i$ is mapped by $L_2\circ L_1$, the entry of the matrix $[L_2\circ L_1]^{\mathcal{E}_n}_{\mathcal{E}_k}$ in column $i$ and row $j$ is the $j$-th component $\sum_{l=1}^m\alpha_{l,i}\beta_{j,l}$ of this vector. Now, from the calculation immediately following [§Matrices, ⁋Definition 2](/en/math/linear_algebra/matrices#def2){: data-lid="km9ia" }, we see that in the product of the two matrices $[L_2]_{\mathcal{E}_k}^{\mathcal{E}_m}$ and $[L_1]_{\mathcal{E}_m}^{\mathcal{E}_n}$, this is the $(j,i)$ component.
:::

## Fundamental Theorem: General Case

Although the fundamental theorem we proved earlier applies only to Euclidean spaces, with only a minor modification it also holds for general finite-dimensional $\mathbb{K}$-vector spaces. This process can be simply summarized by the following diagram.

{% diagram Math/Linear_Algebra/Fundamental_Theorem_of_Linear_Algebra-1.svg width="14.02em" alt="FTLA" %}

The *coordinate representation* defined for an arbitrary finite-dimensional $\mathbb{K}$-vector space $V$ and its basis $\mathcal{B}=\{x_1,\ldots, x_n\}$ is the isomorphism

$$v=\sum_{i=1}^n v_ix_i\mapsto [v]_\mathcal{B}=\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix}\in\mathbb{K}^n$$

Similarly, suppose that another finite-dimensional $\mathbb{K}$-vector space $W$ and its basis $\mathcal{C}=\{y_1,\ldots, y_m\}$ are given, and that a linear map $L:V\rightarrow W$ is determined by the equations

$$\begin{aligned}L(x_1)&=\alpha_{1,1}y_1+\alpha_{2,1}y_2+\cdots+\alpha_{m,1}y_m\\L(x_2)&=\alpha_{1,2}y_1+\alpha_{2,2}y_2+\cdots+\alpha_{m,2}y_m\\&\vdots\\L(x_n)&=\alpha_{1,n}y_1+\alpha_{2,n}y_2+\cdots+\alpha_{m,n}y_m\end{aligned}$$

Then, with respect to $\mathcal{B},\mathcal{C}$, we this time define the *matrix representation* of $L$, $[L]^\mathcal{B}_\mathcal{C}$, by the equation

$$[L]^\mathcal{B}_\mathcal{C}=\begin{pmatrix}\alpha_{1,1}&\alpha_{1,2}&\cdots&\alpha_{1,n}\\\alpha_{2,1}&\alpha_{2,2}&\cdots&\alpha_{2,n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m,1}&\alpha_{m,2}&\cdots&\alpha_{m,n}\end{pmatrix}$$

Now, comparing equation (2) and equation (1), we can verify that for any $v\in V$, the coordinate representation of $L(v)$ with respect to $\mathcal{C}$ is given by

$$[L(v)]_\mathcal{C}=[L]^\mathcal{B}_\mathcal{C}[v]_\mathcal{B}\tag{3}$$

Then the general version of [Theorem 2](#thm2){: data-lid="ty7pq" } is given by the following theorem.

::: Theorem 4
For an $n$-dimensional $\mathbb{K}$-vector space $V$ and an $m$-dimensional $\mathbb{K}$-vector space $W$, $\Hom(V,W)\cong \Mat_{m\times n}(\mathbb{K})$.
:::
::: Proof
For $V$ and $W$, fix bases $\mathcal{B}$ and $\mathcal{C}$, respectively. We need to show that the map $L\mapsto[L]^\mathcal{B}_\mathcal{C}$ is linear.

Suppose $L_1,L_2$ are both elements of $\Hom(V,W)$. Then for each $x_i\in\mathcal{B}$, 

$$\begin{aligned}L_1(x_1)&=\alpha_{1,1}y_1+\alpha_{2,1}y_2+\cdots+\alpha_{m,1}y_m\\L_1(x_2)&=\alpha_{1,2}y_1+\alpha_{2,2}y_2+\cdots+\alpha_{m,2}y_m\\&\vdots\\L_1(x_n)&=\alpha_{1,n}y_1+\alpha_{2,n}y_2+\cdots+\alpha_{m,n}y_m\end{aligned}$$

and

$$\begin{aligned}L_2(x_1)&=\beta_{1,1}y_1+\beta_{2,1}y_2+\cdots+\beta_{m,1}y_m\\L_2(x_2)&=\beta_{1,2}y_1+\beta_{2,2}y_2+\cdots+\beta_{m,2}y_m\\&\vdots\\L_2(x_n)&=\beta_{1,n}y_1+\beta_{2,n}y_2+\cdots+\beta_{m,n}y_m\end{aligned}$$

there exist families of scalars $(\alpha_{i,j})$ and $(\beta_{i,j})$ satisfying these equations. Now, 

$$\begin{aligned}(L_1+L_2)(x_1)&=(\alpha_{1,1}+\beta_{1,1})y_1+(\alpha_{2,1}+\beta_{2,1})y_2+\cdots+(\alpha_{m,1}+\beta_{m,1})y_m\\(L_1+L_2)(x_2)&=(\alpha_{1,2}+\beta_{1,2})y_1+(\alpha_{2,2}+\beta_{2,2})y_2+\cdots+(\alpha_{m,2}+\beta_{m,2})y_m\\&\vdots\\(L_1+L_2)(x_n)&=(\alpha_{1,n}+\beta_{1,n})y_1+(\alpha_{2,n}+\beta_{2,n})y_2+\cdots+(\alpha_{m,n}+\beta_{m,n})y_m\end{aligned}$$

and hence the matrix representation of $L_1+L_2$, denoted $[L_1+L_2]^\mathcal{B}_\mathcal{C}$, is precisely $[L_1]^\mathcal{B}_\mathcal{C}+[L_2]^\mathcal{B}_\mathcal{C}$. Similarly, the same holds for scalar multiplication.
:::

[Theorem 3](#thm3){: data-lid="y9mfy" } also has a similar generalization.

::: Theorem 5
Suppose we are given three $\mathbb{K}$-vector spaces $V_1,V_2,V_3$ and their respective bases $\mathcal{B}_1=\{x_1,\ldots,x_n\}$, $\mathcal{B}_2=\{y_1,\ldots, y_m\}$, and $\mathcal{B}_3=\{z_1,\ldots, z_k\}$. Then for any $L_1:V_1\rightarrow V_2$ and $L_2:V_2\rightarrow V_3$,

$$[L_2\circ L_1]^{\mathcal{B}_1}_{\mathcal{B}_3}=[L_2]^{\mathcal{B}_2}_{\mathcal{B}_3}[L_1]^{\mathcal{B}_1}_{\mathcal{B}_2}$$

always holds. That is, the composition of linear maps corresponds to the product of matrices. 
:::
::: Proof
To determine $[L_2\circ L_1]^{\mathcal{B}_1}_{\mathcal{B}_3}$ on the left-hand side, we only need to check where $L_2\circ L_1$ sends the elements of $\mathcal{B}_1$. Suppose $L_1$ and $L_2$ are given by the following expressions:

$$[L_1]^{\mathcal{B}_1}_{\mathcal{B}_2}=\begin{pmatrix}\alpha_{1,1}&\alpha_{1,2}&\cdots&\alpha_{1,n}\\\alpha_{2,1}&\alpha_{2,2}&\cdots&\alpha_{2,n}\\\vdots&\vdots&\ddots&\vdots\\\alpha_{m,1}&\alpha_{m,2}&\cdots&\alpha_{m,n}\end{pmatrix},\quad[L_2]^{\mathcal{B}_2}_{\mathcal{B}_3}=\begin{pmatrix}\beta_{1,1}&\beta_{1,2}&\cdots&\beta_{1,m}\\\beta_{2,1}&\beta_{2,2}&\cdots&\beta_{2,m}\\\vdots&\vdots&\ddots&\vdots\\\beta_{k,1}&\beta_{k,2}&\cdots&\beta_{k,m}\end{pmatrix}$$

With a straightforward computation,

$$\begin{aligned}(L_2\circ L_1)(x_i)&=L_2(\alpha_{1,i}y_1+\cdots+\alpha_{m,i}y_m)\\&=\alpha_{1,i}L_2(y_1)+\alpha_{2,i}L_2(y_2)+\cdots+\alpha_{m,i}L_2(y_m)\\&=\alpha_{1,i}(\beta_{1,1}z_1+\beta_{2,1}z_2+\cdots+\beta_{k,1}z_k)\\&\phantom{==}+\alpha_{2,i}(\beta_{1,2}z_1+\beta_{2,2}z_2+\cdots+\beta_{k,2}z_k)\\&\phantom{===}+\cdots\\&\phantom{====}+\alpha_{m,i}(\beta_{1,m}z_1+\beta_{2,m}z_2+\cdots+\beta_{k,m}z_k)\end{aligned}$$

Now, grouping the terms by $z$, 

$$(L_2\circ L_1)(x_i)=\left(\sum_{l=1}^m\alpha_{l,i}\beta_{1,l}\right)z_1+\cdots+\left(\sum_{l=1}^m\alpha_{l,i}\beta_{k,l}\right)z_k$$

Earlier, we confirmed that for $[L_2\circ L_1]^{\mathcal{B}_1}_{\mathcal{B}_3}$, the $i$-th column is precisely the coordinate representation of the vector to which $x_i$ is mapped by $L_2\circ L_1$ with respect to $\mathcal{B}_3$; thus, in the matrix $[L_2\circ L_1]^{\mathcal{B}_1}_{\mathcal{B}_3}$, the entry in column $i$ and row $j$ is the $j$-th component $\sum_{l=1}^m\alpha_{l,i}\beta_{j,l}$ of this vector. Just as in [Theorem 3](#thm3){: data-lid="of699" }, in the matrix product $[L_2]^{\mathcal{B}_2}_{\mathcal{B}_3}[L_1]^{\mathcal{B}_1}_{\mathcal{B}_2}$, this component is the $(j,i)$-th entry, which completes the proof.
:::

The above [Theorem 4](#thm4){: data-lid="pbgw2" } shows that once we choose bases for $V,W$, we can treat $\Hom(V,W)$ and $\Mat_{m\times n}(\mathbb{K})$ as the same. For example, in $\Mat_{m\times n}(\mathbb{K})$, the $mn$ basis elements correspond to the $mn$ basis elements examined in [§Space of Linear Maps, ⁋Proposition 5](/en/math/linear_algebra/space_of_linear_maps#prop5){: data-lid="3646q" }. The following corollary is also a consequence of the fundamental theorem.

::: Corollary 6
Suppose two $n$-dimensional $\mathbb{K}$-vector spaces $V,W$ are given, and fix their bases $\mathcal{B},\mathcal{C}$. Then for any isomorphism $L\in\Hom(V,W)$, the matrix representation of $L^{-1}\in\Hom(W,V)$ with respect to the bases $\mathcal{C},\mathcal{B}$, denoted by $[L^{-1}]^{\mathcal{C}}_{\mathcal{B}}$, is equal to the inverse of the matrix $[L]^{\mathcal{B}}_\mathcal{C}$.
:::
::: Proof
Applying [Theorem 5](#thm5){: data-lid="5kwom" } to $L^{-1}\circ L=\id_V$ and $L\circ L^{-1}=\id_W$, we obtain $[L^{-1}]^{\mathcal{C}}_{\mathcal{B}}[L]^{\mathcal{B}}_{\mathcal{C}}=[\id_V]^{\mathcal{B}}_{\mathcal{B}}=I$ and $[L]^{\mathcal{B}}_{\mathcal{C}}[L^{-1}]^{\mathcal{C}}_{\mathcal{B}}=[\id_W]^{\mathcal{C}}_{\mathcal{C}}=I$.
:::

In this way, most of the concepts defined in [§Matrices](/en/math/linear_algebra/matrices){: data-lid="9v4wc" } can be transferred to $\Hom(V,W)$. One concept that cannot be transferred immediately is the transpose matrix $A^t$, the meaning of which can be understood later when we look at dual spaces.

## Change-of-Basis Matrix

To summarize [Theorem 4](#thm4){: data-lid="ganzk" } in a single phrase: for a linear map from an $n$-dimensional vector space $V$ to an $m$-dimensional vector space $W$, once we fix their respective bases $\mathcal{B}, \mathcal{C}$, we can represent it as an $m\times n$ matrix, and conversely, any $m\times n$ matrix can also be understood as a linear map. A natural question then is what happens when we change the bases, and in fact, the answer is already given in [Theorem 5](#thm5){: data-lid="5ds63" }.

::: Definition 7
For any finite-dimensional $\mathbb{K}$-vector space $V$ and, for $V$, two bases $\mathcal{B},\mathcal{B}'$, the *change-of-basis matrix* from $\mathcal{B}$ to $\mathcal{B}'$ refers to

$$[\id_V]_{\mathcal{B}'}^\mathcal{B}$$

.
:::

From the fact that the dimension of a vector space is well-defined, it is clear that such a matrix must be a square matrix. Moreover, from the identity

$$I=[\id_V]^{\mathcal{B}}_{\mathcal{B}}=[\id_V]_{\mathcal{B}}^{\mathcal{B}'}[\id_V]^\mathcal{B}_{\mathcal{B}'}$$

we see that such a matrix is always invertible.

To examine how the change-of-basis matrix works, let us fix a finite-dimensional $\mathbb{K}$-vector space $V$, and suppose that on $V$, two bases $\mathcal{B},\mathcal{B}'$ are given. The fundamental theorem of linear algebra means that the following diagram commutes.

{% diagram Math/Linear_Algebra/Change_of_Basis-1.svg width="6.42em" alt="change_of_basis" %}

Here, the two vertical functions represent $v\mapsto [v]_\mathcal{B}$ and $v\mapsto[v]_{\mathcal{B}'}$, respectively. Therefore, the change-of-basis matrix can be thought of as a matrix that takes the coordinate representation of $v\in V$ with respect to $\mathcal{B}$ and transforms it into the coordinate representation with respect to $\mathcal{B}'$. More generally, suppose an arbitrary linear map $L:V\rightarrow W$ is given, and suppose that for $V,W$, bases $\mathcal{B},\mathcal{C}$ and another pair of bases $\mathcal{B}',\mathcal{C}'$ are given. Then from the fundamental theorem of linear algebra, we obtain the identity

$$[L]_{\mathcal{C}'}^{\mathcal{B}'}=[\id_W]_{\mathcal{C}'}^\mathcal{C}[L]_{\mathcal{C}}^\mathcal{B}[\id_V]^{\mathcal{B}'}_{\mathcal{B}}$$

.

Suppose two $m\times n$ matrices $A,B$ are given. Then from the equation above, if there exist two invertible matrices $P,Q$ satisfying the identity

$$B=PAQ$$

, there is a temptation to treat $A$ and $B$ as the same. This means that given a fixed linear map $L$, we regard all matrix representations obtained by suitably choosing bases for the domain and codomain of $L$ as being the same.

However, compared to such a plausible motivation, the outcome is not very fruitful. This is because if we can change the bases of both the domain and codomain of $L$, we can choose a basis $\{x_1,\ldots, x_n\}$ of the domain such that its trailing elements form a basis of $\ker L$, and then in the codomain, choosing from among $L(x_1),\ldots, L(x_n)$ the linearly independent elements $L(x_1),\ldots, L(x_k)$, and using [§Dimension of Vector Spaces, ⁋Proposition 5](/en/math/linear_algebra/dimension#prop5){: data-lid="bv9hg" } to complete a basis of the codomain, this linear map can always be represented in the form of a block matrix

$$\begin{pmatrix}I&O\\O&O\end{pmatrix}$$

. That is, if we classify the matrix representations of $L$ in this manner, the only thing that affects the classification is the rank of $L$.

Therefore, we must define a finer relation than this equivalence relation.

::: Definition 8
Let any $n\times n$ matrices $A,B$ be given. Then $A$ and $B$ are said to be *similar matrices* if there exists an invertible matrix $P$ such that $A=PBP^{-1}$ holds.
:::

That is, the fact that the matrices $A,B$ are similar matrices means that, when for a fixed vector space $V$ we consider $A$ as *the matrix representation with respect to a basis $\mathcal{B}$ of a linear transformation $L:V\rightarrow V$*, there exists a suitable basis $\mathcal{C}$ such that $B$ can be regarded as *the matrix representation with respect to the basis $\mathcal{C}$ of $L$*. Then in this case,

$$A=[L]_{\mathcal{B}}^\mathcal{B}=[\id_V]^\mathcal{C}_\mathcal{B}[L]^\mathcal{C}_\mathcal{C}[\id_V]^\mathcal{B}_\mathcal{C}=PBP^{-1}$$

holds.

---

**References**

**[Lee]** 이인석, *선형대수와 군*, 서울대학교 출판문화원, 2005.

---

[^1]: Unlike the fundamental theorem of calculus, the fundamental theorem of algebra, and so forth, the *fundamental theorem of linear algebra* can refer to completely different theorems depending on the author. For example, **[Goc]** calls the rank-nullity theorem from the previous post the fundamental theorem of linear algebra, while Gilbert Strang refers to the theorems on orthogonal complements, which will be covered in the next post, as the fundamental theorem of linear algebra. Following **[Lee]**, we choose to call this theorem the fundamental theorem of linear algebra.
