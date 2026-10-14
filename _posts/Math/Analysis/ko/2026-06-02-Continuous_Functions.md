---
title: "연속함수의 성질"
description: "연속함수가 컴팩트 집합을 컴팩트 집합으로 보냄을 보이고, 이로부터 최대·최소 정리와 Heine–Cantor 정리를 증명한다. 균등연속의 정의에서 한정사의 순서를 분석하고, 균등연속이 아닌 함수와 Lipschitz 함수, 연속 전단사의 역함수가 불연속인 예를 다룬다."
excerpt: "컴팩트 집합의 연속상, 최대·최소 정리, 균등연속과 Heine–Cantor 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/continuous_functions
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 12

published: false

---

연속함수는 점에서 정의되지만, 정의역 전체의 성질은 점별 정보만으로는 얻어지지 않는다. 열린구간 $(0,1)$ 위의 $x$는 연속이지만 최댓값이 없고, $(0,1]$ 위의 $1/x$는 연속이지만 bounded가 아니다. 정의역이 컴팩트이면 이런 현상이 사라진다는 것이 이 글의 주제이다. 우리는 [§컴팩트성, ⁋정리 5](/ko/math/analysis/compactness#thm5){: data-lid="np6an" }에서 얻은 결과를 사용하여, 연속함수가 컴팩트 집합을 컴팩트 집합으로 보낸다는 사실에서 최대·최소 정리를 얻고, 같은 방법으로 균등연속성을 다룬다. 연속의 점열 특징화는 [§함수의 극한과 연속, ⁋정리 4](/ko/math/analysis/limits_and_continuity#thm4){: data-lid="tkjmv" }의 것을 쓴다.

거리공간에서는 [§컴팩트성, ⁋정리 5](/ko/math/analysis/compactness#thm5){: data-lid="resqt" }에 의하여 컴팩트인 것과 모든 점열이 집합 안의 점으로 수렴하는 부분수열을 갖는 것이 같으므로, 이 글에서 컴팩트 집합은 후자의 성질로 사용한다. 정의역과 공역은 거리공간이고, 함수 $f : X \rightarrow Y$의 거리는 각각 $d_X$, $d_Y$로 적는다.

## 컴팩트 집합의 연속상

::: 정리 1
$f : X \rightarrow Y$가 연속이고 $K \subseteq X$가 컴팩트이면 $f(K)$는 컴팩트이다.
:::

::: 증명
$f(K)$의 점열 $(y_n)$을 임의로 택하자. 각 $y_n$에 대해 $y_n = f(x_n)$인 $x_n \in K$를 하나씩 고른다. $K$가 컴팩트이므로 어떤 부분수열 $x_{n_k}$와 $x \in K$가 있어 $x_{n_k} \rightarrow x$이다. $f$가 $x$에서 연속이므로 [§함수의 극한과 연속, ⁋정리 4](/ko/math/analysis/limits_and_continuity#thm4){: data-lid="ivnb8" }의 (b)에 의하여 $f(x_{n_k}) \rightarrow f(x)$, 즉 $y_{n_k} \rightarrow f(x)$이고, $f(x) \in f(K)$이다. 따라서 $f(K)$의 모든 점열은 $f(K)$의 점으로 수렴하는 부분수열을 갖는다.
:::

정리의 내용은 compactness가 닫힘과 bounded의 결합이라는 데 있다. 두 성질은 각각으로는 연속함수에 의해 보존되지 않는다. $\arctan$은 닫힌집합 $\mathbb{R}$를 닫혀 있지 않은 $(-\pi/2, \pi/2)$로 보내고, $1/x$는 bounded인 $(0,1]$을 bounded가 아닌 $[1,\infty)$로 보낸다. 반면 컴팩트 집합의 상은 닫히고 bounded이다. 또 정리의 역방향, 곧 상이 컴팩트이면 정의역이 컴팩트라는 주장은 성립하지 않는다. 상수함수는 아무 정의역에서나 상이 한 점이다.

## 최대·최소 정리

::: 따름정리 2 (최대·최소 정리)
$K$가 공집합이 아닌 컴팩트 집합이고 $f : K \rightarrow \mathbb{R}$가 연속이면, $f$는 $K$에서 최댓값과 최솟값을 갖는다. 특히 닫힌구간 $[a,b]$ 위의 연속함수는 최댓값과 최솟값을 갖는다.
:::

::: 증명
[정리 1](#thm1){: data-lid="iubi5" }에 의하여 $f(K)$는 $\mathbb{R}$의 공집합이 아닌 컴팩트 집합이고, 따라서 [§컴팩트성, ⁋명제 6](/ko/math/analysis/compactness#prop6){: data-lid="yhl1o" }에 의하여 닫혀 있고 bounded이다. Bounded이므로 $M = \sup f(K)$가 존재한다. 상한에 대한 [§실수의 완비성, ⁋명제 4](/ko/math/analysis/completeness_of_reals#prop4){: data-lid="m9kts" }에 의하여 각 $n$에 대해

$$M - \frac{1}{n} < y_n \leq M$$

인 $y_n \in f(K)$가 있고, 이 점열은 $M$으로 수렴한다. $f(K)$가 닫혀 있으므로 [§거리공간과 열린집합·닫힌집합, ⁋명제 12](/ko/math/analysis/metric_spaces#prop12){: data-lid="aa9nh" }에 의하여 극한 $M$은 $f(K)$에 속한다. 즉 $M = f(x_0)$인 $x_0 \in K$가 있고, $f(x_0)$가 최댓값이다. 최솟값은 $\inf f(K)$에 대해 같은 논증을 하면 얻는다. 마지막 주장은 $[a,b]$가 닫히고 bounded여서 [§컴팩트성, ⁋정리 7](/ko/math/analysis/compactness#thm7){: data-lid="xvf5g" }에 의하여 컴팩트라는 사실에서 따른다.
:::

증명에서 상한이 $f(K)$에 속한다는 점이 닫힘에서 나오고, 상한이 존재한다는 점이 bounded에서 나온다. 따라서 정의역이 컴팩트가 아니거나 $f$가 연속이 아니면 각각 결론이 깨진다.

::: 예시 3 (최대·최소 정리의 가정)
정의역의 compactness가 빠진 경우로, $f(x) = x$를 $(0,1)$ 위에서 보면 $\sup f = 1$, $\inf f = 0$이지만 어느 값도 취해지지 않는다. 이 경우 $f$는 bounded이므로 문제는 정의역이 닫혀 있지 않다는 데 있다. 반대로 $\mathbb{R}$ 위의 $x$는 닫힌 정의역에서 연속이지만 bounded가 아니어서 최댓값이 없다. $(0,1]$ 위의 $1/x$는 최솟값 $1$은 갖지만 bounded가 아니어서 최댓값이 없다.

연속성이 빠진 경우로, $[0,1]$ 위에서

$$h(x) = \begin{cases} x, & 0 \leq x < 1, \\ 0, & x = 1 \end{cases}$$

로 두면 $h$는 bounded이고 $\sup h = 1$이지만 $h(x) = 1$인 점이 없다. 정의역이 컴팩트인데도 $x = 1$에서의 불연속 때문에 최댓값이 사라진다.
:::

## 균등연속

연속이라는 것은 각 점 $a$와 $\varepsilon > 0$에 대하여 $\delta > 0$이 있다는 뜻이고, 이때 $\delta$는 $\varepsilon$뿐 아니라 $a$에도 의존할 수 있다. 함수가 가파른 곳에서는 작은 $\delta$가, 완만한 곳에서는 큰 $\delta$가 필요하기 때문이다. 정의역 전체에 공통으로 통하는 $\delta$가 있는지는 별개의 질문이며, 이것이 균등연속이다.

::: 정의 4
$f : X \rightarrow Y$가 *균등연속<sub>uniformly continuous</sub>*이라는 것은, 모든 $\varepsilon > 0$에 대하여 $\delta > 0$이 존재하여, 모든 $x, x' \in X$에 대해 $d_X(x,x') < \delta$이면 $d_Y(f(x), f(x')) < \varepsilon$인 것이다.
:::

연속의 정의를 한정사로 적으면

$$\forall \varepsilon > 0\ \ \forall a \in X\ \ \exists \delta > 0\ \ \forall x \in X\ \ \bigl(d_X(x,a) < \delta \implies d_Y(f(x), f(a)) < \varepsilon\bigr)$$

이고, 균등연속은

$$\forall \varepsilon > 0\ \ \exists \delta > 0\ \ \forall a \in X\ \ \forall x \in X\ \ \bigl(d_X(x,a) < \delta \implies d_Y(f(x), f(a)) < \varepsilon\bigr)$$

이다. 두 조건의 차이는 $\exists \delta$와 $\forall a$의 순서뿐이다. 균등연속이면 연속임은 곧바로 알 수 있고, 역은 [예시 7](#ex7){: data-lid="ultoe" }에서 보듯 성립하지 않는다. 균등연속은 함수 하나의 성질이 아니라 함수와 정의역의 쌍의 성질이다. $x^2$은 $\mathbb{R}$에서는 균등연속이 아니지만 $[0,R]$에서는 균등연속이다.

균등연속이 아님을 보이려면 정의를 부정해야 한다. 부정은 어떤 $\varepsilon > 0$이 있어서 모든 $\delta > 0$에 대해 $d_X(x,x') < \delta$이면서 $d_Y(f(x), f(x')) \geq \varepsilon$인 두 점 $x, x'$이 존재한다는 것이다. $\delta$를 $1/n$로 두면 다음의 점열 판정이 된다.

::: 명제 5
$f : X \rightarrow Y$가 균등연속이 아닌 것은, 어떤 $\varepsilon > 0$과 $X$의 점열 $(x_n), (x_n')$이 있어서 $d_X(x_n, x_n') \rightarrow 0$이고 모든 $n$에 대해 $d_Y(f(x_n), f(x_n')) \geq \varepsilon$인 것과 동치이다.
:::

::: 증명
($\Rightarrow$) 균등연속이 아니면 위에서 본 부정에 의해 어떤 $\varepsilon > 0$이 있고, 각 $n$에 대해 $\delta = 1/n$을 적용하면 $d_X(x_n, x_n') < 1/n$이고 $d_Y(f(x_n), f(x_n')) \geq \varepsilon$인 $x_n, x_n'$이 있다. 여기서 $\varepsilon$은 $n$에 무관하게 하나로 고정되어 있다.

($\Leftarrow$) 이 $\varepsilon$에 대해 어떤 $\delta > 0$이 통한다고 하자. $d_X(x_n, x_n') < \delta$인 $n$을 택하면 $d_Y(f(x_n), f(x_n')) < \varepsilon$이어야 하는데, 이는 가정에 모순이다.
:::

점열 판정에서 흔한 실수는 $\varepsilon$을 $n$마다 다르게 잡는 것이다. 예를 들어 $d_Y(f(x_n), f(x_n')) \rightarrow 0$이 아니라는 사실만으로는 충분하지 않고, 모든 $n$에서 같은 $\varepsilon$ 이상이라는 하한이 필요하다.

::: 정리 6 (Heine–Cantor)
$K$가 컴팩트이고 $f : K \rightarrow Y$가 연속이면 $f$는 균등연속이다.
:::

::: 증명
$f$가 균등연속이 아니라 하자. [명제 5](#prop5){: data-lid="vn2lc" }에 의하여 어떤 $\varepsilon > 0$과 점열 $(x_n), (x_n')$이 있어 $d_K(x_n, x_n') \rightarrow 0$이고 모든 $n$에 대해 $d_Y(f(x_n), f(x_n')) \geq \varepsilon$이다. $K$가 컴팩트이므로 $x_{n_k} \rightarrow x \in K$인 부분수열이 있다. 그러면

$$d_K(x_{n_k}', x) \leq d_K(x_{n_k}', x_{n_k}) + d_K(x_{n_k}, x) \rightarrow 0$$

이므로 $x_{n_k}' \rightarrow x$이다. $f$가 $x$에서 연속이므로 [§함수의 극한과 연속, ⁋정리 4](/ko/math/analysis/limits_and_continuity#thm4){: data-lid="jlofh" }의 (b)에 의하여 $f(x_{n_k}) \rightarrow f(x)$이고 $f(x_{n_k}') \rightarrow f(x)$이며,

$$d_Y\bigl(f(x_{n_k}), f(x_{n_k}')\bigr) \leq d_Y\bigl(f(x_{n_k}), f(x)\bigr) + d_Y\bigl(f(x), f(x_{n_k}')\bigr) \rightarrow 0$$

이다. 이는 모든 $k$에서 이 거리가 $\varepsilon$ 이상이라는 데 모순이다.
:::

증명에서 연속성은 한 점 $x$에서만 쓰였고, 두 점열을 같은 점으로 모으는 일을 compactness가 맡았다. 이 때문에 $\delta$는 $x$의 위치에 의존하지 않게 된다.

## 균등연속이 아닌 함수

Heine–Cantor 정리의 가정 중 어느 하나라도 빠지면 균등연속이 깨질 수 있다. 정의역이 bounded가 아닌 경우, 닫혀 있지 않은 경우, 그리고 함수가 bounded여도 정의역이 컴팩트가 아닌 경우를 [명제 5](#prop5){: data-lid="6r9tq" }로 확인한다.

::: 예시 7 (연속이지만 균등연속이 아닌 함수)
1. $f(x) = x^2$, 정의역 $\mathbb{R}$. $x_n = n + 1/n$, $x_n' = n$이면 $\lvert x_n - x_n' \rvert = 1/n \rightarrow 0$이지만 $\lvert f(x_n) - f(x_n') \rvert = (n + 1/n)^2 - n^2 = 2 + 1/n^2 \geq 2$이다. 따라서 $\varepsilon = 2$에 대해 균등연속이 아니다. 정의역이 bounded가 아니어서 기울기 $2x$가 한없이 커진다.

2. $f(x) = 1/x$, 정의역 $(0,1)$. $x_n = 1/n$, $x_n' = 1/(n+1)$ ($n \geq 2$)이면 $\lvert x_n - x_n' \rvert = 1/(n(n+1)) \rightarrow 0$이지만 $\lvert f(x_n) - f(x_n') \rvert = 1$이다. 정의역은 bounded이지만 닫혀 있지 않고, 함수는 $0$ 근처에서 bounded가 아니다.

3. $f(x) = \sin(1/x)$, 정의역 $(0,1)$. 이 함수는 bounded이므로 앞의 두 예와 이유가 다르다. $x_n = 1/(2\pi n)$, $x_n' = 1/(2\pi n + \pi/2)$로 두면 $\lvert x_n - x_n' \rvert = (\pi/2)/(2\pi n(2\pi n + \pi/2)) \rightarrow 0$이지만 $f(x_n) = 0$, $f(x_n') = 1$이므로 $\lvert f(x_n) - f(x_n') \rvert = 1$이다. $0$ 근처에서 함수가 $-1$과 $1$ 사이를 무한히 빠르게 진동하기 때문에 공통의 $\delta$가 없다.
:::

세 예에서 보듯 균등연속이 되기 위해서는 정의역이 bounded인 것도, 함수가 bounded인 것도 충분하지 않다. 컴팩트 정의역에서는 [정리 6](#thm6){: data-lid="g8pcx" }이 이를 모두 해결한다.

## Lipschitz 조건

균등연속이 되는 가장 간단한 충분조건은 함숫값의 변화가 변수의 변화의 상수배로 묶이는 것이다. 어떤 $L \geq 0$이 있어 모든 $x, x' \in X$에 대해

$$d_Y\bigl(f(x), f(x')\bigr) \leq L d_X(x, x')$$

이면 $f$를 *Lipschitz 연속<sub>Lipschitz continuous</sub>*이라 하고, 이 $L$을 *Lipschitz 상수*라 부른다.

::: 명제 8
Lipschitz 연속인 함수는 균등연속이다.
:::

::: 증명
Lipschitz 상수를 $L$이라 하고 $\varepsilon > 0$이 주어졌다고 하자. $\delta = \varepsilon/(L+1)$로 택한다. $L = 0$인 경우에도 $\delta$가 정의되도록 분모에 $1$을 더한 것이다. $d_X(x,x') < \delta$이면

$$d_Y\bigl(f(x), f(x')\bigr) \leq L d_X(x,x') \leq \frac{L}{L+1} \varepsilon < \varepsilon$$

이다. $\delta$는 $x, x'$에 무관하게 정해졌다.
:::

$x^2$은 $[0,R]$ 위에서 $\lvert x^2 - x'^2 \rvert = \lvert x + x' \rvert \lvert x - x' \rvert \leq 2R \lvert x - x' \rvert$이므로 상수 $2R$로 Lipschitz이다. 반면 $\mathbb{R}$ 위에서는 [예시 7](#ex7){: data-lid="871x7" }에서 균등연속이 아니므로 어떤 상수로도 Lipschitz일 수 없다. 이 대조에서 $x + x'$의 크기를 묶어 주는 것이 정의역의 bounded임을 볼 수 있다.

[명제 8](#prop8){: data-lid="l9d8y" }의 역은 성립하지 않는다.

::: 예시 9 (균등연속이지만 Lipschitz가 아닌 함수)
$f(x) = \sqrt{x}$를 $[0,\infty)$ 위에서 보자. $x \geq x' \geq 0$이면
$$x = x' + (x - x') \leq x' + 2\sqrt{x'}\sqrt{x - x'} + (x - x') = \bigl(\sqrt{x'} + \sqrt{x - x'}\bigr)^2$$
이므로 $\sqrt{x} \leq \sqrt{x'} + \sqrt{x - x'}$이고, 따라서 $\lvert \sqrt{x} - \sqrt{x'} \rvert \leq \sqrt{\lvert x - x' \rvert}$이다. $\delta = \varepsilon^2$으로 두면 $\lvert x - x' \rvert < \delta$일 때 $\lvert \sqrt{x} - \sqrt{x'} \rvert < \varepsilon$이므로 $f$는 균등연속이다. 이 결론은 정의역이 컴팩트가 아닌 $[0,\infty)$에서도 성립한다. $[0,1]$로 제한하면 [정리 6](#thm6){: data-lid="sv9c9" }으로도 얻어진다.

그러나 $x' = 0$으로 두면
$$\frac{\lvert \sqrt{x} - \sqrt{0} \rvert}{\lvert x - 0 \rvert} = \frac{1}{\sqrt{x}} \rightarrow \infty \quad (x \rightarrow 0^+)$$
이므로 어떤 $L$로도 묶이지 않아, $f$는 $[0,1]$에서도 Lipschitz가 아니다.
:::

이로써 Lipschitz 연속, 균등연속, 연속은 이 순서로 약해지는 조건이고, 어느 방향의 역도 일반적으로는 성립하지 않는다.

## 연속 전단사의 역함수

연속인 전단사 $f : X \rightarrow Y$의 역함수는 연속일 것처럼 보이지만 일반적으로는 그렇지 않다.

::: 예시 10 (역함수가 불연속인 연속 전단사)
$S^1 = \{(u,v) \in \mathbb{R}^2 : u^2 + v^2 = 1\}$이라 하고

$$f : [0, 2\pi) \rightarrow S^1, \qquad f(t) = (\cos t, \sin t)$$

로 두자. $f$는 연속이고 전단사이다. 그러나 역함수 $g = f^{-1}$은 점 $f(0) = (1,0)$에서 연속이 아니다. 점열 $p_n = f(2\pi - 1/n) = (\cos(1/n), -\sin(1/n))$은 $(1,0)$으로 수렴하지만, $g(p_n) = 2\pi - 1/n \rightarrow 2\pi$이고 $g(1,0) = 0$이기 때문이다. $f$는 $[0,2\pi)$의 두 끝 $0$과 $2\pi$ 근처를 원 위의 가까운 점들로 보내지만, 정의역에는 끝점 $2\pi$가 없어서 $g$가 이 가까움을 되돌리지 못한다.
:::

이 예에서 문제가 되는 것은 정의역 $[0,2\pi)$가 컴팩트가 아니라는 점이다. 정의역이 컴팩트이면 역함수는 자동으로 연속이다.

::: 명제 11
$K$가 컴팩트이고 $f : K \rightarrow Y$가 연속인 전단사이면 $f^{-1} : Y \rightarrow K$는 연속이다.
:::

::: 증명
$y_n \rightarrow y$인 $Y$의 점열을 잡고 $x_n = f^{-1}(y_n)$, $x = f^{-1}(y)$라 하자. $x_n \rightarrow x$가 아니라고 가정하면 어떤 $\varepsilon > 0$과 부분수열 $x_{n_k}$가 있어 모든 $k$에 대해 $d_K(x_{n_k}, x) \geq \varepsilon$이다. $K$가 컴팩트이므로 이 부분수열은 다시 수렴하는 부분수열을 갖는다. 그 극한을 $x' \in K$라 하면 $d_K(x', x) \geq \varepsilon$이므로 $x' \neq x$이다. $f$의 연속성과 [§함수의 극한과 연속, ⁋정리 4](/ko/math/analysis/limits_and_continuity#thm4){: data-lid="ivizb" }의 (b)에 의하여 이 부분수열을 따라 $y_{n_k} = f(x_{n_k}) \rightarrow f(x')$인데, 동시에 $y_{n_k} \rightarrow y = f(x)$이다. [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2){: data-lid="er8nr" }에 의하여 $f(x') = f(x)$이고, $f$가 단사이므로 $x' = x$가 되어 모순이다. 따라서 $f^{-1}(y_n) \rightarrow f^{-1}(y)$이다.
:::
