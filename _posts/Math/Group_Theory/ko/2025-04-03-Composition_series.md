---

title: "합성열"
excerpt: ""

categories: [Math / Group Theory]
permalink: /ko/math/group_theory/composition_series
header:
    overlay_image: /assets/images/Math/Group_Theory/Composition_series.png
    overlay_filter: 0.5
sidebar: 
    nav: "group_theory-ko"

date: 2025-04-03
last_modified_at: 2025-04-03
weight: 3

---


## 교환자

우리는 [\[대수적 구조\] §가환군, ⁋정의 3](/ko/math/algebraic_structures/abelian_groups#def3)에서, 임의의 group $G$와 $G$의 두 subgroup $H,H'$에 대하여 이들의 commutator들로 이루어진 subgroup $[H,H']$를 정의하였다. 해당 글에서는 $H=H'=G$인 경우만 생각하였으나, 이번 글에서는 이를 일반화할 것이므로 우선 commutator에 대한 성질을 더 자세히 살펴보자. 

우선 $[h,h']^{-1}=[h',h]$인 것으로부터 $[H,H']=[H',H]$이 항상 성립한다. 만일 $[H,H']=\\{e\\}$라면, 모든 $h,h'$에 대하여 $hh'=h'h$이므로 $C_G(H)\subseteq H'$이고 $C_G(H')\subseteq H$이며 이들 두 조건 중 하나가 성립하면 $[H,H']=\\{e\\}$가 성립하는 것 또한 자명하다. 비슷하게, 만일 $[H,H']\subseteq H$라 하면 임의의 $h,h'$에 대하여

$$h^{-1}h'^{-1}hh'\in H\implies h'^{-1}hh'^{-1}\in H$$

이므로 $H'\subseteq N_G(H)$이며, 마찬가지로 그 역 또한 자명하다. 마지막으로 만일 $H,H'$가 모두 $G$의 *normal* subgroup이었다면, $[H,H']$의 임의의 generator $[h,h']=h^{-1}h'^{-1}hh'$와 $G$의 임의의 원소 $x$에 대하여

$$x[h,h']x^{-1}=(xh^{-1}x^{-1})(xh'^{-1}x^{-1})(xhx^{-1})(xh'x^{-1})$$

이고, 이 때 $H, H'$ 각각이 normal subgroup이라는 가정으로부터 $[H,H']$ 또한 $G$의 normal subgroup이 된다. 

이러한 종류의 계산을 위한 결과를 [보조정리 1](#lem1)에서 정리한다. 그 전에 표기법을 간단히 하기 위해, inner automorphism $\rho_g: x\mapsto gxg^{-1}$에 대하여

$$\rho_{g^{-1}}(x)=x^g$$

이라 적기로 하자. 그럼 [\[대수적 구조\] §군의 작용, ⁋명제 9](/ko/math/algebraic_structures/group_actions)에 의해, 임의의 $g_1,g_2\in G$와 $x\in G$에 대하여

$$(x^{g_1})^{g_2}=x^{g_1g_2}$$

이 성립한다. 

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 임의의 $x,y,z\in G$에 대하여 다음이 성립한다.

1. $xy=yx[x,y]$.
2. $x^y=[y,x^{-1}]x$.
3. $[x,yz]=[x,z][x,y]^z=[x,z][z,[y,x]][x,y]$.
4. $[xy,z]=[x,z]^y[y,z]=[x,z][[x,z],y][y,z]$.
5. $[x^y,[y,z]][y^z,[z,x]][z^x,[x,y]]=e$.
6. $[x,yz][z,xy][y,zx]=e$.
7. $[xy,z][yz,x][zx,y]=e$.

</div>

이에 대한 증명은 단순히 각 변을 전개하는 것이므로 생략한다. 이를 사용하여 다음을 보일 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Group $G$의 세 subgroup $H, H', H''$에 대하여 다음이 성립한다.

1. $H$는 $[H,H']$를 normalize한다.
2. 만일 $[H',H'']$이 $H$을 normalize한다면, $[H,[H',H'']]$은 $[h,[h',h]]$ 꼴의 원소들로 생성되는 $G$의 subgroup과 같다. 
3. 만일 $H, H', H''$이 모두 normal이라면 다음 부등식
    
    $$[H, [H',H'']]\subseteq[H'',[H',H]][H', [H'',H]]$$

    이 성립한다. 


</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 임의의 generator $[h_1,h']\in [H,H']$와 $h_2\in H$에 대하여 $[h_1,h']^{h_2}\in [H,H']$를 보이면 충분하다. 이는 [보조정리 1](#lem1)의 넷째 결과로부터
    
    $$[h_1,h']^{h_2}=[h_1h_2,h'][h_2,h']^{-1}$$

    이 성립하므로 얻어진다.
2. 편의를 위해 $[h,[h',h'']]$ 꼴의 원소들로 생성되는 $G$의 subgroup을 $K$라 하자. 그럼 $K\subseteq [H, [H',H'']]$인 것은 자명하므로, 우리가 보여야 할 것은 반대쪽 포함관계 $[H,[H',H'']]\subseteq K$이다. 이제 $[H, [H',H'']]$은 $[h, [h_1', h_1'']\cdots[h_k',h_k'']]$ 꼴의 원소들로 생성되므로 우리가 보여야 할 것은 이런 꼴의 원소들이 $K$에 속한다는 것이다.  
    일반적으로 $h\in H, h'\in H', h''\in H''$와 $x\in G$를 고정하고 원소 $[h, [h',h'']x]$를 생각하자. 그럼 [보조정리 1](#lem1)의 셋째 결과로부터,

    $$[h, [h',h'']x]=[h,x][h, [h', h'']]^x=[h,x][x,[[h',h''],h]][h, [h',h'']]$$

    이 성립한다. 이제 만일 $[H',H'']$가 $H$를 normalize한다는 가정으로부터 $[[h',h''],h]$는 $H$의 원소이므로, 만일 $x$가 $[H', H'']$의 원소였다면 위의 식의 각 항은 모두 $[H, [H',H'']]$의 원소이다. 따라서 귀납적으로 $[H, [H',H'']]$의 임의의 generator가 $K$에 속한다는 것을 보일 수 있다.
3. 마지막으로 만일 $H, H', H''$가 normal이라면, 셋째 결과에서 등장하는 모든 group 또한 normal subgroup이다. 따라서, 둘째 결과에 의하여 임의의 $h,h',h''$에 대하여 원소 $[h,[h',h'']]$가 우변에 속한다는 것을 보이면 충분하다. 이제 $u=h^{(h')^{-1}}$이라 하면 다음의 식

    $$[h, [h', h'']]=[u^{h'}, [h', h'']]=[(h'')^u, [u, h']]^{-1}[(h')^{h''},[h'',u]]^{-1}$$

    으로부터 원하는 결과를 얻는다. 

</details>

## 내림 중심열

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Group $G$에 대하여, 다음의 식

$$C_1(G)=G,\qquad C_{n+1}(G)=[G, C_n(G)]$$

을 통해 $G$의 *lower central series<sub>내림 중심열</sub>* $(C_n(G))_{n\geq 1}$을 정의한다. 

</div>

그럼 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Group homomorphism $f:G \rightarrow G'$에 대하여, $f(C_n(G))\subseteq C_n(G')$이 항상 성립한다. 뿐만 아니라, 만일 $f$가 surjective라면 $f(C_n(G))=C_n(G')$이 성립한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$n$에 대한 귀납법으로 진행한다. $f(C_n(G))\subseteq C_n(G')$라 가정하자. 그럼 $C_{n+1}(G)$의 원소는 정의에 의하여

$$x^{-1}y^{-1}xy,\qquad x\in G, y\in C_n(G)$$

꼴의 원소들로 생성되며, 

$$f(x^{-1}y^{-1}xy)=f(x)^{-1}f(y)^{-1}f(x)f(y)\in [G, f(C_n(G))]\subseteq [G, C_n(G')]=C_{n+1}(G')$$

이므로 원하는 결과를 얻는다. 만일 $f$가 surjective라면, $f(G)=G'$이고 위의 귀납법에서 $\subseteq$를 $=$으로 대체할 수 있다.

</details>

한편, $G$는 $G$의 normal subgroup이므로, 마찬가지의 귀납법을 통해 $C_n(G)$들은 모두 $G$의 normal subgroup이며, 따라서 $C_{n+1}(G)$는 $C_n(G)$의 normal subgroup이기도 하다. 한편 우리는 임의의 group $G$와 $G$의 subgroup $H$, 그리고 $G$의 normal subgroup $N$에 대하여 canonical projection $G \rightarrow G/N$을 통한 $H$의 image가 $G/N$의 center에 포함되는 것과 $[G, H]\subseteq N$이 동치임을 알고 있으므로, 이로부터 $C_n(G)/C_{n+1}(G)$은 $G/C_{n+1}(G)$의 center에 포함된다. 즉, 다음의 extension

$$\mathcal{E}: C_{n}(G) \rightarrow G \rightarrow C_{n+1}(G)$$

이 central extension이다. ([§군의 확장, ⁋정의 5](/ko/math/group_theory/extensions#def5)) 