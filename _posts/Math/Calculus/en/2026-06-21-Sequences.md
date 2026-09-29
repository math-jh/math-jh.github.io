---
title: "Limits of Sequences"
description: "We define convergence of sequences using the epsilon-N definition and present boundedness, limit laws, the squeeze theorem, and the ratio test. Standard limits, the natural constant e, the monotone convergence theorem, and subsequences are covered."
excerpt: "Convergence of sequences, limit laws, standard limits and e, monotone convergence"

categories: [Math / Calculus]
permalink: /en/math/calculus/sequences
sidebar: 
    nav: "calculus-en"

date: 2026-06-21
weight: 3
translated_at: 2026-08-19T05:15:05+00:00
translation_source: kimi-cli
last_polished_at: 2026-09-29T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Before we begin calculus proper, we first define the limit of a sequence. Here a *sequence* $(a_n)$ is a function associating real numbers with natural numbers, that is, $a : \mathbb{N} \rightarrow \mathbb{R}$, viewed as the listing of its values $a_1, a_2, a_3, \ldots$. In [§Limits of Functions](/en/math/calculus/functions_and_limits){: data-lid="wfvsa" }, we already addressed how a function behaves when $x \rightarrow \infty$; the limit of a sequence can be thought of as its discrete version, that is, the case where the variable takes only natural numbers and only goes to $n \rightarrow \infty$.

## Convergence of Sequences

::: Definition 1
For a sequence of real numbers $(a_n)_{n=1}^\infty$ and a real number $L$, if for any $\epsilon > 0$ there exists a natural number $N$ such that

$$n > N \implies \lvert a_n - L \rvert < \epsilon$$

holds, then $L$ is called the *limit* of $a_n$ as $n \rightarrow \infty$, and we write $\lim_{n\rightarrow\infty} a_n = L$.
:::

This definition is taken almost verbatim from [§Limits of Functions, ⁋Definition 14](/en/math/calculus/functions_and_limits#def14){: data-lid="dcvlc" }; since a sequence has only natural numbers as its variable and goes in only one direction ($+\infty$), this is essentially the only way to define the limit. For instance, $a_n = 1/n \rightarrow 0$ is verified by noting that if for any $\epsilon > 0$ we choose, with $N > 1/\epsilon$, an $N$, then for $n > N$ we have $1/n < 1/N < \epsilon$. A slight variant is a sequence diverging to infinity, which can be adapted from [§Limits of Functions, ⁋Definition 13](/en/math/calculus/functions_and_limits#def13){: data-lid="tk37e" } as: for any $M$, there exists, such that $n > N \implies a_n > M$, an $N$; for example, $b_n = n$ is such a sequence. However, there also exist sequences that neither converge nor diverge to infinity ([Example 11](#ex11){: data-lid="9lhgt" }).

The basic properties of convergent sequences are mostly obtained by directly transferring the proofs from limits of functions. For example, for the following proposition, it suffices to proceed in the same manner as the proof of [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="b9w9q" }.

::: Proposition 2 (Limit laws for sequences)
Suppose two sequences $a_n$, $b_n$ converge, and let their limits be

$$\lim_{n\rightarrow\infty} a_n = L, \qquad \lim_{n\rightarrow\infty} b_n = M$$

Then

1. $\lim (a_n + b_n) = L + M$,
2. for any constant $c$, $\lim c a_n = cL$,
3. $\lim a_n b_n = LM$,
4. if $M \neq 0$ and for all $n$, $b_n \neq 0$, then $\lim a_n/b_n = L/M$

hold.
:::

## Properties of Limits

For a sequence $(a_n)$, if for all $n$ we have $\lvert a_n\rvert \leq M$ for some positive number $M$, then $(a_n)$ is called *bounded*. A convergent sequence is bounded because, except for the first finitely many terms, it always gathers near the point of convergence.

::: Proposition 3
A convergent sequence is bounded.
:::

::: Proof
If $a_n \rightarrow L$, then taking for $\epsilon = 1$ a corresponding $N$, we have for $n > N$ that $\lvert a_n\rvert \leq \lvert L\rvert + 1$. Including the remaining finitely many terms, if we set $M = \max\{\lvert a_1\rvert, \ldots, \lvert a_N\rvert, \lvert L\rvert + 1\}$, then for all $n$ we have $\lvert a_n\rvert \leq M$.
:::

By copying over in the same manner, the following is the sequence version of [§Limits of Functions, ⁋Proposition 8](/en/math/calculus/functions_and_limits#prop8){: data-lid="ocpzi" }.

::: Proposition 4 (Squeeze theorem)
If for all sufficiently large $n$ we have $a_n \leq c_n \leq b_n$, and $a_n \rightarrow L$, $b_n \rightarrow L$, then $c_n \rightarrow L$.
:::

Then we obtain the following simple but useful result.

::: Proposition 5 (Ratio test)
If a real sequence $a_n$ satisfies, for all $n$, that $a_n > 0$, and the sequence of ratios of adjacent terms $a_{n+1}/a_n$ converges to a value less than $1$, namely $L$, then $a_n \rightarrow 0$.
:::

::: Proof
Choosing a number satisfying $L < r < 1$, say $r$, for sufficiently large $n \geq N$ we have $a_{n+1}/a_n < r$, so $a_{N+k} < r^k a_N$. Since $0 < r < 1$, by part 3 of [Example 6](#ex6){: data-lid="c775e" } we have $r^k \rightarrow 0$, and by the squeeze theorem $a_n \rightarrow 0$.
:::

Similarly, we collect in the following example results that are frequently used in actual calculations.

::: Example 6
The following are basic examples of sequence limits.

1. For $p > 0$, $1/n^p \rightarrow 0$ holds. This is because in the case $p \geq 1$, since for $n \geq 1$ we have $n^p \geq n$, it follows that $0 < 1/n^p \leq 1/n \rightarrow 0$, and thus it suffices to apply [Proposition 4](#prop4){: data-lid="69e6c" }. In the case $0 < p < 1$, if for any $\epsilon > 0$ we choose a number satisfying $N > \epsilon^{-1/p}$, namely $N$, then for $n > N$ we have $n^p > 1/\epsilon$, that is, $1/n^p < \epsilon$, which is obtained directly from [Definition 1](#def1){: data-lid="6m9ua" }.
2. More generally, the ratio of polynomials of the same degree is determined by the ratio of their leading terms.

   $$\frac{a_k n^k + \cdots}{b_k n^k + \cdots}$$

   Dividing the numerator and denominator by $n^k$, both the numerator and denominator consist of finitely many $1/n^j$ terms and a constant term. Then, since $1/n^j \rightarrow 0$, we see that the numerator and denominator each converge to their leading coefficients. If the denominator has a higher degree than the numerator, then by [Proposition 4](#prop4){: data-lid="85hro" } and part 1 above we see that this ratio converges to $0$; similarly, if the numerator has a higher degree than the denominator, we see that this ratio diverges.
3. If $\lvert r\rvert < 1$, then $r^n \rightarrow 0$. To verify this, the case $r=0$ is trivial since the sequence is identically $0$, so suppose $r \neq 0$, and for some suitable $h>0$, let $\lvert r\rvert = 1/(1+h)$. Then using the binomial theorem, $(1+h)^n \geq 1 + nh$, and therefore
    
    $$\lvert r\rvert^n = \frac{1}{(1+h)^n} \leq \frac{1}{1+nh} \rightarrow 0$$
    
    Here the last convergence uses the result of part 2 above. If $r=1$, this sequence is always $1$, so it trivially converges to $1$; if $\lvert r\rvert > 1$, then similarly setting $\lvert r\rvert=1+h$, we have

    $$\lvert r\rvert^n =(1+h)^n \geq 1+nh$$

    so no matter what $M$ is chosen, by making $n$ sufficiently large we can make $\lvert r\rvert^n$ greater than $M$, and therefore $\lvert r\rvert^n$ diverges.
4. $n^{1/n} \rightarrow 1$. To verify this, if we set $n^{1/n} = 1 + h_n$ ( $h_n \geq 0$), then by the binomial theorem

   $$n = (1+h_n)^n \geq \binom{n}{2}h_n^2 = \frac{n(n-1)}{2}h_n^2$$

   so for $n \geq 2$ we have $h_n^2 \leq 2/(n-1) \rightarrow 0$, that is, $h_n \rightarrow 0$.
5. For $r > 1$, $p > 0$, we have $n^p/r^n \rightarrow 0$. By [Proposition 5](#prop5){: data-lid="7cuk8" }, since the ratio of adjacent terms is
    
    $$\frac{(n+1)^p}{r^{n+1}}\cdot\frac{r^n}{n^p} = \frac{1}{r}\left(1+\frac{1}{n}\right)^p \rightarrow \frac{1}{r} < 1$$
    
    this follows immediately.
6. Similarly, for $r > 1$, the ratio of adjacent terms of the sequence $r^n/n!$ is $r/(n+1) \rightarrow 0 < 1$, so for the same reason the limit is $0$.
:::

## Monotone Convergence Theorem

On the other hand, the proof of the following proposition requires knowledge of analysis, so it is impossible for us to prove it at present; nevertheless, the result itself is useful, so we accept it in advance.

::: Proposition 7 (Monotone convergence)
An increasing sequence bounded above and a decreasing sequence bounded below both converge. (The limit of an increasing sequence is the supremum of its terms.)
:::

The most useful application of this is the proof of the existence of the following *natural constant*.

::: Example 8 (The natural constant $e$)
The sequence $a_n = (1 + 1/n)^n$ is increasing and bounded above, and therefore converges by [Proposition 7](#prop7){: data-lid="c0wkx" }.

First, we show that this sequence is increasing. Applying the arithmetic–geometric mean inequality to $n$ copies of $1+1/n$ and one $1$, the arithmetic mean is

$$\frac{n(1+1/n)+1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

and the geometric mean is $((1+1/n)^n\cdot 1)^{1/(n+1)}=a_n^{1/(n+1)}$, so we have

$$a_n \leq \left(1+\frac{1}{n+1}\right)^{n+1} = a_{n+1}$$

and furthermore, since the $n+1$ numbers are not all equal in the equality condition, we obtain the inequality $a_n < a_{n+1}$ where equality does *not* hold.

Now, to show that this sequence is bounded above, observe by the binomial theorem that

$$a_n = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}$$

Each term satisfies

$$\binom{n}{k}\frac{1}{n^k} = \frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k} \leq \frac{1}{k!}$$

and since $k! \geq 2^{k-1}$ ($k \geq 1$), we have

$$a_n \leq \sum_{k=0}^{n}\frac{1}{k!} \leq 1 + \sum_{k=1}^{n}\frac{1}{2^{k-1}} = 3 - \frac{1}{2^{n-1}} < 3$$

We define the limit of this sequence to be the *natural constant* $e = 2.718\ldots$.
:::

## Subsequences

Meanwhile, when analyzing whether a sequence converges, it is useful to consider a new sequence formed by selecting only some of its terms.

::: Definition 9
Given a sequence $(a_n)$ and a strictly increasing sequence of natural numbers $n_1 < n_2 < n_3 < \cdots$, the new sequence $(a_{n_k})_{k\geq 1}$ is called a *subsequence* of $(a_n)$.
:::

That is, it is obtained from the sequence $a_n$ by *skipping* terms while preserving the order of indices. It is intuitively clear that if the original sequence converges to some value, its subsequence will also converge to the same value.

::: Proposition 10
If a sequence $a_n$ converges to $L$, then every subsequence $(a_{n_k})$ also converges to $L$.
:::

::: Proof
For any $\epsilon > 0$, choose $N$ such that $n \geq N$ implies $\lvert a_n - L\rvert < \epsilon$. Then by definition $n_k \geq k$, so if $k \geq N$, then $n_k \geq N$ and therefore

$$\lvert a_{n_k} - L\rvert < \epsilon$$

That is, $a_{n_k} \rightarrow L$.
:::

This proposition is more useful for showing that a sequence does *not* converge than for showing that it converges. This is because, by its contrapositive, if there exist subsequences with two different limits, the original sequence $(a_n)$ does not converge.

::: Example 11 (A divergent sequence)
Consider the sequence $a_n = (-1)^n$. The even-indexed subsequence $a_{2k} = 1 \rightarrow 1$ and the odd-indexed subsequence $a_{2k-1} = -1 \rightarrow -1$ have different limits, so by [Proposition 10](#prop10){: data-lid="wjqkt" } the sequence $(a_n)$ diverges.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
