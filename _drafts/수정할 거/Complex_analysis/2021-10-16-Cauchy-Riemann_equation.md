---

title: "Cauchy-Riemann equation"
excerpt: "Cauchy-Riemann equation and some basic formulae"

categories: [Math / Complex Analysis]
permalink: /ko/math/complex_analysis/Cauchy-Riemann_equation
header:
    overlay_image: /assets/images/Complex_analysis/Cauchy-Riemann_equation.png
    overlay_filter: 0.5
sidebar: 
    nav: "analysis"

date: 2021-10-16
last_modified_At:
weight: 1

published: false

---
<div class="notice--warning" markdown="1">

이 글은 현재 수정중입니다.

이 글은 예전에 쓴 글로, 서술 방향이 마음에 들지 않거나 표기법이 마음에 들지 않아 전체적으로 수정이 진행중입니다. 읽으실 때 참고해주세요.

</div>


## Algebraic and topological structure on $\mathbb{C}$

복소수집합 $\mathbb{C}$는 basis $\\{1,i\\}$를 갖는 $\mathbb{R}$-vector space이다. 물론, 우리는 이 집합 위에 다음의 식

$$(a+ib)(c+id)=(ac-bd)+i(ad+bc)$$

으로 정의된 곱하기가 정의된다는 것도 알고 있으므로, 사실 $\mathbb{C}$는 $\mathbb{R}$-algebra이기도 하다. 이 곱셈에 대해 살펴볼 것이 두 가지 있는데, 

- 우선 이 곱셈은 분배법칙이 성립한다. 이는 
    
    $$\begin{aligned}(a+ib)((x+iy)+(z+iw))&=(a+ib)((x+z)+i(y+w))\\&=(ax+az-by-bw)+i(bx+bz+ay+aw)\\&=((ax-by)+i(bx+ay))+((az-bw)+i(bz+aw))\\&=(a+ib)(x+iy)+(a+ib)(z+iw)\end{aligned}$$
    
    으로부터 분명하다.
- 또, $\mathbb{C}$의 곱셈은 associative, commutative하므로, 임의의 복소수 $z_1,z_2,z_3$에 대하여 
    
    $$z_1(z_2z_3)=(z_1z_2)z_3=(z_2z_1)z_3=z_2(z_1z_3)$$
    
    가 성립한다. 특히 $z_2$를 실수로 잡으면, $\mathbb{C}$의 곱셈은 실수와의 곱셈을 보존한다.
    
즉, 고정된 복소수 $z\in\mathbb{C}$에 대하여, $w\mapsto zw$으로 정의되는 $\mathbb{C}$에서 $\mathbb{C}$로의 map은 $\mathbb{R}$-linear map이다. 그럼 이 map을 나타내는 행렬이 존재하며, $(a+ib)(x+iy)=(ax-by)+i(ay+bx)$이므로

$$\begin{pmatrix}x\\y\end{pmatrix}\mapsto \begin{pmatrix}ax-by\\ ay+bx\end{pmatrix}=\begin{pmatrix}a&-b\\b&a\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}$$

으로부터 어렵지 않게 이 행렬이

$$\begin{pmatrix}a&-b\\b&a\end{pmatrix}\tag{1}$$

로 주어진다는 것을 알 수 있다. 

한편, 우리는 복소수들을 다음의 식

$$e^{i\theta}=\cos\theta+i\sin\theta$$

을 이용하여 다음과 같은 *polar form*

$$z=re^{i\theta}$$

으로 나타낼 수 있다. 여기서 $r>0$이고 $0\leq\theta&lt;2\pi$이다. 만일 $z=x+iy$였다면, $r$의 값은

$$r=\sqrt{a^2+b^2}$$

으로 결정되고, $\theta$의 값은 다음의 두 식

$$\cos\theta=\frac{a}{\sqrt{a^2+b^2}},\qquad\sin\theta=\frac{b}{\sqrt{a^2+b^2}}$$

을 만족하는 유일한 $\theta$로 결정될 것이다. 우리는 편의상 $\theta$의 범위를 $0$에서 $2\pi$까지로 고정하였기에 이 식들이 $\theta$를 유일하게 결정하지만, 사실 이 $\theta$의 값은 $2\pi$를 주기로 결정된다는 것도 눈여겨 볼 만 하다. 이 표현 상에서, $z$와 $w=se^{i\varphi}$와의 곱셈은

$$zw=(re^{i\theta})(se^{i\varphi})=(rs)e^{i\theta+i\varphi}=(rs)e^{i(\theta+\varphi)}$$

으로 주어지므로, 복소수의 곱셈은 어떤 실수에 의한 dilation을 제외하면 회전변환과 동등하기도 하다. 사실 이는 앞서 살펴본 복소수의 행렬표현 (1)에서도 예견되었던 바이기는 하다.

$\mathbb{C}$는 $\mathbb{R}$-vector space로써 뿐만이 아니라, topology 측면에서도 $\mathbb{R}^2$와 동일하다. $\mathbb{C}$ 위의 metric

$$\lvert(a+ib)-(c+id)\rvert=\lvert(a-c)+i(b-d)\rvert=\sqrt{(a-c)^2+(b-d)^2}$$

이 $\mathbb{R}^2$ 위에 정의된 Euclidean metric과 동일하므로, $\mathbb{C}$ 위의 metric topology 또한 그러하다. 따라서, 위상수학의 많은 정리들, 예를 들면 Heine-Borel 정리 등을 복소수에서도 자유롭게 사용할 수 있다. 

한편, $\mathbb{C}$는 자연스러운 *원점*, 즉 $0$을 가지므로, 위에서 정의한 metric $\lvert\;\cdot\;\rvert$를 이용하여 $\mathbb{C}$ 위의 norm을

$$\lvert z\rvert=\sqrt{x^2+y^2},\qquad z=x+iy$$

으로 정의하는 것도 타당하다. 그럼 우리는 앞서 살펴본 polar form에서의 $r$이 별다른 것이 아니라 복소수의 절댓값이라는 것을 알게 된다. 이 norm은 당연히 triangle inequality

$$\lvert z+w\rvert\leq\lvert z\rvert+\lvert w\rvert$$

를 만족시키며, 마찬가지로 reverse triangle inequality

$$\lvert\lvert z\rvert-\lvert w\rvert\rvert\leq\lvert z-w\rvert$$

도 만족시킨다. 또 우리는 임의의 $z\in\mathbb{C}$에 대하여, $z=x+iy$의 *실수부*와 *허수부*를 각각 $\Re(z)=x$와 $\Im(z)=y$로 정의한다. 그럼 특히 $\lvert\Re(z)\rvert\leq\lvert z\rvert$이고 $\lvert\Im(z)\rvert\leq\lvert z\rvert$이다. 

우리는 앞서 $\mathbb{C}$가 $\mathbb{R}^2$과 topological하게 동일하다는 것을 살펴봤는데, 그럼 $\Re$와 $\Im$ 각각은 별다른 것이 아니고 product topology가 주어졌을 때 첫 번째와 두 번째 factor로의 projection map들이다. 따라서 복소수에 정의된 Euclidean metric에서, 예를 들어 복소수열의 수렴은 실수부와 허수부 각각이 실수열로서 수렴하는 것으로 정의되고, 함수의 연속성도 마찬가지가 된다. 뿐만 아니라, 만일 우리가 복소함수 $f:\mathbb{C}\rightarrow\mathbb{C}$를 생각한다면, $f$에 절댓값을 취한 함수 $\lvert f\rvert: z\mapsto \lvert f(z)\rvert$는 $\mathbb{C}$에서 $\mathbb{R}$로의 함수이므로, 우리가 위상수학에서 다뤘던 정리, extreme value theorem을 이용하면 연속함수 $f$와, 복소수 집합의 compact subset $\Omega$에 대하여 $f$는 $\Omega$ 위에서 bounded되어있고, minimum과 maximum을 갖는다는 것을 알 수 있다.

## Differentiability in $\mathbb{C}$

우리는 방금까지 $\mathbb{C}$가 $\mathbb{R}$과 동일한 부분을 살펴봤다. 하지만, 만일 복소수집합이 *정말로* $\mathbb{R}^2$과 동일했다면, 수학자들이 복소수를 탐구하기 위해 이런저런 도구를 개발할 필요도 없었을 것이다.

복소수가 $\mathbb{R}^2$과 다른 점은 미분에서부터 나온다. 함수 $f:\mathbb{C}\rightarrow\mathbb{C}$가 주어졌다 하자. 우리는 $\mathbb{C}$ 위의 metric topology를 이용하여 다음의 극한 

$$\lim_{h\rightarrow 0}\frac{f(z_0+h)-f(z_0)}{h}$$

을 생각할 수 있다. 그렇다면, 위의 극한이 존재할 경우 $f$를 $z_0\in\mathbb{C}$에서 미분가능하다고 하고, 그 값 $f'(z_0)$를 위의 식으로 정의하는 것이 당연할 것이다. 우리는 종종 이 정의를 multivariable과의 연결성을 위해 다음의 식 

$$\lim_{h\rightarrow 0}\frac{\lvert f(z_0+h)-f(z_0)-f'(z_0)h\rvert}{h}$$

으로 쓰기도 했었다. 한편, $f$를 $\mathbb{R}^2$에서 $\mathbb{R}^2$로의 map으로 생각할 경우, $f$의 미분은

$$\lim_{h\rightarrow 0}\frac{\lvert f(z_0+h)-f(z_0)-(Df)h\rvert}{h}=0$$

을 만족하는 $\mathbb{R}$-linear operator $Df:\mathbb{R}^2\rightarrow\mathbb{R}^2$로 정의된다. 우리는 $\mathbb{C}$에 주어진 algebraic structure를 살펴보며 $\mathbb{C}$에서 $\mathbb{C}$로의 함수 $w\mapsto zw$가 항상 $\mathbb{R}$-linear라는 것을 살펴보았는데, 이에 따르면 특히 $h\mapsto f'(z_0)h$ 또한 $\mathbb{R}$-linear이고 따라서 우리는 $\mathbb{C}$에서 differentiable한 함수 $f:\mathbb{C}\rightarrow\mathbb{C}$는 $\mathbb{R}^2$에서 $\mathbb{R}^2$로의 함수로 보더라도 differentiable하다는 것을 알 수 있다. 그러나, 일반적으로 그 역은 성립하지 않는다. 

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 함수 $f:\mathbb{C}\rightarrow\mathbb{C}$를 *conjugate map* $z\mapsto \overline{z}$로 정의하자. 즉, $f$는

$$x+iy\mapsto x-iy$$

을 통해 정의되는 함수이다. 그럼 $f$는 $\mathbb{C}$에서는 differentiable하지 않다. $h$가 purely imaginary일 경우, 우리는

$$\lim_{h\rightarrow 0}\frac{\overline{h}}{h}=\lim_{y\rightarrow 0}\frac{-iy}{iy}=-1$$

을 얻지만, $h$가 real인 경우

$$\lim_{h\rightarrow 0}\frac{\overline{h}}{h}=\lim_{x\rightarrow 0}\frac{x}{x}=1$$

을 얻기 때문이다. 그러나, $\mathbb{R}^2$에서 $\mathbb{R}^2$로의 함수 $f(x,y)=(x,-y)$는 differentiable하다. $f$ 자체가 linear map이므로, 계산할 것도 없이 $Df$도 linear map

$$\begin{pmatrix}x\\y\end{pmatrix}\mapsto\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}$$

으로 주어지며, 따라서 $f$는 differentiable하기 때문이다.

</div>

더 일반적으로, 만약 differentiable function $f:(x,y)\mapsto (u(x,y), v(x,y))$가 주어졌고, $u$, $v$가 각각 differentiable하다면 우리는 $Df$가 다음의 식

$$\begin{pmatrix}\partial u/\partial x&\partial u/\partial y\\\partial v/\partial x&\partial v/\partial y\end{pmatrix}$$

으로 주어진다는 것을 알고 있다. 이러한 관점에서, 일반적으로 앞선 [예시 1](#ex1)과 같은 일이 벌어지는 것은 당연하다. $f$의 Jacobian matrix가 항상 어떤 complex number를 나타낼 필요는 없기 때문이다. 언제 Jacobian matrix가 complex number 하나를 지정할지를 생각해보면 다음 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Complex plane $\mathbb{C}$의 어떤 open subset $\Omega$ 위에서 정의된 함수 $f=u+iv$를 생각하자. 그럼 $f$가 $\mathbb{C}$에서 differentiable할 조건은 $u,v$ 각각이 differentiable하고, 이들이 다음의 *Cauchy-Riemann equation*

$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$

를 만족하는 것과 동치이다. 

</div>

앞으로의 이야기에서, differentiabiliy의 개념이 서로 혼동되지 않도록, 우리는 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 어떤 함수 $f:\mathbb{C}\rightarrow\mathbb{C}$가 $z_0\in\mathbb{C}$에서 *holomorphic*하다는 것은, $z_0$의 어떤 neighborhood $\Omega$가 존재하여, $\Omega$ 안에서 다음의 극한

$$\lim_{h\rightarrow 0}\frac{f(z_0+h)-f(z_0)}{h}$$

이 존재하는 것이다. 이 때의 극한값을 $f'(z_0)$으로 표기한다.

</div>

우리는 앞선 논의에서, holomorphic function은 단순히 $\mathbb{R}^2$에서 $\mathbb{R}^2$로의 differentiable function이 아니라는 것을 지적했었다. 실제로, 우리가 방금 정의한 holomorphic function은 differentiable function보다 훨씬 강력한 조건이 된다는 것을 앞으로 계속 살펴볼 것이다. 예컨대, 일반적인 real-valued differentiable function은 power series를 가질 필요가 없고, power series를 갖더라도 이것이 원래의 함수와 동일할 필요가 없다. 그러나, holomorphic function은 infinitely differentiable하다. 이러한 결과들을 보이기 위해서는 $\mathbb{C}$ 위에서의 선적분을 정의해야 한다.

## Integration along the curve

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 함수 $\gamma:[a,b]\rightarrow\mathbb{C}$가 *piecewise-smooth curve*라는 것은 $\gamma$가 $[a,b]$ 위에서 continuous하고, 적당한 point들

$$a=p_0<p_1<\cdots<p_n=b$$

가 존재하여 $\gamma(t)$가 각각의 interval들 $[p_k, p_{k+1}]$에서 continuously differentiable한 것이다.  

</div>

우리는 앞으로 piecewise-smooth curve만 다룰 예정이므로, 이들을 그냥 간단히 curve라 부르기로 한다. 이렇게 piecewise smooth curve $\gamma$가 주어졌을 때, 우리는 늘상 하던 것처럼 선적분을 다음의 식

$$\int_\gamma f(z)\mathop{dz}=\int_a^b f(z(t))z'(t)\mathop{dt}$$

로 정의한다. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> Curve $\gamma:[a,b]\rightarrow\mathbb{C}$에 대하여, 다음이 성립한다.

1. $\alpha,\beta\in\mathbb{C}$에 대하여 $\int_\gamma (\alpha f(z)+\beta g(z))\mathop{dz}=\alpha\int_\gamma f(z)\mathop{dz}+\beta\int_\gamma g(z)\mathop{dz}$,
2. $\int_\gamma f(z)\mathop{dz}=-\int_{\gamma^-}f(z)\mathop{dz}$, $\gamma^{-1}$은 $\gamma$의 반대 방향 reparametrization
3. $\left\lvert\int_\gamma f(z)\mathop{dz}\right\rvert\leq\sup\lvert f(z)\rvert\operatorname{length}(\gamma)$.

</div>

우리는 앞서 holomorphic function이 differentiable function보다 훨씬 강력한 조건이라는 것을 이야기하며, 그 예시로 holomorphic function은 infinitely differentiable하다는 것을 들었다. 이 증명은 복소해석학의 첫 번째 목표인 Cauchy's theorem에 의존한다. 다음 명제는 그 맛보기.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 어떤 연속함수 $f$가 open set $\Omega$ 안에서 primitive $F$를 갖는다 하자. 만일 $\gamma$가 $\Omega$ 안에 포함된 curve라면, 그 양 끝점 $w_1$과 $w_2$에 대하여, 다음의 식

$$\int_\gamma f(z)\mathop{dz}=F(w_2)-F(w_1)$$

이 성립한다. 

</div>

만일 $w_1=w_2$라면, 즉 $\gamma$가 closed curve라면, 위 가정 하에서 적분값은 항상 0이 될 것이다. Cauchy's theorem은 여기에서 더 나아가, 적당한[^1] open set $\Omega$에서 정의된 *모든* holomorphic function이 primitive를 가지고, 따라서 위의 식이 성립한다는 정리이다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 하지만 이것이 항상 성립하는 것은 아니다. 예를 들어, open set $V=\mathbb{C}\setminus\\{0\\}$과 $f(z)=1/z$를 생각하자. 그럼 예를 들어, $\gamma$를 다음의 식

$$\gamma(t)=e^{2\pi i t}$$

으로 정의하면 (물론 $t\in [0,1]$이다), 

$$\int_\gamma f(z)\mathop{dz}=\int_0^1 f(\gamma(t))\gamma'(t)\mathop{dt}=\int_0^1\frac{2\pi i e^{2\pi i t}}{e^{2\pi i t}}\mathop{dt}=\int_0^1 2\pi i \mathop{dt}=2\pi i$$

가 되어 위의 식이 성립하지 않는다. 따라서 $f$는 $V$에서 primitive를 갖지 않는다.

</div>

이 예시는 앞으로 끊임없이 변주되며 나올 것이다.

## Power series

마지막으로 power series에 대해 살짝 리뷰해보자. 실수에서의 경우와 마찬가지로, 복소수에서도 modulus를 취해서 생각해보면 다음 정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> Power series $\sum_{n=0}^\infty a_nz^n$에 대하여, 적당한 $0\leq R\leq\infty$가 존재하여 $\lvert z\rvert&lt;R$에서는 series가 절대수렴하고, $\lvert z\rvert&gt;R$에서는 발산하도록 할 수 있다. 이 때 $R$은 다음의 식

$$R=\limsup\lvert a_n\rvert^{-1/n}$$

으로 주어진다.
</div>

또, power series

$$f(z)=\sum_{n=0}^\infty a_nz^{n}$$

가 주어졌다면, 그 도함수 또한 다음의 식

$$f'(z)=\sum_{n=0}^\infty na_nz^{n-1}$$

과 같이 power series로 정의되며, 또 이 때 도함수의 radius of convergence는 원래 함수의 그것과 동일하다. 여기에서 도함수에는 어떠한 가정도 걸리지 않으므로, induction을 통해

> Power series로 표현되는 임의의 함수는 무한 번 미분 가능하다

는 것을 알 수 있다. 그러나, 일반적으로 실함수에서는 이렇게 얻어지는 power series가 원래의 함수와 같다는 보장도 없다. 예를 들어, 다음의 식

$$f(x)=\begin{cases}e^{-1/x^2}&x>0\\0&x\leq 0\end{cases}$$

으로 정의된 함수 $f$는 무한 번 미분가능하지만, $f$의 임의의 도함수가 항상 vanish하기 때문에 $x=0$에서의 power series는 0이 된다. 반면, 우리는 다음 글에서

> 임의의 holomorphic function은 무한 번 미분가능하며, 이를 통해 얻어지는 power series는 원래의 함수와 동일하다

는 것을 증명할 수 있다. 

[^1]: 이 *적당한* open set 또한 Cauchy's theorem의 전제조건이다. 이 정리는 아무 open set에 대해서만 성립하는 것은 아니다.
