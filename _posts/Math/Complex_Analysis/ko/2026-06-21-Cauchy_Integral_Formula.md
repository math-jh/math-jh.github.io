---
title: "Cauchy 적분공식"
description: "정칙함수가 원판 안의 값을 경계적분으로 완전히 복원한다는 Cauchy 적분공식을 Cauchy 정리에서 끌어내고, 핵을 미분하여 정칙함수가 무한히 미분가능함을 보인다. Cauchy 부등식에서 Liouville 정리와 대수학의 기본정리를 유도하고, 평균값 성질과 Cauchy 정리의 역인 Morera 정리를 다룬다."
excerpt: "Cauchy 적분공식, 미분공식, 무한미분가능성, Cauchy 부등식, Liouville 정리, 대수학의 기본정리, 평균값 성질, Morera 정리"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/cauchy_integral_formula
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 5

published: false
---

Cauchy 정리는 ([§Cauchy 정리](/ko/math/complex_analysis/cauchy_theorem)) 단순연결 영역에서 정칙함수의 닫힌 경로 적분이 소멸함을 알려 주었다. 이 소멸 현상의 진짜 위력은, 피적분함수에 $$1/(w-z)$$라는 인위적인 극점을 하나 끼워 넣었을 때 비로소 드러난다. 정칙함수 $$f$$를 원판의 경계에서 적분하되 핵 $$1/(w-z)$$로 무게를 주면, 그 적분이 내부의 한 점 $$z$$에서의 함숫값 $$f(z)$$를 정확히 되돌려 준다. 이것이 Cauchy 적분공식으로, 정칙함수가 경계 위의 값만으로 내부 전체에서 완전히 결정된다는 놀라운 강성을 표현한다. 더 나아가 이 공식의 적분기호 안에서 $$z$$에 대해 미분을 자유로이 반복할 수 있어, 한 번 복소미분가능한 함수가 자동으로 무한히 미분가능하다는 실해석에는 유례가 없는 결론이 따라 나온다. 여기에서 도함수의 크기를 경계값으로 어림하는 Cauchy 부등식이 나오고, 그로부터 유계 entire function이 상수임을 말하는 Liouville 정리와 대수학의 기본정리가, 그리고 적분공식의 역방향으로 Cauchy 정리의 역인 Morera 정리가 차례로 갈라져 나온다.

## Cauchy 적분공식

$$f$$가 닫힌 원판 $$\overline{D(z_0, r)}$$를 품는 영역에서 정칙이라 하자. 경계원 위에서 $$f$$를 핵 $$1/(w-z)$$로 무게를 주어 적분하면, 그 값이 내부 점 $$z$$에서의 $$f(z)$$를 복원한다는 것이 Cauchy 적분공식이다. 증명의 발상은 다음과 같다. 함수 $$w \mapsto f(w)/(w-z)$$는 $$w = z$$를 제외한 원판 위에서 정칙이므로, Cauchy 정리의 homotopy 형태를 써서 적분의 경로를 경계원에서 $$z$$를 중심으로 한 아주 작은 원으로 옮길 수 있다. 그 작은 원 위에서는 $$f(w) \approx f(z)$$이고, 남는 적분 $$\oint dw/(w-z)$$이 정확히 $$2\pi i$$를 내므로 결과가 $$2\pi i\, f(z)$$가 된다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Cauchy 적분공식)**</ins> $$\Omega \subseteq \mathbb{C}$$가 열린집합이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 닫힌 원판 $$\overline{D(z_0, r)}$$이 $$\Omega$$에 들어 있으면, 열린 원판 $$D(z_0, r)$$ 안의 임의의 점 $$z$$에 대하여

$$f(z) = \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = r} \frac{f(w)}{w - z}\,dw$$

이다. 여기서 경계원은 반시계방향으로 한 바퀴 도는 것으로 향을 잡는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z \in D(z_0, r)$$을 고정한다. 닫힌 원판이 열린집합 $$\Omega$$에 들어 있으므로, 약간 더 큰 열린 원판 $$D(z_0, R) \subseteq \Omega$$ ($$R > r$$) 을 잡을 수 있다. 함수

$$g(w) = \frac{f(w)}{w - z}$$

는 $$w = z$$를 뺀 $$D(z_0, R)$$에서 정칙이다. 경계원 $$C_r : \lvert w - z_0\rvert = r$$과, $$z$$를 중심으로 한 충분히 작은 원 $$C_\rho : \lvert w - z\rvert = \rho$$ (둘 다 반시계방향, $$\rho$$은 $$\overline{D(z, \rho)} \subseteq D(z_0, r)$$이 되도록 작게) 을 생각한다. 두 원은 모두 구멍 뚫린 영역 $$D(z_0, R)\setminus\{z\}$$ 안의 닫힌 곡선이고, 이 영역 안에서 서로 homotopic하다. 곧 반지름을 연속적으로 키우거나 중심을 옮기며 한 원을 다른 원으로 변형하되 그 과정에서 점 $$z$$를 넘지 않을 수 있다. 따라서 Cauchy의 homotopy 정리 ([§Cauchy 정리, ⁋정리 6](/ko/math/complex_analysis/cauchy_theorem#thm6)) 에 의해

$$\oint_{C_r} g(w)\,dw = \oint_{C_\rho} g(w)\,dw$$

이다. 이제 우변을 $$\rho \to 0$$의 극한으로 평가한다. 핵 부분의 적분 $$\oint_{C_\rho} dw/(w - z)$$는 중심 $$z$$를 한 바퀴 도는 원에서의 적분이므로 $$2\pi i$$이다 ([§복소적분, ⁋명제 10](/ko/math/complex_analysis/complex_integration#prop10)에서 $$n = -1$$인 경우, 평행이동으로 중심을 $$z$$로 옮긴 것). 따라서

$$\oint_{C_\rho} \frac{f(w)}{w - z}\,dw - 2\pi i\, f(z) = \oint_{C_\rho} \frac{f(w) - f(z)}{w - z}\,dw$$

이다. $$f$$가 $$z$$에서 연속이므로 임의의 $$\varepsilon > 0$$에 대해 $$\rho$$이 충분히 작으면 $$C_\rho$$ 위에서 $$\lvert f(w) - f(z)\rvert \leq \varepsilon$$이고, 그 위에서 $$\lvert w - z\rvert = \rho$$이므로 피적분함수의 크기는 $$\varepsilon/\rho$$ 이하이다. ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 을 $$\mathrm{length}(C_\rho) = 2\pi\rho$$에 적용하면

$$\left\lvert \oint_{C_\rho} \frac{f(w) - f(z)}{w - z}\,dw \right\rvert \leq \frac{\varepsilon}{\rho}\cdot 2\pi\rho = 2\pi\varepsilon$$

이다. 좌변은 $$\rho$$에 무관한 상수 $$\bigl\lvert \oint_{C_r} g\,dw - 2\pi i\, f(z)\bigr\rvert$$이고 (앞의 homotopy 불변성으로 $$C_\rho$$ 적분이 $$C_r$$ 적분과 같으므로) 우변은 $$\varepsilon \to 0$$일 때 $$0$$으로 가므로, 이 상수는 $$0$$이다. 곧

$$\oint_{C_r} \frac{f(w)}{w - z}\,dw = 2\pi i\, f(z)$$

이고, 양변을 $$2\pi i$$로 나누면 주장하는 공식을 얻는다.

</details>

정리 1은 정칙함수의 내부값이 경계값에 의해 일의적으로 결정됨을 말한다. 경계원 위의 $$f$$ 값만 알면 적분 한 번으로 원판 내부 어디에서나 $$f$$를 계산할 수 있으므로, 정칙성은 실해석의 매끄러운 함수에는 없는 극단적인 강성을 함수에 부여한다. 가령 두 정칙함수가 한 원의 경계에서 일치하면 그 원판 전체에서 일치한다. 적분기호 안의 $$z$$ 의존성이 핵 $$1/(w-z)$$에만 들어 있고 $$f(w)$$에는 들어 있지 않다는 점이 결정적인데, 이 깔끔한 분리 덕분에 $$z$$에 대한 미분을 적분 안으로 옮겨 핵만 미분하는 것이 가능해진다. 이것이 다음 절의 미분공식이다.

## 미분공식과 무한미분가능성

Cauchy 적분공식은 $$f(z)$$를 매개변수 $$z$$에 의존하는 적분으로 표현한다. 핵 $$1/(w-z)$$이 $$z$$에 대해 매끄럽게 의존하므로, 차분비를 만들어 적분기호 안에서 극한을 취하면 $$f$$의 도함수가 다시 같은 꼴의 적분으로 표현되리라 기대할 수 있다. 이를 반복하면 $$f$$가 임의의 차수로 미분되며, 각 도함수가 경계적분으로 주어진다. 결론적으로 한 번 복소미분가능한 함수는 자동으로 무한히 미분가능하다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Cauchy 미분공식)**</ins> $$\Omega \subseteq \mathbb{C}$$가 열린집합이고 $$f$$가 $$\Omega$$에서 정칙이라 하자. 닫힌 원판 $$\overline{D(z_0, r)}$$이 $$\Omega$$에 들어 있으면, $$f$$는 $$D(z_0, r)$$에서 모든 차수로 복소미분가능하고, 각 $$z \in D(z_0, r)$$과 정수 $$n \geq 0$$에 대하여

$$f^{(n)}(z) = \frac{n!}{2\pi i}\oint_{\lvert w - z_0\rvert = r} \frac{f(w)}{(w - z)^{n+1}}\,dw$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$n$$에 대한 귀납법으로 보인다. $$n = 0$$인 경우는 $$0! = 1$$이고 식이 정리 1의 Cauchy 적분공식 자체이므로 성립한다.

$$f^{(n)}$$이 $$D(z_0, r)$$에서 위 적분 표현을 가진다고 가정하고, $$f^{(n)}$$이 다시 한 번 미분되어 $$f^{(n+1)}$$이 주장하는 공식을 만족함을 보인다. $$z \in D(z_0, r)$$을 고정하고, $$\lvert h\rvert$$이 충분히 작아 $$z + h$$도 $$D(z_0, r)$$에 들어가도록 한다. 귀납가정의 적분 표현에서 차분비를 만들면

$$\frac{f^{(n)}(z + h) - f^{(n)}(z)}{h} = \frac{n!}{2\pi i}\oint_{C_r} f(w)\cdot \frac{1}{h}\left( \frac{1}{(w - z - h)^{n+1}} - \frac{1}{(w - z)^{n+1}} \right) dw$$

이다 (여기서 $$C_r$$은 경계원). 괄호 안에서 $$a = w - z - h$$, $$b = w - z$$로 두면 $$b - a = h$$이고, 항등식

$$\frac{1}{a^{n+1}} - \frac{1}{b^{n+1}} = \frac{b^{n+1} - a^{n+1}}{a^{n+1}b^{n+1}} = (b - a)\,\frac{\sum_{j=0}^{n} a^j b^{n-j}}{a^{n+1}b^{n+1}}$$

를 써서 $$1/h$$을 약분하면, 차분비의 핵은

$$\frac{1}{h}\left( \frac{1}{(w - z - h)^{n+1}} - \frac{1}{(w - z)^{n+1}} \right) = \frac{\sum_{j=0}^{n} (w - z - h)^j (w - z)^{n-j}}{(w - z - h)^{n+1}(w - z)^{n+1}}$$

가 된다. $$h \to 0$$이면 분자의 각 항이 $$(w - z)^j (w - z)^{n-j} = (w-z)^n$$으로 수렴하여 합이 $$(n+1)(w - z)^n$$이 되고, 분모는 $$(w - z)^{2n+2}$$으로 수렴하므로, 핵은 $$C_r$$ 위에서 균등하게

$$\frac{(n+1)(w - z)^n}{(w - z)^{2n+2}} = \frac{n+1}{(w - z)^{n+2}}$$

으로 수렴한다. 균등수렴인 까닭은 $$w$$가 콤팩트집합 $$C_r$$ 위를 움직일 때 $$\lvert w - z\rvert$$이 양의 최솟값 $$\delta = r - \lvert z - z_0\rvert > 0$$을 가져, $$\lvert h\rvert < \delta/2$$이면 분모의 모든 인수가 $$\delta/2$$ 이상으로 아래로 유계이고 분자가 위로 유계이기 때문이다. 따라서 차분비의 극한을 적분기호 안으로 옮길 수 있어 ($$C_r$$ 위 균등수렴이므로 ML 부등식으로 극한과 적분의 교환이 정당화된다)

$$f^{(n+1)}(z) = \frac{n!}{2\pi i}\oint_{C_r} f(w)\cdot \frac{n+1}{(w - z)^{n+2}}\,dw = \frac{(n+1)!}{2\pi i}\oint_{C_r} \frac{f(w)}{(w - z)^{(n+1)+1}}\,dw$$

이다. 이로써 차수 $$n+1$$에 대한 공식이 성립하고, 동시에 $$f^{(n)}$$이 $$D(z_0, r)$$에서 미분가능함이 확인되었다. 귀납법에 의해 $$f$$는 모든 차수로 미분가능하며 각 도함수가 위 적분으로 주어진다.

</details>

정리 2의 가장 중요한 귀결은 정칙함수의 무한미분가능성이다. $$\Omega$$에서 정칙인 $$f$$와 임의의 점 $$z_0 \in \Omega$$에 대해, $$\Omega$$가 열려 있으므로 작은 닫힌 원판 $$\overline{D(z_0, r)} \subseteq \Omega$$을 잡을 수 있고, 정리 2에 의해 $$f$$는 그 원판 안에서 모든 차수로 미분가능하다. 점 $$z_0$$이 임의였으므로 $$f$$는 $$\Omega$$ 전체에서 무한히 미분가능하며, 더구나 모든 도함수 $$f^{(n)}$$이 다시 정칙이다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $$f$$가 영역 $$\Omega \subseteq \mathbb{C}$$에서 정칙이면, $$f$$는 $$\Omega$$에서 무한히 복소미분가능하고, 모든 차수의 도함수 $$f^{(n)}$$ 역시 $$\Omega$$에서 정칙이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_0 \in \Omega$$을 임의로 잡으면 $$\Omega$$가 열려 있어 $$\overline{D(z_0, r)} \subseteq \Omega$$인 $$r > 0$$이 있고, 정리 2가 $$D(z_0, r)$$에서 모든 차수의 도함수 $$f^{(n)}$$의 존재를 보장한다. $$z_0$$이 임의였으므로 $$f$$는 $$\Omega$$의 모든 점에서 모든 차수로 미분가능하다. 각 $$n$$에 대해 $$f^{(n)}$$은 $$\Omega$$의 모든 점에서 복소미분가능한 도함수 $$f^{(n+1)}$$을 가지므로, 정의에 의해 $$\Omega$$에서 정칙이다 ([§정칙함수, ⁋정의 2](/ko/math/complex_analysis/holomorphic_functions#def2)).

</details>

따름정리 3은 복소해석과 실해석을 가르는 분수령이다. 실변수에서는 한 번 미분가능한 함수가 두 번 미분가능할 이유가 전혀 없지만 (가령 $$x\lvert x\rvert$$은 한 번만 미분가능하다), 복소변수에서는 한 점 근방에서 단 한 번 복소미분가능하다는 조건이 곧바로 그 근방에서의 무한미분가능성을 강제한다. 이 무한미분가능성은 곧 정칙함수의 국소 멱급수 전개로 이어지는 발판이 된다.

## Cauchy 부등식과 Liouville 정리

미분공식은 도함수 $$f^{(n)}(z_0)$$을 경계원 위의 적분으로 표현하므로, ML 부등식으로 그 크기를 경계 위 $$f$$의 최댓값으로 직접 어림할 수 있다. 이렇게 얻는 Cauchy 부등식은 도함수의 성장을 함숫값의 크기로 통제하며, 이로부터 평면 전체에서 유계인 정칙함수가 상수일 수밖에 없다는 Liouville 정리가 따라 나온다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Cauchy 부등식)**</ins> $$f$$가 닫힌 원판 $$\overline{D(z_0, r)}$$를 품는 영역에서 정칙이고, 경계원 $$\lvert w - z_0\rvert = r$$ 위에서 $$\lvert f(w)\rvert \leq M$$이라 하자. 그러면 모든 정수 $$n \geq 0$$에 대하여

$$\bigl\lvert f^{(n)}(z_0)\bigr\rvert \leq \frac{n!\,M}{r^n}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 2의 미분공식을 $$z = z_0$$에서 쓰면

$$f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_{\lvert w - z_0\rvert = r} \frac{f(w)}{(w - z_0)^{n+1}}\,dw$$

이다. 경계원 위에서 $$\lvert w - z_0\rvert = r$$이므로 피적분함수의 크기는

$$\left\lvert \frac{f(w)}{(w - z_0)^{n+1}} \right\rvert = \frac{\lvert f(w)\rvert}{r^{n+1}} \leq \frac{M}{r^{n+1}}$$

이하이다. 경계원의 길이가 $$2\pi r$$이므로 ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 에 의해

$$\bigl\lvert f^{(n)}(z_0)\bigr\rvert = \frac{n!}{2\pi}\left\lvert \oint \frac{f(w)}{(w - z_0)^{n+1}}\,dw \right\rvert \leq \frac{n!}{2\pi}\cdot \frac{M}{r^{n+1}}\cdot 2\pi r = \frac{n!\,M}{r^n}$$

이다.

</details>

Cauchy 부등식은 도함수의 크기를 경계 위 함숫값의 최댓값과 원의 반지름으로 직접 묶는다. 특히 $$f$$가 더 큰 영역에서 정칙이어서 반지름 $$r$$을 키울 수 있다면, $$M$$이 $$r$$과 함께 너무 빨리 커지지 않는 한 우변을 $$r$$을 키워 줄일 수 있다. 이 관찰을 $$n = 1$$과 평면 전체에서 유계인 함수에 적용하면 다음 정리가 즉시 나온다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5 (Liouville 정리)**</ins> $$f$$가 entire function이고 평면 전체에서 유계이면, 곧 어떤 상수 $$M$$이 있어 모든 $$z \in \mathbb{C}$$에 대해 $$\lvert f(z)\rvert \leq M$$이면, $$f$$는 상수함수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$f$$가 entire function이므로 ([§정칙함수, ⁋정의 2](/ko/math/complex_analysis/holomorphic_functions#def2)) 임의의 점 $$z_0 \in \mathbb{C}$$과 임의의 $$r > 0$$에 대해 닫힌 원판 $$\overline{D(z_0, r)}$$가 정칙 영역에 들어 있다. 경계원 위에서 $$\lvert f\rvert \leq M$$이므로 정리 4를 $$n = 1$$에 적용하면

$$\bigl\lvert f'(z_0)\bigr\rvert \leq \frac{1!\,M}{r} = \frac{M}{r}$$

이다. $$f$$가 평면 전체에서 정칙이므로 $$r$$을 임의로 크게 잡을 수 있고, $$r \to \infty$$이면 우변이 $$0$$으로 가므로 $$f'(z_0) = 0$$이다. $$z_0$$이 임의였으므로 $$f' \equiv 0$$이다. 도함수가 항상 $$0$$인 정칙함수는 연결된 영역에서 상수이므로 (실수부와 허수부의 모든 편미분이 $$0$$이라 Cauchy–Riemann 관계 아래 $$u, v$$가 상수이다), $$f$$는 $$\mathbb{C}$$에서 상수함수이다.

</details>

Liouville 정리는 정칙성과 유계성이 양립하기에는 너무 강한 조건임을 말한다. entire function이 상수가 아니라면 그 절댓값은 어딘가에서 반드시 무한히 커져야 한다. 가령 $$\sin z$$나 $$e^z$$ 같은 비상수 entire function은 ([§정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10)) 실축 위에서는 유계로 보이더라도 허수방향으로 가면 절댓값이 폭발한다. 이 단순한 정리가 대수학에서 가장 기본적인 사실 하나를 증명하는 열쇠가 된다.

## 대수학의 기본정리

복소수체에서는 상수가 아닌 모든 다항식이 근을 가진다. 이 사실이 대수학의 기본정리이며, 그 이름과 달리 순수하게 대수적인 증명은 알려져 있지 않고 해석학의 도구가 본질적으로 개입한다. Liouville 정리를 쓰면 근이 없다는 가정에서 다항식의 역수가 유계인 entire function이 되어 모순이 빚어짐을 간단히 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (대수학의 기본정리)**</ins> 차수가 $$1$$ 이상인 임의의 복소계수 다항식 $$p(z) = a_n z^n + \cdots + a_1 z + a_0$$ ($$a_n \neq 0$$, $$n \geq 1$$) 은 $$\mathbb{C}$$에서 적어도 하나의 근을 가진다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p$$가 근을 갖지 않는다고 가정하면, 곧 모든 $$z \in \mathbb{C}$$에 대해 $$p(z) \neq 0$$이면 함수

$$g(z) = \frac{1}{p(z)}$$

이 잘 정의된다. 다항식은 entire function이고 ([§정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)에서 다항식의 정칙성) 분모가 $$0$$이 되지 않으므로 그 역수 $$g$$도 $$\mathbb{C}$$ 전체에서 정칙이다.

$$g$$가 유계임을 보인다. $$\lvert z\rvert$$이 클 때 $$p$$의 거동을 보면,

$$p(z) = a_n z^n\left( 1 + \frac{a_{n-1}}{a_n z} + \cdots + \frac{a_0}{a_n z^n} \right)$$

이고 괄호 안은 $$\lvert z\rvert \to \infty$$일 때 $$1$$로 수렴하므로, 충분히 큰 $$R > 0$$이 있어 $$\lvert z\rvert \geq R$$이면 괄호 안의 크기가 $$1/2$$ 이상이고 따라서

$$\lvert p(z)\rvert \geq \frac{1}{2}\,\lvert a_n\rvert\,\lvert z\rvert^n \geq \frac{1}{2}\,\lvert a_n\rvert\,R^n$$

이다. 곧 $$\lvert z\rvert \geq R$$인 곳에서 $$\lvert g(z)\rvert \leq 2/(\lvert a_n\rvert R^n)$$로 유계이다. 한편 닫힌 원판 $$\overline{D(0, R)}$$은 콤팩트이고 $$g$$가 그 위에서 연속이므로 $$\lvert g\rvert$$은 거기서 어떤 최댓값 이하로 유계이다. 두 어림을 합치면 $$g$$는 $$\mathbb{C}$$ 전체에서 유계인 entire function이다.

Liouville 정리 (따름정리 5) 에 의해 $$g$$는 상수이고, 따라서 $$p = 1/g$$도 상수이다. 그런데 이는 $$p$$의 차수가 $$n \geq 1$$이라는 가정에 어긋난다. 모순이므로 $$p$$는 적어도 하나의 근을 가진다.

</details>

정리 6에서 근을 하나 얻으면 인수분해 $$p(z) = (z - \alpha)q(z)$$로 차수를 하나 낮추고, $$q$$에 같은 정리를 반복 적용하여 $$p$$가 (중복도를 세어) 정확히 $$n$$개의 근을 가짐을 얻는다. 곧 $$\mathbb{C}$$ 위에서 차수 $$n$$인 다항식은 $$p(z) = a_n(z - \alpha_1)\cdots(z - \alpha_n)$$으로 일차식의 곱으로 완전히 쪼개지며, 이는 복소수체가 대수적으로 닫혀 있다는 진술과 같다. 해석학의 강성 정리 하나가 대수학의 근본 사실을 떠받친다는 점이 인상적이다.

## 평균값 성질과 Morera 정리

Cauchy 적분공식을 원의 중심에서 평가하면 경계원을 매개화하여 곧장 평균값 성질이 나온다. 정칙함수의 중심값이 경계 위 값들의 평균과 같다는 이 성질은 적분공식의 가장 직접적인 기하학적 그림자이다. 끝으로 적분공식의 논리를 거꾸로 밟아, 모든 삼각형에서 적분이 소멸하는 연속함수가 정칙이라는 Morera 정리를 보인다. 이는 Cauchy 정리의 역에 해당하며, 정칙성의 적분 판정법을 준다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7 (평균값 성질)**</ins> $$f$$가 닫힌 원판 $$\overline{D(z_0, r)}$$를 품는 영역에서 정칙이면

$$f(z_0) = \frac{1}{2\pi}\int_0^{2\pi} f\bigl(z_0 + r e^{i\theta}\bigr)\,d\theta$$

이다. 곧 중심에서의 함숫값은 경계원 위 함숫값의 평균과 같다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정리 1의 Cauchy 적분공식을 $$z = z_0$$에서 쓰면

$$f(z_0) = \frac{1}{2\pi i}\oint_{\lvert w - z_0\rvert = r} \frac{f(w)}{w - z_0}\,dw$$

이다. 경계원을 $$w = z_0 + r e^{i\theta}$$ ($$\theta \in [0, 2\pi]$$) 로 매개화하면 $$dw = i r e^{i\theta}\,d\theta$$이고 $$w - z_0 = r e^{i\theta}$$이므로

$$f(z_0) = \frac{1}{2\pi i}\int_0^{2\pi} \frac{f(z_0 + r e^{i\theta})}{r e^{i\theta}}\,i r e^{i\theta}\,d\theta = \frac{1}{2\pi}\int_0^{2\pi} f\bigl(z_0 + r e^{i\theta}\bigr)\,d\theta$$

이다.

</details>

평균값 성질은 정칙함수가 어떤 점에서도 주위 원을 따른 평균을 그 중심값으로 되돌려 받음을 말한다. 실수부와 허수부를 따로 떼어 보면 이는 조화함수의 평균값 성질이기도 하며 ([§정칙함수, ⁋명제 12](/ko/math/complex_analysis/holomorphic_functions#prop12)에서 정칙함수의 실허부가 조화함수임), 조화함수가 따르는 최대값 원리와 같은 정성적 결론의 출발점이 된다. 이제 적분공식이 의지하던 Cauchy 정리의 방향을 뒤집는다. Cauchy 정리는 정칙성에서 삼각형 적분의 소멸을 끌어냈는데, Morera 정리는 그 역으로 삼각형 적분의 소멸에서 정칙성을 회복한다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Morera)**</ins> $$f$$가 영역 $$\Omega \subseteq \mathbb{C}$$에서 연속이고, $$\Omega$$에 (내부와 경계를 포함하여) 들어 있는 임의의 삼각형 $$T$$에 대하여

$$\oint_{\partial T} f(z)\,dz = 0$$

이면, $$f$$는 $$\Omega$$에서 정칙이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정칙성은 국소적 성질이므로, 각 점 $$z_0 \in \Omega$$의 어떤 원판 근방에서 $$f$$가 정칙임을 보이면 충분하다. $$\Omega$$가 열려 있으므로 원판 $$D = D(z_0, \rho) \subseteq \Omega$$을 잡는다. 원판은 볼록하여 star-shaped이므로, 그 안의 한 점 $$z_0$$을 기준으로 선분을 따라

$$F(z) = \int_{[z_0, z]} f(\zeta)\,d\zeta \qquad (z \in D)$$

을 정의한다. $$F$$가 $$D$$에서 $$f$$의 원시함수임을 보인다. $$z \in D$$과 $$z + h \in D$$에 대해 세 점 $$z_0, z, z + h$$가 이루는 삼각형은 볼록한 $$D$$에 통째로 들어 있으므로, 가정에 의해 그 경계 적분이 $$0$$이고, 변의 향과 이어붙이기를 정리하면 ([§복소적분, ⁋명제 4](/ko/math/complex_analysis/complex_integration#prop4))

$$F(z + h) - F(z) = \int_{[z, z+h]} f(\zeta)\,d\zeta$$

이다. 상수 $$f(z)$$의 선분 적분이 $$f(z)\,h$$이므로

$$\frac{F(z + h) - F(z)}{h} - f(z) = \frac{1}{h}\int_{[z, z+h]} \bigl( f(\zeta) - f(z) \bigr)\,d\zeta$$

이고, $$f$$가 $$z$$에서 연속이라 $$\lvert h\rvert$$이 작으면 선분 위에서 $$\lvert f(\zeta) - f(z)\rvert \leq \varepsilon$$이므로 ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 으로 우변의 크기가 $$\varepsilon$$ 이하이다. 따라서 $$h \to 0$$일 때 차분비가 $$f(z)$$로 수렴하여 $$F'(z) = f(z)$$이고, $$F$$는 $$D$$에서 정칙이다.

그런데 정칙함수의 도함수는 다시 정칙이므로 (따름정리 3), $$f = F'$$이 $$D$$에서 정칙이다. $$z_0$$이 임의였으므로 $$f$$는 $$\Omega$$ 전체에서 정칙이다.

</details>

Morera 정리의 증명은 $$f$$의 원시함수 $$F$$를 만든 뒤 무한미분가능성 정리를 한 번 쓰는 데 있다. 삼각형 적분의 소멸이라는 가정만으로 star-shaped 영역에서 원시함수가 구성되고 ([§Cauchy 정리, ⁋정리 3](/ko/math/complex_analysis/cauchy_theorem#thm3)의 구성과 동일한 국소 논증), 그 원시함수가 정칙이므로 따름정리 3에 의해 그 도함수인 $$f$$ 자신도 정칙해진다. 정칙함수의 도함수가 다시 정칙이라는 따름정리 3의 강성이 없었다면 이 마지막 도약은 불가능했을 것이다. Morera 정리는 정칙성을 미분이 아니라 적분으로 판정하게 해 주므로, 적분 아래에서 정의된 함수나 정칙함수열의 극한이 정칙임을 보일 때 특히 유용하다. 가령 정칙함수들이 콤팩트집합 위에서 균등수렴하면 극한함수의 삼각형 적분이 극한과 적분의 교환으로 $$0$$이 되어, Morera 정리에 의해 극한도 정칙이다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
