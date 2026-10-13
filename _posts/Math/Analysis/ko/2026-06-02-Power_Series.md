---
title: "멱급수와 해석함수"
description: "멱급수의 수렴반경을 Cauchy–Hadamard 공식으로 정하고, 수렴구간 안의 컴팩트 부분집합에서 균등수렴함을 보여 항별 미분과 항별 적분을 정당화한다. 수렴구간의 경계에서 일어나는 일과 Abel 정리, 해석함수의 중심 이동, 해석적이지 않은 C^∞ 함수의 예를 다룬다."
excerpt: "수렴반경, 컴팩트 균등수렴, 항별 미분·적분, Abel 정리, 해석함수와 중심 이동"

categories: [Math / Analysis]
permalink: /ko/math/analysis/power_series
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 24

published: false

---

수열 $(c_n)$과 점 $a$가 주어졌을 때 $\sum_{n=0}^\infty c_n(x-a)^n$ 꼴의 급수를 *멱급수<sub>power series</sub>*라 한다. 이 글에서 계수 $c_n$과 변수 $x$는 실수이다. 멱급수는 $x$마다 하나의 수열급수이므로 먼저 어떤 $x$에서 수렴하는지가 문제가 되는데, 수렴하는 점들의 집합이 $a$를 중심으로 하는 대칭 구간 모양이라는 것이 이 글의 출발점이다. 이 구간 안에서 멱급수는 균등수렴에 가까운 성질을 가져 polynomial처럼 미분하고 적분할 수 있으며, 그 합은 항상 무한 번 미분가능하다. 이 성질을 가진 함수를 해석함수라 부르고, 무한 번 미분가능한 함수가 모두 해석적인 것은 아님을 마지막에 확인한다. 상극한은 [§상극한과 하극한, ⁋정의 1](/ko/math/analysis/limsup_and_liminf#def1){: data-lid="6pijs" }에서, 급수의 비교판정은 [§무한급수와 수렴판정법, ⁋정리 6](/ko/math/analysis/series#thm6){: data-lid="lon7h" }에서 가져온다.

## 수렴반경

멱급수가 $x=a$에서 수렴하는 것은 자명하다. 다른 점에서의 수렴 여부는 계수의 증가 속도가 정한다. 가령 $\sum x^n/n!$은 어느 $x$에서든 [§무한급수와 수렴판정법, ⁋정리 14](/ko/math/analysis/series#thm14){: data-lid="7nroc" }의 비 $\lvert x\rvert/(n+1)$이 $0$으로 가므로 모든 $x$에서 수렴하고, $\sum n!x^n$은 $x\neq 0$이면 비 $(n+1)\lvert x\rvert$가 발산하므로 $x=0$에서만 수렴한다. 그 사이의 경우는 $n$번째 항의 크기 $\lvert c_n(x-a)^n\rvert^{1/n}=\lvert c_n\rvert^{1/n}\lvert x-a\rvert$에 [§무한급수와 수렴판정법, ⁋정리 13](/ko/math/analysis/series#thm13){: data-lid="mdel9" }을 적용하면 정리된다. 극한이 없을 수 있으므로 상극한을 쓴다.

::: 정리 1 (Cauchy–Hadamard)
$L=\limsup_{n\to\infty}\lvert c_n\rvert^{1/n}\in[0,\infty]$라 두고

$$R=\frac{1}{L}\qquad(1/0=\infty,\ 1/\infty=0)$$

으로 정한다. 멱급수 $\sum c_n(x-a)^n$은 $\lvert x-a\rvert<R$이면 절대수렴하고 $\lvert x-a\rvert>R$이면 발산한다. $R$을 이 멱급수의 *수렴반경<sub>radius of convergence</sub>*이라 한다.
:::

::: 증명
$\lvert x-a\rvert<R$인 $x$를 잡는다. $x=a$이면 자명하므로 $x\neq a$로 가정한다. 이때 $L\lvert x-a\rvert<1$이므로 $L\lvert x-a\rvert<\theta<1$인 $\theta$를 하나 고를 수 있다. $L<\theta/\lvert x-a\rvert$이므로 [§상극한과 하극한, ⁋정의 1](/ko/math/analysis/limsup_and_liminf#def1){: data-lid="ck7h9" }에 의하여, 충분히 큰 $n\geq N$에 대하여 $\lvert c_n\rvert^{1/n}<\theta/\lvert x-a\rvert$, 곧 $\lvert c_n(x-a)^n\rvert<\theta^n$이다. $0<\theta<1$이므로 등비급수와의 [§무한급수와 수렴판정법, ⁋정리 6](/ko/math/analysis/series#thm6){: data-lid="p0396" }에 의하여 $\sum\lvert c_n(x-a)^n\rvert$이 수렴한다. $\theta$를 $L\lvert x-a\rvert$와 $1$ 사이에서 고르는 이유는 두 가지이다. $\theta<1$이어야 등비급수가 수렴하고, $\theta>L\lvert x-a\rvert$여야 상극한의 정의로부터 "$N$ 이후 모든 $n$"에 대한 부등식을 얻는다.

$\lvert x-a\rvert>R$이면 $L>0$이고 $L\lvert x-a\rvert>1$이다($L=\infty$ 포함). 상극한의 [§상극한과 하극한, ⁋정의 1](/ko/math/analysis/limsup_and_liminf#def1){: data-lid="gjjur" }에 의하여 $\lvert c_n\rvert^{1/n}>1/\lvert x-a\rvert$인 $n$이 무한히 많고, 이런 $n$에서 $\lvert c_n(x-a)^n\rvert>1$이다. 일반항이 $0$으로 수렴하지 않으므로 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2){: data-lid="ahaue" }에 의하여 급수는 발산한다.
:::

따라서 수렴하는 점들의 집합은 $(a-R,a+R)$를 포함하고 $[a-R,a+R]$에 포함된다. 이 열린 구간을 *수렴구간*이라 하고, 경계 $x=a\pm R$에서는 [정리 1](#thm1){: data-lid="p6699" }이 아무것도 말해주지 않는다. 이는 아래 경계에서의 행동 절에서 다룬다.

계수가 규칙적으로 진동하여 비의 극한이 없는 경우에는 상극한이 필요하다. $c_n$이 짝수 $n$에서 $2^n$, 홀수 $n$에서 $3^n$이면 비 $\lvert c_{n+1}/c_n\rvert$은 $2^{n+1}/3^n$과 $3^{n+1}/2^n$ 사이를 오가므로 비판정은 아무 답도 주지 못한다. 그러나 $\lvert c_n\rvert^{1/n}$은 $2$와 $3$을 번갈아 취하므로 $L=3$이고 $R=1/3$이다.

## 수렴구간 안의 균등수렴

수렴구간 안에서의 수렴은 점마다 일어나는 것이 아니라 구간의 안쪽 닫힌 부분에서 균등하게 일어난다. 균등수렴의 정의와 연속성·적분·미분에 대한 성질은 각각 [§균등수렴, ⁋정의 1](/ko/math/analysis/uniform_convergence#def1){: data-lid="p5em0" }, [§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6){: data-lid="i26yr" }, [§균등수렴, ⁋정리 7](/ko/math/analysis/uniform_convergence#thm7){: data-lid="dg1l6" }, [§균등수렴, ⁋정리 9](/ko/math/analysis/uniform_convergence#thm9){: data-lid="c3ybf" }에서 다루었다.

::: 정리 2
멱급수 $\sum c_n(x-a)^n$의 수렴반경이 $R>0$이라 하고 $f$를 그 합이라 하자. $0\leq r<R$이면 급수는 $[a-r,a+r]$에서 $f$로 균등수렴한다. 따라서 $(a-R,a+R)$의 임의의 compact subset에서도 균등수렴하고, $f$는 $(a-R,a+R)$에서 연속이다.
:::

::: 증명
$r<R$이므로 [정리 1](#thm1){: data-lid="c3ld0" }에 의하여 $\sum\lvert c_n\rvert r^n$이 수렴한다. $s_N(x)=\sum_{n=0}^N c_n(x-a)^n$이라 하면 $\lvert x-a\rvert\leq r$인 모든 $x$에 대하여

$$\lvert f(x)-s_N(x)\rvert=\left\lvert\sum_{n>N}c_n(x-a)^n\right\rvert\leq\sum_{n>N}\lvert c_n\rvert r^n=:\varepsilon_N$$

이고, $\varepsilon_N$은 $x$에 의존하지 않으며 수렴하는 급수의 꼬리이므로 $0$으로 간다. 이것이 균등수렴이다.

$K\subseteq(a-R,a+R)$가 컴팩트이면 [§연속함수의 성질, ⁋따름정리 2](/ko/math/analysis/continuous_functions#cor2){: data-lid="0275w" }에 의하여 $x\mapsto\lvert x-a\rvert$는 $K$에서 최댓값 $r$을 가지고, 최댓값이 $K$의 한 점에서 취해지므로 $r<R$이다. 따라서 $K\subseteq[a-r,a+r]$이고 위의 결과가 적용된다. 연속함수 $s_N$의 균등극한은 [§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6){: data-lid="s1uu4" }에 의하여 연속이므로, 각 $x\in(a-R,a+R)$에 대하여 $\lvert x-a\rvert<r<R$인 $r$을 잡으면 $f$는 $[a-r,a+r]$ 위에서 연속이고 $x$는 그 interior point이다.
:::

[정리 2](#thm2){: data-lid="s1hxi" }의 "compact subset"은 빼면 안 되는 조건이다. 수렴구간 전체에서는 균등수렴하지 않을 수 있다.

::: 예시 3 (수렴구간 전체에서 균등수렴하지 않는 멱급수)
$\sum x^n$의 수렴반경은 $1$이고 합은 $1/(1-x)$이다. 부분합은 $s_N(x)=(1-x^{N+1})/(1-x)$이므로

$$\frac{1}{1-x}-s_N(x)=\frac{x^{N+1}}{1-x}$$

이다. 고정된 $N$에 대하여 $x\to1^-$이면 분자는 $1$로, 분모는 $0$으로 가므로 이 차이는 $(-1,1)$에서 유계가 아니다. 따라서 $\sup_{\lvert x\rvert<1}\lvert f-s_N\rvert=\infty$이고 $(-1,1)$ 위의 균등수렴은 일어나지 않는다. 반면 $[-r,r]$ ($r<1$)에서는 $\varepsilon_N=r^{N+1}/(1-r)\to0$이다.
:::

## 항별 미분과 항별 적분

함수열에서는 균등수렴만으로 극한과 미분을 바꿀 수 없다. $\sin(nx)/n$은 $0$으로 균등수렴하지만 도함수 $\cos(nx)$는 $x=0$에서 $1$이어서 $0$으로 수렴하지 않는다. 필요한 것은 도함수열의 균등수렴이고, 멱급수에서는 이것이 수렴반경이 변하지 않는다는 사실에서 따라 나온다.

::: 정리 4
$\sum c_n(x-a)^n$의 수렴반경이 $R>0$이고 합이 $f$이면 다음이 성립한다.

1. 도함수 급수 $\sum_{n\geq1}nc_n(x-a)^{n-1}$과 적분 급수 $\sum_{n\geq0}c_n(x-a)^{n+1}/(n+1)$의 수렴반경도 $R$이다.
2. $\lvert x-a\rvert<R$에서 $f$는 미분가능하고 $f'(x)=\sum_{n\geq1}nc_n(x-a)^{n-1}$이다.
3. $\lvert x-a\rvert<R$에서 $\int_a^x f(t)\dd{t}=\sum_{n\geq0}c_n(x-a)^{n+1}/(n+1)$이다.
:::

::: 증명
(1) $x-a$를 곱하거나 나누는 것은 $x\neq a$에서의 수렴 여부를 바꾸지 않으므로, $\sum nc_n(x-a)^n$과 $\sum c_n(x-a)^n/(n+1)$의 수렴반경을 보면 된다. 앞의 것은 $\limsup(n\lvert c_n\rvert)^{1/n}=\limsup n^{1/n}\lvert c_n\rvert^{1/n}$을 정한다. $n^{1/n}\to1$이므로(어떤 $\delta_n\geq0$에 대하여 $n^{1/n}=1+\delta_n$이라 쓰면 $n=(1+\delta_n)^n\geq n(n-1)\delta_n^2/2$에서 $\delta_n^2\leq2/(n-1)$이다) 임의의 $\varepsilon>0$에 대하여 충분히 큰 $n$에서 $(1-\varepsilon)\lvert c_n\rvert^{1/n}\leq n^{1/n}\lvert c_n\rvert^{1/n}\leq(1+\varepsilon)\lvert c_n\rvert^{1/n}$이고, 상극한을 취하면 $L$이 $(1\pm\varepsilon)$배 사이에 놓이므로 $\varepsilon$이 임의라서 $\limsup(n\lvert c_n\rvert)^{1/n}=L$이다. 적분 급수도 $(n+1)^{1/n}=\bigl((n+1)^{1/(n+1)}\bigr)^{(n+1)/n}\to1$이므로 같은 논증으로 $L$이 유지된다.

(2) $\lvert x-a\rvert<R$인 $x$를 잡고 $\lvert x-a\rvert<r<R$인 $r$을 고른다. 구간 $I=(a-r,a+r)$에서 부분합 $s_N$은 polynomial이고, $s_N'$은 도함수 급수의 부분합이다. (1)에 의하여 도함수 급수의 수렴반경이 $R>r$이므로 [정리 2](#thm2){: data-lid="nmox4" }를 도함수 급수에 적용하면 $s_N'$은 $I$에서 균등수렴한다. 한편 $s_N(a)=c_0$은 수렴한다. [§균등수렴, ⁋정리 9](/ko/math/analysis/uniform_convergence#thm9){: data-lid="ij2z6" }에 의하여, 미분가능한 함수열이 한 점에서 수렴하고 도함수열이 구간에서 균등수렴하면 함수열 자신도 균등수렴하며 극한함수는 미분가능하고 그 도함수는 도함수열의 극한이다. 따라서 $I$ 위에서 $f'=\lim s_N'$, 곧 도함수 급수의 합이다.

(3) 같은 $x$에 대하여 $a$와 $x$를 잇는 닫힌 구간 $J$ 위에서 $s_N\to f$가 균등하므로 [§균등수렴, ⁋정리 6](/ko/math/analysis/uniform_convergence#thm6){: data-lid="zz3v9" }에 의하여 $f$는 $J$에서 연속이고 $\bigl\lvert\int_a^x(f-s_N)\dd{t}\bigr\rvert\leq\varepsilon_N\lvert x-a\rvert\to0$이다. 이때 $\int_a^x s_N\dd{t}=\sum_{n\leq N}c_n(x-a)^{n+1}/(n+1)$이므로 극한을 취하면 된다.
:::

[정리 4](#thm4){: data-lid="9sbpd" }를 반복해서 적용하면 $k$계 도함수까지 얻는다.

::: 따름정리 5
$f(x)=\sum c_n(x-a)^n$의 수렴반경이 $R>0$이면 $f$는 $(a-R,a+R)$에서 $C^\infty$이고

$$f^{(k)}(x)=\sum_{n\geq k}n(n-1)\cdots(n-k+1)c_n(x-a)^{n-k},\qquad c_k=\frac{f^{(k)}(a)}{k!}$$

이다. 특히 $a$의 어떤 근방에서 두 멱급수 $\sum c_n(x-a)^n$과 $\sum d_n(x-a)^n$의 합이 같으면 모든 $n$에 대하여 $c_n=d_n$이다.
:::

::: 증명
도함수 급수의 수렴반경이 다시 $R$이므로 [정리 4](#thm4){: data-lid="jh9m6" }를 $k$번 적용하면 $f^{(k)}$의 식을 얻고, $x=a$를 대입하면 $n=k$인 항만 남아 $f^{(k)}(a)=k!c_k$이다. 두 멱급수의 합이 $a$의 근방 $(a-\delta,a+\delta)$에서 같으면 두 급수 모두 그곳에서 수렴하므로 수렴반경이 $\delta$ 이상이고, 도함수 $f^{(k)}(a)$는 $f$의 근방에서의 값만으로 정해지므로 $c_k=d_k$이다.
:::

[따름정리 5](#cor5){: data-lid="3xjd6" }에서 멱급수의 합 $f$를 정의하는 멱급수는 $f$의 Taylor 급수 $\sum f^{(n)}(a)(x-a)^n/n!$과 일치한다. 따라서 점화식이나 미정계수법 등 어떤 방법으로 $f$를 멱급수로 적어내든, 같은 중심에서의 전개는 하나뿐이다.

## 경계에서의 행동

$\lvert x-a\rvert=R$인 두 점에서는 수렴할 수도 발산할 수도 있고, 두 점에서의 행동이 서로 다를 수도 있다. 세 급수 $\sum x^n$, $\sum x^n/n$, $\sum x^n/n^2$는 모두 수렴반경이 $1$이다($n^{1/n}\to1$이므로 [정리 4](#thm4){: data-lid="2stv2" }의 (1)과 같은 논증이 적용된다). $\sum x^n$은 $x=\pm1$에서 일반항이 $0$으로 가지 않으므로 [§무한급수와 수렴판정법, ⁋명제 2](/ko/math/analysis/series#prop2){: data-lid="hwy6t" }에 의하여 양 끝에서 발산한다. $\sum x^n/n$은 $x=1$에서 [§무한급수와 수렴판정법, ⁋예시 4](/ko/math/analysis/series#ex4){: data-lid="ygs9p" }에 의하여 발산하고, $x=-1$에서는 [§무한급수와 수렴판정법, ⁋정리 16](/ko/math/analysis/series#thm16){: data-lid="vf4mj" }에 의하여 수렴하지만 절대수렴하지 않으므로 조건수렴한다. $\sum x^n/n^2$은 $x=\pm1$에서 [§무한급수와 수렴판정법, ⁋명제 9](/ko/math/analysis/series#prop9){: data-lid="1np6j" }에 의하여 수렴하는 $\sum1/n^2$과 비교되어 양 끝에서 절대수렴한다. 부호를 바꾼 $\sum(-1)^nx^n/n$은 $x=1$에서만 수렴한다.

두 끝점 사이에는 절대수렴에 관한 제약이 하나 있다. $\sum\lvert c_n\rvert R^n$은 $x=a+R$과 $x=a-R$에서의 절대값 급수로 같은 급수이므로, 한 끝에서 절대수렴하면 다른 끝에서도 절대수렴한다. 따라서 위에서 $x=-1$만 조건수렴인 경우처럼 한 끝에서만 수렴하는 경우에는 그 수렴이 조건수렴이다.

또 미분은 경계에서의 행동을 바꾼다. $\sum x^n/n^2$은 $x=1$에서 수렴하지만 항별로 미분한 $\sum x^{n-1}/n$은 $x=1$에서 발산한다. [정리 4](#thm4){: data-lid="1ic6c" }의 (2)는 수렴구간의 안쪽에서만 성립한다.

## Abel 정리

경계에서 급수가 수렴하면, 그 값이 $f$의 안쪽 극한과 일치하는지가 문제가 된다. 이는 항상 성립한다.

::: 정리 6 (Abel)
$\sum c_n(x-a)^n$의 수렴반경이 $R$이고 $0<R<\infty$이며, 급수가 $x=a+R$에서 수렴한다고 하자. $f$를 수렴구간에서의 합이라 하면

$$\lim_{x\to(a+R)^-}f(x)=\sum_{n=0}^\infty c_nR^n$$

이다. $x=a-R$에서 수렴하는 경우에도 $x\to(a-R)^+$에서 같은 결론이 성립한다.
:::

::: 증명
$c_n$을 $c_nR^n$으로, $x-a$를 $Rt$로 바꾸면 $a=0$, $R=1$인 경우로 환원되고 구하는 극한은 $t\to1^-$이다. $a-R$ 쪽은 $t$를 $-t$로 바꾸어 같은 형태가 된다. 따라서 $\sum c_n$이 수렴한다고 하고 $0<x<1$에서 $f(x)=\sum c_nx^n$에 대하여 $x\to1^-$일 때 $f(x)\to s=\sum c_n$임을 보인다.

$s_n=c_0+\cdots+c_n$($s_{-1}=0$)이라 두면 $s_n\to s$이다. $c_n=s_n-s_{n-1}$을 대입하여 부분합을 정리하면

$$\sum_{n=0}^m c_nx^n=\sum_{n=0}^m s_nx^n-\sum_{n=0}^{m-1}s_nx^{n+1}=(1-x)\sum_{n=0}^{m-1}s_nx^n+s_mx^m$$

이다. $0<x<1$이면 $s_mx^m\to0$이므로 $m\to\infty$일 때

$$f(x)=(1-x)\sum_{n=0}^\infty s_nx^n$$

이다. 또 $(1-x)\sum_{n\geq0}x^n=1$이므로 $s=(1-x)\sum sx^n$이고, 따라서

$$f(x)-s=(1-x)\sum_{n=0}^\infty(s_n-s)x^n$$

이다. $\varepsilon>0$이 주어졌다고 하자. $s_n\to s$이므로 $n>N$이면 $\lvert s_n-s\rvert<\varepsilon/2$인 $N$이 있다. 이 $N$을 고정하고 $C=\sum_{n\leq N}\lvert s_n-s\rvert$라 두면, $0<x<1$에서

$$\lvert f(x)-s\rvert\leq(1-x)C+\frac{\varepsilon}{2}(1-x)\sum_{n>N}x^n\leq(1-x)C+\frac{\varepsilon}{2}$$

이다. $N$이 먼저 정해지고 나서 $C$가 정해지므로, $1-x<\varepsilon/(2(C+1))$로 $x$를 $1$에 가깝게 잡으면 $\lvert f(x)-s\rvert<\varepsilon$이다.
:::

Abel 정리는 합을 구하는 데 쓰인다. 수치급수의 합이 알려진 함수의 경계값으로 읽히는 경우이다.

::: 예시 7 (Σ(−1)^n/(n+1) = log 2)
$\lvert t\rvert<1$에서 $1/(1+t)=\sum(-t)^n$이고 수렴반경은 $1$이다. $\lvert x\rvert<1$에서 이를 $0$부터 $x$까지 항별로 적분하면 [정리 4](#thm4){: data-lid="6l48j" }의 (3)에 의하여

$$\log(1+x)=\sum_{n=0}^\infty\frac{(-1)^n}{n+1}x^{n+1}$$

이다. $x=1$에서 우변은 항의 절댓값 $1/(n+1)$이 $0$으로 단조감소하므로 [§무한급수와 수렴판정법, ⁋정리 16](/ko/math/analysis/series#thm16){: data-lid="5eys0" }에 의하여 수렴한다. [정리 6](#thm6){: data-lid="gy6vc" }에 의하여 이 값은 $x\to1^-$에서의 극한 $\lim\log(1+x)=\log2$와 같다. 곧

$$\sum_{n=0}^\infty\frac{(-1)^n}{n+1}=1-\frac12+\frac13-\cdots=\log2$$

이다. 같은 방법으로 $1/(1+t^2)=\sum(-1)^nt^{2n}$을 적분하여 $\arctan x=\sum(-1)^nx^{2n+1}/(2n+1)$을 얻고, $x=1$에 [정리 6](#thm6){: data-lid="h2dpp" }을 적용하면 $1-1/3+1/5-\cdots=\pi/4$이다.
:::

[정리 6](#thm6){: data-lid="ohz5n" }의 역은 성립하지 않는다. $x\to1^-$일 때 $f(x)$가 극한을 가져도 경계에서 급수가 수렴한다는 보장은 없다.

::: 예시 8 (Abel 정리의 역이 실패하는 경우)
$\sum(-1)^nx^n$은 $\lvert x\rvert<1$에서 $f(x)=1/(1+x)$이므로 $x\to1^-$에서 $f(x)\to1/2$로 극한이 존재한다. 그러나 $x=1$에서의 급수 $1-1+1-1+\cdots$는 부분합이 $1,0,1,0,\ldots$이어서 발산한다. 극한값 $1/2$는 어떤 수렴하는 급수의 합도 아니다.
:::

역이 성립하려면 계수에 조건이 더 필요하다. $nc_n\to0$이면 $f(x)$의 극한이 존재할 때 $\sum c_n$이 수렴한다는 것이 Tauber의 정리이다. [예시 8](#ex8){: data-lid="0aoog" }의 계수 $(-1)^n$은 이 조건을 만족하지 않는다.

## 해석함수와 중심 이동

[따름정리 5](#cor5){: data-lid="ekh1i" }에 의하여 멱급수의 합은 $C^\infty$이다. 이 성질을 가진 함수의 부류를 이름 붙인다.

::: 정의 9
$U\subseteq\mathbb{R}$이 열린집합이고 $f:U\to\mathbb{R}$이라 하자. $a\in U$의 어떤 근방 $(a-\delta,a+\delta)$에서 $f(x)=\sum c_n(x-a)^n$인 멱급수가 있으면 $f$가 $a$에서 *해석적<sub>analytic</sub>*이라 한다. $U$의 모든 점에서 해석적이면 $U$ 위의 *해석함수*라 한다.
:::

[따름정리 5](#cor5){: data-lid="uzzlv" }에 의하여 $a$에서 해석적인 함수는 $a$의 근방에서 $C^\infty$이고, 그 근방에서 자신의 Taylor 급수 $\sum f^{(n)}(a)(x-a)^n/n!$과 같다. 정의는 점 $a$마다 하나의 중심에서의 멱급수를 요구하므로, 수렴구간 안의 다른 점에서도 해석적인지는 따로 확인해야 한다. 다음 정리는 그렇다고 답한다.

::: 정리 10 (중심 이동)
$f(x)=\sum c_n(x-a)^n$의 수렴반경이 $R>0$이고 $b\in(a-R,a+R)$라 하자. $\lvert x-b\rvert<R-\lvert b-a\rvert$이면

$$f(x)=\sum_{k=0}^\infty d_k(x-b)^k,\qquad d_k=\sum_{n\geq k}\binom{n}{k}c_n(b-a)^{n-k}$$

이고 우변의 급수들은 모두 수렴한다. 특히 $f$는 수렴구간의 모든 점에서 해석적이다.
:::

::: 증명
$x-a=(x-b)+(b-a)$로 쓰고 이항정리를 적용하면 $c_n(x-a)^n=\sum_{k=0}^n\binom nk c_n(b-a)^{n-k}(x-b)^k$이다. 따라서 $f(x)$는 지표 $(n,k)$ ($0\leq k\leq n$)에 대한 이중급수를 $n$ 먼저 고정해 $k$로 더한 뒤 $n$으로 더한 값이다. 이 이중급수의 절댓값의 합은

$$\sum_{n=0}^\infty\sum_{k=0}^n\binom nk\lvert c_n\rvert\lvert b-a\rvert^{n-k}\lvert x-b\rvert^k=\sum_{n=0}^\infty\lvert c_n\rvert\bigl(\lvert b-a\rvert+\lvert x-b\rvert\bigr)^n$$

이고, $\lvert b-a\rvert+\lvert x-b\rvert<R$이므로 [정리 1](#thm1){: data-lid="gsqo6" }에 의하여 유한하다. 따라서 이중급수는 절대수렴하여 더하는 순서를 바꿀 수 있다([§급수의 재배열과 곱](/ko/math/analysis/rearrangements_and_products){: data-lid="ng2ih" }). $k$를 먼저 고정해 $n$으로 더하면 각 $k$에 대하여 $d_k$가 수렴하고 $f(x)=\sum_kd_k(x-b)^k$를 얻는다.
:::

[정리 10](#thm10){: data-lid="ppdcu" }의 새 급수는 수렴반경이 $R-\lvert b-a\rvert$ 이상이라는 것만 보장되고, 더 클 수도 있다. 반대로 함수가 $\mathbb{R}$ 전체에서 $C^\infty$이어도 수렴반경이 유한할 수 있다. $1/(1+x^2)=\sum(-1)^nx^{2n}$은 $\lvert x\rvert\geq1$에서 일반항이 $0$으로 가지 않으므로 수렴반경이 $1$이다. 수렴반경은 실수축 위에서 $f$의 매끄러움만으로는 정해지지 않는다.

해석함수는 한 점에서의 정보로 구간 전체가 결정된다는 강한 경직성을 가진다. 연결성은 [§연결성과 중간값 정리, ⁋정의 1](/ko/math/analysis/connectedness#def1){: data-lid="ejpgo" }에서 다루었다.

::: 명제 11 (유일성 정리)
$I$가 열린 구간이고 $f$가 $I$ 위의 해석함수이며, 어떤 $x_0\in I$에서 모든 $n\geq0$에 대하여 $f^{(n)}(x_0)=0$이면 $f$는 $I$에서 항등적으로 $0$이다.
:::

::: 증명
$Z=\{x\in I:\ \text{모든 }n\text{에 대하여 }f^{(n)}(x)=0\}$이라 하자. 각 $f^{(n)}$이 연속이므로 $Z$는 $I$에서 닫혀 있다. $x\in Z$이면 $f$가 $x$에서 해석적이므로 $x$의 근방에서 $f$는 Taylor 급수 $\sum f^{(n)}(x)(t-x)^n/n!=0$과 같고, 그 근방에서 $f$가 항등적으로 $0$이므로 모든 도함수도 $0$이다. 곧 그 근방이 $Z$에 들어가므로 $Z$는 열려 있다. 구간 $I$는 [§연결성과 중간값 정리, ⁋정리 2](/ko/math/analysis/connectedness#thm2){: data-lid="3qwyb" }에 의하여 연결이고 $x_0\in Z$이므로 $Z=I$이다.
:::

두 해석함수가 어떤 점의 근방에서 일치하면 차 $f-g$에 [명제 11](#prop11){: data-lid="p0gn2" }을 적용하여 구간 전체에서 일치한다.

## 해석적이지 않은 C^∞ 함수

$C^\infty$이면서 해석적이지 않은 함수가 있다. [명제 11](#prop11){: data-lid="yh72p" }은 그런 함수가 한 점에서 모든 도함수가 $0$이면서도 영함수가 아닐 수 있음을 시사한다.

::: 예시 12 ($e^{-1/x^2}$)
$f(x)=e^{-1/x^2}$ ($x\neq0$), $f(0)=0$으로 정한다. $f$는 $C^\infty$이고 $f^{(n)}(0)=0$이 모든 $n$에서 성립함을 보인다.

먼저 $x\neq0$에서 $f^{(n)}(x)=p_n(1/x)e^{-1/x^2}$인 polynomial $p_n$이 존재한다. $n=0$에서는 $p_0=1$이고, $f^{(n)}=p_n(1/x)e^{-1/x^2}$이면 $t=1/x$에 대하여

$$\frac{\mathrm d}{\dd{x}}\Bigl(p_n(1/x)e^{-1/x^2}\Bigr)=\Bigl(-\frac{1}{x^2}p_n'(1/x)+\frac{2}{x^3}p_n(1/x)\Bigr)e^{-1/x^2}=p_{n+1}(1/x)e^{-1/x^2}$$

이고 $p_{n+1}(t)=-t^2p_n'(t)+2t^3p_n(t)$는 polynomial이다. 다음으로 임의의 정수 $k\geq0$에 대하여 $t^ke^{-t^2}\to0$ ($t\to\pm\infty$)이다. $2m>k$인 $m$을 잡으면 $e^{t^2}\geq t^{2m}/m!$이므로 $\lvert t\rvert\geq1$에서 $\lvert t\rvert^ke^{-t^2}\leq m!\lvert t\rvert^{k-2m}\to0$이다. 이제 $f^{(n)}(0)=0$을 $n$에 대한 귀납법으로 보인다. $n=0$은 정의이고, $f^{(n)}(0)=0$이면

$$f^{(n+1)}(0)=\lim_{x\to0}\frac{f^{(n)}(x)-f^{(n)}(0)}{x}=\lim_{x\to0}\frac1xp_n(1/x)e^{-1/x^2}=\lim_{t\to\pm\infty}tp_n(t)e^{-t^2}=0$$

이다. 마지막 극한은 $tp_n(t)$가 polynomial이므로 앞의 $t^ke^{-t^2}\to0$을 항마다 적용한 것이다. 같은 논증으로 $x\neq0$에서의 도함수 $f^{(n)}(x)=p_n(1/x)e^{-1/x^2}$도 $x\to0$에서 $0$으로 가므로 $f^{(n)}$은 $0$에서도 연속이고, $f$는 $C^\infty$이다.

따라서 $0$에서의 Taylor 급수는 항등적으로 $0$이다. 그런데 $x\neq0$이면 $f(x)>0$이므로 $f$는 $0$의 어떤 근방에서도 이 급수와 같지 않고, $f$는 $0$에서 해석적이지 않다. 이 급수는 모든 $x$에서 수렴하지만 $x=0$ 이외에서 $f$로 수렴하지 않는다. 같은 계산으로 $x>0$에서 $e^{-1/x^2}$, $x\leq0$에서 $0$인 함수도 $C^\infty$이다. 이 함수는 $(-\infty,0]$에서 $0$이면서 영함수가 아니므로 [명제 11](#prop11){: data-lid="ml8gg" }이 말하는 경직성이 $C^\infty$ 함수에는 없음을 보여 준다.
:::

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
