---

title: "열린사상과 닫힌사상"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/open_mappings_and_closed_mappings
header:
    overlay_image: /assets/images/Math/Topology/Open_mappings_and_closed_mappings.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-11-19
last_modified_at: 2024-11-19
weight: 12

---

## 정의와 기본적인 성질들

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 두 위상공간 $X,Y$와 함수 $f:X \rightarrow Y$에 대하여 다음을 정의한다. 

1. 만일 $X$의 임의의 열린집합 $U$에 대하여 $f(U)$가 항상 $Y$의 열린집합이라면 $f$를 *open mapping<sub>열린사상</sub>*이라 부른다. 
2. 만일 $X$의 임의의 닫힌집합 $A$에 대하여 $f(A)$가 항상 $Y$의 닫힌집합이라면 $f$를 *closed mapping<sub>닫힌사상</sub>*이라 부른다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위상공간 $X,Y,Z$와 함수 $f:X \rightarrow Y$, $g:Y \rightarrow Z$가 주어졌다 하자. 그럼 다음이 성립한다. 

1. 만일 $f, g$가 모두 open (resp. closed)이라면 $g\circ f$ 또한 open (resp. closed)이다.
2. 만일 $g\circ f$가 open (resp. closed)이고 $f$가 continuous surjection이라면 $g$는 open (resp. closed)이다. 
3. 만일 $g\circ f$가 open (resp. closed)이고 $g$가 continuous injection이라면 $f$는 open (resp. closed)이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>
1. 자명하다. 
2. $Y$의 임의의 열린집합 $V$가 주어졌다 하자. 그럼 $f$는 연속이므로 $f^{-1}(V)$는 $X$의 열린집합이고, 따라서
    
    $$(g\circ f)(f^{-1}(V))=g(f(f^{-1}(V)))=g(V)$$

    가 성립하므로 $g(V)$는 $Z$의 열린집합이다. 여기서 $f(f^{-1}(V))=V$인 것은 $f$가 전사함수임을 이용하였다. ([\[집합론\] §Retraction과 section, ⁋정의 2](/ko/math/set_theory/retraction_and_section#def2)) 한편 마찬가지 방식으로 $Y$의 임의의 닫힌집합 $B$가 주어졌다 하면 [§연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)에 의하여 위와 동일한 논증을 적용할 수 있다.
3. 둘째 증명과 마찬가지로 open인 경우만 생각하면 충분하다. $X$의 임의의 열린집합 $U$에 대하여, $g\circ f$가 open이므로 $g(f(U))$는 open이고, 따라서 $g$가 연속이라는 것과 위의 [\[집합론\] §Retraction과 section, ⁋정의 2](/ko/math/set_theory/retraction_and_section#def2)을 사용하면 다음 식
    
    $$g^{-1}(g(f(U))=f(U)$$

    로부터 $f(U)$가 열린집합임을 안다.

</details>

다음 명제는 위상공간 사이의 함수가 언제 open 또는 closed인지를 판별하는데 도움이 된다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 두 위상공간 사이의 함수 $f:X \rightarrow Y$가 주어졌다 하자. 그럼 다음이 성립한다.

1. 만일 $f$가 open (resp. closed)라면, $Y$의 임의의 부분집합 $A$에 대하여 $f\vert_{f^{-1}(A)}: f^{-1}(A) \rightarrow A$도 open (resp. closed)이다.
2. $Y$의 covering $(A\_i)\_{i\in I}$가 (1) locally finite closed covering이거나, (2) $(\interior A\_i)\_{i\in I}$가 $Y$의 open covering이 된다고 하자. 만일 각각의 $f\vert_{f^{-1}(A_i)}$가 open (resp. closed)라면, $f$ 또한 그러하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 결과를 보이기 위해 $f^{-1}(A)$에서의 열린집합 (resp. 닫힌집합)을 택하자. 그럼 $X$에서의 열린집합 (resp. 닫힌집합) $U$가 존재하여 이를 $U\cap f^{-1}(A)$ 꼴로 적을 수 있다. 따라서

$$f\vert_{f^{-1}(A)}(U)=f(U)\cap A$$

이고, 가정에 의하여 $f(U)$가 열린집합 (resp. 닫힌집합)이므로 원하는 결과를 얻는다.

두 번째 결과도 비슷하게 증명할 수 있는데, $X$에서의 열린집합 (resp. 닫힌집합) $U$가 주어졌다 하고, $U\_i$를 다음 식

$$U_i=U\cap f^{-1}(A_i)$$

으로 정의하자. 그럼 $f\vert\_{f^{-1}(A\_i)}(U_i)=f(U)\cap A\_i$이 성립하고, 따라서 가정에 의하여 $f(U)\cap A_i$가 모든 $i$에 대해 열린집합 (resp. 닫힌집합)이다. 따라서 만일 $U$가 열린집합이라면 $f(U)$는 열린집합들의 합집합이므로 열린집합이고, $U$가 닫힌집합이면 [§집합의 내부, 폐포, 경계, ⁋명제 4](/ko/math/topology/other_concepts#prop4)에 의하여 닫힌집합이 된다. 

</details>

## 동치관계들

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> 위상공간 $X$ 위에 정의된 동치관계 $R$이 *open (resp. closed)*이라는 것은 canonical map $X \rightarrow X/R$이 open (resp. closed)인 것이다. 

</div>

그럼 다음이 성립하는 것을 쉽게 보일 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 두 위상공간 $X,Y$ 사이의 연속함수 $f:X \rightarrow Y$와 $f$의 canonical decomposition

$$X \overset{p}{\longrightarrow} X/R \overset{h}{\longrightarrow h} f(X)\overset{i}{\longrightarrow}Y$$

를 생각하자. 그럼 다음이 모두 동치이다.

1. $f$가 open (resp. closed)이다.
2. $p,h,i$가 모두 open (resp. closed)이다.
3. $R$이 open (resp. closed)이고, $h$는 homeomorphism이며 $f(X)$는 $Y$의 open (resp. closed) subset이다.

</div>

## 열린사상의 성질들

이제 우리는 열린사상과 닫힌사상 각각이 갖는 성질들을 살펴본다. 우선 열린사상의 경우부터 시작한다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 

</div>