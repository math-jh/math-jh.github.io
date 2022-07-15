---

title: "반 캄펜 정리"
excerpt: "Fundamental group"

categories: [Math / Topology]
permalink: /ko/math/topology/Van_Kampen_theorem
header:
    overlay_image: /assets/images/Topology/Van_Kampen_theorem.png
    overlay_filter: 0.5
sidebar: 
    nav: "topology-ko"

date: 2022-06-30
last_modified_at: 2022-06-30
weight: 104
    
---

우리는 앞선 글에서 다양한 위상공간의 기본군을 살펴보았는데, 이번 글에서의 반 캄펜 정리[^1]는 더 복잡한 위상공간의 기본군을 계산하는 방법을 제공해준다.

## 반 캄펜 정리

Path-connected인 위상공간 $X$와, $X$의 path-connected open subset들 $A\_\alpha$가 주어져서 $X=\bigcup A\_\alpha$를 만족한다 하자. 그럼 $i\_\alpha:A\_\alpha\hookrightarrow X$에 의하여 fundamental group들의 morphism $(i\_\alpha)\_\ast:\pi\_1(A\_\alpha)\rightarrow\pi\_1(X)$가 잘 정의된다. 이제 free product의 universal property에 의하여, homomorphism

$$\Phi:{\prod_{i\in I}}^\ast\pi_1(A_\alpha)\rightarrow \pi_1(X)$$

이 유일하게 결정된다. 예를 들어, 이렇게 결정된 $\Phi$가 isomorphism이라면 이는 $\pi_1(X)$를 그 부분공간들의 fundamental group을 계산함으로서 얻을 수 있다는 의미가 될 것이다. 이는 분명 매력적인 결과이겠지만, 만일 이것이 참이라면 fundamental group은 어떠한 재미있는 결과도 주지 않을 것이다. 예컨대 $S^1$을 두 개의 path-connected, simply connected인 열린집합으로 쪼갤 수 있기 때문이다.

위의 간단한 반례는 일반적인 경우 $\Phi$가 surjective하지 않다는 것을 보여준다. 우리는 일반적으로 $\Phi$가 injective하지 않으리라는 것 또한 간단한 논증을 통해 보일 수 있다.

$A_\alpha$와 $A_\beta$에 공통적으로 포함되어 있는 고리가 있다고 가정하자. $A_\alpha\cap A_\beta$에서 $A_\alpha$로의 injection을 $i_{\alpha\beta}$를 으로 표기하기로 하면, 임의의 $\sigma\in\pi_1(A_\alpha\cap A_\beta)$에 대하여 $i_{\alpha\beta}(\sigma)$와 $i_{\beta\alpha}(\sigma)$는 본질적으로 동일한 원소 $\sigma$임에도 불구하고 free product에서는 두 번 중복하여 계산된다.

반 캄펜 정리는 이 문제들을 한 번에 해결해준다. 즉, $\Phi$가 surjective할 조건을 제시해주며, 동시에 특정 조건 하에서 $\Phi$의 kernel이 정확하게 위의 문제를 해결하는 subgroup, 즉 $i_{\alpha\beta}(\sigma)i_{\beta\alpha}(\sigma)^{-1}$로 생성되는 subgroup임을 보여준다.

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1 (Seifert-van Kampen)**</ins> 위상공간 $X$와, path-connected open set들 $A_\alpha$가 주어졌다 하고, 위의 상황을 가정하자.

1. $A_\alpha$들이 모두 basepoint $x_0$를 공유하고, $A_\alpha\cap A_\beta$가 모두 path-connected라 가정하자. 그럼 $\Phi$는 surjective이다.
2. 만일 1번의 조건에 더하여, 모든 triple intersection $A_\alpha\cap A_\beta\cap A_\gamma$가 path-connected라면, $\Phi$의 kernel은 $i_{\alpha\beta}(\sigma)i_{\beta\alpha}(\sigma)^{-1}$들로 생성되는 normal subgroup이다.

</div>

따라서 2번의 조건이 만족될 경우 $\Phi$를 통해 $\pi_1(X)\cong\bigl(\prod^\ast \pi\_1(A\_\alpha)\bigr)/N$임을 알 수 있다. 반 캄펜 정리의 대부분은 $X$가 두 개의 open set으로 분해되는 경우에 적용되며, 이 때 2번 조건은 자동으로 만족된다. 다만 일반적인 경우를 증명하는 것 또한 그렇게 어렵지는 않다.

<details class="proof" markdown="1">
<summary>증명</summary>



</details>



[^1]: Seifert-van Kampen theorem. Herbert Seifert는 독일의 수학자 (1897~1996), van Kampen은 네덜란드의 수학자 (1908~1942).