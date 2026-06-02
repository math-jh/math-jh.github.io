---
title: "합동식"
description: "법 n에 대한 합동을 정의하고 그것이 동치관계이며 사칙연산과 호환됨을 보인다. 잉여류와 ℤ/nℤ를 도입하고, Bézout 항등식으로부터 소거법칙과 곱셈 역원의 존재 조건을 끌어낸다."
excerpt: "합동, 합동의 연산, 잉여류, 소거법칙과 곱셈 역원"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/congruences
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Congruences.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 5

published: false
---

정수론의 많은 문제는 "어떤 수로 나눈 나머지"만이 중요하다. 가우스는 이 관점을 *합동*이라는 산뜻한 언어로 정식화하여, 나머지에 관한 추론을 마치 등식처럼 다룰 수 있게 했다. 이 글에서는 합동의 정의와 연산, 그리고 [§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)에서 얻은 도구로 합동식에서의 소거와 역원을 다룬다.

## 합동

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 양의 정수 $$n$$과 정수 $$a, b$$에 대하여, $$n \mid (a - b)$$일 때 *$$a$$와 $$b$$가 법 $$n$$에 대해 합동<sub>congruent modulo $n$</sub>*이라 하고

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

## 잉여류와 ℤ/nℤ

명제 2에 의해 합동은 정수를 동치류로 나눈다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 정수 $$a$$의 법 $$n$$에 대한 *잉여류<sub>residue class</sub>*는 $$a$$와 합동인 모든 정수의 집합 $$[a] = \{a + kn \mid k \in \mathbb{Z}\}$$이다. 서로 다른 잉여류는 정확히 $$[0], [1], \ldots, [n-1]$$의 $$n$$개이며, 이들의 집합을 $$\mathbb{Z}/n\mathbb{Z}$$로 적는다.

</div>

명제 3은 잉여류 위에 $$[a] + [b] = [a + b]$$, $$[a][b] = [ab]$$로 덧셈과 곱셈이 잘 정의됨을 뜻한다. 즉 $$\mathbb{Z}/n\mathbb{Z}$$는 $$n$$개의 원소를 갖는 환을 이룬다.

## 소거와 곱셈 역원

등식과 달리 합동에서는 같은 수로 나누는 소거가 항상 되지는 않는다. 예컨대 $$2\cdot 3 \equiv 2 \cdot 0 \pmod 6$$이지만 $$3 \not\equiv 0 \pmod 6$$이다. 소거가 언제 허용되는지는 Bézout 항등식이 결정한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (소거법칙)**</ins> $$\gcd(c, n) = 1$$이면, $$ca \equiv cb \pmod n$$에서 $$a \equiv b \pmod n$$을 소거할 수 있다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$ca \equiv cb$$이면 $$n \mid c(a - b)$$이다. $$\gcd(c, n) = 1$$이므로 Bézout 항등식 ([§유클리드 호제법과 Bézout 항등식, ⁋정리 3](/ko/math/number_theory/euclidean_algorithm#thm3))으로 $$cx + ny = 1$$인 정수 $$x, y$$가 있다. 양변에 $$a - b$$를 곱하면 $$cx(a-b) + ny(a-b) = a - b$$인데, $$n \mid c(a-b)$$이므로 좌변의 두 항이 모두 $$n$$의 배수이고 따라서 $$n \mid (a - b)$$, 즉 $$a \equiv b \pmod n$$이다.

</details>

소거가 가능하다는 것은 곱셈에 대한 역원이 존재한다는 것과 같은 이야기이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$a$$가 법 $$n$$에 대해 곱셈 역원을 가진다 — 즉 $$ax \equiv 1 \pmod n$$인 $$x$$가 존재한다 — 는 것은 $$\gcd(a, n) = 1$$인 것과 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gcd(a, n) = 1$$이면 Bézout 항등식으로 $$ax + ny = 1$$인 $$x, y$$가 있고, 이는 $$ax \equiv 1 \pmod n$$을 뜻한다. 거꾸로 $$ax \equiv 1 \pmod n$$이면 $$ax - 1 = ny$$인 정수 $$y$$가 있어 $$ax - ny = 1$$이고, $$a$$와 $$n$$의 임의의 공약수는 $$1$$을 나누므로 ([§유클리드 호제법과 Bézout 항등식, ⁋따름정리 4](/ko/math/number_theory/euclidean_algorithm#cor4)) $$\gcd(a, n) = 1$$이다.

</details>

따라서 $$\mathbb{Z}/n\mathbb{Z}$$에서 곱셈 역원을 갖는 원소는 정확히 $$n$$과 서로소인 잉여류들이다. $$n = p$$가 소수이면 $$1, \ldots, p-1$$이 모두 $$p$$와 서로소이므로 $$0$$이 아닌 모든 원소가 역원을 가지며, 이때 $$\mathbb{Z}/p\mathbb{Z}$$는 체를 이룬다.

곱셈 역원의 존재는 다음 글 [§일차 합동식](/ko/math/number_theory/linear_congruences)에서 $$ax \equiv b \pmod n$$의 해를 구하는 열쇠가 되고, 서로소가 아닌 여러 법을 동시에 다루는 [§중국인의 나머지 정리](/ko/math/number_theory/chinese_remainder_theorem)로 이어진다. 또한 $$n$$과 서로소인 잉여류들이 이루는 곱셈 구조는 [§페르마 소정리](/ko/math/number_theory/fermat_little_theorem)와 [§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)의 무대가 된다.
