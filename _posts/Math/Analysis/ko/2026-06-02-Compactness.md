---
title: "컴팩트성"
description: "거리공간에서 open cover에 의한 compactness와 sequential compactness가 동치이며, 이는 complete이면서 totally bounded인 것과도 동치임을 증명한다. 이로부터 ℝⁿ의 Heine–Borel 정리와 Cantor 교집합 정리를 얻고, 닫혀 있고 bounded이지만 compact가 아닌 반례를 정리한다."
excerpt: "거리공간에서의 compactness 동치 조건, Heine–Borel 정리, Cantor 교집합 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/compactness
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 10

published: false

---

[§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4){: data-lid="978rp" }는 bounded sequence에서 수렴하는 부분수열을 뽑았고, [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="5gtrf" }는 $\mathbb{R}$의 Cauchy sequence가 수렴함을 보였다. 이 글에서는 이 두 성질이 한 집합 위에서 함께 작동하기 위한 조건을 찾는다. 그 조건이 compactness이다. 해석학의 존재 정리는 대개 조건을 점점 더 잘 만족하는 점열을 만들고, 그 점열의 극한이 다시 집합 안에 있어 조건을 만족한다는 논증을 거친다. 극한이 반드시 집합 안에 존재하도록 보장하는 것이 compactness의 역할이다.

이 글에서 $(X,d)$는 거리공간이고, 거리공간의 subset은 제한된 거리를 가진 거리공간으로 본다. $B(x,r)=\{y\in X\mid d(x,y)<r\}$는 열린 공이다.

## Open cover와 sequential compactness

집합 $K\subseteq X$의 *open cover<sub>열린덮개</sub>*는 $X$의 열린집합들의 모임 $\mathcal{U}$로서 $K\subseteq\bigcup_{U\in\mathcal{U}}U$를 만족하는 것이다. $\mathcal{U}$의 부분모임이 여전히 $K$를 덮을 때 이를 *subcover*라 한다.

::: 정의 1
$K\subseteq X$가 *compact*라는 것은 $K$의 모든 open cover가 유한 subcover를 가지는 것이다.
:::

$K$ 자신을 거리공간으로 보아도 같은 개념이 된다. $K$의 열린집합은 $X$의 열린집합 $U$에 대한 $U\cap K$ 꼴이므로, $K$를 덮는 $X$의 열린집합들과 $K$를 덮는 $K$의 열린집합들이 서로 대응하기 때문이다. 따라서 compactness는 $K$가 어느 공간 안에 놓여 있는지에 의존하지 않는 성질이다.

개구간 $(0,1)$은 compact가 아니다. $U_n=(1/n,1)$ $(n\geq 2)$로 이루어진 모임은 $(0,1)$을 덮지만, 유한개의 $U_n$의 합집합은 가장 큰 첨자 $N$에 대해 $U_N$과 같아서 $(0,1/N]$을 놓친다. 같은 방식으로 $\mathbb{R}$은 열린 구간 $(-n,n)$들로 덮어 보면 compact가 아님을 알 수 있다. 이처럼 open cover의 정의는 반례를 보이기에는 직접적이지만, compact임을 보이거나 compact 집합에서 결론을 끌어내기에는 점열 쪽이 다루기 쉽다.

::: 정의 2
$K\subseteq X$가 *sequentially compact*라는 것은 $K$의 점으로 이루어진 모든 점열이 $K$의 점으로 수렴하는 부분수열을 가지는 것이다.
:::

극한이 $K$ 안에 있어야 한다는 조건이 핵심이다. $x_n=1/n$은 $(0,1)$의 점열이지만 모든 부분수열이 $0\notin(0,1)$로 수렴하므로, $(0,1)$은 sequentially compact가 아니다.

거리공간이 *complete*라는 것은 모든 Cauchy sequence가 수렴하는 것이다. 이에 더해 다음 조건이 필요하다.

::: 정의 3
$K\subseteq X$가 *totally bounded*라는 것은 임의의 $\varepsilon>0$에 대해 $K$가 중심이 $K$에 있고 반지름이 $\varepsilon$인 유한개의 열린 공으로 덮이는 것이다.
:::

Totally bounded이면 bounded이다. $\varepsilon=1$로 잡아 $K\subseteq B(c_1,1)\cup\cdots\cup B(c_k,1)$이라 하고 $R=\max_i d(c_1,c_i)+1$이라 두면, 삼각부등식에 의해 $K\subseteq B(c_1,R)$이다. 역은 성립하지 않는다. 아래 [예시 8](#ex8){: data-lid="7h2hg" }이 그 반례이다.

## 거리공간에서의 동치 조건

Open cover의 정의에서 sequential compactness를 끌어내려면 Lebesgue 수라는 보조 도구가 필요하다.

::: 보조정리 4 (Lebesgue number lemma)
$X$가 sequentially compact 거리공간이고 $\mathcal{U}$가 $X$의 open cover이면, 어떤 $\delta>0$이 존재하여 반지름이 $\delta$인 모든 열린 공 $B(x,\delta)$가 $\mathcal{U}$의 어떤 원소에 포함된다.
:::

::: 증명
그런 $\delta$가 없다고 하자. 그러면 각 $n$에 대해 $B(x_n,1/n)$이 $\mathcal{U}$의 어느 원소에도 포함되지 않는 $x_n\in X$가 있다. $X$가 sequentially compact이므로 부분수열 $x_{n_k}\to x\in X$를 얻는다. $\mathcal{U}$가 $X$를 덮으므로 $x\in U$인 $U\in\mathcal{U}$가 있고, $U$가 열려 있으므로 $B(x,r)\subseteq U$인 $r>0$이 있다. $k$를 $d(x_{n_k},x)<r/2$이고 $1/n_k<r/2$가 되도록 크게 잡으면, $y\in B(x_{n_k},1/n_k)$에 대해

$$d(y,x)\leq d(y,x_{n_k})+d(x_{n_k},x)<\frac{r}{2}+\frac{r}{2}=r$$

이므로 $B(x_{n_k},1/n_k)\subseteq B(x,r)\subseteq U$이다. 이는 $x_{n_k}$의 선택에 모순된다.
:::

$\delta$를 고르는 방식은 반례를 부정하여 $1/n$ 크기의 공을 쓰는 것이며, 이것이 점열로 옮겨 가는 통로가 된다.

::: 정리 5
거리공간 $X$에 대해 다음 세 조건은 동치이다.

1. $X$는 compact이다.
2. $X$는 sequentially compact이다.
3. $X$는 complete이고 totally bounded이다.
:::

::: 증명
(1)⇒(2). $(x_n)$이 수렴하는 부분수열을 갖지 않는다고 하자. 먼저 각 $p\in X$에 대해, $x_n\in B(p,r_p)$인 첨자 $n$이 유한개뿐인 $r_p>0$이 존재한다. 그렇지 않으면 모든 $k$에 대해 $B(p,1/k)$가 무한히 많은 첨자의 항을 포함하므로, 첨자 $n_1<n_2<\cdots$를 $d(x_{n_k},p)<1/k$가 되게 잡을 수 있고 이때 $x_{n_k}\to p$가 되어 가정에 모순된다. 열린 공 $B(p,r_p)$들은 $X$를 덮으므로 유한 subcover $B(p_1,r_{p_1}),\dots,B(p_N,r_{p_N})$이 있다. 그러면 모든 첨자 $n$은 이 유한개의 공 중 하나에 항을 넣는 첨자인데, 각 공에 대해 그런 첨자가 유한개뿐이므로 첨자 전체가 유한집합이 되어 모순이다.

(2)⇒(3). Complete임을 보인다. Cauchy sequence $(x_n)$이 부분수열 $x_{n_k}\to x$를 가진다고 하자. $\varepsilon>0$에 대해 $n,m\geq N$이면 $d(x_n,x_m)<\varepsilon/2$인 $N$을 잡고, $n_k\geq N$이면서 $d(x_{n_k},x)<\varepsilon/2$인 $k$를 고르면, $n\geq N$에 대해 $d(x_n,x)\leq d(x_n,x_{n_k})+d(x_{n_k},x)<\varepsilon$이다. 즉 $x_n\to x$이다. Totally bounded임을 보이기 위해, 어떤 $\varepsilon>0$에 대해 $X$가 $\varepsilon$-공 유한개로 덮이지 않는다고 하자. 임의의 $x_1$을 잡고, $x_1,\dots,x_n$이 정해졌다면 $B(x_1,\varepsilon)\cup\cdots\cup B(x_n,\varepsilon)\neq X$이므로 이 합집합 밖의 점을 $x_{n+1}$로 잡는다. 그러면 서로 다른 $i,j$에 대해 $d(x_i,x_j)\geq\varepsilon$이므로, 이 점열의 어떤 부분수열도 Cauchy sequence가 아니고 따라서 수렴하지 않는다. 이는 (2)에 모순된다.

(3)⇒(2). $(x_n)$을 임의의 점열이라 하자. $X$가 반지름 $1$인 공 유한개로 덮이므로, 그중 한 공이 무한히 많은 $n$에 대해 $x_n$을 포함한다. 그런 첨자의 집합을 $I_1$이라 하자. $X$를 반지름 $1/2$인 공 유한개로 덮고, $I_1$의 원소 $n$ 중 $x_n$이 같은 공에 속하는 것이 무한히 많은 공 하나를 택하여 그 첨자 집합을 $I_2\subseteq I_1$이라 한다. 같은 과정을 반복하여, 무한집합 $I_1\supseteq I_2\supseteq\cdots$이면서 $I_k$의 모든 $n$에 대해 $x_n$이 반지름 $1/k$인 한 공에 놓이는 것을 얻는다. 따라서 $n,m\in I_k$이면 $d(x_n,x_m)<2/k$이다. 이제 $n_1<n_2<\cdots$를 $n_k\in I_k$가 되도록 고르면, $j\geq k$일 때 $n_j\in I_j\subseteq I_k$이므로 $d(x_{n_j},x_{n_k})<2/k$이다. 즉 $(x_{n_k})$는 Cauchy sequence이고, $X$가 complete이므로 수렴한다.

(2)⇒(1). $\mathcal{U}$를 $X$의 open cover라 하자. [보조정리 4](#lem4){: data-lid="zs5z3" }에서 $\delta>0$을 얻는다. (2)⇒(3)에서 보았듯 $X$는 totally bounded이므로 $X=B(c_1,\delta)\cup\cdots\cup B(c_N,\delta)$인 $c_1,\dots,c_N$이 있다. 각 $B(c_i,\delta)$는 $\mathcal{U}$의 어떤 원소 $U_i$에 포함되므로, $U_1,\dots,U_N$이 $X$를 덮는다.
:::

(3)⇒(2)에서 반지름을 $1/k$로 줄여 가는 것은 같은 공에 속하는 항들 사이의 거리를 $0$으로 보내기 위함이고, 중첩 $I_{k+1}\subseteq I_k$는 하나의 부분수열이 모든 $k$에 대해 동시에 쓰이게 하기 위함이다. 이 논증은 [§부분수열과 Bolzano–Weierstrass 정리, ⁋정리 4](/ko/math/analysis/bolzano_weierstrass#thm4){: data-lid="ke1tr" }에서 쓰인 구간 나누기 논증을 일반 거리공간으로 옮긴 것으로 볼 수 있다.

이 동치 때문에 이하에서는 거리공간의 subset에 대해 compact와 sequentially compact를 구별하지 않고 compact라 부른다. 다음 명제는 모든 거리공간에서 성립하는 필요조건이다.

::: 명제 6
거리공간 $X$의 compact subset $K$는 닫혀 있고 bounded이다.
:::

::: 증명
[정리 5](#thm5){: data-lid="m8oso" }에 의해 $K$는 totally bounded이므로 bounded이다. 닫혀 있음을 보이기 위해 $K$의 점열 $x_n\to x\in X$를 잡는다([§거리공간과 열린집합·닫힌집합, ⁋명제 12](/ko/math/analysis/metric_spaces#prop12){: data-lid="a2saj" }에서 보았듯 닫힌집합은 이런 극한을 모두 포함하는 집합이다). $K$가 sequentially compact이므로 부분수열 $x_{n_k}$가 $K$의 점 $y$로 수렴하는데, 수렴하는 점열의 부분수열은 [§부분수열과 Bolzano–Weierstrass 정리, ⁋명제 2](/ko/math/analysis/bolzano_weierstrass#prop2){: data-lid="l3pxi" }에 의하여 같은 극한으로 수렴하고 극한은 [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2){: data-lid="7onxz" }에 의하여 유일하므로 $x=y\in K$이다.
:::

## Heine–Borel 정리

$\mathbb{R}^n$에서는 [명제 6](#prop6){: data-lid="o6nle" }의 역이 성립한다. 유클리드 노름에 대해 bounded 집합이 언제나 totally bounded가 된다는 것이 이유이다.

::: 정리 7 (Heine–Borel)
$K\subseteq\mathbb{R}^n$이 compact인 것은 $K$가 닫혀 있고 bounded인 것과 동치이다.
:::

::: 증명
(⇒)는 [명제 6](#prop6){: data-lid="2usxj" }이다. (⇐)를 보이기 위해 $K$가 닫혀 있고 $K\subseteq[-R,R]^n$이라 하고, [정리 5](#thm5){: data-lid="l7l4m" }에 의해 $K$가 complete이고 totally bounded임을 확인한다.

Complete임을 보인다. $(x_m)$이 $K$의 Cauchy sequence이면 $\lvert x_m^{(j)}-x_l^{(j)}\rvert\leq\lVert x_m-x_l\rVert$이므로 각 좌표열이 $\mathbb{R}$의 Cauchy sequence이고, $\mathbb{R}$이 complete이므로([§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4){: data-lid="2tmsi" }) $x_m^{(j)}\to\xi_j$이다. $x=(\xi_1,\dots,\xi_n)$이라 두면 $\lVert x_m-x\rVert^2=\sum_j\lvert x_m^{(j)}-\xi_j\rvert^2\to0$이므로 $x_m\to x$이고, $K$가 닫혀 있으므로 $x\in K$이다.

Totally bounded임을 보인다. $\varepsilon>0$이 주어졌다고 하자. 정수 $N>R\sqrt{n}/\varepsilon$를 잡고 각 좌표구간 $[-R,R]$를 길이 $2R/N$인 $N$개의 구간으로 나누면, $[-R,R]^n$이 $N^n$개의 작은 상자로 나뉜다. 상자의 중심 $c$에 대해 상자 안의 점 $y$는 각 좌표에서 $\lvert y_j-c_j\rvert\leq R/N$이므로 $\lVert y-c\rVert\leq R\sqrt{n}/N<\varepsilon$이다. 따라서 $K$는 $N^n$개의 공 $B(c,\varepsilon)$으로 덮인다. 이 중 $K$와 만나는 공마다 $K\cap B(c,\varepsilon)$의 점 $k_c$를 하나 고르면 $B(c,\varepsilon)\subseteq B(k_c,2\varepsilon)$이므로, $K$는 중심이 $K$에 있고 반지름이 $2\varepsilon$인 유한개의 공으로 덮인다. $\varepsilon$이 임의였으므로 $K$는 totally bounded이다.
:::

가령 닫힌구간 $[a,b]$, 닫힌 공, 닫힌 직육면체는 모두 compact이다. 반면 $(0,1)$은 닫혀 있지 않고 $[0,\infty)$는 bounded가 아니므로 compact가 아니다. 한편 $\{0\}\cup\{1/m\mid m\geq1\}$은 닫혀 있고 bounded이므로 compact이다. 이 집합에서 $0$을 빼면 compact가 아니게 되는 점이 닫힘 조건의 역할을 보여 준다.

[정리 7](#thm7){: data-lid="fvwff" }의 증명에서 유한 차원이 쓰인 곳은 bounded 집합이 totally bounded가 되는 단계, 곧 유한개의 작은 상자로 나누는 부분이다. 이 단계가 무너지는 경우를 아래 두 예시가 보여 준다. Heine–Borel 정리의 "닫혀 있고 bounded"는 $\mathbb{R}^n$이라는 특정 공간의 성질이며, 일반 거리공간에서는 필요조건일 뿐이다.

::: 예시 8 (이산거리)
무한집합 $X$에 이산거리 $d(x,y)=1$ $(x\neq y)$, $d(x,x)=0$을 주면, $X$는 닫혀 있고 $X\subseteq B(x_0,2)$로 bounded이지만 compact가 아니다. 열린 공 $B(x,1/2)=\{x\}$들이 $X$의 open cover를 이루는데 유한 subcover가 없기 때문이다. 같은 이유로 $\varepsilon=1/2$에 대해 $X$는 유한개의 $\varepsilon$-공으로 덮이지 않아 totally bounded가 아니다.
:::

::: 예시 9 ($C[0,1]$의 닫힌 단위공)
$C[0,1]$에 거리 $d(f,g)=\max_{x\in[0,1]}\lvert f(x)-g(x)\rvert$를 주고 $\lVert f\rVert=d(f,0)$이라 하자. 닫힌 단위공 $\{f\mid\lVert f\rVert\leq1\}$은 닫혀 있고 bounded이지만 compact가 아니다. 이를 보이기 위해 구간 $[1/(n+1),1/n]$의 중점을 $c_n$, 반길이를 $h_n$이라 하고

$$e_n(x)=\max\Bigl(0,1-\frac{\lvert x-c_n\rvert}{h_n}\Bigr)$$

로 정의한다. $e_n$은 $[1/(n+1),1/n]$ 밖에서 $0$이고 $c_n$에서 값 $1$을 가지므로 $\lVert e_n\rVert=1$이다. 서로 다른 구간들은 끝점에서만 만나므로 $n\neq m$이면 $e_m(c_n)=0$이고, 따라서 $d(e_n,e_m)\geq\lvert e_n(c_n)-e_m(c_n)\rvert=1$이다. 점들 사이의 거리가 모두 $1$ 이상이므로 $(e_n)$의 어떤 부분수열도 Cauchy sequence가 아니고, 수렴하지 않는다.

$\mathbb{R}^n$에서는 bounded 점열이 수렴하는 부분수열을 갖지만, 함수공간에서는 이 성질이 깨진다. $e_n$이 서로 다른 구간에 봉우리를 하나씩 세워 서로 멀어지는 것이 원인이다.
:::

## Cantor 교집합 정리

닫힌 구간이 $[a_1,b_1]\supseteq[a_2,b_2]\supseteq\cdots$ 꼴로 줄어들면 공통부분이 비어 있지 않다는 [§부분수열과 Bolzano–Weierstrass 정리, ⁋보조정리 5](/ko/math/analysis/bolzano_weierstrass#lem5){: data-lid="maj83" }가 compact 집합 일반으로 확장된다.

::: 정리 10 (Cantor 교집합 정리)
거리공간 $X$에서 $K_1\supseteq K_2\supseteq\cdots$이 비어 있지 않은 compact 집합들의 감소열이면, $\bigcap_{n\geq1}K_n\neq\emptyset$이다.
:::

::: 증명
각 $n$에서 $x_n\in K_n$을 고른다. 모든 $x_n$이 $K_1$에 속하고 $K_1$이 sequentially compact이므로, 부분수열 $x_{n_k}$가 $x\in K_1$로 수렴한다. 고정된 $N$에 대해 $n_k\geq N$이면 $x_{n_k}\in K_N$이므로, $x$는 $K_N$의 점열의 극한이다. $K_N$은 [명제 6](#prop6){: data-lid="x9v9g" }에 의해 닫혀 있으므로 $x\in K_N$이다. $N$이 임의였으므로 $x\in\bigcap_nK_n$이다.
:::

가정이 하나라도 빠지면 결론이 무너진다. Compactness가 없는 경우, $K_n=(0,1/n)$은 비어 있지 않고 감소하지만 교집합이 공집합이다. 이 경우 $x_n=1/(2n)$의 극한 $0$이 집합 밖으로 빠져나간다. $K_n=[n,\infty)$는 닫혀 있고 비어 있지 않으나 bounded가 아니어서 교집합이 공집합이고, 이 경우에는 $x_n=n$이 수렴하는 부분수열을 갖지 못한다. $\mathbb{R}$에서는 닫힌 구간의 감소열이 이 정리의 가장 흔한 사례이다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
