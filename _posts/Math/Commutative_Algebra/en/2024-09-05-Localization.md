---
title: "Localization"
description: "It covers the localization process of rings and the properties of local rings with a unique maximal ideal, extending to the localization of modules and the concept of multiplicatively closed subsets."
excerpt: "Localization of rings and modules and local ring construction"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/localization
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-09-05
weight: 2
translated_at: 2026-06-26T14:00:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-03T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Local Rings

In this post, we define localization. Briefly speaking, localization can be thought of as the process of making a ring $A$ into a local ring.

::: Definition 1
A ring $A$ is a *local ring* if $A$ has a unique maximal ideal.
:::

Then we can show the following equivalence.

::: Proposition 2
For a ring $A$, the following are equivalent.

1. $A$ is a local ring. 
2. There exists an ideal $\mathfrak{m}\subsetneq A$ such that all non-units of $A$ belong to $\mathfrak{m}$.
3. The collection of all non-units of $A$ forms an ideal.
:::
::: Proof
First assume 1, and suppose an arbitrary non-unit of $A$, $a\in A$, is given. Then, since $a$ is not a unit, $(a)$ satisfies $(a)\subsetneq A$, so as an ideal of $A$, by [\[Algebraic Structures\] §Definition of a Ring, ⁋Theorem 10](/en/math/algebraic_structures/rings#thm10){: data-lid="lt4t7" } it is contained in some maximal ideal. But since $A$ has a unique maximal ideal $\mathfrak{m}$, we must have $(a)\subseteq \mathfrak{m}$, and therefore $a\in \mathfrak{m}$.

Now assume 2 and show 3. For this, it suffices to show that the collection of non-units of $A$ is closed under addition. First, from $\mathfrak{m}\neq A$ we know that $\mathfrak{m}$ contains no units of $A$. From this we see that the collection of all non-units of $A$ must equal $\mathfrak{m}$.

Finally, we must assume condition 3 and show condition 1. For any ideal $\mathfrak{a}\subsetneq A$, by the preceding observation we know that $\mathfrak{a}$ consists only of non-units, and therefore $\mathfrak{a}$ is contained in the ideal of all non-units of $A$, $\mathfrak{m}$. On the other hand, $\mathfrak{m}$ is a maximal ideal, because any element of $A\setminus \mathfrak{m}$ is a unit of $A$, so the only ideal containing $\mathfrak{m}$ is $A$.
:::

## Localization of Modules

As explained in the previous post, to see the localization of a ring we define the localization of a module more generally.

::: Definition 3
For a ring $A$, a subset $S$ is *multiplicatively closed* if any product of elements of $S$ again belongs to $S$.
:::

In particular, since $1$ can be regarded as the product of a family indexed by the empty set, by definition $1\in S$.

::: Definition 4
For a ring $A$, an $A$-module $M$, and a multiplicative subset of $A$, $S$, the *localization* at $S$ of $M$ is the $A$-module $S^{-1}M$ defined as follows.

1. As a set, $S^{-1}M$ is the quotient set obtained by defining on $M\times S$ the following equivalence relation:
    
    $$(x,s)\sim (x',s')\iff \text{there exists $t\in S$ such that $t(s'x-sx')=0$}$$
  
    Here, the equivalence class containing $(x,s)$ is denoted by $x/s$.
2. On $S^{-1}M$, the $A$-module structure is defined as follows:
  
  $$\frac{x}{s}+\frac{x'}{s'}=\frac{s'x+sx'}{ss'},\qquad a\cdot \frac{x}{s}=\frac{ax}{s}.$$
:::

We should verify that the operations defined in condition 2 actually give an $A$-module structure, but this is not difficult. Instead, we add a few observations. First, for any $t\in S$ and $x/s\in S^{-1}M$,

$$\frac{tx}{ts}=\frac{x}{s}$$

holds. This is simply because $1(txs-tsx)=0$. Also, we can examine the identity and inverse with respect to addition in $S^{-1}M$: first, for any $s,s'\in S$, we can verify that

$$\frac{0}{s}=\frac{0}{s'}$$

holds, and from the equation

$$\frac{0}{s'}+\frac{x}{s}=\frac{x}{s}+\frac{0}{s'}=\frac{0s+s'x}{ss'}=\frac{s'x}{s's}=\frac{x}{s}$$

we see that this is the identity with respect to addition in $S^{-1}M$. By a similar calculation, one can verify that the inverse of any $x/s$ is $(-x)/s$.

The above calculations are no different from the addition and multiplication of fractions we have done since middle school. Taking this as intuition, we can define the canonical map from $M$ to $S^{-1}M$, $\epsilon: M \rightarrow S^{-1}M$, by $x\mapsto x/1$. Unfortunately, in general $\epsilon$ may not be an inclusion; the reason is obvious upon reflection and is captured in the following proposition.

::: Proposition 5
In the above situation, $\epsilon(x)=0$ if and only if there exists $s\in S$ such that $sx=0$. In particular, if $M$ is finitely generated, then $S^{-1}M=0$ if and only if some $s\in S$ annihilates $M$.
:::
::: Proof
If 

$$\epsilon(x)=x/1=0=0/1$$

then there exists $s\in S$ such that 

$$s(1x-0\cdot1)=sx=0$$

holds. The above argument also holds in the reverse direction.
:::

## Localization of Rings

The simplest example of localization is the ring of fractions examined in [\[Algebraic Structures\] §Field of Fractions, ⁋Definition 2](/en/math/algebraic_structures/field_of_fractions#def2){: data-lid="059uz" }. Here we took $M=A$. In particular, we also saw that if $A$ is an integral domain, then its ring of fractions $\Frac(A)$ is a field. ([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 6](/en/math/algebraic_structures/field_of_fractions#prop6){: data-lid="ls922" })

As another example, similarly taking $M=A$, for $A$ with a prime ideal $\mathfrak{p}$, setting $S=A\setminus \mathfrak{p}$ allowed us to consider $A_\mathfrak{p}=S^{-1}A$. Using [Definition 4](#def4){: data-lid="xoitz" }, this can also be applied to any $A$-module $M$, and the resulting $A$-module is denoted by $M_\mathfrak{p}$. 

Both of the above examples have a multiplication structure in addition to the addition structure and scalar multiplication by $A$ defined in [Definition 4](#def4){: data-lid="h58hy" }. Explicitly, this structure is given by

$$\frac{x}{s}\frac{x'}{s'}=\frac{xx'}{ss'}$$

so we can regard $S^{-1}A$ as an $A$-algebra. 

The localization of a ring has the following universal property.

::: Proposition 6
Fix rings $A,B$ and, for $A$, a multiplicative subset $S$. If under a ring homomorphism $f:A \rightarrow B$, the image of $S$, $f(S)\subseteq B$, satisfies $f(S)\subseteq B^\times$, then there exists a unique ring homomorphism $\overline{f}: S^{-1}A \rightarrow B$ such that $\overline{f}\circ\epsilon=f$ holds. 
:::
::: Proof
Suppose that $f$ satisfying the given condition is given. If there exists $\overline{f}: S^{-1}A \rightarrow B$ satisfying the given condition, then for any $a/s\in S^{-1}A$,

$$\overline{f}\left(\frac{a}{s}\right)=\overline{f}\left(\frac{a}{1}\frac{1}{s}\right)=\overline{f}(\epsilon(a)\epsilon(s)^{-1})=\overline{f}(\epsilon(a))\overline{f}(\epsilon(s)^{-1})=f(a)f(s)^{-1}$$

must hold, so if $\overline{f}$ exists, it is uniquely determined by the formula above. Now it suffices to show that, defined by the above formula $\overline{f}(a/s)=f(a)f(s)^{-1}$, $\overline{f}: S^{-1}A \rightarrow B$ is a ring homomorphism, and this is merely a simple calculation.
:::

From this, the functoriality of localization can also be shown. 

## Localization and Ideals

Meanwhile, there is a particular relationship between localization and ideals. First, let us define the following.

::: Definition 7
For a ring homomorphism $f:A \rightarrow B$, an ideal of $A$, $\mathfrak{a}$, and an ideal of $B$, $\mathfrak{b}$, we define the following.

1. Under $f$, the *contraction* of $\mathfrak{b}$ is defined as the ideal of $A$, $f^{-1}(\mathfrak{b})$, and is denoted by $\mathfrak{b}^c$.
2. Under $f$, the *extension* of $\mathfrak{a}$ is defined as the ideal generated by the image $f(\mathfrak{a})$ in $B$, and is denoted by $\mathfrak{a}^e$.
:::

To make the first definition, one must prove that $f^{-1}(\mathfrak{b})$ is an ideal, but this proof is easy. While the above notations are useful, they are relatively less intuitive, so after this post we will write $f^{-1}(\mathfrak{b})$ and $f(\mathfrak{a})B$ instead of the above notations.

::: Proposition 8
For any ring $A$, multiplicative subset $S$, localization $S^{-1}A$, and canonical map $\epsilon:A \rightarrow S^{-1}A$, the following hold.

1. For any ideal $\mathfrak{b}\subseteq S^{-1}A$, we have $\mathfrak{b}=\mathfrak{b}^{ce}$.
2. For any ideal $\mathfrak{a}\subseteq A$,
  
    $$\mathfrak{a}^{ec}=\{a\in A\mid\text{there exists $s\in S$ satisfying $sa\in \mathfrak{a}$}\}$$
  
    holds. In particular, $\mathfrak{a}^e=S^{-1}A$ if and only if $\mathfrak{a}\cap S\neq\emptyset$.

Therefore, there exists an inclusion-preserving bijection between the prime ideals of $S^{-1}A$ and the prime ideals of $A$ that do not meet $S$.
:::
::: Proof
1. First, $\mathfrak{b}^{ce}\subseteq \mathfrak{b}$ always holds in general. For the reverse direction, let $a/s\in \mathfrak{b}$. Then $s(a/s)=a/1$ must belong to $\mathfrak{b}$, so $a\in \mathfrak{b}^c$ holds. Hence $a/1\in \mathfrak{b}^{ce}$, and from this we see that $a/s=(1/s)(a/1)\in \mathfrak{b}^{ce}$.
2. Let us denote the right-hand side of the given equation by $\mathfrak{a}'$ for convenience. Then first, for any $a'\in \mathfrak{a}'$, there exists $s$ such that $sa'\in \mathfrak{a}$. Now from $a'/1=sa'/s\in \mathfrak{a}^e$, we see that $a'\in \mathfrak{a}^{ec}$. Conversely, for any $a\in \mathfrak{a}^{ec}$, we can find $a'\in \mathfrak{a}$ and $s\in S$ satisfying $a/1=a'/s$. Then there exists a suitable $t\in S$ such that $tsa=ta'\in \mathfrak{a}$, and since $ts\in S$, we have $a\in \mathfrak{a}'$ by definition. Also,
  
  $$\mathfrak{a}^e=S^{-1}A\iff 1/1\in \mathfrak{a}^e\iff 1\in \mathfrak{a}^{ec}\iff \text{there exists $s\in S$ s.t. $s1\in \mathfrak{a}$}\iff \mathfrak{a}\cap S\neq \emptyset$$

Now from the result of 2, given any prime ideal $\mathfrak{b}\subseteq S^{-1}A$, we know that $\mathfrak{b}^c$ is a prime ideal of $A$ not meeting $S$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 10](/en/math/algebraic_structures/field_of_fractions#prop10){: data-lid="w4bhk" }) Conversely, let $\mathfrak{a}\subseteq A$ be a prime ideal of $A$ not meeting $S$. Then $\mathfrak{a}^e$ is a prime ideal of $S^{-1}A$. Suppose $(b/t)(b'/t')\in \mathfrak{a}^e$ for arbitrary $b/t,b'/t'$. Then there exist $a\in \mathfrak{a}$ and $s\in S$ such that $(bb')/(tt')=a/s$, and hence there exists $u\in S$ such that $utt'a=usbb'\in \mathfrak{a}$. Now from $\mathfrak{a}\cap S=\emptyset$, we know that $us\not\in \mathfrak{a}$, and since $\mathfrak{a}$ is a prime ideal, $bb'\in \mathfrak{a}$ holds. Therefore $b\in \mathfrak{a}$ or $b'\in \mathfrak{a}$, and $\mathfrak{a}^e$ is a prime ideal. That these correspondences are mutual inverses follows naturally from the results of 1 and 2.
:::

The following is immediate from the above proposition.

::: Corollary 9
The localization of a Noetherian ring is Noetherian.
:::
::: Proof
Suppose an ascending chain of ideals of $S^{-1}A$

$$\mathfrak{b}_0\subseteq \mathfrak{b}_1\subseteq\cdots$$

is given. Then

$$\mathfrak{b}_0^c\subseteq \mathfrak{b}_1^c\subseteq\cdots$$

is an ascending chain of ideals in the Noetherian ring $A$, so there exists $N$ such that whenever $n>N$, $\mathfrak{b}_n^c=\mathfrak{b}_{n+1}^c$. Now for such $n$,

$$\mathfrak{b}_n=\mathfrak{b}_n^{ce}=\mathfrak{b}_{n+1}^{ce}=\mathfrak{b}_{n+1}$$
:::

Meanwhile, from [Proposition 8](#prop8){: data-lid="e4606" }, for any prime ideal $\mathfrak{p}$ of $A$ it is immediate that $\mathfrak{p}^e=\mathfrak{p}A_\mathfrak{p}$ is the unique *maximal* ideal of $A_\mathfrak{p}$. That is, $A_\mathfrak{p}$ is a local ring, and its quotient $A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$ is a field.

::: Definition 10
For a ring $A$ and a prime ideal $\mathfrak{p}$, we call the field $A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$ the *residue field* of $A$ at $\mathfrak{p}$ and denote it by $\kappa(\mathfrak{p})$.
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
