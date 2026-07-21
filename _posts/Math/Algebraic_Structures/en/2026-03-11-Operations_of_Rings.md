---
title: "Product, Coproduct, and Tensor Product of Rings"
description: "The product and coproduct of rings are defined categorically, and it is shown that the category of rings is complete. The structure of the tensor product is also discussed."
excerpt: "Definitions of product, coproduct, and tensor product of rings"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_rings
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-08-10
weight: 103
translated_at: 2026-07-18T20:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-18T20:30:01+00:00
---
Now we define the product and coproduct of rings.

## Product of rings

The product of rings presents no difficulty. Let a family of rings $(A_i)_{i\in I}$ be given. Then the product of abelian groups $\prod_{i\in I}A_i$ is well-defined. The multiplication structure on each $A_i$, given by $\mu_i: A_i\otimes A_i \rightarrow A_i$, is the same as a bilinear map $A_i\times A_i \rightarrow A_i$, and through this we can define a function between sets

$$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I} A_i\right) \cong \prod_{i\in I} (A_i\times A_i) \overset{\prod \mu_i}{\longrightarrow} \prod_{i\in I}A_i.$$

::: Proposition 1
The function defined above is a bilinear map from the abelian group $\left(\prod A_i\right)\times\left(\prod A_i\right)$ to $\prod A_i$, and therefore induces an abelian group homomorphism $\left(\prod A_i\right)\otimes\left(\prod A_i\right) \rightarrow \prod A_i$.
:::
::: Proof
Writing the above function explicitly in terms of elements, an element of $\prod A_i$ is of the form $(\alpha_i)_{i\in I}$, and for two elements $(\alpha_i)_{i\in I}, (\beta_i)_{i\in I}\in \prod A_i$, applying the above function to them yields

$$(\alpha_i)_{i\in I}(\beta_i)_{i\in I}=(\alpha_i\beta_i)_{i\in I}$$

so multiplication is defined componentwise. Bilinearity is also checked componentwise.
:::

Thus $\prod A_i$ carries a ring structure. The additive identity of this ring is the element all of whose components are $0$, and the multiplicative identity is the element all of whose components are $1$. On the other hand, for any two ring homomorphisms $\phi,\psi:A \rightarrow B$, if we define

$$\Eq(\phi,\psi)=\{\alpha\in A\mid \phi(\alpha)=\psi(\alpha)\}$$

then this is a subgroup of $A$ by [§Group Homomorphisms, ⁋Proposition 2](/en/math/algebraic_structures/group_homomorphisms#prop2), and moreover for any $\alpha,\beta\in\Eq(\phi,\psi)$,

$$\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\psi(\alpha)\psi(\beta)=\psi(\alpha\beta)$$

so $\alpha\beta\in\Eq(\phi,\psi)$. That is, $\Eq(\phi,\psi)$ is a subring of $A$, and this defines the equalizer of $\phi$ and $\psi$ in $\Ring$. From this, the following holds.

::: Theorem 2
The category $\Ring$ is complete.
:::

On the other hand, one useful notion in $\Rng$ is the direct sum. Consider a family of rings $(A_i)_{i\in I}$. Among the elements of the direct product $\prod_{i\in I}A_i$, the collection of those that are finitely supported, i.e., all but finitely many components are $0$, is closed under addition and multiplication and forms a subring of $\prod A_i$. (The sum and product of two finitely supported families are still finitely supported.) This is called the following.

::: Definition 3
For a family of rings $(A_i)_{i\in I}$, the collection of finitely supported elements of the direct product $\prod_{i\in I}A_i$ is called the *direct sum* of the rings, and is written as $\bigoplus_{i\in I} A_i$.
:::

This is exactly the same in spirit as the direct sum defined for abelian groups in [\[Algebraic Structures\] §Abelian Groups, ⁋Definition 2](/en/math/algebraic_structures/abelian_groups#def2). However, when the index set $I$ is infinite, the direct sum $\bigoplus A_i$ does not contain the identity element $(1)_{i\in I}$, so it is not a (unital) ring, and therefore this notion is mainly used in $\Rng$. Conversely, when $I$ is a finite set, the direct sum coincides exactly with the direct product by definition.

For abelian groups, the direct sum is the coproduct ([\[Algebraic Structures\] §Abelian Groups, ⁋Theorem 1](/en/math/algebraic_structures/abelian_groups#thm1)), but in (non-commutative) rings the direct sum is not the coproduct. This is the same situation as for non-abelian groups, where the direct sum is not the coproduct, and therefore the coproduct of rings must be defined separately.

## Coproduct of rings

Defining the coproduct of rings requires a bit more effort. This is essentially because the multiplication operation of a ring is not commutative, and there was a similar problem when defining the coproduct in $\Grp$. To overcome this, we had to define the free product in a rather cumbersome way in [§Free Products](/en/math/algebraic_structures/free_products). The coproduct can be defined in the same way for rings, but since this will not be used in the subsequent discussion, we only state it as the following proposition.

::: Proposition 4
For any family of rings $(A_i)_{i\in I}$, their coproduct exists.
:::

On the other hand, let any two ring homomorphisms $\phi,\psi:A \rightarrow B$ be given. Let $\mathfrak{b}$ be the two-sided ideal of $B$ generated by the elements $\phi(\alpha)-\psi(\alpha)$; then $B/\mathfrak{b}$ is well-defined. Then, by the same proof as in [§Isomorphism Theorems, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8), the following holds.

::: Proposition 5
In the above situation, $\CoEq(\phi,\psi)=B/\mathfrak{b}$ defines the coequalizer of $\phi,\psi$.
:::

Therefore, the following holds.

::: Theorem 6
The category $\Ring$ is a bicomplete category.
:::

## Tensor product of rings

Finally, we define the tensor product $\otimes$ in $\Ring$. For this, it suffices to define a multiplication structure on the abelian group $A\otimes B$ for any two rings $A,B$, i.e., an abelian group homomorphism

$$(A\otimes B)\otimes(A\otimes B) \rightarrow A\otimes B.$$

By the associativity and commutativity of the tensor product,

$$(A\otimes B)\otimes(A\otimes B)\cong (A\otimes A)\otimes (B\otimes B)$$

holds, and therefore $\mu_A:A\otimes A \rightarrow A$ and $\mu_B: B\otimes B \rightarrow B$ define a multiplication on $A\otimes B$ by

$$(A\otimes B)\otimes(A\otimes B)\cong (A\otimes A)\otimes (B\otimes B)\overset{\mu_A\otimes\mu_B}{\longrightarrow} A\otimes B.$$

::: Definition 7
For any rings $A,B$, the ring $A\otimes B$ defined as above is called their *tensor product*.
:::

Through this, one can verify that the category $\Ring$ forms a symmetric monoidal category $(\Ring,\otimes, \mathbb{Z})$. Explicitly, the multiplication on $A\otimes B$ is defined by

$$(\alpha\otimes \beta)(\alpha'\otimes \beta')=\alpha\alpha'\otimes \beta\beta'.$$

One interesting fact is that $\otimes$ is the same as the coproduct in $\cRing$. To verify this, it suffices to show that for any commutative rings $A,B$, the map

$$\iota_A: A \hookrightarrow A\otimes B;\quad \alpha\mapsto \alpha\otimes 1$$

and the similarly defined $\iota_B$ satisfy the universal property of the coproduct. Let any $\phi_A: A \rightarrow C$, $\phi_B: B \rightarrow C$ be given. If there exists $\phi: A\otimes B \rightarrow C$ satisfying the universal property of the coproduct, then it must necessarily satisfy

$$\phi(\alpha\otimes \beta)=\phi((\alpha\otimes 1)(1\otimes \beta))=\cdots=\phi_A(\alpha)\phi_B(\beta)$$

so it is unique. On the other hand, since the function $(\alpha,\beta)\mapsto \phi_A(\alpha)\phi_B(\beta)$ from $A\times B$ to $C$ is bilinear, the universal property of the tensor product yields a ring homomorphism $A\otimes B \rightarrow C$ satisfying $\alpha\otimes \beta\mapsto \phi_A(\alpha)\phi_B(\beta)$, and this is exactly $\phi$.
