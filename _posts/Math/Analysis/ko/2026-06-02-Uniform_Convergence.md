---
title: "균등수렴"
description: "함수열의 균등수렴을 상한노름으로 정의하고, 균등극한이 연속성을 보존하며 극한과 적분이 교환됨을 증명한다. 함수항급수의 균등수렴을 보장하는 바이어슈트라스 M-판정법을 다룬다."
excerpt: "균등수렴, 연속성과 적분의 보존, 바이어슈트라스 M-판정"

categories: [Math / Analysis]
permalink: /ko/math/analysis/uniform_convergence
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 17

published: false
---

[§함수열과 점별수렴](/ko/math/analysis/sequences_of_functions)에서 점별수렴이 연속성과 적분을 보존하지 못함을 보았다. 그 병폐의 원인은 수렴 속도가 점마다 다른 데 있었다. 이를 막아 수렴이 정의역 전체에서 고르게 일어나도록 요구하는 것이 균등수렴이다.

## 균등수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수열 $$(f_n)$$이 $$f$$로 *균등수렴<sub>uniform convergence</sub>*한다는 것은, 임의의 $$\varepsilon > 0$$에 대하여 ($$x$$에 무관한) $$N$$이 존재하여 모든 $$n \geq N$$과 모든 $$x$$에 대해

$$\lvert f_n(x) - f(x)\rvert < \varepsilon$$

이 성립하는 것이다. 상한노름 $$\lVert g\rVert_\infty = \sup_x \lvert g(x)\rvert$$을 쓰면, 균등수렴은 $$\lVert f_n - f\rVert_\infty \to 0$$과 같다.

</div>

점별수렴과의 결정적 차이는 $$N$$이 점에 무관하다는 것이다. $$[0,1]$$에서 $$f_n(x) = x^n$$은 $$\lVert f_n - f\rVert_\infty = 1$$ ($$x$$를 $$1$$ 가까이 잡으면 $$f_n$$이 $$1$$에 가까우므로) 이어서 균등수렴하지 않으며, 이것이 그 극한이 불연속이었던 이유이다.

## 연속성과 적분의 보존

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> 연속함수들의 열 $$(f_n)$$이 $$f$$로 균등수렴하면 $$f$$도 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

점 $$a$$와 $$\varepsilon > 0$$에 대해, 균등수렴으로 $$\lVert f_n - f\rVert_\infty < \varepsilon/3$$인 $$n$$을 잡는다. $$f_n$$이 $$a$$에서 연속이므로 $$\lvert x - a\rvert < \delta$$이면 $$\lvert f_n(x) - f_n(a)\rvert < \varepsilon/3$$이다. 그러면

$$\lvert f(x) - f(a)\rvert \leq \lvert f(x) - f_n(x)\rvert + \lvert f_n(x) - f_n(a)\rvert + \lvert f_n(a) - f(a)\rvert < \varepsilon$$

이므로 $$f$$가 $$a$$에서 연속이다. 이 "$$\varepsilon/3$$ 논법"에서 첫째·셋째 항을 동시에 통제하는 데 균등성이 필수적이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 연속함수들의 열 $$(f_n)$$이 $$[a,b]$$에서 $$f$$로 균등수렴하면

$$\lim_{n\to\infty}\int_a^b f_n = \int_a^b f = \int_a^b \lim_{n\to\infty} f_n$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$는 [정리 2](#thm2)로 연속이므로 적분가능하다 ([§Riemann 적분, ⁋정리 4](/ko/math/analysis/riemann_integral#thm4)). 단조성에 의해

$$\left\lvert\int_a^b f_n - \int_a^b f\right\rvert \leq \int_a^b \lvert f_n - f\rvert \leq \lVert f_n - f\rVert_\infty\,(b - a) \to 0$$

이다.

</details>

[§함수열과 점별수렴, ⁋예시 3](/ko/math/analysis/sequences_of_functions#ex3)의 반례에서 적분이 교환되지 않았던 것은 그 수렴이 균등하지 않았기 때문이다. (미분에 대해서는 더 강하게, $$f_n'$$ 자체의 균등수렴을 요구해야 극한과 미분이 교환된다.)

## 바이어슈트라스 M-판정

함수항급수 $$\sum f_n$$의 균등수렴을 보장하는 실용적 기준이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (바이어슈트라스 M-판정)**</ins> 모든 $$x$$에서 $$\lvert f_n(x)\rvert \leq M_n$$이고 수치급수 $$\sum M_n$$이 수렴하면, 함수항급수 $$\sum f_n$$은 균등수렴(이며 절대수렴)한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

부분합 $$s_N = \sum_{n=1}^N f_n$$을 생각하자. $$M > N$$에 대해 $$\lVert s_M - s_N\rVert_\infty \leq \sum_{n=N+1}^M M_n$$인데, $$\sum M_n$$이 수렴하므로 우변은 $$N \to \infty$$에서 $$0$$으로 간다. 즉 $$(s_N)$$이 상한노름에 대해 Cauchy이고, 따라서 극한함수로 균등수렴한다 ([§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)의 완비성 논법을 상한노름 공간에 적용).

</details>

M-판정의 위력은 극한함수의 정체를 전혀 몰라도, 각 항의 크기를 $$x$$에 무관한 수 $$M_n$$으로 위에서 누르기만 하면 균등수렴이 따라 나온다는 데 있다. 이때 $$\sum M_n$$이 수렴하는지는 [§무한급수](/ko/math/analysis/series)에서 익힌 수치급수 판정법으로 결정되므로, 함수항급수의 균등수렴 문제가 익숙한 수치급수의 수렴 문제로 환원된다. 가령 $$\sum \sin(nx)/n^2$$은 $$\lvert\sin\rvert \leq 1$$로 $$x$$ 의존성을 한 번에 지워 $$M_n = 1/n^2$$을 얻으므로 $$\mathbb{R}$$ 전체에서 균등수렴하며, 더 일반적으로 $$\sum a_n \sin(nx)$$은 $$\sum \lvert a_n\rvert < \infty$$이면 같은 방식으로 균등수렴한다. 다만 M-판정은 충분조건일 뿐이어서, 이를 통과하지 못한다고 해서 균등수렴이 곧 부정되는 것은 아니다.

## 균등 Cauchy 판정

극한함수를 미리 알지 못하는 상황에서 균등수렴을 직접 확인하는 도구가 균등 Cauchy 조건이다. 수치열에서 Cauchy 조건이 극한을 언급하지 않고 수렴을 가려냈던 것처럼 ([§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4)), 함수열에서도 같은 일을 한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (균등 Cauchy 판정)**</ins> 함수열 $$(f_n)$$이 어떤 극한 $$f$$로 균등수렴하는 것은, 임의의 $$\varepsilon > 0$$에 대하여 ($$x$$에 무관한) $$N$$이 존재하여 모든 $$m, n \geq N$$과 모든 $$x$$에 대해

$$\lvert f_m(x) - f_n(x)\rvert < \varepsilon$$

이 성립하는 것, 곧 $$(f_n)$$이 상한노름에 대해 *균등 Cauchy<sub>uniformly Cauchy</sub>*인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$(f_n)$$이 $$f$$로 균등수렴한다고 하자. $$\varepsilon > 0$$에 대해 $$n \geq N$$이면 $$\lVert f_n - f\rVert_\infty < \varepsilon/2$$인 $$N$$을 잡으면, $$m, n \geq N$$에서 모든 $$x$$에 대해

$$\begin{aligned}
\lvert f_m(x) - f_n(x)\rvert &\leq \lvert f_m(x) - f(x)\rvert + \lvert f(x) - f_n(x)\rvert \\
&\leq \lVert f_m - f\rVert_\infty + \lVert f_n - f\rVert_\infty \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon
\end{aligned}$$

이므로 균등 Cauchy이다.

역으로 $$(f_n)$$이 균등 Cauchy라 하자. 각 고정된 $$x$$에서 수열 $$(f_n(x))$$은 (균등 Cauchy 조건의 특수한 경우로) 수치 Cauchy 수열이므로 실수의 완비성에 의해 어떤 값으로 수렴한다 ([§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4)). 그 극한을 $$f(x)$$로 두면 점별극한 $$f$$가 정의된다. 이제 균등 Cauchy 조건에서 $$m, n \geq N$$이면 모든 $$x$$에 대해 $$\lvert f_m(x) - f_n(x)\rvert < \varepsilon$$인데, 여기서 $$m \to \infty$$로 보내면 $$f_m(x) \to f(x)$$이므로

$$\lvert f(x) - f_n(x)\rvert \leq \varepsilon \qquad (n \geq N,\ \text{모든 } x)$$

를 얻는다. 좌변의 상한을 취하면 $$\lVert f - f_n\rVert_\infty \leq \varepsilon$$이므로 $$(f_n)$$은 $$f$$로 균등수렴한다.

</details>

균등 Cauchy 조건은 극한 $$f$$를 식에 끌어들이지 않으므로, M-판정의 증명에서 부분합열의 균등수렴을 확인할 때처럼 극한을 모르는 채로 균등수렴을 결론짓는 데 특히 유용하다. 실제로 [정리 4](#thm4)의 증명은 부분합열이 균등 Cauchy임을 보인 것에 다름 아니다.

## 균등수렴의 민감성과 한계

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (구간을 좁혀야 하는 기하급수)**</ins> 기하급수 $$\sum_{n=0}^\infty x^n$$을 보자. $$0 < r < 1$$로 고정하면 $$\lvert x\rvert \leq r$$인 모든 $$x$$에서 $$\lvert x^n\rvert \leq r^n =: M_n$$이고 $$\sum r^n$$이 수렴하므로, M-판정에 의해 급수는 $$[-r, r]$$에서 균등수렴한다. 그러나 열린구간 $$(-1, 1)$$ 전체에서는 균등수렴하지 않는다. 실제로 부분합과 합의 차는

$$\left\lvert \frac{1}{1-x} - \sum_{n=0}^{N} x^n\right\rvert = \left\lvert \frac{x^{N+1}}{1-x}\right\rvert$$

인데, $$x \to 1^-$$로 보내면 이 값은 임의로 커지므로 $$N$$을 아무리 크게 잡아도 상한노름이 $$0$$으로 가지 않는다.

</div>

[예시 6](#ex6)은 균등수렴이 정의역에 민감함을 보여 준다. 같은 급수라도 컴팩트한 부분구간으로 제한하면 균등수렴하지만 경계에 다가가는 점들을 포함하면 그렇지 않을 수 있다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (균등수렴이라도 미분은 안 됨)**</ins> $$\mathbb{R}$$에서 $$f_n(x) = \sin(nx)/\sqrt{n}$$을 보자. 모든 $$x$$에서

$$\lvert f_n(x)\rvert \leq \frac{1}{\sqrt{n}} \to 0$$

이므로 $$\lVert f_n - 0\rVert_\infty \leq 1/\sqrt{n} \to 0$$, 즉 $$f_n$$은 $$0$$으로 균등수렴한다. 그러나 도함수는

$$f_n'(x) = \sqrt{n}\,\cos(nx)$$

이어서 $$x = 0$$에서 $$f_n'(0) = \sqrt{n} \to \infty$$이다. 극한함수 $$0$$의 도함수는 $$0$$이므로

$$\lim_{n\to\infty} f_n'(0) \neq \Bigl(\lim_{n\to\infty} f_n\Bigr)'(0)$$

이다. 이는 함수열의 균등수렴만으로는 극한과 미분의 교환이 보장되지 않으며, 도함수열 $$(f_n')$$ 자체의 균등수렴이 따로 필요함을 보여 준다.

</div>

[예시 7](#ex7)은 적분과 달리 미분은 균등수렴만으로 극한과 교환되지 않음을 드러낸다. 마지막으로 균등수렴이 함수의 유계성을 보존함을 확인해 두자.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (유계성의 보존)**</ins> 유계함수들의 열 $$(f_n)$$이 $$f$$로 균등수렴하면 $$f$$도 유계이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

균등수렴으로 $$\lVert f_N - f\rVert_\infty < 1$$인 $$N$$을 잡고, $$f_N$$이 유계이므로 $$\lVert f_N\rVert_\infty \leq B$$인 $$B$$를 잡는다. 그러면 모든 $$x$$에 대해

$$\begin{aligned}
\lvert f(x)\rvert &\leq \lvert f(x) - f_N(x)\rvert + \lvert f_N(x)\rvert \\
&\leq \lVert f - f_N\rVert_\infty + \lVert f_N\rVert_\infty \\
&< 1 + B
\end{aligned}$$

이므로 $$f$$는 상수 $$1 + B$$로 유계이다.

</details>

유계성의 보존은 점별수렴에서는 깨지는 성질이다 ([§함수열과 점별수렴, ⁋예시 6](/ko/math/analysis/sequences_of_functions#ex6)). 점별수렴은 각 점에서 독립적으로 수렴값을 줄 뿐이어서, 점마다 다른 속도로 수렴하면 극한이 무한정 커질 수 있다. 균등수렴은 단 하나의 $$N$$으로 모든 점을 동시에 잡아 두므로 이런 일이 일어나지 않으며, [명제 8](#prop8)은 그 차이를 가장 단순하게 드러낸다.

균등수렴은 극한 연산과 미적분 연산을 교환할 수 있게 해 주는 핵심 조건이다.
