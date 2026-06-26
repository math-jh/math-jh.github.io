---
title: "Separable Degree"
description: "We introduce the notion of separable degree and examine the relationship between purely inseparable extensions and separable extensions of algebraic extensions over a field of characteristic p through the lens of etale algebra conditions."
excerpt: "The decomposition of separable and inseparable degrees"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/separable_degree
drift_needed: true
sidebar: 
    nav: "field_theory-en"

date: 2025-05-17
weight: 7
translated_at: 2026-06-26T00:30:02+00:00
translation_source: kimi-cli
---
## Radical Extensions

The most inseparable extension one can conceive is, of course, a $$p$$-radical extension. For this reason, a $$p$$-radical extension is often called a *purely inseparable extension*. In this post, we first examine the relationship between $$p$$-radical extensions and separable extensions, and then explain it using the separable degree.

Let us first prove the following lemma.

<div class="proposition" markdown="1">

<ins id="lem1">**Lemma 1**</ins> For a field $$\mathbb{K}$$ of characteristic $$p\neq 0$$, a finite degree $$\mathbb{K}$$-algebra $$A$$ is étale if and only if $$A=\mathbb{K}[A^p]$$. Moreover, in this case, if $$(a_i)$$ is a $$\mathbb{K}$$-basis of $$A$$, then so is $$(a_i^p)$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Consider an algebraic closure $$\overline{\mathbb{K}}$$ of $$\mathbb{K}$$. Then for any $$u,v\in \Hom_\Alg{\mathbb{K}}(A, \overline{\mathbb{K}})$$, if the restrictions of $$u,v$$ to the subalgebra $$\mathbb{K}[A^p]$$ are equal, then the identity

$$u(x)^p=u(x^p)=v(x^p)=v(x)^p$$

holds for all $$x\in A$$, so by definition we know that the inequality

$$[A:\mathbb{K}]_s\leq[\mathbb{K}[A^p]:\mathbb{K}]_s$$

holds. If $$A$$ is an étale $$\mathbb{K}$$-algebra, then by the inequality and its equality condition in [§Étale Algebras, ⁋Proposition 13](/en/math/field_theory/etale_algebras#prop13), we have

$$[A:\mathbb{K}]=[A:\mathbb{K}]_s\leq[\mathbb{K}[A^p]:\mathbb{K}]_s\leq [\mathbb{K}[A^p]:\mathbb{K}]$$

and since $$\mathbb{K}[A^p]\subset A$$ trivially holds in general, we obtain $$A=\mathbb{K}[A^p]$$.

Conversely, assume that $$A=\mathbb{K}[A^p]$$ and let us show that $$A$$ is étale. For this, it suffices to prove the latter condition. Assuming that $$(a_i)$$ is a $$\mathbb{K}$$-basis of $$A$$, the fact that $$(a_i^p)$$ generates $$\mathbb{K}[A^p]$$ as a $$\mathbb{K}$$-vector space follows from [§Fields, ⁋Proposition 12](/en/math/field_theory/fields#prop12), and then the given assumption $$A=\mathbb{K}[A^p]$$ implies that $$(a_i^p)$$ also generates $$A$$.

Now, to use the result of [§Separable Extensions, ⁋Theorem 7](/en/math/field_theory/separable_extensions#thm7), let us show that $$\overline{\mathbb{K}}\otimes_\mathbb{K}A$$ is reduced. If $$u^2=0$$ for some $$u\in\overline{\mathbb{K}}\otimes_\mathbb{K}A$$, then $$u^p=0$$, and writing $$u=\sum \lambda_i\otimes a_i$$ we obtain

$$0=u^p=\sum_{i\in I} (\lambda_i\otimes a_i)^p=\sum_{i\in I} \lambda_i^p\otimes a_i^p$$

so each $$\lambda_i^p$$ must be $$0$$. Since $$\overline{\mathbb{K}}$$ is (of course) reduced, all $$\lambda_i$$ must be $$0$$, and hence $$u=0$$, yielding the desired result.

</details>

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Let $$\mathbb{K}$$ be a field with characteristic exponent $$p$$, and let $$\mathbb{L}/\mathbb{K}$$ be an algebraic extension. Let $$S$$ be a subset such that $$\mathbb{L}=\mathbb{K}(S)$$. If $$\mathbb{L}/\mathbb{K}$$ is separable, then $$\mathbb{L}=\mathbb{K}(S^{p^n})$$ holds for any $$n\geq 0$$. Conversely, if $$\mathbb{L}/\mathbb{K}$$ is a finite degree extension and $$\mathbb{L}=\mathbb{K}(S^p)$$, then $$\mathbb{L}/\mathbb{K}$$ is separable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

As always, there is nothing to prove when $$p=1$$. Thus it suffices to consider the case $$p\neq 1$$.

First, assuming $$\mathbb{L}=\mathbb{K}(S)$$, we have

$$\mathbb{K}(\mathbb{L}^p)=\mathbb{K}(\mathbb{K}(S)^p)=\mathbb{K}(\mathbb{K}^p(S^p))=\mathbb{K}(S^p)$$

so $$\mathbb{K}(S^p)=\mathbb{K}(\mathbb{L}^p)=\mathbb{K}[\mathbb{L}^p]$$. Applying [Lemma 1](#lem1) above with $$A=\mathbb{L}$$, the case where $$\mathbb{L}/\mathbb{K}$$ is a finite degree extension is immediate, since this is equivalent to $$\mathbb{L}$$ being an étale $$\mathbb{K}$$-algebra. Now even when $$\mathbb{L}/\mathbb{K}$$ is of infinite degree, any finite degree subextension $$\mathbb{L}'/\mathbb{K}$$ of $$\mathbb{L}/\mathbb{K}$$ is separable, so by the preceding discussion,

$$\mathbb{L}'=\mathbb{K}[(\mathbb{L}')^p]\subseteq \mathbb{K}[\mathbb{L}^p]$$

holds, and since $$\mathbb{K}[\mathbb{L}^p]$$ is the union of the $$\mathbb{L}'/\mathbb{K}$$, we obtain the desired equality. The equality for arbitrary $$n$$ follows by a simple induction.

</details>

From this we obtain the following two corollaries.

<div class="proposition" markdown="1">

<ins id="cor3">**Corollary 3**</ins> Any algebraic extension of a perfect field $$\mathbb{K}$$ is perfect.

</div>

The proof of this is almost obvious from [Proposition 2](#prop2).

Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="cor4">**Corollary 4**</ins> For a field $$\mathbb{K}$$ with algebraic closure $$\overline{\mathbb{K}}$$ and perfect closure $$\mathbb{K}^{p^{-\infty}}$$ inside it, a subextension $$\mathbb{L}/\mathbb{K}$$ of $$\overline{\mathbb{K}}/\mathbb{K}$$ is separable if and only if it is linearly disjoint from $$\mathbb{K}^{p^{-\infty}}$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

As always, it suffices to consider the case where $$\mathbb{L}/\mathbb{K}$$ is of finite degree. Given a basis $$(x_i)$$ of $$\mathbb{L}/\mathbb{K}$$, the condition that $$\mathbb{L}$$ is linearly disjoint from $$\mathbb{K}^{p^{-\infty}}$$ is equivalent to $$(x_i)$$ being linearly disjoint from every $$\mathbb{K}^{p^{-n}}$$, which is the same as saying that for any family $$(a_i)$$ and any $$n$$,

$$\sum x_i a_i^{p^{-n}}=0\implies a_i=0$$

must always hold. Now taking the $$p^n$$-th power of both sides, we see that the $$x_i^{p^n}$$ must be linearly independent, and therefore they must form a basis of $$\mathbb{L}$$; the converse also holds. Considering dimensions, this is equivalent to $$\mathbb{L}=\mathbb{K}(\mathbb{L}^p)$$, so we obtain the desired result from [Proposition 2](#prop2).

</details>

## Separable Closure

On the other hand, just as with algebraic closures or perfect closures, we can also define the separable closure. Then, just as the perfect closure in [§Fields, ⁋Theorem 15](/en/math/field_theory/fields#thm15) is the relative perfect closure with respect to the algebraic closure, it is natural to first define the relative separable closure, and then define the relative separable closure inside an algebraic closure as the (absolute) separable closure.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For a field extension $$\mathbb{L}/\mathbb{K}$$, let $$\mathbb{L}_s$$ be the set of elements that are algebraic and separable over $$\mathbb{K}$$. Then $$\mathbb{L}_s$$ is a subextension of $$\mathbb{L}/\mathbb{K}$$, and moreover it is the largest algebraic extension contained in $$\mathbb{L}$$ that is separable.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, since every element of a separable extension is separable ([§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12)), any subextension of $$\mathbb{L}$$ that is separable is always contained in $$\mathbb{L}_s$$. Conversely, an algebraic extension generated solely by separable elements is again separable by [§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12), so $$\mathbb{K}(\mathbb{L}_s)$$ is itself a separable extension; hence by the preceding claim we have $$\mathbb{K}(\mathbb{L}_s)\subseteq \mathbb{L}_s$$. Thus $$\mathbb{K}(\mathbb{L}_s)=\mathbb{L}_s$$, which shows that $$\mathbb{L}_s$$ itself is a subextension of $$\mathbb{L}/\mathbb{K}$$; combining this with the maximality observed above, we obtain that $$\mathbb{L}_s$$ is the largest separable subextension.

</details>

As mentioned above, we call $$\mathbb{L}_s$$ the *relative separable algebraic closure* (in $$\mathbb{L}/\mathbb{K}$$).

The central result of this article is that any algebraic extension always splits completely into a separable part (corresponding to the relative separable closure) and an inseparable part. This can be verified as follows.

<div class="proposition" markdown="1">

<ins id="thm6">**Theorem 6**</ins> For an algebraic extension $$\mathbb{L}/\mathbb{K}$$ and $$\mathbb{L}_s$$ defined in [Proposition 5](#prop5), the following hold.

1. $$\mathbb{L}/\mathbb{L}_s$$ is a $$p$$-radical extension.
2. For a subextension $$\mathbb{M}/\mathbb{K}$$, suppose that $$\mathbb{L}/\mathbb{M}$$ is $$p$$-radical. Then $$\mathbb{M}$$ contains $$\mathbb{L}_s$$.
3. $$\mathbb{L}_s$$ is the unique subextension of $$\mathbb{L}$$ that is separable over $$\mathbb{K}$$ and such that $$\mathbb{L}$$ is $$p$$-radical over it.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, for the first claim, the case $$\ch(\mathbb{K})=0$$ is trivial, so let us consider the case $$\ch(\mathbb{K})=p>0$$. Given $$x\in \mathbb{L}$$ and its minimal polynomial $$f$$, there exists a suitable $$m\geq 0$$ such that $$f\in\mathbb{K}[\x^{p^m}]$$ but $$f\not\in \mathbb{K}[\x^{p^{m+1}}]$$, and in this case we can choose a polynomial $$g$$ such that $$f(\x)=g(\x^{p^m})$$. Since $$f$$ is irreducible, so is $$g$$, and therefore $$g$$ is the minimal polynomial of the element $$x^{p^m}$$ over $$\mathbb{K}$$. Now, from the last equivalent condition of [§Separable Extensions, ⁋Proposition 10](/en/math/field_theory/separable_extensions#prop10), $$g$$ is separable, and therefore $$x^{p^m}$$ belongs to $$\mathbb{L}_s$$. Hence $$x$$ is $$p$$-radical over $$\mathbb{L}/\mathbb{L}_s$$, and from this we obtain the desired result.

On the other hand, given a subextension $$\mathbb{M}/\mathbb{K}$$ satisfying the second assumption, let $$x\in \mathbb{L}_s$$. Then $$x$$ is separable over $$\mathbb{K}$$, and hence also over $$\mathbb{M}$$. However, since $$\mathbb{L}/\mathbb{M}$$ is $$p$$-radical, $$x$$ is $$p$$-radical over $$\mathbb{M}$$. Again, from the last equivalent condition of [§Separable Extensions, ⁋Proposition 10](/en/math/field_theory/separable_extensions#prop10), the minimal polynomial of $$x$$ must lie in $$\mathbb{K}[\x^p]$$, but at the same time, from the condition that $$x$$ is $$p$$-radical, for the height $$e$$ of $$x$$, the polynomial $$\x^{p^e}-x^{p^e}$$ must be the minimal polynomial of $$x$$. Therefore $$e=0$$ and $$\x-x$$ must be the minimal polynomial of $$x$$, so $$x$$ must belong to $$\mathbb{M}$$.

The last claim follows from the uniqueness in [Proposition 5](#prop5).

</details>

Since the property of an algebraic extension being separable is stable under base change, if we take two subextensions $$\mathbb{L}/\mathbb{K}$$, $$\mathbb{K}'/\mathbb{K}$$ of some extension, and the relative separable closure $$\mathbb{L}_s$$ of $$\mathbb{K}$$ in $$\mathbb{L}$$, then we can verify that $$\mathbb{K}'(\mathbb{L}_s)$$ is the relative separable closure of $$\mathbb{K}'$$ in $$\mathbb{K}'(\mathbb{L})$$. Also, from the uniqueness of the relative separable closure, for a finite degree extension $$\mathbb{L}/\mathbb{K}$$ we can verify that the formula

$$\mathbb{L}_s=\bigcap_{n\geq 0} \mathbb{K}(\mathbb{L}^{p^n})$$

holds.

How to define the (absolute) separable algebraic closure is obvious.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> A field $$\mathbb{K}$$ is *separably closed* if every separable algebraic extension of $$\mathbb{K}$$ is trivial. If an extension $$\mathbb{L}$$ of a field $$\mathbb{K}$$ is separable algebraic and $$\mathbb{L}$$ is separably closed, then it is called a *separable algebraic closure* of $$\mathbb{K}$$.

</div>

Then, since any separable algebraic extension is algebraic, an algebraically closed field is always separably closed. Conversely, since any algebraic extension of a *perfect* field $$\mathbb{K}$$ is separable, a separably closed perfect field is algebraically closed.

Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Fix an algebraic closure $$\overline{\mathbb{K}}$$ of a field $$\mathbb{K}$$.

1. The relative separable algebraic closure $$\overline{\mathbb{K}}_s$$ in $$\overline{\mathbb{K}}$$ is a separable closure of $$\mathbb{K}$$.
2. The separable algebraic closure of $$\mathbb{K}$$ is uniquely determined up to isomorphism.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. $$\overline{\mathbb{K}}_s$$ is separable by [Proposition 5](#prop5), and since it is a subextension of the algebraic closure $$\overline{\mathbb{K}}$$, it is algebraic. Therefore, the claim is proved once we show that any separable algebraic extension $$\mathbb{L}/\overline{\mathbb{K}}_s$$ is trivial. Since the extension $$\mathbb{L}/\overline{\mathbb{K}}_s$$ is algebraic, there exists a unique $$\overline{\mathbb{K}}_s$$-homomorphism $$u:\mathbb{L}\rightarrow\overline{\mathbb{K}}$$ ([§Algebraic Closures, ⁋Theorem 5](/en/math/field_theory/algebraically_closed_extensions#thm5)), and its image $$u(\mathbb{L})$$ is separable algebraic by [§Separable Extensions, ⁋Proposition 15](/en/math/field_theory/separable_extensions#prop15), so $$u(\mathbb{L})=\overline{\mathbb{K}}_s$$ holds.
2. Similarly, this follows by using [§Algebraic Closures, ⁋Theorem 5](/en/math/field_theory/algebraically_closed_extensions#thm5).

</details>

From this, we know that the separable algebraic closure is the smallest separably closed algebraic extension. That is, if $$\mathbb{L}/\mathbb{K}$$ is a separable algebraic closure of $$\mathbb{K}$$, and for a field extension $$\mathbb{M}/\mathbb{K}$$ the field $$\mathbb{M}$$ is separably closed, then there exists a unique morphism $$\mathbb{L}\rightarrow\mathbb{M}$$.

## Separable Degree

By [Theorem 6](#thm6), any finite degree extension $$\mathbb{L}/\mathbb{K}$$ can be split into a separable part and a non-separable part, written as $$\mathbb{L}/\mathbb{L}_s/\mathbb{K}$$.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> In the above situation, $$[\mathbb{L}:\mathbb{K}]_s=[\mathbb{L}_s:\mathbb{K}]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By definition, $$[\mathbb{L}:\mathbb{K}]_s$$ is the number of $$\mathbb{K}$$-algebra homomorphisms from $$\mathbb{L}$$ to $$\overline{\mathbb{K}}$$, where $$\overline{\mathbb{K}}$$ is an algebraic closure of $$\mathbb{K}$$. Since $$\overline{\mathbb{K}}$$ is an algebraically closed field, it is a perfect field, and therefore by [§Radical Extensions, ⁋Proposition 6](/en/math/field_theory/radical_extensions#prop6), for any given $$\mathbb{K}$$-algebra homomorphism $$\mathbb{L} \rightarrow \overline{\mathbb{K}}$$ there is a unique extension $$\mathbb{L}_s\rightarrow \overline{\mathbb{K}}$$, and conversely, for any given $$\mathbb{K}$$-algebra homomorphism $$\mathbb{L}_s \rightarrow \overline{\mathbb{K}}$$ we can restrict it to $$\mathbb{L}$$ to obtain $$\mathbb{L}\rightarrow\overline{\mathbb{K}}$$. From this we obtain the equality

$$[\mathbb{L}:\mathbb{K}]_s=[\mathbb{L}_s:\mathbb{K}]_s$$

On the other hand, since $$\mathbb{L}_s/\mathbb{K}$$ is a finite degree separable extension, it is an étale algebra, and therefore by [§Étale Algebras, ⁋Proposition 13](/en/math/field_theory/etale_algebras#prop13) we have $$[\mathbb{L}_s:\mathbb{K}]_s=[\mathbb{L}_s:\mathbb{K}]$$, yielding the desired result.

</details>

Therefore it is justified to call $$[\mathbb{L}:\mathbb{K}]_s$$ the *separable degree*. Moreover, from the formula

$$[\mathbb{L}:\mathbb{K}]=[\mathbb{L}:\mathbb{L}_s][\mathbb{L}_s:\mathbb{K}]=[\mathbb{L}:\mathbb{K}]_s[\mathbb{L}:\mathbb{L}_s]$$

we can define the *inseparable degree* of the extension $$\mathbb{L}/\mathbb{K}$$ as $$[\mathbb{L}:\mathbb{K}]_i=[\mathbb{L}:\mathbb{L}_s]$$.

If $$\ch\mathbb{K}=0$$, then $$[\mathbb{L}:\mathbb{K}]_i=1$$ always holds, and if $$\ch\mathbb{K}=p$$, then $$[\mathbb{L}:\mathbb{K}]_i$$ is always a power of $$p$$. ([Theorem 6](#thm6)) However, since there are plenty of polynomials of degree $$p^e$$ that do not define a $$p$$-radical extension, there is no way to determine the value of $$[\mathbb{L}:\mathbb{K}]_i$$ from (say) $$[\mathbb{L}:\mathbb{K}]$$ alone.

Nevertheless, the following still holds.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Fix an extension $$\Omega/\mathbb{K}$$, and consider two finite degree subextensions $$\mathbb{L}/\mathbb{K}$$, $$\mathbb{M}/\mathbb{K}$$ of $$\Omega$$. The following hold.

1. If $$\mathbb{L}\subseteq \mathbb{M}$$, then $$[\mathbb{M}:\mathbb{K}]_s=[\mathbb{M}:\mathbb{L}]_s[\mathbb{L}:\mathbb{K}]_s$$ and $$[\mathbb{M}:\mathbb{K}]_i=[\mathbb{M}:\mathbb{L}]_i[\mathbb{L}:\mathbb{K}]_i$$.
2. For any subextension $$\mathbb{K}'$$ of $$\Omega$$, the inequalities

    $$[\mathbb{K}'(\mathbb{L}):\mathbb{K}']_s\leq [\mathbb{L}:\mathbb{K}]_s,\qquad [\mathbb{K}'(\mathbb{L}):\mathbb{K}']_i\leq [\mathbb{L}:\mathbb{K}]_i$$

    hold, and equality holds when $$\mathbb{K}'$$ and $$\mathbb{L}$$ are linearly disjoint.
3. The two inequalities

    $$[\mathbb{K}(\mathbb{L}\cup \mathbb{M}):\mathbb{K}]_s\leq [\mathbb{L}:\mathbb{K}]_s[\mathbb{M}:\mathbb{K}]_s,\qquad [\mathbb{K}(\mathbb{L}\cup \mathbb{M}):\mathbb{K}]_i\leq [\mathbb{L}:\mathbb{K}]_i[\mathbb{M}:\mathbb{K}]_i$$

    hold, and equality holds when $$\mathbb{L}$$ and $$\mathbb{M}$$ are linearly disjoint.

</div>

The proofs of these are almost tautological; for example, the first result follows from [§Algebraic Extensions, ⁋Proposition 2](/en/math/field_theory/algebraic_extensions#prop2) and [§Étale Algebras, ⁋Proposition 12](/en/math/field_theory/etale_algebras#prop12). The remaining results also hold naturally for the inseparable degree, since analogous results hold for the extension degree and the separable degree.
