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

앞으로 $m$차원의 좌표계를 다룰 일이 많으므로 다음과 같이 표기법을 고정하기로 한다. $\mathbb{R}^m$에 대하여, $i$번째 projection $\operatorname{pr}_i$를 $r^i$로 표기한다. 비슷하게, 임의의 집합 $X$와 함수 $f:X\rightarrow\mathbb{R}^m$에 대하여, $f$의 $i$번째 *성분함수*는 식 $f^i=r^i\circ f$으로 정의된다. 

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

Topological manifold $M$은 항상 국소적으로 유클리드 공간 $\mathbb{R}^m$과 닮아있기 때문에, 이 국소적인 정보들을 이어붙여 $M$ 전체에서 성립하는 성질을 얻을 수 있다. 예를 들어, $M$의 임의의 점 $p$마다 적당한 열린근방 $U$가 존재하여[^1], 함수들 $f:U\rightarrow\mathbb{R}$이 정의되었다고 하자. 만일 $f$들이 모두 compatible하다면 ([집합론, §함수 (1), 정의 3](/ko/math/set_theory/functions_1#df3)), 이들을 이어붙여 $M$ 전체에서 정의된 함수를 만들 수 있을 것이며, 이렇게 만들어진 함수는 대체로 $f$의 성질들, 예를 들어 연속성 혹은 smoothness를 이어받는다. 

그러나 일반적으로, 이렇게 국소적으로 정의된 함수들이 항상 compatible하다는 것을 바랄 수는 없다. 이런 경우에 $M$에 대해 국소적으로 알려진 정보들을 전체 $M$으로 확장하는 과정은 주로 다음의 *partition of unity*를 통해 이루어진다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 위상공간 $X$와, $X$의 open covering $\\{U\_i\\}\_{i\in I}$가 주어졌다 하자. 이 때, 연속함수 $\phi_i:X\rightarrow [0,1]$들의 모임 $\\{\phi\_i\\}\_{i\in I}$가 $\\{U\_i\\}$에 의해 dominate되는 *partition of unity<sub>단위분할</sub>*라는 것은 다음의 세 조건

1. $\operatorname{supp}\phi\_i\subseteq U\_i$,
2. $\\{\operatorname{supp}\phi\_i\\}_{i\in I}$가 locally finite,
3. 모든 $x$에 대하여 $\sum\_{i\in I}\phi\_i(x)=1$.

을 만족하는 것이다.

</div>

위의 정의에서, $\\{\operatorname{supp}\phi\_i\\}\_{i\in I}$가 *locally finite*이라는 것은, 임의의 $x\in X$마다 적당한 열린근방 $U$가 존재하여, $U$가 오직 <em_ko>유한 개의</em_ko> $\operatorname{supp}\phi_i$들과만 만나는 것이다. 따라서 임의의 $x\in X$는 오직 유한히 많은 $\operatorname{supp}\phi_i$에만 속해 있으며, 특히 3번 조건의 합 $\sum\phi_i(x)$는 $x\in X$가 고정될 때마다 유한합이 된다.  
또, 만일 $\bigcup\operatorname{supp}\phi_i\neq X$라면 $x\not\in\bigcup\operatorname{supp}\phi_i$인 $x$에 대하여 $\sum\phi_i(x)=0$일 것이므로, 3번 조건은 모임 $\\{\operatorname{supp}\phi_i\\}$이 $X$의 covering이 된다는 것을 함의한다.

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

우리가 처음으로 보일 사실은 임의의 paracompact Hausdorff space가 normal space가 된다는 사실이다. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 임의의 paracompact, Hausdorff space $X$는 normal space이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

서로소인 두 닫힌집합 $A,B$가 주어졌을 때, 이들 각각을 포함하는 서로소인 열린집합 $U,V$가 존재함을 보여야 한다.

우선 $A$가 singleton $A=\\{a\\}$인 경우부터 고려한다. 각각의 $b\in B$에 대하여, Hausdorff 조건에 의해 $A\subseteq U_b$이고 $b\in V_b$이도록 하는 서로소인 열린집합들 $U_b,V_b$가 존재한다. 특히 $U_b\cap V_b=\emptyset$으로부터 $U_b\subseteq X\setminus V_b$이고, 따라서

$$A\subseteq U_b=\operatorname{int}(U_b)\subset\operatorname{int}(X\setminus V_b)=X\setminus\operatorname{cl}V_b$$

이므로 $A\cap\operatorname{cl}V_b=\emptyset$이다. 이제 $\\{V_b\\}_{b\in B}$는 $B$의 open covering이므로, 여기에 열린집합 $X\setminus B$를 추가한 모임은 $X$의 open covering이 된다. $X$는 paracompact이므로, 이 모임의 locally finite, open refinement가 존재한다. 이를 $\mathcal{C}$라 하자. 

이제 $\mathcal{C}$의 원소들 중, $B$와 만나는 것들을 모두 모아 $\mathcal{D}\subset\mathcal{C}$를 만들자. 그럼 $\mathcal{C}$가 locally finite이므로, 그 부분집합 $\mathcal{D}$ 또한 locally finite이다. 또 $\mathcal{D}$가 $B$를 덮는다는 것은 자명하므로,  다음의 열린집합

$$V=\bigcup_{D\in\mathcal{D}}D$$

은 $B$를 포함하는 열린집합이다. 

한편, 임의의 $D\in\mathcal{D}$에 대해 $D\subseteq V_b$인 $b$를 잡으면

$$A\cap\operatorname{cl}D\subseteq A\cap\operatorname{cl}V_b=\emptyset$$

또한 성립한다. 따라서 [보조정리 4](#lem4)에 의해

$$\emptyset=A\cap \bigcup_{D\in\mathcal{D}}\operatorname{cl}(D)=A\cap \operatorname{cl}V$$

이므로 열린집합 $U=X\setminus\operatorname{cl}V$과 $V$가 각각 $A=\\{a\\}$와 $B$를 분리하는 서로소인 열린집합이 된다. 즉, $X$는 regular space가 된다.

이제 임의의 서로소인 닫힌집합 $A,B$에 대하여, 방금 증명한 regularity를 사용하면 각각의 $b\in B$에 대해 $A\subseteq U_b$, $b\in V_b$이도록 하는 두 서로소인 열린집합 $U_b,V_b$를 잡을 수 있다. 이제 이들을 사용하여 위의 논증을 그대로 반복하면, 그 결과로 얻어지는 $U,V$가 $A$와 $B$를 분리하는 서로소인 열린집합이 된다는 것을 확인할 수 있다.

</details>

따라서 어떠한 위상공간 $X$가 paracompact, Hausdorff라면 Urysohn lemma를 자유롭게 사용할 수 있다. (<#ref#>) 특히 Urysohn lemma는 partition of unity의 존재성을 보일 때 사용된다. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> 임의의 paracompact Hausdorff space $X$와, $X$의 open covering $\\{U\_i\\}\_{i\in I}$가 주어졌다 하자. 그럼 $\operatorname{cl}V_b\subseteq U_i$가 모든 $i\in I$에 대해 성립하도록 하는 $X$의 locally finite open covering $\\{V_i\\}$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathcal{C}$를 [적당한 $i\in I$가 존재하여 $\operatorname{cl}C\subseteq U_i$인 열린집합 $C$들의 모임]으로 정의하자. 임의의 $x\in X$와 $x$를 포함하는 $U_i$에 대하여 $C_i=X\setminus U_i$는 $x$를 포함하지 않는 닫힌집합이고, 따라서 $X$의 regularity에 의하여 $x$와 $C_i$를 분리하는 서로소인 열린집합 $V_i$와 $W_i$가 각각 존재한다.  그럼 $V_i\subseteq X\setminus W_i$이고, 따라서

$$\operatorname{cl}V_i\subseteq X\setminus W_i\subseteq X\setminus C_i=U_i$$

가 성립한다. 즉, 임의의 $x\in X$에 대해 그 closure가 어떤 $U_i$에 포함되도록 하는 열린집합 $V_i$가 항상 존재하고 따라서 $\mathcal{C}$는 open covering이다. $X$의 paracompactness를 이용하여  $\mathcal{C}$의 locally finite open refinement $\mathcal{D}$를 얻자.

적당한 index set $J$를 통해 $\mathcal{D}=\\{W\_j\\}\_{j\in J}$라 적으면, 정의에 의해 $W_j$는 어떠한 $\mathcal{C}$의 원소 $C$에 포함되며, 다시 $C$는 적당한 $i\in I$에 대해 $\operatorname{cl}C\subseteq U_i$를 만족한다. 따라서 각각의 $j$마다 이러한 $i$를 하나씩 뽑아 함수 $f:J\rightarrow I$를 만들 수 있다. 이제 각각의 $i\in I$에 대하여

$$V_i=\bigcup_{j\in f^{-1}(i)} W_j$$

으로 정의하자. 그럼 $\\{V_i\\}_{i\in I}$가 정확히 우리가 원하는 open covering이 된다.

우선 우변의 $W_j$들은 모두 $\operatorname{cl}W_j\subseteq U_i$를 만족하고, 따라서

$$\operatorname{cl}V_i=\operatorname{cl}\left(\bigcup_{j\in f^{-1}(i)}W_j\right)=\bigcup_{j\in f^{-1}(i)}\operatorname{cl}W_j\subseteq U_i$$

가 된다. 또 $\mathcal{D}$는 locally finite이므로, 임의의 $x\in X$마다 적당한 열린근방 $U$가 존재하여 유한히 많은 $W_j$들과만 만나도록 할 수 있다. 그럼 이 $U$는 $j\in f^{-1}(i)$를 만족하는 $V_i$들과만 만나므로, 마찬가지로 $\\{V_i\\}$도 locally finite이다.

</details>

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 임의의 paracompact Hausdorff space $X$와, $X$의 open covering $\\{U\_i\\}\_{i\in I}$에 대하여, $\\{U_i\\}$에 의해 dominate되는 partition of unity가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 앞선 보조정리를 이용하여 locally finite open covering $\\{V\_i\\}\_{i\in I}$를 얻고, 다시 여기에 앞선 보조정리를 이용하여 $\\{W\_i\\}\_{i\in I}$를 얻자. 그럼 $\operatorname{cl}W_i\subseteq V_i$이고 $\operatorname{cl}V_i\subseteq U_i$이다. 

이제 Urysohn lemma를 적용하여 연속함수 $\psi_i:X\rightarrow [0,1]$을 $\psi_i(\operatorname{cl}W_i)=\\{1\\}$, $\psi_i(X\setminus V_i)=\\{0\\}$을 만족하도록 잡자. 그럼 $\operatorname{supp}\psi_i\subset\operatorname{cl}V_i\subseteq U_i$이다. 또, 임의의 열린집합 $U$가 $V_i$와 만나는 것은 $\operatorname{cl}V_i$와 만나는 것과 동치이므로, $\\{\operatorname{cl}V_i\\}$ 또한 locally finite이고 따라서 그 부분집합들의 모임 $\\{\operatorname{supp}\psi_i\\}$ 또한 그러하다. 

따라서 함수 $\Psi$를

$$\Psi(x)=\sum_{i\in I}\psi_i(x)$$

으로 정의하면 우변의 무한합은 항상 유한합이 된다. 뿐만 아니라, 임의의 $x\in X$마다 적당한 열린근방 $U$를 택하여 $U\cap \operatorname{supp}\psi_i\neq\emptyset$인 $i$가 유한하도록 할 수 있으므로, 이 열린집합 $U$ 위에서 $\Psi$는 유한히 많은 연속함수들의 합이 되어 연속이다. 이제 함수 $\phi_i$들을 

$$\phi_i(x)=\frac{\psi_i(x)}{\Psi(x)}$$

로 잡으면 이들이 원하는 partition of unity가 된다.

</details>

물론, topological manifold가 위의 조건들을 만족하지 않았다면 굳이 이 절에서 이렇게 많은 정리들을 증명할 필요가 없었을 것이다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> 임의의 topological manifold $M$은 항상 paracompact이다. 뿐만 아니라, $M$의 임의의 open covering이 주어졌을 때, locally finite open refinement를 countable하고, 각각의 원소들이 relatively compact이도록 잡을 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $M$은 second countable이므로 $M$의 countable basis $\mathcal{B}$가 존재한다. 이 중 relatively compact한 것들만 모아 그 모임을 $\\{U_i\\}$라 하자. 그럼

1. 임의의 $p\in M$에 대하여, $p$를 포함하는 적절한 열린집합 $U$는 $\varphi:U\rightarrow U'$에 의해 $\mathbb{R}^m$의 열린집합 $U'$와 homeomorphic하다. 이제 $B(\varphi(p),\epsilon)\subseteq U'$를 만족하는 적절한 $\epsilon>0$을 잡으면, 두 집합

    $$V'=B(\varphi(p),\epsilon/2),\qquad K'=\operatorname{cl}V$$

    가 정의되며, $V'$는 열린집합, $K'$는 compact이다.  

    이제 $V=\varphi^{-1}(V')$, $K=\varphi^{-1}(K')$라 하면 $p\subseteq V\subseteq K$이고 $M$에서 $V$는 열린집합, $K$는 compact이다. 한편, $\mathcal{B}$는 $M$의 basis이므로 

    $$V=\bigcup_{\substack{B\in\mathcal{B}\\B\subseteq V}}B$$

    로 쓸 수 있는데, 우변의 합집합의 조건을 만족하는 $B$는 $B\subseteq V\subseteq K$를 만족하므로, $\operatorname{cl}B\subseteq K$이고 따라서 relatively compact가 되어 $\\{U_i\\}$에 속한다. 즉, 임의의 $p\in M$에 대하여 $p\in U_i$이도록 하는 적절한 $i$가 존재한다.

2. 비슷하게, 임의의 $U_i,U_j$에 대하여 $p\in U_i\cap U_j$라 하자. 그럼 1번에서 만든 것과 동일하게 열린집합 $V_i,V_j$와 compact set들 $K_i$, $K_j$를 만들 수 있다. 이제 $V_i\cap V_j$를 $\mathcal{B}$의 원소들의 합집합으로 표현하면 $V_i\cap V_j\subseteq K_i\cap K_j$이므로 다시
    
    $$p\in B\subseteq V_i\cap V_j\subseteq K_i\cap K_j$$

    를 만족하는 $B\in\mathcal{B}$를 찾을 수 있고, 이러한 $B$는 compact set $K_i\cap K_j$의 부분집합이므로 relatively compact가 되어 $B\in\\{U_i\\}$이다. 

위의 1번과 2번에서, 모임 $\\{U_i\\}$가 $M$의 basis가 된다는 것을 확인할 수 있다. 

이제 $G_1=U_1$으로 두고, 

$$G_k=U_1\cup\cdots\cup U_{j_k}$$

가 정의되었다 하자. 귀납적으로 $j_{k+1}$을 

$$\operatorname{cl} G_k\subset\bigcup_{i=1}^{j_{k+1}} U_i$$

가 성립하고, $j_k$보다 큰 정수 중 가장 작은 것으로 두면 $\\{G_k\\}$는 열린집합들의 ascending chain이고 $\\{\operatorname{cl}G_k\\}$는 exhaustion이다. (<#ref#>)

이를 이용해 $M$이 paracompact임을 보일 수 있다. $\\{V_\alpha\\}\_{\alpha\in\Lambda}$가 임의의 open covering이라 하자. 각각의 $i$에 대하여, $\operatorname{cl}(G_i)\setminus G_{i-1}$은 집합 $G_{i+1}\setminus\operatorname{cl}(G_{i-2})$에 포함된 compact set이다. 이제 $\\{V_\alpha\\}$의 open refinement $\\{V\_\alpha\cap(G_{i+1}\setminus\operatorname{cl}(G_{i-2}))\\}$는 compact set $\operatorname{cl}(G_i)\setminus G_{i-1}$의 open covering으로서, finite subcover를 가진다. 또, 비슷하게 index가 작은 $\operatorname{cl}(G_2)\subseteq G_3$의 경우에도 $\operatorname{cl}G_2$를 덮는 유한한 $\\{V\_\alpha\cap G\_3\\}$의 subcover를 생각할 수 있다.  
이렇게 만든 subcover들의 모임이 $\\{V_\alpha\\}$의 open refinement가 되는 것은 자명하다. 또, 이 모임은 countable한 compact set $\operatorname{cl}(G_i)\setminus G_{i-1}$마다 유한히 많은 원소들을 모아서 만들어진 모임이므로 자연스럽게 countable이다. 임의의 점 $p\in M$은 정확히 하나의 $\operatorname{cl}(G_i)\setminus G_{i-1}$에만 포함되므로 이 모임은 locally finite이고, 마지막으로 이 모임의 임의의 원소는 충분히 큰 $N$에 대하여 compact set $\operatorname{cl}G_N$의 부분집합이므로 relatively compact이다.

</details>

---

**참고문헌**

**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  
**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013    

---


[^1]: 보편적으로 coordinate domain이 이 역할을 담당한다.
