---

title: "Distribution"
excerpt: "Distribution의 정의와 Frobenius theorem"

categories: [Math / Manifold]
permalink: /ko/math/manifold/distribution
header:
    overlay_image: /assets/images/Math/Manifold/Distribution.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2023-01-12
last_modified_at: 2023-01-12
weight: 14

---

## Distribution과 integral flow

앞서 [§벡터장](/ko/math/manifold/vector_fields)에서 우리는 주어진 manifold $M$ 위에 정의된 임의의 $C^\infty$ 벡터장 $X$에 대하여, 충분히 작은 $\epsilon>0$이 존재하여 다음의 식

$$\sigma'(t)=X(\sigma(t)),\qquad \sigma(0)=p\tag{1}$$

을 만족하는 곡선 $\sigma:(-\epsilon,\epsilon)\rightarrow M$이 존재한다는 것을 보았다. 이렇게 정의된 곡선 $\sigma$의 $M$에서의 image $S$는 점 $p$를 포함하는 $M$의 submanifold로 볼 수 있다. 

한편, 위의 식 (1)은 $\sigma$의 image 뿐만 아니라, 이를 매개화하는 방법도 강제한다. 반면 submanifold $S$는 $\sigma$의 매개화와는 무관하게 결정되므로, 이는 벡터 $X_p$가 아니라 $T_pM$의 1차원 부분공간 $\span(X_p)$에 의해서만 결정된다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $m$차원 manifold $M$이 주어졌다 하고, $1\leq k\leq m$인 정수 $k$가 주어졌다 하자. 각각의 $p\in M$마다 $T_pM$의 $k$차원 부분공간 $\mathcal{D}$를 대응시키는 함수 $p\rightarrow\mathcal{D}(p)$를 *$k$차원 distribution*이라 부른다. 

$k$차원 distribution $\mathcal{D}$가 $C^\infty$인 것은 각각의 $p\in M$마다 적당한 열린근방 $U$와, 이 위에서 정의된 $C^\infty$ 벡터장들 $X_1,\ldots, X_k$가 존재하여, 각각의 $x\in U$마다 다음의 식

$$\mathcal{D}(x)=\span\{(X_1)_x,\ldots, (X_k)_x\}$$

이 성립하는 것이다.

</div>

벡터장 $X$는 위에서 살펴본 것과 같이 다음의 식 $p\mapsto\span(X_p)\subseteq T_pM$을 통해 1차원 distribution을 정의한다. 그럼 submanifold $S$는 다음의 식

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

을 만족하도록 결정된다. 따라서 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $M$ 위에 정의된 $k$차원 distribution $\mathcal{D}$에 대하여, 다음의 식

$$T_xS=\mathcal{D}(x)\qquad\text{for all $x$}$$

을 만족하는 manifold $S$를 $\mathcal{D}$의 *integral manifold*라 부른다.

</div>

만약 각각의 $p\in M$마다, $p$를 포함하는 integral manifold가 존재한다면 이를 *integrable* distribution이라 부른다. 

## 프로베니우스 정리

다음의 정리가 잘 알려져 있다. 

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Frobenius)**</ins> Manifold $M$ 위에 정의된 $k$차원 distribution $\mathcal{D}$를 생각하자. 그럼 $\mathcal{D}$가 integrable인 것과, 임의의 $X,Y\in\mathcal{D}$에 대하여 $[X,Y]\in\mathcal{D}$가 성립하는 것이 동치이다. 

뿐만 아니라, 임의의 $k$차원 involutive distribution에 대하여 다음이 성립한다. 

1. 각각의 $p\in M$에 대하여, $p$를 포함하는 $\mathcal{D}$의 integral manifold가 존재한다. 
2. 뿐만 아니라, $p$를 중심으로 하는 coordinate system $(U,\varphi)$를 잘 택하여, 다음 식들
    
    $$x_i=\text{constant},\qquad i>k$$

   로 정의된 slice들이 $\mathcal{D}$의 integral manifold이도록 할 수 있다.
3. 마지막으로, 만일 $\Phi:N\rightarrow M$이 connected integral manifold이고, $\Phi(N)\subseteq U$라면 $\Phi(N)$은 2번의 slice들 중 단 하나의 slice에만 포함된다.

</div>

후자의 조건을 만족하는 distribution을 *involutive*라 부른다. 따라서 Frobenius 정리는 distribution $\mathcal{D}$가 integrable한 것과 involutive인 것이 동치라고 줄여 쓸 수 있다.

이 정리의 한쪽 방향은 꽤 쉽게 증명할 수 있다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> Manifold $M$ 위에 정의된 smooth distribution $\mathcal{D}$이 integrable이라 하자. 그럼 $\mathcal{D}$는 involutive distribution이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X,Y\in\mathcal{D}$라 하고, 한 점 $p\in M$을 택하자. $[X,Y]_p\in\mathcal{D}(p)$임을 보여야 한다. 

$\mathcal{D}$는 integrable distribution이므로, 점 $p$를 포함하는 $\mathcal{D}$의 integral submanifold $\Phi:S\rightarrow M$이 존재한다. 점 $s\in S$가 $\Phi(s)=p$를 만족한다 하자. 임의의 $x\in S$에 대하여 

$$d\Phi_x:T_xS\rightarrow\mathcal{D}(\Phi(x))$$

이 isomorphism이므로, 우리는 

$$d\Phi_s(\tilde{X}_s)=X_p,\qquad d\Phi_s(\tilde{Y}_s)=Y_p$$

을 만족하는 두 벡터장 $\tilde{X},\tilde{Y}$를 찾을 수 있다. 그럼 이들은 각각 $X,Y$와 $\Phi$-related인 벡터장들이므로, [§리 미분, ⁋명제 9](/ko/math/manifold/Lie_derivative#pp9)에 의하여 $[\tilde{X},\tilde{Y}]$는 $[X,Y]$와 $\Phi$-related이다. 따라서

$$[X,Y]_p=d\Phi_s([\tilde{X},\tilde{Y}]_s)\in\mathcal{D}(p)$$

이 성립한다. 

</details>

따라서 [정리 3](#thm3)의 증명에서 어려운 부분은 반대방향이라 할 수 있다. 이는 distribution의 차원 $k$에 대한 귀납법으로 진행한다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $m$차원 manifold $M$과 한 점 $p\in M$, 그리고 $X_p\neq 0$을 만족하는 벡터장 $X$가 주어졌다 하자. 그럼 $p$를 포함하는 적당한 coordinate system $(U,\varphi), \varphi=(x^1,\ldots, x^m)$가 존재하여

$$X|_U=\frac{\partial}{\partial x^1}\bigg|_U$$

이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

점 $p$를 중심으로 하는 coordinate system $(V,\tau), \tau=(y^1,\ldots, y^m)$을 택하여

$$X_p=\frac{\partial}{\partial y^1}\bigg|_p$$

이도록 하자. 일반성을 잃지 않고, $V$가 충분히 작아서 적당한 $\epsilon>0$에 대하여 다음의 함수

$$(-\epsilon,\epsilon)\times V\rightarrow M;\qquad(t,q)\mapsto X_t(q)$$

가 잘 정의된 $C^\infty$라고 가정할 수 있다. ([§벡터장, 정리 6](/ko/math/manifold/vector_fields#thm6)) 뿐만 아니라, $\epsilon>0$을 다음 포함관계

$$(-\epsilon,\epsilon)\times W\subseteq V,\qquad \text{$W$ is an open neighborhood of the origin in $\mathbb{R}^{d-1}$}$$

가 성립할만큼 작게 잡으면 다음의 함수

$$\sigma: (-\epsilon,\epsilon)\times W;\qquad (t,a^2,\ldots, a^d)\mapsto \phi^t(\tau^{-1}(0,a^2,\ldots, a^d))$$

가 잘 정의된다. 그런데

$$d\sigma\left(\frac{\partial}{\partial r^1}\bigg|_0\right)=\frac{\partial}{\partial y^1}\bigg|_p=X_p\neq 0,\qquad d\sigma\left(\frac{\partial}{\partial r^i}\bigg|_0\right)=\frac{\partial}{\partial y^i}\bigg|_p$$

이므로 $\sigma$는 원점에서 nonsingular이고, 따라서 $\sigma^{-1}$이 coordinate map을 정의한다.

</details>

<details class="proof--alone" markdown="1">
<summary>정리 3의 증명</summary>

정리가 모든 $k-1$차원 distribution에 대해 성립한다고 가정하고, $\mathcal{D}$가 $k$차원 distribution이라 하자. 한 점 $p\in M$에 대하여, $\mathcal{D}$가 $p$ 근방에서는 $k$개의 벡터장 $X_1,\ldots, X_k$에 의해 span된다고 가정할 수 있다. 이제 [보조정리 5](#lem5)를 적용하여

$$X_1|_V=\frac{\partial}{\partial y^1}$$

이도록 하는, $p$를 중심으로 하는 coordinate system $(V,\tau),\tau=(y^1,\ldots, y^k)$을 찾을 수 있다. 

이제 $k$개의 벡터장 $Y_1,\ldots, Y_k$를 다음의 식

$$Y_1=X_1,\qquad Y_i=X_i-(X_i(y^1))X_1\quad(i\geq 2)$$

으로 정의하자. $X_i$들은 서로 independent하므로 $Y_i$들도 그러하다. 

이제 $S$를 $y_1=0$에 의해 정의된 slice라 하자. 그럼 $Y_2,\ldots, Y_k$들을 $S$로 제한하여 벡터장들

$$Z_i=Y_i|_S \qquad (i\geq 2)$$

을 얻을 수 있다. 이 때, 다음의 식

$$Z_i(y^1)=Y_i(y^1)=0$$

이 성립하므로 $Z_i$들은 $S$의 tangent space에 포함되는 independent한 벡터장들임을 안다. 따라서 이들이 $S$ 위에 $k-1$차원 distribution을 span한다.

이제 귀납적 가정을 사용하기 위해 이 distribution이 involutive임을 보이자. 즉, 임의의 $i,j$에 대하여 $[Z_i,Z_j]\in\span(Z_2,\ldots, Z_k)$가 성립한다는 것을 보여야 한다.

Inclusion $\iota:S\rightarrow M$을 생각하자. 그럼 $Z_i$들은 $Y_i$와 $\iota$-related이므로, $[Y_i,Y_j]\in\span(Y_2,\ldots, Y_k)$임을 보이면 충분하다. 그런데 

$$Y_i(y^1)=X_i(y^1)-X_i(y^1)X_1(y^1)=X_i(y^1)-X_i(y^1)=0$$

이 모든 $i$에 대하여 성립하고, 따라서 $[Y_i,Y_j]y^1=0$이다. 이로부터 $[Y_i,Y_j]$들은 실제로 $\span(Y_2,\ldots, Y_k)$에 속한다는 것을 안다. 

이제 $S$ 위에 정의된 involutive distribution $\span(Z_2,\ldots, Z_k)$에 정리의 둘째 주장을 적용하면, $p\in S$를 중심으로 하는 coordinate system $(w^2,\ldots, w^d)$를 잘 택하여 식들

$$w^i=\text{constant},\qquad i>k$$

로 얻어지는 slice들이 $\span(Z_2,\ldots, Z_k)$의 integral submanifold가 되도록 할 수 있다. 

첫 번째와 두 번째 주장의 증명을 마무리하기 위해, $k$개의 함수들

$$x^1=y^1,\quad x^j=w^j\circ\pi$$

를 정의하자. 여기에서 $\pi:V\rightarrow S$는 $y_1$ 성분을 없애주는 projection이다. 그럼 이제 $(x^i)$는 independent인 함수들이므로, 우리는 이들을 성분함수로 갖는 coordinate system $(U,\varphi)$가 존재함을 안다. 그럼 이렇게 정의한 coordinate system은 둘째 주장을 만족한다. 즉, 다음의 식들

$$x^i=\text{constant},\qquad i>k$$

으로 정의된 slice들이 $\mathcal{D}$의 integral manifold가 된다. 이를 보이기 위해서는 각각의 $x^{k+1},\ldots, x^m$에 대하여 $Y_i(x^{k+j})$가 모두 $0$임을 보이면 충분하다.

우선 $x^i$들의 정의에 의하여, $\partial x^j/\partial y^1=\delta_{j1}$이 성립함을 알고, 따라서 $U$에서는 

$$Y_1=\frac{\partial}{\partial x^1}$$

이 성립한다. 나머지 $Y_2,\ldots, Y_k$에 대해서는 우선 다음의 식

$$\frac{\partial}{\partial x^1}Y_i(x^{k+j})=Y_1(Y_i(x^{k+j})=[Y_1,Y_i]x^{k+j}$$

을 사용하면, $\mathcal{D}$가 involutive라는 조건으로부터 

$$[Y_1,Y_i]=\sum_{l=1}^k c_{il}Y_l$$

을 우변에 적용하면

$$\frac{\partial}{\partial x^1}(Y_i(x^{k+j}))=\sum_{l=2}^k c_{il}Y_l(x^{k+j})$$

임을 안다. 이제 고정된 slice $W$에 대하여, $Y_i(x^{k+j})$들은 $x^1$에 대한 일변수함수이고, 따라서 위의 식은 $k-1$개의 linear ODE가 되므로 그 해를 구할 수 있다. 

이렇게 얻어진 slice들은 $S\cap U$와 단 하나의 점에서만 만나고, 여기에서는

$$Y_i(x^{k+j})=Z_i(w^{k+j})=0$$

이 성립하므로, 첫째 주장과 둘째 주장에 대한 증명이 완료되었다. 

마지막으로 세 번째 주장을 보여야 한다. 이번에는 $\pi$를 $\mathbb{R}^m$에서, 나중 $m-k$개의 좌표로의 projection이라 하자. 그럼 $\mathcal{D}$의 $d(\pi\circ\varphi)$에 의한 image가 $0$이므로, 

$$d(\pi\circ\varphi\circ\Phi)\equiv 0$$

이 임의의 $y\in N$에 대해 성립한다. 그런데 $N$은 connected이므로, $\pi\circ\varphi\circ\Phi$가 상수함수이고, 따라서 $\Phi(N)$은 하나의 slice에 포함된다.

</details>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---