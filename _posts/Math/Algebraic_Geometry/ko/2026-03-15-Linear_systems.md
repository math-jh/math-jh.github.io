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
last_modified_at: 2026-03-29
weight: 10
---

앞서 우리는 [§인자, ⁋정의 1](/ko/math/algebraic_geometry/divisors#def1)에서 variety $$X$$의 (Weil) divisor를 정의하였다. Zariski topology의 정의에 의하여, 이는 기본적으로 $$X$$ 위에 정의된 어떤 <em-ko>함수</em-ko>의 zero set에, 이 zero의 order를 더한 것으로 생각할 수 있으며, 이를 $$\mathbb{P}^n$$과 같은 경우에도 잘 정의하기 위해 우리는 <em-ko>함수</em-ko>를 <em-ko>적당한 line bundle의 section</em-ko>으로 일반화했다. 

한편, divisor는 음수 계수 또한 허용하므로 이 zero set은 zero set이 아니라, 음수 order의 zero, 즉 pole이 될 수도 있다. 이런 경우 우리는 주어진 divisor와 linearly equivalent한 *effective* divisor를 찾은 후, 이 성질을 탐구할 수 있다. ([§인자, ⁋정의 7](/ko/math/algebraic_geometry/divisors#def7)) 

위에서 우리는 서술의 편의상 Weil divisor에 대한 논의만 하였지만, Cartier divisor에 대해서도 비슷한 논증을 할 수 있으며, 그 결과로 나오는 정의는 다음과 같다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Variety $$X$$ 위에 정의된 Weil divisor $$D=\sum n_i D_i$$가 *effective*라는 것은 모든 $$i$$에 대해 $$n_i\geq 0$$인 것이다. Cartier divisor $$\{(U_i, f_i)\}$$가 *effective*라는 것은 모든 $$i$$에 대해 $$f_i$$가 $$U_i$$ 위에서 regular인 것이다. 

</div>

그렇다면 우리의 목적은 divisor $$D$$의 divisor class 안에서 어떠한 effective divisor가 존재하는지 살펴보는 것이다. 이를 위해 divisor $$D$$가 정의하는 line bundle $$\mathcal{L}=\mathcal{O}_X(D)$$를 생각하자. ([§선다발과 벡터다발, ⁋정의 17](/ko/math/algebraic_geometry/line_bundles#def17)) 우리는 $$\mathcal{L}$$의 각각의 nonzero global section $$s\in \Gamma(X, \mathcal{L})$$는 pole이 없으므로 effective divisor $$\divisor(s)$$를 정의하며, 이는 원래의 $$D$$와 trivialization만큼만 차이나는 것을 확인할 수 있으므로 $$D$$와 linearly equivalent하다. 즉 $$D$$와 linearly equivalent한 effective divisor를 찾기 위해선 $$\mathcal{O}_X(D)$$의 nonzero global section을 보면 된다. 다만 주의할 사항은 $$\divisor(s)$$는 $$s$$ 자체가 아니라 $$s$$의 nonzero multiple에 의존한다는 것으로, 이때문에 우리가 관심을 가져야할 대상은 $$\Gamma(X, \mathcal{L})$$ 자체가 아니라 그 projectivization이다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Variety $$X$$ 위의 line bundle $$\mathcal{L}$$에 대하여, $$\mathcal{L}$$의 *complete linear system*은 $$\mathcal{L}$$의 global section space $$\Gamma(X, \mathcal{L})$$의 projectivization

$$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$$

이다. $$\mathcal{L}$$에 대한 *linear system*은 $$\lvert \mathcal{L} \rvert$$의 nonempty projective subspace이다. 즉, 부분벡터공간 $$V \subseteq \Gamma(X, \mathcal{L})$$에 대해 $$\mathbb{P}(V) \subseteq \lvert \mathcal{L} \rvert$$의 꼴이다.

</div>


## Projective space의 linear system

앞서 [§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12) 이후의 계산에 의해 $$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d))$$가 차수 $$d$$의 동차다항식들의 공간 $$\mathbb{K}[\x_0, \ldots, \x_n]_d$$와 동형임을 보았다. 이 공간의 각 원소들은 $$\mathbb{P}^n$$의 degree $$d$$ hypersurface를 정의하므로, 우리는 $$\mathcal{O}_{\mathbb{P}^n}(d)$$의 complete linear system

$$\lvert \mathcal{O}_{\mathbb{P}^n}(d)\rvert=\mathbb{P}(\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)))\cong \mathbb{P}(\mathbb{K}[\x_0,\ldots, \x_n]_d)\cong \mathbb{P}^{\binom{n+d}{d} - 1}$$

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

의 방정식이다. 이들은 $$U_2$$ 위에서는 위의 두 식으로부터 계산되는 $$(x,y)=(0,\pm\sqrt{5})$$에서 만나며, $$U_2$$ 바깥 --- 즉 $$U_2$$의 <em_ko>무한대 직선</em_ko>[^1] --- 에서는 두 점 $$[1:i:0]$$, $$[1: -i:0]$$에서 만난다. 위의 pencil $$Z(\lambda F_1+\mu F_2)$$는, 그럼 이들 교집합 $$C_1\cap C_2$$을 지나는 conic들의 모임이다. 

한편 일반적인 degree 2 homogeneous polynomial은

$$F(\x_0,\x_1,\x_2) = a_{00}\x_0^2 + a_{11}\x_1^2 + a_{22}\x_2^2 + a_{01}\x_0\x_1 + a_{02}\x_0\x_2 + a_{12}\x_1\x_2$$

의 꼴이며, 이것이 정확히 $$\Gamma(X, \mathcal{O}(2))$$가 $$6$$차원 공간인 이유이다. 한편, 위에서 계산한 네 점짜리 집합 $$C_1\cap C_2$$를 지나야 한다는 조건을 추가한다면, 이들 네 점이 각각 하나씩의 제약조건을 걸이 필요한 parameter를 하나씩 지워주므로 이를 나타내기 위한 parameter는 2개임을 안다. 더 구체적으로, 다음 네 개의 조건

$$0=F(0,\sqrt{5},1)=5a_{11}+a_{22}+\sqrt{5}a_{12}$$

$$0=F(0,-\sqrt{5},1)=5a_{11}+a_{22}-\sqrt{5}a_{12}$$

$$0=F(1,i,0)=a_{00}-a_{11}+ia_{01}$$

$$0=F(1,-i,0)=a_{00}-a_{11}-ia_{01}$$

이 $$a_{12}=0$$, $$a_{01}=0$$, $$5a_{11}=-a_{22}$$, $$a_{00}=a_{11}$$을 강제하므로 실질적인 변수는 $$a_{00}$$, $$a_{02}$$의 두 개이다. 즉, 이들 conic의 모임은 $$\Gamma(X,\mathcal{O}(2))$$의 2차원 부분공간 $$V$$를 이룰 것이며, 이를 projectivize한 것이 $$[\lambda:\mu]$$로 나타나는 $$\mathbb{P}^1$$이 된다. 

![pencil_of_circles](/assets/images/Math/Algebraic_Geometry/Linear_systems-1.png){:style="width:40em" class="invert" .align-center}

</div>

물론 [정의 2](#def2)는 $$X$$가 projective space이든 quasi-projective variety이든 임의의 variety에 동일하게 적용된다. 그러나 우리가 위의 [예시 3](#ex3)을 이렇게 공들여 계산한 이유는, 임의의 quasi-projective variety $$X\subseteq \mathbb{P}^n$$에 대해서도 $$D$$가 어떠한 $$\mathcal{O}_{\mathbb{P}^n}(d)$$에서 온다면 homogeneous polynomial의 언어를 그대로 사용할 수 있기 때문이다. 즉 이 경우 restriction map

$$\Gamma(\mathbb{P}^n, \mathcal{O}_{\mathbb{P}^n}(d)) \to \Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X)$$

은 homogeneous polynomial $$F \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$를 $$X$$ 위의 section으로 보내며, 그 kernel은 $$I(X)$$의 차수 $$d$$인 homogeneous part $$I(X)_d$$이다. 따라서

$$\Gamma(X, \mathcal{O}_{\mathbb{P}^n}(d)\vert_X) \cong \mathbb{K}[\x_0, \ldots, \x_n]_d / I(X)_d$$

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

위에서의 embedding $$\varphi_L$$은 실은 $$V$$의 basis의 선택에 의존하지만, $$\varphi_L$$이 갖는 여러 성질들은 그렇지 않다. 가령, 방금 전과 같이 basis들 모두가 vanish하는 $$X$$의 점들은 basis의 선택에 의존하지 않는다.

이를 엄밀하게 기술하기 위해, Weil divisor $$D = \sum n_i D_i$$의 *support*를 $$\operatorname{Supp}(D) = \bigcup_{n_i \neq 0} D_i$$로 정의한다. 즉, support는 divisor에서 계수가 $$0$$이 아닌 prime divisor들의 합집합이다. 이를 이용하면 다음이 잘 정의된다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Linear system $$L \subseteq \lvert \mathcal{L} \rvert$$의 *base locus* $$\operatorname{Bs}(L)$$는 $$L$$의 모든 원소가 공유하는 closed subset이다. 구체적으로, $$L = \mathbb{P}(V)$$에서 $$V \subseteq \Gamma(X, \mathcal{L})$$일 때,

$$\operatorname{Bs}(L) = \bigcap_{s \in V \setminus \{0\}} \operatorname{Supp}(\operatorname{div}(s))$$

여기서 $$\operatorname{div}(s)$$는 section $$s$$의 zero divisor이다. 

</div>

특히 $$\mathbb{P}^n$$의 hypersurface 계산에서는 $$V \subseteq \mathbb{K}[\x_0, \ldots, \x_n]_d$$에 대해 $$\operatorname{Bs}(L) = \bigcap_{[F] \in L} Z(F)$$와 동일하다. 그럼 우리가 하고 싶었던 정의는 다음의 정의이다. 

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$L$$이 *basepoint-free*라는 것은 $$\operatorname{Bs}(L) = \emptyset$$인 것이다. 즉, 임의의 점 $$p \in X$$에서 $$p$$를 지나지 않는 $$L$$의 원소가 항상 존재한다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> [예시 3](#ex3)에서 살펴본 $$\mathbb{P}^n$$의 두 예시를 살펴보자. 우선 처음의 complete linear system 

$$\lvert \mathcal{O}_{\mathbb{P}^2}(1)\rvert=\mathbb{P}(\mathbb{K}[\x_0,\x_1,\x_2]_1)$$

을 생각하자. 벡터공간 $$\mathbb{K}[\x_0,\x_1,\x_2]_1$$의 basis를 $$\x_0,\x_1,\x_2$$로 택하면, $$\x_0,\x_1,\x_2$$가 동시에 $$0$$이 되는 $$\mathbb{P}^2$$의 점은 없으므로 이는 basepoint-free이다. 이 basis의 선택이 정의하는 $$\varphi_L$$은 그냥 identity이다.

두 conic의 base locus의 경우, 위에서 살펴보았듯 base locus가 공집합이 아니다. 실제로, base locus는 [예시 3](#ex3)에서 이미 살펴본 $$C_1\cap C_2$$의 네 개의 교점이며, 기하적으로 pencil의 각 원소들은 정확히 $$C_1\cap C_2$$의 네 교점을 공유하므로 이것이 base locus의 정의와 맞아떨어지는 것을 안다.

</div>

위에서 살펴봤듯, basepoint-free linear system의 핵심 성질은 $$\varphi_L$$이 잘 정의된다는 것이다. 즉 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Quasiprojective variety $$X \subseteq \mathbb{P}^n$$ 위의 basepoint-free linear system $$L = \mathbb{P}(V)$$에서, $$V$$의 기저 $$F_0, \ldots, F_r \in \mathbb{K}[\x_0, \ldots, \x_n]_d$$가 다음 조건을 만족한다고 하자.

$$\bigcap_{i=0}^r Z(F_i) \cap X = \emptyset$$

그러면 $$V$$는 $$X$$에서 projective space로의 regular map

$$\varphi_L: X \to \mathbb{P}^r, \quad p \mapsto [F_0(p) : \cdots : F_r(p)]$$

을 정의한다. 여기서 $$F_i(p)$$는 $$F_i$$의 $$p$$에서의 값을 나타낸다.

</div>

위에서와 다른 예시를 하나만 더 살펴보자.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$\mathbb{P}^1$$에서 $$d \ge 1$$일 때, $$\lvert \mathcal{O}_{\mathbb{P}^1}(d) \rvert$$의 complete linear system이 정의하는 map은

$$\nu_d: \mathbb{P}^1 \to \mathbb{P}^d, \quad [s : t] \mapsto [s^d : s^{d-1}t : \cdots : t^d]$$

이다. 이는 [§사영다양체, ⁋예시 16](/ko/math/algebraic_geometry/projective_varieties#ex16)에서 살펴본 Veronese embedding을 complete linear system의 언어로 복원할 수 있다는 것을 보여준다. 

</div>

## Ample line bundle

비록 우리는 모든 variety가 quasi-projective임을 가정하고 있지만, 일반적으로 variety는 더 추상적으로 정의할 수 있다. 이러한 접근에는 장단점이 있는데, 좋은 점은 우리의 논의가 더 유연해진다는 것이고, 그로 인해 포기하게 되는 것은 variety를 embed하는 것이 더 이상 자명하지 않다는 것이다.

가령 우리의 언어에서 $$\mathbb{P}^1\times \mathbb{P}^1$$이 (quasi-projective) variety라고 하려면 반드시 이를 어떤 projective space로 넣어주어야 한다. ([§사영다양체, ⁋예시 16](/ko/math/algebraic_geometry/projective_varieties#ex16)) 대신, variety의 정의에서 ambient projective space의 존재를 가정하지 않는다면 이를 굳이 보이지 않아도 $$\mathbb{P}^1\times \mathbb{P}^1$$은 자동으로 variety이지만, 일반적인 variety가 projective space로 embed되는지는 불분명하다는 것이다. 

그러나 추상적인 variety에서도 line bundle과 linear system 등등을 모두 정의할 수 있다. 그럼 특히 [명제 7](#prop7)을 사용하면 projective space로의 적절한 함수를 정의할 수 있게 된다. 다음 정의의 중요성은 이러한 맥락에서 이해해야 한다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Line bundle $$\mathcal{L}$$ (또는 대응하는 linear system $$\lvert \mathcal{L} \rvert$$)이 *very ample*이라는 것은, complete linear system $$\lvert \mathcal{L} \rvert = \mathbb{P}(\Gamma(X, \mathcal{L}))$$이 정의하는 regular map $$\varphi_{\mathcal{L}}: X \to \mathbb{P}(\Gamma(X, \mathcal{L}))$$이 closed embedding인 것이다.

</div>

이것이 잘 정의되려면 $$\varphi_L$$이 basis의 선택에 의존하지 않아야 하며, 실제로 그러하다는 것을 쉽게 확인할 수 있다. 

Very ample의 정의에서 핵심은 사상이 단순한 morphism이 아니라 *closed* embedding이라는 점이다. 즉, 위에서 설명한 것과 같이 추상적인 variety의 세계에서도 이를 사용하여 projective variety를 정의하고, 심지어 very ample line bundle $$\mathcal{L}$$을 사용하면 $$X$$를 이 ambient projective space에서 명시적인 좌표로 표현할 수도 있게 된다. 

우리는 $$\mathcal{O}_{\mathbb{P}^n}(1)$$은 very ample이지만, $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 그렇지 않다는 것을 안다. [§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12)에서 살펴보았듯, 이는 $$\mathcal{O}_{\mathbb{P}^n}(-1)$$은 fiber가 base를 따라 이동할 때 꼬이는 방향이 section들이 zero section을 넘어가는 것을 허용하지 않아 global section이 존재하지 않기 때문이다. 반면 $$\mathcal{O}_{\mathbb{P}^n}(1)$$이 가지고 있는 꼬임은 이를 허용해주어 global section을 존재하게 해 준다. 

이 예시는 너무 간단한 예시이기는 하지만, 만일 $$\mathbb{P}^n$$보다 복잡한 어떤 공간이 있고, 이 공간의 복잡성이 특정한 line bundle의 꼬임만으로는 (올바른 방향임에도) 해소가 안 된다면, 우리는 이것이 해소될 때까지 더욱 더 꼬임을 추가해줄 수 있을 것이다. 이러한 상상으로부터 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> $$\mathcal{L}$$이 *ample*이라는 것은 어떤 $$m > 0$$에 대해 $$\mathcal{L}^{\otimes m}$$이 very ample인 것이다.

</div>

이 정의의 유용성을 보려면 ample이지만 very ample은 아닌 line bundle을 갖는 공간을 생각해야겠지만, 아직은 그러한 공간을 소개하기에는 다소 이르다. 하지만 머지 않아 그러한 공간을 다루게 되면 ampleness가 본격적으로 그 쓸모를 증명하게 된다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: $$\mathbb{P}^2$$의 <em-ko>무한대 직선</em-ko>과 그 기하적인 직관에 대해서는 [§사영다양체, ⁋예시 11](/ko/math/algebraic_geometry/projective_varieties#ex11)에서 이미 분석하였다. 