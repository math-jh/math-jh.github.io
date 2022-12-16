---

title: "리 미분"
excerpt: "리 미분과 리 브라켓"

categories: [Math / Manifold]
permalink: /ko/math/manifold/Lie_derivative
header:
    overlay_image: /assets/images/Manifold/Lie_derivative.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-12-16
last_modified_at: 2022-12-16
weight: 12

---

## 함수의 방향미분과 리 미분

Manifold $M$ 위에서 정의된 함수 $f$를 생각하자. 정의에 의하여 점 $p\in M$에서 $v\in T_pM$ 방향으로의 $f$의 방향미분은 $v(f)$와 같다. 우리가 $M$ 위에서 <em_ko>일반적인</em_ko> 미분

$$\lim_{t \rightarrow0}\frac{f(p+tv)-f(p)}{t}$$

을 사용하지 못하는 가장 큰 이유는 $p+tv$가 정의되지 않기 때문이다. 그러나 만일 $M$ 위에 적당한 $C^\infty$ 곡선 $\gamma$가 주어졌다고 하고, $\gamma(0)=p$, $\gamma'(0)=v$라 한다면 다음 식

$$\lim_{h\rightarrow 0}\frac{f(\gamma(h))-f(p)}{h}\tag{1}$$

을 통해 방향미분의 값을 구해낼 수 있다는 것을 알고 있다. ([§미분사상의 예시들, 정의 1](/ko/math/manifold/examples_of_differentials#df1)) 

이제 $M$ 위에 벡터장 $X$가 주어졌다 하고, 각 점 $p$에서 $X_p$ 방향으로의 방향미분 $X_pf$를 구하는 문제를 생각해보자. 이는 기하학적으로는 위와 같이 모든 점 $p$마다 $\gamma(0)=p$, $\gamma'(0)=X_p$를 만족하는 곡선 $\gamma_p$를 잡아 위의 식 (1)을 적용하는 것과 같다. 그런데 우리는 이러한 성질을 만족하는 곡선이 반드시 존재한다는 것을 알고 있다. ([§벡터장, 정리 6](/ko/math/manifold/vector_fields#thm6))

<div class="definition" markdown="1">
 
<ins id="df1">**정의 1**</ins> Manifold $M$과 그 위에 정의된 벡터장 $X$를 고정하고, 함수 $f:M\rightarrow\mathbb{R}$이 주어졌다 하자. 그럼 $f$의 *Lie derivative<sub>리 미분</sub>* $\mathcal{L}_Xf$는 다음의 식

$$(\mathcal{L}_Xf)(p)=\lim_{t\rightarrow 0}\frac{f(\phi^t(p))-f(\phi^0(p))}{t}=\lim_{t\rightarrow 0}\frac{f(\phi^t(p))-f(p)}{t}$$

으로 정의되는 함수이다.

</div> 

물론 앞선 논증에 의해 이는 방향미분 $X_pf$와 다를 것이 없다. 그러나 여기에서 사용한 $\phi^t$는 단순히 함수가 아니라, $M$ 위에 정의된 다른 모든 것들을 미분하는 방식을 제공해준다.

## 벡터장의 리 미분

가장 간단한 예시는 벡터장의 미분이다. 벡터장 $Y$는 $M$에서 $TM$으로의 함수이므로, 위의 [정의 1](#df1)과 유사한 방법을 사용하여 미분을 시도해볼 수 있으나 이는 만만한 일이 아니다. 여기에는 함수의 미분보다 조금 더 근본적인 문제가 있는데, $Y(\phi^t(p))$는 $T_{\phi^t(p)}$의 원소인 반면 $Y(p)$는 $T_pM$의 원소이므로 이들 둘의 차 $Y_{\phi^t(p)}-Y_p$를 계산하는 방법이 애초부터 없기 때문이다. 

그럼에도 불구하고 우리 상황에서는 이를 미분하는 것이 가능하다. [§벡터장, 정리 6](/ko/math/manifold/vector_fields#thm6)을 생각하면 $\phi^t$는 diffeomorphism이므로, $d\phi^t$는 $T_pM$에서 $T_{\phi^t(p)}$으로의 isomorphism을 유도한다. 또, 같은 정리에서 이 isomorphism의 역함수는 $d\phi^{-t}$라는 것 또한 안다. 따라서 $Y_{\phi^t(p)}$를 $d\phi^{-t}$를 통해 $T_pM$으로 가져오면 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Manifold $M$과 그 위에 정의된 벡터장 $X$를 고정하고, 또 다른 벡터장 $Y:M\rightarrow TM$이 주어졌다 하자. 그럼 $Y$의 *Lie derivative* $\mathcal{L}_XY$는 다음의 식

$$(\mathcal{L}_XY)_p=\lim_{t\rightarrow 0}\frac{(d\phi^{-t})_{\phi^t(p)}(Y_{\phi^t(p)})-Y_p}{t}$$

으로 정의된 벡터장이다.

</div>

## 미분형식의 리 미분

물론 이와 같은 방식으로 계속 정의해나갈 수 있다. 예를 들어 다음은 미분형식을 벡터장 $X$에 대해 미분하는 방법이다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Manifold $M$과 그 위에 정의된 벡터장 $X$를 고정하고, differential form $\omega\in\Omega^\ast(M)$이 주어졌다 하자. 그럼 $\omega$의 *Lie derivative* $\mathcal{L}_X\omega$는 다음의 식

$$(\mathcal{L}_X\omega)_p=\frac{d}{dt}\bigg|_{t=0}(\phi^t)^\ast\omega_{\phi^t(p)}=\lim_{t\rightarrow 0}\frac{(\phi^t)^\ast\omega_{\phi^t(p)}-\omega_p}{t}$$

으로 정의된 differential form이다.

</div>

뿐만 아니라, 어렵지 않게 임의의 tensor field로도 이 정의를 확장할 수 있다. 특히 Riemannian metric 또한 잘 정의된 Lie derivative를 가질 것이다. 그러나 이는 우리가 사용할 내용은 아니므로 넘기기로 한다.

다음 명제의 일부는 이미 증명하였던 것이고, 일부는 새로운 것이지만 증명을 모두 적기에는 길기 때문에 생략한다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 임의의 $X\in\mathfrak{X}(M)$에 대해 다음이 성립한다.

1. 임의의 $f\in C^\infty(M)$에 대하여 $\mathcal{L}_Xf=X(f)$.
2. 임의의 $Y\in \mathfrak{X}(M)$에 대하여 $\mathcal{L}_XY=[X,Y]$.
3. $\mathcal{L}_X$는 $\Omega^\ast(M)$에서 $\Omega^\ast(M)$으로의 derivation이며, $d$와 commute한다.
4. $\mathcal{L}_X=\iota_X\circ d+d\circ\iota_X$.
5. 임의의 $\omega\in\Omega^k(M)$과 $X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$에 대하여
    
    $$\mathcal{L}_{X_0}(\omega(X_1,\ldots, X_k))=(\mathcal{L}_{X_0}\omega)(X_1,\ldots, X_k)+\sum_{i=1}^k\omega(X_1,\ldots, X_{i-1}, \mathcal{L}_{X_0}X_i,X_{i+1},\ldots, X_k)$$

6. 임의의 $\omega\in\Omega^k(M)$과 $X_0, X_1,\ldots, X_k\in\mathfrak{X}(M)$에 대하여

    $$\begin{aligned}d\omega(X_0,\ldots, X_k)&=\sum_{i=0}^k(-1)^iX_i\omega(X_0,\ldots, \hat{X}_i,\ldots, X_k)\\&\phantom{==}+\sum_{i<j}(-1)^{i+j}\omega([X_i, X_j], X_0,\ldots, \hat{X}_i,\ldots, \hat{X}_j,\ldots, X_k)\end{aligned}$$

5번과 6번에서, hat은 주어진 성분이 생략되었음을 의미한다.

</div>

이 명제의 첫 번째 결과는 우리가 이미 확인한 내용이다. 두 번재 결과와 여섯 번째 결과에서 나오는 $[-,-]$는 *Lie bracket*이라 불리는 벡터장들 사이의 연산인데, 이에 대한 내용은 이번 글에서는 간략하게만 다루고 자세한 내용은 다음 글에서 다룬다. 어쨌든 둘째, 다섯째, 여섯째 결과의 핵심은 $\mathcal{L}_X$를 계산할 때, 원래의 정의를 따르는 대신 상대적으로 간단한 대수적인 계산만을 통해 Lie derivative를 구할 수 있다는 것이다. 네 번째 결과는 Cartan's formula라는 이름으로 알려져 있다.

## Lie Bracket

$\mathfrak{X}(M)$은 일반적인 설정에서 $C^\infty(M)$-algebra가 되지는 않는다. $(XY)(fg)$를 직접 계산해보면,

$$(XY)(fg)=X(f(Yg)+g(Yf))=(Xf)(Yg)+f(XY)g+(Xg)(Yf)+g(XY)f\tag{2}$$

이 된다는 것을 확인할 수 있다. 바꾸어 말하자면 $XY$가 라이프니츠 법칙을 만족하지 못하도록 하는 것은 두 개의 항 $(Xf)(Yg)$와 $(Xg)(Yf)$이며, 따라서 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $X,Y\in\mathfrak{X}(M)$에 대하여, $[X,Y]\in\mathfrak{X}(M)$은 다음의 식

$$[X,Y]f=X(Yf)-Y(Xf)$$

으로 정의되는 원소이다.

</div>

물론 이 정의가 말이 되기 위해서는 우변의 식이 실제로 $\mathfrak{X}(M)$의 원소가 된다는 것을 확인해야 하지만, 이는 위에서 계산한 식 (2)에서 $X$와 $Y$의 정의를 바꾸어 $(YX)(fg)$를 얻은 후, 이를 빼면 된다. 애초부터 이 정의는 문제가 되는 두 항을 소거하기 위한 정의였으므로 당연히 라이프니츠 법칙이 성립할 것이다.

이렇게 정의된 벡터장 $[X,Y]$를 $X$와 $Y$의 *Lie bracket*이라 부른다. 이 정의는 나중에 아주 중요하게 쓰이므로, 몇 가지 결과를 미리 정리해 두는 것이 좋아보인다.

두 manifold $M,N$ 사이의 $C^\infty$ 함수 $F:M\rightarrow N$이 주어졌다 하자. 그럼 $dF_p:T_pM\rightarrow T_{F(p)}N$은 $M$의 한 점 $p$에서 정의된 tangent vector $v$를 $N$의 한 점 $F(p)$에서 정의된 tangent vector $dF_p(v)$로 보내주는 함수이다. 그러나 일반적으로 이것이 벡터장에 대해 가능할 필요는 없다. 즉, $M$ 위에서 정의된 벡터장 $X$가 주어져 있다 하여, 이를 $dF_p$ 등을 통해 $N$ 위에서 정의된 벡터장을 만들 수 없다. 

예컨대 $F$가 전사가 아니라면, $F$의 상에 속하지 않는 점 $q\in N$에서의 tangent vector를 대응시키는 방법이 자연스럽게 존재하지 않는다. 이는 치역을 제한하는 등의 방식으로 해결한다 치더라도, 만일 $F$가 단사가 아니고 $F(p_1)=F(p_2)=q\in N$라면, 이 공통의 점 $q$에서의 tangent vector를 $dF\_{p\_1} v\_1$과 $dF\_{p\_2} v\_2$ 중 어떤 것을 택해야 할지도 정해야 한다.

때문에 $X\in\mathfrak{X}(M)$을 $F$를 통해 움직이려 하기보다는 이미 주어진 $Y\in\mathfrak{X}(N)$이 원하는 성질을 만족하는 경우를 살펴보는 편이 현명하다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $F:M\rightarrow N$이 $C^\infty$ 함수라 하자. 만일 $X\in\mathfrak{X}(M)$과 $Y\in\mathfrak{X}(N)$이 다음의 식

$$dF_p(X_p)=Y_{F(p)}$$

을 모든 $p\in M$에 대해 만족한다면, $X$와 $Y$가 *$F$-related*되어있다고 부른다.

</div>

즉, $X$와 $Y$가 $F$-related라는 것은 다음의 diagram이 commute한다는 것이다.

![F-related](/assets/images/Manifold/Lie_derivative-1.png){:width="160px" class="invert" .align-center}

[명제 2](#pp2)에서 $X$가 $C^\infty$임을 각각의 함수 $f$에 적용해보아 알 수 있듯, $X$와 $Y$가 $F$-related인지의 여부 또한 마찬가지로 각각의 함수에 적용하여 알아낼 수 있다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $F:M\rightarrow N$이 $C^\infty$ 함수라 하고, $X\in\mathfrak{X}(M)$, $Y\in\mathfrak{X}(N)$이라 하자. 그럼 $X,Y$가 $F$-related인 것은 임의의 $f$에 대하여, 다음의 식

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

처음 우리는 $F$가 전사도, 단사도 아니라면 $F$를 통해 $X\in\mathfrak{X}(M)$과 $F$-related인 $Y\in\mathfrak{X}(N)$을 찾는 것이 자연스럽지 않다는 것을 지적했었는데, $F$가 diffeomorphism이라면 다음과 같이 자연스러운 선택이 존재한다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $F:M\rightarrow N$이 diffeomorphism이라면, 임의의 $X\in\mathfrak{X}(M)$마다 유일한 $Y\in\mathfrak{X}(N)$이 존재하여 $X,Y$가 $F$-related이도록 할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $q\in N$마다 유일한 $p\in M$이 존재하여 $F(p)=q$이다. 따라서 각각의 점 $q\in N$마다, $Y$를 다음의 식

$$Y_q=dF_p(X_p)\qquad (F(p)=q)$$

으로 정의해주면 된다. $Y$가 $X$에 $F$-related이기 위해서는 위의 식이 반드시 성립해야 하므로, 이러한 $Y$가 유일하다는 것은 자명하다. 또, $Y:N\rightarrow TN$은 이제 다음 $C^\infty$ 함수들의 합성

$$N\overset{F^{-1}}{\longrightarrow}M\overset{X}{\longrightarrow}TM\overset{dF}{\longrightarrow}TN$$

이므로 $Y$는 $C^\infty$이다. 

</details>

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $F:M\rightarrow N$이 $C^\infty$라 하자. 만일 $i=1,2$에 대해 $X_i\in\mathfrak{X}(M)$, $Y_i\in\mathfrak{X}(N)$이고 $X_i$와 $Y_i$가 $F$-related라면 $[X_1,X_2]$는 $[Y_1,Y_2]$와 $F$-related이다.

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

$\mathfrak{X}(M)$은 