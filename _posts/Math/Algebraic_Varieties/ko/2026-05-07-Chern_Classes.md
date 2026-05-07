---
title: "Chern Classes"
permalink: /ko/math/algebraic_varieties/chern_classes
excerpt: "벡터다발의 Chern classes와 그 성질들"
categories: [Math / Algebraic Varieties]
sidebar: { nav: "algebraic_varieties-ko" }
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 22
---

벡터다발은 대수기하학에서 기하적 대상을 다루는 데 핵심적인 도구이다. 그러나 주어진 벡터다발이 얼마나 "뒤틀려" 있는지, 즉 자명다발에서 얼마나 벗어나 있는지를 측정하는 전역적인 불변량이 필요하다. Chern class는 바로 이러한 특성류 중 하나로, complex vector bundle에 대해 정의되는 위상적·기하적 불변량이다. 우리는 이 글에서 Chern class를 공리적으로 정의하고, 이를 계산하는 데 필수적인 splitting principle을 소개한 뒤, 여러 구체적인 예시를 통해 그 성질을 살펳을 것이다.

## 공리적 정의

우선 Chern class를 다음의 공리들로부터 정의한다. 이는 Hirzebruch가 제시한 공리적 접근법이다. 모든 논의는 적당한 베이스 공간 $X$ 위의 complex vector bundle에 대해 이루어지며, cohomology는 singular cohomology $H^{\\bullet}(X, \\mathbb{Z})$를 사용한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 각 complex vector bundle $E \\to X$에 대해 $c_i(E) \\in H^{2i}(X, \\mathbb{Z})$가 주어지며, 이들을 *Chern classes*라고 부른다. 이들은 다음의 공리들을 만족한다.

1. *(자연성, naturality)* 연속사상 $f: Y \\to X$에 대하여

   $$c_i(f^{\\ast} E) = f^{\\ast} c_i(E)$$

   이 성립한다. 여기서 $f^{\\ast}$은 cohomology에서의 pullback이다.

2. *(Whitney sum formula)* 두 vector bundle $E, F$에 대하여,

   $$c(E \\oplus F) = c(E) \\smile c(F)$$

   이 성립한다. 여기서 $c(E) = \\sum_{i \\ge 0} c_i(E)$는 *total Chern class*이며, 우변의 곱은 cup product이다.

3. *(정규화, normalization)* $L \\to X$가 line bundle일 때,

   $$c(L) = 1 + c_1(L)$$

   이고, 특히 $X = \\mathbb{P}^n$ 위의 tautological line bundle $\\mathcal{O}(-1)$에 대해 $c_1(\\mathcal{O}(1))$은 $H^2(\\mathbb{P}^n, \\mathbb{Z})$의 생성원을 준다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위의 공리를 만족하는 Chern class는 유일하게 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

유일성은 splitting principle을 통해 line bundle들의 직합에 대한 경우로 환원되고, 이 경우 공리 3과 자연성으로부터 모든 Chern class가 결정되기 때문에 자명하다. 존재성은 projective bundle을 이용한 명시적 구성을 통해 확인할 수 있다. 자세한 내용은 생략한다.

</details>

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Rank $r$인 vector bundle $E$에 대해, *Chern polynomial* $c_t(E)$를 다음과 같이 정의한다.

$$c_t(E) = 1 + c_1(E)t + c_2(E)t^2 + \\cdots + c_r(E)t^r$$

이는 공식변수 $t$에 대한 다항식이다.

</div>

## 선다발의 1차 첸류

Line bundle의 첫 번째 Chern class $c_1(L)$은 divisor와 밀접한 관계가 있다. 이는 Chern class의 기하적 의미를 이해하는 데 중요한 단서를 제공한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $X$가 smooth variety이고, $L \\to X$가 line bundle이라 하자. 이때 $L$의 meromorphic section $s$가 주어지면, 이로부터 divisor $\\operatorname{div}(s)$가 정의되며,

$$c_1(L) = [\\operatorname{div}(s)] \\in A^1(X)$$

이 성립한다. 특히, $L = \\mathcal{O}_X(D)$로 표현될 때 $c_1(L) = [D]$이다.

</div>

이 명제에 대한 증명은 exponential exact sequence $0 \\to \\mathbb{Z} \\to \\mathcal{O}_X \\to \\mathcal{O}_X^{\\times} \\to 0$로부터 유도되는 connecting homomorphism $H^1(X, \\mathcal{O}_X^{\\times}) \\to H^2(X, \\mathbb{Z})$를 통해 이루어진다. Line bundle은 $\\mathcal{O}_X^{\\times}$의 cocycle으로 주어지며, 이에 대응하는 cohomology class가 바로 $c_1(L)$이다. 동시에 divisor $D$는 $A^1(X)$의 원소로, 이 두 가지 관점이 Poincaré duality를 통해 일치함을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $L, M$이 같은 베이스 $X$ 위의 line bundle들이라 하자. 그러면 다음이 성립한다.

1. $c_1(L \\otimes M) = c_1(L) + c_1(M)$
2. $c_1(L^{\\vee}) = -c_1(L)$

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 4에 의해 $L = \\mathcal{O}_X(D)$, $M = \\mathcal{O}_X(E)$로 표현할 수 있으며, 이때 $L \\otimes M = \\mathcal{O}_X(D+E)$이다. 따라서

$$c_1(L \\otimes M) = [D+E] = [D] + [E] = c_1(L) + c_1(M)$$

이 성립한다. 둘째로, $L \\otimes L^\\vee \\cong \\mathcal{H}om(L,L) \\cong \\mathcal{O}_X$이고 이는 자명하게 global section을 가지므로 $c_1(L \\otimes L^{\\vee}) = c_1(\\mathcal{O}_X) = 0$이다. 따라서 $c_1(L^{\\vee}) = -c_1(L)$이다.

</details>

## Splitting principle

일반적으로 vector bundle은 line bundle들의 직합으로 분핵되지 않는다. 그러나 다음의 splitting principle을 이용하면, 임의의 vector bundle에 대한 Chern class의 계산을 line bundle의 경우로 환원할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** (Splitting principle)</ins> $E \\to X$를 rank $r$인 vector bundle이라 하자. 그러면 어떤 연속사상 $f: Y \\to X$가 존재하여 다음 두 조건을 만족한다.

1. $f^{\\ast}: H^{\\ast}(X, \\mathbb{Z}) \\to H^{\\ast}(Y, \\mathbb{Z})$는 단사이다.
2. $f^{\\ast} E$는 line bundle $L_1, L_2, \\ldots, L_r$들의 직합 $L_1 \\oplus \\cdots \\oplus L_r$으로 분해된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$f: Y = \\mathbb{P}(E) \\to X$를 projectivization으로 정의한다. $\\mathbb{P}(E)$ 위에는 tautological line bundle $S \\subset \\pi^{\\ast} E$가 존재하며, quotient bundle $Q = (\\pi^{\\ast} E)/S$는 rank $r-1$이다. Leray-Hirsch theorem에 의해 $\\pi^{\\ast}: H^{\\ast}(X) \\to H^{\\ast}(\\mathbb{P}(E))$는 단사이고, $H^{\\ast}(\\mathbb{P}(E))$는 $1, \\xi, \\xi^2, \\ldots, \\xi^{r-1}$을 basis로 하는 자유 $H^{\\ast}(X)$-module이다. 여기서 $\\xi = c_1(\\mathcal{O}_E(1))$이다. 이제 $Q$에 대해 같은 과정을 반복하면, 적당한 $Y \\to X$를 얻어 $f^{\\ast} E$가 line bundle들의 직합으로 분해됨을 확인할 수 있다.

</details>

Splitting principle의 핵심적인 의미는 다음과 같다. Symmetric polynomial으로 표현되는 어떤 식이 line bundle들의 직합에 대해 성립하면, 그 식은 임의의 vector bundle에 대해서도 성립한다. 왜냐하면 $f^{\\ast}$이 단사이므로 $Y$에서의 등식이 $X$에서도 등식이 되기 때문이다.

## 첸 근과 첸 문자

Splitting principle을 바탕으로, 임의의 vector bundle을 마치 line bundle들의 직합인 것처럼 다룰 수 있다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $E$를 rank $r$ vector bundle이라 하고, splitting principle에 의해 $f^{\\ast} E = L_1 \\oplus \\cdots \\oplus L_r$로 분해되었다 하자. 이때 $x_i = c_1(L_i) \\in H^2(Y)$를 $E$의 *Chern roots*라고 부른다. Formally, $E$의 *Chern polynomial*은

$$c_t(E) = \\prod_{i=1}^r (1 + x_i t)$$

으로 주어지며, 이 전개에서 $c_k(E)$는 $x_1, \\ldots, x_r$의 $k$-차 elementary symmetric polynomial이 된다.

또한 $E$의 *Chern character* $ch(E)$를 다음과 같이 정의한다.

$$ch(E) = \\sum_{i=1}^r e^{x_i} = r + c_1(E) + \\frac{c_1(E)^2 - 2c_2(E)}{2} + \\cdots$$

이는 $H^{\\ast}(X, \\mathbb{Q})$의 원소이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Chern character는 다음의 성질을 만족한다.

1. $ch(E \\oplus F) = ch(E) + ch(F)$
2. $ch(E \\otimes F) = ch(E) \\cup ch(F)$

따라서 $ch: K^0(X) \\to H^{\\mathrm{even}}(X, \\mathbb{Q})$는 ring homomorphism을 유도한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Splitting principle에 의해 $E = \\bigoplus L_i$, $F = \\bigoplus M_j$로 가정할 수 있다. 이때

$$ch(E \\oplus F) = \\sum_i e^{x_i} + \\sum_j e^{y_j} = ch(E) + ch(F)$$

이고,

$$ch(E \\otimes F) = ch\\bigg(\\bigoplus_{i,j} L_i \\otimes M_j\\bigg) = \\sum_{i,j} e^{x_i + y_j} = \\bigg(\\sum_i e^{x_i}\\bigg)\\bigg(\\sum_j e^{y_j}\\bigg) = ch(E) \\cup ch(F)$$

이므로 성립한다.

</details>

## Projective bundle formula

Vector bundle $E \\to X$의 projectivization $\\pi: \\mathbb{P}(E) \\to X$는 Chern class 이론에서 중요한 역할을 한다. 특히 $\\mathbb{P}(E)$의 cohomology는 다음의 projective bundle formula로 완전히 결정된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> (Projective bundle formula) $\\pi: \\mathbb{P}(E) \\to X$를 rank $r$ vector bundle $E$의 projectivization이라 하고, $\\xi = c_1(\\mathcal{O}_E(1)) \\in H^2(\\mathbb{P}(E))$라 하자. 그러면

$$H^{\\ast}(\\mathbb{P}(E)) \\cong H^{\\ast}(X)[\\xi] / (\\xi^r + \\pi^{\\ast}c_1(E)\\xi^{r-1} + \\cdots + \\pi^{\\ast}c_r(E))$$

으로 주어지며, 이는 $H^{\\ast}(X)$-algebra의 isomorphism이다. 특히 $H^{\\ast}(\\mathbb{P}(E))$는 $H^{\\ast}(X)$-module로서 $\\{1, \\xi, \\xi^2, \\ldots, \\xi^{r-1}}$을 basis로 하는 자유模이다.

</div>

이 명제로부터 Chern class를 projective bundle의 cohomology ring의 관계식으로 정의할 수도 있다. 위의 식에서 $\\xi$에 대한 $r$-차 관계식의 계수가 바로 $c_i(E)$가 된다.

## 예시: $\\mathbb{P}^n$의 첸 클래스

Projective space $\\mathbb{P}^n$의 tangent bundle $T_{\\mathbb{P}^n}$에 대해, Euler exact sequence를 이용하여 Chern class를 계산할 수 있다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $\\mathbb{P}^n$ 위의 Euler exact sequence는

$$0 \\longrightarrow \\mathcal{O}_{\\mathbb{P}^n} \\longrightarrow \\mathcal{O}_{\\mathbb{P}^n}(1)^{\\oplus (n+1)} \\longrightarrow T_{\\mathbb{P}^n} \\longrightarrow 0$$

이다. Whitney sum formula에 의해

$$c(T_{\\mathbb{P}^n}) = c(\\mathcal{O}_{\\mathbb{P}^n}(1)^{\\oplus (n+1)}) = c(\\mathcal{O}_{\\mathbb{P}^n}(1))^{n+1}$$

이고, $H = c_1(\\mathcal{O}_{\\mathbb{P}^n}(1))$이 hyperplane class임으로부터

$$c(T_{\\mathbb{P}^n}) = (1 + H)^{n+1}$$

를 얻는다. 따라서

$$c_k(T_{\\mathbb{P}^n}) = \\binom{n+1}{k} H^k$$

이다. 특히 top Chern class는 $c_n(T_{\\mathbb{P}^n}) = (n+1)H^n$이며, $\\deg(H^n) = 1$이므로

$$\\int_{\\mathbb{P}^n} c_n(T_{\\mathbb{P}^n}) = n+1$$

이다.

</div>

## 예시: $\\mathbb{P}^1 \\times \\mathbb{P}^1$의 첸 클래스

두 개의 projective line의 곱에 대해 계산해 보자. $\\pi_1, \\pi_2$를 각각 첫 번째, 두 번째 인자로의 사영이라 하고, $\\mathcal{O}(a,b) = \\pi_1^{\\ast}\\mathcal{O}(a) \\otimes \\pi_2^{\\ast}\\mathcal{O}(b)$로 정의한다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $\\mathbb{P}^1 \\times \\mathbb{P}^1$의 tangent bundle은

$$T_{\\mathbb{P}^1 \\times \\mathbb{P}^1} = \\pi_1^{\\ast} T_{\\mathbb{P}^1} \\oplus \\pi_2^{\\ast} T_{\\mathbb{P}^1}$$

이다. 각각의 $T_{\\mathbb{P}^1} = \\mathcal{O}(2)$이므로,

$$c(T_{\\mathbb{P}^1 \\times \\mathbb{P}^1}) = c(\\pi_1^{\\ast}\\mathcal{O}(2)) \\cdot c(\\pi_2^{\\ast}\\mathcal{O}(2))$$

이다. $H_1 = c_1(\\pi_1^{\\ast}\\mathcal{O}(1))$, $H_2 = c_1(\\pi_2^{\\ast}\\mathcal{O}(1))$로 두면,

$$c(T_{\\mathbb{P}^1 \\times \\mathbb{P}^1}) = (1 + 2H_1)(1 + 2H_2) = 1 + 2(H_1 + H_2) + 4H_1H_2$$

이다. 따라서

$$c_1(T_{\\mathbb{P}^1 \\times \\mathbb{P}^1}) = 2(H_1 + H_2), \\quad c_2(T_{\\mathbb{P}^1 \\times \\mathbb{P}^1}) = 4H_1H_2$$

이고, $\\deg(H_1H_2) = 1$이므로 $\\int_{\\mathbb{P}^1 \\times \\mathbb{P}^1} c_2 = 4$이다. 이는 $\\mathbb{P}^1 \\times \\mathbb{P}^1$의 topological Euler characteristic $\\chi_{\\mathrm{top}} = 4$와 일치함을 확인할 수 있다.

</div>

## 접다발의 첸 클래스와 오일러 지표

Chern class의 가장 중요한 응용 중 하나는 compact complex manifold의 topological Euler characteristic을 계산하는 것이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> (Poincaré-Hopf) $X$를 $n$-차원 compact complex manifold라 하자. 그러면

$$\\chi_{\\mathrm{top}}(X) = \\int_X c_n(T_X)$$

이 성립한다. 여기서 $\\chi_{\\mathrm{top}}(X) = \\sum_{i=0}^{2n} (-1)^i \\dim H^i(X, \\mathbb{Q})$는 topological Euler characteristic이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Tangent bundle $T_X$의 section $v: X \\to T_X$를 생각하자. 일반적으로 $v$는 isolated zeros만을 가지며, 각 zero $p$에서의 index $\\operatorname{ind}_p(v)$를 정의할 수 있다. Euler class $e(T_X)$는 zero locus의 Poincaré dual로 주어지며, 특히 complex vector bundle에 대해서는 $e(T_X) = c_n(T_X)$이다. Poincaré-Hopf index theorem에 의해

$$\\sum_{p \\in v^{-1}(0)} \\operatorname{ind}_p(v) = \\chi_{\\mathrm{top}}(X)$$

이고, 동시에 이 합은 $\\int_X c_n(T_X)$으로 주어진다.

</details>

예시 10에서 확인했듯이, $\\mathbb{P}^n$에 대해

$$\\int_{\\mathbb{P}^n} c_n(T_{\\mathbb{P}^n}) = n+1$$

이며 이는 $\\mathbb{P}^n$의 Euler characteristic $\\chi_{\\mathrm{top}}(\\mathbb{P}^n) = n+1$과 정확히 일치한다. 마찬가지로 예시 11에서도 $\\mathbb{P}^1 \\times \\mathbb{P}^1$의 top Chern class를 적분한 값이 4로, 이 곡면의 Euler characteristic과 일치함을 확인하였다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Ful]** W. Fulton, *Intersection theory*, Springer, 1998.

**[BT]** R. Bott and L. Tu, *Differential forms in algebraic topology*, Springer, 1982.
