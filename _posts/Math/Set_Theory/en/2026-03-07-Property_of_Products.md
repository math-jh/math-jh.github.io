---
title: "Properties of Products"
description: "We define the partial product of a product set and the associative law, and prove the associativity of product sets using composition of component functions. We also cover the existence of a bijection via partitioning and a proof using the universal property."
excerpt: "Partial products, associativity and distributivity"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/property_of_products


sidebar: 
    nav: "set_theory-en"

date: 2022-11-25

weight: 11
translated_at: 2026-06-02T20:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T20:00:01+00:00
---
## Partial Products and Associativity

To discuss whether the product of sets is associative, we must first define partial products.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a family $$(A_i)_{i\in I}$$ and its product $$\prod_{i\in I} A_i$$ be given. Then for a subset $$J\subseteq I$$ of the index set, we call $$\prod_{j\in J} A_j$$ a *partial product*.

</div>

Let a partial product $$\prod_{j\in J}A_j$$ of $$\prod_{i\in I}A_i$$ be given. Then for any $$F\in\prod_{i\in I}A_i$$,

$$f\circ\id_J=\biggl(F\circ\Delta_J, J, \bigcup_{j\in J} A_j\biggr)$$

is a new function, and for each $$j$$ it satisfies $$(f\circ\id_J)(j)=f(j)\in A_j$$. Thus $$F\circ\Delta_J$$ is an element of $$\prod_{j\in J}A_j$$.

By the preceding paragraph, $$F\mapsto F\circ\Delta_J$$ defines a function from $$\prod_{i\in I}A_i$$ to $$\prod_{j\in J}A_j$$. We denote this by $$\pr_J$$, borrowing the notation for projection functions. Then for $$K\subseteq J\subseteq I$$, the composition of the $$J$$-th projection from $$\prod_{i\in I}A_i$$ to the partial product $$\prod_{j\in J}A_j$$ and the $$K$$-th projection from $$\prod_{j\in J}A_j$$ to its partial product $$\prod_{k\in K}A_k$$

$$\prod_{i\in I}A_i\longrightarrow \prod_{j\in J}A_j\longrightarrow \prod_{k\in K}A_k$$

is simply the $$K$$-th projection $$\pr_K$$ from $$\prod_{i\in I}A_i$$ to its partial product $$\prod_{k\in K}A_k$$. This follows from $$\Delta_K=\Delta_J\circ\Delta_K$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Consider a family $$(A_i)_{i\in I}$$ whose every component is non-empty, and let $$J\subseteq I$$. If $$g:J\rightarrow\bigcup_{i\in I} A_i$$ satisfies $$g(j)\in A_j$$, then there exists an extension $$f:I\rightarrow\bigcup_{i\in I} A_i$$ of $$g$$ such that $$f(i)\in A_i$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$g=(G,J,\bigcup A_i)$$. For each $$i\in I\setminus J$$, since $$A_i$$ is non-empty we can choose an element $$x_i\in A_i$$. Now define

$$F=G\cup\biggl(\bigcup_{i\in I\setminus J}\{(i, x_i)\}\biggr)$$

and set $$f=(F,I,\bigcup A_i)$$. This yields the desired result.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let a family $$(A_i)_{i\in I}$$ with non-empty index set $$I$$ be given. If $$(J_k)_{k\in K}$$ is a partition of $$I$$, then the function $$f\mapsto (\pr_{J_k}(f))_{k\in K}$$ from $$\prod_{i\in I}A_i$$ to $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ is also a bijection.

</div>

<details class="proof" markdown="1">
<summary>Proof 1</summary>

Since $$(J_k)_{k\in K}$$ is a partition, the functions $$f_k:J_k\rightarrow \bigcup_{i\in I} A_i$$ form a family of functions with pairwise disjoint domains; hence by [§Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2) we obtain a bijection.

</details>

The proof above is concise, but the following argument using the universal property is equally elegant.

<details class="proof--alone" markdown="1">
<summary>Proof 2</summary>

For notational cleanliness we adopt the following uniform convention:

- The $$k$$-th projection of the product $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ with respect to the index set $$K$$

  $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{j\in J_k}A_j$$

  is denoted by $$\pr_k$$,
- The $$j$$-th projection of the product $$\prod_{j\in J_k}A_j$$ with respect to the index set $$J_k$$

  $$\prod_{j\in J_k}A_j\rightarrow A_j$$

  is also denoted by $$\pr_j$$,
- The $$i$$-th projection of the product $$\prod_{i\in I}A_i$$ with respect to the index set $$I$$

  $$\prod_{i\in I}A_i\rightarrow A_i$$

  is also denoted by $$\pr_i$$

While this may cause some confusion when read in text, in diagrams the source and target are both explicit, so there is no ambiguity.

Since $$(J_k)_{k\in K}$$ is a partition of $$I$$, for each $$i\in I$$ there exists a unique $$k\in K$$ such that $$i\in J_k$$. We now define the function $$\pr_{ik}$$ as the composition

$$\pr_{ik}:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\overset{\pr_k}{\longrightarrow}\prod_{j\in J_k}A_j\overset{\pr_i}{\longrightarrow}A_i$$

Then by the universal property of the product $$\prod_{i\in I}A_i$$, there exists a map $$\phi:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{i\in I}A_i$$ making the following diagram commute:

![partial_product_pf_1](/assets/images/Math/Set_Theory/Property_of_Products-1.svg){:style="width:18.53em" class="invert" .align-center}

Similarly, by the universal property of the product $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ with respect to the index set $$K$$, there exists a map $$\psi:\prod_{i\in I}A_i\rightarrow\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ making the following diagram commute:

![partial_product_pf_2](/assets/images/Math/Set_Theory/Property_of_Products-2.svg){:style="width:24.93em" class="invert" .align-center}

Then $$\phi\circ\psi$$ and $$\psi\circ\phi$$ are both identity functions, and thus they furnish the desired bijection.

For instance, let us verify that $$\phi\circ\psi$$ is the identity on $$\prod_{i\in I}A_i$$. It suffices to show that for every $$i\in I$$ the following diagram commutes:

![partial_product_pf_3](/assets/images/Math/Set_Theory/Property_of_Products-3.svg){:style="width:8.51em" class="invert" .align-center}

The universal property of the product asserts that there is a *unique* function $$\prod_{i\in I}A_i\rightarrow \prod_{i\in I}A_i$$ making the above diagram commute. Clearly the identity on $$\prod_{i\in I}A_i$$ also makes the diagram commute, so by uniqueness it must equal $$\phi\circ\psi$$.

Now from

$${\pr_i}\circ(\phi\circ\psi)=({\pr_i}\circ\phi)\circ\psi={\pr_{ik}}\circ\psi={\pr_i}\circ({\pr_k}\circ\psi)={\pr_j}\circ{\pr_{J_k}}=\pr_j$$

we obtain the desired conclusion. (The last equality regards $$\pr_j$$ as the projection onto $$\{j\}\subseteq I$$.) Although this equation appears complicated, it is merely the formulaic transcription of the statement that the following diagram commutes:

![partial_product_pf_4](/assets/images/Math/Set_Theory/Property_of_Products-4.svg){:style="width:17.00em" class="invert" .align-center}

</details> 

Let $$(A_i)_{i\in I}$$ and $$(B_i)_{i\in I}$$ be families with the same index set, and let a family of functions $$(g_i:A_i\rightarrow B_i)_{i\in I}$$ be given. Define $$u_f:I\rightarrow\bigcup_{i\in I}B_i$$ by $$i\mapsto g_i(f(i))$$; then $$u_f(i)\in B_i$$, and therefore $$u_f\in\prod_{i\in I}B_i$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The function $$f\mapsto u_f$$ defined above is called the *product* of the $$(g_i)$$ and is denoted by $$\prod_{i\in I}g_i$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(A_i)_{i\in I}$$, $$(B_i)_{i\in I}$$, and $$(C_i)_{i\in I}$$ be three families, and let $$(f_i)_{i\in I}$$ and $$(g_i)_{i\in I}$$ be families of functions from $$A_i$$ to $$B_i$$ and from $$B_i$$ to $$C_i$$, respectively. Then

$$\prod_{i\in I} (g_i\circ f_i)=\left(\prod_{i\in I} g_i\right)\circ\left(\prod_{i\in I}f_i\right)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

There is nothing to explain beyond the following two commutative diagrams:

![composition_of_product_functions](/assets/images/Math/Set_Theory/Property_of_Products-5.svg){:style="width:14.31em" class="invert" .align-center}

and

![composition_of_product_fuctions_2](/assets/images/Math/Set_Theory/Property_of_Products-6.svg){:style="width:16.81em" class="invert" .align-center}

</details>

Since it is obvious that the product of the $$\id_{A_i}$$ is $$\id_{\prod A_i}$$, the preceding proposition makes it clear that the product of injective functions is injective, and the product of surjective functions is surjective.


## Distributivity Between Operations

When two or more operations are defined, whether distributivity holds between them is an important question.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$((A_{k,i})_{i\in J_k})_{k\in K}$$ be a family of families of sets. Suppose further that $$K\neq\emptyset$$ and $$J_k\neq\emptyset$$ for all $$k\in K$$. Then for $$I=\prod_{k\in K} J_k\neq\emptyset$$,

$$\bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)=\bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right),\quad\bigcap_{k\in K}\left(\bigcup_{i\in J}A_{k,i}\right)=\bigcup_{f\in I}\left(\bigcap_{k\in K}A_{k,f(k)}\right)$$

hold.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, let $$x\in \bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)$$. We must show that $$x\in \bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right)$$, i.e., that $$x\in \bigcup_{k\in K}A_{k,f(k)}$$ for every $$f\in I$$. Since $$x\in \bigcap_{i\in J_k}A_{k,i}$$ for some $$k\in K$$, we have $$x\in A_{k,f(k)}$$. Hence $$x\in \bigcup_{k\in K}A_{k,f(k)}$$ for all $$f$$, and the inclusion follows.

To establish the reverse inclusion we argue by contrapositive. Suppose $$x\not\in \bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)$$. Then for every $$k\in K$$ we have $$x\not\in \bigcap_{i\in J_k}A_{k,i}$$. Thus there exists some $$i$$ such that $$x\not\in A_{k,i}$$ for every $$k$$. Choosing $$f\in I$$ so that $$f(k)$$ is such an $$i$$, we obtain $$x\not\in\bigcup_{k\in K}A_{k,f(k)}$$, so $$x$$ does not belong to the right-hand side. The second equality is proved similarly.
</details>

Distributivity also holds between product and union, and between product and intersection, as follows; the proof is almost identical to the above, so we omit it.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$((A_{k,i})_{i\in J_k})_{k\in K}$$ be a family of families of sets, and define $$I$$ as in the previous proposition. Then

$$\prod_{k\in K}\left(\bigcup_{i\in J_k}A_{k,i}\right)=\bigcup_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right),\quad\prod_{k\in K}\left(\bigcap_{i\in J}A_{k,i}\right)=\bigcap_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right)$$

hold.

</div>

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
