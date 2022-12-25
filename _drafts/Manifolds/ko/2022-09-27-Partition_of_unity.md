---

title: "단위분할"
excerpt: "Partition of unity와 그 결과들"

categories: [Math / Manifold]
permalink: /ko/math/manifold/partition_of_unity
header:
    overlay_image: /assets/images/Manifold/Partition_of_unity.png
    overlay_filter: 0.5
sidebar: 
    nav: "manifold-ko"

date: 2022-09-27
last_modified_at: 2022-09-27
weight: 2

---

## Partition of unity

앞선 글에서 우리는 임의의 topological manifold $M$이 paracompact임을 증명했다. 이 덕분에 $M$ 위에는 *partition of unity*가 존재한다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$와, $X$의 open covering $\\{U\_i\\}\_{i\in I}$가 주어졌다 하자. 이 때, 연속함수 $\phi_i:X\rightarrow [0,1]$들의 모임 $\\{\phi\_i\\}\_{i\in I}$가 $\\{U\_i\\}$에 의해 dominate되는 *partition of unity<sub>단위분할</sub>*라는 것은 다음의 세 조건

1. $\operatorname{supp}\phi\_i\subseteq U\_i$,
2. $\\{\operatorname{supp}\phi\_i\\}_{i\in I}$가 locally finite,
3. 모든 $x$에 대하여 $\sum\_{i\in I}\phi\_i(x)=1$.

을 만족하는 것이다.

</div>

위의 정의에서, $\\{\operatorname{supp}\phi\_i\\}\_{i\in I}$가 *locally finite*이라는 것은, 임의의 $x\in X$마다 적당한 열린근방 $U$가 존재하여, $U$가 오직 <em_ko>유한 개의</em_ko> $\operatorname{supp}\phi_i$들과만 만나는 것이다. 따라서 임의의 $x\in X$는 오직 유한히 많은 $\operatorname{supp}\phi_i$에만 속해 있으며, 특히 3번 조건의 합 $\sum\phi_i(x)$는 $x\in X$가 고정될 때마다 유한합이 된다.  

또, 만일 $\bigcup\operatorname{supp}\phi_i\neq X$라면 $x\not\in\bigcup\operatorname{supp}\phi_i$인 $x$에 대하여 $\sum\phi_i(x)=0$일 것이므로, 3번 조건은 모임 $\\{\operatorname{supp}\phi_i\\}$이 $X$의 covering이 된다는 것을 함의한다.

## Urysohn lemma

다음 명제는 특히 임의의 topological manifold에 대해서도 성립한다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 임의의 paracompact, Hausdorff space $X$는 normal space이다.

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

<ins id="lem3">**보조정리 3**</ins> 임의의 paracompact Hausdorff space $X$와, $X$의 open covering $\\{U\_i\\}\_{i\in I}$가 주어졌다 하자. 그럼 $\operatorname{cl}(V_b)\subseteq U_i$가 모든 $i\in I$에 대해 성립하도록 하는 $X$의 locally finite open covering $\\{V_i\\}$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathcal{C}$를 <phrase>적당한 $i\in I$가 존재하여 $\operatorname{cl}(C)\subseteq U_i$인 열린집합 $C$들의 모임</phrase>으로 정의하자. 임의의 $x\in X$와 $x$를 포함하는 $U_i$에 대하여 $C_i=X\setminus U_i$는 $x$를 포함하지 않는 닫힌집합이고, 따라서 $X$의 regularity에 의하여 $x$와 $C_i$를 분리하는 서로소인 열린집합 $V_i$와 $W_i$가 각각 존재한다.  그럼 $V_i\subseteq X\setminus W_i$이고, 따라서

$$\operatorname{cl}V_i\subseteq X\setminus W_i\subseteq X\setminus C_i=U_i$$

가 성립한다. 즉, 임의의 $x\in X$에 대해 그 closure가 어떤 $U_i$에 포함되도록 하는 열린집합 $V_i$가 항상 존재하고 따라서 $\mathcal{C}$는 open covering이다. $X$의 paracompactness를 이용하여  $\mathcal{C}$의 locally finite open refinement $\mathcal{D}$를 얻자.

적당한 index set $J$를 통해 $\mathcal{D}=\\{W\_j\\}\_{j\in J}$라 적으면, 정의에 의해 $W_j$는 어떠한 $\mathcal{C}$의 원소 $C$에 포함되며, 다시 $C$는 적당한 $i\in I$에 대해 $\operatorname{cl}C\subseteq U_i$를 만족한다. 따라서 각각의 $j$마다 이러한 $i$를 하나씩 뽑아 함수 $f:J\rightarrow I$를 만들 수 있다. 이제 각각의 $i\in I$에 대하여

$$V_i=\bigcup_{j\in f^{-1}(i)} W_j$$

으로 정의하자. 그럼 $\\{V_i\\}_{i\in I}$가 정확히 우리가 원하는 open covering이 된다.

우선 우변의 $W_j$들은 모두 $\operatorname{cl}W_j\subseteq U_i$를 만족하고, 따라서

$$\operatorname{cl}V_i=\operatorname{cl}\left(\bigcup_{j\in f^{-1}(i)}W_j\right)=\bigcup_{j\in f^{-1}(i)}\operatorname{cl}W_j\subseteq U_i$$

가 된다. 또 $\mathcal{D}$는 locally finite이므로, 임의의 $x\in X$마다 적당한 열린근방 $U$가 존재하여 유한히 많은 $W_j$들과만 만나도록 할 수 있다. 그럼 이 $U$는 $j\in f^{-1}(i)$를 만족하는 $V_i$들과만 만나므로, 마찬가지로 $\\{V_i\\}$도 locally finite이다.

</details>

## Partition of unity의 존재성

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 임의의 paracompact Hausdorff space $X$와, $X$의 open covering $\\{U\_i\\}\_{i\in I}$에 대하여, $\\{U_i\\}$에 의해 dominate되는 partition of unity가 존재한다.

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

특히 임의의 topological manifold는 paracompact Hausdorff space이므로, $M$은 partition of unity를 갖는다. 위의 정리의 증명에서 우리는 $\psi_i$들을 연속함수로 잡았는데, 다음 글에서 differentiable manifold를 정의하고, 이 부분을 그에 맞게 수정해야 한다.

