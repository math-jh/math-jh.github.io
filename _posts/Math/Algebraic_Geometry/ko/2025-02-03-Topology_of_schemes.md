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
last_modified_at: 2025-02-03
weight: 5

---

## 일반점

이제 우리는 스킴이 갖는 위상적인 구조를 살펴볼 것이다. [§스펙트럼](/ko/math/algebraic_geometry/spectrums)에서 이미 살펴보았듯, scheme $X$는 일반적으로 우리가 생각하는 위상공간과는 다른 위상이 주어져 있다. 가장 특이한 것 중 하나는 한점집합이 닫힌집합이 아닐 수도 있다는 것이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 위상공간 $X$의 한 점 $x$가 *closed point<sub>닫힌점</sub>*이라는 것은 $\{x\}$가 $X$의 닫힌집합이라는 것이다.

</div>

따라서 공간 $X$가 $T_1$-space인 것과 $X$의 모든 점이 closed point인 것이 동치임을 안다. ([\[위상수학\] §하우스도르프 공간, ⁋정의 3](/ko/math/topology/Hausdorff_spaces#def3)) 특히 우리는 field가 아닌 integral domain의 스펙트럼은 closed point를 갖지 않는다는 것을 보았다. 

한편, 임의의 affine scheme은 반드시 closed point를 갖는다.[^1] 이는 ring $A$의 maximal ideal $\mathfrak{m}$을 하나 택하면 $Z(\mathfrak{m})=\\{\mathfrak{m}\\}$이고, 따라서 [§스펙트럼, ⁋명제 14](/ko/math/algebraic_geometry/spectrums#prop14)과 [\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋명제 7](/ko/math/set_theory/filter_and_ideal#prop7)을 적용하면

$$\cl(\{\mathfrak{m}\})=ZI(\{\mathfrak{m}\})=ZIZ(\mathfrak{m})=Z(\mathfrak{m})=\{\mathfrak{m}\}$$

이기 때문이다. 비슷하게, 만일 임의의 affine scheme $\Spec A$가 closed point $\mathfrak{p}$를 갖는다면, $I(\\{\mathfrak{p}\\})=\mathfrak{p}$와 [§스펙트럼, ⁋명제 14](/ko/math/algebraic_geometry/spectrums#prop14)로부터

$$Z(\mathfrak{p})=ZI(\{\mathfrak{p}\})=\cl(\{\mathfrak{p}\})=\{\mathfrak{p}\}$$

이므로 $\mathfrak{p}$는 반드시 maximal ideal이어야 한다. 

정의에 의하여, $\Spec A$의 점 $\mathfrak{p}$가 closed point가 아니라면 $\mathfrak{q}\in \cl(\{\mathfrak{p}\})$를 만족하는 $\Spec A$의 점 $\mathfrak{q}\neq \mathfrak{p}$가 존재한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 위상공간 $X$의 두 점 $x,y$가 $x\in\cl(\\{y\\})$를 만족한다 하자. 그럼 $x$를 $y$의 *specialization*이라 하고, $y$는 $x$의 *generalization*이라 한다. 만일 위상공간 $X$의 닫힌집합 $A$에 대하여, $A=\cl(\\{x\\})$가 성립한다면 $x$를 $A$의 *generic point<sub>일반점</sub>*라 부른다. 

</div>

예를 들어 우리는 임의의 integral domain $A$에 대하여 $\\{0\\}$이 $A$의 유일한 generic point인 것을 안다. 이 예시를 더욱 기하학적으로 만들기 위해, $A=\mathbb{k}[\x_1,\x_2]/(\x_2-\x_1^2)$이라 하자. 그럼 [§스펙트럼, ⁋명제 9](#prop9)에서 우리는 $\Spec A$가 $\mathbb{A}\_\mathbb{k}^2=\Spec \mathbb{k}[\x_1,\x_2]$의 닫힌집합임을 보였다. 이제 우리는 prime ideal $(\x_2-\x_1^2)\in \Spec \mathbb{k}[\x_1,\x_2]$이 $\Spec A\cong Z(\x_2-\x_1^2)$의 generic point임을 안다. 

## 스킴의 위상적 성질들

Scheme은, structure sheaf를 빼고 보면 그냥 위상공간이므로, 위상공간의 성질들을 가질 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Scheme $(X,\mathscr{O}\_X)$가 주어졌다 하자. 만일 $X$가 위상공간으로서 quasi-compact (resp. noetherian, irreducible, connected)라면, $X$를 quasi-compact (resp. noetherian, irreducible, connected) scheme이라 부른다. 

</div>

위 정의에 해당하는 위상수학의 정의들은 각각 [\[위상수학\] §옹골공간, ⁋정의 1](/ko/math/topology/compact_spaces#def1), [\[위상수학\] §차원, ⁋정의 11](/ko/math/topology/dimension#def11), [\[위상수학\] §차원, ⁋정의 6](/ko/math/topology/dimension#def6)과 [\[위상수학\] §연결공간, ⁋정의 1](/ko/math/topology/connected_spaces#def1)에서 각각 찾아볼 수 있다. 다음은 이 정의에 대한 예시와 반례들이다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 우리는 [§스펙트럼, ⁋보조정리 12](/ko/math/algebraic_geometry/spectrums#lem12)에 의해 임의의 affine scheme은 quasi-compact임을 안다. Quasi-compact가 아닌 scheme의 예시로는, 당연히 무한히 많은 scheme들의 disjoint union이 있다. 

</div>

Irreducibilty의 경우 다음 예시들을 보자. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 임의의 integral domain $A$에 대하여, $\Spec A$는 항상 irreducible이다. Generic point $\\{0\\}$을 생각하면, $\\{0\\}$를 포함하는 닫힌집합은 오직 $\Spec A$ 자신뿐이어야 하므로, $\Spec A$를 두 개의 proper closed subset의 합집합으로 나타내는 것이 불가능하기 때문이다. 따라서 $A=\mathbb{k}[\x_0,\ldots, \x_n]$으로 두면 affine $n$-space $\mathbb{A}\_\mathbb{k}^n$은 irreducible인 것을 안다. 그럼 projective space $\mathbb{P}^n\_\mathbb{k}$는 irreducible open subset들 $D_+(\x_i)$을 가지므로 [\[위상수학\] §차원, ⁋명제 8](/ko/math/topology/dimension#prop8)에 의해 $\mathbb{P}^n\_\mathbb{k}$ 또한 irreducible이다. 

</div>

Irreducible space는 항상 connected이므로, 위의 예시들은 connected space의 예시이기도 하다. 반례의 경우 다음 예시에서 찾아볼 수 있다. 

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 우선 connected가 아닌 scheme의 예시는 $\mathbb{A}^2\_\mathbb{k}$의 (closed) subscheme 

$$\Spec \frac{\mathbb{k}[\x,\y]}{(\x(\x-1))}$$

이 있다. 이것이 connected가 아님을 보기 위해서는 이를 두 개의 (closed) scheme $\Spec \mathbb{k}[\x,\y]/(\x)$와 $\Spec \mathbb{k}[\x,\y]/(\x-1)$의 disjoint union으로 쓸 수 있다는 것을 확인하면 된다. 

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



</details>


[^1]: 그러나 closed point를 갖지 않는 scheme이 존재한다. 