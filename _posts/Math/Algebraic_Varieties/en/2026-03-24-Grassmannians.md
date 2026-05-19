---
title: "Grassmannians"
excerpt: "Grassmannians as parameter spaces of linear subspaces"

categories: [Math / Algebraic Varieties]
permalink: /en/math/algebraic_varieties/grassmannians
sidebar: 
    nav: "algebraic_varieties-en"

header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Grassmannians.png
    overlay_filter: 0.5

date: 2026-03-24
last_modified_at: 2026-03-24
weight: 7
translated_at: 2026-05-19T05:30:01+00:00
translation_source: kimi-cli
---
We introduce a special variety and conclude our introduction to the basic objects of study in algebraic geometry.

By definition, projective space $$\mathbb{P}^n$$ is the space of lines in $$\mathbb{A}^{n+1}$$. The Grassmannian introduced in this post generalizes this: it is the space of $$k$$-dimensional linear subspaces of $$\mathbb{A}^n$$.

## Definition of Grassmannians

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The set of $$k$$-dimensional subspaces of an $$n$$-dimensional vector space $$V$$ is called the *Grassmannian* $$\Gr(k, V)$$ or $$\Gr(k, n)$$.

</div>

Throughout this post we always assume that $$V$$ is an $$n$$-dimensional space.

Of course, one must separately show that it carries a variety structure, but the key result is that it not only has a variety structure but also preserves the relative position of each $$k$$-plane in $$\mathbb{A}^n$$, so it behaves as we want without much effort.

<div class="example" markdown="1">

<ins id="ex2">**Example 2**</ins> For example, $$\Gr(1, n+1)$$ is the space of lines in the $$(n+1)$$-dimensional vector space $$\mathbb{K}^{n+1}$$, so by definition it equals $$\mathbb{P}^n$$. Once we define the variety structure on the Grassmannian, we will see that these two structures are exactly the same.

The simplest example that did not appear before is $$\Gr(2,4)$$. This is the collection of $$2$$-dimensional subspaces of a $$4$$-dimensional space. When dealing with Grassmannians, this example will serve as a toy example.

</div>

As always, to give a variety structure it suffices to think of an affine cover and work affine-locally. For this purpose we make the following definition.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For each set of $$k$$ indices $$I = \{i_1 < \cdots < i_k\}$$, we define an open set $$U_I$$ by

$$U_I = \{W \in \Gr(k, V) \mid \text{projection } W \to \operatorname{span}(e_{i_1}, \ldots, e_{i_k}) \text{ is an isomorphism}\}$$

</div>

Fixing a basis $$e_1,\ldots, e_n$$ of $$V$$ and using vectors $$w_1,\ldots, w_k$$ spanning $$W$$, we see that $$W$$ is the row space of the following $$k\times n$$ matrix

$$\begin{pmatrix}w_1\\\vdots\\w_k\end{pmatrix}=\begin{pmatrix}w_{1,1}&w_{1,2}&\cdots &w_{1,n}\\ \vdots&\vdots&\ddots&\vdots\\ w_{k,1}&w_{k,2}&\cdots&w_{k,n}\end{pmatrix}$$

Then the condition defining $$U_I$$ is equivalent to the $$k\times k$$ matrix formed using the columns $$i_1,\ldots, i_k$$ corresponding to the index set $$I$$ being invertible. Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Each $$U_I \cong \mathbb{A}^{k(n-k)}$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Without loss of generality, we show the case $$I = \{1, 2, \ldots, k\}$$. That is, for the $$k \times n$$ matrix $$A$$ representing $$W \in U_I$$, the left $$k \times k$$ minor is nonzero. Using row operations, we bring this minor to the form

$$A = \begin{pmatrix} I_k & B \end{pmatrix}$$

Here $$B$$ is a $$k \times (n-k)$$ matrix. Then the $$k(n-k)$$ entries of $$B$$ completely determine $$W$$, and there is no constraint among them. Therefore $$U_I \cong \mathbb{A}^{k(n-k)}$$.

</details>

As seen in this proof, the coordinate system on $$U_I$$ consists of $$k(n-k)$$ free parameters. They correspond to the "non-trivial part" of the matrix representing $$W$$. That is, once the $$k \times k$$ block defined by $$I$$ is fixed to be the identity, the remaining $$(n-k) \times k$$ block can vary freely.

Then it is obvious that for any $$W\in \Gr(k,V)$$ there exists an affine open cover containing $$W$$. Moreover, since it is also obvious that the transition maps from $$U_I$$ to $$U_J$$ are regular maps, this endows $$\Gr(k,V)$$ with a variety structure. Of course, to show that this is quasi-projective one needs an explicit projective embedding, but for now we have the following.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> $$\dim \Gr(k, V) = k(n - k)$$.

</div>

## Plücker Embedding

We now show that the Grassmannian is a quasi-projective variety. That is, we define an embedding from the Grassmannian into a suitable projective space.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> The *Plücker embedding* $$\iota: \Gr(k, V) \to \mathbb{P}(\bigwedge^k V)$$ is the map sending a $$k$$-dimensional subspace $$W = \operatorname{span}(v_1, \ldots, v_k)$$ to the element

$$\iota(W) = [v_1 \wedge v_2 \wedge \cdots \wedge v_k]$$

([\[Multilinear Algebra\] §Tensor Algebras, ⁋Definition 10](/en/math/multilinear_algebra/tensor_algebras#def10))

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> The Plücker embedding is well-defined and injective.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

That the Plücker embedding is well-defined means the above value does not change when we choose a different basis of $$W$$. But if we choose a different basis of $$W$$, then $$v_1\wedge\cdots\wedge v_k$$ is only scaled by the determinant of the change-of-basis matrix, so when sent to $$\mathbb{P}(\bigwedge^k V)$$ it specifies the same point anyway. Running a similar argument in reverse, injectivity is also easily shown.

</details>

Moreover, $$\iota$$ realizes $$\Gr(k,V)$$ as a *closed* subvariety of $$\mathbb{P}(\bigwedge^kV)$$. To see this, observe that the image of $$\iota$$ consists precisely of *decomposable* vectors, i.e., vectors of the form

$$v_1\wedge\cdots\wedge v_k$$

Therefore, to show that the image of $$\iota$$ is a closed subvariety, it suffices to define polynomials having these as their zero set, and this follows from the properties of the wedge product via the following *Plücker relations*

$$\sum_{r=1}^{k+1} (-1)^r p_{i_1 \cdots i_{k-1} j_r} p_{j_1 \cdots \widehat{j_r} \cdots j_{k+1}} = 0\tag{$\ast$}$$

Here $$i_1 < \cdots < i_{k-1}$$ and $$j_1 < \cdots < j_{k+1}$$ are arbitrary subsets of $$\{1, \ldots, n\}$$, and $$\widehat{j_r}$$ means omitting $$j_r$$. These equations hold for all possible choices of $$i$$'s and $$j$$'s. From this we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> The image of the Plücker embedding is a closed subvariety of $$\mathbb{P}^{\binom{n}{k}-1}$$, and therefore $$\Gr(k,V)$$ is a projective variety.

</div>

<div class="example" markdown="1">

<ins id="ex9">**Example 9**</ins> Let us examine the Plücker relation ($$\ast$$) for $$\Gr(2,4)$$. The Plücker coordinates are $$p_{12}, p_{13}, p_{14}, p_{23}, p_{24}, p_{34}$$, and these are the homogeneous coordinates of $$\mathbb{P}^5$$. Then the Plücker relation is given by the unique $$3$$-term relation

$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$

This is a quadratic equation, so $$\Gr(2, 4)$$ is a quadric hypersurface in $$\mathbb{P}^5$$. If the dimension of $$V$$ increases, more such equations will appear, and if $$k$$ increases, each equation will have more terms.

</div>

## Schubert Varieties

The Grassmannian is equipped with a kind of cell structure, so it can be understood from a combinatorial viewpoint. For this purpose we first define the notions of flag and partition.

<div class="definition" markdown="1">

<ins id="def10">**Definition 10**</ins> A *flag* in an $$n$$-dimensional vector space $$V$$ is a chain of subspaces

$$F_\bullet:\qquad 0 = F_0 \subset F_1 \subset F_2 \subset \cdots \subset F_n = V$$

where $$\dim F_i = i$$.

</div>

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> When the standard basis $$e_1, \ldots, e_n$$ is given on $$V = \mathbb{K}^n$$, the *standard flag* is defined by

$$F_i = \operatorname{span}(e_1, \ldots, e_i)$$

</div>

Now given a $$k$$-dimensional subspace $$W$$, an element of $$\Gr(k, V)$$, we can track step by step how this $$W$$ meets the flag $$F_\bullet$$. Consider the sequence

$$0 = \dim(W \cap F_0) \leq \dim(W \cap F_1) \leq \cdots \leq \dim(W \cap F_n) = k$$

If we consider this sequence, the dimension increases by at most $$1$$ at each step. To represent this information concisely, we use a partition.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> A sequence $$\lambda = (\lambda_1, \ldots, \lambda_k)$$ of $$k$$ integers satisfying the conditions

$$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_k \geq 0,\qquad \lambda_1 \leq n - k$$

is called a *partition*. The *size* of a partition $$\lambda$$ is defined as $$\lvert \lambda \rvert = \sum_{i=1}^{k} \lambda_i$$.

</div>

Partitions can be visualized geometrically as a *Young diagram*. This consists of a first row with $$\lambda_1$$ boxes, a second row with $$\lambda_2$$ boxes, ..., and a $$k$$th row with $$\lambda_k$$ boxes. This facilitates computations called Schubert calculus, but since these are needed only when performing intersections, or multiplication in cohomology, we do not introduce them yet. Instead, we define the following.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> For a flag $$F_\bullet$$ and a partition $$\lambda = (\lambda_1, \ldots, \lambda_k)$$, the *Schubert variety* $$\Omega_\lambda(F_\bullet)$$ is defined as the set of $$W \in \Gr(k, V)$$ satisfying the conditions

$$\dim(W \cap F_{n - k + i - \lambda_i}) \geq i \quad\text{for all } 1 \leq i \leq k$$

</div>

This condition means that the dimensions of the intersections of $$W$$ with the flag follow a specific pattern. Specifically, $$W$$ must meet $$F_{n-k+i-\lambda_i}$$ in dimension at least $$i$$. The partition condition $$\lambda_1 \leq n - k$$ guarantees that $$n - k + 1 - \lambda_1 \geq 1$$ in the first inequality $$\dim(W \cap F_{n - k + 1 - \lambda_1}) \geq 1$$.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> The Schubert variety $$\Omega_\lambda(F_\bullet)$$ is a closed subvariety of $$\Gr(k, V)$$, and its dimension is $$\lvert \lambda \rvert$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

That $$\Omega_\lambda(F_\bullet)$$ is closed follows because the defining conditions are given by the zero set of regular functions.

To compute the dimension, we consider the (open) *Schubert cell* $$\Omega_\lambda^\circ(F_\bullet)$$ of $$\Omega_\lambda(F_\bullet)$$. This is obtained by changing the inequalities in the defining conditions to equalities:

$$\dim(W \cap F_{n - k + i - \lambda_i}) = i \quad\text{for all } 1 \leq i \leq k$$

and it is an open dense subset of $$\Omega_\lambda(F_\bullet)$$. Computing the dimension of this cell yields $$\lambda_1 + \cdots + \lambda_k = \lvert \lambda \rvert$$, and therefore the dimension of $$\Omega_\lambda(F_\bullet)$$ is also $$\lvert \lambda \rvert$$.

</details>

Schubert varieties provide a *cell decomposition* of the Grassmannian. That is, the Schubert cells $$\Omega_\lambda^\circ(F_\bullet)$$ corresponding to different partitions $$\lambda$$ give $$\Gr(k, V)$$ the structure of a cell complex, and each cell is isomorphic to the affine space $$\mathbb{A}^{\lvert \lambda \rvert}$$. Through this, one can study the topological and combinatorial properties of the Grassmannian.

---

**References**

**[Harris]** J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992.  
**[GH]** P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978.  
**[Ful]** W. Fulton, *Young Tableaux*, Cambridge University Press
