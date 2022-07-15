---

title: "순서관계의 정의"
excerpt: "순서관계의 정의와 성질들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/order_relations_1
header:
    overlay_image: /assets/images/Set_theory/Order_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-22
last_modified_at: 2022-04-04
weight: 10

---

## 순서관계

Binary relation을 처음 정의할 때 언급했던 세 가지 종류의 중요한 relation들, 즉 function, equivalence relation, order relation 중 이제 order relation만이 남았다. Order relation라는 것은 원소들간의 대소비교를 통해 크기를 정해주는 것인데, 예를 들어 자연수 집합에서 정의된 $\leq$와 같은 것이 그 예시다. 이를 위해서는 먼저 다음을 정의해야 한다.

<div class="definition" markdown="1">
<ins id="df1">**정의 1**</ins> Relation $R$이 *anti-symmetric<sub>반대칭적</sub>*이라는 것은 

> $x\mathrel{R}y$이고 $y\mathrel{R}x$이면 $x=y$

가 항상 성립하는 것이다.
</div>

그럼 order relation은 다음과 같이 정의된다. 

<ins id="df2">**정의 2**</ins>  Relation $R$이 *order relation<sub>순서관계</sub>*이라는 것은 $R$이 reflexive, transitive, anti-symmetric한 것이다.
{: .definition}

만일 $x\mathrel{R}x$이면 $x\in E$일 경우, equivalence relation 때와 마찬가지로 이 relation이 집합 $E$ 위에서 정의되었다고 한다. 이 때 correspondence $\Gamma=(R, E, E)$이 잘 정의되며, 우리는 $E$가 <em_ko>$\Gamma$에 의해 ordering이 부여되었다</em_ko>고 하고, 종종 $E$를 *ordered set<sub>순서집합</sub>*이라고 부른다. 

<ins id="ex3">**예시 3**</ins> Relation <box>$x=y$</box>는 order relation이다. Relation <box>$x\subset y$</box> 또한 order relation이다. ([§순서쌍, 명제 2](/ko/math/set_theory/ordered_pair#pp2)과 같은 글의 [명제 3](/ko/math/set_theory/ordered_pair#pp3) 참고)
{: .example}

Ordered set은 $&lt;$라는 relation이 추가적으로 정의된 집합이므로, ordered set들 간의 함수를 생각할 때에는 (단순한 함수가 아니라) 이 relation 또한 보존하는 함수를 생각하는 것이 올바르다. 

<ins id="df4">**정의 4**</ins> 만일 두 order relation $(R, E, E)$과 $(R', E',E')$에 대해 어떠한 bijection $f$가 존재하여 $x\mathrel{R}y$와 $f(x)\mathrel{R'}f(y)$가 동치라면 $f$를 *order isomorphism*이라 부른다. 
{: .definition}

앞으로 ordered set들 사이에서 isomorphism이라 하면 항상 order isomorphism을 뜻하는 것으로 이해한다. 우리는 equivalence relation을 correspondence의 언어로 바꾸어 썼었는데 ([§동치관계, 명제 3](/ko/math/set_theory/equivalence_relations#pp3)), 다음은 이에 대한 analogue.

<div class="proposition" markdown="1">

<ins id="df5">**명제 5**</ins> $\Gamma=(G, E, E)$가 order relation인 것은 $G$가 다음의 조건을 만족하는 것이 동치이다.

- $G\circ G=G$이고,
- $G\cap G^{-1}=\Delta_E$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $\Gamma$가 order relation이라 가정하자. 그럼 transitivity에 의하여 $G\circ G\subset G$이고, 반대로 만일 $(x,y)\in G$라면 $(x,x)\in G$이고 $(x,y)\in G$이므로 $(x,y)\in G\circ G$가 되어 첫 번째 조건이 만족된다. 두 번째 조건은 antisymmetry. 역으로 이들 조건이 만족되면 $\Gamma$가 order relation이 되는 것 또한 쉽게 보일 수 있다.
</details>

## 원순서관계

우선 다음 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 함수 $f:X\rightarrow Y$를 생각하고, $Y$ 위에 order relation $\leq$가 정의되었다고 하자. 그럼 우리는 함수로부터 equivalence relation을 유도하듯 ([§동치관계, 정의 5](/ko/math/set_theory/equivalence_relations#df5)), $X$ 위에 다음과 같이 정의된 relation $\preceq$를 정의할 수 있다.

$$x\preceq y\iff f(x)\leq f(y)$$

정의로부터 $\preceq$는 reflexive하고 transitive하다. 하지만 일반적으로 $f$가 injection이 아닌 한 $\preceq$는 antisymmetry을 만족하지 않는다.
</div>

따라서 antisymmetry 조건을 빼서 다음과 같이 정의한다.

<ins id="df7">**정의 7**</ins> Reflexive하고 transitive한 relation $R$을 *preorder relation<sub>원순서관계</sub>*라 부른다.
{: .definition}

Preorder relation의 성질을 알기 위해 우리는 order relation의 성질이지만 preorder의 성질은 아닌 antisymmetry를 좀 더 살펴봐야 한다.  
만일 relation $R$이 order relation이었다면, antisymmetry는 $(x\mathrel{R}y)\wedge(y\mathrel{R}x)\implies x=y$를 뜻한다. Preorder relation에 대해서는 이것이 성립하지 않는다는 것을 살펴보았지만, 그 대신 Preorder relation에 대해서는 <em_ko>일반화된 등호</em_ko>, 즉 equivalence relation이 똑같은 성질을 준다. 

<div class="proposition" markdown="1">
<ins id="pp8">**명제 8**</ins>  $R$이 preorder relation이라 하자. 그럼 relation <box>$x\mathrel{R}y$이고 $y\mathrel{R}x$</box>은 equivalence relation이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
위의 relation을 $S$라 하자. 우리는 $S$가 reflexive, symmetric, transitive함을 보여야 한다. 우선 이 relation이 reflexive함은 자명하다. $R$이 preorder이므로, 임의의 $x$에 대해 $x\mathrel{R}x$가 항상 성립하기 때문이다. 한편, 임의의 $x$, $y$에 대하여 $x\mathrel{S}y$라 하자. 그럼 

$$x\mathrel{S}y\leftrightarrow(x\mathrel{R}y)\wedge(y\mathrel{R}x)\leftrightarrow(y\mathrel{R}x)\wedge(x\mathrel{R}y)\leftrightarrow y\mathrel{S}x$$

이므로 $S$는 symmetric하다. 마지막으로 만일 $x\mathrel{S}y$, $y\mathrel{S}z$라면

$$\begin{aligned}  (x\mathrel{S}y)\wedge(y\mathrel{S}z)&\iff((x\mathrel{R}y)\wedge(y\mathrel{R}x))\wedge((y\mathrel{R}z)\wedge(zRy))\\
  &\iff(x\mathrel{R}y)\wedge(y\mathrel{R}x)\wedge(y\mathrel{R}z)\wedge(z\mathrel{R}y)\\
  &\iff(x\mathrel{R}y)\wedge(y\mathrel{R}z)\wedge(z\mathrel{R}y)\wedge(y\mathrel{R}x)\\
  &\iff((x\mathrel{R}y)\wedge(y\mathrel{R}z))\wedge((z\mathrel{R}y)\wedge(y\mathrel{R}x))\\
  &\iff(x\mathrel{R}z)\wedge(z\mathrel{R}x)\\
  &\iff x\mathrel{S}z
\end{aligned}$$

이므로 $S$는 transitive하고, 따라서 $S$는 equivalence relation이 된다.
</details>

앞으로 order, preorder relation를 표현하기 위하여 익숙한 표현인 $\leq$를 사용하기로 한다. 

## Strict order

주어진 order relation $\leq$에 대하여, $&lt;$을 <box>$x\leq y$이고 $x\neq y$</box>로 정의된 relation으로 정의하자. 이 때 $&lt;$는 antisymmetry를 만족하지 않으므로 order relation이 될 수는 없고, 또 reflexive하지도 않으므로 preorder 또한 될 수 없다. 대신 다음을 정의하자.

<ins id="df9">**정의 9**</ins>  Relation $R$이 *asymmetric<sub>비대칭적</sub>*이라는 것은 $x\mathrel{R}y$이면 $y\not \mathrel{R}x$인 것이다. Asymmetric, transitive relation을 *strict order*라 부른다.
{: .definition}

그럼 다음이 성립한다.

<ins id="pp10">**명제 10**</ins>  $R$이 order relation이라 하자. 그럼 새로운 relation <box>$x\mathrel{R}y$이고 $x\neq y$</box>는 strict order이다.  
반대로 $S$가 strict order라 하자. 그럼 새로운 relation <box>$x\mathrel{S}y$이거나 $x=y$</box>는 order relation이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>
우선 $R$이 orader relation이라 하고, 새로운 relation $S$를 <box>$x\mathrel{R}y$이고 $x\neq y$</box>으로 정의하자. Asymmetry를 보이기 위해 우리는 $x\mathrel{S}y$와 $y\mathrel{S}x$가 동시에 성립할 수 없음을 보여야 한다. $(x\mathrel{S}y)\wedge(y\mathrel{S}x)$를 풀어 쓰면 다음과 같다.
  
$$((x\mathrel{R}y)\wedge(x\neq y))\wedge((y\mathrel{R}x)\wedge(y\neq x))$$

그런데 이는 다음과 같이 쓸 수 있다.

$$((x\mathrel{R}y)\wedge(y\mathrel{R}x))\wedge(x\neq y)$$

이는 $R$의 antisymmetry에 의하여 $(x=y)\wedge(x\neq y)$이고, 이는 항상 거짓이므로 $x\mathrel{S} y$이면 $y\not\mathrel{S}x$이다.

반대로 $S$가 strict order라 하고, 새로운 relation $R$을 <box>$x\mathrel{S}y$이거나 $x=y$</box>로 정의하자. 우선 $x=x$이므로, 뒤쪽 조건에 걸려 $x\mathrel{R}x$이다. Antisymmetry를 보이기 위해, $x\mathrel{R}y$와 $y\mathrel{R}x$가 성립한다고 가정하자. 그럼 

$$\begin{aligned}  
(x\mathrel{R}y)\wedge(y\mathrel{R}x)&\iff((x\mathrel{S}y)\vee(x=y))\wedge((y\mathrel{S}x)\vee(y=x))\\
   &\iff ((x\mathrel{S}y)\wedge(y\mathrel{S}x))\vee(x=y)
\end{aligned}$$

이다. Asymmetry에 의하여 $(x\mathrel{S}y)\wedge(y\mathrel{S}x)$는 불가능하므로, $(x\mathrel{R}y)\wedge(y\mathrel{R}x)$가 성립한다면 반드시 $x=y$가 성립한다. 마지막으로 transitivity을 보이기 위해 $x\mathrel{R}y$이고 $y\mathrel{R}z$라 하자. 그럼

$$\begin{aligned}
  (x\mathrel{R}y)\wedge(y\mathrel{R}z)&\iff ((x\mathrel{S}y)\vee(x=y))\wedge((y\mathrel{S}z)\vee(y=z))\\
  &\iff ((x\mathrel{S}y)\wedge((y\mathrel{S}z)\vee(y=z)))\vee((x=y)\wedge((y\mathrel{S}z)\vee(y=z)))\\
  &\iff ((x\mathrel{S}y)\wedge(y\mathrel{S}z))\vee((x\mathrel{S}y)\wedge(y=z))\\
  &\phantom{asdfghjkl}\vee((x=y)\wedge (y\mathrel{S}z))\vee((x=y)\wedge(y=z))\\
  &\implies (x\mathrel{S}z)\vee(x\mathrel{S}z)\vee(x\mathrel{S}z)\vee(x=y=z)\\
  &\iff x\mathrel{R}z
\end{aligned}$$

이므로 $R$은 transitive하다. 따라서 $R$은 order relation이 된다.
</details>

<ins id="rmk1">**참고**</ins> 일반적으로 $x\not\leq y$라 하여 $x>y$인 것은 아니다. $E=\left\\{a,b\right\\}$라 하고, $\mathcal{P}(E)$ 위에 정의된 relation $\leq$를 부분집합들 간의 포함관계로 정의하자. 그럼 이는 자명하게 order relation이 된다. 이 때, $\left\\{a\right\\}\not\leq \left\\{b\right\\}$이지만 $\left\\{a\right\\}>\left\\{b\right\\}$ 또한 성립하지 않는다.
{: .remark}

어쨌든 strict ordering이 주어진 집합 또한 마찬가지로 ordered set이라 부른다.

## 원순서관계의 product

집합 $E$가 (pre-)order relation $\Gamma$에 의해 ordering이 주어졌다고 하고, $G$를 $\Gamma$의 그래프라 하자. 그럼 $A\subset E$에 대하여, 그래프 $G\cap (A\times A)$로 정의된 relation은 (pre-)order가 된다. 약간의 abuse of notation을 통해, 이렇게 정의된 relation (즉, $x\leq y$이고 $x$, $y\in A$) 또한 마찬가지로 $x\leq y$로 적는다. 이 relation을 $\leq$에 의해 유도되었다고 말한다.

한편 각각이 $\Gamma_i$로 (pre-)order가 주어진 family $(E_i)\_{i\in I}$를 생각하고, 이 때 $G_i$를 $\Gamma_i$의 그래프라 하자. 그럼 우리는 product set $\prod\_{i\in I} E_i$ 위에서, 임의의 $x=(x_i)\_{i\in I}$와 $(y_i)_{i\in I}$에 대하여 다음과 같은 relation을 생각할 수 있다.

$$\forall i((i\in I)\implies(x_i\leq y_i))$$

즉 이 relation은 모든 $i\in I$에 대하여 $x_i\leq y_i$인 것으로 정의된다. 만일 우리가 이를 $x\leq y$로 적는다면, $\leq$가 (pre-)order가 됨은 쉽게 보일 수 있다. 이를 $\Gamma_i$들의 *product*라 부른다.

<ins id="ex11">**예시 11**</ins>  (pre-)Order가 주어진 집합 $F$를 생각하자. 임의의 집합 $E$에서 $F$로의 함수 $f$는 correspondence $f\leftrightarrow (f(x))\_{x\in E}$에 의하여 $\prod\_{x\in E}F_x$의 원소로 볼 수 있다. ($F_x=F$ for all $x$)  이제 이 product set 위에 정의된 $\Gamma_i$들의 product를 생각하자. 그럼 $f\leq g$는 임의의 $x\in E$에 대하여 $f(x)\leq g(x)$임을 의미한다. 여기에서 $f&lt;g$는 <em_ko>하나의</em_ko> $y\in E$에 대해서만 $f(y)&lt;g(y)$이고 나머지 모든 $x\in E$에 대해서는 $f(x)\leq g(x)$여도 성립함에 유의.
{: .example}

## 단조함수

<ins id="df12">**정의 12**</ins> $E$와 $F$가 preordered set이라 하자. 함수 $f:E\rightarrow F$가 *증가함수<sub>increasing function</sub>*이라는 것은 $x\leq y$이면 $f(x)\leq f(y)$인 것이다. 만약 $x\leq y$이면 $f(x)\geq f(y)$가 성립한다면, 이 함수는 *감소함수<sub>decreasing function</sub>*라 불린다. 증가함수와 감소함수를 통틀어 *단조함수<sub>monotone function</sub>*라 부른다.
{: .definition}

<ins id="rmk2">**참고**</ins> 임의의 상수함수는 증가함수인 동시에 감소함수이다. 그러나 이 역이 성립하는 것은 아니다. $E$가 하나 이상의 원소를 갖는 집합이라 하고. 이 위에서의 order $\leq$을 $x\leq x$만을 만족하도록 정의하자. (즉, 이 relation은 사실 등호다.) 그럼 $E$에서 $E$로의 항등함수는 증가함수인 동시에 감소함수지만 상수함수는 아니다.
{: .remark}

그리고, $\leq$를 $&lt;$로 바꾸면 다음 정의를 얻는다.

<ins id="df13">**정의 13**</ins> $E$, $F$가 strict order $&lt;$가 주어진 집합이라 하자. 함수 $f:E\rightarrow F$가 *순증가함수<sub>strictly increasing function</sub>*라는 것은, 만일 relation $x&lt;y$이 성립하면 $f(x)&lt;f(y)$도 성립한다는 것이며, *순감소함수<sub>strictly decreasing function</sub>*라는 것은 relation $x&lt;y$이 성립하면 $f(x)&gt;f(y)$도 성립한다는 것이다. 순증가함수, 순감소함수들을 통틀어 *순단조함수<sub>strictly monotone function</sub>*라 한다.
{: .definition}

<div class="remark" markdown="1">

<ins id="rmk3">**참고**</ins> 정의에 의해 injective한 단조함수는 항상 순단조함수다. 그러나 이 역 또한 항상 성립하는 것은 아니다. 예컨대, $\mathbb{N}$ 위에 strict order $\prec$을 다음의 식

$$m\prec n\iff ((m-n\text{ is even}) \wedge (m<n))$$

으로 정의하고, 이 집합을 $E$라 하자. 즉, $E$에서는 짝수는 짝수끼리, 홀수는 홀수끼리 크기 비교가 가능하지만 짝수와 홀수의 크기 비교는 불가능하다. 또, 자연수 집합 $\mathbb{N}$에 일상적인 strict order $&lt;$를 부여한 ordered set을 $F$라 하자. 그럼 $E$에서 $F$로의 함수 $m\mapsto \lfloor m/2\rfloor$은 순증가지만, injective가 되지 않는다.
</div>

<ins id="pp14">**명제 14**</ins> $E$, $E'$가 ordered set이고 $u:E\rightarrow E'$, $v:E'\rightarrow E$가 감소함수이며, $v(u(x))\geq x$와 $u(v(x'))\geq x'$이 모든 $x\in E$, $x'\in E'$에 대해 성립한다고 하자. 그럼 $u\circ v\circ u=u$ 이고 $v\circ u\circ v=v$이다.
{: .proposition}

<details class="proof" markdown="1">
<summary>증명</summary>

주어진 가정과 $u$가 감소함수라는 것에서 자명하다. 즉, $u$는 감소함수이므로, $v(u(x))\geq x$에서 $u(v(u(x)))\leq u(x)$가 모든 $x$에 대해 성립하지만, 가정의 두 번째 부분에서 $u(v(u(x)))\geq u(x)$이 성립한다.
</details>


---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

