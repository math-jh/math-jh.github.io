---
title: "Cup Product"
excerpt: "The exterior product in cohomology, the definition of cup product, and the resulting ring structure"

categories: [Math / Algebraic Topology]
permalink: /en/math/algebraic_topology/cup_products
sidebar: 
    nav: "algebraic_topology-en"

date: 2026-03-12
last_modified_at: 2026-03-12
weight: 8
translated_at: 2026-05-29T16:03:58+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-25T17:00:04+00:00
---
When we introduced cohomology earlier, we mentioned that one of its greatest strengths is the multiplicative structure that arises on it naturally. It is then entirely reasonable to ask why this structure was not visible in homology. Once we define this multiplicative structure in the present post, it will become clear that the reason is essentially that cohomology is a contravariant functor.

## Exterior Product of Cohomology

Fix a commutative ring $$A$$, and let $$C_\bullet,D_\bullet$$ be chain complexes of $$A$$-modules. For their dual sequences

$$(C^\vee)^\bullet=\Hom_A(C_\bullet,A),\qquad (D^\vee)^\bullet=\Hom_A(D_\bullet,A)$$

and

$$((C\otimes D)^\vee)^\bullet=\Hom_A((C\otimes D)_\bullet,A)$$

we first define

$$\times:(C^\vee\otimes D^\vee)^\bullet\rightarrow ((C\otimes D)^\vee)^\bullet$$

To do so, we send a simple tensor $$\phi\otimes \psi$$ on the left-hand side to a function from $$(C\otimes D)_\bullet$$ to $$A$$, which is in turn determined by its values on simple tensors in $$(C\otimes D)_\bullet$$. If $$\phi\in (C^\vee)^p,\psi\in (D^\vee)^q$$, we define this correspondence on simple tensors $$\alpha\otimes \beta$$ belonging to $$C_p\otimes D_q$$ by

$$(\phi\times\psi):(C\otimes D)_\bullet \rightarrow A;\qquad (\alpha\otimes \beta)\mapsto (-1)^{\deg(\alpha)\deg(\beta)}\phi(\alpha)\psi(\beta)$$

and declare it to be zero on all other simple tensors. It is then straightforward to verify that this is a morphism of cochain complexes, so $$\times$$ induces a map on cohomology

$$\bar{\times}: H^\bullet(C^\vee\otimes D^\vee)\rightarrow (H(C^\vee)\otimes H(D^\vee))^\bullet\rightarrow H^\bullet((C\otimes D)^\vee)$$

Now let two topological spaces $$X,Y$$ be given with their $$A$$-valued chains

$$C_\bullet(X;A),\qquad C_\bullet(Y;A)$$

Setting $$C_\bullet=C_\bullet(X;A)$$ and $$D_\bullet=C_\bullet(Y;A)$$ and applying the cochain map above, we compose it with the map induced by the Alexander–Whitney map $$\AW$$ from [§Cohomology](/en/math/algebraic_topology/cohomology) to obtain the following cochain map

$$(C^\vee(X;A)\otimes C^\vee(Y;A))^\bullet \overset{\times}{\longrightarrow} \Hom_A(C_\bullet(X;A)\otimes C_\bullet(Y;A),A)\overset{\Hom(\AW,A)}{\longrightarrow} \Hom_A(C_\bullet(X\times Y;A),A)=(C^\vee)^\bullet(X\times Y)$$

Passing to cohomology, for each $$(p,q)$$ we obtain the $$A$$-module homomorphism

$${\AW^\ast}\circ{(-\mathbin{\bar{\times}}-)}:H^p(X;A)\otimes_A H^q(Y;A)\rightarrow H^{p+q}(X\times Y;A)$$

When there is no risk of confusion, we shall simply write this as $$\times$$.

## Definition and Basic Properties of the Cup Product

We are now in a position to define the cup product.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a commutative ring $$A$$ and a topological space $$X$$, the composition

$${\smile}:H^\bullet(X;A)\otimes_A H^\bullet(X;A)\overset{\AW^\ast\circ\bar{\times}}{\longrightarrow}H^\bullet(X\times X)\overset{\Delta^\ast}{\longrightarrow} H^\bullet(X)$$

is called the *cup product* on $$H^\bullet(X;A)$$.

</div>

At this stage it becomes clear why the cup product was not explicitly visible in homology. Using the Eilenberg–Zilber map, one can construct

$$H_p(X;A)\otimes_A H_q(X;A)\rightarrow H_{p+q}(X\times X;A)$$

but applying the homology functor to the diagonal map $$\Delta:X\rightarrow X\times X$$ is covariant, so the directions do not match.

Explicitly, for any $$\alpha\in H^p(X;A)$$ and $$\beta\in H^q(X;A)$$, the element $$\alpha\smile\beta\in H^{p+q}(X;A)$$ is given on any chain $$\sigma:\Delta^{p+q}\rightarrow X$$ by the formula

$$(\alpha\smile\beta)(\sigma)=(\Delta^\ast\AW^\ast(\alpha\mathbin{\bar{\times}}\beta))(\sigma)=(\alpha\mathbin{\bar{\times}}\beta)(\AW(\Delta(\sigma)))=(-1)^{pq}\alpha(\text{front face of $\sigma$})\beta(\text{back face of $\sigma$})$$

As this explicit computation reveals, in de Rham cohomology the cup product is a very familiar object: it corresponds to the wedge product of differential forms.

As its name suggests, the cup product defines a multiplication on the cohomology ring. However, since $$H^\bullet(X;A)$$ is a graded ring, care is required when discussing the commutativity of this multiplication.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Fix a topological space $$X$$ and a commutative ring $$A$$. Then

$$(H^\bullet(X;A), {\smile}, 1)$$

is a graded-commutative, $$\mathbb{N}$$-graded $$A$$-algebra. Here, $$1\in H^0(X;A)$$ is the cocycle sending every $$\Delta$$-simplex of $$X$$ to $$1\in A$$.

</div>

That is, for homogeneous elements $$\alpha\in H^p(X;A),\beta\in H^q(X;A),\gamma\in H^r(X;A)$$, we have

- (Unit) $$1\smile\alpha=\alpha\smile 1=\alpha$$
- (Associativity) $$(\alpha\smile\beta)\smile\gamma=\alpha\smile(\beta\smile\gamma)$$
- (Graded commutativity) $$\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$$

To prove this, we naturally apply [§Acyclic models theorem](/en/math/algebraic_topology/acyclic_models_theorem#thm3) to functors from $$\Top^2$$ (or $$\Top^3$$) to $$\Ch_{\geq 0}(\lMod{A})$$.

## Functoriality of the Cup Product

The property proved above shows that the objects of the functor $$H^\bullet(-;A)$$, although initially defined as landing in $$\lMod{A}$$, ultimately arrive in $$\gr_{\mathbb{N}}\Alg{A}$$. It is then natural to ask whether $$H^\bullet(-;A)$$ itself is a functor from $$\Top$$ to $$\gr_\mathbb{N}\Alg{A}$$.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For any topological spaces $$X,Y$$ and any commutative ring $$A$$,

$$\times: H^\ast(X;A)\otimes_A H^\ast(Y;A) \to H^\ast(X\times Y;A)$$

is a graded $$A$$-algebra homomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

What we must show is the commutativity of the following diagram:

![functoriality_of_cup_products](/assets/images/Math/Algebraic_Topology/Cup_Products-1.png){:style="width:40em" class="invert" .align-center}

For any $$\alpha_1,\alpha_2\in H^\ast(X;A)$$ and any $$\beta_1,\beta_2\in H^\ast(Y;A)$$, we have

$$(\alpha_1\times\beta_1)(\alpha_2\times\beta_2)=\Delta_{X\times Y}^\ast ((\alpha_1\times\beta_1)\times(\alpha_2\times\beta_2))$$

and since the right-hand side is of the form $$\alpha_1\times\beta_1\times\alpha_2\times\beta_2$$, we can regroup the factors appropriately. That this is a graded homomorphism and preserves $$1$$ is clear.

</details>

From this we can also deduce the functoriality of the cup product itself.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For a continuous map $$f:X \rightarrow Y$$, the induced map $$f^\ast=H^\bullet(f;A):H^\bullet(Y;A)\rightarrow H^\bullet(X;A)$$ is a morphism of graded $$A$$-algebras. That is,

$$f^\ast(\alpha\smile\beta)=(f^\ast\alpha)\smile(f^\ast\beta)$$

holds.

</div>

The proof of this proposition is immediate: by [Proposition 3](#prop3) we already know that the following diagram

![functoriality_1](/assets/images/Math/Algebraic_Topology/Cup_Products-2.png){:style="width:20em" class="invert" .align-center}

commutes, and it remains only to apply the cohomology functor to the following diagram

![diagonals_and_f](/assets/images/Math/Algebraic_Topology/Cup_Products-3.png){:style="width:8em" class="invert" .align-center}

## Cap Product

In what follows we prepare the ground for discussing the duality between homology and cohomology. Of course, we have already observed this duality in forms such as [§Cohomology](/en/math/algebraic_topology/cohomology#prop3), but what we now examine is somewhat more subtle.

Our task is to define an action of the graded ring $$H^\bullet(X;A)$$ on the homology module $$H_\bullet(X;A)$$. Writing this as

$${\frown}:H^\bullet(X;A)\otimes_A H_\bullet(X;A) \rightarrow H_\bullet(X;A)$$

the required property of $$\frown$$ is the following *adjunction formula*

$$\langle \alpha\smile\beta,\sigma\rangle=\langle \alpha,\beta\frown \sigma\rangle$$

and through this $$H_\bullet(X;A)$$ becomes an $$H^\bullet(X;A)$$-module. Here, $$\langle-,-\rangle$$ denotes the pairing induced by the Kronecker pairing

$$\langle-,-\rangle: C^\bullet(X;A)\times C_\bullet(X;A) \rightarrow A$$

For this identity to hold we must have

$$\langle\alpha,\beta\frown \sigma\rangle=\langle\alpha\smile \beta,\sigma\rangle=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rangle}\alpha(\sigma_i)\beta(\tau_i)$$

where $$\sigma_i$$ and $$\tau_i$$ are the chains appearing when $$\sigma$$ is written as $$\sum \sigma_i\otimes\tau_i$$ via the Alexander–Whitney map. Since this must hold for all $$\alpha$$, we are forced to define

$$\beta\frown \sigma=\sum_i(-1)^{\lvert\beta\rvert\lvert\sigma_i\rvert}\beta(\tau_i)\sigma_i$$

<div class="definition" markdown="1">

<ins id="def5">**Definition 5**</ins> The map defined above

$$\frown:H^p(X;A)\otimes H_{p+q}(X;A) \rightarrow H_q(X;A)$$

is called the *cap product*.

</div>

Thus $$\frown$$ takes a homology chain of degree $$p+q$$ and a cohomology class of degree $$p$$, pairs the degree $$p$$ part of the homology chain with the cohomology class via the Kronecker pairing, and then multiplies the resulting scalar with the remaining degree $$q$$ homology chain. Although this definition may appear contrived at first, the uniqueness in [§Acyclic models theorem](/en/math/algebraic_topology/acyclic_models_theorem#thm3) guarantees that it is the only definition that behaves coherently. Moreover, from this description one recognizes that the cap product is precisely the operation corresponding to the interior product.

The following then holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6 (Projection formula)**</ins> For a continuous map $$f:X \rightarrow Y$$, and for $$\alpha\in H^p(X)$$, $$\beta\in H^q(Y)$$, and $$\sigma\in H_{p+q}(X)$$, we have

$$f_\ast(f^\ast\beta\frown\sigma)=\beta\frown f_\ast\sigma$$

</div>

--- 

**References**

[Hat] A. Hatcher, *Algebraic Topology*. Cambridge University Press, 2022.

---
