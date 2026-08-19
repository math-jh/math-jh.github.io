---
title: "Limits of Functions"
description: "This post defines the limit of a function using the epsilon-delta language, which is the starting point of calculus. It also covers the limit laws for arithmetic operations, powers, roots, the squeeze theorem, one-sided limits, and limits at infinity with examples."
excerpt: "Defining limits of functions via ε-δ and proving limit laws and the squeeze theorem"

categories: [Math / Calculus]
permalink: /en/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-en"

date: 2026-06-15
weight: 1
translated_at: 2026-08-19T04:15:04+00:00
translation_source: kimi-cli
last_polished_at: 2026-08-19T04:15:04+00:00
---
## Definition of Limits

To define differentiation and integration of functions, we need the concept of limits, just as we learned in high school. What makes the limits we now treat more advanced than those from that time is that we now actually *define* them.

::: Definition 1
Any open interval $(c,d)$ containing a real number $a$ ($c<a<d$) is called a *neighborhood* of the point $a$.
:::

For now, this level of definition for a neighborhood of $a$ is sufficient. For convenience, we call the set obtained by removing $a$ itself from a neighborhood of $a$ a *deleted neighborhood*.

::: Definition 2
Consider a function $f$ defined on some deleted neighborhood of a point $a$. Then a real number $L$ is called the *limit* of $f$ as $x \rightarrow a$ if, for every $\epsilon > 0$, there exists some $\delta > 0$ such that

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon$$

holds. In this case, we write

$$\lim_{x \rightarrow a} f(x) = L.$$
:::

An intuitive explanation for this is as follows. When we discussed the concept of limits in high school by saying that $f(x)$ gets *infinitely close* to $L$, this could not serve as a rigorous mathematical definition because the notion of *closeness* is not mathematical. It is analogous to the fact that, mathematically, the collection of numbers near $L$ does not define a set.

Intuitively, the above $\epsilon$-$\delta$ definition can be understood more easily if we think of it as a process of reaching an agreement that applies to everyone, in order to resolve this issue. That is, no matter how close we require $f(x)$ to be to $L$ (that is, no matter what $\epsilon>0$ is given), as long as we make $x$ sufficiently close to $a$ ($0 < \lvert x - a\rvert < \delta$), we can meet that requirement $\lvert f(x) - L\rvert < \epsilon$. Let us examine this in the following example.

::: Example 3
When proving limits directly from the definition, if $\lvert f(x) - L\rvert$ is a constant multiple of $\lvert x - a\rvert$ as in a linear function, we can read off $\delta$ immediately; but for functions whose rate of change is not constant, one adjustment is needed. Consider $g(x) = x^2$ and let us show that the limit as $x \rightarrow 2$ is $4$. First, we compute

$$\lvert g(x)-4\rvert=\lvert x^2-4\rvert=\lvert x-2\rvert \lvert x+2\rvert.$$

The key point is that $\lvert x-2\rvert$ is small near $2$, but if the accompanying factor $\lvert x+2\rvert$ is not controlled, it can enlarge the product. So we first restrict to $\delta\leq 1$ to secure $\lvert x+2\rvert<5$ (regions with $\delta>1$ are not of interest to begin with), and then set $\delta=\min(1,\epsilon/5)$, so that

$$0 < \lvert x-2\rvert < \delta \implies \lvert x^2 - 4\rvert < 5\delta \leq \epsilon$$

holds.
:::

As above, the essence of this definition is that we can choose $\delta$ to be determined by $\epsilon$. Continuing the intuition from above, no matter what $\epsilon>0$ is brought forth, the *rule* of finding a $\delta>0$ that satisfies this condition is precisely what we do when proving the limit of a function.

## Properties of Limits

Now let us examine the properties of limits based on this. The first property is that if a limit exists, it is unique.

::: Proposition 4 (Uniqueness of Limits)
If $\lim_{x\rightarrow a} f(x) = L$ and $\lim_{x\rightarrow a} f(x) = L'$, then $L = L'$.
:::

::: Proof
Suppose for contradiction that $L \neq L'$. Then $\epsilon = \frac{1}{2}\lvert L - L'\rvert > 0$. Now, by [Definition 2](#def2), there exist corresponding $\delta_1, \delta_2 > 0$ such that the following two conditions

$$0 < \lvert x-a\rvert < \delta_1\implies \lvert f(x) - L\rvert < \epsilon,\qquad 0 < \lvert x-a\rvert < \delta_2\implies\lvert f(x) - L'\rvert < \epsilon$$

are satisfied. Now set $\delta = \min(\delta_1, \delta_2)$. Then for $x$ with $0 < \lvert x-a\rvert < \delta$, the triangle inequality gives

$$\lvert L - L'\rvert \leq \lvert L - f(x)\rvert + \lvert f(x) - L'\rvert < \epsilon + \epsilon = \lvert L - L'\rvert,$$

which is a contradiction. Therefore $L = L'$.
:::

Meanwhile, [Definition 2](#def2) can in principle only be used when a candidate $L$ for the limit of a function is given and we want to show that the limit is indeed $L$. That is, it is not a tool that tells us what the limit of a function *is*. For this purpose, the following proposition is useful.

::: Proposition 5 (Limit Laws)
Suppose $\lim_{x\rightarrow a} f(x) = L$ and $\lim_{x\rightarrow a} g(x) = M$. Then

1. $\lim_{x\rightarrow a} \bigl(f(x) + g(x)\bigr) = L + M$,
2. for any constant $c$, $\lim_{x\rightarrow a} cf(x) = cL$,
3. $\lim_{x\rightarrow a} f(x)g(x) = LM$,
4. if $M \neq 0$, then $\lim_{x\rightarrow a} f(x)/g(x) = L/M$

hold.
:::

::: Proof
1. Given $\epsilon > 0$, from the definition of the limit for $f$ and $g$ we can obtain $\delta_1, \delta_2 > 0$ corresponding to $\epsilon/2$. Then setting $\delta = \min(\delta_1,\delta_2)$, when $0 < \lvert x-a\rvert < \delta$,
    
    $$\lvert (f(x)+g(x)) - (L+M)\rvert \leq \lvert f(x)-L\rvert + \lvert g(x)-M\rvert < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
    
    holds.
2. If $c=0$, any $\delta$ works, so it is trivial. If $c \neq 0$, we take $\delta$ corresponding to $\epsilon/\lvert c\rvert$.

3. We use the following inequality:
    
    $$\lvert f(x)g(x) - LM\rvert = \lvert f(x)(g(x)-M) + M(f(x)-L)\rvert \leq \lvert f(x)\rvert \lvert g(x)-M\rvert + \lvert M\rvert \lvert f(x)-L\rvert.$$
    
    Intuitively, as $x$ approaches $a$, both $\lvert g(x)-M\rvert$ and $\lvert f(x)-L\rvert$ go to $0$, so if we can only guarantee that the accompanying factors $\lvert f(x)\rvert, \lvert g(x)\rvert$ are finite, we can make this smaller than $\epsilon$ through a calculation similar to 1 above.
    
    The trick is to set $\epsilon=1$ and apply [Definition 2](#def2) to $f$ and $g$ respectively. Then there exist suitable $\delta_1, \delta_2$ such that
        
    $$0<\lvert x-a\rvert<\delta_1\implies \lvert f(x)-L\rvert<1\implies \lvert f(x)\rvert< \lvert L\rvert+1$$

    holds, and similarly we can choose $\delta$ so that $\lvert g(x)\rvert <\lvert M\rvert+1$. Now we choose $\delta$ so that all of these two conditions and the following two conditions
    
    $$\lvert g(x)-M\rvert < \frac{\epsilon}{2(\lvert L\rvert+1)},\qquad \lvert f(x)-L\rvert < \frac{\epsilon}{2(\lvert M\rvert+1)}$$
    
    hold simultaneously.

4. It suffices to show $1/g(x) \rightarrow 1/M$ and then apply 3. Since $M \neq 0$, we have $\lvert g(x)\rvert > \lvert M\rvert/2$ in a neighborhood of $a$, and

$$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert \lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert,$$

so it suffices to make $\lvert g(x)-M\rvert$ sufficiently small.
:::

Then the following holds.

::: Corollary 6 (Limits of Powers and Roots)
If $\lim_{x\rightarrow a} f(x) = L$, then

1. for any positive integer $k$, $\lim_{x\rightarrow a} \bigl(f(x)\bigr)^k = L^k$,
2. if $L > 0$, then for any positive integer $k$, $\lim_{x\rightarrow a} \sqrt[k]{f(x)} = \sqrt[k]{L}$

hold.
:::

::: Proof
1. Apply 3 of [Proposition 5](#prop5) and run induction on $k$.
2. First, since $L > 0$, taking $\delta_1 > 0$ corresponding to $\epsilon_1 = L/2$ gives 
    
    $$0 < \lvert x-a\rvert < \delta_1\implies\lvert f(x)-L\rvert < L/2,$$
    
    so $f(x) > L/2 > 0$. On the other hand, for any positive real numbers $u,v$, considering the expansion
    
    $$u - v = \bigl(u^{1/k}-v^{1/k}\bigr)\bigl(u^{(k-1)/k}+u^{(k-2)/k}v^{1/k}+\cdots+v^{(k-1)/k}\bigr)$$
    
    shows that each term of the second factor on the right is greater than or equal to $\min(u,v)^{(k-1)/k}$, so
    
    $$\bigl\lvert u^{1/k}-v^{1/k}\bigr\rvert \leq \frac{\lvert u-v\rvert}{k \min(u,v)^{(k-1)/k}}$$
    
    holds. Therefore, if $0 < \lvert x-a\rvert < \delta_1$, then $0<L/2 < \min(f(x), L)$, so substituting $f(x)=u$ and $L=v$ gives
    
    $$\bigl\lvert \sqrt[k]{f(x)}-\sqrt[k]{L}\bigr\rvert \leq \frac{\lvert f(x)-L\rvert}{k (L/2)^{(k-1)/k}}.$$
    
    Now, for any $\epsilon > 0$, choose $\delta_2 > 0$ corresponding to $k (L/2)^{(k-1)/k} \epsilon$ and set $\delta = \min(\delta_1,\delta_2)$. Then when $0 < \lvert x-a\rvert < \delta$, the right-hand side becomes smaller than $\epsilon$.
:::

By combining these laws, the limit of a polynomial function can be computed by separating it into the limits of each term. The key is the following example.

::: Example 7
For any real number $a$,

$$\lim_{x\rightarrow a}x=a.$$

This is obtained by taking $\delta=\epsilon$. Also, for any real number $c$,

$$\lim_{x\rightarrow a}c=c.$$

This holds no matter what $\delta$ we choose.
:::

Then for any polynomial function

$$f(x)=c_nx^n+\cdots +c_1x+c_0,$$

by separating the limit into each term using the sum and constant multiple laws from [Proposition 5](#prop5) and applying [Corollary 6](#cor6) to the powers, we obtain

$$\lim_{x\rightarrow a}f(x)=c_n\Bigl(\lim_{x\rightarrow a}x\Bigr)^n+\cdots +c_1\lim_{x\rightarrow a}x+\lim_{x\rightarrow a}c_0,$$

and finally substituting [Example 7](#ex7) yields $\lim_{x\rightarrow a}f(x)=f(a)$. Similarly, the limit of a rational function formed as a quotient of polynomial functions is obtained as the quotient of the limits of the numerator and denominator, provided the limit of the denominator is not $0$.

## Squeeze Theorem and Order Properties of Limits

Limits that cannot be computed by limit laws alone are often handled by trapping them with inequalities. The key tool for this method is the squeeze theorem.

::: Proposition 8 (Squeeze Theorem)
If $g(x) \leq f(x) \leq h(x)$ in a deleted neighborhood of a real number $a$ and $\lim_{x\rightarrow a} g(x) = \lim_{x\rightarrow a} h(x) = L$, then $\lim_{x\rightarrow a} f(x) = L$.
:::

::: Proof
For $\epsilon > 0$, let $\delta_1, \delta_2$ be obtained from the limit definitions of $g$ and $h$, and let $\delta_3$ be the radius of the neighborhood where $g \leq f \leq h$ holds. Set $\delta = \min(\delta_1,\delta_2,\delta_3)$. If $0 < \lvert x-a\rvert < \delta$, then $L - \epsilon < g(x) \leq f(x) \leq h(x) < L + \epsilon$, so $\lvert f(x) - L\rvert < \epsilon$.
:::

Another basic fact about how inequalities and limits interact is that limits preserve order.

::: Proposition 9 (Order Preservation of Limits)
If $f(x) \leq g(x)$ in a neighborhood of $a$ (excluding $a$) and the two limits $L = \lim_{x\rightarrow a}f(x)$, $M = \lim_{x\rightarrow a}g(x)$ exist, then $L \leq M$.
:::

::: Proof
Assume $L > M$ and set $\epsilon = \frac{1}{2}(L - M) > 0$. In a sufficiently small neighborhood, $f(x) > L - \epsilon = \frac{L+M}{2}$ and $g(x) < M + \epsilon = \frac{L+M}{2}$, so $f(x) > g(x)$, contradicting the assumption. Therefore $L \leq M$.
:::

Note that a strict inequality $f < g$ does not yield a strict inequality $L < M$. For instance, $f(x) = 0 < x^2 = g(x)$ ($x \neq 0$), but both limits are equal to $0$ as $x \rightarrow 0$. That is, inequalities may weaken under limits.

The most famous application of the squeeze theorem is the following trigonometric limit, which is used crucially when dealing with trigonometric functions in differentiation.

::: Example 10
$\lim_{x\rightarrow 0}(\sin x)/x = 1$. For $0 < x < \pi/2$, comparing areas in the unit circle gives the inequality

$$\frac{1}{2}\sin x \leq \frac{1}{2}x \leq \frac{1}{2}\tan x,$$

that is, $\sin x \leq x \leq \tan x$.

{% diagram Math/Calculus/functions_and_limits-1.svg width="33.66em" alt="Comparison of triangle, sector, and right triangle areas" %}

Now dividing both sides of the above inequality by $\sin x > 0$ and taking reciprocals, we find

$$\cos x \leq \frac{\sin x}{x} \leq 1.$$

This inequality was obtained for $0 < x < \pi/2$, but since $\cos(-x) = \cos x$ and $\sin(-x)/(-x) = (\sin x)/x$, it also holds for $-\pi/2 < x < 0$, and hence over the entire range $0 < \lvert x\rvert < \pi/2$. Moreover, the $\sin x \leq x$ obtained above is also extended to the inequality $\lvert \sin t\rvert \leq \lvert t\rvert$ for all $t$ with $0 < \lvert t\rvert < \pi/2$, since $\sin(-t) = -\sin t$.

Our claim is that $\cos x \rightarrow 1$. For this, using the half-angle formula for trigonometric functions and the $\lvert \sin(x/2)\rvert \leq \lvert x/2\rvert$ obtained above, we have

$$0 \leq \lvert 1 - \cos x\rvert = \left\lvert2\sin^2\frac{x}{2}\right\rvert \leq 2\left(\frac{x}{2}\right)^2 = \frac{x^2}{2},$$

so

$$-\frac{x^2}{2}\leq 1 - \cos x \leq \frac{x^2}{2},$$

and applying [Proposition 8](#prop8) shows that $\cos x \rightarrow 1$. Now using this and applying [Proposition 8](#prop8) again to the earlier inequality shows that the limit of $(\sin x)/x$ is $1$.
:::

The following example is also classical.

::: Example 11
$\lim_{x\rightarrow 0} x\sin(1/x) = 0$. This is because $\bigl\lvert x\sin(1/x)\bigr\rvert \leq \lvert x\rvert$, so

$$-\lvert x\rvert \leq x\sin\frac1x \leq \lvert x\rvert,$$

and both ends go to $0$. On the other hand, $\sin(1/x)$ itself does not have a limit as $x \rightarrow 0$, because it oscillates infinitely between $-1$ and $1$ as $x$ approaches $0$. The factor $x$ pressing this oscillation down to $0$ is the contribution of the squeeze theorem.
:::

## One-Sided Limits and Limits at Infinity

The limits discussed so far were cases where $x$ approaches $a$ from both sides. By restricting the direction of approach to one side, or by extending the definition to cases where $x$ or $f(x)$ becomes infinitely large, we can describe the shape of functions in finer detail.

::: Definition 12
For a real number $a$ and a function $f$, suppose $f$ is defined on $(a, a+c)$ for some suitable $c > 0$. A real number $L$ is called the *right limit* of $f$ as $x \rightarrow a^+$ if, for every $\epsilon > 0$, there exists some $\delta > 0$ such that

$$a < x < a+\delta \implies \lvert f(x) - L\rvert < \epsilon$$

holds. In this case we write $\lim_{x\rightarrow a^+} f(x) = L$. Similarly, when $f$ is defined on $(a-c, a)$, the *left limit* as $x \rightarrow a^-$ is defined by

$$a-\delta < x < a \implies \lvert f(x) - L\rvert < \epsilon$$

and we write $\lim_{x\rightarrow a^-} f(x) = L$.
:::

The existence of the limit $\lim_{x\rightarrow a} f(x)$ is equivalent to both one-sided limits existing and being equal to each other. For example, $f(x) = \lvert x\rvert/x$ has different one-sided limits, $1$ as $x \rightarrow 0^+$ and $-1$ as $x \rightarrow 0^-$, so the limit as $x \rightarrow 0$ does not exist. A point where the two one-sided limits are finite but different from each other is called a jump discontinuity of the function.

::: Definition 13
For a function $f$ defined on a deleted neighborhood of a real number $a$, $\lim_{x\rightarrow a} f(x) = \infty$ means that for every $M > 0$, there exists some $\delta > 0$ such that if $0 < \lvert x-a\rvert < \delta$, then $f(x) > M$. Similarly, $\lim_{x\rightarrow a} f(x) = -\infty$ means that for every $M > 0$, there exists some $\delta > 0$ such that if $0 < \lvert x-a\rvert < \delta$, then $f(x) < -M$.
:::

For example, $\lim_{x\rightarrow 0}1/x^2 = \infty$, and in this case the line $x = 0$ is called a *vertical asymptote* of the graph.

::: Definition 14
For a function $f$ defined for $x$ greater than some real number $N_0$, $\lim_{x\rightarrow\infty} f(x) = L$ means that for every $\epsilon > 0$, there exists some $N > N_0$ such that

$$x > N\implies\lvert f(x) - L\rvert < \epsilon.$$

Similarly, for a function defined for $x$ less than some $N_0$, $\lim_{x\rightarrow-\infty} f(x) = L$ means that there exists $N < N_0$ such that

$$x < N\implies\lvert f(x) - L\rvert < \epsilon.$$
:::

For example, $\lim_{x\rightarrow\infty}1/x = 0$, and for rational functions the highest-degree term dominates the behavior, so $\lim_{x\rightarrow\infty}(2x^2 + 1)/(3x^2 - x) = 2/3$. When such a finite limit $L$ exists, the line $y = L$ becomes a *horizontal asymptote* of the graph.

When direct substitution yields an indeterminate form of type $0/0$, algebraic manipulations such as factorization or rationalizing the numerator can be used to cancel the zero of the denominator, transforming the expression into a form where the limit laws apply. The $\lim(\sin x)/x = 1$ from [Example 10](#ex10) is also used in combination with such algebraic techniques to handle indeterminate forms involving $\sin$.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
