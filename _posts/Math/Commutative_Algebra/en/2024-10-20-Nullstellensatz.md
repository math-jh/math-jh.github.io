---
title: "The Nullstellensatz"
description: "Reviews the definitions of Jacobson rings and radical ideals, and covers the process of proving the Nullstellensatz using the Rabinowitsch lemma."
excerpt: "Jacobson rings and the proof of the Hilbert Nullstellensatz"

categories: [Math / Commutative Algebra]
permalink: /en/math/commutative_algebra/nullstellensatz
sidebar: 
    nav: "commutative_algebra-en"

date: 2024-10-20
weight: 10
translated_at: 2026-08-27T20:45:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-10-04T23:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Jacobson Rings

We have seen that for a ring $A$ and an arbitrary ideal $\mathfrak{a}$, the formula

$$\sqrt{\mathfrak{a}}=\bigcap_\text{\scriptsize$\mathfrak{p}$ prime containing $\mathfrak{a}$} \mathfrak{p}$$

holds. ([§Properties of Localization, ⁋Corollary 8](/en/math/commutative_algebra/properties_of_localization#cor8){: data-lid="k67s8" }) In particular, if $\mathfrak{a}$ is a prime ideal, then $\mathfrak{p}=\sqrt{\mathfrak{p}}$ should naturally hold. More generally, we define the following.

::: Definition 1
For a ring $A$, an arbitrary ideal $\mathfrak{a}$ is called a *radical ideal* if $\mathfrak{a}=\sqrt{\mathfrak{a}}$ holds.
:::

Therefore, in short, the observation above says that every prime ideal is radical. The proof of this observation is more or less trivial; however, had we considered, instead of the intersection of the prime ideals containing $\mathfrak{p}$, the intersection of the *maximal* ideals containing $\mathfrak{p}$ in a manner similar to [§Integral Extensions, §§Nakayama's Lemma](/en/math/commutative_algebra/integral_extension#nakayamas-lemma){: data-lid="y59z8" }, this observation would not have been so trivial, and in fact it does not even hold. For instance, any local ring containing a prime ideal that is not maximal, such as $\mathbb{Z}_{(2)}$, gives a counterexample.

::: Definition 2
A ring $A$ is called a *Jacobson ring* if every prime ideal is an intersection of maximal ideals.
:::

The following then holds.

::: Lemma 3 (Rabinowitch)
For a ring $A$, the following are equivalent.

1. $A$ is a Jacobson ring.
2. For a prime ideal of $A$, $\mathfrak{p}$, if $(A/\mathfrak{p})[a^{-1}]$ is a field for some $a\in A/\mathfrak{p}$, then $A/\mathfrak{p}$ is a field.
:::
::: Proof
First, suppose that $A$ is Jacobson. Then it is also clear by definition that its quotient $A/ \mathfrak{p}$ is Jacobson. Meanwhile, by [\[Algebraic Structures\] §Field of Fractions, ⁋Proposition 9](/en/math/algebraic_structures/field_of_fractions#prop9){: data-lid="ae64m" }, $A/\mathfrak{p}$ is an integral domain, and since $(0)$ is a prime ideal in an integral domain, we can express $(0)$ as an intersection of maximal ideals. Now, by [§Localization, ⁋Proposition 8](/en/math/commutative_algebra/localization#prop8){: data-lid="lk9az" }, there is a one-to-one correspondence between the prime ideals of $(A/\mathfrak{p})[a^{-1}]$ and the prime ideals of $A/\mathfrak{p}$ not containing $a$; since by assumption the only prime ideal of $(A/\mathfrak{p})[a^{-1}]$ is $0$, the only prime ideal of $A/\mathfrak{p}$ not containing $a$ is also $0$. In other words, every nonzero prime ideal of $A/\mathfrak{p}$ must always contain $a$. But if such a prime ideal exists, then $(0)$ is not a maximal ideal, so every maximal ideal of $A/\mathfrak{p}$ is nonzero and therefore contains $a$. Meanwhile,

$$(0)=\bigcap_\text{\scriptsize$\mathfrak{m}$ maximal} \mathfrak{m}$$

and hence $a=0$, a contradiction.

Conversely, let us assume the second condition and prove the first. That is, we fix a prime ideal of $A$, $\mathfrak{p}$, and letting the intersection of all maximal ideals containing $\mathfrak{p}$ be $\mathfrak{P}$, we must show that $\mathfrak{p}=\mathfrak{P}$. Suppose, contrary to the conclusion, that there exists an element $a\in \mathfrak{P}\setminus \mathfrak{p}$. Then by [\[Set Theory\] §Axiom of Choice, ⁋Theorem 4](/en/math/set_theory/axiom_of_choice#thm4){: data-lid="4m2q3" }, among the prime ideals containing $\mathfrak{p}$ but not containing $a$, there exists a maximal prime ideal $\mathfrak{q}$. Since $a\not\in \mathfrak{q}$ by definition, $\mathfrak{q}$ is not a maximal ideal, and therefore $A/\mathfrak{q}$ is not a field. However, in $A[a^{-1}]$, $\mathfrak{q}$ must be a maximal ideal by definition, which contradicts the second condition; hence we must have $\mathfrak{p}=\mathfrak{P}$.
:::

## The Nullstellensatz

Now the Nullstellensatz can be stated as follows.

::: Theorem 4
Let a Jacobson ring $A$ and a finitely generated $A$-algebra $E$ be given. Then $E$ is also a Jacobson ring. Moreover, if $\mathfrak{n}$ is a maximal ideal of $E$, then $\mathfrak{m}=\mathfrak{n}\cap A$ is a maximal ideal of $A$, and $E/\mathfrak{n}$ is a finite field extension of $A/\mathfrak{m}$.
:::
::: Proof
We divide the proof into three steps.

1. First, consider the case where $A=\mathbb{K}$ and $E=\mathbb{K}[\x]$. Then $E$ is a principal ideal domain; in particular, every nonzero prime ideal of $E$ is generated by an irreducible monic polynomial. From this, since no nonzero prime ideal can be contained in another prime ideal, every nonzero prime ideal of $E$ is maximal; such an ideal cannot contain $1\in \mathbb{K}$, so its intersection with $A=\mathbb{K}$ must be $(0)$. In this case, $E/\mathfrak{n}$, whose dimension equals the degree of the irreducible polynomial defining $\mathfrak{n}$, is a $\mathbb{K}$-vector space. Finally, to show that $(0)$ is the intersection of maximal ideals, it suffices to use the argument that $E=\mathbb{K}[\x]$ has infinitely many irreducible polynomials, and since the degree of a polynomial is necessarily finite, the only polynomial having all of them as factors is $0$. Here, the infinitude of irreducible polynomials in $E$ follows by directly mimicking Euclid's proof of the infinitude of primes.
2. For the next step, consider an arbitrary Jacobson ring $A$ and an $A$-algebra $E$ generated by a single element; to show that $E$ is Jacobson, we verify that the second condition of [Lemma 3](#lem3){: data-lid="21aht" } holds. In other words, our goal in this step is to prove the following proposition.
    > Let a Jacobson ring $A$ be given, and let an $A$-algebra $E$ generated by a single element be given. If, for a fixed prime ideal $\mathfrak{q}\subseteq E$, $E/\mathfrak{q}$ contains a nonzero $x\in E/\mathfrak{q}$ such that $(E/\mathfrak{q})[x^{-1}]$ is a field, then $E/\mathfrak{q}$ is also a field.

    Since $E'=E/\mathfrak{q}$ is again an $A$-algebra generated by a single element, the proposition above amounts to showing the following.
    > Let a Jacobson ring $A$ be given, and suppose that an $A$-algebra $E'$ generated by a single element is an integral domain. If $E'$ contains a nonzero $x\in E'$ such that $E'[x^{-1}]$ is a field, then $E'$ is also a field.

    In taking this quotient, $A$ is replaced by $A'=A/(A\cap \mathfrak{q})$, which is again a Jacobson ring; consequently, what we must ultimately show is the following proposition.
    > Suppose that an integral domain $A'$ is Jacobson, and that an $A'$-algebra $E'$ generated by a single element is an integral domain containing $A'$. If $E'$ contains a nonzero $x\in E'$ such that $E'[x^{-1}]$ is a field, then $E'$ is also a field.

    To this end, we show that under the above assumptions $A'$ must be a field, and $E'$ is a finite extension of $A'$. Since in the above proposition $E'$ is an $A'$-algebra generated by a single element, we may write $E'=A'[\x]/\mathfrak{q}$. We first show that $\mathfrak{q}\neq 0$. Suppose for contradiction that $\mathfrak{q}=0$, and assume that there exists some $x\in E'/(0)=A'[\x]$ such that $E'[x^{-1}]=A'[\x][x^{-1}]$ is a field. Letting $K'=\Frac(A')$, this assumption implies that $K'[\x][x^{-1}]$ is also a field. But $K'[\x]$ is Jacobson by the first result, so $K'[\x]$ must be a field, which is a contradiction. Therefore $\mathfrak{q}\neq 0$, and $E'[x^{-1}]=K'[\x]/\mathfrak{q}K'[\x]$ is a finite-dimensional extension of $K'$.  
    Now suppose that $p(\x)\in \mathfrak{q}$ satisfies in $E'$ the equation

    $$p(\alpha)=p_n\alpha^n+\cdots+p_0=0$$

    where $\alpha$ is the generator of $E'$ as an $A'$-algebra. Then from the above equation, $E'[p_n^{-1}]$ is an integral $A'[p_n^{-1}]$-algebra. Meanwhile, the element $x$ defined above must also satisfy some polynomial

    $$q(x)=q_mx^m+\cdots+q_0=0$$

    and since $E'$ is an integral domain, we may assume without loss of generality that $q_0\neq 0$. Then from the monic polynomial

    $$\left(\frac{1}{x}\right)^m+\frac{q_1}{q_0}\left(\frac{1}{x}\right)^{m-1}+\cdots+\frac{q_m}{q_0}=0$$

    we see that $E'[x^{-1}]$ is an integral $A'[(p_nq_0)^{-1}]$-algebra. Now by [§Integral Extensions and Ideals, ⁋Corollary 3](/en/math/commutative_algebra/lying_over_and_going_up#cor3){: data-lid="5mzqr" }, $A'[(p_nq_0)^{-1}]$ is a field, and since $A'$ is Jacobson by assumption, [Lemma 3](#lem3){: data-lid="ngsed" } implies that $A'$ is a field. Therefore $E'$ is an integral $A'$-algebra, and again by [§Integral Extensions and Ideals, ⁋Corollary 3](/en/math/commutative_algebra/lying_over_and_going_up#cor3){: data-lid="s8x58" } we see that $E'$ is a field. 
3. The general case follows by induction on the number of generators using the second result. 
:::

In particular, consider the case where $A=\mathbb{K}$ and $E=\mathbb{K}[\x_1,\ldots, \x_n]$. Then, for any 

$$a=(a_1,\ldots, a_n)\in \mathbb{K}^n$$

if we define the ideal $\mathfrak{m}_a$ by the equation

$$\mathfrak{m}_a=(\x_1-a_1,\ldots, \x_n-a_n)$$

the isomorphism given by evaluation

$$\ev_a:\mathbb{K}[\x_1,\ldots, \x_n]/\mathfrak{m}_a\rightarrow \mathbb{K}$$

shows that $\mathfrak{m}_a$ is a maximal ideal. 

Moreover, if $\mathbb{K}$ is an algebraically closed field, then every maximal ideal of $E$ is of this form. First, for any maximal ideal of $E$, say $\mathfrak{n}$, $E/\mathfrak{n}$ is an algebraic extension of $\mathbb{K}/(\mathfrak{n}\cap \mathbb{K})=\mathbb{K}$; but if $\mathbb{K}$ is algebraically closed, the only such extension is itself, so we must have $E/\mathfrak{n}\cong \mathbb{K}$. Meanwhile, under the canonical surjection $E \rightarrow E/\mathfrak{n}\cong \mathbb{K}$, if we let the image of each $\x_i$ in $\mathbb{K}$ be $a_i$, then $\mathfrak{m}_a\subseteq \mathfrak{n}$, and now from the maximality of $\mathfrak{m}_a$ we obtain the desired result. 

Therefore, from [§Basic Notions, ⁋Proposition 11](/en/math/commutative_algebra/basic_notions#prop11){: data-lid="47akg" }, we obtain the following.

::: Lemma 5
Let a field $\mathbb{K}$ be given. Then $\mathfrak{m}_a=(\x_1-a_1,\ldots, \x_n-a_n)$ is a maximal ideal of $\mathbb{K}[\x_1,\ldots, \x_n]$. Moreover, if $\mathbb{K}$ is algebraically closed, then between the maximal ideals of $\mathbb{K}[\x_1,\ldots,\x_n]/(f_1,\ldots, f_r)$ and, satisfying the equation

$$f_1(x_1,\ldots, x_n)=\cdots=f_r(x_1,\ldots, x_n)=0$$

the $(x_1,\ldots, x_n)$, there is a one-to-one correspondence.
:::

A somewhat more traditional version of the Nullstellensatz is also obtained from this. To state it, consider the function that takes an ideal of $\mathbb{K}[\x_1,\ldots, \x_n]$, $\mathfrak{a}$, and yields the subset of $\mathbb{K}^n$, $Z(\mathfrak{a})$,

$$Z(\mathfrak{a})=\{(a_1,\ldots, a_n)\in \mathbb{K}^n\mid \text{$f(a_1,\ldots, a_n)=0$ for all $f\in \mathfrak{a}$}\}$$

and the function that takes a subset of $\mathbb{K}^n$, $S$, and yields the subset of $\mathbb{K}[\x_1,\ldots, \x_n]$

$$I(S)=\{f\in \mathbb{K}[\x_1,\ldots, \x_n]\mid\text{$f(a_1,\ldots, a_n)=0$ for all $(a_1,\ldots, a_n)\in S$}\}$$

This is the function $I$.

::: Proposition 6
Let an algebraically closed field $\mathbb{K}$ and an ideal $\mathfrak{a}\subseteq \mathbb{K}[\x_1,\ldots, \x_n]$ be given. Then 

$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$$

holds.
:::
::: Proof
From [Lemma 5](#lem5){: data-lid="bh482" }, we know that the elements of $Z(\mathfrak{a})$ are in one-to-one correspondence with the maximal ideals of $\mathbb{K}[\x_1,\ldots, \x_n]$ containing $\mathfrak{a}$. Hence $I(Z(\mathfrak{a}))$ is the intersection of the maximal ideals containing $\mathfrak{a}$ in $\mathbb{K}[\x_1,\ldots, \x_n]$, and since $\mathbb{K}[\x_1,\ldots, \x_n]$ is Jacobson by [Theorem 4](#thm4){: data-lid="inxml" }, this equals the intersection of the prime ideals containing $\mathfrak{a}$ in $\mathbb{K}[\x_1,\ldots, \x_n]$, which is precisely the right-hand side.
:::

---

**References**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---
