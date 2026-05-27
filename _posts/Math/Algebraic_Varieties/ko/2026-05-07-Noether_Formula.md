---title: "Noether Formula"
description: "매끄러운 사영 곡면의 자기교차수, 위상 오일러 특성, 구조 다발의 오일러 특성을 연결하는 노이더 공식을 히르체브뤼히-리만-로크 정리로부터 유도하고, 기하학적 의미와 구체적 예시를 통해 검증한다."
permalink: /ko/math/algebraic_varieties/noether_formula
excerpt: "Noether formula와 그 응용들"
categories: [Math / Algebraic Varieties]
sidebar:
    nav: "algebraic_varieties-ko"
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/Noether_Formula.png
    overlay_filter: 0.5
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 25
published: false
---

Smooth projective surface의 기하학을 분류하는 데 있어 가장 기본적인 불변량들은 자기교차수 $K_S^2$, topological Euler characteristic $\\rchi_{\\mathrm{top}}(S)$, 그리고 structure sheaf의 Euler characteristic $\\rchi(\\rO_S)$이다. 이 세 불변량 사이에는 놀랍도록도 단순한 선형관계가 존재하며, 이를 **Noether formula**라 부른다. 본 글에서는 Hirzebruch-Riemann-Roch 정리의 곡면으로의 환원을 통해 Noether formula를 유도하고, $c_2(S)$의 기하학적 의미를 설명한 뒤, 다양한 구체적인 예시를 통해 이 공식을 검증한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective surface $S$의 **topological Euler characteristic** $\\rchi_{\\mathrm{top}}(S)$는

$$\\rchi_{\\mathrm{top}}(S)=\\sum_{i=0}^4(-1)^i\\dim H^i(S,\\Q)$$

으로 정의된다.

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Poincaré-Hopf)**</ins> Smooth projective surface $S$에 대하여, 그 두 번째 Chern class의 적분값은 topological Euler characteristic과 일치한다. 즉

$$\\int_S c_2(T_S)=\\rchi_{\\mathrm{top}}(S)$$

이 성립한다.

</div>

Poincaré-Hopf theorem의 증명과 직관은 [§Chern Classes, ⁋명제 12](/ko/math/algebraic_varieties/chern_classes#prop12)에서 자세히 다루었으므로 여기서는 생략한다. 이 명제는 $c_2(S)$가 단순한 형식적 불변량이 아니라, surface의 위상적 구조를 측정하는 기하학적 양임을 보장한다. 예를 들어 $\\bbP^2$의 경우 $\\rchi_{\\mathrm{top}}(\\bbP^2)=3$이며, 이는 $c_2(T_{\\bbP^2})=3H^2$의 적분값과 일치함을 [§Chern Classes, ⁋예시 10](/ko/math/algebraic_varieties/chern_classes#ex10)에서 확인하였다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3 (Noether formula)**</ins> Algebraically closed field 위의 smooth projective surface $S$에 대하여 다음이 성립한다.

$$K_S^2+c_2(S)=12\\rchi(\\rO_S)$$

여기서 $K_S$는 canonical divisor, $c_2(S)=c_2(T_S)$는 tangent bundle의 두 번째 Chern class, $\\rchi(\\rO_S)$는 structure sheaf의 Euler characteristic이다.

</div>

Noether formula는 surface의 대수적 불변량 $\\rchi(\\rO_S)$와 기하학적 불변량 $K_S^2$, 위상적 불변량 $c_2(S)$를 하나의 선형 관계로 묶는다. 이는 곡면의 기하학을 분류하는 데 있어 핵심적인 도구로, 특히 Enriques-Kodaira 분류에서 각 birational equivalence class의 불변량들을 제한하는 강력한 제약을 제공한다.

<details class="proof" markdown="1">
<summary>증명</summary>

Hirzebruch-Riemann-Roch 정리 ([§Hirzebruch-Riemann-Roch, ⁋정리 2](/ko/math/algebraic_varieties/hirzebruch_riemann_roch#thm2))에 의해, smooth projective surface $S$ 위의 line bundle $\\rO_S$에 대하여

$$\\rchi(S,\\rO_S)=\\int_S\\operatorname{ch}(\\rO_S)\\cdot\\operatorname{td}(T_S)$$

이 성립한다. Structure sheaf의 Chern character는 $\\operatorname{ch}(\\rO_S)=1$이며, [§Todd Class, ⁋예시 6](/ko/math/algebraic_varieties/todd_class#ex6)에 의해 tangent bundle의 Todd class는

$$\\operatorname{td}(T_S)=1+\\frac{c_1(T_S)}{2}+\\frac{c_1(T_S)^2+c_2(T_S)}{12}$$

이다. Canonical divisor는 $K_S=-c_1(T_S)$를 만족하므로,

$$\\operatorname{td}(T_S)=1-\\frac{K_S}{2}+\\frac{K_S^2+c_2(S)}{12}$$

이다. 이들의 곱에서 $2$차 성분을 취하면 $\\frac{K_S^2+c_2(S)}{12}$이므로, HRR 정리에 의해

$$\\rchi(\\rO_S)=\\int_S\\frac{K_S^2+c_2(S)}{12}=\\frac{K_S^2+c_2(S)}{12}$$

이다. 양변에 $12$를 곱하면 Noether formula를 얻는다. $\\square$

</details>

정리 [3](#thm3)의 증명에서 확인할 수 있듯이, Noether formula는 Hirzebruch-Riemann-Roch 정리에 $\\mathcal{F}=\\rO_S$를 대입한 직접적인 결과이다. 이는 HRR 정리가 단순한 계산적 도구를 넘어, 서로 다른 영역의 불변량들 사이의 심층적인 연결을 제공함을 보여준다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> Smooth projective surface $S$에 대하여

$$12\\rchi(\\rO_S)=K_S^2+\\rchi_{\\mathrm{top}}(S)$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

명제 [2](#prop2)에 의해 $c_2(S)=\\rchi_{\\mathrm{top}}(S)$이므로, 이를 Noether formula의 $c_2(S)$에 대입하면 즉각적으로 결과를 얻는다. $\\square$

</details>

따름정리 [4](#cor4)는 Noether formula를 기하-위상적 관점에서 재해석한다. $K_S^2$은 surface의 "대수적 복잡도"를, $\\rchi_{\\mathrm{top}}(S)$는 "위상적 복잡도"를 측정하며, 이들의 합이 항상 $12$의 배수가 된다는 사실은 놀라운 정수성 조건을 제공한다.

## 지표와의 관계

Noether formula의 우변에 등장하는 $\\rchi(\\rO_S)$는 surface의 여러 중요한 지표들과 밀접하게 연결된다. Serre duality와 Hodge theory를 통해 이 불변량을 보다 구체적인 cohomological 지표로 전개할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Smooth projective surface $S$에 대하여

$$\\rchi(\\rO_S)=1-q+p_g$$

이 성립한다. 여기서 $q=h^1(S,\\rO_S)$는 **불규칙성**<sub>irregularity</sub>, $p_g=h^0(S,K_S)$는 **기하적 genus**<sub>geometric genus</sub>이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Euler characteristic의 정의에 의해

$$\\rchi(\\rO_S)=h^0(\\rO_S)-h^1(\\rO_S)+h^2(\\rO_S)$$

이다. $S$가 연결된 projective variety이므로 $h^0(\\rO_S)=1$이다. Serre duality ([§세르 쌍대성, ⁋명제 4](/ko/math/algebraic_varieties/serre_duality#prop4))에 의해

$$h^2(\\rO_S)=h^0(K_S)=p_g$$

이며, $q$의 정의에 의해 $h^1(\\rO_S)=q$이다. 이들을 종합하면

$$\\rchi(\\rO_S)=1-q+p_g$$

를 얻는다. $\\square$

</details>

명제 [5](#prop5)에 의해 Noether formula는

$$K_S^2+\\rchi_{\\mathrm{top}}(S)=12(1-q+p_g)$$

의 형태로도 쓸 수 있다. 이 식에서 $q$와 $p_g$는 surface의 birational equivalence class의 불변량이며, 특히 $q$와 $p_g$는 birational transform 하에서 변하지 않는다. 반면 $K_S^2$과 $\\rchi_{\\mathrm{top}}(S)$는 blow-up을 통해 변화하나, 그 변화량이 서로 정확히 상쇄되어 Noether formula의 등식을 유지한다.

## 예시

구체적인 surface들에 대해 Noether formula를 직접 검증함으로써, 이 정리의 내용과 불변량들의 계산 방법을 확립한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($\\bbP^2$)**</ins> Projective plane $S=\\bbP^2$에 대하여, canonical divisor는 $K_{\\bbP^2}=-3H$이며 $H$는 hyperplane class이다. 따라서

$$K_{\\bbP^2}^2=(-3H)^2=9H^2=9$$

이다. [§Chern Classes, ⁋예시 10](/ko/math/algebraic_varieties/chern_classes#ex10)에 의해 $c_2(T_{\\bbP^2})=3H^2$이므로 $\\int_{\\bbP^2}c_2=3$이다. 한편 [§사영공간의 코호몰로지, ⁋따름정리 3](/ko/math/algebraic_varieties/cohomology_of_projective_spaces#cor3)에 의해 $h^i(\\bbP^2,\\rO_{\\bbP^2})=0$ for $i>0$이므로

$$\\rchi(\\rO_{\\bbP^2})=h^0(\\rO_{\\bbP^2})=1$$

이다. 따라서 $9+3=12\\cdot 1$이 성립하여 Noether formula를 만족한다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7 ($\\bbP^1\\times\\bbP^1$)**</ins> Product surface $S=\\bbP^1\\times\\bbP^1$에 대하여, $H_1$과 $H_2$를 각 인자로의 pullback of hyperplane class라 하면 canonical divisor는 $K_S=-2H_1-2H_2$이다. $H_1^2=H_2^2=0$이고 $H_1\\cdot H_2=1$이므로

$$K_S^2=(-2H_1-2H_2)^2=4H_1^2+8H_1\\cdot H_2+4H_2^2=8$$

이다. [§Chern Classes, ⁋예시 11](/ko/math/algebraic_varieties/chern_classes#ex11)에 의해 $c_2(T_S)=4H_1H_2$이므로 $\\int_S c_2=4$이다. Künneth formula에 의해

$$\\rchi(\\rO_S)=\\rchi(\\rO_{\\bbP^1})\\cdot\\rchi(\\rO_{\\bbP^1})=1\\cdot 1=1$$

이며, 따라서 $8+4=12\\cdot 1$이 성립한다.

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8 ($\\bbP^2$의 $r$점 blow-up)**</ins> $\\pi:\\widetilde{\\bbP}^2\\rightarrow\\bbP^2$를 $r$개의 일반적인 점에서의 blow-up이라 하자. Canonical divisor는

$$K_{\\widetilde{\\bbP}^2}=\\pi^\\ast K_{\\bbP^2}+E_1+\\cdots+E_r=-3\\pi^\\ast H+E_1+\\cdots+E_r$$

이다. 여기서 $E_i$는 $i$-번째 exceptional divisor이며, $E_i^2=-1$이고 $i\\neq j$일 때 $E_i\\cdot E_j=0$, 또 $\\pi^\\ast H\\cdot E_i=0$이다. 따라서

$$K_{\\widetilde{\\bbP}^2}^2=9-r$$

이다. Topological Euler characteristic의 관점에서, 각 blow-up은 한 점을 exceptional $\\bbP^1$로 교체하므로 Euler characteristic이 $1$씩 증가한다. $\\rchi_{\\mathrm{top}}(\\bbP^2)=3$이므로

$$\\rchi_{\\mathrm{top}}(\\widetilde{\\bbP}^2)=3+r$$

이다. 한편 $\\rchi(\\rO)$는 smooth projective surface의 birational 불변량이므로

$$\\rchi(\\rO_{\\widetilde{\\bbP}^2})=\\rchi(\\rO_{\\bbP^2})=1$$

이다. 따라서 $(9-r)+(3+r)=12=12\\cdot 1$이 성립한다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9 ($\\bbP^3$ 속 degree $d$ smooth surface)**</ins> $S\\subset\\bbP^3$를 degree $d$인 smooth surface라 하자. Adjunction formula에 의해

$$K_S=(K_{\\bbP^3}+S)\\vert_S=(-4H+dH)\\vert_S=(d-4)h$$

이다. 여기서 $h=H\\vert_S$이며, $\\int_S h^2=d$이다. 따라서

$$K_S^2=(d-4)^2\\int_S h^2=d(d-4)^2$$

이다. $c_2(S)$를 계산하기 위해 exact sequence

$$0\\longrightarrow T_S\\longrightarrow T_{\\bbP^3}\\vert_S\\longrightarrow\\rO_S(d)\\longrightarrow 0$$

를 이용한다. Whitney sum formula에 의해 $c(T_{\\bbP^3}\\vert_S)=c(T_S)\\cdot c(\\rO_S(d))$이며, $c(T_{\\bbP^3})=(1+H)^4$로부터 $c(T_{\\bbP^3}\\vert_S)=1+4h+6h^2$이다. $c(\\rO_S(d))=1+dh$이므로, $c(T_S)=1+c_1+c_2$를 대입하여 비교하면

$$c_1=(4-d)h,\\qquad c_2=(d^2-4d+6)h^2$$

을 얻는다. 따라서

$$\\int_S c_2=d(d^2-4d+6)$$

이다. 이제 $\\rchi(\\rO_S)$를 계산한다. Lefschetz hyperplane theorem에 의해 $q=h^1(\\rO_S)=0$이고, Serre duality에 의해 $h^2(\\rO_S)=h^0(K_S)=h^0(\\rO_S(d-4))$이다. $d<4$이면 $p_g=0$이므로 $\\rchi(\\rO_S)=1$이고, $d=4$이면 $K_S=0$이므로 $p_g=1$이어서 $\\rchi(\\rO_S)=2$이다. 일반적으로

$$p_g=h^0(\\rO_S(d-4))=\\binom{d-1}{3}=\\frac{(d-1)(d-2)(d-3)}{6}$$

이므로

$$\\rchi(\\rO_S)=1+\\frac{(d-1)(d-2)(d-3)}{6}$$

이다. 이제 Noether formula를 검증하면

$$K_S^2+\\int_S c_2=d(d-4)^2+d(d^2-4d+6)=2d^3-12d^2+22d$$

이고

$$12\\rchi(\\rO_S)=12+2(d-1)(d-2)(d-3)=2d^3-12d^2+22d$$

이므로 양쪽이 일치함을 확인한다.

</div>

예시 [9](#ex9)에서 $d=4$인 경우, 즉 quartic K3 surface의 경우 $K_S=0$이고 $K_S^2=0$, $\\rchi_{\\mathrm{top}}(S)=24$, $\\rchi(\\rO_S)=2$이므로 $0+24=12\\cdot 2$가 성립한다. 이는 K3 surface의 대표적인 불변량들과 일치하며, 이러한 계산이 surface의 classification에서 어떻게 활용되는지를 보여준다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Ful]** W. Fulton, *Intersection Theory*, Springer, 1984.

**[Hir]** F. Hirzebruch, *Topological Methods in Algebraic Geometry*, Springer, 1966.

**[BHPV]** W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, Springer, 2004.
