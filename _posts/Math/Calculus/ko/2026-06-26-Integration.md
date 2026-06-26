---
title: "적분"
description: "부정적분(원시함수)을 미분의 역연산으로 정의하고, 정적분을 분할 위의 리만 합의 극한으로 도입한다. 두 원시함수가 상수 차이로만 다름, 부정적분의 선형성과 기본 공식, 연속함수의 적분가능성, 적분의 선형성·구간가법성·단조성과 평균값 정리, 부호 있는 넓이로서의 의미를 다룬다."
excerpt: "원시함수와 부정적분, 리만 합과 정적분, 적분의 성질과 평균값 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/integration
sidebar: 
    nav: "calculus-ko"

date: 2026-06-26
weight: 10
---

우리는 지금까지 함수의 극한을 정의하고, 평균변화율의 극한을 이용해 미분을 정의하였다. 이번 글에서 우리는 그 과정의 역연산인 적군을 정리하고 여러가지 성질을 살펴본다. 

## 원시함수

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 구간 $$I$$에서 정의된 함수 $$f$$에 대하여, $$I$$의 모든 점에서 $$F'(x) = f(x)$$를 만족하는 미분가능한 함수 $$F$$를 $$f$$의 *원시함수<sub>antiderivative</sub>*라 한다.

</div>

예를 들어 $$F(x) = x^2$$은 $$f(x) = 2x$$의 원시함수이다. 그런데 $$x^2 + 1$$, $$x^2 - 5$$도 모두 도함수가 $$2x$$이므로 원시함수이다. 즉 한 원시함수에 상수를 더해도 여전히 원시함수이다. 기하학적으로는 같은 모양의 곡선을 위아래로 평행이동한 무리가 모두 같은 도함수(같은 기울기 분포)를 가지는 셈이다. 원시함수는 이처럼 유일하지 않지만, 이는 정확히 상수항의 차이만큼만 달라질 수 있다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$F$$가 구간 $$I$$에서 $$f$$의 원시함수이면, $$f$$의 모든 원시함수는 상수 $$C$$에 대해 $$F(x) + C$$의 꼴이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$G$$도 $$f$$의 원시함수라 하면 $$(G - F)' = f - f = 0$$이다. [§평균값 정리, ⁋따름정리 5](/ko/math/calculus/mean_value_theorem#cor5)에 의해 구간에서 도함수가 항등적으로 $$0$$인 함수는 상수이므로, $$G - F = C$$인 상수 $$C$$가 있어 $$G = F + C$$이다.

</details>

이 명제에 따라 $$f$$의 원시함수 전체를 하나의 표현으로 묶어

$$\int f(x)dx = F(x) + C$$

로 적고, 이를 $$f$$의 *부정적분<sub>indefinite integral</sub>*이라 한다. 여기서 $$C$$를 *적분상수*, $$f$$를 *피적분함수*, 기호 $$dx$$를 적분변수의 표시로 본다. [명제 2](#prop2)가 보장하는 "상수 차이뿐"이라는 사실 덕분에 적분상수 $$C$$ 하나로 모든 원시함수를 한꺼번에 나타낼 수 있다.

우리가 암묵적으로 가정하는 것, 즉 구간이 연결되어 있다는 가정은 본질적인 것까지는 아니지만, 위의 명제는 오직 구간이 연결되어있을 때만 성립한다. 정의역이 끊겨 있으면 각 조각마다 상수가 달라질 수 있기 때문이다. 가령 $$1/x$$는 $$x > 0$$과 $$x < 0$$에서 따로 정의되는데, $$F(x) = \ln\lvert x\rvert$$에 두 조각에서 서로 다른 상수를 더한 것도 모두 $$1/x$$의 원시함수이므로, 정의역 전체에서는 "상수 차이뿐"이라는 명제가 문자 그대로 적용되지는 않는다.

구간이 연결되어 있다는 가정 아래, 적분상수 $$C$$는 *초기조건*이 주어지면 정확하게 하나로 결정된다. 이것이 부정적분으로 미분방정식을 푸는 기본 방식이다. 가령 $$F'(x) = 3x^2 + 1$$이고 $$F(1) = 5$$이면, 부정적분 $$F(x) = x^3 + x + C$$에 초기조건을 넣어 $$1 + 1 + C = 5$$, 곧 $$C = 3$$이 되어 $$F(x) = x^3 + x + 3$$으로 유일하게 정해진다. 

## 부정적분의 성질과 예시

한편, 우리는 [§미분법](/ko/math/calculus/differentiation_rules)에서 여러 함수의 미분을 살펴보았고, 부정적분은 미분의 반대이므로 이를 통해 적분공식들을 유도할 수 있다. 우선 그 전에 부정적분의 선형성을 보이자. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (부정적분의 선형성)**</ins> $$f, g$$가 원시함수를 가지고 $$a, b$$가 상수이면

$$\int \bigl(a f(x) + b g(x)\bigr)dx = a\int f(x)dx + b\int g(x)dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F, G$$를 각각 $$f, g$$의 원시함수라 하면, [§미분과 도함수, ⁋명제 4](/ko/math/calculus/derivatives#prop4)에 의해

$$(aF + bG)' = aF' + bG' = af + bg$$

이므로 $$aF + bG$$가 $$af + bg$$의 원시함수이다.

</details>

이제 [§미분법](/ko/math/calculus/differentiation_rules)에서의 여러 함수들의 도함수 공식을 뒤집으면 다음의 기본 공식들을 얻는다. 즉, 각 공식의 우변을 미분하면 피적분함수가 된다.

$$\int x^rdx = \frac{x^{r+1}}{r+1} + C\ (r \neq -1), \qquad \int \frac{1}{x}dx = \ln\lvert x\rvert + C,$$

$$\int e^xdx = e^x + C, \qquad \int \cos xdx = \sin x + C, \qquad \int \sin xdx = -\cos x + C,\qquad \int \sec^2 xdx = \tan x + C,$$

$$\int \frac{dx}{1 + x^2} = \arctan x + C, \qquad \int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x + C.$$

선형성과 이 공식들을 결합하면 기본 함수들의 임의의 합 또한 항별로 적분할 수 있다. 피적분함수가 표준형이 아니면 먼저 다른 도구들로 변형하는데, 가령 삼각함수 관계식

$$\tan^2 x = \sec^2 x - 1$$

로 바꾸거나 분수 $$(x^2+1)/x$$를 $$x + 1/x$$로 나누어 각 항을 위 공식에 맞추는 식이다.

특히 유용하게 쓰이는 치환적분과 부분적분은 각각 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)와 [§미분법, ⁋명제 3](/ko/math/calculus/differentiation_rules#prop3)을 거꾸로 읽은 것이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (치환적분)**</ins> $$g$$가 미분가능하고 $$f$$가 연속이면

$$\int f(g(x)) g'(x) dx = \int f(u) du \quad (u = g(x))$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$F$$를 $$f$$의 원시함수라 하면 [§미분법, ⁋정리 4](/ko/math/calculus/differentiation_rules#thm4)에 의해

$$\frac{d}{dx}F(g(x)) = F'(g(x))g'(x) = f(g(x))g'(x)$$

이므로, $$F(g(x))$$가 좌변 피적분함수의 원시함수이다. 따라서 $$\int f(g(x))g'(x)dx = F(g(x)) + C = F(u) + C = \int f(u)du$$이다.

</details>

실용에서는 $$u = g(x)$$, $$du = g'(x) dx$$로 두고 식을 $$u$$만으로 바꾸어 적분한 뒤 되돌린다. 가령 $$u = \cos x$$로 두면 $$\int \tan x dx = -\int du/u = -\ln\lvert\cos x\rvert + C$$이고, 같은 요령으로 $$\int x/(x^2+1) dx = \ln(x^2+1)/2 + C$$를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5 (부분적분)**</ins> $$u, v$$가 미분가능하고 그 도함수가 연속이면

$$\int u v' dx = uv - \int u' v dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§미분법, ⁋명제 3](/ko/math/calculus/differentiation_rules#prop3)으로 $$(uv)' = u'v + uv'$$이므로 $$uv' = (uv)' - u'v$$이고, 양변을 적분하면 $$\int (uv)' dx = uv$$에서 주장이 따른다.

</details>

핵심은 $$u$$를 미분하면 단순해지는 쪽, $$v'$$을 적분할 수 있는 쪽으로 고르는 것이다. 가령 $$\int x e^x dx$$는 $$u = x$$로 두어 $$xe^x - e^x + C$$가 되고, 로그·역삼각함수처럼 미분이 도리어 간단해지는 함수는 $$v' = 1$$로 보아 $$u$$ 자리에 놓는다 ($$\int \ln x dx = x\ln x - x + C$$). 부분적분이 피적분함수를 단순화하지 않고 자기 자신으로 되돌아오는 경우도 있는데, 이때는 원래 적분을 미지수로 보고 대수적으로 푼다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$I = \int e^x\cos x dx$$는 부분적분을 두 번 하면 자기 자신이 돌아온다. $$u = e^x$$, $$v' = \cos x$$로 두면

$$I = e^x\sin x - \int e^x\sin x dx = e^x\sin x - \Bigl(-e^x\cos x + \int e^x\cos x dx\Bigr) = e^x(\sin x + \cos x) - I$$

이므로 $$2I = e^x(\sin x + \cos x)$$, 곧

$$I = \frac{e^x(\sin x + \cos x)}{2} + C$$

이다.

</div>

분모가 인수분해되는 유리함수는 부분분수로 분해하면 각 조각이 로그·역탄젠트로 적분된다. 예컨대 

$$\frac{1}{x^2-1} = \frac{1}{2}\left(\frac{1}{x-1} - \frac{1}{x+1}\right)$$

로 가르면 

$$\int \frac{dx}{x^2 - 1} = \frac{1}{2}\ln\left\lvert\frac{x-1}{x+1}\right\rvert + C$$

이고, 분모에 기약 이차식이 있으면 완전제곱으로 묶어 

$$\int \frac{dx}{x^2 + 2x + 5} = \frac{1}{2}\arctan\frac{x+1}{2} + C$$

처럼 역탄젠트를 활용하면 된다. 

$$\sqrt{a^2 - x^2}$$, $$\sqrt{a^2 + x^2}$$ 같은 무리식은 삼각함수로 치환하면 무리식이 사라진다. 가령 $$\int \sqrt{1 - x^2} dx$$에서 $$x = \sin\theta$$로 두면

$$\int \cos^2\theta d\theta = \frac{1}{2}(\arcsin x + x\sqrt{1-x^2}) + C$$

를 얻는다. 삼각함수 자체의 거듭제곱은 항등식으로 차수를 낮추거나 치환한다. 홀수 거듭제곱은 하나를 떼어 치환하여

$$\int \sin^3 x dx = -\cos x + \frac{1}{3}\cos^3 x + C$$

처럼 적분하고, 짝수 거듭제곱은 배각공식으로 차수를 낮추어

$$\int \sin^2 x dx = \frac{x}{2} - \frac{\sin 2x}{4} + C$$

를 얻는다.

부분적분을 반복하면 차수를 한 단계씩 낮추는 점화식을 얻어, 거듭제곱이 섞인 적분을 체계적으로 처리한다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (점화식)**</ins> $$I_n = \int x^n e^x dx$$에 $$u = x^n$$, $$v' = e^x$$로 부분적분하면

$$I_n = x^n e^x - n I_{n-1}$$

이다. $$I_0 = e^x$$에서 시작하면

$$I_1 = (x-1)e^x, \quad I_2 = (x^2 - 2x + 2)e^x$$

로 차수를 내려가며 구해진다. 같은 방식으로

$$\int \sin^n x dx = -\frac{1}{n} \sin^{n-1}x\cos x + \frac{n-1}{n}\int \sin^{n-2}x dx$$

라는 점화식도 얻는다.

</div>

이러한 기법으로도 초등함수로 표현되지 않는 적분, 가령 $$\int e^{-x^2} dx$$나 $$\int (\sin x)/x dx$$가 있다. 이런 함수도 정적분으로는 잘 정의되며, 그 자체로 새로운 함수를 정의함은 미적분의 기본정리에서 보게 된다.

## 분할과 리만 합

위에서 살펴본 적분은 미분의 역연산으로 정의되지만, 역사적으로 적분은 다른 방식, 즉 어떠한 양이 누적되었을 때 그 총량을 구하는 문제에서 시작되었다. 예를 들어 곡선 $$y = f(x)$$ 아래, 구간 $$[a,b]$$ 위의 넓이를 재는 문제가 이에 해당한다. 이 구간의 넓이를 직사각형으로 잘게 쪼개어 근사하고, 쪼갬을 한없이 세밀하게 하는 것이 다음 정의의 아이디어다. 

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 닫힌구간 $$[a, b]$$의 *분할<sub>partition</sub>*은 유한개의 점 $$a = x_0 < x_1 < \cdots < x_n = b$$이다. 각 부분구간 $$[x_{i-1}, x_i]$$의 길이를 $$\Delta x_i = x_i - x_{i-1}$$, 가장 긴 부분구간의 길이를 분할의 *너비<sub>mesh</sub>* $$\lVert P\rVert = \max_i \Delta x_i$$라 한다. 각 부분구간에서 표본점 $$c_i \in [x_{i-1}, x_i]$$을 택했을 때

$$S(P, f) = \sum_{i=1}^{n} f(c_i)\Delta x_i$$

를 함수 $$f$$의 *리만 합<sub>Riemann sum</sub>*이라 한다.

</div>

![리만 합](/assets/images/Math/Calculus/Integration-1.svg){:style="width:24.05em" class="invert" .align-center}

리만 합은 곡선 아래 영역을 폭이 $$\Delta x_i$$, 높이가 $$f(c_i)$$인 직사각형들로 근사한 넓이이다. 표본점 $$c_i$$를 각 부분구간의 왼쪽 끝, 오른쪽 끝, 또는 함수의 최솟·최댓값을 주는 점으로 잡으면 각각 좌·우 리만 합, 하합·상합이 된다. 직관적으로, 우리는 분할을 한없이 잘게 하면 이 근사가 표본점 선택과 무관하게 한 값으로 수렴하기를 기대한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 어떤 실수 $$S$$가 존재하여, 임의의 $$\varepsilon > 0$$에 대해 $$\delta > 0$$이 있어 $$\lVert P\rVert < \delta$$인 모든 분할과 표본점의 선택에 대해 $$\lvert S(P, f) - S\rvert < \varepsilon$$이 성립하면, $$f$$가 $$[a,b]$$에서 *적분가능<sub>integrable</sub>*하다고 하고 $$S$$를 *정적분*이라 하여

$$\int_a^b f(x)dx = S$$

로 적는다. $$a$$와 $$b$$를 각각 적분의 아래끝·위끝이라 한다.

</div>

이 정의를 직접 적용해 정적분을 계산할 수 있다. $$[0,1]$$을 $$n$$등분하고 오른쪽 끝점 $$c_i = i/n$$을 택하면, 

$$\int_0^1 xdx$$

의 리만 합은

$$\sum_{i=1}^n \frac{i}{n}\cdot\frac1n = \frac{1}{n^2}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2n} \to \frac12$$

이고, 같은 방식으로

$$\int_0^1 x^2dx = \lim_{n\to\infty}\sum_{i=1}^n \frac{i^2}{n^3} = \lim_{n\to\infty}\frac{n(n+1)(2n+1)}{6n^3} = \frac13$$

이다. 특히 첫째 결과의 경우 삼각형의 넓이공식으로부터 자명하게 검산 또한 가능하다. 

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> $$[a, b]$$에서 연속인 함수는 적분가능하다.

</div>

이 정리의 증명 또한 현재 우리의 범위를 벗어나므로 받아들이고 넘어가야만 한다. 

## 정적분의 성질

한편, 리만 합이 합과 극한으로 정의되므로, 정적분은 다음 성질들을 물려받는다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> $$f, g$$가 $$[a,b]$$에서 적분가능하면 다음이 성립한다.

1. 상수 $$\alpha, \beta$$에 대해 $$\int_a^b (\alpha f(x) + \beta g(x))dx = \alpha\int_a^b f(x)dx + \beta\int_a^b g(x)dx$$.
2. $$a < c < b$$에 대해 $$\int_a^b f(x)dx = \int_a^c f(x)dx + \int_c^b f(x)dx$$.
3. 모든 $$x$$에서 $$f(x) \leq g(x)$$이면 $$\int_a^b f(x)dx \leq \int_a^b g(x)dx$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

세 성질 모두 리만 합 수준에서 성립하고 극한으로 보존된다. 선형성은 $$S(P, \alpha f + \beta g) = \alpha S(P, f) + \beta S(P, g)$$에서, 단조성은 $$f(c_i) \leq g(c_i)$$이면 $$S(P, f) \leq S(P, g)$$에서 따른다. 구간가법성은 $$c$$를 분점으로 포함하는 분할들만 생각하면 리만 합이 두 구간의 리만 합으로 갈라짐에서 얻는다.

</details>

관례적으로 $$\int_a^a f(x)dx = 0$$, 그리고 $$\int_b^a f(x)dx = -\int_a^b f(x)dx$$로 두면 구간가법성은 $$a, b, c$$의 대소에 무관하게 성립한다. 단조성으로부터 두 가지 유용한 계산이 따라온다. 첫째, $$m \leq f \leq M$$이면

$$m(b-a) \leq \int_a^b f(x)dx \leq M(b-a)$$

이다. 둘째, $$-\lvert f\rvert \leq f \leq \lvert f\rvert$$에 적용하면 삼각부등식의 적분판

$$\left\lvert \int_a^b f(x)dx\right\rvert  \leq \int_a^b \lvert f(x)\rvert dx$$

을 얻는다. 첫 부등식을 연속함수에 적용하면, 적분값이 어떤 점에서의 함숫값에 의해 정확히 달성됨을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12 (적분의 평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이면 

$$\int_a^b f(x)dx = f(c)(b-a)$$

를 만족하는 $$c \in [a,b]$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)로 $$f$$는 $$[a,b]$$에서 최솟값 $$m$$과 최댓값 $$M$$을 가진다. 위 계산에서 평균값 

$$\frac{1}{b-a}\int_a^b f(x)dx$$

가 $$[m, M]$$에 속하므로, [§연속함수, ⁋정리 5](/ko/math/calculus/continuity#thm5)에 의해 그 값을 취하는 $$c$$, 즉 $$f(c) = \frac{1}{b-a}\int_a^b f(x)dx$$인 $$c$$가 존재한다.

</details>

여기서 

$$\frac{1}{b-a}\int_a^b f(x)dx$$

를 $$f$$의 $$[a,b]$$에서의 *평균값*이라 하며, [명제 12](#prop12)은 연속함수가 자신의 평균값을 적어도 한 점에서 실제로 취함을 말한다.

## 넓이와 응용

정적분은 <em-ko>부호가 있는</em-ko> 넓이로 이해하는 것이 가장 직관적이다. 가령 $$f < 0$$인 구간에서는 리만 합의 항 $$f(c_i)\Delta x_i$$가 음수이므로, $$\int_a^b f(x)dx$$는 $$x$$축과 $$f$$로 둘러싸인 영역에 마이너스 부호를 붙여준 것이다. 이 관점은 적분 구간 위에서 함수의 부호가 바뀔 때 특히 분명해지며, 한 적분이 양·음의 넓이를 상쇄하여 $$0$$이 되는 경우와 실제 넓이가 절댓값을 요구하는 경우를 가르는 데서 위에서 살펴본 삼각부등식의 적분판이 진부등호로 나타난다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $$\int_{-1}^{1} xdx = 0$$인 까닭은 $$[-1,0]$$에서의 음의 넓이와 $$[0,1]$$에서의 양의 넓이가 정확히 상쇄되기 때문이다. 각 조각은 밑변과 높이가 $$1$$인 직각삼각형이라 넓이가 $$\frac{1}{2}$$이고, [명제 11](#prop11)의 둘째 결과를 사용해 갈라 쓰면

$$\int_{-1}^{1} xdx = \int_{-1}^{0} xdx + \int_{0}^{1} xdx = -\frac{1}{2} + \frac{1}{2} = 0$$

이다. 곡선과 $$x$$축이 둘러싼 *실제* 넓이를 원한다면 부호를 지운 $$\lvert x\rvert$$를 적분해야 하며,

$$\int_{-1}^{1} \lvert x\rvert dx = \int_{-1}^{0} (-x)dx + \int_{0}^{1} xdx = \frac{1}{2} + \frac{1}{2} = 1$$

이 된다. 이는 삼각부등식의 적분판 $$\bigl\lvert\int f\bigr\rvert \leq \int \lvert f\rvert$$이 등호가 아니라 부등호 $$0 < 1$$로 성립하는 구체적 사례이며, 각 조각의 값은 삼각형 넓이로 곧바로 확인된다. 이 계산은 앞서 리만 합으로 삼각형의 넓이를 구한 것과도 일치한다. 

</div>

평균값 정리는 적분을 한 점에서의 함숫값으로 바꾸어 주므로, 부등식을 다루거나 평균적 거동을 추론할 때 자주 쓰인다. 가중치를 곱한 적분에 대해서도, 가중치의 부호가 일정하기만 하면 같은 정리가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (가중 평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$\mu$$가 $$[a,b]$$에서 적분가능하며 $$\mu \geq 0$$이라면, 어떤 $$c \in [a,b]$$가 존재하여 

$$\int_a^b f(x)\mu(x)dx = f(c)\int_a^b \mu(x)dx$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)로 $$f$$는 최솟값 $$m$$과 최댓값 $$M$$을 가진다. $$\mu \geq 0$$이므로 $$m\mu(x) \leq f(x)\mu(x) \leq M\mu(x)$$이고, 단조성과 선형성으로 적분하면

$$m\int_a^b \mu(x)dx \leq \int_a^b f(x)\mu(x) dx\leq M\int_a^b \mu(x) dx$$

를 얻는다. 만약 $$\int_a^b \mu(x)dx = 0$$이면 가운데 적분도 $$0$$이라 임의의 $$c$$로 등식이 성립한다. $$\int_a^b \mu(x)dx > 0$$이면 위 부등식을 그 값으로 나누어 

$$\frac{\int_a^b f(x)\mu(x) dx}{\int_a^b \mu(x)dx} \in [m, M]$$

임을 얻고, [§연속함수, ⁋정리 5](/ko/math/calculus/continuity#thm5)로 이 값을 취하는 $$c$$가 존재한다. 따라서 여기에 $$\int_a^b \mu(x)dx$$를 곱하면 증명이 완료된다.

</details>

만일 $$\mu \equiv 1$$로 두면 가중 평균값 정리는 [명제 12](#prop12)로 환원되므로, [명제 14](#prop14)은 평균값 정리의 일반화로, 일종의 밀도를 추가하는 것으로 생각할 수 있다.
