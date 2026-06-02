---
title: "수열의 극한"
description: "수열의 수렴을 직관적으로 도입하고 극한 법칙과 단조수렴을 정리하며, 자연상수 e의 정의를 포함한 표준적인 극한들을 계산한다. 무한급수로 나아가는 토대를 마련한다."
excerpt: "수열의 수렴, 극한 법칙, 표준 극한과 e"

categories: [Math / Calculus]
permalink: /ko/math/calculus/sequences
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Sequences.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 13

published: false
---

함수의 극한 ([§함수와 극한](/ko/math/calculus/functions_and_limits))을 다루며 우리는 이미 $$n \to \infty$$의 거동을 암묵적으로 사용해 왔다. 이 글에서는 수열의 극한을 정면으로 다루어, 다음 글들의 무한급수와 멱급수를 위한 계산 도구를 갖춘다.

## 수열의 수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 수열 $$(a_n)$$이 실수 $$L$$로 *수렴<sub>converges</sub>*한다는 것은, $$n$$을 충분히 크게 하면 $$a_n$$을 $$L$$에 원하는 만큼 가깝게 만들 수 있다는 것이다. 정밀하게는, 임의의 $$\varepsilon > 0$$에 대해 $$n \geq N$$이면 $$\lvert a_n - L\rvert < \varepsilon$$이게 하는 $$N$$이 존재하는 것이며, 이를 $$\lim_{n\to\infty} a_n = L$$로 적는다.

</div>

이 정의의 엄밀한 전개와 극한의 유일성·유계성은 해석학 [\[해석학\] §수열의 수렴](/ko/math/analysis/convergence_of_sequences)에서 다룬다. 여기서는 계산에 필요한 성질을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (극한 법칙)**</ins> $$a_n \to A$$, $$b_n \to B$$이면 $$a_n + b_n \to A + B$$, $$a_n b_n \to AB$$이고, $$B \neq 0$$이면 $$a_n/b_n \to A/B$$이다. 또 $$a_n \leq c_n \leq b_n$$이고 $$a_n, b_n \to L$$이면 $$c_n \to L$$이다 (조임).

</div>

## 표준 극한

자주 쓰이는 기본 극한들을 모은다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 다음이 성립한다.

- $$\lvert r\rvert < 1$$이면 $$r^n \to 0$$, $$r = 1$$이면 $$\to 1$$, $$\lvert r\rvert > 1$$이면 발산한다.
- $$p > 0$$에 대해 $$\dfrac{1}{n^p} \to 0$$, 그리고 $$n^{1/n} \to 1$$, $$p^{1/n} \to 1$$ ($$p > 0$$).
- 다항식의 비 $$\dfrac{a_k n^k + \cdots}{b_m n^m + \cdots}$$은 $$k < m$$이면 $$0$$, $$k = m$$이면 $$a_k/b_m$$, $$k > m$$이면 발산한다.

</div>

극한값을 미리 모르더라도 수렴을 보장하는 강력한 도구가 단조수렴이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (단조수렴)**</ins> 위로 유계인 증가수열과 아래로 유계인 감소수열은 수렴한다.

</div>

이 사실은 실수의 완비성에 기반하며, 그 증명은 [\[해석학\] §수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8)에서 다룬다. 그 대표적 응용이 자연상수의 정의이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 수열 $$a_n = \left(1 + \dfrac1n\right)^n$$은 증가하며 위로 유계임을 보일 수 있어, 명제 4에 의해 수렴한다. 그 극한을 *자연상수* $$e = 2.718\ldots$$로 정의한다. 같은 극한이 $$\sum_{k=0}^\infty \dfrac{1}{k!}$$로도 주어짐은 [§테일러 정리, ⁋예시 3](/ko/math/calculus/taylor_theorem#ex3)의 지수함수 전개에서 따른다.

</div>

수열의 극한은 무한히 많은 항을 더하는 일의 토대이다. 부분합이라는 수열의 극한으로 무한급수를 정의하는 것이 다음 글 [§무한급수](/ko/math/calculus/series)의 출발점이다.
