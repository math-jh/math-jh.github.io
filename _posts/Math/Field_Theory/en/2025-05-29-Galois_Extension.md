---
title: "Galois Extensions"
excerpt: "The definition of a Galois extension satisfying both normal and separable"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/galois_extension
header:
    overlay_image: /assets/images/Math/Field_Theory/Galois_Extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-en"

date: 2025-05-29
last_modified_at: 2025-05-29
weight: 8
translated_at: 2026-05-20T12:30:01+00:00
translation_source: kimi-cli
---
We are now ready to define what a Galois extension is, but before that we first examine the following proposition.

<div class="proposition" markdown="1">

<ins id="prop1">**Proposition 1**</ins> Consider an algebraic extension $$\mathbb{L}$$ and an inclusion $$u:\mathbb{L}\rightarrow \overline{\mathbb{K}}$$.

1. If $$u(\mathbb{L})\subseteq \mathbb{L}$$, then $$u$$ is a $$\mathbb{K}$$-automorphism from $$\mathbb{L}$$ to $$\mathbb{L}$$.
2. There exists a $$\mathbb{K}$$-automorphism of $$\overline{\mathbb{K}}$$ extending $$u$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. For any $$x\in E$$, let $$f$$ be the minimal polynomial of $$x$$. Let $$\Phi$$ be the set of roots of $$f$$ in $$\mathbb{L}$$; then $$\Phi$$ is a finite set. Moreover, if $$\alpha\in\Phi$$ then

    $$0=u(0)=u(f(\alpha))=f(u(\alpha))$$
    
    and so $$u(\Phi)\subseteq\Phi$$ holds. But $$u$$ is not the zero map, hence it is injective ([§Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2)), and therefore $$u$$ is a bijection from $$\Phi$$ to $$\Phi$$. Thus $$x\in\Phi=u(\Phi)\subseteq u(E)$$, and from this $$u(E)=E$$.

2. Since $$\overline{\mathbb{K}}$$ is an algebraic closure of both $$u(\mathbb{L})$$ and $$\mathbb{L}$$, we obtain the desired result from the universal property of [§Algebraic Closures, ⁋Theorem 5](/en/math/field_theory/algebraically_closed_extensions#thm5).

</details>

Our goal is to examine all algebraic extensions of a fixed field $$\mathbb{K}$$, or more precisely, to look at equivalence classes of algebraic extensions.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> For two algebraic extensions $$\mathbb{L}$$, $$\mathbb{M}$$ of a field $$\mathbb{K}$$, if there exists a $$\mathbb{K}$$-automorphism $$u:\overline{\mathbb{K}}\rightarrow \overline{\mathbb{K}}$$ such that $$u(\mathbb{L})=\mathbb{M}$$, we say they are *conjugate*. In particular, two elements $$x,y\in\overline{\mathbb{K}}$$ are said to be *conjugate* if there exists a $$\mathbb{K}$$-automorphism $$u: \overline{\mathbb{K}}\rightarrow \overline{\mathbb{K}}$$ such that $$u(x)=y$$.

</div>

By [Proposition 1](#prop1), if $$\mathbb{M}$$ and $$\mathbb{L}$$ are isomorphic extensions of $$\mathbb{K}$$, then they are conjugate extensions, and by definition conjugate extensions are isomorphic. Moreover, the following holds.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Fix two elements $$x,y$$ of $$\overline{\mathbb{K}}$$. The following hold.

1. $$x,y$$ are conjugate elements.
2. There exists a suitable $$\mathbb{K}$$-isomorphism $$v: \mathbb{K}(x) \rightarrow \mathbb{K}(y)$$ satisfying $$v(x)=y$$.
3. $$x$$ and $$y$$ have the same minimal polynomial.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First assume the first condition. Let $$f$$ be the minimal polynomial of $$x$$; then

$$f(y)=f(u(x))=u(f(x))=u(0)=0$$

so the minimal polynomial of $$y$$ divides $$f$$. By the same logic the minimal polynomial of $$x$$ divides that of $$y$$, and therefore they are equal.

On the other hand, if $$x,y$$ have the same minimal polynomial $$f$$, then by the first isomorphism theorem

$$\mathbb{K}(x)\cong \mathbb{K}[\x]/(f)\cong \mathbb{K}(y)$$

so it is obvious that the third condition implies the second. Finally, assuming the second condition, [Proposition 1](#prop1) yields a $$\mathbb{K}$$-isomorphism $$u:\overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$$ extending $$v$$, and thus $$x$$, $$y$$ are conjugate.

</details>

From this, if an algebraic element $$x\in \overline{\mathbb{K}}$$ of degree $$n$$ is given, we know that elements conjugate to $$x$$ must be roots of the minimal polynomial of $$x$$, and therefore there are at most $$n$$ such elements. Moreover, the fact that there are *fewer* than $$n$$ elements conjugate to $$x$$ is equivalent to the minimal polynomial of $$x$$ not being separable. That is, denoting the group of $$\mathbb{K}$$-automorphisms of $$\overline{\mathbb{K}}$$ by $$\Aut_\mathbb{K}(\overline{\mathbb{K}})$$ and letting $$\Aut_\mathbb{K}\overline{\mathbb{K}}$$ act on $$\overline{\mathbb{K}}$$ in the natural way, the set of elements fixed by this action, $$\overline{\mathbb{K}}^{\Aut_{\mathbb{K}}(\overline{\mathbb{K}})}$$, is exactly $$\mathbb{K}^{p^{-\infty}}$$.

## Galois Extensions

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A field extension $$\mathbb{L}/\mathbb{K}$$ is called a *quasi-Galois extension* or *normal extension* if $$\mathbb{L}/\mathbb{K}$$ is algebraic and any irreducible polynomial $$f\in \mathbb{K}[\x]$$ having a root in $$\mathbb{L}$$ splits into a product of linear factors in $$\mathbb{L}[\x]$$.

</div>

Thus, essentially a quasi-Galois extension is nothing but another name for a splitting field.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For an algebraic extension $$\mathbb{L}/\mathbb{K}$$, the following are all equivalent.

1. $$\mathbb{L}/\mathbb{K}$$ is quasi-Galois.
2. For any $$x\in \mathbb{L}$$, all conjugates of $$x$$ (in $$\overline{\mathbb{K}}$$) belong to $$\mathbb{L}$$.
3. Any $$\mathbb{K}$$-automorphism of $$\overline{\mathbb{K}}$$ sends $$\mathbb{L}$$ to $$\mathbb{L}$$,
4. Any $$\mathbb{K}$$-homomorphism from $$\mathbb{L}$$ to $$\overline{\mathbb{K}}$$ maps into $$\mathbb{L}$$.
5. $$\mathbb{L}$$ is the splitting field of some family of non-constant polynomials $$(f_i\in \mathbb{K}[\x])$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

First, the equivalence of the third and fourth conditions follows from [Proposition 1](#prop1). On the other hand, since a quasi-Galois extension can be viewed as the splitting field of the minimal polynomials of its elements, the last condition is implied by the first. Meanwhile, if the last condition holds, then by the same logic as in [Proposition 1](#prop1) any $$\mathbb{K}$$-automorphism of $$\overline{\mathbb{K}}$$ sends roots of $$f_i$$ to roots of $$f_i$$, and therefore sends $$\mathbb{L}$$ to $$\mathbb{L}$$. Hence the third condition holds. Also, it is obvious from the definition that the third condition implies the second. Therefore

$$(1)\implies (5)\implies (3)\iff (4)\implies (2)$$

so it suffices to show $$(2)\implies (1)$$. To this end, let $$f\in \mathbb{K}[\x]$$ be a (monic) irreducible polynomial having a root in $$\mathbb{L}$$. Then since $$\overline{\mathbb{K}}$$ is algebraically closed, $$f$$ is expressed in $$\overline{\mathbb{K}}$$ by the following formula

$$f(\x)=\prod_{i=1}^d (\x- a_i), \qquad a_i\in \overline{\mathbb{K}}$$

. Now each $$a_i$$ is a conjugate, and therefore by assumption they must all belong to $$\mathbb{L}$$.

</details>

From this the following hold.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6**</ins> The following hold.

1. An algebraic extension $$\mathbb{L}/\mathbb{K}$$ is quasi-Galois if and only if any conjugate of $$\mathbb{L}$$ is itself.
2. For an algebraic extension $$\mathbb{K}\subseteq \mathbb{L}\subseteq \mathbb{M}$$, if $$\mathbb{M}/\mathbb{K}$$ is quasi-Galois then $$\mathbb{L}/\mathbb{K}$$ is also quasi-Galois.
3. Let a quasi-Galois extension $$\mathbb{M}/\mathbb{K}$$ and its subextension $$\mathbb{L}/\mathbb{K}$$ be given. Then for any $$\mathbb{K}$$-homomorphism $$u: \mathbb{L}\rightarrow \overline{\mathbb{K}}$$ we have $$u(\mathbb{L})\subseteq \mathbb{M}$$, and there exists a $$\mathbb{K}$$-automorphism $$v$$ of $$\mathbb{M}$$ extending this.
4. For any field extension $$\mathbb{K}'/\mathbb{K}$$ and quasi-Galois extension $$\mathbb{L}/\mathbb{K}$$, the compositum $$\mathbb{K}'(\mathbb{L})$$ is quasi-Galois over $$\mathbb{K}'$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. By [Proposition 5](#prop5), $$\mathbb{L}/\mathbb{K}$$ being quasi-Galois is equivalent to every $$\mathbb{K}$$-automorphism of $$\overline{\mathbb{K}}$$ sending $$\mathbb{L}$$ to $$\mathbb{L}$$.
2. Suppose $$\mathbb{M}/\mathbb{K}$$ is quasi-Galois. Then since $$\overline{\mathbb{K}}$$ is also an algebraic closure of $$\mathbb{L}$$, by [Proposition 5](#prop5) it suffices to show that for any $$\mathbb{L}$$-automorphism $$u: \overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$$ we have $$u(\mathbb{M})=\mathbb{M}$$. But $$\mathbb{M}$$ is a quasi-Galois extension of $$\mathbb{K}$$, and $$u$$ is an $$\mathbb{L}$$-automorphism, so it is automatically a $$\mathbb{K}$$-automorphism as well. From this we see that $$u$$ must satisfy the desired condition.
3. From [Proposition 1](#prop1) we know that there exists a $$\mathbb{K}$$-automorphism $$v:\overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$$ extending $$u$$. Then its restriction to $$\mathbb{M}$$ must satisfy $$v(\mathbb{M})=\mathbb{M}$$ by the assumption that $$\mathbb{M}$$ is quasi-Galois, and therefore the desired claim holds.
4. If $$\mathbb{L}$$ is the splitting field of the $$f_i\in \mathbb{K}[\x]$$, then $$\mathbb{L}'$$ is the splitting field of the $$f_i\in \mathbb{K}'[\x]$$.

</details>

As can be seen from the proof of the above corollary, the most important property characterizing a quasi-Galois extension $$\mathbb{L}/\mathbb{K}$$ is that any $$\mathbb{K}$$-automorphism sends $$\mathbb{L}$$ to $$\mathbb{L}$$. The next proposition is also obvious from this fact.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> Let $$\mathbb{L}_i$$ be quasi-Galois extensions inside an algebraic closure $$\overline{\mathbb{K}}$$ of $$\mathbb{K}$$. Then both $$\bigcap \mathbb{L}_i$$ and $$\mathbb{K}(\bigcup \mathbb{L}_i)$$ are quasi-Galois.

</div>

In particular, for any set $$S$$ of elements of $$\overline{\mathbb{K}}$$, we can consider the smallest quasi-Galois extension containing it. By definition, this is the extension of $$\mathbb{K}$$ generated by all conjugates of each element of $$S$$. We call this the quasi-Galois extension generated by $$S$$.

In [Definition 4](#dzef3), when we defined a quasi-Galois extension, we required that an irreducible polynomial $$f$$ split into a product of linear factors, but we did not require them to be distinct. A Galois extension is obtained by adding the separability condition.

<div class="proposition" markdown="1">

<ins id="thm8">**Theorem 8**</ins> Let an algebraic extension $$\mathbb{L}/\mathbb{K}$$ and the group $$\Gamma$$ of $$\mathbb{K}$$-automorphisms of $$\mathbb{L}$$ be given. The following are all equivalent.

1. Every $$\Gamma$$-invariant element of $$\mathbb{L}$$ is an element of $$\mathbb{K}$$.
2. $$\mathbb{L}$$ is a separable quasi-Galois extension of $$\mathbb{K}$$.
3. For any $$x\in \mathbb{L}$$, the minimal polynomial $$f\in \mathbb{K}[\x]$$ of $$x$$ splits into a product of distinct linear factors in $$\mathbb{L}[\x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Since the equivalence of the second and third conditions is obvious, it suffices to show that these are equivalent to the first.

First assume the first condition. We must show that for any $$x\in \mathbb{L}$$ and its minimal polynomial $$f\in \mathbb{K}[\x]$$, $$f$$ splits into a product of distinct linear factors in $$\mathbb{L}[\x]$$. To this end, let $$S$$ be the set of all roots of $$f$$ in $$\mathbb{L}$$, and define a new polynomial

$$g(\x)=\prod_{a\in S}(\x-a)$$

Then $$g$$ is an element of $$\mathbb{L}[\x]$$, and for any $$\sigma\in\Gamma$$

$$(\sigma\cdot g)(\x)=\prod_{a\in S}(\x-\sigma(a))=\prod_{a\in S}(\x-a)$$

so the coefficients of $$g$$ are unchanged by $$\sigma$$, and therefore by the assumption of the first condition we have $$g\in\mathbb{K}
[\x]$$. Now since $$g(x)=0$$, by [§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15) we know that $$g$$ divides $$f$$, and considering their degrees we must have $$g=f$$. That is, the third condition holds.

Conversely, assume the third condition and let us prove the first. If $$x\in\mathbb{L}$$ does not belong to $$\mathbb{K}$$, we must show that there exists $$\sigma\in\Gamma$$ sending $$x$$ to a different element. Let $$f$$ be the minimal polynomial of $$x$$. Since $$x\not\in\mathbb{K}$$, $$f$$ has degree at least $$2$$, and by assumption

$$f(\x)=\prod_{a\in S}(\x-a), \qquad \text{$S$ the set of comjugates of $x$ in $\overline{\mathbb{K}}$}$$

it splits in this way, and on the other hand since $$\mathbb{L}/\mathbb{K}$$ is quasi-Galois there exists a $$\mathbb{K}$$-automorphism $$u$$ of $$\overline{\mathbb{K}}$$ sending $$x$$ to some $$a\in S$$ different from itself, which is by [Proposition 5](#prop5) a $$\mathbb{K}$$-automorphism of $$\mathbb{L}$$. From this we obtain the desired result.

</details>

We may now define the following.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> An algebraic extension $$\mathbb{L}/\mathbb{K}$$ is called *Galois* if $$\mathbb{L}/\mathbb{K}$$ satisfies the conditions of [Proposition 8](#prop8).

</div>

Then from the result of [Proposition 7](#prop7) and the result on separable extensions we obtain the following two propositions.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Let $$\mathbb{L}_i$$ be Galois extensions inside an algebraic closure $$\overline{\mathbb{K}}$$ of $$\mathbb{K}$$. Then both $$\bigcap \mathbb{L}_i$$ and $$\mathbb{K}(\bigcup \mathbb{L}_i)$$ are Galois.
 
</div>

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Let a Galois extension $$\mathbb{L}/\mathbb{K}$$ and a finite degree subextension $$\mathbb{M}/\mathbb{K}$$ be given. Then there exists a suitable subextension $$\mathbb{N}/\mathbb{K}$$ of $$\mathbb{L}/\mathbb{K}$$ containing $$\mathbb{M}$$ such that $$\mathbb{N}/\mathbb{K}$$ is Galois of finite degree.

</div>

## Galois Groups

As we have already seen, an important tool in studying a Galois extension $$\mathbb{L}/\mathbb{K}$$ is the collection of $$\mathbb{K}$$-automorphisms of $$\mathbb{L}$$.

<div class="definition" markdown="1">
 
<ins id="def12">**Definition 12**</ins> For a Galois extension $$\mathbb{L}/\mathbb{K}$$, the group of $$\mathbb{K}$$-automorphisms of $$\mathbb{L}$$ is called the *Galois group* and is denoted by $$\Gal(\mathbb{L}/\mathbb{K})$$.

</div> 

In particular, fix a field $$\mathbb{K}$$ and consider its algebraic closure $$\overline{\mathbb{K}}$$. For a separable polynomial $$f\in \mathbb{K}[\x]$$ and the set $$A$$ of roots of $$f$$, we have already seen that $$\mathbb{L}=\mathbb{K}(A)$$ is a Galois extension of $$\mathbb{K}$$. Now since $$\mathbb{L}$$ is generated by $$S$$, any $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$ is completely determined by its values on $$A$$, and from this we obtain an injective group homomorphism

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow S_A$$

is induced. In general this homomorphism need not be surjective. That is, among the roots of an arbitrary separable polynomial $$f$$ there may be elements that are not conjugate, and by [Proposition 3](#prop3) this is equivalent to these two roots $$x,y$$ having different minimal polynomials. On the other hand, if $$x,y$$ are roots of $$f$$, then by [§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15) their minimal polynomials each divide $$f$$, and therefore $$x$$ and $$y$$ are roots of distinct irreducible factors of $$f$$. From this we can even determine what the image of the above injective homomorphism looks like.

On the other hand, for a Galois extension $$\mathbb{L}/\mathbb{K}$$ and another Galois extension $$\mathbb{M}/\mathbb{K}$$ that is a subextension of $$\mathbb{L}$$, we obtain the following result from [Proposition 1](#prop1).

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> In the above situation the restriction homomorphism

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K});\qquad \sigma\mapsto \sigma\vert_\mathbb{M}$$

is surjective.

</div>
