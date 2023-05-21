---

title: "함수들 사이의 연산"
excerpt: "함수의 역과 합성, 전사함수와 단사함수"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/operation_of_functions

header:
    overlay_image: /assets/images/Math/Set_Theory/Operation_of_functions.png
    overlay_filter: 0.5

sidebar: 
    nav: "set_theory-ko"

date: 2022-11-23
last_modified_at: 2022-11-23

weight: 6

---

함수는 특정한 조건을 만족하는 이항관계이며, 앞서 우리는 이항관계의 합성과 역을 이미 정의한 적이 있다. 함수의 합성과 역이 잘 정의되기 위해서는 이를 이항관계로서 합성하거나, 혹은 이항관계로서 역을 취했을 때 그 결과물이 함수가 되어야 한다.

## 함수의 합성

함수의 합성은 특별하지 않다.

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 함수 $f:A\rightarrow B$와 $g:B\rightarrow C$를 생각하자. 그럼 $g\circ f$는 $A$에서 $C$로의 함수이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $g\circ f$의 정의역이 $A$ 전체임은 자명하다. $f$의 값은 모든 $A$의 원소들에 대해 정의되고, 또 $g$의 값 또한 모든 $B$의 원소, 특히 모든 $f(A)\subseteq B$의 원소에 대해 정의되기 때문이다. 따라서 주어진 명제를 보이기 위해서는

> 어떠한 $x\in A$에 대해서도 $(x,z)$, $(x,z')\in G\circ H$라면 반드시 $z=z'$이다.

를 보이면 충분하다.

$(x,z),(x,z')\in G\circ F$라 가정하자. 그럼 $G\circ F$의 정의에 의하여, $(x,y)\in F$, $(y,z)\in G$이고 $(x,y')\in F$, $(y',z')\in G$이도록 하는 $y,y'$가 각각 존재한다. 그런데 $f$가 함수이므로 $(x,y)\in F$와 $(x,y')\in F$로부터 $y=y'$이다. 이제 두 조건 $(y,z)\in G$와 $(y',z')\in G$, 그리고 $y=y'$인 것과 $g$가 함수인 것으로부터 $z=z'$임을 안다.

</details>

따라서, 함수의 합성은 별다른 것이 아니라 단순히 이항관계의 합성과 같으며, 그 결과로 얻어지는 이항관계가 항상 함수가 된다. 

우리는 앞선 글에서 임의의 집합 $A$에 대하여 $\id_A$가 함수가 됨을 살펴보았고, 또 [§이항관계들 사이의 연산, 명제 5](/ko/math/set_theory/operation_of_binary_relations#pp5)에서 함수의 합성이 결합법칙을 만족함을 보였으므로, 이들 데이터는 카테고리 $\Set$을 이룬다. ([\[범주론\] §카테고리, ⁋정의 1](/ko/math/category_theory/categories#df1))

## 역함수

역함수를 정의하는 것은 조금 더 복잡하다. 이항관계로서 함수 $f$의 역관계 $f^{-1}$을 생각할 수는 있지만 이 관계는 함수가 되지 않을 수도 있다. $f^{-1}$이 언제 함수가 되는지를 말하려면 단사함수, 전사함수, 전단사함수를 먼저 정의해야 한다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 함수 $f:A\rightarrow B$를 생각하자. $f$가 *단사<sub>injective</sub>*라는 것은 $A$의 임의의 두 원소가 $f$에서 다른 함숫값을 갖는 것이다. $f$가 *전사<sub>surjective</sub>*라는 것은 $f(A)=B$인 것이다. 만일 $f$가 단사함수인 동시에 전사함수라면, 이 함수가 *전단사<sub>bijective</sub>*라고 한다.

</div>

이들 용어가 정착된 것은 수학사 전체적으로 보면 얼마 되지 않았고, 그 전까지는

- Injection이라는 용어 대신 *one-to-one*,
- Surjection이라는 용어 대신 *onto*,
- Bijection이라는 용어 대신 *one-to-one and onto*

와 같은 용어들을 사용했으며, 고등학교 때 흔히 사용하던 *일대일함수*, *일대일대응* 등의 한글 용어는 이러한 용어들의 흔적이다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $A\subseteq B$라 하자. $f:A\rightarrow B$를 $x\mapsto x$로 정의하면 이 함수는 단사함수가 된다. 이 함수를 *canonical injection*이라 부른다. 

임의의 함수 $f:A\rightarrow B$와 부분집합 $X\subseteq A$, 그리고 canonical injection $i:X\hookrightarrow A$에 대하여

$$f|_X=f\circ i$$

가 성립한다는 것을 쉽게 확인할 수 있다. 간혹 우변의 식을 $i_\ast f$로 적기도 한다.

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 정의에 의해, $\id_A=(\Delta_A,A,A)$가 전단사임은 자명하다.

</div>

이제 약속한대로 역함수를 정의할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp5">**명제 5**</ins> 함수 $f:A\rightarrow B$에 대하여, $f^{-1}$이 함수인 것과 $f$가 전단사함수인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $f^{-1}$가 전단사라면 이는 전사함수이기도 하므로 그 정의역은 $B$가 된다. 또, $f$는 단사함수이기도 하므로 $f^{-1}$이 함수가 된다.

이제 역으로 $f^{-1}$이 함수라 하자. 그럼 정의에 의해 $\pr\_1 f^{-1}=B$이다. 그런데 [§이항관계들 사이의 연산, ⁋명제 8](/ko/math/set_theory/operation_of_binary_relations#pp8)의 첫 번째 식에 $R\_2=\id\_A$, $R\_1=f^{-1}$을 넣으면 $\pr\_1f^{-1}=f(A)$이므로, $B=f(A)$이고 따라서 $f$는 전사함수다. 

또, $(x,f(x))\in F$와 $(y, f(y))\in F$가 잘 정의된다고 가정하자. 그럼 $(f(x), x)\in F^{-1}$, $(f(y),y)\in F^{-1}$이다. 여기에 더해 만일 $f(x)=f(y)$라면 $f^{-1}$가 함수라는 것으로부터 $x=y$이다. 따라서 $f$는 단사함수이다.

</details>

이렇게 정의된 $f^{-1}$을 $f$의 *역함수*라 부른다. 우리는 $f^{-1}\circ f=\id_A$이고 $f\circ f^{-1}=\id_B$임을 쉽게 확인할 수 있다.

아래 참고는 다음 글에서 retraction, section을 정의할 때 중요한 직관이 된다.

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 두 식 $f^{-1}\circ f=\id_A$이고 $f\circ f^{-1}=\id_B$은 $f$가 전단사함수가 아니라, 전사함수 혹은 단사함수 각각만 되더라도 일부는 참이 된다.  

- $f$가 단사함수라면 $f$는 $A$와 $f(A)\subseteq B$ 사이의 전단사함수이므로 $\tilde{f}^{-1}:f(A)\rightarrow A$가 존재할 것이다. 이제 $\tilde{f}^{-1}\circ f=\id\_A$이다.   
- $f$가 단사함수라면, 임의의 $y\in B$에 대해 항상 어떠한 $x$가 존재하여 $f(x)=y$이다. 이제 $\tilde{f}^{-1}$를 이렇게 결정된 $y$를 $x$에 대응시키는 함수라 하면 $f\circ \tilde{f}^{-1}=\id\_B$가 된다.

</div>

## 함수의 곱

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> *이변수함수*는 정의역이 순서쌍들의 집합인 함수이다.

</div>

$f$가 이변수함수라면 우리는 $(x,y)$에서의 $f$의 값을 표현하기 위해 $f((x,y))$ 대신 $f(x,y)$로 적는다. 이러한 함수의 가장 큰 특징은 우리가 $f$의 행동을 관찰하기 위해 조작할 수 있는 변수가 두 개라는 것이다.  
예를 들어 $f$가 첫 번째 좌표가 변화함에 따라 어떻게 변화하는지를 보기 위해서는 두 번째 좌표를 고정한 후, $f$를 마치 첫 번째 좌표만을 입력받는 함수로 취급할 수 있다.

<div class="definition" markdown="1">

<ins id="df7">**정의 7**</ins> $f:A\rightarrow B$가 이변수함수라 하자. 모든 $y$에 대하여 $A\_y$를 $(x,y)\in A$이도록 하는 모든 $x$들의 집합으로 정의하자. 그럼 $A\_{y\_0}$에서 $B$로의 함수 $x\mapsto f(x,y\_0)$를 $y_0$에서의 $f$의 *partial mapping*이라 부르고, $f(-,y\_0)$로 적는다. 이와 비슷하게 $f(x\_0,-)$ 또한 정의한다.

</div>

임의의 두 함수 $u:A\rightarrow C$와 $v:B\rightarrow D$에 대하여, 우리는 항상 이들을 묶어 $A\times B$에서 $C\times D$로의 이변수 함수로 만들 수 있다. 즉, 

$$z\mapsto (u(\pr_1 z),v(\pr_2z))$$

로 두면 된다. 이 함수를 $u$와 $v$의 *product*라 부르고, $u\times v$로 적는다. 물론 이 함수는 두 함숫값 $u(x)$와 $v(x)$를 곱해서 만들어지는 함수와는 전혀 관련이 없다.

---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---