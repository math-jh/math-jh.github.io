---

title: "합집합과 교집합"
excerpt: "집합들 간의 합집합과 교집합"

categories: [Math / Set Theory]
permalink: /ko/math/set_theory/union_and_intersection
header:
    overlay_image: /assets/images/Set_theory/Union_and_intersection.png
    overlay_filter: 0.5
sidebar: 
    nav: "set-ko"

date: 2021-08-15
last_modified_at: 2022-05-17
weight: 6

---

이항관계를 처음 소개할 때 언급했듯, 집합론에 대한 우리 이야기는 함수, 동치관계, 순서관계 이 세 가지를 다루면 끝이 난다. 나머지 둘을 다루기 전에 집합 사이의 연산들을 정의할 필요가 있다.

## Family of sets

Index set $I$와, 집합들의 집합 $\mathcal{S}$가 주어졌다 하자. 그럼 $I$에서 $\mathcal{S}$로의 함수 $a=(A,I,\mathcal{S})$는 각각의 $i\in I$마다 $\mathcal{S}$의 원소, 즉 집합을 대응시킨다. 이 경우 $i$에서의 $a$의 함숫값은 $a(i)$ 대신 $A_i$로 적는 것이 일반적이다. 이 함수의 그래프를 우리는 *family of sets<sub>집합족</sub>*이라 부르고, 종종 $(A\_i)\_{i\in I}$로 적는다. 

특별히 주어진 family $(A\_i)\_{i\in I}$의 모든 집합들이 어떤 집합 $A$의[^1] 부분집합이라 하자. 그럼 위에서 함수 $a$의 target $\mathcal{S}$를 $\mathcal{P}(A)$로 둘 수 있다. 대부분의 경우는 이러한 조건의 유무가 큰 차이를 보이지 않지만, 이 차이가 두드러지는 몇몇 경우들이 있다. ([정의 2](#df2)와 [정의 3](#df3)) 집합 $A\_i$들을 $A$의 부분집합으로 보고 싶을 때는 $(A\_i)\_{i\in I}$를 *집합 $A$의 부분집합들의 family*와 같이 표현한다.

## 합집합과 교집합

[§ZFC 공리계](/ko/math/set_theory/zfc_axioms)에서 우리는 합집합이 존재한다는 것을 공리로 받아들였다. 이 공리를 도입했을 때 사용한 표기법보다는 다음의 표기법이 좀 더 자주 쓰인다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $(A\_i)\_{i\in I}$가 집합들의 family라 하자. 그럼 <phrase>적어도 하나의 $A_i$에 속해있는 $x$들을 모두 모아둔 집합</phrase>을 이 family의 *합집합<sub>union</sub>*이라 하고, 이를 $\bigcup\_{i\in I}A\_i$로 적는다.

</div>

즉 합집합은 논리식

$$\exists i(i\in I\wedge x\in A_i)$$

를 만족하는 $x$들의 집합이다. 따라서 $I=\emptyset$이라면 $\bigcup\_{i\in I} A\_i=\emptyset$이다. 

어떤 집합 $A$가 존재하여, 모든 $i$에 대해 $A_i\subseteq A$였다 하더라도, 이들의 합집합 $\bigcup\_{i\in I}A\_i$는 달라질 것이 없다. 즉 함수 $a$의 target을 $\mathcal{P}(A)$로 설정해주어도 이것이 합집합 $\bigcup\_{i\in I}A_i$에 미치는 영향은 없다. 반면 교집합의 경우에는 $a$의 target이 $\mathcal{P}(A)$인지 아닌지가 그 결과에 영향을 끼친다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $(A\_i)\_{i\in I}$가 집합들의 family이고, $I$가 공집합이 아니라 하자. 그럼 <phrase>모든 $A_i$에 속해있는 $x$들의 집합</phrase>을 이 family의 *교집합<sub>intersection</sub>*이라 하고 $\bigcap\_{i\in I}A\_i$로 적는다.

</div>

합집합과는 다르게 $I$가 공집합이 아니라는 조건이 추가되었다. 그 이유는 교집합의 정의를 찬찬히 살펴보면 알 수 있다. 교집합은 논리식

$$\forall i(i\in I\implies x\in A_i)$$

를 만족하는 $x$들의 모임이다. 만일 $I=\emptyset$이라면 $i\in I$가 거짓이 되어 전체 문장이 $x$에 관계없이 참이 되고 $\bigcap\_{i\in\emptyset} A\_i$는 전체집합이 되어야 하므로 모순이다. ([§ZFC 공리계, 예시 4](/ko/math/set_theory/zfc_axioms#ex4))

대신 target $\mathcal{P}(A)$가 정의된다면 사정이 좀 달라진다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> 집합들의 family $(A\_i)\_{i\in I}$가 집합 $A$의 부분집합들의 family라 하자. 그럼 <phrase>$A$의 원소이면서 동시에 모든 $A_i$에 속해있는 $x$들의 집합</phrase>을 이 family의 *교집합*이라 부르며, $\bigcap\_{i\in I}A\_i$로 적는다.

</div>

이번에는 만일 $I=\emptyset$이더라도 조건이 

$$(x\in A)\wedge (\forall i(i\in I\implies x\in A_i))$$

이 되므로 $\bigcap\_{i\in I} A\_i=A$가 될 것이다. 

편의상, 앞으로 교집합의 index set은 항상 공집합이 아닌 것으로 가정한다. 그러나 index set이 공집합인 경우에도 위와 같이 $a$의 target을 적절히 잡아줄 수 있는 경우, 명제는 index set이 공집합인 경우에도 성립한다. 

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $(A\_i)\_{i\in I}$가 집합들의 family라 하고, $f:K\rightarrow I$가 전사함수라 하자. 그럼 다음의 두 식

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

임은 자명하다. 굳이 증명하자면, 

- 임의의 $y\in\bigcup\_{i\in I}B\_i$가 주어졌다면 어떤 $i\_0\in I$에 대해 $y\in B\_{i\_0}$이고, 가정에 의해 $B\_{i\_0}\subseteq A\_{i\_0}$이므로 $y\in A\_{i\_0}$가 되어 $y\in\bigcup A\_i$가 성립하며, 
- 임의의 $y\in\bigcap B\_i$가 주어졌다면, 모든 $i$에 대해 $y\in B\_i$이고, $B\_i\subseteq A\_i$이므로 모든 $i$에 대해 $y\in A\_i$가 되므로 $y\in\bigcap A\_i$이다. 

또, 주어진 family $(A\_i)\_{i\in I}$와 $I$의 부분집합 $J$에 대하여, 

$$\bigcup_{j\in J}A_j\subset\bigcup_{i\in I} A_i,\qquad\bigcap_{j\in J}A_j\supset\bigcap_{i\in I} A_i$$

임도 거의 자명하다. 첫 번째 식의 경우, 만일 $x\in \bigcup\_{j\in J} A\_j$라면 어떠한 $j\in J$에 대해 $x\in A\_j$이고, 이 때 $j$는 $I$의 원소이기도 하므로 $x\in\bigcup\_{i\in I} A\_i$가 된다. 

두 번째 식의 경우, <phrase>$I$의 모든 원소 $i$에 대해 $A_i$의 원소일 것</phrase>이라는 조건이 <phrase>$J$의 모든 원소 $j$에 대해 $A_j$의 원소일 것</phrase>이라는 조건보다 만족해야 할 조건이 더 많으므로, 이를 모두 만족하는 원소는 더 적을 수밖에 없다. 물론 엄밀하게 증명할 수도 있는데, 만일 $x\in\bigcap\_{i\in I} A\_i$라면, 모든 $i\in I$에 대해 $x\in A\_i$이고, 그럼 모든 $j\in J$에 대해 $x\in A\_j$이기도 하므로 $x\in\bigcap\_{j\in J} A\_j$여야 한다. 

한편, 집합의 연산들에도 결합법칙이 성립한다.

<div class="proposition" markdown="1">

<ins id="df5">**명제 5**</ins>  $(A\_i)\_{i\in I}$가 집합들의 family고, index set $I$가 family $(J\_k)\_{k\in K}$들의 합집합이라 하자. 그럼

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

또, 우리는 다음과 같이 합집합/교집합과 correspondence의 image와의 관계도 생각해 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins>  $(A\_i)\_{i\in I}$가 집합 $A$의 부분집합의 family고 $\Gamma$가 $A$에서 $B$로의 correspondence라 하자. 그럼

$$\Gamma\left(\bigcup_{i\in I} A_i\right)=\bigcup_{i\in I}\Gamma(A_i),\quad \Gamma\left(\bigcap_{i\in I} A_i\right)\subset\bigcap_{i\in I}\Gamma(A_i)$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 식을 보이자. 만일 $y\in \Gamma\left(\bigcup\_{i\in I}A_i\right)$라면, 적당한 $x\in \bigcup\_{i\in I}A_i$가 존재하여 $(x,y)\in \Gamma$이다. 이제 $x\in A_j$라 하면 $y\in \Gamma(A_j)$이므로 $y\in\bigcup\_{i\in I}\Gamma\left(A_i\right)$가 성립한다. 반대로 만일 $y\in \bigcup\_{i\in I}\Gamma\left(A_i\right)$라면 어떤 $j$에 대하여 $y\in \Gamma\left(A\_j\right)$이므로, 적당한 $x\in A\_j$가 존재하여 $(x,y)\in\Gamma$이다. 따라서 $y\in\Gamma\left(\bigcup\_{i\in I} A\_i\right)$가 성립한다.

두 번째 식은 한쪽 방향만 보이면 충분하다. $y\in\Gamma\left(\bigcap\_{i\in I}A\_i\right)$라 하자. 그럼 어떤 $x\in\bigcap\_{i\in I}A\_i$가 존재하여 $(x,y)\in \Gamma$이다. $x$는 모든 $A\_i$에 속하므로, 우리는 $(x,y)\in\Gamma(A\_i)$가 모든 $A\_i$에 대해 성립하는 것을 안다. 즉 $y\in \bigcap\_{i\in I}\Gamma\left(A\_i\right)$이다.
</details>

위의 명제의 두 번째 식의 반대쪽 포함관계는 일반적으로 성립하지 않는다. 예를 들어, $\mathbb{R}$에서 $\mathbb{R}$로의 함수 $f(x)=x^2$과 두 개의 구간 $I_1=(1,2)$, $I_2=(-2,-1)$을 생각하자. $I\_1\cap I\_2=\emptyset$이므로 $f(\bigcap\_{i=1,2}I\_i)=\emptyset$이다. 그러나 모든 $i$에 대하여 $f(A\_i)=(1,4)$이므로 $\bigcap\_{i\in I}f(A\_i)=(1,4)$이다. 

대신, $\Gamma$가 어떤 함수의 그래프의 역이라면 등호가 성립한다.

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins>  $f:A\rightarrow B$가 함수라 하고 $(B\_i)\_{i\in I}$가 $B$의 부분집합들의 family라 하자. 그럼 
  
  $$f^{-1}\left(\bigcap_{i\in I} B_i\right)=\bigcap_{i\in I} f^{-1}(B_i)$$

가 성립한다. 
</div>

<details class="proof--alone" markdown="1">
<summary>증명</summary>

한쪽 포함관계는 더 일반적인 경우에서 증명하였으므로, 반대쪽 포함관계만 증명하면 충분하다. 

함수 $f$의 그래프를 $F$라 하고, $x\in\bigcap\_{i\in I} f^{-1}(B\_i)$가 주어졌다 하자. 그럼 모든 $i$에 대하여 $x\in f^{-1}(B_i)$이다. 즉, 모든 $i$에 대해 $(x,y\_i)\in F$이도록 하는 $y\_i\in B\_i$가 존재한다. 그런데 $F$는 functional이므로 그러한 $y\_i$는 유일하다. 이 공통된 값을 $y$라 하면 모든 $i\in I$에 대해 $y\in B\_i$이므로 $y\in\bigcap\_{i\in I} B\_i$이고, 따라서 $f(x)=y$에서 $x\in f^{-1}\left(\bigcap\_{i\in I} B\_i\right)$이다.
</details>

위의 조건에서 $f$가 함수임은 $(x,y\_i)\in F$이면 $y\_i$가 모두 같음을 보이기 위해 사용되었다. 따라서 만일 $f$가 단사함수라면 마찬가지 방법으로

$$f\left(\bigcap_{i\in I} A_i\right)=\bigcap_{i\in I} f(A_i)$$

임을 얻을 수 있다. 

다음은 우리가 흔히 드모르간의 법칙 (De Morgan's law)라고 불렀던 등식의 일반화된 버전이다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8 (De Morgan's law)**</ins> 집합 $A$의 부분집합들의 Family $(A\_i)\_{i\in I}$에 대하여, 
  
$$A\setminus \left(\bigcup_{i\in I}A_i\right)=\bigcap_{i\in I}(A\setminus A_i),\quad A\setminus\left(\bigcap_{i\in I} A_i\right)=\bigcup_{i\in I} (A\setminus A_i)$$

가 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>
첫 번째 식을 보이기 위해 우선 $x\in A\setminus\left(\bigcup\_{i\in I} A\_i\right)$라 하자. 그럼 $x\in A$이고 $x\not\in\left(\bigcup\_{i\in I} A\_i\right)$이다. 따라서 모든 $i$에 대하여 $x\not\in A_i$이므로, $x\in (A\setminus A_i)$가 모든 $i$에 대하여 성립한다. 즉 $x\in\bigcap\_{i\in I}(A\setminus A\_i)$이다.  
반대로 만일 $x\in\bigcap\_{i\in I} (A\setminus A\_i)$라면, 임의의 $i\in I$에 대하여 $x\in A\setminus A_i$이고, 따라서 모든 $i\in I$에 대하여 $x\not\in A\_i$이다. 이제 $x\not\in\bigcup\_{i\in I} A\_i$이므로 $x\in A\setminus\bigcup\_{i\in I} A_i$이다.

두 번째 식은 등식 $A\setminus(A\setminus X)=X$가 모든 $X\subseteq A$에 대해 성립하므로 첫 번째 식으로부터 자명.
</details>

만약 $A$를 전체집합처럼 취급한다면, 이 식은 우리가 원래 알던 $(\bigcup A_i)^c=\bigcap A_i^c$, 그리고 $(\bigcap A_i)^c=\bigcup A_i^c$으로 쓸 수도 있다. 



---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---

[^1]: 앞에서 $a$의 그래프를 나타낼 때 이미 문자 $A$를 사용하였지만, 표기법의 깔끔함을 위해 $A_i$를 포함하는 집합도 $A$로 두었다. $a$의 그래프는 사용할 일이 없으므로, 앞으로도 $A$는 $a$의 그래프가 아니라 그냥 집합이다.