---
title: "나눗셈과 최대공약수"
description: "정수론의 출발점인 나누어떨어짐 관계와 나눗셈 정리를 정리하고, 최대공약수의 정의와 기본 성질을 다룬다. 이후 유클리드 호제법과 산술의 기본정리로 이어지는 토대를 마련한다."
excerpt: "나누어떨어짐, 나눗셈 정리, 최대공약수의 정의와 성질"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/divisibility
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 1

published: false
---

정수론은 정수 $$\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$$의 산술적 성질을 연구하는 분야이다. 그 모든 이야기는 가장 기본적인 관계 — 한 정수가 다른 정수를 나누어떨어지게 하는가 — 에서 시작한다.

정수는 덧셈과 곱셈에 대해 닫혀 있지만 나눗셈에 대해서는 그렇지 않다. $$6$$을 $$2$$로 나누면 정수 $$3$$이 되지만 $$7$$을 $$2$$로 나누면 정수가 아니다. 바로 이 비대칭성 — 나누어떨어지는 경우와 그렇지 않은 경우의 구별 — 이 정수의 곱셈 구조를 풍부하게 만든다. 만약 모든 나눗셈이 정수 안에서 항상 가능했다면 소수도, 최대공약수도, 합동식도 존재하지 않았을 것이다. 우리는 이 글에서 나누어떨어짐 관계를 정밀하게 정의하고, 그로부터 따르는 기본 성질, 나머지를 남기는 나눗셈, 그리고 두 정수의 공통 구조를 재는 최대공약수를 차례로 다룬다.

## 나누어떨어짐

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 정수 $$a, b$$에 대하여, 어떤 정수 $$c$$가 존재하여 $$b = ac$$가 성립할 때 *$$a$$가 $$b$$를 나눈다<sub>$$a$$ divides $$b$$</sub>*고 하고, $$a \mid b$$로 적는다. 이때 $$a$$를 $$b$$의 *약수<sub>divisor</sub>*, $$b$$를 $$a$$의 *배수<sub>multiple</sub>*라 부른다. $$a$$가 $$b$$를 나누지 않을 때는 $$a \nmid b$$로 적는다.

</div>

정의의 형태에 몇 가지 주의할 점이 있다. 첫째, $$a \mid b$$는 $$b/a$$가 정수라는 뜻이지만, 정의 자체에는 나눗셈이 등장하지 않는다 — 오직 곱셈 $$b = ac$$만으로 서술된다. 이렇게 함으로써 $$0$$이 관여하는 경계 경우도 자연스럽게 다룰 수 있다. 가령 모든 정수 $$a$$에 대해 $$a \mid 0$$인데, 이는 $$0 = a \cdot 0$$이기 때문이다. 반대로 $$0 \mid b$$는 $$b = 0 \cdot c = 0$$일 때, 즉 $$b = 0$$일 때만 성립한다. 둘째, 나누어떨어짐은 부호에 둔감하다 — $$a \mid b$$이면 $$-a \mid b$$, $$a \mid -b$$, $$-a \mid -b$$가 모두 성립한다. 그래서 약수를 따질 때는 보통 양의 약수만 헤아려도 충분하다.

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

1은 $$a = a\cdot 1$$, $$a = 1\cdot a$$, $$0 = a\cdot 0$$에서 곧바로 따른다.

2를 보이자. $$a \mid b$$이고 $$b \mid c$$이면 적당한 정수 $$d, e$$가 있어 $$b = ad$$, $$c = be$$이다. 두 식을 결합하면

$$c = be = (ad)e = a(de)$$

이고 $$de$$가 정수이므로 $$a \mid c$$이다.

3을 보이자. $$a \mid b$$이고 $$a \mid c$$이면 적당한 정수 $$d, e$$가 있어 $$b = ad$$, $$c = ae$$이다. 임의의 정수 $$x, y$$에 대하여

$$\begin{aligned}
bx + cy &= (ad)x + (ae)y \\
&= a(dx) + a(ey) \\
&= a(dx + ey)
\end{aligned}$$

이고 $$dx + ey$$가 정수이므로 $$a \mid (bx + cy)$$이다.

4를 보이자. $$a \mid b$$이고 $$b \neq 0$$이면 $$b = ac$$인 정수 $$c$$가 있는데, $$b \neq 0$$이므로 $$c \neq 0$$, 즉 $$\lvert c\rvert \geq 1$$이다. 따라서

$$\lvert b\rvert = \lvert a\rvert\,\lvert c\rvert \geq \lvert a\rvert \cdot 1 = \lvert a\rvert$$

이다.

</details>

성질 2는 나누어떨어짐이 *추이적<sub>transitive</sub>* 관계임을 말한다. 성질 3은 정수론 전체에서 가장 자주 쓰이는 도구로, "$$a$$로 나누어떨어지는 수들의 정수계수 선형결합도 $$a$$로 나누어떨어진다"는 것이다. 특히 $$x = 1$$, $$y = 1$$로 두면 $$a \mid (b + c)$$를, $$x = 1$$, $$y = -1$$로 두면 $$a \mid (b - c)$$를 얻으므로, 두 배수의 합과 차는 다시 배수이다. 성질 4는 $$0$$이 아닌 정수의 약수는 그 절댓값을 넘지 못한다는 유한성 진술로, 약수가 유한 개임을 보장하고 뒤에서 최대공약수가 잘 정의됨을 떠받친다.

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

유일성: 두 표현 $$a = bq + r = bq' + r'$$ ($$0 \leq r, r' < b$$) 이 있다고 하자. 두 식을 빼면

$$\begin{aligned}
b(q - q') &= r' - r
\end{aligned}$$

이므로 $$b \mid (r' - r)$$이다. 한편 $$0 \leq r, r' < b$$에서

$$-b < r' - r < b, \qquad \text{즉} \quad \lvert r' - r\rvert < b$$

이다. 따라서 $$b \mid (r' - r)$$이면서 $$\lvert r' - r\rvert < b$$인데, 만약 $$r' - r \neq 0$$이라면 명제 2.4에 의해 $$\lvert r' - r\rvert \geq b$$여야 하여 모순이다. 그러므로 $$r' - r = 0$$, 즉 $$r = r'$$이고, $$b(q - q') = 0$$과 $$b > 0$$에서 $$q = q'$$이다.

</details>

나머지 $$r$$가 $$0$$인 것은 정확히 $$b \mid a$$인 경우이다. $$b$$가 음수일 때도 나눗셈은 가능한데, 양의 정수 $$\lvert b\rvert$$에 정리를 적용한 뒤 몫의 부호를 조정하면 된다 — 즉 임의의 정수 $$a$$와 $$0$$이 아닌 정수 $$b$$에 대해 $$a = bq + r$$, $$0 \leq r < \lvert b\rvert$$인 $$q, r$$가 유일하게 존재한다. 나눗셈 정리는 다음 글 [§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)에서 최대공약수를 계산하는 알고리즘의 엔진이 된다.

나눗셈 정리를 구체적인 수에 적용해 보자.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (나눗셈 정리)**</ins> $$a = 47$$, $$b = 8$$일 때를 보자. $$47 = 8 \cdot 5 + 7$$이므로 몫은 $$q = 5$$, 나머지는 $$r = 7$$이다. 음의 피제수의 경우도 나머지는 음이 아니어야 한다. $$a = -47$$, $$b = 8$$이면

$$-47 = 8 \cdot (-6) + 1, \qquad 0 \leq 1 < 8$$

이므로 $$q = -6$$, $$r = 1$$이다. 무심코 $$-47 = 8 \cdot (-5) + (-7)$$로 쓰면 나머지가 음수여서 정리의 조건 $$0 \leq r < b$$를 어긴다는 점에 유의한다.

</div>

이렇게 정의 1 이후로 라벨 번호가 정의 1, 명제 2, 정리 3, 예시 4로 단조 증가한다. 다음 절에서는 이 도구들을 모아 두 정수의 공통 약수 구조를 분석한다.

## 최대공약수

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 둘 다 $$0$$은 아닌 정수 $$a, b$$에 대하여, $$a$$와 $$b$$를 모두 나누는 양의 정수 중 가장 큰 것을 $$a, b$$의 *최대공약수<sub>greatest common divisor</sub>*라 하고 $$\gcd(a,b)$$로 적는다. $$\gcd(a,b) = 1$$일 때 $$a$$와 $$b$$는 *서로소<sub>coprime</sub>*라 한다.

</div>

공약수 $$d$$는 명제 2.4에 의해 $$\lvert d\rvert \leq \max(\lvert a\rvert, \lvert b\rvert)$$로 유계이고 $$1$$은 항상 공약수이므로, 최대공약수는 항상 잘 정의된다. 최대공약수의 가장 중요한 성질은 그것이 단순히 "가장 큰 공약수"일 뿐 아니라, 모든 공약수가 그것을 나눈다는 점이다 — 이 사실과 다음의 선형결합 표현(Bézout 항등식)은 유클리드 호제법을 통해 다음 글에서 증명한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$\gcd(12, 18)$$을 구해 보자. $$12$$의 양의 약수는 $$1, 2, 3, 4, 6, 12$$이고 $$18$$의 양의 약수는 $$1, 2, 3, 6, 9, 18$$이므로, 공약수는 $$1, 2, 3, 6$$이고 그중 가장 큰 것은 $$6$$이다. 따라서 $$\gcd(12,18) = 6$$이다. 한편 $$\gcd(8, 15) = 1$$이므로 $$8$$과 $$15$$는 서로소이다.

</div>

약수를 일일이 나열하는 이 방법은 수가 커지면 비효율적이다. 더 큰 예로 $$\gcd(1071, 462)$$을 약수 나열로 구하려면 두 수의 약수를 모두 찾아야 하는데, 이는 사실상 두 수를 소인수분해하는 일과 다르지 않아 큰 수에서는 현실성이 없다. 다음 절에서 보듯 나눗셈 정리를 거듭 쓰면 인수분해 없이도 같은 답에 빠르게 도달한다.

## 최대공약수의 성질

최대공약수를 다룰 때 가장 유용한 사실은, 한쪽 인수에서 다른 쪽의 배수를 빼도 최대공약수가 변하지 않는다는 점이다. 이것이 유클리드 호제법을 정당화하는 핵심이며, 다음 절의 모든 계산이 이 명제 위에 선다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 둘 다 $$0$$은 아닌 정수 $$a, b$$와 임의의 정수 $$k$$에 대하여

$$\gcd(a, b) = \gcd(a, b - ka)$$

가 성립한다. 특히 $$b = qa + r$$ ($$0 \leq r < \lvert a\rvert$$) 이면 $$\gcd(a, b) = \gcd(a, r)$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a$$와 $$b$$의 공약수 집합이 $$a$$와 $$b - ka$$의 공약수 집합과 정확히 같음을 보이면 충분하다. 두 집합이 같으면 그중 최댓값인 최대공약수도 같기 때문이다.

$$d$$가 $$a$$와 $$b$$의 공약수라 하자. 그러면 $$d \mid a$$, $$d \mid b$$이므로 명제 2.3에 의해

$$\begin{aligned}
d &\mid (b \cdot 1 + a \cdot (-k)) \\
&= b - ka
\end{aligned}$$

이고, $$d \mid a$$와 합하면 $$d$$는 $$a$$와 $$b - ka$$의 공약수이다. 역으로 $$d$$가 $$a$$와 $$b - ka$$의 공약수이면 $$d \mid a$$, $$d \mid (b - ka)$$이므로 다시 명제 2.3에 의해

$$\begin{aligned}
d &\mid ((b - ka) \cdot 1 + a \cdot k) \\
&= b
\end{aligned}$$

이고, $$d$$는 $$a$$와 $$b$$의 공약수이다. 두 공약수 집합이 일치하므로 최대공약수가 같다.

</details>

특별한 경우로 $$k$$를 골라 $$b - ka$$를 나머지 $$r$$로 만들면, 큰 수의 최대공약수를 더 작은 수의 최대공약수로 줄일 수 있다. 이 축소를 반복하는 것이 다음 글의 유클리드 호제법이다. 다음 예시에서 그 한 단계를 직접 따라가 보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (최대공약수 축소)**</ins> 명제 7로 $$\gcd(1071, 462)$$을 줄여 보자. 나눗셈 정리로

$$\begin{aligned}
1071 &= 2 \cdot 462 + 147, \\
462 &= 3 \cdot 147 + 21, \\
147 &= 7 \cdot 21 + 0
\end{aligned}$$

이므로, 명제 7을 한 줄씩 적용하면

$$\gcd(1071, 462) = \gcd(462, 147) = \gcd(147, 21) = \gcd(21, 0) = 21$$

이다. 나머지가 $$0$$이 되는 직전 단계의 나눗수 $$21$$이 곧 최대공약수이다. 약수를 일일이 나열하지 않고 단 세 번의 나눗셈으로 답을 얻었다.

</div>

서로소인 경우에는 한 약수가 곱의 다른 인수로 "넘어가는" 성질이 성립한다. 이는 다음 글들에서 소수의 성질과 일차합동식을 다룰 때 반복적으로 쓰인다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 정수 $$a, b, c$$에 대하여 $$a \mid bc$$이고 $$\gcd(a, b) = 1$$이면 $$a \mid c$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gcd(a, b) = 1$$이면 다음 글의 Bézout 항등식에 의해 적당한 정수 $$x, y$$가 존재하여

$$ax + by = 1$$

이다 ([§유클리드 호제법과 Bézout 항등식](/ko/math/number_theory/euclidean_algorithm)). 양변에 $$c$$를 곱하면

$$\begin{aligned}
c &= acx + bcy \\
&= a(cx) + (bc)y
\end{aligned}$$

이다. 우변의 첫 항은 $$a$$의 배수이고, 둘째 항은 $$a \mid bc$$이므로 역시 $$a$$의 배수이다. 따라서 명제 2.3에 의해 $$a$$는 두 배수의 합 $$c$$를 나눈다.

</details>

서로소 조건이 빠지면 이 결론은 깨진다. 가령 $$6 \mid 4 \cdot 9 = 36$$이지만 $$\gcd(6, 4) = 2 \neq 1$$이라 $$6 \nmid 4$$이고 $$6 \nmid 9$$이다. 즉 $$a \mid bc$$만으로는 $$a$$가 $$b$$나 $$c$$ 어느 한쪽을 나눈다는 보장이 없으며, 서로소 조건이 결정적임을 알 수 있다. 명제 9는 다음 글에서 소수가 곱을 나누면 인수 중 하나를 나눈다는 *유클리드 보조정리<sub>Euclid's lemma</sub>*의 토대가 되고, 그것이 다시 [§소수와 산술의 기본정리](/ko/math/number_theory/primes)에서 소인수분해의 유일성을 떠받친다.

마지막으로 최대공약수와 짝을 이루는 개념인 최소공배수를 정의하고, 둘 사이의 깔끔한 관계를 확인한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 둘 다 $$0$$은 아닌 정수 $$a, b$$에 대하여, $$a$$와 $$b$$를 모두 배수로 갖는 양의 정수 중 가장 작은 것을 $$a, b$$의 *최소공배수<sub>least common multiple</sub>*라 하고 $$\operatorname{lcm}(a, b)$$로 적는다.

</div>

공배수 $$\lvert ab\rvert$$가 항상 존재하므로 양의 공배수 전체는 공집합이 아닌 양의 정수 집합이고, 정렬성에 의해 최솟값이 존재하여 최소공배수는 잘 정의된다. 최대공약수와 최소공배수는 다음의 곱 관계로 서로 묶인다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 양의 정수 $$a, b$$에 대하여

$$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = ab$$

가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$d = \gcd(a, b)$$로 두고 $$a = d a'$$, $$b = d b'$$로 쓰면, 약수를 $$d$$로 모두 떼어 낸 $$a', b'$$은 서로소이다 ($$\gcd(a', b') > 1$$이면 그 공약수에 $$d$$를 곱한 것이 $$a, b$$의 더 큰 공약수가 되어 모순). 이제

$$m = \frac{ab}{d} = \frac{(d a')(d b')}{d} = d a' b'$$

이 $$\operatorname{lcm}(a, b)$$임을 보이자. $$m = (d a') b' = a b'$$이자 $$m = (d b') a' = b a'$$이므로 $$m$$은 $$a$$와 $$b$$의 공배수이다. 한편 $$n$$이 임의의 양의 공배수이면 $$a \mid n$$에서 $$n = a k = d a' k$$이고, $$b \mid n$$에서 $$d b' \mid d a' k$$, 즉 $$b' \mid a' k$$이다. $$\gcd(a', b') = 1$$이므로 명제 9에 의해 $$b' \mid k$$이고, 따라서

$$\begin{aligned}
n &= d a' k \\
&\geq d a' b' = m
\end{aligned}$$

이다. 그러므로 $$m$$은 가장 작은 양의 공배수, 곧 $$\operatorname{lcm}(a, b)$$이고 $$\gcd(a,b)\cdot\operatorname{lcm}(a,b) = d \cdot m = d \cdot d a' b' = (d a')(d b') = ab$$이다.

</details>

이 관계 덕분에 최소공배수는 최대공약수 하나만 계산하면 곧바로 얻어진다. 예시 8에서 $$\gcd(1071, 462) = 21$$이었으므로

$$\operatorname{lcm}(1071, 462) = \frac{1071 \cdot 462}{21} = \frac{494802}{21} = 23562$$

이다. 또 작은 예로 예시 6의 $$\gcd(12, 18) = 6$$에서 $$\operatorname{lcm}(12, 18) = \dfrac{12 \cdot 18}{6} = 36$$을 얻는다.

다음 글에서 나눗셈 정리를 반복 적용하여 최대공약수를 빠르게 계산하는 유클리드 호제법을 체계적으로 다루고, 그로부터 $$\gcd(a,b)$$를 $$ax + by$$ 꼴로 표현하는 Bézout 항등식을 얻는다 — 명제 9의 증명에서 이미 이 표현을 미리 끌어 썼다. 이 표현은 이후 [§소수와 산술의 기본정리](/ko/math/number_theory/primes)와 [§합동식](/ko/math/number_theory/congruences) 전반에서 결정적 역할을 한다.
