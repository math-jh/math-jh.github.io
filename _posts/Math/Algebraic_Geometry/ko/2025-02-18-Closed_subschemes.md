---

title: "닫힌 부분스킴"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/closed_subschemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Closed_subschemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-02-18
last_modified_at: 2025-02-18
weight: 9

---

[§스킴, ⁋보조정리 2](/ko/math/algebraic_geometry/schemes#lem2)에서 우리는 affine scheme $\Spec A$에 대하여, 임의의 원소 $f$가 open affine subscheme $D(f)\cong \Spec A_f$를 정의하는 것을 살펴보았으며, 특히 이 두 structure sheaf를 비교하기 위해 우리는 $\epsilon: A \rightarrow A_f$로부터 얻어지는

$$(\Spec\epsilon)^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec \epsilon)_\ast \mathscr{O}_{\Spec A_f}$$

에 [\[위상수학\] §층, ⁋보조정리 11](/ko/math/topology/sheaves#lem11)을 적용하여

$$(\Spec\epsilon \vert^{D(f)})^\sharp: \mathscr{O}_{D(f)} \rightarrow (\Spec\epsilon\vert^{D(f)})_\ast \mathscr{O}_{\Spec A_f}$$

을 얻고, $\Spec A_f$가 $\Spec A$의 열린집합이라는 사실로부터 이것이 isomorphism이라는 사실을 얻을 수 있었다.

한편 [§스펙트럼, ⁋명제 9](/ko/math/algebraic_geometry/spectrums#prop9)의 둘째 결과에 의해, affine scheme $\Spec A$와 $A$의 ideal $\mathfrak{a}$가 주어지면 $\Spec$ functor를 통해 

$$\Spec\pi: \Spec A/\mathfrak{a}\rightarrow \Spec A$$

가 주어지고, 이 때 $\Spec\pi$는 injective이며 그 image는 닫힌집합 $Z(\mathfrak{a})$가 된다는 것을 안다. 이 경우에도 위에서와 마찬가지로 canonical decomposition

$$\Spec A/\mathfrak{a}\overset{\Spec\pi\vert^{Z(\mathfrak{a})}}{\longrightarrow} Z(\mathfrak{a}) \overset{\iota}{\longrightarrow}\Spec A$$

을 생각한 후,

$$(\Spec\pi)^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$

로부터 $Z(\mathfrak{a})$에서 정의된 sheaf들의 morphism

$$\iota^{-1} \mathscr{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$

를 만들 수 있지만, 우리는 $Z(\mathfrak{a})$에 scheme structure를 정의하지도 않았고, 따라서 $\iota^{-1}\mathscr{O}\_{\Spec A}$와 $\mathscr{O}\_{Z(\mathfrak{a})}$ 사이의 관계를 모를 뿐더러, 이것이 isomorphism이 된다는 보장도 없다. 실제로 이는 isomorphism이 되지 않을 가능성이 훨씬 큰데, $\iota^{-1}\mathscr{O}\_{\Spec A}$는 $\Spec A$의 structure sheaf에서 닫힌집합 $Z(\mathfrak{a})$에 대한 위상적인 데이터만을 사용하여 정의된 것이지만, $(\Spec\pi)\_\ast\mathscr{O}\_{\Spec A/\mathfrak{a}}$는 ring $A/\mathfrak{a}$에 대한 대수적인 정보도 가지고 있기 때문이다. 


<div class="example" markdown="1">

<ins id="ex1">**예시 1**</ins> 예를 들어 field $\mathbb{K}$를 고정하고, affine $1$-line $\mathbb{A}\_\mathbb{K}^1=\Spec \mathbb{K}[\x]$을 생각하자. 그럼 다음의 canonical surjection

$$\pi_1:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x)\cong \mathbb{K},\qquad \pi_2:\mathbb{K}[\x] \rightarrow \mathbb{K}[\x]/(\x^2)$$

들이 존재하며, 구체적으로 $\pi_1$과 $\pi_2$는 각각 $\x\mapsto 0+(\x)$와 $\x\mapsto \x+(\x^2)$을 통해 정의된다. 

한편 $\mathbb{K}[\x]/(\x)\cong \mathbb{K}$이므로 $\Spec \mathbb{K}[\x]/(\x)$는 한 점 $(0)$만을 가진다. 마찬가지로 $\Spec \mathbb{K}[\x]/(\x^2)$ 또한 한 점만을 가진다. 이는 $\mathbb{K}[\x]/(\x^2)$의 prime ideal과 $\x^2$을 포함하는 $\mathbb{K}[\x]$의 prime ideal 사이의 일대일대응이 존재하고, $\mathbb{K}[\x]$는 principal ideal domain이므로, $\mathbb{K}[\x]$의 prime ideal을 $(p(\x))$라 쓴다면 이 ideal이 $\x^2$을 포함하기 위해서는 $p(\x)$가 $\x^2$을 나눠야 하기 때문에 반드시 $p(\x)=\x$여야 함을 안다. 

따라서 이들이 정의하는 schememorphism

$$\Spec\pi_1:\Spec \mathbb{K}[\x]/(\x) \rightarrow \Spec \mathbb{K}[\x],\qquad \Spec\pi_2:\Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$$

을 생각하면, 연속함수로서 $\Spec\pi_1$은 $\Spec \mathbb{K}[\x]/(\x)$의 유일한 한 점 $(0)$을 $\Spec \mathbb{K}[\x]$의 한 점 $(\x)$으로, $\Spec\pi_2$는 $\Spec \mathbb{K}[\x]/(\x^2)$의 유일한 한 점 $(\x)$를 $\Spec \mathbb{K}[\x]$의 한 점 $(\x)$으로 보내는 것을 안다. 즉 연속함수로서 이들은 같은 함수를 정의하지만, 물론 $\Spec \mathbb{K}[\x]/(\x)$와 $\mathbb{K}[\x]/(\x^2)$는 scheme으로서 isomorphic하지 않다. 

</div>

당연히 우리가 바라는 structure sheaf는 대수적인 정보를 포함하는 $(\Spec\pi)\_\ast \mathscr{O}\_{\Spec A/\mathfrak{a}}$의 형태이며, 이것이 $\iota^{-1}\mathscr{O}\_{\Spec A}$와 어떠한 관계가 있는지는 이 글의 말미에서 살펴보게 된다.

## 닫힌 부분스킴

위에서 살펴본 것과 같이, 닫힌 부분스킴에 대한 우리의 모델은 canonical projection $\pi: A \rightarrow A/\mathfrak{a}$와, 이로부터 나오는 scheme morphism

$$(\Spec \pi, (\Spec\pi)^\sharp): \Spec A/\mathfrak{a} \rightarrow\Spec A$$

이다. 이 때 $\Spec\pi$는 $\Spec A$의 닫힌집합과 $\Spec A/\mathfrak{a}$ 사이의 homeomorphism을 주는 injective continuous map이고, $\Spec\pi^\sharp: \mathscr{O}\_{\Spec A} \rightarrow (\Spec\pi)\_\ast \mathscr{O}\_{\Spec A/\mathfrak{a}}$는 [§아핀스킴, ⁋명제 9](/ko/math/algebraic_geometry/affine_schemes#prop9)에서 얻어진다.

한편, ring homomorphism $\pi: A \rightarrow A/\mathfrak{a}$에서 가장 중요한 성질은 $\pi$가 surjective라는 것이며, 실제로 임의의 surjective ring homomorphism $\phi: A \rightarrow B$가 주어지면 first isomorphism theorem에 의하여

$$B=\im\phi\cong A/\ker\phi$$

이므로 이 성질이 $\pi$를 정확하게 characterize한다. 한편 [\[가환대수학\] §국소화의 성질들, ⁋명제 4](/ko/math/commutative_algebra/properties_of_localization#prop4)를 생각하면, $\pi$의 surjectivity는 임의의 prime ideal $\mathfrak{p}$에서의 localization $\pi\_\mathfrak{p}: A\_\mathfrak{p} \rightarrow (A/\mathfrak{a})\_{\mathfrak{p}}$이 surjective인지를 살펴보아 확인할 수 있으며 이는 기하적으로는 affine scheme $\Spec A$에서의 임의의 점 $\mathfrak{p}$에서의 stalk을 살펴보는 것과 같고, 따라서 [\[위상수학\] §층, ⁋명제 14](/ko/math/topology/sheaves#prop14)에 의해 $(\Spec\pi)^\sharp$이 surjective인 것과 같다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Scheme morphism $\iota: Z \rightarrow X$가 *closed embedding<sub>닫힌 몰입</sub>*이라는 것은 $\iota$가 연속함수로서 $Z$와 $X$의 닫힌집합 사이의 homeomorphism이고, sheaf morphism $\iota^\sharp: \mathscr{O}\_X \rightarrow \iota_\ast \mathscr{O}\_Z$가 surjective인 것이다.

</div>

연속함수 $\iota$에 대한 조건은 자명한 것이며, $\iota^\sharp$에 대한 직관 또한 기하적인 해석이 가능한데, 그것은 $Z$의 함수들, 더 정확하게는 $\iota(Z)$의 함수들은 모두 $X$의 함수를 $Z$로 제한하여 얻어진 것이어야 한다는 것이다. 혹은, 반대로 말하면 $Z$의 임의의 함수가 주어졌을 때 이를 $X$에서의 함수로 확장하는 것이 가능해야 한다는 것이다. 한편 만일 $\iota$가 open embedding이라면, $\iota^\sharp$는 isomorphism이어야 한다. 

이 정의는 자연스러운 것이지만, 우리가 앞선 글에서 정의한 scheme morphism의 성질들과는 약간 결이 다르다. 따라서 우리는 이와 동치인 다음 정의를 (증명없이) 사용한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Scheme morphism $\varphi: X \rightarrow Y$에 대하여 다음 두 조건이 동치이다.

1. $\varphi$가 closed embedding이다.
2. $\varphi$가 affine morphism이고, $Y$의 임의의 affine open subset $V\cong \Spec B$가 주어질 떄마다, 그 preimage $\varphi^{-1}(V)\cong \Spec A$에 대하여 $B \rightarrow A$가 surjective이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[The equivalence of two definitions of closed subscheme, Vakil's Ex 8.1.K](https://math.stackexchange.com/questions/1720902/the-equivalence-of-two-definitions-of-closed-subscheme-vakils-ex-8-1-k), Stack Exchange.

</details>

그럼 임의의 closed embedding은 국소적으로는 항상 위에서 살펴본 것과 같이 적당한 $\pi: A \rightarrow A/\mathfrak{a}$로부터 오는 것으로 생각할 수 있다. 특히 $Y$가 affine scheme $\Spec B$라 하면 위의 동치에 의해 $Y$로의 임의의 closed embedding $\varphi: X \rightarrow Y$는 정확하게 $B \rightarrow B/\mathfrak{b}$에 대응되는 것을 안다. 

## 닫힌 매장의 성질들

[명제 3](#prop3)를 받아들이고 나면 임의의 closed embedding은 항상 affine-local on target이고, closed embedding은 합성에 대해서도 닫혀있다는 것을 안다. 뿐만 아니라 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 임의의 closed embedding은 항상 finite morphism이다.

</div>

이는 정의에 의해 자명하며, [§스킴 사상의 성질들, ⁋예시 15](/ko/math/algebraic_geometry/properties_of_scheme_morphisms#ex15)에서 만든 (quasi-)finite morphism의 기하학적 직관에 비추어볼 때, 적어도 closed embedding은 항상 quasi-finite이어야 하는 것이 자명하고, 여기에서 더 나아가 finite이기도 하다는 기하적인 해석이 가능하다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 임의의 scheme $Z$에 대하여, $\mathscr{O}\_Z$의 subsheaf $\mathscr{I}$를 $Z$의 *ideal sheaf*라 부른다. 특별히 closed embedding $\iota: Z \rightarrow X$에 대하여, $\mathscr{O}\_X$의 subsheaf $\ker\iota^\sharp$를 $\iota$에 의해 정의되는 ideal sheaf라 부르고, 이를 $\mathscr{I}_{Z/X}$로 표기한다. 

</div>

즉, 다음의 exact seqeunce

$$0 \rightarrow \mathscr{I}_{Z/X} \rightarrow \mathscr{O}_X \rightarrow \iota_\ast \mathscr{O}_Z \rightarrow 0$$

이 존재한다. 따라서 $X$의 임의의 affine open subset $U=\Spec A$에서는

$$0 \rightarrow \mathscr{I}_{Z/X}(U) \rightarrow \mathscr{O}_X(U)\cong A \rightarrow \iota_\ast \mathscr{O}_Z(U) \rightarrow 0$$

이 되므로, $\mathscr{I}_{Z/X}(U)$는 $A$의 ideal이 되어 이 이름이 적절하다 할 수 있다. 

우리는 [명제 3](#prop3) 직후에 임의의 affine scheme $Y=\Spec B$의 closed subscheme은 정확하게 $B$의 ideal에 대응되는 것을 살펴보았다. 한편 임의의 scheme은 affine scheme을 붙여서 만들어지므로, 이러한 affine scheme들마다 ideal들이 정의되고, 이들이 적당한 gluing condition을 만족한다면 이를 통해 원래 scheme의 closed subscheme이 정의될 것이다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Scheme $X$의 임의의 affine open subset $\Spec A$마다, ideal $\mathscr{I}(A)\subseteq A$가 주어져있다고 하자. 만일 각각의 $f\in A$에 대하여, $A \rightarrow A_f$에 의해 isomorphism $\mathscr{I}(A_f)\cong \mathscr{I}(A)_f$가 유도된다면, 이들 데이터는 $X$의 유일한 closed subscheme $Z\hookrightarrow X$를 유도한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $X$를 affine open subset들 $\\{\Spec A\_i\\}$들로 덮자. 그럼 우리가 보여야 할 것은 임의의 $i,j$에 대하여, $\Spec A_i$에서 ideal $\mathscr{I}(A_i)$에 의해 정의되는 closed subscheme과 $\Spec A_j$에서 ideal $\mathscr{I}(A_j)$에 의해 정의되는 closed subscheme이 $\Spec A_i$와 $\Spec A_j$의 교집합에서 같은 closed subscheme을 정의한다는 것이다. 


우선 [§스킴의 위상구조, ⁋보조정리 11](/ko/math/algebraic_geometry/topology_of_schemes)로부터 우리는 $\Spec A_i$와 $\Spec A_j$의 교집합을 principal open subset들 

$$\Spec (A_i)_{f_i}\cong\Spec (A_j)_{f_j}$$

들로 덮을 수 있다. 이제 $\Spec A_i$에서 $\mathscr{I}(A_i)$가 정의하는 closed subscheme을 $D(f\_i)\cong\Spec (A\_i)\_{f\_i}$로 제한하면 $\mathscr{I}(A\_i)\_{f\_i}$이고, 주어진 가정에 의해 이는 $\mathscr{I}((A\_i)\_{f\_i})$와 isomorphic하며 이것은 $\mathscr{I}((A\_j)\_{f\_j})$와 같은 것이므로 이들을 붙여 closed subscheme $Z$를 만들 수 있다. 

</details>

이제 임의의 scheme $X$와 global section $s\in \Gamma(X, \mathscr{O}_X)$가 주어졌다 하자. 그럼 각각의 affine cover $U\cong\Spec A$에 대하여, $s\vert_U$는 $A$의 ideal $\mathscr{I}(A)=(s\vert_U)$를 정의하며 이렇게 정의된 $\mathscr{I}(A)$들은 [명제 6](#prop6)의 조건을 만족하는 것이 자명하다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Scheme $X$와 $X$의 global section $s\in \Gamma(X, \mathscr{O}\_X)$에 대하여, 위와 같이 정의된 scheme $Z(s)$를 $s$의 *vanishing scheme*이라 부른다.

</div>

더 일반적으로, global section들의 집합 $S$에 대하여 $Z(S)$를 어떻게 정의해야 하는지도 자명하며, 따라서 특별히 $X=\Spec A$이고 $S=\mathfrak{a}$가 $A$의 ideal인 경우 $Z(\mathfrak{a})$를 어떻게 정의해야 하는지도 자명하며, 이는 affine scheme $\Spec A/\mathfrak{a}$의 structure sheaf를 $\Spec\pi$를 통해 닫힌집합 $Z(\mathfrak{a})$에 옮겨준 것이다. 앞으로 $Z(\mathfrak{a})$는 항상 이러한 scheme structure가 주어져 있는 것으로 생각한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme morphism $\varphi: X \rightarrow Y$가 *locally closed embedding*이라는 것은 $Y$의 적당한 open subscheme $\iota:Z\hookrightarrow Y$가 존재하여, 다음의 canonical decomposition

$$X\overset{\varphi\vert^Z}{\longrightarrow}Z\overset{\iota}{\longrightarrow} Y$$

을 통해 $\varphi\vert^Z$가 closed embedding인 것이다. 

</div>

그럼 [명제 4](#prop4)에 의하여, 임의의 locally closed embedding은 항상 locally of finite type인 것을 안다. 

## 스킴 사상의 상

이제 우리는 스킴 사상의 상을 정의한다. 당연히 임의의 scheme morphism $\varphi: X \rightarrow Y$가 주어졌을 떄, 우리는 그 image $\im\varphi$ 또한 스킴 구조가 주어지기를 바랄 것이다. 그러나 위상공간 $Y$의 부분집합으로서 $\im\varphi$는 열린집합도, 닫힌집합도 아닐 수 있으므로 $Y$의 structure sheaf를 이용하여 $\im\varphi$에 structure sheaf를 정의하는 것은 요원해보인다. 

이에 대한 해결책은 $\varphi$의 image를 포함하는 closed subscheme 중 가장 작은 것을 $\varphi$의 *scheme-theoretic image*로 정의하는 것이다. 이를 위해서는 우선 $X$의 closed subscheme이 다른 closed subscheme보다 작다는 것이 무엇인지를 살펴보아야 한다.

<div class="proposition" markdown="1">

<ins id="lem9">**보조정리 9**</ins> 두 closed embedding $\iota_1: Z_1 \rightarrow X$, $\iota_2: Z_2 \rightarrow X$가 주어졌다 하자. 그럼 적당한 scheme morphism $\varphi: Z_1 \rightarrow Z_2$가 존재하여 $\iota_1=\iota_2\circ\varphi$를 만족하는 것은 $\mathscr{I}\_{Z\_2/X}\subseteq \mathscr{I}\_{Z\_1/X}$인 것과 동치이다. 이 경우 $\varphi$는 closed embedding이 된다. 

</div>

이는 affine open subset $\Spec A$에서 보면 두 closed embedding은 각각

$$A \rightarrow A/\mathscr{I}_{Z_1/X}(A),\qquad A \rightarrow A/\mathscr{I}_{Z_2/X}(A)$$

에 대응되며, 위의 조건을 만족하는 $\varphi$가 존재하는 것은 ring homomorphism $A \rightarrow A/ \mathscr{I}\_{Z\_1/X}(A)$이 $A \rightarrow A/ \mathscr{I}\_{Z\_2/X}(A)$로 factor through해야 하는 것과 같은 것이며 이것이 다시 $\mathscr{I}\_{Z\_2/X}(A)\subseteq \mathscr{I}\_{Z\_1/X}(A)$와 동치이기 때문이다. 

Scheme $X$의 두 closed subscheme $Z_1,Z_2$에 대하여, closed embedding $\varphi:Z_1 \rightarrow Z_2$가 존재한다면 $Z_1$이 $Z_2$보다 <em_ko>작은</em_ko> closed subscheme인 것으로 생각하자. 

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> 임의의 scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 그럼 $\varphi$의 image가 closed subscheme $\iota: Z \rightarrow Y$에 *포함된다*는 것은 다음의 합성

$$\mathscr{I}_{Z/Y} \rightarrow \mathscr{O}_Y \rightarrow \varphi_\ast \mathscr{O}_X$$

이 $0$이 되는 것이다. 이 때, $\varphi$의 image를 포함하는 $Y$의 closed subscheme 중 가장 작은 것을 $\varphi$의 *scheme-theoretic image*라 부른다.

</div>

만일 위의 식에서 $Y$가 affine scheme $\Spec B$라면, $Y$의 closed subscheme은 $B$의 ideal $\mathfrak{b}$에 의해 완전하게 결정된다. 따라서 이 경우, $Y$의 scheme-theoretic image는 $\mathscr{O}\_Y \rightarrow \varphi\_\ast \mathscr{O}\_X$의 kernel이 정의하는 $Y$의 closed subscheme이 될 것이다. 더 특수한 경우로 만일 $X$도 affine scheme이라면, $\mathscr{O}\_Y \rightarrow \varphi\_\ast \mathscr{O}\_X$는 ring homomorphism $\phi$로부터 나오는 것이므로 명시적인 계산을 해 줄 수 있다.

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> [예시 1](#ex1)에서 살펴본 closed embedding의 예시 $\Spec\pi: \Spec \mathbb{K}[\x]/(\x^2) \rightarrow \Spec \mathbb{K}[\x]$를 약간 변형한 예시를 살펴보자. 이 예시에서는 구별을 위해 $\mathbb{K}[\x]/(\x^2)$를 $\mathbb{K}[\epsilon]/(\epsilon^2)$으로 적는다. 

우리는 [\[대수적 구조\] §대수, ⁋명제 8](/ko/math/algebraic_structures/algebras#prop8)에 의하여 $\mathbb{K}$-algebra homomorphism $\phi:\mathbb{K}[\x_1,\ldots, \x_n] \rightarrow \mathbb{K}[\epsilon]/(\epsilon^2)$는 $\x_i$의 값에 의해 완전히 결정된다는 것을 안다. 따라서 $\phi(\x_i)=a_i+b_i\epsilon$이라 하자. 만일 $0$이 아닌 $b_i$가 존재한다면 $\phi$가 surjective임을 보일 수 있고, 따라서 $\Spec\phi$는 closed embedding이며 $\Spec\phi$의 scheme-theoretic image는 $\Spec\phi$가 정의하는 closed subscheme 자기 자신이다. 구체적으로 이를 써 보면 $\Spec\phi$는 $\mathbb{K}[\epsilon]/(\epsilon^2)$의 유일한 prime ideal $(\epsilon)$을 $\Spec \mathbb{K}[\x_1,\ldots, \x_n]$의 prime ideal

$$(\Spec\phi)(\epsilon)=\phi^{-1}(\epsilon)=\left(\frac{\x_1}{b_1}-\frac{a_1}{b_1},\ldots \frac{\x_n}{b_n}-\frac{a_n}{b_n}\right)=(\x_1-a_1,\ldots, \x_n-a_n)$$

로 보낸다. 즉 연속함수로서 $\Spec\phi$는 한점공간 $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$을 $\mathbb{A}^n$의 한 점 $(a_1,\ldots, a_n)$으로 보낸다.

기하적으로 $\Spec\phi$는 $\mathbb{A}^n$의 한 점 $(a_1,\ldots, a_n)$에서의 tangent vector $(b_1,\ldots, b_n)$에 대응된다. 이는 $\mathbb{A}^n$의 임의의 함수 $f\in \mathbb{K}[\x_1,\ldots, \x_n]$의 점 $(a_1,\ldots, a_n)$에서 벡터 $(b_1,\ldots, b_n)$의 방향으로의 방향미분이 정확히 $\phi(f)$로 주어진다는 것으로부터 확인할 수 있다. 더 일반적으로 $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$ 대신 $\Spec \mathbb{K}[\epsilon]/(\epsilon^k)$를 생각하면 우리는 $k-1$차 미분계수까지 볼 수 있게 된다. 

</div>

위의 예시에서 $X$가 affine scheme이라고 가정하기는 하였지만, $\varphi^\sharp:\mathscr{O}\_Y \rightarrow \varphi\_\ast \mathscr{O}\_X$는 어차피 scheme morphism $\varphi$가 포함하고 있는 정보이므로 여기에는 새로울 것이 없다. 차이는 $Y$를 일반적인 scheme으로 일반화할 때 나오게 되는데, $Y$의 임의의 affine open subset $V=\Spec B$가 주어질 때마다 ideal

$$\mathscr{I}(V):=\ker(\varphi^\sharp(V))\subset B$$

가 $V$의 closed subscheme을 정의하지만, 이들을 이어붙여 $Y$ 전체에서 정의된 단일한 closed subscheme을 만들 수 있는지는 다른 문제이기 때문이다. 물론 우리는 이를 위해 [명제 6](#prop6)을 사용할 것이며, 이 가정은 특히 $X$가 reduced scheme이거나 $\varphi$가 quasi-compact일 경우 만족된다.

<div class="proposition" markdown="1">

<ins id="cor12">**따름정리 12**</ins> Scheme morphism $\varphi: X \rightarrow Y$가 주어졌다 하자. 만일 $X$가 reduced이거나, $\varphi$가 quasi-comapct라면 위에서 정의한 ideal sheaf $\mathscr{I}$는 [명제 6](#prop6)의 조건을 만족하고 따라서 $\mathscr{I}$는 $Y$의 closed subscheme을 정의하며 이것이 $\varphi$의 scheme-theoretic image가 된다.

</div>

위의 조건을 가정하고 $\varphi$의 image를 각각의 affine open subset에서 확인해보면 $\varphi$의 scheme-theoretic image는 $\varphi$의 (연속함수로서의) image의 closure 위에 structure sheaf가 정의된 형태임을 확인할 수 있다. 

[따름정리 12](#cor12)의 가정이 없을 경우 이러한 일은 일어나지 않는다.

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> Scheme $X$를 다음의 식

$$X=\coprod_{k\geq 0} \Spec \mathbb{K}[\epsilon]/(\epsilon^k)$$

으로 정의하고 $Y=\Spec \mathbb{K}[\x]$이라 하자. 이제 $X$의 각각의 component마다 $\x\mapsto \epsilon$을 통해 scheme morphism $X \rightarrow Y$를 정의할 수 있다. 그럼 [예시 11](#ex11)으로부터 우리는 $X \rightarrow Y$의 (연속함수로서의) image는 한 점 $0\in \mathbb{A}^1$인 것을 안다. 

그러나 scheme morphism $\varphi:X \rightarrow Y$의 scheme-theoretic image는 $0$이 아니다. 이를 위해 structure sheaf들 사이의 morphism $\varphi^\sharp:\mathscr{O}\_Y \rightarrow \varphi\_\ast \mathscr{O}\_X$를 관찰하자. 그럼 $\mathcal{O}\_Y$의 원소 $f$가 $\varphi^\sharp(f)=0$을 만족하기 위해서는 임의의 $k$에 대하여 $f$의 $k$차 근사식이 $0$이 되어야 하므로, 반드시 $f=0$이어야 한다. 즉, $\mathscr{I}\_{Z/Y}$는 $0$이 되어야 하고 이로부터 $\varphi$의 scheme-theoretic image는 자기 자신임을 안다.

</div>

## 닫힌집합 위에 정의된 기약스킴구조

이 글의 서두에서 우리는 affine scheme $\Spec A$의 임의의 닫힌집합 $Z(\mathfrak{a})$ 위에 두 개의 structure sheaf $(\Spec\pi)\_\ast \mathscr{O}\_{\Spec A/\mathfrak{a}}$ 그리고 $\iota^{-1} \mathscr{O}\_{\Spec A}$를 정의할 수 있었다. 이 중 $(\Spec\pi)\_\ast \mathscr{O}\_{\Spec A/ \mathfrak{a}}$를 우리는 $Z(\mathfrak{a})$ 위에 정의된 올바른 스킴 구조로 생각하기로 하였다. 이제 우리는 $\iota^{-1} \mathscr{O}\_{\Spec A}$에 대해 살펴본다.

더 일반적으로 임의의 scheme $Y$와 $Y$의 닫힌집합 $X$를 생각하자. 그럼 $Y$의 임의의 열린집합 $\Spec B$에 대하여, $\Spec B$의 닫힌집합 $X\cap \Spec B$는 [§스펙트럼, ⁋정리 15](/ko/math/algebraic_geometry/spectrums#thm15)에 의하여 
$B$의 radical ideal $\mathfrak{b}$에 대해 $Z(\mathfrak{b})$의 꼴로 쓸 수 있다. 뿐만 아니라, $\mathfrak{b}$는 정의에 의하여 $X\cap \Spec B= Z(\mathfrak{b}')$이도록 하는 $B$의 ideal들 중 가장 큰 것이므로 [보조정리 9](#lem9)에 의하여 $X\cap \Spec B$에 줄 수 있는 closed subscheme 구조 중 가장 작은 것이다.

<div class="definition" markdown="1">

<ins id="def14">**정의 14**</ins> Scheme $Y$의 임의의 닫힌집합 $X$에 대하여, $X$ 위에 앞에서 정의한 scheme 구조를 준 것을 *reduced scheme structure*라 부르고 $X^\red$으로 적는다. 

</div>

그럼 특히 $X=Y$인 경우, 임의의 affine subset $\Spec B$에 대하여 $\Spec B=Z(0)$이라 적으면 $\mathfrak{b}=\sqrt{(0)}$이 되어 $B/\sqrt{(0)}$은 reduced ring이 된다. 한편 위에서 살펴본 sheaf morphism

$$\iota^{-1}\mathscr{O}_{\Spec A} \rightarrow (\Spec\pi\vert^{Z(\mathfrak{a})})_\ast \mathscr{O}_{\Spec A/\mathfrak{a}}$$

은 단순히 [보조정리 9](#lem9)에서 얻어지는 canonical한 scheme morphism이다.

---
**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  

--- 