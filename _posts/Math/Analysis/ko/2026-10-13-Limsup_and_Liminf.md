---
title: "상극한과 하극한"
description: "수열의 꼬리에서 취한 상한과 하한으로 상극한과 하극한을 정의하고, 이것이 부분수열 극한값 집합의 최댓값과 최솟값임을 증명한다. 수열이 수렴할 필요충분조건이 상극한과 하극한의 일치임을 보이고, 합에 대한 부등식과 등호가 실패하는 예를 다룬다."
excerpt: "꼬리의 sup/inf, 부분수열 극한값의 최대·최소, 수렴 ⇔ limsup=liminf, limsup(a_n+b_n)의 부등식"

categories: [Math / Analysis]
permalink: /ko/math/analysis/limsup_and_liminf
sidebar: 
    nav: "analysis-ko"

date: 2026-10-13
weight: 3

published: false

---

[§수열의 수렴, ⁋정의 1](/ko/math/analysis/convergence_of_sequences#def1){: data-lid="dm675" }의 극한은 수열이 수렴할 때에만 존재한다. $a_n = (-1)^n$처럼 진동하는 수열은 극한이 없지만, 그럼에도 $1$과 $-1$ 근처를 무한히 자주 방문한다는 정보를 가진다. 상극한과 하극한은 모든 실수열에 대해 정의되는 값으로, 이 정보를 하나의 수로 추출한다. 수열이 유계가 아니어도 의미를 갖도록 이 글에서는 $\pm\infty$를 값으로 허용하며, $\overline{\mathbb{R}} = \mathbb{R}\cup\{-\infty, +\infty\}$에 $-\infty < x < +\infty$ ($x\in\mathbb{R}$)로 순서를 준다. 위로 유계가 아닌 집합의 상한은 $+\infty$, 아래로 유계가 아닌 집합의 하한은 $-\infty$로 둔다. $a_n \to +\infty$는 임의의 $M\in\mathbb{R}$에 대해 어떤 $N$이 있어 $n\ge N$에서 $a_n > M$인 것을 뜻하고, $a_n\to-\infty$도 마찬가지이다.

## 꼬리의 상한과 하한

수열 $(a_n)$이 진동하면 $\sup_k a_k$는 앞쪽의 몇몇 항에 지배당한다. 가령 $a_n = 1/n$이면 $\sup_k a_k = 1$이지만 수열은 $0$으로 간다. 앞의 유한개 항을 버리고 $n$번째 항 이후만 보면 이 문제가 사라지므로, 버리는 항의 수를 늘려 가며 상한이 어디로 내려가는지를 본다.

::: 정의 1
실수열 $(a_n)_{n\ge 1}$에 대하여 $$u_n = \sup_{k\ge n} a_k,\quad l_n = \inf_{k\ge n} a_k \qquad (u_n, l_n\in\overline{\mathbb{R}})$$ 로 두고, *상극한<sub>limit superior</sub>*과 *하극한<sub>limit inferior</sub>*을 $$\limsup_{n\to\infty} a_n = \inf_{n\ge 1} u_n,\quad \liminf_{n\to\infty} a_n = \sup_{n\ge 1} l_n$$ 으로 정의한다.
:::

$n$이 커지면 상한을 취하는 집합 $\{a_k : k\ge n\}$이 줄어들므로 $u_n$은 감소(비증가)하고, 같은 이유로 $l_n$은 증가(비감소)한다. 따라서 [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8){: data-lid="12hus" }과 같은 이유로 $\inf_n u_n$은 $n\to\infty$일 때 $u_n$의 극한과 같고, $\sup_n l_n$은 $l_n$의 극한과 같다. 상극한과 하극한은 어떤 수열에 대해서도 $\overline{\mathbb{R}}$의 원소로 존재하며, 존재성 문제가 없다는 점이 극한과의 가장 큰 차이이다. 수열의 값 자체에 $\pm\infty$가 들어가지는 않는다. $\pm\infty$는 $u_n$, $l_n$ 또는 상극한, 하극한으로만 나타난다.

::: 명제 2
임의의 실수열 $(a_n)$에 대하여 다음이 성립한다.
1. $\liminf a_n \le \limsup a_n$.
2. $\liminf a_n = -\limsup(-a_n)$.
:::

::: 증명
(1) 임의의 $n, m$에 대하여 $k = \max(n,m)$으로 두면 $l_n \le a_k \le u_m$이다. $m$을 고정하고 $n$에 대해 상한을 취하면 $\liminf a_n\le u_m$이고, 이어서 $m$에 대해 하한을 취하면 (1)을 얻는다.

(2) $\sup_{k\ge n}(-a_k) = -\inf_{k\ge n} a_k$이므로 $(-a_n)$의 $u_n$은 $(a_n)$의 $-l_n$이다. 따라서 $\limsup(-a_n) = \inf_n(-l_n) = -\sup_n l_n = -\liminf a_n$이다.
:::

[명제 2](#prop2){: data-lid="hjhi6" }의 (2)에 의하여 하극한에 대한 결과는 상극한에 대한 결과에서 $a_n$을 $-a_n$으로 바꾸어 얻어진다. 이후 증명은 상극한에 대해서만 쓴다. (1)에서 등호가 성립하지 않는 것이 보통이다. 진동이 클수록 두 값의 차이가 벌어진다.

::: 예시 3
$a_n = (-1)^n(1+1/n)$의 상극한과 하극한을 구한다. 홀수 $k$에서는 $a_k<0$이고, 짝수 $k$에서는 $a_k = 1+1/k > 1$이며 이 값은 $k$에 대해 감소한다. $n$ 이상의 가장 작은 짝수를 $m$이라 하면, $n$ 이상의 항 중 양수는 짝수 번째 항뿐이고 그 최댓값이 $a_m$이므로 $u_n = 1 + 1/m$이다. $m\in\{n, n+1\}$이므로 $1 < u_n \le 1+1/n$이다. 따라서 $u_n$은 $1$로 수렴하고, 모든 $u_n$이 $1$보다 크므로 $\limsup a_n = 1$이다. 같은 방식으로 $n$ 이상의 가장 작은 홀수를 $m'$이라 하면 $l_n = -(1+1/m')$이고, $\liminf a_n = -1$이다.

이 예에서 $\sup_n a_n = a_2 = 3/2$, $\inf_n a_n = a_1 = -2$이므로 전체 상한과 상극한은 다르다. 또 $\limsup a_n = 1$은 수열의 어떤 항과도 같지 않다. 상극한은 항들이 모이는 곳을 가리키는 값이기 때문이다.
:::

수열이 유계가 아니면 $\pm\infty$가 나온다. $a_n = (-1)^n n$이면 $u_n = +\infty$이고 $l_n = -\infty$이므로 $\limsup a_n = +\infty$, $\liminf a_n = -\infty$이다. $a_n = n$이면 $l_n = n\to+\infty$이므로 상극한과 하극한이 모두 $+\infty$이다.

## 부분수열의 극한값

[예시 3](#ex3){: data-lid="4qpmg" }에서 상극한 $1$과 하극한 $-1$은 각각 짝수 번째 항들의 부분수열과 홀수 번째 항들의 부분수열의 극한이기도 하다. 이것이 일반적인 사실임을 보인다. 수열 $(a_n)$에 대하여 $n_1<n_2<\cdots$인 부분수열 $(a_{n_j})$가 $\overline{\mathbb{R}}$의 원소 $L$로 수렴할 때 $L$을 $(a_n)$의 *부분수열 극한값*이라 하고, 그 전체의 집합을 $E\subseteq\overline{\mathbb{R}}$로 적는다. $L=\pm\infty$로의 수렴은 위에서 정의한 의미이다.

::: 정리 4
임의의 실수열 $(a_n)$에 대하여 $\limsup a_n = \max E$이고 $\liminf a_n = \min E$이다. 곧 $E$는 최댓값과 최솟값을 가지며 각각 상극한, 하극한과 같다.
:::

::: 증명
상극한만 증명한다. $s = \limsup a_n$으로 두고, $s\in E$인 것과 모든 $L\in E$에 대하여 $L\le s$인 것을 보이면 된다.

*$s\in E$.* 부분수열 $n_1<n_2<\cdots$을 다음과 같이 세 경우로 나누어 만든다.

$s=+\infty$이면 모든 $n$에 대하여 $u_n=+\infty$이므로, 임의의 $n$ 이후에 $M$보다 큰 항이 존재한다. $n_{j-1}$이 정해졌을 때 $n_j > n_{j-1}$이고 $a_{n_j} > j$인 $n_j$를 고른다. 그럼 $a_{n_j}\to+\infty$이다.

$s\in\mathbb{R}$이면 각 $j$에 대하여 $s+1/j$는 $s=\inf_n u_n$보다 크므로 $u_{N_j} < s+1/j$인 $N_j$가 있다. 또 모든 $n$에 대하여 $u_n\ge s$이므로 $\sup_{k\ge n}a_k > s - 1/j$이고, 따라서 $a_k > s-1/j$인 $k\ge n$이 있다. 이제 $n_j > \max(n_{j-1}, N_j)$이면서 $a_{n_j} > s-1/j$인 $n_j$를 고르면, $n_j \ge N_j$이므로 $a_{n_j}\le u_{N_j} < s+1/j$이다. 곧 $\lvert a_{n_j}-s\rvert < 1/j$이고 $a_{n_j}\to s$이다. $\varepsilon$ 대신 $1/j$를 쓴 것은 $j\to\infty$에서 오차가 $0$으로 가는 수열이 필요하기 때문이고, 위쪽 경계 $s+1/j$는 $N_j$를 통해, 아래쪽 경계 $s-1/j$는 상한의 정의를 통해 각각 얻는다.

$s=-\infty$이면 $u_n\to-\infty$이고 $a_n\le u_n$이므로 $a_n\to-\infty$이다. 곧 $(a_n)$ 자신이 $-\infty$로 수렴하는 부분수열이다.

*$L\le s$.* $L\in E$이고 $a_{n_j}\to L$이라 하자. 고정된 $n$에 대하여, $j$가 충분히 크면 $n_j\ge n$이므로 $a_{n_j}\le u_n$이다. 이 부등식에서 $j\to\infty$로 보내면 $L\le u_n$이다. ($L=+\infty$이면 $u_n=+\infty$여야 하므로 마찬가지로 성립한다.) $n$이 임의이므로 $L\le\inf_n u_n = s$이다.

하극한은 [명제 2](#prop2){: data-lid="b11vi" }의 (2)에 의하여 $(-a_n)$에 이 결과를 적용하면 된다. $L\in E(a)$일 필요충분조건이 $-L\in E(-a)$이기 때문이다.
:::

[정리 4](#thm4){: data-lid="1lkxu" }는 상극한과 하극한이 부분수열 극한값 중 가장 큰 것과 가장 작은 것이라는 뜻이며, [정의 1](#def1){: data-lid="hxcyl" }과는 다른 방식의 서술을 준다. 계산에서는 [정의 1](#def1){: data-lid="etq65" }이 편하고, 값의 의미를 읽을 때는 [정리 4](#thm4){: data-lid="j5xh4" }가 편하다. 실수열의 부분수열 극한값은 상극한과 하극한 사이의 구간 안에 있지만, 그 구간의 모든 점이 부분수열 극한값인 것은 아니다. [예시 3](#ex3){: data-lid="v1isg" }에서 $E=\{-1, 1\}$이다.

## 수렴과의 관계

수렴하는 수열은 모든 부분수열이 같은 극한으로 가므로 $E$가 한 점이다. [정리 4](#thm4){: data-lid="ohl27" }에 의하여 이는 상극한과 하극한이 같다는 것을 뜻해야 한다. 이를 부분수열 없이 [정의 1](#def1){: data-lid="k4t7t" }만으로 직접 증명한다.

::: 정리 5
실수열 $(a_n)$과 $L\in\overline{\mathbb{R}}$에 대하여 $a_n\to L$일 필요충분조건은 $\limsup a_n = \liminf a_n = L$인 것이다. 특히 $(a_n)$이 실수로 수렴할 필요충분조건은 상극한과 하극한이 같은 유한한 값을 갖는 것이다.
:::

::: 증명
$L\in\mathbb{R}$인 경우를 먼저 본다.

($\Rightarrow$) $\varepsilon>0$이 주어지면 어떤 $N$이 있어 $k\ge N$에서 $L-\varepsilon < a_k < L+\varepsilon$이다. 따라서 $L-\varepsilon\le l_N$이고 $u_N\le L+\varepsilon$이다. 그럼 $\liminf a_n \ge l_N\ge L-\varepsilon$이고 $\limsup a_n\le u_N \le L+\varepsilon$이다. [명제 2](#prop2){: data-lid="tqcti" }에 의하여 $L-\varepsilon\le\liminf a_n\le\limsup a_n\le L+\varepsilon$이고, $\varepsilon$이 임의이므로 두 값은 모두 $L$이다.

($\Leftarrow$) $\varepsilon>0$이 주어졌다고 하자. $\inf_n u_n = L < L+\varepsilon$이므로 $u_{N_1} < L+\varepsilon$인 $N_1$이 있고, $\sup_n l_n = L > L-\varepsilon$이므로 $l_{N_2} > L-\varepsilon$인 $N_2$가 있다. $N=\max(N_1,N_2)$라 하면, $u_n$은 감소하고 $l_n$은 증가하므로 $n\ge N$에서 $L-\varepsilon < l_n\le a_n\le u_n < L+\varepsilon$이다. 곧 $\lvert a_n-L\rvert<\varepsilon$이다. 여기서 $N_1$과 $N_2$를 따로 잡고 더 큰 쪽을 취하는 것은, 위쪽 경계와 아래쪽 경계가 서로 다른 $n$부터 성립하기 때문이다.

$L=+\infty$인 경우 ($\Rightarrow$) $a_n\to+\infty$이면 임의의 $M$에 대하여 $n\ge N$에서 $a_n>M$이므로 $l_N\ge M$이고, 따라서 $\liminf a_n\ge M$이다. $M$이 임의이므로 $\liminf a_n=+\infty$이고, [명제 2](#prop2){: data-lid="ojj8f" }의 (1)에 의하여 $\limsup a_n=+\infty$이다. ($\Leftarrow$) $\liminf a_n=+\infty$이면 임의의 $M$에 대하여 $l_N>M$인 $N$이 있고, $n\ge N$에서 $a_n\ge l_n \ge l_N>M$이다. $L=-\infty$인 경우는 $(-a_n)$에 적용하면 된다.
:::

따라서 $(a_n)$이 수렴하지 않는다는 것을 보이는 방법으로, 상극한과 하극한이 다르다는 것을 계산하는 길이 있다. [예시 3](#ex3){: data-lid="vjp1e" }의 수열은 $\limsup=1\neq-1=\liminf$이므로 발산한다. 한편 상극한과 하극한이 둘 다 $+\infty$이거나 둘 다 $-\infty$인 경우에도 [정리 5](#thm5){: data-lid="z7apb" }에 의하여 수열은 각각 $+\infty$, $-\infty$로 발산한다.

## 합에 대한 부등식

극한은 합과 교환되지만 상극한은 그렇지 않다. 한 수열이 가장 큰 쪽으로 진동하는 때에 다른 수열이 가장 작은 쪽으로 진동할 수 있기 때문이다. 다음은 성립하는 방향이다. $\limsup a_n+\limsup b_n$이 $+\infty+(-\infty)$ 꼴이면 정의되지 않으므로, 정의되는 경우에만 쓴다.

::: 명제 6
실수열 $(a_n)$, $(b_n)$에 대하여 $A=\limsup a_n$, $B=\limsup b_n$이라 하고 $A+B$가 $\overline{\mathbb{R}}$에서 정의된다고 하자. 그럼 $$\limsup(a_n+b_n)\le A+B$$ 이다. 마찬가지로 $\liminf a_n+\liminf b_n$이 정의되면 $\liminf(a_n+b_n)\ge\liminf a_n+\liminf b_n$이다.
:::

::: 증명
$A+B=+\infty$이면 증명할 것이 없다.

$A, B$가 모두 실수라 하자. $\varepsilon>0$에 대하여 $u_{N_1}(a)<A+\varepsilon$, $u_{N_2}(b)<B+\varepsilon$인 $N_1, N_2$가 있고, $N=\max(N_1,N_2)$로 두면 $u_n$이 감소하므로 $k\ge N$에서 $a_k<A+\varepsilon$, $b_k<B+\varepsilon$이다. 그럼 $k\ge N$에서 $a_k+b_k<A+B+2\varepsilon$이고, $\limsup(a_n+b_n)\le u_N(a+b)\le A+B+2\varepsilon$이다. $\varepsilon$이 임의이므로 결론을 얻는다.

$A+B=-\infty$이면 $A=-\infty$ 또는 $B=-\infty$이고, 정의되는 합이므로 다른 쪽은 $+\infty$가 아니다. 일반성을 잃지 않고 $A=-\infty$, $B<+\infty$라 하자. 그럼 $a_n\le u_n(a)\to-\infty$이고 $\inf_n u_n(b)=B<+\infty$이므로 유한한 $u_{N}(b)$가 있다. $n\ge N$에서 $a_n+b_n\le a_n+u_N(b)$이고 우변은 $-\infty$로 가므로, $a_n+b_n\to-\infty$이다. [정리 5](#thm5){: data-lid="ly0u5" }에 의하여 $\limsup(a_n+b_n)=-\infty$이다.

하극한의 부등식은 [명제 2](#prop2){: data-lid="cagon" }의 (2)에 의하여 $(-a_n)$, $(-b_n)$에 위를 적용하면 얻는다.
:::

등호가 성립하지 않을 수 있다.

::: 예시 7
$a_n=(-1)^n$, $b_n=(-1)^{n+1}$이라 하자. $\limsup a_n=\limsup b_n=1$이므로 $\limsup a_n+\limsup b_n=2$이다. 그러나 $a_n+b_n=0$이 모든 $n$에 대해 성립하므로 $\limsup(a_n+b_n)=0<2$이다. 하극한 쪽에서도 $\liminf a_n+\liminf b_n=-2<0=\liminf(a_n+b_n)$이다. 부등식이 엄격한 이유는 $a_n$이 최대에 가까운 시점에 $b_n$이 최소에 가깝기 때문이다. [정리 4](#thm4){: data-lid="0cadt" }의 표현으로는 $\limsup a_n$과 $\limsup b_n$을 실현하는 부분수열이 서로 다른 번호의 항에 놓여 있다.
:::

두 수열 중 하나가 수렴하면 등호가 회복된다.

::: 명제 8
$(b_n)$이 실수 $B$로 수렴하면 임의의 실수열 $(a_n)$에 대하여 $$\limsup(a_n+b_n)=\limsup a_n+B,\quad\liminf(a_n+b_n)=\liminf a_n+B$$ 이다.
:::

::: 증명
[정리 5](#thm5){: data-lid="js4sk" }에 의하여 $\limsup b_n=\liminf b_n=B$이므로, [명제 2](#prop2){: data-lid="9p1bo" }의 (2)에 의하여 $\limsup(-b_n)=-B$이다. $B$가 실수이므로 아래에 나오는 합은 모두 정의된다. [명제 6](#prop6){: data-lid="8vf7s" }에 의하여 $\limsup(a_n+b_n)\le\limsup a_n+B$이다. 또 $a_n=(a_n+b_n)+(-b_n)$에 [명제 6](#prop6){: data-lid="k1qkv" }을 적용하면 $\limsup a_n\le\limsup(a_n+b_n)-B$이므로 $\limsup a_n+B\le\limsup(a_n+b_n)$이다. 두 부등식을 합치면 등호이다. 하극한은 $(-a_n)$, $(-b_n)$에 적용하면 된다.
:::

[명제 8](#prop8){: data-lid="q953z" }에서 $\limsup a_n$은 $\pm\infty$여도 상관없다. 수렴하는 수열을 더하는 것은 상극한과 하극한을 모두 $B$만큼 평행이동시킬 뿐이다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
