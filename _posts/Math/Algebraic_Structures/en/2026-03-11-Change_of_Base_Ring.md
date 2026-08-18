---
title: "Change of Scalars"
description: "We define two functors, restriction and extension of scalars, that change a module over one ring into a module over another ring via a ring homomorphism, and examine their properties."
excerpt: "Restriction and extension of scalars via ring homomorphism"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/change_of_base_ring
sidebar: 
    nav: "algebraic_structures-en"

date: 2024-08-12
weight: 203
translated_at: 2026-08-18T10:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-18T10:15:05+00:00
---
In this post, we examine how to turn an $A$-module into a $B$-module, or a $B$-module into an $A$-module, via a ring homomorphism $\phi:A \rightarrow B$. Because abbreviating scalar multiplication and operations as before could cause confusion, we agree to keep omitting $\cdot$ for multiplication maps, while denoting actions by $\cdot$ (or $\cdot_A$ and $\cdot_B$).

## Restriction of scalar

Let a $B$-module $\rho_N:B\otimes N \rightarrow N$ be given. Then, considering the following composition

{% diagram Math/Algebraic_Structures/Change_of_Base_Ring-1.svg width="14.53em" alt="restriction_of_scalars" %}

we see that $\phi^\ast\rho_N:A\otimes N \rightarrow N$ satisfies all the conditions required of an action, and therefore defines an $A$-module structure on $N$. Moreover, considering the following diagram

{% diagram Math/Algebraic_Structures/Change_of_Base_Ring-2.svg width="16.59em" alt="restriction_of_scalars_functoriality" %}

we see that this assignment of $A$-modules is functorial.

::: Definition 1
For a ring homomorphism $\phi:A \rightarrow B$, the functor defined in the above manner is denoted $\phi^\ast: \lMod{B} \rightarrow \lMod{A}$ and is called the *restriction of scalar*.
:::

In other words, given an arbitrary $B$-module $\rho_N: B\otimes N \rightarrow N$, we use it to define an action of $A$ on $N$ by the formula

$$\alpha\cdot_A y:=\phi(\alpha)\cdot_B y$$

The same construction applies verbatim to right modules, and in this case we also regard $\phi^\ast$ as a functor $\rMod{B} \rightarrow\rMod{A}$.

Let us consider the special case $N=B$. Since $\phi^\ast B$ and $B$ coincide as sets, we can examine the relationship between the original ring homomorphism $\phi:A \rightarrow B$ and the action on $\phi^\ast B$; in this case, one checks that $\phi$ becomes an $A$-linear map. Also, since $B$ is simultaneously a left $B$-module and a right $B$-module over itself, $\phi^\ast B$ becomes a $(B,A)$-bimodule where $B$ acts by multiplication on the left and $A$ acts on the right via $\beta\cdot_A\alpha=\beta\phi(\alpha)$. Henceforth, when we use $\phi^\ast B$ as the left argument of a tensor product, we mean this right $A$-structure.

::: Example 2
The forgetful functor $U: \lMod{B} \rightarrow\Ab$ is induced from the (unique) ring homomorphism $\mathbb{Z}\rightarrow B$.
:::

## Extension of scalar

We now define two functors from $\lMod{A}$ to $\lMod{B}$. For convenience, fix an $A$-module $M$.

Consider the tensor product of the two $A$-modules $\phi^\ast B$ and $M$, namely $\phi^\ast B\otimes_AM$. Then we can define a $B$-action $\cdot_B$ on this by the formula

$$\beta'\cdot_B(\beta\otimes_A x)=(\beta'\beta)\otimes_A x$$

That this is indeed an action is not difficult to verify by direct computation, or alternatively one may view it as arising from the composition

$$B\otimes_\mathbb{Z}(\phi^\ast B\otimes_AM)\cong (B\otimes_\mathbb{Z}\phi^\ast B)\otimes_AM \overset{\mu_B\otimes_A\id_M}{\longrightarrow} \phi^\ast B\otimes_AM$$[^1]

Also, for any $A$-linear map $u:M \rightarrow M'$, one checks that $\id_{\phi^\ast B}\otimes_A u$ defines a $B$-linear map between the two $B$-modules constructed in this way.

::: Definition 3
We write the above functor $\phi^\ast B\otimes_A-:\lMod{A} \rightarrow \lMod{B}$ simply as $\phi_!$, and call it the *extension of scalar*.
:::

## Coextension of scalar

As before, fix an $A$-module $M$. This time, we consider homomorphisms between the two $A$-modules $\phi^\ast B$ and $M$. We define a $B$-module structure on the abelian group

$$\Hom_A(\phi^\ast B,M)$$

by

$$\beta\cdot g: (\beta'\mapsto g(\beta'\beta))$$

For arbitrary $\alpha\in A$ and $\beta'\in \phi^\ast B$, we have

$$(\beta\cdot g)(\alpha\cdot \beta')=g(\phi(\alpha)\beta'\beta)=g(\alpha\cdot(\beta'\beta))=\alpha\cdot g(\beta'\beta)=\alpha\cdot (\beta\cdot g)(\beta')$$

so $\beta\cdot g$ is also an $A$-linear map. A short computation shows that this is again functorial, and thus the following is defined.

::: Definition 4
The functor $\Hom_A(\phi^\ast B,-): \lMod{A} \rightarrow \lMod{B}$ is called the *coextension of scalar* and is written $\phi_\ast$.
:::

## Adjoint functors

The three functors defined above satisfy certain adjoint relationships. ([\[Category Theory\] §Adjoint Functors, ⁋Definition 1](/en/math/category_theory/adjoints#def1)) We first prove the following lemma.

::: Lemma 5
For a right $B$-module $N_1$ and a left $B$-module $N_2$, consider the two abelian groups $\phi^\ast N_1\otimes_A \phi^\ast N_2$ and $N_1\otimes_B N_2$. Then there exists a unique homomorphism $\Phi:\phi^\ast N_1\otimes_A \phi^\ast N_2 \rightarrow N_1\otimes_BN_2$ sending any $y_1\otimes_A y_2\in \phi^\ast N_1\otimes_A\phi^\ast N_2$ to $y_1\otimes_B y_2\in N_1\otimes_BN_2$.

If both $A$ and $B$ are commutative rings, then $\Phi$ is an $A$-linear map $\phi^\ast N_1\otimes_A\phi^\ast N_2 \rightarrow\phi^\ast(N_1\otimes_BN_2)$.
:::
::: Proof
Define a map $\phi^\ast N_1\times\phi^\ast N_2 \rightarrow N_1\otimes_B N_2$ by $(y_1,y_2)\mapsto y_1\otimes_B y_2$, and then show that this behaves well with respect to scalar multiplication by $A$. Since the $A$-scalar multiplication on $\phi^\ast N_1,\phi^\ast N_2$ is defined via $B$-action through $\phi(\alpha)$, for any $\alpha\in A$ we have

$$(\alpha\cdot_A y_1,y_2)=(\phi(\alpha)\cdot_B y_1, y_2)\mapsto (\phi(\alpha)\cdot_B y_1)\otimes_B y_2=y_1\otimes_B(\phi(\alpha)\cdot_B y_2)$$

and thus $(\alpha\cdot_A y_1,y_2)$ and $(y_1,\alpha\cdot_Ay_2)$ are sent to the same element, so the proof is completed by the universal property of the tensor product.
:::

The following propositions can be proved in the general case as well, but for convenience we assume that $A$ and $B$ are both commutative rings.

::: Proposition 6
The adjunction $\phi_!\dashv\phi^\ast$ exists.
:::
::: Proof
Fix an arbitrary $A$-module $M$ and a $B$-module $N$. First, for any $v\in\Hom_B(\phi_!M,N)$, we obtain a map $M \rightarrow N$ via the composition of functions

{% diagram Math/Algebraic_Structures/Change_of_Base_Ring-3.svg width="22.24em" alt="Adjointness-1" %}

Here $M \rightarrow A\otimes_AM \rightarrow \phi^\ast B\otimes_AM$ is a composition of $A$-linear maps, and $v:\phi^\ast B\otimes_A M \rightarrow N$ is a $B$-linear map. Looking at the composition of the former $A$-linear maps for arbitrary $\alpha\in A$ and $x\in M$, we have

$$\alpha\cdot_Ax\mapsto \alpha\otimes_A x\mapsto \phi(\alpha)\otimes_A x$$

and for the $B$-linear map $v$, using

$$\phi(\alpha)\otimes_A x=(\phi(\alpha)1)\otimes_A x=\phi(\alpha)\cdot_B(1\otimes_A x)$$

we obtain

$$v(\phi(\alpha)\otimes_A x)=v(\phi(\alpha)\cdot_B(1\otimes_A x))=\phi(\alpha)\cdot_B v(1\otimes_A x)$$

That is, viewing $N$ as an $A$-module via restriction of scalar, the above composition is an $A$-linear map.

Conversely, suppose an arbitrary $u\in\Hom_A(M, \phi^\ast N)$ is given. Then this time we obtain a map $\phi_!M \rightarrow N$ via the following composition

{% diagram Math/Algebraic_Structures/Change_of_Base_Ring-4.svg width="30.40em" alt="Adjointness-2" %}

Then for arbitrary $\beta'\in B$ and $\beta\otimes_A x\in \phi^\ast B\otimes_AM$, we have

$$\Phi((\id_{\phi^\ast B}\otimes_A u)(\beta'\cdot_B(\beta\otimes_Ax)))=\Phi((\beta'\beta)\otimes_Au(x))=(\beta'\beta)\otimes_B u(x)$$

and via $B\otimes_BN\cong N$ this is sent to $(\beta'\beta)\cdot_Bu(x)=\beta'\cdot_B(\beta\cdot_Bu(x))$. Thus the map defined above is $B$-linear.

Now one checks that the two maps defined above are inverses of each other, and moreover that they define a natural equivalence.
:::

The following adjoint pair also holds.

::: Proposition 7
The adjunction $\phi^\ast\dashv\phi_\ast$ exists.
:::
::: Proof
Fix a $B$-module $N$ and an $A$-module $M$; it suffices to show $\Hom_A(\phi^\ast N,M)\cong\Hom_B(N,\phi_\ast M)$. For any $u\in\Hom_A(\phi^\ast N,M)$, define $\tilde{u}(y)$ by $\beta\mapsto u(\beta\cdot_By)$. Then

$$\tilde{u}(y)(\alpha\cdot_A\beta)=u\bigl((\phi(\alpha)\beta)\cdot_By\bigr)=u\bigl(\alpha\cdot_A(\beta\cdot_By)\bigr)=\alpha\cdot_A\tilde{u}(y)(\beta)$$

so $\tilde{u}(y)\in\phi_\ast M$, and since $\tilde{u}(\beta'\cdot_By)(\beta)=u((\beta\beta')\cdot_By)=\tilde{u}(y)(\beta\beta')$ equals $(\beta'\cdot_B\tilde{u}(y))(\beta)$ by the $B$-action defined just before [Definition 4](#def4), we have $\tilde{u}\in\Hom_B(N,\phi_\ast M)$.

Conversely, for any $w\in\Hom_B(N,\phi_\ast M)$, setting $u(y)=w(y)(1)$ gives

$$u(\alpha\cdot_Ay)=w(\phi(\alpha)\cdot_By)(1)=w(y)(\phi(\alpha))=w(y)(\alpha\cdot_A1)=\alpha\cdot_Au(y)$$

so $u\in\Hom_A(\phi^\ast N,M)$. These two correspondences are inverses of each other, because $\tilde{u}(y)(1)=u(1\cdot_By)=u(y)$, and conversely for the $u$ obtained from $w$, we have $\tilde{u}(y)(\beta)=w(\beta\cdot_By)(1)=w(y)(\beta)$. Finally, since both correspondences are given solely by composition with $u$ and $w$, they are natural in both $M$ and $N$.
:::

Therefore $\phi^\ast:\lMod{B} \rightarrow\lMod{A}$ is both a left adjoint and a right adjoint, and hence commutes with all kinds of limits and colimits.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.

---

[^1]: Strictly speaking, to make the first isomorphism in this formula work, one must use the fact that $$B$$ is a $(\mathbb{Z},A)$-bimodule.
