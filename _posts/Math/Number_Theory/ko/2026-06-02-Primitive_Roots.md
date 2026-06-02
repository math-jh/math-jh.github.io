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

## 위수의 성질과 계산

위수는 거듭제곱과 곱에 대해 규칙적으로 변한다. 우선 한 원소를 거듭제곱했을 때 위수가 어떻게 바뀌는지를 본다. 이 공식은 원시근으로부터 임의의 위수를 가진 원소를 만들어 내는 핵심 도구이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\gcd(a, n) = 1$$이고 $$d = \operatorname{ord}_n(a)$$이면, 임의의 양의 정수 $$k$$에 대해

$$\operatorname{ord}_n(a^k) = \frac{d}{\gcd(d, k)}$$

이다. 특히 $$\operatorname{ord}_n(a^k) = d$$인 것은 $$\gcd(d, k) = 1$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$e = \operatorname{ord}_n(a^k)$$라 하자. 명제 2에 의해 $$(a^k)^m \equiv 1 \pmod n$$인 것은 $$d \mid km$$인 것과 동치이다. $$g = \gcd(d, k)$$로 두고 $$d = g d'$$, $$k = g k'$$ ($$\gcd(d', k') = 1$$) 로 적으면

$$\begin{aligned}
d \mid km &\iff g d' \mid g k' m \\
&\iff d' \mid k' m \\
&\iff d' \mid m
\end{aligned}$$

이다. 마지막 동치는 $$\gcd(d', k') = 1$$이므로 $$d'$$이 $$m$$을 나누어야 함에서 따른다. 따라서 $$(a^k)^m \equiv 1$$을 만족하는 가장 작은 양의 정수 $$m$$은 $$d' = d/g$$이고, 곧 $$e = d/\gcd(d, k)$$이다.

</details>

이 공식에서 원시근 $$g$$가 있으면 $$\operatorname{ord}_n(g^k) = \varphi(n)/\gcd(\varphi(n), k)$$이므로, $$g^k$$가 다시 원시근이 되는 것은 $$\gcd(k, \varphi(n)) = 1$$일 때뿐이다. 이로부터 원시근의 개수를 즉시 셀 수 있다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 법 $$n$$에 원시근이 하나라도 존재하면, 서로 다른 원시근은 정확히 $$\varphi(\varphi(n))$$개이다. 특히 소수 $$p$$에 대한 원시근은 $$\varphi(p-1)$$개이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

원시근 $$g$$를 고정하면 모든 기약잉여류는 $$g^k$$ ($$1 \leq k \leq \varphi(n)$$) 꼴로 유일하게 적힌다. 명제 6에 의해 $$g^k$$가 원시근, 곧 $$\operatorname{ord}_n(g^k) = \varphi(n)$$인 것은 $$\gcd(k, \varphi(n)) = 1$$인 것과 동치이다. $$1 \leq k \leq \varphi(n)$$ 중 $$\varphi(n)$$과 서로소인 $$k$$의 개수가 바로 $$\varphi(\varphi(n))$$이므로, 원시근은 $$\varphi(\varphi(n))$$개이다.

</details>

명제 6은 또한 정리 4의 증명을 거꾸로 읽는 방법을 준다. 위수가 $$d$$인 원소가 하나 있으면, 그것을 $$\gcd(k,d)=1$$인 $$k$$로 거듭제곱한 $$\varphi(d)$$개가 정확히 위수 $$d$$를 가지므로, 위수 $$d$$인 원소의 개수 $$\psi(d)$$는 $$0$$이거나 $$\varphi(d)$$이다.

## 예시와 계산

추상적인 존재 증명을 구체적인 계산으로 확인한다. 먼저 작은 소수에서 원시근을 직접 찾는다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (법 7의 원시근)**</ins> $$\varphi(7) = 6$$이므로 위수는 $$6$$의 약수 $$1, 2, 3, 6$$ 중 하나이다. $$a = 2$$의 거듭제곱을 차례로 계산하면

$$\begin{aligned}
2^1 &\equiv 2, & 2^2 &\equiv 4, & 2^3 &\equiv 1 \pmod 7
\end{aligned}$$

이므로 $$\operatorname{ord}_7(2) = 3$$이고 $$2$$는 원시근이 아니다. 다음으로 $$a = 3$$을 보면

$$\begin{aligned}
3^1 &\equiv 3, & 3^2 &\equiv 2, & 3^3 &\equiv 6, \\
3^4 &\equiv 4, & 3^5 &\equiv 5, & 3^6 &\equiv 1 \pmod 7
\end{aligned}$$

이어서 $$3, 2, 6, 4, 5, 1$$이 기약잉여계 $$\{1, 2, 3, 4, 5, 6\}$$ 전체를 훑는다. 따라서 $$\operatorname{ord}_7(3) = 6$$이고 $$3$$이 원시근이다.

</div>

명제 7에 따르면 법 $$7$$의 원시근은 $$\varphi(\varphi(7)) = \varphi(6) = 2$$개이어야 한다. 실제로 명제 6으로 $$\gcd(k, 6) = 1$$인 $$k = 1, 5$$에 대한 $$3^1 \equiv 3$$과 $$3^5 \equiv 5$$가 원시근이며, 나머지 $$3^2 \equiv 2$$ (위수 $$3$$), $$3^3 \equiv 6$$ (위수 $$2$$), $$3^4 \equiv 4$$ (위수 $$3$$), $$3^6 \equiv 1$$ (위수 $$1$$) 은 모두 위수가 $$6$$보다 작다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (위수가 합성수일 때의 거동)**</ins> 명제 6은 큰 위수에서 작은 위수를 만들어 낸다. 법 $$7$$에서 원시근 $$3$$은 위수 $$6$$이므로

$$\operatorname{ord}_7(3^2) = \frac{6}{\gcd(6,2)} = \frac{6}{2} = 3, \qquad \operatorname{ord}_7(3^3) = \frac{6}{\gcd(6,3)} = \frac{6}{3} = 2$$

이다. 즉 $$3^2 \equiv 2$$는 위수 $$3$$, $$3^3 \equiv 6$$은 위수 $$2$$이며, 이는 예시 8의 직접 계산과 일치한다. 한 원시근만 알면 가능한 모든 위수의 원소를 이렇게 거듭제곱으로 뽑아낼 수 있다.

</div>

원시근의 진가는 곱셈을 덧셈으로 바꾸는 데 있다. 원시근 $$g$$를 고정하면, 각 기약잉여류 $$a$$에 대해 $$a \equiv g^\ell \pmod n$$인 지수 $$\ell$$ (법 $$\varphi(n)$$) 이 유일하게 정해지는데, 이를 $$g$$에 대한 $$a$$의 *지표<sub>index</sub>* 또는 이산로그라 하고 $$\operatorname{ind}_g a$$로 적는다. 로그의 성질 $$\operatorname{ind}_g(ab) \equiv \operatorname{ind}_g a + \operatorname{ind}_g b \pmod{\varphi(n)}$$이 성립하여, 곱셈 합동식이 덧셈 합동식으로 환원된다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (지표를 이용한 거듭제곱 합동식)**</ins> 법 $$7$$에서 $$x^4 \equiv 4 \pmod 7$$을 풀자. 원시근 $$g = 3$$에 대한 지표표는 예시 8에서

$$\operatorname{ind}_3 1 = 6,\ \operatorname{ind}_3 2 = 2,\ \operatorname{ind}_3 3 = 1,\ \operatorname{ind}_3 4 = 4,\ \operatorname{ind}_3 5 = 5,\ \operatorname{ind}_3 6 = 3$$

이다. $$x \equiv 3^t$$로 놓으면 $$x^4 \equiv 3^{4t}$$이고 $$4 \equiv 3^4$$이므로, 합동식은

$$4t \equiv 4 \pmod 6$$

으로 바뀐다. $$\gcd(4, 6) = 2$$이고 $$2 \mid 4$$이므로 해가 $$2$$개 있으며, 양변을 $$2$$로 나누면 $$2t \equiv 2 \pmod 3$$, 곧 $$t \equiv 1 \pmod 3$$이다. 따라서 $$t \equiv 1, 4 \pmod 6$$이고

$$x \equiv 3^1 \equiv 3, \qquad x \equiv 3^4 \equiv 4 \pmod 7$$

이 두 해이다. 실제로 $$3^4 \equiv 4$$, $$4^4 = 256 = 7\cdot 36 + 4 \equiv 4$$로 확인된다.

</div>

이 방법은 일반적으로 $$x^k \equiv a \pmod p$$ 꼴의 합동식을, 원시근에 대한 지표를 취해 일차 합동식 $$k t \equiv \operatorname{ind}_g a \pmod{p-1}$$로 환원한다 ([§일차 합동식](/ko/math/number_theory/linear_congruences)). 따라서 해의 개수는 $$\gcd(k, p-1)$$이 $$\operatorname{ind}_g a$$를 나누면 $$\gcd(k, p-1)$$개, 그렇지 않으면 $$0$$개이다.

마지막으로 합성수 법에서 곱셈군이 순환하지 않는 경우를 참고 5의 법 $$8$$에서 구체적으로 본다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (법 8에는 원시근이 없음)**</ins> $$\varphi(8) = 4$$이므로 원시근이 있으려면 위수 $$4$$인 원소가 있어야 한다. 기약잉여류 $$1, 3, 5, 7$$의 제곱을 계산하면

$$\begin{aligned}
1^2 &\equiv 1, & 3^2 &= 9 \equiv 1, \\
5^2 &= 25 \equiv 1, & 7^2 &= 49 \equiv 1 \pmod 8
\end{aligned}$$

이어서 $$1$$을 뺀 세 원소가 모두 위수 $$2$$이다. 위수 $$4$$인 원소가 없으므로 원시근이 존재하지 않으며, 곱셈군은 순환군이 아니라 $$\mathbb{Z}/2 \times \mathbb{Z}/2$$ 구조를 가진다. 이는 참고 5의 예외 목록 $$n = 1, 2, 4, p^k, 2p^k$$에 $$8$$이 들지 않음과 부합한다.

</div>

원시근 $$g$$가 있으면 모든 기약잉여류가 $$g$$의 거듭제곱으로 적히므로, 곱셈이 지수의 덧셈으로 바뀌어 — 마치 로그처럼 — 계산이 단순해진다. 이 구조는 다음 글 [§이차 잉여](/ko/math/number_theory/quadratic_residues)에서 어떤 수가 법 $$p$$에서 제곱수인지를 판정하는 데 직접 쓰인다.
