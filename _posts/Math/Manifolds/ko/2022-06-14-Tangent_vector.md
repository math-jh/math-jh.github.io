---

title: "접공간"
excerpt: "접벡터와 접공간"

lang: ko

categories: [Math / Manifold]
permalink: /ko/math/manifold/tangent_space
header:
    overlay_image: /assets/images/Manifold/Tangent_vector.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-14
last_modified_at: 2022-06-15
weight: 4

---

이제 우리는 manifold의 접벡터와, 이들에 의해 생성되는 공간인 접공간을 정의한다.

## Motivation

**[Lee]**에서는 3단원의 앞부분을 꽤 길게 할애하여 앞으로 할 정의를 정당화하고 있는데, 이를 우선 간략하게 살펴보자. 

Manifold의 가장 단순한 예시는 $\mathbb{R}^m$이고, 이보다 조금 더 복잡한 예시는 $\mathbb{R}^m$에 들어있는 곡면이다. 이 곡면의 한 점 $p$에서의 접벡터는 말 그대로 곡면과 점 $p$에서 접하는 벡터들을 의미한다. 이 곡면이 $\mathbb{R}^3$에 들어있는 2차원 곡면이라 하면, 이러한 벡터들을 모아두면 정확히 점 $p$에서의 접평면이 될 것이다. 하지만 이를 manifold에서의 접벡터의 정의로 일반화하는 것은 쉽지 않다. 이 정의에서는 곡면을 포함하는 외부공간 $\mathbb{R}^m$의 존재성이 필수적인데, 우리가 manifold를 정의할 때에는 순수하게 intrinsic한 방식으로 정의했기 때문이다. 

대신 위와 같은 상황에서, 우리는 접벡터들이 주어질 때마다 방향미분이 생긴다는 것을 관찰할 수 있다. 즉, 어떠한 접벡터 $v$가 주어진다면, 이 벡터는 점 $p$ 근방에서 정의된 임의의 함수 $f$마다, $v$-방향의 방향미분

$$\lim_{t\rightarrow 0}\frac{f(p+tv)-f(p)}{t}$$

을 잘 정의해준다. 우리의 아이디어는 이 <em_ko>방향미분</em_ko>이라는 연산자를 접벡터로 정의하는 것이다.

## 함수의 germ

함수 $f$가 점 $p$에서 잘 정의된 미분의 개념을 갖기 위해서는 $f$가 $p$ 근방에서 정의되어야 한다. 여기에서 $p$ 근방에서 정의되어야 한다는 말은 $f$가 $p$의 특정한 열린근방에서 정의되어야 한다는 것이 아니라, $p$의 아무 열린근방 위에서만 $f$가 정의된다면, 미분을 정의하는 데에는 아무런 문제가 없다는 뜻이다. 

뿐만 아니라, 두 함수 $f,g$가 $p$의 적당한 열린근방 $U$에서 같은 함수가 된다면, 즉 $f\|\_U=g\|\_U$라면 이 두 함수 $f,g$의 방향미분 또한 동일할 것이다. 따라서 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Manifold $M$과, $M$의 한 점 $p$가 주어졌다 하고, 두 $C^\infty$ 함수 $f,g$가 점 $p$ 근방에서 정의되었다 하자. 이들 두 함수가 점 $p$에서 동일한 *germ<sub>싹</sub>*을 갖는다는 것은 $p$의 적당한 열린근방 $U$가 존재하여 $f\|\_U=g\|\_U$가 성립하는 것이다.

</div>

어쨌든 germ이라는 것은 적당한 equivalence relation의 equivalence class이고, 이 equivalence relation은 점 $p$의 어떤 근방에서 일치하는 두 함수를 같게 보는 relation이다. **[War]**를 따라 주어진 함수 $f$에 대하여[^1], 잠시동안 $f$의 germ을 $\mathbf{f}$로 표기하기로 하자. 이 표기법은 썩 좋은 표기법은 아니지만, 어차피 접벡터를 엄밀하게 정의한 이후에는 이를 잘 사용하지 않을 것이다.

조금 더 고상한 표현을 빌리자면, $C^\infty(U)$를 열린집합 $U$ 위에서 정의된 $C^\infty$ 함수들의 모임, 그리고 $U\subset V$일 때마다 함수 $\operatorname{res}_{UV}:C^\infty(U)\rightarrow C^\infty(V)$를 

$$\operatorname{res}_{UV}:f\mapsto f|_V$$

으로 정의할 때 germ들은 다음의 direct limit

$$C_p^\infty=\varinjlim_{p\in U} C^\infty(U)$$

의 원소들이라 할 수 있다. ([집합론, §극한<sup>†</sup>, 예시 15](/ko/math/set_theory/limits#ex15)) 

적어도 미분다양체를 다루는 동안은 이 정의를 다시 볼 일은 없긴 하지만, 이렇게 germ들의 모임을 $C^\infty_p$로 적는 표기법은 그대로 사용하자. 이 표기법은 manifold $M$을 특정해주지 않기 때문에, $C_p^\infty(M)$과 같은 표기도 사용한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 manifold $M$에 대하여 $C^\infty_p(M)$은 $\mathbb{R}$-algebra 구조를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 보이기 위해서는 $C^\infty_p(M)$ 위에서의 연산들을 정의해주면 된다. $C^\infty_p(M)$의 두 원소 $\mathbf{f},\mathbf{g}$를 택하자. 그럼 $p$의 적당한 열린근방 $U,V$가 존재하여, $\mathbf{f}$와 $\mathbf{g}$를 각각 $(U, f)$, $(V, g)$의 germ이라 생각할 수 있다. 이제 $\mathbf{f}+\mathbf{g}$를 다음의 함수

$$(U\cap V, f|_{U\cap V}+g|_{U\cap V})$$

의 equivalence class로 정의하자. 즉 두 개의 germ $\mathbf{f}$와 $\mathbf{g}$의 합을 계산하기 위해서는 함수 $f,g$가 공통적으로 정의되는 $p$의 열린근방을 찾은 후, 이 열린근방에서 $f$와 $g$의 합을 계산하면 된다. 물론 이 정의가 representative의 선택에 의존하지 않는다는 것을 쉽게 보일 수 있다.

이와 비슷하게 함수들 사이의 곱셈과 scalar multiplication을 정의할 수 있다.

</details>

사실 $C^\infty_p(M)$에서 정의된 scalar multiplication의 경우, 이는 단순히 상수함수와의 곱으로 생각할 수 있으므로 $C^\infty_p(M)$을 algebra 대신 ring으로 보아도 상관없다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Ring $C^\infty_p(M)$은 local ring이며, 그 maximal ideal은 다음의 식

$$\mathfrak{m}=\{\mathbf{f}\in C^\infty_p(M): \mathbf{f}(p)=0\}$$

으로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 조건 $\mathbf{f}(p)=0$가 잘 정의되었다. 이는 $\mathbf{f}$에 속하는 함수들은 점 $p$에서는 모두 같은 값을 가져야 하기 때문이다. 어렵지 않게 $\mathfrak{m}$이 실제로 ideal이 된다는 것을 알 수 있다. 

또, $\mathfrak{m}$이 maximal인 것은 *evaluation map* $\operatorname{ev}_p:C^\infty_p(M)\rightarrow\mathbb{R}$을 $\mathbf{f}\mapsto\mathbf{f}(p)$로 정의했을 때, 다음의 diagram

$$0\longrightarrow \mathfrak{m}\longrightarrow C^\infty_p(M)\overset{\operatorname{ev}_p}{\longrightarrow}\mathbb{R}\longrightarrow 0$$

이 exact인 것으로부터 얻어진다. $C^\infty_p(M)/\mathfrak{m}$이 field가 되기 때문이다.

</details>

역시 이 maximal ideal을 $\mathfrak{m}$으로 적는 것 또한 manifold $M$에 대한 정보를 담지 않고 있지만, 현실적으로 $\mathfrak{m}$ 이 등장하는 상황에서 이를 구분해줄 일이 많지 않기 때문에 이 표기는 그대로 사용하기로 한다.

## 접벡터

지금까지 우리는 <em_ko>방향미분</em_ko>, 곧 접벡터의 정의역이 될 집합을 정의했다. 즉 접벡터라는 것은 $C^\infty_p(M)$의 각 원소마다 실수값을 대응시키는 함수이다. 대수학에서는 이를 위해 linear map에 다음과 같이 라이프니츠 법칙을 추가적인 조건으로 부여하여 미분을 정의했었다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 임의의 $\mathbb{R}$-algebra $A$에 대하여, $\mathbb{R}$-linear map $d:A\rightarrow A$이 *derivation<sub>미분</sub>*이라는 것은 다음의 *라이프니츠 법칙<sub>Leibniz rule</sub>*

$$d(ab)=d(a)b+ad(b)$$

이 모든 $a,b\in A$에 대하여 성립하는 것이다.

</div>

우리가 지금 정의할 접벡터 또한 방향미분으로서, 라이프니츠 법칙을 만족하도록 정의된다. 다만 방향미분은 $C_p^\infty(M)$의 원소 $\mathbf{f}$를 받아 $C_p^\infty(M)$ 대신 $\mathbb{R}$의 원소를 내놓아야 하므로 위와는 다른 정의를 사용해야 한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Manifold $M$과 한 점 $p\in M$을 생각하자. 다음의 라이프니츠 법칙

$$v(\mathbf{f}\mathbf{g})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})$$

을 만족하는 $\mathbb{R}$-linear map $v:C^\infty_p(M)\rightarrow\mathbb{R}$을 점 $p$에서의 $M$의 *tangent vector<sub>접벡터</sub>*라고 부른다. 점 $p$에서의 $M$의 tangent vector들의 모임을 점 $p$에서의 $M$의 *tangent space<sub>접공간</sub>*이라 하고, $T_pM$으로 적는다.

</div>

$C^\infty_p(M)$와 $\mathbb{R}$ 모두 $\mathbb{R}$-벡터공간이므로, $\operatorname{Hom}_\mathbb{R}(C^\infty_p(M),\mathbb{R})$ 또한 $\mathbb{R}$-벡터공간이다. 따라서 tangent space $T_pM$이 그 이름답게 $\mathbb{R}$-벡터공간이 된다는 것을 보이기 위해서는 $T_pM$이 덧셈과 상수곱에 대해 닫혀있음만 보이면 충분하다.  예를 들어, $v+w$가 다음의 식

$$(v+w)(\mathbf{f})=v(\mathbf{f})+w(\mathbf{f})$$

으로 정의되는 linear map이므로, $T_pM$이 덧셈에 대해 닫혀있다는 것을 보이려면

$$\begin{aligned}(v+w)(\mathbf{fg})&=v(\mathbf{fg})+w(\mathbf{fg})=\mathbf{f}(p)v(\mathbf{g})+\mathbf{g}(p)v(\mathbf{f})+\mathbf{f}(p)w(\mathbf{g})+\mathbf{g}(p)w(\mathbf{f})\\
&=\mathbf{f}(p)(v+w)(\mathbf{g})+\mathbf{g}(p)(v+w)(\mathbf{f})\end{aligned}$$

를 계산하여 $v+w$ 또한 $T_pM$의 원소가 된다는 것을 확인할 수 있다. 

뿐만 아니라, 임의의 tangent vector $v$와 모든 점에서 값 $c$를 갖는 상수함수 $\mathbf{c}$에 대하여 $v(\mathbf{c})=0$이 항상 성립한다. $\mathbf{1}$을 함숫값 $1$을 갖는 상수함수라 하면, $\mathbf{c}=c\cdot\mathbf{1}$이므로 다음만 보이면 충분하다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 임의의 tangent vector $v$에 대하여 $v(\mathbf{1})=0$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$v(\mathbf{1})=v(\mathbf{1}\cdot\mathbf{1})=\mathbf{1}(p)v(\mathbf{1})+\mathbf{1}(p)v(\mathbf{1})=v(\mathbf{1})+v(\mathbf{1})=2v(\mathbf{1}).$$

</details>

## 여접공간과 차원

위의 정의에 의하여 tangent space는 $\mathbb{R}$-벡터공간이 된다. Tangent space는 manifold를 다룰 때에 특히 중요하게 사용되는데, tangent space의 성질 중 우리가 가장 먼저 보일 것은 tangent space $T_pM$이 실은 유한차원 벡터공간이 되며, 그 차원은 manifold $M$의 차원과 동일하다는 것이다. 이를 곧바로 증명하는 것도 어렵지는 않지만, 앞으로 계속해서 사용할 dual space를 연습할 수 있는 **[War]**의 방식도 좋아 보인다.

[명제 3](#pp3)에 의하여, $C_p^\infty(M)$의 ideal들의 descending chain

$$C_p^\infty(M)\supset\mathfrak{m}\supset\mathfrak{m}^2\supset\cdots$$

이 잘 정의된다. 그럼 특히 $\mathfrak{m}/\mathfrak{m}^2$를 $C_p^\infty(M)/\mathfrak{m}\cong\mathbb{R}$ 위의 벡터공간으로 볼 수 있다. 

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> Manifold $M$과 임의의 한 점 $p\in M$에 대하여, $T_pM\cong(\mathfrak{m}/\mathfrak{m}^2)^\ast$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $v\in T_pM$가 주어졌다 하자. 즉, 정의에 의하여 $v$는 $C_p^\infty(M)$에서 $\mathbb{R}$로의 derivation이고, 특히 이를 부분집합 $\mathfrak{m}$으로 restrict하면 $v\|\_\mathfrak{m}\in\operatorname{Hom}_\mathbb{R}(\mathfrak{m},\mathbb{R})$이 성립한다. 이제 $v\|\_\mathfrak{m}$이 linear map $\mathfrak{m}/\mathfrak{m}^2\rightarrow\mathbb{R}$을 잘 정의한다는 것을 보이려면 $\mathfrak{m}^2\subset\ker (v\|\_\mathfrak{m})$임을 보여야 한다. 적당한 index set $I$에 대하여, $\mathfrak{m}$가 $\mathbf{f}_i$들에 의해 생성되는 ideal이라 하자. 그럼 $\mathfrak{m}^2$은 $\mathbf{f}_i\mathbf{f}_j$들에 의하여 생성되는 ideal이다. 그런데

$$v(\mathbf{f}_i\mathbf{f}_j)=\mathbf{f}_i(p)v(\mathbf{f}_j)+\mathbf{f}_j(p)v(\mathbf{f}_i)=0$$

이므로, $v$는 $\mathfrak{m}^2$의 임의의 generator를 항상 0으로 보내고, $\mathfrak{m}^2\subset\ker(v\|\_\mathfrak{m})$이며, 따라서 임의의 $v\in T_pM$마다 적당한 $\mathfrak{m}/\mathfrak{m}^2$의 원소를 대응시킬 수 있다. 이 대응이 $\mathbb{R}$에 대한 linear map이라는 것은 자명하다.

반대로 임의의 $L\in(\mathfrak{m}/\mathfrak{m}^2)^\ast$이 주어졌다 하고, 이를 이용해 tangent vector $v_L$을 하나 만들자. Tangent vector는 $C_p^\infty$에서 $\mathbb{R}$로의 linear map으로서, $v_L$을 만든다는 것은 임의의 $\mathbf{f}\in C_p^\infty(M)$에 대하여 $v_L(\mathbf{f})$의 값을 정해주는 것과 같다. $\mathbf{f(p)}$를 함숫값 $f(p)$를 갖는 상수함수라 하면, $\mathbf{f}-\mathbf{f(p)}$는 $\mathfrak{m}$의 원소이고, 따라서 

$$v_L(\mathbf{f})=L((\mathbf{f}-\mathbf{f(p)})+\mathfrak{m}^2)$$

으로 정의하는 것이 잘 정의된다. 이렇게 정의된 $v_L$이 linear map일 뿐만 아니라 derivation이기도 하다는 것을 보여야 하므로, 

$$\begin{aligned}
            v_L(\mathbf{f}\cdot\mathbf{g})&=L((\mathbf{fg}-\mathbf{f(p)g(p)})+\mathfrak{m}^2)\\
            &=L(((\mathbf{f}-\mathbf{f(p)})(\mathbf{g}-\mathbf{g(p)})+\mathbf{f(p)}(\mathbf{g}-\mathbf{g(p)})+(\mathbf{f}-\mathbf{f(p)})\mathbf{g(p)})+\mathfrak{m}^2)\\
            &=\mathbf{f}(p)L((\mathbf{g}-\mathbf{g(p)})+\mathfrak{m}^2)+\mathbf{g}(p)L((\mathbf{f}-\mathbf{f(p)})+\mathfrak{m}^2)\\
            &=\mathbf{f}(p)+v_L(\mathbf{g})+\mathbf{g}(p)v_L(\mathbf{f}).
        \end{aligned}
$$

을 계산할 수 있다. $L\mapsto v_L$ 또한 linear map이 된다는 것을 쉽게 보일 수 있으며, 뿐만 아니라 이 대응이 앞서 정의한 $T_pM$에서 $(\mathfrak{m}/\mathfrak{m}^2)^\ast$로의 linear map의 역함수가 된다는 것을 확인할 수 있다.

</details>

앞서 언급한 것과 같이 tangent space $T_pM$은 사실 유한차원 벡터공간이고, 따라서 우변의 벡터공간 $\mathfrak{m}/\mathfrak{m}^2$ 또한 그러하다. 이제 

$$(T_pM)^\ast\cong(\mathfrak{m}/\mathfrak{m}^2)^{\ast\ast}\cong\mathfrak{m}/\mathfrak{m}^2$$

이므로, $\mathfrak{m}/\mathfrak{m}^2$을 *cotangent space<sub>여접공간</sub>*으로 생각하면 좋을 것이다. 

어쨌든 이를 이용하면 $T_pM$의 차원을 계산할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> $\mathbb{R}$-벡터공간 $\mathfrak{m}/\mathfrak{m}^2$의 차원은 유한하며, 그 값은 manifold $M$의 차원과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이를 보이기 위해, 다음의 다변수 테일러 근사

$$\begin{aligned}g(x)&=g(x_0)+\sum_{i=1}^m\frac{\partial g}{\partial r^i}\bigg|_{x_0}(r^i(x)-r^i(x_0))\\
&\phantom{phantom}+\sum_{i,j}(r^i(x)-r^i(x_0))(r^j(x)-r^j(x_0))\int_0^1(1-t)\frac{\partial^2g}{\partial r^i\partial r^j}\bigg|_{(x_0+t(x-x_0))}\mathop{dt}\end{aligned}$$

을 사용한다. 

$(U,\varphi)$가 $p$을 중심으로 하는 coordinate system이고, $\varphi=(x^i)\_{i=1}^m$라 하자. 또, $\mathbf{f}\in\mathfrak{m}$가 임의로 주어졌다 하자. 

위의 식은 유클리드 공간에서 성립하는 식이므로, $g=f\circ\varphi^{-1}$로 두고, $g$의 정의역이 $\varphi(U)$인 것으로 생각하자. 원점을 중심으로 한 테일러 근사로부터, 임의의 $x\in\varphi(U)$에 대하여 다음의 식

$$g(x)=g(0)+\sum_{i=1}^m\frac{\partial g}{\partial r^i}\bigg|_0r^i(x)+\sum_{i,j}r^i(x)r^j(x)\int_0^1(1-t)\frac{\partial^2g}{\partial r^i\partial r^j}\bigg|_{tx}\mathop{dt}$$

을 얻는다. 이제 $x=\varphi(q)$라 하면

$$\begin{aligned}f(q)&=f(p)+\sum_{i=1}^m\frac{\partial (f\circ\varphi^{-1})}{\partial r^i}\bigg|_0r^i(\varphi(q))+\sum_{i,j}r^i(\varphi(q))r^j(\varphi(q))\int_0^1(1-t)\frac{\partial^2g}{\partial r^i\partial r^j}\bigg|_{t\varphi(q)}\mathop{dt}\\ &=f(p)+\sum_{i=1}^m\frac{\partial(f\circ\varphi^{-1})}{\partial r^i}\bigg|_0 x^i(q)+\sum_{i,j} x^i(q)x^j(q)\int_0^1(1-t)\frac{\partial^2 g}{\partial r^i\partial r^j}\bigg|_{t\varphi(q)}dt\end{aligned}$$

이다. 우변을 살펴보면, $\mathbf{f}\in\mathfrak{m}$으로부터 $f(p)=0$이고, 또 우변의 적분은 $q$에 대한 $C^\infty$ 함수이다. 이제 $x^i$들은 모두 $x^i(p)=0$을 만족하는 함수이므로, 위 식을 germ으로 바꾸면 우변의 이중합은 $\mathfrak{m}^2$의 원소가 된다. 이를 모두 정리하면

$$\mathbf{f}=\sum_{i=1}^m\frac{\partial(f\circ\varphi^{-1})}{\partial r^i}\bigg|_0\mathbf{x}^i\mod \mathfrak{m}^2$$

이 성립한다. $\mathbf{f}$는 임의의 원소이므로, $\mathfrak{m}/\mathfrak{m}^2$이 $\mathbf{x}^i+\mathfrak{m}^2$들로 생성됨을 알 수 있다.

증명을 마무리하기 위해서는 이들 $n$개의 원소들 $\mathbf{x}^i+\mathfrak{m}^2$들이 linearly independent함을 보여야 한다. 

$$\sum_{i=1}^m a_i\mathbf{x}^i=0\mod \mathfrak{m}^2$$

이라 하자. 그럼 coordinate domain $U$ 위에서 위 식은

$$\sum_{i=1}^m a_i (x^i\circ\varphi^{-1})=0\mod \mathfrak{n}^2$$

이 되고 (단, $\mathfrak{n}$은 점 $0\in\varphi(U)$에 대응되는 maximal ideal이다), $x^i\circ\varphi^{-1}=r^i$이므로 

$$\sum_{i=1}^m a_i\mathbf{r}^i=0\mod \mathfrak{n}^2$$

가 된다. 

우리는 아직 $\partial/\partial x^i$를 정의하진 않았지만 Euclidean space에서의 partial derivative는 잘 알고 있다. 이를 이용해서 위 식의 양변에 $\partial/\partial r^j$를 취하면, 우변의 $0$ (즉 $\mathfrak{n}^2$의 어떤 원소)는 라이프니츠 법칙에 의해 $0$이 될 것이고, 따라서 이 식은

$$a_j=\frac{\partial}{\partial r^j}\bigg|_0\sum a_i r^i=0$$

이 된다. 따라서 $a_j=0$이 모든 $j$에 대해 성립하고 $\mathbf{x}^i+\mathfrak{m}^2$들은 linearly independent하다.

</details>

따라서 $\mathfrak{m}/\mathfrak{m}^2$의 dual space인 $T_pM$ 또한 $M$의 차원과 동일한 차원을 가진다. 그런데 앞선 정리의 증명을 잘 살펴보면, 단순히 차원에 대한 정보 뿐만 아니라 $T_pM$의 basis 또한 얻을 수 있다. 

앞선 증명에서 우리는 $\mathbf{x}^i+\mathfrak{m}^2$들이 $\mathfrak{m}/\mathfrak{m}^2$의 basis가 된다는 것을 보였는데, tangent space $T_pM$은 $(\mathfrak{m}/\mathfrak{m}^2)^\ast$와 isomorphic하다는 사실을 잘 알고 있으므로 $T_pM$의 basis를 이들의 dual basis로 잡는 것이 자연스러워 보인다. 즉,

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> Manifold $M$과 $p\in M$이 주어졌다 하자. $p$을 포함하는 coordinate system $(U,\varphi)$, 그리고 $\varphi$의 component function들 $x^i$에 대하여, $x^i$ 방향의 *directional derivative*는 다음의 식

$$\left(\frac{\partial}{\partial x^i}\bigg|_p\right)f=\frac{\partial(f\circ \varphi^{-1})}{\partial r^i}\bigg|_{\varphi(p)}$$

으로 정의되는 tangent vector이다.

</div>

물론 모든 tangent vector들은 방향미분들로 생각할 수 있지만, 이들 벡터들 $\partial/\partial x^i$들의 특별한 점은 이들이 정확히 coordinate system이 정의해주는 좌표축과 평행한 방향의 미분들이라는 것이다. 

이 $m$개의 tangent vector들은 앞서 말했듯 $\mathfrak{m}/\mathfrak{m}^2$의 basis의 dual이므로, 이들이 basis를 이루는 것은 자명하다. 그러면, 임의의 $v\in T_pM$에 대해, $v$를 $\partial/\partial x^i$들의 linear combination으로 나타내는 방법 또한 유일하게 존재해야 할 것이다. 이는 다음의 식

$$v=\sum_{i=1}^m v(x^i)\frac{\partial}{\partial x^i}\bigg|_p$$

으로 주어진다. 이 식이 맞는지를 체크해 보기 위해서는 임의의 $\mathbf{f}$에다 위 식의 양 변에 있는 tangent vector들을 각각 적용해본 후 그 결과를 비교하면 된다. 혹은 더 간단하게, $\mathbf{f}$는 $\mathbf{x}^i+\mathfrak{m}^2$들의 linear combination으로 나타나니, $\mathbf{x}^j$에 대해서만 적용해 봐도 충분할 것이다. 우변을 $\mathbf{x}^j$에 적용해보면,

$$\sum_{i=1}^m v(x^i)\frac{\partial}{\partial x^i}\bigg|_p x^j=\sum_{i=1}^m v(x^i)\delta_{ij}=v(x^j)$$

이 되므로 앞선 식이 성립한다. 

이제 우리는 tangent vector를 엄밀한 언어로 정의하였으므로, 다음 글부터는 $C^\infty_p(M)$의 원소들을 germ $\mathbf{f}$로 쓰지 않고, 간단히 $f$로만 적기로 한다. 이 때 $f\in C^\infty_p(M)$이라는 것은 $f$가 $p\in M$의 적당한 열린근방에서 정의된 $C^\infty$ 함수라는 뜻이다.


---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---

[^1]: 여기에서 <em_ko>함수</em_ko>는 정의역까지 명시된 것으로 취급한다. 즉, $\mathbf{f}$는 $(U,f)$를 포함하는 equivalence class를 의미하며, 이 때의 쌍 $(U,f)$는 함수 $f$가 $p$의 열린근방 $U$에서 정의되었음을 의미한다. 
