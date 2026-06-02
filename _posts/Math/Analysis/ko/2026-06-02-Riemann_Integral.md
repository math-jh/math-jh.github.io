---
title: "Riemann 적분"
description: "다르부의 상합과 하합으로 Riemann 적분을 엄밀하게 정의하고, 적분가능성의 판정 기준을 제시한다. 컴팩트구간 위의 연속함수가 균등연속성을 통해 적분가능함을 증명한다."
excerpt: "다르부 상합·하합, 적분가능성 판정, 연속함수의 적분가능성"

categories: [Math / Analysis]
permalink: /ko/math/analysis/riemann_integral
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Riemann_Integral.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 14

published: false
---

[\[미적분학\] §정적분](/ko/math/calculus/definite_integral)에서 정적분을 리만 합의 극한으로 도입하면서, 연속함수의 적분가능성은 증명 없이 받아들였다. 이제 [§컴팩트성](/ko/math/analysis/compactness)과 균등연속성을 갖추었으므로, 적분을 엄밀하게 정초하고 그 사실을 증명한다.

## 다르부 상합과 하합

극한을 직접 다루는 대신, 위와 아래에서 죄어 오는 두 합을 쓴다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 유계함수 $$f : [a,b] \to \mathbb{R}$$와 분할 $$P : a = x_0 < \cdots < x_n = b$$에 대하여, 각 부분구간에서 $$m_i = \inf_{[x_{i-1}, x_i]} f$$, $$M_i = \sup_{[x_{i-1}, x_i]} f$$로 두고

$$L(P, f) = \sum_{i=1}^n m_i\,\Delta x_i, \qquad U(P, f) = \sum_{i=1}^n M_i\,\Delta x_i$$

를 각각 *하합<sub>lower sum</sub>*과 *상합<sub>upper sum</sub>*이라 한다.

</div>

분할을 더 잘게 하면 하합은 늘고 상합은 줄어들며 언제나 $$L(P, f) \leq U(Q, f)$$이다. 따라서 *하적분* $$\underline{\int} f = \sup_P L(P, f)$$과 *상적분* $$\overline{\int} f = \inf_P U(P, f)$$이 존재하고 $$\underline{\int} f \leq \overline{\int} f$$이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\underline{\int} f = \overline{\int} f$$일 때 $$f$$가 $$[a,b]$$에서 *Riemann 적분가능*하다고 하고, 그 공통값을 $$\int_a^b f$$로 적는다.

</div>

## 적분가능성 판정

상합과 하합의 차를 임의로 작게 만들 수 있는지가 적분가능성을 결정한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Riemann 판정법)**</ins> 유계함수 $$f$$가 적분가능한 것은, 임의의 $$\varepsilon > 0$$에 대하여 $$U(P, f) - L(P, f) < \varepsilon$$인 분할 $$P$$가 존재하는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

그런 $$P$$가 있으면 $$0 \leq \overline{\int} f - \underline{\int} f \leq U(P,f) - L(P,f) < \varepsilon$$이 임의의 $$\varepsilon$$에 대해 성립하므로 상적분과 하적분이 같다. 역으로 적분가능하면, 상적분·하적분의 정의에서 $$U(P_1, f) < \overline{\int} f + \varepsilon/2$$, $$L(P_2, f) > \underline{\int} f - \varepsilon/2$$인 분할이 있고, 두 분할의 공통세분 $$P$$를 잡으면 $$U(P,f) - L(P,f) < \varepsilon$$이다.

</details>

## 연속함수의 적분가능성

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> $$[a,b]$$에서 연속인 함수는 Riemann 적분가능하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$는 컴팩트구간 $$[a,b]$$에서 연속이므로 균등연속이다 ([§연속함수의 성질, ⁋정리 4](/ko/math/analysis/continuous_functions#thm4)). 임의의 $$\varepsilon > 0$$에 대해, 균등연속성으로 $$\lvert x - y\rvert < \delta$$이면 $$\lvert f(x) - f(y)\rvert < \dfrac{\varepsilon}{b - a}$$이게 하는 $$\delta$$가 있다. 너비가 $$\delta$$ 미만인 분할 $$P$$를 잡으면, 각 부분구간에서 $$f$$가 (컴팩트성으로) 최댓값과 최솟값을 가지므로 $$M_i - m_i \leq \dfrac{\varepsilon}{b-a}$$이고

$$U(P, f) - L(P, f) = \sum_i (M_i - m_i)\Delta x_i \leq \frac{\varepsilon}{b-a}\sum_i \Delta x_i = \varepsilon$$

이다. 정리 3에 의해 $$f$$는 적분가능하다.

</details>

이로써 [\[미적분학\] §정적분, ⁋정리 3](/ko/math/calculus/definite_integral#thm3)에서 받아들였던 연속함수의 적분가능성이 완비성에 기초하여 증명되었다. 같은 다르부 틀에서 선형성·구간가법성·단조성도 따라 나온다. 미분과 적분을 잇는 다리는 다음 글 [§미적분의 기본정리](/ko/math/analysis/fundamental_theorem_of_calculus)에서 엄밀하게 세운다.
