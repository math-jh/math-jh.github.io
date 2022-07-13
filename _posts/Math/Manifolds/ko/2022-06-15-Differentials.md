---

title: "미분사상"
excerpt: "두 접공간 사이의 미분사상"

lang: ko

categories: [Math / Manifold]
permalink: /ko/math/manifold/differentials
header:
    overlay_image: /assets/images/Manifold/Differentials.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-15
last_modified_at: 2022-06-15
weight: 5

---

우리는 앞서 manifold $M$의 tangent space $T_pM$을 정의하고, 이들의 차원이 원래의 manifold $M$과 동일하다는 것을 보이고, 또 $T_pM$의 자연스러운 basis 또한 정의했다. 이번 글에서 우리는 두 manifold 사이의 함수를 정의하고, 이것이 tangent space에서는 어떠한 방식으로 행동하는지를 살펴본다. 

## 미분다양체 사이의 함수

우리는 manifold $M$의 적당한 열린집합 위에서 정의된 함수 $f:U\rightarrow\mathbb{R}$이 언제 $C^\infty$인지를 정의했었다. ([§미분다양체, 정의 2](/ko/math/manifold/smooth_manifolds#df2)) 한편 우리는 유클리드 공간 사이의 함수가 언제 $C^\infty$인지도 정의했었는데 ([§위상다양체, 표기법](/ko/math/manifold/topological_manifolds#표기법)) 이 둘을 적절히 조합하면 두 manifold 사이의 함수 $F:M\rightarrow N$이 $C^\infty$라는 것을 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 두 manifold $M,N$이 주어졌다 하자. 함수 $F:M\rightarrow N$이 점 $p\in M$에서 $C^\infty$라는 것은, $p$를 포함하는 적당한 coordinate system $(U,\varphi)$와, $F(U)\subset V$인 적당한 coordinate system $(V,\psi)$가 존재하여 $\psi\circ F\circ\varphi^{-1}$이 $C^\infty$인 것이다. 

![smooth_map](/assets/images/Manifold/Differentials-1.png){:width="500px" class="invert" .align-center}
<cap>[Lee], p.34. Fig. 2.2</cap>

만일 $F$가 모든 점에서 $C^\infty$라면 이를 간단히 $C^\infty$ 함수라 한다.

</div>

앞서 manifold에서 $\mathbb{R}$로의 $C^\infty$ 함수를 정의했을 때와 마찬가지로, 이 정의 또한 coordinate system의 선택과 무관하다는 것을 보여야 하지만 이는 기본적으로 [§미분다양체, 정의 2](/ko/math/manifold/smooth_manifolds#df2) 이후에 증명한 것과 똑같기에 생략한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 두 manifold $M,N$이 주어졌다 하자. 만일 $F:M\rightarrow N$이 점 $p\in M$에서 $C^\infty$라면, 이 함수는 $p$에서 연속이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정의 1](#df1)의 상황을 그대로 가정하자. 그럼 우선 유클리드 공간 사이의 함수 $\psi\circ F\circ\varphi^{-1}:\varphi(U)\rightarrow\psi(V)$가 $C^\infty$이다. 이 함수는 미분가능하므로 당연히 연속이다. 그런데 $\varphi$와 $\psi$는 모두 homeomorphism이므로, 

$$F=\psi^{-1}\circ(\psi\circ F\circ\varphi^{-1})\circ\varphi$$

는 연속함수들의 합성이므로 연속이다.

</details>


<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $\operatorname{id}_M:M\rightarrow M$은 당연하게 $C^\infty$ 함수이다. 더 일반적으로, 임의의 열린집합 $U\subset M$에 open submanifold 구조를 주면 ([§미분다양체의 예시들, 정의 3](/ko/math/manifold/examples#df3)) inclusion map $U\hookrightarrow M$은 $C^\infty$ 함수이다. 

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 두 manifold $M,N$에 대하여, $M$의 임의의 점 $p\in M$을 모두 고정된 점 $q\in N$으로 보내는 상수함수는 $C^\infty$이다. 

</div>

이제 우리가 다룰 대상들인 manifold들을 정의했고, manifold들 사이의 함수들을 정의했다. 다음 명제가 성립하는 것을 어렵지 않게 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 세 manifold $M,N,P$에 대하여, 만일 $F:M\rightarrow N$과 $G:N\rightarrow P$가 모두 $C^\infty$라면 이들의 합성 $G\circ F$ 또한 $C^\infty$이다.

</div>

그럼 manifold들 사이의 isomorphism은 다음과 같이 정의해야 한다는 것이 명확하다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 만일 두 manifold $M,N$에 대하여, $F:M\rightarrow N$과 $G:N\rightarrow M$이 각각 존재하여 $G\circ F=\operatorname{id}_M$이고 $F\circ G=\operatorname{id}_N$이라면 $F$와 $G$ 각각을 *diffeomorphism<sub>미분동형사상</sub>*이라 부르고, $F$와 $G$가 *diffeomorphic<sub>미분동형</sub>*이라 말한다.

</div>

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 동일한 topological manifold $M$ 위에 diffeomorphic하지만 서로 같지는 않은 미분구조를 줄 수 있다. 두 미분구조 $\mathcal{A}\_1$, $\mathcal{A}\_2$를 각각 single chart들 $(\mathbb{R},\operatorname{id}\_\mathbb{R})$, $(\mathbb{R}, x\mapsto x^{3})$을 통해 정의하자. 그럼 $\mathcal{A}_1$과 $\mathcal{A}\_2$는 서로 다른 미분구조를 정의한다. ([§미분다양체, 예시 4](/ko/math/manifold/smooth_manifolds#ex4))  
편의상 $(M,\mathcal{A}\_1)$을 $M\_1$, $(M,\mathcal{A}\_2)$를 $M\_2$로 이름붙이고, $\varphi=\operatorname{id}\_\mathbb{R}$, 그리고 $\psi=(x\mapsto x^3)$이라 하자. 

이들 두 manifold $M_1, M_2$는 서로 diffeomorphic하다. $M\_1$에서 $M\_2$로의 함수 $F$를 $x\mapsto x^{1/3}$으로 정의하자. 그럼 자명하게 $F^{-1}$은 $y\mapsto y^3$으로 정의된다. 정의에 의해 $F$는 $C^\infty$이다. 임의의 점 $p\in M_1$에 대하여, $M_1$과 $M_2$ 각각에 정의된 두 coordinate system $(\mathbb{R},\varphi)$와 $(\mathbb{R},\psi)$을 잡으면 $p\in\mathbb{R}$,  $F(\mathbb{R})\subset\mathbb{R}$을 만족하는 것은 자명하고, 또 이들이

$$(\psi\circ F\circ \varphi^{-1})(t)=t$$

을 만족하므로 $\psi\circ\varphi^{-1}$이 $C^\infty$이기 때문이다.  
뿐만 아니라 $F^{-1}$ 또한 $C^\infty$가 되는데, 이는 마찬가지로 임의의 점 $q\in M_2$에 대해 위와 동일한 coordinate system을 잡으면 $q\in\mathbb{R}$이고 $F^{-1}(\mathbb{R})\subset\mathbb{R}$이 성립하며, 또

$$(\psi^{-1}\circ F^{-1}\circ \varphi)(s)=s$$

이 성립하기 때문이다. 

</div>

## 미분사상

Manifold는 기본적으로 미분을 할 수 있는 공간이며, 때문에 manifold 사이의 함수를 알기 위해서는 이 함수가 미분들, 즉 tangent space의 원소들을 어떠한 방식으로 변환시키는지를 알아야 한다. 

두 manifold 사이의 $C^\infty$ 함수 $F:M\rightarrow N$이 주어졌다 하자. 함수 $F$는 자연스럽게 다음의 식

$$g\mapsto g\circ F$$

으로 정의된 함수 $F^\ast:C_{F(p)}^\infty(N)\rightarrow C_p^\infty(M)$을 유도한다. 뿐만 아니라, 임의의 $f,g,\in C_{F(p)}(N)$ 그리고 실수 $\alpha\in\mathbb{R}$에 대하여

$$F^\ast(f+g)=(f+g)\circ F=f\circ F+g\circ F=F^\ast(f)+F^\ast(g),\quad F^\ast(\alpha f)=(\alpha f)\circ F=\alpha(f\circ F)=\alpha F^\ast(f)$$

가 성립하므로 $F^\ast$는 두 $\mathbb{R}$-벡터공간 $C_{F(p)}^\infty(N)$, $C_p^\infty(M)$ 사이의 linear map이다. 

한편, $T_pM$과 $T_{F(p)}N$은 $C_p^\infty(M)$과 $C_{F(p)}^\infty(N)$에서 $\mathbb{R}$로의 linear map들 중 라이프니츠 법칙을 만족하는 원소들이므로, 이들은 각각의 dual space $C_p^\infty(M)^\ast$과 $C_{F(p)}^\infty(N)^\ast$의 부분공간이 된다. 따라서, 위에서 얻은 linear map $F^\ast:C_{F(p)}^\infty(N)\rightarrow C_p^\infty(M)$의 dual map $(F^\ast)^\ast:C_p(M)^\ast\rightarrow C_{F(p)}^\infty(N)^\ast$를 생각할 수 있다. 

![differential](/assets/images/Manifold/Differentials-2.png){:width="220px" class="invert" .align-center}

명시적으로, 이 함수는 임의의 linear map $L\in C_{p}^\infty(M)^\ast$에 대하여

$$(F^\ast)^\ast(L)=L\circ F^\ast$$

으로 정의되는 함수이다. 이제 이 정의를 $T_pM$으로 제한하면 원하는 정의를 얻는다.

그 전에 위의 논의를 벡터공간의 원소들의 입장에서 다시 정리하자면, $(F^\ast)^\ast\|\_{T_pM}$는 임의의 $v\in T_pM$을 $v\circ F^\ast\in C_{F(p)}^\infty(N)^\ast$으로 보낸다. 한편 $v\circ F^\ast$는 $C_{F(p)}^\infty(N)^\ast$의 원소이므로 임의의 $g\in C_{F(p)}^\infty(N)$에 어떻게 작용하는지를 통해 정의되는데, 이는

$$(v\circ F^\ast)(g)=v(F^\ast(g))=v(g\circ F)$$

으로 정의된다. 뿐만 아니라, 이렇게 정의된 $v\circ F^\ast$는 실제로 $T_{F(p)}N$에 속한다. 즉, 라이프니츠 법칙을 만족한다. 이는 다음의 식

$$\begin{aligned}(v\circ F^\ast)(fg)&=v(F^\ast(fg))=v((f\circ F)(g\circ F))\\
&=(f\circ F)(p)v(g\circ F)+(g\circ F)(p) v(f\circ F)\\
&=f(F(p))(v\circ F^\ast)(g)+g(F(p))(v\circ F^\ast)(f)\end{aligned}$$

으로부터 얻어진다. 지금까지의 논의를 정리하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> $F:M\rightarrow N$이 두 manifold 사이의 $C^\infty$ 함수라 하자. 임의의 $p\in M$에 대하여, $F$의 점 $p$에서의 *differential<sub>미분사상</sub>* $dF_p:T_pM\rightarrow T_{F(p)}N$은 임의의 $v\in T_pM$과 임의의 $g\in C_{F(p)}^\infty(N)$에 대하여

$$(dF_p(v))g=v(g\circ F)$$

으로 정의되는 linear map이다.

</div>

정의로부터 몇 가지 결과는 자명하다. 우선 $\operatorname{id}\_M:M\rightarrow M$에 대하여 $d(\operatorname{id}\_M)\_p$는 항상 $T\_pM$에서 $T\_pM$으로의 identity인 $\operatorname{id}\_{T\_pM}$이 된다. 이는 [정의 7](#df7)의 식으로부터 명백하다. 또, 세 manifold $M,N,P$에 대하여 $F:M\rightarrow N$, $G:N\rightarrow P$가 $C^\infty$라면, 다음의 식

$$d(G\circ F)_p=(dG_{F(p)})\circ (dF_p)$$ 

이 성립한다. 이는 differential을 정의할 때 사용한 pullback이 합성을 잘 보존한다는 것으로부터도 자명하고, 혹은 마찬가지로 [정의 7](#df7)의 식에 $G\circ F$를 직접 대입해보아도 된다. 이로부터 diffeomorphism $F$에 대해 $dF_p$는 항상 벡터공간 사이의 isomorphism이 된다는 것 등을 보일 수 있다. 

그러나 differential이 isomorphism이 되는 $C^\infty$ 함수 중 diffeomorphism이 아닌 것은 매우 많다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> Manifold $M$과, $M$의 open submanifold $U$에 대하여, inclusion map $\iota:U\hookrightarrow M$은 모든 $p\in U$에 대하여 tangent space 사이의 isomorphism을 유도한다. 즉, $d\iota_p$가 항상 isomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\iota^\ast$가 $C^\infty_{\iota(p)}(U)$와 $C^\infty_p(M)$ 사이의 isomorphism을 만들기 때문에 자명하다. 사실 처음부터 두 벡터공간은 같은 것으로 보아도 무리가 없다.

</details>

## 접공간의 기저와 미분사상

$\mathbb{R}^m$을 $m$차원 manifold로 본다면, 우리가 tangent vector를 정의한 방식은 정확히 $\mathbb{R}^m$에서의 방향벡터와 동일하다는 것을 알 수 있다. 이 경우, 임의의 $p\in\mathbb{R}^m$에 대하여, 점 $p$를 시점으로 하는 $\mathbb{R}^m$의 표준적인 $m$개의 벡터들이 각자의 방향으로의 방향미분을 정의하며, 우리는 이들을 

$$\frac{\partial}{\partial r^1}\bigg|_p,\cdots,\frac{\partial}{\partial r^m}\bigg|_p$$

으로 적기로 하였다. 일반적인 manifold의 경우 우리는 $p\in M$을 포함하는 coordinate system $(U,\varphi)$를 택한 후, $\varphi$의 성분함수 $x^1,\ldots, x^m$들을 이용하여 tangent vector들을

$$\frac{\partial}{\partial x^1}\bigg|_p,\cdots,\frac{\partial}{\partial x^m}\bigg|_p$$

들로 표현하였다. 이 때, 임의의 $f\in C^\infty_p(M)$에 대하여

$$\frac{\partial}{\partial x^i}\bigg|_pf=\frac{\partial}{\partial r^i}\bigg|_p (f\circ\varphi^{-1})$$

이다. 그런데 [정의 7](#df7)을 염두에 두고 이 식을 다시 살펴보면, 이는 $\varphi^{-1}:\varphi(U)\rightarrow U$의 differential과 동일한 모양임을 알 수 있다.[^1] 즉 tangent space의 basis는 다른 것이 아니라, 단지 $\mathbb{R}^m$의 tangent space $T_{\varphi(p)}\mathbb{R}^m$의 $m$개의 basis들을 differential $d\varphi^{-1}_{\varphi(p)}$를 통해 옮겨온 것일 뿐이다.

이를 좀 더 선형대수학적인 관점에서 보자면, $\mathcal{B}$를 $\mathbb{R}^m$의 standard basis, $\mathcal{C}$를 $\partial/\partial x^i$들로 이루어진 $T_pM$의 basis라 하면 $(T_{\varphi(p)}\mathbb{R}^n, \mathcal{B})$에서 $(T_pM, \mathcal{C})$로의 linear map $d\varphi^{-1}_{\varphi(p)}$의 행렬표현이 정확히 항등행렬이 된다고 할 수 있다.

더 일반적으로, $M,N$이 각각 $m,n$차원의 manifold이고 $F:M\rightarrow N$이 임의의 $C^\infty$ 함수라 하자. 그럼 고정된 $p\in M$에 대하여, $p$를 포함하는 coordinate system $(U,\varphi)$, 그리고 $F(U)$를 포함하는 coordinate system $(V,\psi)$가 존재하여 $\psi\circ F\circ\varphi^{-1}$이 $C^\infty$이다. 이제 $\varphi=(x^i)\_{i=1}^{m}$, $\psi=(y^j)\_{j=1}^n$이라 하자. 그럼 마찬가지로 tangent space $T_pM$, $T_{F(p)}N$의 basis는 각각

$$\frac{\partial}{\partial x^1}\bigg|_p,\cdots,\frac{\partial}{\partial x^m}\bigg|_p,\quad\text{and}\quad\frac{\partial}{\partial y^1}\bigg|_{F(p)},\cdots\frac{\partial}{\partial y^n}\bigg|_{F(p)}$$

으로 주어진다. 이제 이들을 통해 $dF_p$를 행렬로 나타내보자. 이를 위해서는 각각의 $\partial/\partial x^i$들이 $dF_p$를 통해 옮겨지는 벡터를 $\partial/\partial y^j$들의 일차결합으로 표현하면 된다. 즉 

$$dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)=a_{1i}\frac{\partial}{\partial y^1}\bigg|_{F(p)}+\cdots+a_{ni}\frac{\partial}{\partial y^n}\bigg|_{F(p)}$$

의 각 계수들 $a_{ji}$를 구해주면 된다. 그런데 어차피 $\partial/\partial y^j$들은 $\mathfrak{n}/\mathfrak{n}^2$의 원소들 $y^j+\mathfrak{n}^2$의 dual basis이므로, 이를 위해서는 양 변을 함수 $y^j$에 적용해주면 된다.[^2] 즉

$$dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)y^j=a_{1i}\frac{\partial}{\partial y^1}\bigg|_{F(p)}y^j+\cdots+a_{ji}\frac{\partial}{\partial y^j}\bigg|_{F(p)}y^j+\cdots+a_{ni}\frac{\partial}{\partial y^n}\bigg|_{F(p)}y^j$$

에서, dual basis의 정의에 의해 우변은 오직 $a_{ji}$만 남게 되므로

$$dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)y^j=a_{ji}$$

이고 이로부터 $dF_p$의 두 basis $\partial/\partial x^i$, $\partial/\partial y^j$들에 대한 행렬표현이 다음의 행렬

$$\begin{pmatrix}\partial(y^1\circ F)/\partial x^1&\partial(y^1\circ F)/\partial x^2&\cdots&\partial(y^1\circ F)/\partial x^m\\\partial(y^2\circ F)/\partial x^1&\partial(y^2\circ F)/\partial x^2&\cdots&\partial(y^2\circ F)/\partial x^m\\\vdots&\vdots&\ddots&\vdots\\\partial(y^n\circ F)/\partial x^1&\partial(y^n\circ F)/\partial x^2&\cdots&\partial(y^n\circ F)/\partial x^m\end{pmatrix}$$

인 것을 알 수 있다. 즉, 이는 단지 유클리드 공간 사이의 함수 $\psi\circ F\circ\varphi^{-1}$의 Jacobian에 불과하다. 

특별히 $M=N$이고 $F=\operatorname{id}_M$이지만 서로 다른 coordinate system $(U, \varphi)$와 $(V,\psi)$를 택한 경우, 이는 transition map $\psi\circ\varphi^{-1}$의 Jacobian matrix가 될 것이다. 

마지막으로 간단한 명제를 하나 소개하고 이 글을 끝마친다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Connected manifold $M$ 위에서 정의된 $C^\infty$함수 $F:M\rightarrow N$이 주어졌다 하자. 만일 임의의 $p\in M$에 대하여 $dF_p$가 zero map이라면 $F$는 상수함수이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $q\in F(M)$을 고르자. 그럼 $F^{-1}(q)$가 공집합이 아닌 닫힌집합임은 자명하다. $F$가 상수함수이려면 $F^{-1}(q)=M$이어야 하는데, $M$이 connected이므로 이를 위해서는 $F^{-1}(q)$가 열린집합이라는 것을 보이면 충분하다.

임의의 $p\in F^{-1}(q)$를 고르자. 그럼 $p$를 포함하는 coordinate system $(U,\varphi)$와 $F(U)$를 포함하는 coordinate system $(V,\psi)$가 존재한다. $\varphi=(x^i)$, $\psi=(y^j)$라 하면, 임의의 $p\in U$에 대하여

$$0=dF_p\left(\frac{\partial}{\partial x^i}\bigg|_p\right)=\sum_{j=1}^n\frac{\partial(y^j\circ F)}{\partial x^i}\frac{\partial}{\partial y^j}\bigg|_F(p)$$

이 성립한다. 이제 $\partial/\partial y^j$들은 linearly independent이므로, 임의의 $p\in U$에 대하여 항상

$$\frac{\partial(y^j\circ F)}{\partial x^i}(p)=0$$

이 성립한다. 이들은 $\psi\circ F\circ\varphi^{-1}$의 Jacobian이므로, 유클리드 공간 사이의 함수 $\psi\circ F\circ\varphi^{-1}$는 상수함수이고, 특히 점 $\varphi^{-1}(p)$가 $\psi(q)$로 옮겨지므로 $\psi\circ F\circ\varphi^{-1}$은 모든 점을 $\psi(q)$로 보내는 상수함수이다. 따라서 $F$는 $U$의 모든 점을 $q$로 보내는 상수함수가 되어 $U\subset F^{-1}(q)$이고 $F^{-1}(q)$는 열린집합이다.

</details>


---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---

[^1]: 물론 이를 위해서는 $\varphi^{-1}$가 $C^\infty$여야 하지만, 애초부터 $U$에서의 미분구조 자체가 $\varphi(U)$의 미분구조를 옮겨놓은 것이기 때문에 $\varphi^{-1}$는 심지어 diffeomorphism이다.
[^2]: 편의상 $\psi(F(p))=0$이라 가정하였다.