---

title: "합집합과 교집합"
excerpt: "집합들 간의 합집합과 교집합"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/union_and_intersection
header:
    overlay_image: /assets/images/Math/Set_Theory/Union_and_intersection.png
    overlay_filter: 0.5
sidebar: 
    nav: "set_theory-ko"

date: 2021-08-15
last_modified_at: 2022-11-24
weight: 8

---

## Family of sets

Index set $I$와, 집합들의 집합 $\mathcal{S}$가 주어졌다 하자. 그럼 $I$에서 $\mathcal{S}$로의 함수 $f=(F,I,\mathcal{S})$는 각각의 $i\in I$마다 $\mathcal{S}$의 원소, 즉 집합을 대응시킨다. 기존에는 이를 $(f\_i)\_{i\in I}$와 같이 쓰기로 하였으나, 집합을 대문자로 적는 관례를 유지하기 위해 이를 $(F\_i)\_{i\in I}$로 적기로 한다. 

Family $(A\_i)\_{i\in I}$의 모든 집합들이 어떤 집합 $A$의 부분집합이라 하자. 그럼 이 함수의 target $\mathcal{S}$를 $\mathcal{P}(A)$로 둘 수 있다. 이렇게 집합 $A\_i$들을 $A$의 부분집합으로 보고 싶을 때는 $(A\_i)\_{i\in I}$를 *집합 $A$의 부분집합들의 family*와 같이 표현한다.

## 합집합과 교집합

[§ZFC 공리계](/ko/math/set_theory/zfc_axioms)에서 우리는 합집합이 존재한다는 것을 공리로 받아들였다. 이 공리를 도입했을 때 사용한 표기법보다는 다음의 표기법이 좀 더 자주 쓰인다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $(A\_i)\_{i\in I}$가 집합들의 family라 하자. 그럼 <phrase>적어도 하나의 $A_i$에 속해있는 $x$들을 모두 모아둔 집합</phrase>을 이 family의 *합집합<sub>union</sub>*이라 하고, 이를 $\bigcup\_{i\in I}A\_i$로 적는다.

</div>

즉 합집합은 논리식

$$\exists i(i\in I\wedge x\in A_i)$$

를 만족하는 $x$들의 집합이다. 따라서 $I=\emptyset$이라면 $\bigcup\_{i\in I} A\_i=\emptyset$이다. 어렵지 않게 합집합은 $(A\_i)\_{i\in I}$의 target $\mathcal{S}$에 의존하지 않는 것을 확인할 수 있다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $(A\_i)\_{i\in I}$가 집합들의 family이고, $I$가 공집합이 아니라 하자. 그럼 <phrase>모든 $A_i$에 속해있는 $x$들의 집합</phrase>을 이 family의 *교집합<sub>intersection</sub>*이라 하고 $\bigcap\_{i\in I}A\_i$로 적는다.

</div>

교집합은 논리식

$$\forall i(i\in I\implies x\in A_i)$$

를 만족하는 $x$들의 모임이다. 만일 $I=\emptyset$이라면 $i\in I$가 거짓이 되어 전체 문장이 $x$에 관계없이 참이 되고 $\bigcap\_{i\in\emptyset} A\_i$는 전체집합이 되어야 하므로 모순이다. ([§ZFC 공리계, ⁋예시 4](/ko/math/set_theory/zfc_axioms#ex4)) $(A\_i)\_{i\in I}$의 target $\mathcal{S}$를 잘 정해준다면 이러한 모순을 피해 교집합을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 집합들의 family $(A\_i)\_{i\in I}$가 집합 $A$의 부분집합들의 family라 하자. 그럼 <phrase>$A$의 원소이면서 동시에 모든 $A_i$에 속해있는 $x$들의 집합</phrase>을 이 family의 *교집합*이라 부르며, $\bigcap\_{i\in I}A\_i$로 적는다.

</div>

이번에는 만일 $I=\emptyset$이더라도 조건이 

$$(x\in A)\wedge (\forall i(i\in I\implies x\in A_i))$$

이 되므로 $\bigcap\_{i\in I} A\_i=A$이다. 앞으로 모든 명제에서, 집합들의 family의 교집합을 택할 일이 있을 경우는 $I$가 공집합이 아니거나 주어진 family가 어떠한 집합의 부분집합들의 family임을 가정한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 집합들의 family $(A\_i)\_{i\in I}$와 전사함수 $f:K\rightarrow I$를 생각하자. 그럼 다음의 두 식

$$\bigcup_{k\in K}A_{f(k)}=\bigcup_{i\in I}A_i,\qquad \bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $x\in\bigcup\_{i\in I} A\_i$라 하자. 즉 어떤 $i_0\in I$에 대하여 $x\in A_{i_0}$이다. 그런데, $f$는 전사함수이므로 어떤 $k_0\in K$가 존재하여 $i_0=f(k_0)$이고, 따라서 $x\in A\_{f(k_0)}$이므로 $x\in\bigcup\_{k\in K}A\_{f(k)}$이다.  

반대로, 만일 $x\in\bigcup\_{k\in K}A\_{f(k)}$가 성립한다면, 어떤 $k_0\in K$에 대하여 $x\in A\_{f(k_0)}$이다. 그런데 $f(k_0)\in I$이므로, $A\_{f(k_0)}$는 $(A_i)\_{i\in I}$를 구성하는 집합 중 하나이고 따라서 $x\in \bigcup_{i\in I} A_{i}$이다.

이제 두 번째 식을 보여야 한다. 우선 $x\in\bigcap\_{i\in I}A\_i$라 하자. 그럼 모든 $i\in I$에 대하여 $x\in A\_i$이다. 임의의 $k_0\in K$에 대하여 $f(k_0)\in I$이므로, 모든 $k\in K$에 대하여 $x\in A\_{f(k)}$이고 따라서 $x\in \bigcap\_{k\in K}A\_{f(k)}$이다.  
반대로 만일 모든 $k\in K$에 대하여 $x\in A\_{f(k)}$라면, $f$는 전사이므로 모든 $i\in I$에 대해 $x\in A\_{f(k)}$이기도 하다.

</details>

특별히 $(A\_k)\_{k\in K}$가 임의의 $k,k'\in K$에 대하여 $A\_k=A\_{k'}$를 만족한다고 하자. 임의의 $k_0\in K$를 하나 택하여 $I=\\{k_0\\}$라 하고, 전사함수 $f:K\rightarrow I$에 위의 명제를 적용하면, 모든 $k$에 대해 $A_k=A_{k_0}=A_{f(k)}$이므로

$$\bigcup_{k\in K} A_k=\bigcup_{k\in K} A_{f(k)}=\bigcup_{i\in I}A_i=A_{k_0},\qquad \bigcap_{k\in K}A_k\bigcap_{k\in K}A_{f(k)}=\bigcap_{i\in I}A_i=A_{k_0}$$

가 성립한다.

이제 합집합과 교집합의 성질들을 조금 더 살펴보자. 만일 같은 index를 갖는 두 family $(A\_i)\_{i\in I}$와 $(B\_i)\_{i\in I}$가 주어졌고, $B_i\subseteq A_i$가 모든 $i\in I$에 대해 성립한다면 

$$\bigcup_{i\in I} B_i\subset\bigcup_{i\in I} A_i,\qquad \bigcap_{i\in I} B_i\subset\bigcap_{i\in I} A_i$$

임은 자명하다. 또, 주어진 family $(A\_i)\_{i\in I}$와 $I$의 부분집합 $J$에 대하여, 

$$\bigcup_{j\in J}A_j\subset\bigcup_{i\in I} A_i,\qquad\bigcap_{j\in J}A_j\supset\bigcap_{i\in I} A_i$$

임도 거의 자명하다. 

## 결합법칙

집합의 연산들은 결합법칙을 만족한다.

<div class="proposition" markdown="1">

<ins id="def5">**명제 5**</ins>  $(A\_i)\_{i\in I}$가 집합들의 family고, index set $I$가 family $(J\_k)\_{k\in K}$들의 합집합이라 하자. 그럼

$$\bigcup_{i\in I} A_i=\bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right),\quad \bigcap_{i\in I}A_i=\bigcap_{k\in K}\left(\bigcap_{j\in J_k} A_j\right)$$

가 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 합집합에 관한 식부터 보이자. 만일 $x\in \bigcup\_{i\in I}A\_i$라면, 어떠한 $i_0\in I$에 대하여 $x\in A\_{i_0}$이다. 이제 $I=\bigcup\_{k\in K} J\_k$이므로, 어떤 $k_0$가 존재하여 $i_0\in J\_{k_0}$이다. 그럼

$$A_{i_0}=\bigcup_{i\in \{i_0\}}A_i\subset\bigcup_{j\in J_{k_0}} A_j=\bigcup_{k\in\left\{k_0\right\}}\left(\bigcup_{i\in J_k} A_i\right)\subseteq \bigcup_{k\in K}\left(\bigcup_{j\in J_k} A_j\right)$$

이므로 $x\in A\_{i_0}\subseteq \bigcup\_{k\in K}\left(\bigcup\_{j\in J_k} A\_j\right)$이다.  

반대로 만일 $x\in \bigcup\_{k\in K}\left(\bigcup\_{j\in J_k} A_j\right)$이라면, 어떠한 $k_0\in K$에 대하여 $x\in \bigcup\_{j\in J\_{k_0}}A\_j$이고, 따라서 다시 어떤 $i_0\in J\_{k_0}$에 대하여 $x\in A\_{i_0}$이다. 이제 $i_0\in I$이므로 $x\in\bigcup\_{i\in I} A\_i$이다. 

이와 비슷하게 두 번째 식도 보일 수 있다. 만일 $x\in\bigcap\_{i\in I} A\_i$라면, 모든 $i\in I$에 대하여 $x\in A\_i$이다. 임의의 $k\in K$에 대하여 $J\_{k}\subseteq I$이므로, 모든 $i\in I$에 대하여 위의 식이 성립한다는 말은 모든 $j\in J\_{k}$에 대하여 $x\in A\_j$가 성립한다는 말이기도 하다. 임의로 선택된 $k$에 대하여 이것이 성립하므로, 이는 정확히 $x\in\bigcap\_{k\in K}\left(\bigcap\_{j\in J\_{k}}A_j\right)$를 의미한다.

</details>

## 합집합, 교집합의 상

다음과 같이 합집합이나 교집합의 image도 생각해 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins>  $(A\_i)\_{i\in I}$가 집합 $A$의 부분집합의 family고 $(R,A,B)$가 이항관계라 하자. 그럼

$$R\left(\bigcup_{i\in I} A_i\right)=\bigcup_{i\in I}R(A_i),\quad R\left(\bigcap_{i\in I} A_i\right)\subset\bigcap_{i\in I}R(A_i)$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 식을 보이자. 만일 $y\in R\left(\bigcup\_{i\in I}A_i\right)$라면, 적당한 $x\in \bigcup\_{i\in I}A_i$가 존재하여 $(x,y)\in R$이다. 이제 $x\in A_j$라 하면 $y\in R(A_j)$이므로 $y\in\bigcup\_{i\in I}R\left(A_i\right)$가 성립한다. 반대로 만일 $y\in \bigcup\_{i\in I}R\left(A_i\right)$라면 어떤 $j$에 대하여 $y\in R\left(A\_j\right)$이므로, 적당한 $x\in A\_j$가 존재하여 $(x,y)\in R$이다. 따라서 $y\in R\left(\bigcup\_{i\in I} A\_i\right)$가 성립한다.

두 번째 식은 한쪽 방향만 보이면 충분하다. $y\in R\left(\bigcap\_{i\in I}A\_i\right)$라 하자. 그럼 어떤 $x\in\bigcap\_{i\in I}A\_i$가 존재하여 $(x,y)\in R$이다. $x$는 모든 $A\_i$에 속하므로, 우리는 $(x,y)\in R(A\_i)$가 모든 $A\_i$에 대해 성립하는 것을 안다. 즉 $y\in \bigcap\_{i\in I}R\left(A\_i\right)$이다.

</details>

위의 명제의 두 번째 식의 반대쪽 포함관계는 일반적으로 성립하지 않지만, $R$이 함수의 역관계라면 등호가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins>  $f:A\rightarrow B$가 함수라 하고 $(B\_i)\_{i\in I}$가 $B$의 부분집합들의 family라 하자. 그럼 
  
  $$f^{-1}\left(\bigcap_{i\in I} B_i\right)=\bigcap_{i\in I} f^{-1}(B_i)$$

가 성립한다. 
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

한쪽 포함관계는 더 일반적인 경우에서 증명하였으므로, 반대쪽 포함관계만 증명하면 충분하다. 

임의의 $x\in\bigcap\_{i\in I} f^{-1}(B\_i)$가 주어졌다 하자. 그럼 모든 $i$에 대하여 $x\in f^{-1}(B_i)$이다. 즉, 모든 $i$에 대해 $(x,y\_i)\in F$이도록 하는 $y\_i\in B\_i$가 존재한다. 그런데 $f$가 함수이므로 그러한 $y\_i$는 유일하다. 이 공통된 값을 $y$라 하면 모든 $i\in I$에 대해 $y\in B\_i$이므로 $y\in\bigcap\_{i\in I} B\_i$이고, 따라서 $f(x)=y$에서 $x\in f^{-1}\left(\bigcap\_{i\in I} B\_i\right)$이다.

</details>

## 드 모르간 법칙

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8 (De Morgan's law)**</ins> 집합 $A$의 부분집합들의 Family $(A\_i)\_{i\in I}$에 대하여, 
  
$$A\setminus \left(\bigcup_{i\in I}A_i\right)=\bigcap_{i\in I}(A\setminus A_i),\quad A\setminus\left(\bigcap_{i\in I} A_i\right)=\bigcup_{i\in I} (A\setminus A_i)$$

가 성립한다.
</div>

<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 식을 보이기 위해 우선 $x\in A\setminus\left(\bigcup\_{i\in I} A\_i\right)$라 하자. 그럼 $x\in A$이고 $x\not\in\left(\bigcup\_{i\in I} A\_i\right)$이다. 따라서 모든 $i$에 대하여 $x\not\in A_i$이므로, $x\in (A\setminus A_i)$가 모든 $i$에 대하여 성립한다. 즉 $x\in\bigcap\_{i\in I}(A\setminus A\_i)$이다.  
반대로 만일 $x\in\bigcap\_{i\in I} (A\setminus A\_i)$라면, 임의의 $i\in I$에 대하여 $x\in A\setminus A_i$이고, 따라서 모든 $i\in I$에 대하여 $x\not\in A\_i$이다. 이제 $x\not\in\bigcup\_{i\in I} A\_i$이므로 $x\in A\setminus\bigcup\_{i\in I} A_i$이다.

두 번째 식은 등식 $A\setminus(A\setminus X)=X$가 모든 $X\subseteq A$에 대해 성립하므로 첫 번째 식으로부터 자명.

</details>


---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---