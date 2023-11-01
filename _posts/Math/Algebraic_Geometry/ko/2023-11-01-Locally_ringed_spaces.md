---

title: "Locally ringed space"
excerpt: "환의 스펙트럼과 locally ringed space"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/locally_ringed_spaces
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Locally_ringed_spaces.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-11-01
last_modified_at: 2023-11-01
weight: 3

---

앞으로 모든 ring은 commutative ring with unity를 의미한다.

대수기하는 가환대수에 기하적인 직관을 부여해서 훨씬 다루기 쉽게 만들어준다. 우선 우리는 affine scheme을 먼저 살펴본다.

## Spectrum of a ring

Ring $A$의 prime ideal들의 집합을 $\Spec A$로 적고, 임의의 ideal $\mathfrak{a}\leq A$에 대하여, $V(\mathfrak{a})$를 $\mathfrak{a}$를 포함하는 prime ideal들의 모임이라 하자. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Zariski

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

이 보조정리에 의해, $\Spec A$ 위에 topology를 줄 수 있다. 이는 간단히 $\Spec A$의 닫힌집합들을 $V(\mathfrak{a})$들이라고 선언하면 되고, 실제로 $V(\mathfrak{a})$들이 닫힌집합이 만족해야 할 성질들을 만족한다는 것이 위의 보조정리이다. 이렇게 정의된 위상을 *Zariski topology<sub>자리스키 위상</sub>*이라 부른다.

한편, 위상공간 $\Spec A$에 적절한 sheaf of rings $\mathscr{O}$를 정의할 수 있다. 우선 각각의 $\mathfrak{p}\in\Spec A$에 대하여, $\mathfrak{p}$에서의 $A$의 localization을 $A\_\mathfrak{p}$으로 적자. 이제 임의의 열린집합 $U\subseteq \Spec A$에 대하여, $\mathscr{O}(U)$의 원소들은 각 점 $\mathfrak{p}$에서의 값이 $A_\mathfrak{p}$에 속하는 함수들 $s:U \rightarrow \coprod\_{\mathfrak{p}\in U}A\_\mathfrak{p}$ 가운데, $s$가 local하게도 $A$의 원소의 quotient로 쓰여지는 함수들의 모임이다. 즉, 임의의 $\mathfrak{p}\in U$가 주어졌을 때마다, $\mathfrak{p}$의 적당한 근방 $V\subseteq U$가 존재하여, 모든 $\mathfrak{q}\in V$마다 $s(\mathfrak{q})=a/f$이도록 하는 $a,f\in A$가 존재해야 한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$에 대하여, $A$의 *spectrum<sub>스펙트럼</sub>*은 $(\Spec A,\mathscr{O})$를 의미한다.

</div>

$(\Spec A,\mathscr{O})$의 성질을 살펴보기 위해 표기를 고정한다. 임의의 $f\in A$에 대하여, $D(f)$를 $V((f))$의 complement로 정의한다. 그럼 $D(0)=\emptyset$이고 $D(1)=\Spec A$이며, 뿐만 아니라 이러한 열린집합 $D(f)$들의 모임은 $\Spec A$의 basis가 된다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> 위에서 정의한 $D(f)$들의 모임은 위상공간 $\Spec A$의 basis가 된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Spec A$의 임의의 열린집합 $U$가 주어졌다 하자. 즉 적당한 $\mathfrak{a}$에 대하여 $U=V(\mathfrak{a})^c$이다. 이제 임의의 $\mathfrak{p}\in U$에 대하여, $\mathfrak{p}\not\supseteq \mathfrak{a}$이므로 적당한 $f\in \mathfrak{a}\setminus \mathfrak{p}$가 존재한다. 이제 $D(f)$가 $\mathfrak{p}$를 포함하며 $U$에 속한다.

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $(\Spec A,\mathscr{O})$에 대하여 다음이 성립한다.

1. 임의의 $\mathfrak{p}\in\Spec A$에 대하여, $\mathscr{O}\_p$는 $A\_\mathfrak{p}$와 isomorphic하다.
2. 임의의 $f\in A$에 대하여, $\mathcal{O}(D(f))$와 $A_f$가 isomorphic하다.
3. 따라서, $f=1$로 두면 $\Gamma(\Spec A,\mathscr{O})\cong A$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

## Locally ringed space

Manifold는 국소적으로 $\mathbb{R}^n$과 닮아있는 위상공간으로 정의된다. 이와 비슷하게, scheme은 국소적으로 어떤 ring의 spectrum $(\Spec A, \mathscr{O})$와 닮아있는 *locally ringed space*로 정의되며, 이러한 chart들을 affine scheme이라 부른다. 따라서 다음을 먼저 정의한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 위상공간 $X$와, 그 위에 정의된 ring들의 sheaf $\mathscr{O}_X$의 pair $(X,\mathscr{O}_X)$를 *ringed space<sub>환 달린 공간</sub>*라 부른다. Ringed space $(X,\mathscr{O}\_X)$에서 $(Y,\mathscr{O}\_Y)$로의 *morphism*은 연속함수 $f:X \rightarrow Y$와, sheaf morphism $f^\sharp:\mathscr{O}\_Y \rightarrow f\_\ast\mathscr{O}\_X$으로 주어진다.

만일 ringed space $(X,\mathscr{O}_X)$의 임의의 stalk $\mathscr{O}\_{X,p}$이 항상 local ring이라면 이를 *locally ringed space<sub>국소적 환 달린 공간</sub>*이라 부른다. Locally ringed space $(X,\mathscr{O}\_X)$에서 $(Y,\mathscr{O}\_Y)$로의 *morphism*은 ringed space 사이의 morphism $(f,f^\sharp)$ 중, $f\_p^\sharp:\mathscr{O}\_{Y,f(p)}\rightarrow \mathscr{O}\_{X,p}$이 항상 local homomorphism인 것들을 말한다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 다음이 성립한다.

1. $(\Spec A, \mathscr{O})$는 항상 locally ringed space이다.
2. Ring homomorphism $\phi:A \rightarrow B$는 locally ringed space 사이의 morphism 
    
    $$(f,f^\sharp):(\Spec B,\mathscr{O}_{\Spec B}) \rightarrow (\Spec A,\mathscr{O}_{\Spec A})$$

    을 유도한다.
3. 반대로, 두 locally ringed space $(\Spec B,\mathscr{O}\_{\Spec B})$에서 $(\Spec A,\mathscr{O}\_{\Spec A})$로의 임의의 morphism은 항상 위와 같은 방식으로 얻어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>