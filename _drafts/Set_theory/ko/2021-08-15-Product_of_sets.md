---

title: "집합의 곱"
excerpt: "집합들 사이의 곱"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/product_of_sets
header:
    overlay_image: /assets/images/Set_theory/Product_of_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-15
last_modified_at: 2022-05-17
weight: 8

---

## 집합의 곱

순서쌍을 가장 자연스럽게 일반화하는 것은 함수이다. 예컨대 $n$-tuple은 $I=\\{1,2,\cdots, n\\}$을 정의역으로 갖는, $i$를 넣으면 $i$번째 성분을 돌려주는 함수로 생각할 수 있다.

한편 집합 $A_1$, $A_2$에 대하여 $A_1\times A_2$은 순서쌍들 $(x_1,x_2)$의 모임이다. 위와 같이 순서쌍을 함수로 보자면, $A_1\times A_2$는 정의역 $\\{1,2\\}$를 갖는 <em_ko>함수들의 모임</em_ko>으로, 이 함수 $f$들은 $f(1)=x_1\in A_1$, $f(2)=x_2\in A_2$를 만족한다. 

그럼 일반적인 family의 곱은 다음과 같이 정의하는 것이 자연스럽다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $(A_i)\_{i\in I}$가 집합들의 family라 하자. 그럼 $I$에서 $\bigcup A_i$로의 모든 functional graph들 중, $x_i=F(i)\in A_i$를 만족하는 것들의 모임 $P$를 이 family의 *곱<sub>product</sub>*이라 부른다.

집합들의 family를 표기할 때와 마찬가지로, $P$의 원소들을 $(x_i)\_{i\in I}$로 적으며, 각각의 $x_i$를 *$i$번째 성분*이라 부르며, $F\in P$를 $F(i)$로 대응시키는 함수를 *$i$번째 성분함수*라 부르고 $\operatorname{pr}\_i$로 적는다.

</div>

따라서 집합의 곱을 생각하는 것은 <em_ko>함수들의 집합</em_ko>을 생각하는 것과 같다. 

집합 $A,B$가 주어졌다고 하자. 그럼 $A$에서 $B$로의 functional graph는 $\mathcal{P}(A\times B)$의 원소이다. 따라서 $A$에서 $B$로의 functional graph들의 모임은 $\mathcal{P}(A\times B)$의 부분집합이 된다. 이를 우리는 $B^A$로 적는다. $A$에서 $B$로의 함수들의 집합을 $\operatorname{Fun}(A,B)$라 하자. 그럼 임의의 $G\in B^A$에 대하여, $g=(G,A,B)$는 $A$에서 $B$로의 함수이며, 이 대응 $G\mapsto g$는 $B^A$에서 $\operatorname{Fun}(A,B)$로의 함수이다. 

한편 $\operatorname{Fun}(A,B)$에서 $B^A$로의 <phrase>함수 $g$를 받아 그 그래프를 주는 대응</phrase>을 생각하자. 그럼 이 대응은 $\operatorname{Fun}(A,B)$에서 $B^A$로의 함수이고, 위에서 정의한 대응의 역함수임을 쉽게 확인할 수 있다. 즉 $B^A$와 $\operatorname{Fun}(A,B)$ 사이의 자연스러운 전단사함수가 존재하여 이 두 집합을 서로 같은 것으로 생각할 수 있다.

함수들 $u:A'\rightarrow A$와 $v:B\rightarrow B'$가 주어졌다고 하고, 다음의 diagram을 생각하자.

![induced_mapping](/assets/images/Set_theory/Product_of_sets-1.png){:width="129.3px"  class="invert" .align-center}

이 diagram에서, 어떤 함수 $f:A\rightarrow B$가 주어질 때마다 우리는 이에 해당하는 $A'$에서 $B'$로의 함수 $\tilde{f}=v\circ f\circ u$를 생각할 수 있다. 이 대응 $f\mapsto \tilde{f}$는 $\operatorname{Fun}(A, B)$에서 $\operatorname{Fun}(A', B')$로의 함수이다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위의 diagram에서, $u$가 전사함수고 $v$가 단사함수라면 $f\mapsto \tilde{f}$는 단사함수다. 만일 $u$가 단사함수고 $v$가 전사함수라면, $f\mapsto \tilde{f}$는 전사함수다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $u$, $v$가 각각 전사함수와 단사함수라 하자. 주어진 함수 $f\mapsto\tilde{f}$가 단사임을 보이기 위해서는 $\tilde{f}=\tilde{g}$라면 $f=g$임을 보여야 한다. $s$와 $r$을 각각에 해당하는 section과 retraction이라 하자. 만일 $\tilde{f}=\tilde{g}$라면, 

$$\begin{aligned}
  f&=\operatorname{id}_B\circ f\circ\operatorname{id}_A=(r\circ v)\circ f\circ(u\circ s)=r\circ(v\circ f\circ u)\circ s\\
  &=r\circ\tilde{f}\circ s=r\circ\tilde{g}\circ s\\
  &=r\circ(v\circ g\circ u)\circ s=(r\circ v)\circ g\circ (u\circ s)=\operatorname{id}_B\circ g\circ\operatorname{id}_A=g
\end{aligned}$$

이므로 $f=g$이다. 따라서 주어진 함수는 단사함수다. 

비슷하게 $u$와 $v$가 각각 단사함수, 전사함수라 하자. 임의의 $f'\in\operatorname{Fun}(A',B')$에 대하여 $\tilde{f}=f'$인 $f\in\operatorname{Fun}(A,B)$가 존재함을 보여야 한다. $r'$, $s'$가 각각 $u$와 $v$의 retraction과 section이라 하자. 그럼

$$f'=\operatorname{id}_{B'}\circ f'\circ\operatorname{id}_{A'}=(v\circ s')\circ f'\circ(r'\circ u)=v\circ(s'\circ f'\circ r')\circ u$$

이므로, $f=s'\circ f'\circ r'$는 $\operatorname{Fun}(A,B)$의 원소이며 $f'=\tilde{f}$를 만족한다. 따라서 주어진 함수는 전사함수다.

</details>

특별히 만일 $u$와 $v$가 모두 전단사라면 $f\mapsto \tilde{f}$ 또한 전단사함수가 된다. 

앞서 집합들 사이의 합이 universal property를 만족했었는데, 마찬가지로 곱도 비슷한 universal property를 만족한다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> 집합들의 family $(A_i)$들의 곱 $P$와, 성분함수들 $\operatorname{pr}\_i:P\rightarrow A_i$가 주어졌다 하자. 다른 집합 $B$와, 함수들 $f_i:B\rightarrow A_i$가 주어졌다고 하면, 식 $f_i=\operatorname{pr}\_i\circ f$를 만족하도록 하는 유일한 함수 $f:B\rightarrow P$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 주어진 조건 $f\_i=\operatorname{pr}\_i\circ f$를 만족하는 함수 $f,f'$가 주어졌다 하자. 우리는 임의의 $y\in B$에 대해 $f(y)=f'(y)$임을 보여야 한다. 그런데 $f(y)$와 $f'(y)$는 어차피 $A$의 원소이므로 함수(순서쌍)이고, 따라서 $i$가 대응되는 값($i$번째 좌표)들에 의해 결정된다. 따라서 임의의 $y\in B$와 $i\in I$가 주어졌다고 할 때, $\operatorname{pr}\_i(f(y))=\operatorname{pr}\_i(f'(y))$라는 것을 보이면 충분하다. 그런데

$$\operatorname{pr}_i(f(y))=f_i(y)=\operatorname{pr}_i(f'(y))$$  

이므로, 그러한 함수 $f$는 유일해야 한다.

존재성의 경우, 마찬가지로 위의 유일성 증명에 힌트를 얻어 $f(y)$의 값을

> $(f(y))(i)=f_i(y)$를 만족하는 함수 (혹은 $i$번째 좌표가 $f_i(y)$인 순서쌍)

으로 정의한 후 이 대응 $y\mapsto f(y)$가 실제로 함수임을 보이면 된다. 

</details>

이제 [정리 3](#thm3)의 조건을 만족하는 $(P, \operatorname{pr}\_i)$가 적어도 하나는 존재하므로 ([정의 1](#df1)), 이를 곱집합의 정의로 삼아도 된다. 즉,  $(A\_i)\_{i\in I}$들의 곱은 다음의 universal property를 만족하는 집합 $\prod\_{i\in I} A\_i$와 함수들 $\operatorname{pr}\_i:\prod\_{i\in I}A\_i\rightarrow A_i$이라 할 수 있다.

![universal_property_of_product](/assets/images/Set_theory/Product_of_sets-2.png){:width="283.65px" class="invert" .align-center}

[§집합의 합, 따름정리 9](/ko/math/set_theory/sum_of_sets#crl9)와 정확하게 같은 논리를 펼치면 이 universal property를 만족하는 대상 및 $\operatorname{pr}\_i$들 또한 unique up to bijection임을 확인할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> 집합 $A$, $B$, $C$에 대해 $f:B\times C\rightarrow A$라 하자. 만일 $\tilde{f}$가 $C$에서 $\operatorname{Fun}(B,A)$로의 함수 $y\mapsto f(-,y)$라면, $f\mapsto\tilde{f}$는 전단사함수이다. 즉, $\operatorname{Fun}(B\times C,A)$와 $\operatorname{Fun}(C, \operatorname{Fun}(B, A))$ 사이의 전단사함수가 존재한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>
우선 $\tilde{f}$는 $C$에서 $\operatorname{Fun}(B,A)$로의 함수이므로, $\tilde{f}\in\operatorname{Fun}(C,\operatorname{Fun}(B,A))$이다. 따라서 주어진 함수는 $\operatorname{Fun}(B\times C, A)$에서 $\operatorname{Fun}(C, \operatorname{Fun}(B,A))$로의 함수이다. 우리는 이 함수가 전단사임을 보이기 위해 역함수를 만들 것이다.

$g\in\operatorname{Fun}(C, \operatorname{Fun}(B,A))$가 주어졌다고 하자. 그럼 임의의 $y\in C$에 대하여, $g(y)$는 $\operatorname{Fun}(B, A)$의 원소이다. 이제 $\bar{g}:B\times C\rightarrow A$를 $(x, y)$를 $g(y)(x)$로 보내는 함수로 정의하자. 그럼 임의의 $g\in \operatorname{Fun}(C,\operatorname{Fun}(B,A))$에 대하여, $g$를 $\bar{g}$로 보내는 함수

$$\begin{aligned}
-:\operatorname{Fun}(C, \operatorname{Fun}(B,A))&\rightarrow\operatorname{Fun}(B\times C,A)\\
g\phantom{function}&\mapsto\phantom{function}\bar{g}
\end{aligned}$$

를 생각할 수 있다. 앞서 말한대로, 우리는 이 함수 $-$가 원래의 함수

$$\begin{aligned}
\sim\;:\operatorname{Fun}(B\times C,A)&\rightarrow\operatorname{Fun}(C, \operatorname{Fun}(B,A))\\
f\phantom{function}&\mapsto\phantom{function}\tilde{f}
\end{aligned}$$

의 역함수임을 보여야 한다.

임의의 $f:B\times C\rightarrow A$에 대하여, $\tilde{f}\in \operatorname{Fun}(C, \operatorname{Fun}(B, A))$이다. 이제 이 함수를 거꾸로 $-$를 타고 $\operatorname{Fun}(B\times C,A)$로 보내자. 그럼 이 결과 $\bar{\tilde{f}}$는 $(x, y)$를 $\tilde{f}(y)(x)$로 보내는 함수이다. 그런데 $\tilde{f}(y)$는 함수 $f(-, y)$이므로 $\bar{\tilde{f}}=f$이다.  
한편 임의의 $g\in\operatorname{Fun}(C, \operatorname{Fun}(B, A))$에 대하여, $\bar{g}$를 먼저 적용한 후 $\tilde{\bar{g}}$를 조사해보면, $\tilde{\bar{g}}$는 $y\mapsto \bar{g}(-,y)$로 정해지는 함수이다. 그런데 $\bar{g}$의 정의에 의하여 이는 다시 $y$를 $g(y)(-)$로 보내는 함수이다. 즉 $\tilde{\bar{g}}$는 다시 $g$가 된다. 이로부터 $\bar{\tilde{f}}=f$이고 $\tilde{\bar{g}}=g$이므로 이들은 서로 역함수 관계이다. 즉, 우리는 다음을 보인 것이다.

$$\begin{aligned}
  f\overset{\sim}{\longrightarrow}&\tilde{f}\overset{-}{\longrightarrow}\bar{\tilde{f}}=f,\\
  g\overset{-}{\longrightarrow}&\bar{g}\overset{\sim}{\longrightarrow}\tilde{\bar{g}}=g
\end{aligned}$$

그러므로 $\sim\;:f\mapsto\tilde{f}$는 전단사이다. 
</details>

우리는 합집합을 정의한 직후에, index set을 전사함수를 통해 바꾸어도 아무런 일도 일어나지 않음을 보았는데, 집합들의 곱에서는 전단사함수를 통해 바꾸어도 아무런 일도 일어나지 않는다. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $(A_i)\_{i\in I}$가 집합들의 family이고 $u:K\rightarrow I$가 전단사라 하자. 만일 $U$가 $u$의 그래프라면 $F\mapsto F\circ U$는 전단사함수이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>
다음의 diagram을 생각하자.

![induced_bijection](/assets/images/Set_theory/Product_of_sets-3.png){:width="275.25px"  class="invert" .align-center}

여기서 $v$는 $(x_i)\_{i\in I}$를 $(x\_{u(k)})\_{k\in K}$로 대응시키는 전단사함수이다. 그럼 위의 [명제 2](#pp2)에 의하여 $F\mapsto F\circ U$는 전단사다.
</details>

합집합, 교집합과 마찬가지로, 곱집합의 결합법칙 또한 성립한다. 하지만 결합법칙이라는 이야기를 하기 위해서는 우선 부분곱을 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> Family $(A_i)\_{i\in I}$와 그 product $\prod\_{i\in I} A_i$가 주어졌다고 하자. 그럼 index set의 부분집합 $J\subseteq I$에 대하여, $\prod\_{j\in J} A_j$를 *부분곱<sub>partial product</sub>*이라 부른다. 

</div>

$\prod\_{i\in I}A\_i$의 부분곱 $\prod\_{j\in J}A_j$가 주어졌다 하자. 그럼 임의의 $F\in\prod\_{i\in I}A\_i$에 대하여 함수 $F\circ\Delta_J$는 정의역 $J$를 갖는 함수이며, 각각의 $j$에 대하여 $(F\circ\Delta_J)(j)=F(j)\in A_j$이고 따라서 $F\circ\Delta_J$는 $\prod\_{j\in J}A_j$의 원소이다. 

위의 문단에 의하여, $F\mapsto F\circ\Delta_J$는 $\prod_{i\in I}A_i$에서 $\prod_{j\in J}A_j$로의 함수를 정의한다. 이를 성분함수의 표기를 빌려 $\operatorname{pr}\_J$로 적는다. 그럼 $K\subseteq J\subseteq I$에 대하여, 곱집합 $\prod\_{i\in I}A\_i$에서 부분곱 $\prod\_{j\in J}A\_j$로의 $J$번째 성분함수와, 곱집합 $\prod\_{j\in J}A\_j$에서 이 곱집합의 부분곱 $\prod\_{k\in K}A\_k$로의 $K$번째 성분함수

$$\prod_{i\in I}A_i\longrightarrow \prod_{j\in J}A_j\longrightarrow \prod_{k\in K}A_k$$

의 합성은 간단히 곱집합 $\prod\_{i\in I}A\_i$에서 이 곱집합의 부분곱 $\prod\_{k\in K}A\_k$로의 $K$번째 성분함수 $\operatorname{pr}_K$와 같다. $\Delta_K=\Delta_J\circ\Delta_K$이기 때문이다. 

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> Family $(A_i)\_{i\in I}$에 대하여, $A_i$들이 모두 공집합이 아니라 하자. 만일 $g:J\rightarrow\bigcup\_{i\in I} A_i$가 $g(i)\in A_i$를 만족한다면, $I$를 정의역으로 갖는 $g$의 extension $f$가 존재하여 $f(i)\in A_i$가 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $i\in I\setminus J$에 대하여, $A_i$가 공집합이 아니므로 $x_i\in A_i$를 하나씩 뽑을 수 있다. 따라서 $g$의 그래프 $G$를 $G\cup\left(\bigcup\_{i\in I\setminus J}\left\\{(i, x_i)\right\\}\right)$로 확장하면 된다.
</details>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $(A\_i)\_{i\in I}$가 $I\neq\emptyset$을 만족하는 family라 하자. 만일 $(J_k)\_{k\in K}$이 $I$의 분할이라면, $\prod\_{i\in I}A_i$에서 $\prod\_{k\in K}\left(\prod\_{j\in J_k}A_j\right)$로의 함수 $f\mapsto (\operatorname{pr}\_{J_k}(f))\_{k\in K}$ 또한 전단사함수이다.

</div>

<details class="proof" markdown="1">
<summary>증명 1</summary>

$(J_k)\_{k\in K}$이 분할이므로, $f_k:J_k\rightarrow \bigcup\_{i\in I} A_i$는 쌍마다 서로소인 정의역을 갖는 함수들의 family이고, 따라서 [§집합의 합, 명제 2](/ko/math/set_theory/sum_of_sets#pp2)를 적용하면 전단사함수를 얻는다.

</details>

위의 증명도 간결하지만, universal property를 이용하는 다음의 증명 또한 아름답다.

<details class="proof--alone" markdown="1">
<summary>증명 2</summary>

표기법 상의 깔끔함을 위해 일괄적으로

- Index set $K$에 대한 곱집합 $\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$의 $k$번째 성분함수

  $$\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{j\in J_k}A_j$$

  을 $\operatorname{pr}_k$,
- Index set $J_k$에 대한 곱집합 $\prod_{j\in J_k}A_j$의 $j$번째 성분함수

  $$\prod_{j\in J_k}A_j\rightarrow A_j$$

  도 $\operatorname{pr}_j$,
- Index set $I$에 대한 곱집합 $\prod_{i\in I}A_i$의 $i$번째 성분함수

  $$\prod_{i\in I}A_i\rightarrow A_i$$

  도 $\operatorname{pr}_i$

으로 표기하자. 글자로 보았을 때는 약간의 혼동이 있을 수 있지만, diagram 상에서는 source와 target이 모두 명시되므로 혼동의 여지가 없다.

$(J\_k)\_{k\in K}$는 $I$의 분할이므로, 각각의 $i\in I$마다 유일한 $k\in K$가 존재하여 $i\in J_k$이다. 이제 함수 $\operatorname{pr}_{ik}$를 다음의 합성

$$\operatorname{pr}_{ik}:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\overset{\operatorname{pr}_k}{\longrightarrow}\prod_{j\in J_k}A_j\overset{\operatorname{pr}_i}{\longrightarrow}A_i$$

으로 정의하자. 그럼 곱집합 $\prod_{i\in I}A_i$의 universal property로부터, 다음의 diagram을 commute하도록 하는 $\phi:\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)\rightarrow\prod_{i\in I}A_i$가 존재함을 안다.

![partial_product_pf_1](/assets/images/Set_theory/Product_of_sets-4.png){:width="378.6px" class="invert" .align-center}

비슷하게 index set $K$에 대한 곱집합 $\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$의 universal property로부터, 다음의 diagram을 commute하게 하는 $\psi:\prod_{i\in I}A_i\rightarrow\prod_{k\in K}\left(\prod_{j\in J_k}A_j\right)$가 존재함을 안다.

![partial_product_pf_2](/assets/images/Set_theory/Product_of_sets-5.png){:width="502.8px" class="invert" .align-center}

그럼 $\phi\circ\psi$와 $\psi\circ\phi$가 각각 항등함수이고, 따라서 이들이 원하는 전단사함수가 된다. 

예를 들어 $\phi\circ\psi$가 $\prod_{i\in I}A_i$에서 자기자신으로의 항등함수임을 보이자. 이를 위해서는 모든 $i\in I$에 대하여 다음의 diagram이 commute함을 보이면 충분하다.

![partial_product_pf_3](/assets/images/Set_theory/Product_of_sets-6.png){:width="184.35px" class="invert" .align-center}

곱집합의 universal property는 위의 diagram을 commute하게 하는 <em_ko>유일한</em_ko> 함수 $\prod_{i\in I}A_i\rightarrow \prod_{i\in I}A_i$가 존재한다는 것을 의미하는데, 당연하게 $\prod_{i\in I}A_i$에서 자기자신으로의 항등함수 또한 위의 diagram을 commute하게 하고 따라서 유일성에 의해 이 함수는 $\phi\circ\psi$와 같아야 하기 때문이다. 

이제

$${\operatorname{pr}_i}\circ(\phi\circ\psi)=({\operatorname{pr}_i}\circ\phi)\circ\psi={\operatorname{pr}_{ik}}\circ\psi={\operatorname{pr}_i}\circ({\operatorname{pr}_k}\circ\psi)={\operatorname{pr}_j}\circ{\operatorname{pr}_{J_k}}=\operatorname{pr}_j$$

에서 원하는 결론을 얻는다. (마지막 등식은 $\operatorname{pr}_j$를 $\\{j\\}\subseteq I$로의 성분함수로 보았다.) 이 식은 복잡해보이지만, 그냥 다음의 diagram이 commute한다는 것을 식으로 쓴 것에 불과하다. 

![partial_product_pf_4](/assets/images/Set_theory/Product_of_sets-7.png){:width="349.05px" class="invert" .align-center}

</details> 

$(A_i)\_{i\in I}$, $(B_i)\_{i\in I}$가 같은 index를 갖는 family이고, <phrase>$A_i$에서 $B_i$로의 함수 $g_i$들의 family</phrase> $(g_i)\_{i\in I}$가 주어졌다 하자. $u_f$를 $I$에서 $\bigcup_{i\in I}B_i$로의 함수 $i\mapsto g_i(f(i))$라 하면 $u_f(i)\in B_i$이고, 따라서 $u_f\in\prod_{i\in I}B_i$이다. 

<div class="definition" markdown="1">

<ins id="df9">**정의 9**</ins> 위에서 정의한 함수 $f\mapsto u_f$를 $(g_i)$들의 *곱<sub>product</sub>*이라 하고, $\prod_{i\in I}g_i$으로 적는다.

</div>

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> $(A_i)\_{i\in I}$, $(B_i)\_{i\in I}$, $(C_i)\_{i\in I}$가 세 family라 하고, $(f_i)\_{i\in I}$, $(g_i)\_{i\in I}$가 각각 $A_i$에서 $B_i$, $B_i$에서 $C_i$로의 함수들의 family라 하자. 그럼

$$\prod_{i\in I} (g_i\circ f_i)=\left(\prod_{i\in I} g_i\right)\circ\left(\prod_{i\in I}f_i\right)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음 두 개의 commutative diagram 이외에는 특별히 설명할 것이 없다.

![composition_of_product_functions](/assets/images/Set_theory/Product_of_sets-8.png){:width="287.1px" class="invert" .align-center}

그리고

![composition_of_product_fuctions_2](/assets/images/Set_theory/Product_of_sets-9.png){:width="335.4px" class="invert" .align-center}

</details>

$\operatorname{id}\_{A\_i}$들의 곱이 $\operatorname{id}\_{\prod A\_i}$라는 것은 자명하므로, 위의 명제에 의해 단사함수들의 곱은 단사함수이고 전사함수들의 곱은 전사함수라는 것 또한 명확하다. 


## 분배법칙

한편, 둘 이상의 연산이 정의되어 있다면 분배법칙이 성립하는지가 중요한 관심사다.

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> $((A\_{k,i})\_{i\in J\_k})\_{k\in K}$가 family들의 family라 하자. 추가로 $K\neq\emptyset$이고, $J_k\neq\emptyset$가 모든 $k\in K$에 대해 성립한다고 하자. 그럼 $I=\prod\_{k\in K} J_k\neq\emptyset$에 대하여,

$$\bigcup_{k\in K}\left(\bigcap_{i\in J_k}A_{k,i}\right)=\bigcap_{f\in I}\left(\bigcup_{k\in K}A_{k,f(k)}\right),\quad\bigcap_{k\in K}\left(\bigcup_{i\in J}A_{k,i}\right)=\bigcup_{f\in I}\left(\bigcap_{k\in K}A_{k,f(k)}\right)$$

이 성립한다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $x\in \bigcup\_{k\in K}\left(\bigcap\_{i\in J_k}A\_{k,i}\right)$라 하자. 우리는 $x\in \bigcap\_{f\in I}\left(\bigcup\_{k\in K}A\_{k,f(k)}\right)$, 즉 모든 $f\in I$에 대하여 $x\in \bigcup\_{k\in K}A\_{k,f(k)}$임을 보여야 한다. 어떤 $k\in K$에 대하여 $x\in \bigcap\_{i\in J_k}A\_{k,i}$이므로, $x\in A\_{k,f(k)}$이다. 따라서 $x\in \bigcup\_{k\in K}A\_{k,f(k)}$가 모든 $f$에 대하여 성립하고, 따라서 포함관계가 성립한다.  

반대쪽 포함관계를 보이기 위해 대우명제를 사용하자. 즉 $x\not\in \bigcup\_{k\in K}\left(\bigcap\_{i\in J_k}A\_{k,i}\right)$라 하자. 그럼 모든 $k\in K$에 대하여, $x\not\in \bigcap\_{i\in J_k}A\_{k,i}$이다. 따라서 어떤 $i$가 존재하여, 모든 $k$에 대해 $x\not\in A\_{k,i}$이다. 이제 $f(k)$가 그러한 $i$가 되도록 하는 $f\in I$를 잡으면, $x\not\in\bigcup\_{k\in K}A\_{k,f(k)}$이고 , 따라서 우변에 속하지 않는다. 두 번째 식도 이와 비슷하게 보이면 된다.
</details>

Product와 union, 그리고 product와 intersection 사이에도 다음과 같이 분배법칙이 성립하며, 이에 대한 증명은 위와 거의 같으므로 생략한다.

<div class="proposition" markdown="1">
<ins id="pp12">**명제 12**</ins> $((A\_{k,i})\_{i\in J\_k})\_{k\in K}$가 family들의 family이고, $I$를 위의 명제와 동일하게 정의하자. 그럼 

$$\prod_{k\in K}\left(\bigcup_{i\in J_k}A_{k,i}\right)=\bigcup_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right),\quad\prod_{k\in K}\left(\bigcap_{i\in J}A_{k,i}\right)=\bigcap_{f\in I}\left(\prod_{k\in K}A_{k,f(k)}\right)$$

가 성립한다.
</div>

---
**참고문헌**

**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  
**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
