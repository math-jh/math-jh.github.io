---
title: "일차 합동식"
description: "일차 합동식 ax ≡ b (mod n)의 해를 다룬다. 해가 존재할 조건이 gcd(a,n)이 b를 나누는 것임을 보이고, 그 경우 법 n에 대한 해의 개수가 정확히 gcd(a,n)임을 증명하며 곱셈 역원으로 해를 구한다."
excerpt: "일차 합동식의 가해성, 해의 개수, 해법"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/linear_congruences
sidebar: 
    nav: "number_theory-ko"

header:
    overlay_image: /assets/images/Math/Number_Theory/Linear_Congruences.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 6

published: false
---

[§합동식](/ko/math/number_theory/congruences)에서 합동의 연산과 곱셈 역원을 다루었다. 이제 가장 기본적인 합동방정식인 일차 합동식 $$ax \equiv b \pmod n$$의 해를 분석한다. 이는 일차 부정방정식 $$ax + ny = b$$를 푸는 것과 같은 문제이며, Bézout 항등식이 그 가해성을 완전히 결정한다.

일차 합동식이 다루기 까다로운 것은 정수에서의 일차방정식 $$ax = b$$와 달리 "나눗셈"이 늘 가능하지는 않기 때문이다. 실수 위에서라면 $$a \neq 0$$일 때 $$x = b/a$$가 유일한 해이지만, 법 $$n$$ 아래에서는 $$a$$로 나누는 일이 $$a$$의 역원을 곱하는 일로 바뀌고, 그 역원은 $$\gcd(a, n) = 1$$일 때에만 존재한다. 따라서 $$a$$와 $$n$$이 공약수를 가지면 해가 아예 없거나, 반대로 여러 개로 갈라진다. 이 글에서 우리는 그 갈림을 $$d = \gcd(a, n)$$ 하나로 깔끔하게 정리한다.

또한 일차 합동식은 합동의 언어로 적혔지만 본질은 정수 해를 묻는 디오판토스 문제이다. $$ax \equiv b \pmod n$$이 해를 가진다는 것은 적당한 정수 $$y$$에 대해 $$ax - ny = b$$가 성립한다는 뜻이고, 좌변이 취할 수 있는 정수 전체가 정확히 $$\gcd(a, n)$$의 배수 전체임은 이미 Bézout 항등식에서 보았다. 가해성의 판정과 해의 명시적 구성이 모두 유클리드 호제법 한 번으로 환원되는 셈이다.

## 가해성과 해의 개수

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> $$d = \gcd(a, n)$$이라 하자. 일차 합동식 $$ax \equiv b \pmod n$$은 $$d \mid b$$일 때에만 해를 가지며, 이 경우 법 $$n$$에 대해 서로 다른 해가 정확히 $$d$$개 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$ax \equiv b \pmod n$$은 정의상 $$n \mid ax - b$$, 즉 적당한 정수 $$y$$에 대해

$$\begin{aligned}
ax - b &= ny \\
ax - ny &= b
\end{aligned}$$

가 성립한다는 것과 동치이다. 좌변 $$ax - ny$$가 $$x, y$$를 정수 전체에 걸쳐 움직일 때 취하는 값 전체는 $$\gcd(a, n) = d$$의 배수 전체와 정확히 일치하므로 ([§유클리드 호제법과 Bézout 항등식, ⁋따름정리 4](/ko/math/number_theory/euclidean_algorithm#cor4)), 위 방정식이 풀릴 필요충분조건은 $$d \mid b$$이다.

이제 $$d \mid b$$라 하고 $$a = da'$$, $$n = dn'$$, $$b = db'$$로 쓰자. 이때 $$\gcd(a', n') = 1$$이며, $$ax \equiv b \pmod n$$의 양변과 법을 공통인수 $$d$$로 나누면

$$a'x \equiv b' \pmod{n'}$$

과 동치가 된다 (합동식을 그 법과 서로소가 아닌 공약수로 약분할 때 법도 함께 나눠야 함에 주의한다). $$\gcd(a', n') = 1$$이므로 $$a'$$은 법 $$n'$$에 대해 곱셈 역원 $$(a')^{-1}$$을 가지고 ([§합동식, ⁋명제 7](/ko/math/number_theory/congruences#prop7)), 양변에 그것을 곱하면

$$x \equiv (a')^{-1} b' \pmod{n'}$$

이라는 법 $$n'$$에 대한 유일한 해를 얻는다. 마지막으로 법을 다시 $$n = dn'$$으로 되돌린다. 법 $$n'$$에 대한 한 잉여류 $$x \equiv x_0 \pmod{n'}$$은 법 $$n$$ 아래에서

$$x_0,\quad x_0 + n',\quad x_0 + 2n',\quad \ldots,\quad x_0 + (d-1)n'$$

라는 서로 다른 $$d$$개의 잉여류로 갈라진다. 이들은 모두 법 $$n'$$으로는 합동이지만 법 $$n$$으로는 서로 다르고, $$x_0 + dn' = x_0 + n \equiv x_0 \pmod n$$이므로 이 목록은 더 늘지 않는다. 따라서 법 $$n$$에 대한 해는 정확히 $$d$$개이다.

</details>

특히 $$\gcd(a, n) = 1$$이면 임의의 $$b$$에 대해 해가 유일하게 존재하며, 그 해는 $$x \equiv a^{-1}b \pmod n$$이다. 역원 $$a^{-1}$$은 Bézout 항등식 $$ax + ny = 1$$을 유클리드 호제법으로 풀어 얻는다. 증명은 동시에 해를 찾는 절차도 알려 준다. 즉 (i) $$d = \gcd(a, n)$$을 구해 $$d \mid b$$인지 확인하고, (ii) $$d \nmid b$$이면 해가 없다고 결론지으며, (iii) $$d \mid b$$이면 양변과 법을 $$d$$로 나눠 $$a'x \equiv b' \pmod{n'}$$을 만든 뒤 $$a'$$의 역원을 곱해 대표해 $$x_0$$을 얻고, (iv) $$x_0, x_0 + n', \ldots, x_0 + (d-1)n'$$로 법 $$n$$에 대한 $$d$$개의 해를 모두 적는다.

이 절차에서 가장 무거운 단계는 역원을 구하는 (iii)이다. $$\gcd(a', n') = 1$$이므로 유클리드 호제법을 거꾸로 펼친 확장 유클리드 알고리즘이 $$a' s + n' t = 1$$인 정수 $$s, t$$를 주고, 그러면 $$a's \equiv 1 \pmod{n'}$$이어서 $$(a')^{-1} \equiv s \pmod{n'}$$이다. 작은 법에서는 시행착오로도 역원을 찾을 수 있으나, 큰 법에서는 이 알고리즘이 표준적인 방법이다.

## 해법과 예시

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $$6x \equiv 8 \pmod{14}$$를 풀자. $$d = \gcd(6, 14) = 2$$이고 $$2 \mid 8$$이므로 해가 있으며, 그 개수는 $$2$$이다. 양변과 법을 $$2$$로 나누면 $$3x \equiv 4 \pmod 7$$이고, $$3^{-1} \equiv 5 \pmod 7$$ ($$3\cdot 5 = 15 \equiv 1$$) 이므로 $$x \equiv 5\cdot 4 = 20 \equiv 6 \pmod 7$$이다. 법 $$14$$로 올리면 해는 $$x \equiv 6$$과 $$x \equiv 13 \pmod{14}$$의 두 개이다.

</div>

예시 2의 마지막 단계가 보여 주듯, 법을 $$7$$에서 다시 $$14$$로 올릴 때 대표해 $$x \equiv 6$$에 약분에 쓴 새 법 $$n' = 7$$을 거듭 더해 $$6, 6+7 = 13$$의 두 잉여류를 얻는다. 만약 법 $$n = dn'$$을 한 번에 떠올리기 어렵다면, 법 $$n'$$에서 얻은 해의 정수 대표들을 $$0$$부터 $$n-1$$까지 늘어놓고 그중 원래 식을 만족하는 것을 모두 골라도 같은 결과가 나온다. 어느 쪽이든 해의 개수가 정확히 $$d$$임은 정리 1이 보장한다.

가해성 조건이 깨지는 경우도 분명히 해 두자. $$d \nmid b$$이면 어떤 정수를 넣어도 식이 성립하지 않는다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (해가 없는 경우)**</ins> $$4x \equiv 3 \pmod 6$$을 보자. $$d = \gcd(4, 6) = 2$$인데 $$2 \nmid 3$$이므로 정리 1에 의해 해가 없다. 실제로 $$4x$$는 언제나 짝수이고 그것을 $$6$$으로 나눈 나머지도 $$0, 2, 4$$ 중 하나여서 결코 $$3$$이 될 수 없다. 일반적으로 $$4x \pmod 6$$이 취하는 값은 $$\{0, 4, 2, 0, 4, 2, \ldots\}$$로 $$d = 2$$의 배수뿐이며, 우변이 이 집합에 속할 때에만 (즉 $$2 \mid b$$일 때에만) 해가 있다.

</div>

서로소인 계수의 경우는 해가 유일하므로 가장 자주 쓰인다. 이때 핵심은 역원 $$a^{-1}$$을 빠르게 구하는 일이다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (확장 유클리드로 역원 구하기)**</ins> $$17x \equiv 5 \pmod{43}$$을 풀자. $$\gcd(17, 43) = 1$$이므로 해가 유일하다. 확장 유클리드 알고리즘으로 $$17^{-1} \pmod{43}$$을 구한다. 호제법은

$$\begin{aligned}
43 &= 2\cdot 17 + 9, \\
17 &= 1\cdot 9 + 8, \\
9 &= 1\cdot 8 + 1, \\
8 &= 8\cdot 1 + 0
\end{aligned}$$

이고, 나머지를 거꾸로 대입하면

$$\begin{aligned}
1 &= 9 - 1\cdot 8 \\
&= 9 - (17 - 9) = 2\cdot 9 - 17 \\
&= 2(43 - 2\cdot 17) - 17 = 2\cdot 43 - 5\cdot 17
\end{aligned}$$

이다. 따라서 $$-5 \cdot 17 \equiv 1 \pmod{43}$$, 곧 $$17^{-1} \equiv -5 \equiv 38 \pmod{43}$$이다. 그러면

$$x \equiv 17^{-1}\cdot 5 \equiv 38 \cdot 5 = 190 \equiv 190 - 4\cdot 43 = 18 \pmod{43}$$

이므로 유일한 해는 $$x \equiv 18 \pmod{43}$$이다.

</div>

역원을 따로 구하지 않고 합동식을 직접 조작해도 된다. 한쪽 변에 법의 배수를 더해 계수가 작아지도록 바꾸는 기법이 작은 법에서 특히 편리하다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (배수를 더해 약분하기)**</ins> $$7x \equiv 3 \pmod{10}$$을 풀자. $$\gcd(7, 10) = 1$$이므로 해가 유일하다. 우변에 법 $$10$$의 배수를 더해 가며 계수 $$7$$로 나누어떨어지는 값을 찾는다:

$$3 \equiv 13 \equiv 23 \equiv 33 \equiv 43 \equiv 53 \equiv 63 \pmod{10},$$

이고 $$63 = 7\cdot 9$$이므로 $$7x \equiv 63 \pmod{10}$$이다. 양변에서 $$\gcd(7, 10) = 1$$이라 계수 $$7$$을 법을 바꾸지 않고 그대로 약분할 수 있어 ([명제 7](#prop7))

$$x \equiv 9 \pmod{10}$$

을 얻는다. 같은 답을 역원으로도 확인할 수 있다. $$7\cdot 3 = 21 \equiv 1 \pmod{10}$$이므로 $$7^{-1} \equiv 3$$이고 $$x \equiv 7^{-1}\cdot 3 \equiv 3\cdot 3 = 9 \pmod{10}$$이다. 검산하면 $$7\cdot 9 = 63 \equiv 3 \pmod{10}$$으로 맞다. 작은 법에서는 이렇게 계수로 나누어떨어지는 우변을 눈으로 찾거나 작은 역원을 떠올리는 편이 빠르다.

</div>

## 해의 구조와 약분

해의 집합이 가지는 구조를 명제로 정리하면, 위 예시들에서 본 "한 해를 알면 나머지가 자동으로 따라온다"는 현상이 분명해진다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (해 집합의 구조)**</ins> $$d = \gcd(a, n)$$이고 $$d \mid b$$라 하자. $$x_0$$이 $$ax \equiv b \pmod n$$의 한 정수해이면, 정수해 전체는

$$x \equiv x_0 + \frac{n}{d}\,k \pmod n \qquad (k = 0, 1, \ldots, d-1)$$

로 주어지며, 이것이 정리 1이 말하는 $$d$$개의 잉여류이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x$$가 해라 하자. $$ax \equiv b \equiv ax_0 \pmod n$$이므로 $$a(x - x_0) \equiv 0 \pmod n$$, 곧 $$n \mid a(x - x_0)$$이다. $$a = da'$$, $$n = dn'$$ ($$\gcd(a', n') = 1$$) 로 쓰면

$$\begin{aligned}
dn' &\mid da'(x - x_0) \\
n' &\mid a'(x - x_0)
\end{aligned}$$

이고, $$\gcd(a', n') = 1$$이므로 $$n' \mid x - x_0$$이다 ([§유클리드 호제법과 Bézout 항등식, ⁋따름정리 4](/ko/math/number_theory/euclidean_algorithm#cor4)에서 따르는 Euclid 보조정리). 곧 $$x = x_0 + n' k = x_0 + \tfrac{n}{d}k$$ 꼴이며, 역으로 이런 모든 $$x$$가 $$a(x - x_0) = a n' k = a' n k$$를 만족해 해가 된다. 법 $$n$$ 아래에서 $$k$$와 $$k + d$$는 같은 잉여류를 주므로 ($$\tfrac{n}{d}(k+d) = \tfrac{n}{d}k + n$$), 서로 다른 해는 $$k = 0, 1, \ldots, d-1$$의 $$d$$개이다.

</details>

명제 6은 해들이 등차적으로 $$\tfrac{n}{d}$$ 간격으로 배열됨을 말한다. 예시 2에서 $$d = 2$$, $$\tfrac{n}{d} = 7$$이었고 해가 $$6, 13$$으로 정확히 $$7$$만큼 떨어져 있었던 것이 이 명제의 구체적 사례이다. 또 합동식을 약분할 때 법을 함께 나눠야 하는 이유도 여기서 분명하다. $$\gcd(a, n) = d$$로 양변을 나누면 정보가 법 $$n$$ 수준에서 법 $$n/d$$ 수준으로 줄어들고, 잃어버린 $$d$$겹의 정보가 바로 해의 다중성이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (소거 법칙)**</ins> $$ca \equiv cb \pmod n$$이고 $$\gcd(c, n) = 1$$이면 $$a \equiv b \pmod n$$이다. 더 일반적으로 $$g = \gcd(c, n)$$이면

$$ca \equiv cb \pmod n \iff a \equiv b \pmod{n/g}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$ca \equiv cb \pmod n$$은 $$n \mid c(a - b)$$와 동치이다. $$g = \gcd(c, n)$$, $$c = gc'$$, $$n = gn'$$ ($$\gcd(c', n') = 1$$) 로 쓰면

$$\begin{aligned}
n \mid c(a-b) &\iff gn' \mid gc'(a-b) \\
&\iff n' \mid c'(a-b) \\
&\iff n' \mid a - b
\end{aligned}$$

이며, 마지막 동치는 $$\gcd(c', n') = 1$$에서 따른다. 곧 $$a \equiv b \pmod{n/g}$$이다. 특히 $$\gcd(c, n) = 1$$이면 $$g = 1$$, $$n/g = n$$이어서 법이 그대로 보존되는 통상의 소거 법칙을 얻는다.

</details>

소거 법칙은 일차 합동식을 손으로 풀 때 가장 자주 쓰는 도구이다. 계수와 법이 공약수를 가지면 무턱대고 약분해서는 안 되고, 명제 7에 따라 법을 동시에 조정해야 등치가 유지된다. 가령 $$8x \equiv 12 \pmod{20}$$에서 양변을 $$4$$로 나눌 때 $$g = \gcd(4, 20) = 4$$이므로 법도 $$20/4 = 5$$로 줄여 $$2x \equiv 3 \pmod 5$$를 얻어야 하며, 이는 $$x \equiv 4 \pmod 5$$, 곧 법 $$20$$에 대해 $$x \equiv 4, 9, 14, 19$$의 네 해를 준다 ($$d = \gcd(8, 20) = 4$$와 일치).

## 응용과 추가 예시

일차 합동식은 정수론의 거의 모든 곳에서 부품처럼 등장한다. 가장 직접적인 응용은 곱셈 역원 자체를 계산하는 것이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (역원표의 계산)**</ins> 법 $$7$$에 대한 곱셈 역원을 모두 구하려면 각 $$a$$에 대해 $$ax \equiv 1 \pmod 7$$을 풀면 된다. $$\gcd(a, 7) = 1$$이 $$a = 1, \ldots, 6$$ 모두에서 성립하므로 전부 역원을 가진다:

$$\begin{aligned}
1\cdot 1 &\equiv 1, & 2\cdot 4 &\equiv 1, & 3\cdot 5 &\equiv 1, \\
4\cdot 2 &\equiv 1, & 5\cdot 3 &\equiv 1, & 6\cdot 6 &\equiv 1 \pmod 7.
\end{aligned}$$

따라서 $$1^{-1} = 1$$, $$2^{-1} = 4$$, $$3^{-1} = 5$$, $$4^{-1} = 2$$, $$5^{-1} = 3$$, $$6^{-1} = 6$$이다. 법이 소수일 때 $$0$$을 제외한 모든 원소가 역원을 가짐은 [§합동식, ⁋명제 7](/ko/math/number_theory/congruences#prop7)의 직접적 귀결이다.

</div>

또 일차 합동식은 일차 디오판토스 방정식의 특수해를 빠르게 찾는 데에도 쓰인다. $$ax + ny = b$$의 정수해를 구할 때, 먼저 $$ax \equiv b \pmod n$$을 풀어 $$x$$를 얻고 그로부터 $$y = (b - ax)/n$$을 결정하면 된다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (디오판토스 방정식)**</ins> $$15x + 6y = 9$$의 정수해를 구하자. $$d = \gcd(15, 6) = 3$$이고 $$3 \mid 9$$이므로 해가 있다. 법 $$6$$으로 보면 $$15x \equiv 9 \pmod 6$$, 곧 $$3x \equiv 3 \pmod 6$$이고, 명제 7에 따라 $$g = \gcd(3, 6) = 3$$으로 약분하면 $$x \equiv 1 \pmod 2$$이다. 따라서 $$x = 1 + 2t$$ ($$t \in \mathbb{Z}$$) 이고,

$$y = \frac{9 - 15x}{6} = \frac{9 - 15(1 + 2t)}{6} = \frac{-6 - 30t}{6} = -1 - 5t$$

이다. 곧 일반해는 $$(x, y) = (1 + 2t,\ -1 - 5t)$$이며, 가령 $$t = 0$$이면 $$(1, -1)$$이 $$15 - 6 = 9$$로 검산된다.

</div>

마지막으로 여러 법에 대한 합동을 다룰 때 일차 합동식이 어떻게 결합되는지 미리 살펴보자. 두 합동을 하나로 줄이는 과정 자체가 일차 합동식 풀이이다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (두 합동의 결합)**</ins> $$x \equiv 2 \pmod 3$$이면서 $$x \equiv 3 \pmod 5$$인 $$x$$를 찾자. 첫 식에서 $$x = 2 + 3s$$ ($$s \in \mathbb{Z}$$) 로 쓰고 둘째 식에 대입하면

$$2 + 3s \equiv 3 \pmod 5 \quad\Longrightarrow\quad 3s \equiv 1 \pmod 5$$

이다. $$3^{-1} \equiv 2 \pmod 5$$ ($$3\cdot 2 = 6 \equiv 1$$) 이므로 $$s \equiv 2 \pmod 5$$, 곧 $$s = 2 + 5u$$이고

$$x = 2 + 3(2 + 5u) = 8 + 15u$$

이다. 따라서 $$x \equiv 8 \pmod{15}$$가 두 합동을 동시에 만족하는 유일한 잉여류이다. 법 $$3$$과 $$5$$가 서로소이므로 합쳐진 법이 $$3\cdot 5 = 15$$가 되었고 해가 유일하게 나왔다.

</div>

예시 10에서 두 합동을 결합하는 과정의 핵심 단계 $$3s \equiv 1 \pmod 5$$가 바로 일차 합동식이었다. 일반적으로 여러 법에 대한 합동계를 푸는 일은 이런 결합을 반복하는 것이며, 법들이 쌍마다 서로소일 때 그 결과가 항상 존재하고 유일함을 다음 글에서 정리한다.

일차 합동식은 한 개의 법에 대한 가장 단순한 방정식이다. 서로 다른 여러 법에 대한 합동식을 동시에 만족시키는 해를 찾는 문제는 다음 글 [§중국인의 나머지 정리](/ko/math/number_theory/chinese_remainder_theorem)에서 다루며, 그곳에서 법들이 쌍마다 서로소일 때 해가 항상 존재하고 유일함을 본다.
