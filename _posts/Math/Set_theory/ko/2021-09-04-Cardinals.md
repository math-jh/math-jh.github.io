---

title: "기수"
excerpt: "Cardinal number의 정의"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/cardinals
header:
    overlay_image: /assets/images/Set_theory/Cardinals.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-09-04
last_modified_at: 2022-04-14
weight: 17

---

## Review

우선 지난 글에서의 중요한 주제들을 간략하게 정리하고 넘어간다. 우리는 자연수를 간략하게 만들었고, 그 이후에는 ordinal number들을 정의하고 그들의 성질을 살펴봤다. Ordinal number와 크게 관련 없는 토픽은 well-ordering이었는데, 우선 well-ordering은 다음과 같이 정의된다.

<div class="definition" markdown="1">

<ins id="df-3">**정의**</ins> 집합 $A$ 위에서 정의된 totally ordered set $R$이 *well-ordering*이라는 것은 공집합이 아닌 $A$의 임의의 부분집합 $X$가 least element를 갖는 것이다. 

</div>

그리고, 우리는 사실 모든 집합들에 well-order를 줄 수 있다는 것을 증명하였으며, 그 증명은 다음의 *선택공리*에 의존했다. 

**The Axiom of Choice.** 임의의 집합은 choice function을 갖는다.
{: .misc}


<ins id="thm-2">**정리 (Zermelo)**</ins> 임의의 집합 $A$에 well-order를 줄 수 있다.
{: .proposition}

<ins id="thm-1">**정리 (Zorn's lemma)**</ins> 임의의 inductive set은 maximal element를 갖는다.
{: .proposition}

이를 이용한 증명 중, 우리가 이번에 쓸 것은 다음 정리다.

<div class="proposition" markdown="1">

<ins id="pp-0">**명제**</ins> $A,B$가 두 well-ordered set들이라 하자. 그럼 적어도 다음 중 하나가 성립한다.
1. $A$에서 $B$의 segment로의 order isomorphism이 존재하거나,
2. $B$에서 $A$의 segment로의 order isomorphism이 존재한다.

</div>

그리고 마지막으로 우리는 ordinal number를 이용해 집합의 크기를 엄밀하게 정의할 수 있다는 것을 살펴보았다.

이번 글에서는, 집합의 크기를 조금 덜 엄밀한 방법으로 정의하고, 이들의 연산을 정의한다. 

## 기본 정의

어쨌든 시작해보자. 집합의 cardinal이라는 것은 집합의 크기, 즉 원소의 개수의 일반화이다. 그러나 우리는 아직 자연수를 정의하지도 않았기 때문에, 우리는 다른 관점을 택해야 한다. 우리는 어떠한 집합이 얼마나 큰지를 정의할 수는 없어도, 어떤 집합들이 같은 크기를 갖는지는 다음과 같이 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 집합 $A$가 집합 $B$와 *equipotent*하다는 것은 $A$에서 $B$로의 전단사함수가 존재하는 것이다.

</div>

잠시동안만 이 관계를 $\operatorname{Eq}(A,B)$로 적자. 이 관계가 동치관계임을 보이는 것은 어렵지 않다.  

자명하게 이 관계는 reflexive하고 (항등함수), symmetric하며 (역함수), 전단사함수 두 개의 합성은 전단사함수이므로 transitive하기도 하다. 따라서 주어진 집합 $X$에 대하여, 우리는 $X$를 포함하는 equivalence class를 얻고, 이제 이 equivalence class 가운데에서 이를 대표하는 원소를 아무거나 하나 뽑으면 집합의 크기를 정의할 수 있다.[^1]

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 집합 $A$의 equivalence class의 한 representative를 $A$의 *cardinal*이라 부르고, $\operatorname{card} A$로 적는다.

</div>

공집합은 유일하므로, $\operatorname{card}\emptyset$은 정확히 $\emptyset$이다. Cardinal을 다룰 때는 이 집합을 $\mathbf{0}$으로 적는다. 원소 하나짜리 집합들, 예컨대 $\\{a\\}$와 $\\{b\\}$들은 모두 서로 equipotent하다. $\\{(a,b)\\}$가 $\\{a\\}$에서 $\\{b\\}$로의 전단사함수의 그래프이기 때문이다. 이를 $\mathbf{1}$로 적자. 아직 이들이 자연수가 되는 것은 아니지만, 우리는 곧 cardinal들에 연산들을 주어 자연수처럼 볼 것이다.

연산을 정의하기 전에 carinal 간의 대소관계부터 정의하자.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> Cardinal들 간의 관계

> $\mathfrak{a}$는 $\mathfrak{b}$의 부분집합과 equipotent하다.

는 order relation이며, 이를 $\mathfrak{a}\leq\mathfrak{b}$로 적는다.

</div>

물론 이 관계가 실제로 order relation이 됨을 확인하지 않았다. 하지만 자명하지 않은 부분은 antisymmetry 뿐이다.

<div class="proposition" markdown="1">

<ins id="lem4">**보조정리 4 (Cantor-Bernstein)**</ins> 위의 관계 $\leq$은 antisymmetric하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 cardinal $\mathfrak{a}$와 $\mathfrak{b}$에 대해 $\mathfrak{a}\leq\mathfrak{b}$이고 $\mathfrak{b}\leq\mathfrak{a}$라 가정하자.  

만일 $\mathfrak{a}$에서 $\mathfrak{b}$의 부분집합으로의 전단사함수를 $i$라 하면 $i(\mathfrak{a})\subset\mathfrak{b}$이고 $\mathfrak{a}$와 $i(\mathfrak{a})$은 equipotent하다. 따라서 $i(\mathfrak{a})$와 $\mathfrak{b}$ 사이의 전단사함수가 존재함을 보이면 충분하다.  
$\mathfrak{b}\leq\mathfrak{a}$이므로, $\mathfrak{b}$에서 $\mathfrak{a}$의 부분집합으로의 전단사함수가 존재하고, 이는 $\mathfrak{b}$에서 $\mathfrak{a}$로의 단사함수로 볼 수 있다. 힌퍈. $\mathfrak{a}$는 $i(\mathfrak{a})$와 equipotent하므로, 이 둘 사이의 전단사함수를 앞선 단사함수와 합성하면 $\mathfrak{b}$에서 $i(\mathfrak{a})$로의 단사함수를 얻는다. 이를 $f$라 하자. 이제 $C_0=\mathfrak{b}\setminus i(\mathfrak{a})$라 하고, 귀납적으로 $C\_{n+1}=f(C_n)$으로 정의하고 $C=\bigcup C_n$이라 하자. 우리는 $h:\mathfrak{b}\rightarrow i(\mathfrak{a})$를 다음의 식 

$$h(x)=\begin{cases} f(x)&x\in C\\ x&x\not\in C\end{cases}$$

으로 정의하고, $\mathfrak{b}$에서 $i(\mathfrak{a})$로의 전단사함수임을 보일 것이다.

우선 $h$는 $\mathfrak{b}$에서 $i(\mathfrak{a})$로의 함수다. $h$가 잘 정의됨은 자명하고, 이 함수의 target이 $i(\mathfrak{a})$임만 보이면 된다. 만일 $x\in C$라면 $h(x)=f(x)\in i(\mathfrak{a})$이므로 자명하고, $x\not\in C$라 하면 $x\not\in C_0$이므로 $x\not\in\mathfrak{b}\setminus i(\mathfrak{a})$이다. 따라서 이 경우에도 $x\in i(\mathfrak{a})$이다.

또, $h$는 단사함수다. 만일 $h(x)=h(y)$라 한다면, $x,y\in C$인 경우는 $f(x)=f(y)$가 되고, 그럼 $f$가 단사이므로 $x=y$이다. 그리고 $x,y\not\in C$인 경우는 자명하게 $x=y$가 된다.  
자명하지 않은 경우는 하나가 $C$의 원소이고 다른 하나는 $C$의 원소가 아닐 때이다. $x\in C$라 하고 $y\not\in C$라 하자. 그럼 어떤 $n$에 대하여 $x\in C_n$이고, 특히 $h(x)=f(x)\in C\_{n+1}\subseteq C$이므로 $h(x)\in C$이다. 한편 $h(y)=y$인데, 가정에 의해 $y\not\in C$이므로 $h(x)=h(y)$라는 가정에 모순이다. 따라서 $x=y$가 항상 성립하고 $h$는 단사함수이다.

마지막으로 $h$가 전사함수임을 보이자. 임의의 $y\in i(\mathfrak{a})$에 대하여, $y\in C$이거나 $y\not\in C$이다. 만일 $y\not\in C$라면 $h$의 정의에 의해 $h(y)=y$이다. 만일 $y\in C$라면, 어떤 $n\geq 1$에 대하여 $y\in C\_{n}$이다. ($y\in C_0=\mathfrak{b}\setminus i(\mathfrak{a})$는 불가능하므로) 따라서 $y\in f(C\_{n-1})$이 되어 $y=f(x)$인 $x\in C\_{n-1}$이 존재한다. 이 $x$는 $C$의 원소이기도 하므로, $h(x)=f(x)=y$이고, 따라서 $h$는 전사함수다.

</details>

뿐만 아니라, cardinal들의 집합은 well-ordered set이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> Cardinal들을 모아둔 임의의 집합 $A$는 least element를 갖는다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

집합 $A=\bigcup_{\mathfrak{a}\in E}\mathfrak{a}$를 생각하자. 그럼 임의의 cardinal $\mathfrak{a}\in E$는 $A$의 부분집합이다.

Well-ordering principle에 의하여 이 집합 위에 well-order가 존재한다. 이를 $\leq$라 하자. 또, $A$의 임의의 부분집합은 $A$의 segment와 equipotent하다 (Review의 [명제](#pp0)). 따라서 임의의 cardinal $\mathfrak{a}$에 대하여, 이와 equipotent한 $A$의 segment들의 집합은 공집합이 아니며, 따라서 $A^\*$의 well-orderedness에 의하여 least element가 존재한다. 이 원소를 $\varphi(\mathfrak{a})$라 하자.  
만일 우리가 $\mathfrak{a}\leq\mathfrak{b}$가 $\varphi(\mathfrak{a})\subset\varphi(\mathfrak{b})$와 동치임을 보인다면, $A$의 well-orderedness로부터 증명이 완료될 것이다. 

우선 나중의 조건이 첫번째 조건을 imply하는 것은 자명하다. 반대로 만일 $\mathfrak{a}\leq\mathfrak{b}$라면, 즉 $\mathfrak{a}$가 $\mathfrak{b}=\varphi(\mathfrak{b})$ (등호는 cardinal로써 성립) 의 부분집합과 equipotent하다고 가정하자. 만일 $\varphi(\mathfrak{b})\subset\varphi(\mathfrak{a})$이고 $\varphi(\mathfrak{a})\neq\varphi(\mathfrak{b})$라면, $\varphi(\mathfrak{b})$의 어떤 segment가 존재하여 $\mathfrak{a}$와 equipotent한 segment를 가질 것이고, 이는 $\varphi(\mathfrak{b})$의 정의에 모순이므로 두 조건은 동치이다.

</details>

## Cardinal 사이의 연산

이제 약속한 대로 cardinal들 간의 연산을 정의하자.

<div class="definition" markdown="1">

<ins id="df6">**정의 6**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family라 하자. 집합 $\mathfrak{a}\_i$들의 곱 (resp. 합)의 cardinal을 이들의 *cardinal product*(resp. *cardinal sum*)이라 부르고 $\prod\_{i\in I}\mathfrak{a}\_i$ (resp. $\sum\_{i\in I}\mathfrak{a}_i$)로 적는다.

</div>

우리가 처음 집합의 합을 정의할 때, 굳이 분리합집합이라는 직관적인 이름을 놔두고 합이라는 용어를 쓴 이유가 여기에 있다.

우선, 위 정의들은 잘 정의되어있다. 만일 $A_i$와 $\mathfrak{a}\_i$가 equipotent하다면, $\prod\_{i\in I} A_i$와 $\prod\_{i\in I}\mathfrak{a}\_i$ 사이에도 bijection이 존재하기 때문이다. 이 연산들을 가지고 있다면 합과 곱의 성질들이 다음과 같이 cardinal간의 연산의 성질로 바뀌게 된다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family이고, $f$가 $K$에서 $I$로의 bijection이라 하자. 그럼 

$$\sum_{k\in K}\mathfrak{a}_{f(k)}=\sum_{i\in I}\mathfrak{a}_i,\quad \prod_{k\in K}\mathfrak{a}_{f(k)}=\prod_{i\in I}\mathfrak{a}_i$$ 

이다. 또, 만일 $(J_l)\_{l\in L}$가 $I$의 partition이라면 

$$\sum_{i\in I}\mathfrak{a}_{i}=\sum_{l\in L}\sum_{i\in J_l}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_{i}=\prod_{l\in L}\prod_{i\in J_l}\mathfrak{a}_i$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§집합의 합, 명제 7](/ko/math/set_theory/sum_of_sets#pp7)에 의하여 우리는 cardinal들의 합을 mutually disjoint family의 합집합으로 취급할 수 있다. 이제, 첫 번째 식들은 각각 [§합집합과 교집합, 명제 4](/ko/math/set_theory/union_and_intersection#pp4), [§집합의 곱, 명제 5](/ko/math/set_theory/product_of_sets#pp5)의 결과들이며, 두 번째 식들은 [§합집합과 교집합, 명제 5](/ko/math/set_theory/union_and_intersection#pp5)와 [§집합의 곱, 명제 8](/ko/math/set_theory/product_of_sets#pp8)의 결과들이다.

</details>

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family이고, $J$ (resp. $K$)가 $I$의 부분집합 중 다음의 식 $\mathfrak{a}\_i=\mathbf{0}$ for all $i\not\in J$ (resp. $\mathfrak{a}\_i=\mathbf{1}$ for all $i\not\in K$)을 만족하는 부분집합이라 하자. 그럼 

$$\sum_{i\in I}\mathfrak{a}_i=\sum_{i\in J}\mathfrak{a}_i,\quad \prod_{i\in I}\mathfrak{a}_i=\prod_{i\in K}\mathfrak{a}_i$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

공집합과 합집합을 하는 것과, 원소 하나짜리 집합과 곱을 하는 것은 cadrinal에 영향을 미치지 않는다. ($x\mapsto (x,i)$가 $A$에서 $A\times\{i\}$로의 bijection을 정의한다)

</details>

그리고, 이렇게 자명한 결과들 외에도, 곱과 합집합 사이의 분배법칙 ([§집합의 곱, 명제 12](/ko/math/set_theory/product_of_sets#pp12))를 이용하면 다음의 명제를 얻는다. 

<div class="proposition" markdown="1">

<ins id="pp9">**명제 9**</ins> Cardinal들의 double-index가 주어진 family $((\mathfrak{a}\_{j,k})\_{j\in J_k})\_{k\in K}$에 대하여, $I=\prod\_{k\in K}J_k$라 하면 

$$\prod_{k\in K}\left(\sum_{j\in J_k}\mathfrak{a}_{j,k}\right)=\sum_{f\in I}\left(\prod_{k\in K}\mathfrak{a}_{k, f(k)}\right)$$

가 성립한다.
</div>

특별히, 위의 명제들을 유한한 경우에만 생각한다면 

- 두 개의 집합 $A$, $B$의 합집합을 하는 순서는 상관이 없으므로 $\mathfrak{a}+\mathfrak{b}=\mathfrak{b}+\mathfrak{a}$, 그리고 $A\times B$와 $B\times A$ 사이의 자연스러운 전단사함수가 존재하므로 $\mathfrak{a}\mathfrak{b}=\mathfrak{b}\mathfrak{a}$.
- 집합의 합과 곱의 결합법칙에 의하여, $\mathfrak{a}+(\mathfrak{b}+\mathfrak{c})=(\mathfrak{a}+\mathfrak{b})+\mathfrak{c}$이고 $\mathfrak{a}(\mathfrak{b}\mathfrak{c})=(\mathfrak{a}\mathfrak{b})\mathfrak{c}$
- 마지막으로, 분배법칙을 유한한 경우에 다시 쓰면 $\mathfrak{a}(\mathfrak{b}+\mathfrak{c})=\mathfrak{a}\mathfrak{c}+\mathfrak{a}\mathfrak{b}$.

등의 결과를 얻는다. 한편, 임의의 집합은 singleton들의 합으로 쓰여질 수 있으므로 (즉 $B=\bigcup\_{x\in B}\\{x\\}$가 항상 성립하므로) $I$가 cardinal $\mathfrak{b}$를 갖는 집합이라면

$$\mathfrak{b}=\sum_{i\in I} \mathfrak{c}_i,\qquad \mathfrak{c}_i=1\text{ for all $i\in I$}$$

을 얻고, 양 변에 $\mathfrak{a}$를 곱하여 앞선 [명제 9](#pp9)를 적용하면

$$\mathfrak{a}\mathfrak{b}=\mathfrak{a}\left(\sum_{i\in I}\mathfrak{c}_i\right)=\sum_{i\in I}\mathfrak{a}\mathfrak{c}_i=\sum_{i\in I}\mathfrak{a}$$

을 얻는다. 

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins> $(\mathfrak{a}\_i)\_{i\in I}$가 cardinal들의 family라 하자. 그럼 $\prod\_{i\in I}\mathfrak{a}\_i\neq \mathbf{0}$인 것은 모든 $i\in I$에 대하여 $\mathfrak{a}_i\neq \mathbf{0}$인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[§순서쌍, 명제7](/ko/math/set_theory/ordered_pair#pp10)의 임의의 product로의 확장. 증명도 동일하게 하면 된다.

</details>

<div class="proposition" markdown="1">

<ins id="pp11">**명제 11**</ins> 만일 $\mathfrak{a}$와 $\mathfrak{b}$가 $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$를 만족하는 cardinal들이라면, $\mathfrak{a}=\mathfrak{b}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$X$가 cardinal $\mathfrak{a}+\mathbf{1}=\mathfrak{b}+\mathbf{1}$짜리 집합이라 하자. 그럼 집합 $X$의 cardinal $\mathfrak{a}$와 $\mathfrak{b}$짜리 부분집합이 존재하여, $X\setminus A$와 $X\setminus B$가 singleton이다. $X\setminus A=\{a\}$, $X\setminus B=\{b\}$라 하고, $A$에서 $B$로의 bijection을 

$$f(x)=\begin{cases}a&\text{if }x=b\\ x&\text{otherwise}\end{cases}$$ 

로 정의하면 된다.

</details>

우리는 심지어 cardinal들 간의 지수관계까지 정의할 수 있다. 함수들의 집합 $B^A$를 이용하면 된다.

<div class="definition" markdown="1">

<ins id="df12">**정의 12**</ins> $\mathfrak{a}$와 $\mathfrak{b}$가 cardinal이라 하자. $\mathfrak{b}$에서 $\mathfrak{a}$로의 함수들의 집합의 cardinal를 $\mathfrak{b}^\mathfrak{a}$로 적는다.

</div>

물론 엄밀히 말하자면 $\mathfrak{b}^\mathfrak{a}$의 equivalence class의 representative는 위의 함수들의 집합과 다를 수도 있으므로 약간의 abuse of notation이 있지만[^2] 문맥상 명확하므로 이렇게 쓰기로 한다.

<div class="proposition" markdown="1">

<ins id="pp13">**명제 13**</ins> $\mathfrak{a}$와 $\mathfrak{b}$가 cardinal이고 $I$가 $\operatorname{card} I=\mathfrak{b}$를 만족하는 집합이라 하자. 만일 모든 $i\in I$에 대하여 $\mathfrak{a}\_i=\mathfrak{a}$라면 $\mathfrak{a}^\mathfrak{b}=\prod_{i\in I}\mathfrak{a}_i$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$B^A$와 $\operatorname{Fun}(A,B)$ 간의 bijection이 존재하므로 자명하다.

</details>

Cardinal $\mathbf{0}$과 $\mathbf{1}$에 대한 성질들, 예컨대 $\mathfrak{a}^\mathbf{0}=\mathbf{1}$, $\mathfrak{a}^\mathbf{1}=\mathfrak{a}$, $\mathbf{1}^\mathfrak{a}=\mathbf{1}$, $\mathbf{0}^\mathfrak{a}=\mathbf{0}$ 등등은 쉽게 증명할 수 있다. 여기에서 가장 중요한 정리들 중 하나는 다음의 정리이다.

<div class="proposition" markdown="1">

<ins id="pp14">**명제 14**</ins> $A$가 집합이고 $\mathfrak{a}$가 그 cardinal이라 하자. 그럼 $\mathcal{P}(A)$의 cardinal는 $\mathbf{2}^\mathfrak{a}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbf{2}=\\{\alpha, \beta\\}$가 cardinal이라 하자. 임의의 $X\in\mathcal{P}(A)$에 대하여, 만약 $x\in X$라면 $x\mapsto\alpha$이고, 그렇지 않을 때에는 $x\mapsto\beta$인 함수 $f_X:A\rightarrow \mathbf{2}$가 존재한다. 반대로 임의의 함수 $f:A\rightarrow \mathbf{2}$에 대하여, $f^{-1}(\alpha)$가 $\mathcal{P}(A)$의 원소를 하나 지정한다.

</details>

다음은 Cantor의 유명한 정리. 

<div class="proposition" markdown="1">

<ins id="pp15">**명제 15 (Cantor)**</ins> 임의의 cardinal $\mathfrak{a}$에 대하여 $\mathbf{2}^\mathfrak{a}>\mathfrak{a}$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$x\mapsto \\{x\\}$가 $\mathfrak{a}$에서 멱집합으로의 단사함수이이므로, $\mathfrak{a}\leq \mathbf{2}^\mathfrak{a}$임은 자명하다. 따라서 $\mathfrak{a}\neq\mathbf{2}^\mathfrak{a}$임만 보이자. 즉, 임의의 함수 $f:\mathfrak{a}\rightarrow\mathcal{P}(\mathfrak{a})$에 대하여, $\mathfrak{a}$의 상 밖에 항상 어떤 원소가 존재한다는 걸 보이면 된다.

$X$가 $x\not\in f(x)$를 만족하는 모든 $x\in\mathfrak{a}$들의 집합이라 하자. 만일 $x\in X$라면, $x\not\in f(x)$이고 따라서 $f(x)\neq X$이며, 반대로 $x\not\in X$라면 $x\in f(x)$이므로 다시 $f(x)\neq X$이다. 따라서 $X\not\in f(\mathfrak{a})$이므로 증명이 완료되었다. 

</details>

만약 $\mathfrak{a}$가 유한집합이라면, $\mathfrak{a}$와 $\mathbf{2}^\mathfrak{a}$ 사이에는 항상 어떤 cardinal이 존재한다. 그런데 무한대인 경우에는 이것이 그렇게 자명하지 않다. 예를 들어, 자연수집합 $\mathbb{N}$의 크기보다, $\mathbb{N}$의 멱집합의 크기가 더 큰 것은 위의 명제에 의해 자명하지만 그 둘 사이에 어떠한 cardinal이 있을것인지는 쉽게 예측할 수 없다.

더 엄밀하게 쓰자면, 우리는 $\aleph_0,\aleph_1,\ldots$를 initial ordinal들로 정의했었다. 만일, 다음의 식

$$\beth_0=\aleph_0,\quad \beth_{\alpha+1}=\mathbf{2}^{\beth_\alpha}$$

으로 새로운 ordinal들의 열을 만든다면, $\beth_1$은 $\beth_0=\aleph_0$보다 확실하게 크므로, $\aleph$의 정의에 의해 $\aleph_1$보다 크거나 같다. 즉 $\aleph_1\leq \beth_1$이다. Cantor는 실수집합 $\mathbb{R}$의 크기가 $\beth_1$과 같다는 것을 증명하고는, 사실 $\aleph_1=\beth_1$이라는 *연속체 가설* (*continuum hypothesis*)을 제안했다. 이 가설이 맞다면, 실수는 자연수 바로 다음 크기를 갖는 집합이 된다. 더 일반적으로, $\aleph_\alpha=\beth_\alpha$가 성립한다는 것이 일반화된 연속체 가설이다. 

이 가설은 제안된 이후 미해결 문제로 남아있다가, Gödel과 Cohen에 의해 이 가설은 ZFC 공리계 상에서 증명도, 반증도 하지 못한다는 것이 증명되었다. 괴델이 비교적 일찍 ZFC 공리계 상에서 CH는 반증이 불가능하다라는 것을 증명하였으며, 이후 Cohen이 ZFC 공리계 상에서 CH는 증명이 불가능하다는 것을 증명했다.   


---
**참고문헌** 

- [Bou13] N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: 이 부분이 이전 글에서 언급했던 <em_ko>엄밀하지 않은 부분</em_ko>.
[^2]: 사실 이는 sum과 product에서도 마찬가지다.
