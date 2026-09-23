---
title: "Grassmann Varieties"
description: "Grassmann varieties are spaces of dimensional subspaces of a vector space, generalizing the concept of projective space. We define their variety structure using affine covers and examine their main properties."
excerpt: "Grassmannians as parameter spaces of linear subspaces"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/grassmannians
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-24
weight: 7
translated_at: 2026-08-18T21:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-23T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We introduce a special variety, concluding our introduction to the basic objects of study in algebraic geometry.

By definition, the projective space $\mathbb{P}^n$ is the space of lines through the origin in $\mathbb{A}^{n+1}$. The Grassmannian, which we introduce in this post, generalizes this: in $\mathbb{A}^n$, it is the space of $k$-dimensional linear subspaces through the origin.

## Definition of the Grassmannian

::: Definition 1
For an $n$-dimensional vector space $V$, the set of $k$-dimensional subspaces is called the *Grassmannian* $\Gr(k, V)$ or $\Gr(k, n)$.
:::

Throughout this post, $V$ is always assumed to be an $n$-dimensional space.

Of course, that this carries a variety structure must be shown separately, but the key result is that it not only has a variety structure, but provides a structure that also well preserves, in $\mathbb{A}^n$, the relative positions of each of the $k$-planes, so it behaves as we desire without our needing to worry much about it.

::: Example 2
For instance, $\Gr(1, n+1)$ is the space of lines in the $n+1$-dimensional vector space $\mathbb{K}^{n+1}$, so by definition it coincides with $\mathbb{P}^n$. Soon, after defining the variety structure on the Grassmannian, we will see that these two structures agree exactly.

The simplest new example is $\Gr(2,4)$. In a $4$-dimensional space, this is the collection of $2$-dimensional subspaces. When dealing with Grassmannians, this example will serve as a toy example.
:::

As always, to endow it with a variety structure, one can consider an affine cover and approach it affine-locally. To this end, for $V$ we fix a basis $e_1,\ldots, e_n$ and define the following.

::: Definition 3
For each choice of $k$ indices $I = \{i_1 < \cdots < i_k\}$, in $\Gr(k, V)$ we define the subset $U_I$ by

$$U_I = \{W \in \Gr(k, V) \mid \text{projection } W \rightarrow \operatorname{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}$$

:::

If for $W$ we write each spanning vector $w_1,\ldots, w_k$ in terms of its components with respect to this basis, $W$ is the row space of the following $k\times n$ matrix:

$$\begin{pmatrix}w_1\\\vdots\\w_k\end{pmatrix}=\begin{pmatrix}w_{1,1}&w_{1,2}&\cdots &w_{1,n}\\ \vdots&\vdots&\ddots&\vdots\\ w_{k,1}&w_{k,2}&\cdots&w_{k,n}\end{pmatrix}$$

Then the condition defining $U_I$ is precisely equivalent to saying that the columns corresponding to the index set $I$, namely $i_1,\ldots, i_k$, form an invertible $k\times k$ matrix. Then the following holds.

::: Proposition 4
Each $U_I \cong \mathbb{A}^{k(n-k)}$.
:::

::: Proof
Without loss of generality, we show the case $I = \{1, 2, \ldots, k\}$. That is, for $W \in U_I$ represented by a $k \times n$ matrix $A$, the left $k \times k$ minor is nonzero. Via row operations, let us bring this minor into the form

$$A = \begin{pmatrix} I_k & B \end{pmatrix}$$

where $B$ is a $k \times (n-k)$ matrix. Then in $B$, the $k(n-k)$ entries completely determine $W$, and there are no constraints among them. Therefore $U_I \cong \mathbb{A}^{k(n-k)}$.
:::

As seen in this proof, the coordinate system on $U_I$ consists of $k(n-k)$ free parameters. These correspond to the "non-trivial part" of the matrix representing $W$. That is, once the block defined by $I$, of size $k \times k$, is fixed as the identity, the remaining $k \times (n-k)$ block can vary freely.

Then for any $W\in \Gr(k,V)$, it is clear that there exists an affine open cover containing $W$. Moreover, since the transition map from $U_I$ to $U_J$ is also clearly a regular map, this endows $\Gr(k,V)$ with a variety structure, and each $U_I$ becomes an open set in this structure. Of course, to show that this is quasi-projective, an explicit projective embedding is needed, but for now the following holds.

::: Proposition 5
$\dim \Gr(k, V) = k(n - k)$.
:::

## Plücker Embedding

Now we show that the Grassmannian is a quasi-projective variety. That is, we define an embedding from the Grassmannian into a suitable projective space.

::: Definition 6
The *Plücker embedding* $\iota: \Gr(k, V) \rightarrow \mathbb{P}(\bigwedge^k V)$ is the map that sends a $k$-dimensional subspace $W = \operatorname{span}(v_1, \ldots, v_k)$ to the element

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k]$$

([Multilinear Algebra] §Tensor Algebras, ⁋Definition 10)
:::

Then the following holds. 

::: Proposition 7
The Plücker embedding is well-defined and injective.
:::

::: Proof
That the Plücker embedding is well-defined means that the above value does not change when a different basis of $W$ is chosen. However, if a different basis of $W$ is chosen, $v_1\wedge\cdots\wedge v_k$ is scaled only by the determinant of the change-of-basis matrix, so when sent to $\mathbb{P}(\bigwedge^k V)$ it specifies the same point anyway. On the other hand, for $\omega = v_1\wedge\cdots\wedge v_k$, we have $W = \{v \in V \mid v\wedge\omega = 0\}$, so $W$ is recovered from $[\omega]$, and hence $\iota$ is injective. 
:::

Moreover, $\iota$ defines $\Gr(k,V)$ as a *closed* subvariety of $\mathbb{P}(\bigwedge^kV)$. To see this, examining the image of $\iota$, we find that the image of $\iota$ consists exactly of *decomposable* vectors, that is, vectors representable in the form

$$v_1\wedge\cdots\wedge v_k$$

For the fixed basis $e_1,\ldots,e_n$, since $\bigwedge^kV$ has, for $i_1<\cdots<i_k$, the basis elements $e_{i_1}\wedge\cdots\wedge e_{i_k}$, we have $\dim\bigwedge^kV=\binom{n}{k}$, and therefore $\mathbb{P}(\bigwedge^kV)\cong\mathbb{P}^{\binom{n}{k}-1}$. In the expansion with respect to this basis,

$$v_1\wedge\cdots\wedge v_k=\sum_{i_1<\cdots<i_k}p_{i_1\cdots i_k}e_{i_1}\wedge\cdots\wedge e_{i_k}$$

the coefficients $p_{i_1\cdots i_k}$ are called the *Plücker coordinates* of $W$. From the matrix representing $W$, which is of size $k\times n$, choosing the $i_1,\ldots,i_k$-th columns yields a $k\times k$ minor, and when the basis of $W$ is changed, as we saw in the proof of [Proposition 7](#prop7){: data-lid="xsm5g" data-relation="required" }, all of these are scaled by the same scalar, so they become homogeneous coordinates on $\mathbb{P}^{\binom{n}{k}-1}$. Henceforth, when indices are not given in increasing order, we understand $p$ as extended antisymmetrically in the indices, and if the same index is repeated, we set it to $0$.

Therefore, to claim that the image of $\iota$ is a closed subvariety, it suffices to define polynomials having these as their zero set, and this is obtained through the following *Plücker relations* from the properties of the wedge product:

$$\sum_{r=1}^{k+1} (-1)^r p_{i_1 \cdots i_{k-1} j_r} p_{j_1 \cdots \widehat{j_r} \cdots j_{k+1}} = 0\tag{$\ast$}$$

Here $i_1 < \cdots < i_{k-1}$ and $j_1 < \cdots < j_{k+1}$ are arbitrary subsets of $\{1, \ldots, n\}$, and $\widehat{j_r}$ means omitting $j_r$. These equations hold for all possible choices of $i$'s and $j$'s. From this we obtain the following. 

::: Proposition 8
The image of the Plücker embedding is a closed subvariety of $\mathbb{P}^{\binom{n}{k}-1}$, and therefore $\Gr(k,V)$ is a projective variety. 
:::

::: Example 9
Let us examine the Plücker relation ($\ast$) for $\Gr(2,4)$. The Plücker coordinates are $p_{12}, p_{13}, p_{14}, p_{23}, p_{24}, p_{34}$, which are the homogeneous coordinates of $\mathbb{P}^5$. Then the Plücker relation is given by the unique 3-term relation

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$

Since this is a quadratic equation, $\Gr(2, 4)$ is a quadric hypersurface in $\mathbb{P}^5$. If the dimension of $V$ increases, more such equations will appear, and if $k$ increases, each equation will have more terms. 
:::

## Schubert Varieties

The Grassmannian is equipped with a certain cell structure, so it can be understood from a combinatorial perspective. To this end, we first define the notions of a flag and a partition.

::: Definition 10
A *flag* in an $n$-dimensional vector space $V$ is a chain of subspaces

$$F_\bullet:\qquad 0 = F_0 \subseteq F_1 \subseteq F_2 \subseteq \cdots \subseteq F_n = V$$

where $\dim F_i = i$.
:::

::: Example 11
When $V = \mathbb{K}^n$ is given with the standard basis $e_1, \ldots, e_n$, the *standard flag* is defined by

$$F_i = \operatorname{span}(e_1, \ldots, e_i)$$
:::

Now, given an element of $\Gr(k, V)$, a $k$-dimensional subspace $W$, we can track step by step how this $W$ meets the flag $F_\bullet$. Considering the sequence

$$0 = \dim(W \cap F_0) \leq \dim(W \cap F_1) \leq \cdots \leq \dim(W \cap F_n) = k$$

the dimension increases by at most $1$ at each step. To represent this information concisely, we use a partition.

::: Definition 12
A sequence of $k$ integers $\lambda = (\lambda_1, \ldots, \lambda_k)$ satisfying the condition

$$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_k \geq 0,\qquad \lambda_1 \leq n - k$$

is called a *partition*. The *size* of a partition $\lambda$ is defined as $\lvert \lambda \rvert = \sum_{i=1}^{k} \lambda_i$.
:::

A partition can be visualized geometrically as a *Young diagram*. It consists of $\lambda_1$ boxes in the first row, $\lambda_2$ boxes in the second row, ..., and $\lambda_k$ boxes in the $k$-th row. This helps facilitate the operations called Schubert calculus, but since this is in any case needed when taking intersections, or multiplication in cohomology, we do not introduce it yet. Instead, we define the following.

::: Definition 13
For a flag $F_\bullet$ and a partition $\lambda = (\lambda_1, \ldots, \lambda_k)$, the *Schubert variety* $\Omega_\lambda(F_\bullet)$ is defined by the condition

$$\dim(W \cap F_{n - k + i - \lambda_i}) \geq i \quad\text{for all } 1 \leq i \leq k$$

as the set of $W \in \Gr(k, V)$ satisfying it.
:::

This condition means that the dimension of the intersection of $W$ with the flag follows a specific pattern. Specifically, $W$ must meet $F_{n-k+i-\lambda_i}$ in dimension at least $i$. The partition condition $\lambda_1 \leq n - k$ ensures that in the first inequality $\dim(W \cap F_{n - k + 1 - \lambda_1}) \geq 1$, we have $n - k + 1 - \lambda_1 \geq 1$.

::: Proposition 14
The Schubert variety $\Omega_\lambda(F_\bullet)$ is a closed subvariety of $\Gr(k, V)$, and its dimension is $k(n-k) - \lvert \lambda \rvert$.
:::

::: Proof
That $\Omega_\lambda(F_\bullet)$ is closed is because the defining conditions are given by the zero set of regular functions.

To compute the dimension, we consider, for $\Omega_\lambda(F_\bullet)$, the (open) *Schubert cell* $\Omega_\lambda^\circ(F_\bullet)$. This is obtained by turning the inequalities in the defining conditions into equalities, and further requiring that the index where the dimension jumps is precisely $n-k+i-\lambda_i$:

$$\dim(W \cap F_{n - k + i - \lambda_i}) = i,\qquad \dim(W \cap F_{n - k + i - \lambda_i - 1}) = i-1 \quad\text{for all } 1 \leq i \leq k$$

and it is an open dense subset of $\Omega_\lambda(F_\bullet)$. Computing the dimension of this cell gives $k(n-k) - (\lambda_1 + \cdots + \lambda_k) = k(n-k) - \lvert \lambda \rvert$, and therefore the dimension of $\Omega_\lambda(F_\bullet)$ is also $k(n-k) - \lvert \lambda \rvert$.
:::

The Schubert varieties provide a *cell decomposition* of the Grassmannian. That is, for different partitions $\lambda$, the corresponding Schubert cells $\Omega_\lambda^\circ(F_\bullet)$ give a cell complex structure on $\Gr(k, V)$, and each cell is isomorphic to the affine space $\mathbb{A}^{k(n-k) - \lvert \lambda \rvert}$. Through this, one can study the topological and combinatorial properties of the Grassmannian.

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press
