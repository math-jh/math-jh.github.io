---

title: "Monotone Functions"
excerpt: "Operations on ordered sets and monotone functions"

categories: [Math / Set Theory]
permalink: /en/math/set_theory/monotone_functions
header:
    overlay_image: /assets/images/Math/Set_Theory/Monotone_functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-en"

date: 2026-03-07
last_modified_at: 2026-03-07
weight: 15

---

## Restriction of a Preorder Relation

Consider a preorder relation $$(R,A,A)$$ and let any subset $$A'\subseteq A$$ be given. Then the relation defined by $$R\cap (A'\times A')$$ defines a preorder relation on $$A'$$.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> The set $$R\cap (A'\times A')$$ defined above is a preorder relation on $$A'$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$x\in A'$$, since $$x$$ is also an element of $$A$$, we have $$(x,x)\in R$$. Also, since $$(x,x)\in A'\times A'$$, we have $$(x,x)\in R\cap(A'\times A')$$.

Now suppose $$(x,y),(y,z)\in R\cap (A'\times A')$$. Then $$x,y,z\in A'$$ and $$(x,y),(y,z)\in R$$. Since $$R$$ is transitive, $$(x,z)\in R$$, and from $$x,z\in A'$$, we conclude $$(x,z)\in R\cap(A'\times A')$$.

</details>

Intuitively, this relation is the same as restricting $$\leq_R$$ to $$A'$$. With some abuse of notation, we write this relation also as $$\leq_R$$.

## Product of Preorder Relations

For any index set $$I$$, let preorder relations $$(R_i,A_i,A_i)$$ be given. Then for any two elements $$x=(x_i)_{i\in I}$$ and $$y=(y_i)_{i\in I}$$ of the product set $$\prod_{i\in I} A_i$$, we can consider the relation

$$x\leq y\iff \forall i((i\in I)\implies(x_i\leq_{\tiny R_i} y_i))$$

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> The relation $$\leq$$ defined above is a preorder relation on $$\prod A_i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For any $$(x_i)\in \prod A_i$$, since $$x_i\leq_{\tiny R_i} x_i$$ holds for all $$i\in I$$, we have $$(x_i)\leq (x_i)$$.

Now suppose $$(x_i)\leq (y_i)$$ and $$(y_i)\leq (z_i)$$. Then for all $$i\in I$$,

$$x_i\leq y_i\leq z_i\implies x_i\leq z_i$$

holds, so $$(x_i)\leq (z_i)$$.

</details>

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins>  Any function $$f$$ from a set $$A$$ to a set $$B$$ can be viewed as an element of the set $$B^A=\prod_{a\in A}B$$, which is the product of $$B$$ indexed by $$A$$.

Now suppose a preorder relation $$R$$ is defined on the set $$B$$. By [Proposition 2](#prop2), the product of preorder relations defines a preorder relation on the set of functions $$B^A$$. Denoting this by $$\leq$$, $$f\leq g$$ means that $$f(x)\leq_{\tiny R} g(x)$$ for all $$x\in A$$.

</div>

The content of the previous two sections also holds when all preorder relations are replaced by order relations. That is, if the originally given preorder relations have antisymmetry and thus become order relations, then the preorder relations obtained in [Proposition 1](#prop1) and [Proposition 2](#prop2) also satisfy antisymmetry and thus become order relations.

In this case, some care is needed when considering strict orders. For example, let an order relation $$R$$ be given on a set $$B$$, and let $$S$$ be the strict order defined by $$R$$. The strict order $$<$$ created from the order relation $$\leq$$ obtained through [Example 3](#ex3) is *different* from the relation defined by

$$f< g\iff\forall x\bigl((x\in A)\implies (f(x)<_{\tiny R}g(x))\bigr)$$

$$f<g$$ holds even if $$f(y)<_{\tiny R} g(y)$$ for only *one* $$y\in A$$, and $$f(x)\leq_{\tiny R} g(x)$$ for all other $$x\in A$$.

## Monotone Functions

<ins id="def4">**Definition 4**</ins> Let $$A$$ and $$A'$$ be sets with preorders $$R$$ and $$R'$$, respectively. A function $$f:A\rightarrow A'$$ is an *increasing function* if $$x\leq_{\tiny R} y\implies f(x)\leq_{\tiny R'} f(y)$$ always holds. If $$x\leq_{\tiny R}y\implies f(y)\leq_{\tiny R'} f(x)$$ always holds, then this function is called a *decreasing function*. Increasing functions and decreasing functions are collectively called *monotone functions*.
{: .definition}

<ins id="rmk1">**Remark**</ins> Any constant function is both an increasing function and a decreasing function. However, the converse is not true. Let $$A$$ be a set with more than one element, and consider the order relation $$=$$ defined on it. Then the identity function from $$A$$ to $$A$$ is both an increasing function and a decreasing function, but it is not a constant function.
{: .remark}

Replacing $$\leq$$ with $$<$$, we obtain the following definition.

<ins id="def5">**Definition 5**</ins> Let $$A$$ and $$A'$$ be sets with strict orders $$S$$ and $$S'$$, respectively. A function $$f:A\rightarrow A'$$ is a *strictly increasing function* if $$x <_{\tiny S} y\implies f(x) <_{\tiny S'} f(y)$$ is always true, and a *strictly decreasing function* if $$x <_{\tiny S} y\implies f(y)<_{\tiny S'}f(x)$$ always holds. Strictly increasing functions and strictly decreasing functions are collectively called *strictly monotone functions*.
{: .definition}

<div class="remark" markdown="1">

<ins id="rmk2">**Remark**</ins> By definition, an injective monotone function is always strictly monotone. However, the converse does not always hold. For example, define a strict order $$\prec$$ on $$\mathbb{N}$$ by

$$m\prec n\iff ((m-n\text{ is even}) \wedge (m<n))$$

and call this set $$A$$. That is, in $$A$$, even numbers can be compared with even numbers, and odd numbers with odd numbers, but even and odd numbers cannot be compared. Also, let $$B$$ be the ordered set obtained by giving the usual strict order $$<$$ to the set of natural numbers $$\mathbb{N}$$. Then the function $$m\mapsto \lfloor m/2\rfloor$$ from $$A$$ to $$B$$ is strictly increasing but not injective.
</div>

<ins id="prop6">**Proposition 6**</ins> Let $$A$$ and $$A'$$ be ordered sets, and let $$u:A\rightarrow A'$$ and $$v:A'\rightarrow A$$ be decreasing functions such that $$v(u(x))\geq x$$ and $$u(v(x'))\geq x'$$ hold for all $$x\in A$$ and $$x'\in A'$$. Then $$u\circ v\circ u=u$$ and $$v\circ u\circ v=v$$.
{: .proposition}

<details class="proof" markdown="1">
<summary>Proof</summary>

This follows from the given assumptions and the fact that $$u$$ is a decreasing function. That is, since $$u$$ is a decreasing function, from $$v(u(x))\geq x$$ we have $$u(v(u(x)))\leq u(x)$$ for all $$x$$, but the second part of the assumption gives $$u(v(u(x)))\geq u(x)$$.

</details>

---
**References**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
