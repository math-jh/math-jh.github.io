---
title: "Radical Extensions"
description: "This post introduces the basic ideas of Galois theory through the example of quadratic extension fields. It covers the process of defining the Galois group as the action that permutes the roots of polynomials in well-behaved field extensions."
excerpt: "The definition of radical extensions and their role in Galois theory"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/radical_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-05-15
weight: 4
published: false
translated_at: 2026-05-31T05:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T05:30:03+00:00
---
Let us look at the broad theme of Galois theory we will study through a very simple example. Consider the degree $$4$$ extension $$\mathbb{Q}(\sqrt{2}, \sqrt{3})$$ of $$\mathbb{Q}$$. The newly adjoined elements $$\sqrt{2}$$ and $$\sqrt{3}$$ arise from the minimal polynomials with rational coefficients

$$\x^2-2,\qquad \x^2-3$$

However, each of these polynomials has two roots $$\pm \sqrt{2}$$ and $$\pm\sqrt{3}$$, and there is no algebraic way to distinguish these roots over $$\mathbb{Q}$$. Therefore, if we consider the action that interchanges these roots—or equivalently, the $$\mathbb{Q}$$-automorphisms of $$\mathbb{Q}(\sqrt{2},\sqrt{3})$$—that is, if we consider the permutation group $$S_2\times S_2$$, this is a subgroup of $$S_4$$.

In this way, whenever a polynomial is given we can define an appropriate Galois group, and the philosophy of Galois theory is that studying these groups allows us to classify extensions of $$\mathbb{Q}$$.

However, if we pursue this philosophy, defining a permutation action becomes quite awkward when a minimal polynomial has a repeated root. This is a false alarm over $$\mathbb{Q}$$, but in some cases such a thing can actually happen.

<div class="remark" markdown="1">

**Remark** Every field appearing in this post has characteristic exponent $$p$$.

</div>

## $$p$$-Radical Extensions

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a field extension $$\mathbb{L}/\mathbb{K}$$, an element $$x\in \mathbb{L}$$ is called *$$p$$-radical* if there exists some $$m\geq 0$$ such that $$x^{p^m}\in \mathbb{K}$$. The smallest such $$m$$ is called the *height* of $$x$$.

</div>

If $$p=1$$, the above definition is essentially meaningless, and the same holds for the rest of the content in this post. In other words, the content of this post is essentially all about fields of characteristic $$p$$.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> Fix a field extension $$\mathbb{L}/\mathbb{K}$$ and a $$p$$-radical element $$x\in \mathbb{K}$$ of height $$e$$. Then for $$a=x^{p^e}\in \mathbb{K}$$, the minimal polynomial of $$x$$ is given by

$$\x^{p^e}-a\in \mathbb{K}[\x]$$

Hence $$[\mathbb{K}(x):\mathbb{K}]=p^e$$.

</div>

We write the image of the Frobenius endomorphism $$\Frob_p:\mathbb{K}\rightarrow \mathbb{K}$$ as $$\mathbb{K}^p$$. By the minimality of $$e$$, we have $$a\not\in \mathbb{K}^p$$, so the claim follows from the next lemma.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> Suppose an element $$a$$ of a field $$\mathbb{K}$$ satisfies $$a\not\in \mathbb{K}^p$$. Then for any $$e\geq 0$$, the polynomial $$f(\x)=\x^{p^e}-a$$ is irreducible in $$\mathbb{K}[\x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>



</details>

The following definition would have been natural even immediately after [Definition 1](#def1).

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> A field extension $$\mathbb{L}/\mathbb{K}$$ is called *$$p$$-radical* if every element of $$\mathbb{L}$$ is $$p$$-radical. If there exists an integer $$e$$ such that $$x^{p^e}\in \mathbb{K}$$ holds for *all* elements $$x$$ of $$\mathbb{L}$$, the smallest such $$e$$ is called the *height* of $$\mathbb{L}$$.

</div>

Thus the height of $$\mathbb{L}/\mathbb{K}$$, if defined, can be thought of as the maximum of the heights of the elements of $$\mathbb{L}$$. Also, by [Proposition 2](#prop2), any $$p$$-radical extension is naturally an algebraic extension.

If the Frobenius endomorphism $$\Frob_p:A\rightarrow A$$ is a bijection, we called $$A$$ a *perfect ring*. Therefore, if $$\mathbb{K}$$ were a perfect field, then $$\mathbb{K}^p=\mathbb{K}$$, so any $$p$$-radical extension of a perfect field must be itself. Moreover, it is obvious from the definition that the compositum of $$p$$-radical extensions is $$p$$-radical. The following proposition concerns the existence of a (relative) $$p$$-radical closure.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Fix a field extension $$\mathbb{L}/\mathbb{K}$$, and for each $$n\geq 0$$ define

$$\mathbb{L}_n=\{x\in \mathbb{L}\mid\text{$x$ is $p$-radical of height $\leq n$}\}$$

Then the union $$\mathbb{L}_\infty$$ of the increasing sequence $$\mathbb{L}_n$$ is the largest $$p$$-radical subextension of $$\mathbb{L}$$ containing $$\mathbb{K}$$.

</div>

The proof of this is essentially obvious.

In the previous post we saw that any field $$\mathbb{K}$$ has an algebraic closure $$\overline{\mathbb{K}}$$. Thus in [Proposition 5](#prop5) we may take $$\mathbb{L}=\overline{\mathbb{K}}$$. Then $$\overline{\mathbb{K}}$$ is a perfect field, and moreover we know that for each $$n$$, $$\overline{\mathbb{K}}_n$$ is exactly $$\mathbb{K}^{p^{-n}}$$. Let us write the (relative) $$p$$-radical closure in this situation as $$\mathbb{K}^{p^{-\infty}}$$. This is exactly the same as [§Fields, ⁋Theorem 15](/en/math/field_theory/fields#thm15). If $$\mathbb{K}$$ is imperfect, that is, if $$\mathbb{K}\neq \mathbb{K}^p$$, then the above ascending sequence is strictly increasing, and hence $$\mathbb{K}^{p^{-\infty}}/\mathbb{K}$$ becomes an extension of infinite degree.

On the other hand, the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Suppose a field extension $$\mathbb{L}/\mathbb{K}$$ is a $$p$$-radical extension, and a homomorphism $$u$$ from $$\mathbb{K}$$ to some perfect field $$\mathbb{F}$$ is given. Then there exists a unique homomorphism $$v:\mathbb{L} \rightarrow \mathbb{F}$$ extending $$u$$.

</div>

Hence the following holds.

<div class="proposition" markdown="1">

<ins id="cor7">**Corollary 7**</ins> A field extension $$\mathbb{L}/\mathbb{K}$$ is the perfect closure of $$\mathbb{K}$$ if and only if $$\mathbb{L}$$ is a $$p$$-radical extension of $$\mathbb{K}$$ and $$\mathbb{L}$$ is a perfect field.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> 

</div>

We close this post by introducing the counterexample mentioned in the introduction.

<div class="example" markdown="1">

<ins id="ex9">**Example 9**</ins> Consider the field $$\mathbb{K}=\mathbb{F}_p(t)$$. Then consider the polynomial $$u(\x)=\x^p-t\in \mathbb{K}[\x]$$, and through this we can consider the $$p$$-radical extension $$\mathbb{L}=\mathbb{K}[\x]/(\x^p-t)$$. Then the minimal polynomial of a root $$\alpha$$ of $$u(\x)=0$$ in $$\mathbb{L}$$ must be $$u(\x)$$ itself ([Proposition 2](#prop2)), and differentiating this gives $$Du=p\x^{p-1}=0$$, so by [\[Ring Theory\] §Polynomial Rings, ⁋Proposition 11](/en/math/ring_theory/polynomial_rings#prop11) we know that $$\alpha$$ is a repeated root of $$u$$. In fact, by [§Fields, ⁋Theorem 10](/en/math/field_theory/fields#thm10) we have $$(\x-\alpha)^p=\x^p-\alpha^p=\x^p-t$$, so $$\alpha$$ has multiplicity $$p$$.

</div>

In the next post and the one after that, we will see how to exclude such cases from our discussion.
