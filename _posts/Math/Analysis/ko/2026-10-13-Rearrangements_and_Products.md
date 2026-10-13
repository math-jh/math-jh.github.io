---
title: "급수의 재배열과 곱"
description: "Abel 부분합 공식에서 Dirichlet 판정법과 Abel 판정법을 얻고, 절대수렴급수는 재배열해도 합이 변하지 않지만 조건수렴급수는 Riemann 재배열 정리에 의해 임의의 값으로 수렴하게 재배열됨을 보인다. 이어서 Cauchy 곱의 수렴을 Mertens 정리로 다루고, 두 급수가 모두 조건수렴이면 Cauchy 곱이 발산할 수 있음을 반례로 보인다."
excerpt: "Abel 부분합, Dirichlet·Abel 판정법, Riemann 재배열 정리, Cauchy 곱과 Mertens 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/rearrangements_and_products
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 7

published: false

---

유한 개의 수는 더하는 순서를 바꿔도 합이 같고, 두 유한합의 곱은 항별 곱을 모두 더한 것과 같다. [§무한급수와 수렴판정법, ⁋정의 1](/ko/math/analysis/series#def1)에서 다룬 무한급수는 부분합 수열의 극한이므로 이 두 성질이 자동으로 따라오지 않는다. 이 글에서는 어떤 조건에서 두 성질이 유지되는지를 정확히 가려낸다. 그 과정에서 [§무한급수와 수렴판정법, ⁋정리 16](/ko/math/analysis/series#thm16)을 일반화하는 Dirichlet 판정법과 Abel 판정법이 필요하므로 이들을 먼저 다룬다. 이 글에서 급수의 항은 실수이고, 수렴하는 급수의 합은 부분합 수열의 극한이다.

## Abel 부분합 공식

수열 $(a_k)$에 대하여 $A_n=\sum_{k=1}^n a_k$, $A_0=0$으로 두자. 곱 $a_kb_k$의 합을 $a_k=A_k-A_{k-1}$로 바꿔 쓰면 $b_k$의 차분이 나타난다. 이는 적분의 부분적분을 합으로 옮긴 것에 해당한다.

::: 정리 1 (Abel 부분합 공식)
두 수열 $(a_k)$, $(b_k)$와 $1\le p\le q$에 대하여 다음이 성립한다.
$$\sum_{k=p}^q a_kb_k=A_qb_q-A_{p-1}b_p-\sum_{k=p}^{q-1}A_k(b_{k+1}-b_k).$$
:::

::: 증명
$a_k=A_k-A_{k-1}$을 대입하고 둘째 합의 첨자를 하나 옮기면 된다.
$$\begin{aligned}
\sum_{k=p}^q a_kb_k&=\sum_{k=p}^q A_kb_k-\sum_{k=p}^q A_{k-1}b_k\\
&=\sum_{k=p}^q A_kb_k-\sum_{k=p-1}^{q-1}A_kb_{k+1}\\
&=A_qb_q-A_{p-1}b_p+\sum_{k=p}^{q-1}A_k(b_k-b_{k+1}).
\end{aligned}$$
마지막 합의 부호를 바꾸면 주어진 식이 된다.
:::

## Dirichlet 판정법과 Abel 판정법

[§무한급수와 수렴판정법, ⁋정리 16](/ko/math/analysis/series#thm16)은 항의 부호가 번갈아 바뀌므로 $a_k=(-1)^k$의 부분합이 $0$ 또는 $\pm1$에 머무른다는 사실에 기대고 있다. 부분합이 bounded이기만 하면 충분하다는 것이 다음 정리이다.

::: 정리 2 (Dirichlet 판정법)
급수 $\sum a_n$의 부분합 $A_n$이 bounded이고, 수열 $(b_n)$이 감소하며 $0$으로 수렴하면 $\sum a_nb_n$은 수렴한다.
:::

::: 증명
$\lvert A_n\rvert\le M$이 모든 $n$에 대해 성립한다고 하자. $b_n$은 $0$으로 감소하므로 모든 $n$에 대해 $b_n\ge0$이고 $b_k-b_{k+1}\ge0$이다. [정리 1](#thm1)에 의하여 $1\le p\le q$에 대해 다음을 얻는다.
$$\begin{aligned}
\Bigl\lvert\sum_{k=p}^q a_kb_k\Bigr\rvert&\le Mb_q+Mb_p+M\sum_{k=p}^{q-1}(b_k-b_{k+1})\\
&=Mb_q+Mb_p+M(b_p-b_q)=2Mb_p.
\end{aligned}$$
$\varepsilon>0$이 주어지면 $b_n\to0$이므로 $2Mb_N<\varepsilon$인 $N$이 있다. $b_n$이 감소하므로 $q\ge p\ge N$이면 $\lvert\sum_{k=p}^q a_kb_k\rvert\le 2Mb_p\le2Mb_N<\varepsilon$이다. 따라서 $\sum a_nb_n$은 [§무한급수와 수렴판정법, ⁋정리 3](/ko/math/analysis/series#thm3)에 의하여 수렴한다. $\varepsilon$을 $2Mb_N$과 비교할 수 있도록 $N$을 고르는 것이 이 증명의 유일한 선택이며, 위 부등식이 $b_p$만으로 상계되기 때문에 $N$이 $p,q$와 무관하게 정해진다.
:::

[§무한급수와 수렴판정법, ⁋정리 16](/ko/math/analysis/series#thm16)은 $a_n=(-1)^{n}$으로 놓은 특수한 경우이다. 이 경우 $\lvert A_n\rvert\le1$이다. $b_n$의 단조성은 빠질 수 없다. $a_n=(-1)^n$에 대해 $b_n$이 홀수 번째에서 $1/n$, 짝수 번째에서 $1/n^2$이면 $b_n\to0$이지만 $\sum a_nb_n=\sum_{n\text{ even}}1/n^2-\sum_{n\text{ odd}}1/n$은 $-\infty$로 발산한다.

다음은 $\sum a_n$ 자체가 수렴하는 경우이고, $b_n$에는 $0$으로의 수렴 대신 단조이고 bounded라는 조건만 요구한다.

::: 정리 3 (Abel 판정법)
급수 $\sum a_n$이 수렴하고 수열 $(b_n)$이 단조이며 bounded이면 $\sum a_nb_n$은 수렴한다.
:::

::: 증명
단조이고 bounded인 $(b_n)$은 [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8)에 의하여 수렴한다. 극한을 $b$라 하자. $a_nb_n=a_nb+a_n(b_n-b)$이고 $\sum a_nb=b\sum a_n$은 수렴하므로 $\sum a_n(b_n-b)$가 수렴함을 보이면 충분하다. $(b_n)$이 감소하면 $b_n-b$가 $0$으로 감소하고, 증가하면 $b-b_n$이 $0$으로 감소한다. $\sum a_n$이 수렴하므로 부분합이 [§수열의 수렴, ⁋명제 3](/ko/math/analysis/convergence_of_sequences#prop3)에 의하여 bounded이다. 따라서 [정리 2](#thm2)가 $\sum a_n(b_n-b)$ 또는 $\sum a_n(b-b_n)$에 적용되고, 어느 쪽이든 $\sum a_n(b_n-b)$는 수렴한다.
:::

가령 $\sum(-1)^n/n$이 수렴하므로 단조이고 bounded인 $b_n=(1+1/n)^n$ 또는 $b_n=\arctan n$에 대해서도 $\sum(-1)^nb_n/n$이 수렴한다. 이처럼 $b_n$의 단조성만 확인되면 $b_n$의 구체적인 식을 몰라도 수렴이 따라온다.

::: 예시 4 ($\sum\sin n/n$)
급수 $\sum_{n=1}^\infty\sin n/n$은 수렴하지만 절대수렴하지 않는다.

수렴은 [정리 2](#thm2)로 보인다. $2\sin(1/2)\sin k=\cos(k-1/2)-\cos(k+1/2)$이므로 $a_k=\sin k$의 부분합은 소거되어 다음과 같다.
$$\sum_{k=1}^n\sin k=\frac{\cos(1/2)-\cos(n+1/2)}{2\sin(1/2)}.$$
따라서 $\lvert A_n\rvert\le1/\sin(1/2)$이고, $b_n=1/n$은 $0$으로 감소하므로 $\sum\sin n/n$이 수렴한다.

절대수렴하지 않음은 $\lvert\sin n\rvert\ge\sin^2n=(1-\cos2n)/2$에서 따라온다. 이로부터 $\lvert\sin n\rvert/n\ge1/(2n)-\cos(2n)/(2n)$이다. 같은 방식으로 $2\sin1\cos2k=\sin(2k+1)-\sin(2k-1)$이므로 $\sum_{k=1}^n\cos2k=(\sin(2n+1)-\sin1)/(2\sin1)$이 bounded이고, [정리 2](#thm2)에 의해 $\sum\cos(2n)/n$은 수렴한다. 반면 $\sum1/(2n)$은 [§무한급수와 수렴판정법, ⁋예시 4](/ko/math/analysis/series#ex4)에 의하여 발산하므로 $\sum\lvert\sin n\rvert/n$도 발산한다.
:::

## 절대수렴급수의 재배열

전단사 $\sigma:\mathbb N\to\mathbb N$에 대하여 급수 $\sum a_{\sigma(n)}$을 $\sum a_n$의 *재배열<sub>rearrangement</sub>*이라 한다. 같은 항을 모두 한 번씩 쓰되 순서만 바꾼 급수이다. [§무한급수와 수렴판정법, ⁋정의 11](/ko/math/analysis/series#def11)의 절대수렴하는 급수에서는 이 순서가 합에 영향을 주지 않는다.

::: 정리 5 (절대수렴급수의 재배열)
급수 $\sum a_n$이 절대수렴하고 합이 $s$이면, 모든 재배열 $\sum a_{\sigma(n)}$도 $s$로 수렴한다.
:::

::: 증명
$s_N=\sum_{n=1}^Na_n$, $t_m=\sum_{k=1}^ma_{\sigma(k)}$로 두자. $\varepsilon>0$이 주어지면 $\sum\lvert a_n\rvert$이 수렴하므로 $\sum_{n>N}\lvert a_n\rvert<\varepsilon$인 $N$이 있다. 이 꼬리의 크기가 두 가지 오차를 동시에 통제하도록 $N$을 정한다. $\sigma$가 전사이므로 $\sigma(k)\le N$인 $k$의 최댓값이 존재하고, 이를 $M$이라 하자. 그럼 $m\ge M$일 때 $\{\sigma(1),\dots,\sigma(m)\}\supseteq\{1,\dots,N\}$이다. 따라서 $t_m-s_N$에는 $a_1,\dots,a_N$이 정확히 상쇄되어 남고, 남는 항은 $\sigma(k)>N$인 $a_{\sigma(k)}$들의 합이다. $\sigma$는 단사이므로 이 항들은 서로 다른 $a_n$ ($n>N$)이고,
$$\lvert t_m-s_N\rvert\le\sum_{n>N}\lvert a_n\rvert<\varepsilon$$
이다. 또한 $\lvert s_N-s\rvert\le\sum_{n>N}\lvert a_n\rvert<\varepsilon$이므로 $m\ge M$이면 $\lvert t_m-s\rvert<2\varepsilon$이다.
:::

이 정리의 가정은 약해질 수 없다. 다음 예시는 조건수렴하는 교대조화급수의 합이 재배열로 바뀌는 구체적인 경우이다. 여기서는 $\sum_{n=1}^\infty(-1)^{n+1}/n=\ln2$인 알려진 사실을 쓴다.

::: 예시 6 (교대조화급수의 재배열)
$\ln2=1-1/2+1/3-1/4+\cdots$에서 홀수 번째 항 하나 뒤에 짝수 번째 항 둘을 놓는 재배열
$$1-\frac12-\frac14+\frac13-\frac16-\frac18+\frac15-\frac1{10}-\frac1{12}+\cdots$$
은 $(\ln2)/2$로 수렴한다.

이 급수는 홀수 번째 항 $1/(2k-1)$을 순서대로, 짝수 번째 항 $-1/(2j)$를 순서대로 쓰되 $k$번째 묶음에 $-1/(4k-2)$와 $-1/(4k)$를 넣은 것이므로 실제로 재배열이다. $k$번째 묶음의 합은
$$\frac1{2k-1}-\frac1{4k-2}-\frac1{4k}=\frac1{4k-2}-\frac1{4k}=\frac12\Bigl(\frac1{2k-1}-\frac1{2k}\Bigr)$$
이고, $k$에 대해 더하면 $\frac12\sum_{k\ge1}\Bigl(\frac1{2k-1}-\frac1{2k}\Bigr)=(\ln2)/2$이다. 항이 $0$으로 수렴하므로 묶음 사이의 부분합도 같은 극한을 가진다.
:::

## Riemann 재배열 정리

[예시 6](#ex6)의 현상은 조건수렴급수 전반에 일어난다. 조건수렴하는 실수 급수는 모든 실수를 합으로 가지도록 재배열할 수 있다.

::: 정리 7 (Riemann 재배열 정리)
실수 급수 $\sum a_n$이 수렴하지만 절대수렴하지 않으면, 모든 $s\in\mathbb R$에 대하여 $s$로 수렴하는 재배열이 존재한다.
:::

::: 증명
$p_n=\max(a_n,0)$, $q_n=\max(-a_n,0)$로 두면 $a_n=p_n-q_n$, $\lvert a_n\rvert=p_n+q_n$이다.

먼저 $\sum p_n=\sum q_n=\infty$임을 보인다. 둘 다 수렴하면 $\sum\lvert a_n\rvert=\sum(p_n+q_n)$이 수렴하여 가정에 모순이다. 하나만 수렴하면 부분합 $\sum_{n\le N}a_n=\sum_{n\le N}p_n-\sum_{n\le N}q_n$이 $+\infty$ 또는 $-\infty$로 발산하여 $\sum a_n$이 수렴한다는 가정에 모순이다.

$a_n\ge0$인 항들을 원래 순서대로 $P_1,P_2,\dots$, $a_n<0$인 항들의 절댓값을 원래 순서대로 $Q_1,Q_2,\dots$라 하자. $\sum p_n=\infty$이므로 $P_k$는 무한히 많고 $\sum P_k=\infty$이며, 마찬가지로 $\sum Q_k=\infty$이다. 또 $\sum a_n$이 수렴하므로 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2)에 의하여 $a_n\to0$이고, 부분수열인 $P_k$와 $Q_k$도 [§부분수열과 Bolzano–Weierstrass 정리, ⁋명제 2](/ko/math/analysis/bolzano_weierstrass#prop2)에 의하여 $0$으로 수렴한다.

목표값 $s$를 향해 다음과 같이 항을 쓴다. 먼저 $P_1+\cdots+P_{m_1}>s$를 만족하는 최소의 $m_1\ge1$까지 $P$를 쓴다. 그다음 합이 $s$ 아래로 내려갈 때까지 $Q_1,Q_2,\dots$를 하나씩 빼서, 합이 처음으로 $s$보다 작아지는 $Q_{n_1}$에서 멈춘다. 이어서 합이 처음으로 $s$를 넘을 때까지 $P_{m_1+1},\dots$를 더하고, 다시 $Q_{n_1+1},\dots$를 빼서 처음으로 $s$ 아래로 내려가면 멈춘다. 이를 되풀이한다. $\sum P_k$와 $\sum Q_k$가 모두 $+\infty$로 발산하므로 각 단계는 반드시 끝난다. 각 단계는 직전 단계가 합을 $s$의 반대편에 두었기 때문에 항을 적어도 하나 쓰며, 단계가 무한히 많으므로 모든 $P_k$와 $Q_k$가 한 번씩 쓰인다. 따라서 얻은 급수는 $\sum a_n$의 재배열이다.

이 급수가 $s$로 수렴함을 보인다. 단계를 $j=1,2,\dots$로 세고, $T_n$을 재배열된 급수의 $n$번째 부분합, $d_j$를 $j$번째 단계의 마지막 항의 크기라 하자. $j\ge2$이면 $j$번째 단계는 합이 $s$보다 작은 상태(또는 $s$보다 큰 상태)에서 시작하고, 마지막 항을 쓰기 직전까지 합이 $s$ 이하(또는 $s$ 이상)에 머문다. 따라서 단계가 끝날 때의 합은 $s$의 반대쪽에 있고 $s$와의 거리가 $d_j$ 이하이다. 한 단계 안에서 부분합은 단조이므로 그 단계의 모든 부분합은 단계의 처음과 끝의 합 사이에 놓이고, $j\ge2$인 단계 $j$ 안의 모든 $n$에 대해 $\lvert T_n-s\rvert\le\max(d_{j-1},d_j)$이다. 한 단계마다 $P$ 또는 $Q$의 번호가 새로 올라가므로 $d_j$는 번호가 $j/2$ 이상인 $P_k$ 또는 $Q_k$이고, $P_k,Q_k\to0$이므로 $d_j\to0$이다. 따라서 $T_n\to s$이다.
:::

같은 구성에서 목표값을 단계마다 바꾸면, 합이 $+\infty$ 또는 $-\infty$로 발산하는 재배열과 부분합이 주어진 두 값 사이를 오가는 재배열도 얻는다. [정리 5](#thm5)와 합치면, 실수 급수가 절대수렴한다는 것은 모든 재배열이 수렴한다는 것과 같다. 한 방향은 [정리 5](#thm5)이고, 다른 방향은 조건수렴이면 [정리 7](#thm7)에 의해 서로 다른 합을 갖는 재배열이 있기 때문이다.

## Cauchy 곱과 Mertens 정리

두 유한합의 곱은 $a_ib_j$를 모두 더한 것이다. 이를 급수에 적용할 때는 $a_ib_j$를 어떤 순서로 더해야 하며, 합을 $i+j$가 같은 항끼리 묶는 방식이 멱급수의 곱과 맞물려 자연스럽다.

::: 정의 8 (Cauchy 곱)
첨자가 $0$부터 시작하는 두 급수 $\sum_{n=0}^\infty a_n$, $\sum_{n=0}^\infty b_n$에 대하여
$$c_n=\sum_{k=0}^na_kb_{n-k}$$
로 정의한 급수 $\sum_{n=0}^\infty c_n$을 두 급수의 *Cauchy 곱<sub>Cauchy product</sub>*이라 한다.
:::

두 급수가 모두 수렴해도 Cauchy 곱이 수렴하는지는 별개의 문제이다. 그러나 한쪽이 절대수렴하면 충분하다.

::: 정리 9 (Mertens 정리)
급수 $\sum a_n$이 $A$로 절대수렴하고 $\sum b_n$이 $B$로 수렴하면, Cauchy 곱 $\sum c_n$은 $AB$로 수렴한다.
:::

::: 증명
$A_n=\sum_{k=0}^na_k$, $B_n=\sum_{k=0}^nb_k$, $C_n=\sum_{k=0}^nc_k$, $\beta_n=B_n-B$로 두자. $C_n$은 $a_ib_j$ ($i+j\le n$)의 합이므로 $i$를 고정한 합 $b_0+\cdots+b_{n-i}=B_{n-i}$로 묶으면
$$C_n=a_0B_n+a_1B_{n-1}+\cdots+a_nB_0$$
이다. $B_{n-i}=B+\beta_{n-i}$를 대입하면
$$C_n=A_nB+\gamma_n,\quad\gamma_n=a_0\beta_n+a_1\beta_{n-1}+\cdots+a_n\beta_0$$
이다. [§수열의 수렴, ⁋정리 5](/ko/math/analysis/convergence_of_sequences#thm5)에 의하여 $A_nB\to AB$이므로 $\gamma_n\to0$을 보이면 된다.

$\alpha=\sum\lvert a_n\rvert$이라 하고, $\beta_n\to0$이므로 [§수열의 수렴, ⁋명제 3](/ko/math/analysis/convergence_of_sequences#prop3)에 의하여 $\lvert\beta_n\rvert\le\beta^\ast$인 상수 $\beta^\ast$가 있다. $\varepsilon>0$이 주어지면 $n\ge N$에서 $\lvert\beta_n\rvert<\varepsilon$인 $N$을 잡는다. $n\ge N$에서 $\gamma_n$의 항을 $\beta$의 첨자 $n-k\ge N$인 부분과 $n-k<N$인 부분으로 나누면,
$$\lvert\gamma_n\rvert\le\sum_{k=0}^{n-N}\lvert a_k\rvert\lvert\beta_{n-k}\rvert+\sum_{j=0}^{N-1}\lvert a_{n-j}\rvert\lvert\beta_j\rvert\le\varepsilon\alpha+\beta^\ast\sum_{j=0}^{N-1}\lvert a_{n-j}\rvert$$
이다. 둘째 항은 $N$개의 항이 모두 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2)에 의하여 $a_m\to0$이므로 $n\to\infty$에서 $0$으로 간다. 따라서 $n$이 충분히 크면 $\lvert\gamma_n\rvert<\varepsilon(\alpha+1)$이고, $\varepsilon$이 임의이므로 $\gamma_n\to0$이다.
:::

$N$을 $n$과 무관하게 고정했기 때문에 둘째 합은 항의 개수가 $N$개로 일정하고, 각 항이 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2)에 의해 $0$으로 간다. 절대수렴 가정은 첫 합을 $\varepsilon\alpha$로 상계하는 데 쓰였다.

두 급수가 모두 절대수렴하면 Cauchy 곱도 절대수렴한다. $\sum_{n=0}^N\lvert c_n\rvert\le\sum_{n=0}^N\sum_{k=0}^n\lvert a_k\rvert\lvert b_{n-k}\rvert\le\bigl(\sum_{k=0}^N\lvert a_k\rvert\bigr)\bigl(\sum_{j=0}^N\lvert b_j\rvert\bigr)$이므로 부분합이 bounded이고, [§무한급수와 수렴판정법, ⁋명제 5](/ko/math/analysis/series#prop5)에 의하여 $\sum\lvert c_n\rvert$이 수렴하기 때문이다.

한쪽의 절대수렴을 생략하면 [정리 9](#thm9)는 성립하지 않는다.

::: 예시 10 (조건수렴급수의 Cauchy 곱)
$a_n=b_n=(-1)^n/\sqrt{n+1}$ ($n\ge0$)이면 $\sum a_n$, $\sum b_n$은 [§무한급수와 수렴판정법, ⁋정리 16](/ko/math/analysis/series#thm16)에 의하여 수렴하지만 Cauchy 곱은 발산한다.

Cauchy 곱의 항은
$$c_n=\sum_{k=0}^n\frac{(-1)^k(-1)^{n-k}}{\sqrt{k+1}\sqrt{n-k+1}}=(-1)^n\sum_{k=0}^n\frac1{\sqrt{(k+1)(n-k+1)}}$$
이다. 두 수 $k+1$과 $n-k+1$의 합이 $n+2$이므로 산술기하평균 부등식에서 $(k+1)(n-k+1)\le((n+2)/2)^2$이고, 각 항은 $2/(n+2)$ 이상이다. 항이 $n+1$개이므로
$$\lvert c_n\rvert\ge\frac{2(n+1)}{n+2}\ge1$$
이다. $c_n\not\to0$이므로 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2)에 의하여 $\sum c_n$은 발산한다.
:::

[예시 10](#ex10)에서 두 급수는 모두 조건수렴이다. 절대수렴 가정은 한쪽에만 있으면 되지만, 둘 다 없으면 이처럼 곱이 아예 수렴하지 않을 수 있다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
