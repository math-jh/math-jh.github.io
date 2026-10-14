---
title: "산술적 함수와 뫼비우스 반전"
description: "약수의 개수 τ, 약수의 합 σ, 오일러 φ, 뫼비우스 함수 μ를 multiplicative function의 틀에서 다루고, Dirichlet convolution의 대수 구조를 증명한다. 이를 바탕으로 뫼비우스 반전 공식과 Σφ(d)=n을 얻고, 짝수 완전수에 대한 Euclid–Euler 정리를 증명한다."
excerpt: "τ, σ, φ, μ와 Dirichlet convolution, 뫼비우스 반전, 짝수 완전수"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/arithmetic_functions
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 6

published: false

---

양의 정수 $n$의 약수의 개수, 약수의 합, $n$ 이하의 서로소인 정수의 개수처럼 정수론에서 계산하는 양은 대부분 양의 정수를 변수로 하는 함수이다. 이런 함수들은 $n$의 소인수분해와 매우 규칙적으로 맞물리고, 약수에 대한 합이라는 연산으로 서로 연결된다. 이 글에서는 그 구조를 정리하고, 약수에 대한 합을 되돌리는 뫼비우스 반전 공식과 그 응용으로 짝수 완전수의 분류를 증명한다.

## Multiplicative function

::: 정의 1
양의 정수 전체에서 정의된 복소수값 함수를 *산술적 함수<sub>arithmetic function</sub>*라 한다. 산술적 함수 $f$가 항등적으로 $0$이 아니고, $\gcd(m,n)=1$인 모든 양의 정수 $m,n$에 대하여 $f(mn)=f(m)f(n)$을 만족하면 *multiplicative function<sub>곱셈적 함수</sub>*라 한다.
:::

$f$가 multiplicative이면 $f(1)=1$이다. $f(n)\neq 0$인 $n$을 하나 잡고 $f(n)=f(n\cdot 1)=f(n)f(1)$을 쓰면 된다. 항등적으로 $0$인 함수를 제외하는 이유가 이것이다. 또 $n=p_1^{e_1}\cdots p_r^{e_r}$의 소인수분해에서 $p_i^{e_i}$들은 서로 소이므로, 귀납법으로 $f(n)=f(p_1^{e_1})\cdots f(p_r^{e_r})$을 얻는다. 따라서 multiplicative function은 소수의 거듭제곱에서의 값으로 완전히 결정되고, 소수 거듭제곱에서의 값을 임의로 주어도 이 곱으로 정의한 함수는 multiplicative이다. 이 정의가 잘 정의됨은 [§소수와 산술의 기본정리, ⁋정리 4](/ko/math/number_theory/primes#thm4){: data-lid="np3na" }의 소인수분해의 유일성이 보장한다.

정의에서 $\gcd(m,n)=1$이라는 가정은 빠질 수 없다. 서로소가 아닌 경우에 곱셈 공식이 성립하는 함수는 *completely multiplicative*라 부르는데, 뒤에서 다룰 함수들은 대부분 여기에 해당하지 않는다.

::: 예시 2
다음 세 함수는 각각 정의 $\tau(n)=\#\{d\ge 1:d\mid n\}$, $\sigma(n)=\sum_{d\mid n}d$, $\varphi(n)=\#\{1\le k\le n:\gcd(k,n)=1\}$로 주어지며, 모두 $\gcd(m,n)=1$ 조건 없이는 곱셈 공식이 깨진다. $\tau(2\cdot 2)=3\neq 4=\tau(2)^2$, $\sigma(2\cdot 2)=7\neq 9=\sigma(2)^2$, $\varphi(2\cdot 2)=2\neq 1=\varphi(2)^2$이다.
:::

## Dirichlet convolution

약수에 대한 합으로 정의되는 함수들을 한꺼번에 다루기 위해 산술적 함수 사이의 연산을 하나 도입한다.

::: 정의 3
두 산술적 함수 $f,g$의 *Dirichlet convolution<sub>디리클레 합성곱</sub>* $f\ast g$를

$$(f\ast g)(n)=\sum_{d\mid n}f(d) g(n/d)$$

으로 정의한다. 합은 $n$의 양의 약수 $d$ 전체에 대해 취한다.
:::

합성곱의 곱셈 보존성을 보이려면 서로소인 $m,n$에 대하여 $mn$의 약수가 어떻게 생겼는지 알아야 한다.

::: 보조정리 4
$\gcd(m,n)=1$이면 $(a,b)\mapsto ab$는 $\{a: a\mid m\}\times\{b:b\mid n\}$에서 $\{d:d\mid mn\}$으로의 전단사이다. 또 이때 $\gcd(a,b)=1$이고 $\gcd(m/a,n/b)=1$이다.
:::

::: 증명
$a\mid m$, $b\mid n$이면 $ab\mid mn$이므로 사상이 정의된다. $\gcd(a,b)$는 $m$과 $n$의 공약수이므로 $1$이고, 같은 이유로 $\gcd(m/a,n/b)=1$이다.

단사성을 보인다. $ab=a'b'$이고 $a,a'\mid m$, $b,b'\mid n$이라 하자. $a\mid a'b'$이고 $\gcd(a,b')=1$이므로 [§나눗셈과 유클리드 호제법, ⁋명제 11](/ko/math/number_theory/euclidean_algorithm#prop11){: data-lid="dykzv" }(서로소인 수가 곱을 나누면 나머지 인수를 나눈다)에 의하여 $a\mid a'$이다. 같은 논증을 $a,a'$의 역할을 바꾸어 적용하면 $a'\mid a$이므로 $a=a'$이고, 따라서 $b=b'$이다.

전사성을 보인다. $d\mid mn$이라 하고 $a=\gcd(d,m)$, $b=\gcd(d,n)$이라 하자. $a\mid m$, $b\mid n$이므로 $\gcd(a,b)=1$이고, $a\mid d$, $b\mid d$이므로 $ab\mid d$이다. 반대로 $d/a$와 $m/a$는 서로소이고 $d/a\mid (m/a) n$이므로 [§나눗셈과 유클리드 호제법, ⁋명제 11](/ko/math/number_theory/euclidean_algorithm#prop11){: data-lid="j5e2e" }에 의하여 $d/a\mid n$이다. $d/a$는 $d$의 약수이기도 하므로 $d/a\mid\gcd(d,n)=b$이다. 즉 $d\mid ab$이다. 두 방향을 합치면 $d=ab$이다.
:::

::: 명제 5
$f,g$가 multiplicative function이면 $f\ast g$도 multiplicative function이다.
:::

::: 증명
$\gcd(m,n)=1$이라 하자. [보조정리 4](#lem4){: data-lid="qjvpo" }에 의하여 $mn$의 약수는 $d=ab$ ($a\mid m$, $b\mid n$)로 유일하게 적히고, $\gcd(a,b)=1$, $\gcd(m/a,n/b)=1$이므로 $f$와 $g$의 곱셈성을 각각 적용할 수 있다.

$$\begin{aligned}
(f\ast g)(mn)&=\sum_{a\mid m}\sum_{b\mid n}f(ab) g\left(\frac{m}{a}\cdot\frac{n}{b}\right)\\
&=\sum_{a\mid m}\sum_{b\mid n}f(a)g\left(\frac{m}{a}\right)f(b)g\left(\frac{n}{b}\right)\\
&=(f\ast g)(m) (f\ast g)(n)
\end{aligned}$$

또 $(f\ast g)(1)=f(1)g(1)=1$이므로 $f\ast g$는 항등적으로 $0$이 아니다.
:::

상수함수 $\mathbf 1(n)=1$과 항등함수 $\id(n)=n$은 completely multiplicative이므로 multiplicative이다. 정의에서 곧바로 $\tau=\mathbf 1\ast\mathbf 1$, $\sigma=\mathbf 1\ast\id$임을 알 수 있고, 따라서 다음을 얻는다.

::: 명제 6
$\tau$와 $\sigma$는 multiplicative function이고, $n=p_1^{e_1}\cdots p_r^{e_r}$이면

$$\tau(n)=\prod_{i=1}^r(e_i+1),\quad \sigma(n)=\prod_{i=1}^r\frac{p_i^{e_i+1}-1}{p_i-1}$$

이다.
:::

::: 증명
곱셈성은 [명제 5](#prop5){: data-lid="o6qga" }에서 나온다. 소수 $p$의 거듭제곱 $p^e$의 약수는 $1,p,\dots,p^e$이므로 $\tau(p^e)=e+1$이고 $\sigma(p^e)=1+p+\cdots+p^e=(p^{e+1}-1)/(p-1)$이다. 소수 거듭제곱에서의 값으로 곱을 취하면 된다.
:::

가령 $360=2^3\cdot 3^2\cdot 5$이면 $\tau(360)=4\cdot3\cdot2=24$이고 $\sigma(360)=15\cdot13\cdot6=1170$이다.

## Convolution의 대수 구조

$n=1$에서만 $1$이고 그 외에서는 $0$인 함수를 $\varepsilon$이라 쓰자. $\varepsilon$은 multiplicative function이다.

::: 명제 7
산술적 함수 전체의 집합에서 Dirichlet convolution은 교환법칙과 결합법칙을 만족하고 $\varepsilon$이 항등원이다.
:::

::: 증명
$d\mapsto n/d$가 $n$의 약수 전체를 자기 자신 위로 보내는 전단사이므로

$$(f\ast g)(n)=\sum_{d\mid n}f(d) g(n/d)=\sum_{d\mid n}f(n/d) g(d)=(g\ast f)(n)$$

이다. 결합법칙은 양변이 같은 합이라는 사실에서 나온다. $((f\ast g)\ast h)(n)$은 $de=n$인 쌍에 대한 합 $\sum_{de=n}\bigl(\sum_{ab=d}f(a)g(b)\bigr)h(e)$이고, 이는 $abe=n$인 양의 정수 순서쌍 $(a,b,e)$ 전체에 대한 $\sum f(a)g(b)h(e)$와 같다. $(f\ast(g\ast h))(n)$도 같은 방식으로 같은 합이 된다. 끝으로 $\varepsilon(n/d)$는 $d=n$일 때만 $1$이므로 $(f\ast\varepsilon)(n)=f(n)$이다.
:::

이제 어떤 함수가 합성곱에 대한 역원을 가지는지 판정한다.

::: 명제 8
산술적 함수 $f$가 $f\ast g=\varepsilon$인 $g$를 가질 필요충분조건은 $f(1)\neq 0$이다. 이때 $g$는 유일하며 $f^{-1}$로 쓴다. 또 $f$가 multiplicative function이면 $f^{-1}$도 multiplicative function이다.
:::

::: 증명
$(f\ast g)(1)=f(1)g(1)$이므로 $f\ast g=\varepsilon$이면 $f(1)\neq 0$이다. 역으로 $f(1)\neq 0$이라 하자. $f\ast g=\varepsilon$은 $n=1$에서 $g(1)=1/f(1)$을, $n>1$에서

$$f(1) g(n)+\sum_{d\mid n,\ d>1}f(d) g(n/d)=0$$

을 뜻한다. 두 번째 합에는 $n$보다 작은 인수 $n/d$에서의 $g$ 값만 나타나므로, 이 식은 $g(n)$을 $g(1),\dots,g(n-1)$로 표현한다. 따라서 $g$가 귀납적으로 존재한다. 유일성은 [명제 7](#prop7){: data-lid="30spf" }의 결합법칙에서 나온다. $g,g'$이 모두 역원이면 $g=g\ast(f\ast g')=(g\ast f)\ast g'=g'$이다.

$f$가 multiplicative이고 $g=f^{-1}$이라 하자. 소수 거듭제곱에서의 값 $g(p^e)$를 따라 정해지는 multiplicative function을 $h$라 하자. [명제 5](#prop5){: data-lid="a5bzs" }에 의하여 $f\ast h$는 multiplicative이고, $p^e$의 약수가 $p^i$ ($0\le i\le e$)뿐이므로 $(f\ast h)(p^e)=\sum_i f(p^i)h(p^{e-i})=\sum_i f(p^i)g(p^{e-i})=(f\ast g)(p^e)=\varepsilon(p^e)$이다. Multiplicative function은 소수 거듭제곱에서의 값으로 결정되므로 $f\ast h=\varepsilon$이고, 유일성에 의하여 $h=g$이다.
:::

## 뫼비우스 함수와 반전 공식

함수 $\mathbf 1$은 $\mathbf 1(1)=1$이므로 [명제 8](#prop8){: data-lid="5d778" }에 의하여 역원을 가진다. 그 역원을 명시적으로 쓰는 것이 다음 정의이다.

::: 정의 9
*뫼비우스 함수<sub>Möbius function</sub>* $\mu$를 $\mu(1)=1$, $n$이 어떤 소수의 제곱으로 나누어떨어지면 $\mu(n)=0$, $n$이 서로 다른 $k$개의 소수의 곱이면 $\mu(n)=(-1)^k$로 정의한다.
:::

$\gcd(m,n)=1$일 때 $mn$이 어떤 소수의 제곱으로 나누어떨어지는 것은 $m$ 또는 $n$이 그런 경우와 동치이고, $mn$이 서로 다른 소수의 곱이면 그 소수의 개수는 $m$과 $n$의 것의 합이다. 따라서 $\mu$는 multiplicative function이다.

::: 명제 10
$\mathbf 1\ast\mu=\varepsilon$이다. 즉 $n>1$이면 $\sum_{d\mid n}\mu(d)=0$이다.
:::

::: 증명
[명제 5](#prop5){: data-lid="ccfru" }에 의하여 $\mathbf 1\ast\mu$는 multiplicative function이므로 소수 거듭제곱에서만 확인하면 된다. $e\ge 1$에 대하여 $(\mathbf 1\ast\mu)(p^e)=\mu(1)+\mu(p)+\mu(p^2)+\cdots+\mu(p^e)=1-1+0+\cdots+0=0$이다.
:::

::: 정리 11 (뫼비우스 반전 공식)
산술적 함수 $f,g$에 대하여 다음 두 조건은 동치이다.

$$g(n)=\sum_{d\mid n}f(d)\quad(\forall n)\quad\iff\quad f(n)=\sum_{d\mid n}\mu(d) g(n/d)\quad(\forall n)$$
:::

::: 증명
첫째 조건은 $g=\mathbf 1\ast f$이고 둘째 조건은 $f=\mu\ast g$이다. 첫째 조건이 성립하면 [명제 7](#prop7){: data-lid="ionpd" }과 [명제 10](#prop10){: data-lid="78by9" }에 의하여 $\mu\ast g=\mu\ast(\mathbf 1\ast f)=(\mu\ast\mathbf 1)\ast f=\varepsilon\ast f=f$이다. 둘째 조건이 성립하면 같은 계산으로 $\mathbf 1\ast f=\mathbf 1\ast\mu\ast g=g$이다.
:::

반전 공식의 합은 $\sum_{d\mid n}\mu(n/d)g(d)$로 적어도 같다. 교환법칙 때문이다. 한편 $f$는 임의의 산술적 함수이고 multiplicative일 필요가 없다는 점에 주의한다. multiplicative인 경우에는 다음이 추가로 성립한다.

::: 따름정리 12
산술적 함수 $f$에 대하여 $f$가 multiplicative function인 것과 $\mathbf 1\ast f$가 multiplicative function인 것은 동치이다.
:::

::: 증명
($\Rightarrow$)은 [명제 5](#prop5){: data-lid="fqa61" }이다. ($\Leftarrow$)에서는 $g=\mathbf 1\ast f$가 multiplicative라 하자. $\mu$는 multiplicative이므로 [정리 11](#thm11){: data-lid="s9ain" }에 의한 $f=\mu\ast g$가 [명제 5](#prop5){: data-lid="c8tv5" }에 의하여 multiplicative이다.
:::

## φ와 약수에 대한 합

$\varphi(n)$은 $1\le k\le n$ 중 $n$과 서로소인 $k$의 개수이다.

::: 명제 13
모든 양의 정수 $n$에 대하여 $\sum_{d\mid n}\varphi(d)=n$이다.
:::

::: 증명
$\{1,\dots,n\}$의 각 원소 $k$를 $\gcd(k,n)$의 값에 따라 분류한다. $n$의 약수 $d$에 대하여 $\gcd(k,n)=n/d$인 $k$는 $k=(n/d)j$ ($1\le j\le d$)로 적히고, 이때 $\gcd(k,n)=(n/d)\gcd(j,d)$이므로 조건은 $\gcd(j,d)=1$과 같다. 따라서 이러한 $k$는 정확히 $\varphi(d)$개이다. 분류된 개수를 모두 더하면 $n=\sum_{d\mid n}\varphi(d)$이다.
:::

이는 $\mathbf 1\ast\varphi=\id$를 말한다. [정리 11](#thm11){: data-lid="tlh5o" }을 적용하면 $\varphi=\mu\ast\id$를 얻는다. $\mu$와 $\id$가 multiplicative이므로 [명제 5](#prop5){: data-lid="xjp30" }에 의하여 $\varphi$는 multiplicative function이다. 소수 거듭제곱에서는 $p^e$ 이하의 정수 중 $p$와 서로소가 아닌 것이 $p$의 배수 $p^{e-1}$개이므로 $\varphi(p^e)=p^e-p^{e-1}$이다. ($\mu\ast\id$로 계산해도 $\mu(1)p^e+\mu(p)p^{e-1}=p^e-p^{e-1}$로 같다.) 이를 정리하면 다음이 된다.

::: 따름정리 14
$\varphi$는 multiplicative function이고, $n=p_1^{e_1}\cdots p_r^{e_r}$이면

$$\varphi(n)=\prod_{i=1}^rp_i^{e_i-1}(p_i-1)=n\prod_{p\mid n}\left(1-\frac1p\right)$$

이다.
:::

$\varphi(360)=\varphi(8)\varphi(9)\varphi(5)=4\cdot6\cdot4=96$이다. 또한 $\varphi=\mu\ast\id$로부터 $\varphi(n)=\sum_{d\mid n}\mu(d) n/d$를 얻고, 가령 $n=12$에서 $12-6-4+2=4$로 $\varphi(12)=4$와 일치한다. ($\mu(4)=\mu(12)=0$이다.)

반전 공식은 $\mu$가 약수에 대한 합을 걸러내는 역할을 한다는 점에서 다른 계수 문제에도 쓰인다. 다음 예시는 [명제 10](#prop10){: data-lid="qlru9" }을 약수가 아닌 공약수에 직접 적용한다.

::: 예시 15
$N(n)$을 $1\le a,b\le n$이면서 $\gcd(a,b)=1$인 순서쌍 $(a,b)$의 개수라 하자. [명제 10](#prop10){: data-lid="ac42h" }에 의하여 $\sum_{d\mid\gcd(a,b)}\mu(d)$는 $\gcd(a,b)=1$이면 $1$이고 아니면 $0$이므로

$$N(n)=\sum_{a,b\le n}\sum_{d\mid\gcd(a,b)}\mu(d)=\sum_{d=1}^n\mu(d)\#\{(a,b):d\mid a,\ d\mid b\}=\sum_{d=1}^n\mu(d)\lfloor n/d\rfloor^2$$

이다. $n=10$이면 $d=4,8,9$는 $\mu(d)=0$이므로 $100-25-9-4+1-1+1=63$이다. 한편 $\gcd(a,b)=1$인 쌍은 $a=b=1$을 제외하면 $a<b$ 또는 $a>b$이고, $a<b$인 쌍은 $b$를 고정할 때 $\varphi(b)$개이므로 $N(n)=2\sum_{k=1}^n\varphi(k)-1$이다. $\varphi(1),\dots,\varphi(10)=1,1,2,2,4,2,6,4,6,4$의 합이 $32$이므로 $2\cdot32-1=63$으로 두 계산이 일치한다.
:::

## 완전수

자기 자신을 제외한 약수의 합이 자기 자신과 같은 양의 정수, 즉 $\sigma(n)=2n$인 $n$을 *완전수<sub>perfect number</sub>*라 한다. $6=1+2+3$, $28=1+2+4+7+14$가 가장 작은 예이다. 짝수 완전수는 다음과 같이 완전히 분류된다. 홀수 완전수는 존재 여부가 알려져 있지 않다.

::: 정리 16 (Euclid–Euler)
짝수 $n$이 완전수인 것은 어떤 양의 정수 $p$에 대하여 $2^p-1$이 소수이고 $n=2^{p-1}(2^p-1)$인 것과 동치이다.
:::

::: 증명
($\Leftarrow$) $q=2^p-1$이 소수라 하자. $q$는 홀수이므로 $\gcd(2^{p-1},q)=1$이고, [명제 6](#prop6){: data-lid="sctfd" }과 곱셈성에 의하여 $\sigma(n)=\sigma(2^{p-1})\sigma(q)=(2^p-1)(q+1)=(2^p-1)2^p=2n$이다.

($\Rightarrow$) $n$이 짝수 완전수라 하고 $n=2^km$ ($k\ge1$, $m$은 홀수)이라 하자. $\sigma$의 곱셈성과 [명제 6](#prop6){: data-lid="nlvcu" }에 의하여

$$(2^{k+1}-1) \sigma(m)=\sigma(n)=2n=2^{k+1}m$$

이다. $2^{k+1}-1$과 $2^{k+1}$의 공약수는 두 수의 차 $1$을 나누므로 서로소이고, [§나눗셈과 유클리드 호제법, ⁋명제 11](/ko/math/number_theory/euclidean_algorithm#prop11){: data-lid="fg8wr" }에 의하여 $2^{k+1}-1\mid m$이다. $m=(2^{k+1}-1)t$라 쓰면 위 식에서 $\sigma(m)=2^{k+1}t$이다. $k\ge1$이므로 $2^{k+1}-1\ge3$이고, 따라서 $t<m$이다. $m$의 서로 다른 약수 $m$과 $t$가 있으므로 $\sigma(m)\ge m+t=2^{k+1}t$이고, 위에서 등호가 성립하므로 $m$의 약수는 $m$과 $t$뿐이다. $1$도 $m$의 약수이므로 $t=1$이어야 하고, 약수가 $1$과 $m$뿐이므로 $m=2^{k+1}-1$은 소수이다. $p=k+1$로 두면 $n=2^{p-1}(2^p-1)$이다.
:::

$2^p-1$이 소수이려면 $p$ 자신이 소수여야 한다. $p=ab$ ($a,b>1$)이면 $2^a-1$이 $2^{ab}-1$을 나누기 때문이다. $p=2,3,5,7$에서 $2^p-1=3,7,31,127$이 모두 소수이므로 $6,28,496,8128$이 완전수이다. $p=11$에서는 $2^{11}-1=23\cdot89$이 합성수이다. 이 형태의 소수 $2^p-1$을 *Mersenne prime*이라 부른다.

---

**참고문헌**

**[OL]** 오정환·이준복, *기초 정수론*, 경문사, 2012.
