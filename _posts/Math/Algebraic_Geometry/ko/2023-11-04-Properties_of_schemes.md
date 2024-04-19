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

이제 우리는 scheme이 갖는 여러가지 성질들을 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme $X$가 *connected*인 것은 $\lvert X\rvert$가 connected인 것이다. 비슷하게, $X$가 *irreducible*인 것은 $\lvert X\rvert$가 irreducible인 것이다.

</div>

위의 두 성질들은 $\lvert X\rvert$의 언어로 표현된다는 점에서 위상적인 성질들이라 할 수 있다. 한편 $X$는 대수적인 대상이기도 하므로, 대수적인 성질들을 정의할 수도 있다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Scheme $X$가 *reduced*인 것은 임의의 열린집합 $U$에 대하여 $\mathscr{O}_X(U)$가 reduced인 것이다. 비슷하게, $X$가 *integral*인 것은 임의의 열린집합 $U$에 대하여 $\mathscr{O}_X(U)$가 integral domain인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $X$가 integral인 것과, $X$가 reduced, irreducible인 것이 동치이다.

</div>

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Scheme $X$가 *locally noetherian*인 것은 $X$의 적당한 open affine cover $\\{\Spec A\_i\\}$가 존재하여 각각의 $A\_i$가 모두 noetherian인 것이다. 만일 $X$가 추가적으로 quasicompact이기도 하다면 $X$를 *noetherian*이라 부른다.

</div>

다음 명제로부터 noetherian이라는 성질이 성질이 local하게 체크될 수 있다는 것을 확인할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Scheme $X$가 locally noetherian인 것과 임의의 affine open subset $U=\Spec A$에 대하여 항상 $A$가 noetherian이 되는 것이 동치이다.

</div>

이와 같은 맥락에서 morphism들의 성질도 affine-local하게 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme morphism $f:X \rightarrow Y$가 *locally of finite type*인 것은 $Y$의 affine open cover $\\{V_i=\Spec B_i\\}$가 존재하여, 각각의 $i$마다 다시 $f^{-1}(V_i)$를 affine open subset들 $U_{ij}=\Spec A_{ij}$로 덮을 수 있는 것이다. 여기서 $A_{ij}$는 finitely generated $B_i$-algebra들이다. 만일 각각의 $f^{-1}(V_i)$들이 유한하게 많은 $U_{ij}$들로 덮일 수 있다면 이를 *of finite type*이라 부른다. 

</div>

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Scheme morphism $f:X \rightarrow Y$가 *finite*인 것은 $U$의 affine open cover $\\{V_i=\Spec B_i\\}$가 존재하여, $f^{-1}(V_i)=\Spec A_i$들이 affine이고 $A_i$가 $B_i$-module로서 finitely generated인 것이다.

</div>