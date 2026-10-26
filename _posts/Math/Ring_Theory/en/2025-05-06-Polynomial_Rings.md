---
title: "Polynomial Rings"
description: "We define polynomial rings over commutative rings and examine the degree of a polynomial and homogeneous polynomials. We cover the representation of polynomials via monomials, properties of degree, leading terms, and monic polynomials."
excerpt: "Factorization in polynomial rings over commutative rings and Gauss's lemma"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/polynomial_rings
sidebar: 
    nav: "ring_theory-en"

date: 2025-05-06
weight: 4
translated_at: 2026-06-26T23:00:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-26T07:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
::: remark Remark {#rmk}
In this post, $A$ is always a commutative ring.
:::

In [\[Algebraic Structures\] §Algebras, ⁋Definition 7](/en/math/algebraic_structures/algebras#def7){: data-lid="80gl1" }, we defined, for any (commutative) ring $A$, the polynomial algebra $A[\x_i]_{i\in I}$. This carries an $A$-algebra structure, but since the scalar multiplication defined on $A[\x_i]_{i\in I}$ by $A$ arises, when regarding $A[\x_i]_{i\in I}$ as a ring anyway, from the inclusion $A\hookrightarrow A[\x_i]_{i\in I}$, to examine the properties of $A[\x_i]_{i\in I}$, it is sufficient to consider $A[\x_i]_{i\in I}$ merely as a ring.

## Degree of Polynomials

Before treating polynomials in earnest, let us first define the tools needed to handle them. First, *polynomials* defined over $A$ mean elements of the polynomial ring $P=A[\x_i]_{i\in I}$. Here, let us define $\mathbb{N}^{(I)}$ as the collection of finitely supported functions from $I$ to $\mathbb{N}$:

$$\mathbb{N}^{(I)}=\{\nu:I \rightarrow \mathbb{N}\mid\text{$\nu(i)=0$ for all but finitely many $i\in I$}\}$$

Then for any $\nu\in \mathbb{N}^{(I)}$, setting

$$\x^\nu=\prod_{i\in I} \x_i^{\nu_i}$$

makes $\x^\nu$ an element of $P$. We call elements of the form

$$a\x^\nu$$

*monomials*. Then any polynomial $u$ can be expressed as a finite sum of monomials

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu=0$ for all but finitely many $\nu$}$$

On the other hand, for any $\nu\in \mathbb{N}^{(I)}$, defining

$$\lvert\nu\rvert=\sum_{i\in I} \nu_i$$

allows us to view $P=A[\x_i]_{i\in I}$ as an $\mathbb{N}$-graded ring

$$P=\bigoplus_{n\in \mathbb{N}}\bigoplus_{\lvert\nu\rvert=n}(A[\x_i]_{i\in I})_\nu=\bigoplus_{n\in \mathbb{N}} P_n$$

For each $n$, we call the elements of $P_n$ *homogeneous polynomials* of degree $n$. Also, for any polynomial $u\in P$, the degree $n$ component of $u$ in this homogeneous decomposition is also written as $u_n$.

::: Definition 1
Let an arbitrary element of the polynomial ring $P=A[\x_i]_{i\in I}$

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu=0$ for all but finitely many $\nu$}$$

be given. Then, among those satisfying $u_n\neq 0$, the largest $n$ is called the *degree* of $u$ and denoted by $\deg(u)$. By definition, the degree of a polynomial having only a constant term is $0$, but in particular, for the additive identity of $P$, $0$, we define $\deg(0)=-\infty$.
:::

Then the following proposition holds trivially.

::: Proposition 2
For two polynomials $u,v$, the following hold.

1. If $\deg (u)\neq\deg(v)$, then $u+v\neq 0$ and the equality

    $$\deg(u+v)=\sup(\deg(u), \deg(v))$$

    holds. If $\deg(u)=\deg(v)$, then the inequality $\deg(u+v)\leq\deg(u)$ holds.
2. The inequality $\deg(uv)\leq\deg(u)+\deg(v)$ holds.
:::

The reason the second condition of this proposition is not an equality lies in $A$. To examine this more closely, consider the polynomial ring $A[\x]$ in one variable. Then any polynomial of $A[\x]$ can be written in the form

$$u(\x)=\sum_{i=0}^n a_i\x^i\qquad\text{($a_n\neq 0$)}$$

and we call $a_n\x^n$ the *leading term* of the polynomial $u$, and its coefficient $a_n$ the *leading coefficient* of the polynomial $u$. If the leading coefficient of $u$ is $1$, we call $u$ a *monic polynomial*.

Now for any two (univariate) polynomials

$$u(\x)=\sum_{i=0}^n a_i\x^i,\qquad v(\x)=\sum_{j=0}^m b_j \x^j$$

their product is explicitly given by the formula

$$u(\x)v(\x)=\sum_{k=0}^{n+m}\left(\sum_{i=0}^k a_ib_{k-i}\right)\x^k$$

and therefore the coefficient of the highest degree term is $a_nb_m$. However, if $A$ is not an integral domain, the product of two nonzero elements $a_n$, $b_m$ could be $0$, so $uv$ might not be a polynomial of degree $m+n$. Using this discussion, we obtain the following.

::: Lemma 3
For an integral domain $A$, the following hold.

1. For any $u,v\in A[\x]$, we have $\deg(uv)=\deg(u)+\deg(v)$. 
2. The units of $A[\x]$ are exactly the units of $A$.
3. $A[\x]$ is an integral domain. 
:::

Now let us return to the general case. If any two polynomials $u,v\in A[\x_i]_{i\in I}$ are given, since only finitely many indeterminates appear in these polynomials anyway, when computing $uv$ it suffices to choose a finite set $J\subseteq I$ and view this in $A[\x_j]_{j\in J}$ instead of $A[\x_i]_{i\in I}$. Then the fact that $A[\x_j]_{j\in J}$ is an integral domain follows from [Lemma 3](#lem3){: data-lid="z7kwa" } and the following isomorphism:

$$A[\x_1,\x_2]\cong (A[\x_1])[\x_2]$$

That is, the following holds. 

::: Proposition 4
For an integral domain $A$ and a polynomial ring $P=A[\x_i]_{i\in I}$, the following hold. 

1. For any $u,v\in P$, we have $\deg(uv)=\deg(u)+\deg(v)$. 
2. The units of $P$ are exactly the units of $A$.
3. $P$ is an integral domain. 
:::

## Univariate Polynomials

We now examine univariate polynomials in somewhat more detail. 

::: Proposition 5
Suppose we are given, in $A[\x]$, a degree $m$ polynomial $u(\x)$ and a degree $n$ polynomial $v(\x)$, and let the leading coefficient of $v$ be $b_n$. If $k=\sup(m-n+1,0)$, then for the following equation

$$b_n^k u=qv+r,\qquad \deg r < n$$

there exist $q,r\in A[\x]$ satisfying it. 
:::

::: Proof
If $n>m$, then $k=0$, and in this case setting $q=0$, $r=u$ satisfies the given equation, so there is nothing to prove in this case. Therefore, assume $n\leq m$.  

We use induction on $m$. Let the leading coefficient of $u$ be $a_m$. If

$$v(\x)=\sum_{j=0}^n b_j\x^j$$

then there exists a polynomial of degree less than $m$, $u_1\in A[\x]$, such that we can write

$$b_n^k u(\x)=b_n^{k-1}a_m\x^{m-n}v(\x)+b_n^{k-1}u_1(\x)$$

This equation is simply obtained by multiplying $v(\x)$ by $a_m\x^{m-n}$ to match the leading term with that of $b_n u$, obtaining

$$b_nu(\x)=a_m\x^{m-n}v(\x)+u_1(\x)$$

and then multiplying both sides by $b_n^{k-1}$. Now by the inductive hypothesis, there exist polynomials $q_1,r\in A[\x]$ such that the equation

$$b_n^{k-1}u_1(\x)=q_1(\x)v(\x)+r(\x),\qquad \deg(r) < n$$

holds. Here, what the inductive hypothesis directly gives for $u_1$ is an equation for $k_1=\sup(\deg(u_1)-n+1,0)$, but from $\deg(u_1)\leq m-1$ and $n\leq m$ we have $k_1\leq k-1$, so multiplying both sides by $b_n^{(k-1)-k_1}$ yields the above equation. Now, substituting this back into the earlier equation, we obtain

$$b_n^k u(\x)=(b_n^{k-1}a_m\x^{m-n}+q_1(\x))v(\x)+r(\x)$$
:::

The coefficient $b_n^k$ appearing here arises when multiplying $v$ by powers of $\x$ to match the leading terms and lowering the degree of the remainder one by one; for instance, if $b_n$ is invertible, one can verify that $q$ and $r$ satisfying the above equation are uniquely determined. In particular, if every nonzero element of $A$ is invertible, that is, if $A=\mathbb{K}$, then in the situation above, for the equation

$$u=qv+r,\qquad \deg r < n$$

we can uniquely determine $q,r$ satisfying it. Moreover, in this case the polynomial ring $\mathbb{K}[\x]$ is an integral domain by [Lemma 3](#lem3){: data-lid="ebkzt" }, and thus defining $N:\mathbb{K}[\x] \rightarrow \mathbb{Z}_{\geq 0}$ by

$$N: u\mapsto \deg(u)\qquad \text{where $N(0)=0$}$$

we see that $\mathbb{K}[\x]$ is a Euclidean domain.

::: Proposition 6
For any field $\mathbb{K}$, $\mathbb{K}[\x]$ is a Euclidean domain. 
:::

In particular, the notion of greatest common divisor is well-defined over a Euclidean domain, and related to this, Bézout's lemma also holds. ([§Integral Domains, ⁋Theorem 7](/en/math/ring_theory/integral_domains#thm7){: data-lid="g0mdk" })

We have previously seen that in $\mathbb{K}[\x]$, the images of arbitrary (non-zero) elements of $\mathbb{K}$ are units of $\mathbb{K}[\x]$. ([Lemma 3](#lem3){: data-lid="ug3hj" }) On the other hand, since whether one element divides another in a Euclidean domain can be determined by running the Euclidean algorithm, an arbitrary non-constant $u\in \mathbb{K}[\x]$ being irreducible is equivalent to: whenever $1\leq \deg(v)<\deg(u)$, $u$ is not divisible by $v\in \mathbb{K}[\x]$. 

Meanwhile, by [Proposition 6](#prop6){: data-lid="hq18v" } and [§Integral Domains, ⁋Theorem 19](/en/math/ring_theory/integral_domains#thm19){: data-lid="98whq" }, $\mathbb{K}[\x]$ is a UFD, and thus we can define irreducible elements, etc., of $\mathbb{K}[\x]$. On the other hand, since the units of $\mathbb{K}[\x]$ are precisely the units of $\mathbb{K}$, any irreducible polynomial $u$ satisfies (by definition) $\deg(u)\geq 1$, and since $u$ is irreducible, if $v\mid u$, then $v$ is a constant polynomial or a constant multiple of $u$. In particular, two irreducible polynomials having a non-constant common factor must be constant multiples of each other, so two distinct *monic* irreducible polynomials are coprime. In this way, any polynomial in $\mathbb{K}[\x]$ other than $0$ can be uniquely expressed as the product of its leading coefficient and monic irreducible polynomials. 

::: Proposition 7
For any polynomial $u\in A[\x]$ and any $a\in A$, the remainder when $u(\x)$ is divided by $\x-a$ is $u(a)$. Therefore, $u$ having $a$ as a root is equivalent to $\x-a$ being, in $A[\x]$, a divisor of $u$. 
:::

The proof of this follows by applying [Proposition 5](#prop5){: data-lid="k9qhn" } to the monic polynomial $v(\x)=\x-a$, and this is in fact a familiar result from middle school. As another result, if $u$ has $a$ as a root, we know that $u$ must necessarily be written in the form

$$u(\x)=(\x-a)^p v(\x),\qquad v(a)\neq 0$$

In this case, we call $p$ the *multiplicity* of the root $a$. Then the following holds. 

::: Proposition 8
Suppose any two polynomials $u,v\in A[\x]$ have a common root $a$, and in $u$ and $v$ respectively, let the multiplicity of $a$ be $p,q$. Then the following hold.

1. In the polynomial $u+v$, the multiplicity of $a$ is at least $\inf(p,q)$, and equality holds when $p\neq q$.
2. In the polynomial $uv$, the multiplicity of $a$ is at least $p+q$, and equality holds when $A$ is an integral domain.
:::
::: Proof
Suppose $u(\x) = (\x-a)^p u_1(\x)$, $v(\x) = (\x-a)^q v_1(\x)$ and $u_1(a) \neq 0$, $v_1(a) \neq 0$. Without loss of generality, assume $p \leq q$; then we obtain the formula

$$u(\x) + v(\x) = (\x-a)^p (u_1(\x) + (\x-a)^{q-p}v_1(\x))$$

and thus obtain the desired inequality. If here $p < q$, then $a$ is not a root of $u_1(\x) + (\x-a)^{q-p}v_1(\x)$, so we obtain the desired result. 

For the second result, under the same assumption,

$$u(\x)v(\x) = (\x-a)^{p+q}u_1(\x)v_1(\x)$$

holds. If $A$ is an integral domain, then $u_1(a)v_1(a) \neq 0$, from which we obtain the second result. 
:::

Furthermore, if $A$ is an integral domain, we can show the following inductively.

::: Proposition 9
Fix an integral domain $A$. Let a nonzero element $u$ of $A[\x]$ have distinct roots $a_1,\ldots, a_r$, and let their multiplicities be $p_1,\ldots, p_r$, respectively. Then

$$u(\x)=(\x-a_1)^{p_1}\cdots(\x-a_r)^{p_r}v(\x),\qquad v(a_1),\ldots, v(a_r)\neq0$$

for some $v\in A[\x]$. 
:::
::: Proof
We proceed by induction on $r$. The case $r=1$ is trivial, so suppose that for $u$, $r$ roots $a_1,\ldots, a_r$ are given, and apply the inductive hypothesis to the first $r-1$ roots to write

$$u(\x)=u_1(\x)u_2(\x)=(\x-a_1)^{p_1}\cdots(\x-a_{r-1})^{p_{r-1}}u_2(\x)$$

Then, from the assumption that $A$ is an integral domain, we know that $u_1(a_r)\neq 0$, so necessarily $u_2(a_r)=0$, and in $u_2$, the multiplicity of $a_r$ must be $p_r$. From this we obtain the desired claim. 
:::

In particular, for any integral domain $A$, we know that any polynomial in $A[\x]$ of degree $n$ has at most $n$ roots (counted with multiplicity). Therefore, if two polynomials of degree at most $n$, $f,g\in A[\x]$, are given, and if we assume that for $n+1$ distinct elements $a_1,\ldots, a_{n+1}$, $f(a_i)=g(a_i)$ holds, then necessarily $f=g$. From this we obtain the following result. 

::: Proposition 10
In a field $\mathbb{K}$, fix $n$ distinct elements $a_1,\ldots, a_n$. For arbitrary elements of $\mathbb{K}$, $b_1,\ldots, b_n$, define for each $i$

$$u_i(\x)=\prod_{j\neq i}\frac{\x-a_j}{a_i-a_j}$$

Then 

$$u=b_1 u_1 + \cdots + b_n u_n$$

is the unique polynomial that satisfies, for each $i$, $u(a_i)=b_i$ and has degree less than $n$. 
:::
::: Proof
Uniqueness is trivial by the above argument, and it remains only to verify that evaluating $u$ at each $a_i$ yields the value $b_i$. If $j\neq i$, the numerator of $u_j$ contains the factor $\x-a_i$, so $u_j(a_i)=0$; and since $u_i(a_i)=1$, we obtain $u(a_i)=b_i$. 
:::

The fact seen above, that a polynomial of degree $n$ over an integral domain has at most $n$ roots, is also used in number theory. For a prime number $p$, $\mathbb{Z}/p\mathbb{Z}$ is a field ([§Units and Zero Divisors, ⁋Example 7](/en/math/ring_theory/units_and_zero_divisors#ex7){: data-lid="zj4hz" }), so for a polynomial with integer coefficients whose leading coefficient is not divisible by $p$, of degree $n$, $f$, the congruence $f(x)\equiv 0\pmod{p}$ has, modulo $p$, at most $n$ solutions.

On the other hand, a useful method for finding multiple roots is to differentiate the given polynomial. We can define algebraically what a derivation is ([\[Multilinear Algebra\] §Derivations](/en/math/multilinear_algebra/derivations){: data-lid="dhqm2" }), but in this category, without such discussion, we choose to define $D: A[\x] \rightarrow A[\x]$ by the following formula:

$$D:\left(u(\x)=\sum_{i=0}^n a_i\x^i\right)\mapsto \left((Du)(\x)=\sum_{i=1}^n i.a_i\x^{i-1}\right)\tag{$\ast$}$$

Here, $i.a_i$ is defined by 

$$i.a_i=\underbrace{a_i+\cdots+a_i}_\text{\scriptsize$i$ times}$$

as an element of $A$. The only property we will use in the remaining discussion is the Leibniz rule

$$D(uv)=(Du)v+u(Dv)$$

which in [\[Multilinear Algebra\] §Derivations](/en/math/multilinear_algebra/derivations){: data-lid="34nqu" } is the definition of a derivation, but if we take the formula ($\ast$) above as the definition, it can be verified by direct computation. 

::: Proposition 11
For any polynomial $u \in A[\x]$, a necessary and sufficient condition for a root of $u$, $a \in A$, not to be a multiple root is that $a$ is not a root of $Du$. 
:::
::: Proof
By the assumption that $a$ is a root of $u$, we have $u = (\x - a)v$ for some $v \in A[\x]$, and here, a necessary and sufficient condition for $a$ not to be a multiple root of $u$ is that $v(a) \neq 0$. Now since $Du = v + (\x - a)Dv$, we have $(Du)(a) = v(a)$.
:::

More generally, using induction we can show the following.

::: Proposition 12
For any polynomial $u \in A[\x]$, if a root of $u$, $a \in A$, has multiplicity $k$, then $a$ is a root of $Du$ of multiplicity $\geq k-1$. If $k \cdot 1$ is cancellable in $A$, then $a$ has, with respect to $Du$, order $k-1$.
:::
::: Proof
Similarly to the proposition above, setting $u=(\x-a)^k v$, since $v(a)\neq 0$, from

$$Du=k(\x-a)^{k-1}v+(\x-a)^k Dv=(\x - a)^{k-1}(kv + (\x - a)Dv)$$

we obtain the first claim. If $k\cdot 1$ is cancellable in $A$, evaluating $kv+(\x-a)Dv$ at $\x=a$ gives the value $k.v(a)$, which is not $0$, so the latter claim holds.
:::

::: Proposition 13
Let an integral domain $A$ and a set $I$ be given, and let $(H_i)_{i\in I}$ be a family, indexed by $I$, of infinite subsets of $A$. Also, let $H=\prod_{i\in I} H_i\subseteq A^I$. Then if $u$ is a non-zero element of $A[\x_i]_{i\in I}$, $H$ and the following set

$$H_u=\{(x_i)\in H\mid u(x_i)\neq 0\}$$

have the same cardinality.
:::
::: Proof
The case where $I$ is a finite set can be shown by induction. Let $\lvert I\rvert=n$, and prove by induction on $n$. First, in the case $n=0$, there is nothing to prove. To use induction, simplify notation by letting $I=\{1,\ldots, n\}$, $J=\{1,\ldots, n-1\}$, and $B=A[\x_i]_{i\in J}$. Then since $u\neq 0$,

$$u=\sum_{k=0}^m v_k\x_n^k$$

holds for some $v_k\in B$. Here, $v_m\neq 0$. Now by the inductive hypothesis, the set

$$H_{v_m}=\{(x_i)\in \prod_{i\in J} H_i\mid v_m(x_i)\neq 0\}$$

has the same cardinality as $\prod_{i\in J} H_i$. Now for any element of $H_{v_m}$, $(x_i)_{i\in J}$,

$$w(\x)=\sum_{k=0}^mv_k(x_1,\ldots, x_{n-1})\x_n^k$$

is a non-zero polynomial. Meanwhile, for the set

$$\{a\in H_n\mid w(a)\neq 0\}$$

from the fact that $H_n$ is an infinite set, the argument after [Proposition 9](#prop9){: data-lid="yw1c8" }, and [\[Set Theory\] §Natural Numbers and Infinite Sets, ⁋Proposition 13](/en/math/set_theory/natural_numbers#prop13){: data-lid="z3cnq" },

$$\lvert H\rvert\geq \lvert H_u\rvert\geq \lvert H_{v_m}\rvert\lvert H_n\rvert=\lvert H\rvert$$

holds. In the case where $I$ is an infinite set, one can reduce to the finite case by considering the polynomial ring containing only the indeterminates appearing in $u$.
:::

In particular, if $I$ is not empty, $H_u$ is an infinite set.

## Factorization

Given any ring homomorphism $\phi:A \rightarrow B$, any $u\in A[\x_i]_{i\in I}$ can be viewed via $\phi$ as an element of $B[\x_i]_{i\in I}$.

In particular, consider the case where $A$ is an integral domain and $\phi$ is the canonical inclusion $A \hookrightarrow \Frac(A)$. Then since $\Frac(A)$ is a field, by [Proposition 6](#prop6){: data-lid="7uocn" }, $(\Frac A)[\x]$ is a Euclidean domain, and thus if we view any $u\in A[\x]$ in $(\Frac A)[\x]$, then $u$ can be factored at least in $(\Frac A)[\x]$. It is then the natural next step to examine how the factorization carried out here is reflected in $A[\x]$.

::: Proposition 14 (Gauss)
Consider a UFD $A$, its field of fractions $\Frac(A)$, and an element of $A[\x]$, $u$. If $u$ is reducible in $(\Frac A)[\x]$, then $u$ is also reducible in $A[\x]$.
:::
::: Proof
Suppose that in $(\Frac A)[\x]$, a polynomial $u$ is expressed as a product of two polynomials

$$u(\x)=\tilde{v}_1(\x)\tilde{v}_2(\x),\qquad \tilde{v}_i\in (\Frac A)[\x]$$

Then, multiplying both sides by the least common multiples of the denominators of the coefficients of $\tilde{v}_1$ and $\tilde{v}_2$, for an appropriate $a\in A$,

$$a u(\x)=v_1(\x)v_2(\x)$$

holds for some $v_i\in A[\x]$. If $a$ is a unit, there is nothing more to prove, so assume $a$ is not a unit. Then $a=p_1\cdots p_r$ for some irreducible elements $p_i\in A$. At this time, by [§Integral Domains, ⁋Proposition 17](/en/math/ring_theory/integral_domains#prop17){: data-lid="iken1" }, $(p_i)$ is a prime ideal of $A$, and thus

$$(A/p_iA)[\x]\cong A[\x]/p_iA[\x]$$

is an integral domain by [Proposition 4](#prop4){: data-lid="s1jyj" }. Therefore, after modding out the equation $au=v_1v_2$ by $p_iA[\x]$, we know that either $v_1$ or $v_2$ in $(A/p_iA)[\x]$ must be $0$. That is, the coefficients of one of $v_1$ or $v_2$ are all multiples of $p_i$, and thus we can cancel this $p_i$ to obtain another polynomial in $A[\x]$. Now, applying this to all $p_i$, we obtain the desired result.
:::

From this we obtain the following.

::: Corollary 15
Consider a UFD $A$, its field of fractions $\Frac A$, and a polynomial $u(\x) \in A[\x]$, and let the greatest common divisor of the coefficients of $u(\x)$ be $1$. Then $u(\x)$ being irreducible in $A[\x]$ is equivalent to $u(\x)$ being irreducible in $(\Frac A)[\x]$.
:::
::: Proof
By [Proposition 14](#prop14){: data-lid="6deee" }, if $u(\x)$ is reducible in $(\Frac A)[\x]$, then it is also reducible in $A[\x]$.

Conversely, suppose the greatest common divisor of the coefficients of $u(\x)$ is 1, and assume $u(\x)$ is reducible in $A[\x]$. That is, we can write

$$u(\x) = v_1(\x) v_2(\x)$$

where the greatest common divisor of the coefficients of $v_1(\x)$ and $v_2(\x)$ must also be 1, so in particular $v_1,v_2$ are both not constant. From this, $u=v_1v_2$ means that even when viewed in $(\Frac A)[\x]$, $u$ is reducible.
:::

Then one of the key results related to factorization is the following theorem.

::: Theorem 16
A necessary and sufficient condition for $A$ to be a UFD is that $A[\x]$ is a UFD.
:::
::: Proof
Since it is trivial that if $A[\x]$ is a UFD then $A$ is also a UFD, it suffices to show the converse direction.

For a UFD $A$, let an element of $A[\x]$ other than $0$ be $u(\x)$, and if we let the greatest common divisor of the coefficients of $u(\x)$ be $d$, then by setting $u(\x)=du_0(\x)$ we can obtain a polynomial whose coefficients have greatest common divisor $1$, namely $u_0\in A[\x]$, so we may assume without loss of generality that the greatest common divisor of the coefficients of $u$ is $1$.

By [Proposition 6](#prop6){: data-lid="99ytv" } and [§Integral Domains, ⁋Theorem 19](/en/math/ring_theory/integral_domains#thm19){: data-lid="c035k" }, $u$ can be factored in a unique way in $(\Frac A)[\x]$, and applying [Proposition 14](#prop14){: data-lid="zly8u" } to this factorization, we can factor $u$ in $A[\x]$. Meanwhile, since the greatest common divisor of the coefficients of $u$ is $1$, the greatest common divisor of the coefficients of the factors of $u$ obtained in this way is also $1$, and therefore by [Corollary 15](#cor15){: data-lid="3l40r" } they are irreducible in $A[\x]$. From this we obtain a factorization of $u$ in $A[\x]$, and the uniqueness is trivial from the fact that in $(\Frac A)[\x]$, each of their components is a $\Frac A$-multiple of the corresponding factor.
:::

## Ring of Rational Functions

We now define rational function rings and power series rings, which are variants of polynomial rings. Earlier in [Proposition 4](#prop4){: data-lid="u4tvs" }, we proved that for any field $\mathbb{K}$, $\mathbb{K}[\x_i]_{i\in I}$ is an integral domain. Therefore, the field of fractions of $\mathbb{K}[\x_i]_{i\in I}$ is well-defined.

::: Definition 17
Over a field $\mathbb{K}$, we call the field of fractions of the polynomial ring $\mathbb{K}[\x_i]_{i\in I}$ the *field of rational functions*, and denote it by $\mathbb{K}(\x_i)_{i\in I}$.
:::

Earlier, we saw that a polynomial ring can be viewed as an $\mathbb{N}$-graded ring using multidegree. In a similar way, let us define a degree on $\mathbb{K}(\x_i)_{i\in I}$ as well. The natural choice is, for any element of $\mathbb{K}(\x_i)_{i\in I}$, $u/v$, to define

$$\deg(u/v)=\deg(u)-\deg(v)$$

and we can verify that this is well-defined. As with polynomials, we define $\deg(0)=-\infty$.

Then the following proposition is the analogue of [Proposition 2](#prop2){: data-lid="exzkm" }.

::: Proposition 18
For two rational fractions $r, s$, the following hold.

1. If $\deg r \ne \deg s$, then
    
    $$r + s \ne 0 \quad \text{이고} \quad \deg(r + s) = \sup(\deg r, \deg s)$$
    
    holds. If $\deg r = \deg s$, then $\deg(r + s) \leq \deg r$.
2. $\deg(rs) = \deg r + \deg s$.
:::
::: Proof
For both claims, it suffices to consider only the case where $r, s \ne 0$. Therefore, let $r =u/v$, $s = w/z$, with $u, v, w, z$ all nonzero polynomials. In any case, the idea is to first compute the given expression and then apply [Proposition 2](#prop2){: data-lid="0skil" } and [Lemma 3](#lem3){: data-lid="ffcyl" }.

1. We have $r + s = (uz+vw)/(vz)$. First, suppose $\deg r \ne \deg s$, that is, $\deg u + \deg z \ne \deg w + \deg v$. Then $uz + vw \ne 0$, and
    
    $$\begin{aligned}\deg(r + s) &= \deg(uz + vw) - \deg(vz) \\
    &= \sup(\deg(uz), \deg(vw)) - \deg(vz) \\
    &= \sup(\deg(uz) - \deg(vz), \deg(vw) - \deg(vz)) \\
    &= \sup(\deg r, \deg s).\end{aligned}$$
    
    Now suppose $\deg r = \deg s$, that is, $\deg u + \deg z = \deg w + \deg v$. If $r + s \ne 0$, then
    
    $$\deg(r + s) = \deg(uz + vw) - \deg(vz)\leq \deg(uz) - \deg(vz) = \deg r$$

    so the claim holds.
    
2. We have $rs = (uw)/(vz)$, and therefore

    $$\deg(rs) = \deg(uw) - \deg(vz) = \deg u - \deg v + \deg w - \deg z = \deg r + \deg s.$$
:::

## Power Series Ring

A power series ring is another variant of a polynomial ring, and is the collection of infinite sums of monomials

$$u(\x)=\sum_{\nu\in \mathbb{N}^{(I)}} a_\nu \x^\nu,\qquad\text{$a_\nu$ need not satisfy finiteness condition}$$

We write this as $A[[\x_i]]_{i\in I}$ and call it the *ring of formal power series*.

Except for the fact that formal power series are *infinite* sums of monomials, we can define concepts analogous to those for polynomials. For example, for a formal power series $u$, we can define its degree $p$ component $u_p$. However, for the (total) degree of $u$, since the degree of elements other than polynomials would be $+\infty$, there is no reason to use this in $A[[\x_i]]_{i\in I}$. Instead, for any formal power series $u$, we define the *order* of $u$, $\omega(u)$, to be, among those with $u_p\neq 0$, the *smallest* $p$. Similarly, setting $\omega(0)=\infty$, the formula

$$\omega(u+v)\geq \inf(\omega(u),\omega(v)),\quad\text{equality if $\omega(u)\neq\omega(v)$}$$

and the formula

$$\omega(uv)\geq \omega(u)+\omega(v)$$

hold.

For degree, when $A$ was an integral domain, the equality corresponding to the second formula held ([Proposition 4](#prop4){: data-lid="oe147" }). Likewise, the following holds.

::: Proposition 19
For an integral domain $A$, the following hold.

1. $A[[\x_i]]_{i\in I}$ is an integral domain.
2. For two nonzero elements $u,v\in A[[\x_i]]_{i\in I}$, $\omega(uv)=\omega(u)+\omega(v)$ holds.
:::

However, one must be somewhat careful: unlike [Proposition 4](#prop4){: data-lid="vn0u0" }, the units of $A[[\x_i]]_{i\in I}$ are larger than those of $A$. For example, consider the formula

$$(1-\x)\left( \sum_{n=0}^\infty \x^n\right)=1$$

More generally, the following holds.

::: Proposition 20
For any $u\in A[[\x_i]]_{i\in I}$, $u$ being invertible in $A[[\x_i]]_{i\in I}$ is equivalent to the constant term of $u$ being invertible in $A$.
:::

---

**References**

**[DF]** D. S. Dummit and R. M. Foote, *Abstract algebra*, 3rd ed., Wiley, 2004.
