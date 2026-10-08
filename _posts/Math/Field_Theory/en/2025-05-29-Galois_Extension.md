---
title: "Galois Extensions"
description: "This post covers the definition and properties of Galois extensions, defining the conjugate relation among algebraic extensions and examining the relationship between conjugate extensions and conjugate elements. It also examines several equivalent conditions for quasi-Galois extensions and characterizations of Galois extensions using minimal polynomials."
excerpt: "Definition of Galois extensions satisfying both normality and separability"

categories: [Math / Field Theory]
permalink: /en/math/field_theory/galois_extension
sidebar: 
    nav: "field_theory-en"

date: 2025-05-29
weight: 8
translated_at: 2026-06-11T06:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-08T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
We are now ready to define what a Galois extension is, but before that we examine the following proposition. 


::: Proposition 1
Consider an algebraic extension $\mathbb{L}/\mathbb{K}$ and an injective $\mathbb{K}$-homomorphism $u:\mathbb{L}\rightarrow \overline{\mathbb{K}}$. 

1. If $u(\mathbb{L})\subseteq \mathbb{L}$, then $u$ from $\mathbb{L}$ to $\mathbb{L}$ is a $\mathbb{K}$-automorphism. 
2. Extending $u$, there exists on $\overline{\mathbb{K}}$ a $\mathbb{K}$-automorphism. 
:::
::: Proof
1. For any $x\in \mathbb{L}$, let the minimal polynomial of $x$ be $f$. If we let the set $\Phi$ be the set of roots in $\mathbb{L}$ of $f$, then $\Phi$ is a finite set. Moreover, if $\alpha\in\Phi$, then

    $$0=u(0)=u(f(\alpha))=f(u(\alpha))$$
    
    holds, so $u(\Phi)\subseteq\Phi$. However, since $u$ is not the zero map, it is injective ([§Fields, ⁋Proposition 2](/en/math/field_theory/fields#prop2){: data-lid="swwn3" }), and therefore $u$ is a bijection from $\Phi$ to $\Phi$. Thus $x\in\Phi=u(\Phi)\subseteq u(\mathbb{L})$, from which $u(\mathbb{L})=\mathbb{L}$.

2. Since $\overline{\mathbb{K}}$ is an algebraic closure of $u(\mathbb{L})$ and $\mathbb{L}$, from the universal property of [§Algebraic Closure, ⁋Theorem 5](/en/math/field_theory/algebraically_closed_extensions#thm5){: data-lid="gn9n1" }, extending $u$, we obtain on $\overline{\mathbb{K}}$ a $\mathbb{K}$-endomorphism $w$. Here, since $w$ is injective, $w(\overline{\mathbb{K}})$ is isomorphic to $\overline{\mathbb{K}}$ and thus algebraically closed; since $\overline{\mathbb{K}}/\mathbb{K}$ is algebraic, $\overline{\mathbb{K}}$ is an algebraic extension of $w(\overline{\mathbb{K}})$, so from the fourth condition of [§Algebraic Closure, ⁋Proposition 1](/en/math/field_theory/algebraically_closed_extensions#prop1){: data-lid="69vuw" }, we obtain $w(\overline{\mathbb{K}})=\overline{\mathbb{K}}$, that is, $w$ is an automorphism. 
:::

Our goal is to examine all algebraic extensions of a fixed field $\mathbb{K}$, or more precisely, to consider equivalence classes of algebraic extensions.  

::: Definition 2
For a field $\mathbb{K}$, in an algebraic closure $\overline{\mathbb{K}}$, given two algebraic extensions $\mathbb{L}$, $\mathbb{M}$, if, satisfying $u(\mathbb{L})=\mathbb{M}$, a $\mathbb{K}$-automorphism $u:\overline{\mathbb{K}}\rightarrow \overline{\mathbb{K}}$ exists, we say that they are *conjugate*. Two elements $x,y\in\overline{\mathbb{K}}$ are *conjugate* if there exists a $\mathbb{K}$-automorphism $u: \overline{\mathbb{K}}\rightarrow \overline{\mathbb{K}}$ such that $u(x)=y$. 
:::

By [Proposition 1](#prop1){: data-lid="a8sf9" }, if $\mathbb{M}$ and $\mathbb{L}$ are $\mathbb{K}$-isomorphic extensions, then they are conjugate extensions, and by definition conjugate extensions are isomorphic. Moreover, the following holds.

::: Proposition 3
Fix two elements $x,y$ of $\overline{\mathbb{K}}$. The following are all equivalent. 

1. $x,y$ are conjugate elements. 
2. There exists a $\mathbb{K}$-isomorphism $v: \mathbb{K}(x) \rightarrow \mathbb{K}(y)$ satisfying $v(x)=y$. 
3. $x$ and $y$ have the same minimal polynomial. 
:::
::: Proof
First assume the first condition, and choose a $\mathbb{K}$-automorphism $u$ of $\overline{\mathbb{K}}$ such that $u(x)=y$. If $f$ is the minimal polynomial of $x$, then 

$$f(y)=f(u(x))=u(f(x))=u(0)=0$$

so the minimal polynomial of $y$ divides $f$. By the same logic, the minimal polynomial of $x$ divides the minimal polynomial of $y$, and therefore they are equal. 

On the other hand, if $x,y$ have the same minimal polynomial $f$, then by the first isomorphism theorem 

$$\mathbb{K}(x)\cong \mathbb{K}[\x]/(f)\cong \mathbb{K}(y)$$

and since the two isomorphisms starting from $\mathbb{K}[\x]/(f)$ send the class of $\x$ to $x$ and $y$ respectively, composing them yields a $\mathbb{K}$-isomorphism $\mathbb{K}(x)\rightarrow \mathbb{K}(y)$ sending $x$ to $y$. That is, the third condition implies the second. Finally, assuming the second condition, by [Proposition 1](#prop1){: data-lid="gtjwc" } there exists a $\mathbb{K}$-isomorphism $u:\overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$ extending $v$, and therefore $x$, $y$ are conjugate. 
:::

From this, if an algebraic element $x\in \overline{\mathbb{K}}$ of degree $n$ is given, we know that elements conjugate to $x$ must be roots of the minimal polynomial of $x$, and hence there are at most $n$ such elements. Moreover, here, having *fewer* than $n$ elements conjugate to $x$ is exactly equivalent to the minimal polynomial of $x$ not being separable. That is, denoting the group of $\mathbb{K}$-automorphisms of $\overline{\mathbb{K}}$ by $\Aut_\mathbb{K}(\overline{\mathbb{K}})$, and letting $\Aut_\mathbb{K}\overline{\mathbb{K}}$ act on $\overline{\mathbb{K}}$ in a natural way, the collection of elements fixed by this action $\overline{\mathbb{K}}^{\Aut_{\mathbb{K}}(\overline{\mathbb{K}})}$ is exactly equal to $\mathbb{K}^{p^{-\infty}}$. Here, $p$ is the characteristic exponent of $\mathbb{K}$, and thus when $\ch(\mathbb{K})=0$, this collection is $\mathbb{K}$ itself. Indeed, that $x\in\overline{\mathbb{K}}$ is fixed by every $\mathbb{K}$-automorphism is equivalent to the only conjugate of $x$ being itself, that is, to the minimal polynomial $f$ of $x$ having a unique root in $\overline{\mathbb{K}}$, which in turn is equivalent to $f=(\x-x)^{p^e}=\x^{p^e}-x^{p^e}$ for some $e\geq 0$, that is, to $x$ being $p$-radical over $\mathbb{K}$. ([§Purely Inseparable Extensions, ⁋Lemma 3](/en/math/field_theory/purely_inseparable_extensions#lem3){: data-lid="4a13s" } and [§Purely Inseparable Extensions, ⁋Proposition 2](/en/math/field_theory/purely_inseparable_extensions#prop2){: data-lid="wpkaf" }) 

## Galois Extensions

::: Definition 4
A field extension $\mathbb{L}/\mathbb{K}$ is called a *quasi-Galois extension* or *normal extension* if $\mathbb{L}/\mathbb{K}$ is algebraic and any irreducible polynomial $f\in \mathbb{K}[\x]$ having a root in $\mathbb{L}$ splits into a product of linear factors in $\mathbb{L}[\x]$. 
:::

For a family $(f_i)$ of non-constant polynomials in $\mathbb{K}[\x]$, an extension of $\mathbb{K}$ in which each $f_i$ splits into a product of linear factors and that is generated by their roots is called a *splitting field* of this family. Then essentially, a quasi-Galois extension is nothing but another name for a splitting field.

::: Proposition 5
For an algebraic extension $\mathbb{L}/\mathbb{K}$, the following are all equivalent.

1. $\mathbb{L}/\mathbb{K}$ is quasi-Galois.
2. For any $x\in \mathbb{L}$, the conjugates of $x$ (in $\overline{\mathbb{K}}$) all belong to $\mathbb{L}$.
3. On $\overline{\mathbb{K}}$, any $\mathbb{K}$-automorphism sends $\mathbb{L}$ to $\mathbb{L}$.
4. From $\mathbb{L}$ to $\overline{\mathbb{K}}$, any $\mathbb{K}$-homomorphism lands in $\mathbb{L}$.
5. $\mathbb{L}$ is the splitting field of some family of non-constant polynomials $(f_i\in \mathbb{K}[\x])$.
:::
::: Proof
First, the equivalence of the third and fourth conditions follows from [Proposition 1](#prop1){: data-lid="4yhl5" }. On the other hand, a quasi-Galois extension can be viewed as the splitting field of the minimal polynomials of its elements, so the last condition is implied by the first. Meanwhile, if the last condition holds, then by the same logic as in [Proposition 1](#prop1){: data-lid="t8ojs" }, on $\overline{\mathbb{K}}$, any $\mathbb{K}$-automorphism sends roots of $f_i$ to roots of $f_i$, and hence sends $\mathbb{L}$ to $\mathbb{L}$. Thus the third condition holds. Also, if the third condition holds, since the conjugates of $x\in \mathbb{L}$ are, on $\overline{\mathbb{K}}$, images under a $\mathbb{K}$-automorphism of $x$, they all belong to $\mathbb{L}$, and from this the second condition holds. Therefore, since

$$(1)\implies (5)\implies (3)\iff (4)\implies (2)$$

it suffices to show $(2)\implies (1)$. To this end, suppose that, having a root in $\mathbb{L}$, a (monic) irreducible polynomial $f\in \mathbb{K}[\x]$ is given. Then, first, since $\overline{\mathbb{K}}$ is algebraically closed, $f$ is expressed in $\overline{\mathbb{K}}$ by the following equation

$$f(\x)=\prod_{i=1}^d (\x- a_i), \qquad a_i\in \overline{\mathbb{K}}$$

. Now each of the $a_i$ is conjugate, and hence by assumption they must all belong to $\mathbb{L}$. That is, $f$ splits into a product of linear factors in $\mathbb{L}[\x]$.
:::

From this, the following holds.

::: Corollary 6
The following hold. 

1. An algebraic extension $\mathbb{L}/\mathbb{K}$ is quasi-Galois if and only if the only conjugate of $\mathbb{L}$ is itself. 
2. For an algebraic extension $\mathbb{K}\subseteq \mathbb{L}\subseteq \mathbb{M}$, if $\mathbb{M}/\mathbb{K}$ is quasi-Galois, then so is $\mathbb{M}/\mathbb{L}$. 
3. Let a quasi-Galois extension $\mathbb{M}/\mathbb{K}$ and its subextension $\mathbb{L}/\mathbb{K}$ be given. Then for any $\mathbb{K}$-homomorphism $u: \mathbb{L}\rightarrow \overline{\mathbb{K}}$, we have $u(\mathbb{L})\subseteq \mathbb{M}$, and there exists on $\mathbb{M}$ a $\mathbb{K}$-automorphism $v$ extending it. 
4. For a field extension $\mathbb{K}'/\mathbb{K}$ and a quasi-Galois extension $\mathbb{L}/\mathbb{K}$ lying in a common extension, their compositum $\mathbb{K}'(\mathbb{L})$ is quasi-Galois over $\mathbb{K}'$. 
:::
::: Proof
1. By [Proposition 5](#prop5){: data-lid="kipxl" }, $\mathbb{L}/\mathbb{K}$ is quasi-Galois if and only if every automorphism of $\overline{\mathbb{K}}$ that is a $\mathbb{K}$-automorphism sends $\mathbb{L}$ to $\mathbb{L}$. 
2. Suppose $\mathbb{M}/\mathbb{K}$ is quasi-Galois. Then first, since $\overline{\mathbb{K}}$ is also an algebraic closure of $\mathbb{L}$, by [Proposition 5](#prop5){: data-lid="sc1wv" } it suffices to show that for any $\mathbb{L}$-automorphism $u: \overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$, we have $u(\mathbb{M})=\mathbb{M}$. But $\mathbb{M}$ is a quasi-Galois extension of $\mathbb{K}$, and since $u$ is an $\mathbb{L}$-automorphism, it is automatically a $\mathbb{K}$-automorphism as well. From this, we know that $u$ must satisfy the desired condition. 
3. From [Proposition 1](#prop1){: data-lid="58z28" }, we know that, extending $u$, there exists a $\mathbb{K}$-automorphism $v:\overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$. Here, its restriction to $\mathbb{M}$, by the assumption that $\mathbb{M}$ is quasi-Galois, must satisfy $v(\mathbb{M})=\mathbb{M}$, and therefore the desired claim holds. 
4. By [Proposition 5](#prop5){: data-lid="204xd" }, $\mathbb{L}$ is the splitting field of suitable $f_i\in \mathbb{K}[\x]$. Then $\mathbb{K}'(\mathbb{L})$ is the splitting field when viewing the same polynomials as elements of $\mathbb{K}'[\x]$, so by [Proposition 5](#prop5){: data-lid="4ysfx" } again, it is quasi-Galois over $\mathbb{K}'$. 
:::

As can be seen from the proof of the above corollary, the most important property characterizing a quasi-Galois extension $\mathbb{L}/\mathbb{K}$ is that any $\mathbb{K}$-automorphism sends $\mathbb{L}$ to $\mathbb{L}$. The following proposition is also obvious from this fact.

::: Proposition 7
In $\mathbb{K}$'s algebraic closure $\overline{\mathbb{K}}$, let quasi-Galois extensions $\mathbb{L}_i$ be given. Then both $\bigcap \mathbb{L}_i$ and $\mathbb{K}(\bigcup \mathbb{L}_i)$ are also quasi-Galois.
:::
::: Proof
Both extensions are subextensions of $\overline{\mathbb{K}}$, hence algebraic, so it suffices to verify only the third condition of [Proposition 5](#prop5){: data-lid="9i14v" }. On $\overline{\mathbb{K}}$, let an arbitrary $\mathbb{K}$-automorphism $u$ be given. Since each $\mathbb{L}_i$ is quasi-Galois, by [Proposition 5](#prop5){: data-lid="z76jn" } again we have $u(\mathbb{L}_i)=\mathbb{L}_i$.

First, since $u$ is bijective,

$$u\left(\bigcap_i\mathbb{L}_i\right)=\bigcap_iu(\mathbb{L}_i)=\bigcap_i\mathbb{L}_i$$

holds. On the other hand, since $u$ is a field automorphism fixing $\mathbb{K}$, for any subset $S\subseteq\overline{\mathbb{K}}$ we have $u(\mathbb{K}(S))=\mathbb{K}(u(S))$. Applying this to $S=\bigcup_i\mathbb{L}_i$ gives

$$u\left(\mathbb{K}\left(\bigcup_i\mathbb{L}_i\right)\right)=\mathbb{K}\left(\bigcup_iu(\mathbb{L}_i)\right)=\mathbb{K}\left(\bigcup_i\mathbb{L}_i\right)$$

so we obtain the desired result.
:::

In particular, for any set of elements of $\overline{\mathbb{K}}$, $S$, we can consider the smallest quasi-Galois extension containing it. By definition, after collecting all conjugates of each element of $S$, this is the extension of $\mathbb{K}$ generated by them. We call this the quasi-Galois extension generated by $S$.

In [Definition 4](#def4){: data-lid="0v1we" }, when we defined a quasi-Galois extension, we required that an irreducible polynomial $f$ split into a product of linear factors, but they did not need to be distinct. A Galois extension is obtained by adding the separability condition here.

::: Theorem 8
Let an algebraic extension $\mathbb{L}/\mathbb{K}$ and, on $\mathbb{L}$, a group of $\mathbb{K}$-automorphisms $\Gamma$ be given. The following are all equivalent. 

1. All elements of $\mathbb{L}$ that are $\Gamma$-invariant are elements of $\mathbb{K}$. 
2. $\mathbb{L}$ is a separable quasi-Galois extension of $\mathbb{K}$. 
3. For any $x\in \mathbb{L}$, the minimal polynomial of $x$, $f\in \mathbb{K}[\x]$, splits into a product of distinct linear factors in $\mathbb{L}[\x]$. 
:::
::: Proof
The equivalence of the second and third conditions follows from [Definition 4](#def4){: data-lid="teezh" } and [§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12){: data-lid="tn7xi" }. If $\mathbb{L}/\mathbb{K}$ is quasi-Galois, then for $x\in \mathbb{L}$ its minimal polynomial $f$ splits into a product of linear factors in $\mathbb{L}[\x]$, and if $\mathbb{L}/\mathbb{K}$ is separable, then by the first result of the same proposition $f$ is separable, so these linear factors are distinct. Conversely, if the third condition holds, an irreducible polynomial having a root in $\mathbb{L}$ is a scalar multiple of the minimal polynomial of that root, so it splits in $\mathbb{L}[\x]$, and since every element of $\mathbb{L}$ is a separable element, $\mathbb{L}/\mathbb{K}$ is separable by the second result of the same proposition. Therefore, it suffices to show that these are equivalent to the first condition. 

First assume the first condition. For any $x\in \mathbb{L}$ and its minimal polynomial $f\in \mathbb{K}[\x]$, we must show that $f$ splits into a product of distinct linear factors in $\mathbb{L}[\x]$. To this end, let the collection of all roots of $f$ in $\mathbb{L}$ be $S$, and define a new polynomial 

$$g(\x)=\prod_{a\in S}(\x-a)$$

then $g$ is an element of $\mathbb{L}[\x]$, and for any $\sigma\in\Gamma$, 

$$(\sigma\cdot g)(\x)=\prod_{a\in S}(\x-\sigma(a))=\prod_{a\in S}(\x-a)$$

so the coefficients of $g$ are unchanged by $\sigma$, and therefore from the assumption of the first condition, $g\in\mathbb{K}[\x]$. Now since $g(x)=0$, by [§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15){: data-lid="5zras" }, $f$ divides $g$. On the other hand, since $S$ is a subset of the roots of $f$, the degree of $g$ does not exceed the degree of $f$, and therefore the monic polynomials $f$ and $g$ are equal. That is, the third condition holds. 

Conversely, assume the third condition and show the first condition. If $x\in\mathbb{L}$ does not belong to $\mathbb{K}$, we must show that $x$ is sent to another element by some $\sigma\in\Gamma$. If we let the minimal polynomial of $x$ be $f$, then from $x\not\in\mathbb{K}$, $f$ has degree at least 2, and by assumption we can split it as 

$$f(\x)=\prod_{a\in R}(\x-a), \qquad \text{$R$ the set of conjugates of $x$ in $\overline{\mathbb{K}}$}$$

and on the other hand, since $\mathbb{L}/\mathbb{K}$ is quasi-Galois, there exists, sending $x$ to $a\in R$ distinct from itself, an automorphism of $\overline{\mathbb{K}}$ over $\mathbb{K}$, $u$, which by [Proposition 5](#prop5){: data-lid="d9ops" } is an automorphism of $\mathbb{L}$ over $\mathbb{K}$. From this we obtain the desired result.
:::

We may now define the following.

::: Definition 9
An algebraic extension $\mathbb{L}/\mathbb{K}$ is said to be *Galois* if $\mathbb{L}/\mathbb{K}$ satisfies the conditions of [Theorem 8](#thm8){: data-lid="lmkjf" }. 
:::

Then from the result of [Proposition 7](#prop7){: data-lid="zi8sx" } and the results on separable extensions we obtain the following two propositions.

::: Proposition 10
Inside an algebraic closure of $\mathbb{K}$, $\overline{\mathbb{K}}$, let a non-empty family $(\mathbb{L}_i)$ of Galois extensions be given. Then both $\bigcap \mathbb{L}_i$ and $\mathbb{K}(\bigcup \mathbb{L}_i)$ are also Galois. 
:::
::: Proof
By the second condition of [Theorem 8](#thm8){: data-lid="j455g" }, a Galois extension is the same as a separable quasi-Galois extension. That both extensions are quasi-Galois was seen in [Proposition 7](#prop7){: data-lid="m1370" }, so it suffices to check that they are separable.

First, $\bigcap_i\mathbb{L}_i$ is a subextension of the separable extension $\mathbb{L}_{i_0}/\mathbb{K}$, so it is separable. ([§Separable Extensions, ⁋Proposition 15](/en/math/field_theory/separable_extensions#prop15){: data-lid="6euhy" }) On the other hand, the elements of $\bigcup_i\mathbb{L}_i$ are each elements of a separable extension, so they are all separable elements over $\mathbb{K}$ (the first result of [§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12){: data-lid="vb0b2" }), and therefore $\mathbb{K}(\bigcup_i\mathbb{L}_i)$ is an extension generated by separable elements, so by the second result of the same proposition it is separable.
:::

::: Proposition 11
Let a Galois extension $\mathbb{L}/\mathbb{K}$ and a finite-degree subextension $\mathbb{M}/\mathbb{K}$ be given. Then, containing $\mathbb{M}$, there exists a suitable subextension of $\mathbb{L}/\mathbb{K}$, $\mathbb{N}/\mathbb{K}$, that is Galois of finite degree.
:::
::: Proof
Since $\mathbb{M}/\mathbb{K}$ is of finite degree, we can write $\mathbb{M}=\mathbb{K}(x_1,\ldots,x_n)$. Let $S$ be the set of all conjugates of $x_1,\ldots,x_n$ (in $\overline{\mathbb{K}}$). Each $x_i$ is algebraic, so it has only finitely many conjugates ([Proposition 3](#prop3){: data-lid="nq39i" }), and since $\mathbb{L}/\mathbb{K}$ is quasi-Galois, by the second condition of [Proposition 5](#prop5){: data-lid="od971" } they all belong to $\mathbb{L}$. That is, $S$ is a finite subset of $\mathbb{L}$, and since $\mathbb{N}=\mathbb{K}(S)$ is generated by finitely many algebraic elements, it is a subextension of finite degree containing $\mathbb{M}$.

We now show that $\mathbb{N}/\mathbb{K}$ is Galois. First, on $\overline{\mathbb{K}}$, any $\mathbb{K}$-automorphism $u$ sends conjugates to conjugates, so $u(S)=S$, and therefore $u(\mathbb{N})=\mathbb{K}(u(S))=\mathbb{N}$, whence by [Proposition 5](#prop5){: data-lid="0zuhg" }, $\mathbb{N}/\mathbb{K}$ is quasi-Galois. On the other hand, $\mathbb{N}$ is a subextension of the separable extension $\mathbb{L}/\mathbb{K}$, so it is separable ([§Separable Extensions, ⁋Proposition 15](/en/math/field_theory/separable_extensions#prop15){: data-lid="xr9mi" }), and therefore by the second condition of [Theorem 8](#thm8){: data-lid="0b681" } it is Galois.
:::

## Galois Group

As we have already seen, when dealing with a Galois extension $\mathbb{L}/\mathbb{K}$, what is importantly used is the collection on $\mathbb{L}$ of $\mathbb{K}$-automorphisms.

::: Definition 12
For a Galois extension $\mathbb{L}/\mathbb{K}$, the group of automorphisms of $\mathbb{L}$ that are $\mathbb{K}$-automorphisms is called the *Galois group* and is denoted $\Gal(\mathbb{L}/\mathbb{K})$.
:::

In particular, let us fix a field $\mathbb{K}$ and consider its algebraic closure $\overline{\mathbb{K}}$. In $\mathbb{K}[\x]$, for a separable polynomial $f$ and the set of roots of $f$, $A$, $\mathbb{L}=\mathbb{K}(A)$ is the splitting field of $f$ and thus quasi-Galois by [Proposition 5](#prop5){: data-lid="fsmgn" }, and since the minimal polynomial of each element of $A$ divides $f$ and has distinct roots ([§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15){: data-lid="iyncw" }), it is separable by the second result of [§Separable Extensions, ⁋Proposition 12](/en/math/field_theory/separable_extensions#prop12){: data-lid="hpe3j" }. That is, $\mathbb{L}$ is a Galois extension of $\mathbb{K}$. However, since $\mathbb{L}$ is generated by $A$, any $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$ is completely determined by its values on $A$, and from this an injective group homomorphism 

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow S_A$$

is induced. In general, this homomorphism need not be surjective. First, two elements of $A$, $x,y$, may not be conjugate to each other, which by [Proposition 3](#prop3){: data-lid="h15xq" } is equivalent to their having different minimal polynomials. On the other hand, since $x,y$ are roots of $f$, their minimal polynomials each divide $f$ by [§Algebraic Extensions, ⁋Theorem 15](/en/math/field_theory/algebraic_extensions#thm15){: data-lid="w6apq" }, so that $x$ and $y$ are not conjugate is equivalent to them being roots of different irreducible factors of $f$. That is, if the sets of roots of the irreducible factors of $f$ are denoted by $A_1,\ldots,A_r$, these are precisely the orbits of $\Gal(\mathbb{L}/\mathbb{K})$ on $A$, and the image of the above homomorphism is contained in the subgroup $S_{A_1}\times\cdots\times S_{A_r}$.

This inclusion is also generally not an equality, so even when $f$ is irreducible, the image need not be all of $S_A$. For instance, $f=\x^3-3\x+1\in \mathbb{Q}[\x]$ has no rational roots and is therefore irreducible, so its three roots are conjugate to each other. However, for a root of $f$, $\alpha$, using $\alpha^3=3\alpha-1$ one can compute that $\alpha^2-2$ is also a root of $f$, and since the sum of the three roots is $0$, the remaining one also belongs to $\mathbb{Q}(\alpha)$. That is, $\mathbb{L}=\mathbb{Q}(\alpha)$ is already the splitting field of $f$, and since any $\sigma\in\Gal(\mathbb{L}/\mathbb{Q})$ is determined by $\sigma(\alpha)$, the group $\Gal(\mathbb{L}/\mathbb{Q})$ has at most three elements, and its image cannot be all of $S_A$, which has six elements.

On the other hand, for a Galois extension $\mathbb{L}/\mathbb{K}$ and, as a subextension of $\mathbb{L}$, another Galois extension $\mathbb{M}/\mathbb{K}$, we obtain the following result from [Proposition 1](#prop1){: data-lid="wsb8k" }.

::: Proposition 13
In the above situation, the restriction homomorphism

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K});\qquad \sigma\mapsto \sigma\vert_\mathbb{M}$$

is surjective.
:::
::: Proof
First, let us verify that this map is well-defined. For any $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$, by [Proposition 1](#prop1){: data-lid="akrwl" }, extending $\sigma$, there exists on $\overline{\mathbb{K}}$ a $\mathbb{K}$-automorphism $v$. Since $\mathbb{M}/\mathbb{K}$ is quasi-Galois, by [Proposition 5](#prop5){: data-lid="8ndjx" } we have $v(\mathbb{M})=\mathbb{M}$, and therefore $\sigma\vert_\mathbb{M}=v\vert_\mathbb{M}$ is an automorphism of $\mathbb{M}$ which is a $\mathbb{K}$-automorphism, that is, an element of $\Gal(\mathbb{M}/\mathbb{K})$.

Now let us show surjectivity. Given any $\tau\in\Gal(\mathbb{M}/\mathbb{K})$, regarding $\tau$ as a homomorphism from $\mathbb{M}$ to $\overline{\mathbb{K}}$ that is a $\mathbb{K}$-homomorphism and applying [Proposition 1](#prop1){: data-lid="teanw" } again, extending $\tau$, we obtain on $\overline{\mathbb{K}}$ a $\mathbb{K}$-automorphism $u$. Then since $\mathbb{L}/\mathbb{K}$ is quasi-Galois, $u(\mathbb{L})=\mathbb{L}$, and $\sigma=u\vert_\mathbb{L}$ is an element of $\Gal(\mathbb{L}/\mathbb{K})$ with $\sigma\vert_\mathbb{M}=u\vert_\mathbb{M}=\tau$.
:::

---

**References**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.
