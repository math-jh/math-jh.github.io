---
title: "유수정리"
description: "isolated singularity에서 Laurent 전개의 음의 일차 계수를 residue로 정의하고, 닫힌 경로 안에 유한개의 singular point를 갖는 holomorphic function의 경로적분이 residue와 회전수의 합으로 결정된다는 유수정리를 증명한다. 극에서의 residue 계산 공식, essential singularity의 residue, 무한대에서의 residue와 residue 총합 0을 다룬다."
excerpt: "residue, 유수정리, 극에서의 유수 공식, Essential singularity의 residue, 무한대에서의 유수와 유수 총합 0"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/residue_theorem
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 10

published: false

---

단위원을 반시계방향으로 한 바퀴 도는 경로에서 $\oint \dd{z}/z = 2\pi i$이고, $\oint z^n\dd{z}$는 $n \neq -1$인 모든 정수 $n$에 대하여 $0$이다. 단위원 안에서 $1/z$가 원점이라는 단 하나의 singular point를 가지기 때문에 적분이 소멸하지 않으며, 그 값 $2\pi i$는 $1/z$의 계수 $1$에서 나온다. isolated singularity 근방에서 함수는 [§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2)에 의하여 Laurent 급수로 전개되고, 정수 멱의 경로적분 가운데 $n = -1$인 항만 남으므로 경로적분에 기여하는 것은 $(z - z_0)^{-1}$의 계수 하나뿐이다. 이 계수를 residue라 부르고, 유수정리는 닫힌 경로의 적분이 경로 안에 놓인 singular point들의 residue를 회전수로 가중하여 합한 값임을 말한다. 이 글에서는 residue를 정의하고 유수정리를 증명한 뒤, 극과 essential singularity에서 residue를 구하는 방법, 그리고 무한대에서의 residue를 다룬다.

## 유수의 정의

$f$가 $z_0$에서 isolated singularity를 가지면 어떤 $R > 0$에 대하여 $0 < \lvert z - z_0\rvert < R$에서 $f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$이라는 Laurent 전개가 성립한다.

::: 정의 1 (유수)
위와 같은 $f$에 대하여 음의 일차 계수 $a_{-1}$을 $f$의 $z_0$에서의 *residue<sub>유수</sub>*라 하고

$$\operatorname{Res}_{z = z_0} f = a_{-1}$$

로 적는다.
:::

[§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2)의 Laurent 계수 적분공식에 $n = -1$을 대입하면, $0 < \rho < R$인 모든 $\rho$에 대하여

$$\operatorname{Res}_{z = z_0} f = \frac{1}{2\pi i}\oint_{\lvert z - z_0\rvert = \rho} f(z)\dd{z}$$

이다. 이때 원은 반시계방향으로 한 바퀴 돈다. 곧 $z_0$ 하나만을 감싸는 작은 원 위의 적분은 $2\pi i$에 residue를 곱한 값이다. 또 $z_0$가 removable singularity이면 $f$가 $z_0$에서 holomorphic으로 확장되어 음의 거듭제곱 항이 없으므로 residue는 $0$이다. 그 역은 성립하지 않는다. $1/z^2$은 극을 가지지만 residue가 $0$이다.

## 유수정리

유수정리는 위의 관찰을 임의의 닫힌 경로로 확장한다. 경로 $\gamma$의 점 $a \notin \gamma$에 대한 회전수는 $n(\gamma, a) = \frac{1}{2\pi i}\oint_\gamma \dd{z}/(z - a)$이며, $\gamma$가 $a$를 반시계방향으로 도는 횟수를 센다.

::: 정리 2 (유수정리)
$\Omega \subseteq \mathbb{C}$가 단순연결 영역이고 $z_1, \dots, z_k$가 $\Omega$ 안의 서로 다른 점이라 하자. $f$가 $\Omega \setminus \{z_1, \dots, z_k\}$에서 holomorphic이면, 자취가 $\Omega \setminus \{z_1, \dots, z_k\}$에 들어 있는 임의의 닫힌 piecewise $C^1$ 경로 $\gamma$에 대하여

$$\oint_\gamma f(z)\dd{z} = 2\pi i \sum_{j=1}^{k} n(\gamma, z_j)\operatorname{Res}_{z = z_j} f$$

이다.
:::

::: 증명
각 $z_j$에서 $f$의 Laurent 전개의 주부를 $P_j(z) = \sum_{n=1}^{\infty} a_{-n}^{(j)}(z - z_j)^{-n}$이라 하자. 변수 $w = 1/(z - z_j)$에 대하여 $P_j$는 $w$의 멱급수이고, 이 멱급수는 $\lvert w\rvert > 1/R_j$인 점에서 수렴한다. 멱급수가 한 점에서 수렴하면 그 점보다 절댓값이 작은 모든 점에서 수렴하므로 $P_j$는 모든 $w \in \mathbb{C}$에서, 곧 $\mathbb{C} \setminus \{z_j\}$에서 수렴하고 그곳에서 holomorphic이다. 또 $\mathbb{C} \setminus \{z_j\}$의 임의의 compact 집합 위에서 균등수렴한다.

함수 $g = f - \sum_{j=1}^{k} P_j$를 생각한다. $z_j$의 구멍 뚫린 근방에서 $f - P_j$는 Laurent 전개의 regular part이므로 $z_j$까지 holomorphic으로 확장되고, 나머지 $P_\ell$ ($\ell \neq j$)은 $z_j$에서 holomorphic이다. 따라서 $g$의 모든 $z_j$는 removable singularity이며, $g$는 $\Omega$ 전체에서 holomorphic인 함수로 확장된다. $\Omega$가 단순연결이므로 [§Cauchy 정리, ⁋따름정리 8](/ko/math/complex_analysis/cauchy_theorem#cor8)에 의하여 $\oint_\gamma g\dd{z} = 0$이고, 따라서

$$\oint_\gamma f(z)\dd{z} = \sum_{j=1}^{k}\oint_\gamma P_j(z)\dd{z}$$

이다. $\gamma$의 자취는 $z_j$를 포함하지 않는 compact 집합이므로 $P_j$의 급수는 그 위에서 균등수렴하고, 항별로 적분할 수 있다. $n \geq 2$이면 $(z - z_j)^{-n}$은 $\mathbb{C} \setminus \{z_j\}$에서 원시함수 $(z - z_j)^{1-n}/(1-n)$을 가지므로 닫힌 경로 위의 적분이 $0$이다. $n = 1$인 항은 회전수의 정의에 의하여 $\oint_\gamma (z - z_j)^{-1}\dd{z} = 2\pi i\cdot n(\gamma, z_j)$를 준다. 그러므로 $\oint_\gamma P_j\dd{z} = 2\pi i\cdot n(\gamma, z_j) a_{-1}^{(j)}$이고, 이를 $j$에 대해 더하면 된다.
:::

회전수는 경로 밖의 singular point를 걸러 낸다. $\gamma$가 단순닫힌곡선이고 반시계방향이면 안쪽 점의 회전수는 $1$, 바깥쪽 점의 회전수는 $0$이므로 공식은 안쪽 singular point의 residue 합에 $2\pi i$를 곱한 꼴이 된다. 반시계방향이 아니면 부호가 바뀐다. 시계방향 경로에서는 안쪽 점의 회전수가 $-1$이다.

정리의 가정은 모두 필요하다. 경로가 singular point를 지나면 적분 자체가 정의되지 않는다. 또 $\Omega$가 단순연결이라는 가정이 빠지면 공식이 무너진다. $\Omega = \mathbb{C} \setminus \{0\}$, $f(z) = 1/z$, $\gamma$를 단위원으로 두면 $\Omega$ 안에는 $f$의 singular point가 없어 우변이 $0$이지만 좌변은 $2\pi i$이다. 원점이 $\Omega$에서 빠져 있어 경로가 $\Omega$ 안에서 한 점으로 수축하지 않기 때문이다.

## 극에서의 유수 계산

residue의 정의대로 Laurent 전개 전체를 구하는 것은 번거롭다. 극에서는 주부가 유한합이므로 곱하고 미분하는 것만으로 $a_{-1}$을 얻는다. $z_0$가 order $m$인 극이라는 것은 $a_{-m} \neq 0$이고 $n < -m$에서 $a_n = 0$이라는 뜻이다.

::: 명제 3 (극에서의 유수)
$m \geq 1$이고 $(z - z_0)^m f(z)$가 $z_0$에서 holomorphic으로 확장된다고 하자. 곧 $z_0$는 order가 $m$ 이하인 극이거나 removable singularity이다. 그럼

$$\operatorname{Res}_{z = z_0} f = \frac{1}{(m-1)!}\lim_{z \rightarrow z_0}\frac{d^{m-1}}{\dd{z}^{m-1}}\Bigl[(z - z_0)^m f(z)\Bigr]$$

이다. 특히 단순극에서는 $\operatorname{Res}_{z = z_0} f = \lim_{z \rightarrow z_0}(z - z_0)f(z)$이다. 또 $g$가 $z_0$에서 holomorphic이고 $h$가 $z_0$에서 단순영점을 가지면 ($h(z_0) = 0$, $h'(z_0) \neq 0$)

$$\operatorname{Res}_{z = z_0}\frac{g}{h} = \frac{g(z_0)}{h'(z_0)}$$

이다.
:::

::: 증명
가정에서 $a_n = 0$ ($n < -m$)이므로 $(z - z_0)^m f(z) = \sum_{k=0}^{\infty} a_{k-m}(z - z_0)^k$이다. 이는 $z_0$에서 holomorphic인 함수의 Taylor 전개이고, Taylor 계수는 [§멱급수와 해석성, ⁋정리 1](/ko/math/complex_analysis/power_series_and_analyticity#thm1)에 의하여 도함수로 주어진다. $a_{-1}$은 $k = m - 1$인 항의 계수이므로

$$a_{-1} = \frac{1}{(m-1)!}\frac{d^{m-1}}{\dd{z}^{m-1}}\Bigl[(z - z_0)^m f(z)\Bigr]\bigg\rvert_{z = z_0}$$

이고, 도함수가 연속이므로 대입은 극한과 일치한다. $m = 1$이면 $(m-1)! = 1$이고 미분이 없으므로 단순극 공식을 얻는다. 마지막 공식은 $f = g/h$에 대하여 $(z - z_0)f(z) = g(z)\cdot (z - z_0)/h(z)$가 $h(z_0) = 0$ 때문에 $h(z) = h(z) - h(z_0)$이고, 차분비 $(h(z) - h(z_0))/(z - z_0)$가 $h'(z_0) \neq 0$으로 수렴하므로 $z \rightarrow z_0$에서 $g(z_0)/h'(z_0)$으로 수렴하기 때문이다. $h$가 단순영점을 가지므로 $(z - z_0)f$가 $z_0$에서 holomorphic으로 확장되어 $m = 1$의 경우가 적용된다.
:::

[명제 3](#prop3)에서 $m$은 정확한 order일 필요가 없고 그 이상이면 된다. order를 정확히 판정하는 것이 번거로운 경우에는 넉넉한 $m$을 잡아도 같은 값이 나온다. 반대로 $m$이 order보다 작으면 극한이 발산하여 공식을 쓸 수 없다.

::: 예시 4 (이중극과 order의 상한)
$f(z) = 1/(z^2 + 1)^2$은 $z = \pm i$에서 이중극을 가진다. $z = i$에서 $(z - i)^2 f(z) = (z + i)^{-2}$이므로 $m = 2$를 쓰면

$$\operatorname{Res}_{z = i} f = \frac{d}{\dd{z}}(z + i)^{-2}\bigg\rvert_{z = i} = \frac{-2}{(2i)^3} = \frac{1}{4i}$$

이고, 같은 방식으로 $\operatorname{Res}_{z = -i} f = -1/(4i)$이다. 두 residue의 합이 $0$이라는 사실은 아래의 [정리 8](#thm8)과 맞는다.

다음으로 $f(z) = (e^z - 1)/z^3$의 $z = 0$에서의 residue를 구한다. 분자가 $0$에서 소멸하므로 order가 $3$인지 $2$인지 곧바로 보이지 않는다. $m = 3$으로 놓으면 $z^3 f(z) = e^z - 1$이므로

$$\operatorname{Res}_{z = 0} f = \frac{1}{2!}\frac{d^2}{\dd{z}^2}(e^z - 1)\bigg\rvert_{z = 0} = \frac{1}{2}$$

이다. 실제 Laurent 전개는 $f(z) = z^{-2} + 1/2z^{-1} + 1/6 + \cdots$이므로 order는 $2$이고, $m = 3$이 order보다 크지만 같은 값이 나온다. $m = 1$을 쓰면 $z f(z) = (e^z - 1)/z^2$이 $z \rightarrow 0$에서 발산하여 공식이 적용되지 않는다.
:::

## Essential singularity의 residue

essential singularity에서는 Laurent 전개의 음의 거듭제곱 항이 무한히 많으므로 [명제 3](#prop3)의 어떤 $m$도 조건을 만족하지 않는다. 가령 $e^{1/z}$에 대하여 $z^m e^{1/z}$은 $z \rightarrow 0^+$에서 모든 $m$에 대하여 발산한다. 이 경우 residue는 Laurent 전개를 직접 구해서 $z^{-1}$의 계수를 읽어 내야 한다. $e^{1/z} = \sum_{n=0}^{\infty} z^{-n}/n!$이므로 $\operatorname{Res}_{z = 0} e^{1/z} = 1$이고, 따라서 $\oint_{\lvert z\rvert = 1} e^{1/z}\dd{z} = 2\pi i$이다.

::: 예시 5 (두 멱급수의 곱)
$f(z) = e^{z + 1/z}$은 $z = 0$에서 essential singularity를 가진다. $e^z$와 $e^{1/z}$는 각각 $z \neq 0$에서 절대수렴하는 급수 $\sum_a z^a/a!$와 $\sum_b z^{-b}/b!$로 전개되므로, 두 급수의 곱을 항의 순서와 무관하게 전개할 수 있다.

$$f(z) = \sum_{a, b \geq 0}\frac{z^{a-b}}{a!b!}$$

$z^{-1}$의 계수는 $b = a + 1$인 항들의 합이므로

$$\operatorname{Res}_{z = 0} f = \sum_{a=0}^{\infty}\frac{1}{a!(a+1)!} = 1 + \frac{1}{2} + \frac{1}{12} + \frac{1}{144} + \cdots$$

이고, 따라서 $\oint_{\lvert z\rvert = 1} e^{z + 1/z}\dd{z} = 2\pi i\sum_{a \geq 0} 1/(a!(a+1)!)$이다. 이 경우 $\lim_{z \rightarrow 0} z^m f(z)$ 꼴의 공식은 어떤 $m$에 대해서도 쓸 수 없다.
:::

## 무한대에서의 유수

$f$가 어떤 $R > 0$에 대하여 $\lvert z\rvert > R$에서 holomorphic이면 $\lvert z\rvert > R$에서 $f(z) = \sum_{n=-\infty}^{\infty} a_n z^n$인 Laurent 전개가 성립한다. 이 경우 $\infty$를 $f$의 isolated singularity로 취급하여 residue를 정의한다. 정의에서 부호를 주의해야 한다.

::: 정의 6 (무한대에서의 유수)
$f$가 $\lvert z\rvert > R$에서 holomorphic이고 그곳에서 $f(z) = \sum_{n} a_n z^n$이라 하자. $f$의 *무한대에서의 residue*를

$$\operatorname{Res}_{\infty} f = -a_{-1}$$

로 정의한다. 곧 $\operatorname{Res}_{\infty} f$는 $\rho > R$인 원 $\lvert z\rvert = \rho$를 시계방향으로 한 바퀴 돈 적분의 $1/(2\pi i)$배이다.
:::

원 $\lvert z\rvert = \rho$를 시계방향으로 돌면 $\infty$를 포함하는 바깥 영역이 경로의 왼쪽에 놓이므로, 정의의 음의 부호는 $\infty$를 기준으로 반시계방향을 택한 결과이다. 주의할 점은 $f$가 $\infty$에서 holomorphic으로 확장되더라도 $a_{-1} \neq 0$이면 $\operatorname{Res}_\infty f \neq 0$이라는 것이다. $f(z) = 1/z$이 그 예이며 $\operatorname{Res}_\infty (1/z) = -1$이다. 반대로 $f(z) = O(z^{-2})$이면 $a_{-1} = 0$이므로 $\operatorname{Res}_\infty f = 0$이다.

실제 계산에는 $w = 1/z$로 바꾼 식이 쓰인다.

::: 명제 7 (무한대에서의 유수의 계산)
$f$가 $\lvert z\rvert > R$에서 holomorphic이면

$$\operatorname{Res}_{\infty} f = -\operatorname{Res}_{w = 0}\Bigl[\frac{1}{w^2}f\Bigl(\frac{1}{w}\Bigr)\Bigr]$$

이다.
:::

::: 증명
$F(w) = w^{-2}f(1/w)$는 $0 < \lvert w\rvert < 1/R$에서 holomorphic이므로 $w = 0$이 isolated singularity이다. $\rho > R$에 대하여 $z = 1/w$로 치환하면 $z$가 원 $\lvert z\rvert = \rho$를 반시계방향으로 돌 때 $w$는 원 $\lvert w\rvert = 1/\rho$를 시계방향으로 돌고, $\dd{z} = -w^{-2}\dd{w}$이다. 따라서

$$\oint_{\lvert z\rvert = \rho} f(z)\dd{z} = -\oint_{\lvert w\rvert = 1/\rho}^{\text{시계방향}} F(w)\dd{w} = \oint_{\lvert w\rvert = 1/\rho} F(w)\dd{w}$$

이다. 마지막 적분은 반시계방향이다. 좌변은 [§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2)의 계수 공식에 의하여 $2\pi i a_{-1}$이고 우변은 $2\pi i \operatorname{Res}_{w = 0} F$이므로 $a_{-1} = \operatorname{Res}_{w=0} F$이고, [정의 6](#def6)에 의하여 주장을 얻는다.
:::

[명제 7](#prop7)의 식에서 $\operatorname{Res}_\infty f = -\operatorname{Res}_{z = 0} f$가 아니라는 점에 주의해야 한다. 우변은 $f$ 자신이 아니라 $f(1/w)/w^2$의 residue이다. $f(z) = 1/(z-1)$이면 $f$는 $z = 0$에서 holomorphic이므로 $\operatorname{Res}_{z=0} f = 0$이지만, $1/(z-1) = \sum_{n \geq 1} z^{-n}$ ($\lvert z\rvert > 1$)이므로 $\operatorname{Res}_\infty f = -1$이다. [명제 7](#prop7)로 확인하면 $F(w) = w^{-2}/(1/w - 1) = 1/\bigl(w(1 - w)\bigr)$이고 $\operatorname{Res}_{w=0} F = 1$이어서 $\operatorname{Res}_\infty f = -1$로 일치한다.

singular point가 유한개이면 유한한 점들의 residue와 무한대에서의 residue를 모두 더한 값이 $0$이다.

::: 정리 8 (유수 총합)
$f$가 $\mathbb{C} \setminus \{z_1, \dots, z_k\}$에서 holomorphic이면

$$\sum_{j=1}^{k}\operatorname{Res}_{z = z_j} f + \operatorname{Res}_{\infty} f = 0$$

이다.
:::

::: 증명
$\rho > \max_j \lvert z_j\rvert$를 잡으면 $f$는 $\lvert z\rvert > \max_j\lvert z_j\rvert$에서 holomorphic이다. 원판 $\lvert z\rvert < \rho + 1$과 경로 $\lvert z\rvert = \rho$에 [정리 2](#thm2)를 적용한다. 각 $z_j$의 회전수가 $1$이므로 $\oint_{\lvert z\rvert = \rho} f\dd{z} = 2\pi i\sum_j\operatorname{Res}_{z=z_j} f$이다. 한편 같은 적분은 [§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2)의 계수 공식에 의하여 $2\pi i a_{-1} = -2\pi i\operatorname{Res}_\infty f$이다. 두 식을 비교하면 된다.
:::

$f$가 $\infty$에서 isolated singularity를 갖지 않으면 [정리 8](#thm8)은 쓸 수 없다. 가령 $1/\sin z$는 $z = n\pi$에서 극을 가지며 이 극들이 $\infty$로 쌓이므로 $\infty$가 isolated singularity이 아니다. [정리 8](#thm8)의 효용은 안쪽에 singular point가 많은 경로적분에서 드러난다. [정리 2](#thm2)를 그대로 쓰면 모든 singular point의 residue를 구해야 하지만, $\operatorname{Res}_\infty$ 하나만 구해도 같은 값을 얻는다.

::: 예시 9 (유수 총합을 이용한 적분)
$f(z) = z^{17}/\bigl((z^2 + 2)^3(z^3 + 3)^4\bigr)$에 대하여 $\oint_{\lvert z\rvert = 2} f(z)\dd{z}$를 구한다. $f$의 극은 $z^2 + 2 = 0$의 두 근($\lvert z\rvert = \sqrt{2}$, order $3$)과 $z^3 + 3 = 0$의 세 근($\lvert z\rvert = 3^{1/3}$, order $4$)이고, 다섯 극 모두 $\lvert z\rvert < 2$ 안에 있다. 각 극의 residue를 [명제 3](#prop3)으로 구하려면 최대 $3$번에서 $2$번 미분하는 계산이 다섯 번 필요하다.

대신 $\operatorname{Res}_\infty f$를 구한다. [명제 7](#prop7)의 $F(w) = w^{-2}f(1/w)$를 계산하면

$$F(w) = \frac{w^{-17-2}}{w^{-6}(1 + 2w^2)^3 w^{-12}(1 + 3w^3)^4} = \frac{1}{w}\cdot\frac{1}{(1 + 2w^2)^3(1 + 3w^3)^4}$$

이다. 마지막 인수는 $w = 0$에서 holomorphic이고 값이 $1$이므로 $\operatorname{Res}_{w = 0} F = 1$이고 $\operatorname{Res}_\infty f = -1$이다. 모든 극이 경로 안에 있으므로 [정리 2](#thm2)와 [정리 8](#thm8)에 의하여

$$\oint_{\lvert z\rvert = 2} f(z)\dd{z} = 2\pi i\sum_{j=1}^{5}\operatorname{Res}_{z = z_j} f = -2\pi i\operatorname{Res}_\infty f = 2\pi i$$

이다.
:::

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.  
**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.  
**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
