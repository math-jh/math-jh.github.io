---
title: "Limits of Functions and Sequences"
description: "We define the limit of a function using epsilon-delta language, and cover the limit laws for arithmetic operations, limits of powers and roots, the squeeze theorem, one-sided limits, and limits at infinity with examples. Sequences are treated as a special case of functions with the natural numbers as their domain, and their limits are presented using epsilon-N language based on the theory of functional limits."
excerpt: "Defining limits via epsilon-delta and proving limit laws and the squeeze theorem"

categories: [Math / Calculus]
permalink: /en/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-en"

date: 2026-06-15
weight: 1
translated_at: 2026-06-21T13:30:01+00:00
translation_source: kimi-cli
last_polished_at: 2026-06-21T13:30:01+00:00
---
## Definition of Limits

To define the derivative and integral of a function, we need the concept of limits, just as we learned in high school. What makes the limits we now deal with more advanced than back then is that we now *define* limits.

<div class="definition" markdown="1">

<ins id="def1">**Definition 1**</ins> Any open interval $$(c,d)$$ containing a real number $$a$$ ($$c<a<d$$) is called a *neighborhood* of the point $$a$$.

</div>

For now, this definition of a neighborhood of $$a$$ is sufficient. For convenience, we call the set obtained by removing $$a$$ itself from a neighborhood of $$a$$ a *deleted neighborhood*.

<div class="definition" markdown="1">

<ins id="def2">**Definition 2**</ins> Consider a function $$f$$ defined on some deleted neighborhood of $$a$$. Then a real number $$L$$ is called the *limit* of $$f$$ as $$x \to a$$ if, for every $$\epsilon > 0$$, there exists some $$\delta > 0$$ such that

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon$$

holds. In this case, we write $$\displaystyle\lim_{x \to a} f(x) = L$$.

</div>

The intuitive explanation is as follows. In high school, we said that $$f(x)$$ gets *infinitely close* to $$L$$; this cannot become a rigorous mathematical definition because the notion of *close* is not mathematical. It is analogous to observing that the collection of numbers near $$L$$ does not define a set in the mathematical sense.

Intuitively, the above $$\epsilon$$-$$\delta$$ definition resolves this by regarding it as a process of reaching a consensus that works for everyone. That is, no matter how close we require $$f(x)$$ to be to $$L$$ (that is, whatever $$\epsilon>0$$ is given), we can satisfy this demand as long as we make $$x$$ sufficiently close to $$a$$ ($$\lvert f(x) - L\rvert < \epsilon$$). Let us examine this in the following example.

<div class="example" markdown="1">

<ins id="ex3">**Example 3**</ins> In this example, we apply the definition of limits to linear and quadratic functions.

First, consider the linear function $$f(x)=2x-1$$ and show that its limit as $$x\rightarrow 3$$ is $$5$$. Then

$$\lvert f(x)-L\rvert=\lvert (2x-1)-5\rvert=2\lvert x-3\rvert$$

so, if we choose $$\delta=\epsilon/2$$,

$$0<\lvert x-3\rvert<\delta\implies 0<> 2\lvert x-3\rvert<2\delta=\epsilon$$

follows.

As another example, consider the quadratic function $$g(x)=x^2$$ and show that its limit as $$x\rightarrow 2$$ is $$4$$. First, just as above, we compute

$$\lvert g(x)-L\rvert=\lvert x^2-4\rvert=\lvert x-2\rvert\lvert x+2\rvert.$$

The key point in this computation is that while $$\lvert x-2\rvert$$ is small near $$2$$, $$\lvert x+2\rvert$$ does not become too large. That is, if we consider where $$\delta\leq 1$$, then $$\lvert x+2\rvert<5$$ here, and regions where $$\delta>1$$ are not of interest to us in the first place. Therefore, setting $$\delta=\min(1,\epsilon/5)$$,

$$0 < \lvert x-2\rvert < \delta \implies \lvert x^2 - 4\rvert < 5\delta \leq \epsilon$$

holds.

</div>

As above, the essence of this definition is that we can essentially determine $$\epsilon$$ by something determined by $$\delta$$; continuing the intuition above, the *rule* of finding a $$\delta>0$$ that satisfies this condition no matter what $$\epsilon>0$$ is brought in is precisely what we do when proving the limit of a function.

## Properties of Limits

Now let us examine the properties of limits based on this. First, the first property is that if a limit exists, it is unique.

<div class="proposition" markdown="1">

<ins id="prop4">**Proposition 4 (Uniqueness of Limits)**</ins> If $$\displaystyle\lim_{x\to a} f(x) = L$$ and $$\displaystyle\lim_{x\to a} f(x) = L'$$, then $$L = L'$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Suppose for contradiction that $$L \neq L'$$. Then $$\epsilon = \frac{1}{2}\lvert L - L'\rvert > 0$$. By [Definition 2](#def2), there exist corresponding $$\delta_1, \delta_2 > 0$$ such that the following two conditions

$$0 < \lvert x-a\rvert < \delta_1\implies \lvert f(x) - L\rvert < \epsilon,\qquad 0 < \lvert x-a\rvert < \delta_2\implies\lvert f(x) - L'\rvert < \epsilon$$

are satisfied. Now set $$\delta = \min(\delta_1, \delta_2)$$; then for $$x$$ with $$0 < \lvert x-a\rvert < \delta$$, by the triangle inequality

$$\lvert L - L'\rvert \leq \lvert L - f(x)\rvert + \lvert f(x) - L'\rvert < \epsilon + \epsilon = \lvert L - L'\rvert$$

which is a contradiction. Therefore $$L = L'$$.

</details>

Meanwhile, [Definition 2](#def2) can in principle only be used when a candidate $$L$$ for the limit is given and we want to show that the limit is actually $$L$$. That is, it is not a tool that tells us *what* the limit of a function is. For this, the following proposition is useful.

<div class="proposition" markdown="1">

<ins id="prop5">**Proposition 5 (Limit Laws)**</ins> Suppose $$\displaystyle\lim_{x\to a} f(x) = L$$ and $$\displaystyle\lim_{x\to a} g(x) = M$$. Then

1. $$\displaystyle\lim_{x\to a} \bigl(f(x) + g(x)\bigr) = L + M$$,
2. For any constant $$c$$, $$\displaystyle\lim_{x\to a} cf(x) = cL$$,
3. $$\displaystyle\lim_{x\to a} f(x)g(x) = LM$$,
4. If $$M \neq 0$$, then $$\displaystyle\lim_{x\to a} \frac{f(x)}{g(x)} = \frac{L}{M}$$

hold.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. Given $$\epsilon > 0$$, from the definition of limits for $$f$$ and $$g$$ we can obtain $$\delta_1, \delta_2 > 0$$ corresponding to $$\epsilon/2$$. Then setting $$\delta = \min(\delta_1,\delta_2)$$, when $$0 < \lvert x-a\rvert < \delta$$
    
    $$\lvert (f(x)+g(x)) - (L+M)\rvert \leq \lvert f(x)-L\rvert + \lvert g(x)-M\rvert < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
    
    holds.
2. If $$c=0$$, any $$\delta$$ works, so it is trivial. If $$c \neq 0$$, we can take $$\delta$$ corresponding to $$\epsilon/\lvert c\rvert$$.

3. We use the following inequality
    
    $$\lvert f(x)g(x) - LM\rvert = \lvert f(x)(g(x)-M) + M(f(x)-L)\rvert \leq \lvert f(x)\rvert\,\lvert g(x)-M\rvert + \lvert M\rvert\,\lvert f(x)-L\rvert$$
    
    Intuitively, as $$x$$ approaches $$a$$, both $$\lvert g(x)-M\rvert$$ and $$\lvert f(x)-L\rvert$$ go to $$0$$, so if we can only guarantee that the factors $$\lvert f(x)\rvert, \lvert g(x)\rvert$$ in front of them are finite, then we can make this smaller than $$\epsilon$$ through a calculation similar to 1 above.
    
    The trick is to set $$\epsilon=1$$ and apply [Definition 2](#def2) to $$f$$ and $$g$$ respectively. Then there exist suitable $$\delta_1, \delta_2$$ such that
        
    $$0<\lvert x-a\rvert<\delta_1\implies 0<\lvert f(x)-L\rvert<1\implies \lvert f(x)\rvert< \lvert L\rvert+1$$

    and similarly we can choose $$\delta$$ so that $$\lvert g(x)\rvert <\lvert M\rvert+1$$. Now we choose $$\delta$$ so that all of these and the following two conditions
    
    $\lvert g(x)-M\rvert < \frac{\epsilon}{2(\lvert L\rvert+1)},\qquad \lvert f(x)-L\rvert < \frac{\epsilon}{2(\lvert M\rvert+1)}$$
    
    hold simultaneously.

4. We show $$1/g(x) \to 1/M$$ and then apply 3. Since $$M \neq 0$$, we have $$\lvert g(x)\rvert > \lvert M\rvert/2$$ in a neighborhood of $$a$$, and

$$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert\,\lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert$$

so it suffices to make $$\lvert g(x)-M\rvert$$ sufficiently small.

</details>

Then the following holds.

<div class="proposition" markdown="1">

<ins id="cor6">**Corollary 6 (Limits of Powers and Roots)**</ins> If $$\displaystyle\lim_{x\to a} f(x) = L$$, then

1. For any positive integer $$k$$, $$\displaystyle\lim_{x\to a} \bigl(f(x)\bigr)^k = L^k$$,
2. If $$L > 0$$, then for any positive integer $$k$$, $$\displaystyle\lim_{x\to a} \sqrt[k]{f(x)} = \sqrt[k]{L}$$

hold.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

1. Apply 3 of [Proposition 5](#prop5) and run induction on $$k$$.
2. First, since $$L > 0$$, taking $$\delta_1 > 0$$ corresponding to $$\epsilon_1 = L/2$$,
    
    $$0 < \lvert x-a\rvert < \delta_1\implies\lvert f(x)-L\rvert < L/2$$
    
    so $$f(x) > L/2 > 0$$. Meanwhile, for any positive real numbers $$u,v$$, considering the following expansion
    
    $$u - v = \bigl(u^{1/k}-v^{1/k}\bigr)\bigl(u^{(k-1)/k}+u^{(k-2)/k}v^{1/k}+\cdots+v^{(k-1)/k}\bigr)$$
    
    each term of the second factor on the right is greater than $$\min(u,v)^{(k-1)/k}$$, so
    
    $$\bigl\lvert u^{1/k}-v^{1/k}\bigr\rvert \leq \frac{\lvert u-v\rvert}{k\,\min(u,v)^{(k-1)/k}}$$
    
    holds. Therefore if $$0 < \lvert x-a\rvert < \delta_1$$, then $$0<L/2 < \min(f(x), L)$$, so substituting $$f(x)=u$$ and $$L=v$$,
    
    $$\bigl\lvert \sqrt[k]{f(x)}-\sqrt[k]{L}\bigr\rvert \leq \frac{\lvert f(x)-L\rvert}{k\,(L/2)^{(k-1)/k}}$$
    
    we obtain. Now for any $$\epsilon > 0$$, choose $$\delta_2 > 0$$ corresponding to $$k\,(L/2)^{(k-1)/k}\,\epsilon$$ and set $$\delta = \min(\delta_1,\delta_2)$$; then when $$0 < \lvert x-a\rvert < \delta$$, the right-hand side becomes smaller than $$\epsilon$$.

</details>

By combining these laws, the limit of a polynomial can be computed by separating it into the limits of each term. The key is the following example.

<div class="example" markdown="1">

<ins id="ex7">**Example 7**</ins> For any real number $$a$$,

$$\lim_{x\rightarrow a}x=a$$

holds. This is obtained by taking $$\delta=\epsilon$$. Also, for any real number $$c$$,

$$\lim_{x\rightarrow a}c=c$$

holds. Any $$\delta$$ works for this.

</div>

Then for any polynomial

$$f(x)=c_nx^n+\cdots +c_1x+c_0$$

by applying the first law of [Proposition 5](#prop5) repeatedly, we obtain

$$\lim_{x\rightarrow a}f(x)=\lim_{x \rightarrow a}c_nx^n+\cdots +\lim_{x\rightarrow a}c_1x+ \lim_{x\rightarrow a} c_0$$

and then applying the second law of [Proposition 5](#prop5) and [Corollary 6](#cor6), we rewrite this as

$$\lim_{x\rightarrow a}f(x)=c_n\lvert(\lim_{x\rightarrow a}x\rvert)^n+\cdots c_1\lim_{x\rightarrow a}x+\lim_{x\rightarrow a}c_0$$

and then apply [Example 7](#ex7). In a similar way, we can show that the limit of any rational function formed as a ratio of polynomials is also obtained by taking the limits of the numerator and denominator separately and then forming their quotient, provided the limit of the denominator is not $$0$$.

## Squeeze Theorem and Order Properties of Limits

Limits that cannot be computed by limit laws alone are often handled by trapping them with inequalities. The key tool for this method is the squeeze theorem.

<div class="proposition" markdown="1">

<ins id="prop8">**Proposition 8 (Squeeze Theorem)**</ins> If $$g(x) \leq f(x) \leq h(x)$$ in a deleted neighborhood of a real number $$a$$ and $$\displaystyle\lim_{x\to a} g(x) = \lim_{x\to a} h(x) = L$$, then $$\displaystyle\lim_{x\to a} f(x) = L$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

For $$\epsilon > 0$$, gather $$\delta_1, \delta_2$$ obtained from the limit definitions of $$g$$ and $$h$$ and the radius $$\delta_3$$ of the neighborhood where $$g \leq f \leq h$$ holds, and set $$\delta = \min(\delta_1,\delta_2,\delta_3)$$. If $$0 < \lvert x-a\rvert < \delta$$, then $$L - \epsilon < g(x) \leq f(x) \leq h(x) < L + \epsilon$$, so $$\lvert f(x) - L\rvert < \epsilon$$.

</details>

Another basic fact about how inequalities and limits interact is that limits preserve order.

<div class="proposition" markdown="1">

<ins id="prop9">**Proposition 9 (Order Preservation of Limits)**</ins> If $$f(x) \leq g(x)$$ in a neighborhood of $$a$$ (excluding $$a$$) and the two limits $$L = \displaystyle\lim_{x\to a}f(x)$$, $$M = \displaystyle\lim_{x\to a}g(x)$$ exist, then $$L \leq M$$.

</div>

<details class="proof" markdown="1">
<summary>Proof</summary>

Assume $$L > M$$ and set $$\epsilon = \frac{1}{2}(L - M) > 0$$. In a sufficiently small neighborhood, $$f(x) > L - \epsilon = \frac{L+M}{2}$$ and $$g(x) < M + \epsilon = \frac{L+M}{2}$$, so $$f(x) > g(x)$$, contradicting the assumption. Therefore $$L \leq M$$.

</details>

Note that a strict inequality $$f < g$$ does not give a strict inequality $$L < M$$. For example, $$f(x) = 0 < x^2 = g(x)$$ ($$x \neq 0$$), but both limits as $$x \to 0$$ are equal to $$0$$. That is, inequalities may weaken under limits.

The most famous application of the squeeze theorem is the following trigonometric limit, which is used decisively when dealing with trigonometric functions in differentiation.

<div class="example" markdown="1">

<ins id="ex10">**Example 10**</ins> $$\displaystyle\lim_{x\to 0}\frac{\sin x}{x} = 1$$. Comparing areas in the unit circle for $$0 < x < \pi/2$$, we obtain the inequality

$$\frac{1}{2}\sin x \leq \frac{1}{2}x \leq \frac{1}{2}\tan x$$

That is, $$\sin x \leq x \leq \tan x$$.

![Comparison of triangle, sector, and right triangle areas](/assets/images/Math/Calculus/functions_and_limits-1.svg){:style="width:33.66em" class="invert" .align-center}

Now dividing both sides of the above inequality by $$\sin x > 0$$ and taking reciprocals, we know that

$$\cos x \leq \frac{\sin x}{x} \leq 1$$

Our claim is that $$\cos x \to 1$$. For this, using the half-angle formula for trigonometric functions and $$\sin\frac{x}{2} \leq \frac{x}{2}$$ obtained above,

$$0 \leq \lvert 1 - \cos x\rvert = \left\lvert2\sin^2\frac{x}{2}\right\rvert \leq 2\left(\frac{x}{2}\right)^2 = \frac{x^2}{2}$$

so

$$-\frac{x^2}{2}\leq 1 - \cos x \leq \frac{x^2}{2}$$

and applying the squeeze theorem, we know that $$\cos x \to 1$$. Now applying the squeeze theorem again to the earlier inequality, we know that the limit of $$\frac{\sin x}{x}$$ is $$1$$.

</div>

The following example is also classical.

<div class="example" markdown="1">

<ins id="ex11">**Example 11**</ins> $$\displaystyle\lim_{x\to 0} x\sin\frac{1}{x} = 0$$. This is because $$\bigl\lvert x\sin\frac{1}{x}\bigr\rvert \leq \lvert x\rvert$$, so

$$-\lvert x\rvert \leq x\sin\frac1x \leq \lvert x\rvert$$

and both ends go to $$0$$. On the other hand, $$\sin\frac1x$$ itself does not have a limit as $$x \to 0$$, because $$x$$ oscillates infinitely between $$-1$$ and $$1$$ as it approaches $$0$$. The factor $$x$$ pressing this oscillation to $$0$$ is the contribution of the squeeze theorem.

</div>

## One-Sided Limits and Limits at Infinity

The limits so far have been the case where $$x$$ approaches $$a$$ from both sides. By restricting the direction of approach to one side, or extending the definition to cases where $$x$$ or $$f(x)$$ becomes infinitely large, we can describe the shape of functions in more detail.

<div class="definition" markdown="1">

<ins id="def12">**Definition 12**</ins> For a real number $$a$$ and a function $$f$$, suppose $$f$$ is defined on $$(a, a+c)$$ for some suitable $$c > 0$$. A real number $$L$$ is called the *right limit* of $$f$$ as $$x \to a^+$$ if, for every $$\epsilon > 0$$, there exists some $$\delta > 0$$ such that

$$a < x < a+\delta \implies \lvert f(x) - L\rvert < \epsilon$$

holds. In this case, we write $$\displaystyle\lim_{x\to a^+} f(x) = L$$. Similarly, when $$f$$ is defined on $$(a-c, a)$$, the *left limit* as $$x \to a^-$$ is defined by

$$a-\delta < x < a \implies \lvert f(x) - L\rvert < \epsilon$$

and we write $$\displaystyle\lim_{x\to a^-} f(x) = L$$.

</div>

The existence of the limit $$\displaystyle\lim_{x\to a} f(x)$$ is equivalent to both one-sided limits existing and being equal to each other. For example, $$f(x) = \dfrac{\lvert x\rvert}{x}$$ has right limit $$1$$ as $$x \to 0^+$$ and left limit $$-1$$ as $$x \to 0^-$$; since the two one-sided limits differ, the limit as $$x \to 0$$ does not exist. A point where the two one-sided limits are finite but different from each other is called a *jump* discontinuity of the function.

<div class="definition" markdown="1">

<ins id="def13">**Definition 13**</ins> For a function $$f$$ defined on a deleted neighborhood of a real number $$a$$, $$\displaystyle\lim_{x\to a} f(x) = \infty$$ means that for every $$M > 0$$, there exists some $$\delta > 0$$ such that if $$0 < \lvert x-a\rvert < \delta$$, then $$f(x) > M$$. Similarly, $$\displaystyle\lim_{x\to a} f(x) = -\infty$$ means that for every $$M > 0$$, there exists some $$\delta > 0$$ such that if $$0 < \lvert x-a\rvert < \delta$$, then $$f(x) < -M$$.

</div>

For example, $$\displaystyle\lim_{x\to 0}\frac{1}{x^2} = \infty$$, and in this case the line $$x = 0$$ is called a *vertical asymptote* of the graph.

<div class="definition" markdown="1">

<ins id="def14">**Definition 14**</ins> For a function $$f$$ defined for $$x$$ greater than some real number $$N_0$$, $$\displaystyle\lim_{x\to\infty} f(x) = L$$ means that for every $$\epsilon > 0$$, there exists some $$N > N_0$$ such that if $$x > N$$, then $$\lvert f(x) - L\rvert < \epsilon$$. Similarly, for a function defined for $$x$$ less than some $$N_0$$, $$\displaystyle\lim_{x\to-\infty} f(x) = L$$ means that there exists an $$N$$ such that if $$x < N$$, then $$\lvert f(x) - L\rvert < \epsilon$$.

</div>

For example, $$\displaystyle\lim_{x\to\infty}\frac{1}{x} = 0$$, and for rational functions the leading term dominates the behavior, so $$\displaystyle\lim_{x\to\infty}\frac{2x^2 + 1}{3x^2 - x} = \frac{2}{3}$$. If such a finite limit $$L$$ exists, the line $$y = L$$ becomes a *horizontal asymptote* of the graph.

<div class="example" markdown="1">

<ins id="ex15">**Example 15 (Resolving Indeterminate Forms)**</ins> If direct substitution yields $$\frac00$$, we resolve the indeterminate form by algebraic manipulation. By factoring,

$$\lim_{x\to 2}\frac{x^2 - 4}{x - 2} = \lim_{x\to 2}(x + 2) = 4,$$

by rationalizing the numerator,

$$\lim_{x\to 0}\frac{\sqrt{1+x} - 1}{x} = \lim_{x\to 0}\frac{1}{\sqrt{1+x}+1} = \frac12,$$

and combining with [Example 10](#ex10), $$\displaystyle\lim_{x\to 0}\frac{\sin 3x}{x} = \lim_{x\to 0}3\cdot\frac{\sin 3x}{3x} = 3$$.

</div>
