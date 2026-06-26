---
title: "Limits of Sequences"
description: "This post defines sequence convergence using the epsilon-N definition and covers boundedness, limit laws, the squeeze theorem, and the ratio test. It also discusses standard limits, the natural constant e, the monotone convergence theorem, and subsequences."
excerpt: "Convergence, limit laws, standard limits, e, and monotone convergence"

categories: [Math / Calculus]
permalink: /en/math/calculus/sequences
sidebar: 
    nav: "calculus-en"

date: 2026-06-21
weight: 3
translated_at: 2026-06-22T18:30:03+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-22T18:30:03+00:00
---
Before we begin calculus proper, we first define the limit of a sequence. Here a *sequence* $$(a_n)$$ is a function that assigns a real number to each natural number, i.e. $$a : \mathbb{N} \to \mathbb{R}$$, viewed as the list of its values $$a_1, a_2, a_3, \ldots$$. In [§Limits of Functions](/en/math/calculus/functions_and_limits) we already studied how a function behaves as $$x \to \infty$$, and the limit of a sequence can be thought of as the discrete version of this: the case where the variable takes only natural numbers and goes to $$n \to \infty$$.

## Convergence of Sequences

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> For a real sequence $$(a_n)_{n=1}^\infty$$ and a real number $$L$$, if for every $$\varepsilon > 0$$ there exists a natural number $$N$$ such that

$$n > N \implies \lvert a_n - L \rvert < \varepsilon$$

holds, we call $$L$$ the *limit* of $$a_n$$ as $$n \to \infty$$, and write $$\lim_{n\to\infty} a_n = L$$.

</div>

This definition is taken almost verbatim from [§Limits of Functions, ⁋Definition 14](/en/math/calculus/functions_and_limits#def14), and since a sequence has only natural numbers as its variable and goes in only one direction ($$+\infty$$), this is essentially the only way to define its limit. For example, $$a_n = 1/n \to 0$$ is verified by choosing, for arbitrary $$\varepsilon > 0$$, an $$N > 1/\varepsilon$$; then for $$n > N$$ we have $$1/n < 1/N < \varepsilon$$. A slight variant is when a sequence diverges to infinity, which is obtained by transcribing [§Limits of Functions, ⁋Definition 13](/en/math/calculus/functions_and_limits#def13): for arbitrary $$M$$, there exists $$N$$ such that $$n > N \implies a_n > M$$; for example, $$b_n = n$$ is such a sequence. However, there also exist sequences that neither converge nor diverge to infinity ([Example 11](#ex11)).

The basic properties of convergent sequences are mostly obtained by copying the proofs from limits of functions. For example, the following proposition can be proved in exactly the same way as [§Limits of Functions, ⁋Proposition 5](/en/math/calculus/functions_and_limits#prop5).

<div class="proposition" markdown="1">

<ins id="prop2">**Proposition 2 (Limit Laws for Sequences)**</ins> Suppose two sequences $$a_n$$, $$b_n$$ converge, with limits

$$\lim_{n\to\infty} a_n = L, \qquad \lim_{n\to\infty} b_n = M$$

Then

1. $$\lim (a_n + b_n) = L + M$$,
2. for any constant $$c$$, $$\lim c a_n = cL$$,
3. $$\lim a_n b_n = LM$$,
4. if $$M \neq 0$$ and $$b_n \neq 0$$ for all $$n$$, then $$\lim a_n/b_n = L/M$$

hold.

</div>

## Properties of Limits

For a sequence $$(a_n)$$, if there exists a positive number $$M$$ such that $$\lvert a_n\rvert \leq M$$ for all $$n$$, we call $$(a_n)$$ *bounded*. A convergent sequence is bounded because, except for finitely many initial terms, all its terms gather near the limit point.

<div class="proposition" markdown="1">

<ins id="prop3">**Proposition 3**</ins> A convergent sequence is bounded.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

If $$a_n \to L$$, then for $$\varepsilon = 1$$ there exists $$N$$ such that for $$n \geq N$$ we have $$\lvert a_n\rvert \leq \lvert L\rvert + 1$$. Including the remaining finitely many terms, set $$M = \max\{\lvert a_1\rvert, \ldots, \lvert a_{N-1}\rvert, \lvert L\rvert + 1\}$$; then $$\lvert a_n\rvert \leq M$$ for all $$n$$.

</details>

By the same copying, the following is the sequence version of [§Limits of Functions, ⁋Proposition 8](/en/math/calculus/functions_and_limits#prop8).

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4 (Squeeze Theorem)**</ins> If for all sufficiently large $$n$$ we have $$a_n \leq c_n \leq b_n$$, and $$a_n \to L$$, $$b_n \to L$$, then $$c_n \to L$$.

</div>

Then we obtain the following simple but useful result.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Ratio Test)**</ins> If a real sequence $$a_n$$ satisfies $$a_n > 0$$ for all $$n$$, and the sequence of ratios of consecutive terms $$a_{n+1}/a_n$$ converges to a value $$L$$ less than $$1$$, then $$a_n \to 0$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Choose $$r$$ with $$L < r < 1$$; then for sufficiently large $$n \geq N$$ we have $$a_{n+1}/a_n < r$$, so $$a_{N+k} < r^k a_N$$. Since $$0 < r < 1$$, we have $$r^k \to 0$$, and by the squeeze theorem $$a_n \to 0$$.

</details>

Similarly, we collect in the following example several results that are frequently used in actual calculations.

<div class="example" markdown="1">

<ins id="ex6">**Example 6**</ins> The following are basic examples of limits of sequences.

1. For $$p > 0$$, $$1/n^p \to 0$$ holds. Since $$n^p \geq n$$ for $$n \geq 1$$, we have $$0 < 1/n^p \leq 1/n \to 0$$, and thus [Proposition 4](#prop4) applies.
2. More generally, the ratio of two polynomials of the same degree is determined by the ratio of their leading coefficients.

   $$\frac{a_k n^k + \cdots}{b_k n^k + \cdots}$$

   Dividing numerator and denominator by $$n^k$$, both consist of finitely many terms of the form $$1/n^j$$ and a constant term. Then since $$1/n^j \to 0$$, the numerator and denominator converge to their respective leading coefficients. If the denominator has higher degree than the numerator, then by [Proposition 4](#prop4) and the previous item 1, this ratio converges to $$0$$; similarly, if the numerator has higher degree than the denominator, this ratio diverges.
3. If $$\lvert r\rvert < 1$$, then $$r^n \to 0$$. To verify this, set $$\lvert r\rvert = 1/(1+h)$$ for suitable $$h>0$$. Then by the binomial theorem $$(1+h)^n \geq 1 + nh$$, and therefore

    $$\lvert r\rvert^n = \frac{1}{(1+h)^n} \leq \frac{1}{1+nh} \to 0$$

    The convergence of the last term used the result of item 2 above. If $$r=1$$, this sequence is identically $$1$$, so it trivially converges to $$1$$; if $$\lvert r\rvert > 1$$, similarly setting $$r=1+h$$ gives

    $$\lvert r\rvert^n =(1+h)^n \geq 1+nh$$

    so no matter what $$M$$ we choose, by making $$n$$ sufficiently large we can make $$\lvert r\rvert^n$$ exceed $$M$$, and thus $$\lvert r\rvert^n$$ diverges.
4. $$n^{1/n} \to 1$$. To verify this, set $$n^{1/n} = 1 + h_n$$ ($$h_n \geq 0$$); then by the binomial theorem

   $$n = (1+h_n)^n \geq \binom{n}{2}h_n^2 = \frac{n(n-1)}{2}h_n^2$$

   so $$h_n^2 \leq 2/(n-1) \to 0$$, i.e. $$h_n \to 0$$.
5. For $$r > 1$$, $$p > 0$$, $$n^p/r^n \to 0$$ holds. This follows immediately from [Proposition 5](#prop5), since the ratio of consecutive terms is

    $$\frac{(n+1)^p}{r^{n+1}}\cdot\frac{r^n}{n^p} = \frac{1}{r}\left(1+\frac{1}{n}\right)^p \to \frac{1}{r} < 1$$

6. Similarly, for $$r > 1$$, $$p > 0$$, the ratio of consecutive terms of the sequence $$r^n/n!$$ is $$r/(n+1) \to 0 < 1$$, so by the same reasoning it is $$0$$.

</div>

## Monotone Convergence Theorem

Meanwhile, to prove the following proposition we need knowledge of analysis, so it is impossible for us to prove it at present; however, since the result itself is useful, we accept it in advance.

<div class="proposition" markdown="1">

<ins id="prop7">**Proposition 7 (Monotone Convergence)**</ins> An increasing sequence bounded above and a decreasing sequence bounded below converge. (The limit of an increasing sequence is the supremum of its terms.)

</div>

The most useful application of this is the existence proof of the following *natural constant*.

<div class="example" markdown="1">

<ins id="ex8">**Example 8 (The natural constant $$e$$)**</ins> The sequence $$a_n = (1 + 1/n)^n$$ is increasing and bounded above, and thus converges by [Proposition 7](#prop7).

First let us show that this sequence is increasing. Applying the arithmetic–geometric mean inequality to $$n$$ copies of $$1+1/n$$ and one $$1$$, the arithmetic mean is

$$\frac{n(1+1/n)+1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

and the geometric mean is $$((1+1/n)^n\cdot 1)^{1/(n+1)}=a_n^{1/(n+1)}$$, so

$$a_n \leq \left(1+\frac{1}{n+1}\right)^{n+1} = a_{n+1}$$

and moreover, since the $$n+1$$ numbers are not all equal in the equality condition, we obtain the strict inequality $$a_n < a_{n+1}$$.

Now to show that this sequence is bounded above, observe by the binomial theorem that

$$a_n = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}$$

Each term satisfies

$$\binom{n}{k}\frac{1}{n^k} = \frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k} \leq \frac{1}{k!}$$

and since $$k! \geq 2^{k-1}$$ ($$k \geq 1$$),

$$a_n \leq \sum_{k=0}^{n}\frac{1}{k!} \leq 1 + \sum_{k=1}^{\infty}\frac{1}{2^{k-1}} = 3$$

We define the limit of this sequence as the *natural constant* $$e = 2.718\ldots$$.

</div>

## Subsequences

Meanwhile, when analyzing whether a sequence converges, it is useful to consider a new sequence formed by selecting only some of its terms.

<div class="definition" markdown="1">

<ins id="def9">**Definition 9**</ins> Given a sequence $$(a_n)$$ and a strictly increasing sequence of natural numbers $$n_1 < n_2 < n_3 < \cdots$$, the new sequence $$(a_{n_k})_{k\geq 1}$$ is called a *subsequence* of $$(a_n)$$.

</div>

That is, it is obtained from the sequence $$a_n$$ by selecting terms while preserving the order of indices, <em-ko>skipping over</em-ko> some terms along the way. It is intuitively obvious that if the original sequence converges to some value, then any subsequence of it also converges to that same value.

<div class="proposition" markdown="1">

<ins id="prop10">**Proposition 10**</ins> If a sequence $$a_n$$ converges to $$L$$, then every subsequence $$(a_{n_k})$$ also converges to $$L$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For arbitrary $$\varepsilon > 0$$, pick $$N$$ such that for $$n \geq N$$ we have $$\lvert a_n - L\rvert < \varepsilon$$. Then by definition $$n_k \geq k$$, and thus for $$k \geq N$$ we have $$n_k \geq N$$, so

$$\lvert a_{n_k} - L\rvert < \varepsilon$$

That is, $$a_{n_k} \to L$$.

</details>

This proposition is more useful when showing that a sequence does <em-ko>not</em-ko> converge than when showing that it does. By its contrapositive, if there exist two subsequences with different limits, then the original sequence $$(a_n)$$ does not converge.

<div class="example" markdown="1">

<ins id="ex11">**Example 11 (A divergent sequence)**</ins> Consider the sequence $$a_n = (-1)^n$$. The even subsequence $$a_{2k} = 1 \to 1$$ and the odd subsequence $$a_{2k-1} = -1 \to -1$$ have different limits, so by Proposition 10, $$(a_n)$$ diverges.

</div>
