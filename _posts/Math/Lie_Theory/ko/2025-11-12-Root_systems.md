---

title: "근계"
excerpt: ""

categories: [Math / Lie Theory]
permalink: /ko/math/Lie_theory/root_systems
header:
    overlay_image: /assets/images/Math/Lie_Theory/Root_systems.png
    overlay_filter: 0.5
sidebar: 
    nav: "Lie_theory-ko"

date: 2025-11-12
last_modified_at: 2025-11-12
weight: 2

---

이전 글에서 우리는 (simply connected) Lie group의 classification이 Lie algebra의 classification에 의해 결정되는 것을 보았다. 일박적으로 기하적인 대상들을 분류하는 문제는 매우 비자명한 반면, 대수적인 구조를 분류하는 것은 대부분의 경우 그렇게 어렵지 않았다. 우리는 이러한 이유로 임의의 Lie algebra를 classify하는 것에 관심을 가지게 된다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 임의의 non-abelian Lie algebra $\mathbb{g}$가 *simple*이라는 것은 $\mathfrak{g}$의 ideal이 $0$과 자기자신 뿐인 것이다. Simple Lie algebra들의 direct sum으로 이루어진 Lie algebra를 *semi-simple Lie algebra*라 부른다. 

</div>

한편 임의의 abelian Lie algebra는 그저 곱셤이 정의되지 않은 일반적인 벡터공간에 불과하다. 더 일판적으로 우리는 다음의 derived series

$$\mathfrak{g}\geq[\mathfrak{g},\mathfrak{g}]\geq[[\mathfrak{g},\mathfrak{g}],[\mathfrak{g},\mathfrak{g}]]\geq \cdots$$

가 최종적으로 zero ideal이 된다면 이를 *solvable* Lie algebra라 부른다. 이는 abelian Lie algebra의 일반화로서, 최종적으로는 bracket structure가 trivial한 것들이다. 그럼 다음의 정리는 본질적으로 우리가 semisimple Lie algebra들에 관심을 기울여야 하는 이유를 보여준다. 

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2**</ins> Base field $\mathbb{k}$가 $\ch(\mathbb{k})=0$을 만족하는 임의의 유한차원 Lie $\mathbb{k}$-algebra $\mathfrak{g}$는 solvable ideal과 semisimple subalgebra의 semidirect product이다.

</div>

정의에 의해 solvable ideal은 zero ideal로푸터 시작하여 차원을 하나씩 늘리가는 extension들의 sequence로 생각할 수 있다. 따라서 이들을 classify하는 것은 불가능하지만 그 구조 자체가 복잡한 것은 아니다. 바꾸어 말하자면 Lie algebra의 classification은 가의 전적으로 semisimple Lie algebra의 classification과 관련되어있다. 

