---
title: "오일러 정리와 phi 함수"
description: "n과 서로소인 잉여류의 개수를 세는 오일러 phi 함수를 정의하고, 임의의 법에 대해 a^φ(n) ≡ 1이 성립한다는 오일러 정리를 증명한다. 중국인의 나머지 정리로부터 φ의 곱셈성과 명시 공식을 끌어낸다."
excerpt: "오일러 phi 함수, 오일러 정리, φ의 곱셈성과 공식"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/euler_theorem
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
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

<ins id="ex4">**예시 4**</ins> $$\varphi(360)$$을 구하자. $$360 = 2^3\cdot 3^2\cdot 5$$이므로 공식에 대입하면

$$\begin{aligned}
\varphi(360) &= 360\left(1 - \tfrac12\right)\left(1 - \tfrac13\right)\left(1 - \tfrac15\right) \\
&= 360\cdot\tfrac12\cdot\tfrac23\cdot\tfrac45 \\
&= 96
\end{aligned}$$

이다. 같은 값을 곱셈성으로도 확인할 수 있다. $$\varphi(8) = 4$$, $$\varphi(9) = 6$$, $$\varphi(5) = 4$$이고 $$8, 9, 5$$가 쌍마다 서로소이므로 $$\varphi(360) = 4\cdot 6\cdot 4 = 96$$이다.

</div>

## 응용: 거듭제곱과 역원

오일러 정리의 실질적 위력은 합성수 법에서 큰 거듭제곱을 계산할 때 드러난다. $$\gcd(a, n) = 1$$이면 $$a^{\varphi(n)} \equiv 1 \pmod n$$이므로, 지수를 $$\varphi(n)$$으로 나눈 나머지만 보면 충분하다. 즉 지수에 대한 산술은 법 $$\varphi(n)$$에서 이루어진다. 페르마 소정리가 소수 법에서 지수를 $$p - 1$$로 줄여 주었듯, 오일러 정리는 임의의 법에서 지수를 $$\varphi(n)$$으로 줄여 준다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (합성수 법의 거듭제곱)**</ins> $$7^{222}$$을 $$10$$으로 나눈 나머지를 구하자. $$\gcd(7, 10) = 1$$이고 $$\varphi(10) = 4$$이므로 오일러 정리에 의해 $$7^4 \equiv 1 \pmod{10}$$이다. 지수 $$222$$를 $$4$$로 나누면 $$222 = 4\cdot 55 + 2$$이므로

$$7^{222} = (7^4)^{55}\cdot 7^2 \equiv 1^{55}\cdot 49 \equiv 9 \pmod{10}$$

이다. 즉 $$7^{222}$$의 일의 자리는 $$9$$이다. 직접 $$7$$의 거듭제곱을 보면 일의 자리가 $$7, 9, 3, 1$$로 주기 $$4$$를 이루는 것과 일치한다.

</div>

지수가 다시 거듭제곱으로 주어질 때에는 이 환원을 두 단계로 반복한다. 바깥 법에서는 지수를 법 $$\varphi(n)$$으로 줄이고, 그 지수를 계산할 때 다시 안쪽 법 $$\varphi(n)$$에서 오일러 정리를 적용하는 식이다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (지수가 거듭제곱일 때)**</ins> $$3^{3^{100}}$$을 $$100$$으로 나눈 나머지를 구하자. $$\gcd(3, 100) = 1$$이고 $$\varphi(100) = 100\left(1 - \tfrac12\right)\left(1 - \tfrac15\right) = 40$$이므로 $$3^{40} \equiv 1 \pmod{100}$$이다. 따라서 지수 $$3^{100}$$을 법 $$40$$으로 줄여야 한다. 다시 $$\gcd(3, 40) = 1$$이고 $$\varphi(40) = 40\left(1 - \tfrac12\right)\left(1 - \tfrac15\right) = 16$$이므로

$$3^{100} = 3^{16\cdot 6 + 4} \equiv (3^{16})^6\cdot 3^4 \equiv 3^4 = 81 \equiv 1 \pmod{40}$$

이다. 그러므로 $$3^{3^{100}} \equiv 3^{1} = 3 \pmod{100}$$이며, $$3^{3^{100}}$$의 마지막 두 자리는 $$03$$이다.

</div>

오일러 정리는 역원을 명시적으로 적는 데에도 쓰인다. 페르마 소정리에서 소수 법의 역원이 $$a^{p-2}$$로 주어졌듯이 ([§페르마 소정리, ⁋명제 8](/ko/math/number_theory/fermat_little_theorem#prop8)), 임의의 법에서는 지수를 $$\varphi(n)$$ 기준으로 한 칸 내린 거듭제곱이 역원이 된다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (거듭제곱에 의한 역원)**</ins> $$\gcd(a, n) = 1$$이면 $$a$$의 법 $$n$$에 대한 곱셈 역원은 $$a^{\varphi(n) - 1}$$이다. 즉

$$a^{-1} \equiv a^{\varphi(n) - 1} \pmod n$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

오일러 정리 (정리 2) 에 의해 $$a^{\varphi(n)} \equiv 1 \pmod n$$이다. $$\varphi(n) \geq 1$$이므로 좌변을 $$a\cdot a^{\varphi(n) - 1}$$로 쪼개면

$$a\cdot a^{\varphi(n) - 1} \equiv 1 \pmod n$$

이고, 이는 정확히 $$a^{\varphi(n) - 1}$$이 $$a$$의 곱셈 역원임을 뜻한다.

</details>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (거듭제곱으로 역원 구하기)**</ins> 법 $$10$$에 대한 $$3$$의 역원을 구하자. $$\gcd(3, 10) = 1$$이고 $$\varphi(10) = 4$$이므로 명제 7에 의해

$$3^{-1} \equiv 3^{\varphi(10) - 1} = 3^{3} = 27 \equiv 7 \pmod{10}$$

이다. 실제로 $$3\cdot 7 = 21 \equiv 1 \pmod{10}$$이므로 옳다.

</div>

## φ 값의 합

$$\varphi$$의 곱셈성과 공식은 개별 값을 계산하게 해 주지만, $$\varphi$$ 자체가 만족하는 항등식도 있다. 가장 기본적인 것은 한 수의 모든 약수에 대한 $$\varphi$$ 값을 더하면 그 수 자신이 된다는 사실이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (약수에 대한 합)**</ins> 모든 양의 정수 $$n$$에 대하여

$$\sum_{d \mid n} \varphi(d) = n$$

이다. 여기서 합은 $$n$$의 모든 양의 약수 $$d$$에 걸친다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$1$$부터 $$n$$까지의 정수를 분모를 $$n$$으로 한 분수 $$\frac{1}{n}, \frac{2}{n}, \ldots, \frac{n}{n}$$로 보고, 각 분수를 기약분수로 약분하자. 약분된 분모는 모두 $$n$$의 약수이고, 분모가 $$d$$인 기약분수 $$\frac{a}{d}$$는 $$1 \leq a \leq d$$이면서 $$\gcd(a, d) = 1$$인 것이므로 정확히 $$\varphi(d)$$개이다. 따라서

$$\begin{aligned}
n &= \#\left\{\tfrac{1}{n}, \tfrac{2}{n}, \ldots, \tfrac{n}{n}\right\} \\
&= \sum_{d \mid n} \#\left\{\tfrac{a}{d} : 1 \leq a \leq d,\ \gcd(a, d) = 1\right\} \\
&= \sum_{d \mid n} \varphi(d)
\end{aligned}$$

를 얻는다. 둘째 줄에서 우리는 $$n$$개의 분수를 약분 후 분모에 따라 분류했으며, 같은 기약분수가 두 번 세어지지 않으므로 분할이 옳다.

</details>

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (합 항등식의 확인)**</ins> $$n = 12$$에서 명제 9를 확인하자. $$12$$의 약수는 $$1, 2, 3, 4, 6, 12$$이고 각각의 $$\varphi$$ 값은

$$\varphi(1) = 1,\quad \varphi(2) = 1,\quad \varphi(3) = 2,\quad \varphi(4) = 2,\quad \varphi(6) = 2,\quad \varphi(12) = 4$$

이다. 이들을 더하면

$$\sum_{d \mid 12} \varphi(d) = 1 + 1 + 2 + 2 + 2 + 4 = 12$$

로 과연 $$n = 12$$와 같다.

</div>

