---
title: "가우스 정수와 두 제곱수의 합"
description: "정수에 √-1을 더한 가우스 정수환을 도입하고, 노름을 이용해 그것이 유클리드 정역, 따라서 유일인수분해환임을 보인다. 이를 이차 잉여 이론과 결합하여 어떤 소수가 두 제곱수의 합인지를 결정한다."
excerpt: "가우스 정수, 노름과 유클리드 나눗셈, 두 제곱수의 합 정리"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/gaussian_integers
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Gaussian_Integers.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 14

published: false
---

어떤 소수가 두 제곱수의 합 $$p = x^2 + y^2$$으로 쓰이는가? 이 정수론의 고전적 물음은 정수환을 $$x^2 + y^2 = (x+yi)(x-yi)$$로 인수분해되는 더 큰 환으로 확장할 때 가장 자연스럽게 풀린다.

## 가우스 정수와 노름

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *가우스 정수<sub>Gaussian integer</sub>*는 $$a + bi$$ ($$a, b \in \mathbb{Z}$$, $$i^2 = -1$$) 꼴의 복소수이며, 그 전체를 $$\mathbb{Z}[i]$$로 적는다. $$\alpha = a + bi$$의 *노름<sub>norm</sub>*을 $$N(\alpha) = a^2 + b^2$$으로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 노름은 곱셈적이다: $$N(\alpha\beta) = N(\alpha)N(\beta)$$. 따라서 $$\alpha$$가 $$\mathbb{Z}[i]$$의 가역원(단원)인 것은 $$N(\alpha) = 1$$인 것과 동치이며, 단원은 $$\pm 1, \pm i$$의 넷뿐이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$N(\alpha) = \alpha\overline{\alpha}$$ ($$\overline{\alpha}$$는 켤레) 이므로 $$N(\alpha\beta) = \alpha\beta\overline{\alpha\beta} = \alpha\overline{\alpha}\,\beta\overline{\beta} = N(\alpha)N(\beta)$$이다. $$\alpha\beta = 1$$이면 $$N(\alpha)N(\beta) = 1$$이고 노름은 양의 정수이므로 $$N(\alpha) = 1$$, 즉 $$a^2 + b^2 = 1$$이어서 $$\alpha \in \{\pm 1, \pm i\}$$이다. 역으로 이 넷은 모두 가역이다.

</details>

## 유클리드 나눗셈과 유일인수분해

$$\mathbb{Z}$$에서와 마찬가지로 노름을 "크기"로 삼아 나눗셈 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$\mathbb{Z}[i]$$는 유클리드 정역이다. 즉 임의의 $$\alpha, \beta \in \mathbb{Z}[i]$$ ($$\beta \neq 0$$) 에 대하여 $$\alpha = \beta\kappa + \rho$$이면서 $$N(\rho) < N(\beta)$$인 $$\kappa, \rho$$가 존재한다. 따라서 $$\mathbb{Z}[i]$$에서는 소인수분해가 단원을 무시하면 유일하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

복소수 $$\alpha/\beta = u + vi$$ ($$u, v \in \mathbb{Q}$$) 에 대해 가장 가까운 정수 $$m, n$$ ($$\lvert u - m\rvert \leq \tfrac12$$, $$\lvert v - n\rvert \leq \tfrac12$$) 을 잡고 $$\kappa = m + ni$$로 두자. $$\rho = \alpha - \beta\kappa$$로 두면

$$N(\rho) = N(\beta)\,N\!\left(\frac{\alpha}{\beta} - \kappa\right) = N(\beta)\bigl((u-m)^2 + (v-n)^2\bigr) \leq N(\beta)\left(\tfrac14 + \tfrac14\right) = \tfrac12 N(\beta) < N(\beta)$$

이다. 유클리드 나눗셈이 성립하면 $$\mathbb{Z}$$에서와 똑같은 논증 ([§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm), [§소수와 산술의 기본정리](/ko/math/number_theory/primes))으로 최대공약수·Bézout·유일인수분해가 모두 따라온다.

</details>

## 두 제곱수의 합

이제 소수 $$p$$를 $$\mathbb{Z}[i]$$에서 보면, $$p = x^2 + y^2$$은 $$p = (x+yi)(x-yi)$$로 $$p$$가 $$\mathbb{Z}[i]$$에서 쪼개진다는 뜻이다. 언제 그러한지는 이차 잉여가 결정한다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (페르마의 두 제곱수 정리)**</ins> 홀수 소수 $$p$$가 두 제곱수의 합으로 쓰이는 것은 $$p \equiv 1 \pmod 4$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p \equiv 3 \pmod 4$$이면, $$x^2 + y^2 \equiv 0 \pmod p$$에서 $$p \nmid x$$라면 $$(xy^{-1})^2 \equiv -1 \pmod p$$가 되어 $$-1$$이 이차 잉여여야 하는데, $$\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2} = -1$$ ([§이차 잉여, ⁋따름정리 5](/ko/math/number_theory/quadratic_residues#cor5))이므로 불가능하다. 따라서 $$p \mid x, p\mid y$$이고 $$x^2 + y^2$$은 $$p^2$$의 배수가 되어 $$p$$와 같을 수 없다.

$$p \equiv 1 \pmod 4$$이면 $$\left(\frac{-1}{p}\right) = 1$$이므로 $$m^2 \equiv -1 \pmod p$$인 $$m$$이 있다. 그러면 $$p \mid m^2 + 1 = (m+i)(m-i)$$이지만, $$p$$는 $$\tfrac{m\pm i}{p} = \tfrac{m}{p} \pm \tfrac1p i \notin \mathbb{Z}[i]$$이므로 $$m + i$$도 $$m - i$$도 나누지 못한다. 즉 $$p$$는 $$\mathbb{Z}[i]$$에서 소수가 아니어서 $$p = \pi\overline{\pi}$$로 비단원 인수분해되고, 노름을 취하면 $$p^2 = N(\pi)^2$$에서 $$N(\pi) = p$$, 곧 $$\pi = x + yi$$에 대해 $$p = x^2 + y^2$$이다.

</details>

여기서 $$p = 2 = 1^2 + 1^2$$은 특별하다. 일반 정수 $$n$$이 두 제곱수의 합인지는 그 소인수분해에서 $$4$$로 나눠 $$3$$이 남는 소수들이 모두 짝수 번 나타나는지로 판정되며, 이는 정리 4와 노름의 곱셈성에서 따른다.

가우스 정수는 정수환을 확장하여 산술 문제를 푸는 대수적 정수론의 첫걸음이다. 또 다른 확장 방향으로, 무리수를 정수의 비의 극한으로 다루어 $$\sqrt{d}$$ 꼴의 무리수와 이차 방정식의 정수해에 접근하는 [§연분수](/ko/math/number_theory/continued_fractions)와 [§펠 방정식](/ko/math/number_theory/pell_equation)이 있다.
