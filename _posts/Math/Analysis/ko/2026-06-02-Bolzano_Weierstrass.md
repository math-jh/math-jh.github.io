---
title: "부분수열과 Bolzano–Weierstrass 정리"
description: "부분수열을 정의하고, 모든 실수열이 단조 부분수열을 가짐을 보인다. 이로부터 유계수열은 수렴하는 부분수열을 가진다는 Bolzano–Weierstrass 정리를 증명하며, 이는 컴팩트성으로 이어지는 핵심 정리이다."
excerpt: "부분수열, 단조 부분수열, Bolzano–Weierstrass 정리"

categories: [Math / Analysis]
permalink: /ko/math/analysis/bolzano_weierstrass
sidebar: 
    nav: "analysis-ko"

header:
    overlay_image: /assets/images/Math/Analysis/Bolzano_Weierstrass.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 4

published: false
---

[§수열의 수렴](/ko/math/analysis/convergence_of_sequences)의 단조수렴정리는 단조수열에만 적용된다. 그러나 유계이지만 단조가 아닌 수열, 가령 $$a_n = (-1)^n$$은 수렴하지 않는다. 이런 수열에서도 "수렴하는 부분만 뽑아낼" 수 있다는 것이 Bolzano–Weierstrass 정리이며, 이것이 해석학에서 컴팩트성을 떠받치는 핵심 도구이다.

## 부분수열

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 수열 $$(a_n)$$과 자연수의 순증가 수열 $$n_1 < n_2 < n_3 < \cdots$$이 주어졌을 때, $$(a_{n_k})_{k=1}^{\infty}$$를 $$(a_n)$$의 *부분수열<sub>subsequence</sub>*이라 한다.

</div>

순증가성 때문에 항상 $$n_k \geq k$$임에 유의한다. 부분수열은 원래 수열의 극한 정보를 보존한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$a_n \to L$$이면 그 모든 부분수열도 $$L$$로 수렴한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\varepsilon > 0$$에 대해 $$n \geq N$$이면 $$\lvert a_n - L\rvert < \varepsilon$$이게 하는 $$N$$을 잡는다. $$n_k \geq k$$이므로 $$k \geq N$$이면 $$n_k \geq N$$이고 따라서 $$\lvert a_{n_k} - L\rvert < \varepsilon$$이다.

</details>

이 명제의 대우는 자주 쓰인다: 서로 다른 두 값으로 수렴하는 부분수열을 가지면 그 수열은 발산한다.

## 단조 부분수열

Bolzano–Weierstrass의 핵심은 다음의 조합론적 보조정리이다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 모든 실수열은 단조 부분수열을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

수열 $$(a_n)$$의 항 $$a_m$$이 *봉우리<sub>peak</sub>*라는 것을, 모든 $$n > m$$에 대해 $$a_n \leq a_m$$인 것으로 정의한다. 두 경우로 나눈다.

봉우리가 무한히 많으면, 그 첨자들을 $$n_1 < n_2 < \cdots$$로 나열한다. 각 $$a_{n_k}$$가 봉우리이고 $$n_{k+1} > n_k$$이므로 $$a_{n_{k+1}} \leq a_{n_k}$$이며, $$(a_{n_k})$$는 감소 부분수열이다.

봉우리가 유한개뿐이면, 마지막 봉우리 이후의 첨자 $$N$$을 잡는다. $$n_1 = N$$은 봉우리가 아니므로 $$a_{n_2} > a_{n_1}$$인 $$n_2 > n_1$$이 있고, $$n_2$$도 봉우리가 아니므로 $$a_{n_3} > a_{n_2}$$인 $$n_3 > n_2$$가 있다. 이를 반복하면 순증가 부분수열을 얻는다.

</details>

## Bolzano–Weierstrass 정리

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Bolzano–Weierstrass)**</ins> 유계인 실수열은 수렴하는 부분수열을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(a_n)$$이 유계라 하자. 보조정리 3에 의해 단조 부분수열 $$(a_{n_k})$$가 있고, 이 부분수열도 유계이다. 단조이며 유계인 수열은 단조수렴정리 ([§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8))에 의해 수렴하므로, $$(a_{n_k})$$는 수렴하는 부분수열이다.

</details>

Bolzano–Weierstrass 정리는 유계수열에서 극한을 추출하는 만능 도구로, 해석학의 존재 정리 곳곳에서 쓰인다. 그 즉각적 응용으로, 앞 글에서 예고한 [§Cauchy 수열과 완비성, ⁋정리 4](/ko/math/analysis/cauchy_sequences#thm4)의 증명이 완성된다 — Cauchy 수열은 유계이므로 수렴하는 부분수열을 가지고, 그 극한으로 전체가 수렴한다.

정리 4가 주장하는 것은 부분수열의 *존재*일 뿐, 그것이 유일하다거나 구성적으로 주어진다는 것이 아님에 유의한다. 하나의 유계수열에서 서로 다른 극한으로 가는 여러 부분수열을 동시에 뽑아낼 수 있는 경우가 흔하며, 다음 절에서 이를 구체적인 수열로 살펴본다.

## 예시와 계산

가장 단순하면서도 핵심을 보여 주는 예는 [§수열의 수렴](/ko/math/analysis/convergence_of_sequences)에서 본 발산수열 $$a_n = (-1)^n$$이다. 이 수열은 수렴하지 않지만 유계이므로 정리 4가 적용되며, 실제로 두 개의 수렴 부분수열을 곧바로 읽어낼 수 있다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$(-1)^n$$의 부분수열)**</ins> $$a_n = (-1)^n$$은 $$\lvert a_n\rvert = 1$$이므로 유계이다. 짝수 첨자만 취하면

$$a_{2k} = (-1)^{2k} = 1 \quad (k = 1, 2, 3, \dots)$$

이라는 상수 부분수열을 얻어 $$a_{2k} \to 1$$이고, 홀수 첨자만 취하면

$$a_{2k-1} = (-1)^{2k-1} = -1 \quad (k = 1, 2, 3, \dots)$$

이라는 상수 부분수열을 얻어 $$a_{2k-1} \to -1$$이다. 두 부분극한이 다르므로 명제 2의 대우에 의해 $$(a_n)$$ 자체는 발산한다.

</div>

이 예시는 정리 4의 부분수열이 일반적으로 유일하지 않음을 보여 준다. 집적점이 둘 이상일 수 있는 것이다. 다음 예시는 같은 현상을 한층 극적으로 보여 준다 — 한 유계수열이 무수히 많은 집적점을 가질 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (조밀한 집적점)**</ins> 유리수 전체를 하나의 수열 $$(q_n)$$로 늘어놓되, 그 일부를 구간 $$[0, 1]$$ 안의 유리수로 한정하여 $$(r_n)$$을 만들면 $$(r_n)$$은 $$[0, 1]$$에 들어 있으므로 유계이다. $$[0,1]$$의 임의의 실수 $$x$$와 임의의 $$\varepsilon > 0$$에 대해 구간 $$(x - \varepsilon, x + \varepsilon)$$ 안에는 유리수가 무한히 많으므로, 다음과 같이 첨자를 귀납적으로 고른다.

$$\lvert r_{n_k} - x\rvert < \frac{1}{k} \qquad (n_1 < n_2 < n_3 < \cdots).$$

그러면 $$r_{n_k} \to x$$이다. 즉 $$[0, 1]$$의 *모든* 점이 이 수열의 집적점이며, 정리 4가 보장하는 "적어도 하나"가 실제로는 연속체만큼 많을 수 있음을 보인다.

</div>

반대로, 수렴하는 수열에서는 모든 부분수열이 같은 극한을 공유하므로 집적점이 단 하나뿐이다. 일반적으로 유계수열에서 집적점이 유일하면 그 수열은 그 점으로 수렴한다. 이 사실은 정리 4의 자연스러운 동반 명제이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 유계수열 $$(a_n)$$이 단 하나의 집적점 $$L$$만을 가지면 $$a_n \to L$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

대우를 보인다. $$a_n \not\to L$$이라 하자. 그러면 어떤 $$\varepsilon_0 > 0$$이 있어, 임의로 큰 첨자에서 $$\lvert a_n - L\rvert \geq \varepsilon_0$$인 항이 나타난다. 이런 항들의 첨자를 $$n_1 < n_2 < \cdots$$로 모으면 부분수열 $$(a_{n_k})$$를 얻는데, 이 부분수열은 유계이므로 정리 4에 의해 다시 수렴하는 부분수열 $$(a_{n_{k_j}})$$를 가지며, 그 극한을 $$L'$$이라 하자. 모든 $$j$$에서

$$\begin{aligned}
\lvert L' - L\rvert
&= \lim_{j\to\infty} \lvert a_{n_{k_j}} - L\rvert \\
&\geq \varepsilon_0 > 0
\end{aligned}$$

이므로 $$L' \neq L$$이다. 즉 $$L$$과 다른 집적점 $$L'$$이 존재하여 집적점이 유일하다는 가정에 모순이다. 따라서 $$a_n \to L$$이다.

</details>

## 구간 이분법에 의한 증명

보조정리 3을 거치지 않고 정리 4를 직접 증명하는 또 하나의 표준적 방법이 *구간 이분법<sub>bisection</sub>*이다. 유계수열을 가두는 구간을 반씩 잘라 가며 항이 무한히 많은 쪽을 택하는 이 방법은 컴팩트성 증명에서 되풀이되는 기법이므로 따로 정리해 둔다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (Bolzano–Weierstrass의 이분법 증명)**</ins> 유계인 실수열은 수렴하는 부분수열을 가진다 (정리 4의 다른 증명).

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(a_n)$$이 유계라 하면 모든 항을 담는 닫힌 구간 $$I_0 = [m, M]$$이 있다. $$I_0$$을 중점에서 둘로 나누면, 적어도 한쪽 반구간은 수열의 항을 (첨자 기준) 무한히 많이 포함한다. 그쪽을 $$I_1$$이라 하고, 같은 절차를 반복하여 닫힌 구간들의 열

$$I_0 \supseteq I_1 \supseteq I_2 \supseteq \cdots, \qquad \operatorname{length}(I_j) = \frac{M - m}{2^{j}}$$

을 얻는다. 각 $$I_j$$는 무한히 많은 항을 담으므로, 다음을 만족하는 순증가 첨자열 $$n_1 < n_2 < \cdots$$을 귀납적으로 고를 수 있다.

$$a_{n_j} \in I_j \qquad (j = 1, 2, 3, \dots).$$

구간의 길이가 $$0$$으로 가므로, 구간축소정리에 의해 모든 $$I_j$$에 공통으로 들어 있는 점 $$L$$이 유일하게 존재한다. 이때 $$a_{n_j}$$와 $$L$$이 모두 $$I_j$$ 안에 있으므로

$$\begin{aligned}
\lvert a_{n_j} - L\rvert
&\leq \operatorname{length}(I_j) \\
&= \frac{M - m}{2^{j}} \;\longrightarrow\; 0
\end{aligned}$$

이고, 따라서 $$a_{n_j} \to L$$이다. 즉 $$(a_{n_j})$$가 수렴하는 부분수열이다.

</details>

두 증명은 모두 실수의 완비성을 본질적으로 사용한다. 보조정리 3을 거치는 증명은 단조수렴정리를, 이분법 증명은 구간축소정리를 쓰는데, 이 둘은 모두 상한 성질과 동치인 완비성의 표현들이다. 어느 길을 택하든 유리수 위에서는 정리가 성립하지 않는다 — 가령 $$\sqrt{2}$$로 수렴하는 유계 유리수열은 $$\mathbb{Q}$$ 안에서 수렴하는 부분수열을 갖지 못한다.

## 응용

정리 4의 위력은 극한값을 미리 알지 못한 채 존재만으로 결론을 끌어내는 데 있다. 그 전형적 사례가 앞서 본 Cauchy 판정법의 완성이며, 다음 예시는 그 논증을 한 줄기로 정리한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (Cauchy 판정법의 골격)**</ins> $$(a_n)$$이 Cauchy 수열이라 하자. Cauchy 수열은 유계이므로 정리 4에 의해 수렴하는 부분수열 $$a_{n_k} \to L$$이 존재한다. 임의의 $$\varepsilon > 0$$에 대해 Cauchy 조건으로 $$m, n \geq N$$이면 $$\lvert a_m - a_n\rvert < \varepsilon/2$$이게 $$N$$을 잡고, 부분수열의 수렴으로 $$n_k \geq N$$이면서 $$\lvert a_{n_k} - L\rvert < \varepsilon/2$$인 $$k$$를 잡으면, 모든 $$n \geq N$$에서

$$\begin{aligned}
\lvert a_n - L\rvert
&\leq \lvert a_n - a_{n_k}\rvert + \lvert a_{n_k} - L\rvert \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon
\end{aligned}$$

이므로 $$a_n \to L$$이다. 부분수열의 극한 하나가 전체 수열을 끌어당기는 것이다.

</div>

같은 발상이 연속함수 이론의 최대·최소 정리에서도 작동한다. 닫힌 유계 구간 위의 연속함수 $$f$$가 상한 $$S = \sup f$$에 임의로 가까운 값을 취하는 점들의 수열 $$(x_n)$$을 잡으면, 이 수열은 유계이므로 정리 4에 의해 수렴하는 부분수열 $$x_{n_k} \to c$$를 가진다. 구간이 닫혀 있어 극한점 $$c$$도 구간 안에 있고, $$f$$의 연속성으로 $$f(x_{n_k}) \to f(c)$$이므로 $$f(c) = S$$가 되어, 상한이 실제로 달성된다. 이처럼 "유계수열에서 극한을 추출한다"는 정리 4의 한 문장이 존재 정리의 골격을 이룬다.

수렴하는 부분수열의 극한들을 *부분수열극한* 또는 *집적점*이라 하며, 정리 4는 유계수열이 적어도 하나의 집적점을 가짐을 말한다. 이 정리는 다음 글들에서 컴팩트 집합 위의 수열이 그 집합 안에서 수렴하는 부분수열을 가진다는 [§컴팩트성](/ko/math/analysis/compactness)의 *점렬컴팩트성*으로 일반화되며, [§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 최대·최소 정리를 증명하는 열쇠가 된다.
