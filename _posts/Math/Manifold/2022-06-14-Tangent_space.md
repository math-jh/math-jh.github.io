---

title: "접공간"
excerpt: "접벡터와 접공간"

categories: [Math / Manifold]
permalink: /ko/math/manifold/tangent_space
header:
    overlay_image: /assets/images/Manifold/Tangent_space.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-14
last_modified_at: 2022-12-09
weight: 3

---

이제 우리는 manifold의 접벡터와, 이들에 의해 생성되는 공간인 접공간을 정의한다.

## Motivation

**[Lee]**에서는 3단원의 앞부분을 꽤 길게 할애하여 앞으로 할 정의를 정당화하고 있는데, 이를 우선 간략하게 살펴보자. 

Manifold의 가장 단순한 예시는 $\mathbb{R}^m$이고, 이보다 조금 더 복잡한 예시는 $\mathbb{R}^m$에 들어있는 곡면이다. 이 곡면의 한 점 $p$에서의 접벡터는 말 그대로 곡면과 점 $p$에서 접하는 벡터들을 의미한다. 이 곡면이 $\mathbb{R}^3$에 들어있는 2차원 곡면이라 하면, 이러한 벡터들을 모아두면 정확히 점 $p$에서의 접평면이 될 것이다. 하지만 이를 manifold에서의 접벡터의 정의로 일반화하는 것은 쉽지 않다. 이 정의에서는 곡면을 포함하는 외부공간 $\mathbb{R}^m$의 존재성이 필수적인데, 우리가 manifold를 정의할 때에는 순수하게 intrinsic한 방식으로 정의했기 때문이다. 

대신 위와 같은 상황에서 우리는 접벡터들이 주어질 때마다 방향미분이 생긴다는 것을 관찰할 수 있다. 즉, 어떠한 접벡터 $v$가 주어진다면, 이 벡터는 점 $p$ 근방에서 정의된 임의의 함수 $f$마다 $v$-방향의 방향미분

$$\lim_{t\rightarrow 0}\frac{f(p+tv)-f(p)}{t}$$

을 잘 정의해준다. 우리의 아이디어는 이 <em_ko>방향미분</em_ko>이라는 연산자를 접벡터로 정의하는 것이다.

## 미분가능한 함수들의 sheaf

대수기하의 언어에 익숙하지 않다면 바로 [다음 절](/ko/math/manifold/tangent_space#%EC%A0%91%EB%B2%A1%ED%84%B0)로 넘어가도 좋다.

$C^\infty(U)$를 열린집합 $U$ 위에서 정의된 $C^\infty$ 함수들의 모임, 그리고 $U\subseteq V$일 때마다 함수 $\operatorname{res}_{UV}:C^\infty(U)\rightarrow C^\infty(V)$를 

$$\operatorname{res}_{UV}:f\mapsto f|_V$$

으로 정의하자. 그럼 이 구조는 $M$ 위에 정의된 ring들의 sheaf $\mathcal{C}^\infty_M$가 된다. 임의의 $p\in M$에서의 $\mathcal{C}^\infty$의 stalk은 $\mathcal{C}^\infty_{M,p}$, 혹은 혼동이 없을 때에는 $\mathcal{C}^\infty_p$로 적는다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 임의의 manifold $M$에 대하여 $\mathcal{C}^\infty_p$은 $\mathbb{R}$-algebra 구조를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 보이기 위해서는 $\mathcal{C}^\infty_p$ 위에서의 연산들을 정의해주면 된다. $\mathcal{C}^\infty_p$의 두 원소 $\mathbf{f},\mathbf{g}$를 택하자. 그럼 $p$의 적당한 열린근방 $U,V$가 존재하여, $\mathbf{f}$와 $\mathbf{g}$를 각각 $(f,U)$, $(g,V)$의 germ이라 생각할 수 있다. 이제 $\mathbf{f}+\mathbf{g}$를 다음의 함수

$$(f|_{U\cap V}+g|_{U\cap V}, U\cap V)$$

의 equivalence class로 정의하자. 즉 두 개의 germ $\mathbf{f}$와 $\mathbf{g}$의 합을 계산하기 위해서는 함수 $f,g$가 공통적으로 정의되는 $p$의 열린근방을 찾은 후, 이 열린근방에서 $f$와 $g$의 합을 계산하면 된다. 물론 이 정의가 representative의 선택에 의존하지 않는다는 것을 쉽게 보일 수 있다.

이와 비슷하게 함수들 사이의 곱셈과 scalar multiplication을 정의할 수 있다.

</details>

사실 $\mathcal{C}^\infty_p$에서 정의된 scalar multiplication의 경우, 이는 단순히 상수함수와의 곱으로 생각할 수 있으므로 $\mathcal{C}^\infty_p$을 algebra 대신 ring으로 보아도 상관없다. 즉 $(M,\mathcal{C}^\infty_M)$가 ringed space가 된다. 다음 명제는 이 공간이 *locally ringed space*임을 보여준다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Ring $\mathcal{C}^\infty_p$은 local ring이며, 그 maximal ideal은 다음의 식

$$\mathfrak{m}_p=\{\mathbf{f}\in \mathcal{C}^\infty_p: \mathbf{f}(p)=0\}$$

으로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 조건 $\mathbf{f}(p)=0$가 잘 정의되었다. 이는 $\mathbf{f}$에 속하는 함수들은 점 $p$에서는 모두 같은 값을 가져야 하기 때문이다. 어렵지 않게 $\mathfrak{m}_p$가 실제로 ideal이 된다는 것을 알 수 있다. 

또, $\mathfrak{m}_p$가 maximal인 것은 *evaluation map* $\operatorname{ev}_p:\mathcal{C}^\infty_p\rightarrow\mathbb{R}$을 $\mathbf{f}\mapsto\mathbf{f}(p)$로 정의했을 때, 다음의 diagram

$$0\longrightarrow \mathfrak{m}_p\longrightarrow \mathcal{C}^\infty_p\overset{\operatorname{ev}_p}{\longrightarrow}\mathbb{R}\longrightarrow 0$$

이 exact인 것으로부터 얻어진다. $\mathcal{C}^\infty_p/\mathfrak{m}_p$이 field $\mathbb{R}$이 되기 때문이다.

</details>

## 접벡터

앞선 내용을 sheaf의 언어 없이 요약하자면 다음과 같다. 

우리는 점 $p$에서의 tangent vector를 <em_ko>점 $p$에서의 방향미분</em_ko>으로 정의하기로 하였다. 이 방향미분은 물론 $M$ 전체에서 미분가능한 임의의 함수에 대해서도 잘 정의되지만, 미분가능성은 본질적으로 국소적인 성질이므로 사실 점 $p$의 적당한 열린근방 $U$ 위에서만 정의된 함수에 대한 방향미분도 정의할 수 있다.[^1] 

뿐만 아니라, 두 함수 $f,g$가 점 $p$의 어떤 열린근방 $U$ 위에서 동일한 함수를 정의한다면, 점 $p$에서의 이들의 미분 또한 동일해지므로 방향미분을 다룰 때 이들은 동일한 것으로 취급해도 된다. 그럼 우리가 관심있는 대상들은 더 이상 함수가 아니라 함수들의 equivalence class가 되며, 명시적으로 이는 다음과 같다.

$$\mathcal{C}^\infty_p=\{(f,U):f\in C^\infty(U)\}\big/{\sim},\qquad (f,U)\sim (g,V)\iff f\vert_W=g\vert_W\text{ for some $W\subseteq U\cap V$ open}$$

$f$의 equivalence class를 $\mathbf{f}$로 적자. 그럼 $\mathbf{f}\mathbf{g},\mathbf{f}+\mathbf{g}$와 같이 $\mathcal{C}^\infty$ 위에 스칼라곱과 덧셈, 더 나아가 곱셈까지 잘 정의된다는 것이 [명제 1](#pp1)의 내용이다.

이제 접벡터라는 것은 $\mathcal{C}^\infty_p$의 각 원소마다 실수값을 대응시키는 방향미분이다. 여기에서 미분은 라이프니츠 법칙을 만족하는 linear map으로 정의된다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Manifold $M$과 한 점 $p\in M$을 생각하자. 다음의 라이프니츠 법칙

$$v(\mathbf{f}\mathbf{g})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})$$

을 만족하는 $\mathbb{R}$-linear map $v:\mathcal{C}^\infty_p\rightarrow\mathbb{R}$을 점 $p$에서의 $M$의 *tangent vector<sub>접벡터</sub>*라고 부른다. 점 $p$에서의 $M$의 tangent vector들의 모임을 점 $p$에서의 $M$의 *tangent space<sub>접공간</sub>*이라 하고, $T_pM$으로 적는다.

</div>

다음 명제는 이미 명제로부터 충분히 짐작할 수 있는 사실이다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> [정의 3](#df3)에서 정의한 $T_pM$은 $\mathbb{R}$-벡터공간이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{C}^\infty_p$와 $\mathbb{R}$ 모두 $\mathbb{R}$-벡터공간이므로, $\operatorname{Hom}_\mathbb{R}(\mathcal{C}^\infty_p,\mathbb{R})$ 또한 $\mathbb{R}$-벡터공간이다. 따라서 tangent space $T_pM$이 그 이름답게 $\mathbb{R}$-벡터공간이 된다는 것을 보이기 위해서는 $T_pM$이 덧셈과 상수곱에 대해 닫혀있음만 보이면 충분하다.  예를 들어, $v+w$가 다음의 식

$$(v+w)(\mathbf{f})=v(\mathbf{f})+w(\mathbf{f})$$

으로 정의되는 linear map이므로, $T_pM$이 덧셈에 대해 닫혀있다는 것을 보이려면

$$\begin{aligned}(v+w)(\mathbf{fg})&=v(\mathbf{fg})+w(\mathbf{fg})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})+\mathbf{f}(p)w(\mathbf{g})+\mathbf{g}(p)w(\mathbf{f})\\
&=\mathbf{f}(p)(v+w)(\mathbf{g})+\mathbf{g}(p)(v+w)(\mathbf{f})\end{aligned}$$

를 계산하여 $v+w$ 또한 $T_pM$의 원소가 된다는 것을 확인할 수 있다. 

</details>

뿐만 아니라, 임의의 tangent vector $v$와 모든 점에서 값 $c$를 갖는 상수함수 $\mathbf{c}$에 대하여 $v(\mathbf{c})=0$이 항상 성립한다. $\mathbf{1}$을 함숫값 $1$을 갖는 상수함수라 하면, $\mathbf{c}=c\cdot\mathbf{1}$이므로 다음만 보이면 충분하다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 임의의 tangent vector $v$에 대하여 $v(\mathbf{1})=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$v(\mathbf{1})=v(\mathbf{1}\cdot\mathbf{1})=\mathbf{1}(p)v(\mathbf{1})+\mathbf{1}(p)v(\mathbf{1})=v(\mathbf{1})+v(\mathbf{1})=2v(\mathbf{1}).$$

</details>

그러나 아직 $T_pM$이 어떤 공간인지는 잘 알지 못한다. 특히 $T_pM$의 차원을 아직 알지 못한다. 이는 다음 글에서 살펴본다.


---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: $U$ 위에서만 정의된 함수도 partition of unity를 통해 $M$ 전체로 확장할 수 있으므로 현재 상황에서는 이 둘을 구별하지 않아도 된다.
