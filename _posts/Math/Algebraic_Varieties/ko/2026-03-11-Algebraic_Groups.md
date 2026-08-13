---
title: "대수적 군"
description: "Variety 위의 group 구조를 정의하고 translation이 주는 homogeneity로부터 매끄러움과 identity component의 구조를 얻은 뒤, affine algebraic group의 coordinate ring이 갖는 comodule 구조와 representation, torus의 weight decomposition, 그리고 orbit과 homogeneous space를 다룬다."
excerpt: "Algebraic groups, their representations, and homogeneous spaces"

categories: [Math / Algebraic Varieties]
permalink: /ko/math/algebraic_varieties/algebraic_groups
sidebar: 
    nav: "algebraic_varieties-ko"

date: 2026-03-11
weight: 8
published: false
drift_needed: true

---

우리는 수학적 대상이 다른 대상에 작용하는 많은 예시들을 알고 있다. 대수적으로 가장 중요한 예시는 벡터공간 위에 작용하는 group일 것이며, 기하적으로는 Lie group action이 있다. Algebraic geometry는 algebraic한 대상들에 기하학적인 의미를 부여하므로, 이 두 관점은 group 구조와 variety 구조를 동시에 갖는 대상에서 하나로 합쳐진다. 이번 글에서 base field $\mathbb{K}$는 언제나 algebraically closed라 가정한다.

## 대수적 군의 정의

Variety 위에 group 구조를 얹되 두 구조가 서로 어긋나지 않기를 요구하는 것이 우리의 정의가 될 것이다. 그 전에 두 가지를 정리해 두어야 한다.

첫째로 우리가 다룰 대상은 irreducible일 필요가 없다. [§준사영다양체, ⁋정의 1](/ko/math/algebraic_varieties/quasi_projective_varieties#def1)의 quasi-projective variety는 irreducible한 것만을 가리키지만, orthogonal group처럼 흔히 쓰이는 algebraic group 가운데 irreducible이 아닌 것이 있기 때문이다. 그래서 이 글에서는 projective algebraic set의 열린부분집합을 *quasi-projective algebraic set*이라 부르고 이것을 대상으로 삼는다. Irreducibility를 요구하지 않아도 잃는 것은 없다. [§아핀다양체, ⁋정의 11](/ko/math/algebraic_varieties/affine_varieties#def11)의 coordinate ring $\mathbb{K}[X] = \mathbb{K}[\x_1, \ldots, \x_n]/I(X)$과 [§아핀다양체, ⁋정의 14](/ko/math/algebraic_varieties/affine_varieties#def14)의 regular function, 그리고 [§준사영다양체, ⁋정의 7](/ko/math/algebraic_varieties/quasi_projective_varieties#def7)의 morphism은 정의에 irreducibility가 들어가지 않으므로 affine algebraic set과 quasi-projective algebraic set에 그대로 적용되고, [§아핀다양체, ⁋정리 10](/ko/math/algebraic_varieties/affine_varieties#thm10)도 임의의 ideal에 대한 진술이며, [§아핀다양체, ⁋명제 16](/ko/math/algebraic_varieties/affine_varieties#prop16)과 [§아핀다양체, ⁋명제 18](/ko/math/algebraic_varieties/affine_varieties#prop18)의 증명도 irreducibility를 쓰지 않는다. 게다가 [명제 4](#prop4)에서 보듯 이 완화는 서로소인 유한개의 variety를 나란히 놓는 것 이상을 허용하지 않는다.

둘째로 곱 $G \times G$ 위의 구조를 정해야 한다. [§사영다양체, ⁋예시 16](/ko/math/algebraic_varieties/projective_varieties#ex16)의 Segre embedding을 일반화한

$$s: \mathbb{P}^n \times \mathbb{P}^m \rightarrow \mathbb{P}^{(n+1)(m+1)-1};\qquad ([x_0 : \cdots : x_n], [y_0 : \cdots : y_m]) \mapsto [\cdots : x_iy_j : \cdots]$$

는 단사이고, 그 image는 $\z_{ij}\z_{kl} - \z_{il}\z_{kj}$들의 zero set이므로 닫힌집합이다. 또 projective algebraic set $P \subseteq \mathbb{P}^n$과 $Q \subseteq \mathbb{P}^m$에 대하여 $s(P \times Q)$도 닫힌집합인데, $P$를 정의하는 각 homogeneous polynomial $F$에 대하여 $\y$의 $\deg F$차 monomial $\y^\alpha$를 곱한 $F(\x)\y^\alpha$가 $\z_{ij}$들의 homogeneous polynomial로 표현되고 $Q$ 쪽도 마찬가지이기 때문이다. 이로부터 열린집합 $U \subseteq \mathbb{P}^n$과 $V \subseteq \mathbb{P}^m$에 대해 $s(U \times V)$는 image 안에서 열린집합이다. Image 안에서의 여집합이 $s((\mathbb{P}^n \setminus U) \times \mathbb{P}^m)$과 $s(\mathbb{P}^n \times (\mathbb{P}^m \setminus V))$의 합집합, 곧 닫힌집합이기 때문이다. 따라서 $X = P \cap U$와 $Y = Q \cap V$가 quasi-projective algebraic set이면

$$s(X \times Y) = s(P \times Q) \cap s(U \times V)$$

역시 quasi-projective algebraic set이다. 이하에서 $X \times Y$에는 언제나 이 구조가 주어진 것으로 본다.

::: 정의 1
Quasi-projective algebraic set $G$ 위에 group 구조가 주어졌다 하자. $G$가 *algebraic group<sub>대수적 군</sub>*이라는 것은 multiplication

$$m: G \times G \rightarrow G;\qquad (g, h) \mapsto gh$$

와 inversion

$$i: G \rightarrow G;\qquad g \mapsto g^{-1}$$

이 모두 morphism인 것이다.
:::

즉 algebraic group은 group 구조와 quasi-projective algebraic set 구조를 함께 갖되 두 구조가 morphism의 수준에서 맞물려 있는 대상이다. Identity $e \in G$와 각 원소의 역원은 group 구조가 이미 결정하므로 따로 요구할 것이 없고, 확인할 것은 $m$과 $i$가 morphism이라는 조건뿐이다.

::: 예시 2
다음은 이 글 전체에서 반복해 쓰일 예시들이다.

1. Additive group $\mathbb{G}_a$는 affine line $\mathbb{A}^1$에 덧셈을 준 것이다. $m(x,y) = x+y$와 $i(x) = -x$가 모두 다항식이므로 둘 다 morphism이다. ([§아핀다양체, ⁋정의 15](/ko/math/algebraic_varieties/affine_varieties#def15))
2. Multiplicative group $\mathbb{G}_m$은 $\mathbb{A}^1 \setminus \{0\}$에 multiplication을 준 것이다. 이는 principal open set이므로 affine variety $Z(\x\y - 1) \subseteq \mathbb{A}^2$와 isomorphic하고 ([§아핀다양체, ⁋명제 7](/ko/math/algebraic_varieties/affine_varieties#prop7)), 이 좌표에서 inversion이 $(x,y) \mapsto (y,x)$이므로 morphism이다. Coordinate ring은 $\mathbb{K}[\x, \x^{-1}]$이다.
3. General linear group $\GL(n;\mathbb{K})$는 $\mathbb{A}^{n^2}$의 principal open set $D(\det)$이므로 affine variety이고, 그 coordinate ring은 $\mathbb{K}[\x_{11}, \ldots, \x_{nn}][1/\det]$이다. Multiplication의 각 성분은 $\x_{ij}$들의 다항식이고 Cramer 공식 $i(A) = (\det A)^{-1}\operatorname{adj}(A)$의 각 성분은 $D(\det)$ 위의 regular function이므로 ([§아핀다양체, ⁋정의 14](/ko/math/algebraic_varieties/affine_varieties#def14)) 둘 다 morphism이다. $n = 1$이면 $\GL(1;\mathbb{K}) = \mathbb{G}_m$이다.
4. Special linear group $\SL(n;\mathbb{K}) = Z(\det - 1)$은 $\GL(n;\mathbb{K})$의 닫힌집합이며, multiplication과 inversion의 restriction이 다시 morphism이므로 ([§준사영다양체, ⁋명제 12](/ko/math/algebraic_varieties/quasi_projective_varieties#prop12)) algebraic group이다.
5. Smooth plane cubic $E \subseteq \mathbb{P}^2$ 위의 inflection point $O$를 하나 고정하면, chord-tangent 구성은 $O$를 identity로 하는 abelian group 구조를 $E$에 주며, group law가 유리식으로 주어지므로 $m$과 $i$는 morphism이다. 이를 *타원곡선<sub>elliptic curve</sub>*이라 부른다. $E$는 projective variety이므로 위의 예시들과 달리 affine variety가 아니고, 이 차이가 algebraic group의 구조론에서 가장 큰 분기점이 된다.
6. Finite group $\Gamma$는 유한개의 점으로 이루어진 affine algebraic set이고 그 위의 모든 함수가 regular이므로 algebraic group이다. 가령 $\operatorname{char}\mathbb{K}$가 $n$을 나누지 않으면 $\mu_n = Z(\x^n - 1) \subseteq \mathbb{G}_m$은 $n$개의 점으로 이루어진 algebraic group이며 $\mathbb{Z}/n\mathbb{Z}$와 isomorphic하다.
:::

위의 예시들에서 보듯 $m$과 $i$가 morphism이라는 것을 확인하는 일은 대체로 간단하다. 정작 중요한 것은 group 구조가 variety의 국소적 성질에 강한 제약을 준다는 사실이며, 그 출발점은 translation이다.

::: 명제 3
Algebraic group $G$와 $g \in G$에 대하여 left translation $\lambda_g: x \mapsto gx$, right translation $\rho_g: x \mapsto xg$, 그리고 inversion $i$는 모두 $G$의 isomorphism이다.
:::

::: 증명
$\lambda_g$는 morphism $x \mapsto (g,x)$와 $m$의 합성이므로 morphism이고 ([§준사영다양체, ⁋명제 11](/ko/math/algebraic_varieties/quasi_projective_varieties#prop11)), $\lambda_{g^{-1}}$이 그 역사상이므로 isomorphism이다. ([§준사영다양체, ⁋정의 13](/ko/math/algebraic_varieties/quasi_projective_varieties#def13)) $\rho_g$도 같은 이유로 isomorphism이다. Inversion $i$는 [정의 1](#def1)에 의해 morphism이고 $i \circ i = \id_G$이므로 isomorphism이다.
:::

따라서 임의의 두 점 $x, y \in G$에 대하여 $\lambda_{yx^{-1}}$은 $x$를 $y$로 옮기는 $G$의 automorphism이다. 즉 algebraic group은 어느 점에서 보나 똑같이 생겼으며, 이 homogeneity가 다음 두 명제의 원천이다.

::: 명제 4
Algebraic group $G$의 irreducible component들은 서로소이고, 따라서 각각은 $G$의 열린 닫힌 부분집합이다. 또 $G$는 smooth이다.
:::

::: 증명
$\mathbb{P}^n$의 닫힌집합은 homogeneous ideal의 zero set이고 $\mathbb{K}[\x_0, \ldots, \x_n]$이 Noetherian ring이므로 $\mathbb{P}^n$은 Noetherian 공간이다. Noetherian 공간의 부분공간도 Noetherian이므로 $G$는 유한개의 irreducible component $C_1, \ldots, C_r$의 합집합이다. ([\[위상수학\] §차원, ⁋명제 13](/ko/math/topology/dimension#prop13))

[명제 3](#prop3)의 $\lambda_g$는 homeomorphism이므로 component들의 모임을 permute한다. 이제

$$S = \bigcup_{i \ne j} (C_i \cap C_j)$$

라 두면 $S$는 닫힌집합이고 모든 $g \in G$에 대하여 $\lambda_g(S) = S$이다. 만일 $S \ne \emptyset$이면 $x \in S$를 하나 잡을 때 임의의 $y \in G$에 대하여 $y = \lambda_{yx^{-1}}(x) \in S$이므로 $S = G$이다. 그러나 irreducible component의 정의에 의해 $C_i \not\subseteq \bigcup_{j \ne i} C_j$이므로 $S \ne G$이며, 이는 모순이다. 따라서 $S = \emptyset$이고 component들은 서로소이다. 그럼 $C_i$의 여집합은 나머지 component들의 합집합이므로 닫힌집합이고, 따라서 $C_i$는 열린집합이기도 하다.

이제 $C_i$가 $G$의 열린집합이므로 점 $x \in C_i$에서의 local ring은 $C_i$에서 계산한 것과 같고, $x$가 $G$의 smooth point인지는 variety $C_i$ 안에서 판정된다. $C_i$의 smooth point들은 $C_i$의 dense open subset을 이루므로 ([§접공간과 매끄러움, ⁋명제 10](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#prop10)) smooth point $z \in C_i$가 존재한다. 임의의 $x \in C_i$에 대하여 $\lambda_{xz^{-1}}$은 $z$를 $x$로 보내는 $G$의 isomorphism이고 component를 component로 보내므로 $C_i$를 $C_i$ 위로 보낸다. Isomorphism은 smooth point를 smooth point로 보내므로 $x$ 역시 smooth point이다.
:::

즉 algebraic group에서는 singular point도, 서로 겹치는 component도 나타날 수 없다. 이는 [명제 3](#prop3)의 homogeneity가 국소적인 정보를 전역으로 퍼뜨린 결과이며, 일반적인 variety에서는 기대할 수 없는 성질이다. 특히 $G$는 유한개의 서로소인 smooth variety를 나란히 놓은 것이므로, 남은 일은 이 조각들이 group 구조와 어떻게 맞물리는지를 보는 것이다.

::: 명제 5
$G^\circ$를 identity $e$를 포함하는 $G$의 irreducible component라 하자. 그럼 $G^\circ$는 $G$의 closed normal subgroup이면서 그 index가 유한하고, $G$의 irreducible component들은 정확히 $G^\circ$의 left coset들이다. 특히 $G$가 connected인 것과 irreducible인 것은 동치이다.
:::

::: 증명
[명제 4](#prop4)에 의해 각 $\lambda_g$는 component들을 permute한다. $x \in G^\circ$이면 $\lambda_x(G^\circ)$는 $\lambda_x(e) = x$를 포함하는 component이므로 $G^\circ$와 같고, 따라서 $G^\circ G^\circ = G^\circ$이다. 또 $i$도 homeomorphism이므로 component를 permute하며 $i(e) = e$이므로 $i(G^\circ) = G^\circ$이다. 즉 $G^\circ$는 subgroup이고, irreducible component로서 닫혀 있다.

임의의 $g \in G$에 대하여 conjugation $c_g = \lambda_g \circ \rho_{g^{-1}}$는 [명제 3](#prop3)에 의해 isomorphism이고 $c_g(e) = e$이므로 $c_g(G^\circ) = G^\circ$이다. 따라서 $G^\circ$는 normal이다.

또 $\lambda_g(G^\circ) = gG^\circ$는 $g$를 포함하는 component이고, 역으로 임의의 component $C$와 $g \in C$에 대하여 $C = gG^\circ$이다. Component가 유한개이므로 $[G : G^\circ] < \infty$이다.

마지막으로 [명제 4](#prop4)에 의해 각 component가 열린 닫힌집합이므로 $G$의 connected component와 irreducible component가 일치한다. 따라서 $G$가 connected인 것은 component가 하나뿐인 것, 곧 $G$가 irreducible인 것과 동치이다.
:::

$G^\circ$를 $G$의 *identity component*라 부른다. [명제 5](#prop5)는 algebraic group의 연구를 두 층으로 나누어 준다. 하나는 connected algebraic group $G^\circ$이고 다른 하나는 finite group $G/G^\circ$이며, 앞으로 다룰 결과들은 대부분 앞쪽에 관한 것이다. 또 이 명제 덕분에 connected와 irreducible을 구별할 필요가 없어지므로, 이하에서 둘을 구별 없이 쓴다.

::: 예시 6
[예시 2](#ex2)의 대상들에서 identity component를 확인해 보자.

1. $\mathbb{G}_a$, $\mathbb{G}_m$, $\GL(n;\mathbb{K})$는 각각 $\mathbb{A}^1$, $\mathbb{A}^1$, $\mathbb{A}^{n^2}$의 열린집합이므로 irreducible이고, 따라서 [명제 5](#prop5)에 의해 connected이다.
2. $\operatorname{char}\mathbb{K} \ne 2$일 때 orthogonal group $\Omat(n;\mathbb{K}) = \{A \mid A^\mathsf{T}A = I\}$에서는 $(\det A)^2 = 1$이므로 $\det A = \pm 1$이다. 두 조건 $\det A = 1$과 $\det A = -1$은 각각 닫힌집합을 정의하고 어느 쪽도 공집합이 아니므로 $\Omat(n;\mathbb{K})$는 connected가 아니다. 한편 $\det$은 $\Omat(n;\mathbb{K})$ 위에서 $\pm 1$의 값만 가지므로 connected인 $\Omat(n;\mathbb{K})^\circ$ 위에서는 상수 $1$이고, 따라서 $\Omat(n;\mathbb{K})^\circ$는 $\operatorname{SO}(n;\mathbb{K}) = \{A \in \Omat(n;\mathbb{K}) \mid \det A = 1\}$에 포함된다. 실제로는 등호가 성립하나 그러려면 $\operatorname{SO}(n;\mathbb{K})$가 connected임을 보여야 하고, 이는 여기서 다루지 않는다.
3. Finite group $\Gamma$에서는 $\Gamma^\circ = \{e\}$이고 component가 $\lvert \Gamma \rvert$개이므로, [명제 5](#prop5)의 index 조건이 극단적으로 실현된다.
:::

## Subgroup과 homomorphism

Algebraic group들 사이에서 우리가 볼 morphism은 variety 구조뿐 아니라 group 구조까지 보존하는 것들이다.

::: 정의 7
두 algebraic group $G$, $H$ 사이의 morphism $\varphi: G \rightarrow H$가 group homomorphism이기도 할 때, $\varphi$를 algebraic group들 사이의 *homomorphism<sub>준동형사상</sub>*이라 부른다. 또 $G$의 subgroup 가운데 닫힌집합인 것을 $G$의 *closed subgroup*이라 부른다.
:::

Closed subgroup $H \subseteq G$는 그 자체로 algebraic group이다. $\mathbb{P}^n$의 열린집합 $U$와 projective algebraic set $Y$에 대하여 $G = Y \cap U$라 쓰면, $H$가 $G$의 닫힌집합이므로 $\mathbb{P}^n$의 적당한 닫힌집합 $W$에 대하여 $H = (Y \cap W) \cap U$이고 $Y \cap W$는 다시 projective algebraic set이다. 여기에 $m$과 $i$의 restriction이 morphism이라는 것을 더하면 된다. ([§준사영다양체, ⁋명제 12](/ko/math/algebraic_varieties/quasi_projective_varieties#prop12)) 가령 $\det: \GL(n;\mathbb{K}) \rightarrow \mathbb{G}_m$은 homomorphism이고 $\SL(n;\mathbb{K})$는 그 kernel이다. 또 상삼각가역행렬들의 집합 $B_n$, 대각가역행렬들의 집합 $T_n$, 그리고 대각성분이 모두 $1$인 상삼각행렬들의 집합 $U_n$은 모두 $\GL(n;\mathbb{K})$의 closed subgroup이며, 특히 $U_n$은 variety로서 $\mathbb{A}^{n(n-1)/2}$와 isomorphic하다.

::: 명제 8
Homomorphism $\varphi: G \rightarrow H$에 대하여 $\ker\varphi$는 $G$의 closed normal subgroup이고, image의 closure $\overline{\varphi(G)}$는 $H$의 closed subgroup이다.
:::

::: 증명
$H$의 한 점 $e$는 닫힌집합이고 $\varphi$는 연속이므로 ([§준사영다양체, ⁋명제 10](/ko/math/algebraic_varieties/quasi_projective_varieties#prop10)) $\ker\varphi = \varphi^{-1}(e)$는 $G$의 닫힌집합이다. Normal이라는 것은 group 구조만 쓰는 사실이다.

$Y = \overline{\varphi(G)}$라 하자. 임의의 $g \in G$에 대하여 $\lambda_{\varphi(g)}$는 homeomorphism이면서 $\varphi(G)$를 자기 자신으로 보내므로 $\lambda_{\varphi(g)}(Y) = Y$이고, 따라서 $\varphi(G) \cdot Y \subseteq Y$이다. 이제 $y \in Y$를 고정하면 방금 얻은 포함관계는 $\rho_y(\varphi(G)) \subseteq Y$를 뜻하며, $\rho_y$가 homeomorphism이므로

$$\rho_y(Y) = \rho_y\left(\overline{\varphi(G)}\right) = \overline{\rho_y(\varphi(G))} \subseteq Y$$

이다. 즉 $Y \cdot Y \subseteq Y$이다. 또 $i(\varphi(G)) = \varphi(G)$이고 $i$가 homeomorphism이므로 $i(Y) = Y$이며, $e \in Y$이므로 $Y$는 $H$의 closed subgroup이다.
:::

실은 $\varphi(G)$ 자체가 닫혀 있음을 보일 수 있으나, 그 증명에는 morphism의 image가 constructible이라는 사실이 필요하므로 여기서는 다루지 않는다.

## 좌표환과 comodule

Algebraic group이 affine일 때에는 group 구조 전체가 coordinate ring 위의 대수적 데이터로 번역되며, 이 번역이 이 글의 나머지 부분을 지배한다.

::: 정의 9
Algebraic group $G$가 affine algebraic set일 때, $G$를 *affine algebraic group<sub>아핀 대수적 군</sub>*이라 부른다.
:::

[예시 2](#ex2)의 $\mathbb{G}_a$, $\mathbb{G}_m$, $\GL(n;\mathbb{K})$, $\SL(n;\mathbb{K})$와 finite group은 모두 affine algebraic group이고, 타원곡선은 그렇지 않다. 두 affine algebraic set $X \subseteq \mathbb{A}^n$과 $Y \subseteq \mathbb{A}^m$에 대하여 곱 $X \times Y \subseteq \mathbb{A}^{n+m}$도 affine algebraic set이며, 이는 앞에서 정한 Segre 구성과 일치한다. Segre embedding을 $\mathbb{A}^n \times \mathbb{A}^m$에 제한하면 점 $(x, y)$를 좌표가 $x_i$, $y_j$, $x_iy_j$인 점으로 보내는 morphism이 되는데, 처음 $n + m$개의 좌표로의 projection이 그 역사상이기 때문이다.

이 곱의 coordinate ring은 두 인자의 coordinate ring으로부터 결정된다. 우선 $f \otimes g$를 함수 $(x, y) \mapsto f(x)g(y)$로 보내는 대응은 algebra homomorphism

$$\mathbb{K}[X] \otimes_\mathbb{K} \mathbb{K}[Y] \rightarrow \mathbb{K}[X \times Y]$$

를 정의한다. $X \times Y$의 좌표함수는 모두 $\x_i \otimes 1$ 또는 $1 \otimes \y_j$의 image이고 이들이 $\mathbb{K}[X \times Y]$를 생성하므로 이 homomorphism은 전사이다. 단사임을 보기 위해 $\sum_i f_i \otimes g_i$가 $0$으로 간다 하고, 일반성을 잃지 않고 $g_i$들이 $\mathbb{K}[Y]$에서 일차독립이라 하자. 각 $x \in X$를 고정하면 $\sum_i f_i(x) g_i$는 $Y$ 위에서 항등적으로 $0$인 함수이므로 모든 $i$에 대하여 $f_i(x) = 0$이고, $x$가 임의였으므로 $f_i = 0$이다. 따라서

$$\mathbb{K}[X \times Y] \cong \mathbb{K}[X] \otimes_\mathbb{K} \mathbb{K}[Y]$$

이다.

이제 $A = \mathbb{K}[G]$라 두자. Multiplication, inversion, 그리고 identity는 각각 algebra homomorphism

$$\Delta = m^\ast: A \rightarrow A \otimes_\mathbb{K} A, \qquad S = i^\ast: A \rightarrow A, \qquad \epsilon = \operatorname{ev}_e: A \rightarrow \mathbb{K}$$

를 유도하며, 구체적으로 $\Delta(f)(g,h) = f(gh)$, $S(f)(g) = f(g^{-1})$, $\epsilon(f) = f(e)$이다. Group의 세 공리는 그대로 $\Delta$의 coassociativity $(\Delta \otimes \id_A) \circ \Delta = (\id_A \otimes \Delta) \circ \Delta$, counit 조건 $(\epsilon \otimes \id_A) \circ \Delta = (\id_A \otimes \epsilon) \circ \Delta = \id_A$, 그리고 $\Delta(f) = \sum_i f_i \otimes h_i$일 때 $\sum_i S(f_i) h_i = f(e) \cdot 1$이라는 antipode 조건으로 번역된다. 이러한 구조를 갖춘 $\mathbb{K}$-algebra를 *Hopf algebra*라 부른다.

::: 정의 10
Algebraic group $G$의 quasi-projective algebraic set $X$ 위로의 *action<sub>작용</sub>*이란 morphism

$$\alpha: G \times X \rightarrow X;\qquad (g, x) \mapsto g \cdot x$$

로서 모든 $g, h \in G$와 $x \in X$에 대하여 $e \cdot x = x$와 $g \cdot (h \cdot x) = (gh) \cdot x$를 만족하는 것이다.
:::

Action이 주어지면 각 $g \in G$마다 $x \mapsto g \cdot x$는 [명제 3](#prop3)에서와 같은 이유로 $X$의 automorphism이 된다. 즉 action은 $G$에서 $X$의 automorphism들의 group으로 가는 group homomorphism이며, 여기에 morphism 조건이 얹힌 것이다. $G$와 $X$가 모두 affine이면 이 데이터는 완전히 대수적인 것이 된다. $A = \mathbb{K}[G]$, $B = \mathbb{K}[X]$라 하고 $B$ 위에 $(g \cdot f)(x) = f(g^{-1} \cdot x)$로 $G$의 action을 주자. 역원을 넣은 것은 이렇게 두어야 $B$ 위의 것이 다시 left action이 되기 때문이다.

::: 정의 11
$G$가 affine algebraic group이고 $A = \mathbb{K}[G]$라 하자. $\mathbb{K}$-벡터공간 $V$ 위의 *comodule structure*란 선형사상 $\Delta_V: V \rightarrow V \otimes_\mathbb{K} A$로서 다음 두 조건

$$(\Delta_V \otimes \id_A) \circ \Delta_V = (\id_V \otimes \Delta) \circ \Delta_V, \qquad (\id_V \otimes \epsilon) \circ \Delta_V = \id_V$$

을 만족하는 것이다.
:::

$\Delta_V(v) = \sum_i v_i \otimes a_i$라 쓰고 $g \cdot v = \sum_i a_i(g) v_i$로 두면 $V$ 위에 $G$의 linear action이 정의되는데, 위의 두 조건은 정확히 $g \cdot (h \cdot v) = (gh) \cdot v$와 $e \cdot v = v$에 해당한다. $A \otimes_\mathbb{K} A = \mathbb{K}[G \times G]$의 원소는 $G \times G$ 위의 함수이므로 모든 점에서의 값이 같으면 같은 원소이고, 따라서 이 대응은 양방향으로 성립한다. 즉 comodule structure는 $V$ 위의 linear action을 대수적으로 적은 것이다.

::: 명제 12
Affine algebraic group $G$가 affine algebraic set $X$ 위에 작용한다 하고 $A = \mathbb{K}[G]$, $B = \mathbb{K}[X]$라 하자. 그럼 $(g \cdot f)(x) = f(g^{-1} \cdot x)$로 주어지는 $B$ 위의 action은 algebra homomorphism이기도 한 comodule structure $\Delta_B: B \rightarrow B \otimes_\mathbb{K} A$로부터 오며, 역으로 algebra homomorphism인 comodule structure $\Delta_B$는 $G$의 $X$ 위로의 action을 유일하게 결정한다.
:::

::: 증명
$\alpha^\ast: B \rightarrow \mathbb{K}[G \times X] = A \otimes_\mathbb{K} B$를 $\alpha$의 pullback이라 하고 ([§아핀다양체, ⁋명제 16](/ko/math/algebraic_varieties/affine_varieties#prop16)), $\Delta_B$를 $\alpha^\ast$에 $S \otimes \id_B$를 합성한 뒤 두 factor의 순서를 바꾼 것으로 정의하자. 그럼 $\Delta_B$는 algebra homomorphism들의 합성이므로 algebra homomorphism이고, $\Delta_B(f) = \sum_i f_i \otimes a_i$라 쓰면 정의에 의해

$$\sum_i f_i(x) a_i(g) = f(g^{-1} \cdot x), \qquad \text{즉}\qquad g \cdot f = \sum_i a_i(g) f_i$$

이다.

이제 $B \otimes_\mathbb{K} A \otimes_\mathbb{K} A = \mathbb{K}[X \times G \times G]$의 원소는 $X \times G \times G$ 위의 함수이므로, 두 원소가 같음을 보이려면 모든 점에서의 값을 비교하면 충분하다. 위의 식으로부터 $(\Delta_B \otimes \id_A)\Delta_B(f)$를 점 $(x, g, h)$에서 evaluate한 값은 $(g \cdot (h \cdot f))(x)$이고, $(\id_B \otimes \Delta)\Delta_B(f)$를 같은 점에서 evaluate한 값은 $((gh) \cdot f)(x)$이다. $f \mapsto g \cdot f$가 left action이므로 두 값은 같으며, 따라서 coassociativity가 성립한다. Counit 조건은 $e \cdot f = f$를 옮겨적은 것이다.

역으로 algebra homomorphism인 comodule structure $\Delta_B$가 주어졌다 하자. $i \circ i = \id_G$이므로 $S \circ S = \id_A$이고, 따라서 $\Delta_B$의 두 factor를 바꾼 뒤 $S \otimes \id_B$를 합성하면 algebra homomorphism $B \rightarrow A \otimes_\mathbb{K} B = \mathbb{K}[G \times X]$를 얻는다. 이는 morphism $\alpha: G \times X \rightarrow X$를 유도하며 ([§아핀다양체, ⁋명제 18](/ko/math/algebraic_varieties/affine_varieties#prop18)), 위의 계산을 거꾸로 밟으면 comodule의 두 조건이 각각 action의 두 조건을 준다.
:::

## 대수적 군의 표현

Lie group에서와 마찬가지로 algebraic group도 그 representation을 통해 이해된다. 앞 절의 언어로 옮기면 representation은 유한차원 comodule에 지나지 않으며, 이 관찰이 affine algebraic group의 구조를 결정한다.

::: 정의 13
Algebraic group $G$의 *representation<sub>표현</sub>*이란 유한차원 벡터공간 $V$와 algebraic group들 사이의 homomorphism

$$\rho: G \rightarrow \GL(V)$$

의 쌍이다. 여기서 $V$의 basis를 고정하면 $\GL(V) \cong \GL(n;\mathbb{K})$이다.
:::

즉 $\rho$는 group homomorphism이면서 동시에 morphism이어야 한다. Finite group의 표현론에서와 마찬가지로 $\chi_\rho(g) = \tr(\rho(g))$를 생각할 수 있고 이를 $\rho$의 character라 부르지만, 이 글에서 정작 쓰이는 것은 다음의 대수적 번역이다.

::: 명제 14
$G$가 affine algebraic group이고 $A = \mathbb{K}[G]$라 하자. 유한차원 벡터공간 $V$에 대하여, representation $\rho: G \rightarrow \GL(V)$들과 $V$ 위의 comodule structure $\Delta_V: V \rightarrow V \otimes_\mathbb{K} A$들 사이에는 일대일 대응이 있다. 이 대응은 $V$의 basis $v_1, \ldots, v_n$을 고정할 때

$$\rho(g) v_j = \sum_{i=1}^n a_{ij}(g) v_i \qquad\Longleftrightarrow\qquad \Delta_V(v_j) = \sum_{i=1}^n v_i \otimes a_{ij}$$

로 주어진다.
:::

::: 증명
Representation $\rho$가 주어졌다 하자. $\GL(n;\mathbb{K})$의 좌표함수 $\x_{ij}$에 대하여 $a_{ij} = \rho^\ast(\x_{ij}) = \x_{ij} \circ \rho \in A$이며, 이것이 위의 행렬성분이다. $\rho(gh) = \rho(g)\rho(h)$는 성분별로 $a_{ij}(gh) = \sum_k a_{ik}(g) a_{kj}(h)$, 곧

$$\Delta(a_{ij}) = \sum_k a_{ik} \otimes a_{kj}$$

를 뜻하고, $\rho(e)$가 항등행렬이라는 것은 $\epsilon(a_{ij}) = \delta_{ij}$를 뜻한다. 이제 $\Delta_V(v_j) = \sum_i v_i \otimes a_{ij}$로 두면

$$(\Delta_V \otimes \id_A)\Delta_V(v_j) = \sum_i \Delta_V(v_i) \otimes a_{ij} = \sum_{i,k} v_k \otimes a_{ki} \otimes a_{ij}$$

이고

$$(\id_V \otimes \Delta)\Delta_V(v_j) = \sum_k v_k \otimes \Delta(a_{kj}) = \sum_{i,k} v_k \otimes a_{ki} \otimes a_{ij}$$

이므로 coassociativity가 성립한다. 또 $(\id_V \otimes \epsilon)\Delta_V(v_j) = \sum_i \delta_{ij} v_i = v_j$이므로 counit 조건도 성립한다.

역으로 comodule structure $\Delta_V$가 주어지면 $\Delta_V(v_j) = \sum_i v_i \otimes a_{ij}$로 $a_{ij} \in A$를 정의하고 $\rho(g) = (a_{ij}(g))$로 두자. Counit 조건은 $\rho(e)$가 항등행렬임을 주고, coassociativity를 위와 같이 전개한 뒤 $v_k$들이 basis라는 것을 쓰면 $\Delta(a_{kj}) = \sum_i a_{ki} \otimes a_{ij}$, 곧 $\rho(gh) = \rho(g)\rho(h)$를 얻는다. 특히 $\rho(g)\rho(g^{-1})$이 항등행렬이므로 각 $\rho(g)$는 가역이다. 성분 $a_{ij}$가 regular function이므로 $\rho$는 $G$에서 $\mathbb{A}^{n^2}$로 가는 morphism이고 그 image가 열린집합 $\GL(n;\mathbb{K})$에 들어가므로, $\rho: G \rightarrow \GL(n;\mathbb{K})$는 morphism이다. ([§준사영다양체, ⁋명제 12](/ko/math/algebraic_varieties/quasi_projective_varieties#prop12)) 두 구성이 서로 역이라는 것은 정의에서 곧바로 확인된다.
:::

Representation을 comodule로 바꾸어 놓으면 무한차원의 comodule $A$ 자신을 유한차원 조각들로 자를 수 있게 되고, 이것이 affine algebraic group의 구조를 결정한다.

::: 명제 15
$G$가 affine algebraic group이고 $(V, \Delta_V)$가 comodule이라 하자. 그럼 $V$의 임의의 유한차원 부분공간 $W$는 $\Delta_V(W') \subseteq W' \otimes_\mathbb{K} A$를 만족하는 유한차원 부분공간 $W' \supseteq W$에 포함된다.
:::

::: 증명
$A$의 $\mathbb{K}$-basis $\{a_\lambda\}$를 잡자. 각 $w \in V$에 대하여 $\Delta_V(w) = \sum_\lambda w_\lambda \otimes a_\lambda$는 유한합이고 $w_\lambda \in V$는 $w$에 선형으로 의존한다. $W$의 basis $w^{(1)}, \ldots, w^{(r)}$을 잡고 $W'$을 모든 $w^{(s)}_\lambda$들이 생성하는 부분공간이라 하면 $W'$은 유한차원이며, counit 조건에 의해

$$w = \sum_\lambda \epsilon(a_\lambda) w_\lambda \in W'$$

이므로 $W \subseteq W'$이다.

이제 $\Delta(a_\lambda) = \sum_{\mu, \nu} c^\lambda_{\mu\nu} a_\mu \otimes a_\nu$ ($c^\lambda_{\mu\nu} \in \mathbb{K}$, 유한합)라 쓰면 $w \in W$에 대하여

$$(\id_V \otimes \Delta)\Delta_V(w) = \sum_{\lambda, \mu, \nu} c^\lambda_{\mu\nu} w_\lambda \otimes a_\mu \otimes a_\nu$$

이고

$$(\Delta_V \otimes \id_A)\Delta_V(w) = \sum_\nu \Delta_V(w_\nu) \otimes a_\nu$$

이다. 두 식이 같고 $\{a_\nu\}$가 basis이므로 각 $\nu$에 대하여

$$\Delta_V(w_\nu) = \sum_{\lambda, \mu} c^\lambda_{\mu\nu} w_\lambda \otimes a_\mu \in W' \otimes_\mathbb{K} A$$

를 얻는다. $W'$의 generator들이 모두 이 꼴이므로 $\Delta_V(W') \subseteq W' \otimes_\mathbb{K} A$이다.
:::

즉 comodule은 언제나 유한차원 subcomodule들의 합집합이며, [명제 14](#prop14)에 의해 각 subcomodule은 $G$의 representation이다. 이 관찰을 $A$ 자신에 적용하면, $A$의 임의의 유한개의 원소를 담는 유한차원 representation을 얻는다. $A$가 finitely generated algebra라는 사실을 여기에 얹으면 다음을 얻는다.

::: 정리 16
모든 affine algebraic group $G$는 적당한 $n$에 대하여 $\GL(n;\mathbb{K})$의 closed subgroup과 isomorphic하다. 이 때문에 affine algebraic group을 *linear algebraic group*이라 부르기도 한다.
:::

::: 증명
$A = \mathbb{K}[G]$는 finitely generated $\mathbb{K}$-algebra이므로 그 generator $f_1, \ldots, f_m$을 잡자. Coassociativity와 counit 조건에 의해 $\Delta: A \rightarrow A \otimes_\mathbb{K} A$ 자신이 $A$ 위의 comodule structure이며, 대응하는 action은 right translation $(g \cdot f)(x) = f(xg)$이다. [명제 15](#prop15)에 의해 $f_1, \ldots, f_m$을 모두 포함하는 유한차원 subcomodule $V \subseteq A$가 존재한다. $V$의 basis $v_1, \ldots, v_n$을 잡고 $\Delta(v_j) = \sum_i v_i \otimes a_{ij}$라 쓰면 [명제 14](#prop14)에 의해 이는 representation $\rho: G \rightarrow \GL(n;\mathbb{K})$를 준다.

Counit 조건 $(\epsilon \otimes \id_A) \circ \Delta = \id_A$를 $v_j$에 적용하면

$$v_j = \sum_i \epsilon(v_i) a_{ij} = \sum_i v_i(e) a_{ij}$$

이므로 각 $v_j$는 $a_{ij}$들의 $\mathbb{K}$-linear combination이다. 특히 $f_1, \ldots, f_m \in V$가 $a_{ij}$들로 생성되는 subalgebra에 속하므로 $A$는 $a_{ij}$들로 생성되고, $\rho^\ast(\x_{ij}) = a_{ij}$이므로 $\rho^\ast: \mathbb{K}[\GL(n;\mathbb{K})] \rightarrow A$는 전사이다.

$J = \ker\rho^\ast$라 하면 $\mathbb{K}[\GL(n;\mathbb{K})]/J \cong A$가 reduced이므로 $J$는 radical ideal이고, 따라서 [§아핀다양체, ⁋정리 10](/ko/math/algebraic_varieties/affine_varieties#thm10)에 의해 $J$가 정의하는 닫힌집합 $Z(J) \subseteq \GL(n;\mathbb{K})$의 coordinate ring은 $A$와 isomorphic하다. 그럼 [§아핀다양체, ⁋명제 18](/ko/math/algebraic_varieties/affine_varieties#prop18)에 의해 $\rho$는 $G$에서 $Z(J)$ 위로의 isomorphism이며, $\rho$가 homomorphism이므로 $Z(J)$는 $\GL(n;\mathbb{K})$의 closed subgroup이다.
:::

## Torus와 weight decomposition

Affine algebraic group 가운데 가장 단순하면서도 가장 자주 등장하는 것은 torus이다. Torus의 representation은 전부 $1$차원 조각으로 쪼개지며, 그 조각들을 기록하는 것이 character이다.

::: 정의 17
Algebraic group $G$의 *character<sub>지표</sub>*란 algebraic group들 사이의 homomorphism $\rchi: G \rightarrow \mathbb{G}_m$이다. Character들은 점별 multiplication $(\rchi\rchi')(g) = \rchi(g)\rchi'(g)$에 대하여 abelian group을 이루며, 이를 $G$의 *character group<sub>지표군</sub>* $X^\ast(G)$라 부른다.
:::

두 character의 곱과 역이 다시 regular function이므로 $X^\ast(G)$가 group이라는 것은 곧바로 확인된다. Finite group의 표현론에서 쓰는 $1$차원 representation의 character가 정확히 이 개념이며, [정의 13](#def13)의 뒤에서 언급한 $\tr(\rho(g))$는 $\dim V = 1$일 때 이것과 일치한다.

::: 정의 18
Algebraic group $T$가 *algebraic torus<sub>대수적 토러스</sub>*라는 것은 적당한 $n \ge 1$에 대하여

$$T \cong (\mathbb{G}_m)^n$$

인 것이다.
:::

$n = 1$인 경우가 [예시 2](#ex2)의 $\mathbb{G}_m$이고, 일반의 $n$에 대해서는 앞서 본 대각가역행렬들의 group $T_n \subseteq \GL(n;\mathbb{K})$가 그 예이다. Torus의 character group은 완전히 계산할 수 있다.

::: 명제 19
$T = (\mathbb{G}_m)^n$이라 하자. 각 $a = (a_1, \ldots, a_n) \in \mathbb{Z}^n$에 대하여

$$\rchi^a(t_1, \ldots, t_n) = t_1^{a_1} \cdots t_n^{a_n}$$

로 정의되는 함수는 $T$의 character이고, $a \mapsto \rchi^a$는 group isomorphism $\mathbb{Z}^n \rightarrow X^\ast(T)$이다. 또 $X^\ast(T)$는 $\mathbb{K}[T]$의 $\mathbb{K}$-basis를 이룬다. 즉

$$\mathbb{K}[T] = \bigoplus_{\rchi \in X^\ast(T)} \mathbb{K}\rchi$$

이다.
:::

::: 증명
$\mathbb{G}_m$의 coordinate ring이 $\mathbb{K}[\x, \x^{-1}]$이므로 ([예시 2](#ex2)) 곱의 coordinate ring은

$$\mathbb{K}[T] = \mathbb{K}[\x_1^{\pm 1}, \ldots, \x_n^{\pm 1}]$$

이고, Laurent monomial $\x^a$들이 이 ring의 $\mathbb{K}$-basis를 이룬다. 각 $\rchi^a$는 regular function이면서 값이 결코 $0$이 아니고 $\rchi^a(st) = \rchi^a(s)\rchi^a(t)$를 만족하므로 character이다. 또 $\rchi^a \rchi^b = \rchi^{a+b}$이므로 $a \mapsto \rchi^a$는 group homomorphism이고, $\rchi^a$가 상수함수 $1$이면 monomial의 유일성에서 $a = 0$이므로 단사이다.

전사임을 보이자. Character $\rchi \in X^\ast(T)$는 $\mathbb{K}[T]$의 원소이므로 $\rchi = \sum_a c_a \x^a$ (유한합)로 쓸 수 있다. 조건 $\rchi(st) = \rchi(s)\rchi(t)$를 $\mathbb{K}[T \times T] = \mathbb{K}[\x^{\pm 1}, \y^{\pm 1}]$에서 적으면

$$\sum_a c_a \x^a \y^a = \left(\sum_a c_a \x^a\right)\left(\sum_b c_b \y^b\right)$$

이고, $\x^a \y^b$들이 basis이므로 $a \ne b$이면 $c_a c_b = 0$이고 각 $a$에 대해 $c_a^2 = c_a$이다. $\rchi$가 $0$이 아니므로 정확히 하나의 $a$에 대해서만 $c_a = 1$이고 나머지는 $0$이며, 곧 $\rchi = \rchi^a$이다.

마지막 주장은 $\{\x^a\}$와 $\{\rchi^a\}$가 같은 집합이라는 것에 다름아니다.
:::

Torus가 affine algebraic set 위에 작용하면 coordinate ring이 character를 따라 쪼개진다. 이는 [명제 12](#prop12)의 comodule 언어에서 곧바로 나온다.

::: 명제 20
Torus $T$가 affine algebraic set $Y$ 위에 작용한다 하고 $B = \mathbb{K}[Y]$라 하자. 각 character $\rchi \in X^\ast(T)$에 대하여

$$B_\rchi = \{f \in B \mid t \cdot f = \rchi(t) f \text{ for all } t \in T\}$$

라 두면

$$B = \bigoplus_{\rchi \in X^\ast(T)} B_\rchi$$

이다.
:::

::: 증명
$A = \mathbb{K}[T]$라 하고 [명제 12](#prop12)의 comodule structure $\Delta_B: B \rightarrow B \otimes_\mathbb{K} A$를 생각하자. [명제 19](#prop19)에 의해 $X^\ast(T)$가 $A$의 $\mathbb{K}$-basis이므로 각 $f \in B$에 대하여

$$\Delta_B(f) = \sum_\rchi f_\rchi \otimes \rchi$$

로 유일하게 쓸 수 있다. Character는 $\Delta(\rchi) = \rchi \otimes \rchi$를 만족하므로

$$(\id_B \otimes \Delta)\Delta_B(f) = \sum_\rchi f_\rchi \otimes \rchi \otimes \rchi, \qquad (\Delta_B \otimes \id_A)\Delta_B(f) = \sum_\rchi \Delta_B(f_\rchi) \otimes \rchi$$

이고, 두 식을 비교하며 $X^\ast(T)$가 basis임을 쓰면 $\Delta_B(f_\rchi) = f_\rchi \otimes \rchi$, 곧 $t \cdot f_\rchi = \rchi(t) f_\rchi$를 얻는다. 즉 $f_\rchi \in B_\rchi$이며, counit 조건은 $f = \sum_\rchi f_\rchi$를 주므로 $B = \sum_\rchi B_\rchi$이다.

합이 직합임을 보이자. 우선 $f \in B_\rchi$이면 $\Delta_B(f) - f \otimes \rchi$는 $B \otimes_\mathbb{K} A = \mathbb{K}[Y \times T]$의 원소로서 모든 점 $(x,t)$에서 값이 $0$이므로 $\Delta_B(f) = f \otimes \rchi$이다. 따라서 $f_\rchi \in B_\rchi$들에 대해 $\sum_\rchi f_\rchi = 0$이라 하면

$$0 = \Delta_B\left(\sum_\rchi f_\rchi\right) = \sum_\rchi f_\rchi \otimes \rchi$$

이고, $X^\ast(T)$가 basis이므로 모든 $f_\rchi$가 $0$이다.
:::

$B_\rchi$의 $0$이 아닌 원소가 *weight* $\rchi$를 갖는다고 말하고, $B_\rchi$를 $\rchi$의 *weight space*, [명제 20](#prop20)의 분해를 $B$의 *weight decomposition*이라 부른다. $B$가 유한차원이 아니어도 분해가 성립한다는 점과 각 조각이 character 하나로 기술된다는 점이 torus에 특유한 것이며, 이 때문에 torus의 action은 계산 가능한 대상이 된다.

$T = (\mathbb{G}_m)^n$이 $\mathbb{A}^n$ 위에 좌표별 multiplication으로 작용하는 경우 $B = \mathbb{K}[\x_1, \ldots, \x_n]$이고, monomial $\x^b$에 대해 $(t \cdot \x^b)(x) = (t^{-1}x)^b = t^{-b} x^b$이므로 $t \cdot \x^b = \rchi^{-b}(t) \x^b$이며 $\x^b$는 weight $\rchi^{-b}$를 갖는다. 따라서 이 경우 [명제 20](#prop20)의 분해는 다항식을 monomial들의 합으로 적는 것에 지나지 않는다. 반면 $T_n$이 $\GL(n;\mathbb{K})$ 위에 conjugation으로 작용하면 좌표함수 $\x_{ij}$에 대하여

$$(t \cdot \x_{ij})(x) = \x_{ij}(t^{-1}xt) = t_i^{-1} t_j x_{ij}$$

이므로 $\x_{ij}$는 weight $\rchi^{e_j - e_i}$를 가지며, weight decomposition은 행렬성분의 위치를 character로 기록하게 된다.

## Orbit과 homogeneous space

Action이 주어졌을 때 가장 먼저 보게 되는 것은 각 점이 그리는 자취이다.

::: 정의 21
Algebraic group $G$가 $X$ 위에 작용한다 하자. 점 $x \in X$에 대하여 다음을 정의한다.

- $x$의 *orbit<sub>궤도</sub>*은 $G \cdot x = \{g \cdot x \mid g \in G\} \subseteq X$이다.
- $x$의 *stabilizer<sub>안정자</sub>*는 $G_x = \{g \in G \mid g \cdot x = x\} \subseteq G$이다.
- $G$의 *fixed point set<sub>고정점 집합</sub>*은 $X^G = \{x \in X \mid g \cdot x = x \text{ for all } g \in G\}$이다.
:::

각 $x$에 대하여 $\mu_x: G \rightarrow X$, $g \mapsto g \cdot x$는 morphism이므로 $G_x = \mu_x^{-1}(x)$는 $G$의 closed subgroup이다. 또 $\mathbb{P}^n \times \mathbb{P}^n$의 diagonal은 $\x_i\y_j - \x_j\y_i$들의 zero set이므로 닫힌집합이고, $x \mapsto (g \cdot x, x)$의 preimage를 생각하면 각 $g$마다 $\{x \in X \mid g \cdot x = x\}$가 $X$의 닫힌집합이므로 $X^G$도 닫힌집합이다. 이하에서 orbit의 차원이란 그 closure의 차원 $\dim \overline{G \cdot x}$를 뜻하는 것으로 한다.

::: 명제 22
Connected algebraic group $G$가 $X$ 위에 작용한다 하고 $x \in X$라 하자. 그럼 다음이 성립한다.

1. Orbit $G \cdot x$는 $\overline{G \cdot x}$의 열린집합이며 smooth이다.
2. $\overline{G \cdot x} \setminus G \cdot x$는 $G$-invariant인 닫힌집합이고, 그 안에 포함된 모든 orbit의 차원은 $G \cdot x$의 차원보다 작다.
3. $\overline{G \cdot x}$는 closed orbit을 포함한다.
:::

::: 증명
(1) $\mu_x: G \rightarrow \overline{G \cdot x}$는 dominant morphism이다. ([§유리사상, ⁋정의 8](/ko/math/algebraic_varieties/rational_maps#def8)) 일반적으로 dominant morphism의 image는 target의 공집합이 아닌 열린집합을 포함하는데, 이 사실의 증명은 이 글의 범위를 벗어나므로 [Spr]에서 가져다 쓴다. 그럼 $U \subseteq G \cdot x$인 $\overline{G \cdot x}$의 공집합이 아닌 열린집합 $U$가 존재한다. $G \cdot x$가 $G$-invariant이므로 임의의 $g$에 대해 $g \cdot U \subseteq G \cdot x$이고, 임의의 $y = h \cdot x \in G \cdot x$와 $u = k \cdot x \in U$에 대해 $y = (hk^{-1}) \cdot u$이므로

$$G \cdot x = \bigcup_{g \in G} g \cdot U$$

이다. 각 $g \cdot U$는 $\overline{G \cdot x}$의 automorphism $y \mapsto g \cdot y$에 의한 열린집합의 상이므로 열린집합이고, 따라서 $G \cdot x$는 $\overline{G \cdot x}$의 열린집합이다.

$G$가 connected이므로 [명제 5](#prop5)에 의해 irreducible이고, 따라서 $G \cdot x$와 $\overline{G \cdot x}$도 irreducible이다. 앞 문단과 [§준사영다양체, ⁋명제 3](/ko/math/algebraic_varieties/quasi_projective_varieties#prop3)에 의해 $G \cdot x$는 quasi-projective variety이므로 그 smooth point들은 dense open subset을 이루며 ([§접공간과 매끄러움, ⁋명제 10](/ko/math/algebraic_varieties/tangent_spaces_and_smoothness#prop10)), $G$가 $G \cdot x$ 위에 transitive하게 작용하므로 [명제 4](#prop4)의 증명과 같은 논증으로 모든 점이 smooth point이다.

(2) (1)에 의해 $Z = \overline{G \cdot x} \setminus G \cdot x$는 $\overline{G \cdot x}$의 닫힌집합이고, $G \cdot x$가 $G$-invariant이므로 $Z$도 $G$-invariant이다. $G \cdot x$가 $\overline{G \cdot x}$에서 dense이므로 $Z$는 $\overline{G \cdot x}$의 진부분집합이며, $Z$의 각 irreducible component에 [§차원, ⁋명제 9](/ko/math/algebraic_varieties/dimension#prop9)를 적용하면 $\dim Z < \dim \overline{G \cdot x}$를 얻는다. $Z$에 포함된 orbit의 closure는 $Z$에 포함되므로 그 차원은 $\dim Z$ 이하이다.

(3) $\overline{G \cdot x}$에 포함된 orbit들의 차원은 음이 아닌 정수이므로 그 가운데 차원이 최소인 orbit $O$가 존재한다. 만일 $O$가 닫혀 있지 않다면 (1)에 의해 $\overline{O} \setminus O$는 공집합이 아니고, 이 집합은 $G$-invariant이므로 orbit을 포함한다. 그럼 (2)를 $O$에 적용하여 그 orbit의 차원이 $O$의 차원보다 작음을 얻으므로 $O$의 최소성에 모순이다. 따라서 $O$는 closed orbit이다.
:::

Connected가 아닌 $G$에 대해서는 $G^\circ$로 바꾸어 생각하면 된다. [명제 5](#prop5)에 의해 $G$의 orbit은 $G^\circ$의 orbit 유한개의 합집합이고, 이들은 서로 isomorphic하므로 차원이 같기 때문이다.

::: 예시 23
1. $\mathbb{G}_m$이 $\mathbb{A}^1$ 위에 multiplication으로 작용하면 orbit은 $\{0\}$과 $\mathbb{A}^1 \setminus \{0\}$ 둘뿐이다. 후자는 열린집합이고 그 closure가 $\mathbb{A}^1$이며 그 boundary가 closed orbit $\{0\}$이므로, 이는 [명제 22](#prop22)가 기술하는 상황의 가장 단순한 예이다. 한편 모든 $t$에 대해 $t \cdot f = f$를 만족하는 $f \in \mathbb{K}[\x]$는 상수뿐이므로, invariant function으로 두 orbit을 구별할 수 없다. 이처럼 orbit들의 집합은 일반적으로 variety 구조를 자연스럽게 물려받지 못한다.
2. $\GL(2;\mathbb{K})$가 $2 \times 2$ 행렬들의 공간 $\mathbb{A}^4$ 위에 conjugation으로 작용한다 하자. 좌표를 $\x_{11}, \x_{12}, \x_{21}, \x_{22}$로 적는다. $a \ne b$일 때 $\operatorname{diag}(a,b)$의 orbit은 characteristic polynomial이 $(\lambda - a)(\lambda - b)$인 행렬들 전체와 같은데, 그러한 행렬은 서로 다른 두 eigenvalue를 가져 모두 대각화되기 때문이다. 이 집합은 $\tr = a + b$와 $\det = ab$가 정의하는 닫힌집합이므로 closed orbit이다. 또 $\x_{22} = a + b - \x_{11}$을 대입하면 이 집합은 $\mathbb{A}^3$ 안의 hypersurface

    $$\x_{12}\x_{21} + (\x_{11} - a)(\x_{11} - b) = 0$$

    과 isomorphic한데, 좌변은 $\x_{12}$에 대하여 일차이고 그 두 계수 $\x_{21}$과 $(\x_{11} - a)(\x_{11} - b)$가 서로소이므로 irreducible이다. 따라서 이 orbit의 차원은 $2$이다. ([§차원, ⁋명제 6](/ko/math/algebraic_varieties/dimension#prop6))

    반면

    $$J = \begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix}$$

    의 orbit은 eigenvalue가 $a$뿐이면서 대각화되지 않는 행렬들, 곧 $(A - aI)^2 = 0$이고 $A \ne aI$인 $A$들 전체이다. Cayley–Hamilton 정리에 의해 $N = A - aI$에 대한 조건 $N^2 = 0$은 $\tr N = \det N = 0$과 동치이므로, $\x_{22} = 2a - \x_{11}$을 대입하면 이 orbit은 $\mathbb{A}^3$ 안의 quadric cone

    $$(\x_{11} - a)^2 + \x_{12}\x_{21} = 0$$

    에서 꼭짓점 하나를 뺀 것과 isomorphic하다. 좌변도 위와 같은 이유로 irreducible이므로 이 cone은 차원 $2$의 irreducible hypersurface이고, orbit은 그 안의 공집합이 아닌 열린집합이므로 $\overline{G \cdot J}$는 cone 전체이며 $G \cdot J$의 차원은 $2$이다. 실제로

    $$\begin{pmatrix} t & 0 \\ 0 & 1 \end{pmatrix} J \begin{pmatrix} t & 0 \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} a & t \\ 0 & a \end{pmatrix}$$

    이므로 $t$가 $\mathbb{G}_m$ 위를 움직일 때 얻어지는 행렬들의 closure는 $t = 0$에 해당하는 $aI$를 포함한다. 즉 $G \cdot J$는 닫혀 있지 않으며, 그 boundary는 차원 $0$인 closed orbit $\{aI\}$이다.
:::

Orbit들의 집합 자체에 기하학적 구조를 주는 일반론은 geometric invariant theory에서 다룬다. 여기서는 그 대신 orbit 하나가 variety로서 어떻게 생겼는지만 살펴본다. Orbit $G \cdot x$는 집합으로서 coset space $G/G_x$와 같으므로, 자연스러운 질문은 임의의 closed subgroup $H \subseteq G$에 대하여 $G/H$가 variety 구조를 갖는지의 여부일 것이다.

::: 정리 24
Algebraic group $G$와 그 closed subgroup $H$에 대하여, 다음을 만족하는 quasi-projective algebraic set $G/H$와 morphism $\pi: G \rightarrow G/H$가 존재한다.

1. $\pi$는 전사이고 그 fiber들은 정확히 $H$의 left coset들이다.
2. $G$는 $G/H$ 위에 transitive하게 작용하고 $\pi$는 이 작용에 대해 equivariant이며, $\pi(e)$의 stabilizer는 $H$이다.
3. $\dim G/H = \dim G - \dim H$이다.
:::

::: 증명
이 정리의 증명은 이 글의 범위를 벗어나므로 [Spr]와 [Hum]에 위임하고, 무엇을 가져다 쓰는지만 밝힌다. 핵심 재료는 [정리 16](#thm16)을 정교하게 만든 결과로, $G$의 representation $\rho: G \rightarrow \GL(V)$와 $1$차원 부분공간 $L \subseteq V$가 존재하여

$$H = \{g \in G \mid \rho(g)L = L\}$$

이 되도록 할 수 있다는 것이다. 이를 얻고 나면 $G$는 $V$의 직선들의 공간 $\mathbb{P}(V)$ 위에 작용하고 ([§그라스만 다양체, ⁋예시 2](/ko/math/algebraic_varieties/grassmannians#ex2)), $L$에 해당하는 점의 orbit이 [명제 22](#prop22)와 같은 논증으로 locally closed subset이 되므로 이것을 $G/H$로 삼으면 된다. 차원에 대한 주장 역시 같은 문헌에 함께 있다.
:::

$\operatorname{char}\mathbb{K} = 0$일 때에는 더 나아가, $G$가 $X$ 위에 transitive하게 작용하면 $x \in X$에 대해 $gG_x \mapsto g \cdot x$가 유도하는 morphism $G/G_x \rightarrow X$가 isomorphism이 된다. 양의 characteristic에서는 이것이 bijective morphism이기는 하나 isomorphism이 아닐 수 있다. Transitive한 action이 주어진 variety를 *homogeneous space*라 부르며, 위의 사실은 homogeneous space가 언제나 $G/H$ 꼴로 나타남을 말해준다.

::: 예시 25
이 예시에서는 $\operatorname{char}\mathbb{K} = 0$을 가정한다. $\GL(n;\mathbb{K})$는 Grassmannian $\Gr(k, n)$ 위에 $g \cdot W = g(W)$로 작용한다. ([§그라스만 다양체, ⁋정의 1](/ko/math/algebraic_varieties/grassmannians#def1)) 임의의 $k$차원 부분공간의 basis를 전체 공간의 basis로 확장할 수 있으므로 이 action은 transitive하다. Standard subspace $W_0 = \operatorname{span}(e_1, \ldots, e_k)$의 stabilizer는 $W_0$을 보존하는 가역행렬들, 곧 왼쪽 아래 $(n-k) \times k$ block이 $0$인 행렬들의 집합

$$P = \left\{ \begin{pmatrix} A & B \\ 0 & D \end{pmatrix} \in \GL(n;\mathbb{K}) \right\}$$

이며 이는 closed subgroup이다. 따라서 앞 문단에 의해

$$\Gr(k, n) \cong \GL(n;\mathbb{K})/P$$

이다. 이 표현에서 차원을 세면 $\dim P = k^2 + (n-k)^2 + k(n-k) = n^2 - k(n-k)$이므로 [정리 24](#thm24)에 의해

$$\dim \Gr(k, n) = n^2 - \dim P = k(n-k)$$

이고, 이는 [§그라스만 다양체, ⁋명제 5](/ko/math/algebraic_varieties/grassmannians#prop5)와 일치한다. $k = 1$인 경우가 $\mathbb{P}^{n-1} \cong \GL(n;\mathbb{K})/P$이다. 양의 characteristic에서도 같은 isomorphism이 성립하지만, 그것을 확인하려면 orbit map $\GL(n;\mathbb{K}) \rightarrow \Gr(k, n)$이 separable이라는 사실이 필요하므로 여기서는 [Spr]에 맡긴다.
:::

---

**참고문헌**

**[Spr]** T. A. Springer, *Linear Algebraic Groups*, Birkhäuser, 1998.  
**[Hum]** J. E. Humphreys, *Linear Algebraic Groups*, Springer, 1975.  
**[Mil]** J. S. Milne, *Algebraic Groups*, Cambridge University Press, 2017.  
**[MFK]** D. Mumford, J. Fogarty, F. Kirwan, *Geometric Invariant Theory*, Springer, 1994.
