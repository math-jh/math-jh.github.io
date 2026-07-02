---
title: "Paracompact 공간과 단위분할"
description: "임의의 열린 덮개가 국소유한 세분을 갖는 paracompact 공간을 정의하고, paracompact Hausdorff 공간이 normal임과 단위분할의 존재를 Urysohn 보조정리로 증명하여 국소 구성을 대역화하는 도구를 마련한다."
excerpt: "Paracompact spaces, local finiteness, and partitions of unity"

categories: [Math / Topology]
permalink: /ko/math/topology/paracompact_spaces
sidebar: 
    nav: "topology-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 16.6

published: false

---

## 국소성과 대역성의 가교

위상공간 위에서 우리가 다루려는 대상은 흔히 국소적으로 먼저 주어진다. 각 점 근방에서 정의된 연속함수, 국소적으로 얻어진 절단, 좌표조각마다 놓인 구성이 그러하다. 이러한 국소적 자료를 하나의 대역적 대상으로 이어 붙이려면, 각 조각을 자기 정의역 안에서 부드럽게 소멸시키면서 전체에 걸쳐 값이 겹치지 않게 배분하는 장치가 필요하다. 이 역할을 하는 표준적인 도구가 *partition of unity*이며, 그것이 자연스럽게 존재하는 무대가 바로 이 글에서 다루는 paracompact Hausdorff 공간이다.

Compactness는 임의의 열린 덮개에서 유한한 부분덮개를 뽑아낼 것을 요구하지만 ([§옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1)), 우리가 실제로 다루는 공간의 대부분은 compact가 아니다. Paracompactness는 유한성 대신 국소유한성을 요구하여 compactness를 알맞게 약화시킨 조건으로, compact 공간에서 성립하던 여러 논증을 국소적으로 되살릴 수 있게 해 준다. 우리는 이 개념을 도입하고, paracompact Hausdorff 공간이 normal임을 보인 뒤, 이를 발판으로 임의의 열린 덮개에 종속된 단위분할을 언제나 구성할 수 있음을 증명한다.

## Paracompact 공간

열린 덮개를 더 잘게 쪼개어 각 조각이 원래 덮개의 어느 한 조각 안에 온전히 들어가도록 만드는 조작을 먼저 이름 붙인다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $$X$$의 두 덮개 $$(U_i)_{i\in I}$$와 $$(V_j)_{j\in J}$$가 주어졌다 하자. 후자가 전자의 *세분<sub>refinement</sub>*이라는 것은 임의의 $$j\in J$$에 대하여 $$V_j\subseteq U_i$$를 만족하는 $$i\in I$$가 존재하는 것이다. 세분 $$(V_j)_{j\in J}$$의 모든 원소가 열린집합일 때 이를 *open refinement*라 부른다.

</div>

세분은 부분덮개보다 훨씬 유연한 개념이다. 부분덮개가 원래 덮개의 조각들 가운데 일부를 그대로 골라내는 것인 데 반해, 세분은 각 조각을 원래의 어느 한 조각 안에 갇히기만 하면 자유롭게 잘게 나누는 것을 허용한다. 여기에 국소유한성을 결합하면 compactness를 대신할 새로운 유한성 조건을 얻는다. Family $$(A_i)_{i\in I}$$가 *locally finite*라는 것은 임의의 점이 유한 개의 $$A_i$$만을 만나는 근방을 갖는 것이었음을 상기한다. ([§집합의 내부, 폐포, 경계, ⁋정의 3](/ko/math/topology/other_concepts#def3))

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위상공간 $$X$$가 *paracompact*라는 것은 $$X$$의 임의의 open covering이 locally finite open refinement를 갖는 것이다.

</div>

우리는 이 개념을 [§옹골성, ⁋정의 5](/ko/math/topology/compactness#def5)에서 이미 도입한 바 있으며, 이 글의 출발점으로 삼기 위해 여기에 다시 적는다. 정의는 임의의 열린 덮개에 대하여 그것을 세분하는 국소유한 열린 덮개가 존재할 것을 요구한다. Compactness가 요구하는 것은 임의의 열린 덮개에서 유한 개만 남겨도 여전히 전체를 덮는다는 것인데, 유한 개의 열린집합으로 이루어진 덮개는 그 자체로 국소유한이므로, paracompactness는 compactness가 요구하는 유한성을 각 점 주위에서의 유한성으로 완화한 것이라 읽을 수 있다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 임의의 compact space는 paracompact이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 compact space라 하고 open covering $$(U_i)_{i\in I}$$가 주어졌다 하자. Compactness에 의하여 유한한 $$J\subseteq I$$가 존재하여 $$(U_j)_{j\in J}$$가 여전히 $$X$$를 덮는다. ([§옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1)) 이 유한한 부분덮개는 원래 덮개의 open refinement이며, 유한한 family는 언제나 locally finite이므로 ([§집합의 내부, 폐포, 경계, ⁋정의 3](/ko/math/topology/other_concepts#def3)) 이는 $$(U_i)_{i\in I}$$의 locally finite open refinement이다. 따라서 $$X$$는 paracompact이다.

</details>

Paracompactness가 compactness보다 실질적으로 넓은 조건임은 compact가 아닌 공간에서 확인해야 한다. 다음은 그 대표적인 경우로, 유한성이 전혀 없는 Euclidean space에서도 국소유한 세분을 명시적으로 만들어 낼 수 있음을 보여 준다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> Euclidean space $$\mathbb{R}^n$$은 paracompact이다. $$\mathbb{R}^n$$은 유계가 아니어서 compact가 아니지만, 원점을 중심으로 반경이 커지는 열린 공들로 공간을 소진시켜 국소유한 세분을 얻을 수 있다.

임의의 open covering $$\mathcal{U}=(U_i)_{i\in I}$$가 주어졌다 하자. 각 정수 $$k\geq 1$$에 대하여 반경 $$k$$인 열린 공 $$B_k=\{x\mid\lVert x\rVert<k\}$$을 두고, $$B_0=B_{-1}=\emptyset$$이라 약속한다. 그럼 껍질

$$A_k=\cl(B_k)\setminus B_{k-1}=\{x\mid k-1\leq\lVert x\rVert\leq k\}$$

은 $$\mathbb{R}^n$$의 닫힌 유계 부분집합이므로 Heine–Borel 정리에 의해 compact이고, 이들의 합집합은 $$\mathbb{R}^n$$ 전체이다. 한편

$$O_k=B_{k+1}\setminus\cl(B_{k-2})$$

은 열린집합으로 $$A_k\subseteq O_k$$를 만족한다. 여기서 $$k\geq 3$$이면 $$O_k=\{x\mid k-2<\lVert x\rVert<k+1\}$$이고, $$k=1,2$$일 때는 $$B_{k-2}=\emptyset$$이라 $$\cl(B_{k-2})=\emptyset$$이므로 $$O_k=B_{k+1}$$이다.

이제 각 $$k$$에 대하여 compact 집합 $$A_k$$를 다룬다. 각 $$x\in A_k$$는 어떤 $$U_{i}$$에 속하므로 $$x\in U_i\cap O_k$$이며, 이러한 열린집합들이 $$A_k$$를 덮는다. $$A_k$$가 compact이므로 유한 개의 $$i$$, 곧 유한집합 $$F_k\subseteq I$$를 택하여 $$(U_i\cap O_k)_{i\in F_k}$$이 $$A_k$$를 덮도록 할 수 있다. ([§옹골공간, ⁋명제 2](/ko/math/topology/compact_spaces#prop2)) 모든 $$k\geq 1$$에 걸쳐 모은 family

$$\mathcal{V}=(U_i\cap O_k)_{k\geq 1,i\in F_k}$$

를 생각하자. 각 원소는 열린집합이며 $$U_i$$에 포함되므로 $$\mathcal{V}$$는 $$\mathcal{U}$$의 open refinement이고, $$A_k$$들이 $$\mathbb{R}^n$$을 덮으므로 $$\mathcal{V}$$도 $$\mathbb{R}^n$$을 덮는다. 끝으로 $$\mathcal{V}$$가 locally finite임을 본다. 점 $$x$$에 대하여 $$r=\lVert x\rVert$$이라 두면 근방 $$B_{r+1}=\{y\mid\lVert y\rVert<r+1\}$$은 $$O_k$$와 만나는 경우 $$k-2<r+1$$, 곧 $$k<r+3$$일 때뿐이므로 유한 개의 $$k$$에 대해서만 $$O_k$$와 만난다. 각 $$k$$마다 $$\mathcal{V}$$의 원소는 유한 개($$F_k$$개)뿐이므로, $$B_{r+1}$$은 $$\mathcal{V}$$의 유한히 많은 원소만을 만난다. 따라서 $$\mathcal{V}$$는 locally finite open refinement이고 $$\mathbb{R}^n$$은 paracompact이다.

</div>

이 예시의 논증은 $$\mathbb{R}^n$$의 특수성보다는 두 가지 성질, 곧 국소적 옹골성과 가산 개의 compact 집합으로의 소진에만 의존한다. 실제로 같은 방법으로 임의의 second countable LCH space, 나아가 임의의 $$\sigma$$-compact LCH space가 paracompact임을 보일 수 있다. 이는 뒤에서 다룰 위상다양체의 paracompactness의 바탕이 된다.

## Paracompact Hausdorff 공간의 정규성

Paracompactness의 위력은 Hausdorff 조건과 결합될 때 비로소 드러난다. Compact Hausdorff space가 normal이었던 것과 마찬가지로 ([§옹골공간, ⁋명제 7](/ko/math/topology/compact_spaces#prop7)), paracompact Hausdorff space도 normal임을 보이는 것이 이 절의 목표이다. 정규성이 확보되면 Urysohn 보조정리를 통해 풍부한 연속함수를 얻을 수 있고, 이것이 단위분할 구성의 핵심 재료가 된다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋정리 2](/ko/math/topology/urysohn_and_tietze#thm2))

증명은 국소유한 family의 다음 성질에 반복적으로 의존한다. 국소유한 family에서는 합집합의 closure가 각 원소의 closure의 합집합과 일치하여, closure 연산이 무한 합집합과 자유롭게 교환된다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> 위상공간 $$X$$의 부분집합들의 family $$(A_i)_{i\in I}$$가 locally finite라 하자. 그럼

$$\cl\Bigl(\bigcup_{i\in I} A_i\Bigr)=\bigcup_{i\in I}\cl(A_i)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 $$i$$에 대하여 $$A_i\subseteq\bigcup_j A_j$$이므로 $$\cl(A_i)\subseteq\cl(\bigcup_j A_j)$$이고, 따라서 $$\bigcup_i\cl(A_i)\subseteq\cl(\bigcup_j A_j)$$이다.

반대 포함을 위해 $$\bigcup_i\cl(A_i)$$가 닫힌집합임을 보이면 충분하다. 이 집합이 닫혀 있으면 $$\bigcup_i A_i\subseteq\bigcup_i\cl(A_i)$$의 closure 역시 $$\bigcup_i\cl(A_i)$$에 포함되기 때문이다. 먼저 family $$(\cl(A_i))_{i\in I}$$가 locally finite임을 관찰한다. 점 $$x$$의 근방 $$V$$가 $$V\cap A_i\neq\emptyset$$을 만족하는 $$i$$를 유한 개만 갖도록 잡을 수 있는데, $$V$$를 열린집합으로 택하면 $$V\cap\cl(A_i)\neq\emptyset$$일 때마다 $$V$$가 $$\cl(A_i)$$의 점의 근방이므로 $$V\cap A_i\neq\emptyset$$이다. 따라서 $$V$$는 유한 개의 $$\cl(A_i)$$만을 만나며, $$(\cl(A_i))_{i\in I}$$도 locally finite이다. 이는 닫힌집합들의 locally finite family이므로 그 합집합 $$\bigcup_i\cl(A_i)$$는 닫힌집합이다. ([§집합의 내부, 폐포, 경계, ⁋명제 4](/ko/math/topology/other_concepts#prop4))

</details>

이제 paracompact Hausdorff space가 regular임을 먼저 보인다. 논증의 골격은 다음과 같다. 점과 닫힌집합을 분리하려 할 때, Hausdorff성으로부터 닫힌집합의 각 점을 그 점의 closure가 문제의 점을 피하도록 감싸는 열린집합을 얻고, 이들과 닫힌집합의 여집합으로 이루어진 열린 덮개를 paracompactness로 국소유한하게 세분한 뒤 [보조정리 5](#lem5)로 closure를 통제한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 임의의 paracompact Hausdorff space는 regular space이다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 paracompact Hausdorff space라 하고, 점 $$a\in X$$와 이를 포함하지 않는 닫힌집합 $$B\subseteq X$$가 주어졌다 하자. 각 $$b\in B$$에 대하여 $$a\neq b$$이므로 $$X$$의 Hausdorff성에 의해 서로소인 열린집합 $$P_b\ni a$$와 $$U_b\ni b$$가 존재한다. $$U_b\subseteq X\setminus P_b$$이고 $$X\setminus P_b$$는 닫힌집합이므로 $$\cl(U_b)\subseteq X\setminus P_b$$이며, 특히 $$a\notin\cl(U_b)$$이다.

Family $$(U_b)_{b\in B}$$에 열린집합 $$X\setminus B$$를 더하면 $$X$$의 open covering을 이룬다. $$X$$가 paracompact이므로 이 덮개의 locally finite open refinement $$\mathcal{C}$$를 택한다. $$\mathcal{C}$$의 원소 가운데 $$B$$와 만나는 것들을 모아 $$\mathcal{D}=\{C\in\mathcal{C}\mid C\cap B\neq\emptyset\}$$이라 두자. $$\mathcal{D}$$의 각 원소 $$C$$는 세분의 성질에 의해 $$X\setminus B$$나 어떤 $$U_b$$에 포함되는데, $$C$$가 $$B$$와 만나므로 $$X\setminus B$$에는 포함될 수 없고 따라서 어떤 $$U_b$$에 포함되어 $$a\notin\cl(C)$$이다. 또한 $$B$$의 각 점은 자신을 품는 $$\mathcal{C}$$의 원소에 속하고 그 원소는 $$B$$와 만나므로 $$\mathcal{D}$$에 든다. 즉 $$\mathcal{D}$$는 $$B$$를 덮는다.

$$V=\bigcup\mathcal{D}$$라 두면 $$V$$는 $$B$$를 포함하는 열린집합이다. $$\mathcal{D}$$는 locally finite family $$\mathcal{C}$$의 부분족이므로 locally finite이고, [보조정리 5](#lem5)에 의하여 $$\cl(V)=\bigcup_{C\in\mathcal{D}}\cl(C)$$이다. 각 $$\cl(C)$$가 $$a$$를 포함하지 않으므로 $$a\notin\cl(V)$$이다. 그럼 $$W=X\setminus\cl(V)$$은 $$a$$를 품는 열린집합이며 $$V\supseteq B$$와 서로소이다. 따라서 $$a$$와 $$B$$는 근방으로 분리가능하고 $$X$$는 regular이다.

</details>

같은 논증을 점 $$a$$ 대신 닫힌집합 $$A$$에 대해 펼치면 정규성을 얻는다. 이때 Hausdorff성 대신 방금 증명한 regularity를 사용하여 $$B$$의 각 점을 감싸는 열린집합의 closure가 $$A$$를 피하도록 만든다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> 임의의 paracompact Hausdorff space는 normal space이다. ([§하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3))

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$X$$가 paracompact Hausdorff space라 하고 서로소인 두 닫힌집합 $$A,B\subseteq X$$가 주어졌다 하자. $$X$$는 [명제 6](#prop6)에 의하여 regular이다. 각 $$b\in B$$에 대하여 $$b\notin A$$이므로 regularity를 점 $$b$$와 닫힌집합 $$A$$에 적용하면 서로소인 열린집합 $$U_b\ni b$$와 $$Q_b\supseteq A$$를 얻는다. $$U_b\subseteq X\setminus Q_b$$이고 $$X\setminus Q_b$$가 닫힌집합이므로 $$\cl(U_b)\subseteq X\setminus Q_b\subseteq X\setminus A$$이며, 곧 $$\cl(U_b)\cap A=\emptyset$$이다.

Family $$(U_b)_{b\in B}$$에 열린집합 $$X\setminus B$$를 더한 open covering의 locally finite open refinement $$\mathcal{C}$$를 paracompactness로 택하고, $$\mathcal{D}=\{C\in\mathcal{C}\mid C\cap B\neq\emptyset\}$$이라 두자. [명제 6](#prop6)의 증명에서와 같이 $$\mathcal{D}$$의 각 원소는 어떤 $$U_b$$에 포함되어 $$\cl(C)\cap A=\emptyset$$이고, $$\mathcal{D}$$는 $$B$$를 덮는다.

$$V=\bigcup\mathcal{D}$$는 $$B$$를 포함하는 열린집합이며, $$\mathcal{D}$$가 locally finite이므로 [보조정리 5](#lem5)에 의하여 $$\cl(V)=\bigcup_{C\in\mathcal{D}}\cl(C)$$이고 이는 $$A$$와 서로소이다. 따라서 $$W=X\setminus\cl(V)$$은 $$A$$를 품는 열린집합으로 $$V\supseteq B$$와 서로소이다. 그럼 $$V$$와 $$W$$가 각각 $$B$$와 $$A$$를 담는 서로소인 열린집합이므로 $$X$$는 normal이다.

</details>

[정리 7](#thm7)은 compact Hausdorff space가 normal이라는 사실의 진정한 일반화이다. 실제로 [명제 3](#prop3)에 의하여 compact space는 paracompact이므로, compact Hausdorff space가 normal이라는 결과는 [정리 7](#thm7)의 특수한 경우로 다시 얻어진다. 정규성이 확보되었으므로 우리는 이제 서로소인 두 닫힌집합을 가르는 연속함수를 언제나 얻을 수 있으며, 이것이 다음 절의 단위분할 구성을 가능하게 한다.

Paracompact 공간의 가장 풍부한 공급원 가운데 하나는 metric space이다. 모든 metric space가 normal임은 이미 알고 있으나 ([§Urysohn 보조정리와 Tietze 확장정리, ⁋명제 4](/ko/math/topology/urysohn_and_tietze#prop4)), 사실 이들은 언제나 paracompact이기도 하다. 이는 A. H. Stone의 정리로 알려져 있다.

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> (Stone) 임의의 metric space는 paracompact이다.

</div>
<details class="proof" markdown="1">
<summary>증명 (개요)</summary>

증명의 핵심 착상만 밝히고 세부는 표준적인 문헌을 따른다. **[Mun]** Metric $$d$$를 가진 공간 $$X$$와 open covering $$(U_\alpha)_{\alpha\in J}$$가 주어졌다 하자. 우선 선택공리를 사용하여 첨수집합 $$J$$에 정렬순서를 준다. 각 정수 $$n\geq 1$$과 각 $$\alpha$$에 대하여, $$U_\alpha$$의 점 가운데 경계로부터 적어도 $$2^{-n}$$만큼 떨어져 있고, 순서상 앞선 어떤 $$U_\beta$$의 그러한 대응 집합에도 이미 들어 있지 않은 점들만을 남긴 뒤, 그 점들을 중심으로 반경 $$2^{-n-1}$$인 열린 공들을 합쳐 집합 $$V_{n,\alpha}$$을 정의한다. 이때 $$\alpha$$에 대한 정렬순서와 반경의 기하급수적 축소가 맞물려, family $$(V_{n,\alpha})$$는 $$(U_\alpha)$$를 세분하는 열린 덮개가 되며 동시에 locally finite이다. 각 점 $$x$$에 대하여, $$x$$가 처음 덮이는 단계의 지표 $$n$$을 보면 반경 $$2^{-n-1}$$ 정도의 근방이 유한히 많은 $$V_{n',\alpha}$$만을 만나기 때문이다. 따라서 $$X$$는 paracompact이다. 이 구성은 M. E. Rudin이 정리한 형태로 널리 알려져 있다.

</details>

## 단위분할의 존재

이제 국소적 자료를 대역적으로 이어 붙이는 도구인 단위분할을 정식화한다. 연속함수 $$\phi:X\to[0,1]$$의 *support<sub>지지</sub>*를 $$\supp\phi=\cl(\{x\in X\mid\phi(x)\neq 0\})$$으로 정의하며, 이는 $$\phi$$가 $$0$$이 아닌 값을 갖는 영역을 담는 가장 작은 닫힌집합이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> 위상공간 $$X$$ 위의 연속함수들의 family $$(\phi_i)_{i\in I}$$가 *partition of unity<sub>단위분할</sub>*이라는 것은 각 $$\phi_i:X\to[0,1]$$이 다음 두 조건을 만족하는 것이다.

1. Family $$(\supp\phi_i)_{i\in I}$$는 locally finite이다.
2. 임의의 $$x\in X$$에 대하여 $$\sum_{i\in I}\phi_i(x)=1$$이 성립한다.

나아가 $$X$$의 open covering $$(U_i)_{i\in I}$$가 주어졌을 때, 같은 첨수집합으로 놓인 partition of unity $$(\phi_i)_{i\in I}$$가 모든 $$i$$에 대하여 $$\supp\phi_i\subseteq U_i$$를 만족하면 이를 *$$(U_i)$$에 종속된<sub>subordinate</sub>* 단위분할이라 부른다.

</div>

이 개념 역시 [§옹골성, ⁋정의 6](/ko/math/topology/compactness#def6)에서 이미 도입하였다. 첫째 조건의 국소유한성은 둘째 조건의 합 $$\sum_i\phi_i(x)$$이 각 점의 어떤 근방에서 유한합으로 환원되어 실제로 의미를 가지도록 보장한다. 종속성 조건 $$\supp\phi_i\subseteq U_i$$은 각 $$\phi_i$$가 $$U_i$$ 바깥에서는 물론 $$U_i$$의 경계 부근에서까지 소멸함을 뜻하므로, $$U_i$$ 위에서만 정의된 국소적 자료에 $$\phi_i$$를 곱하면 그 곱을 $$X$$ 전체로 $$0$$을 채워 연속적으로 연장할 수 있게 된다. 이것이 단위분할이 국소 구성을 대역화하는 원리이다.

존재 증명의 관건은 정규성만으로는 부족하고, 덮개를 두 번 "수축"시켜 닫힌집합이 여전히 전체를 덮게 만드는 데에 있다. 이를 위한 보조정리를 먼저 마련한다. Family $$(U_i)_{i\in I}$$가 *point-finite<sub>점별유한</sub>*라는 것은 각 점 $$x\in X$$가 유한 개의 $$U_i$$에만 속하는 것을 말하며, locally finite family는 언제나 point-finite이다.

<div class="proposition" markdown="1">

<ins id="lem10">**보조정리 10**</ins> (Shrinking lemma) Normal space $$X$$의 point-finite open covering $$(U_\alpha)_{\alpha\in J}$$가 주어졌다 하자. 그럼 open covering $$(V_\alpha)_{\alpha\in J}$$가 존재하여 모든 $$\alpha$$에 대하여 $$\cl(V_\alpha)\subseteq U_\alpha$$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

선택공리를 사용하여 첨수집합 $$J$$에 정렬순서를 준다. 우리는 초한귀납법으로 각 $$\alpha\in J$$마다 열린집합 $$V_\alpha$$를 정의하되, 다음의 불변식이 모든 단계에서 유지되도록 한다.

$$(\ast_\alpha)\qquad \{V_\beta\mid\beta<\alpha\}\cup\{U_\beta\mid\beta\geq\alpha\}\ \text{가}\ X\ \text{를 덮는다.}$$

먼저 $$(\ast_\alpha)$$가 임의의 $$\alpha$$에서 성립함을 point-finiteness로부터 확인한다. $$\beta<\alpha$$인 각 $$\beta$$에 대해 이미 $$V_\beta$$가 $$\cl(V_\beta)\subseteq U_\beta$$를 만족하도록 정의되었다고 하자. 점 $$x\in X$$가 주어지면 $$x$$는 유한 개의 $$U_\gamma$$에만 속한다. 만일 이들 가운데 $$\gamma\geq\alpha$$인 것이 있으면 $$x$$는 $$U_\gamma$$로 덮인다. 그렇지 않다면 $$x\in U_\gamma$$인 모든 $$\gamma$$는 $$\alpha$$보다 작으며, 이러한 $$\gamma$$ 가운데 가장 큰 것을 $$\gamma_0$$이라 하자. 이미 성립하는 $$(\ast_{\gamma_0})$$에 의하여 $$x$$는 $$\{V_\beta\mid\beta\leq\gamma_0\}\cup\{U_\beta\mid\beta>\gamma_0\}$$ 가운데 하나로 덮이는데, $$\gamma_0$$의 최대성에 의해 $$\beta>\gamma_0$$이면 $$x\notin U_\beta$$이므로 $$x$$는 어떤 $$V_\beta$$($$\beta\leq\gamma_0<\alpha$$)로 덮인다. 어느 경우든 $$x$$는 $$(\ast_\alpha)$$의 family로 덮이므로 $$(\ast_\alpha)$$가 성립한다.

이제 $$\beta<\alpha$$에 대해 $$V_\beta$$가 정의되었다 할 때 $$V_\alpha$$를 정의한다. 집합

$$C_\alpha=X\setminus\Bigl(\bigcup_{\beta<\alpha}V_\beta\cup\bigcup_{\beta>\alpha}U_\beta\Bigr)$$

은 닫힌집합이다. $$(\ast_\alpha)$$에 의하여 이 여집합의 밖에 있는 점, 곧 $$C_\alpha$$의 점은 어떤 $$V_\beta$$($$\beta<\alpha$$)나 $$U_\beta$$($$\beta>\alpha$$)에도 속하지 않으므로 반드시 $$U_\alpha$$에 속한다. 즉 $$C_\alpha\subseteq U_\alpha$$이다. $$X$$가 normal이므로 닫힌집합 $$C_\alpha$$와 이를 포함하는 열린집합 $$U_\alpha$$에 대하여 열린집합 $$V_\alpha$$가 존재하여 $$C_\alpha\subseteq V_\alpha\subseteq\cl(V_\alpha)\subseteq U_\alpha$$이도록 할 수 있다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋보조정리 1](/ko/math/topology/urysohn_and_tietze#lem1)) 그럼 $$C_\alpha\subseteq V_\alpha$$이므로 $$\{V_\beta\mid\beta\leq\alpha\}\cup\{U_\beta\mid\beta>\alpha\}$$이 $$X$$를 덮어 다음 단계의 불변식을 잇는다.

끝으로 이렇게 얻은 $$(V_\alpha)_{\alpha\in J}$$이 $$X$$를 덮음을 본다. 점 $$x$$가 속하는 $$U_\gamma$$는 유한 개뿐이므로 그 지표 가운데 가장 큰 것을 $$\gamma_0$$이라 하면, $$(\ast_{\gamma_0})$$과 $$\gamma_0$$의 최대성에 의해 앞에서와 같이 $$x$$는 어떤 $$V_\beta$$($$\beta\leq\gamma_0$$)로 덮인다. 따라서 $$(V_\alpha)_{\alpha\in J}$$는 $$X$$의 open covering이며 각 $$\alpha$$에 대해 $$\cl(V_\alpha)\subseteq U_\alpha$$를 만족한다.

</details>

Point-finiteness가 초한귀납의 극한 단계와 최종 단계에서 덮개성을 유지하는 데에 결정적으로 쓰였음에 유의한다. 정렬순서만으로는 무한히 많은 $$U_\beta$$를 한꺼번에 $$V_\beta$$로 갈아치울 때 어떤 점이 덮이지 않을 위험이 있으나, 각 점이 유한 개의 조각에만 속한다는 사실이 그 점이 덮이는 단계를 유한한 곳에서 붙들어 준다. 이제 주요 정리를 증명할 준비가 되었다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11**</ins> Paracompact Hausdorff space $$X$$의 임의의 open covering $$(U_\alpha)_{\alpha\in J}$$에 대하여, $$(U_\alpha)$$에 종속된 단위분할이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

증명은 네 단계로 이루어진다. 먼저 덮개를 같은 첨수로 놓인 국소유한 세분으로 바꾸고, 이를 두 번 수축시켜 닫힌 덮개를 얻은 뒤, Urysohn 보조정리로 각 조각의 bump 함수를 만들고, 마지막으로 이들을 정규화한다.

**(1) 정밀 국소유한 세분.** $$X$$가 paracompact이므로 $$(U_\alpha)$$의 locally finite open refinement $$(W_\beta)_{\beta\in K}$$이 존재한다. 세분의 정의에 의해 각 $$\beta$$마다 $$W_\beta\subseteq U_{\alpha(\beta)}$$인 $$\alpha(\beta)\in J$$를 하나 고른다. 이제 각 $$\alpha\in J$$에 대하여

$$V_\alpha=\bigcup\{W_\beta\mid\alpha(\beta)=\alpha\}$$

이라 두자 (해당하는 $$\beta$$가 없으면 $$V_\alpha=\emptyset$$). 그럼 $$V_\alpha$$는 열린집합이고 $$V_\alpha\subseteq U_\alpha$$이며, $$W_\beta$$들이 $$X$$를 덮으므로 $$(V_\alpha)_{\alpha\in J}$$도 $$X$$를 덮는다. 또한 점 $$x$$의 근방이 유한 개의 $$W_\beta$$만을 만나면 유한 개의 $$V_\alpha$$만을 만나므로 ($$V_\alpha$$와 만나는 근방은 $$\alpha(\beta)=\alpha$$인 어떤 $$W_\beta$$와도 만나기 때문이다) $$(V_\alpha)_{\alpha\in J}$$는 locally finite이다. 이로써 $$V_\alpha\subseteq U_\alpha$$를 만족하는 국소유한 open covering을 같은 첨수집합 $$J$$ 위에서 얻었다.

**(2) 두 번의 수축.** $$X$$는 [정리 7](#thm7)에 의하여 normal이고, locally finite인 $$(V_\alpha)$$는 point-finite이다. [보조정리 10](#lem10)을 $$(V_\alpha)$$에 적용하여 open covering $$(P_\alpha)_{\alpha\in J}$$을 얻는데, 모든 $$\alpha$$에 대해 $$\cl(P_\alpha)\subseteq V_\alpha$$이다. $$P_\alpha\subseteq V_\alpha$$이므로 $$(P_\alpha)$$도 point-finite이며, 여기에 [보조정리 10](#lem10)을 다시 적용하여 open covering $$(Q_\alpha)_{\alpha\in J}$$을 얻는다. 모든 $$\alpha$$에 대해 $$\cl(Q_\alpha)\subseteq P_\alpha$$이다. 정리하면 두 덮개 $$(P_\alpha)$$와 $$(Q_\alpha)$$가 모두 $$X$$를 덮으면서

$$\cl(Q_\alpha)\subseteq P_\alpha\subseteq\cl(P_\alpha)\subseteq V_\alpha\subseteq U_\alpha$$

를 만족한다.

**(3) Bump 함수.** 각 $$\alpha$$에 대하여 $$\cl(Q_\alpha)$$와 $$X\setminus P_\alpha$$는 서로소인 두 닫힌집합이다. $$X$$가 normal이므로 Urysohn 보조정리에 의하여 연속함수 $$\psi_\alpha:X\to[0,1]$$이 존재하여 $$\cl(Q_\alpha)$$에서 $$1$$의 값을, $$X\setminus P_\alpha$$에서 $$0$$의 값을 갖는다. ([§Urysohn 보조정리와 Tietze 확장정리, ⁋정리 2](/ko/math/topology/urysohn_and_tietze#thm2)) 그럼 $$\{x\mid\psi_\alpha(x)\neq 0\}\subseteq P_\alpha$$이므로

$$\supp\psi_\alpha=\cl(\{x\mid\psi_\alpha(x)\neq 0\})\subseteq\cl(P_\alpha)\subseteq V_\alpha\subseteq U_\alpha$$

이다. 특히 $$(\supp\psi_\alpha)_{\alpha\in J}$$는 $$\supp\psi_\alpha\subseteq V_\alpha$$이고 $$(V_\alpha)$$가 locally finite이므로 locally finite이다.

**(4) 정규화.** Family $$(\psi_\alpha)$$가 locally finite인 support를 가지므로, 각 점 $$x$$는 유한 개의 $$\psi_\alpha$$만이 $$0$$이 아닌 근방을 가진다. 그 근방 위에서 합 $$\psi=\sum_{\alpha\in J}\psi_\alpha$$은 유한합이고, 연속함수의 유한합은 연속이므로 $$\psi$$는 그 근방에서 연속이다. 연속성은 국소적 성질이므로 $$\psi:X\to\mathbb{R}$$은 연속함수이다. 또한 $$(Q_\alpha)$$가 $$X$$를 덮으므로 임의의 $$x$$는 어떤 $$Q_\alpha$$에 속하고, 그럼 $$x\in\cl(Q_\alpha)$$에서 $$\psi_\alpha(x)=1$$이므로 $$\psi(x)\geq 1>0$$이다. 따라서

$$\phi_\alpha=\frac{\psi_\alpha}{\psi}$$

로 정의하면 각 $$\phi_\alpha:X\to[0,1]$$은 연속함수이다 ($$\psi$$가 어디에서도 $$0$$이 아니기 때문이다). $$\psi>0$$이므로 $$\{x\mid\phi_\alpha(x)\neq 0\}=\{x\mid\psi_\alpha(x)\neq 0\}$$이고, 따라서 $$\supp\phi_\alpha=\supp\psi_\alpha\subseteq U_\alpha$$이며 $$(\supp\phi_\alpha)$$는 locally finite이다. 끝으로 각 $$x$$에서

$$\sum_{\alpha\in J}\phi_\alpha(x)=\frac{1}{\psi(x)}\sum_{\alpha\in J}\psi_\alpha(x)=\frac{\psi(x)}{\psi(x)}=1$$

이다. 그러므로 $$(\phi_\alpha)_{\alpha\in J}$$은 $$(U_\alpha)$$에 종속된 단위분할이다.

</details>

<div class="remark" markdown="1">

<ins id="rmk12">**참고 12**</ins> [정리 11](#thm11)의 역도 성립한다. 임의의 open covering $$(U_i)_{i\in I}$$에 대하여 이에 종속된 단위분할 $$(\phi_i)_{i\in I}$$이 존재하는 공간 $$X$$가 주어졌다 하자. 그럼 열린집합 $$G_i=\{x\mid\phi_i(x)>0\}$$은 $$G_i\subseteq\supp\phi_i\subseteq U_i$$를 만족하여 $$(U_i)$$의 open refinement를 이루고, $$(\supp\phi_i)$$가 locally finite이므로 $$(G_i)$$도 locally finite이며, $$\sum_i\phi_i(x)=1$$로부터 각 $$x$$에서 $$\phi_i(x)>0$$인 $$i$$가 존재하여 $$(G_i)$$가 $$X$$를 덮는다. 따라서 $$X$$는 paracompact이다. Hausdorff 조건을 함께 놓으면 이것이 [§옹골성, ⁋정리 7](/ko/math/topology/compactness#thm7)에서 증명 없이 진술한 동치, 곧 위상공간이 paracompact Hausdorff인 것과 임의의 open covering이 종속 단위분할을 허락하는 것이 동치라는 사실을 이룬다.

</div>

## 국소 구성의 대역화

단위분할이 마련되면 국소적으로 정의된 자료를 대역적 대상으로 묶는 표준적인 절차가 열린다. 이 절에서는 그 원리를 연속함수의 경우로 예시한다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> Paracompact Hausdorff space $$X$$의 open covering $$(U_\alpha)_{\alpha\in J}$$이 주어지고, 각 $$U_\alpha$$ 위에서만 정의된 연속함수 $$f_\alpha:U_\alpha\to\mathbb{R}$$이 주어졌다 하자. [정리 11](#thm11)에 의하여 $$(U_\alpha)$$에 종속된 단위분할 $$(\phi_\alpha)_{\alpha\in J}$$을 택한다. 각 $$\alpha$$에 대하여 곱 $$\phi_\alpha f_\alpha$$은 $$U_\alpha$$ 위에서 연속이며, $$\supp\phi_\alpha\subseteq U_\alpha$$이 $$X$$의 닫힌집합이므로 이 곱을 $$U_\alpha$$ 바깥에서 $$0$$으로 두어 $$X$$ 전체에서 연속인 함수로 연장할 수 있다. 이 연장을 다시 $$\phi_\alpha f_\alpha$$로 적으면, family $$(\supp\phi_\alpha)$$가 locally finite이므로

$$f=\sum_{\alpha\in J}\phi_\alpha f_\alpha$$

은 각 점의 근방에서 유한합으로 환원되어 $$X$$ 전체에서 정의된 연속함수를 이룬다. 여기에서 $$f$$는 국소적 자료 $$(f_\alpha)$$를 단위분할의 무게로 평균 낸 대역적 함수이다. 반대로 $$X$$ 위의 임의의 연속함수 $$g$$가 주어지면 $$g=\sum_\alpha\phi_\alpha g$$이 성립하여, $$g$$가 $$U_\alpha$$ 위의 조각 $$\phi_\alpha g$$들로 분해된다.

</div>

이 구성은 위상다양체를 다룰 때 특히 유용하다. 위상다양체는 언제나 paracompact Hausdorff space이므로, 그 임의의 좌표 덮개에 종속된 단위분할이 존재한다. 이 사실 덕분에 각 좌표조각에서 Euclidean space의 언어로 정의한 대상을 다양체 전체로 이어 붙이는 일이 가능해지며, 이것이 단위분할이 다양체론과 다발 이론에서 필수적인 도구로 쓰이는 이유이다.

---

**참고문헌**

**[Mun]** J. R. Munkres, *Topology*, 2nd ed., Prentice Hall, 2000.

**[Wil]** S. Willard, *General Topology*, Addison-Wesley, 1970.

**[Lee]** J. M. Lee, *Introduction to Topological Manifolds*, 2nd ed., Springer, 2011.
