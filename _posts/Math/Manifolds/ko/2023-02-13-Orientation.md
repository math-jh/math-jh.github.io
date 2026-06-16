---
title: "향"
description: "벡터 공간과 다양체에서의 방향을 다룹니다. 행렬식의 부호로 기저의 순서를 판별하고, 오리엔터블 다양체의 성질을 양의 야코비안을 갖는 좌표계와 소멸하지 않는 최고차 미분형으로 나타냅니다."
excerpt: "Manifold 위의 orientation"

categories: [Math / Manifolds]
permalink: /ko/math/manifolds/orientation
sidebar: 
    nav: "manifolds-ko"

date: 2023-02-13
weight: 19
published: false

---

## 유클리드 공간에서의 방향

3차원 공간에서 주어진 standard basis $$(e_1,e_2,e_3)$$를 생각하자. 우리는 미적분학을 배울 때부터 이 basis가 배열된 순서가 중요하다는 것을 알고 있다. 예를 들어, 위의 basis는 $$e_1\times e_2=e_3$$을 만족하지만, 순서가 바뀌어 $$(e_2,e_1,e_3)$$과 같은 식으로 배열되어 있다면 $$e_2\times e_1=-e_3$$이 되었을 것이다. 

이 관찰을 굳이 standard basis로 한정지을 필요는 없다. 일반적으로 $$\mathbb{R}^3$$의 모든 orthonormal basis $$(x_1,x_2,x_3)$$에 대하여도 $$x_1\times x_2$$의 값이 $$x_3$$인지 $$-x_3$$인지의 여부에 따라 이 basis가 올바른 순서로 배열되었는지 아닌지를 알 수 있다. 이를 식으로 나타내면

$$x_3\cdot(x_1\times x_2)$$

의 값이 $$+1$$인지, $$-1$$인지에 따라 순서가 결정되는 것이다. 그런데 위의 식은

$$x_3\cdot(x_1\times x_2)=\det[x_3\;x_1\;x_2]=\det[x_1\;x_2\;x_3]$$

과 같으므로, 우리는 orthonormal이 아닌 일반적인 basis에 대해서도 위의 행렬식의 값이 양수인지 음수인지를 읽어내어 순서를 정해줄 수 있다.

이렇게 $$\mathbb{R}^3$$의 경우에서 basis의 순서를 행렬식을 통해 정의하고 나면, $$\mathbb{R}^m$$에서도 자연스럽게 basis $$(x_1,\ldots, x_m)$$이 올바른 순서로 배열되었는지, 혹은 반대로 배열되었는지를 알 수 있다. 즉 다음의 행렬식

$$\det[x_1\;x_2\;\cdots\;x_m]$$

의 부호를 조사해보면 된다.

## 행렬식과 방향

$$V,W$$가 $$n$$차원 $$\mathbb{R}$$ 벡터공간이라 하고, linear map $$L:V\rightarrow W$$가 주어졌다 하자. 그럼 [\[다중선형대수학\] §텐서대수, ⁋명제 11](/ko/math/multilinear_algebra/tensor_algebras#prop11)의 universal property에 의하여, 다음의 linear map

$$\bigwedge\nolimits^n(L):\bigwedge\nolimits^n(V)\rightarrow\bigwedge\nolimits^n(W)$$

이 잘 정의된다. 한편 $$V,W$$가 모두 $$n$$차원이므로 $$\bigwedge\nolimits^n(V),\bigwedge\nolimits^n(W)$$는 모두 1차원 벡터공간이 되고, 따라서 위의 linear map은 임의의 영이 아닌 벡터가 어디로 옮겨지는지에 의해 유일하게 결정된다. 특히 만일 $$V=W$$라면, $$\bigwedge\nolimits^n(V)$$의 영이 아닌 임의의 벡터는 항상 자기 자신의 상수배로 옮겨지게 되며, 이 때의 상수가 $$L$$의 행렬식과 같다. 이러한 관점에서 $$\bigwedge\nolimits^n(L)$$을 *determinant map*이라 부르기도 하고, $$E$$가 manifold $$M$$ 위에 정의된 $$n$$차원의 vector bundle이라면 $$\bigwedge\nolimits^n(E)$$를 $$E$$의 *determinant bundle*이라 부르기도 한다.

특별히 $$E=T^\ast M$$이라면 다음과 같이 정의한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$M$$이 $$m$$차원의 connected manifold라 하자. 이 때, $$M$$이 *orientable*이라는 것은 $$\bigwedge\nolimits^m(M)\setminus\{0\}$$이 두 개의 component를 갖는 것이고, 이 때 두 component중 하나를 택하는 것을 $$M$$의 *orientation*이라 부른다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$M$$이 $$m$$차원의 connected manifold라 하자. 다음이 모두 동치이다.

1. $$M$$이 orientable이다.
2. $$M$$을 덮는 적당한 coordinate system들의 모임이 존재하여, 이들이 겹치는 곳에서 Jacobian이 항상 0보다 크도록 할 수 있다.
3. $$M$$ 위에 정의된 non-vanishing $$m$$-form이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

편의상 $$M$$의 coordinate system들은 모두 connected인 것으로 가정한다. 이는 항상 가능한데, 임의의 chart의 정의역을 좌표근방 안의 열린 공들로 제한하면 되기 때문이다. 또, coordinate system $$(U,x)$$마다 $$U$$ 위에서 정의된 non-vanishing $$m$$-form

$$\omega_U=dx^1\wedge\cdots\wedge dx^m$$

을 생각하자. 두 coordinate system $$(U,x)$$, $$(V,y)$$가 겹치는 곳에서는 다음의 변환식

$$dy^1\wedge\cdots\wedge dy^m=\det\left(\frac{\partial y^i}{\partial x^j}\right)dx^1\wedge\cdots\wedge dx^m$$

이 성립한다는 것을 기억하자.

**(3)$$\implies$$(2)** Non-vanishing $$m$$-form $$\omega$$가 주어졌다 하자. 임의의 connected coordinate system $$(U,x)$$ 위에서 $$\omega=f\,\omega_U$$로 쓰면 $$f$$는 non-vanishing인 연속함수이고, $$U$$가 connected이므로 $$f>0$$이거나 $$f<0$$이다. 후자의 경우 $$x^1$$과 $$x^2$$를 맞바꾸면 (혹은 $$m=1$$일 때 $$x^1$$을 $$-x^1$$으로 바꾸면) $$\omega_U$$의 부호가 바뀌므로, $$M$$을 덮는 coordinate system들을 모두 $$f>0$$이도록 택할 수 있다. 그럼 이들이 겹치는 곳에서 $$\omega=f\,\omega_U=g\,\omega_V$$ ($$f,g>0$$)이고, 위의 변환식에 의하여 Jacobian의 행렬식은 $$f/g>0$$이다.

**(2)$$\implies$$(1)** 조건을 만족하는 coordinate system들의 모임 $$(U_\alpha,x_\alpha)$$가 주어졌다 하자. $$\Lambda=\bigwedge\nolimits^m(M)$$이라 적고, 다음의 두 집합

$$\Lambda^+=\left\{t\,\omega_{U_\alpha}(p)\mid \text{$p\in U_\alpha$, $t>0$}\right\},\qquad \Lambda^-=\left\{t\,\omega_{U_\alpha}(p)\mid \text{$p\in U_\alpha$, $t<0$}\right\}$$

을 생각하자. 겹치는 곳에서 $$\omega_{U_\alpha}$$들은 서로의 positive multiple이므로 ($$\det>0$$ 가정) 이 두 집합은 서로소이고, 각 fiber가 $$\omega_{U_\alpha}(p)$$로 span되는 1차원 벡터공간이므로 $$\Lambda^+\sqcup\Lambda^-=\Lambda\setminus\{0\}$$이다. 한편 vector bundle의 chart

$$\Lambda\vert_{U_\alpha}\cong U_\alpha\times \mathbb{R};\qquad t\,\omega_{U_\alpha}(p)\mapsto (p,t)$$

에 의하여 $$\Lambda^+\cap \Lambda\vert_{U_\alpha}\cong U_\alpha\times(0,\infty)$$은 열린집합이고 connected이다. 따라서 $$\Lambda^+$$는 이러한 connected 열린집합들의 합집합인데, $$M$$이 connected이므로 임의의 두 $$U_\alpha$$들은 서로 겹치는 chart들의 유한한 사슬로 연결되고, 사슬을 따라 $$U_\alpha\times(0,\infty)$$꼴의 집합들이 차례로 만나므로 $$\Lambda^+$$는 connected이다. 같은 이유로 $$\Lambda^-$$도 connected인 열린집합이다. 즉 $$\Lambda\setminus\{0\}$$은 공집합이 아닌 서로소인 두 connected 열린집합의 합집합이므로 정확히 두 개의 component를 갖는다.

**(1)$$\implies$$(2)** $$\Lambda\setminus\{0\}$$이 정확히 두 개의 component $$\Lambda_1,\Lambda_2$$를 갖는다 하자. 우선 $$0$$이 아닌 임의의 $$v\in\Lambda\setminus\{0\}$$에 대하여 ray $$\{tv\mid t>0\}$$는 connected이므로 하나의 component에 포함되고, 스칼라곱 $$\mu:v\mapsto -v$$는 $$\Lambda\setminus\{0\}$$의 homeomorphism이므로 component들을 component들로 보낸다.

이제 임의의 점 $$p$$에서 fiber의 두 ray가 서로 다른 component에 속한다는 것을 보이자. 결론에 반하여 어떤 fiber의 두 ray가 모두 한 component에 속한다 가정하자. Connected coordinate system $$(U,x)$$에 대하여 $$\Lambda\vert_U\setminus\{0\}\cong U\times(\mathbb{R}\setminus\{0\})$$의 두 조각 $$U\times(0,\infty)$$와 $$U\times(-\infty,0)$$은 각각 connected이므로 각각 하나의 component에 포함된다. 그런데 어떤 $$p\in U$$에서 두 ray가 같은 component $$\Lambda_1$$에 속한다면, 두 조각이 모두 $$\Lambda_1$$과 만나므로 $$\Lambda\vert_U\setminus\{0\}\subseteq\Lambda_1$$이다. 즉 "fiber의 두 ray가 같은 component에 속하는 점들의 집합"과 그 여집합은 모두 열린집합이고, $$M$$이 connected이므로 가정에 의해 모든 점에서 두 ray가 같은 component에 속한다. 그럼 위의 논증을 $$M$$을 덮는 chart들의 사슬에 적용하면 $$\Lambda\setminus\{0\}$$ 전체가 하나의 component가 되어, component가 두 개라는 가정에 모순이다.

따라서 각 fiber는 두 component와 ray 하나씩으로 만난다. 이제 component 하나를 택해 $$\Lambda^+$$라 부르자. 임의의 connected coordinate system $$(U,x)$$에 대하여 $$\omega_U(U)$$는 connected이므로 하나의 component에 포함되고, 만일 그것이 $$\Lambda^+$$가 아니라면 (3)$$\implies$$(2)에서와 같이 좌표를 맞바꾸어 $$\omega_U(U)\subseteq \Lambda^+$$이도록 할 수 있다. 이렇게 얻은 coordinate system들의 모임에 대하여, 겹치는 점 $$p$$에서 $$\omega_{U}(p)$$와 $$\omega_{V}(p)$$는 같은 fiber에서 모두 $$\Lambda^+$$에 속하므로 같은 ray에 속하고, 즉 서로의 positive multiple이다. 따라서 변환식에 의해 Jacobian의 행렬식이 항상 $$0$$보다 크다.

**(2)$$\implies$$(3)** 조건을 만족하는 coordinate system들의 모임 $$(U_\alpha,x_\alpha)$$를 생각하자. Manifold는 paracompact Hausdorff이므로 open cover $$(U_\alpha)$$에 subordinate한 partition of unity가 존재하고 ([\[위상수학\] §옹골성, ⁋정리 7](/ko/math/topology/compactness#thm7)), [§미분다양체, §§Smooth partition of unity](/ko/math/manifolds/smooth_manifolds)에서 살펴본 것과 같이 이를 $$C^\infty$$이도록 택할 수 있다. 이 partition of unity를 $$(\phi_i)_{i\in I}$$라 하고 각각의 $$i$$마다 $$\supp\phi_i\subseteq U_{\alpha(i)}$$라 하자. 이제

$$\omega=\sum_{i\in I}\phi_i\,\omega_{U_{\alpha(i)}}$$

으로 정의하면, 각 항은 $$M$$ 전체에서 정의된 $$C^\infty$$ $$m$$-form으로 확장되고 ($$\supp\phi_i$$ 바깥에서 $$0$$), 합은 locally finite이므로 $$\omega$$는 $$M$$ 위의 $$C^\infty$$ $$m$$-form이다. 임의의 점 $$p$$에서 $$\sum\phi_i(p)=1$$이므로 $$\phi_i(p)>0$$인 $$i$$가 존재하고, 그러한 $$i$$들에 대하여 $$\omega_{U_{\alpha(i)}}(p)$$들은 모두 서로의 positive multiple이므로 $$\omega(p)$$는 이들 중 하나의 positive multiple이 되어 $$0$$이 아니다. 즉 $$\omega$$는 non-vanishing $$m$$-form이다.

종합하면 (3)$$\implies$$(2)$$\implies$$(1)$$\implies$$(2)$$\implies$$(3)이므로 세 조건이 모두 동치이다.

</details>

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> 

임의의 Lie group은 orientable이다. 이는 $$\Omega_\text{l.inv}^\ast(G)$$에서의 임의의 basis $$\omega_1,\ldots,\omega_n$$을 택한 후, 이들의 wedge $$\omega_1\wedge\cdots\wedge\omega_n$$을 생각하면 이것이 $$G$$ 위에서 nonvanishing $$n$$-form을 정의하기 때문이다.

</div>

---

**참고문헌**

**[War]** Frank W. Warner. *Foundations of Differentiable Manifolds and Lie Groups*, Graduate texts in mathematics, Springer, 2013  
**[Lee]** John M. Lee. *Introduction to Smooth Manifolds*, Graduate texts in mathematics, Springer, 2012  

---