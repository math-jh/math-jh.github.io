---
title: "산술적 함수와 뫼비우스 반전"
description: "곱셈적 산술 함수를 정의하고 약수 함수와 뫼비우스 함수를 다룬다. 디리클레 합성곱을 도입하여 뫼비우스 반전공식을 증명하고, 약수에 대한 phi 함수의 합이 n과 같다는 항등식을 응용으로 얻는다."
excerpt: "곱셈적 함수, 약수 함수, 뫼비우스 함수와 반전공식"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/arithmetic_functions
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Arithmetic_Functions.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 10

published: false
---

[§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)에서 $$\varphi$$가 서로소인 인수에 대해 곱으로 분해됨을 보았다. 이런 성질을 가진 함수들은 정수론에서 거듭 나타나며, 그들 사이의 관계는 합성곱이라는 연산으로 깔끔하게 기술된다.

## 곱셈적 함수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 양의 정수에서 정의된 함수를 *산술적 함수<sub>arithmetic function</sub>*라 한다. 산술적 함수 $$f$$가 항등적으로 $$0$$은 아니면서 $$\gcd(m, n) = 1$$일 때마다 $$f(mn) = f(m)f(n)$$을 만족하면 *곱셈적<sub>multiplicative</sub>*이라 한다.

</div>

곱셈적 함수는 $$f(1) = 1$$을 만족하며, 소수 거듭제곱에서의 값으로 완전히 결정된다: $$n = \prod p_i^{e_i}$$이면 $$f(n) = \prod f(p_i^{e_i})$$이다. $$\varphi$$는 곱셈적 함수의 한 예였다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 약수의 개수 $$\tau(n) = \sum_{d \mid n} 1$$과 약수의 합 $$\sigma(n) = \sum_{d\mid n} d$$은 곱셈적이다. 소수 거듭제곱에서 $$\tau(p^e) = e + 1$$, $$\sigma(p^e) = 1 + p + \cdots + p^e = \dfrac{p^{e+1} - 1}{p - 1}$$이므로, 일반적으로

$$\tau(n) = \prod_i (e_i + 1), \qquad \sigma(n) = \prod_i \frac{p_i^{e_i + 1} - 1}{p_i - 1}$$

이다. 가령 $$\tau(12) = \tau(2^2)\tau(3) = 3\cdot 2 = 6$$이다.

</div>

## 디리클레 합성곱과 뫼비우스 함수

산술적 함수들 사이의 자연스러운 곱은 약수에 걸친 합으로 정의된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 두 산술적 함수 $$f, g$$의 *디리클레 합성곱<sub>Dirichlet convolution</sub>* $$f \ast g$$는

$$(f \ast g)(n) = \sum_{d \mid n} f(d)\, g\!\left(\frac{n}{d}\right)$$

으로 정의된다.

</div>

상수함수 $$\mathbf{1}(n) = 1$$과 항등함수 $$\mathrm{id}(n) = n$$을 합성곱의 재료로 쓰면 약수 함수가 $$\tau = \mathbf{1} \ast \mathbf{1}$$, $$\sigma = \mathbf{1} \ast \mathrm{id}$$로 표현된다. 합성곱의 단위원은 $$n = 1$$에서만 $$1$$이고 나머지에서 $$0$$인 함수 $$\varepsilon$$이다. $$\mathbf{1}$$의 합성곱 역원이 다음의 뫼비우스 함수이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *뫼비우스 함수<sub>Möbius function</sub>* $$\mu$$는 $$\mu(1) = 1$$, 그리고 $$n > 1$$이 서로 다른 $$k$$개의 소수의 곱이면 $$\mu(n) = (-1)^k$$, $$n$$이 어떤 소수의 제곱으로 나누어떨어지면 $$\mu(n) = 0$$으로 정의된다.

</div>

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\mu$$는 곱셈적이며, $$n > 1$$이면 $$\sum_{d \mid n} \mu(d) = 0$$이다. 즉 $$\mathbf{1} \ast \mu = \varepsilon$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$n = \prod p_i^{e_i}$$ ($$n > 1$$) 에 대해 $$\sum_{d\mid n}\mu(d)$$에서 $$\mu(d) \neq 0$$인 약수는 서로 다른 소수들의 곱뿐이다. $$n$$의 서로 다른 소인수가 $$r$$개이면, 그중 $$j$$개를 고른 약수가 $$\binom{r}{j}$$개이고 각각 $$\mu$$ 값이 $$(-1)^j$$이므로

$$\sum_{d\mid n}\mu(d) = \sum_{j=0}^{r}\binom{r}{j}(-1)^j = (1 - 1)^r = 0$$

이다. 곱셈성은 정의에서 직접 확인된다.

</details>

## 뫼비우스 반전공식

명제 5는 합성곱에서 $$\mathbf{1}$$을 "되돌리는" 도구가 되어, 약수합의 형태로 묶인 관계를 풀어낸다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (뫼비우스 반전공식)**</ins> 산술적 함수 $$f, g$$에 대하여

$$g(n) = \sum_{d \mid n} f(d) \quad\Longleftrightarrow\quad f(n) = \sum_{d \mid n}\mu(d)\, g\!\left(\frac{n}{d}\right)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

왼쪽 조건은 $$g = \mathbf{1}\ast f$$를 뜻한다. 양변에 $$\mu$$를 합성곱하면 합성곱의 결합법칙과 명제 5에 의해 $$\mu \ast g = \mu\ast\mathbf{1}\ast f = \varepsilon \ast f = f$$이고, 이것이 오른쪽 식이다. 역방향도 같은 계산을 거꾸로 하면 된다.

</details>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 약수에 걸친 $$\varphi$$의 합은 $$\sum_{d \mid n}\varphi(d) = n$$이다. 실제로 $$1$$부터 $$n$$까지의 각 정수 $$m$$을 $$\gcd(m, n) = n/d$$에 따라 분류하면, $$\gcd(m,n) = n/d$$인 $$m$$의 개수가 $$\varphi(d)$$이므로 전체 합이 $$n$$이 된다. 이 관계 $$\mathbf{1}\ast\varphi = \mathrm{id}$$에 뫼비우스 반전을 적용하면 $$\varphi = \mu \ast \mathrm{id}$$, 즉 $$\varphi(n) = \sum_{d\mid n}\mu(d)\,\dfrac{n}{d}$$이라는 $$\varphi$$의 또 다른 공식을 얻는다.

</div>

곱셈적 함수와 디리클레 합성곱은 소수의 분포를 함수의 언어로 다루는 해석적 정수론의 대수적 골격을 이룬다. 이들을 생성함수 $$\sum_n f(n) n^{-s}$$로 부호화한 디리클레 급수는 리만 제타 함수와 만나며, 그 해석적 성질은 [§소수의 무한성과 분포, ⁋참고 3](/ko/math/number_theory/distribution_of_primes#rmk3)에서 언급한 소수 정리로 이어진다.
