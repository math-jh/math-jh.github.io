---

title: "스킴의 성질들"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/properties_of_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Properties_of_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-11-04
last_modified_at: 2023-11-04
weight: 6

---

이제 우리는 scheme이 갖는 여러가지 성질들을 정의한다. 여기에서는 [§대수다양체](/ko/math/algebraic_geometry/algebraic_varieties)에서와 같이 $\mathbb{A}^2$에서의 그림이 도움이 된다. 

## Integrality

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$가 *connected*인 것은 $\lvert X\rvert$가 connected인 것이다. 비슷하게, $X$가 *irreducible*인 것은 $\lvert X\rvert$가 irreducible인 것이다.

</div>

위의 두 성질들은 $\lvert X\rvert$의 언어로 표현된다는 점에서 위상적인 성질들이라 할 수 있다. Connected가 아닌 scheme의 예시는 $V(x(x-1))$이 있으며, connected이지만 irreducible하지 않은 scheme의 예시로는 $V(xy)$이 있다. 

img

한편 $X$는 대수적인 대상이기도 하므로, 대수적인 성질들을 정의할 수도 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Scheme $X$가 *reduced*인 것은 임의의 열린집합 $U$에 대하여 $\mathscr{O}_X(U)$가 reduced인 것이다. 비슷하게, $X$가 *integral*인 것은 임의의 열린집합 $U$에 대하여 $\mathscr{O}_X(U)$가 integral domain인 것이다. ([\[대수적 구조\] §정역, ⁋정의 11](/ko/math/algebraic_structures/integral_domains#def11))

</div>

Non-reduced scheme의 예시로는 $V(y=x^2)$이 있다. 

img

[명제 4](#prop4)는 이러한 대수적인 성질과 위상적인 성질들 사이의 관계를 보여준다. 증명을 위해서는 다음 보조정리를 먼저 보이는 것이 쓸만하다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Affine scheme $\Spec A$가 irreducible인 것은 nilradical $\mathfrak{N}(A)$가 prime ideal인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\Spec A$가 irreducible인 것은 이 공간의 임의의 두 basis $D(f),D(g)\neq\emptyset$에 대하여 $D(fg)\neq\emptyset$인 것과 동치이다. 그런데 다음 동치관계

$$D(f)\neq\emptyset\iff f\not\in \mathfrak{p}\text{ for some $\mathfrak{p}$}\iff f\not\in \mathfrak{N}(A)$$

로부터, ([\[대수적 구조\] §정역, ⁋명제 14](/ko/math/algebraic_structures/integral_domains#prop14)) 명제 $D(f),D(g)\neq\emptyset\implies D(fg)\not\in\emptyset$은 다음 명제

$$f,g\not\in \mathfrak{N}(A)\implies fg\not\in \mathfrak{N}(A)$$

와 동치임을 안다. 

</details>

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $X$가 integral인 것과, $X$가 reduced, irreducible인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$가 integral이라 하자. 임의의 integral domain은 항상 reduced이므로 $X$는 reduced scheme이다. 만일 $X$가 irreducible scheme이 아니라 하면, 서로소인 두 열린집합 $U_1,U_2\neq\emptyset$가 존재한다. 그럼 이제 $\mathcal{O}(U_1\cup U_2)=\mathcal{O}(U_1)\times \mathcal{O}(U_2)$가 되어 $X$가 integral이라는 가정에 모순이 된다.

반대로 $X$가 reduced이고 irreducible이라 가정하고, $X$가 integral scheme임을 보이자. 이를 위해서 우리는 임의의 *affine* open subset $U$에 대해 $\mathcal{O}(U)$가 integral임을 보인다. 우선 $A=\mathcal{O}(U)$는 가정에 의해 reduced이고, $U=\Spec A$는 irreducible space의 열린집합이므로 irreducible이고, 따라서 $\mathfrak{N}(A)=0$가 prime ideal이다. 즉 $\mathcal{O}(U)$가 integral이다.

이제 임의의 열린집합 $V\subseteq X$를 생각하면, scheme의 정의에 의하여 적당한 affine open subset $U\subseteq V$가 존재하고, 따라서 restriction map $\rho_{VU}:\mathcal{O}(V) \rightarrow \mathcal{O}(U)$이 존재한다. 그럼 $\rho_{VU}$는 injective이고, integral domain의 subring은 integral이므로 $\mathcal{O}(V)$가 integral domain이 된다.

따라서 증명을 완료하기 위해서는 $\rho_{VY}$가 injective임을 보이면 충분하다. $f\in\ker\rho_{VU}$라 하자. $f=0$임을 보이기 위해서는 $V$에 속하는 임의의 다른 affine open subset $W$에 대하여 $f$가 $W$에서 $0$이 됨을 보이면 충분하다. 그런데 $\mathcal{O}(W)$는 앞서 증명한 것에 의해 integral이고, $f$가 $U\cap W$에서 $0$이므로 $f$는 $W$에서 $0$이 되어야 한다. 

</details>

## Finiteness

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Scheme $X$가 *locally noetherian*인 것은 $X$의 적당한 open affine cover $\\{\Spec A\_i\\}$가 존재하여 각각의 $A\_i$가 모두 noetherian인 것이다. 만일 $X$가 추가적으로 quasicompact이기도 하다면 $X$를 *noetherian*이라 부른다.

</div>

이름으로부터, locally noetherian scheme과 noetherian scheme 사이에는 적당한 관계가 있어야 한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Scheme $X$가 locally noetherian인 것과 임의의 affine open subset $U=\Spec A$에 대하여 항상 $A$가 noetherian이 되는 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Partition of unity

</details>

여전히 더 많은 종류의 성질들이 남아있다. 

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Scheme morphism $f:X \rightarrow Y$가 *locally of finite type*인 것은 $Y$의 affine open cover $\\{V_i=\Spec B_i\\}$가 존재하여, 각각의 $i$마다 다시 $f^{-1}(V_i)$를 affine open subset들 $U_{ij}=\Spec A_{ij}$로 덮을 수 있는 것이다. 여기서 $A_{ij}$는 finitely generated $B_i$-algebra들이다. 만일 각각의 $f^{-1}(V_i)$들이 유한하게 많은 $U_{ij}$들로 덮일 수 있다면 이를 *of finite type*이라 부른다. 

</div>

예를 들어, inclusion $k[x]\rightarrow k[x,y]$를 생각하면, 이로부터 나오는 projection $\mathbb{A}_k^2 \rightarrow \mathbb{A}_k^1$은 morphism of finite type이다. 이와 같이 finite type morphism은 기하적으로는 (generic) fiber가 finite dimensional인 것으로 생각할 수 있으며, 이는 대수적으로 $k[x,y]$가 finitely generated $k[x]$-algebra인 것으로 설명된다. 

img

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme morphism $f:X \rightarrow Y$가 *finite*인 것은 $U$의 affine open cover $\\{V_i=\Spec B_i\\}$가 존재하여, $f^{-1}(V_i)=\Spec A_i$들이 affine이고 $A_i$가 $B_i$-module로서 finitely generated인 것이다.

</div>

예를 들어, 위의 inclusion $k[x] \rightarrow k[x,y]$에 projection $k[x,y] \rightarrow k[x,y]/(y^2-x)$을 합성하면 ring homomorphism $k[x] \rightarrow k[x,y]/(y^2-x)$을 얻으며, 기하적으로 이는 포물선 $y^2=x$에서 $x$축 방향으로 수선의 발을 내리는 projection map에 해당한다. 이 또한 기하적으로는 fiber가 유한집합이라는 것과 관련이 있다. $\Spec k[x]$의 prime ideal $(x-a)$를 생각하면, 이 prime ideal의 projection에 대한 fiber는 두 개, 즉 $(x-a,y-\sqrt{a})$와 $(x-a,y+\sqrt{a})$의 두 개가 있다. 

img

## Dimension

위의 직관을 제대로 설명하기 위해서는 차원과 fiber를 각각 정의해야 한다. 차원은 정의하기 쉽다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Scheme $X$의 *dimension*은 $X$의 위상공간으로서의 차원을 뜻한다. 만일 $Z$가 $X$의 irreducivle closed subsetdㅣ라면, $Z$의 $X$에서의 *codimension*은 을 뜻한다.

</div>

## Fiber product