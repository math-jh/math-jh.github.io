---

title: "벡터다발"
excerpt: "Vector bundle, tangent bundle, cotangent bundle"

lang: ko

categories: [Math / Manifold]
permalink: /ko/math/manifold/vector_bundles
header:
    overlay_image: /assets/images/Manifold/Vector_bundles.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-19
last_modified_at: 2022-06-19
weight: 10

---

## 벡터다발

이제 우리는 벡터장을 정의해야 하는데, $C^\infty$ 벡터장과 같은 개념을 정의하기 위해서는 벡터다발의 개념을 먼저 정의하는 것이 좋다. 

Manifold $M$의 벡터다발은 $M$의 각 점 $p$마다 고정된 차원의 $\mathbb{R}$-벡터공간 $\mathbb{R}^k$가 하나씩 붙어있는 것이다. 구분을 위해 점 $p$에 붙어있는 $\mathbb{R}^k$를 $E_p$로 표기하자. 그럼 전체적으로 보았을 때, 이 데이터는 다음의 집합

$$E=\{(p,v): p\in M, v\in E_p\}$$

으로 정의된다. 그럼 자연스러운 projection map $\pi:E\rightarrow M$이 존재한다. 

벡터다발의 좋은 점 중 하나는 벡터다발이 그 자체로 위상구조, 혹은 $M$이 manifold일 경우에는 manifold 구조를 갖는다는 것이다. 하지만 이 때 $E$에 주어지는 위상구조 혹은 manifold 구조는 단순한 product space(혹은 manifold)와는 다르다. 

$S^1$의 각 점에 $\mathbb{R}$을 붙인다고 생각하자. 우선 다음과 같이 모든 방향에서 평행하도록 $\mathbb{R}$을 붙일 수 있으며, 이 경우 벡터다발의 모양은 원기둥이 된다.

![cylinder](/assets/images/Manifold/Vector_bundles-1.png){:width="140px" class="invert" .align-center}
<cap>Image from <a href="https://ncatlab.org/nlab/show/vector+bundle">nLab</a></cap>


이 벡터다발은 $S^1\times\mathbb{R}$과 동일한 위상구조를 가진다. 그러나 $\mathbb{R}$을 한 바퀴 돌려서 $S^1$에 붙이면 다음과 같이 뫼비우스 띠 모양의 공간을 얻게 된다.

![mobius_strip](/assets/images/Manifold/Vector_bundles-2.png){:width="140px" class="invert" .align-center}
<cap>Image from <a href="https://ncatlab.org/nlab/show/vector+bundle">nLab</a></cap>

첫 번째 원기둥과 같이 벡터다발의 구조가 $M\times\mathbb{R}^k$과 동일한 경우 우리는 이를 *trivial bundle*이라 부른다. 벡터다발이 trivial하지 않은 경우에도, 우리는 국소적으로는 벡터다발이 trivial하기를 원하므로, 이를 벡터다발의 정의에 추가한다.

지금까지의 논의를 정리하면 다음과 같다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 주어졌다 하자. Rank $k$의 *vector bundle<sub>벡터다발</sub>*은 다음과 같이 구성된 데이터다.

1. *Base space* $X$와, *total space* $E$,
2. *Bundle projection* $\pi:E\rightarrow X$,
3. 각각의 $x\in X$마다 정의된 $k$차원 $\mathbb{R}$-벡터공간 $\pi^{-1}(p)=E_p$.

추가적으로 다음의 조건이 만족되어야 한다.

> 임의의 $x\_0\in X$에 대하여, $x\_0$의 열린근방 $U$와 homeomorphism[^1] $\phi:\pi^{-1}(U)\rightarrow U\times\mathbb{R}^k$가 존재하여, $(\pi\circ\phi)(x,v)=x$가 모든 $x\in U$, $v\in E_x$에 대해 성립하고, 임의의 $x\in U$마다 $\phi\|\_{E\_x}$가 $\mathbb{R}$-벡터공간 사이의 isomorphism이다. 

![local_trivialization](/assets/images/Manifold/Vector_bundles-3.png){:width="450px" class="invert" .align-center}
<cap>[Lee] p.250. Fig. 10.1</cap>

</div>

지금 우리가 관심있는 대상은 $X$가 manifold인 경우이다. 따라서 $C^\infty$ vector bundle의 경우, total space $E$는 위상공간 대신 manifold이고, $\pi$는 continuous surjection 대신 $C^\infty$ surjection, 그리고 local trivialization $\phi$는 homeomorphism 대신 diffeomorphism으로 바꾸어야 한다. 

## 접다발과 여접다발

Vector bundle의 대표적인 두 예시는 tangent bundle과 cotangent bundle이다. 이들은 점 $p\in M$에 각각 $T_pM$과 $T_p^\ast M$을 붙여서 만들어지는 rank $m$의 vector bundle이다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2 (Tangent bundle)**</ins> 집합 $TM$을

$$TM=\bigsqcup_{p\in M} T_pM$$

으로 정의하자. 그럼 자연스러운 projection map $\pi:TM\rightarrow M$이 존재한다. $TM$을 vector bundle로 보기 위해서는 여기에 manifold 구조를 주어야 한다.

우선 $TM$ 위에 coorindate system을 정의하자. 임의의 coordinate system $(U,\varphi)$에 대하여, 함수 $\tilde{\varphi}:\pi^{-1}(U)\rightarrow\mathbb{R}^m\times\mathbb{R}^m$을 다음의 식

$$\tilde{\varphi}(v)=\bigl(x^1(\pi(v)), \ldots, x^m(\pi(v)), dx^1(v),\ldots, dx^m(v)\bigr)$$

으로 정의하자. 그럼 $\tilde{\varphi}$는 $\pi^{-1}(U)$에서 $\mathbb{R}^{2m}$의 열린집합 $\varphi(U)\times\mathbb{R}^m$으로의 bijection이다. 

이들은 $C^\infty$-compatible이다. 또 다른 coordinate system $(V,\psi)$, $\psi=(y^j)\_{j=1}^m$가 주어졌다 하고, $\tilde{\psi}$를 위와 같이 정의하자. 그럼 $\pi^{-1}(U)\cap\pi^{-1}(V)=\pi^{-1}(U\cap V)$ 위에서

$$\begin{aligned}(\tilde{\psi}\circ\tilde{\varphi}^{-1})(p^1, \ldots, p^m, v^1, \ldots, v^m)&=\tilde{\psi}\left(\varphi^{-1}(p), \sum v^i\frac{\partial}{\partial x^i}\bigg|_{\varphi^{-1}(p)}\right)\\&=\left((\psi\circ\varphi^{-1})(p), dy^1(v), \ldots, dy^m(v)\right)\end{aligned}$$

이고, 이 때 $v=\sum v^i\frac{\partial}{\partial x^i}$이다. 또, 임의의 $j$에 대하여

$$dy^j\left(\sum v^i\frac{\partial}{\partial x^i}\bigg|_{\varphi^{-1}(p)}\right)=\sum_{i=1}^m v^i\frac{\partial y^j}{\partial x^i}\bigg|_{\varphi^{-1}(p)}$$

가 된다. 따라서, 위의 transition map $\tilde{\psi}\circ\tilde{\varphi}^{-1}$의 각 성분들이 $C^\infty$이므로 $\tilde{\psi}\circ\tilde{\varphi}^{-1}$도 $C^\infty$이다. 

한편 $TM$의 위상은 다음의 집합들

$$\{\tilde{\varphi}^{-1}(W): \text{$W$ open in $\mathbb{R}^{2m}$, $(U,\varphi)\in\mathcal{A}$}\}$$

을 basis로 하여 얻어진다. $W=\mathbb{R}^{m}$으로 두면 위의 집합에 의해 만들어지는 위상에서 $\pi^{-1}(U)$들이 모두 열린집합임을 확인할 수 있고, 이 위상이 $2m$차원의 topological manifold를 만든다는 것도 확인할 수 있다. 

이제 남은 것은 $TM$에서의 local trivialization 뿐이다. 임의의 coordinate system $(U,\varphi)$에 대하여, $\phi:\pi^{-1}(U)\rightarrow U\times\mathbb{R}^m$을 이번에는 다음의 식

$$v|_p\mapsto (p, dx^1(v),\ldots, dx^m(v))$$

으로 정의하면 된다. 고정된 $\pi^{-1}(p)$ 위에서 $\phi$가 벡터공간 사이의 isomorphism이 되는 것은 자명하고, 또 임의의 $v_x$에 대하여 $(\pi\circ\phi)(x,v)=x$임도 자명하다. $\phi$가 diffeomorphism이 된다는 것은 

$$\tilde{\varphi}=(\varphi\times\operatorname{id}_{\mathbb{R}^m})\circ\phi$$

이고, 이 식에서 $\phi$를 제외한 두 함수가 모두 diffeomorphism이기 때문에 성립한다.

</div>

처음에 살펴봤던 것과 같이, 일반적인 vector bundle은 $M\times\mathbb{R}^k$와 닮아있을 필요가 없다. 이는 tangent bundle도 마찬가지이며, 만일 $TM$이 product manifold $M\times\mathbb{R}^m$과 동일한 manifold 구조를 갖는다면 $M$이 *parallizable*하다고 말한다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3 (Cotangent bundle)**</ins> 위의 예시와 동일하게 $T^\ast M$을 정의할 수 있다. $T^\ast M$은 집합으로서는

$$T^\ast M=\bigsqcup_{p\in M} T_p^\ast M$$

이며, projection map $\pi^\ast:T^\ast M\rightarrow M$ 또한 잘 정의된다. 나머지 부분은 주어진 coordinate chart $(U,\varphi)$에 대하여

$$\tilde{\varphi}^\ast(\omega)=\left(x^1(\pi^\ast(\omega)), \ldots, x^m(\pi^\ast(\omega)), \omega\left(\frac{\partial}{\partial x^1}\right), \ldots, \omega\left(\frac{\partial}{\partial x^m}\right)\right)$$

으로 정의하고 [예시 2](#ex2)를 반복하면 된다.

</div>

Rank $k$의 $C^\infty$ vector bundle $\pi:E\rightarrow M$이 주어졌다 하자. $E$가 trivial bundle이 아닌 이상 이를 표현하기 위해서는 여러 개의 local trivialization이 필요한데, 이 때의 local trivialization들 역시 일종의 $C^\infty$-compatibility를 만족한다. 

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $\pi:E\rightarrow M$이 rank $k$의 $C^\infty$ vector bundle이라 하자. $\phi:\pi^{-1}(U)\rightarrow U\times\mathbb{R}^k$와 $\psi:\pi^{-1}(V)\rightarrow V\times\mathbb{R}^k$가 두 local trivialization이라 하면, 적당한 $C^\infty$ 함수 $\tau:U\cap V\rightarrow\operatorname{GL}_k(\mathbb{R})$이 존재하여 

$$\phi\circ\psi^{-1}(p,v)=(p, \tau(p)v)$$

가 성립한다. 

</div>

## Section and frame

주어진 vector bundle $\pi:E\rightarrow M$에 대하여, 열린집합 $U\subset M$에서 정의된 *local section*은 다음의 식

$$\pi\circ \sigma=\operatorname{id}_U$$

을 만족하는 연속함수 $\sigma:U\rightarrow E$를 뜻한다. ([집합론, §함수 (2), 정의 2](/ko/math/set_theory/functions_2#df2)) 만일 $U=M$이라면 $\sigma$를 *global section*이라 부른다. 만일 $E$가 $C^\infty$ vector bundle이고, $\sigma$가 $C^\infty$ 함수라면 이를 $C^\infty$ section이라 부른다. 

조건 $\pi\circ\sigma=\operatorname{id}_U$가 성립하기 위해서는 각각의 $p\in U$에 대하여 $\sigma(p)$가 $\pi^{-1}(p)$에 속해 있어야 한다. 따라서, $E$를 $M$의 각 점 $p$마다 $\mathbb{R}^k$가 붙어있는 모습으로 상상한다면, $\sigma$가 local section이라는 것은 각각의 점 $p$마다, 이 점에 붙어있는 $\mathbb{R}^k$의 원소가 대응되며, 이 대응이 $E$ 위에 주어진 위상구조에 대해 연속이라는 것이다. 

Local section $\sigma$는 각 점 $p$마다 <em_ko>하나의</em_ko> 벡터 $\sigma(p)$를 대응시킨다. $\mathbb{R}^k$는 $k$개의 일차독립인 벡터가 존재하면 완벽하게 표현할 수 있으므로, 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 

</div>

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---

[^1]: 이 때의 $\phi$를 *local trivialization*이라 부른다. 