---
title: "페르마 소정리"
description: "소수를 법으로 할 때 a^(p-1) ≡ 1이 성립한다는 페르마 소정리를, 0이 아닌 잉여류의 곱집합이 a 배로 보존됨을 이용하여 증명한다. 페르마 판정법과 카마이클 수 등 소수 판정에의 응용을 개관한다."
excerpt: "페르마 소정리, 잉여류의 재배열 증명, 소수 판정"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/fermat_little_theorem
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Fermat_Little_Theorem.png
    overlay_filter: 0.5

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

$$a \cdot 2a \cdots (p-1)a \equiv 1 \cdot 2 \cdots (p-1) \pmod p,$$

즉 $$a^{p-1}(p-1)! \equiv (p-1)! \pmod p$$이다. $$(p-1)!$$은 $$p$$와 서로소이므로 소거하면 $$a^{p-1} \equiv 1 \pmod p$$를 얻는다.

</details>

양변에 $$a$$를 곱하면 서로소 조건 없이 성립하는 형태를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> $$p$$가 소수이면 모든 정수 $$a$$에 대해 $$a^{p} \equiv a \pmod p$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p \nmid a$$이면 정리 1의 양변에 $$a$$를 곱하면 된다. $$p \mid a$$이면 양변이 모두 $$0$$과 합동이므로 자명하게 성립한다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$2^{100}$$을 $$13$$으로 나눈 나머지를 구하자. $$13$$이 소수이고 $$13 \nmid 2$$이므로 페르마 소정리로 $$2^{12} \equiv 1 \pmod{13}$$이다. $$100 = 12\cdot 8 + 4$$이므로 $$2^{100} = (2^{12})^8\cdot 2^4 \equiv 2^4 = 16 \equiv 3 \pmod{13}$$이다.

</div>

## 소수 판정에의 응용

따름정리 2의 대우는 소수성을 부정하는 데 쓰인다: 어떤 $$a$$에 대해 $$a^n \not\equiv a \pmod n$$이면 $$n$$은 합성수이다. 이 *페르마 판정법*은 큰 수의 합성수성을 거듭제곱의 합동 계산만으로 빠르게 검출한다.

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 페르마 판정법의 역은 성립하지 않는다. 합성수이면서도 $$\gcd(a, n) = 1$$인 모든 $$a$$에 대해 $$a^{n-1} \equiv 1 \pmod n$$을 만족하는 수가 존재하며, 이를 *카마이클 수<sub>Carmichael number</sub>*라 한다. 가장 작은 예는 $$561 = 3\cdot 11\cdot 17$$이다. 따라서 페르마 판정법은 합성수를 놓칠 수 있고, 실용적 소수 판정에는 이를 정교화한 밀러–라빈 판정 등이 쓰인다.

</div>

페르마 소정리는 법이 소수일 때의 정리이다. 이를 임의의 법 $$n$$으로 일반화하면, 지수 $$p - 1$$의 자리에 $$n$$과 서로소인 잉여류의 개수 $$\varphi(n)$$이 들어가는 오일러 정리가 된다. 이것이 다음 글 [§오일러 정리와 phi 함수](/ko/math/number_theory/euler_theorem)의 주제이며, $$\mathbb{Z}/p\mathbb{Z}$$의 곱셈군이 순환군임을 밝히는 [§원시근](/ko/math/number_theory/primitive_roots)으로 이어진다.
