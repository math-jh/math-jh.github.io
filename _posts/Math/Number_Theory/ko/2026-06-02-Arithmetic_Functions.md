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

마지막 식을 곱셈성과 결합하면 $$\varphi$$의 곱공식이 다시 나온다. $$\varphi = \mu \ast \mathrm{id}$$가 곱셈적 함수 두 개의 합성곱이므로 (아래 [명제 9](#prop9)) 곱셈적이고, 소수 거듭제곱에서

$$\varphi(p^e) = \sum_{j=0}^{e}\mu(p^j)\,p^{e-j} = \mu(1)\,p^e + \mu(p)\,p^{e-1} = p^e - p^{e-1} = p^{e-1}(p-1)$$

이므로, $$n = \prod_i p_i^{e_i}$$에 대해

$$\varphi(n) = \prod_i p_i^{e_i - 1}(p_i - 1) = n\prod_{p \mid n}\Bigl(1 - \frac1p\Bigr)$$

이라는 익숙한 형태를 얻는다. 합성곱과 반전이라는 대수적 도구만으로 ([§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem))에서 직접 센 결과가 재생산되는 것이다.

## 합성곱의 대수적 구조

디리클레 합성곱이 단순한 표기 약식이 아니라 풍부한 대수 구조를 갖는다는 점이 뫼비우스 반전을 떠받친다. 산술적 함수 전체의 모임 위에서 덧셈과 합성곱은 가환환을 이루며, 그 단위원이 $$\varepsilon$$이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 디리클레 합성곱은 가환적·결합적이며 $$\varepsilon$$을 단위원으로 갖는다. 즉 임의의 산술적 함수 $$f, g, h$$에 대해 $$f \ast g = g \ast f$$, $$(f \ast g)\ast h = f \ast (g \ast h)$$, $$f \ast \varepsilon = f$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

가환성은 $$d \mapsto n/d$$가 $$n$$의 약수들을 그 자신으로 치환함에서 나온다:

$$(f \ast g)(n) = \sum_{d \mid n} f(d)\,g\!\left(\frac{n}{d}\right) = \sum_{d' \mid n} f\!\left(\frac{n}{d'}\right)g(d') = (g \ast f)(n).$$

결합성은 양변을 약수 셋에 걸친 대칭적 삼중합으로 펼치면 드러난다:

$$\begin{aligned}
\bigl((f \ast g)\ast h\bigr)(n) &= \sum_{d \mid n}\Bigl(\sum_{e \mid d} f(e)\,g\!\left(\tfrac{d}{e}\right)\Bigr) h\!\left(\frac{n}{d}\right) \\
&= \sum_{abc = n} f(a)\,g(b)\,h(c) \\
&= \sum_{d \mid n} f\!\left(\frac{n}{d}\right)\Bigl(\sum_{e \mid d} g(e)\,h\!\left(\tfrac{d}{e}\right)\Bigr) = \bigl(f \ast (g \ast h)\bigr)(n),
\end{aligned}$$

여기서 가운데 합은 $$abc = n$$을 만족하는 양의 정수 순서쌍 $$(a, b, c)$$ 전체에 걸친 것이다. 끝으로 $$\varepsilon$$은 $$d = n$$인 항만 살아남으므로 $$(f \ast \varepsilon)(n) = \sum_{d \mid n} f(d)\,\varepsilon(n/d) = f(n)$$이다.

</details>

명제 8에 의해 $$f(1) \neq 0$$인 산술적 함수는 합성곱에 대한 역원을 가진다. 역원 $$f^{-1}$$은 $$f^{-1}(1) = 1/f(1)$$로 시작해

$$f^{-1}(n) = -\frac{1}{f(1)}\sum_{\substack{d \mid n \\ d < n}} f\!\left(\frac{n}{d}\right) f^{-1}(d)$$

라는 점화식으로 차례차례 결정된다. 명제 5의 $$\mathbf{1}\ast\mu = \varepsilon$$은 정확히 $$\mathbf{1}$$의 역원이 $$\mu$$라는 진술이며, 이렇게 보면 뫼비우스 반전은 "$$\mathbf{1}$$로 곱한 것을 $$\mu$$로 나누어 되돌린다"는 군 이론적 상투구의 한 사례에 지나지 않는다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 산술적 함수 $$f, g$$가 모두 곱셈적이면 $$f \ast g$$도 곱셈적이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gcd(m, n) = 1$$이라 하자. $$mn$$의 각 약수 $$d$$는 $$d = ab$$ ($$a \mid m$$, $$b \mid n$$) 로 유일하게 쪼개지며, 이때 $$\gcd(a, b) = 1$$이고 $$\gcd(m/a,\, n/b) = 1$$이다. 곱셈성을 두 번 써서

$$\begin{aligned}
(f \ast g)(mn) &= \sum_{d \mid mn} f(d)\,g\!\left(\frac{mn}{d}\right) = \sum_{a \mid m}\sum_{b \mid n} f(ab)\,g\!\left(\frac{m}{a}\cdot\frac{n}{b}\right) \\
&= \sum_{a \mid m}\sum_{b \mid n} f(a)f(b)\,g\!\left(\frac{m}{a}\right) g\!\left(\frac{n}{b}\right) \\
&= \Bigl(\sum_{a \mid m} f(a)\,g\!\left(\tfrac{m}{a}\right)\Bigr)\Bigl(\sum_{b \mid n} f(b)\,g\!\left(\tfrac{n}{b}\right)\Bigr) = (f \ast g)(m)\,(f \ast g)(n)
\end{aligned}$$

이다. 또 $$f, g$$가 항등적으로 $$0$$이 아니므로 $$(f\ast g)(1) = f(1)g(1) = 1 \neq 0$$이어서 $$f \ast g$$는 항등적 $$0$$이 아니다. 따라서 곱셈적이다.

</details>

명제 9는 곱셈적 함수가 합성곱 아래 닫혀 있음을 말한다. $$\mathbf{1}$$과 $$\mathrm{id}$$가 곱셈적이므로 $$\tau = \mathbf{1}\ast\mathbf{1}$$과 $$\sigma = \mathbf{1}\ast\mathrm{id}$$이 곱셈적임이 예시 2와 별개로 곧장 따라 나오고, $$\mathbf{1}$$의 역원 $$\mu$$ 역시 곱셈적임을 같은 틀에서 재확인할 수 있다. 더 일반적으로 $$\mathrm{id}_k(n) = n^k$$로 두면 $$\sigma_k = \mathbf{1}\ast\mathrm{id}_k$$, 즉 $$\sigma_k(n) = \sum_{d \mid n} d^k$$이 곱셈적이며, $$k = 0$$이면 $$\tau$$, $$k = 1$$이면 $$\sigma$$가 된다.

## 예시와 계산

추상적 항등식이 구체적인 수에서 어떻게 작동하는지 살펴본다. 먼저 한 정수를 정해 여러 산술적 함수의 값을 곱공식으로 한꺼번에 계산한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$n = 360 = 2^3 \cdot 3^2 \cdot 5$$에 대해 곱셈성을 이용하면

$$\begin{aligned}
\tau(360) &= (3+1)(2+1)(1+1) = 4\cdot 3\cdot 2 = 24, \\
\sigma(360) &= \frac{2^4 - 1}{2-1}\cdot\frac{3^3 - 1}{3-1}\cdot\frac{5^2 - 1}{5-1} = 15\cdot 13\cdot 6 = 1170, \\
\varphi(360) &= 360\Bigl(1 - \tfrac12\Bigr)\Bigl(1 - \tfrac13\Bigr)\Bigl(1 - \tfrac15\Bigr) = 360\cdot\frac12\cdot\frac23\cdot\frac45 = 96
\end{aligned}$$

이다. $$360$$이 어떤 소수의 제곱으로 나누어떨어지므로 $$\mu(360) = 0$$이고, 약수에 걸친 합 $$\sum_{d \mid 360}\varphi(d) = 360$$ (예시 7) 역시 곱셈성으로 인수마다 $$\sum_{j}\varphi(p^j) = p^e$$임을 확인하면 즉시 따라온다.

</div>

다음으로 뫼비우스 반전을 적용해 약수합으로 정의된 함수를 풀어내는 전형적인 계산을 본다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$g(n) = \sum_{d \mid n} \tau(d)$$로 정의된 함수를 $$\tau$$로 되돌려 보자. 정의에 따라 $$g = \mathbf{1}\ast\tau = \mathbf{1}\ast\mathbf{1}\ast\mathbf{1}$$이므로 $$g$$는 곱셈적이고 소수 거듭제곱에서

$$g(p^e) = \sum_{j=0}^{e}\tau(p^j) = \sum_{j=0}^{e}(j+1) = \frac{(e+1)(e+2)}{2} = \binom{e+2}{2}$$

이다. 뫼비우스 반전 $$\tau = \mu \ast g$$를 명시적으로 적으면

$$\tau(n) = \sum_{d \mid n}\mu(d)\,g\!\left(\frac{n}{d}\right)$$

이고, 가령 $$n = p^2$$에서 $$\mu(1)g(p^2) + \mu(p)g(p) = 6 - 3 = 3 = \tau(p^2)$$로 좌우가 맞아떨어진다.

</div>

마지막으로 부분합을 직접 합산해 뫼비우스 함수의 상쇄 효과를 관찰한다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> *메르텐스 함수<sub>Mertens function</sub>* $$M(n) = \sum_{k=1}^{n}\mu(k)$$의 처음 값들을 명제 5의 곱셈성과 정의 4로 계산하면

$$\mu(1),\dots,\mu(10) = 1,\,-1,\,-1,\,0,\,-1,\,1,\,-1,\,0,\,0,\,1$$

이므로 누적합은

$$M(1),\dots,M(10) = 1,\,0,\,-1,\,-1,\,-2,\,-1,\,-2,\,-2,\,-2,\,-1$$

이다. $$\mu$$의 값이 $$\pm 1$$ 사이에서 비정칙하게 진동하여 $$M(n)$$이 $$n$$에 비해 매우 느리게 자란다는 사실은 소수 정리와 동치인 깊은 진술 $$M(n) = o(n)$$으로 정식화되며, 더 강한 $$M(n) = O(n^{1/2+\epsilon})$$ 여부는 리만 가설과 맞닿아 있다.

</div>

이 예시들은 곱셈성·합성곱·반전이라는 세 도구가 어떻게 맞물려 한 함수의 값을 다른 함수의 값으로 번역하는지를 보여 준다.

곱셈적 함수와 디리클레 합성곱은 소수의 분포를 함수의 언어로 다루는 해석적 정수론의 대수적 골격을 이룬다. 이들을 생성함수 $$\sum_n f(n) n^{-s}$$로 부호화한 디리클레 급수는 리만 제타 함수와 만나며, 그 해석적 성질은 [§소수의 무한성과 분포, ⁋참고 3](/ko/math/number_theory/distribution_of_primes#rmk3)에서 언급한 소수 정리로 이어진다.
