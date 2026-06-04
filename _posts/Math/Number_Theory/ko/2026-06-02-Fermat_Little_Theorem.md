---
title: "페르마 소정리"
description: "소수를 법으로 할 때 a^(p-1) ≡ 1이 성립한다는 페르마 소정리를, 0이 아닌 잉여류의 곱집합이 a 배로 보존됨을 이용하여 증명한다. 페르마 판정법과 카마이클 수 등 소수 판정에의 응용을 개관한다."
excerpt: "페르마 소정리, 잉여류의 재배열 증명, 소수 판정"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/fermat_little_theorem
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 8

published: false
---

[§합동식](/ko/math/number_theory/congruences)에서 소수 $$p$$를 법으로 하면 $$0$$이 아닌 모든 잉여류가 곱셈 역원을 가져 $$\mathbb{Z}/p\mathbb{Z}$$가 체를 이룸을 보았다. 이 곱셈 구조에서 나오는 가장 기본적이고 강력한 사실이 페르마 소정리이며, 거듭제곱의 합동을 극적으로 단순화한다.

## 페르마 소정리

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (페르마 소정리)**</ins> $$p$$가 소수이고 $$p \nmid a$$이면

$$a^{p-1} \equiv 1 \pmod p$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$0$$이 아닌 잉여류들 $$1, 2, \ldots, p-1$$에 각각 $$a$$를 곱한 $$a, 2a, \ldots, (p-1)a$$를 생각한다. $$p \nmid a$$이고 $$1 \leq i \leq p-1$$이면 $$p \nmid ia$$이므로 이들은 모두 $$0$$이 아니고, $$ia \equiv ja \pmod p$$이면 소거법칙 ([§합동식, ⁋명제 6](/ko/math/number_theory/congruences#prop6))에 의해 $$i \equiv j$$이므로 서로 다르다. 따라서 $$a, 2a, \ldots, (p-1)a$$는 법 $$p$$에 대해 $$1, 2, \ldots, p-1$$을 순서만 바꾸어 놓은 것이다. 양쪽을 모두 곱하면

$$\begin{aligned}
a \cdot 2a \cdots (p-1)a &= a^{p-1}\cdot \bigl(1 \cdot 2 \cdots (p-1)\bigr) \\
&\equiv 1 \cdot 2 \cdots (p-1) \pmod p,
\end{aligned}$$

즉 $$a^{p-1}(p-1)! \equiv (p-1)! \pmod p$$이다. $$(p-1)!$$은 $$p$$와 서로소이므로 소거하면 $$a^{p-1} \equiv 1 \pmod p$$를 얻는다.

</details>

증명의 핵심은 $$a$$를 곱하는 사상 $$x \mapsto ax$$가 $$0$$이 아닌 잉여류들의 집합 $$\{1, 2, \ldots, p-1\}$$을 그 자신으로 일대일로 옮긴다는 사실이다. 즉 곱셈군 위에서 $$a$$ 배는 단순한 재배열에 불과하며, 그 재배열이 곱을 보존하기 때문에 $$a^{p-1}$$만큼의 인수가 상쇄되어 사라진다. 이 관점은 다음 글 [§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)에서 임의의 법으로 일반화되며, 본질적으로는 유한 곱셈군에서 원소의 위수가 군의 크기를 나눈다는 군론적 사실의 가장 단순한 표현이다.

양변에 $$a$$를 곱하면 서로소 조건 없이 성립하는 형태를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$p$$가 소수이면 모든 정수 $$a$$에 대해 $$a^{p} \equiv a \pmod p$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p \nmid a$$이면 정리 1의 양변에 $$a$$를 곱하면 된다. $$p \mid a$$이면 양변이 모두 $$0$$과 합동이므로 자명하게 성립한다.

</details>

따름정리 2의 형태 $$a^p \equiv a \pmod p$$는 서로소 조건을 요구하지 않으므로 모든 정수에 무차별적으로 적용할 수 있어 종종 더 편리하다. 정리 1이 곱셈군에 관한 진술이라면, 따름정리 2는 그것을 $$p \mid a$$인 경우까지 흡수해 모든 잉여류에 대해 성립하는 항등식으로 다듬은 것이다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$2^{100}$$을 $$13$$으로 나눈 나머지를 구하자. $$13$$이 소수이고 $$13 \nmid 2$$이므로 페르마 소정리로 $$2^{12} \equiv 1 \pmod{13}$$이다. $$100 = 12\cdot 8 + 4$$이므로 $$2^{100} = (2^{12})^8\cdot 2^4 \equiv 2^4 = 16 \equiv 3 \pmod{13}$$이다.

</div>

## 소수 판정에의 응용

따름정리 2의 대우는 소수성을 부정하는 데 쓰인다: 어떤 $$a$$에 대해 $$a^n \not\equiv a \pmod n$$이면 $$n$$은 합성수이다. 이 *페르마 판정법*은 큰 수의 합성수성을 거듭제곱의 합동 계산만으로 빠르게 검출한다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 페르마 판정법의 역은 성립하지 않는다. 합성수이면서도 $$\gcd(a, n) = 1$$인 모든 $$a$$에 대해 $$a^{n-1} \equiv 1 \pmod n$$을 만족하는 수가 존재하며, 이를 *카마이클 수<sub>Carmichael number</sub>*라 한다. 가장 작은 예는 $$561 = 3\cdot 11\cdot 17$$이다. 따라서 페르마 판정법은 합성수를 놓칠 수 있고, 실용적 소수 판정에는 이를 정교화한 밀러–라빈 판정 등이 쓰인다.

</div>

## 이항정리에 의한 증명

따름정리 2는 잉여류의 재배열에 의존하지 않고 이항정리와 귀납법만으로도 직접 증명할 수 있다. 이 두 번째 증명은 소수성이 어디서 결정적으로 쓰이는지를 한층 분명히 드러낸다. 핵심은 $$0 < k < p$$인 이항계수 $$\binom{p}{k}$$가 모두 $$p$$로 나누어떨어진다는 사실이다. 실제로

$$\binom{p}{k} = \frac{p!}{k!\,(p-k)!}$$

에서 분자에는 $$p$$라는 인수가 있는 반면, $$0 < k < p$$이면 분모의 $$k!$$과 $$(p-k)!$$은 모두 $$p$$보다 작은 수들의 곱이라 소수 $$p$$를 인수로 갖지 않는다. $$\binom{p}{k}$$가 정수이므로 분자의 $$p$$는 약분되지 않고 살아남아 $$p \mid \binom{p}{k}$$가 된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (이항정리에 의한 증명)**</ins> $$p$$가 소수이고 $$a, b$$가 정수이면 $$(a + b)^p \equiv a^p + b^p \pmod p$$이며, 이로부터 모든 정수 $$a$$에 대해 $$a^p \equiv a \pmod p$$가 따라 나온다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이항정리로 전개하면

$$\begin{aligned}
(a + b)^p &= \sum_{k=0}^{p} \binom{p}{k} a^k b^{p-k} \\
&= a^p + b^p + \sum_{k=1}^{p-1} \binom{p}{k} a^k b^{p-k}
\end{aligned}$$

이고, 위에서 본 대로 $$1 \leq k \leq p-1$$이면 $$p \mid \binom{p}{k}$$이므로 가운데 합은 법 $$p$$에 대해 사라진다. 따라서 $$(a+b)^p \equiv a^p + b^p \pmod p$$이다. 이제 $$a \geq 0$$에 대한 귀납법을 쓴다. $$a = 0$$이면 $$0^p = 0$$으로 자명하고, $$a^p \equiv a \pmod p$$를 가정하면

$$\begin{aligned}
(a + 1)^p &\equiv a^p + 1^p \\
&\equiv a + 1 \pmod p
\end{aligned}$$

이므로 모든 음이 아닌 정수에서 성립한다. 음의 정수에 대해서는 $$a$$를 법 $$p$$에 대해 $$0 \leq a' \leq p-1$$인 $$a'$$으로 바꾸면 음이 아닌 경우로 환원된다.

</details>

명제 5의 등식 $$(a+b)^p \equiv a^p + b^p \pmod p$$는 흔히 "신입생의 꿈<sub>freshman's dream</sub>"이라 불리며, 표수 $$p$$를 가진 체에서 $$p$$제곱 사상 $$x \mapsto x^p$$가 덧셈과 곱셈을 모두 보존하는 준동형 — *프로베니우스 자기준동형<sub>Frobenius endomorphism</sub>* — 이 되는 현상의 산술적 그림자이다.

## 예시와 계산

페르마 소정리의 직접적인 효용은 거듭제곱의 지수를 법 $$p-1$$로 줄여 큰 거듭제곱의 합동을 손으로 계산할 수 있게 해 준다는 데 있다. 예시 3에서 본 방법을 조금 더 큰 수에 적용해 보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (큰 거듭제곱의 나머지)**</ins> $$3^{1000}$$을 $$7$$로 나눈 나머지를 구하자. $$7$$이 소수이고 $$7 \nmid 3$$이므로 페르마 소정리에 의해 $$3^{6} \equiv 1 \pmod 7$$이다. 따라서 지수 $$1000$$을 $$6$$으로 나눈 나머지만 보면 된다.

$$\begin{aligned}
1000 &= 6 \cdot 166 + 4, \\
3^{1000} &= \bigl(3^{6}\bigr)^{166}\cdot 3^{4} \\
&\equiv 1^{166}\cdot 3^{4} \\
&= 81 \equiv 4 \pmod 7.
\end{aligned}$$

즉 나머지는 $$4$$이다.

</div>

지수를 줄일 때 핵심은 $$3^6 \equiv 1$$이라는 사실이며, 따라서 $$3$$의 거듭제곱은 지수에 대해 주기 $$6$$으로 순환한다. 실제 위수는 $$6$$의 약수이지만, 페르마 소정리는 그 약수를 일일이 찾지 않고도 곧바로 쓸 수 있는 지수 $$p-1$$을 보장한다는 점에서 편리하다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (지수가 더 클 때)**</ins> $$2^{2^{10}}$$을 $$11$$로 나눈 나머지를 구하자. $$11$$이 소수이므로 $$2^{10} \equiv 1 \pmod{11}$$이고, 따라서 지수 $$2^{10} = 1024$$를 $$10$$으로 나눈 나머지가 필요하다.

$$\begin{aligned}
2^{10} = 1024 &= 10 \cdot 102 + 4, \\
2^{2^{10}} = 2^{1024} &= \bigl(2^{10}\bigr)^{102}\cdot 2^{4} \\
&\equiv 1^{102}\cdot 2^{4} \\
&= 16 \equiv 5 \pmod{11}.
\end{aligned}$$

즉 나머지는 $$5$$이다. 지수가 다시 거듭제곱으로 주어질 때에는, 바깥쪽 법 $$p$$에 대해서는 지수를 법 $$p-1$$로 줄이고, 그 지수 자체를 계산할 때 또 합동을 쓰는 식으로 한 단계씩 내려가면 된다.

</div>

페르마 소정리는 곱셈 역원을 명시적으로 주는 데에도 쓰인다. $$p \nmid a$$이면 $$a \cdot a^{p-2} = a^{p-1} \equiv 1 \pmod p$$이므로, $$a$$의 법 $$p$$에 대한 역원은 곧 $$a^{p-2}$$이다. 이는 확장 유클리드 알고리즘 ([§일차 합동식, ⁋예시 4](/ko/math/number_theory/linear_congruences#ex4)) 과는 다른, 거듭제곱만으로 역원을 얻는 길을 열어 준다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (거듭제곱에 의한 역원)**</ins> $$p$$가 소수이고 $$p \nmid a$$이면, $$a$$의 법 $$p$$에 대한 곱셈 역원은 $$a^{p-2}$$이다. 즉 $$a^{-1} \equiv a^{p-2} \pmod p$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 1에 의해 $$a^{p-1} \equiv 1 \pmod p$$이므로

$$a \cdot a^{p-2} = a^{p-1} \equiv 1 \pmod p$$

이고, 따라서 $$a^{p-2}$$가 $$a$$의 곱셈 역원이다. 역원은 유일하므로 ([§합동식, ⁋명제 7](/ko/math/number_theory/congruences#prop7)) 이것이 $$a^{-1}$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (거듭제곱으로 역원 구하기)**</ins> 법 $$7$$에 대한 $$3$$의 역원을 구하자. 명제 8에 의해 $$3^{-1} \equiv 3^{7-2} = 3^{5} \pmod 7$$이다.

$$\begin{aligned}
3^2 &= 9 \equiv 2 \pmod 7, \\
3^4 &= \bigl(3^2\bigr)^2 \equiv 2^2 = 4 \pmod 7, \\
3^5 &= 3^4 \cdot 3 \equiv 4 \cdot 3 = 12 \equiv 5 \pmod 7.
\end{aligned}$$

즉 $$3^{-1} \equiv 5 \pmod 7$$이며, 실제로 $$3 \cdot 5 = 15 \equiv 1 \pmod 7$$로 맞다.

</div>

마지막으로 페르마 판정법이 합성수성을 어떻게 검출하는지 구체적인 수로 살펴본다. 따름정리 2의 대우에 따라, 어떤 밑 $$a$$에서 $$a^n \not\equiv a \pmod n$$이 단 한 번이라도 관찰되면 $$n$$은 결코 소수일 수 없다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (페르마 판정법)**</ins> $$n = 15$$가 합성수임을 밑 $$2$$로 검출하자. 만약 $$15$$가 소수라면 $$2^{15} \equiv 2 \pmod{15}$$여야 한다. 그러나

$$\begin{aligned}
2^{4} &= 16 \equiv 1 \pmod{15}, \\
2^{15} &= \bigl(2^{4}\bigr)^{3}\cdot 2^{3} \\
&\equiv 1^{3}\cdot 8 = 8 \pmod{15}
\end{aligned}$$

이고 $$8 \not\equiv 2 \pmod{15}$$이므로, 페르마 판정법에 의해 $$15$$는 합성수이다. 여기서 우리는 $$15 = 3 \cdot 5$$라는 인수분해를 전혀 사용하지 않았다 — 거듭제곱의 합동 계산만으로 합성수성이 드러난 것이다. 이것이 페르마 판정법이 인수분해보다 훨씬 빠르게 큰 수의 합성수성을 가려내는 이유이다.

</div>

페르마 소정리는 법이 소수일 때의 정리이다. 이를 임의의 법 $$n$$으로 일반화하면, 지수 $$p - 1$$의 자리에 $$n$$과 서로소인 잉여류의 개수 $$\varphi(n)$$이 들어가는 오일러 정리가 된다. 이것이 다음 글 [§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)의 주제이며, $$\mathbb{Z}/p\mathbb{Z}$$의 곱셈군이 순환군임을 밝히는 [§원시근](/ko/math/number_theory/primitive_roots)으로 이어진다.
