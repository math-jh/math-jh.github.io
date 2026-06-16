---
title: "적분"
description: "다양체 위의 미분 형식 적분을 정의하고, 오리엔테이션을 통해 부호가 결정되는 과정을 다룬다."
excerpt: "Manifold 위에서의 적분"

categories: [Math / Manifolds]
permalink: /ko/math/manifolds/integration
sidebar: 
    nav: "manifolds-ko"

date: 2023-02-17
weight: 20
published: false

---

이제 우리는 적분을 정의한다. 미적분학에서의 적분은 유클리드 공간의 영역 위에서 정의되었지만, 이를 manifold로 가져오려 하면 곧바로 문제가 생긴다. Manifold 위의 함수는 좌표를 통해서만 유클리드 공간의 함수로 볼 수 있는데, 좌표를 바꾸면 변수변환 공식에 의해 적분값이 Jacobian만큼 달라지기 때문이다. 이 문제는 함수 대신 미분형식을 적분의 대상으로 삼으면 해결되는데, $$m$$차원 manifold 위의 $$m$$-form은 좌표변환에 대해 정확히 Jacobian의 행렬식만큼 변하기 때문이다. 다만 변수변환 공식에는 행렬식의 절댓값이 등장하므로, 부호를 일관되게 통제하기 위해 [§향](/ko/math/manifolds/orientation)에서 살펴본 orientation이 필요하다.

## 유클리드 공간에서의 미분형식의 적분

우선 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Manifold $$M$$ 위에 정의된 differential form $$\omega$$에 대하여, $$\omega$$의 *support<sub>받침</sub>*는 다음의 집합

$$\supp\omega=\cl\left\{p\in M\mid \omega(p)\neq 0\right\}$$

으로 정의된다. 만일 $$\supp\omega$$가 compact라면 $$\omega$$가 *compactly supported*라 말한다.

</div>

열린집합 $$U\subseteq\mathbb{R}^m$$ 위의 임의의 $$m$$-form은 표준좌표 $$r^1,\ldots,r^m$$에 대하여 유일한 방식으로

$$\omega=f\,dr^1\wedge\cdots\wedge dr^m,\qquad f\in C^\infty(U)$$

로 쓸 수 있다. 이를 이용해 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 열린집합 $$U\subseteq\mathbb{R}^m$$ 위의 compactly supported $$m$$-form $$\omega=f\,dr^1\wedge\cdots\wedge dr^m$$에 대하여, $$\omega$$의 $$U$$ 위에서의 *적분<sub>integral</sub>*을 다음의 식

$$\int_U\omega=\int_Uf\,dr^1\cdots dr^m$$

으로 정의한다. 우변은 미적분학에서의 (Riemann) 적분이다.

</div>

$$f$$가 연속이고 compact support를 가지므로 우변의 적분은 잘 정의된다. 주의할 것은 이 정의가 좌표들의 *순서*에 의존한다는 것이다. 가령 $$m=2$$일 때 $$\omega=f\,dr^2\wedge dr^1$$로 쓰여진 형식의 적분은 $$dr^2\wedge dr^1=-dr^1\wedge dr^2$$이므로 $$-\int_Uf\,dr^1dr^2$$가 된다.

다음은 미적분학의 변수변환 공식이다. 이에 대한 증명은 미적분학의 영역이므로 여기서는 다루지 않는다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (변수변환)**</ins> 두 열린집합 $$U,V\subseteq\mathbb{R}^m$$ 사이의 diffeomorphism $$\varphi:V\rightarrow U$$와, compact support를 갖는 연속함수 $$f:U\rightarrow\mathbb{R}$$가 주어졌다 하자. 그럼 다음의 식

$$\int_Uf\,dr^1\cdots dr^m=\int_V(f\circ\varphi)\,\lvert\det D\varphi\rvert\,dr^1\cdots dr^m$$

이 성립한다. 여기서 $$D\varphi$$는 $$\varphi$$의 Jacobian matrix이다.

</div>

이를 미분형식의 언어로 다시 적으면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> 위와 같은 상황에서, $$\det D\varphi$$가 $$V$$ 전체에서 $$0$$보다 크다면, 임의의 compactly supported $$m$$-form $$\omega$$ on $$U$$에 대하여

$$\int_V\varphi^\ast\omega=\int_U\omega$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\omega=f\,dr^1\wedge\cdots\wedge dr^m$$이라 하자. [§미분형식](/ko/math/manifolds/differential_forms)에서 살펴본 pullback의 정의에 의하여 $$\varphi^\ast dr^i=d(r^i\circ\varphi)=\sum_{j=1}^m\frac{\partial\varphi^i}{\partial r^j}dr^j$$이고, $$\varphi^\ast$$가 wedge product를 보존하므로

$$\varphi^\ast\omega=(f\circ\varphi)\,\bigwedge_{i=1}^m\left(\sum_{j=1}^m\frac{\partial \varphi^i}{\partial r^j}dr^j\right)=(f\circ\varphi)\,\det(D\varphi)\,dr^1\wedge\cdots\wedge dr^m$$

이다. 마지막 등식은 행렬식의 정의에 따른 것이다. 한편 $$\varphi$$가 diffeomorphism이므로 $$\supp\varphi^\ast\omega=\varphi^{-1}(\supp\omega)$$는 compact이고, 따라서 [정의 2](#def2)와 [정리 3](#thm3)에 의하여

$$\int_V\varphi^\ast\omega=\int_V(f\circ\varphi)\det(D\varphi)\,dr^1\cdots dr^m=\int_V(f\circ\varphi)\,\lvert\det D\varphi\rvert\,dr^1\cdots dr^m=\int_U\omega$$

이다. 두 번째 등식에서 $$\det D\varphi>0$$ 가정을 사용하였다.

</details>

즉, 미분형식의 적분은 Jacobian의 행렬식이 항상 양수인 좌표변환에 대해서는 불변이다. [§향, ⁋명제 2](/ko/math/manifolds/orientation#prop2)의 둘째 조건이 정확히 이러한 좌표계들의 모임의 존재를 보장하므로, 우리는 orientable manifold 위에서 적분을 정의할 수 있다.

## 다양체 위에서의 적분

이제 $$M$$이 $$m$$차원의 connected orientable manifold라 하고, orientation, 즉 $$\bigwedge\nolimits^m(M)\setminus\{0\}$$의 component $$\Lambda^+$$ 하나를 고정하자. ([§향, ⁋정의 1](/ko/math/manifolds/orientation#def1)) Coordinate system $$(U,x)$$가 *positively oriented*라는 것은 $$U$$의 모든 점에서 $$dx^1\wedge\cdots\wedge dx^m$$이 $$\Lambda^+$$에 속하는 것이다. [§향, ⁋명제 2](/ko/math/manifolds/orientation#prop2)의 증명에서 살펴본 것과 같이 $$M$$은 positively oriented coordinate system들로 덮을 수 있으며, 이들이 겹치는 곳에서 Jacobian의 행렬식은 항상 $$0$$보다 크다.

우선 support가 하나의 좌표근방에 들어가는 경우를 처리한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Compactly supported $$m$$-form $$\omega$$ on $$M$$이 어떤 positively oriented coordinate system $$(U,x)$$에 대하여 $$\supp\omega\subseteq U$$를 만족한다 하자. 그럼 $$\omega$$의 적분을 다음의 식

$$\int_M\omega=\int_{x(U)}(x^{-1})^\ast\omega$$

으로 정의한다.

</div>

우변에서 $$(x^{-1})^\ast\omega$$는 열린집합 $$x(U)\subseteq\mathbb{R}^m$$ 위의 $$m$$-form이고, 그 support는 compact집합 $$x(\supp\omega)$$이므로 [정의 2](#def2)를 적용할 수 있다. 물론 이 정의가 말이 되려면 우변이 $$(U,x)$$의 선택에 의존하지 않아야 한다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> [정의 5](#def5)는 잘 정의된다. 즉 $$\supp\omega$$를 포함하는 positively oriented coordinate system $$(U,x)$$, $$(V,y)$$가 주어졌다면

$$\int_{x(U)}(x^{-1})^\ast\omega=\int_{y(V)}(y^{-1})^\ast\omega$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\supp\omega\subseteq U\cap V$$이므로, $$(x^{-1})^\ast\omega$$는 $$x(U\cap V)$$ 바깥에서 $$0$$이고 $$(y^{-1})^\ast\omega$$는 $$y(U\cap V)$$ 바깥에서 $$0$$이다. 따라서 두 적분은 각각 $$x(U\cap V)$$와 $$y(U\cap V)$$ 위에서의 적분과 같다. 이제 transition $$\varphi=x\circ y^{-1}:y(U\cap V)\rightarrow x(U\cap V)$$를 생각하면, 두 좌표계가 모두 positively oriented이므로 $$\det D\varphi>0$$이고,

$$\varphi^\ast\bigl((x^{-1})^\ast\omega\bigr)=(x^{-1}\circ\varphi)^\ast\omega=(y^{-1})^\ast\omega$$

이므로 [따름정리 4](#cor4)에 의하여 원하는 등식을 얻는다.

</details>

일반적인 경우는 [§미분다양체, §§Smooth partition of unity](/ko/math/manifolds/smooth_manifolds)의 결과를 이용해 위의 경우로 쪼개면 된다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Oriented manifold $$M$$ 위의 compactly supported $$m$$-form $$\omega$$가 주어졌다 하자. Positively oriented coordinate system들의 모임 $$(U_\alpha,x_\alpha)$$가 $$M$$을 덮는다 하고, $$(\phi_i)_{i\in I}$$가 이 open cover에 subordinate한 smooth partition of unity라 하자. 그럼 $$\omega$$의 $$M$$ 위에서의 적분을 다음의 식

$$\int_M\omega=\sum_{i\in I}\int_M\phi_i\,\omega$$

으로 정의한다.

</div>

이 정의가 말이 되는지부터 확인하자. 각각의 $$\phi_i\omega$$는 $$\supp(\phi_i\omega)\subseteq\supp\phi_i\subseteq U_{\alpha(i)}$$를 만족하는 compactly supported $$m$$-form이므로 각 항은 [정의 5](#def5)에 의해 정의된다. 또, $$(\supp\phi_i)$$가 locally finite이므로 compact집합 $$\supp\omega$$는 유한 개의 $$\supp\phi_i$$들과만 만나고, 따라서 위의 합에서 $$0$$이 아닌 항은 유한 개 뿐이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> [정의 7](#def7)은 잘 정의된다. 즉 위의 적분은 positively oriented coordinate system들의 모임과 partition of unity의 선택에 의존하지 않는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

또 다른 positively oriented coordinate system들의 모임 $$(V_\beta,y_\beta)$$와 그에 subordinate한 partition of unity $$(\psi_j)_{j\in J}$$가 주어졌다 하자. 우선 support가 하나의 positively oriented 좌표근방에 들어가는 form들에 대하여, [정의 5](#def5)의 적분은 [정의 2](#def2)의 적분의 선형성에 의해 선형이다. 이제 각각의 $$i$$에 대하여 $$\phi_i\omega$$는 $$U_{\alpha(i)}$$에 support를 갖고, $$\sum_{j\in J}\psi_j=1$$이며 $$\supp(\phi_i\omega)$$와 만나는 $$\supp\psi_j$$가 유한 개 뿐이므로

$$\int_M\phi_i\,\omega=\int_M\left(\sum_{j\in J}\psi_j\right)\phi_i\,\omega=\sum_{j\in J}\int_M\psi_j\phi_i\,\omega$$

이다. 여기서 각각의 $$\psi_j\phi_i\omega$$는 $$U_{\alpha(i)}$$와 $$V_{\beta(j)}$$ 모두에 support를 가지므로, [보조정리 6](#lem6)에 의해 $$\int_M\psi_j\phi_i\omega$$는 어느 쪽 좌표계로 계산해도 같은 값이다. 따라서

$$\sum_{i\in I}\int_M\phi_i\,\omega=\sum_{i\in I}\sum_{j\in J}\int_M\psi_j\phi_i\,\omega=\sum_{j\in J}\sum_{i\in I}\int_M\phi_i\psi_j\,\omega=\sum_{j\in J}\int_M\psi_j\,\omega$$

이고, 가운데 등식은 $$0$$이 아닌 항이 유한 개 뿐인 이중합의 순서교환이다. 즉 두 정의가 일치한다.

</details>

정의로부터 적분의 기본 성질들이 따라나온다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Oriented manifold $$M$$ 위의 compactly supported $$m$$-form들 $$\omega,\eta$$와 실수 $$a,b$$에 대하여 다음이 성립한다.

1. $$\int_M(a\omega+b\eta)=a\int_M\omega+b\int_M\eta$$.
2. Oriented manifold $$N$$과 orientation을 보존하는 diffeomorphism $$F:N\rightarrow M$$, 즉 positively oriented coordinate system들을 positively oriented coordinate system들로 옮기는 diffeomorphism에 대하여, $$\int_NF^\ast\omega=\int_M\omega$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫째 주장을 보이자. $$\omega,\eta$$에 대해 공통의 positively oriented coordinate system들의 모임과 partition of unity $$(\phi_i)$$를 택하면, 각 항에서의 선형성 ([정의 2](#def2)의 적분의 선형성)에 의하여

$$\int_M(a\omega+b\eta)=\sum_i\int_M\phi_i(a\omega+b\eta)=a\sum_i\int_M\phi_i\,\omega+b\sum_i\int_M\phi_i\,\eta=a\int_M\omega+b\int_M\eta$$

이다.

둘째 주장을 보이자. $$M$$의 positively oriented coordinate system들의 모임 $$(U_\alpha,x_\alpha)$$와 partition of unity $$(\phi_i)$$를 택하자. 그럼 $$(F^{-1}(U_\alpha),x_\alpha\circ F)$$들은 가정에 의해 $$N$$의 positively oriented coordinate system들이고, $$(\phi_i\circ F)$$는 이들에 subordinate한 partition of unity이다. 각각의 $$i$$에 대하여 $$\supp\bigl((\phi_i\circ F)F^\ast\omega\bigr)=F^{-1}(\supp\phi_i\omega)\subseteq F^{-1}(U_{\alpha(i)})$$이고, $$(\phi_i\circ F)F^\ast\omega=F^\ast(\phi_i\omega)$$이므로 [정의 5](#def5)를 계산하면

$$\int_NF^\ast(\phi_i\,\omega)=\int_{x_{\alpha(i)}(U_{\alpha(i)})}\bigl((x_{\alpha(i)}\circ F)^{-1}\bigr)^\ast F^\ast(\phi_i\,\omega)=\int_{x_{\alpha(i)}(U_{\alpha(i)})}(x_{\alpha(i)}^{-1})^\ast(\phi_i\,\omega)=\int_M\phi_i\,\omega$$

이다. 이를 $$i$$에 대해 더하면 원하는 결과를 얻는다.

</details>

<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> $$M$$이 connected orientable일 때 orientation의 선택지는 $$\Lambda^+$$와 $$\Lambda^-$$ 두 가지이다. 반대쪽 component를 택하면 positively oriented coordinate system의 역할이 뒤바뀌고, [정의 5](#def5)의 각 항의 부호가 바뀌므로 적분 전체의 부호가 바뀐다. 즉 $$\int_{-M}\omega=-\int_M\omega$$이다. 여기서 $$-M$$은 반대 orientation이 주어진 $$M$$을 뜻한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $$M$$이 표준 orientation이 주어진 열린집합 $$U\subseteq\mathbb{R}^m$$이라 하자. 즉 identity chart $$(U,\id_U)$$가 positively oriented이도록 orientation을 잡은 것이다. 그럼 compactly supported $$m$$-form $$\omega=f\,dr^1\wedge\cdots\wedge dr^m$$에 대하여, 하나의 chart $$(U,\id_U)$$와 상수함수 $$1$$로 이루어진 partition of unity를 택하면 [정의 7](#def7)의 적분은 정확히 [정의 2](#def2)의 적분, 즉 미적분학에서의 적분 $$\int_Uf\,dr^1\cdots dr^m$$과 일치한다.

</div>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
