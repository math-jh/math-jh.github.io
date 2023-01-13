---

title: "단조함수"
excerpt: "순서집합의 연산과 단조함수"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/monotone_functions
header:
    overlay_image: /assets/images/Math/Set_Theory/Monotone_functions.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2021-08-22
last_modified_at: 2022-11-27
weight: 15

---

## 원순서관계의 restriction

Preorder relation $(R,A,A)$을 생각하고, 임의의 부분집합 $A'\subseteq A$가 주어졌다 하자. 그럼 $R\cap (A'\times A')$로 정의된 관계는 $A'$ 위에 preorder relation을 정의한다. 

<div class="proposition" markdown="1">

<ins id="pp1">**명제 1**</ins> 위의 집합 $R\cap (A'\times A')$는 $A'$ 위에 정의된 preorder relation이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 임의의 $x\in A'$에 대하여, $x$는 $A$의 원소이기도 하므로 $(x,x)\in R$이다. 또, $(x,x)\in A'\times A'$이므로 $(x,x)\in R\cap(A'\times A')$이다.

이제 $(x,y),(y,z)\in R\cap (A'\times A')$이라 가정하자. 그럼 $x,y,z\in A'$이고 $(x,y),(y,z)\in R$이다. $R$은 transitive하므로 $(x,z)\in R$이고, $x,z\in A'$로부터 $(x,z)\in R\cap(A'\times A')$임을 안다.

</details>

직관적으로 생각하여 이 관계는 $\leq\_R$을 $A'$로 제한한 것과 같다. 약간의 표기법의 남용을 통해 이 관계 또한 $\leq\_R$로 적는다.

## 원순서관계의 곱

임의의 index set $I$에 대하여, preorder relation들 $(R\_i,A\_i,A\_i)$이 주어졌다 하자. 그럼 곱집합 $\prod\_{i\in I} A_i$의 임의의 두 원소 $x=(x_i)\_{i\in I}$와 $y=(y_i)_{i\in I}$에 대하여 다음과 같은 관계

$$x\leq y\iff \forall i((i\in I)\implies(x_i\leq_{\tiny R_i} y_i))$$

를 생각할 수 있다. 

<div class="proposition" markdown="1">

<ins id="pp2">**명제 2**</ins> 위의 관계 $\leq$는 $\prod A_i$ 위에 정의된 preorder relation이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $(x\_i)\in \prod A\_i$에 대하여, $x\_i\leq_{\tiny R_i} x\_i$가 모든 $i\in I$에 대해 성립하므로 $(x\_i)\leq (x\_i)$이다.

이제 $(x\_i)\leq (y\_i)$이고 $(y\_i)\leq (z\_i)$라 하자. 그럼 모든 $i\in I$에 대하여,

$$x_i\leq y_i\leq z_i\implies x_i\leq z_i$$

가 성립하므로 $(x\_i)\leq (z\_i)$이다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins>  임의의 집합 $A$에서 $B$로의 함수 $f$는 index set을 $A$로 하여, 각각의 $a\in A$마다 $B$를 곱한 집합 $B^A=\prod_{a\in A}B$의 원소로 볼 수 있다.

이제 집합 $B$ 위에 preorder relation $R$이 정의되었다 하자. 앞선 [명제 2](#pp2)에 의하여 preorder relation들의 곱은 함수들의 집합 $B^A$ 위에 preorder relation을 정의한다. 이를 $\leq$라 적기로 하면, $f\leq g$는 임의의 $x\in A$에 대하여 $f(x)\leq_{\tiny R} g(x)$임을 의미한다. 

</div>

앞선 두 절의 내용은 preorder relation을 모두 order relation으로 바꾸어도 성립한다. 즉 원래 주어진 preorder relation이 antisymmetry를 가져서 order relation이 되었다면, [명제 1](#pp1)과 [명제 2](#pp2)에서 얻어지는 preorder relation 또한 antisymmetry를 만족하고 따라서 order relation이 된다.

이 경우 strict order를 살펴볼 때에는 약간의 주의가 필요하다. 가령 집합 $B$에 order relation $R$이 주어졌다 하고, $R$에 의해 정의되는 strict order를 $S$라 하자. [예시 3](#ex3)을 통해 만들어진 order relation $\leq$로부터 만들어지는 strict order $&lt;$는 다음의 관계

$$f< g\iff\forall x\bigl((x\in A)\implies (f(x)<_{\tiny R}g(x))\bigr)$$

로 정의되는 관계와는 <em_ko>다르다</em_ko>. $f&lt;g$는 <em_ko>하나의</em_ko> $y\in A$에 대해서만 $f(y)<\_{\tiny R} g(y)$이고. 나머지 모든 $x\in A$에 대해서는 $f(x)\leq\_{\tiny R} g(x)$여도 성립한다.

## 단조함수

<ins id="df4">**정의 4**</ins> Preorder $R,R'$가 주어진 집합 $A$와 $A'$를 생각하자. 함수 $f:A\rightarrow A'$가 *증가함수<sub>increasing function</sub>*이라는 것은 $x\leq\_{\tiny R} y\implies f(x)\leq\_{\tiny R'} f(y)$가 항상 성립하는 것이다. 만약 $x\leq\_{\tiny R}y\implies f(y)\leq\_{\tiny R'} f(x)$가 항상 성립한다면, 이 함수는 *감소함수<sub>decreasing function</sub>*라 불린다. 증가함수와 감소함수를 통틀어 *단조함수<sub>monotone function</sub>*라 부른다.
{: .definition}

<ins id="rmk1">**참고**</ins> 임의의 상수함수는 증가함수인 동시에 감소함수이다. 그러나 이 역이 성립하는 것은 아니다. $A$가 하나 이상의 원소를 갖는 집합이라 하고. 이 위에 정의된 order relation $=$를 생각하자. 그럼 $A$에서 $A$로의 항등함수는 증가함수인 동시에 감소함수지만 상수함수는 아니다.
{: .remark}

그리고, $\leq$를 $&lt;$로 바꾸면 다음 정의를 얻는다.

<ins id="df5">**정의 5**</ins> Strict order $S,S'$가 주어진 집합 $A$와 $A'$를 생각하자. 함수 $f:A\rightarrow A'$가 *순증가함수<sub>strictly increasing function</sub>*라는 것은 $x <\_{\tiny S} y\implies f(x) <\_{\tiny S'} f(y)$가 항상 참인 것이고, *순감소함수<sub>strictly decreasing function</sub>*라는 것은 $x <\_{\tiny S} y\implies f(y)<\_{\tiny S'}f(x)$가 항상 성립하는 것이다. 순증가함수, 순감소함수들을 통틀어 *순단조함수<sub>strictly monotone function</sub>*라 한다.
{: .definition}

<div class="remark" markdown="1">

<ins id="rmk2">**참고**</ins> 정의에 의해 단조인 단사함수는 항상 순단조함수다. 그러나 이 역 또한 항상 성립하는 것은 아니다. 예컨대, $\mathbb{N}$ 위에 strict order $\prec$을 다음의 식

$$m\prec n\iff ((m-n\text{ is even}) \wedge (m<n))$$

으로 정의하고, 이 집합을 $A$라 하자. 즉, $A$에서는 짝수는 짝수끼리, 홀수는 홀수끼리 크기 비교가 가능하지만 짝수와 홀수의 크기 비교는 불가능하다. 또, 자연수 집합 $\mathbb{N}$에 일상적인 strict order $&lt;$를 부여한 ordered set을 $B$라 하자. 그럼 $A$에서 $B$로의 함수 $m\mapsto \lfloor m/2\rfloor$은 순증가지만 단사함수는 아니다.
</div>

<ins id="pp6">**명제 6**</ins> $A$, $A'$가 ordered set이고 $u:A\rightarrow A'$, $v:A'\rightarrow A$가 감소함수이며, $v(u(x))\geq x$와 $u(v(x'))\geq x'$이 모든 $x\in A$, $x'\in A'$에 대해 성립한다고 하자. 그럼 $u\circ v\circ u=u$ 이고 $v\circ u\circ v=v$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

주어진 가정과 $u$가 감소함수라는 것에서 자명하다. 즉, $u$는 감소함수이므로, $v(u(x))\geq x$에서 $u(v(u(x)))\leq u(x)$가 모든 $x$에 대해 성립하지만, 가정의 두 번째 부분에서 $u(v(u(x)))\geq u(x)$이 성립한다.

</details>

---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---