---
title: "Units and Zero Divisors"
description: "We define units, zero divisors, and regular elements of a ring and show that a unit is never a zero divisor. Using the injectivity of multiplication maps, we prove that every regular element in a finite commutative ring is a unit, establishing that every finite integral domain is a field as a corollary."
excerpt: "Units, regular elements, and their equivalence in finite commutative rings"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/units_and_zero_divisors
sidebar: 
    nav: "ring_theory-en"

date: 2026-06-20


weight: 1
translated_at: 2026-09-26T07:15:06+00:00
translation_source: antigravity-gemini-3.8-flash-high
---
In this post, we organize the two most fundamental classes of elements in the multiplicative structure of a ring: *units*, which have multiplicative inverses, and *zero divisors*, which have a partner that multiplies to $0$. These two concepts have already been used implicitly in several places. An integral domain was defined as a commutative ring with no zero divisors ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5){: data-lid="94w7a" }), and a field was a commutative ring in which every nonzero element is a unit ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3){: data-lid="p7nwo" }). Here, we properly define units, verify that their collection forms a group, show that units and zero divisors are mutually exclusive, and then prove that in a finite ring, every element that is not a zero divisor is automatically a unit. As a direct consequence, we obtain that every finite integral domain is a field.

Unless otherwise specified, $A$ is a ring with identity $1\neq 0$, and commutativity is specified as needed.

## Units

::: Definition 1
An element $u\in A$ of a ring $A$ is a *unit* if there exists an element $v$ in $A$ satisfying $uv=vu=1$. Such $v$, if it exists, is unique, and we denote it as the *inverse* $u^{-1}$ of $u$. We denote the collection of all units of $A$ by $A^\times$.
:::

The uniqueness of the inverse follows immediately from the associativity of multiplication. For instance, if $vu=1$ and $uw=1$, then

$$v=v\cdot 1=v(uw)=(vu)w=1\cdot w=w$$

so the left inverse and right inverse coincide, and therefore an element that has an inverse on both sides has a unique inverse.

Moreover, $A^\times$ is closed under multiplication. First, being closed under the empty product, that is, $1\in A^\times$, is obvious from $1\cdot 1=1$, and if $u,u'\in A^\times$, then

$$(uu')(u'^{-1}u^{-1})=u(u'u'^{-1})u^{-1}=uu^{-1}=1$$

and in the same manner $(u'^{-1}u^{-1})(uu')=1$, so $uu'\in A^\times$ and its inverse is $u'^{-1}u^{-1}$. In addition, if $u\in A^\times$, then $u^{-1}$ also has $u$ as its inverse, so $u^{-1}\in A^\times$. Therefore, $A^\times$ is a group with the multiplication of $A$ as its operation, which we call the *unit group* of $A$.

::: Example 2
In the ring $\mathbb{Z}$, the only integers $u,v$ satisfying $uv=1$ are $u=v=1$ or $u=v=-1$, so $\mathbb{Z}^\times=\{1,-1\}$.

In any division ring $A$, every element except $0$ has an inverse by definition, so $A^\times=A\setminus\{0\}$ ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 3](/en/math/algebraic_structures/field_of_fractions#def3){: data-lid="8hpq8" }). In particular, for a field $\mathbb{K}$, $\mathbb{K}^\times=\mathbb{K}\setminus\{0\}$ is an abelian group under multiplication.

One thing to note is that a unit of a ring may not be a unit in a particular subring of it. For example, $2\in\mathbb{Q}$ is an element of $\mathbb{Q}^\times$, but since there is no integer $v$ satisfying $2v=1$ in $\mathbb{Z}$, we have $2\not\in\mathbb{Z}^\times$.
:::

## Zero Divisors and Regular Elements

In the multiplicative structure, the opposite extreme of a unit can be said to be $0$. Extending this, we examine elements that multiply together to give $0$, namely zero divisors ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5){: data-lid="xqcr3" }). First, let us refine the definition in more detail.

::: Definition 3
For an element $a\in A$ of a ring $A$, we define the following:

1. $a$ is a *left zero divisor* if there exists a nonzero element $b\neq 0$ such that $ab=0$.
2. Similarly, $a$ is called a *right zero divisor* if $ba=0$ for some $b\neq 0$.
3. An element that is not a zero divisor is called a *regular element* or a non-zero-divisor.
:::

[\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5){: data-lid="wdywa" } was stated without distinguishing between left and right zero divisors, encompassing both of these concepts. In particular, for commutative rings, this distinction disappears, so there is no ambiguity even without specifying a direction.

By definition, as long as $A\neq 0$, $0$ itself is a zero divisor since multiplying it by a nonzero element (for instance, $1$) always gives $0$, and considering the contrapositive, a regular element must always be nonzero.

Our interest lies in the relationship between regular elements and units. First, one direction always holds in a general ring.

::: Proposition 4
Any unit of a ring $A$ is a regular element.
:::
::: Proof
Let $u\in A^\times$, and suppose for the sake of contradiction that $ub=0$ for some $b\neq 0$. Multiplying both sides by $u^{-1}$ on the left, we have

$$b=1\cdot b=(u^{-1}u)b=u^{-1}(ub)=u^{-1}\cdot 0=0$$

so $b=0$, which contradicts $b\neq 0$. A similar argument holds if we assume $bu=0$, and therefore $u$ is a regular element.
:::

The above [Proposition 4](#prop4){: data-lid="yqlgq" } shows that any unit is regular, but in general the converse does not hold. For instance, in $\mathbb{Z}$, one can easily check that $2$ is a regular element, but $2$ is not a unit of $\mathbb{Z}$ ([Example 2](#ex2){: data-lid="cx3y6" }).

However, if the ring is a *finite* ring, the converse holds; this is because, fundamentally by the definition of a finite set ([\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Definition 1](/en/math/set_theory/natural_numbers#def1){: data-lid="gkwn4" }), a function from a finite set to itself is automatically guaranteed to be bijective as long as it is surjective or injective.

::: Theorem 5
For a finite ring $A$ and any element $a$, $a$ is a regular element if and only if it is a unit.
:::
::: Proof
By [Proposition 4](#prop4){: data-lid="o9enb" }, a unit is always a regular element, so it suffices to show that a regular element is a unit. Let $a\in A$ be a regular element, and consider the multiplication map

$$\lambda_a:A\rightarrow A;\qquad x\mapsto ax$$

Then if $\lambda_a(x)=\lambda_a(y)$, we have $a(x-y)=0$, and since $a$ is a regular element, $x-y=0$, that is, $x=y$. Thus $\lambda_a$ is injective. However, $A$ is a finite set, and an injective map from a finite set to itself is surjective, so $\lambda_a$ is surjective. Therefore, $\lambda_a(v)=1$ for some $v\in A$, which means $av=1$. In a similar manner, using the fact that the right multiplication map is surjective, we can construct a left inverse of $a$, and from the argument immediately following [Definition 1](#def1){: data-lid="ivfgz" }, we know that these two inverses must coincide.
:::

The most important consequence of this theorem concerns integral domains.

::: Corollary 6
Every finite integral domain is a field.
:::
::: Proof
By definition, any finite integral domain $A$ is commutative and $0\neq 1$. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5){: data-lid="lia9q" }) Now, to further show that $A$ is a field, it suffices to show that every nonzero element is a unit. Since an integral domain has no zero divisors other than $0$, any nonzero element $a$ is a regular element, and thus by [Theorem 5](#thm5){: data-lid="y5bb5" }, $a$ is a unit.
:::

## Examples

We now look at examples of the above results.

::: Example 7
For $n\geq 1$, consider the ring $\mathbb{Z}/n\mathbb{Z}$. For an element $a+n\mathbb{Z}$ of this ring to be a unit means that there exists some $x+n\mathbb{Z}$ such that

$$(a+n\mathbb{Z})(x+n\mathbb{Z})=1+n\mathbb{Z}$$

holds. That is, for some integers $x,k$, the equation $ax-kn=1$ holds. By [\[Number Theory\] §Euclidean Algorithm and Bézout's Identity, ⁋Proposition 5](/en/math/number_theory/euclidean_algorithm#prop5){: data-lid="svu88" }, the existence of such $x,k$ is equivalent to $\gcd(a,n)=1$, that is, $a$ being coprime to $n$, so

$$(\mathbb{Z}/n\mathbb{Z})^\times=\{a+n\mathbb{Z}\mid\gcd(a,n)=1\}$$

and the order of this group is the number of integers coprime to $n$ between $1$ and $n$, which is $\varphi(n)$ ([\[Number Theory\] §Euler's Theorem and the Phi Function, ⁋Definition 1](/en/math/number_theory/euler_theorem#def1){: data-lid="g583e" }).

On the other hand, if $\gcd(a,n)=d>1$ and $a+n\mathbb{Z}\neq 0+n\mathbb{Z}$, then $a+n\mathbb{Z}$ is a zero divisor. This is because $n/d+n\mathbb{Z}\neq 0+n\mathbb{Z}$ and

$$(a+n\mathbb{Z})(n/d+n\mathbb{Z})=a\cdot(n/d)+n\mathbb{Z}=(a/d)n+n\mathbb{Z}=0+n\mathbb{Z}$$

. Therefore, every nonzero element of $\mathbb{Z}/n\mathbb{Z}$ is either a unit or a zero divisor, and this classification once again illustrates [Theorem 5](#thm5){: data-lid="27kkl" }.

In particular, if $n=p$ is prime, then $1,\ldots,p-1$ are all coprime to $p$, so $(\mathbb{Z}/p\mathbb{Z})^\times=\mathbb{Z}/p\mathbb{Z}\setminus\{0+p\mathbb{Z}\}$, and $\mathbb{Z}/p\mathbb{Z}$ is a finite integral domain having no zero divisors other than $0$. By [Corollary 6](#cor6){: data-lid="4o12k" }, this is a field; this is the *prime field* with $p$ elements, $\mathbb{F}_p$ ([\[Field Theory\] §Fields, §§Prime Fields](/en/math/field_theory/fields#prime-fields){: data-lid="w7bat" }).
:::

Meanwhile, the unit group of a product ring is determined componentwise. This is because multiplication in a product ring is computed componentwise.

::: Proposition 8
For rings $A_1,\ldots,A_n$ and their product $A=A_1\times\cdots\times A_n$, an element $(a_1,\ldots,a_n)$ is a unit of $A$ if and only if each $a_i$ is a unit of $A_i$. That is, as groups,

$$A^\times=A_1^\times\times\cdots\times A_n^\times$$

holds.
:::
::: Proof
Multiplication in $A$ is performed componentwise, and the identity is $(1,\ldots,1)$. If an element $a=(a_1,\ldots,a_n)$ is a unit, then $ab=ba=(1,\ldots,1)$ holds for some $b=(b_1,\ldots,b_n)$, which means that $a_ib_i=b_ia_i=1$ in each component; thus each $a_i$ is a unit and $b_i=a_i^{-1}$.

Conversely, if each $a_i$ is a unit, then $b=(a_1^{-1},\ldots,a_n^{-1})$ satisfies $ab=ba=(1,\ldots,1)$, so $a$ is a unit. Therefore, $a\in A^\times$ is equivalent to each $a_i\in A_i^\times$, and the morphism

$$A^\times\rightarrow A_1^\times\times\cdots\times A_n^\times;\quad (a_1,\ldots,a_n)\mapsto(a_1,\ldots,a_n)$$

is a well-defined bijection by the equivalence above, and since multiplication is componentwise, it is a group homomorphism, defining an isomorphism.
:::

Meanwhile, for matrix rings, the unit group is the general linear group.

::: Example 9
For a ring $R$, consider the ring of $n\times n$ matrices $\Mat_n(R)$ with entries from the ring. By definition, a unit of $\Mat_n(R)$ is a matrix having a two-sided multiplicative inverse, that is, an invertible matrix. The collection of all such matrices is called the *general linear group* and denoted by $\GL(n;R)$. That is,

$$\Mat_n(R)^\times=\GL(n;R)$$

([\[Multilinear Algebra\] §Change of Basis, ⁋Definition 3](/en/math/multilinear_algebra/change_of_basis#def3){: data-lid="l6ryk" }). When $R$ is a commutative ring, it is known that a matrix $M\in \Mat_n(R)$ is invertible if and only if its determinant $\det M$ is an element of $R^\times$ ([\[Multilinear Algebra\] §Determinants, ⁋Corollary 3](/en/math/multilinear_algebra/determinants#cor3){: data-lid="o6xrr" }). That is, in this case,

$$\GL(n;R)=\{M\in \Mat_n(R)\mid\det M\in R^\times\}$$

holds. For example, if $R=\mathbb{Z}$, then $\mathbb{Z}^\times=\{1,-1\}$, so $\GL(n;\mathbb{Z})$ consists of integer matrices with determinant $\pm 1$.

The ring $\Mat_n(R)$ has nontrivial zero divisors when $n\geq 2$, so the distinction between units and zero divisors is meaningful. For instance, when $n=2$, the matrix units

$$E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$

satisfy $E_{12}E_{11}=0$ while $E_{12}\neq 0$ and $E_{11}\neq 0$, so both are zero divisors and therefore not invertible by [Proposition 4](#prop4){: data-lid="40rtx" }.
:::

---

**References**

**[AM]** M. F. Atiyah and I. G. Macdonald, *Introduction to commutative algebra*, Addison–Wesley, 1969.  
**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.  
**[Lam]** T. Y. Lam, *A first course in noncommutative rings*, 2nd ed., Graduate Texts in Mathematics 131, Springer, 2001.
