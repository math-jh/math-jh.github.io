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
translated_at: 2026-07-14T06:00:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-14T06:00:04+00:00
---
In this post we organize the two most fundamental classes of elements in the multiplicative structure of a ring: the *unit*, which possesses a multiplicative inverse, and the *zero divisor*, which has a partner multiplying to $0$. Both concepts have already appeared implicitly in many places. An integral domain was defined as a commutative ring with no zero divisors ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)), and a field was a division ring in which every nonzero element is a unit ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3)). Here we formally define the unit, verify that its collection forms a group, show that units and zero divisors are mutually exclusive, and prove that in a finite commutative ring every element that is not a zero divisor is automatically a unit. As an immediate corollary we obtain that every finite integral domain is a field.

Unless otherwise stated, $A$ denotes a ring with identity $1\neq 0$; commutativity is assumed only where explicitly needed.

## Units

::: Definition 1
An element $u\in A$ of a ring $A$ is called a *unit* if there exists an element $v$ in $A$ satisfying $uv=vu=1$. Such a $v$ is unique when it exists, and we denote it by the *inverse* $u^{-1}$ of $u$. The set of all units of $A$ is written $A^\times$.
:::

The uniqueness of the inverse follows immediately from the associativity of multiplication. For instance, if $vu=1$ and $uw=1$, then

$$v=v\cdot 1=v(uw)=(vu)w=1\cdot w=w$$

so the left and right inverses agree, and hence the inverse of an element possessing inverses on both sides is unique.

Moreover, $A^\times$ is closed under multiplication. Closure under the empty product—that is, $1\in A^\times$—is clear from $1\cdot 1=1$. If $u,u'\in A^\times$, then

$$(uu')(u'^{-1}u^{-1})=u(u'u'^{-1})u^{-1}=uu^{-1}=1$$

and similarly $(u'^{-1}u^{-1})(uu')=1$, so $uu'\in A^\times$ and its inverse is $u'^{-1}u^{-1}$. Also, if $u\in A^\times$, then $u^{-1}$ has $u$ as its inverse, so $u^{-1}\in A^\times$. Therefore $A^\times$ is a group under the multiplication of $A$, called the *unit group* of $A$.

::: Example 2
In the ring $\mathbb{Z}$, the only integers $u,v$ satisfying $uv=1$ are $u=v=1$ or $u=v=-1$, so $\mathbb{Z}^\times=\{1,-1\}$.

In any division ring $A$, every nonzero element has an inverse by definition, so $A^\times=A\setminus\{0\}$ ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3)). In particular, for a field $\mathbb{K}$, the set $\mathbb{K}^\times=\mathbb{K}\setminus\{0\}$ is an abelian group under multiplication.

One subtlety is that a unit in a ring need not remain a unit in a given subring. For example, $2\in\mathbb{Q}$ lies in $\mathbb{Q}^\times$, yet in $\mathbb{Z}$ there is no integer $v$ with $2v=1$, so $2\not\in\mathbb{Z}^\times$.
:::

## Zero Divisors and Regular Elements

In the multiplicative structure, the opposite extreme from a unit may be said to be $0$. Extending this, we examine elements that multiply to $0$, namely zero divisors. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)) Let us first refine the definition a little further.

::: Definition 3
For an element $a\in A$ of a ring $A$, we define the following.

1. $a$ is a *left zero divisor* if there exists a nonzero element $b\neq 0$ such that $ab=0$.
2. Likewise, if $ba=0$ for some $b\neq 0$, we call $a$ a *right zero divisor*.
3. An element that is not a zero divisor is called a *regular element* or a non-zero-divisor.
:::

[\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5) does not distinguish between left and right zero divisors, and encompasses both notions. In particular, in a commutative ring this distinction vanishes, so omitting the direction causes no confusion.

By definition, $0$ itself is a zero divisor: whenever $A\neq 0$, multiplying $0$ by any nonzero element (for instance $1$) yields $0$. The contrapositive shows that every regular element must be nonzero.

Our interest lies in the relationship between regular elements and units. One direction always holds in an arbitrary ring.

::: Proposition 4
Every unit in a ring $A$ is a regular element.
:::
::: Proof
Suppose, for contradiction, that $u\in A^\times$ and $ub=0$ for some $b\neq 0$. Multiplying both sides on the left by $u^{-1}$ gives

$$b=1\cdot b=(u^{-1}u)b=u^{-1}(ub)=u^{-1}\cdot 0=0$$

so $b=0$, a contradiction. A similar argument applies assuming $bu=0$, and therefore $u$ is a regular element.
:::

[Proposition 4](#prop4) shows that every unit is regular, but the converse fails in general. For example, in $\mathbb{Z}$ the element $2$ is easily seen to be regular, yet it is not a unit. ([Example 2](#ex2))

However, if the ring is *finite*, the converse does hold. This rests essentially on the definition of a finite set ([\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Definition 1](/en/math/set_theory/natural_numbers#def1)): a function from a finite set to itself is automatically bijective as soon as it is either injective or surjective.

::: Theorem 5
In a finite ring $A$, an element is a regular element if and only if it is a unit.
:::
::: Proof
By [Proposition 4](#prop4) every unit is regular, so it suffices to show that a regular element is a unit. Let $a\in A$ be regular, and consider the left multiplication map

$$\lambda_a:A\rightarrow A;\qquad x\mapsto ax$$

If $\lambda_a(x)=\lambda_a(y)$, then $a(x-y)=0$, and since $a$ is regular we have $x-y=0$, i.e. $x=y$. Thus $\lambda_a$ is injective. But $A$ is finite, and an injective self-map of a finite set is surjective; hence $\lambda_a$ is surjective. Therefore there exists $v\in A$ with $\lambda_a(v)=1$, which means $av=1$. In the same way, surjectivity of the right multiplication map yields a left inverse for $a$, and the argument immediately following [Definition 1](#def1) shows that these two inverses must coincide.
:::

The most important corollary of this theorem concerns integral domains.

::: Corollary 6
Every finite integral domain is a field.
:::
::: Proof
By definition any finite integral domain $A$ is commutative and satisfies $0\neq 1$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)) To show further that $A$ is a field, we must verify that every nonzero element is a unit. Since an integral domain has no zero divisors other than $0$, any nonzero element $a$ is regular and hence a unit by [Theorem 5](#thm5).
:::

## Examples

Now let us examine some examples illustrating the results above.

::: Example 7
Consider the ring $\mathbb{Z}/n\mathbb{Z}$ defined for $n\geq 1$. An element $a+n\mathbb{Z}$ of this ring is a unit precisely when there exists some $x+n\mathbb{Z}$ such that

$$(a+n\mathbb{Z})(x+n\mathbb{Z})=1+n\mathbb{Z}$$

that is, when there exist integers $x,k$ satisfying $ax-kn=1$. By [\[Number Theory\] §Euclidean Algorithm and Bézout's Identity, ⁋Theorem 3](/en/math/number_theory/euclidean_algorithm#thm3), the existence of such $x,k$ is equivalent to $\gcd(a,n)=1$, i.e. to $a$ being coprime to $n$. Consequently,

$$(\mathbb{Z}/n\mathbb{Z})^\times=\{a+n\mathbb{Z}\mid\gcd(a,n)=1\}$$

and the order of this group is $\varphi(n)$, the number of integers between $1$ and $n$ coprime to $n$ ([\[Number Theory\] §Euler's Theorem and the Phi Function, ⁋Definition 1](/en/math/number_theory/euler_theorem#def1)).

On the other hand, if $\gcd(a,n)=d>1$ and $a+n\mathbb{Z}\neq 0+n\mathbb{Z}$, then $a+n\mathbb{Z}$ is a zero divisor. Indeed, $n/d+n\mathbb{Z}\neq 0+n\mathbb{Z}$ and

$$(a+n\mathbb{Z})(n/d+n\mathbb{Z})=a\cdot(n/d)+n\mathbb{Z}=(a/d)n+n\mathbb{Z}=0+n\mathbb{Z}$$

Hence every nonzero element of $\mathbb{Z}/n\mathbb{Z}$ is either a unit or a zero divisor, and this classification again illustrates [Theorem 5](#thm5).

In particular, when $n=p$ is prime, the integers $1,\ldots,p-1$ are all coprime to $p$, so $(\mathbb{Z}/p\mathbb{Z})^\times=\mathbb{Z}/p\mathbb{Z}\setminus\{0+p\mathbb{Z}\}$ and $\mathbb{Z}/p\mathbb{Z}$ is a finite integral domain with no zero divisors. By [Corollary 6](#cor6) it is a field, namely the *prime field* $\mathbb{F}_p$ with $p$ elements ([\[Field Theory\] §Fields, §§Prime Fields](/en/math/field_theory/fields#prime-fields)).
:::

Meanwhile, the unit group of a product ring is determined componentwise, because multiplication in a product ring is computed componentwise.

::: Proposition 8
For the product $A=A_1\times\cdots\times A_n$ of rings $A_1,\ldots,A_n$, an element $(a_1,\ldots,a_n)$ is a unit of $A$ if and only if each $a_i$ is a unit of $A_i$. That is, as groups,

$$A^\times=A_1^\times\times\cdots\times A_n^\times$$

holds.
:::
::: Proof
Multiplication in $A$ is componentwise and the identity is $(1,\ldots,1)$. If $a=(a_1,\ldots,a_n)$ is a unit, then there exists $b=(b_1,\ldots,b_n)$ with $ab=ba=(1,\ldots,1)$, which means $a_ib_i=b_ia_i=1$ in each component; thus each $a_i$ is a unit and $b_i=a_i^{-1}$.

Conversely, if each $a_i$ is a unit, then $b=(a_1^{-1},\ldots,a_n^{-1})$ satisfies $ab=ba=(1,\ldots,1)$, so $a$ is a unit. Therefore $a\in A^\times$ is equivalent to each $a_i\in A_i^\times$, and the map

$$A^\times\longrightarrow A_1^\times\times\cdots\times A_n^\times,\qquad (a_1,\ldots,a_n)\longmapsto(a_1,\ldots,a_n)$$

is a well-defined bijection by the above equivalence; since multiplication is componentwise, it is a group homomorphism, hence an isomorphism.
:::

On the other hand, for a matrix ring the unit group becomes the general linear group.

::: Example 9
Consider the ring $\Mat_n(R)$ of $n\times n$ matrices with entries in a ring $R$. By definition, a unit of $\Mat_n(R)$ is a matrix possessing a two-sided inverse under multiplication, i.e. an invertible matrix. The set of all such matrices is called the *general linear group* and denoted $\GL(n;R)$. Thus

$$\Mat_n(R)^\times=\GL(n;R)$$

([\[Multilinear Algebra\] §Matrices, ⁋Definition 1](/en/math/multilinear_algebra/matrices#def1)). It is known that when $R$ is a commutative ring, a matrix $M\in \Mat_n(R)$ is invertible if and only if its determinant $\det M$ lies in $R^\times$. ([\[Multilinear Algebra\] §Determinants, ⁋Corollary 3](/en/math/multilinear_algebra/determinants#cor3)) Hence in this case

$$\GL(n;R)=\{M\in \Mat_n(R)\mid\det M\in R^\times\}$$

For example, if $R=\mathbb{Z}$, then $\mathbb{Z}^\times=\{1,-1\}$, so $\GL(n;\mathbb{Z})$ consists of the integer matrices with determinant $\pm 1$.

When $n\geq 2$, the ring $\Mat_n(R)$ contains nontrivial zero divisors, so the distinction between units and zero divisors is meaningful. For instance, when $n=2$ the matrix units

$$E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$

satisfy $E_{12}E_{11}=0$ while $E_{12}\neq 0$ and $E_{11}\neq 0$; thus both are zero divisors and hence not invertible by [Proposition 4](#prop4).
:::

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.

**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
