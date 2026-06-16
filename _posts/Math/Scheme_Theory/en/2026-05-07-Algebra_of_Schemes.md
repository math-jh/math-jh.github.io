---
title: "Algebra of Schemes"
description: "We examine the algebraic structure of schemes, define reduced and integral schemes, and prove that reducedness is a stalk-local property. We also show that an integral scheme is equivalent to an irreducible reduced scheme."
excerpt: "Definitions and properties of reduced schemes and integral schemes"

categories: [Math / Scheme Theory]
permalink: /en/math/scheme_theory/algebra_of_schemes
sidebar: 
    nav: "scheme_theory-en"

date: 2025-02-05
last_modified_at: 2025-02-11
weight: 6
translated_at: 2026-06-02T00:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-02T00:30:02+00:00
---
A scheme is simultaneously a geometric and an algebraic object, so to understand it well we must consider not only the topological structure of schemes examined in previous posts but also their algebraic structure at the same time; in earlier posts we briefly surveyed how this philosophy is reflected. In this post we develop that philosophy further.

## Reduced Schemes and Integral Schemes

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> A scheme $$X$$ is a *reduced scheme* if for every open subset $$U$$, $$\mathcal{O}_X(U)$$ is reduced. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 11](/en/math/algebraic_structures/field_of_fractions#def11)) Similarly, $$X$$ is *integral* if for every open subset $$U$$, $$\mathcal{O}_X(U)$$ is an integral domain. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5))

</div>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> A scheme $$X$$ is reduced if and only if for every $$x\in X$$, the stalk $$\mathcal{O}_{X, x}$$ is a reduced ring.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for any point $$x\in X$$ of a reduced scheme $$X$$, consider an affine open subscheme $$U=\Spec A$$ containing $$x$$. Let $$\mathfrak{p}$$ be the prime ideal corresponding to $$x$$ in $$\Spec A$$; then

$$\mathcal{O}_{X,x}=(\mathcal{O}_X\vert_U)_x\cong \mathcal{O}_{\Spec A, \mathfrak{p}}\cong A_\mathfrak{p}$$

and by assumption $$\mathcal{O}_X(U)\cong A$$ is reduced, so $$A_\mathfrak{p}$$ is also reduced.

Conversely, suppose $$\mathcal{O}_{X,x}$$ is reduced for every $$x\in X$$. Then for any open subset $$U$$, the inclusion

$$\mathcal{O}_X(U)\hookrightarrow\prod_{x\in U} \mathcal{O}_{X,x}$$

shows that $$\mathcal{O}_X(U)$$ is reduced.

</details>

From this we see that reducedness is a stalk-local property. ([§Topological Structure of Schemes, ⁋Proposition 16](/en/math/scheme_theory/topology_of_schemes#prop16)) Moreover, since it is easy to show that the localization of a reduced ring is reduced, the spectrum of a reduced ring is itself reduced.

Similarly, the spectrum of an integral domain is an integral scheme. This is not difficult to prove directly, but in [Proposition 4](#prop4) we prove that a scheme $$X$$ is integral if and only if it is irreducible and reduced. Then the spectrum $$\Spec A$$ of an integral domain $$A$$ is

1. a reduced scheme, because $$A$$ is a reduced ring, and
2. irreducible, because $$A$$ has the unique minimal prime ideal $$\{0\}$$.

Thus, granting this, we see that the spectrum of an integral domain is an integral scheme.

For the proof of [Proposition 4](#prop4), it is convenient to translate irreducibility into algebraic language as follows.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> An affine scheme $$\Spec A$$ is irreducible if and only if its nilradical $$\mathfrak{N}(A)$$ is a prime ideal.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$\Spec A$$ is irreducible if and only if for any two basic open sets $$D(f),D(g)\neq\emptyset$$, we have $$D(fg)\neq\emptyset$$. From the equivalence

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

([\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 14](/en/math/algebraic_structures/field_of_fractions#prop14)) we know that the statement $$D(f),D(g)\neq\emptyset\implies D(fg)\neq\emptyset$$ is equivalent to the statement

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A).$$

</details>

Now we obtain the following.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> $$X$$ is integral if and only if it is reduced and irreducible.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$X$$ is integral. Since every integral domain is reduced, $$X$$ is a reduced scheme. If $$X$$ were not irreducible, there would exist two disjoint nonempty open subsets $$U_1,U_2\neq\emptyset$$. Then for the open subset $$U_1\cup U_2$$,

$$\mathcal{O}_X(U_1\cup U_2)=\mathcal{O}_X(U_1)\times \mathcal{O}_X(U_2)$$

and the right-hand side is not an integral domain, contradicting the assumption that $$X$$ is integral.

Conversely, let an irreducible reduced scheme $$X$$ be given; we show that $$X$$ is integral. That is, for any open subset $$U$$ of $$X$$, we must show that $$\mathcal{O}_X(U)$$ is an integral domain. We first establish the following claim.

**Claim.** For any affine open subset $$\Spec A\cong V\subseteq X$$, $$\mathcal{O}_X(V)\cong A$$ is always an integral domain.
> From the assumption that $$X$$ is reduced, we know that $$A$$ must be a reduced ring. On the other hand, since $$X$$ is an irreducible closed subset of itself, $$V$$ is also irreducible, and hence by ([\[Topology\] §Dimension, ⁋Proposition 14](/en/math/topology/dimension#prop14)) and [Lemma 3](#lem3), $$\mathfrak{N}(A)=0$$ is a prime ideal, so $$A$$ is an integral domain.

Now we show that for a general open subset $$U$$ of $$X$$, $$\mathcal{O}_X(U)$$ is an integral domain. To this end, suppose two elements $$f,g\in \mathcal{O}_X(U)$$ satisfy $$fg=0$$. Consider the two open subsets of $$U$$

$$D_U(f)=\{x\in U\mid f_x\not\in \mathfrak{m}_x\},\qquad D_U(g)=\{x\in U\mid g_x\not\in \mathfrak{m}_x\}$$

and their complements $$Z_U(f), Z_U(g)$$; then $$U=Z_U(f)\cup Z_U(g)$$. Since $$X$$ is irreducible, by ([\[Topology\] §Dimension, ⁋Proposition 14](/en/math/topology/dimension#prop14)) its open subset $$U$$ is likewise irreducible, and therefore either $$Z_U(f)=U$$ or $$Z_U(g)=U$$ must hold. Without loss of generality, suppose $$Z_U(f)=U$$. Then for any open affine subset $$V$$ of $$U$$, defining

$$D_V(f)=\{x\in V\mid f_x\not\in \mathfrak{m}_x\}$$

in $$V$$, we have $$D_V(f)=D_U(f)\cap V=D(f\vert_{U\cap D_U(f)})\subseteq V$$, and for this to be empty, $$f\vert_{U\cap D_U(f)}$$ must be a nilpotent element of $$\mathcal{O}_X(V)$$. However, by the claim above $$\mathcal{O}_X(V)$$ is an integral domain, so this forces $$f\vert_{U\cap D_U(f)}=0$$, and since this holds for every open affine subset $$V$$ of $$U$$, we must have $$f=0$$.

</details>

On the other hand, from [§Topological Structure of Schemes, ⁋Example 6](/en/math/scheme_theory/topology_of_schemes#ex6) we know that the irreducibility of an arbitrary scheme $$X$$ cannot be determined by looking at stalks alone. For example, $$Z(\x(\x-1))$$ splits into two components, so points in each component know nothing about points in the other component. Hence integrality also cannot be determined from stalks alone.

However, if $$X$$ is a *connected* scheme, its irreducible components must meet at some point, and by examining the stalk at that point we might be able to detect irreducibility. The following proposition makes this idea precise.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> A Noetherian scheme $$X$$ is integral if and only if it is nonempty and connected and each stalk $$\mathcal{O}_{X,x}$$ is an integral domain.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, if $$X$$ is integral then it is irreducible and hence connected, and since the localization of an integral domain is an integral domain, one direction is clear.

For the opposite direction, that $$X$$ is reduced is clear because every integral domain is reduced and reducedness is a stalk-local property. Thus, using the given conditions, it suffices to show that $$X$$ is irreducible; the rest follows from [Proposition 4](#prop4).

Since $$X$$ is a Noetherian scheme, there exist suitable Noetherian rings $$A_1,\ldots, A_r$$ such that $$X=\bigcup \Spec A_i$$. Also, $$X$$ is Noetherian as a topological space, and therefore by ([\[Topology\] §Dimension, ⁋Proposition 13](/en/math/topology/dimension#prop13)) it has finitely many irreducible components. Let

$$X=\bigcup_{j=1}^s X_j\tag{$\ast$}$$

be the decomposition of $$X$$ into irreducible components. For a fixed $$i$$, among the sets

$$X_1\cap \Spec A_i,\quad X_2\cap \Spec A_i,\quad\ldots,\quad X_s\cap \Spec A_i$$

the nonempty ones are the irreducible components of $$\Spec A_i$$. Now by [§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16), each of these defines a minimal prime ideal $$\mathfrak{q}_j=I(X_j)$$, and conversely any minimal prime ideal of $$A_i$$ uniquely determines an irreducible component $$X_j\cap \Spec A_i$$.

On the other hand, since $$X$$ is connected, consider the intersection

$$X_1\cap \bigcup_{j=2}^s X_j$$

in the irreducible decomposition ($$\ast$$). This is the intersection of two nonempty open subsets of $$X$$, and because $$X$$ is connected they must meet at some point $$x$$. That is, there exists a suitable $$j$$ such that $$x\in X_1\cap X_j$$. Let $$\Spec A_i$$ be an affine cover of $$X$$ containing $$x$$, and suppose $$x$$ corresponds to a prime ideal $$\mathfrak{p}$$. Thus

$$x\in \Spec A_i\cap X_1\cap X_j=(\Spec A_i\cap X_1)\cap (\Spec A_i\cap X_j).$$

From the preceding argument, $$\Spec A_i\cap X_1$$ has generic point $$\mathfrak{q}_1$$, and $$\Spec A_i\cap X_j$$ has generic point $$\mathfrak{q}_j$$; these are minimal prime ideals of $$A_i$$. Now consider the stalk at $$x$$, $$\mathcal{O}_{X,x}\cong (A_i)_\mathfrak{p}$$. By the minimality of $$\mathfrak{q}_1,\mathfrak{q}_2$$ we have $$\mathfrak{q}_1,\mathfrak{q}_2\subseteq \mathfrak{p}$$, and therefore $$\mathfrak{q}_1 A_i, \mathfrak{q}_2 A_i$$ are minimal prime ideals of $$A_i$$. ([\[Commutative Algebra\] §Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8)) But an integral domain has a unique minimal prime ideal $$(0)$$, so this contradicts the assumption that $$\mathcal{O}_{X,x}$$ is an integral domain.

</details>

The key logic in the above proof can be summarized as follows:

1. Since $$X$$ is connected, if we decompose $$X$$ into irreducible components then each irreducible component must meet another one[^1]
2. Let $$x$$ be a point where two irreducible components meet; then any open neighborhood of $$x$$ contains the generic point of each irreducible component ([§Spectra, ⁋Proposition 16](/en/math/scheme_theory/spectrums#prop16)),
3. Therefore these generic points survive in the stalk $$\mathcal{O}_{X,x}$$ at $$x$$, but this is impossible since $$\mathcal{O}_{X,x}$$ is an integral domain.

We will examine this property of generic points at the end of this post.

## Normal Schemes

In parallel with integral schemes, we can make the following definition.

<div class="definition" markdown="1">

<ins id="def6">**Definition 6**</ins> A scheme $$X$$ is *normal* if for every $$x\in X$$, the stalk $$\mathcal{O}_{X,x}$$ is a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Definition 3](/en/math/commutative_algebra/integral_extension#def3))

</div>

In general, the localization of a normal domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 12](/en/math/commutative_algebra/integral_extension#prop12)) From this we see that the spectrum $$\Spec A$$ of a normal domain $$A$$ is a normal scheme.

Every integral domain is reduced, and since reducedness can be checked on stalks by [Lemma 2](#lem2), every normal scheme is reduced. On the other hand, being integral is not a stalk-local property, so a normal scheme is not in general an integral scheme. However, if $$X$$ is a connected, nonempty Noetherian scheme, then by [Proposition 5](#prop5) normality implies integrality.

Moreover, we know that a unique factorization domain is always a normal domain. ([\[Commutative Algebra\] §Integral Extensions, ⁋Proposition 9](/en/math/commutative_algebra/integral_extension#prop9)) From this we define the following.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A scheme $$X$$ is *factorial* if for every $$x\in X$$, the stalk $$\mathcal{O}_{X,x}$$ is a unique factorization domain.

</div>

Hence every factorial scheme is a normal scheme. Also, since the localization of a unique factorization domain is a unique factorization domain, the spectrum $$\Spec A$$ of a unique factorization domain $$A$$ is factorial.

## Associated Points

By [§Spectra, ⁋Corollary 17](/en/math/scheme_theory/spectrums#cor17), we know that there is a one-to-one correspondence between the irreducible components of a scheme $$X=\Spec A$$ and the minimal prime ideals of the ring $$A$$. This was used crucially in [Proposition 5](#prop5) above.

On the other hand, algebraically a minimal prime ideal is always an associated prime ideal. This can be seen by viewing the ring $$A$$ as a module over itself: since $$\ann A=\{0\}$$, we apply ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)). Therefore we define the associated points of a (locally Noetherian) scheme as follows.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> For a point $$x$$ of a locally Noetherian scheme $$X$$ and an affine open neighborhood $$U\cong \Spec A$$ of $$x$$, we say that $$x$$ is an *associated point* of $$X$$ if the prime ideal $$\mathfrak{p}_x\subset A$$ corresponding to $$x$$ is an associated prime ideal of $$A$$.

</div>

This definition does not depend on the choice of $$U$$, and moreover can be expressed stalk-locally. Indeed, for an affine open neighborhood $$\Spec A$$ containing $$x$$, the condition that $$X$$ is locally Noetherian lets us assume that $$A$$ is a Noetherian ring; then from the third condition of ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)) we know that there is a one-to-one correspondence between the associated prime ideals of $$A$$ contained in $$\mathfrak{p}_x$$ and the associated prime ideals of $$A_{\mathfrak{p}_x}$$, and via this correspondence [Definition 8](#def8) can be rewritten as:

> For a point $$x$$ of a locally Noetherian scheme $$X$$, we say that $$x$$ is an *associated point* of $$X$$ if $$\mathfrak{m}_x$$ is an associated prime ideal of $$\mathcal{O}_{X,x}$$.

Now the first condition of ([\[Commutative Algebra\] §Associated Primes, ⁋Theorem 7](/en/math/commutative_algebra/associated_primes#thm7)) also guarantees finiteness of associated points when $$X$$ is a quasicompact locally Noetherian scheme, that is, when $$X$$ is a Noetherian scheme.

Moreover, by this condition every minimal prime ideal is an associated prime ideal, so this notion generalizes the concept of generic points on $$\Spec A$$. By [Definition 8](#def8) we may restrict our attention to the spectrum $$\Spec A$$ of a Noetherian ring.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Among the associated points of the spectrum $$\Spec A$$ of a Noetherian ring, those that do not correspond to the generic points of the irreducible components of $$\Spec A$$ are called *embedded points*.

</div>

On the other hand, the following holds by definition.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> The associated points of the spectrum $$\Spec A$$ of a Noetherian ring are precisely the generic points of the irreducible components of $$\supp(f)$$ for suitable $$f\in A$$, and conversely.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for any $$g\in A$$ and prime ideal $$\mathfrak{q}\in \Spec A$$,

$$\mathfrak{q}\in \supp(g)\iff g_\mathfrak{q}\neq 0\text{ in $A_\mathfrak{q}$}\iff \ann(g_\mathfrak{q})\neq A_\mathfrak{q}$$

holds. Now by ([\[Commutative Algebra\] §Localization, ⁋Proposition 5](/en/math/commutative_algebra/localization#prop5))

$$\ann(g_\mathfrak{q})=\ann(g)A_\mathfrak{q}$$

so the last condition is equivalent to $$\ann(g)\setminus \mathfrak{q}=\emptyset$$, that is, $$\mathfrak{q}\in Z(\ann(g))$$. From this we see that for any $$g\in A$$,

$$\supp(g)=Z(\ann(g))$$

holds. Therefore there is a one-to-one correspondence between the irreducible components of $$\supp(g)$$ and the minimal prime ideals containing $$\ann(g)$$.

Now let an arbitrary associated point $$\mathfrak{p}$$ of $$\Spec A$$ be given; by definition there exists a suitable $$f\in A$$ such that $$\mathfrak{p}=\ann(f)$$. Then

$$\supp(f)=Z(\ann(f))=Z(\mathfrak{p})$$

and since it is obvious that $$\mathfrak{p}$$ is a minimal prime of $$\ann(f)=\mathfrak{p}$$, we see that $$\mathfrak{p}$$ is a generic point of $$\supp f$$. This argument reverses as well, by the observation above.

</details>

Examining the identity

$$\supp(f)=Z(\ann(f))$$

used in the proof above, if $$A$$ were an integral domain then $$\ann(f)$$ would be all of $$A$$ only when $$f=0$$, and would be $$0$$ otherwise. That is, in this case $$\supp(f)$$ is empty only when $$f=0$$, and is all of $$\Spec A$$ otherwise; since we know from [Proposition 4](#prop4) that $$\Spec A$$ is irreducible, we see that the only associated point of $$\Spec A$$ is the generic point $$(0)$$.

More generally, if $$A$$ is not an integral domain, there exist cases where $$\ann(f)$$ is neither $$0$$ nor $$A$$, so the possibility of embedded points arises.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> Consider the affine scheme $$X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2^2, \x_1\x_2)$$. Then by [§Spectra, ⁋Lemma 6](/en/math/scheme_theory/spectrums#lem6) and [§Spectra, ⁋Proposition 9](/en/math/scheme_theory/spectrums#prop9), as a set

$$X= Z(\x_2^2,\x_1\x_2)=Z(\x_2^2)\cap Z(\x_1\x_2)=\{(0,0)\}.$$

</div>

## Rational Functions

Now we define rational functions on a scheme. First, by the second result of ([\[Commutative Algebra\] §Associated Primes, ⁋Corollary 4](/en/math/commutative_algebra/associated_primes#cor4)), we know that the map

$$A \rightarrow \prod_\text{\scriptsize $\mathfrak{p}$ associated prime} A_\mathfrak{p}$$

is injective. Therefore for any open subset $$U$$ of a locally Noetherian scheme $$X$$, the map

$$\Gamma(U, \mathcal{O}_X) \rightarrow \prod_\text{\scriptsize $x$ associated in $U$} \mathcal{O}_{X,x}\tag{$\ast$}$$

is injective.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> For a locally Noetherian scheme $$X$$ and an open subset $$U$$ containing all associated points of $$X$$, we call the image of $$\Gamma(U, \mathcal{O}_X)$$ under ($$\ast$$) a *rational function* defined on $$X$$.

</div>

Thus, by definition, a rational function defined on $$X$$ consists of the data of (1) a *domain of definition* $$U$$ containing all associated points of $$X$$, and (2) a function $$f\in \Gamma(U, \mathcal{O}_X)$$ on it, and two such pairs $$(U, f)$$ and $$(U',f')$$ define the same function if $$f$$ and $$f'$$ agree on $$U\cap U'$$.

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> Consider the affine scheme $$X=\Spec \mathbb{K}[\x_1,\x_2]/(\x_2-\x_1^2)$$. Then $$X$$ has a unique associated prime $$(0)$$, and any open subset of $$X$$ contains this point, so a rational function on $$X$$ consists of any nonempty open subset $$U$$ together with a function $$f\in\Gamma(U, \mathcal{O}_X)$$ on it.

On the other hand, we know that any (nonempty) open subset of an affine scheme $$X=\Spec A$$ is of the form $$\Spec A_f$$ for a suitable nonzero $$f\in A$$, and the functions on it are given by $$A_f$$. For instance, in this example if we choose $$f$$ to be the image of $$\x_1$$ in $$A$$, then by the isomorphism

$$\left(\frac{\mathbb{K}[\x_1,\x_2]}{(\x_2-\x_1^2)}\right)_{\x_1}\cong\frac{\mathbb{K}[\x_1,\x_2]_{\x_1}}{(\x_2-\x_1^2)_{\x_1}}$$

functions such as $$1/\x_1$$ defined on the open subset $$\Spec A_{\x_1}$$ become rational functions on $$X$$. Through this we see that all rational expressions not having $$\x_2-\x_1^2$$ as a factor in the denominator become rational functions on $$X$$ (on a suitable open subset).

</div>

The collection of rational functions defined on a locally Noetherian scheme $$X$$ forms the *total quotient ring* $$K(X)$$. Now, as above, suppose $$X$$ is an integral scheme. Then in particular $$X$$ is irreducible, so it has a unique generic point $$x$$. For any affine open subset $$U\cong\Spec A$$, this point must correspond to the unique minimal prime ideal $$(0)$$ of the integral domain $$A$$. The localization at this point is obtained by inverting all nonzero elements of $$A$$, that is, it coincides with $$\Frac(A)$$.

---
**References**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---
[^1]: In this process we used the fact that each irreducible component is an open subset because there are finitely many of them.
