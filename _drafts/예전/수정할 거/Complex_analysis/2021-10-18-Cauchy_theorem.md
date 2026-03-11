---

title: "Cauchy's theorem"
excerpt: "Cauchy's theorem and its application"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/Cauchy_theorem
header:
    overlay_image: /assets/images/Complex_analysis/Cauchy_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-10-18
last_modified_at:
weight: 2

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>

이전 글에서 언급했듯, 복소해석학을 하며 처음 잡게 되는 목표는 Cauchy's theorem을 증명하는 것이다. 하지만 이것이 바로 가능한 것은 아니고, 우리는 우선 다음과 같이 약한 Cauchy's theorem을 우선 증명한다. 

<div class="proposition" markdown="1">

<ins id="thm0">**정리 (Cauchy's theorem on open disc)**</ins> Open disc $D$ 위에 정의된 임의의 holomorphic function $f$와, $D$에 포함된 임의의 closed curve $\gamma$에 대하여,

$$\int_\gamma f(z)\mathop{dz}=0$$

이 항상 성립한다.

</div>

사실은, 이 정리의 증명으로부터 우리는 open disc 뿐만 아니라 몇몇 특수한 영역들에 대해서도 이것이 성립한다는 것을 알 수 있고, 이를 이용해서 몇몇 재미있는 결과들을 우선 증명할 것이다. 

## Goursat's theorem

이를 위해서 우리는 우리가 생각할 수 있는 가장 간단한 closed curve인 삼각형을 생각할 것이다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Goursat)**</ins> $\Omega$가 $\mathbb{C}$의 open set이라 하고, $T$가 $\Omega$ 안에 포함되어 있는 삼각형 모양의 curve이고, $T$의 내부 또한 $\Omega$에 포함된다 하자. $f$가 $\Omega$에서 정의된 임의의 holomorphic function이라면, 다음의 식

$$\int_T f(z)\mathop{dz}=0$$

이 항상 성립한다.

</div>

몇 가지 핵심 아이디어만 기억하면 남는 증명은 거의 verification 뿐이다. 이 명제를 보이기 위해서 우리는 임의의 $\epsilon&gt;0$에 대하여, 

$$\left\lvert\int_T f(z)\mathop{dz}\right\rvert\leq\epsilon$$

임을 보이면 충분하다. 어차피 우리가 지금 아는 적분에 대한 부등식은 

$$\left\lvert\int_\gamma f(z)\mathop{dz}\right\rvert\leq\length(\gamma)\sup_{z\in\gamma}f(z)$$

뿐이므로, 마지막에는 결국 여기에 의존해야 할 것이다. 또, 위 부등식을 이용하기 위해서는 $\length(\gamma)$를 어떻게든 0으로 보내야 한다는 것도 대충 감이 온다. 여기에서 가장 crucial한 아이디어는, 이를 위해 삼각형을 다음과 같이 4등분하는 것이다.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

대략적인 증명의 흐름은 이렇게 삼각형을 반복해서 줄여가며 이전 적분을 bound시키고, 따라서 최종적으로는 첫 번째 적분 $\int_T f(z)\mathop{dz}$가 이 $n$번째 step에 의해 항상 bound되도록 하는 것이다. 그럼 $n$이 커질수록 적분 경로는 작아지므로, 앞선 부등식을 사용하면 될 것이다.

<details class="proof--alone" markdown="1">
<summary>정리 1의 증명</summary>

우선, 위 그림과 같이 삼각형을 네 조각으로 나누면 원래 삼각형 내부에 있는 작은 삼각형들은 적분 경로가 상쇄되어 없어지게 된다. 따라서

$$\int_T f(z)\mathop{dz}=\int_{T_1} f(z)\mathop{dz}+\int_{T_2} f(z)\mathop{dz}+\int_{T_3} f(z)\mathop{dz}+\int_{T_4} f(z)\mathop{dz}$$

가 된다. $T_i$들 가운데 적분값을 가장 크도록 하는 것을 하나 골라 이를 $j$라 하면 위의 식으로부터 부등식

$$\left\lvert\int_T f(z)\mathop{dz}\right\rvert\leq4\left\lvert\int_{T_j}f(z)\mathop{dz}\right\rvert$$

을 얻게 된다. 원래의 삼각형 $T$를 $T^{(0)}$이라 적고, 이렇게 해서 새로 얻어진 삼각형을 $T^{(1)}$이라 하자. 그럼 이 과정을 반복하면

$$\left\lvert\int_{T^{(0)}}f(z)\mathop{dz}\right\rvert\leq4^n\left\lvert\int_{T^{(n)}}f(z)\mathop{dz}\right\rvert$$

를 얻게 된다. 한편, 이 삼각형들의 (경계를 포함한) 내부를 생각하면, 이들은 compact set들의 decreasing sequence이고 그 크기가 0으로 수렴하므로, 어떤 유일한 점 $z_0$이 존재하여 이들의 교집합이 singleton $\\{z_0\\}$이 된다. $f$는 $\Omega$의 모든 점에서 holomorphic이므로, 특히 $z_0$에서도 holomorphic하고 따라서 다음과 같은 approximation

$$f(z)=f(z_0)+f'(z_0)(z-z_0)+\psi(z)(z-z_0)\qquad\text{near $z_0$}$$

을 얻는다. 여기에서 $\psi(z)$는 $z\rightarrow z_0$일 때 $0$으로 가는 적당한 remainder function이다. 그런데 constant function $f(z_0)$와, linear function $f'(z_0)(z-z_0)$은 각각 자명한 primitive들을 가지므로, 이들을 삼각형 $T^{(n)}$을 따라 적분한 값은 0이고, 따라서 위 식의 양변을 적분하면 우변의 앞의 두 term이 사라져서

$$\int_{T^{(n)}}f(z)\mathop{dz}=\int_{T^{(n)}}\psi(z)(z-z_0)\mathop{dz}$$

를 얻는다. 이제 우리가 미리 생각해놨듯, 

$$\left\lvert\int_{T^{(n)}}f(z)\mathop{dz}\right\rvert=\left\lvert\int_{T^{(n)}}\psi(z)(z-z_0)\mathop{dz}\right\rvert$$

을 우선 얻고, 우변은 다시 

$$\operatorname{legnth}(T^{(n)})\sup\lvert\psi(z)(z-z_0)\rvert\leq d_nl_n\epsilon_n$$

으로 bound시킬 수 있다. 여기에서 $d_n$은 $T^{(n)}$의 내부를 포함한 삼각형의 diameter, $l_n$은 $T^{(n)}$의 length, 그리고 $\epsilon_n$은 이 경로 위에서의 $\psi$의 supremum이다. 그런데, 잘 살펴보면 $d_n$과 $l_n$은 하나의 스텝이 진행될 때마다 각각 절반이 된다는 것을 알 수 있으므로, 이 부등식의 우변을 다시 써서 원래의 식과 합치면

$$\left\lvert\int_{T^{(n)}} f(z)\mathop{dz}\right\rvert\leq\epsilon_n 4^{-n}d_0l_0$$

을 얻는다. 그럼 이제

$$\left\lvert\int_{T^{(0)}} f(z)\mathop{dz}\right\rvert\leq4^n\left\lvert\int_{T^{(n)}}f(z)\mathop{dz}\right\rvert\leq 4^n(\epsilon_n 4^{-n}d_0l_0)=\epsilon_nd_0l_0$$  
 
 이다. $n$이 커질수록 $\epsilon_n\rightarrow 0$이므로, 우리는 원하는 결과를 얻는다.
</details>

임의의 다각형을 삼각형들로 쪼개면 이 정리를 어렵지 않게 임의의 다각형으로 확장할 수 있다. 그러나 이러한 방법으로는 결코 open disc에 닿을 수 없다는 것도 자명하다. 

## Cauchy's theorem on open disc

따라서 우리는 뭔가 다른 방법을 찾아야 한다. 다음 명제의 증명에서 우리는 primitive $F$를 직접 만드는 방법을 생각하게 된다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Cauchy)**</ins> Open disc $D$ 위에 정의된 임의의 holomorphic function $f$와, $D$에 포함된 임의의 closed curve $\gamma$에 대하여,

$$\int_\gamma f(z)\mathop{dz}=0$$

이 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§Cauchy-Riemann equation, 명제 6](/ko/math/complex_analysis/Cauchy-Riemann_equation#pp6)에 의하여, $f$가 primitive $F$를 갖는다는 것만 보이면 충분하다. 일반성을 잃지 않고 주어진 disc $D$의 중심이 원점이라 하자. 임의의 point $z\in D$에 대하여, 우리는 다음의 경로 $\gamma_z$를 생각할 수 있다.

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

이제 $F(z)$를 식

$$F(z)=\int_{\gamma_z}f(w)\mathop{dw}$$

으로 정의하자. 이제 우리는 $F$가 holomorphic이라는 것을 보여야 한다. 충분히 작은 $h$에 대하여 $z+h\in D$라 하자. 그럼

$$F(z+h)-F(z)=\int_{\gamma_{z+h}}f(w)\mathop{dw}-\int_{\gamma_z}f(w)\mathop{dw}$$

에서, 예를 들면 다음과 같이 경로를 만들어주면

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

삼각형 경로를 따르는 적분들은 모두 Goursat's theorem에 의해 0이 되므로, 우리는 이 값이 사실은 $z$와 $z+h$를 잇는 straight line을 따른 $f$의 적분

$$\int_\eta f(w)\mathop{dw}$$

이라는 것을 알 수 있다. 그런데, $f$의 continuity를 이용하면, $z$ 근처에서 $f$는

$$f(w)=f(z)+\psi(w),\qquad \psi(w)\rightarrow 0\text{ as }w\rightarrow z$$

으로 쓸 수 있다. 따라서 

$$F(z+h)-F(z)=f(z)\int_\eta \mathop{dw}+\int_\eta\psi(w)\mathop{dw}$$

인데, $\int\_\eta \mathop{dw}$에서 피적분함수 1은 primitive $w$를 가지므로, 이 값은 그냥 양 끝값의 차이인 $h$가 되고, 남는 두 번째 항은

$$\left\lvert\int_\eta\psi(w)\mathop{dw}\right\rvert\leq\length(\eta)\sup_{w\in\eta}\left\lvert\psi(w)\right\rvert=\sup_{w\in\eta}\left\lvert\psi(w)\right\rvert h$$

가 된다. 따라서, 

$$\left\lvert\frac{F(z+h)-F(z)}{h}-f(z)\right\rvert\leq \frac{1}{h}\left\lvert h\sup_{w\in\eta}\left\lvert\psi(w)\right\rvert\right\rvert=\sup_{w\in\eta}\left\lvert\psi(w)\right\rvert\rightarrow 0$$  

이므로, 원하는대로 $F'(z)=f(z)$를 얻는다.

</details>

사실 우리가 처음에 적분 경로 $\gamma_z$를 원점과 $z$를 잇는 line segment로 잡았어도 다음의 그림

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

과 같이 Goursat's theorem을 적용할 수 있었다. 따라서, 이 정리는 사실 임의의 *convex* set에 대해서도 성립한다. 하지만 convex set 또한 이 정리의 적합한 일반화는 아니고, 이보다 훨씩 약한 조건인 *simply connected* 조건만 있어도 성립한다. 예를 들어, 다음과 같이 주어진 집합

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

에 대해서도 적당히 꺾여있는 다음의 curve

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

를 생각하면 어렵지 않게 이 집합 안에서도 Cauchy's theorem이 성립한다는 것을 알 수 있다. 특히 방금 소개한 이 열쇠구멍 모양의 집합은 앞으로 매우 자주 사용할 것이다.

## Cauchy's integral formula

Stein은 여기에서 잠깐 멈추고 여러가지 예시들을 소개하는데, 그건 어차피 연습문제를 풀면 되니 바로 Cauchy's integral formula를 살펴보자. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Cauchy's integral formula for a disc)**</ins> $f$가 어떤 disc $D$의 closure를 포함하는 open set $\Omega$ 위에서 holomorphic이라 하자. 그럼 임의의 $z\in D$에 대하여,

$$f(z)=\frac{1}{2\pi i}\int_{\partial D}\frac{f(w)}{w-z}\mathop{dw}$$

가 성립한다.[^1]

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞서 소개한 keyhole 모양의 경로 $\Gamma$를 이용한다. 

![<#description#>](/assets/images/<#path#>/<#name#>.png){:width="250px"  class="invert" .align-center}

열쇠구멍 안의 작은 원이 $z$를 중심으로 하는 반지름 $\epsilon$짜리 원이고, 이 작은 원과 $\partial D$를 잇는 직선경로들 사이의 거리가 $\delta$라 하자. 피적분함수 $F(w)=f(w)/(w-z)$는 어차피 $w=z$를 제외하면 holomorphic하므로, 

$$\int_\Gamma F(w)\mathop{dw}=0$$

이 성립한다. 이제 $\delta\rightarrow 0$이라 하면 $F$의 continuity에 의해 이 두 경로는 서로 상쇄될 것이므로, 결국은 바깥쪽 원 (반시계방향)과 안쪽 원(시계방향)만 남게 된다. 안쪽 원을 $C_\epsilon$이라 표기하자. 

$$F(w)=\frac{f(w)-f(z)}{w-z}+\frac{f(z)}{w-z}$$

라 하면, 우변의 첫째 항은 $f$가 holomorphic하므로 bounded되어있고, 따라서 적분경로 $C\_\epsilon$이 $\epsilon\rightarrow 0$에 따라 짧아지면 0이 된다. 따라서 두 번째 term만 살펴보면 충분하다. $C\_\epsilon$을 $z+\epsilon e^{-2\pi i t}$으로 parmetrize하면 간단한 계산을 통해,

$$\begin{aligned}\int_{C_\epsilon}\frac{f(z)}{w-z}\mathop{dw}&=f(z)\int_{C_\epsilon}\frac{dw}{w-z}=f(z)\int_0^1\frac{-2\pi i \epsilon e^{-2\pi it}}{\epsilon e^{-2\pi i t}}\mathop{dt}\\&=-2\pi i f(z)\int_0^1\mathop{dt}=-2\pi i f(z)\end{aligned}$$

를 얻는다. 따라서, 

$$0=\int_\Gamma F(w)\mathop{dw}=\int_{\partial D}F(w)\mathop{dw}+\int_{C_\epsilon} F(w)\mathop{dw}=\int_{\partial D}\frac{f(w)}{w-z}\mathop{dw}-2\pi i f(z)$$

로부터 원하는 결과를 얻는다.

</details>

이를 이용하면 임의의 holomorphic function $f$를 power series를 통해 나타낼 수 있다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Open set $\Omega$ 위에서 정의된 holomorphic function $f$를 생각하자. 그럼 임의의 $z_0\in\Omega$와 $z_0$을 포함하고, 그 closure가 $\Omega$에 포함되는 disc $D$에 대하여, $f$는 $z_0$을 중심으로 하는 power series expansion

$$f(z)=\sum_{n=0}^\infty a_n(z-z_0)^n$$

을 가지며, 이 때 계수 $a_n$들은 다음의 식

$$a_n=\frac{f^{(n)}(z_0)}{n!}$$

으로 주어진다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $z\in D$가 주어졌다 하자. 그럼 앞선 [정리 3](#thm3)에 의하여, 

$$f(z)=\frac{1}{2\pi i}\int_{\partial D}\frac{f(w)}{w-z}\mathop{dw}$$

가 성립한다. 그런데, 임의의 $w\in\partial D$에 대하여, $D$의 반지름을 $r$이라 하면 부등식

$$\left\lvert\frac{z-z_0}{w-z_0}\right\rvert=\frac{\lvert z-z_0\rvert}{r}<1$$

이 성립하므로, 

$$\frac{1}{w-z}=\frac{1}{w-z_0-(z-z_0)}\frac{1}{w-z_0}\frac{1}{1-\frac{z-z_0}{w-z_0}}=\frac{1}{w-z_0}\sum_{n=0}^\infty\left(\frac{z-z_0}{w-z_0}\right)^n$$

이 성립한다. 뿐만 아니라, $z$가 fix되어있으므로 이 series는 사실 임의의 $w$에 대해 uniformly convergent이고, 따라서 이 식을 Cauchy's integral formula에 대입한 후 적분과 무한합의 순서를 바꾸면

$$\begin{aligned}f(z)&=\frac{1}{2\pi i }\int_{\partial D}\frac{f(w)}{w-z}\mathop{dw}=\frac{1}{2\pi i}\int_{\partial D}\frac{f(w)}{w-z_0}\sum_{n=0}^\infty\left(\frac{z-z_0}{w-z_0}\right)^n\mathop{dw}\\&=\sum_{n=0}^\infty a_n(z-z_0)^n\end{aligned}$$

이며, $a_n$ 또한 증명하려던 것과 동일하다.

</details>

따라서, 임의의 holomorphic function은 정의역의 내부 점에서 무한 번 미분 가능하다. 뿐만 아니라, 우리는 $f$의 $z=z_0$에서의 $n$th derivative 또한 위 식으로부터 쉽게 얻을 수 있다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $f$가 open set $\Omega$에서 holomorphic하다고 가정하자. 그 closure가 $\Omega$에 포함된 open disc $D$에 대하여, 

$$f^{(n)}(z)=\frac{n!}{2\pi i}\int_{\partial D}\frac{f(w)}{(w-z)^{n+1}}\mathop{dw}$$

는 임의의 $z\in D$에 대해서도 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Induction으로 진행한다. $n=0$은 Cauchy's integral formula에 의해 자명하다. 만일

$$f^{(n-1)}(z)=\frac{(n-1)!}{2\pi i }\int_{\partial D}\frac{f(w)}{(w-z)^n}\mathop{dw}$$

가 성립한다면, 단순한 계산을 통해

$$\frac{f^{(n-1)}(z+h)-f^{(n-1)}(z)}{h}=\frac{(n-1)!}{2\pi i}\int_{\partial D} f(w)\frac{1}{h}\left(\frac{1}{(w-z-h)^n}-\frac{1}{(w-z)^n}\right)\mathop{dw}$$

임을 알 수 있다. 이제 $A^n-B^n$의 전개식에서, $A=(w-z-h)^{-1}$, $B=(w-z)^{-1}$로 둔 후 $h\rightarrow 0$을 취하면 $A\approx B$에서 이들은

$$\frac{h}{(w-z)(w-z)}\cdot \frac{n}{(w-z)^{n-1}}$$

이 되고, 이를 원래 식에 대입하면 원하는 결과인

$$f^{(n)}(z)=\frac{(n-1)!}{2\pi i}\int_{\partial D} f(w)\frac{1}{h}\frac{h}{(w-z)^2}\frac{n}{(w-z)^{n-1}}\mathop{dw}=\frac{n!}{2\pi i}\int_{\partial D}\frac{f(w)}{(w-z)^{n+1}}\mathop{dw}$$

를 얻는다. 

</details>

따라서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="crl6">**따름정리 6 (Cauchy inequality)**</ins> $f$가 중심 $z_0$, 반지름 $R$로 정의된 disc $D$의 closure를 포함하는 open set $\Omega$에서 holomorphic하다고 하자. 만약 $f$가 $\partial D$에서 $B$로 bounded되어있다면, $f^{(n)}$들은 모두 $D$ 안에서 bounded되어있고 다음의 부등식

$$\lvert f^{(n)}(z_0)\rvert\leq\frac{n!B}{R^n}$$

이 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 명제에서 $w-z=R$이고, $\partial D$의 길이는 $2\pi R$이므로 자명하다.  

</details>
Cauchy's theorem은 다음과 같이 쓸만한 converse를 갖는다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7 (Morera)**</ins> $f$가 open disc $D$ 위에서 정의된 continuous function이라 하자. 만약 $D$에 포함된 임의의 triangle $T$에 대하여, $\int_{\partial D} f(z)\mathop{dz}=0$이 성립한다면 $f$는 $D$ 위에서 holomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, Cauchy's theorem을 증명할 때 우리는 $f$가 holomorphic이라는 조건을 전부 쓴 것이 아니라, $f$가 continuous하다는 것과, 임의의 삼각형 경로를 따라 $f$를 적분한 것이 0이라는 사실만 이용했다. 따라서, 이 증명을 그대로 따라가면 $f$의 primitive $F$가 존재한다는 것을 알 수 있다. 이제 $F$는 holomorphic function으로써 infinitely differentiable이므로, $f$ 또한 그러하다.

</details>

우리가 지금까지 엄밀하게 *증명*한 Cauchy's theorem은 $f$의 domain이 convex set일 때 뿐이다. 그러나 우리는 이를 조금 더 확장하여 simply connected domain에 대해서도 증명할 수 있다. 이에 대한 것은 다음으로 미뤄두고, 우선은 holomorphic function의 성질들을 조금 더 탐구하자.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> Open set $\Omega$에 대하여, $(f\_n)\_{n=0}^\infty$가 $\Omega$의 임의의 compact subset $K$ 위에서 모두 $f_n$으로 uniformly convergent라 하자.[^2] 그럼 $f$ 또한 $\Omega$에서 holomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Omega$와, 그 closure까지 $\Omega$에 포함된 open disc $D$를 생각하자. $T$가 $D$에 포함된 triangle이라 하면, 각각의 $f_n$들이 holomorphic하므로 Goursat's theorem에 의하여

$$\int_{\partial T}f_n(z)\mathop{dz}=0$$

이 항상 성립한다. 그런데, $\partial T$는 compact이므로, 가정에 의해 적분경로 위에서 $f_n\rightrightarrows f$이므로 적분과 극한의 순서를 바꾸어

$$\int_{\partial T} f_n(z)\mathop{dz}\rightarrow \int_{\partial T}f(z)\mathop{dz}$$

이므로 $\int_{\partial T}f(z)\mathop{dz}=0$인 것을 안다. 따라서, Morera's theorem을 이용하면 $f$는 $D$에서 holomorphic하고, $D$는 임의로 선택할 수 있으므로 $f$는 $\Omega$ 위에서도 holomorphic하다. 
</details>

우리는 여기에서 멈추지 않고, $f_n$들의 *derivative*들 또한 $f'$르 uniformly convergent한다는 것을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Open set $\Omega$에 대하여, $(f\_n)\_{n=0}^\infty$가 $\Omega$의 임의의 compact subset $K$ 위에서 모두 $f_n$으로 uniformly convergent라 하자. 그럼 $f_n$들의 derivative $f_n'\rightrightarrows f'$ uniformly on compacta.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

논의의 편의를 위해 이들이 $\Omega$ 전체에서 uniformly converge한다고 해도 무방하다. 임의의 $\delta>0$에 대하여, $\Omega_\delta$를 다음의 식

$$\Omega_\delta=\{z\in\Omega:\overline{D(z,\delta)}\subset\Omega\}$$

으로 정의된 집합이라 하자. 그럼 우리는 $f_n'$들이 모든 $\Omega_\delta$들에서 uniformly convergent라는 것을 보이면 된다. 우리는 이를 위해 다음의 부등식

$$\sup_{z\in\Omega_\delta}\lvert F'(z)\rvert\leq\frac{1}{\delta}\sup_{w\in\Omega}\lvert F(z)\rvert$$

가 모든 holomorphic function $F$에 대해 성립하는 것을 보인다. $\Omega_\delta$의 정의로부터, $z\in\Omega_\delta$인 모든 $z$에 대해 $z$를 중심으로 하고 반지름 $\delta$인 원 $D$는 그 closure까지 $\Omega$에 포함되므로, Cauchy integral formula로부터

$$F'(z)=\frac{1}{2\pi i}\int_{\partial D}\frac{F(w)}{(w-z)^2\mathop{dw}$$

인 것을 알고 있다. 따라서

$$\lvert F'(z)\rvert\leq \frac{1}{2\pi}\left(\frac{1}{\delta^2}\sup_{w\in \Omega}\lvert F(w)\rvert\right)2\pi\delta=\frac{1}{\delta}\sup_{w\in\Omega}\lvert F(z)\rvert$$

가 성립한다. 이 부등식은 *모든* holomorphic function $F$에 대해 성립하므로, $F=f_n-f$로 두면 원하는 결과를 얻는다.  

</details>

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> Connected open subset $\Omega$와 $\Omega$ 위에서 정의된 holomorphic function $f$에 대하여, 만일 $f$의 zero set

$$Z(f)=\{z\in\Omega: f(z)=0\}$$

이 $\Omega$에서 limit point를 갖는다면 $f=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$z_0\in \Omega$가 $Z(f)$의 limit point라 하자. 그럼 $f$의 continuity에 의하여 $f(z)=0$이다. 그럼 $z_0$을 중심으로 하는 power series expansion

$$f(z)=\sum_{n=0}^\infty a_n(z-z_0)^n$$

에서, $f$가 0이 아니라면 $a_n\neq 0$이도록 하는 자연수 $n$이 존재한다. 이들 중 가장 작은 것을 $m$이라 하자. 그럼

$$f(z)=a_m(z-z_0)^m(1+g(z-z_0))$$

이라 할 수 있다. 그런데, $z_0$은 $Z(f)$의 limit point이므로 $z_0$으로 수렴하고, 모두 $z_0$과는 다른 $Z(f)$의 점들의 수열을 찾을 수 있다. 또, $z\rightarrow z_0$일 때 $g\rightarrow 0$이므로, 우리는 이 수열에서 (i) $w\in D$이고, (ii) $\lvert g(w-z_0)\rvert\leq 1$이도록 하는 점 $w\neq z_0$를 잡을 수 있다. 그럼

$$0=f(w)=a_m(w-z_0)^m(1+g(w-z_0))^m$$

인데, $w-z_0\neq 0$이고 $1+g(w-z_0)\neq 0$이므로 이는 모순이다. 따라서 $f$는 identically zero.

이제 이를 $\Omega$로 확장해야 한다. 이를 이용해 $\Omega$의 connectedness를 이용한다. 우선 $Z(f)$의 interior $U$는 앞선 argument에 의해 nonempty이고, 당연히 정의에 의해 open이다. 한편, 만일 $U$의 point들이 어떤 점 $z$로 수렴한다고 하면 (즉, $z$가 $U$의 limit point라면) $f$의 continuity에 의해 $f(z)=0$이고 따라서 다시 앞선 argument를 활용하면 $f$는 $z$의 근방에서 vanish한다. 즉, $z\in U$이고 따라서 $U$는 임의의 limit point를 포함하므로 closed이기도 하다. 이제 $U$는 nonempty clopen subset이므로, $U=\Omega$이다.

</details>

위 명제의 증명은 $f$의 power series, 그 중에서도 $f$를 

$$f(z)=a_m(z-z_0)^m(1+g(z-z_0))$$

으로 나타내는 것이 중요한 역할을 했다. 그런데, 만일 $f$가 $z_0$에서 근을 갖는다면, $z_0$을 중심으로 한 power series expansion은 항상 이런 식으로 표현될 수 있으므로, 이 상황은 꽤 흔한 상황이다. 이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> Holomorphic function $f$가 근 $z=z_0$를 갖는다고 하자. 그럼 $z_0$의 *order*는 $f^{(n)}(z)\neq 0$을 만족하는 최소의 자연수 $N$으로 정의된다. 

</div>

이를 이용하면 다음의 *maximum modulus theorem*을 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm12">**정리 12 (Maximum modulus theorem)**</ins> Connected open set $\Omega$ 위에서 정의된 non-constant holomorphic function $f$를 생각하자. 그럼 $\lvert f\rvert$는 $\Omega$ 위에서는 maximum을 가질 수 없다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $a\in\Omega$를 택하자. 우리는 어떤 $z\in \Omega$가 존재하여 $\lvert f(z)\rvert>\lvert f(a)\rvert$이도록 할 수 있다는 것을 보여야 한다. 

우선 $f(w)-f(a)$는 $w=a$에서 근을 가지므로, 이를 order $N>0$이라 하면 

$$f(w)=f(a)+c(w-a)^N+(w-a)^{N+1}h(w)$$

이라 할 수 있다. 여기에서 바로 maximum modulus theorem을 증명하는 것은 복잡하므로, 조금 머리를 써서 $w-a$가 $c$와 같은 방향, 즉 같은 argument를 갖도록 설정하자. 이를 위해 $\alpha\beta\in\mathbb{R}$을 다음의 두 식

$$f(a)=\lvert f(a)\rvert e^{i\alpha},\qquad c=\lvert c\rvert e^{i\beta}$$

을 만족하도록 잡자. 그럼 $\beta+N\theta=\alpha$이도록 하는 실수 $\theta$가 존재한다. 우선, $z=a+re^{i\theta}$에 대하여, 

$$f(a)+c(z-a)^N=\left(\lvert f(a)\rvert+\lvert c\rvert r^N\right)e^{i(\beta+N\theta)}$$

이므로 

$$\left\lvert f(a)+c(z-a)^N\right\rvert=\lvert f(a)\rvert+\lvert c\rvert r^N$$

이 성립한다. 한편, $h$는 연속이므로 $a$ 근방에서 bounded이다. Formal하게, 이를 

$$\lvert h(z)\rvert\leq M\qquad\text{if $\lvert z-a\rvert<2r$}$$

이라 하자. 그럼 $0<r'<r$인 임의의 $r'$에 대하여

$$\lvert f(z)\rvert\geq\lvert f(a)+c(z-a)^N\rvert-\lvert(z-a)^{N+1}h(z)\rvert\geq \lvert f(a)\rvert+(\lvert c\rvert-Mr')(r')^N$$

이 성립하고, $r'$을 충분히 작게 잡아 $\lvert c\rvert-Mr'>0$이도록 할 수 있으므로 증명 끝.
</details>

## Fundamental theorem of algebra

이제 남은 이야기들은 다음 글에서 하도록 하고, 잠깐 쉬어가는 시간을 갖자. 정말 뜬금없게도 우리가 지금까지 한  내용으로 다음의 *fundamental theorem of algebra*를 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13**</ins> 임의의 복소수 계수 다항식 $p(z)=a_nz^n+\cdots+a_0$은 $n$개의 근을 갖는다. 

</div>

이를 우리가 바로 증명할 수 있는 것은 아니고, 우선 Liouville's theorem을 증명해야 한다. $f$가 *entire function*이라는 것은 $f$가 $\mathbb{C}$ 전체에서 holomorphic하다는 것이다.

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14 (Liouville's theorem)**</ins> $f$가 entire고 bounded라면, $f$는 constant다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f'=0$인 것을 보이면 충분하다. 임의의 $z_0\in\mathbb{C}$와, $R>0$에 대하여 Cauchy inequality를 사용하면

$$\lvert f'(z_0)\rvert\leq\frac{B}{R}$$

이 성립한다. 이제 $R\rightarrow\infty$이면 원하는 결과를 얻는다.

</details>

Fundamental theorem of algebra의 증명은, 사실 임의의 복소수 계수 다항식이 하나의 근을 갖는다는 것만 보이면 충분하다. 나머지는 induction을 이용하면 자명하기 때문이다. Liouville's theorem을 이용하면 이를 쉽게 보일 수 있다.

<details class="proof" markdown="1">
<summary>정리 13의 증명</summary>

만일 $p$가 근을 갖지 않는다면 $1/p$가 bounded holomorphic function이 된다. Holomorphic이 된다는 것은 자명하고, boundedness를 보이려면

$$\frac{p(z)}{z^n}=a_n+\left(\frac{a_{n-1}}{z}+\cdots+\frac{a_0}{z^n}\right)$$

이 된다는 것을 확인하면 된다. 괄호 안에 있는 항들은 $z$가 커지면 어차피 0으로 가므로, $p(z)$는 $z^n$과 같은 growth를 가진다. 특히, 적당한 $R$에 대해 

$$\lvert p(z)\rvert\geq \frac{\lvert a_n\rvert}{2}R^n$$

이도록 할 수 있으며, 또 $1/p$는 어쨌든 $\lvert z\rvert\leq R$인 disc에서는 어차피 bounded이므로 결국 $1/p$는 $\mathbb{C}$ 전체에서 bounded이다. 따라서 Liouville's theorem에 의해 $1/p$는 constant여야 하고, 이는 모순이므로 원하는 결과를 얻는다. 

</details>

[^1]: 물론, 언제나 그렇듯, $\partial D$는 반시계방향의 curve이다.
[^2]: 이렇게 임의의 compact subset에 대해 수렴하는 것을 *$f_n$ converges to $f$ (uniformly) on compacta*와 같이 표현한다.
