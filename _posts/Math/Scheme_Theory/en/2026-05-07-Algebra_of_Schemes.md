---
title: "Algebraic Structure of Schemes"
description: "We examine the algebraic structure of schemes, defining reduced and integral schemes and proving that reducedness is a stalk-local property. We also show that an integral scheme is equivalent to an irreducible reduced scheme."
excerpt: "Definitions and properties of reduced and integral schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/algebra_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-05
weight: 7
translated_at: 2026-07-26T17:48:31+00:00
translation_source: kimi-cli
---
Since a scheme is simultaneously a geometric and an algebraic object, understanding it well requires considering not only the topological structure of schemes examined in the previous post but also the algebraic structure at the same time, and we briefly saw in the previous post how this philosophy is reflected. In this post, we develop this philosophy further.

## Reduced and Integral Schemes

::: Definition 1
A scheme $X$ is called a *reduced scheme* if for every open subset $U$, the ring $\mathcal{O}_X(U)$ is reduced. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 11](/en/math/algebraic_structures/field_of_fractions#def11)) Similarly, $X$ is called *integral* if for every nonempty open subset $U$, the ring $\mathcal{O}_X(U)$ is an integral domain. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5))
:::

Then the following holds.

::: Lemma 2
A scheme $X$ is a reduced scheme if and only if for every $x\in X$, the stalk $\mathcal{O}_{X, x}$ is a reduced ring.
:::
::: Proof
First, for any point $x\in X$ of a reduced scheme $X$, consider an affine open subscheme $U=\Spec A$ containing $x$. If $\mathfrak{p}$ is the prime ideal corresponding to $x$ in $\Spec A$, then

$$\mathcal{O}_{X,x}=(\mathcal{O}_X\vert_U)_x\cong \mathcal{O}_{\Spec A, \mathfrak{p}}\cong A_\mathfrak{p}$$

and by assumption $\mathcal{O}_X(U)\cong A$ is reduced, so $A_\mathfrak{p}$ is also reduced.

Conversely, if $\mathcal{O}_{X,x}$ is reduced for every $x\in X$, then for any open subset $U$, considering the inclusion

$$\mathcal{O}_X(U)\hookrightarrow\prod_{x\in U} \mathcal{O}_{X,x}$$

we can verify that $\mathcal{O}_X(U)$ is reduced.
:::

From this we see that reducedness is a stalk-local property. ([§Topology of Schemes, ⁋Proposition 16](/en/math/scheme_theory/topology_of_schemes#prop16)) Also, since it is easy to show that if a ring $A$ is reduced then its localization is also reduced, we can show that the spectrum of a reduced ring is reduced.

Similarly, the spectrum of an integral domain is an integral scheme. This is not difficult to show directly, but in [Proposition 4](#prop4) we prove that a scheme $X$ is integral if and only if $X$ is an irreducible, reduced scheme. Then the spectrum $\Spec A$ of an integral domain $A$ is

1. a reduced scheme because $A$ is a reduced ring, and
2. irreducible because $A$ has the unique minimal prime ideal $\{0\}$.

That is, accepting this, we can see that the spectrum of an integral domain is an integral scheme.

For the proof of [Proposition 4](#prop4), it is useful to rewrite irreducibility in algebraic language as follows.

::: Lemma 3
An affine scheme $\Spec A$ is irreducible if and only if the nilradical $\mathfrak{N}(A)$ is a prime ideal.
:::
::: Proof
That $\Spec A$ is irreducible is equivalent to the condition that for any two basis elements $D(f),D(g)\neq\emptyset$, we have $D(fg)\neq\emptyset$. Now from the equivalence

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 14](/en/math/algebraic_structures/field_of_fractions#prop14)) we know that the proposition $D(f),D(g)\neq\emptyset\implies D(fg)\neq\emptyset$ is equivalent to the following proposition:

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A).$$
:::

Now we obtain the following.

::: Proposition 4
$X$ is integral if and only if $X$ is reduced and irreducible.
:::
::: Proof
First, suppose $X$ is integral. Since every integral domain is always reduced, $X$ is a reduced scheme. If $X$ were not an irreducible scheme, there would exist two disjoint nonempty open subsets $U_1,U_2\neq\emptyset$. Then for the open subset $U_1\cup U_2$,

$$\mathcal{O}_X(U_1\cup U_2)=\mathcal{O}_X(U_1)\times \mathcal{O}_X(U_2)$$

and the right-hand side is not an integral domain, which contradicts the assumption that $X$ is integral.

Conversely, suppose an irreducible reduced scheme $X$ is given, and let us show that $X$ is an integral scheme. That is, given any open subset $U$ of $X$, we must show that $\mathcal{O}_X(U)$ is an integral domain. First, let us prove the following claim.

> **Claim.** For any affine open subset $\Spec A\cong V\subseteq X$, the ring $\mathcal{O}_X(V)\cong A$ is always an integral domain.  
> **Proof.** From the assumption that $X$ is reduced, we know that $A$ must be a reduced ring. On the other hand, since $X$ is an irreducible closed subset of itself, $V$ is also irreducible and ([\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15)) therefore from [Lemma 3](#lem3) we obtain that $\mathfrak{N}(A)=0$ is a prime ideal, so $A$ is an integral domain.

Now we show that for a general open subset $U$ of $X$, $\mathcal{O}_X(U)$ is an integral domain. For this, suppose two elements $f,g\in \mathcal{O}_X(U)$ satisfy $fg=0$. Then for the two open subsets of $U$

$$D_U(f)=\{x\in U\mid f_x\not\in \mathfrak{m}_x\},\qquad D_U(g)=\{x\in U\mid g_x\not\in \mathfrak{m}_x\}$$

and their complements $Z_U(f), Z_U(g)$, we have $U=Z_U(f)\cup Z_U(g)$. Now since $X$ is irreducible, from [\[Topology\] §Dimension, ⁋Proposition 15](/en/math/topology/dimension#prop15) we know that its open subset $U$ is likewise, and therefore we must have $Z_U(f)=U$ or $Z_U(g)=U$. Without loss of generality, suppose $Z_U(f)=U$. Then for any open affine subset $V$ of $U$, defining

$$D_V(f)=\{x\in V\mid f_x\not\in \mathfrak{m}_x\}$$

in $V$, we have $D_V(f)=D_U(f)\cap V$, and for this to be empty, $f\vert_V$ must be a nilpotent element of $\mathcal{O}_X(V)$. But $\mathcal{O}_X(V)$ is an integral domain by the claim above, so from this we know that $f\vert_V=0$ must hold, and since this holds for any open affine subset $V$ of $U$, we must have $f=0$.
:::

On the other hand, looking at [§Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6), we know that the irreducibility of an arbitrary scheme $X$ cannot be determined by looking at stalks alone. For example, $Z(\x(\x-1))$ splits into two components, so points in each component do not know about points in the other component. Therefore, integrality also cannot be determined by looking at stalks alone.

However, if $X$ were a *connected* scheme, the irreducible components would necessarily meet at some point, and by looking at the stalk at this point we might be able to determine irreducibility. The following proposition is a rigorous formulation of this idea.

::: Proposition 5
A Noetherian scheme $X$ is integral if and only if $X$ is nonempty and connected and each $\mathcal{O}_{X,x}$ is an integral domain.
:::
::: Proof
First, if $X$ is integral then $X$ is irreducible and hence connected, and also since the localization of an integral domain is an integral domain, one direction is trivial.

For the opposite direction, that the scheme $X$ is reduced is trivial because every integral domain is reduced and reducedness is a stalk-local property. Therefore, using the given conditions to show that $X$ is irreducible, the rest follows trivially from [Proposition 4](#prop4).

First, since $X$ is a Noetherian scheme, there exist suitable Noetherian rings $A_1,\ldots, A_r$ such that $X=\bigcup \Spec A_i$. Also, $X$ is Noetherian as a topological space, and therefore by [\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13) it has finitely many irreducible components. Now if

$$X=\bigcup_{j=1}^s X_j\tag{$\ast$}$$

is the decomposition of $X$ into irreducible components, then for a fixed $i$, those among the sets

$$X_1\cap \Spec A_i,\quad X_2\cap \Spec A_i,\quad\ldots,\quad X_s\cap \Spec A_i$$

that are nonempty become the irreducible components of $\Spec A_i$. Now by [§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16), each of these defines a minimal prime ideal $\mathfrak{q}_j=I(X_j)$ and conversely any minimal prime ideal of $A_i$ uniquely determines an irreducible component $X_j\cap \Spec A_i$.

On the other hand, if $s=1$ then $X$ is already irreducible so there is nothing to prove. Therefore suppose $s\geq 2$ and consider the two closed sets in the irreducible decomposition ($\ast$)

$$X_1,\qquad \bigcup_{j=2}^s X_j.$$

An irreducible component is always a nonempty closed set ([\[Topology\] §Dimension, ⁋Definition 9](/en/math/topology/dimension#def9)), and the union of finitely many closed sets is again a closed set, so these are all nonempty closed sets. If these two sets do not meet, then $X$ becomes the union of two disjoint closed sets, each of which is also open, contradicting the assumption that $X$ is connected. Therefore there exist a suitable $j$ and a point $x$ such that $x\in X_1\cap X_j$. Now let $\Spec A_i$ be an affine cover of $X$ containing the point $x$, and suppose $x$ corresponds to the prime ideal $\mathfrak{p}$. That is,

$$x\in \Spec A_i\cap X_1\cap X_j=(\Spec A_i\cap X_1)\cap (\Spec A_i\cap X_j).$$

Now from the preceding argument, $\Spec A_i\cap X_1$ has generic point $\mathfrak{q}_1$, and $\Spec A_i\cap X_j$ has generic point $\mathfrak{q}_j$, and these are minimal prime ideals of $A_i$. Now consider the stalk at $x$, $\mathcal{O}_{X,x}\cong (A_i)_\mathfrak{p}$. Since $x$ belongs to both $X_1$ and $X_j$, we have $\mathfrak{q}_1,\mathfrak{q}_j\subseteq \mathfrak{p}$, and therefore by [\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8), $\mathfrak{q}_1(A_i)_\mathfrak{p}$ and $\mathfrak{q}_j(A_i)_\mathfrak{p}$ become distinct minimal prime ideals of $(A_i)_\mathfrak{p}\cong\mathcal{O}_{X,x}$. But an integral domain has a unique minimal prime ideal $(0)$, so this contradicts the assumption that $\mathcal{O}_{X,x}$ is an integral domain.
:::

The key logic in the above proof can be summarized as follows:

1. Since $X$ is connected, if we decompose $X$ into irreducible components then each irreducible component must meet another irreducible component[^1]
2. Let $x$ be a point where two irreducible components meet; then any open neighborhood of $x$ will contain the generic point of each irreducible component ([§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)),
3. Therefore these generic points survive in the stalk $\mathcal{O}_{X,x}$ at $x$, but this is impossible since $\mathcal{O}_{X,x}$ is an integral domain.

We examine this property of generic points at the end of this post.

## Normal Schemes

Similarly to integral schemes, we can define the following.

::: Definition 6
A scheme $X$ is called *normal* if for every $x\in X$, the stalk $\mathcal{O}_{X,x}$ is a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))
:::

In general, the localization of a normal domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 12](/en/math/commutative_algebra/integral_extension#prop12)) From this we know that the spectrum $\Spec A$ of a normal domain $A$ is a normal scheme.

Any integral domain is always reduced, and since reducedness can be checked on stalks by [Lemma 2](#lem2), any normal scheme is reduced. On the other hand, since being an integral scheme is not a stalk-local property, a normal scheme is not generally always an integral scheme. However, if $X$ is a connected, nonempty Noetherian scheme, then by [Proposition 5](#prop5) we know that normality implies integrality.

On the other hand, we know that a unique factorization domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 9](/en/math/commutative_algebra/integral_extension#prop9)) From this we define the following.

::: Definition 7
A scheme $X$ is called *factorial* if for every $x\in X$, the stalk $\mathcal{O}_{X,x}$ is a unique factorization domain.
:::

Therefore any factorial scheme is a normal scheme. Also, since the localization of a unique factorization domain is a unique factorization domain, the spectrum $\Spec A$ of a unique factorization domain $A$ is factorial.

## Associated Primes

By [§Spectra, ⁋Corollary 17](/en/math/scheme_theory/spectrums#cor17), we know that there is a one-to-one correspondence between the irreducible components of a scheme $X=\Spec A$ and the minimal prime ideals of the ring $A$. This was used importantly in [Proposition 5](#prop5) above.

On the other hand, algebraically, the minimal prime ideals of a Noetherian ring $A$ are always associated prime ideals. This can be verified by applying [\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) to $A$ viewed as a module over itself, since $\ann A=\{0\}$. The Noetherian hypothesis is essential; for example, $A=\mathbb{K}[\x_1,\x_2,\ldots]/(\x_1^2,\x_2^2,\ldots)$ has a unique prime ideal $\mathfrak{m}=(\x_1,\x_2,\ldots)$, but any nonzero element of $A$ uses only finitely many variables, so for an unused $\x_j$ we have $\x_jf\neq 0$ and thus $\ann(f)=\mathfrak{m}$ is impossible, hence $\Ass(A)=\emptyset$.

However, associated prime ideals contain more information than minimal primes. For a Noetherian ring $A$, by the second result of [\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), the union of the associated primes of $A$ is exactly the set of zero-divisors of $A$ together with $0$. For example, in the case of $Z(\x\y)$ seen in [§Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6), the zero-divisors $\x,\y$ were functions that become $0$ on different irreducible components respectively, and their zero-divisor relation is already completely explained by the minimal primes $(\x),(\y)$, which are the generic points of the two components. However, as we will see in [Example 11](#ex11) below, this is not always the case, and associated points capture even the locations of zero-divisors that are missed by minimal primes, that is, the generic points of irreducible components.

::: Definition 8
For a locally Noetherian scheme $X$, a point $x$ and an affine open neighborhood $U\cong \Spec A$ of $x$, we say that $x$ is an *associated point* of $X$ if the prime ideal $\mathfrak{p}_x\subseteq A$ corresponding to $x$ is an associated prime ideal of $A$.
:::

Then this definition does not depend on the choice of $U$, and moreover it can be written stalk-locally. This is because, for an affine open neighborhood $\Spec A$ containing $x$, assuming $A$ is a Noetherian ring from the condition that $X$ is a locally Noetherian scheme, we know from the third condition of [\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) that there is a one-to-one correspondence between the set of associated prime ideals of $A$ contained in $\mathfrak{p}_x$ and the associated prime ideals of $A_{\mathfrak{p}_x}$, and from this one-to-one correspondence we can rewrite [Definition 8](#def8) as

> For a locally Noetherian scheme $X$ and a point $x$, we say that $x$ is an *associated point* of $X$ if $\mathfrak{m}_x$ is an associated prime ideal of $\mathcal{O}_{X,x}$.

Now the first condition of [\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) also guarantees the finiteness of associated points when $X$ is a quasicompact locally Noetherian scheme, that is, when $X$ is a Noetherian scheme. Now since [Definition 8](#def8) is rephrased in terms of stalks alone regardless of the choice of $U$ as seen above, we can restrict our attention to the spectrum $\Spec A$ of a Noetherian ring.

::: Definition 9
Among the associated points of the spectrum $\Spec A$ of a Noetherian ring, those that do not correspond to the generic points of the irreducible components of $\Spec A$ are called *embedded points*.
:::

That is, the points corresponding to the locations of zero-divisors that are missed by the generic points of irreducible components, mentioned before introducing [Definition 8](#def8), are precisely the embedded points, and this can be checked concretely in [Example 11](#ex11). Intuitively, an embedded point is a point that already lies in another (larger) irreducible component but records that $A$ locally has additional nilpotent-directional information at that spot, so that the scheme near it actually contains more information than the reduced structure determined by that component alone.

On the other hand, the following holds by definition.

::: Proposition 10
The associated points of the spectrum $\Spec A$ of a Noetherian ring are the generic points of the irreducible components of $\supp(f)$ for suitable $f\in A$, and the converse also holds.
:::
::: Proof
First, for any $g\in A$ and prime ideal $\mathfrak{q}\in \Spec A$,

$$\mathfrak{q}\in \supp(g)\iff g_\mathfrak{q}\neq 0\text{ in $A_\mathfrak{q}$}\iff \ann(g_\mathfrak{q})\neq A_\mathfrak{q}$$

holds. Now by [\[Commutative Algebra\] §Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5),

$$\ann(g_\mathfrak{q})=\ann(g)A_\mathfrak{q}$$

so the last condition is equivalent to $\ann(g)\setminus \mathfrak{q}=\emptyset$, that is, $\mathfrak{q}\in Z(\ann(g))$. From this we know that for any $g\in A$,

$$\supp(g)=Z(\ann(g))$$

holds. Therefore there is a one-to-one correspondence between the irreducible components of $\supp(g)$ and the minimal prime ideals containing $\ann(g)$.

Now given any associated point $\mathfrak{p}$ of $\Spec A$, by definition there exists a suitable $f\in A$ such that $\mathfrak{p}=\ann(f)$. Now

$$\supp(f)=Z(\ann(f))=Z(\mathfrak{p})$$

and that $\mathfrak{p}$ is a minimal prime of $\ann(f)=\mathfrak{p}$ is trivial, so $\mathfrak{p}$ is the generic point of $\supp f$.

Conversely, suppose $\mathfrak{p}$ is the generic point of $\supp(g)$ for a suitable $g\in A$. That is, suppose $\mathfrak{p}$ is a minimal prime ideal containing $\ann(g)$. Since the kernel of the morphism $A \rightarrow Ag$, $a\mapsto ag$ is exactly $\ann(g)$, we have $Ag\cong A/\ann(g)$, and in particular $\ann(A/\ann(g))=\ann(g)$. Now applying the first result of [\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7) to the $A$-module $A/\ann(g)$, we obtain $\mathfrak{p}\in \Ass(A/\ann(g))=\Ass(Ag)$. But since $Ag$ is a submodule of $A$, by the first inclusion relation of [\[Commutative Algebra\] §Associated Primes, ⁋Lemma 5](/en/math/commutative_algebra/associated_primes#lem5) we have $\Ass(Ag)\subseteq \Ass(A)$, and therefore $\mathfrak{p}\in \Ass(A)$, that is, $\mathfrak{p}$ is an associated point of $\Spec A$.
:::

Looking at the formula

$$\supp(f)=Z(\ann(f))$$

used in the above proof, we can see that the associated point $\mathfrak{p}=\ann(f)$ exactly records the location of the zero-divisor relation that $f$ is involved in, that is, the set of elements that multiply with $f$ to give $0$. If $A$ were an integral domain, such a zero-divisor relation would not exist in the first place, so $\ann(f)$ would be all of $A$ only when $f=0$, and would be $0$ otherwise. That is, in this case $\supp(f)$ is empty only when $f=0$, and is all of $\Spec A$ otherwise, and since we know from [Proposition 4](#prop4) that $\Spec A$ is irreducible, we know that the unique associated point of $\Spec A$ is only the generic point $(0)$.

Therefore, to see an example of an embedded point, we must look at the case where $A$ is not an integral domain, and thus $\ann(f)$ is neither $0$ nor $A$.

::: Example 11
Consider the affine scheme $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2, \x_1\x_2)$. Then by [§Spectra, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9), as a set $X=Z(\x_2^2,\x_1\x_2)$, and since $\sqrt{(\x_2^2,\x_1\x_2)}=(\x_2)$, this is $Z(\x_2)$, that is, the $\x_1$-axis $\Spec\mathbb{K}[\x_1]$.

Now let us find the associated points directly in the form $\ann(f)$ according to [Proposition 10](#prop10). Any element of the ring $A=\mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ can be written uniquely in the form

$$p(\x_1)+c\x_2,\qquad p\in \mathbb{K}[\x_1],\quad c\in \mathbb{K}$$

and since $\x_1\x_2=0$,

$$\x_1\cdot(p(\x_1)+c\x_2)=p(\x_1)\x_1.$$

That is, $\ann(\x_1)=(\x_2)$, and this is the generic point of the unique irreducible component of $X$.

On the other hand, from $\x_2^2=0$ and $\x_1\x_2=0$,

$$\x_2\cdot(p(\x_1)+c\x_2)=p(0)\x_2$$

so $\ann(\x_2)=(\x_1,\x_2)$. This is an ideal that properly contains $\ann(\x_1)=(\x_2)$, and geometrically corresponds to the origin. Unlike the above example, this is a point that does not appear as the generic point of an irreducible component of $X$, that is, an embedded point.

In fact, these two points are all the associated points of $X$. For $f=p(\x_1)+c\x_2$ and $g=q(\x_1)+d\x_2$, from $\x_1\x_2=\x_2^2=0$,

$$fg=p(\x_1)q(\x_1)+\bigl(dp(0)+cq(0)\bigr)\x_2$$

so if $p=0$ and $c\neq 0$, then $\ann(f)$ is the set of $g$ satisfying $q(0)=0$, that is, $(\x_1,\x_2)$; if $p\neq 0$ and $p(0)=0$, then $q=0$ is forced and $\ann(f)=(\x_2)$; and if $p(0)\neq 0$, then both $q=0$ and $d=0$ are forced and $\ann(f)=0$. That is, the prime ideals obtained as annihilators of nonzero elements are only $(\x_2)$ and $(\x_1,\x_2)$.

Unlike $Z(\x\y)$ in [§Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6), note that this zero-divisor relation does not come from the product of two irreducible components. Specifically, the side $\x_2\in \ann(\x_1)$ is data already visible at the generic point $(\x_2)$, but the side $\x_1\in \ann(\x_2)$ is, as $\supp(\x_2)=Z(\ann(\x_2))=\{(\x_1,\x_2)\}$ shows, the fact that $\x_2$ vanishes everywhere except the origin, and is therefore captured as an associated prime only at the embedded point.
:::

## Rational Functions

Now we define rational functions defined on a scheme. First, by the second result of [\[Commutative Algebra\] §Associated Primes, ⁋Corollary 4](/en/math/commutative_algebra/associated_primes#cor4), the following map

$$A \rightarrow \prod_\text{\scriptsize $\mathfrak{p}$ associated prime} A_\mathfrak{p}$$

is injective. Therefore for any open subset $U$ of a locally Noetherian scheme $X$, the following map

$$\Gamma(U, \mathcal{O}_X) \rightarrow \prod_\text{\scriptsize $x$ associated in $U$} \mathcal{O}_{X,x}\tag{$\ast$}$$

is injective. This holds even when $U$ is not affine: covering $U$ by affine open subsets $V_k$ that are spectra of Noetherian rings, the associated points of $V_k$ are exactly the associated points of $U$ belonging to $V_k$ by the rephrasing after [Definition 8](#def8), so applying the above injectivity on affines to each $V_k$ yields $f\vert_{V_k}=0$.

::: Definition 12
For a locally Noetherian scheme $X$ and an open subset $U$ containing all associated points of $X$, we call the image of an element of $\Gamma(U, \mathcal{O}_X)$ under ($\ast$) a *rational function* defined on $X$.
:::

Therefore, by definition, a rational function defined on $X$ consists of the data of (1) a *domain of definition* $U$ containing all associated points of $X$, and (2) a function $f\in \Gamma(U, \mathcal{O}_X)$ on it, and two such pairs $(U, f)$ and $(U',f')$ define the same function if $f$ and $f'$ define the same function on $U\cap U'$. This structure of pairs and equivalence relation is exactly of the same form as the definition of rational functions on varieties in [\[Algebraic Varieties\] §Rational Maps, ⁋Definition 1](/en/math/algebraic_varieties/rational_maps#def1). The only difference is that now the domain of definition $U$ is required to contain all associated points, and since associated points are points that did not appear in classical algebraic geometry, this is not so surprising.

Then examining where this condition comes from is essential for understanding [Definition 12](#def12). First, by [Proposition 10](#prop10), for any associated point $\mathfrak{p}$ of $X=\Spec A$,

$$\mathfrak{p}=\ann(f),\qquad \supp(f)=Z(\mathfrak{p})$$

there exists a nonzero function $f\in \Gamma(X, \mathcal{O}_X)$ satisfying this, and this satisfies the condition of [Definition 12](#def12), so the pair $(X, f)$ defines some nonzero rational function along ($\ast$).

Now consider an open subset $U$ missing this associated point $\mathfrak{p}$. Then $Z(\mathfrak{p})$ is an irreducible closed subset having $\mathfrak{p}$ as its generic point ([§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)), so any nonempty open subset of $Z(\mathfrak{p})$ always contains $\mathfrak{p}$, and therefore we know that we must have $U\cap Z(\mathfrak{p})=\emptyset$. That is, the germs of $f$ at all points contained in such an open subset $U$, in particular at the associated points contained in $U$, must be $0$. The problem is that if we allow such an open subset $U$ as a domain of definition for a rational function, then by the injectivity of ($\ast$) above, $f$ becomes indistinguishable from $0$.

Looking at the simplest example of a generic point, when $\mathfrak{p}$ is the generic point of some irreducible component $C$, we have $Z(\mathfrak{p})=C$, so if $f$ is not defined at this point, that is, intuitively if it has a pole at this point, the above argument means that $U$ misses the entire component $C$ and thus $f\vert_U=0$. Similarly, when $\mathfrak{p}$ is an embedded point, $Z(\mathfrak{p})$ becomes a smaller closed set rather than an entire component, but such a loss still occurs.

For example, consider $Z(\x\y)=\Spec \mathbb{K}[\x,\y]/(\x\y)$ from [§Topology of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6). This scheme has two irreducible components, the $y$-axis $Z(\x)$ and the $x$-axis $Z(\y)$, whose generic points are $(\x)$ and $(\y)$ respectively. Also, since $\ann(\y)=(\x)$, the function $f$ obtained from the result of [Proposition 10](#prop10) is precisely $\y$, and indeed $\supp(\y)=Z(\x)$ shows that this gives the entire $y$-axis. Now if we consider an open subset $U=D(\x)$ that excludes this generic point $(\x)$, then from $\x\y=0$,

$$\y=\x^{-1}(\x\y)=0\qquad\text{in $A_\x$}$$

so $\y\vert_U=0$. That is, the moment we take $U$ as a domain of definition, the function $\y$ carrying the information of the $y$-axis becomes indistinguishable from the $0$ rational function, which exactly reflects the fact that $U$ misses the entire component that is the $y$-axis.

::: Example 13
Let us examine what rational functions on $X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ from [Example 11](#ex11) concretely look like. By the second result of [\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7), the set of all zero-divisors of $A=\mathbb{K}[\x_1,\x_2]/(\x_2^2,\x_1\x_2)$ equals the union of associated primes

$$(\x_2)\cup(\x_1,\x_2)=(\x_1,\x_2)$$

so a non-zerodivisor is exactly an element that does not vanish at the origin, that is, of the form $s=q(\x_1)+c'\x_2$ for $q$ satisfying $q(0)\ne0$. Such an $s$ does not belong to either of the two associated primes $(\x_2),(\x_1,\x_2)$, so $D(s)$ contains both associated points of $X$ and becomes a valid domain of definition satisfying the condition of [Definition 12](#def12), and by [§Affine Schemes, ⁋Lemma 6](/en/math/scheme_theory/affine_schemes#lem6) the functions on it are given by $A_s$.

Our claim is that looking only at the rational functions defined on this domain $D(s)$, they already give all rational functions on $X$. For this, suppose an arbitrary domain of definition $U$ is given, and let $X\setminus U=Z(I)$. Then since $U$ must contain associated points, for this there must exist an element of $I$ that does not vanish at the origin, that is, an element not contained in the ideal $(\x_1,\x_2)$. Such an element is exactly the non-zerodivisor $s$ examined above, and from $s\in I$ we obtain $D(s)\subseteq U$. That is, any domain of definition always contains such a $D(s)$ inside it, and through this we can restrict a function defined on $U$ to $D(s)$, and since $D(s)$ already contains all associated points, by the injectivity of ($\ast$) this restriction preserves distinct functions on $U$ as distinct on $D(s)$. Moreover, for the same reason, ($\ast$) for $U$ decomposes as the composition of this restriction and ($\ast$) for $D(s)$, so restricting a function on $U$ to $D(s)$ does not change its image, that is, the rational function it defines.

From the above, the total quotient ring $K(X)$ formed by all rational functions on $X$, using the same notation for elements as in [Example 11](#ex11), becomes

$$K(X)=\left\{\frac{p(\x_1)+c\x_2}{q(\x_1)+c'\x_2} \mid q(0)\neq0\right\}.$$

This is a parallel form to the classical case where the fraction field was the set of rational expressions with nonzero denominator, except that the condition has changed to the denominator not vanishing not only at the generic point but also at the origin.

What makes this different from the classical function field is that the above $K(X)$ contains nonzero nilpotents, and this is precisely due to the embedded point. Specifically, $\x_2$ is a nilpotent element satisfying $\x_2^2=0$ but becomes a nonzero function in $K(X)$. If [Definition 12](#def12) had not required this embedded point to be contained in the domain of definition, then $D(\x_1)$ excluding the origin would also have been allowed as a domain of definition, and as seen in [Example 11](#ex11), $\x_2$ is already $0$ on it, so $\x_2$ would have disappeared in $K(X)$, and thus the nilpotent-directional thickening of $X$ would not have been detected in $K(X)$.
:::

More generally, the collection of rational functions defined on a locally Noetherian scheme $X$ defines the *total quotient ring* $K(X)$ in the same manner as the above construction. If $X$ is an integral scheme, then $X$ is in particular irreducible and thus has a unique generic point $x$, and this point must correspond to the unique minimal prime ideal $(0)$ of the integral domain $A$ for any affine open subset $U\cong\Spec A$. Then the localization at this point is the same as adding all nonzero elements of $A$ as denominators, that is, $\Frac(A)$, so $K(X)\cong \mathcal{O}_{X,x}\cong \Frac(A)$, and this shows that the fraction field of $A$, which we already knew when $X$ consisted of a single affine open $\Spec A$, plays the same role as the field of rational functions on a general integral scheme.


---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
[^1]: In this process we used that $X$ has finitely many irreducible components. This ensures that the union of the remaining components is again a closed set, and therefore if these two closed sets do not meet, they become simultaneously open sets, contradicting connectedness.
