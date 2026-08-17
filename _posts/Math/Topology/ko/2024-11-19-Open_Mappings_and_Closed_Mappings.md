---
title: "열린사상과 닫힌사상"
description: "위상공간 사이 함수의 열린사상과 닫힌사상을 정의하고, 합성·전사·단사 함수에 대한 기본 성질을 다룬다. 열린사상 및 닫힌사상의 판별 조건도 함께 살펴본다."
excerpt: "Open map과 closed map의 정의 및 quotient map과의 관계"

categories: [Math / Topology]
permalink: /ko/math/topology/open_mappings_and_closed_mappings
sidebar: 
    nav: "topology-ko"

date: 2024-11-19
weight: 12
revising: true
drift_needed: true

---

## 정의와 기본적인 성질들

::: 정의 1
임의의 두 위상공간 $X,Y$와 함수 $f:X \rightarrow Y$에 대하여 다음을 정의한다. 

1. 만일 $X$의 임의의 열린집합 $U$에 대하여 $f(U)$가 항상 $Y$의 열린집합이라면 $f$를 *open mapping<sub>열린사상</sub>*이라 부른다. 
2. 만일 $X$의 임의의 닫힌집합 $A$에 대하여 $f(A)$가 항상 $Y$의 닫힌집합이라면 $f$를 *closed mapping<sub>닫힌사상</sub>*이라 부른다. 
:::

그럼 다음이 성립한다.

::: 명제 2
위상공간 $X,Y,Z$와 함수 $f:X \rightarrow Y$, $g:Y \rightarrow Z$가 주어졌다 하자. 그럼 다음이 성립한다. 

1. 만일 $f, g$가 모두 open (resp. closed)이라면 $g\circ f$ 또한 open (resp. closed)이다.
2. 만일 $g\circ f$가 open (resp. closed)이고 $f$가 continuous surjection이라면 $g$는 open (resp. closed)이다. 
3. 만일 $g\circ f$가 open (resp. closed)이고 $g$가 continuous injection이라면 $f$는 open (resp. closed)이다. 
:::
::: 증명
1. $X$의 임의의 열린집합 (resp. 닫힌집합) $U$에 대하여 $f$가 open (resp. closed)이므로 $f(U)$는 $Y$의 열린집합 (resp. 닫힌집합)이고, 다시 $g$가 open (resp. closed)이므로 $g(f(U))$는 $Z$의 열린집합 (resp. 닫힌집합)이다. 
2. $Y$의 임의의 열린집합 $V$가 주어졌다 하자. 그럼 $f$는 연속이므로 $f^{-1}(V)$는 $X$의 열린집합이고, 따라서
    
    $$(g\circ f)(f^{-1}(V))=g(f(f^{-1}(V)))=g(V)$$

    가 성립하므로 $g(V)$는 $Z$의 열린집합이다. 여기서 $f(f^{-1}(V))=V$인 것은 $f$가 전사함수임을 이용하였다. ([\[집합론\] §Retraction과 section](/ko/math/set_theory/retraction_and_section)) 한편 마찬가지 방식으로 $Y$의 임의의 닫힌집합 $B$가 주어졌다 하면 [§연속함수, ⁋정리 4](/ko/math/topology/continuous_functions#thm4)에 의하여 위와 동일한 논증을 적용할 수 있다.
3. 둘째 증명과 마찬가지로 open인 경우만 생각하면 충분하다. $X$의 임의의 열린집합 $U$에 대하여, $g\circ f$가 open이므로 $g(f(U))$는 open이고, 따라서 $g$가 연속이라는 것과 $g$가 단사함수라는 것을 사용하면 다음 식
    
    $$g^{-1}(g(f(U)))=f(U)$$

    로부터 $f(U)$가 열린집합임을 안다. ([\[집합론\] §Retraction과 section](/ko/math/set_theory/retraction_and_section))
:::

다음 명제는 위상공간 사이의 함수가 언제 open 또는 closed인지를 판별하는데 도움이 된다.

::: 명제 3
두 위상공간 사이의 함수 $f:X \rightarrow Y$가 주어졌다 하자. 그럼 다음이 성립한다.

1. 만일 $f$가 open (resp. closed)라면, $Y$의 임의의 부분집합 $A$에 대하여 $f\vert_{f^{-1}(A)}: f^{-1}(A) \rightarrow A$도 open (resp. closed)이다.
2. $Y$의 covering $(A_i)_{i\in I}$가 (1) locally finite closed covering이거나, (2) $(\interior A_i)_{i\in I}$가 $Y$의 open covering이 된다고 하자. 만일 각각의 $f\vert_{f^{-1}(A_i)}$가 open (resp. closed)라면, $f$ 또한 그러하다. 
:::
::: 증명
첫 번째 결과를 보이기 위해 $f^{-1}(A)$에서의 열린집합 (resp. 닫힌집합)을 택하자. 그럼 $X$에서의 열린집합 (resp. 닫힌집합) $U$가 존재하여 이를 $U\cap f^{-1}(A)$ 꼴로 적을 수 있다. 따라서

$$f\vert_{f^{-1}(A)}(U\cap f^{-1}(A))=f(U)\cap A$$

이고, 가정에 의하여 $f(U)$가 열린집합 (resp. 닫힌집합)이므로 원하는 결과를 얻는다.

두 번째 결과도 비슷하게 증명할 수 있는데, $X$에서의 열린집합 (resp. 닫힌집합) $U$가 주어졌다 하고, $U_i$를 다음 식

$$U_i=U\cap f^{-1}(A_i)$$

으로 정의하자. 그럼 $U_i$는 $f^{-1}(A_i)$의 열린집합 (resp. 닫힌집합)이고 첫 번째 결과에서와 같은 계산으로 $f\vert_{f^{-1}(A_i)}(U_i)=f(U)\cap A_i$를 얻으므로, 가정에 의하여 $f(U)\cap A_i$는 모든 $i$에 대하여 부분공간 $A_i$의 열린집합 (resp. 닫힌집합)이다. 이는 $f(U)\cap A_i$가 $Y$의 열린집합 (resp. 닫힌집합)이라는 뜻이 아니므로, $B=f(U)$와 $B_i=B\cap A_i$로 적고 $(A_i)$에 주어진 두 조건을 각각 사용하여야 한다.

가정 (1)에서는 $A_i$가 $Y$의 닫힌집합이므로 $A_i$의 닫힌집합이 곧 $Y$의 닫힌집합이 되고, $B_i\subseteq A_i$이므로 $(B_i)$와 $(A_i\setminus B_i)$ 또한 locally finite이다. 따라서 각각의 $f\vert_{f^{-1}(A_i)}$가 closed라면 $B_i$는 $Y$의 닫힌집합이므로 [§집합의 내부, 폐포, 경계, ⁋명제 4](/ko/math/topology/other_concepts#prop4)에 의하여 $B=\bigcup_{i\in I}B_i$가 닫힌집합이다. 각각의 $f\vert_{f^{-1}(A_i)}$가 open이라면 $A_i\setminus B_i$가 $A_i$의, 따라서 $Y$의 닫힌집합이고, 같은 명제에 의하여 $\bigcup_{i\in I}(A_i\setminus B_i)$는 닫힌집합이다. 그런데 $(A_i)$가 $Y$의 covering이므로 이 합집합은 $Y\setminus B$와 같고, 결국 $B$는 열린집합이 된다.

가정 (2)에서는 $\interior A_i\subseteq A_i$인 것을 이용한다. 각각의 $f\vert_{f^{-1}(A_i)}$가 open이라 하면 $Y$의 열린집합 $O_i$가 존재하여 $B_i=O_i\cap A_i$이고, 따라서 $B\cap\interior A_i=B_i\cap\interior A_i=O_i\cap\interior A_i$는 $Y$의 열린집합이다. $(\interior A_i)$가 $Y$의 covering이므로 $B=\bigcup_{i\in I}(B\cap\interior A_i)$가 되어 $B$는 열린집합이다. 각각의 $f\vert_{f^{-1}(A_i)}$가 closed인 경우에는 $Y$의 열린집합 $O_i$를 $A_i\setminus B_i=O_i\cap A_i$이도록 잡으면 $\interior A_i\setminus B=\interior A_i\cap(A_i\setminus B_i)=O_i\cap\interior A_i$가 $Y$의 열린집합이고, $Y\setminus B=\bigcup_{i\in I}(\interior A_i\setminus B)$이므로 $B$는 닫힌집합이 된다. 
:::

## 동치관계들

::: 정의 4
위상공간 $X$ 위에 정의된 동치관계 $R$이 *open (resp. closed)*이라는 것은 canonical map $X \rightarrow X/R$이 open (resp. closed)인 것이다. 
:::

아래에서 $R$은 연속함수 $f$에 의해 정의된 동치관계를 뜻하고 ([\[집합론\] §동치관계의 예시들, ⁋정의 2](/ko/math/set_theory/examples_of_equivalence#def2)), $p$는 canonical projection, $i$는 canonical injection, $h$는 canonical decomposition에서 얻어지는 전단사함수를 뜻한다. ([\[집합론\] §동치관계의 예시들, §§Canonical decomposition](/ko/math/set_theory/examples_of_equivalence#canonical-decomposition)) 이때 $f(X)$에 부분위상을 부여하면 [§몫공간, ⁋명제 4](/ko/math/topology/quotient_spaces#prop4)와 [§Initial topology와 final topology, ⁋명제 3](/ko/math/topology/initial_and_final_topology#prop3)에 의하여 $h$는 연속이다.

그럼 다음이 성립하는 것을 쉽게 보일 수 있다.

::: 명제 5
두 위상공간 $X,Y$ 사이의 연속함수 $f:X \rightarrow Y$와 $f$의 canonical decomposition

$$X \overset{p}{\longrightarrow} X/R \overset{h}{\longrightarrow} f(X)\overset{i}{\longrightarrow}Y$$

를 생각하자. 그럼 다음이 모두 동치이다.

1. $f$가 open (resp. closed)이다.
2. $p,h,i$가 모두 open (resp. closed)이다.
3. $R$이 open (resp. closed)이고, $h$는 homeomorphism이며 $f(X)$는 $Y$의 open (resp. closed) subset이다.
:::

## 열린사상의 성질들

이제 우리는 open mapping과 closed mapping 각각이 갖는 성질들을 살펴본다. 우선 open mapping의 경우부터 시작한다. 

::: 명제 6
:::

---

**참고문헌**

**[Bou]** N. Bourbaki, <i>General Topology</i>. Elements of mathematics. Springer, 1995.
