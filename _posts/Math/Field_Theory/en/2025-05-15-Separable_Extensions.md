---
title: "Separable Extensions"
description: "This post defines the notion of separable field extensions based on the properties of étale algebras, and discusses the differential characterization of étale algebras through lemmas in algebraically closed fields."
excerpt: "Characterization of separable extensions through étale algebras"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/separable_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Separable_Extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-en"

date: 2025-05-15
last_modified_at: 2025-05-15
weight: 6
translated_at: 2026-05-31T06:30:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T06:30:04+00:00
---
## Properties of Étale Algebras

We now define the notion of a separable extension. First, we review the properties of étale algebras that we studied in the previous post.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> Let $$A$$ be a commutative $$\mathbb{K}$$-algebra of finite degree over an algebraically closed field $$\mathbb{K}$$, and suppose $$\Omega_{A/\mathbb{K}}=0$$. Then for any maximal ideal $$\mathfrak{m}$$ of $$A$$, we have $$\mathfrak{m}=\mathfrak{m}^2$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The field $$A/\mathfrak{m}$$ is a finite degree extension of the algebraically closed field $$\mathbb{K}$$, so it must be an algebraic extension, and therefore $$[A/\mathfrak{m}:\mathbb{K}]=1$$. Thus for each $$a\in A$$ we can find $$\lambda\in \mathbb{K}$$ such that $$a-\lambda\in \mathfrak{m}$$. Then the map

$$A \rightarrow \mathfrak{m}/\mathfrak{m}^2;\qquad a\mapsto a-\lambda)$$

defines a function $$D:A \rightarrow \mathfrak{m}/\mathfrak{m}^2$$ that is evidently a $$\mathbb{K}$$-derivation. By the universal property of [[Multilinear Algebra] §Differential Modules, ⁋Proposition 8](/en/math/multilinear_algebra/differential_modules#prop8), $$D$$ must factor through $$\Omega_{A/\mathbb{K}}$$, which is $$0$$ by assumption, so $$D=0$$.

</details>

To establish our characterization of étale algebras, we need the following lemma, which builds on the result of the previous lemma.

<div class="proposition" markdown="1">

<ins id="lem2">**Lemma 2**</ins> Let $$\mathfrak{a}$$ be a finitely generated ideal of a commutative ring $$A$$ satisfying $$\mathfrak{a}=\mathfrak{a}^2$$. Then there exists an idempotent $$e\in A$$ such that $$\mathfrak{a}=Ae$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$a_1,\ldots,a_n$$ be generators of $$\mathfrak{a}$$. Since $$\mathfrak{a}=\mathfrak{a}^2$$, for each $$i$$ there exist $$x_{ij}$$ such that

$$a_i=\sum_{j=1}^r x_{ij}a_j$$

holds. For the resulting $$r\times r$$ matrix, let $$M=I_r-(x_{ij})$$. Then by the adjoint matrix of $$M$$, there exists an $$r\times r$$ matrix $$N$$ such that

$$NM=(\det M) I_r$$

holds. Now computing where the column vector corresponding to $$a_j$$ goes on both sides, we see that $$(\det M)a_j=0$$ must hold for all $$j$$, and therefore $$(\det M)\mathfrak{a}=0$$.

On the other hand, by its definition the matrix $$M$$ becomes $$I_r$$ after reduction modulo $$\mathfrak{a}$$, so its determinant $$\det M$$ is also $$1$$ modulo $$\mathfrak{a}$$. Setting $$e=1-D$$ then gives the desired idempotent $$e$$.

</details>

The differential characterization of étale algebras is then given as follows.

<div class="proposition" markdown="1">

<ins id="thm3">**Theorem 3**</ins> For a finite degree commutative $$\mathbb{K}$$-algebra $$A$$, the following are equivalent: $$A$$ is étale, and $$\Omega_{A/\mathbb{K}}=0$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since both $$\Omega_{A/\mathbb{K}}$$ and the notion of an étale algebra behave well under base change, we may assume that $$\mathbb{K}$$ is algebraically closed. More precisely, $$A$$ being étale is equivalent to the $$\overline{\mathbb{K}}$$-algebra $$A_{(\overline{\mathbb{K}})}=A\otimes_\mathbb{K}\overline{\mathbb{K}}$$ being diagonalizable for the algebraic closure $$\overline{\mathbb{K}}$$ of $$\mathbb{K}$$ ([§Étale Algebras, ⁋Proposition 8](/en/math/field_theory/etale_algebras#prop8)), while by the canonical isomorphism of [[Multilinear Algebra] §Differential Modules, ⁋Proposition 12](/en/math/multilinear_algebra/differential_modules#prop12) and the definition of the $$\overline{\mathbb{K}}$$-algebra $$A_{(\overline{\mathbb{K}})}$$ we obtain the isomorphism

$$\Omega_{A_{(\overline{\mathbb{K}})}/\overline{\mathbb{K}}}\cong \Omega_{A/\mathbb{K}}\otimes_A A_{(\overline{\mathbb{K}})}=\Omega_{A/\mathbb{K}}\otimes_A A\otimes_\mathbb{K}\overline{\mathbb{K}}\cong \Omega_{A/\mathbb{K}}\otimes_\mathbb{K}\overline{\mathbb{K}}$$

and therefore $$\Omega_{A/\mathbb{K}}=0$$ is equivalent to $$\Omega_{A_{(\overline{\mathbb{K}})}/\overline{\mathbb{K}}}=0$$. That is, to prove the theorem it suffices to assume $$\mathbb{K}$$ is algebraically closed and show that $$A$$ being diagonalizable is equivalent to $$\Omega_{A/\mathbb{K}}=0$$.

First, assuming $$A$$ is diagonalizable, $$A$$ is generated by idempotents by the second condition of [§Étale Algebras, ⁋Proposition 6](/en/math/field_theory/etale_algebras#prop6). But for any idempotent $$e$$, the Leibniz rule gives

$$d(e)=d(e^2)=ed(e)+ed(e)=2ed(e)$$

and multiplying both sides by $$e$$ gives $$ed(e)=0$$, so substituting back we see that $$de=0$$. On the other hand, $$\Omega_{A/\mathbb{K}}$$ is explicitly presented as a free module generated by such elements $$de$$ modulo appropriate relations ([[Multilinear Algebra] §Differential Modules, ⁋Example 10](/en/math/multilinear_algebra/differential_modules#ex10)), from which we conclude that $$\Omega_{A/\mathbb{K}}=0$$.

Conversely, assume $$\Omega_{A/\mathbb{K}}=0$$ and let us show that $$A$$ is diagonalizable. We proceed by induction on the degree of $$A$$; the degree $$1$$ case is trivial. For the general case, choose a maximal ideal $$\mathfrak{m}$$ of $$A$$. Then by [Lemma 1](#lem1) we have $$\mathfrak{m}=\mathfrak{m}^2$$, so applying [Lemma 2](#lem2) we find an idempotent $$e$$ such that $$\mathfrak{m}=Ae$$. Then decomposing $$A$$ as a direct sum of $$\mathfrak{a}=(1-e)A$$ and $$\mathfrak{m}$$, we see from the assumption that $$\mathbb{K}$$ is algebraically closed that the extension $$A/\mathfrak{m}$$ has degree $$1$$. That is, we can write this direct sum as

$$A\cong \mathfrak{a}\oplus\mathfrak{m}\cong \mathbb{K}\times A/\mathfrak{a}$$

Now since $$\Omega$$ is a right exact functor ([[Multilinear Algebra] §Differential Modules, ⁋Proposition 13](/en/math/multilinear_algebra/differential_modules#prop13)), $$\Omega_{(A/\mathfrak{a})/\mathbb{K}}$$ is a quotient of $$\Omega_{A/\mathbb{K}}=0$$ and hence is $$0$$. Therefore, by the inductive hypothesis $$A/\mathfrak{a}$$ is diagonalizable, and so is $$A$$, which is its product with $$\mathbb{K}$$.

</details>

Earlier, in [§Radical Extensions, ⁋Example 9](/en/math/field_theory/radical_extensions#ex9), we examined a situation that could cause problems when developing Galois theory; let us revisit this example in light of [Theorem 3](#thm3).

<div class="example" markdown="1">

<ins id="ex4">**Example 4**</ins> A favorable case is $$\mathbb{Q}(\sqrt{2})/\mathbb{Q}$$, as we saw in the introduction to [§Radical Extensions](/en/math/field_theory/radical_extensions). From the computation in [[Multilinear Algebra] §Differential Modules, ⁋Example 10](/en/math/multilinear_algebra/differential_modules#ex10), we know that $$\Omega_{\mathbb{Q}[\x]/\mathbb{Q}}$$ is the free $$\mathbb{Q}[\x]$$-module generated by $$d\x$$. On the other hand, considering the ideal $$\mathfrak{I}=(\x^2-2)$$ of $$\mathbb{Q}[\x]$$, from [[Multilinear Algebra] §Differential Modules, ⁋Proposition 14](/en/math/multilinear_algebra/differential_modules#prop14) we have the exact sequence

$$\mathfrak{I}/\mathfrak{I}^2\overset{\overline{d}}{\longrightarrow}\Omega_{\mathbb{Q}[\x]/\mathbb{Q}}\otimes_\mathbb{Q}\mathbb{Q}(\sqrt{2})\overset{\Omega_0(u)}{\longrightarrow}\Omega_{\mathbb{Q}(\sqrt{2})/\mathbb{Q}}\longrightarrow 0$$

from which we know that $$\Omega_{\mathbb{Q}(\sqrt{2})/\mathbb{Q}}$$ is the $$\mathbb{Q}(\sqrt{2})$$-module generated by the element $$d(\sqrt{2})$$. But the computation

$$0=d(2)=d((\sqrt{2})^2)=2\sqrt{2}d(\sqrt{2})$$

together with the fact that $$2\sqrt{2}$$ is invertible in $$\mathbb{Q}(\sqrt{2})$$ shows that $$d(\sqrt{2})=0$$, and therefore $$\Omega_{\mathbb{Q}(\sqrt{2})/\mathbb{Q}}=0$$.

On the other hand, for the algebraic extension $$\mathbb{K}(t^{1/p})=\mathbb{K}[\x]/(\x^p-t)$$ of $$\mathbb{K}=\mathbb{F}_p(t)$$ examined in [§Radical Extensions, ⁋Example 9](/en/math/field_theory/radical_extensions#ex9), the above computation fails. Similarly, $$\Omega_{\mathbb{K}(t^{1/p})/\mathbb{K}}$$ is the $$\mathbb{K}(t^{1/p})$$-module generated by $$d(t^{1/p})$$, but the computation

$$0=d(t)=d((t^{1/p})^p)=p(t^{1/p})^{p-1}d(t^{1/p})$$

does not yield $$d(t^{1/p})=0$$. Since $$\mathbb{K}(t^{1/p})$$ has characteristic $$p$$, the coefficient $$p(t^{1/p})^{p-1}$$ is $$0$$, so the above equation gives no relation on $$d(t^{1/p})$$ whatsoever. Indeed, explicitly considering any field $$\mathbb{K}$$ and algebraic extension $$\mathbb{K}(\alpha)=\mathbb{K}[\x]/(f)$$, we have

$$\Omega_{(\mathbb{K}[\x]/(f))/\mathbb{K}}\cong\frac{\Omega_{\mathbb{K}[\x]/\mathbb{K}}\otimes_\mathbb{K}\mathbb{K}(\alpha)}{\mathfrak{I}/\mathfrak{I}^2}\cong\frac{ {\mathbb{K}[\x]\mathop{d\x}}\otimes\mathbb{K}[\x]/(f)}{(df)}\cong \frac{\mathbb{K}[\x]}{(f, f')}\mathop{d\x}$$

from which the two computations above follow.

</div>

The case we wish to exclude is precisely when the minimal polynomial $$f$$ has a multiple root, that is, when $$df=0$$; thus the notion of an étale algebra will be useful. We shall define a *separable extension* as a field extension in which every finite degree subextension is an étale $$\mathbb{K}$$-algebra. ([Definition 8](#def8)) Then, as we saw in [Example 4](#ex4), any algebraic extension of $$\mathbb{Q}$$ is a separable extension. Furthermore, we will show that any algebraic extension of a perfect field is separable. ([Proposition 9](#prop9)) Let us examine a few more properties of étale algebras that we will use in this process.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For any field $$\mathbb{K}$$, a finite degree commutative $$\mathbb{K}$$-algebra $$A$$ is reduced if and only if there exist finite degree field extensions $$\mathbb{L}_1,\ldots, \mathbb{L}_n$$ of $$\mathbb{K}$$ such that $$A$$ is isomorphic to $$\mathbb{L}_1\times\cdots\times \mathbb{L}_n$$ as a $$\mathbb{K}$$-algebra.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since $$\mathbb{L}_1\times\cdots\times \mathbb{L}_n$$ is reduced, one direction is trivial. Conversely, let $$A$$ be a finite degree reduced commutative $$\mathbb{K}$$-algebra. If $$A$$ is a field there is nothing more to show, so it suffices to prove the case where $$A$$ is not a field, and as usual by induction on the degree of $$A$$ it is enough to show that any (non-field) reduced algebra $$A$$ can always be written as a nontrivial product $$A_1\times A_2$$.

To see this, we show that $$A$$ has an idempotent other than $$0,1$$. Any ideal of $$A$$ is a finite-dimensional $$\mathbb{K}$$-vector space, so we can choose an ideal $$\mathfrak{a}$$ of $$A$$ of minimal dimension as a $$\mathbb{K}$$-vector space. Then by the minimality of $$\mathfrak{a}$$ and the assumption that $$A$$ is reduced, we have $$\mathfrak{a}^2=\mathfrak{a}$$, so [Lemma 2](#lem2) applies.

</details>

Then the claim of [Theorem 9](#thm9) mentioned above is essentially contained in the following lemma.

<div class="proposition" markdown="1">

<ins id="lem6">**Lemma 6**</ins> For a perfect field $$\mathbb{K}$$, any finite degree reduced $$\mathbb{K}$$-algebra is étale.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider a $$\mathbb{K}$$-algebra $$A$$ satisfying the hypotheses. First, by [Proposition 5](#prop5) there exist extensions such that $$A\cong \mathbb{L}_1\times\cdots \times\mathbb{L}_n$$. Since the product of étale algebras is étale, the claim reduces to showing that any finite degree field extension over a perfect field $$\mathbb{K}$$ is étale. Thus by [Theorem 3](#thm3), it suffices to show that $$d\alpha=0$$ for any $$\alpha\in A$$. By the computation in [Example 4](#ex4), we know that the equation $$f'(\alpha)d\alpha=0$$ must hold, and by similar logic we must show that $$f'(\alpha)\neq 0$$.

Suppose for contradiction that $$f'(\alpha)=0$$. If $$f$$ is constant there is nothing to prove, so we may assume $$f$$ has degree at least one; then by the result of [§Fields, ⁋Proposition 19](/en/math/field_theory/fields#prop19), we have $$\ch(\mathbb{K})=p\neq 0$$ and $$f\in \mathbb{K}[\x^p]=\mathbb{K}[\x]^p$$. But $$f$$ is a minimal polynomial, hence irreducible, and an irreducible polynomial cannot belong to $$\mathbb{K}[\x]^p$$ by definition, which is a contradiction. Therefore $$f'(\alpha)\neq 0$$.

</details>

Using the above lemma, we can now produce another characterization of étale algebras as follows.

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7**</ins> For any finite degree commutative $$\mathbb{K}$$-algebra $$A$$, the following are all equivalent.

1. $$A$$ is étale.
2. For any extension $$\mathbb{L}/\mathbb{K}$$, the algebra $$A_{(\mathbb{L})}=\mathbb{L}\otimes_\mathbb{K}A$$ is reduced.
3. There exists an extension $$\mathbb{L}/\mathbb{K}$$ such that $$\mathbb{L}$$ is perfect and $$A_{(\mathbb{L})}$$ is reduced.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That the second condition implies the third is trivial from the existence of a perfect closure, and that the first implies the second is the result of [§Étale Algebras, ⁋Proposition 8](/en/math/field_theory/etale_algebras#prop8). Thus it suffices to show that the third implies the first. This follows again from [Lemma 6](#lem6) and [§Étale Algebras, ⁋Proposition 8](/en/math/field_theory/etale_algebras#prop8).

</details>

## Separable Extensions

The time has finally come to state the following definition.

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> An algebraic extension $$\mathbb{L}/\mathbb{K}$$ is called a *separable extension* if every finite degree subextension of $$\mathbb{L}/\mathbb{K}$$ is an étale $$\mathbb{K}$$-algebra.

</div>

We could define this notion for non-algebraic field extensions as well, but for now we only consider separable algebraic extensions.

By definition, for any finite degree $$\mathbb{K}$$-algebra $$\mathbb{L}$$ that is itself a field, being étale and being separable are the same thing. From the definition, if $$\mathbb{L}/\mathbb{K}$$ is separable then any subextension is separable, and conversely if all (finite degree) subextensions are separable then $$\mathbb{L}/\mathbb{K}$$ is also separable; both are trivial.

The promised claim can now also be easily verified.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> A field $$\mathbb{K}$$ is perfect if and only if every algebraic extension $$\mathbb{L}/\mathbb{K}$$ is separable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Any algebraic extension $$\mathbb{L}/\mathbb{K}$$ is itself a finite degree reduced $$\mathbb{K}$$-algebra, so if $$\mathbb{K}$$ is perfect then one direction is trivial from [Lemma 6](#lem6). Thus it suffices to show the converse.

Suppose for contradiction that $$\mathbb{K}$$ is not perfect, so it has characteristic $$p\neq 0$$. Then from the assumption that $$\mathbb{K}$$ is not perfect, we can consider a (relative) $$p$$-radical extension $$\mathbb{K}(a)/\mathbb{K}$$ (inside an algebraic closure $$\overline{\mathbb{K}}/\mathbb{K}$$). On the other hand, the homomorphism $$\mathbb{K}(a)\rightarrow\overline{\mathbb{K}}$$ obtained from the embedding $$\mathbb{K}\hookrightarrow\overline{\mathbb{K}}$$ is unique by [§Radical Extensions, ⁋Proposition 6](/en/math/field_theory/radical_extensions#prop6). In other words, the set $$\Hom_{\Alg{\mathbb{K}}}(\mathbb{K}(a), \overline{\mathbb{K}})$$ is a singleton, and therefore

$$1=[\mathbb{K}(a):\mathbb{K}]_s\nleq [\mathbb{K}(a):\mathbb{K}]=p^e$$

so $$\mathbb{K}(a)$$ is not étale and hence not separable.

</details>

The proof of the above proposition justifies calling $$[\mathbb{K}(a):\mathbb{K}]_s$$ the *separable degree*. On the other hand, even if $$\mathbb{K}$$ is not perfect, a particular polynomial $$f$$ may still fail to have multiple roots. The following proposition is merely a compilation of what we have observed so far.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For a polynomial $$f\in \mathbb{K}[\x]$$, the following are all equivalent.

1. $$f'$$ is not $$0$$.
2. $$f$$ and $$f'$$ are coprime in $$\mathbb{K}[\x]$$.
3. There exists an extension $$\mathbb{L}/\mathbb{K}$$ such that $$f$$ has a simple root in $$\mathbb{L}[\x]$$.
4. There exists an extension $$\mathbb{L}/\mathbb{K}$$ such that $$f$$ splits into a product of distinct linear factors in $$\mathbb{L}[\x]$$.
5. $$f$$ has only simple roots in $$\overline{\mathbb{K}}/\mathbb{K}$$.
6. $$\mathbb{K}[\x]/(f)$$ is an étale $$\mathbb{K}$$-algebra.
7. $$\mathbb{K}$$ has characteristic $$0$$, or $$\ch(\mathbb{K})=p$$ and $$f\not\in\mathbb{K}[\x^p]$$.

</div>

A polynomial satisfying these conditions is called a *separable polynomial*. Then applying [Proposition 9](#prop9) once more, we see that $$\mathbb{K}$$ being perfect is equivalent to every irreducible polynomial in $$\mathbb{K}[\x]$$ being separable. Focusing on the elements added by $$f$$, we can define the following.

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> For a field extension $$\mathbb{L}/\mathbb{K}$$, an algebraic element $$x\in \mathbb{L}$$ is called a *separable element* if $$\mathbb{K}(x)/\mathbb{K}$$ is a separable extension.

</div>

By definition, if $$f$$ is the minimal polynomial of $$x$$, then $$f$$ must be separable and in this case $$x$$ becomes a simple root of $$f$$. These concepts all (of course) mean the same thing. That is, for an extension $$\mathbb{L}/\mathbb{K}$$, an element $$x\in\mathbb{L}$$, and the minimal polynomial $$f$$ of $$x$$, the following are all equivalent:

1. $$x$$ is separable.
2. $$f$$ is separable.
3. $$x$$ is a simple root of $$f$$.

Moreover, just as every element being algebraic makes an extension algebraic, the following holds.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For an algebraic extension $$\mathbb{L}/\mathbb{K}$$, the following hold.

1. If $$\mathbb{L}/\mathbb{K}$$ is separable, then every element of $$\mathbb{L}$$ is separable.
2. Conversely, if $$A$$ is a set of separable elements of $$\mathbb{L}$$ and $$\mathbb{L}=\mathbb{K}(A)$$, then $$\mathbb{L}$$ is a separable extension.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The first result is trivial, so it suffices to show the second. That is, we must show that any finite degree subextension $$\mathbb{M}$$ of $$\mathbb{L}$$ is étale. Since $$\mathbb{L}=\mathbb{K}(A)$$ and $$\mathbb{M}$$ is a finite degree subextension of $$\mathbb{L}$$, we can choose finitely many elements $$x_1,\ldots, x_m$$ from $$A$$ such that

$$\mathbb{M}\subset \mathbb{K}(x_1,\ldots, x_m)=\mathbb{K}[x_1,\ldots, x_m]$$

Each $$\mathbb{K}[x_i]$$ is a separable extension by the assumption on $$A$$, so they are étale; then $$\mathbb{K}[x_1,\ldots, x_m]$$ is obtained from their tensor product $$\mathbb{K}[x_1]\otimes\cdots\otimes \mathbb{K}[x_n]$$ by quotienting by the relations expressing their associativity and commutativity, and since $$\mathbb{M}$$ is a subalgebra of this, $$\mathbb{M}$$ is étale by [§Étale Algebras, ⁋Corollary 14](/en/math/field_theory/etale_algebras#cor14).

</details>

Furthermore, a finite degree separable extension can be generated by a single element. That is, if $$\mathbb{L}/\mathbb{K}$$ is a finite degree separable extension, we can choose an appropriate $$x\in \mathbb{L}$$ such that $$\mathbb{L}=\mathbb{K}[x]$$. Such an element is called a *primitive element*.

[Theorem 14](#thm14) shows that a primitive element can always be found for finite degree separable extensions. For this we need the following lemma.

<div class="proposition" markdown="1">

<ins id="lem13">**Lemma 13**</ins> For an infinite field $$\mathbb{K}$$, fix a commutative $$\mathbb{K}$$-algebra $$A$$. If $$A$$ has only finitely many subalgebras, and $$V$$ is a subspace generating $$A$$, then there exists $$x\in V$$ such that $$A=\mathbb{K}[x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose the subalgebras of $$A$$ are only $$A_1,\ldots, A_n$$. Then since $$V$$ generates $$A$$, it cannot generate any of the $$A_i$$; that is, $$V\not\subset A_i$$. If we can show from this that $$V\not\subset A_1\cup\cdots\cup A_n$$, then for $$x\in V\setminus A_1\cup\cdots \cup A_n$$ the subalgebra $$\mathbb{K}[x]$$ of $$A$$ cannot equal any $$A_i$$, and therefore must be $$A=\mathbb{K}[x]$$, giving the desired result.

Suppose for contradiction that $$V\subset A_1\cup\cdots\cup A_n$$. By assumption $$V\not\subset A_n$$, so there exists $$x\in V\setminus A_n$$. Then for any $$y\in V$$, consider the infinite set

$$\{x\}\cup \{y+\lambda x\mid \lambda\in\mathbb{K}\}$$

This set is a subset of $$V$$ and therefore a subset of $$A_1\cup\cdots\cup A_n$$. Hence by the pigeonhole principle, at least two of these elements must belong to the same $$A_i$$, and from this we know that there exists some $$A_i$$ containing both $$x$$ and $$y$$. By assumption $$x\not\in A_n$$, so $$i$$ cannot be $$n$$, and therefore $$y$$ must belong to one of $$A_1,\ldots, A_{n-1}$$ (just as $$x$$ does). From this we see that $$y$$ belongs to $$A_1\cup\cdots \cup A_{n-1}$$, and since $$y$$ was an arbitrary element of $$V$$, we have $$V\subset A_1\cup\cdots\cup A_{n-1}$$.

Repeating this process inductively, we eventually obtain $$V\subset A_1$$, which is a contradiction; therefore $$V\not\subset A_1\cup\cdots\cup A_n$$.

</details>

<div class="proposition" markdown="1">

<ins id="thm14">**Theorem 14**</ins> Fix an infinite field $$\mathbb{K}$$. For an algebraic extension $$\mathbb{L}/\mathbb{K}$$, the following are equivalent.

1. $$\mathbb{L}$$ has a primitive element.
2. $$\mathbb{L}$$ has only finitely many subextensions.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, suppose $$\mathbb{L}$$ has a primitive element $$x$$, and let $$f(\x)\in \mathbb{K}[\x]$$ be the minimal polynomial of $$x$$. Considering a monic polynomial $$g(\x)\in \mathbb{L}[\x]$$ dividing $$f(\x)$$ in $$\mathbb{L}[\x]$$, we can associate to each such polynomial $$g$$ the subextension of $$\mathbb{L}$$ generated by the coefficients of $$g$$. Denote this by $$\mathbb{K}_g$$. Our claim is that these $$\mathbb{K}_g$$ are exactly the subextensions of $$\mathbb{L}$$. In particular, there are at most $$2^d$$ such extensions if $$f$$ has degree $$d$$, so the second condition will hold.

To prove the claim, let $$\mathbb{M}$$ be an arbitrary subextension. Since $$x$$ is a primitive element, $$\mathbb{M}[x]=\mathbb{L}$$ holds. That is, $$x$$ is an algebraic element of the extension $$\mathbb{L}/\mathbb{M}$$, so we can choose a minimal polynomial $$h(\x)\in\mathbb{M}[\x]$$, which by [§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15) is a monic polynomial dividing $$f$$ in $$\mathbb{L}[\x]$$. Thus $$\mathbb{K}_h$$ is defined as above, and by its definition $$\mathbb{K}_h\subset\mathbb{M}$$. On the other hand, since $$x$$ is a primitive element of $$\mathbb{L}/\mathbb{K}$$, we have the equality

$$\mathbb{K}_h[x]=\mathbb{M}[x]=\mathbb{L}$$

But by definition $$[\mathbb{L}:\mathbb{M}]=\deg h$$, and since $$h(\x)\in \mathbb{K}_h[\x]$$ satisfies $$h(x)=0$$, we have $$[\mathbb{L}:\mathbb{K}_h]\leq\deg h$$. From this we conclude that $$\mathbb{K}_h=\mathbb{M}$$ must hold.

Now assuming the second condition, since $$\mathbb{L}/\mathbb{K}$$ has only finitely many subextensions, setting $$A=\mathbb{L}$$ satisfies the hypotheses of [Lemma 13](#lem13), and we obtain the desired result.

</details>

In particular, if $$\mathbb{L}/\mathbb{K}$$ is a finite degree separable extension, then it is in particular a finite degree étale $$\mathbb{K}$$-algebra, and therefore by [§Étale Algebras, ⁋Proposition 9](/en/math/field_theory/etale_algebras#prop9) we know that the second condition of the above theorem holds.

[Theorem 14](#thm14) always holds even when $$\mathbb{K}$$ is a finite field, but to prove this requires a somewhat more delicate counting argument than [Lemma 13](#lem13), so we postpone it. ([##ref##]())

On the other hand, separability is essentially (almost) an étale algebra, and since étale algebras behave well under base change ([§Étale Algebras, ⁋Corollary 14](/en/math/field_theory/etale_algebras#cor14)), with slight modifications as in the proof of [Proposition 12](#prop12), we can show that separability also behaves well under base change in the following two cases.

<div class="proposition" markdown="1">

<ins id="prop15">**Proposition 15**</ins> For an algebraic extension $$\mathbb{M}/\mathbb{L}/\mathbb{K}$$, $$\mathbb{M}/\mathbb{K}$$ is separable if and only if both $$\mathbb{M}/\mathbb{L}$$ and $$\mathbb{L}/\mathbb{K}$$ are separable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$\mathbb{M}/\mathbb{K}$$ is separable, then its subextension $$\mathbb{L}/\mathbb{K}$$ is separable by definition, and any element of $$\mathbb{M}$$ is separable over $$\mathbb{K}$$ ([Proposition 12](#prop12)), so viewed as an extension $$\mathbb{M}/\mathbb{L}$$ it is also separable over $$\mathbb{L}$$ ([Proposition 10](#prop10)). That is, since every element of $$\mathbb{M}$$ is separable, $$\mathbb{M}/\mathbb{L}$$ is separable by [Proposition 12](#prop12) again.

Thus the heart of this proposition is the converse. First, if $$\mathbb{M}/\mathbb{K}$$ had finite degree, then separable algebra and étale algebra are the same thing, so the claim is trivial from the third result of [§Étale Algebras, ⁋Proposition 12](/en/math/field_theory/etale_algebras#prop12). The idea of the proof is similar to the above: even if $$\mathbb{M}/\mathbb{K}$$ has infinite degree, looking at a single specific element allows us to reduce to the finite degree case.

Given any $$x\in \mathbb{M}$$ with minimal polynomial $$f\in\mathbb{L}[\x]$$, the polynomial $$f$$ is separable. Now define the subextension $$\mathbb{L}'$$ of $$\mathbb{L}/\mathbb{K}$$ to be the subextension generated by adjoining the coefficients appearing in $$f$$ to $$\mathbb{K}$$. Then $$\mathbb{L}'$$ is generated by finitely many algebraic elements, so $$\mathbb{L}'/\mathbb{K}$$ is a finite degree extension. Now $$f$$ is the minimal polynomial of $$x$$ in both $$\mathbb{L}$$ and $$\mathbb{L}'$$, and since it is separable in $$\mathbb{L}$$, it is also separable in $$\mathbb{L}'$$. That is, $$x$$ is a separable element of the extension $$\mathbb{M}/\mathbb{L}'$$, and setting $$\mathbb{M}'=\mathbb{L}'(x)$$, we have that $$\mathbb{M}'/\mathbb{L}'$$ is a finite degree separable extension, that is, a finite degree étale algebra. On the other hand, since $$\mathbb{L}/\mathbb{K}$$ is separable, its subextension $$\mathbb{L}'$$ is also separable, and therefore $$\mathbb{L}'/\mathbb{K}$$ is also a finite degree étale algebra. Hence their tower $$\mathbb{M}'/\mathbb{K}$$ is also a finite degree étale algebra, and therefore a finite degree separable extension. That is, $$x$$ is a separable element over $$\mathbb{K}$$, and since $$x$$ was chosen arbitrarily, we obtain the desired result.

</details>

<div class="proposition" markdown="1">

<ins id="prop16">**Proposition 16**</ins> Fix an appropriate extension of $$\mathbb{K}$$, and let a subextension $$\mathbb{K'}/\mathbb{K}$$ and an algebraic subextension $$\mathbb{L}/\mathbb{K}$$ of this extension be given. Then for $$\mathbb{L}'=\mathbb{K}'(\mathbb{L})$$, the following hold.

1. If $$\mathbb{L}/\mathbb{K}$$ is separable, then so is $$\mathbb{L}'/\mathbb{K}'$$.
2. Conversely, if $$\mathbb{L}'/\mathbb{K}'$$ is separable and $$\mathbb{L}/\mathbb{K}, \mathbb{K}'/\mathbb{K}$$ are linearly disjoint, then $$\mathbb{L}/\mathbb{K}$$ is also separable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. By assumption every element of $$\mathbb{L}$$ is separable over $$\mathbb{K}$$, so every element of $$\mathbb{K}'(\mathbb{L})$$ is separable over $$\mathbb{K}'$$.
2. To show this, we must prove that any finite degree subextension $$\mathbb{M}/\mathbb{K}$$ is étale. First, from the given assumption $$\mathbb{M}$$ and $$\mathbb{K}'$$ are linearly disjoint, so $$\mathbb{M}_{(\mathbb{K}')}=\mathbb{M}\otimes_\mathbb{K}\mathbb{K}'$$ is isomorphic to $$\mathbb{K}'(\mathbb{M})$$. ([§Algebraic Extensions, ⁋Proposition 10](/en/math/field_theory/algebraic_extensions#prop10)) On the other hand, since $$\mathbb{K}'(\mathbb{M})/\mathbb{K}'$$ has finite degree, it is étale from the assumption that $$\mathbb{L}'/\mathbb{K}'$$ is separable. Now since étale morphisms are stable under base change, we obtain the desired result. ([§Étale Algebras, ⁋Corollary 14](/en/math/field_theory/etale_algebras#cor14))

</details>
