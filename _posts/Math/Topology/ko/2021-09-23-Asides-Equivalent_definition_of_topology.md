---

title: "위상공간의 다른 정의들<sup>†</sup>"
excerpt: "Closure axiom, Filter, "

categories: [Math / Topology]
permalink: /ko/math/topology/equivalent_definition_of_topology
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-04-13
last_modified_at: 2022-05-22
weight: 5
    
---

우리는 $X$의 어떤 부분집합들이 열린집합인지를 정해줌으로써 집합 $X$ 위에 위상구조를 정의했다. 하지만 이것이 위상구조를 정의하는 유일한 방법은 아니고, 실제로 우리는 다른 방식으로 위상구조를 정의하는 방법을 살펴보기도 하였다. ([§열린집합과 닫힌집합, 명제 8](/ko/math/topology/basic_definition_1#pp8)) 이번 글에서 우리는 위상구조를 정의하는 또 다른 방법들을 소개한다.


## Closure axiom

<div class="definition" markdown="1">

<ins id="df1">**정의 1 (Kuratowski closure axiom)**</ins> 임의의 집합 $X$에 대하여, 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 다음의 조건들을 모두 만족한다 하자.

- $A\subset\operatorname{cl}(A)$
- $\operatorname{cl}(\operatorname{cl}(A))=\operatorname{cl}(A)$
- $\operatorname{cl}(A\cup B)=\operatorname{cl}(A)\cup\operatorname{cl}(B)$
- $\operatorname{cl}(\emptyset)=\emptyset$

이 조건들을 만족하는 함수를 *closure operator*라 부른다. ([집합론, §필터와 아이디얼, 갈루아 대응, 정의 8](/ko/math/set_theory/order_relations_3#df8))

</div>

세 번째 조건으로부터, 만일 $A\subset B$라면

$$\operatorname{cl}(A)\subset\operatorname{cl}(A)\cup\operatorname{cl}(B)=\operatorname{cl}(A\cup B)=\operatorname{cl}(B)$$

임을 알 수 있다. 

임의의 위상공간 $X$에 대하여, $X$의 임의의 부분집합 $A$를 $A$의 closure로 보내는 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 위의 조건을 만족한다는 것은 자명하다. 

거꾸로 임의의 집합 $X$ 위에 위의 조건을 만족하는 closure operator $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$이 주어졌다 하자. 이제 $\mathcal{P}(X)$의 원소들 중 $\operatorname{cl}(C)=C$를 만족하는 집합들의 모임을 $\mathcal{C}$로 적자. 그러면

- $\operatorname{cl}(\emptyset)=\emptyset$이므로, $\emptyset\in\mathcal{C}$이다. 한편 $X\subset\operatorname{cl}(X)$이므로 $\operatorname{cl}(X)=X$이고 따라서 $X\in\mathcal{C}$이다.
- 임의의 $A,B\in\mathcal{C}$에 대하여, $A\cup B=\operatorname{cl}(A)\cup\operatorname{cl}(B)=\operatorname{cl}(A\cup B)$가 성립하므로 $A\cup B\in\mathcal{C}$가 성립한다. 
- 임의의 index set $I$와 $A_i\in\mathcal{C}$들에 대하여, $\bigcap A_i\subset\operatorname{cl}(\bigcap A_i)$이고, 또 $\bigcap A_i\subset A_i$으로부터 

  $$\operatorname{cl}(\bigcap A_i)\subset\operatorname{cl}(A_i)=A_i$$

  가 성립하므로 $\operatorname{cl}(\bigcap A_i)\subset\bigcap A_i$ 또한 성립한다.

이로부터 다음의 정리가 얻어진다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> [정의 1](#df1)의 조건을 모두 만족하는 함수 $\operatorname{cl}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 주어졌다 하자. $\mathcal{C}$를 $\operatorname{cl}(C)=C$를 만족하는 모든 $C$들의 모임으로 정의하면, $\mathcal{C}$는 [§열린집합과 닫힌집합, 명제 8](/ko/math/topology/basic_definition_1#pp8)의 조건을 모두 만족하며 따라서 유일한 위상구조를 정의한다.

</div>

물론 집합의 interior를 이용하여도 어렵지 않게 위상구조를 하나 정의할 수 있다. 이 경우, interior operator $\operatorname{int}$가 만족해야 할 공리들은 다음과 같다.

<div class="misc" markdown="1">

**Interior axiom.** 임의의 집합 $X$에 대하여, 함수 $\operatorname{int}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$가 다음의 조건들을 만족한다 하자.

- $\operatorname{int}(A)\subset A$
- $\operatorname{int}(\operatorname{int}(A))=\operatorname{int}(A)$
- $\operatorname{int}(A\cap B)=\operatorname{int}(A)\cap\operatorname{int}(B)$
- $\operatorname{int}(X)=X$

이 조건들을 만족하는 함수를 *interior operator*라 부른다.

</div>

## Neighborhood filter

이 절에서 점 $x$의 근방은 항상 열린근방이 아닌, 일반적인 근방을 뜻한다. ([§열린집합과 닫힌집합, 정의5](/ko/math/topology/basic_definition_1#df5))

위상공간 $X$가 주어졌다 하고, 공집합이 아닌 부분집합 $A$를 생각하자. $A$의 근방들의 모임을 $\mathcal{N}(A)$라 하면 $\mathcal{N}(A)$는 ordered set $\mathcal{P}(X)$의 filter가 된다. 

1. (Left directed) 임의의 $N_1, N_2\in\mathcal{N}(A)$가 주어졌다 하자. 그럼 $A\subset U_i\subset N_i$를 만족하는 $A$의 열린근방 $U_i$들이 존재한다. 그런데 $A\subset U_1\cap U_2\subset N_1\cap N_2$이고 $U_1\cap U_2$는 $A$의 열린근방이므로, $N_1\cap N_2$도 $A$의 근방이다.
2. (Upper set) 만일 $N\in\mathcal{N}(A)$라면, $A$의 적당한 열린근방 $U$가 존재하여 $A\subset U\subset N$이다. 그런데 $N\subset N'$를 만족하는 임의의 $N'$에 대하여 $U$는 $N'$의 부분집합이기도 하므로 $N'\in\mathcal{N}(A)$가 성립한다.

특별히 $A=\\{x\\}$인 경우, $\mathcal{N}(A)$ 대신 간단하게 $\mathcal{N}(x)$로 표기하기로 한다.

거꾸로 임의의 $x\in X$마다 filter $\mathcal{F}_x$가 정의되었다 하자. 그럼 이들 각각을 $x$에서의 neighborhood filter로 갖는 위상구조 $\mathcal{T}$가 존재하는지를 생각할 수 있다. 이에 답하기 위해서는 power set $\mathcal{P}(X)$ 위에서 정의된 filter, 그 중에서도 $\emptyset$을 포함하지 않는 *proper* filter를 조금 더 자세히 살펴볼 필요가 있다.

Filter $\mathcal{F}$가 ordered set $\mathcal{P}(X)$의 proper filter임을 일일히 언급하는 것은 성가신 일이므로, 앞으로 이를 간단히 <phrase>$X$ 위에서 정의된 filter $\mathcal{F}$</phrase>으로 표현하기로 한다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $X$ 위에 정의된 두 filter $\mathcal{F},\mathcal{F}$를 생각하자. 만일 $\mathcal{F}\subset\mathcal{F}'$라면 $\mathcal{F}'$가 $\mathcal{F}$보다 *강한* filter, 혹은 $\mathcal{F}$가 $\mathcal{F}'$보다 *약한* filter라 한다. 

</div>

$X$의 부분집합들의 모임 $\mathcal{S}\subset\mathcal{P}(X)$를 생각하자. 만일 $X$의 적당한 filter $\mathcal{F}$가 존재하여 $\mathcal{S}\subset\mathcal{F}$라면, $\mathcal{F}$는 left directed set이므로 $\mathcal{S}$의 유한한 교집합 또한 포함해야 한다. 만일 $\mathcal{S}$의 원소들 중 유한개를 택하여 이들의 교집합이 공집합이 되도록 할 수 있다면, $\mathcal{F}$는 $\emptyset$을 포함하게 되어 $X$ 위에서의 (proper) filter가 될 수 없다. 따라서, $\mathcal{F}$가 filter가 되기 위해서는 반드시 $\mathcal{S}$가 finite intersection property를 만족해야 한다.  
거꾸로 finite intersection property를 만족하는 부분집합들의 모임 $\mathcal{S}$가 주어졌다 하면, $\mathcal{S}$의 원소들의 유한한 교집합들의 모임 $\mathcal{S}'$은 $\emptyset$을 포함하지 않는다. 이제 $\mathcal{F}={}\uparrow\mathcal{S}'$를 생각하면, $\mathcal{F}$가 $X$ 위에서 정의된 filter가 된다는 것을 쉽게 확인할 수 있다. 

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 위에서 정의한 filter $\mathcal{F}$를 $\mathcal{S}$에 의해 generate되었다고 하고, 이 때 $\mathcal{S}$를 $\mathcal{F}$의 *subbasis*라 한다.

</div>

일반적으로 $\mathcal{S}\subset\mathcal{P}(X)$에 대해, $\uparrow\mathcal{S}$는 filter가 될 필요가 없으며, 이는 $\uparrow\mathcal{S}$가 left directed가 아니기 때문이다. 하지만 $\uparrow\mathcal{S}$는 정의에 의해 upper set이므로, 만일 $\mathcal{S}$가 left directed라면 $\uparrow\mathcal{S}$는 $X$ 위에서의 filter가 된다.

이상에서 다음의 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> $\mathcal{P}(X)$의 임의의 부분집합 $\mathcal{S}$가 주어졌다 하자. $\uparrow\mathcal{S}$가 $X$ 위에서의 filter가 되는 것은 다음의 두 조건

- $\mathcal{B}$는 유한한 부분집합에 대해 닫혀있다.
- $\mathcal{B}$는 공집합이 아니며, $\emptyset\not\in\mathcal{B}$이다.

과 동치이다.

</div>

위의 조건을 만족하는 $\mathcal{S}$를 filter $\mathcal{F}={}\uparrow\mathcal{S}$의 *basis*라 부른다. 

한편, 집합 $X$의 임의의 부분집합 $A$에 대하여, $X$ 위에서 정의된 filter $\mathcal{F}$는 일반적으로 $A$ 위에서의 filter로 restricted 되지 않는다. 이는 만일 $\mathcal{F}$의 어떤 원소와 $A$가 만나지 않는다면, $\mathcal{F}_A=\\{A\cap F: F\in\mathcal{F}\\}$가 $\emptyset$을 포함하기 때문이다. 다음 명제는 $\mathcal{F}_A$가 $A$ 위의 filter가 되지 않을 수 있는 이유는 오직 이것 뿐임을 보여준다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins> 위에서 정의한 $\mathcal{F}_A$가 $A$ 위에서의 filter가 되는 것은 $\mathcal{F}$의 임의의 원소가 $A$와 만나는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $F\cap A,F'\cap A\in\mathcal{F}_A$에 대하여 $(F\cap A)\cap(F'\cap A)=(F\cap F')\cap A$이고, $\mathcal{F}$는 filter이므로 $F\cap F'\in\mathcal{F}$가 되어 $(F\cap A)\cap(F'\cap A)\in\mathcal{F}_A$가 성립한다. 또, 만일 $F\cap A\subset G\subset A$라 하면, $G=(F\cup G)\cap A$이므로 $G\in\mathcal{F}_A$이다. 따라서 $\emptyset\not\in\mathcal{F}_A$이기만 하면 $\mathcal{F}_A$가 filter로써 잘 정의되며, 또 당연히 $\mathcal{F}_A$가 filterrㅏ 되기 위해서는 $\emptyset\not\in\mathcal{F}_A$여야 하므로 원하는 결과를 얻는다.

</details>

이제 우리는 앞서 말한 것과 같이 neighborhood filter $\mathcal{N}(x)$를 이용해 $X$ 위에서의 위상구조를 정의해야 한다. 열린집합(닫힌집합)을 이용한 정의 혹은 closure operator를 이용한 정의에서는 열린집합, 닫힌집합 혹은 closure operator들이 만족해야 할 공리가 주어졌었는데, 마찬가지로 neighborhood filter $\mathcal{N}(x)$ 또한 다음의 공리를 만족해야 한다.

<div class="misc" markdown="1">

**Neighborhood axiom.** 임의의 $z\in X$와, 각각의 원소가 $z$를 포함하는 $X$의 filter $\mathcal{N}(z)$가 주어졌다 하자. 그럼 임의의 $S\in\mathcal{N}(z)$마다 적당한 $S'\in\mathcal{N}(z)$가 존재하여, <phrase>임의의 $x\in S'$마다 $S\in\mathcal{N}(x)$</phrase>가 성립하도록 할 수 있다.

</div>

각각의 점에서의 neighborhood filter $\mathcal{N}(x)$가 위의 조건을 만족한다면, 다음과 같이 neighborhood filter가 유일한 위상구조를 정의한다는 것을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 임의의 집합 $X$에 대해, 각각의 원소 $x\in X$마다 위의 neighborhood axiom을 만족하는 $\mathcal{N}(x)$가 주어졌다 하자. 그럼 $\mathcal{N}(x)$들 각각이 $\mathcal{T}$로부터 정의된 neighborhood filter이도록 하는 유일한 위상 $\mathcal{T}$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathcal{P}(X)$에서 $\mathcal{P}(X)$로의 operator $\operatorname{int}$를 다음의 식

$$\operatorname{int}(A)=\{x\in X:A\in\mathcal{N}(x)\}$$

으로 정의하자. 그럼 임의의 $x\in\operatorname{int}(A)$에 대하여 $A\in\mathcal{N}(x)$이므로 $x\in A$이고, 따라서 $\operatorname{int}(A)\subset A$가 성립한다.

이로부터 $\operatorname{int}(\operatorname{int}(A))\subset\operatorname{int}(A)$는 자명하다. 거꾸로 $x\in\operatorname{int}(A)$라 하자. 즉 $A\in\mathcal{N}(x)$이다. 그럼 neighborhood axiom에 의하여, 적당한 $A'\in\mathcal{N}(x)$가 존재하여 $x'\in A'$일 때마다 $A\in\mathcal{N}(x')$이다. 이는 정확히 임의의 $x'\in A'$에 대하여 항상 $x'\in\operatorname{int}(A)$라는 뜻이므로, $A'\subset\operatorname{int}(A)$이고, $\mathcal{N}(x)$는 upper set이므로 $\operatorname{int}(A)\in\mathcal{N}(x)$이다. 즉, $x\in\operatorname{int}(\operatorname{int}(A))$이고, 따라서 $\operatorname{int}(\operatorname{int}(A))=\operatorname{int}(A)$가 성립한다.  

$x\in\operatorname{int}(A\cap B)$라 하자. 그럼 정의에 의해 $A\cap B\in\mathcal{N}(x)$가 성립하므로, $A,B\in\mathcal{N}(x)$이고 따라서 $x\in\operatorname{int}(A)\cap\operatorname{int}(B)$이다. 반대로 만일 $x\in\operatorname{int}(A)\cap\operatorname{int}(B)$라면 $x\in\operatorname{int}(A)$, $x\in\operatorname{int}(B)$와 neighborhood axiom으로부터 적당한 $A',B'\in\mathcal{N}(x)$가 존재하여, 임의의 $x'\in A'$와 $y'\in B'$마다 각각 $A\in\mathcal{N}(x')$ 그리고 $B\in\mathcal{N}(y')$임을 알 수 있다. 즉, $A'\subset\operatorname{int}(A),B'\subset\operatorname{int}(B)$이므로 $A'\cap B'\subset\operatorname{int}(A)\cap\operatorname{int}(B)$가 성립한다. 다시 $\mathcal{N}(x)$가 filter이므로, $A'\cap B'\in\mathcal{N}(x)$이고 따라서 $\operatorname{int}(A)\cap\operatorname{int}(B)\in\mathcal{N}(x)$이고 특히 $x\in\operatorname{int}(A)\cap\operatorname{int}(B)$가 성립한다.

마지막으로 임의의 $x\in X$에 대하여 $X$는 항상 $\operatorname{N}(x)$의 원소이므로 $x\in\operatorname{int}(X)$이다. 

이상에서 $\operatorname{int}:\mathcal{P}(X)\rightarrow\mathcal{P}(X)$는 interior operator이며, 따라서 $\operatorname{int}$에 의해 정의되는 유일한 위상 $\mathcal{T}$가 존재한다.

</details>



---

**참고문헌**

**[Sch]** E. Schechter, <i>Handbook of Analysis and Its Foundations</i>. Elements of mathematics. Academic Press, 1997.  
**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.

---
