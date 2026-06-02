---
title: "Cauchy 수열과 완비성"
description: "극한값을 미리 알 필요 없이 수렴을 판정하는 Cauchy 수열을 정의하고, 실수에서 Cauchy인 것과 수렴하는 것이 동치임을 증명한다. 이 동치가 완비성의 또 다른 형태이며 거리공간의 완비성 개념으로 일반화됨을 본다."
excerpt: "Cauchy 수열, Cauchy 판정법, 완비성의 동치 형태"

categories: [Math / Analysis]
permalink: /ko/math/analysis/cauchy_sequences
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Cauchy_Sequences.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
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

Cauchy 판정법의 진정한 가치는 극한을 모르고도 수렴을 보일 수 있다는 데 있으며, 이는 [§무한급수](/ko/math/analysis/series)의 수렴 판정에서 곧바로 활용된다. 또한 항들 사이의 거리만으로 정식화되는 Cauchy 조건은 거리만 주어진 일반적 공간으로 그대로 옮겨져, [§거리공간](/ko/math/analysis/metric_spaces)에서 *완비 거리공간*의 정의가 된다.
