---

title: "집합의 합"
excerpt: "집합들 사이의 합 (분리합집합)"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/sum_of_sets
header:
    overlay_image: /assets/images/Set_theory/Sum_of_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-15
last_modified_at: 2022-05-17
weight: 7

---

## Covering
<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> Family $(A\_i)\_{i\in I}$가 집합 $A$의 *covering<sub>덮개</sub>*이라는 것은 $A=\bigcup\_{i\in I} A\_i$임을 뜻한다. $A$의 두 covering $(A\_i)\_{i\in I}$와 $(A'\_j)\_{j\in J}$에 대하여, $(A'_j)\_{j\in J}$가 $(A_i)\_{i\in I}$보다 *finer*하다는 것은 임의의 $j\in J$에 대하여, $A'\_j\subseteq A\_i$를 만족하는 $i\in I$가 존재하는 것이다.

</div>


집합 $A$의 covering $(A\_i)\_{i\in I}$이 주어졌을 때, 전사함수 $f:A\rightarrow B$가 주어진다면 $(f(A\_i))\_{i\in I}$는 $B$의 covering이 된다. 이를 *$(A\_i)\_{i\in I}$의 $f$에 의한 상*이라 부른다. 반대로 임의의 함수 $g:C\rightarrow A$가 주어진다면 $(g^{-1}(A\_i))\_{i\in I}$가 $C$의 covering이 된다. 이를 covering $(A\_i)$의 $f$에 의한 역상이라 부른다.

한편, 집합 $A$의 covering $(A\_i)\_{i\in I}$와 이들 각각을 정의역으로 하고 동일한 target을 갖는 함수들 $f\_i:A\_i\rightarrow B$가 주어진 상황을 생각할 수 있다. 이 경우 우리의 가장 큰 관심사는 각 부분마다 정의된 함수 $f_i$들을 모두 모아, 전체 함수 $f:A\rightarrow B$를 만들수 있느냐는 것이다. 그리고 정확히 이를 위해 정의했던 개념이 있다. ([§함수 (1), 정의 2](/ko/math/set_theory/functions_1#df2))

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins>  $A$가 집합이고 $(A_i)\_{i\in I}$가 $A$의 covering이라 하자. 

1. 만일 $f$, $g$가 $A$를 정의역으로 갖는 함수이고, 모든 $i\in I$에 대하여 $f$, $g$가 $A_i$ 위에서 compatible하다면, $f$와 $g$는 $A$ 전체에서 compatible하다.  
2. 더 일반적으로 family $(A\_i)\_{i\in I}$와 공통된 target $B$를 갖는 함수들의 family $(f\_i)\_{i\in I}$를 생각하자.  

     1. 모든 $i$에 대하여 $f_i$의 정의역이 $A_i$이고,  
     2. 임의의 $i, j\in I$에 대하여 $f_i$와 $f_j$가 $A_i\cap A_j$ 위에서 compatible하다면,

    모든 $f_i$를 확장하는 유일한 함수 $f:A\rightarrow B$가 존재한다. 
</div>

<details class="proof" markdown="1">
<summary>증명</summary>
우선 첫 번째 주장을 보이기 위해 임의의 $x\in A$가 주어졌다고 하자. $(A_i)\_{i\in I}$가 $A$를 덮으므로, 어떤 $i\in I$가 존재하여 $x\in A_i$이다. 그런데 $f$와 $g$는 $A_i$ 위에서 compatible하므로 $f(x)=g(x)$이다. $x$가 임의의 원소이므로 $f$와 $g$는 $A$ 전체에서 compatible하다.

이제 두 번째를 증명하기 위해, $f_i$들의 그래프를 $F_i$라 하자. 우리는 $F=\bigcup\_{i\in I} F_i$가 functional graph임을 보일 것이다. 즉, 임의로 주어진 $x\in \bigcup\_{i\in I} A_i$에 대하여,

> 만일 $(x,y)\in F$이고 $(x,y')\in F$라면 $y=y'$

임을 보여야 한다. $F$는 $F_i$들의 합집합이므로, 위의 전제가 성립한다면 어떤 $i$, $j$에 대하여 $(x,y)\in F_i$이고 $(x,y')\in F_j$이므로 $x\in A_i$, $y\in A_j$이다. 따라서 <phrase>$x\in \operatorname{pr}_1 F_i=A_i$이고 $x\in\operatorname{pr}_1 F_j=A_j$</phrase>에서 $x\in A_i\cap A_j$이고, 집합 $A_i\cap A_j$ 위에서 $f_i$와 $f_j$는 compatible하므로 $y=f_i(x)=f_j(x)=y'$이다. 따라서 $F$는 functional이다.  

이 그래프의 정의역이 $\bigcup\_{i\in I} A_i$임은 자명하고, $f$의 유일성은 첫 번째 부분으로부터 자명하다. 만일 $f\_i$들을 확장하는 또다른 $g$가 존재한다면, 임의의 $i$에 대하여 $f$와 $g$가 모두 $A_i$에서 $f_i$와 compatible할 것이기 때문이다.

</details>

위의 증명과 같이 $(f_i)\_{i\in I}$들이 주어졌을 때, compatible 조건이 필요한 것은 어떠한 $x\in A_i\cap A_j$에 대하여 $f_i(x)\neq f_j(x)$라면 $f$가 최소한 두 개의 값을 가지므로, 함수가 될 수 없기 때문이다. 다음과 같이 애초에 교집합이 공집합이라면 이를 걱정할 필요가 없다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 집합 $A$와 $B$가 *서로소<sub>disjoint</sub>*라는 것은 $A\cap B=\emptyset$인 것이다. 더 일반적으로, $(A_i)\_{i\in I}$가 *쌍마다 서로소<sub>pairwise disjoint</sub>*라는 것은 임의의 $i, j\in I$에 대하여 $i\neq j$라면 $A_i\cap A_j=\emptyset$인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="df4">**정의 4**</ins> 집합 $A$의 *분할<sub>partition</sub>*은 $A$의 쌍마다 서로소인 covering을 뜻한다.

</div>

일반적으로 이 family의 구성원 중 $\emptyset$은 어떠한 역할도 하지 않으므로, 분할이라고 하면 모든 구성원이 공집합이 아님을 전제로 한다. 

## 집합의 합

<div class="proposition" markdown="1">

<ins id="p53">**명제 5**</ins> $(A_i)\_{i\in I}$가 어떤 집합들의 family라 하자. 그럼 어떠한 집합 $S$가 존재하여, 

- $S$는 쌍마다 서로소인 family $(S\_i)\_{i\in I}$들의 합집합이며, 
- 모든 $i\in I$에 대하여 $A_i$에서 $S_i$로의 전단사함수가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
$S_i$를 <phrase>$x\in A_i$를 만족하는 $(x, i)$들로 이루어진 집합</phrase>이라 하자. 그럼 $(S_i)\_{i\in I}$는 쌍마다 서로소이다. 또, 각각의 $i$에 대하여 $x\mapsto (x,i)$는 $A_i$에서 $S_i$로의 전단사함수가 된다. 따라서 $S=\bigcup\_{i\in I} S_i$가 주어진 조건을 만족한다.
</details>

특히 위 명제에서, $A_i$와 $S_i$간의 전단사함수는 ($S$가 $S_i$들의 합집합이므로) $A_i$에서 $S$로의 단사함수가 된다. 대부분의 경우는 이 단사함수는 언급 없이도 자명하게 주어지는 것으로 생각하지만, 필요한 경우에는 이들 단사함수들을 분명하게 명시해주기도 한다.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> 위의 조건을 만족하는 $S$를 family $(A_i)\_{i\in I}$들의 *합<sub>sum</sub>*이라 하며, $\sum\_{i\in I} A_i$로 적는다.

</div>

이 집합을 종종 *분리합집합<sub>disjoint union</sub>*이라 부르고, $\bigsqcup_{i\in I} A_i$으로 적기도 한다. 다음 명제를 보면 이 이름도 꽤나 그럴싸해 보인다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> 쌍마다 서로소인 family $(A_i)\_{i\in I}$를 생각하자. 이들의 합집합을 $A$, 합을 $S$라 하면 $A$와 $S$ 간의 전단사함수가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
$f_i:A_i\rightarrow A_i\times\left\\{i\right\\}$를 $x\mapsto (x, i)$로 정의하자. 이제 $(f_i)\_{i\in I}$를 $\bigcup\_{i\in I} A_i=A$로 확장하면 된다.
</details>

다른 모든 분야에서는 $\bigsqcup A_i$의 표기와, 분리합집합이라는 이름이 더 잘 쓰이지만 집합론을 하는 동안은 **[Bou]**를 따라 [정의 6](#df6)의 표기를 유지하기로 하자. 이에 대한 직관은 나중에 나온다. ([§Cardinal, 정의 6](/ko/math/set_theory/cardinals#df6))

[정의 6](#df6)에서 우리가 언급하지 않은 사실이 있다. 집합들의 family $(A_i)$들의 합 $X$는 유일하지 않다는 것이다. [명제 5](#pp5)의 조건을 만족하는 집합은 무수히 많다. 예를 들어 해당 명제의 증명에서는 $S$를 $(x,i)$들의 집합으로 두었는데, $(i,x)$들의 집합으로 두어도 합의 정의를 만족한다는 것을 알 수 있다. 때문에 엄밀히 말하자면 $A_i$들의 합을 $\sum A_i$로 적는 것은 잘 정의된 표현이 아니다.

우선 다음과 같이 합의 *universal property<sub>보편성질</sub>*를 살펴보자.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Universal property of sum)**</ins> 집합들의 family $(A_i)$와 [명제 5](#pp5)에서 정의한 집합 $S$, 그리고 단사함수들 $\iota_i:A_i\rightarrow S$가 주어졌다 하자. 그럼, 또 다른 어떤 집합 $B$와, $f_i:A_i\rightarrow B$들이 주어질 때마다, 이에 해당하는 유일한 $f:S\rightarrow B$가 존재하여 $f_i=f\circ\iota_i$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선, 이러한 함수 $f$가 (존재한다면) 유일하다는 것을 보이자. 이를 위해서는 임의의 $x\in S$에 대하여, 그 함숫값 $f(x)$가 항상 유일하게 결정된다는 것을 보이면 충분하다. $S$는 쌍마다 서로소인 family $(S_i)$들의 합집합이므로, $x\in S_i$이도록 하는 유일한 $i\in I$가 존재한다. 그럼 $\iota_i:A_i\rightarrow S_i$가 전단사함수이므로, 또 다시 $A_i$의 유일한 원소 $x_i$가 존재하여 $\iota_i(x_i)=x$이도록 할 수 있다. 이제,

$$f(x)=f(\iota_i(x_i))=(f\circ\iota_i)(x_i)=f_i(x_i)$$

이므로, $x$에서의 함숫값 $f(x)$는 반드시 $f_i(x_i)$와 같아야 하고 따라서 $f$는 유일하게 결정된다.

이제 유일성 증명에서 힌트를 얻어, 함수 $f$의 존재성을 보이자. $f(x)$를 위의 식과 같이 $f_i(x_i)$로 <em_ko>정의</em_ko>하고, $f$가 실제로 함수가 된다는 것을 증명하면 된다. 예를 들어, 이렇게 정의하면 $f$는 모든 $S$의 원소에 대해 정의가 될 것이며, 또 하나의 $x$는 위에서 이야기한 것과 같이 오직 하나의 함숫값만을 지정한다.

</details>


많은 경우에 [명제 5](#pp5)의 증명에 등장한 집합 $S$를 $A_i$들의 합이라 정의하지만, 사실 이는 주객이 전도된 정의다. 우리가 많은 분야들에서 $S$를 $A_i$들의 합으로 생각하는 이유는 표기법 상의 편리함 때문이지, $S$라는 집합 자체가 특별한 의미를 가져서가 아니다. 합의 성질은 집합 $S$에서 나오는 것이 아니라, 위의 universal property에서 나온다.

따라서 애초에 다음과 같이 정의를 해 버릴 수도 있다.

<div class="definition" markdown="1">

<ins id="df6-1">**정의 6$'$**</ins> 주어진 집합들의 family $(A_i)$의 *합*은 다음과 같은 조건
 
> 임의의 집합 $B$와 $f_i:A_i\rightarrow B$가 주어질 때마다, 유일한 함수 $f:\sum A_i\rightarrow B$가 존재하여 $f_i=f\circ\iota_i$가 성립한다.

![universal_property_of_sum](/assets/images/Set_theory/Sum_of_sets-1.png){:width="285.9px" class="invert" .align-center}

을 만족하는 집합 $\sum A_i$와 $\iota_i:A_i\rightarrow \sum A_i$들의 모임이다.

</div>

물론 이를 정의로 쓰기 위해서는 universal property를 만족하는 대상이 적어도 하나 존재한다는 것은 보여줘야 한다. 그리고 [정리 8](#thm8)이 정확히 그런 역할을 해 준다. 

우리는 앞서 $\sum A_i$라는 집합이 엄밀한 의미에서는 잘 정의되지 않는다는 것을 언급했다. 하지만 이러한 집합 자체는 잘 정의되지 않더라도, 이러한 집합들이 여럿 주어진다면 이들 사이의 전단사함수가 존재한다. 이런 상황을 unique *up to bijection*과 같이 표현한다. 그리고 이는 앞선 [정의 6$'$](#df6-1)만으로 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="crl9">**따름정리 9**</ins> 집합들의 family $(A_i)$에 대하여, $\sum A_i$는 unique up to bijection이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 개의 합 $S$, $S'$가 주어졌다 하고, $A_i$에서 $S$, $S'$로의 단사함수들을 각각 $\iota_i$, $\iota_i'$라 하자. 우선, 함수 $\iota_i':A_i\rightarrow Y$에 대하여, $S$의 universal property를 적용하면 유일한 $\phi':S\rightarrow S'$가 존재하여 $\iota_i'=\phi'\circ\iota_i$이도록 할 수 있다. 이와 비슷하게, 함수 $\iota_i$들에 $S'$의 universal property를 적용하면, 또 다시 유일한 $\phi:S'\rightarrow S$가 존재하여 $\iota_i=\phi\circ\iota_i'$이도록 할 수 있다. 그럼

$$\iota_i'=\phi'\circ\iota_i=\phi'\circ(\phi\circ\iota_i')=(\phi'\circ\phi)\circ\iota_i'$$

이다. 한편, 함수들 $\iota_i':A_i\rightarrow S'$에 이번에는 $S'$의 universal property를 적용하자. 그럼 어떤 유일한 함수 $\psi:S'\rightarrow S'$가 존재하여 $\iota_i'=\psi\circ\iota_i'$를 만족한다. 이는 당연히 $\psi=\operatorname{id}\_{S'}$에 의해 만족되는 식이므로, 유일성에 의해 이 식을 만족하는 모든 함수 $\psi$들은 $\operatorname{id}\_{S'}$와 같다. 따라서 $\phi'\circ\phi=\operatorname{id}\_{S'}$이고, $\operatorname{id}\_{S'}$는 전단사이므로 $\phi'$는 전사함수, $\phi$는 단사함수이다. ([§함수 (2), 명제 3](/ko/math/set_theory/functions_2#pp3))

마찬가지로, $\phi\circ\phi'=\operatorname{id}\_S$임을 보일 수 있고, 이로 인해 $\phi$는 전사함수, $\phi'$는 단사함수다. 즉, 이들은 각각 전단사함수가 되므로 $S$와 $S'$ 사이의 전단사함수가 존재한다. 

</details>


---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

