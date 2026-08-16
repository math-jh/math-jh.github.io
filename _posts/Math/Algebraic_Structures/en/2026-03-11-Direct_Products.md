---
title: "Direct Product of Groups"
description: "We define the direct product of groups from a categorical perspective and construct the product group via operations on the Cartesian product. The universal property of the product is proved, and uniqueness up to isomorphism is established."
excerpt: "Categorical definition and universal property of group products"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/direct_products
sidebar: 
    nav: "algebraic_structures-en"

date: 2021-10-31
weight: 7
translated_at: 2026-08-16T10:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-16T10:15:04+00:00
---
## Products of Groups

We know how to define products in an arbitrary category $\mathcal{A}$. ([[Category Theory] §Limits, ⁋Example 6](/en/math/category_theory/limits#ex6)) The following lemma shows that arbitrary products always exist in the category $\Grp$.

::: Lemma 1
$\Grp$ has arbitrary products; in particular, it is a cartesian monoidal category. ([[Category Theory] §Monoidal Categories](/en/math/category_theory/monoidal_categories))
:::
::: Proof
First, the product set $\prod_{i\in I} G_i$ satisfying the universal property of products in $\Set$ was already defined in [[Set Theory] §Product of Sets, ⁋Definition 1](/en/math/set_theory/product_of_sets#def1). For notational convenience, we write an element $f:I\rightarrow \bigcup G_i$ of $\prod_{i\in I}G_i$ as a tuple $(a_i)_{i\in I}$.

Now, for any two elements $x=(x_i)_{i\in I}$ and $y=(y_i)_{i\in I}$ of the set $\prod_{i\in I}G_i$, define

$$xy=(x_i)_{i\in I}(y_i)_{i\in I}=(x_iy_i)_{i\in I}.$$

Then $\prod_{i\in I}G_i$ becomes a group under this operation; its identity element is $(e_i)_{i\in I}$, and the inverse of $x=(x_i)_{i\in I}$ is $(x_i^{-1})_{i\in I}$. Moreover, for any $j\in I$,

$$\pr_j(xy)=\pr_j(x_iy_i)_{i\in I}=x_jy_j=\pr_j(x)\pr_j(y),$$

so each $\pr_j$ is a group homomorphism.

We now prove that $(G=\prod_{i\in I}G_i,(\pr_i)_{i\in I})$ satisfies the universal property. For this, it suffices to show that the map $f:H\rightarrow G$ furnished by the universal property of the product set is a group homomorphism. For any $x,y\in H$ and any $i\in I$,

$$f(xy)=(f_i(xy))_{i\in I}=(f_i(x)f_i(y))_{i\in I}=(f_i(x))_{i\in I}(f_i(y))_{i\in I}=f(x)f(y),$$

so $f$ is a group homomorphism; therefore $(G=\prod_{i\in I}G_i,(\pr_i)_{i\in I})$ satisfies the universal property.
:::

The following corollaries are also immediate consequences of the universal property of products.

::: Corollary 2
For a family of groups $(G_i)$, the product of this family is uniquely determined up to a unique isomorphism.
:::
::: Proof
A terminal object in any category is uniquely determined up to a unique isomorphism.
:::

::: Corollary 3
Let $(G_i)$ and $(H_i)$ be families of groups indexed by the same set $I$, and suppose a group homomorphism $f_i:G_i\rightarrow H_i$ is given for each $i$. Then there exists a unique group homomorphism $f:\prod G_i\rightarrow\prod H_i$ making the following diagram

{% diagram Math/Algebraic_Structures/Direct_Products-1.svg width="13.07em" alt="Product_of_map" %}

commute. In this case, $\ker f=\prod\ker f_i$ and $\im f=\prod\im f_i$.
:::
::: Proof
$\prod H_i$ is the terminal object of the collection of cones satisfying the given condition. ([[Category Theory] §Limits, §§Universal Property of Limits](/en/math/category_theory/limits#universal-property-of-limits)) From the commutative diagram thus defined,

$$x\in\ker f\iff f(x)=e\iff \forall i(\pr_i^H(f(x))=e_i)\iff \forall i((f_i\circ \pr_i^G)(x)=e_i)\iff \forall i(\pr_i^G(x)\in\ker f_i),$$

so $\ker f=\prod\ker f_i$.

Similarly, for $y\in\prod H_i$, the condition $y\in\im f$ is equivalent to the existence of $x\in\prod G_i$ with $y=f(x)$, and for such $x$,

$$\pr_i^H(y)=\pr_i^H(f(x))=f_i(\pr_i^G(x))\in\im f_i,$$

so $\im f\subseteq\prod\im f_i$. Conversely, given $y\in\prod\im f_i$, for each $i\in I$ we can choose $x_i\in G_i$ such that $f_i(x_i)=\pr_i^H(y)$ ([[Set Theory] §Axiom of Choice, ⁋The Axiom of Choice.](/en/math/set_theory/axiom_of_choice#axiom-choice)); setting $x=(x_i)_{i\in I}$, we obtain $f(x)=y$, so $\im f=\prod\im f_i$ also holds.
:::

::: Corollary 4
Let $(G_i)_{i\in I}$ be a family of groups. If for each $i\in I$ the $H_i$ are normal subgroups of $G_i$, then $\prod H_i$ is also a normal subgroup of $\prod G_i$, and its quotient group is isomorphic to $\prod (G_i/H_i)$.
:::
::: Proof
Apply [Corollary 3](#cor3) to the canonical homomorphisms $p_i:G_i\rightarrow G_i/H_i$.

{% diagram Math/Algebraic_Structures/Direct_Products-2.svg width="18.32em" alt="product_of_normal_subgroups" %}

Each $p_i\circ\pr_i$ is a composition of surjective homomorphisms, hence surjective, and therefore by the preceding corollary $\im p$ equals $\prod(G_i/H_i)$. Also, the kernel of each $p_i$ is $H_i$. Thus, by the first isomorphism theorem,

$$\biggl(\prod_{i\in I} G_i\biggr)\bigg/\biggl(\prod_{i\in I}H_i\biggr)\cong\prod_{i\in I} (G_i/H_i)$$

holds.
:::

Of course, even if the $H_i$ are not normal subgroups of the $G_i$, the product $\prod H_i$ is still a subgroup of $\prod G_i$.

::: Corollary 5
Let $(G_i)_{i\in I}$ be a family of groups. If $H_i\leq G_i$ for each $i\in I$, then $\prod H_i$ is a subgroup of $\prod G_i$.
:::
::: Proof
Applying [Corollary 3](#cor3) to the inclusion homomorphisms $\iota_i:H_i\hookrightarrow G_i$, the map $\iota$ is injective and $\prod H_i$ is exactly the image of $\iota$, hence a subgroup of $\prod G_i$.
:::

## Partial Products

The above corollaries are especially useful in the following situation.

Let $(G_i)_{i\in I}$ be a family of groups, and consider a subset $J\subseteq I$. Then the product $\prod_{j\in J}G_j$ is well defined. On the other hand, define a family of groups $(G_i')$ by

$$G_i'=\begin{cases} G_i&i\in J\\ \{e\}&i\not\in J\end{cases}$$

and consider the group homomorphisms $f_i:G_i'\rightarrow G_i$ given by

$$f_i=\begin{cases} \id_{G_i}&i\in J\\ \iota_i&i\not\in J\end{cases}.$$

Then one easily shows that $\prod_{i\in I}G_i'\cong\prod_{j\in J}G_j$, and thus by [Corollary 4](#cor4) one verifies that

$$\biggl(\prod_{i\in I}G_i\biggr)\bigg/\biggl(\prod_{j\in J}G_j\biggr)\cong\prod_{i\in I\setminus J} G_i$$

holds.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
