---
title: "Group Homomorphisms"
description: "This post covers group homomorphisms and their theorems. We prove the first and second isomorphism theorems, and examine the properties of normal subgroups and quotient groups."
excerpt: "Homomorphism theorems"

categories: [Math / Algebraic Structures]
permalink: /en/math/algebraic_structures/isomorphism_theorems
sidebar: 
    nav: "algebraic_structures-en"

date: 2022-11-30
weight: 6
translated_at: 2026-08-16T11:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-16T11:15:04+00:00
---
We begin with an easy lemma.

::: Lemma 1
For any homomorphism $f:G\rightarrow G'$, the kernel $\ker f$ is a normal subgroup of $G$.
:::
::: Proof
For any $g\in G$ and $x\in \ker f$, we have

$$f(gxg^{-1})=f(g)f(x)f(g^{-1})=f(g)e'f(g)^{-1}=f(g)f(g)^{-1}=e'.$$
:::

Now consider the equivalence relation defined by $\ker f$:

$$x\sim y\iff xy^{-1}\in\ker f$$

From the identity

$$f(y)=e'f(y)=f(xy^{-1})f(y)=f(xy^{-1}y)=f(x)$$

we see that $x\sim y\iff f(x)=f(y)$. That is, $\sim$ is nothing other than the equivalence relation induced by the function $f$ ([[Set Theory] §Examples of Equivalence Relations, ⁋Definition 2](/en/math/set_theory/examples_of_equivalence#def2)), and by the definition of a quotient group the canonical map $p:G\rightarrow G/\ker f$ is a homomorphism. Considering the canonical decomposition of $f$, we obtain a bijection $h:G/\ker f\rightarrow\im f$. Then for any $[x], [x']\in G/\ker f$,

$$h([x][x'])=h([xx'])=f(xx')=f(x)f(x')=h([x])h([x'])$$

so $h$ is a homomorphism, and therefore an isomorphism.

::: Theorem 2 (The first isomorphism theorem)
For any homomorphism $f:G\rightarrow G'$, we always have $G/\ker f\cong \im f$.
:::

On the other hand, using [[Set Theory] §Examples of Equivalence Relations, ⁋Proposition 7](/en/math/set_theory/examples_of_equivalence#prop7) we obtain the following proposition.

::: Proposition 3
For any homomorphism $f:G\rightarrow G'$ and any normal subgroup $N$ of $G$, there exists $\bar{f}:G/N\rightarrow G'$ satisfying $f=\bar{f}\circ p$ if and only if $N\leq \ker f$. In this case, since $p$ is surjective, $\bar{f}$ is uniquely determined.
:::

## The second isomorphism theorem

To prove the second isomorphism theorem, we need the following lemma. In the next proposition, $N\vee K$ denotes the smallest subgroup of $G$ containing the union $N\cup K$, that is, $\langle N\cup K\rangle$, and $NK$ denotes the set

$$NK=\{nk\mid n\in N,k\in K\}.$$

::: Lemma 4
Let $K$ be a subgroup of a group $G$ and let $N$ be a normal subgroup of $G$. Then the following hold.

1. $N\cap K$ is a normal subgroup of $K$.
2. $N$ is a normal subgroup of $N\vee K$.
3. $NK=N\vee K=KN$.
:::
::: Proof
1. For any $n\in N\cap K$ and $k\in K$, the element $knk^{-1}$ is a product of elements of $K$, hence lies in $K$, and at the same time, since $N$ is a normal subgroup of $G$, it also lies in $N$. Therefore $knk^{-1}\in N\cap K$.
2. That $N$ is a subgroup of $N\vee K$ is obvious. Moreover, for any $g\in N\vee K$ and $n\in N$, we have $gng^{-1}\in N$.
3. For any $nk\in NK$, since $n,k\in N\vee K$ we have $nk\in N\vee K$. Thus it suffices to show the reverse inclusion. Consider the subset of $G$ consisting of all products of the form $n_1k_1\cdots n_rk_r$ with $n_i\in N$ and $k_i\in K$. One easily checks that this subset is a subgroup, and since it contains both $N$ and $K$, it also contains $N\vee K$.[^1]  
Hence every element of $N\vee K$ can be written in the form $n_1k_1\cdots n_rk_r$. Now since $N$ is a normal subgroup of $N\vee K$, for $k_1n_2$ there exists $n_2'\in N$ such that $k_1n_2=n_2'k_1$. Repeating this process, we can rewrite $n_1k_1\cdots n_rk_r$ in the form of an element of $NK$.
:::

::: Theorem 5 (The second isomorphism theorem)
Let $K$ be a subgroup of a group $G$ and let $N$ be a normal subgroup of $G$. Then $K/(N\cap K)\cong NK/N$.
:::
::: Proof
First, from the preceding lemma, $N$ is a normal subgroup of $NK=N\vee K=KN$. On the other hand, since $K\subseteq NK$, we may consider the composition of homomorphisms

$$K\overset{\iota}{\hookrightarrow}NK\overset{\pi}{\twoheadrightarrow}NK/N.$$ 

Then

$$\ker(\pi\iota)=(\pi\iota)^{-1}(e)=\iota^{-1}(\ker\pi)=\iota^{-1}(N)=K\cap N$$

so applying the first isomorphism theorem to $\pi\iota$ yields

$$K/\ker(\pi\iota)=K/(K\cap N)\cong\im(\pi\iota).$$

But every element of $NK/N$ is of the form $nkN$, and since there exists some $n'\in N$ such that $nk=kn'$, every element $nkN$ of $NK/N$ satisfies

$$nkN=kn'N=kN=\pi(k)=\pi(\iota(k))\in\im(\pi\iota)$$

which gives the desired result.
:::

## The third isomorphism theorem

::: Theorem 6 (The third isomorphism theorem)
Let $H$ and $K$ be normal subgroups of a group $G$ with $K\leq H$. Then $H/K$ is a normal subgroup of $G/K$ and $(G/K)/(H/K)\cong G/H$.  
:::
::: Proof
The decomposition following [[Set Theory] §Examples of Equivalence Relations, ⁋Definition 8](/en/math/set_theory/examples_of_equivalence#def8).
:::

## The fourth isomorphism theorem

The following theorem is one of the most useful forms: given a group $G$ and a normal subgroup $N$ of $G$, it shows that the function taking a subgroup $H$ of $G$ containing $N$ to the subgroup $H/N$ of $G/N$, and conversely the function taking a subgroup $\overline{H}$ of $G/N$ to $p^{-1}(\overline{H})$, are inverses of each other. The proof itself is a single line, but the point is that this bijection preserves intersections, indices, normality, and so on; the proofs of these facts must each be given separately. These proofs are purely technical, so we omit them.

::: Theorem 7 (The fourth isomorphism theorem)
Let $G$ be a group and let $N$ be a normal subgroup of $G$. Then there exists an inclusion-preserving bijection between the set of subgroups of $G$ containing $N$ and the set of subgroups of $G/N$. Moreover, this bijection preserves all relations such as intersection, index, and normal subgroup.
:::

## Coequalizer of group homomorphisms

Now let two group homomorphisms $f,g:G \rightarrow H$ be given. Earlier we saw that the equalizer $\Eq(f,g)$ is always a subgroup of $G$. Their coequalizer is somewhat more complicated.

First, from the universal property of the coequalizer, $q:H\rightarrow\CoEq(f,g)$ is initial among those satisfying $q\circ f=q\circ g$. If we encountered such a situation in $\Set$, we would define an equivalence relation $\sim$ on $H$ by the relation generated by

$$f(x)\sim g(x)\qquad\text{for all $x\in G$}$$

and then the projection $H\rightarrow H/{\sim}$ would be the coequalizer; but in $\Grp$ we do not know whether the $\sim$ defined above is compatible with the group operation of $H$. That is, the subset

$$S=\{f(x)g(x)^{-1}\mid x\in G\}$$

is not in general a normal subgroup, so $H/S$ is not defined.

To resolve this, let $\overline{S}$ be the *normal closure* of $S$, that is, the smallest normal subgroup containing $S$. Then the quotient $H/\overline{S}$ of $H$ by $\overline{S}$ is well defined.

::: Proposition 8
The quotient $q: H \rightarrow H/\overline{S}$ defined as above is a coequalizer.
:::
::: Proof
First, for any $x\in G$ we have $f(x)g(x)^{-1}\in S\subseteq\overline{S}=\ker q$, so $q(f(x))=q(g(x))$, that is, $q\circ f=q\circ g$.

Suppose a group homomorphism $q': H \rightarrow H'$ satisfies $q'\circ f=q'\circ g$. Then by [Lemma 1](#lem1), $\ker q'$ is a normal subgroup, and from the condition $q'\circ f=q'\circ g$ we have

$$q'(f(x))=q'(g(x))\iff q'(f(x)g(x)^{-1})=e$$

so $f(x)g(x)^{-1}\in\ker q'$ holds for all $x\in G$. Therefore, by the definition of $\overline{S}$, we have $\overline{S}\leq\ker q'$, and applying [Proposition 3](#prop3) yields a homomorphism $\overline{q'}:H/\overline{S}\rightarrow H'$ satisfying $q'=\overline{q'}\circ q$. Such $\overline{q'}$ is unique because $q$ is surjective.
:::

---

**References**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---

[^1]: The reverse inclusion can also be easily verified.
