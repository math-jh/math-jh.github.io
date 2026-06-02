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

date: 2026-06-19
last_modified_at: 2026-06-19

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

수렴하는 부분수열의 극한들을 *부분수열극한* 또는 *집적점*이라 하며, 정리 4는 유계수열이 적어도 하나의 집적점을 가짐을 말한다. 이 정리는 다음 글들에서 컴팩트 집합 위의 수열이 그 집합 안에서 수렴하는 부분수열을 가진다는 [§컴팩트성](/ko/math/analysis/compactness)의 *점렬컴팩트성*으로 일반화되며, [§연속함수의 성질](/ko/math/analysis/continuous_functions)에서 최대·최소 정리를 증명하는 열쇠가 된다.
