---
title: "소수의 무한성과 분포"
description: "소수가 무한히 많다는 유클리드의 정리를 증명하고, 임의로 긴 합성수 구간이 존재함을 보인다. 에라토스테네스의 체와 함께, 소수 정리·베르트랑 가설 등 소수의 분포에 관한 깊은 결과들을 개관한다."
excerpt: "소수의 무한성, 소수 사이의 간격, 소수 정리"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/distribution_of_primes
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Distribution_of_Primes.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 4

published: false
---

[§소수와 산술의 기본정리](/ko/math/number_theory/primes)에서 소수가 정수의 곱셈적 구성 요소임을 보았다. 그렇다면 소수는 몇 개나 있으며, 자연수 안에 어떻게 흩어져 있는가? 이 글에서는 소수가 무한히 많다는 고전적 사실에서 출발하여, 소수의 분포라는 정수론의 깊은 주제를 개관한다.

## 소수의 무한성

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (유클리드)**</ins> 소수는 무한히 많다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

소수가 유한개 $$p_1, p_2, \ldots, p_k$$뿐이라 가정하고 모순을 이끈다. 정수

$$N = p_1 p_2 \cdots p_k + 1$$

을 생각하자. $$N > 1$$이므로 산술의 기본정리 ([§소수와 산술의 기본정리, ⁋정리 3](/ko/math/number_theory/primes#thm3))에 의해 $$N$$은 어떤 소수 $$p$$로 나누어떨어지고, 가정에 의해 $$p$$는 $$p_1, \ldots, p_k$$ 중 하나이다. 그러면 $$p \mid N$$이고 $$p \mid p_1\cdots p_k$$이므로 선형결합 성질 ([§나눗셈과 최대공약수, ⁋명제 2](/ko/math/number_theory/divisibility#prop2))에 의해 $$p \mid (N - p_1\cdots p_k) = 1$$이 되어, 소수가 $$1$$을 나눈다는 모순이 생긴다. 따라서 소수는 유한할 수 없다.

</details>

## 소수 사이의 간격

소수는 무한히 많지만, 군데군데 아무리 길게도 끊긴다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 자연수 $$k$$에 대하여, 연속한 $$k$$개의 합성수가 존재한다. 즉 소수를 전혀 포함하지 않는 길이 $$k$$의 구간이 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$(k+1)! = 1\cdot 2\cdots (k+1)$$을 생각하면, $$2 \leq j \leq k+1$$인 각 $$j$$에 대해 $$j \mid (k+1)!$$이고 또 $$j \mid j$$이므로 $$j \mid \bigl((k+1)! + j\bigr)$$이다. 따라서

$$(k+1)! + 2,\ (k+1)! + 3,\ \ldots,\ (k+1)! + (k+1)$$

은 각각 $$2, 3, \ldots, k+1$$을 약수로 가지는 합성수이며, 이는 연속한 $$k$$개의 합성수이다.

</details>

이처럼 소수는 한없이 성기게 흩어지는 구간을 가지면서도 결코 고갈되지 않는다. 주어진 한계 이하의 소수를 실제로 가려내는 가장 오래된 방법은 *에라토스테네스의 체<sub>sieve of Eratosthenes</sub>*로, $$2$$부터 차례로 각 소수의 배수를 지워 나가면 남는 수가 소수이다.

## 소수의 분포

소수가 "평균적으로" 얼마나 촘촘한가라는 물음은 정수론의 가장 깊은 주제로 이어진다. $$x$$ 이하의 소수의 개수를 $$\pi(x)$$로 적는다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3 (소수 정리)**</ins> 소수의 밀도에 관한 두 이정표를 증명 없이 적는다.

- *베르트랑 가설*: 모든 $$n \geq 1$$에 대해 $$n < p \leq 2n$$인 소수 $$p$$가 존재한다 (체비쇼프가 증명).
- *소수 정리<sub>prime number theorem</sub>*: $$x \to \infty$$일 때 $$\pi(x) \sim \dfrac{x}{\ln x}$$, 즉 $$\dfrac{\pi(x)\ln x}{x} \to 1$$이다 (아다마르와 드 라 발레푸생이 1896년에 독립적으로 증명).

</div>

소수 정리는 복소해석학적 도구 — 특히 리만 제타 함수 $$\zeta(s) = \sum_{n\geq 1} n^{-s}$$의 영점 분포 — 를 통해 증명되며, 이는 정수론과 해석학이 만나는 *해석적 정수론*의 출발점이다. 한편 오일러는 더 기초적인 사실로 소수의 역수의 합 $$\sum_p \tfrac1p$$이 발산함을 보였는데, 이는 소수가 (제곱수처럼) 너무 성기지는 않음을 정량적으로 말해 주며 유클리드 정리의 강화로 볼 수 있다.

이처럼 소수의 곱셈적 구조를 함수의 언어로 다루는 관점은 다음 글 [§산술적 함수와 뫼비우스 반전](/ko/math/number_theory/arithmetic_functions)에서 약수의 개수·합과 같은 곱셈적 함수로 구체화된다. 소수의 분포를 떠받치는 무한급수와 극한의 엄밀한 이론은 해석학 [\[해석학\] §무한급수](/ko/math/analysis/series)에서 다룬다.
