---

title: "카테고리의 예시들"
excerpt: "카테고리의 예시들"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/examples_of_categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Examples_of_categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2023-06-19
last_modified_at: 2023-06-19
weight: 2

---

범주론을 잘 아는 것은 단순히 이론을 이해하는 것뿐만 아니라, 예시들 또한 잘 이해하는 것을 포함한다. 많이 과장해서 말하자면 예시가 없는 범주론은 쓸모가 없다.

## Category의 예시들

<div class="example" markdown="1">

<ins id="ex1">**예시 1 (Concrete categories)**</ins> 다음은 모두 category의 예시들이다.

- 집합들과 함수들의 category $\Set$
- Pointed set들과 pointed function들의 category $\Set_\ast$
- Monoid들과 monoid homomorphism들의 category $\Mon$
- Group들과 group homomorphism들의 category $\Grp$
- Abelian group들과 group homomorphism들의 category $\Ab$
- Ring들과 ring homomorphism들의 category[^1] $\Ring$
- Field들과 field extension들의 category $\Field$
- Left, right $G$-set들과 $G$-set homomorphism들의 category $\lset{G},\rset{G}$
- Left, right $R$-module들과 $R$-module homomorphism들의 category $\lmod{R},\rmod{R}$
- $k$-벡터공간들과 linear map들의 category $\Vect_k$
- 유한차원 $k$-벡터공간들과 linear map들의 category $\FVect_k$
- 위상공간들과 연속함수들의 category $\Top$
- Pointed topological space들과 pointed continuous map들의 category $\Top_\ast$
- $C^k$-manifold들과 $C^k$-map들의 category $\Man^k$
- $R$-module들의 chain complex와 chain map들의 category $\Ch(R)$


</div>

앞선 예시에서의 모든 category의 object들은 집합 위에 추가적인 구조가 주어진 수학적인 대상들이며, 이들 사이의 morphism은 집합들 사이의 함수들 중 이 구조를 보존하는 것들로 주어진다. 이러한 category들을 *concrete category*라 부른다.

당연히 concrete하지 않은 카테고리들이 존재한다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 다음 또한 모두 category의 예시들이다.

- 위상공간들과 homotopy class들의 category $\hTop$
- Pointed topological space들과 pointed homotopy class들의 category $\hTop$
- 임의의 ring $R$에 대하여, category $\Mat_R$의 object는 자연수들이며, $\Hom(n,m)=\Mat_{m\times n}(R)$, 그리고 morphism들의 합성은 행렬의 곱이다.
- 임의의 preordered set $(S,\preceq)$에 대하여, category $\mathbf{S}$의 object는 $S$의 원소들이며, 임의의 $x,y\in S$에 대해 $x\preceq y$가 성립할 경우 $\Hom(x,y)$가 유일한 원소를 갖고, 그렇지 않은 경우는 공집합인 것으로 정의한다.

</div>

다음 예시들은 category들이 주어졌을 때, 그로부터 새로운 category를 만드는 법을 보여준다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Category $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$의 *opposite category<sub>반대 카테고리</sub>* $\mathcal{A}^\op$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}^\op)=\obj(\mathcal{A})$이다.
- 임의의 $A,B\in \obj(\mathcal{A}^\op)=\obj(\mathcal{A})$에 대하여, $\Hom_{\mathcal{A}^\op}(A,B)=\Hom_{\mathcal{A}}(B,A)$가 성립한다.
- 임의의 $A\in\obj(\mathcal{A})$에 대하여, $\mathcal{A}^\op$에서의 identity $\id_A$는 $\mathcal{A}$에서의 identity와 동일한 것으로 주어진다.
- 임의의 $f\in\Hom_{\mathcal{A}^\op}(A,B),g\in\Hom_{\mathcal{A}^\op}(B,C)$에 대하여, 이들의 합성 $g\circ^\op f$는 $f,g$를 $\mathcal{A}$의 morphism들로 본 후, 이를 $\mathcal{A}$에서 합성한 것으로 정의된다.   
  즉, $f\in \Hom_\mathcal{A}(B,A),g\in\Hom_\mathcal{A}(C,B)$에 대하여, $f$와 $g$의 $\mathcal{A}^\op$에서의 합성 $g\circ^\op f$는 
    
    $$g\circ^\op f= f\circ g\in\Hom_{\mathcal{A}}(C,A)=\Hom_{\mathcal{A}^\op}(A,C)$$

  으로 정의된다. 

</div>

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 두 category $\mathcal{A},\mathcal{B}$가 주어졌다 하자. 이들의 *product category<sub>곱 카테고리</sub>* $\mathcal{A}\times \mathcal{B}$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}\times \mathcal{B})$의 대상들은 쌍 $(A,B)$의 꼴이다.
- 임의의 $(A_1,B_1),(A_2,B_2)\in\obj(\mathcal{A}\times \mathcal{B})$에 대하여, $\Hom_{\mathcal{A}\times \mathcal{B}}((A_1,B_1),(A_2,B_2))$는 $f\in\Hom_\mathcal{A}(A_1,A_2),g\in\Hom_\mathcal{B}(B_1,B_2)$에 대해 $(f,g)$의 꼴이다. 
- 임의의 $A\times B\in \mathcal{A}\times \mathcal{B}$에 대하여, $A\times B$에서의 identity는 $(\id_A,\id_B)$로 주어진다.
- 임의의 $(f_1,g_1):(A_1,B_1)\rightarrow(A_2,B_2)$, $(f_2,g_2):(A_2,B_2)\rightarrow(A_3,B_3)$에 대해, 이들의 합성은 $(f_2\circ f_1,g_2\circ g_1)\in\Hom((A_1,B_1),(A_3,B_3))$으로 주어진다. 

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> Category $\mathcal{A}$가 주어졌다 하고, $A\in\obj(\mathcal{A})$를 고정하자. 

- $\mathcal{A}$의 *slice category over $A$<sub>$A$ 위에서의 조각 범주</sub>* $A/\mathcal{A}$는 다음과 같은 데이터로 주어진다.
  - $A/\mathcal{A}$의 object들은 $\mathcal{A}$의 morphism들 $f:A\rightarrow A_1$이다.
  - 임의의 $(A\overset{f_1}{\longrightarrow}A_1)\in\obj(A/\mathcal{A})$와 $(A\overset{f_2}{\longrightarrow}A_2)\in\obj(A/\mathcal{A})$에 대하여, $f_1$에서 $f_2$로의 morphism은 $f_2=g\circ f_1$가 성립하도록 하는 $g:A_1\rightarrow A_2$이다.
- $\mathcal{A}$의 *slice category under $A$<sub>$A$ 위에서의 쌍대 조각 범주</sub>* $\mathcal{A}/A$는 다음과 같은 데이터로 주어진다.
  - $\mathcal{A}/A$의 object들은 $\mathcal{A}$의 morphism들 $f:A_1\rightarrow A$이다.
  - 임의의 $(A_1\overset{f_1}{\longrightarrow}A)\in\obj(\mathcal{A}/A)$와 $(A_2\overset{f_2}{\longrightarrow}A)\in\obj(\mathcal{A}/A)$에 대하여, $f_1$에서 $f_2$로의 morphism은 $f_1=g\circ f_2$가 성립하도록 하는 $g:A_1\rightarrow A_2$이다.

</div>

---

**참고문헌**

**[Lei]**

---

[^1]: 별 말이 없다면 모든 ring은 $1$을 갖는 unital ring인 것으로 가정한다. $1$을 갖지 않을 수도 있는 ring들의 category $\Rng$가 존재하지만, 잘 쓸 일은 없다.