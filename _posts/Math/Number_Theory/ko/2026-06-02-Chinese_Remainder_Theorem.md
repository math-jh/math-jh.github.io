---
title: "합동식과 중국인의 나머지 정리"
description: "법 n에 대한 합동의 정의와 연산, 약분 법칙, 완전잉여계와 ℤ/nℤ를 정리하고 일차 합동식 ax≡b의 해의 존재와 개수를 결정한다. 이어서 서로소인 법에 대한 중국인의 나머지 정리와, 법이 서로소가 아닐 때 연립합동식이 해를 갖는 조건을 증명한다."
excerpt: "합동의 연산, 약분 법칙, 일차 합동식, 모듈러 역원, 중국인의 나머지 정리"

categories: [Math / Number Theory]
permalink: /ko/math/number_theory/chinese_remainder_theorem
sidebar: 
    nav: "number_theory-ko"

date: 2026-06-02
weight: 3

published: false

---

정수를 $n$으로 나눈 나머지만이 문제가 되는 경우가 많다. 요일 계산, 큰 수의 끝자리, 정수해의 존재 여부 따위가 그렇다. 합동은 이 나머지에 관한 추론을 등식과 같은 형태로 적게 해 주는 언어이다. 이 글에서는 합동의 정의와 연산 규칙, 약분이 허용되는 조건, 일차 합동식의 풀이를 정리하고, 이를 바탕으로 서로 다른 법에 관한 조건을 한꺼번에 만족하는 정수를 찾는 중국인의 나머지 정리를 증명한다. 증명에서는 [§나눗셈과 유클리드 호제법, ⁋정리 8](/ko/math/number_theory/euclidean_algorithm#thm8), 즉 두 정수 $a, b$에 대해 $\gcd(a,b)=au+bv$인 정수 $u, v$가 존재한다는 사실을 쓴다.

## 합동과 그 연산

::: 정의 1
양의 정수 $n$과 정수 $a, b$에 대하여 $n \mid (a-b)$일 때 *$a$와 $b$는 법 $n$에 대해 합동<sub>congruent modulo $n$</sub>*이라 하고

$$a \equiv b \pmod{n}$$

으로 적는다. 이때 $n$을 *법<sub>modulus</sub>*이라 한다.
:::

$a$와 $b$를 $n$으로 나눈 나머지가 같다는 것과 $a \equiv b \pmod{n}$은 동치이다. [§나눗셈과 유클리드 호제법, ⁋정리 3](/ko/math/number_theory/euclidean_algorithm#thm3)에 의하여 $a = nq+r$, $b = nq'+r'$($0 \le r, r' < n$)이라 하면 $a-b = n(q-q') + (r-r')$이고 $\lvert r-r'\rvert < n$이므로, $n \mid (a-b)$인 것은 $r = r'$인 것과 같다. 따라서 합동은 정수 위의 동치관계이다. 반사성은 $n \mid 0$에서, 대칭성은 $a-b$와 $b-a$가 서로 배수·약수 관계라는 데서, 추이성은 $a-c = (a-b)+(b-c)$에서 나온다.

::: 명제 2
$a \equiv b \pmod{n}$이고 $c \equiv d \pmod{n}$이면 다음의 합동식

$$a + c \equiv b + d, \qquad a - c \equiv b - d, \qquad ac \equiv bd \pmod{n}$$

이 성립한다. 특히 모든 자연수 $k$에 대해 $a^k \equiv b^k \pmod{n}$이다.
:::

::: 증명
$(a+c)-(b+d) = (a-b)+(c-d)$와 $(a-c)-(b-d) = (a-b)-(c-d)$는 $n$의 배수 둘의 합과 차이므로 [§나눗셈과 유클리드 호제법, ⁋명제 2](/ko/math/number_theory/euclidean_algorithm#prop2)의 (2)에 의하여 $n$의 배수이다. 곱에 대해서는 $ac - bd = a(c-d) + d(a-b)$가 $n$의 배수이다. 거듭제곱은 곱셈 규칙을 $k$번 적용하면 된다.
:::

[명제 2](#prop2)는 합동식의 양변에 같은 수를 더하거나 곱해도 합동이 유지되고, 합동인 수끼리는 덧셈·뺄셈·곱셈 안에서 서로 바꿔 넣을 수 있음을 뜻한다. 가령 $7^{100}$을 $10$으로 나눈 나머지는 $7^2 = 49 \equiv -1 \pmod{10}$에서 $7^{100} = (7^2)^{50} \equiv (-1)^{50} = 1$로 구한다. 반면 나눗셈은 일반적으로 허용되지 않는다. $2 \cdot 3 \equiv 2 \cdot 0 \pmod{6}$이지만 $3 \not\equiv 0 \pmod{6}$이다. 나눗셈이 어느 범위에서 허용되는지는 다음 명제가 정확히 말해 준다.

::: 명제 3 (약분 법칙)
$n$이 양의 정수이고 $c \ne 0$이 정수라 하자. $d = \gcd(c, n)$일 때

$$ac \equiv bc \pmod{n} \quad\Longrightarrow\quad a \equiv b \pmod{n/d}$$

이다. 특히 $\gcd(c,n)=1$이면 $ac \equiv bc \pmod{n}$에서 $a \equiv b \pmod{n}$을 얻는다.
:::

::: 증명
$c = dc'$, $n = dn'$이라 쓰면 $\gcd(c', n') = 1$이다. 실제로 [§나눗셈과 유클리드 호제법, ⁋정리 8](/ko/math/number_theory/euclidean_algorithm#thm8)에 의하여 $d = cu + nv$로 쓰고 양변을 $d$로 나누면 $1 = c'u + n'v$이다. $n \mid c(a-b)$는 $dn' \mid dc'(a-b)$, 곧 $n' \mid c'(a-b)$와 동치이다. $\gcd(c', n')=1$이므로 [§나눗셈과 유클리드 호제법, ⁋명제 11](/ko/math/number_theory/euclidean_algorithm#prop11)에 의하여 $n' \mid (a-b)$이다.
:::

주의할 점은 법이 $n$인 채로 약분하면 안 되고, 약분한 인수 $d=\gcd(c,n)$만큼 법을 줄여야 한다는 것이다. 이 점을 놓치는 것이 합동식에서 가장 흔한 실수이다.

::: 예시 4
$12 \cdot 2 \equiv 12 \cdot 5 \pmod{18}$이다($24-60 = -36$). $\gcd(12, 18) = 6$이므로 [명제 3](#prop3)에 의하여 얻는 결론은 $2 \equiv 5 \pmod{3}$이고, 이는 참이다. 법을 $18$로 둔 채 $2 \equiv 5 \pmod{18}$이라고 하면 거짓이다. 법이 $n/d$로 줄어든다는 것은 $d$가 클수록 약분 후의 정보가 약해진다는 뜻이며, $c$가 $n$의 배수($d = n$)인 극단에서는 $ac \equiv bc \equiv 0$이 항상 성립하여 $a, b$에 대한 정보가 전혀 남지 않는다.
:::

## 잉여류와 ℤ/nℤ

법 $n$에 대한 합동은 동치관계이므로 정수 전체를 equivalence class로 나눈다. $a$를 포함하는 equivalence class $[a] = \{a + nk : k \in \mathbb{Z}\}$를 법 $n$에 대한 *residue class*라 하고, 이들의 모임을 $\mathbb{Z}/n\mathbb{Z}$로 적는다. 나머지가 $0, 1, \dots, n-1$인 정수가 각각 정확히 하나의 residue class를 정하므로 $\mathbb{Z}/n\mathbb{Z}$는 $n$개의 원소 $[0], [1], \dots, [n-1]$로 이루어진다. 일반적으로 법 $n$에 대한 *완전잉여계*란 residue class마다 정확히 하나씩의 representative를 뽑은 정수 $n$개의 모임이다. $\{0, 1, \dots, n-1\}$이 표준적인 선택이고, $\{1, 2, \dots, n\}$이나 $n$이 홀수일 때의 $\{-(n-1)/2, \dots, (n-1)/2\}$도 완전잉여계이다. 정수 $n$개가 완전잉여계인 것은 이들이 법 $n$에 대해 서로 합동이 아닌 것과 동치이다.

[명제 2](#prop2)는 $[a]+[b] = [a+b]$, $[a][b] = [ab]$가 representative의 선택과 무관하게 잘 정의됨을 말한다. 이 연산으로 $\mathbb{Z}/n\mathbb{Z}$는 단위원 $[1]$을 갖는 commutative ring이 된다. 환의 공리는 $\mathbb{Z}$에서 그대로 옮겨진다. 이 환에서 $[a]$가 곱셈 역원을 갖는지의 여부는 다음 절에서 결정된다.

## 일차 합동식

일차 합동식 $ax \equiv b \pmod{n}$을 푼다는 것은 이를 만족하는 정수 $x$ 전체를 구하는 것이다. $x$가 해이면 $x$와 합동인 모든 수도 해이므로, 해의 개수는 법 $n$에 대한 residue class의 개수로 센다.

::: 정리 5
양의 정수 $n$과 정수 $a, b$에 대해 $g = \gcd(a, n)$이라 하자.

(a) $ax \equiv b \pmod{n}$이 해를 가질 필요충분조건은 $g \mid b$이다.

(b) 해가 존재하면 해는 법 $n$에 대해 정확히 $g$개이다. $x_0$가 하나의 해일 때 해 전체는 $x_0 + (n/g)k$ ($k \in \mathbb{Z}$)이고, 법 $n$의 residue class로는 $k = 0, 1, \dots, g-1$에 대응하는 $x_0, x_0 + n/g, \dots, x_0 + (g-1)n/g$로 주어진다.
:::

::: 증명
(a) 해 $x$가 있으면 $ax - b = ny$인 정수 $y$가 있고, $g$가 $a$와 $n$을 나누므로 [§나눗셈과 유클리드 호제법, ⁋명제 2](/ko/math/number_theory/euclidean_algorithm#prop2)의 (2)에 의하여 $b = ax - ny$도 나눈다. 반대로 $g \mid b$라 하자. [§나눗셈과 유클리드 호제법, ⁋정리 8](/ko/math/number_theory/euclidean_algorithm#thm8)에 의하여 $au + nv = g$인 정수 $u, v$가 있고, $x_0 = u(b/g)$로 두면

$$ax_0 = (g - nv)\frac{b}{g} = b - n\frac{vb}{g}$$

이다. $b/g$가 정수이므로 $ax_0 \equiv b \pmod{n}$이다.

(b) $x_0$가 해라 하자. 정수 $x$에 대해 $ax \equiv b \equiv ax_0$이고 이는 $a(x - x_0) \equiv 0 \pmod{n}$과 동치이다. $a = ga'$, $n = gn'$으로 쓰면 [§나눗셈과 유클리드 호제법, ⁋따름정리 9](/ko/math/number_theory/euclidean_algorithm#cor9)에 의하여 $\gcd(a', n')=1$이고, $n \mid a(x-x_0)$는 $n' \mid a'(x - x_0)$와 동치이므로 [§나눗셈과 유클리드 호제법, ⁋명제 11](/ko/math/number_theory/euclidean_algorithm#prop11)에 의하여 $n' \mid (x - x_0)$와 동치이다. 즉 해 전체는 $x_0 + n'k$이다. 이 중 두 해 $x_0 + n'k$, $x_0 + n'l$이 법 $n = gn'$에 대해 합동인 것은 $g \mid (k-l)$인 것과 동치이므로, 서로 다른 residue class는 $k = 0, 1, \dots, g-1$로 정확히 $g$개이다.
:::

[정리 5](#thm5)의 해가 $g$개라는 것은 법 $n$에서 센 것이다. 법 $n/g$에서 보면 해는 단 하나의 class $x_0 \bmod (n/g)$이며, 이것이 [명제 3](#prop3)에서 법이 $n/g$로 줄어드는 이유와 같다.

::: 따름정리 6 (모듈러 역원)
정수 $a$와 양의 정수 $n$에 대하여 $ax \equiv 1 \pmod{n}$이 해를 가질 필요충분조건은 $\gcd(a, n) = 1$이다. 이때 해는 법 $n$에 대해 유일하며, 이를 $a$의 *모듈러 역원<sub>modular inverse</sub>*이라 하고 $a^{-1} \bmod n$으로 적는다. 따라서 $\mathbb{Z}/n\mathbb{Z}$에서 $[a]$가 곱셈 역원을 갖는 것은 $\gcd(a,n)=1$일 때, 그리고 그 경우에 한한다.
:::

::: 증명
[정리 5](#thm5)에서 $b = 1$로 두면 $g \mid 1$, 곧 $g = 1$일 때 해가 존재하고 그 개수는 $g = 1$이다.
:::

특히 $n = p$가 prime이면 $0$이 아닌 모든 class가 역원을 가지므로 $\mathbb{Z}/p\mathbb{Z}$는 체이다. 역원의 구체적 계산에는 [§나눗셈과 유클리드 호제법, ⁋예시 10](/ko/math/number_theory/euclidean_algorithm#ex10)처럼 유클리드 호제법을 거꾸로 푸는 방법을 쓴다. 가령 $7^{-1} \bmod 50$을 구하려면 $50 = 7 \cdot 7 + 1$에서 $1 = 50 - 7\cdot 7$이므로 $7 \cdot (-7) \equiv 1 \pmod{50}$이고, $7^{-1} \equiv -7 \equiv 43 \pmod{50}$이다.

::: 예시 7
$14x \equiv 30 \pmod{100}$을 푼다. $\gcd(14, 100) = 2$이고 $2 \mid 30$이므로 해가 존재하고 법 $100$에서 $2$개이다. 양변과 법을 $2$로 나누면 $7x \equiv 15 \pmod{50}$인데, 이 변형은 [명제 3](#prop3)과 같은 논증으로 동치가 보장된다. $7^{-1} \equiv 43 \pmod{50}$이므로 $x \equiv 15 \cdot 43 = 645 \equiv 45 \pmod{50}$이다. 법 $100$으로는 $x \equiv 45, 95 \pmod{100}$이다. 확인하면 $14 \cdot 45 = 630 \equiv 30$, $14 \cdot 95 = 1330 \equiv 30 \pmod{100}$이다. 법을 $100$으로 둔 채 양변을 $2$로 나누어 $7x \equiv 15 \pmod{100}$으로 쓰면 해 $x \equiv 45$ 하나만 얻어 $95$를 놓친다.
:::

## 중국인의 나머지 정리

연립합동식에서 서로 다른 법에 대한 조건을 한꺼번에 만족하는 정수를 구하는 것이 중국인의 나머지 정리의 문제이다. 법이 서로소이면 연립합동식은 언제나 해를 갖고, 해는 법들의 곱에 대해 유일하다.

::: 정리 8 (중국인의 나머지 정리)
$n_1, \dots, n_k$가 쌍마다 서로소인 양의 정수이고 $N = n_1 n_2 \cdots n_k$라 하자. 임의의 정수 $a_1, \dots, a_k$에 대해 연립합동식

$$x \equiv a_1 \pmod{n_1}, \quad \dots, \quad x \equiv a_k \pmod{n_k}$$

은 해를 가지며, 해는 법 $N$에 대해 유일하다. 따라서 대응 $\mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/n_1\mathbb{Z} \times \cdots \times \mathbb{Z}/n_k\mathbb{Z}$, $[x] \mapsto ([x], \dots, [x])$는 ring isomorphism이다.
:::

::: 증명
존재를 보인다. 각 $i$에 대해 $N_i = N/n_i$라 두면, $N_i$는 $n_i$와 다른 $n_j$들의 곱이고 이들은 각각 $n_i$와 서로소이다. 곱이 $n_i$와 서로소임은 [§나눗셈과 유클리드 호제법, ⁋따름정리 9](/ko/math/number_theory/euclidean_algorithm#cor9)에 의하여 $1 = n_i u_j + n_j v_j$ ($j \ne i$)를 모두 곱하면 $1 = n_i(\cdots) + N_i \prod_{j \ne i} v_j$로 쓰이는 데서 따른다. 따라서 $\gcd(N_i, n_i) = 1$이고, [따름정리 6](#cor6)에 의하여 $N_i y_i \equiv 1 \pmod{n_i}$인 정수 $y_i$가 있다. 이제

$$x_0 = a_1 N_1 y_1 + a_2 N_2 y_2 + \cdots + a_k N_k y_k$$

라 두자. $j \ne i$이면 $n_i \mid N_j$이므로 $a_j N_j y_j \equiv 0 \pmod{n_i}$이고, $x_0 \equiv a_i N_i y_i \equiv a_i \pmod{n_i}$이다. 따라서 $x_0$는 모든 합동식을 만족한다.

유일성을 보인다. $x, x'$가 모두 해이면 모든 $i$에 대해 $n_i \mid (x - x')$이다. $m = x - x'$라 하자. $k$에 대한 귀납법으로 $N \mid m$을 보인다. $k = 1$은 자명하다. $n_1 \cdots n_{k-1} \mid m$이라 가정하고 $m = n_1 \cdots n_{k-1} t$라 쓰자. 위와 같이 $n_1 \cdots n_{k-1}$은 $n_k$와 서로소이고 $n_k \mid m$이므로 [§나눗셈과 유클리드 호제법, ⁋명제 11](/ko/math/number_theory/euclidean_algorithm#prop11)에 의하여 $n_k \mid t$이다. 따라서 $N \mid m$이다.

마지막으로 동형 주장은, 이 대응이 [명제 2](#prop2)에 의해 환 준동형으로 잘 정의되고, 방금 보인 존재와 유일성이 각각 전사성과 단사성이므로 따른다.
:::

증명의 존재 부분은 해를 구성하는 공식을 준다. 해는 $x_0 \bmod N$이다.

::: 예시 9
$x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$, $x \equiv 2 \pmod 7$을 푼다. $N = 105$이고 $N_1 = 35$, $N_2 = 21$, $N_3 = 15$이다. $35 \equiv 2 \pmod 3$이므로 $y_1 = 2$ ($2 \cdot 2 = 4 \equiv 1$), $21 \equiv 1 \pmod 5$이므로 $y_2 = 1$, $15 \equiv 1 \pmod 7$이므로 $y_3 = 1$이다. 따라서

$$x_0 = 2 \cdot 35 \cdot 2 + 3 \cdot 21 \cdot 1 + 2 \cdot 15 \cdot 1 = 140 + 63 + 30 = 233 \equiv 23 \pmod{105}$$

이다. $23 = 3 \cdot 7 + 2 = 4 \cdot 5 + 3 = 7 \cdot 3 + 2$이므로 세 조건을 모두 만족한다. 법이 작을 때는 공식 대신 순차적으로 푸는 편이 빠르다. 첫 조건에서 $x = 2 + 3s$로 두고 둘째에 넣으면 $3s \equiv 1 \pmod 5$이므로 $s \equiv 2 \pmod 5$, 따라서 $x \equiv 8 \pmod{15}$이다. 셋째에 넣기 위해 $x = 8 + 15t$로 두면 $8 + 15 t \equiv 1 + t \equiv 2 \pmod 7$에서 $t \equiv 1$이고 $x \equiv 23 \pmod{105}$이다.
:::

서로소 조건은 필요하다. $x \equiv 1 \pmod 4$와 $x \equiv 2 \pmod 6$을 동시에 만족하는 정수는 없다. 첫째 조건은 $x$가 홀수임을, 둘째 조건은 $x$가 짝수임을 뜻하기 때문이다. 한편 $x \equiv 1 \pmod 4$와 $x \equiv 3 \pmod 6$은 $x = 9$가 해이지만, 이 해는 법 $4 \cdot 6 = 24$가 아니라 $12$에 대해서만 유일하다($9$와 $21$이 모두 해이다). 서로소가 아닌 법에서 무엇이 일어나는지를 정확히 말하는 것이 다음 명제이다.

## 서로소가 아닌 법

::: 명제 10
양의 정수 $m, n$과 정수 $a, b$에 대해 $g = \gcd(m, n)$이라 하자. 연립합동식 $x \equiv a \pmod m$, $x \equiv b \pmod n$이 해를 가질 필요충분조건은 $g \mid (a - b)$이다. 해가 존재하면 해는 법 $\lcm(m, n) = mn/g$에 대해 유일하다.
:::

::: 증명
첫째 합동식의 해는 $x = a + mt$ ($t \in \mathbb{Z}$)이다. 이것이 둘째 합동식을 만족할 조건은 $mt \equiv b - a \pmod n$이고, 이는 $t$에 대한 일차 합동식이다. $\gcd(m, n) = g$이므로 [정리 5](#thm5)의 (a)에 의하여 해 $t$가 존재할 필요충분조건은 $g \mid (b-a)$이다. 해가 존재하면 (b)에 의하여 $t$는 법 $n/g$에 대해 유일하다. $t$가 $t_0 + (n/g)s$로 변할 때 $x = a + mt$는 $a + mt_0 + (mn/g)s$로 변하므로 $x$는 법 $mn/g$에 대해 유일하다.
:::

[명제 10](#prop10)은 중국인의 나머지 정리의 일반화이다. $g = 1$이면 조건 $g \mid (a-b)$가 항상 성립하고 [§나눗셈과 유클리드 호제법, ⁋명제 13](/ko/math/number_theory/euclidean_algorithm#prop13)에 의하여 $\lcm(m, n) = mn$이다. 위의 반례에서 $x \equiv 1 \pmod 4$, $x \equiv 2 \pmod 6$은 $g = 2 \nmid 1$이므로 해가 없고, $x \equiv 1 \pmod 4$, $x \equiv 3 \pmod 6$은 $g = 2 \mid 2$이고 $\lcm = 12$이므로 해가 법 $12$에 대해 유일하다.

::: 예시 11
$x \equiv 2 \pmod{12}$, $x \equiv 8 \pmod{18}$을 푼다. $\gcd(12, 18) = 6$이고 $6 \mid (8 - 2) = 6$이므로 해가 존재하며 법 $\lcm(12, 18) = 36$에 대해 유일하다. $x = 2 + 12t$를 둘째 조건에 넣으면 $12 t \equiv 6 \pmod{18}$이다. $\gcd(12, 18) = 6$으로 양변과 법을 나누면 $2t \equiv 1 \pmod 3$이고 $t \equiv 2 \pmod 3$이다. 따라서 $x = 2 + 12 \cdot 2 = 26$이고 해는 $x \equiv 26 \pmod{36}$이다. $26 = 2 \cdot 12 + 2 = 18 + 8$이므로 두 조건을 만족한다.
:::

법이 셋 이상일 때에도 해의 존재 조건은 두 법씩 짝지은 조건으로 충분하다.

::: 명제 12
양의 정수 $n_1, \dots, n_k$와 정수 $a_1, \dots, a_k$에 대해 연립합동식 $x \equiv a_i \pmod{n_i}$ ($1 \le i \le k$)이 해를 가질 필요충분조건은 모든 $i, j$에 대해 $\gcd(n_i, n_j) \mid (a_i - a_j)$인 것이다. 해가 존재하면 해는 법 $L = \lcm(n_1, \dots, n_k)$에 대해 유일하다.
:::

::: 증명
필요성은 [명제 10](#prop10)의 필요성 부분과 같다. 해 $x$에 대해 $\gcd(n_i, n_j)$는 $x - a_i$와 $x - a_j$를 모두 나누므로 [§나눗셈과 유클리드 호제법, ⁋명제 2](/ko/math/number_theory/euclidean_algorithm#prop2)의 (2)에 의하여 그 차 $a_j - a_i$도 나눈다.

충분성을 보인다. 각 소수 $p$에 대해 $e_i(p)$를 $n_i$의 소인수분해에서 $p$의 지수라 하자. 소인수분해의 존재와 유일성은 [§소수와 산술의 기본정리, ⁋정리 4](/ko/math/number_theory/primes#thm4)에 의한다. 합동식 $x \equiv a_i \pmod{n_i}$는 $n_i$를 나누는 각 소수 $p$에 대한 $x \equiv a_i \pmod{p^{e_i(p)}}$들을 모두 만족하는 것과 동치이다. 소수 $p$ 하나를 고정하고, $p$가 나누는 법 중 지수가 최대인 $n_{i_0}$를 택한다. 임의의 $i$에 대해 $e = \min(e_i(p), e_{i_0}(p)) = e_i(p)$이므로 가정 $\gcd(n_i, n_{i_0}) \mid (a_i - a_{i_0})$에서 $p^{e_i(p)} \mid (a_i - a_{i_0})$를 얻는다. 따라서 $x \equiv a_{i_0} \pmod{p^{e_{i_0}(p)}}$이면 $x \equiv a_{i_0} \equiv a_i \pmod{p^{e_i(p)}}$이다. 즉 소수 $p$에 대한 조건은 $x \equiv a_{i_0} \pmod{p^{e_{i_0}(p)}}$ 하나로 줄어든다. 모든 소수에 대해 이렇게 줄이면 법이 서로 다른 소수의 거듭제곱인 연립합동식이 되고, 그 법들은 쌍마다 서로소이다. [정리 8](#thm8)에 의하여 이 연립합동식은 해를 가지며 그 해는 법 $\prod_p p^{\max_i e_i(p)} = L$에 대해 유일하다. 줄이기 전의 연립합동식과 동치이므로 원래 연립합동식도 같은 해를 갖는다.
:::
