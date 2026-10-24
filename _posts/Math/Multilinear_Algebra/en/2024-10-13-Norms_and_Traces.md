---
title: "Norms and Traces"
description: "We define the trace, norm, and characteristic polynomial of an element in an algebra over a commutative ring, and examine their relationship with matrix representations. We also prove a multiplicative formula for descending chains of submodules."
excerpt: "The norm and trace defined by elements of an algebra"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/norms_and_traces
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-13
weight: 12
translated_at: 2026-06-01T19:00:06+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-24T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definition of Norms and Traces

As always, suppose that a commutative ring $A$ is given, and this time let a unital associative $A$-algebra $E$ be given. Then any $E$-module can always be regarded as an $A$-module via restriction of scalars.

::: Definition 1
Let an $E$-module $M$ be given, and suppose that $M$ has a finite basis as an $A$-module. For any $\alpha\in E$, suppose that the following $A$-module endomorphism

$$\alpha_M: x\mapsto \alpha x$$

is given. Then the trace, determinant, and characteristic polynomial of $\alpha_M$ are called the *trace*, *norm*, and *characteristic polynomial* of $\alpha$, respectively, and denoted by

$$\tr_{M/A}(\alpha)=\tr(\alpha_M),\qquad N_{M/A}(\alpha)=\det(\alpha_M),\qquad \chi_{M/A,\alpha}(\x)=\chi_{\alpha_M}(\x)$$
:::

Then, from the properties of the trace and determinant, we obtain

$$\tr_{M/A}(\alpha+\beta)=\tr_{M/A}(\alpha)+\tr_{M/A}(\beta),\qquad \tr_{M/A}(\alpha\beta)=\tr_{M/A}(\beta\alpha),\qquad N_{M/A}(\alpha\beta)=N_{M/A}(\alpha)N_{M/A}(\beta)$$

We also saw in the previous post that these can be viewed as the trace, determinant, and characteristic polynomial of a matrix.

In particular, suppose that a commutative $A$-algebra $A'$ is given. Then via $M'=A'\otimes_AM$ and $E'=A'\otimes_AE$, we can regard $M'$ as an $E'$-module, and since its basis in this case is given by tensoring $1\in A'$ with $M$'s $A$-basis, we see again from the matrix representation that

$$\tr_{M'/A'}(1 \otimes \alpha) = \tr_{M/A}(\alpha) \cdot 1,\qquad N_{M'/A'}(1 \otimes \alpha) = N_{M/A}(\alpha) \cdot 1,\qquad\chi_{M'/A',1 \otimes \alpha}(\x) = \chi_{M/A,\alpha}(\x) \cdot 1
$$

In particular, when $A' = A[\x]$,

$$\chi_{M/A,\alpha}(\x) = N_{M[\x]/A[\x]}(\x - \alpha)$$

holds.

A notable fact is that the above choice depends only on the isomorphism class of $M$. This is because if there is an isomorphism from $M$ to $M'$ as $E$-modules, then along this isomorphism the basis of $M$ is carried to a basis of $M'$, and representing $\alpha_{M'}$ as a matrix with respect to this basis is the same as representing $\alpha_M$ as a matrix with respect to the original basis. The following proposition can also be proved in a similar manner.

::: Proposition 2
Let a decreasing sequence of submodules of an $E$-module $M$

$$M = M_0 \supset M_1 \supset \cdots \supset M_r = \{0\}$$

be given, and suppose each $P_i := M_{i-1}/M_i$ has a finite basis as an $A$-module.

Then $M$ also has a finite basis as an $A$-module, and for all $\alpha \in E$, the following formulas

$$\tr_{M/A}(\alpha) = \sum_{i=1}^r \tr_{P_i/A}(\alpha),\qquad
N_{M/A}(\alpha) = \prod_{i=1}^r N_{P_i/A}(\alpha),\qquad
\chi_{M/A,\alpha}(\x) = \prod_{i=1}^r \chi_{P_i/A,\alpha}(\x)$$

hold.
:::

::: Proof
For $P_i$, let an $A$-basis be $\mathcal{B}_i'$. Lifting these, in $M_{i-1}$ we can extend them to a basis of a supplementary $A$-submodule $\mathcal{B}_i$, and their union $\mathcal{B} = \bigcup \mathcal{B}_i$ becomes $M$'s $A$-basis. Now for each $\alpha \in E$, letting the matrix of the endomorphism $\alpha_{P_i}$ with respect to $\mathcal{B}_i'$ be $X_{ii}$, the full matrix of $\alpha_M$

$$\alpha_M \sim
\begin{pmatrix}
X_{rr} & \ast  & \cdots & \ast  \\
0 & X_{r-1,r-1} & \cdots & \ast  \\
\vdots & \ddots & \ddots & \vdots \\
0 & \cdots & 0 & X_{11}
\end{pmatrix}$$

has a block upper-triangular form with each diagonal block being $X_{ii}$. Now, since the trace is given by the sum of the traces of the diagonal blocks, the determinant by the product of the determinants of the diagonal blocks, and the characteristic polynomial by the product of the characteristic polynomials of the diagonal blocks, the proposition follows.
:::

By the same principle, the following holds.

::: Proposition 3
Let $E, E'$ be $A$-algebras, and let $M$ and $M'$ be an $E$-module and an $E'$-module, respectively.  
Suppose that $M$ and $M'$ are free as $A$-modules, of ranks $n$ and $n'$, respectively. If we regard $M \otimes_A M'$ as an $E \otimes_A E'$-module, then for any $\alpha \in E$ and $\alpha' \in E'$, the following formulas

$$\tr_{M \otimes M'/A}(\alpha \otimes \alpha') = \tr_{M/A}(\alpha) \cdot \tr_{M'/A}(\alpha'),\qquad N_{M \otimes M'/A}(\alpha \otimes \alpha') = N_{M/A}(\alpha)^{n'} \cdot N_{M'/A}(\alpha')^n$$

hold.
:::

Essentially, the norm is the determinant, and since the determinant is a tool for determining the invertibility of a matrix, it is not surprising that the following holds.

::: Proposition 4
Let $E$ be an $A$-algebra having a finite $A$-basis.  
$\alpha \in E$ is invertible if and only if $N_{E/A}(\alpha)$ is invertible in $A$.
:::
::: Proof
Suppose that $\alpha$ has in $E$ an inverse $\alpha' \in E$. Then

$$N_{E/A}(\alpha)N_{E/A}(\alpha') = N_{E/A}(\alpha\alpha') = N_{E/A}(1) = 1$$

so $N_{E/A}(\alpha)$ is invertible in $A$.

Conversely, suppose that $N_{E/A}(\alpha)$ is invertible in $A$. Then the $A$-module endomorphism

$$h : x \mapsto \alpha x$$

is injective, and since $E$ is finitely generated, $h$ is bijective. Now if we take an element satisfying $\alpha\alpha' = 1$, say $\alpha' \in E$, then

$$h(\alpha'\alpha- 1) = \alpha\alpha'\alpha - \alpha = (\alpha\alpha' - 1)\alpha = 0$$

so $\alpha'\alpha = 1$, and $\alpha'$ is the inverse of $\alpha$.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
