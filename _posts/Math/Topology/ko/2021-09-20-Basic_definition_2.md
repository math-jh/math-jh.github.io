---

title: "위상공간의 기저"
excerpt: "기본정의 2: 기저"

categories: [Math / Topology]
permalink: /ko/math/topology/basic_definition_2
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-20
last_modified_at: 2022-04-07
weight: 2

---

## 위상공간의 기저

특정한 수학적 구조가 주어졌을 때, 이를 연구하기 위한 방법 중 하나는 이 구조를 잘 설명할 수 있는 부분집합을 찾는 것이다. 예컨대 선형대수학에서는 basis를 찾으면 대부분의 문제가 해결되었다. 비슷하게 위상공간도 위상구조를 설명할 수 있는 부분집합을 갖는다. 이 부분집합 또한 마찬가지로 위상의 *basis*라고 부른다. 

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $(X,\mathcal{T})$에 대하여, $\mathcal{T}$의 부분집합 $\mathcal{B}$가 $\mathcal{T}$의 *basis<sub>기저</sub>*라는 것은 임의의 $U\in\mathcal{T}$에 대하여, $U=\bigcup\_{i\in I} B\_i$를 만족하는 $\mathcal{B}$의 원소들의 family $(B\_i)\_{i\in I}$가 존재하는 것이다.

</div>

특별히 $X\in\mathcal{T}$이므로  $\mathcal{B}$는 $X$의 covering이기도 하다.  정의에 의해 $\mathcal{B}$의 원소들은 모두 열린집합들이니, 이를 $\mathcal{B}$가 $X$의 *open covering<sub>열린덮개</sub>*이라고 표현하면 적절할 것이다. ([집합론, §집합의 합, 정의 1](/ko/math/set_theory/sum_of_sets#df1))

**[Mun]**을 포함한 대부분의 저자들은 위의 정의 대신 다음을 basis의 정의로 삼는다.

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위상공간 $(X,\mathcal{T})$에 대하여, $\mathcal{B}$가 $\mathcal{T}$의 basis인 것은 세 가지 조건

1. 각각의 $x\in X$에 대하여, 적어도 하나의 $B\in \mathcal{B}$가 존재하여 $x\in B$이고,
2. 만일 $x$를 포함하는 $\mathcal{B}$의 두 원소 $B\_1$, $B\_2$가 존재한다면, 또 다른 $B\_3\in\mathcal{B}$가 존재하여 $x\in B\_3$이고 $B\_3\subseteq B\_1\cap B\_2$를 만족하고,
3. 각각의 $U\in\mathcal{T}$와 $x\in U$에 대하여, $x\in B\subseteq U$를 만족하는 $B\in\mathcal{B}$가 존재한다.

을 만족하는 것과 동치이다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathcal{B}$가 $\mathcal{T}$의 basis라 가정하자. 그럼 $\mathcal{B}$는 $X$의 open covering이므로, 1번 조건이 자명하게 성립된다. 

한편, $B\_1$, $B\_2$가 2번 조건과 같이 주어졌다면, $B\_1\cap B\_2$도 열린집합이므로 $B\_1\cap B\_2=\bigcup\_{i\in I} B\_i$를 만족하는 $\mathcal{B}$의 원소들의 family $(B\_i)\_{i\in I}$가 존재한다. 이 때, $(B\_i)\_{i\in I}$는 $B\_1\cap B\_2$의 open covering이므로, 1번 조건과 마찬가지로 2번 조건도 자명하게 성립된다. 여기에서 $B\_1\cap B\_2$를 임의의 열린집합 $U$로 바꾸면 3번을 얻는다.

거꾸로 세 개의 조건이 만족된다고 가정하고, 임의의 열린집합 $U$를 택하자. 그럼 $x\in U$에 대해, 3번 조건에 의해 $x\in B\_x\subseteq U$를 만족하는 $B\_x\in\mathcal{B}$가 존재한다. 이제 $U=\bigcup\_{x\in U} B\_x$이므로, 증명 끝.  

</details>

위의 명제로부터 다음과 같은 질문이 자연스럽게 따라온다.

> 임의의 <em_ko>집합</em_ko> $X$ 위에 앞선 조건들을 만족하는 $\mathcal{P}(X)$의 부분집합 $\mathcal{B}$가 주어졌다 하자. 그럼 $X$ 위에 위상 $\mathcal{T}$를 부여하여, $(X,\mathcal{T})$를 basis $\mathcal{B}$를 갖는 위상공간으로 생각할 수 있는가?

이 질문에 답하기 전에, [명제 2](#pp2)의 세 가지 조건 중 마지막 조건은 $\mathcal{T}$의 원소 $U$에 대한 조건이므로 $X$가 위상공간임을 이미 전제하고 있다는 것을 기억하자. 어쨌든 이 세 조건을 적절히 수정해주면 위의 질문에 대한 답은 가능하다는 것이다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 집합 $X$에 대하여, $X$의 부분집합의 family $\mathcal{B}$가 앞선 명제의 1번과 2번 조건을 만족한다고 하자. $\mathcal{T}$를 다음의 명제

> 임의의 $x\in U$마다 적절한 $B\in\mathcal{B}$가 존재하여 $x\in B\subseteq U$이도록 할 수 있다.

를 만족하는 모든 $U$들의 모임으로 정의한다면, $\mathcal{T}$는 $X$ 위에 위상공간 구조를 준다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

- 우선, $X$ 자기 자신은 $\mathcal{T}$의 원소이다. 첫 번째 조건에 의하여 임의의 $x\in X$마다 적당한 $B\in\mathcal{B}$가 존재하여 $x\in B$이도록 할 수 있는데, 이것이 정확히 $U=X$가 주어진 조건을 만족한다는 의미이다. 또 $\emptyset\in\mathcal{T}$가 vacuous하게 성립한다.

이제 $(U\_i)\_{i\in I}$가 $\mathcal{T}$의 원소들의 family라 하자. 

- $U=\bigcup\_{i\in I} U\_i$도 $\mathcal{T}$에 속한다. $U$의 임의의 원소 $x$를 택하면 이를 포함하는 $U\_i$가 존재하며, 따라서 $U_i\in\mathcal{T}$로부터 $x\in B\_i\subseteq U\_i$를 만족하는 $B\_i\in\mathcal{B}$가 존재하기 때문이다. 이러한 $B\_i$에 대하여

    $$x\in B_i\subseteq U_i\subseteq U$$

    가 성립하고 따라서 $U$는 $\mathcal{T}$의 원소이다.
- $I$가 유한집합이라 가정하자. 그럼 $U'=\bigcap\_{i\in I} U\_i$가 $\mathcal{T}$의 원소이다. $U'=\emptyset$이라면 더 이상 보일 것이 없으므로, $x\in U'$라 하자. 그럼 $x\in U\_i$가 모든 $i$에 대해 성립하고, 따라서 각각의 $i$마다 다음 조건
    
    $$x\in B_i\subseteq U_i$$

    을 만족하는 $B\_i\in\mathcal{B}$가 존재한다. 이제 임의의 $i,j\in I$에 대하여 $x\in B\_i$, $x\in B\_j$가 성립하므로, $\mathcal{B}$의 두 번째 조건에 의하여

    $$x\in B_{ij}\subseteq B_i\cap B_j$$

    를 만족하는 $B\_{ij}\in\mathcal{B}$가 존재하고 $B\_{ij}$는 $B\_{ij}\subseteq U_i\cap U_j$를 만족한다. 마찬가지로 또 다른 $k$에 대하여 $x\in B\_k$, $x\in B\_{ij}$가 성립하므로

    $$x\in B_{ijk}\subseteq B_{ij}\cap B_k$$    

    를 만족하는 $B\_{ijk}$가 존재하고 $B\_{ijk}\subseteq U\_i\cap U\_j\cap U\_k$이다. $I$는 유한집합임을 가정하였으므로, 이를 귀납적으로 반복하면 $x\in B'\subseteq U'$를 만족하는 $\mathcal{B}$의 원소 $B'$를 얻는다.

</details>

한편 [정의 1](#df1)을 더 다듬어서 다음과 같이 *subbasis*를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 위상공간 $(X,\mathcal{T})$의 *subbasis<sub>부분기저</sub>* $\mathcal{S}$는 임의의 $U\in\mathcal{T}$에 대하여, $S\subseteq U$인 $S\in\mathcal{S}$가 존재하는 $X$의 open covering을 의미한다.

</div>

$\mathcal{S}$의 원소들의 유한한 교집합들을 모아 새로운 모임 $\mathcal{B}$를 만들 수 있다. 이 모임이 basis인지를 체크하는 데 필요한 것은 오직 2번 조건 뿐인데, 어차피 $\mathcal{B}$의 원소들은 $\mathcal{S}$의 유한한 교집합으로 얻어지고, 따라서 $B\_1\cap B\_2$를 해봐야 $\mathcal{S}$의 원소들의 유한한 교집합이므로 $\mathcal{B}$가 basis가 된다. 이렇게 정의된 위상을 subbasis $\mathcal{S}$에 의해 정의된 위상이라 부른다. 이 위상은 자명하게 $\mathcal{S}$를 포함하는 위상 중 가장 약한 것이 된다. 


## 실수집합 위에 정의된 위상들

앞으로 정의해야 할 기본적인 위상수학의 개념들이 조금 남았지만, 이들 중 헷갈리는 성질 몇 가지는 실수집합 위에 정의된 standard topology에서의 반례를 통해 살펴볼 수 있다. 따라서 실수집합 위에서 정의된 위상들을 먼저 살펴본다.

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 실수집합 $\mathbb{R}$에서의 *standard topology*는 다음의 집합

$$\mathcal{B}=\{(a,b)\subset\mathbb{R}:a<b\}$$

를 basis로 하여 만들어진 위상을 의미한다. 

</div>

이 정의로부터 *반직선들*, 예컨대 $(-\infty, a)$가 열린집합임을 쉽게 확인할 수 있다.

$$(-\infty, a)=\bigcup_{x<a} (x, a)$$

이기 때문이다. 이와 비슷하게 $(b,\infty)$ 또한 열린집합이며, 따라서 $[a,b]$는 

$$[a,b]=\mathbb{R}\setminus\left((-\infty, a)\cup(b,\infty)\right)$$

이므로 닫힌집합이다. 특히, $a=b$로 주면 임의의 singleton $\\{a\\}$는 닫힌집합이 된다.

당연히 $\mathbb{R}$에 위상을 주는 방법은 이것만 있는 것이 아니다. 예를 들어, $\mathbb{R}$ 위에 discrete topology 혹은 trivial topology, cofinite topology 등등을 모두 줄 수 있다. 하지만 대부분의 경우에 쓸만한 반례로 작동하는 건 다음 두 가지다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $\mathbb{R}$의 부분집합들의 모임

$$\mathcal{B}_l=\{[a,b)\subset\mathbb{R}: a<b\}$$

을 basis로 하여 만들어진 위상을 *lower limit topology<sub>하극한위상</sub>*라고 부른다. 한편, 집합 

$$K=\{1/n:n\in\mathbb{N}^{>0}\}$$

이라 하면, standard topology의 basis $\mathcal{B}$에, $(a,b)\setminus K$꼴의 원소들을 추가하여 만든 집합 $\mathcal{B}\_K$를 생각하자. 이를 basis로 하여 만들어진 위상은 *$K$-topology*라고 불린다.[^1]
</div>

이렇게 만들어지는 위상 두 개는 모두 standard topology와는 다르다. 

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $\mathbb{R}\_l$과 $\mathbb{R}\_K$는 모두 $\mathbb{R}$보다 strict하게 강한 위상이다. 또, $\mathbb{R}\_l$과 $\mathbb{R}\_K$는 비교가 가능하지 않다.

</div>

이들 세 위상은 모두 basis를 이용해 정의되었으므로, [§열린집합과 닫힌집합, 정의 3](/ko/math/topology/basic_definition_1#df3)을 basis의 언어로 풀어 쓸 필요가 있다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> $X$ 위에 두 위상 $\mathcal{T}$, $\mathcal{T}'$가 각각 basis $\mathcal{B}$, $\mathcal{B}'$를 통해 정의되었다고 하자. 그럼 $\mathcal{T}\subset\mathcal{T}'$인 것은 $\mathcal{B}$의 임의의 원소 $B$와 $x\in B$에 대하여, $x$를 포함하며 $B$에 포함되는 $\mathcal{B}'$의 원소 $B'$이 존재하는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\mathcal{T}\subset\mathcal{T}'$라 하자. 즉, $\mathcal{T}'$가 $\mathcal{T}$보다 강하다. 임의로 주어진 $B\in\mathcal{T}$와 $x\in B$에 대하여, $B$가 $\mathcal{T}'$에서 열린집합이기 위해서는 $x$를 포함하고 $B$에 포함된 $\mathcal{B}'$의 원소 $B'$가 존재해야 하는데 ([명제 2](#pp2)), 이것이 정확히 주어진 조건이다.

거꾸로 주어진 조건이 성립한다 하고, 임의의 $U\in\mathcal{T}$는 $\mathcal{T}'$의 원소이기도 하다는 것을 보이자. 이는 임의의 $x\in U$에 대하여, $U$에 포함되고 $x$를 포함하는 $\mathcal{B}'$의 원소 $B'$가 존재한다는 것을 보이는 것과 같다. 그런데, $U$는 $\mathcal{T}$에서 열린집합이므로 $x\in B\subseteq U$를 만족하는 $B\in\mathcal{T}$가 존재하고, 주어진 조건에 의하여 $x\in B'\subseteq B$를 만족하는 $B'\in\mathcal{T}$가 존재하므로 정확히 이 $B'$가 이를 만족한다.
</details>

이 보조정리와 함께라면 앞선 명제를 쉽게 보일 수 있다. 

<details class="proof--alone" markdown="1">
<summary>명제 7의 증명</summary>
우선, $\mathbb{R}\_l$은 $\mathbb{R}$보다 강하다. $\mathbb{R}$의 basis의 원소 $(a,b)$를 택하자. 그럼 임의의 $x\in (a,b)$에 대하여, $[x,b)$가 $(a,b)$에 포함되고 $x$를 포함하는 $\mathcal{B}\_l$의 원소이다.  
그러나 그 역은 성립하지 않는다. 만일 $\mathbb{R}$이 $\mathbb{R}\_l$보다 강하다면, $\mathbb{R}\_l$의 basis의 원소 $[a,b)$와 $x\in [a,b)$에 대하여, $x$를 포함하고 $[a,b)$에 속하는 $\mathcal{B}$의 원소 $(c,d)$가 존재해야 한다. 그런데 $x=a$로 두면 이러한 원소는 존재할 수 없다. $a\in (c,d)$이기 위해서는 $c<a$여야 하는데, 이것이 만족되는 순간 $(c,d)\not\subseteq [a,b)$이기 때문이다. 

한편, 정의에 의해 $\mathbb{R}\_K$가 $\mathbb{R}$보다 강한 것은 자명하므로, 이 반대가 성립하지 않는다는 것만 보이면 된다. $\mathcal{B}\_K$의 원소 $(-1,1)\setminus K$를 생각하자. 그럼 $0\in(-1,1)\setminus K$이다.  
그러나, $0$을 포함하며 $(-1,1)\setminus K$에 포함되는 $\mathcal{B}$의 원소 $(c,d)$는 존재하지 않는다. $0\in (c,d)$이기 위해서는 $0<d$여야 하는데, $n$을 충분히 크게 잡으면 $1/n<d$이도록 할 수 있으므로, 이러한 $n$에 대하여 $1/n\not\in (-1,1)\setminus K$이지만 $1/n\in (c,d)$이기 때문이다.

마지막으로 $\mathbb{R}\_l$과 $\mathbb{R}\_K$를 비교할 수 없다는 것을 보이자. 우선 $\mathcal{B}\_K$의 원소 $(-1,1)\setminus K$에 대하여, 0을 포함하고 $(-1,1)\setminus K$에 포함되는 $[c,d)$가 존재하지 않는다는 것은 앞선 문단과 똑같이 보일 수 있다. 따라서 $\mathbb{R}\_l$은 $\mathbb{R}\_K$보다 강하지 않다.  
한편, $1<a$인 $a$에 대하여, $\mathcal{B}\_l$의 원소 $[a,b)$를 생각하자. 그럼 $a$를 포함하고 $[a,b)$에 포함된 $\mathcal{B}\_K$의 원소는 존재하지 않는다. 어차피 $[a,b)$에 포함될 수 있는 $\mathcal{B}\_K$의 원소는 모두 $\mathcal{B}$의 원소들이므로, 첫 번째 문단과 동일하게 진행하면 된다.

</details>


---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

[^1]: 문자 $K$는 머리빗을 뜻하는 독일어 *Kamm*으로부터 온 것이다.
