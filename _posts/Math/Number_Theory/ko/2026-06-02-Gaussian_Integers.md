---
title: "가우스 정수와 두 제곱수의 합"
description: "정수에 √-1을 더한 가우스 정수환을 도입하고, 노름을 이용해 그것이 유클리드 정역, 따라서 유일인수분해환임을 보인다. 이를 이차 잉여 이론과 결합하여 어떤 소수가 두 제곱수의 합인지를 결정한다."
excerpt: "가우스 정수, 노름과 유클리드 나눗셈, 두 제곱수의 합 정리"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/gaussian_integers
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
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

여기서 $$p = 2 = 1^2 + 1^2$$은 특별하다. $$2 = -i(1+i)^2$$이므로 $$2$$의 노름 $$N(1+i) = 2$$인 인수 $$1+i$$가 단원을 곱한 차이로 자기 켤레와 같아지는, 이른바 *분기<sub>ramification</sub>*가 일어나는 유일한 소수이다. 이제 이러한 거동을 모든 소수에 대해 분류하여 $$\mathbb{Z}[i]$$의 소수(가우스 소수)가 무엇인지 완전히 기술하자.

## 가우스 소수의 분류

정리 4의 증명은 홀수 소수 $$p$$의 $$\mathbb{Z}[i]$$에서의 거동이 $$p \bmod 4$$에 따라 둘로 갈림을 보였다. $$p \equiv 1$$이면 $$p = \pi\overline{\pi}$$로 쪼개지고, $$p \equiv 3$$이면 쪼개지지 않는다. 이를 노름을 길잡이로 하나의 명제로 모은다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (가우스 소수의 분류)**</ins> 단원을 무시하면 $$\mathbb{Z}[i]$$의 소수는 정확히 다음 셋으로 나뉜다.

1. $$1 + i$$ (노름 $$2$$). 여기서 $$2 = -i(1+i)^2$$이다.
2. 유리소수 $$p \equiv 3 \pmod 4$$ (노름 $$p^2$$). 이들은 $$\mathbb{Z}[i]$$에서도 소수로 남는다.
3. $$p \equiv 1 \pmod 4$$인 각 $$p$$에 대해 $$p = \pi\overline{\pi}$$로 나타나는 켤레쌍 $$\pi, \overline{\pi}$$ (노름 $$p$$). 서로 단원배가 아니다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\pi \in \mathbb{Z}[i]$$가 비단원 소수라 하자. $$N(\pi) = \pi\overline{\pi}$$는 $$1$$보다 큰 정수이므로 어떤 유리소수 $$p$$로 나뉜다. 그러면

$$\begin{aligned}
\pi \mid \pi\overline{\pi} = N(\pi), \qquad p \mid N(\pi)
\end{aligned}$$

에서 $$\pi$$가 정수 $$N(\pi)$$를 나누고 그 정수가 $$p$$를 인수로 가지므로, $$\pi$$는 어떤 유리소수 $$p$$를 나눈다 (만약 $$\pi$$가 서로 다른 두 유리소수 $$p, q$$를 모두 나누면 $$\gcd(p,q)=1$$의 Bézout 표현으로 $$\pi \mid 1$$이 되어 모순이므로, 그러한 $$p$$는 유일하다). 따라서 모든 가우스 소수는 정확히 하나의 유리소수를 나누며, 각 유리소수가 $$\mathbb{Z}[i]$$에서 어떻게 쪼개지는지를 보면 충분하다.

$$p = 2$$이면 $$2 = (1+i)(1-i) = -i(1+i)^2$$이고 $$N(1+i) = 2$$는 소수이므로 $$1+i$$는 가우스 소수이며, $$1 - i = -i(1+i)$$는 그 단원배이다. $$p \equiv 3 \pmod 4$$이면 정리 4에서 보았듯 $$p$$는 두 제곱수의 합이 아니어서 $$N(\pi) = p$$인 $$\pi$$가 없고, 만약 $$p = \alpha\beta$$가 비단원 분해라면 $$p^2 = N(\alpha)N(\beta)$$에서 $$N(\alpha) = p$$가 강제되어 모순이므로 $$p$$ 자체가 가우스 소수이다 (노름 $$p^2$$). $$p \equiv 1 \pmod 4$$이면 정리 4에서 $$p = \pi\overline{\pi}$$, $$N(\pi) = p$$이고, $$N(\pi)$$가 소수이므로 $$\pi$$는 가우스 소수이다. 끝으로 $$\pi$$와 $$\overline{\pi}$$가 단원배가 아님을 본다. $$\pi = a + bi$$ ($$a^2 + b^2 = p$$) 라 두고 $$\overline{\pi} = u\pi$$인 단원 $$u \in \{1, -1, i, -i\}$$가 있다고 가정하자. $$u = \pm 1$$이면 $$a - bi = \pm(a + bi)$$에서 $$b = 0$$ 또는 $$a = 0$$이 되어 $$p = a^2$$ 또는 $$p = b^2$$이 완전제곱수가 되고, $$u = \pm i$$이면 $$a = \mp b$$가 되어 $$p = a^2 + b^2 = 2a^2$$이 짝수가 된다. 어느 경우도 홀수 소수 $$p$$에 대해서는 성립할 수 없으므로, 둘은 단원배가 아니다.

</details>

이 분류로 임의의 가우스 정수의 소인수분해를 노름을 단서 삼아 실제로 계산할 수 있다. 노름이 곱셈적이므로, $$\alpha$$를 인수분해하려면 먼저 정수 $$N(\alpha)$$를 인수분해하고 각 유리소인수에 대응하는 가우스 소수를 골라내면 된다.

## 예시와 계산

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (가우스 정수의 소인수분해)**</ins> $$\alpha = 3 + i$$를 인수분해하자. 노름은

$$N(3 + i) = 3^2 + 1^2 = 10 = 2 \cdot 5$$

이다. $$2$$는 $$1 + i$$에서, $$5 = (2+i)(2-i)$$는 $$2 \pm i$$에서 온다. 따라서 $$\alpha$$는 노름 $$2$$인 소수 하나와 노름 $$5$$인 소수 하나의 곱이어야 한다. $$\dfrac{3+i}{1+i} = \dfrac{(3+i)(1-i)}{2} = \dfrac{4 - 2i}{2} = 2 - i$$이므로

$$3 + i = (1 + i)(2 - i)$$

이고, 우변의 두 인수는 각각 노름 $$2, 5$$인 가우스 소수이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (유클리드 나눗셈)**</ins> 정리 3의 알고리즘을 $$\alpha = 11 + 7i$$, $$\beta = 3 + 2i$$에 실행하자. 먼저

$$\frac{\alpha}{\beta} = \frac{(11 + 7i)(3 - 2i)}{N(\beta)} = \frac{(33 + 14) + (21 - 22)i}{13} = \frac{47 - i}{13} \approx 3.62 - 0.08\,i$$

이다. 가장 가까운 가우스 정수는 $$\kappa = 4$$ (실수부 $$3.62 \to 4$$, 허수부 $$-0.08 \to 0$$) 이며, 나머지는

$$\rho = \alpha - \beta\kappa = (11 + 7i) - 4(3 + 2i) = -1 - i$$

이다. $$N(\rho) = 2 < 13 = N(\beta)$$로 나머지의 노름이 줄어들어 나눗셈 정리가 확인된다.

</div>

이러한 나눗셈을 반복하면 두 가우스 정수의 최대공약수를 호제법으로 구할 수 있다 ([§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)의 논증이 그대로 옮겨진다). 노름이 매 단계 진감소하는 양의 정수이므로 알고리즘은 유한 번에 끝난다.

## 일반 정수의 두 제곱수 표현

정리 4는 소수에 관한 것이지만, 노름의 곱셈성과 가우스 소수의 분류를 결합하면 임의의 양의 정수에 대한 완전한 판정이 따라 나온다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (두 제곱수의 합 판정법)**</ins> 양의 정수 $$n$$이 두 제곱수의 합인 것은, $$n$$의 소인수분해에서 $$p \equiv 3 \pmod 4$$인 모든 소수 $$p$$가 짝수 번 나타나는 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$n = x^2 + y^2$$인 것은 $$n = N(\alpha)$$인 $$\alpha = x + yi \in \mathbb{Z}[i]$$가 존재하는 것과 같다. $$\alpha$$를 가우스 소수들로 인수분해하고 노름을 취하면, $$n$$은 가우스 소수들의 노름의 곱이다. 정리 5에 의해 그 노름들은 $$2$$, $$p \equiv 1$$인 $$p$$, 또는 $$p \equiv 3$$인 $$p^2$$ 중 하나이다. 따라서

$$\begin{aligned}
n = N(\alpha) &= 2^{a}\prod_{p \equiv 1} p^{b_p} \prod_{p \equiv 3} (p^2)^{c_p}
\end{aligned}$$

꼴이 되어, $$p \equiv 3$$인 소수는 모두 짝수 지수로만 나타난다. 역으로 $$n = 2^a \prod_{p\equiv 1} p^{b_p}\prod_{p\equiv 3} p^{2c_p}$$이면, $$2 = N(1+i)$$, $$p = N(\pi_p)$$ ($$p \equiv 1$$), $$p^2 = N(p)$$ ($$p \equiv 3$$) 이므로 각 인수가 어떤 가우스 정수의 노름이고, 노름이 곱셈적이므로 그 곱 $$n$$도 노름, 곧 두 제곱수의 합이다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (판정법의 적용)**</ins> $$45 = 3^2 \cdot 5$$에서 $$3 \equiv 3 \pmod 4$$는 짝수 번 나타나므로 $$45$$는 두 제곱수의 합이다. 실제로

$$45 = 6^2 + 3^2 = 36 + 9$$

이다. 반면 $$21 = 3 \cdot 7$$은 $$3, 7$$ 모두 $$4$$로 나눠 $$3$$이 남으면서 홀수 번 나타나므로 두 제곱수의 합이 아니다. 또 $$50 = 2 \cdot 5^2$$은 위배되는 소수가 없어 두 제곱수의 합이며,

$$50 = 5^2 + 5^2 = 1^2 + 7^2$$

처럼 본질적으로 다른 표현을 둘 가질 수 있다 — 이는 $$50$$이 노름 $$5$$인 켤레쌍 $$2 \pm i$$를 거듭 가지기 때문이다.

</div>

표현의 개수까지도 가우스 소인수분해가 설명한다. $$p \equiv 1 \pmod 4$$인 서로 다른 소수들의 곱 $$n = p_1 \cdots p_k$$는 각 $$p_j = \pi_j\overline{\pi_j}$$에서 켤레를 고르는 자유로 인해, 단원과 순서를 무시하면 $$2^{k-1}$$가지의 본질적으로 다른 두 제곱수 표현을 갖는다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (켤레 선택과 다중 표현)**</ins> $$65 = 5 \cdot 13$$을 보자. $$5 = (2+i)(2-i)$$, $$13 = (3+2i)(3-2i)$$이다. 한 쪽 켤레 선택은

$$(2+i)(3+2i) = 6 + 4i + 3i - 2 = 4 + 7i, \qquad N = 4^2 + 7^2 = 65,$$

다른 선택은

$$(2+i)(3-2i) = 6 - 4i + 3i + 2 = 8 - i, \qquad N = 8^2 + 1^2 = 65$$

이다. 따라서 $$65 = 4^2 + 7^2 = 1^2 + 8^2$$로 두 가지 표현을 얻으며, 이는 $$2^{2-1} = 2$$라는 셈과 일치한다.

</div>

가우스 정수는 정수환을 확장하여 산술 문제를 푸는 대수적 정수론의 첫걸음이다. 같은 방식으로 $$\mathbb{Z}[\omega]$$ ($$\omega = e^{2\pi i/3}$$, 아이젠슈타인 정수) 는 $$x^2 + xy + y^2$$ 꼴과 $$p \equiv 1 \pmod 3$$의 표현을 다루고, 더 일반의 이차체 $$\mathbb{Q}(\sqrt{d})$$의 정수환에서는 유일인수분해가 깨지기도 하여 아이디얼이 등장한다. 또 다른 확장 방향으로, 무리수를 정수의 비의 극한으로 다루어 $$\sqrt{d}$$ 꼴의 무리수와 이차 방정식의 정수해에 접근하는 [§연분수](/ko/math/number_theory/continued_fractions)와 [§펠 방정식](/ko/math/number_theory/pell_equation)이 있다.
