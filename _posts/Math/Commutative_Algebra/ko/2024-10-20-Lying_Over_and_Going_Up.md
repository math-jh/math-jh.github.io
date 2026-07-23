---
title: "정수적 확장과 아이디얼"
description: "정수적 확장에서 lying over과 going up 정리를 증명하며, 소 아이디얼의 원상 존재성과 포함 관계를 다룬다. 대수적 확장에서의 아이디얼 교차 성질도 확인한다."
excerpt: "Integral extension 하 prime ideal의 lying over와 going up 정리"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/lying_over_and_going_up
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-10-20
weight: 9

toc: false

---

## Lying over, going up

::: 명제 1
Integral extension $A\hookrightarrow B$가 주어졌다 하자.

1. (Lying over) $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여, 적당한 $B$의 prime ideal $\mathfrak{q}$가 존재하여 $\mathfrak{q}\cap A=\mathfrak{p}$이도록 할 수 있다.
2. (Going up) 위의 명제에서 얻어지는 $\mathfrak{q}$는 $\mathfrak{b}\cap A\subseteq \mathfrak{p}$를 만족하는 $B$의 임의의 ideal $\mathfrak{b}$가 주어질 때마다, $\mathfrak{b}\subseteq \mathfrak{q}$이도록 잡을 수 있다. 
:::
::: 증명
우선 둘째 결과에서, 만일 $A\hookrightarrow B$가 integral extension이라면 $B$의 임의의 ideal $\mathfrak{b}$에 대하여 다음의 ring homomorphism

$$\frac{A}{A\cap \mathfrak{b}}\hookrightarrow \frac{B}{\mathfrak{b}}$$ 

또한 integral extension인 것을 안다. 따라서, 일반성을 잃지 않고 $\mathfrak{b}=0$이라 가정해도 충분하고, 이는 정확히 첫째 결과를 보이는 것과 같다.

따라서 주어진 prime ideal $\mathfrak{p}\subseteq A$에 대하여, $\mathfrak{q}\cap A=\mathfrak{p}$를 만족하는 $B$의 prime ideal $\mathfrak{q}$를 찾으면 충분하다. 

한편, $S=A\setminus \mathfrak{p}$라 하면, $A \hookrightarrow B$가 integral이라면 $S^{-1}A \rightarrow S^{-1}B$ 또한 그러하다. 따라서 $A$가 maximal ideal $\mathfrak{p}$를 갖는 local ring인 경우만 생각하면 충분하다. 이러한 상황에서, $\mathfrak{p}B$를 포함하는 $B$의 maximal ideal의 preimage는 반드시 $\mathfrak{p}$가 되어야 하므로, $\mathfrak{p}B=B$가 아닌 한 이 maximal ideal이 우리가 찾는 $B$의 prime ideal이 된다. 

결론에 반하여 $\mathfrak{p}B=B$라 가정하자. 그럼 $1\in B$는 $\mathfrak{p}$의 원소들의 $B$-linear combination

$$1=\sum_{i=1}^n b_i a_i,\qquad a_i\in \mathfrak{p},\quad b_i\in B$$

으로 쓰여질 수 있다. 이제 $b_i$들로 생성되는 $B$의 $A$-subalgebra를 $B'$라 하자. 그럼 $B'$의 모든 원소는 integral이며, $B'$는 $A$-algebra로서 유한하게 생성된다. 따라서 [§정수적 확장, ⁋보조정리 4](/ko/math/commutative_algebra/integral_extension#lem4)에 의하여 $B'$는 $A$-module로서 유한하게 생성된다. 이제 [§정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)을 적용하면 $B'=0$이므로 모순이다. 
:::

이 글의 중요한 부분은 [따름정리 4](#cor4)를 증명하는 것으로, 대략적으로 [명제 1](#prop1)을 통해 $A$의 prime ideal $\mathfrak{p}$ 위에 있는 $B$의 두 prime ideal $\mathfrak{q}_1, \mathfrak{q}_2$가 주어졌다면 이들은 서로를 포함하지 않는다는 것이다. 

::: 보조정리 2
두 integral domain $A\subseteq B$에 대하여, 만일 $\Frac(A) \rightarrow \Frac(B)$가 algebraic extension이라면 $B$의 임의의 nonzero ideal은 $A$와 nontrivial하게 만난다.
:::
::: 증명
이를 위해서는 $B$의 principal ideal들만 생각하면 충분하다. $b\in B$로 생성되는 임의의 principal ideal을 생각하자. 그럼 $\Frac(B)$가 $\Frac(A)$의 algebraic extension이므로, 

$$a_nb^n+\cdots+a_1b+a_0=0,\qquad a_i\in \Frac(A)$$

이도록 할 수 있다. 이제 $a_i$들의 분모들의 최소공배수를 양변에 곱하고, 필요하다면 $b$의 거듭제곱으로 양변을 적절히 나눠서 각각의 $a_i$들이 모두 $A$의 원소이고, $a_0\neq 0$이도록 할 수 있다. 그럼 $a_0$은 $b$로 생성되는 principal ideal에 속한다.
:::

::: 따름정리 3
Integral domain $A$가 주어졌다 하고, integral extension $A \rightarrow B$가 주어졌다 하자. 그럼 $B$의 prime ideal $\mathfrak{q}$이 maximal ideal인 것과 $\mathfrak{q}\cap A$가 $A$의 maximal ideal인 것이 동치이다.
:::
::: 증명
이 또한 [명제 1](#prop1)의 증명에서와 마찬가지로, $\mathfrak{q}\cap A$와 $\mathfrak{q}$로 각각 quotient를 취해주면, 두 integral domain $A,B$ 그리고 integral extension $A \hookrightarrow B$가 주어졌을 때, $A$가 field인 것과 $B$가 field인 것이 동치라는 것을 보이면 충분하다. 한편, 만일 $A$가 field라면 [보조정리 2](#lem2)에 의하여 $B$는 nonzero ideal을 갖지 않아야 한다. 즉, $B$는 field이다. 

따라서 $B$가 field임을 가정하고 $A$가 field임을 보이면 충분하다. $A$의 maximal ideal $\mathfrak{m}$이 주어졌다 하자. 그럼 [명제 1](#prop1)에 의하여, 우리는 적당한 $B$의 prime ideal $\mathfrak{q}$가 존재하여 $\mathfrak{q}\cap A= \mathfrak{m}$이 성립하도록 할 수 있다. 그런데 $B$는 field이므로, $\mathfrak{q}=0$이고 따라서 $\mathfrak{m}=0$이다. 이로부터 원하는 결과를 얻는다. 
:::

마지막으로 다음을 살펴보자. 

::: 따름정리 4
Integral extension $A\hookrightarrow B$에 대하여, 만일 $B$의 두 prime ideal $\mathfrak{q}_1\neq \mathfrak{q}_2$이 $A\cap \mathfrak{q}_1=A\cap \mathfrak{q}_2=\mathfrak{p}$를 만족한다면 $\mathfrak{q}_1\not\subseteq \mathfrak{q}_2$이고 $\mathfrak{q}_2\not\subseteq \mathfrak{q}_1$이다.
:::
::: 증명
결론에 반하여 $\mathfrak{q}_1\subseteq \mathfrak{q}_2$라 가정하고 $A\cap \mathfrak{q}_1=A\cap \mathfrak{q}_2=\mathfrak{p}$라 하자. 그럼 $A$에서는 $\mathfrak{p}$로, $B$에서는 $\mathfrak{q}_1$으로 quotient를 취하여, 주어진 상황을 integral domain $B$와 $\mathfrak{q}_1=0$, 그리고 $\mathfrak{q}_2\cap A=0$이 성립하도록 바꿔줄 수 있다. 그런데 $B$의 원소들에 대해 성립하는 integral equation들은 $\mathfrak{p}$로 quotient를 취하여도 그대로 integral equation이 되며, 특히 $\Frac(B)$가 $\Frac(A)$의 algebraic extension이 된다. 따라서 [보조정리 2](#lem2)에 의하여 원하는 결과를 얻는다.
:::

[명제 1](#prop1)과 [따름정리 4](#cor4)가 prime ideal chain을 위로 올리는 방향이라면, 반대 방향의 *going-down*은 일반적인 integral extension에서는 성립하지 않는다. 다만 base가 integrally closed일 때 성립하며, 그 증명은 다음 보조정리에 기반한다.

::: 보조정리 5
Integral extension $A\hookrightarrow B$에서 $A$가 integrally closed domain이고 $B$도 domain이라 하자. 임의의 $b\in B$의 $K=\Frac(A)$ 위 minimal polynomial을 $f_b\in K[\x]$라 하자.

1. $f_b$의 모든 계수는 $A$에 속한다.
2. $b\in\mathfrak{p}B$를 만족하는 $A$의 prime ideal $\mathfrak{p}$가 주어지면, $f_b$의 최고차항 계수가 아닌 계수들은 모두 $\mathfrak{p}$에 속한다.
:::
::: 증명
$b$가 integral이므로 $b$를 root로 갖는 monic 다항식 $g\in A[\x]$가 존재한다. $K[\x]$에서 $f_b\mid g$이며, $f_b$의 root들은 모두 $g$의 root여서 $A$ 위에서 integral이다. 따라서 이 root들의 대칭식인 $f_b$의 계수들도 $A$ 위에서 integral이고, $A$가 integrally closed이므로 $A$에 속한다.

이제 $b\in\mathfrak{p}B$라 하자. $b=\sum_i p_i b_i$ ($p_i\in\mathfrak{p}, b_i\in B$)라 적고, $b_i$들이 생성하는 $B$의 $A$-subalgebra를 $B'$라 하면 $B'$은 finitely generated $A$-module이다. $b\in\mathfrak{p}B'$이므로 [\[가환대수학\] §정수적 확장, ⁋보조정리 8](/ko/math/commutative_algebra/integral_extension#lem8)에 의하여 $b$를 root로 갖고 최고차항이 아닌 계수들이 모두 $\mathfrak{p}$에 속하는 monic 다항식 $g\in A[\x]$를 얻는다. 앞서 보인 바에 의해 $h=g/f_b\in A[\x]$이고, $g=f_b h$를 $\mathfrak{p}$로 나누면 $(A/\mathfrak{p})[\x]$에서 $\x^{\deg g}=\overline{f_b}\overline{h}$가 된다. $A/\mathfrak{p}$가 domain이므로 $\overline{f_b}$는 $\x$의 거듭제곱이어야 하며, 이는 $f_b$의 최고차항 계수가 아닌 계수들이 $\mathfrak{p}$에 속함을 뜻한다.
:::

::: 정리 6 (Going down)
Integral extension $A\hookrightarrow B$에서 $A$가 integrally closed domain이고 $B$가 domain이라 하자. $A$의 prime ideal $\mathfrak{p}_1\subseteq\mathfrak{p}_2$와 $\mathfrak{q}_2\cap A=\mathfrak{p}_2$를 만족하는 $B$의 prime ideal $\mathfrak{q}_2$가 주어졌다 하자. 그럼 $\mathfrak{q}_1\subseteq\mathfrak{q}_2$이고 $\mathfrak{q}_1\cap A=\mathfrak{p}_1$인 $B$의 prime ideal $\mathfrak{q}_1$이 존재한다.
:::
::: 증명
$B$가 domain이므로 $B\hookrightarrow B_{\mathfrak{q}_2}$이고, 이와 $A\hookrightarrow B$를 합성하여 ring extension $A\hookrightarrow B_{\mathfrak{q}_2}$를 얻는다. [명제 1](#prop1)의 증명에서 쓰인 것과 같은 논증으로, $\mathfrak{p}_1 B_{\mathfrak{q}_2}\cap A\subseteq\mathfrak{p}_1$을 보이면 $\mathfrak{p}_1$ 위에 lying over하는 $B_{\mathfrak{q}_2}$의 prime ideal이 존재한다. 이는 $B$의 $\mathfrak{q}_2$에 포함된 prime ideal $\mathfrak{q}_1$에 해당하므로 원하는 결과를 얻는다.

$a\in\mathfrak{p}_1 B_{\mathfrak{q}_2}\cap A$라 하자. $a=p/s$ ($p\in\mathfrak{p}_1 B$, $s\in B\setminus\mathfrak{q}_2$)로 쓰고 $a\neq 0$이라 가정하자. [보조정리 5](#lem5)에 의해 $p$의 minimal polynomial $f=\x^n+c_{n-1}\x^{n-1}+\cdots+c_0$는 모든 $c_i\in\mathfrak{p}_1$을 만족한다. 한편 $a\in A\subseteq K$이고 $p=as$이므로, $f$에 치환 $\x\mapsto a\x$을 하고 정규화한 다항식

$$\frac{1}{a^n}f(a\x)=\x^n+\frac{c_{n-1}}{a}\x^{n-1}+\cdots+\frac{c_0}{a^n}$$

은 $K$ 위에서 기약이며 $s$를 root로 갖는다. 즉 이것이 $s$의 minimal polynomial이고, [보조정리 5](#lem5)에 의해 계수들이 $A$에 속한다. 이를 $\x^n+c'_{n-1}\x^{n-1}+\cdots+c'_0$이라 쓰면 $c'_{n-i}a^i=c_{n-i}\in\mathfrak{p}_1$이다. 만일 $a\notin\mathfrak{p}_1$이라면 $\mathfrak{p}_1$이 prime이므로 모든 $c'_{n-i}\in\mathfrak{p}_1$이고, 따라서 $s^n=-c'_{n-1}s^{n-1}-\cdots-c'_0\in\mathfrak{p}_1 B\subseteq\mathfrak{q}_2$가 되어 $\mathfrak{q}_2$가 prime이라는 사실과 모순이다. 그러므로 $a\in\mathfrak{p}_1$이다.
:::

---

**참고문헌**

**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---