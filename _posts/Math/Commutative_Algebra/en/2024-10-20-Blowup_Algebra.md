---
title: "Blowup Algebras"
description: "We construct the associated graded ring and associated graded module from the ideals of a ring, and analyze the structure of finitely generated modules through the notions of filtrations and stable filtrations."
excerpt: "Blowup algebras and associated graded rings from an ideal"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/blowup_algebra
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-20
weight: 11
translated_at: 2026-08-27T20:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-27T20:15:05+00:00
---
In this post, we fix an ideal $\mathfrak{a}$ of a ring $A$ and define two graded $A$-algebras built from it.

## Associated graded module

::: Definition 1
The *associated graded ring* of a ring $A$ with respect to $\mathfrak{a}$ is defined by

$$\gr_\mathfrak{a}A= A/\mathfrak{a}\oplus \mathfrak{a}/\mathfrak{a}^2\oplus\cdots$$

.
:::

In the above definition, the multiplication on $\gr_\mathfrak{a}A$ is given as follows: given arbitrary $a\in \mathfrak{a}^k/\mathfrak{a}^{k+1}$ and $b\in \mathfrak{a}^l/\mathfrak{a}^{l+1}$, their product $ab$ is obtained by first computing the product $\tilde{a}\tilde{b}$ of representatives $\tilde{a}\in \mathfrak{a}^k, \tilde{b}\in \mathfrak{a}^l$ of $a$ and $b$, and then restricting it to $\mathfrak{a}^{k+l}/\mathfrak{a}^{k+l+1}$.

::: Lemma 2
The multiplication on $\gr_\mathfrak{a}A$ defined above is well defined.
:::
::: Proof
Suppose we chose different representatives $\tilde{a}',\tilde{b}'$, and write $\tilde{a}'=\tilde{a}+x,\tilde{b}'=\tilde{b}+y$ for some $x\in \mathfrak{a}^{k+1}$ and $y\in \mathfrak{a}^{l+1}$. Then

$$\tilde{a}'\tilde{b}'=\tilde{a}\tilde{b}+y\tilde{a}+x\tilde{b}+xy$$

and since $x\tilde{b},y\tilde{a}\in \mathfrak{a}^{k+l+1}$ and $xy\in \mathfrak{a}^{k+l+2}\subseteq \mathfrak{a}^{k+l+1}$, the proof is complete.
:::

To generalize this to $A$-modules, we define the following.

::: Definition 3
For a ring $A$, an arbitrary ideal $\mathfrak{a}$ of $A$, and an $A$-module $M$, a filtration

$$M=M_0\supseteq M_1\supseteq\cdots$$

is called an *$\mathfrak{a}$-filtration* if $\mathfrak{a}M_k\subseteq M_{k+1}$ holds for every $k$. Furthermore, if there exists some $n$ such that $\mathfrak{a}M_k=M_{k+1}$ holds whenever $k>n$, the filtration is said to be *$\mathfrak{a}$-stable*.

Now, for an arbitrary $\mathfrak{a}$-filtration

$$\mathcal{J}:\quad M=M_0\supseteq M_1\supseteq\cdots$$

the *associated graded module* of $M$ with respect to $\mathcal{J}$ is defined by

$$\gr_\mathcal{J}M=M/M_1\oplus M_1/M_2\oplus\cdots$$

.
:::

In the above definition, $\gr_\mathcal{J}M$ carries a $\gr_\mathfrak{a}A$-module structure: for arbitrary $a\in \mathfrak{a}^k/\mathfrak{a}^{k+1}$ and $x\in M_l/M_{l+1}$, one takes representatives $\tilde{a}\in \mathfrak{a}^k$, $\tilde{x}\in M_l$ and restricts $\tilde{a}\tilde{x}$ to $M_{k+l}/M_{k+l+1}$, and a computation similar to that of [Lemma 2](#lem2) shows that this is well defined. In particular, when $M=A$ and the $M_i$ are ideals of $A$ satisfying $M_iM_j\subseteq M_{i+j}$ for all $i,j$, then just as in [Definition 1](#def1), $\gr_\mathcal{J}A$ also carries a ring structure, and this is likewise called the associated graded ring with respect to the filtration $\mathcal{J}$.

The following now holds.

::: Proposition 4
Let $M$ be a finitely generated module equipped with an $\mathfrak{a}$-stable filtration $\mathcal{J}$, and suppose that every term $M_k$ of $\mathcal{J}$ is a finitely generated submodule of $M$. Then $\gr_\mathcal{J}M$ is a finitely generated $\gr_\mathfrak{a}A$-module.
:::
::: Proof
Since $\mathcal{J}$ is an $\mathfrak{a}$-stable filtration, there exists some $n$ such that $\mathfrak{a}M_k=M_{k+1}$ holds for all $k>n$. Hence, for such $k$, we have $(\mathfrak{a}/\mathfrak{a}^2)(M_k/M_{k+1})=M_{k+1}/M_{k+2}$. Therefore, if we collect generators of the components

$$M_0/M_1, M_1/M_2,\ldots, M_{n+1}/M_{n+2}$$

of $\gr_\mathcal{J}M$, these generate all of $\gr_\mathcal{J}M$. The desired claim now follows from the assumption that each $M_i$ is finitely generated.
:::

## Blowup algebras

::: Definition 5
For a ring $A$ and an ideal $\mathfrak{a}$, the *blowup algebra* of $\mathfrak{a}$ over $A$ is the graded $A$-algebra

$$\Bl_\mathfrak{a}A=A\oplus \mathfrak{a}\oplus \mathfrak{a}^2\oplus\cdots\cong A[t \mathfrak{a}]\subseteq A[t]$$

.
:::

Then $\mathfrak{a}\Bl_\mathfrak{a}A=\bigoplus_{n\geq 0}\mathfrak{a}^{n+1}$, so $\Bl_\mathfrak{a}A/\mathfrak{a}\Bl_\mathfrak{a}A=\gr_\mathfrak{a}A$. More generally, for an arbitrary $A$-module $M$ and an $\mathfrak{a}$-filtration $\mathcal{J}: M_0\supseteq M_1\supseteq\cdots$, the $\Bl_\mathcal{J}M$ defined by

$$\Bl_\mathcal{J}M =M\oplus M_1\oplus\cdots$$

becomes a graded $\Bl_\mathfrak{a}A$-module thanks to $\mathfrak{a}^kM_l\subseteq M_{k+l}$. The following now holds.

::: Proposition 6
For a Noetherian ring $A$ and a finitely generated $A$-module $M$, an $\mathfrak{a}$-filtration $\mathcal{J}$ of $M$ is $\mathfrak{a}$-stable if and only if $\Bl_\mathcal{J}M$ is finitely generated as a $\Bl_\mathfrak{a}A$-module.
:::
::: Proof
First, if $\Bl_\mathcal{J}M$ is finitely generated, there exists some $n$ such that these generators are contained in the first $n$ terms of $\Bl_\mathcal{J}M$. Rewriting each of them as a sum of homogeneous elements, we see that $\Bl_\mathcal{J}M$ is generated by these homogeneous elements. From this we conclude that $\mathcal{J}$ is $\mathfrak{a}$-stable. The same argument also works in the opposite direction.
:::

## The Artin–Rees lemma

We now prove the following useful Artin–Rees lemma.

::: Lemma 7 (Artin-Rees)
Fix a Noetherian ring $A$ and an ideal $\mathfrak{a}\subseteq A$, and fix a finitely generated $A$-module $M$ and a submodule $M'$ of $M$. If

$$\mathcal{J}:\quad M=M_0\supseteq M_1\supseteq\cdots$$

is an $\mathfrak{a}$-stable filtration, then the induced filtration

$$\mathcal{J}':\quad M'\supseteq M'\cap M_1\supseteq M'\cap M_2\supseteq\cdots$$

is also $\mathfrak{a}$-stable.
:::
::: Proof
Since $\mathcal{J}$ is $\mathfrak{a}$-stable, $\Bl_\mathcal{J}M$ is finitely generated as a $\Bl_\mathfrak{a}A$-module. On the other hand, $\Bl_\mathfrak{a}A$ is a finitely generated $A$-algebra, and since $A$ is Noetherian, [§Basic Notions, ⁋Corollary 13](/en/math/commutative_algebra/basic_notions#cor13) implies that $\Bl_\mathfrak{a}A$ is also Noetherian. Therefore, the submodule $\Bl_{\mathcal{J}'}M'$ of $\Bl_\mathcal{J}M$ is also finitely generated, and applying [Proposition 6](#prop6) again yields the desired result.
:::

::: Corollary 8 (Krull intersection theorem)
Fix a Noetherian ring $A$, an ideal $\mathfrak{a}$ of $A$, and a finitely generated $A$-module $M$. Then the following hold.

1. There exists $a\in \mathfrak{a}$ such that $(1-a)\left(\bigcap_1^\infty \mathfrak{a}^i M\right)=0$.
2. If $\mathfrak{a}$ is a proper ideal and $A$ is a domain or a local ring, then $\bigcap \mathfrak{a}^i=0$ holds.
:::
::: Proof
Consider the $\mathfrak{a}$-stable filtration

$$M\supseteq \mathfrak{a}M \supseteq \mathfrak{a}^2 M\supseteq\cdots$$

of $M$. Then, by [Lemma 7](#lem7), the filtration

$$\left(\bigcap \mathfrak{a}^iM\right) \cap M\supseteq \left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}M \supseteq \left(\bigcap \mathfrak{a}^iM\right) \cap \mathfrak{a}^2 M\supseteq\cdots$$

is also $\mathfrak{a}$-stable. In other words, there exists some $n$ such that for every $p>n$,

$$\mathfrak{a}\left(\left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}^p M\right)=\left(\bigcap \mathfrak{a}^iM\right)\cap \mathfrak{a}^{p+1} M$$

. Now, simplifying each side of the above identity yields

$$\mathfrak{a}\left(\bigcap \mathfrak{a}^iM\right)=\left(\bigcap \mathfrak{a}^iM\right)$$

. Since $A$ is Noetherian and $M$ is finitely generated, $\bigcap \mathfrak{a}^iM$ is also finitely generated, so applying [§Integral Extensions, ⁋Lemma 7](/en/math/commutative_algebra/integral_extension#lem7) gives the first result.

For the second result, set $M=A$. For the element $a$ obtained from the first result, it suffices to show that $1-a$ is not a zerodivisor. First, since $\mathfrak{a}$ is a proper ideal of $A$, we have $1-a\neq 0$, so if $A$ is a domain there is nothing more to prove. If $A$ is a local ring, then $\mathfrak{a}$ is contained in the (unique) maximal ideal $\mathfrak{m}$ of $A$, so $a\in \mathfrak{m}$, and hence $1-a$ must be a unit.
:::

Finally, we define the following.

::: Definition 9
Let $M$ be an $A$-module equipped with an $\mathfrak{a}$-filtration

$$\mathcal{J}:\qquad M=M_0\supseteq M_1\supseteq\cdots$$

and associated graded module $\gr_\mathcal{J}M$. Then for an arbitrary $x\in M$, the *initial form* $\initial(x)$ of $x$ is defined by

$$\initial(x)=x+M_{k+1}\quad\text{in $M_k/M_{k+1}$,}\qquad\text{where $k$ is the greatest integer satisfying $x\in M_k$}$$

. If $x\in\bigcap_k M_k$, such a $k$ does not exist, and in this case we define $\initial(x)=0$.
:::

In this situation, suppose an arbitrary $A$-submodule $M'\subseteq M$ is given. Then, viewing $\gr_\mathcal{J}M$ as a $\gr_\mathfrak{a}A$-module, we can define $\initial(M')$ to be the $\gr_\mathfrak{a}A$-submodule of $\gr_\mathcal{J}M$ generated by the $\initial(x)$ for $x\in M'$.

::: Example 10
Let $A=\mathbb{K}[\x,\y]$ and $\mathfrak{a}=(\x,\y)$. Then $\gr_\mathfrak{a}A$ is a graded ring whose grading is determined by the degree of polynomials. Now set $M=A$ and consider the $A$-submodule (i.e., ideal of $A$) $\mathfrak{b}=(\x^2, \y^2)$ of $M$. Since every element of $\mathfrak{b}$ is of the form

$$f(\x,\y)\x^2+g(\x,\y)\y^2$$

, $\initial(\mathfrak{b})$ is the homogeneous ideal of $\gr_\mathfrak{a}A$ generated by $\x^2, \y^2$.
:::

In general, however, $\initial(M')$ is not generated by the initial forms of generators of $M'$. For instance, with $A$ and $\mathfrak{a}$ as above, consider $\mathfrak{c}=(\x^2-\y^3, \x\y)$; the initial forms of the two generators are $\x^2$ and $\x\y$, respectively. Since $\x(\x\y)-\y(\x^2-\y^3)=\y^4$, we have $\y^4\in \mathfrak{c}$, and hence $\initial(\y^4)=\y^4$ belongs to $\initial(\mathfrak{c})$; but every element of $(\x^2,\x\y)$ is divisible by $\x$, so $\y^4$ does not belong to it.

::: Corollary 11
Let $A$ be a Noetherian local ring and $\mathfrak{a}$ a proper ideal of $A$. If $\gr_\mathfrak{a}A$ is a domain, then so is $A$.
:::
::: Proof
Assume $ab=0$ in $A$; it suffices to show that $a=0$ or $b=0$. Now, in $\gr_\mathfrak{a}A$ we must have $\initial(a)\initial(b)=0$, so $\initial(a)$ or $\initial(b)$ must be $0$. Since $\bigcap \mathfrak{a}^n=0$ by [Corollary 8](#cor8), we must have $a=0$ or $b=0$.
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
