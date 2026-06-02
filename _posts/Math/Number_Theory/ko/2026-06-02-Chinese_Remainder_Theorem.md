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

date: 2026-06-02
last_modified_at: 2026-06-02
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

## 명시적 공식과 계산

정리 1과 따름정리 3은 해의 존재와 유일성을 보장하지만, 실제 계산에서는 해를 구체적으로 적어 주는 공식이 필요하다. 두 법의 경우 증명에서 이미 $$x_0 = a\,nv + b\,mu$$라는 표현을 얻었는데, 이를 여러 법으로 곧장 일반화한 것이 다음의 구성적 공식이다. 핵심 착상은 "$$i$$번째 조건만 살리고 나머지는 죽이는" 기저 원소들을 만드는 데 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (해의 구성 공식)**</ins> $$m_1, \ldots, m_r$$이 쌍마다 서로소이고 $$M = m_1 \cdots m_r$$이라 하자. 각 $$i$$에 대하여 $$M_i = M / m_i$$로 두면 $$\gcd(M_i, m_i) = 1$$이므로 $$M_i N_i \equiv 1 \pmod{m_i}$$인 $$N_i$$가 존재한다. 이때 연립 $$x \equiv a_i \pmod{m_i}$$의 해는

$$x \equiv \sum_{i=1}^{r} a_i M_i N_i \pmod{M}$$

으로 주어진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\gcd(M_i, m_i) = 1$$임을 본다. $$M_i = \prod_{j \neq i} m_j$$는 $$m_i$$와 서로소인 인수들의 곱이고, 쌍마다 서로소인 수들의 곱은 다시 $$m_i$$와 서로소이므로 ([§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)의 결과로 얻는다) $$\gcd(M_i, m_i) = 1$$이다. 따라서 곱셈 역원 $$N_i \equiv M_i^{-1} \pmod{m_i}$$가 존재한다. 이제 $$x = \sum_{k} a_k M_k N_k$$를 고정된 법 $$m_i$$로 환원하자. $$j \neq i$$이면 $$m_i \mid M_j$$이므로 $$M_j N_j \equiv 0 \pmod{m_i}$$이고, $$k = i$$인 항만 살아남아

$$\begin{aligned}
x &= \sum_{k=1}^{r} a_k M_k N_k \\
&\equiv a_i M_i N_i \pmod{m_i} \\
&\equiv a_i \cdot 1 \pmod{m_i} \\
&= a_i
\end{aligned}$$

이 된다. 이것이 모든 $$i$$에 대해 성립하므로 $$x$$는 연립의 해이고, 따름정리 3의 유일성에 의해 법 $$M$$에 대해 이 해가 유일하다.

</details>

명제 5의 표현은 라그랑주 보간과 같은 꼴이다. $$M_i N_i$$는 법 $$m_i$$에서는 $$1$$, 다른 모든 법에서는 $$0$$이 되는 멱등 비슷한 원소이고, 해는 그러한 기저의 $$a_i$$-가중합이다. 같은 법 $$m_1, \ldots, m_r$$로 여러 연립을 풀 때에는 $$M_i N_i$$를 한 번만 계산해 두면 우변 $$(a_1, \ldots, a_r)$$이 바뀌어도 곧바로 재사용할 수 있다는 실용적 장점이 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (공식으로 세 법 풀기)**</ins> 연립

$$x \equiv 2 \pmod 3, \qquad x \equiv 3 \pmod 5, \qquad x \equiv 2 \pmod 7$$

을 명제 5의 공식으로 풀자. $$M = 3\cdot 5\cdot 7 = 105$$이고 $$M_1 = 35$$, $$M_2 = 21$$, $$M_3 = 15$$이다. 각 역원을 구하면

$$\begin{aligned}
N_1 &\equiv 35^{-1} \equiv 2^{-1} \equiv 2 \pmod 3, \\
N_2 &\equiv 21^{-1} \equiv 1^{-1} \equiv 1 \pmod 5, \\
N_3 &\equiv 15^{-1} \equiv 1^{-1} \equiv 1 \pmod 7
\end{aligned}$$

이다. 따라서

$$\begin{aligned}
x &\equiv a_1 M_1 N_1 + a_2 M_2 N_2 + a_3 M_3 N_3 \\
&= 2\cdot 35\cdot 2 + 3\cdot 21\cdot 1 + 2\cdot 15\cdot 1 \\
&= 140 + 63 + 30 = 233 \\
&\equiv 233 - 2\cdot 105 = 23 \pmod{105}
\end{aligned}$$

이다. 검산하면 $$23 = 3\cdot 7 + 2 \equiv 2 \pmod 3$$, $$23 = 5\cdot 4 + 3 \equiv 3 \pmod 5$$, $$23 = 7\cdot 3 + 2 \equiv 2 \pmod 7$$로 세 조건을 모두 만족한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (연쇄 대입법)**</ins> 같은 연립을 예시 2의 방식, 즉 한 식씩 대입하며 푸는 방법으로도 풀 수 있다. 먼저 $$x \equiv 2 \pmod 3$$에서 $$x = 3s + 2$$로 쓰고 둘째 식에 넣으면

$$3s + 2 \equiv 3 \pmod 5 \;\Longrightarrow\; 3s \equiv 1 \pmod 5 \;\Longrightarrow\; s \equiv 2 \pmod 5$$

이다 ($$3^{-1} \equiv 2 \pmod 5$$). 그러므로 $$s = 5t + 2$$, 곧 $$x = 3(5t + 2) + 2 = 15t + 8$$이다. 이를 셋째 식에 대입하면

$$15t + 8 \equiv 2 \pmod 7 \;\Longrightarrow\; t + 1 \equiv 2 \pmod 7 \;\Longrightarrow\; t \equiv 1 \pmod 7$$

이므로 $$t = 7u + 1$$, 따라서 $$x = 15(7u + 1) + 8 = 105u + 23$$이다. 결국 $$x \equiv 23 \pmod{105}$$로 예시 6과 같은 답을 얻는다. 연쇄 대입법은 큰 역원을 미리 모두 구할 필요가 없어 손으로 풀 때 흔히 더 빠르다.

</div>

## 일반화: 서로소가 아닌 법

법들이 서로소가 아니면 연립이 해를 갖지 않을 수도 있다. 가령 $$x \equiv 1 \pmod 2$$와 $$x \equiv 0 \pmod 4$$는 동시에 만족될 수 없는데, 둘째 조건은 $$x$$가 짝수임을 강제하지만 첫째 조건은 홀수임을 요구하기 때문이다. 해가 있으려면 겹치는 법에서 두 조건이 서로 모순되지 않아야 하며, 그 정확한 양립 조건을 다음 명제가 기술한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (일반 양립 조건)**</ins> 임의의 양의 정수 $$m, n$$과 정수 $$a, b$$에 대하여, 연립

$$x \equiv a \pmod m, \qquad x \equiv b \pmod n$$

은 $$\gcd(m, n) \mid (a - b)$$일 때에만 해를 가지며, 해가 있을 경우 법 $$\operatorname{lcm}(m, n)$$에 대해 유일하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$d = \gcd(m, n)$$으로 두자. $$x$$가 해이면 $$x - a$$가 $$m$$의 배수, 따라서 $$d$$의 배수이고, $$x - b$$도 $$d$$의 배수이므로 그 차 $$(x - a) - (x - b) = b - a$$가 $$d$$로 나누어떨어진다. 즉 $$d \mid (a - b)$$가 필요조건이다.

역으로 $$d \mid (a - b)$$라 하자. 첫 식에서 $$x = a + m t$$로 쓰고 둘째 식에 넣으면 $$a + mt \equiv b \pmod n$$, 곧 $$mt \equiv b - a \pmod n$$이다. 이 $$t$$에 관한 일차 합동식은 $$\gcd(m, n) = d$$가 우변 $$b - a$$를 나누므로 ([§일차 합동식, ⁋정리 1](/ko/math/number_theory/linear_congruences#thm1)) 해를 가진다. 그러한 $$t$$를 하나 잡으면 $$x = a + mt$$가 연립의 해이다.

유일성은 다음과 같다. $$x_0, x_1$$이 모두 해이면 $$x_0 - x_1$$이 $$m$$과 $$n$$의 공배수, 즉 $$\operatorname{lcm}(m, n)$$의 배수이므로 $$x_0 \equiv x_1 \pmod{\operatorname{lcm}(m, n)}$$이다. $$\gcd(m, n) = 1$$인 특수한 경우에는 $$d = 1$$이 항상 $$a - b$$를 나누고 $$\operatorname{lcm}(m, n) = mn$$이 되어 정리 1로 환원된다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (양립하는 경우와 모순되는 경우)**</ins> 먼저 $$x \equiv 5 \pmod 6$$이고 $$x \equiv 11 \pmod 8$$인 경우를 보자. $$\gcd(6, 8) = 2$$이고 $$a - b = 5 - 11 = -6$$이 $$2$$로 나누어떨어지므로 명제 8에 의해 해가 있다. $$x = 6t + 5$$를 둘째 식에 넣으면

$$6t + 5 \equiv 11 \pmod 8 \;\Longrightarrow\; 6t \equiv 6 \pmod 8 \;\Longrightarrow\; 3t \equiv 3 \pmod 4 \;\Longrightarrow\; t \equiv 1 \pmod 4$$

이므로 $$t = 4u + 1$$, 곧 $$x = 6(4u + 1) + 5 = 24u + 11$$이다. 즉 $$x \equiv 11 \pmod{24}$$이고, 여기서 $$24 = \operatorname{lcm}(6, 8)$$이다. 반면 $$x \equiv 3 \pmod 6$$이고 $$x \equiv 0 \pmod 8$$이면 $$\gcd(6, 8) = 2$$인데 $$a - b = 3$$이 $$2$$로 나누어떨어지지 않으므로 해가 없다.

</div>

## 응용: 법별 분해

중국인의 나머지 정리의 실용적 가치는 큰 합성수 법에 대한 계산을 서로소인 소수 거듭제곱 법으로 쪼개어 각각 작은 법에서 처리하고 마지막에 합치는 데 있다. 거듭제곱 계산이나 다항 합동식의 해를 셀 때 이 분해가 특히 위력을 발휘한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (거듭제곱의 분해 계산)**</ins> $$7^{100} \pmod{60}$$을 구하자. $$60 = 4\cdot 3\cdot 5$$로 쪼개어 각 법에서 따로 계산한다.

$$\begin{aligned}
7 &\equiv 3 \pmod 4, & 7^2 = 49 &\equiv 1 \pmod 4 &\Longrightarrow\quad 7^{100} = (7^2)^{50} &\equiv 1 \pmod 4, \\
7 &\equiv 1 \pmod 3, & & & 7^{100} &\equiv 1 \pmod 3, \\
7 &\equiv 2 \pmod 5, & 7^4 \equiv 2^4 = 16 &\equiv 1 \pmod 5 &\Longrightarrow\quad 7^{100} = (7^4)^{25} &\equiv 1 \pmod 5
\end{aligned}$$

이다. 따라서 $$7^{100}$$은 세 법 $$4, 3, 5$$ 모두에 대해 $$1$$과 합동이고, 정리에 의해 법 $$60$$에 대해 $$1$$과 합동인 수가 유일하므로 $$7^{100} \equiv 1 \pmod{60}$$이다. 큰 지수의 거듭제곱을 직접 다루지 않고 작은 법에서의 주기성만으로 답을 얻었다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (제곱근의 개수)**</ins> 합동식 $$x^2 \equiv 1 \pmod{15}$$의 해의 개수를 세자. $$15 = 3\cdot 5$$이고 참고 4의 동형 $$\mathbb{Z}/15\mathbb{Z} \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z}$$에 의해, 법 $$15$$에서의 해는 법 $$3$$에서의 해와 법 $$5$$에서의 해의 쌍에 일대일 대응한다. $$x^2 \equiv 1 \pmod 3$$의 해는 $$x \equiv 1, 2 \pmod 3$$의 두 개, $$x^2 \equiv 1 \pmod 5$$의 해는 $$x \equiv 1, 4 \pmod 5$$의 두 개이므로, 곱집합의 원소는 $$2\cdot 2 = 4$$개이다. 따라서 법 $$15$$에서 $$x^2 \equiv 1$$의 해도 $$4$$개이며, 각 쌍을 명제 5의 공식으로 복원하면 $$x \equiv 1, 4, 11, 14 \pmod{15}$$이다. 소수 법에서 이차합동식의 해가 둘 이하임에도 합성수 법에서는 더 많아질 수 있는 이유가 이 분해로 설명된다.

</div>
