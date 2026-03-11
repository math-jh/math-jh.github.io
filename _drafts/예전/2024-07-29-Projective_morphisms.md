---

title: "사영사상"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/projective_morphisms
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Projective_morphisms.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-07-29
last_modified_at: 2024-07-29
weight: 14

---

Ring $A$를 고정하자. 그럼 $\mathbb{P}^n_A=\Proj A[x_0,\ldots, x_n]$는 $\mathbb{P}^n_\mathbb{Z}\Spec A$로 불 수 있으며 $\mathscr{O}_{\mathbb{P}^n_A}(1)$은 $\mathbb{P}^n_\mathbb{Z}$ 위에 정의된 $\mathscr{O}(1)$의 pullback이며, $\mathscr{O}(1)$은 global section들 $x_0,\ldots, x_n$에 의해 생성된다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Ring $A$와 $A$-scheme $X$를 생각하자. 

1. $A$-morphism $\phi:X \rightarrow \mathbb{P}^n_A$에 대하여, $\phi^\ast \mathscr{O}(1)$은 $X$ 위에 line bundle을 정의하며, 이는 global section들 $s_i=\phi^\ast x_i$로 생성된다. 
2. 거꾸로 임의의 line bundle $\mathscr{L}$이 $s_0,\ldots, s_n$에 의해 globally generated라면, 유일한 $A$-morphism $\phi:X \rightarrow \mathbb{P}^n_A$가 존재하여 $\mathscr{L}\cong \phi^\ast \mathscr{O}(1)$이고 $s_i=\phi^\ast x_i$이다. 

</div>

이게 closed일 조건 7.2 7.3

따라서 projective space의 variety는 line bundle과 global section들에 대한 데이터로 대체될 수 있다. 

