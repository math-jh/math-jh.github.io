---
title: "경계가 있는 다양체"
description: "반공간을 모델로 하는 경계가 있는 다양체를 정의하고, 경계의 좌표불변성과 경계가 물려받는 다양체 구조, 그리고 유도된 향을 다룬다."
excerpt: "Manifold with boundary와 induced orientation"

categories: [Math / Manifolds]
permalink: /ko/math/manifolds/manifolds_with_boundary
sidebar: 
    nav: "manifolds-ko"

date: 2026-06-11
last_modified_at: 2026-06-11
weight: 21
published: false

---

[§적분](/ko/math/manifolds/integration)에서 우리는 oriented manifold 위에서 미분형식을 적분하는 방법을 살펴보았다. 미적분학의 기본정리를 이 언어로 일반화하기 위해서는 "영역과 그 경계"를 다룰 수 있어야 하는데, 지금까지의 manifold는 모든 점이 유클리드 공간의 열린집합과 닮아 있어 경계라 부를 만한 점이 없다. 이번 글에서는 모델 공간을 유클리드 공간에서 반공간으로 바꾸어 이 문제를 해결한다.

## 반공간과 매끄러운 함수

다음의 집합

$$\mathbb{H}^m=\left\{x\in\mathbb{R}^m\mid x^m\geq 0\right\}$$

에 $$\mathbb{R}^m$$의 subspace topology를 준 것을 *반공간<sub>half-space</sub>*이라 부른다. 또, 다음의 두 집합

$$\partial\mathbb{H}^m=\left\{x\in \mathbb{H}^m\mid x^m=0\right\},\qquad \operatorname{int}\mathbb{H}^m=\left\{x\in\mathbb{H}^m\mid x^m>0\right\}$$

을 각각 $$\mathbb{H}^m$$의 경계와 내부라 부른다. $$\operatorname{int}\mathbb{H}^m$$은 $$\mathbb{R}^m$$의 열린집합이지만, $$\mathbb{H}^m$$의 열린집합들 가운데에는 $$\partial\mathbb{H}^m$$과 만나는 것들도 있다는 것에 주의해야 한다.

반공간의 부분집합은 $$\mathbb{R}^m$$의 열린집합이 아닐 수 있으므로, 그 위에서의 미분가능성을 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 부분집합 $$A\subseteq\mathbb{R}^m$$ 위에서 정의된 함수 $$f:A \rightarrow \mathbb{R}^n$$이 *$$C^\infty$$*라는 것은, 각각의 $$p\in A$$마다 $$p$$의 ($$\mathbb{R}^m$$에서의) 열린근방 $$W$$와 $$C^\infty$$ 함수 $$\tilde{f}:W \rightarrow \mathbb{R}^n$$이 존재하여 $$\tilde{f}\vert_{W\cap A}=f\vert_{W\cap A}$$이 성립하는 것이다.

</div>

즉 국소적으로 열린집합 위의 $$C^\infty$$ 함수로 확장되는 함수를 $$C^\infty$$라 부르는 것이다. $$A$$가 열린집합이라면 이는 기존의 정의와 일치한다. 한편 $$A=\mathbb{H}^m$$의 열린집합이고 $$p\in\partial\mathbb{H}^m$$인 경우, $$f$$의 편미분 $$\partial f/\partial x^i(p)$$들은 확장 $$\tilde{f}$$의 선택과 무관하게 잘 정의되는데, 이는 $$p$$ 근방에서 $$W\cap A$$가 $$p$$로 수렴하는 점렬들을 모든 방향에 대해 충분히 담고 있어 $$\tilde f$$의 일계도함수들이 $$W\cap A$$ 위의 값들로 결정되기 때문이다. 실제로 $$i<m$$ 방향의 편미분은 $$\partial\mathbb{H}^m$$ 방향의 차분몫의 극한으로, $$i=m$$ 방향의 편미분은 한쪽 극한

$$\frac{\partial f}{\partial x^m}(p)=\lim_{t\to0^+}\frac{f(p+te_m)-f(p)}{t}$$

으로 계산된다. 고계도함수들도 마찬가지이다.

## 경계가 있는 다양체

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Second countable Hausdorff space $$M$$이 *$$m$$차원의 경계가 있는 다양체<sub>manifold with boundary</sub>*라는 것은 다음의 조건을 만족하는 chart들의 모임 $$(U_\alpha,\varphi_\alpha)$$이 존재하는 것이다.

1. $$U_\alpha$$들은 $$M$$의 open covering이고, 각각의 $$\varphi_\alpha$$는 $$U_\alpha$$에서 $$\mathbb{H}^m$$의 열린집합으로의 homeomorphism이다.
2. 임의의 $$\alpha,\beta$$에 대하여, transition $$\varphi_\beta\circ\varphi_\alpha^{-1}:\varphi_\alpha(U_\alpha\cap U_\beta) \rightarrow \varphi_\beta(U_\alpha\cap U_\beta)$$는 [정의 1](#def1)의 의미에서 $$C^\infty$$이다.

이 때 점 $$p\in M$$이 *경계점<sub>boundary point</sub>*이라는 것은 어떤 chart $$\varphi_\alpha$$에 대하여 $$\varphi_\alpha(p)\in\partial\mathbb{H}^m$$인 것이고, 그렇지 않은 점들을 *내부점<sub>interior point</sub>*이라 부른다. 경계점들의 모임을 $$\partial M$$, 내부점들의 모임을 $$\operatorname{int}M$$이라 적는다.

</div>

[§미분다양체](/ko/math/manifolds/smooth_manifolds)에서와 마찬가지로 atlas를 maximal한 것으로 키워 미분구조를 생각한다. $$\operatorname{int}\mathbb{H}^m$$이 $$\mathbb{R}^m$$의 열린집합이므로, $$\partial M=\emptyset$$인 경우 위의 정의는 기존의 manifold의 정의와 일치한다.

위의 정의가 말이 되려면 경계점이라는 개념이 chart의 선택에 의존하지 않아야 한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> 점 $$p\in M$$와 두 chart $$(U,\varphi)$$, $$(V,\psi)$$에 대하여, $$\varphi(p)\in\partial\mathbb{H}^m$$인 것과 $$\psi(p)\in\partial\mathbb{H}^m$$인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

대우를 보이자. 즉 $$\varphi(p)\in\operatorname{int}\mathbb{H}^m$$이라 가정하고 $$\psi(p)\in\operatorname{int}\mathbb{H}^m$$임을 보인다. Transition $$\tau=\psi\circ\varphi^{-1}$$와 그 역함수 $$\sigma=\varphi\circ\psi^{-1}$$를 생각하자. [정의 1](#def1)에 의하여 $$\varphi(p)$$와 $$\psi(p)$$의 적당한 열린근방 $$W,W'\subseteq\mathbb{R}^m$$과 $$C^\infty$$ 확장 $$\tilde{\tau}:W \rightarrow \mathbb{R}^m$$, $$\tilde{\sigma}:W' \rightarrow \mathbb{R}^m$$이 존재한다.

$$\varphi(p)\in\operatorname{int}\mathbb{H}^m$$이므로, $$W$$를 줄여 $$W$$가 $$\varphi(U\cap V)\cap\operatorname{int}\mathbb{H}^m$$에 포함되는 $$\mathbb{R}^m$$의 열린집합이라 가정할 수 있고, 그럼 $$\tilde\tau=\tau\vert_W$$이다. 또, 연속성에 의해 $$W$$를 한 번 더 줄여 $$\tau(W)\subseteq W'$$이라 가정하자. 그럼 $$W$$ 위에서

$$\tilde{\sigma}\circ\tilde{\tau}=\sigma\circ\tau=\id_W$$

가 성립하고, $$W$$는 $$\mathbb{R}^m$$의 열린집합이므로 chain rule에 의하여 $$D\tilde\sigma(\tau(\varphi(p)))\circ D\tilde\tau(\varphi(p))=\id$$이다. 특히 $$D\tilde\tau(\varphi(p))$$는 invertible이고, 역함수 정리 ([§부분다양체와 역함수 정리, ⁋정리 4](/ko/math/manifolds/submanifolds#thm4))에 의하여 $$\tilde\tau$$는 $$\varphi(p)$$의 적당한 열린근방을 $$\psi(p)=\tau(\varphi(p))$$를 포함하는 $$\mathbb{R}^m$$의 *열린집합*으로 보낸다. 이 열린집합은 $$\tau$$의 image, 즉 $$\mathbb{H}^m$$의 부분집합에 포함되므로, $$\psi(p)$$는 $$\mathbb{H}^m$$ 안에서 $$\mathbb{R}^m$$-열린근방을 갖는다. 그런데 $$\partial\mathbb{H}^m$$의 점의 임의의 $$\mathbb{R}^m$$-열린근방은 $$x^m<0$$인 점을 포함하므로, $$\psi(p)\not\in\partial\mathbb{H}^m$$이다.

</details>

따라서 $$M$$은 서로소인 두 집합 $$\operatorname{int}M$$과 $$\partial M$$으로 나뉜다. 이들 각각은 다시 다양체가 된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$m$$차원의 경계가 있는 다양체 $$M$$에 대하여 다음이 성립한다.

1. $$\operatorname{int}M$$은 $$M$$의 열린집합이고, ($$\partial$$ 없는) $$m$$차원 manifold이다.
2. $$\partial M$$은 $$M$$의 닫힌집합이고, chart들 $$(U_\alpha\cap\partial M, (\varphi_\alpha^1,\ldots,\varphi_\alpha^{m-1})\vert_{\partial M})$$에 대하여 ($$\partial$$ 없는) $$(m-1)$$차원 manifold이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫째 주장을 보이자. $$p\in\operatorname{int}M$$이라 하면 chart $$(U,\varphi)$$에 대해 $$\varphi(p)\in\operatorname{int}\mathbb{H}^m$$이고, $$\operatorname{int}\mathbb{H}^m$$이 $$\mathbb{H}^m$$에서 열린집합이므로 $$U'=\varphi^{-1}(\operatorname{int}\mathbb{H}^m\cap\varphi(U))$$는 $$p$$의 열린근방이다. [명제 3](#prop3)에 의해 $$U'$$의 모든 점이 내부점이므로 $$\operatorname{int}M$$은 열린집합이고, 이러한 $$(U',\varphi\vert_{U'})$$들은 $$\mathbb{R}^m$$의 열린집합으로 가는 chart들이므로 $$\operatorname{int}M$$은 $$m$$차원 manifold이다.

이제 둘째 주장을 보이자. $$\partial M$$은 열린집합 $$\operatorname{int}M$$의 여집합이므로 닫힌집합이다. Chart $$(U,\varphi)$$에 대하여 [명제 3](#prop3)에 의해 $$\varphi(U\cap\partial M)=\varphi(U)\cap\partial\mathbb{H}^m$$이고, $$\partial\mathbb{H}^m$$을 $$\mathbb{R}^{m-1}$$과 identify하면 이는 $$\mathbb{R}^{m-1}$$의 열린집합이다. 따라서 $$(\varphi^1,\ldots,\varphi^{m-1})\vert_{U\cap\partial M}$$은 $$U\cap\partial M$$에서 $$\mathbb{R}^{m-1}$$의 열린집합으로의 homeomorphism이고, 이들의 transition은 $$M$$의 transition들의 제한이므로 $$C^\infty$$이다. $$\partial M$$이 $$M$$의 subspace로서 Hausdorff이고 second countable인 것은 자명하므로 $$\partial M$$은 $$(m-1)$$차원 manifold이다.

</details>

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> 반공간 $$\mathbb{H}^m$$ 자신은 identity chart 하나로 이루어진 atlas에 대해 경계가 있는 다양체이고, 그 경계는 정의에 의해 $$\partial\mathbb{H}^m\cong\mathbb{R}^{m-1}$$이다. 비슷하게 닫힌구간 $$[0,1]$$은 두 chart $$t\mapsto t$$ (on $$[0,1)$$), $$t\mapsto 1-t$$ (on $$(0,1]$$)에 대해 $$1$$차원의 경계가 있는 다양체이고 $$\partial[0,1]=\{0,1\}$$이다.

조금 더 의미있는 예시로 닫힌 공 $$\overline{B}^m=\{x\in\mathbb{R}^m\mid \lvert x\rvert\leq 1\}$$을 생각하자. 내부는 열린 공이므로 chart 하나로 충분하다. 경계 근방의 점들에 대해서는, $$S^{m-1}$$의 chart $$(V,\theta)$$마다 함수

$$x\mapsto \bigl(\theta(x/\lvert x\rvert),\,1-\lvert x\rvert\bigr)$$

를 생각하면 이것이 $$\{x\neq 0\mid x/\lvert x\rvert\in V\}\cap\overline{B}^m$$에서 $$\mathbb{H}^m$$의 열린집합으로 가는 chart가 되고, transition들이 $$C^\infty$$임을 확인할 수 있다. 따라서 $$\overline{B}^m$$은 경계가 있는 다양체이고 $$\partial\overline{B}^m=S^{m-1}$$이다.

</div>

## 접공간과 바깥 방향

경계가 있는 다양체 $$M$$의 점 $$p$$에서의 tangent space $$T_pM$$은 [§접공간](/ko/math/manifolds/tangent_space)에서와 동일하게 정의한다. 여기서 함수의 germ은 [정의 1](#def1)의 의미에서 $$C^\infty$$인 함수들의 germ이다. 주의할 점은 $$p\in\partial M$$이더라도 $$T_pM$$은 여전히 $$m$$차원이라는 것이다. 이는 [§접공간](/ko/math/manifolds/tangent_space)에서의 논증이 그대로 적용되기 때문인데, 핵심이 되는 Taylor 전개 논증은 정의역이 convex하기만 하면 성립하고, $$\varphi(p)$$ 근방에서 $$\mathbb{H}^m$$과 열린 공의 교집합은 convex하기 때문이다. 특히 $$p\in\partial M$$에서도 chart $$(U,x)$$는 basis $$(\partial/\partial x^1\vert_p,\ldots,\partial/\partial x^m\vert_p)$$를 준다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 경계점 $$p\in\partial M$$에서의 tangent vector $$v=\sum_{i=1}^ma^i\,\partial/\partial x^i\vert_p$$가 *outward<sub>바깥 방향</sub>*라는 것은 $$a^m<0$$인 것이고, *inward<sub>안쪽 방향</sub>*라는 것은 $$a^m>0$$인 것이다.

</div>

이 정의가 의미를 가지려면 $$a^m$$의 부호가 chart의 선택과 무관해야 하고, 이는 다음 보조정리로부터 나온다. 이 보조정리는 아래에서 유도된 향을 정의할 때도 핵심적으로 사용된다.

<div class="proposition" markdown="1">

<ins id="lem7">**보조정리 7**</ins> 두 chart $$(U,x)$$, $$(V,y)$$와 경계점 $$p\in U\cap V\cap \partial M$$에 대하여, transition $$\tau=y\circ x^{-1}$$는 점 $$x(p)$$에서 다음을 만족한다.

$$\frac{\partial y^m}{\partial x^j}(x(p))=0\quad(j<m),\qquad \frac{\partial y^m}{\partial x^m}(x(p))>0$$

특히 $$\det D\tau(x(p))$$와 $$\det\bigl(\partial y^i/\partial x^j\bigr)_{1\leq i,j\leq m-1}(x(p))$$의 부호가 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

함수 $$y^m\circ x^{-1}$$은 $$\mathbb{H}^m$$의 열린집합 위에서 음이 아닌 값을 가지며, [명제 3](#prop3)에 의하여 정확히 $$\partial\mathbb{H}^m$$ 위에서 $$0$$이 된다. $$j<m$$에 대하여 $$x(p)+te_j$$는 $$t$$가 충분히 작을 때 $$\partial\mathbb{H}^m$$에 머무르므로, 이 방향의 편미분은 항등적으로 $$0$$인 함수의 미분이 되어 $$0$$이다. 한편 $$x^m$$ 방향으로는

$$\frac{\partial y^m}{\partial x^m}(x(p))=\lim_{t\to0^+}\frac{(y^m\circ x^{-1})(x(p)+te_m)-0}{t}\geq0$$

이다. 그런데 [명제 3](#prop3)의 증명에서 살펴본 것과 같이 $$D\tau(x(p))$$는 invertible이므로, 마지막 행이 $$(0,\ldots,0,\partial y^m/\partial x^m)$$인 행렬의 행렬식

$$\det D\tau(x(p))=\frac{\partial y^m}{\partial x^m}(x(p))\cdot\det\left(\frac{\partial y^i}{\partial x^j}\right)_{1\leq i,j\leq m-1}(x(p))$$

이 $$0$$이 아니어야 하고, 따라서 $$\partial y^m/\partial x^m(x(p))>0$$이다. 마지막 주장은 위의 행렬식 전개로부터 자명하다.

</details>

이제 [정의 6](#def6)이 잘 정의되는 것을 확인할 수 있다. $$v$$의 두 좌표표현 $$\sum a^i\partial/\partial x^i\vert_p=\sum b^i\partial/\partial y^i\vert_p$$에 대하여 $$b^m=\sum_ja^j\,\partial y^m/\partial x^j(x(p))=a^m\,\partial y^m/\partial x^m(x(p))$$이고, [보조정리 7](#lem7)에 의해 마지막 인수가 양수이기 때문이다.

## 유도된 향

$$\operatorname{int}M$$은 경계가 없는 $$m$$차원 manifold이므로, 우리는 $$M$$이 *orientable*이라는 것을 $$\operatorname{int}M$$이 orientable인 것으로, $$M$$의 *orientation*을 $$\operatorname{int}M$$의 orientation으로 정의한다. ([§향, ⁋정의 1](/ko/math/manifolds/orientation#def1), 그리고 connected 가정에 대해서는 아래의 [참고 10](#rmk10)을 보라.) 또, $$M$$의 chart $$(U,x)$$가 *positively oriented*라는 것은 그 제한 $$(U\cap\operatorname{int}M,x)$$가 [§향, ⁋명제 2](/ko/math/manifolds/orientation#prop2)의 의미에서 주어진 orientation과 호환되는 것, 즉 $$dx^1\wedge\cdots\wedge dx^m$$이 $$U\cap\operatorname{int}M$$ 위에서 선택된 component에 들어가는 것이다.

$$m\geq 2$$라면 oriented manifold with boundary $$M$$은 항상 positively oriented chart들로 덮을 수 있다. Chart가 positively oriented가 아니라면 $$x^1$$의 부호를 바꾼 chart $$(U,(-x^1,x^2,\ldots,x^m))$$가 여전히 $$\mathbb{H}^m$$의 열린집합으로 가는 chart이면서 orientation이 뒤집히기 때문이다. 반면 $$m=1$$인 경우에는 이러한 조작이 불가능한데, 부호를 바꿀 수 있는 좌표가 마지막 좌표 $$x^1$$ 뿐이고 이것의 부호를 바꾸면 chart가 $$\mathbb{H}^1$$을 벗어나기 때문이다. 실제로 $$[0,1]$$의 양 끝점을 모두 $$\mathbb{H}^1$$-chart로 덮으면 두 chart의 orientation은 반드시 반대가 된다. 이러한 이유로 $$m=1$$인 경우에는 negatively oriented chart도 함께 사용하되, 적분 등을 정의할 때 부호를 붙여 사용한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$M$$이 oriented manifold with boundary라 하고 $$m\geq 2$$라 하자. 그럼 $$M$$의 positively oriented chart들을 [명제 4](#prop4)에서와 같이 제한하여 얻은 $$\partial M$$의 chart들

$$\bigl(U\cap\partial M,\ (x^1,\ldots,x^{m-1})\vert_{\partial M}\bigr)$$

은 transition들의 Jacobian의 행렬식이 항상 $$0$$보다 큰 $$\partial M$$의 atlas를 이룬다. 특히 $$\partial M$$은 orientable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 positively oriented chart의 transition $$\tau$$와 경계점에서의 그 제한을 생각하자. $$\partial M$$ 위에서의 transition의 Jacobian matrix는 정확히 $$\bigl(\partial y^i/\partial x^j\bigr)_{1\leq i,j\leq m-1}$$이고, [보조정리 7](#lem7)에 의하여 이 행렬의 행렬식은 $$\det D\tau>0$$과 같은 부호를 가지므로 양수이다.

</details>

다만 Stokes 정리의 부호를 맞추기 위해서는 [명제 8](#prop8)의 orientation을 그대로 쓰는 대신 다음과 같이 수정하는 것이 표준적이다. 점 $$p\in\partial M$$에서, outward vector $$\nu$$를 맨 앞에 둔 ordered basis $$(\nu,v_1,\ldots,v_{m-1})$$ ($$v_i\in T_p\partial M$$)가 $$M$$의 orientation에 대해 positively oriented일 때 $$(v_1,\ldots,v_{m-1})$$이 positively oriented이도록 $$\partial M$$의 orientation을 잡는 것이다. Positively oriented chart $$(U,x)$$에서 $$\nu=-\partial/\partial x^m$$으로 택하고 행렬식을 계산하면

$$\det\bigl[-e_m\ e_1\ \cdots\ e_{m-1}\bigr]=(-1)^m$$

이므로, 이는 [명제 8](#prop8)의 atlas가 주는 orientation에 $$(-1)^m$$을 곱한 것이다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Oriented manifold with boundary $$M$$ ($$m\geq 2$$)에 대하여, $$\partial M$$의 *유도된 향<sub>induced orientation</sub>*은 [명제 8](#prop8)의 atlas가 주는 orientation에 $$(-1)^m$$을 곱한 것, 즉 $$m$$이 짝수라면 그 atlas 자신이 positively oriented이고 $$m$$이 홀수라면 그 atlas의 첫 좌표의 부호를 바꾼 것이 positively oriented이도록 하는 orientation이다.

$$m=1$$인 경우 $$\partial M$$은 $$0$$차원 manifold, 즉 점들의 모임이고, 이 때 orientation은 각 점에 부호 $$\pm1$$을 주는 것으로 정의한다. 유도된 향은 outward vector가 $$T_pM$$의 orientation에 대해 positively oriented인 점 $$p$$에 $$+1$$을, 그렇지 않은 점에 $$-1$$을 주는 것이다.

</div>

<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> $$\partial M$$은 $$M$$이 connected이더라도 connected일 필요가 없다. 가령 $$\partial[0,1]=\{0,1\}$$은 두 점이다. [§향](/ko/math/manifolds/orientation)에서는 편의상 connected manifold에 대해 orientation을 정의했지만, 위에서와 같이 positively oriented atlas의 언어로 정의하면 connected 가정 없이도 의미를 가지며, 이는 각 connected component마다 orientation을 골라주는 것과 같다.

</div>

다음 글에서는 이 글에서 준비한 언어를 사용하여 미적분학의 기본정리의 일반화인 Stokes 정리를 증명한다.

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---
