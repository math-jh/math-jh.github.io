---
title: "미분과 도함수"
description: "함수의 순간변화율인 미분계수를 극한으로 정의하고, 미분가능성이 연속성을 함의함을 보인다. 도함수와 고계도함수, 선형 근사로서의 미분, 그리고 미분가능성과 매끄러움의 위계를 정리한다."
excerpt: "미분계수의 정의, 미분가능성과 연속성, 도함수와 고계도함수"

categories: [Math / Calculus]
permalink: /ko/math/calculus/derivatives
sidebar: 
    nav: "calculus-ko"

date: 2026-06-02
weight: 6

published: false
---

우리는 [§연속함수](/ko/math/calculus/continuity)에서 함수가 연속이라는 것을 앞서 도입한 $$\epsilon-\delta$$의 언어로 재정립했다. 이제 자연스러운 흐름은 함수의 미분을 정의하는 것이다.

## 미분계수의 정의

두 점 $$(a, f(a))$$와 $$(x, f(x))$$를 잇는 직선의 기울기는 평균변화율 $$\frac{f(x) - f(a)}{x - a}$$이며, 이 때 $$x$$를 $$a$$로 보내는 극한을 취하면 미분계수를 얻는다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f$$가 점 $$a$$에서 *미분가능<sub>differentiable</sub>*하다는 것은 극한

$$f'(a) := \lim_{x \to a} \frac{f(x) - f(a)}{x - a} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

이 존재하는 것이다. 이 값 $$f'(a)$$를 $$f$$의 $$a$$에서의 *미분계수<sub>derivative</sub>*라 부른다. $$f$$가 정의역의 모든 점에서 미분가능하면, $$a \mapsto f'(a)$$로 정의되는 함수 $$f'$$를 $$f$$의 *도함수<sub>derivative function</sub>*라 한다.

</div>

두 표현은, 당연히, $$x=a+h$$로 두면 같은 것임이 자명하며, 위의 평균변화율에 대한 논의에 의해 미분계수 $$f'(a)$$는 점 $$(a, f(a))$$에서 그래프에 그은 접선의 기울기이다. 한편 임의의 직선은 기울기와 그 위의 한 점에 의해 완벽하게 결정되며, 특히 이 접선은 $$(a,f(a))$$를 지난다는 것이 이미 주어진 것이므로 점 $$a$$에서 미분가능한 함수의 접선은

$$y = f(a) + f'(a)(x - a)$$

로 주어진다. 이 일차함수는 $$a$$ 근방에서 $$f$$를 가장 잘 근사하여, $$h$$가 작을 때 $$f(a+h) \approx f(a) + f'(a)h$$로 쓴다. 도함수는 라이프니츠를 따라 

$$\frac{df}{dx},\qquad \frac{d}{dx}f$$ 

등으로도 적지만, 미적분학에서는 $$f'$$ 표기로 충분할 때가 많다. 

정의를 직접 적용하면, 가령 $$f(x) = x^2$$의 차분몫은 $$\dfrac{(a+h)^2 - a^2}{h} = 2a + h$$이므로 $$f'(a) = 2a$$이고, 상수함수의 도함수는 항상 $$0$$이다. 같은 방식으로 $$f(x) = 1/x$$ ($$x \neq 0$$) 는 차분몫을 통분하여 $$f'(a) = -1/a^2$$을, $$f(x) = \sqrt x$$ ($$x > 0$$) 는 분자를 유리화하여 $$f'(a) = 1/(2\sqrt a)$$을 준다.

## 미분가능성과 연속성

미분가능은 연속보다 강한 조건이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$f$$가 $$a$$에서 미분가능하면 $$f$$는 $$a$$에서 연속이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x \neq a$$에서 

$$f(x) - f(a) = \frac{f(x)-f(a)}{x-a}\cdot(x-a)$$

이다. $$x \to a$$일 때 우변의 첫 인자는 $$f'(a)$$로, 둘째 인자는 $$0$$으로 수렴하므로, [§함수의 극한, ⁋명제 5](/ko/math/calculus/functions_and_limits#prop5)에 의해 

$$\lim_{x\to a}\bigl(f(x)-f(a)\bigr) = f'(a)\cdot 0 = 0$$

이다. 따라서 $$f$$는 $$a$$에서 연속이다.

</details>

그러나 그 역은 성립하지 않는다. 대표적인 예가 $$f(x) = \lvert x\rvert$$로, 이 함수는 $$0$$에서 연속이지만 미분가능하지 않다. 

![절댓값함수의 그래프](/assets/images/Math/Calculus/Derivatives-1.svg){:style="width:11.21em" class="invert" .align-center}

실제로 

$$\frac{f(h)-f(0)}{h} = \frac{\lvert h\rvert}{h}=\begin{cases}1&\text{if $h>0$}\\-1&\text{if $h<0$}\end{cases}$$

이므로, 이 함수의 미분계수는 $$h \to 0^+$$일 때 $$1$$, $$h \to 0^-$$일 때 $$-1$$로, 한쪽 극한이 서로 달라 극한이 존재하지 않는다. 

비슷한 예시로, $$f(x) = \sqrt[3]{x}$$는 $$0$$에서 차분몫이 $$h^{-2/3} \to \infty$$로 발산하는 *수직접선<sub>vertical tangent</sub>*을 갖는다.

![세제곱근함수의 수직접선](/assets/images/Math/Calculus/Derivatives-2.svg){:style="width:12.46em" class="invert" .align-center}

이를 $$f(x) = x^{2/3}$$는 $$0$$에서 좌우 차분몫이 $$\mp\infty$$로 갈라지는 *첨점<sub>cusp</sub>*을 이룬다.

![2/3제곱함수의 첨점](/assets/images/Math/Calculus/Derivatives-3.svg){:style="width:13.17em" class="invert" .align-center}

거꾸로 미분가능성은 한 점에서만 성립할 수도 있는 국소적 성질이어서, 다음과 같은 형태의 극단적인 예시도 가능하다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (한 점에서만 미분가능한 함수)**</ins> 함수

$$f(x) = \begin{cases} x^2 & (x \in \mathbb{Q}) \\ 0 & (x \notin \mathbb{Q}) \end{cases}$$

를 보자. $$a \neq 0$$에서는 $$a$$에 수렴하는 유리수열과 무리수열을 따라 함숫값이 각각 $$a^2$$과 $$0$$으로 갈라지므로 $$f$$는 불연속이고, 명제 2의 대우에 의해 미분가능하지 않다. 반면 $$0$$에서는 $$\lvert f(x)\rvert \leq x^2$$이라 연속이며, 차분몫이

$$\left\lvert \frac{f(x) - f(0)}{x - 0} \right\rvert = \frac{\lvert f(x)\rvert}{\lvert x\rvert} \leq \lvert x\rvert \to 0$$

이므로 $$f'(0) = 0$$이 존재한다. 즉 $$f$$는 오직 $$0$$에서만 미분가능하다. 미분가능성이 한 점에서의 연속성만을 동반할 뿐, 근방 전체의 규칙성과는 무관함을 본다.

</div>

## 미분의 선형성과 기본 공식

도함수는 극한이므로, 극한의 선형성으로부터 미분도 선형 연산임을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (미분의 선형성)**</ins> $$f, g$$가 $$a$$에서 미분가능하고 $$c$$가 상수이면, $$f + g$$와 $$cf$$도 $$a$$에서 미분가능하고

$$(f+g)'(a) = f'(a) + g'(a), \qquad (cf)'(a) = c\,f'(a)$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

차분몫이 $$\dfrac{(f+g)(a+h)-(f+g)(a)}{h} = \dfrac{f(a+h)-f(a)}{h} + \dfrac{g(a+h)-g(a)}{h}$$로 갈라지고, 각 항이 $$f'(a), g'(a)$$로 수렴하므로 극한법칙에 의해 합도 수렴한다. $$cf$$도 차분몫이 $$c\cdot\dfrac{f(a+h)-f(a)}{h}$$이므로 마찬가지이다.

</details>

거듭제곱함수의 도함수는 다음과 같다: 자연수 $$n$$에 대해 $$\dfrac{d}{dx}x^n = n x^{n-1}$$이다. 이는 $$\dfrac{(x+h)^n - x^n}{h}$$를 이항정리로 전개하면 $$nx^{n-1} + \binom n2 x^{n-2}h + \cdots$$이 되고, $$h \to 0$$일 때 첫 항만 남기 때문이다. 이 공식과 선형성을 결합하면 임의의 다항함수의 도함수를 즉시 계산할 수 있다. 예를 들어 $$\dfrac{d}{dx}(3x^4 - 5x + 2) = 12x^3 - 5$$이다.

## 고계도함수와 매끄러움

도함수 $$f'$$도 다시 함수이므로, 그것이 미분가능하면 또 미분할 수 있다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$f$$의 도함수 $$f'$$이 미분가능하면 그 도함수를 *이계도함수* $$f'' = (f')'$$라 한다. 이를 반복하여 $$n$$번 미분한 것을 *$$n$$계도함수* $$f^{(n)}$$이라 하며, $$f^{(0)} = f$$로 둔다. 어떤 구간에서 $$f^{(n)}$$이 존재하고 연속이면 $$f$$가 그 구간에서 *$$C^n$$급*이라 하고, 모든 계의 도함수가 존재하면 *$$C^\infty$$급* 또는 *매끄럽다<sub>smooth</sub>*고 한다.

</div>

이계도함수 $$f''$$은 변화율의 변화율로, $$f$$가 위치라면 $$f''$$은 가속도이다. 또 $$f''$$의 부호는 그래프가 굽는 방향(볼록·오목)을 알려 준다. 다항함수는 매끄럽고, $$\sin, \cos, \exp$$도 매끄럽다. 특히 $$n$$차 다항식은 미분할 때마다 차수가 하나씩 떨어져 $$(n+1)$$계도함수부터 항등적으로 $$0$$이다. 반면 $$C^n$$급이지만 $$C^{n+1}$$급은 아닌 함수도 있어 위계는 진짜로 층을 이룬다: 가령 $$f(x) = x\lvert x\rvert$$는 $$f'(x) = 2\lvert x\rvert$$로 $$C^1$$급이지만 $$f''$$이 $$0$$에서 존재하지 않아 $$C^2$$급은 아니다.

위계의 틈은 더 미세한 곳에도 있다. 함수가 어디서나 미분가능하더라도 그 도함수가 연속이 아닐 수 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 (미분가능하지만 $$C^1$$급이 아닌 함수)**</ins> 함수

$$f(x) = \begin{cases} x^2 \sin(1/x) & (x \neq 0) \\ 0 & (x = 0) \end{cases}$$

는 모든 점에서 미분가능하다. $$x \neq 0$$에서는 표준적인 미분 규칙으로 $$f'(x) = 2x\sin(1/x) - \cos(1/x)$$이고, $$0$$에서는 차분몫이 $$\dfrac{x^2 \sin(1/x)}{x} = x\sin(1/x) \to 0$$이므로 $$f'(0) = 0$$이다. 그런데 $$x \to 0$$일 때 $$2x\sin(1/x) \to 0$$이지만 $$\cos(1/x)$$는 $$[-1, 1]$$ 사이를 무한히 진동하여 극한을 갖지 않으므로, $$f'$$은 $$0$$에서 불연속이다. 즉 $$f$$는 어디서나 미분가능하지만 도함수가 연속이 아니어서 $$C^1$$급이 아니다. 미분가능성과 $$C^1$$급 사이에도 틈이 있는 것이다.

</div>

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7 (도함수의 중간값 성질)**</ins> 예시 6은 도함수가 불연속일 수 있음을 보였다. 그럼에도 도함수는 임의의 중간값을 반드시 취한다(*Darboux 정리*). $$f$$가 구간에서 미분가능하고 $$f'(a) < c < f'(b)$$이면 $$g(x) = f(x) - cx$$는 $$g'(a) < 0 < g'(b)$$를 만족하고, $$g$$가 연속이므로 $$[a, b]$$에서 최솟값을 가진다. 이 최솟값은 $$g'(a) < 0$$, $$g'(b) > 0$$ 때문에 양 끝점이 아닌 내부의 한 점 $$\xi$$에서 달성되며, 내부 최솟값에서는 차분몫의 좌우극한이 각각 $$0$$ 이하와 $$0$$ 이상이어야 하므로 $$g'(\xi) = 0$$, 곧 $$f'(\xi) = c$$이다. 따라서 도함수에는 점프 불연속이 생길 수 없고, 예시 6에서처럼 불연속이 나타난다면 그것은 진동에 의한 것이다.

</div>

<div class="remark" markdown="1">

<ins id="rmk8">**참고 8**</ins> 명제 2의 역이 거짓임을 넘어, 연속이지만 *어느 점에서도* 미분 불가능한 함수가 존재한다. 바이어슈트라스가 제시한 $$W(x) = \sum_{n=0}^\infty a^n\cos(b^n\pi x)$$ ($$0 < a < 1$$, $$ab > 1 + \tfrac{3\pi}{2}$$) 가 그 예로, $$\mathbb{R}$$ 전체에서 연속이지만 어디서도 접선을 갖지 않는다. 이는 "연속함수의 그래프는 매끄럽다"는 직관이 틀렸음을 보여 주며, 미분가능성이 연속성보다 훨씬 강한 조건임을 극적으로 드러낸다.

</div>

## 한쪽 미분계수와 미분가능성의 판정

극한이 좌우에서 일치할 때에만 존재하듯, 미분계수의 존재도 좌우 차분몫의 극한이 일치하는지에 달려 있다. 이를 떼어 정의해 두면 모서리·끝점에서의 미분가능성을 정밀하게 다룰 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 함수 $$f$$의 점 $$a$$에서의 *우미분계수<sub>right-hand derivative</sub>*와 *좌미분계수<sub>left-hand derivative</sub>*를 각각

$$f'_+(a) := \lim_{h \to 0^+} \frac{f(a+h) - f(a)}{h}, \qquad f'_-(a) := \lim_{h \to 0^-} \frac{f(a+h) - f(a)}{h}$$

로 정의한다. 두 한쪽 미분계수가 모두 존재하고 서로 같으면, 그리고 오직 그때에만, $$f$$는 $$a$$에서 미분가능하고 그 공통값이 $$f'(a)$$이다.

</div>

이는 양쪽 극한이 일치할 때에만 극한이 존재한다는 사실 ([§함수의 극한](/ko/math/calculus/functions_and_limits))을 차분몫에 적용한 것에 지나지 않는다. 절댓값함수 $$f(x) = \lvert x\rvert$$를 다시 보면 $$f'_+(0) = 1$$, $$f'_-(0) = -1$$로 둘이 달라 $$0$$에서 미분 불가능함이 곧바로 확인된다. 한쪽 미분계수는 정의역의 끝점에서 미분가능성을 논할 때에도 자연스럽게 쓰이는데, 가령 $$[0, \infty)$$에서 정의된 $$f(x) = \sqrt x$$의 $$0$$에서의 거동은 우미분계수로만 의미를 갖는다.

