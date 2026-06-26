---
title: "Blowup Algebras"
description: "We construct the associated graded ring and associated graded module from ideals of a ring, and analyze the structure of finitely generated modules using the notions of filtrations and stable filtrations."
excerpt: "Rees algebra and associated graded ring from an ideal"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/blowup_algebra
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-20
weight: 11
translated_at: 2026-06-26T14:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T14:30:02+00:00
---
In this post, we fix an ideal $\mathfrak{a}$ of a ring $A$ and define two graded $A$-algebras arising from it.

## Associated graded module

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> The *associated graded ring* of $A$ with respect to $\mathfrak{a}$ is defined as

$$\gr_\mathfrak{a}A= A/\mathfrak{a}\oplus \mathfrak{a}/\mathfrak{a}^2\oplus\cdots$$

</div>

In the above definition, the multiplication in $\gr_\mathfrak{a}A$ is defined as follows: given arbitrary $a\in \mathfrak{a}^k/\mathfrak{a}^{k+1}$ and $b\in \mathfrak{a}^l/\mathfrak{a}^{l+1}$, their product $ab$ is obtained by first computing the product $\tilde{a}\tilde{b}$ of representatives $\tilde{a}\in \mathfrak{a}^k$ and $\tilde{b}\in \mathfrak{a}^l$, then restricting the result to $\mathfrak{a}^{k+l}/\mathfrak{a}^{k+l+1}$.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> The multiplication on $\gr_\mathfrak{a}A$ defined above is well-defined.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose we choose different representatives $\tilde{a}',\tilde{b}'$, and write $\tilde{a}'=\tilde{a}+x$ and $\tilde{b}'=\tilde{b}+y$ for suitable $x\in \mathfrak{a}^{k+1}$ and $y\in \mathfrak{a}^{l+1}$. Then

$$\tilde{a}'\tilde{b}'=\tilde{a}\tilde{b}+y\tilde{a}+x\tilde{b}+xy$$

and since $x\tilde{b},y\tilde{a}\in \mathfrak{a}^{k+l+1}$ and $xy\in \mathfrak{a}^{k+l+2}\subseteq \mathfrak{a}^{k+l+1}$, the proof is complete.

</details>

To generalize this to $A$-modules, we introduce the following.

<div class="definition" markdown="1">

<ins id="def3">**Definition 3**</ins> For a ring $A$, an arbitrary ideal $\mathfrak{a}$ of $A$, and an $A$-module $M$, a filtration

$$M=M_0\supseteq M_1\supseteq\cdots$$

is called an *$\mathfrak{a}$-filtration* if $\mathfrak{a}M_k\subseteq M_{k+1}$ holds for all $k$. Furthermore, if there exists some $n$ such that $\mathfrak{a}M_k=M_{k+1}$ for all $k>n$, then this filtration is called *$\mathfrak{a}$-stable*.

Now, for any $\mathfrak{a}$-filtration

$$\mathcal{J}:\quad M=M_0\supseteq M_1\supseteq\cdots$$

we define the *associated graded module* of $M$ with respect to $\mathcal{J}$ as

$$\gr_\mathcal{J}M=M/M_1\oplus M_1/M_2\oplus\cdots$$

</div>

In the above definition, $\gr_\mathcal{J}M$ carries a $\gr_\mathfrak{a}A$-module structure: for arbitrary $a\in \mathfrak{a}^k/\mathfrak{a}^{k+1}$ and $x\in M_l/M_{l+1}$, we choose representatives $\tilde{a}\in \mathfrak{a}^k$ and $\tilde{x}\in M_l$, then restrict $\tilde{a}\tilde{x}$ to $M_{k+l}/M_{k+l+1}$; a calculation similar to [Lemma 2](#lem2) shows that this is well-defined. In the special case where $M=A$ and the $M_i$ are ideals of $A$, $\gr_\mathcal{J}A$ also has a ring structure, just as in [Definition 1](#def1), and this too is called the associated graded ring with respect to the filtration $\mathcal{J}$.

We now have the following.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> Let $\mathcal{J}$ be an $\mathfrak{a}$-stable filtration of a finitely generated module $M$, and suppose every term $M_k$ of $\mathcal{J}$ is a finitely generated submodule of $M$. Then $\gr_\mathcal{J}M$ is a finitely generated $\gr_\mathfrak{a}A$-module.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $\mathcal{J}$ is an $\mathfrak{a}$-stable filtration, there exists a suitable $n$ such that $\mathfrak{a}M_k=M_{k+1}$ holds for all $k>n$. Therefore, for such $k$, we have $(\mathfrak{a}/\mathfrak{a}^2)(M_k/M_{k+1})=M_{k+1}/M_{k+2}$. Hence, collecting only the generators of the components

$$M_0/M_1, M_1/M_2,\ldots, M_{n+1}/M_{n+2}$$

of $\gr_\mathcal{J}M$ suffices to generate all of $\gr_\mathcal{J}M$. The desired claim now follows from the assumption that each $M_i$ is finitely generated.

</details>

## Blowup algebra

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> For a ring $A$ and an ideal $\mathfrak{a}$, the *blowup algebra* of $\mathfrak{a}$ in $A$ is the following graded $A$-algebra:

$$\Bl_\mathfrak{a}A=A\oplus \mathfrak{a}\oplus \mathfrak{a}^2\oplus\cdots\cong A[t \mathfrak{a}]\subseteq A[t]$$

</div>

Then $\Bl_\mathfrak{a}A/\mathfrak{a}\Bl_\mathfrak{a}A=\gr_\mathfrak{a}A$ is obvious. More generally, for any $A$-module $M$ and $\mathfrak{a}$-filtration $\mathcal{J}: M_0\supseteq M_1\supseteq\cdots$, one can also easily verify that $\Bl_\mathcal{J}M =M\oplus M_1\oplus\cdots$ defined by the formula above becomes a graded $\Bl_\mathfrak{a}A$-module. We now have the following.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> An $\mathfrak{a}$-filtration $\mathcal{J}$ of $M$ is $\mathfrak{a}$-stable if and only if $\Bl_\mathcal{J}M$ is finitely generated as a $\Bl_\mathfrak{a}A$-module.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, if $\Bl_\mathcal{J}M$ is finitely generated, then there exists a suitable $n$ such that these generators can be arranged to lie in the first $n$ terms of $\Bl_\mathcal{J}M$. If we replace them by the sums of their homogeneous components, then $\Bl_\mathcal{J}M$ is generated by these homogeneous elements. From this we see that $\mathcal{J}$ is $\mathfrak{a}$-stable. This argument works in the reverse direction as well.

</details>

## Artin–Rees lemma

We now prove the following useful Artin–Rees lemma.

<div class="proposition" markdown="1">

<ins id="lem7">**Lemma 7 (Artin–Rees)**</ins> Fix a Noetherian ring $A$ and an ideal $\mathfrak{a}\subseteq A$, and let $M$ be a finitely generated $A$-module with a submodule $M'$. If

$$\mathcal{J}:\quad M=M_0\supseteq M_1\supseteq\cdots$$

is an $\mathfrak{a}$-stable filtration, then the induced filtration

$$\mathcal{J}':\quad M'\supseteq M'\cap M_1\supseteq M'\cap M_2\supseteq\cdots$$

is also $\mathfrak{a}$-stable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $\mathcal{J}$ is $\mathfrak{a}$-stable, $\Bl_\mathcal{J}M$ is finitely generated as a $\Bl_\mathfrak{a}A$-module. On the other hand, $\Bl_\mathfrak{a}A$ is a finitely generated $A$-algebra and $A$ is Noetherian, so by [§Basic Notions, ⁋Corollary 13](/en/math/commutative_algebra/basic_notions#cor13), $\Bl_\mathfrak{a}A$ is also Noetherian. Therefore, the submodule $\Bl_{\mathcal{J}'}M'$ of $\Bl_\mathcal{J}M$ is also finitely generated, and applying [Proposition 6](#prop6) again yields the desired result.

</details>

<div class="proposition" markdown="1">

<ins id="cor8">**Corollary 8 (Krull intersection theorem)**</ins> Fix a Noetherian ring $A$, an ideal $\mathfrak{a}$, and a finitely generated $A$-module $M$. Then the following hold.

1. There exists $a\in \mathfrak{a}$ such that $(1-a)\left(\bigcap_1^\infty \mathfrak{a}^i M\right)=0$.
2. If $A$ is a domain or a local ring and $\mathfrak{a}$ is a proper ideal, then $\bigcap \mathfrak{a}^i=0$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider the $\mathfrak{a}$-stable filtration of $M$

$$M\supseteq \mathfrak{a}M \supseteq \mathfrak{a}^2 M\supseteq\cdots$$

Then by [Lemma 7](#lem7), the filtration

$$\left(\bigcap \mathfrak{a}^iM\right) \cap M\supseteq \left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}M \supseteq \left(\bigcap \mathfrak{a}^iM\right) \cap \mathfrak{a}^2 M\supseteq\cdots$$

is also $\mathfrak{a}$-stable. That is, there exists a suitable $n$ such that

$$\mathfrak{a}\left(\left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}^p M\right)=\left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}^{n+1} M$$

Simplifying the left-hand and right-hand sides of the above equation, we obtain

$$\mathfrak{a}\left(\bigcap \mathfrak{a}^iM\right)=\left(\bigcap \mathfrak{a}^iM\right)$$

and applying [§Integral Extensions, ⁋Lemma 7](/en/math/commutative_algebra/integral_extension#lem7) gives the first result.

To show the second result, set $M=A$. For the element $a$ obtained from the first result, it suffices to show that $1-a$ is not a zerodivisor. Since $\mathfrak{a}$ is a proper ideal of $A$, we have $1-a\neq 0$, and there is nothing more to prove when $A$ is a domain. If $A$ is a local ring, then $\mathfrak{a}$ must belong to the (unique) maximal ideal $\mathfrak{m}$ of $A$, so $a\in \mathfrak{m}$, and hence $1-a$ must be a unit.

</details>

Finally, we define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Let an $\mathfrak{a}$-filtration

$$\mathcal{J}:\qquad M=M_0\supseteq M_1\supseteq\cdots$$

be given on an $A$-module $M$, with associated graded module $\gr_\mathcal{J}M$. Then for any $x\in M$, the *initial form* $\initial(x)$ of $x$ is defined by the formula

$$\initial(x)=x+M_{k+1}\quad\text{in $M_k/M_{k+1}$,}\qquad\text{where $k$ is the greatest integer satisfying $x\in M_k$}$$

</div>

In the situation above, suppose an arbitrary $A$-submodule $M'\subseteq M$ is given. Regarding $\gr_\mathcal{J}M$ as a $\gr_\mathfrak{a}A$-module, we can define $\initial(M')$ as the $\gr_\mathfrak{a}A$-submodule of $\gr_\mathcal{J}M$ generated by the $\initial(x)$ for $x\in M'$.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> Let $A=\mathbb{K}[\x,\y]$ and $\mathfrak{a}=(\x,\y)$. Then $\gr_\mathfrak{a}A$ is the graded ring with grading determined by the degree of polynomials. Now set $M=A$, and consider the $A$-submodule (that is, the ideal of $A$) $\mathfrak{b}=(\x^2, \y^2)$. Then any element of $\mathfrak{b}$ has the form

$$f(\x,\y)\x^2+g(\x,\y)\y^2$$

so $\initial(\mathfrak{b})$ is the homogeneous ideal of $\gr_\mathcal{a}A$ generated by $\x^2$ and $\y^2$.

</div>

However, in general $\initial(M')$ is not generated by the initial forms of generators of $M'$.

<div class="proposition" markdown="1">

<ins id="cor11">**Corollary 11**</ins> For a Noetherian local ring $A$ and a proper ideal $\mathfrak{a}$ of $A$, if $\gr_\mathfrak{a}A$ is a domain then so is $A$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Assume $ab=0$ in $A$; it suffices to show that $a=0$ or $b=0$. In $\gr_\mathfrak{a}A$ we must have $\initial(a)\initial(b)=0$, so either $\initial(a)$ or $\initial(b)$ must be $0$. By the corollary above, $\bigcap \mathfrak{a}^n=0$, and hence $a=0$ or $b=0$.

</details>

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
