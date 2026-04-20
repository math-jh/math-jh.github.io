---

title: "Order Relations"
excerpt: "Definition and properties of order relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/order_relations
header:
    overlay_image: /assets/images/Math/Set_Theory/Order_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
last_modified_at: 2022-11-27
weight: 14

---

## Order Relations

<div class="definition" markdown="1">
<ins id="def1">**Definition 1**</ins> A binary relation $$R$$ is *anti-symmetric* if

> $$x\mathrel{R}y$$ and $$y\mathrel{R}x$$ implies $$x=y$$

always holds.
</div>

An order relation is then defined as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A binary relation $$(R,A,A)$$ is an *order relation* if $$R$$ is reflexive, transitive, and anti-symmetric.

</div>

In this case, we say that $$A$$ is *ordered by $$R$$*, and often call $$A$$ an *ordered set*. Also, similar to equivalence relations, we write $$x\mathrel{R}y$$ as $$x\leq_{\tiny R}y$$.

<ins id="ex3">**Example 3**</ins> The binary relation <phrase>$x=y$</phrase> is an order relation. The relation <phrase>$x\subseteq y$</phrase> is also an order relation. ([§Ordered Pairs, ⁋Proposition 2](/en/math/set_theory/ordered_pair#prop2) and [§Ordered Pairs, ⁋Proposition 3](/en/math/set_theory/ordered_pair#prop3))
{: .example}

Since an ordered set is a set with an additionally defined relation $$\leq$$, when considering functions between them, we are primarily interested in functions that preserve $$\leq$$. In particular, we define the following.

<ins id="def4">**Definition 4**</ins> If for two order relations $$(R, A, A)$$ and $$(R', A',A')$$ there exists a bijection $$f$$ such that $$x\leq_{\tiny R}y$$ is equivalent to $$f(x)\leq_{\tiny R'}f(y)$$, then $$f$$ is called an *order isomorphism*.
{: .definition}

Hereafter, when we refer to an isomorphism between ordered sets, it will always mean an order isomorphism.

We can do something similar to [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3) for order relations.

<div class="proposition" markdown="1">

<ins id="def5">**Proposition 5**</ins> A binary relation $$(R,A,A)$$ is an order relation if and only if the following two conditions hold:

$$R\circ R=R,\qquad R\cap R^{-1}=\Delta_A$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The equivalence of the first condition with transitivity was already examined in the proof of [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3). The second condition can also easily be shown to combine reflexivity and antisymmetry.

</details>

## Preorder Relations

First, let us examine the following example.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Consider a function $$f:A\rightarrow B$$ and suppose an order relation $$\leq$$ is defined on $$B$$. Then, just as we induced an equivalence relation from a function, we can define a relation $$\preceq$$ on $$A$$ as follows. ([§Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2))

$$x\preceq y\iff f(x)\leq f(y)$$

By definition, $$\preceq$$ is reflexive and transitive. However, in general, unless $$f$$ is injective, $$\preceq$$ does not satisfy antisymmetry.
</div>

Therefore, by removing the antisymmetry condition, we define the following.

<ins id="def7">**Definition 7**</ins> A reflexive and transitive relation $$R$$ is called a *preorder relation*.
{: .definition}

When $$R$$ is a preorder relation, it may be written as $$\preceq_{\tiny R}$$, but since preorders share many properties with order relations in many cases, the same symbol $$\leq_{\tiny R}$$ is sometimes used as for order relations. We will also use $$\leq_{\tiny R}$$ unless otherwise specified.

To understand the properties of preorder relations, we need to examine antisymmetry more closely, which is a property of order relations but not of preorders. If a relation $$R$$ were an order relation, antisymmetry means $$(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\implies x=y$$. We have seen that this does not hold for preorders, but in this case, the following proposition shows that a *generalized equality*, i.e., an equivalence relation, gives the same property.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$R$$ be a preorder relation. Then the relation <phrase>$x\leq_{\tiny R}y$ and $y\leq_{\tiny R}x$</phrase> is an equivalence relation.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>
Let us denote the above relation by $$S$$. We need to show that $$S$$ is reflexive, symmetric, and transitive. First, it is clear that this relation is reflexive. Since $$R$$ is a preorder, $$x\mathrel{R}x$$ always holds for any $$x$$. Meanwhile, for any $$x$$ and $$y$$, let $$x\mathrel{S}y$$. Then

$$x\mathrel{S}y\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\iff(y\leq_{\tiny R}x)\wedge(x\leq_{\tiny R}y)\iff y\mathrel{S}x$$

so $$S$$ is symmetric. Finally, if $$x\mathrel{S}y$$ and $$y\mathrel{S}z$$, then

$$\begin{aligned}  (x\mathrel{S}y)\wedge(y\mathrel{S}z)&\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge((y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y))\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\\
  &\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z))\wedge((z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\\
  &\iff(x\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}x)\\
  &\iff x\mathrel{S}z
\end{aligned}$$

so $$S$$ is transitive, and thus $$S$$ is an equivalence relation.
</details>

## Strict Order

For a given order relation $$\leq$$, let $$<$$ be the relation defined by <phrase>$x\leq y$ and $x\neq y$</phrase>. In this case, since $$<$$ does not satisfy antisymmetry, it cannot be an order relation, and since it is not reflexive, it cannot be a preorder either. Instead, we define the following.

<ins id="def9">**Definition 9**</ins> A relation $$R$$ is *asymmetric* if $$x\mathrel{R}y$$ implies $$y\not \mathrel{R}x$$. An asymmetric, transitive relation is called a *strict order*.
{: .definition}

To denote a strict order, we use $$<_{\tiny S}$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$R$$ be an order relation. Then the new relation <phrase>$x\leq_{\tiny R}y$ and $x\neq y$</phrase> is a strict order.

Conversely, let $$S$$ be a strict order. Then the new relation <phrase>$x<_{\tiny S}y$ or $x=y$</phrase> is an order relation.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, let $$R$$ be an order relation and define a new relation $$S$$ by <phrase>$x\leq_{\tiny R}y$ and $x\neq y$</phrase>. To show asymmetry, we need to prove that $$x\mathrel{S}y$$ and $$y\mathrel{S}x$$ cannot both hold. Expanding $$(x\mathrel{S}y)\wedge(y\mathrel{S}x)$$ gives:
  
$$((x\leq_{\tiny R}y)\wedge(x\neq y))\wedge((y\leq_{\tiny R}x)\wedge(y\neq x))$$

This can be rewritten as:

$$((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge(x\neq y)$$

By antisymmetry of $$R$$, this is $$(x=y)\wedge(x\neq y)$$, which is always false, so $$x\mathrel{S} y$$ implies $$y\not\mathrel{S}x$$.

Conversely, let $$S$$ be a strict order and define a new relation $$R$$ by <phrase>$x<_{\tiny S}y$ or $x=y$</phrase>. First, since $$x=x$$, the latter condition gives $$x\mathrel{R}x$$. To show antisymmetry, assume $$x\mathrel{R}y$$ and $$y\mathrel{R}x$$ hold. Then

$$\begin{aligned}  
(x\mathrel{R}y)\wedge(y\mathrel{R}x)&\iff((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}x)\vee(y=x))\\
   &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}x))\vee(x=y)
\end{aligned}$$

By asymmetry, $$(x<_{\tiny S}y)\wedge(y<_{\tiny S}x)$$ is impossible, so if $$(x\mathrel{R}y)\wedge(y\mathrel{R}x)$$ holds, then $$x=y$$ must hold. Finally, to show transitivity, let $$x\mathrel{R}y$$ and $$y\mathrel{R}z$$. Then

$$\begin{aligned}
  (x\mathrel{R}y)\wedge(y\mathrel{R}z)&\iff ((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}z)\vee(y=z))\\
  &\iff ((x<_{\tiny S}y)\wedge((y<_{\tiny S}z)\vee(y=z)))\vee((x=y)\wedge((y<_{\tiny S}z)\vee(y=z)))\\
  &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}z))\vee((x<_{\tiny S}y)\wedge(y=z))\\
  &\phantom{asdfghjkl}\vee((x=y)\wedge (y<_{\tiny S}z))\vee((x=y)\wedge(y=z))\\
  &\implies (x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x=y=z)\\
  &\iff x\mathrel{R}z
\end{aligned}$$

so $$R$$ is transitive. Therefore $$R$$ is an order relation.
</details>

Hereafter, we will denote the strict order obtained from an order relation $$R$$ by $$<_{\tiny R}$$, and the order relation obtained from a strict order $$S$$ by $$\leq_{\tiny S}$$.

<ins id="rmk1">**Remark**</ins> In general, $$x\not\leq y$$ does not imply $$x>y$$. Let $$S=\left\{a,b\right\}$$ and define the relation $$\leq$$ on $$\mathcal{P}(S)$$ as the inclusion relation between subsets. This is clearly an order relation. In this case, $$\left\{a\right\}\not\leq \left\{b\right\}$$ but $$\left\{a\right\}>\left\{b\right\}$$ also does not hold.
{: .remark}




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.  
**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  

---
