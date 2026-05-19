---
title: "다양체에서 스킴으로"
excerpt: "From varieties to schemes"
categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/from_varieties_to_schemes
sidebar: 
    nav: "scheme_theory-ko"
header:
    overlay_image: /assets/images/Math/Algebraic_Varieties/From_Varieties_to_Schemes.png
    overlay_filter: 0.5
date: 2026-05-07
last_modified_at: 2026-05-07
weight: 1
published: false
---

우리는 지금까지 classical algebraic geometry의 기본적인 틀을 따라 왔다. Algebraically closed field $k$ 위에서 affine space $\mathbb{A}_k^n$의 부분집합으로 정의되는 affine variety, 그리고 이들을 적절히 paste하여 얻어지는 projective variety의 이론은 여러 방면에서 풍부한 결과를 낳았다. 특히 variety의 좌표환(coordinate ring)과 정의ideal 사이의 대응, Zariski topology 위에서의 regular function과 rational map 등은 기하와 대수의 깊은 연관성을 보여주는 대표적인 예이다.

그러나 20세기 중반 이후 Grothendieck에 의해 체계화된 scheme theory는 이러한 classical framework를 크게 확장하였다. 본 글에서는 classical variety의 관점이 갖는 본질적인 한계를 구체적인 예와 함께 살펴 보고, 이를 scheme theory가 어떻게 극복하는지 직관적으로 설명한다. 우리의 목표는 scheme의 엄밀한 정의를 제시하는 것이 아니라, 다양체에서 스킴으로의 전환이 왜 자연스러운지, 그리고 어떤 새로운 기하학적 직관을 제공하는지를 밝히는 데 있다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Algebraically closed field $k$ 위의 <em-ko>affine variety</em-ko>는 $\mathbb{A}_k^n$의 어떤 algebraic subset $V$를, <em-ko>projective variety</em-ko>는 $\mathbb{P}_k^n$의 어떤 algebraic subset $V$를 의미한다. 이 때 $V$는 Zariski topology 위에서 irreducible인 closed subset으로, regular functions들의 sheaf $\mathcal{O}_V$를 갖는 locally ringed space $(V,\mathcal{O}_V)$로도 <em-ko>이해</em-ko>한다.

</div>

Classical variety의 세계에서는 모든 점이 closed point였다. 즉, $\mathbb{A}_k^2$ 위의 점은 단순히 좌표 $(a,b)\in k^2$에 해당하는 maximal ideal $(\x-a, \y-b)\subseteq k[\x,\y]$로 완전히 결정되었다. 이 관점에서는 두 곡선의 교차가 단순히 집합론적인 교집합으로 환원되며, 교차하는 점의 개수만을 셀 수 있을 뿐 그것이 얼마나 깊이 교차하는지를 내포하는 구조를 담기 어려웠다.

예를 들어 $\mathbb{A}_k^2$ 위에서 직선 $V(\y)$와 포물선 $V(\y-\x^2)$를 생각해 보자. 이들은 원점에서 접한다. Classical variety의 언어로는 이들의 교차는 원점이라는 한 점에 불과하다. 그러나 해석학적 직관에 따류면, 이 교차는 원점을 단순히 지나는 것이 아니라 <em-ko>intersection multiplicity</em-ko> $2$로 교차한다. 이러한 multiplicity 정보는 classical framework에서는 사라진다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> $\mathbb{A}_k^2$ 위에서 두 곡선 $V(\y-\x)$와 $V(\y)$의 교차를 생각하자. 이들은 원점에서 서로 다른 방향으로 만나므로 transversal intersection을 이룬다. 한편 $V(\y-\x^2)$와 $V(\y)$의 교차는 원점에서 접하므로 tangential intersection이다. Classical variety의 범주에서는 두 경우 모두 원점이라는 동일한 집합 $V(\x,\y)=\{(0,0)\}$를 교차로 얻는다. 그러나 ideal의 관점에서는

$$$(\y-\x)+(\y)=(\x,\y),\qquad (\y-\x^2)+(\y)=(\x^2,\y)$$$

이므로, 첫 번째 경우와 달리 두 번째 경우에는 $\mathbb{A}_k^2$의 좌표환 $k[\x,\y]$에 남는 nilpotent element $\bar{\x}$가 존재한다. 사실

$$$\frac{k[\x,\y]}{(\x^2,\y)} \cong \frac{k[\epsilon]}{(\epsilon^2)}$$$

이 성립하며, 이 환의 $k$-벡터공간으로서의 차원은 $2$이다. 이 차원이 바로 교차 multiplicity를 계수로 반영하는 scheme-theoretic intersection의 핵심이다.

</div>

이처럼 classical variety는 radical ideal에 의해서만 정의되므로, nilpotent element를 모두 버리게 된다. 그 결과 infinitesimal한 정보, 즉 점의 근방에서 함수가 어떻게 변하는지에 대한 1차 혹은 그 이상의 미분 정보를 기하학적 대상 자체에 담을 수 없었다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 환 $k[\epsilon]/(\epsilon^2)$를 생각하자. 이 환은 단 하나의 prime ideal $(\epsilon)$을 가지므로, 이에 대응하는 geometric object는 점 하나로 이루어진 공간처럼 보인다. 그러나 이 공간 위의 regular function은 $a+b\epsilon$ 꼴이며, 두 함수가 동일한 값을 갖는다고 해서 같은 함수가 되는 것은 아니다. 오히려 두 함수가 같은 값과 같은 1차 미분값을 갖을 때에만 이 공간 위에서 동일해진다. 따라서 $\operatorname{Spec} k[\epsilon]/(\epsilon^2)$는 원점에 붙은 infinitesimal 방향, 다시 말해 tangent direction을 기억하는 <em-ko>fat point</em-ko>로 <em-ko>이해</em-ko>한다.

</div>

또 다른 중요한 한계는 base change의 어려움이다. Classical variety는 항상 algebraically closed field 위에 정의되며, 따라서 reduction modulo $p$나 임의의 field extension을 자연스럽게 다루기 힘들다. 예를 들어 $\mathbb{Z}$ 위에서 정의되는 다항식 방정식의 해를 살펴 보고, 이를 여러 소수 $p$에 대해 modulo $p$로 줄여보고 싶다면, classical framework에서는 각각의 algebraically closed field $\bar{\mathbb{F}}_p$ 위에서 별개의 variety를 만들어야 한다. 이들 사이의 체계적인 연결고리를 제공하지 못하는 것이다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Classical variety의 범주는 algebraically closed field $k$ 위에서만 닫혀 있으며, 임의의 commutative ring 위에서 정의되는 geometric object를 포함하지 않는다. 특히 arithmetic information을 담는 $\operatorname{Spec} \mathbb{Z}$와 같은 대상은 classical algebraic geometry의 범주 밖에 놓인다.

</div>

Scheme theory는 이 모든 문제를 해결하기 위해 탄생했다. Scheme은 locally ringed space의 일종으로, 그 기하학적 대상이 단순히 점들의 집합이 아니라 점 위에 놓인 local ring의 구조까지 포함한다. 이로써 nilpotent element가 자연스럽게 등장하고, non-closed point를 통해 generic point를 포착하며, 임의의 base 위에서 정의되는 relative geometry가 가능해진다.

가장 먼저, classical affine variety가 scheme의 언어로 어떻게 해석되는지 살펴보자. $\mathbb{A}_k^n$ 속의 irreducible algebraic subset $V$가 radical ideal $I(V)$에 의해 정의된다고 하자. 이 때 $V$의 coordinate ring은 $A=k[\x_1,\dotsc,\x_n]/I(V)$이며, 이는 reduced finitely generated $k$-algebra이다. Classical variety $V$는 $A$의 maximal ideal들의 집합 $\operatorname{MaxSpec} A$와 대응하였다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Affine variety $V\subseteq\mathbb{A}_k^n$에 대하여, 그 **coordinate ring**을 $A=\Gamma(V,\mathcal{O}_V)$라 하자. 이 때 $V$에 대응하는 **affine scheme**은 locally ringed space $\operatorname{Spec} A$이다. 여기서 $\operatorname{Spec} A$의 underlying topological space는 $A$의 모든 prime ideal들의 집합이며, structure sheaf는 Zariski topology 위에서 standard way로 정의된다.

</div>

이 대응은 classical variety를 scheme의 세계로 자연스럽게 끌어들인다. 특히 $\operatorname{MaxSpec} A$는 $\operatorname{Spec} A$의 closed point들에 해당하며, $V$ 위의 Zariski topology는 $\operatorname{Spec} A$의 induced topology로 회복된다. Regular function은 <em-ko>structure sheaf</em-ko> $\mathcal{O}_{\operatorname{Spec} A}$의 section으로, rational map는 scheme 사이의 dominant rational morphism으로 <em-ko>이해</em-ko>한다.

Projective variety에 대해서도 유사한 해석이 가능하다. Projective variety $V\subseteq\mathbb{P}_k^n$는 homogeneous coordinate ring $S=k[\x_0,\dotsc,\x_n]/I(V)$를 갖는다. 이 때 $S$는 graded ring이며, 이로부터 scheme $\operatorname{Proj} S$를 구성할 수 있다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Homogeneous coordinate ring $S$가 주어진 projective variety $V\subseteq\mathbb{P}_k^n$에 대하여, 그에 대응하는 **projective scheme**은 $\operatorname{Proj} S$로 정의된다. $\operatorname{Proj} S$의 underlying topological space는 $S$의 homogeneous prime ideal 중 irrelevant ideal $S_+=\bigoplus_{d>0} S_d$를 포함하지 않는 것들의 집합이며, structure sheaf는 homogeneous localization을 통해 정의된다.

</div>

이러한 대응은 classical variety와 scheme 사이의 관계를 다음과 같이 요약할 수 있게 한다. Classical variety는 단순히 특별한 종류의 scheme으로 볼 수 있으며, 이는 scheme theory가 classical theory를 확장하는 것이지 폐기하는 것이 아님을 보여준다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> Algebraically closed field $k$ 위에서, classical variety는 다음 조건을 만족하는 scheme $X$와 일치한다: $X$는 $k$ 위에서 finite type인 separated scheme이며, reduced이고 irreducible이다. 다시 말해 classical affine variety는 $\operatorname{Spec} A$꼴의 reduced irreducible scheme이고, classical projective variety는 $\operatorname{Proj} S$꼴의 reduced irreducible scheme이다.

</div>

Scheme theory의 본질적 확장은 classical variety가 가진 제약들을 하나씩 푸는 데서 나타난다. 먼저, scheme은 모든 prime ideal을 점으로 포함하므로, classical variety에서는 보이지 않던 <em-ko>generic point</em-ko>가 자연스럽게 등장한다. 예를 들어 $\operatorname{Spec} k[\x,\y]$에서는 closed point $(\x-a,\y-b)$ 외에도 $(\x)$, $(\y)$, 그리고 $(0)$와 같은 non-closed point들이 존재한다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme $X=\operatorname{Spec} A$ 위에서, prime ideal $\mathfrak{p}\in\operatorname{Spec} A$가 **generic point**라 함은 $\overline{\{\mathfrak{p}\}}=V(\mathfrak{p})$가 $X$의 irreducible component가 되는 경우를 말한다. 특히 $(0)\in\operatorname{Spec} A$는 integral domain인 경우 $X$ 전체의 generic point가 된다.

</div>

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $\operatorname{Spec} \mathbb{Z}[\x]$를 생각하자. 이 scheme은 $\mathbb{Z}$ 위에서 정의되는 직선 $\mathbb{A}_{\mathbb{Z}}^1$에 해당한다. 이 공간의 점들은 다음과 같이 분류된다. 먼저 $(0)$는 전체 공간의 generic point이다. $(\x)$는 $x$-축 위의 generic point로, 모든 fiber 위에서 $x=0$인 직선의 보편적인 성질을 담고 있다. $(p)$는 소수 $p$에 해당하는 vertical fiber의 generic point이며, $(p,\x)$는 그 fiber 위의 원점이라는 closed point이다. 이처럼 non-closed point들은 geometric object의 보편적이고 relative한 성질을 포착하는 데 필수적이다.

</div>

다음으로, scheme은 structure sheaf에 nilpotent element를 허용함으로써 non-reduced 구조를 기하학적으로 실현한다. 이는 앞서 살펴 본 교차 multiplicity와 infinitesimal deformation의 개념을 정당화한다.

<div class="definition" markdown="1">

<ins id="def10">**정의 10**</ins> Scheme $X$가 **non-reduced**라 함은 structure sheaf $\mathcal{O}_X$의 어떤 stalk $\mathcal{O}_{X,x}$에 nilpotent element가 존재하는 경우를 말한다. Equivalently, $X=\operatorname{Spec} A$인 경우 $A$에 nilpotent element가 존재한다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> $\operatorname{Spec} k[\x,\y]/(\y^2)$를 생각하자. 이 scheme의 underlying topological space는 $\mathbb{A}_k^2$ 위의 $x$-축 $V(\y)$와 동일하지만, structure sheaf는 $y$-방향으로의 1차 미분 정보를 추가로 담고 있다. 이 scheme 위의 두 regular function이 동일한 값을 갖는다고 해서 같은 함수가 되는 것은 아니며, $y=0$에서의 1차 편미분값까지 일치해야 비로소 같아진다. 이는 $x$-축에 수직인 방향으로의 infinitesimal thickening을 나타낸다.

</div>

또한 scheme theory는 모든 대상을 어떤 base scheme $S$ 위로부터의 family로 이해하는 <em-ko>relative viewpoint</em-ko>를 제공한다. 즉, scheme $X$에 대하여 단순히 $X$ 자체를 보는 대신 구조사상 $X\rightarrow S$를 고려함으로써, $S$의 각 점 위에서의 fiber를 살펴볼 수 있다. 이는 reduction modulo $p$나 field extension을 단순히 base change $X\times_S S'\rightarrow S'$로 통일되게 이해하게 한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Base scheme $S=\operatorname{Spec} \mathbb{Z}$ 위에서 scheme $X\rightarrow\operatorname{Spec}\mathbb{Z}$를 생각하면, 각 소수 $p$에 대하여 fiber $X_p=X\times_{\operatorname{Spec}\mathbb{Z}}\operatorname{Spec}\mathbb{F}_p$는 $p$에서의 reduction modulo $p$를 의미한다. 이처럼 arithmetic geometry에서는 하나의 scheme이 여러 소수들 위에서의 geometric family를 동시에 encode한다.

</div>

Scheme을 단순히 locally ringed space로만 이해하는 것은 그 본질을 충분히 포착하지 못할 수 있다. Grothendieck은 scheme $X$를 그 <em-ko>functor of points</em-ko> $h_X$를 통해 <em-ko>이해</em-ko>할 것을 제안하였다. 이는 scheme을 단순히 점들의 집합이 아니라, 다른 모든 scheme으로부터의 관점에서 바라보는 방식이다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> Scheme $X$에 대하여, 그 **functor of points** $h_X$는 범주 $(\operatorname{Sch}/S)^{\mathrm{op}}$에서 $\mathbf{Sets}$로의 functor로, 임의의 $S$-scheme $T$에 대하여

$$$h_X(T)=\operatorname{Hom}_S(T,X)$$$

를 정의하고, morphism $f:T'\rightarrow T$에 대하여 $h_X(f):h_X(T)\rightarrow h_X(T')$를 precomposition by $f$로 준다.

</div>

Classical variety $V$ 위의 $k$-rational point는 단순히 $k$-값을 갖는 좌표 $(a_1,\dotsc,a_n)$의 집합으로 <em-ko>이해</em-ko>되었다. 이는 scheme의 언어로는 morphism $\operatorname{Spec} k\rightarrow V$에 해당한다. Functor of points는 이 관점을 확장하여, $V$의 $T$-valued point를 임의의 scheme $T$로부터의 morphism으로 정의한다.

<div class="example" markdown="1">

<ins id="ex14">**예시 14**</ins> Classical variety $V\subseteq\mathbb{A}_k^n$의 $k$-rational points의 집합은 $V(k)=\operatorname{Hom}_k(\operatorname{Spec} k,V)$이다. 이는 functor of points $h_V$를 base scheme $T=\operatorname{Spec} k$에 대하여 평가한 값 $h_V(\operatorname{Spec} k)$에 해당한다. 그러나 $T=\operatorname{Spec} k[\epsilon]/(\epsilon^2)$를 대입하면, $h_V(T)$는 $V$의 tangent bundle 위의 점들을 parameterize하며, 이는 classical $k$-rational points만으로는 볼 수 없는 풍부한 geometric information을 제공한다.

</div>

특히 projective line $\mathbb{P}_k^1$의 경우, functor of points를 통해 infinitesimal structure가 어떻게 드러나는지 명확히 볼 수 있다. $\mathbb{P}_k^1$은 그 자체로 homogeneous coordinate를 갖는 scheme이므로, 임의의 $k$-algebra $R$에 대하여 $\mathbb{P}_k^1(R)$는 $R$ 위의 projective line 위의 점들로 정의된다.

<div class="example" markdown="1">

<ins id="ex15">**예시 15**</ins> $T=\operatorname{Spec} k[\epsilon]/(\epsilon^2)$라 하자. $\mathbb{P}_k^1$의 $T$-valued points, 즉 morphism $T\rightarrow\mathbb{P}_k^1$를 생각하면, 이들은 $\mathbb{P}_k^1$ 위의 한 점 $P$와 그 점에서의 tangent vector를 동시에 결정한다. 구체적으로, 점 $P$는 closed immersion $\operatorname{Spec} k\hookrightarrow T$를 $T\rightarrow\mathbb{P}_k^1$와 합성함으로써 얻어지고, 나머지 정보는 $P$에서의 Zariski tangent space의 원소가 된다. 따라서 $\mathbb{P}_k^1$의 $k[\epsilon]/(\epsilon^2)$-points는 $\mathbb{P}_k^1$의 tangent bundle을 구성하는 점들에 일대일 대응한다.

</div>

Functor of points는 scheme을 representable functor로 이해하게 함으로써, geometric intuition과 범주론적 formalism 사이의 가교 역할을 한다. 특히 moduli problem을 다룰 때, 우리가 원하는 geometric object를 classify하는 functor를 먼저 정의하고, 이를 represent하는 scheme 혹은 더 일반적으로 algebraic space나 stack이 존재하는지를 묻는 방식이 표준적인 접근이 되었다.

우리는 이번 글에서 classical algebraic geometry의 framework가 갖는 세 가지 핵심적 한계, 즉 generic point의 부재, nilpotent element의 부재, 그리고 relative viewpoint의 부재를 살펴 보았다. Scheme theory는 locally ringed space의 개념을 통해 이 모든 어려움을 극복하며, classical variety를 reduced irreducible scheme의 특수한 경우로 자연스럽게 포함시킨다. 특히 functor of points를 통해 scheme은 단순한 점의 집합을 넘어, infinitesimal deformation과 base change를 아우르는 유연한 기하학적 객체로 거듭난다. 다음 글에서는 scheme의 정의를 보다 엄밀하게 전개하고, $\operatorname{Spec} A$의 Zariski topology와 structure sheaf의 구체적인 구성을 다루어 이 직관들을 엄밀한 framework 위에 올리고자 한다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.
