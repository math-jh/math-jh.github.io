---
title: "유클리드 호제법과 Bézout 항등식"
description: "나눗셈 정리를 반복 적용하여 최대공약수를 계산하는 유클리드 호제법을 정리하고, 그로부터 최대공약수를 두 수의 정수계수 선형결합으로 표현하는 Bézout 항등식을 증명한다. 최대공약수가 모든 공약수의 배수임도 보인다."
excerpt: "유클리드 호제법, Bézout 항등식, 최대공약수의 보편성"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/euclidean_algorithm
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Euclidean_Algorithm.png
    overlay_filter: 0.5

date: 2026-06-07
last_modified_at: 2026-06-07

weight: 2

published: false
---

[§나눗셈과 최대공약수](/ko/math/number_theory/divisibility)에서 최대공약수를 정의하였으나, 약수를 일일이 나열하는 계산법은 큰 수에 대해 비효율적이다. 이 글에서는 나눗셈 정리만으로 최대공약수를 빠르게 계산하는 고전 알고리즘과, 그것이 부수적으로 주는 강력한 표현 정리를 다룬다.

## 유클리드 호제법

핵심은 다음의 단순한 관찰이다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> $$a = bq + r$$이면 $$\gcd(a, b) = \gcd(b, r)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a$$와 $$b$$의 공약수와, $$b$$와 $$r$$의 공약수가 정확히 일치함을 보이면 충분하다. $$d \mid a$$이고 $$d \mid b$$이면, $$r = a - bq$$이므로 ([§나눗셈과 최대공약수, ⁋명제 2](/ko/math/number_theory/divisibility#prop2)의 선형결합 성질에 의해) $$d \mid r$$이다. 거꾸로 $$d \mid b$$이고 $$d \mid r$$이면 $$a = bq + r$$이므로 $$d \mid a$$이다. 따라서 두 쌍의 공약수 집합이 같고, 그 최댓값도 같다.

</details>

보조정리 1을 반복하면 *유클리드 호제법<sub>Euclidean algorithm</sub>*을 얻는다. $$a \geq b > 0$$에서 출발하여 나눗셈 정리를 거듭 적용한다.

$$\begin{aligned}
a &= b q_1 + r_1, & 0 \leq r_1 < b,\\
b &= r_1 q_2 + r_2, & 0 \leq r_2 < r_1,\\
r_1 &= r_2 q_3 + r_3, & 0 \leq r_3 < r_2,\\
&\;\;\vdots
\end{aligned}$$

나머지들은 $$b > r_1 > r_2 > \cdots \geq 0$$로 엄격히 감소하는 음이 아닌 정수열이므로 유한 단계 안에 $$0$$이 된다. 마지막으로 $$0$$이 아닌 나머지 $$r_k$$가 나타났다고 하자 (즉 $$r_{k+1} = 0$$). 보조정리 1을 단계마다 적용하면

$$\gcd(a,b) = \gcd(b, r_1) = \gcd(r_1, r_2) = \cdots = \gcd(r_{k-1}, r_k) = \gcd(r_k, 0) = r_k$$

이다. 즉 마지막으로 0이 아닌 나머지가 최대공약수이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$\gcd(1071, 462)$$를 호제법으로 구하자.

$$\begin{aligned}
1071 &= 462 \cdot 2 + 147,\\
462 &= 147 \cdot 3 + 21,\\
147 &= 21 \cdot 7 + 0.
\end{aligned}$$

마지막으로 $$0$$이 아닌 나머지는 $$21$$이므로 $$\gcd(1071, 462) = 21$$이다.

</div>

## Bézout 항등식

호제법의 등식들을 거꾸로 거슬러 올라가면, 최대공약수를 두 수의 정수계수 선형결합으로 표현할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Bézout 항등식)**</ins> 둘 다 $$0$$은 아닌 정수 $$a, b$$에 대하여, 다음을 만족하는 정수 $$x, y$$가 존재한다.

$$\gcd(a, b) = ax + by$$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

집합 $$S = \{ax + by \mid x, y \in \mathbb{Z}\} \cap \mathbb{Z}_{>0}$$를 생각하자. $$a \neq 0$$이면 $$\lvert a\rvert = a\cdot(\pm 1) + b\cdot 0 \in S$$이므로 $$S$$는 공집합이 아니고, 정렬성에 의해 최솟값 $$d = ax_0 + by_0 > 0$$을 갖는다 ([\[집합론\] §정렬집합의 성질들](/ko/math/set_theory/well_ordering)).

$$d \mid a$$임을 보이자. 나눗셈 정리로 $$a = dq + r$$ ($$0 \leq r < d$$) 라 하면

$$r = a - dq = a - (ax_0 + by_0)q = a(1 - x_0 q) + b(-y_0 q)$$

는 $$a, b$$의 정수계수 선형결합이다. 만약 $$r > 0$$이면 $$r \in S$$이면서 $$r < d$$이므로 $$d$$의 최소성에 모순이다. 따라서 $$r = 0$$, 즉 $$d \mid a$$이다. 같은 논증으로 $$d \mid b$$이므로 $$d$$는 공약수이다.

한편 임의의 공약수 $$c$$ ($$c \mid a$$, $$c \mid b$$) 는 선형결합 성질에 의해 $$c \mid (ax_0 + by_0) = d$$이므로 $$c \leq d$$이다. 따라서 $$d$$는 최대공약수 $$\gcd(a,b)$$이고, $$\gcd(a,b) = ax_0 + by_0$$이다.

</details>

증명 과정에서 부수적으로 매우 중요한 사실 하나가 따라온다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4 (최대공약수의 보편성)**</ins> 정수 $$a, b$$의 임의의 공약수 $$c$$는 $$\gcd(a,b)$$를 나눈다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 3의 증명에서 $$d = \gcd(a,b) = ax_0 + by_0$$이고, $$c \mid a$$, $$c \mid b$$이면 선형결합 성질로 $$c \mid d$$임을 이미 보였다.

</details>

이 따름정리는 최대공약수가 단지 "수치상 가장 큰" 공약수일 뿐 아니라, 나누어떨어짐 순서에서 모든 공약수의 위에 있는 *보편적인* 공약수임을 말한다. 이 보편성이 다음 글 [§소수와 산술의 기본정리](/ko/math/number_theory/primes)에서 유클리드 보조정리 — "소수가 곱을 나누면 인수 중 하나를 나눈다" — 를 증명하는 열쇠가 되며, 소인수분해의 유일성으로 이어진다.

Bézout 항등식의 직접적 귀결로, $$a$$와 $$b$$가 서로소인 것은 $$ax + by = 1$$인 정수 $$x, y$$가 존재하는 것과 동치이다. 이 동치는 [§합동식](/ko/math/number_theory/congruences)에서 곱셈에 대한 역원의 존재 판정으로 다시 등장한다. 또한 위 증명은 추상화하면 "$$\mathbb{Z}$$의 모든 아이디얼이 주아이디얼"이라는 사실 — 즉 $$\mathbb{Z}$$가 주아이디얼 정역 — 의 구체적 형태이며, 이는 환론에서 더 일반적으로 다루어진다.
