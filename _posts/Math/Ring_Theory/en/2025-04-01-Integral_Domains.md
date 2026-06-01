---
title: "Integral Domains"
description: "This post covers the definition of the norm in a Euclidean domain and the division algorithm, using integer division and polynomial division as examples to show that every ideal is principal."
excerpt: "Definitions of Euclidean domains, PIDs, and UFDs, and their inclusion relationships"

categories: [Math / Ring Theory]
permalink: /en/math/ring_theory/integral_domains
header:
    overlay_image: /assets/images/Math/Ring_Theory/Integral_Domains.png
    overlay_filter: 0.5
sidebar: 
    nav: "ring_theory-en"

date: 2025-04-01
last_modified_at: 2025-04-01
weight: 1
translated_at: 2026-06-01T22:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-01T22:30:02+00:00
---
In the posts in this category, we examine properties of rings in somewhat greater detail. The first topic we cover is integral domains. ([\[Algebraic Structures\] §Field of Fractions, ⁋Definition 5](/en/math/algebraic_structures/field_of_fractions#def5)) 

## Euclidean Domains

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Fix an integral domain $$A$$. If a function $$N : A \to \mathbb{Z}^{\geq0}$$ satisfies $$N(0) = 0$$, we call it a *norm* on $$A$$. If $$N(a) > 0$$ for every $$a \neq 0$$, we call this norm a *positive norm*. 

</div>

The condition defining a norm is very weak; for instance, given a fixed integral domain, there are many ways to define a norm on it. 

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> An integral domain $$A$$ is called a *Euclidean domain* if there exists a norm $$N$$ on $$A$$ such that for any $$a, b \in A$$ (with $$b \neq 0$$), there exist elements $$q, r \in A$$ satisfying

$$a = qb + r \qquad\text{with $r = 0$ or $N(r) < N(b)$}$$

Here $$q$$ is called the *quotient* and $$r$$ the *remainder*.

</div>

If we replace $$A$$ by the integers $$\mathbb{Z}$$ and regard $$N$$ as the absolute value function $$\lvert-\rvert:\mathbb{Z} \rightarrow \mathbb{Z}^{\geq0}$$, this is exactly the familiar division algorithm for integers. As another example, if we define $$N$$ on the polynomial ring $$\mathbb{K}[\x]$$ to be the degree function, we obtain the polynomial division algorithm. Finally, any field $$\mathbb{K}$$ is a Euclidean domain, via the function $$N$$ sending every $$x\in\mathbb{K}$$ to $$0$$. The reason this satisfies the above condition is that every nonzero element of a field divides every other element. 

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> Every ideal of a Euclidean domain is principal. More precisely, for any nonzero ideal $$\mathfrak{a}$$ of a Euclidean domain $$A$$, if we let $$a$$ be an element of $$\mathfrak{a}$$ with minimal norm, then $$\mathfrak{a}=(a)$$. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

If $$\mathfrak{a}$$ is the zero ideal there is nothing to prove, so assume $$\mathfrak{a}\neq 0$$. 

The image of $$\mathfrak{a}\setminus \{0\}$$ under $$N$$ is a subset of $$\mathbb{Z}^{\geq 0}$$, which is well-ordered; hence we can choose a nonzero element $$a$$ of $$\mathfrak{a}$$ with minimal norm. 

Since $$(a)\subseteq \mathfrak{a}$$ is obvious, to show $$(a)=\mathfrak{a}$$ it suffices to prove the reverse inclusion. Applying the division algorithm to an arbitrary element $$x$$ of $$\mathfrak{a}$$, we have

$$x=qa+r,\qquad\text{with $r = 0$ or $N(r) < N(a)$}$$

Then $$r = x - qa$$, and since both $$x$$ and $$qa$$ lie in $$\mathfrak{a}$$, so does $$r$$. By the minimality of the norm of $$a$$, the inequality $$N(r) < N(a)$$ is impossible, so $$r$$ must be $$0$$. Thus $$x=qa$$, and hence $$\mathfrak{a} = (a)$$.

</details>

Now we define the following.

<div class="definition" markdown="1">

<ins id="def4">**Definition 4**</ins> Let $$A$$ be a commutative ring and let $$a, b \in A$$ ($$b \neq 0$$). We define the following.

1. We say $$a$$ is a *multiple* of $$b$$ if there exists $$x \in A$$ such that $$a = bx$$. In this case we say $$b$$ *divides* $$a$$, and write $$b \mid a$$. 
2. A *greatest common divisor* of $$a$$ and $$b$$ is a nonzero element $$d$$ satisfying the following conditions.
   - $$d \mid a$$ and $$d \mid b$$, and
   - if $$d'$$ satisfies $$a \mid d'$$ and $$b \mid d'$$, then always $$d \mid d'$$

The greatest common divisor of $$a$$ and $$b$$ is denoted $$\gcd(a, b)$$ or simply $$(a, b)$$.

</div>

By definition, $$b \mid a$$ holding in the ring $$A$$ is equivalent to $$(a) \subset (b)$$. In particular, if $$d$$ is a common divisor of $$a$$ and $$b$$, then $$(d)$$ must contain $$(a, b)$$. Thus the above two conditions can be translated into the language of ideals as follows:

- $$\mathfrak{a} \subseteq (d)$$
- $$(d) \subseteq (d')$$ for any principal ideal $$(d')$$ such that $$a, b \in (d')$$

That is, the greatest common divisor of $$a$$ and $$b$$ (if it exists) is an element generating the smallest principal ideal containing $$a$$ and $$b$$. An integral domain in which this is always possible is called a *GCD domain*, but this definition will not appear separately in our discussion. 

From the above discussion we obtain the following. 

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5**</ins> Let $$a, b \in A$$ in a commutative ring $$A$$ be nonzero. If the ideal $$(a, b)$$ generated by $$a$$ and $$b$$ is a principal ideal $$(d)$$ generated by some element $$d \in A$$, then $$d$$ is a greatest common divisor of $$a$$ and $$b$$.

</div>

Then a greatest common divisor is uniquely determined. We must be somewhat careful in speaking of this uniqueness, because for example in the integers $$(2)$$ and $$(-2)$$ are the same ideal. 

<div class="proposition" markdown="1">

<ins id="prop6">**Proposition 6**</ins> Let $$A$$ be an integral domain. Suppose two elements $$d, d' \in A$$ generate the same principal ideal, i.e., $$(d) = (d')$$. Then there exists a unit $$u \in A$$ such that $$d' = ud$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$d = 0$$ or $$d' = 0$$ the claim is obvious, so assume $$d, d'$$ are both nonzero. Since $$(d) = (d')$$, there exist $$x, y \in A$$ such that

$$d = xd',\qquad d' = yd$$

Then from $$d = xyd$$ we obtain $$(1-xy)d=0$$. Since $$A$$ is an integral domain and $$d \neq 0$$, we have $$xy = 1$$, and therefore $$x$$ and $$y$$ are units and inverses of each other. 

</details>

Then, just as with Bézout's lemma for the integers, the following holds for Euclidean domains. 

<div class="proposition" markdown="1">

<ins id="thm7">**Theorem 7**</ins> Let $$A$$ be a Euclidean domain. Let $$a, b \in A$$ be nonzero elements, and let $$r_n$$ be the last nonzero remainder obtained by repeating the process of [Definition 2](#def2) until it can no longer continue. Then the following hold:

1. $$r_n$$ is a greatest common divisor of $$a$$ and $$b$$. 
2. $$(r_n)$$ is the same ideal as $$(a, b)$$. In particular, $$r_n$$ can be written as an $$A$$-linear combination of $$a$$ and $$b$$; that is, there exist $$x, y \in A$$ satisfying $$r_n=ax+by$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Let us show that $$r_n$$ divides $$a$$ and $$b$$. The last step of the Euclidean algorithm is given by the equation
    
$$r_{n-1} = q_n r_n$$

and in general the steps take the form

$$r_{k-2}=q_{k}r_{k-1}+r_{k}$$

where we set $$r_{-2}=a$$, $$r_{-1}=b$$. Our claim is that every remainder $$r_k$$ is divisible by $$r_n$$. To show this, we use induction working backwards through the equations.

First, $$r_n\mid r_{n-1}$$ is obvious. Thus, assuming $$r_n \mid r_k$$ and $$r_n \mid r_{k-1}$$, we see from the above equation that $$r_n$$ also divides $$r_{k-2}$$, and hence by induction $$r_n$$ divides both $$a$$ and $$b$$. That is, $$(a), (b)\subset (r_n)$$, so $$(a,b)\subset (r_n)$$. On the other hand, for $$r_n$$ to be the greatest common divisor of $$a$$ and $$b$$, we must have $$(a,b)=(r_n)$$, and this is immediate because the above equations allow us to express $$r_n$$ as an $$A$$-linear combination of $$a$$ and $$b$$. 

</details>


## Principal Ideal Domains

Now we define the following. 

<div class="definition" markdown="1">

<ins id="def8">**Definition 8**</ins> A *principal ideal domain* is an integral domain in which every ideal is principal.

</div>

Then from [Proposition 3](#prop3) we know that every Euclidean domain is a PID. However, the converse does not hold. The division algorithm gives a concrete method for obtaining the greatest common divisor of two elements $$a, b$$, but by [Proposition 5](#prop5) the following holds. 

<div class="proposition" markdown="1">

<ins id="cor9">**Corollary 9**</ins> Let $$A$$ be a principal ideal domain and let $$a, b \in A$$ be nonzero elements. Let $$d$$ be a generator of the principal ideal $$(a, b)$$ generated by $$a, b$$. Then the following hold:

1. $$d$$ is a greatest common divisor of $$a$$ and $$b$$.
2. $$d$$ can be written as an $$A$$-linear combination of $$a$$ and $$b$$. That is, there exist $$x, y \in A$$ such that

   $$d = ax + by$$

3. $$d$$ is unique in the sense of [Proposition 6](#prop6). 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

This follows from [Proposition 5](#prop5) and [Proposition 6](#prop6); the second assertion is immediate from the assumption $$(a,b)=(d)$$. 

</details>

One useful property of a principal ideal domain is that every prime ideal is maximal. 

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> Every nonzero prime ideal of a principal ideal domain $$A$$ is a maximal ideal.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose, for contradiction, that for a nonzero prime ideal $$\mathfrak{p} = (p)$$ of $$A$$ there exists an ideal $$\mathfrak{m}$$ with $$\mathfrak{p} \subsetneq \mathfrak{m} = (m)$$. Then since $$p \in \mathfrak{m} = (m)$$, we have $$p = rm$$ for some $$r\in A$$. From the assumption that $$\mathfrak{p}$$ is a prime ideal we have $$r\in \mathfrak{p}$$ or $$m\in\mathfrak{p}$$; but by the assumption $$\mathfrak{p} \subsetneq \mathfrak{m}$$ we must have $$m\not\in \mathfrak{p}$$. However, if $$r \in \mathfrak{p} = (p)$$, then $$r = ps$$ for some $$s\in A$$, and thus $$p = rm = psm$$, so $$1 = sm$$. Hence $$m$$ is a unit, which contradicts the assumption that $$\mathfrak{m}$$ is a maximal ideal. (By definition, $$A$$ itself is not a maximal ideal.)

</details>

## Unique Factorization Domains

Now we finally define unique factorization domains. To do so, let us first fix the terminology. 

<div class="definition" markdown="1">

<ins id="def11">**Definition 11**</ins> Let $$A$$ be an integral domain. 

1. Fix a nonzero, non-unit $$r\in A$$. If whenever $$r = ab$$ for some $$a, b$$, at least one of $$a$$ or $$b$$ is necessarily a unit, we call $$r$$ *irreducible*. Otherwise $$r$$ is called *reducible*.
2. Fix a nonzero, non-unit $$p \in A$$. If whenever $$p \mid ab$$ for some $$a, b$$, we always have $$p \mid a$$ or $$p \mid b$$, we call $$p$$ *prime*. 
3. For two elements $$a, b$$, if there exists a unit $$u$$ in $$A$$ such that $$a=ub$$, we say they are *associate in $$A$$*. 

</div>

For example, consider $$\mathbb{Z}$$. We would like to claim that any element of $$\mathbb{Z}$$, for instance $$10$$, can be uniquely factorized into the form $$2\times 5$$. However, because of the unit of $$\mathbb{Z}$$ other than $$1$$, namely $$-1$$, the equations

$$10=2\times 5=(-2)\times (-5)=(-1)^2\times 2\times 5=\cdots$$

allow us to express $$10$$ as products of this form, and we would like to regard these expressions as not genuinely different. This is why in the above definition we regard two elements differing by a unit as essentially the same. 

Meanwhile, the difference between irreducible and prime is somewhat subtle, and to properly define unique factorization domains we must clearly distinguish them. First, the following proposition is obvious. 

<div class="proposition" markdown="1">

<ins id="prop12">**Proposition 12**</ins> In an integral domain $$A$$, every prime element is irreducible.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Assume $$p \in A$$ is a prime element, and let $$p = ab$$ for some $$a, b$$. Then $$p\mid a$$ or $$p\mid b$$; without loss of generality assume $$p\mid a$$. That is, there exists $$r\in A$$ such that $$a=pr$$. Now from $$p=ab=prb$$ we have $$p(1-rb)=0$$; since $$A$$ is an integral domain and $$p$$ is nonzero, $$1-rb=0$$. Thus $$b$$ is a unit. 

</details>

However, the converse does not always hold. 

<div class="example" markdown="1">

<ins id="ex13">**Example 13**</ins> First, define the following norm on $$A=\mathbb{Z}[\sqrt{-5}]$$:

$$N(a + b\sqrt{-5}) := a^2 + 5b^2$$

Then we know that the equation

$$N(xy) = N(x)N(y)$$

holds for all $$x,y\in A$$. From this, if $$x$$ is a unit of $$A$$ then necessarily $$N(x)=1$$, and the converse also holds. 

Now consider the element $$3$$ of $$A$$. Then for $$xy=3$$ with $$x$$ and $$y$$ simultaneously non-units, we must have

$$N(x) N(y)=N(3) = 9$$

so $$N(x)=N(y)=3$$. However, by the definition of $$N$$ no element satisfies this, so $$3$$ is irreducible.

But $$3$$ is not prime. This is because

$$3 \mid (2 + \sqrt{-5})(2 - \sqrt{-5}) = 4 + 5 = 9$$

but $$3$$ divides neither $$2 + \sqrt{-5}$$ nor $$2 - \sqrt{-5}$$. 

</div>

However, in a PID this always holds. 

<div class="proposition" markdown="1">

<ins id="prop14">**Proposition 14**</ins> In a PID $$A$$, being irreducible and being prime are equivalent for a nonzero element. 

</div>
<details class="proof" markdown="1">
<summary>Proof</summary>

Fix an irreducible element $$p \in A$$. We must show that $$p$$ is prime, i.e., that $$(p)$$ is a prime ideal. Since $$A$$ is a P.I.D., any ideal can be written in the form $$(m)$$. Now if $$(p) \subseteq (m)$$, then $$p = rm$$ for some $$r \in A$$. But $$p$$ is irreducible, so one of $$r$$ or $$m$$ must be a unit.

- If $$r$$ is a unit, then $$p$$ and $$m$$ are associate, and $$(p) = (m)$$.
- If $$m$$ is a unit, then $$(m) = A$$.

Therefore the only ideals containing $$(p)$$ are $$(p)$$ itself and $$A$$, so $$(p)$$ is maximal; and in a P.I.D. every maximal ideal is prime, so $$(p)$$ is a prime ideal. Hence $$p$$ is a prime element.

</details>

Therefore $$A=\mathbb{Z}[\sqrt{-5}]$$ of [Example 13](#ex13) is not a PID.

<div class="example" markdown="1">

<ins id="ex15">**Example 15**</ins> Let us show using the definition that $$A=\mathbb{Z}[\sqrt{-5}]$$ is actually not a PID. Our claim is that the ideal

$$\mathfrak{a}=(3, 1+\sqrt{-5})$$

is non-principal. Let us continue using the norm defined in [Example 13](#ex13). Then 

$$N(3)=9,\qquad N(1+\sqrt{-5})=6$$

so if there existed $$x\in A$$ such that $$\mathfrak{a}=(x)$$, then $$N(x)$$ would have to be a divisor of $$3$$. However, as seen in [Example 13](#ex13), there is no $$x\in A$$ satisfying $$N(x)=3$$, so the only possibility is $$N(x)=1$$, and therefore $$(3, 1+\sqrt{-5})$$ would be the unit ideal. 

However, $$2\not\in \mathfrak{a}$$. To show this, suppose for some $$x, y \in A$$ that

$$2=3x+(1+\sqrt{-5})y$$

Writing $$x = a_1 + a_2\sqrt{-5}$$, $$y = b_1 + b_2\sqrt{-5}$$ and expanding the right-hand side,

$$3x + (1+\sqrt{-5})y = (3a_1 + b_1 - 5b_2) + (3a_2 + b_1 + b_2)\sqrt{-5}$$

For this to equal $$2$$ the following system of equations

$$\begin{cases}3a_1 + b_1 - 5b_2 = 2 \\3a_2 + b_1 + b_2 = 0\end{cases}$$

must hold. But substituting $$b_1 = -3a_2 - b_2$$ from the second equation into the first,

$$3a_1 - 3a_2 - 6b_2 = 2$$

we obtain an equation whose left-hand side is a multiple of $$3$$ while the right-hand side is not, a contradiction. Thus $$(3, 1+\sqrt{-5}) \neq (1)$$.

</div>

Now we define the following.

<div class="definition" markdown="1">

<ins id="def16">**Definition 16**</ins> An integral domain $$A$$ is called a *unique factorization domain* if the following two conditions hold for every non-zero, non-unit $$a\in A$$. 

1. $$a$$ can be expressed as a finite product of irreducible elements of $$A$$. That is, there exist irreducibles $$p_1, \dots, p_n \in A$$ such that
    
    $$a = p_1 p_2 \cdots p_n$$

2. The above expression is unique up to *associates*. That is, if $$a = q_1 q_2 \cdots q_m$$ is another such expression, then $$m = n$$ and after a suitable reordering each $$p_i$$ and $$q_i$$ are associate. 

</div>

Then the following holds. 

<div class="proposition" markdown="1">

<ins id="prop17">**Proposition 17**</ins> In a UFD $$A$$, being irreducible and being prime are equivalent for a nonzero element. 

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

It suffices to show that every irreducible element is prime.

Choose an irreducible element $$p \in A$$, and suppose $$p \mid ab$$ for some $$a, b \in A$$. We must show that $$p \mid a$$ or $$p \mid b$$. Since $$A$$ is a UFD, we can write $$a$$, $$b$$, and $$ab$$ as products of irreducibles. Write

$$a = p_1 \cdots p_k,\quad b = q_1 \cdots q_l$$

then $$ab = p_1 \cdots p_k q_1 \cdots q_l$$. Here $$p \mid ab$$ means there exists $$c \in A$$ such that $$ab = pc$$. Now $$p$$ is also irreducible and $$ab$$ is expressed as a product of irreducibles, so by the definition of a UFD, $$p$$ is associate to one of the factors $$p_i$$ or $$q_j$$ of $$ab$$, and accordingly $$p$$ divides $$a$$ or $$b$$. 

</details>

A UFD is, by its definition, an integral domain in which every element can be factored. The advantage of prime factorizations of two integers is that their greatest common divisor can be read off immediately. 

<div class="proposition" markdown="1">

<ins id="prop18">**Proposition 18**</ins> Let $$A$$ be a unique factorization domain. Suppose $$a, b \in A$$ are nonzero elements with the following prime factorizations:

$$a = u \cdot p_1^{e_1} p_2^{e_2} \cdots p_n^{e_n}, \qquad b = v \cdot p_1^{f_1} p_2^{f_2} \cdots p_n^{f_n}$$

where $$u, v \in A^\times$$ are units, $$p_1, \dots, p_n$$ are distinct irreducibles (or primes), and $$e_i, f_i \geq 0$$. Then the element defined by

$$d = p_1^{\min(e_1, f_1)} p_2^{\min(e_2, f_2)} \cdots p_n^{\min(e_n, f_n)}$$

is a greatest common divisor of $$a$$ and $$b$$. (If all exponents are $$0$$, then $$d = 1$$.)

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

First, since the exponent $$\min(e_i, f_i)$$ of each prime factor $$p_i$$ of $$d$$ is the minimum number of times $$p_i$$ appears in the factorizations of both $$a$$ and $$b$$, it is immediate that $$d \mid a$$ and $$d \mid b$$. That is, $$d$$ is a common divisor.

Now let $$c$$ be an arbitrary common divisor of $$a$$ and $$b$$. Then the prime factorization of $$c$$ is

$$c = q_1^{g_1} \cdots q_m^{g_m}$$

Since $$c \mid a, b$$, each $$q_j$$ must be associate to some prime factor of $$a$$ or $$b$$. That is, $$\{q_1, \dots, q_m\} \subseteq \{p_1, \dots, p_n\}$$.

Moreover, each exponent $$g_j$$ cannot exceed the exponent of $$q_j$$ in $$a$$ and $$b$$, so $$g_j \leq \min(e_j, f_j)$$. Therefore $$c \mid d$$, and $$d$$ is a greatest common divisor of $$a$$ and $$b$$.

</details>

Then the following theorem ties together the three definitions we have covered so far. 

<div class="proposition" markdown="1">

<ins id="thm19">**Theorem 19**</ins> Every Euclidean domain is a principal ideal domain, and every principal ideal domain is a unique factorization domain. In particular, every Euclidean domain is a unique factorization domain.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

We need only show that every PID is a UFD. Fix a PID $$A$$ and a non-zero, non-unit $$r\in A$$. First, we will inductively construct a chain of ideals

$$(r)=(r_0) \subsetneq (r_1) \subsetneq (r_2) \subsetneq \cdots$$

If $$r$$ is irreducible we end the process here; otherwise there exist non-units $$r_1, r_2$$ such that $$r = r_1 r_2$$. If both of these are again irreducible we terminate the process here; otherwise we obtain the above chain of ideals by repeating this process. 

Now set $$\mathfrak{a}=\bigcup_{i=0}^\infty (r_i)$$. That $$\mathfrak{a}$$ is an ideal is obvious, and by the assumption that $$A$$ is a PID there exists $$a\in A$$ such that $$\mathfrak{a}=(a)$$. Then for some $$n$$ we must have $$a\in (r_n)$$, and then from this $$n$$ onwards $$(r_n)$$ always contains $$a$$, contradicting $$(r_n)\subsetneq (r_{n+1})$$. 

For uniqueness, in a manner similar to [Proposition 18](#prop18), assume two expressions

$$r = p_1 \cdots p_m = q_1 \cdots q_n$$

are given, and find the $$q_j$$'s associate to the $$p_i$$'s in order.

</details>
