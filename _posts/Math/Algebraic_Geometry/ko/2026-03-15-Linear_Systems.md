---
title: "선형계"
excerpt: "Complete linear systems, base loci, and ampleness"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/linear_systems
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Linear_Systems.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-15
weight: 10

published: false
---

앞서 우리는 [§인자, ⁋정의 1](/ko/math/algebraic_geometry/divisors#def1)에서 variety $$X$$의 (Weil) divisor를 정의하였다. Zariski topology의 정의에 의하여, 이는 기본적으로 $$X$$ 위에 정의된 어떤 <em-ko>함수</em-ko>의 zero set에, 이 zero의 order를 더한 것으로 생각할 수 있으며, 이를 $$\mathbb{P}^n$$과 같은 경우에도 잘 정의하기 위해 우리는 <em-ko>함수</em-ko>를 <em-ko>적당한 line bundle의 section</em-ko>으로 일반화했다. 

한편, divisor는 음수 계수 또한 허용하므로 이 zero set은 zero set이 아니라, 음수 order의 zero, 즉 pole이 될 수도 있다. 이런 경우 우리는 주어진 divisor와 linearly equivalent한 *effective* divisor를 찾은 후, 이 성질을 탐구할 수 있다. ([§인자, ⁋정의 7](/ko/math/algebraic_geometry/divisors#def7)) 

위에서 우리는 서술의 편의상 Weil divisor에 대한 논의만 하였지만, Cartier divisor에 대해서도 비슷한 논증을 할 수 있으며, 그 결과로 나오는 정의는 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위에 정의된 Weil divisor $$D=\sum n_i D_i$$가 *effective*라는 것은 모든 $$i$$에 대해 $$n_i\geq 0$$인 것이다. Cartier divisor $$\{(U_i, f_i)\}$$가 *effective*라는 것은 모든 $$i$$에 대해 $$f_i$$가 $$U_i$$ 위에서 regular인 것이다. 

</div>

그렇다면 우리의 목적은 divisor $$D$$의 divisor class 안에서 어떠한 effective divisor가 존재하는지 살펴보는 것이다. 이를 위해 divisor $$D$$가 정의하는 line bundle $$\mathcal{L}=\mathcal{O}_X(D)$$를 생각하자. ([§선다발과 벡터다발, ⁋정의 17](/ko/math/algebraic_geometry/line_bundles#def17)) 우리는 $$\mathcal{L}$$의 각각의 nonzero global section $$s\in H^0(X, \mathcal{L})$$는 pole이 없으므로 effective divisor $$\divisor(s)$$를 정의하며, 이는 원래의 $$D$$와 trivialization만큼만 차이나는 것을 확인할 수 있으므로 $$D$$와 linearly equivalent하다. 즉 $$D$$와 linearly equivalent한 effective divisor를 찾기 위해선 $$\mathcal{O}_X(D)$$의 nonzero global section을 보면 된다. 다만 주의할 사항은 $$\divisor(s)$$는 $$s$$ 자체가 아니라 $$s$$의 nonzero multiple에 의존한다는 것으로, 이때문에 우리가 관심을 가져야할 대상은 $$H^0(X, \mathcal{L})$$ 자체가 아니라 그 projectivization이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$ 위의 line bundle $$\mathcal{L}$$에 대하여, $$\mathcal{L}$$의 *complete linear system*은 $$\mathcal{L}$$의 global section space $$H^0(X, \mathcal{L})$$의 projectivization

$$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$

이다. $$\mathcal{L}$$에 대한 *linear system*은 $$\lvert \mathcal{L} \rvert$$의 nonempty projective subspace이다. 즉, 부분벡터공간 $$V \subseteq H^0(X, \mathcal{L})$$에 대해 $$\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$$의 꼴이다.

</div>


## Projective space의 linear system

앞서 [§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12) 이후의 계산에 의해 $$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$가 차수 $$d$$의 동차다항식들의 공간 $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$와 동형임을 보았다. 이 공간의 각 원소들은 $$\mathbb{P}^n$$의 degree $$d$$ hypersurface를 정의하므로, 우리는 $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d)\rvert=\mathbb{P}(H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)))\cong \mathbb{P}(\mathbb{K}[\x_0,\ldots, \x_n]_d)\cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

을 기하적으로 degree $$d$$ hypersurface in $$\mathbb{P}^n$$들의 family로 이해할 수 있다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 편의상 $$n=2$$로 고정하자. 그럼 degree $$1$$ hypersurface들, 즉 $$\mathbb{P}^2$$의 직선들의 family는 $$\mathbb{P}^2$$ 자기자신과 isomorphic하다. 더 자세히 살펴보면, 

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)\cong \mathbb{P}^{\binom{3}{1}-1}=\mathbb{P}^2$$

에서 우변 $$\mathbb{P}^2$$의 한 점 $$[a_0:a_1:a_2]$$는 $$\mathbb{P}^2$$의 한 직선 $$Z(a_0\x_0+a_1\x_1+a_2\x_2)$$을 정의한다. 

조금 더 복잡하고 기하적인 예시를 위해, 우리는 $$\mathbb{P}^2$$ 위의 line bundle $$\mathcal{O}_{\mathbb{P}^2}(2)$$가 정의하는 complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^2}(2)\rvert\cong \mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_2)\cong \mathbb{P}^{\binom{3}{2}-1}=\mathbb{P}^5$$

의 1차원 부분공간 (즉 $$1$$차원 linear system)을 생각하자. 대표적인 예시는 두 conic의 *pencil*이다. $$\mathbb{P}^2$$에서 정의된 두 conic $$C_1=Z(F_1)$$, $$C_2=Z(F_2)$$을 생각하자. 그럼 $$C_1$$과 $$C_2$$가 동일한 conic이 아닌 한, 이들의 linear combination

$$Z(\lambda F_1+\mu F_2)$$

은 $$\mathbb{P}^2$$의 또 다른 degree $$2$$ curve이며, 정의에 의해 이들 conic은 모두 $$C_1\cap C_2$$를 지나게 된다. 이 때, 점 $$[\lambda:\mu]\in \mathbb{P}^1$$이 이들 conic을 parametrize한다. 

더 구체적인 예시를 위해, $$\mathbb{P}^2$$에서의 두 conic

$$C_1: Z((\x_0-2\x_2)^2+\x_1^2-9\x_2^2),\qquad C_2: Z((\x_0+2\x_2)^2+\x_1^2-9\x_2^2)$$

을 생각하자. 이 식은 그 자체로는 복잡해보이지만 $$U_2$$로 제한하면 두 원

$$(\x-2)^2+\y^2=9,\qquad (\x+2)^2+\y^2=9$$

의 방정식이다. 이들은 $$U_2$$ 위에서는 위의 두 식으로부터 계산되는 $$(x,y)=(0,\pm\sqrt{5})$$에서 만나며, $$U_2$$ 바깥 --- 즉 $$U_2$$의 <em_ko>무한대 직선</em_ko>[^1] --- 에서는 두 점 $$[1,i:0]$$, $$[1, -i:0]$$에서 만난다. 위의 pencil $$Z(\lambda F_1+\mu F_2)$$는, 그럼 이들 교집합 $$C_1\cap C_2$$을 지나는 conic들의 모임이다. 

한편 일반적인 degree 2 homogeneous polynomial은

$$F(\x_0,\x_1,\x_2) = a_{00}\x_0^2 + a_{11}\x_1^2 + a_{22}\x_2^2 + a_{01}\x_0\x_1 + a_{02}\x_0\x_2 + a_{12}\x_1\x_2$$

의 꼴이며, 이것이 정확히 $$H^0(X, \mathcal{O}(2))$$가 $$6$$차원 공간인 이유이다. 한편, 위에서 계산한 네 점짜리 집합 $$C_1\cap C_2$$를 지나야 한다는 조건을 추가한다면, 이들 네 점이 각각 하나씩의 제약조건을 걸이 필요한 parameter를 하나씩 지워주므로 이를 나타내기 위한 parameter는 2개임을 안다. 더 구체적으로, 다음 네 개의 조건

$$0=F(0,\sqrt{5},1)=5a_{11}+a_{22}+\sqrt{5}a_{12}$$

$$0=F(0,-\sqrt{5},1)=5a_{11}+a_{22}-\sqrt{5}a_{12}$$

$$0=F(1,i,0)=a_{00}-a_{11}+ia_{01}$$

$$0=F(1,-i,0)=a_{00}-a_{11}-ia_{01}$$

이 $$a_{12}=0$$, $$a_{01}=0$$, $$5a_{11}=-a_{22}$$, $$a_{00}=a_{11}$$을 강제하므로 실질적인 변수는 $$a_{00}$$, $$a_{02}$$의 두 개이다. 즉, 이들 conic의 모임은 $$H^0(X,\mathcal{O}(2))$$의 2차원 부분공간 $$V$$를 이룰 것이며, 이를 projectivize한 것이 $$[\lambda:\mu]$$로 나타나는 $$\mathbb{P}^1$$이 된다. 

img

</div>

물론 [정의 2](#def2)는 $$X$$가 projective space이든 quasi-projective variety이든 임의의 variety에 동일하게 적용된다. 그러나 우리가 위의 [예시 3](#ex3)을 이렇게 공들여 계산한 이유는, 임의의 quasi-projective variety $$X\subseteq \mathbb{P}^n$$에 대해서도 $$D$$가 어떠한 $$\mathcal{O}_{\mathbb{P}^n}(d)$$에서 온다면 homogeneous polynomial의 언어를 그대로 사용할 수 있기 때문이다. 즉 이 경우 restriction map

$$H^0(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)) \to H^0(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X)$$

은 homogeneous polynomial $$F \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$를 $$X$$ 위의 section으로 보내며, 그 kernel은 $$I(X)$$의 차수 $$d$$인 homogeneous part $$I(X)_d$$이다. 따라서

$$H^0(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d / I(X)_d$$

로서 $$\mathbb{P}^n$$에서와 본질적으로 동일한 계산이 가능하다. 특히 $$F - G \in I(X)$$일 때 같은 교차를 정의하므로, parameter space는 $$\mathbb{P}(V/(V \cap I(X)))$$가 된다.

## Base Locus

우리는 남은 글에서 $$X$$의 linear system $$L=\mathbb{P}(V)$$와 $$V$$의 basis $$F_0,\ldots, F_r$$이 주어졌을 때, 이를 사용하여 embedding

$$\varphi_L:X\rightarrow \mathbb{P}^r;\qquad x\mapsto [F_0(x):\cdots:F_r(x)]$$

을 정의한다. 

물론 이것이 항상 가능한 것은 아니다. 가령 [예시 3](#ex3)에서, $$(a_{00},a_{02})=(1,0), (0,1)$$에 해당하는 다음의 두 basis

$$F_1(\x_0,\x_1,\x_2)=\x_0^2+\x_1^2-5\x_2^2, \qquad F_2(\x_0,\x_1,\x_2)=\x_0\x_2$$

를 택하면 이 "embedding"은

$$\mathbb{P}^2\rightarrow \mathbb{P}^1;\qquad [\x_0,\x_1,\x_2]\mapsto [\x_0^2+\x_1^2-5\x_2^2:\x_0\x_2]$$

이 된다. 이는 우선 $$\mathbb{P}^2$$에서 더 작은 공간 $$\mathbb{P}^1$$로 가는 함수이므로 어딘가 잘못되었다는 것을 알고 있고, 이는 두 함수 $$F_1,F_2$$가 동시에 $$0$$이 되는 부분이 존재하기 때문이다.



이 대응 자체는 $$F_i$$들의 선택에 의존하지만, 이 대응의 여러 성질들은 $$F_i$$의 선택에 의존하지 않는다는 것을 곧 살펴보게 될 것이다.

이 대응이 정의되기 위해서는 우선 모든 $$F_i$$에 대하여 $$F_i(x)=0$$이도록 하는 $$x$$가 존재하면 곤란할 것이다. 


[예시 3](#ex3)의 conic pencil에서 우리는 $$H^0(\mathbb{P}^2, \mathcal{O}(2))$$의 차원이 $$6$$인 반면, $$C_1 \cap C_2$$의 네 점을 모두 지나야 한다는 조건이 parameter를 $$6$$개에서 $$2$$개로 줄여 $$\mathbb{P}^5 \to \mathbb{P}^1$$로 차원이 감소함을 보았다. 이처럼 linear system의 원소들이 모두 지나는 점들이 존재하면, 이 점들은 parameter space의 차원을 낮추는 제약으로 작용한다. 이런 공통점들의 집합을 *base locus*라 하며, base locus가 존재하면 linear system이 정의하는 사상에서 문제가 생긴다. 사실 linear system $$L = \mathbb{P}(V)$$는 variety에서 사영공간으로의 정칙사상을 자연스럽게 정의한다 --- 이에 대해서는 [명제 8](#prop8)에서 자세히 살펴볼 것이다. Base locus가 존재하면 이 사상을 정의할 수 없게 되는데, base locus의 모든 점에서 모든 section이 동시에 zero가 되어 사상의 값을 결정할 수 없기 때문이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Linear system $$L \subseteq \lvert \mathcal{L} \rvert$$의 *base locus* $$\operatorname{Bs}(L)$$는 $$L$$의 모든 원소가 공유하는 closed subset이다. 구체적으로, $$L = \mathbb{P}(V)$$에서 $$V \subseteq H^0(X, \mathcal{L})$$일 때,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\operatorname{div}(s))$$

여기서 $$\operatorname{div}(s)$$는 section $$s$$의 zero divisor이다. $$\mathbb{P}^n$$의 hypersurface 계산에서는 $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$에 대해 $$\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$$와 동일하다.

</div>

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$L$$이 *basepoint-free*라는 것은 $$\operatorname{Bs}(L) = \emptyset$$인 것이다. 즉, 임의의 점 $$p \in X$$에서 $$p$$를 지나지 않는 $$L$$의 원소가 항상 존재한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> **$$\mathbb{P}^n$$의 hyperplane system**: $$\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert = \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_1)$$는 basepoint-free이다. 임의의 점 $$p = [p_0 : \cdots : p_n] \in \mathbb{P}^n$$에 대해, $$p$$를 지나지 않는 hyperplane $$Z(\x_i)$$ (단, $$p_i \ne 0$$인 $$i$$를 택함)이 존재하기 때문이다. 즉, $$p \notin \operatorname{Bs}(\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert)$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> **Pencil의 base locus**: [예시 3](#ex3)의 conic pencil의 base locus는 $$C_1 \cap C_2$$이다. Bézout's theorem ([§Bézout 정리](/ko/math/algebraic_geometry/bezout_theorem))에 의해, $$\mathbb{P}^2$$에서 두 conic의 교차는 (중복도를 포함하여) 4개의 점으로 구성된다. [예시 3](#ex3)에서 본 것처럼, 두 원의 경우 아핀 부분에서 2개의 실수 교점을 보이지만, 무한원에서 2개의 복소수 교점을 추가로 가지므로 총 4개로 일치한다.

</div>

사실 base locus가 있는 linear system에 대해서도, base locus를 blow-up하면 사상을 정의할 수 있다. 이에 대해서는 [§Rational map](/ko/math/algebraic_geometry/rational_maps)에서 다룬다.

따라서 base locus가 존재하면 linear system으로부터 사상을 얻을 수 없으므로, basepoint-free가 사상을 정의하기 위한 자연스러운 조건임을 알 수 있다. 실제로 이 조건이 충족되면 linear system은 variety에서 사영공간으로의 정칙사상을 부여한다.

## Basepoint-Free Linear System이 정의하는 사상

Basepoint-free linear system의 핵심 성질은, 이것이 다양체에서 사영공간으로의 사상을 자연스럽게 정의한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Quasiprojective variety $$X \subseteq \mathbb{P}^n$$ 위의 basepoint-free linear system $$L = \mathbb{P}(V)$$에서, $$V$$의 기저 $$F_0, \ldots, F_r \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$가 다음 조건을 만족한다고 하자:

$$\bigcap_{i=0}^r Z(F_i) \cap X = \emptyset$$

그러면 $$V$$는 $$X$$에서 사영공간으로의 정칙사상

$$\varphi_L: X \to \mathbb{P}^r, \quad p \mapsto [F_0(p) : \cdots : F_r(p)]$$

을 정의한다. 여기서 $$F_i(p)$$는 $$F_i$$의 $$p$$에서의 값을 나타낸다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\varphi_L$$이 well-defined임을 보여야 한다. $$p \in X$$일 때, $$p \in \operatorname{Bs}(L) = \emptyset$$이므로 어떤 $$i$$에 대해 $$F_i(p) \ne 0$$이다. 따라서 $$[F_0(p) : \cdots : F_r(p)]$$는 $$\mathbb{P}^r$$의 정상적인 점이다.

다음으로 $$\varphi_L$$이 정칙사상임을 보이자. $$X$$의 affine open cover $$U_\alpha = X \cap (\mathbb{P}^n \setminus Z(\x_\alpha))$$를 생각하자. 여기서 $$\x_\alpha$$는 $$\mathbb{P}^n$$의 standard homogeneous coordinate이다. 각 $$U_\alpha$$에서 $$\x_\alpha \ne 0$$이므로, $$F_i / \x_\alpha^d$$는 $$U_\alpha$$에서 정의되는 regular function이다. $$\varphi_L$$의 $$j$$번째 좌표는 이 regular function들의 비율로 나타나므로, $$\varphi_L$$은 $$U_\alpha$$에서 정칙사상이다.

</details>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> **Rational normal curve**: $$\mathbb{P}^1$$에서 $$d \ge 1$$일 때, $$\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$$의 complete linear system이 정의하는 사상은 *Veronese 사상* 또는 *rational normal curve*이라 불린다.

$$\nu_d: \mathbb{P}^1 \to \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d]$$

이 사상의 image는 $$\mathbb{P}^d$$에서 degree $$d$$의 *rational normal curve*이다. $$d = 2$$일 때는 $$\mathbb{P}^2$$의 conic, $$d = 3$$일 때는 $$\mathbb{P}^3$$의 twisted cubic이다.

</div>

## Very Ample과 Ample

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Line bundle $$\mathcal{L}$$ (또는 대응하는 linear system $$\lvert \mathcal{L} \rvert$$)이 *very ample*이라는 것은, complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(H^0(X, \mathcal{L}))$$이 정의하는 사상 $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(H^0(X, \mathcal{L}))$$이 closed embedding인 것이다.

</div>

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> $$\mathcal{L}$$이 *ample*이라는 것은 어떤 $$m > 0$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample인 것이다.

</div>

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Very ample line bundle은 항상 basepoint-free이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\varphi_{\mathcal{L}}: X \hookrightarrow \mathbb{P}^r$$이 embedding이면 모든 점에서 정의된다. $$\varphi_{\mathcal{L}}(p) = [s_0(p) : \cdots : s_r(p)]$$ (여기서 $$s_0, \ldots, s_r$$은 $$H^0(X, \mathcal{L})$$의 기저)이므로, 각 $$p \in X$$에 대해 어떤 $$i$$가 $$s_i(p) \ne 0$$이다. 따라서 $$\operatorname{Bs}(\lvert \mathcal{L} \rvert) = \emptyset$$이다.

</details>

<div class="example" markdown="1">

<ins id="ex13">**예시 13**</ins> **$$\mathcal{O}_{\mathbb{P}^n}(1)$$은 very ample**: $$\lvert \mathcal{O}_{\mathbb{P}^n}(1) \rvert = \mathbb{P}(\mathbb{K}[\x_0, \ldots, \x_n]_1)$$는 identity embedding $$\mathbb{P}^n \hookrightarrow \mathbb{P}^n$$을 정의한다. $$F_i = \x_i$$로 놓으면 $$\varphi_L([x_0 : \cdots : x_n]) = [x_0 : \cdots : x_n]$$이다.

</div>

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> **$$\mathcal{O}_{\mathbb{P}^n}(d)$$도 very ample**: $$d > 0$$이면 $$\lvert \mathcal{O}_{\mathbb{P}^n}(d) \rvert$$는 *Veronese embedding*

$$\nu_d: \mathbb{P}^n \hookrightarrow \mathbb{P}^N, \quad [x_0 : \cdots : x_n] \mapsto [x_0^{a_0} \cdots x_n^{a_n} \text{ (모든 차수 } d \text{의 monomial, } \sum a_i = d)]$$

을 정의한다. 여기서 $$N = \binom{n+d}{d} - 1$$이다. 이 사상은 $$\mathbb{P}^n$$을 $$\mathbb{P}^N$$의 smooth degree $$d$$의 subvariety로 embedding한다.

</div>

Very ample의 정의에서 핵심은 사상이 단순한 morphism이 아니라 **closed embedding**이라는 점이다. Closed embedding $$X \hookrightarrow \mathbb{P}^r$$이 주어지면, $$X$$는 $$\mathbb{P}^r$$ 위의 어떤 homogeneous ideal의 zero set으로 실현되며, 따라서 $$X$$의 모든 기하학적 정보가 사영공간 안에서 읽어낼 수 있게 된다. 실제로 projective variety의 본질적 정의는 "어떤 사영공간의 closed subvariety"인 것이며, [§사영다양체](/ko/math/algebraic_geometry/projective_varieties)에서 다루었듯 quasi-projective variety와의 구별도 여기에 있다. 이 관점에서, $$\mathcal{L}$$이 very ample이라는 것은 $$\mathcal{L}$$ 자체가 $$X$$를 사영공간에 넣는 "좌표"를 제공한다는 의미를 갖는다.

Ample line bundle은 대수기하학에서 가장 중요한 개념 중 하나이다. 정의 11은 "충분히 큰 거듭제곱이 very ample"이라는 형태로만 ample을 규정하지만, 이 정의는 다음과 같은 깊은 결과들과 연결된다. 첫째, $$\mathcal{L}$$이 ample이면 충분히 큰 $$m$$에 대해 complete linear system $$\lvert \mathcal{L}^{\otimes m} \rvert$$가 basepoint-free이고 매우 자유로운 (sufficiently ample) section들을 제공하며, 이를 통해 $$X$$ 위의 임의의 coherent sheaf에 대해 Serre's vanishing theorem $$H^i(X, \mathcal{F} \otimes \mathcal{L}^{\otimes m}) = 0$$ (for $$m \gg 0$$, $$i > 0$$)이 성립한다. 둘째, $$\mathcal{L}$$이 ample이면 $$\lvert \mathcal{L}^{\otimes m} \rvert$$는 매우 다양한 effective divisor를 parameterize하며, $$X$$의 인자 이론에서 기본적인 역할을 수행한다. 셋째, projective variety의 분류론에서 ample (또는 그 일반화인 nef, big) line bundle의 존재 여부는 variety의 기하학적 성질을 결정하는 핵심 정보이다.

Complex geometry와의 연결에서, **Kodaira embedding 정리**는 다음을 assertion한다. Compact complex manifold $$X$$ 위의 line bundle $$\mathcal{L}$$에 대해, $$\mathcal{L}$$이 positive curvature를 갖는 Hermitian metric을 인정하는 것 (complex-analytic positivity)은 $$\mathcal{L}$$이 ample인 것과 동치이다. 대수기하학적으로는, smooth projective variety $$X$$ 위의 line bundle $$\mathcal{L}$$이 ample인 것과 $$\mathcal{L}^{\otimes m}$$이 very ample인 것은 정의 11에 의해 동치이다. Kodaira embedding 정리의 본질은 이 대수적 조건이 해석적 조건 — positive curvature를 갖는 Hermitian metric의 존재 — 과 동치라는 점에 있다. 증명의 핵심 아이디어는, ample line bundle의 section들이 $$X$$를 사영공간에 embed하기에 충분하다는 점과, 이 embedding의 image가 사실 대수적 variety라는 것을 보이는 데 있다. (증명은 생략한다.)

이 글 전체의 narrative를 정리하자. 우리는 divisor에서 출발하여, 이를 line bundle의 section으로 reinterpret하고, linear system의 개념을 통해 section들의 family를 parameterize하였다. Base locus의 관념은 linear system이 사영공간으로의 사상을 정의할 수 있는지의 여부를 결정하며, basepoint-free linear system은 자연스럽게 morphism $$\varphi_L$$를 부여한다. 이 morphism이 closed embedding이 되는 조건이 바로 very ample의 정의이고, 충분한 거듭제곱에서 이 조건을 만족하는 것이 ample의 정의이다. 따라서

$$\text{Ample} \subseteq \text{Very ample} \subseteq \text{Basepoint-free}$$

라는 포함 관계를 얻으며, 가장 강한 조건인 ample line bundle은 사영다양체의 구조를 사영공간 안에서 이해하는 데 필요한 핵심 도구이다. Projective variety는 정의상 어떤 사영공간의 closed subvariety이므로, 결국 모든 projective variety는 어떤 ample line bundle을 가지며, 그 ample line bundle을 통해 variety의 인자 이론, 기하학, 그리고 분류를 연구할 수 있다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: $$\mathbb{P}^2$$의 <em-ko>무한대 직선</em-ko>과 그 기하적인 직관에 대해서는 [§사영다양체, ⁋예시 11](/ko/math/algebraic_geometry/projective_varieties#ex11)에서 이미 분석하였다. 