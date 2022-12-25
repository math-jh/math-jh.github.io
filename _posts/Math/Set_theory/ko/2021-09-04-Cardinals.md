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
last_modified_at: 2022-11-29
weight: 24

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

그럼

1. 임의의 집합 $A$에 대하여, $\id_A$는 $A$에서 $A$로의 전단사함수이다.
2. 임의의 집합 $A,B$ 사이에 전단사함수 $f:A\rightarrow B$가 존재한다면 그 역함수 $f^{-1}:B\rightarrow A$는 $B$에서 $A$로의 전단사함수이다.
3. 두 전단사함수의 합성 또한 전단사함수이다.

이상에서 동치관계의 정의에서 만족되지 않는 유일한 조건은 위의 관계가 <em_ko>특정 집합 $U$ 위에서</em_ko> reflexive하다는 조건뿐이며, 따라서 전체집합이 존재하지 않는다는 문제만 해결하면 이 관계를 전체집합 위에서 정의된 동치관계라 생각할 수 있다. 

엄밀한 해결책은 아니지만, 지금부터는 이 문제가 해결되었다고 가정하고 이야기를 전개한다. (참고: [Wikipedia, Class](https://en.wikipedia.org/wiki/Class_(set_theory)))

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> 집합 $A$의 equivalence class의 한 representative를 $A$의 *cardinal*이라 부르고, $\card A$로 적는다.

</div>

공집합은 유일하므로, $\card\emptyset$은 정확히 $\emptyset$이다. Cardinal을 다룰 때는 이 집합을 $\mathbf{0}$으로 적는다. 원소 하나짜리 집합들, 예컨대 $\\{a\\}$와 $\\{b\\}$들은 모두 서로 equipotent하다. $\\{(a,b)\\}$가 $\\{a\\}$에서 $\\{b\\}$로의 전단사함수이기 때문이다. 이를 $\mathbf{1}$로 적자. 아직 이들이 자연수가 되는 것은 아니지만, 우리는 곧 cardinal들에 연산들을 주어 자연수처럼 볼 것이다.

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

---
**참고문헌** 

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---
