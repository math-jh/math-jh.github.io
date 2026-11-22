---
title: "Limits of Sequences"
description: "Defines sequence convergence via the epsilon-N criterion and establishes boundedness, limit laws, the squeeze theorem, and the ratio test. Covers standard limits, Euler's number, the monotone convergence theorem, and subsequences."
excerpt: "Sequence convergence, limit laws, standard limits and e, monotone convergence"

categories: [Math / Calculus]
permalink: /en/math/calculus/sequences
sidebar: 
    nav: "calculus-en"

date: 2026-06-21
weight: 3
translated_at: 2026-11-21T11:22:07+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-11-22T03:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
Before starting calculus in earnest, we first define the limit of a sequence. Here, a *sequence* $(a_n)$ is a function assigning a real number to each natural number, that is, $a : \mathbb{N} \rightarrow \mathbb{R}$, viewed as the list of its values $a_1, a_2, a_3, \ldots$. In [§Limits of Functions](/en/math/calculus/functions_and_limits){: data-lid="wfvsa" }, we already examined how a function behaves as $x \rightarrow \infty$; the limit of a sequence can be thought of as its discrete version, where the variable takes only natural-number values and we only consider $n \rightarrow \infty$.

## Convergence of Sequences

::: Definition 1
For a real sequence $(a_n)_{n=1}^\infty$ and a real number $L$, if for every $\epsilon>0$ there exists a natural number $N$ such that

$$n>N \implies \lvert a_n-L \rvert<\epsilon$$

holds, then we call $L$ the *limit*, as $n \rightarrow \infty$, of $a_n$, and write $\lim_{n\rightarrow\infty} a_n=L$.
:::

This definition is taken almost verbatim from [§Limits of Functions, ⁋Definition 14](/en/math/calculus/functions_and_limits#def14){: data-lid="dcvlc" }. Since the variable of a sequence is a natural number, and the natural numbers are discretely distributed, a limit toward a particular natural number (for instance, $2$) is meaningless, and only this definition in the direction of $+\infty$ makes sense.

By the nature of this definition, proofs of limits can be carried out in much the same way as proofs for limits of functions. For example, we can verify the limit $a_n=1/n \rightarrow 0$ by noting that for any $\epsilon>0$, if we arrange $N>1/\epsilon$ by choosing $N$ accordingly, then whenever $n>N$ for a natural number $n$, the inequality $1/n<1/N<\epsilon$ holds. A minor variant is when a sequence diverges to infinity; for instance, divergence to positive infinity can be expressed using [§Limits of Functions, ⁋Definition 13](/en/math/calculus/functions_and_limits#def13){: data-lid="tk37e" } by requiring that for every $M$, the implication $n>N \implies a_n>M$ holds for some $N$. However, there also exist sequences that neither converge nor diverge to infinity ([Example 11](#ex11){: data-lid="9lhgt" }).

As explained above, the basic properties of convergent sequences are mostly obtained by carrying over the proofs from limits of functions directly. For instance, for the following proposition, it suffices to proceed in the same way as in the proof of [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5){: data-lid="b9w9q" }.

::: Proposition 2 (Limit laws for sequences)
Suppose two sequences $a_n$ and $b_n$ converge, and let their limits be

$$\lim_{n\rightarrow\infty} a_n=L, \qquad \lim_{n\rightarrow\infty} b_n=M$$

Then:

1. $\lim (a_n+b_n)=L+M$,
2. for any constant $c$, $\lim c a_n=cL$,
3. $\lim a_n b_n=LM$,
4. if $M \neq 0$ and for all $n$ we have $b_n \neq 0$, then $\lim a_n/b_n=L/M$.
:::

## Properties of Limits

For a sequence $(a_n)$, if the condition that for all $n$ we have $\lvert a_n\rvert \leq M$ holds for some positive number $M$, we say that $(a_n)$ is *bounded*. Since a convergent sequence always clusters near the point to which it converges except for finitely many initial terms, it is bounded.

::: Proposition 3
Every convergent sequence is bounded.
:::
::: Proof
If $a_n \rightarrow L$, then for $\epsilon=1$ we may choose a corresponding $N$ so that for $n>N$, we have $\lvert a_n\rvert \leq \lvert L\rvert+1$. Including the remaining finitely many terms and setting $M=\max\{\lvert a_1\rvert, \ldots, \lvert a_N\rvert, \lvert L\rvert+1\}$, we see that for all $n$, $\lvert a_n\rvert \leq M$.
:::

In the same way, the following is the sequence version of [§Limits of Functions, ⁋Proposition 8](/en/math/calculus/functions_and_limits#prop8){: data-lid="ocpzi" }.

::: Proposition 4 (Squeeze theorem)
If for all sufficiently large $n$ we have $a_n \leq c_n \leq b_n$, and $a_n \rightarrow L$ and $b_n \rightarrow L$, then $c_n \rightarrow L$.
:::

Using this, we obtain the following simple yet useful result.

::: Proposition 5 (Ratio test)
If a real sequence $a_n$ is such that for all $n$ we have $a_n>0$, and the sequence $a_{n+1}/a_n$ of ratios of consecutive terms converges to a value less than $1$, say $L$, then $a_n \rightarrow 0$.
:::
::: Proof
If we choose $L<r<1$, then for this $r$ and sufficiently large $n\geq N$, we have $a_{n+1}/a_n<r$, and hence $a_{N+k}<r^k a_N$. For $0<r<1$, we can show that $r^k \rightarrow 0$ ([Example 6](#ex6){: data-lid="c775e" }), and applying the squeeze theorem yields $a_n \rightarrow 0$.
:::

Including the limit $r^k\rightarrow 0$ ($0<r<1$) that we used only as an assertion in the proof above, in the following example we collect results frequently used in actual computations.

::: Example 6
The following are basic examples of limits of sequences.

1. For $p>0$, we have $1/n^p \rightarrow 0$. When $p \geq 1$, for $n \geq 1$ we have $n^p \geq n$, so $0<1/n^p \leq 1/n \rightarrow 0$, and the result follows by applying [Proposition 4](#prop4){: data-lid="69e6c" }. When $0<p<1$, for any $\epsilon>0$, if we choose a value satisfying $N>\epsilon^{-1/p}$ for $N$, then for $n>N$ we have $n^p>1/\epsilon$, that is, $1/n^p<\epsilon$, so the result follows directly from [Definition 1](#def1){: data-lid="6m9ua" }.
2. More generally, the limit of a ratio of polynomials of the same degree is determined by the ratio of their leading terms. Dividing both the numerator and the denominator of

   $$\frac{a_k n^k+\cdots}{b_k n^k+\cdots}$$

   by $n^k$ leaves each consisting of finitely many $1/n^j$ terms and a constant term. Then, since $1/n^j \rightarrow 0$, we see that the numerator and denominator converge to their respective leading coefficients. If the denominator has larger degree than the numerator, then [Proposition 4](#prop4){: data-lid="85hro" } together with item 1 above shows that this ratio converges to $0$; similarly, if the numerator has larger degree than the denominator, we see that this ratio diverges.
3. If $\lvert r\rvert<1$, then $r^n \rightarrow 0$. The case $r=0$ is trivial since the sequence is identically $0$, so assume $r \neq 0$ and, for a suitable $h>0$, write $\lvert r\rvert=1/(1+h)$. By the binomial theorem, $(1+h)^n \geq 1+nh$, and therefore

    $$\lvert r\rvert^n=\frac{1}{(1+h)^n} \leq \frac{1}{1+nh} \rightarrow 0$$

    Here, the final convergence uses the result of item 2 above. If $r=1$, then this sequence is always $1$ and trivially converges to $1$; similarly, if $\lvert r\rvert>1$, writing $\lvert r\rvert=1+h$ gives

    $$\lvert r\rvert^n =(1+h)^n \geq 1+nh$$

    so for any $M$, taking $n$ sufficiently large makes $\lvert r\rvert^n$ greater than $M$, and hence $\lvert r\rvert^n$ diverges.
4. We have $n^{1/n} \rightarrow 1$. To verify this, set $n^{1/n}=1+h_n$ ($h_n \geq 0$). By the binomial theorem,

   $$n=(1+h_n)^n \geq \binom{n}{2}h_n^2=\frac{n(n-1)}{2}h_n^2$$

   so for $n \geq 2$ we have $h_n^2 \leq 2/(n-1) \rightarrow 0$, that is, $h_n \rightarrow 0$.
5. For $r>1$ and $p>0$, we have $n^p/r^n \rightarrow 0$. By [Proposition 5](#prop5){: data-lid="7cuk8" }, this follows immediately since the ratio of consecutive terms satisfies

    $$\frac{(n+1)^p}{r^{n+1}}\cdot\frac{r^n}{n^p}=\frac{1}{r}\left(1+\frac{1}{n}\right)^p \rightarrow \frac{1}{r}<1$$

6. Similarly, for $r>1$, the ratio of consecutive terms of the sequence $r^n/n!$ is $r/(n+1) \rightarrow 0<1$, so its limit is $0$ for the same reason.
:::

## Monotone Convergence Theorem

Proving the next proposition requires knowledge of analysis, so we cannot prove it at present; broadly speaking, it essentially shares the same roots as the intermediate value theorem and the extreme value theorem. As with those results, even though we cannot give a rigorous proof right now, the result itself is useful, so we accept it in advance.

::: Proposition 7 (Monotone convergence)
Every increasing sequence that is bounded above converges, and every decreasing sequence that is bounded below converges.
:::

The most useful application of this is the following proof of the existence of *Euler's number*.

::: Example 8 (Euler's number $e$)
The sequence $a_n=(1+1/n)^n$ is increasing and bounded above, and therefore converges by [Proposition 7](#prop7){: data-lid="c0wkx" }.

First, let us show that this sequence is increasing. If we apply the arithmetic–geometric mean inequality to $n$ copies of $1+1/n$ and one copy of $1$, the arithmetic mean is

$$\frac{n(1+1/n)+1}{n+1}=\frac{n+2}{n+1}=1+\frac{1}{n+1}$$

and the geometric mean is $((1+1/n)^n\cdot 1)^{1/(n+1)}=a_n^{1/(n+1)}$, so

$$a_n \leq \left(1+\frac{1}{n+1}\right)^{n+1}=a_{n+1}$$

and moreover, by the equality condition, since the $n+1$ numbers are not all equal, we obtain the *strict* inequality $a_n<a_{n+1}$.

Now, to show that this sequence is bounded above, we observe from the binomial theorem that

$$a_n=\sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}$$

Each term satisfies

$$\binom{n}{k}\frac{1}{n^k}=\frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k} \leq \frac{1}{k!}$$

and since $k! \geq 2^{k-1}$ ($k \geq 1$), we have

$$a_n \leq \sum_{k=0}^{n}\frac{1}{k!} \leq 1+\sum_{k=1}^{n}\frac{1}{2^{k-1}}=3-\frac{1}{2^{n-1}}<3$$

We define the limit of this sequence to be *Euler's number* $e=2.718\ldots$.
:::

## Subsequences

When analyzing whether a sequence converges, it is useful to consider a new sequence formed by selecting only some of its terms.

::: Definition 9
Given a sequence $(a_n)$ and a strictly increasing sequence of natural numbers $n_1<n_2<n_3<\cdots$, we call the new sequence $(a_{n_k})_{k\geq 1}$ a *subsequence* of $(a_n)$.
:::

In other words, we select terms from the sequence $a_n$ by *skipping* some while preserving the order of the indices. It is intuitively clear that if the original sequence converges to some value, then its subsequences should also converge to the same value.

::: Proposition 10
If a sequence $a_n$ converges to $L$, then every subsequence $(a_{n_k})$ also converges to $L$.
:::

::: Proof
For any $\epsilon>0$, we can ensure that $n \geq N$ implies $\lvert a_n-L\rvert<\epsilon$ by choosing a suitable $N$. Then by definition we have $n_k \geq k$, so whenever $k \geq N$ we have $n_k \geq N$, and hence

$$\lvert a_{n_k}-L\rvert<\epsilon$$

That is, $a_{n_k} \rightarrow L$.
:::

This proposition is more useful for showing that a sequence does *not* converge than for showing that it converges. This is because, by its contrapositive, if there exist two subsequences with different limits, then the original sequence $(a_n)$ does not converge.

::: Example 11 (A divergent sequence)
Consider the sequence $a_n=(-1)^n$. Since the even-indexed subsequence $a_{2k}=1 \rightarrow 1$ and the odd-indexed subsequence $a_{2k-1}=-1 \rightarrow -1$ have different limits, by [Proposition 10](#prop10){: data-lid="wjqkt" }, $(a_n)$ diverges.
:::

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
