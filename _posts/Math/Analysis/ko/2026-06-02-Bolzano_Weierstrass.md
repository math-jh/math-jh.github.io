---
title: "부분수열과 Bolzano–Weierstrass 정리"
description: "부분수열을 정의하고, 모든 실수열이 단조 부분수열을 가짐을 peak 논법으로 보인다. 이로부터 bounded sequence가 수렴하는 부분수열을 가진다는 Bolzano–Weierstrass 정리를 증명하고, bisection method에 의한 두 번째 증명과 ℝⁿ으로의 확장을 다룬다. 비유계 수열과 ℚ 안의 수열에서 정리가 어떻게 깨지는지도 확인한다."
excerpt: "부분수열, 단조 부분수열, Bolzano–Weierstrass 정리와 ℝⁿ으로의 확장"

categories: [Math / Analysis]
permalink: /ko/math/analysis/bolzano_weierstrass
sidebar: 
    nav: "analysis-ko"

date: 2026-06-02
weight: 4

published: false

---

수열 $a_n = (-1)^n$은 수렴하지 않지만, 짝수 번째 항만 모으면 상수수열 $1$이 되고 홀수 번째 항만 모으면 상수수열 $-1$이 된다. 이렇게 수열에서 일부 항을 골라 새 수열을 만드는 것이 부분수열이다. Bolzano–Weierstrass 정리는 수열이 bounded이기만 하면 수렴하는 부분수열을 반드시 뽑을 수 있다고 말한다. 이 정리는 극한값을 미리 알지 못해도 극한의 존재를 얻어내는 기본 도구이다. 우리는 [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3){: data-lid="4ucbf" }과 [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8){: data-lid="hryl0" }을 사용한다.

## 부분수열

::: 정의 1
수열 $(a_n)_{n\geq 1}$과 자연수의 순증가 수열 $n_1 < n_2 < n_3 < \cdots$이 주어졌을 때, 수열 $(a_{n_k})_{k\geq 1}$을 $(a_n)$의 *부분수열<sub>subsequence</sub>*이라 한다.
:::

핵심은 첨자가 순증가여야 한다는 점이다. 항의 순서를 바꾸거나 같은 항을 두 번 쓰는 것은 부분수열이 아니다. 예를 들어 $a_1, a_1, a_2, a_2, \dots$는 $(a_n)$의 부분수열이 아니다. 순증가성에서 $n_1 \geq 1$이고 $n_{k+1} > n_k$이므로 귀납적으로 모든 $k$에 대해 $n_k \geq k$이다. 이 부등식이 아래에서 계속 쓰인다.

::: 명제 2
$a_n \to L$이면 $(a_n)$의 모든 부분수열도 $L$로 수렴한다.
:::

::: 증명
$\varepsilon > 0$을 임의로 주고, $(a_n)$의 수렴으로부터 $n \geq N$이면 $\lvert a_n - L\rvert < \varepsilon$인 $N$을 잡는다. 부분수열 $(a_{n_k})$에 대해 $k \geq N$이면 $n_k \geq k \geq N$이므로 $\lvert a_{n_k} - L\rvert < \varepsilon$이다. 부분수열에서는 새 $\varepsilon$을 따로 고를 필요 없이, 원래 수열의 $N$을 그대로 쓰면 된다.
:::

이 명제의 대우에서, 서로 다른 값으로 수렴하는 두 부분수열을 가진 수열은 발산한다. $(-1)^n$의 발산은 이렇게 설명된다.

## 단조 부분수열

Bolzano–Weierstrass 정리의 증명에서 bounded라는 가정은 마지막 단계에서만 쓰인다. 그 앞 단계는 어떤 가정도 필요하지 않은 다음 사실이다.

::: 보조정리 3
모든 실수열은 단조 부분수열을 가진다.
:::

::: 증명
수열 $(a_n)$의 항 $a_m$이 *peak*라는 것을, 모든 $n > m$에 대해 $a_n \leq a_m$인 것으로 정의한다. 즉 $a_m$은 그 뒤의 모든 항 이상이다. 두 경우로 나눈다.

Peak가 무한히 많은 경우, peak인 첨자를 작은 것부터 $n_1 < n_2 < \cdots$로 나열한다. $a_{n_k}$가 peak이고 $n_{k+1} > n_k$이므로 $a_{n_{k+1}} \leq a_{n_k}$이다. 따라서 $(a_{n_k})$는 감소하는 부분수열이다.

Peak가 유한히 많은 경우, 모든 peak의 첨자보다 큰 $n_1$을 잡는다. 그러면 $a_{n_1}$은 peak가 아니고, peak가 아니라는 것은 $a_n > a_{n_1}$인 $n > n_1$이 존재한다는 뜻이다. 그런 $n$ 하나를 $n_2$로 잡는다. $n_2$도 모든 peak의 첨자보다 크므로 peak가 아니고, 같은 이유로 $a_{n_3} > a_{n_2}$인 $n_3 > n_2$가 있다. 이 과정은 끝나지 않으므로 증가하는 부분수열 $(a_{n_k})$를 얻는다.
:::

Peak의 정의에서 부등호가 $\leq$인 것은 첫째 경우에서 감소(비증가)를 얻기 위해서이며, 둘째 경우의 증가는 엄밀하다. 둘째 경우에서 $n_1$을 "마지막 peak 이후"로 잡는 이유는, peak인 항에서는 자기보다 큰 항을 뒤에서 찾을 수 없기 때문이다.

## Bolzano–Weierstrass 정리

::: 정리 4 (Bolzano–Weierstrass)
Bounded sequence는 수렴하는 부분수열을 가진다.
:::

::: 증명
$(a_n)$이 bounded라 하자. [보조정리 3](#lem3){: data-lid="bdx8n" }에 의하여 단조 부분수열 $(a_{n_k})$가 있다. 이 부분수열은 $(a_n)$의 항만을 취하므로 같은 한계로 bounded이다. 단조이면서 bounded인 수열은 [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8){: data-lid="28xaw" }에 의하여 수렴하므로, $(a_{n_k})$는 수렴하는 부분수열이다.
:::

정리가 주장하는 것은 수렴하는 부분수열의 존재뿐이다. 그 극한이 하나로 정해진다는 말은 없으며, $(-1)^n$처럼 극한이 서로 다른 부분수열이 여럿 있는 것이 보통이다.

## Bisection method

[정리 4](#thm4){: data-lid="e6tco" }의 다른 증명은 구간을 반씩 잘라 가는 bisection method이다. 이 방법은 compactness 증명에서도 되풀이되므로 따로 적어 둔다. [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8){: data-lid="0gskh" } 대신 다음의 nested interval 성질이 쓰인다.

::: 보조정리 5 (nested interval)
closed interval $I_j = [\alpha_j, \beta_j]$가 $I_1 \supseteq I_2 \supseteq \cdots$이고 $\beta_j - \alpha_j \to 0$이면, 모든 $I_j$에 공통으로 속하는 점이 정확히 하나 존재한다.
:::

::: 증명
모든 $j, k$에 대해 $\alpha_j \leq \beta_k$이다. 실제로 $m = \max(j, k)$로 두면 $I_m \subseteq I_j \cap I_k$이므로 $\alpha_j \leq \alpha_m \leq \beta_m \leq \beta_k$이다. 따라서 집합 $\{\alpha_j\}$는 위로 bounded이고, [§실수의 완비성, ⁋정의 3](/ko/math/analysis/completeness_of_reals#def3){: data-lid="ytq7s" }에 의하여 $L = \sup_j \alpha_j$가 존재한다. 정의에 의해 $\alpha_j \leq L$이고, 각 $\beta_k$가 $\{\alpha_j\}$의 상계이므로 $L \leq \beta_k$이다. 즉 $L \in I_j$이다. 공통점 $p, q$가 둘 있다면 모든 $j$에 대해 $\lvert p - q\rvert \leq \beta_j - \alpha_j$이므로 $p = q$이다.
:::

::: 증명 (정리 4)
$(a_n)$이 bounded이므로 모든 항을 담는 closed interval $I_0 = [m, M]$이 있다. $I_0$을 중점에서 둘로 나눈 두 closed 반구간 중 하나는 $a_n \in$ (그 반구간)인 첨자 $n$을 무한히 많이 가져야 한다. 두 반구간에 해당하는 첨자 집합의 합집합이 $I_0$에 해당하는 첨자 집합 전체인 $\mathbb{N}$이고, 유한 집합 둘의 합집합은 유한하기 때문이다. 그러한 반구간 하나를 $I_1$로 잡는다. 같은 절차를 $I_1$에 적용하는 것을 반복하여, 각 $j$에 대해 $A_j = \{n : a_n \in I_j\}$가 무한집합이고 $I_j$의 길이가 $(M - m)/2^j$인 구간열 $I_0 \supseteq I_1 \supseteq \cdots$을 얻는다.

$A_j$가 무한집합이므로 $n_{j-1}$보다 큰 원소가 항상 있다. 따라서 $n_j \in A_j$이고 $n_j > n_{j-1}$인 $n_1 < n_2 < \cdots$을 귀납적으로 고를 수 있다. [보조정리 5](#lem5){: data-lid="oha9l" }에 의하여 모든 $I_j$에 속하는 점 $L$이 있다. $a_{n_j}$와 $L$이 모두 $I_j$에 속하므로 다음이 성립한다.

$$\lvert a_{n_j} - L\rvert \leq \frac{M - m}{2^j} \to 0.$$

따라서 $a_{n_j} \to L$이다.
:::

Bisection method에서 "무한히 많은 항이 들어 있는 쪽"을 택하는 이유는, 항이 유한개만 들어 있는 구간에서는 첨자를 계속 뒤로 보내며 항을 고를 수 없기 때문이다. 둘 중 어느 쪽이 무한한지가 불명확해도 한쪽은 반드시 무한하므로 임의로 하나를 택하면 된다.

## 집적점

수렴하는 부분수열의 극한을 수열의 *집적점<sub>cluster point</sub>*이라 한다. 이 용어는 수열에 대한 것이며, 집합의 집적점(accumulation point)과 다르다. $(-1)^n$의 집적점은 $1$과 $-1$ 둘이지만, 이 수열의 값의 집합 $\{1, -1\}$은 집적점을 갖지 않는다. 수열은 같은 값을 반복해서 취할 수 있고, 그 값이 수열의 집적점이 되기 때문이다.

[정리 4](#thm4){: data-lid="nmyhe" }는 bounded sequence가 집적점을 적어도 하나 가진다는 말이다. 수렴하는 수열은 [명제 2](#prop2){: data-lid="v6wel" }에 의해 집적점이 하나뿐이다. 다음 명제는 bounded 수열에 한하여 그 역이 성립함을 보인다.

::: 명제 6
Bounded sequence $(a_n)$의 모든 집적점이 $L$과 같으면 $a_n \to L$이다.
:::

::: 증명
$a_n \not\to L$이라 가정하자. 이는 어떤 $\varepsilon_0 > 0$에 대해, 모든 $N$마다 $\lvert a_n - L\rvert \geq \varepsilon_0$인 $n \geq N$이 존재한다는 뜻이다. 이때 $\varepsilon_0$은 수렴하지 않음의 부정에서 정해지는 고정된 수이다. 따라서 $\lvert a_n - L\rvert \geq \varepsilon_0$인 첨자 $n_1 < n_2 < \cdots$을 귀납적으로 고를 수 있다. $(a_{n_k})$는 bounded이므로 [정리 4](#thm4){: data-lid="h6720" }에 의하여 수렴하는 부분수열을 가지며, 그 극한을 $L'$이라 하자. 이는 $(a_n)$의 부분수열이므로 $L'$은 $(a_n)$의 집적점이다. 한편 모든 항이 $\lvert a_{n_k} - L\rvert \geq \varepsilon_0$이므로 극한에서 $\lvert L' - L\rvert \geq \varepsilon_0 > 0$이고, $L' \neq L$이다. 이는 모든 집적점이 $L$이라는 가정에 모순이다.
:::

Bounded라는 가정은 필수이다. 수열 $1, 0, 2, 0, 3, 0, \dots$은 집적점이 $0$ 하나뿐이지만 $0$으로 수렴하지 않는다.

::: 예시 7 (집적점이 구간 전체인 수열)
$\mathbb{Q} \cap [0, 1]$은 가산집합이므로, 각 유리수가 정확히 한 번씩 나타나도록 $(r_n)$으로 나열할 수 있다. 이 수열은 $[0, 1]$에 들어 있으므로 bounded이다. 우리는 $[0, 1]$의 모든 점 $x$가 집적점임을 보인다.

각 $k \geq 1$에 대해 $(x - 1/k, x + 1/k) \cap [0, 1]$은 길이가 양수인 구간이고, 유리수는 실수에서 조밀하므로 이 구간은 유리수를 무한히 많이 포함한다. 각 유리수는 수열에서 서로 다른 첨자를 가지므로, 이 구간에 값이 들어가는 첨자도 무한히 많다. 따라서 $n_{k-1}$보다 큰 첨자 중에서

$$\lvert r_{n_k} - x\rvert < \frac{1}{k}$$

을 만족하는 $n_k$를 고를 수 있고, 이렇게 얻은 부분수열은 $x$로 수렴한다.
:::

[정리 4](#thm4){: data-lid="gmbhu" }가 보장하는 "적어도 하나"는 이 수열에서 연속체만큼 많은 집적점으로 나타난다.

## 정리의 가정

**Bounded가 아닌 경우.** $a_n = n$이면 $n_k \geq k$이므로 모든 부분수열이 $a_{n_k} = n_k \geq k$를 만족하여 bounded가 아니고, [§수열의 수렴, ⁋명제 3](/ko/math/analysis/convergence_of_sequences#prop3){: data-lid="ghqcp" }에 의하여 수렴하는 수열은 bounded이므로 수렴하는 부분수열이 없다. 일반적으로 bounded가 아닌 수열 $(a_n)$은, 각 $k$에 대해 $n_{k-1}$ 이하의 항들의 절댓값의 최댓값과 $k$ 중 큰 값을 $M_k$로 놓으면 $\lvert a_n\rvert > M_k$인 $n$이 있고, 이 $n$은 $n_{k-1}$보다 크다. 이를 $n_k$로 잡으면 $\lvert a_{n_k}\rvert > k$인 부분수열을 얻으며, 그 모든 부분수열 또한 bounded가 아니다. 즉 수열의 모든 부분수열이 수렴하는 부분수열을 가지려면 그 수열은 bounded여야 한다. 다만 위의 $1, 0, 2, 0, 3, 0, \dots$처럼 bounded가 아니어도 수렴하는 부분수열 하나는 가질 수 있으므로, [정리 4](#thm4){: data-lid="c6ats" }의 역은 이 형태로만 성립한다.

**극한이 집합 밖으로 나가는 경우.** 다음 따름정리는 closed interval 안의 수열에 대해 극한까지 구간 안에 있음을 말한다.

::: 따름정리 8
$[a, b]$ 안의 수열은 극한이 $[a, b]$에 속하는 수렴 부분수열을 가진다.
:::

::: 증명
[정리 4](#thm4){: data-lid="wbtzv" }에 의하여 수렴하는 부분수열 $a_{n_k} \to L$이 있다. $L < a$라 가정하고 $\varepsilon = a - L$로 두면, 충분히 큰 $k$에 대해 $a_{n_k} < L + \varepsilon = a$이므로 모든 항이 $a$ 이상이라는 사실에 모순이다. $L > b$인 경우도 같다. 따라서 $a \leq L \leq b$이다.
:::

구간이 closed라는 가정과 $\mathbb{R}$ 안에서 생각한다는 가정이 모두 필요하다.

::: 예시 9 (closedness와 완비성이 빠진 경우)
(1) 열린 구간 $(0, 1)$ 안의 수열 $a_n = 1/n$은 bounded이지만, 모든 부분수열이 $0$으로 수렴하고 $0 \notin (0, 1)$이므로 $(0, 1)$ 안에서 수렴하는 부분수열이 없다.

(2) $\mathbb{Q}$ 안에서 생각하면 $[1, 2] \cap \mathbb{Q}$처럼 closed interval 모양의 집합에서도 정리가 깨진다. $a_n = \lfloor 10^n \sqrt{2}\rfloor / 10^n$, 곧 $\sqrt{2}$의 소수점 아래 $n$째 자리까지의 절삭은 유리수이고 $[1, 2]$에 들어 있다. 또 $0 \leq \sqrt{2} - a_n < 10^{-n}$이므로 $\mathbb{R}$에서 $a_n \to \sqrt{2}$이다. [명제 2](#prop2){: data-lid="me9ta" }에 의하여 모든 부분수열이 $\sqrt{2}$로 수렴한다. [§수열의 수렴, ⁋명제 2](/ko/math/analysis/convergence_of_sequences#prop2){: data-lid="q5bwu" } 때문에 어떤 부분수열이 유리수 $q$로 수렴하면 $q = \sqrt{2}$여야 하는데, $\sqrt{2}$는 유리수가 아니다. 따라서 $\mathbb{Q}$ 안에서 수렴하는 부분수열이 없다.
:::

(2)에서 깨지는 곳은 증명의 어느 단계인지도 분명하다. [보조정리 3](#lem3){: data-lid="i099u" }은 $\mathbb{Q}$에서도 성립하여 $(a_n)$은 단조 부분수열을 가지지만, [§수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8){: data-lid="qf2x7" }과 [보조정리 5](#lem5){: data-lid="e28ow" }의 상한 성질이 $\mathbb{Q}$에서는 성립하지 않아 두 증명이 모두 막힌다.

## $\mathbb{R}^n$으로의 확장

$\mathbb{R}^n$의 점 $x = (x_1, \dots, x_n)$에 대해 $\lVert x\rVert = \sqrt{x_1^2 + \cdots + x_n^2}$로 두고, 점열이 bounded라는 것은 $\lVert x^{(m)}\rVert$가 bounded라는 뜻으로 한다. 각 좌표에 대해 $\lvert x_i\rvert \leq \lVert x\rVert \leq \lvert x_1\rvert + \cdots + \lvert x_n\rvert$이 성립하므로, 점열은 bounded인 것과 각 좌표수열이 bounded인 것이 동치이고, $x^{(m)} \to x$인 것과 각 좌표수열이 $x_i^{(m)} \to x_i$인 것도 동치이다.

::: 정리 10 (Bolzano–Weierstrass, $\mathbb{R}^n$)
$\mathbb{R}^n$의 bounded 점열은 수렴하는 부분수열을 가진다.
:::

::: 증명
점열 $(x^{(m)})$이 bounded라 하자. 첫째 좌표수열 $(x_1^{(m)})$은 bounded이므로 [정리 4](#thm4){: data-lid="k5e4q" }에 의하여 수렴하는 부분수열 $(x_1^{(m_k)})$이 있다. 이 부분수열을 따라가는 점열 $(x^{(m_k)})$의 둘째 좌표수열 $(x_2^{(m_k)})$ 역시 bounded이므로 다시 수렴하는 부분수열을 가진다. 이 과정을 $n$번째 좌표까지 반복하면, 부분수열의 부분수열로 이어지는 점열 $(x^{(\mu_l)})$을 얻는다. 여기서 순증가 첨자열의 합성은 순증가이므로 이것은 원래 점열의 부분수열이다. 각 좌표수열은 마지막 점열에서 수렴하는 부분수열의 부분수열이거나 그 자체이므로 [명제 2](#prop2){: data-lid="3p0eo" }에 의하여 수렴한다. 모든 좌표수열이 수렴하므로 $(x^{(\mu_l)})$은 $\mathbb{R}^n$에서 수렴한다.
:::

좌표를 하나씩 처리할 때 이전 좌표의 수렴이 보존되는 것이 [명제 2](#prop2){: data-lid="8d40c" }의 역할이다. 한 번에 모든 좌표를 맞추려 하지 않고 좌표마다 부분수열을 한 번 더 뽑는다는 것이 핵심이다. 이 증명은 좌표가 유한개라는 사실을 쓰므로 무한 차원에서는 성립하지 않는다. 제곱합이 유한한 실수열의 공간 $\ell^2$에서 표준기저 $e_k$는 $\lVert e_k\rVert = 1$이지만 $j \neq k$이면 $\lVert e_j - e_k\rVert = \sqrt{2}$이므로 수렴하는 부분수열을 갖지 않는다.

---

**참고문헌**

**[Rud]** W. Rudin, *Principles of mathematical analysis*, 3rd ed., McGraw-Hill, 1976.
