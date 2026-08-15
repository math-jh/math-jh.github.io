---
title: "Grassmann Varieties"
description: "Grassmann varieties are spaces of linear subspaces of a given dimension in a vector space, generalizing the notion of projective space. We define their variety structure using affine charts and examine their main properties."
excerpt: "Grassmannians as parameter spaces of linear subspaces"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/grassmannians
sidebar: 
    nav: "algebraic_varieties-en"

date: 2026-03-24
weight: 7
translated_at: 2026-08-15T22:47:42+00:00
translation_source: kimi-cli
---
We introduce a special variety and finish our overview of the basic objects of study in algebraic geometry.

By definition, the projective space $\mathbb{P}^n$ is the space of lines through the origin in $\mathbb{A}^{n+1}$. The Grassmannian, which we introduce in this post, generalizes this: it is the space of $k$-dimensional linear subspaces through the origin in $\mathbb{A}^n$.

## Definition of the Grassmannian

::: Definition 1
The set of $k$-dimensional subspaces of an $n$-dimensional vector space $V$ is called the *Grassmannian* $\Gr(k, V)$, or $\Gr(k, n)$.
:::

Throughout this post, we always assume that $V$ is an $n$-dimensional space.

Of course, one must separately verify that this carries a variety structure, but the key result is that not only does it have a variety structure, but because this structure preserves the relative position of each $k$-plane in $\mathbb{A}^n$, it behaves exactly as we want without requiring much care.

::: Example 2
For instance, $\Gr(1, n+1)$ is the space of lines in the $(n+1)$-dimensional vector space $\mathbb{K}^{n+1}$, so by definition it coincides with $\mathbb{P}^n$. Once we define the variety structure on the Grassmannian, we will see that these two structures are exactly the same.

The simplest new example is $\Gr(2,4)$. This is the collection of $2$-dimensional subspaces of a $4$-dimensional space. When we study Grassmannians, this example will serve as a toy example.
:::

As always, to endow it with a variety structure, we can consider an affine cover and work affine-locally. To this end, we fix a basis $e_1,\ldots, e_n$ of $V$ and make the following definition.

::: Definition 3
For each set of $k$ indices $I = \{i_1 < \cdots < i_k\}$, we define the subset $U_I$ of $\Gr(k, V)$ by

$$U_I = \{W \in \Gr(k, V) \mid \text{projection } W \rightarrow \operatorname{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}.$$

:::

Writing the vectors $w_1,\ldots, w_k$ spanning $W$ in terms of their components with respect to this basis, $W$ is the row space of the following $k \times n$ matrix

$$\begin{pmatrix}w_1\\\vdots\\w_k\end{pmatrix}=\begin{pmatrix}w_{1,1}&w_{1,2}&\cdots &w_{1,n}\\ \vdots&\vdots&\ddots&\vdots\\ w_{k,1}&w_{k,2}&\cdots&w_{k,n}\end{pmatrix}.$$

Then the condition defining $U_I$ is equivalent to the $k \times k$ matrix formed by the columns $i_1,\ldots, i_k$ corresponding to the index set $I$ being invertible. Then the following holds.

::: Proposition 4
Each $U_I \cong \mathbb{A}^{k(n-k)}$.
:::

::: Proof
Without loss of generality, let us show the case $I = \{1, 2, \ldots, k\}$. That is, for the $k \times n$ matrix $A$ representing $W \in U_I$, the left $k \times k$ minor is nonzero. By row operations, we bring this minor to the form

$$A = \begin{pmatrix} I_k & B \end{pmatrix}.$$

Here $B$ is a $k \times (n-k)$ matrix. Then the $k(n-k)$ entries of $B$ completely determine $W$, and there are no constraints among them. Therefore $U_I \cong \mathbb{A}^{k(n-k)}$.
:::

As seen in this proof, the coordinate system on $U_I$ consists of $k(n-k)$ free parameters. These correspond to the "non-trivial part" of the matrix representing $W$; that is, once the $k \times k$ block determined by $I$ is fixed to be the identity, the remaining $k \times (n-k)$ block can vary freely.

Then it is obvious that for any $W\in \Gr(k,V)$, there exists an affine open cover containing $W$. Moreover, since the transition map from $U_I$ to $U_J$ is also obviously a regular map, this endows $\Gr(k,V)$ with a variety structure, and each $U_I$ becomes an open subset in this structure. Of course, to show that this is quasi-projective, an explicit projective embedding is needed, but for now the following holds.

::: Proposition 5
$\dim \Gr(k, V) = k(n - k)$.
:::

## Plücker Embedding

Now we show that the Grassmannian is a quasi-projective variety. That is, we define an embedding from the Grassmannian into a suitable projective space.

::: Definition 6
The *Plücker embedding* $\iota: \Gr(k, V) \rightarrow \mathbb{P}(\bigwedge^k V)$ is the map that sends a $k$-dimensional subspace $W = \operatorname{span}(v_1, \ldots, v_k)$ to the element

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k].$$

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

$$v_1\wedge\cdots\wedge v_k.$$

For the fixed basis $e_1,\ldots,e_n$, since $\bigwedge^kV$ has the $e_{i_1}\wedge\cdots\wedge e_{i_k}$ with $i_1<\cdots<i_k$ as a basis, we have $\dim\bigwedge^kV=\binom{n}{k}$, and therefore $\mathbb{P}(\bigwedge^kV)\cong\mathbb{P}^{\binom{n}{k}-1}$. The coefficients

$$v_1\wedge\cdots\wedge v_k=\sum_{i_1<\cdots<i_k}p_{i_1\cdots i_k}e_{i_1}\wedge\cdots\wedge e_{i_k}$$

in the expansion with respect to this basis are called the *Plücker coordinates* of $W$. These are the $k\times k$ minors formed by choosing the columns $i_1,\ldots,i_k$ from the $k\times n$ matrix representing $W$, and as we saw in the proof of [Proposition 7](#prop7), when the basis of $W$ is changed, all of these are scaled by the same scalar, so they become homogeneous coordinates on $\mathbb{P}^{\binom{n}{k}-1}$. Henceforth, when indices are not given in increasing order, we understand $p$ as extended antisymmetrically in the indices, and if the same index is repeated, we set it to $0$.

Therefore, to claim that the image of $\iota$ is a closed subvariety, it suffices to define polynomials having these as their zero set, and this is obtained through the following *Plücker relations* from the properties of the wedge product:

$$\sum_{r=1}^{k+1} (-1)^r p_{i_1 \cdots i_{k-1} j_r} p_{j_1 \cdots \widehat{j_r} \cdots j_{k+1}} = 0\tag{$\ast$}$$

Here $i_1 < \cdots < i_{k-1}$ and $j_1 < \cdots < j_{k+1}$ are arbitrary subsets of $\{1, \ldots, n\}$, and $\widehat{j_r}$ means omitting $j_r$. These equations hold for all possible choices of $i$'s and $j$'s. From this we obtain the following.

::: Proposition 8
The image of the Plücker embedding is a closed subvariety of $\mathbb{P}^{\binom{n}{k}-1}$, and therefore $\Gr(k,V)$ is a projective variety.
:::

::: Example 9
Let us examine the Plücker relation ($\ast$) for $\Gr(2,4)$. The Plücker coordinates are $p_{12}, p_{13}, p_{14}, p_{23}, p_{24}, p_{34}$, which are the homogeneous coordinates of $\mathbb{P}^5$. Then the Plücker relation is given by the unique $3$-term relation

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0.$$

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

$$F_i = \operatorname{span}(e_1, \ldots, e_i).$$

:::

Now, given a $k$-dimensional subspace $W$, which is an element of $\Gr(k, V)$, we can track step by step how this $W$ meets the flag $F_\bullet$. Considering the sequence

$$0 = \dim(W \cap F_0) \leq \dim(W \cap F_1) \leq \cdots \leq \dim(W \cap F_n) = k,$$

the dimension increases by at most $1$ at each step. To represent this information concisely, we use a partition.

::: Definition 12
A sequence $\lambda = (\lambda_1, \ldots, \lambda_k)$ of $k$ integers satisfying the conditions

$$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_k \geq 0,\qquad \lambda_1 \leq n - k$$

is called a *partition*. The *size* of a partition $\lambda$ is defined as $\lvert \lambda \rvert = \sum_{i=1}^{k} \lambda_i$.
:::

A partition can be visualized geometrically as a *Young diagram*. This consists of a first row with $\lambda_1$ boxes, a second row with $\lambda_2$ boxes, ..., and a $k$-th row with $\lambda_k$ boxes. This facilitates the operations called Schubert calculus, but since this is needed only when taking intersections, or products in cohomology, we do not introduce it yet. Instead, we define the following.

::: Definition 13
For a flag $F_\bullet$ and a partition $\lambda = (\lambda_1, \ldots, \lambda_k)$, the *Schubert variety* $\Omega_\lambda(F_\bullet)$ is defined as the set of $W \in \Gr(k, V)$ satisfying the conditions

$$\dim(W \cap F_{n - k + i - \lambda_i}) \geq i \quad\text{for all } 1 \leq i \leq k.$$

:::

This condition means that the dimensions of the intersections of $W$ with the flag follow a specific pattern. Specifically, $W$ must meet $F_{n-k+i-\lambda_i}$ in dimension at least $i$. The partition condition $\lambda_1 \leq n - k$ ensures that $n - k + 1 - \lambda_1 \geq 1$ in the first inequality $\dim(W \cap F_{n - k + 1 - \lambda_1}) \geq 1$.

::: Proposition 14
The Schubert variety $\Omega_\lambda(F_\bullet)$ is a closed subvariety of $\Gr(k, V)$, and its dimension is $k(n-k) - \lvert \lambda \rvert$.
:::

::: Proof
That $\Omega_\lambda(F_\bullet)$ is closed is because the defining conditions are given by the zero set of regular functions.

To compute the dimension, we consider the (open) *Schubert cell* $\Omega_\lambda^\circ(F_\bullet)$ of $\Omega_\lambda(F_\bullet)$. This is obtained by turning the inequalities in the defining conditions into equalities, and further requiring that the dimension jumps exactly at the index $n-k+i-\lambda_i$:

$$\dim(W \cap F_{n - k + i - \lambda_i}) = i,\qquad \dim(W \cap F_{n - k + i - \lambda_i - 1}) = i-1 \quad\text{for all } 1 \leq i \leq k,$$

and it is an open dense subset of $\Omega_\lambda(F_\bullet)$. Computing the dimension of this cell gives $k(n-k) - (\lambda_1 + \cdots + \lambda_k) = k(n-k) - \lvert \lambda \rvert$, and therefore the dimension of $\Omega_\lambda(F_\bullet)$ is also $k(n-k) - \lvert \lambda \rvert$.
:::

The Schubert varieties provide a *cell decomposition* of the Grassmannian. That is, the Schubert cells $\Omega_\lambda^\circ(F_\bullet)$ corresponding to different partitions $\lambda$ give a cell complex structure on $\Gr(k, V)$, and each cell is isomorphic to the affine space $\mathbb{A}^{k(n-k) - \lvert \lambda \rvert}$. Through this, one can study the topological and combinatorial properties of the Grassmannian.

---

**References**

**[Har]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press
