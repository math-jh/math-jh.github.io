---
title: "나눗셈과 최대공약수"
description: "정수론의 출발점인 나누어떨어짐 관계와 나눗셈 정리를 정리하고, 최대공약수의 정의와 기본 성질을 다룬다. 이후 유클리드 호제법과 산술의 기본정리로 이어지는 토대를 마련한다."
excerpt: "나누어떨어짐, 나눗셈 정리, 최대공약수의 정의와 성질"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/divisibility
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Divisibility.png
    overlay_filter: 0.5

date: 2026-06-06
last_modified_at: 2026-06-06

weight: 1

published: false
---

정수론은 정수 $$\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$$의 산술적 성질을 연구하는 분야이다. 그 모든 이야기는 가장 기본적인 관계 — 한 정수가 다른 정수를 나누어떨어지게 하는가 — 에서 시작한다.

## 나누어떨어짐

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 정수 $$a, b$$에 대하여, 어떤 정수 $$c$$가 존재하여 $$b = ac$$가 성립할 때 *$$a$$가 $$b$$를 나눈다<sub>$a$ divides $b$</sub>*고 하고, $$a \mid b$$로 적는다. 이때 $$a$$를 $$b$$의 *약수<sub>divisor</sub>*, $$b$$를 $$a$$의 *배수<sub>multiple</sub>*라 부른다. $$a$$가 $$b$$를 나누지 않을 때는 $$a \nmid b$$로 적는다.

</div>

정의에서 곧바로 따르는 기본 성질들을 모아 둔다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 정수 $$a, b, c$$에 대하여 다음이 성립한다.

1. $$a \mid a$$이고, $$1 \mid a$$이며, $$a \mid 0$$이다.
2. $$a \mid b$$이고 $$b \mid c$$이면 $$a \mid c$$이다 (추이성).
3. $$a \mid b$$이고 $$a \mid c$$이면, 임의의 정수 $$x, y$$에 대하여 $$a \mid (bx + cy)$$이다.
4. $$a \mid b$$이고 $$b \neq 0$$이면 $$\lvert a\rvert \leq \lvert b\rvert$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

1은 $$a = a\cdot 1$$, $$a = 1\cdot a$$, $$0 = a\cdot 0$$에서 따른다. 2는 $$b = ad$$, $$c = be$$이면 $$c = a(de)$$이므로 성립한다. 3은 $$b = ad$$, $$c = ae$$이면 $$bx + cy = a(dx + ey)$$이므로 성립한다. 4는 $$b = ac$$에서 $$b \neq 0$$이므로 $$c \neq 0$$, 즉 $$\lvert c\rvert \geq 1$$이고 따라서 $$\lvert b\rvert = \lvert a\rvert\,\lvert c\rvert \geq \lvert a\rvert$$이다.

</details>

성질 3은 정수론 전체에서 가장 자주 쓰이는 도구로, "$$a$$로 나누어떨어지는 수들의 정수계수 선형결합도 $$a$$로 나누어떨어진다"는 것이다.

## 나눗셈 정리

정수는 일반적으로 서로 나누어떨어지지 않지만, 나누고 *나머지*를 남기는 것은 언제나 가능하다. 이것이 정수론의 핵심 알고리즘적 사실이다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (나눗셈 정리)**</ins> 임의의 정수 $$a$$와 양의 정수 $$b$$에 대하여, 다음을 만족하는 정수 $$q, r$$가 유일하게 존재한다.

$$a = bq + r, \qquad 0 \leq r < b$$

여기서 $$q$$를 *몫<sub>quotient</sub>*, $$r$$를 *나머지<sub>remainder</sub>*라 부른다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

존재성: 집합 $$S = \{a - bk \mid k \in \mathbb{Z},\; a - bk \geq 0\}$$을 생각하자. $$k$$를 충분히 작은 (음수) 정수로 잡으면 $$a - bk \geq 0$$이므로 $$S$$는 공집합이 아닌 음이 아닌 정수의 집합이고, 정렬성에 의해 최솟값 $$r = a - bq$$를 갖는다 ([\[집합론\] §정렬집합의 성질들](/ko/math/set_theory/well_ordering)). $$r \geq 0$$이다. 만약 $$r \geq b$$라면 $$r - b = a - b(q+1) \geq 0$$이 $$S$$의 원소이면서 $$r$$보다 작아 최소성에 모순이다. 따라서 $$0 \leq r < b$$이다.

유일성: $$a = bq + r = bq' + r'$$ ($$0 \leq r, r' < b$$) 이면 $$b(q - q') = r' - r$$이고 $$\lvert r' - r\rvert < b$$이다. 따라서 $$b \mid (r'-r)$$이면서 $$\lvert r'-r\rvert < b$$이므로 명제 2.4에 의해 $$r' - r = 0$$, 즉 $$r = r'$$이고 $$q = q'$$이다.

</details>

나머지 $$r$$가 $$0$$인 것은 정확히 $$b \mid a$$인 경우이다. 나눗셈 정리는 다음 글 [§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)에서 최대공약수를 계산하는 알고리즘의 엔진이 된다.

## 최대공약수

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 둘 다 $$0$$은 아닌 정수 $$a, b$$에 대하여, $$a$$와 $$b$$를 모두 나누는 양의 정수 중 가장 큰 것을 $$a, b$$의 *최대공약수<sub>greatest common divisor</sub>*라 하고 $$\gcd(a,b)$$로 적는다. $$\gcd(a,b) = 1$$일 때 $$a$$와 $$b$$는 *서로소<sub>coprime</sub>*라 한다.

</div>

공약수 $$d$$는 명제 2.4에 의해 $$\lvert d\rvert \leq \max(\lvert a\rvert, \lvert b\rvert)$$로 유계이고 $$1$$은 항상 공약수이므로, 최대공약수는 항상 잘 정의된다. 최대공약수의 가장 중요한 성질은 그것이 단순히 "가장 큰 공약수"일 뿐 아니라, 모든 공약수가 그것을 나눈다는 점이다 — 이 사실과 다음의 선형결합 표현(Bézout 항등식)은 유클리드 호제법을 통해 다음 글에서 증명한다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$\gcd(12, 18)$$을 구해 보자. $$12$$의 양의 약수는 $$1, 2, 3, 4, 6, 12$$이고 $$18$$의 양의 약수는 $$1, 2, 3, 6, 9, 18$$이므로, 공약수는 $$1, 2, 3, 6$$이고 그중 가장 큰 것은 $$6$$이다. 따라서 $$\gcd(12,18) = 6$$이다. 한편 $$\gcd(8, 15) = 1$$이므로 $$8$$과 $$15$$는 서로소이다.

</div>

약수를 일일이 나열하는 이 방법은 수가 커지면 비효율적이다. 다음 글에서 나눗셈 정리를 반복 적용하여 최대공약수를 빠르게 계산하는 유클리드 호제법을 다루고, 그로부터 $$\gcd(a,b)$$를 $$ax + by$$ 꼴로 표현하는 Bézout 항등식을 얻는다. 이 표현은 이후 [§소수와 산술의 기본정리](/ko/math/number_theory/primes)와 [§합동식](/ko/math/number_theory/congruences) 전반에서 결정적 역할을 한다.
