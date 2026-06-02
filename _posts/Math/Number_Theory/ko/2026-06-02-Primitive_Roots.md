---
title: "원시근"
description: "잉여류의 위수를 정의하고, 소수를 법으로 하는 기약잉여계의 곱셈군이 순환군임을 — 즉 원시근이 존재함을 — 약수에 대한 phi 함수의 합 항등식을 이용하여 증명한다. 일반 법에서의 원시근 존재 조건도 정리한다."
excerpt: "위수, 원시근, 소수 법의 곱셈군의 순환성"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/primitive_roots
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Primitive_Roots.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 11

published: false
---

[§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)는 $$\gcd(a, n) = 1$$일 때 $$a^{\varphi(n)} \equiv 1$$임을 말했다. 그렇다면 $$a$$의 거듭제곱이 $$1$$로 돌아오는 가장 작은 지수는 무엇이며, 그 거듭제곱이 기약잉여계 전체를 훑을 수 있는가? 이 물음이 잉여류의 곱셈 구조를 드러낸다.

## 위수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\gcd(a, n) = 1$$일 때, $$a^k \equiv 1 \pmod n$$을 만족하는 가장 작은 양의 정수 $$k$$를 $$a$$의 법 $$n$$에 대한 *위수<sub>order</sub>*라 하고 $$\operatorname{ord}_n(a)$$로 적는다.

</div>

오일러 정리에 의해 위수는 항상 존재하며 $$\varphi(n)$$ 이하이다. 위수는 다음의 나눗셈 성질로 통제된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$a^k \equiv 1 \pmod n$$인 것은 $$\operatorname{ord}_n(a) \mid k$$인 것과 동치이다. 특히 $$\operatorname{ord}_n(a) \mid \varphi(n)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$d = \operatorname{ord}_n(a)$$라 하고 $$k = dq + r$$ ($$0 \leq r < d$$) 로 나누면 $$a^k = (a^d)^q a^r \equiv a^r \pmod n$$이다. $$a^k \equiv 1$$이면 $$a^r \equiv 1$$인데 $$r < d$$이고 $$d$$가 최소이므로 $$r = 0$$, 즉 $$d \mid k$$이다. 역은 자명하다. 오일러 정리 $$a^{\varphi(n)} \equiv 1$$에 적용하면 $$d \mid \varphi(n)$$이다.

</details>

## 원시근의 존재

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$\operatorname{ord}_n(a) = \varphi(n)$$인 $$a$$를 법 $$n$$의 *원시근<sub>primitive root</sub>*이라 한다. 원시근 $$g$$가 존재하면 $$g, g^2, \ldots, g^{\varphi(n)}$$이 기약잉여계 전체를 이룬다.

</div>

원시근의 존재는 곱셈군이 한 원소로 생성되는 순환군임을 뜻한다. 소수 법에서는 언제나 존재한다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> $$p$$가 소수이면 법 $$p$$의 원시근이 존재한다. 즉 $$\mathbb{Z}/p\mathbb{Z}$$의 $$0$$이 아닌 원소들이 이루는 곱셈군은 순환군이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위수 $$d$$인 원소의 개수를 $$\psi(d)$$라 하자. 각 위수는 $$p - 1$$의 약수이므로 $$\sum_{d \mid p-1}\psi(d) = p - 1$$이다. 위수가 $$d$$인 원소가 하나라도 있으면, 그것이 생성하는 $$d$$개의 원소 $$1, a, \ldots, a^{d-1}$$이 모두 $$x^d \equiv 1 \pmod p$$의 해이다. 이 합동식은 체 $$\mathbb{Z}/p\mathbb{Z}$$에서 차수 $$d$$의 다항식이므로 해가 많아야 $$d$$개이고, 따라서 그 $$d$$개가 해 전부이다. 그중 위수가 정확히 $$d$$인 것은 $$\varphi(d)$$개이므로, $$\psi(d)$$는 $$0$$ 또는 $$\varphi(d)$$이다. 한편 $$\sum_{d\mid p-1}\varphi(d) = p - 1$$이므로 ([§산술적 함수와 뫼비우스 반전, ⁋예시 7](/ko/math/number_theory/arithmetic_functions#ex7)), $$\sum_d \psi(d) = \sum_d \varphi(d)$$에서 모든 약수 $$d$$에 대해 $$\psi(d) = \varphi(d)$$이어야 한다. 특히 $$\psi(p-1) = \varphi(p-1) \geq 1$$이므로 위수 $$p - 1$$인 원소, 곧 원시근이 존재한다.

</details>

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> 일반 법 $$n$$에 대해 원시근이 존재하는 것은 $$n = 1, 2, 4, p^k, 2p^k$$ (여기서 $$p$$는 홀수 소수) 인 경우에 한한다. 따라서 $$\mathbb{Z}/n\mathbb{Z}$$의 곱셈군은 일반적으로 순환군이 아니며, 가령 법 $$8$$에서는 $$1, 3, 5, 7$$의 위수가 모두 $$2$$ 이하여서 원시근이 없다.

</div>

원시근 $$g$$가 있으면 모든 기약잉여류가 $$g$$의 거듭제곱으로 적히므로, 곱셈이 지수의 덧셈으로 바뀌어 — 마치 로그처럼 — 계산이 단순해진다. 이 구조는 다음 글 [§이차 잉여](/ko/math/number_theory/quadratic_residues)에서 어떤 수가 법 $$p$$에서 제곱수인지를 판정하는 데 직접 쓰인다.
