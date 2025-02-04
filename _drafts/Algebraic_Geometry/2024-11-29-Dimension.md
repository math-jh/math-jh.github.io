---

title: "차원"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/dimension
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-29
last_modified_at: 2024-11-29
weight: 13

---

## 기본 정의들

스킴은 위상공간이므로, 위상공간으로서의 Krull dimension이 정의된다. ([\[위상수학\] §차원, ⁋정의 10](/ko/math/topology/dimension#def10)) 그럼 $\Spec A$의 irreducible closed subset과 $A$의 prime ideal 사이의 일대일 대응이 있으므로, 다음 명제는 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> 임의의 ring $A$에 대하여, $\Spec A$의 위상공간으로서의 차원과 $A$의 ring으로서의 차원이 서로 같다.

</div>

위상수학에서와 마찬가지로, 공간이 irreducible이 아닌 경우는 다소 주의를 기울일 필요가 있다. 때문에 대부분의 명제는 전체공간이 irreducible인 것으로 생각하는 것이 더 좋다.

한편 [\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13)와 마찬가지 이유로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 scheme $X$에 대하여, $\dim X=n$인 것은 $X$의 affine open covering $(U_i)$가 존재하여, 모든 $U_i$에 대하여 $\dim U_i\leq n$이고, 적어도 하나의 $i$에 대해서는 등호가 성립하는 것과 동치이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Integral morphism $f:X \rightarrow Y$의 fiber는 항상 $0$차원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

즉, 임의의 field $\mathbb{k}$에 대하여 $\phi: \mathbb{k} \rightarrow A$가 integral extension이라면 $\dim A=0$임을 보여야 한다. 이는 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 3](/ko/math/commutative_algebra/lying_over_and_going_up#cor3) 그리고 [\[가환대수학\] §정수적 확장과 아이디얼, ⁋따름정리 4](/ko/math/commutative_algebra/lying_over_and_going_up#cor4)에 의해 자명하다. 

</details>

더 일반적으로 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Integral extension $\phi:A \rightarrow B$에 대하여, $\dim\Spec A=\dim \Spec B$가 성립한다. 

</div>

특히 normalization은 차원을 변화시키지 않는다. 

한편 위상공간 $X$와 irreducible subset $Y$에 대하여, $Y$의 codimension 또한 정의할 수 있다. 이제 [명제 1](#prop1)과 마찬가지 이유로 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 임의의 ring $A$와 prime ideal $\mathfrak{p}$에 대하여, $A$에서의 $\mathfrak{p}$의 height와 $\Spec A$에서 $\mathfrak{p}$의 codimension이 서로 같다.

</div>

임의의 scheme $X$와, $X$의 임의의 irreducible closed subset에 대하여 

$$\codim_XY+\dim Y\leq \dim X$$

가 성립한다는 것은 정의로부터 자명하다. 

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6**</ins> $A$가 finitely generated $\mathbb{k}$-algebra이며, 동시에 integral domain이라 하자. 그럼 $\dim \Spec A=\trdeg \Frac(A)/\mathbb{k}$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

