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

---

우리는 본격적으로 미적분학을 시작하기 전에 우선 수열의 극한을 정의한다. 여기서 *수열<sub>sequence</sub>* $$(a_n)$$이란 자연수에 실수를 대응시키는 함수, 즉 $$a : \mathbb{N} \to \mathbb{R}$$을 그 값들 $$a_1, a_2, a_3, \ldots$$의 나열로 본 것이다. [§함수의 극한](/ko/math/calculus/functions_and_limits)에서 우리는 이미 $$x \to \infty$$일 때 함수가 어떻게 행동하는지를 다루었는데, 수열의 극한은 그 이산적 버전, 즉 변수가 자연수만 취하는 경우에서 $$n \to \infty$$로만 가는 경우로 생각할 수 있다. 

## 수열의 수렴

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 실수열 $$(a_n)_{n=1}^\infty$$와 실수 $$L$$에 대해, 임의의 $$\varepsilon > 0$$에 대하여 어떤 자연수 $$N$$이 존재하여

$$n > N \implies \lvert a_n - L \rvert < \varepsilon$$

이 성립할 때, $$L$$을 $$n \to \infty$$일 때 $$a_n$$의 *극한<sub>limit</sub>*이라 하고 $$\lim_{n\to\infty} a_n = L$$로 적는다.

</div>

이 정의는 [§함수의 극한, ⁋정의 14](/ko/math/calculus/functions_and_limits#def14)를 거의 그대로 가져온 것으로, 수열은 그 정의에 의해 변수가 자연수뿐이고 한 방향($$+\infty$$)으로만 가므로, 수열의 극한을 정의하는 거의 유일한 방법은 이것 뿐이다. 약간의 변종은 수열이 무한대로 발산하는 것으로, 이는 [§함수의 극한, ⁋정의 13](/ko/math/calculus/functions_and_limits#def13)을 약간 변형하면 어떻게 정의해야 할지 자명하다. 그러나 물론, 특정한 값으로 수렴하는 수열과 무한대로 발산하는 수열이 아닌 다른 종류의 수열도 존재한다 ([예시 12](#ex12))

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 이 예시에서 우리는 $$a_n=1/n$$이 $$0$$으로 수렴하는 것과, $$b_n=n$$이 무한대로 발산하는 것을 보인다. 

우선 첫째 극한의 경우, 임의의 $$\varepsilon > 0$$에 대해 $$N > 1/\varepsilon$$인 자연수 $$N$$을 택하면, 

$$n > N\implies 1/n < 1/N < \varepsilon$$

이므로 $$\lvert 1/n\rvert < \varepsilon$$가 되어 증명이 완료된다.

또, 수열 $$b_n = n$$은 발산한다. 이를 확인하기 위해서는 임의의 실수 $$M$$에 대해 $$N = \lfloor M\rfloor$$로 잡으면 

$$n > N\implies b_n = n > M$$

임을 확인하면 된다. 

</div>

한편, 다음 명제 또한 [§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5)의 증명과 동일한 방식으로 진행하면 충분하다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (수열의 극한법칙)**</ins> 두 수열 $$a_n$$, $$b_n$$이 수렴하고, 그 수렴값을

$$\lim_{n\to\infty} a_n = L, \qquad \lim_{n\to\infty} b_n = M$$

이라 하자. 그러면

1. $$\lim (a_n + b_n) = L + M$$,
2. 임의의 상수 $$c$$에 대해 $$\lim c\,a_n = cL$$,
3. $$\lim a_n b_n = LM$$,
4. $$M \neq 0$$이고 모든 $$n$$에 대해 $$b_n \neq 0$$이면 $$\lim a_n/b_n = L/M$$

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

수렴하는 수열의 기본 성질들 또한 [명제 3](#prop3)에서 그러했듯 함수의 극한에서의 증명을 그대로 베껴와서 얻어진다. 가령 다음은 [§함수의 극한, ⁋명제 8](/ko/math/calculus/functions_and_limits#prop8)의 수열 버전이다.


<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (조임정리)**</ins> 충분히 큰 모든 $$n$$에서 $$a_n \leq c_n \leq b_n$$이고 $$a_n \to L$$, $$b_n \to L$$이면 $$c_n \to L$$이다.

</div>

그럼 다음의 간단하지만 유용한 결과를 얻을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (비율 판정)**</ins> 실수열 $$a_n$$이 모든 $$n$$에 대해 $$a_n > 0$$을 만족하고, 인접항의 비로 이루어진 수열이 $$a_{n+1}/a_n$$이 $$1$$보다 작은 값 $$L$$로 수렴하면 $$a_n \to 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$L < r < 1$$인 $$r$$를 고르면, 충분히 큰 $$n \geq N$$에서 $$a_{n+1}/a_n < r$$이므로 $$a_{N+k} < r^k a_N$$이다. $$0 < r < 1$$이라 $$r^k \to 0$$이고, 조임정리로 $$a_n \to 0$$이다.

</details>

이와 비슷하게, 실제 계산에서 많이 쓰이는 결과들을 다음 예시로 모아둔다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 다음은 수열의 극한의 기본 예시들이다.

1. $$p > 0$$에 대해 $$1/n^p \to 0$$이 성립한다. 이는 $$n \geq 1$$에서 $$n^p \geq n$$이므로 $$0 < 1/n^p \leq 1/n \to 0$$이고, 따라서 [명제 5](#prop5)를 적용하면 된다. 
2. 더 일반적으로, 같은 차수를 갖는 다항식의 비는 최고차항의 비에 의해 결정된다.

   $$\frac{a_k n^k + \cdots}{b_k n^k + \cdots}$$

   의 분자·분모를 $$n^k$$으로 나누면 분자·분모 모두 유한개의 $$1/n^j$$ 항과 상수항으로 이루어진다. 그럼 이 때 $$1/n^j \to 0$$이므로 분자와 분모는 각각 최고차항의 계수로 수렴하는 것을 알 수 있다. 만일 분모가 분자보다 큰 차수를 갖는다면 [명제 5](#prop5)와 앞선 1번에 의하여 이 비율이 $$0$$으로 수렴함을 알 수 있고, 비슷하게 분자가 분모보다 큰 차수를 갖는다면 이 비율이 발산함을 알 수 있다. 
3. $$\lvert r\rvert < 1$$이면 $$r^n \to 0$$이다. 이를 확인하기 위해, 적당한 $$h>0$$에 대해 $$\lvert r\rvert = 1/(1+h)$$이라 하자. 그럼 이항정리를 사용하면 $$(1+h)^n \geq 1 + nh$$이고, 따라서
    
    $$\lvert r\rvert^n = \frac{1}{(1+h)^n} \leq \frac{1}{1+nh} \to 0$$
    
    이다. 여기서 마지막의 수렴은 위 2번의 결과를 사용하였다. 만일 $$r=1$$인 경우 이 수열은 항상 $$1$$이므로 $$1$$로 수렴하는 것이 자명하며, 만일 $$\lvert r\rvert > 1$$이면 비슷하게 $$r=1+h$$라 했을 때

    $$\lvert r\rvert^n =(1+h)^n \geq 1+nh$$

    이므로 어떠한 $$M$$을 잡아오더라도 $$n$$을 충분히 키우기만 하면 $$\lvert r\rvert^n$$을 $$M$$보다 커지게 할 수 있고, 따라서 $$\lvert r\rvert^n$$은 발산한다. 
4. $$n^{1/n} \to 1$$이다. 이를 확인하기 위해 $$n^{1/n} = 1 + h_n$$ ( $$h_n \geq 0$$)으로 두면 이항정리로

   $$n = (1+h_n)^n \geq \binom{n}{2}h_n^2 = \frac{n(n-1)}{2}h_n^2$$

   이므로 $$h_n^2 \leq 2/(n-1) \to 0$$, 즉 $$h_n \to 0$$이기 때문이다.
5. $$r > 1$$, $$p > 0$$에 대해 $$n^p/r^n \to 0$$이 성립한다. 이는 [명제 6](#prop6)에 의하여, 인접한 항의 비가
    
    $$\frac{(n+1)^p}{r^{n+1}}\cdot\frac{r^n}{n^p} = \frac{1}{r}\left(1+\frac{1}{n}\right)^p \to \frac{1}{r} < 1$$

    이므로 바로 얻어진다. 
6. 비슷하게, $$r > 1$$, $$p > 0$$에 대해 수열 $$r^n/n!$$의 인접한 항의 비는 $$r/(n+1) \to 0 < 1$$이므로 같은 이유로 $$0$$이다.

</div>

## 단조수렴정리

한편, 다음 명제를 증명하기 위해서는 해석학의 지식이 필요하므로 현재 우리가 증명하는 것은 불가능하지만, 그 결과 자체는 유용하므로 미리 받아들이기로 한다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (단조수렴)**</ins> 위로 유계인 증가수열과 아래로 유계인 감소수열은 수렴한다. (증가수열의 극한은 그 항들의 상한이다.)

</div>

이에 대한 가장 유용한 활용은 다음 *자연상수*의 존재성 증명이다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (자연상수 $$e$$)**</ins> 수열 $$a_n = (1 + 1/n)^n$$은 증가하며 위로 유계이고, 따라서 [명제 8](#prop8)에 의해 수렴한다.

우선 이 수열이 증가수열임을 보이자. 우선 $$n$$개의 $$1+1/n$$과 하나의 $$1$$에 대하여 산술기하평균 부등식을 적용하면, 산술평균은

$$\frac{n(1+1/n)+1}{n+1} = \frac{n+2}{n+1} = 1 + \frac{1}{n+1}$$

이고 기하평균은 $$((1+1/n)^n\cdot 1)^{1/(n+1)}=a_n^{1/(n+1)}$$이므로 

$$a_n \leq \left(1+\frac{1}{n+1}\right)^{n+1} = a_{n+1}$$

가 되며, 뿐만 아니라 등호조건에서 $$n+1$$개의 수가 모두 같지 않으므로, 등호가 성립하지 <em-ko>않는</em-ko> 부등식 $$a_n < a_{n+1}$$을 얻을 수 있다. 

이제 이 함수가 위로 유계임을 보이기 위해, 이항정리로

$$a_n = \sum_{k=0}^{n}\binom{n}{k}\frac{1}{n^k}$$

임을 관찰하자. 각 항은

$$\binom{n}{k}\frac{1}{n^k} = \frac{1}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k} \leq \frac{1}{k!}$$

이며, $$k! \geq 2^{k-1}$$ ( $$k \geq 1$$ ) 이므로

$$a_n \leq \sum_{k=0}^{n}\frac{1}{k!} \leq 1 + \sum_{k=1}^{\infty}\frac{1}{2^{k-1}} = 3$$

이다. 이 수열의 극한을 *자연상수* $$e = 2.718\ldots$$로 정의한다.

</div>

## 부분수열

한편, 수열의 수렴 여부를 분석할 때, 수열의 일부 항만 골라 뽑은 새 수열을 보는 것이 유용하다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 수열 $$(a_n)$$과 자연수의 순증가 수열 $$n_1 < n_2 < n_3 < \cdots$$이 주어졌을 때, 새 수열 $$(a_{n_k})_{k\geq 1}$$을 $$(a_n)$$의 *부분수열<sub>subsequence</sub>*이라 한다.

</div>

설명은 복잡하게 해 두었지만, 수열 $$a_n$$에서 index의 순서를 유지한 상태로 일부 항만 택하는 것, 혹은 원래 수열에서 <em-ko>건너뛰며</em-ko> 항을 고르는 것이다. 그렇다면, 원래 수열이 특정 값으로 수렴한다면 이 수열의 임의의 부분수열도 그 값으로 수렴한다는 것이 직관적으로 자명할 것이다. 

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> 만일 수열 $$a_n$$이 $$L$$로 수렴하면 모든 부분수열 $$(a_{n_k})$$도 $$L$$로 수렴한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $$\varepsilon > 0$$에 대해 $$n \geq N$$이면 $$\lvert a_n - L\rvert < \varepsilon$$인 $$N$$을 잡자. 그럼 정의에 의해 $$n_k \geq k$$이고, 따라서 $$k \geq N$$이면 $$n_k \geq N$$이라

$$\lvert a_{n_k} - L\rvert < \varepsilon$$

이다. 즉 $$a_{n_k} \to L$$이다. 

</details>

이 명제의 실제 유용성은 어떠한 수열이 수렴한다는 것을 보일 때보다, 어떠한 수열이 수렴하지 <em-ko>않는다</em-ko>는 것을 보일 때 특히 유용하다. 위 명제의 대우명제에 의하여, 서로 다른 두 극한을 갖는 부분수열이 존재한다면 원래의 수열 $$(a_n)$$이 수렴하지 않을 것이기 때문이다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (발산하는 수열)**</ins> 수열 $$a_n = (-1)^n$$을 보자. 짝수번째 부분수열 $$a_{2k} = 1 \to 1$$과 홀수번째 부분수열 $$a_{2k-1} = -1 \to -1$$이 서로 다른 극한을 가지므로, 명제 11에 의해 $$(a_n)$$은 발산한다.

</div>
