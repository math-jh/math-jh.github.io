---
title: "합동식"
description: "법 n에 대한 합동을 정의하고 그것이 동치관계이며 사칙연산과 호환됨을 보인다. 잉여류와 ℤ/nℤ를 도입하고, Bézout 항등식으로부터 소거법칙과 곱셈 역원의 존재 조건을 끌어낸다."
excerpt: "합동, 합동의 연산, 잉여류, 소거법칙과 곱셈 역원"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/congruences
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 5

published: false
---

정수론의 많은 문제는 "어떤 수로 나눈 나머지"만이 중요하다. 가우스는 이 관점을 *합동*이라는 산뜻한 언어로 정식화하여, 나머지에 관한 추론을 마치 등식처럼 다룰 수 있게 했다. 이 글에서는 합동의 정의와 연산, 그리고 [§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)에서 얻은 도구로 합동식에서의 소거와 역원을 다룬다.

## 합동

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 양의 정수 $$n$$과 정수 $$a, b$$에 대하여, $$n \mid (a - b)$$일 때 *$$a$$와 $$b$$가 법 $$n$$에 대해 합동<sub>congruent modulo n</sub>*이라 하고

$$a \equiv b \pmod{n}$$

으로 적는다. $$n$$을 *법<sub>modulus</sub>*이라 한다.

</div>

나눗셈 정리 ([§나눗셈과 최대공약수, ⁋정리 3](/ko/math/number_theory/divisibility#thm3))에 의해 $$a \equiv b \pmod n$$인 것은 $$a$$와 $$b$$를 $$n$$으로 나눈 나머지가 같은 것과 동치이다. 즉 합동은 "나머지가 같음"을 그대로 옮긴 것이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 법 $$n$$에 대한 합동은 정수 위의 동치관계이다. 즉 반사적($$a \equiv a$$), 대칭적($$a\equiv b \Rightarrow b \equiv a$$), 추이적($$a \equiv b,\ b\equiv c \Rightarrow a \equiv c$$)이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$n \mid 0 = a - a$$이므로 반사적이다. $$n \mid (a-b)$$이면 $$n \mid (b - a)$$이므로 대칭적이다. $$n \mid (a-b)$$이고 $$n \mid (b-c)$$이면 선형결합 성질 ([§나눗셈과 최대공약수, ⁋명제 2](/ko/math/number_theory/divisibility#prop2))에 의해 $$n \mid (a - c)$$이므로 추이적이다.

</details>

## 합동의 연산

합동이 등식처럼 유용한 까닭은 사칙연산과 잘 어울리기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$a \equiv b \pmod n$$이고 $$c \equiv d \pmod n$$이면

$$a + c \equiv b + d, \qquad a - c \equiv b - d, \qquad ac \equiv bd \pmod n$$

이다. 특히 임의의 자연수 $$k$$에 대해 $$a^k \equiv b^k \pmod n$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$n \mid (a - b)$$이고 $$n \mid (c - d)$$이다. 덧셈은 $$(a + c) - (b + d) = (a - b) + (c - d)$$가 선형결합 성질로 $$n$$의 배수임에서 따른다. 곱셈은 $$ac - bd = a(c - d) + d(a - b)$$가 역시 $$n$$의 배수임에서 따른다. 거듭제곱은 $$ac \equiv bd$$를 반복 적용하면 된다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$7^{100}$$을 $$5$$로 나눈 나머지를 구하자. $$7 \equiv 2 \pmod 5$$이므로 $$7^{100} \equiv 2^{100} \pmod 5$$이다. 한편 $$2^4 = 16 \equiv 1 \pmod 5$$이므로 $$2^{100} = (2^4)^{25} \equiv 1^{25} = 1 \pmod 5$$이다. 따라서 나머지는 $$1$$이다.

</div>

예시 4의 요령은 합동의 거듭제곱 성질이 가진 위력을 잘 보여 준다. $$7^{100}$$을 직접 계산하는 것은 $$84$$자리가 넘는 수를 다루는 일이지만, 법 $$5$$에서는 밑을 작은 대표원 $$2$$로 바꾸고 지수의 *주기*를 찾는 것으로 환원된다. 곧 거듭제곱의 수열 $$2^1, 2^2, 2^3, \ldots$$이 법 $$5$$에서 어느 시점부터 같은 값을 반복하는지를 보면 충분하다. 실제로

$$2^1 \equiv 2,\quad 2^2 \equiv 4,\quad 2^3 \equiv 3,\quad 2^4 \equiv 1 \pmod 5$$

이어서 길이 $$4$$의 주기로 순환하므로, 지수를 $$4$$로 나눈 나머지만이 결과를 결정한다. $$100 = 4\cdot 25$$이므로 $$2^{100} \equiv (2^4)^{25} \equiv 1 \pmod 5$$가 되는 것이다. 이러한 주기의 존재는 우연이 아니다.

같은 방식으로 다항식 값의 합동도 한꺼번에 다룰 수 있다. 명제 3은 정수계수 다항식 $$P$$에 대해 $$a \equiv b \pmod n$$이면 $$P(a) \equiv P(b) \pmod n$$임을 함의하는데, 이는 덧셈·곱셈·거듭제곱이 모두 합동을 보존하기 때문이다. 이 관찰은 자릿수에 관한 여러 검산법을 한꺼번에 설명해 준다. $$10 \equiv 1 \pmod 9$$로부터 임의의 자연수가 그 자리 숫자의 합과 법 $$9$$에서 합동임이 곧바로 따라 나온다.

## 잉여류와 ℤ/nℤ

명제 2에 의해 합동은 정수를 동치류로 나눈다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 정수 $$a$$의 법 $$n$$에 대한 *잉여류<sub>residue class</sub>*는 $$a$$와 합동인 모든 정수의 집합 $$[a] = \{a + kn \mid k \in \mathbb{Z}\}$$이다. 서로 다른 잉여류는 정확히 $$[0], [1], \ldots, [n-1]$$의 $$n$$개이며, 이들의 집합을 $$\mathbb{Z}/n\mathbb{Z}$$로 적는다.

</div>

잉여류는 정수 전체를 $$n$$개의 줄로 나눈 것으로 볼 수 있다. 정수 $$a$$를 $$n$$으로 나눈 나머지를 $$r$$이라 하면 $$a \equiv r \pmod n$$이므로 $$[a] = [r]$$이고, $$0 \le r \le n-1$$인 $$r$$이 유일하게 결정되므로 $$[0], [1], \ldots, [n-1]$$은 서로 다르고 모든 잉여류를 빠짐없이 준다. 한 잉여류에서 아무 정수나 골라 그 류를 대표시킬 수 있는데, 이렇게 고른 수를 그 잉여류의 *대표원<sub>representative</sub>*이라 한다. 예컨대 법 $$5$$에서 $$[2] = [7] = [-3] = [12]$$이며, 이 중 어느 것을 써도 같은 류를 가리킨다.

명제 3은 잉여류 위에 $$[a] + [b] = [a + b]$$, $$[a][b] = [ab]$$로 덧셈과 곱셈이 잘 정의됨을 뜻한다. 여기서 "잘 정의됨"이란 결과가 대표원의 선택에 의존하지 않음을 말한다. 만약 $$[a] = [a']$$이고 $$[b] = [b']$$이면 $$a \equiv a'$$, $$b \equiv b' \pmod n$$이고, 명제 3에 의해

$$a + b \equiv a' + b', \qquad ab \equiv a'b' \pmod n$$

이므로 $$[a+b] = [a'+b']$$, $$[ab] = [a'b']$$가 되어 어느 대표원을 골라 계산해도 같은 잉여류를 얻는다. 이 호환성이 없었다면 잉여류 위의 연산을 정의할 수 없었을 것이다. 결국 $$\mathbb{Z}/n\mathbb{Z}$$는 $$n$$개의 원소를 갖는 *환<sub>ring</sub>*을 이룬다.

가장 작은 경우인 $$n = 2$$에서는 $$\mathbb{Z}/2\mathbb{Z} = \{[0], [1]\}$$이 짝수와 홀수의 산술을 그대로 옮긴 것으로, $$[1] + [1] = [0]$$은 "홀수 더하기 홀수는 짝수"라는 사실에 다름 아니다. $$n = 12$$의 경우 $$\mathbb{Z}/12\mathbb{Z}$$는 시계의 시각이 이루는 산술과 같아, $$9$$시의 $$5$$시간 뒤가 $$2$$시인 것은 $$9 + 5 = 14 \equiv 2 \pmod{12}$$로 표현된다.

## 소거와 곱셈 역원

등식과 달리 합동에서는 같은 수로 나누는 소거가 항상 되지는 않는다. 예컨대 $$2\cdot 3 \equiv 2 \cdot 0 \pmod 6$$이지만 $$3 \not\equiv 0 \pmod 6$$이다. 소거가 언제 허용되는지는 Bézout 항등식이 결정한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (소거법칙)**</ins> $$\gcd(c, n) = 1$$이면, $$ca \equiv cb \pmod n$$에서 $$a \equiv b \pmod n$$을 소거할 수 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$ca \equiv cb$$이면 정의에 의해 $$n \mid c(a - b)$$이다. $$\gcd(c, n) = 1$$이므로 Bézout 항등식 ([§유클리드 호제법과 Bézout 항등식, ⁋정리 3](/ko/math/number_theory/euclidean_algorithm#thm3))으로 $$cx + ny = 1$$인 정수 $$x, y$$가 존재한다. 이 등식의 양변에 $$a - b$$를 곱하면

$$\begin{aligned}
a - b &= (cx + ny)(a - b) \\
&= x \cdot c(a - b) + ny(a - b)
\end{aligned}$$

이다. 우변의 첫 항은 $$n \mid c(a-b)$$이므로 $$n$$의 배수이고, 둘째 항은 인수 $$n$$을 가지므로 $$n$$의 배수이다. 따라서 두 항의 합인 $$a - b$$도 $$n$$의 배수이고, 곧 $$n \mid (a - b)$$, 즉 $$a \equiv b \pmod n$$이다.

</details>

소거가 가능하다는 것은 곱셈에 대한 역원이 존재한다는 것과 같은 이야기이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$a$$가 법 $$n$$에 대해 곱셈 역원을 가진다 — 즉 $$ax \equiv 1 \pmod n$$인 $$x$$가 존재한다 — 는 것은 $$\gcd(a, n) = 1$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gcd(a, n) = 1$$이면 Bézout 항등식으로 $$ax + ny = 1$$인 정수 $$x, y$$가 존재한다. 이 등식의 양변을 법 $$n$$으로 읽으면 $$ny \equiv 0 \pmod n$$이므로

$$ax = 1 - ny \equiv 1 \pmod n$$

이 되어 $$x$$가 $$a$$의 곱셈 역원이다. 거꾸로 $$ax \equiv 1 \pmod n$$인 $$x$$가 존재하면 어떤 정수 $$y$$에 대해 $$ax - 1 = ny$$, 곧 $$ax - ny = 1$$이다. $$d = \gcd(a, n)$$이라 하면 $$d \mid a$$이고 $$d \mid n$$이므로 좌변을 나누어 $$d \mid 1$$이고 ([§나눗셈과 최대공약수, ⁋명제 2](/ko/math/number_theory/divisibility#prop2)), 따라서 $$d = 1$$, 즉 $$\gcd(a, n) = 1$$이다.

</details>

따라서 $$\mathbb{Z}/n\mathbb{Z}$$에서 곱셈 역원을 갖는 원소는 정확히 $$n$$과 서로소인 잉여류들이다. $$n = p$$가 소수이면 $$1, \ldots, p-1$$이 모두 $$p$$와 서로소이므로 $$0$$이 아닌 모든 원소가 역원을 가지며, 이때 $$\mathbb{Z}/p\mathbb{Z}$$는 체를 이룬다. 역원이 존재할 때 그것은 법 $$n$$에 대해 유일하다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (역원의 유일성)**</ins> $$\gcd(a, n) = 1$$이면 $$ax \equiv 1 \pmod n$$을 만족하는 잉여류 $$[x]$$는 유일하다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$ax \equiv 1$$이고 $$ax' \equiv 1 \pmod n$$이라 하자. 그러면

$$ax \equiv ax' \pmod n$$

이고, $$\gcd(a, n) = 1$$이므로 소거법칙 ([명제 6](#prop6))으로 $$a$$를 소거하여 $$x \equiv x' \pmod n$$, 곧 $$[x] = [x']$$을 얻는다.

</details>

이 유일한 잉여류를 $$a$$의 *법 $$n$$에서의 역원*이라 하고 $$a^{-1} \pmod n$$으로 적는다. 역원을 실제로 구하는 일은 Bézout 계수 $$x$$를 찾는 일, 곧 확장 유클리드 호제법을 돌리는 일과 같다.

## 예시와 계산

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (역원의 계산)**</ins> $$17$$의 법 $$23$$에서의 역원을 구하자. $$\gcd(17, 23) = 1$$이므로 역원이 존재한다. 확장 유클리드 호제법으로 $$23$$과 $$17$$에 대한 Bézout 계수를 찾는다:

$$\begin{aligned}
23 &= 1\cdot 17 + 6, \\
17 &= 2\cdot 6 + 5, \\
6 &= 1\cdot 5 + 1.
\end{aligned}$$

거꾸로 거슬러 올라가면

$$\begin{aligned}
1 &= 6 - 1\cdot 5 \\
&= 6 - (17 - 2\cdot 6) = 3\cdot 6 - 17 \\
&= 3\cdot(23 - 17) - 17 = 3\cdot 23 - 4\cdot 17
\end{aligned}$$

이므로 $$-4\cdot 17 \equiv 1 \pmod{23}$$이고, $$-4 \equiv 19 \pmod{23}$$이다. 따라서 $$17^{-1} \equiv 19 \pmod{23}$$이다. 검산하면 $$17\cdot 19 = 323 = 14\cdot 23 + 1 \equiv 1 \pmod{23}$$이다.

</div>

역원을 손에 넣으면 일차 합동식을 등식처럼 풀 수 있다. $$ax \equiv b \pmod n$$의 양변에 $$a^{-1}$$을 곱하면 $$x \equiv a^{-1}b \pmod n$$이 되기 때문이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (일차 합동식의 풀이)**</ins> $$17x \equiv 5 \pmod{23}$$을 풀자. 예시 9에서 $$17^{-1} \equiv 19 \pmod{23}$$이었으므로 양변에 $$19$$를 곱하면

$$x \equiv 19\cdot 5 = 95 = 4\cdot 23 + 3 \equiv 3 \pmod{23}$$

이다. 따라서 해는 $$x \equiv 3 \pmod{23}$$, 곧 $$\ldots, -20, 3, 26, 49, \ldots$$이다. 실제로 $$17\cdot 3 = 51 = 2\cdot 23 + 5 \equiv 5 \pmod{23}$$로 확인된다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (큰 거듭제곱의 끝자리)**</ins> $$3^{1000}$$의 마지막 두 자리, 곧 $$3^{1000} \bmod 100$$을 구하자. 거듭제곱의 주기를 찾는다:

$$\begin{aligned}
3^1 &\equiv 3, & 3^2 &\equiv 9, & 3^3 &\equiv 27, & 3^4 &\equiv 81 \pmod{100}, \\
3^5 &\equiv 43, & 3^{10} &\equiv 43^2 = 1849 \equiv 49, & 3^{20} &\equiv 49^2 = 2401 \equiv 1 \pmod{100}.
\end{aligned}$$

따라서 $$3^{20} \equiv 1 \pmod{100}$$이고, $$1000 = 20\cdot 50$$이므로

$$3^{1000} = (3^{20})^{50} \equiv 1^{50} = 1 \pmod{100}$$

이다. 곧 $$3^{1000}$$의 마지막 두 자리는 $$01$$이다.

</div>

마지막으로, 합동은 어떤 방정식이 정수해를 가지지 *않음*을 보이는 데에도 자주 쓰인다. 적당한 법으로 양변을 옮겨 합동이 성립할 수 없음을 보이면 충분하기 때문이다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (해의 부재)**</ins> 방정식 $$x^2 + y^2 = 4z + 3$$이 정수해를 갖지 않음을 보이자. 정수 $$x$$에 대해 $$x \equiv 0, 1, 2, 3 \pmod 4$$를 각각 제곱하면 $$x^2 \equiv 0, 1, 0, 1 \pmod 4$$이므로, 제곱수는 법 $$4$$에서 항상 $$0$$ 또는 $$1$$이다. 따라서

$$x^2 + y^2 \equiv 0,\ 1,\ \text{또는}\ 2 \pmod 4$$

뿐이며 결코 $$3$$이 될 수 없다. 그런데 우변은 $$4z + 3 \equiv 3 \pmod 4$$이므로 양변의 합동이 모순이고, 따라서 정수해가 존재하지 않는다.

</div>

## 응용

자릿수에 관한 검산법은 합동의 가장 친숙한 응용이다. 앞에서 예고한 대로, $$10 \equiv 1 \pmod 9$$이 모든 자리 거듭제곱을 $$1$$로 만든다는 사실이 그 핵심이다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (구거법과 11 판정법)**</ins> 자연수 $$N$$을 십진법으로 $$N = \sum_k d_k 10^k$$로 적자. $$10 \equiv 1 \pmod 9$$이므로 임의의 $$k$$에 대해 $$10^k \equiv 1 \pmod 9$$이고, 명제 3에 의해

$$N = \sum_k d_k 10^k \equiv \sum_k d_k \pmod 9$$

이다. 곧 $$N$$은 그 자리 숫자의 합과 법 $$9$$에서 합동이다. 가령 $$N = 8643$$이면 $$8+6+4+3 = 21 \equiv 3 \pmod 9$$이므로 $$N \equiv 3 \pmod 9$$이다. 한편 $$10 \equiv -1 \pmod{11}$$이므로 $$10^k \equiv (-1)^k \pmod{11}$$이고,

$$N \equiv \sum_k (-1)^k d_k = d_0 - d_1 + d_2 - \cdots \pmod{11}$$

이 되어, 자리 숫자의 교대합으로 법 $$11$$의 나머지를 안다. $$8643$$이면 $$3 - 4 + 6 - 8 = -3 \equiv 8 \pmod{11}$$이다. 두 판정법 모두 명제 3의 한 따름일 뿐이다.

</div>

