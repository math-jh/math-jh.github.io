---
title: "Group Extensions"
description: "Group extensions classify the extension structures between two given groups, and cover the equivalence conditions for trivial extensions and the morphisms between extensions."
excerpt: "Group extensions as short exact sequences, and semidirect products"

categories: [Math / Group Theory]
permalink: /en/math/group_theory/extensions
sidebar: 
    nav: "group_theory-en"

date: 2025-03-29
weight: 2
translated_at: 2026-05-31T09:00:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T09:00:05+00:00
---
In this post we discuss extensions of groups.

## Group Extensions

::: Definition 1
For two groups $G, F$, an *extension* $\mathcal{E}$ of $G$ by $F$ is a pair

$$\mathcal{E}: F\overset{i}{\hookrightarrow}E\overset{p}{\twoheadrightarrow}G$$

satisfying the condition $\ker p=\im i$.
:::

The intuition is provided by the pair

$$\mathcal{E}_0: F \rightarrow F\oplus G \rightarrow G$$

which we call the *trivial extension*. However, although the first isomorphism theorem gives

$$G\cong E/\ker p=E/\im i$$

in general one must be careful that this does not imply

$$E\cong (E/i(F))\oplus i(F).$$

In any case, from this computation we see that $E$ being an extension of $G$ by $F$ is equivalent to the existence of a suitable normal subgroup $F'$ of $E$ such that $F'$ is isomorphic to $F$ and $E/F'$ is isomorphic to $G$.

Now, for fixed $G$ and $F$, the collection of all extensions of $G$ by $F$ forms a category. Its morphisms are given as follows.

::: Definition 2
For two extensions $\mathcal{E}_1: F \rightarrow E_1 \rightarrow G$ and $\mathcal{E}_2:F \rightarrow E_2 \rightarrow G$, a *morphism* from $\mathcal{E}_1$ to $\mathcal{E}_2$ is a map $u:E_1 \rightarrow E_2$ making the following diagram commute:

![morphism_of_extensions](/assets/images/Math/Group_Theory/Extensions-1.svg){:style="width:10.17em" class="invert" .align-center}
:::

Then if $u:E_1 \rightarrow E_2$ is an isomorphism of groups, its inverse $u^{-1}: E_2 \rightarrow E_1$ also satisfies the condition of [Definition 2](#def2), and hence $u$ is an isomorphism of extensions.

Extending the previous definition, we give the following.

::: Definition 3
If an extension $\mathcal{E}:F \rightarrow E \rightarrow G$ of $G$ by $F$ is isomorphic to the extension

$$\mathcal{E}_0:F \rightarrow F\oplus G \rightarrow G$$

then we call it the *trivial extension*.
:::

Then the following holds.

::: Proposition 4
For an extension $\mathcal{E}:F \rightarrow E \rightarrow G$, the following are all equivalent.

1. $\mathcal{E}$ is a trivial extension.
2. A retraction $r: E \rightarrow F$ exists.
3. A section $s: G \rightarrow E$ exists such that $s(G)$ can be chosen to lie in the centralizer of $i(F)$.
:::

Of course, here retraction and section mean group homomorphisms, not merely functions. ([\[Set Theory\] §Retraction and Section, ⁋Definition 2](/en/math/set_theory/retraction_and_section#def2))

::: Proof (Proposition 4)
First, assume the first condition and consider the following diagram:

![retraction_and_section](/assets/images/Math/Group_Theory/Extensions-2.svg){:style="width:11.92em" class="invert" .align-center}

Then we define the retraction $r:E \rightarrow F$ as $\pr_1\circ u$, and $s:G \rightarrow E$ as $u^{-1}\circ\iota_2$.

Conversely, assume that the second condition holds. Then $(r,p): E \rightarrow F\oplus G$ is an isomorphism between the given extension and $F \rightarrow F\oplus G \rightarrow G$. Similarly, assume the third condition. Then since $s(G)$ is contained in the centralizer of $i(F)$, we can construct a morphism from $F\oplus G$ to $E$ by taking the weak direct product of $F$ and $G$.
:::

If $i(F)$ is contained in the center $Z(E)$ of $E$, then in the third condition we may ignore the relationship between $s(G)$ and $i(F)$. ([\[Algebraic Structures\] §Group Actions, ⁋Definition 12](/en/math/algebraic_structures/group_actions#def12))

::: Definition 5
An extension $\mathcal{E}:F \rightarrow E \rightarrow G$ is called a *central extension* if the image of $F$ in $E$ is contained in the center of $E$.
:::

## Semidirect Products of Groups

On the other hand, the reason nontrivial extensions exist is that, as we saw above, for any normal subgroup $N$ of a group $G$, the formula

$$G\cong (G/N)\oplus N$$

does not always hold. However, the converse is not always true either.

::: Definition 6
Let two groups $N,H$ and a group homomorphism $\tau:H \rightarrow \Aut(N)$ be given. Then the *semi-direct product* $N\rtimes_\tau H$ of $N$ and $H$ with respect to $\tau$ is the group given by the set $N\times H$ with the following operation:

$$(x_1,y_1)(x_2,y_2)=(x_1\tau(y_1)(x_2), y_1y_2)$$
:::

Then one can show that $N\rtimes_\tau H$ has a group structure under the above operation; in this case the identity element of $N\rtimes_\tau H$ is $(e_N, e_H)$ and the inverse of $(x,y)$ is $(\tau(y^{-1})(x^{-1}), y^{-1})$. Moreover, the following holds.

::: Proposition 7
Define two maps $i: N \rightarrow N\rtimes_\tau H$ and $p: N\rtimes_\tau H\rightarrow H$ by the formulas

$$i(x)=(x, e_H),\qquad p(x,y)=y$$

Then these maps are group homomorphisms, and the sequence

$$\mathcal{E}_\tau: N \overset{i}{\rightarrow} N\rtimes_\tau H\overset{p}{\rightarrow} H$$

obtained from them is an extension of $H$ by $N$. Moreover, if we define a map $s: H \rightarrow N\rtimes_\tau H$ by the formula

$$s(y)=(e_N, y)$$

then $s$ is a section of $p$, and since it is contained in the centralizer of $N\rtimes_\tau H$, by [Proposition 4](#prop4) the extension $\mathcal{E}_\tau$ is trivial.
:::

The proof of this is a straightforward computation.

Now suppose the $N,H$ examined above are subgroups of a specific group $G$. If $N$ is a *normal* subgroup of $G$, then for each $h\in H$ the inner automorphism $\rho_h$ is an automorphism of $N$, and thus $\rho: H \rightarrow \Aut(N)$ is defined. ([\[Algebraic Structures\] §Group Actions, ⁋Definition 10](/en/math/algebraic_structures/group_actions#def10)) Then from the above proposition we obtain the following.

::: Corollary 8
Let $G$ be a group, and let $N$ be a normal subgroup of $G$ and $H$ a subgroup of $G$. If $N\cap H=\{e_G\}$ and $NH=G$, then the group homomorphism defined by the formula

$$N\rtimes_\rho H \rightarrow G;\qquad (x,y)\mapsto xy$$

is an isomorphism.
:::
::: Proof
It suffices to construct an inverse. To do this, using the condition $NH=G$ we need to find suitable $x\in N$ and $y\in H$ satisfying $g=xy$ for an arbitrary element $g$ of $G$; this is generally impossible, but is possible because $N$ is a *normal* subgroup of $G$. The rest is a straightforward computation.
:::

In this case we say that $G$ is the (internal) semi-direct product of $N$ and $H$. The difference between the external semi-direct product and the internal semi-direct product is merely where we started from, and is not important.

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---
