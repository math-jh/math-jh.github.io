---
title: "Polynomial Rings"
description: "We define polynomial rings over commutative rings and examine the degree of a polynomial and homogeneous polynomials. We cover the representation of polynomials via monomials, properties of degree, leading terms, and monic polynomials."
excerpt: "Factorization in polynomial rings over commutative rings and Gauss's lemma"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/polynomial_rings
sidebar: 
    nav: "ring_theory-en"

date: 2025-05-06
weight: 3
translated_at: 2026-06-26T23:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-26T23:00:01+00:00
---
<div class="remark" markdown="1">

<ins id="rmk">**Remark**</ins> In this post, $$A$$ is always a commutative ring.

</div>

We defined the polynomial algebra $$A[\x_i]_{i\in I}$$ for an arbitrary (commutative) ring $$A$$ in [\[Algebraic Structures\] §Algebras, ⁋Definition 7](/en/math/algebraic_structures/algebras#def7). This carries an $$A$$-algebra structure, but since the scalar multiplication of $$A$$ on $$A[\x_i]_{i\in I}$$ arises from the inclusion $$A\hookrightarrow A[\x_i]_{i\in I}$$ when we regard $$A[\x_i]_{i\in I}$$ as a ring, it suffices to consider $$A[\x_i]_{i\in I}$$ merely as a ring when studying its properties.

## Degree of Polynomials

Before treating polynomials in earnest, let us first define the tools needed to handle them. By a *polynomial* defined over $$A$$ we mean an element of the polynomial ring $$P=A[\x_i]_{i\in I}$$. Let $$\mathbb{N}^{(I)}$$ denote the set of finitely supported functions from $$I$$ to $$\mathbb{N}$$:

$$\mathbb{N}^{(I)}=\{\nu:I \rightarrow \mathbb{N}\mid\text{$f(i)=0$ for all but finitely many $i\in I$}\}$$

For any $$\nu\in \mathbb{N}^{(I)}$$, setting

$$\x^\nu=\prod_{i\in I} \x_i^{\nu_i}$$

makes $$\x^\nu$$ an element of $$P$$. We call elements of the form

$$a\x^\nu$$

*monomials*. Then any polynomial $$u$$ can be expressed as a finite sum of monomials

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu=0$ for all but finitely many $\nu$}$$

On the other hand, for any $$\nu\in \mathbb{N}^{(I)}$$, defining

$$\lvert\nu\rvert=\sum_{i\in I} \nu_i$$

allows us to view $$P=A[\x_i]_{i\in I}$$ as an $$\mathbb{N}$$-graded ring

$$P=\bigoplus_{n\in \mathbb{N}}\bigoplus_{\lvert\nu\rvert=n}(A[\x_i]_{i\in I})_\nu=\bigoplus_{n\in \mathbb{N}} P_n$$

For each $$n$$, we call the elements of $$P_n$$ *homogeneous polynomials* of degree $$n$$. Also, for any polynomial $$u\in P$$, we write the component of $$u$$ of degree $$n$$ in this homogeneous decomposition as $$u_n$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let an arbitrary element of the polynomial ring $$P=A[\x]_{i\in I}$$

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu=0$ for all but finitely many $\nu$}$$

be given. Then we call the largest $$n$$ satisfying $$u_n\neq 0$$ the *degree* of $$u$$, and denote it by $$\deg(u)$$. By definition, the degree of a polynomial having only a constant term is $$0$$, but in particular for the additive identity $$0$$ of $$P$$, we define $$\deg(0)=-\infty$$.

</div>

Then the following proposition holds trivially.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For two polynomials $$u,v$$, the following hold.

1. If $$\deg (u)\neq\deg(v)$$, then $$u+v\neq 0$$ and the equality

    $$\deg(u+v)=\sup(\deg(u), \deg(v))$$

    holds. If $$\deg(u)=\deg(v)$$, then the inequality $$\deg(u+v)\leq\deg(u)$$ holds.
2. The inequality $$\deg(uv)\leq\deg(u)+\deg(v)$$ holds.

</div>

The reason the second condition of this proposition is not an equality lies in $$A$$. To examine this more closely, consider the polynomial ring $$A[\x]$$ in one variable. Then any polynomial of $$A[\x]$$ can be written in the form

$$u(\x)=\sum_{i=0}^n a_i\x^i\qquad\text{($a_n\neq 0$)}$$

and we call $$a_n\x^n$$ the *leading term* of the polynomial $$p$$, and its coefficient $$a_n$$ the *leading coefficient* of the polynomial $$p$$. If the leading coefficient of $$p$$ is $$1$$, we call $$p$$ a *monic polynomial*.

Now for any two (univariate) polynomials

$$u(\x)=\sum_{i=0}^n a_i\x^i,\qquad v(\x)=\sum_{j=0}^m b_j \x^j$$

their product is explicitly given by the formula

$$u(\x)v(\x)=\sum_{k=0}^{n+m}\left(\sum_{i=0}^k a_ib_{k-i}\right)\x^k$$

and therefore the coefficient of the highest degree term is $$a_nb_m$$. However, if $$A$$ is not an integral domain, the product of two nonzero elements $$a_n$$, $$b_m$$ could be $$0$$, so $$uv$$ might not be a polynomial of degree $$m+n$$. Using this discussion, we obtain the following.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> For an integral domain $$A$$, the following hold.

1. For any $$u,v\in A[\x]$$, we have $$\deg(uv)=\deg(u)+\deg(v)$$.
2. The units of $$A[\x]$$ are exactly the units of $$A$$.
3. $$A[\x]$$ is an integral domain.

</div>

Now let us return to the general case. If any two polynomials $$u,v\in A[\x_i]_{i\in I}$$ are given, since only finitely many indeterminates appear in these polynomials, when computing $$uv$$ it suffices to consider $$A[\x_j]_{j\in J}$$ for some finite set $$J\subset I$$ instead of $$A[\x_i]_{i\in I}$$. Then the fact that $$A[\x_j]_{j\in J}$$ is an integral domain follows from [Lemma 3](#lem3) and the isomorphism

$$A[\x_1,\x_2]\cong (A[\x_1])[\x_2]$$

That is, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For an integral domain $$A$$ and a polynomial ring $$P=A[\x_i]_{i\in I}$$, the following hold.

1. For any $$u,v\in P$$, we have $$\deg(uv)=\deg(u)+\deg(v)$$.
2. The units of $$P$$ are exactly the units of $$A$$.
3. $$P$$ is an integral domain.

</div>

## Univariate Polynomials

We now examine univariate polynomials in somewhat more detail.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let a polynomial $$u(\x)$$ of degree $$m$$ and a polynomial $$v(\x)$$ of degree $$n$$ in $$A[\x]$$ be given, and let the leading coefficient of $$v$$ be $$b_n$$. Setting $$k=\sup(m-n+1,0)$$, there exist $$q,r\in A[\x]$$ satisfying the formula

$$b_n^k u=qv+r,\qquad \deg r < n$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$n>m$$, then $$k=0$$, and in this case setting $$q=0$$, $$r=u$$ satisfies the given formula, so there is nothing to prove in this case. Therefore, assume $$n\leq m$$.

We use induction on $$m$$. Let the leading coefficient of $$u$$ be $$a_m$$. If

$$v(\x)=\sum_{j=0}^n b_j\x^j$$

then there exists a polynomial $$u_1\in A[\x]$$ of degree less than $$m$$ such that

$$b_n^k u(\x)=b_n^{k-1}a_m\x^{m-n}v(\x)+b_n^{k-1}u_1(\x)$$

This formula is obtained by multiplying $$v(\x)$$ by $$a_m\x^{m-n}$$ to match the leading term with that of $$b_n u$$, obtaining

$$b_nu(\x)=a_m\x^{m-n}v(\x)+u_1(\x)$$

and then multiplying both sides by $$b_n^{k-1}$$. Now by the inductive hypothesis, there exist suitable polynomials $$q_1,r\in A[\x]$$ such that the formula

$$b_n^{k-1}u_1(\x)=q_1(\x)v(\x)+r(\x),\qquad \deg(r) < n$$

holds. Substituting this back into the previous formula, we obtain

$$b_n^k u(\x)=(b_n^{k-1}a_m\x^{m-n}+q_1(\x))v(\x)+r(\x)$$

</details>

The coefficient $$b_n^k$$ appearing here arises when we raise the degree one by one from $$v$$ to match the leading term with $$u$$, and if $$b_n$$ is invertible, we can verify that the $$q$$ and $$r$$ satisfying the above formula are uniquely determined. In particular, if every nonzero element of $$A$$ is invertible, that is, if $$A=\mathbb{K}$$, then in the above situation we can uniquely determine $$q,r$$ satisfying

$$u=qv+r,\qquad \deg r < n$$

Moreover, in this case the polynomial ring $$\mathbb{K}[\x]$$ is an integral domain by [Lemma 3](#lem3), and thus defining $$N:\mathbb{K}[\x] \rightarrow \mathbb{Z}^{\geq0}$$ by

$$N: u\mapsto \deg(u)\qquad \text{where $N(0)=0$}$$

we see that $$\mathbb{K}[\x]$$ is a Euclidean domain.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any field $$\mathbb{K}$$, $$\mathbb{K}[\x]$$ is a Euclidean domain.

</div>

In particular, the notion of greatest common divisor is well-defined over a Euclidean domain, and related to this, Bézout's lemma also holds. ([§Integral Domains, ⁋Theorem 7](/en/math/ring_theory/integral_domains#thm7))

We have previously seen that the images of arbitrary (nonzero) elements of $$\mathbb{K}$$ in $$\mathbb{K}[\x]$$ are units of $$\mathbb{K}[\x]$$. ([Lemma 3](#lem3)) On the other hand, in a Euclidean domain whether one element divides another can be determined by running the Euclidean algorithm, so an arbitrary non-constant $$u\in \mathbb{K}[\x]$$ being irreducible is equivalent to $$u$$ not being divisible by any $$v\in \mathbb{K}[\x]$$ satisfying $$\deg(v)<\deg(u)$$.

On the other hand, $$\mathbb{K}[\x]$$ is a UFD, and thus we can define irreducible elements of $$\mathbb{K}[\x]$$. Since the units of $$\mathbb{K}[\x]$$ are exactly the units of $$\mathbb{K}$$, any irreducible polynomial $$u$$ satisfies $$\deg(u)\geq 1$$ by definition, and since $$u$$ is irreducible, if $$v\mid u$$ then $$v$$ is either a constant polynomial or a constant multiple of $$u$$. In particular, any two irreducible polynomials must be constant multiples of each other, so two distinct *monic* irreducible polynomials are coprime. In this way, any polynomial in $$A[\x]$$ can be uniquely expressed as a product of its leading coefficient and monic irreducible polynomials.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For any polynomial $$u\in A[\x]$$ and any $$a\in A$$, the remainder when $$u(\x)$$ is divided by $$\x-a$$ is $$u(a)$$. Therefore, $$u$$ having $$a$$ as a root is equivalent to $$\x-a$$ being a divisor of $$u$$ in $$A[\x]$$.

</div>

The proof of this is of course to run the Euclidean algorithm, and this is in fact a familiar result from middle school. As another result, if $$u$$ has $$a$$ as a root, then $$u$$ must necessarily be written in the form

$$u(\x)=(\x-a)^p v(\x),\qquad v(a)\neq 0$$

In this case, we call $$p$$ the *multiplicity* of the root $$a$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Suppose any two polynomials $$u,v\in A[\x]$$ have a common root $$a$$, and let the multiplicity of $$a$$ in $$u$$ and $$v$$ be $$p,q$$ respectively. Then the following hold.

1. The multiplicity of $$a$$ in the polynomial $$u+v$$ is at least $$\inf(p,q)$$, and equality holds when $$p\neq q$$.
2. The multiplicity of $$a$$ in the polynomial $$uv$$ is at least $$p+q$$, and equality holds when $$A$$ is an integral domain.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose $$u(\x) = (\x-a)^p u_1(\x)$$, $$v(\x) = (\x-a)^q v_1(\x)$$ with $$u_1(a) \neq 0$$, $$v_1(a) \neq 0$$. Without loss of generality, assume $$p \leq q$$; then we obtain the formula

$$u(\x) + v(\x) = (\x-a)^p (u_1(\x) + (\x-a)^{q-p}v_1(\x))$$

and thus obtain the desired inequality. If here $$p < q$$, then $$a$$ is not a root of $$u_1(\x) + (\x-a)^{q-p}v_1(\x)$$, so we obtain the desired result.

For the second result, under the same assumption,

$$u(\x)v(\x) = (\x-a)^{p+q}u_1(\x)v_1(\x)$$

If $$A$$ is an integral domain, then $$u_1(a)v_1(a) \neq 0$$, from which we obtain the second result.

</details>

Furthermore, if $$A$$ is an integral domain, we can show the following inductively.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Fix an integral domain $$A$$. Let a nonzero element $$u$$ of $$A[\x]$$ have roots $$a_1,\ldots, a_r$$, and let their multiplicities be $$p_1,\ldots, p_r$$ respectively. Then there exists $$v\in A[\x]$$ such that

$$u(\x)=(\x-a_1)^{p_1}\cdots(\x-a_r)^{p_r}v(\x),\qquad v(a_1),\ldots, v(a_r)\neq0$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed by induction on $$r$$. The case $$p=1$$ is trivial, so suppose $$r$$ roots $$a_1,\ldots, a_r$$ of $$u$$ are given, and apply the inductive hypothesis to the first $$r-1$$ roots to write

$$u(\x)=u_1(\x)u_2(\x)=(\x-a_1)^{p_1}\cdots(\x-a_{r-1})^{p_{r-1}}u_2(\x)$$

Then since $$A$$ is an integral domain, we know $$u_1(a_r)\neq 0$$, so necessarily $$u_2(a_r)=0$$ and the multiplicity of $$a_r$$ in $$u_2$$ must be $$p_r$$. From this we obtain the desired claim.

</details>

In particular, for any integral domain $$A$$, any polynomial of degree $$n$$ in $$A[\x]$$ has at most $$n$$ roots (counted with multiplicity). Therefore, if two polynomials $$f,g\in A[\x]$$ of degree at most $$n$$ are given, and if $$f(a_i)=g(a_i)$$ holds for $$n+1$$ distinct elements $$a_1,\ldots, a_{n+1}$$, then necessarily $$f=g$$. From this we obtain the following result.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Fix $$n$$ distinct elements $$a_1,\ldots, a_n$$ of a field $$\mathbb{K}$$. For arbitrary elements $$b_1,\ldots, b_n$$ of $$\mathbb{K}$$, define for each $$i$$

$$u_i(\x)=\prod_{j\neq i}\frac{\x-a_j}{a_i-a_j}$$

Then

$$u=b_1 u_1 + \cdots + b_n u_n$$

is the unique polynomial of degree less than $$n$$ satisfying $$u(a_i)=b_i$$ for each $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Uniqueness is trivial by the above argument, and it remains only to verify that substituting each $$a_i$$ into $$u$$ yields the value $$b_i$$.

</details>

On the other hand, one useful method for finding multiple roots is to differentiate the given polynomial. We can define algebraically what differentiation is ([\[Multilinear Algebra\] §Derivations](/en/math/multilinear_algebra/derivations)), but in this post we define $$D: A[\x] \rightarrow A[\x]$$ by the formula

$$D:\left(u(\x)=\sum_{i=0}^n a_i\x^i\right)\mapsto \left((Du)(\x)=i.a_i\x^{i-1}\right)\tag{$\ast$}$$

Here, $$i.a_i$$ is the element of $$A$$ defined by

$$i.a_i=\underbrace{a_i+\cdots+a_i}_\text{\scriptsize$i$ times}$$

The only property we will use in the remaining discussion is the Leibniz rule

$$D(uv)=(Du)v+u(Dv)$$

which in [\[Multilinear Algebra\] §Derivations](/en/math/multilinear_algebra/derivations) is the definition of a derivation, but if we accept the formula ($$\ast$$) as a definition, it can be verified by direct computation.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For any polynomial $$u \in A[\x]$$, a necessary and sufficient condition for a root $$a \in A$$ of $$u$$ to be a simple root is that $$a$$ is not a root of $$Du$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By the assumption that $$a$$ is a root of $$u$$, there exists $$v \in A[\x]$$ such that $$u = (\x - a)v$$, and in this case the necessary and sufficient condition for $$a$$ to be a simple root of $$u$$ is $$v(a) \neq 0$$. Now since $$Du = v + (\x - a)Dv$$, we have $$(Du)(a) = v(a)$$.

</details>

More generally, using induction we can show the following.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For any polynomial $$u \in A[\x]$$, if a root $$a \in A$$ of $$u$$ has multiplicity $$k$$, then $$a$$ is a root of $$Du$$ of multiplicity $$\geq k-1$$. If $$k \cdot 1$$ is cancellable in $$A$$, then $$a$$ has order $$k-1$$ in $$Du$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Similarly to the above proposition, set $$u=(\x-a)^k v$$ with $$v(a)\neq 0$$; then

$$Du=k(\x-a)^{k-1}v+(\x-a)^k Dv=(\x - a)^{k-1}(kv + (\x - a)Dv)$$

from which we obtain the first claim. If $$k\cdot 1$$ is cancellable in $$A$$, then substituting $$\x=a$$ into $$kv+(\x-a)Dv$$ gives $$k.v(a)$$, which is not $$0$$, so the latter claim holds.

</details>

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> Let an integral domain $$A$$ and a set $$I$$ be given, and let $$(H_i)_{i\in I}$$ be a family of infinite subsets of $$A$$ indexed by $$I$$. Also, let $$H=\prod_{i\in I} H_i\subseteq A^I$$. Then if $$u$$ is a nonzero element of $$A[\x_i]_{i\in I}$$, the set

$$H_u=\{(\x_i)\in H\mid u(\x_i)\neq 0\}$$

has the same cardinality as $$H$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The case where $$I$$ is a finite set can be shown by induction. Let $$\lvert I\rvert=n$$, and prove by induction on $$n$$. First, the case $$n=0$$ is trivial. To simplify notation for the induction, let $$I=\{1,\ldots, n\}$$, $$J=\{1,\ldots, n-1\}$$, and $$B=A[\x_i]_{i\in J}$$. Then since $$u\neq 0$$, there exist $$v_k\in B$$ such that

$$u=\sum_{k=0}^m v_k\x_n^k$$

Here, $$v_m\neq 0$$. Now by the inductive hypothesis, the set

$$H_{v_m}=\{(\x_i)\in H\mid v_m(\x_i)\neq 0\}$$

has the same cardinality as $$\prod_{i\in J} H_i$$. Now for any element $$(x_i)_{i\in J}$$ of $$\prod_{i\in J} H_i$$,

$$w(\x)=\sum_{k=0}^mv_k(x_1,\ldots, x_{n-1})\x_n^k$$

is a nonzero polynomial. On the other hand, the set

$$\{a\in H_n\mid w(a)\neq 0\}$$

has, by the fact that $$H_n$$ is infinite and the argument after [Proposition 9](#prop9), and by [\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Proposition 13](/en/math/set_theory/natural_numbers#prop13),

$$\lvert H\rvert\geq \lvert H_u\rvert\geq \lvert H_{v_m}\rvert\lvert H_n\rvert=\lvert H\rvert$$

The case where $$I$$ is an infinite set can be reduced to the finite case by considering the polynomial ring containing only the indeterminates appearing in $$u$$.

</details>

In particular, if $$I$$ is nonempty, then $$H_u$$ is an infinite set.

## Factorization

If an arbitrary ring homomorphism $$\phi:A \rightarrow B$$ is given, any $$u\in A[\x_i]_{i\in I}$$ can be viewed as an element of $$B[\x_i]_{i\in I}$$ via $$\phi$$.

In particular, consider the case where $$A$$ is an integral domain and $$\phi$$ is the canonical inclusion $$A \hookrightarrow \Frac(A)$$. Then since $$\Frac(A)$$ is a field, $$(\Frac A)[\x]$$ is a Euclidean domain by [Proposition 6](#prop6), and thus if we view any $$u\in A[\x]$$ in $$(\Frac A)[\x]$$, then $$u$$ can be factored at least in $$(\Frac A)[\x]$$. It is then natural to examine how this factorization is reflected in $$A[\x]$$.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14 (Gauss)**</ins> Consider a UFD $$A$$, its field of fractions $$\Frac(A)$$, and an element $$u$$ of $$A[\x]$$. If $$u$$ is reducible in $$(\Frac A)[\x]$$, then $$u$$ is also reducible in $$A[\x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose a polynomial $$u$$ in $$(\Frac A)[\x]$$ is expressed as a product of two polynomials

$$u(\x)=\tilde{v}_1(\x)\tilde{v}_2(\x),\qquad \tilde{v}_i\in (\Frac A)[\x]$$

Then multiplying both sides by the least common multiple of the coefficients of $$\tilde{v}_1$$ and $$\tilde{v}_2$$, there exist $$v_i\in A[\x]$$ such that for some appropriate $$a\in A$$,

$$a u(\x)=v_1(\x)v_2(\x)$$

If $$a$$ is a unit, there is nothing more to prove, so assume $$a$$ is not a unit. Then there exist irreducible elements $$p_i\in A$$ such that $$a=p_1\cdots p_r$$. In this case, by [§Integral Domains, ⁋Proposition 17](/en/math/ring_theory/integral_domains#prop17), $$(p_i)$$ is a prime ideal of $$A$$, and thus

$$(A/p_iA)[\x]\cong A[\x]/P_i$$

is an integral domain by [Proposition 4](#prop4). Therefore, reducing the equation $$au=v_1v_2$$ modulo $$P_i$$, we see that either $$v_1$$ or $$v_2$$ must become $$0$$ in $$(A/p_iA)[x]$$. That is, the coefficients of one of $$v_1$$ or $$v_2$$ are all multiples of $$p_i$$, and thus we can cancel this $$p_i$$ to obtain another polynomial in $$A[\x]$$. Applying this to all $$p_i$$ gives the desired result.

</details>

From this we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor15">**Corollary 15**</ins> Consider a UFD $$A$$ and its field of fractions $$\Frac A$$, and a polynomial $$u(\x) \in A[\x]$$, and let the greatest common divisor of the coefficients of $$u(\x)$$ be $$1$$. Then $$u(\x)$$ being irreducible in $$A[\x]$$ is equivalent to $$u(\x)$$ being irreducible in $$(\Frac A)[\x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 14](#prop14), if $$u(\x)$$ is reducible in $$(\Frac A)[\x]$$, then it is also reducible in $$A[\x]$$.

Conversely, suppose the greatest common divisor of the coefficients of $$u(\x)$$ is $$1$$, and assume $$u(\x)$$ is reducible in $$A[\x]$$. That is, we can write

$$u(\x) = v_1(\x) v_2(\x)$$

and since the greatest common divisor of the coefficients of $$v_1(\x)$$ and $$v_2(\x)$$ must also be $$1$$, in particular neither $$v_1$$ nor $$v_2$$ is constant. From this, $$u=v_1v_2$$ means that $$u$$ is also reducible when viewed in $$(\Frac A)[\x]$$.

</details>

Then one of the key results related to factorization is the following theorem.

<div class="proposition" markdown="1">

<ins id="thm16">**Theorem 16**</ins> A necessary and sufficient condition for $$A$$ to be a UFD is that $$A[\x]$$ is a UFD.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$A[\x]$$ being a UFD implies $$A$$ is also a UFD is trivial, so it suffices to show the converse.

For a UFD $$A$$, let a nonzero element of $$A[\x]$$ be $$u(\x)$$, and if the greatest common divisor of the coefficients of $$u(\x)$$ is $$d$$, then we can write $$u(\x)=du_0(\x)$$ to obtain a polynomial $$u_0\in A[\x]$$ whose coefficients have greatest common divisor $$1$$; thus we may assume without loss of generality that the greatest common divisor of the coefficients of $$u$$ is $$1$$.

By [Proposition 6](#prop6), $$u$$ can be uniquely factored in $$(\Frac A)[\x]$$, and applying [Proposition 14](#prop14) to this factorization, we can factor $$u$$ in $$A[\x]$$. On the other hand, since the greatest common divisor of the coefficients of $$u$$ is $$1$$, the greatest common divisor of the coefficients of the factors of $$u$$ thus obtained is also $$1$$, and therefore by [Corollary 15](#cor15) they are irreducible in $$A[\x]$$. From this we obtain a factorization of $$u$$ in $$A[\x]$$, and uniqueness is trivial using the fact that each of these components is a $$\Frac A$$-multiple of the corresponding factor in $$(\Frac A)[\x]$$.

</details>

## Field of Rational Functions

We now define rational function fields and power series rings, which are variants of polynomial rings. Earlier in [Proposition 4](#prop4), we proved that for any field $$\mathbb{K}$$, $$\mathbb{K}[\x_i]_{i\in I}$$ is an integral domain. Therefore, the field of fractions of $$\mathbb{K}[\x_i]_{i\in I}$$ is well-defined.

<div class="definition" markdown="1">

<ins id="def17">**Definition 17**</ins> We call the field of fractions of the polynomial ring $$\mathbb{K}[\x_i]_{i\in I}$$ defined over a field $$\mathbb{K}$$ the *field of rational functions*, and denote it by $$\mathbb{K}(\x_i)_{i\in I}$$.

</div>

Earlier, we saw that a polynomial ring can be viewed as an $$\mathbb{N}$$-graded ring using multidegree. In a similar way, let us define a degree on $$\mathbb{K}(\x_i)_{i\in I}$$ as well. The natural choice is to define for any element $$u/v$$ of $$\mathbb{K}(\x_i)_{i\in I}$$

$$\deg(u/v)=\deg(u)-\deg(v)$$

and we can verify that this is well-defined. As with polynomials, we define $$\deg(0)=-\infty$$.

Then the following proposition is the analogue of [Proposition 2](#prop2).

<div class="proposition" markdown="1">

<ins id="prop18">**Proposition 18**</ins> For two rational fractions $$r, s$$, the following hold.

1. If $$\deg r \ne \deg s$$, then

    $$r + s \ne 0 \quad \text{and} \quad \deg(r + s) = \sup(\deg r, \deg s)$$

    holds. If $$\deg r = \deg s$$, then $$\deg(r + s) \leq \deg r$$.
2. $$\deg(rs) = \deg r + \deg s$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

For both claims, it suffices to consider only the case where $$r, s \ne 0$$. Therefore, let $$r =u/v$$, $$s = w/z$$ with $$u, v, w, z$$ all nonzero polynomials. In any case, the idea is to first compute the given expression and then apply [Proposition 2](#prop2) and [Lemma 3](#lem3).

1. $$r + s = (uz+vw)/(vz)$$. First, suppose $$\deg r \ne \deg s$$, that is, $$\deg u + \deg z \ne \deg w + \deg v$$. Then $$uz + vw \ne 0$$, and

    $$\begin{aligned}\deg(r + s) &= \deg(uz + vw) - \deg(vz) \\
    &= \sup(\deg(uz), \deg(vw)) - \deg(vz) \\
    &= \sup(\deg(uz) - \deg(vz), \deg(vw) - \deg(vz)) \\
    &= \sup(\deg r, \deg s).\end{aligned}$$

    Now suppose $$\deg r = \deg s$$, that is, $$\deg u + \deg z = \deg w + \deg v$$, and if $$r + s \ne 0$$, then

    $$\deg(r + s) = \deg(uz + vw) - \deg(vz)\leq \deg(uz) - \deg(vz) = \deg r$$

    so the claim holds.

2. $$rs = (uw)/(vz)$$, and therefore

    $$\deg(rs) = \deg(uw) - \deg(vz) = \deg u - \deg v + \deg w - \deg z = \deg r + \deg s.$$

</details>

## Power Series Ring

A power series ring is another variant of a polynomial ring, and is now the set of infinite sums of monomials

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu$ need not satisfy finiteness condition}$$

We write this as $$A[[\x_i]]_{i\in I}$$ and call it the *ring of formal power series*.

Formal power series can be defined with concepts similar to polynomials, except for the fact that they are *infinite* sums of monomials. For example, we can define the degree $$p$$ component $$u_p$$ of a formal power series $$u$$. However, for the (total) degree of $$u$$, since the degree of elements other than polynomials would be $$+\infty$$, there is no reason to use this in $$A[[\x_i]]_{i\in I}$$. Instead, for any formal power series $$u$$, we define the *order* $$\omega(u)$$ of $$u$$ as the *smallest* $$p$$ such that $$u_p\neq 0$$. Similarly, setting $$\omega(0)=\infty$$, the formulas

$$\omega(u+v)\geq \inf(\omega(u),\omega(v)),\quad\text{equality if $\omega(u)\neq\omega(v)$}$$

and

$$\omega(uv)\geq \omega(u)+\omega(v)$$

hold.

For degree, the above inequality would have held if $$A$$ were an integral domain. Similarly, the following holds.

<div class="proposition" markdown="1">

<ins id="prop19">**Proposition 19**</ins> For an integral domain $$A$$, the following hold.

1. $$A[[x_i]]_{i\in I}$$ is an integral domain.
2. For two nonzero elements $$u,v\in A[[x_i]]_{i\in I}$$, we have $$\omega(uv)=\omega(u)+\omega(v)$$.

</div>

However, one must be somewhat careful: unlike [Proposition 4](#prop4), the units of $$A[[x_i]]_{i\in I}$$ are larger than those of $$A$$. For example, consider the formula

$$(1-\x)\left( \sum_{n=0}^\infty \x^n\right)=1$$

More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop20">**Proposition 20**</ins> For any $$u\in A[[x_i]]_{i\in I}$$, $$u$$ being invertible in $$A[[x_i]]_{i\in I}$$ is equivalent to the constant term of $$u$$ being invertible in $$A$$.

</div>
