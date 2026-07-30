---
title: "Limits of Functions"
description: "This post defines limits of functions using epsilon-delta language, the starting point of calculus. It covers the limit laws for arithmetic operations, limits of powers and roots, the squeeze theorem, one-sided limits, and limits at infinity, with examples."
excerpt: "Defining limits of functions via ε-δ and proving limit laws and the squeeze theorem"

categories: [Math / Calculus]
permalink: /en/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-en"

date: 2026-06-15
weight: 1
translated_at: 2026-07-13T21:30:02+00:00
translation_source: kimi-cli
last_polished_at: 2026-07-13T21:30:02+00:00
---
## Definition of the Limit

To define the differentiation and integration of functions, we need the concept of the limit, just as we learned in high school. What makes the limit we are now dealing with more advanced than what we studied then is that we now *define* the limit.

::: Definition 1
Any open interval $(c,d)$ containing a real number $a$ ($c<a<d$) is called a *neighborhood* of the point $a$.
:::

For now, this definition of a neighborhood of $a$ is sufficient. For convenience, we call the set obtained by removing $a$ itself from a neighborhood of $a$ a *deleted neighborhood*.

::: Definition 2
Consider a function $f$ defined on some deleted neighborhood of the point $a$. Then a real number $L$ is called the *limit* of $f$ as $x \rightarrow a$ if, for every $\epsilon > 0$, there exists a $\delta > 0$ such that

$$0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \epsilon$$

holds. We write this as

$$\lim_{x \rightarrow a} f(x) = L$$
:::

The intuitive explanation is as follows. The reason why the high school description that $f(x)$ gets *infinitely close* to $L$ cannot be made into a rigorous mathematical definition is that the notion of *closeness* is not mathematical. It is analogous to saying that a collection of numbers close to $L$ does not define a set in mathematical terms.

Intuitively, it is helpful to think of the above $\epsilon$-$\delta$ definition as a process of reaching a consensus that works for everyone. That is, no matter how close we demand $f(x)$ to be to $L$ (i.e., no matter what $\epsilon>0$ is given), as long as we make $x$ sufficiently close to $a$ ($0 < \lvert x - a\rvert < \delta$), we can meet that demand: $\lvert f(x) - L\rvert < \epsilon$. Let us examine this in the following example.

::: Example 3
When proving a limit directly from the definition, if $\lvert f(x) - L\rvert$ is a constant multiple of $\lvert x - a\rvert$ as in a linear function, we can read off $\delta$ immediately. However, for functions whose rate of change is not constant, a small adjustment is needed. Consider $g(x) = x^2$ and let us show that the limit as $x \rightarrow 2$ is $4$. First, we compute

$$\lvert g(x)-4\rvert=\lvert x^2-4\rvert=\lvert x-2\rvert \lvert x+2\rvert$$

The key point is that while $\lvert x-2\rvert$ is small near $2$, the factor $\lvert x+2\rvert$ in front of it can inflate the product if it is not controlled. Therefore, we first restrict to $\delta\leq 1$ to secure $\lvert x+2\rvert<5$ (regions where $\delta>1$ are not of interest in the first place), and then set $\delta=\min(1,\epsilon/5)$, so that

$$0 < \lvert x-2\rvert < \delta \implies \lvert x^2 - 4\rvert < 5\delta \leq \epsilon$$

holds.
:::

As above, the essence of this definition is that we can choose $\delta$ to be determined by $\epsilon$. Continuing the intuition from above, what we do when proving the limit of a function is precisely to find a *rule* that, no matter what $\epsilon>0$ is brought forward, produces a $\delta>0$ satisfying this condition.

## Properties of Limits

Now let us examine the properties of limits based on this. First, if a limit exists, it is unique.

::: Proposition 4 (Uniqueness of the Limit)
If $\lim_{x\rightarrow a} f(x) = L$ and $\lim_{x\rightarrow a} f(x) = L'$, then $L = L'$.
:::

::: Proof
Suppose, for the sake of contradiction, that $L \neq L'$. Then $\epsilon = \frac{1}{2}\lvert L - L'\rvert > 0$. By [Definition 2](#def2), there exist corresponding $\delta_1, \delta_2 > 0$ such that the following two conditions

$$0 < \lvert x-a\rvert < \delta_1\implies \lvert f(x) - L\rvert < \epsilon,\qquad 0 < \lvert x-a\rvert < \delta_2\implies\lvert f(x) - L'\rvert < \epsilon$$

are satisfied. Now set $\delta = \min(\delta_1, \delta_2)$. Then for $x$ with $0 < \lvert x-a\rvert < \delta$, the triangle inequality gives

$$\lvert L - L'\rvert \leq \lvert L - f(x)\rvert + \lvert f(x) - L'\rvert < \epsilon + \epsilon = \lvert L - L'\rvert$$

which is a contradiction. Therefore, $L = L'$.
:::

Meanwhile, [Definition 2](#def2) can in principle only be used when a candidate $L$ for the limit of a function is given and we want to show that the limit is actually $L$. That is, it is not a tool that tells us *what* the limit of a function is. For this purpose, the following proposition is useful.

::: Proposition 5 (Limit Laws)
Let $\lim_{x\rightarrow a} f(x) = L$ and $\lim_{x\rightarrow a} g(x) = M$. Then

1. $\lim_{x\rightarrow a} \bigl(f(x) + g(x)\bigr) = L + M$,
2. For any constant $c$, $\lim_{x\rightarrow a} cf(x) = cL$,
3. $\lim_{x\rightarrow a} f(x)g(x) = LM$,
4. If $M \neq 0$, then $\lim_{x\rightarrow a} f(x)/g(x) = L/M$

hold.
:::

::: Proof
1. Given a positive number $\epsilon > 0$, we can obtain $\delta_1, \delta_2 > 0$ corresponding to $\epsilon/2$ from the limit definitions of $f$ and $g$, respectively. Then setting $\delta = \min(\delta_1,\delta_2)$, when $0 < \lvert x-a\rvert < \delta$,
    
    $$\lvert (f(x)+g(x)) - (L+M)\rvert \leq \lvert f(x)-L\rvert + \lvert g(x)-M\rvert < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
    
    holds.
2. If $c=0$, any $\delta$ will do, so this is trivial. If $c \neq 0$, we simply take the $\delta$ corresponding to $\epsilon/\lvert c\rvert$.

3. We use the inequality
    
    $$\lvert f(x)g(x) - LM\rvert = \lvert f(x)(g(x)-M) + M(f(x)-L)\rvert \leq \lvert f(x)\rvert \lvert g(x)-M\rvert + \lvert M\rvert \lvert f(x)-L\rvert$$
    
    Intuitively, as $x$ approaches $a$, both $\lvert g(x)-M\rvert$ and $\lvert f(x)-L\rvert$ go to $0$, so if we can guarantee that the coefficients $\lvert f(x)\rvert$ and $\lvert g(x)\rvert$ in front of them are finite, we can make this smaller than $\epsilon$ through a calculation similar to 1 above.
    
    The trick is to set $\epsilon=1$ and apply [Definition 2](#def2) to $f$ and $g$ separately. Then there exist appropriate $\delta_1, \delta_2$ such that
        
    $$0<\lvert x-a\rvert<\delta_1\implies 0<\lvert f(x)-L\rvert<1\implies \lvert f(x)\rvert< \lvert L\rvert+1$$

    and similarly we can choose a $\delta$ such that $\lvert g(x)\rvert <\lvert M\rvert+1$. Now we choose $\delta$ so that all of these two conditions and the following two conditions
    
    $$\lvert g(x)-M\rvert < \frac{\epsilon}{2(\lvert L\rvert+1)},\qquad \lvert f(x)-L\rvert < \frac{\epsilon}{2(\lvert M\rvert+1)}$$
    
    are satisfied.

4. We show $1/g(x) \rightarrow 1/M$ and then apply 3. Since $M \neq 0$, we have $\lvert g(x)\rvert > \lvert M\rvert/2$ in a neighborhood of $a$, and

$$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert \lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert$$

so it suffices to make $\lvert g(x)-M\rvert$ sufficiently small.
:::

Then the following holds.

::: Corollary 6 (Limits of Powers and Roots)
If $\lim_{x\rightarrow a} f(x) = L$, then

1. For any positive integer $k$, $\lim_{x\rightarrow a} \bigl(f(x)\bigr)^k = L^k$,
2. If $L > 0$, then for any positive integer $k$, $\lim_{x\rightarrow a} \sqrt[k]{f(x)} = \sqrt[k]{L}$

hold.
:::

::: Proof
1. Apply 3 of [Proposition 5](#prop5) and run induction on $k$.
2. First, since $L > 0$, if we choose $\delta_1 > 0$ corresponding to $\epsilon_1 = L/2$, then 
    
    $$0 < \lvert x-a\rvert < \delta_1\implies\lvert f(x)-L\rvert < L/2$$
    
    so $f(x) > L/2 > 0$. Meanwhile, for any positive real numbers $u,v$, considering the expansion
    
    $$u - v = \bigl(u^{1/k}-v^{1/k}\bigr)\bigl(u^{(k-1)/k}+u^{(k-2)/k}v^{1/k}+\cdots+v^{(k-1)/k}\bigr)$$
    
    each term of the second factor on the right is greater than $\min(u,v)^{(k-1)/k}$, so
    
    $$\bigl\lvert u^{1/k}-v^{1/k}\bigr\rvert \leq \frac{\lvert u-v\rvert}{k \min(u,v)^{(k-1)/k}}$$
    
    holds. Therefore, if $0 < \lvert x-a\rvert < \delta_1$, then $0<L/2 < \min(f(x), L)$, so substituting $f(x)=u$ and $L=v$, we obtain
    
    $$\bigl\lvert \sqrt[k]{f(x)}-\sqrt[k]{L}\bigr\rvert \leq \frac{\lvert f(x)-L\rvert}{k (L/2)^{(k-1)/k}}$$
    
    Now for any $\epsilon > 0$, choose $\delta_2 > 0$ corresponding to $k (L/2)^{(k-1)/k} \epsilon$ and set $\delta = \min(\delta_1,\delta_2)$. Then when $0 < \lvert x-a\rvert < \delta$, the right-hand side becomes smaller than $\epsilon$.
:::

By combining these laws, the limit of a polynomial function can be computed by separating it into the limits of each term. The key is the following example.

::: Example 7
For any real number $a$,

$$\lim_{x\rightarrow a}x=a$$

This is obtained by setting $\delta=\epsilon$. Also, for any real number $c$,

$$\lim_{x\rightarrow a}c=c$$

This holds no matter what $\delta$ we choose.
:::

Then for any polynomial function

$$f(x)=c_nx^n+\cdots +c_1x+c_0$$

by separating the limit into each term using the sum and constant-multiple laws of [Proposition 5](#prop5) and applying [Corollary 6](#cor6) to the powers, we get

$$\lim_{x\rightarrow a}f(x)=c_n\Bigl(\lim_{x\rightarrow a}x\Bigr)^n+\cdots +c_1\lim_{x\rightarrow a}x+\lim_{x\rightarrow a}c_0$$

and finally substituting [Example 7](#ex7) yields $\lim_{x\rightarrow a}f(x)=f(a)$. In a similar manner, the limit of a rational function formed as a ratio of polynomial functions is also obtained as the ratio of the limits of the numerator and denominator, provided the limit of the denominator is not $0$.

## The Squeeze Theorem and Order Properties of Limits

Limits that cannot be computed by the limit laws alone are often handled by bounding them with inequalities. The key tool for this method is the squeeze theorem.

::: Proposition 8 (Squeeze Theorem)
If $g(x) \leq f(x) \leq h(x)$ in a deleted neighborhood of the real number $a$ and $\lim_{x\rightarrow a} g(x) = \lim_{x\rightarrow a} h(x) = L$, then $\lim_{x\rightarrow a} f(x) = L$.
:::

::: Proof
For $\epsilon > 0$, let $\delta_1, \delta_2$ be obtained from the limit definitions of $g$ and $h$, and let $\delta_3$ be the radius of the neighborhood where $g \leq f \leq h$ holds. Set $\delta = \min(\delta_1,\delta_2,\delta_3)$. If $0 < \lvert x-a\rvert < \delta$, then $L - \epsilon < g(x) \leq f(x) \leq h(x) < L + \epsilon$, so $\lvert f(x) - L\rvert < \epsilon$.
:::

Another basic fact about how inequalities and limits interact is that limits preserve order.

::: Proposition 9 (Order Preservation of Limits)
If $f(x) \leq g(x)$ in a neighborhood of $a$ (excluding $a$) and the two limits $L = \lim_{x\rightarrow a}f(x)$, $M = \lim_{x\rightarrow a}g(x)$ exist, then $L \leq M$.
:::

::: Proof
Assume $L > M$ and set $\epsilon = \frac{1}{2}(L - M) > 0$. In a sufficiently small neighborhood, $f(x) > L - \epsilon = \frac{L+M}{2}$ and $g(x) < M + \epsilon = \frac{L+M}{2}$, so $f(x) > g(x)$, contradicting the assumption. Therefore, $L \leq M$.
:::

Note that a strict inequality $f < g$ does not yield a strict inequality $L < M$. For example, $f(x) = 0 < x^2 = g(x)$ ($x \neq 0$), but both limits are equal to $0$ as $x \rightarrow 0$. That is, an inequality may weaken in the limit.

The most famous application of the squeeze theorem is the following trigonometric limit, which is used decisively when dealing with trigonometric functions in differentiation.

::: Example 10
$\lim_{x\rightarrow 0}(\sin x)/x = 1$. For $0 < x < \pi/2$, comparing the areas of the unit circle gives the inequality

$$\frac{1}{2}\sin x \leq \frac{1}{2}x \leq \frac{1}{2}\tan x$$

That is, $\sin x \leq x \leq \tan x$.

{% diagram Math/Calculus/functions_and_limits-1.svg width="33.66em" alt="Comparison of triangle, sector, and right triangle areas" %}

Now dividing both sides of the above inequality by $\sin x > 0$ and taking reciprocals, we obtain

$$\cos x \leq \frac{\sin x}{x} \leq 1$$

Our claim is that $\cos x \rightarrow 1$. To see this, using the half-angle formula for trigonometric functions and the inequality $\sin(x/2) \leq x/2$ obtained above, we have

$$0 \leq \lvert 1 - \cos x\rvert = \left\lvert2\sin^2\frac{x}{2}\right\rvert \leq 2\left(\frac{x}{2}\right)^2 = \frac{x^2}{2}$$

so

$$-\frac{x^2}{2}\leq 1 - \cos x \leq \frac{x^2}{2}$$

and applying [Proposition 8](#prop8) shows that $\cos x \rightarrow 1$. Now using this and applying [Proposition 8](#prop8) again to the earlier inequality, we find that the limit of $(\sin x)/x$ is $1$.
:::

The following example is also classical.

::: Example 11
$\lim_{x\rightarrow 0} x\sin(1/x) = 0$. This is because $\bigl\lvert x\sin(1/x)\bigr\rvert \leq \lvert x\rvert$, so

$$-\lvert x\rvert \leq x\sin\frac1x \leq \lvert x\rvert$$

and both ends go to $0$. On the other hand, $\sin(1/x)$ itself does not have a limit as $x \rightarrow 0$, because it oscillates infinitely between $-1$ and $1$ as $x$ approaches $0$. The factor $x$ suppresses this oscillation to $0$, which is the contribution of the squeeze theorem.
:::

## One-Sided Limits and Limits at Infinity

The limits considered so far were for the case where $x$ approaches $a$ from both sides. By restricting the direction of approach to one side, or extending the definition to the case where $x$ or $f(x)$ grows without bound, we can describe the shape of a function in finer detail.

::: Definition 12
For a real number $a$ and a function $f$, suppose that for some $c > 0$, $f$ is defined on $(a, a+c)$. A real number $L$ is called the *right limit* of $f$ as $x \rightarrow a^+$ if, for every $\epsilon > 0$, there exists a $\delta > 0$ such that

$$a < x < a+\delta \implies \lvert f(x) - L\rvert < \epsilon$$

holds. We write this as $\lim_{x\rightarrow a^+} f(x) = L$. Similarly, when $f$ is defined on $(a-c, a)$, the *left limit* as $x \rightarrow a^-$ is defined by

$$a-\delta < x < a \implies \lvert f(x) - L\rvert < \epsilon$$

and we write $\lim_{x\rightarrow a^-} f(x) = L$.
:::

The existence of the limit $\lim_{x\rightarrow a} f(x)$ is equivalent to both one-sided limits existing and being equal. For example, for $f(x) = \lvert x\rvert/x$, the two one-sided limits are different: $1$ as $x \rightarrow 0^+$ and $-1$ as $x \rightarrow 0^-$, so the limit as $x \rightarrow 0$ does not exist. A point where the two one-sided limits are finite but different is called a *jump* discontinuity of the function.

::: Definition 13
For a function $f$ defined on a deleted neighborhood of a real number $a$, $\lim_{x\rightarrow a} f(x) = \infty$ means that for every $M > 0$, there exists a $\delta > 0$ such that if $0 < \lvert x-a\rvert < \delta$, then $f(x) > M$. Similarly, $\lim_{x\rightarrow a} f(x) = -\infty$ means that for every $M > 0$, there exists a $\delta > 0$ such that if $0 < \lvert x-a\rvert < \delta$, then $f(x) < -M$.
:::

For example, $\lim_{x\rightarrow 0}1/x^2 = \infty$, and in this case the line $x = 0$ is called a *vertical asymptote* of the graph.

::: Definition 14
For a function $f$ defined for $x$ greater than some real number $N_0$, $\lim_{x\rightarrow\infty} f(x) = L$ means that for every $\epsilon > 0$, there exists an $N > N_0$ such that

$$x > N\implies\lvert f(x) - L\rvert < \epsilon$$

Similarly, for a function defined for $x$ less than some $N_0$, $\lim_{x\rightarrow-\infty} f(x) = L$ means that there exists an $N$ such that

$$x < N\implies\lvert f(x) - L\rvert < \epsilon$$
:::

For example, $\lim_{x\rightarrow\infty}1/x = 0$, and for rational functions, the leading term dominates the behavior, so $\lim_{x\rightarrow\infty}(2x^2 + 1)/(3x^2 - x) = 2/3$. If such a finite limit $L$ exists, the line $y = L$ becomes a *horizontal asymptote* of the graph.

When direct substitution yields an indeterminate form of the type $0/0$, we can factor or rationalize the numerator to cancel the zero of the denominator, transforming it into a form to which the limit laws apply. The $\lim(\sin x)/x = 1$ from [Example 10](#ex10) is also combined with such algebraic techniques to handle indeterminate forms involving $\sin$.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
