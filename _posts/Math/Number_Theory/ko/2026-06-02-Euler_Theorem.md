---
title: "오일러 정리와 phi 함수"
description: "n과 서로소인 잉여류의 개수를 세는 오일러 phi 함수를 정의하고, 임의의 법에 대해 a^φ(n) ≡ 1이 성립한다는 오일러 정리를 증명한다. 중국인의 나머지 정리로부터 φ의 곱셈성과 명시 공식을 끌어낸다."
excerpt: "오일러 phi 함수, 오일러 정리, φ의 곱셈성과 공식"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/euler_theorem
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Euler_Theorem.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 9

published: false
---

[§페르마 소정리](/ko/math/number_theory/fermat_little_theorem)는 법이 소수일 때 $$a^{p-1} \equiv 1$$임을 말했다. 그 증명의 핵심은 $$0$$이 아닌 잉여류가 $$p-1$$개라는 것과 그들이 곱셈에 대해 닫혀 있다는 점이었다. 법이 합성수이면 곱셈 역원을 갖는 잉여류만이 이런 성질을 가지므로, 그 개수를 세는 함수가 필요하다.

## 오일러 phi 함수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 양의 정수 $$n$$에 대하여, $$1 \leq a \leq n$$이면서 $$\gcd(a, n) = 1$$인 정수 $$a$$의 개수를 *오일러 phi 함수<sub>Euler's totient</sub>* $$\varphi(n)$$이라 한다. $$n$$과 서로소인 잉여류들의 대표 모임 $$\{a_1, \ldots, a_{\varphi(n)}\}$$을 법 $$n$$의 *기약잉여계<sub>reduced residue system</sub>*라 한다.

</div>

곱셈 역원을 갖는 잉여류가 정확히 $$n$$과 서로소인 것들이므로 ([§합동식, ⁋명제 7](/ko/math/number_theory/congruences#prop7)), $$\varphi(n)$$은 $$\mathbb{Z}/n\mathbb{Z}$$에서 역원을 갖는 원소의 개수이다. 예컨대 $$\varphi(1) = 1$$, $$\varphi(p) = p - 1$$ ($$p$$ 소수), $$\varphi(12) = 4$$ ($$1, 5, 7, 11$$) 이다.

## 오일러 정리

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (오일러 정리)**</ins> $$\gcd(a, n) = 1$$이면

$$a^{\varphi(n)} \equiv 1 \pmod n$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$r_1, r_2, \ldots, r_{\varphi(n)}$$을 기약잉여계라 하자. $$\gcd(a, n) = 1$$이면 $$a r_1, a r_2, \ldots, a r_{\varphi(n)}$$ 역시 모두 $$n$$과 서로소이고, 소거법칙 ([§합동식, ⁋명제 6](/ko/math/number_theory/congruences#prop6))에 의해 법 $$n$$에 대해 서로 다르다. 따라서 이들은 기약잉여계 $$\{r_1, \ldots, r_{\varphi(n)}\}$$을 순서만 바꾸어 놓은 것이다. 양쪽을 모두 곱하면

$$a^{\varphi(n)} r_1 r_2 \cdots r_{\varphi(n)} \equiv r_1 r_2 \cdots r_{\varphi(n)} \pmod n$$

이고, 우변의 곱 $$r_1\cdots r_{\varphi(n)}$$은 $$n$$과 서로소이므로 소거하면 $$a^{\varphi(n)} \equiv 1 \pmod n$$을 얻는다.

</details>

$$n = p$$가 소수이면 $$\varphi(p) = p - 1$$이므로 오일러 정리는 페르마 소정리로 환원된다. 즉 오일러 정리는 페르마 소정리를 임의의 법으로 일반화한 것이다.

## φ의 곱셈성과 공식

$$\varphi$$를 실제로 계산하려면 그것이 곱셈적임을 알면 된다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$\gcd(m, n) = 1$$이면 $$\varphi(mn) = \varphi(m)\varphi(n)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

중국인의 나머지 정리 ([§중국인의 나머지 정리, ⁋참고 4](/ko/math/number_theory/chinese_remainder_theorem#rmk4))에 의해 환 동형 $$\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$$가 성립한다. 동형은 역원을 갖는 원소를 역원을 갖는 원소로 보내므로, $$\mathbb{Z}/mn\mathbb{Z}$$에서 가역인 원소는 양쪽 성분이 모두 가역인 쌍에 정확히 대응한다. 가역원의 개수를 세면 $$\varphi(mn) = \varphi(m)\varphi(n)$$이다.

</details>

소수 거듭제곱에서의 값은 직접 센다: $$1$$부터 $$p^k$$까지 중 $$p$$와 서로소가 *아닌* 수는 $$p$$의 배수 $$p, 2p, \ldots, p^{k-1}p$$의 $$p^{k-1}$$개이므로

$$\varphi(p^k) = p^k - p^{k-1} = p^k\left(1 - \frac1p\right)$$

이다. 곱셈성과 결합하면, $$n = p_1^{e_1}\cdots p_r^{e_r}$$의 소인수분해 ([§소수와 산술의 기본정리, ⁋정리 3](/ko/math/number_theory/primes#thm3))로부터

$$\varphi(n) = n\prod_{p \mid n}\left(1 - \frac1p\right)$$

을 얻는다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\varphi(360)$$을 구하자. $$360 = 2^3\cdot 3^2\cdot 5$$이므로 $$\varphi(360) = 360\left(1 - \tfrac12\right)\left(1 - \tfrac13\right)\left(1 - \tfrac15\right) = 360\cdot\tfrac12\cdot\tfrac23\cdot\tfrac45 = 96$$이다.

</div>

$$\varphi$$는 곱셈적 함수의 대표적인 예이며, 약수의 개수나 합 같은 다른 곱셈적 함수들과 함께 다음 글 [§산술적 함수와 뫼비우스 반전](/ko/math/number_theory/arithmetic_functions)에서 일반론으로 다루어진다. 한편 $$\mathbb{Z}/n\mathbb{Z}$$의 가역원들이 이루는 곱셈군의 구조 — 특히 그것이 언제 순환군인가 — 는 [§원시근](/ko/math/number_theory/primitive_roots)의 주제이다.
