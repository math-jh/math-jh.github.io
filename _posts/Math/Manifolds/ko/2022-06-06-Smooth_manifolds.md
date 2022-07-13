---

title: "미분다양체"
excerpt: "Smooth manifold의 정의"

lang: ko

categories: [Math / Manifold]
permalink: /ko/math/manifold/smooth_manifolds
header:
    overlay_image: /assets/images/Manifold/Smooth_manifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-06
last_modified_at: 2022-06-06
weight: 2

---

현대수학에는 여러가지 철학이 있지만, 대부분의 분야에서 공통적으로 나타나는 것은

> 수학적인 대상을 알기 위해서는, 그 대상 위에 정의된 함수를 살펴보면 된다.

는 것이다. 예를 들어 어떠한 위상공간이 주어졌을 때, 이 위상공간의 성질은 위상공간 위에서 정의된 연속함수들을 이용해 설명할 수 있고, 벡터공간과 같은 경우에는 아예 그 쌍대공간을 떼어놓고는 설명하기가 힘들 정도이다. 마찬가지로 미분다양체의 성질을 알기 위해서는 이 위에 정의된 미분가능한 함수들에 대해 알아야 한다.

## 미분다양체

이를 위해서는 우선 differentiable manifold 위에 미분구조가 어떠한 식으로 주어졌는지를 알아야 한다. 물론 일반적인 위상공간에서 미분을 정의하는 것은 쉬운 일이 아니다. 하지만 일반적인 위상공간과 달리, topological manifold는 국소적으로 $\mathbb{R}^n$과 닮아 있으므로, 여기에서 정의된 미분의 개념을 $M$으로 가져올 수 있다. ([정의 3](#df3)) 이것이 가능한 이유는 미분가능성이 본질적으로는 국소적인 성질이기 때문이다. 

힌퍈, 도입부에서 우리는 간단히 미분가능이라는 말로 뭉뚱그렸지만, 미분가능성에도 일종의 미분가능한 정도가 정의된다는 것을 잘 알고 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Topological manifold $M$이 주어졌다 하자. $0\leq k\leq\infty$에 대해, coordinate chart들 $(U,\varphi)$와 $(V,\psi)$가 *$C^k$-compatible*인 것은 두 *transition map*들 

$$\psi\circ\varphi^{-1}:\varphi(U\cap V)\rightarrow\psi(U\cap V),\qquad\varphi\circ\psi^{-1}:\psi(U\cap V)\rightarrow\varphi(U\cap V)$$

가 모두 $C^k$인 것이다.[^1] $C^k$-compatible한 chart들의 모임 $\mathcal{A}=\\{(U\_\lambda, \varphi\_\lambda)\\}\_{\lambda\in\Lambda}$이 $M=\bigcup U_\lambda$을 만족한다면 $\mathcal{A}$를 *$C^k$-atlas*라 부른다. 

$M$ 위에 정의된 $C^k$-atlas 중, 포함관계에 대해 maximal인 atlas를 *$C^k$-differentiable structure<sub>$k$급 미분구조</sub>*라 부르고, 이 때 $M$을 *$C^k$-differentiable manifold<sub>$k$급 미분다양체</sub>*라 부른다. 특별히 $k=\infty$인 경우 이 구조를 *smooth differentiable manifold<sub>매끄러운 미분다양체</sub>* 혹은 더 간단히 *differentiable manifold<sub>미분다양체</sub>*라 부른다.

</div>

위에서 정의한 것과 같이, manifold를 다룰 때 우리는 *미분가능*이라는 말을 $C^\infty$와 동일한 말로 사용하지만, 혼동을 피하기 위해 $C^\infty$ 함수는 그대로 $C^\infty$라는 말로 표현하기로 한다. 또, 앞으로는 topological manifold를 다룰 일이 거의 없으므로, differentiable manifold를 더 간단히 *manifold*로 줄여 쓰기도 한다.

앞서 말했듯 *differentiable* manifold의 성질을 알기 위해서는 이 위에 정의된 미분가능한 함수를 알면 된다. 이들은 다음과 같이 정의된다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> Manifold $M$과 한 점 $p\in M$을 생각하자. $p$의 적당한 열린근방에서 정의된 함수 $f$가 $p$에서 $C^\infty$하다는 것은 $p$를 포함하는 어떤 coorinate chart $(U,\varphi)$에 대하여, 함수 $f\circ\varphi^{-1}:U'\rightarrow \mathbb{R}$이 점 $\varphi(p)$에서 $C^\infty$인 것이다.

</div>

위의 두 정의들에 대해 언급할 것들이 있다. 

우선 [정의 2](#df2)의 경우, 이 정의가 잘 정의되었는지를 살펴볼 필요가 있다. 예컨대 $p$의 또 다른 열린근방에서 coordinate chart $(V,\psi)$가 정의되었을 때, $f\circ\varphi^{-1}$이 점 $\varphi(p)$에서 $C^\infty$인 것과 $f\circ\psi^{-1}$이 점 $\psi(p)$에서 $C^\infty$인 것이 동치여야 한다. 이는 정확히 $M$에 주어진 differentiable structure 덕분에 성립한다. 예컨대 $f\circ\varphi^{-1}$이 점 $\varphi(p)$에서 미분가능하다 하자. 그럼 $\psi(p)$를 포함하는 열린근방 $\psi(U\cap V)$로 함수 $f\circ\psi^{-1}$을 제한해주면[^2], 이 위에서

$$f\circ\psi^{-1}=(f\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

이 되어, 함수 $f\circ\psi^{-1}$은 두 $C^\infty$ 함수들의 합성이 되고 따라서 $C^\infty$이다. 

[정의 1](#df1)의 조건 $M=\bigcup U_\lambda$는 이와 같은 일이 $M$ 전체에서 가능하고, 따라서 $M$ 위의 임의의 점에서의 미분가능성을 정의할 수 있게 해 준다. 이 정의에서 덜 명확한 것은 manifold를 정의할 때, 일반적인 atlas 대신 굳이 *maximal* atlas를 이용하는 이유인데, 여기에는 기술적인 (즉 본질적이지는 않은) 문제가 있다. 

예를 들어 $\mathbb{R}$은 다음의 $C^\infty$-atlas 

$$\mathcal{A}=\{(\mathbb{R}, \operatorname{id}_\mathbb{R})\}$$

도 갖지만, 또 다른 atlas 

$$\mathcal{A}'=\{((-\infty, 1), \operatorname{id}_{(-\infty, 1)}), ((-1, \infty),\operatorname{id}_{(-1,\infty)})\}$$ 

또한 갖는다. 이 두 atlas는 사실상 동일한 구조가 되며, 이와 같이 $\mathbb{R}$ 위에 동일한 미분구조를 주는 방법은 무수히 많을 것이다. 물론 서로 다른 atlas가 같은 미분구조를 줄 수도 있다고 생각하고 넘어갈 수도 있지만, 그 대신 미분구조를 *maximal* atlas가 주는 것으로 생각하면 maximality에 의하여 유일성이 잘 보장된다. 

그러나 앞서 말했듯 이 문제는 본질적인 내용이라기보다는 사소한 내용에 가깝다. 현실적으로 미분구조를 줄 때, 우리는 maximal $C^k$-atlas를 명시할 필요없이 아무 $C^k$-atlas만 주어도 문제가 없다. 

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Topological manifold $M$ 위에 $C^k$-atlas $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$를 포함하는 maximal $C^k$-atlas가 유일하게 존재한다. 따라서 임의의 $C^k$-atlas $\mathcal{A}$는 $M$ 위에 유일한 $C^k$-differentiable structure를 정의한다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{A}'$를 다음의 식

$$\mathcal{A}'=\{(V,\psi):\psi\circ\varphi_\lambda^{-1}, \varphi_\lambda\circ\psi^{-1}\text{ are $C^k$ for all $\varphi_\lambda\in\mathcal{A}$}\}$$

으로 정의하면 된다. 그럼 $\mathcal{A}'$는 $\mathcal{A}$를 포함하고, 따라서 $M$을 coordinate chart들로 덮을 수 있다. 한편, $(V,\psi)$, $(V',\psi')$가 $\mathcal{A}'$의 원소들이고 $V\cap V'\neq\emptyset$이라면 transition map

$$\psi'\circ\psi^{-1}:\psi(V\cap V')\rightarrow\psi'(V\cap V')$$

는 $C^k$이다. 임의의 $p\in\psi(V\cap V')$에 대하여, $p\in U$를 만족하는 $(U,\varphi)\in\mathcal{A}$를 뽑아오면 $U\cap V\cap V'$ 위에서

$$\psi'\circ\psi^{-1}=(\psi'\circ\varphi^{-1})\circ(\varphi\circ\psi^{-1})$$

가 되어 $\psi'\circ\psi^{-1}$가 점 $p$에서 $C^k$이기 때문이다. 점 $p$는 임의로 택한 점이므로, 이것이 $\psi'\circ\psi^{-1}$이 $C^k$임을 보여준다. 물론 $(V,\psi)$와 $(V',\psi')$의 역할을 바꾸면 반대방향 transition map 또한 $C^k$임을 보일 수 있다. 

당연히 정의에 의해 $\mathcal{A}'$는 maximal $C^k$-atlas가 되고, 이는 유일함을 쉽게 확인할 수 있다. 

</details>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 실수집합 $\mathbb{R}$ 위에 두 개의 atlas

$$\mathcal{A}_1=\{(\mathbb{R},\operatorname{id}_\mathbb{R})\},\qquad \mathcal{A}_2=\{(\mathbb{R}, x\mapsto x^3)\}$$

를 주자. 이들은 하나의 chart로 이루어진 atlas들이므로 당연히 $C^\infty$이다. 앞선 [명제 3](#pp3)에 의하여 이들 각각을 포함하는 미분구조가 존재한다. 그러나 이들은 서로 같지 않다. 두 chart $(\mathbb{R},\operatorname{id}_\mathbb{R})$과 $(\mathbb{R}, x\mapsto x^3)$이 서로 $C^\infty$-compatible이 아니기 때문이다. ($x\mapsto x^3$은 $C^\infty$ 함수지만, 그 역함수 $x\mapsto x^{1/3}$은 그렇지 않다)

</div>

그럼에도 불구하고 [예시 4](#ex4)의 두 manifold는 서로 diffeomorphic하다는 것을 나중에 확인하게 된다. 

## Partition of unity

우리는 이전 글에서 topological manifold $M$이 주어졌을 때, second countability를 이용하여 $M$이 paracompact임을 보이고, 따라서 $M$이 partition of unity를 갖는다는 것을 증명하였다. 그러나 이제 우리는 differentiable manifold에 관심이 있기 때문에 이를 적절하게 수정해주어야 한다. 앞서 *continuous* partition of unity의 존재성을 보인 [§위상다양체, 정리 8](#/ko/math/manifolds/topological_manifolds)을 다시 살펴보면, 이를 적절히 수정하기 위해서는 Urysohn lemma에 의해 얻어지는 $\psi_i$들 각각을 $C^\infty$ 함수들로 바꿔주기만 하면 된다는 것을 알 수 있다. 즉 다음의 보조정리만 보이면 충분하다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5 ($C^\infty$ Urysohn lemma)**</ins> 실수 $a'&lt;a&lt;b&lt;b'$가 주어졌다 하자. 그럼 $[a,b]$ 위에서는 1이고, $(a',b')$ 바깥에서는 0인 $C^\infty$ 함수 $\psi:\mathbb{R}\rightarrow[0,1]$이 존재한다.

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

[^1]: 만일 $U\cap V=\emptyset$이라면 $(U,\varphi)$, $(V,\psi)$는 vacuously $C^k$-compatible인 것으로 생각한다.
[^2]: 미분가능성은 국소적인 성질이므로.