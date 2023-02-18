---

title: "Measurable sets"
excerpt: "Definition of measure"

categories: [Math / Measure Theory]
permalink: /ko/math/measure_theory/measurable_sets
header:
    overlay_image: /assets/images/Measure_theory/Measurable_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-12-24
last_modified_at: 2023-02-14
weight: 1

---

## Lebesgue integral and Vitali set

학부 때 배우는 리만-스틸체스 적분은 우리가 고등학교 떄 배우는 리만적분 (혹은 구분구적법)의 성공적인 일반화라 할 수 있지만, 그럼에도 불구하고 이는 아직 중요한 몇 가지 질문에 대한 답을 주지 못한다. 예를 들어, 우리는 모든 연속함수가 리만-스틸체스의 정의 하에서 적분 가능하다는 것을 알고, 더 일반적으로 불연속점의 개수가 유한 개 뿐인 함수도 적분 가능하다는 것을 알고 있다. 하지만 반대로, 적분 가능한 함수가 정확하게 어떤 모양인지에 대해서는 전혀 알고 있지 않다. 

이를 가장 일반적인 방법으로 일반화하는 것이 르벡의 방법이다. 책상 위에 동전 무더기가 놓여있다고 하자. 이 동전들의 개수를 샐 때, 동전들이 이루는 탑을 하나하나 분리한 후, 각 탑이 몇 층인지를 세는 방법이 있을 수 있다. 이 방법이 리만적분이다. 즉, 리만적분은 밑면을 잘 나눈 다음, 이들에 해당하는 높이를 각각 재서 더하는 방법이라 할 수 있다. 반면 르벡적분은 각 층에 해당하는 동전이 몇 개 있는지를 센다. 이를 가능하도록 하기 위해서는 각 층에 있는 동전들을 세는 방법이 잘 주어져야 한다. 조금 더 수학적으로 이야기하자면, 구분구적법이나 리만적분은 적분을 할 때, 직사각형의 밑면이 적분구간의 어떤 partition으로 나오겠지만, 르벡적분의 경우, 직사각형의 밑면은 (충분히 좋은 함수의 경우) partition일 수도 있지만 여러 구간의 합집합일 수도 있고, 심지어는 discrete하게 주어질 수도 있다. 그럼에도 불구하고, 이렇게 이상하게 생긴 집합들의 넓이를 구하는 방법만 알 수 있다면 르벡적분의 값은 충분히 계산할 수 있을 것이다.

대표적인 예시는 유리수 집합 $\mathbb{Q}$의 characteristic function $1\_\mathbb{Q}$이다. 유리수의 denseness에 의하여, 구간 $[0,1]$의 partition을 어떻게 잡더라도 주어진 구간에서 이 함수의 supremum은 1이고, infimum은 0이므로 이 함수는 리만적분 가능하지 않다. 그러나 $1\_\mathbb{Q}$는 단 두 개의 값 $0,1$만을 함숫값으로 가지며, 함숫값이 1이 되는 집합 (즉 $\mathbb{Q}$)는 0이 되는 집합 ($[0,1]\setminus\mathbb{Q}$)보다 "무시할 만큼" 작으므로 르벡의 관점에서 이 함수는 적분 가능하며 적분값은 0이다.

이를 가능하게 하려면 실수집합 $\mathbb{R}$의 임의의 부분집합마다 넓이의 개념을 정의할 수 있어야 한다. 그러나 선택공리를 가정한다면 이는 불가능하다. 아주 루즈하게 다음과 같은 예시를 생각해보자.

실수의 임의의 부분집합 $E$에 대하여, $E$의 "넓이"를 주는 함수를 $\mu$라 하자. 즉, $E$의 넓이는 $\mu(E)$로 주어진다. 이 함수 $\mu$는 $\mathbb{R}$의 멱집합 $\mathcal{P}(\mathbb{R})$에서 $[0,\infty]$로의 함수이며, 기하학적인 의미에서 다음의 조건들을 만족해야 할 것이다.

1. 만일 집합들 $(E_i)$가 서로소라면, 이들의 합집합의 넓이는 이들 각각의 넓이의 합과 같다. 즉, $\mu(E_1\cup E_2\cup\cdots)=\mu(E_1)+\mu(E_2)+\cdots$가 성립해야 한다.
2. 만일 적당한 isometry에 의해서 집합 $E$가 $F$로 옮겨질 수 있다면, $\mu(E)=\mu(F)$이다.
3. Unit interval $[0,1)$의 크기는 1이다.

우선, 집합 $[0,1)$ 위에 equivalence relation $\sim$을

> $x\sim y\iff x-y\in\mathbb{Q}$

로 정의하자. 어렵지 않게 $\sim$이 equivalence relation임을 보일 수 있고, 따라서 $\sim$은 quotient set $[0,1)/\sim$을 만든다. 이제 quotient set의 각 원소들 (즉 equivalence class들)에서 원소들을 하나씩 뽑은 후, 이들을 모아 $N$이라 이름붙이자. 그리고 임의의 $r\in\mathbb{Q}\cap[0,1)$에 대하여 집합 $N_r$을 

> $N$을 $r$만큼 평행이동한 후, $[0,1)$ 바깥으로 나간 부분을 잘라 원점에 붙인 집합

으로 정의하자. 그럼 $N_r$은 $[0,1)$의 부분집합이 되며, 임의의 $x\in [0,1)$은 정확히 하나의 $r$에 대해 $N_r$의 원소가 된다. 이는

1. $N$에는 $x$와 $\sim$에 의해 equivalent한 어떤 원소 $y$가 있을 것이고, 그럼 (부호를 적당히 조절하여) $r=x-y$만큼만 평행이동을 해 주면 $x$는 $N_r$의 원소가 될 것이며, 
2. 또 만일 $x$가 $N_{r_1}$과 $N_{r_2}$에 동시에 포함된다면 적당한 $y_1,y_2\in N$에 대해 $x=r_1+y_1=r_2+y_2$이고[^1], 따라서 $y_1-y_2=r_2-r_1\in\mathbb{Q}$이므로 $y_1=y_2$여야 하기 때문이다.  

바꿔 말하자면, 서로 다른 $r\in\mathbb{Q}\cap[0,1)$에 대하여, $N_r$들은 $[0,1)$의 partition을 이룬다. 뿐만 아니라, 이들은 모두 동일한 집합 $N$을 평행이동하여 얻어진 집합들이므로 이들의 넓이는 모두 같아야 하며, 따라서

$$1=\mu([0,1))=\sum_{r\in\mathbb{Q}\cap [0,1)}\mu(N_r)$$

이 되어야 한다. 그런데 우변의 식은 만일 $\mu(N)=0$이라면 0이고, $\mu(N)$이 양수라면 무한대가 될 것이므로 어쨌건 1이 될 수는 없다.

1번부터 3번까지의 조건은 모두 넓이가 당연히 가져야 하는 성질이고, 우리는 넓이를 정의할 때 이들 조건을 포기할 생각이 없다. 그럼 이 예시는 실수집합의 넓이를 주는 함수 $\mu$가 1부터 3의 조건을 모두 만족하기 위해서는, 필연적으로 *넓이를 잴 수 없는 집합*이 존재해야 한다는 것을 보여준다.

## Measurable sets

따라서, 넓이를 정의하기 위해서는 먼저 *넓이를 잴 수 있는 집합*, 즉 *measurable set*을 먼저 정의해야 한다. 임의의 집합 $X$에 대하여, $X$의 measurable set을 정해준다는 것은 $X$에다, $\mathcal{P}(X)$의 어떤 부분집합 $\mathfrak{M}$을 붙여준 후 $\mathfrak{M}$의 원소들이 measurable하다고 정의하는 것이다. 이 정의는 $X$에다, $\mathcal{P}(X)$의 어떤 부분집합 $\mathcal{T}$를 붙여준 후, $\mathcal{T}$의 원소들을 open이라고 정의하는, 즉 $X$에 topology를 주는 과정과도 닮아있다. 실제로 measurable set들, 그리고 우리가 앞으로 정의할 measurable function들은 open set 및 continuous function과 비슷한 성질을 가지며, 이 때문에 루딘은 이들 두 개념을 병렬적으로 소개해놨다. 개인적으로 이 방식은 좀 산만하기도 하고, 우리는 위상수학을 따로 정리했으므로 measurable set에 대한 이야기만 하기로 한다. 

$\mathfrak{M}$은 다음과 같은 성질을 만족해야 한다.

1. $X$는 $\mathfrak{M}$의 원소이다. 즉, $X$ 자체는 크기를 잴 수 있어야 한다.
2. 만약 어떤 집합 $A$가 $\mathfrak{M}$의 원소라면, $A^c$도 $\mathfrak{M}$의 원소이다. 즉, 만일 $A$의 크기를 잴 수 있다면, 그 여집합 $A^c$의 크기 또한 잴 수 있어야 한다.
3. 만약 $A_1,A_2,\ldots\in\mathfrak{M}$이라면, $A=\bigcup A_i$ 또한 $\mathfrak{M}$의 원소이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 집합 $X$에 대하여, 위의 조건 1~3을 만족하는 모임 $\mathfrak{M}$을 $X$ 위에서 정의된 *$\sigma$-algebra*라 부른다.

</div>

여기서 $\sigma$는 우리가 앞으로 자주 사용할 naming convention으로, *countable*의 줄임말이라 생각하면 된다. $\mathfrak{M}$이 $\sigma$-algebra라 불리는 이유는 $\mathfrak{M}$이 3번 조건에 의해 *countable*한 union에 대해 닫혀있기 때문이다. 만일 $\mathfrak{M}$이 유한한 합집합에 대해서만 닫혀있다면, $\sigma$를 떼고 그냥 algebra라고만 부른다.

몇 가지 주의해서 살펴볼 것이 있다. 우선, 1번 조건에 의해 $X\in\mathfrak{M}$이므로, 이를 2번과 결합하면 $\emptyset\in\mathfrak{M}$이다. 그럼 countable union에서, 유한 개의 집합만 남겨두고 나머지를 모두 공집합으로 잡으면 임의의 $\sigma$-algebra는 그냥 algebra이기도 하다는 것을 알 수 있다. 또, 2번과 3번 조건을 결합하면 De Morgan 법칙에 의해

$$\bigcap A_i=\left(\bigcup A_i^c\right)^c\in\mathfrak{M}$$

이므로 $\mathfrak{M}$은 countable intersection에 대해서도 닫혀있다. 마지막으로, $A\setminus B=A\cap B^c$이므로, 만일 $A,B\in\mathfrak{M}$이라면 $A\setminus B$도 $\mathfrak{M}$의 원소다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 집합 $X$와, $X$ 위에서 정의된 $\sigma$-algebra $\mathfrak{M}$에 대하여 pair $(X,\mathfrak{M})$을 *measurable space*라 부르고, $\mathfrak{M}$의 원소들을 *measurable set*들이라 부른다. 

</div>

그리고 마지막으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Measurable space $X$와, topological space $Y$가 주어졌을 때, 함수 $f:X\rightarrow Y$가 *measurable function*이라는 것은 임의의 open set $V\subset Y$에 대하여, $f^{-1}(V)$가 항상 measurable인 것이다.

</div>

정의에 의해, 다음 명제는 자명하다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Measurable space $X$, 그리고 두 topological space $Y,Z$와 continuous function $g:Y\rightarrow Z$가 주어졌다 하자. 그럼 임의의 measurable function $f:X\rightarrow Y$에 대하여, $g\circ f:X\rightarrow Z$는 항상 measurable이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 open set $V\subset Z$에 대하여, $g$는 continuous이므로 $U=g^{-1}(V)$는 $Y$의 open set이다. 이제 $f$는 measurable이므로 증명 끝.

</details>

조금 덜 자명한 건 다음의 명제다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $u,v$가 measurable space $X$ 위에 정의된 real measurable function들이라 하자. 만일 $\Phi$가 $\mathbb{R}^2$에서 topological space $Y$로의 continuous function이라면, 다음의 함수

$$h(x)=\Phi(u(x),v(x))$$

는 $X$에서 $Y$로의 measurable function이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이 함수 $h$는 사실 $f(x)=(u(x),v(x))$에 대해 $\Phi\circ f$로 정의된 함수다. $\Phi$는 연속이므로, 앞선 명제에 의해 $f$가 measurable임만 보이면 충분하다.

우선 임의의 interval $I_1,I_2$에 대해 $I_1\times I_2$를 생각하자. 그럼 $f^{-1}(I_1\times I_2)$는 사실

$$f^{-1}(I_1\times I_2)=u^{-1}(I_1)\cap v^{-1}(I_2)$$

이므로, measurable subset들의 finite intersection이다. 한편, 임의의 open set은 이러한 box들의 countable union으로 나타낼 수 있으므로 (예컨대 **[SS]**, Theorem 1.4.) $\sigma$-additivity에 의해 나머지는 자명. 

</details>

특히, $\Phi(x,y)=x+y$, 그리고 $\Phi(x,y)=xy$일 경우 우리는 두 measurable function의 합과 곱이 각각 measurable임을 알 수 있다. 또, 만일 $\Phi:\mathbb{R}^2\rightarrow\mathbb{C}$를 $(x,y)\mapsto x+iy$로 잡는다면, 우리는 두 real-valued measurable function $u,v$에 대해 $f=u+iv$가 measurable임을 알 수 있다. 그리고 주어진 복소수에 대해 real part, imaginary part, 절댓값을 얻는 함수는 연속이므로 $\Re f$, $\Im f$, 그리고 $\lvert f\rvert$ 또한 모두 real measurable function들이 된다. 

조금 대수적인 마인드로 다음을 정의할 수 있다. 

> $\mathcal{P}(X)$의 subset $\mathcal{S}$에 대하여, $\mathcal{S}$를 포함하는 $\sigma$-algebra 중 가장 작은 것을 $\mathcal{S}$에 의해 generate된 $\sigma$-algebra라 한다.

$\mathcal{P}(X)$ 자체가 $\sigma$-algebra이므로, 다음만 보이면 충분하다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> $\sigma$-algebra의 임의의 교집합은 다시 $\sigma$-algebra이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $X$ 위에 정의된 $\sigma$-algebra들의 collection $\\{\mathfrak{M}\_i\\}\_{i\in I}$를 생각하자. 우선, 각 $i$에 대해 $X\in\mathfrak{M}_i$이므로 $X\in\bigcap\mathfrak{M}_i=\mathfrak{M}$이다. 또, 만일 $A\in\mathfrak{M}$이라면 모든 $i$에 대해 $A\in\mathfrak{M}_i$이고, 따라서 모든 $i$에 대해 $A^c\in\mathfrak{M}_i$이므로 다시 $A^c\in\mathfrak{M}$이다. $\sigma$-additivity의 경우도 마찬가지로 성립한다.   

</details>

## Borel sets

많은 $\sigma$-algebra 가운데 우리가 관심을 갖는 것은 *Borel $\sigma$-algebra*다. 정의를 보면 왜 우리가 여기에 관심을 갖는지 알게 된다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> Topological space $(X,\mathcal{T})$에 대하여, $\mathfrak{M}
_\mathcal{T}$를 $\mathcal{T}$에 의해 generate된 $\sigma$-algebra라 하자. 이 떼 measurable space $(X,\mathfrak{M}\_\mathcal{T}$를 *Borel $\sigma$-algebra*, 그리고 이 때의 measurable set들을 *Borel set*, measurable function들을 *Borel function*이라 부른다. 

</div>

우리는 최소한 임의의 interval (혹은 box, ...) 들의 넓이는 잴 수 있어야 한다. 또, 임의의 open set은 이러한 interval들의 countable union으로 나타나므로, open set들은 모두 measurable해야 한다. 따라서 $\mathcal{T}$의 모든 원소가 measurable해야 하므로, 이들을 포함하는 가장 작은 $\sigma$-algebra $\mathfrak{M}\_\mathcal{T}$를 생각하는 것이다.

이렇게 $\mathfrak{M}\_\mathcal{T}$를 정의하고 나면 몇 가지 확인할 것이 있다. 우선, $\sigma$-algebra의 조건에 의해, 임의의 open set $U\in\mathcal{T}\subset\mathfrak{M}\_\mathcal{T}$의 complement는 정의에 의해 다시 $\mathfrak{M}\_\mathcal{T}$의 원소이므로, 임의의 closed set은 measurable이다. 뿐만 아니라, open이거나 closed일 필요는 없는 다음의 집합들

> open set들의 countable intersection, closed set들의 countable union

들도 모두 $\mathfrak{M}\_\mathcal{T}$의 원소가 된다. 이렇게 만들어지는 집합들에는 *Borel hierarchy*라는 전통에 따라 이름을 붙인다. 예를 들어, open set들의 countable union은 $G\_\delta$ set, 그리고 closed set들의 countable intersection은 $F\_\sigma$ set이라 하고, 다시 $G_\delta$ set들의 countable intersection은 $G\_{\delta\sigma}$ set, $F\_\sigma$ set들의 countable union은 $F\_{\sigma\delta}$ set, ... 그러나 이 이름들을 본격적으로 사용하지는 않을 것이다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $(X,\mathfrak{M})$이 $sigma$-algebra, $Y$가 topological space, 그리고 $f:X\rightarrow Y$가 어떤 함수라 하자.

1. Preimage $f^{-1}(E)$가 $\mathfrak{M}$의 원소이도록 하는 $Y$의 임의의 부분집합 $E$들을 모아 이를 $\Omega$라 하자. 그럼 $\Omega$는 $Y$ 위에서 정의된 $\sigma$-algebra이다.
2. $f$가 measurable이고, $E$를 $Y$의 Borel set이라 하자. 그럼 $f^{-1}(E)\in\mathfrak{M}$이다. 
3. 만약 $Y$가, 일반적인 topology가 장착된 $[-\infty, \infty]$ (즉 $\mathbb{R}$에 양 끝점 $\pm\infty$를 붙인 extended real number system)이라면, 함수 $f$가 measurable이기 위해서는 $f^{-1}((\alpha,\infty])\in\mathfrak{M}$임을 보이면 충분하다.
4. $Z$가 또 다른 topological space이고, $g:Y\rightarrow Z$가 Borel mapping이라 하자. 만일 $f$가 measurable이라면, $g\circ f$도 measurable이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1번 성질은 자명하다. 예컨대 [Set theory, §집합의 연산, 명제 6](/ko/math/set_theory/set_operations#pp6)과 같은 글의 [명제 8](/ko/math/set_theory/set_operations#pp8)등을 보면 된다.

한편, 2번의 경우, $f$는 measurable이므로 임의의 open set $V$에 대해 $f^{-1}(V)\in\mathfrak{M}$이어야 하고, Borel set은 이러한 open set들을 바탕으로 countable한 연산을 통해 얻어지므로 성립한다.

3번은 실제로 계산을 할 때 가끔 사용하는 명제인데, 우선 임의의 closed ray $[\beta, \infty]$와 같은 경우, $(\beta+1/n,\infty]$들의 합집합으로 나타낼 수 있으므로 $[\beta,\infty]$를 $(\alpha,\infty]$꼴의 countable union으로 나타낼 수 있다. 한편, 이렇게 만든 closed ray의 차집합은 $[-\infty,\beta)$이고, 따라서 $[-\infty,\beta)\cap (\alpha,\infty]=(\alpha,\beta)$에서 임의의 basic open set을 countable한 집합의 연산을 통해 얻을 수 있다는 것을 안다. 한편, 이들 basic open set $(\alpha,\beta)$들은 그럼 $Y$의 Borel set의 preimage이므로, 2번에 의해 $f^{-1}((\alpha,\beta)))\in\mathfrak{M}$이고 따라서 $f$는 measurable이다.

마지막으로, $Z$의 임의의 open set $U$에 대해 $g^{-1}(U)$는 $Y$에서 Borel이고, 따라서 2번에 의해 $g^{-1}(U)$의 $f$에 의한 preimage는 measurable이므로 증명 끝.  

</details>

이 명제의 1번에서 $Y$는 topological space가 아니라 그냥 집합이어도 된다. 1번은 $X$에 정의된 measurable structure를 임의의 함수 $f$를 이용해 다른 집합 $Y$에 옮기는, topology에서는 우리가 weak topology라 부르던 것과 유사한 construction이다. 4번은 앞선 [명제 4](#pp4)의 일반화라 할 수 있으며, 우리는 종종 3번을 이용해 어떤 함수 $f$가 measurable인 것을 보일 수 있다. 이는 대표적으로 다음과 같이 사용된다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Measurable function $f_n:X\rightarrow [-\infty,\infty]$들의 family $(f_n)_1^\infty$을 생각하자. 그럼 다음의 두 함수

$$g(x)=\sup_{n\geq 1} f_n,\qquad h(x)=\limsup_{n\rightarrow\infty} f_n(x)$$

는 모두 measurable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$g^{-1}((\alpha,\infty])=\bigcup_1^\infty f_n^{-1}((\alpha,\infty])$이므로 앞선 명제의 3번에 의해 자명하다. Limsup을 보일 때는 다음의 식

$$h=\inf_{k\geq 1}\sup_{i\geq k}f_i$$

을 기억하자.

</details>

물론, 마찬가지로 $\inf$와 $\liminf$에 대해서도 동일한 결과가 성립한다. 이렇게 정의된 함수들을 간단히 $\sup f_n$, $\inf f_n$, $\liminf f_n$ 등과 같이 적기로 하자. 만약 임의의 $x\in X$에 대하여, $n\rightarrow\infty$일 때 $f_n(x)$가 수렴한다면, 이 함수는 $\lim f_n$과 같이 쓸 수 있을 것이다. 이 경우, 우리는

$$\lim f_n=\limsup f_n=\liminf f_n$$

인 것을 알고 있으므로 앞선 명제에 의해 $\lim f_n$은 항상 measurable이다. 

이번에는 주어진 measurable function들 $f,g$에 대해 함수열을 $f,g,f,g,\ldots$로 정의해보자. 그럼 이들의 supremum과 infimum은 정확히 다음의 식

$$h_1(x)=\max(f(x),g(x)),\qquad h_2(x)=\min(f(x),g(x))$$

으로 주어진다. 따라서, 앞선 명제에 의해 이들은 measurable이다. 특수한 경우는 $g$가 상수함수 $0$인 경우인데, $[-\infty,\infty]$의 임의의 부분집합 $U$가 $0$을 포함한다면 $g^{-1}(U)=X$, 그렇지 않다면 $\emptyset$이므로 우리는 어렵지 않게 $g$가 measurable이란 것을 증명할 수 있다. 그럼 measurable function $\max(f,0)$과 $\min(f,0)$은 모두 measurable이다. 이들은 각각, $f$가 양수 (혹은 음수)인 곳에서는 $f$의 함숫값을 그대로 유지하지만, 그렇지 않은 곳은 모두 0으로 통일해주는 함수이다. 우리는 루딘을 따라 $f^+=\max(f,0)$, $f^-=\min(f,0)$으로 정의하고, 이들을 $f$의 positive/negative part라 부른다. 이 정의에서 좋은 점은 $f^-$ 또한 항상 0보다 크거나 같다는 것이다. 우리는

$$f=f^+-f^-,\qquad\lvert f\rvert=f^++f^-$$

임을 알고 있으므로, 앞으로 real-valued measurable function을 생각할 때는 0보다 크거나 같은 함수들만 생각하면 충분하다. 뿐만 아니라, 임의의 complex-valued measurable function은 실수부와 허수부로 분리하고 나면 real-valued이므로, 음이 아닌 real-valued measurable function만 잘 다룰 수 있으면 complex-valued measurable function 또한 다룰 수 있다. 

## Measure space

지금까지 우리는 *크기를 잴 수 있는 집합*을 정의했으므로, 이제는 그 집합들에 실제로 크기를 줄 차례다.

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> Measurable space $(X,\mathfrak{M})$이 주어졌다 하자. 이 때, *positive measure*는 countable additivity를 만족하는 함수 $\mu:\mathfrak{M}\rightarrow[0,\infty]$다. 즉, 만일 $(E_i)$가 서로소인 집합이라면 $\mu(\bigcup E_i)=\sum\mu(E_i)$가 성립한다. 이 때, $(X,\mathfrak{M},\mu)$를 *measure space*라 부른다.

</div>

위에서 정의했던 measurable function과 마찬가지로, measure $\mu$의 함숫값 또한 양수 뿐만 아니라 일반적인 실수나, 더 나아가 복소수까지도 될 수 있다. 물론 이 경우 $\mu$를 넓이로 보기는 좀 그렇지만, 예를 들어 각 넓이마다 일종의 가중치를 준다고 생각하면 안될 것도 없긴 하다. 하지만 역시 앞선 measurable function과 마찬가지로, complex-valued measure 또한 positive measure를 잘 연구하여 그 성질을 파악할 수 있다. 따라서 별다른 말이 없다면 앞으로 measure라는 말은 항상 positive measure만을 의미하는 것으로 한다. Complex-valued measure는 우선 우리가 positive measure를 잘 탐구한 후에 다시 살펴보게 될 것이다.

Measure $\mu$는 $\infty$를 그 값으로 가질 수 있다. 하지만 모든 measurable set이 $\infty$를 그 크기로 갖는다면 조금 문제가 생겨서, 적어도 어떤 하나의 집합에 대해서는 $\mu(E)<\infty$인 것으로 가정한다. 다음은 measure의 성질.

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> Measure space $(X,\mathfrak{M},\mu)$에 대하여, 

1. $\mu(\emptyset)=0$이다.
2. 따라서, finite additivity 또한 성립한다. 즉, 만일 $A_1,\ldots, A_n$이 서로소인 measurable set들이라면 
     $$\mu(A_1\cup\cdots\cup A_n)=\mu(A_1)+\cdots+\mu(A_n).$$
3. $A\subset B$라면 $\mu(A)\leq\mu(B)$.
4. 만일 $A_n\nearrow A$이고, $A_n$들과 $A$가 모두 measurable이라면 $\mu(A_n)\rightarrow\mu(A)$.
5. 만일 $A_n\searrow A$이고, $A_n$들과 $A$가 모두 measurable이며, $\mu(A_1)<\infty$라면 $\mu(A_n)\rightarrow\mu(A)$.

</div>

$A_n\nearrow A$는 

$$A_1\subset A_2\subset\cdots,\qquad A=\bigcup_{i=1}^\infty A_i$$

를 줄여 쓴 것이고, 비슷하게 $A_n\searrow A$는

$$A_1\supset A_2\supset\cdots,\qquad A=\bigcap_{i=1}^\infty A_i$$

을 줄여 쓴 것이다. 마지막 두 성질은 measure $\mu$가 일종의 continuity를 만족하는 것으로 생각할 수 있기 때문에, 이를 각각 continuity from below/above라 부르기도 한다.

<details class="proof--alone" markdown="1">
<summary>증명</summary>

$E$가 $\mu(E)<\infty$를 만족하는 measurable set이라 하자. 그럼 $E=E\cup\emptyset\cup\emptyset\cup\cdots$이고, 우변의 집합들은 당연히 서로소이므로

$$\mu(E)=\mu(E\cup\emptyset\cup\emptyset\cup\cdots)=\mu(E)+\mu(\emptyset)+\mu(\emptyset)+\cdots$$

이제 $\mu(E)<\infty$이므로, 양 변에서 $\mu(E)$를 빼면 $\mu(\emptyset)=0$을 얻는다. 그럼 $A_{n+1}$부터의 집합을 모두 공집합으로 두면 2번을 얻는다. 

한편, 임의의 두 measurable set $A,B$에 대해 우리는 $A\setminus B$ 또한 measurable인 것을 확인했었다. 이제 $A\subset B$라면, $B=A\cup(B\setminus A)$이고, $A$와 $B\setminus A$는 서로소이므로 2번에 의해

$$\mu(B)=\mu(A)+\mu(B\setminus A)$$

이고, $\mu(B\setminus A)\geq 0$이므로 $\mu(B)\geq \mu(A)$가 성립한다.

이제 마지막 두 성질을 보이자. $A_i$들은 서로소가 아니므로, $\sigma$-additivity를 함부로 사용할 수 없다. 따라서 집합 $B_1=A_1$, 그리고 $B_n=A_n\setminus A_{n-1}$로 정의하자. 그럼 $\bigcup B_i$는 정확히 $A$가 되며, $B_i$들은 서로소이고 

$$A_n=\bigcup_{i=1}^n B_i$$

가 성립하므로 $\bigcup B_i=A$이고 $\mu(A_n)=\sum_{i=1}^n\mu(B_i)$가 성립한다. 이제 $\mu$의 $\sigma$-additivity에 의해

$$\mu(A)=\sum_{i=1}^\infty\mu(B_i)=\lim_{n\rightarrow\infty}\sum_{i=1}^n \mu(B_i)=\lim_{n\rightarrow\infty}\mu(A_n)$$

이므로 원하는 결과를 얻는다. 마지막 조건은 간단하게 $C_n=A_1\setminus A_n$으로 정의한 후, $C_n\nearrow C=A_1\setminus A$임을 확인하면 된다. 그럼 앞선 결과에 의해

$$\mu(A_1)=\mu(C)+\mu(A)=\lim_{n\rightarrow\infty}\mu(C_n)+\mu(A)=\lim_{n\rightarrow\infty}\mu(A_1\setminus A_n)+\mu(A)$$

를 얻을 것이다. $\mu(A_1)=\mu(A_n)+\mu(A_1\setminus A_n)$에서, $\mu(A_1)<\infty$이므로 $\mu(A_n)$도 유한하고 따라서 $\mu(A_n)$을 이항하면 $\mu(A_1)-\mu(A_n)=\mu(A_1\setminus A_n)$이다. 그러므로 앞선 식은

$$\mu(A_1)=\lim_{n\rightarrow\infty}(\mu(A_1)-\mu(A_n))+\mu(A)=\mu(A_1)-\lim_{n\rightarrow\infty}\mu(A_n)+\mu(A)$$

가 된다. $\mu(A_1)<\infty$이므로 양 변에서 $\mu(A_1)$을 소거할 수 있고, 마찬가지로 $\mu(A)<\mu(A_1)$도 유한해야 하므로 우리는 원하는 결론

$$\mu(A)=\lim_{n\rightarrow\infty}\mu(A_n)$$

을 얻는다.
</details>

마지막 성질의 증명을 잘 살펴보면, 굳이 $\mu(A_1)$이 유한하지 않더라도, 어떤 하나의 $A_i$에 대해서만 $\mu(A_i)<\infty$이면 된다는 것을 확인할 수 있다. 하지만 반드시 어떤 집합의 measure는 반드시 유한해야 한다. 예를 들어, (아직 정의하지는 않았지만) 실수 집합에 Lebesgue measure를 주자. 집합 $A_n=[n,\infty)$는 모두 무한한 measure를 가지며, $n$이 커질 때 $A_n\searrow \emptyset$이지만 $\mu(A_n)$은 항상 $\infty$이므로, 0으로 수렴하지 않는다. 

위에서의 Lebesgue measure는 우리가 생각하는 일반적인 넓이를 주는 measure다. 물론 앞서 언급했듯 이 넓이는 실수의 모든 부분집합에 대해서 정의될 수는 없다. 실제로 우리는 다다음 글에서 $\mathbb{R}$ 위에 정의된 Borel $\sigma$-algebra 위에서 Lebesgue measure가 잘 정의된다는 것을 보일 것이다. 그 전에 몇 가지 (상대적으로 정의하기 용이한) measure 두 개를 살펴보자. 

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> 임의의 집합 $X$를 생각하자. 그럼 $\mathcal{P}(X)$는 당연히 $\sigma$-algebra다. 이제 $\mu:\mathcal{P}(X)\rightarrow[0,\infty]$를 

$$\mu(E)=\begin{cases}n&\text{if $\lvert E\rvert=n$}\\\infty&\text{if $E$ is infinite}\end{cases}$$

으로 정의하자. 어렵지 않게 $\mu$의 $\sigma$-additivity를 보일 수 있다. 서로소인 집합을 합집합할 때, 이 집합열에서 원소의 개수가 하나 이상인 유한집합이 유한개라면 합집합 또한 유한하며 그 원소의 개수는 합집합 되어있는 집합들의 원소의 개수들의 총합과 같을 것이다. 만일 원소의 개수가 하나 이상인 유한집합이 무한개 모여있거나, 혹은 더해지는 집합 중 하나가 무한집합이라면 합집합도 무한집합이 될 것이다. 이렇게 정의된 measure $\mu$를 *counting measure*라 부른다. 

한편, 우리는 고정된 $x\in X$에 대해, 이번에는 measure $\delta_x:\mathcal{P}(X)\rightarrow[0,\infty]$를

$$\delta_x(E)=\begin{cases}1&\text{if $x\in E$}\\ 0&\text{if $x\not\in E$}\end{cases}$$

으로 정의할 수 있다. 이 measure는 $x$에 concentrate되어있는 unit mass라 부른다. 

</div>




---
**Reference**

**[Rud]** W. Rudin, *Real and complex analysis* Mathematics series. McGraw-Hill, 1987.  
**[SS]** E.M. Stein and R. Shakarchi. *Real Analysis: Measure theory, Integration, and Hilbert spaces*. Princeton University Press, 2009.  
**[Fol]** G.B. Folland, *Real Analysis: Modern Techniques and Their Applications*. Pure and Applied Mathematics: A Wiley Series of Texts, Monographs and Tracts. Wiley, 2013.

---

[^1]: 편의상 대충 썼지만 정확히 말하자면 $r_1+y_1-1$이 될 수도 있고... 아무튼 $y_1$과 $y_2$의 차이가 유리수라는 게 중요하다.
