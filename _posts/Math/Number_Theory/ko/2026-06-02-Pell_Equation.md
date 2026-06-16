---
title: "펠 방정식"
description: "제곱수가 아닌 D에 대한 펠 방정식 x²-Dy²=1을 다룬다. 자명하지 않은 해가 항상 존재함을 연분수로부터 보이고, 기본해의 거듭제곱이 모든 해를 준다는 군 구조를 ℤ[√D]의 단원으로 설명한다."
excerpt: "펠 방정식, 기본해의 존재, 해의 군 구조"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/pell_equation
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 16

published: false
---

[§연분수](/ko/math/number_theory/continued_fractions)는 무리수를 유리수로 근사하는 도구였다. 그 가장 빛나는 응용이 펠 방정식 $$x^2 - Dy^2 = 1$$의 정수해를 모두 찾는 것이다. 이 방정식은 [§가우스 정수와 두 제곱수의 합](/ko/math/number_theory/gaussian_integers)에서 본 노름의 산술과 깊이 연결된다.

## 펠 방정식과 노름

이 글에서 $$D$$는 제곱수가 아닌 양의 정수로 둔다 ($$D$$가 제곱수이면 방정식은 자명한 해뿐이다).

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 방정식 $$x^2 - Dy^2 = 1$$을 *펠 방정식<sub>Pell's equation</sub>*이라 한다. $$x = \pm 1, y = 0$$인 해를 *자명한 해*라 한다.

</div>

수 $$\alpha = x + y\sqrt{D}$$ ($$x, y \in \mathbb{Z}$$) 들이 이루는 환 $$\mathbb{Z}[\sqrt D]$$에서 *노름*을 $$N(\alpha) = (x + y\sqrt D)(x - y\sqrt D) = x^2 - Dy^2$$으로 정의하면, 펠 방정식의 해는 정확히 $$N(\alpha) = 1$$인 원소이다. 노름은 곱셈적이므로 — $$N(\alpha\beta) = N(\alpha)N(\beta)$$ — 해들의 곱도 다시 해이다. 이것이 해의 구조를 지배한다.

## 기본해의 존재

핵심은 자명하지 않은 해가 반드시 존재한다는 사실이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> 제곱수가 아닌 $$D$$에 대하여 펠 방정식은 자명하지 않은 해를 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명 (개요)</summary>

연분수 근사 ([§연분수, ⁋정리 3](/ko/math/number_theory/continued_fractions#thm3))에 의해 $$\left\lvert \sqrt D - \dfrac{p}{q}\right\rvert < \dfrac{1}{q^2}$$인 유리수가 무한히 많다. 이런 $$p, q$$에 대해 $$\lvert p^2 - Dq^2\rvert = \lvert p - q\sqrt D\rvert\,\lvert p + q\sqrt D\rvert < \dfrac1q\cdot(2q\sqrt D + 1)$$이 유계이므로, $$p^2 - Dq^2$$이 같은 값 $$k$$를 갖는 해가 무한히 많다. 그중 $$p, q$$가 법 $$\lvert k\rvert$$에 대해 같은 잉여류인 두 해 $$\alpha_1, \alpha_2$$를 고르면, 비 $$\alpha_1/\alpha_2$$가 노름 $$1$$인 자명하지 않은 정수해 $$\mathbb{Z}[\sqrt D]$$의 원소를 준다. 실제로 $$\sqrt D$$의 순환연분수의 한 주기에서 나오는 점근분수가 기본해를 직접 산출한다.

</details>

자명하지 않은 양의 해 중 $$x + y\sqrt D$$가 가장 작은 것을 *기본해<sub>fundamental solution</sub>* $$\varepsilon_1 = x_1 + y_1\sqrt D$$라 한다.

## 모든 해의 구조

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$\varepsilon_1 = x_1 + y_1\sqrt D$$을 기본해라 하면, $$x^2 - Dy^2 = 1$$의 모든 양의 해 $$x_n + y_n\sqrt D$$은

$$x_n + y_n\sqrt D = (x_1 + y_1\sqrt D)^n \qquad (n = 1, 2, 3, \ldots)$$

으로 정확히 한 번씩 주어진다. 부호와 $$y$$의 부호까지 포함하면 모든 해는 $$\pm \varepsilon_1^{\,n}$$ ($$n \in \mathbb{Z}$$) 이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

노름의 곱셈성으로 $$N(\varepsilon_1^n) = N(\varepsilon_1)^n = 1$$이므로 각 $$\varepsilon_1^n$$은 해이다. 거꾸로 $$\beta = x + y\sqrt D > 1$$이 어떤 해인데 $$\varepsilon_1^n$$ 꼴이 아니라면, $$\varepsilon_1^n \leq \beta < \varepsilon_1^{n+1}$$인 $$n$$을 잡을 수 있고 $$1 \leq \beta\varepsilon_1^{-n} < \varepsilon_1$$이다. $$\beta\varepsilon_1^{-n}$$도 노름 $$1$$의 해인데 $$1$$보다 작은 자명하지 않은 해가 되어 기본해의 최소성에 모순이다 (또는 $$1$$이어서 $$\beta = \varepsilon_1^n$$). 따라서 모든 양의 해가 거듭제곱으로 소진된다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$D = 2$$이면 $$\sqrt 2 = [1; \overline{2}]$$의 점근분수 $$3/2$$에서 기본해 $$\varepsilon_1 = 3 + 2\sqrt2$$ ($$3^2 - 2\cdot 2^2 = 1$$) 을 얻는다. 거듭제곱하면 $$\varepsilon_1^2 = 17 + 12\sqrt2$$ ($$17^2 - 2\cdot 12^2 = 1$$), $$\varepsilon_1^3 = 99 + 70\sqrt2$$로 해가 줄줄이 나온다.

</div>

## 해의 점화식

정리 3은 모든 해를 기본해의 거듭제곱으로 기술하지만, 실제 계산에서는 거듭제곱을 직접 펼치기보다 이웃한 해를 잇는 점화식을 쓰는 편이 편리하다. 곱셈 $$\varepsilon_1^{n+1} = \varepsilon_1 \cdot \varepsilon_1^{n}$$을 좌표로 풀어 쓰면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 기본해를 $$\varepsilon_1 = x_1 + y_1\sqrt D$$, $$n$$번째 양의 해를 $$x_n + y_n\sqrt D = \varepsilon_1^{\,n}$$이라 하면

$$x_{n+1} = x_1 x_n + D\,y_1 y_n, \qquad y_{n+1} = x_1 y_n + y_1 x_n$$

이 성립한다. 특히 $$x_n, y_n$$은 모두 정수이고 $$n$$에 대해 단조증가한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varepsilon_1^{\,n+1} = (x_1 + y_1\sqrt D)(x_n + y_n\sqrt D)$$을 전개하면

$$\begin{aligned}
\varepsilon_1^{\,n+1} &= x_1 x_n + x_1 y_n\sqrt D + y_1 x_n\sqrt D + y_1 y_n\,(\sqrt D)^2 \\
&= (x_1 x_n + D\,y_1 y_n) + (x_1 y_n + y_1 x_n)\sqrt D
\end{aligned}$$

이다. $$\sqrt D$$가 무리수이므로 $$\{1, \sqrt D\}$$는 $$\mathbb{Q}$$ 위에서 일차독립이고, 따라서 유리수 계수의 비교가 정당하다. 좌변을 $$x_{n+1} + y_{n+1}\sqrt D$$로 적어 두 계수를 견주면 주장하는 두 식을 얻는다. $$x_1, y_1 \geq 1$$이고 $$D \geq 2$$이므로 모든 항이 양이어서 $$x_{n+1} > x_n$$, $$y_{n+1} > y_n$$이 따른다.

</details>

이 점화식은 $$2 \times 2$$ 행렬의 거듭제곱으로도 읽을 수 있다. 명제 5의 두 식을 한데 묶으면

$$\begin{pmatrix} x_{n+1} \\ y_{n+1} \end{pmatrix} = \begin{pmatrix} x_1 & D\,y_1 \\ y_1 & x_1 \end{pmatrix} \begin{pmatrix} x_n \\ y_n \end{pmatrix}$$

이므로, 해의 열은 행렬 $$M = \left(\begin{smallmatrix} x_1 & D y_1 \\ y_1 & x_1 \end{smallmatrix}\right)$$의 거듭제곱을 초기벡터 $$(x_1, y_1)^{\mathsf T}$$에 작용시켜 얻는다. $$\det M = x_1^2 - D y_1^2 = 1$$이라 $$M \in \mathrm{SL}_2(\mathbb{Z})$$이며, 펠 방정식의 군 구조가 이 행렬군 안에 자연스럽게 들어앉음을 보여 준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$D = 2$$의 기본해 $$\varepsilon_1 = 3 + 2\sqrt2$$에 명제 5를 적용하면 $$x_{n+1} = 3x_n + 4y_n$$, $$y_{n+1} = 3y_n + 2x_n$$이다. $$(x_1, y_1) = (3, 2)$$에서 출발하면

$$\begin{aligned}
(x_2, y_2) &= (3\cdot 3 + 4\cdot 2,\ 3\cdot 2 + 2\cdot 3) = (17, 12), \\
(x_3, y_3) &= (3\cdot 17 + 4\cdot 12,\ 3\cdot 12 + 2\cdot 17) = (99, 70), \\
(x_4, y_4) &= (3\cdot 99 + 4\cdot 70,\ 3\cdot 70 + 2\cdot 99) = (577, 408)
\end{aligned}$$

로 거듭제곱을 펼치지 않고도 해가 줄줄이 나온다. $$577^2 - 2\cdot 408^2 = 332929 - 332928 = 1$$로 확인된다.

</div>

## 기본해의 크기

작은 $$D$$에 대해서는 기본해를 손으로 어렵지 않게 찾을 수 있다. 그러나 기본해의 크기는 $$D$$에 대해 결코 단조롭지 않고, 어떤 $$D$$에서는 폭발적으로 커진다는 점이 펠 방정식 특유의 묘미이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 작은 비제곱 $$D$$에 대한 기본해 $$(x_1, y_1)$$을 나열하면

$$\begin{aligned}
D = 2:&\ (3, 2), \qquad D = 3:\ (2, 1), \qquad D = 5:\ (9, 4), \\
D = 6:&\ (5, 2), \qquad D = 7:\ (8, 3), \qquad D = 8:\ (3, 1), \\
D = 13:&\ (649, 180), \qquad D = 61:\ (1766319049,\ 226153980)
\end{aligned}$$

이다. $$D = 60$$이 $$(31, 4)$$로 작은 데 비해 바로 옆 $$D = 61$$의 기본해가 십억 자리로 치솟는 것이 단조성의 결여를 극명하게 보여 준다.

</div>

$$D = 61$$의 사례는 인도 수학자 바스카라 2세와 브라마굽타가 이미 다루었고, 17세기에 페르마가 이를 도전 문제로 제시한 일화로 유명하다. 기본해가 이처럼 거대해질 수 있다는 사실은, 단지 작은 정수를 대입해 보는 방식으로는 펠 방정식이 풀리지 않으며 연분수 같은 구조적 도구가 필수임을 말해 준다. 점근분수의 분모 $$q_k$$는 기하급수적으로 증가하므로, 한 주기 안에서 노름 $$1$$을 처음 내는 점근분수까지의 단계 수만큼만 계산하면 거대한 기본해도 효율적으로 산출된다.

## 음의 펠 방정식

노름이 $$-1$$인 방정식 $$x^2 - Dy^2 = -1$$은 *음의 펠 방정식<sub>negative Pell equation</sub>*이라 불리며, 보통의 펠 방정식과 달리 항상 풀리지는 않는다. 그 해법 가능성은 $$\sqrt D$$ 연분수의 주기 길이의 홀짝성에 달려 있다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$x^2 - Dy^2 = -1$$이 정수해를 가지면 $$D$$는 두 제곱수의 합으로 표현되며, 특히 $$4$$로 나눈 나머지가 $$3$$인 소인수를 갖지 않는다. 따라서 $$D \equiv 3 \pmod 4$$이거나 $$D$$가 그런 소인수를 가지면 음의 펠 방정식은 풀리지 않는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x^2 - Dy^2 = -1$$이면 $$x^2 + 1 = D y^2$$이다. $$p \mid D$$인 홀소수 $$p$$를 잡으면 $$p \mid x^2 + 1$$, 곧 $$x^2 \equiv -1 \pmod p$$이므로 $$-1$$이 법 $$p$$의 이차잉여이다. 오일러 판정법 ([§가우스 정수와 두 제곱수의 합](/ko/math/number_theory/gaussian_integers)에서 본 사실) 에 의해 이는 $$p \equiv 1 \pmod 4$$와 동치이다. 또 $$x$$는 홀수여야 하는데, 만약 $$x$$가 짝수이면 $$x^2 + 1$$이 홀수이고 $$D y^2$$도 홀수여야 하므로 $$D$$와 $$y$$가 모두 홀수가 되어 $$x^2 - Dy^2 \equiv -y^2 \equiv 3 \pmod 4$$ ($$y$$ 홀수일 때) 등으로 $$-1 \pmod 4$$과의 정합성을 따져 보면 $$D \not\equiv 3 \pmod 4$$가 강제된다. 종합하면 $$D$$의 모든 홀소인수가 $$1 \pmod 4$$이고 $$D \not\equiv 3 \pmod 4$$여서, 두 제곱수의 합 정리에 의해 $$D$$는 두 제곱수의 합이다.

</details>

위 조건은 필요조건일 뿐 충분조건은 아니다. 가령 $$D = 34 = 25 + 9$$는 두 제곱수의 합이고 모든 홀소인수($$2$$와 $$17$$)가 적격이지만, $$x^2 - 34 y^2 = -1$$은 해가 없다. 정확한 판정은 $$\sqrt D$$ 연분수의 최소 주기 길이 $$\ell$$이 홀수일 때 음의 펠 방정식이 풀리고 짝수이면 풀리지 않는다는 것이며, 풀리는 경우 기본해 $$\varepsilon_1$$ 자체가 노름 $$-1$$을 갖고 $$\varepsilon_1^2$$이 노름 $$1$$ 펠 방정식의 기본해가 된다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$D = 2$$에서 $$x^2 - 2y^2 = -1$$은 $$(x, y) = (1, 1)$$로 풀린다 ($$1 - 2 = -1$$). 이때 $$\eta = 1 + \sqrt2$$는 노름 $$-1$$의 단원이고

$$\eta^2 = (1 + \sqrt2)^2 = 3 + 2\sqrt2 = \varepsilon_1$$

로, 그 제곱이 정확히 예시 4의 노름 $$1$$ 기본해를 준다. 한편 $$D = 3$$에서는 $$\sqrt3 = [1; \overline{1, 2}]$$의 주기가 $$2$$로 짝수여서 $$x^2 - 3y^2 = -1$$은 해가 없다. 실제로 임의의 정수에 대해 $$x^2 - 3y^2 \equiv x^2 + y^2 \pmod 3$$이 $$2$$가 될 수 없어 $$-1 \equiv 2 \pmod 3$$과 모순이다.

</div>

## 응용

펠 방정식은 순수한 호기심의 대상에 그치지 않고 여러 고전적 문제에서 자연스럽게 출현한다. 두 가지 전형적인 예를 살펴본다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (삼각수이면서 제곱수)**</ins> $$T_m = \tfrac{m(m+1)}2$$를 $$m$$번째 *삼각수<sub>triangular number</sub>*라 한다. $$T_m = k^2$$인 $$m, k$$를 찾는 문제는 펠 방정식으로 환원된다. 양변에 $$8$$을 곱해 정리하면

$$8 T_m + 1 = 4m^2 + 4m + 1 = (2m+1)^2$$

이므로 $$T_m = k^2$$은 $$(2m+1)^2 - 8k^2 = 1$$과 동치이다. 여기서 $$x = 2m+1$$, $$y = k$$로 두면 이는 $$x^2 - 8y^2 = 1$$, 곧 $$D = 8$$의 펠 방정식이다 (그 기본해는 예시 7에서 본 $$(3, 1)$$이다). 따라서 $$D = 8$$ 펠 방정식의 양의 해 $$(x, y)$$ 중 $$x$$가 홀수인 것마다 $$m = \tfrac{x-1}2$$, $$k = y$$가 하나의 삼각제곱수를 준다. 명제 5의 점화식을 $$D = 8$$, $$(x_1, y_1) = (3, 1)$$에 적용하면 $$x_{n+1} = 3x_n + 8y_n$$, $$y_{n+1} = x_n + 3y_n$$이고, $$x$$는 $$3 \to 17 \to 99 \to \cdots$$로 항상 홀수를 유지하므로

$$\begin{aligned}
(x, y) = (3, 1) &\implies (m, k) = (1, 1), \quad T_1 = 1 = 1^2, \\
(x, y) = (17, 6) &\implies (m, k) = (8, 6), \quad T_8 = 36 = 6^2, \\
(x, y) = (99, 35) &\implies (m, k) = (49, 35), \quad T_{49} = 1225 = 35^2
\end{aligned}$$

처럼 삼각수이면서 동시에 제곱수인 수가 무한히 많음을 얻는다. 여기서 등장하는 $$x$$값 $$3, 17, 99, \ldots$$이 예시 6의 $$D = 2$$ 해의 $$x$$좌표와 정확히 일치하는 것은 우연이 아니다. $$x^2 - 8y^2 = 1$$이면 $$x^2 - 2(2y)^2 = 1$$이므로 $$D = 8$$의 해 $$(x, y)$$는 곧바로 $$D = 2$$의 해 $$(x, 2y)$$를 주고, 거꾸로 $$D = 2$$의 해는 $$x^2 = 1 + 2y^2$$에서 $$x$$가 홀수, 따라서 $$y^2 = \tfrac{x^2 - 1}2$$이 짝수여서 $$y$$가 짝수임이 강제되어 $$y = 2k$$ 꼴로 되돌아온다. 두 방정식의 양의 해가 이렇게 일대일로 대응하기에 예시 6의 $$(3, 2), (17, 12), (99, 70)$$과 위의 $$(3, 1), (17, 6), (99, 35)$$이 같은 삼각제곱수를 가리킨다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 ($$\sqrt D$$의 근사)**</ins> 펠 방정식의 해는 $$\sqrt D$$의 좋은 유리근사를 직접 제공한다. $$x^2 - Dy^2 = 1$$에서

$$\frac{x}{y} - \sqrt D = \frac{x - y\sqrt D}{y} = \frac{x^2 - D y^2}{y(x + y\sqrt D)} = \frac{1}{y(x + y\sqrt D)}$$

이고, $$x + y\sqrt D > 2y\sqrt D$$이므로

$$\left\lvert \frac{x}{y} - \sqrt D \right\rvert < \frac{1}{2\sqrt D\,y^2}$$

이다. 따라서 해 $$(x_n, y_n)$$의 비 $$x_n/y_n$$은 $$\sqrt D$$로 매우 빠르게 (오차가 $$y_n^{-2}$$ 규모로) 수렴한다. $$D = 2$$의 경우 $$\tfrac32, \tfrac{17}{12}, \tfrac{99}{70}, \tfrac{577}{408}$$이 차례로 $$\sqrt2 = 1.41421356\ldots$$에 접근하며, $$\tfrac{577}{408} = 1.41421568\ldots$$은 이미 소수점 아래 다섯 자리까지 정확하다.

</div>

정리 3은 펠 방정식의 해가 무한순환군 (자명한 부호를 곱하면 $$\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$$의 구조) 을 이룸을 뜻한다. 이는 실이차체 $$\mathbb{Q}(\sqrt D)$$의 정수환의 단원군에 관한 디리클레 단원정리의 가장 단순한 경우로, [§가우스 정수와 두 제곱수의 합](/ko/math/number_theory/gaussian_integers)에서 본 단원 $$\pm 1, \pm i$$가 유한했던 것과 대비된다. 두 글은 함께 대수적 정수론으로 들어가는 두 문 — 허이차체와 실이차체 — 을 보여 준다.
