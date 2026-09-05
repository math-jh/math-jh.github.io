---
title: "Direct Product of Groups"
description: "We define the direct product of groups from a categorical perspective and cover the process of constructing the direct product group via an operation defined on the Cartesian product. We prove the universal property of the product and show that the product of a family of groups is uniquely determined up to isomorphism."
excerpt: "Direct product of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/direct_products
sidebar: 
    nav: "algebraic_structures-en"

date: 2021-10-31
weight: 7
translated_at: 2026-08-16T10:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-05T07:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Products of Groups

We know how to define products in an arbitrary category $\mathcal{A}$. ([[Category Theory] §Limits, ⁋Example 6](/en/math/category_theory/limits#ex6)) The following lemma shows that arbitrary products in the category $\Grp$ always exist. 

::: Lemma 1
$\Grp$ has arbitrary products and, in particular, is a cartesian monoidal category. ([[Category Theory] §Monoidal Categories](/en/math/category_theory/monoidal_categories))
:::
::: Proof
First, in $\Set$, the product set $\prod_{i\in I} G_i$ satisfying the universal property of products was already defined in [[Set Theory] §Product of Sets, ⁋Definition 1](/en/math/set_theory/product_of_sets#def1). For notational convenience, an element of $\prod_{i\in I}G_i$, $f:I\rightarrow \bigcup G_i$, is written as a tuple $(a_i)_{i\in I}$.

Now, for any two elements of the set $\prod_{i\in I}G_i$, $x=(x_i)_{i\in I},y=(y_i)_{i\in I}$, define

$$xy=(x_i)_{i\in I}(y_i)_{i\in I}=(x_iy_i)_{i\in I}$$

Then $\prod_{i\in I}G_i$ has the structure of a group under this operation, and we see that the identity element is $(e_i)_{i\in I}$ and the inverse of $x=(x_i)_{i\in I}$ is $(x_i^{-1})_{i\in I}$. Moreover, for any $j\in I$,

$$\pr_j(xy)=\pr_j(x_iy_i)_{i\in I}=x_jy_j=\pr_j(x)\pr_j(y)$$

so $\pr_j$ is a group homomorphism. 

Now let us prove that $(G=\prod_{i\in I}G_i,(\pr_i)_{i\in I})$ defined in this way satisfies the universal property. For this, it suffices to show that the function $f:H\rightarrow G$ obtained from the universal property of the product set is a group homomorphism. Now, for any $x,y\in H$ and any $i\in I$,

$$f(xy)=(f_i(xy))_{i\in I}=(f_i(x)f_i(y))_{i\in I}=(f_i(x))_{i\in I}(f_i(y))_{i\in I}=f(x)f(y)$$

so $f$ is a group homomorphism, and therefore $(G=\prod_{i\in I}G_i,(\pr_i)_{i\in I})$ above satisfies the universal property. 
:::

The following corollaries are also immediate from the universal property of products. 

::: Corollary 2
For a family $(G_i)$ of groups, the product of this family is uniquely determined up to a unique isomorphism. 
:::
::: Proof
A terminal object in any category is uniquely determined up to a unique isomorphism.
:::

::: Corollary 3
Let $(G_i)$ and $(H_i)$ be families of groups having the same set $I$ as their index set, and suppose that for each $i$, a group homomorphism $f_i:G_i\rightarrow H_i$ is given. Then there exists a unique group homomorphism $f:\prod G_i\rightarrow\prod H_i$ making the following diagram

{% diagram Math/Algebraic_Structures/Direct_Products-1.svg width="13.07em" alt="Product_of_map" %}

commute. In this case, $\ker f=\prod\ker f_i$ and $\im f=\prod\im f_i$.
:::
::: Proof
$\prod H_i$ is the terminal object of the collection of cones satisfying the given condition. ([[Category Theory] §Limits, §§Universal Property of Limits](/en/math/category_theory/limits#universal-property-of-limits)) From the commutative diagram defined in this way,

$$x\in\ker f\iff f(x)=e\iff \forall i(\pr_i^H(f(x))=e_i)\iff \forall i((f_i\circ \pr_i^G)(x)=e_i)\iff \forall i(\pr_i^G(x)\in\ker f_i)$$

so $\ker f=\prod\ker f_i$ holds.

Similarly, for $y\in\prod H_i$, having $y\in\im f$ is equivalent to $y=f(x)$ for some $x\in\prod G_i$, and for such $x$,

$$\pr_i^H(y)=\pr_i^H(f(x))=f_i(\pr_i^G(x))\in\im f_i$$

so $\im f\subseteq\prod\im f_i$ holds. Conversely, if $y\in\prod\im f_i$ is given, then for each $i\in I$ we can choose, satisfying $f_i(x_i)=\pr_i^H(y)$, an element $x_i\in G_i$ ([[Set Theory] §Axiom of Choice, ⁋The Axiom of Choice.](/en/math/set_theory/axiom_of_choice#axiom-choice)), and setting $x=(x_i)_{i\in I}$ gives $f(x)=y$, so $\im f=\prod\im f_i$ also holds.
:::

::: Corollary 4
Let a family $(G_i)_{i\in I}$ of groups be given. If for each $i\in I$ the $H_i$ are normal subgroups of $G_i$, then $\prod H_i$ is also a normal subgroup of $\prod G_i$, and its quotient group is equal to $\prod (G_i/H_i)$.
:::
::: Proof
It suffices to apply [Corollary 3](#cor3) to the canonical homomorphisms $p_i:G_i\rightarrow G_i/H_i$.

{% diagram Math/Algebraic_Structures/Direct_Products-2.svg width="18.32em" alt="product_of_normal_subgroups" %}

Each $p_i\circ\pr_i$ is a composition of surjective homomorphisms and thus surjective; therefore, by the preceding corollary, $\im p$ is equal to $\prod(G_i/H_i)$. Also, the kernel of each $p_i$ is equal to $H_i$. Therefore, by the first isomorphism theorem,

$$\biggl(\prod_{i\in I} G_i\biggr)\bigg/\biggl(\prod_{i\in I}H_i\biggr)\cong\prod_{i\in I} (G_i/H_i)$$

holds.
:::

Of course, even if the $H_i$ are subgroups of the $G_i$ that are not normal, $\prod H_i$ is a subgroup of $\prod G_i$.

::: Corollary 5
Let a family $(G_i)_{i\in I}$ of groups be given. If for each $i\in I$ we have $H_i\leq G_i$, then $\prod H_i$ is a subgroup of $\prod G_i$.
:::
::: Proof
Applying [Corollary 3](#cor3) to the inclusion homomorphisms $\iota_i:H_i\hookrightarrow G_i$, $\iota$ is injective, and since $\prod H_i$ is precisely the image of $\iota$, it is a subgroup of $\prod G_i$.
:::

## Partial Products

The above corollaries are especially useful in the following situation. 

Let $(G_i)_{i\in I}$ be a family of groups, and for $I$, consider a subset $J$. Then the product $\prod_{j\in J}G_j$ is well-defined. On the other hand, consider, defined by the following formula

$$G_i'=\begin{cases} G_i&i\in J\\ \{e\}&i\not\in J\end{cases}$$

the family $(G_i')$ of groups, and the group homomorphisms from $G_i'$ to $G_i$

$$f_i=\begin{cases} \id_{G_i}&i\in J\\ \iota_i&i\not\in J\end{cases}$$

Then one can show without difficulty that $\prod_{i\in I}G_i'\cong\prod_{j\in J}G_j$, and therefore by [Corollary 4](#cor4) one can verify that the following formula

$$\biggl(\prod_{i\in I}G_i\biggr)\bigg/\biggl(\prod_{j\in J}G_j\biggr)\cong\prod_{i\in I\setminus J} G_i$$

holds. 

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
