---
title: "중국인의 나머지 정리"
description: "쌍마다 서로소인 법들에 대한 합동식의 연립이 유일한 해를 가진다는 중국인의 나머지 정리를 증명하고, 해를 구성하는 방법을 제시한다. 이를 환의 직접곱 분해로 재해석한다."
excerpt: "연립 합동식, 중국인의 나머지 정리, 환 동형"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/chinese_remainder_theorem
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Chinese_Remainder_Theorem.png
    overlay_filter: 0.5

date: 2026-06-22
last_modified_at: 2026-06-22

weight: 7

published: false
---

[§일차 합동식](/ko/math/number_theory/linear_congruences)은 하나의 법에 대한 방정식을 다루었다. 이제 서로 다른 여러 법에 대한 조건을 동시에 부과한다. 법들이 쌍마다 서로소이면 이러한 연립은 언제나 유일한 해를 가진다는 것이 중국인의 나머지 정리로, 정수론과 대수학 전반에서 "법별로 따로 풀어 합치는" 분해 원리의 출발점이다.

## 두 법에 대한 정리

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (중국인의 나머지 정리)**</ins> $$\gcd(m, n) = 1$$이면, 임의의 정수 $$a, b$$에 대하여 연립 합동식

$$x \equiv a \pmod m, \qquad x \equiv b \pmod n$$

은 법 $$mn$$에 대해 유일한 해를 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

*존재성.* $$\gcd(m, n) = 1$$이므로 Bézout 항등식 ([§유클리드 호제법과 Bézout 항등식, ⁋정리 3](/ko/math/number_theory/euclidean_algorithm#thm3))으로 $$mu + nv = 1$$인 정수 $$u, v$$가 있다. $$x_0 = a\,nv + b\,mu$$로 두면, $$nv = 1 - mu \equiv 1 \pmod m$$이므로 $$x_0 \equiv a\cdot 1 + 0 = a \pmod m$$이고, 대칭적으로 $$mu \equiv 1 \pmod n$$이므로 $$x_0 \equiv b \pmod n$$이다. 따라서 $$x_0$$이 해이다.

*유일성.* $$x_0, x_1$$이 모두 해이면 $$x_0 - x_1$$이 $$m$$과 $$n$$ 모두로 나누어떨어진다. $$\gcd(m, n) = 1$$이므로 $$mn \mid (x_0 - x_1)$$이고 (서로소인 두 수로 나누어떨어지면 그 곱으로도 나누어떨어진다 — 산술의 기본정리 또는 Euclid 보조정리로 얻는다), 따라서 $$x_0 \equiv x_1 \pmod{mn}$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$x \equiv 2 \pmod 3$$이고 $$x \equiv 3 \pmod 5$$인 $$x$$를 구하자. $$3, 5$$가 서로소이므로 법 $$15$$에 대한 유일한 해가 있다. $$x = 3k + 2$$를 둘째 식에 넣으면 $$3k + 2 \equiv 3 \pmod 5$$, 즉 $$3k \equiv 1 \pmod 5$$이고 $$3^{-1} \equiv 2 \pmod 5$$이므로 $$k \equiv 2 \pmod 5$$이다. 따라서 $$x = 3(5j + 2) + 2 = 15j + 8$$, 즉 $$x \equiv 8 \pmod{15}$$이다.

</div>

## 일반화와 환 동형

귀납법으로 정리 1은 여러 법으로 확장된다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $$m_1, m_2, \ldots, m_r$$이 쌍마다 서로소이면, 임의의 $$a_1, \ldots, a_r$$에 대하여 연립 $$x \equiv a_i \pmod{m_i}$$ ($$i = 1, \ldots, r$$) 은 법 $$M = m_1 m_2 \cdots m_r$$에 대해 유일한 해를 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$r$$에 대한 귀납법으로 보인다. $$r = 1$$은 자명하다. 앞의 $$r-1$$개를 합쳐 법 $$m_1\cdots m_{r-1}$$에 대한 하나의 합동식으로 만들면, 이 법은 $$m_r$$과 서로소이므로 ($$m_r$$이 각 $$m_i$$와 서로소이면 그 곱과도 서로소) 정리 1을 적용하여 법 $$M$$에 대한 유일한 해를 얻는다.

</details>

따름정리 3은 구조적으로 환의 직접곱 분해로 읽힌다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> $$m_1, \ldots, m_r$$이 쌍마다 서로소이고 $$M = \prod m_i$$이면, 잉여류를 각 법의 나머지로 보내는 사상

$$\mathbb{Z}/M\mathbb{Z} \;\xrightarrow{\;\sim\;}\; \mathbb{Z}/m_1\mathbb{Z} \times \cdots \times \mathbb{Z}/m_r\mathbb{Z}, \qquad [x] \mapsto ([x]_{m_1}, \ldots, [x]_{m_r})$$

는 환의 동형이다. 따름정리 3은 이 사상이 전단사임을 말하며, 사칙연산과의 호환은 합동의 연산 성질 ([§합동식, ⁋명제 3](/ko/math/number_theory/congruences#prop3))에서 따른다.

</div>

이 분해는 법 $$M$$에 대한 계산을 서로소인 소수 거듭제곱 법들로 쪼개어 처리하게 해 준다. 그 직접적 귀결로 오일러 $$\varphi$$ 함수의 곱셈성이 따르며, 이는 다음 글들 [§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)와 [§산술적 함수와 뫼비우스 반전](/ko/math/number_theory/arithmetic_functions)에서 곱셈적 함수의 일반론으로 발전한다.
