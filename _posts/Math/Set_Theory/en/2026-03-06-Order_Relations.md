---
title: "Definition of Order Relations"
excerpt: "Definitions and properties of order relations"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/order_relations
header:
    overlay_image: /assets/images/Math/Set_Theory/Order_Relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
last_modified_at: 2022-11-27
weight: 14
translated_at: 2026-05-29T16:03:58+00:00
translation_source: kimi-cli
---
## Order Relations

<div class="definition" markdown="1">
<ins id="def1">**Definition 1**</ins> A binary relation $$R$$ is said to be *anti-symmetric* if

> whenever $$x\mathrel{R}y$$ and $$y\mathrel{R}x$$, then $$x=y$$

always holds.
</div>

Then order relations are defined as follows.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> A binary relation $$(R,A,A)$$ is called an *order relation* if $$R$$ is reflexive, transitive, and anti-symmetric.

</div>

In this case, we say that $$A$$ is ordered by $$R$$, and we often call $$A$$ an *ordered set*. Also, as with equivalence relations, we write $$x\mathrel{R}y$$ as $$x\leq_{\tiny R}y$$.

<ins id="ex3">**Example 3**</ins> The binary relation <phrase>$x=y$</phrase> is an order relation. The relation <phrase>$x\subseteq y$</phrase> is also an order relation. ([§Ordered Pairs, ⁋Proposition 2](/en/math/set_theory/ordered_pair#prop2) and [§Ordered Pairs, ⁋Proposition 3](/en/math/set_theory/ordered_pair#prop3))
{: .example}

Since an ordered set is a set with an additional relation $$\leq$$, when we consider functions between them we usually think of functions that also preserve $$\leq$$. In particular, we define the following.

<ins id="def4">**Definition 4**</ins> If for two order relations $$(R, A, A)$$ and $$(R', A',A')$$ there exists a bijection $$f$$ such that $$x\leq_{\tiny R}y$$ is equivalent to $$f(x)\leq_{\tiny R'}f(y)$$, then we call $$f$$ an *order isomorphism*.
{: .definition}

Henceforth, when we say isomorphism between ordered sets, we shall always understand it to mean an order isomorphism.

We can do something similar for order relations as we did in [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3).

<div class="proposition" markdown="1">

<ins id="def5">**Proposition 5**</ins> A binary relation $$(R,A,A)$$ is an order relation if and only if the following two conditions hold.

$$R\circ R=R,\qquad R\cap R^{-1}=\Delta_A$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the first condition is equivalent to transitivity was already shown in the proof of [§Equivalence Relations, ⁋Proposition 3](/en/math/set_theory/equivalence_relations#prop3). That the second condition combines reflexivity and antisymmetry can also be easily seen.

</details>

## Preorder Relations

First let us look at the following example.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> Consider a function $$f:A\rightarrow B$$, and suppose an order relation $$\leq$$ is defined on $$B$$. Then, just as we derive an equivalence relation from a function, we can define a relation $$\preceq$$ on $$A$$ as follows. ([§Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2))

$$x\preceq y\iff f(x)\leq f(y)$$

By definition $$\preceq$$ is reflexive and transitive. However, unless $$f$$ is injective, $$\preceq$$ does not generally satisfy antisymmetry.
</div>

Therefore, we drop the antisymmetry condition and define the following.

<ins id="def7">**Definition 7**</ins> A reflexive and transitive relation $$R$$ is called a *preorder relation*.
{: .definition}

If $$R$$ is a preorder relation we sometimes write it as $$\preceq_{\tiny R}$$, but in many cases preorders share properties similar to order relations, so the same symbol $$\leq_{\tiny R}$$ as for order relations is also used. We too shall use $$\leq_{\tiny R}$$ unless there is a special reason not to.

To understand the properties of preorder relations, we need to examine antisymmetry more closely: it is a property of order relations but not of preorders. If the relation $$R$$ were an order relation, antisymmetry would mean $$(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\implies x=y$$. We have seen that this does not hold for preorders, but in this case a generalized equality, that is, an equivalence relation, provides the same property by the following proposition.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$R$$ be a preorder relation. Then the relation <phrase>$x\leq_{\tiny R}y$ and $y\leq_{\tiny R}x$</phrase> is an equivalence relation.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>
Let the above relation be $$S$$. We must show that $$S$$ is reflexive, symmetric, and transitive. First, it is obvious that this relation is reflexive, because $$R$$ being a preorder means $$x\mathrel{R}x$$ always holds for any $$x$$. On the other hand, let $$x\mathrel{S}y$$ for arbitrary $$x$$, $$y$$. Then

$$x\mathrel{S}y\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\iff(y\leq_{\tiny R}x)\wedge(x\leq_{\tiny R}y)\iff y\mathrel{S}x$$

so $$S$$ is symmetric. Finally, if $$x\mathrel{S}y$$ and $$y\mathrel{S}z$$, then

$$\begin{aligned}  (x\mathrel{S}y)\wedge(y\mathrel{S}z)&\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge((y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y))\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\\
  &\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z))\wedge((z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\\
  &\iff(x\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}x)\\
  &\iff x\mathrel{S}z
\end{aligned}$$

so $$S$$ is transitive, and therefore $$S$$ becomes an equivalence relation.
</details>

## Strict Orders

Given an order relation $$\leq$$, let $$<$$ be the relation defined by <phrase>$x\leq y$ and $x\neq y$</phrase>. Then $$<$$ cannot be an order relation because it does not satisfy antisymmetry, nor can it be a preorder because it is not reflexive. Instead, we define the following.

<ins id="def9">**Definition 9**</ins> A relation $$R$$ is said to be *asymmetric* if $$x\mathrel{R}y$$ implies $$y\not\mathrel{R}x$$. An asymmetric, transitive relation is called a *strict order*.
{: .definition}

To denote a strict order we use $$<_{\tiny S}$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$R$$ be an order relation. Then the new relation <phrase>$x\leq_{\tiny R}y$ and $x\neq y$</phrase> is a strict order.

Conversely, let $$S$$ be a strict order. Then the new relation <phrase>$x<_{\tiny S}y$ or $x=y$</phrase> is an order relation.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, let $$R$$ be an order relation and define a new relation $$S$$ by <phrase>$x\leq_{\tiny R}y$ and $x\neq y$</phrase>. To show asymmetry, we must demonstrate that $$x\mathrel{S}y$$ and $$y\mathrel{S}x$$ cannot hold simultaneously. Expanding $$(x\mathrel{S}y)\wedge(y\mathrel{S}x)$$ gives the following.
  
$$((x\leq_{\tiny R}y)\wedge(x\neq y))\wedge((y\leq_{\tiny R}x)\wedge(y\neq x))$$

But this can be rewritten as

$$((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge(x\neq y)$$

By the antisymmetry of $$R$$ this becomes $$(x=y)\wedge(x\neq y)$$, which is always false; hence if $$x\mathrel{S}y$$ then $$y\not\mathrel{S}x$$.

Conversely, let $$S$$ be a strict order and define a new relation $$R$$ by <phrase>$x<_{\tiny S}y$ or $x=y$</phrase>. First, since $$x=x$$, the latter condition gives $$x\mathrel{R}x$$. To show antisymmetry, assume that $$x\mathrel{R}y$$ and $$y\mathrel{R}x$$ hold. Then

$$\begin{aligned}  
(x\mathrel{R}y)\wedge(y\mathrel{R}x)&\iff((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}x)\vee(y=x))\\
   &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}x))\vee(x=y)
\end{aligned}$$

By asymmetry, $$(x<_{\tiny S}y)\wedge(y<_{\tiny S}x)$$ is impossible, so if $$(x\mathrel{R}y)\wedge(y\mathrel{R}x)$$ holds then necessarily $$x=y$$. Finally, to show transitivity, let $$x\mathrel{R}y$$ and $$y\mathrel{R}z$$. Then

$$\begin{aligned}
  (x\mathrel{R}y)\wedge(y\mathrel{R}z)&\iff ((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}z)\vee(y=z))\\
  &\iff ((x<_{\tiny S}y)\wedge((y<_{\tiny S}z)\vee(y=z)))\vee((x=y)\wedge((y<_{\tiny S}z)\vee(y=z)))\\
  &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}z))\vee((x<_{\tiny S}y)\wedge(y=z))\\
  &\phantom{asdfghjkl}\vee((x=y)\wedge (y<_{\tiny S}z))\vee((x=y)\wedge(y=z))\\
  &\implies (x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x=y=z)\\
  &\iff x\mathrel{R}z
\end{aligned}$$

so $$R$$ is transitive. Therefore $$R$$ becomes an order relation.
</details>

Henceforth, we shall write the strict order obtained from an order relation $$R$$ as $$<_{\tiny R}$$, and the order relation obtained from a strict order $$S$$ as $$\leq_{\tiny S}$$.

<ins id="rmk1">**Remark**</ins> In general, $$x\not\leq y$$ does not imply $$x>y$$. Let $$S=\left\{a,b\right\}$$, and define the relation $$\leq$$ on $$\mathcal{P}(S)$$ to be the inclusion relation between subsets. Then this is obviously an order relation. Here, $$\left\{a\right\}\not\leq\left\{b\right\}$$, but $$\left\{a\right\}>\left\{b\right\}$$ does not hold either.
{: .remark}




---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.  
**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  

---
