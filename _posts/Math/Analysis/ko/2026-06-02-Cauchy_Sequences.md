---
title: "Cauchy 수열과 완비성"
description: "극한값을 미리 알 필요 없이 수렴을 판정하는 Cauchy 수열을 정의하고, 실수에서 Cauchy인 것과 수렴하는 것이 동치임을 증명한다. 이 동치가 완비성의 또 다른 형태이며 거리공간의 완비성 개념으로 일반화됨을 본다."
excerpt: "Cauchy 수열, Cauchy 판정법, 완비성의 동치 형태"

categories: [Math / Analysis]
permalink: /ko/math/analysis/cauchy_sequences
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 3

published: false
---

[§수열의 수렴](/ko/math/analysis/convergence_of_sequences)의 단조수렴정리는 강력하지만 단조수열에만 쓸 수 있고, 극한이 무엇인지 알아야 수렴을 정의할 수 있다. 극한값을 미리 지목하지 않고 "항들이 자기들끼리 점점 가까워진다"는 내부적 조건만으로 수렴을 판정할 수 있다면 훨씬 유용할 것이다. 그것이 Cauchy 수열이며, 실수에서는 이 조건이 수렴과 정확히 동치이다.

## Cauchy 수열

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 수열 $$(a_n)$$이 *Cauchy 수열<sub>Cauchy sequence</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대하여 자연수 $$N$$이 존재하여 모든 $$m, n \geq N$$에 대해

$$\lvert a_m - a_n\rvert < \varepsilon$$

이 성립하는 것이다.

</div>

수렴의 정의가 항과 *극한* 사이의 거리를 통제하는 반면, Cauchy 조건은 항들 *서로* 사이의 거리만을 통제한다. 후자는 극한이라는 외부 대상을 언급하지 않는다.

## 수렴과 Cauchy 조건

수렴하는 수열이 Cauchy임은 어렵지 않다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 수렴하는 수열은 Cauchy 수열이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a_n \to L$$이라 하자. 임의의 $$\varepsilon > 0$$에 대해 $$N$$을 잡아 $$n \geq N$$이면 $$\lvert a_n - L\rvert < \varepsilon/2$$이게 한다. 그러면 $$m, n \geq N$$일 때 삼각부등식으로 $$\lvert a_m - a_n\rvert \leq \lvert a_m - L\rvert + \lvert L - a_n\rvert < \varepsilon$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Cauchy 수열은 유계이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varepsilon = 1$$에 대응하는 $$N$$을 잡으면, $$n \geq N$$에서 $$\lvert a_n - a_N\rvert < 1$$, 즉 $$\lvert a_n\rvert < \lvert a_N\rvert + 1$$이다. 유한개의 항을 포함해 $$M = \max\{\lvert a_1\rvert, \ldots, \lvert a_{N-1}\rvert, \lvert a_N\rvert + 1\}$$로 두면 모든 $$n$$에서 $$\lvert a_n\rvert \leq M$$이다.

</details>

핵심은 그 역, 즉 Cauchy이면 반드시 수렴한다는 사실이며, 여기에서 비로소 실수의 완비성이 본질적으로 쓰인다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Cauchy 판정법)**</ins> 실수열 $$(a_n)$$이 수렴하는 것은 그것이 Cauchy 수열인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

수렴 $$\Rightarrow$$ Cauchy는 명제 2이다. 역을 보이자. $$(a_n)$$이 Cauchy이면 명제 3에 의해 유계이고, Bolzano–Weierstrass 정리 ([§부분수열과 Bolzano–Weierstrass 정리](/ko/math/analysis/bolzano_weierstrass))에 의해 수렴하는 부분수열 $$a_{n_k} \to L$$이 존재한다. 이제 전체 수열이 같은 $$L$$로 수렴함을 보인다. 임의의 $$\varepsilon > 0$$에 대해, Cauchy 조건으로 $$m, n \geq N$$이면 $$\lvert a_m - a_n\rvert < \varepsilon/2$$이게 $$N$$을 잡고, 부분수열의 수렴으로 $$n_k \geq N$$이면서 $$\lvert a_{n_k} - L\rvert < \varepsilon/2$$인 $$k$$를 잡는다. 그러면 모든 $$n \geq N$$에 대해

$$\lvert a_n - L\rvert \leq \lvert a_n - a_{n_k}\rvert + \lvert a_{n_k} - L\rvert < \varepsilon$$

이므로 $$a_n \to L$$이다.

</details>

## 완비성의 동치 형태

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> 정리 4에서 "Cauchy $$\Rightarrow$$ 수렴"은 실수의 완비성과 동치이다. 실제로 이 성질을 *완비성*의 정의로 채택하는 길도 있으며, 상한 성질로부터 (Bolzano–Weierstrass를 거쳐) 이를 유도한 것이 정리 4이다.

</div>

이 동치는 $$\mathbb{Q}$$ 위에서는 깨진다. 예컨대 $$\sqrt{2}$$의 십진 근삿값으로 이루어진 유리수열 $$1, 1.4, 1.41, 1.414, \ldots$$은 항들끼리 한없이 가까워지므로 Cauchy이지만, 그 극한 $$\sqrt{2}$$가 유리수가 아니므로 $$\mathbb{Q}$$ 안에서는 수렴하지 않는다. 완비성이란 바로 이런 "수렴해야 마땅한" Cauchy 수열이 실제로 극한을 갖도록 빈틈을 메운 것이다.

이 빈틈을 좀 더 정량적으로 들여다보자. 위 유리수열 $$a_n$$을 $$\sqrt 2$$의 소수점 아래 $$n-1$$자리까지의 근삿값이라 하면, $$m, n \geq N$$일 때 두 항은 소수점 아래 $$N-1$$자리까지 일치하므로

$$\lvert a_m - a_n\rvert \leq 10^{-(N-1)}$$

이 성립한다. 따라서 임의의 $$\varepsilon > 0$$에 대해 $$10^{-(N-1)} < \varepsilon$$이 되도록 $$N$$을 크게 잡으면 Cauchy 조건이 충족된다. 정의 1의 검증이 극한 $$\sqrt 2$$를 한 번도 언급하지 않았다는 점이 핵심이다. 같은 부등식이 $$\mathbb{R}$$ 안에서는 $$a_n \to \sqrt 2$$를 보장하지만, $$\mathbb{Q}$$ 안에서는 갈 곳이 없다.

## 예시와 계산

Cauchy 판정법의 가치는 극한값을 모르는 채로 수렴을 확정할 수 있다는 데 있다. 아래의 예시들은 정의 1과 정리 4를 직접 적용하여, 극한을 따로 구하지 않고도 수렴 여부를 가르는 전형적인 계산을 보인다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (조화급수의 부분합)**</ins> 조화급수의 부분합 $$s_n = \sum_{k=1}^{n} \dfrac{1}{k}$$이 이루는 수열은 Cauchy가 아니다. $$n = 2N$$, $$m = N$$을 택하면

$$\begin{aligned}
\lvert s_{2N} - s_N\rvert &= \sum_{k=N+1}^{2N} \frac{1}{k} \\
&\geq \sum_{k=N+1}^{2N} \frac{1}{2N} \\
&= \frac{N}{2N} = \frac{1}{2}
\end{aligned}$$

이므로, $$\varepsilon = \tfrac12$$에 대해서는 아무리 큰 $$N$$을 잡아도 $$m, n \geq N$$이면서 $$\lvert s_m - s_n\rvert \geq \tfrac12$$인 짝이 존재한다. 따라서 $$(s_n)$$은 Cauchy 조건을 어기고, 정리 4의 대우에 의해 발산한다. 극한값을 구하지 않고 발산을 증명한 셈이다.

</div>

위 예시는 Cauchy 조건의 부정이 발산의 직접 증명으로 쓰이는 전형을 보여 준다. 반대로 항 사이의 거리가 충분히 빠르게 줄어들면 수렴을 곧바로 끌어낼 수 있다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (교대조화급수의 부분합)**</ins> 교대조화급수의 부분합 $$t_n = \sum_{k=1}^{n} \dfrac{(-1)^{k-1}}{k}$$을 보자. $$m > n$$일 때 차

$$t_m - t_n = \frac{(-1)^{n}}{n+1} + \frac{(-1)^{n+1}}{n+2} + \cdots + \frac{(-1)^{m-1}}{m}$$

은 절댓값이 단조감소하며 부호가 번갈아 나타나는 합이다. 이런 교대합은 첫 항으로 위에서 눌리므로

$$\lvert t_m - t_n\rvert \leq \frac{1}{n+1}$$

이 성립한다. 따라서 임의의 $$\varepsilon > 0$$에 대해 $$\dfrac{1}{N+1} < \varepsilon$$이 되도록 $$N$$을 잡으면 모든 $$m, n \geq N$$에서 $$\lvert t_m - t_n\rvert < \varepsilon$$이고, $$(t_n)$$은 Cauchy이다. 정리 4에 의해 수렴하며, 그 극한이 $$\ln 2$$임은 여기서 쓰지 않았다.

</div>

조화급수와 교대조화급수의 대조는 Cauchy 판정법이 부분합 사이의 거리를 직접 다룬다는 점을 잘 드러낸다. 다음 예시는 거리가 기하급수적으로 줄어드는 경우이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (기하적으로 가까워지는 수열)**</ins> 어떤 $$0 \leq r < 1$$과 상수 $$C$$에 대해 모든 $$n$$에서 $$\lvert a_{n+1} - a_n\rvert \leq C r^n$$이라 하자. 그러면 $$m > n$$일 때 삼각부등식과 기하급수의 합으로

$$\begin{aligned}
\lvert a_m - a_n\rvert &\leq \sum_{k=n}^{m-1} \lvert a_{k+1} - a_k\rvert \\
&\leq \sum_{k=n}^{m-1} C r^k \\
&\leq C \sum_{k=n}^{\infty} r^k = \frac{C r^n}{1 - r}
\end{aligned}$$

이다. $$r < 1$$이므로 $$r^n \to 0$$이고, 따라서 임의의 $$\varepsilon > 0$$에 대해 $$\dfrac{C r^N}{1-r} < \varepsilon$$이 되도록 $$N$$을 잡으면 모든 $$m, n \geq N$$에서 $$\lvert a_m - a_n\rvert < \varepsilon$$이다. 즉 $$(a_n)$$은 Cauchy이고 정리 4에 의해 수렴한다.

</div>

예시 8의 가정은 인접한 두 항의 거리만 통제하는데도 수열 전체의 수렴을 보장한다. 다만 인접 항의 거리가 $$0$$으로 가는 것만으로는 충분하지 않음에 주의해야 한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (인접 거리가 0으로 가도 Cauchy가 아닌 예)**</ins> $$a_n = \sqrt{n}$$이라 하면

$$\lvert a_{n+1} - a_n\rvert = \sqrt{n+1} - \sqrt{n} = \frac{1}{\sqrt{n+1} + \sqrt{n}} \to 0$$

이므로 인접한 두 항의 거리는 $$0$$으로 간다. 그러나 $$m = 4N$$, $$n = N$$을 택하면

$$\lvert a_{4N} - a_N\rvert = 2\sqrt{N} - \sqrt{N} = \sqrt{N} \to \infty$$

이므로, $$\varepsilon = 1$$에 대해서조차 Cauchy 조건이 깨진다. 따라서 $$(\sqrt n)$$은 Cauchy가 아니며, 실제로 $$\infty$$로 발산한다. Cauchy 조건은 "임의로 멀리 떨어진 두 첨자"를 함께 통제해야 하며, 인접 항만의 거리로 환원되지 않는다.

</div>

예시 9는 정의 1에서 "모든 $$m, n \geq N$$"이라는 두 자유 첨자가 본질적임을 보여 준다. 인접 항의 차만 다루면 예시 8과 같은 추가 가정(거리의 합 가능성)이 따로 필요하다.

## 수축수열

극한을 모르고도 수렴을 보장하는 가장 깔끔한 충분조건은, 연속한 두 차가 일정한 비율로 줄어드는 *수축<sub>contractive</sub>* 조건이다. 이는 예시 8을 명제로 다듬은 것이며, 반복 대입으로 정의되는 수열의 수렴 증명에서 표준적으로 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (수축수열의 수렴)**</ins> 어떤 상수 $$0 \leq c < 1$$이 존재하여 모든 $$n$$에서

$$\lvert a_{n+1} - a_n\rvert \leq c\,\lvert a_n - a_{n-1}\rvert$$

이 성립하면, $$(a_n)$$은 Cauchy 수열이고 따라서 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

가정을 반복 적용하면 $$d_n = \lvert a_{n+1} - a_n\rvert$$에 대해 $$d_n \leq c\, d_{n-1} \leq \cdots \leq c^{n-1} d_1$$, 즉

$$\lvert a_{n+1} - a_n\rvert \leq c^{n-1} \lvert a_2 - a_1\rvert$$

이다. 그러면 $$m > n$$일 때 예시 8과 같은 계산으로

$$\begin{aligned}
\lvert a_m - a_n\rvert &\leq \sum_{k=n}^{m-1} \lvert a_{k+1} - a_k\rvert \\
&\leq \lvert a_2 - a_1\rvert \sum_{k=n}^{m-1} c^{k-1} \\
&\leq \lvert a_2 - a_1\rvert \cdot \frac{c^{n-1}}{1 - c}
\end{aligned}$$

을 얻는다. $$0 \leq c < 1$$이므로 $$c^{n-1} \to 0$$이고, 우변은 $$n \to \infty$$에서 $$0$$으로 수렴한다. 따라서 임의의 $$\varepsilon > 0$$에 대해 $$N$$을 충분히 크게 잡으면 모든 $$m, n \geq N$$에서 $$\lvert a_m - a_n\rvert < \varepsilon$$이 되어 $$(a_n)$$은 Cauchy이고, 정리 4에 의해 수렴한다.

</details>

수축 조건은 그 자체로 극한값을 알려 주지 않지만, 수열이 어딘가로 모인다는 사실만큼은 보장한다. 이것이 Cauchy 판정법이 빛을 발하는 지점이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (반복 대입으로 정의된 수열)**</ins> $$a_1 = 1$$이고 $$a_{n+1} = 1 + \dfrac{1}{a_n}$$으로 정의되는 수열을 보자. 모든 항이 $$1$$ 이상이므로 $$a_n \geq 1$$이고, 두 차를 비교하면

$$\lvert a_{n+1} - a_n\rvert = \left\lvert \frac{1}{a_n} - \frac{1}{a_{n-1}} \right\rvert = \frac{\lvert a_n - a_{n-1}\rvert}{a_n\, a_{n-1}} \leq \lvert a_n - a_{n-1}\rvert$$

이 된다. 더 정밀하게 보면 두 번째 항부터는 $$a_n \geq \tfrac32$$이므로 $$a_n a_{n-1} \geq \tfrac94 > 2$$여서 $$c = \tfrac12$$로 수축 조건이 성립한다. 명제 10에 의해 $$(a_n)$$은 수렴한다. 그 극한 $$L$$은 점화식의 양변에 극한을 취해 얻는 $$L = 1 + \dfrac{1}{L}$$, 곧 $$L^2 - L - 1 = 0$$의 양의 해 $$L = \dfrac{1 + \sqrt 5}{2}$$이다. 수렴은 명제 10이 보장하고, 극한값은 그 다음에 방정식을 풀어 얻는다.

</div>

이처럼 수렴의 *존재*를 먼저 Cauchy 판정법으로 확보한 뒤 극한값을 따로 결정하는 순서는, 점화식이나 급수로 정의된 대상을 다룰 때 거듭 쓰이는 표준적 전략이다.

Cauchy 판정법의 진정한 가치는 극한을 모르고도 수렴을 보일 수 있다는 데 있으며, 이는 [§무한급수](/ko/math/analysis/series)의 수렴 판정에서 곧바로 활용된다. 또한 항들 사이의 거리만으로 정식화되는 Cauchy 조건은 거리만 주어진 일반적 공간으로 그대로 옮겨져, [§거리공간](/ko/math/analysis/metric_spaces)에서 *완비 거리공간*의 정의가 된다.
