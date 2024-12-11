---

title: "카르티에 인자"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/Cartier_divisors
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Cartier_divisors.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-07-25
last_modified_at: 2024-07-25
weight: 13

---

이번 글에서는 Cartier divisor를 정의한다. 이는 공간 대신 그 위에 정의된 함수들을 생각한다는 점에서 cohomology와 조금 더 닮아있다고 할 수 있다.

## Cartier divisor

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$를 고정하자. 임의의 열린집합 $U$마다, $\Gamma(U, \mathscr{O}_X)$의 원소들 중, 각각의 local ring $\mathscr{O}_x$ ($x\in U$)들에서 모두 zero divisor가 아닌 것들을 $S(U)$라 표기하기로 하자. 그럼 다음 presheaf

$$U\mapsto S(U)^{-1}\Gamma(U, \mathscr{O}_X)$$

의 sheafification $\mathscr{K}$를 *sheaf of total quotient rings*이라 부른다. 

</div>

$\mathscr{K}$의 원소들 중 invertible한 원소들만 뽑아온 sheaf를 $\mathscr{K}^\ast$으로 표기하고, 비슷하게 $\mathscr{O}^\ast$를 $\mathscr{O}_X$ 중 invertible한 원소들만 뽑아온 sheaf로 정의한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Sheaf $\mathscr{K}^\ast/\mathscr{O}^\ast$의 global section을 $X$ 위에 정의된 *Cartier divisor<sub>카르티에 인자</sub>*라 부르고, 이들의 모임을 $\CaDiv(X)$로 적는다. 이들 중 $\Gamma(X, \mathscr{K}^\ast)\rightarrow \Gamma(X, \mathscr{K}^\ast/\mathscr{O}^\ast)$의 image에 속하는 것들을 *principal Cartier divisor*라 부르고, principal Cartier divisor만큼 차이나는 두 Cartier divisor를 *linearly equivalent*하다고 한다. 이는 동치관계이며, 따라서 quotient group $\CaCl(X)$를 정의한다.

</div>

이들 $\mathscr{K}^\ast, \mathscr{O}^\ast, \mathscr{K}^\ast/\mathscr{O}^\ast$는 모두 곱셈으로 연산이 주어진 abelian group들이다. Cartier divisor는 local하게 열린집합 $U_i$들과, 그 위에 정의된 rational function들 $f_i\in \mathscr{K}^\ast$의 pair들의 gluing으로 쓸 수 있다. 이 때 요구되는 조건은 $U_i\cap U_j$ 위에서 $f_i/f_j\in \mathscr{O}^\ast(U_i\cap U_j)$인 것이다. 

Cartier divisor는 일반적인 scheme 위에서 정의되므로 Weil divisor보다 더 일반적인 것이지만, 다음 명제에 따라 충분히 좋은 공간 위에서는 이들 둘이 동일하다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Integral separated noetherian scheme $X$가 주어졌다 하자. 만일 $X$의 임의의 local ring이 항상 UFD이면, $\CaDiv(X)\cong \Div(X)$이다. 뿐만 아니라, 이 isomorphism을 통해 principal Weil divisor들과 principal Cartier divisor들도 일대일 대응이 되어, $\CaCl(X)\cong \Cl(X)$를 유도한다. 

</div>

임의의 Cartier divisor $\\{(U_i,f_i)\\}$가 주어졌다 하자. 이로부터 Weil divisor를 얻어내는 방법은 자명하다. 임의의 prime divisor $Y$마다, $Y\cap U_i\neq\emptyset$을 만족하는 $i$를 택한 후,

$$D=\sum v_Y(f_i)Y$$

으로 정의하면 된다. 이 식이 잘 정의되기 위해서는 $v_Y(f_i)$가 index $i$의 선택에 의존하지 않아야 하지만, Cartier divisor의 조건으로부터 $f_i/f_j$가 $U_i\cap U_j$에서는 invertible이므로 $v_Y(f_i/f_j)=0$이 되어 어떠한 index를 택해도 상관이 없다.

문제는 반대로 임의의 Weil divisor를 가져왔을 때 Cartier divisor를 정의하는 부분이다. 직관적으로 이야기해서 이는 Weil divisor가 prime ideal들 위에서의 전체 scheme structure 대신, multiplicity만 기억하기 때문인데 위의 [명제 3](#prop3)의 조건 하에서는 이 정보를 복원할 수 있다. 

## Line bundle

앞서 우리는 locally free sheaf of rank $1$을 *line bundle*이라 부르기로 하였다. 이들은 divisor class와 밀접한 연관이 있다. 종종 line bundle을 *invertible sheaf*라 부르기도 하는데, 이는 다음 명제에 따른 것이다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 ringed space $X$ 위에 정의된 line bundle $\mathscr{L}_1,\mathscr{L}_2$에 대하여, 이들의 텐서곱 $\mathscr{L}_1\otimes \mathscr{L}_2$는 $X$ 위의 line bundle이 된다. 또, $X$ 위의 임의의 line bundle $\mathscr{L}$에 대하여, $\mathscr{L}\otimes \mathscr{L}^{-1}\cong \mathscr{O}_X$이도록 하는 line bundle $\mathscr{L}^{-1}$이 존재한다. 

</div>

두 번째 주장이 덜 자명해 보일 수도 있지만 이는 그냥 $\mathscr{L}^{-1}=\mathscr{Hom}(\mathscr{L},\mathscr{O}_X)$로 두면 된다. 어쨌든 위의 명제에 의해 line bundle들의 isomorphism class를 모아두면 이는 $\otimes$에 대해 group structure를 가진다. 

이를 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Ringed space $X$에 대하여, line bundle들의 isomorphism class에 $\otimes$를 장착한 것을 $X$의 *Picard group<sub>피카르드 군</sub>*이라 부르고 $\Pic X$로 적는다. 

</div>


<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme $X$ 위에 정의된 Cartier divisor $D$를 생각하고, local하게 이를 $\\{(U\_i,f_i)\\}$로 나타내자. 그럼 각 $U_i$마다 $\mathscr{K}$의 원소 $f^{-1}_i$로 생성된 $\mathscr{O}_X$-submodule을 $\mathscr{O}_X(D)$로 적고 *sheaf associated to $D$*라 부른다. 

</div>

정의에 의해 $\mathscr{O}(D)$는 line bundle이다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 위와 같은 상황에서 다음이 성립한다. 

1. $D\mapsto \mathscr{O}_X(D)$는 Cartier divisor와 $\mathscr{K}$의 invertible subsheaf 사이의 일대일대응을 정의한다. 
2. 뿐만 아니라, $\mathscr{O}_X(D_1-D_2)\cong \mathscr{O}_X(D_1)\otimes \mathscr{O}_X(D_2)^{-1}$이고, $D_1\sim D_2$인 것과 $\mathscr{O}_X(D_1)\cong \mathscr{O}_X(D_2)$인 것이 동치이다. 

따라서, $D\mapsto \mathscr{O}_X(D)$가 injecetive map $\CaCl X \rightarrow \Pic X$를 정의한다. 

</div>

만일 $X$가 integral scheme이라면 이 injective homomorphism은 isomorphism이 되며, 특히 $X$의 Weil divisor가 잘 정의되면 $\Cl X\cong \CaCl X\cong \Pic X$를 얻는다. 