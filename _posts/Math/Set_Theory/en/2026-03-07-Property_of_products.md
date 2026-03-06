---

title: "Properties of Products"
excerpt: "Partial products, associativity and distributivity"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/property_of_products

header:
    overlay_image: /assets/images/Math/Set_Theory/Property_of_products.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07

weight: 11

---

## Partial Products and Associativity

To discuss whether the product of sets is associative, we must first define partial products.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a family $$(A_i)_{i\in I}$$ and its product $$\prod_{i\in I} A_i$$ be given. For a subset $$J\subseteq I$$ of the index set, $$\prod_{j\in J} A_j$$ is called a *partial product*.

</div>

Let a partial product $$\prod_{j\in J}A_j$$ of $$\prod_{i\in I}A_i$$ be given. Then for any $$F\in\prod_{i\in I}A_i$$,

$$f\circ\id_J=\biggl(F\circ\Delta_J, J, \bigcup_{j\in J} A_j\biggr)$$

is a new function, and for each $$j$$, it satisfies $$(f\circ\id_J)(j)=f(j)\in A_j$$. That is, $$F\circ\Delta_J$$ is an element of $$\prod_{j\in J}A_j$$.

By the above paragraph, $$F\mapsto F\circ\Delta_J$$ defines a function from $$\prod_{i\in I}A_i$$ to $$\prod_{j\in J}A_j$$. This is denoted by $$\pr_J$$, borrowing the notation for projection functions. Then for $$K\subseteq J\subseteq I$$, the composition of the $$J$$-th projection function from $$\prod_{i\in I}A_i$$ to the partial product $$\prod_{j\in J}A_j$$, and the $$K$$-th projection function from $$\prod_{j\in J}A_j$$ to its partial product $$\prod_{k\in K}A_k$$

$$\prod_{i\in I}A_i\longrightarrow \prod_{j\in J}A_j\longrightarrow \prod_{k\in K}A_k$$

is simply the $$K$$-th projection function $$\pr_K$$ from $$\prod_{i\in I}A_i$$ to its partial product $$\prod_{k\in K}A_k$$. This is because $$\Delta_K=\Delta_J\circ\Delta_K$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Consider a family $$(A_i)_{i\in I}$$ in which every component is non-empty, and let $$J\subseteq I$$. If $$g:J\rightarrow\bigcup_{i\in I} A_i$$ satisfies $$g(j)\in A_j$$, then there exists an extension $$f:I\rightarrow\bigcup_{i\in I} A_i$$ of $$g$$ such that $$f(i)\in A_i$$ holds.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$g=(G,J,\bigcup A_i)$$. For each $$i\in I\setminus J$$, since $$A_i$$ is non-empty, we can select one element $$x_i\in A_i$$. Now define

$$F=G\cup\biggl(\bigcup_{i\in I\setminus J}\{(i, x_i)\}\biggr)$$

and let $$f=(F,I,\bigcup A_i)$$. This gives the desired result.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Let a family $$(A_i)_{i\in I}$$ with a non-empty index set $$I$$ (i.e., $$I\neq\emptyset$$) be given. If $$(J_k)_{k\in K}$$ is a partition of $$I$$, then the function $$f\mapsto (\pr_{J_k}(f))_{k\in K}$$ from $$\prod_{i\in I}A_i$$ to $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ is also a bijection.

</div>

<details class="proof" markdown="1">
<summary>Proof 1</summary>

Since $$(J_k)_{k\in K}$$ is a partition, the functions $$f_k:J_k\rightarrow \bigcup_{i\in I} A_i$$ form a family of functions with pairwise disjoint domains, and thus by [§Sum of Sets, ⁋Proposition 2](/en/math/set_theory/sum_of_sets#prop2), we obtain a bijection.

</details>

The proof above is concise, but the following proof using the universal property is also elegant.

<details class="proof--alone" markdown="1">
<summary>Proof 2</summary>

For notational cleanliness, we uniformly denote:

- The $$k$$-th projection function of the product $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ with respect to index set $$K$$

  $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{j\in J_k}A_j$$

  by $$\pr_k$$,
- The $$j$$-th projection function of the product $$\prod_{j\in J_k}A_j$$ with respect to index set $$J_k$$

  $$\prod_{j\in J_k}A_j\rightarrow A_j$$

  also by $$\pr_j$$,
- The $$i$$-th projection function of the product $$\prod_{i\in I}A_i$$ with respect to index set $$I$$

  $$\prod_{i\in I}A_i\rightarrow A_i$$

  also by $$\pr_i$$

While this may cause some confusion when reading the text, in diagrams the source and target are both specified, so there is no ambiguity.

Since $$(J_k)_{k\in K}$$ is a partition of $$I$$, for each $$i\in I$$ there exists a unique $$k\in K$$ such that $$i\in J_k$$. Now define the function $$\pr_{ik}$$ as the composition

$$\pr_{ik}:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\overset{\pr_k}{\longrightarrow}\prod_{j\in J_k}A_j\overset{\pr_i}{\longrightarrow}A_i$$

Then by the universal property of the product $$\prod_{i\in I}A_i$$, we know there exists a $$\phi:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{i\in I}A_i$$ making the following diagram commute:

![partial_product_pf_1](/assets/images/Math/Set_Theory/Property_of_products-1.png){:style="width:18em" class="invert" .align-center}

Similarly, by the universal property of the product $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ with respect to index set $$K$$, we know there exists a $$\psi:\prod_{i\in I}A_i\rightarrow\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$$ making the following diagram commute:

![partial_product_pf_2](/assets/images/Math/Set_Theory/Property_of_products-2.png){:style="width:22em" class="invert" .align-center}

Then $$\phi\circ\psi$$ and $$\psi\circ\phi$$ are each identity functions, and thus they give the desired bijection.

For example, let us show that $$\phi\circ\psi$$ is the identity function from $$\prod_{i\in I}A_i$$ to itself. To do this, it suffices to show that for all $$i\in I$$, the following diagram commutes:

![partial_product_pf_3](/assets/images/Math/Set_Theory/Property_of_products-3.png){:style="width:8em" class="invert" .align-center}

The universal property of the product implies that there exists a *unique* function $$\prod_{i\in I}A_i\rightarrow \prod_{i\in I}A_i$$ making the diagram above commute. Naturally, the identity function from $$\prod_{i\in I}A_i$$ to itself also makes the diagram above commute, so by uniqueness this function must equal $$\phi\circ\psi$$.

Now from

$${\pr_i}\circ(\phi\circ\psi)=({\pr_i}\circ\phi)\circ\psi={\pr_{ik}}\circ\psi={\pr_i}\circ({\pr_k}\circ\psi)={\pr_j}\circ{\pr_{J_k}}=\pr_j$$

we obtain the desired conclusion. (The last equality views $$\pr_j$$ as a projection function to $$\{j\}\subseteq I$$.) This equation may look complicated, but it is merely writing out in formula form that the following diagram commutes:

![partial_product_pf_4](/assets/images/Math/Set_Theory/Property_of_products-4.png){:style="width:16em" class="invert" .align-center}

</details> 

Let $$(A_i)_{i\in I}$$ and $$(B_i)_{i\in I}$$ be families with the same index, and let a family of functions $$(g_i:A_i\rightarrow B_i)_{i\in I}$$ be given. If we define $$u_f:I\rightarrow\bigcup_{i\in I}B_i$$ by $$i\mapsto g_i(f(i))$$, then $$u_f(i)\in B_i$$, so $$u_f\in\prod_{i\in I}B_i$$.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> The function $$f\mapsto u_f$$ defined above is called the *product* of $$(g_i)$$ and is denoted by $$\prod_{i\in I}g_i$$.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$(A_i)_{i\in I}$$, $$(B_i)_{i\in I}$$, and $$(C_i)_{i\in I}$$ be three families, and let $$(f_i)_{i\in I}$$ and $$(g_i)_{i\in I}$$ be families of functions from $$A_i$$ to $$B_i$$ and from $$B_i$$ to $$C_i$$, respectively. Then

$$\prod_{i\in I} (g_i\circ f_i)=\left(\prod_{i\in I} g_i\right)\circ\left(\prod_{i\in I}f_i\right)$$

holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

There is nothing particularly special to explain beyond the following two commutative diagrams:

![composition_of_product_functions](/assets/images/Math/Set_Theory/Property_of_products-5.png){:width="287.1px" class="invert" .align-center}

and

![composition_of_product_fuctions_2](/assets/images/Math/Set_Theory/Property_of_products-6.png){:width="335.4px" class="invert" .align-center}

</details>

Since it is obvious that the product of $$\id_{A_i}$$ is $$\id_{\prod A_i}$$, the above proposition makes it clear that the product of injective functions is an injective function, and the product of surjective functions is a surjective function.


## Distributivity Between Operations

When two or more operations are defined, whether distributivity holds between them becomes an important concern.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$((A_{k,i})_{i\in J_k})_{k\in K}$$ be a family of families of sets. Additionally, suppose $$K\neq\emptyset$$ and $$J_k\neq\emptyset$$ for all $$k\in K$$. Then for $$I=\prod_{k\in K} J_k\neq\emptyset$$,

$$\bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)=\bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right),\quad\bigcap_{k\in K}\left(\bigcup_{i\in J}A_{k,i}\right)=\bigcup_{f\in I}\left(\bigcap_{k\in K}A_{k,f(k)}\right)$$

hold.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, let $$x\in \bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)$$. We need to show that $$x\in \bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right)$$, i.e., that for all $$f\in I$$, we have $$x\in \bigcup_{k\in K}A_{k,f(k)}$$. Since $$x\in \bigcap_{i\in J_k}A_{k,i}$$ for some $$k\in K$$, we have $$x\in A_{k,f(k)}$$. Therefore $$x\in \bigcup_{k\in K}A_{k,f(k)}$$ holds for all $$f$$, and the inclusion relation is established.

To show the inclusion in the opposite direction, we use the contrapositive. Suppose $$x\not\in \bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)$$. Then for all $$k\in K$$, we have $$x\not\in \bigcap_{i\in J_k}A_{k,i}$$. Thus there exists some $$i$$ such that for all $$k$$, $$x\not\in A_{k,i}$$. Now taking $$f\in I$$ such that $$f(k)$$ is such an $$i$$, we have $$x\not\in\bigcup_{k\in K}A_{k,f(k)}$$, so $$x$$ does not belong to the right-hand side. The second equation can be shown similarly.
</details>

Distributivity also holds between product and union, and between product and intersection, as follows, and the proof is almost identical to the above, so it is omitted.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$((A_{k,i})_{i\in J_k})_{k\in K}$$ be a family of families of sets, and define $$I$$ as in the previous proposition. Then

$$\prod_{k\in K}\left(\bigcup_{i\in J_k}A_{k,i}\right)=\bigcup_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right),\quad\prod_{k\in K}\left(\bigcap_{i\in J}A_{k,i}\right)=\bigcap_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right)$$

hold.

</div>

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
