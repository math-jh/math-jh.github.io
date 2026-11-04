---
title: "Properties of Products"
description: "We define the partial product of a product set and the associative law, and prove the associativity of product sets using composition of component functions. We also cover the existence of a bijection via partitioning and a proof using the universal property."
excerpt: "Partial products, associativity and associativity"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/property_of_products


sidebar: 
    nav: "set_theory-en"

date: 2022-11-25

weight: 11
translated_at: 2026-06-02T20:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-11-04T11:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Partial Products and Associativity

To discuss the associativity of products of sets, we must first define partial products.

::: Definition 1
Let a family $(A_i)_{i\in I}$ and its product $\prod_{i\in I} A_i$ be given. Then for a subset $J\subseteq I$ of the index set, we call $\prod_{j\in J} A_j$ a *partial product*.
:::

For the product $\prod_{i\in I}A_i$, let a partial product $\prod_{j\in J}A_j$ be given. Then for any $F\in\prod_{i\in I}A_i$,

$$\biggl(F\circ\Delta_J, J, \bigcup_{j\in J} A_j\biggr)$$

is a new function, and for each $j$ it satisfies $(F\circ\Delta_J)(j)=F(j)\in A_j$. That is, $F\circ\Delta_J$ is an element of $\prod_{j\in J}A_j$.

By the above paragraph, $F\mapsto F\circ\Delta_J$ defines a function from $\prod_{i\in I}A_i$ to $\prod_{j\in J}A_j$. Borrowing the notation for projection functions, we denote this by $\pr_J$. Then for $K\subseteq J\subseteq I$, the composition of the projection from the product set $\prod_{i\in I}A_i$ to the partial product $\prod_{j\in J}A_j$ (the $J$-th projection) and the projection from the product set $\prod_{j\in J}A_j$ to the partial product $\prod_{k\in K}A_k$ of this product set (the $K$-th projection)

$$\prod_{i\in I}A_i\rightarrow \prod_{j\in J}A_j\rightarrow \prod_{k\in K}A_k$$

is simply equal to the projection from the product set $\prod_{i\in I}A_i$ to the partial product $\prod_{k\in K}A_k$ of this product set, namely the $K$-th projection $\pr_K$. This is because $\Delta_K=\Delta_J\circ\Delta_K$.

::: Proposition 2
Consider a family $(A_i)_{i\in I}$ whose components are all non-empty, and let $J\subseteq I$. If $g:J\rightarrow\bigcup_{i\in I} A_i$ satisfies $g(j)\in A_j$, then there exists an extension $f:I\rightarrow\bigcup_{i\in I} A_i$ of $g$ such that $f(i)\in A_i$.
:::

::: Proof
Let $g=(G,J,\bigcup A_i)$. For each $i\in I\setminus J$, since $A_i$ is non-empty, we can choose an element $x_i\in A_i$. Now if we define

$$F=G\cup\biggl(\bigcup_{i\in I\setminus J}\{(i, x_i)\}\biggr)$$

and set $f=(F,I,\bigcup A_i)$, we obtain the desired result.
:::

::: Proposition 3
Let a family $(A_i)_{i\in I}$ with a non-empty index set $I$ be given. If $(J_k)_{k\in K}$ is a partition of $I$, then the function $f\mapsto (\pr_{J_k}(f))_{k\in K}$ from $\prod_{i\in I}A_i$ to $\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$ is also a bijection.
:::

::: Proof
Since $(J_k)_{k\in K}$ is a partition, $f_k:J_k\rightarrow \bigcup_{i\in I} A_i$ is a family of functions with pairwise disjoint domains; hence by applying [§Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2){: data-lid="dcwv6" } we obtain a bijection.
:::

While the proof above is concise, the following proof using the universal property is also beautiful.

::: Proof (Proposition 3)
For notational cleanliness, let us uniformly denote:

- the $k$-th projection of the product $\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$ with respect to the index set $K$

  $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{j\in J_k}A_j$$

  by $\pr_k$,
- the $j$-th projection of the product $\prod_{j\in J_k}A_j$ with respect to the index set $J_k$

  $$\prod_{j\in J_k}A_j\rightarrow A_j$$

  also by $\pr_j$,
- the $i$-th projection of the product $\prod_{i\in I}A_i$ with respect to the index set $I$

  $$\prod_{i\in I}A_i\rightarrow A_i$$

  also by $\pr_i$.

While this may cause some confusion in text, in diagrams both the source and the target are explicitly specified, so there is no room for confusion.

Since $(J_k)_{k\in K}$ is a partition of $I$, for each $i\in I$ there exists a unique $k\in K$ such that $i\in J_k$. Now define the function $\pr_{ik}$ as the composition

$$\pr_{ik}:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\overset{\pr_k}{\rightarrow}\prod_{j\in J_k}A_j\overset{\pr_i}{\rightarrow}A_i$$

Then by the universal property of the product $\prod_{i\in I}A_i$, we know that there exists $\phi:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{i\in I}A_i$ making the following diagram commute:

{% diagram Math/Set_Theory/Property_of_Products-1.svg width="18.53em" alt="partial_product_pf_1" %}

Similarly, by the universal property of the product $\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$ with respect to the index set $K$, we know that there exists $\psi:\prod_{i\in I}A_i\rightarrow\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$ making the following diagram commute:

{% diagram Math/Set_Theory/Property_of_Products-2.svg width="24.93em" alt="partial_product_pf_2" %}

Then $\phi\circ\psi$ and $\psi\circ\phi$ are each identity functions, and thus they become the desired bijections.

For example, let us show that $\phi\circ\psi$ is the identity function from $\prod_{i\in I}A_i$ to itself. For this, it suffices to show that for all $i\in I$ the following diagram commutes:

{% diagram Math/Set_Theory/Property_of_Products-3.svg width="8.51em" alt="partial_product_pf_3" %}

The universal property of the product means that there exists a *unique* function $\prod_{i\in I}A_i\rightarrow \prod_{i\in I}A_i$ making the above diagram commute; naturally, the identity function from $\prod_{i\in I}A_i$ to itself also makes the above diagram commute, and therefore by uniqueness this function must equal $\phi\circ\psi$.

Now from

$${\pr_i}\circ(\phi\circ\psi)=({\pr_i}\circ\phi)\circ\psi={\pr_{ik}}\circ\psi={\pr_i}\circ({\pr_k}\circ\psi)={\pr_i}\circ{\pr_{J_k}}=\pr_i$$

we obtain the desired conclusion. (The last equality regards $\pr_i$ as the projection onto $\{i\}\subseteq I$.) Although this equation appears complicated, it is merely writing as a formula that the following diagram commutes:

{% diagram Math/Set_Theory/Property_of_Products-4.svg width="17.00em" alt="partial_product_pf_4" %}
:::

Let $(A_i)_{i\in I}$ and $(B_i)_{i\in I}$ be families with the same index set, and let a family of functions $(g_i:A_i\rightarrow B_i)_{i\in I}$ be given. If we define $u_f:I\rightarrow\bigcup_{i\in I}B_i$ by $i\mapsto g_i(f(i))$, then $u_f(i)\in B_i$, and therefore $u_f\in\prod_{i\in I}B_i$.

::: Definition 4
The function $f\mapsto u_f$ defined above is called the *product* of the $(g_i)$ and is denoted by $\prod_{i\in I}g_i$.
:::

::: Proposition 5
Let $(A_i)_{i\in I}$, $(B_i)_{i\in I}$, and $(C_i)_{i\in I}$ be three families, and let $(f_i)_{i\in I}$ and $(g_i)_{i\in I}$ be families of functions from $A_i$ to $B_i$ and from $B_i$ to $C_i$, respectively. Then

$$\prod_{i\in I} (g_i\circ f_i)=\left(\prod_{i\in I} g_i\right)\circ\left(\prod_{i\in I}f_i\right)$$

holds.
:::
::: Proof
There is nothing to explain beyond the following two commutative diagrams:

{% diagram Math/Set_Theory/Property_of_Products-5.svg width="14.31em" alt="composition_of_product_functions" %}

and

{% diagram Math/Set_Theory/Property_of_Products-6.svg width="16.81em" alt="composition_of_product_fuctions_2" %}
:::

Since it is obvious that the product of the $\id_{A_i}$ is $\id_{\prod A_i}$, it is also clear by the above proposition that the product of injective functions is injective and the product of surjective functions is surjective.


## Distributivity Between Operations

Meanwhile, if two or more operations are defined, whether distributivity holds is an important concern.

::: Proposition 6
Let $((A_{k,i})_{i\in J_k})_{k\in K}$ be a family of families of sets. Suppose further that $K\neq\emptyset$, and that $J_k\neq\emptyset$ holds for all $k\in K$. Then for $I=\prod_{k\in K} J_k\neq\emptyset$,

$$\bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)=\bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right),\quad\bigcap_{k\in K}\left(\bigcup_{i\in J_k}A_{k,i}\right)=\bigcup_{f\in I}\left(\bigcap_{k\in K}A_{k,f(k)}\right)$$

holds.
:::

::: Proof
First, let $x\in \bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)$. We must show that $x\in \bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right)$, that is, $x\in \bigcup_{k\in K}A_{k,f(k)}$ for all $f\in I$. Since $x\in \bigcap_{i\in J_k}A_{k,i}$ for some $k\in K$, we have $x\in A_{k,f(k)}$. Therefore, $x\in \bigcup_{k\in K}A_{k,f(k)}$ holds for all $f$, and hence the inclusion holds.  

To show the reverse inclusion, let us use the contrapositive. That is, let $x\not\in \bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)$. Then for all $k\in K$, we have $x\not\in \bigcap_{i\in J_k}A_{k,i}$. Thus for each $k$, there exists $i_k\in J_k$ such that $x\not\in A_{k,i_k}$. Now if we choose $f\in I$ such that $f(k)=i_k$, then $x\not\in\bigcup_{k\in K}A_{k,f(k)}$, and therefore it does not belong to the right-hand side. The second equation can be shown similarly.
:::

Distributivity also holds between product and union, and between product and intersection, as follows; the proof is almost identical to the above, so we omit it.

::: Proposition 7
Let $((A_{k,i})_{i\in J_k})_{k\in K}$ be a family of families of sets, and define $I$ as in the proposition above. Then 

$$\prod_{k\in K}\left(\bigcup_{i\in J_k}A_{k,i}\right)=\bigcup_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right),\quad\prod_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)=\bigcap_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right)$$

holds.
:::

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
