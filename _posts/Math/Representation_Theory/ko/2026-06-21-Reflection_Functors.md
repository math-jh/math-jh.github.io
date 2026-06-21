---
title: "반사 함자"
description: "Sink과 source에서의 Bernstein–Gelfand–Ponomarev reflection functor S_k^+, S_k^-를 정의하고, dimension vector에 대한 효과가 root lattice 위의 simple reflection s_k의 작용과 일치함을 증명한다. 두 함자가 simple projective/injective를 제외하고 서로 quasi-inverse임을 보이고, Coxeter 함자와 preprojective·preinjective module을 도입한 뒤 Euler form 및 Gabriel 정리와의 관계를 서술한다."
excerpt: "BGP reflection functor, sink/source 반사, dimension vector와 simple reflection, Coxeter 함자, preprojective module"

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/reflection_functors
sidebar: 
    nav: "representation_theory-ko"

date: 2026-06-21
weight: 13

published: false
---

유한차원 representation을 분류하는 문제는 indecomposable들을 찾는 문제로 환원되며 ([§Krull–Schmidt 정리, ⁋정리 6](/ko/math/representation_theory/krull_schmidt#thm6)), 같은 quiver라도 arrow의 방향을 바꾸면 그 indecomposable들의 모임이 어떻게 달라지는지를 묻는 것은 자연스럽다. *Reflection functor*는 이 물음에 답하는 도구이다. Quiver $$Q$$의 한 vertex $$k$$가 모든 화살표를 받기만 하는 *sink*이거나 내보내기만 하는 *source*일 때, 그 vertex에 인접한 화살표를 모두 뒤집어 새 quiver $$\sigma_k Q$$를 얻고, 동시에 representation을 $$\Rep(Q)$$에서 $$\Rep(\sigma_k Q)$$로 옮기는 함자 $$S_k^+$$ 또는 $$S_k^-$$를 구성한다. 핵심은 이 조작이 dimension vector 위에서 정확히 root lattice의 simple reflection $$s_k$$로 작용한다는 것이며, 이로써 quiver의 representation 이론과 root system의 조합론이 직접 연결된다. 이 연결은 Gabriel 정리, 곧 representation-finite quiver가 정확히 type $$A$$, $$D$$, $$E$$의 Dynkin quiver임을 밝히는 정리의 핵심 도구가 된다.

이 글에서 $$k$$는 field를 가리키고 (vertex를 가리킬 때는 문맥에서 구별된다), $$Q=(Q_0,Q_1,s,t)$$는 oriented cycle을 가지지 않는 유한 quiver이며 ([§Quiver와 경로대수, ⁋정의 1](/ko/math/representation_theory/path_algebras#def1)), representation이라 하면 유한차원 representation을 뜻한다 ([§Quiver와 경로대수, ⁋정의 9](/ko/math/representation_theory/path_algebras#def9)). Root system과 그 위의 reflection, root lattice의 일반론은 [\[리 이론\] §근계](/ko/math/lie_theory/root_systems)를 따른다.

## Sink과 source, 그리고 quiver의 반사

먼저 반사의 대상이 되는 vertex를 정의하고, 그러한 vertex에서 quiver를 어떻게 바꾸는지를 기술한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Quiver $$Q$$의 vertex $$k\in Q_0$$가 *sink<sub>들임 꼭짓점</sub>*이라는 것은 $$s(\alpha)=k$$인 arrow $$\alpha\in Q_1$$이 하나도 없는 것이다. 곧 $$k$$에 인접한 모든 arrow가 $$k$$를 target으로 가진다. 대칭적으로 $$k$$가 *source<sub>냄 꼭짓점</sub>*라는 것은 $$t(\alpha)=k$$인 arrow가 하나도 없는 것이다. 곧 $$k$$에 인접한 모든 arrow가 $$k$$를 source로 가진다.

</div>

Vertex $$k$$가 sink이면 $$k$$로 들어오는 arrow들만 있고, source이면 $$k$$에서 나가는 arrow들만 있다. $$Q$$에 oriented cycle이 없으므로 적어도 하나의 sink와 하나의 source가 항상 존재한다. 임의의 vertex가 sink일 필요는 없으나, 반사 함자는 sink 또는 source인 vertex에서만 정의된다. 이제 그러한 vertex에서 인접한 화살표를 모두 뒤집는 조작을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Quiver $$Q$$와 vertex $$k\in Q_0$$에 대하여, $$k$$에서의 *반사<sub>reflection</sub>* $$\sigma_k Q$$는 같은 vertex 집합 $$Q_0$$를 가지며, arrow 집합은 $$k$$에 인접하지 않은 arrow는 그대로 두고 $$k$$에 인접한 각 arrow $$\alpha$$의 방향만 뒤집어 얻는 quiver이다. 곧 $$\alpha:i\rightarrow k$$는 $$\bar\alpha:k\rightarrow i$$로, $$\alpha:k\rightarrow j$$는 $$\bar\alpha:j\rightarrow k$$로 바꾼다.

</div>

$$k$$가 $$Q$$에서 sink이면, $$k$$에 인접한 arrow는 모두 $$k$$로 들어오므로 반사 후에는 모두 $$k$$에서 나가게 되어 $$k$$는 $$\sigma_k Q$$에서 source가 된다. 대칭적으로 $$k$$가 $$Q$$에서 source이면 $$\sigma_k Q$$에서는 sink가 된다. $$Q$$에 oriented cycle이 없고 $$k$$가 sink 또는 source인 한, 한 vertex의 인접 화살표만 뒤집는 이 조작은 oriented cycle을 만들지 않으므로 $$\sigma_k Q$$도 다시 oriented cycle을 가지지 않는다.

## Sink에서의 reflection functor

이제 sink $$k$$에서 representation을 옮기는 함자를 구성한다. 발상은 다음과 같다. $$k$$가 sink이면 $$k$$로 들어오는 화살표들이 정보를 $$V_k$$로 모으는데, 이 모음 사상의 *kernel*이 $$V_k$$가 채 담아내지 못한 부분을 측정한다. 새 representation에서는 이 kernel을 vertex $$k$$ 위의 공간으로 삼고, 뒤집힌 화살표들이 이 kernel에서 각 $$V_i$$로 자연스럽게 사상되도록 한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$k$$가 $$Q$$의 sink라 하고, $$V=(V_i,V_\alpha)$$를 $$Q$$의 representation이라 하자. $$k$$로 들어오는 arrow들 $$\alpha:i\rightarrow k$$ (이때 $$i=s(\alpha)$$) 로부터 사상

$$V_{\mathrm{in}}=(V_\alpha)_\alpha:\bigoplus_{\alpha:\,i\rightarrow k}V_{s(\alpha)}\longrightarrow V_k$$

을 각 성분에서 $$V_\alpha$$로 주어지는 사상으로 정의한다. *Sink에서의 reflection functor* $$S_k^+:\Rep(Q)\rightarrow\Rep(\sigma_k Q)$$를 다음과 같이 둔다. $$W=S_k^+ V$$는

$$W_k=\ker\Bigl(V_{\mathrm{in}}:\bigoplus_{\alpha:\,i\rightarrow k}V_{s(\alpha)}\rightarrow V_k\Bigr),\qquad W_i=V_i\ (i\neq k)$$

를 vertex 위의 공간으로 가진다. $$k$$에 인접하지 않은 arrow $$\beta$$에는 $$W_\beta=V_\beta$$를 두고, 뒤집힌 각 arrow $$\bar\alpha:k\rightarrow s(\alpha)$$에는 합성

$$W_{\bar\alpha}:W_k\hookrightarrow\bigoplus_{\alpha:\,i\rightarrow k}V_{s(\alpha)}\xrightarrow{\ \mathrm{pr}_\alpha\ }V_{s(\alpha)}$$

곧 $$W_k$$를 직합에 포함한 뒤 $$\alpha$$-성분으로 사영하는 사상을 둔다. Morphism $$f=(f_i):V\rightarrow V'$$에 대해서는 $$i\neq k$$에서 $$(S_k^+ f)_i=f_i$$로 두고, vertex $$k$$에서는 $$f$$가 $$V_{\mathrm{in}}$$과 $$V'_{\mathrm{in}}$$을 교환시키므로 직합 위의 사상 $$\bigoplus_\alpha f_{s(\alpha)}$$가 kernel을 kernel로 보내는 것으로부터 유도되는 제한사상 $$(S_k^+ f)_k:W_k\rightarrow W'_k$$를 둔다.

</div>

$$W_k$$는 $$\bigoplus_\alpha V_{s(\alpha)}$$의 부분공간이고, 뒤집힌 화살표 $$\bar\alpha$$의 작용 $$W_{\bar\alpha}$$는 이 부분공간을 $$\alpha$$-좌표로 읽어 낸 것이다. 따라서 $$S_k^+ V$$는 $$\sigma_k Q$$의 올바른 representation이다. $$\sigma_k Q$$에서 $$k$$는 source이므로, $$k$$에서 나가는 화살표 $$\bar\alpha:k\rightarrow s(\alpha)$$들에 사상을 배정하는 것이 마땅하며 위 정의가 바로 그것이다. Morphism에 대한 정의가 잘 됨은 다음을 보면 된다. $$f:V\rightarrow V'$$가 morphism이면 각 $$\alpha:i\rightarrow k$$에 대하여 $$f_k\circ V_\alpha=V'_\alpha\circ f_{s(\alpha)}$$이므로, 직합 위의 사상 $$F=\bigoplus_\alpha f_{s(\alpha)}$$이 $$V'_{\mathrm{in}}\circ F=f_k\circ V_{\mathrm{in}}$$을 만족한다. 따라서 $$F$$는 $$\ker V_{\mathrm{in}}$$을 $$\ker V'_{\mathrm{in}}$$ 안으로 보내고, 그 제한이 $$(S_k^+ f)_k$$이다.

$$S_k^+$$가 함자임은 kernel로의 제한이 합성과 항등사상을 보존한다는 사실에서 곧바로 따라온다. 다음 예시는 가장 단순한 경우에서 이 함자가 무엇을 하는지를 보여 준다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> 선형 $$A_2$$ quiver $$Q:1\xrightarrow{\ \alpha\ }2$$를 생각하자. Vertex $$2$$는 sink이다. Representation $$V$$는 선형사상 $$V_\alpha:V_1\rightarrow V_2$$ 하나로 주어진다. 이때 $$\sigma_2 Q$$는 $$1\xleftarrow{\ \bar\alpha\ }2$$이고, $$S_2^+ V$$는

$$W_2=\ker(V_\alpha:V_1\rightarrow V_2),\qquad W_1=V_1,\qquad W_{\bar\alpha}:W_2\hookrightarrow V_1$$

로 주어진다. 가령 $$V_\alpha=\id:k\rightarrow k$$인 indecomposable $$V=(k\xrightarrow{\id}k)$$에 대해서는 $$W_2=\ker\id=0$$이므로 $$S_2^+ V=(k\xleftarrow{}0)$$, 곧 vertex $$1$$에만 $$k$$가 놓인 simple representation이다. 한편 simple representation $$V=(k\xrightarrow{0}0)$$, 곧 dimension vector $$(1,0)$$인 것에 대해서는 $$W_2=\ker(0:k\rightarrow 0)=k$$, $$W_1=k$$이고 $$W_{\bar\alpha}:k\xrightarrow{\id}k$$가 되어 $$S_2^+ V=(k\xleftarrow{\id}k)$$이다.

</div>

예시 4의 마지막 경우에서 simple representation $$(1,0)$$이 $$\sigma_2 Q$$의 indecomposable $$(1,1)$$로 옮겨졌다. 이것이 dimension vector 위에서 simple reflection이 일으키는 전형적인 변화이며, 다음 절에서 이를 일반적으로 정식화한다. 한편 source에서의 함자는 위 구성을 완전히 쌍대화하여 얻는다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> $$k$$가 $$Q$$의 source라 하고, $$V$$를 $$Q$$의 representation이라 하자. $$k$$에서 나가는 arrow들 $$\alpha:k\rightarrow j$$ (이때 $$j=t(\alpha)$$) 로부터 사상

$$V_{\mathrm{out}}=(V_\alpha)_\alpha:V_k\longrightarrow\bigoplus_{\alpha:\,k\rightarrow j}V_{t(\alpha)}$$

을 각 성분이 $$V_\alpha$$인 사상으로 정의한다. *Source에서의 reflection functor* $$S_k^-:\Rep(Q)\rightarrow\Rep(\sigma_k Q)$$는 $$W=S_k^- V$$를

$$W_k=\coker\Bigl(V_{\mathrm{out}}:V_k\rightarrow\bigoplus_{\alpha:\,k\rightarrow j}V_{t(\alpha)}\Bigr),\qquad W_i=V_i\ (i\neq k)$$

로 두고, $$k$$에 인접하지 않은 arrow에는 $$V$$의 사상을, 뒤집힌 각 arrow $$\bar\alpha:t(\alpha)\rightarrow k$$에는 합성

$$W_{\bar\alpha}:V_{t(\alpha)}\xrightarrow{\ \iota_\alpha\ }\bigoplus_{\alpha:\,k\rightarrow j}V_{t(\alpha)}\twoheadrightarrow W_k$$

곧 $$\alpha$$-성분으로의 포함과 cokernel로의 사영의 합성을 둔다. Morphism에 대해서는 $$S_k^+$$와 대칭적으로 cokernel로 내려가는 유도사상을 둔다.

</div>

$$\sigma_k Q$$에서 source였던 $$k$$는 sink가 되며, 이번에는 $$k$$로 들어오는 화살표들에 사상을 배정해야 한다. 정의의 $$W_{\bar\alpha}:V_{t(\alpha)}\rightarrow W_k$$가 바로 그 사상이다. $$S_k^+$$가 kernel을 취해 정보를 "되돌려 받았다"면, $$S_k^-$$는 cokernel을 취해 "내보내고 남은" 부분을 vertex $$k$$ 위에 둔다. 두 구성이 서로 쌍대이며, 다음 절에서 이들이 dimension vector 위에서 같은 reflection을 일으키고 서로 거의 역임을 본다.

## Dimension vector와 simple reflection

Quiver $$Q$$의 vertex 집합 $$Q_0$$를 $$\{1,\ldots,n\}$$으로 두면, representation $$V$$의 *dimension vector*

$$\underline\dim V=(\dim_k V_1,\ldots,\dim_k V_n)\in\mathbb{Z}^{n}$$

은 $$V$$가 각 vertex에 얹은 공간의 차원을 기록한다. $$\mathbb{Z}^n$$을 vertex들을 simple root로 가지는 root lattice로 보면, 반사 함자가 dimension vector에 미치는 효과는 정확히 한 simple root에 대한 reflection으로 나타난다. 이를 정확히 적기 위해 $$Q$$의 *Euler form*과 그에 딸린 symmetric form을 도입한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Oriented cycle이 없는 quiver $$Q$$의 *Euler form<sub>오일러 형식</sub>*은 $$\mathbb{Z}^n$$ 위의 bilinear form

$$\langle d,e\rangle=\sum_{i\in Q_0}d_i e_i-\sum_{\alpha\in Q_1}d_{s(\alpha)}e_{t(\alpha)}$$

이다. 그 대칭화 $$(d,e)=\langle d,e\rangle+\langle e,d\rangle$$를 $$Q$$의 *symmetric Euler form*이라 부르고, 이에 딸린 이차형식 $$q(d)=\langle d,d\rangle$$을 $$Q$$의 *Tits form<sub>티츠 형식</sub>*이라 부른다.

</div>

표준 basis vector $$e_k\in\mathbb{Z}^n$$ (vertex $$k$$에 대응) 에 대하여 $$(e_k,e_k)=2$$임을 직접 확인할 수 있다. Loop가 없으므로 $$\langle e_k,e_k\rangle=1$$이고 따라서 $$(e_k,e_k)=2$$이다. 그럼 각 vertex $$k$$에 대하여 root lattice 위의 simple reflection

$$s_k(d)=d-(d,e_k)\,e_k$$

을 정의할 수 있다. 이는 근계의 reflection ([\[리 이론\] §근계, ⁋정의 9](/ko/math/lie_theory/root_systems#def9))과 같은 꼴이며, vertex $$k$$ 좌표만 바꾸는 변환이다. 구체적으로 $$k$$가 sink일 때 $$k$$로 들어오는 arrow의 개수를 $$m$$이라 하면 $$(d,e_k)$$의 계산에서 $$s_k(d)$$의 $$k$$-좌표는 $$\sum_{\alpha:i\rightarrow k}d_{s(\alpha)}-d_k$$로 바뀐다. 다음 명제가 이 변환이 정확히 반사 함자의 효과임을 말한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$k$$가 $$Q$$의 sink이고 $$V$$가 $$Q$$의 indecomposable representation으로서 vertex $$k$$에 얹힌 simple representation $$S_k$$ (곧 dimension vector $$e_k$$인 것) 와 isomorphic하지 않다고 하자. 그럼 사상 $$V_{\mathrm{in}}$$이 전사이고,

$$\underline\dim(S_k^+ V)=s_k(\underline\dim V)$$

가 성립한다. 대칭적으로 $$k$$가 source이고 $$V$$가 simple representation $$S_k$$와 isomorphic하지 않은 indecomposable이면 $$V_{\mathrm{out}}$$이 단사이고 $$\underline\dim(S_k^- V)=s_k(\underline\dim V)$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Sink의 경우를 보이고 source의 경우는 쌍대적으로 따라온다. $$k$$가 sink이므로 $$V$$에서 vertex $$k$$ 위의 공간 $$V_k$$로 들어오는 정보는 사상 $$V_{\mathrm{in}}:\bigoplus_{\alpha:i\rightarrow k}V_{s(\alpha)}\rightarrow V_k$$로 전부 모인다. 먼저 $$V_{\mathrm{in}}$$이 전사임을 보인다. $$U=\im V_{\mathrm{in}}\subseteq V_k$$라 하고, $$V_k$$의 부분공간 $$U$$의 한 보충공간 $$C$$를 택해 $$V_k=U\oplus C$$로 적자. 그럼 vertex $$k$$에만 $$C$$를 얹고 나머지 vertex에는 $$0$$을 얹은 representation $$V'=(C\text{ at }k)$$는 $$V$$의 subrepresentation이다. 실제로 $$k$$가 sink이므로 $$k$$에서 나가는 arrow가 없어 $$C$$가 arrow를 따라 옮겨질 곳이 없고, 따라서 부분공간 조건이 자명하게 성립한다 ([§Quiver와 경로대수, ⁋정의 11](/ko/math/representation_theory/path_algebras#def11)). 더 나아가 $$C$$ 위의 공간은 다른 vertex로부터 들어오는 사상의 image $$U$$와 직합을 이루므로, $$V'$$는 $$V$$의 direct summand이다. 곧 $$V\cong V''\oplus V'$$이고 $$V'$$는 vertex $$k$$ 위의 simple representation들의 직합, 곧 $$S_k^{\oplus\dim C}$$이다. $$V$$가 indecomposable이고 $$S_k$$와 isomorphic하지 않다고 가정하였으므로 $$V'=0$$, 곧 $$C=0$$이어야 한다. 따라서 $$U=V_k$$이고 $$V_{\mathrm{in}}$$은 전사이다.

이제 차원을 센다. $$V_{\mathrm{in}}$$이 전사이므로 짧은 완전열

$$0\longrightarrow W_k\longrightarrow\bigoplus_{\alpha:\,i\rightarrow k}V_{s(\alpha)}\xrightarrow{\ V_{\mathrm{in}}\ }V_k\longrightarrow 0$$

을 얻고, $$W_k=\ker V_{\mathrm{in}}$$이므로 rank–nullity에 의하여

$$\dim_k W_k=\sum_{\alpha:\,i\rightarrow k}\dim_k V_{s(\alpha)}-\dim_k V_k$$

이다. $$i\neq k$$에서는 $$(S_k^+ V)_i=V_i$$이므로 dimension vector는 $$k$$-좌표에서만 달라지며, 그 새 $$k$$-좌표가 위 식이다. 한편 $$s_k(\underline\dim V)$$도 $$k$$-좌표에서만 달라지고, $$(\underline\dim V,e_k)$$가 $$k$$에 인접한 arrow들로부터 $$\sum_{\alpha:i\rightarrow k}\dim_k V_{s(\alpha)}$$를, $$(e_k,e_k)=2$$로부터 $$2\dim_k V_k$$를 받아

$$s_k(\underline\dim V)_k=\dim_k V_k-\Bigl(2\dim_k V_k-\sum_{\alpha:\,i\rightarrow k}\dim_k V_{s(\alpha)}\Bigr)$$

이 되는데, 정리하면 $$\sum_{\alpha:i\rightarrow k}\dim_k V_{s(\alpha)}-\dim_k V_k$$로 위에서 구한 $$\dim_k W_k$$와 같다. 따라서 $$\underline\dim(S_k^+ V)=s_k(\underline\dim V)$$이다.

</details>

명제 7에서 simple representation $$S_k$$를 제외해야 하는 이유는 분명하다. $$V=S_k$$이면 $$V_{\mathrm{in}}$$은 $$0\rightarrow V_k$$ (들어오는 화살표 쪽 공간이 모두 $$0$$) 이므로 전사가 아니고, 실제로 $$S_k^+ S_k=0$$이 되어 dimension vector가 보존되지 않는다. 반면 $$s_k(e_k)=-e_k$$는 음의 좌표를 가져 어떤 representation의 dimension vector도 될 수 없다. 이 한 예외를 제외하면 $$S_k^+$$는 indecomposable을 indecomposable로 보내며 dimension vector 위에서 정확히 $$s_k$$로 작용한다.

## 두 함자의 quasi-inverse 관계

Sink에서의 $$S_k^+$$와 source에서의 $$S_k^-$$는 서로 반대 방향의 quiver 사이를 오가므로 합성할 수 있다. $$k$$가 $$Q$$의 sink이면 $$S_k^+:\Rep(Q)\rightarrow\Rep(\sigma_k Q)$$이고, $$\sigma_k Q$$에서 $$k$$는 source이므로 $$S_k^-:\Rep(\sigma_k Q)\rightarrow\Rep(\sigma_k\sigma_k Q)=\Rep(Q)$$이다. 두 함자를 잇따라 적용하면 $$S_k$$를 제외한 곳에서 원래 representation을 회복한다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> $$k$$가 $$Q$$의 sink라 하자. $$V$$가 simple representation $$S_k$$를 direct summand로 가지지 않는 $$Q$$의 representation이면

$$S_k^- S_k^+ V\cong V$$

가 자연스럽게 성립한다. 대칭적으로 $$k$$가 source이고 $$V$$가 $$S_k$$를 direct summand로 가지지 않으면 $$S_k^+ S_k^- V\cong V$$이다. 특히 $$S_k^+$$와 $$S_k^-$$는 simple representation $$S_k$$만 제외한 indecomposable들의 isomorphism class 위에서 서로 역인 전단사를 주며, 두 함자는 이들 사이의 quasi-inverse equivalence로 제한된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$k$$가 sink인 경우를 보인다. $$V$$가 $$S_k$$를 direct summand로 가지지 않으므로, 명제 7의 증명에서 본 것과 같이 사상 $$V_{\mathrm{in}}:\bigoplus_{\alpha:i\rightarrow k}V_{s(\alpha)}\rightarrow V_k$$이 전사이다. (그 논증은 $$V$$가 indecomposable이라는 것보다 약한, $$S_k$$를 summand로 가지지 않는다는 조건만 사용한다. $$\im V_{\mathrm{in}}$$의 보충공간이 vertex $$k$$ 위의 $$S_k$$-summand를 주기 때문이다.) 따라서

$$0\longrightarrow W_k\xrightarrow{\ j\ }\bigoplus_{\alpha:\,i\rightarrow k}V_{s(\alpha)}\xrightarrow{\ V_{\mathrm{in}}\ }V_k\longrightarrow 0$$

은 짧은 완전열이며, 여기서 $$W=S_k^+ V$$이고 $$j$$는 포함이다. 이제 $$\sigma_k Q$$에서 $$k$$는 source이고 $$W$$에서 $$k$$로부터 나가는 사상은 $$W_{\bar\alpha}=\mathrm{pr}_\alpha\circ j:W_k\rightarrow V_{s(\alpha)}$$이다. 이들을 모은 사상이 정확히 $$W_{\mathrm{out}}=j:W_k\rightarrow\bigoplus_\alpha V_{s(\alpha)}$$인데, $$j$$가 단사이므로 그 cokernel은

$$(S_k^- W)_k=\coker(W_{\mathrm{out}})=\coker(j)\cong V_k$$

이고, 이 isomorphism은 $$V_{\mathrm{in}}$$이 유도하는 것이다. 곧 짧은 완전열의 cokernel이 $$V_k$$와 표준적으로 동일시된다. 나머지 vertex에서는 $$S_k^+$$도 $$S_k^-$$도 공간을 바꾸지 않으므로 $$(S_k^- S_k^+ V)_i=V_i$$이다. 마지막으로 arrow 위의 사상이 일치함을 본다. 원래 $$k$$로 들어오던 arrow $$\alpha:i\rightarrow k$$에 대하여, $$S_k^- W$$에서 그에 대응하는 (다시 뒤집혀 원래 방향이 된) arrow의 사상은 $$V_{s(\alpha)}\xrightarrow{\iota_\alpha}\bigoplus_\beta V_{s(\beta)}\twoheadrightarrow\coker(j)\cong V_k$$인데, $$\coker(j)\cong V_k$$가 $$V_{\mathrm{in}}$$으로 주어졌으므로 이 합성은 $$V_{\mathrm{in}}\circ\iota_\alpha=V_\alpha$$와 같다. 따라서 $$k$$에 인접하지 않은 arrow의 사상이 보존됨과 합쳐, representation의 동형 $$S_k^- S_k^+ V\cong V$$를 얻고, 이 동형은 위 구성에 자연스럽다.

Source의 경우는 $$k$$가 sink일 때의 논증을 완전히 쌍대화하여, $$V_{\mathrm{out}}$$의 단사성으로부터 $$S_k^+ S_k^- V\cong V$$를 얻는다. 끝으로 두 함자가 $$S_k$$를 제외한 indecomposable 위에서 서로 역임은 다음과 같다. $$V$$가 $$S_k$$가 아닌 indecomposable이면 명제 7에 의하여 $$S_k^+ V$$의 dimension vector가 음이 아니고 $$0$$이 아니므로 $$S_k^+ V\neq 0$$이며, 위에서 $$S_k^- S_k^+ V\cong V$$이므로 $$S_k^+ V$$ 또한 indecomposable이고 $$S_k$$ (이번에는 $$\sigma_k Q$$의 simple) 가 아니다. 따라서 두 대응이 서로 역인 전단사를 이룬다.

</details>

명제 8은 반사 함자가 거의 모든 indecomposable을 가역적으로 옮긴다는 것을 말한다. 유일하게 잃는 것은 vertex $$k$$ 위의 simple $$S_k$$ 하나뿐이며, $$S_k^+ S_k=0$$이다. 따라서 한 vertex에서의 반사는 indecomposable의 분류를 $$S_k$$ 하나만큼 어긋나게 옮긴다. 이 한 칸의 어긋남을 모든 vertex에 걸쳐 한 바퀴 누적시키면, 다음 절의 Coxeter 함자가 얻어진다.

## Coxeter 함자와 preprojective module

여러 vertex에서 차례로 sink reflection을 적용하되, 매 단계에서 해당 vertex가 그 순간의 quiver에서 sink가 되도록 순서를 잡으면, 결국 모든 arrow가 한 바퀴 뒤집혀 원래 quiver로 돌아온다. 이러한 순서를 admissible이라 부른다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Oriented cycle이 없는 quiver $$Q$$의 vertex들을 모두 한 번씩 나열한 순서 $$(k_1,k_2,\ldots,k_n)$$이 *admissible sink sequence<sub>허용 sink 나열</sub>*라는 것은, $$k_1$$이 $$Q$$의 sink이고, 각 $$2\leq r\leq n$$에 대하여 $$k_r$$가 $$\sigma_{k_{r-1}}\cdots\sigma_{k_1}Q$$의 sink인 것이다. 이러한 나열에 대하여 *Coxeter 함자*를

$$C^+=S_{k_n}^+\cdots S_{k_2}^+ S_{k_1}^+:\Rep(Q)\longrightarrow\Rep(Q)$$

로 정의한다. 대칭적으로 admissible source sequence를 따라 $$S^-$$들을 합성하여 $$C^-:\Rep(Q)\rightarrow\Rep(Q)$$를 정의한다.

</div>

각 vertex를 정확히 한 번씩 sink로 만들어 모든 인접 화살표를 뒤집으므로, 모든 vertex를 거치고 나면 $$\sigma_{k_n}\cdots\sigma_{k_1}Q=Q$$가 되어 $$C^+$$는 $$\Rep(Q)$$를 자기 자신으로 보낸다. Admissible sink sequence는 $$Q$$에 oriented cycle이 없으므로 항상 존재한다. 매 단계에서 sink를 하나 골라 제거하는 방식으로 위상정렬을 하면 되기 때문이다. 서로 다른 admissible sink sequence는 다른 함자를 줄 수 있으나, dimension vector 위에서는 모두 같은 변환, 곧 Weyl group ([\[리 이론\] §근계, ⁋정의 17](/ko/math/lie_theory/root_systems#def17))의 *Coxeter element* $$c=s_{k_n}\cdots s_{k_1}$$로 작용한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $$(k_1,\ldots,k_n)$$이 admissible sink sequence이고 $$V$$가 $$Q$$의 indecomposable representation이라 하자. $$C^+ V\neq 0$$이면

$$\underline\dim(C^+ V)=c\,(\underline\dim V),\qquad c=s_{k_n}\cdots s_{k_1}$$

이며 $$C^+ V$$는 다시 indecomposable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$C^+=S_{k_n}^+\cdots S_{k_1}^+$$의 각 단계를 차례로 살핀다. $$r$$번째 단계에서 $$k_r$$는 그 시점의 quiver $$Q^{(r-1)}=\sigma_{k_{r-1}}\cdots\sigma_{k_1}Q$$의 sink이고, 이전 단계까지의 결과 $$V^{(r-1)}=S_{k_{r-1}}^+\cdots S_{k_1}^+ V$$가 그 위의 representation이다. $$C^+ V\neq 0$$이라는 가정은 모든 중간 단계 $$V^{(r)}$$이 $$0$$이 아님을 함의한다. 어느 한 단계에서 $$V^{(r)}=0$$이 되면 이후 모든 합성이 $$0$$이 되기 때문이다. 따라서 각 단계에서 $$V^{(r-1)}$$은 nonzero이고, 명제 8에 의하여 $$S_{k_r}^+$$가 indecomposable을 보존하는 한 $$V^{(r-1)}$$은 해당 quiver의 simple $$S_{k_r}$$이 아니어야 한다.

$$V^{(r-1)}$$이 indecomposable이고 $$S_{k_r}$$이 아니라고 하자. 그럼 명제 7에 의하여

$$\underline\dim V^{(r)}=\underline\dim(S_{k_r}^+ V^{(r-1)})=s_{k_r}(\underline\dim V^{(r-1)})$$

이고, 명제 8에 의하여 $$S_{k_r}^+ V^{(r-1)}=V^{(r)}$$ 또한 indecomposable이다. 만일 $$V^{(r-1)}$$이 어떤 단계에서 simple $$S_{k_r}$$과 같다면 $$V^{(r)}=S_{k_r}^+ V^{(r-1)}=0$$이 되어 $$C^+ V=0$$이라는 결론에 이르므로, $$C^+ V\neq 0$$이라는 가정 아래에서는 그런 단계가 없다. 따라서 모든 단계에서 dimension vector에 $$s_{k_r}$$가 차례로 작용하고 indecomposability가 보존되어,

$$\underline\dim(C^+ V)=s_{k_n}\cdots s_{k_1}(\underline\dim V)=c\,(\underline\dim V)$$

이며 $$C^+ V$$는 indecomposable이다.

</details>

Coxeter 함자를 거듭 적용하면 어떤 indecomposable은 유한 번 만에 $$0$$으로 사라지고, 어떤 것은 결코 사라지지 않는다. 사라지는 쪽이 projective의 궤도에서 나오는 것들이며, 이로부터 preprojective와 preinjective module을 정의한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> $$Q$$의 indecomposable representation $$V$$가 *preprojective<sub>전사영적</sub>*라는 것은 어떤 $$m\geq 0$$에 대하여 $$(C^+)^m V=0$$인 것이다. 대칭적으로 $$V$$가 *preinjective<sub>전입사적</sub>*라는 것은 어떤 $$m\geq 0$$에 대하여 $$(C^-)^m V=0$$인 것이다.

</div>

Preprojective indecomposable은 $$C^+$$를 거듭하면 결국 $$0$$이 되므로, $$C^-$$로 거슬러 올라가면 모두 어떤 indecomposable projective $$P$$로부터 $$(C^-)^m P$$의 꼴로 얻어진다. 곧 preprojective module들은 indecomposable projective들의 $$C^-$$-궤도를 모두 합한 것이며, 대칭적으로 preinjective module들은 indecomposable injective들의 $$C^+$$-궤도를 모두 합한 것이다. 이 궤도들은 명제 10에 의하여 dimension vector 위에서 Coxeter element $$c$$의 거듭제곱에 의한 궤도로 나타나므로, root system의 조합론으로 완전히 통제된다. Dynkin quiver의 경우에는 모든 indecomposable이 preprojective이며, 따라서 다음 절의 Gabriel 정리가 성립한다.

## Euler form과 Gabriel 정리

명제 7과 명제 10은 indecomposable의 dimension vector가 Weyl group의 작용 아래에서 어떻게 움직이는지를 말해 준다. 이를 Euler form 및 Tits form과 결합하면, indecomposable의 dimension vector가 정확히 root임을 알 수 있다. 핵심 관찰은 반사 함자가 dimension vector 위에서 reflection으로 작용하고 ([정의 6](#def6)의 symmetric form에 대한 simple reflection), reflection이 Tits form을 보존한다는 것이다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> Reflection $$s_k$$는 Tits form을 보존한다. 곧 임의의 $$d\in\mathbb{Z}^n$$에 대하여 $$q(s_k(d))=q(d)$$이다. 특히 admissible sink sequence가 주는 Coxeter element $$c$$도 $$q$$를 보존한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Tits form $$q(d)=\langle d,d\rangle$$은 대칭화 $$(d,e)=\langle d,e\rangle+\langle e,d\rangle$$에 대하여 $$q(d)=\tfrac12(d,d)$$를 만족하므로, $$q$$를 보존하는 것과 symmetric form $$(-,-)$$을 보존하는 것이 동치이다. Reflection $$s_k(d)=d-(d,e_k)e_k$$는 $$(e_k,e_k)=2$$인 vector $$e_k$$에 대한 reflection이므로, 임의의 $$d$$에 대하여

$$(s_k(d),s_k(d))=(d,d)-2(d,e_k)(e_k,d)+(d,e_k)^2(e_k,e_k)=(d,d)-2(d,e_k)^2+2(d,e_k)^2=(d,d)$$

이다. 따라서 $$s_k$$가 $$(-,-)$$을, 곧 $$q$$를 보존한다. Coxeter element $$c=s_{k_n}\cdots s_{k_1}$$은 이러한 reflection들의 합성이므로 역시 $$q$$를 보존한다.

</details>

명제 12에 의하여 dimension vector $$\underline\dim V$$가 반사를 통해 움직여도 그 Tits form 값 $$q(\underline\dim V)$$는 변하지 않는다. Indecomposable representation의 dimension vector는 항상 $$q(d)\leq 1$$을 만족하며, 특히 $$Q$$가 Dynkin quiver, 곧 그 underlying graph가 type $$A$$, $$D$$, $$E$$인 경우 Tits form은 positive definite이어서 $$q(d)=1$$인 $$d$$들이 정확히 root system의 root에 대응한다. 이로부터 다음의 결과가 나오며, 그 완전한 증명은 반사 함자를 핵심 도구로 사용한다.

<div class="proposition" markdown="1">

<ins id="thm13">**정리 13**</ins> (Gabriel) $$Q$$를 oriented cycle이 없는 연결 quiver라 하자. $$Q$$가 *representation-finite*, 곧 유한개의 indecomposable representation만을 (isomorphism을 무시하여) 가지는 것은 $$Q$$의 underlying graph가 type $$A_n$$, $$D_n$$, $$E_6$$, $$E_7$$, $$E_8$$의 Dynkin diagram인 것과 동치이다. 이 경우 대응

$$V\longmapsto\underline\dim V$$

은 indecomposable representation의 isomorphism class들과 Tits form의 positive root들 사이의 전단사이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

완전한 증명은 길어 여기서 재구성하지 않으며, 그 골격만 적고 [ASS, Chapter VII]과 [Br, §5]의 논증을 따른다. 반사 함자가 증명의 두 방향 모두에서 중심 역할을 한다.

$$Q$$가 Dynkin이면 Tits form은 positive definite이므로 ([정의 6](#def6)) $$q(d)=1$$인 정수 vector는 유한개뿐이고, 이들이 type $$A$$, $$D$$, $$E$$ root system의 양의 root들에 대응한다. Indecomposable의 dimension vector가 항상 root임은 다음과 같이 본다. Admissible sink sequence를 잡아 Coxeter 함자 $$C^+$$를 만들면, 임의의 indecomposable $$V$$에 대하여 $$(C^+)^m V=0$$이 되는 $$m$$이 존재하여 $$V$$는 preprojective이다 ([정의 11](#def11)). 곧 $$V$$는 어떤 indecomposable projective $$P$$에 대하여 $$(C^-)^j P$$의 꼴이며, projective의 dimension vector에 명제 10의 reflection들을 적용하여 얻어진다. Projective의 dimension vector는 root이고 reflection이 root를 root로, Tits form을 보존하므로 ([명제 12](#prop12)) $$V$$의 dimension vector도 root이다. 이로써 $$V\mapsto\underline\dim V$$가 indecomposable에서 양의 root로 가는 사상임을 안다. 이 사상이 단사이고 전사임은, 각 양의 root에 대하여 그것을 dimension vector로 가지는 indecomposable이 정확히 하나 존재함을 반사 함자로 추적하여 보인다. Root는 simple reflection들로 simple root $$e_k$$까지 줄일 수 있고 ([\[리 이론\] §근계](/ko/math/lie_theory/root_systems)), $$e_k$$는 simple representation $$S_k$$의 dimension vector이므로, 이 reflection의 자취를 반사 함자로 들어 올리면 해당 indecomposable이 유일하게 복원된다. Root가 유한개이므로 indecomposable도 유한개이다.

역으로 $$Q$$가 Dynkin이 아니면 그 underlying graph는 extended Dynkin diagram을 포함하고, 그 위에서 Tits form은 positive definite가 아니어서 $$q(d)\leq 1$$을 만족하는 dimension vector가 무한히 많은 indecomposable을 허용한다. 따라서 $$Q$$는 representation-finite가 아니다.

</details>

정리 13은 반사 함자가 어디에 쓰이는지를 가장 선명하게 보여 준다. 한 vertex에서의 반사가 dimension vector 위에서 simple reflection으로 작용한다는 명제 7의 등식이, indecomposable의 분류를 root system의 조합론으로 옮겨 주는 다리가 된다. Indecomposable마다 하나의 양의 root가 대응하고, 그 root는 Weyl group의 작용으로 simple root까지 환원되며, 그 환원의 매 단계가 곧 하나의 반사 함자이다. 이렇게 quiver의 representation 이론과 finite root system의 분류가 정확히 포개진다는 것이 Gabriel 정리의 내용이다.

---

**참고문헌**

**[BGP]** I. N. Bernstein, I. M. Gelfand, and V. A. Ponomarev, *Coxeter functors and Gabriel's theorem*, Russian Mathematical Surveys **28** (1973), 17–32.

**[ASS]** I. Assem, D. Simson, and A. Skowroński, *Elements of the representation theory of associative algebras, Volume 1: Techniques of representation theory*, Cambridge University Press, 2006.

**[ARS]** M. Auslander, I. Reiten, and S. O. Smalø, *Representation theory of Artin algebras*, Cambridge University Press, 1995.

**[Br]** M. Brion, *Representations of quivers*, in *Geometric methods in representation theory I*, Société Mathématique de France, 2012.

**[DW]** H. Derksen and J. Weyman, *An introduction to quiver representations*, American Mathematical Society, 2017.
