---

title: "군의 작용 (작성중)"
excerpt: "Group action"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/group_action
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Group_action.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2023-02-14
last_modified_at: 2023-02-14
weight: 10

---

복잡한 대수적 구조를 다룰 때 유효한 전략 중 하나는 이 구조를 직접 분석하는 대신, 주어진 대수적 대상이 다른 대수적 대상에 어떻게 작용하는지를 살펴보는 것이다. 우리는 특별히 군의 작용에 관심이 있는데, 언제나 그렇듯 조금 더 일반적으로 모노이드가 집합 위에 작용하는 경우를 먼저 생각한다.

## 집합 위에 작용하는 모노이드

임의의 집합 $E$가 주어졌다 하고, $E$에서 자기 자신으로의 함수들의 집합 $\Fun(E,E)$를 생각하자. 그럼 이 집합 $\Fun(E,E)$는 단순한 집합이 아니라, 함수의 합성 $\circ$, 그리고 항등원 $\id_E$을 갖는 monoid 구조를 갖는다. 일반적으로 대수적 대상에서 자기 자신으로 가는 함수를 *endomorphism*이라 부르므로, 이 monoid $\Fun(E,E)$를 집합 $E$의 *endomorphism monoid*라 부르고 $\End(E)$로 적는다. 

또, $\End(E)$의 원소들 가운데 역함수가 존재하는 것들을 *(set) automorphism*이라 부르고, 이들의 모임을 $\Aut(E)$로 적는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 monoid $M$이 주어졌다 하고, 집합 $E$를 고정하자. $M$이 $E$ 위에 왼쪽에서 *act<sub>작용</sub>*한다는 것은 monoid homomorphism $\rho:M\rightarrow\End(E)$가 주어진 것이다. 이 때, 집합 $E$를 *left $M$-set*이라 부른다.

임의의 $\alpha\in M$과 $x\in E$에 대하여, 함숫값 $\rho(\alpha)(x)$를 간단히 $\alpha\cdot x$로 표기한다. 

</div>

바꿔 말하자면 $M$이 $E$에 왼쪽에서 act한다는 것은 임의의 $\alpha,\beta\in M$과 $x\in E$에 대하여, 다음의 식

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x),\qquad e\cdot x=x$$

이 성립하는 것이다. 

일반적인 경우, 우리는 위와 같이 주어진 대상이 다른 대상에 왼쪽에서 act하는 경우를 생각하지만, 종종 오른쪽에서 act하는 것이 자연스러울 때도 있다. 이를 [정의 1](#def1)과 비슷한 형태로 정의하기 위해서는 다음 정의가 필요하다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 마그마 $(M,\ast)$에 대하여, $M$의 *opposite magma<sub>반대 마그마</sub>* $(M^\op,\ast^\op)$는 다음과 같이 정의된 마그마이다.

1. $M^\op=M$이다.
2. 임의의 $x,y\in M^\op$에 대하여, $x\ast^\op y$는 $y\ast x$로 정의된다.

</div>

그럼 monoid의 *right action*은 다음과 같이 정의된다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 임의의 monoid $M$과 집합 $E$에 대하여, $M$이 $E$ 위에 오른쪽에서 *act<sub>작용</sub>*한다는 것은 monoid homomorphism $\rho:M\rightarrow \End(E)^\op$가 주어진 것이다. 이 때, 집합 $E$를 *right $M$-set*이라 부른다.

임의의 $\alpha\in M$과 $x\in E$에 대하여, 함숫값 $\rho(\alpha)(x)$를 간단히 $x\cdot\alpha$로 표기한다.

</div>

이를 다시 쓰자면 

$$x\cdot(\beta\alpha)=(x\cdot\beta)\cdot\alpha,\qquad x\cdot e=x$$

라 할 수 있다. 

Left action과 right action은 표기상의 차이일 뿐, 본질적으로는 동일한 의미를 갖는다. 즉, $E$가 left $M$-set이라 하면 이는 자연스럽게 right $M^\op$-set으로 생각할 수 있고, 거꾸로 $E$가 right $M$-set이라 하면 이는 자연스럽게 left $M^\op$-set으로 생각할 수 있다. 따라서 앞으로 일반적인 이론을 전개할 때는 모든 action이 left action인 것으로 생각한다.

## $M$-set homomorphism

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Monoid $M$이 고정되었다 하고, $E,E'$가 $M$-set들이라 하자. 함수 $f:E\rightarrow E'$가 *$M$-set homomorphism*이라는 것은 모든 $x\in E$와 $\alpha\in M$에 대하여

$$f(\alpha\cdot x)=\alpha\cdot f(x)$$

이 성립하는 것이다.

</div>

어렵지 않게 $M$-set homomorphism들의 합성이 $M$-set homomorphism이고, 또 항등함수가 $M$-set homomorphism인 것을 확인할 수 있다. 즉, (left) $M$-set들의 모임은 카테고리를 이룬다. 이를 $\lset{M}$으로 적는다.

한편, $(E_i)$들이 $M$-set들의 모임이면 이들의 product $\prod E_i$에 다음의 식

$$\alpha\cdot(x_i)_{i\in I}=(\alpha\cdot x_i)_{i\in I}$$

을 통해 $M$의 action을 정의한 것이 다시 $M$-set이 된다. 이와 비슷하게 $M$-set $E$의 부분집합 $F$가 다음의 식

$$x\in F\implies \alpha\cdot x\text{ for all $\alpha\in F$}$$

을 만족한다면 $F$를 $M$-subset이라 부른다. 또, $M$-set 위에 정의된 동치관계 $\sim$이 $M$의 action과 compatible하다면, 즉

$$x\sim y\implies\alpha\cdot x\sim\alpha\cdot y$$

가 항상 참이라면 $E/\mathnormal{\sim}$은 자연스러운 $M$-set의 구조를 갖는다. 

## Stabilizer

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $M$-set $E$의 부분집합 $A$에 대하여, $A$의 *stabilizer<sub>안정자</sub>*는 $\alpha A\subseteq A$를 만족하는 $\alpha$들의 집합을 뜻한다. 이를 $\Stab (A)$로 적는다.

</div>

임의의 부분집합 $A$에 대하여 $e\in\Stab (A)$가 성립한다는 것이 자명하다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $M$-set $E$와 그 부분집합 $A$에 대하여, $\Stab (A)$는 $M$의 submonoid이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x\in A$에 대하여 $e\cdot x=x\in A$이므로 $e\in\Stab A$임은 자명하다. 임의의 $\alpha,\beta\in A$에 대하여, 

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x)$$

이고, $\beta\in\Stab A$로부터 $\beta\cdot x\in A$이므로 우변은 $A$의 원소이다.

</details>

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> Group $G$가 주어졌다 하자. $G$-set $E$와 그 부분집합 $A$에 대하여, $\Stab (A)$는 $G$의 subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $\alpha\in \Stab A$에 대하여, $\alpha^{-1}\in\Stab (A)$임만 보이면 충분하다. 그런데 임의의 $x\in A$에 대하여 

$$x=e\cdot x=\alpha\cdot(\alpha^{-1}\cdot x)$$

이므로 $x\in \alpha A$이고, 따라서 $A=\alpha A$가 성립한다. 이제 임의의 $y\in A=\alpha A$에 대하여, $y=\alpha\cdot x$라 하면

$$\alpha^{-1}\cdot y=\alpha^{-1}(\alpha\cdot x)=x\in A$$

이므로 $\alpha^{-1}\in\Stab (A)$가 성립한다.

</details>

위의 따름정리의 증명으로부터, group $G$가 집합 $E$에 act할 때, $\rho_g$는 반드시 bijection임을 안다. 즉 $\im\rho\subseteq \Aut(E)$가 항상 성립한다.

## 자기 자신 위에 작용하는 군

이제 우리는 집합 $E$ 위에 추가적인 구조가 주어진 경우를 생각한다. 가령 $E$ 또한 monoid 구조를 가진다 하고, 주어진 monoid $M$이 $E$ 위에 act한다 하자. 그럼 우리는 이제 $M$의 action이 $E$의 monoid 구조를 보존하기를 원한다. 

일반적으로 대수적인 대상이 주어졌을 때, endomorphism monoid의 원소들은 대수적인 구조를 보존해야 한다. 집합 $E$는 별도의 대수적인 구조가 없었으므로 $\End(E)=\Fun(E,E)$가 성립하지만, 가령 monoid $M$에 대해서 $\End(M)$이라 하면 항상 $M$의 *monoid endomorphism*들의 모임을 뜻하는 것으로 이해하며, $\Aut(M)$ 또한 마찬가지이다. 

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Group $G$의 임의의 원소 $g$에 대하여, $\rho_g\in\End(G)$를 다음의 식

$$\rho_g(x)=gxg^{-1}$$

으로 정의하면 $\rho_g\in\Aut(G)$가 성립하며, 대응 $\rho:g\mapsto \rho_g$는 group homomorphism이 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x,y\in G$에 대하여

$$\rho_g(xy)=g(xy)g^{-1}=(gxg^{-1})(gyg^{-1})=\rho_g(x)\rho_g(y)$$

가 성립하는 것으로부터 $\rho_g$가 group homomorphism이라는 것을 안다. 따라서 $\im\rho_g\subseteq\Aut(G)$가 성립한다. 

한편 임의의 $g,h\in G$와 $x\in G$에 대하여,

$$\rho_{gh}(x)=(gh)x(gh)^{-1}=g(hxh^{-1})g^{-1}=(\rho_g\circ\rho_h)(x)$$

이므로 $\rho_{gh}=\rho_g\circ\rho_h$이다. 즉, $\rho:g\mapsto \rho_g$는 $G$에서 $\Aut(G)$로의 group homomorphism이다.

</details>

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Group $G$가 주어졌다 하자. [명제 8](#prop8)의 automorphism $\rho_g$를 $g$에 의해 정의되는 *inner automorphism*이라 부르고, 이들의 모임을 $\Inn(G)$로 적는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Group $G$에 대하여, inner automorphism들의 모임 $\Inn(G)$는 $\Aut(G)$의 normal subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Inn(G)$는 group homomorphism $\rho:G\rightarrow\Aut(G)$의 image이므로 $\Aut(G)$의 subgroup인 것은 자명하며, 따라서 $\Inn(G)$가 *normal* subgroup임만 보이면 충분하다. 

임의의 $f\in\Aut(G)$를 택하고, $g\in G$를 임의로 고정하자. $f\circ\rho_g\circ f^{-1}\in \Inn(G)$임을 보여야 한다. 이는 임의의 $x\in G$에 대하여, 

$$(f\circ\rho_g\circ f^{-1})(x)=f(gf^{-1}(x)g^{-1})=f(g)xf(g^{-1})=\rho_{f(g)}(x)$$

이므로 자명하다. 

</details>

임의의 group $G$가 주어졌을 때, $\Aut(G)$는 $\Aut(G)\hookrightarrow \Fun(G,G)$를 통해 $G$에 act하며 


한편, $\rho:G\rightarrow\Inn(G)$는 전사이며, 따라서 first isomorphism theorem에 의하여

$$G/\ker\rho\cong\Inn(G)$$

가 성립한다. $\ker\rho$에도 특별한 이름이 있다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> Group $G$와, [명제 8](#prop8)에서 정의한 group homomorphism $\rho:G\rightarrow\Inn(G)$에 대하여, $\ker\rho$를 $G$의 *center<sub>중심</sub>*이라 부르고 $C(G)$로 표기한다.

</div>

정의에 의하여,

$$g\in\ker\rho\iff\rho_g=\id_G\iff gxg^{-1}=x\quad\text{for all $x\in G$}$$

이므로

$$C(G)=\{g\in G:gx=xg\text{ for all $x\in G$}\}$$

가 성립한다. 

$\Aut(G)\hookrightarrow\End(G)$는 monoid homomorphism이며, 따라서 

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---