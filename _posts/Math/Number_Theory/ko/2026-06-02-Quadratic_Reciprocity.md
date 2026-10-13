---
title: "이차 상호법칙"
description: "서로 다른 두 홀수 소수 p, q에 대하여 (p/q)와 (q/p)가 어떻게 연결되는지를 말하는 이차 상호법칙을 가우스 보조정리와 lattice point 세기로 증명한다. 이를 합성수 분모로 확장한 Jacobi 기호와 호제법형 계산 절차, Jacobi 기호가 1이어도 이차 잉여가 아닌 반례, 그리고 3과 5가 이차 잉여인 소수의 분류까지 다룬다."
excerpt: "이차 상호법칙의 lattice point 증명, Jacobi 기호와 Legendre 기호의 계산"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/quadratic_reciprocity
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 9

published: false

---

[§이차 잉여, ⁋따름정리 5](/ko/math/number_theory/quadratic_residues#cor5)에서 우리는 Legendre 기호가 multiplicative이고 $-1$이 이차 잉여인 소수가 $p \equiv 1 \pmod4$임을, [§이차 잉여, ⁋정리 9](/ko/math/number_theory/quadratic_residues#thm9)에서 $2$가 이차 잉여인 소수가 $p \equiv \pm 1 \pmod8$임을 보았다. 곱셈성에 의하여 $(a/p)$의 계산은 $-1$, $2$, 홀수 소수 $q$에서의 값 $(q/p)$로 환원되므로, 남은 문제는 홀수 소수 $q$가 어떤 소수 $p$에 대하여 이차 잉여인지이다.

$q = 3$으로 직접 확인해 보자. $3$은 법 $11$에서 $5^2 = 25 \equiv 3$, 법 $13$에서 $4^2 = 16 \equiv 3$, 법 $37$에서 $15^2 = 225 \equiv 3$이므로 이차 잉여이다. 반면 법 $5, 7, 17, 19$에서는 이차 비잉여이다. 잉여인 소수 $11, 13, 37$은 $12$로 나눈 나머지가 $\pm 1$이고, 비잉여인 소수 $5, 7, 17, 19$는 나머지가 $\pm 5$이다. $(3/p)$는 $p$의 크기가 아니라 $p$를 $12 = 4 \cdot 3$으로 나눈 나머지에만 의존하는 것처럼 보인다. 이 의존성은 $(q/p)$가 $(p/q)$와 단순한 부호로 연결된다는 사실에서 나오며, 이것이 이차 상호법칙이다.

## 이차 상호법칙의 진술

::: 정리 1 (이차 상호법칙)
서로 다른 두 홀수 소수 $p, q$에 대하여

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$$

이다. 곧 $p, q$ 중 적어도 하나가 $4$로 나누어 $1$이 남으면 $(p/q) = (q/p)$이고, 둘 다 $4$로 나누어 $3$이 남으면 $(p/q) = -(q/p)$이다.
:::

지수 $\frac{p-1}{2}\cdot\frac{q-1}{2}$가 홀수인 것은 두 인수가 모두 홀수인 것, 곧 $p \equiv q \equiv 3 \pmod{4}$인 것과 동치이므로 정리의 둘째 문장이 따른다. 부호가 바뀌는 경우는 이 한 가지뿐이다.

$q^\ast = (-1)^{(q-1)/2}q$로 두면, 곧 $q^\ast$는 $q \equiv 1 \pmod{4}$이면 $q$, $q \equiv 3 \pmod{4}$이면 $-q$이다. [§이차 잉여, ⁋따름정리 5](/ko/math/number_theory/quadratic_residues#cor5)의 $(-1/p) = (-1)^{(p-1)/2}$와 곱셈성에 의하여 $(q^\ast/p) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}(q/p)$이고, [정리 1](#thm1)을 쓰면

$$\left(\frac{q^\ast}{p}\right) = \left(\frac{p}{q}\right)$$

을 얻는다. 우변 $(p/q)$는 $p \bmod q$에만 의존하므로, $(q/p) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}(p/q)$는 $p \bmod 4$와 $p \bmod q$에만 의존한다. 따라서 홀수 소수 $q$가 이차 잉여인 소수 $p$의 집합은 $4q$를 법으로 하는 합동류들의 합집합이다. 위에서 본 $q = 3$의 경우가 법 $12$였던 이유가 이것이다.

## Lattice point 세기에 의한 증명

증명은 Eisenstein의 방법을 따른다. [§이차 잉여, ⁋보조정리 7](/ko/math/number_theory/quadratic_residues#lem7)은 $(a/p)$를 $as$ ($s = 1, \ldots, (p-1)/2$)의 나머지 중 $p/2$를 넘는 것의 개수 $\mu$의 홀짝으로 표현한다. 이 $\mu$를 직접 세는 대신 quotient $\lfloor as/p\rfloor$의 합의 홀짝으로 바꾸면, 그 합은 좌표평면의 lattice point 개수로 읽힌다.

::: 보조정리 2
$p$가 홀수 소수이고 $a$가 $p \nmid a$인 홀수 정수이면

$$\left(\frac{a}{p}\right) = (-1)^{M}, \qquad M = \sum_{s=1}^{(p-1)/2}\left\lfloor \frac{as}{p}\right\rfloor$$

이다.
:::

::: 증명
$S = \{1, \ldots, (p-1)/2\}$로 두고, $s \in S$에 대하여 $as$의 법 $p$ 최소 양의 나머지를 $\rho_s$라 하자. $p \nmid as$이므로 $\rho_s \ne 0$이고, $as = p\lfloor as/p\rfloor + \rho_s$이다. 이를 $s \in S$에 대하여 모두 더하면

$$a\sum_{s \in S} s = pM + \sum_{s \in S}\rho_s$$

이다. 이제 $\sum \rho_s$의 홀짝을 구한다. [§이차 잉여, ⁋보조정리 7](/ko/math/number_theory/quadratic_residues#lem7)의 증명에서와 같이, 각 $s \in S$에 대하여 $as \equiv \varepsilon_s r_s \pmod{p}$를 만족하는 $\varepsilon_s \in \{1, -1\}$과 $r_s \in S$를 택하면 $s \mapsto r_s$는 $S$ 위의 전단사이다. $\varepsilon_s = 1$이면 $\rho_s = r_s$이고 $\varepsilon_s = -1$이면 $\rho_s = p - r_s$이며, $\varepsilon_s = -1$인 $s$의 개수가 보조정리의 $\mu$이다. 그러므로

$$\sum_{s \in S}\rho_s = \sum_{s \in S} r_s - 2\sum_{\varepsilon_s = -1} r_s + \mu p \equiv \sum_{s \in S} s + \mu \pmod{2}$$

이다. 마지막 합동에서 $\sum r_s = \sum s$와 $p$가 홀수라는 사실을 썼다. 위의 두 식을 합치고 $a, p$가 홀수임을 쓰면 법 $2$에서

$$\sum_{s \in S} s \equiv M + \sum_{s \in S} s + \mu$$

이므로 $M \equiv \mu \pmod{2}$이다. [§이차 잉여, ⁋보조정리 7](/ko/math/number_theory/quadratic_residues#lem7)에 의하여 $(a/p) = (-1)^\mu = (-1)^M$이다.
:::

[보조정리 2](#lem2)는 $a$가 홀수일 때만 성립한다. $a$가 짝수이면 $a\sum s$의 홀짝이 $\sum s$와 달라져 위의 소거가 일어나지 않는다. 상호법칙에서는 $a$로 홀수 소수가 들어가므로 문제가 없다.

::: 증명 (정리 1)
$p, q$가 서로 다른 홀수 소수이므로 [보조정리 2](#lem2)를 $(a, p) = (q, p)$와 $(a, p) = (p, q)$에 적용할 수 있다. 곧

$$\left(\frac{q}{p}\right) = (-1)^{M_1}, \quad M_1 = \sum_{x=1}^{(p-1)/2}\left\lfloor \frac{qx}{p}\right\rfloor, \qquad \left(\frac{p}{q}\right) = (-1)^{M_2}, \quad M_2 = \sum_{y=1}^{(q-1)/2}\left\lfloor \frac{py}{q}\right\rfloor$$

이다. 따라서 $M_1 + M_2 = \frac{p-1}{2}\cdot\frac{q-1}{2}$임을 보이면 충분하다.

직사각형 안의 lattice point 집합 $R = \{(x, y) \in \mathbb{Z}^2 : 1 \le x \le (p-1)/2,\ 1 \le y \le (q-1)/2\}$를 생각하면 $R$의 원소 수는 $\frac{p-1}{2}\cdot\frac{q-1}{2}$이다. $R$의 점 $(x, y)$에 대하여 $qx = py$일 수 없다. 그렇다면 $p \mid qx$이고 $p \ne q$가 소수이므로 [§소수와 산술의 기본정리, ⁋보조정리 2](/ko/math/number_theory/primes#lem2)에 의하여 $p \mid x$인데, $1 \le x < p$이기 때문이다. 따라서 $R$은 $qx > py$인 점들의 집합 $R_1$과 $qx < py$인 점들의 집합 $R_2$의 서로소 합집합이다.

$M_1 = \lvert R_1\rvert$임을 보이자. 고정된 $x$에 대하여 $1 \le y < qx/p$인 정수 $y$는 $\lfloor qx/p\rfloor$개이다. 이 $y$들은 모두 $R$ 안에 있다. 실제로 $y < qx/p \le q(p-1)/(2p) < q/2$이고 $y$가 정수이므로 $y \le (q-1)/2$이기 때문이다. 이것이 $x$와 $y$의 범위를 모두 절반 $\{1, \ldots, (p-1)/2\}$, $\{1, \ldots, (q-1)/2\}$로 잡는 이유이다. 가우스 보조정리의 $S$와 같은 구간이어서 [보조정리 2](#lem2)를 쓸 수 있고, 동시에 quotient $\lfloor qx/p\rfloor$가 $y$의 상한을 넘지 않아 quotient의 합이 $R$ 안의 점 개수와 정확히 일치한다. 따라서 $x = 1, \ldots, (p-1)/2$에 대하여 더하면 $M_1 = \lvert R_1\rvert$이다. $p$와 $q$의 역할을 바꾸어 같은 논증을 적용하면 $M_2$는 $1 \le x < py/q$, 곧 $qx < py$인 $R$의 점의 개수 $\lvert R_2\rvert$이다. 그러므로

$$M_1 + M_2 = \lvert R_1\rvert + \lvert R_2\rvert = \lvert R\rvert = \frac{p-1}{2}\cdot\frac{q-1}{2}$$

이고, $(p/q)(q/p) = (-1)^{M_1 + M_2}$로부터 정리가 따른다.
:::

## Jacobi 기호

상호법칙을 계산에 쓰려면 매 단계에서 분자를 소인수분해해야 한다. 분자가 크면 이것이 병목이 된다. 분모를 합성수로 확장한 Jacobi 기호를 쓰면 분자를 소인수분해하지 않고도 상호법칙을 적용할 수 있다.

::: 정의 3
홀수인 양의 정수 $n = p_1 p_2 \cdots p_k$ ($p_i$는 소수, 중복 허용)와 정수 $a$에 대하여 *Jacobi 기호<sub>Jacobi symbol</sub>* $(a/n)$을 Legendre 기호의 곱

$$\left(\frac{a}{n}\right) = \prod_{i=1}^{k}\left(\frac{a}{p_i}\right)$$

으로 정의한다. $n = 1$이면 빈 곱으로 $(a/1) = 1$이다.
:::

$n$이 소수이면 Legendre 기호와 일치한다. 정의에서 곧바로 $(a/n)$이 $a \bmod n$에만 의존하고 $a$와 $n$ 각각에 대하여 multiplicative임을 알 수 있다. 또 $\gcd(a, n) > 1$이면 어떤 $p_i$가 $a$를 나누어 $(a/n) = 0$이고, $\gcd(a, n) = 1$이면 $(a/n) = \pm 1$이다.

::: 명제 4
$m, n$이 홀수인 양의 정수이면 다음이 성립한다.

1. $\left(\frac{-1}{n}\right) = (-1)^{(n-1)/2}$.
2. $\left(\frac{2}{n}\right) = (-1)^{(n^2-1)/8}$.
3. $\gcd(m, n) = 1$이면 $\left(\frac{m}{n}\right)\left(\frac{n}{m}\right) = (-1)^{\frac{m-1}{2}\cdot\frac{n-1}{2}}$.
:::

::: 증명
홀수 양의 정수 $a$에 대하여 $e(a) = (a-1)/2$, $f(a) = (a^2-1)/8$로 둔다. 홀수 $a, b$에 대하여 $e(ab) = e(a) + e(b) + 2e(a)e(b)$이고 $f(ab) = f(a) + f(b) + 8f(a)f(b)$인 것은 전개로 확인된다. 따라서 $e$와 $f$는 법 $2$에서 곱을 합으로 보낸다. ($f(a)$가 정수인 것은 $a$가 홀수일 때 $a^2 \equiv 1 \pmod{8}$이기 때문이다.)

$n = p_1 \cdots p_k$로 쓴다. 정의와 [§이차 잉여, ⁋따름정리 5](/ko/math/number_theory/quadratic_residues#cor5)의 소수 분모에 대한 결과에 의하여

$$\left(\frac{-1}{n}\right) = \prod_{i}(-1)^{e(p_i)} = (-1)^{\sum e(p_i)} = (-1)^{e(n)}$$

이고, 같은 방식으로 $(2/n) = \prod_i (-1)^{f(p_i)} = (-1)^{f(n)}$이다. 이것이 1, 2이다.

3을 보이자. $m = p_1 \cdots p_k$, $n = q_1 \cdots q_l$로 소인수분해하면 $\gcd(m, n) = 1$이므로 모든 $p_i$와 $q_j$는 서로 다른 홀수 소수이다. 정의에 의하여 $(m/n) = \prod_{i,j}(p_i/q_j)$, $(n/m) = \prod_{i,j}(q_j/p_i)$이므로 [정리 1](#thm1)에 의하여

$$\left(\frac{m}{n}\right)\left(\frac{n}{m}\right) = \prod_{i,j}(-1)^{e(p_i)e(q_j)} = (-1)^{\left(\sum_i e(p_i)\right)\left(\sum_j e(q_j)\right)} = (-1)^{e(m)e(n)}$$

이다. 마지막 등호는 $\sum_i e(p_i) \equiv e(m)$, $\sum_j e(q_j) \equiv e(n) \pmod{2}$에서 나온다.
:::

[명제 4](#prop4)의 3에서 $\gcd(m, n) > 1$이면 두 기호가 모두 $0$이어서 등식은 $0 = 0$으로 의미가 없다. 그러나 계산에서는 이 경우가 자연스럽게 걸러진다. 아래 알고리즘은 공약수가 있으면 분자가 $0$이 되는 데서 끝나고, 이때 기호의 값은 $0$이다.

### Jacobi 기호가 1인데 이차 잉여가 아닌 경우

Jacobi 기호를 Legendre 기호처럼 읽으면 틀린다. $n$이 합성수이면 $(a/n) = 1$이 $a$가 법 $n$의 이차 잉여임을 뜻하지 않는다. 한쪽 방향만 성립한다. $\gcd(a, n) = 1$이고 $x^2 \equiv a \pmod{n}$이 해를 가지면 각 소인수 $p_i$에 대하여 $x^2 \equiv a \pmod{p_i}$이므로 $(a/p_i) = 1$이고 따라서 $(a/n) = 1$이다. 대우로 $(a/n) = -1$이면 $a$는 법 $n$의 이차 비잉여이다. 역은 성립하지 않는다.

::: 예시 5 ($n = 15$)
$n = 15 = 3 \cdot 5$에서 $(2/15) = (2/3)(2/5) = (-1)(-1) = 1$이다. 그런데 법 $15$에서 reduced residue class $1, 2, 4, 7, 8, 11, 13, 14$의 제곱은 차례로 $1, 4, 1, 4, 4, 1, 4, 1$이므로 이차 잉여는 $1, 4$뿐이고 $2$는 이차 잉여가 아니다. 법 $15$에서 $x^2 \equiv 2$는 이미 법 $3$에서 $x^2 \equiv 2$로 환원되어 해가 없다. $(a/15) = 1$인 $a$는 $1, 2, 4, 8$인데, $a$가 두 소인수에서 모두 비잉여이면 두 $-1$이 곱해져 기호가 $1$이 되고 이차 잉여성은 [§합동식과 중국인의 나머지 정리, ⁋정리 8](/ko/math/number_theory/chinese_remainder_theorem#thm8)에 의하여 소인수별로 따로 판정되기 때문이다.
:::

일반적으로 $(a/n) = 1$인 $a$는 이차 비잉여인 소인수 성분이 짝수 개 있다는 것만 알려 준다. 이차 잉여성 자체를 판정하려면 $n$의 소인수 각각에서 $(a/p_i) = 1$인지 보아야 한다. 분모가 소수일 때만 $(a/n) = 1$이 이차 잉여성과 동치이다.

## 호제법형 계산

[명제 4](#prop4)의 세 성질과 $a \bmod n$에의 의존성으로 $(a/n)$을 [§나눗셈과 유클리드 호제법, ⁋정리 6](/ko/math/number_theory/euclidean_algorithm#thm6)과 같은 모양으로 계산할 수 있다. $n$이 홀수인 양의 정수일 때 다음을 반복한다. 먼저 $a$를 $n$으로 나눈 나머지로 바꾼다. 음수인 $a$는 이 단계에서 양수가 되므로 $(-1/n)$을 따로 다룰 필요가 없다. 나머지가 $0$이면 $n = 1$일 때 값은 $1$이고, 그렇지 않으면 $0$이다. 다음으로 $a = 2^k a'$ ($a'$는 홀수)로 쓰고 $(2/n)^k$을 [명제 4](#prop4)의 2로 처리한다. $a' = 1$이면 끝난다. $a' > 1$이면 [명제 4](#prop4)의 3으로 $(a'/n) = \pm(n/a')$로 뒤집는다. 부호는 $a' \equiv n \equiv 3 \pmod{4}$일 때만 $-$이다. 뒤집은 뒤에는 분모가 $a'$로 줄어 있으므로 처음으로 돌아간다.

분자를 소인수분해하는 단계는 $2$의 거듭제곱을 떼는 것뿐이고, 홀수 부분은 어떤 소수의 곱인지 알 필요가 없다. 단계 수는 분모의 로그에 비례한다. 분모가 $n_0 > n_1 > n_2 > \cdots$로 줄 때 $n_2 \le n_0 \bmod n_1 < n_0/2$이기 때문이다. 뒤의 부등식은 임의의 $x \ge y$에 대하여 $x \bmod y < x/2$라는 호제법의 표준적 사실이다.

::: 예시 6 ($(3141/7919)$)
$7919$는 소수이므로 $(3141/7919)$는 $3141$이 법 $7919$의 이차 잉여인지를 알려 준다. $3141 \equiv 1$, $7919 \equiv 3 \pmod{4}$이므로 [명제 4](#prop4)의 3에 의하여 뒤집을 때 부호가 바뀌지 않는다.

$$\begin{aligned}
\left(\frac{3141}{7919}\right) &= \left(\frac{7919}{3141}\right) = \left(\frac{1637}{3141}\right) = \left(\frac{3141}{1637}\right) = \left(\frac{1504}{1637}\right) \\
&= \left(\frac{2}{1637}\right)^5\left(\frac{47}{1637}\right) = -\left(\frac{47}{1637}\right) = -\left(\frac{1637}{47}\right) = -\left(\frac{39}{47}\right) \\
&= \left(\frac{47}{39}\right) = \left(\frac{8}{39}\right) = \left(\frac{2}{39}\right)^3 = 1
\end{aligned}$$

이다. 둘째 등호는 $7919 - 2 \cdot 3141 = 1637$, 넷째 등호는 $3141 - 1637 = 1504 = 2^5 \cdot 47$, 여섯째 등호의 부호는 $1637 \equiv 5 \pmod{8}$에서 $(2/1637) = -1$, 일곱째 등호는 $1637 \equiv 1 \pmod{4}$와 $1637 - 34 \cdot 47 = 39$에서 나온다. 아홉째 등호에서 $39 \equiv 47 \equiv 3 \pmod{4}$이므로 부호가 한 번 바뀌고, 마지막은 $39 \equiv 7 \pmod{8}$이라 $(2/39) = 1$이다. 따라서 $3141$은 법 $7919$의 이차 잉여이다. 실제로 $3047^2 \equiv 3141 \pmod{7919}$이다.

이 계산에서 소인수분해한 것은 $1504$에서 뗀 $2^5$뿐이다. 중간에 나온 $3141 = 3^2 \cdot 349$ 같은 수의 소인수를 구할 필요는 없었다.
:::

호제법형 계산이 알려 주는 것은 $(a/p)$의 값이지 제곱근이 아니다. $x^2 \equiv 3141 \pmod{7919}$의 해 $x = 3047$은 이 계산에서 얻어지지 않으며, 그것을 구하는 일은 별개의 문제이다.

## 이차 잉여인 소수의 분류

서두에서 관찰한 $q = 3$의 경우를 증명하자. 이 계산은 [정리 1](#thm1)의 부호 규칙이 실제로 어떻게 작동하는지를 보여 준다.

::: 예시 7 ($3$과 $5$가 이차 잉여인 소수)
$p > 3$인 소수에 대하여 [정리 1](#thm1)에 의하여 $(3/p) = (-1)^{\frac{p-1}{2}}(p/3)$이다. $(p/3)$은 $p \equiv 1 \pmod{3}$이면 $1$, $p \equiv 2 \pmod{3}$이면 $-1$이고, $(-1)^{(p-1)/2}$은 $p \equiv 1 \pmod{4}$이면 $1$, $p \equiv 3 \pmod{4}$이면 $-1$이다. $p$를 $12$로 나눈 나머지 $1, 5, 7, 11$에 대하여 두 값을 표로 만들면 $(3/p)$는 차례로 $1 \cdot 1 = 1$, $1 \cdot (-1) = -1$, $(-1) \cdot 1 = -1$, $(-1)(-1) = 1$이다. 따라서

$$\left(\frac{3}{p}\right) = 1 \iff p \equiv \pm 1 \pmod{12}$$

이다. $5 \equiv 1 \pmod{4}$이므로 [정리 1](#thm1)에 의하여 $(5/p) = (p/5)$이고, 법 $5$의 이차 잉여가 $1, 4$이므로

$$\left(\frac{5}{p}\right) = 1 \iff p \equiv \pm 1 \pmod{5}$$

이다. 가령 $p = 29 \equiv -1 \pmod{5}$에서 $11^2 = 121 \equiv 5$이고, $p = 13 \equiv 3 \pmod{5}$에서 $5$는 이차 비잉여이다.
:::

같은 방식으로 임의의 홀수 소수 $q$에 대하여 $(q/p) = 1$인 소수 $p$는 $4q$를 법으로 하는 합동류로 기술되며, 계산은 $(p/q)$를 법 $q$의 이차 잉여표에서 읽고 $p \bmod 4$로 부호를 결정하는 것으로 끝난다.

---

**참고문헌**

**[OL]** 오정환·이준복, *기초 정수론*, 경문사, 2012.
