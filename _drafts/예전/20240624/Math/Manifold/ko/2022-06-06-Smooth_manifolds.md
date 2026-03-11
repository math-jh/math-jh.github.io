---

title: "미분다양체"
excerpt: "Smooth manifold의 정의"

categories: [Math / Manifold]
permalink: /ko/math/manifold/smooth_manifolds
header:
    overlay_image: /assets/images/Math/Manifold/Smooth_manifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-06
last_modified_at: 2022-06-06
weight: 1

---

우리는 위상수학에서 위상다양체의 개념을 정의했는데, 이 글타래에서는 미분다양체, 그 중에서도 특히 매끄러운 다양체를 다룬다.

## 표기법

앞으로 $m$차원의 좌표계를 다룰 일이 많으므로 다음과 같이 표기법을 고정하기로 한다. $\mathbb{R}^m$에 대하여, $i$번째 projection $\pr_i$를 $r^i$로 표기한다. 비슷하게, 임의의 집합 $X$와 함수 $f:X\rightarrow\mathbb{R}^m$에 대하여, $f$의 $i$번째 *성분함수*는 식 $f^i=r^i\circ f$으로 정의된다. 

이제 함수 $f$가 $\mathbb{R}^m$에서 $\mathbb{R}$로의 함수라 하자. 그럼 $f$의 $i$번째 성분에 대한 편미분을 다음의 식

$$\frac{\partial}{\partial r^i}\bigg|_t f=\frac{\partial f}{\partial r^i}\bigg|_t=\lim_{h\rightarrow 0}\frac{f(t^1,\ldots, t^{i-1}, t^i+h, t^{i+1},\ldots, t^m)-f(t^1,\ldots, t^m)}{h}$$

으로 정의하기로 한다. 위의 표기법과 같이, **[Lee]**의 표기를 따라 $i$번째 성분을 $x_i$ 대신 $x^i$로 적기로 한다.

만일 각각의 성분함수들이 $k$번 미분가능하고, 그 결과가 연속이라면 함수 $f$가 $C^k$라 부른다. 예를 들어 함수 $f:\mathbb{R}^2\rightarrow\mathbb{R}$이 $C^2$라는 것은 다음의 편미분들

$$\frac{\partial^2 f}{\partial x^2},\quad\frac{\partial^2 f}{\partial x\partial y},\quad\frac{\partial^2 f}{\partial y\partial x},\quad\frac{\partial^2 f}{\partial y^2}$$

이 모두 존재하고 연속인 것이다. 함수 $f$가 모든 자연수 $k$에 대하여 $C^k$라면 이를 $C^\infty$라 부른다.

## 미분다양체

일반적인 위상공간과 달리, topological manifold는 국소적으로 $\mathbb{R}^n$과 닮아 있으므로, 여기에서 정의된 미분의 개념을 $M$으로 가져올 수 있다. 이것이 가능한 이유는 미분가능성이 본질적으로는 국소적인 성질이기 때문이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Topological manifold $M$이 주어졌다 하자. $0\leq k\leq\infty$에 대해, coordinate chart들 $(U,\varphi)$와 $(V,\psi)$가 *$C^k$-compatible*인 것은 두 *transition map*들 

$$\psi\circ\varphi^{-1}:\varphi(U\cap V)\rightarrow\psi(U\cap V),\qquad\varphi\circ\psi^{-1}:\psi(U\cap V)\rightarrow\varphi(U\cap V)$$

가 모두 $C^k$인 것이다. $C^k$-compatible한 chart들의 모임 $\mathcal{A}=\\{(U\_\lambda, \varphi\_\lambda)\\}\_{\lambda\in\Lambda}$이 $M=\bigcup U_\lambda$을 만족한다면 $\mathcal{A}$를 *$C^k$-atlas*라 부른다. 

$M$ 위에 정의된 $C^k$-atlas 중, 포함관계에 대해 maximal인 atlas를 *$C^k$-differentiable structure<sub>$k$급 미분구조</sub>*라 부르고, 이 때 $M$을 *$C^k$-differentiable manifold<sub>$k$급 미분다양체</sub>*라 부른다. 특별히 $k=\infty$인 경우 이 구조를 *smooth differentiable manifold<sub>매끄러운 미분다양체</sub>* 혹은 더 간단히 *differentiable manifold<sub>미분다양체</sub>*라 부른다.

</div>

이 정의에서 *maximal* atlas가 미분구조를 주는 것으로 생각하는 이유는 maximal atlas가 아닌 두 atlas가 본질적으로 같은 미분구조를 주는 것이 얼마든 가능하기 때문이다. 예를 들어 $\mathbb{R}$은 다음의 $C^\infty$-atlas 

$$\mathcal{A}=\{(\mathbb{R}, \id_\mathbb{R})\}$$

도 갖지만, 또 다른 atlas 

$$\mathcal{A}'=\{((-\infty, 1), \id_{(-\infty, 1)}), ((-1, \infty),\id_{(-1,\infty)})\}$$ 

또한 갖는다. 그러나 [명제 3](#prop3)에서 확인할 수 있듯, 임의의 atlas가 주어진다면 이를 포함하는 maximal atlas가 유일하게 결정되므로 본질적인 의미에서 이는 그렇게 큰 차이는 아니다.

한편, 수학에서 어떠한 대상을 알기 위해서는 이 대상 위에 정의된 함수를 알면 된다. 앞으로 모든 manifold는 smooth differentiable manifold인 것으로 생각한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Manifold $M$과 한 점 $p\in M$을 생각하자. $p$의 적당한 열린근방에서 정의된 함수 $f$가 $p$에서 $C^\infty$이라는 것은 $p$를 포함하는 어떤 coorinate chart $(U,\varphi)$에 대하여, 함수 $f\circ\varphi^{-1}:U'\rightarrow \mathbb{R}$이 점 $\varphi(p)$에서 $C^\infty$인 것이다.

</div>

점 $p$의 또 다른 열린근방에서 coordinate chart $(V,\psi)$가 정의되었다 하자. 만일 $f\circ\varphi^{-1}$이 $\varphi(p)$에서 $C^\infty$이지만 $f\circ\psi^{-1}$은 $\psi(p)$에서 그렇지 않다면 이 정의는 좋은 정의가 아니다. 그러나 $\psi(U\cap V)$에서

$$f\circ\psi^{-1}=(f\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

이므로 $f\circ\psi^{-1}$은 점 $\psi(p)$에서 $C^\infty$이다. 이와 비슷한 논증을 통해 다음을 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Topological manifold $M$ 위에 $C^k$-atlas $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$를 포함하는 maximal $C^k$-atlas가 유일하게 존재한다. 따라서 임의의 $C^k$-atlas $\mathcal{A}$는 $M$ 위에 유일한 $C^k$-differentiable structure를 정의한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{A}'$를 다음의 식

$$\mathcal{A}'=\{(V,\psi)\mid\psi\circ\varphi_\lambda^{-1}, \varphi_\lambda\circ\psi^{-1}\text{ are $C^k$ for all $\varphi_\lambda\in\mathcal{A}$}\}$$

으로 정의하면 된다. 그럼 $\mathcal{A}'$는 $\mathcal{A}$를 포함하고, 따라서 $M$을 coordinate chart들로 덮을 수 있다. 한편, $(V,\psi)$, $(V',\psi')$가 $\mathcal{A}'$의 원소들이고 $V\cap V'\neq\emptyset$이라면 transition map

$$\psi'\circ\psi^{-1}:\psi(V\cap V')\rightarrow\psi'(V\cap V')$$

는 $C^k$이다. 임의의 $p\in\psi(V\cap V')$에 대하여, $p\in U$를 만족하는 $(U,\varphi)\in\mathcal{A}$를 뽑아오면 $U\cap V\cap V'$ 위에서

$$\psi'\circ\psi^{-1}=(\psi'\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

가 되어 $\psi'\circ\psi^{-1}$가 점 $p$에서 $C^k$이기 때문이다. 점 $p$는 임의로 택한 점이므로, 이것이 $\psi'\circ\psi^{-1}$이 $C^k$임을 보여준다. 물론 $(V,\psi)$와 $(V',\psi')$의 역할을 바꾸면 반대방향 transition map 또한 $C^k$임을 보일 수 있다. 

당연히 정의에 의해 $\mathcal{A}'$는 maximal $C^k$-atlas가 되고, 이는 유일함을 쉽게 확인할 수 있다. 

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 실수집합 $\mathbb{R}$ 위에 두 개의 atlas

$$\mathcal{A}_1=\{(\mathbb{R},\id_\mathbb{R})\},\qquad \mathcal{A}_2=\{(\mathbb{R}, x\mapsto x^3)\}$$

를 주자. 이들은 하나의 chart로 이루어진 atlas들이므로 당연히 $C^\infty$이다. 앞선 [명제 3](#prop3)에 의하여 이들 각각을 포함하는 미분구조가 존재한다. 그러나 이들은 서로 같지 않다. 두 chart $(\mathbb{R},\id_\mathbb{R})$과 $(\mathbb{R}, x\mapsto x^3)$이 서로 $C^\infty$-compatible이 아니기 때문이다. ($x\mapsto x^3$은 $C^\infty$ 함수지만, 그 역함수 $x\mapsto x^{1/3}$은 그렇지 않다)

</div>

다만, [예시 4](#ex4)의 두 atlas는 서로 <em_ko>같은</em_ko> 미분구조를 주지는 않더라도, 서로 *diffeomorphic*한 미분구조를 준다. 

## Smooth partition of unity

임의의 topological manifold에서는 continuous partition of unity가 존재한다는 것을 보일 수 있었는데, differentiable manifold를 다룰 때는 연속인 partition of unity는 별 도움이 되지 않는다. 가령 임의의 $C^\infty$ 함수를 연속이기만 한 partition of unity와 곱한다면 이 함수의 미분가능한 정도가 바로 약화될 것이다.

따라서 우리는 smooth partition of unity를 만들어야 하는데, 이는 다음의 보조정리만 보이면 충분하다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5 ($C^\infty$ Urysohn lemma)**</ins> 실수 $a'&lt;a&lt;b&lt;b'$가 주어졌다 하자. 그럼 $[a,b]$ 위에서는 $1$이고, $(a',b')$ 바깥에서는 $0$인 $C^\infty$ 함수 $\psi:\mathbb{R}\rightarrow[0,1]$이 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

일반성을 잃지 않고 $a'=-2,a=-1,b=1,b'=2$로 두어도 된다. 우선 함수 $f$를 

$$f(t)=\begin{cases}e^{-1/t}&t>0\\0&t\leq 0\end{cases}$$

으로 두자. 그럼 특히 $f$는 항상 음이 아니며, $C^\infty$가 된다. 이제

$$g(t)=\frac{f(t)}{f(t)+f(1-t)}$$

으로 정의하면 $g$는 마찬가지로 항상 음이 아니며, 그 값은 항상 1보다 작거나 같고 특히 $t\geq 1$인 경우 함수값이 항등적으로 1, $t\leq 0$인 경우 함수값이 항등적으로 0이 된다. 따라서 $\psi$를 다음의 식

$$\psi(t)=g(t+2)g(2-t)$$

으로 정의하면 된다.

</details>

일반적인 Urysohn lemma 대신 위의 $C^\infty$ Urysohn lemma를 사용하면 differentiable manifold 위에서의 smooth partition of unity를 만들 수 있다. 

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---