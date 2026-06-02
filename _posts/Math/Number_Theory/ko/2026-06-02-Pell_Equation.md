---
title: "펠 방정식"
description: "제곱수가 아닌 D에 대한 펠 방정식 x²-Dy²=1을 다룬다. 자명하지 않은 해가 항상 존재함을 연분수로부터 보이고, 기본해의 거듭제곱이 모든 해를 준다는 군 구조를 ℤ[√D]의 단원으로 설명한다."
excerpt: "펠 방정식, 기본해의 존재, 해의 군 구조"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/pell_equation
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Pell_Equation.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
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

정리 3은 펠 방정식의 해가 무한순환군 (자명한 부호를 곱하면 $$\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$$의 구조) 을 이룸을 뜻한다. 이는 실이차체 $$\mathbb{Q}(\sqrt D)$$의 정수환의 단원군에 관한 디리클레 단원정리의 가장 단순한 경우로, [§가우스 정수와 두 제곱수의 합](/ko/math/number_theory/gaussian_integers)에서 본 단원 $$\pm 1, \pm i$$가 유한했던 것과 대비된다. 두 글은 함께 대수적 정수론으로 들어가는 두 문 — 허이차체와 실이차체 — 을 보여 준다.
