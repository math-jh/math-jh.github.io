---
title: "Tensor Product of Matrices"
description: "The tensor product of matrices implements the tensor product of linear maps via the Kronecker product. We summarize the definition and basic properties of this induced operation."
excerpt: "The Kronecker product as matrix realization of tensor products"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/tensor_product_of_matrices
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-06
weight: 9
translated_at: 2026-08-02T16:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-02T16:45:05+00:00
---
In [§Matrices and Linear Maps](/en/math/multilinear_algebra/matrices_and_linear_maps), we represented linear maps between free $A$-modules as matrices and observed that composition of linear maps corresponds to matrix multiplication. Another operation available on linear maps is the tensor product, so it is natural to ask which matrix operation emerges at the level of matrix representations. In this post, we examine the answer: the tensor product of matrices, i.e., the Kronecker product. Throughout, $A$ denotes a commutative ring.

## Tensor Product of Linear Maps

Let $M,M',L,L'$ be four $A$-modules and let $u:M \rightarrow L$, $u':M' \rightarrow L'$ be linear maps. Then the map

$$M\times M' \rightarrow L\otimes_AL';\qquad (x,x')\mapsto u(x)\otimes u'(x')$$

is $A$-bilinear, so by the universal property of [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 8](/en/math/algebraic_structures/operations_of_modules#prop8), the following definition is well-posed.

::: Definition 1
In the above situation, the *tensor product* $u\otimes u': M\otimes_AM' \rightarrow L\otimes_AL'$ is the unique $A$-linear map satisfying

$$(u\otimes u')(x\otimes x')=u(x)\otimes u'(x').$$
:::

This definition supplies the action on morphisms when $\otimes_A$ is regarded as a functor of two variables. Indeed, the following holds.

::: Proposition 2
For linear maps $v:N \rightarrow M$, $v':N' \rightarrow M'$, $u:M \rightarrow L$, $u':M' \rightarrow L'$, the identities

$$(u\otimes u')\circ(v\otimes v')=(u\circ v)\otimes(u'\circ v'),\qquad \id_M\otimes\id_{M'}=\id_{M\otimes_AM'}$$

hold.
:::
::: Proof
Since both sides are $A$-linear, it suffices to check agreement on generators of $M\otimes_AM'$ or $N\otimes_AN'$. For any $y\otimes y'\in N\otimes_AN'$,

$$\bigl((u\otimes u')\circ(v\otimes v')\bigr)(y\otimes y')=(u\otimes u')\bigl(v(y)\otimes v'(y')\bigr)=u(v(y))\otimes u'(v'(y'))=\bigl((u\circ v)\otimes (u'\circ v')\bigr)(y\otimes y')$$

and $(\id_M\otimes\id_{M'})(x\otimes x')=x\otimes x'$.
:::

## Basis of the Tensor Product

To obtain a matrix representation, we need a basis of $M\otimes_AM'$.

::: Lemma 3
Let $M,M'$ be free $A$-modules with bases $\mathcal{B}=(e_i)_{i\in I}$, $\mathcal{B}'=(e'_{i'})_{i'\in I'}$. Then the family

$$\mathcal{B}\otimes\mathcal{B}'=(e_i\otimes e'_{i'})_{(i,i')\in I\times I'}$$

is a basis of $M\otimes_AM'$.
:::
::: Proof
By definition of basis, there exist isomorphisms $M\cong\bigoplus_{i\in I}A$ and $M'\cong\bigoplus_{i'\in I'}A$. Moreover, by the adjunction of [\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Theorem 9](/en/math/algebraic_structures/operations_of_modules#thm9), the functor $-\otimes_AN$ is a left adjoint, hence preserves colimits and in particular direct sums. Applying this successively in each variable yields

$$M\otimes_AM'\cong\left(\bigoplus_{i\in I}A\right)\otimes_AM'\cong\bigoplus_{i\in I}(A\otimes_AM')\cong \bigoplus_{i\in I}\bigoplus_{i'\in I'}(A\otimes_AA)\cong\bigoplus_{(i,i')\in I\times I'}A.$$

Here $A\otimes_AA\cong A$ is the isomorphism given by multiplication $a\otimes b\mapsto ab$. Tracing the composite isomorphism, $e_i\otimes e'_{i'}$ is sent precisely to $1$ in the $(i,i')$-th component, so $(e_i\otimes e'_{i'})_{(i,i')\in I\times I'}$ is a basis of $M\otimes_AM'$.
:::

## Tensor Product of Matrices

Now let us define the operation at the level of matrices that corresponds to the tensor product. Since in [§Matrices, ⁋Definition 1](/en/math/multilinear_algebra/matrices#def1) we allowed matrix indices to range over arbitrary sets, the following definition is natural.

::: Definition 4
For two matrices $X=(x_{ji})\in\Mat_{J\times I}(A)$, $X'=(x'_{j'i'})\in\Mat_{J'\times I'}(A)$, their *tensor product* or *Kronecker product* $X\otimes X'$ is the $(J\times J')\times (I\times I')$ matrix defined by

$$(X\otimes X')_{(j,j'),(i,i')}=x_{ji}x'_{j'i'}.$$
:::

In particular, if $I,J,I',J'$ are finite sets of the form $\{1,\ldots,m\}$ and we equip $I\times I'$ and $J\times J'$ with the lexicographic order, then $X\otimes X'$ becomes the block matrix obtained by replacing each entry $x_{ji}$ of $X$ with the block $x_{ji}X'$:

$$X\otimes X'=\begin{pmatrix}x_{11}X'&x_{12}X'&\cdots\\x_{21}X'&x_{22}X'&\cdots\\\vdots&\vdots&\ddots\end{pmatrix}$$

which is the standard notation for the Kronecker product. Let us verify that this operation indeed realizes the tensor product of linear maps.

::: Proposition 5
Let $M,M',L,L'$ be free $A$-modules with bases $\mathcal{B}=(e_i)_{i\in I}$, $\mathcal{B}'=(e'_{i'})_{i'\in I'}$, $\mathcal{C}=(f_j)_{j\in J}$, $\mathcal{C}'=(f'_{j'})_{j'\in J'}$, and let $u:M \rightarrow L$, $u':M' \rightarrow L'$ be linear maps. Then the identity

$$[u\otimes u']_{\mathcal{C}\otimes\mathcal{C}'}^{\mathcal{B}\otimes\mathcal{B}'}=[u]_\mathcal{C}^\mathcal{B}\otimes[u']_{\mathcal{C}'}^{\mathcal{B}'}$$

holds.
:::
::: Proof
Write $[u]_\mathcal{C}^\mathcal{B}=(x_{ji})$ and $[u']_{\mathcal{C}'}^{\mathcal{B}'}=(x'_{j'i'})$. By [§Matrices and Linear Maps, ⁋Definition 1](/en/math/multilinear_algebra/matrices_and_linear_maps#def1),

$$u(e_i)=\sum_{j\in J}x_{ji}f_j,\qquad u'(e'_{i'})=\sum_{j'\in J'}x'_{j'i'}f'_{j'}$$

and therefore

$$(u\otimes u')(e_i\otimes e'_{i'})=u(e_i)\otimes u'(e'_{i'})=\sum_{(j,j')\in J\times J'}x_{ji}x'_{j'i'}(f_j\otimes f'_{j'}).$$

By [Lemma 3](#lem3), the elements $(f_j\otimes f'_{j'})$ form a basis of $L\otimes_AL'$, so the $\bigl((j,j'),(i,i')\bigr)$-entry of $[u\otimes u']_{\mathcal{C}\otimes\mathcal{C}'}^{\mathcal{B}\otimes\mathcal{B}'}$ is $x_{ji}x'_{j'i'}$, which is exactly the corresponding entry of $[u]_\mathcal{C}^\mathcal{B}\otimes[u']_{\mathcal{C}'}^{\mathcal{B}'}$.
:::

Thus [Definition 4](#def4) gives the matrix representation of the linear map produced by [Definition 1](#def1).

## Properties of the Tensor Product

Let us examine the basic properties of the tensor product of matrices. The most important is compatibility with matrix multiplication, also called the *mixed product property*.

::: Proposition 6
Let $X\in\Mat_{K\times J}(A)$, $Y\in\Mat_{J\times I}(A)$, $X'\in\Mat_{K'\times J'}(A)$, $Y'\in\Mat_{J'\times I'}(A)$ be matrices, and assume $J,J'$ are finite. Then the identity

$$(X\otimes X')(Y\otimes Y')=(XY)\otimes(X'Y')$$

holds.
:::
::: Proof
Computing the $\bigl((k,k'),(i,i')\bigr)$-entry of the left-hand side by the definition of matrix multiplication,

$$\sum_{(j,j')\in J\times J'}(X\otimes X')_{(k,k'),(j,j')}(Y\otimes Y')_{(j,j'),(i,i')}=\sum_{(j,j')\in J\times J'}x_{kj}x'_{k'j'}y_{ji}y'_{j'i'}=\left(\sum_{j\in J}x_{kj}y_{ji}\right)\left(\sum_{j'\in J'}x'_{k'j'}y'_{j'i'}\right)$$

which equals $(XY)_{ki}(X'Y')_{k'i'}$, i.e., the corresponding entry of the right-hand side. The last equality uses commutativity of $A$.
:::

Of course, this proposition can also be obtained by combining [Proposition 2](#prop2), [Proposition 5](#prop5), and [§Matrices and Linear Maps, ⁋Corollary 4](/en/math/multilinear_algebra/matrices_and_linear_maps#cor4), which states that the matrix representation of a composition is the matrix product. From this, the following properties follow.

::: Proposition 7
For matrices $X\in\Mat_{J\times I}(A)$, $X'\in\Mat_{J'\times I'}(A)$, the following hold.

1. $(X\otimes X')^t=X^t\otimes X'^t$.
2. If $I,I'$ are finite and $X,X'$ are both invertible square matrices, then $X\otimes X'$ is also invertible and $(X\otimes X')^{-1}=X^{-1}\otimes X'^{-1}$.
3. If $I,I'$ are finite and $X,X'$ are square matrices, then $\tr(X\otimes X')=\tr(X)\tr(X')$.
:::
::: Proof
The first identity follows from a component-wise computation: by definition of transpose,

$$\bigl((X\otimes X')^t\bigr)_{(i,i'),(j,j')}=(X\otimes X')_{(j,j'),(i,i')}=x_{ji}x'_{j'i'}=(X^t)_{ij}(X'^t)_{i'j'}=(X^t\otimes X'^t)_{(i,i'),(j,j')}.$$

For the second claim, let $\lvert I\rvert=n$ and $\lvert I'\rvert=m$; then $\lvert I\times I'\rvert=nm$, and comparing entries of the identity matrices,

$$(I_n\otimes I_m)_{(j,j'),(i,i')}=\delta_{ji}\delta_{j'i'}=\delta_{(j,j'),(i,i')}$$

so $I_n\otimes I_m=I_{nm}$. Hence by [Proposition 6](#prop6),

$$(X\otimes X')(X^{-1}\otimes X'^{-1})=(XX^{-1})\otimes(X'X'^{-1})=I_n\otimes I_m=I_{nm}$$

and the product in the reverse order is the same.

Finally, let us compute the trace. Even for a square matrix $X=(x_{ji})$ indexed by a finite set $I$, if we define its trace by $\tr(X)=\sum_{i\in I}x_{ii}$, then

$$\tr(X\otimes X')=\sum_{(i,i')\in I\times I'}(X\otimes X')_{(i,i'),(i,i')}=\sum_{i\in I}\sum_{i'\in I'}x_{ii}x'_{i'i'}=\left(\sum_{i\in I}x_{ii}\right)\left(\sum_{i'\in I'}x'_{i'i'}\right)=\tr(X)\tr(X').$$
:::

To read the third property at the level of linear maps, we require $L=M$ and $L'=M'$ to be finitely generated free $A$-modules, with $u\in\End_\rMod{A}(M)$ and $u'\in\End_\rMod{A}(M')$, and we must choose a single basis $\mathcal{B}$ for $M$ and $\mathcal{B}'$ for $M'$. Then $u\otimes u'\in\End_\rMod{A}(M\otimes_AM')$, and combining the fact that the trace is independent of the choice of matrix representation with [Proposition 5](#prop5), we obtain $\tr(u\otimes u')=\tr(u)\tr(u')$. ([§Matrices and Linear Maps, §§Matrix Representations and Trace](/en/math/multilinear_algebra/matrices_and_linear_maps#matrix-representations-and-trace))

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  
