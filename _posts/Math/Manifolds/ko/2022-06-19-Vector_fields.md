---

title: "벡터장"
excerpt: "Vector fields"

categories: [Math / Manifold]
permalink: /ko/math/manifold/vector_fields
header:
    overlay_image: /assets/images/Manifold/Vector_fields.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-19
last_modified_at: 2022-06-19
weight: 11

---

## 벡터장

앞선 글에서 벡터다발을 정의한 것은 나중에 사용하기 위한 것이기도 하지만, 당장은 벡터장을 정의하기 위해 필요했기 때문이다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Vector bundle $\pi: TM\rightarrow M$의 (global) section $X:M\rightarrow TM$을 *vector field<sub>벡터장</sub>*라 부른다. 더 일반적으로, 임의의 submanifold $S\rightarrow M$에 대하여, $S$를 따라 정의된 vector field라는 것은 $\pi\|\_S:TM\|\_S\rightarrow S$의 global section을 의미한다. 

</div>

Vector field $X$에 대하여, 점 $p$에서의 $X$의 함숫값은 $X(p)$ 대신 $X_p$로 적는 것이 보통이다. 이는 $T_pM$의 원소로서 $X_p$가 $C^\infty_p(M)$의 원소 $f$에 작용하므로, 이를 $X_p(f)$로 적기 위해서이다.

한편 $f$가 열린집합 $U\subset M$에서 정의되었다 하자. 그럼 각각의 $p\in U$에 대하여 $X_p(f)$가 잘 정의되며, 대응 $p\mapsto X_p(f)$를 $U$ 위에서 정의된 함수로 생각할 수 있다. 이를 $X(f)$로 적는다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> Manifold $M$ 위에서 정의된 vector field $X$를 생각하자. 다음이 모두 동치이다.

1. $X$가 $C^\infty$이다.
2. 임의의 coordinate system $(U,\varphi)$, $\varphi=(x^i)\_{i=1}^m$에 대하여, 다음의 식
    
    $$(X|_U)_p=\sum_{i=1}^m a^i(p)\frac{\partial}{\partial x^i}\bigg|_p$$

    으로 정의된 함수 $a^i:U\rightarrow\mathbb{R}$들이 모두 $U$에서 정의된 $C^\infty$ 함수들이다. 
3. 임의의 열린집합 $V\subset M$과 $V$ 위에서 정의된 $C^\infty$ 함수 $f:V\rightarrow\mathbb{R}$에 대하여, $X(f)$ 또한 $C^\infty$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$가 $C^\infty$라면 $X\|\_U$가 $C^\infty$인 것은 자명하다. 한편, $TM$에서 정의된 함수로서 $dx^i$들은 coordinate system $\tilde{\varphi}:\pi^{-1}(U)\rightarrow\mathbb{R}^{2m}$의 성분함수들이므로 마찬가지로 $C^\infty$이고, 따라서 이들의 합성

$$a^i(p)=dx^i\left(\sum a^i(p)\frac{\partial}{\partial x^i}\bigg|_p\right)=dx^i|_p\circ(X|_U)_p$$

또한 $C^\infty$인 것이 자명하다. 

2번 조건이 성립한다 가정하자. 임의의 $p\in V$에 대하여 $X(f)$가 $p$에서 $C^\infty$인 것을 보여야 하므로, 이를 위해서는 $p$를 포함하는 적당한 coordinate system $(U,\varphi)$에 대하여 $X(f)$가 $p$에서 $C^\infty$임을 보이면 충분하다. 이제 2번 조건에 의하여 

$$(X|_U)_pf=\sum_{i=1}^m a^i(p)\frac{\partial f}{\partial x^i}(p)$$

이고, 그럼 우변의 식은 $U$ 위에서 정의된 $C^\infty$ 함수가 되므로 $X(f)$가 $C^\infty$ 함수이다.

마지막으로 3번 조건을 가정하고 1번을 보이자. $X:M\rightarrow TM$이 $C^\infty$임을 보이기 위해서는 임의의 coordinate system $(U,\varphi)$에 대하여 $X\circ\varphi^{-1}$가 $\varphi(U)$에서 $TM$으로의 $C^\infty$ 함수임을 보이면 되고, 이는 다시 $TM$의 coordinate system을 생각하면 다음의 함수들

$$x^i\circ\pi\circ (X|_U),\quad dx^i\circ(X|_U)$$

들이 $C^\infty$임을 보이면 된다. 그런데 직접 계산을 해 보면

$$x^i\circ\pi\circ (X|_U)=x^i\circ\operatorname{id}_U=x^i,\qquad dx^i\circ(X|_U)=X(x^i)$$

가 성립하므로 이들은 모두 $C^\infty$가 된다.

</details>

$M$ 위에서 정의된 $C^\infty$ vector field들의 모임을 $\mathfrak{X}(M)$으로 적는다. $\mathfrak{X}(M)$이 $\mathbb{R}$-벡터공간이 된다는 것은 자명하다. 뿐만 아니라, $M$ 전체에서 정의된 $C^\infty$ 함수의 모임을 $C^\infty(M)$이라 적으면 $\mathfrak{X}(M)$이 $C^\infty(M)$-module이 된다. 이는 임의의 $f\in C^\infty(M)$에 대하여 vector field $fX$를 다음의 식

$$(fX)_p=f(p)X_p$$

으로 정의해주면 된다. 

그럼 앞선 [명제 2](#pp2)에 의해 $X$는 $C^\infty(M)$에서 $C^\infty(M)$으로의 derivation을 정의한다. ([§접공간, 정의 4](/ko/math/manifold/tangent_space#df4)) 뿐만 아니라, $C^\infty(M)$에서 $C^\infty(M)$으로의 derivation들의 모임은 정확하게 $\mathfrak{X}(M)$과 identify하면 된다. 이는 임의의 derivation $D:C^\infty(M)\rightarrow C^\infty(M)$이 주어졌을 때, $\mathfrak{X}(M)$의 한 원소 $X$를 다음의 식

$$X_p(f)=(Df)(p)$$

으로 정의해줄 수 있기 때문이다. 

## Lie Bracket

$\mathfrak{X}(M)$은 일반적인 설정에서 $C^\infty(M)$-algebra가 되지는 않는다. 즉 두 원소 $X,Y\in\mathfrak{X}(M)$에 대하여 다음의 식

$$(XY)f=X(Yf)$$

으로 정의된 $XY$는 vector field가 되지 않는다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $\mathbb{R}^2$에서 정의된 두 vector field $X=\frac{\partial}{\partial x}$와 $Y=x\frac{\partial}{\partial y}$를 생각하자. 그럼 $C^\infty(M)$의 두 원소 $f(x,y)=x$와 $g(x,y)=y$에 대하여

$$(XY)(fg)=\frac{\partial}{\partial x}\left(x\frac{\partial}{\partial y}(xy)\right)=\frac{\partial}{\partial x}x^2=2x$$

이지만, 

$$f(XY)g=x\left(\frac{\partial}{\partial x}\left(x\frac{\partial}{\partial y}y\right)\right)=x$$

이고

$$g(XY)f=y\left(\frac{\partial}{\partial x}\left(x\frac{\partial}{\partial y} x\right)\right)=0$$

이므로

$$(XY)(fg)\neq f(XY)g+g(XY)f$$

이다. 즉, $XY$는 라이프니츠 법칙을 만족하지 않고 따라서 $\mathfrak{X}(M)$의 원소가 아니다.

</div>

더 일반적인 세팅에서 $(XY)(fg)$를 직접 계산해보면,

$$(XY)(fg)=X(f(Yg)+g(Yf))=(Xf)(Yg)+f(XY)g+(Xg)(Yf)+g(XY)f\tag{1}$$

이 된다는 것을 확인할 수 있다. 바꾸어 말하자면 $XY$가 라이프니츠 법칙을 만족하지 못하도록 하는 것은 두 개의 항 $(Xf)(Yg)$와 $(Xg)(Yf)$이며, 따라서 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> $X,Y\in\mathfrak{X}(M)$에 대하여, $[X,Y]\in\mathfrak{X}(M)$은 다음의 식

$$[X,Y]f=X(Yf)-Y(Xf)$$

으로 정의되는 원소이다.

</div>

물론 이 정의가 말이 되기 위해서는 우변의 식이 실제로 $\mathfrak{X}(M)$의 원소가 된다는 것을 확인해야 하지만, 이는 위에서 계산한 식 (1)에서 $X$와 $Y$의 정의를 바꾸어 $(YX)(fg)$를 얻은 후, 이를 빼면 된다. 애초부터 이 정의는 문제가 되는 두 항을 소거하기 위한 정의였으므로 당연히 라이프니츠 법칙이 성립할 것이다.

이렇게 정의된 vector field $[X,Y]$를 $X$와 $Y$의 *Lie bracket*이라 부른다. 이 정의는 나중에 아주 중요하게 쓰이므로, 몇 가지 결과를 미리 정리해 두는 것이 좋아보인다.

두 manifold $M,N$ 사이의 $C^\infty$ 함수 $F:M\rightarrow N$이 주어졌다 하자. 그럼 $dF_p:T_pM\rightarrow T_{F(p)}N$은 $M$의 한 점 $p$에서 정의된 tangent vector $v$를 $N$의 한 점 $F(p)$에서 정의된 tangent vector $dF_p(v)$로 보내주는 함수이다. 그러나 일반적으로 이것이 vector field에 대해 가능할 필요는 없다. 즉, $M$ 위에서 정의된 vector field $X$가 주어져 있다 하여, 이를 $dF_p$ 등을 통해 $N$ 위에서 정의된 vector field를 만들 수 없다. 

예컨대 $F$가 surjection이 아니라면, $F$의 image에 속하지 않는 점 $q\in N$에서의 tangent vector를 대응시키는 방법이 자연스럽게 존재하지 않는다. 이는 치역을 제한하는 등의 방식으로 해결한다 치더라도, 만일 $F$가 injective가 아니고 $F(p_1)=F(p_2)=q\in N$라면, 이 공통의 점 $q$에서의 tangent vector를 $dF\_{p\_1} v\_1$과 $dF\_{p\_2} v\_2$ 중 어떤 것을 택해야 할지도 정해야 한다.

때문에 $X\in\mathfrak{X}(M)$을 $F$를 통해 움직이려 하기보다는 이미 주어진 $Y\in\mathfrak{X}(N)$이 원하는 성질을 만족하는 경우를 살펴보는 편이 현명하다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $F:M\rightarrow N$이 $C^\infty$ 함수라 하자. 만일 $X\in\mathfrak{X}(M)$과 $Y\in\mathfrak{X}(N)$이 다음의 식

$$dF_p(X_p)=Y_{F(p)}$$

을 모든 $p\in M$에 대해 만족한다면, $X$와 $Y$가 *$F$-related*되어있다고 부른다.

</div>

즉, $X$와 $Y$가 $F$-related라는 것은 다음의 diagram이 commute한다는 것이다.

![F-related](/assets/images/Manifold/Vector_fields-1.png){:width="160px" class="invert" .align-center}

[명제 2](#pp2)에서 $X$가 $C^\infty$임을 각각의 함수 $f$에 적용해보아 알 수 있듯, $X$와 $Y$가 $F$-related인지의 여부 또한 마찬가지로 각각의 함수에 적용하여 알아낼 수 있다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $F:M\rightarrow N$이 $C^\infty$ 함수라 하고, $X\in\mathfrak{X}(M)$, $Y\in\mathfrak{X}(N)$이라 하자. 그럼 $X,Y$가 $F$-related인 것은 임의의 $f$에 대하여, 다음의 식

$$X(f\circ F)=(Yf)\circ F$$

이 성립하는 것과 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 점 $p\in M$에 대하여,

$$X(f\circ F)(p)=X_p(f\circ F)=dF_p(X_p)f$$

그리고

$$((Yf)\circ F)(p)=(Yf)(F(p))=Y_{F(p)}f$$

이다. 따라서 주어진 두 조건이 동치이다.

</details>

처음 우리는 $F$가 surjective도 아니고, injective도 아니라면 $F$를 통해 $X\in\mathfrak{X}(M)$과 $F$-related인 $Y\in\mathfrak{X}(N)$을 찾는 것이 자연스럽지 않다는 것을 지적했었는데, $F$가 diffeomorphism이라면 다음과 같이 자연스러운 선택이 존재한다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $F:M\rightarrow N$이 diffeomorphism이라면, 임의의 $X\in\mathfrak{X}(M)$마다 유일한 $Y\in\mathfrak{X}(N)$이 존재하여 $X,Y$가 $F$-related이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $q\in N$마다 유일한 $p\in M$이 존재하여 $F(p)=q$이다. 따라서 각각의 점 $q\in N$마다, $Y$를 다음의 식

$$Y_q=dF_p(X_p)\qquad (F(p)=q)$$

으로 정의해주면 된다. $Y$가 $X$에 $F$-related이기 위해서는 위의 식이 반드시 성립해야 하므로, 이러한 $Y$가 유일하다는 것은 자명하다. 또, $Y:N\rightarrow TN$은 이제 다음 $C^\infty$들의 합성

$$N\overset{F^{-1}}{\longrightarrow}M\overset{X}{\longrightarrow}TM\overset{dF}{\longrightarrow}TN$$

이므로 $Y$는 $C^\infty$이다. 

</details>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $F:M\rightarrow N$이 $C^\infty$라 하자. 만일 $i=1,2$에 대해 $X_i\in\mathfrak{X}(M)$, $Y_i\in\mathfrak{X}(N)$이고 $X_i$와 $Y_i$가 $F$-related라면 $[X_1,X_2]$는 $[Y_1,Y_2]$와 $F$-related이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음의 식

$$dF_p([X_1,X_2]_p)=[Y_1,Y_2]_{F(p)}$$

이 모든 $p$에 대해 성립함을 보여야 한다. 이제 $F(p)$ 근방에서 정의된 임의의 함수 $f$에 대하여,

$$\begin{aligned}dF_p([X_1,X_2]_p)f&=[X_1,X_2]_p(f\circ F)\\
&=(X_1)_p(X_2(f\circ F))-(X_2)_p(X_1(f\circ F))\\
&=(X_1)_p((Y_2f)\circ F)-(X_2)_p((Y_1f)\circ F)\\
&=dF_p(X_1)_p(Y_2f)-dF_p(X_2)_p(Y_1f)\\
&=(Y_1)_{F(p)}(Y_2f)-(Y_2)_{F(p)}(Y_1f)\\
&=[Y_1,Y_2]_{F(p)}f\end{aligned}$$

이므로 원하는 결론을 얻는다.

</details>


## Integral curve

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> Manifold $M$의 $C^\infty$ curve $\sigma$가 $X\in\mathfrak{X}(M)$의 *integral curve*라는 것은 $\sigma'(t)=X(\sigma(t))$가 모든 $t$에 대해 성립하는 것이다.

</div>

다음 정리는 상미분방정식으로부터 쉽게 얻어지는데, 증명 자체는 우리의 관심사에서 벗어나므로 생략하기로 한다. 또, 정리의 4번 항목부터는 약간의 추가적인 정의가 필요하다. 

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> Manifold $M$과 $X\in\mathfrak{X}(M)$을 생각하자. 임의의 $p\in M$이 주어질 때마다, ($\pm\infty$를 포함하는) 적당한 상수 $a(p), b(p)$과 $C^\infty$ curve $\gamma_p: \bigl(a(p),b(p)\bigr)\rightarrow M$이 존재하여 다음 조건들을 만족한다. 

1. $0\in \bigl(a(p),b(p)\bigr)$, $\gamma_p(0)=p$.
2. $\gamma_p$는 $X$의 integral curve이다.
3. 만일 $\mu:(c,d)\rightarrow M$이 위의 두 조건을 만족하는 $C^\infty$ 함수라면 $(c,d)\subset \bigl(a(p),b(p)\bigr)$이고, $\mu$는 $\gamma_p$를 $(c,d)$로 제한한 것과 동일한 함수이다.
4. 각각의 $p\in M$마다 적당한 열린근방 $V$와 양수 $\epsilon$이 존재하여, $(t,p)\mapsto X_t(p)$가 잘 정의되며, 이 함수는 $(-\epsilon,\epsilon)\times V$에서 $M$으로의 $C^\infty$ 함수이다.
5. 임의의 $t$에 대해 $\mathcal{D}_t$가 열린집합이다.
6. $\bigcup\_{t>0}\mathcal{D}_t=M$.
7. $X\_t:\mathcal{D}\_t\rightarrow\mathcal{D}\_{-t}$는 diffeomorphism이고, 그 역함수는 $X\_{-t}$이다.
8. $X_s\circ X_t$의 정의역은 $\mathcal{D}\_{s+t}$에 포함되며, 특히 $s$와 $t$가 같은 부호일 경우 이 함수의 정의역은 정확히 $\mathcal{D}\_{s+t}$와 동일하다. 또, 이 정의역 상에서 $X_s\circ X_t=X\_{t+s}$이다.

</div>

증명은 생략하더라도, 이 정리가 뜻하는 바는 자명하다. 우선 1번과 2번, 3번은 각각의 $p\in M$마다 maximal integral curve를 잡을 수 있으며, 이는 (시작점을 $t=0$으로 고정한다면) 유일하다는 것을 보여준다.

한편 $X_t$들은 다음의 식

$$X_t(p)=\gamma_p(t)$$

으로 정의된 함수들이며, 이 때 $X_t$의 정의역을 

$$\mathcal{D}_t=\left\{p\in M: t\in\bigl(a(m),b(m)\bigr)\right\}$$

으로 나타내기로 한다. 즉 $X_t$는 점 $p$를 받은 후, 이 점이 앞선 조건들에서 정의된 integral curve를 따라 움직인다면 $t$초 후 어디에 있을지를 알려주는 함수이고, $\mathcal{D}_t$는 integral curve를 따라 $t$초만큼 움직일 여유가 있는 점들의 모임이다. 4번과 5번은 다소 기술적인 결과이고, 6번의 경우는 사실 integral curve의 존재성을 다른 방식으로 서술한 것에 불과하다. 7번과 8번의 경우가 흥미로운데, 이는 다음의 정의를 하면 깔끔하게 서술할 수 있다.

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> $X\in\mathfrak{X}(M)$이 *complete*라는 것은 모든 $t$에 대하여 $\mathcal{D}_t=M$이라는 것이다. 이 때, $X_t$들은 $\circ$에 대한 group을 이루는데, 이를 $X$의 *one-parameter group*이라 부른다. 

</div>

만일 $X$가 complete이 아니라면, $X\_t\circ X\_s$와 $X\_{t+s}$는 엄밀하게는 서로 다른 함수가 될 수 있다. 이들의 정의역이 다르기 때문이다. 이럴 경우 $X_t$들의 모임을 *local one-parameter group*이라 부르기도 한다.

## Lie derivative

우리는 $M$ 위에서 정의된 임의의 $C^\infty$ 함수 $f:M\rightarrow\mathbb{R}$을 점 $p$에서 주어진 방향 $v$로 미분하는 방법을 잘 알고 있다. 이는 정의에 의해 단순히 $v(f)$를 계산하는 것에 불과하다. 하지만 임의의 $X\in\mathfrak{X}(M)$이 주어졌을 때, 점 $p$에서 $X$가 $v$ 방향으로 움직일 때의 방향미분을 구하는 것은 쉽지 않다. 이를 위해서는 $X(p+tv)-X(p)$를 계산해야 하는데, $X(p+tv)$는 $T_{p+tv}M$, $X(p)$는 $T_pM$에 속한 원소이기 때문에 이들을 서로 빼는 것이 불가능하다. 

따라서 무엇인가 다른 방법이 필요한데, 방법 중 하나는 $v\in T_pM$ 방향의 방향미분을 생각하는 대신, $v$를 $V\in\mathfrak{X}(M)$으로 대체하는 것이다. 그럼 $V$의 integral curve를 <em_ko>따라</em_ko> $X(p+tv)$를 점 $p$로 옮겨온 후 계산을 할 수 있다.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> $V,W\in\mathfrak{X}(M)$이라 하자. 그럼 $V$에 대한 $W$의 *Lie derivative* $\mathscr{L}_VW$는 각 점 $p$에서 다음의 식

$$(\mathscr{L}_VW)_p=\frac{d}{dt}\bigg|_{t=0} d(X_{-t})_{X_t(p)}(W_{X_t(p)})=\lim_{t\rightarrow 0}\frac{d(X_{-t})_{X_t(p)}(W_{X_t(p)})}{t}$$

으로 정의된 vector field이다.

</div>

앞선 정리에 의해 $X\_t$의 역함수가 $X\_{-t}$이므로, $W\_{X\_t(p)}$를 $d(X_{-t})$를 통해 옮기면 $T\_{X\_{0}(p)}M=T\_pM$의 원소가 된다. 

이 정의를 통해 미분을 실제로 계산하는 것은 복잡하지만, 다행히도 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> $V,W\in\mathfrak{X}(M)$에 대하여 $\mathscr{L}_VW=[V,W]$가 성립한다.

</div>

이에 대한 증명은 나중에 $\mathscr{L}_V$에 대한 성질을 모아 한 번에 처리한다. ([§미분형식, 명제 5](/ko/math/manifold/differential_forms#pp5))



---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---