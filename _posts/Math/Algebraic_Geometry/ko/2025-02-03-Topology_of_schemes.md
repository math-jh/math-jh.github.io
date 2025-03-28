---

title: "스킴의 위상구조"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/topology_of_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Topology_of_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-02-03
last_modified_at: 2025-02-23
weight: 5

---

## 일반점

이제 우리는 스킴이 갖는 위상적인 구조를 살펴볼 것이다. [§스펙트럼](/ko/math/algebraic_geometry/spectrums)에서 이미 살펴보았듯, scheme $X$는 일반적으로 우리가 생각하는 위상공간과는 다른 위상이 주어져 있다. 가장 특이한 것 중 하나는 한점집합이 닫힌집합이 아닐 수도 있다는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$의 한 점 $x$가 *closed point<sub>닫힌점</sub>*이라는 것은 $\\{x\\}$가 $X$의 닫힌집합이라는 것이다.

</div>

따라서 공간 $X$가 $T_1$-space인 것과 $X$의 모든 점이 closed point인 것이 동치임을 안다. ([\[위상수학\] §하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)) 특히 우리는 field가 아닌 integral domain의 스펙트럼은 closed point를 갖지 않는다는 것을 보았다. 

한편, 임의의 affine scheme은 반드시 closed point를 갖는다.[^1] 이는 ring $A$의 maximal ideal $\mathfrak{m}$을 하나 택하면 $Z(\mathfrak{m})=\\{\mathfrak{m}\\}$이고, 따라서 [§스펙트럼, ⁋명제 14](/ko/math/algebraic_geometry/spectrums#prop14)과 [\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋명제 7](/ko/math/set_theory/filter_and_ideal#prop7)을 적용하면

$$\cl(\{\mathfrak{m}\})=ZI(\{\mathfrak{m}\})=ZIZ(\mathfrak{m})=Z(\mathfrak{m})=\{\mathfrak{m}\}$$

이기 때문이다. 비슷하게, 만일 임의의 affine scheme $\Spec A$가 closed point $\mathfrak{p}$를 갖는다면, $I(\\{\mathfrak{p}\\})=\mathfrak{p}$와 [§스펙트럼, ⁋명제 14](/ko/math/algebraic_geometry/spectrums#prop14)로부터

$$Z(\mathfrak{p})=ZI(\{\mathfrak{p}\})=\cl(\{\mathfrak{p}\})=\{\mathfrak{p}\}$$

이므로 $\mathfrak{p}$는 반드시 maximal ideal이어야 한다. 

정의에 의하여, $\Spec A$의 점 $\mathfrak{p}$가 closed point가 아니라면 $\mathfrak{q}\in \cl(\{\mathfrak{p}\})$를 만족하는 $\Spec A$의 점 $\mathfrak{q}\neq \mathfrak{p}$가 존재한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위상공간 $X$의 두 점 $x,y$가 $x\in\cl(\\{y\\})$를 만족한다 하자. 그럼 $x$를 $y$의 *specialization*이라 하고, $y$는 $x$의 *generalization*이라 한다. 만일 위상공간 $X$의 닫힌집합 $C$에 대하여, $C=\cl(\\{x\\})$가 성립한다면 $x$를 $C$의 *generic point<sub>일반점</sub>*라 부른다. 

</div>

그럼 정의에 의하여, $x$가 $C$의 generic point라면 $A$의 임의의 열린집합 $U$는 항상 $x$를 포함한다. 따라서 generic point는 $C$의 모든 점에 가까운 점으로 생각할 수 있다.

특별히 $X$가 affine scheme $\Spec A$인 경우, 우리는 $\Spec A$의 임의의 irreducible closed set은 $A$의 적당한 prime ideal $\mathfrak{p}$에 대하여 $Z(\mathfrak{p})$의 꼴로 나타난다는 것을 확인하였다. 그럼 자명하게 $\mathfrak{p}\in Z(\mathfrak{p})$이고, 이 때 $Z(\mathfrak{p})$에 속하는 prime ideal들 중 $\mathfrak{p}$가 (유일하게) minimal한 것은 자명하므로 $Z(\mathfrak{p})$의 (유일한) generic point가 된다.

이를 더욱 기하학적으로 만들기 위해, $A=\mathbb{k}[\x_1,\x_2]/(\x_2-\x_1^2)$이라 하자. 그럼 [§스펙트럼, ⁋명제 9](#prop9)에서 우리는 $\Spec A$가 $\mathbb{A}\_\mathbb{k}^2=\Spec \mathbb{k}[\x_1,\x_2]$의 닫힌집합임을 보였다. 이제 우리는 prime ideal $(\x_2-\x_1^2)\in \Spec \mathbb{k}[\x_1,\x_2]$이 $\Spec A\cong Z(\x_2-\x_1^2)$의 generic point임을 안다. 즉 generic point는 곡선 $\x_2-\x_1^2$ 그 자체를 나타내는 것으로 해석할 수 있다. 

## 스킴의 위상적 성질들

Scheme은, structure sheaf를 빼고 보면 그냥 위상공간이므로, 위상공간의 성질들을 가질 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme $(X,\mathscr{O}\_X)$가 주어졌다 하자. 만일 $X$가 위상공간으로서 quasi-compact (resp. irreducible, connected)라면, $X$를 quasi-compact (resp. irreducible, connected) scheme이라 부른다. 

</div>

위 정의에 해당하는 위상수학의 정의들은 각각 [\[위상수학\] §옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1), [\[위상수학\] §차원, ⁋정의 6](/ko/math/topology/dimension#def6)과 [\[위상수학\] §연결공간, ⁋정의 1](/ko/math/topology/connected_spaces#def1)에서 각각 찾아볼 수 있다.[^2] 다음은 이 정의에 대한 예시와 반례들이다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 우리는 [§스펙트럼, ⁋보조정리 12](/ko/math/algebraic_geometry/spectrums#lem12)에 의해 임의의 affine scheme은 quasi-compact임을 안다. Quasi-compact가 아닌 scheme의 예시로는, 당연히 무한히 많은 scheme들의 disjoint union이 있다. 

</div>

Irreducibilty의 경우 다음 예시들을 보자. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 임의의 integral domain $A$에 대하여, $\Spec A$는 항상 irreducible이다. Generic point $\\{0\\}$을 생각하면, $\\{0\\}$를 포함하는 닫힌집합은 오직 $\Spec A$ 자신뿐이어야 하므로, $\Spec A$를 두 개의 proper closed subset의 합집합으로 나타내는 것이 불가능하기 때문이다. 따라서 $A=\mathbb{k}[\x_0,\ldots, \x_n]$으로 두면 affine $n$-space $\mathbb{A}\_\mathbb{k}^n$은 irreducible인 것을 안다. 그럼 projective space $\mathbb{P}^n\_\mathbb{k}$는 irreducible open subset들 $D_+(\x_i)$을 가지므로 [\[위상수학\] §차원, ⁋명제 8](/ko/math/topology/dimension#prop8)에 의해 $\mathbb{P}^n\_\mathbb{k}$ 또한 irreducible이다. 

거꾸로 scheme $X$의 임의의 irreducible closed set $Z$는 항상 generic point $I(Z)$를 갖는다. ([§스펙트럼, ⁋명제 16](/ko/math/algebraic_geometry/spectrums#prop16)) 

</div>

Irreducible space는 항상 connected이므로, 위의 예시들은 connected space의 예시이기도 하다. 다음 예시는 connected가 아닌 scheme과, connected이지만 irreducible이 아닌 scheme들의 예시를 위한 것으로, affine plane $\mathbb{A}^2\_\mathbb{k}$의 특정한 *closed subscheme*들이 주어져 있다. 

우리는 아직 closed subscheme을 정의하지 않았으나, 적어도 [§스펙트럼, ⁋명제 9](/ko/math/algebraic_geometry/spectrums#prop9)에서 우리는 affine scheme $\Spec A$와 $A$의 임의의 ideal $\mathfrak{a}$에 대하여 canonical morphism $A \rightarrow A/\mathfrak{a}$을 통해 $\Spec A/\mathfrak{a}$와 $Z(\mathfrak{a})\subseteq \Spec A$가 위상공간으로서 homeomorphic한 것은 이미 살펴보았다. Connectedness와 irreducibility는 모두 위상공간의 성질이므로, $\Spec A/\mathfrak{a}$의 위상적인 성질은 $\Spec A$의 닫힌집합 $Z(\mathfrak{a})$의 위상구조를 살펴보아 확인할 수 있다. 이들을 closed subscheme이라 부를 때, 부족한 것은 오직 $\Spec A/\mathfrak{a}$의 structure sheaf와 $\Spec A$의 structure sheaf(를 $Z(\mathfrak{a})$로 제한한 것)이 어떤 관계에 있는지 뿐이며, 이는 [§닫힌 부분스킴](/ko/math/algebraic_geometry/closed_subschemes)에서 다시 살펴보게 된다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 우선 connected가 아닌 scheme의 예시는 $\mathbb{A}^2\_\mathbb{k}$의 closed subscheme 

$$\Spec \frac{\mathbb{k}[\x,\y]}{(\x(\x-1))}$$

이 있다. 이것이 connected가 아님을 보기 위해서는 이를 두 개의 subscheme $\Spec \mathbb{k}[\x,\y]/(\x)$와 $\Spec \mathbb{k}[\x,\y]/(\x-1)$의 disjoint union으로 쓸 수 있다는 것을 확인하면 된다. 

한편 connected이지만 irreducible하지 않은 scheme의 예시로는 

$$Z(\x\y)=\Spec \frac{\mathbb{k}[\x,\y]}{(\x\y)}$$

이 있으며, 이 scheme의 irreducible component는 $\Spec\mathbb{k}[\x,\y]/(\x)$와 $\Spec \mathbb{k}[\x,\y]/(\y)$이다. 

![counterexamples](/assets/images/Math/Algebraic_Geometry/Properties_of_schemes-1.png){:style="width:20em" class="invert" .align-center}

</div>

한편, noetherian scheme의 예시는 다음 명제에 의해 얻어진다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Noetherian ring $A$에 대하여, $\Spec A$는 항상 noetherian topological space이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Spec A$의 닫힌집합들의 chain

$$Z(\mathfrak{a}_1)\supseteq Z(\mathfrak{a}_2)\supseteq\cdots$$

이 주어졌다 하면, $A$의 ideal들의 chain

$$IZ(\mathfrak{a}_1)\subseteq IZ(\mathfrak{a}_2)\supseteq\cdots$$

을 얻고 이것은

$$\sqrt{\mathfrak{a}_1}\subseteq \sqrt{\mathfrak{a}_2}\subseteq\cdots$$

와 같다. 이제 $A$가 noetherian ring이라는 가정으로부터 적당한 $k$가 존재하어

$$\sqrt{\mathfrak{a}_k}=\sqrt{\mathfrak{a}_{k+1}}=\cdots$$

이 성립하고 따라서

$$Z(\sqrt{\mathfrak{a}_k})=Z(\sqrt{\mathfrak{a}_{k+1}})=\cdots$$

이다. 이제 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)로부터 원하는 결과를 얻는다.

</details>

그러나 일반적으로 그 역은 성립하지 않는다. 

## 국소성

다음 글에서 우리는 scheme의 대수적인 성질들을 살펴볼 것이다. 이번 글에서 살펴본 위상적인 성질들과 다음 글에서 살펴볼 대수적인 성질들은 물론, 긴밀한 관계가 있으며 이를 동시에 살펴보는 것이 스킴에 대한 우리의 이해를 더 깊게 해 준다. 이를 더 잘 살펴볼 수 있는 정의들을 내리고 이번 글을 마친다. 특히 남은 부분에서 우리는 ring $A$의 localization $A_f$와 $A_\mathfrak{p}$에 기하적인 직관을 부여할 수 있다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Ring의 성질 $Q$가 *local*이라는 것은 다음의 두 조건이 성립하는 것이다.

1. 임의의 ring $A$와 $f\in A$에 대하여, 만일 $A$가 $Q$를 만족한다면 $A_f$도 $Q$를 만족한다.
2. 임의의 ring $A$와, $f_1,\ldots, f_n\in A$가 $A=(f_1,\ldots, f_n)$을 만족한다 하자. 그럼 만일 모든 $A\_{f_i}$가 $Q$를 만족한다면 $A$도 $Q$를 만족한다. 

</div>

이를 affine scheme의 언어로 이를 바꾸어보자. 만일 ring $A$가 local property $Q$를 만족한다면, 

$$D(f)\cong \Spec A_f$$

이므로 $\Spec A$의 principal open set $D(f)$의 global section $\mathscr{O}\_{\Spec A}(D(f))$ 또한 $P$를 만족한다. 거꾸로, 만일 $A$가 $f_1,\ldots, f_r$로부터 생성된다면 다음의 식

$$A=A\setminus \emptyset=A\setminus Z(1)=A\setminus Z\left(\sum_{i=1}^r Z(f_i)\right)=A\setminus\bigcap_{i=1}^r Z(f_i)=\bigcup_{i=1}^rA\setminus Z(f_i)=\bigcup_{i=1}^r D(f_i)$$

으로부터 $D(f_i)$들이 $\Spec A$를 덮는 것을 알 수 있다. 편의상 affine scheme $X$의 global section들의 ring $\mathscr{O}_X(X)$가 성질 $Q$를 갖는다면, $X$가 성질 $P$를 갖는다고 하자. 그럼  이상에서 [정의 8](#def8)의 두 조건은 다음과 같이 번역할 수 있다. 

1. $\Spec A$가 $P$를 만족한다면, 임의의 principal open set $D(f)$ 또한 $P$를 만족한다.
2. $\Spec A$를 덮는 open covering $D(f_1),\ldots, D(f_r)$가 각각 $P$를 만족한다면, $\Spec A$도 $P$를 만족한다. 

한편 $\Spec A$의 일반적인 open set $U$는 principal open set들의 합집합으로 나타낼 수 있고 ([§스펙트럼, ⁋보조정리 11](/ko/math/algebraic_geometry/spectrums#lem11)) 따라서 만일 $\Spec A$가 $P$를 만족한다면 $\Spec A$의 임의의 *affine* open subset $U$가 $P$를 만족하는 것을 안다. 이러한 측면에서, 위의 두 조건을 만족하는 scheme의 성질 $P$를 *affine-local property*라 부르기도 한다. 

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Scheme $X$의 적당한 affine subscheme들에 대해 정의된 성질 $P$가 *affine-local property*라는 것은 다음 두 조건이 성립하는 것이다. 

1. 만일 $\Spec A\subseteq X$가 $P$를 만족한다면, 임의의 $f\in A$에 대해 $\Spec A_f\subseteq X$ 또한 $P$를 만족한다.
2. 만일 $A=(f_1,\ldots, f_r)$이고 $\Spec A\_{f\_i}\subseteq X$가 모두 $P$를 만족한다면 $\Spec A \subseteq X$ 또한 $P$를 만족한다. 

</div>

반면 우리는 [§스킴, ⁋예시 8](/ko/math/algebraic_geometry/schemes#ex8)에서 affine scheme의 open subscheme이 affine이 되지 않을 수 있다는 것을 이미 살펴보았으므로 $P$가 ring의 local property라고 하여도 이러한 식으로 정의한 성질 $P$는 진정한 의미에서 local한 성질이 아니다. 이를 위해서는 다음과 같이 정의하면 된다. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Scheme의 affine-local property $P$에 대하여, scheme $(X, \mathscr{O}\_X)$가 *locally $P$*라는 것은 임의의 $x\in X$마다 적절한 open affine neighborhood $U$가 존재하여 $X$의 affine open subscheme $U$가 $P$를 만족하는 것이다. 

</div>

그럼 [보조정리 12](#lem12)에서 우리는 scheme $X$가 locally $P$라면, $X$의 임의의 open subscheme이 locally $P$라는 것을 보인다. 우선 다음 보조정리를 보이자.

<div class="proposition" markdown="1">

<ins id="lem11">**보조정리 11 (Nike)**</ins> Scheme $X$와 임의의 affine open subset $U,V$가 주어졌다 하자. 그럼 임의의 $x\in U\cap V$에 대하여, 적당한 $x\in W\subseteq U\cap V$가 존재하여 $W$가 $U$와 $V$ 모두에서 principal open subset이도록 할 수 있다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

표기를 위해 $U=\Spec A$, $V=\Spec B$라 하고, $x$가 이들 각각에서 prime ideal들 $\mathfrak{p}\subset A$, $\mathfrak{q}\subset B$에 대응된다 하자. 그럼 우선 $U\cap V$를 $U$의 열린집합으로 보아 [§스펙트럼, ⁋보조정리 11](/ko/math/algebraic_geometry/spectrums#lem11)를 적용하면 $U$의 principal open set $D(f)$를 택하여

$$\mathfrak{p}\in D(f)\subseteq U\cap V$$

이도록 할 수 있다. 이 때, $D(f)\cong \Spec A_f$이므로 inclusion $D(f)\hookrightarrow V$는 ring homomorphism $i:B \rightarrow A_f$로부터 얻어진다. 

한편, 이제 $D(f)\cong\Spec A_f$를 $V$의 열린집합으로 보면 다시 $V$의 principal open set $D(g)$가 존재하여

$$\mathfrak{q}\in D(g)\subseteq D(f)\cap V$$

이도록 할 수 있다. 이제 $\Spec B$의 open subscheme $D(g)$와, $\Spec A$의 open subscheme $D(i(g))$이 서로 같다는 것을 확인하면 된다. 

</details>

<div class="proposition" markdown="1">

<ins id="lem12">**보조정리 12**</ins> Scheme $X$와 scheme의 affine-local property $P$에 대하여 다음이 모두 동치이다.

1. $X$가 locally $P$이다.
2. $X$의 임의의 affine open subset $U\subseteq X$에 대하여, $X$의 open subscheme $U$가 $P$를 만족한다.
3. $X$의 적당한 affine open covering $\\{U\_i\\}$가 존재하여 $X$의 open subscheme $U_i$가 모두 $P$를 만족한다.
4. $X$의 적당한 open covering $\\{U_i\\}$가 존재하여, 각각의 open subscheme $(U\_i, \mathscr{O}\_X\vert\_{U_i})$가 locally $P$이다.

특히, 만일 $X$가 locally $P$라면 $X$의 임의의 open subscheme이 locally $P$이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫째 조건이 성립한다면 각각의 $x$마다 open affine neighborhood $U_x$가 존재한다. 따라서 $\\{U_x\\}_{x\in X}$가 셋째 조건에서 요구하는 $X$의 affine open covering이 된다. 거꾸로 셋째 조건에 의해 주어지는 affine open covering $\\{U_i\\}$가 주어진다면, $X$의 임의의 점 $x$가 주어질 때마다 $x\in U_i$를 만족하는 $U_i$를 택할 수 있고, 이렇게 얻어지는 $U_i$가 [정의 9](#def9)에서 요구하는 $x$의 open affine neighoborhood가 된다. 따라서 첫째 조건과 셋째 조건은 동치이다. 또, 둘째 조건이 첫째 조건을 함의하는 것은 자명하다. 

이제 셋째 조건이 성립한다 가정하고 둘째 조건이 성립함을 보인다. 셋째 조건을 만족하는 $X$의 affine open covering $\\{U\_i=\Spec A\_i\\}$가 주어졌다 하자. 그럼 $X$의 임의의 affine open subset $V=\Spec A$에 대하여, 각각의 $V\cap U_i$들은 $V$의 열린집합이기도 하므로 [보조정리 11](#lem11)로부터 

$$V=\bigcup_{i\in I} V\cap U_i=\bigcup_{i\in I} \bigcup_{j\in J_i} \Spec (A_i)_{f_j}$$

를 만족하는 $f_j\in A_j$들을 찾을 수 있고, $\Spec (A\_i)\_{f\_j}$들 각각은 $\Spec A$의 적당한 localization $\Spec A\_{g\_j}$들로 둘 수 있다는 것을 알고 [§스펙트럼, ⁋보조정리 12](/ko/math/algebraic_geometry/spectrums#lem12)를 사용하면 $g_j$들이 유한하게 주어졌다 가정할 수 있다. 이제 [정의 9](#def9) 이전의 논의로부터 $P$가 local이라는 가정으로부터 각각의 $\Spec (A\_i)\_{f\_j}=\Spec A\_{g\_j}$가 $P$를 만족하는 것을 알고, 이로부터 $\Spec A$가 $P$를 만족하는 것을 안다.

이상에서 첫째 조건부터 셋째 조건이 모두 동치임을 안다. 

이제 $X$가 locally $P$라 하고, $U$가 $X$의 임의의 open subscheme이라 하자. 그럼 임의의 $x\in U$에 대하여, [§스펙트럼, ⁋보조정리 11](/ko/math/algebraic_geometry/spectrums#lem11)로부터 $x\in D(f)\subseteq U$를 만족하는 $X$의 affine open subset $D(f)$를 잡을 수 있고 이제 둘째 조건으로부터 $D(f)$가 $P$를 만족하는 affine scheme인 것을 안다. 따라서 scheme $U$ 또한 locally $P$가 되어 마지막 주장을 얻는다. 마지막으로 넷째 조건과 나머지 조건이 동치인 것은 이 주장을 사용하여 둘째 조건과 셋째 조건에서 affine이라는 가정만 빼면 얻어진다. 

</details>

한편 우리는 [명제 7](#prop7)에서 noetherian ring $A$에 대하여 $\Spec A$가 noetherian space임을 보았다. 이제 임의의 scheme $X$에 대하여 $X$가 noetherian인 것이 무엇인지를 정의하자.

<div class="proposition" markdown="1">

<ins id="lem13">**보조정리 13**</ins> Ring $A$가 noetherian인 것은 local property이고, 따라서 affine-local property $P$를 정의한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정의 8](#def8)의 두 조건을 증명해야 한다. 

첫째 조건은 [\[가환대수학\] §국소화, ⁋따름정리 9](/ko/math/commutative_algebra/localization#cor9)로부터 얻어지며, 혹은 [\[위상수학\] §차원, ⁋명제 12](/ko/math/topology/dimension#prop13)의 첫쨰 결과를 사용해도 충분하다.

둘쨰 조건을 보자. 만일 $A=(f_1,\ldots, f_r)$이라 하면, 우리는 $D(f_i)$들이 $\Spec A$의 open covering이라는 것을 알고, 따라서 $\mathscr{O}\_{\Spec A}$가 [\[위상수학\] §층, ⁋정의 1](/ko/math/topology/sheaves#def1)의 첫째 조건을 만족하는 것으로부터 다음의 inclusion

$$A \cong \mathscr{O}_{\Spec A}(\Spec A) \hookrightarrow \prod_{i=1}^r \mathscr{O}_{\Spec A}(D(f_i))\cong\prod_{i=1}^r A_{f_i}$$

을 얻는다. 이제 만일 $A\_{f\_i}$들이 모두 noetherian이라면, 그들의 (유한한) 곱 $\prod A\_{f\_i}$ 또한 noetherian이고 따라서 $A$는 noetherian ring의 subring이므로 [\[가환대수학\] §기본 개념들, ⁋정리 3](/ko/math/commutative_algebra/basic_notions#thme)에 의하여 noetherian이다.

</details>

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Scheme $X$가 *locally noetherian scheme<sub>국소뇌터스킴</sub>*인 것은 $A\_i$가 모두 noetherian인 $X$의 affine open covering $\\{U\_i=\Spec A\_i\\}$가 존재하는 것이다. 만일 $X$가 quasi-compact locally noetherian scheme이라면 이를 *noetherian scheme<sub>뇌터스킴</sub>*이라 부른다. 

</div>

그럼 만일 $A$가 noetherian이라면 $\Spec A$가 noetherian scheme인 것은 정의와 [§스펙트럼, ⁋보조정리 12](/ko/math/algebraic_geometry/spectrums#lem12)로부터 자명하다. 또, [명제 7](#prop7)과 마차나지로 임의의 noetherian scheme은 위상공간으로서 noetherian이다. 그러나 [명제 7](#prop7) 이후에 지적했듯, scheme $X$가 위상공간으로서 noetherian이라 해서 위의 조건이 성립하는 것은 아니라는 것에 주의해야 한다.

마지막으로 우리는 [정의 9](#def9)와는 조금 다른 국소성의 개념을 정의하는데, *stalk-local*의 개념이 그것이다. 

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> Scheme $X$의 성질 $P$가 *stalk-local*이라는 것은 각각의 $x\in X$에 대하여 ring $\mathscr{O}\_{X,x}$가 ring의 성질 $Q$를 만족하는 것이다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop16">**명제 16**</ins> Scheme $X$의 stalk-local property $P$에 대하여, 다음이 모두 동치이다.

1. $X$가 $P$를 만족한다.
2. $X$의 임의의 open subscheme이 $P$를 만족한다.
3. $X$의 임의의 affine open subscheme이 $P$를 만족한다. 
4. $X$의 affine open cover $\\{U\_i\\}$를 택하여 각각의 open subscheme들 $U_i$가 $P$를 만족하도록 할 수 있다. 
5. $X$의 open cover $\\{U\_i\\}$를 택하여 각각의 open subscheme들 $U_i$가 $P$를 만족하도록 할 수 있다.  

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $2\implies 3\implies 4\implies 5$임은 자명하므로, $5\implies 1$ 그리고 $1\implies 2$만 보이면 충분하며, 이들은 다음의 isomorphism

$$\mathscr{O}_{X,x}= \varinjlim_{V\ni x} \mathscr{O}_X(U)\cong \varinjlim_{U\supseteq V\ni x}\mathscr{O}(V)=\mathscr{O}_{U, x}$$

으로부터 자명하다. 

</details>

특히 임의의 stalk-local property는 affine-local property이기도 하다. 그러나 이는 다소 주의할 필요가 있는 명제인데, 이는 가령 $X$ 위의 stalk-local property가

$$\text{$X$ is $P$}\iff \text{$\mathscr{O}_{X,x}$ satisfies $Q$}$$

로 주어졌을 때, 임의의 affine open subset $U$에 대하여 $\mathscr{O}\_X(U)$가 $Q$를 만족한다는 것이 <em_ko>아니라</em_ko>, 임의의 affine open subset $U$와 원소 $x\in U$에 대하여 $\mathscr{O}\_{U,x}$가 성질 $Q$를 만족하고 따라서 affine open subscheme $U$가 성질 $P$를 만족한다는 것이다. 

가령 다음의 affine scheme

$$X=\Spec A=\Spec\left(\prod_{i=1}^\infty \mathbb{Z}/2\mathbb{Z}\right)$$

을 생각하면 $A$의 임의의 원소 $x$는 $x^2=x$를 만족하고, 따라서 임의의 localization $A\_\mathfrak{p}$의 원소도 그러하다. 이제 $A\_{\mathfrak{p}}$에서 성립하는 $x(1-x)=0$으로부터 우리는 $x\in \mathfrak{p}A\_\mathfrak{p}$이거나 $1-x\in \mathfrak{p}A\_\mathfrak{p}$임을 알고, $\mathfrak{p}A\_\mathfrak{p}$에 속하지 않는 원소는 unit임을 안다. ([\[가환대수학\] §국소화, ⁋명제 2](/ko/math/commutative_algebra/localization#prop2)) 따라서 $x=0$ 혹은 $x=1$이므로 $A\_\mathfrak{p}$의 ideal의 chain은 $(0)\subseteq (1)=A\_\mathfrak{p}$ 뿐이다. 이로부터 $A\_\mathfrak{p}$ 각각은 noetherian이지만, 

$$A\times \{0\}\times\{0\}\times\cdots\subseteq A\times A\times\{0\}\subseteq\cdots$$

을 생각하면 $A$는 noetherian이 아니라는 것을 알 수 있다. 

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

---

[^1]: 그러나 closed point를 갖지 않는 scheme이 존재한다. 
[^2]: 우리는 [§스펙트럼, ⁋보조정리 11](/ko/math/algebraic_geometry/spectrums#lem11) 이후에 (Hausdorff가 아닐 수 있는) compact한 위상공간을 *quasi-compact*라 부르기로 하였다. 