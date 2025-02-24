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

[§스킴, ⁋정의 1](/ko/math/algebraic_geometry/schemes#def1) 이후에 우리는 affine scheme $\Spec A$에 대하여, 임의의 원소 $f$가 open affine subscheme $D(f)\cong \Spec A_f$를 정의하는 것을 살펴보았다. 이를 보이는 것은 단순히 $D(f)$가 $\Spec A$의 열린집합이라는 것 뿐만 아니라, 이 열린집합 $D(f)$에 정의할 수 있는 두 개의 ringed space 구조 $\mathscr{O}\_{\Spec A}\vert\_{D(f)}$와 $\mathscr{O}\_{\Spec A_f}$가 서로 같다는 것까지 보이는 것이며, 이를 비교할 수 있는 morphism을 얻기 위해 우리는 자연스러운 sheaf morphism $(\Spec \epsilon)^\sharp: \mathscr{O}_{\Spec A} \rightarrow (\Spec \epsilon)\_\ast \mathscr{O}\_{\Spec A_f}$에 다음의 adjoint

$$\Hom_{\Sh(\Spec A)}(\mathscr{O}_{\Spec A}, (\Spec \epsilon)_\ast \mathscr{O}_{\Spec A_f})\cong\Hom_{\Sh(\Spec A_f)}((\Spec\epsilon)^{-1}\mathscr{O}_{\Spec A}, \mathscr{O}_{\Spec A_f})$$

을 적용한 후, [§스펙트럼, ⁋명제 9](/ko/math/algebraic_geometry/spectrums#prop9)의 셋째 결과에 의해 $\Spec \epsilon$은 open immersion $D(f)\hookrightarrow \Spec A$이므로 $(\Spec\epsilon)^{-1}\mathscr{O}_{\Spec A}$는 그냥 $\mathscr{O}\_{\Spec A}\vert\_{D(f)}$에 불과하다는 사실을 이용했다. 

한편 [§스펙트럼, ⁋명제 9](/ko/math/algebraic_geometry/spectrums#prop9)의 둘째 결과에 의해, affine scheme $\Spec A$와 $A$의 ideal $\mathfrak{a}$가 주어지면 $\Spec$ functor를 통해 

$$\Spec\pi: \Spec A/\mathfrak{a}\rightarrow \Spec A$$

가 주어지고, 이 때 $\Spec\pi$는 injective이며 그 image는 $Z(\mathfrak{a})$가 된다는 것을 안다. 이 경우에도 위에서와 마찬가지로 $(\Spec\pi)^\sharp: \mathscr{O}\_{\Spec A} \rightarrow (\Spec\pi)_\ast \mathscr{O}\_{\Spec A/\mathfrak{a}}$ 또한 잘 정의될 것이나, 다른 점은 $(\Spec\pi)^{-1}\mathscr{O}\_{\Spec A}$를 표현할 수 있는 언어가 아직 존재하지 않는다는 것이다. 이번 글에서 우리는 closed subscheme을 정의하여 이를 해결한다.

## 닫힌 부분스킴

Scheme $X$의 closed subscheme은 당연히 위상공간으로서는 $X$의 닫힌집합이 될 것이다. 즉 $X$로의 *closed immersion*은 우선 위상공간에서 보았을 때는 그 image가 $X$의 닫힌집합이 되는 injective continuous map $\iota:Z\hookrightarrow X$이다. 그러나 위에서와 마찬가지로 이것이 subscheme이기 위해서는 structure sheaf에도 적절한 종류의 조건이 주어져야 한다. 이는 structure sheaf를 공간 위에서 정의된 함수들의 sheaf로 생각하는 우리의 직관을 활용하면 쉽게 줄 수 있는데, 그것은 sheaf morphism $\iota^\sharp: \mathscr{O}\_X \rightarrow \iota_\ast \mathscr{O}\_Z$가 surjective여야 한다는 것이다. 즉 $Z$의 함수들, 더 정확하게는 $\iota(Z)$의 함수들은 모두 $X$의 함수를 $Y$로 제한하여 얻어진 것이어야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme morphism $\iota: Z \rightarrow X$가 *closed immersion<sub>닫힌 몰입</sub>*이라는 것은 $\iota$가 연속함수로서 $Z$와 $X$의 닫힌집합 사이의 homeomorphism이고, sheaf morphism $\iota^\sharp: \mathscr{O}\_X \rightarrow \iota_\ast \mathscr{O}\_Z$가 surjective인 것이다.

Scheme $X$의 *closed subscheme*은 closed immersion들 위에 다음의 equivalence relation

$$(\iota: Z \rightarrow X)\sim(\iota': Z' \rightarrow X)\iff \text{there exists an isomorphism $\psi: Z' \rightarrow Z$ such that $\iota'=\iota\circ\psi$}$$

을 주었을 때의 equivalence class로 정의한다.

</div>

이 정의는 자연스러운 것이지만, 우리가 앞선 글에서 정의한 scheme morphism의 성질들과는 약간 결이 다르다. 따라서 우리는 이와 동치인 다음 정의를 (증명없이) 사용한다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Scheme morphism $\varphi: X \rightarrow Y$에 대하여 다음 두 조건이 동치이다.

1. $\varphi$가 closed immersion이다.
2. $\varphi$가 affine morphism이고, $Y$의 임의의 affine open subset $V\cong \Spec B$가 주어질 떄마다, 그 preimage $\varphi^{-1}(V)\cong \Spec A$에 대하여 $B \rightarrow A$가 surjective이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[The equivalence of two definitions of closed subscheme, Vakil's Ex 8.1.K](https://math.stackexchange.com/questions/1720902/the-equivalence-of-two-definitions-of-closed-subscheme-vakils-ex-8-1-k), Stack Exchange.

</details>

그럼 surjective ring homomorphism $\pi:B \rightarrow A$는 first isomorphism theorem에 의하여 항상

$$B \rightarrow \im(\pi)\cong B/\ker\pi$$

와 identify할 수 있으므로 closed immersion은 항상 





우리는 임의의 closed immersion이 항상 국소적으로는 이러한 꼴임을 보인다. 우선 다음의 명제를 증명하자. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 scheme $X$와 affine scheme $\Spec A$, 그리고 scheme morphism $\iota: X \rightarrow \Spec A$에 대하여 다음 두 조건이 동치이다.

1. $\iota$는 closed immersion이다. 
2. $\Spec A$의 임의의 에 대하여 affineness? [link](https://math.stackexchange.com/questions/1720902/the-equivalence-of-two-definitions-of-closed-subscheme-vakils-ex-8-1-k)

</div>
<details open class="proof" markdown="1">
<summary>증명</summary>

우선 [§아핀스킴, ⁋정리 13](/ko/math/algebraic_geometry/affine_schemes#thm13)과 scheme morphism의 정의로부터

$$\Hom_\Sch(X, \Spec A)=\Hom_\text{LocallyRingedSpace}(X, \Spec)\cong\Hom_{\cRing}(A, \Gamma(X, \mathscr{O}_X))$$

이므로 $\iota$가 주어진 것은 ring homomorphism $\iota^\sharp(A): A \rightarrow \Gamma(X, \mathscr{O}_X)$가 주어진 것과 같다. 이 때 kernel $\ker\iota^\sharp(A)$를 $\mathfrak{a}$라 적고 canonical decomposition을 사용하면

$$\iota^\sharp(A): A \twoheadrightarrow A/\mathfrak{a} \hookrightarrow \Gamma(X, \mathscr{O}_X)$$

을 얻는다. 이제 여기에 다시 $\Spec$을 취하여 위의 adjoint를 거꾸로 따라가면 $\iota$의 decomposition

$$\iota: X \rightarrow \Spec (A/\mathfrak{a}) \rightarrow \Spec A$$

을 얻는다. 

</details>

임의의 closed immersion $\iota: Z \rightarrow X$를 생각하자. 그럼 $X$는 affine open covering $U_i=\Spec A_i$를 가지므로, 이를 통해 

$$\iota\vert_{\iota^{-1}(U_i)}: \iota^{-1}(U_i) \rightarrow U_i$$

를 생각할 수 있다. 만일 $\iota\vert\_{\iota^{-1}(U\_i)}$들이 모두 closed immersion이라면, $\iota(Z)$는 $U_i$들 각각에서 closed이므로 $X$ 전체에서도 closed이며 $\iota^\sharp$의 surjectivity는 stalk에서 체크할 수 있으므로 $\iota$가 closed immersion이 된다. 



이를 증명하기 위해 준비작업이 필요하다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 scheme $Z$에 대하여, $\mathscr{O}\_Z$의 subsheaf $\mathscr{I}$를 $Z$의 *ideal sheaf*라 부른다. 특별히 closed immersion $\iota: Z \rightarrow X$에 대하여, $\mathscr{O}\_X$의 subsheaf $\ker\iota^\sharp$를 $\iota$에 의해 정의되는 ideal sheaf라 부르고, 이를 $\mathscr{I}_{Z/X}$로 표기한다. 

</div>

즉, 다음의 exact seqeunce

$$0 \rightarrow \mathscr{I}_{Z/X} \rightarrow \mathscr{O}_X \rightarrow \iota_\ast \mathscr{O}_Z \rightarrow 0$$

이 존재한다. 따라서 $X$의 임의의 affine open subset $U=\Spec A$에서는

$$0 \rightarrow \mathscr{I}_{Z/X}(U) \rightarrow \mathscr{O}_X(U)\cong A \rightarrow \iota_\ast \mathscr{O}_Z(U) \rightarrow 0$$

이 되므로, $\mathscr{I}_{Z/X}(U)$는 $A$의 ideal이 되므로 이 이름이 적절하다. 

한편, [정의 1](#def1)의 closed immersion은 