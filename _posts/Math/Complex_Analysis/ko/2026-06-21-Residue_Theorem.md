---
title: "유수정리"
description: "고립특이점에서의 Laurent 계수 a_{-1}을 유수로 정의하고, 닫힌 경로 안에 유한개의 고립특이점만 갖는 정칙함수의 적분이 유수와 회전수의 합으로 결정된다는 유수정리를 Laurent 전개와 Cauchy 정리로 증명한다. 단순극과 고차극에서의 유수 계산법을 확립하고, 실수 위의 무한적분, 삼각함수 적분, 무한급수의 합 계산에 응용한다."
excerpt: "residue, 유수정리, 단순극과 고차극의 유수, 반원 contour, Jordan 보조정리, 삼각함수 적분, π cot πz 무한급수 합"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/residue_theorem
sidebar: 
    nav: "complex_analysis-ko"

date: 2026-06-21
weight: 9

published: false
---

Cauchy 정리는 정칙함수의 닫힌 경로 적분이 소멸함을 알려 주었지만 ([§Cauchy 정리, ⁋따름정리 8](/ko/math/complex_analysis/cauchy_theorem#cor8)), 정작 계산에서 흥미로운 적분은 피적분함수가 경로 안에서 특이점을 가져 적분이 $$0$$이 아닌 경우이다. 가령 $$\oint dz/z = 2\pi i$$는 원점이라는 단 하나의 특이점 때문에 소멸하지 않으며, 그 값 $$2\pi i$$은 Laurent 전개 $$1/z$$의 음의 일차 계수가 $$1$$이라는 사실에서 정확히 나온다. 일반적으로 고립특이점 근방에서 함수는 Laurent 급수로 전개되고 ([§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2)), 그 음의 일차 계수 $$a_{-1}$$만이 작은 원을 따른 적분에 살아남는다. 이 계수를 유수라 부르며, 유수정리는 닫힌 경로 적분이 경로 안에 든 특이점들의 유수를 회전수로 가중하여 합한 것임을 말한다. 이로써 적분 계산은 국소적인 유수 계산으로 환원되고, 그 위력은 복소적분 자체를 넘어 실수 위의 정적분과 무한급수의 합을 닫힌 형태로 구하는 데까지 미친다. 이 글은 유수를 정의하고 유수정리를 확립한 뒤, 극에서의 유수 계산법과 세 갈래의 표준적 응용을 다룬다.

## 유수와 유수정리

고립특이점 $$z_0$$ 근방에서 정칙인 함수 $$f$$는 구멍 뚫린 원판 $$0 < \lvert z - z_0\rvert < R$$에서 Laurent 전개 $$f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$을 가진다. 이 전개의 계수 가운데 음의 일차 계수 $$a_{-1}$$이 특별한 지위를 가지는데, 작은 원을 따라 항별로 적분하면 정수 멱 $$(z - z_0)^n$$의 적분이 $$n = -1$$일 때만 $$2\pi i$$이고 나머지는 모두 $$0$$이기 때문이다. 따라서 $$a_{-1}$$만이 적분에 흔적을 남긴다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1 (유수)**</ins> $$f$$가 $$z_0$$에서 고립특이점을 가지고 $$0 < \lvert z - z_0\rvert < R$$에서의 Laurent 전개가 $$f(z) = \sum_{n=-\infty}^{\infty} a_n (z - z_0)^n$$이라 하자. 이때 음의 일차 계수 $$a_{-1}$$을 $$f$$의 $$z_0$$에서의 *residue<sub>유수</sub>*라 하고

$$\operatorname{Res}_{z = z_0} f = a_{-1}$$

로 적는다.

</div>

유수는 Laurent 전개에서 단 하나의 계수만을 뽑아낸 양이지만, 정의 1의 계수공식 ([§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2)) 에 $$n = -1$$을 대입하면

$$\operatorname{Res}_{z = z_0} f = a_{-1} = \frac{1}{2\pi i}\oint_{\lvert z - z_0\rvert = \rho} f(z)\,dz$$

이 되어, 유수가 작은 원을 따른 적분과 직결됨을 곧장 본다. 곧 한 특이점을 반시계방향으로 한 번 감는 작은 원에서의 적분은 정확히 그 점에서의 유수에 $$2\pi i$$을 곱한 것이다. 유수정리는 이 국소적 관찰을 임의의 닫힌 경로로 끌어올린다. 경로 안에 여러 특이점이 있으면 각 특이점을 작은 원으로 도려내고, 그 사이의 영역에서 정칙성과 Cauchy 정리를 써서 큰 경로의 적분을 작은 원들의 적분 합으로 분해한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (유수정리)**</ins> $$\Omega \subseteq \mathbb{C}$$가 단순연결 영역이고, $$z_1, \dots, z_k$$이 $$\Omega$$ 안의 서로 다른 유한개의 점이라 하자. $$f$$가 $$\Omega \setminus \{z_1, \dots, z_k\}$$에서 정칙이고 각 $$z_j$$에서 고립특이점을 가진다고 하자. 그러면 자취가 $$\Omega \setminus \{z_1, \dots, z_k\}$$에 들어 있는 임의의 닫힌 piecewise $$C^1$$ 곡선 $$\gamma$$에 대하여

$$\oint_\gamma f(z)\,dz = 2\pi i \sum_{j=1}^{k} n(\gamma, z_j)\operatorname{Res}_{z = z_j} f$$

이다. 여기서 $$n(\gamma, z_j)$$은 $$\gamma$$의 $$z_j$$에 대한 회전수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각 특이점 $$z_j$$에서의 Laurent 전개의 주부를 떼어 내어 적분을 분해한다. $$z_j$$의 구멍 뚫린 근방에서 $$f$$의 Laurent 전개의 주부를

$$P_j(z) = \sum_{n=1}^{\infty} a_{-n}^{(j)}(z - z_j)^{-n}$$

이라 하자. 여기서 $$a_{-n}^{(j)}$$은 $$z_j$$에서의 Laurent 계수이다. 주부 $$P_j$$은 변수치환 $$\zeta = (z - z_j)^{-1}$$로 보면 $$\zeta$$의 멱급수이므로 $$z \neq z_j$$인 모든 점, 곧 $$\mathbb{C} \setminus \{z_j\}$$에서 수렴하여 정칙함수를 정의한다 ([§고립특이점과 Laurent 급수, ⁋정리 2](/ko/math/complex_analysis/isolated_singularities#thm2) 뒤의 주부 수렴역).

이제 함수

$$g(z) = f(z) - \sum_{j=1}^{k} P_j(z)$$

을 생각한다. 각 $$z_j$$ 근방에서 $$f$$의 주부는 정확히 $$P_j$$이고 다른 $$P_\ell$$ ($$\ell \neq j$$) 은 $$z_j$$에서 정칙이므로, $$g$$의 $$z_j$$에서의 Laurent 전개에는 주부가 남지 않는다. 따라서 $$g$$는 각 $$z_j$$에서 가제거 특이점을 가지며 ([§고립특이점과 Laurent 급수, ⁋정의 4](/ko/math/complex_analysis/isolated_singularities#def4)), 그 점들을 메우면 $$g$$가 $$\Omega$$ 전체에서 정칙함수로 확장된다. $$\Omega$$가 단순연결이므로 Cauchy 정리 ([§Cauchy 정리, ⁋따름정리 8](/ko/math/complex_analysis/cauchy_theorem#cor8)) 에 의해

$$\oint_\gamma g(z)\,dz = 0, \qquad \text{곧}\qquad \oint_\gamma f(z)\,dz = \sum_{j=1}^{k}\oint_\gamma P_j(z)\,dz$$

이다.

각 주부의 적분을 계산한다. 주부 $$P_j$$은 $$\mathbb{C} \setminus \{z_j\}$$에서 균등수렴하는 급수이므로 $$\gamma$$ 위에서 항별로 적분할 수 있고,

$$\oint_\gamma P_j(z)\,dz = \sum_{n=1}^{\infty} a_{-n}^{(j)}\oint_\gamma (z - z_j)^{-n}\,dz$$

이다. $$n \geq 2$$인 항에서는 $$(z - z_j)^{-n}$$이 $$\mathbb{C} \setminus \{z_j\}$$에서 원시함수 $$(z - z_j)^{-n+1}/(-n+1)$$을 가지므로 닫힌 경로 적분이 $$0$$이다 ([§복소적분, ⁋따름정리 9](/ko/math/complex_analysis/complex_integration#cor9)). $$n = 1$$인 항만 살아남고, 회전수의 정의 ([§Cauchy 정리, ⁋정의 9](/ko/math/complex_analysis/cauchy_theorem#def9)) 에 의해

$$\oint_\gamma (z - z_j)^{-1}\,dz = 2\pi i\, n(\gamma, z_j)$$

이므로 $$\oint_\gamma P_j\,dz = a_{-1}^{(j)} \cdot 2\pi i\, n(\gamma, z_j) = 2\pi i\, n(\gamma, z_j)\operatorname{Res}_{z=z_j} f$$이다. 이를 $$j$$에 대해 더하면 주장하는 등식을 얻는다.

</details>

유수정리는 닫힌 경로 적분이라는 전역적 양을, 경로가 감는 특이점들에서의 국소적 양인 유수로 완전히 분해한다. 회전수 인자 $$n(\gamma, z_j)$$은 경로가 각 특이점을 몇 번 감는지를 세므로, 경로 밖의 특이점은 $$n(\gamma, z_j) = 0$$이 되어 적분에 기여하지 않는다. 실제 응용에서는 거의 항상 $$\gamma$$이 각 특이점을 반시계방향으로 정확히 한 번 감는 단순 닫힌 곡선이며, 이때 안쪽 특이점에서는 $$n(\gamma, z_j) = 1$$, 바깥 특이점에서는 $$0$$이 되어 공식이

$$\oint_\gamma f(z)\,dz = 2\pi i \sum_{z_j \text{ 안쪽}} \operatorname{Res}_{z = z_j} f$$

로 간단해진다. 이 형태가 모든 계산의 출발점이며, 남은 과제는 각 극에서의 유수를 Laurent 전개를 직접 구하지 않고 빠르게 계산하는 것이다.

## 극에서의 유수 계산

유수가 적분을 결정하는 유일한 계수이므로, 그것을 Laurent 전개 전체를 구하지 않고 뽑아내는 방법이 필요하다. 극의 경우 주부가 유한 개의 항으로 이루어지므로 ([§고립특이점과 Laurent 급수, ⁋정의 4](/ko/math/complex_analysis/isolated_singularities#def4)), 적당히 인수를 곱하고 극한을 취하거나 미분하여 $$a_{-1}$$만을 깔끔하게 끄집어낼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (극에서의 유수)**</ins> $$f$$가 $$z_0$$에서 위수 $$m$$인 극을 가진다고 하자. 그러면

$$\operatorname{Res}_{z = z_0} f = \frac{1}{(m-1)!}\lim_{z \to z_0}\frac{d^{m-1}}{dz^{m-1}}\Bigl[(z - z_0)^m f(z)\Bigr]$$

이다. 특히 단순극 ($$m = 1$$) 의 경우

$$\operatorname{Res}_{z = z_0} f = \lim_{z \to z_0}(z - z_0)f(z)$$

이고, $$f = g/h$$이며 $$g, h$$가 $$z_0$$에서 정칙이고 $$g(z_0) \neq 0$$, $$h(z_0) = 0$$, $$h'(z_0) \neq 0$$이면

$$\operatorname{Res}_{z = z_0} \frac{g}{h} = \frac{g(z_0)}{h'(z_0)}$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z_0$$이 위수 $$m$$인 극이면 Laurent 전개가 $$f(z) = \sum_{n=-m}^{\infty} a_n (z - z_0)^n$$ ($$a_{-m} \neq 0$$) 이다. $$(z - z_0)^m$$을 곱하면

$$(z - z_0)^m f(z) = \sum_{n=-m}^{\infty} a_n (z - z_0)^{n+m} = \sum_{k=0}^{\infty} a_{k-m}(z - z_0)^k$$

이 되어, 이는 $$z_0$$에서 정칙한 멱급수이다. 이 멱급수의 $$k$$차 계수는 $$a_{k-m}$$이고, 우리가 원하는 유수 $$a_{-1}$$은 $$k - m = -1$$, 곧 $$k = m - 1$$인 항의 계수이다. 정칙함수의 Taylor 계수는 미분으로 추출되므로 ([§멱급수와 해석성, ⁋정리 1](/ko/math/complex_analysis/power_series_and_analyticity#thm1)),

$$a_{-1} = a_{(m-1)-m} = \frac{1}{(m-1)!}\frac{d^{m-1}}{dz^{m-1}}\Bigl[(z - z_0)^m f(z)\Bigr]\bigg\rvert_{z = z_0} = \frac{1}{(m-1)!}\lim_{z \to z_0}\frac{d^{m-1}}{dz^{m-1}}\Bigl[(z - z_0)^m f(z)\Bigr]$$

이다. 미분한 멱급수가 $$z_0$$에서 정칙이므로 극한과 대입이 일치한다.

단순극은 $$m = 1$$인 경우로 $$(m-1)! = 1$$이고 미분 차수가 $$0$$이므로 $$\operatorname{Res} = \lim_{z\to z_0}(z - z_0)f(z)$$이다. 끝으로 $$f = g/h$$ 꼴에서 $$h(z_0) = 0$$, $$h'(z_0) \neq 0$$이면 $$h$$가 $$z_0$$에서 단순영점을 가지므로 $$g(z_0) \neq 0$$과 더불어 $$f$$가 $$z_0$$에서 단순극을 가진다 ([§고립특이점과 Laurent 급수, ⁋명제 6](/ko/math/complex_analysis/isolated_singularities#prop6)). 단순극 공식에 대입하면

$$\operatorname{Res}_{z = z_0}\frac{g}{h} = \lim_{z \to z_0}(z - z_0)\frac{g(z)}{h(z)} = \lim_{z \to z_0} g(z)\cdot \frac{z - z_0}{h(z) - h(z_0)} = g(z_0)\cdot\frac{1}{h'(z_0)}$$

인데, 마지막 등식은 $$h(z_0) = 0$$이라 $$h(z) = h(z) - h(z_0)$$이고 그 차분비의 극한이 $$h'(z_0)$$이기 때문이다.

</details>

명제 3은 극의 위수에 맞춰 적용해야 한다. 단순극에서는 인수 $$(z - z_0)$$를 곱하고 극한만 취하면 되지만, 위수가 높아질수록 $$m - 1$$번 미분해야 하므로 계산이 무거워진다. 분모의 영점으로 생기는 단순극에서는 마지막 공식 $$g(z_0)/h'(z_0)$$이 가장 효율적인데, 분모를 인수분해할 필요 없이 도함수 한 번으로 유수가 나온다. 두 가지 구체적 예로 감을 잡아 둔다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4 (단순극과 이차극의 유수)**</ins> 먼저 $$f(z) = \dfrac{z}{(z - 1)(z + 2)}$$의 두 단순극에서의 유수를 구한다. $$z = 1$$에서는 인수 $$(z - 1)$$을 곱해

$$\operatorname{Res}_{z = 1} f = \lim_{z \to 1}(z - 1)\frac{z}{(z - 1)(z + 2)} = \lim_{z \to 1}\frac{z}{z + 2} = \frac{1}{3}$$

이고, $$z = -2$$에서는

$$\operatorname{Res}_{z = -2} f = \lim_{z \to -2}\frac{z}{z - 1} = \frac{-2}{-3} = \frac{2}{3}$$

이다.

다음으로 $$g(z) = \dfrac{e^z}{(z - 1)^2}$$의 $$z = 1$$에서의 이차극을 본다. 위수 $$m = 2$$이므로 명제 3에서 $$(z - 1)^2 g(z) = e^z$$을 한 번 미분하고 극한을 취해

$$\operatorname{Res}_{z = 1} g = \frac{1}{(2 - 1)!}\lim_{z \to 1}\frac{d}{dz}\Bigl[(z - 1)^2 \frac{e^z}{(z - 1)^2}\Bigr] = \lim_{z \to 1}\frac{d}{dz}e^z = e$$

를 얻는다. 만일 일차극에서처럼 $$(z-1)g(z)=e^z/(z-1)$$의 극한을 취하려 하면 $$z\to1$$에서 발산하여 유수를 얻지 못한다. 이차극에서는 $$(z-1)^2 g(z)=e^z$$를 한 번 미분한 뒤 극한을 취해야 올바른 유수 $$e$$가 나오며, 이 예가 그 미분 단계의 필요성을 보여 준다.

</div>

## 실수 위의 무한적분

유수정리의 첫 응용은 실수 전체에 걸친 정적분 $$\int_{-\infty}^{\infty} f(x)\,dx$$의 계산이다. 발상은 실축 구간 $$[-R, R]$$을 상반평면의 반원호로 닫아 닫힌 경로를 만들고, 그 경로의 적분을 유수정리로 계산한 뒤, 반원호 위의 적분이 $$R \to \infty$$에서 사라짐을 보여 실축 적분만 남기는 것이다. 반원호의 기여가 사라지려면 피적분함수가 큰 $$\lvert z\rvert$$에서 충분히 빨리 작아져야 하며, 유리함수의 경우 분모의 차수가 분자보다 $$2$$ 이상 크면 충분하다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (유리함수의 무한적분)**</ins> $$f = P/Q$$가 유리함수이고 $$P, Q$$가 다항식이라 하자. $$Q$$가 실축 위에서 영점을 갖지 않고 $$\deg Q \geq \deg P + 2$$이면

$$\int_{-\infty}^{\infty} f(x)\,dx = 2\pi i \sum_{\Img z_j > 0} \operatorname{Res}_{z = z_j} f$$

이며, 합은 상반평면에 있는 $$f$$의 극 전체에 걸친다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

반지름 $$R$$인 상반평면 반원 경계 $$\gamma_R$$을, 실축 위의 선분 $$[-R, R]$$과 그 위를 잇는 반원호 $$C_R = \{Re^{i\theta} : 0 \leq \theta \leq \pi\}$$를 이어붙인 닫힌 경로로 잡는다. $$R$$을 모든 극의 절댓값보다 크게 잡으면 상반평면의 극이 모두 $$\gamma_R$$ 안에 들고 각각 회전수가 $$1$$이므로, 유수정리 (정리 2) 에 의해

$$\int_{-R}^{R} f(x)\,dx + \int_{C_R} f(z)\,dz = 2\pi i \sum_{\Img z_j > 0}\operatorname{Res}_{z = z_j} f$$

이다. 이제 반원호 적분이 $$R \to \infty$$에서 $$0$$으로 감을 보인다. $$\deg Q \geq \deg P + 2$$이므로 충분히 큰 $$\lvert z\rvert$$에서 어떤 상수 $$M$$이 있어 $$\lvert f(z)\rvert \leq M/\lvert z\rvert^2$$이고, 따라서 $$C_R$$ 위에서 $$\lvert f(z)\rvert \leq M/R^2$$이다. ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 으로

$$\left\lvert \int_{C_R} f(z)\,dz\right\rvert \leq \frac{M}{R^2}\cdot \pi R = \frac{\pi M}{R} \xrightarrow[R \to \infty]{} 0$$

이다. 한편 $$\deg Q \geq \deg P + 2$$이라 $$f$$가 실축 위에서 절대적분가능하므로 $$\int_{-R}^{R} f\,dx \to \int_{-\infty}^{\infty} f\,dx$$이다. $$R \to \infty$$의 극한을 취하면 주장하는 등식을 얻는다.

</details>

명제 5의 증명에서 결정적인 단계는 반원호 위 적분의 소멸이며, 이것이 차수 조건 $$\deg Q \geq \deg P + 2$$의 존재 이유이다. 차이가 정확히 $$1$$뿐이면 $$\lvert f\rvert \sim 1/R$$이라 ML 어림이 $$\pi M$$이라는 상수로만 유계여서 소멸을 보장하지 못한다. 같은 반원 기법은 분자에 $$e^{iax}$$ 같은 진동인자가 붙은 경우에도 통하지만, 이때는 $$C_R$$ 위에서 $$\lvert e^{iaz}\rvert = e^{-a\Img z}$$이 상반평면에서 감소함을 활용하는 더 섬세한 어림이 필요하며, 이를 정리한 것이 Jordan 보조정리이다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6 (Jordan)**</ins> $$a > 0$$이라 하자. $$f$$가 상반평면의 반원호 $$C_R = \{Re^{i\theta} : 0 \leq \theta \leq \pi\}$$ 위에서 연속이고, $$M(R) = \max_{z \in C_R}\lvert f(z)\rvert \to 0$$ ($$R \to \infty$$) 이면

$$\lim_{R \to \infty}\int_{C_R} f(z)\,e^{iaz}\,dz = 0$$

이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$z = Re^{i\theta}$$로 매개변수화하면 $$dz = iRe^{i\theta}\,d\theta$$이고 $$\lvert e^{iaz}\rvert = e^{-aR\sin\theta}$$이므로

$$\left\lvert \int_{C_R} f(z)e^{iaz}\,dz\right\rvert \leq \int_0^\pi \lvert f(Re^{i\theta})\rvert\, e^{-aR\sin\theta}\, R\,d\theta \leq M(R)\,R\int_0^\pi e^{-aR\sin\theta}\,d\theta$$

이다. 피적분함수가 $$\theta = \pi/2$$에 대해 대칭이므로 $$\int_0^\pi = 2\int_0^{\pi/2}$$이고, 구간 $$[0, \pi/2]$$에서 $$\sin\theta \geq 2\theta/\pi$$ (Jordan 부등식, $$\sin$$의 오목성에서 따름) 이므로

$$\int_0^{\pi/2} e^{-aR\sin\theta}\,d\theta \leq \int_0^{\pi/2} e^{-2aR\theta/\pi}\,d\theta = \frac{\pi}{2aR}\bigl(1 - e^{-aR}\bigr) \leq \frac{\pi}{2aR}$$

이다. 이를 합치면

$$\left\lvert \int_{C_R} f(z)e^{iaz}\,dz\right\rvert \leq M(R)\,R\cdot 2\cdot\frac{\pi}{2aR} = \frac{\pi}{a}M(R) \xrightarrow[R \to \infty]{} 0$$

이다.

</details>

보조정리 6의 핵심은 $$\sin\theta \geq 2\theta/\pi$$라는 부등식으로 지수 감소를 끌어내어, 적분 $$\int_0^\pi e^{-aR\sin\theta}\,d\theta$$이 $$R$$에 반비례하여 작아짐을 보인 데 있다. 이 $$1/R$$ 인자가 $$C_R$$의 길이에서 오는 $$R$$ 인자와 상쇄되어, $$\lvert f\rvert$$이 단지 $$0$$으로 가기만 하면 ($$\lvert f\rvert \sim 1/R^2$$일 필요 없이) 적분이 소멸한다. 덕분에 진동적분에서는 차수 조건이 $$\deg Q \geq \deg P + 1$$로 약화된다. 이를 Fourier 변환형 적분에 적용한다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7 (Fourier 적분)**</ins> 적분 $$\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{x^2 + 1}\,dx$$를 계산한다. $$\cos x = \Real(e^{ix})$$이므로 복소화하여 $$f(z) = \dfrac{e^{iz}}{z^2 + 1}$$을 상반평면 반원 경로에서 적분한다. 분모 $$z^2 + 1 = (z - i)(z + i)$$의 영점 가운데 상반평면에 있는 것은 $$z = i$$ 하나이고, 이는 단순극이다. 명제 3의 단순극 공식으로

$$\operatorname{Res}_{z = i} f = \frac{e^{iz}}{(z^2 + 1)'}\bigg\rvert_{z = i} = \frac{e^{iz}}{2z}\bigg\rvert_{z = i} = \frac{e^{i\cdot i}}{2i} = \frac{e^{-1}}{2i}$$

이다. 여기서 $$g(z) = e^{iz}$$, $$h(z) = z^2 + 1$$, $$h'(z) = 2z$$로 보아 $$g(i)/h'(i)$$ 공식을 썼다. 분자 $$\lvert e^{iz}\rvert = e^{-\Img z} \leq 1$$이 상반평면에서 유계이고 $$\lvert 1/(z^2+1)\rvert \to 0$$이므로 보조정리 6에 의해 반원호 적분이 소멸하여, 유수정리로

$$\int_{-\infty}^{\infty}\frac{e^{ix}}{x^2 + 1}\,dx = 2\pi i\cdot\frac{e^{-1}}{2i} = \frac{\pi}{e}$$

이다. 양변의 실수부를 취하면 $$\displaystyle\int_{-\infty}^{\infty}\frac{\cos x}{x^2 + 1}\,dx = \frac{\pi}{e}$$이다. 허수부는 $$0$$인데, 피적분함수 $$\sin x/(x^2 + 1)$$이 기함수라 적분이 소멸하는 것과 일치한다.

</div>

## 삼각함수의 정적분

$$0$$부터 $$2\pi$$까지 $$\sin\theta$$와 $$\cos\theta$$의 유리식을 적분하는 문제는 유수정리가 특히 깔끔하게 처리하는 또 다른 부류이다. 핵심 발상은 적분 구간 $$[0, 2\pi]$$를 단위원 한 바퀴로 보아 $$z = e^{i\theta}$$로 치환하는 것이다. 그러면 삼각함수가 $$z$$의 유리식이 되고, 실수 위의 적분이 단위원을 따른 복소적분으로 바뀌어 유수정리가 곧장 적용된다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (단위원 치환)**</ins> $$R(\cos\theta, \sin\theta)$$이 $$\cos\theta$$와 $$\sin\theta$$의 유리식이고 $$[0, 2\pi]$$에서 분모가 사라지지 않는다고 하자. 치환 $$z = e^{i\theta}$$ 아래

$$\cos\theta = \frac{1}{2}\Bigl(z + \frac{1}{z}\Bigr), \qquad \sin\theta = \frac{1}{2i}\Bigl(z - \frac{1}{z}\Bigr), \qquad d\theta = \frac{dz}{iz}$$

이며,

$$\int_0^{2\pi} R(\cos\theta, \sin\theta)\,d\theta = \oint_{\lvert z\rvert = 1} R\Bigl(\tfrac{1}{2}(z + z^{-1}),\, \tfrac{1}{2i}(z - z^{-1})\Bigr)\frac{dz}{iz} = 2\pi i\sum_{\lvert z_j\rvert < 1}\operatorname{Res}_{z = z_j} F$$

이다. 여기서 $$F(z)$$은 가운데 적분의 피적분함수이고, 합은 단위원판 안의 극 전체에 걸친다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\theta$$가 $$0$$부터 $$2\pi$$까지 증가하면 $$z = e^{i\theta}$$이 단위원을 반시계방향으로 정확히 한 번 돈다. Euler 공식 ([§정칙함수, ⁋정의 10](/ko/math/complex_analysis/holomorphic_functions#def10)) 에서 $$e^{i\theta} = \cos\theta + i\sin\theta$$이고 $$e^{-i\theta} = \cos\theta - i\sin\theta$$이므로, 두 식을 더하고 빼면 $$\cos\theta = \tfrac12(e^{i\theta} + e^{-i\theta}) = \tfrac12(z + z^{-1})$$, $$\sin\theta = \tfrac{1}{2i}(e^{i\theta} - e^{-i\theta}) = \tfrac{1}{2i}(z - z^{-1})$$이다. 또 $$dz = ie^{i\theta}\,d\theta = iz\,d\theta$$이므로 $$d\theta = dz/(iz)$$이다.

이 치환을 적분에 대입하면 실수 적분이 단위원 $$\lvert z\rvert = 1$$을 따른 복소적분으로 바뀌고, 피적분함수 $$F(z) = R(\cdots)/(iz)$$은 $$z$$의 유리함수이다. 가정에서 $$R$$의 분모가 $$[0, 2\pi]$$의 $$\theta$$에 대해 사라지지 않으므로 $$F$$은 단위원 위 ($$\lvert z\rvert = 1$$) 에 극을 갖지 않고, 따라서 유한 개의 극이 단위원판 안팎에 흩어져 있다. 단위원이 안쪽 극을 각각 한 번 감으므로 유수정리 (정리 2) 에 의해 적분이 $$2\pi i$$ 곱하기 단위원판 안 극들의 유수 합이다.

</details>

명제 8은 삼각적분을 기계적으로 유수 계산으로 바꾼다. 치환 뒤 남는 일은 피적분함수 $$F(z)$$의 극 가운데 어느 것이 단위원판 $$\lvert z\rvert < 1$$ 안에 있는지 가려내고 그 유수를 더하는 것뿐이다. 분모가 $$z$$의 이차식이면 두 근의 곱이 상수항으로 주어지므로, 보통 한 근만 원판 안에 들어와 계산이 단순극 하나로 끝난다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9 (삼각적분)**</ins> $$a > 1$$일 때 $$\displaystyle\int_0^{2\pi}\frac{d\theta}{a + \cos\theta}$$를 구한다. $$z = e^{i\theta}$$로 치환하면 $$\cos\theta = \tfrac12(z + z^{-1})$$, $$d\theta = dz/(iz)$$이므로

$$\int_0^{2\pi}\frac{d\theta}{a + \cos\theta} = \oint_{\lvert z\rvert = 1}\frac{1}{a + \tfrac12(z + z^{-1})}\frac{dz}{iz} = \oint_{\lvert z\rvert = 1}\frac{2}{i}\frac{dz}{z^2 + 2az + 1}$$

이다. 분모 $$z^2 + 2az + 1$$의 근은 $$z_\pm = -a \pm \sqrt{a^2 - 1}$$이고, 두 근의 곱은 $$z_+ z_- = 1$$이다. $$a > 1$$이므로 $$z_+ = -a + \sqrt{a^2 - 1}$$은 $$\lvert z_+\rvert < 1$$로 단위원판 안에 있고 $$z_- = -a - \sqrt{a^2 - 1}$$은 밖에 있다. 따라서 $$F(z) = \dfrac{2}{i}\dfrac{1}{(z - z_+)(z - z_-)}$$의 단위원판 안 극은 단순극 $$z_+$$ 하나뿐이고, 그 유수는

$$\operatorname{Res}_{z = z_+} F = \frac{2}{i}\frac{1}{z_+ - z_-} = \frac{2}{i}\frac{1}{2\sqrt{a^2 - 1}} = \frac{1}{i\sqrt{a^2 - 1}}$$

이다. 유수정리로

$$\int_0^{2\pi}\frac{d\theta}{a + \cos\theta} = 2\pi i\cdot\frac{1}{i\sqrt{a^2 - 1}} = \frac{2\pi}{\sqrt{a^2 - 1}}$$

을 얻는다.

</div>

## 무한급수의 합

유수정리는 적분을 넘어 무한급수 $$\sum_{n} f(n)$$의 닫힌 합을 구하는 데에도 쓰인다. 발상은 정수 $$n$$에서 유수가 $$1$$인 보조함수를 곱해, 그 함수의 정수에서의 유수가 급수의 항 $$f(n)$$을 정확히 재현하도록 만드는 것이다. 이 역할에 꼭 맞는 함수가 $$\pi\cot\pi z$$인데, $$\cot\pi z = \cos\pi z/\sin\pi z$$의 분모 $$\sin\pi z$$이 정확히 정수에서 단순영점을 가지므로 $$\pi\cot\pi z$$이 각 정수에서 단순극을 가지고, 그 유수가 모두 $$1$$이기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10 (cotangent 합 공식)**</ins> $$f$$가 유리함수이고 $$\deg(\text{분모}) \geq \deg(\text{분자}) + 2$$이며, $$f$$의 극이 모두 정수가 아니라 하자. 그러면

$$\sum_{n = -\infty}^{\infty} f(n) = -\sum_{j}\operatorname{Res}_{z = z_j}\Bigl[\pi\cot(\pi z)\,f(z)\Bigr]$$

이다. 여기서 오른쪽 합은 $$f$$의 극 $$z_j$$ 전체에 걸친다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$\pi\cot\pi z$$이 각 정수 $$n$$에서 유수 $$1$$인 단순극을 가짐을 본다. $$\sin\pi z$$은 $$z = n$$에서 단순영점을 가지고 ($$(\sin\pi z)' = \pi\cos\pi z$$이 $$z = n$$에서 $$\pi(-1)^n \neq 0$$) $$\cos\pi n = (-1)^n \neq 0$$이므로, 명제 3의 $$g/h$$ 공식으로

$$\operatorname{Res}_{z = n}\pi\cot\pi z = \operatorname{Res}_{z = n}\frac{\pi\cos\pi z}{\sin\pi z} = \frac{\pi\cos\pi n}{\pi\cos\pi n} = 1$$

이다. 따라서 $$g_f(z) = \pi\cot(\pi z)f(z)$$은 각 정수 $$n$$ (단, $$f$$의 극이 아닌) 에서 단순극을 가지며, 그 유수는 $$f(n)$$이 정칙이므로

$$\operatorname{Res}_{z = n} g_f = f(n)\operatorname{Res}_{z = n}\pi\cot\pi z = f(n)$$

이다.

이제 한 변이 $$N + \tfrac12$$인 정사각형 경로 $$\Gamma_N$$을 잡는다. 곧 꼭짓점이 $$(\pm(N+\tfrac12), \pm(N+\tfrac12))$$인 정사각형의 경계를 반시계방향으로 도는 경로이다. 이 경로 위에서 $$\lvert\cot\pi z\rvert$$이 $$N$$에 무관한 상수 $$C$$로 유계임이 알려져 있다 (변마다 $$\sin\pi z$$의 절댓값이 아래로 유계이기 때문이다). $$N$$을 충분히 크게 잡으면 $$\Gamma_N$$ 안에 정수 $$-N, \dots, N$$과 $$f$$의 모든 극이 들어가므로, 유수정리 (정리 2) 에 의해

$$\frac{1}{2\pi i}\oint_{\Gamma_N} \pi\cot(\pi z)f(z)\,dz = \sum_{n = -N}^{N} f(n) + \sum_{j}\operatorname{Res}_{z = z_j}\Bigl[\pi\cot(\pi z)f(z)\Bigr]$$

이다. 왼쪽 적분을 어림한다. 차수 조건에서 큰 $$\lvert z\rvert$$에 대해 $$\lvert f(z)\rvert \leq A/\lvert z\rvert^2$$이고 $$\Gamma_N$$ 위에서 $$\lvert z\rvert \geq N + \tfrac12$$이므로, $$\Gamma_N$$의 둘레가 $$4(2N + 1)$$임과 함께 ML 부등식 ([§복소적분, ⁋명제 6](/ko/math/complex_analysis/complex_integration#prop6)) 으로

$$\left\lvert\oint_{\Gamma_N}\pi\cot(\pi z)f(z)\,dz\right\rvert \leq \pi C\cdot\frac{A}{(N + \frac12)^2}\cdot 4(2N + 1) \xrightarrow[N \to \infty]{} 0$$

이다. 따라서 $$N \to \infty$$에서 왼쪽이 $$0$$으로 가고, 오른쪽에서 $$\sum_{n=-N}^{N} f(n) \to \sum_{n=-\infty}^{\infty} f(n)$$ ($$f$$의 절대수렴성은 차수 조건에서 따름) 이므로

$$0 = \sum_{n=-\infty}^{\infty} f(n) + \sum_{j}\operatorname{Res}_{z = z_j}\Bigl[\pi\cot(\pi z)f(z)\Bigr]$$

이 되어 주장하는 등식을 얻는다.

</details>

명제 10은 무한급수의 합을 유한개의 유수 계산으로 환원한다. 급수의 항이 한 유리함수 $$f$$에서 $$f(n)$$으로 나오기만 하면, $$f$$의 극이라는 유한집합에서의 유수만 구하면 합이 닫힌 형태로 결정된다. 정사각형 경로를 쓰는 것은 그 위에서 $$\cot\pi z$$이 균등하게 유계여서 적분이 소멸하기 때문이며, 정수에 걸리지 않도록 변을 반정수 $$N + \tfrac12$$에 두는 것이 요령이다. 이 공식의 가장 유명한 응용이 Basel 문제이다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11 (Basel 문제)**</ins> $$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$$임을 보인다. $$f(z) = 1/z^2$$은 차수 조건을 만족하지만 극 $$z = 0$$이 정수라 명제 10을 곧장 쓸 수 없으므로, 원점을 따로 다룬다. 정사각형 경로 $$\Gamma_N$$ 안에서 $$g(z) = \pi\cot(\pi z)/z^2$$의 극은 정수 $$z = n$$ ($$n \neq 0$$) 들과 원점이며, 명제 10의 증명과 같은 어림으로 $$N \to \infty$$에서 $$\oint_{\Gamma_N} g\,dz \to 0$$이다. 따라서 모든 극에서의 유수 합이 $$0$$이다.

$$n \neq 0$$인 정수에서는 $$\pi\cot\pi z$$이 유수 $$1$$인 단순극이므로 $$\operatorname{Res}_{z = n} g = 1/n^2$$이다. 원점에서는 $$\pi\cot\pi z$$이 단순극, $$1/z^2$$이 이차극이라 $$g$$이 $$z = 0$$에서 삼차극을 가지며, 그 유수는 Laurent 전개로 구한다. $$\pi\cot\pi z$$의 원점 근방 전개는

$$\pi\cot\pi z = \frac{1}{z} - \frac{\pi^2}{3}z - \frac{\pi^4}{45}z^3 - \cdots$$

이므로 ($$\cot$$의 표준 전개), $$z^2$$으로 나누면

$$g(z) = \frac{\pi\cot\pi z}{z^2} = \frac{1}{z^3} - \frac{\pi^2}{3}\frac{1}{z} - \frac{\pi^4}{45}z - \cdots$$

이고, $$1/z$$의 계수가 $$\operatorname{Res}_{z = 0} g = -\pi^2/3$$이다. 모든 유수의 합이 $$0$$이라는 조건은

$$\sum_{n \neq 0}\frac{1}{n^2} + \Bigl(-\frac{\pi^2}{3}\Bigr) = 0$$

이 되고, $$\sum_{n \neq 0} 1/n^2 = 2\sum_{n=1}^{\infty} 1/n^2$$이므로 $$2\sum_{n=1}^{\infty} 1/n^2 = \pi^2/3$$, 곧

$$\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$$

을 얻는다.

</div>

---

**참고문헌**

**[Ahl]** L.V. Ahlfors, *Complex analysis*, 3rd ed., McGraw–Hill, 1979.

**[Con]** J.B. Conway, *Functions of one complex variable I*, 2nd ed., Graduate Texts in Mathematics 11, Springer, 1978.

**[SS]** E.M. Stein, R. Shakarchi, *Complex analysis*, Princeton Lectures in Analysis II, Princeton University Press, 2003.
