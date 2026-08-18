---
title: "Products, Coproducts, and Tensor Products of Rings"
description: "We define products and coproducts of rings categorically, show that the category of rings is complete, and discuss the structure of tensor products."
excerpt: "Categorical definitions of ring products, coproducts, and tensor products"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/operations_of_rings
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-08-10
weight: 103
translated_at: 2026-08-18T09:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T09:15:04+00:00
---
Now we define products and coproducts of rings.

## Products of Rings

The product of rings can be defined without difficulty. Let a family of rings $(A_i)_{i\in I}$ be given. Then the product of abelian groups $\prod_{i\in I}A_i$ is well-defined. On the other hand, the multiplication structure $\mu_i: A_i\otimes A_i \rightarrow A_i$ on $A_i$ is the same as a bilinear map $A_i\times A_i \rightarrow A_i$, and through this we can define a function between sets

$$\left(\prod_{i\in I} A_i\right)\times\left(\prod_{i\in I} A_i\right) \cong \prod_{i\in I} (A_i\times A_i) \overset{\prod \mu_i}{\longrightarrow} \prod_{i\in I}A_i.$$

::: Proposition 1
The function defined above is a bilinear map from the abelian group $\left(\prod A_i\right)\times\left(\prod A_i\right)$ to $\prod A_i$, and therefore induces an abelian group homomorphism $\left(\prod A_i\right)\otimes\left(\prod A_i\right) \rightarrow \prod A_i$.
:::
::: Proof
Writing the above function explicitly in terms of elements, elements of $\prod A_i$ are tuples $(\alpha_i)_{i\in I}$, and for two elements $(\alpha_i)_{i\in I}, (\beta_i)_{i\in I}\in \prod A_i$, the result of applying the above function to these two is given by

$$(\alpha_i)_{i\in I}(\beta_i)_{i\in I}=(\alpha_i\beta_i)_{i\in I}$$

so that multiplication is defined. That is, the given function multiplies two elements componentwise. Now bilinearity can also be checked componentwise.
:::

Through this, $\prod A_i$ also carries a ring structure. Here, the additive identity of this ring is the element all of whose components are $0$, and the multiplicative identity is the element all of whose components are $1$. On the other hand, for any two ring homomorphisms $\phi,\psi:A \rightarrow B$,

$$\Eq(\phi,\psi)=\{\alpha\in A\mid \phi(\alpha)=\psi(\alpha)\}$$

is a subgroup of $A$ by [\[Algebraic Structures\] §Group Homomorphisms, ⁋Proposition 2](/en/math/algebraic_structures/group_homomorphisms#prop2), and moreover for any $\alpha,\beta\in\Eq(\phi,\psi)$,

$$\phi(\alpha\beta)=\phi(\alpha)\phi(\beta)=\psi(\alpha)\psi(\beta)=\psi(\alpha\beta)$$

so $\alpha\beta\in\Eq(\phi,\psi)$, and also $\phi(1)=1=\psi(1)$ so $1\in\Eq(\phi,\psi)$. That is, $\Eq(\phi,\psi)$ is a subring of $A$, and this defines the equalizer of $\phi$ and $\psi$ in $\Ring$. From this, the following holds.

::: Theorem 2
The category $\Ring$ is complete.
:::

On the other hand, one useful notion in $\Rng$ is the direct sum. Consider a family of rings $(A_i)_{i\in I}$. Among the elements of the direct product $\prod_{i\in I}A_i$, those that are finitely supported (that is, all but finitely many components are $0$) are closed under addition and multiplication and form a subobject of $\prod A_i$ in $\Rng$. (The sum and product of two finitely supported families are still finitely supported.) This is called the following.

::: Definition 3
For a family of rings $(A_i)_{i\in I}$, the collection of finitely supported elements of the direct product $\prod_{i\in I}A_i$ is called the *direct sum* of rings and is written $\bigoplus_{i\in I} A_i$.
:::

This is exactly the same in spirit as the direct sum defined for abelian groups in [\[Algebraic Structures\] §Abelian Groups, ⁋Definition 2](/en/math/algebraic_structures/abelian_groups#def2). However, if all $A_i$ are nonzero and the index set $I$ is infinite, then the direct sum $\bigoplus A_i$ does not contain the identity element $(1)_{i\in I}$, so it is not a (unital) ring; because of this, this notion is mainly used in $\Rng$. Conversely, when $I$ is a finite set, the direct sum coincides exactly with the direct product by definition.

In the case of abelian groups the direct sum is the coproduct ([\[Algebraic Structures\] §Abelian Groups, ⁋Theorem 1](/en/math/algebraic_structures/abelian_groups#thm1)), but in (non-commutative) rings the direct sum is not the coproduct. This is analogous to the situation in non-abelian groups, where the direct sum is not the coproduct either, and therefore the coproduct of rings must be defined separately.

## Coproducts of Rings

Defining the coproduct of rings, however, requires a little effort. This is essentially because the multiplication operation of a ring is not commutative, and there was a similar problem when defining the coproduct in $\Grp$. To overcome this, we had to define the free product in a rather tedious way in [§Free Products](/en/math/algebraic_structures/free_products). In rings, the coproduct can be defined in the same manner, but since its construction repeats that of the free product verbatim, we omit it here.

::: Proposition 4
For any family of rings $(A_i)_{i\in I}$, their coproduct exists.
:::

On the other hand, let any two ring homomorphisms $\phi,\psi:A \rightarrow B$ be given. Let $\mathfrak{b}$ be the two-sided ideal of $B$ generated by the elements $\phi(\alpha)-\psi(\alpha)$; then $B/\mathfrak{b}$ is well-defined. The same proof as in [\[Algebraic Structures\] §Group Homomorphisms, ⁋Proposition 8](/en/math/algebraic_structures/isomorphism_theorems#prop8) then shows that the following holds.

::: Proposition 5
In the above situation, $\CoEq(\phi,\psi)=B/\mathfrak{b}$ defines the coequalizer of $\phi,\psi$.
:::

By [Proposition 4](#prop4) and [Proposition 5](#prop5), $\Ring$ has arbitrary coproducts and coequalizers, so it is cocomplete, and adding [Theorem 2](#thm2) to this we obtain the following.

::: Theorem 6
The category $\Ring$ is a bicomplete category.
:::

## Tensor Products of Rings

Finally, we define the tensor product $\otimes$ in $\Ring$. For this, it suffices to define a multiplication structure on the abelian group $A\otimes B$ for any two rings $A,B$, that is, an abelian group homomorphism

$$(A\otimes B)\otimes(A\otimes B) \rightarrow A\otimes B.$$

However, by the associativity and commutativity of the tensor product,

$$(A\otimes B)\otimes(A\otimes B)\cong (A\otimes A)\otimes (B\otimes B)$$

holds, and therefore $\mu_A:A\otimes A \rightarrow A$ and $\mu_B: B\otimes B \rightarrow B$ define a multiplication on $A\otimes B$:

$$(A\otimes B)\otimes(A\otimes B)\cong (A\otimes A)\otimes (B\otimes B)\overset{\mu_A\otimes\mu_B}{\longrightarrow} A\otimes B.$$

::: Definition 7
For any rings $A,B$, the ring $A\otimes B$ defined as above is called their *tensor product*.
:::

Through this, one can verify that the category $\Ring$ forms a symmetric monoidal category $(\Ring,\otimes, \mathbb{Z})$. Explicitly, the multiplication on $A\otimes B$ is defined by

$$(\alpha\otimes \beta)(\alpha'\otimes \beta')=\alpha\alpha'\otimes \beta\beta'.$$

One interesting fact is that $\otimes$ coincides with the coproduct in $\cRing$. To verify this, it suffices to show that

$$\iota_A: A \rightarrow A\otimes B;\quad \alpha\mapsto \alpha\otimes 1$$

and $\iota_B$ defined in a similar way satisfy the universal property of the coproduct. Let any commutative ring $C$ and ring homomorphisms $\phi_A: A \rightarrow C$, $\phi_B: B \rightarrow C$ be given. If there exists $\phi: A\otimes B \rightarrow C$ satisfying the universal property of the coproduct, then it must necessarily satisfy

$$\phi(\alpha\otimes \beta)=\phi((\alpha\otimes 1)(1\otimes \beta))=\cdots=\phi_A(\alpha)\phi_B(\beta)$$

so we see that it is unique. On the other hand, the map $(\alpha,\beta)\mapsto \phi_A(\alpha)\phi_B(\beta)$ from $A\times B$ to $C$ is bilinear, so by the universal property of the tensor product there exists an abelian group homomorphism $A\otimes B \rightarrow C$ sending $\alpha\otimes \beta\mapsto \phi_A(\alpha)\phi_B(\beta)$; since $C$ is commutative, $\phi_B(\beta)$ and $\phi_A(\alpha')$ commute, so this map preserves multiplication and also sends $1\otimes 1$ to $1$, hence it is a ring homomorphism and is exactly $\phi$.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.
