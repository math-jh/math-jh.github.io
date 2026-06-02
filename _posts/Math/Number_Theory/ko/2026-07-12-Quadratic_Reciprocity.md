---
title: "이차 상호법칙"
description: "가우스 보조정리를 증명하여 2가 언제 이차 잉여인지를 결정하고, 두 홀수 소수의 르장드르 기호를 맞바꾸는 이차 상호법칙을 격자점 계산으로 증명한다. 이를 이용해 르장드르 기호를 효율적으로 계산한다."
excerpt: "가우스 보조정리, 제2보충법칙, 이차 상호법칙"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/quadratic_reciprocity
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Quadratic_Reciprocity.png
    overlay_filter: 0.5

date: 2026-07-12
last_modified_at: 2026-07-12

weight: 13

published: false
---

[§이차 잉여](/ko/math/number_theory/quadratic_residues)에서 르장드르 기호가 곱셈적임을 보았고, 그 계산이 소수와 $$-1$$에서의 값으로 환원됨을 알았다. $$-1$$의 경우는 이미 해결했으니, 남은 것은 두 홀수 소수의 르장드르 기호 사이의 관계 — 가우스가 "황금 정리"라 부른 이차 상호법칙 — 이다.

## 가우스 보조정리

상호법칙의 증명과 $$2$$의 처리에 공통으로 쓰이는 도구이다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1 (가우스 보조정리)**</ins> 홀수 소수 $$p$$와 $$p \nmid a$$에 대하여, $$a, 2a, \ldots, \dfrac{p-1}{2}a$$를 법 $$p$$로 환원한 최소 양의 나머지 중 $$\dfrac{p}{2}$$보다 큰 것의 개수를 $$\mu$$라 하면

$$\left(\frac{a}{p}\right) = (-1)^{\mu}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 $$ja$$ ($$1 \leq j \leq \tfrac{p-1}{2}$$) 의 최소 양의 나머지를 $$r_j$$라 하자. $$r_j > p/2$$인 것들은 $$p - r_j < p/2$$로 바꾸어 두면, 얻어진 수들 $$\{r_j : r_j < p/2\} \cup \{p - r_j : r_j > p/2\}$$이 정확히 $$1, 2, \ldots, \tfrac{p-1}{2}$$의 재배열임을 보일 수 있다 (서로 다르고 모두 $$p/2$$ 미만이며 개수가 같다). 모두 곱하면

$$\left(\tfrac{p-1}{2}\right)! \equiv (-1)^{\mu}\prod_j r_j \equiv (-1)^{\mu} a^{(p-1)/2}\left(\tfrac{p-1}{2}\right)! \pmod p$$

이고 (부호 $$(-1)^\mu$$는 $$r_j > p/2$$인 $$\mu$$개를 $$-r_j$$로 바꾼 데서 나온다), $$\left(\tfrac{p-1}{2}\right)!$$을 소거한 뒤 오일러 판정법 ([§이차 잉여, ⁋정리 4](/ko/math/number_theory/quadratic_residues#thm4))을 쓰면 $$\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \equiv (-1)^\mu$$를 얻는다.

</details>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (제2보충법칙)**</ins> 홀수 소수 $$p$$에 대하여 $$\left(\dfrac{2}{p}\right) = (-1)^{(p^2-1)/8}$$이다. 즉 $$2$$는 $$p \equiv \pm 1 \pmod 8$$일 때 이차 잉여이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

가우스 보조정리를 $$a = 2$$에 적용한다. $$2, 4, \ldots, p-1$$ 중 $$p/2$$를 넘는 것의 개수 $$\mu$$를 세면 $$\mu = \tfrac{p-1}{2} - \lfloor p/4\rfloor$$이고, $$p$$를 $$8$$로 나눈 나머지에 따라 $$\mu$$의 홀짝을 따지면 $$(-1)^\mu = (-1)^{(p^2-1)/8}$$임이 확인된다.

</details>

## 이차 상호법칙

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (이차 상호법칙)**</ins> 서로 다른 두 홀수 소수 $$p, q$$에 대하여

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$$

이다. 즉 $$p$$와 $$q$$ 중 적어도 하나가 $$4$$로 나누어 $$1$$이 남으면 $$\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$$이고, 둘 다 $$3$$이 남으면 부호가 반대이다.

</div>

<details class="proof" markdown="1">
<summary>증명 (개요)</summary>

가우스 보조정리에 의해 $$\left(\frac{q}{p}\right) = (-1)^{S}$$이며, 여기서 $$S = \sum_{j=1}^{(p-1)/2}\lfloor jq/p\rfloor$$임을 보일 수 있다. 이 합 $$S$$는 직사각형 $$0 < x < p/2$$, $$0 < y < q/2$$ 안의 격자점 중 직선 $$py = qx$$ 아래에 있는 것의 개수이다. 대칭적으로 $$\left(\frac{p}{q}\right) = (-1)^{T}$$이고 $$T$$는 같은 직사각형에서 직선 위의 격자점 개수이다. 직선 위에는 격자점이 없으므로 $$S + T$$는 직사각형 안의 전체 격자점 수 $$\dfrac{p-1}{2}\cdot\dfrac{q-1}{2}$$와 같고, 따라서 $$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{S+T} = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\left(\dfrac{30}{53}\right)$$을 구하자. $$53$$은 소수이고 $$30 = 2\cdot 3\cdot 5$$이므로 곱셈성으로 $$\left(\frac{30}{53}\right) = \left(\frac{2}{53}\right)\left(\frac{3}{53}\right)\left(\frac{5}{53}\right)$$이다. $$53 \equiv 5 \pmod 8$$이므로 $$\left(\frac{2}{53}\right) = -1$$이다. 상호법칙으로 $$53 \equiv 1 \pmod 4$$이니 $$\left(\frac{3}{53}\right) = \left(\frac{53}{3}\right) = \left(\frac{2}{3}\right) = -1$$, $$\left(\frac{5}{53}\right) = \left(\frac{53}{5}\right) = \left(\frac{3}{5}\right) = -1$$이다. 따라서 $$\left(\frac{30}{53}\right) = (-1)(-1)(-1) = -1$$로, $$30$$은 법 $$53$$의 비잉여이다.

</div>

이차 상호법칙은 르장드르 기호의 계산을 유클리드 호제법처럼 분모와 분자를 번갈아 줄여 가는 효율적 절차로 바꾼다. 제곱수의 산술은 정수의 범위를 넘어서면 더 풍부해지는데, 다음 글 [§가우스 정수와 두 제곱수의 합](/ko/math/number_theory/gaussian_integers)에서 $$\sqrt{-1}$$을 더한 정수환을 다루며 어떤 소수가 두 제곱수의 합인지를 판정한다.
