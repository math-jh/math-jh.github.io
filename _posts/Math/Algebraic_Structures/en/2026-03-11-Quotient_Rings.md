---

title: "Quotient Rings and Ring Homomorphisms"
excerpt: "Quotient ring and ring isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/quotient_rings
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Quotient_rings.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-en"

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 102

---

In this article, we define the notion of a quotient ring. Recall from [§Quotient Groups](/en/math/algebraic_structures/quotient_groups) that for any subgroup $$H$$ of a group $$G$$, the set $$G/H$$ is always defined as a set, but it does not always carry a group structure; for this, we needed the condition that $$H$$ be a normal subgroup. Similarly, for a ring $$A$$ and a subring $$S$$, the set $$A/S$$ does not always carry a ring structure.

## Definition of Quotient Rings

First, if we forget the multiplicative structure of $$A$$ and $$S$$, then $$S$$ is a subgroup of $$A$$. Since $$A$$ is an abelian group, $$A/S$$ has an abelian group structure. For a ring structure to be defined on this, a similar property must hold for the multiplication. That is, for any two elements $$\alpha+S$$ and $$\alpha'+S$$ of $$A/S$$, their product

$$(\alpha+S)(\alpha'+S)\overset{?}{=}\alpha\alpha'+S$$

should be defined as above. Now, for any $$xx'\in S$$,

$$(\alpha+x)(\alpha'+x')=\alpha\alpha'+x\alpha'+\alpha x'+xx'$$

and since $$xx'\in S$$, for the above equation to hold, we must have $$x\alpha',\alpha x'\in S$$ always. That is, for an element $$x$$ of $$S$$, when we take any $$\alpha\in A$$, both $$\alpha x\in S$$ and $$x\alpha\in S$$ must hold, so $$S$$ must be a two-sided ideal of $$A$$. From this discussion, we obtain the following.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let a ring $$A$$ and a two-sided ideal $$\mathfrak{a}$$ be given. The ring $$A/\mathfrak{a}$$ defined as above is called the *quotient ring* of $$A$$ by $$\mathfrak{a}$$.

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a ring $$A$$ and a two-sided ideal $$\mathfrak{a}$$, the following holds:

1. The function $$\pi:A\rightarrow A/\mathfrak{a}$$ defined by $$\alpha\mapsto \alpha+\mathfrak{a}$$ is a ring homomorphism.
2. For a ring homomorphism $$\phi:A \rightarrow B$$, if $$\phi(\mathfrak{a})=\{0\}$$, then there exists a unique $$\bar{\phi}$$ from $$A/\mathfrak{a}$$ to $$B$$ such that $$\phi=\bar{\phi}\circ\pi$$ holds.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. That $$\pi$$ defines an abelian group homomorphism with respect to addition follows immediately from the results of [§Quotient Groups](/en/math/algebraic_structures/quotient_groups). That $$\pi$$ preserves multiplication is also clear from the above discussion, and we can verify that $$1+\mathfrak{a}$$ is the multiplicative identity of $$A/\mathfrak{a}$$.
2. First, consider $$\phi$$ as an abelian group homomorphism. By the given condition, the subgroup $$\mathfrak{a}$$ of $$A$$ is contained in $$\ker \phi$$, so there exists a unique *group* homomorphism $$\bar{\phi}:A/\mathfrak{a}\rightarrow B$$ such that $$\phi=\bar{\phi}\circ\pi$$ holds. ([§Isomorphisms, ⁋Proposition 3](/en/math/algebraic_structures/isomorphism_theorems#prop3]))
    Now choose any two elements $$\alpha+\mathfrak{a}, \beta+\mathfrak{a}$$ of $$A/\mathfrak{a}$$. Then

    $$(\alpha+\mathfrak{a})(\beta+\mathfrak{a})=\alpha\beta+\mathfrak{a}=\pi(\alpha\beta)$$

    so by the equation

    $$\bar{\phi}((\alpha+\mathfrak{a})(\beta+\mathfrak{a}))=\bar{\phi}(\pi(\alpha)\pi(\beta))=\bar{\phi}(\pi(\alpha\beta))=\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\bar{\phi}(\pi(\alpha))\bar{\phi}(\pi(\beta))=\bar{\phi}(\alpha+\mathfrak{a})\bar{\phi}(\beta+\mathfrak{a})$$

    we see that $$\bar{\phi}$$ preserves multiplication. Similarly, from $$\bar{\phi}(1+\mathfrak{a})=\bar{\phi}(\pi(1))=\phi(1)=1$$, we see that $$\bar{\phi}$$ sends $$1$$ to $$1$$.

</details>

The following theorem can be considered as the ring homomorphism version of [§Isomorphisms](/en/math/algebraic_structures/isomorphism_theorems).

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3**</ins> For a ring homomorphism $$\phi:A \rightarrow B$$ with kernel $$\ker \phi$$ and image $$\im\phi$$, the following holds:

1. $$\ker \phi$$ is a two-sided ideal of $$A$$, and $$\alpha+\ker \phi \mapsto \phi(\alpha)$$ defines a well-defined isomorphism $$A/\ker \phi \rightarrow \im \phi$$.
2. For a subring $$S$$ of $$A$$, the set $$S+\ker \phi=\{\alpha+x\mid\alpha\in S, x\in\ker \phi\}$$ is a subring of $$A$$, and $$S\cap\ker \phi$$ is a two-sided ideal of $$S$$, with an isomorphism $$(S+\ker \phi)/\ker \phi\cong S/(S\cap \ker f)$$.
3. If two two-sided ideals $$\mathfrak{a}, \mathfrak{b}$$ of $$A$$ satisfy $$\mathfrak{b}\subseteq \mathfrak{a}$$, then $$\mathfrak{a}/\mathfrak{b}$$ is a two-sided ideal of $$A/\mathfrak{b}$$ and $$(A/\mathfrak{b})/(\mathfrak{a}/\mathfrak{b})\cong A/\mathfrak{a}$$ holds.
4. For a two-sided ideal $$\mathfrak{a}$$ of $$A$$, there is an inclusion-preserving bijection between the set of two-sided ideals of $$A/\mathfrak{a}$$ and the set of ideals of $$A$$ containing $$\mathfrak{a}$$.

</div>

The proof follows almost identically to what was done in [§Isomorphisms](/en/math/algebraic_structures/isomorphism_theorems), as in [Proposition 2](#prop2), with the only additional step being to verify that the resulting group homomorphisms are indeed ring homomorphisms.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
