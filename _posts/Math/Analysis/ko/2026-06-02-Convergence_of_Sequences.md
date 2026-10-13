---
title: "수열의 수렴"
description: "수열의 수렴을 ε-N 정의로 세우고, 한정사의 순서와 그 부정을 정리한다. 극한의 유일성, 유계성, 사칙연산, 순서 보존, 조임정리, 단조수렴정리를 증명하고, $(1+1/n)^n$의 수렴과 무한대로의 발산까지 다룬다."
excerpt: "ε-N 수렴, 극한의 성질, 조임정리, 단조수렴정리, (1+1/n)^n, 무한대로의 발산"

categories: [Math / Analysis]
permalink: /ko/math/analysis/convergence_of_sequences
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 2

published: false

---

[§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3)의 실수의 상한 성질과 [§실수의 완비성, ⁋정리 6](/ko/math/analysis/completeness_of_reals#thm6)의 Archimedean property를 얻었다. 이 글에서는 이를 바탕으로 수열이 어떤 값에 수렴한다는 말을 부등식만으로 정의하고, 수렴하는 수열이 가지는 기본 성질과 수렴을 판정하는 두 가지 도구인 조임정리와 단조수렴정리를 증명한다. 수열 $(a_n)_{n\ge 1}$은 자연수 $n$에 실수 $a_n$을 대응시키는 함수이며, 이하 $\mathbb{N}=\{1,2,3,\ldots\}$이다.

## 수렴의 정의

"$n$이 커질수록 $a_n$이 $L$에 한없이 가까워진다"는 말에서 한없이 가깝다는 것은 어떤 오차 범위를 주더라도 $n$이 충분히 크면 $a_n$이 그 범위 안에 들어온다는 뜻이다. 오차 범위를 $\varepsilon$으로, 충분히 크다는 것을 $n\ge N$으로 적으면 다음 정의를 얻는다.

::: 정의 1
수열 $(a_n)$이 실수 $L$로 *수렴*한다는 것은, 임의의 $\varepsilon > 0$에 대하여 자연수 $N$이 존재하여 모든 $n \ge N$에 대해 $\lvert a_n - L\rvert < \varepsilon$이 성립하는 것이다. 이때 $L$을 $(a_n)$의 *극한*이라 하고 $\lim_{n\to\infty} a_n = L$ 또는 $a_n \to L$로 적는다. 실수로 수렴하지 않는 수열은 *발산*한다고 한다.
:::

정의에서 $N$은 $\varepsilon$을 먼저 받은 뒤에 정해지므로 $\varepsilon$에 의존하며, $\varepsilon$이 작아질수록 $N$은 일반적으로 커진다. 수렴을 정의대로 증명하는 일은 주어진 $\varepsilon$에서 $N$을 구성하는 일이고, 이는 $\lvert a_n - L\rvert<\varepsilon$을 $n$에 대한 부등식으로 풀어 보면 대개 드러난다.

가령 $a_n = 1/n$은 $0$으로 수렴한다. $\varepsilon>0$이 주어지면 [§실수의 완비성, ⁋정리 6](/ko/math/analysis/completeness_of_reals#thm6)에 의하여 $N>1/\varepsilon$인 자연수 $N$이 있고, $n\ge N$에서 $\lvert 1/n - 0\rvert = 1/n \le 1/N < \varepsilon$이다. 조금 더 일반적으로 $a_n = (3n+1)/(n+2)$는 $3$으로 수렴한다. $\lvert a_n - 3\rvert = 5/(n+2) < 5/n$이므로 $N > 5/\varepsilon$으로 고르면 $n\ge N$에서 $\lvert a_n - 3\rvert < 5/n \le 5/N<\varepsilon$이다. 여기서 $N$을 $5/\varepsilon$ 이상으로 잡은 것은 $\lvert a_n-3\rvert$를 $n$만의 간단한 식 $5/n$으로 위에서 누르고, 그 식이 $\varepsilon$ 아래로 내려가는 지점을 역으로 푼 결과이다. $N$은 최소일 필요가 없고, 존재만 하면 된다.

### 한정사의 순서와 부정

정의는 한정사의 순서를 포함하여 다음과 같이 적힌다.

$$\forall \varepsilon > 0\ \ \exists N \in \mathbb{N}\ \ \forall n \ge N\ \ \lvert a_n - L\rvert < \varepsilon$$

순서를 바꾸면 전혀 다른 명제가 된다. $\exists N\ \forall \varepsilon>0\ \forall n\ge N$ 순서로 쓰면 $n\ge N$인 모든 $n$에 대해 $\lvert a_n - L\rvert$가 모든 양수보다 작아야 하므로 $a_n=L$이고, 이는 $N$번째 항부터 상수인 수열만을 가리킨다. 또 $N$이 $n$에 의존하는 것을 허용하면 $N=n$으로 잡아 아무 수열이나 통과시키게 되므로, $N$은 $n$을 고르기 전에 $\varepsilon$만 보고 정해져야 한다.

정의를 부정하면 한정사가 각각 뒤집혀 $(a_n)$이 $L$로 수렴하지 않는다는 것은 $$\exists \varepsilon > 0\ \ \forall N \in \mathbb{N}\ \ \exists n \ge N\ \ \lvert a_n - L\rvert \ge \varepsilon$$ 이 성립한다는 것과 같다. 곧 어떤 고정된 $\varepsilon$에 대해, 아무리 큰 $N$ 뒤에서도 $L$에서 $\varepsilon$ 이상 떨어진 항이 계속 나타난다. 발산은 이것이 모든 실수 $L$에 대해 성립한다는 뜻이다.

수렴의 정의를 쓸 때 흔히 틀리는 지점이 몇 가지 있다. 첫째, $\lvert a_n - L\rvert<\varepsilon$이 *무한히 많은* $n$에 대해서만 성립하는 것은 수렴이 아니다. $a_n=(-1)^n$은 $L=1$에 대해 짝수 $n$에서 $\lvert a_n-L\rvert=0$이지만 수렴하지 않는다. 둘째, 정의의 부등식은 $<$이든 $\le$이든 같은 수렴을 준다. $\varepsilon$이 임의의 양수이므로 $\le\varepsilon$을 만족시키는 $N$을 $\varepsilon/2$에 대해 구하면 $<\varepsilon$이 되고, 같은 이유로 결론이 $\lvert a_n-L\rvert<C\varepsilon$ 꼴($C>0$ 고정)로 끝나도 증명은 완결된다. 셋째, 이웃한 항의 차 $\lvert a_{n+1}-a_n\rvert$가 $0$으로 가는 것만으로는 수렴하지 않는다. $a_n=\sqrt{n}$에서 $a_{n+1}-a_n = 1/(\sqrt{n+1}+\sqrt{n})\to 0$이지만 $a_n$은 위로 유계가 아니다.

## 극한의 기본 성질

극한이라는 표기 $\lim a_n$이 의미를 가지려면 극한이 하나뿐이어야 한다.

::: 명제 2 (극한의 유일성)
수열이 $L$과 $L'$ 모두로 수렴하면 $L=L'$이다.
:::

::: 증명
$L\ne L'$이라 가정하고 $\varepsilon=\lvert L-L'\rvert/2>0$으로 둔다. $\varepsilon$을 이렇게 고르는 이유는 $L$과 $L'$ 둘레의 반경 $\varepsilon$인 열린 구간이 서로 겹치지 않게 하기 위해서이다. $a_n\to L$이므로 $n\ge N_1$에서 $\lvert a_n-L\rvert<\varepsilon$이고, $a_n\to L'$이므로 $n\ge N_2$에서 $\lvert a_n-L'\rvert<\varepsilon$이다. $n\ge\max\{N_1,N_2\}$를 하나 잡으면 삼각부등식에 의해 $\lvert L-L'\rvert\le\lvert L-a_n\rvert+\lvert a_n-L'\rvert<2\varepsilon=\lvert L-L'\rvert$이 되어 모순이다.
:::

수열이 bounded라는 것은 어떤 $M\ge 0$이 존재하여 모든 $n$에서 $\lvert a_n\rvert\le M$인 것이다.

::: 명제 3
수렴하는 수열은 bounded이다.
:::

::: 증명
$a_n\to L$이라 하자. $\varepsilon=1$에 대한 $N$을 잡으면 $n\ge N$에서 $\lvert a_n\rvert\le\lvert a_n-L\rvert+\lvert L\rvert<\lvert L\rvert+1$이다. 나머지 항은 유한 개($a_1,\ldots,a_{N-1}$)이므로 $M=\max\{\lvert a_1\rvert,\ldots,\lvert a_{N-1}\rvert,\lvert L\rvert+1\}$이 모든 $n$에서 $\lvert a_n\rvert\le M$을 준다.
:::

이 증명에서 $\varepsilon=1$은 임의로 고른 것이 아니라, 꼬리 부분을 $L$ 근방의 유한한 범위에 가두는 것이 목적이므로 어떤 양수여도 되며 $1$이 가장 편할 뿐이다. 핵심은 정의가 꼬리 부분만 통제하고 앞부분은 유한 개이므로 최댓값이 존재한다는 점이다. 역은 성립하지 않는다.

::: 예시 4 ($(-1)^n$)
$a_n=(-1)^n$은 $\lvert a_n\rvert=1$이므로 bounded이지만 발산한다. 임의의 실수 $L$을 잡고 $\varepsilon=1$로 두자. $L\ge0$이면 홀수 $n$에서 $\lvert a_n-L\rvert=\lvert -1-L\rvert=1+L\ge1$이고, $L<0$이면 짝수 $n$에서 $\lvert a_n-L\rvert=1-L>1$이다. 어느 경우에도 임의로 큰 $N$ 뒤에 $n\ge N$인 홀수 또는 짝수 $n$이 있으므로 $a_n\not\to L$이다.
:::

따라서 bounded는 수렴의 필요조건일 뿐이다. bounded인 수열이 수렴하려면 아래 [정리 8](#thm8)처럼 추가 구조가 필요하다.

### 극한과 사칙연산

::: 정리 5 (극한의 사칙연산)
$a_n\to A$, $b_n\to B$이면 다음이 성립한다.

1. $a_n+b_n\to A+B$.
2. $a_nb_n\to AB$.
3. 모든 $n$에서 $b_n\ne0$이고 $B\ne0$이면 $a_n/b_n\to A/B$.
:::

::: 증명
(1) $\varepsilon>0$이 주어졌다고 하자. $a_n\to A$에 $\varepsilon/2$를 적용하여 $n\ge N_1$에서 $\lvert a_n-A\rvert<\varepsilon/2$를, $b_n\to B$에 $\varepsilon/2$를 적용하여 $n\ge N_2$에서 $\lvert b_n-B\rvert<\varepsilon/2$를 얻는다. $n\ge\max\{N_1,N_2\}$이면 $\lvert(a_n+b_n)-(A+B)\rvert\le\lvert a_n-A\rvert+\lvert b_n-B\rvert<\varepsilon/2+\varepsilon/2=\varepsilon$이다. 오차가 두 개 더해지므로 각각을 $\varepsilon/2$로 제어하면 합이 정확히 $\varepsilon$이 된다. 이것이 $\varepsilon/2$를 고르는 이유이고, 항이 $k$개이면 $\varepsilon/k$를 쓴다.

(2) $a_n b_n-AB=a_n(b_n-B)+B(a_n-A)$이므로 $\lvert a_nb_n-AB\rvert\le\lvert a_n\rvert\lvert b_n-B\rvert+\lvert B\rvert\lvert a_n-A\rvert$이다. [명제 3](#prop3)에 의하여 모든 $n$에서 $\lvert a_n\rvert\le M$인 $M$이 있다. $K=\max\{M,\lvert B\rvert\}+1>0$으로 두고 $\varepsilon'=\varepsilon/(2K)$에 대해 $n$이 충분히 크면 $\lvert a_n-A\rvert<\varepsilon'$, $\lvert b_n-B\rvert<\varepsilon'$이다. 그럼 $\lvert a_nb_n-AB\rvert<K\varepsilon'+K\varepsilon'=\varepsilon$이다. 여기서 $a_n$의 크기를 상수 $M$으로 눌러야 하는 이유는, 두 번째 인자의 오차 $\lvert b_n-B\rvert$ 앞에 $n$에 따라 변하는 $a_n$이 곱해져 있기 때문이다.

(3) 먼저 $1/b_n\to1/B$를 보인다. $\varepsilon_0=\lvert B\rvert/2$에 대해 $n\ge N_0$에서 $\lvert b_n-B\rvert<\lvert B\rvert/2$이므로 $\lvert b_n\rvert>\lvert B\rvert/2$이다. 그러므로 $n\ge N_0$에서
$$\left\lvert\frac1{b_n}-\frac1B\right\rvert=\frac{\lvert b_n-B\rvert}{\lvert b_n\rvert\lvert B\rvert}<\frac{2}{\lvert B\rvert^2}\lvert b_n-B\rvert$$
이다. 임의의 $\varepsilon>0$에 대해 $\lvert b_n-B\rvert<\varepsilon\lvert B\rvert^2/2$를 만족하는 $N_1$을 잡고 $n\ge\max\{N_0,N_1\}$을 취하면 좌변이 $\varepsilon$보다 작다. 이제 (2)를 $a_n$과 $1/b_n$에 적용하면 $a_n/b_n\to A/B$이다.
:::

정리의 항 수는 유한 개로 고정되어 있다는 점에 주의한다. 가령 $1+1/n\to1$이므로 $(1+1/n)^n\to1^n$이라고 쓸 수는 없다. 지수 $n$ 자체가 변하여 곱해지는 인자의 개수가 늘어나므로 [정리 5](#thm5)를 반복 적용한 것이 되지 않는다. 이 수열의 극한은 아래에서 $e$로 정의된다. 또 합이나 곱의 극한이 존재해도 각 수열이 수렴해야 하는 것은 아니다. $a_n=(-1)^n$, $b_n=-(-1)^n$은 둘 다 발산하지만 $a_n+b_n=0$은 수렴한다.

### 극한과 순서

::: 명제 6 (극한의 순서 보존)
$a_n\to A$, $b_n\to B$이고 충분히 큰 모든 $n$에서 $a_n\le b_n$이면 $A\le B$이다.
:::

::: 증명
$A>B$라 가정하고 $\varepsilon=(A-B)/2>0$으로 둔다. $n$이 충분히 크면 $a_n>A-\varepsilon=(A+B)/2$이고 $b_n<B+\varepsilon=(A+B)/2$이므로 $b_n<a_n$이 되어 가정에 모순이다.
:::

부등호가 엄격하면 극한에서는 엄격성이 사라진다. 모든 $n$에서 $1/n>0$이지만 $\lim 1/n=0$이다. 따라서 극한을 취하는 순간 $<$는 $\le$로 약해진다.

이를 이용한 조임정리는, 모르는 수열을 극한이 같은 두 수열 사이에 가두는 방법이다.

::: 정리 7 (조임정리)
충분히 큰 모든 $n$에서 $a_n\le c_n\le b_n$이고 $a_n\to L$, $b_n\to L$이면 $c_n\to L$이다.
:::

::: 증명
$\varepsilon>0$이 주어졌다고 하자. $n$이 충분히 크면 $a_n>L-\varepsilon$, $b_n<L+\varepsilon$, $a_n\le c_n\le b_n$이 모두 성립한다. 따라서 $L-\varepsilon<c_n<L+\varepsilon$, 곧 $\lvert c_n-L\rvert<\varepsilon$이다.
:::

두 수열의 극한이 같다는 조건이 본질적이다. $a_n=-1$, $b_n=1$이면 $c_n=(-1)^n$이 둘 사이에 있지만 수렴하지 않는다. 특별한 경우로 $\lvert c_n-L\rvert\le b_n$이고 $b_n\to0$이면 $c_n\to L$이다. 가령 $0<n!/n^n=\prod_{k=1}^{n}(k/n)\le1/n$이므로 $n!/n^n\to0$이다. 곱의 첫 인자 $1/n$만 남기고 나머지 인자는 모두 $1$ 이하라는 점만 쓴 것이다.

이와 같은 계산 수열의 극한을 [\[미적분학\] §수열의 극한, ⁋예시 6](/ko/math/calculus/sequences#ex6)에서도 다룬다.

## 단조수열

극한값을 모르는 채로 수렴만 보장하려면 완비성이 필요하다. 수열이 모든 $n$에서 $a_n\le a_{n+1}$이면 *증가*, $a_n\ge a_{n+1}$이면 *감소*한다고 하고, 둘을 합쳐 *단조수열*이라 한다.

::: 정리 8 (단조수렴정리)
위로 bounded인 증가수열은 수렴하고, 그 극한은 $\sup\{a_n\mid n\in\mathbb{N}\}$이다. 아래로 bounded인 감소수열은 수렴하고, 그 극한은 $\inf\{a_n\mid n\in\mathbb{N}\}$이다.
:::

::: 증명
$(a_n)$이 증가하고 위로 bounded라 하자. 집합 $\{a_n\}$은 공집합이 아니고 upper bound를 가지므로 [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3)에 의하여 $L=\sup\{a_n\}$이 존재한다. $\varepsilon>0$이 주어졌을 때 $L-\varepsilon$은 upper bound가 아니므로 $a_N>L-\varepsilon$인 $N$이 있다. $(a_n)$이 증가하므로 $n\ge N$에서 $L-\varepsilon<a_N\le a_n\le L<L+\varepsilon$이고, 따라서 $\lvert a_n-L\rvert<\varepsilon$이다. 감소하는 경우는 $(-a_n)$이 증가하며 위로 bounded이므로 앞의 경우를 적용하면 된다.
:::

수열이 증가하는 것만으로는 부족하고 위로 bounded여야 한다. $a_n=n$은 증가하지만 수렴하지 않는다. 반대로 bounded인 것만으로도 부족하여, [예시 4](#ex4)의 $(-1)^n$이 그 경우이다. 단조성과 bounded가 함께 있어야 완비성이 수렴으로 번역된다.

::: 예시 9 (점화식으로 정의된 수열)
$a_1=2$, $a_{n+1}=\frac12\left(a_n+\frac2{a_n}\right)$로 정의된 수열은 수렴하고 극한의 제곱은 $2$이다.

귀납법으로 모든 $n$에서 $a_n>0$이다. 다음으로
$$a_{n+1}^2-2=\frac14\left(a_n^2+4+\frac4{a_n^2}\right)-2=\left(\frac12\left(a_n-\frac2{a_n}\right)\right)^2\ge0$$
이므로 $n\ge2$에서 $a_n^2\ge2$이고, $a_1^2=4$이므로 모든 $n$에서 $a_n^2\ge2$이다. 그러므로 $a_n-a_{n+1}=\frac12(a_n-2/a_n)=(a_n^2-2)/(2a_n)\ge0$이어서 $(a_n)$은 감소하고, $0$ 아래로 내려가지 않으므로 아래로 bounded이다. [정리 8](#thm8)에 의하여 $a_n\to L$인 $L$이 존재한다.

이제 [정리 5](#thm5)에 의하여 $a_n^2\to L^2$이고, $a_n^2\ge2$이므로 [명제 6](#prop6)에 의하여 $L^2\ge2$, 특히 $L\ne0$이다. 또 $(a_{n+1})$도 $L$로 수렴하고 $2/a_n\to2/L$이므로 점화식의 양변에서 극한을 취하면 $L=\frac12(L+2/L)$이고 이를 정리하면 $L^2=2$이다.
:::

이 예에서 극한 $L$이 존재한다는 사실을 먼저 [정리 8](#thm8)로 확보한 뒤에 점화식의 극한을 취한다. 존재를 보이지 않고 "극한이 $L$이라 하면 $L=\frac12(L+2/L)$"로 시작하는 풀이는, 가령 $a_{n+1}=-a_n$의 경우처럼 극한이 없는 수열에도 $L=-L$이라는 방정식을 만들어 낼 수 있으므로 논증이 아니다.

### $(1+1/n)^n$의 수렴

$a_n=(1+1/n)^n$은 [정리 8](#thm8)의 전형적인 응용이다. 극한값은 식으로 적히지 않으므로 증가와 위로 bounded를 직접 보여야 한다.

::: 정리 10
수열 $a_n=(1+1/n)^n$은 수렴하며, 그 극한을 $e$로 적는다. $2\le e\le3$이다.
:::

::: 증명
이항정리에 의하여
$$a_n=\sum_{k=0}^{n}\binom nk\frac1{n^k}=\sum_{k=0}^{n}\frac1{k!}\prod_{j=0}^{k-1}\left(1-\frac jn\right)$$
이다. 여기서 $\binom nk/n^k=\frac{n(n-1)\cdots(n-k+1)}{k!\cdot n^k}$를 $k$개의 인자 $(n-j)/n$의 곱으로 쓴 것이고, $k=0$이면 빈 곱은 $1$이다.

증가함을 보인다. $0\le j<k\le n$에서 $1-j/n\le1-j/(n+1)$이고 두 쪽 모두 음이 아니므로, $a_n$의 $k$번째 항은 $a_{n+1}$의 $k$번째 항 이하이다. 또 $a_{n+1}$에는 $k=n+1$ 항이 더 있고 이는 양수이다. 따라서 $a_n\le a_{n+1}$이다.

위로 bounded임을 보인다. 곱의 각 인자가 $1$ 이하이므로 $a_n$의 $k$번째 항은 $1/k!$ 이하이다. $k\ge1$에서 $k!\ge2^{k-1}$이다($k=1$에서 성립하고, $(k+1)!=(k+1)k!\ge2\cdot2^{k-1}$이므로 귀납적으로 따른다). 그러므로
$$a_n\le1+\sum_{k=1}^{n}\frac1{2^{k-1}}=1+2\left(1-\frac1{2^n}\right)<3$$
이다. [정리 8](#thm8)에 의하여 $a_n$은 수렴한다. $a_n$이 증가하므로 모든 $n$에서 $a_n\ge a_1=2$이고, [명제 6](#prop6)에 의하여 $2\le e\le3$이다.
:::

위 증명에서 증가와 bounded가 모두 이항전개의 각 항을 비교하는 한 가지 장치로 해결된다는 점에 주목한다. 극한값이 식으로 주어지지 않는 수열은 이처럼 존재를 먼저 보인 뒤 극한에 이름을 붙이는 방식으로 상수를 도입한다.

## 무한대로의 발산

수렴하지 않는 수열 중에는 값이 한없이 커지는 경우가 있어, 이를 따로 구분한다.

::: 정의 11
수열 $(a_n)$이 *양의 무한대로 발산*한다는 것은, 임의의 $M\in\mathbb{R}$에 대하여 자연수 $N$이 존재하여 모든 $n\ge N$에서 $a_n>M$이 성립하는 것이며, $a_n\to\infty$ 또는 $\lim_{n\to\infty}a_n=\infty$로 적는다. $-a_n\to\infty$일 때 $a_n\to-\infty$로 적고 *음의 무한대로 발산*한다고 한다.
:::

[정의 1](#def1)에서 "$L$ 근방에 들어온다"를 "$M$보다 커진다"로 바꾼 것이다. $a_n\to\infty$라고 적어도 $\infty$는 실수가 아니므로 이는 [정의 1](#def1)의 수렴이 아니고, 실수의 수열로서는 여전히 발산이다. [정리 5](#thm5)는 실수 극한에 대한 진술이므로 극한이 $\pm\infty$일 때 그대로 쓸 수 없다.

::: 명제 12
수열 $(a_n)$에 대해 다음이 성립한다.

1. $a_n\to\infty$이면 $(a_n)$은 bounded가 아니다. 특히 발산한다.
2. $a_n\to\infty$이면 $n$이 충분히 클 때 $a_n>0$이고 $1/a_n\to0$이다.
3. 증가수열이 위로 bounded가 아니면 $a_n\to\infty$이다.
:::

::: 증명
(1) 모든 $n$에서 $\lvert a_n\rvert\le M_0$이라 하면 $M=M_0$에 대해 $a_N>M_0$인 $N$이 있어 모순이다. 발산은 [명제 3](#prop3)의 대우이다.

(2) $\varepsilon>0$이 주어지면 $M=1/\varepsilon$에 대해 $n\ge N$에서 $a_n>1/\varepsilon>0$이다. 따라서 $0<1/a_n<\varepsilon$이다.

(3) $M$이 주어지면 $M$은 $\{a_n\}$의 upper bound가 아니므로 $a_N>M$인 $N$이 있고, $(a_n)$이 증가하므로 $n\ge N$에서 $a_n\ge a_N>M$이다.
:::

[명제 12](#prop12)의 (1)의 역은 성립하지 않는다. $a_n=(-1)^nn$은 bounded가 아니지만 $\infty$로도 $-\infty$로도 발산하지 않는다. (2)의 역도 양수 조건 없이는 성립하지 않는다. $a_n=(-1)^n/n\to0$이지만 $1/a_n=(-1)^nn$은 $\pm\infty$ 어느 쪽으로도 가지 않는다. (3)과 [정리 8](#thm8)을 합치면 증가수열은 위로 bounded이면 수렴하고 아니면 $\infty$로 발산하므로, 증가수열에서는 이 둘 외의 다른 거동이 없다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
