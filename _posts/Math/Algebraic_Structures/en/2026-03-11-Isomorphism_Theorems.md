---
title: "Group Isomorphisms"
description: "This post covers group isomorphisms and their theorems. We prove the first and second isomorphism theorems, and examine the properties of normal subgroups and quotient groups."
excerpt: "Isomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/isomorphism_theorems
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-11-30
weight: 6
translated_at: 2026-08-16T11:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-05T15:15:05+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## The first isomorphism theorem

We begin with an easy lemma.

::: Lemma 1
For any homomorphism $f:G\rightarrow G'$, $\ker f$ is a normal subgroup of $G$.
:::
::: Proof
For any $g\in G$ and $x\in \ker f$,

$$f(gxg^{-1})=f(g)f(x)f(g^{-1})=f(g)e'f(g)^{-1}=f(g)f(g)^{-1}=e'.$$
:::

Now, considering the equivalence relation defined by $\ker f$,

$$x\sim y\iff xy^{-1}\in\ker f$$

we see from the following equation

$$f(y)=e'f(y)=f(xy^{-1})f(y)=f(xy^{-1}y)=f(x)$$

that $x\sim y\iff f(x)=f(y)$. That is, $\sim$ is nothing other than the equivalence relation defined by the function $f$ ([[Set Theory] §Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2)), and from the definition of a quotient group, the canonical map $p:G\rightarrow G/\ker f$ is a homomorphism. Now, considering the canonical decomposition of $f$, we obtain a bijection $h:G/\ker f\rightarrow\im f$. Then for any $[x], [x']\in G/\ker f$, since

$$h([x][x'])=h([xx'])=f(xx')=f(x)f(x')=h([x])h([x'])$$

$h$ is a homomorphism, and therefore an isomorphism. 

::: Theorem 2 (The first isomorphism theorem)
For any homomorphism $f:G\rightarrow G'$, $G/\ker f\cong \im f$ always holds.
:::

On the other hand, using [[Set Theory] §Examples of Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/examples_of_equivalence#prop7), we obtain the following proposition. 

::: Proposition 3
For any homomorphism $f:G\rightarrow G'$ and any normal subgroup of $G$, $N$, there exists, satisfying $f=\bar{f}\circ p$, a map $\bar{f}:G/N\rightarrow G'$ if and only if $N\leq \ker f$. In this case, since $p$ is surjective, $\bar{f}$ is uniquely determined. 
:::

## The second isomorphism theorem

To prove the second isomorphism theorem, we must show the following lemma. In the following proposition, $N\vee K$ denotes the smallest subgroup containing the union $N\cup K$ in $G$, that is, $\langle N\cup K\rangle$, and $NK$ denotes the set

$$NK=\{nk\mid n\in N,k\in K\}$$

::: Lemma 4
Let a group $G$, a subgroup $K$, and a normal subgroup $N$ be given. Then the following hold.

1. $N\cap K$ is a normal subgroup of $K$.
2. $N$ is a normal subgroup of $N\vee K$.
3. $NK=N\vee K=KN$ holds.
:::
::: Proof
1. For any $n\in N\cap K$ and $k\in K$, since $knk^{-1}$ is a product of elements of $K$, it is an element of $K$, and at the same time, since $N$ is a normal subgroup of $G$, it is an element of $N$. Therefore, $knk^{-1}\in N\cap K$.
2. It is clear that $N$ is a subgroup of $N\vee K$. Moreover, for any $g\in N\vee K$ and $n\in N$, we have $gng^{-1}\in N$.
3. For any $nk\in NK$, since $n,k\in N\vee K$, we have $nk\in N\vee K$. Thus it suffices to show only the reverse direction. Consider, for elements of $N$ and $K$, the subset containing all products $n_1k_1\cdots n_rk_r$ in $G$. One can easily verify that this set is a subgroup, and since this subgroup contains both $N$ and $K$, it also contains $N\vee K$.[^1]  
Therefore, every element of $N\vee K$ can be written in the form $n_1k_1\cdots n_rk_r$. Now since $N$ is a normal subgroup of $N\vee K$, we have $k_1n_2=n_2'k_1$ for some $n_2'\in N$. By repeating this process, we can rewrite $n_1k_1\cdots n_rk_r$ in the form of an element of $NK$.
:::

::: Theorem 5 (The second isomorphism theorem)
Let a group $G$, a subgroup $K$, and a normal subgroup $N$ be given. Then $K/(N\cap K)\cong NK/N$ holds.
:::
::: Proof
First, from the preceding lemma, $N$ is a normal subgroup of $NK=N\vee K=KN$. Meanwhile, since $K\subseteq NK$, we can consider the composition of homomorphisms

$$K\overset{\iota}{\hookrightarrow}NK\overset{\pi}{\twoheadrightarrow}NK/N$$ 

Then, since

$$\ker(\pi\iota)=(\pi\iota)^{-1}(e)=\iota^{-1}(\ker\pi)=\iota^{-1}(N)=K\cap N$$

applying the first isomorphism theorem to $\pi\iota$ yields

$$K/\ker(\pi\iota)=K/(K\cap N)\cong\im(\pi\iota)$$

However, every element of $NK/N$ is of the form $nkN$, and since there exists some $n'\in N$ such that $nk=kn'$, any element $nkN$ of $NK/N$ satisfies

$$nkN=kn'N=kN=\pi(k)=\pi(\iota(k))\in\im(\pi\iota)$$

which yields the desired result.
:::

## The third isomorphism theorem

::: Theorem 6 (The third isomorphism theorem)
Let $H$ and $K$ be normal subgroups of a group $G$, and let $K\leq H$. Then $H/K$ is a normal subgroup of $G/K$ and $(G/K)/(H/K)\cong G/H$ holds.  
:::
::: Proof
The decomposition following [[Set Theory] §Examples of Equivalence Relations, ⁋Definition 8](/en/math/set_theory/examples_of_equivalence#def8).
:::

## The fourth isomorphism theorem

The following theorem is one of the most useful forms: given a group $G$ and a normal subgroup of $G$, $N$, it shows that the function taking a subgroup containing $N$ in $G$, $H$, to the subgroup of $G/N$, $H/N$, and conversely the function taking a subgroup of $G/N$, $\overline{H}$, to $p^{-1}(\overline{H})$, are inverses of each other. The proof itself is a single line, but the point is that this bijection preserves intersections, indices, normality, and so on between subgroups; the proofs of these facts must each be given separately. Since these proofs are purely technical, we omit them.

::: Theorem 7 (The fourth isomorphism theorem)
Let $G$ be a group and let $N$ be a normal subgroup of $G$. Then there exists an inclusion-preserving bijection between *the set of subgroups containing $N$ in $G$* and *the set of subgroups of $G/N$*. Moreover, this bijection preserves all relations such as intersections, indices, and normal subgroups.
:::

## Coequalizer of homomorphisms

Now let two group homomorphisms $f,g:G \rightarrow H$ be given. Earlier we saw that the equalizer of $f,g$, $\Eq(f,g)$, is always a subgroup of $G$. Their coequalizer is somewhat more complicated.

First, considering the universal property of the coequalizer, $q:H\rightarrow\CoEq(f,g)$ is initial among those satisfying $q\circ f=q\circ g$. If we encountered such a situation in $\Set$, then endowing $H$ with the equivalence relation $\sim$ generated by

$$f(x)\sim g(x)\qquad\text{for all $x\in G$}$$

and considering the projection $H\rightarrow H/{\sim}$, this would be the coequalizer; but in $\Grp$, we do not know whether the $\sim$ defined above is compatible with the group operation of $H$. That is, the following subset

$$S=\{f(x)g(x)^{-1}\mid x\in G\}$$

is not in general a normal subgroup, so $H/S$ is not defined.

To resolve this, let $\overline{S}$ be the *normal closure* of $S$, that is, the smallest normal subgroup containing $S$. Then the quotient by $\overline{S}$ of $H$, $H/\overline{S}$, is well-defined.

::: Proposition 8
The quotient $q: H \rightarrow H/\overline{S}$ defined as above is a coequalizer.
:::
::: Proof
First, for any $x\in G$, since $f(x)g(x)^{-1}\in S\subseteq\overline{S}=\ker q$, we have $q(f(x))=q(g(x))$, that is, $q\circ f=q\circ g$ holds.

Suppose there exists a group homomorphism $q': H \rightarrow H'$ satisfying $q'\circ f=q'\circ g$. Then by [Lemma 1](#lem1), $\ker q'$ is a normal subgroup, and by the condition $q'\circ f=q'\circ g$, since

$$q'(f(x))=q'(g(x))\iff q'(f(x)g(x)^{-1})=e$$

we have $f(x)g(x)^{-1}\in\ker q'$ for all $x\in G$. Therefore, by the definition of $\overline{S}$, we have $\overline{S}\leq\ker q'$, and applying [Proposition 3](#prop3), we have $q'=\overline{q'}\circ q$ for some $\overline{q'}:H/\overline{S}\rightarrow H'$. Such $\overline{q'}$ is unique because $q$ is surjective.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: One can also easily show that the reverse inclusion holds.
