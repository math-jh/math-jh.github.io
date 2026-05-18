---
title: "Morse 이론과 stationary phase 근사"
excerpt: "Morse function의 critical point와 oscillating integral의 점근전개"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/morse_stationary_phase
header:
    overlay_image: /assets/images/Math/Symplectic_Geometry/morse_stationary_phase.png
    overlay_filter: 0.5
sidebar:
    nav: "symplectic_geometry-ko"

date: 2023-05-15
last_modified_at: 2023-05-15
weight: 4
published: false

---

해석학과 기하학의 여러 응용에서 다음 형태의 진동적분

$$\mathcal{I}(z) = \int_\gamma e^{W(x)/z}\,\omega$$

의 $$z\to 0$$ 점근행동이 자주 등장하며, 그 점근치가 phase function $$W$$의 임계점에서의 국소 데이터로 환원된다는 사실은 양자역학의 semiclassical limit, partial differential equation의 WKB 해석, singularity theory, 그리고 후술할 mirror symmetry의 B-model superpotential 분석 등 다양한 맥락에서 핵심적이다. 이러한 환원은 두 개의 기초 위에 서 있다. 첫째는 임계점 근방에서 phase를 표준형으로 환원하는 *Morse lemma*이며, 둘째는 Gaussian integral의 다변수 일반화로 얻어지는 *stationary phase formula*이다. 또한 적분 경로의 선택을 통제하는 *Lefschetz thimble*의 구성도 본질적으로 Morse 이론의 gradient flow에 의해 주어진다. 본 글에서는 이 세 도구를 차례로 정리한다. 본 글의 결과는 이후 mirror symmetry에서 oscillating integral, $$J$$-function의 점근분석, Gauss-Manin connection 등을 다룰 때 직접 사용된다.

## Morse function과 임계점

우선 critical point와 그 non-degeneracy 개념을 정확히 하자.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth manifold $$M$$([\[미분다양체\] §미분다양체, ⁋정의 1](/ko/math/manifold/smooth_manifolds#def1))과 smooth function $$f:M\to\mathbb{R}$$이 주어졌다 하자. 점 $$p\in M$$이 $$f$$의 *critical point<sub>임계점</sub>*라는 것은 differential $$df_p:T_pM\to\mathbb{R}$$([\[미분다양체\] §미분사상, ⁋정의 7](/ko/math/manifold/differentials#def7))이 영사상인 것을 뜻한다. 여기서 $$T_pM$$은 $$p$$에서의 tangent space ([\[미분다양체\] §접공간, ⁋정의 3](/ko/math/manifold/tangent_space#def3))이다.

</div>

좌표 $$(x_1,\ldots,x_n)$$을 점 $$p$$ 근방에 잡으면 위 조건은 $$\partial f/\partial x_i(p)=0$$이 모든 $$i$$에 대해 성립한다는 것과 동치이다. 임계점에서는 일차 정보가 사라지므로, 함수의 국소적 형상은 이차 정보, 즉 Hessian이 결정한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$f:M\to\mathbb{R}$$의 임계점 $$p$$에서의 *Hessian<sub>헤시안</sub>* $$\operatorname{Hess}_p(f)$$는 다음의 식

$$\operatorname{Hess}_p(f)(X,Y) = X_p(\tilde Y f)$$

으로 정의되는 대칭 bilinear form $$T_pM\times T_pM\to\mathbb{R}$$이다. 여기서 $$\tilde Y$$는 $$Y$$의 임의의 smooth extension이고, $$p$$가 critical point라는 사실에 의해 위 표현은 extension의 선택과 무관하다.

</div>

좌표 $$(x_1,\ldots,x_n)$$에서는

$$\operatorname{Hess}_p(f) = \left[\frac{\partial^2 f}{\partial x_i\partial x_j}(p)\right]_{i,j}$$

으로 주어지는 대칭행렬이다. Critical point가 $$df_p=0$$이라는 1차 조건만으로 결정되는 데에 반해, Hessian은 그 critical point가 어떤 종류인가, 즉 극소·극대·안장점인가를 구분하는 이차 정보를 담는다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Critical point $$p$$가 *non-degenerate<sub>비퇴화</sub>*라는 것은 $$\operatorname{Hess}_p(f)$$가 비퇴화 대칭 bilinear form인 것, 즉 좌표를 잡았을 때 이 Hessian 행렬이 가역인 것을 뜻한다. 모든 critical point가 non-degenerate인 smooth function $$f:M\to\mathbb{R}$$을 *Morse function<sub>모스 함수</sub>*이라 부른다.

</div>

Non-degenerate critical point $$p$$에서 $$\operatorname{Hess}_p(f)$$의 signature는 좌표 변환에 대한 불변량이다. 양의 eigenvalue의 개수와 음의 eigenvalue의 개수가 좌표 선택에 의존하지 않으므로 다음 정의가 의미를 가진다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Non-degenerate critical point $$p$$의 *Morse index<sub>모스 지수</sub>* $$\lambda_p$$는 $$\operatorname{Hess}_p(f)$$의 음의 eigenvalue의 개수이다. 또 $$\operatorname{Hess}_p(f)$$의 *signature* $$\sigma_p$$는 양의 eigenvalue의 개수에서 음의 eigenvalue의 개수를 뺀 값이다. 즉 $$n=\dim M$$일 때

$$\sigma_p = n - 2\lambda_p$$

이다.

</div>

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> 문헌에 따라 signature를 $$|\det\operatorname{Hess}_p(f)|$$의 부호와 혼동하는 경우가 있으나, 우리는 signature를 위와 같이 *eigenvalue 부호의 부호화*로 정의한다. Stationary phase formula의 위상 인자 $$e^{i\pi\sigma_p/4}$$에서 사용되는 것은 이 정의이다.

</div>

## Morse lemma

Non-degenerate critical point는 Hessian의 signature 외에는 어떠한 추가적인 좌표 불변량을 갖지 않는다. 다음 정리가 이 사실을 엄밀히 진술한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Morse lemma)**</ins> $$f:M\to\mathbb{R}$$의 non-degenerate critical point $$p$$에 대하여, 적당한 좌표 차트 $$(U,\varphi=(y_1,\ldots,y_n))$$이 존재하여 $$\varphi(p)=0$$이고

$$f\circ\varphi^{-1}(y) = f(p) - y_1^2 - \cdots - y_{\lambda_p}^2 + y_{\lambda_p+1}^2 + \cdots + y_n^2$$

가 $$\varphi(U)$$ 위에서 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

논의를 $$M=\mathbb{R}^n$$의 원점 근방으로 옮겨도 무방하다. $$f(0)=0$$, $$df_0=0$$이라 가정하자. 우선 다음의 보조 항등식이 필요하다. 임의의 smooth function $$g:U\to\mathbb{R}$$이 $$g(0)=0$$을 만족하면

$$g(x) = \int_0^1 \frac{d}{dt}g(tx)\,dt = \sum_{i=1}^n x_i\int_0^1 \frac{\partial g}{\partial x_i}(tx)\,dt = \sum_{i=1}^n x_i\,g_i(x)$$

로 쓸 수 있다. 여기서 $$g_i(x)=\int_0^1 (\partial g/\partial x_i)(tx)\,dt$$는 smooth이고 $$g_i(0)=(\partial g/\partial x_i)(0)$$이다.

이 보조항등식을 $$f$$ 자신에 한 번 적용하면 $$f(x)=\sum_i x_i f_i(x)$$를 얻으며, $$df_0=0$$이므로 $$f_i(0)=0$$이다. 따라서 각 $$f_i$$에 다시 같은 항등식을 적용하면

$$f_i(x) = \sum_{j=1}^n x_j h_{ij}(x)$$

이 되고, 이를 합치면

$$f(x) = \sum_{i,j} x_i x_j h_{ij}(x)$$

이다. $$h_{ij}$$를 $$\tfrac12(h_{ij}+h_{ji})$$로 대체해도 합은 변하지 않으므로 $$h_{ij}$$가 대칭이라 가정해도 좋다. 한편 양변을 두 번 미분하여 원점에서 평가하면 $$h_{ij}(0)=\tfrac12 (\partial^2 f/\partial x_i\partial x_j)(0)$$이므로, $$H(x)=[h_{ij}(x)]$$는 원점에서 비퇴화이고 대칭인 행렬 값 smooth function이다.

이제 비퇴화 대칭행렬은 *국소적으로* 표준형으로 정렬할 수 있다는 사실을 사용한다. 구체적으로, 원점 근방의 대칭행렬 $$H(x)$$에 대하여 smooth하게 정해지는 가역행렬 $$Q(x)$$가 존재하여

$$Q(x)^\top H(x) Q(x) = \operatorname{diag}(-1,\ldots,-1,+1,\ldots,+1)$$

으로 만들 수 있다. 이는 다음과 같이 귀납적으로 구성한다. $$H(0)$$이 비퇴화이므로 어떤 $$h_{ii}(0)\neq 0$$이 존재하며, 좌표 재배열을 통해 $$h_{11}(0)\neq 0$$이라 가정한다. 새 변수

$$y_1(x) = \sqrt{\lvert h_{11}(x)\rvert}\left(x_1 + \sum_{j\ge 2}\frac{h_{1j}(x)}{h_{11}(x)}x_j\right)$$

를 도입하면 $$y_1$$은 원점 근방에서 smooth이고 (제곱근 안의 양은 $$h_{11}(0)$$의 부호와 같은 부호로 원점 근방에서 영이 되지 않는다), 직접 계산에 의해

$$f(x) = \pm y_1(x)^2 + \sum_{i,j\ge 2} x_i x_j h_{ij}'(x)$$

가 성립한다. 여기서 부호 $$\pm$$은 $$h_{11}(0)$$의 부호와 일치하며, $$h_{ij}'$$는 새로운 대칭 행렬 값 함수로서 원점에서 여전히 비퇴화이다. 변수 $$(y_1,x_2,\ldots,x_n)$$이 원점 근방에서 좌표를 이룬다는 것은 Jacobian 계산으로 확인된다. 이제 $$(x_2,\ldots,x_n)$$에 대한 귀납을 적용하여 모든 변수를 순차적으로 표준화하면

$$f = \sum_{i=1}^n \epsilon_i y_i^2,\qquad \epsilon_i\in\{-1,+1\}$$

을 얻는다. 끝으로 좌표를 재배열하여 음수 부호를 앞쪽 $$\lambda_p$$개에 모으면 원하는 표준형이 성립한다. 음수 부호의 개수가 Hessian의 음의 eigenvalue 개수와 같다는 것은 이 표준형이 자체로 Hessian을 $$\operatorname{diag}(-2,\ldots,-2,+2,\ldots,+2)$$로 만들어 준다는 사실로부터 확인된다.

</details>

증명에서 두드러지는 핵심은 *Hadamard lemma* 형식의 항등식 $$g(x)=\sum_i x_i g_i(x)$$를 두 번 적용하여 $$f$$를 좌표의 이차형식의 *변형*으로 표현하는 것, 그리고 비퇴화 대칭행렬의 대각화를 smooth하게 수행하는 것이다. 즉, Morse lemma는 Hessian이라는 *대수적 데이터*가 함수의 *기하학적 표준형*을 완전히 결정함을 의미한다.

다음 따름정리도 즉시 얻어진다.

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> $$f$$의 non-degenerate critical point는 고립되어 있다. 특히 compact manifold $$M$$ 위의 Morse function은 유한 개의 critical point를 갖는다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

[정리 6](#thm6)의 표준형 $$f(y)=f(p)-y_1^2-\cdots-y_{\lambda_p}^2+y_{\lambda_p+1}^2+\cdots+y_n^2$$에서 $$df(y)=(-2y_1,\ldots,-2y_{\lambda_p},2y_{\lambda_p+1},\ldots,2y_n)$$이므로, $$y=0$$ 외에는 critical point가 존재하지 않는다. 즉 $$p$$의 적당한 근방에는 $$p$$ 외의 critical point가 없으므로 $$p$$는 고립된 critical point이다. $$M$$이 compact이면 임계점 집합이 closed이며 고립점들로 구성되므로 유한집합이다.

</details>

두 가지 표준적인 예시를 살펴본다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 평면 $$\mathbb{R}^2$$ 위의 함수 $$f(x,y)=x^2-y^2$$을 생각하자. $$df=(2x,-2y)$$이므로 유일한 critical point는 원점이며, 그 Hessian은 $$\operatorname{diag}(2,-2)$$이므로 비퇴화이고 Morse index는 $$1$$, signature는 $$0$$이다. 즉 원점은 *안장점<sub>saddle point</sub>*이며, 이미 $$f$$ 자체가 [정리 6](#thm6)의 표준형으로 주어진 형태이다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$\mathbb{R}^3$$에 표준적으로 들어가 있는 토러스 $$T^2$$ 위의 *height function* $$h:T^2\to\mathbb{R}$$, $$h(x,y,z)=z$$를 생각하자. 토러스를 도넛 모양으로 세워두면 $$h$$는 정확히 네 개의 critical point를 가진다: 최고점($$\lambda=2$$), 안쪽 위 안장점($$\lambda=1$$), 안쪽 아래 안장점($$\lambda=1$$), 최저점($$\lambda=0$$). Hessian 계산으로 이들이 모두 비퇴화임을 확인할 수 있으므로 $$h$$는 Morse function이며, Morse 부등식

$$\sum_p (-1)^{\lambda_p} = \chi(T^2) = 0$$

이 $$1 - 2 + 1 = 0$$으로 성립함을 즉시 확인할 수 있다.

</div>

[예시 9](#ex9)는 Morse 이론이 단순한 국소 표준화를 넘어 manifold의 *전역적인* 위상 정보 (Euler characteristic, Betti number 등)를 critical point 데이터로부터 복원하는 도구임을 시사하지만, 본 글의 목적상 우리는 국소적 측면만 사용한다. 전역 Morse 이론의 본격적인 전개는 **[Mil]** 또는 **[AD]**를 참조한다.

## Stationary phase 근사

Morse lemma의 첫 번째 응용은 진동적분의 점근전개이다. Smooth amplitude $$a\in C_c^\infty(M)$$과 smooth phase $$\phi:M\to\mathbb{R}$$이 주어졌을 때, 우리는 다음의 *oscillating integral<sub>진동적분</sub>*

$$I(\hbar) = \int_M e^{i\phi(x)/\hbar}\,a(x)\,dx$$

의 $$\hbar\to 0^+$$ 점근 행동을 구하고자 한다. 여기서 $$dx$$는 manifold 위의 고정된 (예컨대 Riemannian) volume form이며, support condition은 $$a$$의 compact support로 보장된다. 직관적으로 $$\hbar\to 0$$인 극한에서 phase $$\phi/\hbar$$가 빠르게 진동하므로 적분의 기여는 phase의 미분이 $$0$$이 되는 점, 즉 $$\phi$$의 critical point 근방에서만 살아남는다. 이를 정량화하는 것이 다음 정리이다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (stationary phase formula)**</ins> $$\phi:M\to\mathbb{R}$$이 $$\operatorname{supp}(a)$$ 위에서 유한 개의 non-degenerate critical point만을 가진다고 하자. $$n=\dim M$$이라 할 때, $$\hbar\to 0^+$$에서 다음의 점근전개가 성립한다.

$$I(\hbar) = (2\pi\hbar)^{n/2}\sum_{p\in\operatorname{Crit}(\phi)\cap\operatorname{supp}(a)} \frac{e^{i\phi(p)/\hbar}\,e^{i\pi\sigma_p/4}}{\sqrt{\lvert\det\operatorname{Hess}_p(\phi)\rvert}}\,a(p) + O(\hbar^{n/2+1})$$

여기서 $$\sigma_p$$는 [정의 4](#def4)의 Hessian signature이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

증명은 다음 세 단계로 나누어진다.

**1단계 (localization).** 우선 critical point 바깥에서는 적분이 임의의 다항 차수보다 빠르게 감소함을 본다. $$x_0\in\operatorname{supp}(a)$$가 critical point가 아니라 하자. 그럼 $$d\phi(x_0)\neq 0$$이므로 $$x_0$$ 근방에서 vector field $$X$$를 $$X\phi=1$$이 되도록 잡을 수 있다. 그럼

$$X\bigl(e^{i\phi/\hbar}\bigr) = \frac{i}{\hbar}(X\phi)e^{i\phi/\hbar} = \frac{i}{\hbar}e^{i\phi/\hbar}$$

이므로 $$e^{i\phi/\hbar} = (\hbar/i)\,X(e^{i\phi/\hbar})$$로 쓸 수 있다. 이를 적분에 대입하고 divergence theorem (즉 $$X$$의 transpose에 대한 부분적분)을 $$N$$번 적용하면 $$I(\hbar)$$ 중 critical point의 밖에 해당하는 기여가 $$O(\hbar^N)$$임을 알 수 있다. 따라서 smooth partition of unity ([\[미분다양체\] §미분다양체](/ko/math/manifold/smooth_manifolds))를 이용하여 $$a$$의 support를 critical point들의 작은 근방으로 잘라내도 점근전개의 오차는 임의의 차수로 통제된다. 이제 $$\operatorname{supp}(a)$$가 단 하나의 critical point $$p$$의 작은 근방에 들어 있는 경우만 다루면 충분하다.

**2단계 (Morse lemma에 의한 표준화).** [정리 6](#thm6)을 $$\phi$$에 적용하면 $$p$$ 근방에서 좌표 $$y=(y_1,\ldots,y_n)$$이 존재하여

$$\phi(y) = \phi(p) - y_1^2 - \cdots - y_{\lambda_p}^2 + y_{\lambda_p+1}^2 + \cdots + y_n^2 = \phi(p) + \tfrac12 Q(y)$$

이라 할 수 있다. 여기서 $$Q(y)=\sum_i 2\epsilon_i y_i^2$$이며 $$\epsilon_i\in\{-1,+1\}$$이다. 좌표변환의 Jacobian을 $$J(y)$$라 하고 $$\tilde a(y)=a(y)J(y)$$로 두면

$$I(\hbar) = e^{i\phi(p)/\hbar}\int_{\mathbb{R}^n} e^{iQ(y)/(2\hbar)}\,\tilde a(y)\,dy$$

로 환원된다 (확장은 0으로). 이제 문제는 *Gaussian 형태의 진동적분*

$$J(\hbar) = \int_{\mathbb{R}^n} e^{i\sum_i \epsilon_i y_i^2/\hbar}\,\tilde a(y)\,dy$$

의 $$\hbar\to 0$$ 점근을 계산하는 것이다.

**3단계 (Gaussian integral).** $$\tilde a(y) = \tilde a(0) + \sum_i y_i \tilde a_i(y)$$로 Taylor 전개하면, $$y_i$$항들은 부분적분 후 $$O(\hbar)$$의 보정만을 주므로 leading order는

$$J(\hbar) \sim \tilde a(0)\prod_{i=1}^n \int_{-\infty}^\infty e^{i\epsilon_i y_i^2/\hbar}\,dy_i$$

으로 인수분해된다. 1차원 Fresnel 적분의 표준 결과

$$\int_{-\infty}^\infty e^{i\epsilon y^2/\hbar}\,dy = \sqrt{\pi\hbar}\,e^{i\epsilon\pi/4} = (\pi\hbar)^{1/2}\,e^{i\operatorname{sgn}(\epsilon)\pi/4}$$

를 모든 $$i$$에 대해 곱하면

$$\prod_{i=1}^n \int_{-\infty}^\infty e^{i\epsilon_i y_i^2/\hbar}\,dy_i = (\pi\hbar)^{n/2}\,e^{i\pi\sum_i\operatorname{sgn}(\epsilon_i)/4} = (\pi\hbar)^{n/2}\,e^{i\pi\sigma_p/4}$$

이 된다. 여기서 마지막 등호는 $$\sum_i\operatorname{sgn}(\epsilon_i)$$이 정확히 $$Q$$, 즉 $$\operatorname{Hess}_p(\phi)$$의 signature $$\sigma_p$$라는 사실을 사용한다.

한편 좌표변환 $$y=y(x)$$의 Jacobian은 $$J(0)^2 \cdot \det[\operatorname{diag}(2\epsilon_i)] = \det\operatorname{Hess}_p(\phi)$$를 만족하므로 (Morse lemma의 좌표가 Hessian을 $$\operatorname{diag}(2\epsilon_i)$$로 만들기 때문이다) $$\tilde a(0) = a(p)\lvert\det\operatorname{Hess}_p(\phi)\rvert^{-1/2}\cdot 2^{n/2}$$가 성립한다. 이를 위 식과 결합하고 $$(\pi\hbar)^{n/2}\cdot 2^{n/2}=(2\pi\hbar)^{n/2}$$임을 사용하면

$$I(\hbar) = (2\pi\hbar)^{n/2}\,\frac{e^{i\phi(p)/\hbar}\,e^{i\pi\sigma_p/4}}{\sqrt{\lvert\det\operatorname{Hess}_p(\phi)\rvert}}\,a(p) + O(\hbar^{n/2+1})$$

을 얻는다. 1단계의 partition of unity에 의해 여러 critical point가 있는 일반적인 경우 위 leading term이 각 점에서 합산되어 원하는 공식이 성립한다.

</details>

[정리 10](#thm10)의 본질은 다음과 같이 요약된다. 진동적분의 $$\hbar\to 0$$ 점근은 *critical point의 국소 데이터*인 (1) critical value $$\phi(p)$$, (2) Hessian의 determinant 절댓값, (3) Hessian의 signature, 그리고 (4) amplitude의 critical point에서의 값으로 완전히 결정된다. Signature가 위상 인자 $$e^{i\pi\sigma_p/4}$$로 나타나는 것은 Fresnel 적분의 부호별 위상회전이 누적된 결과이며, 이는 *Maslov index*가 등장하는 가장 단순한 정황이기도 하다.

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> 위 정리는 leading order만을 진술하였으나, 동일한 방법은 모든 차수의 점근전개를 제공한다. 즉

$$I(\hbar) \sim (2\pi\hbar)^{n/2}\sum_p e^{i\phi(p)/\hbar}\,e^{i\pi\sigma_p/4}\,\lvert\det\operatorname{Hess}_p(\phi)\rvert^{-1/2}\sum_{k\ge 0}\hbar^k\,c_k(p)$$

의 형태로 적힌다. 여기서 $$c_0(p)=a(p)$$이며 $$c_k(p)$$는 $$a$$와 $$\phi$$의 $$p$$에서의 $$2k$$차 derivative들의 다항조합으로 구체적으로 계산된다. Hörmander **[Hör]** Theorem 7.7.5 또는 그 미세화된 형태들이 이 전개의 표준 참고문헌이다.

</div>

간단한 예시 두 개를 본다.

<div class="example" markdown="1">

<ins id="ex12">**예시 12**</ins> $$M=\mathbb{R}$$ 위에서 $$\phi(x)=x^2/2$$, $$a\in C_c^\infty(\mathbb{R})$$이라 하자. 유일한 critical point는 $$0$$이며 $$\phi(0)=0$$, $$\operatorname{Hess}_0(\phi)=1$$, $$\sigma_0=+1$$이다. [정리 10](#thm10)에 의해

$$\int_{\mathbb{R}} e^{ix^2/(2\hbar)}\,a(x)\,dx = \sqrt{2\pi\hbar}\,e^{i\pi/4}\,a(0) + O(\hbar^{3/2})$$

가 성립하며, 이는 1차원 Fresnel 적분의 표준 공식과 정확히 일치한다.

</div>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> $$M=\mathbb{R}^2$$ 위의 $$\phi(x,y)=xy$$를 생각하자. $$d\phi=(y,x)$$이므로 유일한 critical point는 원점이고, Hessian은

$$\operatorname{Hess}_0(\phi) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

이며 eigenvalue가 $$\pm 1$$이므로 비퇴화이고 $$\sigma_0=0$$, $$\lvert\det\operatorname{Hess}_0(\phi)\rvert=1$$이다. 따라서 [정리 10](#thm10)에 의해

$$\int_{\mathbb{R}^2} e^{ixy/\hbar}\,a(x,y)\,dx\,dy = 2\pi\hbar\,a(0,0) + O(\hbar^2)$$

가 성립한다. 이 식은 Fourier 변환과 inverse Fourier 변환을 연결하는 *Fourier inversion* 정형과 동등하며, $$a$$의 Fourier 변환을 적당히 재배열하면 직접 검증할 수 있다.

</div>

[예시 13](#ex13)에서 보듯이 signature가 $$0$$인 경우 위상 인자가 자명하므로 stationary phase formula는 Fourier 해석에서 친숙한 형태로 환원된다. 일반적으로 signature가 0이 아닐 때 등장하는 위상 인자가 Morse 이론에서 *index*가 가지는 의미와 결합하여 Maslov class, half-density bundle 등 보다 정교한 구조로 발전한다.

## Lefschetz thimble

지금까지 우리는 phase function이 *실가*라고 가정하였다. 그러나 응용에서 마주치는 phase는 holomorphic function인 경우가 많고 (가령 singularity theory의 versal family, mirror symmetry의 superpotential 등), 이 경우 적분 contour 자체를 신중하게 선택해야 한다. 이 선택을 Morse 이론으로부터 자연스럽게 얻어내는 구성이 *Lefschetz thimble*이다.

$$X$$가 complex manifold이고 $$W:X\to\mathbb{C}$$가 holomorphic function이라 하자. 형식적으로 우리는 진동적분

$$\int_\Gamma e^{W(x)/\hbar}\,\omega$$

를 정의하고 싶지만, $$\operatorname{Re}(W)$$가 $$X$$ 위에서 위로 유계가 아니므로 임의의 cycle $$\Gamma$$에 대해 적분이 수렴할 보장이 없다. 이를 해결하기 위해 적분 경로를 $$\operatorname{Re}(W/\hbar)\to-\infty$$인 영역으로 빨려들어가는 경로로 잡아야 한다. 이를 위해 다음 함수에 주목한다. $$h:X\to\mathbb{R}$$을

$$h(x) = -\operatorname{Re}(W(x)/\hbar)$$

라 하면, $$h$$는 smooth real-valued function이며, $$W$$의 holomorphic critical point $$p$$ (즉 $$dW(p)=0$$) 가 정확히 $$h$$의 critical point에 대응한다. 또한 $$W$$가 $$p$$에서 non-degenerate, 즉 complex Hessian이 가역이라는 조건은 $$h$$가 $$p$$에서 비퇴화 critical point를 가짐과 동치이다. 단 그 *Morse index*는 항상 절반 차원이다 (complex Hessian의 eigenvalue가 $$\lambda_1,\ldots,\lambda_n\in\mathbb{C}^\ast$$일 때 $$-\operatorname{Re}(\lambda_i/\hbar)$$의 부호 분포가 정확히 절반씩이라는 사실로부터 얻어진다).

$$X$$ 위에 적당한 Kähler metric을 고정하고 (실 부분이 Riemannian metric을 이루므로 [\[리만기하학\] §리만 계량](/ko/math/riemannian_geometry/Riemannian_metric)의 일반론에 따라 gradient vector field가 정의된다) $$h$$의 gradient flow를 생각하자.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> $$W$$의 비퇴화 critical point $$p$$에 대하여, $$h=-\operatorname{Re}(W/\hbar)$$의 *Lefschetz thimble<sub>레프셰츠 팀블</sub>* $$\Gamma_p$$는 $$h$$의 negative gradient flow

$$\frac{dx}{dt} = -\nabla h(x)$$

의 $$p$$에서의 unstable manifold, 즉 $$t\to-\infty$$일 때 $$p$$로 수렴하는 점들의 집합이다.

</div>

위에서 언급한 *Morse index가 절반*이라는 사실로부터, $$\Gamma_p$$는 $$X$$의 실차원의 절반에 해당하는 real submanifold이며, 정확히 적분의 수렴 조건 $$\operatorname{Re}(W/\hbar)\to -\infty$$를 따라가는 경로의 다발이 된다. 정의에 의해 $$h$$는 $$\Gamma_p$$ 위에서 $$p$$에서 최소를 가지므로 $$\operatorname{Re}(W/\hbar)$$는 $$p$$에서 최대를 가지며, $$\Gamma_p$$를 따라 무한대로 가면 $$\operatorname{Re}(W/\hbar)\to-\infty$$이다. 따라서 적분

$$\mathcal{I}_p(\hbar) = \int_{\Gamma_p} e^{W(x)/\hbar}\,\omega$$

가 absolutely convergent이다.

이렇게 정의된 thimble들 $$\{\Gamma_p\}_{p\in\operatorname{Crit}(W)}$$는 rapid decay relative cohomology의 기저를 이루며, 임의의 적분 contour의 deformation을 thimble들의 정수계수 선형결합으로 분해할 수 있다. 이는 *Picard–Lefschetz 공식*의 출발점이며, 자세한 내용은 **[AGV]**의 II장 또는 **[Pha]**를 참조한다.

각 thimble $$\Gamma_p$$ 위에서 $$\hbar\to 0$$ 점근을 계산하면 [정리 10](#thm10)을 holomorphic 세팅으로 확장한 다음의 진술을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> $$W$$가 비퇴화 critical point $$p$$를 가질 때, $$\hbar\to 0^+$$에서

$$\int_{\Gamma_p} e^{W(x)/\hbar}\,\omega = (2\pi\hbar)^{n/2}\,\frac{e^{W(p)/\hbar}}{\sqrt{\det\operatorname{Hess}_p(W)}}\bigl(\alpha(p) + O(\hbar)\bigr)$$

가 성립한다. 여기서 $$n=\dim_{\mathbb{C}}X$$이고, $$\alpha(p)$$는 holomorphic volume form $$\omega$$의 $$p$$에서의 값에 해당하는 계수이며, square root의 branch는 $$\Gamma_p$$의 orientation에 의해 결정된다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$p$$ 근방에서 holomorphic Morse lemma (즉 [정리 6](#thm6)의 복소 버전)에 의해 holomorphic 좌표 $$z=(z_1,\ldots,z_n)$$이 존재하여

$$W(z) = W(p) + \tfrac12\sum_{i=1}^n z_i^2$$

이라 할 수 있다. 그럼 $$\Gamma_p$$는 이 좌표에서 $$z_i = e^{i\theta_i}t_i$$ ($$t_i\in\mathbb{R}$$)의 꼴로 적당한 위상 $$\theta_i$$들을 따라 잡은 실 $$n$$차원 submanifold가 되며, 위상 $$\theta_i$$는 정확히 적분이 수렴하도록 결정된다. 이 좌표에서 적분은 Gaussian integral

$$e^{W(p)/\hbar}\,\alpha(p)\,\prod_{i=1}^n \int_{\mathbb{R}} e^{e^{2i\theta_i}t_i^2/(2\hbar)}\,dt_i$$

으로 환원되며, 각 1차원 적분은 [정리 10](#thm10)의 증명 3단계와 동일한 방식으로 $$\sqrt{2\pi\hbar/(-e^{2i\theta_i})}=\sqrt{2\pi\hbar}/\sqrt{-e^{2i\theta_i}}$$를 준다. 이를 모두 곱하면 $$(2\pi\hbar)^{n/2}/\sqrt{\det\operatorname{Hess}_p(W)}$$가 나오며, square root의 branch는 thimble의 orientation $$\{e^{i\theta_i}\}$$에 의해 결정된다. 자세한 부호 추적은 **[Pha]** §5를 참조한다.

</details>

[명제 15](#prop15)는 위의 stationary phase formula ([정리 10](#thm10))를 holomorphic 세팅으로 확장한 것이며, mirror symmetry의 superpotential $$W_q$$에 대한 oscillating integral의 thimble별 점근 분해에 직접 사용된다. 그 맥락에서는 critical point가 양자 매개변수 $$q$$에 따라 이동하며, thimble들의 monodromy가 Picard–Lefschetz 변환을 통해 적분의 분해를 통제한다.

---

**참고문헌**

**[Mil]** J. Milnor, *Morse theory*, Annals of Mathematics Studies **51**, Princeton University Press, 1963.  
**[AD]** M. Audin and M. Damian, *Morse theory and Floer homology*, Universitext, Springer, 2014.  
**[Hör]** L. Hörmander, *The analysis of linear partial differential operators I*, Grundlehren der Mathematischen Wissenschaften **256**, Springer, 1983.  
**[AGV]** V. I. Arnold, S. M. Gusein-Zade, and A. N. Varchenko, *Singularities of differentiable maps, Volume II*, Monographs in Mathematics **83**, Birkhäuser, 1988.  
**[Pha]** F. Pham, *Vanishing homologies and the $$n$$ variable saddlepoint method*, Proc. Sympos. Pure Math. **40** (1983), 319--333.  
