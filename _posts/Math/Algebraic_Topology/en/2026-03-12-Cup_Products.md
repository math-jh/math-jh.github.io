---
title: "Cup Product"
description: "This post covers the definition and properties of the cup product on cohomology. We examine how the multiplicative structure arising from the contravariant functor is used to form the cohomology ring."
excerpt: "The exterior product in cohomology, cup product definition, and ring structure"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cup_products
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-12
weight: 11
translated_at: 2026-08-18T15:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T15:15:05+00:00
---
When introducing cohomology earlier, we observed that one of its greatest strengths is the multiplicative structure naturally defined on it. It is then entirely reasonable to ask why this structure does not appear explicitly in homology; as we define this product in the present post, it will become clear that the reason is essentially that cohomology is a contravariant functor.

## The Exterior Product in Cohomology

Fix a commutative ring $A$, and let $C_\bullet, D_\bullet$ be chain complexes of $A$-modules. For their dual sequences

$$(C^\vee)^\bullet=\Hom_A(C_\bullet,A),\qquad (D^\vee)^\bullet=\Hom_A(D_\bullet,A)$$

and

$$((C\otimes D)^\vee)^\bullet=\Hom_A((C\otimes D)_\bullet,A)$$

we first define

$$\times:(C^\vee\otimes D^\vee)^\bullet\rightarrow ((C\otimes D)^\vee)^\bullet$$

To do this, we take a simple tensor $\phi\otimes \psi$ on the left-hand side and assign to it a function from $(C\otimes D)_\bullet$ to $A$, which is in turn determined by its values on simple tensors of $(C\otimes D)_\bullet$. If $\phi\in (C^\vee)^p$ and $\psi\in (D^\vee)^q$, then for a simple tensor $\alpha\otimes \beta$ belonging precisely to $C_p\otimes D_q$, we set

$$(\phi\times\psi):(C\otimes D)_\bullet \rightarrow A;\qquad (\alpha\otimes \beta)\mapsto (-1)^{\deg(\alpha)\deg(\beta)}\phi(\alpha)\psi(\beta)$$

and declare this correspondence to be the zero function on all other components. It is then straightforward to verify that this is a morphism of cochain complexes, and therefore $\times$ defines a map on cohomology

$$\bar{\times}: (H(C^\vee)\otimes H(D^\vee))^\bullet\rightarrow H^\bullet(C^\vee\otimes D^\vee)\rightarrow H^\bullet((C\otimes D)^\vee)$$

Now let $X,Y$ be topological spaces with $A$-valued chains

$$C_\bullet(X;A),\qquad C_\bullet(Y;A)$$

Setting $C_\bullet=C_\bullet(X;A)$ and $D_\bullet=C_\bullet(Y;A)$ and taking the above cochain map, we compose it with the map induced by the Alexander–Whitney map $\AW$ from [§Cohomology](/en/math/algebraic_topology/cohomology) to obtain the following cochain map

$$(C^\vee(X;A)\otimes C^\vee(Y;A))^\bullet \overset{\times}{\longrightarrow} \Hom_A(C_\bullet(X;A)\otimes C_\bullet(Y;A),A)\overset{\Hom(\AW,A)}{\longrightarrow} \Hom_A(C_\bullet(X\times Y;A),A)=(C^\vee)^\bullet(X\times Y)$$

and descending again to the cohomology level, for each $(p,q)$ we obtain the $A$-module homomorphism

$${\AW^\ast}\circ{(-\mathbin{\bar{\times}}-)}:H^p(X;A)\otimes_A H^q(Y;A)\rightarrow H^{p+q}(X\times Y;A)$$

When there is no risk of confusion, we shall simply write this as $\times$.

## Definition and Basic Properties of the Cup Product

We are now in a position to define the cup product.

::: Definition 1
For a commutative ring $A$ and a topological space $X$, the composition

$${\smile}:H^\bullet(X;A)\otimes_A H^\bullet(X;A)\overset{\AW^\ast\circ\bar{\times}}{\longrightarrow}H^\bullet(X\times X;A)\overset{\Delta^\ast}{\longrightarrow} H^\bullet(X;A)$$

is called the *cup product* on $H^\bullet(X;A)$.
:::

At this stage it becomes apparent why the cup product does not appear explicitly in homology. Using the Eilenberg–Zilber map, one can construct

$$H_p(X;A)\otimes_A H_q(X;A)\rightarrow H_{p+q}(X\times X;A)$$

but applying the homology functor to the diagonal map $\Delta:X\rightarrow X\times X$ goes in the wrong direction because homology is covariant.

Explicitly, for any $\alpha\in H^p(X;A)$ and $\beta\in H^q(X;A)$, the class $\alpha\smile\beta\in H^{p+q}(X;A)$ is given on any singular simplex $\sigma:\Delta^{p+q}\rightarrow X$ by the formula

$$(\alpha\smile\beta)(\sigma)=(\Delta^\ast\AW^\ast(\alpha\mathbin{\bar{\times}}\beta))(\sigma)=(\alpha\mathbin{\bar{\times}}\beta)(\AW(\Delta(\sigma)))=(-1)^{pq}\alpha(\text{front face of $\sigma$})\beta(\text{back face of $\sigma$})$$

As this explicit computation shows, the cup product in de Rham cohomology is a very familiar operation: it corresponds to the wedge product of differential forms.

Then, as its name suggests, the cup product defines a multiplicative structure on the cohomology ring. However, since $H^\bullet(X;A)$ is a graded ring, we must take care when discussing the commutativity of the product defined on it, as follows.

::: Proposition 2
Fix a topological space $X$ and a commutative ring $A$. Then

$$(H^\bullet(X;A), {\smile}, 1)$$

forms a graded-commutative, $\mathbb{N}$-graded $A$-algebra. Here $1\in H^0(X;A)$ is the cocycle that sends every singular 0-simplex of $X$ to $1\in A$.
:::

That is, for homogeneous classes $\alpha\in H^p(X;A)$, $\beta\in H^q(X;A)$, $\gamma\in H^r(X;A)$, the following hold:

- (Unit) $1\smile\alpha=\alpha\smile 1=\alpha$
- (Associativity) $(\alpha\smile\beta)\smile\gamma=\alpha\smile(\beta\smile\gamma)$
- (Graded-commutativity) $\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$

To prove this, we naturally apply [§Acyclic Models Theorem, ⁋Theorem 3](/en/math/algebraic_topology/acyclic_models_theorem#thm3) to the functors from $\Top^2$ (or $\Top^3$) to $\Ch_{\geq 0}(\lMod{A})$.

## Functorial Properties of the Cup Product

The properties proved above show that the objects of the functor $H^\bullet(-;A)$, which were initially defined as functors to $\lMod{A}$, ultimately land in $\gr_{\mathbb{N}}\Alg{A}$. It is then natural to ask whether $H^\bullet(-;A)$ is itself a functor from $\Top$ to $\gr_\mathbb{N}\Alg{A}$.

To address this, we must first decide how to view the domain $H^\bullet(X;A)\otimes_A H^\bullet(Y;A)$ of $\times$ as an $A$-algebra. For this purpose, we equip it with the product of the graded tensor product: for homogeneous classes $\alpha_1,\alpha_2\in H^\bullet(X;A)$ and $\beta_1,\beta_2\in H^\bullet(Y;A)$, we define

$$(\alpha_1\otimes\beta_1)(\alpha_2\otimes\beta_2)=(-1)^{\lvert\beta_1\rvert\lvert\alpha_2\rvert}(\alpha_1\smile\alpha_2)\otimes(\beta_1\smile\beta_2)$$

::: Proposition 3
For any topological spaces $X,Y$ and commutative ring $A$,

$$\times: H^\bullet(X;A)\otimes_A H^\bullet(Y;A) \rightarrow H^\bullet(X\times Y;A)$$

is a graded $A$-algebra homomorphism.
:::
::: Proof
What we wish to show is the commutativity of the following diagram

{% diagram Math/Algebraic_Topology/Cup_Products-1.svg width="41.10em" alt="functoriality_of_cup_products" %}

where the left vertical arrow ${\smile}\otimes{\smile}$ denotes the graded tensor product structure defined above. Spelled out in formulas, this amounts to showing that for any homogeneous classes $\alpha_1,\alpha_2\in H^\bullet(X;A)$ and $\beta_1,\beta_2\in H^\bullet(Y;A)$,

$$(\alpha_1\times\beta_1)(\alpha_2\times\beta_2)=\Delta_{X\times Y}^\ast (\alpha_1\times\beta_1\times\alpha_2\times\beta_2)=(-1)^{\lvert\beta_1\rvert\lvert\alpha_2\rvert}(\alpha_1\smile\alpha_2)\times(\beta_1\smile\beta_2)$$

For the second equality, consider the homeomorphism $T:X\times X\times Y\times Y\rightarrow X\times Y\times X\times Y$ that swaps the two middle factors; since $\Delta_{X\times Y}=T\circ(\Delta_X\times\Delta_Y)$, the middle term equals $(\Delta_X\times\Delta_Y)^\ast T^\ast(\alpha_1\times\beta_1\times\alpha_2\times\beta_2)$. Then, applying the formula $\tau^\ast(\beta\times\alpha)=(-1)^{\lvert\alpha\rvert\lvert\beta\rvert}\alpha\times\beta$, which follows from the same acyclic-models argument as [Proposition 2](#prop2), to the homeomorphism $\tau:X\times Y\rightarrow Y\times X$ that swaps the two factors, with $T=\id_X\times\tau\times\id_Y$, we obtain

$$T^\ast(\alpha_1\times\beta_1\times\alpha_2\times\beta_2)=(-1)^{\lvert\beta_1\rvert\lvert\alpha_2\rvert}\alpha_1\times\alpha_2\times\beta_1\times\beta_2$$

Finally, since $\AW$ and $\Hom_A(-,A)$ are functorial at the cochain level, applying the naturality $(f\times g)^\ast(\mu\times\nu)=(f^\ast\mu)\times(g^\ast\nu)$ of $\times$ to $\Delta_X\times\Delta_Y$ yields the desired formula from $\Delta_X^\ast(\alpha_1\times\alpha_2)=\alpha_1\smile\alpha_2$ and $\Delta_Y^\ast(\beta_1\times\beta_2)=\beta_1\smile\beta_2$. That this is a graded homomorphism follows from the fact that $\times$ sends $H^p(X;A)\otimes_A H^q(Y;A)$ to $H^{p+q}(X\times Y;A)$; the preservation of $1$ follows from the fact that any singular 0-simplex of $X\times Y$ is sent by $\AW$ to the tensor of its two projections.
:::

Building on this, we can also establish the functoriality of the cup product itself.

::: Proposition 4
For a continuous map $f:X \rightarrow Y$, the map $f^\ast=H^\bullet(f;A):H^\bullet(Y;A)\rightarrow H^\bullet(X;A)$ induced by the cohomology functor is a morphism of graded $A$-algebras. That is,

$$f^\ast(\alpha\smile\beta)=(f^\ast\alpha)\smile(f^\ast\beta)$$

holds.
:::

From the naturality $(f\times f)^\ast(\alpha\times\beta)=(f^\ast\alpha)\times(f^\ast\beta)$ of $\times$ used in the previous proof, we already know that the following diagram, whose horizontal arrows are $\times$ and whose vertical arrows are $f^\ast\otimes f^\ast$ and $(f\times f)^\ast$ respectively,

{% diagram Math/Algebraic_Topology/Cup_Products-2.svg width="21.22em" alt="functoriality_1" %}

commutes, and it remains only to apply the cohomology functor to the following diagram

{% diagram Math/Algebraic_Topology/Cup_Products-3.svg width="8.72em" alt="diagonals_and_f" %}

## Cap Product

In what follows we prepare for the study of duality between homology and cohomology. Of course, we have already observed this duality in a form similar to [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3), but what we shall examine now has a somewhat more subtle flavor.

Our present task is to define an action of the graded ring $H^\bullet(X;A)$ on the homology module $H_\bullet(X;A)$. Writing this as

$${\frown}:H^\bullet(X;A)\otimes_A H_\bullet(X;A) \rightarrow H_\bullet(X;A)$$

the property we require of $\frown$ is the following *adjunction formula*

$$\langle \alpha\smile\beta,\sigma\rangle=\langle \alpha,\beta\frown \sigma\rangle$$

which endows $H_\bullet(X;A)$ with an $H^\bullet(X;A)$-module structure. Here $\langle-,-\rangle$ is the pairing induced by the Kronecker pairing

$$\langle-,-\rangle: C^\bullet(X;A)\times C_\bullet(X;A) \rightarrow A$$

For this identity to hold, we must have

$$\langle\alpha,\beta\frown \sigma\rangle=\langle\alpha\smile \beta,\sigma\rangle=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\alpha(\sigma_i)\beta(\tau_i)$$

where $\sigma_i$ and $\tau_i$ are the chains appearing when $\sigma$ is expressed as $\sum \sigma_i\otimes\tau_i$ via the Alexander–Whitney map. Since this formula must hold for all $\alpha$, we are forced to define

$$\beta\frown \sigma=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(\tau_i)\sigma_i$$

::: Definition 5
The map defined above

$${\frown}:H^p(X;A)\otimes H_{p+q}(X;A) \rightarrow H_q(X;A)$$

is called the *cap product*.
:::

That is, $\frown$ takes a homology chain of degree $p+q$ and a cohomology class of degree $p$, evaluates the latter against the degree-$p$ part of the former via the Kronecker pairing, and then multiplies the remaining degree-$q$ homology chain by the resulting scalar. This may appear to be a somewhat artificial definition, but by the uniqueness in [§Acyclic Models Theorem, ⁋Theorem 3](/en/math/algebraic_topology/acyclic_models_theorem#thm3) it is in fact the only sensible one. Moreover, from this expression one recognizes that it corresponds precisely to the interior product.

On the other hand, since the Alexander–Whitney map sends chains of a subspace $X_0\subseteq X$ again to tensors of chains in $X_0$, the above construction works equally well for pairs. Indeed, if $\beta$ vanishes on $C_p(X_0)$, then for a chain $\sigma$ in $X_0$ all $\beta(\tau_i)$ become $0$ and thus $\beta\frown\sigma=0$, so $\frown$ descends to relative chains. The resulting *relative cap product*

$${\frown}:H^p(X,X_0;A)\otimes H_{p+q}(X,X_0;A) \rightarrow H_q(X;A)$$

will also be denoted by the same symbol; the case $X_0=\emptyset$ is [Definition 5](#def5). Then the following holds.

::: Proposition 6 (Projection formula)
For a continuous map of pairs $f:(X,X_0) \rightarrow (Y,Y_0)$, and for $\beta\in H^q(Y,Y_0;A)$ and $\sigma\in H_{p+q}(X,X_0;A)$, the identity

$$f_\ast(f^\ast\beta\frown\sigma)=\beta\frown f_\ast\sigma$$

holds.
:::
::: Proof
Let $\sigma$ be a relative cycle representing the class, and apply the Alexander–Whitney map to write $\AW(\sigma)=\sum_i\sigma_i\otimes\tau_i$. Then since $(f^\ast\beta)(\tau_i)=\beta(C_\bullet(f)(\tau_i))$, the explicit formula used to derive [Definition 5](#def5) gives

$$C_\bullet(f)(f^\ast\beta\frown\sigma)=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(C_\bullet(f)(\tau_i))C_\bullet(f)(\sigma_i)$$

On the other hand, since $\AW$ is natural, $\AW(C_\bullet(f)(\sigma))=\sum_i C_\bullet(f)(\sigma_i)\otimes C_\bullet(f)(\tau_i)$, and since $C_\bullet(f)$ preserves degree, applying the same explicit formula to $\beta$ and $C_\bullet(f)(\sigma)$ yields the same expression for $\beta\frown C_\bullet(f)(\sigma)$. Finally, since $f$ sends $X_0$ into $Y_0$, the map $C_\bullet(f)$ sends $C_\bullet(X_0)$ to $C_\bullet(Y_0)$; therefore if $\beta$ vanishes on $C_\bullet(Y_0)$, then $f^\ast\beta$ also vanishes on $C_\bullet(X_0)$. Thus both sides of the cap product are well-defined on relative classes, and descending to homology gives the desired identity.
:::

---

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.

---
