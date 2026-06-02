---
title: "평균값 정리"
description: "내부 극값에서 도함수가 사라진다는 페르마 정리에서 출발하여 롤의 정리와 평균값 정리를 증명한다. 도함수가 0이면 함수가 상수라는 따름정리와, 로피탈 정리의 토대가 되는 코시 평균값 정리도 다룬다."
excerpt: "페르마 정리, 롤의 정리, 평균값 정리, 코시 평균값 정리"

categories: [Math / Calculus]
permalink: /ko/math/calculus/mean_value_theorem
sidebar: 
    nav: "calculus-ko"

header:
    overlay_image: /assets/images/Math/Calculus/Mean_Value_Theorem.png
    overlay_filter: 0.5

date: 2026-06-02
last_modified_at: 2026-06-02
weight: 5

published: false
---

[§미분과 도함수](/ko/math/calculus/derivatives)에서 도함수를 정의하였으나, 도함수의 값이 함수 자체의 거동을 어떻게 통제하는지는 아직 보지 않았다. 그 다리를 놓는 것이 평균값 정리이며, 미분이 함수의 증감·극값·근사에 대해 말해 주는 거의 모든 정리가 여기서 나온다.

## 극값과 페르마 정리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 함수 $$f$$가 점 $$c$$에서 *극댓값<sub>local maximum</sub>*을 가진다는 것은, $$c$$를 포함하는 어떤 열린구간 안의 모든 $$x$$에 대해 $$f(x) \leq f(c)$$인 것이다. *극솟값<sub>local minimum</sub>*도 대칭적으로 정의하며, 둘을 통틀어 *극값<sub>local extremum</sub>*이라 한다.

</div>

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (페르마 정리)**</ins> $$f$$가 내부의 점 $$c$$에서 극값을 가지고 $$c$$에서 미분가능하면 $$f'(c) = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$c$$가 극댓값인 경우를 보자 (극솟값은 $$-f$$를 보면 된다). $$c$$ 근방에서 $$f(x) \leq f(c)$$이므로, 차분몫 $$\dfrac{f(c+h)-f(c)}{h}$$의 분자는 $$0$$ 이하이다. 따라서 $$h > 0$$인 쪽에서 차분몫은 $$0$$ 이하이고 그 극한 $$f'(c) \leq 0$$이며, $$h < 0$$인 쪽에서 차분몫은 $$0$$ 이상이고 그 극한 $$f'(c) \geq 0$$이다. $$f$$가 $$c$$에서 미분가능하여 두 한쪽 극한이 같아야 하므로 $$f'(c) = 0$$이다.

</details>

도함수가 $$0$$이거나 존재하지 않는 점을 *임계점<sub>critical point</sub>*이라 한다. 페르마 정리는 내부 극값이 반드시 임계점에서 일어남을 말한다. 단, 역은 거짓이다: $$f(x) = x^3$$은 $$x = 0$$에서 $$f'(0) = 0$$이지만 극값을 갖지 않는다.

## 롤의 정리와 평균값 정리

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (롤의 정리)**</ins> $$f$$가 닫힌구간 $$[a,b]$$에서 연속이고 열린구간 $$(a,b)$$에서 미분가능하며 $$f(a) = f(b)$$이면, $$f'(c) = 0$$인 $$c \in (a,b)$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$[a,b]$$에서 연속이므로 최대·최소 정리 ([§연속함수, ⁋정리 3](/ko/math/calculus/continuity#thm3))에 의해 $$[a,b]$$에서 최댓값과 최솟값을 가진다. 두 값이 모두 끝점에서만 일어난다면, $$f(a) = f(b)$$이므로 최댓값과 최솟값이 같아 $$f$$는 상수이고 모든 내부 점에서 $$f' = 0$$이다. 그렇지 않으면 최댓값이나 최솟값 중 적어도 하나가 내부 점 $$c$$에서 일어나며, 그 점은 극값이므로 페르마 정리에 의해 $$f'(c) = 0$$이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (평균값 정리)**</ins> $$f$$가 $$[a,b]$$에서 연속이고 $$(a,b)$$에서 미분가능하면

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

를 만족하는 $$c \in (a,b)$$가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

두 끝점을 잇는 직선을 빼서 롤의 정리를 적용한다. 보조함수

$$g(x) = f(x) - \left[ f(a) + \frac{f(b)-f(a)}{b-a}(x - a) \right]$$

를 두면 $$g$$는 $$[a,b]$$에서 연속, $$(a,b)$$에서 미분가능하고 $$g(a) = g(b) = 0$$이다. 롤의 정리에 의해 $$g'(c) = 0$$인 $$c \in (a,b)$$가 있고, $$g'(c) = f'(c) - \dfrac{f(b)-f(a)}{b-a}$$이므로 정리가 따른다.

</details>

평균값 정리는 "구간 위 어딘가에서 순간변화율이 평균변화율과 같다"는 것으로, 구간 끝의 정보 $$f(a), f(b)$$를 내부의 도함수와 잇는다.

## 평균값 정리의 따름정리

도함수가 함수를 통제한다는 사실의 가장 기본적 형태는 다음이다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> $$f$$가 구간 $$I$$에서 미분가능하고 모든 점에서 $$f'(x) = 0$$이면, $$f$$는 $$I$$에서 상수이다. 따라서 $$f' = g'$$이면 $$f - g$$는 상수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$I$$의 임의의 두 점 $$x_1 < x_2$$에 대해, 평균값 정리를 $$[x_1, x_2]$$에 적용하면 $$f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0$$인 $$c$$가 있다. 따라서 $$f(x_1) = f(x_2)$$이고 $$f$$는 상수이다. 둘째 주장은 $$f - g$$의 도함수가 $$0$$임에서 따른다.

</details>

이 따름정리는 부정적분이 상수 차이를 빼면 유일하다는 사실의 근거이며 ([§부정적분](/ko/math/calculus/antiderivatives)), 미적분의 기본정리에서 결정적으로 쓰인다. 마지막으로, 두 함수의 변화율을 동시에 비교하는 일반화가 부정형 극한 계산의 토대가 된다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (코시 평균값 정리)**</ins> $$f, g$$가 $$[a,b]$$에서 연속이고 $$(a,b)$$에서 미분가능하면

$$\bigl(f(b) - f(a)\bigr)\,g'(c) = \bigl(g(b) - g(a)\bigr)\,f'(c)$$

를 만족하는 $$c \in (a,b)$$가 존재한다. 특히 $$g(a) \neq g(b)$$이고 $$g' \neq 0$$이면 $$\dfrac{f(b)-f(a)}{g(b)-g(a)} = \dfrac{f'(c)}{g'(c)}$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

보조함수 $$h(x) = \bigl(f(b)-f(a)\bigr)g(x) - \bigl(g(b)-g(a)\bigr)f(x)$$를 두면 $$h(a) = h(b) = f(b)g(a) - f(a)g(b)$$로 같다. 롤의 정리에 의해 $$h'(c) = 0$$인 $$c \in (a,b)$$가 있고, 이것이 곧 주장하는 등식이다.

</details>

코시 평균값 정리에서 $$g(x) = x$$로 두면 $$g'(c) = 1$$, $$g(b) - g(a) = b - a$$가 되어 정리 4의 평균값 정리가 다시 나온다. 즉 코시 평균값 정리는 평균값 정리를 두 함수의 비교로 일반화한 것이며, 그 증명 또한 평균값 정리가 아닌 롤의 정리로 직접 환원된다는 점에 유의한다. 끝점에서 같은 값을 갖는 보조함수를 만들어 롤의 정리를 적용하는 이 수법은 본 글의 모든 정리를 관통하는 공통의 골격이다.

## 단조성 판정

평균값 정리가 응용에서 가장 자주 쓰이는 형태는 도함수의 부호로 함수의 증감을 읽어 내는 것이다. 차분 $$f(x_2) - f(x_1)$$을 $$f'(c)(x_2 - x_1)$$로 바꾸면, 도함수의 부호가 곧 차분의 부호를 결정하기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (단조성 판정)**</ins> $$f$$가 구간 $$I$$에서 미분가능하다고 하자. 모든 내부 점에서 $$f'(x) > 0$$이면 $$f$$는 $$I$$에서 순증가하고, $$f'(x) < 0$$이면 순감소한다. 더 약하게 $$f'(x) \geq 0$$이면 $$f$$는 비감소이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$I$$의 임의의 두 점 $$x_1 < x_2$$를 택하면, 평균값 정리를 $$[x_1, x_2]$$에 적용하여

$$f(x_2) - f(x_1) = f'(c)\,(x_2 - x_1), \qquad c \in (x_1, x_2)$$

인 $$c$$를 얻는다. 여기서 $$x_2 - x_1 > 0$$이므로 우변의 부호는 $$f'(c)$$의 부호와 일치한다. 따라서 모든 점에서 $$f' > 0$$이면 $$f(x_2) - f(x_1) > 0$$, 곧 $$f(x_1) < f(x_2)$$이므로 순증가이고, $$f' < 0$$이면 같은 방식으로 순감소이며, $$f' \geq 0$$이면 $$f(x_2) - f(x_1) \geq 0$$이므로 비감소이다.

</details>

이 판정은 도함수가 함수를 통제한다는 사실의 가장 실용적인 형태이다. 주의할 점은 순증가가 모든 점에서 $$f' > 0$$임을 강제하지는 않는다는 것이다. $$f(x) = x^3$$은 $$\mathbb{R}$$에서 순증가하지만 $$f'(0) = 0$$이다. 즉 명제 7의 첫 부분은 충분조건일 뿐 필요조건은 아니며, 정확한 필요충분조건은 "$$f' \geq 0$$이고 $$f'$$이 어떤 구간에서도 항등적으로 $$0$$이 아님"이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8 (부등식의 증명)**</ins> 모든 $$x > 0$$에 대해 $$\ln(1 + x) < x$$임을 보이자. $$f(x) = x - \ln(1+x)$$로 두면 $$f(0) = 0$$이고

$$f'(x) = 1 - \frac{1}{1+x} = \frac{x}{1+x} > 0 \qquad (x > 0)$$

이다. 명제 7에 의해 $$f$$는 $$[0, \infty)$$에서 순증가하므로, $$x > 0$$이면 $$f(x) > f(0) = 0$$, 곧 $$x > \ln(1+x)$$이다. 같은 방식으로 $$g(x) = \ln(1+x) - \dfrac{x}{1+x}$$를 보면 $$g(0) = 0$$이고 $$g'(x) = \dfrac{x}{(1+x)^2} > 0$$이므로, $$\dfrac{x}{1+x} < \ln(1+x)$$도 따른다. 두 부등식을 합치면

$$\frac{x}{1+x} < \ln(1+x) < x \qquad (x > 0)$$

라는 로그의 양쪽 평가가 나온다.

</div>

## 평균값 정리에 의한 평가

평균값 정리의 등식 $$f(b) - f(a) = f'(c)(b-a)$$에서 미지의 $$c$$를 도함수의 상·하한으로 묶으면, 함수의 증분 자체를 한 줄로 평가할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9 (증분의 평가)**</ins> $$f$$가 $$[a,b]$$에서 연속, $$(a,b)$$에서 미분가능하고 모든 $$x$$에서 $$m \leq f'(x) \leq M$$이면

$$m\,(b - a) \leq f(b) - f(a) \leq M\,(b - a)$$

이다. 특히 $$\lvert f'(x)\rvert \leq L$$이면 $$\lvert f(b) - f(a)\rvert \leq L\,\lvert b - a\rvert$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

평균값 정리로 $$f(b) - f(a) = f'(c)(b-a)$$인 $$c \in (a,b)$$를 잡는다. 가정에서 $$m \leq f'(c) \leq M$$이고 $$b - a > 0$$이므로 세 변에 $$b - a$$를 곱하면

$$m\,(b-a) \leq f'(c)\,(b-a) \leq M\,(b-a)$$

이고 가운데 항이 $$f(b) - f(a)$$이다. 둘째 주장은 $$-L \leq f'(x) \leq L$$에 같은 부등식을 적용하여 $$\lvert f(b) - f(a)\rvert \leq L\,(b-a)$$를 얻는 것이다.

</details>

도함수가 유계인 함수는 이렇게 *립시츠 연속<sub>Lipschitz continuous</sub>*이 된다. 두 점에서의 값의 차이가 두 점 사이 거리에 비례해 묶이는 것이다. 이는 미분가능성이 단순한 연속성보다 훨씬 강한 통제를 준다는 것을 보여 준다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10 (근사값 평가)**</ins> $$\sqrt{50}$$을 평가하자. $$f(x) = \sqrt{x}$$에 평균값 정리를 $$[49, 50]$$에서 적용하면

$$\sqrt{50} - \sqrt{49} = f'(c)\,(50 - 49) = \frac{1}{2\sqrt{c}}, \qquad c \in (49, 50)$$

인 $$c$$가 있다. $$49 < c < 50$$이므로 $$\dfrac{1}{2\sqrt{50}} < \dfrac{1}{2\sqrt{c}} < \dfrac{1}{2\sqrt{49}} = \dfrac{1}{14}$$이고, 따라서

$$7 + \frac{1}{2\sqrt{50}} < \sqrt{50} < 7 + \frac{1}{14}$$

이다. 우변에서 $$\sqrt{50} < 7.0714\cdots$$를 얻으며, 실제 값 $$7.07106\cdots$$과 잘 맞는다. 같은 방법으로 $$\sin$$의 도함수가 $$\lvert \cos\rvert \leq 1$$로 묶이므로, 명제 9에서 모든 $$x, y$$에 대해 $$\lvert \sin x - \sin y\rvert \leq \lvert x - y\rvert$$가 즉시 나온다.

</div>

## 해의 개수와 롤의 정리

롤의 정리는 도함수의 근의 개수로 함수의 근의 개수를 위에서 묶는 데도 쓰인다. 함수의 서로 다른 두 근 사이마다 도함수의 근이 적어도 하나 끼어 있어야 하기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11 (근의 분리)**</ins> $$f$$가 구간 $$I$$에서 미분가능하고 $$f'$$이 $$I$$에서 많아야 $$k$$개의 근을 가지면, $$f$$는 $$I$$에서 많아야 $$k + 1$$개의 근을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 $$I$$에서 서로 다른 근 $$x_0 < x_1 < \cdots < x_k < x_{k+1}$$을 $$k + 2$$개 가진다고 가정하고 모순을 이끈다. 각 인접한 쌍 $$[x_{i-1}, x_i]$$에서 $$f(x_{i-1}) = f(x_i) = 0$$이므로 롤의 정리에 의해

$$f'(c_i) = 0, \qquad c_i \in (x_{i-1}, x_i)$$

인 $$c_i$$가 있다. 이렇게 얻은 $$c_1 < c_2 < \cdots < c_{k+1}$$은 서로 다른 $$k + 1$$개의 점이고 모두 $$f'$$의 근이므로, $$f'$$이 많아야 $$k$$개의 근을 가진다는 가정에 모순이다. 따라서 $$f$$의 근은 많아야 $$k + 1$$개이다.

</details>

이 원리는 다항식이 아닌 함수의 근의 개수를 다룰 때 특히 유용하다. 예컨대 $$n$$차 다항식의 도함수는 $$n - 1$$차여서 많아야 $$n - 1$$개의 근을 가지므로, 명제 11을 반복 적용하면 $$n$$차 다항식이 많아야 $$n$$개의 실근을 가진다는 사실이 미분만으로 따라 나온다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12 (근의 유일성)**</ins> 방정식 $$x^3 + x - 1 = 0$$의 실근이 정확히 하나임을 보이자. $$f(x) = x^3 + x - 1$$로 두면 $$f(0) = -1 < 0$$이고 $$f(1) = 1 > 0$$이므로, 중간값 정리 ([§연속함수, ⁋정리 4](/ko/math/calculus/continuity#thm4)) 에 의해 $$(0, 1)$$에 근이 적어도 하나 있다. 한편

$$f'(x) = 3x^2 + 1 > 0 \qquad (\text{모든 } x)$$

이므로 $$f'$$은 근을 갖지 않는다. 명제 11에서 $$k = 0$$이면 $$f$$의 근은 많아야 한 개이다. 적어도 하나이면서 많아야 하나이므로, 실근은 정확히 하나이다.

</div>

## 코시 평균값 정리와 부정형 극한

코시 평균값 정리는 두 함수의 증분의 비를 도함수의 비로 바꿔 주므로, $$\dfrac{0}{0}$$ 꼴의 부정형 극한을 다루는 로피탈 정리의 직접적 토대가 된다. 정리 6의 비율 형태에서 $$a$$를 향해 극한을 취하면 이를 한눈에 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13 (로피탈 정리, $$0/0$$ 형)**</ins> $$f, g$$가 $$a$$를 포함하는 구간에서 미분가능하고 $$f(a) = g(a) = 0$$, $$a$$ 근방에서 $$g'(x) \neq 0$$이라 하자. 극한 $$\displaystyle\lim_{x \to a} \dfrac{f'(x)}{g'(x)} = L$$이 존재하면

$$\lim_{x \to a} \frac{f(x)}{g(x)} = L$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$x$$가 $$a$$의 한쪽에 있을 때, 코시 평균값 정리를 $$[a, x]$$ (또는 $$[x, a]$$) 에 적용하면 $$f(a) = g(a) = 0$$이므로

$$\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(c_x)}{g'(c_x)}, \qquad c_x \text{는 } a \text{와 } x \text{ 사이}$$

인 $$c_x$$가 존재한다 (여기서 $$g(x) \neq g(a)$$임은 $$g' \neq 0$$과 롤의 정리에서 보장된다). 이제 $$x \to a$$이면 $$c_x$$도 $$a$$와 $$x$$ 사이에 끼여 있으므로 $$c_x \to a$$이고, 가정에서

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(c_x)}{g'(c_x)} = \lim_{c \to a} \frac{f'(c)}{g'(c)} = L$$

이다.

</details>

<div class="example" markdown="1">

<ins id="ex14">**예시 14 (로피탈 정리의 적용)**</ins> 잘 알려진 극한 $$\displaystyle\lim_{x\to 0}\dfrac{\sin x}{x}$$를 명제 13으로 계산하면, $$f(x) = \sin x$$, $$g(x) = x$$가 모두 $$0$$에서 사라지고

$$\lim_{x \to 0} \frac{f'(x)}{g'(x)} = \lim_{x \to 0} \frac{\cos x}{1} = 1$$

이므로 $$\displaystyle\lim_{x\to 0}\dfrac{\sin x}{x} = 1$$이다. 한 단계로 풀리지 않는 경우는 정리를 반복한다. 예컨대

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \lim_{x \to 0} \frac{\sin x}{2x} = \lim_{x \to 0} \frac{\cos x}{2} = \frac{1}{2}$$

인데, 처음 두 극한이 모두 $$\dfrac{0}{0}$$ 형이라 명제 13을 두 번 적용한 것이다. 단, 매 단계에서 분모·분자가 모두 $$0$$으로 가는지를 확인해야 하며, 그렇지 않은데 형식적으로 도함수의 비를 취하면 틀린 답이 나온다.

</div>

평균값 정리에서 끌어낸 단조성·극값·볼록성 판정과 코시 평균값 정리에 기댄 로피탈 정리는 다음 글 [§도함수의 응용](/ko/math/calculus/applications_of_derivatives)에서 다룬다. 평균값 정리를 고계도함수로 반복 적용하면 [§테일러 정리](/ko/math/calculus/taylor_theorem)의 나머지항 평가를 얻는다. 본 글의 정리들은 모두 연속함수의 최대·최소 정리를 전제로 하는데, 그것을 떠받치는 실수의 완비성과 함께 엄밀한 증명은 해석학 [§평균값 정리와 테일러 정리](/ko/math/analysis/mean_value_theorem)에서 다시 다룬다.
