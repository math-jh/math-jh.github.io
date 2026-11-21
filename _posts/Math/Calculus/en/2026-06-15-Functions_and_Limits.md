---
title: "Limits of Functions"
description: "Defines limits of functions, the starting point of calculus, in epsilon-delta terms. Covers arithmetic limit laws, limits of powers and roots, the squeeze theorem, one-sided limits, and limits at infinity with examples."
excerpt: "Defining function limits using epsilon-delta; proving limit laws and the squeeze theorem"

categories: [Math / Calculus]
permalink: /en/math/calculus/functions_and_limits
sidebar: 
    nav: "calculus-en"

date: 2026-06-15
weight: 1
translated_at: 2026-11-21T03:24:35+00:00
translation_source: antigravity-gemini-3.8-flash-high
last_polished_at: 2026-11-21T19:15:06+00:00
translation_polish_source: antigravity-gemini-3.8-flash-high
---
## Definition of a Limit

Just as we learn in high school, defining differentiation and integration of functions requires the concept of a limit. Compared to then, what makes the limit we deal with now more advanced is that we now *define* the limit.

::: Definition 1
For a real number $a$, any open interval $(c,d)$ ($c<a<d$) containing it is called a *neighborhood* of the point $a$.
:::

For now, this definition of a neighborhood of the point $a$ is sufficient. In particular, for convenience, we call a neighborhood of the point $a$ with $a$ itself removed a *deleted neighborhood*.

::: Definition 2
Suppose that on some deleted neighborhood of a point $a$, a function $f$ is defined. Then a real number $L$ is the *limit* as $x\rightarrow a$ of $f$ if, for every $\epsilon>0$, there exists some $\delta>0$ such that

$$0<\lvert x-a\rvert<\delta \implies \lvert f(x)-L\rvert<\epsilon$$

holds. In this case, we write

$$\lim_{x \rightarrow a}f(x)=L$$
:::

An intuitive explanation of this is as follows. The reason why our high school description of the concept of a limit, saying that $f(x)$ gets *infinitely close* to $L$, cannot serve as a rigorous mathematical definition is that the notion of being *close* is not mathematical. It is for the same reason that, *for example, the collection of numbers close to $L$* does not mathematically define a set.

Intuitively, to resolve this, it helps to think of the $\epsilon$-$\delta$ definition above as a process of reaching an agreement with everyone. That is, no matter *how* close one demands $f(x)$ to be to $L$ (i.e., whatever $\epsilon>0$ is given), as long as we make $x$ sufficiently close to $a$ ($0<\lvert x-a\rvert<\delta$), we can meet that demand $\lvert f(x)-L\rvert<\epsilon$. Let us examine this in the following example.

::: Example 3
For a linear function, $\lvert f(x)-L\rvert$ is a constant multiple of $\lvert x-a\rvert$. For instance, if we take $f(x)=cx+d$ ($c\neq 0$), then for any $\epsilon>0$, if we define $\delta>0$ by $\delta=\epsilon/\lvert c\rvert$, then

$$0<\lvert x-a\rvert<\delta\implies \lvert (cx+d)-(ca+d)\rvert=\lvert c\rvert\lvert x-a\rvert<\lvert c\rvert\delta=\epsilon$$

holds, so we can show that $\lim_{x\rightarrow a}(cx+d)=ca+d=f(a)$. In the case $c=0$ of a constant function $f(x)=d$, $\lvert f(x)-d\rvert$ is independent of $x$ and equals $0$, so for any $\epsilon>0$, no matter what positive $\delta$ we choose, $\lvert f(x)-d\rvert=0<\epsilon$ holds, showing that $\lim_{x\rightarrow a} f(x)=d$.

For general functions, we need to be slightly more careful. For instance, let us consider $g(x) = x^2$ and show that as $x \rightarrow 2$, its limit is $4$. First, we compute

$$\lvert g(x)-4\rvert=\lvert x^2-4\rvert=\lvert x-2\rvert \lvert x+2\rvert$$

The key issue is that while $\lvert x-2\rvert$ is controlled by $\epsilon$, the factor $\lvert x+2\rvert$ multiplying it can grow uncontrollably large as we move away from $x=2$. However, since a limit only looks at what happens in a neighborhood of $x=2$, this is merely a technical issue. If we set $\delta=\min(1,\epsilon/5)>0$, we can ensure that $x$ differs from $2$ by at most $1$, and on this range $\lvert x+2\rvert$ is at most $5$. Therefore, for this $\delta$,

$$0<\lvert x-2\rvert<\delta \implies \lvert x^2-4\rvert<5\delta\leq\epsilon$$

holds.
:::

As seen above, the core of this definition is that we can essentially let $\delta$ be determined by $\epsilon$; continuing the intuition from above, finding a *rule* that, given any $\epsilon>0$, produces a $\delta>0$ satisfying this condition is precisely what we do when we prove the limit of a function.

## Properties of Limits

Based on this, let us now examine the properties of limits. The first property is that if a limit exists, it is unique.

::: Proposition 4 (Uniqueness of limits)
If $\lim_{x\rightarrow a}f(x)= L$ and $\lim_{x\rightarrow a}f(x)=L'$, then $L=L'$.
:::
::: Proof
Suppose for the sake of contradiction that $L\neq L'$. Then $\frac{1}{2}\lvert L-L'\rvert>0$, so let us set $\epsilon$ to this value. Then by [Definition 2](#def2){: data-lid="api8o" }, for this $\epsilon$, there exist $\delta_1,\delta_2>0$ satisfying the following two conditions:

$$0<\lvert x-a\rvert<\delta_1\implies \lvert f(x)-L\rvert<\epsilon, \qquad 0<\lvert x-a\rvert<\delta_2\implies\lvert f(x)-L'\rvert<\epsilon$$

Now, if we set $\delta=\min(\delta_1, \delta_2)$, then whenever $0<\lvert x-a\rvert<\delta$ holds for $x$, the triangle inequality yields

$$\lvert L-L'\rvert\leq\lvert L-f(x)\rvert+\lvert f(x)-L'\rvert<\epsilon+\epsilon=\lvert L- L'\rvert$$

which is a contradiction. Therefore, $L=L'$.
:::

Meanwhile, [Definition 2](#def2){: data-lid="u8ea3" } can, in principle, only be used when a candidate $L$ for the limit of a function is given, to show that its limit is indeed $L$. In other words, it is not a tool that tells us *what* the limit of a function is. For this purpose, the following proposition is useful.

::: Proposition 5 (Limit laws)
Suppose $\lim_{x\rightarrow a}f(x)=L$ and $\lim_{x\rightarrow a}g(x)=M$. Then:

1. $\lim_{x\rightarrow a}\bigl(f(x)+g(x)\bigr)=L+M$,
2. for any constant $c$, $\lim_{x\rightarrow a}cf(x)=cL$,
3. $\lim_{x\rightarrow a}f(x)g(x)=LM$,
4. if $M\neq 0$, then $\lim_{x\rightarrow a}f(x)/g(x)=L/M$.
:::
::: Proof
1. Given $\epsilon>0$, corresponding to $\epsilon/2$ we can obtain $\delta_1, \delta_2>0$ from the definitions of the limits of $f, g$, respectively. Now setting $\delta=\min(\delta_1,\delta_2)$, whenever $0<\lvert x-a\rvert<\delta$,

    $$\lvert(f(x)+g(x))-(L+M)\rvert\leq\lvert f(x)-L\rvert+\lvert g(x)-M\rvert<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon$$

    holds.
2. If $c=0$, the claim is trivial since any $\delta$ works. If $c\neq 0$, for $\epsilon/\lvert c\rvert$, we simply choose a corresponding $\delta$.

3. We use the following inequality:

    $$\lvert f(x)g(x)-LM\rvert=\lvert f(x)(g(x)-M)+M(f(x)-L)\rvert \leq \lvert f(x)\rvert\lvert g(x)-M\rvert+\lvert M\rvert\lvert f(x)-L\rvert$$

    Then intuitively, as $x$ approaches $a$, both $\lvert g(x)-M\rvert$ and $\lvert f(x)-L\rvert$ approach $0$; hence, provided that the factors $\lvert f(x)\rvert, \lvert g(x)\rvert$ in front are guaranteed to be finite, we can make this smaller than $\epsilon$ by a calculation similar to (1) above.

    The trick is to set $\epsilon=1$ and apply [Definition 2](#def2){: data-lid="gyq6x" } to $f$ and $g$ separately. Then there exist suitable $\delta_1, \delta_2$ such that

    $$0<\lvert x-a\rvert<\delta_1\implies \lvert f(x)-L\rvert<1\implies \lvert f(x)\rvert< \lvert L\rvert+1$$

    and similarly we can also ensure $\lvert g(x)\rvert <\lvert M\rvert+1$ by choosing $\delta_2$. Now we simply choose $\delta$ so that these two conditions and the following two conditions

    $$\lvert g(x)-M\rvert < \frac{\epsilon}{2(\lvert L\rvert+1)},\qquad \lvert f(x)-L\rvert < \frac{\epsilon}{2(\lvert M\rvert+1)}$$

    all hold.

4. It suffices to show that $1/g(x) \rightarrow 1/M$ and then apply (3). Since $M \neq 0$, near $a$ we have $\lvert g(x)\rvert > \lvert M\rvert/2$, and

    $$\left\lvert \frac{1}{g(x)} - \frac{1}{M}\right\rvert = \frac{\lvert g(x)-M\rvert}{\lvert g(x)\rvert \lvert M\rvert} < \frac{2}{\lvert M\rvert^2}\lvert g(x)-M\rvert$$

    so it suffices to make $\lvert g(x)-M\rvert$ sufficiently small.
:::

Then the following holds.

::: Corollary 6 (Limits of powers and roots)
If $\lim_{x\rightarrow a} f(x)=L$, then:

1. for any positive integer $k$, $\lim_{x\rightarrow a} \bigl(f(x)\bigr)^k=L^k$,
2. if $L>0$, then for any positive integer $k$, $\lim_{x\rightarrow a} \sqrt[k]{f(x)}=\sqrt[k]{L}$.
:::
::: Proof
1. Apply part (3) of [Proposition 5](#prop5){: data-lid="l1jgq" } and proceed by induction on $k$.
2. First, since $L>0$, choosing $\delta_1>0$ corresponding to $\epsilon_1=L/2$ gives

    $$0<\lvert x-a\rvert<\delta_1\implies\lvert f(x)-L\rvert<L/2$$

    and hence $f(x)>L/2>0$. On the other hand, for any positive real numbers $u,v$, consider the expansion

    $$u-v=\bigl(u^{1/k}-v^{1/k}\bigr)\bigl(u^{(k-1)/k}+u^{(k-2)/k}v^{1/k}+\cdots+v^{(k-1)/k}\bigr)$$

    Because each term in the second factor on the right-hand side is greater than or equal to $(\min(u,v))^{(k-1)/k}$, it follows that

    $$\bigl\lvert u^{1/k}-v^{1/k}\bigr\rvert \leq \frac{\lvert u-v\rvert}{k(\min(u,v))^{(k-1)/k}}$$

    Therefore, whenever $0 < \lvert x-a\rvert < \delta_1$, we have $0<L/2 < \min(f(x), L)$, and this inequality yields

    $$\bigl\lvert\sqrt[k]{f(x)}-\sqrt[k]{L}\bigr\rvert\leq\frac{\lvert f(x)-L\rvert}{k(\min(f(x),L))^{(k-1)/k}}\leq\frac{\lvert f(x)-L\rvert}{k(L/2)^{(k-1)/k}}$$

    Now, for any $\epsilon>0$, choose $\delta_2>0$ corresponding to $k(L/2)^{(k-1)/k}\epsilon$ and set $\delta=\min(\delta_1,\delta_2)$; then for $0<\lvert x-a\rvert<\delta$, the right-hand side is less than $\epsilon$.
:::

Combining these laws, we can compute the limit of a polynomial function by splitting it into the limits of its individual terms. The base step for this is [Example 3](#ex3){: data-lid="jql4u" }.

::: Example 7
By [Example 3](#ex3){: data-lid="yahaj" }, we know in particular that the limits

$$\lim_{x\rightarrow a} x=a,\qquad \lim_{x\rightarrow a}c=c$$

hold. Therefore, for any polynomial function

$$f(x)=c_nx^n+\cdots +c_1x+c_0$$

applying [Proposition 5](#prop5){: data-lid="bkyke" } to split the limit across each term and [Corollary 6](#cor6){: data-lid="kc5tq" } to the powers gives

$$\lim_{x\rightarrow a}f(x)=c_n\Bigl(\lim_{x\rightarrow a}x\Bigr)^n+\cdots+c_1\Bigl(\lim_{x\rightarrow a}x\Bigr)+\lim_{x\rightarrow a}c_0$$

and thus substituting the computations above yields

$$\lim_{x\rightarrow a}f(x)=c_n\Bigl(\lim_{x\rightarrow a}x\Bigr)^n+\cdots+c_1\Bigl(\lim_{x\rightarrow a}x\Bigr)+\lim_{x\rightarrow a}c_0=c_na^n+\cdots+c_1a+c_0=f(a)$$

In a similar way, the limit of a rational function, formed as a ratio of polynomial functions, is also obtained as the ratio of the limits of the numerator and the denominator, provided that the limit of the denominator is not $0$.
:::

## The Squeeze Theorem and Order Relations for Limits

With the limit laws and computable expressions we currently have, results like [Example 7](#ex7){: data-lid="ep8wd" } are close to the extent of what we can derive. For computations involving more general functions, we sometimes need calculations using inequalities, such as the following.

::: Proposition 8 (Squeeze theorem)
Suppose that on a deleted neighborhood of a real number $a$, we have $g(x) \leq f(x)\leq h(x)$, and that $\lim_{x\rightarrow a} g(x)=\lim_{x\rightarrow a} h(x)=L$. Then $\lim_{x\rightarrow a} f(x)=L$.
:::
::: Proof
For $\epsilon>0$, the definitions of the limits of $g$ and $h$ yield $\delta_1, \delta_2$, and the inequality $g\leq f\leq h$ holds on a neighborhood of radius $\delta_3$; set $\delta=\min(\delta_1,\delta_2,\delta_3)$. Whenever $0<\lvert x-a\rvert<\delta$, we have $L-\epsilon<g(x)\leq f(x)\leq h(x)<L+\epsilon$, and hence $\lvert f(x)-L\rvert<\epsilon$.
:::

Another basic fact that is useful when applying inequalities to the computation of limits is that limits preserve order.

::: Proposition 9 (Order preservation of limits)
Suppose that on a deleted neighborhood of a real number $a$, we have $f(x)\leq g(x)$, and that the two limits $L=\lim_{x\rightarrow a}f(x)$ and $M=\lim_{x\rightarrow a}g(x)$ exist. Then $L\leq M$.
:::
::: Proof
Suppose for contradiction that $L > M$, and set $\epsilon=\frac{1}{2}(L-M)>0$. On a sufficiently small neighborhood, we have $f(x)>L-\epsilon=\frac{L+M}{2}$ and $g(x)<M+\epsilon=\frac{L+M}{2}$, so $f(x)>g(x)$, contradicting our assumption. Hence $L\leq M$.
:::

Note that even if we replace the hypothesis with the inequality $f<g$, the result does not yield the inequality $L<M$. For instance, for $x\neq 0$ we have $f(x)=0<x^2=g(x)$, yet as $x \rightarrow 0$ both limits are equal to $0$.

The most famous application of the squeeze theorem is the following trigonometric limit, which plays a decisive role in deriving the differentiation formulas for trigonometric functions.

::: Example 10
We have $\lim_{x\rightarrow 0}(\sin x)/x=1$. To show this, we first compare areas on the unit circle for $0<x<\pi/2$ to obtain the inequality

$$\frac{1}{2}\sin x\leq\frac{1}{2}x\leq\frac{1}{2}\tan x$$

that is, $\sin x\leq x\leq\tan x$.

{% diagram Math/Calculus/functions_and_limits-1.svg width="33.66em" alt="Area comparison of a triangle, a circular sector, and a right triangle" %}

Now, dividing the inequality above by $\sin x>0$ and taking reciprocals, we see that

$$\cos x\leq \frac{\sin x}{x}\leq 1 \tag{$\ast$}$$

Although this inequality was obtained for $0<x<\pi/2$, since $\cos(-x)=\cos x$ and $\sin(-x)/(-x)=(\sin x)/x$, it continues to hold for $-\pi/2<x<0$, and thus throughout $0<\lvert x\rvert<\pi/2$. Meanwhile, the inequality $\sin x \leq x$ obtained above also extends via $\sin(-t)=-\sin t$: whenever $0<\lvert t\rvert<\pi/2$, $t$ satisfies $\lvert \sin t\rvert \leq\lvert t\rvert$.

We claim that as $x\rightarrow 0$, we have $\cos x \rightarrow 1$. To show this, we use the trigonometric half-angle formula together with the inequality $\lvert\sin(x/2)\rvert \leq \lvert x/2\rvert$ obtained above to get

$$0 \leq \lvert 1-\cos x\rvert = \left\lvert 2\sin^2\frac{x}{2}\right\rvert \leq 2\left(\frac{x}{2}\right)^2=\frac{x^2}{2}$$

so that

$$-\frac{x^2}{2}\leq 1-\cos x \leq \frac{x^2}{2}$$

and applying [Proposition 8](#prop8){: data-lid="cglpa" } shows that $\cos x \rightarrow 1$. Now, using this, we apply [Proposition 8](#prop8){: data-lid="629s1" } once more to ($\ast$) to see that the limit of $(\sin x)/x$ is $1$.
:::

The following example is also classic.

::: Example 11
We have $\lim_{x\rightarrow 0} x\sin(1/x) = 0$. This holds because $\bigl\lvert x\sin(1/x)\bigr\rvert \leq \lvert x\rvert$, which gives

$$-\lvert x\rvert \leq x\sin\frac{1}{x} \leq \lvert x\rvert$$

and both outer expressions tend to $0$. On the other hand, $\sin(1/x)$ itself has no limit as $x \rightarrow 0$, since as $x$ approaches $0$ it oscillates infinitely many times between $-1$ and $1$. The way the squeeze theorem works is that the factor $x$ damps this oscillation down to $0$.
:::

## One-Sided Limits and Limits at Infinity

So far, we have considered limits in which $x$ approaches $a$ from both sides. By restricting the direction of approach to one side, or by extending the definition to the cases where $x$ or $f(x)$ grows without bound, we can describe the behavior of a function in finer detail.

::: Definition 12
For a real number $a$ and a function $f$, suppose that for some $c>0$, $f$ is defined on the interval $(a, a+c)$. We say that a real number $L$ is the *right limit* as $x \rightarrow a^+$ of $f$ if, for every $\epsilon>0$, there exists some $\delta>0$ such that

$$a<x<a+\delta \implies \lvert f(x)-L\rvert<\epsilon$$

holds. In this case, we write $\lim_{x\rightarrow a^+} f(x)=L$. Similarly, when $f$ is defined on the interval $(a-c, a)$, the *left limit* as $x \rightarrow a^-$ is defined by

$$a-\delta<x<a \implies \lvert f(x)-L\rvert<\epsilon$$

and we write $\lim_{x\rightarrow a^-} f(x)=L$.
:::

The limit $\lim_{x\rightarrow a} f(x)$ exists if and only if both one-sided limits exist and are equal. For example, for $f(x)=\lvert x\rvert/x$, the limit as $x \rightarrow 0^+$ is $1$ and the limit as $x \rightarrow 0^-$ is $-1$; since the two one-sided limits differ, the limit as $x \rightarrow 0$ does not exist.

We also make the following definition.

::: Definition 13
For a real number $a$ and a function $f$ defined on a deleted neighborhood of that point, $\lim_{x\rightarrow a} f(x)=\infty$ means that for every $M>0$ there exists some $\delta>0$ such that $0<\lvert x-a\rvert<\delta$ implies $f(x)>M$. Similarly, $\lim_{x\rightarrow a} f(x)=-\infty$ means that for every $M>0$ there exists some $\delta>0$ such that $0<\lvert x-a\rvert<\delta$ implies $f(x)<-M$.
:::

For instance, $\lim_{x\rightarrow 0}1/x^2=\infty$, and in this case the line $x=0$ is called a *vertical asymptote* of the graph. We can similarly define the notion of a horizontal asymptote, but since this requires $x$ to tend to $\pm\infty$, a definition of a somewhat different form from the limits defined above is needed.

::: Definition 14
Given some real number $N_0$, suppose that for all $x$ greater than it, a function $f$ is defined. Then $\lim_{x\rightarrow\infty} f(x)=L$ means that for every $\epsilon>0$ there exists some $N>N_0$ such that

$$x>N\implies\lvert f(x)-L\rvert<\epsilon$$

holds. Similarly, given some $N_0$, for a function defined for all $x$ less than it, $\lim_{x\rightarrow-\infty} f(x)=L$ means that

$$x<N\implies\lvert f(x)-L\rvert<\epsilon$$

holds for some $N<N_0$.
:::

For example, $\lim_{x\rightarrow\infty}1/x=0$. If such a finite limit $L$ exists, then the line $y = L$ is a *horizontal asymptote* of the graph.

---

**References**

**[Ste]** J. Stewart, *Calculus*, 8th ed., Cengage Learning, 2016.  
**[Kim]** 김홍종, *미적분학 1·2*, 제3개정판, 서울대학교출판문화원, 2020.
