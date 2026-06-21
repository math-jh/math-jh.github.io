---
title: "정적분"
description: "정적분을 분할 위의 리만 합의 극한으로 정의하고, 연속함수가 적분가능함을 받아들인 뒤 선형성·구간가법성·단조성과 적분의 평균값 정리를 다룬다. 부호 있는 넓이로서의 의미와 넓이·부피 응용을 본다."
excerpt: "분할과 리만 합, 정적분의 정의, 적분의 성질, 평균값 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/definite_integral
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 12

published: false
---

[§부정적분](/ko/math/calculus/antiderivatives)은 미분의 역연산이었다. 정적분은 그와 전혀 다른 동기 — 곡선 아래의 넓이, 누적된 양 — 에서 출발한다. 이 글에서는 먼저 정적분을 넓이의 근사라는 직관에 충실하게 정의하고, 그 기본 성질을 정리한다.

## 분할과 리만 합

곡선 $$y = f(x)$$ 아래, 구간 $$[a,b]$$ 위의 넓이를 어떻게 잴 것인가? 직사각형으로 잘게 쪼개어 근사하고, 쪼갬을 한없이 세밀하게 하는 것이 리만의 착상이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 닫힌구간 $$[a, b]$$의 *분할<sub>partition</sub>*은 유한개의 점 $$a = x_0 < x_1 < \cdots < x_n = b$$이다. 각 부분구간 $$[x_{i-1}, x_i]$$의 길이를 $$\Delta x_i = x_i - x_{i-1}$$, 가장 긴 부분구간의 길이를 분할의 *너비<sub>mesh</sub>* $$\lVert P\rVert = \max_i \Delta x_i$$라 한다. 각 부분구간에서 표본점 $$c_i \in [x_{i-1}, x_i]$$을 택했을 때

$$S(P, f) = \sum_{i=1}^{n} f(c_i)\,\Delta x_i$$

를 함수 $$f$$의 *리만 합<sub>Riemann sum</sub>*이라 한다.

</div>

리만 합은 곡선 아래 영역을 폭이 $$\Delta x_i$$, 높이가 $$f(c_i)$$인 직사각형들로 근사한 넓이이다. 표본점 $$c_i$$를 각 부분구간의 왼쪽 끝, 오른쪽 끝, 또는 함수의 최솟·최댓값을 주는 점으로 잡으면 각각 좌·우 리만 합, 하합·상합이 된다. 분할을 한없이 잘게 하면($$\lVert P\rVert \to 0$$) 이 근사가 표본점 선택과 무관하게 한 값으로 수렴하기를 기대한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 어떤 실수 $$I$$가 존재하여, 임의의 $$\varepsilon > 0$$에 대해 $$\delta > 0$$이 있어 $$\lVert P\rVert < \delta$$인 모든 분할과 표본점의 선택에 대해 $$\lvert S(P, f) - I\rvert < \varepsilon$$이 성립하면, $$f$$가 $$[a,b]$$에서 *적분가능<sub>integrable</sub>*하다고 하고 $$I$$를 *정적분*이라 하여

$$\int_a^b f(x)\,dx = I$$

로 적는다. $$a$$와 $$b$$를 각각 적분의 아래끝·위끝이라 한다.

</div>

이 정의를 직접 적용해 정적분을 계산할 수 있다. $$[0,1]$$을 $$n$$등분하고 오른쪽 끝점 $$c_i = i/n$$을 택하면, $$\displaystyle\int_0^1 x\,dx$$의 리만 합은

$$\sum_{i=1}^n \frac{i}{n}\cdot\frac1n = \frac{1}{n^2}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2n} \to \frac12$$

이고, 같은 방식으로 $$\displaystyle\int_0^1 x^2\,dx = \lim_{n\to\infty}\sum_{i=1}^n \frac{i^2}{n^3} = \lim_{n\to\infty}\frac{n(n+1)(2n+1)}{6n^3} = \frac13$$이다.

모든 함수가 적분가능하지는 않다. 유리수에서 $$1$$, 무리수에서 $$0$$인 디리클레 함수는 어떤 부분구간에서도 상합이 $$1$$, 하합이 $$0$$이라 리만 합이 표본점에 따라 $$0$$과 $$1$$ 사이를 오가므로 한 값으로 모이지 않아 적분 불가능하다. 그러나 우리가 다루는 함수 대부분은 적분가능하다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$[a, b]$$에서 연속인 함수는 적분가능하다.

</div>

이 정리의 증명은 연속함수가 닫힌구간에서 균등연속이라는 사실에 기대며, 그 엄밀한 논증은 실수의 완비성을 본격적으로 사용하는 해석학 [\[해석학\] §Riemann 적분](/ko/math/analysis/riemann_integral)에서 다룬다. 여기서는 이를 도구로 받아들인다. 연속성을 완화하여 유한개의 점에서만 불연속인 유계함수, 가령 조각마다 연속인 함수도 적분가능하므로, 실용에서 마주치는 함수는 거의 모두 적분가능하다고 보아도 좋다.

## 정적분의 성질

리만 합이 합과 극한으로 정의되므로, 정적분은 다음 성질들을 물려받는다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$f, g$$가 $$[a,b]$$에서 적분가능하면 다음이 성립한다.

1. (선형성) 상수 $$\alpha, \beta$$에 대해 $$\displaystyle\int_a^b (\alpha f + \beta g) = \alpha\int_a^b f + \beta\int_a^b g$$.
2. (구간가법성) $$a < c < b$$에 대해 $$\displaystyle\int_a^b f = \int_a^c f + \int_c^b f$$.
3. (단조성) 모든 $$x$$에서 $$f(x) \leq g(x)$$이면 $$\displaystyle\int_a^b f \leq \int_a^b g$$.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

세 성질 모두 리만 합 수준에서 성립하고 극한으로 보존된다. 선형성은 $$S(P, \alpha f + \beta g) = \alpha S(P, f) + \beta S(P, g)$$에서, 단조성은 $$f(c_i) \leq g(c_i)$$이면 $$S(P, f) \leq S(P, g)$$에서 따른다. 구간가법성은 $$c$$를 분점으로 포함하는 분할들만 생각하면 리만 합이 두 구간의 리만 합으로 갈라짐에서 얻는다.

</details>

관례적으로 $$\int_a^a f = 0$$, 그리고 $$\int_b^a f = -\int_a^b f$$로 두면 구간가법성은 $$a, b, c$$의 대소에 무관하게 성립한다. 단조성으로부터 두 가지 유용한 평가가 따른다. 첫째, $$m \leq f \leq M$$이면

$$m(b-a) \leq \int_a^b f \leq M(b-a)$$

이다. 둘째, $$-\lvert f\rvert \leq f \leq \lvert f\rvert$$에 적용하면 삼각부등식의 적분판

$$\left\lvert \int_a^b f\right\rvert \leq \int_a^b \lvert f\rvert$$

을 얻는다. 첫 평가를 연속함수에 적용하면, 적분값이 어떤 점에서의 함숫값에 의해 정확히 달성됨을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (적분의 평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이면 $$\displaystyle\int_a^b f(x)\,dx = f(c)\,(b-a)$$를 만족하는 $$c \in [a,b]$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

최대·최소 정리 ([§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4))로 $$f$$는 $$[a,b]$$에서 최솟값 $$m$$과 최댓값 $$M$$을 가진다. 위 평가에서 평균값 $$\dfrac{1}{b-a}\int_a^b f$$가 $$[m, M]$$에 속하므로, 중간값 정리 ([§연속함수, ⁋정리 5](/ko/math/calculus/continuity#thm5))에 의해 그 값을 취하는 $$c$$, 즉 $$f(c) = \dfrac{1}{b-a}\int_a^b f$$인 $$c$$가 존재한다.

</details>

여기서 $$\dfrac{1}{b-a}\int_a^b f$$를 $$f$$의 $$[a,b]$$에서의 *평균값*이라 하며, 명제 5는 연속함수가 자신의 평균값을 적어도 한 점에서 실제로 취함을 말한다.

## 넓이와 응용

정적분은 "넓이"이되 *부호 있는 넓이*이다. $$f < 0$$인 구간에서는 리만 합의 항 $$f(c_i)\Delta x_i$$가 음수이므로, $$\int_a^b f$$는 $$x$$축 위쪽 넓이에서 아래쪽 넓이를 뺀 값이다. 가령 $$\int_0^{2\pi}\sin x\,dx = 0$$이다. 이 부호 규약 덕분에 정적분은 단순한 넓이를 넘어 누적된 양 — 변위, 일, 질량, 확률 — 을 통일적으로 나타내며, 응용에서 곧장 확장된다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (평균값)**</ins> $$f(x) = x^2$$의 $$[0, 3]$$에서의 평균값은 $$\dfrac{1}{3 - 0}\int_0^3 x^2\,dx = \dfrac13\cdot 9 = 3$$이다 (다음 글의 평가정리로 $$\int_0^3 x^2 = 9$$). 명제 5에 따르면 $$f(c) = 3$$, 곧 $$c = \sqrt3 \in [0,3]$$에서 평균값이 실제로 달성된다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (두 곡선 사이 넓이)**</ins> $$[a,b]$$에서 $$f \geq g$$일 때 두 곡선 사이의 넓이는 단조성과 선형성에 의해 $$\displaystyle\int_a^b \bigl(f(x) - g(x)\bigr)\,dx$$이다. 예로 $$y = x$$와 $$y = x^2$$이 $$[0,1]$$에서 이루는 넓이는 $$\displaystyle\int_0^1 (x - x^2)\,dx = \tfrac12 - \tfrac13 = \tfrac16$$이다. 마찬가지로 $$y = f(x)$$를 $$x$$축 둘레로 회전시킨 회전체의 부피는 단면이 반지름 $$f(x)$$인 원이므로 $$\displaystyle\int_a^b \pi f(x)^2\,dx$$로 주어진다.

</div>

## 예시와 계산

정의 2를 곧이곧대로 적용하여 리만 합의 극한을 직접 계산하는 일은 대체로 번거롭다. 그러나 그 과정을 한 번 끝까지 밀어붙여 보는 것은, 정적분이 무엇을 재는지를 손으로 확인하는 좋은 연습이 된다. 먼저 거듭제곱 함수를 같은 길이의 부분구간으로 분할하여 직접 계산한다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (세제곱의 정적분)**</ins> $$\displaystyle\int_0^1 x^3\,dx$$를 정의로 계산하자. $$[0,1]$$을 $$n$$등분하면 $$\Delta x_i = 1/n$$이고, 오른쪽 끝점 $$c_i = i/n$$을 표본점으로 택한다. 이때 너비는 $$\lVert P\rVert = 1/n \to 0$$이다. 거듭제곱 합 공식 $$\displaystyle\sum_{i=1}^n i^3 = \left(\frac{n(n+1)}{2}\right)^2$$를 쓰면 리만 합은

$$\begin{aligned}
S(P, f) &= \sum_{i=1}^n \left(\frac{i}{n}\right)^3 \cdot \frac1n \\
&= \frac{1}{n^4}\sum_{i=1}^n i^3 \\
&= \frac{1}{n^4}\cdot \frac{n^2(n+1)^2}{4} \\
&= \frac{(n+1)^2}{4n^2} = \frac14\left(1 + \frac1n\right)^2
\end{aligned}$$

이고, $$n \to \infty$$에서 $$\displaystyle\int_0^1 x^3\,dx = \frac14$$를 얻는다. 정리 3이 보장하는 적분가능성 덕분에, 우리는 표본점을 오른쪽 끝점으로 편하게 고정해도 같은 극한값에 도달함을 안다.

</div>

표본점 선택과 무관하게 같은 값으로 수렴한다는 점은 정의 2의 핵심이며, 다음 예시는 같은 적분을 왼쪽 끝점으로 계산해도 결과가 변하지 않음을 보여 준다. 이는 적분가능한 함수에 대해 좌·우 리만 합의 차이가 분할을 잘게 할수록 사라짐을 반영한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (표본점의 무관함)**</ins> 같은 분할에서 왼쪽 끝점 $$c_i = (i-1)/n$$을 택하면

$$\begin{aligned}
S(P, f) &= \sum_{i=1}^n \left(\frac{i-1}{n}\right)^3 \cdot \frac1n \\
&= \frac{1}{n^4}\sum_{j=0}^{n-1} j^3 \\
&= \frac{1}{n^4}\cdot \frac{(n-1)^2 n^2}{4} \\
&= \frac14\left(1 - \frac1n\right)^2
\end{aligned}$$

이다. 오른쪽 끝점이 준 $$\frac14(1 + 1/n)^2$$과 비교하면 두 합의 차이는

$$\frac14\left[\left(1+\tfrac1n\right)^2 - \left(1-\tfrac1n\right)^2\right] = \frac14\cdot \frac{4}{n} = \frac1n \to 0$$

이어서, 두 합 모두 같은 극한 $$\frac14$$로 수렴한다. 일반적으로 단조함수에서는 좌·우 리만 합이 각각 하합·상합(또는 그 반대)이 되며, 그 차이는 $$\lvert f(b) - f(a)\rvert\,\lVert P\rVert$$로 위에서 눌려 $$0$$으로 간다.

</div>

부호 있는 넓이라는 관점은 적분 구간 위에서 함수의 부호가 바뀔 때 특히 분명해진다. 다음 예시는 한 적분이 양·음의 넓이를 상쇄하여 0이 되는 경우와, 실제 넓이를 구하려면 절댓값을 씌워야 하는 경우를 대비한다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (부호 있는 넓이와 실제 넓이)**</ins> $$\displaystyle\int_0^{2\pi}\sin x\,dx = 0$$인 까닭은 $$[0,\pi]$$에서의 양의 넓이와 $$[\pi, 2\pi]$$에서의 음의 넓이가 정확히 상쇄되기 때문이다. 구간가법성(명제 4)으로 갈라 쓰면

$$\int_0^{2\pi}\sin x\,dx = \int_0^{\pi}\sin x\,dx + \int_{\pi}^{2\pi}\sin x\,dx = 2 + (-2) = 0$$

이다 (각 조각의 값은 다음 글의 기본정리로 $$\int_0^\pi \sin = 2$$). 곡선과 $$x$$축이 둘러싼 *실제* 넓이를 원한다면 부호를 지운 $$\lvert\sin x\rvert$$를 적분해야 하며,

$$\int_0^{2\pi}\lvert \sin x\rvert\,dx = \int_0^{\pi}\sin x\,dx - \int_{\pi}^{2\pi}\sin x\,dx = 2 + 2 = 4$$

가 된다. 이는 삼각부등식의 적분판 $$\bigl\lvert\int f\bigr\rvert \leq \int \lvert f\rvert$$이 등호가 아니라 진부등호 $$0 < 4$$로 성립하는 구체적 사례이기도 하다.

</div>

명제 4의 단조성에서 따라 나온 상·하한 평가 $$m(b-a) \leq \int_a^b f \leq M(b-a)$$는, 적분을 정확히 계산하지 않고도 그 크기를 거칠게 가두는 데 유용하다. 다음 예시는 이 평가만으로 적분값의 범위를 결정하는 방법을 보인다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (적분의 상·하한 평가)**</ins> $$\displaystyle I = \int_0^1 \frac{dx}{1 + x^4}$$를 생각하자. $$[0,1]$$에서 $$0 \leq x^4 \leq 1$$이므로 $$1 \leq 1 + x^4 \leq 2$$, 따라서 피적분함수는

$$\frac12 \leq \frac{1}{1 + x^4} \leq 1$$

을 만족한다. 단조성을 이 부등식의 세 변에 적용하면

$$\int_0^1 \frac12\,dx \leq I \leq \int_0^1 1\,dx, \qquad \text{즉} \quad \frac12 \leq I \leq 1$$

을 얻는다. 적분의 평균값 정리(명제 5)에 비추면, 연속함수 $$\frac{1}{1+x^4}$$는 $$[0,1]$$의 어떤 점 $$c$$에서 정확히 자신의 평균값 $$I$$를 취하며, 그 값은 위 두 끝값 사이에 놓인다.

</div>

평균값 정리는 적분을 한 점에서의 함숫값으로 바꾸어 주므로, 부등식을 다루거나 평균적 거동을 추론할 때 자주 쓰인다. 다음 예시는 부호가 일정하지 않은 가중치를 곱한 적분에 평균값 정리의 일반화된 형태를 적용한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12 (가중 평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$g$$가 $$[a,b]$$에서 적분가능하며 부호가 일정($$g \geq 0$$)하면, 어떤 $$c \in [a,b]$$가 존재하여 $$\displaystyle\int_a^b f(x)g(x)\,dx = f(c)\int_a^b g(x)\,dx$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

최대·최소 정리로 $$f$$는 최솟값 $$m$$과 최댓값 $$M$$을 가진다. $$g \geq 0$$이므로 $$m\,g(x) \leq f(x)g(x) \leq M\,g(x)$$이고, 단조성과 선형성으로 적분하면

$$m\int_a^b g \leq \int_a^b fg \leq M\int_a^b g$$

를 얻는다. 만약 $$\int_a^b g = 0$$이면 가운데 적분도 $$0$$이라 임의의 $$c$$로 등식이 성립한다. $$\int_a^b g > 0$$이면 위 부등식을 그 값으로 나누어 $$\dfrac{\int_a^b fg}{\int_a^b g} \in [m, M]$$임을 얻고, 중간값 정리로 이 값을 취하는 $$c$$, 즉 $$f(c) = \dfrac{\int_a^b fg}{\int_a^b g}$$인 $$c$$가 존재한다. 양변에 $$\int_a^b g$$를 곱하면 주장이 따른다.

</details>

$$g \equiv 1$$로 두면 가중 평균값 정리는 명제 5로 환원되므로, 명제 12는 평균값 정리의 진정한 일반화이다. 마지막으로, 두 곡선 사이의 넓이와 회전체의 부피를 구하는 예시 7의 공식을 구체적인 함수에 적용하여 끝맺는다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13 (회전체의 부피)**</ins> $$y = \sqrt{x}$$를 $$[0,1]$$에서 $$x$$축 둘레로 회전시킨 회전체의 부피는 예시 7의 공식 $$\int_a^b \pi f(x)^2\,dx$$에서 $$f(x)^2 = x$$이므로

$$V = \int_0^1 \pi\bigl(\sqrt{x}\bigr)^2\,dx = \pi\int_0^1 x\,dx = \pi\cdot \frac12 = \frac{\pi}{2}$$

이다 (정의로 계산한 $$\int_0^1 x = \tfrac12$$을 사용했다). 같은 방식으로 반지름 $$r$$인 반원 $$y = \sqrt{r^2 - x^2}$$를 $$[-r, r]$$에서 회전시키면

$$V = \int_{-r}^{r}\pi\bigl(r^2 - x^2\bigr)\,dx = \pi\left[r^2\int_{-r}^r dx - \int_{-r}^r x^2\,dx\right]$$

가 되고, $$\int_{-r}^r dx = 2r$$과 $$\int_{-r}^r x^2\,dx = \tfrac23 r^3$$를 넣으면 $$V = \pi\bigl(2r^3 - \tfrac23 r^3\bigr) = \tfrac43\pi r^3$$, 곧 반지름 $$r$$인 구의 부피가 나온다.

</div>


## 멱급수의 항별 적분

멱급수는 수렴요경 안에서 항별로 적분할 수도 있다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14 (멱급수의 항별 적분)**</ins> $$f(x) = \sum_{n=0}^\infty c_n x^n$$이 수렴요경 $$R > 0$$을 가지면, $$\lvert x\rvert < R$$에서

$$\int_0^x f(t)\,dt = \sum_{n=0}^\infty \frac{c_n}{n+1} x^{n+1}$$

이고, 이 급수의 수렴요경도 $$R$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex15">**예시 15 (로그와 역탄젠트)**</ins> 기하급수 $$\dfrac{1}{1 - x} = \sum_{n=0}^\infty x^n$$ ($$\lvert x\rvert < 1$$) 을 항별 적분하면

$$-\ln(1 - x) = \sum_{n=1}^\infty \frac{x^n}{n} \quad\Longrightarrow\quad \ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n$$

을 얻고, $$\dfrac{1}{1 + x^2} = \sum_{n=0}^\infty (-1)^n x^{2n}$$을 항별 적분하면

$$\arctan x = \sum_{n=0}^\infty \frac{(-1)^n}{2n+1} x^{2n+1}$$

을 얻는다.

</div>
