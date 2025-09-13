---

title: "합곱"
excerpt: ""

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/cup_products
header:
    overlay_image: /assets/images/Math/Algebraic_Topology/Cup_products.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_topology-ko"

date: 2025-09-12
last_modified_at: 2025-09-12
weight: 7

---

앞서 cohomology를 도입하며 우리는 cohomology의 가장 큰 장점 중 하나가 이 위에 자연스럽게 정의된 곱셈구조라 하였다. 그렇다면 이 구조가 왜 호몰로지에서는 보이지 않았는지 또한 합리적인 의문일 것인데, 이번 글에서 이 곱셈구조를 정의하면, 본질적으로 cohomology가 contravariant functor이기 때문이라는 것이 드러난다.

## 코호몰로지의 외적

Commutative ring $A$를 고정하고, $A$-module들의 chain complex $C_\bullet,D_\bullet$이 주어졌다 하자. 이들의 dual sequence

$$(C^\vee)^\bullet=\Hom_A(C_\bullet,A),\qquad (D^\vee)^\bullet=\Hom_A(D_\bullet,A)$$

그리고 

$$((C\otimes D)^\vee)^\bullet=\Hom_A((C\otimes D)_\bullet,A)$$

에 대하여, 우리는 우선 

$$\times:(C^\vee\otimes D^\vee)^\bullet\rightarrow ((C\otimes D)^\vee)^\bullet$$

을 정의한다. 이를 위해서는 좌변의 simple tensor $\phi\otimes \psi$를 받아 $(C\otimes D)\_\bullet$에서 $A$의 함수를 하나 대응시켜주면 되고, 이는 다시 $(C\otimes D)\_\bullet$의 simple tensor에서의 값으로 정의된다. 만일 $\phi\in (C^\vee)^p,\psi\in (D^\vee)^q$라면, 우리는 정확히 $C_p\otimes D_q$에 속하는 simple tensor $\alpha\otimes \beta$에 대해서만

$$(\phi\times\psi):(C\otimes D)_\bullet \rightarrow A;\qquad (\alpha\otimes \beta)\mapsto (-1)^{\deg(\alpha)\deg(\beta)}\phi(\alpha)\psi(\beta)$$

이고, 나머지에 대해서는 $0$인 함수로 이 대응을 정의한다. 그럼 어렵지 않게 이것이 cochain complex들 사이의 morphism이며 따라서 $\times$는 cohomology의 함수

$$\times: H^\bullet(C^\vee\otimes D^\vee)\rightarrow (H(C^\vee)\otimes H(D^\vee))^\bullet\rightarrow H^\bullet((C\otimes D)^\vee)$$

를 정의한다.

이제 두 위상공간 $X,Y$의 $A$-valued chain

$$C_\bullet(X;A),\qquad C_\bullet(Y;A)$$

들이 주어졌다 하자. $C_\bullet=C_\bullet(X;A), D_\bullet=C_\bullet(Y;A)$로 두고 위의 cochain map을 취하면 우리는 이를 [§코호몰로지](/ko/math/algebraic_topology/cohomology)의 Alexander-Whitney map $\AW$가 유도하는 함수와 합성하여 다음의 cochain map

$$(C^\vee(X;A)\otimes C^\vee(Y;A))^\bullet \rightarrow \Hom_A(C_\bullet(X;A)\otimes C_\bullet(Y;A),A)\rightarrow \Hom_A(C_\bullet(X\times Y);A)=(C^\vee)^\bullet(X\times Y)$$

을 얻고, 다시 이를 cohomology 레벨로 내리면 각각의 $(p,q)$마다 다음의 $A$-module homomorphism

$$\times:H^p(X;A)\otimes_A H^q(Y;A)\rightarrow H^{p+q}(X\times Y;A)$$

을 얻는다.

## 합곱의 정의와 기본 성질들

이제 우리는 합곱을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Commutative ring $A$와 위상공간 $X$에 대하여, 다음의 합성

$${\smile}:H^\bullet(X;A)\otimes_A H^\bullet(X;A)\overset{\times}{\longrightarrow}H^\bullet(X\times X)\overset{\Delta^\ast}{\longrightarrow} H^\bullet(X)$$

을 $H^\bullet(X;A)$ 위의 *cup product<sub>합곱</sub>*이라 부른다. 

</div>

이 단계에서 cup product가 왜 homology에서는 명시적으로 보이지 않았는지가 나타난다. Eilenberg-Zilber map을 사용하면

$$H_p(X;A)\otimes_A H_q(X;A)\rightarrow H_{p+q}(X\times X;A)$$

까지는 만들 수 있을 것이나, diagonal map $\Delta:X\rightarrow X\times X$에 homology functor를 취하는 것은 covariant이므로 방향이 맞지 않을 것이기 때문이다.

명시적으로, 임의의 $\alpha\in H^p(X;A)$, $\beta\in H^q(X;A)$에 대하여, $\alpha\smile\beta\in H^{p+q}(X;A)$는 임의의 chain $\sigma:\Delta^{p+q}\rightarrow X$ 위에서 다음의 식

$$(\alpha\smile\beta)(\sigma)=(\Delta^\ast\AW^\ast(\alpha\times\beta))(\sigma)=(\alpha\times\beta)(\AW(\Delta(\sigma)))=(-1)^{pq}\alpha(\text{front face of $\sigma$})\beta(\text{back face of $\sigma$})$$

으로 주어진다. 이 명시적인 계산에서 알 수 있듯, de Rham cohomology에서 cup product는 아주 익숙한 것으로, differential form들의 wedge product에 해당하는 것이다.

그럼 그 이름에서 짐작할 수 있듯, cup product는 cohomology ring 위의 곱셈구조를 정의한다. 그런데 $H^\bullet(X;A)$는 graded ring이기도 하므로, 이 위에 정의된 곱셈의 commutativity를 논할 때는 다음과 같이 주의를 기울여야 한다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 위상공간 $X$와 commutative ring $A$를 고정하자. 그럼 

$$(H^\bullet(X;A), {\smile}, 1)$$

은 *grade*-commutative, $\mathbb{N}$-graded $A$-algebra를 이룬다. 여기서 $1\in H^0(X;A)$는 $X$의 임의의 $\Delta$-simplex를 모두 $1\in A$로 보내는 cocycle이다.

</div>

즉, homogeneous cycle들 $\alpha\in H^p(X;A),\beta\in H^q(X;A),\gamma\in H^r(X;A)$에 대하여, 

- (Unit) $1\smile\alpha=\alpha\smile 1=\alpha$
- (Associativity) $(\alpha\smile\beta)\smile\gamma=\alpha\smile(\beta\smile\gamma)$
- (Grade-commutativity) $\alpha\smile\beta=(-1)^{pq}\beta\smile\alpha$

이 성립한다. 이를 보이는 것은 [acyclic models theorem](https://en.wikipedia.org/wiki/Acyclic_model)을 통하면 편하지만, 우리는 이를 소개하지 않기로 하였으므로 이 명제의 증명은 

## 합곱의 함자적 성질들

위에서 증명한 성질은 functor $H^\bullet(-;A)$의 대상들이, 처음 정의할 때는 $\lMod{A}$로의 functor로 정의하였지만, 최종적으로는 $\gr_{\mathbb{N}}\Alg{A}$에 도착한다는 것을 보여준다. 그렇다면 $H^\bullet(-;A)$가 $\Top$에서 $\gr_\mathbb{N}\Alg{A}$로의 functor인지를 궁금해하는 것이 당연하다. 