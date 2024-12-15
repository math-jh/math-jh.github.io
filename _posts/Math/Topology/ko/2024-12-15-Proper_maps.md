---

title: "고유함수"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/proper_maps
header:
    overlay_image: /assets/images/Math/Topology/Proper_maps.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
last_modified_at: 2024-12-15
weight: 17

---

## 보편닫힌사상

일반적으로 연속함수 $f_1:X_1 \rightarrow Y_1$, $f_2: X_2 \rightarrow Y_2$가 닫혀있다 해서 이들의 곱 $f_1\times f_2: X_1\times X_2 \rightarrow Y_1\times Y_2$가 닫혀있을 필요는 없다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 연속함수 $f:X \rightarrow Y$가 *universally closed<sub>보편닫힌사상</sub>*라는 것은 임의의 위상공간 $Z$에 대하여, $f\times\id_Z: X\times Z \rightarrow Y\times Z$가 closed인 것이다.

</div>

$Z=\\{\ast\\}$로 두면 임의의 universally closed map은 closed map인 것을 보일 수 있지만, 그 역은 성립하지 않는다. 하지만 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 만일 $f:X \rightarrow Y$가 연속인 단사함수라면, 다음이 모두 동치이다. 

1. $f$가 universally closed이다.
2. $f$가 closed이다.
3. $f$는 $X$와 $f(X)$ 사이의 homeomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위의 논증에 의해 첫 번째 조건이 성립하면 두 번째 조건이 성립하는 것은 자명하다. 한편, $f$가 injective이므로 $f$의 canonical decomposition을 생각하면 $X$와 $f(X)$ 사이의 homeomorphism이 되는 것을 안다. ([§열린사상과 닫힌사상, ⁋명제 5](/ko/math/topology/open_mappings_and_closed_mappings#prop5)) 이제 세 번째 조건이 성립한다 가정하면, 임의의 $Z$에 대하여 $f\times\id_Z$가 $X\times Z$에서 $Y\times Z$의 닫힌집합 $f(X)\times Z$로의 homeomorphism이므로 원하는 결과를 얻는다.

</details>

그러나 일반적으로는 함수 $f$가 universally closed인 것은 직접 체크해보아야 한다. 다음 명제의 두 번째 결과는 이를 target $Y$에서 살펴볼 수 있다는 것을 보여준다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 연속함수 $f:X \rightarrow Y$가 주어졌다 하자. 그럼 다음이 성립한다.

1. 만일 $f$가 universally closed라면, $Y$의 임의의 부분집합 $A$에 대하여, $f\vert_{f^{-1}(A)}: f^{-1}(A) \rightarrow A$도 universally closed이다.
2. $Y$의 covering $(A\_i)\_{i\in I}$가 (1) locally finite closed covering이거나, (2) $(\interior A\_i)\_{i\in I}$가 $Y$의 open covering이 된다고 하자. 만일 각각의 $f\vert_{f^{-1}(A_i)}$가 universally closed라면, $f$ 또한 그러하다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫째 결과를 보이기 위해 임의의 위상공간 $Z$가 주어졌다 하자. 그럼 $Y$의 임의의 부분집합 $A$에 대하여

$$(f\vert_{f^{-1}(A)})\times \id_Z=(f\times\id_Z)\vert_{f^{-1}(A\times Z)}$$

가 성립한다. 이제 $f$가 universally closed라는 가정으로부터 $f\times\id_Z$는 closed이고, 따라서 $(f\times\id_Z)\vert_{f^{-1}(A\times Z)}$ 또한 closed이다. 

이제 두 번째 결과를 보이자. 주어진 조건을 만족하는 $(A\_i)$가 주어졌다 하면, $(A\_i\times Z)$ 또한 동일한 조건을 만족한다. 이제 만일 $f\vert\_{f^{-1}(A\_i)}$들이 universally closed라면 다음의 함수들

$$(f\times\id_Z)\vert_{f^{-1}(A_i\times Z)}$$

이 closed이므로, $f\times\id_Z$ 또한 그러하다. ([§열린사상과 닫힌사상, ⁋명제 3](/ko/math/topology/open_mappings_and_closed_mappings#prop3))

</details>

또, 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 두 연속함수 $f:X \rightarrow Y$, $g:Y \rightarrow Z$에 대하여 다음이 성립한다.

1. 만일 $f,g$가 모두 universally closed라면, $g\circ f$도 그러하다.
2. 만일 $g\circ f$가 universally closed이고 $f$가 surjective라면 $g$는 universally closed이다. 
3. 만일 $g\circ f$가 universally closed이고 $g$가 injective라면 $f$는 universally closed이다. 
4. $g\circ f$가 universally closed이고 $Y$가 Hausdorff라면 $f$는 universally closed이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

처음 세 결과는 모두 다음의 식

$$(g\circ f)\times\id_Z=(g\times\id_Z)\circ(f\times\id_Z)$$

과 [§열린사상과 닫힌사상, ⁋명제 2](/ko/math/topology/open_mappings_and_closed_mappings#prop2)의 결과들로부터 자명하다. 

마지막 결과의 경우, 두 함수 $\Gamma_f: X \rightarrow X\times Y$와 $\Gamma_g: Y \rightarrow Z\times Y$를 각각 

$$\Gamma_f(x)=(x,f(x)),\qquad \Gamma_g(y)=(g(y), y)$$

으로 정의하자. 그럼 식

$$((g\circ f)\times\id_Y)\circ\Gamma_f=\Gamma_g\circ f$$

이 성립하는 것을 쉽게 확인할 수 있다. 이 때 $\Gamma_f$와 $\Gamma_g$들은 각각 $X, Y$에서 $f,g$의 graph로의 homeomorphism이다. ([§곱공간, ⁋따름정리 4](/ko/math/topology/product_spaces#cor4)) 또, $Y$가 Hausdorff라는 가정으로부터 $\Gamma(f)\subseteq X\times Y$가 닫힌집합임을 안다. ([§하우스도르프 공간, ⁋따름정리 7](/ko/math/topology/Hausdorff_spaces#cor7)) 따라서 [명제 2](#prop2)로부터 $\Gamma_f$가 universally closed인 것을 안다. 한편 어렵지 않게 universally closed map들의 곱은 universally closed인 것을 보일 수 있으므로, 이것과 [명제 4](#prop4)를 종합하면 $(g\circ f)\times\id_Y$가 universally closed임을 안다. 따라서 위의 식의 우변 $\Gamma_g\circ f$ 또한 universally closed이고, $\Gamma_g$가 injective이므로 $f$는 universally closed이다.

</details>

## 옹골성과 보편닫힌사상

아직까지는 이 정의가 옹골성과 관련되어 있는 부분이 보이지 않는데, 이 절에서는 이들 사이의 관계를 살펴본다. 그 전에 [§옹골성, ⁋보조정리 1](/ko/math/topology/compactness#lem1)을 사용하기 위해 filter에 대한 이야기를 조금 해야한다. 

임의의 위상공간 $X$와 그 위의 임의의 filter $\mathcal{F}$가 주어졌다 하자. $X$에 한 점을 추가하여 만든 집합 $X'=X\cup \\{\ast_X\\}$을 생각하고, 이 위의 filter

$$\mathcal{F}'=\{F\cup\{\ast_X\}: F\in \mathcal{F}\}$$

를 생각하자. 이제 $\ast_X$를 제외한 임의의 $x\in X'$에 대하여는 $\mathcal{N}(x)=\uparrow\\{x\\}$으로 정의하고, $\mathcal{N}(\ast_X)=\mathcal{F}'$로 정의하면 이는 [§열린집합, ⁋명제 6](/ko/math/topology/open_sets#prop6)의 네 가지 조건을 모두 만족하며 따라서 $X'$ 위에서의 위상구조가 정의된다. 이 위상공간 $X'$에서, $\ast_X$는 $X$의 closure에 포함되며, $\mathcal{F}=\mathcal{F}'\vert_X=\mathcal{N}(\ast_X)\vert_X$임이 자명하다. 

그럼 다음 보조정리를 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 위상공간 $X$에 대하여, $f: X \rightarrow \\{\ast\\}$이 universally closed라 하자. 그럼 $X$는 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

임의의 $X$ 위의 임의의 filter $\mathcal{F}$에 대하여, 위의 논증으로부터 얻어지는 $X'$를 생각하자. 또, $X\times X'$의 부분집합 $\Delta$를

$$\Delta=\{(x,x): x\in X\}$$

으로 정의하자. 그럼 $\Delta$의 closure $\cl\Delta$를 생각할 수 있으며, 이 때 $f$가 universally closed라는 가정으로부터 $\cl\Delta$의 $f\times\id_{X'}:X\times X'\rightarrow \\{\ast\\}\times X'\cong X'$에 의한 image가 닫힌집합임을 안다. 이제 이 image는 $x$를 포함하므로, $\ast_X$가 closure에 포함된다는 가정으로부터 적당한 $x\in X$가 존재하여 $(x,\ast_X)\in \cl\Delta$임을 안다. 그럼 $x$가 $\mathcal{F}$의 cluster point이고, 따라서 $\mathcal{F}$를 포함하는 ultrafilter를 생각하면 $x$는 그 filter의 limit point임을 안다. 

</details>

위의 보조정리는 그 역 또한 성립한다. 더 일반적으로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> 연속함수 $f:X \rightarrow Y$에 대하여 다음이 동치이다.

1. $f$가 universally closed이다.
2. $f$가 closed이고, 각각의 $y\in Y$에 대하여 $f^{-1}(y)$가 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 조건이 성립한다면 임의의 $y\in Y$에 대하여, $f\vert_{f^{-1}(y)}$가 universally closed임을 알고, 앞선 보조정리로부터 $f^{-1}(y)$가 compact라는 것을 안다. 반대방향은 universally closed map들의 곱이 universally closed라는 것을 사용하면 증명할 수 있다.

</details>

따라서, compact space의 정의를 $f:X \rightarrow \\{\ast\\}$가 universally closed이라는 것으로 했어도 되었을 것이다. 특히 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> 연속함수 $f:X \rightarrow Y$가 universally closed라면, 임의의 compact subset $C\subseteq Y$에 대하여 $f^{-1}(C)$ 또한 compact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$f$가 universally closed이므로 $f\vert_{f^{-1}(C)}$는 universally closed이다. 한편 $C \rightarrow\\{\ast\\}$는 $C$가 compact라는 가정으로부터 universally closed이고, 따라서 합성 $f^{-1}(C) \rightarrow C \rightarrow \\{\ast\\}$는 universally closed이므로 $f^{-1}(C)$도 compact이다. 

</details>

## 고유함수

[따름정리 7](#cor7)의 결과를 만족하는 함수 $f$를 *proper map<sub>고유함수</sub>*라 부른다. 다음 명제는 특별한 경우에서 위의 따름정리의 역 또한 성립한다는 것을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Hausdorff space들 사이의 연속함수 $f:X \rightarrow Y$가 주어졌다 하고, 추가로 $Y$가 locally compact라 가정하자. 그럼 $f$가 universally closed인 것과 $f$가 proper인 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

앞서 언급한 것과 같이, $f$가 universally closed라면 $f$가 proper라는 것은 [따름정리 7](#cor7)의 결과이다. 

따라서 이 명제의 핵심은 역방향이다. $Y$가 locally compact이므로, 적당한 compact set들 안에 포함되는 열린집합들로 이루어진 $Y$의 open covering $(U_i)$가 존재한다. 그럼 $f^{-1}(\cl U_i)$들은 $X$에서 compact이고 각각의 $f\vert_{f^{-1}(\cl U_i)}$가 universally closed이다. 이제 [명제 3](#prop3)으로부터 원하는 결과를 얻는다. 

</details>

특히 이는 앞서 살펴본 one-point compactification에 적용하여 다음 결과를 준다.

<div class="proposition" markdown="1">

<ins id="cor9">**따름정리 9**</ins> 두 locally compact Hausdorff space $X_1,X_2$가 주어졌다 하고, 이들의 one-point compactification $\overline{X}_i=X\cup \\{\ast_i\\}$가 주어졌다 하자. 그럼 $f:X_1: X_2$가 universally closed인 것은 다음 식

$$\overline{f}(x)=\begin{cases}\ast_2&\text{if $x=\ast_1$}\\f(x)&\text{otherwise}\end{cases}$$

으로 정의한 $\overline{f}:\overline{X}_1 \rightarrow \overline{X}_2$가 연속인 것과 동치이다.

</div>