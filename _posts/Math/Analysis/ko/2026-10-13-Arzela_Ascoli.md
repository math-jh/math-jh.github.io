---
title: "동등연속성과 Arzelà–Ascoli 정리"
description: "함수열이 균등수렴하는 부분수열을 가지기 위한 조건을 equicontinuity로 찾고, 대각선 논법으로 Arzelà–Ascoli 정리를 증명한다. 이로부터 C(K)의 compact subset을 특성화하고, uniformly bounded이지만 동등연속이 아닌 sin(nx), 균등 Lipschitz 함수열의 응용, 가정이 빠질 때의 반례를 다룬다."
excerpt: "Equicontinuity, 대각선 논법, Arzelà–Ascoli 정리와 C(K)의 compact subset"

categories: [Math / Analysis]
permalink: /ko/math/analysis/arzela_ascoli
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 22

published: false

---

[§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4)는 $\mathbb{R}$의 bounded sequence가 수렴하는 부분수열을 가진다고 말한다. 함수열에 대해서도 같은 형태의 정리를 원한다면, 수렴을 균등수렴으로 읽어야 한다. 점별수렴하는 부분수열은 bounded만으로도 얻어지지만, 극한이 연속이라는 보장도, 수렴이 균등하다는 보장도 없다. 이 글에서는 compact 거리공간 $K$ 위의 연속함수열이 균등수렴하는 부분수열을 가지기 위한 조건이 bounded이면서 동등연속인 것임을 보인다. 값은 $\mathbb{R}$ 또는 $\mathbb{C}$에서 취하고, $C(K)$는 $K$ 위의 연속함수 전체에 상한노름 $\lVert f\rVert=\sup_{x\in K}\lvert f(x)\rvert$을 준 거리공간이다. $B(x,r)$은 $K$의 열린 공을 뜻한다. [§균등수렴, ⁋정의 1](/ko/math/analysis/uniform_convergence#def1)에서 보았듯이 이 노름에 대한 수렴이 균등수렴이다.

## 유계성과 동등연속성

::: 정의 1
$F\subseteq C(K)$가 *pointwise bounded<sub>점별유계</sub>*라는 것은 각 $x\in K$에 대해 $\sup_{f\in F}\lvert f(x)\rvert<\infty$인 것이다. *Uniformly bounded<sub>균등유계</sub>*라는 것은 $\sup_{f\in F}\lVert f\rVert<\infty$, 즉 $x$와 $f$에 무관한 $M$이 있어 모든 $f\in F$와 $x\in K$에 대해 $\lvert f(x)\rvert\leq M$인 것이다.
:::

Uniformly bounded이면 pointwise bounded이지만 역은 성립하지 않는다. $[0,1]$ 위에서 $f_n(x)=\max\{0,n-n^2\lvert x-1/n\rvert\}$는 $[0,2/n]$ 밖에서 $0$이고 $x=1/n$에서 최댓값 $n$을 가진다. 고정된 $x>0$에 대해서는 $n>2/x$이면 $f_n(x)=0$이고 $f_n(0)=0$이므로 pointwise bounded이지만, $\lVert f_n\rVert=n$이므로 uniformly bounded가 아니다. 아래에서 보듯 동등연속성이 더해지면 두 조건은 같아진다.

::: 정의 2
$F\subseteq C(K)$가 *equicontinuous<sub>동등연속</sub>*라는 것은 임의의 $x\in K$와 $\varepsilon>0$에 대하여 $\delta>0$이 존재하여, 모든 $f\in F$와 $d(x,y)<\delta$인 모든 $y\in K$에 대해

$$\lvert f(y)-f(x)\rvert<\varepsilon$$

이 성립하는 것이다. $\delta$를 $x$에 무관하게 잡을 수 있을 때, 즉 모든 $x,y$에 대해 $d(x,y)<\delta$이면 모든 $f\in F$에 대해 $\lvert f(x)-f(y)\rvert<\varepsilon$일 때 *uniformly equicontinuous<sub>균등 동등연속</sub>*라 한다.
:::

한정사의 순서가 핵심이다. $F$의 각 함수가 연속이라는 것은 $x$와 $\varepsilon$과 $f$를 정한 뒤에 $\delta$가 정해진다는 뜻이다. 동등연속은 $\delta$가 $f$에 의존하지 않고 $F$ 전체에 공통으로 통하는 것을 요구한다. 함수가 유한개이면 각 함수의 $\delta$ 중 최솟값을 취하면 되므로 항상 동등연속이고, 무한히 많은 함수 사이에서 $\delta$가 $0$으로 줄어들지 않는다는 것이 새로운 조건이다. 균등 동등연속은 여기에 $x$에 대한 균등성까지 더한 것이다.

정의역이 compact이면 두 개념은 같다. 연속함수 하나에 대한 [§연속함수의 성질, ⁋정리 6](/ko/math/analysis/continuous_functions#thm6)의 증명이 $F$ 전체에 대해 그대로 통한다.

::: 보조정리 3
$K$가 compact이고 $F\subseteq C(K)$가 equicontinuous이면 $F$는 uniformly equicontinuous이다.
:::

::: 증명
$\varepsilon>0$이 주어졌다고 하자. 각 $x\in K$에 대해 $F$의 동등연속성에서 $\delta_x>0$을 잡아, 모든 $f\in F$와 $d(x,y)<\delta_x$인 $y$에 대해 $\lvert f(y)-f(x)\rvert<\varepsilon/2$이도록 한다. 열린 공 $B(x,\delta_x/2)$들은 $K$를 덮으므로 [§컴팩트성, ⁋정의 1](/ko/math/analysis/compactness#def1)에 의하여 유한개 $x_1,\dots,x_m$으로 $K$가 덮인다. $\delta=\min_i\delta_{x_i}/2$라 두자. $d(y,z)<\delta$인 $y,z\in K$를 잡고 $y\in B(x_i,\delta_{x_i}/2)$인 $i$를 택하면, $d(z,x_i)\leq d(z,y)+d(y,x_i)<\delta+\delta_{x_i}/2\leq\delta_{x_i}$이다. 따라서 $y$와 $z$ 모두 $x_i$에서 $\delta_{x_i}$ 미만 떨어져 있고, 모든 $f\in F$에 대해

$$\lvert f(y)-f(z)\rvert\leq\lvert f(y)-f(x_i)\rvert+\lvert f(x_i)-f(z)\rvert<\varepsilon$$

이다. $\delta$는 $f$와 $y,z$에 의존하지 않는다.
:::

$\varepsilon/2$를 택한 것은 마지막에 두 항을 더해 $\varepsilon$ 미만을 얻기 위해서이고, 공의 반지름을 $\delta_x/2$로 줄인 것은 $y$에서 $z$로 옮겨도 $x_i$의 $\delta_{x_i}$-공을 벗어나지 않게 하기 위해서이다.

동등연속이면 pointwise bounded와 uniformly bounded가 같아진다.

::: 보조정리 4
$K$가 compact이고 $F\subseteq C(K)$가 equicontinuous이며 pointwise bounded이면 $F$는 uniformly bounded이다.
:::

::: 증명
[보조정리 3](#lem3)에 의하여 $\varepsilon=1$에 대해 $\delta>0$이 있어 모든 $f\in F$에 대해 $d(x,y)<\delta$이면 $\lvert f(x)-f(y)\rvert<1$이다. 공 $B(x,\delta)$들이 $K$를 덮으므로 유한개의 중심 $x_1,\dots,x_m$이 있어 $K=\bigcup_iB(x_i,\delta)$이다. $M_i=\sup_{f\in F}\lvert f(x_i)\rvert$는 pointwise boundedness에 의해 유한하다. 임의의 $x\in K$를 $B(x_i,\delta)$에 속하는 $x$로 잡으면, 모든 $f\in F$에 대해 $\lvert f(x)\rvert\leq\lvert f(x_i)\rvert+1\leq\max_jM_j+1$이다.
:::

## 대각선 논법

Arzelà–Ascoli 정리의 증명은 두 부분으로 이루어진다. 먼저 셀 수 있는 점들에서 수렴하는 부분수열을 뽑고, 그 다음 동등연속성으로 이 수렴을 $K$ 전체에서의 균등수렴으로 끌어올린다. 앞 부분이 대각선 논법이다.

::: 보조정리 5 (대각선 논법)
$E$가 셀 수 있는 집합이고 $f_n:E\rightarrow\mathbb{C}$가 각 점에서 pointwise bounded인 함수열, 즉 각 $x\in E$에 대해 $\sup_n\lvert f_n(x)\rvert<\infty$라 하자. 그러면 $(f_n)$은 $E$의 모든 점에서 수렴하는 부분수열을 가진다.
:::

::: 증명
$E=\{x_1,x_2,\dots\}$로 나열한다. 유한집합이면 아래 과정이 유한 번에 끝나므로 무한집합인 경우만 다룬다. $(f_n(x_1))_n$은 bounded 수열이므로 [§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4)에 의하여 $(f_n)$의 부분수열 $S_1=(f_{1,k})_k$가 있어 $f_{1,k}(x_1)$이 수렴한다. 다음으로 $(f_{1,k}(x_2))_k$도 bounded이므로 $S_1$의 부분수열 $S_2=(f_{2,k})_k$로서 $f_{2,k}(x_2)$가 수렴하는 것이 있다. 같은 방식으로 $S_{j}$를 $S_{j-1}$의 부분수열로서 $f_{j,k}(x_j)$가 수렴하도록 귀납적으로 잡는다.

이제 대각선 $g_k=f_{k,k}$를 취한다. $f_{k,k}=f_{n_k}$라 하자. $S_{k+1}$이 $S_k$의 부분수열이므로 $S_{k+1}$의 $k$번째 항은 $S_k$의 $k$번째 항 이후에 나타나고, $S_{k+1}$ 안에서 $(k+1)$번째 항은 $k$번째 항 뒤에 오므로 $n_{k+1}>n_k$이다. 즉 $(g_k)$는 $(f_n)$의 부분수열이다. 또한 각 $j$에 대해 $k\geq j$인 항 $g_k$는 모두 $S_j$의 항이고 $S_j$ 안에서 순서를 지키므로, $(g_k)_{k\geq j}$는 $S_j$의 부분수열이다. $f_{j,k}(x_j)$가 수렴하므로 그 부분수열 $g_k(x_j)$도 수렴한다. 이것이 모든 $j$에 대해 성립한다.
:::

대각선을 취하는 이유는, $S_1\supseteq S_2\supseteq\cdots$의 어느 하나도 모든 점에서 수렴하지는 않지만 $S_j$는 처음 $j$개의 점에서 수렴하기 때문이다. $k$번째 항을 $S_k$에서 가져오면 $j$번째 점에서는 $j$번째 항 이후가 전부 $S_j$ 안에 있게 된다.

## Arzelà–Ascoli 정리

$E$를 $K$의 셀 수 있는 dense subset으로 잡아야 한다. Compact 거리공간에는 그런 집합이 있다. 각 $m$에 대해 $K$를 반지름 $1/m$인 유한개의 열린 공으로 덮을 수 있으므로([§컴팩트성, ⁋정의 1](/ko/math/analysis/compactness#def1)), 이 공들의 중심을 모든 $m$에 대해 모으면 셀 수 있는 집합 $E$를 얻는다. 임의의 $x\in K$와 $r>0$에 대해 $1/m<r$인 $m$을 잡으면 $x$는 반지름 $1/m$인 공 중 하나에 속하고 그 중심이 $E$에 있으므로, $E$는 $x$의 $r$-근방과 만난다.

::: 정리 6 (Arzelà–Ascoli)
$K$가 compact 거리공간이고 $(f_n)$이 $C(K)$의 함수열로서 pointwise bounded이고 equicontinuous라 하자. 그러면 $(f_n)$은 uniformly bounded이고, 균등수렴하는 부분수열을 가진다. 극한은 $C(K)$에 속한다.
:::

::: 증명
Uniform boundedness는 [보조정리 4](#lem4)에서 나온다. $E\subseteq K$를 위에서 만든 셀 수 있는 dense 집합이라 하자. [보조정리 5](#lem5)에 의하여 $E$의 모든 점에서 수렴하는 부분수열 $(g_k)$가 있다. 이 부분수열이 상한노름에 대해 Cauchy임을 보인다.

$\varepsilon>0$이 주어졌다고 하자. $(g_k)$도 equicontinuous이므로 [보조정리 3](#lem3)에서 $\delta>0$이 있어 모든 $k$에 대해 $d(x,y)<\delta$이면 $\lvert g_k(x)-g_k(y)\rvert<\varepsilon/3$이다. $E$가 dense이므로 모든 $x\in K$는 어떤 $e\in E$와 $d(x,e)<\delta$이다. 따라서 공 $B(e,\delta)$ $(e\in E)$는 $K$를 덮고, [§컴팩트성, ⁋정의 1](/ko/math/analysis/compactness#def1)에 의하여 유한개의 $e_1,\dots,e_m\in E$로 $K$가 덮인다. 각 $g_k(e_i)$가 수렴하므로 Cauchy이고, 유한개의 $i$에 대해 동시에 $k,l\geq N$이면 $\lvert g_k(e_i)-g_l(e_i)\rvert<\varepsilon/3$인 $N$이 있다. 이제 $x\in K$를 $d(x,e_i)<\delta$인 $e_i$와 함께 잡으면, $k,l\geq N$에 대해

$$\lvert g_k(x)-g_l(x)\rvert\leq\lvert g_k(x)-g_k(e_i)\rvert+\lvert g_k(e_i)-g_l(e_i)\rvert+\lvert g_l(e_i)-g_l(x)\rvert<\varepsilon$$

이다. $N$은 $x$에 의존하지 않으므로 $\lVert g_k-g_l\rVert\leq\varepsilon$이다. $\varepsilon/3$으로 나눈 것은 위 세 항에 각각 같은 크기를 배분하기 위해서이고, 유한개의 $e_i$를 쓴 것은 $N$을 점마다 새로 잡지 않고 하나로 고정하기 위해서이다.

이제 극한을 만든다. 각 $x$에 대해 $(g_k(x))$가 $\mathbb{C}$의 Cauchy 수열이므로 $g(x)=\lim_kg_k(x)$가 존재한다. 위에서 $k,l\geq N$이면 모든 $x$에 대해 $\lvert g_k(x)-g_l(x)\rvert\leq\varepsilon$이므로, $l\rightarrow\infty$로 보내면 $\lvert g_k(x)-g(x)\rvert\leq\varepsilon$이다. 즉 $k\geq N$이면 $\lVert g_k-g\rVert\leq\varepsilon$이고 $g_k\rightarrow g$는 균등수렴이다. [§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6)에 의하여 연속함수열의 균등극한은 연속이므로 $g\in C(K)$이다.
:::

[정리 6](#thm6)은 pointwise boundedness만 가정했는데 결론은 uniform boundedness까지 포함한다. 동등연속성이 점별 정보를 정의역 전체로 퍼뜨리기 때문이다. 또 균등수렴하는 부분수열을 뽑기만 하고 전체 수열이 수렴한다고는 말하지 않는다. $f_n=(-1)^n$은 상수함수열이어서 동등연속이고 uniformly bounded이지만 수렴하지 않는다.

## $C(K)$의 compact subset

[정리 6](#thm6)은 점열의 말로 쓰인 것이다. $C(K)$는 거리공간이므로 [§컴팩트성, ⁋정리 5](/ko/math/analysis/compactness#thm5)에서 본 대로 점열의 말은 compactness와 같은 뜻이 된다. 이로부터 compact subset의 특성화를 얻는다.

::: 정리 7
$K$가 compact 거리공간일 때 $F\subseteq C(K)$가 compact인 것은 $F$가 닫혀 있고, uniformly bounded이며, equicontinuous인 것과 동치이다.
:::

::: 증명
($\Leftarrow$) $(f_n)$을 $F$의 점열이라 하자. $F$가 uniformly bounded이므로 pointwise bounded이고, [정리 6](#thm6)에 의하여 $C(K)$에서 어떤 $g$로 수렴하는 부분수열이 있다. $F$가 닫혀 있으므로 $g\in F$이다. 따라서 $F$는 sequentially compact이고, [§컴팩트성, ⁋정리 5](/ko/math/analysis/compactness#thm5)에 의하여 거리공간에서 이는 compact와 같다.

($\Rightarrow$) $F$가 compact이면 닫혀 있고 bounded이다. 또한 [§컴팩트성, ⁋정리 5](/ko/math/analysis/compactness#thm5)에 의하여 totally bounded이다. $\varepsilon>0$이 주어졌다고 하자. $F$의 유한개 원소 $f_1,\dots,f_m$이 있어 모든 $f\in F$에 대해 어떤 $i$가 $\lVert f-f_i\rVert<\varepsilon/3$을 만족한다. 각 $f_i$는 compact 집합 $K$ 위의 연속함수이므로 [§연속함수의 성질, ⁋정리 6](/ko/math/analysis/continuous_functions#thm6)에 의하여 균등연속이고, $d(x,y)<\delta_i$이면 $\lvert f_i(x)-f_i(y)\rvert<\varepsilon/3$인 $\delta_i$가 있다. $\delta=\min_i\delta_i$라 두자. $d(x,y)<\delta$이고 $f\in F$이면 위의 $i$에 대해

$$\lvert f(x)-f(y)\rvert\leq\lvert f(x)-f_i(x)\rvert+\lvert f_i(x)-f_i(y)\rvert+\lvert f_i(y)-f(y)\rvert<\varepsilon$$

이다. $\delta$는 $f$와 $x,y$에 의존하지 않으므로 $F$는 uniformly equicontinuous이고, 특히 equicontinuous이다.
:::

($\Rightarrow$)에서 totally bounded가 쓰이는 이유는 무한한 족 $F$를 유한개의 함수 $f_i$로 근사하여, 균등연속성의 $\delta$를 유한개의 최솟값으로 만들기 위해서이다. 이것이 동등연속성의 필요성을 보이는 방식이다.

[정리 7](#thm7)에서 $F$가 닫혀 있어야 한다는 조건을 빼면 relatively compact, 즉 폐포가 compact인 것의 특성화가 된다. Uniformly bounded이고 동등연속인 족의 폐포도 같은 성질을 가지므로(균등유계의 상수 $M$과 동등연속의 $\delta$가 극한에서도 보존된다), [정리 7](#thm7)로 폐포가 compact임을 알 수 있다.

## 가정이 빠질 때

Uniformly bounded이지만 동등연속이 아닌 함수열의 표준 예가 $\sin(nx)$이다.

::: 예시 8 ($\sin(nx)$)
$K=[0,2\pi]$에서 $f_n(x)=\sin(nx)$는 $\lVert f_n\rVert\leq1$이므로 uniformly bounded이다. 그러나 동등연속이 아니고, 균등수렴하는 부분수열도 없다.

동등연속이 아님을 $x=0$에서 보인다. $\varepsilon=1/2$에 대해 어떤 $\delta>0$이 있다고 하자. $\pi/(2n)<\delta$인 $n$을 잡으면 $\lvert f_n(\pi/(2n))-f_n(0)\rvert=1\geq\varepsilon$이다. 어떤 $\delta$도 모든 $n$에 공통으로 통하지 않는다.

균등수렴하는 부분수열이 없음은 다음과 같다. 서로 다른 양의 정수 $a\neq b$에 대해 $\int_0^{2\pi}\sin(ax)\sin(bx)\dd{x}=0$이고 $\int_0^{2\pi}\sin^2(ax)\dd{x}=\pi$이므로

$$\int_0^{2\pi}\bigl(\sin(ax)-\sin(bx)\bigr)^2\dd{x}=2\pi$$

이다. 피적분함수는 $\lVert f_a-f_b\rVert^2$ 이하이므로 $2\pi\leq2\pi\lVert f_a-f_b\rVert^2$, 즉 $\lVert f_a-f_b\rVert\geq1$이다. 따라서 서로 다른 항 사이의 거리가 모두 $1$ 이상이고, 어떤 부분수열도 상한노름에 대해 Cauchy가 아니다. 점별수렴하는 부분수열이 존재하는지와는 무관하게 균등수렴하는 부분수열은 없다.
:::

이 예는 [정리 7](#thm7)의 관점에서도 읽힌다. $\{f_n\}$을 포함하는 $C[0,2\pi]$의 closed unit ball은 닫혀 있고 uniformly bounded이지만 compact가 아니고, 모자라는 조건이 동등연속이다.

정의역의 compactness도 빠질 수 없다.

::: 예시 9 (정의역이 compact가 아닌 경우)
$\varphi(x)=\max\{0,1-\lvert x\rvert\}$라 하고 $\mathbb{R}$ 위에서 $f_n(x)=\varphi(x-n)$으로 둔다. 각 $f_n$은 $0\leq f_n\leq1$이고 Lipschitz 상수가 $1$이므로 uniformly bounded이고 동등연속이다. 그러나 고정된 $x$에 대해 $n>x+1$이면 $f_n(x)=0$이므로 $f_n$은 $0$으로 점별수렴한다. 부분수열이 균등수렴한다면 그 극한은 점별극한 $0$이어야 하는데 $\lVert f_n\rVert=1$이므로 모순이다. 따라서 균등수렴하는 부분수열은 없다. 봉우리가 $x=n$으로 달아나기 때문에, 증명에서 쓴 유한 덮개를 만들 수 없다.
:::

## 균등 Lipschitz 함수열

동등연속성을 확인하는 가장 흔한 방법은 도함수나 Lipschitz 상수를 균등하게 제어하는 것이다.

::: 따름정리 10
$K$가 compact 거리공간이고 $(f_n)$이 $K$ 위의 함수열로서, 상수 $L$이 있어 모든 $n$과 $x,y\in K$에 대해 $\lvert f_n(x)-f_n(y)\rvert\leq L d(x,y)$이며, 어떤 $x_0\in K$에서 $(f_n(x_0))$이 bounded라 하자. 그러면 $(f_n)$은 균등수렴하는 부분수열을 가진다.
:::

::: 증명
$\varepsilon>0$에 대해 $\delta=\varepsilon/L$로 두면($L=0$이면 모든 $f_n$이 상수이므로 임의의 $\delta$) $d(x,y)<\delta$일 때 모든 $n$에 대해 $\lvert f_n(x)-f_n(y)\rvert\leq L d(x,y)<\varepsilon$이므로 $(f_n)$은 equicontinuous이다. 각 $f_n$은 Lipschitz이므로 연속이다. 또 $K$가 compact이어서 $D=\sup_{x,y\in K}d(x,y)$가 유한하고, $\lvert f_n(x)\rvert\leq\lvert f_n(x_0)\rvert+LD$이므로 $(f_n)$은 uniformly bounded이다. [정리 6](#thm6)을 적용하면 된다.
:::

특히 $K=[a,b]$이고 $f_n$이 미분가능하며 $\lvert f_n'\rvert\leq L$이면 [§평균값 정리와 테일러 정리, ⁋정리 3](/ko/math/analysis/mean_value_theorem#thm3)에 의하여 $f_n$은 Lipschitz 상수 $L$을 가지므로 위의 결론이 성립한다.

Uniform boundedness(여기서는 한 점에서의 boundedness)가 빠지면 결론이 무너진다. 상수함수열 $f_n\equiv n$은 $L=0$으로 균등 Lipschitz이지만, 모든 점에서 $f_n(x)=n\rightarrow\infty$이므로 점별수렴하는 부분수열조차 없다. 반대로 Lipschitz 조건이 빠져도 무너진다는 것이 [예시 8](#ex8)이다. 두 조건은 각각 [정리 6](#thm6)의 두 가정에 대응하며, 어느 쪽도 다른 쪽으로 대신할 수 없다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
