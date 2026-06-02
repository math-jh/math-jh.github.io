---
title: "이차 상호법칙"
description: "가우스 보조정리를 증명하여 2가 언제 이차 잉여인지를 결정하고, 두 홀수 소수의 르장드르 기호를 맞바꾸는 이차 상호법칙을 격자점 계산으로 증명한다. 이를 이용해 르장드르 기호를 효율적으로 계산한다."
excerpt: "가우스 보조정리, 제2보충법칙, 이차 상호법칙"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/quadratic_reciprocity
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Quadratic_Reciprocity.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 13

published: false
---

[§이차 잉여](/ko/math/number_theory/quadratic_residues)에서 르장드르 기호가 곱셈적임을 보았고, 그 계산이 소수와 $$-1$$에서의 값으로 환원됨을 알았다. $$-1$$의 경우는 이미 해결했으니, 남은 것은 두 홀수 소수의 르장드르 기호 사이의 관계 — 가우스가 "황금 정리"라 부른 이차 상호법칙 — 이다.

이 관계가 왜 놀라운지를 먼저 짚어 두자. 르장드르 기호 $$\left(\frac{q}{p}\right)$$는 "$$q$$가 법 $$p$$의 이차 잉여인가"라는, $$p$$를 법으로 한 산술에 관한 물음이다. 반대로 $$\left(\frac{p}{q}\right)$$는 법 $$q$$의 산술에 관한 물음으로, 표면적으로는 전혀 다른 세계의 정보이다. 이차 상호법칙은 이 두 물음의 답이 $$p, q$$를 $$4$$로 나눈 나머지라는 사소한 정보만으로 서로 결정됨을 말한다. 즉 한쪽의 어려운 계산을 다른 쪽의 같은 종류 계산으로 뒤집을 수 있고, 분모를 줄여 가며 유클리드 호제법처럼 답에 도달할 수 있다. 가우스 스스로 평생에 걸쳐 여덟 가지가 넘는 증명을 남긴 것도 이 대칭의 깊이를 반영한다.

## 가우스 보조정리

상호법칙의 증명과 $$2$$의 처리에 공통으로 쓰이는 도구는 르장드르 기호를 격자점 세기로 번역하는 가우스 보조정리이다. 핵심 발상은 오일러 판정법이 $$\left(\frac{a}{p}\right)$$를 거듭제곱 $$a^{(p-1)/2}$$로 환원해 주었으니, 이 거듭제곱을 $$a, 2a, \ldots, \frac{p-1}{2}a$$의 곱으로 풀어쓴 뒤 그 나머지들의 부호를 추적하는 것이다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1 (가우스 보조정리)**</ins> 홀수 소수 $$p$$와 $$p \nmid a$$에 대하여, $$a, 2a, \ldots, \dfrac{p-1}{2}a$$를 법 $$p$$로 환원한 최소 양의 나머지 중 $$\dfrac{p}{2}$$보다 큰 것의 개수를 $$\mu$$라 하면

$$\left(\frac{a}{p}\right) = (-1)^{\mu}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 $$ja$$ ($$1 \leq j \leq \tfrac{p-1}{2}$$) 의 최소 양의 나머지를 $$r_j$$라 하자. $$r_j > p/2$$인 것들은 $$p - r_j < p/2$$로 바꾸어 두면, 얻어진 수들

$$\{\, r_j : r_j < p/2 \,\} \cup \{\, p - r_j : r_j > p/2 \,\}$$

이 정확히 $$1, 2, \ldots, \tfrac{p-1}{2}$$의 재배열임을 보일 수 있다. 실제로 이들은 모두 $$1$$과 $$\tfrac{p-1}{2}$$ 사이에 있고 그 개수가 $$\tfrac{p-1}{2}$$로 같으므로, 서로 다름만 보이면 된다. 만약 두 수가 같다면 $$r_i = r_j$$ 또는 $$r_i = p - r_j$$인데, 앞의 경우는 $$ia \equiv ja \pmod p$$에서 $$i = j$$를 주고, 뒤의 경우는 $$ia \equiv -ja \pmod p$$에서 $$(i+j)a \equiv 0$$, 곧 $$p \mid i + j$$를 주지만 $$2 \leq i + j \leq p-1$$이라 불가능하다. 따라서 재배열이다. 이제 양변을 모두 곱하면

$$\begin{aligned}
\left(\tfrac{p-1}{2}\right)!
&= \prod_{r_j < p/2} r_j \cdot \prod_{r_j > p/2} (p - r_j) \\
&\equiv \prod_{r_j < p/2} r_j \cdot \prod_{r_j > p/2} (-r_j) \pmod p \\
&\equiv (-1)^{\mu} \prod_{j=1}^{(p-1)/2} r_j
\equiv (-1)^{\mu} \prod_{j=1}^{(p-1)/2} (ja) \\
&\equiv (-1)^{\mu}\, a^{(p-1)/2} \left(\tfrac{p-1}{2}\right)! \pmod p
\end{aligned}$$

이다. 부호 $$(-1)^\mu$$는 $$r_j > p/2$$인 $$\mu$$개의 항에서 $$p - r_j$$를 $$-r_j$$로 바꾼 데서 나온다. 양변에서 $$\left(\tfrac{p-1}{2}\right)!$$은 $$p$$와 서로소이므로 소거할 수 있고, 남은 합동식에 오일러 판정법 ([§이차 잉여, ⁋정리 4](/ko/math/number_theory/quadratic_residues#thm4))을 쓰면

$$\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \equiv (-1)^\mu \pmod p$$

을 얻는다. 양변이 $$\pm 1$$이고 $$p$$가 홀수 소수라 $$1 \not\equiv -1$$이므로 합동은 등호가 되어 결론이 따른다.

</details>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (제2보충법칙)**</ins> 홀수 소수 $$p$$에 대하여 $$\left(\dfrac{2}{p}\right) = (-1)^{(p^2-1)/8}$$이다. 즉 $$2$$는 $$p \equiv \pm 1 \pmod 8$$일 때 이차 잉여, $$p \equiv \pm 3 \pmod 8$$일 때 비잉여이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

가우스 보조정리를 $$a = 2$$에 적용한다. 우리가 곱하는 수는 $$2, 4, \ldots, p-1$$이고, 이 가운데 $$p/2$$를 넘는 것은 모두 변환되어 $$\mu$$에 기여한다. $$2j \leq p/2$$, 곧 $$j \leq p/4$$인 $$j$$의 개수는 $$\lfloor p/4 \rfloor$$이므로

$$\mu = \frac{p-1}{2} - \left\lfloor \frac{p}{4} \right\rfloor$$

이다. 이제 $$p$$를 $$8$$로 나눈 나머지에 따라 $$\mu$$를 직접 계산한다. $$p = 8k + r$$로 쓰면

$$\begin{aligned}
r = 1:\quad &\mu = (4k) - (2k) = 2k, &&\text{짝수}, \\
r = 3:\quad &\mu = (4k+1) - (2k) = 2k+1, &&\text{홀수}, \\
r = 5:\quad &\mu = (4k+2) - (2k+1) = 2k+1, &&\text{홀수}, \\
r = 7:\quad &\mu = (4k+3) - (2k+1) = 2k+2, &&\text{짝수}
\end{aligned}$$

이 되어, $$p \equiv \pm 1 \pmod 8$$이면 $$\mu$$가 짝수, $$p \equiv \pm 3 \pmod 8$$이면 홀수이다. 한편 $$(-1)^{(p^2-1)/8}$$도 같은 분류를 따르므로 ($$p^2 - 1 = (p-1)(p+1)$$이 $$8$$의 배수임은 항상 성립하고, 그 몫의 홀짝이 위 네 경우와 일치한다), $$(-1)^\mu = (-1)^{(p^2-1)/8}$$이 확인된다.

</details>

## 이차 상호법칙

이제 두 홀수 소수의 르장드르 기호를 맞바꾸는 황금 정리를 격자점 계산으로 증명한다. 핵심은 가우스 보조정리의 부호 $$\mu$$를 직접 세는 대신, 나머지 $$r_j$$가 $$p/2$$를 넘는지를 몫 $$\lfloor jq/p \rfloor$$의 홀짝으로 바꾸어 표현하고, 그 합을 좌표평면의 직사각형 안 격자점 수로 해석하는 데 있다. 그러면 $$p$$와 $$q$$의 역할을 맞바꾼 두 합이 대각선을 사이에 두고 직사각형을 정확히 양분하게 되어, 둘의 합이 직사각형 전체의 격자점 수가 된다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (이차 상호법칙)**</ins> 서로 다른 두 홀수 소수 $$p, q$$에 대하여

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$$

이다. 즉 $$p$$와 $$q$$ 중 적어도 하나가 $$4$$로 나누어 $$1$$이 남으면 $$\left(\frac{p}{q}\right) = \left(\frac{q}{p}\right)$$이고, 둘 다 $$3$$이 남으면 부호가 반대이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 가우스 보조정리의 부호를 몫의 합으로 바꾼다. $$1 \leq j \leq \tfrac{p-1}{2}$$에 대해 $$jq = p\lfloor jq/p\rfloor + r_j$$ ($$0 < r_j < p$$) 로 나눗셈을 하면, 이 식들을 모두 더해

$$q\sum_{j=1}^{(p-1)/2} j = p\sum_{j=1}^{(p-1)/2}\left\lfloor \frac{jq}{p}\right\rfloor + \sum_{j=1}^{(p-1)/2} r_j$$

를 얻는다. 가우스 보조정리의 증명에서 보았듯 $$r_j > p/2$$인 $$\mu$$개를 $$p - r_j$$로 바꾼 수들이 $$1, \ldots, \tfrac{p-1}{2}$$의 재배열이므로

$$\sum_{r_j < p/2} r_j + \sum_{r_j > p/2} (p - r_j) = \sum_{j=1}^{(p-1)/2} j$$

이고, 따라서 $$\sum_j r_j = \sum_j j - \mu p + 2\sum_{r_j > p/2} r_j$$이다. 위 두 식을 빼고 $$\bmod\ 2$$로 환원하면, $$q$$가 홀수이고 $$p$$가 홀수임을 써서

$$\sum_{j=1}^{(p-1)/2}\left\lfloor \frac{jq}{p}\right\rfloor \equiv \mu \pmod 2$$

이 따른다. 그러므로 $$S = \sum_{j=1}^{(p-1)/2}\lfloor jq/p\rfloor$$로 두면 가우스 보조정리는

$$\left(\frac{q}{p}\right) = (-1)^{\mu} = (-1)^{S}$$

가 된다.

이제 $$S$$를 격자점 수로 읽는다. $$\lfloor jq/p\rfloor$$는 $$x = j$$에서 직선 $$py = qx$$ 아래에 있는 양의 정수 $$y$$의 개수와 같으므로, $$S$$는 직사각형 $$0 < x < p/2$$, $$0 < y < q/2$$ 안의 격자점 가운데 직선 $$py = qx$$의 *아래쪽*($$py < qx$$)에 있는 것의 개수이다. 같은 논법을 $$p, q$$를 맞바꾸어 적용하면

$$\left(\frac{p}{q}\right) = (-1)^{T}, \qquad T = \sum_{i=1}^{(q-1)/2}\left\lfloor \frac{ip}{q}\right\rfloor$$

이고 $$T$$는 같은 직사각형에서 직선의 *위쪽*($$py > qx$$)에 있는 격자점 수이다. 직선 $$py = qx$$ 위에 격자점이 있으려면 $$p \mid x$$여야 하는데 $$0 < x < p/2$$에는 그런 $$x$$가 없으므로, 직선 위에는 격자점이 없다. 따라서 직사각형 안의 모든 격자점은 위·아래 중 한쪽에 속하고

$$S + T = \left(\frac{p-1}{2}\right)\left(\frac{q-1}{2}\right)$$

이다. 양변을 $$-1$$의 지수로 올리면

$$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{S+T} = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$$

를 얻는다.

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\left(\dfrac{30}{53}\right)$$을 구하자. $$53$$은 소수이고 $$30 = 2\cdot 3\cdot 5$$이므로 곱셈성으로 $$\left(\frac{30}{53}\right) = \left(\frac{2}{53}\right)\left(\frac{3}{53}\right)\left(\frac{5}{53}\right)$$이다. $$53 \equiv 5 \pmod 8$$이므로 $$\left(\frac{2}{53}\right) = -1$$이다. 상호법칙으로 $$53 \equiv 1 \pmod 4$$이니 $$\left(\frac{3}{53}\right) = \left(\frac{53}{3}\right) = \left(\frac{2}{3}\right) = -1$$, $$\left(\frac{5}{53}\right) = \left(\frac{53}{5}\right) = \left(\frac{3}{5}\right) = -1$$이다. 따라서 $$\left(\frac{30}{53}\right) = (-1)(-1)(-1) = -1$$로, $$30$$은 법 $$53$$의 비잉여이다.

</div>

## 르장드르 기호의 계산

이차 상호법칙은 르장드르 기호의 계산을 유클리드 호제법처럼 분모와 분자를 번갈아 줄여 가는 효율적 절차로 바꾼다. 분자를 분모보다 작은 양수로 환원하고($$\bmod p$$), 소인수분해로 $$2$$와 홀수 소수의 기호로 쪼갠 뒤, 상호법칙으로 각 홀수 소수 기호의 분자·분모를 맞바꾸어 분모를 줄인다. 이 세 단계를 반복하면 분모가 단조 감소하여 유한 번에 끝난다. 다음 예시들에서 이 절차를 직접 따라가 본다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 ($$3$$의 잉여성)**</ins> $$3$$이 법 $$p$$의 이차 잉여인 소수 $$p > 3$$를 분류하자. 상호법칙에서 $$\frac{3-1}{2} = 1$$이므로

$$\left(\frac{3}{p}\right) = (-1)^{\frac{p-1}{2}\cdot 1}\left(\frac{p}{3}\right) = (-1)^{(p-1)/2}\left(\frac{p}{3}\right)$$

이다. $$\left(\frac{p}{3}\right)$$은 $$p \bmod 3$$에만 의존하여 $$p \equiv 1$$이면 $$+1$$, $$p \equiv 2$$이면 $$-1$$이다. 또 $$(-1)^{(p-1)/2}$$은 $$p \equiv 1 \pmod 4$$이면 $$+1$$, $$p \equiv 3 \pmod 4$$이면 $$-1$$이다. 중국인의 나머지 정리로 두 조건을 합치면

$$\left(\frac{3}{p}\right) = +1 \iff p \equiv \pm 1 \pmod{12}$$

임이 따른다. 예컨대 $$p = 11 \equiv -1$$이면 $$3$$은 잉여이고 ($$5^2 = 25 \equiv 3$$), $$p = 7 \equiv 7$$이면 비잉여이다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (큰 분자의 환원)**</ins> $$\left(\dfrac{105}{317}\right)$$을 구하자. $$317$$은 소수이고 $$105 = 3\cdot 5\cdot 7$$이므로

$$\left(\frac{105}{317}\right) = \left(\frac{3}{317}\right)\left(\frac{5}{317}\right)\left(\frac{7}{317}\right)$$

이다. $$317 \equiv 1 \pmod 4$$이므로 세 기호 모두 부호 변화 없이 뒤집힌다:

$$\begin{aligned}
\left(\frac{3}{317}\right) &= \left(\frac{317}{3}\right) = \left(\frac{2}{3}\right) = -1, \\
\left(\frac{5}{317}\right) &= \left(\frac{317}{5}\right) = \left(\frac{2}{5}\right) = -1, \\
\left(\frac{7}{317}\right) &= \left(\frac{317}{7}\right) = \left(\frac{2}{7}\right) = +1
\end{aligned}$$

이다 (마지막에서 $$7 \equiv -1 \pmod 8$$이라 $$\left(\frac{2}{7}\right) = +1$$). 따라서 $$\left(\frac{105}{317}\right) = (-1)(-1)(+1) = +1$$로, $$105$$는 법 $$317$$의 이차 잉여이다.

</div>

소인수분해를 거치지 않고 곧장 호제법처럼 진행할 수도 있다. 이를 위해서는 르장드르 기호를 합성수 분모로 확장한 *야코비 기호<sub>Jacobi symbol</sub>*가 편리하다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 홀수인 양의 정수 $$n = p_1 p_2 \cdots p_k$$ (소수의 곱, 중복 허용) 와 $$\gcd(a, n) = 1$$인 정수 $$a$$에 대하여 *야코비 기호<sub>Jacobi symbol</sub>*를

$$\left(\frac{a}{n}\right) = \prod_{i=1}^{k}\left(\frac{a}{p_i}\right)$$

로 정의한다. 각 인수는 르장드르 기호이다.

</div>

야코비 기호는 르장드르 기호의 곱셈성을 분모로도 확장한 것으로, $$\left(\frac{a}{n}\right) = +1$$이라고 해서 $$a$$가 법 $$n$$의 이차 잉여라는 보장은 없음에 주의한다. 가령 $$\left(\frac{2}{15}\right) = \left(\frac{2}{3}\right)\left(\frac{2}{5}\right) = (-1)(-1) = +1$$이지만 $$2$$는 법 $$15$$의 이차 잉여가 아니다. 그러나 야코비 기호는 상호법칙과 두 보충법칙을 그대로 만족한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (야코비 기호의 상호법칙)**</ins> 서로소인 두 홀수 양의 정수 $$m, n$$에 대하여

$$\left(\frac{m}{n}\right)\left(\frac{n}{m}\right) = (-1)^{\frac{m-1}{2}\cdot\frac{n-1}{2}}$$

이고, 또 $$\left(\dfrac{-1}{n}\right) = (-1)^{(n-1)/2}$$, $$\left(\dfrac{2}{n}\right) = (-1)^{(n^2-1)/8}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$m = \prod p_i$$, $$n = \prod q_j$$로 소인수분해하면, 정의와 르장드르 기호의 상호법칙(정리 3)으로

$$\left(\frac{m}{n}\right)\left(\frac{n}{m}\right) = \prod_{i,j}\left(\frac{p_i}{q_j}\right)\left(\frac{q_j}{p_i}\right) = \prod_{i,j}(-1)^{\frac{p_i-1}{2}\cdot\frac{q_j-1}{2}} = (-1)^{\sum_{i,j}\frac{p_i-1}{2}\frac{q_j-1}{2}}$$

이다. 지수의 합은 $$\bigl(\sum_i \frac{p_i-1}{2}\bigr)\bigl(\sum_j \frac{q_j-1}{2}\bigr)$$로 분리되므로, 두 홀수 $$a, b$$의 곱에 대해 $$\frac{ab-1}{2} \equiv \frac{a-1}{2} + \frac{b-1}{2} \pmod 2$$임을 반복 적용하면

$$\sum_i \frac{p_i-1}{2} \equiv \frac{m-1}{2}, \qquad \sum_j \frac{q_j-1}{2} \equiv \frac{n-1}{2} \pmod 2$$

이 되어 지수가 $$\frac{m-1}{2}\cdot\frac{n-1}{2}$$와 같은 홀짝을 가진다. 두 보충법칙도 같은 방식으로, $$\frac{a^2b^2-1}{8} \equiv \frac{a^2-1}{8} + \frac{b^2-1}{8} \pmod 2$$를 써서 인수별 르장드르 보충법칙의 곱으로부터 얻는다.

</details>

야코비 기호 덕분에 분모가 소수인지 일일이 확인하지 않고도 르장드르 기호를 계산할 수 있다. 다음 예시가 이 호제법형 절차를 보여 준다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (호제법형 계산)**</ins> $$\left(\dfrac{1009}{2307}\right)$$을 구하자. $$2307 = 3\cdot 769$$로 홀수이고 $$1009$$가 소수임을 안다면 르장드르 기호이지만, 야코비 기호로 보면 소인수분해 없이도 진행된다:

$$\begin{aligned}
\left(\frac{1009}{2307}\right)
&= (-1)^{\frac{1008}{2}\cdot\frac{2306}{2}}\left(\frac{2307}{1009}\right) = \left(\frac{2307}{1009}\right) \\
&= \left(\frac{289}{1009}\right) = \left(\frac{17^2}{1009}\right) = +1
\end{aligned}$$

이다. 첫 줄에서 $$\frac{1008}{2} = 504$$가 짝수라 부호가 $$+1$$이고 $$2307 \equiv 289 \pmod{1009}$$이며, 마지막에서 $$289 = 17^2$$이 완전제곱이라 기호가 $$+1$$이다. 따라서 $$\left(\frac{1009}{2307}\right) = +1$$이다.

</div>

이렇게 분자를 항상 분모로 환원하고 완전제곱 인수를 떼어 내면, 도중에 분모의 소인수분해를 시도할 필요가 전혀 없다. 이것이 야코비 기호가 르장드르 기호 계산에 주는 실질적 이점이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 ($$x^2 \equiv 7 \pmod{11}$$의 가해성)**</ins> 합동식 $$x^2 \equiv 7 \pmod{11}$$이 풀리는지 판정하자. $$11 \equiv 3 \pmod 4$$이고 $$7 \equiv 3 \pmod 4$$이므로 두 소수 모두 $$4$$로 나눠 $$3$$이 남아 상호법칙의 부호가 음이다:

$$\left(\frac{7}{11}\right) = -\left(\frac{11}{7}\right) = -\left(\frac{4}{7}\right) = -\left(\frac{2^2}{7}\right) = -1$$

이다. 따라서 $$7$$은 법 $$11$$의 비잉여이고 합동식은 해를 갖지 않는다. 실제로 $$1^2, \ldots, 5^2$$을 법 $$11$$로 환원한 잉여 $$\{1, 4, 9, 5, 3\}$$에 $$7$$이 없음으로 확인된다.

</div>

## 응용

이차 상호법칙의 가장 직접적인 응용은 특정 소수의 잉여류를 분류해, 어떤 디오판토스 방정식이 해를 가질 수 없음을 보이는 것이다. 예를 들어 $$x^2 + 1 \equiv 0 \pmod p$$가 풀리려면 $$-1$$이 잉여여야 하므로 $$p \equiv 1 \pmod 4$$가 필요하고, 이는 $$4k+3$$ 꼴 소수가 두 제곱수의 합이 될 수 없다는 사실로 이어진다. 같은 방식으로 $$x^2 - 2$$, $$x^2 + 2$$, $$x^2 - 3$$ 등의 가해 소수를 보충법칙과 상호법칙으로 분류할 수 있다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (제수의 잉여류)**</ins> $$n^2 + 1$$의 홀수 소인수는 모두 $$4k+1$$ 꼴임을 보이자. $$p \mid n^2 + 1$$이면 $$n^2 \equiv -1 \pmod p$$이므로 $$-1$$이 법 $$p$$의 이차 잉여이고, 제1보충법칙

$$\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2}$$

에서 $$(-1)^{(p-1)/2} = +1$$, 곧 $$\frac{p-1}{2}$$가 짝수여야 하므로 $$p \equiv 1 \pmod 4$$이다. 같은 논법으로 $$n^2 + 2$$의 홀수 소인수는 $$\left(\frac{-2}{p}\right) = +1$$, 즉 $$p \equiv 1, 3 \pmod 8$$을 만족함을 얻는다. 이는 특정 꼴의 소수가 무한히 많다는 디리클레형 결과의 초보적 사례를 제공한다.

</div>

제곱수의 산술은 정수의 범위를 넘어서면 더 풍부해지는데, 다음 글 [§가우스 정수와 두 제곱수의 합](/ko/math/number_theory/gaussian_integers)에서 $$\sqrt{-1}$$을 더한 정수환을 다루며 어떤 소수가 두 제곱수의 합인지를 판정한다. 위 예시 11에서 본 $$p \equiv 1 \pmod 4$$라는 필요조건이 사실은 충분조건이기도 함을, 그 글에서 가우스 정수의 소인수분해로 증명한다.
