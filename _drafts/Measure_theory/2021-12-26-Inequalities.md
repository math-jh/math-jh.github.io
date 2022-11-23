---

title: "Inequalities"
excerpt: "Lebesgue integration"

categories: [Math / Measure Theory]
permalink: /ko/math/measure_theory/inequalities
header:
    overlay_image: /assets/images/Measure_theory/Inequalities.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-12-26
last_modified_at:
weight: 4

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


우리가 지금 하는 내용은 크게 나누자면 세 가지 부분+@으로 나뉜다. 첫 번째 부분은 measure 및 적분을 정의하는 부분으로, 방금 막 끝마친 부분이고, 그 다음 부분은 지금부터 할 functional analysis 맛보기, 세 번째 부분은 라돈-니코딤 정리로 시작하는 미분, 그리고 마지막 +@는 푸비니 정리다.

지금부터 남은 부분 셋 모두에서 가장 많이 쓰이는 내용은 여러 부등식들이다. 때문에 우리는 이번 글에서, 분량은 좀 적더라도 부등식들을 따로 분리해서 살펴본다. 

## Jensen's inequality

우선 가볍게 시작하자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $\varphi:(a,b)\rightarrow\mathbb{R}$이 *convex*라는 것은 임의의 $x,y\in(a,b)$와 $\lambda\in [0,1]$에 대하여 다음의 식

$$\varphi((1-\lambda)x+\lambda y)\leq(1-\lambda)\varphi(x)+\lambda\varphi(y)$$

가 성립하는 것이다.

</div>

위 정의에서 $a,b$는 무한대일 수 있으며, 이 경우 $\varphi$는 (예를 들어) 실수 전체의 집합에서 정의된 convex function이 된다. 정의의 부등식은 우리가 고등학교 때 배웠듯, 함수의 그래프에 두 점을 찍었을 때 이 두 점의 임의의 내분점이 항상 함수의 그래프보다 위에 있으면 된다는 것을 의미한다. 

어렵지 않게, open set 위에서 정의된 임의의 convex function은 continuous임을 보일 수 있다. Removable, jump, essential singularity인 경우를 각각 생각해보면 세 경우 모두 불가능하다는 것을 쉽게 확인할 수 있으며, 엄밀한 증명은 **[Rud]**의 Theorem 3.2에 소개되어 있다.  

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2 (Jensen)**</ins> Probability measure space $(\Omega, \mathfrak{M},\mu)$가 주어졌다 하자.[^1] Real-valued function $f\in L^1(\mu)$가 $a<f(x)<b$를 모든 $x\in\Omega$에 대해 만족하고, $\varphi$가 $(a,b)$ 위에서 정의된 convex function이라면 다음의 식

$$\varphi\left(\int_\Omega f\mathop{d\mu}\right)\leq\int_\Omega(\varphi\circ f)\mathop{d\mu}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$t=\int_\Omega f\mathop{d\mu}$라 하면, $\mu$가 probability measure이므로

$$a=a\mu(\Omega)=\int_\Omega a\mathop{d\mu}<t=\int_\Omega f\mathop{d\mu}<\int_\Omega b\mathop{d\mu}=b\mu(\Omega)=b$$

가 성립한다. Convexity에 의하여, $a<s<t<u<b$를 만족하는 $s,u$에 대해 항상

$$\frac{\varphi(t)-\varphi(s)}{t-s}\leq\frac{\varphi(u)-\varphi(t)}{u-t}$$

가 성립하고, 따라서 $\beta=\sup_{a<s<t}\frac{\varphi(t)-\varphi(s)}{t-s}$라 하면

$$\frac{\varphi(s)-\varphi(t)}{s-t}\leq\beta\leq\frac{\varphi(u)-\varphi(t)}{u-t}$$

가 임의의 $s,u\in (t,b)$에 대해 성립한다. 양쪽 부등식을 각각 정리하면, 임의의 $s\in (a,t)$이든, $s\in (t,b)$이든 다음의 식

$$\varphi(s)\geq\varphi(t)+\beta(s-t)$$

이 성립한다는 것을 확인할 수 있고, 또 $s=t$일 때도 위 식은 자명하게 성립하므로 이 식은 *모든* $s\in (a,b)$에 대해 성립한다. 임의의 $x$에 대해 $f(x)\in (a,b)$이므로, 다음의 식

$$\varphi(f(x))\geq\varphi(t)+\beta(f(x)-t)$$

도 항상 성립하고 따라서 양 변을 적분하면

$$\int_\Omega(\varphi\circ f)\mathop{d\mu}\geq\int_\Omega(\varphi(t)+\beta(f(x)-t))\mathop{d\mu}=\varphi(t)-\beta t+\beta\int_\Omega f\mathop{d\mu}=\varphi\left(\int_\Omega f\mathop{d\mu}\right)$$

를 얻는다.

</details>

## Hölder's inequality

임의의 양의 실수 $p$에 대하여, 

$$\frac{1}{p}+\frac{1}{q}=1$$

을 만족하는 $q$를 $p$의 *conjugate exponent*라 부른다. 예를 들어, $p=q=2$는 자기 자신이 스스로의 conjugate exponent이고, 만약 $p=3$이라면 그 conjugate exponent는 $q=3/2$이 될 것이다. 우리는 특별히 $p$가 1이 되는 경우도 허용한다. 이 경우, $1/p$ 자체가 1이 되므로, $1/q=0$이어야 한다. 이를 위해서는 $1$과 $\infty$가 서로의 conjugate exponent라고 생각하면 될 것이다. 

이 pair는 앞으로 중요한 순간순간마다 등장할 것이다. 그리고, 우리가 소개할 두 부등식, Hölder inequality와 Minkowski inequality는 이를 다루는 데에 유용한 도구를 제공해줄 것이다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3 (Hölder)**</ins> Measure space $(X,\mathfrak{M},\mu)$가 주어졌다 하자. 또, $1<p<\infty$와 그 conjugate exponent $q$를 고정하자. 그럼 두 measurable function $f,g:X\rightarrow[0,\infty]$에 대하여, 다음의 부등식

$$\int_X fg\mathop{d\mu}\leq\left(\int_X f^p\mathop{d\mu}\right)^{1/p}\left(\int_X g^q\mathop{d\mu}\right)^{1/q}$$

가 항상 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 다음과 같이 두 상수

$$A^p=\int_X f^p\mathop{d\mu},\quad B^q=\int_X g^q\mathop{d\mu}$$

를 정의하자. 만약, 예를 들어 $A=0$이라면 $f=0$ a.e.이고, 따라서 $fg$ 또한 a.e. 0이 되므로, 부등식이 성립한다. 또, 만약 $A=\infty$이고 $B>0$이라면 우변이 $\infty$이므로 이 경우에도 부등식은 자명하다. 그러므로 우리는 $0<A,B<\infty$인 경우만 고려하면 충분하다. 

이제 $F=f/A$, $G=g/B$와 같이 두 함수를 normalize하자. 그럼

$$\int_X F^p\mathop{d\mu}=\int_X \frac{f^p}{A^p}\mathop{d\mu}=\frac{1}{A^p}\int_X f^p\mathop{d\mu}=1$$

이고 유사하게 $\int_X G^q\mathop{d\mu}=1$이다. $0<F(x), G(x)<\infty$를 만족하는 $x\in X$를 모아 이들을 $E$라 하면 $f,g$가 measurable이므로 $E$ 또한 measurable이고, 이러한 $E$ 위에서는 적당한 함수 $s(x)$, $t(x)$를 잡아 

$$F(x)=e^{s(x)/p},\quad G(x)=e^{t(x)/q}$$

로 쓸 수 있다. 그럼 

$$F(x)G(x)=e^{s(x)/p+t(x)/q}$$

이고, 우변은 $t$에 대한 함수 $e^t$의 convexity에 의하여

$$e^{s(x)/p+t(x)/q}\leq\frac{1}{p}e^{s(x)}+\frac{1}{q}e^{t(x)}\tag{1}$$ 

가 성립한다. 즉,

$$F(x)G(x)\leq \frac{1}{p}F(x)^p+\frac{1}{q}G(x)^q$$

이고, 이를 적분하면 

$$\begin{aligned}\int_X F(x)G(x)\mathop{d\mu}&=\int_E F(x)G(x)\mathop{d\mu}\leq\frac{1}{p}\int_E F^p\mathop{d\mu}+\frac{1}{q}\int_EG^q\mathop{d\mu}\\
&\leq\int_XF^p\mathop{d\mu}+\int_XG^q\mathop{d\mu}\\
&=\frac{1}{p}+\frac{1}{q}=1\end{aligned}$$

이 성립한다. 이제 원래대로 $F=f/A$, $G=g/B$를 대입하면

$$\int_X f(x)g(x)\leq AB=\left(\int_X f^p\mathop{d\mu}\right)^{1/p}\left(\int_X g^q\mathop{d\mu}\right)^{1/q}$$

를 얻는다.

</details>

Hölder inequality의 등호는 $e^t$의 convexity를 이용한 부등식 (1)의 등호가 a.e. 성립할 때 얻어지며, 이 조건은 따라서 $F^p=G^q$ a.e. 로 생각할 수 있다. 한편 $p=q=2$인 경우, 이 부등식은 우리가 잘 알고 있는 Cauchy-Schwartz 부등식이 된다. 

## Minkowski's inequality

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4 (Minkowski)**</ins> Measure space $(X,\mathfrak{M},\mu)$가 주어졌다 하자. 또, $1<p<\infty$를 고정하자. 그럼 다음의 부등식

$$\left(\int_X(f+g)^p\mathop{d\mu}\right)^{1/p}\leq\left(\int_X f^p\mathop{d\mu}\right)^{1/p}+\left(\int_Xg^p\mathop{d\mu}\right)^{1/p}$$

이 항상 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선

$$(f+g)^p=f(f+g)^{p-1}+g(f+g)^{p-1}$$

이고, 앞선 Hölder's inequality를 각 term에 적용하면

$$\int f(f+g)^{p-1}\mathop{d\mu}\leq\left(\int f^p\mathop{d\mu}\right)^{1/p}\left(\int (f+g)^{(p-1)q}\right)^{1/q}$$

그리고

$$\int g(f+g)^{p-1}\mathop{d\mu}\leq\left(\int g^p\mathop{d\mu}\right)^{1/p}\left(\int (f+g)^{(p-1)q}\right)^{1/q}$$

를 얻는다. 위 두 식의 양변을 더하면,

$$\int (f+g)^p\mathop{d\mu}\leq\left(\left(\int_X f^p\mathop{d\mu}\right)^{1/p}+\left(\int_X g^p\mathop{d\mu}\right)^{1/p}\right)\left(\int (f+g)^{(p-1)q}\mathop{d\mu}\right)^{1/q}$$

이 성립한다. 그런데 $p,q$는 conjugate exponent이므로, 계산을 해 보면 $(p-1)q=p$이고 (양 변을 $pq$로 나누면 사실 conjugate exponent의 정의 자체다) 따라서 

$$\int (f+g)^p\mathop{d\mu}\leq\left(\left(\int_X f^p\mathop{d\mu}\right)^{1/p}+\left(\int_X g^p\mathop{d\mu}\right)^{1/p}\right)\left(\int (f+g)^{p}\mathop{d\mu}\right)^{1/q}$$

이 된다. Hölder's inequality와 마찬가지로, 우리는 각 적분 $\int_X f\mathop{d\mu}$와 $\int_X g\mathop{d\mu}$가 모두 nonzero, 유한인 경우만 보이면 충분하고, 이 경우에는 $t>0$에서 정의된 함수 $t^p$의 convexity에 의해, 

$$\left(\frac{f+g}{2}\right)^p\leq\frac{1}{2}(f^p+g^p)$$

가 성립하므로 $\int (f+g)^p\mathop{d\mu}\leq 2^{p-1}\int f^p+g^p\mathop{d\mu}$

가 되어 $\int(f+g)^p\mathop{d\mu}$의 값이 유한하다. 따라서 우변에 있는 $\left(\int(f+g)^p\mathop{d\mu}\right)^{1/q}$를 좌변으로 이항하면, $1-1/q=1/p$이므로

$$\left(\int_X(f+g)^p\mathop{d\mu}\right)^{1/p}=\left(\int_X(f+g)^p\mathop{d\mu}\right)^{1-1/q}\leq\left(\int_X f^p\mathop{d\mu}\right)^{1/p}+\left(\int_Xg^p\mathop{d\mu}\right)^{1/p}$$

를 얻는다.

</details>

---
**Reference**

**[Rud]** W. Rudin, *Real and complex analysis*, Mathematics series. McGraw-Hill, 1987.  

---

[^1]: 즉, $\mu(\Omega)=1$이고 $\mu$는 positive measure.
