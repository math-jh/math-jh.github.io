---
title: "Algebraic Extensions"
description: "We cover the definition of field extensions and the perspective of interpreting a field extension as an associative algebra."
excerpt: "The definition and degree of algebraic extensions of fields"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/algebraic_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-04-26
last_modified_at: 2025-04-26
weight: 2
translated_at: 2026-05-31T04:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-05-31T04:00:04+00:00
---
## Field Extensions

We saw in [§Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2) that a morphism between fields is either injective or the zero map. In this post we examine the former case.

We call an injective field morphism a *field extension*. Then, for a fixed field $$\mathbb{K}\in\Field$$, the under category of $$\mathbb{K}$$ becomes the category of extensions of $$\mathbb{K}$$.

Although this notation differs slightly from that of [§Categories, ⁋Example 13](/en/math/category_theory/categories#ex13), we often denote a field extension $$\mathbb{K}\rightarrow \mathbb{L}$$ by $$\mathbb{L}/\mathbb{K}$$. Then, whenever a field extension $$\mathbb{L}/\mathbb{K}$$ is given, we can identify $$\mathbb{K}$$ with a subfield of $$\mathbb{L}$$ via the injective map $$\mathbb{K}\hookrightarrow\mathbb{L}$$. However, if $$\mathbb{L}=\mathbb{K}$$ and $$\mathbb{K}\hookrightarrow\mathbb{L}=\mathbb{K}$$ is an endomorphism, such an identification may cause confusion, so in this case we do not identify $$\mathbb{K}$$ with a subfield of $$\mathbb{L}$$.

By definition, given two extensions $$\mathbb{K} \rightarrow \mathbb{L}_1$$ and $$\mathbb{K} \rightarrow \mathbb{L}_2$$, the following commutative diagram

![morphism_of_field_extensions](/assets/images/Math/Field_Theory/Algebraic_Extensions-1.png){:style="width:10em" class="invert" .align-center}

is a morphism between them. Here, since both $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are fields, the morphism $$\mathbb{L}_1 \rightarrow \mathbb{L}_2$$ must be injective. Subject to the caution above, in this case we call $$\mathbb{L}_1$$ a *subextension* of $$\mathbb{L}_2$$.

Thus any field extension $$\mathbb{L}/\mathbb{K}$$ can be regarded as an associative unital $$\mathbb{K}$$-algebra (which is itself a field).

<div class="remark" markdown="1">

**Remark**</ins> We consider $$\mathbb{K}$$-algebras and homomorphisms between them in order to treat situations similar to the above; henceforth in our posts the category $$\Alg{\mathbb{K}}$$ will always be the category of unital associative $$\mathbb{K}$$-algebras. That is, by a $$\mathbb{K}$$-algebra we shall always mean a unital associative $$\mathbb{K}$$-algebra, and by a $$\mathbb{K}$$-algebra homomorphism we shall always mean a unital $$\mathbb{K}$$-algebra homomorpihsm.

</div>

Any $$\mathbb{K}$$-algebra is also a $$\mathbb{K}$$-module, so its dimension is well-defined. ([§Basis, ⁋Proposition 6](/en/math/multilinear_algebra/basis_of_free_modules#prop6))

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For any $$\mathbb{K}$$-algebra $$A$$, we call $$\dim_{\mathbb{K}}A$$ the *degree* of $$A$$ and denote it by $$[A:\mathbb{K}]$$.

</div>

Then the following is obvious from the definition.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For a field extension $$\mathbb{L}_2/\mathbb{L}_1/\mathbb{K}$$, the equality $$[\mathbb{L}_2:\mathbb{K}]=[\mathbb{L}_2:\mathbb{L}_1][\mathbb{L}_1:\mathbb{K}]$$ holds.

</div>

More generally, for a field $$\mathbb{K}$$ and any $$\mathbb{K}$$-algebra $$E$$, we can define $$[E:\mathbb{K}]$$ as $$\dim_\mathbb{K}E$$. Then the following proposition is simple linear algebra.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> For a finite degree $$\mathbb{K}$$-algebra $$E$$, if $$x\in E$$ is a non-zerodivisor in $$E$$, then $$x$$ is an invertible element of $$E$$.

</div>
<details class="proof">
<summary>Proof</summary>

By assumption $$E$$ is a finite-dimensional $$\mathbb{K}$$-algebra, and since $$x$$ is a non-zerodivisor in $$E$$, the map

$$E \rightarrow E;\qquad y\mapsto xy$$

is injective. Since $$E$$ is finite-dimensional, for this linear map injectivity is equivalent to surjectivity; hence there exists $$y\in E$$ such that $$xy=1$$, yielding the desired result.

</details>

In particular, if a finite-dimensional $$\mathbb{K}$$-algebra $$E$$ is an integral domain, then $$E$$ is necessarily a field.

Meanwhile, for any ring $$A$$, we have denoted by $$A[\x]$$ the polynomial ring in the variable $$\x$$ with coefficients in $$A$$, which can be thought of as the smallest algebra containing $$A$$ and the variable $$\x$$. Similarly, to adjoin an element $$\x$$ to a field $$\mathbb{K}$$, we must also adjoin its inverses.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> For a field extension $$\mathbb{L}/\mathbb{K}$$ and a subset $$A\subseteq \mathbb{L}$$, we denote by $$\mathbb{K}(A)$$ the smallest subextension of $$\mathbb{L}$$ containing $$A$$.

</div>

In this definition, $$\mathbb{L}$$ is needed only to define $$A$$, and regardless of what $$\mathbb{L}$$ actually is, $$\mathbb{K}(A)$$ will be an isomorphic field. For this reason, we often fix a (very large) field extension $$\Omega$$ of $$\mathbb{K}$$ (without worrying about what $$\Omega$$ is) and consider subsets $$M,N$$ of this extension.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> For two subsets $$M,N$$ of some extension of $$\mathbb{K}$$, the following formula

$$K(M \cup N) = K(M)(N) = K(N)(M)$$

holds.

</div>

The proof of this is almost obvious from the minimality in the definition.

Meanwhile, to obtain the field $$\mathbb{K}(A)$$ of [Definition 4](#def4), one can fix an extension $$\mathbb{L}$$ of $$\mathbb{K}$$ and then take the intersection of all subextensions of $$\mathbb{L}$$ containing $$A$$. On the other hand, since we have shown that morphisms in the category of extensions of $$\mathbb{K}$$ are nothing but extensions, the following holds.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$\mathcal{F}$$ be the set of subfields of a field $$E$$; with the inclusion relation $$\subseteq$$ it becomes a directed set. In particular, the union $$L$$ of the fields belonging to $$\mathcal{F}$$ is a field.

</div>

If there exists a finite set $$A$$ such that $$\mathbb{L}=\mathbb{K}(A)$$, we call the extension $$\mathbb{L}/\mathbb{K}$$ a *finite extension*. Then in particular a finite degree field extension is a finite extension, because a basis of $$\mathbb{L}$$ as a $$\mathbb{K}$$-vector space will serve as a set of generators of $$\mathbb{L}$$ as a field.

Now let two $$\mathbb{K}$$-extensions $$\mathbb{L}_1/\mathbb{K}$$, $$\mathbb{L}_2/\mathbb{L}$$ be given. Then we can consider the smallest extension containing both $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$.

<div class="definition" markdown="1">

<ins id="def7">**Definition 7**</ins> For two $$\mathbb{K}$$-extensions $$\mathbb{L}_1/\mathbb{K}$$, $$\mathbb{L}_2/\mathbb{L}$$, a $$\mathbb{K}$$-extension $$\mathbb{K} \rightarrow \mathbb{M}$$ is called their *composite* if there exist $$\mathbb{K}$$-algebra homomorphisms $$\mathbb{L}_1 \rightarrow \mathbb{M}$$ and $$\mathbb{L}_2 \rightarrow \mathbb{M}$$ making the following diagram

![composite_field](/assets/images/Math/Field_Theory/Algebraic_Extensions-2.png){:style="width:10em" class="invert" .align-center}

commute.

</div>

This can be made concrete as follows.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let two $$\mathbb{K}$$-extensions $$\mathbb{L}_1, \mathbb{L}_2$$ be given.

1. For their composite field $$\mathbb{M}$$ and extensions $$u_i: \mathbb{L}_i \rightarrow \mathbb{M}$$, the kernel of the function $$u_1\ast u_2: \mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2 \rightarrow \mathbb{M}$$ defined by the formula
    
    $$\mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2 \rightarrow \mathbb{M};\qquad x_1\otimes x_2\mapsto u_1(x_1)u_2(x_2)$$

    is a prime ideal.
2. Conversely, for any prime ideal $$\mathfrak{p}$$ of $$\mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2$$, there exist a suitable composite field $$\mathbb{M}$$ and extensions $$u_i: \mathbb{L}_i \rightarrow \mathbb{M}$$ such that $$\mathfrak{p}$$ is the kernel of $$u_1\ast u_2$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

1. The image $$\im(u_1\ast u_2)$$ of $$u_1\ast u_2$$ is a subring of the field $$\mathbb{M}$$, and hence an integral domain. The given claim is now obvious from [§Field of Fractions, ⁋Proposition 8](/en/math/algebraic_structures/field_of_fractions#prop8) and [§Quotient Rings and Ring Homomorphisms, ⁋Theorem 3](/en/math/algebraic_structures/quotient_rings#thm3).

2. Conversely, let $$\mathfrak{p}$$ be a prime ideal of $$\mathbb{L}_1\otimes_\mathbb{K}\mathbb{L}_2$$, and let $$\mathbb{M}=\Frac((\mathbb{L}_1\otimes_\mathbb{K}\mathbb{L}_2)/\mathfrak{p})$$ be the field of fractions of the integral domain $$(\mathbb{L}_1\otimes_\mathbb{K}\mathbb{L}_2)/\mathfrak{p}$$. Then for each $$x_1\in \mathbb{L}_1$$ and $$x_2\in \mathbb{L}_2$$, defining $$u_1(x_1)$$ to be the image of $$x_1\otimes 1$$ in $$\mathbb{M}$$ and $$u_2(x_2)$$ to be the image of $$1\otimes x_2$$ in $$\mathbb{M}$$, we see that these satisfy the required conditions.

</details>

Moreover, it is also obvious that the composite field obtained from the second result is uniquely determined up to isomorphism. Meanwhile, for any two $$\mathbb{K}$$-extensions $$\mathbb{L}_1, \mathbb{L}_2$$, since $$\mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2$$ always has a prime ideal ([§Definition of a Ring, ⁋Theorem 9 (Krull)](/en/math/algebraic_structures/rings#thm9)), we can verify that any two $$\mathbb{K}$$-extensions have a composite field.

## Algebraic Extensions

Let us fix a suitable extension $$\Omega$$ of $$\mathbb{K}$$. Unless stated otherwise, all field extensions are assumed to be subextensions of $$\Omega$$.

For any two $$\mathbb{K}$$-subalgebras $$E,F$$ of $$\Omega$$, considering the multiplication map $$\mu: E\otimes_\mathbb{K}F \rightarrow \Omega$$, its image $$G$$ is the subring of $$\Omega$$ generated by $$E\cup F$$.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> In the above situation, if the multiplication map $$\mu: E\otimes_\mathbb{K}F \rightarrow G$$ is an isomorphism, we say that $$E$$ and $$F$$ are *linearly disjoint*.

</div>

It is not difficult to see that this is equivalent to the family $$(x_iy_j)_{i\in I,j\in J}$$ being linearly independent when $$(x_i)_{i\in I}$$ and $$(y_j)_{j\in J}$$ are $$\mathbb{K}$$-bases of $$E$$ and $$F$$, respectively.

In particular, when $$E,F$$ are $$\mathbb{K}$$-extensions, we obtain the following proposition.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> For two $$\mathbb{K}$$-extensions $$\mathbb{L}_1, \mathbb{L}_2$$, the following hold.

1. If $$\mathbb{L}_2$$ has finite degree, the subring of $$\Omega$$ generated by $$\mathbb{L}_1 \cup \mathbb{L}_2$$ is a field, which coincides with $$\mathbb{L}_1(\mathbb{L}_2)$$. Moreover, the degree of $$\mathbb{L}_1(\mathbb{L}_2)$$ over $$\mathbb{L}_1$$ is also finite and
    
    $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1] \leq [\mathbb{L}_2 : \mathbb{K}]$$
    
    with equality holding when $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are linearly disjoint. In this case, $$\mathbb{L}_1(\mathbb{L}_2)$$ is $$\mathbb{L}_1$$-isomorphic to $$\mathbb{L}_1 \otimes_\mathbb{K} \mathbb{L}_2$$.
2. Assume further that the degree of $$\mathbb{L}_1$$ is also finite. Then the degree of $$\mathbb{L}_1(\mathbb{L}_2) = \mathbb{K}(\mathbb{L}_1 \cup \mathbb{L}_2)$$ is also finite and

    $$[\mathbb{K}(\mathbb{L}_1 \cup \mathbb{L}_2) : \mathbb{K}] \leq [\mathbb{L}_1 : \mathbb{K}][\mathbb{L}_2 : \mathbb{K}]$$

    with equality holding when $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are linearly disjoint.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. Let $$G$$ be the subring of $$\Omega$$ generated by $$\mathbb{L}_1 \cup \mathbb{L}_2$$. If $$(y_j)_{1 \leq j \leq n}$$ is a $$\mathbb{K}$$-basis of $$\mathbb{L}_2$$, then $$G$$ is generated as an $$\mathbb{L}_1$$-vector space by the $$y_j$$. Thus $$G$$ becomes an $$\mathbb{L}_1$$-algebra of finite rank $$\leq n$$. Since $$G$$ is contained in the field $$\Omega$$, it is an integral domain, and hence is a field by [Proposition 3](#prop3). Consequently $$G=\mathbb{L}_1(\mathbb{L}_2)$$, and
    
    $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1] \leq [\mathbb{L}_2 : \mathbb{K}]$$

    holds.
    Moreover, if $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1] = [\mathbb{L}_2 : \mathbb{K}]$$, then the $$y_j$$ must be linearly independent over $$\mathbb{L}_1$$; that is, $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are linearly disjoint.
2. This is obvious from the formula
    
    $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{K}] = [\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1][\mathbb{L}_1 : \mathbb{K}]$$

    .
</details>

In general, for two $$\mathbb{K}$$-extensions $$\mathbb{L}_1,\mathbb{L}_2$$, we mentioned earlier that the ring $$\mathbb{K}[\mathbb{L}_1\cup \mathbb{L}_2]$$ is not a field. However, the formula

$$\Frac(\mathbb{K}[\mathbb{L}_1\cup\mathbb{L}_2])=\mathbb{K}(\mathbb{L}_1\cup\mathbb{L}_2)$$

holds. More generally, let $$S_i\subseteq \mathbb{L}_i$$ be subsets satisfying $$\Frac(S_i)=\mathbb{L}_i$$. If $$G$$ is the ring generated by $$S_1\cup S_2$$, then we obtain the isomorphism

$$\Frac(G)\cong \mathbb{K}(\mathbb{L}_1\cup\mathbb{L}_2).$$

The following proposition extends this observation to the language of linearly disjoint extensions.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> Let $$\mathbb{L}_1, \mathbb{L}_2$$ be two extensions of $$\mathbb{K}$$, and let $$E_1, E_2$$ be $$\mathbb{K}$$-subalgebras of $$\Omega$$. Writing $$\mathbb{L}_i=\Frac(E_i)$$, then $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are linearly disjoint if and only if $$E_1$$ and $$E_2$$ are linearly disjoint.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

One direction is obvious, so assume that $$E_1, E_2$$ are linearly disjoint. Then we can first show that $$E_1$$ and $$\mathbb{L}_2$$ are linearly disjoint, because any $$E_2$$-free family in $$\Omega$$ is also $$\mathbb{L}_2$$-free. By the same logic, $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are linearly disjoint.

</details>

Meanwhile, since a linear combination of an arbitrary family consists only of finite sums (even if the family is infinite), the following holds.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> Let $$\mathbb{L}_1, \mathbb{L}_2$$ be two $$\mathbb{K}$$-extensions. If $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are linearly disjoint, then every subextension of $$\mathbb{L}_1$$ and every subextension of $$\mathbb{L}_2$$ are also linearly disjoint over $$\mathbb{K}$$. Conversely, if for all finitely generated subextensions $$\mathbb{L}_i'$$ of the $$\mathbb{L}_i$$, the extensions $$\mathbb{L}_1'$$ and $$\mathbb{L}_2'$$ are linearly disjoint, then $$\mathbb{L}_1$$ and $$\mathbb{L}_2$$ are also linearly disjoint.

</div>

In other words, whether two arbitrary extensions are linearly disjoint can be checked by looking only at their finite subextensions.

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> Let three $$\mathbb{K}$$-extensions $$\mathbb{L},\mathbb{M}_1,\mathbb{M}_2$$ be given, and suppose $$\mathbb{M}_1 \subseteq \mathbb{M}_2$$. Then $$\mathbb{L}$$ and $$\mathbb{M}_2$$ being linearly disjoint is equivalent to $$\mathbb{L}$$ and $$\mathbb{M}_1$$ being linearly disjoint and at the same time $$\mathbb{L}(\mathbb{M}_1)$$ and $$\mathbb{M}_2$$ being linearly disjoint.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First assume that $$\mathbb{L}$$ and $$\mathbb{M}_2$$ are linearly disjoint. Then by [Proposition 12](#prop12), $$\mathbb{L}$$ and $$\mathbb{M}_1$$ are also linearly disjoint. On the other hand, a $$\mathbb{K}$$-basis of $$\mathbb{L}$$ is also an $$\mathbb{M}_1$$-basis of $$\mathbb{M}_1[\mathbb{L}]$$. But by assumption this basis is $$\mathbb{M}_2$$-free, so $$\mathbb{M}_1[\mathbb{L}]$$ and $$\mathbb{M}_2$$ are linearly disjoint. Moreover, by [Proposition 11](#prop11), $$\mathbb{L}(\mathbb{M}_1) = \mathbb{M}_1(\mathbb{L})$$ and $$\mathbb{M}_2$$ are also linearly disjoint.

Now let us show the converse. As above, taking a $$\mathbb{K}$$-basis $$B$$ of $$\mathbb{L}$$, the hypothesis implies that $$B$$ is $$\mathbb{M}_1$$-free. Hence $$B$$ is an $$\mathbb{M}_1$$-basis of $$\mathbb{M}_1[\mathbb{L}]$$, and again by hypothesis $$\mathbb{M}_1[\mathbb{L}]$$ and $$\mathbb{M}_2$$ are linearly disjoint, so we obtain the desired result.

</details>

Consider a field $$\mathbb{K}$$ and a $$\mathbb{K}$$-algebra $$E$$. Then for any $$x\in E$$, exactly one of the following two holds.

1. $$(x^n)_{n\geq 0}$$ is $$\mathbb{K}$$-free.
2. There exists $$n$$ such that $$1,x,\cdots, x^{n-1}$$ are $$\mathbb{K}$$-linearly dependent.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> In the above situation, if the first case holds we call $$x\in E$$ *transcendental*, and if the second case holds we call $$x$$ *algebraic*.

Now suppose $$x\in E$$ is algebraic. Then the smallest $$n$$ such that $$1,x,\ldots, x^{n-1}$$ are $$\mathbb{K}$$-linearly dependent is called the *degree* of $$x$$, and for the linear combination

$$a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0=0$$

the polynomial

$$f(\x)=\x^n-\sum_{k=0}^{n-1}\frac{a_k}{a_n}\x^k$$

is called the *minimal polynomial* of $$x$$.

</div>

Then the following theorem holds, and its proof is not very difficult either.

<div class="proposition" markdown="1">

<ins id="thm15">**Theorem 15**</ins> For an algebraic element $$x\in E$$ of a $$\mathbb{K}$$-algebra $$E$$, let $$n$$ be the degree of $$x$$ and $$f$$ its minimal polynomial. Then the following hold.

1. For $$g \in \mathbb{K}[\x]$$, the necessary and sufficient condition for $$g(x) = 0$$ is that $$g$$ be a multiple of $$f$$.
2. Define $$\mathbb{K}[\x] \rightarrow \mathbb{K}[x]$$ by $$g\mapsto g(x)$$. Then this morphism factors through the quotient algebra $$\mathbb{K}[\x]/(f)$$, and the resulting map $$\mathbb{K}[\x]/(f) \rightarrow \mathbb{K}[x]$$ is an isomorphism. Moreover, in this case $$1, x, \dots, x^{n-1}$$ form a $$\mathbb{K}$$-basis of $$\mathbb{K}[x]$$, and therefore $$[\mathbb{K}[x] : \mathbb{K}] = n$$ holds.
3. If $$E$$ is an integral domain, then $$\mathbb{K}[x]$$ is a field, and $$f\in \mathbb{K}[\x]$$ is the unique monic irreducible polynomial satisfying $$f(x) = 0$$.
4. The necessary and sufficient condition for $$x$$ to be an invertible element in $$E$$ is that $$f(0) \neq 0$$, and in this case $$x^{-1} \in \mathbb{K}[x]$$.

</div>

Also, for an extension $$\mathbb{K}\hookrightarrow \mathbb{L}$$ and an $$\mathbb{L}$$-algebra $$E$$, if an element $$x\in E$$ is algebraic over $$\mathbb{K}$$, then $$x$$ is also algebraic over $$\mathbb{L}$$, and its degree does not exceed that over $$\mathbb{K}$$.

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> A field extension $$\mathbb{L}/\mathbb{K}$$ in which every element is algebraic is called an *algebraic extension*. A field extension that is not algebraic is called a *transcendental extension*.

</div>

Then it is not difficult to see that an extension $$\mathbb{L}/\mathbb{K}$$ being algebraic is equivalent to every $$\mathbb{K}$$-subalgebra of $$\mathbb{L}$$ being a field. Also, the following proposition is obvious.

<div class="proposition" markdown="1">

<ins id="prop17">**Proposition 17**</ins> A degree $$n$$ $$\mathbb{K}$$-extension $$\mathbb{L}$$ is necessarily an algebraic extension, and the degree of any element of $$\mathbb{L}$$ is a divisor of $$n$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

$$[\mathbb{L}:\mathbb{K}]=[\mathbb{L}:\mathbb{K}(x)][\mathbb{K}(x):\mathbb{K}].$$

</details>

Extending this inductively, we obtain the following.

<div class="proposition" markdown="1">

<ins id="thm18">**Theorem 18**</ins> Let a finitely generated $$\mathbb{K}$$-extension $$\mathbb{L}$$ be generated by algebraic elements $$a_1, \dots, a_m$$. Then $$\mathbb{L}/\mathbb{K}$$ is a finite degree extension. Moreover, if for each $$i$$ we let $$n_i$$ be the degree of $$a_i$$ over $$\mathbb{K}(a_1, \dots, a_{i-1})$$, then the degree of $$\mathbb{L}$$ over $$\mathbb{K}$$ is $$n_1 n_2 \cdots n_m$$, and the elements

$$a_1^{\nu_1} a_2^{\nu_2} \cdots a_m^{\nu_m}\qquad (0 \leq \nu_i \leq n_i - 1)$$

form a $$\mathbb{K}$$-basis of $$\mathbb{L}$$.

</div>

In particular, for a set $$A$$ consisting only of algebraic elements, $$\mathbb{K}(A)=\mathbb{K}[A]$$ holds. Moreover, algebraic extensions are transitive. That is, the following proposition holds.

<div class="proposition" markdown="1">

<ins id="prop19">**Proposition 19**</ins> For a field extension $$\mathbb{M}/\mathbb{L}/\mathbb{K}$$, the necessary and sufficient condition for $$\mathbb{M}$$ to be algebraic over $$\mathbb{K}$$ is that $$\mathbb{L}$$ be algebraic over $$\mathbb{K}$$ and at the same time $$\mathbb{M}$$ be algebraic over $$\mathbb{L}$$.
</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

One direction is obvious, so it suffices to show the converse. Assume that $$\mathbb{L}$$ is algebraic over $$\mathbb{K}$$ and that $$\mathbb{M}$$ is algebraic over $$\mathbb{L}$$, and pick an arbitrary element $$x$$ of $$\mathbb{M}$$. We must show that $$x$$ is algebraic over $$\mathbb{K}$$.

First, by assumption $$x$$ is algebraic over $$\mathbb{L}$$. Let $$g \in \mathbb{L}[\x]$$ be the minimal polynomial of $$x$$, and let $$A$$ be the set of coefficients of $$g$$. Then $$g \in \mathbb{K}(A)[\x]$$, and therefore $$x$$ is algebraic over $$\mathbb{K}(A)$$.

Moreover, $$\mathbb{K}(A \cup \{x\}) = \mathbb{K}(A)(x)$$ has finite degree over $$\mathbb{K}(A)$$. Since $$A \subseteq \mathbb{L}$$ and $$\mathbb{L}$$ is algebraic over $$\mathbb{K}$$, by [Theorem 18](#thm18) the extension $$\mathbb{K}(A)$$ has finite degree over $$\mathbb{K}$$. Hence $$\mathbb{K}(A \cup \{x\})$$ has finite degree over $$\mathbb{K}$$, and therefore $$x$$ is algebraic over $$\mathbb{K}$$.

</details>
