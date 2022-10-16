---

title: "컴팩트"
excerpt: ""

categories: [Math / Topology]
permalink: /ko/math/topology/compactness
header:
    overlay_image: /assets/images/Topology/Compactness.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-10-17
last_modified_at: 2022-10-17
weight: 15

published: false
    
---

이번 글에서 소개할 컴팩트의 개념은 그 동안 보아왔던 개념들에 비하면 그 정의가 인위적으로 느껴질 수 있지만, 수학의 모든 분야에서 중요하게 사용된다.

<div class="definition" markdown="1">

<ins id="df1">**정의 1**</ins> 위상공간 $X$가 *컴팩트<sub>compact</sub>*라는 것은 $X$의 임의의 open covering $\mathcal{A}$가 주어질 때마다, $\mathcal{A}$에 속한 열린집합 중 유한 개만 택하여 $X$를 덮을 수 있는 것이다.

</div>

일반적으로 어떤 집합이 컴팩트임을 보일 때 위의 정의를 바로 적용하는 것은 좋은 생각이 아니다. 컴팩트성에 대한 몇 개의 명제들을 보이자. 