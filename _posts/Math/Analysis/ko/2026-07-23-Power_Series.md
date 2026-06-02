---
title: "멱급수와 해석함수"
description: "멱급수의 수렴반경을 코시–아다마르 공식으로 정하고, 수렴반경 안의 컴팩트집합에서 균등수렴함을 보인다. 그로부터 항별 미분이 정당화되어 멱급수의 합이 해석함수임을 증명한다."
excerpt: "코시–아다마르 수렴반경, 균등수렴, 항별 미분과 해석함수"

categories: [Math / Analysis]
permalink: /ko/math/analysis/power_series
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Power_Series.png
    overlay_filter: 0.5

date: 2026-07-23
last_modified_at: 2026-07-23

weight: 18

published: false
---

[\[미적분학\] §멱급수](/ko/math/calculus/power_series)에서 멱급수의 항별 미분·적분을 받아들였다. 이제 [§균등수렴](/ko/math/analysis/uniform_convergence)을 갖추었으므로 그 근거를 엄밀하게 세운다. 핵심은 멱급수가 수렴반경 안에서 균등수렴한다는 것이다.

## 수렴반경

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (코시–아다마르)**</ins> 멱급수 $$\sum_{n=0}^\infty c_n (x - a)^n$$에 대하여

$$R = \frac{1}{\limsup_{n\to\infty} \lvert c_n\rvert^{1/n}}$$

으로 두면 ($$0$$과 $$\infty$$는 통상적으로 해석한다), $$\lvert x - a\rvert < R$$이면 절대수렴하고 $$\lvert x - a\rvert > R$$이면 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

근판정의 양 $$\limsup \lvert c_n (x-a)^n\rvert^{1/n} = \lvert x - a\rvert\,\limsup\lvert c_n\rvert^{1/n} = \lvert x - a\rvert/R$$를 본다. 이 값이 $$1$$보다 작으면, 곧 $$\lvert x - a\rvert < R$$이면 절대수렴하고, $$1$$보다 크면 일반항이 $$0$$으로 가지 않아 발산한다 ([§무한급수](/ko/math/analysis/series)의 근판정).

</details>

## 균등수렴과 항별 미분

수렴반경 안에서는 (끝까지는 아니어도) 컴팩트하게 균등수렴한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> $$0 < r < R$$이면 멱급수는 $$\lvert x - a\rvert \leq r$$에서 균등수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\lvert x - a\rvert \leq r$$이면 $$\lvert c_n(x-a)^n\rvert \leq \lvert c_n\rvert r^n =: M_n$$이고, $$r < R$$이므로 $$\sum M_n$$이 수렴한다 (정리 1). 바이어슈트라스 M-판정 ([§균등수렴, ⁋정리 4](/ko/math/analysis/uniform_convergence#thm4))에 의해 균등수렴한다.

</details>

균등수렴과 연속성 보존으로부터 멱급수의 합은 수렴반경 안에서 연속이고, 항별 미분이 정당화된다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$f(x) = \sum_{n=0}^\infty c_n (x-a)^n$$이 수렴반경 $$R > 0$$을 가지면, $$f$$는 $$\lvert x - a\rvert < R$$에서 무한히 미분가능하고

$$f'(x) = \sum_{n=1}^\infty n\,c_n (x - a)^{n-1}$$

이며, 이 도함수 급수도 수렴반경 $$R$$을 가진다. 따라서 $$c_n = \dfrac{f^{(n)}(a)}{n!}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\lim n^{1/n} = 1$$이므로 항별 미분한 급수의 수렴반경도 $$1/\limsup\lvert n c_n\rvert^{1/n} = R$$로 같다. 도함수 급수가 컴팩트하게 균등수렴하므로 (정리 2), 균등수렴하는 도함수열의 극한이 원래 극한의 도함수가 된다는 정리에 의해 $$f' $$가 항별 미분으로 주어진다. 이를 반복하면 $$f$$가 무한히 미분가능하고, $$x = a$$를 대입하면 $$f^{(n)}(a) = n!\,c_n$$이다.

</details>

## 해석함수

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 함수 $$f$$가 점 $$a$$ 근방에서 그곳을 중심으로 하는 멱급수와 일치하면 $$f$$가 $$a$$에서 *해석적<sub>analytic</sub>*이라 한다.

</div>

정리 3에 의해 해석함수는 무한히 미분가능하고 자신의 테일러 급수와 같다. 그러나 그 역은 거짓이다: $$f(x) = e^{-1/x^2}$$ ($$f(0) = 0$$) 은 무한히 미분가능하지만 $$0$$에서 모든 도함수가 $$0$$이어서 테일러 급수가 항등적으로 $$0$$이고, 따라서 $$0$$에서 해석적이지 않다. 즉 [\[미적분학\] §테일러 정리](/ko/math/calculus/taylor_theorem)의 테일러 급수가 함수로 수렴하는지는 나머지항의 거동에 달려 있으며, 매끄러움만으로는 보장되지 않는다.

해석함수는 실해석학과 복소해석학을 잇는 다리이며, 멱급수를 복소수 변수로 확장하면 한층 강력한 이론이 펼쳐진다. 다음으로는 미분을 여러 변수로 확장하는 [§다변수 미분](/ko/math/analysis/multivariable_differentiation)으로 나아간다.
