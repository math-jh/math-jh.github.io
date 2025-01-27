---

title: "아핀스킴"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/affine_schemes
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Affine_schemes.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2025-01-27
last_modified_at: 2025-01-27
weight: 2

---

## Locally ringed space로서의 $\Spec A$

이제 우리는 $\Spec A$ 위에 structure sheaf $\mathscr{O}\_{\Spec A}$를 정의하자. 위상공간 위에 정의된 sheaf의 예시 중 가장 기본적인 것은 위상공간 위에 정의된 연속함수들의 모임이며, 우리가 정의할 $\mathscr{O}\_{\Spec A}$ 또한 비슷하다. 

그러나 $\mathscr{O}\_{\Spec A}$가 $\Spec A$ 위에 정의된 연속함수들의 sheaf였다면 여기에 굳이 새로운 이름을 붙일 필요가 없을 것이다. 가장 간단한 예시로, 임의의 field $\mathbb{k}$의 유일한 prime ideal은 $(0)$이므로, 위상공간으로서 $\Spec \mathbb{k}$는 항상 singleton일 것이며 이 위에 위상구조를 주는 방법은 하나 뿐이다. 바꾸어 말하자면, isomorphic하지 않은 두 field의 스펙트럼을 서로 구별하고자 한다면 그 정보는 $\Spec \mathbb{k}$의 structure sheaf에 들어있어야 한다. 

기본적으로 위상공간 위에 정의된 sheaf에 대해서는 [\[위상수학\] §층](/ko/math/topology/sheaves)에서 이미 다루었지만, $\Spec A$에 정의할 structure sheaf를 서술하기에는 해당 글의 정의는 불충분하다. 

<div class="definition" markdown="1">

<ins id="def15">**정의 15**</ins> 위상공간 $X$와, 그 위에 정의된 $\cRing$-valued sheaf $\mathscr{O}\_X$의 pair $(X,\mathscr{O}\_X)$를 *ringed space<sub>환 달린 공간</sub>*라 부른다. 만일 $X$의 임의의 점 $x$에 대하여, $x$에서의 stalk $\mathscr{O}\_{X,x}$가 항상 local ring이라면 이 pair $(X, \mathscr{O}\_X)$를 *locally ringed space<sub>국소적 환 달린 공간</sub>*라 부른다. 

</div>

우리의 주장은 $\Spec A$에 적당한 structure sheaf $\mathscr{O}\_{\Spec A}$를 정의하여 $(\Spec A, \mathscr{O}\_{\Spec A})$를 locally ringed space로 만들 수 있고, 이 때 $\Spec$이 $\cRing$에서 locally ringed space들의 category로의 contravariant functor를 정의한다는 것이다. 이를 수학적으로 적기 위해서는 우선 locally ringed space들 사이의 morphism을 정의해야 한다. 

<div class="definition" markdown="1">

<ins id="def16">**정의 16**</ins> 두 ringed space $(X, \mathscr{O}\_X)$, $(Y, \mathscr{O}\_Y)$에 대하여, 이들 사이의 morphism은 연속함수 $f:X \rightarrow Y$와 $\Sh(Y,\cRing)$에서의 morphism $f^\sharp:\mathscr{O}\_Y \rightarrow f_\ast \mathscr{O}\_X$의 pair를 의미한다. 

두 locally ringed space $(X, \mathscr{O}\_X)$, $(Y, \mathscr{O}\_Y)$ 사이의 morphism은 ringed space로서의 morphism $(f,f^\sharp)$이, 추가적으로 각각의 $x\in X$에 대하여 local homomorphism $f_p^\sharp:\mathscr{O}\_{Y,f(x)} \rightarrow \mathscr{O}\_{X,x}$를 유도하는 것이다. 

</div>

이제 $\mathscr{O}\_{\Spec A}$를 정의해야 한다. 이는 

<div class="definition" markdown="1">

<ins id="def17">**정의 17**</ins> 고정된 원소 $f\in A$에 대하여, 

$$S=\{g\in A: D(f)\subseteq D(g)\}$$

으로 정의하자. 그럼 $S$는 $A$의 multiplicative subset이며, 이 때 $\mathscr{O}\_{\Spec A}(D(f))$를 $S^{-1}A$로 정의한다.

</div>