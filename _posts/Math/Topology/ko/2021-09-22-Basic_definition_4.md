---

title: "연속함수"
excerpt: "기본정의 4: 연속함수"

categories: [Math / Topology]
permalink: /ko/math/topology/basic_definition_4
header:
    overlay_image: /assets/images/Topology/Topological_basis.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2021-09-22
last_modified_at: 2022-04-07
weight: 4

---

## 연속함수

이제 우리는 연속함수의 개념을 정의한다. 직관적으로 이는 대수적인 설정에서의 homomorphism과 마찬가지로 위상구조를 보존하는 함수라 생각할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 임의의 위상공간 $X$, $Y$ 사이의 함수 $f:X\rightarrow Y$가 $x\in X$에서 *연속<sub>continuous</sub>*이라는 것은 $f(x)\in Y$의 임의의 열린근방 $V$에 대하여, $f(U)\subset V$이도록 하는 $x$의 열린근방 $U$가 존재하는 것이다. 만일 $f$가 $X$의 모든 점에서 연속이라면, $f$를 *연속함수<sub>continuous function</sub>*라 부른다.

</div>

정의에 의해 항등함수가 연속임은 자명하다. 또, 실수에서 실수로의 연속함수의 정의는 정확하게 $\epsilon$-$\delta$ 정의와 일치한다. (ref) 

<div class="proposition" markdown="1">

<ins is="pp2">**명제 2**</ins> 두 위상공간 $X,Y$와 함수 $f:X\rightarrow Y$에 대하여, 다음이 모두 동치이다.

1. $f$가 연속이다. 
2. $Y$의 임의의 열린집합 $V$에 대하여, $f^{-1}(V)$가 $X$에서 열린집합이다.
3. $Y$의 임의의 닫힌집합 $C$에 대하여, $f^{-1}(C)$가 $X$에서 닫힌집합이다.
4. $X$의 임의의 부분집합 $A$에 대하여, $f(\operatorname{cl}A)\subset\operatorname{cl}f(A)$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $f$가 연속이라 하자. 2번을 보이기 위해서는 $Y$의 임의의 열린집합 $V$가 주어졌다고 가정한 후, $f^{-1}(V)$가 열린집합임을 보여야 한다. 이를 위해 임의의 $x\in f^{-1}(V)$를 택하자. 그럼 $f(x)\in V$이므로 $V$는 $f(x)$의 열린근방이다. 따라서, $x$의 어떤 열린근방 $U$가 존재하여 $f(U)\subset V$이고 

$$U\subset f^{-1}(f(U))\subset f^{-1}(V)$$

이 성립하므로 $f^{-1}(V)$는 열린집합이다. 

이제 2번이 만족된다고 하고, $Y$의 임의의 닫힌집합 $C$가 주어졌다 하자. 그럼 $V=Y\setminus C$는 열린집합이므로, 2번 조건에 의하여 $f^{-1}(V)$는 $X$에서 열린집합이다. 그런데 

$$f^{-1}(V)=f^{-1}(Y\setminus C)=X\setminus f^{-1}(C)$$

이므로, $X\setminus f^{-1}(C)$가 열린집합이고 따라서 $f^{-1}(C)$는 닫힌집합이다. 

이제 3번을 가정하고 4번을 보이자. $X$의 임의의 부분집합 $A$에 대하여, $\operatorname{cl}f(A)$는 $Y$의 닫힌집합이므로, $f^{-1}(\operatorname{cl}f(A))$는 $X$의 닫힌집합이다. 또, 이 집합은 항상 $A$를 포함하므로, $\operatorname{cl}A$도 포함해야 한다. 즉

$$\operatorname{cl}A\subset f^{-1}(\operatorname{cl}f(A))$$

가 성립하고, 따라서 

$$f(\operatorname{cl}A)\subset f(f^{-1}(\operatorname{cl}f(A))\subset \operatorname{cl}f(A)$$

또한 성립한다. 

마지막으로 4번이 성립한다고 가정하자. 임의의 $x\in X$에 대해 $f(x)\in Y$의 열린근방 $V$가 주어졌다고 하면, $V^c$는 닫힌집합이므로 $\operatorname{cl}V^c=V^c$이고, 따라서 

$$f(\operatorname{cl}f^{-1}(V^c))\subset \operatorname{cl}(f(f^{-1}(V^c))\subset\operatorname{cl}V^c=V^c$$

가 성립한다. $f(x)\not\in V^c$이므로, $x\not\in\operatorname{cl}f^{-1}(V^c)$이고, 따라서 

$$U= \left(\operatorname{cl}f^{-1}(V^c)\right)^c$$

라 하면 $x\in U$이다. $U$는 닫힌집합의 여집합이므로 열린집합이고, 따라서 $x$의 열린근방이 된다. 이제 $f(U)\subset V$임을 보여야 하는데, 임의의 $x'\in U$에 대하여, $x'\not\in \operatorname{cl}(f^{-1}(V^c))$이고 따라서 $x'\not\in f^{-1}(V^c)$이다. 즉, $f(x')\not\in V^c$이므로 $f(x')\in V$이고, $f(U)\subset V$가 성립한다.
</details>

2번의 결과가 특히 눈여겨볼만한데, 일반적인 대수구조는 $X$에서의 연산이 $Y$의 연산으로 보내지는 형태를 homomorphism이라 생각하지만, 위상구조에서는 방향이 반대로 바뀌어 $Y$의 열린집합의 preimage가 $X$의 열린집합이 되는 함수를 연속함수라 부르고 있다. 
이는 위상구조가 단순히 $X$라는 집합 위의 연산 등으로 정의되는 대신, $X$의 부분집합들의 모임 (열린집합들) 위에 정의되었고, 이들 사이의 연산은 함수에 의한 image가 아닌 preimage에 의해 보존되기 때문이다. ([집합론, §합집합과 교집합, 명제 7](/ko/math/set_theory/union_and_intersection#pp7)) 

또, 앞서 우리는 열린집합과 닫힌집합이 거의 동일한 개념이라고 한 적이 있었는데, 역시 위의 명제의 2번과 3번을 비교하여도 이를 확인할 수 있다. 마찬가지로 4번과 비슷한 다음의 명제

> $f:X\rightarrow Y$가 연속인 것은 $f^{-1}(\operatorname{int}A)\subset\operatorname{int} f^{-1}(A)$인 것과 동치이다.

도 쉽게 증명할 수 있다. 어쨌든 이렇게 구조를 잘 보존하는 함수를 정의한 후에는 그 합성을 생각해야 한다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> 위상공간들 $X,Y,Z$가 주어졌다고 하자. 만일 $f:X\rightarrow Y$와 $g:Y\rightarrow Z$가 연속이라면, 그 합성 $g\circ f$ 또한 연속이다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 열린집합 $W\subset Z$에 대하여, 

$$(g\circ f)^{-1}(W)=f^{-1}(g^{-1}(W))$$

이고, $g$의 연속성에 의해 $g^{-1}(W)$는 열린집합이므로, $f$의 연속성을 다시 한 번 적용하면 $f^{-1}(g^{-1}(W))$도 열린집합이다.
</details>

또, 연속함수에 의해 *같은 것*으로 취급되는 위상공간도 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 연속함수 $f:X\rightarrow Y$가 *homeomorphism<sub>위상동형사상</sub>*이라는 것은, 또 다른 연속함수 $g:Y\rightarrow X$가 존재하여 $f\circ g=\operatorname{id}_Y$이고 $g\circ f=\operatorname{id}_X$인 것이다.
</div>

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 대수적인 구조들과는 다르게, bijective한 연속함수가 항상 homeomorphism이 되는 것은 아니다. 이는 연속함수의 역함수가 연속이 되리라는 보장이 없기 때문이다. 

예를 들어, standard topology가 주어진 ([§위상공간의 기저, 정의 5](/ko/math/topology/basic_definition_2#df5)) 실수에서 실수로의 함수 

$$f(x)=\begin{cases}x&x<1\\ x-1&x\geq 2\end{cases}$$

는 연속이지만, 이 함수의 역함수는

$$g(x)=\begin{cases} x&x<1\\ x+1&x\geq 1\end{cases}$$

이므로 연속이 아니다.

![bijective_conti_but_not_homeo](/assets/images/Topology/Basic_definition_4-1.png){:width="250px"  class="invert" .align-center}

</div>

위상공간 $X$에서 $T_1$공간 $Y$로의 함수들의 수열 $(f_n)_{n=1}^\infty$가 주어졌다 하자. 각각의 점 $x\in X$에 대하여, $Y$의 점들로 이루어진 수열 $(f_n(x))_1^\infty$를 생각할 수 있다. 이들 수열이 임의의 점 $x$에 대하여 항상 수렴한다면, 대응 $x\mapsto \lim f_n(x)$이 잘 정의되며 $X$에서 $Y$로의 함수가 된다. 이 함수를 $f:X\rightarrow Y$라 적자. 만일 $f_n$들이 모두 연속함수였다면 $f$가 연속이 되는지를 생각해볼 수 있다. 다음 예시는 이에 대한 반례를 제공한다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 함수 $f_n$을 다음의 식

$$f_n(x)=\begin{cases}0&\lvert x\rvert\geq 1/n\\ nx+1&-1/n<x\leq 0\\ -nx+1&0<x<1/n\end{cases}$$

으로 정의하자. 그럼 각각의 $f_n$은 모두 연속함수이지만, 그 극한 $f$는

$$f(x)=\begin{cases}1&x=0\\ 0&x\neq 0\end{cases}$$

이 되므로 연속함수가 아니다.

</div>  

직관적으로 이러한 상황은 $0$에 가까이 있는 점일수록 함수 $f$로 수렴하기 위해서는 더 큰 $n$이 필요하기 때문이다. 즉, 각각의 점마다 수렴속도가 다르기 때문이다. 여기에서 필요한 조건을 이야기하기 위해서는 거리를 정의해야 하므로, 이에 대한 이야기는 나중으로 미룬다.

---

**참고문헌**

**[Mun]** J.R. Munkres, <i>Topology</i>. Featured Titles for Topology. Prentice Hall, Incorporated, 2000.

---

