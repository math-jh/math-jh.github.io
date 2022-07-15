---
title: "몫위상"
excerpt: "몫공간과 몫사상"

categories: [Math / Topology]
permalink: /ko/math/topology/quotient_topology
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-26
last_modified_at: 2022-06-13
weight: 11
    
---

이제 우리는 마지막으로 몫위상에 대해 살펴본다.

## 몫위상의 정의

위상공간은 우리가 그 동안 다루어왔던 대수적인 공간들보다는 시각화하기가 좋은데, 이에 대한 단적인 예시가 몫위상이다. 기본적으로 몫집합 위에 새로운 위상을 정의한다는 아이디어는 똑같지만, 이 경우 특히 두 점을 equivalence relation을 통해 <em_ko>같게 본다</em_ko>는 것은, 두 점을 하나의 점으로 <em_ko>합친다</em_ko>는 기하학적인 의미를 갖게 된다. 예를 들어, 다음의 그림과 같이, 직사각형에서 마주보는 점들을 각각 같게 본다면, 우리는 원기둥을 얻을 것이다.

![quotient_topology](/assets/images/Topology/Constructing_topologies-2.png){:width="360px"  class="invert" .align-center}

위상공간 $X$가 주어졌다고 하자. 우리는 equivalence relation $R$을 통해 서로 다른 두 개 이상의 점들을 하나의 점으로 취급하려 하므로, 이 여러 개의 점을 하나의 점, 즉 equivalence class로 묶을 것이고, 그를 위해서는 quotient set $X/R$을 생각해야 한다. ([집합론, §동치관계, 정의 6](/ko/math/set_theory/equivalence_relations#df6)) 그러므로, *quotient topology*라는 것을 정의한다는 것은 이 quotient set $X/R$ 위에 어떤 위상구조를 새롭게 정의하는 것이다. 

우리가 갖고 있는 정보는 $X$에서의 위상과, canonical surjection $p:X\rightarrow X/R$이다. 따라서 $X/R$에 열린집합이라는 정보를 주기 위해서는 

> $X/R$의 부분집합 $V$가 열린집합이라는 것은, $p^{-1}(V)$가 $X$에서 열린집합인 것이다.

이렇게 정의하는 방법이 가장 자연스럽다. 물론 우리는 이렇게 정의되는 $X/R$의 열린집합들의 모임이 위상의 성질을 만족하는지를 따져봐야 한다.  

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 위와 같이 정의된 열린집합들의 모임은 집합 $X/R$ 위의 위상의 조건을 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

자명하게 $p^{-1}(\emptyset)=\emptyset$이고 $p^{-1}(X/R)=X$이므로 $\emptyset$, $X/R$은 모두 $\mathcal{T}$의 원소이다.

위상이 만족해야 할 나머지 두 개의 성질들은 다음의 두 식

$$\begin{aligned}
p^{-1}\left(\bigcup_{\alpha\in I}U_\alpha\right)&=\bigcup_{\alpha\in I}p^{-1}\left(U_\alpha\right)\\
p^{-1}\left(\bigcap_{i=1}^n U_i\right)&=\bigcap_{i=1}^np^{-1}\left(U_i\right).
\end{aligned}$$

에서 자명하다.

</details>

한편, $X/R$ 위에 위상을 정의하기 위해서는 $X/R$의 어떠한 집합들이 닫힌집합인지를 명시하는 것으로도 충분한데, 어렵지 않게 

> $X/R$의 부분집합 $C$가 닫힌집합이라는 것은, $p^{-1}(C)$가 $X$에서 닫힌집합인 것이다.

으로 정의하였을 때, 이렇게 정의된 위상이 위에서 정의한 위상과 정확하게 동일하다는 것을 확인할 수 있다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $X$가 위상공간이고, $R$이 집합 $X$ 위에 정의된 equivalence relation이라 하자. 그럼 canonical map $p:X\rightarrow X/R$에 대하여, 위와 같이 정의된 위상 $\mathcal{T}$를 $R$에 의해 정의된 *quotient topology<sub>몫위상</sub>*이라 하고, quotient topology가 장착된 위상공간 $X/R$을 *quotient space<sub>몫공간</sub>*이라 부른다.

</div>

## 몫사상

더 일반적으로, 두 위상공간들 간의 연속인 surjection $p:X\rightarrow Y$를 생각하자. 우리는 $p$가 $X$ 위의 equivalence relation $R$을 정의한다는 것을 알고 있으며 ([집합론, §동치관계, 명제 4](/ko/math/set_theory/equivalence_relations#pp4)), $p$의 canonical decomposition을 생각하면 우리는 [정의 1](#df1)에 의해 정의된 위상공간 $X/R$과, 주어진 위상공간 $Y$ 사이의 bijection $h$를 얻는다.

![quotient_topology_induced_by_surjection](/assets/images/Topology/Constructing_topologies-3.png){:width="140px"  class="invert" .align-center}

이러한 상황에서, 우리가 바랄 수 있는 가장 좋은 상황은 이렇게 유도된 bijection $h$가 실은 homeomorphism인 것이다. 우선 $Y$의 임의의 열린집합 $V$가 주어졌다 하자. 그럼 $p$가 연속이므로, $p^{-1}(V)$는 열린집합이고, 

$$p^{-1}(V)=(h\circ\pi)^{-1}(V)=\pi^{-1}(h^{-1}(V))$$

이 성립하므로 $h$는 연속이다. $h$가 homeomorphism이 되기 위해서는 그 역함수 $h^{-1}$ 또한 연속이어야 하는데, 이 부분에 문제가 있다. 우선 다음의 보조정리를 보이자.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위의 diagram에서, $X/R$의 임의의 부분집합 $U$에 대하여 다음의 식

$$p(\pi^{-1}(U))=h(U)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $y\in h(U)$라 하자. 그럼 $h$에 의해 $y$에 대응되는 $X/R$의 원소가 존재하므로, 이 원소의 representative를 $x$라 하고, $[x]\in U$에 대하여 $h([x])=y$라 할 수 있다. $\pi(x)=[x]$이므로, $x\in\pi^{-1}(U)$이고 

$$p(x)=(h\circ\pi)(x)=h(\pi(x))=h([x])=y$$

가 성립한다. 즉, $y\in p(\pi^{-1}(U))$이다. 

거꾸로 $y\in p(\pi^{-1}(U))$라 하자. 그럼 $p(x)=y$이도록 하는 $x\in\pi^{-1}(U))$가 존재한다. 이제 $\pi(x)\in U$이고, 

$$h(\pi(x))=p(x)=y$$

이므로 $y\in h(U)$이다. 

</details>

위상공간 $X/R$의 열린집합 $U$가 주어졌다 하자. $h^{-1}$이 연속이기 위해서는 그 역함수 $h=(h^{-1})^{-1}$에 의한 $U$의 image $h(U)$ 또한 열린집합이어야 한다. 집합 $U$가 $X/R$에서 열린집합이라는 것은 정의에 의하여 $\pi^{-1}(U)$가 $X$에서 열린집합이라는 것과 동치이지만, $p$가 연속함수라 하더라도

$$h(U)=p(\pi^{-1}(U))$$

가 열린집합일 필요는 없으므로, $h^{-1}$이 연속이라는 것을 확신할 수 없다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 두 위상공간 $X,Y$가 주어졌다 하자.

- 함수 $f:X\rightarrow Y$가 *open map<sub>열린사상</sub>*이라는 것은 $f$가 열린집합을 열린집합으로 보내는 것이다.
- 함수 $f:X\rightarrow Y$가 *closed map<sub>닫힌사상</sub>*이라는 것은 $f$가 닫힌집합을 닫힌집합으로 보내는 것이다.

</div>

앞선 상황에서, 만일 $p$가 open map이었다면 $p$는 열린집합 $\pi^{-1}(U)$들을 모두 열린집합으로 보냈을 것이고, 따라서 $h^{-1}$이 연속함수가 되어 $X/R$과 $Y$가 homeomorphic했을 것이다. 비슷하게, $h^{-1}$의 연속성을 닫힌집합으로 표현하고, $X/R$에 정의된 위상 또한 닫힌집합으로 표현한다면, $p$가 closed map임을 가정하고 $X/R$과 $Y$가 homeomorphic하다는 것을 보일 수 있다. 그러나 일반적으로 open map과 closed map은 연속함수일 필요는 없으며, 이들 두 개념 사이에도 별다른 관련이 없다는 것을 기억해둘 필요가 있다.

하지만 $p$가 open map이라는 것은 과도하게 강한 가정이다. $h(U)=p(\pi^{-1}(U))$가 열린집합이기 위해서는, $h$가 <em_ko>모든</em_ko> 열린집합을 열린집합으로 보낼 필요 없이, $\pi^{-1}(U)$ 꼴들의 열린집합만 열린집합으로 보내주면 된다. 우리는 이러한 꼴의 집합을 *saturated subset*으로 부르기로 했었으니 ([집합론, §동치관계, 정의 13](/ko/math/set_theory/equivalence_relations#df13)), 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 두 위상공간 $X$, $Y$에 대하여, $p:X\rightarrow Y$가 *quotient map<sub>몫사상</sub>*이라는 것은

- $p$가 연속인 surjection이고,
- $p$에 의해 정의된 equivalence relation $R$에 대하여, $R$에 대해 saturated인 $X$의 열린 부분집합이 모두 $Y$의 열린집합으로 옮겨지는 것이다.

</div>


이렇게 새로운 공간을 정의한 후에는 언제나처럼 우리가 원래 정의한 개념들과의 관계를 살펴봐야 한다. 그런데, quotient space은 일반적으로 subspace도 잘 보존하지 않고, product도 잘 보존하지 않는다. 즉, quotient map을 subspace로 제한했을 때 이 함수가 quotient map이 될 필요가 없고, quotient map의 product가 quotient map이 될 필요 또한 마찬가지로 없다. 

어떤 quotient map $p:X\rightarrow Y$에 대하여, $A$가 집합 $X$의 subspace라 하자. $p$에 의해 정의된 equivalence relation을 $R$이라 한다면, relation $R$을 $A\times A$ 위로 제한한 relation, 즉 $R\cap (A\times A)$ 또한 $A$ 위에서의 equivalence relation이고, 따라서 우리는 $A$ 위에서 이 equivalence relation을 이용해 quotient space를 만들어 볼 수 있다.  

우선 $f$를 $A$로 제한한 함수 $p\|\_A$를 생각하면, $p\|\_A:A\rightarrow p(A)$는 surjection이다. 또, $p\|\_A$는 연속함수를 제한하여 얻어졌으므로 연속이다. 그러나 $p\|\_A$가 saturated인 열린집합을 열린집합으로 보내는지는 확실하지 않다. 이는 $A$에서 $R\cap (A\times A)$에 대해 saturated인 집합이 $X$에서는 saturated가 아닐 수도 있기 때문이다. 즉, $R\cap(A\times A)$에서 $x\in A$와 equivalent한 원소들은 모두 $A$의 원소들이고, 이 때 $x$와 equivalent한 원소들 중 $A$ 바깥에 있는 원소들이 빠져있으므로 어떤 집합 $U\subset A$가 $A$에서 saturated라 하더라도, $X$에서는 saturated가 아닐 수 있으므로, $p\|\_A(U)$가 열린집합일 필요가 없다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 예를 들어, 집합 $X=\\{1,2,3\\}$ 위에 위상을 $\mathcal{T}=\\{\emptyset, \\{1,2\\},\\{3\\},X\\}$를 주자. 이제 집합 $Y=\\{0,1\\}$에 대해, $f:X\rightarrow Y$를 다음의 식

$$f(x)=\left\{\begin{array}{l l}1&x=1,3\\0&x=2\end{array}\right.$$

으로 정의하자. 그럼 $Y$ 위에서 정의되는 quotient topology는 trivial topology이다. $\\{0\\}$과 $\\{1\\}$의 $f$에 대한 preimage가 모두 열린집합이 아니기 때문이다. 이제 $A=\\{1,2\\}$에 subspace 구조를 주면, $A$는 discrete topology이다. 이 집합 위에 $R$을 제한하여 만들어진 equivalence relation은 identity relation이다. 따라서 $\\{1\\}$과 $\\{2\\}$는 모두 saturated인 열린집합이지만 $f(\\{1\\})=\\{1\\}$, $f(\\{2\\})=\\{0\\}$은 모두 $p(A)=Y$에서 열린집합이 아니다.

</div>

만일 $A$가 saturated인 부분집합이었다면, 이 문제를 해결할 수도 있을 것이다. 그러나 이 경우에도 $A$가 닫힌집합도, 열린집합도 아니라면 또 다시 문제가 생긴다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 자연수 집합 $\mathbb{N}$ 위에 cofinite topology를 주고, $\operatorname{id}:\mathbb{N}\rightarrow\mathbb{N}$을 생각하자. 그럼 $\mathbb{N}$의 $\operatorname{id}$에 의한 quotient space는 자기 자신과 같다. 이 경우, equivalence relation은 identity relation이 되므로, $\mathbb{N}$의 임의의 부분집합은 모두 saturated인 부분집합이다.  
이제 $\mathbb{N}$의 부분집합으로, 짝수들의 부분집합 $2\mathbb{N}$을 생각하자. 이 집합은 saturated이지만 열린집합도, 닫힌집합도 아니다. 이제 홀수 전체의 집합 $2\mathbb{N}+1$는 $2\mathbb{N}$의 subspace topology에서 (공집합이므로) saturated인 열린집합이지만, $2\mathbb{N}+1$은 $\mathbb{N}$ 위에서 열린집합이 아니다.

</div>

따라서 우리는 $A$가 saturated인 열린 (혹은 닫힌) 부분집합 정도는 되어있어야 함을 추측할 수 있고, 다행히 이 경우에는 $A$의 subspace가 quotient map을 잘 정의한다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $p:X\rightarrow Y$가 위상공간 $X$와 $Y$ 간의 quotient map이라 하고, $A$가 $p$에 대응되는 equivalence relation에 대해 saturated되었다고 하자. 

1. 만일 $A$가 $X$에서 열린집합이거나, 닫힌집합이라면 $p\|\_A$는 quotient map이다. 
2. 만일 $p$가 open map이거나 closed map이라면 $p\|\_A$는 quotient map이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저, $A$는 saturated인 부분집합이므로 $p^{-1}(p(A))=A$이고, 따라서 $U\subset p(A)$에 대하여 $p^{-1}(U)\subset p^{-1}(p(A))=A$이다. 그러므로 $U\subset p(A)$인 집합 $U$에 대해서는

$$(p|_A)^{-1}(U)=p^{-1}(U)$$

가 성립한다.  

또, 임의의 부분집합 $V\subset X$에 대하여 $p(V\cap A)=p(V)\cap p(A)$가 성립한다. $p(V\cap A)\subset p(V)\cap p(A)$는 일반적으로 성립하며, $y\in p(V)\cap p(A)$라면 $p^{-1}(\left\\{y\right\\})\subset p^{-1}(p(A))=A$이고, 따라서 $p(x)=y$를 만족하는 모든 $x\in X$는 $A$의 원소이므로, 특히 $y\in p(V)$에서 얻어지는 $p(v)=y$를 만족하는 $v\in V$도 $A$의 원소여야 하므로 $v\in A\cap V$이고 $p(v)=y\in p(V\cap A)$이다.

이제 주어진 명제들을 보이자. 이를 위해서, 우리는 $A$에서의 saturated인 열린집합을 하나 가져온 다음, 이 집합의 image가 $p(A)$ 상에서 열린집합이 됨을 보여야 한다. $A$에서의 saturated인 부분집합의 형태는 항상 $p^{-1}(V)$의 형태이므로, 우리는 $(p\|\_A)^{-1}(V)$이 $A$에서 열린집합이라면 $V$가 $p(A)$에서 열린집합임만 보이면 된다. 만일 $A$가 열린집합이고 $(p\|\_A)^{-1}(V)$가 $A$에서 열린집합이라면, 이 집합은 $X$에서도 열린집합이다. 한편, $(p\|\_A)^{-1}(V)=p^{-1}(V)$이므로, 다음의 집합

$$V=(p|_A)((p|_A)^{-1}(V))=p(p^{-1}(V))$$

는 열린집합이다. 이와 비슷하게, $p$가 open map이고 $(p\|\_A)^{-1}(V)$가 $A$에서 열린집합이라 하자. 그럼 다시 $(p\|\_A)^{-1}(V)=p^{-1}(V)$이므로, $X$의 어떤 부분집합이 존재하여 $p^{-1}(V)=U\cap A$라 할 수 있다. 그럼 다음의 식

$$V=p(p^{-1}(V))=p(U\cap A)=p(U)\cap p(A)$$

에서, $p$가 open이므로 $p(U)$는 열린집합이고, 따라서 $p(A)$의 부분공간 상에서 $V$는 열린집합이다. 지금까지의 증명에서 열린집합/open map들을 모두 닫힌집합/closed map들로 바꾸면 나머지도 증명된다.

</details>

우리는 연속함수가 위상공간들을 다룰 때 적합한 함수들인 것을 알고 있으므로, 어떤 함수 $X/R\rightarrow Z$가 연속인지 아닌지를 판별하는 것은 특히 중요하다. 우선 다음의 diagram

![continuity_and_quotient_topology](/assets/images/Topology/Constructing_topologies-4.png){:width="140px"  class="invert" .align-center}

에서, $p$가 quotient map이고 $Y$가 $p$에 의해 정의되는 quotient space, 그리고 $g:X\rightarrow Z$가 위상공간 $X$와 $Z$ 간의 함수라 하자. 이 때, $g=f\circ p$를 만족하는 함수 $f$가 존재하는 것은 $g$가 $p^{-1}(\left\\{y\right\\})$ 상에서 상수함수인 것과 동치이다. ([집합론, §함수 (2), 명제 4](/ko/math/set_theory/functions_2#pp4)) 이 조건 하에서 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> $g:X\rightarrow Z$가 위상공간들 간의 연속인 surjection이라 하고, $R$이 $g$에 의해 정의된 equivalence relation이라 하자. 그럼 $g$는 함수 $f:X/R\rightarrow Z$를 정의하며, 이 함수가 연속인 것은 $g$가 연속인 것과 동치이다. 특히, $f$가 quotient map인 것은 $g$가 quotient map인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞서 적은 것과 같이, [집합론, §함수 (2), 명제 4](/ko/math/set_theory/functions_2#pp4)에 의해 $f$가 잘 정의된다. 한편, 만일 $f$가 연속이라면, 두 연속함수들의 합성 $f\circ p=g$가 연속임은 자명하다. 이제 $g$가 연속이라 가정하자. 그럼 임의의 $V\subset Z$에 대하여, $V$가 열린집합이라면 $g^{-1}(V)$ 또한 열린집합이다. 그런데 

$$g^{-1}(V)=(f\circ p)^{-1}(V)=p^{-1}(f^{-1}(V))$$

이고, $p$가 quotient map이므로 $f^{-1}(V)$는 열린집합이다. 즉, $f$가 연속이다.

만일 $f$가 quotient map이라면, $f\circ p=g$는 quotient map들의 합성이므로 quotient map임이 자명하다. 반대로 만일 $g$가 quotient map이라면, $X$의 saturated인 열린집합 $f^{-1}(V)$에 대하여 $V$가 $Z$에서 열린집합임을 보여야 한다. 그런데 $p^{-1}(f^{-1}(V))$는 $p$의 연속성에 의해 열려있고, 이 집합은 곧 $g^{-1}(V)$와 같으므로 $g^{-1}(V)$는 열린집합이다. 다시 $g$는 quotient map이므로, $V$는 $Z$에서 열린집합이다.

</details>



---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

[^1]: $f:X\rightarrow Y$가 열린사상이라는 것은 $f$가 $X$의 열린집합을 모두 $Y$의 열린집합으로 옮긴다는 것이고, 닫힌사상이라는 것은 닫힌집합을 모두 닫힌집합으로 옮긴다는 것이다.
