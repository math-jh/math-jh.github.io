---

title: "Diagram chasing"
excerpt: "기본정의"

categories: [Math / Algebraic topology]
permalink: /ko/math/algebraic_topology/diagram_chasing
header:
    overlay_image: /assets/images/Algebraic_topology/Diagram_chasing.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-07-02
last_modified_at: 2022-07-02
weight: 2

---

필연적으로 homology는 대수학과 밀접한 관련이 있다. 이번 글에서는 이를 다루기 위한 기본적인 도구들을 리뷰한다. 이번 글에서 모든 group은 abelian group임을 가정한다.

## Exact sequence

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Group homomorphism들 

$$\cdots\longrightarrow A\overset{f}{\longrightarrow}B\overset{g}{\longrightarrow}C\longrightarrow \cdots$$

이 $B$에서 *exact*하다는 것은 $\ker g=\operatorname{im}f$임을 뜻한다. 또, 이러한 sequence가 *exact sequence<sub>완전열</sub>*이라는 것은 모든 곳에서 homomorphism들이 exact인 것이다.

</div>

Exact sequence 중 가장 단순한 예시는 다음의 *short exact sequence*이다.

$$0\longrightarrow A\overset{f}{\longrightarrow}B\overset{g}{\longrightarrow}C\longrightarrow0$$

두 개의 exact sequence가 주어졌을 때 적용할 수 있는 보조정리들을 소개한다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2 (The four lemma)**</ins> 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (The five lemma)**</ins> 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>
<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4 (The snake lemma)**</ins> 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

특히 snake lemma의 경우 이제 정의할 chain complex에서 유용하게 사용할 것이다.

## Chain complex

Exact sequence에서 중요한 성질 중 하나는 인접한 homomorphism을 두 번 따라가면 zero morphism이 된다는 사실이다. 이러한 성질은 다양한 상황에서 등장한다. 예를 들어 differential form을 다룰 때, $d^2=0$이 된다. 만일 

$$\Omega^0(M)\overset{d}{\longrightarrow}\Omega^1(M)\overset{d}{\longrightarrow}\Omega^2(M)\overset{d}{\longrightarrow}\cdots$$

가 exact sequence였다면, $d\omega=0$를 만족하는 differential form $\omega$에 대하여, 항상 적당한 $\eta$가 존재하여 $\omega=d\eta$로 쓸 수 있어야 할 것이다. 하지만 이는 일반적으로 참이 아니며, 따라서 위의 sequence는 exact sequence가 아니라는 것을 알 수 있다. 따라서 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> Homomorphism들의 sequence

$$C_\bullet:\qquad\cdots\longrightarrow C_{n+1}\overset{\partial}{\longrightarrow}C_n\overset{\partial}{\longrightarrow}C_{n-1}\longrightarrow\cdots$$

이 *chain complex*라는 것은 $\partial^2=0$인 것이다. 이 때 $\partial$들을 *boundary operator*, $C_n$의 원소를 *$n$-dimensional chain*이라 부른다.

</div>

위에서 예로 든 differential form들의 sequence $\Omega^\bullet(M)$의 경우에는 약간 상황이 다른데, 이들은 index가 증가하는 방향으로 이루어져 있다. 이를 *cochain complex*라 부르는데, 지금 우리 상황에서는 chain complex만이 관심의 대상이고, 또 cochain complex는 chain complex와 동일한 방식으로 다룰 수 있으므로 우리는 chain complex만 신경쓰기로 한다.

이전 글에서 했던 것과 같이, homology group을 정의할 수 있다. $C_n$에 속한 kernel $\ker\partial=Z_n(C)$라 적고, 또 $C_n$에 속한 imeage $\operatorname{im}\partial=B_n(C)$라 적자. 그럼 $Z_n$과 $B_n$의 원소들을 각각 $n$-dimensional cycle과 $n$-dimensional boundary라 부른다. 이 때 이들의 quotient $Z_n(C)/B_n(C)$를 $H_n(C)$로 적고, $n$-th homology group이라 부른다.

두 chain complex들 $C_\bullet,D_\bullet$이 주어졌다 하자. 그럼 $C_\bullet$에서 $D_\bullet$으로의 *chain transformation*은 다음의 diagram이 commute하도록 하는 homomorphism들 $f_n$의 모임 $f_\bullet=(f_n)$이다. 

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> Chain transformation $f_\bullet:C_\bullet\rightarrow D_\bullet$이 주어졌다 하자. 그럼 각각의 $f_n$은 $Z_n(C)$를 $Z_n(D)$로, $B_n(C)$를 $B_n(D)$로 옮긴다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

따라서 $f$는 $H_n(C)$를 $H_n(D)$로 옮긴다. 이를 우리는 $H_n(f)$로 적는다. 

## Homotopic transformations

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 두 chain transformation $f_\bullet,g_\bullet:C_\bullet\rightarrow D_\bullet$이 *homotopic*하다는 것은 적절한 homomorphism들의 모임

$$h_\bullet=\{h_n:C_n\rightarrow D_{n+1}\}$$

이 존재하여, 임의의 $n$에 대해

$$\partial\circ h_n+h_{n-1}\circ\partial=f_n-g_n$$

이 성립하는 것이다. 이 때 $h$를 *chain homotopy*라 부른다.

</div>

$h$를 homotopy라 부르는 이유는 조만간 보게 된다. 우선 다음을 증명한다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> Homotopic한 두 chain transformation $f_\bullet,g_\bullet:C_\bullet\rightarrow D_\bullet$에 대하여, 항상 $H_n(f)=H_n(g)$가 성립한다.

</div>

## Long exact sequence

세 chain complex $C_\bullet,D_\bullet, E_\bullet$이 주어졌다 하자. 다음의 sequence

$$0\longrightarrow C_\bullet\overset{f_\bullet}{\longrightarrow}D_\bullet\overset{g_\bullet}{\longrightarrow}E_\bullet\longrightarrow 0$$

이 chain complex들 사이의 short exact sequence라는 것은 임의의 $n$에 대하여 다음의 sequence

$$0\longrightarrow C_n\overset{f_n}{\longrightarrow}D_n\overset{g_n}{\longrightarrow}E_n\longrightarrow 0$$

가 short exact sequence인 것이다. 

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> Chain complex들 사이의 short exact sequence가 주어졌다 하자. 그럼 homology sequence들 사이의 *long exact sequence*가 잘 정의된다.

</div>

## Induced chain map

연속함수 $f:X\rightarrow Y$가 주어졌다 하자. 그럼 각각의 $\sigma\in C_n(X)$에 대하여 $\sigma\mapsto f\circ\sigma$를 통해 함수 $f_n:C_n(X)\rightarrow C_n(Y)$가 정의된다. 어렵지 않게 $f_\bullet=(f_n)$이 chain transformation임을 확인할 수 있다. 이 때, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> 두 연속함수 $f,g:X\rightarrow Y$가 homotopic하다면 모든 $n$에 대해 $H_n(f)=H_n(g)$가 성립한다.

</div>