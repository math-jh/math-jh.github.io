---title: "Norms and Traces"
excerpt: "The norm and trace defined by elements of an algebra"

categories: [Math / Multilinear Algebra]
permalink: /en/math/multilinear_algebra/norms_and_traces
header:
    overlay_image: /assets/images/Math/Multilinear_Algebra/Norms_and_Traces.png
    overlay_filter: 0.5
sidebar: 
    nav: "multilinear_algebra-en"

date: 2024-10-13
last_modified_at: 2025-04-13
weight: 12
translated_at: 2026-05-28T11:36:15+00:00
translation_source: kimi-cli
---
## Definition of Norms and Traces

As always, let a commutative ring $$A$$ be given, and now let a unital associative $$A$$-algebra $$E$$ be given. Then any $$E$$-module can always be regarded as an $$A$$-module via restriction of scalars.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let an $$E$$-module $$M$$ be given, and suppose that $$M$$ has a finite basis as an $$A$$-module. For any $$\alpha\in E$$, let the following $$E$$-module endomorphism

$$\alpha_M: x\mapsto \alpha x$$

be given. Then we call the trace, determinant, and characteristic polynomial of $$\alpha_M$$ the *trace*, *norm*, and *characteristic polynomial* of $$\alpha$$, respectively, and denote them by

$$\tr_{M/A}(\alpha)=\tr(\alpha_M),\qquad N_{M/A}(\alpha)=\det(\alpha_M),\qquad \chi_{M/A,\alpha}(\x)=\chi_{\alpha_M}(\x)$$

</div>

Then from the properties of trace and determinant we obtain

$$\tr_{M/A}(\alpha+\beta)=\tr_{M/A}(\alpha)+\tr_{M/A}(\beta),\qquad \tr_{M/A}(\alpha\beta)=\tr_{M/A}(\beta\alpha),\qquad N_{M/A}(\alpha\beta)=N_{M/A}(\alpha)N_{M/A}(\beta)$$

We also saw in the previous post that these can be viewed as the trace, determinant, and characteristic polynomial of a matrix. 

In particular, let a commutative $$A$$-algebra $$A'$$ be given. Then via $$M'=A'\otimes_AM$$ and $$E'=A'\otimes_AE$$ we can regard $$M'$$ as an $$E'$$-module, and the basis in this case is given by tensoring $$1\in A'$$ with an $$E$$-basis of $$M$$, so again from the matrix representation 

$$\tr_{M'/A'}(1 \otimes \alpha) = \tr_{M/A}(\alpha) \cdot 1,\qquad N_{M'/A'}(1 \otimes \alpha) = N_{M/A}(\alpha) \cdot 1,\qquad\chi_{M'/A',\,1 \otimes \alpha}(x) = \chi_{M/A,\,\alpha}(x) \cdot 1
$$

we know. In particular, when $$A' = A[\x]$$,

$$\chi_{M/A,\,\alpha}(\x) = N_{M[\x]/A[\x]}(\x - \alpha)$$

holds.

A notable fact is that the above choice depends only on the isomorphism class of $$M$$. This is because if there is an isomorphism from $$M$$ to $$M'$$, then the basis of $$M$$ moves to a basis of $$M'$$ along this isomorphism, and the matrix representation of $$\alpha_{M'}$$ with respect to this basis is the same as the matrix representation of $$\alpha_M$$ with respect to the original basis. The following proposition can also be proved in a similar way.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let a decreasing sequence of submodules of an $$E$$-module $$M$$

$$M = M_0 \supset M_1 \supset \cdots \supset M_r = \{0\}$$

be given, and suppose each $$P_i := M_{i-1}/M_i$$ is finitely generated as an $$A$$-module. 

Then $$M$$ also has a finite basis as an $$A$$-module, and for every $$\alpha \in E$$ the following formulas

$$\tr_{M/A}(\alpha) = \sum_{i=1}^r \tr_{P_i/A}(\alpha),\qquad
N_{M/A}(\alpha) = \prod_{i=1}^r N_{P_i/A}(\alpha),\qquad
\chi_{M/A,\alpha}(x) = \prod_{i=1}^r \chi_{P_i/A,\alpha}(x)$$

hold. 

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$\mathcal{B}_i'$$ be an $$A$$-basis of $$P_i$$. Lifting these, we can extend them to a basis of a supplementary $$A$$-submodule $$\mathcal{B}_i$$ of $$M_{i-1}$$, and their union $$\mathcal{B} = \bigcup \mathcal{B}_i$$ becomes an $$A$$-basis of $$M$$. Now for each $$\alpha \in E$$, let $$X_{ii}$$ be the matrix of the endomorphism $$\alpha_{P_i}$$ with respect to $$\mathcal{B}_i$$; then the full matrix of $$\alpha_M$$

$$e_M \sim
\begin{pmatrix}
X_{rr} & * & \cdots & * \\
0 & X_{r-1,r-1} & \cdots & * \\
\vdots & \ddots & \ddots & \vdots \\
0 & \cdots & 0 & X_{11}
\end{pmatrix}$$

has a block upper-triangular form with diagonal blocks $$X_{ii}$$. Since the trace is given by the sum of the diagonal entries, the determinant by the product of the diagonal entries, and the characteristic polynomial by the product of the diagonal terms, the proposition holds.

</details>

By the same principle, the following holds. 

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let $$E$$ and $$E'$$ be $$A$$-algebras, and let $$M$$ and $$M'$$ be an $$E$$-module and an $$E'$$-module, respectively.  
Suppose that $$M$$ and $$M'$$ are free as $$A$$-modules, of ranks $$n$$ and $$n'$$, respectively. If we regard $$M \otimes_A M'$$ as an $$E \otimes_A E'$$-module, then for any $$\alpha \in E$$ and $$\alpha' \in E'$$ the following formulas

$$\tr_{M \otimes M'/A}(\alpha \otimes \alpha') = \tr_{M/A}(\alpha) \cdot \tr_{M'/A}(\alpha'),\qquad N_{M \otimes M'/A}(\alpha \otimes \alpha') = N_{M/A}(\alpha)^{n'} \cdot N_{M'/A}(\alpha')^n$$

hold. 

</div>

Now we get to the heart of the matter. Essentially, the norm is the determinant, and since the determinant is the tool that determines the invertibility of a matrix, it is not surprising that the following holds. 

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $$E$$ be an $$A$$-algebra having a finite $$A$$-basis.  
Then $$\alpha \in E$$ is invertible if and only if $$N_{E/A}(\alpha)$$ is invertible in $$A$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose that $$\alpha$$ has an inverse $$\alpha' \in E$$ in $$E$$. Then

$$N_{E/A}(\alpha)N_{E/A}(\alpha') = N_{E/A}(\alpha\alpha') = N_{E/A}(1) = 1$$

so $$N_{E/A}(\alpha)$$ is invertible in $$A$$.

Conversely, suppose that $$N_{E/A}(\alpha)$$ is invertible in $$A$$. Then the $$A$$-module endomorphism

$$h : x \mapsto \alpha x$$

is injective, and since $$E$$ is finitely generated, $$h$$ is bijective. Now if we take $$\alpha' \in E$$ such that $$\alpha\alpha' = 1$$, then

$$h(\alpha'\alpha- 1) = \alpha\alpha'\alpha - \alpha = (\alpha'\alpha - 1)\alpha = 0$$

so $$\alpha'\alpha = 1$$, and $$\alpha'$$ becomes the inverse of $$\alpha$$.

</details>
