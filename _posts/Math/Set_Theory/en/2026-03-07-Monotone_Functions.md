---
title: "Monotone Functions"
description: "Defines the restriction and product of well-orderings on subsets, and discusses how this structure extends to order relations."
excerpt: "Operations on ordered sets and monotone functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/monotone_functions
sidebar: 
    nav: "set_theory-en"

date: 2021-08-22
last_modified_at: 2022-11-27
weight: 15
translated_at: 2026-06-02T21:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T21:30:02+00:00
---
## Restriction of a Preorder Relation

Consider a preorder relation $$(R,A,A)$$ and let $$A'\subseteq A$$ be any subset. Then the relation defined by $$R\cap (A'\times A')$$ is a preorder relation on $$A'$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> The set $$R\cap (A'\times A')$$ defined above is a preorder relation on $$A'$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for any $$x\in A'$$, since $$x$$ is also an element of $$A$$, we have $$(x,x)\in R$$. Moreover, since $$(x,x)\in A'\times A'$$, it follows that $$(x,x)\in R\cap(A'\times A')$$.

Now suppose $$(x,y),(y,z)\in R\cap (A'\times A')$$. Then $$x,y,z\in A'$$ and $$(x,y),(y,z)\in R$$. Since $$R$$ is transitive, $$(x,z)\in R$$, and because $$x,z\in A'$$, we conclude $$(x,z)\in R\cap(A'\times A')$$.

</details>

Intuitively, this relation coincides with the restriction of $$\leq_R$$ to $$A'$$. By a slight abuse of notation, we also write this relation as $$\leq_R$$.

## Product of Preorder Relations

For any index set $$I$$, let preorder relations $$(R_i,A_i,A_i)$$ be given. Then for any two elements $$x=(x_i)_{i\in I}$$ and $$y=(y_i)_{i\in I}$$ of the product set $$\prod_{i\in I} A_i$$, we may consider the relation

$$x\leq y\iff \forall i((i\in I)\implies(x_i\leq_{\tiny R_i} y_i))$$

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The relation $$\leq$$ defined above is a preorder relation on $$\prod A_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$(x_i)\in \prod A_i$$, since $$x_i\leq_{\tiny R_i} x_i$$ holds for all $$i\in I$$, we have $$(x_i)\leq (x_i)$$.

Now suppose $$(x_i)\leq (y_i)$$ and $$(y_i)\leq (z_i)$$. Then for all $$i\in I$$,

$$x_i\leq y_i\leq z_i\implies x_i\leq z_i$$

holds, and therefore $$(x_i)\leq (z_i)$$.

</details>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins>  Any function $$f$$ from a set $$A$$ to a set $$B$$ can be viewed as an element of the set $$B^A=\prod_{a\in A}B$$, which is the product of copies of $$B$$ indexed by $$A$$.

Now suppose a preorder relation $$R$$ is defined on $$B$$. By [Proposition 2](#prop2), the product of preorder relations defines a preorder relation on the set of functions $$B^A$$. Writing this as $$\leq$$, the condition $$f\leq g$$ means that $$f(x)\leq_{\tiny R} g(x)$$ for all $$x\in A$$.

</div>

The contents of the preceding two sections remain valid if all preorder relations are replaced by order relations. That is, if the originally given preorder relations are antisymmetric and hence become order relations, then the preorder relations obtained in [Proposition 1](#prop1) and [Proposition 2](#prop2) also satisfy antisymmetry and hence become order relations.

In this case, some care is needed when examining strict orders. For instance, suppose an order relation $$R$$ is given on a set $$B$$, and let $$S$$ be the strict order defined by $$R$$. The strict order $$<$$ arising from the order relation $$\leq$$ constructed in [Example 3](#ex3) is *different* from the relation defined by

$$f< g\iff\forall x\bigl((x\in A)\implies (f(x)<_{\tiny R}g(x))\bigr)$$

Indeed, $$f<g$$ may hold even if $$f(y)<_{\tiny R} g(y)$$ for only *a single* $$y\in A$$, while $$f(x)\leq_{\tiny R} g(x)$$ for all remaining $$x\in A$$.

## Monotone Functions

<ins id="def4">**Definition 4**</ins> Let $$A$$ and $$A'$$ be sets equipped with preorders $$R$$ and $$R'$$, respectively. A function $$f:A\rightarrow A'$$ is an *increasing function* if $$x\leq_{\tiny R} y\implies f(x)\leq_{\tiny R'} f(y)$$ always holds. If $$x\leq_{\tiny R}y\implies f(y)\leq_{\tiny R'} f(x)$$ always holds, then this function is called a *decreasing function*. Increasing and decreasing functions are collectively called *monotone functions*.
{: .definition}

<ins id="rmk1">**Remark**</ins> Any constant function is both increasing and decreasing. However, the converse is not true. Let $$A$$ be a set with more than one element, and consider the order relation $$=$$ on it. Then the identity function from $$A$$ to $$A$$ is both increasing and decreasing, but it is not constant.
{: .remark}

Replacing $$\leq$$ with $$<$$ yields the following definition.

<ins id="def5">**Definition 5**</ins> Let $$A$$ and $$A'$$ be sets equipped with strict orders $$S$$ and $$S'$$, respectively. A function $$f:A\rightarrow A'$$ is a *strictly increasing function* if $$x <_{\tiny S} y\implies f(x) <_{\tiny S'} f(y)$$ always holds, and a *strictly decreasing function* if $$x <_{\tiny S} y\implies f(y)<_{\tiny S'}f(x)$$ always holds. Strictly increasing and strictly decreasing functions are collectively called *strictly monotone functions*.
{: .definition}

<div class="remark" markdown="1">

<ins id="rmk2">**Remark**</ins> By definition, an injective monotone function is always strictly monotone. However, the converse does not always hold. For example, define a strict order $$\prec$$ on $$\mathbb{N}$$ by

$$m\prec n\iff ((m-n\text{ is even}) \wedge (m<n))$$

and denote this ordered set by $$A$$. That is, in $$A$$, even numbers can be compared with even numbers and odd numbers with odd numbers, but no comparison is possible between even and odd numbers. Also, let $$B$$ be the ordered set obtained by endowing the set of natural numbers $$\mathbb{N}$$ with the usual strict order $$<$$. Then the function $$m\mapsto \lfloor m/2\rfloor$$ from $$A$$ to $$B$$ is strictly increasing but not injective.
</div>

<ins id="prop6">**Proposition 6**</ins> Let $$A$$ and $$A'$$ be ordered sets, and let $$u:A\rightarrow A'$$ and $$v:A'\rightarrow A$$ be decreasing functions such that $$v(u(x))\geq x$$ and $$u(v(x'))\geq x'$$ hold for all $$x\in A$$ and $$x'\in A'$$. Then $$u\circ v\circ u=u$$ and $$v\circ u\circ v=v$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

This follows immediately from the given assumptions and the fact that $$u$$ is decreasing. Specifically, since $$u$$ is decreasing, from $$v(u(x))\geq x$$ we obtain $$u(v(u(x)))\leq u(x)$$ for all $$x$$, while the second part of the assumption yields $$u(v(u(x)))\geq u(x)$$.

</details>

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
