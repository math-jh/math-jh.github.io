---
title: "다양체에서 스킴으로"
description: "고전 대수다양체의 한계를 교차곱 multiplicity와 nilpotent 정보를 담지 못하는 점에서 짚어보고, 그로텐디크의 스킴 이론이 어떻게 이를 자연스럽게 확장하는지 직관적으로 설명한다."
excerpt: "From varieties to schemes"
categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/from_varieties_to_schemes
sidebar: 
    nav: "scheme_theory-ko"
date: 2026-05-07
weight: 1
---

## 대수다양체

[대수다양체](/ko/algebraic_varieties/) 카테고리의 글에서는 classical algebraic geometry의 기본적인 틀을 따라 왔다. 즉, algebraically closed field $\mathbb{K}$ 위에서 affine space $\mathbb{A}_\mathbb{K}^n$의 부분집합으로 정의되는 affine variety, 그리고 이들을 적절히 붙여 얻어지는 projective variety의 이론은 여러 방면에서 풍부한 결과를 낳았다. 특히 variety의 isomorphism과 coordinate ring의 isomorphism 사이의 대응 ([\[대수다양체\] §아핀다양체, ⁋명제 18](/ko/math/algebraic_varieties/affine_varieties#prop18)) 등은 기하와 대수의 깊은 연관성을 보여주는 대표적인 예이다.

Scheme은 이러한 variety들이 놓치는 것들을 극복하기 위해 체계화된 공간이다. 이번 글은 scheme theory를 전개하기 전에, 이것이 어떤 차원에서 variety를 확장하고, 어떠한 새로운 기하학적 직관을 제공하는지를 살펴보아 큰 흐름을 미리 잡아두는 것에 있다. 

이를 위해 간단히 algebraic variety에서의 세팅을 기억하자. 출발점이 되는 대상은 [\[대수다양체\] §아핀다양체, ⁋정의 2](/ko/math/algebraic_varieties/affine_varieties#def2)의 *affine variety*와 [\[대수다양체\] §사영다양체, ⁋정의 3](/ko/math/algebraic_varieties/projective_varieties#def3)의 *projective variety*로, 이들은 각각 algebraically closed field $\mathbb{K}$ 위의 affine space $\mathbb{A}_\mathbb{K}^n$과 projective space $\mathbb{P}_\mathbb{K}^n$의 irreducible algebraic subset으로 정의되었다. 더욱 중요한 것은 이들이 그 위에 정의된 regular function들의 sheaf $\mathcal{O}_V$를 갖는 locally ringed space $(V,\mathcal{O}_V)$로 이해될 수 있다는 것이었다. 

이 세계에서는 모든 점이 closed point였다. 즉, $\mathbb{A}_\mathbb{K}^2$ 위의 점은 단순히 좌표 $(a,b)\in \mathbb{K}^2$에 해당하는 maximal ideal $(\x-a, \y-b)\subseteq \mathbb{K}[\x,\y]$로 완전히 결정되었다. 이는 기하적 직관으로는 타당하다고도 할 수 있지만, 이론을 펼치기에는 썩 좋은 환경은 아닌데 예를 들어 $\mathbb{A}_\mathbb{K}^2$ 위에서 직선 $Z(\y)$와 포물선 $Z(\y-\x^2)$을 생각하면, 이들이 만나는 점이 $(0,0)$으로 주어진다는 것 자체는 classical algebraic variety에서 잘 보이는 것이지만, 이 만나는 degree가 $1$차가 아니라는 것이 전혀 보이지 않는다. 

::: 예시 1
Scheme에서 이러한 교차점의 degree를 어떻게 담아내는지를 살펴보자. 우선 교차점이 degree $1$인 경우로 $\mathbb{A}_\mathbb{K}^2$ 위에서 두 곡선 $Z(\y-\x)$와 $Z(\y)$의 교차를 생각할 수 있다. 그럼 이는 classical algebraic variety 관점에서는 위에서 살펴본 상황과 구별할 수 없다. 즉 이 두 직선은 한 점 $Z(\x,\y)=\{(0,0)\}$에서 만난다. 

이 두 직선의 교점이 위의 예시와 어떻게 다른지 살펴보기 위해서는 이들을 정의하는 ideal을 살펴보면 된다. 즉

$$(\y-\x)+(\y)=(\x,\y),\qquad (\y-\x^2)+(\y)=(\x^2,\y)$$

이므로, 첫 번째 경우와 달리 두 번째 경우에는 $\mathbb{K}[\x,\y]/(\x^2, \y)$에 남는 nilpotent element $\bar{\x}$가 존재한다. 사실

$$\frac{\mathbb{K}[\x,\y]}{(\x^2,\y)} \cong \frac{\mathbb{K}[\epsilon]}{(\epsilon^2)}$$

이 성립하며, 이 ring의 $\mathbb{K}$-벡터공간으로서의 차원은 $2$이다. 이 차원이 바로 교차 multiplicity를 계수로 반영하는 scheme-theoretic intersection의 핵심이다.
:::

이는 사실, [\[대수다양체\] §아핀다양체, ⁋정리 10](/ko/math/algebraic_varieties/affine_varieties#thm10)로부터 어느 정도 예견되었던 것인데, classical variety의 점들은 radical ideal에 의해서만 정의되므로, nilpotent element들을 모두 버리게 되고, 그 결과 infinitesimal한 정보를 모두 버려야 하기 때문이었다. Scheme의 핵심적인 아이디어는 이 버리던 정보들을 그대로 살려서 모두 담아두는 것이다. 

::: 예시 2
위에서 살펴본 ring $\mathbb{K}[\epsilon]/(\epsilon^2)$를 생각하자. 이 ring은 단 하나의 prime ideal $(\epsilon)$을 가지므로, classical algebraic geometry에서 이 공간은 점 하나로 이루어진 공간처럼 보이며, 이는 사실 scheme의 세상에서도 마찬가지이다. 

핵심적으로 다른 것은 scheme의 세상에서는 이 공간 위에 정의된 함수가 더 세밀하다는 것이다. 이 세밀함을 제대로 보려면, 이 공간을 단순한 점 하나가 아니라 <em-ko>tangent 방향 하나를 덧붙인 것</em-ko>으로 이해해야 한다. 즉 $\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$는 한 점에 $\epsilon$이라는 infinitesimal 방향을 붙인 *fat point*로, 보통의 점 $\Spec \mathbb{K}$가 점에서의 값만을 기억하는 데 비해 그 점에서의 tangent 방향의 정보까지 함께 갖는 공간이다.

이 관점에서 regular function, 즉 $\mathbb{K}[\epsilon]/(\epsilon^2)$의 원소 $a+b\epsilon$은 두 정보를 동시에 담는다. $a$는 그 점에서의 (보통 의미의) 함숫값이고, $b$는 바로 그 tangent 방향을 따라 함수가 어떻게 변하는지를 나타내는 좌표, 다시 말해 그 점에서의 일차 미분 정보이다. 그래서 두 함수가 그 점에서 같은 값 $a$를 갖더라도 $b$가 다르면 서로 다른 함수이다. 예컨대 $a+b\epsilon$과 $a+b'\epsilon$( $b\ne b'$ )은 같은 점에서 같은 값을 갖지만 tangent 방향으로의 변화가 다르므로 이 공간 위에서는 구별되는 regular function이다. 두 함수가 비로소 같아지는 것은 값 $a$뿐 아니라 tangent 좌표 $b$까지 일치할 때, 곧 점에서의 값과 일차 미분값을 둘 다 공유할 때뿐이다. 이렇게 점에 tangent 방향의 두께를 붙여 보는 것이 *fat point*의 본질이며, 이 두께가 남아 있다는 사실이 교차 multiplicity를 비롯한 infinitesimal 정보를 담아내는 열쇠가 된다.
:::

Classical variety의 또 다른 근본적 제약은 base change 혹은 fiber product가 자연스럽지 않다는 것이다. 이는 사소해 보이는 곳에서부터 이미 드러나는데, 가령 두 projective space의 곱 $\mathbb{P}^n\times \mathbb{P}^m$이 projective variety가 된다는 것조차 우리는 Segre embedding 등을 사용해서 손수 (더 큰) projective space 안에 넣어서 보여줬어야 했다. 이렇듯 가장 단순한 공간 두 개의 곱을 다루기 위해 추가적인 machinery가 필요하다는 점은 우리가 그 동안 그렇게 좋은 세상에서 작업을 하지 않았음을 보여주는 증거이다. 

## 스킴

Scheme theory는 이 모든 문제를 해결하기 위해 탄생했다. Scheme은 locally ringed space의 일종으로, 그 기하학적 대상이 단순히 점들의 집합이 아니라 점 위에 놓인 local ring의 구조까지 포함한다. 

구체적으로, 위에서 우리는 classical variety가 점을 maximal ideal로만 보고 radical ideal을 취해 nilpotent를 모두 버렸다는 한계를 살펴보고, 이들을 살려 fat point로 보면 손실되는 정보가 없어진다는 것을 보았다. Scheme은 이 수정을 전체에 걸쳐 체계화한 것으로, 여기에서 우리는 점을 maximal ideal이 아니라 <em-ko>모든 prime ideal</em-ko>로 삼고, 각 점 위에 local ring을 올려 함수를 그 section으로 정의한다. 

그 결과로 나타나는 것 중 가장 비직관적인 것 중 하나는 generic point의 존재이다. 예를 들어 $\Spec \mathbb{K}[\x,\y]$에서는 closed point $(\x-a,\y-b)$ 외에도 $(\x)$, $(\y)$, 그리고 $(0)$와 같은 non-closed point들이 존재한다. 이 가운데 어떤 점 $\mathfrak{p}\in\Spec A$의 closure $\overline{\{\mathfrak{p}\}}=Z(\mathfrak{p})$이 irreducible closed subset이 될 때, $\mathfrak{p}$를 그 irreducible closed subset의 *generic point*라 부르며, $A$가 integral domain이면 $(0)$이 $\Spec A$ 전체의 generic point가 된다. 

::: 예시 3
$\Spec \mathbb{Z}[\x]$를 생각하자. 이 scheme은 $\mathbb{Z}$ 위에서 정의되는 직선 $\mathbb{A}_{\mathbb{Z}}^1$에 해당한다. 이 예시에서 우리는 이 공간의 몇몇 점들을 살펴본다. 

먼저 $(0)$는 전체 공간의 generic point이다. $(\x)$는 $x$-축 위의 generic point로, 모든 fiber 위에서 $x=0$인 직선의 보편적인 성질을 담고 있다. $(p)$는 소수 $p$에 해당하는 vertical fiber의 generic point이며, $(p,\x)$는 그 fiber 위의 원점이라는 closed point이다. 이처럼 non-closed point들은 geometric object의 보편적이고 relative한 성질을 포착하는 데 필수적이다.
:::

즉, 직관적으로 generic point는 classical에서 prime ideal이 정의하던 irreducible subvariety를 **하나의 점으로 대표**시킨 것으로, 그 점의 닫힘이 바로 원래의 subvariety를 복원한다.

Scheme이 nilpotent를 허용한다는 점은 이미 [예시 2](#ex2)의 fat point에서 보았다. 일반적으로 scheme은 structure sheaf에 nilpotent를 그대로 둘 수 있어 *non-reduced* 구조를 기하학적으로 실현하며, 이 여유 덕분에 앞서 본 multiplicity와 infinitesimal deformation의 직관이 정당화된다.

## Relative geometry와 functor of points

지금까지 우리가 다룬 variety의 coordinate ring은 모두 $\mathbb{K}$-algebra였다. $\mathbb{K}$-algebra라는 것은 ring homomorphism $\mathbb{K}\rightarrow A$가 주어져 있다는 뜻이고, 이는 $\Spec$이 contravariant이므로 morphism $\Spec A\rightarrow\Spec\mathbb{K}$이 주어진 것과 같다. 즉 우리의 variety는 자연스럽게 $\Spec\mathbb{K}$ 위에 놓인 scheme이었던 셈이다. 

Scheme의 세계에서는 이 base $\Spec\mathbb{K}$를 임의의 scheme $S$로 바꾸어, structure morphism $X\rightarrow S$를 갖는 *$S$-scheme*을 자연스럽게 다룬다. 이 *relative viewpoint* 아래에서는 임의의 base 위에서 family를 논할 수 있으며, 위에서 만만치 않았던 곱조차 base 위에서의 fiber product $X\times_S Y$로 깔끔하게 정의되며, 위에서의 product는 $S=\Spec \mathbb{K}$인 경우에 불과하다. 

한편 이 관점은 [\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)와도 맞아떨어지는데, scheme $X$를 점들의 집합 대신, *functor of points* $h_X$로 보아, scheme을 다른 모든 scheme으로부터 morphism을 받는 functor

$$h_X:(\Sch_{/S})^{\op}\rightarrow\Set,\qquad h_X(T)=\Hom_S(T,X)$$

로 파악하면, 이 정리는 $h_X$가 scheme $X$를 손실 없이 완전히 결정한다는 것을 보여주며, 이러한 관점에서 scheme을 $S$-scheme들의 category $\Sch_{/S}$ 위에서 정의된 contravariant functor로 이해할 수도 있다. 

Classical variety $V$ 위의 $\mathbb{K}$-rational point는 단순히 $\mathbb{K}$-값을 갖는 좌표 $(a_1,\dotsc,a_n)$의 집합으로 이해되었다. 이는 scheme의 언어로는 morphism $\Spec \mathbb{K}\rightarrow V$에 해당한다. Functor of points는 이 관점을 확장하여, $V$의 $T$-valued point를 임의의 scheme $T$로부터의 morphism으로 정의한다.

::: 예시 4
Classical variety $V\subseteq\mathbb{A}_\mathbb{K}^n$의 $\mathbb{K}$-rational points의 집합은 $V(\mathbb{K})=\Hom_\mathbb{K}(\Spec \mathbb{K},V)$이다. 이는 functor of points $h_V$를 $T=\Spec \mathbb{K}$에 대하여 평가한 값 $h_V(\Spec \mathbb{K})$에 해당한다. 그러나 $T=\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$를 대입하면, $h_V(T)$는 $V$의 $\mathbb{K}$-point에서의 tangent vector들을 parameterize하게 된다.
:::

특히 projective line $\mathbb{P}_\mathbb{K}^1$의 경우, functor of points를 통해 infinitesimal structure가 어떻게 드러나는지 명확히 볼 수 있다. $\mathbb{P}_\mathbb{K}^1$은 그 자체로 homogeneous coordinate를 갖는 scheme이므로, 임의의 local $\mathbb{K}$-algebra $R$에 대하여 $\mathbb{P}_\mathbb{K}^1(R)$는 $R$ 위의 projective line 위의 점들로 정의된다.

::: 예시 5
$T=\Spec \mathbb{K}[\epsilon]/(\epsilon^2)$라 하자. $\mathbb{P}_\mathbb{K}^1$의 $T$-valued points, 즉 morphism $T\rightarrow\mathbb{P}_\mathbb{K}^1$를 생각하면, 이들은 $\mathbb{P}_\mathbb{K}^1$ 위의 한 점 $P$와 그 점에서의 tangent vector를 동시에 결정한다. 구체적으로, 점 $P$는 closed embedding $\Spec \mathbb{K}\hookrightarrow T$를 $T\rightarrow\mathbb{P}_\mathbb{K}^1$와 합성함으로써 얻어지고, 나머지 정보는 $P$에서의 Zariski tangent space의 원소가 된다. 따라서 $\mathbb{P}_\mathbb{K}^1$의 $\mathbb{K}[\epsilon]/(\epsilon^2)$-points는 $\mathbb{P}_\mathbb{K}^1$의 tangent bundle을 구성하는 점들에 일대일 대응한다.
:::

Functor of points는 이렇게 scheme을 representable functor로 이해하게 함으로써, geometric intuition과 범주론적 formalism 사이의 가교 역할을 한다.

이 글은 엄밀한 정의나 중요 정리를 세운 글은 아니지만, 이 카테고리에서 앞으로 다룰 scheme theory의 몇 가지 큰 주제를 미리 보는 내용으로, 이어질 글들에서 필요한 엄밀한 도구들이 놓칠 수 있는 직관을 보충하기 위해 앞으로의 길을 미리 써둔 것이다. 다음 글부터는 다시 엄밀한 수학적 내용을 바탕으로 scheme theory를 전개한다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.
