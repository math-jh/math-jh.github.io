---

title: "대수적 집합"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/algebraic_sets
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Algebraic_sets.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-06
last_modified_at: 2024-11-06
weight: 1

---

처음 몇 개의 글에서 우리는 고전적인 대수기하학에 대해 살펴본다. 이는 본격적으로 scheme을 다루기 전에 우리에게 충분한 motivation을 준다. 

## 아핀 공간

임의의 algebraically closed field $\mathbb{k}$를 고정하자. 그럼 다음 집합

$$\mathbb{A}^n_\mathbb{k}=\{(a_1,\ldots, a_n): a_i\in \mathbb{k}\}$$

을 *affine $n$-space<sub>아핀 $n$-공간</sub>*이라 부른다. 문맥에 따라 $\mathbb{k}$가 명확할 경우는 이를 간단히 $\mathbb{A}^n$으로만 적기로 한다.

그럼 임의의 다항식 $f(\x_1,\ldots,\x_n)\in \mathbb{k}[\x_1,\ldots,\x_n]$에 대하여, 다음의 부분집합

$$Z(f)=\{(x_1,\ldots, x_n)\in \mathbb{A}^n: f(x_1,\ldots, x_n)=0\}$$

을 $f$의 *zero set<sub>영점</sub>*이라 부른다. 더 일반적으로, 임의의 다항식들의 모임 $I=(f\_i)\subseteq \mathbb{k}[\x_1,\ldots,\x_n]$에 대하여 이들 모두를 $0$으로 만드는 $\mathbb{A}^n$의 점들의 모임을 $Z(I)$로 적는다. 그럼 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 임의의 다항식들의 모임 $I=(f\_i)$에 의해 생성되는 $\mathbb{k}[\x_1,\ldots,\x_n]$의 ideal을 $\mathfrak{a}$라 하면, $Z(I)=Z(\mathfrak{a})$가 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

포함관계 $I\subseteq \mathfrak{a}$로부터 $Z(\mathfrak{a})\subseteq Z(I)$임은 자명하다. 한편 $\mathfrak{a}$의 임의의 원소는

$$f=\sum_{i\in I} q_if_i,\qquad \text{$q_i=0$ for all but finitely many $i$}$$

으로 적을 수 있고, $Z(I)$의 정의에 의하여 임의의 $(x_1,\ldots, x_n)\in Z(I)$에 대해 $f_i(x_1,\ldots, x_n)=0$이 성립하므로 $f(x_1,\ldots, x_n)=0$ 또한 성립한다. 즉 $(x_1,\ldots, x_n)\in Z(\mathfrak{a})$이다.

</details>

한편, 그 이름이 시사하는 바와 같이 $\mathbb{A}^n$은 단순한 집합이 아니라, 공간으로서 그 위에 정의된 위상공간을 갖는다. 이를 위해서는 closed set이 무엇인지를 정의해주면 충분하다. ([\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2))

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $	\mathbb{A}^n$의 *닫힌집합*은 $\mathbb{k}[\x_1,\ldots,\x_n]$의 적당한 ideal $\mathfrak{a}$에 대해 $Z(\mathfrak{a})$ 꼴로 나타나는 집합을 의미한다.  이렇게 정의되는 $\mathbb{A}^n$의 위상구조를 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다.

</div>

이렇게 정의한 닫힌집합들이 [\[위상수학\] §집합의 내부, 폐포, 경계, ⁋명제 2](/ko/math/topology/other_concepts#prop2)의 조건들을 만족한다는 것을 증명해야 한다. 이는 다음 명제를 통해 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $\mathbb{k}[\x_1,\ldots,\x_n]$의 임의의 ideal들의 모임 $(\mathfrak{a}\_i)\_{i\in I}$에 대하여, 다음 식

$$Z\left(\sum_{i\in I} \mathfrak{a}_i\right)=\bigcap_{i\in I} Z(\mathfrak{a}_i)$$

이 성립한다. 또, $\mathbb{k}[\x_1,\ldots,\x_n]$의 두 ideal $\mathfrak{a}\_1,\mathfrak{a}\_2$에 대하여, 다음 식

$$Z\left(\mathfrak{a}_1 \mathfrak{a}_2\right)=Z(\mathfrak{a}_1)\cup Z(\mathfrak{a}_2)$$

이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫째 식을 증명하자. 만일 $x\in Z\left(\sum\_{i\in I} \mathfrak{a}\_i\right)$라면 임의의 $f\in \sum\_{i\in I} \mathfrak{a}\_i$에 대하여 $f(x)=0$이어야 하고, 따라서 임의의 $\mathfrak{a}\_i$의 원소에 대해서도 $x$에서의 함숫값을 계산하면 $0$이 되어야 한다. 이로부터 $Z\left(\sum\_{i\in I} \mathfrak{a}\_i\right)\subseteq \bigcap\_{i\in I} Z(\mathfrak{a}\_i)$임을 안다.  
반대로 $x\in \bigcap\_{i\in I} Z(\mathfrak{a}\_i)$라 하면, $\sum \mathfrak{a}\_i$의 임의의 원소는 $\mathfrak{a}_i$들의 원소들의 유한한 합으로 나타나고, 정의에 의해 이 합에 등장하는 모든 항의 $x$에서의 함숫값은 $0$이므로 원하는 등식을 얻는다.

둘째 등식의 경우, 우선 포함관계 $\mathfrak{a}_1 \mathfrak{a}_2\subseteq \mathfrak{a}_1, \mathfrak{a}_2$으로부터 $Z(\mathfrak{a}_1)\cup Z(\mathfrak{a}_2)\subseteq Z(\mathfrak{a}_1 \mathfrak{a}_2)$를 얻는다. 반대방향을 보이기 위해 $x\in Z(\mathfrak{a}_1 \mathfrak{a}_2)$라 하자. 만일 $x\not\in Z(\mathfrak{a}\_1)$이라면, $f(x)\neq 0$이도록 하는 $f\in \mathfrak{a}\_1$을 잡을 수 있다. 이제 임의의 $g\in \mathfrak{a}\_2$에 대하여, $fg\in \mathfrak{a}\_1 \mathfrak{a}\_2$이므로 특히 $x$에서의 함숫값을 계산하면 $f(x)g(x)=0$이어야 한다. 이제 $f(x)\neq 0$인 것으로부터 $g(x)=0$이어야 하고, $g$는 $\mathfrak{a}\_2$의 임의의 원소이므로 $x\in Z(\mathfrak{a}_2)$가 성립한다. 

</details>

편의상 $\mathbb{A}^n$의 닫힌집합을 *algebraic set<sub>대수적 집합</sub>*이라 부르기도 한다. 

## 정칙사상

이제 우리는 algebraic set $X$ 위에 정의된 함수들에 대해 살펴본다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Algebraic set $X\subseteq \mathbb{A}^n$ 위에 정의된 함수 $f$가 *regular function<sub>정칙함수</sub>*이라는 것은 적당한 다항식 $F\in \mathbb{k}[\x_1,\ldots, \x_n]$이 존재하여, 임의의 $(x_1,\ldots, x_n)\in X$에 대해 $f(x)=F(x)$가 성립하는 것이다. $X$ 위에 정의된 모든 regular function들의 모임을 $\mathbb{k}[X]$로 적고, 이를 $X$의 *coordinate ring*이라 부른다.

</div>

자명한 예시로, $X=\mathbb{A}^n$인 경우, $\mathbb{k}[\x_1,\ldots, \x_n]$의 임의의 원소들은 $X$ 위의 regular function이다. 특별히 $\x_1,\ldots, \x_n$들은 $X$의 coordinate function들이라 부른다. 

그럼 다음의 명제는 자명하다.  

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> [정의 4](#def4)의 $\mathbb{k}[X]$는 함수의 덧셈과 곱셈에 대해 commutative ring의 구조를 갖고, 따라서 $\mathbb{k}[X]$는 commutative $\mathbb{k}$-algebra 구조를 갖는다. 

</div>

한편, 임의의 $\mathbb{k}[\x_1,\ldots, \x_n]$의 원소는 자명한 이유로 $\mathbb{k}[X]$의 원소이기도 하며, 이로부터 얻어지는 surjective ring homomorphism $\varphi:\mathbb{k}[\x_1,\ldots, \x_n] \rightarrow \mathbb{k}[X]$가 존재한다. 여기에 first isomorphism theorem을 적용하면 다음의 isomorphism

$$\mathbb{k}[X]\cong \mathbb{k}[\x_1,\ldots, \x_n]/\ker\varphi$$

을 얻는다. 그럼 정의에 의해 $\ker\varphi$는 정확히 $X$ 위에서 $0$이 되는 regular function들로 이루어진 ideal인 것을 알 수 있다. 

위의 과정을 통해 algebraic set $X\subseteq \mathbb{A}^n$로부터 얻어지는 ideal $\ker\varphi$를 $I(X)$로 표기하자. 그럼 우리는 $\mathbb{k}[\x_1,\ldots, \x_n]$의 ideal들의 모임에서 $\mathbb{A}^n$의 닫힌집합들의 모임으로의 함수 $Z$, 그리고 $\mathbb{A}^n$의 닫힌집합들의 모임에서 $\mathbb{k}[\x_1,\ldots, \x_n]$의 ideal들의 모임으로의 함수 $I$를 얻는다. 그럼 [##ref##]()로부터 다음 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 위와 같은 상황에서, $\mathbb{k}[\x_1,\ldots, \x_n]$의 임의의 ideal $\mathfrak{a}$, 그리고 $\mathbb{A}^n$의 임의의 부분집합 $Y$를 생각하자. 그럼 다음 두 식

$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}},\quad Z(I(Y))=\overline{Y}$$

이 성립한다. 즉, $Z$와 $I$는 $\mathbb{A}^n$의 algebraic set들과 $\mathbb{k}[\x_1,\ldots, \x_n]$의 radical ideal들 사이의 bijection이 되며, 이들은 서로의 역함수이다. 

</div>

이제 [정의 4](#def4)를 더 일반화하여 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> 두 algebraic set $X\subseteq \mathbb{A}^n$, $Y\subseteq \mathbb{A}^m$에 대하여, $f:X \rightarrow Y$가 *regular map<sub>정칙사상</sub>*이라는 것은 $X$ 위에 정의된 $m$개의 regular function들 $f_1,\ldots, f_m$이 존재하여 $f(x)=(f_1(x),\ldots, f_m(x))$가 모든 $x\in X$에 대해 성립하는 것이다. 

</div>

고정된 $f: X \rightarrow Y$에 대하여, $Y$ 위에서 정의된 함수 $u$가 주어질 때마다 $u$의 *pullback* $f^\ast u=u\circ f$를 정의할 수 있다. 특히 $u$가 $Y$ 위에서 정의된 regular function이고 $f$가 regular map이라면 그 pullback $f^\ast u$ 또한 $X$ 위에서의 regular function인 것은 자명하다. 뿐만 아니라 다음이 성립한다.  

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $f^\ast: \mathbb{k}[Y] \rightarrow \mathbb{k}[X]$는 $\mathbb{k}$-algebra homomorphism이 된다. 거꾸로 임의의 $\mathbb{k}$-algebra homomorphism $\varphi: \mathbb{k}[Y] \rightarrow \mathbb{k}[X]$가 주어진다면 $\varphi=f^\ast$이도록 하는 regular map $f: X \rightarrow Y$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f^\ast$가 $\mathbb{k}$-algebra homomorphism인 것은 단순한 계산의 결과이므로 생략하고, 두 번째 주장만 보이기로 한다. $Y$를 포함하고 있는 $\mathbb{A}^m_\mathbb{k}$의 coordinate function들 $\y_1,\ldots, \y_m$을 생각하자. 그럼 가정에 의하여 $f_j=\varphi(\y_j)$들은 모두 $X$ 위에서의 regular function들이다. 이제 다음의 함수

$$f=(f_1,\ldots, f_m): X \rightarrow \mathbb{A}^m$$

을 생각하면 이 함수는 $Y$로의 regular map이 되는 것을 확인할 수 있다. 

</details>

이를 더 현대적인 언어로 바꾸어 쓰면 다음과 같다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> 지금까지 살펴본 $X\mapsto \mathbb{k}[X]$는 fully faithful (contravariant) functor를 정의한다. 

</div>

즉, category $\Alg{\mathbb{k}}$의 적당한 subcategory가 affine space의 닫힌집합들의 category와 equivalent하다. [따름정리 6](#cor6)을 적용하면 이 subcategory를 명시적으로 정해줄 수도 있다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> $\mathbb{k}$-algebra $A$가 적당한 coordinate ring $\mathbb{k}[X]$와 isomorphic한 것은 $A$가 finitely generated reduced $\mathbb{k}$-algebra인 것과 동치이다. 따라서, finitely generated reduced $\mathbb{k}$-algebra들의 category와 algebraic set들의 category 사이의 categorical equivalence가 존재한다.

</div>

