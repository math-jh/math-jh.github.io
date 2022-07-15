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

우리는 앞서 binary relation을 소개할 때, function, equivalence relation, order relation의 세 가지가 앞으로 살펴 볼 가장 중요한 주제들이라고 이야기한 적이 있다. 지난 글에서 함수에 대한 내용은 살펴봤으니 다음 차례는 equivalence relation인데, 그 전에 우선 집합 사이의 연산을 먼저 살펴볼 필요가 있다. 내용이 워낙 많아 여러 부분으로 쪼개어져 있다.

우리는 앞서 함수 $f$를 $f(x)$ 대신 $f_x$와 같이 쓰기도 하고, 이 경우는 그래프 $F$를 *family*, 그 정의역을 *index set*이라 부르기도 한다고 했었다. Index set $I$가 주어졌고, 각각의 $i\in I$마다 집합 $X_i$가 대응되는 family가 있다고 하자. 이러한 family는 $(X_i)_{i\in I}$로 적는 것이 일반적이다. 

<div class="remark" markdown="1">

<ins id="rmk">**참고**</ins>  이 표기는 고등학교 때 사용하던 수열의 표기 $(a\_n)\_{n\in\mathbb{N}}$을 떠올리게 하는데, 수열이라는 것이 정의역이 $\mathbb{N}$인 함수이듯 $(X\_i)\_{i\in I}$을 수열의 일반화라고 볼 수도 있다. 

유한개의 대상들을 다룰 때 가장 좋은 것은 첫 번째 좌표, 두 번째 좌표, ... $n$번째 좌표로 이루어진 순서쌍이다. 그런데 이를 잘 생각해보면 순서쌍이라는 것은  

> $i$라는 숫자를 넣으면 $i$번째 좌표에 해당하는 값을 돌려주는 함수  

라고 볼 수 있다. 예컨대, 1을 넣으면 첫 번째 좌표, 3을 넣으면 세 번째 좌표... 등을 돌려주는 함수인 것이다. 따라서 무한개의 대상을 다룰 때 가장 자연스러운 확장은 무한수열 $\\{a\_n\\}\_{n\in\mathbb{N}}$일 것이며, 우리가 "더 큰" 무한대를 다룬다면 그에 해당하는 집합을 정의역으로 갖는 함수를 이용할 수 있을 것이다. 

이러한 관점에서 볼 때, 위의 표기 $(X\_i)\_{i\in I}$는

> $i$라는 index를 넣으면 $i$에 해당하는 집합 $X_i$를 돌려주는 함수

라고 생각할 수 있다.

</div>

어떤 상황에서는 family $(X\_i)\_{i\in I}$의 모든 원소들이 특정한 집합 $E$의 부분집합일 수 있다. 즉, 함수로서 이 family의 target이 $\mathcal{P}(E)$일 수 있다. 대부분의 경우는 이러한 조건의 유무가 큰 차이를 보이지 않으므로 이 경우 또한 target을 특정하여 $(X,I,\mathcal{P}(E))$로 쓰는 대신 그냥 $(X\_i)\_{i\in I}$로 적는다. 다만 이 차이가 두드러지는 몇몇 경우들이 있다. ([정의 2](#df2)와 [정의 3](#df3))

## 합집합과 교집합

우리는 합집합이 존재한다는 것을 공리로 채택했었는데 ([§ZFC 공리계](/ko/math/set_theory/zfc_axioms)의 Axiom of union), 그 때 사용한 표기법은 공리적 집합론에서 주로 쓰이고, 사실 대부분의 분야에서는 다음의 표기법이 좀 더 자주 쓰인다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> $(X\_i)\_{i\in I}$가 집합들의 family라 하자. 그럼 <box>적어도 하나의 $X_i$에 속해있는 $x$들을 모두 모아둔 집합</box>을 이 family의 *합집합<sub>union</sub>*이라 하고, 이를 $\bigcup\_{i\in I}X\_i$로 적는다.

</div>

즉 합집합은 논리식

$$\exists i(i\in I\wedge x\in X_i)$$

를 만족하는 $x$들의 집합이다. 따라서 $I=\emptyset$이라면 $\bigcup\_{i\in I} X\_i=\emptyset$이다. 만일 $X_i$들이 모두 $E$의 부분집합이었다 하더라도, 합집합은 target $\mathcal{P}(E)$에 영향을 받지 않으므로[^1] target을 굳이 명시할 필요가 없다. 반면 교집합은 이 둘 사이에 미묘한 차이가 생긴다.

<div class="definition" markdown="1">

<ins id="df2">**정의 2**</ins> $(X\_i)\_{i\in I}$가 집합들의 family이고, $I$가 공집합이 아니라 하자. 그럼 <box>모든 $X_i$에 속해있는 $x$들의 집합</box>을 이 family의 *교집합<sub>intersection</sub>*이라 하고 $\bigcap\_{i\in I}X\_i$로 적는다.

</div>

합집합과는 다르게 $I$가 공집합이 아니라는 조건이 추가되었다. 그 이유는 교집합의 정의를 찬찬히 살펴보면 알 수 있다. 교집합은 논리식

$$\forall i(i\in I\implies x\in X_i)$$

를 만족하는 $x$들의 모임인데, 만일 $I=\emptyset$이라면 $i\in I$가 거짓이 되어 전체 문장이 $x$에 관계없이 참이 되기 때문이다. 즉 $\bigcap\_{i\in\emptyset} X\_i$는 전체집합이 되어야 하는데, 이러한 집합은 존재하지 않음을 이미 알고 있다. ([§ZFC 공리계, 예시 4](/ko/math/set_theory/zfc_axioms#ex4))

대신 target $E$가 정의된다면 사정이 좀 달라진다.

<div class="definition" markdown="1">

<ins id="df3">**정의 3**</ins> $(X, I, \mathcal{P}(E))$가 집합 $E$의 부분집합들의 family라 하자. 그럼 <box>$E$의 원소이면서 동시에 모든 $X_i$에 속해있는 $x$들의 집합</box>을 이 family의 *교집합*이라 부르며, $\bigcap\_{i\in I}X\_i$로 적는다.

</div>

이번에는 만일 $I=\emptyset$이더라도 조건이 

$$(x\in E)\wedge (\forall i(i\in I\implies x\in X_i))$$

이 되므로 $\bigcap\_{i\in I} X\_i=E$가 될 것이다. 하지만 이렇게 index set이 공집합인 경우만 제외하면 $\bigcap\_{i\in I} X\_i$ 또한 target $E$의 영향을 받지 않으므로, 앞으로는 family가 $E$의 부분집합들을 target으로 삼는지 아닌지는 신경쓰지 않기로 한다.

<div class="proposition" markdown="1">

<ins id="pp4">**명제 4**</ins> $(X\_i)\_{i\in I}$가 집합들의 family라 하고, $f:K\rightarrow I$가 index set들 사이의 surjection이라 하자. 그럼

$$\bigcup_{k\in K}X_{f(k)}=\bigcup_{i\in I}X_i$$ 

가 성립하며, $I\neq\emptyset$일 경우[^2]

$$\bigcap_{k\in K}X_{f(k)}=\bigcap_{i\in I} X_i$$

가 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>
우선 첫 번째 식을 보이기 위해, $x\in\bigcup\_{i\in I} X\_i$라 하자. 정의에 의해, 이건 어떤 $i\in I$에 대하여 $x\in X_i$라는 뜻이다. 그런데, $f$는 surjection이므로 어떤 $k\in K$가 존재하여 $i=f(k)$이고, 따라서 $x\in X\_{f(k)}$이므로 $x\in\bigcup\_{k\in K}X\_{f(k)}$이다.  
반대로, 만일 $x\in\bigcup\_{k\in K}X\_{f(k)}$가 성립한다면, 어떤 $k\in K$에 대하여 $x\in X\_{f(k)}$이다. 그런데 $f(k)\in I$이므로, $X\_{f(k)}$는 $(X_i)\_{i\in I}$를 구성하는 집합 중 하나이고 따라서 어떤 $i$에 대해 $x\in X_i$이다.

이제 두 번째 식을 보여야 한다. 우선 $x\in\bigcap\_{i\in I}X\_i$라 하자. 그럼 모든 $i\in I$에 대하여 $x\in X\_i$이다. 임의의 $k\in K$에 대하여 $f(k)\in I$이므로, 모든 $k\in K$에 대하여 $x\in X\_{f(k)}$이고 따라서 $x\in \bigcap\_{k\in K}X\_{f(k)}$이다.  
반대로 만일 모든 $k\in K$에 대하여 $x\in X\_{f(k)}$라면, $f$는 surjective하므로 모든 $i\in I$에 대해 $x\in X\_{f(k)}$이다.  
</details>

Family $(X\_k)\_{k\in K}$가 임의의 $k,k'$에 대하여 $X\_k=X\_{k'}$를 만족한다고 하자. 임의의 $i\in K$를 하나 택하여 $f:K\rightarrow \\{i\\}$로 정의되는 surjection을 생각하고 위의 정리를 적용하면, 항상 $X_k=X_i=X_{f(k)}$이므로

$$\bigcup_{k\in K} X_k=\bigcup_{j\in\{i\}}X_j=X_i,\qquad \bigcap_{k\in K}X_k=\bigcap_{j\in \{i\}}X_j=X_i$$

가 성립한다.

이제 합집합과 교집합의 성질들을 조금 더 살펴보자. 만일 같은 index를 갖는 두 family $(X\_i)\_{i\in I}$와 $(Y\_i)\_{i\in I}$가 주어지고, $Y_i\subset X_i$가 모든 $i\in I$에 대해 성립한다면 

$$\bigcup_{i\in I} Y_i\subset\bigcup_{i\in I} X_i,\qquad \bigcap_{i\in I} Y_i\subset\bigcap_{i\in I} X_i$$

임은 자명하다. 굳이 증명하자면, 

- 임의의 $y\in\bigcup\_{i\in I}Y\_i$가 주어졌다면 어떤 $i$에 대해 $y\in Y\_i$이고, 이 $i$에 대해 $Y\_i\subset X\_i$이므로 $y\in X\_i$가 되어 $y\in\bigcup X\_i$가 성립하며, 
- 임의의 $y\in\bigcap Y\_i$가 주어졌다면, 모든 $i$에 대해 $y\in Y\_i$이고, $Y\_i\subset X\_i$이므로 모든 $i$에 대해 $y\in X\_i$가 되므로 $y\in\bigcap X\_i$이다. 

또, 주어진 family $(X\_i)\_{i\in I}$와 $I$의 부분집합 $J$에 대하여, 

$$\bigcup_{j\in J}X_j\subset\bigcup_{i\in I} X_i,\qquad\bigcap_{j\in J}X_j\supset\bigcap_{i\in I} X_i$$

임도 거의 자명하다. 만일 $x\in \bigcup\_{j\in J} X\_j$라면, 어떠한 $j\in J$에 대해 $x\in X\_j$이고, 이 때 $j$는 $I$의 원소이기도 하므로 $x\in\bigcup\_{i\in I} X\_i$가 된다. 두 번째 식은 inclusion-reversing이라는 것에 주의해야 하는데, 곰곰히 생각해보면 당연한 일이다. <box>$I$의 모든 원소 $i$에 대해 $X_i$의 원소일 것</box>이라는 조건이 <box>$J$의 모든 원소 $j$에 대해 $X_j$의 원소일 것</box>이라는 조건보다 만족해야 할 조건이 더 많으므로, 이를 모두 만족하는 원소는 더 적을 수밖에 없다. 엄밀하게 쓰자면, 만일 $x\in\bigcap\_{i\in I} X\_i$라면, 모든 $i\in I$에 대해 $x\in X\_i$이고, 그럼 모든 $j\in J$에 대해 $x\in X\_j$이기도 하므로 $x\in\bigcap\_{j\in J} X\_j$여야 한다. 

한편, 집합의 연산들에도 결합법칙이 성립한다.

<div class="proposition" markdown="1">
<ins id="df5">**명제 5**</ins>  $(X\_i)\_{i\in I}$가 집합들의 family고, index set $I$가 family $(J\_k)\_{k\in K}$들의 합집합이라 하자. 그럼

$$\bigcup_{i\in I} X_i=\bigcup_{k\in K}\left(\bigcup_{j\in J_k} X_j\right),\quad \bigcap_{i\in I}X_i=\bigcap_{k\in K}\left(\bigcap_{j\in J_k} X_j\right)$$

가 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>
우선 합집합에 관한 식부터 보이자. 만일 $x\in \bigcup\_{i\in I}X\_i$라면, 어떠한 $i'\in I$에 대하여 $x\in X\_{i'}$이다. 이제 $I=\bigcup\_{k\in K} J\_k$이므로, 어떤 $k'$가 존재하여 $i'\in J\_{k'}$이다. 그럼

$$X_{i'}=\bigcup_{i\in \{i'\}}X_i\subset\bigcup_{j\in J_{k'}} X_j=\bigcup_{k\in\left\{k'\right\}}\left(\bigcup_{i\in J_k} X_i\right)\subset \bigcup_{k\in K}\left(\bigcup_{j\in J_k} X_j\right)$$

이므로 $x\in X\_{i'}\subset \bigcup\_{k\in K}\left(\bigcup\_{j\in J_k} X\_j\right)$이다.  
반대로 만일 $x\in \bigcup\_{k\in K}\left(\bigcup\_{j\in J_k} X_j\right)$이라면, 어떠한 $k'\in K$에 대하여 $x\in \bigcup\_{j\in J\_{k'}}X\_j$이고, 따라서 다시 어떤 $i'\in J\_{k'}$에 대하여 $x\in X\_{i'}$이다. 이제 $i'\in I$이므로 $x\in\bigcup\_{i\in I} X\_i$이다. 

이와 비슷하게 두 번째 식도 보일 수 있다. 만일 $x\in\bigcap\_{i\in I} X\_i$라면, 모든 $i\in I$에 대하여 $x\in X\_i$이다. 임의의 $k'\in K$에 대하여, $J\_{k'}\subset I$이므로, 모든 $i\in I$에 대하여 위의 식이 성립한다는 말은 모든 $j\in J\_{k'}$에 대하여 $x\in X\_j$가 성립한다는 말이기도 하다. 임의로 선택된 $k'$에 대하여 이것이 성립하므로, 이는 정확히 $x\in\bigcap\_{k\in K}\left(\bigcap\_{j\in J\_{k}}X_j\right)$를 의미한다.
</details>

또, 우리는 다음과 같이 합집합/교집합과 correspondence의 image와의 관계도 생각해 볼 수 있다.

<div class="proposition" markdown="1">

<ins id="pp6">**명제 6**</ins>  $(X\_i)\_{i\in I}$가 집합 $A$의 부분집합의 family고 $\Gamma$가 $A$에서 $B$로의 correspondence라 하자. 그럼

$$\Gamma\left(\bigcup_{i\in I} X_i\right)=\bigcup_{i\in I}\Gamma(X_i),\quad \Gamma\left(\bigcap_{i\in I} X_i\right)\subset\bigcap_{i\in I}\Gamma(X_i)$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫 번째 식을 보이자. 만일 $y\in \Gamma\left(\bigcup\_{i\in I}X_i\right)$라면, 적당한 $x\in \bigcup\_{i\in I}X_i$가 존재하여 $(x,y)\in \Gamma$이다. 이제 $x\in X_j$라 하면 $y\in \Gamma(X_j)$이므로 $y\in\bigcup\_{i\in I}\Gamma\left(X_i\right)$가 성립한다. 반대로 만일 $y\in \bigcup\_{i\in I}\Gamma\left(X_i\right)$라면 어떤 $j$에 대하여 $y\in \Gamma\left(X\_j\right)$이므로, 적당한 $x\in X\_j$가 존재하여 $(x,y)\in\Gamma$이다. 따라서 $y\in\Gamma\left(\bigcup\_{i\in I} X\_i\right)$가 성립한다.

두 번째 식은 한쪽 방향만 보이면 충분하다. $y\in\Gamma\left(\bigcap\_{i\in I}X\_i\right)$라 하자. 그럼 어떤 $x\in\bigcap\_{i\in I}X\_i$가 존재하여 $(x,y)\in \Gamma$이다. $x$는 모든 $X\_i$에 속하므로, 우리는 $(x,y)\in\Gamma(X\_i)$가 모든 $X\_i$에 대해 성립하는 것을 안다. 즉 $y\in \bigcap\_{i\in I}\Gamma\left(X\_i\right)$이다.
</details>

위의 명제의 두 번째 식의 반대쪽 포함관계는 일반적으로 성립하지 않는다. 예를 들어, $\mathbb{R}$에서 $\mathbb{R}$로의 함수 $f(x)=x^2$과 두 개의 구간 $I_1=(1,2)$, $I_2=(-2,-1)$을 생각하자. $I\_1\cap I\_2=\emptyset$이므로 $f(\bigcap\_{i=1,2}I\_i)=\emptyset$이다. 그러나 모든 $i$에 대하여 $f(X\_i)=(1,4)$이므로 $\bigcap\_{i\in I}f(X\_i)=(1,4)$이다. 

대신, $\Gamma$가 어떤 함수의 그래프의 inverse라면 등호가 성립한다.[^3]

<div class="proposition" markdown="1">

<ins id="pp7">**명제 7**</ins>  $f:A\rightarrow B$가 함수라 하고 $(Y\_i)\_{i\in I}$가 $B$의 부분집합들의 family라 하자. 그럼 
  
  $$F^{-1}\left(\bigcap_{i\in I} Y_i\right)=\bigcap_{i\in I} F^{-1}(Y_i)$$

가 성립한다. 
</div>

여기서 $F$는 $f$의 그래프이고, 따라서 $F^{-1}$은 $f$가 bijection이 아니더라도 잘 정의된다. 

<details class="proof--alone" markdown="1">
<summary>증명</summary>
한쪽 포함관계는 더 일반적인 경우에서 증명하였으므로, 반대쪽 포함관계만 증명하면 충분하다. 

$x\in\bigcap\_{i\in I} F^{-1}(Y\_i)$라 하자. 그럼 모든 $i$에 대하여 $x\in F^{-1}(Y_i)$이다. 즉, 모든 $i$에 대해 $(x,y\_i)\in F$이도록 하는 $y\_i\in Y\_i$가 존재한다. 그런데 $F$는 functional이므로 그러한 $y\_i$는 유일하다. 이 공통된 값을 $y$라 하면 모든 $i\in I$에 대해 $y\in Y\_i$이므로 $y\in\bigcap\_{i\in I} Y\_i$이고, 따라서 $f(x)=y$에서 $x\in F^{-1}\left(\bigcap\_{i\in I} Y\_i\right)$이다.
</details>

위의 조건에서 $f$가 함수임은 $(x,y\_i)\in F$이면 $y\_i$가 모두 같음을 보이기 위해 사용되었다. 따라서 만일 $f$가 injective라면 마찬가지 방법으로

$$f\left(\bigcap_{i\in I} X_i\right)=\bigcap_{i\in I} f(X_i)$$

임을 얻을 수 있다. 

다음은 우리가 흔히 드모르간의 법칙 (De Morgan's law)라고 불렀던 등식의 일반화된 버전이다.

<div class="proposition" markdown="1">

<ins id="pp8">**명제 8 (De Morgan's law)**</ins> 집합 $E$의 부분집합들의 Family $(X\_i)\_{i\in I}$에 대하여, 
  
$$E\setminus \left(\bigcup_{i\in I}X_i\right)=\bigcap_{i\in I}(E\setminus X_i),\quad E\setminus\left(\bigcap_{i\in I} X_i\right)=\bigcup_{i\in I} (E\setminus X_i)$$

가 성립한다.
</div>
<details class="proof" markdown="1">
<summary>증명</summary>
첫 번째 식을 보이기 위해 우선 $x\in E\setminus\left(\bigcup\_{i\in I} X\_i\right)$라 하자. 그럼 $x\in E$이고 $x\not\in\left(\bigcup\_{i\in I} X\_i\right)$이다. 따라서 모든 $i$에 대하여 $x\not\in X_i$이므로, $x\in (E\setminus X_i)$가 모든 $i$에 대하여 성립한다. 즉 $x\in\bigcap\_{i\in I}(E\setminus X\_i)$이다.  
반대로 만일 $x\in\bigcap\_{i\in I} (E\setminus X\_i)$라면, 임의의 $i\in I$에 대하여 $x\in E\setminus X_i$이고, 따라서 모든 $i\in I$에 대하여 $x\not\in X\_i$이다. 이제 $x\not\in\bigcup\_{i\in I} X\_i$이므로 $x\in E\setminus\bigcup\_{i\in I} X_i$이다.

두 번째 식은 등식 $E\setminus(E\setminus X)=X$가 모든 $X\subset E$에 대해 성립하므로 첫 번째 식으로부터 자명.
</details>

만약 $E$를 전체집합처럼 취급한다면, 이 식은 우리가 원래 알던 $(\bigcup X_i)^c=\bigcap X_i^c$, 그리고 $(\bigcap X_i)^c=\bigcup X_i^c$으로 쓸 수도 있다. 



---
**참고문헌**

**[Bou]** N. Bourbaki, <i>Theory of Sets</i>. Elements of mathematics. Springer Berlin-Heidelberg, 2013.

---


[^1]: 예를 들어, $E\subset F$인 $F$에 대하여 $X\_i$를 $(X,I,\mathcal{P}(E))$로 보든 $(X, I, \mathcal{P}(F))$로 보든 결과는 동일하다.
[^2]: 물론 $I\neq\emptyset$으로 둔 것은 $\bigcap\_{i\in I} X\_i$가 잘 정의되기 위한 것이다. 만일 $X_i$가 어떤 집합 $E$의 부분집합들의 family라면 $I$가 공집합인 것도 허용되며, 그 때도 동일한 명제가 성립하긴 하지만 그 경우를 직접 계산해보면 별로 의미 없는 주장이 나온다. ($E=E$) 앞으로 나올 교집합에 대한 명제들에 대해서도 이는 마찬가지이다.
[^3]: 이런 성질이 함수가 아니라 함수의 preimage에 대해 성립하는 것은 어색해보이지만, 다른 분야들에서도 공통적으로 나타난다. 예를 들어 prime ideal의 homomorphic image는 prime ideal일 필요가 없지만 preimage는 prime ideal이 되고, open set의 continuous image는 open일 필요가 없지만 preimage는 open이다.  
