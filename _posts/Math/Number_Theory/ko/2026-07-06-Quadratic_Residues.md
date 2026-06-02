---
title: "이차 잉여"
description: "법 p에서 제곱수가 되는 이차 잉여를 정의하고, 정확히 절반이 이차 잉여임을 보인다. 르장드르 기호를 도입하고, a^((p-1)/2)로 이차 잉여 여부를 판정하는 오일러 판정법을 증명한다."
excerpt: "이차 잉여와 비잉여, 르장드르 기호, 오일러 판정법"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/quadratic_residues
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Quadratic_Residues.png
    overlay_filter: 0.5

date: 2026-07-06
last_modified_at: 2026-07-06

weight: 12

published: false
---

선형 합동식 $$ax \equiv b$$는 [§일차 합동식](/ko/math/number_theory/linear_congruences)에서 완전히 풀렸다. 다음 단계는 이차 합동식 $$x^2 \equiv a \pmod p$$이다. 이 식이 해를 갖는가 — 즉 $$a$$가 법 $$p$$에서 제곱수인가 — 라는 물음이 정수론에서 가장 아름다운 이론 중 하나로 이어진다.

## 이차 잉여

이 글에서 $$p$$는 항상 홀수 소수로 둔다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\gcd(a, p) = 1$$일 때, $$x^2 \equiv a \pmod p$$가 해를 가지면 $$a$$를 법 $$p$$의 *이차 잉여<sub>quadratic residue</sub>*, 해를 갖지 않으면 *이차 비잉여<sub>quadratic non-residue</sub>*라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 법 $$p$$의 기약잉여계 $$1, 2, \ldots, p-1$$ 중 정확히 절반인 $$\dfrac{p-1}{2}$$개가 이차 잉여이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

제곱 사상 $$x \mapsto x^2$$를 기약잉여계 위에서 본다. $$x^2 \equiv y^2 \pmod p$$인 것은 $$p \mid (x-y)(x+y)$$, 즉 $$y \equiv \pm x \pmod p$$인 것과 동치이다 (유클리드 보조정리 [§소수와 산술의 기본정리, ⁋보조정리 2](/ko/math/number_theory/primes#lem2)). $$p$$가 홀수이므로 $$x \not\equiv -x$$이고, 따라서 제곱 사상은 정확히 두 원소 $$\pm x$$를 같은 값으로 보낸다. 그러므로 서로 다른 제곱값, 곧 이차 잉여는 $$(p-1)/2$$개이다.

</details>

## 르장드르 기호와 오일러 판정법

이차 잉여 여부를 부호로 부호화하면 곱셈적 구조가 드러난다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 홀수 소수 $$p$$와 정수 $$a$$에 대하여 *르장드르 기호<sub>Legendre symbol</sub>*를

$$\left(\frac{a}{p}\right) = \begin{cases} \;\;\,1, & a\text{가 법 }p\text{의 이차 잉여},\\ -1, & a\text{가 법 }p\text{의 이차 비잉여},\\ \;\;\,0, & p \mid a \end{cases}$$

로 정의한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (오일러 판정법)**</ins> 홀수 소수 $$p$$와 $$p \nmid a$$에 대하여

$$\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod p$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

페르마 소정리 ([§페르마 소정리, ⁋정리 1](/ko/math/number_theory/fermat_little_theorem#thm1))로 $$a^{p-1} \equiv 1$$이므로 $$\bigl(a^{(p-1)/2} - 1\bigr)\bigl(a^{(p-1)/2} + 1\bigr) \equiv 0 \pmod p$$이고, 따라서 $$a^{(p-1)/2} \equiv \pm 1 \pmod p$$이다.

$$a$$가 이차 잉여이면 $$a \equiv x^2$$인 $$x$$가 있어 $$a^{(p-1)/2} \equiv x^{p-1} \equiv 1$$이다. 거꾸로 $$g$$를 법 $$p$$의 원시근 ([§원시근, ⁋정리 4](/ko/math/number_theory/primitive_roots#thm4))이라 하고 $$a \equiv g^j$$로 쓰면, $$a$$가 이차 잉여인 것은 $$j$$가 짝수인 것과 동치이다. 한편 $$a^{(p-1)/2} \equiv g^{j(p-1)/2} \equiv 1$$인 것은 $$\operatorname{ord}_p(g) = p-1$$이 $$j(p-1)/2$$를 나누는 것, 곧 $$j$$가 짝수인 것과 동치이다. 따라서 $$a^{(p-1)/2} \equiv 1$$인 것과 $$a$$가 이차 잉여인 것이 일치하고, 비잉여이면 $$a^{(p-1)/2} \equiv -1$$이다.

</details>

오일러 판정법은 거듭제곱의 합동을 계산하여 이차 잉여 여부를 판정하게 해 줄 뿐 아니라, 르장드르 기호가 곱셈적임을 즉시 준다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> $$\left(\dfrac{ab}{p}\right) = \left(\dfrac{a}{p}\right)\left(\dfrac{b}{p}\right)$$이고, 특히 $$\left(\dfrac{-1}{p}\right) = (-1)^{(p-1)/2}$$이다. 즉 $$-1$$은 $$p \equiv 1 \pmod 4$$일 때만 이차 잉여이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

오일러 판정법으로 $$\left(\dfrac{ab}{p}\right) \equiv (ab)^{(p-1)/2} = a^{(p-1)/2}b^{(p-1)/2} \equiv \left(\dfrac{a}{p}\right)\left(\dfrac{b}{p}\right) \pmod p$$이고, 양변이 $$\pm 1$$이며 $$p > 2$$이므로 합동은 등호가 된다. $$a = -1$$로 두면 $$\left(\dfrac{-1}{p}\right) \equiv (-1)^{(p-1)/2}$$를 얻는다.

</details>

곱셈성에 의해 르장드르 기호의 계산은 소수와 $$-1$$에서의 값으로 환원된다. 남은 핵심은 두 홀수 소수 $$p, q$$에 대해 $$\left(\frac{q}{p}\right)$$와 $$\left(\frac{p}{q}\right)$$가 어떻게 연관되는가인데, 이 놀라운 대칭이 다음 글 [§이차 상호법칙](/ko/math/number_theory/quadratic_reciprocity)의 주제이다.
