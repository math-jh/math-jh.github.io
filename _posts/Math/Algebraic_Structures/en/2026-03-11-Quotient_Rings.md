---
title: "Quotient Rings and Ring Homomorphisms"
description: "A quotient ring is formed from a ring and a two-sided ideal, satisfying the universal property of ring homomorphisms. For any ring homomorphism, the induced homomorphism exists and is unique."
excerpt: "Quotient rings and ring isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_rings
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-05-05
weight: 102
translated_at: 2026-08-18T06:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T06:45:05+00:00
---
In this post we define the notion of a quotient ring. Recalling how [§Quotient Groups](/en/math/algebraic_structures/quotient_groups) was defined, for any group $G$ and any subgroup $H$, the quotient $G/H$ always exists as a set, but it does not always carry a group structure; for that we needed the condition that $H$ be a normal subgroup. Likewise, for a ring $A$, the manner in which a quotient can be defined is also restricted.

## Definition of Quotient Rings

First, if $A$ is an abelian group and $S$ is a subgroup, then $A/S$ carries an abelian group structure. For a ring structure to be defined on top of this, a similar property must hold for multiplication as well. That is, for any two elements $\alpha+S$, $\alpha'+S$ of $A/S$, their product

$$(\alpha+S)(\alpha'+S)\overset{?}{=}\alpha\alpha'+S$$

should be defined as above. On the other hand, for any $x,x'\in S$ we have

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+x\alpha'+\alpha x'+xx',$$

so for the above formula to hold we must always have $x\alpha'+\alpha x'+xx'\in S$. In particular, setting $x'=0$ forces $x\alpha'\in S$ for any $\alpha'\in A$, and setting $x=0$ forces $\alpha x'\in S$ for any $\alpha\in A$. Thus $S$ must be a two-sided ideal of $A$. Conversely, if $S$ is a two-sided ideal, then all three terms $x\alpha'$, $\alpha x'$, $xx'$ lie in $S$, so the above multiplication is well defined independent of the choice of representatives. From this discussion we obtain the following.

::: Definition 1
Let a ring $A$ and a two-sided ideal $\mathfrak{a}$ be given. The ring $A/\mathfrak{a}$ defined as above is called the *quotient ring of $A$ by $\mathfrak{a}$*.
:::

Then the following holds.

::: Proposition 2
For a ring $A$ and a two-sided ideal $\mathfrak{a}$, the following hold.

1. The function $\pi:A\rightarrow A/\mathfrak{a}$ defined by $\alpha\mapsto \alpha+\mathfrak{a}$ is a ring homomorphism.
2. For a ring homomorphism $\phi:A \rightarrow B$, if $\phi(\mathfrak{a})=\{0\}$ then there exists a unique ring homomorphism $\bar{\phi}$ from $A/\mathfrak{a}$ to $B$ such that $\phi=\bar{\phi}\circ\pi$.
:::
::: Proof
1. That $\pi$ defines an abelian group homomorphism with respect to addition follows from the result of [§Quotient Groups](/en/math/algebraic_structures/quotient_groups). That $\pi$ preserves multiplication follows from the calculation
  
    $$\pi(\alpha)\pi(\alpha')=(\alpha+\mathfrak{a})(\alpha'+\mathfrak{a})=\alpha\alpha'+\mathfrak{a}=\pi(\alpha\alpha')$$
    
    and at this point one can check that $1+\mathfrak{a}$ becomes the multiplicative identity of $A/\mathfrak{a}$.
2. First regard $\phi$ as an abelian group homomorphism. Then the given condition implies that the subgroup $\mathfrak{a}$ of $A$ is contained in $\ker \phi$, so there exists a unique *group* homomorphism $\bar{\phi}:A/\mathfrak{a}\rightarrow B$ such that $\phi=\bar{\phi}\circ\pi$. ([§Group Homomorphisms, ⁋Proposition 3](/en/math/algebraic_structures/isomorphism_theorems#prop3))  
    Now choose two arbitrary elements $\alpha+\mathfrak{a}, \beta+\mathfrak{a}$ of $A/\mathfrak{a}$. Then

    $$(\alpha+\mathfrak{a})(\beta+\mathfrak{a})=\alpha\beta+\mathfrak{a}=\pi(\alpha\beta)$$

    so the identity

    $$\bar{\phi}((\alpha+\mathfrak{a})(\beta+\mathfrak{a}))=\bar{\phi}(\pi(\alpha)\pi(\beta))=\bar{\phi}(\pi(\alpha\beta))=\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\bar{\phi}(\pi(\alpha))\bar{\phi}(\pi(\beta))=\bar{\phi}(\alpha+\mathfrak{a})\bar{\phi}(\beta+\mathfrak{a})$$

    shows that $\bar{\phi}$ preserves multiplication. Similarly, from $\bar{\phi}(1+\mathfrak{a})=\bar{\phi}(\pi(1))=\phi(1)=1$ we see that $\bar{\phi}$ sends $1$ to $1$. 
:::

The following theorem can be regarded as the ring-homomorphism version of [§Group Homomorphisms](/en/math/algebraic_structures/isomorphism_theorems).

::: Theorem 3
For a ring homomorphism $\phi:A \rightarrow B$, its kernel $\ker \phi$, and its image $\im\phi$, the following hold.

1. $\ker \phi$ is a two-sided ideal of $A$, and $\alpha+\ker \phi \mapsto \phi(\alpha)$ defines a well-defined isomorphism $A/\ker \phi \rightarrow \im \phi$.
2. For a subring $S$ of $A$, the set $S+\ker \phi=\{\alpha+x\mid\alpha\in S, x\in\ker \phi\}$ is a subring of $A$, the intersection $S\cap\ker \phi$ is a two-sided ideal of $S$, and there is an isomorphism $(S+\ker \phi)/\ker \phi\cong S/(S\cap \ker \phi)$.
3. If two two-sided ideals $\mathfrak{a}, \mathfrak{b}$ of $A$ satisfy $\mathfrak{b}\subseteq \mathfrak{a}$, then $\mathfrak{a}/\mathfrak{b}$ is a two-sided ideal of $A/\mathfrak{b}$ and $(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$.
4. For a two-sided ideal $\mathfrak{a}$ of $A$, there is an inclusion-preserving bijection between the set of two-sided ideals of $A/\mathfrak{a}$ and the set of two-sided ideals of $A$ containing $\mathfrak{a}$.
:::
::: Proof
For 1 and 3 one proceeds almost exactly as in [§Group Homomorphisms](/en/math/algebraic_structures/isomorphism_theorems), and checks that the group homomorphisms obtained there are actually ring homomorphisms in the same way as in part 2 of [Proposition 2](#prop2).

For 2, that $S+\ker \phi$ is a subgroup under addition is the same as in the group case. For any $\alpha,\alpha'\in S$ and $x,x'\in\ker \phi$ we have

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+(x\alpha'+\alpha x'+xx')$$

where $\alpha\alpha'\in S$, and since $\ker \phi$ is a two-sided ideal by 1, the three terms in parentheses all lie in $\ker \phi$. Adding $1\in S$ we obtain that $S+\ker \phi$ is a subring of $A$. Also $S\cap\ker \phi$ is a subgroup of $S$ under addition, and for any $\alpha\in S$ and $y\in S\cap\ker \phi$ both $\alpha y$ and $y\alpha$ belong to $S$ and $\ker \phi$, so this is a two-sided ideal of $S$. Now consider the composition

$$S\hookrightarrow S+\ker \phi\longrightarrow (S+\ker \phi)/\ker \phi$$

which is surjective and has kernel $S\cap\ker \phi$, so applying 1 yields the desired isomorphism.

That the two correspondences $\bar{\mathfrak{b}}\mapsto\pi^{-1}(\bar{\mathfrak{b}})$ and $\mathfrak{b}\mapsto\pi(\mathfrak{b})$ are inverses of each other and preserve inclusions follows from [§Group Homomorphisms, ⁋Theorem 7](/en/math/algebraic_structures/isomorphism_theorems#thm7). It remains to check that these correspondences send two-sided ideals to two-sided ideals. First, for any $\alpha\in A$ and $x\in\pi^{-1}(\bar{\mathfrak{b}})$,

$$\pi(\alpha x)=\pi(\alpha)\pi(x)\in\bar{\mathfrak{b}}$$

so $\alpha x\in\pi^{-1}(\bar{\mathfrak{b}})$, and thus $\pi^{-1}(\bar{\mathfrak{b}})$ is closed under left multiplication. Similarly, since $\pi$ is surjective any element of $A/\mathfrak{a}$ is of the form $\pi(\alpha)$, and therefore

$$\pi(\alpha)\pi(x)=\pi(\alpha x)\in\pi(\mathfrak{b})$$

from which we can verify that $\bar{\mathfrak{b}}$ is closed under left multiplication. The case of right multiplication can be shown in the same way, and hence these are two-sided ideals.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
