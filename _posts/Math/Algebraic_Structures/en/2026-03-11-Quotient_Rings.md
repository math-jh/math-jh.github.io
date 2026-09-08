---
title: "Quotient Rings and Ring Isomorphisms"
description: "A quotient ring is formed from a ring and a two-sided ideal and satisfies the universal property of ring homomorphisms. For any ring homomorphism, the induced homomorphism exists and is unique."
excerpt: "Quotient rings and ring isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_rings
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-05-05
weight: 102
translated_at: 2026-08-18T06:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-08T15:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In this post we define the notion of a quotient ring. Recalling when we defined [§Quotient Groups](/en/math/algebraic_structures/quotient_groups), for any group $G$ and any subgroup $H$, $G/H$ is always defined as a set, but it did not always have a group structure, and for this, the condition that $H$ is a normal subgroup was required. Likewise, for a ring $A$, the manner in which a quotient can be defined is restricted.

## Definition of Quotient Rings

First, if $A$ is an abelian group and $S$ is its subgroup, an abelian group structure exists on $A/S$. For a ring structure to be defined on top of this, a similar property must hold for the multiplicative structure as well. That is, for any two elements $\alpha+S$, $\alpha'+S$ of $A/S$, their product

$$(\alpha+S)(\alpha'+S)\overset{?}{=}\alpha\alpha'+S$$

must be defined as above. On the other hand, since for any $x,x'\in S$

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+x\alpha'+\alpha x'+xx'$$

in order for the above formula to hold, $x\alpha'+\alpha x'+xx'\in S$ must always hold. In particular, setting $x'=0$, for any $\alpha'\in A$ we must have $x\alpha'\in S$, and setting $x=0$, for any $\alpha\in A$ we must have $\alpha x'\in S$. That is, $S$ must be a two-sided ideal of $A$. Conversely, if $S$ is a two-sided ideal, then the three terms $x\alpha'$, $\alpha x'$, $xx'$ all belong to $S$, so the multiplication above is well-defined independently of the choice of representatives. From this discussion we obtain the following.

::: Definition 1
Let a ring $A$ and a two-sided ideal $\mathfrak{a}$ be given. The ring $A/\mathfrak{a}$ defined as above is called the *quotient ring by $\mathfrak{a}$ of $A$*.
:::

Then the following holds.

::: Proposition 2
For a ring $A$ and a two-sided ideal $\mathfrak{a}$, the following hold.

1. Defined by $\alpha\mapsto \alpha+\mathfrak{a}$, the function $\pi:A\rightarrow A/\mathfrak{a}$ is a ring homomorphism.
2. For a ring homomorphism $\phi:A \rightarrow B$, if $\phi(\mathfrak{a})=\{0\}$, then from $A/\mathfrak{a}$ to $B$ there exists a unique ring homomorphism $\bar{\phi}$ such that $\phi=\bar{\phi}\circ\pi$ holds.
:::
::: Proof
1. That $\pi$ defines an abelian group homomorphism with respect to addition is a result of [§Quotient Groups](/en/math/algebraic_structures/quotient_groups). That $\pi$ preserves multiplication is obtained from the following calculation
  
    $$\pi(\alpha)\pi(\alpha')=(\alpha+\mathfrak{a})(\alpha'+\mathfrak{a})=\alpha\alpha'+\mathfrak{a}=\pi(\alpha\alpha')$$
    
    and here one can verify that $1+\mathfrak{a}$ becomes the $1$ of $A/\mathfrak{a}$.
2. First regard $\phi$ as an abelian group homomorphism. Then by the given condition, the subgroup of $A$, $\mathfrak{a}$, is contained in $\ker \phi$, so from $A/\mathfrak{a}$ to $B$ there exists a unique *group* homomorphism $\bar{\phi}:A/\mathfrak{a}\rightarrow B$ such that $\phi=\bar{\phi}\circ\pi$ holds. ([§Group Isomorphisms, ⁋Proposition 3](/en/math/algebraic_structures/isomorphism_theorems#prop3))  
    Now arbitrarily choose two elements of $A/\mathfrak{a}$, $\alpha+\mathfrak{a}, \beta+\mathfrak{a}$. Then since

    $$(\alpha+\mathfrak{a})(\beta+\mathfrak{a})=\alpha\beta+\mathfrak{a}=\pi(\alpha\beta)$$

    by the following equation,

    $$\bar{\phi}((\alpha+\mathfrak{a})(\beta+\mathfrak{a}))=\bar{\phi}(\pi(\alpha)\pi(\beta))=\bar{\phi}(\pi(\alpha\beta))=\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\bar{\phi}(\pi(\alpha))\bar{\phi}(\pi(\beta))=\bar{\phi}(\alpha+\mathfrak{a})\bar{\phi}(\beta+\mathfrak{a})$$

    $\bar{\phi}$ preserves multiplication. Similarly, from $\bar{\phi}(1+\mathfrak{a})=\bar{\phi}(\pi(1))=\phi(1)=1$, $\bar{\phi}$ sends $1$ to $1$. 
:::

The following theorem can be regarded as the ring homomorphism version of [§Group Isomorphisms](/en/math/algebraic_structures/isomorphism_theorems).

::: Theorem 3
For a ring homomorphism $\phi:A \rightarrow B$, its kernel $\ker \phi$, and its image $\im\phi$, the following hold.

1. $\ker \phi$ is a two-sided ideal of $A$, and $\alpha+\ker \phi \mapsto \phi(\alpha)$ defines a well-defined isomorphism $A/\ker \phi \rightarrow \im \phi$.
2. For a subring of $A$, $S$, the set $S+\ker \phi=\{\alpha+x\mid\alpha\in S, x\in\ker \phi\}$ is a subring of $A$, $S\cap\ker \phi$ becomes a two-sided ideal of $S$, and there exists an isomorphism $(S+\ker \phi)/\ker \phi\cong S/(S\cap \ker \phi)$. 
3. If two two-sided ideals of $A$, $\mathfrak{a}, \mathfrak{b}$, satisfy $\mathfrak{b}\subseteq \mathfrak{a}$, then $\mathfrak{a}/\mathfrak{b}$ is a two-sided ideal of $A/\mathfrak{b}$ and $(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$ holds.
4. For a two-sided ideal of $A$, $\mathfrak{a}$, there exists an inclusion-preserving bijection between the set of two-sided ideals of $A/\mathfrak{a}$ and the set of two-sided ideals containing $\mathfrak{a}$ in $A$.
:::
::: Proof
Parts 1 and 3 proceed almost identically to what was treated in [§Group Isomorphisms](/en/math/algebraic_structures/isomorphism_theorems); one only needs to verify that the group homomorphism obtained there is in fact also a ring homomorphism in the same manner as part 2 of [Proposition 2](#prop2).

In the case of 2, that $S+\ker \phi$ is a subgroup under addition is the same as in the case of groups. For any $\alpha,\alpha'\in S$ and $x,x'\in\ker \phi$, in

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+(x\alpha'+\alpha x'+xx')$$

we have $\alpha\alpha'\in S$, and since $\ker \phi$ is a two-sided ideal by 1, the three terms in parentheses all belong to $\ker \phi$. Adding $1\in S$ to this, we obtain that $S+\ker \phi$ is a subring of $A$. Also, $S\cap\ker \phi$ is a subgroup of $S$ under addition, and for any $\alpha\in S$ and $y\in S\cap\ker \phi$, since both $\alpha y$ and $y\alpha$ belong to both $S$ and $\ker \phi$, this is a two-sided ideal of $S$. Now considering the composition

$$S\hookrightarrow S+\ker \phi\longrightarrow (S+\ker \phi)/\ker \phi$$

this is surjective and its kernel is $S\cap\ker \phi$, so applying 1 yields the desired isomorphism.

That the two correspondences $\bar{\mathfrak{b}}\mapsto\pi^{-1}(\bar{\mathfrak{b}})$ and $\mathfrak{b}\mapsto\pi(\mathfrak{b})$ in 4 are inverses of each other and preserve inclusion follows from [§Group Isomorphisms, ⁋Theorem 7](/en/math/algebraic_structures/isomorphism_theorems#thm7). What remains is that this correspondence sends two-sided ideals to two-sided ideals. First, for any $\alpha\in A$ and $x\in\pi^{-1}(\bar{\mathfrak{b}})$,

$$\pi(\alpha x)=\pi(\alpha)\pi(x)\in\bar{\mathfrak{b}}$$

so $\alpha x\in\pi^{-1}(\bar{\mathfrak{b}})$, and thus $\pi^{-1}(\bar{\mathfrak{b}})$ is closed under left multiplication. Similarly, since $\pi$ is surjective, any element of $A/\mathfrak{a}$ is of the form $\pi(\alpha)$, and therefore 

$$\pi(\alpha)\pi(x)=\pi(\alpha x)\in\pi(\mathfrak{b})$$

from which we can verify that $\bar{\mathfrak{b}}$ is closed under left multiplication. The case of right multiplication can be shown in the same way, and hence these are two-sided ideals.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
