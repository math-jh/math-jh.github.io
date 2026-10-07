---
title: "Algebraic Extensions"
description: "We cover field extensions and the definition of a field extension, and the perspective of interpreting a field extension as an associative algebra."
excerpt: "The definition and degree of algebraic extensions of fields"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/algebraic_extensions
sidebar: 
    nav: "field_theory-en"

date: 2025-04-26
weight: 2
translated_at: 2026-05-31T04:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-07T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Field Extensions

We saw by [§Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2){: data-lid="ysg0g" } that a morphism between fields is either injective or the zero map. In this post we examine the former case. 

We call an injective field morphism a *field extension*. Then, for a fixed field $\mathbb{K}\in\Field$, the under category of $\mathbb{K}$ becomes the category of extensions of $\mathbb{K}$. 

Although this notation differs slightly from that of [\[Category Theory\] §Category, ⁋Example 13](/en/math/category_theory/categories#ex13){: data-lid="1xd6q" }, we often denote a field extension $\mathbb{K}\rightarrow \mathbb{L}$ by $\mathbb{L}/\mathbb{K}$. Then, whenever a field extension $\mathbb{L}/\mathbb{K}$ is given, via the injective map $\mathbb{K}\hookrightarrow\mathbb{L}$ we can identify $\mathbb{K}$ with a subfield of $\mathbb{L}$. However, if $\mathbb{L}=\mathbb{K}$ and $\mathbb{K}\hookrightarrow\mathbb{L}=\mathbb{K}$ is an endomorphism, such an identification may cause confusion, so in this case we do not identify $\mathbb{K}$ with a subfield of $\mathbb{L}$.  

By definition, given two extensions $\mathbb{K} \rightarrow \mathbb{L}_1$ and $\mathbb{K} \rightarrow \mathbb{L}_2$, the following commutative diagram

{% diagram Math/Field_Theory/Algebraic_Extensions-1.svg width="10.39em" alt="morphism_of_field_extensions" %}

is a morphism between them. Here, since both $\mathbb{L}_1$ and $\mathbb{L}_2$ are fields, the morphism $\mathbb{L}_1 \rightarrow \mathbb{L}_2$ must be injective. Subject to the caution above, in this case we call $\mathbb{L}_1$ a *subextension* of $\mathbb{L}_2$. 

Thus any field extension $\mathbb{L}/\mathbb{K}$ can be regarded as an associative unital $\mathbb{K}$-algebra (which is itself a field). 

::: remark Remark {#rmk}
We consider $\mathbb{K}$-algebras and homomorphisms between them in order to treat situations similar to the above; henceforth in our posts the category $\Alg{\mathbb{K}}$ will always be the category of unital associative $\mathbb{K}$-algebras. That is, by a $\mathbb{K}$-algebra we shall always mean a unital associative $\mathbb{K}$-algebra, and by a $\mathbb{K}$-algebra homomorphism we shall always mean a unital $\mathbb{K}$-algebra homomorphism. 
:::

Any $\mathbb{K}$-algebra is also a $\mathbb{K}$-module, so its dimension is well-defined. ([\[Multilinear Algebra\] §Bases, ⁋Proposition 6](/en/math/multilinear_algebra/basis_of_free_modules#prop6){: data-lid="4yolo" })

::: Definition 1
For any $\mathbb{K}$-algebra $A$, we call $\dim_{\mathbb{K}}A$ the *degree* of $A$ and denote it by $[A:\mathbb{K}]$. 
:::

Then the following is obvious from the definition. 

::: Proposition 2
For a field extension $\mathbb{L}_2/\mathbb{L}_1/\mathbb{K}$, $[\mathbb{L}_2:\mathbb{K}]=[\mathbb{L}_2:\mathbb{L}_1][\mathbb{L}_1:\mathbb{K}]$ holds. 
:::

More generally, for a field $\mathbb{K}$ and any $\mathbb{K}$-algebra $E$, we can define $[E:\mathbb{K}]$ as $\dim_\mathbb{K}E$. Then the following proposition is simple linear algebra.

::: Proposition 3
For a finite degree $\mathbb{K}$-algebra $E$, if $x\in E$ is a non-zerodivisor in $E$, then $x$ is an invertible element of $E$. 
:::
::: Proof
By assumption, $E$ is a finite-dimensional $\mathbb{K}$-algebra, and since $x$ is a non-zerodivisor of $E$, the function

$$E \rightarrow E;\qquad y\mapsto xy$$

is injective. Now since $E$ is finite-dimensional, injectivity of the above linear map is equivalent to surjectivity, and therefore $xy=1$ holds for some $y\in E$. Here, if we define $L_x, L_y$ by $z\mapsto xz$ and $z\mapsto yz$ respectively, then $L_x$ is bijective and $L_x\circ L_y=\id$, so $L_y=L_x^{-1}$; thus evaluating $L_y\circ L_x=\id$ at $z=1$ yields $yx=1$, from which we obtain the desired result. 
:::

In particular, if a finite-dimensional $\mathbb{K}$-algebra $E$ is an integral domain, then $E$ is necessarily a field. 

Meanwhile, for any ring $A$, we have denoted the polynomial ring with coefficients in $A$ in the variable $\x$ by $A[\x]$, which can be thought of as the smallest algebra containing $A$ and the variable $\x$. In a similar manner, to adjoin to a field $\mathbb{K}$ an element $\x$, this time we will also have to add the inverses.

::: Definition 4
For a field extension $\mathbb{L}/\mathbb{K}$ and a subset $A\subseteq \mathbb{L}$, we denote the smallest subextension containing $A$ in $\mathbb{L}$ by $\mathbb{K}(A)$.
:::

In this definition, $\mathbb{L}$ is needed only to define $A$, and regardless of what $\mathbb{L}$ actually is, $\mathbb{K}(A)$ will be an isomorphic field. For this reason, we often fix for $\mathbb{K}$ a (very large) field extension $\Omega$ (without worrying about what $\Omega$ is) and consider subsets $M,N$ of this extension.

::: Proposition 5
For a suitable extension of $\mathbb{K}$ and two subsets $M,N$ of it, the following formula

$$\mathbb{K}(M \cup N) = \mathbb{K}(M)(N) = \mathbb{K}(N)(M)$$

holds.
:::

The proof of this is almost obvious from the minimality of the definition.

Meanwhile, to obtain the field $\mathbb{K}(A)$ of [Definition 4](#def4){: data-lid="7v7xb" }, one can fix a $\mathbb{K}$-extension $\mathbb{L}$ and then take the intersection of all subextensions containing $A$ in $\mathbb{L}$. On the other hand, since we have shown that morphisms in the category of extensions of $\mathbb{K}$ are only extensions, the following holds.

::: Proposition 6
Let $\mathcal{F}$ be a set of subfields of a field $E$; with the inclusion relation $\subseteq$, it becomes a directed set. In particular, the union $L$ of the fields belonging to $\mathcal{F}$ is a field.
:::

If $\mathbb{L}=\mathbb{K}(A)$ for some finite set $A$, we call the extension $\mathbb{L}/\mathbb{K}$ a *finite extension*. Then in particular a finite degree field extension is a finite extension, because a basis of $\mathbb{L}$ as a $\mathbb{K}$-vector space will serve as a set of generators of $\mathbb{L}$ as a field.

Now let two $\mathbb{K}$-extensions $\mathbb{L}_1/\mathbb{K}$, $\mathbb{L}_2/\mathbb{K}$ be given. Then we can consider the smallest extension containing both $\mathbb{L}_1$ and $\mathbb{L}_2$.

::: Definition 7
For two $\mathbb{K}$-extensions $\mathbb{L}_1/\mathbb{K}$, $\mathbb{L}_2/\mathbb{K}$, that a $\mathbb{K}$-extension $\mathbb{K} \rightarrow \mathbb{M}$ is their *composite* means that, for the following diagram,

{% diagram Math/Field_Theory/Algebraic_Extensions-2.svg width="10.57em" alt="composite_field" %}

there exist $\mathbb{K}$-algebra homomorphisms $\mathbb{L}_1 \rightarrow \mathbb{M}$ and $\mathbb{L}_2 \rightarrow \mathbb{M}$ making it commute.
:::

Concretely, this can be written as follows.

::: Proposition 8
Let two $\mathbb{K}$-extensions $\mathbb{L}_1, \mathbb{L}_2$ be given.

1. For their composite field $\mathbb{M}$ and extensions $u_i: \mathbb{L}_i \rightarrow \mathbb{M}$, the following formula
    
    $$\mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2 \rightarrow \mathbb{M};\qquad x_1\otimes x_2\mapsto u_1(x_1)u_2(x_2)$$

    defines a function $u_1\ast u_2: \mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2 \rightarrow \mathbb{M}$ whose kernel $\ker (u_1\ast u_2)$ is a prime ideal.
2. Conversely, in $\mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2$, for any prime ideal $\mathfrak{p}$, there exist a suitable composite field $\mathbb{M}$ and extensions $u_i: \mathbb{L}_i \rightarrow \mathbb{M}$ such that $\mathfrak{p}$ is the kernel of $u_1\ast u_2$.
:::
::: Proof
1. For $u_1\ast u_2$, its image $\im(u_1\ast u_2)$ is a subring of the field $\mathbb{M}$, and hence an integral domain. Now the given claim is obvious from [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9){: data-lid="kkli6" } and [\[Algebraic Structures\] §Quotient Rings and Ring Isomorphisms, ⁋Theorem 3](/en/math/algebraic_structures/quotient_rings#thm3){: data-lid="vb5so" }.

2. Conversely, let $\mathfrak{p}$ be a prime ideal of $\mathbb{L}_1\otimes_\mathbb{K}\mathbb{L}_2$, and let the field of fractions of the integral domain $(\mathbb{L}_1\otimes_\mathbb{K}\mathbb{L}_2)/\mathfrak{p}$ be $\mathbb{M}=\Frac((\mathbb{L}_1\otimes_\mathbb{K}\mathbb{L}_2)/\mathfrak{p})$. Then for each $x_1\in \mathbb{L}_1$ and $x_2\in \mathbb{L}_2$, defining $u_1(x_1)$ to be the image of $x_1\otimes 1$ in $\mathbb{M}$ and $u_2(x_2)$ to be the image of $1\otimes x_2$ in $\mathbb{M}$, we see that these satisfy the required conditions.
:::

Moreover, it is also obvious that the composite field obtained from the second result is uniquely determined up to isomorphism. Meanwhile, for any two $\mathbb{K}$-extensions $\mathbb{L}_1, \mathbb{L}_2$, since $\mathbb{L}_1\otimes_\mathbb{K} \mathbb{L}_2$ always has a prime ideal ([\[Algebraic Structures\] §Definition of a Ring, ⁋Theorem 10](/en/math/algebraic_structures/rings#thm10){: data-lid="1u585" }), we can verify that any two $\mathbb{K}$-extensions have a composite field.

## Algebraic Extensions

For $\mathbb{K}$, let us fix a suitable extension $\Omega$. Unless stated otherwise, all field extensions are assumed to be subextensions of $\Omega$.

In $\Omega$, for any two $\mathbb{K}$-subalgebras $E,F$, considering the multiplication map $\mu: E\otimes_\mathbb{K}F \rightarrow \Omega$, its image $G$ is the subring generated by $E\cup F$ in $\Omega$.

::: Definition 9
In the above situation, if the multiplication map $\mu: E\otimes_\mathbb{K}F \rightarrow G$ is an isomorphism, we say that $E$ and $F$ are *linearly disjoint*.
:::

It is not difficult to see that for $E$ and $F$, given two $\mathbb{K}$-bases $(x_i)_{i\in I}$ and $(y_j)_{j\in J}$, this is equivalent to $(x_iy_j)_{i\in I,j\in J}$ being linearly independent.

In particular, when $E,F$ are $\mathbb{K}$-extensions, we obtain the following proposition.

::: Proposition 10
For two $\mathbb{K}$-extensions $\mathbb{L}_1, \mathbb{L}_2$, the following hold.

1. If $\mathbb{L}_2$ has finite degree, the subring generated by $\mathbb{L}_1 \cup \mathbb{L}_2$ in $\Omega$ is a field, which coincides with $\mathbb{L}_1(\mathbb{L}_2)$. Moreover, the degree of $\mathbb{L}_1(\mathbb{L}_2)$ over $\mathbb{L}_1$ is also finite, and
    
    $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1] \leq [\mathbb{L}_2 : \mathbb{K}]$$
    
    with equality holding when $\mathbb{L}_1$ and $\mathbb{L}_2$ are linearly disjoint. In this case, $\mathbb{L}_1(\mathbb{L}_2)$ and $\mathbb{L}_1 \otimes_\mathbb{K} \mathbb{L}_2$ are $\mathbb{L}_1$-isomorphic.
2. In addition to the above conditions, assume further that the degree of $\mathbb{L}_1$ is also finite. Then the degree of $\mathbb{L}_1(\mathbb{L}_2) = \mathbb{K}(\mathbb{L}_1 \cup \mathbb{L}_2)$ is also finite, and

    $$[\mathbb{K}(\mathbb{L}_1 \cup \mathbb{L}_2) : \mathbb{K}] \leq [\mathbb{L}_1 : \mathbb{K}][\mathbb{L}_2 : \mathbb{K}]$$

    with equality holding when $\mathbb{L}_1$ and $\mathbb{L}_2$ are linearly disjoint.
:::

::: Proof
1. Let the subring generated by $\mathbb{L}_1 \cup \mathbb{L}_2$ in $\Omega$ be $G$. If $(y_j)_{1 \leq j \leq n}$ is a basis of $\mathbb{L}_2$ over $\mathbb{K}$, then $G$ is generated as an $\mathbb{L}_1$-vector space by the $y_j$. Then $G$ has finite rank $\leq n$ as an $\mathbb{L}_1$-algebra. Now, since $G$ is contained in the field $\Omega$, it is an integral domain, and therefore is a field by [Proposition 3](#prop3){: data-lid="ocv0h" }. Consequently, $G=\mathbb{L}_1(\mathbb{L}_2)$, and
    
    $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1] \leq [\mathbb{L}_2 : \mathbb{K}]$$

    holds.  
    Moreover, if $[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1] = [\mathbb{L}_2 : \mathbb{K}]$, then the $y_j$ must be linearly independent over $\mathbb{L}_1$; that is, $\mathbb{L}_1$ and $\mathbb{L}_2$ are linearly disjoint. 
2. This is obvious from the following formula:
    
    $$[\mathbb{L}_1(\mathbb{L}_2) : \mathbb{K}] = [\mathbb{L}_1(\mathbb{L}_2) : \mathbb{L}_1][\mathbb{L}_1 : \mathbb{K}]$$
:::

In general, for two $\mathbb{K}$-extensions $\mathbb{L}_1,\mathbb{L}_2$, we mentioned earlier that the ring $\mathbb{K}[\mathbb{L}_1\cup \mathbb{L}_2]$ is not a field. However, the formula

$$\Frac(\mathbb{K}[\mathbb{L}_1\cup\mathbb{L}_2])=\mathbb{K}(\mathbb{L}_1\cup\mathbb{L}_2)$$

holds. More generally, let $S_i\subseteq \mathbb{L}_i$ be subsets satisfying $\Frac(\mathbb{K}[S_i])=\mathbb{L}_i$. If $G$ is the ring generated by $\mathbb{K}\cup S_1\cup S_2$, we obtain the isomorphism

$$\Frac(G)\cong \mathbb{K}(\mathbb{L}_1\cup\mathbb{L}_2)$$

The following proposition extends this observation to the language of linearly disjoint extensions. 

::: Proposition 11
Let $E_1, E_2$ in $\Omega$ be $\mathbb{K}$-subalgebras. If $\mathbb{L}_i=\Frac(E_i)$, then $\mathbb{L}_1$ and $\mathbb{L}_2$ are linearly disjoint if and only if $E_1$ and $E_2$ are linearly disjoint. 
:::
::: Proof
One direction is obvious, so assume that $E_1, E_2$ are linearly disjoint. Then we can first show that $E_1$ and $\mathbb{L}_2$ are linearly disjoint, because any family in $\Omega$ that is $E_2$-free is also $\mathbb{L}_2$-free. Now, by the same logic, $\mathbb{L}_1$ and $\mathbb{L}_2$ are linearly disjoint. 
:::

Meanwhile, since a linear combination of an arbitrary family consists only of finite sums (even if the family is infinite), the following holds.

::: Proposition 12
For a field $\mathbb{K}$, consider two extensions $\mathbb{L}_1$, $\mathbb{L}_2$. If $\mathbb{L}_1$ and $\mathbb{L}_2$ are linearly disjoint, then every subextension of $\mathbb{L}_1$ and every subextension of $\mathbb{L}_2$ are also linearly disjoint over $\mathbb{K}$. Conversely, if for the $\mathbb{L}_i$, all finitely generated subextensions $\mathbb{L}_i'$ are such that $\mathbb{L}_1'$ and $\mathbb{L}_2'$ are linearly disjoint, then $\mathbb{L}_1$ and $\mathbb{L}_2$ are also linearly disjoint.
:::

In other words, whether two arbitrary extensions are linearly disjoint can be checked just by looking at arbitrary finite subextensions of the two extensions.

::: Proposition 13
Let three $\mathbb{K}$-extensions $\mathbb{L},\mathbb{M}_1,\mathbb{M}_2$ be given, and suppose $\mathbb{M}_1 \subseteq \mathbb{M}_2$. Then $\mathbb{L}$ and $\mathbb{M}_2$ being linearly disjoint is equivalent to $\mathbb{L}$ and $\mathbb{M}_1$ being linearly disjoint and at the same time $\mathbb{L}(\mathbb{M}_1)$ and $\mathbb{M}_2$ being linearly disjoint over $\mathbb{M}_1$.
:::

::: Proof
First assume that $\mathbb{L}$ and $\mathbb{M}_2$ are linearly disjoint. Then by [Proposition 12](#prop12){: data-lid="pgho1" }, $\mathbb{L}$ and $\mathbb{M}_1$ are also linearly disjoint. On the other hand, a basis of $\mathbb{L}$ over $\mathbb{K}$ is also a basis of $\mathbb{M}_1[\mathbb{L}]$ over $\mathbb{M}_1$. But by assumption this basis is $\mathbb{M}_2$-free, so $\mathbb{M}_1[\mathbb{L}]$ and $\mathbb{M}_2$ are linearly disjoint over $\mathbb{M}_1$. Also, by [Proposition 11](#prop11){: data-lid="3303o" }, $\mathbb{L}(\mathbb{M}_1) = \mathbb{M}_1(\mathbb{L})$ and $\mathbb{M}_2$ are also linearly disjoint over $\mathbb{M}_1$.

Now let us show the converse. As above, considering a basis of $\mathbb{L}$ over $\mathbb{K}$, denoted $B$, from the hypothesis $B$ is $\mathbb{M}_1$-free. Therefore $B$ is a basis of $\mathbb{M}_1[\mathbb{L}]$ over $\mathbb{M}_1$, and again by hypothesis $\mathbb{M}_1[\mathbb{L}]$ and $\mathbb{M}_2$ are linearly disjoint over $\mathbb{M}_1$, so we obtain the desired result.
:::

Consider a field $\mathbb{K}$ and a $\mathbb{K}$-algebra $E$. Then for any $x\in E$, exactly one of the following two holds.

1. $(x^n)_{n\geq 0}$ is $\mathbb{K}$-free.
2. $1,x,\cdots, x^{n-1}$ are $\mathbb{K}$-linearly dependent for some $n$.

::: Definition 14
In the above situation, if the first case holds we call $x\in E$ *transcendental*, and if the second case holds we call $x$ *algebraic*.

Now suppose $x\in E$ is algebraic. Then, for $1,x,\ldots, x^{n}$ to be $\mathbb{K}$-linearly dependent, the smallest such $n$ is called the *degree* of $x$, and for the linear combination at this time

$$a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0=0$$

the following polynomial

$$f(\x)=\x^n+\sum_{k=0}^{n-1}\frac{a_k}{a_n}\x^k$$

is called the *minimal polynomial* of $x$.
:::

Then the following theorem holds, and its proof is not very difficult either.

::: Theorem 15
For a $\mathbb{K}$-algebra $E$ and an algebraic element $x\in E$, let the degree of $x$ be $n$ and its minimal polynomial be $f$. Then the following hold. 

1. For $g \in \mathbb{K}[\x]$, $g(x) = 0$ if and only if $g$ is a multiple of $f$.
2. Define $\mathbb{K}[\x] \rightarrow \mathbb{K}[x]$ by $g\mapsto g(x)$. Then this morphism factors through the quotient algebra $\mathbb{K}[\x]/(f)$, and the resulting map $\mathbb{K}[\x]/(f) \rightarrow \mathbb{K}[x]$ is an isomorphism. Moreover, in this case $1, x, \dots, x^{n-1}$ form a basis of $\mathbb{K}[x] $ over $\mathbb{K}$, and therefore $[\mathbb{K}[x] : \mathbb{K}] = n$ holds.
3. If $E$ is an integral domain, then $\mathbb{K}[x]$ is a field, and $f\in \mathbb{K}[\x]$ is the unique monic irreducible polynomial satisfying $f(x) = 0$.
4. $x$ is an invertible element in $E$ if and only if $f(0) \neq 0$, in which case $x^{-1} \in \mathbb{K}[x]$.
:::

Also, for an extension $\mathbb{K}\hookrightarrow \mathbb{L}$ and an $\mathbb{L}$-algebra $E$, we know that if an element $x\in E$ is algebraic over $\mathbb{K}$, then $x$ is also algebraic over $\mathbb{L}$ and its degree does not exceed its degree over $\mathbb{K}$. 

::: Definition 16
A field extension $\mathbb{L}/\mathbb{K}$ in which every element is algebraic is called an *algebraic extension*. A field extension that is not algebraic is called a *transcendental extension*. 
:::

Then it is not difficult to see that an extension $\mathbb{L}/\mathbb{K}$ being algebraic is equivalent to every subalgebra of $\mathbb{L}$ over $\mathbb{K}$ being a field. Also, the following proposition is obvious. 

::: Proposition 17
A degree $n$ $\mathbb{K}$-extension $\mathbb{L}$ is necessarily an algebraic extension, and the degree of any element of $\mathbb{L}$ is a divisor of $n$. 
:::
::: Proof
$$[\mathbb{L}:\mathbb{K}]=[\mathbb{L}:\mathbb{K}(x)][\mathbb{K}(x):\mathbb{K}].$$
:::

Extending this inductively, we obtain the following. 

::: Theorem 18
Suppose that a finitely generated $\mathbb{K}$-extension $\mathbb{L}$ is generated by algebraic elements $a_1, \dots, a_m$. Then $\mathbb{L}/\mathbb{K}$ is a finite degree extension. Moreover, if for each $i$, we let the degree of $a_i$ over $\mathbb{K}(a_1, \dots, a_{i-1})$ be $n_i$, then the degree of $\mathbb{L}$ over $\mathbb{K}$ is $n_1 n_2 \cdots n_m$, and the following elements

$$a_1^{\nu_1} a_2^{\nu_2} \cdots a_m^{\nu_m}\qquad (0 \leq \nu_i \leq n_i - 1)$$

form a basis of $\mathbb{L}$ over $\mathbb{K}$. 
:::

In particular, for a set $A$ consisting only of algebraic elements, $\mathbb{K}(A)=\mathbb{K}[A]$ holds. Moreover, algebraic extensions are transitive. That is, the following proposition holds. 

::: Proposition 19
For a field extension $\mathbb{M}/\mathbb{L}/\mathbb{K}$, $\mathbb{M}$ is algebraic over $\mathbb{K}$ if and only if $\mathbb{L}$ is algebraic over $\mathbb{K}$ and at the same time $\mathbb{M}$ is algebraic over $\mathbb{L}$.
:::

::: Proof
One direction is obvious, so it suffices to show the converse. Assume that $\mathbb{L}$ is algebraic over $\mathbb{K}$ and at the same time $\mathbb{M}$ is algebraic over $\mathbb{L}$, and choose from $\mathbb{M}$ an arbitrary element $x$. We must show that $x$ is algebraic over $\mathbb{K}$. 

First, by assumption $x$ is algebraic over $\mathbb{L}$. Let $g \in \mathbb{L}[\x]$ be the minimal polynomial of $x$, and let the set of coefficients of $g$ be $A$. Then $g \in \mathbb{K}(A)[\x]$, and therefore $x$ is algebraic over $\mathbb{K}(A)$.

Also, $\mathbb{K}(A \cup \{x\}) = \mathbb{K}(A)(x)$ has finite degree over $\mathbb{K}(A)$. $A$ is a finite set consisting of the coefficients of $g$, and since $A \subseteq \mathbb{L}$ and $\mathbb{L}$ is algebraic over $\mathbb{K}$, by [Theorem 18](#thm18){: data-lid="im3pw" }, $\mathbb{K}(A)$ has finite degree over $\mathbb{K}$. From this, $\mathbb{K}(A \cup \{x\})$ has finite degree over $\mathbb{K}$, and therefore $x$ is algebraic over $\mathbb{K}$. 
:::

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
