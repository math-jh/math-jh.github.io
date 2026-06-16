---
title: "Polynomial Rings"
description: "We define the polynomial ring over a commutative ring and examine the degree of a polynomial and homogeneous polynomials. We also cover the representation of polynomials via monomials, properties of degree, the leading term, and monic polynomials."
excerpt: "Factorization of polynomial rings over commutative rings and Gauss's lemma"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/polynomial_rings
sidebar: 
    nav: "ring_theory-en"

date: 2025-05-06
weight: 3
translated_at: 2026-06-01T23:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T23:30:01+00:00
---
<div class="remark" markdown="1">

<ins id="rmk">**Remark**</ins> In this post, $$A$$ is always a commutative ring.

</div>

In [\[Algebraic Structures\] §Algebras, ⁋Definition 7](/en/math/algebraic_structures/algebras#def7), we defined the polynomial algebra $$A[\x_i]_{i\in I}$$ for an arbitrary (commutative) ring $$A$$. It carries an $$A$$-algebra structure, but the scalar multiplication of $$A$$ on $$A[\x_i]_{i\in I}$$ arises from the inclusion $$A\hookrightarrow A[\x_i]_{i\in I}$$ when we view $$A[\x_i]_{i\in I}$$ as a ring; thus, to study the properties of $$A[\x_i]_{i\in I}$$, it suffices to regard it simply as a ring.

## Degree of Polynomials

Before dealing with polynomials in earnest, let us first define the tools for handling them. By a *polynomial* defined over $$A$$, we mean an element of the polynomial ring $$P=A[\x_i]_{i\in I}$$. Let $$\mathbb{N}^{(I)}$$ denote the set of finitely supported functions from $$I$$ to $$\mathbb{N}$$:

$$\mathbb{N}^{(I)}=\{\nu:I \rightarrow \mathbb{N}\mid\text{$f(i)=0$ for all but finitely many $i\in I$}\}$$

Then for any $$\nu\in \mathbb{N}^{(I)}$$, setting

$$\x^\nu=\prod_{i\in I} \x_i^{\nu_i}$$

makes $$\x^\nu$$ an element of $$P$$. We call elements of the form

$$a\x^\nu$$

*monomials*. Any polynomial $$u$$ can then be expressed as a finite sum of monomials

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu=0$ for all but finitely many $\nu$}$$

On the other hand, for any $$\nu\in \mathbb{N}^{(I)}$$, defining

$$\lvert\nu\rvert=\sum_{i\in I} \nu_i$$

allows us to regard $$P=A[\x_i]_{i\in I}$$ as an $$\mathbb{N}$$-graded ring

$$P=\bigoplus_{n\in \mathbb{N}}\bigoplus_{\lvert\nu\rvert=n}(A[\x_i]_{i\in I})_\nu=\bigoplus_{n\in \mathbb{N}} P_n$$

For each $$n$$, the elements of $$P_n$$ are called *homogeneous polynomials* of degree $$n$$. For any polynomial $$u\in P$$, the component of $$u$$ of degree $$n$$ in this homogeneous decomposition is sometimes written as $$u_n$$.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Let an arbitrary element of the polynomial ring $$P=A[\x]_{i\in I}$$

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu=0$ for all but finitely many $\nu$}$$

be given. Then the largest $$n$$ satisfying $$u_n\neq 0$$ is called the *degree* of $$u$$, denoted by $$\deg(u)$$. By definition, the degree of a polynomial having only a constant term is $$0$$, but for the additive identity $$0$$ of $$P$$, we specially define $$\deg(0)=-\infty$$.

</div>

Then the following proposition holds obviously.

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2**</ins> For two polynomials $$u,v$$, the following hold.

1. If $$\deg (u)\neq\deg(v)$$, then $$u+v\neq 0$$ and the equality
     
    $$\deg(u+v)=\sup(\deg(u), \deg(v))$$

    holds. If $$\deg(u)=\deg(v)$$, then the inequality $$\deg(u+v)\leq\deg(u)$$ holds.
2. The inequality $$\deg(uv)\leq\deg(u)+\deg(v)$$ holds.

</div>

The reason why the second condition of this proposition is not an equality lies in $$A$$. To examine this in more detail, consider the polynomial ring $$A[\x]$$ in one variable. Then any polynomial in $$A[\x]$$ can be written in the form

$$u(\x)=\sum_{i=0}^n a_i\x^i\qquad\text{($a_n\neq 0$)}$$

and here $$a_n\x^n$$ is called the *leading term* of the polynomial $$p$$, and its coefficient $$a_n$$ is called the *leading coefficient* of $$p$$. If the leading coefficient of $$p$$ is $$1$$, then $$p$$ is called a *monic polynomial*.

Now for any two (univariate) polynomials

$$u(\x)=\sum_{i=0}^n a_i\x^i,\qquad v(\x)=\sum_{j=0}^m b_j \x^j$$

their product is given explicitly by the formula

$$u(\x)v(\x)=\sum_{k=0}^{n+m}\left(\sum_{i=0}^k a_ib_{k-i}\right)\x^k$$

and thus the coefficient of the highest-degree term is $$a_nb_m$$. However, if $$A$$ is not an integral domain, the product of two nonzero elements $$a_n$$ and $$b_m$$ can be $$0$$, so $$uv$$ may fail to be a polynomial of degree $$m+n$$. Using this argument, we obtain the following.

<div class="proposition" markdown="1">

<ins id="lem3">**Lemma 3**</ins> For an integral domain $$A$$, the following hold.

1. For any $$u,v\in A[\x]$$, we have $$\deg(uv)=\deg(u)+\deg(v)$$.
2. The units of $$A[\x]$$ are exactly the units of $$A$$.
3. $$A[\x]$$ is an integral domain.

</div>

Now let us return to the general case. Given any two polynomials $$u,v\in A[\x_i]_{i\in I}$$, only finitely many indeterminates appear in them, so when computing $$uv$$, it suffices to choose a finite subset $$J\subset I$$ and work in $$A[\x_j]_{j\in J}$$ instead of $$A[\x_i]_{i\in I}$$. Then the fact that $$A[\x_j]_{j\in J}$$ is an integral domain follows from [Lemma 3](#lem3) and the isomorphism

$$A[\x_1,\x_2]\cong (A[\x_1])[\x_2]$$

That is, the following holds.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4**</ins> For an integral domain $$A$$ and the polynomial ring $$P=A[\x_i]_{i\in I}$$, the following hold.

1. For any $$u,v\in P$$, we have $$\deg(uv)=\deg(u)+\deg(v)$$.
2. The units of $$P$$ are exactly the units of $$A$$.
3. $$P$$ is an integral domain.

</div>

## Univariate Polynomials

We now examine univariate polynomials in a bit more detail.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$u(\x)$$ be a polynomial of degree $$m$$ and $$v(\x)$$ a polynomial of degree $$n$$ in $$A[\x]$$, and let $$b_n$$ be the leading coefficient of $$v$$. If we set $$k=\sup(m-n+1,0)$$, then there exist $$q,r\in A[\x]$$ satisfying the equation

$$b_n^k u=qv+r,\qquad \deg r < n$$

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$n>m$$, then $$k=0$$, and in this case the given equation holds with $$q=0$$ and $$r=u$$, so there is nothing to prove. Thus assume $$n\leq m$$.

We use induction on $$m$$. Let $$a_m$$ be the leading coefficient of $$u$$. If

$$v(\x)=\sum_{j=0}^n b_j\x^j$$

then there exists a polynomial $$u_1\in A[\x]$$ of degree less than $$m$$ such that we can write

$$b_n^k u(\x)=b_n^{k-1}a_m\x^{m-n}v(\x)+b_n^{k-1}u_1(\x)$$

This equation is nothing but multiplying $$v(\x)$$ by $$a_m\x^{m-n}$$ to match the leading term with that of $$b_n u$$, obtaining

$$b_nu(\x)=a_m\x^{m-n}v(\x)+u_1(\x)$$

and then multiplying both sides by $$b_n^{k-1}$$. Now by the induction hypothesis, there exist suitable polynomials $$q_1,r\in A[\x]$$ such that the following equation

$$b_n^{k-1}u_1(\x)=q_1(\x)v(\x)+r(\x),\qquad \deg(r) < n$$

holds. Substituting this back into the previous equation, we obtain

$$b_n^k u(\x)=(b_n^{k-1}a_m\x^{m-n}+q_1(\x))v(\x)+r(\x)$$

</details>

The coefficient $$b_n^k$$ appearing here arises when we match the leading terms of $$u$$ by raising the degree step by step from $$v$$, and for instance, if $$b_n$$ is invertible, one can verify that the $$q$$ and $$r$$ satisfying the above equation are uniquely determined. In particular, if every nonzero element of $$A$$ is invertible, that is, if $$A=\mathbb{K}$$, then in the above situation we can uniquely determine $$q,r$$ satisfying

$$u=qv+r,\qquad \deg r < n$$

Moreover, in this case the polynomial ring $$\mathbb{K}[\x]$$ is an integral domain by [Lemma 3](#lem3), and therefore if we define $$N:\mathbb{K}[\x] \rightarrow \mathbb{Z}^{\geq0}$$ by

$$N: u\mapsto \deg(u)\qquad \text{with $N(0)=0$}$$

then we see that $$\mathbb{K}[\x]$$ is a Euclidean domain.

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> For any field $$\mathbb{K}$$, $$\mathbb{K}[\x]$$ is a Euclidean domain.

</div>

In particular, the notion of greatest common divisor is well defined over a Euclidean domain, and related to this, Bézout's lemma also holds. ([§Integral Domains, ⁋Theorem 7](/en/math/ring_theory/integral_domains#thm7))

Earlier we observed that the images of arbitrary (nonzero) elements of $$\mathbb{K}$$ in $$\mathbb{K}[\x]$$ are units of $$\mathbb{K}[\x]$$. ([Lemma 3](#lem3)) On the other hand, in a Euclidean domain whether one element divides another can be determined by running the Euclidean algorithm, so for any nonconstant $$u\in \mathbb{K}[\x]$$, being irreducible is equivalent to not being divisible by any $$v\in \mathbb{K}[\x]$$ with $$\deg(v)<\deg(u)$$.

Moreover, $$\mathbb{K}[\x]$$ is a UFD, so irreducible elements in $$\mathbb{K}[\x]$$ can be defined. Since the units of $$\mathbb{K}[\x]$$ are exactly the units of $$\mathbb{K}$$, any irreducible polynomial $$u$$ satisfies $$\deg(u)\geq 1$$ by definition, and because $$u$$ is irreducible, if $$v\mid u$$ then $$v$$ is either a constant polynomial or a constant multiple of $$u$$. In particular, any two irreducible polynomials must be constant multiples of each other, so two distinct *monic* irreducible polynomials are coprime. In this way, any polynomial in $$A[\x]$$ can be uniquely expressed as a product of its leading coefficient and monic irreducible polynomials.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7**</ins> For any polynomial $$u\in A[\x]$$ and any $$a\in A$$, the remainder upon dividing $$u(\x)$$ by $$\x-a$$ is $$u(a)$$. Therefore, $$u$$ having $$a$$ as a root is equivalent to $$\x-a$$ being a divisor of $$u$$ in $$A[\x]$$.

</div>

The proof of this is of course to run the Euclidean algorithm, and this is in fact a familiar result from middle school. As another result, if $$u$$ has a root $$a$$, then $$u$$ must necessarily be written in the form

$$u(\x)=(\x-a)^p v(\x),\qquad v(a)\neq 0$$

In this case, we call $$p$$ the *multiplicity* of the root $$a$$. Then the following holds.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8**</ins> Let $$u,v\in A[\x]$$ be two arbitrary polynomials having a common root $$a$$, and let $$p,q$$ be the multiplicities of $$a$$ in $$u$$ and $$v$$, respectively. Then the following hold.

1. The multiplicity of $$a$$ in the polynomial $$u+v$$ is at least $$\inf(p,q)$$, and equality holds when $$p\neq q$$.
2. The multiplicity of $$a$$ in the polynomial $$uv$$ is at least $$p+q$$, and equality holds when $$A$$ is an integral domain.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Let $$u(\x) = (\x-a)^p u_1(\x)$$ and $$v(\x) = (\x-a)^q v_1(\x)$$ with $$u_1(a) \neq 0$$ and $$v_1(a) \neq 0$$. Without loss of generality assume $$p \leq q$$. Then we obtain the expression

$$u(\x) + v(\x) = (\x-a)^p (u_1(\x) + (\x-a)^{q-p}v_1(\x))$$

and thus obtain the desired inequality. If here $$p < q$$, then $$a$$ is not a root of $$u_1(\x) + (\x-a)^{q-p}v_1(\x)$$, so we obtain the desired result.

For the second result, under the same assumption we have

$$u(\x)v(\x) = (\x-a)^{p+q}u_1(\x)v_1(\x)$$

If $$A$$ is an integral domain, then $$u_1(a)v_1(a) \neq 0$$, from which we obtain the second result.

</details>

Furthermore, if $$A$$ is an integral domain, the following can be shown inductively.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9**</ins> Fix an integral domain $$A$$. Let $$u$$ be a nonzero element of $$A[\x]$$ having roots $$a_1,\ldots, a_r$$ with respective multiplicities $$p_1,\ldots, p_r$$. Then there exists $$v\in A[\x]$$ such that

$$u(\x)=(\x-a_1)^{p_1}\cdots(\x-a_r)^{p_r}v(\x),\qquad v(a_1),\ldots, v(a_r)\neq0$$

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

We proceed by induction on $$r$$. The case $$p=1$$ is obvious, so let $$a_1,\ldots, a_r$$ be the $$r$$ roots of $$u$$ and apply the induction hypothesis to the first $$r-1$$ roots to write

$$u(\x)=u_1(\x)u_2(\x)=(\x-a_1)^{p_1}\cdots(\x-a_{r-1})^{p_{r-1}}u_2(\x)$$

Then since $$A$$ is an integral domain, we know that $$u_1(a_r)\neq 0$$, so we must have $$u_2(a_r)=0$$ and the multiplicity of $$a_r$$ in $$u_2$$ must be $$p_r$$. From this we obtain the desired claim.

</details>

In particular, for any integral domain $$A$$, we know that any polynomial of degree $$n$$ in $$A[\x]$$ has at most $$n$$ roots (counted with multiplicity). Therefore, if two polynomials $$f,g\in A[\x]$$ of degree at most $$n$$ are given, and if $$f(a_i)=g(a_i)$$ holds for $$n+1$$ distinct elements $$a_1,\ldots, a_{n+1}$$, then we must have $$f=g$$. From this we obtain the following result.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Fix $$n$$ distinct elements $$a_1,\ldots, a_n$$ of a field $$\mathbb{K}$$. For arbitrary elements $$b_1,\ldots, b_n$$ of $$\mathbb{K}$$, define for each $$i$$

$$u_i(\x)=\prod_{j\neq i}\frac{\x-a_j}{a_i-a_j}$$

Then

$$u=b_1 u_1 + \cdots + b_n u_n$$

is the unique polynomial of degree less than $$n$$ satisfying $$u(a_i)=b_i$$ for each $$i$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Uniqueness is obvious from the above argument, and it remains only to verify that substituting each $$a_i$$ into $$u$$ yields the value $$b_i$$.

</details>

Meanwhile, one useful method for finding multiple roots is to differentiate the given polynomial. We can define algebraically what differentiation is ([\[Multilinear Algebra\] §Derivations](/en/math/multilinear_algebra/derivations)), but in this category we shall define $$D: A[\x] \rightarrow A[\x]$$ by the formula

$$D:\left(u(\x)=\sum_{i=0}^n a_i\x^i\right)\mapsto \left((Du)(\x)=i.a_i\x^{i-1}\right)\tag{$\ast$}$$

as a definition without such discussion. Here $$i.a_i$$ is the element of $$A$$ defined by

$$i.a_i=\underbrace{a_i+\cdots+a_i}_\text{\scriptsize$i$ times}$$

The only property we will use in the remaining discussion is the Leibniz rule

$$D(uv)=(Du)v+u(Dv)$$

which is the definition of a derivation in [\[Multilinear Algebra\] §Derivations](/en/math/multilinear_algebra/derivations), but if we accept the above formula ($$\ast$$) as a definition, it can be verified by direct computation.

<div class="proposition" markdown="1">

<ins id="prop11">**Proposition 11**</ins> For any polynomial $$u \in A[\x]$$, a necessary and sufficient condition for a root $$a \in A$$ of $$u$$ to be a simple root is that $$a$$ is not a root of $$Du$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By the assumption that $$a$$ is a root of $$u$$, there exists $$v \in A[\x]$$ such that $$u = (\x - a)v$$, and in this case the necessary and sufficient condition for $$a$$ to be a simple root of $$u$$ is that $$v(a) \neq 0$$. Now since $$Du = v + (\x - a)Dv$$, we have $$(Du)(a) = v(a)$$.

</details>

More generally, using induction we can show the following.

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> For any polynomial $$u \in A[\x]$$, if a root $$a \in A$$ of $$u$$ has multiplicity $$k$$, then $$a$$ is a root of $$Du$$ with multiplicity $$\geq k-1$$. If $$k \cdot 1$$ is cancellable in $$A$$, then $$a$$ has order $$k-1$$ in $$Du$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Similarly to the above proposition, set $$u=(\x-a)^k v$$ with $$v(a)\neq 0$$. Then

$$Du=k(\x-a)^{k-1}v+(\x-a)^k Dv=(\x - a)^{k-1}(kv + (\x - a)Dv)$$

yields the first claim. If $$k\cdot 1$$ is cancellable in $$A$$, then substituting $$\x=a$$ into $$kv+(\x-a)Dv$$ gives the value $$k.v(a)\neq 0$$, so the latter claim holds.

</details>

<div class="proposition" markdown="1">

<ins id="prop13">**Proposition 13**</ins> Let $$A$$ be an integral domain and $$I$$ a set, and let $$(H_i)_{i\in I}$$ be a family of infinite subsets of $$A$$ indexed by $$I$$. Also, let $$H=\prod_{i\in I} H_i\subseteq A^I$$. Then if $$u$$ is a nonzero element of $$A[\x_i]_{i\in I}$$, the set

$$H_u=\{(\x_i)\in H\mid u(\x_i)\neq 0\}$$

has the same cardinality as $$H$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

The case where $$I$$ is finite can be shown by induction. Let $$\lvert I\rvert=n$$, and we prove by induction on $$n$$. First, the case $$n=0$$ is trivial. To use induction, let us simplify notation by setting $$I=\{1,\ldots, n\}$$, $$J=\{1,\ldots, n-1\}$$, and $$B=A[\x_i]_{i\in J}$$. Then since $$u\neq 0$$, there exist $$v_k\in B$$ such that

$$u=\sum_{k=0}^m v_k\x_n^k$$

Here $$v_m\neq 0$$. Now by the induction hypothesis, the set

$$H_{v_m}=\{(\x_i)\in H\mid v_m(\x_i)\neq 0\}$$

has the same cardinality as $$\prod_{i\in J} H_i$$. Now for any element $$(x_i)_{i\in J}$$ of $$\prod_{i\in J} H_i$$,

$$w(\x)=\sum_{k=0}^mv_k(x_1,\ldots, x_{n-1})\x_n^k$$

is a nonzero polynomial. On the other hand, from the fact that $$H_n$$ is an infinite set, the argument after [Proposition 9](#prop9), and [\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Proposition 13](/en/math/set_theory/natural_numbers#prop13), the set

$$\{a\in H_n\mid w(a)\neq 0\}$$

satisfies

$$\lvert H\rvert\geq \lvert H_u\rvert\geq \lvert H_{v_m}\rvert\lvert H_n\rvert=\lvert H\rvert$$

If $$I$$ is infinite, we can reduce to the finite case by considering the polynomial ring containing only the indeterminates appearing in $$u$$.

</details>

In particular, if $$I$$ is not empty, then $$H_u$$ is an infinite set.

## Factorization

Given any ring homomorphism $$\phi:A \rightarrow B$$, any $$u\in A[\x_i]_{i\in I}$$ can be regarded as an element of $$B[\x_i]_{i\in I}$$ via $$\phi$$. Let us specially consider the case where $$A$$ is an integral domain and $$\phi$$ is the canonical inclusion $$A \hookrightarrow \Frac(A)$$. Then since $$\Frac(A)$$ is a field, $$(\Frac A)[\x]$$ is a Euclidean domain by [Proposition 6](#prop6), and therefore if we regard any $$u\in A[\x]$$ in $$(\Frac A)[\x]$$, then $$u$$ can be factored at least in $$(\Frac A)[\x]$$. Then it is natural to examine how this factorization performed here is reflected in $$A[\x]$$.

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14 (Gauss)**</ins> Let $$A$$ be a UFD with its field of fractions $$\Frac(A)$$, and let $$u$$ be an element of $$A[\x]$$. If $$u$$ is reducible in $$(\Frac A)[\x]$$, then $$u$$ is also reducible in $$A[\x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose the polynomial $$u$$ in $$(\Frac A)[\x]$$ is expressed as a product of two polynomials

$$u(\x)=\tilde{v}_1(\x)\tilde{v}_2(\x),\qquad \tilde{v}_i\in (\Frac A)[\x]$$

Then multiplying both sides by the least common multiples of the coefficients of $$\tilde{v}_1$$ and $$\tilde{v}_2$$, there exist $$v_i\in A[\x]$$ and a suitable $$a\in A$$ such that

$$a u(\x)=v_1(\x)v_2(\x)$$

If $$a$$ is a unit, there is nothing more to prove, so assume $$a$$ is not a unit. Then there exist irreducible elements $$p_i\in A$$ such that $$a=p_1\cdots p_r$$. At this time, by [§Integral Domains, ⁋Proposition 17](/en/math/ring_theory/integral_domains#prop17), $$(p_i)$$ is a prime ideal of $$A$$, and therefore

$$(A/p_iA)[\x]\cong A[\x]/P_i$$

is an integral domain by [Proposition 4](#prop4). Hence, reducing the equation $$au=v_1v_2$$ modulo $$P_i$$, we see that either $$v_1$$ or $$v_2$$ becomes $$0$$ in $$(A/p_iA)[x]$$. That is, the coefficients of one of $$v_1$$ or $$v_2$$ are all multiples of $$p_i$$, so we can cancel this $$p_i$$ to obtain another polynomial in $$A[\x]$$. Applying this to all $$p_i$$ gives the desired result.

</details>

From this we obtain the following.

<div class="proposition" markdown="1">

<ins id="cor15">**Corollary 15**</ins> Let $$A$$ be a UFD with its field of fractions $$\Frac A$$, and consider a polynomial $$u(\x) \in A[\x]$$ whose coefficients have greatest common divisor $$1$$. If $$u(\x)$$ is irreducible in $$A[\x]$$, then $$u(\x)$$ is also irreducible in $$(\Frac A)[\x]$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

By [Proposition 14](#prop14), if $$u(\x)$$ is reducible in $$(\Frac A)[\x]$$, then it is also reducible in $$A[\x]$$.

Conversely, suppose the coefficients of $$u(\x)$$ have greatest common divisor $$1$$, and assume $$u(\x)$$ is reducible in $$A[\x]$$. That is, we can write

$$u(\x) = v_1(\x) v_2(\x)$$

and here the coefficients of $$v_1(\x)$$ and $$v_2(\x)$$ must also have greatest common divisor $$1$$, so in particular neither $$v_1$$ nor $$v_2$$ is constant. Hence $$u=v_1v_2$$ means that $$u$$ is reducible even when viewed in $$(\Frac A)[\x]$$.

</details>

Then one of the key results concerning factorization is the following theorem.

<div class="proposition" markdown="1">

<ins id="thm16">**Theorem 16**</ins> A necessary and sufficient condition for $$A$$ to be a UFD is that $$A[\x]$$ is a UFD.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

That $$A[\x]$$ being a UFD implies $$A$$ is a UFD is obvious, so it suffices to show the converse.

For a UFD $$A$$, let $$u(\x)$$ be a nonzero element of $$A[\x]$$ and let $$d$$ be the greatest common divisor of the coefficients of $$u(\x)$$. Then we can write $$u(\x)=du_0(\x)$$ to obtain a polynomial $$u_0\in A[\x]$$ whose coefficients have greatest common divisor $$1$$, so without loss of generality we may assume that the coefficients of $$u$$ have greatest common divisor $$1$$.

By [Proposition 6](#prop6), $$u$$ can be factored uniquely in $$(\Frac A)[\x]$$, and applying [Proposition 14](#prop14) to this factorization, we can factor $$u$$ in $$A[\x]$$. On the other hand, since the coefficients of $$u$$ have greatest common divisor $$1$$, the coefficients of the factors of $$u$$ thus obtained also have greatest common divisor $$1$$, and hence by [Corollary 15](#cor15) they are irreducible in $$A[\x]$$. From this we obtain a factorization of $$u$$ in $$A[\x]$$, and uniqueness is obvious from the fact that each of these factors is a $$\Frac A$$-multiple of the corresponding factor in $$(\Frac A)[\x]$$.

</details>

## Fields of Rational Functions

We now define the variants of polynomial rings: fields of rational functions and formal power series rings. Earlier, in [Proposition 4](#prop4), we proved that for any field $$\mathbb{K}$$, $$\mathbb{K}[\x_i]_{i\in I}$$ is an integral domain. Therefore, the field of fractions of $$\mathbb{K}[\x_i]_{i\in I}$$ is well defined.

<div class="definition" markdown="1">

<ins id="def17">**Definition 17**</ins> The field of fractions of the polynomial ring $$\mathbb{K}[\x_i]_{i\in I}$$ defined over a field $$\mathbb{K}$$ is called the *field of rational functions* and denoted by $$\mathbb{K}(\x_i)_{i\in I}$$.

</div>

Earlier we saw that a polynomial ring can be regarded as an $$\mathbb{N}$$-graded ring using multidegree. In a similar way, let us define a degree on $$\mathbb{K}(\x_i)_{i\in I}$$. The natural choice is to define, for any element $$u/v$$ of $$\mathbb{K}(\x_i)_{i\in I}$$,

$$\deg(u/v)=\deg(u)-\deg(v)$$

and one can verify that this is well defined. As with polynomials, we define $$\deg(0)=-\infty$$. Then the following proposition is the analogue of [Proposition 2](#prop2).

<div class="proposition" markdown="1">

<ins id="prop18">**Proposition 18**</ins> For two rational fractions $$r, s$$, the following hold.

1. If $$\deg r \ne \deg s$$, then
    
    $$r + s \ne 0 \quad \text{and} \quad \deg(r + s) = \sup(\deg r, \deg s)$$
    
    hold. If $$\deg r = \deg s$$, then $$\deg(r + s) \leq \deg r$$.
2. $$\deg(rs) = \deg r + \deg s$$.

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to consider only the case where $$r, s \ne 0$$. Thus let $$r =u/v$$ and $$s = w/z$$ where $$u, v, w, z$$ are all nonzero polynomials. In any case, the idea is to first compute the given expression and then apply [Proposition 2](#prop2) and [Lemma 3](#lem3).

1. We have $$r + s = (uz+vw)/(vz)$$. First suppose $$\deg r \ne \deg s$$, that is, $$\deg u + \deg z \ne \deg w + \deg v$$. Then $$uz + vw \ne 0$$, and
    
    $$\begin{aligned}\deg(r + s) &= \deg(uz + vw) - \deg(vz) \\
    &= \sup(\deg(uz), \deg(vw)) - \deg(vz) \\
    &= \sup(\deg(uz) - \deg(vz), \deg(vw) - \deg(vz)) \\
    &= \sup(\deg r, \deg s).\end{aligned}$$
    
    On the other hand, now suppose $$\deg r = \deg s$$, that is, $$\deg u + \deg z = \deg w + \deg v$$, and if $$r + s \ne 0$$ then
    
    $$\deg(r + s) = \deg(uz + vw) - \deg(vz)\leq \deg(uz) - \deg(vz) = \deg r$$

    so the claim holds.
    
2. We have $$rs = (uw)/(vz)$$, and therefore

    $$\deg(rs) = \deg(uw) - \deg(vz) = \deg u - \deg v + \deg w - \deg z = \deg r + \deg s.$$
    

</details>

## Formal Power Series Rings

The ring of formal power series is another variant of the polynomial ring; it is the collection of infinite sums of monomials

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu$ need not satisfy finiteness condition}$$

This is denoted by $$A[[\x_i]]_{i\in I}$$ and called the *ring of formal power series*. For formal power series, similar concepts to those for polynomials can be defined, except for the fact that they are infinite sums of monomials. For example, we can define the degree $$p$$ component $$u_p$$ of a formal power series $$u$$. However, for the (total) degree of $$u$$, since the degree of elements that are not polynomials would be $$+\infty$$, there is no particular reason to use it in $$A[[\x_i]]_{i\in I}$$. Instead, for any formal power series $$u$$, we define the *order* $$\omega(u)$$ of $$u$$ as the smallest $$p$$ such that $$u_p\neq 0$$. Likewise, setting $$\omega(0)=\infty$$, the formula

$$\omega(u+v)\geq \inf(\omega(u),\omega(v)),\quad\text{equality if $\omega(u)\neq\omega(v)$}$$

and the formula

$$\omega(uv)\geq \omega(u)+\omega(v)$$

hold.

For degree, the above inequality would have held as an equality if $$A$$ were an integral domain. Similarly, the following holds.

<div class="proposition" markdown="1">

<ins id="prop19">**Proposition 19**</ins> For an integral domain $$A$$, the following hold.

1. $$A[[x_i]]_{i\in I}$$ is an integral domain.
2. For two nonzero elements $$u,v\in A[[x_i]]_{i\in I}$$, we have $$\omega(uv)=\omega(u)+\omega(v)$$.

</div>

However, one thing to be careful about is that, unlike [Proposition 4](#prop4), the units of $$A[[x_i]]_{i\in I}$$ are larger than those of $$A$$. For example, it suffices to consider the formula

$$(1-\x)\left( \sum_{n=0}^\infty \x^n\right)=1$$

More generally, the following holds.

<div class="proposition" markdown="1">

<ins id="prop20">**Proposition 20**</ins> For any $$u\in A[[x_i]]_{i\in I}$$, $$u$$ being invertible in $$A[[x_i]]_{i\in I}$$ is equivalent to the constant term of $$u$$ being invertible in $$A$$.

</div>
