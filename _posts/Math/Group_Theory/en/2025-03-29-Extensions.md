---
title: "Group Extensions"
description: "Group extensions classify extension structures between two given groups, and cover equivalence conditions for trivial extensions and morphisms between extensions."
excerpt: "Group extensions as short exact sequences and semidirect products"

categories: [Math / Group Theory]
permalink: /en/math/group_theory/extensions
sidebar: 
    nav: "group_theory-en"

date: 2025-03-29
weight: 2
translated_at: 2026-05-31T09:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-10T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
In this post we discuss extensions of groups.

## Group Extensions

::: Definition 1
For two groups $G, F$, an *extension* of $G$ by $F$, $\mathcal{E}$, means the following pair satisfying the condition $\ker p=\im i$:

$$\mathcal{E}: F\overset{i}{\hookrightarrow}E\overset{p}{\twoheadrightarrow}G$$
:::

The intuition for this is the following pair

$$\mathcal{E}_0: F \rightarrow F\oplus G \rightarrow G$$

which we call the *trivial extension*. However, in the above situation, while the relation

$$G\cong E/\ker p=E/\im i$$

holds in general by the first isomorphism theorem, one must be careful because this does not imply that

$$E\cong (E/i(F))\oplus i(F)$$

holds. In any case, from this computation we see that for $E$ to be an extension of $G$ by $F$, it is equivalent that $E$ has a suitable normal subgroup $F'$ such that $F'$ is isomorphic to $F$ and $E/F'$ is isomorphic to $G$.

Now, for fixed $G$ and $F$, the collection of all extensions of $G$ by $F$ forms a category. Morphisms here are given as follows.

::: Definition 2
For two extensions $\mathcal{E}_1: F \rightarrow E_1 \rightarrow G$ and $\mathcal{E}_2:F \rightarrow E_2 \rightarrow G$, a *morphism* from $\mathcal{E}_1$ to $\mathcal{E}_2$ means $u:E_1 \rightarrow E_2$ making the following diagram

{% diagram Math/Group_Theory/Extensions-1.svg width="10.17em" alt="morphism_of_extensions" %}

commute.
:::

Then if $u:E_1 \rightarrow E_2$ is an isomorphism as a group homomorphism, the inverse of $u$, $u^{-1}: E_2 \rightarrow E_1$, also satisfies the condition of [Definition 2](#def2){: data-lid="72k99" }, and therefore we can verify that $u$ is an isomorphism as a morphism between extensions.

Extending the previous definition, we define the following.

::: Definition 3
If an extension of $G$ by $F$, $\mathcal{E}:F \rightarrow E \rightarrow G$, is isomorphic to the extension

$$\mathcal{E}_0:F \rightarrow F\oplus G \rightarrow G$$

then we call it a *trivial extension*.
:::

Then the following holds.

::: Proposition 4
For an extension $\mathcal{E}:F \rightarrow E \rightarrow G$, the following are all equivalent.

1. $\mathcal{E}$ is a trivial extension.
2. A retraction $r: E \rightarrow F$ exists.
3. A section $s: G \rightarrow E$ exists such that $s(G)$ can be chosen to lie in the centralizer of $i(F)$.
:::

Of course, here retraction and section mean group homomorphisms, not merely functions. ([\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2){: data-lid="2vuvt" })

::: Proof (Proposition 4)
First, assume the first condition and consider the following diagram:

{% diagram frozen/a212f2a0/Math/Group_Theory/Extensions-2.svg width="11.92em" alt="retraction_and_section" %}

Then from this, we may define the retraction $r:E \rightarrow F$ as $\pr_1\circ u$, and $s:G \rightarrow E$ as $u^{-1}\circ\iota_2$.

Conversely, assume that the second condition holds. Then $(r,p): E \rightarrow F\oplus G$ is an isomorphism between the given extension and $F \rightarrow F\oplus G \rightarrow G$. Similarly, assume the third condition. Then, since $s(G)$ is contained in the centralizer of $i(F)$, from $F\oplus G$, via the weak direct product of $F$ and $G$, we can construct a morphism to $E$.
:::

If $i(F)$ is contained in the center of $E$, $Z(E)$, then in the third condition we may ignore the relationship between $s(G)$ and $i(F)$. ([\[Algebraic Structures\] §Group Action, ⁋Definition 12](/en/math/algebraic_structures/group_actions#def12){: data-lid="ibty8" })

::: Definition 5
An extension $\mathcal{E}:F \rightarrow E \rightarrow G$ is called a *central extension* if the image of $F$ in $E$ is contained in the center of $E$.
:::

## Semidirect Products of Groups

On the other hand, the reason extensions other than the trivial extension exist is that, as seen above, for a group $G$ and any of its normal subgroups $N$, the formula

$$G\cong (G/N)\oplus N$$

does *not* always hold. However, the converse does not always hold either.

::: Definition 6
Let two groups $N,H$ and a group homomorphism $\tau:H \rightarrow \Aut(N)$ be given. Then the *semi-direct product* of $N$ and $H$ with respect to $\tau$, $N\rtimes_\tau H$, is the group given by the set $N\times H$ with the following operation:

$$(x_1,y_1)(x_2,y_2)=(x_1\tau(y_1)(x_2), y_1y_2)$$
:::

Then one can show that $N\rtimes_\tau H$ has a group structure under the above operation; in this case the identity element of $N\rtimes_\tau H$ is $(e_N, e_H)$ and the inverse of $(x,y)$ is $(\tau(y^{-1})(x^{-1}), y^{-1})$. Moreover, the following holds.

::: Proposition 7
Define two maps $i: N \rightarrow N\rtimes_\tau H$ and $p: N\rtimes_\tau H\rightarrow H$ by the formulas

$$i(x)=(x, e_H),\qquad p(x,y)=y$$

Then these maps are group homomorphisms, and

$$\mathcal{E}_\tau: N \overset{i}{\rightarrow} N\rtimes_\tau H\overset{p}{\rightarrow} H$$

obtained from them is an extension of $H$ by $N$. Moreover, if we define a map $s: H \rightarrow N\rtimes_\tau H$ by the formula

$$s(y)=(e_N, y)$$

then $s$ is a section of $p$, and since it is contained in the centralizer of $N\rtimes_\tau H$, by [Proposition 4](#prop4){: data-lid="2fna4" }, $\mathcal{E}_\tau$ is a trivial extension.
:::

The proof of this is a straightforward computation.

Now suppose the $N,H$ examined above are subgroups of a specific group $G$. If $N$ is a *normal* subgroup of $G$, then for each $h\in H$, the inner automorphism $\rho_h$ defined by it is an automorphism of $N$, and thus $\rho: H \rightarrow \Aut(N)$ is defined. ([\[Algebraic Structures\] §Group Action, ⁋Definition 10](/en/math/algebraic_structures/group_actions#def10){: data-lid="mg90k" }) Then from the above proposition we obtain the following.

::: Corollary 8
Let a group $G$, and in $G$ a normal subgroup $N$, and in $G$ a subgroup $H$ be given. If $N\cap H=\{e_G\}$ and $NH=G$ hold, then the group homomorphism defined by the formula

$$N\rtimes_\rho H \rightarrow G;\qquad (x,y)\mapsto xy$$

is an isomorphism.
:::
::: Proof
It suffices to construct an inverse. To do this, using the condition $NH=G$, for an arbitrary element of $G$, $g$, we must find, satisfying $g=xy$, suitable $x\in N$ and $y\in H$; this is generally impossible, but is possible because $N$ is a *normal* subgroup of $G$. The rest is a straightforward computation.
:::

In this case we say that $G$ is the (internal) semi-direct product of $N$ and $H$. The difference between the external semi-direct product and the internal semi-direct product is merely where we started from, and is not important.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
