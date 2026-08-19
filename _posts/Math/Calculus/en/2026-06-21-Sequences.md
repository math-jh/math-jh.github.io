---
title: "Limits of Sequences"
description: "We define convergence of sequences using the epsilon-N definition and present boundedness, limit laws, the squeeze theorem, and the ratio test. Standard limits, the natural constant e, the monotone convergence theorem, and subsequences are also covered."
excerpt: "Convergence, limit laws, standard limits, e, and monotone convergence"

categories: [Math / Calculus]
permalink: /en/math/calculus/sequences
sidebar: 
    nav: "calculus-en"

date: 2026-06-21
weight: 3
translated_at: 2026-08-19T05:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T05:15:05+00:00
---
Before we begin calculus proper, we first define the limit of a sequence. Here a *sequence* $(a_n)$ is a function from the natural numbers to the real numbers, i.e., $a : \mathbb{N} \rightarrow \mathbb{R}$, viewed as the list of its values $a_1, a_2, a_3, \ldots$. In [§Limits of Functions](/en/math/calculus/functions_and_limits) we already studied how a function behaves as $x \rightarrow \infty$; the limit of a sequence can be thought of as the discrete version of this, where the variable is restricted to the natural numbers and only tends to $n \rightarrow \infty$.

## Convergence of Sequences

::: Definition 1
For a real sequence $(a_n)_{n=1}^\infty$ and a real number $L$, if for every $\epsilon > 0$ there exists a natural number $N$ such that

$$n > N \implies \lvert a_n - L \rvert < \epsilon$$

then we call $L$ the *limit* of $a_n$ as $n \rightarrow \infty$, and write $\lim_{n\rightarrow\infty} a_n = L$.
:::

This definition is taken almost verbatim from [§Limits of Functions, ⁋Definition 14](/en/math/calculus/functions_and_limits#def14). Since a sequence has only natural numbers as its variable and tends in only one direction ($+\infty$), there is essentially only one way to define its limit. For instance, $a_n = 1/n \rightarrow 0$ is verified by choosing, for any $\epsilon > 0$, an $N > 1/\epsilon$; then for $n > N$ we have $1/n < 1/N < \epsilon$. A slight variant is a sequence diverging to infinity, which is obtained by translating [§Limits of Functions, ⁋Definition 13](/en/math/calculus/functions_and_limits#def13): for every $M$ there exists $N$ such that $n > N \implies a_n > M$; for example, $b_n = n$ behaves this way. However, there also exist sequences that neither converge nor diverge to infinity ([Example 11](#ex11)).

The basic properties of convergent sequences are mostly obtained by translating proofs from the function limit case directly. For example, the following proposition can be proved in exactly the same way as [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5).

::: Proposition 2 (Limit laws for sequences)
Suppose two sequences $a_n$, $b_n$ converge, with limits

$$\lim_{n\rightarrow\infty} a_n = L, \qquad \lim_{n\rightarrow\infty} b_n = M$$

Then

1. $\lim (a_n + b_n) = L + M$,
2. for any constant $c$, $\lim c a_n = cL$,
3. $\lim a_n b_n = LM$,
4. if $M \neq 0$ and $b_n \neq 0$ for all $n$, then $\lim a_n/b_n = L/M$.
:::

## Properties of Limits

A sequence $(a_n)$ is called *bounded* if there exists a positive number $M$ such that $\lvert a_n\rvert \leq M$ for all $n$. A convergent sequence must be bounded, because all but finitely many of its terms gather near the limit point.

::: Proposition 3
Every convergent sequence is bounded.
:::

::: Proof
If $a_n \rightarrow L$, then for $\epsilon = 1$ there is a corresponding $N$, and for $n > N$ we have $\lvert a_n\rvert \leq \lvert L\rvert + 1$. Taking $M = \max\{\lvert a_1\rvert, \ldots, \lvert a_N\rvert, \lvert L\rvert + 1\}$ then gives $\lvert a_n\rvert \leq M$ for all $n$.
:::

By the same copy-and-translate method, the following is the sequence version of [§Limits of Functions, ⁋Proposition 8](/en/math/calculus/functions_and_limits#prop8).

::: Proposition 4 (Squeeze theorem)
If $a_n \leq c_n \leq b_n$ for all sufficiently large $n$, and $a_n \rightarrow L$, $b_n \rightarrow L$, then $c_n \rightarrow L$.
:::

From this we obtain the following simple but useful result.

::: Proposition 5 (Ratio test)
Let $(a_n)$ be a real sequence with $a_n > 0$ for all $n$. If the sequence of ratios $a_{n+1}/a_n$ converges to a value $L < 1$, then $a_n \rightarrow 0$.
:::

::: Proof
Choose $r$ with $L < r < 1$. Then for all sufficiently large $n \geq N$ we have $a_{n+1}/a_n < r$, so $a_{N+k} < r^k a_N$. Since $0 < r < 1$, we have $r^k \rightarrow 0$ by part 3 of [Example 6](#ex6), and the squeeze theorem gives $a_n \rightarrow 0$.
:::

Similarly, we collect in the next example several results that are frequently used in actual calculations.

::: Example 6
The following are basic examples of sequence limits.

1. For $p > 0$, we have $1/n^p \rightarrow 0$. If $p \geq 1$, then $n^p \geq n$ for $n \geq 1$, so $0 < 1/n^p \leq 1/n \rightarrow 0$, and [Proposition 4](#prop4) applies. If $0 < p < 1$, choose $N > \epsilon^{-1/p}$ for any $\epsilon > 0$; then for $n > N$ we have $n^p > 1/\epsilon$, i.e., $1/n^p < \epsilon$, which follows directly from [Definition 1](#def1).
2. More generally, the ratio of two polynomials of the same degree is determined by the ratio of their leading coefficients.

   $$\frac{a_k n^k + \cdots}{b_k n^k + \cdots}$$

   Dividing numerator and denominator by $n^k$ yields expressions consisting of finitely many terms of the form $1/n^j$ plus a constant. Since $1/n^j \rightarrow 0$, the numerator and denominator each converge to their leading coefficients. If the denominator has larger degree than the numerator, then by [Proposition 4](#prop4) and part 1 above this ratio converges to $0$; similarly, if the numerator has larger degree than the denominator, the ratio diverges.
3. If $\lvert r\rvert < 1$, then $r^n \rightarrow 0$. To verify this, the case $r=0$ is trivial since the sequence is identically $0$, so assume $r \neq 0$ and write $\lvert r\rvert = 1/(1+h)$ for some suitable $h>0$. Then by the binomial theorem $(1+h)^n \geq 1 + nh$, and therefore

    $$\lvert r\rvert^n = \frac{1}{(1+h)^n} \leq \frac{1}{1+nh} \rightarrow 0$$

    Here the final convergence uses the result of part 2 above. If $r=1$, the sequence is constantly $1$, so it trivially converges to $1$; if $\lvert r\rvert > 1$, then similarly writing $\lvert r\rvert=1+h$ gives

    $$\lvert r\rvert^n =(1+h)^n \geq 1+nh$$

    so no matter what $M$ we pick, making $n$ sufficiently large makes $\lvert r\rvert^n$ exceed $M$; hence $\lvert r\rvert^n$ diverges.
4. $n^{1/n} \rightarrow 1$. To verify this, set $n^{1/n} = 1 + h_n$ ($h_n \geq 0$). Then by the binomial theorem

   $$n = (1+h_n)^n \geq \binom{n}{2}h_n^2 = \frac{n(n-1)}{2}h_n^2$$

   so for $n \geq 2$ we have $h_n^2 \leq 2/(n-1) \rightarrow 0$, i.e., $h_n \rightarrow 0$.
5. For $r > 1$, $p > 0$, we have $n^p/r^n \rightarrow 0$. This follows immediately from [Proposition 5](#prop5), since the ratio of consecutive terms is

    $$\frac{(n+1)^p}{r^{n+1}}\cdot\frac{r^n}{n^p} = \frac{1}{r}\left(1+\frac{1}{n}\right)^p \rightarrow \frac{1}{r} < 1$$
6. Similarly, for $r > 1$ the ratio of consecutive terms of the sequence $r^n/n!$ is $r/(n+1) \rightarrow 0 < 1$, so for the same reason the limit is $0$.
:::

## Monotone Convergence Theorem

On the other hand, the proof of the following proposition requires knowledge of analysis, so it is impossible for us to prove it at present; nevertheless, the result itself is useful, so we accept it in advance.

::: Proposition 7 (Monotone convergence)
An increasing sequence bounded above and a decreasing sequence bounded below both converge. (The limit of an increasing sequence is the supremum of its terms.)
:::

The most useful application of this is the proof of the existence of the following *natural constant*.

::: Example 8 (The natural constant $e$)
The sequence $a_n = (1 + 1/n)^n$ is increasing and bounded above, hence converges by [Proposition 7](#prop7).

First we show that this sequence is increasing. Applying the arithmetic–geometric mean inequality to $n$ copies of $1+1/n$ and one copy of $1$, the arithmetic mean is

$$\frac{n(1+1/n)+1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

and the geometric mean is $((1+1/n)^n\cdot 1)^{1/(n+1)}=a_n^{1/(n+1)}$, so we obtain

$$a_n \leq \left(1+\frac{1}{n+1}\right)^{n+1} = a_{n+1}$$

Moreover, since the $n+1$ numbers are not all equal, the equality condition fails and we obtain the strict inequality $a_n < a_{n+1}$.

Now to show that this sequence is bounded above, observe by the binomial theorem that

$$a_n = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}$$

Each term satisfies

$$\binom{n}{k}\frac{1}{n^k} = \frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k} \leq \frac{1}{k!}$$

and since $k! \geq 2^{k-1}$ ($k \geq 1$), we have

$$a_n \leq \sum_{k=0}^{n}\frac{1}{k!} \leq 1 + \sum_{k=1}^{n}\frac{1}{2^{k-1}} = 3 - \frac{1}{2^{n-1}} < 3$$

We define the limit of this sequence to be the *natural constant* $e = 2.718\ldots$.
:::

## Subsequences

Meanwhile, in analyzing whether a sequence converges, it is useful to consider a new sequence formed by selecting only some of its terms.

::: Definition 9
Given a sequence $(a_n)$ and a strictly increasing sequence of natural numbers $n_1 < n_2 < n_3 < \cdots$, the new sequence $(a_{n_k})_{k\geq 1}$ is called a *subsequence* of $(a_n)$.
:::

That is, it is obtained from the sequence $a_n$ by *skipping* terms while preserving the order of indices. It is intuitively clear that if the original sequence converges to some value, then every subsequence also converges to the same value.

::: Proposition 10
If a sequence $a_n$ converges to $L$, then every subsequence $(a_{n_k})$ also converges to $L$.
:::

::: Proof
For any $\epsilon > 0$, choose $N$ such that $n \geq N$ implies $\lvert a_n - L\rvert < \epsilon$. Then by definition $n_k \geq k$, so if $k \geq N$ we have $n_k \geq N$ and therefore

$$\lvert a_{n_k} - L\rvert < \epsilon$$

Thus $a_{n_k} \rightarrow L$.
:::

This proposition is more useful for showing that a sequence does *not* converge than for showing that it does. By contrapositive, if there exist subsequences with two different limits, then the original sequence $(a_n)$ does not converge.

::: Example 11 (A divergent sequence)
Consider the sequence $a_n = (-1)^n$. The even subsequence $a_{2k} = 1 \rightarrow 1$ and the odd subsequence $a_{2k-1} = -1 \rightarrow -1$ have different limits, so by [Proposition 10](#prop10) the sequence $(a_n)$ diverges.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
