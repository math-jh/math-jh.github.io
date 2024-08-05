---

title: "아핀스킴"
excerpt: "국소적 환 달린 공간과 아핀 스킴"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2023-11-01
last_modified_at: 2023-11-01
weight: 5

---

## 국소적 환 달린 공간

[§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)의 첫 번째 결과에 의하여, 임의의 스펙트럼 $(\Spec A, \mathscr{O}\_{\Spec A})$의 점 $\mathfrak{p}$에서의 stalk은 항상 local ring이 된다. 이러한 상황을 다음과 같이 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ringed space $(X,\mathscr{O}_X)$의 임의의 stalk $\mathscr{O}\_{X,p}$이 항상 local ring이라면 이를 *locally ringed space<sub>국소적 환 달린 공간</sub>*이라 부른다. Locally ringed space $(X,\mathscr{O}\_X)$에서 $(Y,\mathscr{O}\_Y)$로의 *morphism*은 ringed space 사이의 morphism $(f,f^\sharp)$ 중, $f\_p^\sharp:\mathscr{O}\_{Y,f(p)}\rightarrow \mathscr{O}\_{X,p}$이 항상 local homomorphism인 것들을 말한다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 다음이 성립한다.

1. [⁋스펙트럼, 정의 3](/ko/math/algebraic_geometry/spectrums#def3)의 $(\Spec A, \mathscr{O}\_{\Spec A})$는 항상 locally ringed space이다.
2. Ring homomorphism $\phi:A \rightarrow B$는 locally ringed space 사이의 morphism 
    
    $$(f,f^\sharp):(\Spec B,\mathscr{O}_{\Spec B}) \rightarrow (\Spec A,\mathscr{O}_{\Spec A})$$

    을 유도한다.
3. 반대로, 두 locally ringed space $(\Spec B,\mathscr{O}\_{\Spec B})$에서 $(\Spec A,\mathscr{O}\_{\Spec A})$로의 임의의 morphism은 항상 위와 같은 방식으로 얻어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 지먕히디.
2. 잎서 [§스펙트럼, ⁋명제 6](/ko/math/algebraic_geometry/spectrums#prop6)에서 위의 map을 정의하고 이것이 두 ringed space들 사이의 morphism임을 보였다. 한편 prime ideal $\mathfrak{p}\in\Spec B$에 대하여

    $$f^\sharp_p:\mathscr{O}_{\Spec A, f(\mathfrak{p})} \rightarrow \mathscr{O}_{\Spec B, \mathfrak{p}}$$

    는 $\phi_\mathfrak{p}:A_{\phi^{-1}(\mathfrak{p})}\rightarrow B_\mathfrak{p}$와 같으며, 이는 $A_{\phi^{-1}(\mathfrak{p})}$의 유일한 maximal ideal $\phi^{-1}(\mathfrak{p})A_{\phi^{-1}(\mathfrak{p})}$를 $B\_\mathfrak{p}$의 유일한 maximal ideal $\mathfrak{p}B_\mathfrak{p}$로 보낸다. 
3. 마지막으로, locally ringed space들 사이의 morphism $(f,f^\sharp):(\Spec B, \mathscr{O}\_{\Spec B}) \rightarrow (\Spec A, \mathscr{O}\_{\Spec A})$가 주어졌다 하자. 그럼 우선 $f^\sharp:\mathscr{O}\_{\Spec A} \rightarrow \mathscr{O}\_{\Spec B}$의 global section을 보면

    $$f^\sharp(\Spec A):\Gamma(\Spec A, \mathscr{O}_{\Spec A}) \rightarrow \Gamma(f^{-1}(\Spec A), \mathscr{O}_{\Spec B})=\Gamma(\Spec B, \mathscr{O}_{\Spec B})$$

    이고, [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)의 3번에 의하여 $f^\sharp(\Spec A)$는 $A$에서 $B$로의 ring homomorphism이 된다. 그럼 3번 주장을 보이기 위해서는 이 $\phi=f^\sharp(\Spec A):A \rightarrow B$가 사실은 ($\Spec$에 의하여) $f$와 같은 것임을 보여야 한다. 우선 임의의 $\mathfrak{p}\in\Spec B$에 대하여,

    $$f^\sharp_\mathfrak{p}:\mathscr{O}_{\Spec A, f(\mathfrak{p})} \rightarrow \mathscr{O}_{X,\mathfrak{p}}$$

    을 생각하자. 그럼 정의와 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)의 첫째 결과에 의하여, $f^\sharp_\mathfrak{p}$는 $A_{f(\mathfrak{p})}\rightarrow B(\mathfrak{p})$으로 생각할 수 있으며, 동시에 $\phi$의 정의에 의해 다음의 commutative diagram이 존재한다.

    ![localization](/assets/images/Math/Algebraic_Geometry/Schemes-1.png){:width="162.9px" class="invert" .align-center}

    그런데 가정에 의하여 $f^\sharp_\mathfrak{p}$는 local homomorphism이므로, $A_{f(\mathfrak{o})}$의 유일한 maximal ideal (즉 $f(\mathfrak{p})$의 $A_{f(\mathfrak{p})}$에서의 상)이 $f^\sharp_\mathfrak{p}$에 의해 $B$의 유일한 maximal ideal (즉 $\mathfrak{p}$의 $B$에서의 상)우로 옮겨진다. 바꿔말하면 $\phi^{-!}(\mathfrak{p})=f(\mathfrak{p})$이 성립한다. 처음부터 $\mathfrak{p}$는 임의의 prime ideal로 잡았으므로 $\Spec\phi=f$이고, 이제 어렵지 않게 $f^\sharp$이 $\phi$로부터 유도되는 것을 보일 수 있다.

</details>

## 아핀스킴

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Locally ringed space $(X,\mathscr{O}\_X)$가 어떤 ring의 spectrum과 isomorphic하다면 이를 *affine scheme<sub>아핀스킴</sub>*이라 부른다. 

</div>

Affine scheme들 사이의 morphism은 locally ringed space 사이의 morphism으로 주어진다. 그럼 [명제 2](#prop2)가 주장하는 것은 $\Spec$이 $\cRing$에서 affine scheme들의 category $\AffSch$로의 functor일 뿐만 아니라, 두 category $\cRing^\op$와 $\AffSch$ 사이의 categorical equivalence를 정의한다는 것이다. 

특별히 $\cRing$에서의 canonical morphism들이 $\AffSch$에서는 어떻게 정의되는지를 살펴볼 필요가 있다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 임의의 ring $A$와 ideal $\mathfrak{a}$를 고정하면, canonical projection $A \rightarrow A/\mathfrak{a}$가 존재한다. 이를 $\Spec$을 통해 기하적으로 살펴보면 $\Spec A/\mathfrak{a} \rightarrow \Spec A$가 되고, 위의 projection이 surjective이므로 스펙트럼 사이의 map은 injective가 된다. 더 명시적으로 이야기하자면 $A/\mathfrak{a}$의 prime ideal은 정확히 $A$의 prime ideal 중 $\mathfrak{a}$를 포함하는 것들이기 때문에 이것이 성립한다고 볼 수도 있다. 

</div>

또 다른 중요한 예시는 localization으로부터 나오는 $\epsilon:A \rightarrow S^{-1}A$이다. 

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 임의의 ring $A$와 multiplicative subset $S$를 고정하면, canonical map $A \rightarrow S^{-1}A$기 존재하고, 따라서 스펙트럼 사이의 map $\Spec S^{-1}A \rightarrow\Spec A$가 존재한다. 그런데 $S^{-1}A$의 prime ideal은 정확히 $A$의 prime ideal 중, $S$와 만나지 않는 것이므로 이 map 또한 injective가 된다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 일반적인 위상수학에서 위상공간 $X$의 한 점은 one-point space $\ast$에서 $X$로의 continuous map으로 생각할 수 있는데, 이번 예시에서는 이를 scheme의 세상에서 살펴본다. 

임의의 field $k$에 대하여, $\Spec k$는 하나의 원소 $(0)$만을 가지며, structure sheaf $\mathscr{O}\_{\Spec k}$는 $\mathscr{O}\_{\Spec k}((0))=k$를 통해 주어진다. 앞서 언급한 위상공간에서의 예시를 떠올리면, affine scheme $(\Spec A, \mathscr{O}\_{\Spec A})$의 한 점은 다음의 morphism 

$$(f, f^\sharp):(\Spec k, \mathscr{O}_{\Spec k})\rightarrow (\Spec A, \mathscr{O}_{\Spec A})$$

으로 생각하는 것이 자연스러울 것이다. $f((0))=\mathfrak{p}$라 하자. 그럼 $f^\sharp$이 local homomorphism이라는 조건으로부터, 다음의 ring homomorphism

$$f^\sharp_{(0)}:\mathscr{O}_{\Spec A, \mathfrak{p}} \rightarrow \mathscr{O}_{\Spec k, (0)}$$

이 local homomorphism인 것을 안다. 그런데 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)에 의하여 $\mathscr{O}\_{\Spec k, (0)}\cong k_{(0)}\cong k$이고, $\mathscr{O}\_{\Spec A, \mathfrak{p}}\cong A\_\mathfrak{p}$이며 $A\_\mathfrak{p}$의 유일한 maximal ideal은 $\mathfrak{p}A_\mathfrak{p}$이다. 그런데 $k$의 유일한 maximal ideal은 $(0)$이므로, $\mathscr{O}\_{\Spec A, \mathfrak{p}}$의 maximal ideal $\mathfrak{p}A_\mathfrak{p}$가 $0$으로 옮겨져야 한다. 즉 $\mathfrak{p}A_\mathfrak{p}\subseteq\ker f^\sharp\_{(0)}$이며 따라서 $\mathscr{O}\_{\Spec A, \mathfrak{p}}/\mathfrak{p}A_\mathfrak{p} \rightarrow k$가 정의된다. 거꾸로 이러한 local homomorphism이 주어진다면 이를 $\Spec A$의 한 점으로 생각할 수 있다. 이 때 field $\kappa(\mathfrak{p})=\mathscr{O}\_{\Spec A, \mathfrak{p}}/\mathfrak{p}A_\mathfrak{p}\cong\Frac(A/\mathfrak{p})$를 $A$의 점 $\mathfrak{p}$에서의 *residue field*라 부른다. 

</div>

더 일반적으로, 위의 예시에서 field $k$를 local ring $B$으로 바꾸고, $\mathfrak{m}$이 어느 점으로 가는지를 살펴보자. 만일 $f(\mathfrak{m})=\mathfrak{p}$라면, $f^\sharp$이 local homomorphism이라는 조건으로부터

$$f^\sharp_{\mathfrak{m}}:\mathscr{O}_{\Spec A, \mathfrak{p}} \rightarrow \mathscr{O}_{\Spec B, \mathfrak{m}}$$

이 local homomorphism이라는 것을 알고, 마찬가지로 [§스펙트럼, ⁋명제 5](/ko/math/algebraic_geometry/spectrums#prop5)으로부터 $\mathscr{O}\_{\Spec B, \mathfrak{m}}\cong B_\mathfrak{m}\cong B$인데, $B$의 유일한 maximal ideal은 $\mathfrak{m}$이므로 위의 예시와 비슷한 일을 할 수 있다. 즉 $\mathfrak{m}\in\Spec B$이 $\mathfrak{p}\in\Spec A$로 보내지는 morphism은 정확하게 $A\_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$에서 $B$로의 local homomorphism과 같은 것이다. 