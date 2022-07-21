---

title: "동치관계"
excerpt: "동치관계의 정의와 성질들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/equivalence_relations
header:
    overlay_image: /assets/images/Set_theory/Equivalence_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-22
last_modified_at: 2022-05-17
weight: 9

---

이제 우리는 동치관계에 대해 살펴본다.

## 동치관계의 정의

<div class="definition" markdown="1">
<ins id="df1">**정의 1**</ins> $R$이 이항관계라 하자. $R$이 *symmetric<sub>대칭적</sub>*이라는 것은 $x\mathrel{R}y$가 성립하면 $y\mathrel{R}x$도 성립하는 것이다. 만일 

$$(x\mathrel{R}y)\wedge(y\mathrel{R}z)\implies  x\mathrel{R}z$$

가 성립할 경우, 이를 *transitive<sub>추이적</sub>*라고 한다. 마지막으로 어떠한 집합 $A$에 대하여 $x\mathrel{R}x \implies x\in A$일 경우, $R$이 $A$ 위에서 *reflexive<sub>반사적</sub>*라고 한다. Symmetric, transitive, 그리고 어떤 집합 $A$ 위에서 reflexive한 관계 $R$을 *동치관계<sub>equivalence relation</sub>*라 부른다. 
</div>

우리는 종종 $x\mathrel{R}y$대신 $x\equiv y\mod R$과 같이 쓰며, 혼동의 여지가 없을 때에는 $x\equiv y$로만 쓰기도 한다. 다만 이 글에서는 최대한 엄밀한 표현을 유지한다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 변수 $x$, $y$에 대한 관계 $x=y$는 symmetric하고 transitive하지만 그래프를 갖지 않는다. ([§이항관계의 그래프, 예시 2](/ko/math/set_theory/binary_relation#ex2)) 따라서 이 관계 자체는 동치관계가 되지 않는다. 

반면 만일 우리가 앞의 정의를 다듬어서 <phrase>$x=y$이고 $x\in A$</phrase>로 정의한다면 이 관계는 $A$ 위에서 reflexive하므로, 그래프 $\Delta_A$를 갖는다. 한편 <phrase>$x\in A$이고 $y\in A$</phrase> 또한 $A$ 위에서의 동치관계다. 이 때의 그래프는 $A\times A$가 된다.  

임의의 동치관계의 그래프 $\Gamma$는 reflexive 조건에 의해 항상 $\Delta_A$를 부분집합으로 포함해야 하므로, 첫 번째 예시는 $A$ 위에서 정의될 수 있는 동치관계의 그래프 중 가장 작은 것이고, 두 번째 예시는 당연히 $A$ 위에서 정의될 수 있는 가장 큰 그래프이다. 

</div>

다음은 동치관계의 정의를 조금 더 수식적으로 다듬은 것이다.

<div class="proposition" markdown="1">

<ins id="pp3">**명제 3**</ins> Correspondence $\Gamma=(G,A,A)$가 $A$ 위에서의 동치관계인 것은 

1. $\Gamma$의 정의역이 $A$이고,
2. $\Gamma=\Gamma^{-1}$이고,
3. $\Gamma\circ\Gamma=\Gamma$   

인 것과 동치이다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>
만일 $\Gamma$가 $A$ 위에서의 동치관계라면 모든 $x\in A$에 대해 $(x,x)\in G$이다. 따라서 $A$는 $\Gamma$의 정의역이다. 또, 만일 $(x,y)\in G$라면 $(y,x)\in G$이고, 이는 $(x, y)\in G^{-1}$과 동치이므로, $\Gamma=\Gamma^{-1}$이다. 마지막으로 임의의 $(x,y)\in G$에 대하여 $(x,x)\in G$이고 $(x, y)\in G$이므로 $(x,y)\in G\circ G$이며, 반대로 임의의 $(x, y)\in G\circ G$에 대해 어떠한 $z$가 존재하여 $(x,z)\in G$이고 $(z,y)\in G$이므로 transitivity에 의해여 $(x, y)\in G$이다. 따라서 $\Gamma\circ\Gamma=\Gamma$이다.  

반대로 $\Gamma$가 주어진 조건들을 만족하는 correspondence이라 하자. 만일 $(x, y)\in G$라면, 조건 2에 의하여 $(y,x)\in G^{-1}=G$이므로 관계 $(x,y)\in G$는 symmetric이다. 또, 만일 $(x, y)\in G$이고 $(y,z)\in G$라면 조건 3에 의해 $(x,z)\in G\circ G=G$이므로 이 관계는 transitive이며, 마지막으로 조건 1에 의하여 $G$의 정의역은 $A$이고, 따라서 임의의 $x\in A$에 대해 $(x, y)\in G$라 하면 symmetry에 의해 $(y,x)\in G$, transitivity에 의해 $(x,x)\in G$이므로 $A$ 위에서 reflexive하다. 따라서 이는 동치관계다.
</details>

이제부터 동치관계들의 성질을 살펴보고, 다양한 동치관계들의 예시를 살펴보자.

## 함수에 의해 정의되는 동치관계

<div class="proposition" markdown="1">
<ins id="pp4">**명제 4**</ins> $f$가 함수이고 $A$를 정의역으로 갖는 함수라 하자. 그럼 $x$, $y$ 사이의 관계 <phrase>$x$, $y\in A$이고 $f(x)=f(y)$</phrase>는 $A$ 위에서의 동치관계다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

주어진 관계가 $A$ 위에서 reflexive함은 자명하다. 한편, 만일 $f(x)=f(y)$라면 $f(y)=f(x)$이고, $f(x)=f(y)$, $f(y)=f(z)$이면 $f(x)=f(z)$이므로 이 관계는 symmetric, transitive하기도 하다.

</details>

<div class="definition" markdown="1">

<ins id="df5">**정의 5**</ins> 위의 명제에서 정의된 동치관계를 *$f$에 의해 정의된 동치관계*라 부른다.

</div>

위의 정의에서, $F$를 $f$의 그래프라 하자. 그럼 $x\equiv y$인 것은 <phrase>어떠한 $z$가 존재하여 $(x,z)\in F$이고 $(y, z)\in F$인 것</phrase>과 동치이다. 이는 다시 <phrase>어떠한 $z$가 존재하여 $(x, z)\in F$이고 $(z, y)\in F^{-1}$인 것</phrase>과 동치이므로, 이 동치관계의 그래프는 $F^{-1}\circ F$가 된다. 

## 동치관계와 분할

한편, 우리가 앞서 정의했던 분할 ([§집합의 합, 정의 4](/ko/math/set_theory/sum_of_sets#df4))은 동치관계와 아주 깊은 관계가 있다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $R$이 $A$ 위에서의 동치관계라 하고, $G$를 $R$의 그래프라 하자. 그럼 모든 $x\in A$에 대하여, $x$에서의 section $G(x)$를 $R$에서 $x$의 *equivalence class<sub>동치류</sub>*라 부른다. 이러한 equivalence class들의 모임을 $R$의 *quotient set<sub>몫집합</sub>*이라 부르고, $A/R$로 표기한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 집합 $A$ 위에서 <phrase>$x=y$</phrase>는 동치관계가 됨을 이미 살펴보았다. 이 관계에서 $x$의 equivalence class는 집합 $\{x\}$이다. 한편 동일한 예시에서 <phrase>$x\in A$이고 $y\in A$</phrase> 또한 동치관계였는데, 이 경우 $x$의 equivalence class는 $E$ 전체가 된다. 이런 관점에서 첫 번째 관계는 집합 $E$ 위에서 정의된 가장 조밀한 동치관계라 할 수 있고, 두 번째는 가장 성긴 동치관계라 할 수 있다.

</div>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $R$이 $A$ 위에서의 동치관계라 하자. 그럼 어떠한 함수 $p$가 존재하여, $R$을 $p$에 의해 정의된 동치관계로 볼 수 있다.

</div>

이는 다음의 보조정리로부터 자명하다.

<div class="proposition" markdown="1">

<ins id="lem9">**보조정리 9**</ins> $R$이 $A$ 위의 동치관계라 하고, $p:A\rightarrow A/R$을 $x\mapsto G(x)$로 정의하자. 그럼 $x\mathrel{R}y$와 $p(x)=p(y)$는 서로 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $(x,y)\in G$라 하자. 그럼 $y\in G(x)$로부터 $G(y)\subset G(G(x))=G(x)$이다. 비슷하게 $G(x)\subset G(y)$이므로 $p(x)=G(x)=G(y)=p(y)$이다. 반대로 만일 $G(x)=G(y)$라면, $x\in G(x)=G(y)$이므로 $(y, x)\in G$가 되어 보조정리가 성립한다.
</details>

위의 함수 $p$를 canonical이라 부른다. 위의 정리로부터 equivalence class들은 서로소라는 것을 알 수 있으므로, 동치관계는 집합 $A$의 분할을 유도한다. 반대로,

<div class="definition" markdown="1">

<ins id="pp10">**명제 10**</ins> $(A_i)\_{i\in I}$가 $A$의 분할이라 하자. 그럼 

> 어떤 $i$가 존재하여 $x,y\in A_i$이다

는 $x$, $y$에 대한 동치관계이다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위의 관계를 $R$이라 적자. 그럼 $R$이 $E$ 위에서 reflexive인 것은 자명하다. 또, $x$와 $y$가 같은 집합에 포함되면 $y$와 $x$도 같은 집합에 포함되므로 $x\mathrel{R}y$이면 $y\mathrel{R}x$이다. 즉 $R$은 symmetric하다. 마지막으로 만일 $x\mathrel{R}y$이고 $y\mathrel{R}z$라면, $x,y\in A_i$이고 $y,z\in A_j$이다. 그런데 $y\in A_i\cap A_j$이고 $(A_i)_{i\in I}$가 partition이므로 $i=j$이다. 따라서 $x,z\in A_i$이고 명제가 성립한다.
</details>

## 단항관계와 compatible한 동치관계

<div class="definition" markdown="1">

<ins id="df11">**정의 11**</ins> $R$이 동치관계라 하자. 그럼 단항관계 $P$가 $R$과 *compatible*하다는 것은 $P(x)\wedge (x\mathrel{R}y)\implies P(y)$인 것이다.

</div>

예를 들어, 단항관계 

>$x$는 짝수이다

는 동치관계 

>$x-y$가 4의 배수이다

와 compatible하다. Equivalence class의 관점에서 위 정의를 다시 쓰면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="pp12">**명제 12**</ins> $R$이 집합 $A$ 위에서의 동치관계이고, $P$가 $R$과 compatible한 단항관계라 하자. 그럼 <phrase>$t\in A/R$이고 어떤 $x\in t$가 존재하여 $P(x)$인 것</phrase>과 <phrase>$t\in A/R$이고 모든 $x\in t$에 대하여 $P(x)$인 것</phrase>이 서로 동치이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>
일상적인 언어로 풀어 쓰자면, 

> $P$가 $R$과 compatible할 때, equivalence class의 단 하나의 원소만 $P$를 만족한다면, 그 원소와 같은 class에 들어있는 모든 원소에 대해서도 $P$가 성립한다.

그리고 이건 정확히 compatible한 단항관계의 정의다. 

반대 방향은 자명하다. 만일 $t\in A/R$에 대하여 $a\in t$가 존재하여 $P(a)$라 하자. 그럼 모든 $x\in t$에 대하여 $a R x$이므로 $P(x)$이다.
</details>

## 동치관계의 포화

흐름만 놓고 보자면 다음 정의는 [정의 6](#df6) 직후에 나왔어야 하지만, 이를 정의하기 위해서는 앞선 [정의 11](#df11)이 필요하다.

<div class="definition" markdown="1">

<ins id="df13">**정의 13**</ins> $R$이 $A$ 위에서의 동치관계이고 $A'$가 $A$의 부분집합이라 하자. $A'$가 $R$에 대해 *saturated<sub>포화</sub>*되었다는 것은 단항관계 $x\in A$가 $R$과 compatible한 것이다.

</div>

$G$를 $R$의 그래프라 하자. 위의 정의에 따르면, 어떤 집합 $A'$가 $R$에 대해 saturated이기 위해서는 <phrase>$x\in A'$라면 $G(x)\subset A'$</phrase>가 반드시 성립해야 한다. 따라서 saturated인 부분집합 $A'$는 어떠한 부분집합 $B\subset A$에 대하여 $\bigcup\_{x\in B}G(x)$로 나타낼 수 있는 집합이다. 이로부터 다음의 두 결과를 쉽게 확인할 수 있다.

1. 만일 $(A\_i)\_{i\in I}$가 saturated인 부분집합들의 family라면, $\bigcup\_{i\in I} A_i$와 $\bigcap\_{i\in I} A_i$가 saturated이다.
2. Saturated인 부분집합 $A'$에 대해 $A\setminus A'$ 또한 saturated이다.

이번에는 canonical map $f:A\rightarrow A/R$과 그 그래프 $F$를 생각하자. [§이항관계의 그래프, 명제 14](/ko/math/set_theory/binary_relation#pp14)에 의하여 $f^{-1}(f(A'))\supseteq A'$가 성립하며, 일반적인 경우에 반대쪽 포함관계는 성립하지 않는다. 그러나 만일 $A'$가 saturated라면 반대쪽 포함관계도 성립한다. 각각의 $x\in A'$에 대하여, $f^{-1}(\left\\{f(x)\right\\})\subseteq A'$이므로

$$f^{-1}(f(A'))=\bigcup_{x\in A'}f^{-1}(\left\{f(x)\right\})\subseteq A'$$

가 성립하기 때문이다.

더 일반적으로, $B$가 임의의 집합이라 하자. $f^{-1}(f(B))$는 여전히 saturated이다. 만일 $x\in f^{-1}(f(B))$라 하면 $z\in F(x)$에 대하여 어떠한 $y\in f(B)$가 존재하여 $(y,x)\in F^{-1}$이므로 $(x, y)\in F$이고, 따라서 transitivity에 의하여 $(z,x)\in F$이면 $(z,y)\in F$이고   $z\in f^{-1}(f(B))$이기 때문이다. 만일 $\overline{B}$가 $B$를 포함하는 saturated subset이라면, 

$$\overline{B}=f^{-1}(f(\overline{B}))\supseteq f^{-1}(f(B))$$

이므로 $f^{-1}(f(B))$는 $B$를 포함하는 saturated subset 가운데서 가장 작은 것이다. 이를 $B$의 *saturation*이라 부른다.

## Canonical decomposition

<div class="definition" markdown="1">

<ins id="df14">**정의 14**</ins> 집합 $A$ 위에서 정의된 동치관계 $R$이 주어졌다고 하자. $A$를 정의역으로 갖는 함수 $f$에 대하여, $f$가 $R$과 *compatible*하다는 것은 $x$에 대한 단항관계 $y=f(x)$가 $R$과 compatible하다는 것을 의미한다.

</div>

즉, $f$가 $R$과 compatible하려면 $f$는 각각의 equivalence class로 제한하였을 때 상수함수가 되어야 한다. 만일 $x\mathrel{R}x'$라면 $f(x)=y=f(x')$이여야 하기 때문이다. 이제 [§함수 (2), 명제 4](/ko/math/set_theory/functions_2#pp4)를 적용하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="pp15">**명제 15**</ins> $R$이 집합 $A$ 위에서의 동치관계이고, $p:E\rightarrow E/R$이 canonical이라 하자. 그럼 $f:A\rightarrow B$가 $R$과 compatible한 것은 어떤 $h:A/R\rightarrow B$에 대하여 $f$가 $h\circ p$의 꼴로 쓰여질 수 있는 것과 동치이다.

</div>

즉, 다음의 diagram이 commute한다.

![induced_injection](/assets/images/Set_theory/Equivalence_relations-1.png){:width="147.6px"  class="invert" .align-center}

이 때 $h$는 $p$의 section $s$에 의하여 $h=f\circ s$로 유일하게 결정된다. $h$는 $f$에 의해 induce되었다고 한다. 

특별히 $R$이 $f$에 의해 정의된 동치관계([정의 5](#df5))라 하자. 다음의 diagram을 생각할 수 있다.

![canonical_decomposition](/assets/images/Set_theory/Equivalence_relations-2.png){:width="262.05px"  class="invert" .align-center}

이 때 $\tilde{f}$는 $f$의 공역 $F$를 $f(A)$로 제한하여 얻어지는 함수이고, $j$는 canonical injection, 그리고 $p$는 $R$에 해당하는 canonical mapping이다. 따라서 우리는

$$f=j\circ\tilde{f}=j\circ h\circ p$$

를 얻는다. 만일 어떠한 $t, t'\in A/R$에 대해 $h(t)=h(t')$라면, $x\in t$, $x'\in t'$에 대하여 $f(x)=f(x')$이므로 $x\mathrel{R}x'$이고, 따라서 $t=t'$가 되어 $h$는 단사함수이다. 그런데 $h$의 공역은 $f$의 치역으로 제한된 상태이므로, $h$는 전사함수이기도 하다. 따라서 $h$는 전단사이며, 위의 식을 $f$의 *canonical decomposition*이라 부른다.

추가로 공역 $B$에 동치관계 $S$가 주어졌다고 하자. 그럼 우선 다음의 diagram을 얻는다.

![induced_mapping_of_equivalence](/assets/images/Set_theory/Equivalence_relations-3.png){:width="172.5px"  class="invert" .align-center}

만일 $q\circ f$이 $R$과 compatible하다면, $f$가 두 동치관계 $R$, $S$와 compatible하다고 한다. [명제 15](#pp15)에 의해 이는 다시 $h:A/R\rightarrow B/S$가 존재하여 $h\circ p=q\circ f$인 것과 동치이다. 

또, 공역 $B$에 정의된 동치관계 $S$로부터 $A$ 위에 동치관계를 만들 수도 있다. 우선 $f:A\rightarrow B$이고 $S$가 $B$ 위에서의 동치관계, 그리고 $p:B\rightarrow B/S$가 canonical이라 하자. 이 상황을 diagram으로 나타내면 다음과 같다.

![inverse_image_of_equivalence](/assets/images/Set_theory/Equivalence_relations-4.png){:width="145.5px"  class="invert" .align-center}

그럼 우리는 함수 $p\circ f$에 의해 정의되는 동치관계 $R$을 $A$ 위에 정의할 수 있다. 이를 $S$의 $f$에 의한 *inverse image*라 부른다.

<ins id="df16">**정의 16**</ins>  $R$, $S$가 동치관계들이라 하자. $S$가 $R$보다 *finer<sub>세밀하다</sub>*하다는 것은 $x\mathrel{S}y\implies x\mathrel{R}y$가 항상 성립하는 것이다.
{: .definition}

두 동치관계 $R,S$가 집합 $A$ 위에서 정의된 동치관계이고, $S$가 $R$보다 finer하다고 하자. 

![third_iso_1](/assets/images/Set_theory/Equivalence_relations-5.png){:width="171.3px"  class="invert" .align-center}

그럼 함수 $p_S$가 전사함수이고, $p_S(x)=p_S(y)\implies p_R(x)=p_R(y)$가 항상 성립한다. 따라서 유일한 함수 $h:A/S\rightarrow A/R$이 존재하여 $p_R=h\circ p_S$이다. ([§함수 (2), 명제 4](/ko/math/set_theory/functions_2#pp4)) 

위와 같이 정의된 함수 $h$에 대하여, $h$에 의해 $A/S$ 위에 정의된 동치관계를 $R$의 $S$에 의한 *quotient*라 부르고, $R/S$로 적는다. 이 상황은 canonical decomposition을 거치면 다음과 같다. 

![third_iso_2](/assets/images/Set_theory/Equivalence_relations-6.png){:width="368.25px"  class="invert" .align-center}

위의 $k$는 앞선 canonical decomposition의 정의에 의하여 전단사함수가 된다. 

## 동치관계의 product
마지막으로 두 equivalence relation $R$, $R'$이 주어졌다고 하자. 만일 우리가 $S$를 다음의 relation

> $u\mathrel{S}v$인 것은 어떠한 $x$, $x'$, $y$, $y'$가 존재하여 $u=(x,x')$, $v=(y,y')$이고 $x\mathrel{R}y$, $x'\mathrel{R}y'$인 것이다

로 정의한다면 $S$가 equivalence relation이 됨은 자명하다. 이 equivalence relation을 $R$과 $R'$의 *product*이라 부른다. 이제 주어진 집합 $E$, $E'$를 정의역으로 갖는 함수 $f$, $f'$가 주어졌다고 하고, $R$과 $R'$을 각각 $f$와 $f'$에 의해 유도되는 equivalence relation이라 하자. 그럼 약간의 노력을 통해 $f\times f'$에 의해 유도되는 equivalence relation이 $R\times R'$과 같음을 보일 수 있다. 따라서 우리는 $(E\times E')/(R\times R')$과 $(E/R)\times(E'/R')$ 사이의 bijection을 만들 수 있다.



---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

