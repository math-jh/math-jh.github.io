---
title: "복소적분"
description: "조각마다 C¹인 곡선 위의 경로적분을 매개변수 적분으로 정의하고, 선형성·재매개화 불변·역방향 부호·이어붙이기와 ML 부등식을 확립한다. 원시함수가 있으면 경로적분이 양 끝값의 차로 환원되어 닫힌 경로에서 0이 됨을 보이고, 원시함수가 없는 핵심 예 ∮dz/z=2πi와 ∮zⁿdz를 계산한다."
excerpt: "경로적분, 매개변수 적분, ML 부등식, 원시함수, 경로 독립, ∮dz/z=2πi"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/complex_integration
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 3

published: false
---

정칙함수의 미분 이론을 ([§정칙함수](/ko/math/complex_analysis/holomorphic_functions)) 정비한 다음 단계는 적분이다. 복소해석학의 깊은 정리들, 가령 정칙함수의 무한미분가능성이나 멱급수 전개는 모두 함수를 평면의 곡선을 따라 적분하는 데서 출발한다. 실변수 적분이 구간 $$[a, b]$$ 위에서 이루어지는 것과 달리, 복소적분의 정의역은 평면을 가로지르는 곡선이며, 같은 두 끝점을 잇는 곡선이 무수히 많으므로 적분값이 *경로*에 어떻게 의존하는가가 핵심 물음이 된다. 이 글에서는 곡선을 따라가는 경로적분을 정의하고 그 기본 성질을 확립한 뒤, 원시함수가 있는 함수에 대해서는 적분이 경로와 무관하게 끝점만으로 결정됨을 보인다. 끝으로 원시함수를 갖지 않아 이 환원이 실패하는 가장 중요한 예 $$\oint \frac{dz}{z} = 2\pi i$$를 계산하는데, 이 한 등식이 뒤따르는 적분 이론 전체의 씨앗이 된다.

## 경로와 경로적분

적분의 정의역이 될 곡선을 먼저 정비한다. 곡선은 실구간을 평면으로 보내는 연속사상으로 보되, 적분에서 곡선의 *속도* $$\gamma'(t)$$가 필요하므로 미분가능성을 요구한다. 다만 꺾인 점을 가지는 곡선(가령 사각형의 경계)을 다루기 위해, 유한히 많은 점을 빼고 미분가능한 *조각마다 매끄러운* 곡선까지 허용한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 연속사상 $$\gamma : [a, b] \to \mathbb{C}$$가 *piecewise $$C^1$$ 곡선<sub>조각마다 C¹인 곡선</sub>*이라는 것은, 구간의 분할 $$a = t_0 < t_1 < \cdots < t_n = b$$이 있어 각 부분구간 $$[t_{k-1}, t_k]$$ 위에서 $$\gamma$$가 $$C^1$$급(곧 도함수 $$\gamma'$$이 존재하고 연속)인 것이다. 점 $$\gamma(a)$$를 곡선의 *시점<sub>initial point</sub>*, $$\gamma(b)$$를 *종점<sub>terminal point</sub>*이라 하고, $$\gamma(a) = \gamma(b)$$이면 $$\gamma$$를 *닫힌 곡선<sub>closed curve</sub>*이라 한다.

</div>

여기서 $$\gamma$$를 실수부와 허수부로 갈라 $$\gamma(t) = x(t) + i\,y(t)$$로 적으면, 그 도함수는 $$\gamma'(t) = x'(t) + i\,y'(t)$$로 정의되는 복소숫값 함수이다. 곧 복소숫값 함수의 미분은 실허 두 성분을 각각 미분한 것이며, 각 부분구간 위에서 $$x, y$$가 $$C^1$$이라는 뜻이다. 분할의 끝점 $$t_k$$에서는 좌·우 도함수가 다를 수 있어 $$\gamma'$$이 불연속일 수 있지만, 그런 점은 유한 개뿐이므로 아래 적분에는 영향을 주지 않는다. 같은 자취를 그리는 곡선이라도 매개변수 $$t$$를 어떻게 잡느냐에 따라 사상 $$\gamma$$ 자체는 달라지는데, 적분값이 이 선택에 무관함은 [명제 4](#prop4)에서 확인한다.

이제 곡선 위에서 함수를 적분한다. 발상은 곡선을 따라 미소 변위 $$dz = \gamma'(t)\,dt$$를 잡고 $$f$$ 값을 곱해 더하는 것으로, 형식적으로는 치환 $$z = \gamma(t)$$를 통해 실변수 적분으로 환원된다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\gamma : [a, b] \to \mathbb{C}$$가 piecewise $$C^1$$ 곡선이고 $$f$$가 $$\gamma$$의 자취 $$\gamma([a,b])$$를 포함하는 열린집합에서 정의된 연속함수일 때, $$\gamma$$를 따르는 $$f$$의 *경로적분<sub>contour integral</sub>*을

$$\int_\gamma f(z)\,dz = \int_a^b f(\gamma(t))\,\gamma'(t)\,dt$$

로 정의한다. 닫힌 곡선 $$\gamma$$에 대하여는 같은 적분을 $$\oint_\gamma f(z)\,dz$$로도 적는다.

</div>

우변의 적분은 복소숫값 함수 $$g(t) = f(\gamma(t))\gamma'(t)$$를 실구간에서 적분한 것이며, 복소숫값 함수의 적분은 실허부를 따로 적분하여 $$\int_a^b g\,dt = \int_a^b \Real g\,dt + i\int_a^b \Img g\,dt$$로 정의된다. 피적분함수 $$g$$는 각 부분구간 $$[t_{k-1}, t_k]$$ 위에서 연속이므로 (유한 개의 분할점을 빼고) 적분이 잘 정의되며, 전체 적분은 부분구간별 적분의 합 $$\sum_k \int_{t_{k-1}}^{t_k} g\,dt$$이다. 정의가 자취뿐 아니라 매개변수 $$\gamma$$ 자체에 기대어 적혀 있지만, 곧 보듯 적분값은 곡선이 그리는 방향만 같으면 매개변수에 무관하다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (단위원 위의 적분)**</ins> 반시계방향 단위원 $$\gamma(t) = e^{it}$$ ($$t \in [0, 2\pi]$$) 를 따라 $$f(z) = 1/z$$를 적분한다. $$\gamma'(t) = i e^{it}$$이고 자취 위에서 $$f(\gamma(t)) = e^{-it}$$이므로

$$\oint_\gamma \frac{dz}{z} = \int_0^{2\pi} e^{-it}\,(i e^{it})\,dt = \int_0^{2\pi} i\,dt = 2\pi i$$

이다. 같은 곡선 위에서 $$f(z) = z$$를 적분하면 $$f(\gamma(t)) = e^{it}$$이라

$$\oint_\gamma z\,dz = \int_0^{2\pi} e^{it}\,(i e^{it})\,dt = i\int_0^{2\pi} e^{2it}\,dt = i\left[\frac{e^{2it}}{2i}\right]_0^{2\pi} = 0$$

이 된다. 두 적분의 대비가 이 글의 주제를 압축한다. $$z$$는 평면 전체에서 원시함수 $$z^2/2$$를 가져 닫힌 곡선에서 적분이 $$0$$인 반면, $$1/z$$는 원점을 둘러싼 영역에서 단일한 원시함수를 갖지 못해 적분이 $$0$$이 아니다.

</div>

## 기본 성질

경로적분은 정의가 실변수 적분으로 환원되므로, 실적분의 성질이 그대로 옮겨 온다. 먼저 피적분함수에 대한 선형성과 곡선의 방향·이어붙이기에 대한 거동을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\gamma : [a, b] \to \mathbb{C}$$가 piecewise $$C^1$$ 곡선이고 $$f, g$$가 $$\gamma$$의 자취를 포함하는 열린집합에서 연속이라 하자. 그러면 다음이 성립한다.

1. (선형성) 임의의 복소수 $$\alpha, \beta$$에 대하여 $$\displaystyle\int_\gamma (\alpha f + \beta g)\,dz = \alpha\int_\gamma f\,dz + \beta\int_\gamma g\,dz$$이다.
2. (재매개화 불변) $$\varphi : [c, d] \to [a, b]$$가 $$\varphi(c) = a$$, $$\varphi(d) = b$$인 $$C^1$$급 증가 전단사이면, $$\tilde{\gamma} = \gamma \circ \varphi$$에 대하여 $$\displaystyle\int_{\tilde\gamma} f\,dz = \int_\gamma f\,dz$$이다.
3. (역방향) $$\gamma$$를 거꾸로 지나는 곡선 $$(-\gamma)(t) = \gamma(a + b - t)$$ ($$t \in [a, b]$$) 에 대하여 $$\displaystyle\int_{-\gamma} f\,dz = -\int_\gamma f\,dz$$이다.
4. (이어붙이기) $$\gamma_1 : [a, b] \to \mathbb{C}$$의 종점이 $$\gamma_2 : [b, c] \to \mathbb{C}$$의 시점과 같아 이어붙인 곡선 $$\gamma_1 + \gamma_2$$을 이룰 때, $$\displaystyle\int_{\gamma_1 + \gamma_2} f\,dz = \int_{\gamma_1} f\,dz + \int_{\gamma_2} f\,dz$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) 정의 2에서 피적분함수가 $$(\alpha f + \beta g)(\gamma(t))\gamma'(t) = \alpha\,f(\gamma(t))\gamma'(t) + \beta\,g(\gamma(t))\gamma'(t)$$로 갈라지고, 실변수 복소숫값 적분이 선형이므로 적분이 분배된다.

(2) 치환적분으로 직접 계산한다. $$\tilde\gamma'(s) = \gamma'(\varphi(s))\varphi'(s)$$이므로

$$\int_{\tilde\gamma} f\,dz = \int_c^d f(\gamma(\varphi(s)))\,\gamma'(\varphi(s))\,\varphi'(s)\,ds$$

이고, $$t = \varphi(s)$$로 치환하면 $$dt = \varphi'(s)\,ds$$이고 $$\varphi$$가 증가하여 적분 구간이 $$s : c \to d$$에서 $$t : a \to b$$로 바뀌므로, 우변이 $$\int_a^b f(\gamma(t))\gamma'(t)\,dt = \int_\gamma f\,dz$$가 된다.

(3) $$(-\gamma)(t) = \gamma(a + b - t)$$의 도함수는 연쇄법칙으로 $$-\gamma'(a + b - t)$$이므로

$$\int_{-\gamma} f\,dz = \int_a^b f(\gamma(a + b - t))\,\bigl(-\gamma'(a + b - t)\bigr)\,dt$$

이다. $$u = a + b - t$$로 치환하면 $$du = -dt$$이고 구간이 $$t : a \to b$$에서 $$u : b \to a$$로 뒤집히므로

$$\int_{-\gamma} f\,dz = \int_b^a f(\gamma(u))\,\bigl(-\gamma'(u)\bigr)\,(-du) = \int_b^a f(\gamma(u))\gamma'(u)\,du = -\int_a^b f(\gamma(u))\gamma'(u)\,du$$

가 되어 $$-\int_\gamma f\,dz$$와 같다.

(4) 이어붙인 곡선 $$\gamma_1 + \gamma_2$$은 $$[a, c]$$ 위에서 $$[a, b]$$에서는 $$\gamma_1$$로, $$[b, c]$$에서는 $$\gamma_2$$로 주어지는 piecewise $$C^1$$ 곡선이다. 실변수 적분의 구간가법성에 의해

$$\int_{\gamma_1 + \gamma_2} f\,dz = \int_a^c f(\gamma(t))\gamma'(t)\,dt = \int_a^b f(\gamma_1(t))\gamma_1'(t)\,dt + \int_b^c f(\gamma_2(t))\gamma_2'(t)\,dt$$

이고 이는 $$\int_{\gamma_1} f\,dz + \int_{\gamma_2} f\,dz$$이다.

</details>

명제 4의 둘째 항은 적분값이 곡선의 자취와 그 진행 방향만으로 결정되고 구체적인 매개변수 선택에는 무관함을 말한다. 단조 증가 재매개화는 같은 자취를 같은 방향으로 다시 훑는 것이므로, 가령 단위원을 $$e^{it}$$로 한 바퀴 돌든 $$e^{2\pi i s^2}$$ 류로 속도를 바꿔 돌든 적분값이 같다. 셋째 항의 역방향 부호는 정적분 $$\int_a^b = -\int_b^a$$의 복소판이며, 넷째 항과 결합하면 닫힌 곡선을 여러 호로 쪼개 따로 적분한 뒤 합산할 수 있게 해 준다. 다음으로 적분의 크기를 곡선의 길이로 가늠하는 부등식을 세우는데, 이를 위해 곡선의 길이를 정의한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> piecewise $$C^1$$ 곡선 $$\gamma : [a, b] \to \mathbb{C}$$의 *길이<sub>length</sub>*를

$$\mathrm{length}(\gamma) = \int_a^b \lvert \gamma'(t)\rvert\,dt$$

로 정의한다.

</div>

피적분함수 $$\lvert\gamma'(t)\rvert = \sqrt{x'(t)^2 + y'(t)^2}$$은 곡선의 순간 속력이므로, 그 적분은 곡선을 따라 이동한 총 거리, 곧 호의 길이이다. 가령 단위원 $$\gamma(t) = e^{it}$$ ($$t \in [0, 2\pi]$$) 은 $$\lvert\gamma'(t)\rvert = \lvert i e^{it}\rvert = 1$$이라 $$\mathrm{length}(\gamma) = \int_0^{2\pi} 1\,dt = 2\pi$$로, 반지름 $$1$$인 원의 둘레와 일치한다. 이 길이를 써서 경로적분의 크기를 위로 어림한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6 (ML 부등식)**</ins> $$\gamma : [a, b] \to \mathbb{C}$$가 piecewise $$C^1$$ 곡선이고 $$f$$가 $$\gamma$$의 자취 위에서 연속이라 하자. 그러면

$$\left\lvert \int_\gamma f(z)\,dz \right\rvert \leq \Bigl(\sup_{z \in \gamma([a,b])} \lvert f(z)\rvert\Bigr)\,\mathrm{length}(\gamma)$$

이다. 특히 $$\gamma$$의 자취 위에서 $$\lvert f\rvert \leq M$$이고 $$L = \mathrm{length}(\gamma)$$이면 $$\bigl\lvert\int_\gamma f\,dz\bigr\rvert \leq ML$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 임의의 복소숫값 연속함수 $$g : [a, b] \to \mathbb{C}$$에 대하여 $$\bigl\lvert\int_a^b g\,dt\bigr\rvert \leq \int_a^b \lvert g\rvert\,dt$$임에 유의한다. 적분값 $$I = \int_a^b g\,dt$$가 $$0$$이면 자명하고, $$I \neq 0$$이면 $$I = \lvert I\rvert e^{i\theta}$$로 적어 $$e^{-i\theta}$$를 곱하면

$$\lvert I\rvert = e^{-i\theta} I = \int_a^b e^{-i\theta} g(t)\,dt = \Real \int_a^b e^{-i\theta} g(t)\,dt = \int_a^b \Real\bigl(e^{-i\theta} g(t)\bigr)\,dt$$

이다 ($$\lvert I\rvert$$이 실수이므로 가운데 적분은 자기 실수부와 같다). 피적분함수에 $$\Real w \leq \lvert w\rvert$$를 적용하면 $$\Real(e^{-i\theta}g(t)) \leq \lvert e^{-i\theta}g(t)\rvert = \lvert g(t)\rvert$$이므로 $$\lvert I\rvert \leq \int_a^b \lvert g(t)\rvert\,dt$$이다.

이를 $$g(t) = f(\gamma(t))\gamma'(t)$$에 적용하면

$$\left\lvert \int_\gamma f\,dz \right\rvert = \left\lvert \int_a^b f(\gamma(t))\gamma'(t)\,dt \right\rvert \leq \int_a^b \lvert f(\gamma(t))\rvert\,\lvert\gamma'(t)\rvert\,dt$$

이다. 자취 위에서 $$\lvert f(\gamma(t))\rvert \leq \sup_{z}\lvert f(z)\rvert =: M$$이므로 우변은 $$M\int_a^b \lvert\gamma'(t)\rvert\,dt = M\,\mathrm{length}(\gamma)$$ 이하이다.

</details>

ML 부등식은 적분의 정확한 값을 모르더라도 그 크기에 상한을 주므로, 곡선을 변형시키며 적분이 $$0$$으로 가는지를 가늠하는 데 두루 쓰인다. 이름의 $$M$$은 피적분함수의 최댓값(maximum), $$L$$은 곡선의 길이(length)를 가리킨다. 가령 반지름 $$R$$인 원호 위에서 $$\lvert f\rvert \leq M_R$$이고 $$M_R \cdot R \to 0$$이면 그 호를 따른 적분이 $$0$$으로 감을 즉시 알 수 있는데, 이런 어림이 닫힌 곡선 적분의 평가에서 결정적 역할을 한다.

## 원시함수와 미적분의 기본정리

실변수에서 미적분의 기본정리는 적분을 원시함수의 양 끝값 차로 환원한다. 같은 정리가 복소경로적분에도 성립하며, 그 귀결로 원시함수를 갖는 함수의 적분은 경로와 무관하게 끝점만으로 결정된다. 이것이 복소적분 이론의 첫 번째 큰 단순화이다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 열린집합 $$\Omega \subseteq \mathbb{C}$$ 위의 함수 $$f$$에 대하여, $$\Omega$$에서 정칙이고 $$F'(z) = f(z)$$ ($$z \in \Omega$$) 를 만족하는 함수 $$F$$를 $$f$$의 *원시함수<sub>primitive</sub>* 혹은 *antiderivative<sub>역도함수</sub>*라 한다.

</div>

원시함수는 실변수의 부정적분에 해당하는 복소판이며, 정칙함수 $$F$$의 도함수 $$F'$$이 다시 $$f$$가 되는 관계로 정의된다. 가령 $$n \geq 0$$인 정수에 대해 $$z^n$$은 평면 전체에서 원시함수 $$z^{n+1}/(n+1)$$을 가지고, $$e^z$$는 자기 자신을 원시함수로 가진다 ([§정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10)에서 $$(e^z)' = e^z$$). 원시함수가 존재할 때, 경로적분은 다음과 같이 끝값의 차로 환원된다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (경로적분에 대한 미적분의 기본정리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 열려 있고 $$f$$가 $$\Omega$$에서 연속이며 $$F$$가 $$\Omega$$ 위의 $$f$$의 원시함수라 하자. 그러면 시점 $$\gamma(a)$$, 종점 $$\gamma(b)$$를 갖고 자취가 $$\Omega$$에 들어 있는 임의의 piecewise $$C^1$$ 곡선 $$\gamma : [a, b] \to \mathbb{C}$$에 대하여

$$\int_\gamma f(z)\,dz = F(\gamma(b)) - F(\gamma(a))$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\gamma$$이 한 구간 $$[a, b]$$ 전체에서 $$C^1$$인 경우를 본다. 합성함수 $$t \mapsto F(\gamma(t))$$를 생각하면, $$F$$가 정칙이므로 정칙함수의 합성에 대한 미분 규칙 ([§정칙함수, ⁋명제 3](/ko/math/complex_analysis/holomorphic_functions#prop3)) 에 의해

$$\frac{d}{dt}F(\gamma(t)) = F'(\gamma(t))\,\gamma'(t) = f(\gamma(t))\,\gamma'(t)$$

이다. 따라서 정의 2의 피적분함수가 정확히 $$H(t) = F(\gamma(t))$$의 도함수 $$H'(t)$$이고, 실변수 미적분의 기본정리를 실허부에 각각 적용하면

$$\int_\gamma f\,dz = \int_a^b H'(t)\,dt = H(b) - H(a) = F(\gamma(b)) - F(\gamma(a))$$

이다. 일반적인 piecewise $$C^1$$ 곡선의 경우, 분할 $$a = t_0 < \cdots < t_n = b$$의 각 부분구간 $$[t_{k-1}, t_k]$$에서 $$\gamma$$이 $$C^1$$이므로 위 결과를 적용하면

$$\int_\gamma f\,dz = \sum_{k=1}^n \bigl( F(\gamma(t_k)) - F(\gamma(t_{k-1})) \bigr) = F(\gamma(t_n)) - F(\gamma(t_0)) = F(\gamma(b)) - F(\gamma(a))$$

로, 중간항이 망원합으로 소거되어 같은 결론을 얻는다.

</details>

정리 8의 우변은 곡선의 시점과 종점에만 의존하고 그 사이를 어떤 경로로 잇는지에는 전혀 무관하다. 이로부터 원시함수의 존재가 곧 경로 독립성과 닫힌 경로 적분의 소멸로 번역됨이 따라 나온다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> $$\Omega \subseteq \mathbb{C}$$가 열려 있고 연속함수 $$f$$가 $$\Omega$$에서 원시함수 $$F$$를 가진다고 하자. 그러면 다음이 성립한다.

1. (경로 독립) 자취가 $$\Omega$$에 들어 있고 시점·종점이 같은 두 piecewise $$C^1$$ 곡선 $$\gamma_1, \gamma_2$$에 대하여 $$\displaystyle\int_{\gamma_1} f\,dz = \int_{\gamma_2} f\,dz$$이다.
2. (닫힌 경로) 자취가 $$\Omega$$에 들어 있는 임의의 닫힌 piecewise $$C^1$$ 곡선 $$\gamma$$에 대하여 $$\displaystyle\oint_\gamma f\,dz = 0$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

(1) $$\gamma_1, \gamma_2$$이 공통 시점 $$p$$와 공통 종점 $$q$$를 가진다고 하자. 정리 8을 각각에 적용하면 $$\int_{\gamma_1} f\,dz = F(q) - F(p) = \int_{\gamma_2} f\,dz$$이다.

(2) $$\gamma$$이 닫혀 있으면 시점과 종점이 같은 점 $$p = \gamma(a) = \gamma(b)$$이므로, 정리 8에 의해 $$\oint_\gamma f\,dz = F(p) - F(p) = 0$$이다.

</details>

따름정리 9는 원시함수의 존재가 적분을 얼마나 단순하게 만드는지를 보여 준다. 원시함수가 있으면 적분은 사실상 끝값의 뺄셈이고, 닫힌 곡선을 따라 한 바퀴 돌면 출발점으로 돌아와 차가 $$0$$이 된다. 거꾸로 보면, 어떤 닫힌 곡선에서 적분이 $$0$$이 아니라는 사실은 그 함수가 해당 영역에서 원시함수를 가질 수 없다는 강한 증거가 된다. 바로 이 현상이 다음 절의 핵심 계산에서 드러난다.

## 핵심 계산: ∮dz/z

지금까지의 도구를 $$f(z) = z^n$$ 꼴의 멱함수에 적용하여, 원점을 둘러싼 원 위에서의 적분을 모든 정수 $$n$$에 대해 계산한다. 그 결과는 $$n = -1$$이라는 단 하나의 지수에서만 적분이 $$0$$이 아닌 값을 주는 극적인 형태를 띤다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$r > 0$$이고 $$\gamma_r(t) = r e^{it}$$ ($$t \in [0, 2\pi]$$) 이 반시계방향으로 한 바퀴 도는 원이라 하자. 그러면 임의의 정수 $$n$$에 대하여

$$\oint_{\gamma_r} z^n\,dz = \begin{cases} 2\pi i, & n = -1, \\ 0, & n \neq -1 \end{cases}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\gamma_r(t) = r e^{it}$$이면 $$\gamma_r'(t) = i r e^{it}$$이고 자취 위에서 $$z^n = r^n e^{int}$$이므로

$$\oint_{\gamma_r} z^n\,dz = \int_0^{2\pi} r^n e^{int}\,(i r e^{it})\,dt = i\, r^{n+1}\int_0^{2\pi} e^{i(n+1)t}\,dt$$

이다. $$n = -1$$이면 지수가 $$0$$이 되어 피적분함수가 $$1$$이므로

$$\oint_{\gamma_r} z^{-1}\,dz = i\,r^0 \int_0^{2\pi} 1\,dt = i \cdot 2\pi = 2\pi i$$

이다 (반지름 $$r$$에 무관함에 유의한다). $$n \neq -1$$이면 $$m = n + 1$$이 $$0$$이 아닌 정수이고

$$\int_0^{2\pi} e^{imt}\,dt = \left[ \frac{e^{imt}}{im} \right]_0^{2\pi} = \frac{e^{2\pi i m} - 1}{im} = 0$$

인데, $$m$$이 정수이므로 $$e^{2\pi i m} = 1$$ ([§복소수와 복소평면, ⁋정의 5](/ko/math/complex_analysis/complex_numbers#def5)의 Euler 형식에서 $$e^{2\pi i m} = \cos(2\pi m) + i\sin(2\pi m) = 1$$) 이기 때문이다. 따라서 $$n \neq -1$$이면 적분이 $$0$$이다.

</details>

명제 10의 두 경우를 따름정리 9에 비추어 해석하면, 이 글 전체의 결론이 또렷해진다. $$n \neq -1$$인 멱함수 $$z^n$$은 적분이 $$0$$인데, 이는 우연이 아니라 $$z^n$$이 원시함수 $$z^{n+1}/(n+1)$$을 가지기 때문이다. $$n \geq 0$$이면 이 원시함수가 평면 전체에서 정칙이고, $$n \leq -2$$이면 원점을 뺀 영역 $$\mathbb{C}\setminus\{0\}$$에서 정칙이어서, 어느 경우든 원 $$\gamma_r$$의 자취를 품는 영역에서 원시함수가 존재하므로 따름정리 9에 의해 적분이 $$0$$이다. 유독 $$n = -1$$, 곧 $$f(z) = 1/z$$만이 예외인데, 적분값 $$2\pi i \neq 0$$은 따름정리 9에 의해 $$1/z$$이 원 $$\gamma_r$$의 자취를 포함하는 어떤 영역에서도 원시함수를 가질 수 없음을 뜻한다.

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> $$1/z$$이 원시함수를 가지지 못하는 까닭은 그 자연스러운 원시함수인 복소로그함수 $$\log z$$가 원점을 둘러싼 영역에서 단일한 값으로 정의되지 않기 때문이다. 곡선을 따라 한 바퀴 돌면 편각 $$\arg z$$가 ([§복소수와 복소평면, ⁋정의 5](/ko/math/complex_analysis/complex_numbers#def5)) $$2\pi$$만큼 증가하여 $$\log z$$의 허수부가 $$2\pi i$$만큼 점프하는데, 명제 10의 $$2\pi i$$가 바로 이 점프의 크기이다. 이는 $$1/z$$이 국소적으로는(원점을 둘러싸지 않는 작은 영역에서는) 원시함수를 갖지만 전역적으로는 갖지 못한다는 뜻으로, 영역의 위상이 적분에 개입하는 첫 신호이다.

</div>

명제 10은 작아 보이지만, 닫힌 곡선 적분이 피적분함수의 특이점을 어떻게 감지하는가를 보여 주는 원형이다. 적분값 $$2\pi i$$는 반지름 $$r$$에 무관하게 항상 같으며, 이는 원을 연속적으로 부풀리거나 수축시켜도 그 안에 갇힌 원점이라는 특이점이 그대로 남아 있는 한 적분이 변하지 않음을 시사한다. 이 불변성은 같은 두 끝점을 잇되 특이점을 사이에 두고 양쪽으로 갈라지는 두 경로의 적분이 서로 다를 수 있다는 사실, 곧 경로 독립성이 영역의 위상에 의존한다는 사실과 동전의 양면이다.

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
</content>
</invoke>
