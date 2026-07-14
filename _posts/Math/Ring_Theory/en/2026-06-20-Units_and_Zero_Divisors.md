---
title: "Invertible Elements and Zero Divisors"
description: "We define units, zero divisors, and regular elements in a ring, and show that a unit is never a zero divisor. In finite commutative rings, we prove that every regular element is a unit using the injectivity of the multiplication map, and deduce as a corollary that every finite integral domain is a field."
excerpt: "Units, regular elements, and when regular elements become units in finite commutative rings"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/units_and_zero_divisors
sidebar: 
    nav: "ring_theory-en"

date: 2026-06-20

weight: 1
translated_at: 2026-07-14T05:30:02+00:00
translation_source: kimi-cli
---
In this post, we organize the two most fundamental classes of elements in the multiplicative structure of a ring: the *unit*, which has a multiplicative inverse, and the *zero divisor*, which has a partner that multiplies to $0$. These two concepts have already been used implicitly in many places. An integral domain was defined as a commutative ring with no zero divisors ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)), and a field was a division ring in which every nonzero element is a unit ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3)). Here we formally define the unit, verify that its collection forms a group, show that units and zero divisors are mutually exclusive, and then prove that in a finite commutative ring, every element that is not a zero divisor is automatically a unit. As an immediate corollary, we obtain that every finite integral domain is a field.

Unless otherwise stated, $A$ is a ring with identity $1\neq 0$, and commutativity is specified wherever needed.

## Units

::: Definition 1
An element $u\in A$ of a ring $A$ is called a *unit* if there exists an element $v$ in $A$ satisfying $uv=vu=1$. Such a $v$ is unique if it exists, and we write it as the *inverse* $u^{-1}$ of $u$. The set of all units of $A$ is denoted by $A^\times$.
:::

The uniqueness of the inverse follows immediately from the associativity of multiplication. For example, if $vu=1$ and $uw=1$, then

$$v=v\cdot 1=v(uw)=(vu)w=1\cdot w=w$$

so the left inverse and the right inverse coincide, and therefore the inverse of an element having inverses on both sides is unique.

Moreover, $A^\times$ is closed under multiplication. First, it is closed under the empty product, that is, $1\in A^\times$ is obvious from $1\cdot 1=1$. If $u,u'\in A^\times$, then

$$(uu')(u'^{-1}u^{-1})=u(u'u'^{-1})u^{-1}=uu^{-1}=1$$

and similarly $(u'^{-1}u^{-1})(uu')=1$, so $uu'\in A^\times$ and its inverse is $u'^{-1}u^{-1}$. Also, if $u\in A^\times$, then $u^{-1}$ has $u$ as its inverse, so $u^{-1}\in A^\times$. Therefore $A^\times$ is a group under the multiplication of $A$, and we call it the *unit group* of $A$.

::: Example 2
In the ring $\mathbb{Z}$, the integers $u,v$ satisfying $uv=1$ are only $u=v=1$ or $u=v=-1$, so $\mathbb{Z}^\times=\{1,-1\}$.

In any division ring $A$, every nonzero element has an inverse by definition, so $A^\times=A\setminus\{0\}$ ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3)). In particular, for a field $\mathbb{K}$, $\mathbb{K}^\times=\mathbb{K}\setminus\{0\}$ is a commutative group under multiplication.

One thing to note is that a unit in one ring may not be a unit in a particular subring. For example, $2\in\mathbb{Q}$ is an element of $\mathbb{Q}^\times$, but in $\mathbb{Z}$ there is no integer $v$ satisfying $2v=1$, so $2\not\in\mathbb{Z}^\times$.
:::

## Zero Divisors and Regular Elements

In the multiplicative structure, the opposite extreme of a unit can be said to be $0$. Extending this, we examine elements that multiply to $0$, namely zero divisors. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)) Let us first refine the definition a bit more.

::: Definition 3
For an element $a\in A$ of a ring $A$, we define the following.

1. $a$ is called a *left zero divisor* if there exists a nonzero element $b\neq 0$ such that $ab=0$.
2. Similarly, if $ba=0$ for some $b\neq 0$, we call $a$ a *right zero divisor*.
3. An element that is not a zero divisor is called a *regular element* or a non-zero-divisor.
:::

[\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5) does not distinguish between left zero divisors and right zero divisors, and encompasses both concepts. In particular, for a commutative ring, the distinction between them disappears, so there is no risk of confusion even if the direction is not specified.

By definition, $0$ itself is a zero divisor because it always yields $0$ when multiplied by any nonzero element (for example, $1$) as long as $A\neq 0$, and considering the contrapositive, a regular element must always be nonzero.

Our interest is in the relationship between regular elements and units. First, one direction always holds in a general ring.

::: Proposition 4
Any unit in a ring $A$ is a regular element.
:::
::: Proof
Suppose, for contradiction, that $u\in A^\times$ and $ub=0$ for some $b\in A$. Multiplying both sides on the left by $u^{-1}$,

$$b=1\cdot b=(u^{-1}u)b=u^{-1}(ub)=u^{-1}\cdot 0=0$$

so $b=0$, which is a contradiction. A similar argument works assuming $bu=0$, and therefore $u$ is a regular element.
:::

The above [Proposition 4](#prop4) shows that any unit is regular, but the converse does not generally hold. For example, in $\mathbb{Z}$, $2$ is easily verified to be a regular element, but $2$ is not a unit of $\mathbb{Z}$. ([Example 2](#ex2))

However, if the ring is *finite*, the converse does hold, because by the definition of a finite set ([\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Definition 1](/en/math/set_theory/natural_numbers#def1)), a function from a finite set to itself is automatically bijective if it is either surjective or injective.

::: Theorem 5
For a finite ring $A$ and any element $a$, being a regular element is equivalent to being a unit.
:::
::: Proof
By [Proposition 4](#prop4), a unit is always a regular element, so it suffices to show that a regular element is a unit. Let $a\in A$ be a regular element, and consider the multiplication map

$$\lambda_a:A\rightarrow A;\qquad x\mapsto ax$$

If $\lambda_a(x)=\lambda_a(y)$, then $a(x-y)=0$, and since $a$ is a regular element, $x-y=0$, that is, $x=y$. Therefore $\lambda_a$ is injective. But $A$ is a finite set, and an injective function from a finite set to itself is surjective, so $\lambda_a$ is surjective. Hence there exists $v\in A$ satisfying $\lambda_a(v)=1$, which means $av=1$. In a similar way, we can use the fact that the right multiplication map is surjective to construct a left inverse of $a$, and from the argument immediately following [Definition 1](#def1) we know that these two inverses must necessarily coincide.
:::

Then the most important corollary of this theorem concerns integral domains.

::: Corollary 6
Every finite integral domain is a field.
:::
::: Proof
By definition, any finite integral domain $A$ is commutative and $0\neq 1$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)) To further show that $A$ is a field, we need to show that every nonzero element is a unit; since an integral domain has no zero divisors other than $0$, any nonzero element $a$ is a regular element and therefore a unit by [Theorem 5](#thm5).
:::

## Examples

Now let us look at some examples of the above results.

::: Example 7
Consider the ring $\mathbb{Z}/n\mathbb{Z}$ defined for $n\geq 1$. An element $a+n\mathbb{Z}$ of this ring is a unit if and only if there exists some $x+n\mathbb{Z}$ such that

$$(a+n\mathbb{Z})(x+n\mathbb{Z})=1+n\mathbb{Z}$$

that is, there exist integers $x,k$ satisfying $ax-kn=1$. By [\[Number Theory\] §Euclidean Algorithm and Bézout's Identity, ⁋Theorem 3](/en/math/number_theory/euclidean_algorithm#thm3), the existence of such $x,k$ is equivalent to $\gcd(a,n)=1$, that is, $a$ being coprime to $n$, so

$$(\mathbb{Z}/n\mathbb{Z})^\times=\{a+n\mathbb{Z}:\gcd(a,n)=1\}$$

and the size of this group is $\varphi(n)$, the number of integers between $1$ and $n$ coprime to $n$ ([\[Number Theory\] §Euler's Theorem and the Phi Function, ⁋Definition 1](/en/math/number_theory/euler_theorem#def1)).

On the other hand, if $\gcd(a,n)=d>1$ and $a+n\mathbb{Z}\neq 0+n\mathbb{Z}$, then $a+n\mathbb{Z}$ is a zero divisor. This is because $n/d+n\mathbb{Z}\neq 0+n\mathbb{Z}$, and

$$(a+n\mathbb{Z})(n/d+n\mathbb{Z})=a\cdot(n/d)+n\mathbb{Z}=(a/d)n+n\mathbb{Z}=0+n\mathbb{Z}$$

Therefore, every nonzero element of $\mathbb{Z}/n\mathbb{Z}$ is either a unit or a zero divisor, and this classification again illustrates [Theorem 5](#thm5) well.

In particular, if $n=p$ is prime, then $1,\ldots,p-1$ are all coprime to $p$, so $(\mathbb{Z}/p\mathbb{Z})^\times=\mathbb{Z}/p\mathbb{Z}\setminus\{0+p\mathbb{Z}\}$, and $\mathbb{Z}/p\mathbb{Z}$ is a finite integral domain with no zero divisors. By [Corollary 6](#cor6), this is a field, and it is the *prime field* $\mathbb{F}_p$ with $p$ elements ([\[Field Theory\] §Fields, §§Prime Fields](/en/math/field_theory/fields#소체)).
:::

Meanwhile, the unit group of a product ring is determined componentwise. This is because multiplication in a product ring is computed componentwise.

::: Proposition 8
For the product $A=A_1\times\cdots\times A_n$ of rings $A_1,\ldots,A_n$, an element $(a_1,\ldots,a_n)$ is a unit of $A$ if and only if each $a_i$ is a unit of $A_i$. That is, as groups,

$$A^\times=A_1^\times\times\cdots\times A_n^\times$$

holds.
:::
::: Proof
Multiplication in $A$ is componentwise and the identity is $(1,\ldots,1)$. If an element $a=(a_1,\ldots,a_n)$ is a unit, then there exists $b=(b_1,\ldots,b_n)$ satisfying $ab=ba=(1,\ldots,1)$, which means $a_ib_i=b_ia_i=1$ in each component, so each $a_i$ is a unit and $b_i=a_i^{-1}$.

Conversely, if each $a_i$ is a unit, then $b=(a_1^{-1},\ldots,a_n^{-1})$ satisfies $ab=ba=(1,\ldots,1)$, so $a$ is a unit. Therefore $a\in A^\times$ is equivalent to each $a_i\in A_i^\times$, and the map

$$A^\times\longrightarrow A_1^\times\times\cdots\times A_n^\times,\qquad (a_1,\ldots,a_n)\longmapsto(a_1,\ldots,a_n)$$

is a well-defined bijection by the above equivalence, and since multiplication is componentwise, it is a group homomorphism, defining an isomorphism.
:::

On the other hand, in the case of a matrix ring, the unit group becomes the general linear group.

::: Example 9
Consider the ring $\Mat_n(R)$ of $n\times n$ matrices with entries in a ring $R$. By definition, a unit of $\Mat_n(R)$ is a matrix having a two-sided inverse under multiplication, that is, an invertible matrix. The set of all such matrices is called the *general linear group* and is written $\GL(n;R)$. That is,

$$\Mat_n(R)^\times=\GL(n;R)$$

([\[Multilinear Algebra\] §Matrices, ⁋Definition 1](/en/math/multilinear_algebra/matrices#def1)). It is known that if $R$ is a commutative ring, then a matrix $M\in \Mat_n(R)$ is invertible if and only if its determinant $\det M$ is an element of $R^\times$. ([\[Multilinear Algebra\] §Determinants, ⁋Corollary 3](/en/math/multilinear_algebra/determinants#cor3)) That is, in this case,

$$\GL(n;R)=\{M\in \Mat_n(R):\det M\in R^\times\}$$

For example, if $R=\mathbb{Z}$, then $\mathbb{Z}^\times=\{1,-1\}$, so $\GL(n;\mathbb{Z})$ consists of integer matrices with determinant $\pm 1$.

$\Mat_n(R)$ has nontrivial zero divisors when $n\geq 2$, so the distinction between units and zero divisors is meaningful. For example, for $n=2$, the matrix units

$$E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$

satisfy $E_{12}E_{11}=0$ but $E_{12}\neq 0$, $E_{11}\neq 0$, so both are zero divisors, and therefore are not invertible by [Proposition 4](#prop4).
:::

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
