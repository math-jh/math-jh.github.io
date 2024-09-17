---

title: "벡터공간"
excerpt: "벡터공간의 정의, 간단한 성질과 예시들"

categories: [Math / Basic Linear Algebra]
permalink: /ko/math/basic_linear_algebra/vector_spaces
sidebar: 
    nav: "basic_linear_algebra-ko"

header:
    overlay_image: /assets/images/Math/Basic_Linear_Algebra/Vector_spaces.png
    overlay_filter: 0.5

date: 2022-07-28
last_modified_at: 2022-07-28

weight: 2

---

앞선 글의 서두에서 이야기했듯 선형대수에서 다루는 공간인 *벡터공간*은 고등학교 때 배우는 좌표공간을 일반화하는 개념이다. 우리는 이를 위해 지난 글에서 abelian group과 field를 정의했다. 

많은 선형대수 책에서는 이 정의들을 피하고 단순히 $\mathbb{R}$-벡터공간 혹은 $\mathbb{C}$-벡터공간만을 생각하기도 하지만, 더 일반적인 경우가 전혀 복잡하지 않으므로 굳이 특수한 경우로 우리의 관심사를 한정할 필요가 없다.

## 벡터공간의 정의

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $\mathbb{k}$가 field이고, $V$가 abelian group이라 하자. $V$가 *$\mathbb{k}$에 대한 벡터공간<sub>vector space over $\mathbb{k}$</sub>*, 혹은 간단히 *$\mathbb{k}$-벡터공간<sub>$\mathbb{k}$-vector space</sub>*이라는 것은 여기에 추가적인 연산 (*스칼라곱*) $\cdot:\mathbb{k}\times V\rightarrow V$가 존재하여 

1. 임의의 $\alpha,\beta\in\mathbb{k}$와 임의의 $u\in V$에 대하여 $\alpha\cdot(\beta\cdot u)=(\alpha\beta)\cdot u$가 성립한다.
2. 임의의 $\alpha\in\mathbb{k}$와 임의의 $u,v\in V$에 대하여 $\alpha\cdot(u+\_{\tiny V}v)=(\alpha\cdot u)+\_{\tiny V}(\alpha\cdot v)$가 성립한다.
3. 임의의 $\alpha,\beta\in\mathbb{k}$와 임의의 $u\in V$에 대하여 $(\alpha+\_{\tiny \mathbb{k}}\beta)\cdot u=(\alpha\cdot u)+\_{\tiny V}(\beta\cdot u)$가 성립한다.  
4. 곱셈에 대한 $\mathbb{k}$의 항등원 $1\in\mathbb{k}$에 대하여, $1\cdot u=u$가 임의의 $u\in V$에 대하여 성립한다.

가 모두 만족되는 것이다. 이 때 $V$의 원소들을 *벡터<sub>vector</sub>*들이라 부른다.

</div>

위의 정의와 같이, 앞으로는 혼동을 피하기 위해 field $\mathbb{k}$의 원소는 모두 $\alpha,\beta,\ldots$으로 적고, $\mathbb{k}$-벡터공간의 원소들은 $u,v,\ldots$로 적기로 한다. 위의 정의에서는 $+\_{\tiny V}$와 $+\_{\tiny \mathbb{k}}$를 구별하여 적었는데, 방금 만든 표기법처럼 이들을 구분하면 $+$ 주위에 있는 원소가 $\mathbb{k}$의 원소인지, $V$의 원소인지가 명확하게 구별되므로 이들을 모두 $+$로만 적어도 혼동의 여지가 없다.  

스칼라곱도 마찬가지로 $\alpha\cdot u$와 같은 표기 대신 $\alpha u$와 같이 적기로 한다. 이 경우 유일한 걱정은 $\alpha\beta u$라고 쓸 때 이것이 $(\alpha\beta)u$인지, $\alpha(\beta u)$인지 헷갈릴 수 있다는 것인데, 위 정의의 첫 번째 조건에 의해 어떤 것을 선택하더라도 그 값은 동일하므로 이는 걱정할 필요가 없다.  

벡터공간은 abelian group $V$ 위에 추가적인 구조인 $\mathbb{k}$-스칼라곱이 정의된 형태이다. 때문에 $V$는 abelian group이 갖는 성질을 모두 갖는다. ([§가환군과 체, ⁋명제 2](/ko/math/basic_linear_algebra/fields#prop2) 그리고 [§가환군과 체, ⁋따름정리 3](/ko/math/basic_linear_algebra/fields))

다음 성질들은 $\mathbb{k}$-스칼라곱에 의해 결정되는 추가적인 성질들이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $\mathbb{k}$-벡터공간 $V$가 주어졌다 하자. 그럼

1. 임의의 $\alpha\in\mathbb{k}$에 대하여, $\alpha0=0$이고,
2. 임의의 $v\in V$에 대하여, $0v=0$이다.

거꾸로, 만일 $\alpha v=0$이라면, $\alpha=0$이거나 $v=0$이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 두 주장은 [§가환군과 체, ⁋명제 6](/ko/math/basic_linear_algebra/fields#prop6)과 비슷하게 진행하면 된다. 예를 들어, 

$$\alpha0+\alpha0=\alpha(0+0)=\alpha0$$

이므로 $\alpha0=0$이고, 이와 비슷하게

$$0v+0v=(0+0)v=0v$$

이므로 $0v=0$이다. 마지막으로, $\alpha v=0$이고 $\alpha\neq 0$이라 하자. 만일 $\alpha\neq 0$이라면, $\alpha^{-1}\in\mathbb{k}$가 존재하여 $\alpha\alpha^{-1}=1$이고, 따라서

$$v=1v=(\alpha^{-1}\alpha)v=\alpha^{-1}(\alpha v)=\alpha^{-1}0=0$$

이므로, $v=0$이 되어 주어진 명제가 성립한다.

</details>

위의 명제의 1번에 등장하는 $0$과 2번의 우변에 등장하는 $0$은 모두 $V$의 원소이고, 2번의 좌변에 등장하는 $0$은 $\mathbb{k}$의 원소이다. 엄밀히 적기 위해서는 이들 또한 $0\_{\tiny V}$와 $0\_{\tiny \mathbb{k}}$ 등으로 구별해주어야 하나 문맥상 이들은 명확하게 구별할 수 있으므로 모두 $0$으로만 적는다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> $\mathbb{k}$-벡터공간 $V$의 임의의 원소 $v$에 대하여, $(-1)v=-v$가 항상 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다음의 식

$$(-1)v+v=(-1)v+1v=((-1)+1)v=0v=0$$

과 $V$에서의 덧셈에 대한 역원의 유일성으로부터 자명하다.

</details>

## 벡터공간의 예시들

이제 벡터공간의 몇 가지 예시를 살펴보자.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 가장 간단한 벡터공간의 예시는 $\\{0\\}$이다. 이 집합에 더하기 구조를 줄 수 있는 방법은 하나 뿐이고 (즉 $0+0=0$), 이 구조 하에서 이 집합은 abelian group의 구조를 갖는다. 뿐만 아니라, 어떤 field $\mathbb{k}$를 가져오더라도 이 집합에 스칼라곱을 정의할 수 있는 방법 또한 하나 뿐이며 (즉 $\alpha 0=0$), 이렇게 정의된 스칼라곱은 $\\{0\\}$를 $\mathbb{k}$-벡터공간으로 만든다. 이를 *trivial space*이라 부른다.

조금 덜 자명한 예시는 field 그 자체다. 임의의 field $\mathbb{k}$에 대하여, $\mathbb{k}$는 $\mathbb{k}$-벡터공간이다. $\mathbb{k}$는 field이므로, 덧셈에 대해 abelian group이 된다는 것은 자명하다. 여기에 스칼라곱 구조만 주면 충분한데, 이는 그냥 $\mathbb{k}$에서의 곱하기 $\mathbb{k}\times \mathbb{k}\rightarrow \mathbb{k}$로 주면 된다. 이렇게 정의하면 스칼라곱이 [정의 1](#def1)의 조건들을 모두 만족한다는 것을 확인할 수 있고, 따라서 $\mathbb{k}$는 그 자체로 $\mathbb{k}$-벡터공간이다. 

더 일반적으로 $\mathbb{k}$가 field이고, 다른 어떤 field $\mathbb{k}'$가 존재하여 $\mathbb{k}'\supseteq \mathbb{k}$라 하자. 그럼 $\mathbb{k}'$는 $\mathbb{k}$-벡터공간이 된다. $\mathbb{k}'$는 field이므로, 아까 전과 같이 덧셈에 대해 abelian group을 이루며, $\alpha\in\mathbb{k}$의 원소와의 스칼라곱은 $\alpha$를 $\mathbb{k}'$의 원소로 취급한 후 $\mathbb{k}'$에서의 곱셈구조를 이용하면 된다. 예를 들어 $\mathbb{C}$는 $\mathbb{R}$-벡터공간이고, $\mathbb{R}$은 $\mathbb{Q}$-벡터공간이다. 

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 이번에는 field $\mathbb{k}$가 주어졌다고 하자. 그럼 *유클리드 $n$차원 공간*은 다음의 $n$-순서쌍

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix},\qquad a_i\in\mathbb{k}\text{ for all $i$}$$

들로 이루어진 $\mathbb{k}$-벡터공간이다. 이들 사이의 덧셈과 스칼라곱은 각각

$$\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}+\begin{pmatrix}b_1\\b_2\\\vdots\\b_n\end{pmatrix}=\begin{pmatrix}a_1+b_1\\a_2+b_2\\\vdots\\a_n+b_n\end{pmatrix},\qquad \alpha\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}=\begin{pmatrix}\alpha a_1\\\alpha a_2\\\vdots\\\alpha a_n\end{pmatrix}$$

으로 정의된다. $\mathbb{k}=\mathbb{R}$이고 $n=2,3$일 경우, 이 정의는 우리가 잘 아는 좌표평면과 좌표공간이 된다. 

</div>

유클리드 공간은 우리가 특히 많이 다룰 대상이다. 위의 예시에서 우리는 순서쌍 $(a\_1, a\_2, \ldots, a\_n)$이라는 표기법 대신 열로 이루어진 표기법을 사용하고 있으며, 이는 선형대수학의 기본정리와 밀접한 연관이 있다.

 하지만 아무리 그럴듯한 이유가 있더라도, 이 표기법을 $\begin{pmatrix}a\_1\\\a\_2\\\\\vdots\\\a\_n\end{pmatrix}$ 과 같이 본문에서 고집하는 것도 어리석은 일이다. 따라서 본문 중에서는 $(a\_1\;a\_2\;\cdots\;a\_n)^t$와 같은 표기법 혹은, 고등학교 때의 표기법을 따라 $(a\_1,a\_2,\ldots, a\_n)$와 같이 쓰기로 한다.

위에서 살펴본 두 개의 벡터공간들은 상당히 구체적인 예시에 속한다. 다음 예시와 같이, 일반적으로 벡터공간은 좌표평면 혹은 좌표공간처럼 시각적으로 표현되지 않는 경우도 있다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $I$가 어떤 구간이라 하고, $I$에서 $\mathbb{R}$로의 함수들의 모임 $\Fun(I,\mathbb{R})$을 생각하자. 이제 이 집합 위에, 덧셈과 스칼라곱을 다음의 식

$$f+g:t\mapsto f(t)+g(t),\qquad \alpha f:t\mapsto \alpha f(t)$$

으로 정의하면 $\Fun(I,\mathbb{R})$이 벡터공간 구조를 갖는 것을 확인할 수 있다. 즉, $f+g$는 임의의 $t\in I$를 $f(t)+g(t)$라는 값으로 보내는 함수로, $\alpha f$는 임의의 $t\in I$를 $\alpha f(t)$로 보내는 함수로 정의된다. 

뿐만 아니라, $\Fun(I,\mathbb{R})$의 여러 부분집합들도 $\mathbb{R}$-벡터공간이 된다. 예를 들어, $I$에서 $\mathbb{R}$로의 연속함수들의 모임 $C(I)$ 또한 $\mathbb{R}$-벡터공간이고, 더 일반적으로 $k$번째 도함수가 연속인 함수들의 모임 $C^k(I)$들의 모임도 $\mathbb{R}$-벡터공간이 된다는 것을 확인할 수 있다.

</div>

$\Fun(I,\mathbb{R})$을 product set $\mathbb{R}^I$라 생각하면 [예시 6](#ex6)은 [예시 5](#ex5)의 자연스러운 일반화로 볼 수도 있다. ([\[집합론\] §집합의 곱, ⁋정의 1](/ko/math/set_theory/product_of_sets#def1))

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.

---