---
title: "완비 거리공간과 축소사상 정리"
description: "거리공간에서 Cauchy 수열이 항상 수렴할 때 완비라고 하며, R^n과 sup 거리를 준 C[a,b]가 완비임을 증명한다. 완비 거리공간 위의 축소사상이 fixed point를 유일하게 가짐을 보이고 반복법의 오차 추정을 얻은 뒤, 가정이 빠지면 정리가 무너지는 반례와 cos x = x에의 적용을 다룬다. 마지막으로 Baire 범주정리를 증명하고 R의 비가산성을 이끌어낸다."
excerpt: "완비 거리공간, C[a,b]의 완비성, Banach 고정점 정리와 오차 추정, 가정의 반례, cos x = x, Baire 범주정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/contraction_mapping
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 9

published: false

---

[§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="lnyuz" }에서 실수의 Cauchy 수열은 항상 수렴함을 보았다. 이 성질은 극한값을 미리 알지 못해도 수렴을 판정할 수 있게 해 주며, 실수의 순서 구조가 아니라 거리만으로 서술되므로 일반적인 [§거리공간과 열린집합·닫힌집합, ⁋정의 1](/ko/math/analysis/metric_spaces#def1){: data-lid="rlghh" }의 거리공간으로 그대로 옮겨진다. 이 글에서는 이 성질을 가진 거리공간을 완비 거리공간으로 부르고, 그 위에서 성립하는 두 가지 정리를 증명한다. 하나는 축소사상이 유일한 fixed point을 가지며 그 fixed point이 반복으로 계산된다는 Banach fixed point 정리이고, 다른 하나는 완비 거리공간이 가산 개의 '얇은' 집합으로 덮이지 않는다는 Baire 범주정리이다.

## 완비 거리공간

거리공간 $(X,d)$의 수열 $(x_n)$이 *Cauchy 수열<sub>Cauchy sequence</sub>*이라는 것은, 임의의 $\varepsilon>0$에 대해 어떤 $N$이 있어 $m,n\ge N$이면 $d(x_m,x_n)<\varepsilon$이 성립한다는 뜻이다. 수렴하는 수열은 항상 Cauchy 수열이다. 극한을 $x$라 하면 $m,n\ge N$에서 $d(x_m,x_n)\le d(x_m,x)+d(x,x_n)$이 $\varepsilon$ 미만이 되도록 $N$을 잡을 수 있기 때문이다. 역은 일반적으로 성립하지 않는다.

::: 정의 1
거리공간 $(X,d)$의 모든 Cauchy 수열이 $X$의 점으로 수렴하면 $(X,d)$를 *완비 거리공간<sub>complete metric space</sub>*이라 한다.
:::

완비성은 위상이 아니라 거리의 성질이다. [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="ktj4x" }에 의하여 $\mathbb{R}$은 완비이지만 $\mathbb{R}$과 homeomorphic한 $(0,1)$은 보통의 거리에서 완비가 아니다. $x_n = 1/n$은 $(0,1)$에서 Cauchy 수열이지만 극한 $0$이 $(0,1)$ 밖에 있다. 같은 이유로 $(0,1]$도 완비가 아니다. 유리수 집합 $\mathbb{Q}$도 완비가 아니다. $\sqrt{2}$의 decimal expansion를 소수점 아래 $n$째 자리에서 끊은 수열은 $\mathbb{Q}$의 Cauchy 수열이지만 $\mathbb{Q}$에서는 [§실수의 완비성, ⁋예시 5](/ko/math/analysis/completeness_of_reals#ex5){: data-lid="qq1o1" }에 의하여 극한이 없다.

완비인 대표적인 공간은 $\mathbb{R}$이다. $\mathbb{R}^n$도 보통의 거리 $\lVert x-y\rVert$에서 완비이다. $(x^{(m)})$이 $\mathbb{R}^n$의 Cauchy 수열이면, 각 좌표 $i$에 대해 $\lvert x^{(m)}_i - x^{(l)}_i\rvert\le \lVert x^{(m)}-x^{(l)}\rVert$이므로 $(x^{(m)}_i)_m$은 $\mathbb{R}$의 Cauchy 수열이고 [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="w6m1k" }에 의하여 어떤 $x_i$로 수렴한다. $x=(x_1,\dots,x_n)$이라 하면 $\lVert x^{(m)}-x\rVert^2$은 $n$개의 항 $\lvert x^{(m)}_i-x_i\rvert^2$의 합이고 각 항이 $0$으로 가므로 $x^{(m)}\to x$이다.

완비 공간의 subset이 언제 다시 완비인지는 다음과 같이 정리된다.

::: 명제 2
완비 거리공간 $X$의 subset $A$가 $X$의 거리를 물려받을 때, $A$가 $X$에서 닫힌집합이면 $A$는 완비이다. 역으로 $A$가 완비이면 $A$는 $X$에서 닫혀 있다.
:::

::: 증명
$A$가 닫혀 있다고 하고 $(a_n)$을 $A$의 Cauchy 수열이라 하자. 이는 $X$의 Cauchy 수열이기도 하므로 어떤 $x\in X$로 수렴한다. [§거리공간과 열린집합·닫힌집합, ⁋명제 12](/ko/math/analysis/metric_spaces#prop12){: data-lid="2f9lw" }에 의하여 닫힌집합은 그 점들의 수열의 극한을 포함하므로 $x\in A$이다. 역으로 $A$가 완비이고 $a_n\in A$가 $x\in X$로 수렴하면, $(a_n)$은 수렴하므로 Cauchy 수열이고 $A$의 완비성에 의해 $A$의 어떤 점 $a$로 수렴한다. [§거리공간과 열린집합·닫힌집합, ⁋명제 7](/ko/math/analysis/metric_spaces#prop7){: data-lid="24l6q" }에 의하여 $x=a\in A$이므로 $A$는 닫혀 있다.
:::

특히 $[1,\infty)$, $[a,b]$는 $\mathbb{R}$의 닫힌집합이므로 완비이다.

### 함수공간 C[a,b]

완비성이 가장 많이 쓰이는 곳은 함수들로 이루어진 공간이다. $C[a,b]$를 $[a,b]$에서 정의된 실숫값 연속함수 전체의 집합이라 하자. 연속함수는 [\[미적분학\] §연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4){: data-lid="sdrjn" }에 의하여 $[a,b]$에서 유계이므로 

$$d(f,g)=\sup_{x\in[a,b]}\lvert f(x)-g(x)\rvert$$

는 유한하고, 이것이 $C[a,b]$ 위의 [§거리공간과 열린집합·닫힌집합, ⁋정의 1](/ko/math/analysis/metric_spaces#def1){: data-lid="qihkj" }의 거리가 됨은 삼각부등식이 각 점에서의 삼각부등식에서 나오는 것으로 확인된다. 이 거리에 대한 수렴 $d(f_n,f)\to0$은 $f_n$이 $f$로 $[a,b]$ 전체에서 한꺼번에 수렴한다는 뜻이다.

::: 명제 3
$C[a,b]$는 $d$에 대해 완비 거리공간이다.
:::

::: 증명
$(f_n)$을 $C[a,b]$의 Cauchy 수열이라 하자. 극한 후보를 점별로 만들고, 그것이 연속이며 $d$에 대해서도 수렴함을 차례로 확인한다.

먼저 각 $x\in[a,b]$에 대해 $\lvert f_n(x)-f_m(x)\rvert\le d(f_n,f_m)$이므로 $(f_n(x))_n$은 $\mathbb{R}$의 Cauchy 수열이고, $\mathbb{R}$이 완비이므로 [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="eesnt" }에 의하여 수렴한다. 그 극한을 $f(x)$로 정의한다.

다음으로 $d(f_n,f)\to0$을 보인다. $\varepsilon>0$이 주어졌을 때 $m,n\ge N$이면 $d(f_n,f_m)<\varepsilon$이 되도록 $N$을 잡는다. $n\ge N$과 $x\in[a,b]$를 고정하면 모든 $m\ge N$에 대해 $\lvert f_n(x)-f_m(x)\rvert<\varepsilon$이다. 여기서 $m\to\infty$로 보내면 [§수열의 수렴, ⁋명제 6](/ko/math/analysis/convergence_of_sequences#prop6){: data-lid="trf1o" }에 의하여 $\lvert f_n(x)-f(x)\rvert\le\varepsilon$이다. $x$는 임의이므로 $n\ge N$에서 $\sup_x\lvert f_n(x)-f(x)\rvert\le\varepsilon$이다. 이 단계에서는 $f$가 $C[a,b]$에 속하는지를 아직 모르므로 $d(f_n,f)$가 아니라 상한 자체로 적었다.

마지막으로 $f$가 연속임을 보인다. $x_0\in[a,b]$와 $\varepsilon>0$이 주어졌다고 하자. 위 단계를 $\varepsilon/3$에 적용해, 모든 $x$에 대해 $\lvert f_n(x)-f(x)\rvert\le\varepsilon/3$이 되는 $n$을 하나 고정한다. $f_n$은 연속이므로 $\lvert x-x_0\rvert<\delta$이면 $\lvert f_n(x)-f_n(x_0)\rvert<\varepsilon/3$이 되는 $\delta>0$가 있다. 이때 $\lvert x-x_0\rvert<\delta$이면

$$\begin{aligned}
\lvert f(x)-f(x_0)\rvert &\le \lvert f(x)-f_n(x)\rvert+\lvert f_n(x)-f_n(x_0)\rvert+\lvert f_n(x_0)-f(x_0)\rvert \\
&<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon
\end{aligned}$$

이다. 오차를 세 부분으로 나누는 이유는 $f$를 $f_n$으로 바꾸는 두 번의 비용(점 $x$와 점 $x_0$에서 각각 한 번)과 $f_n$ 자체의 연속성에서 오는 비용이 모두 $\varepsilon$ 이하여야 하기 때문이다. 앞의 두 비용은 같은 $n$으로 모든 점에서 동시에 작아야 하며, 이것이 점별 수렴이 아니라 위의 $\sup$ 추정이 필요한 이유이다. 따라서 $f\in C[a,b]$이고, 앞 단계의 추정은 $n\ge N$에서 $d(f_n,f)\le\varepsilon$을 뜻한다.
:::

## 축소사상과 고정점 정리

방정식 $f(x)=x$의 해를 *fixed point<sub>고정점</sub>*이라 한다. $f$를 반복해서 적용하는 수열 $x_{n+1}=f(x_n)$이 수렴한다면 그 극한은 $f$가 연속인 한 fixed point이다. 이 수열이 언제 수렴하는지는 $f$가 점들 사이의 거리를 얼마나 줄이는가에 달려 있고, 이를 정확히 하는 것이 다음 정의이다.

::: 정의 4
거리공간 $(X,d)$에서 $X$로 가는 함수 $f$가 *축소사상<sub>contraction</sub>*이라는 것은, 어떤 상수 $0\le k<1$이 있어 모든 $x,y\in X$에 대해

$$d(f(x),f(y))\le k d(x,y)$$

가 성립한다는 뜻이다.
:::

여기서 $k$는 $x,y$에 무관한 하나의 상수여야 하며, 정의역과 공역이 모두 $X$라는 점이 중요하다. $f(x)=x/2$는 $\mathbb{R}$에서 $k=1/2$인 축소사상이지만, $[1,2]$에서 정의된 같은 식은 값이 $[1/2,1]$에 놓여 $[1,2]$로 가는 함수가 아니므로 축소사상이 아니다. 실제로 이 함수는 $[1,2]$에 fixed point이 없다. 닫힌 subset 위에서 쓰려면 $f$가 그 subset을 자기 자신으로 보내는지 먼저 확인해야 한다. 축소사상은 $d(f(x),f(y))\le k d(x,y)$에서 $y\to x$일 때 $f(y)\to f(x)$이므로 연속이다.

::: 정리 5 (Banach fixed point 정리)
$(X,d)$가 공집합이 아닌 완비 거리공간이고 $f:X\to X$가 상수 $k$의 축소사상이라 하자. 그러면 $f$는 fixed point $x^\ast$를 정확히 하나 가진다. 또한 임의의 $x_0\in X$에서 시작하여 $x_{n+1}=f(x_n)$으로 정의한 수열은 $x^\ast$로 수렴하며, 모든 $n\ge1$에 대해

$$d(x_n,x^\ast)\le\frac{k^n}{1-k} d(x_1,x_0),\qquad d(x_n,x^\ast)\le\frac{k}{1-k} d(x_n,x_{n-1})$$

이 성립한다.
:::

::: 증명
$x_0$를 임의로 잡고 $x_{n+1}=f(x_n)$으로 정의한다. 축소 조건을 반복하면 $d(x_{n+1},x_n)=d(f(x_n),f(x_{n-1}))\le k d(x_n,x_{n-1})$이므로, 귀납적으로

$$d(x_{n+1},x_n)\le k^n d(x_1,x_0)$$

을 얻는다. $m>n$일 때 삼각부등식을 연속된 항에 적용하면

$$\begin{aligned}
d(x_m,x_n)&\le\sum_{j=n}^{m-1}d(x_{j+1},x_j)\le d(x_1,x_0)\sum_{j=n}^{m-1}k^j \\
&\le d(x_1,x_0)\frac{k^n}{1-k}
\end{aligned}$$

이다. 마지막 부등식은 등비급수의 합 $\sum_{j\ge n}k^j=k^n/(1-k)$로 위에서 누른 것이며, $k<1$이 여기서 쓰인다.

$(x_n)$이 Cauchy 수열임을 보이자. $\varepsilon>0$이 주어지면 $k^n\to0$이므로 $k^N d(x_1,x_0)/(1-k)<\varepsilon$이 되는 $N$을 잡을 수 있다($d(x_1,x_0)=0$이면 어떤 $N$이든 된다). 그러면 $m>n\ge N$에서 $d(x_m,x_n)\le k^n d(x_1,x_0)/(1-k)<\varepsilon$이다. 이처럼 $N$을 $m$과 무관하게 잡을 수 있는 것은 위의 추정이 $m$에 의존하지 않는 우변을 갖기 때문이다. $X$가 완비이므로 $x_n\to x^\ast\in X$인 $x^\ast$가 존재한다.

$f$는 연속이므로 $f(x^\ast)=\lim f(x_n)=\lim x_{n+1}=x^\ast$이다. 즉 $x^\ast$는 fixed point이다. fixed point이 둘, $p$와 $q$가 있다면 $d(p,q)=d(f(p),f(q))\le k d(p,q)$에서 $(1-k)d(p,q)\le0$이고 $1-k>0$이므로 $d(p,q)=0$이다. 따라서 fixed point은 유일하다.

오차 추정은 위의 부등식에서 $m\to\infty$로 보내면 된다. 거리 함수는 $\lvert d(x_m,x_n)-d(x^\ast,x_n)\rvert\le d(x_m,x^\ast)\to0$이므로 $d(x_m,x_n)\to d(x^\ast,x_n)$이고, 부등식 $d(x_m,x_n)\le k^nd(x_1,x_0)/(1-k)$는 [§수열의 수렴, ⁋명제 6](/ko/math/analysis/convergence_of_sequences#prop6){: data-lid="7bhvx" }에 의하여 극한에서도 유지되어 첫째 추정을 준다. 둘째 추정은 $j\ge n$에 대해 $d(x_{j+1},x_j)\le k^{j-n+1}d(x_n,x_{n-1})$이라는 것에서 같은 방식으로 $d(x_m,x_n)\le\sum_{j\ge n}k^{j-n+1}d(x_n,x_{n-1})=\frac{k}{1-k}d(x_n,x_{n-1})$을 얻고 $m\to\infty$로 보내면 된다.
:::

첫째 추정은 계산을 시작하기 전에 $d(x_1,x_0)$만으로 필요한 반복 횟수를 알려 준다(a priori 추정). 둘째 추정은 계산 도중에 이미 얻은 두 항의 차이로 현재 오차의 상계를 주며(a posteriori 추정), 보통 더 날카롭다. 두 추정 모두 $k$가 $1$에 가까울수록 나빠진다.

### 가정의 필요성

정리의 가정은 세 가지, 곧 $k<1$, 완비성, 그리고 $f$가 $X$를 자기 자신으로 보낸다는 것이다. 각각이 빠지면 결론이 실제로 무너진다.

::: 예시 6 (k<1 대신 엄격한 부등식만 있는 경우)
$X=[1,\infty)$는 완비이고, $f(x)=x+1/x$는 $f(x)\ge1$이므로 $X$를 $X$로 보낸다. $x\neq y$인 $x,y\ge1$에 대해

$$f(x)-f(y)=(x-y)+\frac{y-x}{xy}=(x-y)\Bigl(1-\frac{1}{xy}\Bigr)$$

이고, $x,y\ge1$이며 둘 중 적어도 하나는 $1$보다 크므로 $xy>1$이어서 $0<1-1/(xy)<1$이다. 따라서 $\lvert f(x)-f(y)\rvert<\lvert x-y\rvert$가 모든 $x\neq y$에서 성립한다. 그러나 $f(x)=x$는 $1/x=0$을 뜻하므로 fixed point이 없다. 모든 쌍에서 거리가 줄어든다는 것과 하나의 $k<1$로 줄어든다는 것은 다르다. 이 예에서 $x,y\to\infty$이면 $1-1/(xy)\to1$이므로 $\sup$이 $1$이 되어 $k<1$인 상수가 존재하지 않는다. $k=1$을 허용해도, 가령 평행이동 $x\mapsto x+1$은 $\mathbb{R}$에서 거리를 보존하지만 fixed point이 없다.
:::

::: 예시 7 (완비성이 빠진 경우)
$X=(0,1]$에서 $f(x)=x/2$는 $(0,1]$을 자기 자신으로 보내고 $k=1/2$인 축소사상이다. 그러나 fixed point이 될 수 있는 값은 $0$뿐이며 $0\notin X$이다. 반복수열 $x_n=x_0/2^n$은 $X$의 Cauchy 수열이지만 $X$ 안에 극한이 없다.

유리수 위에서도 같은 일이 일어난다. $f(x)=x/2+1/x$는 $\mathbb{Q}\cap[1,2]$를 자기 자신으로 보낸다. 실제로 $x\in[1,2]$에서 산술·기하평균 부등식에 의해 $f(x)\ge2\sqrt{(x/2)(1/x)}=\sqrt2$이고 $f(x)\le\max(f(1),f(2))=3/2$이다. 또한

$$f(x)-f(y)=(x-y)\Bigl(\frac12-\frac1{xy}\Bigr)$$

에서 $x,y\in[1,2]$이면 $1/(xy)\in[1/4,1]$이므로 $\lvert 1/2-1/(xy)\rvert\le1/2$이다. 따라서 $f$는 $k=1/2$인 축소사상이다. 그러나 fixed point의 조건 $x=x/2+1/x$는 $x^2=2$이므로 $\mathbb{Q}$에는 fixed point이 없다. 유리수에서 시작한 반복수열 $1, 3/2, 17/12, \dots$은 $\sqrt2$로 가는 Cauchy 수열이며, 그 극한은 $\mathbb{R}$에서만 존재한다.
:::

## 반복법에의 적용

[정리 5](#thm5){: data-lid="tlfxm" }의 응용은 방정식을 $x=f(x)$의 꼴로 바꾸어 $f$가 적당한 완비 공간 위의 축소사상임을 확인하는 것이다. 그러면 해의 존재, 유일성, 그리고 오차를 통제한 근삿값이 한꺼번에 얻어진다.

::: 예시 8 ($\cos x = x$)
$f(x)=\cos x$를 $X=[0,1]$에서 생각한다. $X$는 $\mathbb{R}$의 닫힌집합이므로 [명제 2](#prop2){: data-lid="8vipv" }에 의해 완비이다. $0<1<\pi/2$에서 $\cos$은 감소하므로 $f([0,1])\subseteq[\cos1,1]\subseteq[0,1]$이고, $f$는 $X$를 자기 자신으로 보낸다.

$f$가 축소사상임을 보이자. 합을 곱으로 바꾸는 공식에 의해

$$\cos x-\cos y=-2\sin\frac{x+y}{2}\sin\frac{x-y}{2}$$

이다. $x,y\in[0,1]$이면 $(x+y)/2\in[0,1]$이고 $\sin$은 $[0,\pi/2]$에서 증가하므로 $0\le\sin\frac{x+y}{2}\le\sin1$이다. 또 $\lvert\sin t\rvert\le\lvert t\rvert$이므로 $\lvert\sin\frac{x-y}{2}\rvert\le\lvert x-y\rvert/2$이다. 따라서

$$\lvert\cos x-\cos y\rvert\le\sin1\cdot\lvert x-y\rvert$$

이고, $\sin1<\sin(\pi/2)=1$이므로 $k=\sin1\approx0.8415$인 축소사상이다. [정리 5](#thm5){: data-lid="76m74" }에 의해 $\cos x=x$는 $[0,1]$에서 해가 정확히 하나이다. 이 해는 $\mathbb{R}$ 전체에서도 유일하다. $\lvert\cos x\rvert\le1$이므로 해는 $[-1,1]$에 있어야 하고, $x\in[-1,0)$이면 $\cos x>0>x$이므로 해가 될 수 없기 때문이다.

$x_0=1$에서 시작하면 $x_1=\cos1\approx0.5403$, $x_2\approx0.8576$, $x_3\approx0.6543$, $x_4\approx0.7935$, $x_5\approx0.7014$이고, 이 수열은 $x^\ast\approx0.739085$로 진동하며 수렴한다. [정리 5](#thm5){: data-lid="c9egm" }의 첫째 추정에서 $d(x_1,x_0)=1-\cos1\approx0.4597$이므로 $\lvert x_n-x^\ast\rvert\le 2.90\cdot(0.8415)^n$이다. 이 추정으로 오차 $10^{-6}$ 이하를 보장하는 데 필요한 반복 횟수는 $n\ge87$이다. 실제 오차는 훨씬 빨리 줄어드는데, $x_5$에서 이미 $\lvert x_5-x^\ast\rvert\approx0.038$이고 둘째 추정은 $\lvert x_5-x^\ast\rvert\le\frac{k}{1-k}\lvert x_5-x_4\rvert\approx0.49$를 준다. 두 추정이 보수적인 것은 $k$가 $[0,1]$ 전체에서의 최악의 경우를 반영하기 때문이다.
:::

## Baire 범주정리

완비성의 다른 결과는 위상적인 성격을 가진다. 거리공간 $X$의 subset $D$가 [§거리공간과 열린집합·닫힌집합, ⁋정의 21](/ko/math/analysis/metric_spaces#def21){: data-lid="c8cpz" }의 *dense*라는 것은 [§거리공간과 열린집합·닫힌집합, ⁋명제 22](/ko/math/analysis/metric_spaces#prop22){: data-lid="yhiwb" }에 의하여 $X$의 모든 공집합이 아닌 열린집합이 $D$와 만난다는 뜻이다. 닫힌집합 $F$의 내부가 공집합인 것과 여집합 $X\setminus F$가 dense인 것은 같은 말이다. $F$가 비어 있지 않은 열린집합 $V$를 포함하는 것이 $V\cap(X\setminus F)=\emptyset$인 것과 같기 때문이다.

::: 정리 9 (Baire 범주정리)
$X$가 공집합이 아닌 완비 거리공간이고 $U_1,U_2,\dots$가 $X$의 열린 dense subset이면, 교집합 $\bigcap_{n\ge1}U_n$도 dense이다. 특히 이 교집합은 공집합이 아니다.
:::

::: 증명
$W$를 $X$의 공집합이 아닌 열린집합이라 하자. $\bigcap_nU_n$이 $W$와 만남을 보이면 된다. 열린 공 $B(x,r)=\{y:d(y,x)<r\}$와 닫힌 공 $\overline{B}(x,r)=\{y:d(y,x)\le r\}$를 쓴다. 닫힌 공은 닫힌집합이고 $\overline{B}(x,r)\subseteq B(x,2r)$이다.

$U_1$이 dense이므로 [§거리공간과 열린집합·닫힌집합, ⁋명제 10](/ko/math/analysis/metric_spaces#prop10){: data-lid="4gt18" }에 의하여 열린집합인 $W\cap U_1$은 공집합이 아니다. 그 안의 점 $x_1$을 잡고, 닫힌 공 $\overline{B}(x_1,r_1)\subseteq W\cap U_1$이 되도록 $0<r_1<1$을 택한다. $W\cap U_1$이 열린집합이므로 충분히 작은 열린 공이 그 안에 들어가고, 반지름을 절반으로 줄이면 닫힌 공도 들어간다.

$n\ge2$에서는 $x_{n-1},r_{n-1}$이 이미 주어졌다고 하자. $U_n$이 dense이므로 [§거리공간과 열린집합·닫힌집합, ⁋명제 9](/ko/math/analysis/metric_spaces#prop9){: data-lid="41myc" }와 [§거리공간과 열린집합·닫힌집합, ⁋명제 10](/ko/math/analysis/metric_spaces#prop10){: data-lid="vuido" }에 의하여 열린집합인 $B(x_{n-1},r_{n-1})\cap U_n$은 공집합이 아니고, 그 안의 점 $x_n$과 $0<r_n<1/n$을 $\overline{B}(x_n,r_n)\subseteq B(x_{n-1},r_{n-1})\cap U_n$이 되도록 잡을 수 있다. 이렇게 닫힌 공의 감소열

$$\overline{B}(x_1,r_1)\supseteq\overline{B}(x_2,r_2)\supseteq\cdots$$

을 얻으며 $\overline{B}(x_n,r_n)\subseteq U_n$, $\overline{B}(x_1,r_1)\subseteq W$이다. 반지름을 $r_n<1/n$으로 택하는 이유는 공의 지름이 $0$으로 가게 하여 중심들이 Cauchy 수열이 되도록 하기 위해서이다.

실제로 $m\ge n$이면 $x_m\in\overline{B}(x_n,r_n)$이므로 $d(x_m,x_n)\le r_n<1/n$이다. 따라서 $(x_n)$은 Cauchy 수열이고, $X$의 완비성에 의해 어떤 $x\in X$로 수렴한다. 각 $n$에 대해 $m\ge n$인 모든 $x_m$이 닫힌집합 $\overline{B}(x_n,r_n)$에 있으므로 극한 $x$도 [§거리공간과 열린집합·닫힌집합, ⁋명제 12](/ko/math/analysis/metric_spaces#prop12){: data-lid="3vrs2" }에 의하여 이 집합에 속한다. 그러므로 모든 $n$에 대해 $x\in\overline{B}(x_n,r_n)\subseteq U_n$이고, 또 $x\in\overline{B}(x_1,r_1)\subseteq W$이다. 즉 $x\in W\cap\bigcap_nU_n$이다.
:::

여집합을 취하면 같은 내용이 다음과 같이 읽힌다. 공집합이 아닌 완비 거리공간은 내부가 공집합인 닫힌집합들의 가산 합집합이 될 수 없다. $F_n$이 그런 집합이면 $U_n=X\setminus F_n$은 열린 dense 집합이고, $\bigcap U_n\ne\emptyset$은 $\bigcup F_n\ne X$를 뜻한다. 완비성은 여기서도 필수이다. $\mathbb{Q}=\bigcup_{q\in\mathbb{Q}}\{q\}$는 가산 개의 한 점 집합의 합집합이고, 각 한 점 집합은 $\mathbb{Q}$에서 닫혀 있으며 내부가 공집합이므로 Baire 범주정리의 결론이 $\mathbb{Q}$에서는 성립하지 않는다.

::: 따름정리 10
$\mathbb{R}$은 비가산 집합이다.
:::

::: 증명
$\mathbb{R}$이 가산이라 가정하고 $\mathbb{R}=\{a_1,a_2,\dots\}$로 나열하자. 각 $n$에 대해 $U_n=\mathbb{R}\setminus\{a_n\}$은 열린집합이다. 또한 $\mathbb{R}$의 공집합이 아닌 열린집합은 구간을 포함하므로 무한히 많은 점을 가지고, 따라서 $a_n$ 이외의 점을 포함한다. 즉 $U_n$은 dense이다. $\mathbb{R}$은 [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="vfh8y" }에 의하여 완비이므로 [정리 9](#thm9){: data-lid="f57ly" }에 의해 $\bigcap_nU_n$은 공집합이 아니다. 그러나 이 교집합의 점 $x$는 모든 $a_n$과 다르므로 $\mathbb{R}$의 원소가 아니다. 이는 모순이다.
:::

이 증명은 실수가 가산이 아님을 [§부분수열과 Bolzano–Weierstrass 정리, ⁋보조정리 5](/ko/math/analysis/bolzano_weierstrass#lem5){: data-lid="m9kfl" }의 구간 축소 논증이나 [§거리공간과 열린집합·닫힌집합, ⁋명제 23](/ko/math/analysis/metric_spaces#prop23){: data-lid="dor44" }의 대각선 논법과 달리 완비성만으로 보여 준다. 같은 논증은 isolated point이 없는 임의의 비어 있지 않은 완비 거리공간이 비가산임을 보인다. 다음 글에서는 거리공간의 compactness를 다룬다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
