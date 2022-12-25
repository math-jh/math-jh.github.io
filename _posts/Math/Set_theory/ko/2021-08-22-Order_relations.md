---

title: "순서관계의 정의"
excerpt: "순서관계의 정의와 성질들"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/order_relations
header:
    overlay_image: /assets/images/Set_theory/Order_relations.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-22
last_modified_at: 2022-11-27
weight: 14

---

## 순서관계

<div class="definition" markdown="1">
<ins id="df1">**정의 1**</ins> 이항관계 $R$이 *anti-symmetric<sub>반대칭적</sub>*이라는 것은 

> $x\mathrel{R}y$이고 $y\mathrel{R}x$이면 $x=y$

가 항상 성립하는 것이다.
</div>

그럼 순서관계는 다음과 같이 정의된다. 

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins>  이항관계 $(R,A,A)$가 *order relation<sub>순서관계</sub>*이라는 것은 $R$이 reflexive하며, transitive, anti-symmetric한 것이다.

</div>

이 경우, 우리는 $A$가 <em_ko>$R$에 의해 순서가 부여되었다</em_ko>고 하고, 종종 $A$를 *ordered set<sub>순서집합</sub>*이라고 부른다. 또, 동치관계 때와 비슷하게 $x\mathrel{R}y$를 $x\leq\_{\tiny R}y$로 적는다. 

<ins id="ex3">**예시 3**</ins> 이항관계 <phrase>$x=y$</phrase>는 order relation이다. 관계 <phrase>$x\subseteq y$</phrase> 또한 order relation이다. ([§순서쌍, ⁋명제 2](/ko/math/set_theory/ordered_pair#pp2)와 [§순서쌍, ⁋명제 3](/ko/math/set_theory/ordered_pair#pp3))
{: .example}

Ordered set은 $ \leq $라는 관계가 추가적으로 정의된 집합이므로, 이들 사이의 함수를 생각할 때는 $ \leq $ 또한 보존하는 함수를 주로 생각하게 된다. 특별히 다음을 정의한다.

<ins id="df4">**정의 4**</ins> 만일 두 order relation $(R, A, A)$과 $(R', A',A')$에 대해 어떠한 전단사함수 $f$가 존재하여 $x\leq\_{\tiny R}y$와 $f(x)\leq\_{\tiny R'}f(y)$가 동치라면 $f$를 *order isomorphism*이라 부른다. 
{: .definition}

앞으로 ordered set들 사이에서 isomorphism이라 하면 항상 order isomorphism을 뜻하는 것으로 이해한다. 

[§동치관계, ⁋명제 3](/ko/math/set_theory/equivalence_relations#pp3)과 비슷한 것을 순서관계에 대해서도 할 수 있다.

<div class="proposition" markdown="1">

<ins id="df5">**명제 5**</ins> 이항관계 $(R,A,A)$가 order relation인 것은 다음의 두 조건과 동치이다.

$$R\circ R=R,\qquad R\cap R^{-1}=\Delta_A$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 조건이 transitivity와 동등한 것은 [§동치관계, ⁋명제 3](/ko/math/set_theory/equivalence_relations#pp3)의 증명에서 이미 살펴보았다. 두 번째 조건은 reflexive와 antisymmetry를 섞어둔 것이라는 것도 쉽게 보일 수 있다.

</details>

## 원순서관계

우선 다음 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 함수 $f:A\rightarrow B$를 생각하고, $B$ 위에 order relation $\leq$가 정의되었다고 하자. 그럼 우리는 함수로부터 동치관계를 유도하듯, $A$ 위에 다음과 같이 정의된 관계 $\preceq$를 정의할 수 있다. ([§동치관계의 예시들, ⁋정의 2](/ko/math/set_theory/examples_of_equivalence#df2))

$$x\preceq y\iff f(x)\leq f(y)$$

정의로부터 $\preceq$는 reflexive하고 transitive하다. 하지만 일반적으로 $f$가 단사가 아닌 한 $\preceq$는 antisymmetry을 만족하지 않는다.
</div>

따라서 antisymmetry 조건을 빼서 다음과 같이 정의한다.

<ins id="df7">**정의 7**</ins> Reflexive하고 transitive한 관계 $R$을 *preorder relation<sub>원순서관계</sub>*라 부른다.
{: .definition}

$R$이 preorder relation이라면 이를 $\preceq\_{\tiny R}$과 같이 적기도 하지만, 많은 경우 preorder는 order relation과 비슷한 성질을 공유하기 때문에 order relation과 동일한 기호 $\leq\_{\tiny R}$를 사용하기도 한다. 우리도 특별한 경우가 아닌 한 $\leq\_{\tiny R}$를 사용한다.

Preorder relation의 성질을 알기 위해 우리는 order relation의 성질이지만 preorder의 성질은 아닌 antisymmetry를 좀 더 살펴봐야 한다. 만일 관계 $R$이 order relation이었다면, antisymmetry는 $(x\leq\_{\tiny R}y)\wedge(y\leq\_{\tiny R}x)\implies x=y$를 뜻한다. Preorder에 대해서는 이것이 성립하지 않는다는 것을 살펴보았지만, 이 경우는 다음 명제에 의해 <em_ko>일반화된 등호</em_ko>, 즉 동치관계가 똑같은 성질을 준다. 

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8**</ins>  $R$이 preorder relation이라 하자. 그럼 관계 <phrase>$x\leq_{\tiny R}y$이고 $y\leq_{\tiny R}x$</phrase>은 동치관계다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
위의 관계를 $S$라 하자. 우리는 $S$가 reflexive, symmetric, transitive함을 보여야 한다. 우선 이 관계가 reflexive함은 자명하다. $R$이 preorder이므로, 임의의 $x$에 대해 $x\mathrel{R}x$가 항상 성립하기 때문이다. 한편, 임의의 $x$, $y$에 대하여 $x\mathrel{S}y$라 하자. 그럼 

$$x\mathrel{S}y\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\iff(y\leq_{\tiny R}x)\wedge(x\leq_{\tiny R}y)\iff y\mathrel{S}x$$

이므로 $S$는 symmetric하다. 마지막으로 만일 $x\mathrel{S}y$, $y\mathrel{S}z$라면

$$\begin{aligned}  (x\mathrel{S}y)\wedge(y\mathrel{S}z)&\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge((y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y))\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\\
  &\iff(x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x)\\
  &\iff((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}z))\wedge((z\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\\
  &\iff(x\leq_{\tiny R}z)\wedge(z\leq_{\tiny R}x)\\
  &\iff x\mathrel{S}z
\end{aligned}$$

이므로 $S$는 transitive하고, 따라서 $S$는 동치관계가 된다.
</details>

## Strict order

주어진 order relation $\leq$에 대하여, $ < $을 <phrase>$x\leq y$이고 $x\neq y$</phrase>로 정의된 관계라 하자. 이 때 $ < $는 antisymmetry를 만족하지 않으므로 order relation이 될 수는 없고, 또 reflexive하지도 않으므로 preorder 또한 될 수 없다. 대신 다음을 정의하자.

<ins id="df9">**정의 9**</ins> 관계 $R$이 *asymmetric<sub>비대칭적</sub>*이라는 것은 $x\mathrel{R}y$이면 $y\not \mathrel{R}x$인 것이다. Asymmetric, transitive relation을 *strict order*라 부른다.
{: .definition}

Strict order를 표현하기 위해서 우리는 $<_{\tiny S}$를 사용한다. 그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="pp10">**명제 10**</ins>  $R$이 order relation이라 하자. 그럼 새로운 관계 <phrase>$x\leq_{\tiny R}y$이고 $x\neq y$</phrase>는 strict order이다.  

반대로 $S$가 strict order라 하자. 그럼 새로운 관계 <phrase>$x<_{\tiny S}y$이거나 $x=y$</phrase>는 order relation이다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $R$이 order relation이라 하고, 새로운 relation $S$를 <phrase>$x\leq_{\tiny R}y$이고 $x\neq y$</phrase>으로 정의하자. Asymmetry를 보이기 위해 우리는 $x\mathrel{S}y$와 $y\mathrel{S}x$가 동시에 성립할 수 없음을 보여야 한다. $(x\mathrel{S}y)\wedge(y\mathrel{S}x)$를 풀어 쓰면 다음과 같다.
  
$$((x\leq_{\tiny R}y)\wedge(x\neq y))\wedge((y\leq_{\tiny R}x)\wedge(y\neq x))$$

그런데 이는 다음과 같이 쓸 수 있다.

$$((x\leq_{\tiny R}y)\wedge(y\leq_{\tiny R}x))\wedge(x\neq y)$$

이는 $R$의 antisymmetry에 의하여 $(x=y)\wedge(x\neq y)$이고, 이는 항상 거짓이므로 $x\mathrel{S} y$이면 $y\not\mathrel{S}x$이다.

반대로 $S$가 strict order라 하고, 새로운 relation $R$을 <phrase>$x<_{\tiny S}y$이거나 $x=y$</phrase>로 정의하자. 우선 $x=x$이므로, 뒤쪽 조건에 걸려 $x\mathrel{R}x$이다. Antisymmetry를 보이기 위해, $x\mathrel{R}y$와 $y\mathrel{R}x$가 성립한다고 가정하자. 그럼 

$$\begin{aligned}  
(x\mathrel{R}y)\wedge(y\mathrel{R}x)&\iff((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}x)\vee(y=x))\\
   &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}x))\vee(x=y)
\end{aligned}$$

이다. Asymmetry에 의하여 $(x<\_{\tiny S}y)\wedge(y<\_{\tiny S}x)$는 불가능하므로, $(x\mathrel{R}y)\wedge(y\mathrel{R}x)$가 성립한다면 반드시 $x=y$가 성립한다. 마지막으로 transitivity을 보이기 위해 $x\mathrel{R}y$이고 $y\mathrel{R}z$라 하자. 그럼

$$\begin{aligned}
  (x\mathrel{R}y)\wedge(y\mathrel{R}z)&\iff ((x<_{\tiny S}y)\vee(x=y))\wedge((y<_{\tiny S}z)\vee(y=z))\\
  &\iff ((x<_{\tiny S}y)\wedge((y<_{\tiny S}z)\vee(y=z)))\vee((x=y)\wedge((y<_{\tiny S}z)\vee(y=z)))\\
  &\iff ((x<_{\tiny S}y)\wedge(y<_{\tiny S}z))\vee((x<_{\tiny S}y)\wedge(y=z))\\
  &\phantom{asdfghjkl}\vee((x=y)\wedge (y<_{\tiny S}z))\vee((x=y)\wedge(y=z))\\
  &\implies (x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x<_{\tiny S}z)\vee(x=y=z)\\
  &\iff x\mathrel{R}z
\end{aligned}$$

이므로 $R$은 transitive하다. 따라서 $R$은 order relation이 된다.
</details>

앞으로 order relation $R$에 의해 얻어지는 strict order를 $<_{\tiny R}$, 그리고 strict order $S$에 의해 얻어지는 order relation을 $\leq\_{\tiny S}$으로 적기로 한다.

<ins id="rmk1">**참고**</ins> 일반적으로 $x\not\leq y$라 하여 $x>y$인 것은 아니다. $S=\left\\{a,b\right\\}$라 하고, $\mathcal{P}(S)$ 위에 정의된 relation $\leq$를 부분집합들 간의 포함관계로 정의하자. 그럼 이는 자명하게 order relation이 된다. 이 때, $\left\\{a\right\\}\not\leq \left\\{b\right\\}$이지만 $\left\\{a\right\\}>\left\\{b\right\\}$ 또한 성립하지 않는다.
{: .remark}




---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.  
**[HJJ]** K. Hrbacek, T.J. Jeck, and T. Jech. *Introduction to Set Theory*. Lecture Notes in Pure and Applied Mathematics. M. Dekker, 1978.  

---

