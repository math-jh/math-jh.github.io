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

date: 2026-06-02
last_modified_at: 2026-06-02
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

오일러 판정법은 작은 법에서 르장드르 기호를 직접 계산하게 해 준다. 핵심은 $$a^{(p-1)/2}$$를 반복제곱으로 빠르게 줄인 뒤 $$\pm 1$$ 중 어느 쪽인지 읽는 것이다.

## 예시와 계산

먼저 명제 2가 말하는 “정확히 절반”을 구체적인 법에서 직접 확인한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (법 $$7$$과 법 $$11$$의 이차 잉여)**</ins> $$p = 7$$에서 $$1, \ldots, 6$$의 제곱을 차례로 계산하면

$$\begin{aligned}
1^2 &\equiv 1, & 2^2 &\equiv 4, & 3^2 &\equiv 2,\\
4^2 &\equiv 2, & 5^2 &\equiv 4, & 6^2 &\equiv 1 \pmod 7
\end{aligned}$$

이므로 이차 잉여는 $$\{1, 2, 4\}$$이고 비잉여는 $$\{3, 5, 6\}$$이다. 명제 2가 말하듯 각각 $$\dfrac{7-1}{2} = 3$$개이며, $$x$$와 $$-x = 7-x$$의 제곱이 같음도 표에서 그대로 드러난다. 같은 방식으로 $$p = 11$$에서는

$$1, 4, 9, 5, 3 \pmod{11}$$

이 $$1^2, \ldots, 5^2$$로 나오므로 이차 잉여는 $$\{1, 3, 4, 5, 9\}$$, 비잉여는 $$\{2, 6, 7, 8, 10\}$$이고 각각 $$5$$개이다.

</div>

다음으로 오일러 판정법 (정리 4) 을 거듭제곱 계산에 적용한다. 큰 수의 거듭제곱은 법을 줄여 가며 반복제곱하는 것이 요령이다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (오일러 판정법에 의한 판정)**</ins> $$\left(\dfrac{2}{7}\right)$$을 구하자. $$\dfrac{7-1}{2} = 3$$이므로

$$2^{3} = 8 \equiv 1 \pmod 7$$

이고, 정리 4에 의해 $$\left(\dfrac{2}{7}\right) = 1$$이다. 실제로 $$3^2 = 9 \equiv 2$$이므로 $$2$$는 법 $$7$$의 이차 잉여이다. 반면 $$\left(\dfrac{3}{7}\right)$$은

$$3^{3} = 27 \equiv 6 \equiv -1 \pmod 7$$

이므로 $$-1$$, 곧 $$3$$은 비잉여이다. 더 큰 예로 $$\left(\dfrac{6}{11}\right)$$은 $$\dfrac{11-1}{2} = 5$$제곱을 반복제곱으로 계산하여

$$\begin{aligned}
6^2 &= 36 \equiv 3, \\
6^4 &\equiv 3^2 = 9, \\
6^5 &\equiv 6^4 \cdot 6 \equiv 9 \cdot 6 = 54 \equiv 10 \equiv -1 \pmod{11}
\end{aligned}$$

이므로 $$\left(\dfrac{6}{11}\right) = -1$$이다. 이는 예시 6에서 본 비잉여 목록 $$\{2,6,7,8,10\}$$에 $$6$$이 들어 있는 것과 일치한다.

</div>

곱셈성 (따름정리 5) 은 큰 르장드르 기호를 작은 인수의 곱으로 쪼개 준다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (곱셈성을 이용한 계산)**</ins> $$\left(\dfrac{6}{11}\right)$$을 다시, 이번에는 따름정리 5로 분해해 보자. $$6 = 2 \cdot 3$$이므로

$$\left(\frac{6}{11}\right) = \left(\frac{2}{11}\right)\left(\frac{3}{11}\right)$$

이고, 예시 6의 잉여 목록 $$\{1,3,4,5,9\}$$에서 $$3$$은 잉여, $$2$$는 비잉여임을 읽으면

$$\left(\frac{2}{11}\right) = -1, \qquad \left(\frac{3}{11}\right) = +1 \;\Longrightarrow\; \left(\frac{6}{11}\right) = (-1)(+1) = -1$$

로 예시 7의 결과를 재확인한다. 또 따름정리 5의 $$\left(\dfrac{-1}{p}\right) = (-1)^{(p-1)/2}$$를 보면, $$p = 11 \equiv 3 \pmod 4$$이므로 $$\left(\dfrac{-1}{11}\right) = -1$$이어서 $$-1 \equiv 10$$이 비잉여임이 예시 6의 목록과 들어맞는다. 반면 $$p = 13 \equiv 1 \pmod 4$$에서는 $$\left(\dfrac{-1}{13}\right) = +1$$이고, 실제로 $$5^2 = 25 \equiv -1 \pmod{13}$$이 성립한다.

</div>

## 잉여의 분포

곱셈성은 이차 잉여와 비잉여가 곱셈에 대해 어떻게 결합하는지를 부호의 곱으로 요약한다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 법 $$p$$에서 두 이차 잉여의 곱은 이차 잉여이고, 두 이차 비잉여의 곱도 이차 잉여이며, 이차 잉여와 이차 비잉여의 곱은 이차 비잉여이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

따름정리 5의 곱셈성으로 $$\left(\dfrac{ab}{p}\right) = \left(\dfrac{a}{p}\right)\left(\dfrac{b}{p}\right)$$이다. 따라서

$$\begin{aligned}
(+1)(+1) &= +1, \\
(-1)(-1) &= +1, \\
(+1)(-1) &= -1
\end{aligned}$$

이라는 부호의 곱이 그대로 잉여·비잉여의 결합 규칙을 준다. 즉 잉여 전체는 곱셈에 대해 닫혀 있고 (지수의 짝수성으로도 보인다), 비잉여 둘의 곱은 짝수 지수가 되어 잉여로 돌아온다.

</details>

이 부호 규칙은 르장드르 기호가 군 준동형 $$(\mathbb{Z}/p\mathbb{Z})^\times \to \{\pm 1\}$$임을 말한다. 그 핵은 이차 잉여들로 이루어진 지수 $$2$$의 부분군이고, 이것이 명제 2의 “절반”을 군론적으로 설명한다. 같은 관점에서 잉여와 비잉여의 합을 부호로 더하면 서로 상쇄됨을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> 홀수 소수 $$p$$에 대하여 기약잉여계 위에서 르장드르 기호의 합은

$$\sum_{a=1}^{p-1} \left(\frac{a}{p}\right) = 0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 2에 의해 $$1, \ldots, p-1$$ 중 이차 잉여가 정확히 $$\dfrac{p-1}{2}$$개, 비잉여가 정확히 $$\dfrac{p-1}{2}$$개이다. 잉여에서는 르장드르 기호가 $$+1$$, 비잉여에서는 $$-1$$이므로

$$\sum_{a=1}^{p-1} \left(\frac{a}{p}\right) = \frac{p-1}{2}\cdot(+1) + \frac{p-1}{2}\cdot(-1) = 0$$

이다.

</details>

가령 $$p = 7$$이면 예시 6의 부호열은 $$+\, +\, -\, +\, -\, -$$ (각각 $$1,2,3,4,5,6$$에 대응) 이고, 그 합은 $$3 \cdot (+1) + 3 \cdot (-1) = 0$$으로 명제 10과 일치한다. 마지막으로 오일러 판정법이 어떻게 합동식의 가해성 판정으로 직결되는지를 본다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (합동식의 가해성)**</ins> $$x^2 \equiv 5 \pmod{13}$$이 해를 갖는지 판정하자. 오일러 판정법으로 $$5^{6} \pmod{13}$$을 반복제곱으로 계산하면

$$\begin{aligned}
5^2 &= 25 \equiv -1, \\
5^4 &\equiv (-1)^2 = 1, \\
5^6 &\equiv 5^4 \cdot 5^2 \equiv 1 \cdot (-1) = -1 \pmod{13}
\end{aligned}$$

이므로 $$\left(\dfrac{5}{13}\right) = -1$$이고, 따라서 $$x^2 \equiv 5 \pmod{13}$$은 해를 갖지 않는다. 반대로 $$x^2 \equiv 3 \pmod{13}$$은 $$3^6 = (3^3)^2 = 27^2 \equiv 1^2 = 1 \pmod{13}$$이므로 가해이며, 실제로 $$4^2 = 16 \equiv 3 \pmod{13}$$이 한 해이고 $$-4 \equiv 9$$가 다른 해이다. 이렇게 명제 2가 보장하는 두 해 $$\pm x$$가 함께 나타난다.

</div>

곱셈성에 의해 르장드르 기호의 계산은 소수와 $$-1$$에서의 값으로 환원된다. 남은 핵심은 두 홀수 소수 $$p, q$$에 대해 $$\left(\frac{q}{p}\right)$$와 $$\left(\frac{p}{q}\right)$$가 어떻게 연관되는가인데, 이 놀라운 대칭이 다음 글 [§이차 상호법칙](/ko/math/number_theory/quadratic_reciprocity)의 주제이다.
