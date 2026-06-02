---
title: "수열의 수렴"
description: "수열의 수렴을 ε-N 언어로 엄밀히 정의하고, 극한의 유일성·유계성·대수적 성질을 증명한다. 완비성을 수열의 언어로 옮긴 단조수렴정리를 통해 해석학의 존재 정리들이 작동하는 방식을 본다."
excerpt: "ε-N 수렴, 극한의 대수, 단조수렴정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/convergence_of_sequences
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Convergence_of_Sequences.png
    overlay_filter: 0.5

date: 2026-06-13
last_modified_at: 2026-06-13

weight: 2

published: false
---

[§실수의 완비성](/ko/math/analysis/completeness_of_reals)에서 실수를 완비순서체로 못박았다. 해석학의 모든 극한 개념은 결국 수열의 수렴으로 환원되므로, 우리는 먼저 수열의 수렴을 엄밀히 정의하고 그 기본 성질을 확립한 뒤, 완비성을 수열의 언어로 번역한다.

## 수열과 수렴

*수열<sub>sequence</sub>* $$(a_n)$$은 자연수에서 실수로 가는 함수 $$n \mapsto a_n$$이다. "$$n$$이 커질수록 $$a_n$$이 어떤 값 $$L$$에 한없이 가까워진다"는 직관을 부등식으로 옮긴다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 수열 $$(a_n)$$이 실수 $$L$$로 *수렴<sub>converges</sub>*한다는 것은, 임의의 $$\varepsilon > 0$$에 대하여 자연수 $$N$$이 존재하여 모든 $$n \geq N$$에 대해

$$\lvert a_n - L\rvert < \varepsilon$$

이 성립하는 것이다. 이때 $$L$$을 $$(a_n)$$의 *극한<sub>limit</sub>*이라 하고 $$\lim_{n\to\infty} a_n = L$$ 또는 $$a_n \to L$$로 적는다. 수렴하지 않는 수열은 *발산<sub>diverges</sub>*한다고 한다.

</div>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$a_n = 1/n$$은 $$0$$으로 수렴한다. 임의의 $$\varepsilon > 0$$에 대해, 아르키메데스 성질 ([§실수의 완비성, ⁋정리 4](/ko/math/analysis/completeness_of_reals#thm4))에 의해 $$1/N < \varepsilon$$인 $$N$$이 있고, $$n \geq N$$이면 $$\lvert 1/n - 0\rvert = 1/n \leq 1/N < \varepsilon$$이다.

</div>

## 극한의 기본 성질

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (극한의 유일성)**</ins> 수렴하는 수열의 극한은 유일하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a_n \to L$$이고 $$a_n \to L'$$이며 $$L \neq L'$$이라 하자. $$\varepsilon = \lvert L - L'\rvert/2 > 0$$으로 두면, 충분히 큰 $$n$$에 대해 $$\lvert a_n - L\rvert < \varepsilon$$이면서 $$\lvert a_n - L'\rvert < \varepsilon$$이다. 삼각부등식에 의해 $$\lvert L - L'\rvert \leq \lvert L - a_n\rvert + \lvert a_n - L'\rvert < 2\varepsilon = \lvert L - L'\rvert$$이 되어 모순이다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 수렴하는 수열은 유계이다. 즉 어떤 $$M$$에 대해 모든 $$n$$에서 $$\lvert a_n\rvert \leq M$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a_n \to L$$이면 $$\varepsilon = 1$$에 대해 $$n \geq N$$에서 $$\lvert a_n\rvert \leq \lvert L\rvert + 1$$이다. 나머지 유한개의 항 $$a_1, \ldots, a_{N-1}$$과 함께 $$M = \max\{\lvert a_1\rvert, \ldots, \lvert a_{N-1}\rvert, \lvert L\rvert + 1\}$$로 두면 모든 $$n$$에서 $$\lvert a_n\rvert \leq M$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (극한의 대수)**</ins> $$a_n \to A$$, $$b_n \to B$$이면 다음이 성립한다.

$$a_n + b_n \to A + B, \qquad a_n b_n \to AB, \qquad \frac{a_n}{b_n} \to \frac{A}{B}\ (B \neq 0).$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

합만 보인다. 임의의 $$\varepsilon > 0$$에 대해, $$n$$이 충분히 크면 $$\lvert a_n - A\rvert < \varepsilon/2$$이고 $$\lvert b_n - B\rvert < \varepsilon/2$$이다. 삼각부등식으로 $$\lvert (a_n + b_n) - (A+B)\rvert \leq \lvert a_n - A\rvert + \lvert b_n - B\rvert < \varepsilon$$이다. 곱은 $$a_n b_n - AB = a_n(b_n - B) + (a_n - A)B$$로 가르고 명제 4의 유계성을 쓰며, 몫은 $$1/b_n \to 1/B$$를 먼저 보이면 된다.

</details>

다음은 모르는 수열을 아는 두 수열 사이에 가두어 극한을 결정하는 자주 쓰이는 도구이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (조임정리)**</ins> 충분히 큰 모든 $$n$$에서 $$a_n \leq c_n \leq b_n$$이고 $$a_n \to L$$, $$b_n \to L$$이면 $$c_n \to L$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\varepsilon > 0$$에 대해 충분히 큰 $$n$$에서 $$L - \varepsilon < a_n$$이고 $$b_n < L + \varepsilon$$이다. 그러면 $$L - \varepsilon < a_n \leq c_n \leq b_n < L + \varepsilon$$이므로 $$\lvert c_n - L\rvert < \varepsilon$$이다.

</details>

## 단조수렴정리

이제 완비성을 수열의 언어로 옮긴다. 이것이 수열에서 극한의 *존재*를 보장하는 첫 도구이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 수열 $$(a_n)$$이 모든 $$n$$에서 $$a_n \leq a_{n+1}$$이면 *증가수열*, $$a_n \geq a_{n+1}$$이면 *감소수열*이라 하며, 둘을 통틀어 *단조수열<sub>monotone sequence</sub>*이라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (단조수렴정리)**</ins> 위로 유계인 증가수열은 수렴하며, 그 극한은 $$\sup\{a_n \mid n \in \mathbb{N}\}$$이다. 대칭적으로 아래로 유계인 감소수열은 하한으로 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(a_n)$$이 증가하고 위로 유계라 하자. 집합 $$\{a_n\}$$이 위로 유계이고 공집합이 아니므로, 완비성 공리 ([§실수의 완비성, ⁋정의 2](/ko/math/analysis/completeness_of_reals#def2))에 의해 $$L = \sup\{a_n\}$$이 존재한다. 임의의 $$\varepsilon > 0$$에 대해 $$L - \varepsilon$$은 상계가 아니므로 $$a_N > L - \varepsilon$$인 $$N$$이 있고, $$(a_n)$$이 증가하므로 $$n \geq N$$이면 $$L - \varepsilon < a_N \leq a_n \leq L < L + \varepsilon$$이다. 따라서 $$\lvert a_n - L\rvert < \varepsilon$$이고 $$a_n \to L$$이다.

</details>

단조수렴정리는 명시적 극한값을 모를 때에도 수렴을 보증한다. 예컨대 $$a_1 = 2$$, $$a_{n+1} = \tfrac12(a_n + 2/a_n)$$로 정의된 수열은 아래로 유계인 감소수열임을 보일 수 있어 수렴하며, 그 극한 $$L$$은 $$L = \tfrac12(L + 2/L)$$을 풀어 $$\sqrt{2}$$임이 따른다.

이 정리는 [\[미적분학\] §수열의 극한](/ko/math/calculus/sequences)에서 계산적으로 다룬 극한들의 존재를 비로소 정당화한다. 그러나 단조성을 갖지 않는 수열의 수렴을 다루려면 극한값을 미리 알 필요 없는 더 일반적인 판정이 필요하며, 그것이 다음 글 [§Cauchy 수열과 완비성](/ko/math/analysis/cauchy_sequences)의 Cauchy 판정법이다. 또한 단조수렴정리로부터 임의의 유계수열이 수렴하는 부분수열을 가진다는 [§부분수열과 Bolzano–Weierstrass 정리](/ko/math/analysis/bolzano_weierstrass)가 따라 나온다.
