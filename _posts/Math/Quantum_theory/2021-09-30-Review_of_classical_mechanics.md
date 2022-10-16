---

title: "Review of classical mechanics"
excerpt: "고전역학"

categories: [Math / Quantum Theory]
permalink: /ko/math/quantum_theory/classical_mechanics
header:
    overlay_image: /assets/images/Quantum_theory/Classical_mechanics.png
    overlay_filter: 0.5
sidebar: 
    nav: "physics"

date: 2021-09-30
last_modified_at:
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


## One-dimensional motions

보편적으로, 물리학에서 다루는 미분은 시간 $t$에 대한 미분인 경우가 많다. 이 미분값을 수학에서는 $x'(t)$와 같이 쓰지만, 물리학에서는 $\dot{x}(t)$로 쓰는 것이 보통이다.  예를 들어, 물체의 위치를 $\dot{x}(t)$라 적으면, 이 물체의 속도는

$$v(t)=\dot{x}(t)$$

으로 정의되고, 물체의 가속도는 $v$를 $t$에 대해 한 번 더 미분한

$$a(t)=\dot{x}(t)=\ddot{x}(t)$$

으로 주어진다. 이러한 notation 상에서, 뉴턴의 제 2법칙 $F=ma$는 다음의 식

$$F(t)= m\ddot{x}(t)$$

으로 주어진다. 만약 함수 $F(t)$가 물체의 위치 $x$에만 의존한다면, $t=t_0$에서의 초기조건이 주어진다면 그 근방에서의 local한 solution을 찾는 것은 어렵지 않다. 이 운동방정식의 해 $x(t)$를 *trajectory*라 부른다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 예를 들어, 이상적인 상황에 놓여있는 harmoinic oscillator를 생각해보자. 그럼 후크의 법칙에 의해, $F(x)=-kx$ ($k$는 spring constant)이므로 $F$는 순수하게 $x$에 의해서만 결정된다. 이 때의 solution은

$$x(t)=a\cos(\omega t)+b\sin(\omega t),\qquad \omega=\sqrt{k/m}$$

로 주어지며, $t=t_0$에서의 초기조건 $x(t_0)=x_0$와 $\dot{x}(t_0)=v_0$이 주어진다면 $a$와 $b$의 값을 결정할 수 있을 것이다. 
</div>

고전역학에서 중요한 것 중 하나는 에너지 보존법칙이다. 어떠한 물체가 운동을 할 때 특정한 값이 보존된다면, 우리는 이 값이 어떤 식으로든 이 물체의 운동을 표현하고 있다고 생각할 수 있다. 가장 단순한 예시는 우리가 고등학교 때 배우는 역학적 에너지다. 

아까와 같은 가정으로, $F$가 $x$에만 의존한다고 가정하자. 그럼 *potential energy*는 다음의 식

$$V(x)=-\int F(x)\mathop{dx}$$

으로 주어진다. 즉, $F(x)=-dV/dx$이고, 그럼 chain rule에 의해 

$$\frac{d}{dt}V(x(t))=\frac{dV}{dx}\frac{dx}{dt}=-F(x(t))\dot{x}(t)$$

가 될 것이다. 이 때, 이 계의 총 *에너지*를 운동에너지와 퍼텐셜에너지의 합

$$E(x,v)=\frac{1}{2}mv^2+V(x)$$

으로 정의한다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 어떤 입자가 $F(x)=m\ddot{x}$를 만족한다고 하고, $E(x,v)$가 위와 같이 주어졌다고 가정하자. 그럼 $E$는 시간에 대해 불변이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉, $E$의 시간에 대한 미분이 0임을 보이면 된다. 

$$\begin{aligned}
\frac{d}{dt}E(x(t),\dot{x}(t))&=\frac{d}{dt}\left(\frac{1}{2}m(\dot{x}(t))^2+V(x)\right)\\
&=m\dot{x}(t)\ddot{x}(t)-F(x(t))\dot{x}(t)\\
&=\dot{x}(t)[m\ddot{x}(t)-F(x(t))]
\end{aligned}$$

그런데, $m\ddot{x}(t)-F(x(t))$는 뉴턴의 법칙에 의해 정확히 0이 되므로, 이 값은 운동의 불변량이 된다. 

</details>

수리물리학에서 *phase space*란 운동하는 물체의 상태를 나타내는 공간이다. 고전역학에서, 물체의 운동은 물체의 위치와 물체의 속도로 정확하게 주어지므로 phase space는 $(x,v)$들을 모아둔 공간이고, 우리는 지금은 1차원에서 놀고 있으므로 이 공간은 2차원 공간이 된다. 그렇다면 원래의 운동방정식 $F(x)=m\ddot{x}$를 푸는 것은 다음의 조건

$$\frac{dx}{dt}=v(t),\qquad \frac{dv}{dt}=\frac{1}{m}F(x(t))$$

을 만족하는 두 개의 함수 $x$와 $v$를 찾는 것이 된다. 그럼 이제 운동방정식의 solution을 찾는 것은, phase space 상에서 다음의 level set

$$\{(x,v)\in\mathbb{R}^2: E(x,v)=E(x_0,v_0)\}$$

을 그리는 것과 같다. 혹은, 미분다양체에서 했던 것을 생각하면 이건 integral flow를 찾는 문제가 된다. 위에서 다뤘던  

---

**Reference**

- [Mun00] J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---
