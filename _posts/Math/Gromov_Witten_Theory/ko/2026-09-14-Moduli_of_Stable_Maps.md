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

---

우리는 [\[스택\] §고유스택](/ko/math/stacks/proper_stacks){: data-lid="5ib31" data-relation="weak" }에서 moduli space의 properness가 갖는 중요성을 이미 살펴보았지만, 일반적인 enumerative problem에서는 이러한 성질을 기대할 수 없다. 이러한 종류의 문제 중 고전적인 것은 $\mathbb{P}^2$ 안의 $3d-1$개의 general point를 지나는 degree $d$ rational curve를 세는 문제로, 예를 들어 $d=2$일 때 그 값은 $1$인 것이 알려져 있다. 즉 $\mathbb{P}^2$ 안의 $5$개의 점을 지나는 곡선은 유일하게 존재하여야 한다. 반면 다음 map

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

Incidence condition도 map의 자료로 기록할 수 있다. 곡선이 주어진 점 $q_i\in X$를 지난다는 조건은 domain 위에 점 $p_i$를 지정하고 $\mu(p_i)=q_i$를 요구하면 되므로, 우리가 원하는 map의 domain은 정확히 prestable curve가 모두 담고 있다. ([§마디 곡선의 변형, ⁋정의 1](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#def1){: data-lid="ovp6z" data-relation="required" }) 앞의 예에서는 limit의 각 $q_i$에 대응하는 점을 해당 component 위에 표시하면 될 것이며, 일반적인 incidence condition은 $\mu(p_i)$가 지정된 subvariety에 속하도록 부과한다.

이제 우리가 자료를 map에 담을 때 생기는 문제는 같은 곡선이 다른 parametrization을 통해서 바뀌면 이는 다른 map으로 보인다는 것이다. 따라서 우리는 marked point와 map을 보존하는 domain의 isomorphism으로 이들을 identify한다. 문제는 한 자료 안에서도 automorphism이 생길 수 있다는 것인데, 일반적으로 우리가 생각하는 automorphism은 map 자체의 대칭을 나타내는 정보이므로 이는 유의미한 정보이다. 그러나 nodal domain을 허용하면 이러한 유의미한 정보는 아무것도 보태지 않는 parametrization의 자유도가 생길 수 있는데, 예를 들어 한 점으로 보내지는 한 $\mathbb{P}^1$ 성분에 node가 하나 뿐이고, marked point가 아무것도 없으면 이 성분은 무한히 많은 automorphism을 가지지만, 이 성분을 무시해도 나머지 map과 marked point의 정보는 고스란히 남아있다. 이러한 성분을 배제하기 위해 우리는 automorphism group이 유한하다는 stability 조건을 부과하며, 이는 map의 유한한 대칭을 허용하면서 moduli가 Deligne–Mumford stack이 되게 하는 핵심 조건이다. 여기에 곡선의 class $\beta$를 고정하면 다음 정의를 얻는다.

::: 정의 1
Genus $g$의 $n$-pointed prestable curve $(C,p_1,\ldots,p_n)$와 class $\beta\in H_2(X,\mathbb{Z})$가 주어졌다고 하자. *Stable map<sub>안정사상</sub>*은 prestable curve와, 이를 domain으로 갖는 map $\mu$의 쌍

$$(C,p_1,\ldots,p_n,\mu),\qquad \mu:C\rightarrow X$$

으로서, 다음 두 조건을 만족하는 것들이다. 

- $\mu_\ast[C]=\beta$이다.
- Automorphism group $\Aut(C,p_1,\ldots,p_n,\mu)$이 유한하다.

두 stable map은 marked point와 $X$로 가는 map을 보존하는 domain의 isomorphism이 존재할 때 두 map이 *isomorphic*하다 말한다. 
:::

첫째 조건은 각 성분의 mapping degree를 반영하여 image의 class를 합한 값이 $\beta$라는 뜻이다. 둘째 조건을 살펴보면, automorphism 중 서로 다른 성분들과 node들의 순열로 나오는 것 혹은 self-node의 두 branch를 맞바꾸는 등의 경우의 수는 유한하므로, automorphism의 유한성은 본질적으로 domain curve의 각 성분의 automorphism의 유한성에 대한 조건이 된다. 

이러한 automorphism을 고정하는 것은 marked point들과 node들이 그대로 남아있어야 한다는 조건으로, 우리는 이들 두 종류의 점들을 통틀어 *special points*라 부른다. Domain curve $C$의 irreducible component $C_i$의 normalization을 $\widetilde{C}_i$라 하고, $\widetilde{C}_i$의 special point의 개수를 $s_i$라 하자. 

이제 $\widetilde{C}_i$의 genus 개수를 $h_i$라 하면 tangent bundle $\mathcal{T}_{\widetilde{C}_i}$의 degree는 $2-2h_i$이다. Special point들의 합을 divisor $D_i$로 적으면, [§마디 곡선의 변형, ⁋명제 4](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#prop4){: data-lid="paz7d" data-relation="required" }와 그 이후의 논증에 의하여 이 점들을 고정하는 infinitesimal automorphism은

$$H^0\bigl(\widetilde{C}_i,\mathcal{T}_{\widetilde{C}_i}(-D_i)\bigr)$$

로 계산된다. 이는 $\widetilde{C}_i$의 special point들을 각각 고정하는 automorphism group $G$의 항등원에서의 tangent space와 같았으므로, 만일 이 차원이 $0$이 된다면 $G$의 항등원에서의 차원, 더 나아가 임의의 점에서의 차원이 $0$차원이 된다. 일반적으로 smooth projective curve의 유한개의 점을 고정하는 automorphism group은 finite type임이 알려져 있으므로, 이 사실로부터 $G$가 유한하다는 사실을 얻을 수 있다. 

이제 만일 $h_i\geq2$이면 $\deg\mathcal{T}_{\widetilde{C}_i}=2-2h_i<0$이므로 global vector field가 없다. ([\[대수다양체\] §곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="pq7bu" data-relation="required" }) 따라서 이 경우에는 special point가 없어도 automorphism group이 유한하다. 이는 낮은 genus에서는 일반적으로 성립하지 않는 논증으로, 여기에 special point들이 고정된다는 조건을 이용해 자유도를 줄여주어야 한다. 우선 $h_i=0$인 경우, $\widetilde{C}_i\cong\mathbb{P}^1$이고 $\mathcal{T}_{\mathbb{P}^1}(-D_i)\cong\mathcal{O}_{\mathbb{P}^1}(2-s_i)$이므로 위 공간의 dimension은 $\max\{3-s_i,0\}$이고, 따라서 $s_i$는 $3$ 이상이어야 한다. 직관적으로 이는 $\mathbb{P}^1$의 automorphism은 $(az+b)/(cz+d)$의 꼴이므로 $3$개의 자유도가 있는데, 이 자유도를 special point들이 하나씩 죽여주는 상황에 해당한다. $h_i=1$인 경우, tangent bundle은 trivial이 되어 global vector field의 공간은 dimension $1$이 되고, 이를 죽이기 위해서는 최소 하나의 special point가 필요하다. 

정리하면 automorphism group의 유한성은, 위와 같은 상황에서 

$$2g(\widetilde{C}_i)-2+s_i>0$$

이 성립하는 것과 같다. 즉 genus $0$에서는 special point가 적어도 $3$개, genus $1$에서는 적어도 $1$개가 필요하며, genus $2$ 이상에서는 추가조건이 없다. 이 조건은 오직 $\mu$가 constant로 죽이는 component $C_i$에만 해당되는 것으로, 만일 $\mu$가 $C_i$에서 nonconstant라면 이미 automorphism group이 $\mu$를 보존해야 한다는 사실로부터 유한성이 따라나온다. 

::: 예시 2
우리는 이제 automorphism group이 (non-trivial하게) 유한하게 나오는 경우를 실제로 살펴본다. $C$가 irreducible nodal cubic이고 $\mu:C\rightarrow X$가 constant map이라고 하자. $C$의 arithmetic genus는 $1$이지만 normalization은 $\mathbb{P}^1$이다. ([\[대수다양체\] §접공간과 매끄러움, ⁋예시 7](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#ex7){: data-lid="0htg0" data-relation="weak" }) Node 위의 두 점을 $0,\infty$로 잡으면, marked point가 없을 때는 모든 $z\mapsto az$ ($a\in\mathbb{C}^{\times}$)가 이 두 점을 고정하고 $C$의 automorphism으로 내려간다. 따라서 이 map은 stable하지 않으며, 실제로 위의 부등식에 $h_i=0$, $s_i=2$를 대입해보아도 확인할 수 있다. 

이제 smooth locus에 marked point $p$ 하나를 고르고 그 preimage가 $1$이 되도록 좌표를 잡으면 $s_i=3$이 되어 이는 stability 조건을 만족한다. 단 여기서 주의할 것은 automorphism group이 trivial group이 아니라는 것이다. 즉 $0,1,\infty$를 각각 고정하는 automorphism은 항등사상 뿐이지만, 처음 normalization 단계에서 node의 두 branch를 서로 바꾸어줄 수 있는 자유도가 있으며, 실제로 $z\mapsto1/z$이 $0,\infty$를 맞바꾸고 $1$을 고정해주는 automorphism의 역할을 한다. 즉,

$$\Aut(C,p,\mu)\cong\mathbb{Z}/2$$

이다. 반면 같은 nodal cubic의 inclusion $C\hookrightarrow\mathbb{P}^2$는 map을 보존하는 automorphism이 항등사상뿐이므로 marked point가 없어도 stable하다.
:::

Stability는 이처럼 각 성분의 parametrization에 연속적인 자유도가 남는지를 판정한다. Contracted component에서는 special point가 그 자유도를 제한하고, nonconstant component에서는 map 자체가 이를 제한한다. Nodal cubic의 예처럼 유한한 대칭은 남을 수 있으며, 이 대칭까지 기록하는 것이 stable map의 moduli를 Deligne–Mumford stack으로 다루는 이유이다.

## 안정사상들의 모듈라이 공간

[예시 2](#ex2){: data-lid="nr248" data-relation="required" }에서 보았듯, stable map은 비자명한 automorphism을 가질 수 있다. 따라서 stable map들을 모아둔 공간은 각 점이 나타내는 map의 automorphism까지 기억하는 stack으로 다룬다. Genus $g$, marked point의 개수 $n$, effective class $\beta$ (즉 $X$ 안의 irreducible curve들의 homology class를 음이 아닌 정수 계수로 합한 class)를 고정한 stable map들의 family와 그 사이의 isomorphism으로 이루어진 stack을

$$\overline{\mathcal{M}}_{g,n}(X,\beta)$$

로 적는다. 이 stack의 geometric point들의 isomorphism class는 stable map들의 isomorphism class에 대응하고, 각 점의 stabilizer는 해당 stable map의 automorphism group이 된다.

::: 명제 3
$\beta$가 effective class이면 $\overline{\mathcal{M}}_{g,n}(X,\beta)$은 proper Deligne–Mumford stack이고 ([\[스택\] §대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6){: data-lid="r3t1v" data-relation="required" }), 그 coarse moduli space는 projective scheme이다. ([\[스택\] §모듈라이 공간, ⁋정의 7](/ko/math/stacks/moduli_spaces#def7){: data-lid="d7w0d" data-relation="required" })
:::

도입부에서 properness가 필요했던 이유는 주어진 조건을 움직일 때 곡선의 limit이 moduli 안에 남아 있어야 했기 때문이며, 위 명제는 $\overline{\mathcal{M}}_{g,n}(X,\beta)$이 그러한 조건을 만족하는 moduli space임을 보여준다. 예를 들어 도입부의 conic 계산에서 image가 둘로 갈라진다면, 우리는 그 domain도 두 개의 성분으로 나누어줄 수 있으므로 이는 더 이상 문제가 되지 않는다. 한편, 문제의 소지가 있는 limit은 이러한 상황에서만 일어나는 것은 아닌데, 가령 두 marked point들이 하나의 점으로 충돌하는 경우에도 그 극한은 순진한 방식으로는 $\overline{\mathcal{M}}_{g,n}(X,\beta)$ 안에 머물지 않는다. 이 경우 우리는 이 충돌지점에 $\mathbb{P}^1$ component를 붙이고, 충돌한 두 marked point를 이 component 위에 붙이는 방식으로 원래의 모습을 기억한다. 이 때 새로 생긴 $\mathbb{P}^1$ component는 $\mu$를 통해 충돌지점의 image $\mu(p)$로 옮겨지며, 이 component에는 node 하나와 두 marked point가 있으므로 stability condition은 여전히 만족된다. 

이는 엄밀하게는 곡선들이 이루는 family를 생각한 것으로 이해할 수 있다. 이를 위해 충돌지점 근처에서 국소적으로 매개변수 $\t$를 사용하여 곡선들의 family $C_\t$를 매개화하고, central fiber $\t=0$에서 두 marked point가 충돌한다 하자. 이 그림에서 곡선들의 family는 total space가 곡면인 $S\rightarrow \mathbb{A}^1_\t$으로, 각 marked point의 궤적은 이 projection의 두 section으로 나타나며, 따라서 두 marked point가 $\t=0$에서 충돌한다는 것은 이 section들이 $\t=0$에서 교점을 갖는다는 것으로 이해할 수 있다. 가령 각 fiber의 local coordinate를 $\z$라 하고 두 section을 $\z=0$, $\z=\t$로 잡으면 이 두 section은 $(\z,\t)=(0,0)$에서 교점을 가지게 된다. 이러한 상황에서 충돌을 풀어주는 표준적인 방법은 blowup으로, 위에서 붙여준 bubble $\mathbb{P}^1$은 바로 이 blowup의 exceptional curve이며, blowup의 coordinate $\u=\z/\t$에서 두 section의 strict transform은 $\u=0,\u=1$이 되어 이 component에서 서로 다른 두 marked point가 나타나게 되는 것이다. 우리의 예시에서는 두 section이 일차식으로 만났으므로 blowup이 한 번으로 끝났지만, 이들 section이 높은 차수로 만나는 경우에는 이들을 분리할 때까지 blowup을 반복해야 한다. 그러나 이 과정에서 중간에 생기는 component들은 stability를 만족하지 않게 되어 한 점으로 수축되므로, 최종적으로 나오는 그림은 위에서 설명한 그림과 동일하다. 

이제 이 moduli stack $\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위에는 몇 가지 자연스러운 morphism들이 존재한다. 우선 각 marked point의 image를 읽는 *evaluation map*은

$$\ev_i:\overline{\mathcal{M}}_{g,n}(X,\beta)\rightarrow X,\qquad (C,p_\bullet,\mu)\mapsto\mu(p_i)$$

으로 정의되며, 그 의미 또한 명확하다. 일반적인 enumerative problem에서는 $i$번째 marked point가 주어진 subvariety를 지난다는 incidence condition을 부과할 때가 많은데, 이러한 경우 그 subvariety의 class를 $\ev_i$로 pullback해오면 된다. 

또 다른 morphism은 마지막 marked point를 잊는 *forgetful morphism*

$$\pi:\overline{\mathcal{M}}_{g,n+1}(X,\beta)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

으로, $\beta\neq 0$ 혹은 $2g-2+n>0$인 경우 항상 정의된다. Marked point의 개수는 stability를 통제하는 변수이므로, 단순히 마지막 marked point를 잊기만 한다면 그 결과는 stable map이 되지 않을 수 있는데, $\pi$는 이렇게 unstable해진 component를 점으로 수축시키는 stabilization 과정까지 포함하여 그 결과물이 stable map이 되도록 만들어준 morphism이며, 이를 위해 앞선 조건 $\beta\neq 0$ 또는 $2g-2+n>0$이라는 가정이 필요하다. 이렇게 정의한 $\pi$는 $\overline{\mathcal{M}}_{g,n}(X,\beta)$ 위의 universal curve가 된다. ([\[스택\] §모듈라이 공간, §§모듈라이 함자](/ko/math/stacks/moduli_spaces#모듈라이-함자){: data-lid="r8e2o" data-relation="required" }) 실제로, 편의상 stable map 하나, 즉 $\overline{\mathcal{M}}_{g,n}(X,\beta)$의 점 하나를 고정하고 이 위에서의 $\pi$의 fiber를 본다고 하면, 이 점에서 fiber로 가는 section을 정하는 것은 정확하게 마지막 marked point를 이 stable map의 어디에 찍는지와 같으며 따라서 이 점 위에서의 fiber가 그 stable map의 domain curve로 나오게 된다. 

마지막으로 $2g-2+n>0$이면 map 없이도 stable한 pointed curve로 안정화할 수 있다. 이 경우 $X$로 가는 map을 잊은 뒤, pointed curve로서 unstable한 성분들을 수축하여

$$\overline{\mathcal{M}}_{g,n}(X,\beta)\rightarrow\overline{\mathcal{M}}_{g,n},\qquad (C,p_\bullet,\mu)\mapsto(C,p_\bullet)^{\mathrm{stab}}$$

을 얻는다.

앞서 properness를 설명할 때, smooth domain을 갖는 stable map의 family가 nodal domain을 갖는 stable map으로 degenerate할 수 있으므로 이러한 limit도 moduli에 포함해야 함을 보았다. 이제 이러한 nodal domain을 갖는 locus를 *boundary*라 부르고, node에서 domain을 분리한 뒤 다시 붙이는 방식으로 기술한다. 우선 node 하나의 두 branch를 떼어냈을 때 curve가 두 개의 connected curve로 나뉘고 $\{1,\ldots,n\}=A\sqcup B$, $g=g_1+g_2$, $\beta=\beta_1+\beta_2$라면 gluing morphism은

$$\overline{\mathcal{M}}_{g_1,A\cup\{\bullet\}}(X,\beta_1)\times_X\overline{\mathcal{M}}_{g_2,B\cup\{\bullet\}}(X,\beta_2)\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

이다. 두 factor에 새로 붙인 marked point $\bullet$의 evaluation이 같아야 하나의 node로 붙일 수 있으므로 fiber product가 $X$ 위에서 형성된다. 이때 source는 붙이기 전의 두 curve를 첫째와 둘째로 구별하지만, 붙인 결과는 그 순서를 기억하지 않는다. 따라서 두 factor의 genus, marking, class 자료가 같아 서로 맞바꿀 수 있는 경우에는 이 morphism이 그 image와 isomorphic하지 않을 수 있다. 또, node가 여러 개 있는 curve에서는 같은 분해 자료를 주는 node를 서로 다르게 선택할 수 있으며, 이 경우에도 서로 다른 gluing 자료가 같은 stable map을 줄 수 있다. 이것이 boundary의 서로 다른 국소 branch가 만나는 상황이다.

한편 node의 두 branch를 떼어내도 curve가 여전히 connected일 수 있다. [예시 2](#ex2){: data-lid="vz072" data-relation="weak" reviewed="" }의 irreducible nodal cubic이 바로 이런 경우로, node를 풀면 두 curve로 갈라지는 대신 하나의 $\mathbb{P}^1$ 위에 두 점 $0,\infty$가 나타난다. 일반적으로, 이 경우에는 node를 풀면 arithmetic genus가 하나 줄어들므로, 우리는 genus $g-1$의 connected curve 위에 두 marked point를 붙인다. 해당 gluing morphism은

$$\overline{\mathcal{M}}_{g-1,n+2}(X,\beta)\times_{X\times X}X\rightarrow\overline{\mathcal{M}}_{g,n}(X,\beta)$$

이고, $X\rightarrow X\times X$는 diagonal이다. 여기서도 source는 마지막 두 marked point의 순서를 구별하지만 붙인 결과는 이를 기억하지 않는다. 예시 2의 $z\mapsto1/z$은 이 두 점을 맞바꾸므로, 붙이기 전에는 각각의 marked point를 보존하는 automorphism이 아니지만 붙인 뒤에는 stable map의 automorphism이 된다. 

## Virtual dimension
{: #기대차원 }

$\overline{\mathcal{M}}_{g,n}(X,\beta)$은 일반적으로 매끄럽지 않으며, $g,n,\beta$를 고정해도 여러 irreducible component를 가질 수 있다. 뿐만 아니라 이러한 component들은 서로 만날 수도 있고, 각각의 차원도 다를 수 있다.

반면 stable map $(C,p_\bullet,\mu)$의 infinitesimal deformation space를 $T^1$, obstruction space를 $T^2$라 하면, 이 deformation–obstruction theory는 *virtual dimension*

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

::: 증명
위에서 정의한 $\LL_\mu$에 $R\Hom_C(-,\mathcal{O}_C)$를 적용하면 위 exact sequence가 나온다. 첫 morphism의 kernel은 pointed domain의 infinitesimal automorphism 중 map까지 보존하는 것들로, stability에 의해 이 kernel이 $0$이므로 sequence의 왼쪽에 $0$이 붙는다.

이제 $E=\mu^\ast T_X$, $A^i=\Ext_C^i(\Omega_C(p_1+\cdots+p_n),\mathcal{O}_C)$로 적자. 위 exact sequence에서 차원의 교대합은 $0$이므로

$$\dim T^1-\dim T^2=\bigl(\dim A^1-\dim A^0\bigr)+\rchi(C,E)$$

로 분리된다. 이 때 첫 괄호는 pointed domain의 deformation space와 infinitesimal automorphism space의 차원이므로, [§마디 곡선의 변형, ⁋따름정리 6](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#cor6){: data-lid="5ao1g" data-relation="required" }에 의하여 $3g-3+n$이다.

둘째 항의 경우, 우선 smooth projective curve $Y$ 위의 rank $r$ vector bundle $F$에 대하여, [\[대수다양체\] §곡선에서의 리만-로흐 정리, ⁋명제 3](/ko/math/algebraic_varieties/riemann_roch_theorem#prop3){: data-lid="ol72u" data-relation="required" }의 vector bundle 버전은

$$\rchi(Y,F)=\deg F+r(1-g(Y))$$

을 준다. 

우리의 domain $C$는 smooth curve는 아니지만, normalization $\nu:\widetilde C=\coprod_{j=1}^c\widetilde C_j\rightarrow C$을 통해 이 계산을 옮겨줄 수 있다. 각 $\widetilde C_j$의 genus를 $h_j$, node의 개수를 $d$, $E$의 rank를 $r$라 하자. Structure sheaf의 normalization exact sequence ([§마디 곡선의 변형, ⁋정의 1](/ko/math/gromov-witten_theory/deformations_of_nodal_curves#def1){: data-lid="uihgw" data-relation="required" } 직후)에 locally free sheaf $E$를 tensor하면

$$0\rightarrow E\rightarrow\nu_\ast\nu^\ast E\rightarrow\bigoplus_{q\in\Sing C}E\otimes_{\mathcal O_C}\kappa(q)\rightarrow0$$

을 얻는다. 이제 이를 사용하면

$$\rchi(C,E)=\sum_{j=1}^c\rchi(\widetilde C_j,\nu^\ast E\vert_{\widetilde C_j})-rd=\sum_{j=1}^c\left(\deg(\nu^\ast E\vert_{\widetilde C_j})+r(1-h_j)\right)-rd=\deg E+r\left(c-\sum_{j=1}^c h_j-d\right)=\deg E+r(1-g)$$

이고, 이 식에 $E=\mu^\ast T_X$를 대입하면 $\rank E=\dim X$이고, $\mu_\ast[C]=\beta$이므로 

$$\deg E=\int_C\mu^\ast c_1(T_X)=\int_\beta c_1(T_X)$$

이다. 

이제 마지막으로 이 계산들을 모두 합하면

$$\dim T^1-\dim T^2=(3g-3+n)+\int_\beta c_1(T_X)+\dim X(1-g)=\int_\beta c_1(T_X)+(\dim X-3)(1-g)+n$$

을 얻는다.
:::

## 예시

위에서 언급한 것처럼, virtual dimension은 실제 dimension보다 항상 작거나 같다. Virtual dimension이 actual dimension이 되는 대표적인 경우는 target $X$가 convex일 때 genus $0$ stable map이다. 여기서 smooth projective variety $X$가 *convex<sub>볼록</sub>*하다는 것은 모든 morphism $\mu:\mathbb{P}^1\rightarrow X$에 대하여 $H^1(\mathbb{P}^1,\mu^\ast T_X)=0$이라는 것이다.

::: 명제 5
$X$가 convex이면 임의의 effective $\beta$와 $n\geq0$에 대하여 $\overline{\mathcal{M}}_{0,n}(X,\beta)$은 virtual dimension

$$\int_\beta c_1(T_X)+\dim X-3+n$$

의 smooth proper Deligne–Mumford stack이다.
:::

Convexity는 smooth $\mathbb{P}^1$ 위의 조건이지만 nodal genus $0$ curve에서도 $H^1(C,\mu^\ast T_X)=0$임을 보일 수 있다. 따라서 [명제 4](#prop4){: data-lid="qh7wb" data-relation="required" reviewed="" }에 의해 $T^2=0$가 성립함을 알 수 있다. 이러한 convex target의 대표적인 예시는 homogeneous space $G/P$로, 이 경우 $T_{G/P}$가 globally generated이므로 convexity가 성립한다.

::: 예시 6
$X=\mathbb{P}^r$, $g=0$, $n=0$, $\beta=[\text{line}]$이라 하자. Degree $1$ stable map은 $\mathbb{P}^1$을 $\mathbb{P}^r$ 안의 직선으로 isomorphic하게 보내며, parametrization의 자유도는 $\Aut(\mathbb{P}^1)$이 흡수한다. 따라서 남는 자료는 직선 자체이고

$$\overline{\mathcal{M}}_{0,0}(\mathbb{P}^r,1)\cong\Gr(2,r+1)$$

이다. 이 Grassmannian의 dimension은 $2(r+1-2)=2r-2$인데, $c_1(T_{\mathbb{P}^r})=(r+1)H$이므로 virtual dimension 또한

$$\vdim=(r+1)+(r-3)=2r-2$$

가 되어 두 값이 일치하는 것을 확인할 수 있다.
:::

같은 계산을 $\overline{\mathcal{M}}_{0,0}(\mathbb{P}^2,2)$에 적용하면

$$\vdim=\int_{2[\text{line}]}c_1(T_{\mathbb{P}^2})+(2-3)=6-1=5$$

이다. $\mathbb{P}^2$은 convex이므로 이 값은 actual dimension과 일치한다.

---

**참고문헌**

**[FP]** W. Fulton, R. Pandharipande, *Notes on stable maps and quantum cohomology*, in *Algebraic Geometry, Santa Cruz 1995*, Proc. Sympos. Pure Math. **62**, Part 2, AMS, 1997, pp. 45–96.  
**[HKK+]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow, *Mirror Symmetry*, Clay Mathematics Monographs **1**, AMS, 2003.
