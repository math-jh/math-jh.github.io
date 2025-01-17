---

title: "차원"
excerpt: ""

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/Krull_dimension
header:
    overlay_image: /assets/images/Math/Commutative_Algebra/Krull_dimension.png
    overlay_filter: 0.5
sidebar: 
    nav: "commutative_algebra-ko"

date: 2025-01-16
last_modified_at: 2025-01-16
weight: 16

---

## 차원의 정의

앞으로의 몇 개의 글에서 우리는 ring의 차원을 정의하고, 그 성질들을 살펴본다. 차원의 정의 자체는 어렵지 않다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring $A$의 *Krull dimension<sub>크룰 차원</sub>*은 $A$의 prime ideal들의 descending chain

$$\mathfrak{p}_r\supseteq \mathfrak{p}_{r-1}\supseteq\cdots\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_0$$

의 length $r$들의 supremum으로 정의하고, 이를 $\dim A$로 적는다. 

</div>

간단히 ring $A$의 Krull dimension을 $A$의 dimension이라 부른다. 예를 들어, field $\mathbb{k}$는 유일한 prime ideal $(0)$을 가지므로 $\mathbb{k}$는 항상 $0$차원이다. 

더 일반적으로 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Ring $A$의 ideal $\mathfrak{a}$에 대하여, $\mathfrak{a}$의 dimension은

$$\dim \mathfrak{a}=\dim A/\mathfrak{a}$$

으로 정의한다. 

$A$의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{p}$의 *codimension<sub>여차원</sub>* $\codim \mathfrak{p}$는 $A_\mathfrak{p}$의 차원으로 정의하며, 일반적인 ideal $\mathfrak{a}$의 경우 $\codim \mathfrak{a}$는 $\mathfrak{a}$를 포함하는 prime ideal들의 codimension들의 minimum으로 정의한다. 

마지막으로, 임의의 $A$-module $M$에 대하여 $M$의 dimension과 codimension을 $\ann(M)$의 dimension과 codimension으로 각각 정의한다.

</div>

다소 주의할 사항으로, 위의 정의를 따르면 $\mathfrak{a}$는 먼저 정의한 ideal로서의 dimension과, 이를 $A$-module로 봤을 때의 dimension의 두 가지 정의를 갖게 되는데, 이 두 정의가 주는 값이 다를 수 있다. 따라서 $\dim \mathfrak{a}$라는 표기법을 사용할 때에는 [정의 2](#def2)에서 먼저 정의한 것과 같이 $A$의 ideal로서의 dimension만 의미하기로 한다.

그럼 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)에 의하여 $\codim \mathfrak{p}$는 prime ideal $\mathfrak{p}$로부터 시작하는 decreasing chain

$$\mathfrak{p}=\mathfrak{p}_r\supseteq \mathfrak{p}_{r-1}\supseteq\cdots\supseteq \mathfrak{p}_1\supseteq \mathfrak{p}_0$$

의 길이의 supremum과 같다. 한편 그 이름과 같이, 다음의 식

$$\dim \mathfrak{a}+\dim \codim \mathfrak{a}=\dim A$$

을 기대하는 것이 자연스러울 것이지만, 이는 일반적으로 성립하지 않는다.

## $0$차원의 환들

한편 우리는 [§조르단-횔더 정리, ⁋정리 4](/ko/math/commutative_algebra/Jordan-Holder_theorem#thm4)의 첫째 조건과 셋째 조건 사이의 동치를 통해 다음을 안다.

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> Noetherian ring $A$에 대하여, $\dim A =0$인 것과 $A$가 artinian인 것이 동치이다. 

</div>

한편, 우리는 다음 명제에 의하여, 일반적으로 $\phi:A \rightarrow B$가 integral이면 dimension이 변하지 않는다는 것을 안다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $\phi: A \rightarrow B$가 integral이라 하자. 그럼 $\ker\phi$를 포함하는 $A$의 임의의 prime ideal $\mathfrak{p}$에 대하여, $\mathfrak{p}=\phi^{-1} \mathfrak{q}$이도록 하는 $B$의 prime ideal $\mathfrak{q}$이 존재한다. 뿐만 아니라, $B$의 임의의 ideal $\mathfrak{b}$에 대하여 $\dim \mathfrak{b}=\dim \phi^{-1} \mathfrak{b}$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

첫 번째 결과는 단순히 [%%ref%%](going_up)이다. 두 번째 결과의 경우, $\dim \mathfrak{b}\geq \dim \phi^{-1}\mathfrak{b}$는 [%%ref%%](going_up)에 의해 성립하고, 반대방향 부등식은 [%%ref%%](incompacability)에 의해 성립한다. 

</details>

## 1차원의 환들