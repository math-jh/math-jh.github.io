---

title: "접속"
excerpt: "Vector bundle 위에서 정의된 미분"

categories: [Math / Manifold]
permalink: /ko/math/manifold/connection
header:
    overlay_image: /assets/images/Manifold/Connection.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 13

---

## 접속과 공변미분

Lie derivative를 이용하면 벡터장이나 differential form을 미분할 수 있지만, 이 개념을 임의의 vector bundle $\pi:E\rightarrow M$의 section $\Gamma(E)$로 확장하는 것은 불가능하다. Tangent bundle $TM$ 위에서는 integral flow $\phi$ 위의 두 점 $p,q$가 주어졌을 때, 두 tangent space $T_pM$과 $T_qM$을 잇는 자연스러운 isomorphism $d\phi^{-t}$가 존재했지만, 임의의 vector bundle $E$의 두 fiber $E_p$와 $E_q$ 사이에는 이러한 함수가 존재하지 않기 때문이다. 따라서 우리는 이들 fiber들을 <em_ko>이어주는</em_ko> *connection*이라는 것을 추가로 정의한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Manifold $M$ 위에 정의된 vector bundle $E\rightarrow M$에 대하여, $E$ 위에서 정의된 *connection<sub>접속</sub>* $\nabla:\mathfrak{X}(M)\times\Gamma(E)\rightarrow\Gamma(E)$는 다음 조건들을 만족하는 함수이다.

1. (Tensoriality) $\nabla_XY$는 첫째 성분에 대하여 $C^\infty$-linear이다.
2. (Linearity) $\nabla_XY$는 둘째 성분에 대하여 $\mathbb{R}$-linear이다.
3. 임의의 $f\in C^\infty(M)$에 대하여, $\nabla$는 다음의 라이프니츠 법칙 
    
    $$\nabla_X(fY)=f\nabla_XY+(Xf)Y$$

    을 만족한다.

</div>

이 때, $\nabla_XY$를 *$Y$의 $X$방향으로의 covariant derivative<sub>공변미분</sub>*라 부르기도 한다. 다음 명제는 $(\nabla_XY)_p$를 계산하기 위해서는 $p$ 근방에서의 $X$와 $Y$만 알면 충분하다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Manifold $M$이 주어졌다 하고, $X\in\mathfrak{X}(M)$, $Y\in\Gamma(E)$라 하자. 임의의 점 $p\in M$에 대하여, $(\nabla_XY)_p$는 

1. 점 $p$에서의 벡터장 $X$의 값 $X_p$,
2. 점 $p$의 열린근방에서의 벡터장 $Y\vert_U$

에만 의존한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $(\nabla_XY)_p$가 점 $p$의 열린근방 $U$에서의 벡터장에만 의존한다는 것을 보이자. 두 벡터장 $Y_1,Y_2$가 $p$의 열린근방 $U$에서 같다면 $(\nabla_XY_1)_p=(\nabla_XY_2)_p$임을 보여야 하므로, 이를 위해서는 벡터장 $Y$가 열린근방 $U$의 모든 점에서 항등적으로 $0$이라면 $(\nabla_XY)_p$가 $0$임을 보이면 충분하다. $\varphi$를 $\supp(\varphi)\subseteq U$, $\varphi(p)=1$을 만족하는 bump function이라 하면 벡터장 $\varphi Y$는 $M$ 전체에서 항등적으로 $0$이다. 따라서 [정의 1](#df1)의 둘째 조건으로부터 $\nabla_X(\varphi Y)=0$이다. 한편 라이프니츠 법칙에 의해,

$$0=\nabla_X(\varphi Y)=\varphi\nabla_XY+(X\varphi)Y$$

이고, 우번을 점 $p$에서 계산하면

$$\varphi(p)(\nabla_XY)_p+(X\varphi)(p)Y_p=(\nabla_XY)_p$$

이므로 $(\nabla_XY)_p=0$이다.

이제 $\nabla_XY$가 점 $p$에서의 벡터 $X_p$에만 의존한다는 것을 보인다. 이를 위해서는 위와 마찬가지로 $X_p=0$을 가정하고 $0=(\nabla_XY)_p$임을 보이면 충분하다. 점 $p$ 근방에서의 coordinate chart $(U,(x^i))$를 잡고, $X$를 이 좌표계에 대하여

$$X=X^1\frac{\partial}{\partial x^1}+\cdots+X^n\frac{\partial}{\partial x^n}$$

과 같이 쓰자. 그럼

$$(\nabla_XY)_p=(\nabla_{\sum X^i\frac{\partial}{\partial x^i}}Y)_p=\left(\sum_{i=1}^n X^i\nabla_{\partial/\partial x^i} Y\right)_p$$

이고, 모든 $i$에 대하여 $X^i(p)=0$이므로 원하는 결과를 얻는다.

</details>

## Tangent bundle 위에서의 공변미분

특별히 tangent bundle $TM\rightarrow M$ 위에서 정의된 connection을 살펴보자. 그럼 $\nabla$는 $\mathfrak{X}(M)\times\mathfrak{X}(M)$에서 $\mathfrak{X}(M)$으로의 함수이다. 주의할 것은 Lie derivative와 connection은 모두 미분을 생각하기 위한 개념들이지만 서로 다른 결과를 갖는다는 것이다. 예컨대 Lie derivative에서는

$$\mathcal{L}_{fX}Y=[fX,Y]=fX(Y)-Y(fX)=fX(Y)-(Yf)X-fY(X)=f[X,Y]-(Yf)X=f\mathcal{L}_XY-(Yf)X$$

이지만, 정의에 의하여

$$\nabla_{fX}Y=f\nabla_XY$$

이므로 $Y$와 $f$를 잘 택하여 $\nabla_{fX}Y\neq\mathcal{L}_{fX}Y$이도록 하는 것이 항상 가능하다.

어쨌든 $TM$ 위에서 정의된 connection을 생각하면, [명제 2](#pp2)에 의하여 점 $p$에서의 $\nabla_XY$의 값은 $p$ 근방에서의 local frame $(E_i)$들에 의해 완전히 결정된다. 이는

$$(\nabla_XY)_p=\nabla_{\sum X^i(p)E_i(p)}\left(\sum Y^i(p)E_i(p)\right)$$

이 성립하기 때문이다. 한편

$$\nabla_X\left(\sum_{j=1}^n Y^jE_j\right)=\sum_{j=1}^n \nabla_X(Y^jE_j)=\sum_{j=1}^n\left(Y^j\nabla_XE_j+X(Y^j)E_j\right)=\sum_{i,j=1}^nX^iY^j\nabla_{E_i}E_j+\sum_{j=1}^n X(Y^j)E_j\tag{1}$$

이므로, $\nabla_XY$는 $n^2$개의 벡터장 $\nabla_{E_i}E_j$으로 완전하게 결정된다. 다시 벡터장 $\nabla_{E_i}E_j$를 $E_k$들의 일차결합으로 나타내면

$$\nabla_{E_i}E_j=\Gamma_{ij}^k E_k$$

을 만족하는 $n^3$개의 $C^\infty$-함수들 $\Gamma\_{ij}^k$가 존재한다. 그럼 위의 식 (1)은

$$\nabla_XY=\sum_{k=1}^n\left(\sum_{i,j=1}^nX(Y^k)+X^iY^j\Gamma_{ij}^k\right)E_k$$

으로 쓸 수 있다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위에서 정의한 $n^3$개의 함수 $\Gamma_{ij}^k$를 *connection coefficient<sub>접속 계수</sub>*이라 부른다.

</div>

한편, 임의의 manifold $M$위의 tangent bundle은 항상 connection을 갖는다. 이를 확인하기 위해서는 Riemannian metric 때와 마찬가지로, 유클리드 공간에서의 connection

$$\nabla_vY:=v(Y^1)\frac{\partial}{\partial x^i}+\cdots+v(Y^n)\frac{\partial}{\partial x^n}$$

을 partition of unity를 통해 이어붙이면 된다.

## Cotangent bundle 위에서의 공변미분

우리는 tangent bundle $TM$ 위에 정의된 connection $\nabla$가 임의의 $(r,s)$-tensor field $\mathcal{T}^{r,s}(M)$로 잘 확장된다는 것을 보인다. ([]()) 이를 위해서는 우선 $\nabla$가 cotangent bundle $T^\ast M$ 위에서는 어떻게 확장되는지를 정해줘야 한다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> Manifold $M$과, tangent bundle $TM$ 위의 connection $\nabla$가 주어졌다 하자. 함수 $\nabla^\ast:\mathfrak{X}(M)\times\Gamma(T^\ast M)\rightarrow\Gamma(T^\ast M)$을 다음의 식

$$(\nabla_X^\ast\alpha)_p(Y)=X\bigl(\alpha(Y)\bigr)-\alpha_p\bigl(\nabla_XY\bigr)_p$$

으로 정하면, $\nabla^\ast$는 $T^\ast M$ 위의 connection이 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 우변의 식으로 정의된 $\nabla^\ast\alpha$가 $1$-form이라는 것을 보일 수 있으므로 $\nabla^\ast$의 공역에는 문제가 없다.

$\nabla^\ast$가 실제로 connection의 조건을 만족한다는 사실은 라이프니츠 법칙 이외에는 자명하다. 사실 라이프니츠 법칙 또한

$$\begin{aligned}(\nabla_X^\ast f\alpha)_pY&=X(f\cdot\alpha(Y))-(f\alpha)_p(\nabla_XY)_p\\&=(Xf)(\alpha(Y))+f(p)\bigl(X(\alpha(Y))-\alpha_p(\nabla_XY)_p\bigr)\\&=\bigl((Xf)\alpha+f\nabla_X\alpha\bigr)Y\end{aligned}$$

으로부터 자명하다.

</details>

약간의 abuse of notation을 통해, 위에서 정의한 $\nabla^\ast$도 마찬가지로 $\nabla$로 적는다.

## Tensor field 위에서의 공변미분

이제 드디어 $TM$의 connection을 $(r,s)$-tensor field $\mathcal{T}^{r,s}(M)$으로 확장할 수 있다. 위에서와 마찬가지로, 이렇게 정의한 connection 역시 $\nabla$로 적기로 한다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> Tangent bundle $TM\rightarrow M$ 위에 정의된 connection $\nabla$가 주어졌다 하자. 그럼 $\nabla$를 모든 tensor field $\mathcal{T}^{r,s}(M)$들 위에 다음 두 조건

$$\nabla_X(F\otimes G)=(\nabla_X F)\otimes G+F\otimes(\nabla_XG),\qquad\nabla_X(F+G)=\nabla_XF+\nabla_XG$$

을 만족하도록 확장할 수 있으며, 추가로 $\mathcal{T}^{0,0}M$에서 $\nabla_Xf=Xf$이도록 하는 확장이 유일하게 결정된다.

</div>

임의의 $(r,s)$-tensor $F$는 다음의 linear map

$$\underbrace{\Omega^1(M)\times\cdots\times \Omega^1(M)}_\text{\small $r$ times}\times\underbrace{\mathfrak{X}(M)\times\cdots\times \mathfrak{X}(M)}_\text{\small $s$ times}\rightarrow C^\infty(M)$$

과 동일하게 취급할 수 있으므로, $\nabla_XF$는 $\omega^1,\ldots,\omega^r\in\Omega^1(M)$, $Y_1,\ldots, Y_s\in\mathfrak{X}(M)$에서의 함수값으로 유일하게 결정된다. 가령, simple tensor $F=X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\otimes\alpha^s\in\mathcal{T}^{r,s}(M)$에 대해 라이프니츠 법칙을 적용하면

$$\begin{aligned}\nabla_X(X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\otimes\alpha^s)&=(\nabla_XX_1)\otimes X_2\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\cdots\alpha^s\\
&\phantom{=aa}+\cdots\\
&\phantom{=aaaa}+X_1\otimes X_2\otimes\cdots\otimes(\nabla_XX_r)\otimes\alpha^1\otimes\cdots\otimes\alpha^s\\
&\phantom{=aaaaaa}+X_1\otimes\cdots X_r\otimes(\nabla_X\alpha^1)\otimes\alpha^2\otimes\cdots\otimes\alpha^s\\
&\phantom{=aaaaaaaa}+\cdots\\
&\phantom{=aaaaaaaaaa}+X_1\otimes\cdots\otimes X_r\otimes\alpha^1\otimes\alpha^2\otimes\cdots\otimes(\nabla_X\alpha^s)\end{aligned}$$

을 얻으므로, $\omega^1,\ldots,\omega^r\in\Omega^1(M)$, $Y_1,\ldots, Y_s\in\mathfrak{X}(M)$에서 $\nabla_XF$의 값을 계산하면 그 값은

$$\sum_{i=1}^r\omega^1(X_1)\omega^2(X_2)\cdots\omega^i(\nabla_XX_i)\cdots\omega^r(X_r)\alpha^1(Y_1)\cdots\alpha^s(Y_s)+\sum_{j=1}^s\omega^1(X_1)\cdots\omega^r(X_r)\left(X(\alpha^j(Y^j))-\alpha^j(\nabla_XY^j)\right)$$

이고, 우변의 첫째 합을

$$\omega^i(\nabla_XX_i)=X(\omega^i(X_i))-(\nabla_X\omega^i)(X_i)$$

을 통해 바꾸어주면 다음의 식

$$\begin{aligned}\nabla_XF(\omega_1,\ldots,\omega^r,Y_1,\ldots, Y_s)&=X(F(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s))\\
&\phantom{=aa}-\sum_{i=1}^r F(\omega^1,\ldots,\nabla_X\omega^i,\ldots,\omega^r,Y_1,\ldots, Y_s)\\
&\phantom{=aaaa}-\sum_{j=1}^s F(\omega^1,\ldots, \omega^r,Y_1,\ldots, \nabla_XY_j,\ldots, Y_s)\end{aligned}$$

을 얻는다. 이 식은 simple $(r,s)$-tensor에 대해서 모두 성립하므로 모든 $(r,s)$-tensor에 대해서도 성립한다. 이제 이렇게 정의된 $\nabla$가 원하는 조건을 만족하고, 조건 $\nabla_Xf=Xf$에 의해 유일하게 결정된다는 것은 단순한 계산의 결과이다.

## Total connection

위에서 정의한 $\mathcal{T}^{r,s}(M)$ 위에서의 connection $\nabla$를 생각하자. 임의의 $(r,s)$-tensor $F$에 대하여, $\nabla F$는 $r$개의 $1$-form들 $\omega^1,\ldots,\omega^r$과 $s+1$개의 벡터장들 $Y_1,\ldots, Y_s, X$를 받아 $C^\infty(M)$ 함수

$$(\nabla_XF)(\omega^1,\ldots,\omega^r,Y_1,\ldots, Y_s)$$

을 내놓는 $(r,s+1)$-tensor $\nabla F$로 생각할 수 있다.

특히 $(0,0)$-tensor, 즉 $C^\infty$ 함수 $f$에 $\nabla$를 적용하면 $(0,1)$-tensor $\nabla f$를 얻는다. 정의에 의하여 covector $\nabla f$는 다음의 식

$$X\mapsto \nabla_Xf=Xf$$

으로 정의된다. 한편, $M=\mathbb{R}^m$으로 두고 [§리만 계량, §§Musical isomorphism](/ko/math/manifold/Riemannian_metric#musical-isomorphism)에서와 같이 함수 $f$의 그라디언트 벡터 $\operatorname{grad} f$를 다음의 식

$$X\mapsto \langle X, \operatorname{grad} f\rangle$$

으로 정의된 covector로 본다면, 그라디언트 벡터의 성질에 의하여 $\langle X,\operatorname{grad} f\rangle=Xf$임을 알 수 있다. 이로부터 기존에 그라디언트 벡터를 표기할 때 $\nabla f$로 표기하기도 하는 것이 설명된다. 이를 일반적인 manifold에서 다루기 위해서는 필연적으로 Riemannian metric을 가져와야 하므로 자세한 내용은 다음 글에서 다루기로 한다.

이제 *second covariant derivative<sub>이계 공변미분</sub>* $\nabla_{X,Y}^2 F$는 다음의 식

$$\nabla_{X,Y}^2F(\ldots)=(\nabla^2 F)(\cdots, Y,X)$$

을 만족하는 $(r,s)$-tenor $\nabla_{X,Y}^2F$으로 정의된다. 이렇게 정의된 $\nabla_{X,Y}^2F$는 $Y$에 대하여 $C^\infty(M)$-linear이지만, $\nabla_X\nabla_Y$는 $Y$에 대하여 $C^\infty$-linear가 아니므로 일반적으로 $\nabla_{X,Y}^2\neq\nabla_X\nabla_Y$이다. 그러나 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 임의의 $(r,s)$-tensor $F$에 대하여,

$$\nabla_{X,Y}^2F=\nabla_X(\nabla_YF)-\nabla_{\nabla_XY}F$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우변에 $(\omega^1,\ldots,\omega^r,Z_1,\ldots,Z_s)$를 넣어보면 된다.

</details>

특히 $(0,0)$-tensor $C^\infty(M)$에 이를 적용하면 *covariant Hessian* $\nabla^2 u$를 얻는다. 