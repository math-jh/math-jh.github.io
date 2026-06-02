---
title: "수열의 극한"
description: "수열의 수렴을 ε-N으로 정의하고, 유계성·극한 법칙·조임정리·비율판정을 정리한다. 표준 극한과 자연상수 e, 단조수렴정리, 점화식으로 정의된 수열의 극한, 부분수열과 Cauchy 조건을 다룬다."
excerpt: "수열의 수렴, 극한 법칙, 표준 극한과 e, 단조수렴"

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

*수열<sub>sequence</sub>* $$(a_n)$$이란 자연수에 실수를 대응시키는 함수, 즉 $$a : \mathbb{N} \to \mathbb{R}$$을 그 값들 $$a_1, a_2, a_3, \ldots$$의 나열로 본 것이다. 함수의 극한 ([§함수와 극한](/ko/math/calculus/functions_and_limits))에서 우리는 이미 $$x \to \infty$$의 거동을 다루었는데, 수열의 극한은 그 이산적 판본 — 변수가 자연수만 취하며 $$n \to \infty$$로만 가는 경우 — 이다. 이 글에서는 수열의 극한을 정면으로 다루어, 다음 글들의 무한급수와 멱급수를 위한 계산 도구를 갖춘다.

## 수열의 수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 수열 $$(a_n)$$이 실수 $$L$$로 *수렴<sub>converges</sub>*한다는 것은, 임의의 $$\varepsilon > 0$$에 대하여 자연수 $$N$$이 존재하여

$$n \geq N \implies \lvert a_n - L\rvert < \varepsilon$$

이 성립하는 것이다. 이때 $$L$$을 $$(a_n)$$의 *극한*이라 하고 $$\displaystyle\lim_{n\to\infty} a_n = L$$ 또는 $$a_n \to L$$로 적는다. 수렴하지 않는 수열은 *발산<sub>diverges</sub>*한다고 한다.

</div>

직관적으로, 어떤 오차 폭 $$\varepsilon$$을 정해도 충분히 뒤쪽의 항들(즉 $$n \geq N$$인 모든 항)이 구간 $$(L - \varepsilon, L + \varepsilon)$$ 안에 들어온다는 뜻이다. 앞쪽의 유한개 항은 극한에 아무 영향을 주지 않는다 — 극한은 오로지 수열의 "꼬리"가 결정한다. 함수극한과의 차이는 변수가 자연수뿐이고 한 방향($$+\infty$$)으로만 간다는 점이다.

가장 기본적인 예로 $$a_n = 1/n$$은 $$0$$으로 수렴한다. 임의의 $$\varepsilon > 0$$에 대해 $$N > 1/\varepsilon$$인 자연수를 잡으면 ($$\mathbb{R}$$의 아르키메데스 성질로 존재한다) $$n \geq N$$일 때 $$\lvert 1/n - 0\rvert = 1/n \leq 1/N < \varepsilon$$이다. 반면 $$a_n = (-1)^n$$은 $$1$$과 $$-1$$ 사이를 오가며 어느 값으로도 모이지 않아 발산한다. 발산에는 두 양상이 있다. $$(-1)^n$$처럼 진동하며 발산하기도 하고, $$a_n = n$$처럼 한없이 커져 발산하기도 한다. 후자는 *무한대로 발산*한다고 하며 $$a_n \to \infty$$로 적는다: 임의의 $$M$$에 대해 충분히 큰 모든 $$n$$에서 $$a_n > M$$인 경우이다.

## 극한의 성질

수렴하는 수열은 그 항들이 한 점 근처로 모이므로 전체적으로 유계이다. 이 단순한 사실이 곱의 극한 등 여러 논증에서 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 수렴하는 수열은 유계이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a_n \to L$$이면 $$\varepsilon = 1$$에 대응하는 $$N$$을 잡았을 때 $$n \geq N$$에서 $$\lvert a_n\rvert \leq \lvert L\rvert + 1$$이다. 나머지 유한개 항을 포함하여 $$M = \max\{\lvert a_1\rvert, \ldots, \lvert a_{N-1}\rvert, \lvert L\rvert + 1\}$$로 두면 모든 $$n$$에서 $$\lvert a_n\rvert \leq M$$이다.

</details>

수열의 극한도 함수의 극한과 똑같이 사칙연산 및 부등식과 어울린다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (극한 법칙)**</ins> $$a_n \to A$$, $$b_n \to B$$이면

$$a_n + b_n \to A + B, \qquad a_n b_n \to AB, \qquad \frac{a_n}{b_n} \to \frac{A}{B}\ (B \neq 0)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

합만 보인다. 임의의 $$\varepsilon > 0$$에 대해 $$\varepsilon/2$$에 대응하는 $$N_1, N_2$$를 각각 잡고 $$N = \max(N_1, N_2)$$로 두면, $$n \geq N$$일 때 $$\lvert (a_n + b_n) - (A+B)\rvert \leq \lvert a_n - A\rvert + \lvert b_n - B\rvert < \varepsilon$$이다. 곱과 몫은 명제 2의 유계성을 써서 함수극한의 경우 ([§함수와 극한, ⁋명제 3](/ko/math/calculus/functions_and_limits#prop3))와 같은 방식으로 보인다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (조임정리)**</ins> 충분히 큰 모든 $$n$$에서 $$a_n \leq c_n \leq b_n$$이고 $$a_n \to L$$, $$b_n \to L$$이면 $$c_n \to L$$이다.

</div>

조임정리는 부호가 진동하는 수열에 특히 유용하다. 예컨대 $$\bigl\lvert \tfrac{\sin n}{n}\bigr\rvert \leq \tfrac1n \to 0$$이므로 $$\tfrac{\sin n}{n} \to 0$$이다. 또 다음의 비율 판정은 지수적으로 줄어드는 수열의 수렴을 즉시 준다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (비율 판정)**</ins> $$a_n > 0$$이고 $$\dfrac{a_{n+1}}{a_n} \to L < 1$$이면 $$a_n \to 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L < r < 1$$인 $$r$$를 고르면, 충분히 큰 $$n \geq N$$에서 $$\dfrac{a_{n+1}}{a_n} < r$$이므로 $$a_{N+k} < r^k a_N$$이다. $$0 < r < 1$$이라 $$r^k \to 0$$이고, 조임정리로 $$a_n \to 0$$이다.

</details>

## 표준 극한

계산에서 거듭 쓰이는 기본 극한들을 모은다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 다음이 성립한다.

1. $$\lvert r\rvert < 1$$이면 $$r^n \to 0$$, $$r = 1$$이면 $$\to 1$$, $$\lvert r\rvert > 1$$이면 발산한다.
2. $$p > 0$$에 대해 $$\dfrac{1}{n^p} \to 0$$, 그리고 $$n^{1/n} \to 1$$, $$p^{1/n} \to 1$$ ($$p > 0$$).
3. 다항식의 비는 최고차항이 지배하여 $$\dfrac{a_k n^k + \cdots}{b_m n^m + \cdots}$$이 $$k < m$$이면 $$0$$, $$k = m$$이면 $$a_k/b_m$$, $$k > m$$이면 발산한다.
4. 지수는 거듭제곱을, 계승은 지수를 압도한다: $$r > 1$$, $$p > 0$$에 대해 $$\dfrac{n^p}{r^n} \to 0$$이고 $$\dfrac{r^n}{n!} \to 0$$이다.

</div>

이들 대부분은 명제 5나 조임정리로 얻는다. 가령 4의 $$\dfrac{r^n}{n!}$$은 비가 $$\dfrac{r}{n+1} \to 0 < 1$$이므로 명제 5로 $$0$$이고, $$\dfrac{n^p}{r^n}$$도 비가 $$\dfrac{(n+1)^p}{n^p}\cdot\dfrac1r \to \dfrac1r < 1$$이라 $$0$$이다. 한편 2의 $$n^{1/n} \to 1$$은 $$n^{1/n} = 1 + h_n$$으로 두면 이항정리로 $$n = (1+h_n)^n \geq \binom n2 h_n^2$$, 곧 $$h_n^2 \leq \dfrac{2}{n-1} \to 0$$이므로 $$h_n \to 0$$임에서 따른다.

## 단조수렴정리

극한값을 미리 모르더라도 수렴을 보장하는 강력한 도구가 단조수렴이다. 이것이 수열에서 극한의 *존재*를 끌어내는 첫 수단이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (단조수렴)**</ins> 위로 유계인 증가수열과 아래로 유계인 감소수열은 수렴한다. (증가수열의 극한은 그 항들의 상한이다.)

</div>

이 사실은 실수의 완비성 — 위로 유계인 집합이 상한을 갖는다는 성질 — 에 정확히 기반하며, 그 증명은 [\[해석학\] §수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8)에서 다룬다. 단조수렴정리의 가장 유명한 응용이 자연상수의 정의이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (자연상수 $$e$$)**</ins> 수열 $$a_n = \left(1 + \dfrac1n\right)^n$$은 증가하며 위로 유계임을 이항정리로 보일 수 있어, 명제 7에 의해 수렴한다. 그 극한을 *자연상수* $$e = 2.718\ldots$$로 정의한다. 같은 극한이 $$\sum_{k=0}^\infty \dfrac{1}{k!}$$로도 주어짐은 [§테일러 정리, ⁋예시 3](/ko/math/calculus/taylor_theorem#ex3)의 지수함수 전개에서 따른다.

</div>

단조수렴정리는 점화식으로 정의된 수열에도 위력을 발휘한다. 극한의 값을 모른 채 수렴을 먼저 확보한 뒤, 점화식의 양변에 극한을 취해 값을 구하는 것이 표준 전략이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$a_1 = 2$$, $$a_{n+1} = \dfrac12\left(a_n + \dfrac{2}{a_n}\right)$$로 정의된 수열을 보자. 산술·기하 평균 부등식으로 모든 $$n$$에서 $$a_n \geq \sqrt 2$$이고, 이로부터 $$a_{n+1} - a_n = \dfrac{1}{2a_n}(2 - a_n^2) \leq 0$$이라 감소수열이다. 아래로 유계인 감소수열이므로 명제 7에 의해 극한 $$L$$이 존재하고, 점화식의 양변에 극한을 취하면 $$L = \dfrac12(L + 2/L)$$, 곧 $$L^2 = 2$$이다. $$L \geq \sqrt2 > 0$$이므로 $$L = \sqrt 2$$이다. 이것이 제곱근을 구하는 뉴턴 방법으로, 수렴이 매우 빨라 몇 단계면 소수점 여러 자리가 맞는다.

</div>

예시 9의 점화식은 초깃값을 바꾸어도 극한이 같다. $$a_1 > 0$$이기만 하면 같은 논증이 그대로 적용되어 $$a_n \to \sqrt 2$$이다. 일반적으로 양수 $$c$$에 대해 $$a_{n+1} = \dfrac12\bigl(a_n + \dfrac{c}{a_n}\bigr)$$은 $$\sqrt c$$로 수렴하며, 점화식으로 정의된 수열의 극한을 다루는 표준 전략 — 단조성과 유계성으로 수렴을 먼저 확보하고 양변에 극한을 취하는 것 — 의 전형적인 예이다.

## 부분수열

수렴 여부를 분석할 때, 수열의 일부 항만 골라 뽑은 새 수열을 보는 것이 유용하다. 발산을 보일 때 특히 그러한데, 서로 다른 극한으로 가는 두 부분수열을 찾으면 원래 수열이 발산함이 곧장 따라 나온다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 수열 $$(a_n)$$과 자연수의 순증가 수열 $$n_1 < n_2 < n_3 < \cdots$$이 주어졌을 때, 새 수열 $$(a_{n_k})_{k\geq 1}$$을 $$(a_n)$$의 *부분수열<sub>subsequence</sub>*이라 한다.

</div>

지표열이 순증가하므로 $$n_k \geq k$$가 항상 성립한다. 부분수열은 원래 수열에서 "건너뛰며" 항을 고르는 것이며, 수렴하는 수열에서 어떻게 골라도 같은 극한을 얻는다는 것이 다음 명제이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$a_n \to L$$이면 모든 부분수열 $$(a_{n_k})$$도 $$L$$로 수렴한다. 역으로, 어떤 두 부분수열이 서로 다른 극한으로 수렴하면 $$(a_n)$$은 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\varepsilon > 0$$에 대해 $$n \geq N$$이면 $$\lvert a_n - L\rvert < \varepsilon$$인 $$N$$을 잡자. 지표열이 순증가하므로 $$n_k \geq k$$이고, 따라서 $$k \geq N$$이면 $$n_k \geq N$$이라

$$\lvert a_{n_k} - L\rvert < \varepsilon$$

이다. 즉 $$a_{n_k} \to L$$이다. 역방향은 대우로 따른다. 만약 $$(a_n)$$이 어떤 $$L$$로 수렴한다면 방금 보인 대로 모든 부분수열이 같은 $$L$$로 수렴해야 하므로, 서로 다른 두 극한을 갖는 부분수열이 존재한다는 것은 $$(a_n)$$이 수렴하지 않음을 뜻한다.

</details>

이 판정은 진동하는 수열의 발산을 즉시 준다. 가령 $$a_n = (-1)^n$$은 짝수 지표 부분수열 $$a_{2k} = 1 \to 1$$과 홀수 지표 부분수열 $$a_{2k-1} = -1 \to -1$$이 다른 극한을 가지므로 명제 11에 의해 발산한다. 같은 방식으로 $$a_n = \cos(n\pi/2)$$ 같은 주기적 진동도 발산함을 본다.

## 예시와 계산

지금까지 정리한 도구 — 극한 법칙, 조임정리, 표준 극한, 단조수렴 — 를 결합해 구체적인 극한을 계산하자. 핵심은 식을 지배하는 항을 가려내어 알려진 표준 극한으로 환원하는 것이다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (유리식의 극한)**</ins> $$a_n = \dfrac{3n^2 - n + 5}{2n^2 + 7n}$$의 극한을 구하자. 분자·분모를 최고차 $$n^2$$으로 나누면

$$a_n = \frac{3 - \dfrac{1}{n} + \dfrac{5}{n^2}}{2 + \dfrac{7}{n}}$$

이고, $$1/n \to 0$$, $$1/n^2 \to 0$$이므로 극한 법칙 (명제 3) 에 의해 분자는 $$3$$으로, 분모는 $$2$$로 수렴한다. 분모의 극한이 $$0$$이 아니므로

$$\lim_{n\to\infty} a_n = \frac{3}{2}$$

이다. 이는 예시 6의 3에서 분자·분모의 차수가 같으면 극한이 최고차항 계수의 비라는 사실과 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (근호의 차)**</ins> $$a_n = \sqrt{n^2 + n} - n$$의 극한을 구하자. 그대로는 $$\infty - \infty$$ 꼴이므로 켤레를 곱해 정리한다.

$$\begin{aligned}
a_n &= \bigl(\sqrt{n^2 + n} - n\bigr)\cdot \frac{\sqrt{n^2+n} + n}{\sqrt{n^2+n} + n} \\
&= \frac{(n^2 + n) - n^2}{\sqrt{n^2 + n} + n} \\
&= \frac{n}{\sqrt{n^2 + n} + n} \\
&= \frac{1}{\sqrt{1 + \tfrac1n} + 1}
\end{aligned}$$

마지막 줄에서 분자·분모를 $$n$$으로 나누었다. $$1/n \to 0$$이므로 분모는 $$\sqrt{1} + 1 = 2$$로 수렴하고, 따라서

$$\lim_{n\to\infty} \bigl(\sqrt{n^2 + n} - n\bigr) = \frac12$$

이다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14 (조임정리의 활용)**</ins> $$a_n = \dfrac{n!}{n^n}$$의 극한을 구하자. 모든 항이 양수이고

$$0 < \frac{n!}{n^n} = \frac{1}{n}\cdot\frac{2}{n}\cdot\frac{3}{n}\cdots\frac{n}{n} \leq \frac{1}{n}\cdot 1 \cdot 1 \cdots 1 = \frac1n$$

이다. 둘째 인수부터 마지막 인수까지는 모두 $$1$$ 이하이고 첫 인수가 $$1/n$$이기 때문이다. $$1/n \to 0$$이므로 조임정리 (명제 4) 에 의해

$$\lim_{n\to\infty} \frac{n!}{n^n} = 0$$

이다. 같은 결론을 비율 판정으로도 얻는다. 비가 $$\dfrac{a_{n+1}}{a_n} = \dfrac{(n+1)!}{(n+1)^{n+1}}\cdot\dfrac{n^n}{n!} = \Bigl(\dfrac{n}{n+1}\Bigr)^n = \Bigl(1 + \tfrac1n\Bigr)^{-n} \to e^{-1} < 1$$이기 때문이다.

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15 ($$n$$제곱근의 극한)**</ins> $$a_n = \sqrt[n]{2^n + 3^n}$$의 극한을 구하자. 두 항 중 큰 쪽인 $$3^n$$을 묶어내면

$$a_n = \sqrt[n]{3^n\Bigl(1 + \bigl(\tfrac23\bigr)^n\Bigr)} = 3\cdot\Bigl(1 + \bigl(\tfrac23\bigr)^n\Bigr)^{1/n}$$

이다. $$(2/3)^n \to 0$$이므로 괄호 안은 $$1$$로 수렴하고, $$1 \leq \bigl(1 + (2/3)^n\bigr)^{1/n} \leq \bigl(1 + (2/3)^n\bigr) \to 1$$이라 조임정리로 그 $$n$$제곱근도 $$1$$로 간다. 따라서

$$\lim_{n\to\infty} \sqrt[n]{2^n + 3^n} = 3$$

이다. 일반적으로 $$\sqrt[n]{c_1^n + \cdots + c_m^n} \to \max\{c_1, \ldots, c_m\}$$이며, 같은 묶어내기로 확인된다.

</div>

## Cauchy 조건

지금까지의 수렴 판정은 극한값 $$L$$을 알거나 단조성을 확인할 수 있어야 했다. 그러나 극한값을 전혀 언급하지 않고, 오직 항들이 서로 가까워진다는 내적 조건만으로 수렴을 판정할 수 있다.

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> 수열 $$(a_n)$$이 *Cauchy 수열<sub>Cauchy sequence</sub>*이라는 것은, 임의의 $$\varepsilon > 0$$에 대해 자연수 $$N$$이 존재하여

$$m, n \geq N \implies \lvert a_m - a_n\rvert < \varepsilon$$

이 성립하는 것이다.

</div>

수렴의 정의가 항을 고정된 $$L$$과 비교하는 데 비해, Cauchy 조건은 항들끼리 비교한다. 수렴하는 수열은 항상 Cauchy임을 쉽게 본다.

<div class="proposition" markdown="1">

<ins id="prop17">**명제 17**</ins> 수렴하는 수열은 Cauchy 수열이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a_n \to L$$이라 하자. 임의의 $$\varepsilon > 0$$에 대해 $$\varepsilon/2$$에 대응하는 $$N$$을 잡으면, $$m, n \geq N$$일 때 삼각부등식으로

$$\begin{aligned}
\lvert a_m - a_n\rvert &= \lvert (a_m - L) - (a_n - L)\rvert \\
&\leq \lvert a_m - L\rvert + \lvert a_n - L\rvert \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon
\end{aligned}$$

이다. 따라서 $$(a_n)$$은 Cauchy 수열이다.

</details>

실수에서는 그 역도 참이다. 즉 모든 Cauchy 수열이 수렴하는데, 이를 실수의 *완비성<sub>completeness</sub>*이라 한다. 이는 명제 7의 단조수렴정리와 동치인 실수의 깊은 성질로, 그 증명은 [\[해석학\] §수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8)에서 다룬다. Cauchy 조건의 실용적 가치는, 극한값을 모르고도 수렴을 판정하게 해 준다는 데 있다 — 무한급수의 수렴 판정에서 부분합 수열에 이 조건을 적용하는 것이 대표적이다. 한편 단조가 아닌 유계수열에서도 수렴하는 부분수열을 항상 뽑을 수 있다는 것이 해석학의 Bolzano–Weierstrass 정리이며, 이들 엄밀한 이론도 [\[해석학\] §수열의 수렴](/ko/math/analysis/convergence_of_sequences)과 이어지는 글들에서 다룬다.

당장 우리에게 필요한 것은, 수열의 극한이 무한히 많은 항을 더하는 일의 토대라는 점이다. 부분합이라는 수열의 극한으로 무한급수를 정의하는 것이 다음 글 [§무한급수](/ko/math/calculus/series)의 출발점이다.
