---

title: "Direct Products of Groups"
excerpt: "Direct product of groups"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/direct_products
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Direct_products.png
    overlay_filter: 0.5
sidebar:
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 7

---

## Products of Groups

We know how to define products in any category $$\mathcal{A}$$. ([\[Category Theory\] §Limits, ⁋Example 6](/en/math/category_theory/limits#ex6)) The following lemma shows that any product in the category $$\Grp$$ always exists.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> $$\Grp$$ is a cartesian monoidal category.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, we already defined the product set $$\prod_{i\in I} G_i$$ satisfying the universal property of products in $$\Set$$ in [\[Set Theory\] §Product of Sets, ⁋Definition 1](/en/math/set_theory/product_of_sets#def1). For notational convenience, we denote elements $$f:I\rightarrow \bigcup G_i$$ of $$\prod_{i\in I}G_i$$ as tuples $$(a_i)_{i\in I}$$.

Now, for any two elements $$x=(x_i)_{i\in I},y=(y_i)_{i\in I}$$ of the set $$\prod_{i\in I}G_i$$, define

$$xy=(x_i)_{i\in I}(y_i)_{i\in I}=(x_iy_i)_{i\in I}$$

Then $$\prod_{i\in I}G_i$$ has a group structure under this operation, with identity element $$(e_i)_{i\in I}$$ and the inverse of $$x=(x_i)_{i\in I}$$ being $$(x_i^{-1})_{i\in I}$$. Also, for any $$j\in I$$,

$$\pr_j(xy)=\pr_j(x_iy_i)_{i\in I}=x_jy_j=\pr_j(x)\pr_j(y)$$

so $$\pr_j$$ is a group homomorphism.

Now we prove that $$(G=\prod_{i\in I}G_i,(\pr_i)_{i\in I})$$ defined in this way satisfies the universal property. For this, it suffices to show that the function $$f:H\rightarrow G$$ obtained from the universal property of product sets is a group homomorphism. Now for any $$x,y\in H$$ and any $$i\in I$$,

$$f(xy)=(f_i(xy))_{i\in I}=(f_i(x)f_i(y))_{i\in I}=(f_i(x))_{i\in I}(f_i(y))_{i\in I}=f(x)f(y)$$

so $$f$$ is a group homomorphism, and thus the above $$(G=\prod_{i\in I}G_i,(\pr_i)_{i\in I})$$ satisfies the universal property.

</details>

The following corollaries are also immediate from the universal property of products.

<div class="proposition" markdown="1">

<ins id="cor2">**Corollary 2**</ins> For a family of groups $$(G_i)$$, their product is uniquely determined up to unique isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

In any category, terminal objects are unique up to unique isomorphism.

</details>

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Let $$(G_i)$$ and $$(H_i)$$ be families of groups with the same index set $$I$$, and suppose group homomorphisms $$f_i:G_i\rightarrow H_i$$ are given for each $$i$$. Then there exists a unique group homomorphism $$f:\prod G_i\rightarrow\prod H_i$$ making the following diagram

![Product_of_map](/assets/images/Math/Algebraic_Structures/Direct_products-1.png){:style="width:12em" class="invert" .align-center}

commute. Moreover, $$\ker f=\prod\ker f_i$$ and $$\im f=\prod\im f_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$\prod H_i$$ is the terminal object of the collection of cones satisfying the given conditions. ([\[Category Theory\] §Limits, §§Universal Property of Limits](/en/math/category_theory/limits#universal-property-of-limits)) By the commutative diagram defined in this way,

$$x\in\ker f\iff f(x)=e\iff \forall i(\pr_i^H(f(x))=e_i)\iff \forall i((f_i\circ \pr_i^G)(x)=e_i)\iff \forall i(\pr_i^G(x)\in\ker f_i)$$

so $$\ker f=\prod\ker f_i$$ holds.

Similarly, for $$y\in\prod H_i$$, $$y\in\im f$$ if and only if there exists $$x\in H_i$$ such that $$y=f(x)$$, and for such $$x$$,

$$\pr_i^H(y)=\pr_i^H(f(x))=f_i(\pr_i^G(x))\in\im f_i$$

so $$\im f=\prod\im f_i$$ also holds.

</details>

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> Let a family of groups $$(G_i)_{i\in I}$$ be given. If for each $$i\in I$$, $$H_i$$ are normal subgroups of $$G_i$$, then $$\prod H_i$$ is also a normal subgroup of $$\prod G_i$$, and its quotient group equals $$\prod (G_i/H_i)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Apply [Corollary 3](#cor3) to the canonical homomorphisms $$p_i:G_i\rightarrow G_i/H_i$$.

![product_of_normal_subgroups](/assets/images/Math/Algebraic_Structures/Direct_products-2.png){:style="width:16.4em" class="invert" .align-center}

Each $$p_i\circ\pr_i$$ is surjective as a composition of surjective homomorphisms, so by the previous corollary, $$\im p$$ equals $$\prod(G_i/H_i)$$. Also, the kernel of each $$p_i$$ is $$H_i$$. Therefore, by the first isomorphism theorem,

$$\biggl(\prod_{i\in I} G_i\biggr)\bigg/\biggl(\prod_{i\in I}H_i\biggr)\cong\prod_{i\in I} (G_i/H_i)$$

holds.

</details>

Of course, even if $$H_i$$ are subgroups (not necessarily normal) of $$G_i$$, $$\prod H_i$$ is a subgroup of $$\prod G_i$$.

<div class="proposition" markdown="1">

<ins id="cor5">**Corollary 5**</ins> Let a family of groups $$(G_i)_{i\in I}$$ be given. If for each $$i\in I$$, $$H_i\leq G_i$$, then $$\prod H_i$$ is a subgroup of $$\prod G_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Apply [Corollary 3](#cor3) to the inclusion homomorphisms $$\iota_i:H_i\hookrightarrow G_i$$. Then $$\iota$$ is injective and $$\prod H_i$$ is precisely the image of $$\iota$$, so it is a subgroup of $$\prod G_i$$.

</details>

## Partial Products

The above corollaries are particularly useful in the following situation.

Let $$(G_i)_{i\in I}$$ be a family of groups, and consider a subset $$J$$ of $$I$$. Then the product $$\prod_{j\in J}G_j$$ is well-defined. On the other hand, consider the family of groups $$(G_i')$$ defined by

$$G_i'=\begin{cases} G_i&i\in J\\ \{e\}&i\not\in J\end{cases}$$

and the group homomorphisms from $$G_i'$$ to $$G_i$$

$$f_i=\begin{cases} \id_{G_i}&i\in J\\ \iota_i&i\not\in J\end{cases}$$

It is not difficult to show that $$\prod_{i\in I}G_i'\cong\prod_{j\in J}G_j$$, and therefore by [Corollary 4](#cor4),

$$\biggl(\prod_{i\in I}G_i\biggr)\bigg/\biggl(\prod_{j\in J}G_j\biggr)\cong\prod_{i\in I\setminus J} G_i$$

holds.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---
