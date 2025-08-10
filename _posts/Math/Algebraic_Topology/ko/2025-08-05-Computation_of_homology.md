---

title: "호몰로지의 계산"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/computation_of_homology
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Computation_of_homology.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-08-05
last_modified_at: 2025-08-05
weight: 5

---

우리는 이제 호몰로지를 실질적으로 계산할 수 있는 도구들을 살펴본다. 임의의 공간에 대해 이 공간의 호몰로지를 정의로부터 직접 계산하는 것은 거의 불가능한 일이므로, 우리는 큰 공간들을 작은 공간으로 쪼개고 이들의 호몰로지들로부터 큰 공간의 호몰로지를 계산하는 도구를 개발할 것이다. 

Colimit의 예시 중 하나는 합집합이므로, 이를 위해 적합한 도구의 후보 중 하나는 당연히 Seifert-van Kampen 정리일 것이다. ([§피복공간, ⁋정리 13](/ko/math/algebraic_topology/covering_spaces#thm13)) 뿐만 아니라 abeliainization functor는 forgetful functor의 left adjoint functor이고 ([\[대수적 구조\] §가환군, ⁋명제 7](/ko/math/algebraic_structures/abelian_groups#prop7)) left adjoint functor는 colimit을 보존하므로 이것이 여전히 호몰로지에 대해서도 정보를 줄 것이다.