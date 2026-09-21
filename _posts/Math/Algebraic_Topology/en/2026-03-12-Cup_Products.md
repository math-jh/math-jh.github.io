---
title: "Cup Product"
description: "We cover the definition and properties of the cup product defined on cohomology. We examine how to construct the cohomology ring through the multiplicative structure arising from being a contravariant functor."
excerpt: "Exterior product of cohomology, cup product definition, and ring structure"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cup_products
sidebar: 
    nav: "algebraic_topology-en"

date: 2025-09-12
weight: 11
translated_at: 2026-08-18T15:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-21T15:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Earlier, when introducing cohomology, we stated that one of the greatest advantages of cohomology is the multiplicative structure naturally defined on it. It would then also be a reasonable question why this structure was not seen in homology; once we define this multiplicative structure in this post, it will become clear that this is essentially because cohomology is a contravariant functor.

## The Cross Product in Cohomology

Fix a commutative ring $A$, and suppose that chain complexes of $A$-modules $C_\bullet,D_\bullet$ are given. ([\[Algebraic Structures\] §Direct Products, Direct Sums, and Tensor Products of Modules, ⁋Proposition 8](/en/math/algebraic_structures/operations_of_modules#prop8){: data-lid="7nh4b" data-relation="required" }) For their dual sequences

$$(C^\vee)^\bullet=\Hom_A(C_\bullet,A),\qquad (D^\vee)^\bullet=\Hom_A(D_\bullet,A)$$

and 

$$((C\otimes D)^\vee)^\bullet=\Hom_A((C\otimes D)_\bullet,A)$$

we first define 

$$\times:(C^\vee\otimes D^\vee)^\bullet\rightarrow ((C\otimes D)^\vee)^\bullet$$

To do this, it suffices to take a simple tensor $\phi\otimes \psi$ on the left-hand side and assign to it a function from $(C\otimes D)_\bullet$ to $A$, which in turn is defined by its values on the simple tensors of $(C\otimes D)_\bullet$. If $\phi\in (C^\vee)^p,\psi\in (D^\vee)^q$, we define this correspondence to be the function that, only for a simple tensor belonging precisely to $C_p\otimes D_q$, $\alpha\otimes \beta$, is

$$(\phi\times\psi):(C\otimes D)_\bullet \rightarrow A;\qquad (\alpha\otimes \beta)\mapsto (-1)^{\deg(\alpha)\deg(\beta)}\phi(\alpha)\psi(\beta)$$

and is $0$ on the rest. Then it is not difficult to verify that this is a morphism of cochain complexes, and therefore $\times$ defines a map on cohomology

$$\bar{\times}: (H(C^\vee)\otimes H(D^\vee))^\bullet\rightarrow H^\bullet(C^\vee\otimes D^\vee)\rightarrow H^\bullet((C\otimes D)^\vee)$$

Now suppose that for two topological spaces $X,Y$, the $A$-valued chains

$$C_\bullet(X;A),\qquad C_\bullet(Y;A)$$

are given. Setting $C_\bullet=C_\bullet(X;A), D_\bullet=C_\bullet(Y;A)$ and taking the above cochain map, we compose it with the map induced by the Alexander-Whitney map $\AW$ from [§Cohomology](/en/math/algebraic_topology/cohomology){: data-lid="aqy4b" data-relation="required" } to obtain the following cochain map

$$(C^\vee(X;A)\otimes C^\vee(Y;A))^\bullet \overset{\times}{\longrightarrow} \Hom_A(C_\bullet(X;A)\otimes C_\bullet(Y;A),A)\overset{\Hom(\AW,A)}{\longrightarrow} \Hom_A(C_\bullet(X\times Y;A),A)=(C^\vee)^\bullet(X\times Y)$$

and descending this again to the cohomology level, for each $(p,q)$ we obtain the $A$-module homomorphism

$${\AW^\ast}\circ{(-\mathbin{\bar{\times}}-)}:H^p(X;A)\otimes_A H^q(Y;A)\rightarrow H^{p+q}(X\times Y;A)$$

When there is no risk of confusion, let us simply write this as $\times$.

## Definition and Basic Properties of the Cup Product

Now we can define the cup product.

::: Definition 1
For a commutative ring $A$ and a topological space $X$, the composition

$${\smile}:H^\bullet(X;A)\otimes_A H^\bullet(X;A)\overset{\AW^\ast\circ\bar{\times}}{\longrightarrow}H^\bullet(X\times X;A)\overset{\Delta^\ast}{\longrightarrow} H^\bullet(X;A)$$

is called the *cup product* on $H^\bullet(X;A)$.
:::

At this stage, it becomes apparent why the cup product did not appear explicitly in homology. Using the Eilenberg–Zilber map, one can construct up to

$$H_p(X;A)\otimes_A H_q(X;A)\rightarrow H_{p+q}(X\times X;A)$$

but applying the homology functor to the diagonal map $\Delta:X\rightarrow X\times X$ is covariant, so the direction would not match.

Explicitly, for any $\alpha\in H^p(X;A)$ and $\beta\in H^q(X;A)$, $\alpha\smile\beta\in H^{p+q}(X;A)$ is given on any singular simplex $\sigma:\Delta^{p+q}\rightarrow X$ by the following formula:

$$(\alpha\smile\beta)(\sigma)=(\Delta^\ast\AW^\ast(\alpha\mathbin{\bar{\times}}\beta))(\sigma)=(\alpha\mathbin{\bar{\times}}\beta)(\AW(\Delta(\sigma)))=(-1)^{pq}\alpha(\text{front face of $\sigma$})\beta(\text{back face of $\sigma$})$$

As this explicit computation shows, the cup product in de Rham cohomology is something very familiar, corresponding to the wedge product of differential forms.

Then, as its name suggests, the cup product defines a multiplicative structure on the cohomology ring. However, since $H^\bullet(X;A)$ is also a graded ring, care must be taken when discussing the commutativity of the multiplication defined on it, as follows.

::: Proposition 2
Fix a topological space $X$ and a commutative ring $A$. Then

$$(H^\bullet(X;A), {\smile}, 1)$$

forms a graded-commutative, $\mathbb{N}$-graded $A$-algebra. Here $1\in H^0(X;A)$ is the cocycle that sends every singular 0-simplex of $X$ to $1\in A$.
:::

That is, for homogeneous classes $\alpha\in H^p(X;A),\beta\in H^q(X;A),\gamma\in H^r(X;A)$, the following hold:

- (Unit) $1\smile\alpha=\alpha\smile 1=\alpha$
- (Associativity) $(\alpha\smile\beta)\smile\gamma=\alpha\smile(\beta\smile\gamma)$
- (Grade-commutativity) $\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$

To show this, one naturally applies [§Acyclic Models Theorem, ⁋Theorem 3](/en/math/algebraic_topology/acyclic_models_theorem#thm3){: data-lid="vears" data-relation="required" } to the functors from $\Top^2$ (or $\Top^3$) to $\Ch_{\geq 0}(\lMod{A})$.

## Functorial Properties of the Cup Product

The property proved above shows that the objects of the functor $H^\bullet(-;A)$, which was initially defined as a functor to $\lMod{A}$, ultimately land in $\gr_{\mathbb{N}}\Alg{A}$. It is then natural to wonder whether $H^\bullet(-;A)$ is a functor from $\Top$ to $\gr_\mathbb{N}\Alg{A}$.

To address this, we must first decide how to view the domain of $\times$, namely $H^\bullet(X;A)\otimes_A H^\bullet(Y;A)$, as an $A$-algebra. For this purpose, we equip it with the product of the graded tensor product, namely the multiplication defined for homogeneous classes $\alpha_1,\alpha_2\in H^\bullet(X;A)$ and $\beta_1,\beta_2\in H^\bullet(Y;A)$ by

$$(\alpha_1\otimes\beta_1)(\alpha_2\otimes\beta_2)=(-1)^{\lvert\beta_1\rvert\lvert\alpha_2\rvert}(\alpha_1\smile\alpha_2)\otimes(\beta_1\smile\beta_2)$$

::: Proposition 3
For any topological spaces $X,Y$ and commutative ring $A$,

$$\times: H^\bullet(X;A)\otimes_A H^\bullet(Y;A) \rightarrow H^\bullet(X\times Y;A)$$

is a graded $A$-algebra homomorphism.
:::
::: Proof
That is, what we wish to show is the commutativity of the following diagram

{% diagram Math/Algebraic_Topology/Cup_Products-1.svg width="41.10em" alt="functoriality_of_cup_products" %}

where the left vertical arrow ${\smile}\otimes{\smile}$ denotes the multiplication of the graded tensor product defined above. Spelled out in formulas, this amounts to showing that for any homogeneous classes $\alpha_1,\alpha_2\in H^\bullet(X;A)$ and $\beta_1,\beta_2\in H^\bullet(Y;A)$,

$$(\alpha_1\times\beta_1)(\alpha_2\times\beta_2)=\Delta_{X\times Y}^\ast (\alpha_1\times\beta_1\times\alpha_2\times\beta_2)=(-1)^{\lvert\beta_1\rvert\lvert\alpha_2\rvert}(\alpha_1\smile\alpha_2)\times(\beta_1\smile\beta_2)$$

holds. For the second equality, consider the homeomorphism $T:X\times X\times Y\times Y\rightarrow X\times Y\times X\times Y$ that swaps the two middle factors; since $\Delta_{X\times Y}=T\circ(\Delta_X\times\Delta_Y)$, the middle term equals $(\Delta_X\times\Delta_Y)^\ast T^\ast(\alpha_1\times\beta_1\times\alpha_2\times\beta_2)$. Then, for the homeomorphism $\tau:X\times Y\rightarrow Y\times X$ that swaps the two factors, applying the formula $\tau^\ast(\beta\times\alpha)=(-1)^{\lvert\alpha\rvert\lvert\beta\rvert}\alpha\times\beta$ given by the same acyclic models argument as [Proposition 2](#prop2){: data-lid="6ict5" data-relation="required" } to $T=\id_X\times\tau\times\id_Y$, we obtain

$$T^\ast(\alpha_1\times\beta_1\times\alpha_2\times\beta_2)=(-1)^{\lvert\beta_1\rvert\lvert\alpha_2\rvert}\alpha_1\times\alpha_2\times\beta_1\times\beta_2$$

Finally, since $\AW$ and $\Hom_A(-,A)$ are functorial at the cochain level, applying the naturality $(f\times g)^\ast(\mu\times\nu)=(f^\ast\mu)\times(g^\ast\nu)$ of $\times$ to $\Delta_X\times\Delta_Y$ yields the desired formula from $\Delta_X^\ast(\alpha_1\times\alpha_2)=\alpha_1\smile\alpha_2$ and $\Delta_Y^\ast(\beta_1\times\beta_2)=\beta_1\smile\beta_2$. That this is a graded homomorphism follows from the fact that $\times$ sends $H^p(X;A)\otimes_A H^q(Y;A)$ to $H^{p+q}(X\times Y;A)$; the preservation of $1$ follows from the fact that any singular 0-simplex of $X\times Y$ is sent by $\AW$ to the tensor of its two projections.
:::

Based on this, we can also show the functoriality of the cup product.

::: Proposition 4
For a continuous map $f:X \rightarrow Y$, the map $f^\ast=H^\bullet(f;A):H^\bullet(Y;A)\rightarrow H^\bullet(X;A)$ induced by the cohomology functor is a morphism of graded $A$-algebras. That is, the equation

$$f^\ast(\alpha\smile\beta)=(f^\ast\alpha)\smile(f^\ast\beta)$$

holds.
:::

By the naturality $(f\times f)^\ast(\alpha\times\beta)=(f^\ast\alpha)\times(f^\ast\beta)$ of $\times$ used in the previous proof, we know that the following diagram, whose horizontal arrows are $\times$ and whose vertical arrows are $f^\ast\otimes f^\ast$ and $(f\times f)^\ast$ respectively,

{% diagram Math/Algebraic_Topology/Cup_Products-2.svg width="21.22em" alt="functoriality_1" %}

commutes, so in addition to this, it suffices to apply the cohomology functor to the following diagram:

{% diagram Math/Algebraic_Topology/Cup_Products-3.svg width="8.72em" alt="diagonals_and_f" %}

## Cap product

Now in the remaining part, we prepare to treat the duality between homology and cohomology. Of course, we were able to observe this duality in a form such as [§Cohomology, ⁋Proposition 3](/en/math/algebraic_topology/cohomology#prop3){: data-lid="an0yw" data-relation="weak" }, but what we shall examine this time has a somewhat more subtle flavor.

What we will do from now on is to define an action of the graded ring $H^\bullet(X;A)$ on the homology module $H_\bullet(X;A)$. Writing this as

$${\frown}:H^\bullet(X;A)\otimes_A H_\bullet(X;A) \rightarrow H_\bullet(X;A)$$

the property we require of $\frown$ is the following *adjunction formula*

$$\langle \alpha\smile\beta,\sigma\rangle=\langle \alpha,\beta\frown \sigma\rangle$$

through which $H_\bullet(X;A)$ acquires an $H^\bullet(X;A)$-module structure. Here $\langle-,-\rangle$ is the pairing induced by the Kronecker pairing

$$\langle-,-\rangle: C^\bullet(X;A)\times C_\bullet(X;A) \rightarrow A$$

Now, for this equation to hold, we must have

$$\langle\alpha,\beta\frown \sigma\rangle=\langle\alpha\smile \beta,\sigma\rangle=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\alpha(\sigma_i)\beta(\tau_i)$$

Here, each of $\sigma_i$ and $\tau_i$ is a chain appearing when $\sigma$ is expressed as $\sum \sigma_i\otimes\tau_i$ via the Alexander-Whitney map. Then, since this equation must hold for all $\alpha$, we must define

$$\beta\frown \sigma=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(\tau_i)\sigma_i$$

::: Definition 5
The map defined above

$${\frown}:H^p(X;A)\otimes H_{p+q}(X;A) \rightarrow H_q(X;A)$$

is called the *cap product*.
:::

That is, $\frown$ is obtained by taking a homology chain of degree $p+q$ and a cohomology chain of degree $p$, evaluating the degree $p$ part of the homology chain and the cohomology chain via the Kronecker pairing, and then scalar-multiplying the remaining degree $q$ homology chain by this constant. This may appear to be a somewhat artificial definition, but by the uniqueness in [§Acyclic Models Theorem, ⁋Theorem 3](/en/math/algebraic_topology/acyclic_models_theorem#thm3){: data-lid="5gix8" data-relation="weak" }, it can be said to be the only definition that makes sense. Moreover, from this expression we see that this is precisely the operation corresponding to the interior product.

On the other hand, since the Alexander-Whitney map sends chains of a subspace $X_0\subseteq X$ back to tensors of chains of $X_0$, the above construction works equally well for pairs. Indeed, if $\beta$ vanishes on $C_p(X_0)$, then for a chain $\sigma$ of $X_0$, the $\beta(\tau_i)$ are all $0$, so that $\beta\frown\sigma=0$; hence $\frown$ descends to relative chains. The *relative cap product* obtained in this way

$${\frown}:H^p(X,X_0;A)\otimes H_{p+q}(X,X_0;A) \rightarrow H_q(X;A)$$

will also be denoted by the same symbol in what follows, and the case $X_0=\emptyset$ is [Definition 5](#def5){: data-lid="pofnt" data-relation="weak" }. Then the following holds.

::: Proposition 6 (Projection formula)
For a continuous map of pairs $f:(X,X_0) \rightarrow (Y,Y_0)$, $\beta\in H^q(Y,Y_0;A)$, and $\sigma\in H_{p+q}(X,X_0;A)$, the identity

$$f_\ast(f^\ast\beta\frown\sigma)=\beta\frown f_\ast\sigma$$

holds.
:::
::: Proof
Applying the Alexander-Whitney map to a relative cycle representing $\sigma$, let us write $\AW(\sigma)=\sum_i\sigma_i\otimes\tau_i$. Then since $(f^\ast\beta)(\tau_i)=\beta(C_\bullet(f)(\tau_i))$, from the explicit formula used to derive [Definition 5](#def5){: data-lid="pho4o" data-relation="required" }, we obtain

$$C_\bullet(f)(f^\ast\beta\frown\sigma)=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(C_\bullet(f)(\tau_i))C_\bullet(f)(\sigma_i)$$

On the other hand, since $\AW$ is natural, $\AW(C_\bullet(f)(\sigma))=\sum_i C_\bullet(f)(\sigma_i)\otimes C_\bullet(f)(\tau_i)$, and since $C_\bullet(f)$ preserves degree, applying the same explicit formula to $\beta$ and $C_\bullet(f)(\sigma)$ also yields the same expression for $\beta\frown C_\bullet(f)(\sigma)$. Finally, since $f$ sends $X_0$ into $Y_0$, the map $C_\bullet(f)$ sends $C_\bullet(X_0)$ to $C_\bullet(Y_0)$; therefore if $\beta$ vanishes on $C_\bullet(Y_0)$, then $f^\ast\beta$ also vanishes on $C_\bullet(X_0)$. That is, the cap products on both sides are both well-defined on relative classes, and descending to homology gives the desired identity.
:::

---

**References**

**[Hat]** A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.

---
