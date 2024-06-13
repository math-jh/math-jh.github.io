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

이번 글에서는 이미 존재하는 category로부터 새로운 category들을 만드는 방법을 살펴본다. 

## Opposite category

<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> Category $\mathcal{A}$가 주어졌다 하자. 그럼 $\mathcal{A}$의 *opposite category<sub>반대 카테고리</sub>* $\mathcal{A}^\op$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}^\op)=\obj(\mathcal{A})$이다.
- 임의의 $A,B\in \obj(\mathcal{A}^\op)=\obj(\mathcal{A})$에 대하여, $\Hom_{\mathcal{A}^\op}(A,B)=\Hom_{\mathcal{A}}(B,A)$가 성립한다.
- 임의의 $A\in\obj(\mathcal{A})$에 대하여, $\mathcal{A}^\op$에서의 identity $\id_A$는 $\mathcal{A}$에서의 identity와 동일한 것으로 주어진다.
- 임의의 $f\in\Hom_{\mathcal{A}^\op}(A,B),g\in\Hom_{\mathcal{A}^\op}(B,C)$에 대하여, 이들의 합성 $g\circ^\op f$는 $f,g$를 $\mathcal{A}$의 morphism들로 본 후, 이를 $\mathcal{A}$에서 합성한 것으로 정의된다.   
  즉, $f\in \Hom_\mathcal{A}(B,A),g\in\Hom_\mathcal{A}(C,B)$에 대하여, $f$와 $g$의 $\mathcal{A}^\op$에서의 합성 $g\circ^\op f$는 
    
    $$g\circ^\op f= f\circ g\in\Hom_{\mathcal{A}}(C,A)=\Hom_{\mathcal{A}^\op}(A,C)$$

  으로 정의된다. 

</div>

어렵지 않게 $\mathcal{A}^\op$가 실제로 

## Product category

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 두 category $\mathcal{A},\mathcal{B}$가 주어졌다 하자. 이들의 *product category<sub>곱 카테고리</sub>* $\mathcal{A}\times \mathcal{B}$는 다음의 데이터로 이루어진다.

- $\obj(\mathcal{A}\times \mathcal{B})$의 대상들은 쌍 $(A,B)$의 꼴이다.
- 임의의 $(A_1,B_1),(A_2,B_2)\in\obj(\mathcal{A}\times \mathcal{B})$에 대하여, $\Hom_{\mathcal{A}\times \mathcal{B}}((A_1,B_1),(A_2,B_2))$는 $f\in\Hom_\mathcal{A}(A_1,A_2),g\in\Hom_\mathcal{B}(B_1,B_2)$에 대해 $(f,g)$의 꼴이다. 
- 임의의 $A\times B\in \mathcal{A}\times \mathcal{B}$에 대하여, $A\times B$에서의 identity는 $(\id_A,\id_B)$로 주어진다.
- 임의의 $(f_1,g_1):(A_1,B_1)\rightarrow(A_2,B_2)$, $(f_2,g_2):(A_2,B_2)\rightarrow(A_3,B_3)$에 대해, 이들의 합성은 $(f_2\circ f_1,g_2\circ g_1)\in\Hom((A_1,B_1),(A_3,B_3))$으로 주어진다. 

</div>

## Over category and under category

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Category $\mathcal{A}$가 주어졌다 하고, $A\in\obj(\mathcal{A})$를 고정하자. 

- $\mathcal{A}$의 *slice category over $A$<sub>$A$ 위에서의 조각 범주</sub>* $A_{/\mathcal{A}}$는 다음과 같은 데이터로 주어진다.
  - $\mathcal{A}_{/A}$의 object들은 $\mathcal{A}$의 morphism들 $f:A_1\rightarrow A$이다.
  - 임의의 $(A\_1\overset{f\_1}{\longrightarrow}A)\in\obj(\mathcal{A}\_{/A})$와 $(A\_2\overset{f\_2}{\longrightarrow}A)\in\obj(\mathcal{A}\_{/A})$에 대하여, $f_1$에서 $f_2$로의 morphism은 $f_1=g\circ f_2$가 성립하도록 하는 $g:A_1\rightarrow A_2$이다.
- $\mathcal{A}$의 *slice category under $A$<sub>$A$ 위에서의 쌍대 조각 범주</sub>* ${}_{A/}\mathcal{A}$는 다음과 같은 데이터로 주어진다.
  - ${}_{A/}\mathcal{A}$의 object들은 $\mathcal{A}$의 morphism들 $f:A\rightarrow A_1$이다.
  - 임의의 $(A\overset{f\_1}{\longrightarrow}A\_1)\in\obj({}\_{A/}\mathcal{A})$와 $(A\overset{f\_2}{\longrightarrow}A\_2)\in\obj({}\_{A/}\mathcal{A})$에 대하여, $f_1$에서 $f_2$로의 morphism은 $f_2=g\circ f_1$가 성립하도록 하는 $g:A_1\rightarrow A_2$이다.

</div>

---

**참고문헌**

**[Lei]**

---

[^1]: 별 말이 없다면 모든 ring은 $1$을 갖는 unital ring인 것으로 가정한다. $1$을 갖지 않을 수도 있는 ring들의 category $\Rng$가 존재하지만, 잘 쓸 일은 없다.