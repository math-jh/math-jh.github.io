---

title: "리 군"
excerpt: "Lie group의 정의와 성질"

categories: [Math / Manifold]
permalink: /ko/math/manifold/Lie_groups
header:
    overlay_image: /assets/images/Math/Manifold/Lie_groups.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-01-23
last_modified_at: 2023-01-23
weight: 19

---

[§리 미분, ⁋명제 4](/ko/math/manifold/Lie_derivative#pp4)에서 우리는 주어진 벡터장 $X$ 방향으로의 벡터장 $Y$의 미분 

$$\mathcal{L}_XY=\lim_{t\rightarrow 0}\frac{(d\phi^{-t})_{\phi^t(p)}(Y_{\phi^t(p)})-Y_p}{t}$$

를 정의했으며, 그 값이 Lie bracket $[X,Y]$와 같다는 것을 살펴봤다. 한편, 벡터장 $X,Y$에 대하여, 다음의 식

$$(XY)f=X(Yf)$$

으로 정의된 연산자 $XY$는 라이프니츠 법칙을 만족하지 않고 따라서 $XY\not\in\mathfrak{X}(M)$이므로, 이와 같은 곱셈에 대하여 $\mathfrak{X}(M)$은 $C^\infty(M)$-algebra가 되지 않았다. 반면 $[X,Y]\in\mathfrak{X}(M)$이므로, $[-,-]$을 $\mathfrak{X}(M)$의 곱셈으로 삼으면 이를 $C^\infty(M)$-algebra로 생각할 수 있다. 이러한 구조를 *Lie algebra<sub>리 대수</sub>*라 부른다. 

이번 글에서 우리의 목표는 리 대수와 리 군에 대한 정의를 내리고, 이들의 성질을 간단하게 살펴보는 것이다.

## 리 군

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Group $G$가 *Lie group<sub>리 군</sub>*이라는 것은 $G$가 그 자체로 manifold 구조를 가지고 있으며, 이 manifold 구조에 대하여 다음의 함수

$$G\times G\rightarrow G;\qquad (x,y)\mapsto xy^{-1}$$

가 $C^\infty$인 것이다. 

</div>

위와 같이, 특별한 경우를 제외하고는 대수학에서의 표기를 따라 $G$의 항등원은 $e$로, $G$에서의 연산은 $xy$와 같이 표기한다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> Lie group은 우리가 이미 알고 있는 많은 예시들을 포함하는 개념이다.

1. $\mathbb{R}^n$에 덧셈구조를 주면 $\mathbb{R}^n$은 Lie group이 된다. 이는 $(\mathbf{x},\mathbf{y})\mapsto \mathbf{x}-\mathbf{y}$으로 정의된 연산 $\mathbb{R}^n\times\mathbb{R}^n\rightarrow\mathbb{R}^n$이 $C^\infty$이기 때문이다.
2. 두 Lie group $G,H$에 대하여, $G\times H$ 또한 Lie group이 된다. 
3. $\GL_n(\mathbb{R})$의 곱셈, 그리고 역원은 (분모가 $0$이 되지 않는) 유리함수에 불과하므로 $C^\infty$이고, 따라서 $\GL_n(\mathbb{R})$ 또한 Lie group이다. $\SL_n(\mathbb{R})$ 또한 마찬가지이다.

</div>

## 리 대수

리 군이 정의되면, 이 위에 정의된 자연스러운 리 대수의 구조가 존재한다. 이를 위해서는 우선 리 대수가 무엇인지를 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $\mathbb{R}$-벡터공간 $\mathfrak{g}$가 $\mathbb{R}$ 위에 정의된 *Lie algebra<sub>리 대수</sub>*라는 것은 이 위에 다음의 두 조건

1. (anticommutativity) $[x,y]=-[y,x]$,
2. (Jacobi identity) $[[x,y],z]+[[y,z],x]+[[z,x],y]=0$

을 만족하는 *Lie bracket<sub>리 브라켓</sub>* $[-,-]:\mathfrak{g}\times\mathfrak{g}\rightarrow\mathfrak{g}$가 정의된 것이다.

</div>

이 정의는 사실 이전에 이미 살펴본 적이 있다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 manifold $M$이 주어졌을 때, 그 위에 정의된 벡터장들의 모임 $\mathfrak{X}(M)$은 [§리 미분, ⁋정의 5](/ko/math/manifold/Lie_derivative#df5)에서 정의된 연산 $[-,-]:\mathfrak{X}(M)\times\mathfrak{X}(M)\rightarrow\mathfrak{X}(M)$를 bracket으로 하는 Lie algebra를 이룬다.

</div>

## 리 군과 리 대수

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Lie group $G$와, $G$의 임의의 원소 $g\in G$에 대하여, $g$에 의한 *left translation* $L_g$는

$$L_g:G\rightarrow G;\qquad x\mapsto gx$$

으로 정의된 $C^\infty$ 함수이다. 비슷하게, right translation $R_g$는

$$R_g:G\rightarrow G;\qquad x\mapsto xg$$

으로 정의된다.

</div>

Lie group $G$ 위에 정의된 벡터장 $X$에 대하여, $X$가 *left invariant*라는 것은 $X$가 자기 자신과 $L_g$-related인 것이다. 즉, 다음의 식

$$d(L_g)\circ X=X\circ L_g$$

이 성립하는 것이며, 더 명시적으로는 임의의 $p\in G$에 대하여

$$\left(d(L_g)\right)(X_p)=X_{gp}$$

이 항상 성립하는 것이다.

위의 식으로부터, $G$ 위에 정의된 left invariant인 벡터장 $X$를 명시하기 위해서는 <em_ko>오직 하나의 점</em_ko> $p\in G$에서의 값 $X_p$만 알면 충분하다는 것을 알 수 있으며, 당연하게도 가장 평범한 $p$의 선택은 $G$의 항등원 $e$이다. 또, 각 점에서의 $X$의 값이 이러한 방식으로 정의되었기 때문에, $X$가 left-invariant라는 사실이 $X$의 smoothness를 줄 것이라는 것도 추측할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> Lie group $G$가 주어졌다 하고, $\mathfrak{g}$를 $G$ 위에서 정의된 모든 left invariant vector field들의 모임이라 하자. 

1. $\mathfrak{g}$는 $\mathbb{R}$-벡터공간이며, $\alpha:\mathfrak{g} \rightarrow T_eG$ 를 다음의 식
     
    $$\alpha(X)=X_e$$
    
    으로 정의하면 $\alpha$는 isomorphism이 된다.
2. 임의의 $X\in\mathfrak{g}$는 $C^\infty$이다.
3. 임의의 $X,Y\in\mathfrak{g}$에 대하여, $X$와 $Y$의 Lie bracket ([예시 4](#ex4)) $[X,Y]$ 또한 left-invariant이고, 따라서 $\mathfrak{g}$는 $\mathbb{R}$ 위에서 정의된 Lie algebra가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 벡터장들의 덧셈과 스칼라곱에 대하여 $\mathfrak{g}$가 $\mathbb{R}$-벡터공간이 된다는 것은 자명하고, 또 $\alpha$가 linear map이라는 것 또한 자명하다. 이제 $\alpha$가 isomorphism임을 보여야 하는데, $T_eG$는 유한차원 벡터공간이므로 $\alpha$가 전단사임을 보이면 충분하다. 우선 $\alpha(X)=\alpha(Y)$를 만족하는 두 $X,Y\in\mathfrak{g}$가 존재한다 가정하면, 임의의 $g\in G$에 대하여
  
    $$X_g=(dL_g)_e(X_e)=(dL_g)_e(Y_e)=Y_g$$

    이므로 $X=Y$이다. 거꾸로 임의의 $v\in T_eG$에 대하여 $X_g$를 $(dL_g)_e(v)$으로 정의하면 $X$가 left invariant인 벡터장이고, $\alpha(X)=v$를 만족함이 자명하다. 
2. $X\in\mathfrak{g}$가 $C^\infty$임을 보이기 위해서는 임의의 함수 $f$에 대하여 $Xf$가 $C^\infty$임을 보이면 충분하다. ([§벡터장, ⁋명제 2](/ko/math/manifold/vector_fields#pp2)) 한편 임의의 $p\in G$에 대하여, 
    
    $$(Xf)(p)=X_pf=(dL_p)_e(X_e)f=X_e(f\circ L_p)$$
    
    이므로 이는 다시 함수 $p\mapsto X_e(f\circ L_p)$가 $C^\infty$를 보이는 문제와 같다. $G$의 곱셈을 $m:G\times G\rightarrow G$로 쓰고, $G$에서 $G\times G$로의 자연스러운 두 embedding을

    $$\iota_1^p: x\mapsto (x,p),\qquad \iota_2^p:x\mapsto (p,x)$$

    으로 적고, $Y_e=X_e$를 만족하는 $C^\infty$ 벡터장을 택하여 $G\times G$ 위에 정의된 새로운 벡터장 $(0,Y)$을 생각하자. 그럼 $f\circ m$은 $C^\infty$ 함수이고 $(0,Y)$는 $C^\infty$ 벡터장이므로 $(0,Y)(f\circ m)$은 $C^\infty$ 함수가 되고, 따라서 합성 $\bigl((0,Y)(f\circ m)\bigr)\circ\iota_1^e$ 또한 $C^\infty$이다. 그런데 임의의 $p\in G$에 대하여, isomorphism

    $$T_{(x,y)}(M\times N)\cong T_xM\oplus T_yN$$

    을 통하면

    $$\begin{aligned}\bigl((0,Y)(f\circ m)\bigr)(\iota_1^e(p))&=(0,Y)_{(p,e)}(f\circ m)=0_p(f\circ m\circ\iota_1^e)+Y_e(f\circ m\circ\iota_2^p)\\&=X_e(f\circ m\circ\iota_2^p)=X_e(f\circ L_p)\end{aligned}$$

    이므로 원하는 결과를 얻는다.
3. [§리 미분, ⁋명제 9](/ko/math/manifold/Lie_derivative#pp9)에 의하여 자명하다.

</details>

위의 과정을 통해 얻어진 Lie algebra $\mathfrak{g}$를 *$G$의 Lie algebra*라 부른다. 일반적으로 Lie group을 $G$라 적으면, 이에 해당하는 프락투어 소문자 $\mathfrak{g}$를 통해 $G$의 Lie algebra를 적는 것이 보통이다. 

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  

---