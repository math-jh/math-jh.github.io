---
title: "sl₂의 표현론"
description: "sl₂(ℂ)의 유한차원 표현을 완전히 분류한다. 각 정수 n≥0에 대해 차원 n+1의 기약 표현 V(n)이 유일하게 존재함을 보이고, 모든 유한차원 표현이 weight 분해되어 완전가약임을 Casimir element로 증명한 뒤, 텐서곱의 분해를 주는 Clebsch–Gordan 공식을 유도한다."
excerpt: "sl₂의 기약표현 V(n), weight string, 완전가약성, Clebsch–Gordan 공식"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/representations_of_sl2
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 7.1

published: false
---

Semisimple Lie algebra의 표현론 전체에서 $$\sl_2$$는 가장 작으면서도 가장 근본적인 경우이다. 임의의 semisimple Lie algebra의 각 root $$\alpha$$는 그 안에 $$\sl_2$$와 isomorphic한 subalgebra $$\sl_{2,\alpha}$$를 낳고 ([§근계, ⁋명제 12](/ko/math/lie_theory/root_systems#prop12) 이후의 논의), 일반적인 highest weight 이론의 integrality와 Weyl group 대칭성은 모두 이 $$\sl_2$$들에 대한 표현론을 root별로 적용하여 얻어진다. 이 글에서 우리는 $$\sl_2=\sl(2;\mathbb{C})$$의 유한차원 표현을 완전히 분류한다. 각 정수 $$n\geq 0$$마다 차원 $$n+1$$의 기약 표현 $$V(n)$$이 동형을 무시하고 유일하게 존재함을 보이고, 임의의 유한차원 표현이 $$h$$의 작용으로 weight 분해되어 완전가약<sub>completely reducible</sub>임을 Casimir element를 통해 증명한 뒤, 두 기약 표현의 텐서곱을 분해하는 Clebsch–Gordan 공식을 유도한다.

이 글 전체에서 기반 체는 $$\mathbb{C}$$이며, $$\sl_2$$의 representation이란 Lie algebra 준동형 $$\sl_2\rightarrow\gl(V)$$, 곧 유한차원 $$\mathbb{C}$$-벡터공간 $$V$$ 위의 $$\sl_2$$-가군 구조를 뜻한다. $$x\in\sl_2$$와 $$v\in V$$에 대하여 그 작용을 $$x\cdot v$$로 적는다.

## 표준 기저와 weight space

$$\sl_2$$는 traceless $$2\times 2$$ 복소행렬들의 Lie algebra이며 ([§리 군, ⁋명제 12](/ko/math/lie_theory/Lie_groups#prop12)), *standard basis<sub>표준 기저</sub>*

$$h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad f=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

와 commutation relation

$$[h,e]=2e,\qquad [h,f]=-2f,\qquad [e,f]=h$$

을 갖는다. ([§근계](/ko/math/lie_theory/root_systems#예시-sl2mathbbc)) 이 세 관계식이 $$\sl_2$$의 Lie algebra 구조를 완전히 결정하므로, $$\sl_2$$의 representation을 분석한다는 것은 이 관계식을 만족하는 세 연산자 $$h,e,f$$를 유한차원 공간 위에서 분석하는 것과 같다.

분석의 출발점은 $$h$$의 작용을 대각화하는 데에 있다. $$h$$의 고윳값을 따라 공간을 쪼개면, $$e$$와 $$f$$가 그 고윳값을 각각 $$+2$$, $$-2$$만큼 이동시킨다는 사실이 위 관계식에서 곧바로 따라온다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$\sl_2$$-representation $$V$$와 $$\lambda\in\mathbb{C}$$에 대하여, 부분공간

$$V_\lambda=\{v\in V\mid h\cdot v=\lambda v\}$$

을 *weight $$\lambda$$의 weight space*라 부른다. $$V_\lambda\neq 0$$인 $$\lambda$$를 $$V$$의 *weight<sub>무게</sub>*라 하고, $$\dim V_\lambda$$를 그 weight의 *multiplicity<sub>중복도</sub>*라 부른다.

</div>

여기에서 $$V_\lambda$$는 $$h$$의 고윳값 $$\lambda$$에 대한 고유공간이며, $$V$$가 유한차원이라도 일반적으로는 $$h$$가 대각화 가능하다는 보장이 없으므로 $$\bigoplus_\lambda V_\lambda$$가 $$V$$ 전체가 된다고 단정할 수는 없다. 우리는 우선 기약 표현의 경우에 한해 이 분해가 성립함을 보이고, 일반적인 경우의 대각화 가능성은 완전가약성과 함께 [정리 9](#thm9)에서 확립한다.

다음 명제는 $$e,f$$가 weight을 어떻게 옮기는지를 정리한 것으로, $$\sl_2$$ 표현론 전체의 골격을 이룬다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$\sl_2$$-representation $$V$$와 $$\lambda\in\mathbb{C}$$에 대하여

$$e\cdot V_\lambda\subseteq V_{\lambda+2},\qquad f\cdot V_\lambda\subseteq V_{\lambda-2}$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$v\in V_\lambda$$, 곧 $$h\cdot v=\lambda v$$라 하자. 관계식 $$[h,e]=2e$$에서 $$h\cdot(e\cdot v)=e\cdot(h\cdot v)+[h,e]\cdot v=e\cdot(\lambda v)+2e\cdot v=(\lambda+2)(e\cdot v)$$이므로 $$e\cdot v\in V_{\lambda+2}$$이다. 마찬가지로 $$[h,f]=-2f$$에서 $$h\cdot(f\cdot v)=f\cdot(\lambda v)-2f\cdot v=(\lambda-2)(f\cdot v)$$이므로 $$f\cdot v\in V_{\lambda-2}$$이다.

</details>

이러한 이유로 $$e$$를 *raising operator*, $$f$$를 *lowering operator*라 부른다. ([§근계](/ko/math/lie_theory/root_systems#예시-sl2mathbbc)) 두 연산자는 weight space들을 격자 $$\{\lambda,\lambda\pm2,\lambda\pm4,\dots\}$$를 따라 이어 붙인 *weight string<sub>무게 사슬</sub>*을 따라 작용한다.

## 기약 표현의 분류

이제 기약 표현을 분석한다. 핵심은 유한차원성에서 비롯하는 두 가지 사실이다. 첫째, $$h$$의 고윳값이 적어도 하나는 존재하고, 둘째, weight을 계속 올릴 수는 없으므로 $$e$$에 의해 소멸되는 벡터가 존재한다는 것이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$\sl_2$$-representation $$V$$의 벡터 $$v\neq 0$$이 weight $$\mu$$의 *highest weight vector<sub>최고무게 벡터</sub>*라는 것은

$$h\cdot v=\mu v,\qquad e\cdot v=0$$

이 성립하는 것이다. 이 때 $$\mu$$를 *highest weight<sub>최고무게</sub>*이라 부른다.

</div>

임의의 유한차원 $$V\neq 0$$에는 highest weight vector가 존재한다. $$h$$는 복소공간 위의 연산자이므로 고윳값 $$\lambda$$와 고유벡터 $$w\in V_\lambda$$를 적어도 하나 가지며, [명제 2](#prop2)에 의해 $$w,\,e\cdot w,\,e^2\cdot w,\dots$$은 서로 다른 weight $$\lambda,\lambda+2,\lambda+4,\dots$$의 weight space에 속한다. 서로 다른 고윳값의 고유벡터는 일차독립이고 $$V$$가 유한차원이므로 이 열은 유한 번 안에 $$0$$이 되어야 하며, $$e^k\cdot w\neq 0$$이지만 $$e^{k+1}\cdot w=0$$인 $$k$$를 잡으면 $$e^k\cdot w$$가 highest weight vector이다.

다음 명제는 highest weight vector 하나에서 출발해 $$f$$를 반복 적용하여 얻는 사슬의 작용을 완전히 기술한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$v_0$$이 weight $$\mu$$의 highest weight vector라 하고, $$j\geq 0$$에 대하여 $$v_j=\tfrac{1}{j!}f^j\cdot v_0$$, $$v_{-1}=0$$으로 두자. 그럼 각 $$j\geq 0$$에 대하여

$$h\cdot v_j=(\mu-2j)v_j,\qquad f\cdot v_j=(j+1)v_{j+1},\qquad e\cdot v_j=(\mu-j+1)v_{j-1}$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$v_j$$는 $$f^j\cdot v_0$$의 스칼라배이므로 [명제 2](#prop2)에 의하여 $$v_j\in V_{\mu-2j}$$, 곧 $$h\cdot v_j=(\mu-2j)v_j$$이다. 또 $$f\cdot v_j=f\cdot\tfrac{1}{j!}f^j\cdot v_0=\tfrac{j+1}{(j+1)!}f^{j+1}\cdot v_0=(j+1)v_{j+1}$$이다.

$$e$$에 대한 식은 $$j$$에 대한 귀납법으로 보인다. $$j=0$$인 경우 $$v_{-1}=0$$이고 $$e\cdot v_0=0$$이므로 성립한다. 식이 $$j$$에 대해 성립한다고 가정하면, $$ef=fe+[e,f]=fe+h$$를 사용하여

$$\begin{aligned}
e\cdot v_{j+1}&=e\cdot\tfrac{1}{j+1}f\cdot v_j=\tfrac{1}{j+1}(fe+h)\cdot v_j\\
&=\tfrac{1}{j+1}\bigl(f\cdot((\mu-j+1)v_{j-1})+(\mu-2j)v_j\bigr)\\
&=\tfrac{1}{j+1}\bigl((\mu-j+1)\cdot j\,v_j+(\mu-2j)v_j\bigr)\\
&=\tfrac{1}{j+1}\bigl(j\mu-j^2+j+\mu-2j\bigr)v_j=(\mu-j)v_j
\end{aligned}$$

을 얻는데, 이는 $$j$$를 $$j+1$$로 바꾼 식 $$e\cdot v_{j+1}=(\mu-(j+1)+1)v_j$$와 일치한다. 여기에서 $$f\cdot v_{j-1}=j\,v_j$$를 사용하였다.

</details>

이 사슬은 highest weight $$\mu$$가 음이 아닌 정수일 때에만 유한차원 안에서 일관되게 닫힌다. $$V$$가 유한차원이면 $$v_0,v_1,v_2,\dots$$ 중 $$0$$이 아닌 것은 서로 다른 weight를 가지므로 일차독립이고, 따라서 $$v_{m+1}=0$$이면서 $$v_m\neq 0$$인 최소의 $$m\geq 0$$이 존재한다. 이 $$m$$에 대하여 [명제 4](#prop4)의 $$e$$-식을 $$j=m+1$$에서 적용하면

$$0=e\cdot v_{m+1}=(\mu-m)v_m$$

이고 $$v_m\neq 0$$이므로 $$\mu=m$$이다. 곧 highest weight은 항상 음이 아닌 정수 $$m$$이며, $$v_0,\dots,v_m$$이 span하는 부분공간은 $$h,e,f$$ 모두의 작용에 대해 닫혀 있어 $$V$$의 subrepresentation을 이룬다. 이 관찰이 다음 분류로 이어진다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 정수 $$n\geq 0$$에 대하여, $$(n+1)$$-차원 벡터공간 $$V(n)=\bigoplus_{j=0}^{n}\mathbb{C}v_j$$ 위에

$$h\cdot v_j=(n-2j)v_j,\qquad f\cdot v_j=(j+1)v_{j+1},\qquad e\cdot v_j=(n-j+1)v_{j-1}$$

($$v_{-1}=v_{n+1}=0$$)으로 정의되는 $$\sl_2$$-representation을 정의한다. 이를 highest weight $$n$$의 *irreducible representation<sub>기약 표현</sub>*이라 부른다.

</div>

위 작용이 실제로 $$\sl_2$$의 representation을 정의함은 세 관계식 $$[h,e]=2e$$, $$[h,f]=-2f$$, $$[e,f]=h$$가 각 $$v_j$$ 위에서 성립함을 확인하면 된다. 가령 $$[e,f]=h$$의 경우 $$j$$에 대하여 $$ef\cdot v_j-fe\cdot v_j$$를 계산하면

$$ef\cdot v_j=(j+1)\,e\cdot v_{j+1}=(j+1)(n-j)v_j,\qquad fe\cdot v_j=(n-j+1)\,f\cdot v_{j-1}=(n-j+1)j\,v_j$$

이고 그 차는 $$\bigl((j+1)(n-j)-j(n-j+1)\bigr)v_j=(n-2j)v_j=h\cdot v_j$$이다. 나머지 두 관계식도 같은 방식으로 확인된다. $$V(n)$$의 weight들은 $$n,n-2,\dots,-n$$이며 각각 multiplicity $$1$$을 갖는다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 각 정수 $$n\geq 0$$에 대하여 $$V(n)$$은 기약이다. 또한 임의의 유한차원 기약 $$\sl_2$$-representation은 어떤 $$n\geq 0$$에 대한 $$V(n)$$과 isomorphic하며, $$V(m)\cong V(n)$$이면 $$m=n$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$V(n)$$이 기약임을 보인다. $$W\subseteq V(n)$$이 $$0$$이 아닌 subrepresentation이라 하자. $$W$$는 $$h$$의 작용에 대해 닫혀 있고 $$h$$가 $$V(n)$$ 위에서 서로 다른 고윳값 $$n-2j$$들로 대각화되므로, $$W$$는 그 weight space들의 직합, 곧 어떤 첨자 집합 $$J\subseteq\{0,\dots,n\}$$에 대해 $$\bigoplus_{j\in J}\mathbb{C}v_j$$의 꼴이다. $$J\neq\varnothing$$이므로 $$v_j\in W$$인 $$j$$가 있고, $$e\cdot v_j=(n-j+1)v_{j-1}$$에서 계수 $$n-j+1$$은 $$1\leq j\leq n$$에 대해 $$0$$이 아니므로 $$e$$를 반복 적용하면 $$v_0\in W$$이다. 다시 $$f\cdot v_j=(j+1)v_{j+1}$$의 계수가 모두 $$0$$이 아니므로 $$f$$를 반복 적용하면 모든 $$v_0,\dots,v_n\in W$$, 곧 $$W=V(n)$$이다.

다음으로 임의의 유한차원 기약 표현 $$V$$를 생각하자. 위에서 보았듯 $$V$$에는 highest weight vector $$v_0$$이 존재하고 그 highest weight은 정수 $$m\geq 0$$이며, $$v_0,\dots,v_m$$이 span하는 부분공간 $$V'$$은 [명제 4](#prop4)에 의해 $$h,e,f$$의 작용에 대해 닫힌 $$V$$의 $$0$$이 아닌 subrepresentation이다. $$V$$가 기약이므로 $$V'=V$$이고, 따라서 $$v_0,\dots,v_m$$은 $$V$$의 기저이며 그 위의 작용은 [정의 5](#def5)의 작용과 정확히 일치한다. 곧 $$V\cong V(m)$$이다.

끝으로 $$V(m)\cong V(n)$$이면 두 표현의 차원이 같아야 하므로 $$m+1=n+1$$, 곧 $$m=n$$이다.

</details>

[명제 6](#prop6)에 의하여 유한차원 기약 $$\sl_2$$-representation은 그 차원, 동등하게는 highest weight에 의해 완전히 분류된다. $$V(0)$$은 자명한 $$1$$차원 표현이고, $$V(1)$$은 $$\sl_2$$가 정의된 standard representation $$\mathbb{C}^2$$이며, $$V(2)$$는 $$3$$차원 adjoint representation $$\sl_2$$ 자신과 동형이다.

## 완전가약성

기약 표현의 분류는 임의의 표현을 기약 표현들로 분해할 수 있을 때에 비로소 완결된 그림을 준다. $$\SL(2;\mathbb{C})$$는 compact가 아니므로 invariant inner product를 적분으로 평균내는 unitarian trick을 직접 쓸 수 없고, 따라서 완전가약성은 별도의 논증을 요구한다. 우리는 ([§보편 포락 대수, ⁋예시 12](/ko/math/lie_theory/universal_enveloping_algebra#ex12))에서 정의된 Casimir element를 사용한다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$\sl_2$$-representation $$V$$ 위에서, ([§보편 포락 대수, ⁋예시 12](/ko/math/lie_theory/universal_enveloping_algebra#ex12))의 Casimir element $$\Omega=ef+fe+\tfrac{1}{2}h^2$$가 정의하는 연산자

$$C=e\circ f+f\circ e+\tfrac{1}{2}h\circ h:V\rightarrow V$$

을 $$V$$ 위의 *Casimir operator*라 부른다.

</div>

$$\Omega$$가 $$U(\sl_2)$$의 중심에 속하므로 ([§보편 포락 대수, ⁋예시 12](/ko/math/lie_theory/universal_enveloping_algebra#ex12)), $$C$$는 $$h,e,f$$의 작용 모두와 가환이다. 곧 $$C$$는 $$\sl_2$$-equivariant한 자기준동형이며, Schur의 보조정리의 정신에 따라 기약 표현 위에서는 스칼라로 작용한다. 실제로 $$V(n)$$의 highest weight vector $$v_0$$ 위에서 $$e\cdot v_0=0$$을 사용하면

$$C\cdot v_0=ef\cdot v_0+fe\cdot v_0+\tfrac{1}{2}h^2\cdot v_0=(fe+h)\cdot v_0+0+\tfrac{1}{2}n^2v_0=n\,v_0+\tfrac{1}{2}n^2v_0=\tfrac{1}{2}n(n+2)v_0$$

이므로, $$C$$는 $$V(n)$$ 위에서 스칼라 $$\tfrac{1}{2}n(n+2)$$로 작용한다. 여기에서 $$ef\cdot v_0=(fe+[e,f])\cdot v_0=(fe+h)\cdot v_0$$이고 $$fe\cdot v_0=0$$, $$h\cdot v_0=nv_0$$을 사용하였다. 이 스칼라는 $$n\geq 0$$에 대해 서로 다른 값을 가지므로 $$C$$의 고윳값은 표현을 구별한다.

완전가약성 증명의 핵심은 표현이 짧은 완전열로 쪼개질 때, 그 완전열이 항상 분리됨을 보이는 것이다. 다음 보조정리가 그 출발점이다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> $$0\to W\to V\to\mathbb{C}\to 0$$이 $$\sl_2$$-representation들의 짧은 완전열이고, 여기에서 $$\mathbb{C}=V(0)$$은 자명한 표현이라 하자. 그럼 이 완전열은 분리된다. 곧 $$V\cong W\oplus\mathbb{C}$$인 $$\sl_2$$-불변 분해가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim W$$에 대한 귀납법으로 보인다. $$W$$가 $$0$$이 아닌 진부분 subrepresentation $$W'$$을 가지면, 몫 $$V/W'$$은 $$0\to W/W'\to V/W'\to\mathbb{C}\to 0$$을 이루고 $$\dim(W/W')<\dim W$$이므로 귀납 가정에 의해 분리되어, $$V/W'$$ 안에 $$\mathbb{C}$$로 사상되는 $$1$$차원 subrepresentation $$\widetilde U/W'$$이 있다. 이제 $$0\to W'\to\widetilde U\to\mathbb{C}\to 0$$은 $$\dim W'<\dim W$$이므로 다시 귀납 가정으로 분리되어, $$\widetilde U$$ 안에 $$\mathbb{C}$$로 사상되는 $$1$$차원 subrepresentation $$L$$이 있다. $$L$$은 $$V\to\mathbb{C}$$로 동형으로 사상되므로 $$V=W\oplus L$$이다.

따라서 $$W$$가 기약인 경우만 보이면 된다. $$W=V(0)$$이 자명한 표현이면 $$V$$는 $$2$$차원이고 $$\sl_2$$가 $$V$$ 위에서 nilpotent하게만 작용하므로 ($$h,e,f$$의 모든 commutator가 자명한 $$1$$차원 몫과 부분 위에서 $$0$$이 되어 작용 전체가 strictly upper-triangular), $$[e,f]=h$$의 trace를 비교하면 $$h$$의 작용이 $$0$$이고 작용이 분리되어 $$V\cong W\oplus\mathbb{C}$$이다. $$W=V(n)$$이 $$n\geq 1$$인 기약인 경우, $$V$$ 위의 Casimir operator $$C$$를 생각한다. $$C$$는 자명한 표현 $$\mathbb{C}=V(0)$$ 위에서 $$\tfrac{1}{2}\cdot0\cdot2=0$$으로, $$W=V(n)$$ 위에서 $$\tfrac{1}{2}n(n+2)\neq 0$$으로 작용한다. $$C$$가 $$\sl_2$$의 작용과 가환이므로 $$\ker C$$는 $$V$$의 subrepresentation이다. 완전열에서 $$V/W\cong\mathbb{C}$$ 위에서 $$C$$가 $$0$$이므로 $$C(V)\subseteq W$$이고, $$W$$ 위에서 $$C$$가 가역 스칼라이므로 $$C\colon V\to W$$는 전사이며 $$\ker C$$는 $$1$$차원이다. $$\ker C\cap W=0$$이므로 $$V=W\oplus\ker C$$가 $$\sl_2$$-불변 분해이다.

</details>

이제 일반적인 짧은 완전열로 넘어간다. 보조정리 8의 자명한 몫이라는 제약을 $$\Hom$$ 공간을 도입하여 제거한다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Weyl 완전가약성)**</ins> 모든 유한차원 $$\sl_2$$-representation은 기약 표현들의 직합이다. 특히 임의의 유한차원 $$\sl_2$$-representation 위에서 $$h$$는 대각화 가능하고 정수 고윳값만 가지며, $$V=\bigoplus_\lambda V_\lambda$$로 weight 분해된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 임의의 짧은 완전열 $$0\to W\to V\xrightarrow{\pi}U\to 0$$이 분리됨을 보인다. $$\Hom_{\mathbb{C}}(U,V)$$ 위에 $$\sl_2$$-작용을 $$(x\cdot\varphi)(u)=x\cdot\varphi(u)-\varphi(x\cdot u)$$로 주면, $$\sl_2$$-equivariant한 사상 $$U\to V$$들의 공간은 정확히 이 작용의 불변 부분공간 $$\Hom_{\mathbb{C}}(U,V)^{\sl_2}$$이다.

$$\sl_2$$-equivariant한 사상 $$s\colon U\to V$$로 $$\pi\circ s=\id_U$$인 것을 찾으면 $$V=W\oplus s(U)$$가 되어 완전열이 분리된다. 이를 위해 부분공간

$$A=\{\varphi\in\Hom_{\mathbb{C}}(U,V)\mid \pi\circ\varphi=\lambda\cdot\id_U\ \text{for some}\ \lambda\in\mathbb{C}\},\qquad B=\{\varphi\mid \pi\circ\varphi=0\}$$

을 생각하면, $$\pi$$가 전사이므로 $$B\subseteq A$$는 부분공간이고 $$\varphi\mapsto\lambda$$가 $$\sl_2$$-equivariant한 짧은 완전열 $$0\to B\to A\to\mathbb{C}\to 0$$을 준다. ($$\sl_2$$가 $$A,B$$를 보존함은 작용의 정의에서 확인된다. $$\pi$$가 $$\sl_2$$-equivariant이므로 $$\pi\circ(x\cdot\varphi)=x\cdot(\pi\circ\varphi)-(\pi\circ\varphi)\circ x_U$$이고, $$\pi\circ\varphi=\lambda\id_U$$이면 이는 $$\lambda(x_U-x_U)=0$$이 되어 $$x\cdot\varphi\in B$$이다.) [보조정리 8](#lem8)에 의해 이 완전열은 분리되어, $$A$$ 안에 $$\varphi\mapsto\lambda$$로 $$1$$로 사상되는 $$\sl_2$$-불변 원소 $$\varphi_0$$, 곧 $$\pi\circ\varphi_0=\id_U$$인 $$\sl_2$$-equivariant $$\varphi_0$$이 존재한다. 이것이 우리가 찾던 splitting이다.

완전가약성은 $$\dim V$$에 대한 귀납법으로 따라온다. $$V$$가 기약이면 끝이고, 그렇지 않으면 $$0$$이 아닌 진부분 subrepresentation $$W$$를 잡아 $$0\to W\to V\to V/W\to 0$$을 분리하면 $$V\cong W\oplus V/W$$이며, 두 인자는 차원이 더 작으므로 귀납 가정으로 기약 표현들의 직합이다. 따라서 $$V$$도 그러하다. 마지막으로 각 기약 인자 $$V(n)$$ 위에서 $$h$$가 정수 고윳값 $$n,n-2,\dots,-n$$으로 대각화되므로, 그 직합인 $$V$$ 위에서도 $$h$$가 정수 고윳값으로 대각화되어 $$V=\bigoplus_\lambda V_\lambda$$이다.

</details>

[정리 9](#thm9)는 [정의 1](#def1) 이후에 미루어 둔 weight 분해의 일반적 성립을 확립한다. 임의의 유한차원 표현은 weight space들의 직합이고, 각 weight은 정수이며, 표현 전체는 그 안에 나타나는 기약 인자들의 중복도에 의해 결정된다. 어떤 기약 인자가 몇 번 나타나는지는 Casimir operator $$C$$의 고유공간 분해와 각 weight space의 차원으로부터 읽어낼 수 있다.

## Clebsch–Gordan 분해

완전가약성에 의해 두 기약 표현의 텐서곱 $$V(m)\otimes V(n)$$도 기약 표현들의 직합으로 분해된다. 텐서곱 위의 $$\sl_2$$-작용은 Lie algebra의 표준적인 작용, 곧 $$x\cdot(u\otimes w)=(x\cdot u)\otimes w+u\otimes(x\cdot w)$$로 주어진다. 이 작용에서 $$h$$의 고윳값은 두 인자의 weight의 합이므로, 텐서곱의 weight들과 그 multiplicity를 먼저 세는 것으로 분해를 결정할 수 있다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (Clebsch–Gordan)**</ins> 정수 $$m,n\geq 0$$에 대하여 $$\sl_2$$-representation의 동형

$$V(m)\otimes V(n)\cong\bigoplus_{k=0}^{\min(m,n)}V(m+n-2k)$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[정리 9](#thm9)에 의해 좌변은 기약 표현들의 직합 $$\bigoplus_{r}V(r)^{\oplus c_r}$$로 분해되며, 분해를 결정하기 위해서는 각 multiplicity $$c_r$$를 정하면 된다. 이를 weight의 개수를 세어 얻는다.

$$V(m)$$의 weight은 $$m,m-2,\dots,-m$$이고 $$V(n)$$의 weight은 $$n,n-2,\dots,-n$$이며 모두 multiplicity $$1$$이다. 텐서곱 위에서 $$h$$의 작용이 $$h\otimes\id+\id\otimes h$$이므로, weight space의 기저 $$\{v_i\otimes w_j\}$$에 대하여 $$v_i\otimes w_j$$의 weight은 두 인자의 weight의 합이다. 따라서 $$V(m)\otimes V(n)$$의 weight $$\lambda$$의 multiplicity $$d_\lambda$$는 $$a\in\{m,m-2,\dots,-m\}$$과 $$b\in\{n,n-2,\dots,-n\}$$ 중 $$a+b=\lambda$$인 쌍 $$(a,b)$$의 개수와 같다.

이제 $$m\geq n$$이라 두어도 일반성을 잃지 않는다. 가능한 weight들은 $$m+n$$부터 $$-(m+n)$$까지 $$2$$씩 줄어드는 값들이며, multiplicity $$d_\lambda$$는 $$\lambda=m+n$$에서 $$1$$로 시작하여 $$\lambda$$가 $$2$$씩 줄어들 때마다 $$1$$씩 늘다가, $$\lambda=m-n$$에서 최댓값 $$n+1$$에 이른 뒤 $$\lvert\lambda\rvert\leq m-n$$인 구간에서 $$n+1$$로 일정하고, 다시 $$\lambda<-(m-n)$$에서 $$1$$씩 줄어 $$\lambda=-(m+n)$$에서 $$1$$이 된다. 곧 $$d_\lambda$$는 $$\lambda$$에 대해 우함수이며 정점이 평평한 사다리꼴 모양이다.

한편 분해 $$\bigoplus_r V(r)^{\oplus c_r}$$에서 $$V(r)$$은 weight $$r,r-2,\dots,-r$$에 각각 $$1$$씩 기여하므로, weight $$\lambda$$의 총 multiplicity는 $$d_\lambda=\sum_{r\geq\lvert\lambda\rvert,\,r\equiv\lambda\,(2)}c_r$$이다. 이로부터 $$c_r=d_r-d_{r+2}$$를 얻는다. 위에서 구한 $$d_\lambda$$를 대입하면, $$r$$이 $$m+n,m+n-2,\dots,m-n$$ 중 하나일 때 $$d_r-d_{r+2}=1$$이고 그 밖의 $$r$$에 대해서는 $$0$$이다. 따라서

$$V(m)\otimes V(n)\cong\bigoplus_{r\in\{m-n,m-n+2,\dots,m+n\}}V(r)=\bigoplus_{k=0}^{n}V(m+n-2k)$$

이고, $$n=\min(m,n)$$이므로 이는 주장한 분해이다.

</details>

가장 단순한 경우인 $$V(1)\otimes V(1)$$을 보면, $$\min(1,1)=1$$이므로 분해는 $$V(2)\oplus V(0)$$이다. 이는 $$\mathbb{C}^2\otimes\mathbb{C}^2$$가 대칭부분 $$\Sym^2\mathbb{C}^2\cong V(2)$$와 반대칭부분 $$\textstyle\bigwedge^2\mathbb{C}^2\cong V(0)$$으로 갈라지는 친숙한 사실과 일치한다. 더 일반적으로 $$\Sym^n\mathbb{C}^2\cong V(n)$$이 성립하며, 따라서 standard representation $$V(1)=\mathbb{C}^2$$의 대칭곱들이 모든 기약 표현을 실현한다.

이로써 $$\sl_2$$의 유한차원 표현론은 완결된다. 각 차원마다 유일한 기약 표현이 존재하고, 모든 표현이 이들의 직합이며, 텐서곱은 Clebsch–Gordan 공식으로 분해된다. 일반적인 semisimple Lie algebra의 highest weight 이론은 Cartan subalgebra에 대한 weight 분해, dominant integral weight에 의한 기약 표현의 분류, Casimir element를 통한 완전가약성이라는 동일한 세 축 위에 세워지며, 그 각 축은 root별 $$\sl_{2,\alpha}$$의 표현론을 국소모형으로 삼는다.

---

**참고문헌**

**[FH]** W. Fulton and J. Harris, *Representation theory: a first course*, Graduate Texts in Mathematics, Springer, 1991.  
**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Kna]** A. W. Knapp, *Lie groups beyond an introduction*, Progress in Mathematics, Birkhäuser, 2002.  
