---
title: "몫공간"
description: "부분공간으로 벡터공간을 나눈 몫공간을 coset을 통해 구성하고, 연산의 잘 정의됨과 차원 공식을 증명한다. 나아가 자연스러운 사영, 보편 성질, 그리고 제1동형정리를 살펴본다."
excerpt: "부분공간으로 나눈 몫공간"

categories: [Math / Linear Algebra]
permalink: /ko/math/linear_algebra/quotient_space
sidebar: 
    nav: "linear_algebra-ko"


date: 2026-06-19

weight: 8

published: false

---

우리는 이번 글에서 $$\mathbb{K}$$-벡터공간 $$V$$와 그 부분공간 $$W$$에 대하여, 그 *몫공간<sub>quotient space</sub>* $$V/W$$를 정의한다. 직관적으로 이는 $$V$$ 안에서, $$W$$의 원소들을 모두 $$0$$으로 만들어서 얻어지는 공간으로, 다만 이렇게 $$W$$의 원소들을 모두 $$0$$으로 만든 후에도 남아있는 공간이 여전히 벡터공간이기를 바라므로, $$W$$의 모든 원소들을 단순히 $$0$$이라고 선언하는 것만으로는 이를 달성할 수 없다. 

## 잉여류

가장 큰 문제는, 위에서 지적했듯 $$W$$의 원소들을 모두 $$0$$으로 두기만 한다면, 남아있는 공간이 벡터공간이 되리라는 보장이 없다는 것이다. 가령, 이것이 벡터공간이 되기 위해서는 우선 연산에 대해 닫혀있어야 하는데, 임의의 $$V$$의 원소 $$v$$는 항상 고정된 $$w\in W$$에 대하여 $$v=(v-w)+w$$의 형태로 쓸 수 있고, 따라서 만일 $$v$$와 $$v-w$$가 $$W$$에 속하지 않는다면, $$W$$의 모든 원소를 $$0$$으로 취급하여도

$$v-(v-w)=w=0$$

가 되어, $$v$$와 $$v-w$$가 같지 않음에도 불구하고 이들의 차가 $$0$$이 되어버린다. 

이는 두 가지를 보여준다. 우선 $$V/W$$를 정의하기 위해서는 이를 단순히 $$W$$의 모든 원소를 $$0$$으로 두고 나머지 원소들을 그대로 두는 것으로는 불충분하다. 둘째로, 더 중요한 것은 위의 단순한 계산이 실제로 $$V/W$$를 어떻게 만들지에 대한 힌트도 준다는 것이다. 즉 우리는 만일 두 벡터 $$v,v'$$의 차이가 $$W$$에 들어있다면, 이를 $$V/W$$ 안에서는 <em-ko>같은</em-ko> 원소로 취급해야 한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\mathbb{K}$$-벡터공간 $$V$$와 그 부분공간 $$W\leq V$$가 주어졌다 하자. 임의의 $$v\in V$$에 대하여, 다음의 집합

$$v+W=\{v+w\mid w\in W\}$$

을 $$v$$를 포함하는 $$W$$의 *coset<sub>잉여류</sub>*라 부른다.

</div>

정의에서 coset $$v+W$$은 $$v$$와의 차이가 $$W$$에 속하는 벡터들, 즉 도입부에서 $$V/W$$ 안에서 $$v$$와 같게 취급하기로 한 벡터들을 모두 모은 집합이다. 이는 집합론에서 다루는 동치류의 한 예시이지만 ([\[집합론\] §동치관계, ⁋정의 4](/ko/math/set_theory/equivalence_relations#def4)), 우리에게 필요한 것은 위의 도입에서 주장한, 두 coset이 같은지를 대표원의 차이로 판정하는 다음 사실 뿐이다.

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> $$\mathbb{K}$$-벡터공간 $$V$$와 그 부분공간 $$W\leq V$$, 그리고 임의의 두 벡터 $$v,v'\in V$$에 대하여, 다음의 동치

$$v+W=v'+W\iff v-v'\in W$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$v-v'\in W$$라 하면, 임의의 $$v+w\in v+W$$에 대하여 $$v+w=v'+\bigl((v-v')+w\bigr)\in v'+W$$이고 그 역도 같은 방식으로 성립하므로 $$v+W=v'+W$$이다. 거꾸로 $$v+W=v'+W$$라 하면, $$v=v+0\in v'+W$$이므로 $$v=v'+w$$를 만족하는 $$w\in W$$가 존재하고 따라서 $$v-v'=w\in W$$이다.

</details>

특히 $$v+W=W$$인 것은 $$v\in W$$인 것과 동치이고, 이로부터 서로 다른 두 coset은 항상 서로소임을 안다.

## 몫공간의 정의

이제 coset들 위에 벡터공간 구조를 부여하자. 

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$\mathbb{K}$$-벡터공간 $$V$$와 그 부분공간 $$W\leq V$$에 대하여, $$W$$의 coset들을 모두 모은 집합을 $$V/W$$로 적고 이를 $$W$$에 의한 $$V$$의 *몫공간<sub>quotient space</sub>*이라 부른다. $$V/W$$ 위의 덧셈과 스칼라곱은 각각 다음의 식

$$(v+W)+(v'+W)=(v+v')+W,\qquad \alpha(v+W)=(\alpha v)+W$$

으로 정의한다.

</div>

위의 정의에서 덧셈과 스칼라곱은 coset을 대표하는 벡터 $$v$$를 통해 기술되었으므로, 이들이 대표원의 선택과 무관하게 잘 정의되는지를 확인해야 한다. 즉, $$v+W=v_1+W$$이고 $$v'+W=v_1'+W$$라면 

$$(v+v')+W=(v_1+v_1')+W,\qquad (\alpha v)+W=(\alpha v_1)+W$$

이 성립해야 한다. 가정에 의해 $$v-v_1\in W$$이고 $$v'-v_1'\in W$$이므로, $$W$$가 덧셈에 대해 닫혀있다는 사실로부터

$$(v+v')-(v_1+v_1')=(v-v_1)+(v'-v_1')\in W$$

이고, $$W$$가 스칼라곱에 대해 닫혀있다는 사실로부터

$$(\alpha v)-(\alpha v_1)=\alpha(v-v_1)\in W$$

이다. [보조정리 2](#lem2)에 의해 이는 정확히 우리가 원하던 식이다. 따라서 $$V/W$$ 위의 두 연산은 잘 정의된다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> [정의 3](#def3)의 연산을 부여한 $$V/W$$는 $$\mathbb{K}$$-벡터공간이다. 이 때 덧셈에 대한 항등원은 $$0+W=W$$이고, $$v+W$$의 덧셈에 대한 역원은 $$(-v)+W$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

벡터공간의 모든 공리는 $$V/W$$의 연산이 $$V$$의 연산으로부터 coset 단위로 유도된다는 사실로부터 곧바로 따라온다. 예를 들어 덧셈의 결합법칙은 임의의 $$v,v',v''\in V$$에 대하여

$$\bigl((v+W)+(v'+W)\bigr)+(v''+W)=\bigl((v+v')+v''\bigr)+W=\bigl(v+(v'+v'')\bigr)+W=(v+W)+\bigl((v'+W)+(v''+W)\bigr)$$

이 성립하는 것으로부터 따라오며, 이는 $$V$$에서의 덧셈의 결합법칙의 직접적인 귀결이다. 교환법칙과 분배법칙, 그리고 스칼라곱에 대한 공리들 또한 같은 방식으로 확인된다. 한편 임의의 $$v\in V$$에 대하여

$$(v+W)+(0+W)=(v+0)+W=v+W,\qquad (v+W)+((-v)+W)=(v-v)+W=0+W$$

이므로 $$0+W$$이 덧셈에 대한 항등원이고 $$(-v)+W$$이 $$v+W$$의 역원이다.

</details>

## 몫공간의 차원

몫공간의 가장 기본적인 불변량은 그 차원이며, 이는 $$V$$와 $$W$$의 차원으로부터 곧바로 결정된다. 

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> 유한차원 $$\mathbb{K}$$-벡터공간 $$V$$와 그 부분공간 $$W\leq V$$에 대하여, 다음의 식

$$\dim(V/W)=\dim V-\dim W$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim W=k$$, $$\dim V=n$$이라 하고, $$W$$의 basis $$\{x_1,\ldots, x_k\}$$를 택하자. 이는 $$V$$의 일차독립인 부분집합이므로, [§벡터공간의 차원, ⁋명제 5](/ko/math/linear_algebra/dimension#prop5)에 의하여 이를 확장하여 $$V$$의 basis $$\{x_1,\ldots, x_k, x_{k+1},\ldots, x_n\}$$을 얻을 수 있다. 우리는 다음의 coset들

$$x_{k+1}+W,\quad\ldots,\quad x_n+W$$

이 $$V/W$$의 basis가 됨을 보인다.

우선 이들은 $$V/W$$를 span한다. 임의의 $$v\in V$$에 대하여, $$v=\sum_{i=1}^n\alpha_ix_i$$라 하면 

$$v+W=\sum_{i=1}^n\alpha_i(x_i+W)=\sum_{i=k+1}^n\alpha_i(x_i+W)$$

인데, 마지막 등호는 $$i\leq k$$에 대하여 $$x_i\in W$$이므로 $$x_i+W=W$$이 $$V/W$$의 영벡터인 것으로부터 성립한다. 

다음으로 이들은 일차독립이다. 스칼라들 $$\alpha_{k+1},\ldots,\alpha_n$$에 대하여 

$$\sum_{i=k+1}^n\alpha_i(x_i+W)=0+W$$

라 하자. 그럼 $$\sum_{i=k+1}^n\alpha_ix_i+W=W$$이므로 [보조정리 2](#lem2)에 의해 $$\sum_{i=k+1}^n\alpha_ix_i\in W$$이다. 따라서 이 벡터를 $$W$$의 basis로 나타내어 적당한 스칼라들 $$\beta_1,\ldots,\beta_k$$에 대해

$$\sum_{i=k+1}^n\alpha_ix_i=\sum_{i=1}^k\beta_ix_i$$

이라 할 수 있다. 그런데 $$\{x_1,\ldots, x_n\}$$은 $$V$$의 basis로서 일차독립이므로 모든 계수가 $$0$$이어야 하고, 특히 $$\alpha_{k+1}=\cdots=\alpha_n=0$$이다. 

따라서 $$\{x_{k+1}+W,\ldots, x_n+W\}$$은 $$V/W$$의 basis이고, 그 원소의 개수는 $$n-k$$이므로 $$\dim(V/W)=n-k=\dim V-\dim W$$이다.

</details>

## 자연스러운 사영과 제1동형정리

몫공간이 자연스럽게 등장하는 맥락은 linear map과 함께할 때 비로소 분명해진다. 우리는 [§선형사상](/ko/math/linear_algebra/linear_map)에서 linear map을, [§동형사상](/ko/math/linear_algebra/isomorphic_vector_spaces)에서 isomorphism과 rank-nullity 정리를 살펴보았으므로, 이제 이들과 몫공간의 관계를 살펴본다. 

임의의 $$\mathbb{K}$$-벡터공간 $$V$$와 부분공간 $$W\leq V$$에 대하여, 다음의 식

$$\pi(v)=v+W$$

으로 정의된 함수 $$\pi:V\rightarrow V/W$$를 생각하자. 그럼 [정의 3](#def3)의 연산은 정확히 $$\pi$$가 다음의 두 식

$$\pi(\alpha v)=(\alpha v)+W=\alpha(v+W)=\alpha\pi(v),\qquad \pi(v+v')=(v+v')+W=(v+W)+(v'+W)=\pi(v)+\pi(v')$$

을 만족하도록 정의된 것이다. 즉 $$\pi$$는 linear map이며, 이를 $$V$$에서 $$V/W$$로의 *자연스러운 사영<sub>natural projection</sub>*이라 부른다. 정의에 의해 $$\pi$$는 전사이고, 

$$\ker\pi=\{v\in V\mid v+W=W\}=W$$

이 성립한다. 이로부터 임의의 부분공간은 적당한 linear map의 kernel로 나타난다는 것을 안다. 

자연스러운 사영의 가장 중요한 성질은 다음의 보편 성질이다. 이는 $$W$$를 $$0$$으로 보내는 임의의 linear map이 $$V/W$$를 거쳐 유일하게 분해된다는 것을 말한다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$\mathbb{K}$$-벡터공간 $$V$$와 부분공간 $$W\leq V$$, 그리고 또 다른 $$\mathbb{K}$$-벡터공간 $$U$$로의 linear map $$L:V\rightarrow U$$가 $$W\subseteq\ker L$$을 만족한다 하자. 그럼 다음의 식

$$\bar L(v+W)=L(v)$$

으로 정의된 linear map $$\bar L:V/W\rightarrow U$$가 유일하게 존재하여 $$L=\bar L\circ\pi$$를 만족한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\bar L$$이 잘 정의됨을 보인다. $$v+W=v'+W$$라 하면 $$v-v'\in W\subseteq\ker L$$이므로 

$$L(v)-L(v')=L(v-v')=0$$

이고 따라서 $$L(v)=L(v')$$이다. 즉 $$\bar L(v+W)$$의 값은 대표원의 선택과 무관하다. $$\bar L$$이 linear인 것은 

$$\bar L\bigl(\alpha(v+W)+(v'+W)\bigr)=\bar L\bigl((\alpha v+v')+W\bigr)=L(\alpha v+v')=\alpha L(v)+L(v')=\alpha\bar L(v+W)+\bar L(v'+W)$$

으로부터 따라온다. 또 임의의 $$v\in V$$에 대하여 $$(\bar L\circ\pi)(v)=\bar L(v+W)=L(v)$$이므로 $$L=\bar L\circ\pi$$이다. 마지막으로 $$L=L'\circ\pi$$를 만족하는 linear map $$L':V/W\rightarrow U$$가 주어졌다 하면, $$\pi$$가 전사이므로 임의의 $$v+W\in V/W$$에 대하여 $$L'(v+W)=L'(\pi(v))=L(v)=\bar L(v+W)$$이고 따라서 $$L'=\bar L$$이다.

</details>

특히 위의 보편 성질을 $$W=\ker L$$인 경우에 적용하면, 벡터공간을 분류하는 데에 핵심적인 다음의 정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (제1동형정리)**</ins> 두 $$\mathbb{K}$$-벡터공간 $$V,U$$와 linear map $$L:V\rightarrow U$$에 대하여, 다음의 식

$$\bar L(v+\ker L)=L(v)$$

으로 정의된 linear map $$\bar L:V/\ker L\rightarrow \im L$$은 isomorphism이다. 즉 $$V/\ker L\cong\im L$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$W=\ker L$$로 두면 [명제 6](#prop6)에 의하여 $$\bar L(v+\ker L)=L(v)$$으로 정의된 linear map $$\bar L:V/\ker L\rightarrow U$$이 잘 정의되며, 그 image는 $$\im L$$과 같다. 따라서 공역을 $$\im L$$로 제한하면 $$\bar L:V/\ker L\rightarrow\im L$$은 전사이다. 한편 $$\bar L(v+\ker L)=0$$이라 하면 $$L(v)=0$$, 즉 $$v\in\ker L$$이므로 $$v+\ker L=\ker L$$이 $$V/\ker L$$의 영벡터이다. 따라서 $$\ker\bar L=\{0\}$$이고 ([§선형사상, ⁋명제 8](/ko/math/linear_algebra/linear_map#prop8)) $$\bar L$$은 단사이다. 따라서 $$\bar L$$은 전단사인 linear map이므로 isomorphism이다. ([§동형사상, ⁋보조정리 2](/ko/math/linear_algebra/isomorphic_vector_spaces#lem2))

</details>

제1동형정리와 [정리 5](#thm5)를 결합하면 rank-nullity 정리를 다시 얻는다. 실제로 유한차원 $$V$$에 대하여 

$$\rank L=\dim\im L=\dim(V/\ker L)=\dim V-\dim\ker L=\dim V-\nullity L$$

이 성립하며, 이는 정확히 [§동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)의 식이다. 즉 rank-nullity 정리는 $$L$$이 $$\ker L$$을 "접어버린" 후에는 단사가 된다는 사실을 차원의 언어로 옮긴 것에 지나지 않는다. 

---

**참고문헌**

**[Goc]** M.S. Gockenbach, *Finite-dimensional linear algebra*, Discrete Mathematics and its applications, Taylor&Francis, 2011.  
**[Rom]** S. Roman, *Advanced linear algebra*, 3rd ed., Graduate Texts in Mathematics 135, Springer, 2008.

---
