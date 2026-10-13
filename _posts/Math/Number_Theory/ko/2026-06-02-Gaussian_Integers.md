---
title: "가우스 정수와 두 제곱수의 합"
description: "가우스 정수환 ℤ[i]가 노름에 의해 Euclidean domain이 되고 따라서 unique factorization이 성립함을 보인다. 이를 바탕으로 가우스 소수를 분류하고, Fermat의 두 제곱수 정리와 임의의 양의 정수가 두 제곱수의 합이 되기 위한 필요충분조건을 증명한다."
excerpt: "가우스 정수, 노름과 나눗셈, 가우스 소수의 분류, 두 제곱수의 합"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/gaussian_integers
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 10

published: false

---

정수 $n$이 $x^2 + y^2$ 꼴로 쓰이는지를 판정하는 문제를 생각하자. 제곱수를 $4$로 나눈 나머지는 $0$ 또는 $1$이므로 $n \equiv 3 \pmod{4}$이면 $n$은 두 제곱수의 합이 될 수 없다. 그러나 이 조건은 충분하지 않다. $21 = 3 \cdot 7$은 $4$로 나눈 나머지가 $1$이지만 $21 = x^2 + y^2$의 해는 없다. 어떤 수가 두 제곱수의 합인지는 그 수의 소인수분해에 달려 있고, 이를 읽어내는 도구가 $x^2 + y^2 = (x + yi)(x - yi)$라는 인수분해이다. 우리는 이 식이 정수환 $\mathbb{Z}$를 $\mathbb{Z}[i]$로 확장한 곳에서의 소인수분해라는 점을 이용한다.

## 가우스 정수와 노름

::: 정의 1
*가우스 정수<sub>Gaussian integer</sub>*는 $a + bi$ ($a, b \in \mathbb{Z}$) 꼴의 복소수이고, 그 전체를 $\mathbb{Z}[i]$로 적는다. 복소수 $z = a + bi$의 *norm<sub>노름</sub>*을 $N(z) = z\overline{z} = a^2 + b^2$으로 정의한다.
:::

$\mathbb{Z}[i]$는 덧셈과 곱셈에 대하여 닫혀 있으므로 $\mathbb{C}$의 subring이고, 따라서 정역이다. 노름은 $\lvert z\rvert^2$과 같으므로 $z \neq 0$이면 $N(z) > 0$이고, 가우스 정수의 노름은 항상 음이 아닌 정수이다.

::: 명제 2
임의의 복소수 $z, w$에 대하여 $N(zw) = N(z)N(w)$이다. 또한 $\alpha \in \mathbb{Z}[i]$가 $\mathbb{Z}[i]$에서 곱셈 역원을 갖는 *unit<sub>단원</sub>*인 것은 $N(\alpha) = 1$인 것과 동치이며, 단원은 $1, -1, i, -i$ 넷뿐이다.
:::

::: 증명
$N(zw) = zw\overline{zw} = z\overline{z}w\overline{w}$이므로 곱셈성이 성립한다. $\alpha\beta = 1$인 $\beta \in \mathbb{Z}[i]$가 있으면 $N(\alpha)N(\beta) = 1$이고 두 노름이 양의 정수이므로 $N(\alpha) = 1$이다. 역으로 $N(\alpha) = 1$이면 $\alpha\overline{\alpha} = 1$이고 $\overline{\alpha} \in \mathbb{Z}[i]$이므로 $\alpha$는 단원이다. 끝으로 $a^2 + b^2 = 1$의 정수해는 $(\pm 1, 0), (0, \pm 1)$뿐이다.
:::

두 가우스 정수 $\alpha, \beta$에 대하여 $\alpha = u\beta$인 단원 $u$가 있으면 $\alpha$와 $\beta$는 *associate*라 한다. $\mathbb{Z}$에서 $n$과 $-n$을 같은 수로 취급하는 것과 같은 일이고, $\mathbb{Z}[i]$에서는 단원이 네 개이므로 한 원소의 associate가 네 개씩 있다. 소인수분해의 유일성은 항상 이 단원 곱의 차이를 무시한 의미이다.

## 나눗셈 정리와 unique factorization

[§나눗셈과 유클리드 호제법, ⁋정리 3](/ko/math/number_theory/euclidean_algorithm#thm3)에서 나머지의 크기를 절댓값으로 쟀듯이, $\mathbb{Z}[i]$에서는 노름으로 잰다.

::: 정리 3
$\alpha, \beta \in \mathbb{Z}[i]$이고 $\beta \neq 0$이면, $\alpha = \beta\kappa + \rho$이고 $N(\rho) < N(\beta)$인 $\kappa, \rho \in \mathbb{Z}[i]$가 존재한다.
:::

::: 증명
복소수 $\alpha/\beta = \alpha\overline{\beta}/N(\beta)$를 $u + vi$ ($u, v \in \mathbb{Q}$)로 적자. 정수 $m, n$을 각각 $u, v$에 가장 가까운 정수로 잡으면 $\lvert u - m\rvert \leq 1/2$, $\lvert v - n\rvert \leq 1/2$이다. $\kappa = m + ni$, $\rho = \alpha - \beta\kappa$로 두면 $\rho \in \mathbb{Z}[i]$이고, 노름의 곱셈성에 의하여

$$\begin{aligned}
N(\rho) &= N(\beta)N\left(\frac{\alpha}{\beta} - \kappa\right) \\
&= N(\beta)\bigl((u - m)^2 + (v - n)^2\bigr) \\
&\leq N(\beta)\left(\frac{1}{4} + \frac{1}{4}\right) = \frac{1}{2}N(\beta) < N(\beta)
\end{aligned}$$

이다.
:::

증명에서 $1/2$라는 수는 임의의 실수에서 가장 가까운 정수까지의 거리가 $1/2$을 넘지 않는다는 사실에서 나온다. 필요한 것은 두 좌표의 제곱합이 $1$보다 작은 것뿐이고, 여기서는 $1/2$로 충분히 여유가 있다. 한편 이 $\kappa, \rho$는 유일하지 않을 수 있다. $u$나 $v$가 $1/2$의 홀수 배이면 가장 가까운 정수가 둘이기 때문이고, 가령 $\alpha = 1$, $\beta = 2$이면 $\kappa \in \{0, 1\}$ 어느 쪽을 택해도 $N(\rho) = 1 < 4$이다. 나눗셈 정리가 나머지의 유일성을 주지 않는다는 점은 $\mathbb{Z}$에서와 다르다. 이는 소인수분해의 유일성에는 영향을 주지 않는다.

[정리 3](#thm3)이 성립하는 정역을 *Euclidean domain*이라 한다. $\mathbb{Z}$에서 [§소수와 산술의 기본정리, ⁋정리 4](/ko/math/number_theory/primes#thm4)를 얻을 때와 같은 경로로 $\mathbb{Z}[i]$에서도 소인수분해의 유일성이 따라온다. 이를 위해 두 개념을 구별해 둔다. 0도 단원도 아닌 $\pi \in \mathbb{Z}[i]$가 $\pi = \alpha\beta$일 때 $\alpha, \beta$ 중 하나가 반드시 단원이면 $\pi$를 *irreducible*이라 하고, $\pi \mid \alpha\beta$이면 $\pi \mid \alpha$ 또는 $\pi \mid \beta$일 때 *Gaussian prime<sub>가우스 소수</sub>*라 한다. 일반의 정역에서는 prime이면 irreducible이지만 역은 성립하지 않을 수 있다. $\mathbb{Z}[i]$에서는 두 개념이 일치한다.

::: 정리 4
$\mathbb{Z}[i]$에서 irreducible인 원소는 Gaussian prime이고, 0이 아닌 모든 비단원은 유한 개의 Gaussian prime의 곱으로 쓰인다. 이 표현은 순서와 단원 곱을 무시하면 유일하다.
:::

::: 증명
먼저 $\mathbb{Z}[i]$의 영이 아닌 ideal $I$는 한 원소로 생성됨을 보인다. $I$의 영이 아닌 원소 중 노름이 가장 작은 것을 $\delta$라 하자. 임의의 $\alpha \in I$에 대해 [정리 3](#thm3)으로 $\alpha = \delta\kappa + \rho$, $N(\rho) < N(\delta)$를 잡으면 $\rho = \alpha - \delta\kappa \in I$이다. $\delta$의 선택에 의해 $\rho = 0$이어야 하므로 $I = (\delta)$이다.

$\pi$가 irreducible이고 $\pi \mid \alpha\beta$, $\pi \nmid \alpha$라 하자. ideal $(\pi, \alpha)$를 $(\delta)$로 쓰면 $\delta \mid \pi$이므로 $\delta$는 단원이거나 $\pi$의 associate이다. 후자이면 $\pi \mid \delta \mid \alpha$가 되어 가정에 모순이므로 $\delta$는 단원이고, $1 = \pi x + \alpha y$인 $x, y \in \mathbb{Z}[i]$가 있다. 양변에 $\beta$를 곱하면 $\beta = \pi\beta x + \alpha\beta y$이고 우변은 $\pi$로 나누어떨어지므로 $\pi \mid \beta$이다. 따라서 $\pi$는 Gaussian prime이다.

분해의 존재는 노름에 대한 귀납법으로 보인다. $N(\alpha) > 1$인 $\alpha$가 irreducible이 아니면 $\alpha = \beta\gamma$로 쓰이는 비단원 $\beta, \gamma$가 있고, [명제 2](#prop2)에 의해 $N(\beta), N(\gamma) > 1$이므로 $N(\beta), N(\gamma) < N(\alpha)$이다. 귀납 가정에 의해 $\beta, \gamma$가 각각 irreducible의 곱이므로 $\alpha$도 그렇다.

유일성은 $\pi_1 \cdots \pi_r = \rho_1 \cdots \rho_s$ ($\pi_i, \rho_j$는 irreducible)에서 $r$에 대한 귀납법으로 보인다. $\pi_1$은 Gaussian prime이므로 어떤 $\rho_j$를 나누고, $\rho_j$가 irreducible이므로 $\rho_j = u\pi_1$인 단원 $u$가 있다. $\mathbb{Z}[i]$가 정역이므로 $\pi_1$을 약분하면 같은 형태의 등식이 더 짧은 길이로 남고, 귀납 가정을 적용하면 된다.
:::

이 논증이 $\mathbb{Z}[i]$에서 통하는 것은 [정리 3](#thm3)이 있기 때문이고, 노름이 비슷하게 정의되는 다른 환에서는 이 단계가 무너질 수 있다.

::: 예시 5 ($\mathbb{Z}[\sqrt{-5}]$에서의 반례)
환 $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$에서 노름 $N(a + b\sqrt{-5}) = a^2 + 5b^2$도 multiplicative이고 단원은 $\pm 1$뿐이다. 이 환에서

$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$$

이다. $a^2 + 5b^2 = 2$와 $a^2 + 5b^2 = 3$은 정수해가 없으므로 노름이 $2$ 또는 $3$인 원소가 없다. 따라서 노름이 $4, 9, 6, 6$인 $2, 3, 1 \pm \sqrt{-5}$는 비단원으로 분해될 수 없어 모두 irreducible이다. 이 네 원소는 단원 $\pm 1$을 곱해서 서로 옮겨지지 않으므로 위의 두 분해는 다른 분해이고, unique factorization이 성립하지 않는다.

[정리 3](#thm3)의 증명이 여기서 실패하는 지점은 $1/4 + 1/4$이 있던 곳이다. 이 환에서 같은 방법으로 나눗셈을 하면 $(u - m)^2 + 5(v - n)^2$의 상한은 $1/4 + 5/4 = 3/2$이어서 $1$보다 작다는 결론을 얻지 못한다. 실제로 이 환은 Euclidean domain이 아니다.
:::

## 가우스 소수의 분류

[정리 4](#thm4)에 의하여 $\mathbb{Z}[i]$의 구조는 Gaussian prime의 목록으로 결정된다. 목록은 유리소수 $p$가 $\mathbb{Z}[i]$에서 어떻게 분해되는지로 읽힌다. 모든 Gaussian prime $\pi$는 $\pi \mid \pi\overline{\pi} = N(\pi)$이므로 $N(\pi)$의 어떤 소인수 $p$를 나누고, 따라서 $\mathbb{Z}$의 소수 $p$ 각각을 $\mathbb{Z}[i]$에서 분해하면 모든 Gaussian prime이 나온다.

::: 정리 6 (가우스 소수의 분류)
단원 곱을 무시하면 $\mathbb{Z}[i]$의 Gaussian prime은 다음 셋뿐이다.

1. $1 + i$ (노름 $2$). 이때 $2 = -i(1 + i)^2$이다.
2. $q \equiv 3 \pmod{4}$인 유리소수 $q$ (노름 $q^2$).
3. $p \equiv 1 \pmod{4}$인 유리소수 $p$에 대하여 $p = \pi\overline{\pi}$를 만족하는 $\pi$와 $\overline{\pi}$ (노름 $p$). 두 원소는 associate가 아니다.
:::

::: 증명
$2 = -i(1 + i)^2$은 직접 전개하여 확인된다. $N(1 + i) = 2$이고 노름이 소수인 원소는 항상 irreducible이므로 ($\alpha\beta$로 분해되면 $N(\alpha)N(\beta)$가 소수이므로 한쪽 노름이 $1$이다) $1 + i$는 [정리 4](#thm4)에 의해 Gaussian prime이다.

$q \equiv 3 \pmod{4}$라 하자. $q = \alpha\beta$가 비단원 분해이면 $N(\alpha)N(\beta) = q^2$이고 둘 다 $1$보다 크므로 $N(\alpha) = q$이다. $\alpha = a + bi$이면 $q = a^2 + b^2$인데 제곱수는 $4$로 나눈 나머지가 $0$ 또는 $1$이므로 $a^2 + b^2 \equiv 3 \pmod{4}$는 불가능하다. 따라서 $q$는 irreducible이고, [정리 4](#thm4)에 의해 Gaussian prime이다.

$p \equiv 1 \pmod{4}$라 하자. 이 경우 $-1$이 $\bmod\ p$의 제곱수이므로 ([§이차 잉여, ⁋따름정리 5](/ko/math/number_theory/quadratic_residues#cor5)) $m^2 \equiv -1 \pmod{p}$인 정수 $m$이 있다. 그러면 $p \mid m^2 + 1 = (m + i)(m - i)$이다. 그런데 $(m \pm i)/p = m/p \pm i/p$의 허수부 $\pm 1/p$는 정수가 아니므로 $p$는 $m + i$도 $m - i$도 나누지 못한다. 따라서 $p$는 Gaussian prime이 아니고, [정리 4](#thm4)에 의해 irreducible도 아니다. $p = \alpha\beta$를 비단원 분해라 하면 $N(\alpha)N(\beta) = p^2$에서 $N(\alpha) = N(\beta) = p$이다. 노름이 소수이므로 $\alpha$는 Gaussian prime이고, $p = \alpha\overline{\alpha}$이므로 $\beta = \overline{\alpha}$이며 $\overline{\alpha}$도 노름이 $p$인 Gaussian prime이다. $\alpha = \pi$로 두자. $\overline{\pi}$가 $\pi$의 associate라고 가정하고 $\pi = a + bi$로 쓰면, $\overline{\pi} = u\pi$ ($u \in \{\pm 1, \pm i\}$)에서 $u = 1$이면 $b = 0$, $u = -1$이면 $a = 0$, $u = \pm i$이면 $a = \mp b$이다. 앞의 두 경우 $p = a^2 + b^2$은 완전제곱수이고 뒤의 경우 $p = 2a^2$이므로 홀수 소수 $p$에 모순이다.

이제 위 목록이 전부임을 보이자. $\pi'$가 임의의 Gaussian prime이면 어떤 유리소수 $p$를 나눈다. $p = 2$이면 $\pi' \mid -i(1 + i)^2$에서 $\pi' \mid 1 + i$이고, $1 + i$가 irreducible이므로 $\pi'$는 $1 + i$의 associate이다. $p \equiv 3 \pmod{4}$이면 $p = \pi'\gamma$에서 $p$가 irreducible이므로 $\gamma$가 단원이다. $p \equiv 1 \pmod{4}$이면 $\pi' \mid \pi\overline{\pi}$이므로 $\pi' \mid \pi$ 또는 $\pi' \mid \overline{\pi}$이고, 둘 다 irreducible이므로 $\pi'$는 $\pi$ 또는 $\overline{\pi}$의 associate이다.
:::

[정리 6](#thm6)은 $\mathbb{Z}[i]$에서의 소수 개념이 $\mathbb{Z}$에서와 어긋나는 지점을 정확히 알려준다. $2$는 소수가 아니고 단원 곱을 제외하고 $(1 + i)^2$이다. $5 = (2 + i)(2 - i)$, $13 = (3 + 2i)(3 - 2i)$처럼 $4k + 1$ 꼴의 소수는 서로 다른 두 Gaussian prime으로 쪼개진다. 반면 $3, 7, 11$ 같은 $4k + 3$ 꼴의 소수는 그대로 Gaussian prime으로 남는다. 노름이 소수인 원소는 항상 Gaussian prime이지만 역은 성립하지 않는다는 점도 보인다. $3$은 Gaussian prime이지만 노름이 $9$이다.

가우스 정수의 소인수분해는 이 분류를 따라 노름을 길잡이로 삼아 계산한다.

::: 예시 7 ($7 + i$의 소인수분해)
$N(7 + i) = 50 = 2 \cdot 5^2$이므로 $7 + i$는 $1 + i$ 하나와 노름이 $5$인 Gaussian prime 두 개의 곱이다. $(7 + i)/(1 + i) = (7 + i)(1 - i)/2 = (8 - 6i)/2 = 4 - 3i$이다. 노름이 $5$인 Gaussian prime은 $2 + i$와 $2 - i$ (단원 곱 제외)이고, 둘 중 어느 쪽이 약수인지는 직접 나누어 확인해야 한다. $(4 - 3i)/(2 + i) = (4 - 3i)(2 - i)/5 = (5 - 10i)/5 = 1 - 2i$는 가우스 정수이고 $1 - 2i = -i(2 + i)$이므로 $4 - 3i = -i(2 + i)^2$이다. 따라서

$$7 + i = -i(1 + i)(2 + i)^2$$

이다. 같은 노름의 $2 - i$는 약수가 아니다. $(7 + i)/(2 - i) = (7 + i)(2 + i)/5 = (13 + 9i)/5$가 가우스 정수가 아니기 때문이다. 노름 $5$의 소인수가 있다는 사실만으로는 $2 + i$와 $2 - i$를 구별할 수 없다는 점이 이 계산에서 틀리기 쉬운 부분이다.
:::

[정리 6](#thm6)에서 곧바로 Fermat의 정리가 나온다. $2 = 1^2 + 1^2$이므로 홀수 소수만 다루면 된다.

::: 따름정리 8 (Fermat의 두 제곱수 정리)
소수 $p$가 두 제곱수의 합 $p = x^2 + y^2$으로 쓰이는 것은 $p = 2$이거나 $p \equiv 1 \pmod{4}$인 것과 동치이다. $p \equiv 1 \pmod{4}$이면 이 표현은 $x, y$의 순서와 부호를 무시하고 유일하다.
:::

::: 증명
$p \equiv 3 \pmod{4}$이면 제곱수의 합이 $4$로 나눈 나머지 $3$을 가질 수 없다. $p = 2$는 $1^2 + 1^2$이다. $p \equiv 1 \pmod{4}$이면 [정리 6](#thm6)의 3에서 $p = \pi\overline{\pi}$, $N(\pi) = p$이므로 $\pi = x + yi$에 대해 $p = x^2 + y^2$이다.

유일성을 보이자. $p = x^2 + y^2$이면 $N(x + yi) = p$이므로 $x + yi$는 노름이 소수인 Gaussian prime이고 $p \mid N(x + yi)$이므로 $x + yi \mid p = \pi\overline{\pi}$에서 $x + yi$는 $\pi$ 또는 $\overline{\pi}$의 associate이다. 따라서 $x + yi \in \{\pm\pi, \pm i\pi, \pm\overline{\pi}, \pm i\overline{\pi}\}$이다. $\pi = a + bi$이면 이 여덟 원소의 실수부와 허수부는 $(\pm a, \pm b)$ 또는 $(\pm b, \pm a)$이고, $\{\lvert x\rvert, \lvert y\rvert\} = \{a, b\}$가 결정된다.
:::

## 두 제곱수로 표현되는 정수

이제 소수에서 임의의 양의 정수 $n$으로 간다. $n = x^2 + y^2$은 $n = N(x + yi)$와 같은 말이므로, $n$이 노름으로 나타나는지가 문제이다. 여기서 $x, y$는 $0$이어도 되고 $n = 9 = 3^2 + 0^2$도 두 제곱수의 합으로 센다.

::: 정리 9 (두 제곱수의 합의 특성화)
양의 정수 $n$이 두 제곱수의 합인 것은, $q \equiv 3 \pmod{4}$인 모든 소수 $q$에 대하여 $n$의 소인수분해에서 $q$의 지수가 짝수인 것과 동치이다.
:::

::: 증명
$q \equiv 3 \pmod{4}$인 모든 소수의 지수가 짝수라 하고 $n = 2^a\prod p_j^{b_j}\prod q_k^{2c_k}$로 쓰자 ($p_j \equiv 1$, $q_k \equiv 3 \pmod{4}$). $2 = N(1 + i)$이고 $p_j = N(\pi_j)$ ([정리 6](#thm6)), $q_k^2 = N(q_k)$이므로 각 인수가 가우스 정수의 노름이다. 노름은 multiplicative이므로 그 곱인 $n$도 노름, 곧 두 제곱수의 합이다.

역으로 $n = x^2 + y^2 = N(\alpha)$ ($\alpha = x + yi$)이고 $q \equiv 3 \pmod{4}$인 소수 $q$가 있다고 하자. [정리 6](#thm6)에 의하여 $q$는 Gaussian prime이다. [정리 4](#thm4)에 의하여 $\alpha$를 소인수분해했을 때 $q$의 associate가 나타나는 횟수를 $e$라 하자. 복소켤레는 환의 automorphism이고 $q$를 고정하므로 $\overline{\alpha}$의 소인수분해에서도 $q$의 associate가 정확히 $e$번 나타난다. $n = \alpha\overline{\alpha}$이므로 $n$의 소인수분해에서 $q$의 지수는 $2e$이다. 여기서 $\mathbb{Z}$의 소인수분해와 $\mathbb{Z}[i]$의 소인수분해를 비교할 때는 $q$ 외의 Gaussian prime이 $q$의 associate가 아니라는 사실을 쓴다. 이는 [정리 4](#thm4)의 유일성에서 나온다.
:::

$21 = 3 \cdot 7$은 $3$과 $7$이 모두 $4k + 3$ 꼴이고 지수가 $1$이므로 두 제곱수의 합이 아니다. $4$로 나눈 나머지가 $1$인 것만으로 충분하지 않다는 처음의 관찰이 이렇게 설명된다. 반면 $45 = 3^2 \cdot 5$는 $3$의 지수가 짝수이고 $45 = 6^2 + 3^2$이다. 이 경우 표현이 $3 \cdot (2 + i)$의 노름에서 나온다.

표현이 여러 개 존재하는 것도 같은 방법으로 읽힌다. $p \equiv 1 \pmod{4}$인 소수가 둘 이상 곱해져 있으면 각 소수마다 $\pi$와 $\overline{\pi}$ 중 어느 것을 쓸지 선택할 수 있고, 선택마다 다른 가우스 정수가 나온다.

::: 예시 10 ($65$의 두 표현)
$65 = 5 \cdot 13$이고 $5 = (2 + i)(2 - i)$, $13 = (3 + 2i)(3 - 2i)$이다. $65$를 노름으로 갖는 가우스 정수는 $5$에서 $2 + i$ 또는 $2 - i$를, $13$에서 $3 + 2i$ 또는 $3 - 2i$를 하나씩 골라 곱한 것의 associate이다. 선택 $(2 + i)(3 + 2i)$와 $(2 + i)(3 - 2i)$를 계산하면

$$\begin{aligned}
(2 + i)(3 + 2i) &= 6 + 4i + 3i - 2 = 4 + 7i, \\
(2 + i)(3 - 2i) &= 6 - 4i + 3i + 2 = 8 - i
\end{aligned}$$

이고 $65 = 4^2 + 7^2 = 8^2 + 1^2$이다. 나머지 두 선택은 각각 위 두 원소의 켤레이므로 부호와 순서를 무시하면 같은 표현을 준다. 따라서 이 두 가지가 $65$의 서로 다른 표현의 전부이다. 반면 $25 = 5^2$에서는 $(2 + i)^2 = 3 + 4i$가 $25 = 3^2 + 4^2$을 주고, $2 + i$와 $2 - i$를 하나씩 쓴 선택은 $5$ 자체이므로 $25 = 5^2 + 0^2$을 준다.
:::

여기까지는 두 제곱수의 합을 다루었다. 제곱수 네 개까지 허용하면 제한이 사라진다. 이 정리의 증명은 다루지 않고 진술만 둔다.

::: 정리 11 (Lagrange의 네 제곱수 정리)
모든 음이 아닌 정수는 네 개의 정수의 제곱의 합으로 쓰인다.
:::

[정리 9](#thm9)에 의해 $3$이나 $21$은 두 제곱수의 합이 아니고, $7 = 4 + 1 + 1 + 1$은 세 제곱수의 합으로도 쓰이지 않으므로 네 개라는 개수는 줄일 수 없다.

---

**참고문헌**

**[OL]** 오정환·이준복, *기초 정수론*, 경문사, 2012.
