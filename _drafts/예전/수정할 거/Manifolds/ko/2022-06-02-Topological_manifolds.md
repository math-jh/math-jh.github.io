---

title: "위상다양체"
excerpt: "위상다양체와 partition of unity"

categories: [Math / Manifold]
permalink: /ko/math/manifold/topological_manifolds
header:
    overlay_image: /assets/images/Manifold/Topological_manifolds.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-06-02
last_modified_at: 2022-06-06
weight: 1

---

## 표기법

앞으로 $m$차원의 좌표계를 다룰 일이 많으므로 다음과 같이 표기법을 고정하기로 한다. $\mathbb{R}^m$에 대하여, $i$번째 projection $\pr_i$를 $r^i$로 표기한다. 비슷하게, 임의의 집합 $X$와 함수 $f:X\rightarrow\mathbb{R}^m$에 대하여, $f$의 $i$번째 *성분함수*는 식 $f^i=r^i\circ f$으로 정의된다. 

이제 함수 $f$가 $\mathbb{R}^m$에서 $\mathbb{R}$로의 함수라 하자. 그럼 $f$의 $i$번째 성분에 대한 편미분을 다음의 식

$$\frac{\partial}{\partial r^i}\bigg|_t f=\frac{\partial f}{\partial r^i}\bigg|_t=\lim_{h\rightarrow 0}\frac{f(t^1,\ldots, t^{i-1}, t^i+h, t^{i+1},\ldots, t^m)-f(t^1,\ldots, t^m)}{h}$$

으로 정의하기로 한다. 위의 표기법과 같이, **[Lee]**의 표기를 따라 $i$번째 성분을 $x_i$ 대신 $x^i$로 적기로 한다.

만일 각각의 성분함수들이 $k$번 미분가능하고, 그 결과가 연속이라면 함수 $f$가 $C^k$라 부른다. 예를 들어 함수 $f:\mathbb{R}^2\rightarrow\mathbb{R}$이 $C^2$라는 것은 다음의 편미분들

$$\frac{\partial^2 f}{\partial x^2},\quad\frac{\partial^2 f}{\partial x\partial y},\quad\frac{\partial^2 f}{\partial y\partial x},\quad\frac{\partial^2 f}{\partial y^2}$$

이 모두 존재하고 연속인 것이다. 함수 $f$가 모든 자연수 $k$에 대하여 $C^k$라면 이를 $C^\infty$라 부른다.

## 위상다양체

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 $m$차원 *locally Euclidean<sub>국소적 유클리드 공간</sub>*이라는 것은 임의의 $x\in X$마다 적당한 열린근방 $U\subseteq X$에서 유클리드 공간의 열린집합 $U'\subset\mathbb{R}^m$으로의 homeomorphism $\varphi:U\rightarrow U'\subset\mathbb{R}^m$이 존재하는 것이다.  

위상공간 $M$이 second countable, Hausdorff이고 $m$차원 locally Euclidean이라면 $M$을 $m$차원 *topological manifold<sub>위상다양체</sub>*라 부른다.

</div>

위 정의에서의 homeomorphism $\varphi:U\rightarrow U'$를 *coordinate chart*라 부른다. $U'$는 $\mathbb{R}^m$의 부분집합이므로, $\varphi$는 $m$개의 성분함수들로 이루어진 함수이다. 위에서 약속한 표기법에 따르면, 성분함수 $r^i\circ\varphi$들은 $\varphi^i$로 적는 것이 옳지만 이들이 $U$ 위에서의 좌표계와 같은 역할을 한다는 것을 강조하기 위해 $x^i$로 적는다.

또, 실제로 위의 정의를 적용할 때에는 $U$와 $U'$가 모두 연결집합인 경우만 생각한다. 이는 우선 점 $x$의 임의의 열린근방 $U_0$, 그리고 이와 homeomorphic한 $\mathbb{R}^n$에서의 열린집합 $U'_0$이 주어졌다 하면, $\mathbb{R}^n$의 위상의 정의에 의하여 $\varphi(x)$를 포함하는 열린 공 $U'$을 잡을 수 있고, 이를 다시 $\varphi^{-1}$을 타고 $X$로 보내어 $U=\varphi^{-1}(U')$로 정의할 수 있기 때문이다. 

임의의 $m$차원 topological manifold $M$이 주어졌다 하자. 일반적으로 $M$은 국소적으로만 $\mathbb{R}^m$과 닮아있기 때문에 이를 $\mathbb{R}^m$ 안에 그리는 것은 불가능할 수도 있다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 1차원 구면 $S^1$을 생각하자. 그럼 임의의 점 $p\in S^1$에 대하여, $p$의 antipodal point를 포함하지 않을 정도로 작게 호를 그리면, 이는 $p$를 포함하는 $S^1$의 열린집합이 되며, 이 집합이 $\mathbb{R}^1$의 열린집합과 homeomorphic하다는 것은 직관적으로 자명하다. 따라서 $S^1$은 $1$차원의 위상다양체다. 

그러나 $S^1$과 homeomorphic한 $\mathbb{R}^1$의 부분집합은 존재하지 않는다. $S^1$에서 한 점을 뺀 공간은 여전히 연결집합이지만, $\mathbb{R}^1$에는 그러한 성질을 만족하는 집합이 없기 때문이다.

</div>

그러나 Whitney embedding theorem에 의하여, 임의의 $n$차원 manifold는 $2n-1$차원 유클리드 공간에 적당히 넣을 수 있다는 것이 알려져 있다. 때문에 **[MS]**와 같은 책에서는 manifold를 정의할 때 충분히 큰 차원의 유클리드 공간의 부분집합으로 정의하기도 한다. 그러나 이런 식으로 정의할 경우, manifold $M$의 성질이 $M$에 내재되어 있는 성질인지, 혹은 $\mathbb{R}^A$의 부분집합으로서 생기는 성질인지를 꼼꼼히 따져줘야 하기 때문에 우리는 [정의 1](#df1)과 같은 접근방식을 유지한다.

이 접근방식은 manifold를 다룰 때 많은 도움이 되지만, 동시에 직관적인 몇몇 정의들을 새로운 언어로 써야 한다. 예컨대 위의 예시 $S^1$를 보면, 점 $p\in S^1$에서의 접선이 무엇인지는 직관적으로 명확하지만 이를 $S^1$을 둘러싸고 있는 공간 $\mathbb{R}^2$ 없이 설명하는 것은 어렵다. 이를 [§접공간]()에서 정의한다. 

## Paracompactness

한편, manifold는 국소적으로는 우리에게 친숙한 공간인 유클리드 공간이다. 따라서 manifold를 다룰 때에는 이렇게 잘 알려진 정보를 이어붙여 manifold 전역에서 성립하는 정보를 얻어내는 과정이 필요하다. 가령 $M$의 임의의 점 $p$마다, 적당한 열린근방 $U$와 이 위에서 정의된 함수 $f_U:U\rightarrow M$들이 주어졌다 가정하자. 만일 $U\cap V\neq\emptyset$일 때마다 $f\_U\|\_{U\cap V}=f\_V\|\_{U\cap V}$라면, 이들 $f\_U$들을 이어붙여 $M$ 전역에서 정의된 함수 $f:M\rightarrow\mathbb{R}$을 만들 수 있다. ([집합론, §함수 (1), 정의 3](/ko/math/set_theory/functions_1#df3)) 이를 더 일반화하여, 각각의 조각들에서 정의된 정보들이 compatible하지 않더라도 $M$ 전역에서의 정보를 주는 방법이 존재한다. 

이를 위해서는 일종의 finiteness가 필요하다. 위상공간 $X$와, $X$의 부분집합들의 모임 $\\{A\_i\\}\_{i\in I}$에 대하여, 이 모임이 *locally finite*이라는 것은 임의의 $x\in X$가 주어질 때마다, $x$의 적당한 열린근방 $U$가 존재하여 $U\cap A\_i\neq\emptyset$인 $i\in I$가 오직 유한 개 뿐이도록 할 수 있는 것이다. 또, 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 위상공간 $X$가 주어졌다 하자.

1. $S\subseteq X$와 그 covering $\\{U\_i\\}\_{i\in I}$에 대해, 또 다른 $S$의 covering $\\{V_j\\}_{j\in J}$가 $\\{U_i\\}$의 *refinement*라는 것은 각각의 $j$마다 적당한 $i$가 존재하여 $V_j\subseteq U_i$이도록 할 수 있는 것이다. 
2. 만일 $X$의 임의의 open covering이 항상 locally finite, open refinement를 갖는다면, $X$를 *paracompact*라 한다.

</div>

정의에 의해 닫힌집합들의 <em_ko>유한한</em_ko> 합집합은 다시 닫힌집합이 되었었는데, 다음 보조정리는 locally finite 조건이 이를 잘 일반화한다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4**</ins> $X$의 닫힌집합들의 모임 $\\{C_i\\}$가 locally finite이라 하자. 그럼 $C=\bigcup C_i$도 닫힌집합이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$X\setminus C$가 열린집합임을 보이면 충분하다. 임의의 $x\not\in C$에 대하여, 유한히 많은 $C_i$들과만 만나는 열린근방 $V$를 찾을 수 있다. 각각의 $i\in I$에 대해 $U_i=X\setminus C_i$라 하자. 그럼 

$$X\setminus C=X\setminus\bigcup_{i\in I} C_i= \bigcap_{i\in I} (X\setminus C_i)=\bigcap_{i\in I} U_i$$

이므로, $X\setminus C$는 집합 $V\cap \bigcap U_i$를 포함한다. 따라서 $V\cap \bigcap U_i$는 집합 $X\setminus C$에 포함된 $x$의 열린근방이며, $x\in C$는 임의의 원소였으므로 $X\setminus C$는 열린집합이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 임의의 topological manifold $M$은 항상 paracompact이다. 뿐만 아니라, $M$의 임의의 open covering이 주어졌을 때, locally finite open refinement를 countable하고, 각각의 원소들이 relatively compact이도록 잡을 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $M$은 second countable이므로 $M$의 countable basis $\mathcal{B}$가 존재한다. 이 중 relatively compact한 것들만 모아 그 모임을 $\\{U_i\\}$라 하자. 그럼

1. 임의의 $p\in M$에 대하여, $p$를 포함하는 적절한 열린집합 $U$는 $\varphi:U\rightarrow U'$에 의해 $\mathbb{R}^m$의 열린집합 $U'$와 homeomorphic하다. 이제 $B(\varphi(p),\epsilon)\subseteq U'$를 만족하는 적절한 $\epsilon>0$을 잡으면, 두 집합

    $$V'=B(\varphi(p),\epsilon/2),\qquad K'=\clV$$

    가 정의되며, $V'$는 열린집합, $K'$는 compact이다.  

    이제 $V=\varphi^{-1}(V')$, $K=\varphi^{-1}(K')$라 하면 $p\subseteq V\subseteq K$이고 $M$에서 $V$는 열린집합, $K$는 compact이다. 한편, $\mathcal{B}$는 $M$의 basis이므로 

    $$V=\bigcup_{\substack{B\in\mathcal{B}\\B\subseteq V}}B$$

    로 쓸 수 있는데, 우변의 합집합의 조건을 만족하는 $B$는 $B\subseteq V\subseteq K$를 만족하므로, $\clB\subseteq K$이고 따라서 relatively compact가 되어 $\\{U_i\\}$에 속한다. 즉, 임의의 $p\in M$에 대하여 $p\in U_i$이도록 하는 적절한 $i$가 존재한다.

2. 비슷하게, 임의의 $U_i,U_j$에 대하여 $p\in U_i\cap U_j$라 하자. 그럼 1번에서 만든 것과 동일하게 열린집합 $V_i,V_j$와 compact set들 $K_i$, $K_j$를 만들 수 있다. 이제 $V_i\cap V_j$를 $\mathcal{B}$의 원소들의 합집합으로 표현하면 $V_i\cap V_j\subseteq K_i\cap K_j$이므로 다시
    
    $$p\in B\subseteq V_i\cap V_j\subseteq K_i\cap K_j$$

    를 만족하는 $B\in\mathcal{B}$를 찾을 수 있고, 이러한 $B$는 compact set $K_i\cap K_j$의 부분집합이므로 relatively compact가 되어 $B\in\\{U_i\\}$이다. 

위의 1번과 2번에서, 모임 $\\{U_i\\}$가 $M$의 basis가 된다는 것을 확인할 수 있다. 

이제 $G_1=U_1$으로 두고, 

$$G_k=U_1\cup\cdots\cup U_{j_k}$$

가 정의되었다 하자. 귀납적으로 $j_{k+1}$을 

$$\cl G_k\subset\bigcup_{i=1}^{j_{k+1}} U_i$$

가 성립하고, $j_k$보다 큰 정수 중 가장 작은 것으로 두면 $\\{G_k\\}$는 열린집합들의 ascending chain이고 $\\{\clG_k\\}$는 exhaustion이다. (<#ref#>)

이를 이용해 $M$이 paracompact임을 보일 수 있다. $\\{V_\alpha\\}\_{\alpha\in\Lambda}$가 임의의 open covering이라 하자. 각각의 $i$에 대하여, $\cl(G_i)\setminus G_{i-1}$은 집합 $G_{i+1}\setminus\cl(G_{i-2})$에 포함된 compact set이다. 이제 $\\{V_\alpha\\}$의 open refinement $\\{V\_\alpha\cap(G_{i+1}\setminus\cl(G_{i-2}))\\}$는 compact set $\cl(G_i)\setminus G_{i-1}$의 open covering으로서, finite subcover를 가진다. 또, 비슷하게 index가 작은 $\cl(G_2)\subseteq G_3$의 경우에도 $\clG_2$를 덮는 유한한 $\\{V\_\alpha\cap G\_3\\}$의 subcover를 생각할 수 있다.  
이렇게 만든 subcover들의 모임이 $\\{V_\alpha\\}$의 open refinement가 되는 것은 자명하다. 또, 이 모임은 countable한 compact set $\cl(G_i)\setminus G_{i-1}$마다 유한히 많은 원소들을 모아서 만들어진 모임이므로 자연스럽게 countable이다. 임의의 점 $p\in M$은 정확히 하나의 $\cl(G_i)\setminus G_{i-1}$에만 포함되므로 이 모임은 locally finite이고, 마지막으로 이 모임의 임의의 원소는 충분히 큰 $N$에 대하여 compact set $\clG_N$의 부분집합이므로 relatively compact이다.

</details>




---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---


[^1]: 보편적으로 coordinate domain이 이 역할을 담당한다.
