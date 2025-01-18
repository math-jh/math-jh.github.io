---

title: "완비화"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/completion
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Completion.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2024-12-22
last_modified_at: 2024-12-22
weight: 14

---

## 완비화의 정의

임의의 abelian group $G$와 그 subgroup들의 decreasing sequence

$$\mathcal{J}:\qquad G=H_0\supseteq H_1\supseteq\cdots$$

가 주어졌다 하면, $G/ H_{i+1} \rightarrow G/H_{i}$들이 잘 정의되며, 더 일반적으로 이들의 적절한 합성을 통해 $j>i$일 때마다 $\rho_{ji}:G/H_j \rightarrow G/H_i$가 정의된다. 이들 데이터를 통해 inverse limit

$$\widehat{G}_\mathcal{J}=\varprojlim_i G/H_i=\left\{(g_1,g_2,\ldots)\in \prod G/H_i:\text{$\rho_{ji}(g_j)=g_i$ for all $j>i$}\right\}$$

그리고 canonical morphism들 $\rho_i:\widehat{G}\_{\mathcal{J}} \rightarrow G/ H_i$들이 주어지며, 이 때 $\rho_{ji}\circ\rho_j=\rho_i$가 모든 $j>i$에 대해 성립한다. 표기의 편의를 위해 $\mathcal{J}$가 문맥에 따라 명확할 경우 이를 간단히 $\widehat{G}$로 쓰기도 한다.

그럼 이들은 [\[범주론\] §극한, ⁋예시 5](/ko/math/category_theory/limits#ex5)에서 살펴본 것과 같이 범주론적인 극한으로 생각할 수 있으며, 따라서 다음의 universal property 또한 만족한다.

> $\rho_{ji}\circ\pi_j=\pi_i$를 만족하는 $K \rightarrow G/H_i$들이 주어질 때마다, 유일한 $\pi:K \rightarrow \widehat{G}$가 존재하여 다음의 diagram
> 
> ![universal_property](/assets/images/Math/Commutative_Algebra/Completion-1.png){:style="width:14em" class="invert" .align-center}
> 
> 이 commute하도록 할 수 있다.

만일 $G$에 ring 구조가 주어져 있고 $H_i$들이 ideal들이었다면 $\widehat{G}$ 또한 자연스러운 ring 구조를 갖는다. 우리가 살펴볼 상황은 다음과 같은 상황이다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$와 ideal $\mathfrak{a}$를 고정하자. 그럼 $A$의 ideal들의 $\mathfrak{a}$-filtration

$$\mathcal{J}:\qquad A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq \mathfrak{a}_2\cdots$$

에 대하여, 

$$\widehat{A}=\varprojlim_i A/\mathfrak{a}_i$$

을 이 filtration에 의해 정의되는 $A$의 *completion<sub>완비화</sub>*이라 부른다. 만일 natural map $A \rightarrow \widehat{A}$이 isomorphism이라면, $A$을 이 filtration에 대한 *complete ring<sub>완비환</sub>*이라 부른다. 

특별히 위의 filtration이

$$A\supseteq\mathfrak{a}\supseteq \mathfrak{a}^2\cdots$$

꼴로 주어졌다면 이를 $A$의 *$\mathfrak{a}$-adic completion<sub>$\mathfrak{a}$진 완비화</sub>*이라 부른다. 이 경우, 만일 $\mathfrak{a}$가 maximal ideal이라면 $\widehat{A}$은 유일한 maximal ideal $\widehat{\mathfrak{a}}$를 갖는 local ring이 되므로, $\widehat{A}$을 *complete local ring<sub>국소완비환</sub>*이라 부른다. 

</div>

우선 natural map $\rho:A \rightarrow \widehat{A}$는 canonical morphism들 $\pr_i: A \rightarrow A/\mathfrak{a}_i$들에 universal property를 적용하여 얻어지는 것이다. 그럼 정의에 의하여

$$x\in\ker\rho\iff\rho(x)=0\iff \rho_i(\rho(x))=0\text{ for all $i$}\iff \pr_i(x)=0\text{ for all $i$}\iff x\in \mathfrak{a}_i\text{ for all $i$}$$

이므로 $\rho$가 injective인 것과 $\bigcap \mathfrak{a}_i=0$인 것이 동치이다. 

이제 canonical morphism $\rho_i:\widehat{A}\rightarrow A/\mathfrak{a}_i$들의 kernel을 $\widehat{\mathfrak{a}}_i$로 쓰기로 하자. 그럼 정의에 의해 $\mathfrak{a}_i=\rho^{-1}(\widehat{\mathfrak{a}}_i)$이며, $\pr_i$들이 surjective이고 $\pr_i=\rho_i\circ\rho$이므로 $\rho_i$들이 모두 surjective이고, 따라서 first isomorphism theorem에 의하여

$$\widehat{A}/\widehat{\mathfrak{a}}_i\cong A/\mathfrak{a}_i$$

이 성립한다. 따라서 $\widehat{A}$의 ideal들의 descending chain

$$\widehat{A}=\widehat{\mathfrak{a}}_0\supseteq \widehat{\mathfrak{a}}_1\supseteq\cdots\tag{1}$$

은 $\mathfrak{a}$-filtration이 되며, 또 위의 isomorphism으로부터

$$\widehat{A}=\varprojlim_i A/\mathfrak{a}_i\cong\varprojlim_i \widehat{A}/\widehat{\mathfrak{a}}_i$$

이므로 $\widehat{A}$는 주어진 filtration에 대해 complete이다. 또, 위의 isomorphism은 다음의 isomorphism

$$\gr_\mathcal{J}A\cong\gr_{\widehat{\mathcal{J}}}\widehat{A}$$

또한 준다. 

## $\mathfrak{a}$진 위상

한편, $A$로부터 $\widehat{A}$를 만드는 과정은 특수한 종류의 위상을 부여하여 살펴볼 수도 있다. 우선 topological abelian group $G$가 주어졌다 하자. 그럼 $G$의 한 원소 $g$를 고정한 후, 이를 사용해 정의하는 translation map $T_g$는 연속이므로 $G$의 각 점에서의 neighborhood filter는 정확히 $0\in G$에서의 neighoborhood filter에 의해 모두 결정된다. 이 과정은 당연히 거꾸로 해낼 수도 있다.

앞선 절과 같이, $G$의 subgroup들의 decreasing sequence

$$G=H_0\supseteq H_1\supseteq\cdots$$

가 주어졌다 하자. 그럼 

$$\mathcal{N}(0)=\{U\subseteq G:\text{$G_n\subseteq U$ for some $n$}\}$$

으로 정의하면 이것이 [\[위상수학\] §열린집합, ⁋명제 6](/ko/math/topology/open_sets#prop6)의 모든 조건을 만족한다는 것을 안다. 이제 임의의 $g\in G$와 $U\in \mathcal{N}(0)$에 대하여, $g+U\in \mathcal{N}(g)$이도록 하면 이것이 $G$ 위에 위상구조를 준다. 

특별히 이를 [정의 1](#def1)의 상황에 대입하면 위의 과정을 통해 정의한 위상구조를 *$\mathfrak{a}$-adic topology<sub>$\mathfrak{a}$진 위상</sub>*이라 부른다. 이 때, $0\in A$는 countable local base

$$\mathfrak{a}\supseteq \mathfrak{a}^2\supseteq\cdots\tag{2}$$

를 가지므로 이렇게 정의된 $A$ 위에서의 위상은 first countable이다. 

다시 일반적인 topological abelian group $G$로 돌아와서, 우리는 [##ref##]()의 조건을 약화시켜 다음을 정의할 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Topological group $(G, +, 0)$에 대하여, $G$의 원소들의 수열 $(x_i)_{i\in \mathbb{N}}$이 *Cauchy sequence<sub>코시 수열</sub>*이라는 것은 $0$의 임의의 근방 $U$가 주어질 때마다 적당한 자연수 $N$이 존재하여, 다음 명제

$$m,n>N \implies x_m-x_n\in U$$

가 참이도록 할 수 있는 것을 말한다. 

</div>

그럼 [##ref##]()에서 Cauchy filter들의 equivalence class들의 모임으로 completion을 정의한 것과 같이, 우리는 두 Cauchy sequence $(x_m)$, $(y_n)$이 주어졌을 때 이들을 언제 같은 것으로 볼지를 정하고, 그를 통해 (위상적인) completion을 정의할 수 있다. 다만 우리가 관심있는 것은 위의 filtration (2)에 의해 정의되는 first countable topological group $A$이며, first countable space는 sequentual이므로 다음 정의에서는 편의를 위해 $G$가 first countable space라 가정하고, Cauchy filter 대신 Cauchy sequence를 사용한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Topological group $(G, +, 0)$의 두 Cauchy sequence $(x_m)$, $(y_n)$이 *equivalent<sub>동등</sub>*하다는 것은 $0$의 임의의 근방 $U$가 주어질 때마다 적당한 자연수 $N$이 존재하여, 다음 명제

$$m,n>N \implies x_m-y_n\in U$$

가 참이도록 할 수 있는 것을 말한다. First countable topological group $G$의 모든 Cauchy sequence들의 집합에 이 equivalence relation을 주어 얻어지는 집합을 $G$의 *completion<sub>완비화</sub>*이라 부르고, 이를 $\widehat{G}$로 적는다. 

</div>

이제 $0\in G$의 열린근방 $U$에 대하여, 

$$\widehat{U}=\{[(x_n)]\in \widehat{G}:\text{for any $(y_n)\in [(x_n)]$, $y_n\in U$ for all but finitely many $n$}\}$$

으로 정의하자. 그럼 약간의 계산을 통해, $\widehat{H}\_i$들을 coninitial subset으로 갖는 $\widehat{G}$의 집합들의 모임 $\mathcal{N}(0)$이 [\[위상수학\] §열린집합, ⁋명제 6](/ko/math/topology/open_sets#prop6)의 모든 조건을 만족한다는 것을 확인할 수 있고, 따라서 $\widehat{G}$에 위상구조를 정의할 수 있다. 정의에 의해 $\widehat{G}$ 또한 first countable이며, $x\in G$를 받아 상수수열 $(x_i=x)$를 내놓는 함수 $G \rightarrow \widehat{G}$가 연속임을 알 수 있다. 뿐만 아니라, 이 함수는 앞선 절에서 정의한 $G \rightarrow \widehat{G}$와 완전히 같은 것이다. 

## 완비화의 기본적인 성질들

이제 완비화의 기본적인 성질들에 대해 살펴보자. 앞서 살펴본 [정의 3](#def3)에 의하여 $\widehat{A}$의 임의의 원소는 $A$의 $\mathfrak{a}$-adic topology에서의 Cauchy sequence로 생각할 수 있다. 그럼 $b_j\in \mathfrak{a}^j$를 만족하는 $b_j$들에 대하여,

$$a_i=\sum_{j=1}^i b_j\tag{3}$$

으로 적으면 $(a_i)$는 $\widehat{A}$에서의 Cauchy sequence이고 따라서 이 수열의 극한

$$\sum_{j=1}^\infty b_j$$

은 $\widehat{A}$의 원소를 하나 정의한다. 거꾸로, 임의의 $\widehat{A}$의 원소 $(a_n')$이 주어졌다하면 $0$의 local base (2)를 이용하여 이 원소와 equivalent하고 (3)과 같은 형태를 갖는 Cauchy sequence를 찾을 수 있다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 만일 $A=\mathbb{k}[\x]$이고 $\mathfrak{a}=(\x)$라면 $\widehat{A}$는 *formal power series*들의 ring $\mathbb{k}[[\x]]$이다.

</div>

Ring $\mathbb{k}[[\x]]$는 유일한 nonzero prime ideal $\mathfrak{m}=(\x)$를 갖는 discrete valuation ring이다. 즉 $(\x)$에 속하지 않는 임의의 원소는 unit이며, 이는 본질적으로 다음의 식

$$\frac{1}{1+\x}=1-\x+\x^2-\cdots$$ 

으로부터 나온다. 위의 등식, 혹은 이와 동치인 다음의 등식

$$(1+\x)(1-\x+\x^2-\cdots)=1$$

은 위의 논의와 같이, $1-\x+\x^2-\cdots$의 차수 $i$까지의 부분합

$$1-\x+\x^2-\cdots+(-1)^i\x^i$$

에 대하여 

$$(1+\x)(1-\x+\x^2-\cdots+(-1)^i\x^i)=1+(-1)^i\x^i\in \mathfrak{m}^i$$

이므로, 이 곱은 상수수열 $(1)$과 equivalent하다는 것을 통해 얻어진다.

이 계산을 일반화하여 다음의 두 결과를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $A$가 ideal $\mathfrak{a}$에 대해 complete이라 하자. 그럼 다음 집합

$$U=\{1+a: a\in \mathfrak{a}\}$$

은 $A$의 unit들의 모임이며, $U$는 multiplicatively closed이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 논증에서 $\x$만 $a$로 바꾸면 된다.

</details>

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> Local ring $(A, \mathfrak{m})$에 대하여, $A[[\x_1,\ldots, \x_n]]$도 local ring이며, 그 유일한 maximal ideal은 $\mathfrak{m}+(\x_1,\ldots, \x_n)$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathfrak{m}+(\x_1,\ldots,\x_n)$ 바깥의 원소는 $0$이 아닌 상수항을 가지므로, [명제 5](#prop5)에 의해 이것이 unit임을 보일 수 있다. 

</details>

또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $A$의 ideal들의 filtration

$$A=\mathfrak{a}_0\supseteq \mathfrak{a}_1\supseteq\cdots$$

과 filtration에 대한 associated graded ring $\gr A$를 고정하자. 만일 $A$가 이 filtration에 대해 complete이라 하면, $A$의 ideal $\mathfrak{a}$와 그 원소들 $a_1,\ldots, a_n$에 대하여, $\initial(\mathfrak{a})$가 $\initial(a_1),\ldots, \initial(a_n)$에 의해 생성된다면 $\mathfrak{a}$ 또한 $a_1,\ldots, a_n$에 의해 생성된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

원소들 $a_1,\ldots, a_n$에 의해 생성되는 ideal을 $\mathfrak{a}'$라 하고 $\mathfrak{a}=\mathfrak{a}'$임을 보이자. 일반성을 잃지 않고 이들 원소들이 모두 $0$이 아니라 가정할 수 있다. 또, 만일 $a_k\in \mathfrak{a}_i$가 모든 $i$에 대해 성립했다면, canonical morphism $A \rightarrow \widehat{A}$에 의해 $a_k$는 $0\in \widehat{A}$로 옮겨지고, $A$가 complete이므로 이는 $a_k=0$이었다는 것이므로 적당한 $d$를 택하여 $a_k\not\in \mathfrak{a}_i$가 모든 $k$에 대해 성립하도록 할 수 있다.

한편 $\initial(\mathfrak{a})$가 $\initial(a_k)$들에 의해 생성된다는 가정으로부터, 임의의 $a\in \mathfrak{a}$에 대해 다음의 식

$$\initial(a)=\sum_{k=1}^n \beta_k\initial(a_k)\tag{4}$$

를 만족하는 $\beta_k\in \gr_\mathfrak{a}A$들이 존재하며, 위의 식에서 차수를 고려하면 $\beta_k$들은 homogeneous이고 그 차수는

$$\degree(\beta_k)=\degree (\initial(a))-\degree(\initial(a_k))>\degree(\initial(a))-d$$

여야 함을 안다. 따라서 $\initial(b_k)=\beta_k$를 만족하는 $b_k\in A$들에 대하여 $a-\sum_k b_k a_k$는 $\mathfrak{m}_{\degree(\initial(a))+1}$에 속하게 된다. 이 과정을 반복하여, 

$$a-\underbrace{\sum_k b_k a_k-\cdots}_{=a'} \in \mathfrak{a}_{d+1}$$

이도록 하는 $a'\in \mathfrak{a}'$를 택할 수 있다. 이 때, $a'$는 어차피 $a_k$들로 생성되므로 $a$가 $a_k$들로 생성되는 것은 $a-a'$가 $a_k$들로 생성되는 것을 보이는 것과 같다. 즉, 우리는 일반성을 잃지 않고 $a$가 $\mathfrak{a}_{d+1}$에 속해있다고 가정할 수 있다.

이제 이와 같은 가정에서 위의 식 (4)를 다시 살펴보자. $\degree(\initial(a))=e$라 하면, $\beta_k$의 차수는 $e-d$ 이상이어야 함을 앞에서 살펴보았다. 따라서 $b_k$들을 $\mathfrak{a}_{e-d}$에서 택할 수 있으며, 이제 위에서와 마찬가지 논리를 통해

$$a-\sum_{k=1}^n b_ka_k$$

는 $\mathfrak{a}_{e-d+1}$에 속한다는 것을 안다. 이를 반복하면

$$a-\sum_{k=1}^n\sum_{l=0}^j b_k^{(l)}a_k\in \mathfrak{a}_{e+j+1}$$

이도록 하는 $b_k^{(l)}\in \mathfrak{a}_{e-d+l}$들을 택할 수 있다. 이제 $A$는 complete이므로, 무한합

$$\sum_{l=0}^\infty b_k^{(l)}$$

은 $A$의 원소 $c_k$로 생각할 수 있다. 그럼

$$a-\sum_{k=1}^n c_k a_k\in \bigcap \mathfrak{a}_i=0$$

이므로 원하는 결과를 얻는다. 

</details>


---

**참고문헌**

**[AM]** M.F. Atiyah and I.G. Macdonald, *Introduction to commutative algebra*, Basic Books, 1969.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.

---