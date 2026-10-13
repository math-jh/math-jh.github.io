---
title: "원시근"
description: "법 n에 대한 정수의 위수를 정의하고, 소수 법에서 원시근이 존재함을 Lagrange 정리와 phi 함수의 약수 합 항등식으로 증명한다. 소수 거듭제곱 법의 원시근, 원시근이 존재하는 법의 완전한 분류, 그리고 지표를 이용한 거듭제곱 합동식의 풀이를 다룬다."
excerpt: "위수, 소수 법과 소수 거듭제곱 법의 원시근, 원시근이 존재하는 법의 분류, 지표"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/primitive_roots
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 7

published: false

---

[§페르마 소정리와 오일러 정리, ⁋정리 3](/ko/math/number_theory/euler_theorem#thm3)에 의하여 $\gcd(a,n)=1$이면 $a^{\varphi(n)}\equiv 1 \pmod n$이다. 이 지수 $\varphi(n)$이 $a$의 거듭제곱이 $1$로 돌아오는 가장 작은 지수인지는 $a$와 $n$에 따라 다르다. 법 $7$에서 $2^3=8\equiv 1$이므로 $2$의 거듭제곱은 $2,4,1$만 반복하고, $\varphi(7)=6$에는 이르지 못한다. 반면 $3$의 거듭제곱은 $3,2,6,4,5,1$로 법 $7$의 reduced residue class 여섯 개를 모두 지난다. 이 글에서는 이 차이를 *위수*로 정량화하고, 후자의 현상이 일어나는 법 $n$이 어떤 것인지를 결정한다.

## 위수

::: 정의 1
$\gcd(a,n)=1$일 때 $a^k\equiv 1 \pmod n$을 만족하는 가장 작은 양의 정수 $k$를 $a$의 법 $n$에 대한 *위수<sub>order</sub>*라 하고 $\ord_n(a)$로 적는다. $\ord_n(a)=\varphi(n)$일 때 $a$를 법 $n$의 *원시근<sub>primitive root</sub>*이라 한다.
:::

[§페르마 소정리와 오일러 정리, ⁋정리 3](/ko/math/number_theory/euler_theorem#thm3)에 의하여 위수는 항상 존재하고 $\varphi(n)$ 이하이다. 법 $7$에서 $\ord_7(2)=3$이고 $\ord_7(3)=6$이므로 $3$은 원시근이다. 위수는 다음과 같이 지수의 나눗셈을 통제한다.

::: 명제 2
$\gcd(a,n)=1$이고 $d=\ord_n(a)$이면, 양의 정수 $k$에 대하여 $a^k\equiv 1 \pmod n$인 것은 $d\mid k$인 것과 동치이다. 특히 $d\mid \varphi(n)$이다.
:::

::: 증명
$d\mid k$이면 $a^k=(a^d)^{k/d}\equiv 1$이다. 거꾸로 $a^k\equiv 1$이라 하고 $k=dq+r$ ($0\le r<d$)로 나누면 $a^k=(a^d)^q a^r\equiv a^r$이므로 $a^r\equiv 1$이다. $d$가 $a^d\equiv 1$을 만족하는 최소의 양의 정수이고 $0\le r<d$이므로 $r=0$이다. 마지막 주장은 [§페르마 소정리와 오일러 정리, ⁋정리 3](/ko/math/number_theory/euler_theorem#thm3)의 $a^{\varphi(n)}\equiv 1$에 앞의 동치를 적용한 것이다.
:::

::: 명제 3
$\gcd(a,n)=1$이고 $d=\ord_n(a)$이면 양의 정수 $k$에 대하여
$$\ord_n(a^k)=\frac{d}{\gcd(d,k)}$$
이다. 특히 $\ord_n(a^k)=d$인 것은 $\gcd(d,k)=1$인 것과 동치이다.
:::

::: 증명
$g=\gcd(d,k)$로 두고 $d=gd'$, $k=gk'$ ($\gcd(d',k')=1$)로 적는다. [명제 2](#prop2)에 의하여 $(a^k)^m\equiv 1$인 것은 $d\mid km$인 것과 동치이고, 이는 $d'\mid k'm$과 동치이다. $\gcd(d',k')=1$이므로 이는 다시 $d'\mid m$과 동치이다. 따라서 $(a^k)^m\equiv 1$을 만족하는 가장 작은 양의 정수 $m$은 $d'=d/g$이다.
:::

위수가 알려진 경우 원시근 여부를 소수 몇 개에 대한 검사로 판정할 수 있다.

::: 명제 4
$\gcd(g,n)=1$이라 하자. $g$가 법 $n$의 원시근인 것은 $\varphi(n)$의 모든 소인수 $q$에 대하여 $g^{\varphi(n)/q}\not\equiv 1 \pmod n$인 것과 동치이다.
:::

::: 증명
$\varphi(n)/q<\varphi(n)$이므로 원시근이면 $g^{\varphi(n)/q}\not\equiv 1$이다. 거꾸로 $r=\ord_n(g)<\varphi(n)$이라 하자. [명제 2](#prop2)에 의하여 $r\mid\varphi(n)$이므로 $\varphi(n)/r>1$이고, 이것의 소인수 $q$를 하나 잡으면 $r\mid\varphi(n)/q$이다. 다시 [명제 2](#prop2)에 의하여 $g^{\varphi(n)/q}\equiv 1$이다.
:::

## 합동식의 근의 개수

소수 법에서 원시근의 존재를 보이기 위한 도구로 polynomial의 근의 개수에 대한 상한이 필요하다. 합동식의 해는 법에 대한 residue class 단위로 센다.

::: 정리 5 (Lagrange)
$p$가 소수이고 $f(x)=a_nx^n+\cdots+a_0$이 $p\nmid a_n$인 정수 계수 polynomial이면, 합동식 $f(x)\equiv 0 \pmod p$의 해는 법 $p$에 대하여 합동이 아닌 것이 많아야 $n$개이다.
:::

::: 증명
$n$에 대한 귀납법을 쓴다. $n=0$이면 $f$는 $p$의 배수가 아닌 상수이므로 해가 없다. $n\ge 1$이고 $n-1$까지 성립한다고 하자. 해가 없으면 증명할 것이 없으므로 해 $a$가 있다고 하자. $x^i-a^i$는 $x-a$로 나누어떨어지므로 $f(x)-f(a)=(x-a)h(x)$인 정수 계수 polynomial $h$가 있고, $h$의 차수는 $n-1$, 최고차 계수는 $a_n$이다. $f(a)\equiv 0$이므로 $f(x)\equiv (x-a)h(x) \pmod p$이다. $b\not\equiv a$가 또 하나의 해이면 $p\mid (b-a)h(b)$이고 $p\nmid b-a$이며 $p$가 소수이므로 $p\mid h(b)$이다. 귀납 가정에 의하여 $h(x)\equiv 0$의 해는 법 $p$에서 많아야 $n-1$개이므로, $f$의 해는 $a$를 포함하여 많아야 $n$개이다.
:::

$p$가 소수라는 가정은 필수이다. 합성수 법에서는 해가 차수보다 많을 수 있다. 법 $8$에서 $x^2\equiv 1$의 해는 $1,3,5,7$로 네 개이고, 법 $15$에서도 $x^2\equiv 1$의 해는 $1,4,11,14$로 네 개이다.

## 소수 법의 원시근

::: 정리 6 (소수 법의 원시근)
$p$가 소수이면 법 $p$의 원시근이 존재하고, 그 개수는 $\varphi(p-1)$이다.
:::

::: 증명
$p-1$의 약수 $d$에 대하여 $\psi(d)$를 법 $p$의 reduced residue class 중 위수가 $d$인 것의 개수라 하자. [명제 2](#prop2)에 의하여 모든 reduced residue class의 위수는 $p-1$의 약수이므로 $\sum_{d\mid p-1}\psi(d)=p-1$이다.

$\psi(d)\ge 1$이라 하고 위수가 $d$인 $a$를 하나 잡자. $a^0,a^1,\ldots,a^{d-1}$은 위수의 정의에 의하여 법 $p$에서 서로 다르고, 모두 $(a^i)^d=(a^d)^i\equiv 1$이므로 $x^d-1\equiv 0$의 해이다. [정리 5](#thm5)에 의하여 이 합동식의 해는 많아야 $d$개이므로 이 $d$개가 해 전부이다. 위수가 $d$인 원소는 $x^d\equiv 1$의 해이므로 $a^i$ 꼴이고, [명제 3](#prop3)에 의하여 $a^i$의 위수가 $d$인 것은 $\gcd(i,d)=1$인 것과 동치이다. 이런 $i$ ($0\le i<d$)는 $\varphi(d)$개이므로 $\psi(d)=\varphi(d)$이다.

따라서 모든 약수 $d$에 대하여 $\psi(d)\le\varphi(d)$이다. 한편 [§산술적 함수와 뫼비우스 반전, ⁋명제 13](/ko/math/number_theory/arithmetic_functions#prop13)에 의하여 $\sum_{d\mid p-1}\varphi(d)=p-1=\sum_{d\mid p-1}\psi(d)$이다. 항마다 부등식이 성립하는데 합이 같으므로 모든 $d$에 대하여 $\psi(d)=\varphi(d)$이다. $d=p-1$인 경우가 원시근의 개수 $\varphi(p-1)\ge 1$을 준다.
:::

증명에서 [정리 5](#thm5)가 쓰이는 곳은 위수가 $d$인 원소가 $\varphi(d)$개를 넘을 수 없다는 부분이다. 합성수 법에서는 이 부분이 무너지고, 실제로 원시근이 존재하지 않는 법이 있음을 아래에서 본다. 증명은 존재만을 보장하고 원시근을 구하는 방법을 주지 않는다. 구체적인 법에서는 [명제 4](#prop4)로 후보를 검사한다.

::: 예시 7 (법 13의 원시근)
$\varphi(13)=12=2^2\cdot 3$이므로 [명제 4](#prop4)에 의하여 $g^6\not\equiv 1$과 $g^4\not\equiv 1$만 확인하면 된다. $g=2$에 대하여 $2^6=64\equiv 12$, $2^4=16\equiv 3$이므로 $2$는 법 $13$의 원시근이다. 반면 $g=3$은 $3^3=27\equiv 1$이어서 위수가 $3$이다. [명제 3](#prop3)에 의하여 $2^k$가 원시근인 것은 $\gcd(k,12)=1$일 때이므로 $k=1,5,7,11$이고, 법 $13$의 원시근은 $2,\ 2^5\equiv 6,\ 2^7\equiv 11,\ 2^{11}\equiv 7$의 네 개이다. 이는 $\varphi(12)=4$와 일치한다.
:::

일반적으로 원시근이 하나라도 존재하는 법에서는 개수가 소수 법과 같은 방식으로 정해진다.

::: 명제 8
법 $n$에 원시근 $g$가 존재하면 $g,g^2,\ldots,g^{\varphi(n)}$은 법 $n$의 reduced residue class 전체를 한 번씩 지나고, 원시근은 정확히 $\varphi(\varphi(n))$개이다.
:::

::: 증명
$1\le i<j\le\varphi(n)$에 대하여 $g^i\equiv g^j$이면 $\gcd(g,n)=1$이므로 $g^{j-i}\equiv 1$인데 $0<j-i<\varphi(n)=\ord_n(g)$이므로 모순이다. 따라서 $g^1,\ldots,g^{\varphi(n)}$은 서로 다른 reduced residue class $\varphi(n)$개이고, reduced residue class가 $\varphi(n)$개뿐이므로 전부이다. 각 reduced residue class는 $g^k$ ($1\le k\le\varphi(n)$) 꼴이고, [명제 3](#prop3)에 의하여 그 위수가 $\varphi(n)$인 것은 $\gcd(k,\varphi(n))=1$인 것과 동치이다. 이런 $k$는 $\varphi(\varphi(n))$개이다.
:::

## 소수 거듭제곱 법

소수 법의 원시근이 $p^2$, $p^3$, $\ldots$ 법의 원시근으로 올라가는지를 살펴본다. 아래 예시와 같이 법 $p$의 원시근이 법 $p^2$의 원시근이 아닐 수 있으므로 올림에서 후보를 골라야 한다.

::: 예시 9 (법 5의 원시근이 법 25의 원시근이 아닌 경우)
$7\equiv 2 \pmod 5$이고 $2$는 법 $5$의 원시근이므로 $7$도 법 $5$의 원시근이다. 그러나 $7^2=49\equiv -1 \pmod{25}$이므로 $7^4\equiv 1 \pmod{25}$이고, $\ord_{25}(7)=4<\varphi(25)=20$이다. 같은 residue class $2 \pmod 5$에 속하는 $2$와 $12$를 보면, $2^4=16\not\equiv 1$이고 $2^{10}=1024\equiv -1 \pmod{25}$이므로 [명제 4](#prop4)에 의하여 $2$는 법 $25$의 원시근이다. $12^4=20736\equiv 11 \pmod{25}$이고 $12\equiv 2 \pmod 5$이므로 $12$도 법 $25$의 원시근이 된다.
:::

예시의 현상을 다음 보조정리로 정확히 통제한다.

::: 보조정리 10
$p$가 홀수 소수이고 $a=1+pt$ ($p\nmid t$)이면, 모든 $j\ge 0$에 대하여 $a^{p^j}=1+p^{j+1}u_j$인 정수 $u_j$가 있고 $p\nmid u_j$이다.
:::

::: 증명
$j=0$이면 $u_0=t$이다. $a^{p^j}=1+p^{j+1}u$ ($p\nmid u$)라 하면
$$a^{p^{j+1}}=(1+p^{j+1}u)^p=1+p^{j+2}u+\sum_{i=2}^{p}\binom{p}{i}p^{i(j+1)}u^i$$
이다. $2\le i\le p-1$이면 $p\mid\binom{p}{i}$이므로 해당 항은 $p^{1+i(j+1)}$의 배수이고, $1+i(j+1)\ge 2j+3\ge j+3$이다. $i=p$인 항은 $p^{p(j+1)}$의 배수이고, $p\ge 3$이므로 $p(j+1)\ge 3j+3\ge j+3$이다. 따라서 합 전체가 $p^{j+3}$의 배수이고 $a^{p^{j+1}}=1+p^{j+2}(u+pw)$인 정수 $w$가 있다. $p\nmid u$이므로 $p\nmid u+pw$이다.
:::

$p=2$이면 $i=p=2$인 항의 지수가 $2(j+1)$이어서 $j=0$일 때 $j+3$ 이상이 되지 못한다. 이 때문에 법 $4$ 이상의 $2$의 거듭제곱 법은 홀수 소수 법과 다르게 행동한다.

::: 정리 11 (소수 거듭제곱 법의 원시근)
$p$가 홀수 소수이고 $k\ge 1$이면 법 $p^k$와 법 $2p^k$에 원시근이 존재한다.
:::

::: 증명
먼저 법 $p^k$를 다룬다. [정리 6](#thm6)에 의하여 법 $p$의 원시근 $g$가 있다. $g^{p-1}\equiv 1 \pmod{p^2}$이면 $g$ 대신 $g+p$를 택한다. $g+p$도 법 $p$의 원시근이고, 이항전개에서
$$(g+p)^{p-1}\equiv g^{p-1}+(p-1)g^{p-2}p\equiv 1-pg^{p-2} \pmod{p^2}$$
이므로 $p\nmid g$에 의하여 $(g+p)^{p-1}\not\equiv 1 \pmod{p^2}$이다. 따라서 $g$가 법 $p$의 원시근이고 $g^{p-1}\not\equiv 1 \pmod{p^2}$이라 가정할 수 있다. $g^{p-1}=1+pt$ ($p\nmid t$)로 적는다.

$r=\ord_{p^k}(g)$라 하자. $g^r\equiv 1 \pmod{p^k}$에서 $g^r\equiv 1 \pmod p$이므로 [명제 2](#prop2)에 의하여 $\ord_p(g)=p-1$이 $r$을 나눈다. 또 [명제 2](#prop2)에 의하여 $r\mid\varphi(p^k)=p^{k-1}(p-1)$이다. 따라서 $r=(p-1)p^s$ ($0\le s\le k-1$)이다. [보조정리 10](#lem10)을 $a=g^{p-1}$에 적용하면 $g^r=(g^{p-1})^{p^s}=1+p^{s+1}u_s$ ($p\nmid u_s$)이고, 이것이 $p^k$로 나누어떨어지는 $1$과 합동이려면 $s+1\ge k$이어야 한다. 즉 $s=k-1$이고 $r=\varphi(p^k)$이므로 $g$는 법 $p^k$의 원시근이다.

법 $2p^k$를 다룬다. $g$가 법 $p^k$의 원시근이면 $g+p^k$도 그러하고, 둘 중 하나는 홀수이므로 $g$가 홀수라 가정한다. $g$가 홀수이므로 모든 $m$에 대하여 $g^m-1$은 짝수이고, 따라서 $g^m\equiv 1 \pmod{2p^k}$인 것은 $g^m\equiv 1 \pmod{p^k}$인 것과 동치이다. 그러므로 $\ord_{2p^k}(g)=\ord_{p^k}(g)=\varphi(p^k)=\varphi(2p^k)$이다.
:::

## 원시근이 존재하는 법

법 $1,2,4$에는 각각 $1,1,3$이 원시근이다(법 $1$에서는 모든 정수가 원시근이다). [정리 11](#thm11)과 합하면 $n=1,2,4,p^k,2p^k$ ($p$는 홀수 소수)에서 원시근이 존재한다. 다음은 이것이 전부임을 말한다.

::: 정리 12
법 $n$에 원시근이 존재하는 것은 $n=1,2,4,p^k,2p^k$ ($p$는 홀수 소수, $k\ge 1$)인 것과 동치이다.
:::

::: 증명
충분성은 위에서 보였다. $n$이 이 꼴이 아니라고 하고 원시근이 없음을 보인다. 두 경우로 나눈다.

$n=2^k$ ($k\ge 3$)인 경우. 홀수 $a$에 대하여 $a^{2^{k-2}}\equiv 1 \pmod{2^k}$임을 $k$에 대한 귀납법으로 보인다. $k=3$이면 $a=2m+1$일 때 $a^2=4m(m+1)+1\equiv 1 \pmod 8$이다. $a^{2^{k-2}}=1+2^km$이라 하면 $a^{2^{k-1}}=1+2^{k+1}m+2^{2k}m^2\equiv 1 \pmod{2^{k+1}}$이다. 따라서 모든 reduced residue class의 위수가 $2^{k-2}<\varphi(2^k)=2^{k-1}$ 이하이다.

그 밖의 경우. $n$이 $2$의 거듭제곱이 아니고 $n\ne 1,2,4,p^k,2p^k$이면 $n=ab$ ($\gcd(a,b)=1$, $a,b>2$)로 쓸 수 있다. 실제로 $n$이 서로 다른 홀수 소수를 둘 이상 가지면 $a$를 한 소수의 거듭제곱 부분으로, 홀수 소수 $p$를 하나만 가지면 $n=2^ep^k$에서 $e\ge 2$이므로 $a=2^e$, $b=p^k$로 잡는다. $a>2$이면 $\varphi(a)$는 짝수이다. [§산술적 함수와 뫼비우스 반전, ⁋따름정리 14](/ko/math/number_theory/arithmetic_functions#cor14)에 의하여 $\varphi(a)=\prod p^{e-1}(p-1)$이므로 $a$가 홀수 소수 $p$로 나누어지면 인수 $p-1$이 짝수이고, 그렇지 않으면 $a=2^e$, $e\ge 2$이므로 인수 $2^{e-1}$이 짝수이기 때문이다. $b$에 대해서도 같다. $\gcd(x,n)=1$인 $x$에 대하여 $L=\lcm(\varphi(a),\varphi(b))$로 두면 [§페르마 소정리와 오일러 정리, ⁋정리 3](/ko/math/number_theory/euler_theorem#thm3)에 의하여 $x^L\equiv 1 \pmod a$와 $\pmod b$가 모두 성립하므로 $x^L\equiv 1 \pmod n$이다. $\varphi(a)$와 $\varphi(b)$는 둘 다 짝수이므로 $L\le\varphi(a)\varphi(b)/2=\varphi(n)/2<\varphi(n)$이다($\varphi(a)\varphi(b)=\varphi(n)$은 [§페르마 소정리와 오일러 정리, ⁋명제 5](/ko/math/number_theory/euler_theorem#prop5)에 의한다). 따라서 $\ord_n(x)\le L<\varphi(n)$이고 원시근이 없다.
:::

::: 예시 13 (원시근이 없는 법 8과 15)
법 $8$의 reduced residue class $1,3,5,7$은 모두 제곱하면 $1$이 된다. $\varphi(8)=4$인데 위수가 $4$인 원소가 없으므로 원시근이 없다. reduced residue class들의 multiplicative group은 위수가 $1$ 또는 $2$인 원소 네 개로 이루어지고, 한 원소의 거듭제곱으로 생성되지 않는다. 법 $15$에서는 $\varphi(15)=8$이고 $\gcd(x,15)=1$이면 $x^2\equiv 1 \pmod 3$, $x^4\equiv 1 \pmod 5$이므로 $x^4\equiv 1 \pmod{15}$이다. 위수가 $8$인 원소가 없다. 두 경우 모두 $x^2\equiv 1$의 해가 $4$개여서, [정리 6](#thm6)의 증명이 의존한 [정리 5](#thm5)의 부등식이 합성수 법에서 성립하지 않는 것과 맞물린다.
:::

## 지표

법 $n$에 원시근 $g$가 있다고 하자. [명제 8](#prop8)에 의하여 $\gcd(a,n)=1$인 모든 $a$는 $a\equiv g^\ell$인 정수 $\ell$을 가진다. [명제 2](#prop2)에 의하여 $g^\ell\equiv g^{\ell'}$인 것은 $\ell\equiv\ell' \pmod{\varphi(n)}$인 것과 동치이므로 $\ell$은 법 $\varphi(n)$에 대하여 유일하게 정해진다.

::: 정의 14
법 $n$의 원시근 $g$와 $\gcd(a,n)=1$인 $a$에 대하여 $a\equiv g^\ell \pmod n$을 만족하는 $\ell \pmod{\varphi(n)}$을 $g$에 대한 $a$의 *지표<sub>index</sub>* 또는 이산로그라 하고 $\ind_g a$로 적는다.
:::

지표는 $g$의 선택에 의존한다. 정의에서 곧바로 $g^{\ind_g a+\ind_g b}\equiv ab\equiv g^{\ind_g(ab)}$이므로 법 $\varphi(n)$에 대하여

$$\ind_g(ab)\equiv \ind_g a+\ind_g b,\qquad \ind_g(a^k)\equiv k\ind_g a$$

이다. 곱셈과 거듭제곱이 덧셈과 곱셈으로 바뀌므로, 소수 법의 거듭제곱 합동식은 일차 합동식으로 환원된다.

::: 명제 15
$p$가 소수이고 $g$가 법 $p$의 원시근이며 $p\nmid a$, $k\ge 1$이라 하자. $x^k\equiv a \pmod p$가 해를 가지는 것은 $\gcd(k,p-1)\mid\ind_g a$인 것과 동치이고, 이때 해는 법 $p$에서 정확히 $\gcd(k,p-1)$개이다.
:::

::: 증명
$p\nmid x$인 $x$만 해가 될 수 있고, $x\equiv g^t$로 쓰면 $t$는 법 $p-1$에서 $x$와 일대일로 대응한다. $x^k\equiv g^{kt}$이므로 $x^k\equiv a$인 것은 $kt\equiv \ind_g a \pmod{p-1}$인 것과 동치이다. 일차 합동식 $kt\equiv c \pmod{p-1}$은 $\gcd(k,p-1)\mid c$일 때에만 해가 있고, 그때 법 $p-1$에서 정확히 $\gcd(k,p-1)$개의 해를 가진다([§합동식과 중국인의 나머지 정리, ⁋정리 5](/ko/math/number_theory/chinese_remainder_theorem#thm5)).
:::

::: 예시 16 (법 13의 지표표와 거듭제곱 합동식)
원시근 $2$에 대하여 $2^1,\ldots,2^{12}$를 법 $13$으로 계산하면 $2,4,8,3,6,12,11,9,5,10,7,1$이므로 지표표는 다음과 같다.

$$\begin{aligned}
&\ind_2 1=12\equiv 0,\ \ind_2 2=1,\ \ind_2 3=4,\ \ind_2 4=2,\ \ind_2 5=9,\ \ind_2 6=5,\\
&\ind_2 7=11,\ \ind_2 8=3,\ \ind_2 9=8,\ \ind_2 10=10,\ \ind_2 11=7,\ \ind_2 12=6
\end{aligned}$$

$x^4\equiv 3 \pmod{13}$에서는 $\gcd(4,12)=4$이고 $\ind_2 3=4$로 $4\mid 4$이므로 해가 $4$개이다. $4t\equiv 4 \pmod{12}$는 $t\equiv 1 \pmod 3$과 같으므로 $t=1,4,7,10$이고 $x\equiv 2,3,11,10$이다. $11\equiv -2$, $10\equiv -3$이므로 $x^4$이 $2^4=16\equiv 3$, $3^4=81\equiv 3$과 같음이 확인된다. $x^4\equiv 5$에서는 $\ind_2 5=9$이고 $4\nmid 9$이므로 해가 없다. 실제로 법 $13$의 네제곱은 $1,3,9$뿐이다. $x^5\equiv 8$에서는 $\gcd(5,12)=1$이므로 해가 하나이다. $5t\equiv 3 \pmod{12}$에서 $5\cdot 5\equiv 1$이므로 $t\equiv 15\equiv 3$이고 $x\equiv 2^3=8$이다. $8^2\equiv 12$, $8^4\equiv 144\equiv 1$이므로 $8^5\equiv 8$이 맞다.

곱셈도 지표로 계산된다. $7\cdot 9$에서 $\ind_2 7+\ind_2 9=11+8=19\equiv 7 \pmod{12}$이고 $2^7\equiv 11$이다. 직접 계산하면 $63=4\cdot 13+11$이다.
:::

---

**참고문헌**

**[OL]** 오정환·이준복, *기초 정수론*, 경문사, 2012.
