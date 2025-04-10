---

title: "군의 작용"
excerpt: "Group action"

categories: [Math / Algebraic Structures]
permalink: /ko/math/algebraic_structures/group_actions
header:
    overlay_image: /assets/images/Math/Algebraic_Structures/Group_actions.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_structures-ko"

date: 2023-02-14
last_modified_at: 2023-02-14
weight: 11

---

복잡한 대수적 구조를 다룰 때 유효한 전략 중 하나는 이 구조를 직접 분석하는 대신, 주어진 대수적 대상이 다른 대수적 대상에 어떻게 작용하는지를 살펴보는 것이다. 우리는 특별히 군의 작용에 관심이 있는데, 언제나 그렇듯 조금 더 일반적으로 모노이드가 집합 위에 작용하는 경우를 먼저 생각한다.

## 집합 위에 작용하는 모노이드

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Monoidal category $(\mathcal{A},\otimes, I)$와 $\mathcal{A}$의 monoid object $(A,\cdot, 1)$를 고정하자. 그럼 morphism $\rho: A\otimes E\rightarrow E$이 대상 $E\in\obj(\mathcal{A})$ 위에 정의된 $A$의 *left action<sub>왼쪽 작용</sub>*이라는 것은 다음 두 diagram이 모두 commute하는 것이다.

![left_module](/assets/images/Math/Algebraic_Structures/Modules-1.png){:style="width:30em" class="invert" .align-center}

여기서 $I\otimes E \rightarrow E$는 left unitor이다. 이 상황을 $A\circlearrowright E$로 적는다.

비슷하게, morphism $\rho: E\otimes A\rightarrow E$이 대상 $E\in\obj(\mathcal{A})$ 위에 정의된 $A$의 *right action<sub>오른쪽 작용</sub>*이라는 것은 다음 두 diagram이 모두 commute하는 것이다.

![right_module](/assets/images/Math/Algebraic_Structures/Modules-2.png){:style="width:30em" class="invert" .align-center}

마찬가지로 $E\otimes I \rightarrow E$는 right unitor이다. 이 상황을 $E \circlearrowleft A$로 적는다.

</div>

Monoidal category $(\Set,\times, I)$ 위의 monoid object $(M,\cdot,1)$을 고정하자. 그럼 이를 통해 임의의 집합 $E$ 위에 정의된 $M$의 left action을 생각할 수 있다. 그럼 [\[집합론\] §집합의 곱, ⁋명제 4](/ko/math/set_theory/product_of_sets#prop4)로부터

$$\Hom_\Set(M\times E,E)\cong\Hom_\Set(M,\Hom_\Set(E,E))\cong\Hom_\Set(M, \End(E))$$

이므로, 임의의 left action은 함수 $M \rightarrow \End(E)$를 정의한다. 그럼 [정의 1](#def1)의 두 diagram이 commutative라는 것은 이 함수가 실은 monoid homomorphism이라는 것과 같다. 

바꿔 말하자면 $M$이 $E$에 왼쪽에서 act한다는 것은 임의의 $\alpha,\beta\in M$과 $x\in E$에 대하여, 다음의 식

$$(\alpha\beta)\cdot x=\alpha\cdot(\beta\cdot x),\qquad e\cdot x=x$$

이 성립하는 것이다. 

일반적인 경우, 우리는 위와 같이 주어진 대상이 다른 대상에 왼쪽에서 act하는 경우를 생각하지만, 종종 오른쪽에서 act하는 것이 자연스러울 때도 있다. 이는 다음 정의에 의해 사실은 같은 것이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 마그마 $(M,\ast)$에 대하여, $M$의 *opposite magma<sub>반대 마그마</sub>* $(M^\op,\ast^\op)$는 다음과 같이 정의된 마그마이다.

1. 집합으로서 $M^\op=M$이다.
2. 임의의 $x,y\in A^\op$에 대하여, $x\ast^\op y$는 $y\ast x$로 정의된다.

</div>

그럼 right $M$-action은 left $M^\op$-action과 같은 것임을 확인할 수 있다. 이를 다시 쓰자면 

$$x\cdot(\beta\alpha)=(x\cdot\beta)\cdot\alpha,\qquad x\cdot e=x$$

라 할 수 있다. 이렇게 left action과 right action은 표기상의 차이일 뿐, 본질적으로는 동일한 의미를 갖는다. 따라서 앞으로 일반적인 이론을 전개할 때는 모든 action이 left action인 것으로 생각한다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Monoid $M$과 $M$-set $E$가 주어졌다 하자. 그럼 $\mathcal{P}(E)$도 자연스러운 $M$-set 구조를 갖는다. 임의의 $\alpha\in M$과 $A\in \mathcal{P}(E)$에 대하여, $\alpha\cdot A$를 다음 식

$$\alpha\cdot A=\{\alpha\cdot a\mid a\in A\}$$

으로 정의하자. 그럼 

$$(\alpha\beta)\cdot A=\{(\alpha\beta)\cdot a\mid a\in A\}=\{\alpha\cdot(\beta\cdot a)\mid a\in A\}=\alpha\cdot\{\beta\cdot a\mid a\in A\}=\alpha\cdot(\beta\cdot A)$$

이므로 이것이 $\mathcal{P}(E)$ 위에 $M$-action을 정의한다.

</div>

논의의 편의를 위해 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Monoid $M$이 집합 $E$ 위에 left action을 정의할 때, $E$와 이 action을 통틀 (left) $M$-set이라 부른다. 

</div>

## $M$-set homomorphism

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Monoid $M$이 고정되었다 하고, $E,E'$가 $M$-set들이라 하자. 함수 $f:E\rightarrow E'$가 *$M$-set homomorphism*이라는 것은 모든 $x\in E$와 $\alpha\in M$에 대하여

$$f(\alpha\cdot x)=\alpha\cdot f(x)$$

이 성립하는 것이다. 

</div>

어렵지 않게 $M$-set homomorphism들의 합성이 $M$-set homomorphism이고, 또 항등함수가 $M$-set homomorphism인 것을 확인할 수 있다. 즉, (left) $M$-set들의 모임은 카테고리를 이룬다. 이를 $\lset{M}$으로 적는다.

임의의 monoid homomorphism $\phi:M \rightarrow M'$을 고정하자. 그럼 임의의 $M'$-set $E$에 대하여, 다음 합성

$$M\overset{\phi}{\longrightarrow}M'\overset{\rho}{\longrightarrow}\End(E)$$

을 통해 $E$를 $M$-set으로 생각할 수 있다. 이렇게 정의되는 action을 $\phi^\ast\rho$라 적자. 그럼 명시적으로 $\phi^\ast\rho$는 임의의 $\alpha\in M$과 $x\in E$에 대해,

$$(\phi^\ast\rho)(\alpha)(x)=\rho(\phi(\alpha))(x)$$

으로 정의되는 action이다. 이제 두 $M'$-action $\rho:M' \rightarrow \End(E)$와 $\rho':M' \rightarrow \End(E)$가 주어졌다 하고, 이들 사이의 $M'$-homomorphism $f:E \rightarrow E'$가 주어졌다 하자. 그럼 임의의 $\alpha\in M$과 $x\in E$에 대하여,

$$f((\phi^\ast\rho)(\alpha)(x))=f(\rho(\phi(\alpha))(x))=\rho'(\phi(\alpha))(f(x))=(\phi^\ast\rho')(f(x))$$

이 성립한다. 즉 임의의 monoid homomorphism $\phi:M \rightarrow M'$은 $\lset{M'}$에서 $\lset{M}$으로의 functor를 정의한다. 툭별히 $\iota$가 submonoid의 inclusion이라면 이는 monoid action의 restriction이 된다. 


한편, $(E_i)$들이 $M$-set들의 모임이면 이들의 product $\prod E_i$에 다음의 식

$$\alpha\cdot(x_i)_{i\in I}=(\alpha\cdot x_i)_{i\in I}$$

을 통해 $M$의 action을 정의한 것이 다시 $M$-set이 된다. 이와 비슷하게 $M$-set $E$의 부분집합 $F$가 다음의 식

$$x\in F\implies \alpha\cdot x\text{ for all $\alpha\in F$}$$

을 만족한다면 $F$를 $M$-subset이라 부른다. 또, $M$-set 위에 정의된 동치관계 $\sim$이 $M$의 action과 compatible하다면, 즉

$$x\sim y\implies\alpha\cdot x\sim\alpha\cdot y$$

가 항상 참이라면 $E/\mathnormal{\sim}$은 자연스러운 $M$-set의 구조를 갖는다. 

## Stabilizer, fixer

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> $M$-set $E$의 부분집합 $A$가 주어졌다 하자. 
- $A$의 *stabilizer<sub>안정자</sub>*는 $\alpha A\subseteq A$를 만족하는 $\alpha$들의 집합을 뜻하고, 이를 $\stab (A)$로 적는다.
- $A$의 *strict stabilizer<sub>강한 안정자</sub>*는 $\alpha A=A$를 만족하는 $\alpha$들의 집합을 뜻하고, 이를 $\Stab(A)$로 적는다.
- $A$의 *fixer<sub>고정자</sub>*는 모든 $a\in A$에 대해 $\alpha a=a$를 만족하는 $\alpha$들의 집합을 뜻하며, 이를 $\Fix(A)$로 적는다.

</div>

임의의 부분집합 $A$에 대하여 $\Fix(A)\subseteq \Stab(A)\subseteq \stab(A)$가 성립한다. 또, $e\in\Fix(A)$임이 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $M$-set $E$와 그 부분집합 $A$에 대하여, $\stab(A)$, $\Stab (A)$와 $\Fix(A)$는 $M$의 submonoid이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이들 집합이 연산에 대해 닫혀있음만 보이면 충분하다. 만일 $\alpha,\beta\in\stab(A)$라 하면, 

$$(\alpha\beta)A=\alpha(\beta A)\subseteq \alpha A\subseteq A$$

으로부터 $\alpha\beta\in \stab(A)$임을 안다. 비슷하게 만일 $\alpha,\beta\in\Stab(A)$라 하면,

$$(\alpha\beta)A=\alpha(\beta A)=\alpha A=A$$

이므로 $\alpha\beta\in \Stab(A)$이고 주장이 성립한다. 마지막으로 만일 $\alpha,\beta\in\Fix(A)$라면 임의의 $a\in A$에 대해

$$(\alpha\beta)a=\alpha(\beta a)=\alpha a=a$$

이므로 $\alpha\beta\in \Fix(A)$이다.

</details>

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> Group $G$가 주어졌다 하자. $G$-set $E$와 그 부분집합 $A$에 대하여, $\Stab (A)$와 $\Fix(A)$는 $G$의 subgroup이며, 특히 $\Fix(A)$는 $\Stab(A)$의 normal subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 주장은 주어진 집합들이 역원에 대해 닫혀있음만 보이면 충분하고, 이는 임의의 $\alpha\in\Stab(A)$에 대해 다음 식

$$A=(\alpha^{-1}\alpha)A=\alpha^{-1}(\alpha A)=\alpha^{-1}A$$

이 성립하고, 임의의 $\alpha\in\Fix(A)$와 $a\in A$에 대해 

$$a=(\alpha^{-1}\alpha)a=\alpha^{-1}(\alpha a)=\alpha^{-1}a$$

이 성립하는 것으로부터 자명하다. 두 번째 주장은 임의의 $\alpha\in\Fix(A)$, $\beta\in\Stab(A)$가 주어졌다 하고, 임의의 $a\in A$에 대해 $(\beta\alpha\beta^{-1})a$를 계산해보면

$$(\beta\alpha\beta^{-1})a=\beta(\alpha(\beta^{-1}a))=\beta\beta^{-1}a=a$$

이므로 $\beta\alpha\beta^{-1}\in\Fix(A)$가 되어 성립한다. 

</details>

위의 따름정리의 증명으로부터, group $G$가 집합 $E$에 act할 때, $\rho_g$는 반드시 전단사임을 안다. 즉 $\im\rho\subseteq \Aut(E)$가 항상 성립한다.

## 내부자기동형사상

이제 우리는 집합 $E$ 위에 추가적인 구조가 주어진 경우를 생각한다. 가령 $E$ 또한 monoid 구조를 가진다 하고, 주어진 monoid $M$이 $E$ 위에 act한다 하면, $M$-action은 monoid homomorphism $M \rightarrow\End(E)=\End_\Mon(E)$로 주어진다. 

특별히 group $G$가 자기 자신 위에 act하는 경우를 생각하자. 즉 $\rho:G\rightarrow\End(G)=\End_\Grp(G)$가 주어져 있다 하면, [따름정리 8](#cor8)의 증명으로부터 $\rho$의 image는 모두 전단사라는 것을 안다. 그런데 전단사인 group homomorphism은 항상 group isomorphism이므로 ([§대수적 구조, ⁋정의 6](/ko/math/algebraic_structures/algebraic_structures#def6)) $G$가 자기 자신 위에 act한다면 이는 반드시 group homomorphism $G \rightarrow \Aut(G)$와 같은 형태로 나타나야 한다는 것을 안다.

자기 자신 위에서 정의된 group action 중 특히 다음의 예시는 기억해둘 만한 가치가 있다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Group $G$의 임의의 원소 $g$에 대하여, $\rho_g\in\Aut(G)$를 다음의 식

$$\rho_g(x)=gxg^{-1}$$

으로 정의하면 대응 $\rho:g\mapsto \rho_g$는 group homomorphism이 된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $x,y\in G$에 대하여

$$\rho_g(xy)=g(xy)g^{-1}=(gxg^{-1})(gyg^{-1})=\rho_g(x)\rho_g(y)$$

가 성립하는 것으로부터 $\rho_g$가 group homomorphism이라는 것을 안다. 따라서 $\im\rho\subseteq\Aut(G)$가 성립한다. 

한편 임의의 $g,h\in G$와 $x\in G$에 대하여,

$$\rho_{gh}(x)=(gh)x(gh)^{-1}=g(hxh^{-1})g^{-1}=(\rho_g\circ\rho_h)(x)$$

이므로 $\rho_{gh}=\rho_g\circ\rho_h$이다. 즉, $\rho:g\mapsto \rho_g$는 $G$에서 $\Aut(G)$로의 group homomorphism이다.

</details>

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Group $G$가 주어졌다 하자. [명제 9](#prop9)의 automorphism $\rho_g$를 $g$에 의해 정의되는 *inner automorphism<sub>내부자기동형사상</sub>*이라 부르고, 이들의 모임을 $\Inn(G)$로 적는다.

</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Group $G$에 대하여, inner automorphism들의 모임 $\Inn(G)$는 $\Aut(G)$의 normal subgroup이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Inn(G)$는 group homomorphism $\rho:G\rightarrow\Aut(G)$의 image이므로 $\Aut(G)$의 subgroup인 것은 자명하며, 따라서 $\Inn(G)$가 *normal* subgroup임만 보이면 충분하다. 

임의의 $f\in\Aut(G)$를 택하고, $g\in G$를 임의로 고정하자. $f\circ\rho_g\circ f^{-1}\in \Inn(G)$임을 보여야 한다. 이는 임의의 $x\in G$에 대하여, 

$$(f\circ\rho_g\circ f^{-1})(x)=f(gf^{-1}(x)g^{-1})=f(g)xf(g^{-1})=\rho_{f(g)}(x)$$

이므로 자명하다. 

</details>

한편, $\rho:G\rightarrow\Inn(G)$는 전사이며, 따라서 first isomorphism theorem에 의하여

$$G/\ker\rho\cong\Inn(G)$$

가 성립한다. $\ker\rho$에도 특별한 이름이 있다.

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> Group $G$와, [명제 9](#prop9)에서 정의한 group homomorphism $\rho:G\rightarrow\Inn(G)$에 대하여, $\ker\rho$를 $G$의 *center<sub>중심</sub>*이라 부르고 $C(G)$로 표기한다.

</div>

정의에 의하여,

$$g\in\ker\rho\iff\rho_g=\id_G\iff gxg^{-1}=x\quad\text{for all $x\in G$}$$

이므로, $G$가 inner automorphism으로 자기 자신 위에 작용하는 상황에서의 fixer $\Fix(G)$가 정확히 $C(G)$이다. 더 일반적으로, 임의의 부분집합 $A\subseteq G$에 대하여 $A$의 fixer $\Fix(A)$를 $A$의 *centralizer* $C_G(A)$로 정의한다. 이와 비슷하게 $A$의 *normalizer* $N_G(A)$를 $\Stab(A)$로 정의한다. 

## 궤도-안정자 정리

이제 다시 우리는 일반적인 집합 $E$ 위에 정의된 group action을 생각한다. 우선 다음을 정의하자. 

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> 집합 $E$ 위에 group $G$의 action이 정의되었다 하자. 그럼 원소 $x\in E$의 *orbit*은 다음의 집합

$$G\cdot x=\{g\cdot x\mid g\in G\}$$

으로 주어진다. 

</div>

그럼 $E$ 위에 정의된 다음의 relation

$$x\sim y\iff G\cdot x=G\cdot y\tag{$\ast$}$$

은 equivalence relation이므로 quotient set $E/{\sim}$이 정의되며, 이는 orbit들로 이루어진 집합이다. 

<div class="proposition" markdown="1">

<ins id="thm14">**정리 14 (Orbit-stabilizer theorem)**</ins> 집합 $E$ 위에 group $G$의 action이 주어졌다 하자. 그럼 다음의 식

$$\lvert G\cdot x\rvert=[G:\Stab(x)]$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $p:G \rightarrow G\cdot x$를 $g\mapsto g\cdot x$로 정의하면 $G\cdot x$의 정의에 의해 이 함수는 surjective이다. 한편, $p(g_1)=p(g_2)\iff g_1^{-1}g_2\in \Stab(x)$이므로 [\[집합론\] §동치관계의 예시들, ⁋명제 7](/ko/math/set_theory/examples_of_equivalence#prop7) 이후의 canonical decomposition으로부터 원하는 결과를 얻는다. 

</details>

따라서, 만일 $G$가 finite이라면 [§몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups)에 의하여 다음의 식

$$\lvert G\cdot x\rvert=\frac{\lvert G\rvert}{\lvert\Stab(x)\rvert}\tag{$\ast\ast$}$$

을 얻는다. 

마찬가지로 $G$가 finite이라 하고, $G$가 유한집합 $E$ 위에 act한다 하자. $E^g$를 $g$에 의해 고정되는 원소들

$$E^g=\{x\in E\mid g\cdot x=x\}$$

로 정의하면

$$\sum_{g\in G}\lvert E^g\rvert=\# \{(g, x)\in G\times E: g\cdot x=x\}=\sum_{x\in X}\lvert \Stab(x)\rvert$$

이 성립한다. 이제 ($\ast\ast$)로부터 

$$\sum_{x\in X}\lvert \Stab(x)\rvert=\sum_{x\in X}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}$$

이다. 한편 ($\ast$)로부터 정의되는 quotient set $E/{\sim}$을 생각하면, 위의 합은 다시

$$\sum_{x\in X}\frac{\lvert G\rvert}{\lvert G\cdot x\rvert}=\lvert G\rvert\sum_{O\in E/{\sim}}\sum_{x\in O}\frac{1}{\lvert O\rvert}=\lvert G\rvert\sum_{O\in E/{\sim}} 1=\lvert G\rvert\lvert E/{\sim}\rvert$$

로 쓸 수 있다. 이로부터 다음 보조정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="lem15">**보조정리 15**</ins> Finite group $G$가 유한집합 $E$ 위에 act한다고 하고, $E/{\sim}$을 orbit들로 이루어진 $E$의 quotient set이라 하자. 그럼 다음의 식

$$\lvert E/{\sim}\rvert=\frac{1}{\lvert G\rvert}\sum_{g\in G}\lvert E^g\rvert$$

이 성립한다. 

</div>

---

**참고문헌**

**[Bou]** Bourbaki, N. Algebra I. *Elements of Mathematics*. Springer. 1998.  

---