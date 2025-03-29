---

title: "조르단-횔더 정리"
excerpt: ""

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/Jordan-Holder_theorem
header:
    overlay_image: /assets/images/Math/Group_Theory/Jordan-Holder_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "group_theory-ko"

date: 2025-03-29
last_modified_at: 2025-03-29
weight: 2

---

첫 번째로 우리가 살펴볼 결과는 Jordan-Hölder 정리이다.

Group을 분류할 때 주요한 전략 중 하나는 group의 subgroup들 사이의 관계를 보는 것이며, 이를 위해 우리는 임의의 group $G$의 subgroup들의 모임을 생각한 후, 여기에 $\subset$을 통해 순서관계를 준다. 그럼 이 ordered set이 lattice가 된다는 것은 자명하다. ([\[집합론\] §유향집합, ⁋정의 4](/ko/math/set_theory/directed_set#def4)) 물론 isomorphic하지 않은 두 개의 group들의 subgroup들의 lattice가 서로 isomorphic할 수 있기는 하지만, 적어도 subgroup들의 lattice가 non-isomorphic한 두 개의 group들이 서로 isomorphic할 수는 없으므로 이 전략은 좋은 시작점이 된다.

한편 우리는 [\[대수적 구조\] §군 동형사상, ⁋정리 7](/ko/math/algebraic_structures/isomorphism_theorems#thm7)로부터 임의의 group $G$와 normal subgroup $N$이 주어졌다면, $N$을 포함하는 $G$의 subgroup들의 lattice와, $G/N$의 subgroup들의 lattice가 서로 isomorphic하다는 것을 안다. 만일 $G$가 유한한 group이고, $N$이 trivial group이 아니었다면 