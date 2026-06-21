---
title: "수열의 극한"
description: "수열의 수렴을 ε-N으로 정의하고, 유계성·극한 법칙·조임정리·비율판정을 정리한다. 표준 극한과 자연상수 e, 단조수렴정리, 부분수열을 다룬다."
excerpt: "수열의 수렴, 극한 법칙, 표준 극한과 e, 단조수렴"

categories: [Math / Calculus]
permalink: /ko/math/calculus/sequences
sidebar: 
    nav: "calculus-ko"

date: 2026-06-21
weight: 3

published: false
---

우리는 본격적으로 미적분학을 시작하기 전에 우선 수열의 극한을 정의한다. 여기서 *수열<sub>sequence</sub>* $$(a_n)$$이란 자연수에 실수를 대응시키는 함수, 즉 $$a : \mathbb{N} \to \mathbb{R}$$을 그 값들 $$a_1, a_2, a_3, \ldots$$의 나열로 본 것이다. 함수의 극한 ([§함수와 극한](/ko/math/calculus/functions_and_limits))에서 우리는 이미 $$x \to \infty$$일 때 함수가 어떻게 행동하는지를 다루었는데, 수열의 극한은 그 이산적 버전, 즉 변수가 자연수만 취하는 경우에서 $$n \to \infty$$로만 가는 경우로 생각할 수 있다. 

## 수열의 수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 실수열 $$(a_n)_{n=1}^\infty$$와 실수 $$L$$에 대해, 임의의 $$\varepsilon > 0$$에 대하여 어떤 자연수 $$N$$이 존재하여

$$n > N \implies \lvert a_n - L \rvert < \varepsilon$$

이 성립할 때, $$L$$을 $$n \to \infty$$일 때 $$a_n$$의 *극한<sub>limit</sub>*이라 하고 $$\displaystyle\lim_{n\to\infty} a_n = L$$로 적는다.

</div>

이 정의는 [§함수와 수열의 극한, ⁋정의 14](/ko/math/calculus/functions_and_limits#def14)를 거의 그대로 가져온 것으로, 수열은 그 정의에 의해 변수가 자연수뿐이고 한 방향($$+\infty$$)으로만 가므로, 수열의 극한을 정의하는 거의 유일한 방법은 이것 뿐이다. 약간의 변종은 수열이 무한대로 발산하는 것으로, 이는 [§함수와 수열의 극한, ⁋정의 13](/ko/math/calculus/functions_and_limits#def13)을 약간 변형하면 어떻게 정의해야 할지 자명하다. 그러나 물론, 특정한 값으로 수렴하는 수열과 무한대로 발산하는 수열이 아닌 다른 종류의 수열도 존재한다 ([예시 13](#ex13))

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 이 예시에서 우리는 $$a_n=1/n$$이 $$0$$으로 수렴하는 것과, $$a_n=n$$이 무한대로 발산하는 것을 보인다. 우선 첫째 극한의 경우, 임의의 $$\varepsilon > 0$$에 대해 $$N > \frac{1}{\varepsilon}$$인 자연수 $$N$$을 택하면, $$n > N$$일 때 $$\frac{1}{n} < \frac{1}{N} < \varepsilon$$이므로 $$\bigl\lvert \frac{1}{n}-0\bigr\rvert < \varepsilon$$이다. 한편 수열 $$a_n = n$$은 발산한다. 이를 확인하기 위해서는 임의의 실수 $$M$$에 대해 $$N = \lfloor M\rfloor$$로 잡으면 $$n > N$$일 때 $$a_n = n > M$$임을 확인하면 된다. 

</div>

한편, 다음 명제 또한 [§함수와 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5)의 증명과 동일한 방식으로 진행하면 충분하다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (수열의 극한법칙)**</ins> $$\displaystyle\lim_{n\to\infty} a_n = L$$, $$\displaystyle\lim_{n\to\infty} b_n = M$$이라 하자. 그러면

1. $$\displaystyle\lim_{n\to\infty} \bigl(a_n + b_n\bigr) = L + M$$,
2. 임의의 상수 $$c$$에 대해 $$\displaystyle\lim_{n\to\infty} c\,a_n = cL$$,
3. $$\displaystyle\lim_{n\to\infty} a_n b_n = LM$$,
4. $$M \neq 0$$이고 모든 $$n$$에 대해 $$b_n \neq 0$$이면 $$\displaystyle\lim_{n\to\infty} \frac{a_n}{b_n} = \frac{L}{M}$$

이 성립한다.

</div>

## 극한의 성질

수열 $$(a_n)$$에 대해 모든 $$n$$에서 $$\lvert a_n\rvert \leq M$$인 양수 $$M$$이 존재하면 $$(a_n)$$을 *유계<sub>bounded</sub>*라 한다. 수렴하는 수열은 앞의 유한개의 항을 제외하면 항상 수렴하는 점 근처로 모이므로 유계이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 수렴하는 수열은 유계이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$a_n \to L$$이면 $$\varepsilon = 1$$에 대응하는 $$N$$을 잡았을 때 $$n \geq N$$에서 $$\lvert a_n\rvert \leq \lvert L\rvert + 1$$이다. 나머지 유한개 항을 포함하여 $$M = \max\{\lvert a_1\rvert, \ldots, \lvert a_{N-1}\rvert, \lvert L\rvert + 1\}$$로 두면 모든 $$n$$에서 $$\lvert a_n\rvert \leq M$$이다.

</details>

수렴하는 수열의 기본 성질들 또한 [명제 3](#prop3)에서 그러했듯 함수의 극한에서의 증명을 그대로 베껴와서 얻어진다. 가령 다음은 [§함수와 극한, ⁋명제 8](/ko/math/calculus/functions_and_limits#prop8)의 수열 버전이다.


<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (조임정리)**</ins> 충분히 큰 모든 $$n$$에서 $$a_n \leq c_n \leq b_n$$이고 $$a_n \to L$$, $$b_n \to L$$이면 $$c_n \to L$$이다.

</div>

그럼 다음의 간단하지만 유용한 결과를 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (비율 판정)**</ins> $$a_n > 0$$이고 $$a_{n+1}/a_n \to L < 1$$이면 $$a_n \to 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L < r < 1$$인 $$r$$를 고르면, 충분히 큰 $$n \geq N$$에서 $$a_{n+1}/a_n < r$$이므로 $$a_{N+k} < r^k a_N$$이다. $$0 < r < 1$$이라 $$r^k \to 0$$이고, 조임정리로 $$a_n \to 0$$이다.

</details>

이와 비슷하게, 실제 계산에서 많이 쓰이는 결과들을 다음 예시로 모아둔다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 다음은 수열의 극한의 기본 예시들이다.

1. $$\lvert r\rvert < 1$$이면 $$r^n \to 0$$, $$r = 1$$이면 $$\to 1$$, $$\lvert r\rvert > 1$$이면 발산한다.
2. $$p > 0$$에 대해 $$1/n^p \to 0$$, 그리고 $$n^{1/n} \to 1$$, $$p^{1/n} \to 1$$ ($$p > 0$$).
3. 다항식의 비는 최고차항이 지배하여

   $$\frac{a_k n^k + \cdots}{b_m n^m + \cdots}$$

   이 $$k < m$$이면 $$0$$, $$k = m$$이면 $$a_k/b_m$$, $$k > m$$이면 발산한다.

4. 지수는 거듭제곱을, 계승은 지수를 압도한다: $$r > 1$$, $$p > 0$$에 대해 $$n^p/r^n \to 0$$이고 $$r^n/n! \to 0$$이다.

**1의 증명.** $$r = 1$$이면 $$r^n = 1 \to 1$$이다. $$\lvert r\rvert < 1$$이면 임의의 $$\varepsilon > 0$$에 대해 $$\lvert r\rvert^n < \varepsilon$$, 즉 $$n \ln\lvert r\rvert < \ln\varepsilon$$, 곧

$$n > \frac{\ln\varepsilon}{\ln\lvert r\rvert}$$

( $$\ln\lvert r\rvert < 0$$ ) 을 만족하는 $$N$$을 잡으면 $$n > N$$일 때 $$\lvert r^n - 0\rvert = \lvert r\rvert^n < \varepsilon$$이다. $$\lvert r\rvert > 1$$이면 $$\lvert r\rvert^n \to \infty$$이므로 발산한다.

**2의 증명.** $$1/n^p$$의 경우, $$n \geq 1$$에서 $$n^p \geq n$$ ( $$p > 0$$ ) 이므로 $$0 < 1/n^p \leq 1/n \to 0$$이고, 조임정리로 $$1/n^p \to 0$$이다.

$$n^{1/n} \to 1$$의 경우, $$n^{1/n} = 1 + h_n$$ ( $$h_n \geq 0$$ ) 으로 두면 이항정리로

$$n = (1+h_n)^n \geq \binom{n}{2}h_n^2 = \frac{n(n-1)}{2}h_n^2$$

이다. 따라서 $$h_n^2 \leq 2/(n-1) \to 0$$이므로 $$h_n \to 0$$, 즉 $$n^{1/n} \to 1$$이다.

$$p^{1/n} \to 1$$의 경우, $$p \geq 1$$이면 베르누이 부등식으로 $$p = (p^{1/n})^n = (1+h_n)^n \geq 1 + nh_n$$이므로 $$h_n \leq (p-1)/n \to 0$$이다. $$0 < p < 1$$이면 $$1/p^{1/n} = (1/p)^{1/n} \to 1$$이므로 $$p^{1/n} \to 1$$이다.

**3의 증명.** 분자·분모를 $$n^{\max(k,m)}$$으로 나누면 분자·분모 모두 유한개의 $$1/n^j$$ 항과 상수항으로 이루어진다. $$1/n^j \to 0$$이므로 분자와 분모는 각각 최고차항의 계수로 수렴하고, 극한법칙 (명제 3) 에 의해 결론이 따른다.

**4의 증명.** $$n^p/r^n$$에 비율 판정 (명제 6) 을 쓰면 비가

$$\frac{(n+1)^p}{r^{n+1}}\cdot\frac{r^n}{n^p} = \frac{1}{r}\left(1+\frac{1}{n}\right)^p \to \frac{1}{r} < 1$$

이므로 $$n^p/r^n \to 0$$이다. $$r^n/n!$$의 비는 $$r/(n+1) \to 0 < 1$$이므로 같은 이유로 $$0$$이다.

</div>

## 단조수렴정리

극한값을 미리 모르더라도 수렴을 보장하는 강력한 도구가 단조수렴이다. 이것이 수열에서 극한의 *존재*를 끌어내는 첫 수단이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (단조수렴)**</ins> 위로 유계인 증가수열과 아래로 유계인 감소수열은 수렴한다. (증가수열의 극한은 그 항들의 상한이다.)

</div>

이 사실은 실수의 완비성 — 위로 유계인 집합이 상한을 갖는다는 성질 — 에 정확히 기반하며, 그 증명은 [\[해석학\] §수열의 수렴, ⁋정리 8](/ko/math/analysis/convergence_of_sequences#thm8)에서 다룬다. 단조수렴정리의 가장 유명한 응용이 자연상수의 정의이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (자연상수 $$e$$)**</ins> 수열 $$a_n = (1 + 1/n)^n$$이 증가하며 위로 유계임을 보이자.

**증가성.** $$n+1$$개의 수 $$\underbrace{1+1/n, \ldots, 1+1/n}_{n\text{개}}, \; 1$$에 AM–GM 부등식을 적용하면, 기하평균 $$[(1+1/n)^n \cdot 1]^{1/(n+1)} = a_n^{1/(n+1)}$$이 산술평균

$$\frac{n(1+1/n)+1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

보다 작거나 같다. 따라서

$$a_n \leq \left(1+\frac{1}{n+1}\right)^{n+1} = a_{n+1}$$

이다. $$n+1$$개의 수가 모두 같지 않으므로 ( $$1+1/n \neq 1$$ ) 등호가 성립하지 않아 $$a_n < a_{n+1}$$이다.

**유계성.** 이항정리로

$$a_n = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}$$

이고, 각 항은

$$\binom{n}{k}\frac{1}{n^k} = \frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k} \leq \frac{1}{k!}$$

이며, $$k! \geq 2^{k-1}$$ ( $$k \geq 1$$ ) 이므로

$$a_n \leq \sum_{k=0}^{n}\frac{1}{k!} \leq 1 + \sum_{k=1}^{\infty}\frac{1}{2^{k-1}} = 3$$

이다. 증가하고 위로 유계인 수열이므로 명제 8에 의해 수렴한다. 그 극한을 *자연상수* $$e = 2.718\ldots$$로 정의한다.

</div>

## 부분수열

수렴 여부를 분석할 때, 수열의 일부 항만 골라 뽑은 새 수열을 보는 것이 유용하다. 발산을 보일 때 특히 그러한데, 서로 다른 극한으로 가는 두 부분수열을 찾으면 원래 수열이 발산함이 곧장 따라 나온다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 수열 $$(a_n)$$과 자연수의 순증가 수열 $$n_1 < n_2 < n_3 < \cdots$$이 주어졌을 때, 새 수열 $$(a_{n_k})_{k\geq 1}$$을 $$(a_n)$$의 *부분수열<sub>subsequence</sub>*이라 한다.

</div>

지표열이 순증가하므로 $$n_k \geq k$$가 항상 성립한다. 부분수열은 원래 수열에서 "건너뛰며" 항을 고르는 것이며, 수렴하는 수열에서 어떻게 골라도 같은 극한을 얻는다는 것이 다음 명제이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (조임정리의 활용)**</ins> $$a_n = n!/n^n$$의 극한을 구하자. 모든 항이 양수이고

$$0 < \frac{n!}{n^n} = \frac{1}{n}\cdot\frac{2}{n}\cdot\frac{3}{n}\cdots\frac{n}{n} \leq \frac{1}{n}\cdot 1 \cdot 1 \cdots 1 = \frac1n$$

이다. 둘째 인수부터 마지막 인수까지는 모두 $$1$$ 이하이고 첫 인수가 $$1/n$$이기 때문이다. $$1/n \to 0$$이므로 조임정리 (명제 5) 에 의해

$$\lim_{n\to\infty} \frac{n!}{n^n} = 0$$

이다. 같은 결론을 비율 판정으로도 얻는다. 비가

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!} = \left(\frac{n}{n+1}\right)^n = \left(1 + \frac{1}{n}\right)^{-n} \to e^{-1} < 1$$

이기 때문이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$a_n \to L$$이면 모든 부분수열 $$(a_{n_k})$$도 $$L$$로 수렴한다. 역으로, 어떤 두 부분수열이 서로 다른 극한으로 수렴하면 $$(a_n)$$은 발산한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\varepsilon > 0$$에 대해 $$n \geq N$$이면 $$\lvert a_n - L\rvert < \varepsilon$$인 $$N$$을 잡자. 지표열이 순증가하므로 $$n_k \geq k$$이고, 따라서 $$k \geq N$$이면 $$n_k \geq N$$이라

$$\lvert a_{n_k} - L\rvert < \varepsilon$$

이다. 즉 $$a_{n_k} \to L$$이다. 역방향은 대우로 따른다. 만약 $$(a_n)$$이 어떤 $$L$$로 수렴한다면 방금 보인 대로 모든 부분수열이 같은 $$L$$로 수렴해야 하므로, 서로 다른 두 극한을 갖는 부분수열이 존재한다는 것은 $$(a_n)$$이 수렴하지 않음을 뜻한다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (발산하는 수열)**</ins> 수열 $$a_n = (-1)^n$$을 보자. 짝수 지표 부분수열 $$a_{2k} = 1 \to 1$$과 홀수 지표 부분수열 $$a_{2k-1} = -1 \to -1$$이 서로 다른 극한을 가지므로, 명제 12에 의해 $$(a_n)$$은 발산한다. 같은 방식으로 $$a_n = \cos(n\pi/2)$$ 같은 주기적 진동도 발산한다.

</div>

당장 우리에게 필요한 것은, 수열의 극한이 무한히 많은 항을 더하는 일의 토대라는 점이다.
