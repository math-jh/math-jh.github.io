---

title: "이항관계의 그래프"
excerpt: "이항관계의 그래프와 역, 합성"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/binary_relation

header:
    overlay_image: /assets/images/Set_theory/Binary_relation.png
    overlay_filter: 0.5

sidebar: 
    nav: "set-ko"

date: 2021-08-14
last_modified_at: 2022-05-12

weight: 3

---

## 그래프와 이항관계

우리가 순서쌍을 도입한 이유는 이항관계를 살펴보기 위해서였다. 앞으로 별 말이 없으면 대문자 $R$은 이항관계를 뜻한다. 예를 들어, $x\mathrel{R}y$라는 표기는 $x$와 $y$가 $R$에 의해 관계되어 있다는 뜻이다. 

우선 다음을 정의하자.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $G$가 *그래프<sub>graph</sub>*라는 것은 $G$의 모든 원소가 순서쌍이라는 것이다.

</div>

이항관계 $R$에 대해, 만일 어떤 그래프 $G$가 존재하여 $(x,y)\in G\iff x\mathrel{R}y$가 성립한다면 관계 $R$이 <em_ko>그래프를 갖는다</em_ko>고 하고, 이를 $R$의 그래프라 부른다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 이항관계 $=$을 생각해보자. 즉, $x$와 $y$는 $x=y$일 때 서로 관계되어 있다. 그럼 $=$는 그래프를 갖지 않는다. 만일 그래프가 존재한다면 그건 두 개의 전체집합의 곱이어야 한다.

</div>

전체집합 두 개의 곱이 존재한다면, 다음 명제에 의해 전체집합 또한 존재해야 하고 이는 [§ZFC 공리계, 예시 4](/ko/math/set_theory/zfc_axioms#ex4)에 모순이므로 관계 $=$는 그래프를 갖지 않는다.  
그러나 앞으로 우리는 주로 그래프를 갖는 관계만을 생각할 것이므로 이항관계와 그래프를 같은 것으로 생각해도 큰 무리는 없다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> $G$가 그래프라 하자. 그럼 유일한 두 개의 집합 $A$, $B$가 존재하여,  

<ul>
<li> <phrase>$x\in A$인 것</phrase>과 <phrase>어떤 $y$가 존재하여 $(x,y)\in G$인 것</phrase>이 동치이고,</li>
<li> <phrase>$y\in B$인 것</phrase>과 <phrase>어떤 $x$가 존재하여 $(x,y)\in G$인 것</phrase>이 동치이다.</li>
</ul>

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$G$가 그래프라 하고, 집합 $\bigcup(\bigcup G)$를 생각하자. 약간의 계산을 해 보면, 만일 $(x,y)\in G$라면 $x,y\in\bigcup(\bigcup G))$임을 알 수 있다. 따라서 성질 $P$를

> $P(t)$: 어떠한 $s$가 존재하여 $(s,t)\in G$이다.

로 정의하면, 다음의 집합

$$A=\left\{x:\left(x\in\bigcup\left(\bigcup G\right)\right)\wedge P(x)\right\}$$

를 얻는다. 따라서 첫 번째 문장이 성립하며, 이와 유사하게 성질 $Q$를

> $Q(s)$: 어떠한 $t$가 존재하여 $(s,t)\in G$이다.

로 정의하면 집합 $B$를 얻는다.

</details>

[§순서쌍, 정의 7](/ko/math/set_theory/ordered_pair#df7)에서 했듯 이들을 각각 첫 번째와 두 번째 *projection*이라 부르고, $\operatorname{pr}_1G$와 $\operatorname{pr}_2G$로 쓴다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 집합 $A$와 $B$ 사이의 *correspondence*라는 것은 다음의 triple

$$\Gamma=(G, A, B)$$

을 의미한다. 여기서 $G$는 $\operatorname{pr}_1 G\subseteq A$, $\operatorname{pr}_2 G\subseteq B$를 만족하는 그래프이다. 이 때, $G$는 $\Gamma$의 그래프, $A$는 *source*, $B$는 *target*이라 불린다. 또,

- 만일 $x\in \operatorname{pr}_1G$라면 $\Gamma$가 $x$에서 정의되었다고 하며, $\operatorname{pr}_1G$는 $\Gamma$의 *정의역<sub>domain</sub>*이라 불린다. 
- 만일 $y\in \operatorname{pr}_2G$라면, $y$는 $\Gamma$가 갖는 값이라 하고, $\operatorname{pr}_2G$는 $\Gamma$의 *치역<sub>range</sub>*이라 부른다.
 
</div>

$\Gamma=(G,A,B)$가 correspondence라 하자. 그럼 [§순서쌍, 명제 9](/ko/math/set_theory/ordered_pair#pp9)에 의하여,

$$G\subseteq \operatorname{pr}_1 G\times\operatorname{pr}_2G\subseteq A\times B$$

이므로 곱집합 $A\times B$는 $A$를 source로, $B$를 target으로 갖는 그래프 중 가장 큰 것이라 할 수 있다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> $G$가 그래프, $A$가 집합이라 하자. 그럼 <phrase>$G$에 의해 $A$의 원소와 관계되는 모든 원소들의 집합</phrase>을 $G$에 의한 $A$의 *상<sub>image</sub>*라 부르고 , $G(A)$로 표기한다.

</div>

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> $G$가 그래프라 하고, 임의의 집합 $A$와 그 부분집합 $X$를 생각하자. 그럼 $G(X)\subseteq G(A)$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$y\in G(X)$라 하자. 그럼 어떤 $x\in X$가 존재하여 $(x,y)\in G(X)$이다. 이제 $X\subseteq A$로부터 $x\in A$이므로, $y\in G(A)$이다.

</details>

위의 명제에 의하여 임의의 $A$에 대해 

$$G(A)=\operatorname{pr}_2\{z\in G:\text{$\operatorname{pr}_1z\in A$}\}\subset\operatorname{pr}_2G$$

이고, 따라서 $G(A)\subset\operatorname{pr}_2G$가 성립한다. 특히 $A=\emptyset$이라면 $G(A)=\emptyset$이며, 더 일반적으로 만일 $A\cap\operatorname{pr}_1G=\emptyset$이라면 $G(A)=\emptyset$이다.

만일 어떤 $x$에 대해 $A=\\{x\\}$라면 $G(A)$를 마치 $x$에서의 $G$의 함숫값처럼 생각할 수 있다. 

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> 그래프 $G$에 대하여, 집합 $G(\\{x\\})$를 $x$에서의 $G$의 *section*이라 부른다.

</div>

이 집합을 마치 $x$에서의 $G$의 함숫값처럼 $G(x)$로 적기도 한다. 이 <em_ko>함숫값</em_ko>은 유일하지 않으며, 따라서 $G(x)$ 또한 여러 개의 원소를 가질 수 있다.

## 이항관계의 역과 합성

우리는 이제 이항관계의 역, 그리고 이들의 합성 등을 정의한다.

<div class="definition" markdown="1">

<ins id="df8">**정의 8**</ins> $G$가 그래프라 하자. 그럼 $(x,y)\in G$를 만족하는 모든 $(y,x)$들로 이루어진 그래프를 $G$의 *역<sub>inverse</sub>*이라 부르고 이를 $G^{-1}$로 표기한다. 또, 집합 $G^{-1}(A)$를 $A$의 *preimage<sub>역상</sub>*이라 부른다. 만일 $G^{-1}=G$라면 $G$가 *symmetric<sub>대칭적</sub>*하다고 한다.

</div>

명시적으로 $G^{-1}$은 다음의 식

$$(x,y)\in G\iff (y,x)\in G^{-1}$$

이 성립하도록 하는 집합이다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $G^{-1}$의 역은 $G$이다. 또, $\operatorname{pr}_1G^{-1}=\operatorname{pr}_2G$이고 $\operatorname{pr}_2G^{-1}=\operatorname{pr}_1G$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 주장은 다음의 식

$$(x,y)\in G\iff (y,x)\in G^{-1}\iff (x,y)\in (G^{-1})^{-1}$$ 

에 의해 자명하다. 

둘째 주장을 보자. 만일 $x\in\operatorname{pr}_1G^{-1}$라면, 어떠한 $y$가 존재하여 $(x,y)\in G^{-1}$이다. 이제 $(y,x)\in G$이므로 $x\in\operatorname{pr}_2G$가 성립한다. 이 논증을 뒤집으면 $\operatorname{pr}_2G\subset\operatorname{pr}_1G^{-1}$임을 증명할 수 있다.

아직 보이지 않은 $\operatorname{pr}_2G^{-1}=\operatorname{pr}_1G$의 경우, 방금 주장의 $G$ 자리에 대신 $G^{-1}$을 넣으면 된다.   

</details>

주어진 집합 $A,B$에 대하여, $A\times B$는 $A$를 source로, $B$를 target으로 갖는 가장 큰 그래프였다. 따라서 두 개의 식

$$\operatorname{pr}_1(A\times B)^{-1}=\operatorname{pr}_2(A\times B)=B,\qquad \operatorname{pr}_2(A\times B)^{-1}=\operatorname{pr}_1(A\times B)=A$$

에서, $(A\times B)^{-1}\subseteq B\times A$이다. 반대로, 만일 $(y,x)\in B\times A$라면 $x\in A$, $y\in B$이므로 $(x,y)\in A\times B$이고, 따라서 $(y,x)\in (A\times B)^{-1}$이므로 $(A\times B)^{-1}=B\times A$가 성립한다.

<div class="definition" markdown="1">

<ins id="df10">**정의 10**</ins> $G$와 $G'$가 그래프라 하자. 이 두 그래프의 *합성<sub>composition</sub>* $G'\circ G$는 $(x,y)\in G$이고 $(y,z)\in G'$이도록 하는 $y$가 존재하는 순서쌍들 $(x,z)$의 집합이다.

</div>

이렇게 정의한 그래프의 합성이 위에서 정의한 역과 어떠한 관계가 있는지 궁금한 것이 당연하다.

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> $G$, $G'$가 그래프라 하자. 그럼 $G'\circ G$의 역은 $G'^{-1}\circ G^{-1}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$(z,x)\in (G'\circ G)^{-1}$인 것은 $(x,z)\in G'\circ G$인 것과 동치이다. 그리고 이는 다시 <phrase>어떠한 $y$가 존재하여 $(x,y)\in G$이고 $(y,z)\in G'$인 것</phrase>과 동치이다. 이 조건을 만족하는 $y$는 <phrase>$(y,x)\in G^{-1}$이고 $(z,y)\in G'^{-1}$</phrase> 또한 만족하므로, 합성의 정의에 의해 $(z,x)\in G'^{-1}\circ G^{-1}$이 성립한다. 반대방향도 동일하게 보일 수 있다.

</details>

또한, 그래프의 합성은 결합법칙을 만족한다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> 두 그래프의 합성은 결합법칙을 만족한다. 즉, 두 그래프 $G$, $G'$에 대하여 

$$(G_3\circ G_2)\circ G_1=G_3\circ(G_2\circ G_1)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $(x,w)$가 $(G\_3\circ G\_2)\circ G\_1$의 원소인 것과 $G\_3\circ(G\_2\circ G\_1)$의 원소임이 동치임을 보이면 충분하다.  

우선 $(x,w)\in (G\_3\circ G\_2)\circ G\_1$은 <phrase>어떠한 $y$가 존재하여 $(x,y)\in G_1$이고 $(y,w)\in G_3\circ G_2$</phrase>와 동치이다. 그런데 뒤의 조건은 다시 <phrase>어떠한 $z$가 존재하여 $(y,z)\in G_2$이고 $(z,w)\in G_3$</phrase>과 동치이므로, 이 조건은 <phrase>$(x,z)\in G_2\circ G_1$이고 $(z,w)\in G_3$</phrase>과 동치이다. 따라서 이는 <phrase>$(x,w)\in G_3\circ(G_2\circ G_1)$</phrase>과 동치이다.

</details>

따라서 이 공통의 결과인 $(G\_3\circ G\_2)\circ G\_1=G\_3\circ(G\_2\circ G\_1)$을 괄호 없이 $G\_3\circ G\_2\circ G\_1$로 표현해도 아무런 문제가 없다. 

몇 가지 명제들을 더 살펴보자.

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> $G$, $G'$가 그래프이고 $A$가 집합이라 하자. 그럼

$$(G'\circ G)(A)=G'(G(A))$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞선 명제와 같이 진행한다. 

어떠한 $z$에 대하여 $z\in (G'\circ G)(A)$인 것은 <phrase>어떠한 $x\in X$가 존재하여 $(x,z)\in G'\circ G$인 것</phrase>과 동치이다. 그런데 이는 다시 <phrase>어떠한 $y$가 존재하여 $(x,y)\in G$이고 $(y,z)\in G'$인 것</phrase>과 동치이다. $y\in G(A)$이므로, $z\in G'(G(A))$이다. 이 논리를 거꾸로 뒤집으면 반대방향의 증명이 된다.

</details>

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14**</ins> Correspondence $\Gamma=(G,A,B)$에 대하여 $X\subseteq A$, $Y\subseteq B$라 하자. 그럼 

1. $G^{-1}(G(X))\supset X\cap\operatorname{pr}_1G$  
2. $G(G^{-1}(Y))\supset Y\cap\operatorname{pr}_2G$  

가 각각 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

본격적으로 증명을 시작하기 전에, 위의 두 식은 <em_ko>모든</em_ko> $G$에 대해 성립해야 하므로, $G$ 자리에 $G^{-1}$을 집어넣어도 성립해야 한다. 따라서, 1만 보이면 2는 [명제 9](#pp9)에 의해 자명하다.  

이제 $x\in X\cap\operatorname{pr}\_1G$라 하자. 그럼 $x\in\operatorname{pr}\_1G$에서, 어떠한 $y$가 존재하여 $(x,y)\in G$이고, $x\in X$이므로 이 $y$는 $y\in G(X)$를 만족한다. 이제 $(y,x)\in G^{-1}$이므로, $x\in G^{-1}(G(X))$이다.

</details>

<div class="proposition" markdown="1">

<ins id="pp15">**명제 15**</ins> $G$, $G'$가 그래프라 하자. 그럼 다음의 두 식이 성립한다.

$$ \operatorname{pr}_1(G'\circ G)=G^{-1}(\operatorname{pr}_1G'),\quad \operatorname{pr}_2(G'\circ G)=G'(\operatorname{pr}_2G).$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음 implication들의 chain

$$\begin{aligned}
        x\in\operatorname{pr}_1(G'\circ G)&\iff \exists z\big((x,z)\in G'\circ G\big)\\
        &\iff\exists y,z\big(((x,y)\in G)\wedge((y,z)\in G')\big)\\
        &\iff\exists y\big(((x,y)\in G)\wedge(y\in\operatorname{pr}_1G')\big)\\
        &\iff x\in G^{-1}(\operatorname{pr}_1 G').
\end{aligned}$$

에 의해 자명하다. 두 번째 식도 마찬가지로 보일 수 있다.

</details>

마지막으로, 특별한 correspondence 하나를 소개한다. 

<div class="definition" markdown="1">

<ins id="df16">**정의 16**</ins> 집합 $A$에 대하여, $\Delta_A$는 $x\in A$를 만족하는 모든 $(x,x)$들의 모임을 뜻한다. 이를 $A\times A$의 *diagonal*이라 부른다.

</div>

정의에 의해 $\operatorname{pr}_1\Delta_A=\operatorname{pr}_2\Delta_A=A$이므로, 다음과 같은 correspondence

$$\operatorname{id}_A=\left(\Delta_A,A,A\right)$$

가 존재한다. $A$를 source로 갖는 그래프 $G$ 혹은, $A$를 target으로 갖는 그래프 $G'$에 대하여 두 식

$$G\circ\Delta_A=G,\qquad \Delta_A\circ G'=G'$$

이 항상 성립하므로 위에서 정의한 correspondence를 *identity correspondence*이라 부르는 것이 어색하지 않다. 이 correspondence는 집합론 바깥에서도 많이 사용된다.

---
**참고문헌**

**[Bou]** N. Bourbaki, *Theory of Sets*. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

