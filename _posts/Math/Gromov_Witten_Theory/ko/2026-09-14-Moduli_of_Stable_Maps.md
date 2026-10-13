---
title: "안정사상들의 모듈라이 공간"
description: "Stable map들의 proper Deligne–Mumford stack과 그 natural morphism·boundary 구조를 살펴보고, deformation과 obstruction의 exact sequence에서 virtual dimension을 계산한다."
excerpt: "Stable map moduli, Deligne–Mumford stack, virtual dimension, convex targets"

categories: [Math / Gromov-Witten Theory]
permalink: /ko/math/gromov-witten_theory/moduli_of_stable_maps
sidebar: 
    nav: "gromov-witten_theory-ko"

date: 2026-09-14
weight: 2
revising: true
drift_needed: true

---

우리는 [\[스택\] §고유스택](/ko/math/stacks/proper_stacks){: data-lid="5ib31" }에서 moduli space의 properness가 갖는 중요성을 이미 살펴보았지만, 일반적인 enumerative problem에서는 이러한 성질을 기대할 수 없다. 이러한 종류의 문제 중 고전적인 것은 $\mathbb{P}^2$ 안의 $3d-1$개의 general point를 지나는 degree $d$ rational curve를 세는 문제로, 예를 들어 $d=2$일 때 그 값은 $1$인 것이 알려져 있다. 즉 $\mathbb{P}^2$ 안의 $5$개의 점을 지나는 곡선은 유일하게 존재하여야 한다. 반면 다음 map

$$\mu_t:\mathbb{P}^1\longrightarrow\mathbb{P}^2,\qquad [\u:\v]\longmapsto[-t\u\v:\u(\u-(1+t)\v):\v(\u-(1+t)\v)],\qquad t\neq 0,-1$$

을 생각하면, 이는 equation

$$C_t=V(\x\y+t\y\z-(1+t)\x\z)$$

를 만족하는 conic이며, 이들은 네 점

$$q_1=[1:0:0],\qquad q_2=[0:1:0],\qquad q_3=[0:0:1],\qquad q_4=[1:1:1]$$

을 지나는 것을 확인할 수 있다. 위의 결과에 따르면 이 네 점에, 추가로 하나의 점을 고르는 것이 $C_t$를 유일하게 결정하게 되는데, 예를 들어 마지막 점을 $q_5=[0:1:2]$로 고르면 조건 $q_5\in C_t$는 $2t=0$, 즉 $t=0$을 강제한다. 그런데 $t=0$에서 이 곡선은 $C_0=V(\x(\y-\z))$으로, 두 직선 $V(\x)$와 $V(\y-\z)$의 합집합이 된다.

이는 smooth rational curve들만으로는 properness가 깨져서 생기는 일로, 이를 해결하기 위해서는 어떠한 식으로든 극한을 추가해주어야 한다. 이를 구현하는 것이 stable map이다. Stable map은 곡선을 map $\mu:C\rightarrow X$와 함께 기억하고 domain에 nodal curve를 허용하여, 갈라진 component와 각 component 위의 map을 limit에 함께 보존한다.

이번 글에서 우리는 target $X$를 항상 복소수 $\mathbb{C}$ 위의 smooth projective variety로 둔다.

## 안정사상

앞선 계산에서 smooth conic의 limit은 두 line이 한 점에서 만나는 곡선이었으므로, 이를 map의 limit으로 보존하려면 domain도 갈라질 수 있어야 한다. 실제로, $\mathbb{P}^1$의 image는 irreducible이므로, domain을 $\mathbb{P}^1$로 고정한 morphism으로는 두 line을 모두 덮을 수 없다. 대신 두 $\mathbb{P}^1$을 한 점에서 붙이고 각각을 해당 line으로 보내면, 붙인 점에서 두 map의 값이 일치하여 전체 domain 위의 morphism을 얻는다. 따라서 이러한 limit을 포함하려면 smooth curve에서 nodal curve로 domain의 범위를 넓혀야 한다.

Incidence condition도 map의 자료로 기록할 수 있다. 곡선이 주어진 점 $q_i\in X$를 지난다는 조건은 domain 위에 점 $p_i$를 지정하고 $\mu(p_i)=q_i$를 요구하면 되므로, 우리가 원하는 map의 domain은 정확히 prestable curve가 모두 담고 있다. ([§마디 곡선의 변형, ⁋정의 1](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#def1){: data-lid="ovp6z" }) 앞의 예에서는 limit의 각 $q_i$에 대응하는 점을 해당 component 위에 표시하면 될 것이며, 일반적인 incidence condition은 $\mu(p_i)$가 지정된 subvariety에 속하도록 부과한다.

이제 우리가 자료를 map에 담을 때 생기는 문제는 같은 곡선이 다른 parametrization을 통해서 바뀌면 이는 다른 map으로 보인다는 것이다. 따라서 우리는 marked point와 map을 보존하는 domain의 isomorphism으로 이들을 identify한다. 문제는 한 자료 안에서도 automorphism이 생길 수 있다는 것인데, 일반적으로 우리가 생각하는 automorphism은 map 자체의 대칭을 나타내는 정보이므로 이는 유의미한 정보이다. 그러나 nodal domain을 허용하면 이러한 유의미한 정보는 아무것도 보태지 않는 parametrization의 자유도가 생길 수 있는데, 예를 들어 한 점으로 보내지는 한 $\mathbb{P}^1$ 성분에 node가 하나 뿐이고, marked point가 아무것도 없으면 이 성분은 무한히 많은 automorphism을 가지지만, 이 성분을 무시해도 나머지 map과 marked point의 정보는 고스란히 남아있다. 이러한 성분을 배제하기 위해 우리는 automorphism group이 유한하다는 stability 조건을 부과하며, 이는 map의 유한한 대칭을 허용하면서 moduli가 Deligne–Mumford stack이 되게 하는 핵심 조건이다. 여기에 곡선의 class $\beta$를 고정하면 다음 정의를 얻는다.

::: 정의 1
Genus $g$의 $n$-pointed prestable curve $(C,p_1,\ldots,p_n)$와 class $\beta\in H_2(X,\mathbb{Z})$가 주어졌다고 하자. *Stable map<sub>안정사상</sub>*은 prestable curve와, 이를 domain으로 갖는 map $\mu$의 쌍

$$(C,p_1,\ldots,p_n,\mu),\qquad \mu:C\rightarrow X$$

으로서, 다음 두 조건을 만족하는 것들이다. 

- $\mu_\ast[C]=\beta$이다.
- Automorphism group $\Aut(C,p_1,\ldots,p_n,\mu)$이 유한하다.

두 stable map은 marked point와 $X$로 가는 map을 보존하는 domain의 isomorphism이 존재할 때 *isomorphic*하다 말한다. 
:::

첫째 조건은 각 성분의 mapping degree를 반영하여 image의 class를 합한 값이 $\beta$라는 뜻이다. 둘째 조건을 살펴보면, automorphism 중 서로 다른 성분들과 node들의 순열로 나오는 것 혹은 self-node의 두 branch를 맞바꾸는 등의 경우의 수는 유한하므로, automorphism의 유한성은 본질적으로 domain curve의 각 성분의 automorphism의 유한성에 대한 조건이 된다. 

이러한 automorphism이 고정하는 것은 marked point들과 node들이 그대로 남아있어야 한다는 조건으로, 우리는 이들 두 종류의 점들을 통틀어 *special points*라 부른다. Domain curve $C$의 irreducible component $C_i$의 normalization을 $\widetilde{C}_i$라 하고, $\widetilde{C}_i$의 special point의 개수를 $s_i$라 하자. 

이제 $\widetilde{C}_i$의 genus를 $h_i$라 하면 tangent bundle $\mathcal{T}_{\widetilde{C}_i}$의 degree는 $2-2h_i$이다. Special point들의 합을 divisor $D_i$로 적으면, [§마디 곡선의 변형, ⁋명제 4](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#prop4){: data-lid="paz7d" }와 그 이후의 논증에 의하여 이 점들을 고정하는 infinitesimal automorphism은

$$H^0\bigl(\widetilde{C}_i,\mathcal{T}_{\widetilde{C}_i}(-D_i)\bigr)$$

로 계산된다. 이는 $\widetilde{C}_i$의 special point들을 각각 고정하는 automorphism group $G$의 항등원에서의 tangent space와 같았으므로, 만일 이 차원이 $0$이 된다면 $G$의 항등원에서의 차원, 더 나아가 임의의 점에서의 차원이 $0$차원이 된다. 일반적으로 smooth projective curve의 유한개의 점을 고정하는 automorphism group은 finite type임이 알려져 있으므로, 이 사실로부터 $G$가 유한하다는 사실을 얻을 수 있다.

이제 만일 $h_i\geq2$이면 $\deg\mathcal{T}_{\widetilde{C}_i}=2-2h_i<0$이므로 global vector field가 없다. ([\[대수다양체\] §곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="pq7bu" }) 따라서 이 경우에는 special point가 없어도 automorphism group이 유한하다. 이는 낮은 genus에서는 일반적으로 성립하지 않는 논증으로, 여기에 special point들이 고정된다는 조건을 이용해 자유도를 줄여주어야 한다. 우선 $h_i=0$인 경우, $\widetilde{C}_i\cong\mathbb{P}^1$이고 $\mathcal{T}_{\mathbb{P}^1}(-D_i)\cong\mathcal{O}_{\mathbb{P}^1}(2-s_i)$이므로 위 공간의 dimension은 $\max\{3-s_i,0\}$이고, 따라서 $s_i$는 $3$ 이상이어야 한다. 직관적으로 이는 $\mathbb{P}^1$의 automorphism은 $(az+b)/(cz+d)$의 꼴이므로 $3$개의 자유도가 있는데, 이 자유도를 special point들이 하나씩 죽여주는 상황에 해당한다. $h_i=1$인 경우, tangent bundle은 trivial이 되어 global vector field의 공간은 dimension $1$이 되고, 이를 죽이기 위해서는 최소 하나의 special point가 필요하다. 

정리하면 automorphism group의 유한성은, 위와 같은 상황에서 

$$2g(\widetilde{C}_i)-2+s_i>0$$

이 성립하는 것과 같다. 즉 genus $0$에서는 special point가 적어도 $3$개, genus $1$에서는 적어도 $1$개가 필요하며, genus $2$ 이상에서는 추가조건이 없다. 이 조건은 오직 $\mu$가 constant로 죽이는 component $C_i$에만 해당되는 것으로, 만일 $\mu$가 $C_i$에서 nonconstant라면 이미 automorphism group이 $\mu$를 보존해야 한다는 사실로부터 유한성이 따라나온다.

Nonconstant component에서의 이 사실은 infinitesimal automorphism으로 보면 다음과 같다. $\widetilde{C}_i$ 위의 vector field $v$가 $\mu$를 보존하는 infinitesimal automorphism이라면, $v$를 따라 domain을 움직일 때 $\mu$가 받는 일차적인 변화, 곧 $\mu$의 differential을 $v$에 적용한 것이 $0$이어야 한다. 그런데 $\mu$가 $C_i$에서 nonconstant이면 이 differential은 $\widetilde{C}_i$의 dense open subset에서 injective이므로 $v$는 그 위에서 $0$이고, 따라서 $v=0$이다.

::: 예시 2
우리는 이제 automorphism group이 (non-trivial하게) 유한하게 나오는 경우를 실제로 살펴본다. $C$가 irreducible nodal cubic이고 $\mu:C\rightarrow X$가 constant map이라고 하자. $C$의 arithmetic genus는 $1$이지만 normalization은 $\mathbb{P}^1$이다. ([\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="0htg0" }) Node 위의 두 점을 $0,\infty$로 잡으면, marked point가 없을 때는 모든 $z\mapsto az$ ($a\in\mathbb{C}^{\times}$)가 이 두 점을 고정하고 $C$의 automorphism으로 내려간다. 따라서 이 map은 stable하지 않으며, 실제로 위의 부등식에 $h_i=0$, $s_i=2$를 대입해보아도 확인할 수 있다. 

이제 smooth locus에 marked point $p$ 하나를 고르고 그 preimage가 $1$이 되도록 좌표를 잡으면 $s_i=3$이 되어 이는 stability 조건을 만족한다. 단 여기서 주의할 것은 automorphism group이 trivial group이 아니라는 것이다. 즉 $0,1,\infty$를 각각 고정하는 automorphism은 항등사상 뿐이지만, 처음 normalization 단계에서 node의 두 branch를 서로 바꾸어줄 수 있는 자유도가 있으며, 실제로 $z\mapsto1/z$이 $0,\infty$를 맞바꾸고 $1$을 고정해주는 automorphism의 역할을 한다. 즉,

$$\Aut(C,p,\mu)\cong\mathbb{Z}/2$$

이다. 반면 같은 nodal cubic의 inclusion $C\hookrightarrow\mathbb{P}^2$는 map을 보존하는 automorphism이 항등사상뿐이므로 marked point가 없어도 stable하다.
:::

Stability는 이처럼 각 성분의 parametrization에 연속적인 자유도가 남는지를 판정한다. Contracted component에서는 special point가 그 자유도를 제한하고, nonconstant component에서는 map 자체가 이를 제한한다. Nodal cubic의 예처럼 유한한 대칭은 남을 수 있으며, 이 대칭까지 기록하는 것이 stable map의 moduli를 Deligne–Mumford stack으로 다루는 이유이다.

## 안정사상들의 모듈라이 공간

[예시 2](#ex2){: data-lid="nr248" }에서 보았듯, stable map은 비자명한 automorphism을 가질 수 있다. 따라서 stable map들을 모아둔 공간은 각 점이 나타내는 map의 automorphism까지 기억하는 stack으로 다룬다. Genus $g$, marked point의 개수 $n$, effective class $\beta$ (즉 $X$ 안의 irreducible curve들의 homology class를 음이 아닌 정수 계수로 합한 class)를 고정한 stable map들의 family와 그 사이의 isomorphism으로 이루어진 stack을

$$\overline{\mathcal{M}}_{g,n}(X,\beta)$$

로 적는다. 이 stack의 geometric point들의 isomorphism class는 stable map들의 isomorphism class에 대응하고, 각 점의 stabilizer는 해당 stable map의 automorphism group이 된다.

여기서 scheme $T$ 위의 stable map의 family는 [§마디 곡선의 변형, ⁋정의 8](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#def8){: data-lid="q3x42" }의 $T$ 위의 genus $g$, $n$개의 marked point를 갖는 prestable curve $(\pi:\mathcal{C}\rightarrow T,\sigma_1,\ldots,\sigma_n)$와 morphism $\mu:\mathcal{C}\rightarrow X$의 짝으로서, $T$의 각 geometric point $\bar{t}$ 위의 fiber $(\mathcal{C}_{\bar{t}},\sigma_1(\bar{t}),\ldots,\sigma_n(\bar{t}),\mu\vert_{\mathcal{C}_{\bar{t}}})$가 class $\beta$의 stable map인 것이다. 두 family $(\mathcal{C},\sigma_\bullet,\mu)$와 $(\mathcal{C}',\sigma'_\bullet,\mu')$ 사이의 isomorphism은 $\varphi\circ\sigma_i=\sigma'_i$, $\mu'\circ\varphi=\mu$를 만족하는 $T$-isomorphism $\varphi:\mathcal{C}\rightarrow\mathcal{C}'$이다.

::: 명제 3
$\beta$가 effective class이면 $\overline{\mathcal{M}}_{g,n}(X,\beta)$은 proper Deligne–Mumford stack이고 ([\[스택\] §대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6){: data-lid="r3t1v" }), 그 coarse moduli space는 projective scheme이다. ([\[스택\] §모듈라이 공간, ⁋정의 7](/ko/math/stacks/moduli_spaces#def7){: data-lid="d7w0d" })
:::

도입부에서 properness가 필요했던 이유는 주어진 조건을 움직일 때 곡선의 limit이 moduli 안에 남아 있어야 했기 때문이며, 위 명제는 $\overline{\mathcal{M}}_{g,n}(X,\beta)$이 그러한 조건을 만족하는 moduli space임을 보여준다. 예를 들어 도입부의 conic 계산에서 image가 둘로 갈라진다면, 우리는 그 domain도 두 개의 성분으로 나누어줄 수 있으므로 이는 더 이상 문제가 되지 않는다. 한편, 문제의 소지가 있는 limit은 이러한 상황에서만 일어나는 것은 아닌데, 가령 두 marked point들이 하나의 점으로 충돌하는 경우에도 그 극한은 순진한 방식으로는 $\overline{\mathcal{M}}_{g,n}(X,\beta)$ 안에 머물지 않는다. 이 경우 우리는 이 충돌지점에 $\mathbb{P}^1$ component를 붙이고, 충돌한 두 marked point를 이 component 위에 붙이는 방식으로 원래의 모습을 기억한다. 이 때 새로 생긴 $\mathbb{P}^1$ component는 $\mu$를 통해 충돌지점의 image $\mu(p)$로 옮겨지며, 이 component에는 node 하나와 두 marked point가 있으므로 stability condition은 여전히 만족된다. 

이는 엄밀하게는 곡선들이 이루는 family를 생각한 것으로 이해할 수 있다. 이를 위해 충돌지점 근처에서 국소적으로 매개변수 $\t$를 사용하여 곡선들의 family $C_\t$를 매개화하고, central fiber $\t=0$에서 두 marked point가 충돌한다 하자. 이 그림에서 곡선들의 family는 total space가 곡면인 $S\rightarrow \mathbb{A}^1_\t$으로, 각 marked point의 궤적은 이 projection의 두 section으로 나타나며, 따라서 두 marked point가 $\t=0$에서 충돌한다는 것은 이 section들이 $\t=0$에서 교점을 갖는다는 것으로 이해할 수 있다. 가령 각 fiber의 local coordinate를 $\z$라 하고 두 section을 $\z=0$, $\z=\t$로 잡으면 이 두 section은 $(\z,\t)=(0,0)$에서 교점을 가지게 된다. 이러한 상황에서 충돌을 풀어주는 표준적인 방법은 blowup으로, 위에서 붙여준 bubble $\mathbb{P}^1$은 바로 이 blowup의 exceptional curve이며, blowup의 coordinate $\u=\z/\t$에서 두 section의 strict transform은 $\u=0,\u=1$이 되어 이 component에서 서로 다른 두 marked point가 나타나게 되는 것이다. 우리의 예시에서는 두 section이 일차식으로 만났으므로 blowup이 한 번으로 끝났지만, 이들 section이 높은 차수로 만나는 경우에는 이들을 분리할 때까지 blowup을 반복해야 한다. 그러나 이 과정에서 중간에 생기는 component들은 stability를 만족하지 않게 되어 한 점으로 수축되므로, 최종적으로 나오는 그림은 위에서 설명한 그림과 동일하다.

이제 이 moduli stack $\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위에는 몇 가지 자연스러운 morphism들이 존재한다. 우선 각 marked point의 image를 읽는 *evaluation map*은

$$\ev_i:\overline{\mathcal{M}}_{g,n}(X,\beta)\rightarrow X,\qquad (C,p_\bullet,\mu)\mapsto\mu(p_i)$$

으로 정의되며, 그 의미 또한 명확하다. 일반적인 enumerative problem에서는 $i$번째 marked point가 주어진 subvariety를 지난다는 incidence condition을 부과할 때가 많은데, 이러한 경우 그 subvariety의 class를 $\ev_i$로 pullback해오면 된다. 

또 다른 morphism은 마지막 marked point를 잊는 *forgetful morphism*

$$\pi:\overline{\mathcal{M}}_{g,n+1}(X,\beta)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

으로, $\beta\neq 0$ 혹은 $2g-2+n>0$인 경우 항상 정의된다. Marked point의 개수는 stability를 통제하는 변수이므로, 단순히 마지막 marked point를 잊기만 한다면 그 결과는 stable map이 되지 않을 수 있는데, $\pi$는 이렇게 unstable해진 component를 점으로 수축시키는 stabilization 과정까지 포함하여 그 결과물이 stable map이 되도록 만들어준 morphism이며, 이를 위해 앞선 조건 $\beta\neq 0$ 또는 $2g-2+n>0$이라는 가정이 필요하다. 이렇게 정의한 $\pi$는 $\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위의 universal curve가 된다. ([\[스택\] §모듈라이 공간, §§모듈라이 함자](/ko/math/stacks/moduli_spaces#모듈라이-함자){: data-lid="r8e2o" }) 실제로, 편의상 stable map 하나, 즉 $\overline{\mathcal{M}}_{g,n}(X,\beta)$의 점 하나를 고정하고 이 위에서의 $\pi$의 fiber를 본다고 하면, 이 점에서 fiber로 가는 section을 정하는 것은 정확하게 마지막 marked point를 이 stable map의 어디에 찍는지와 같으며 따라서 이 점 위에서의 fiber가 그 stable map의 domain curve로 나오게 된다.

단, 새 점을 node나 이미 있는 marked point $p_i$ 위에 찍는 경우에는 그 점을 그대로 marked point로 쓸 수 없다. 이때는 앞에서 두 marked point가 충돌할 때 한 것처럼 그 자리에 $\mathbb{P}^1$ component를 하나 붙이고 새 marked point를 그 위에 둔다. $p_i$ 위에 찍은 경우에는 $p_i$와 새 점이 함께 이 component 위로 옮겨 가고, node 위에 찍은 경우에는 이 component가 node의 두 branch 사이에 끼어 들어가 양쪽과 각각 node를 이룬다. 어느 경우든 이 component는 $\mu$에 의해 한 점으로 가고 special point가 셋이므로 결과는 stable map이며, 새 점을 잊으면 special point가 둘만 남아 $\pi$가 이 component를 다시 수축하므로 원래의 stable map으로 돌아온다. 따라서 이러한 점까지 포함하면 $\pi$의 fiber의 점들은 여전히 $C$의 점들과 하나씩 대응한다.

마지막으로 $2g-2+n>0$이면 map 없이도 stable한 pointed curve로 안정화할 수 있다. 이 경우 $X$로 가는 map을 잊은 뒤, pointed curve로서 unstable한 성분들을 수축하여

$$\overline{\mathcal{M}}_{g,n}(X,\beta)\rightarrow\overline{\mathcal{M}}_{g,n},\qquad (C,p_\bullet,\mu)\mapsto(C,p_\bullet)^{\mathrm{stab}}$$

을 얻는다.

앞서 properness를 설명할 때, smooth domain을 갖는 stable map의 family가 nodal domain을 갖는 stable map으로 degenerate할 수 있으므로 이러한 limit도 moduli에 포함해야 함을 보았다. 이제 이러한 nodal domain을 갖는 locus를 *boundary*라 부르고, node에서 domain을 분리한 뒤 다시 붙이는 방식으로 기술한다. 우선 node 하나의 두 branch를 떼어냈을 때 curve가 두 개의 connected curve로 나뉘고 $\{1,\ldots,n\}=A\sqcup B$, $g=g_1+g_2$, $\beta=\beta_1+\beta_2$라면 gluing morphism은

$$\overline{\mathcal{M}}_{g_1,A\cup\{\bullet\}}(X,\beta_1)\times_X\overline{\mathcal{M}}_{g_2,B\cup\{\bullet\}}(X,\beta_2)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

이다. 두 factor에 새로 붙인 marked point $\bullet$의 evaluation이 같아야 하나의 node로 붙일 수 있으므로 fiber product가 $X$ 위에서 형성된다. 이때 source는 붙이기 전의 두 curve를 첫째와 둘째로 구별하지만, 붙인 결과는 그 순서를 기억하지 않는다. 따라서 두 factor의 genus, marking, class 자료가 같아 서로 맞바꿀 수 있는 경우에는 이 morphism이 그 image와 isomorphic하지 않을 수 있다. 또, node가 여러 개 있는 curve에서는 같은 분해 자료를 주는 node를 서로 다르게 선택할 수 있으며, 이 경우에도 서로 다른 gluing 자료가 같은 stable map을 줄 수 있다. 이것이 boundary의 서로 다른 국소 branch가 만나는 상황이다.

반대로 $A$와 $B$가 모두 공집합이 아니면 이 두 경우는 일어나지 않는다. 두 factor는 서로 다른 marked point들을 담으므로 맞바꿀 수 없다. 또 같은 분해 자료를 주는 서로 다른 두 node $x_1,x_2$가 있다면, $A$의 marked point 하나를 기준으로 보았을 때 $C$에서 두 node를 떼어 낸 세 조각 가운데 $x_1$과 $x_2$ 사이의 조각은 marked point를 담지 않고 genus와 class가 모두 $0$이어야 한다. 이 조각은 $\mu$가 한 점으로 보내는 $\mathbb{P}^1$들의 tree로서 나머지와는 $x_1$, $x_2$에서만 만나므로, component가 $k$개이면 그 special point는 모두 $2(k-1)+2=2k$개이고, 따라서 special point가 $2$개 이하인 component가 있어 stability에 어긋난다. 그러므로 이 경우 gluing morphism은 image 위에서 일대일이며, 실제로 그 image로의 isomorphism이다.

한편 node의 두 branch를 떼어내도 curve가 여전히 connected일 수 있다. [예시 2](#ex2){: data-lid="vz072" }의 irreducible nodal cubic이 바로 이런 경우로, node를 풀면 두 curve로 갈라지는 대신 하나의 $\mathbb{P}^1$ 위에 두 점 $0,\infty$가 나타난다. 일반적으로, 이 경우에는 node를 풀면 arithmetic genus가 하나 줄어들므로, 우리는 genus $g-1$의 connected curve 위에 두 marked point를 붙인다. 해당 gluing morphism은

$$\overline{\mathcal{M}}_{g-1,n+2}(X,\beta)\times_{X\times X}X\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

이고, $X\rightarrow X\times X$는 diagonal이다. 여기서도 source는 마지막 두 marked point의 순서를 구별하지만 붙인 결과는 이를 기억하지 않는다. 예시 2의 $z\mapsto1/z$은 이 두 점을 맞바꾸므로, 붙이기 전에는 각각의 marked point를 보존하는 automorphism이 아니지만 붙인 뒤에는 stable map의 automorphism이 된다. 

## Virtual dimension
{: #기대차원 }

$\overline{\mathcal{M}}_{g,n}(X,\beta)$은 일반적으로 매끄럽지 않으며, $g,n,\beta$를 고정해도 여러 irreducible component를 가질 수 있다. 뿐만 아니라 이러한 component들은 서로 만날 수도 있고, 각각의 차원도 다를 수 있다.

반면 stable map $(C,p_\bullet,\mu)$의 infinitesimal deformation space를 $T^1$, obstruction space를 $T^2$라 하면(이들은 map $\mu$까지 함께 움직이는 공간으로, domain만의 공간인 [§마디 곡선의 변형](/ko/math/gromov-witten_theory/deformations_of_nodal_curves){: data-lid="d37yd" }의 $T^0(C,p_\bullet)$, $T^1(C,p_\bullet)$과는 다르다), 이 deformation–obstruction theory는 *virtual dimension*

$$\vdim=\dim T^1-\dim T^2$$

을 정의한다. 직관적으로 $T^1$은 주어진 stable map이 moduli 안에서 일차적으로 움직일 수 있는 방향들을 담으므로 대략적으로는 tangent space와 같은 것이지만, 문제는 일차적으로 가능해보이는 움직임들이 실제 family로 이어진다는 보장이 없다는 것에 있다. 이러한 연장의 obstruction은 $T^2$의 원소이므로, 만일 $T^1$의 좌표들을 변수로 생각한다면, obstruction의 소멸은 이 변수들 위에 $T^2$에 값을 갖는 방정식을 부과하는 것으로 이해할 수 있다. Virtual dimension은 이렇게 변수의 수에서 방정식의 수를 뺀 값이다. 각 방정식은 dimension을 최대 $1$만큼 낮추므로 actual dimension은 virtual dimension 이상이며, 방정식들이 독립적으로 작용하지 않으면 더 클 수 있다.

이를 실제로 계산하려면 우선 $\mu:C\rightarrow X$가 정의하는 자연스러운 사상 $\mu^\ast\Omega_X\rightarrow\Omega_C$을 생각한다. 이 사상의 dual은 domain의 vector field $v$를 map의 infinitesimal variation $\dd{\mu}(v)$로 보내는 것으로, 이는 domain의 infinitesimal reparametrization이 map에 유도하는 일차적인 변화이다. 즉 $v$에 대응하는 infinitesimal automorphism을 $\varphi_\epsilon$이라 하면, $\mu\circ\varphi_\epsilon$의 일차적인 변화가 $\dd{\mu}(v)$이다. Stable map을 볼 때는 여기에 marked point들을 반영해야 하므로, 여기에 $\Omega_C\rightarrow\Omega_C(p_1+\cdots+p_n)$을 합성한다. 이 때

$$\Hom_C(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$$

는 marked point에서 사라지는 derivation을 담으므로, marked point를 고정하는 domain의 infinitesimal automorphism을 기록한다. 이렇게 얻은 two-term complex를

$$\LL_\mu=\Bigl[\at{-1}{\mu^\ast\Omega_X}\longrightarrow\at{0}{\Omega_C(p_1+\cdots+p_n)}\Bigr]$$

로 적는다. 직관적으로 이는 $\mu:C\rightarrow X$의 relative cotangent complex를 나타내는 two-term model에서 domain 쪽 항에 marked point의 twist를 넣은 것으로, deformation theory의 표준적인 해석에 의해 $X$를 고정하고 pointed domain과 map을 함께 변형하는 문제에서는

$$T^i=H^i\bigl(R\Hom_C(\LL_\mu,\mathcal{O}_C)\bigr)=\Ext_C^i(\LL_\mu,\mathcal{O}_C)$$

가 deformation space $T^1$과 obstruction space $T^2$를 준다. 이를 통해 다음 exact sequence를 얻는다.

::: 명제 4
Stable map $(C,p_\bullet,\mu)$의 deformation space $T^1$과 obstruction space $T^2$은 exact sequence

$$\begin{aligned}
0&\rightarrow\Ext_C^0\left(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C\right)\rightarrow H^0(C,\mu^\ast T_X)\rightarrow T^1 \\
&\rightarrow\Ext_C^1\left(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C\right)\rightarrow H^1(C,\mu^\ast T_X)\rightarrow T^2\rightarrow0
\end{aligned}$$

에 들어간다. 따라서 $\overline{\mathcal{M}}_{g,n}(X,\beta)$의 virtual dimension은

$$\vdim=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

이다.
:::

이 때, 첫 번째 $\Ext^0$은 pointed domain의 infinitesimal automorphism, $H^0(C,\mu^\ast T_X)$은 domain을 고정한 map의 deformation이다. 다음 $\Ext^1$은 pointed domain의 deformation이고, $H^1(C,\mu^\ast T_X)$에서 map의 local deformation들을 붙일 때 생기는 obstruction을 읽는다.

이 가운데 pointed domain의 deformation을 $H^1(C,\mu^\ast T_X)$로 보내는 map은 다음과 같이 읽는다. Pointed domain의 first-order deformation $C_\epsilon$이 주어졌다 하고, $C$를 affine open $U_\alpha$들로 덮자. 각 $U_\alpha$는 $C_\epsilon$ 안의 affine open $U_{\alpha,\epsilon}$의 square-zero closed subscheme이고 $X$는 smooth하므로, [\[스킴\] §매끄러운 사상과 에탈 사상, ⁋정리 15](/ko/math/scheme_theory/smooth_and_etale_morphisms#thm15){: data-lid="l5en5" }에 의하여 $\mu\vert_{U_\alpha}$를 $U_{\alpha,\epsilon}\rightarrow X$로 연장할 수 있다. 이는 node를 펴는 deformation처럼 $C_\epsilon$이 국소적으로도 trivial하지 않은 경우에도 성립한다. 두 연장은 $U_\alpha\cap U_\beta$ 위에서 같은 map $\mu$의 연장이므로 그 차는 $U_\alpha\cap U_\beta$ 위의 $\mu^\ast T_X$의 section이고, 이들은 Čech $1$-cocycle을 이루어 $H^1(C,\mu^\ast T_X)$의 원소를 준다. 연장을 바꾸면 이 cocycle은 coboundary만큼 바뀌며, 이 원소가 $0$인 것은 국소적인 연장들을 고쳐 $C_\epsilon$ 전체 위의 map으로 붙일 수 있다는 것과 같다. 즉 이 원소는 domain의 deformation을 따라 map을 연장하는 것에 대한 obstruction이며, $T^2$는 $H^1(C,\mu^\ast T_X)$를 이러한 원소들로 나눈 quotient이다.

::: 증명
위에서 정의한 $\LL_\mu$에 $R\Hom_C(-,\mathcal{O}_C)$를 적용하면 위 exact sequence가 나온다. 첫 morphism의 kernel은 pointed domain의 infinitesimal automorphism 중 map까지 보존하는 것들로, stability에 의해 이 kernel이 $0$이므로 sequence의 왼쪽에 $0$이 붙는다.

또 [§마디 곡선의 변형, §§준안정 곡선의 변형](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#준안정-곡선의-변형){: data-lid="qitvx" }에서 본 것처럼 $\Ext^i_C(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$는 pointed domain의 $T^i(C,p_\bullet)$이다. 위의 long exact sequence는 $T^2$ 다음에 $\Ext^2_C(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$로 이어지는데, [§마디 곡선의 변형, ⁋명제 7](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#prop7){: data-lid="zlpds" }에 의하여 이 공간은 $0$이므로 sequence의 오른쪽 끝에도 $0$이 붙는다. 즉 pointed domain의 deformation에는 obstruction이 없고, stable map의 obstruction은 모두 $H^1(C,\mu^\ast T_X)$에서 온다.

이제 $E=\mu^\ast T_X$, $A^i=\Ext_C^i(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$로 적자. 위 exact sequence에서 차원의 교대합은 $0$이므로

$$\dim T^1-\dim T^2=\bigl(\dim A^1-\dim A^0\bigr)+\rchi(C,E)$$

로 분리된다. 이 때 첫 괄호는 pointed domain의 deformation space와 infinitesimal automorphism space의 차원이므로, [§마디 곡선의 변형, ⁋따름정리 6](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#cor6){: data-lid="5ao1g" }에 의하여 $3g-3+n$이다.

둘째 항의 경우, 우선 smooth projective curve $Y$ 위의 rank $\ell$ vector bundle $F$에 대하여, [\[대수다양체\] §곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="ol72u" }의 vector bundle 버전은

$$\rchi(Y,F)=\deg F+\ell(1-g(Y))$$

을 준다. 

우리의 domain $C$는 smooth curve는 아니지만, normalization $\nu:\widetilde{C}=\coprod_{j=1}^c\widetilde{C}_j\rightarrow C$을 통해 이 계산을 옮겨줄 수 있다. 각 $\widetilde{C}_j$의 genus를 $h_j$, node의 개수를 $\delta$, $E$의 rank를 $\ell$이라 하자. Structure sheaf의 normalization exact sequence ([§마디 곡선의 변형, ⁋정의 1](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#def1){: data-lid="uihgw" } 직후)에 locally free sheaf $E$를 tensor하면

$$0\rightarrow E\rightarrow\nu_\ast\nu^\ast E\rightarrow\bigoplus_{q\in\Sing C}E\otimes_{\mathcal{O}_C}\kappa(q)\rightarrow0$$

을 얻는다. 이제 이를 사용하면

$$\rchi(C,E)=\sum_{j=1}^c\rchi(\widetilde{C}_j,\nu^\ast E\vert_{\widetilde{C}_j})-\ell\delta=\sum_{j=1}^c\left(\deg(\nu^\ast E\vert_{\widetilde{C}_j})+\ell(1-h_j)\right)-\ell\delta=\deg E+\ell\left(c-\sum_{j=1}^c h_j-\delta\right)=\deg E+\ell(1-g)$$

이고, 이 식에 $E=\mu^\ast T_X$를 대입하면 $\rank E=\dim X$이고, $\mu_\ast[C]=\beta$이므로 

$$\deg E=\int_C\mu^\ast c_1(T_X)=\int_\beta c_1(T_X)$$

이다. 

이제 마지막으로 이 계산들을 모두 합하면

$$\dim T^1-\dim T^2=(3g-3+n)+\int_\beta c_1(T_X)+\dim X(1-g)=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

을 얻는다.
:::

[명제 4](#prop4){: data-lid="yrgmr" }의 $T^1$과 $T^2$는 virtual dimension을 정의할 때 본 국소적인 그림을 다음과 같이 정확한 진술로 만든다. $\overline{\mathcal{M}}_{g,n}(X,\beta)$의 étale atlas $W$ 위의 점 $w$가 stable map $(C,p_\bullet,\mu)$를 나타낸다 하자. [명제 4](#prop4){: data-lid="rad08" }의 증명에서 본 것처럼 stable map에는 infinitesimal automorphism이 없으므로 $w$에서 $W$의 Zariski tangent space는 $T^1$이고, $N=\dim T^1$이라 하면 $w$에서의 complete local ring은

$$\widehat{\mathcal{O}}_{W,w}\cong\mathbb{C}[[\x_1,\ldots,\x_N]]/(f_1,\ldots,f_m),\qquad m\leq\dim T^2$$

의 꼴로 쓸 수 있다. 여기서 각 $f_j$는 $(\x_1,\ldots,\x_N)^2$에 속하며, 이들이 $T^1$의 좌표 위에 부과되는 방정식이다. 따라서 $w$를 지나는 $W$의 irreducible component는 모두 dimension이 $N-m$ 이상이고, 특히 $\vdim=\dim T^1-\dim T^2$ 이상이다. 또 $T^2=0$이면 $\widehat{\mathcal{O}}_{W,w}$는 power series ring이므로 $\overline{\mathcal{M}}_{g,n}(X,\beta)$는 이 점 근방에서 dimension $\dim T^1$의 smooth stack이다. $T^2\neq0$이더라도 $w$에서 $W$의 dimension이 $\dim T^1$과 같으면 $\widehat{\mathcal{O}}_{W,w}$는 dimension과 tangent space의 dimension이 같은 regular local ring이므로 $W$는 $w$에서 smooth하다.

## 예시

위에서 언급한 것처럼, virtual dimension은 actual dimension보다 항상 작거나 같다. Virtual dimension이 actual dimension이 되는 대표적인 경우는 target $X$가 convex일 때 genus $0$ stable map이다. 여기서 smooth projective variety $X$가 *convex<sub>볼록</sub>*하다는 것은 모든 morphism $\mu:\mathbb{P}^1\rightarrow X$에 대하여 $H^1(\mathbb{P}^1,\mu^\ast T_X)=0$이라는 것이다.

::: 명제 5
$X$가 convex이면 임의의 effective $\beta$와 $n\geq0$에 대하여 $\overline{\mathcal{M}}_{0,n}(X,\beta)$은 dimension

$$\int_\beta c_1(T_X)+\dim X-3+n$$

의 smooth proper Deligne–Mumford stack이다.
:::

Convexity는 smooth $\mathbb{P}^1$ 위의 조건이지만 nodal genus $0$ curve에서도 $H^1(C,\mu^\ast T_X)=0$임을 보일 수 있다. 따라서 [명제 4](#prop4){: data-lid="qh7wb" }에 의해 $T^2=0$이 성립함을 알 수 있다. 이러한 convex target의 대표적인 예시는 homogeneous space $G/P$로, 이 경우 $T_{G/P}$가 globally generated이므로 convexity가 성립한다.

::: 증명 (명제 5)
[명제 3](#prop3){: data-lid="ytyi8" }에 의하여 $\overline{\mathcal{M}}_{0,n}(X,\beta)$이 proper Deligne–Mumford stack이라는 것은 이미 알고 있으므로, 각 점 $(C,p_\bullet,\mu)$에서 $H^1(C,\mu^\ast T_X)=0$임을 보이면 된다.

우선 genus $0$ prestable curve $C$의 모양을 보자. $C$의 irreducible component의 개수를 $c$, node의 개수를 $d$, normalization의 각 성분의 genus를 $h_1,\ldots,h_c$라 하면 [§마디 곡선의 변형, ⁋명제 2](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#prop2){: data-lid="76c0a" }에 의하여

$$0=\sum_{j=1}^ch_j+(d-c+1)$$

이다. Component들을 꼭짓점으로, node들을 변으로 하는 graph를 $C$의 *dual graph*라 하자. $C$가 connected이므로 dual graph도 connected이고, 따라서 $c-1$개의 변으로 이루어진 spanning tree를 가지므로 $d\geq c-1$이며 등호는 dual graph 자체가 tree일 때뿐이다. 그러므로 모든 $h_j$가 $0$이고 dual graph는 tree이다. 특히 self-node는 dual graph의 loop가 되므로 존재하지 않고, $C$의 각 component는 $\mathbb{P}^1$이다.

이제 component $C_0\cong\mathbb{P}^1$ 하나를 고르자. $\mathbb{P}^1$ 위의 vector bundle은 line bundle들의 direct sum으로 쪼개지므로

$$\mu^\ast T_X\vert_{C_0}\cong\bigoplus_{i=1}^{\dim X}\mathcal{O}_{\mathbb{P}^1}(a_i)$$

로 쓸 수 있다. 우리는 모든 $a_i$가 $0$ 이상임을 보인다. $\mathbb{P}^1$ 위에서 $H^1(\mathbb{P}^1,\mathcal{O}(m))$은 $m\geq-1$이면 $0$이고 $m\leq-2$이면 $0$이 아니다. $\mu\vert_{C_0}$ 자체도 morphism $\mathbb{P}^1\rightarrow X$이므로 convexity에 의하여 $H^1(\mathbb{P}^1,\mu^\ast T_X\vert_{C_0})=0$이지만, 이로부터 얻는 것은 $a_i\geq-1$뿐이다. 대신 degree $2$의 morphism, 즉 double cover $\varphi:\mathbb{P}^1\rightarrow C_0$을 합성한 $\mu\vert_{C_0}\circ\varphi:\mathbb{P}^1\rightarrow X$에 convexity를 적용하면, $\varphi^\ast\mathcal{O}(a_i)\cong\mathcal{O}(2a_i)$이므로 모든 $i$에 대하여 $H^1(\mathbb{P}^1,\mathcal{O}(2a_i))=0$, 즉 $2a_i\geq-1$이다. 따라서 모든 $a_i$는 $0$ 이상이다.

다음으로 $C$의 임의의 smooth point $p$에 대하여

$$H^1\bigl(C,\mu^\ast T_X\otimes\mathcal{O}_C(-p)\bigr)=0\tag{$\ast$}$$

임을 component의 개수에 대한 induction으로 보이자. $C\cong\mathbb{P}^1$이면 $\mu^\ast T_X\otimes\mathcal{O}_C(-p)\cong\bigoplus_i\mathcal{O}(a_i-1)$이고 $a_i-1\geq-1$이므로 ($\ast$)가 성립한다. Component가 둘 이상이면 $p$가 놓인 component를 $C_0$, 나머지 component들의 합집합을 $C'$이라 하자. Dual graph가 tree이므로 $C'$은 connected component $C'_1,\ldots,C'_k$로 나뉘고, 각 $C'_j$는 $C_0$와 한 node $p'_j$에서만 만난다. 각 $C'_j$는 다시 genus $0$의 connected nodal curve로서 component의 개수가 $C$보다 적고, $p'_j$는 $C'_j$의 smooth point이다. 한편 node $p'_j$ 근방에서 $C$를 $\x\y=0$, $C_0$를 $\y=0$, $C'_j$를 $\x=0$으로 두면 restriction $\mathcal{O}_C\rightarrow\mathcal{O}_{C_0}$의 kernel은 ideal $(\y)$이고, $\x\y=0$이므로 이는 $C'_j$ 위에서 $p'_j$의 ideal과 같다. 따라서 short exact sequence

$$0\rightarrow\mathcal{O}_{C'}(-p'_1-\cdots-p'_k)\rightarrow\mathcal{O}_C\rightarrow\mathcal{O}_{C_0}\rightarrow0$$

이 존재하고, $p\notin C'$이므로 여기에 locally free sheaf $\mu^\ast T_X\otimes\mathcal{O}_C(-p)$를 tensor하면

$$0\rightarrow\mu^\ast T_X\vert_{C'}\otimes\mathcal{O}_{C'}(-p'_1-\cdots-p'_k)\rightarrow\mu^\ast T_X\otimes\mathcal{O}_C(-p)\rightarrow\mu^\ast T_X\vert_{C_0}\otimes\mathcal{O}_{C_0}(-p)\rightarrow0$$

을 얻는다. 왼쪽 항의 $H^1$은 각 $C'_j$와 $p'_j$에 대한 induction 가정에 의하여 $0$이고, 오른쪽 항의 $H^1$은 $\bigoplus_iH^1(\mathbb{P}^1,\mathcal{O}(a_i-1))=0$이므로, cohomology long exact sequence에서 가운데 항의 $H^1$도 $0$이다.

이제 $H^1(C,\mu^\ast T_X)=0$을 보이자. $C\cong\mathbb{P}^1$이면 모든 $a_i\geq0$이므로 바로 성립한다. Component가 둘 이상이면 아무 component $C_0$를 골라 위와 같이 $C'$과 $p'_j$를 잡고, 같은 short exact sequence에 $\mu^\ast T_X$를 tensor하면

$$0\rightarrow\mu^\ast T_X\vert_{C'}\otimes\mathcal{O}_{C'}(-p'_1-\cdots-p'_k)\rightarrow\mu^\ast T_X\rightarrow\mu^\ast T_X\vert_{C_0}\rightarrow0$$

이다. 왼쪽 항의 $H^1$은 각 $C'_j$와 그 smooth point $p'_j$에 ($\ast$)를 적용하면 $0$이고, 오른쪽 항의 $H^1$은 $\bigoplus_iH^1(\mathbb{P}^1,\mathcal{O}(a_i))=0$이므로 $H^1(C,\mu^\ast T_X)=0$이다.

따라서 [명제 4](#prop4){: data-lid="okl51" }의 exact sequence에서 $H^1(C,\mu^\ast T_X)$의 quotient인 $T^2$도 $0$이다. 그럼 virtual dimension을 정의할 때 본 국소적인 그림에서 $T^1$의 좌표 위에 부과되는 방정식이 하나도 없으므로, 각 점 근방에서 $\overline{\mathcal{M}}_{0,n}(X,\beta)$는 dimension $\dim T^1$의 smooth stack이고 [명제 4](#prop4){: data-lid="21e38" }에 의하여 $\dim T^1=\vdim$이다.
:::

[명제 5](#prop5){: data-lid="pit6k" }의 증명에서 $a_i\geq0$을 얻을 때 $\mu\vert_{C_0}$ 대신 double cover를 합성한 map에 convexity를 적용한 것은 꼭 필요한 걸음이다. 다음 예시의 target에서는 tangent bundle을 pullback했을 때의 음의 degree가 degree $1$의 map에서는 $H^1$에 나타나지 않다가 double cover에서 드러나며, 그 결과 obstruction space가 모든 점에서 사라지지 않아 actual dimension이 virtual dimension보다 커진다.

::: 예시 6
$S\subset\mathbb{P}^3$를 smooth cubic surface, $L\subset S$를 그 위의 line이라 하자. Adjunction에 의하여 canonical bundle은 $\omega_S\cong\mathcal{O}_S(-1)$이므로 $K_S\cdot L=-1$, $c_1(T_S)\cdot L=1$이고, $L\cong\mathbb{P}^1$에 다시 adjunction을 적용하면 $-2=L^2+K_S\cdot L$에서 $L^2=-1$이다. 따라서 $N_{L/S}\cong\mathcal{O}_L(-1)$이고, exact sequence $0\rightarrow T_L\rightarrow T_S\vert_L\rightarrow N_{L/S}\rightarrow0$은 $\Ext^1_L(\mathcal{O}_L(-1),\mathcal{O}_L(2))\cong H^1(L,\mathcal{O}_L(3))=0$이므로 split하여

$$T_S\vert_L\cong\mathcal{O}_L(2)\oplus\mathcal{O}_L(-1)$$

이다. 그러므로 isomorphism $\mu:\mathbb{P}^1\rightarrow L$에 대해서는 $H^1(\mathbb{P}^1,\mu^\ast T_S)=0$이지만, degree $2$의 map $\mu:\mathbb{P}^1\rightarrow L$에 대해서는 $\mu^\ast T_S\cong\mathcal{O}(4)\oplus\mathcal{O}(-2)$이므로 $H^1(\mathbb{P}^1,\mu^\ast T_S)$는 $1$차원이다. 즉 $S$는 convex가 아니고, 이는 degree $1$의 map만 보아서는 드러나지 않는다.

이제 $g=0$, $n=0$, $\beta=2[L]$로 두면 [명제 4](#prop4){: data-lid="51krk" }에 의하여

$$\vdim=\int_{2[L]}c_1(T_S)+(2-3)=2-1=1$$

이다. 한편 stable map $(C,\mu)$에 대하여 $Z=\mu_\ast[C]$는 class $2[L]$을 갖는 effective cycle이고 $Z\cdot L=2L^2=-2<0$이므로 $L$을 성분으로 갖는다. $Z=aL+Z'$ ($a\geq1$이고 $Z'$은 $L$을 성분으로 갖지 않는 effective cycle)로 쓰면 $0\leq Z'\cdot L=-2+a$에서 $a\geq2$이고, hyperplane class $H$와의 intersection number를 비교한 $2=H\cdot Z=a+H\cdot Z'$에서 $a=2$, $Z'=0$이다. 따라서 $\mu$의 image는 $L$이고, $C$가 reduced이므로 $\mu$는 $L$을 거쳐 간다. 또 $n=0$이므로 contracted component는 node를 셋 이상 가져야 하는데, dual graph가 tree이므로 그 node들에서 갈라지는 가지들 각각의 끝에는 node가 하나뿐인 component, 즉 contracted가 아닌 component가 있어야 하고 그러면 degree가 $3$ 이상이 된다. 그러므로 $C$는 $\mathbb{P}^1$ 하나가 $L$을 degree $2$로 덮는 것이거나, 두 $\mathbb{P}^1$이 한 점에서 만나고 각각이 $L$로 isomorphic하게 가는 것이다.

이들은 정확히 $\overline{\mathcal{M}}_{0,0}(L,2)\cong\overline{\mathcal{M}}_{0,0}(\mathbb{P}^1,2)$의 점들이다. $T_{\mathbb{P}^1}=\mathcal{O}(2)$를 degree $e$의 map으로 pullback하면 $\mathcal{O}(2e)$이므로 $\mathbb{P}^1$은 convex이고, [명제 5](#prop5){: data-lid="myulu" }에 의하여 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^1,2)$는 dimension $4+1-3=2$의 smooth stack이다. 따라서 $\overline{\mathcal{M}}_{0,0}(S,2[L])$는 $L$을 거쳐 가는 map들의 closed substack $\overline{\mathcal{M}}_{0,0}(L,2)$와 같은 점들을 가지므로 모든 점에서 dimension이 $2$이다.

이 $2$차원은 map들을 직접 매개화하여 볼 수도 있다. Degree $2$의 map $\mathbb{P}^1\rightarrow L$은 서로 다른 두 점에서 branch하며, branch point가 같은 두 degree $2$ map은 domain의 isomorphism으로 서로 옮겨지므로 이러한 map은 isomorphism을 법으로 branch divisor로 정해진다. 두 branch point가 한 점 $x\in L$로 모이면 domain이 두 $\mathbb{P}^1$으로 갈라져, 각 성분이 $L$로 isomorphic하게 가고 node가 $x$로 가는 위의 둘째 경우의 map이 극한으로 나타난다. 따라서 $\overline{\mathcal{M}}_{0,0}(L,2)$의 점들은 $L$ 위의 degree $2$ effective divisor들, 곧 $\Sym^2L\cong\mathbb{P}^2$의 점들과 일대일로 대응하며, 대각선 위의 점들이 nodal domain에 해당한다. 또 모든 점이 order $2$의 automorphism을 갖는다. 첫째 경우에는 두 sheet를 맞바꾸는 deck involution이, 둘째 경우에는 두 성분을 맞바꾸는 involution이 map을 보존한다. 그러므로 이 map들의 image는 모두 같은 cycle $2L$이지만 $\overline{\mathcal{M}}_{0,0}(L,2)$에서는 $2$차원에 걸친 서로 다른 점들이고, 각 점의 stabilizer는 $\mathbb{Z}/2$이다. Stack으로도 같은 매개화를 쓸 수 있다. $L$의 homogeneous coordinate $[\u:\v]$에 대한 $0$이 아닌 quadratic form $q$마다 line bundle $\mathcal{O}_L(1)$의 total space 안의 곡선 $\w^2=q(\u,\v)$와 $L$로의 projection이 degree $2$의 stable map을 주고, $q$가 double root를 가져 $q=\ell^2$이면 이 곡선은 두 section $\w=\pm\ell(\u,\v)$가 한 점에서 만나는 nodal curve이다. $\w$를 $\lambda\w$로 바꾸면 $q$가 $\lambda^2q$로 바뀌므로, $\overline{\mathcal{M}}_{0,0}(L,2)$는 $0$이 아닌 quadratic form들의 공간 $\mathbb{C}^3\setminus\{0\}$을 weight $2$로 작용하는 $\mathbb{G}_m$으로 나눈 quotient stack, 곧 weighted projective stack $\mathbb{P}(2,2,2)$이며, 위의 stabilizer $\mathbb{Z}/2$는 $\lambda^2=1$인 $\lambda$들이다.

이제 각 점에서 $T^1$과 $T^2$를 계산하자. $\mu$가 $L$을 거쳐 가므로 $L$ 위의 exact sequence $0\rightarrow T_L\rightarrow T_S\vert_L\rightarrow N_{L/S}\rightarrow0$을 $\mu$로 pullback할 수 있고, $L\cong\mathbb{P}^1$은 convex이므로 [명제 5](#prop5){: data-lid="dj5mk" }의 증명에 의하여 $H^1(C,\mu^\ast T_L)=0$이다. 따라서 cohomology long exact sequence에서 $H^1(C,\mu^\ast T_S)\cong H^1(C,\mu^\ast N_{L/S})$이다. 위의 두 경우 모두 line bundle $\mu^\ast N_{L/S}$는 $C$의 각 component 위에서 음의 degree를 가지므로 global section이 없고, [명제 4](#prop4){: data-lid="38ui0" }의 증명에서 얻은 식에 의하여 $\rchi(C,\mu^\ast N_{L/S})=\deg\mu^\ast N_{L/S}+1=-1$이다. 즉 $H^1(C,\mu^\ast T_S)$는 모든 점에서 $1$차원이다.

[명제 4](#prop4){: data-lid="44m01" }의 exact sequence에서 $T^2$는 이 공간의 quotient이므로 $\dim T^2\leq1$이다. 한편 $T^1$은 이 점에서의 tangent space이므로 그 dimension은 이 점에서의 dimension $2$ 이상이고, $\dim T^1-\dim T^2=\vdim=1$이므로 $\dim T^1=2$, $\dim T^2=1$일 수밖에 없다. 그러므로 $\overline{\mathcal{M}}_{0,0}(S,2[L])$는 모든 점에서 tangent space의 dimension이 실제 dimension과 같아 dimension $2$의 smooth stack이고, 따라서 $\overline{\mathcal{M}}_{0,0}(L,2)$와 같다. 또 obstruction space $T^2\cong H^1(C,\mu^\ast N_{L/S})$들은 universal curve $\pi:\overline{\mathcal{M}}_{0,1}(L,2)\rightarrow\overline{\mathcal{M}}_{0,0}(L,2)$와 $\ev_1:\overline{\mathcal{M}}_{0,1}(L,2)\rightarrow L$에 대하여 rank $1$의 vector bundle

$$R^1\pi_\ast\ev_1^\ast N_{L/S}$$

을 이룬다.
:::

이 예시에서 $\overline{\mathcal{M}}_{0,0}(S,2[L])$는 smooth하지만 그 dimension $2$는 virtual dimension $1$보다 크고, 그 차이는 모든 점에서 $1$차원인 obstruction space의 dimension과 같다. Virtual dimension을 정의할 때의 그림으로 말하면, 각 점에서 $2$차원의 $T^1$ 위에 $T^2$에 값을 갖는 방정식 하나가 부과되지만 이 방정식이 항등적으로 $0$이어서 dimension을 전혀 낮추지 못한 것이다. 반면 convex target의 genus $0$ stable map에서는 [명제 5](#prop5){: data-lid="rkqqz" }에 의하여 이러한 일이 일어나지 않으며, 다음은 그 가장 간단한 경우이다.

::: 예시 7
$X=\mathbb{P}^r$, $g=0$, $n=0$, $\beta=[\text{line}]$이라 하자. Degree $1$ stable map은 $\mathbb{P}^1$을 $\mathbb{P}^r$ 안의 직선으로 isomorphic하게 보내며, parametrization의 자유도는 $\Aut(\mathbb{P}^1)$이 흡수한다. 따라서 남는 자료는 직선 자체이고

$$\overline{\mathcal{M}}_{0,0}(\mathbb{P}^r,1)\cong\Gr(2,r+1)$$

이다. 이 Grassmannian의 dimension은 $2(r+1-2)=2r-2$인데, $c_1(T_{\mathbb{P}^r})=(r+1)H$이므로 virtual dimension 또한

$$\vdim=(r+1)+(r-3)=2r-2$$

가 되어 두 값이 일치하는 것을 확인할 수 있다.
:::

같은 계산을 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^2,2)$에 적용하면

$$\vdim=\int_{2[\text{line}]}c_1(T_{\mathbb{P}^2})+(2-3)=6-1=5$$

이다. $\mathbb{P}^2$은 convex이므로 이 값은 actual dimension과 일치한다.

끝으로 convex target으로 가는 genus $0$ stable map들의 moduli에서 boundary의 모양을 보자. 우선 $\mu^\ast T_X$는 $C$ 위에서 global section들로 생성된다. 실제로 $C$의 각 component $C_0$에 대하여 restriction $H^0(C,\mu^\ast T_X)\rightarrow H^0(C_0,\mu^\ast T_X\vert_{C_0})$는 surjective이다. Component가 하나뿐이면 당연하고, 둘 이상이면 [명제 5](#prop5){: data-lid="u79og" }의 증명의 마지막 short exact sequence에서 왼쪽 항의 $H^1$이 $0$이기 때문이다. 한편 [명제 5](#prop5){: data-lid="4w2te" }의 증명에서 본 것처럼 $a_i\geq0$이므로 $\mu^\ast T_X\vert_{C_0}\cong\bigoplus_i\mathcal{O}(a_i)$는 global section들로 생성되고, $C$의 모든 점은 어떤 component 위에 있다. 특히 marked point $p_i$에서 값을 취하는 map $H^0(C,\mu^\ast T_X)\rightarrow T_{\mu(p_i)}X$는 surjective이다. 이 map은 domain을 고정하고 map만 움직이는 deformation이 $\ev_i$의 값에 주는 일차적인 변화이므로 $\ev_i$의 differential은 모든 점에서 surjective이고, [명제 5](#prop5){: data-lid="bxw07" }에 의하여 $\overline{\mathcal{M}}_{0,n}(X,\beta)$가 smooth하므로 $\ev_i$는 smooth morphism이다. 따라서 gluing morphism의 source

$$\overline{\mathcal{M}}_{0,A\cup\{\bullet\}}(X,\beta_1)\times_X\overline{\mathcal{M}}_{0,B\cup\{\bullet\}}(X,\beta_2)$$

는 dimension

$$\vdim\overline{\mathcal{M}}_{0,A\cup\{\bullet\}}(X,\beta_1)+\vdim\overline{\mathcal{M}}_{0,B\cup\{\bullet\}}(X,\beta_2)-\dim X=\vdim\overline{\mathcal{M}}_{0,n}(X,\beta)-1$$

의 smooth stack이다.

또 [명제 4](#prop4){: data-lid="w3px3" }의 exact sequence에서 $H^1(C,\mu^\ast T_X)=0$이므로, stable map의 deformation을 pointed domain의 deformation으로 보내는 $T^1\rightarrow T^1(C,p_\bullet)$은 surjective이다. 이를 [§마디 곡선의 변형, ⁋정리 5](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#thm5){: data-lid="u4t65" }의 오른쪽 map, 곧 각 node 근방의 local deformation으로의 restriction과 합성한

$$T^1\longrightarrow\bigoplus_{q\in\Sing C}T_q^1$$

도 surjective이다. 즉 stable map을 일차적으로 움직여 domain의 node들을 서로 독립적으로 펼 수 있다. 이를 앞에서 본 complete local ring으로 옮기자. $(C,p_\bullet,\mu)$를 나타내는 점 $w\in W$에서 $W$ 위의 universal curve는 $(C,p_\bullet)$의 versal base $R$ 위의 versal family를 어떤 local homomorphism $R\rightarrow\widehat{\mathcal{O}}_{W,w}$로 당긴 것이다. 이 homomorphism이 [§마디 곡선의 변형, ⁋명제 10](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#prop10){: data-lid="qg02e" }의 smoothing parameter $\t_q$를 보내는 원소를 다시 $\t_q$로 적으면, node $q$에서 이 family의 complete local ring은 $\widehat{\mathcal{O}}_{W,w}[[\u_q,\v_q]]/(\u_q\v_q-\t_q)$이므로 node $q$가 node로 남는 locus는 $\t_q=0$이다. 위의 surjectivity는 이 $\t_q$들의 class가 $\widehat{\mathcal{O}}_{W,w}$의 cotangent space에서 linearly independent하다는 것과 같으므로, 앞의 꼴 $\mathbb{C}[[\x_1,\ldots,\x_N]]/(f_1,\ldots,f_m)$에서 $\t_q$들을 변수의 일부로 택할 수 있다. 이 걸음은 surjectivity만 쓰므로, convex가 아닌 target에서도 node들의 집합 $S\subseteq\Sing C$에 대하여 $T^1\rightarrow\bigoplus_{q\in S}T_q^1$가 surjective이면 $\t_q$ ($q\in S$)들을 변수의 일부로 택할 수 있다. 지금은 $T^2=0$이므로 $\widehat{\mathcal{O}}_{W,w}$는 power series ring이고, 따라서 $w$에서 nodal domain을 갖는 stable map들의 locus, 곧 boundary는

$$\prod_{q\in\Sing C}\t_q=0$$

으로 주어지는 normal crossings divisor이다. 즉 node가 $\delta$개인 stable map은 boundary의 smooth branch $\delta$개가 transversal하게 만나는 점이고, 각 branch $\t_q=0$은 node $q$에서 domain을 떼어 낸 gluing morphism의 image의 국소 branch이다.

---

**참고문헌**

**[FP]** W. Fulton, R. Pandharipande, *Notes on stable maps and quantum cohomology*, in *Algebraic Geometry, Santa Cruz 1995*, Proc. Sympos. Pure Math. **62**, Part 2, AMS, 1997, pp. 45–96.  
**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
