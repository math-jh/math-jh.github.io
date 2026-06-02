---
title: "일차 합동식"
description: "일차 합동식 ax ≡ b (mod n)의 해를 다룬다. 해가 존재할 조건이 gcd(a,n)이 b를 나누는 것임을 보이고, 그 경우 법 n에 대한 해의 개수가 정확히 gcd(a,n)임을 증명하며 곱셈 역원으로 해를 구한다."
excerpt: "일차 합동식의 가해성, 해의 개수, 해법"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/linear_congruences
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Linear_Congruences.png
    overlay_filter: 0.5

date: 2026-06-21
last_modified_at: 2026-06-21

weight: 6

published: false
---

[§합동식](/ko/math/number_theory/congruences)에서 합동의 연산과 곱셈 역원을 다루었다. 이제 가장 기본적인 합동방정식인 일차 합동식 $$ax \equiv b \pmod n$$의 해를 분석한다. 이는 일차 부정방정식 $$ax + ny = b$$를 푸는 것과 같은 문제이며, Bézout 항등식이 그 가해성을 완전히 결정한다.

## 가해성과 해의 개수

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $$d = \gcd(a, n)$$이라 하자. 일차 합동식 $$ax \equiv b \pmod n$$은 $$d \mid b$$일 때에만 해를 가지며, 이 경우 법 $$n$$에 대해 서로 다른 해가 정확히 $$d$$개 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$ax \equiv b \pmod n$$은 $$ax - b = ny$$, 즉 $$ax - ny = b$$인 정수 $$y$$가 있다는 것과 동치이다. $$ax - ny$$ 꼴의 정수 전체는 $$\gcd(a,n) = d$$의 배수 전체와 일치하므로 ([§유클리드 호제법과 Bézout 항등식, ⁋따름정리 4](/ko/math/number_theory/euclidean_algorithm#cor4)), 해가 존재할 필요충분조건은 $$d \mid b$$이다.

$$d \mid b$$라 하고 $$a = da'$$, $$n = dn'$$, $$b = db'$$로 쓰면 $$\gcd(a', n') = 1$$이고, 원래 식은 $$a'x \equiv b' \pmod{n'}$$과 동치이다. $$\gcd(a', n') = 1$$이므로 $$a'$$은 법 $$n'$$에 대해 역원을 가지고 ([§합동식, ⁋명제 7](/ko/math/number_theory/congruences#prop7)), 이 식은 법 $$n'$$에 대해 유일한 해 $$x \equiv (a')^{-1}b' \pmod{n'}$$을 가진다. 법 $$n'$$에 대한 하나의 해는 법 $$n = dn'$$에 대해서는 $$x_0, x_0 + n', x_0 + 2n', \ldots, x_0 + (d-1)n'$$의 $$d$$개의 서로 다른 잉여류에 대응하므로, 해는 정확히 $$d$$개이다.

</details>

특히 $$\gcd(a, n) = 1$$이면 임의의 $$b$$에 대해 해가 유일하게 존재하며, 그 해는 $$x \equiv a^{-1}b \pmod n$$이다. 역원 $$a^{-1}$$은 Bézout 항등식 $$ax + ny = 1$$을 유클리드 호제법으로 풀어 얻는다.

## 해법과 예시

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$6x \equiv 8 \pmod{14}$$를 풀자. $$d = \gcd(6, 14) = 2$$이고 $$2 \mid 8$$이므로 해가 있으며, 그 개수는 $$2$$이다. 양변과 법을 $$2$$로 나누면 $$3x \equiv 4 \pmod 7$$이고, $$3^{-1} \equiv 5 \pmod 7$$ ($$3\cdot 5 = 15 \equiv 1$$) 이므로 $$x \equiv 5\cdot 4 = 20 \equiv 6 \pmod 7$$이다. 법 $$14$$로 올리면 해는 $$x \equiv 6$$과 $$x \equiv 13 \pmod{14}$$의 두 개이다.

</div>

일차 합동식은 한 개의 법에 대한 가장 단순한 방정식이다. 서로 다른 여러 법에 대한 합동식을 동시에 만족시키는 해를 찾는 문제는 다음 글 [§중국인의 나머지 정리](/ko/math/number_theory/chinese_remainder_theorem)에서 다루며, 그곳에서 법들이 쌍마다 서로소일 때 해가 항상 존재하고 유일함을 본다.
