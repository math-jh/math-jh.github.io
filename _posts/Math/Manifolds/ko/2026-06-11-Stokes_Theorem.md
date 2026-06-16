---
title: "스토크스 정리"
description: "경계가 있는 oriented 다양체 위에서 미분형식의 외미분의 적분이 경계에서의 적분과 일치한다는 스토크스 정리를 증명한다."
excerpt: "미적분학의 기본정리의 일반화인 Stokes 정리"

categories: [Math / Manifolds]
permalink: /ko/math/manifolds/stokes_theorem
sidebar: 
    nav: "manifolds-ko"

date: 2026-06-11
weight: 22
published: false

---

이번 글의 목표는 미적분학의 기본정리

$$\int_a^bf'(t)\,dt=f(b)-f(a)$$

를 manifold의 언어로 일반화하는 것이다. 좌변은 "도함수를 영역 위에서 적분한 것"이고 우변은 "원래 함수를 영역의 경계에서 (부호를 붙여) 읽은 것"이므로, [§적분](/ko/math/manifolds/integration)과 [§경계가 있는 다양체](/ko/math/manifolds/manifolds_with_boundary)의 언어로는 다음과 같이 일반화되어야 할 것이다. 도함수의 역할은 외미분 $$d$$가, 영역의 역할은 oriented manifold with boundary가, 부호의 역할은 induced orientation이 맡는다.

## 경계가 있는 다양체 위에서의 적분

우선 [§적분](/ko/math/manifolds/integration)의 정의가 경계가 있는 경우로 그대로 확장된다는 것을 확인하자. $$\mathbb{H}^m$$의 열린집합 $$V$$ 위의 compactly supported $$m$$-form $$\omega=f\,dr^1\wedge\cdots\wedge dr^m$$에 대하여, 그 적분을 미적분학에서의 반복적분

$$\int_V\omega=\int_{\mathbb{R}^{m-1}}\int_0^\infty f\,dr^m\,dr^1\cdots dr^{m-1}$$

으로 정의한다. 여기서 $$f$$는 $$V$$ 바깥에서 $$0$$으로 확장한 것이다. 한편 $$\partial\mathbb{H}^m$$은 각 변수의 적분에 기여하지 않으므로, 이 적분은 $$V\cap\operatorname{int}\mathbb{H}^m$$ 위에서의 적분과 같다. [§경계가 있는 다양체, ⁋명제 3](/ko/math/manifolds/manifolds_with_boundary#prop3)에서 살펴본 것과 같이 chart들의 transition은 내부를 내부로 보내는 diffeomorphism이므로, 적분의 잘 정의됨과 chart 무관성, 그리고 partition of unity를 통한 전체 적분의 정의는 [§적분](/ko/math/manifolds/integration)에서의 논증이 글자 그대로 적용된다. 즉 oriented manifold with boundary $$M$$ 위의 compactly supported $$m$$-form $$\omega$$에 대하여 $$\int_M\omega$$가 잘 정의된다.

$$m=1$$인 경우에는 [§경계가 있는 다양체](/ko/math/manifolds/manifolds_with_boundary)에서 살펴본 것과 같이 positively oriented chart만으로 $$M$$을 덮지 못할 수 있으므로, negatively oriented chart $$(U,x)$$에 대해서는

$$\int_M\omega=-\int_{x(U)}(x^{-1})^\ast\omega\qquad(\supp\omega\subseteq U)$$

으로 부호를 붙여 정의한다. 이것이 잘 정의되는 것은 orientation을 뒤집는 transition에 [§적분, ⁋정리 3](/ko/math/manifolds/integration#thm3)을 적용하면 절댓값 때문에 부호가 한 번 더 바뀐다는 것으로부터 확인된다.

마지막으로 $$0$$차원의 경우를 약속하자. Oriented $$0$$차원 manifold는 부호 $$\epsilon(p)=\pm1$$가 주어진 (discrete한) 점들의 모임이고, compactly supported $$0$$-form은 유한 개의 점에서만 $$0$$이 아닌 함수 $$f$$이므로, 그 적분을

$$\int_Mf=\sum_{p\in M}\epsilon(p)f(p)$$

으로 정의한다.

## 스토크스 정리

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Stokes)**</ins> $$m\geq1$$차원의 oriented manifold with boundary $$M$$과 compactly supported $$(m-1)$$-form $$\omega$$가 주어졌다 하자. $$\partial M$$에 induced orientation을 주고 $$\iota:\partial M \rightarrow M$$을 inclusion이라 하면, 다음의 식

$$\int_Md\omega=\int_{\partial M}\iota^\ast\omega$$

이 성립한다. 특히 $$\partial M=\emptyset$$이라면 $$\int_Md\omega=0$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 partition of unity를 통해 주장을 국소적인 명제로 줄이자. $$M$$을 덮는 chart들 $$(U_\alpha,x_\alpha)$$와 이에 subordinate한 smooth partition of unity $$(\phi_i)$$를 택하면 ([§미분다양체, §§Smooth partition of unity](/ko/math/manifolds/smooth_manifolds)), $$\supp\omega$$가 compact이므로 $$\omega=\sum_i\phi_i\omega$$는 유한 합이다. 한편 $$\sum_i\phi_i=1$$로부터 $$\sum_id\phi_i=0$$이므로

$$\sum_id(\phi_i\,\omega)=\sum_i\bigl(d\phi_i\wedge\omega+\phi_i\,d\omega\bigr)=d\omega$$

이고, 양변이 모두 $$\omega$$에 대해 선형이므로 $$\supp\omega$$가 하나의 chart $$(U,x)$$에 들어가는 경우만 증명하면 충분하다. $$m\geq2$$라면 chart를 positively oriented로 택할 수 있다. ([§경계가 있는 다양체](/ko/math/manifolds/manifolds_with_boundary))

이제 $$m\geq 2$$라 하고, $$V=x(U)\subseteq\mathbb{H}^m$$ 위에서 $$\eta=(x^{-1})^\ast\omega$$를 좌표로 적자.

$$\eta=\sum_{i=1}^mf_i\;dr^1\wedge\cdots\wedge\widehat{dr^i}\wedge\cdots\wedge dr^m$$

여기서 $$\widehat{dr^i}$$는 해당 항을 생략한다는 뜻이고, $$f_i$$들은 compactly supported인 $$C^\infty$$ 함수들로 $$V$$ 바깥에서 $$0$$으로 확장한다. 외미분을 계산하면 $$dr^j\wedge dr^1\wedge\cdots\wedge\widehat{dr^i}\wedge\cdots\wedge dr^m$$은 $$j=i$$가 아니면 $$0$$이고 $$j=i$$일 때 $$(-1)^{i-1}dr^1\wedge\cdots\wedge dr^m$$이므로

$$d\eta=\sum_{i=1}^m(-1)^{i-1}\frac{\partial f_i}{\partial r^i}\;dr^1\wedge\cdots\wedge dr^m$$

이다. 따라서

$$\int_Md\omega=\int_{\mathbb{H}^m}d\eta=\sum_{i=1}^m(-1)^{i-1}\int_{\mathbb{H}^m}\frac{\partial f_i}{\partial r^i}\,dr^1\cdots dr^m$$

이다. $$i<m$$인 항들은 $$r^i$$에 대한 적분을 가장 안쪽에서 수행하면, $$f_i$$가 compact support를 가지므로 미적분학의 기본정리에 의하여

$$\int_{-\infty}^\infty\frac{\partial f_i}{\partial r^i}\,dr^i=0$$

이 되어 사라진다. $$i=m$$인 항은 $$r^m$$에 대한 적분을 가장 안쪽에서 수행하면

$$\int_0^\infty\frac{\partial f_m}{\partial r^m}\,dr^m=-f_m(r',0)$$

이므로, $$r'=(r^1,\ldots,r^{m-1})$$에 대하여

$$\int_Md\omega=(-1)^{m-1}\int_{\mathbb{R}^{m-1}}\bigl(-f_m(r',0)\bigr)\,dr'=(-1)^m\int_{\mathbb{R}^{m-1}}f_m(r',0)\,dr'$$

을 얻는다. 특히 $$U$$가 $$\partial M$$과 만나지 않는다면 $$f_m(r',0)=0$$이므로 $$\int_Md\omega=0$$이고, 이 경우 $$\iota^\ast\omega=0$$이므로 주장이 성립한다.

이제 경계 쪽을 계산하자. Inclusion $$\partial\mathbb{H}^m\hookrightarrow\mathbb{H}^m$$을 따라 pullback하면 $$r^m$$이 상수함수 $$0$$이 되므로 $$dr^m$$은 $$0$$으로 당겨지고, 따라서 $$i<m$$인 항들이 모두 사라져

$$\iota^\ast\eta=f_m(r',0)\;dr^1\wedge\cdots\wedge dr^{m-1}$$

이다. 그런데 [§경계가 있는 다양체, ⁋정의 9](/ko/math/manifolds/manifolds_with_boundary#def9)의 induced orientation은 제한된 chart $$(r^1,\ldots,r^{m-1})$$이 주는 orientation의 $$(-1)^m$$배이므로

$$\int_{\partial M}\iota^\ast\omega=(-1)^m\int_{\mathbb{R}^{m-1}}f_m(r',0)\,dr'$$

이 되어 두 값이 일치한다.

마지막으로 $$m=1$$인 경우를 살펴보자. $$\omega$$는 compactly supported 함수 $$f$$이고, $$\supp f$$가 chart $$(U,x)$$에 들어간다고 하자. Chart의 부호를 $$\epsilon=\pm1$$이라 하면 적분의 정의에 의해

$$\int_Mdf=\epsilon\int_{x(U)}d\bigl((x^{-1})^\ast f\bigr)$$

이다. 만일 $$x(U)$$가 $$\partial\mathbb{H}^1$$과 만나지 않으면 위에서와 같이 기본정리에 의해 양변이 모두 $$0$$이다. $$x(U)$$가 경계점 $$0$$을 포함하면, $$g=(x^{-1})^\ast f$$에 대하여

$$\int_0^\infty g'(t)\,dt=-g(0)=-f(p)$$

이다. 여기서 $$p=x^{-1}(0)\in\partial M$$이다. 즉 $$\int_Mdf=-\epsilon f(p)$$이다. 한편 chart $$x$$에 대하여 inward vector는 $$\partial/\partial x$$이므로 outward vector $$-\partial/\partial x$$가 positively oriented인 것은 $$\epsilon=-1$$인 것과 동치이고, 따라서 [§경계가 있는 다양체, ⁋정의 9](/ko/math/manifolds/manifolds_with_boundary#def9)에 의해 $$p$$의 부호는 $$\epsilon(p)=-\epsilon$$이다. 그럼

$$\int_{\partial M}\iota^\ast\omega=\epsilon(p)f(p)=-\epsilon f(p)=\int_Mdf$$

가 되어 주장이 성립한다.

</details>

위의 증명을 한 문장으로 줄이자면, Stokes 정리는 본질적으로 미적분학의 기본정리에 partition of unity를 묻힌 것이다. 정리의 형태에서 바로 읽을 수 있는 중요한 특수한 경우는 경계가 없는 경우이다.

<div class="proposition" markdown="1">

<ins id="cor2">**따름정리 2**</ins> 경계가 없는 oriented manifold $$M$$ 위의 compactly supported $$(m-1)$$-form $$\omega$$에 대하여 $$\int_Md\omega=0$$이다. 특히 $$M$$이 compact라면, $$M$$ 위의 임의의 exact $$m$$-form의 적분은 $$0$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 1](#thm1)에서 $$\partial M=\emptyset$$인 경우이다. $$M$$이 compact라면 임의의 미분형식이 compactly supported이므로 둘째 주장이 따라나온다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$M=[0,1]$$에 표준적인 orientation, 즉 $$\operatorname{int}M=(0,1)$$에 $$\mathbb{R}$$의 표준 orientation을 주자. [§경계가 있는 다양체, ⁋예시 5](/ko/math/manifolds/manifolds_with_boundary#ex5)에서 살펴본 것과 같이 $$\partial M=\{0,1\}$$이고, 점 $$1$$에서는 outward vector $$\partial/\partial t$$가 positively oriented이므로 $$\epsilon(1)=+1$$, 점 $$0$$에서는 outward vector가 $$-\partial/\partial t$$이므로 $$\epsilon(0)=-1$$이다. 따라서 임의의 $$C^\infty$$ 함수 $$f$$에 대하여 [정리 1](#thm1)은

$$\int_{[0,1]}df=f(1)-f(0)$$

이 되어 미적분학의 기본정리를 복원한다.

</div>

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> 미적분학에서 다루는 Green 정리, divergence 정리, 고전적인 Stokes 정리는 모두 [정리 1](#thm1)의 특수한 경우이다. 가령 $$\mathbb{R}^2$$의 (경계가 매끄러운) 영역 $$D$$와 $$1$$-form $$\omega=P\,dx+Q\,dy$$에 대하여 $$d\omega=(\partial Q/\partial x-\partial P/\partial y)\,dx\wedge dy$$이므로 [정리 1](#thm1)은 Green 정리가 된다. 이들 고전적 정리들에서 등장하는 "반시계 방향"이나 "바깥쪽 법선" 같은 조건들이 정확히 induced orientation의 내용이다.

</div>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
