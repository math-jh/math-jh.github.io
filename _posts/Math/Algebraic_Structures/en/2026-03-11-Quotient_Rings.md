---
title: "Quotient Rings and Ring Homomorphisms"
excerpt: "Quotient ring and ring isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_rings
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 102
translated_at: 2026-05-29T02:00:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-24T18:00:04+00:00
---
In this post, we define the notion of a quotient ring. Recall from [§Quotient Groups](/en/math/algebraic_structures/quotient_groups) that for any subgroup $$H$$ of a group $$G$$, the quotient $$G/H$$ is always defined as a set, yet it need not carry a group structure; for that, $$H$$ must be a normal subgroup. Likewise, for a ring $$A$$ and a subring $$S$$, the quotient $$A/S$$ need not inherit a ring structure.

## Definition of Quotient Rings

First, if we ignore the multiplicative structures on $$A$$ and $$S$$, then $$S$$ is a subgroup of $$A$$. Since $$A$$ is an abelian group, $$A/S$$ inherits an abelian group structure. To define a ring structure on this quotient, a similar property must hold for multiplication. That is, for any two elements $$\alpha+S$$ and $$\alpha'+S$$ in $$A/S$$, their product

$$(\alpha+S)(\alpha'+S)\overset{?}{=}\alpha\alpha'+S$$

must be defined as above. On the other hand, for any $$xx'\in S$$,

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+x\alpha'+\alpha x'+xx'$$

and since $$xx'\in S$$, the above equation can hold only if $$x\alpha',\alpha x'\in S$$. That is, for any element $$x\in S$$ and any $$\alpha\in A$$, both $$\alpha x\in S$$ and $$x\alpha\in S$$ must hold; hence $$S$$ must be a two-sided ideal of $$A$$. From this discussion we obtain the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let $$A$$ be a ring and $$\mathfrak{a}$$ a two-sided ideal thereof. The ring $$A/\mathfrak{a}$$ defined as above is called the *quotient ring* of $$A$$ by $$\mathfrak{a}$$.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$A$$ be a ring and $$\mathfrak{a}$$ a two-sided ideal. Then the following hold:

1. The map $$\pi:A\rightarrow A/\mathfrak{a}$$ defined by $$\alpha\mapsto \alpha+\mathfrak{a}$$ is a ring homomorphism.
2. For a ring homomorphism $$\phi:A \rightarrow B$$, if $$\phi(\mathfrak{a})=\{0\}$$, then there exists a unique $$\bar{\phi}:A/\mathfrak{a}\rightarrow B$$ such that $$\phi=\bar{\phi}\circ\pi$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. That $$\pi$$ is an abelian group homomorphism with respect to addition follows immediately from the results of [§Quotient Groups](/en/math/algebraic_structures/quotient_groups). That $$\pi$$ preserves multiplication is likewise clear from the above discussion, and one easily verifies that $$1+\mathfrak{a}$$ is the multiplicative identity in $$A/\mathfrak{a}$$.
2. First, regard $$\phi$$ as an abelian group homomorphism. Then the subgroup $$\mathfrak{a}$$ of $$A$$ is contained in $$\ker \phi$$ by the given condition, so there exists a unique *group* homomorphism $$\bar{\phi}:A/\mathfrak{a}\rightarrow B$$ such that $$\phi=\bar{\phi}\circ\pi$$. ([§Isomorphism Theorems, ⁋Proposition 3](/en/math/algebraic_structures/isomorphism_theorems#prop3))
    Now take any two elements $$\alpha+\mathfrak{a}, \beta+\mathfrak{a}$$ in $$A/\mathfrak{a}$$. Then

    $$(\alpha+\mathfrak{a})(\beta+\mathfrak{a})=\alpha\beta+\mathfrak{a}=\pi(\alpha\beta)$$

    so

    $$\bar{\phi}((\alpha+\mathfrak{a})(\beta+\mathfrak{a}))=\bar{\phi}(\pi(\alpha)\pi(\beta))=\bar{\phi}(\pi(\alpha\beta))=\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\bar{\phi}(\pi(\alpha))\bar{\phi}(\pi(\beta))=\bar{\phi}(\alpha+\mathfrak{a})\bar{\phi}(\beta+\mathfrak{a})$$

    and therefore $$\bar{\phi}$$ preserves multiplication. Similarly, $$\bar{\phi}(1+\mathfrak{a})=\bar{\phi}(\pi(1))=\phi(1)=1$$, so $$\bar{\phi}$$ sends $$1$$ to $$1$$.

</details>

The following theorem may be regarded as the ring-homomorphism version of [§Isomorphism Theorems](/en/math/algebraic_structures/isomorphism_theorems).

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3**</ins> Let $$\phi:A \rightarrow B$$ be a ring homomorphism with kernel $$\ker \phi$$ and image $$\im\phi$$. Then the following hold:

1. $$\ker \phi$$ is a two-sided ideal of $$A$$, and the map $$\alpha+\ker \phi \mapsto \phi(\alpha)$$ is a well-defined isomorphism $$A/\ker \phi \rightarrow \im \phi$$.
2. For a subring $$S$$ of $$A$$, the set $$S+\ker \phi=\{\alpha+x\mid\alpha\in S, x\in\ker \phi\}$$ is a subring of $$A$$, and $$S\cap\ker \phi$$ is a two-sided ideal of $$S$$; moreover, there is an isomorphism $$(S+\ker \phi)/\ker \phi\cong S/(S\cap \ker f)$$.
3. If $$\mathfrak{a}, \mathfrak{b}$$ are two-sided ideals of $$A$$ satisfying $$\mathfrak{b}\subseteq \mathfrak{a}$$, then $$\mathfrak{a}/\mathfrak{b}$$ is a two-sided ideal of $$A/\mathfrak{b}$$ and $$(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$$.
4. For a two-sided ideal $$\mathfrak{a}$$ of $$A$$, there is an inclusion-preserving bijection between the set of two-sided ideals of $$A/\mathfrak{a}$$ and the set of ideals of $$A$$ containing $$\mathfrak{a}$$.

</div>

As with [Proposition 2](#prop2), the proof proceeds almost exactly as in [§Isomorphism Theorems](/en/math/algebraic_structures/isomorphism_theorems); the only additional step is to verify that the resulting group homomorphisms are indeed ring homomorphisms.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
