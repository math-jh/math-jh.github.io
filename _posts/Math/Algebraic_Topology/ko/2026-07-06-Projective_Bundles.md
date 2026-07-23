---
title: "사영다발과 Leray–Hirsch 정리"
description: "벡터다발의 사영다발을 도입하고, Leray–Hirsch 정리로 그 코호몰로지가 밑공간의 코호몰로지 위의 자유가군임을 보인 뒤, 이를 반복하여 splitting principle을 얻는다."
excerpt: "Leray–Hirsch 정리와 splitting principle"

categories: [Math / Algebraic Topology]
permalink: /ko/math/algebraic_topology/projective_bundles
sidebar: 
    nav: "algebraic_topology-ko"

date: 2026-07-06
weight: 11.5

published: false

drift_needed: true

---

## Leray–Hirsch 정리

[§코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10)은 곱공간 $X\times Y$의 cohomology를 두 인자의 cohomology의 tensor product로 계산해 주었다. Fiber bundle $\pi:E\rightarrow B$는 밑공간 $B$ 위에 fiber $F$를 비틀어 붙인 뒤틀린 곱으로, 국소적으로는 $U\times F$의 꼴이지만 전역적으로는 그렇지 않을 수 있다. 그럼에도 전공간의 cohomology $H^\bullet(E)$가 곱공간에서와 마찬가지로 밑공간과 fiber의 cohomology만으로 결정되는 경우가 있는데, Leray–Hirsch 정리는 이를 보장하는 충분조건을 준다. 그 조건은 fiber의 cohomology를 이루는 class들이 전공간 위의 전역적인 class의 restriction으로 실현되는 것이다.

우리가 이 정리를 사용하는 주된 목적은 splitting principle이다. [§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)에서 보았듯 line bundle의 Chern class는 first Chern class 하나로 완전히 통제되고 Whitney 합에 대해서도 단순하게 행동하므로, rank가 높은 bundle의 Chern class 계산은 그 bundle을 line bundle들의 합으로 쪼갤 수 있을 때 크게 간단해진다. 임의의 vector bundle이 실제로 line bundle들의 합인 것은 아니지만, Leray–Hirsch 정리를 아래에서 구성할 projective bundle에 적용하면 cohomology 계산에 관한 한 언제나 그렇게 취급해도 좋다는 것이 splitting principle의 내용이다.

여기서 fiber bundle이란 [§호모토피의 계산, ⁋참고 5](/ko/math/algebraic_topology/fibrations#rmk5)에서와 같이 밑공간이 열린집합들로 덮여 각 $U$ 위에서 $\pi^{-1}(U)$가 $U\times F$와 자연스럽게 homeomorphic한, 국소적으로 자명한 사상을 뜻한다. 이러한 $U$를 *trivializing open*이라 부르자.

::: 정리 1 (Leray–Hirsch)
Paracompact 밑공간 $B$ 위의 fiber bundle $\pi:E\rightarrow B$의 fiber $F$에 대하여, $H^\bullet(F;\mathbb{Z})$가 유한 rank의 자유 abelian group이라 하자. 만일 class들 $a_1,\ldots,a_r\in H^\bullet(E;\mathbb{Z})$이 존재하여 각 fiber로의 restriction $a_1\vert_F,\ldots,a_r\vert_F$이 $H^\bullet(F;\mathbb{Z})$의 basis를 이룬다면, $H^\bullet(E;\mathbb{Z})$은 $a_1,\ldots,a_r$을 basis로 하는 $H^\bullet(B;\mathbb{Z})$ 위의 자유가군이다.
:::

즉, 각 원소 $\xi\in H^\bullet(E)$는 $\xi=\sum_j\pi^\ast(\alpha_j)\smile a_j$의 꼴로 밑공간의 class $\alpha_j\in H^\bullet(B)$을 계수로 하여 유일하게 적힌다. 이를 morphism의 언어로 다시 적으면, $a_j\vert_F$이 $H^\bullet(F)$의 basis이므로 이들로 $H^\bullet(F)$를 식별하여 얻는

$$\Phi:H^\bullet(B)\otimes_{\mathbb{Z}}H^\bullet(F)\rightarrow H^\bullet(E),\qquad \Phi\bigl(\alpha\otimes(a_j\vert_F)\bigr)=\pi^\ast\alpha\smile a_j$$

가 $H^\bullet(B)$-가군의 isomorphism이라는 것이다.

::: 증명
열린집합 $U\subseteq B$에 대하여 $E_U=\pi^{-1}(U)$라 쓰고, 같은 식으로 정의된 morphism

$$\Phi_U:H^\bullet(U)\otimes H^\bullet(F)\rightarrow H^\bullet(E_U),\qquad \Phi_U\bigl(\alpha\otimes(a_j\vert_F)\bigr)=\pi^\ast\alpha\smile a_j\vert_{E_U}$$

을 생각하자. $a_j\vert_{E_U}$은 여전히 각 fiber로 제한하면 basis를 주므로, 우리가 보일 것은 $U=B$에서 $\Phi_B=\Phi$가 isomorphism이라는 것이다. 이를 $B$의 유한 trivializing covering의 크기에 대한 귀납으로 보인다.

우선 $U$가 하나의 trivializing open인 경우, $E_U\cong U\times F$이고 $\pi$는 projection이 된다. $H^\bullet(F)$가 자유이므로 [§코호몰로지, ⁋따름정리 10](/ko/math/algebraic_topology/cohomology#cor10)에 의하여

$$H^\bullet(U\times F)\cong H^\bullet(U)\otimes H^\bullet(F)$$

이 성립하고, 따라서 우변은 $\{1\times(a_k\vert_F)\}_k$을 basis로 하는 유한 rank의 자유 $H^\bullet(U)$-가군이다. 좌변 $H^\bullet(U)\otimes H^\bullet(F)$ 또한 $\{1\otimes(a_k\vert_F)\}_k$을 basis로 하는 같은 rank의 자유 $H^\bullet(U)$-가군이며, $\Phi_U$는 이를 원소 $a_j\vert_{E_U}\in H^\bullet(U\times F)$들로 보낸다. 그런데 $a_j\vert_{E_U}$을 한 fiber $\{u\}\times F$로 제한하면 $a_j\vert_F$이 되므로, Künneth 분해에서

$$a_j\vert_{E_U}=1\times(a_j\vert_F)+(\text{$U$의 차수가 양인 항들})$$

이 성립한다. 곧 basis $\{1\times(a_k\vert_F)\}$에 대한 $\{a_j\vert_{E_U}\}$의 전이행렬은 대각성분이 $1$이고 밑공간 degree를 올리는 방향으로만 어긋나는 삼각행렬이므로 $H^\bullet(U)$ 위에서 가역이다. 따라서 $\Phi_U$는 isomorphism이다.

다음으로 $U=U'\cup U''$이고 $\Phi_{U'}$, $\Phi_{U''}$, $\Phi_{U'\cap U''}$이 모두 isomorphism이라 하자. $E_{U'\cup U''}=E_{U'}\cup E_{U''}$이고 $E_{U'}\cap E_{U''}=E_{U'\cap U''}$이므로, 밑공간과 전공간에서 [§코호몰로지, ⁋명제 6](/ko/math/algebraic_topology/cohomology#prop6)이 주는 두 exact sequence가 얻어진다. 앞의 exact sequence를 자유 abelian group $H^\bullet(F)$와 tensor하면 (자유이므로 완전성이 보존된다) 각 항이 $H^\bullet(U)\otimes H^\bullet(F)$, $\bigl(H^\bullet(U')\oplus H^\bullet(U'')\bigr)\otimes H^\bullet(F)$, $H^\bullet(U'\cap U'')\otimes H^\bullet(F)$로 이어지는 exact sequence를 얻는다. 이를 위 행에, 전공간의 Mayer–Vietoris exact sequence를 아래 행에 두고 세로 방향으로 $\Phi_U$, $\Phi_{U'}\oplus\Phi_{U''}$, $\Phi_{U'\cap U''}$을 놓으면 사다리 모양의 diagram이 된다. $\pi^\ast$와 고정된 class $a_j$와의 cup product가 restriction 및 Mayer–Vietoris의 connecting homomorphism과 (부호를 무시하면) 교환하므로 각 사각형은 commute하며, 가정에 의해 $\Phi_{U'}\oplus\Phi_{U''}$과 $\Phi_{U'\cap U''}$이 isomorphism이므로 [\[호몰로지 대수학\] §Diagram chasing, ⁋따름정리 2](/ko/math/homological_algebra/diagram_chasing#cor2)에 의하여 $\Phi_U$ 또한 isomorphism이다.

Trivializing open들의 교집합은 다시 trivializing open이므로, $B$가 유한 trivializing covering을 가지면 covering의 크기에 대한 귀납으로 $\Phi_B$가 isomorphism임을 얻는다. 일반적인 paracompact 밑공간에 대해서는 open cover에 대한 직접극한 논증이 추가로 필요하며, 이는 [Hat]와 [BT]에 자세히 다루어져 있다.
:::

계수를 $\mathbb{Z}$로 두었지만, 위의 증명은 fiber의 cohomology가 자유가군이 되는 임의의 PID 계수에 대하여 그대로 성립한다. 조건의 핵심은 fiber의 cohomology가 전역적인 class로 "펼쳐진다"는 것으로, 이 때 전공간의 cohomology는 밑공간의 cohomology를 coefficient ring으로 삼아 fiber의 cohomology를 그대로 복제한 모양이 된다. 아래에서 이 정리는 밑공간이 무한차원인 경우 ($\CP^\infty$ 등) 에도 쓰이므로 일반 판본이 실제로 필요하다.

개념적으로 [정리 1](#thm1)은 [§호모토피의 계산, ⁋정리 15](/ko/math/algebraic_topology/fibrations#thm15)이 degenerate하는 특수한 경우이다. 전역 class $a_j$은 $H^\bullet(E)$에서 오므로 fiber 방향 열의 permanent cycle이고, 이들이 $H^\bullet(F)$ 전체를 생성하므로 곱 구조에 의해 모든 미분이 소멸하며, 동시에 그 존재가 $\pi_1(B)$의 $H^\bullet(F)$ 위 action을 자명하게 만들어 $E_2^{p,q}=H^p(B)\otimes H^q(F)$이 비틀림 없이 성립한다. 따라서 $E_2=E_\infty$가 되어 위의 결론이 그대로 따라온다. 우리가 택한 Mayer–Vietoris 증명은 이 spectral sequence를 경유하지 않고 같은 결론에 이르는 초등적인 우회로이며, 그런 만큼 국소계수계에 얽힌 미묘함도 자연스럽게 비켜간다.

## 사영다발의 코호몰로지

이제 Leray–Hirsch 정리를 적용할 fiber bundle을 만든다. Complex vector bundle의 fiber에서 원점을 지나는 직선들을 모으면 projective space가 나오고, 이를 밑공간 위에서 다발로 묶은 것이 projective bundle이다.

::: 정의 2
Complex rank $n$ vector bundle $E\rightarrow B$의 *projective bundle<sub>사영다발</sub>* $\mathbb{P}(E)$는 각 점 $x\in B$ 위의 fiber가 $E_x$의 원점을 지나는 complex 직선들의 projective space $\mathbb{P}(E_x)$인 fiber bundle이다. 곧 그 전공간은

$$\mathbb{P}(E)=\{(x,\ell):x\in B,\ \ell\subseteq E_x\text{ 는 1차원 부분공간}\}$$

이고 projection $\pi:\mathbb{P}(E)\rightarrow B$는 $(x,\ell)\mapsto x$이며, fiber는 $\CP^{n-1}$이다.
:::

$E$가 $U$ 위에서 $U\times\mathbb{C}^n$으로 자명해지면 $\mathbb{P}(E)$는 $U$ 위에서 $U\times\CP^{n-1}$이 되므로, $\mathbb{P}(E)$는 fiber $\CP^{n-1}$을 갖는 fiber bundle이다. Projective bundle 위에는 표준적인 line bundle이 하나 살고 있다. 각 점 $(x,\ell)\in\mathbb{P}(E)$에 그 점이 지정하는 직선 $\ell\subseteq E_x$ 자체를 fiber로 붙이면 $\mathbb{P}(E)$ 위의 line bundle $\gamma_E$가 얻어지며, 이는 정의상 pullback $\pi^\ast E$의 부분다발 $\gamma_E\subseteq\pi^\ast E$이다. 이를 projective bundle의 *tautological line bundle*이라 부른다. $E$에 Hermitian 내적을 주면 각 $\ell$의 직교여를 취하여

$$\pi^\ast E\cong\gamma_E\oplus\gamma_E^\perp$$

로 쪼갤 수 있고, 여기서 $\gamma_E^\perp$는 rank $(n-1)$의 complex vector bundle이다.

::: 정리 3
Complex rank $n$ vector bundle $E\rightarrow B$의 projective bundle $\pi:\mathbb{P}(E)\rightarrow B$와 tautological line bundle $\gamma_E$에 대하여, $a=c_1(\gamma_E)\in H^2(\mathbb{P}(E);\mathbb{Z})$이라 두자. 그럼 $H^\bullet(\mathbb{P}(E);\mathbb{Z})$은 $1,a,\ldots,a^{n-1}$을 basis로 하는 $H^\bullet(B;\mathbb{Z})$ 위의 자유가군이다. 특히 $\pi^\ast:H^\bullet(B)\rightarrow H^\bullet(\mathbb{P}(E))$은 단사이다.
:::

::: 증명
각 fiber $\mathbb{P}(E_x)$는 $\CP^{n-1}$이고, 그 위로 $\gamma_E$를 제한하면 정확히 $\CP^{n-1}$의 tautological line bundle이 되므로, $a$를 이 fiber로 제한하면 그 first Chern class $c_1(\gamma)$가 된다. [§벡터다발의 특성류, ⁋예시 8](/ko/math/algebraic_topology/characteristic_classes#ex8)에서 $H^\bullet(\CP^\infty;\mathbb{Z})=\mathbb{Z}[c_1(\gamma)]$이고 $c_1(\gamma)$가 $H^2$의 generator였으며, $\CP^{n-1}$은 $2(n-1)$차 이하의 짝수 cell만 가지므로 restriction $H^\bullet(\CP^\infty)\rightarrow H^\bullet(\CP^{n-1})$이 그 범위에서 isomorphism이고 위로는 $0$이 되어

$$H^\bullet(\CP^{n-1};\mathbb{Z})=\mathbb{Z}[c_1(\gamma)]/(c_1(\gamma)^n)$$

이다. 따라서 $1,a,\ldots,a^{n-1}$의 fiber로의 restriction은 $H^\bullet(\CP^{n-1})$의 basis를 이룬다. $H^\bullet(\CP^{n-1})$은 유한 rank의 자유가군이므로 [정리 1](#thm1)에 의하여 $H^\bullet(\mathbb{P}(E))$은 $1,a,\ldots,a^{n-1}$을 basis로 하는 $H^\bullet(B)$ 위의 자유가군이다. 이 basis에서 $1$에 대응하는 성분이 $\pi^\ast\alpha=\pi^\ast\alpha\smile 1$이고 $\Phi$가 isomorphism이므로 $\pi^\ast$은 단사이다.
:::

Generator로 $a=c_1(\gamma_E)$ 대신 그 dual $\gamma_E^\vee$의 first Chern class를 택해도 거듭제곱들이 같은 자유가군의 basis를 이루므로 결과는 같다. [정리 3](#thm3)은 projective bundle의 cohomology가 밑공간의 cohomology 위에서 tautological class $a$의 거듭제곱들로 완전히 펼쳐짐을 뜻한다.

::: 참고 4
[정리 3](#thm3)은 사실 관계식까지 담아 정밀하게 적을 수 있다. Tautological line bundle의 dual $\gamma_E^\vee$의 first Chern class를 $\xi=c_1(\gamma_E^\vee)$라 하면, $H^\bullet(\mathbb{P}(E))$은 $H^\bullet(B)$-대수로서 generator $\xi$가 유일한 관계식

$$\xi^n+\pi^\ast c_1(E)\smile \xi^{n-1}+\cdots+\pi^\ast c_n(E)=0$$

을 만족하는 것으로 표현되며, 곧 $H^\bullet(\mathbb{P}(E))=H^\bullet(B)[\xi]/\bigl(\sum_{i=0}^n\pi^\ast c_i(E)\xi^{n-i}\bigr)$이다. 거꾸로 이 관계식의 계수로 [§벡터다발의 특성류, ⁋정의 6](/ko/math/algebraic_topology/characteristic_classes#def6)의 Chern class를 정의할 수도 있으며, 이것이 Grothendieck을 따른 Chern class의 또 다른 정의이다. ([MS] §14)
:::

## Splitting principle

[정리 3](#thm3)의 projective bundle을 반복하면 임의의 vector bundle을 line bundle들의 합으로 만들 수 있다. 핵심은 각 단계의 pullback이 cohomology에서 단사라는 것으로, 이 덕분에 위에서 성립하는 등식이 아래로 그대로 내려온다.

::: 정리 5 (Splitting principle)
Paracompact 밑공간 $B$ 위의 complex rank $n$ vector bundle $E\rightarrow B$에 대하여, 공간 $F(E)$와 연속함수 $\rho:F(E)\rightarrow B$가 존재하여 다음을 만족한다.

1. Pullback $\rho^\ast:H^\bullet(B;\mathbb{Z})\rightarrow H^\bullet(F(E);\mathbb{Z})$은 단사이다.
2. $\rho^\ast E$는 complex line bundle들의 Whitney 합 $L_1\oplus\cdots\oplus L_n$으로 쪼개진다.
:::

::: 증명
Rank $n$에 대한 귀납으로 보인다. $n=1$이면 $E$ 자체가 line bundle이므로 $F(E)=B$와 $\rho=\id$로 두면 된다.

$n\geq 2$라 하고, rank $n-1$까지 명제가 성립한다 가정하자. Projective bundle $\pi:\mathbb{P}(E)\rightarrow B$를 잡으면 [정리 3](#thm3)에 의하여 $\pi^\ast$은 단사이고, tautological line bundle에 대하여

$$\pi^\ast E\cong\gamma_E\oplus\gamma_E^\perp$$

가 성립하며 $\gamma_E^\perp$는 rank $(n-1)$이다. 귀납가정을 $\mathbb{P}(E)$ 위의 $\gamma_E^\perp$에 적용하면, 연속함수 $\rho':F(\gamma_E^\perp)\rightarrow\mathbb{P}(E)$가 존재하여 $\rho'^\ast$이 단사이고 $\rho'^\ast\gamma_E^\perp\cong L_2\oplus\cdots\oplus L_n$이 line bundle들의 합이 된다. 이제 $F(E)=F(\gamma_E^\perp)$와 $\rho=\pi\circ\rho'$로 두면, $\rho^\ast=\rho'^\ast\pi^\ast$은 단사인 두 morphism의 합성이므로 단사이고,

$$\rho^\ast E=\rho'^\ast\pi^\ast E=\rho'^\ast(\gamma_E\oplus\gamma_E^\perp)=\rho'^\ast\gamma_E\oplus L_2\oplus\cdots\oplus L_n$$

이 되어 $L_1=\rho'^\ast\gamma_E$로 두면 line bundle들의 합이다.
:::

이렇게 얻어진 $F(E)$는 $E$의 *flag bundle*로, 각 점 $x\in B$ 위의 fiber가 $E_x$의 완전한 flag들의 공간인 fiber bundle이다. 두 조건 가운데 실질적인 힘은 단사성에 있다. Pullback과 호환되는 (곧 naturality를 갖는) 특성류의 등식을 증명하려 할 때, [정리 5](#thm5)에 의하여 그 등식을 $F(E)$ 위로 pullback한 뒤 증명해도 충분한데, 그 위에서는 $E$가 line bundle들의 합으로 쪼개져 모든 Chern class가 first Chern class들의 다항식으로 환원되기 때문이다. 등식이 $F(E)$ 위에서 성립하면 $\rho^\ast$의 단사성에 의해 $B$ 위에서도 성립한다. [§벡터다발의 특성류, ⁋정리 9](/ko/math/algebraic_topology/characteristic_classes#thm9)과 [§벡터다발의 특성류, ⁋명제 10](/ko/math/algebraic_topology/characteristic_classes#prop10)의 켤레 공식이 바로 이 방식으로 증명된다.

---

**참고문헌**

**[MS]** J. W. Milnor and J. D. Stasheff, *Characteristic Classes*, Annals of Mathematics Studies 76, Princeton University Press, 1974.

**[BT]** R. Bott and L. W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982.

**[Hat]** A. Hatcher, *Vector Bundles and K-Theory*, online notes, 2017.
