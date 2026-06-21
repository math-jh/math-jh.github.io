---
title: "Gabriel 정리"
description: "연결 quiver Q가 representation-finite인 것이 그 underlying graph가 ADE Dynkin diagram인 것과 동치이고, 그때 V↦dim V가 indecomposable의 동형류와 연관 root system의 positive root 사이의 전단사임을 보이는 Gabriel 정리를 다룬다. Euler form과 그 대칭화로 얻는 Tits 이차형식 q를 도입하고 q가 positive definite인 것이 ADE와 동치임을 root system의 분류로 환원하며, indecomposable의 dimension vector가 q(d)=1인 real root임을 reflection functor와 Coxeter functor로 추적하는 증명 골격을 서술한 뒤 선형 A_3 quiver에서 6개의 positive root와 6개의 indecomposable의 대응을 확인한다."
excerpt: "Gabriel 정리, finite representation type, ADE Dynkin quiver, Tits 이차형식, dimension vector와 positive root의 전단사, A_3 예시"

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/gabriel_theorem
sidebar: 
    nav: "representation_theory-ko"

date: 2026-06-21
weight: 14

published: false
---

유한차원 representation을 이해하는 문제는 indecomposable들을 분류하는 문제로 환원되며 ([§Krull–Schmidt 정리, ⁋정리 6](/ko/math/representation_theory/krull_schmidt#thm6)), 따라서 가장 먼저 물어야 할 것은 주어진 quiver가 과연 유한개의 indecomposable만을 가지는가이다. *Gabriel 정리*는 이 물음에 완벽하게 답한다. 연결 quiver $$Q$$가 isomorphism을 무시하여 유한개의 indecomposable representation만을 가지는 것은, $$Q$$의 화살표 방향을 잊은 underlying graph가 정확히 type $$A_n$$, $$D_n$$, $$E_6$$, $$E_7$$, $$E_8$$의 Dynkin diagram인 것과 동치이다. 더 나아가 이 경우 각 indecomposable은 그 dimension vector에 의하여 완전히 결정되며, 이 dimension vector들은 정확히 연관 root system의 positive root들이다. 곧 representation 이론의 분류 문제가 finite root system의 분류, 곧 ADE 분류와 정확히 포개진다. 이 글에서는 이 대응을 통제하는 Tits 이차형식을 도입하고, reflection functor를 도구로 삼아 정리의 골격을 제시한 뒤 선형 $$A_3$$ quiver에서 그 내용을 구체적으로 확인한다.

이 글에서 $$k$$는 field를 가리키고, $$Q=(Q_0,Q_1,s,t)$$는 oriented cycle을 가지지 않으며 ([§Quiver와 경로대수, ⁋명제 5](/ko/math/representation_theory/path_algebras#prop5)) underlying graph가 연결인 유한 quiver이다. Representation이라 하면 유한차원 representation을 뜻하고 ([§Quiver와 경로대수, ⁋정의 9](/ko/math/representation_theory/path_algebras#def9)), $$Q_0=\{1,\ldots,n\}$$으로 둔다. Reflection functor $$S_k^\pm$$, Coxeter functor $$C^\pm$$, preprojective module, 그리고 Euler form과 Tits form의 정의는 [§반사 함자](/ko/math/representation_theory/reflection_functors)를 따르며, root system과 그 위의 reflection, positive root, 이차형식의 일반론은 [\[리 이론\] §근계](/ko/math/lie_theory/root_systems)를 따른다.

## Tits form과 ADE

Gabriel 정리의 두 조건을 잇는 다리는 $$Q$$의 dimension vector lattice $$\mathbb{Z}^n$$ 위에 놓인 이차형식이다. 이 이차형식은 Euler form을 대칭화하여 얻어진다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Oriented cycle이 없는 quiver $$Q$$의 *Euler form* $$\langle d,e\rangle$$과 그 대칭화 $$(d,e)=\langle d,e\rangle+\langle e,d\rangle$$, 그리고 *Tits form*

$$q(d)=\langle d,d\rangle=\sum_{i\in Q_0}d_i^2-\sum_{\alpha\in Q_1}d_{s(\alpha)}d_{t(\alpha)}$$

은 [§반사 함자, ⁋정의 6](/ko/math/representation_theory/reflection_functors#def6)에서 정의한 것이다. $$Q$$의 underlying graph가 $$d$$를 통하여 정해지는 이 이차형식 $$q:\mathbb{Z}^n\rightarrow\mathbb{Z}$$를 $$Q$$의 Tits form이라 부른다.

</div>

Tits form은 화살표의 방향에 의존하지 않는다. $$q(d)=\sum_i d_i^2-\sum_\alpha d_{s(\alpha)}d_{t(\alpha)}$$에서 둘째 합의 각 항 $$d_{s(\alpha)}d_{t(\alpha)}$$는 곱이므로 $$\alpha$$의 방향을 뒤집어도 값이 같고, 따라서 $$q$$는 $$Q$$의 underlying graph와 그 위의 multiple edge 수에만 의존한다. 대칭화 $$(-,-)$$에 대하여 표준 basis vector $$e_k$$가 $$(e_k,e_k)=2\langle e_k,e_k\rangle=2$$를 만족하므로 ($$Q$$에 loop가 없어 $$\langle e_k,e_k\rangle=1$$), 각 vertex $$k$$는 root lattice의 simple root처럼 행동하고 reflection $$s_k(d)=d-(d,e_k)e_k$$가 정의된다 ([§반사 함자, ⁋정의 6](/ko/math/representation_theory/reflection_functors#def6)). 이 형식이 언제 positive definite인지가 핵심이며, 그 답이 곧 ADE 분류이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 연결 quiver $$Q$$에 대하여 다음이 동치이다.

1. Tits form $$q$$가 positive definite이다. 곧 모든 $$0\neq d\in\mathbb{Z}^n$$에 대하여 $$q(d)>0$$이다.
2. $$Q$$의 underlying graph가 type $$A_n$$, $$D_n$$, $$E_6$$, $$E_7$$, $$E_8$$의 Dynkin diagram 가운데 하나이다.

이 경우 대칭화 $$(-,-)$$은 해당 type의 root system을 그 위에 정의하는 Cartan form과 일치하며, $$q(d)=1$$인 $$d\in\mathbb{Z}^n$$의 집합은 그 root system의 root 전체의 집합과 일치한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

대칭화 $$(-,-)$$의 Gram 행렬을 계산한다. $$(e_i,e_i)=2$$이고, $$i\neq j$$에 대하여 $$(e_i,e_j)=\langle e_i,e_j\rangle+\langle e_j,e_i\rangle$$인데, $$\langle e_i,e_j\rangle=-\#\{\alpha:i\rightarrow j\}$$이고 $$\langle e_j,e_i\rangle=-\#\{\alpha:j\rightarrow i\}$$이므로

$$(e_i,e_j)=-\bigl(\#\{\alpha:i\rightarrow j\}+\#\{\alpha:j\rightarrow i\}\bigr)=-m_{ij}$$

이다. 여기서 $$m_{ij}$$는 underlying graph에서 vertex $$i$$와 $$j$$를 잇는 edge의 개수이다. 따라서 행렬 $$\bigl((e_i,e_j)\bigr)_{i,j}$$은 대각이 $$2$$이고 비대각이 $$-m_{ij}$$인 대칭행렬, 곧 underlying graph의 *generalized Cartan matrix*의 대칭화이며, 이것이 $$2q$$의 Gram 행렬이다. 그러므로 $$q$$가 positive definite인 것은 이 대칭행렬이 positive definite인 것과 동치이다.

이제 어떤 그래프의 generalized Cartan matrix가 positive definite인가를 묻는 문제는 root system 이론에서 완전히 해결되어 있다. 위와 같은 대각 $$2$$, 비대각 $$\leq 0$$, 대칭인 행렬이 positive definite인 연결 그래프는 정확히 단순 끈 ADE Dynkin diagram, 곧 $$A_n$$ ($$n\geq 1$$), $$D_n$$ ($$n\geq 4$$), $$E_6,E_7,E_8$$뿐이다 ([\[리 이론\] §근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)). 이 분류의 핵심은 다음과 같다. 그래프가 cycle을 포함하거나, 한 vertex의 차수가 너무 크거나, 가지의 길이가 허용 한계를 넘으면 어떤 $$0\neq d$$에 대하여 $$q(d)\leq 0$$이 되는 vector가 나타난다. 가장 작은 그러한 그래프들이 extended Dynkin diagram $$\widetilde{A}_n,\widetilde{D}_n,\widetilde{E}_6,\widetilde{E}_7,\widetilde{E}_8$$이며, 이들 위에서는 모든 좌표가 양인 *null vector* $$\delta$$가 존재하여 $$q(\delta)=0$$이 된다. 따라서 어떤 그래프 위에서 $$q$$가 positive definite이면 그 그래프는 어떤 extended Dynkin diagram도 부분그래프로 포함하지 않으며, 이로부터 그래프가 ADE Dynkin diagram임이 따라온다. 역으로 ADE Dynkin diagram 위에서 대칭화 $$(-,-)$$은 정확히 해당 단순 끈 root system의 Cartan form이고, 이 root system은 positive definite inner product space 위에 놓이므로 ([\[리 이론\] §근계, ⁋정의 9](/ko/math/lie_theory/root_systems#def9)) $$q$$ 또한 positive definite이다.

마지막으로 $$q$$가 positive definite인 ADE의 경우 $$\{d\in\mathbb{Z}^n\mid q(d)=1\}$$이 root 전체와 일치함을 본다. $$q(d)=\tfrac12(d,d)$$이므로 $$q(d)=1$$은 $$(d,d)=2$$와 같다. 단순 끈 root system에서는 모든 root $$\alpha$$가 $$(\alpha,\alpha)=2$$를 만족하고, 거꾸로 root lattice $$\bigoplus_k\mathbb{Z}e_k$$ 안에서 길이의 제곱이 $$2$$인 vector는 정확히 root뿐이다 (positive definite 격자에서 norm $$2$$인 vector가 유한개이고, 각 root에 대한 reflection으로 생성되는 Weyl group의 궤도가 이들을 모두 채운다). 따라서 $$q(d)=1$$인 정수 vector의 집합은 root 전체와 일치한다.

</details>

명제 2는 Gabriel 정리에서 "ADE"라는 조건이 등장하는 근원을 설명한다. Quiver의 representation 이론이 직접 보는 것은 그 dimension vector lattice 위의 이차형식 $$q$$ 하나이며, 이 $$q$$가 positive definite인가 아닌가가 모든 것을 가른다. $$q$$가 positive definite이면 명제의 마지막 주장에 의하여 $$q(d)=1$$인 dimension vector가 유한개뿐이고, 이들이 root와 일대일로 대응한다. 다음 절에서 indecomposable의 dimension vector가 항상 $$q(d)=1$$을 만족함을 보이면, indecomposable이 유한개일 수밖에 없다는 결론으로 이어진다. $$q$$가 positive definite가 아닌 경우, 곧 underlying graph가 ADE가 아닌 경우에는 $$q(d)\leq 0$$인 dimension vector가 무한히 많은 indecomposable을 허용하며, 이것이 representation-infinite의 근원이다.

## Indecomposable의 dimension vector

이제 indecomposable representation의 dimension vector가 Tits form에 대하여 어떤 값을 가지는지를 살핀다. 핵심은 reflection functor가 dimension vector 위에서 reflection으로 작용하고, reflection이 $$q$$를 보존한다는 사실이며 ([§반사 함자, ⁋명제 12](/ko/math/representation_theory/reflection_functors#prop12)), 이를 Coxeter functor와 결합하면 indecomposable의 dimension vector를 root까지 환원할 수 있다. 먼저 $$q$$가 positive definite일 때 어떤 indecomposable도 Coxeter functor를 거듭하면 결국 사라진다는, 곧 모든 indecomposable이 preprojective라는 사실을 정리한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$Q$$의 Tits form $$q$$가 positive definite이라 하자. 그럼 $$Q$$의 임의의 indecomposable representation $$V$$에 대하여 어떤 $$m\geq 0$$이 존재하여 $$(C^+)^m V=0$$이다. 곧 모든 indecomposable은 preprojective이다 ([§반사 함자, ⁋정의 11](/ko/math/representation_theory/reflection_functors#def11)).

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

귀류법으로 어떤 indecomposable $$V$$에 대하여 모든 $$m\geq 0$$에서 $$(C^+)^m V\neq 0$$이라 하자. 그럼 [§반사 함자, ⁋명제 10](/ko/math/representation_theory/reflection_functors#prop10)에 의하여 각 $$m$$에서 $$(C^+)^m V$$는 다시 indecomposable이고, 그 dimension vector는

$$d_m=\underline\dim\bigl((C^+)^m V\bigr)=c^m(\underline\dim V)$$

로 주어진다. 여기서 $$c=s_{k_n}\cdots s_{k_1}$$은 admissible sink sequence가 정하는 Coxeter element이다. 각 $$d_m$$은 nonzero representation의 dimension vector이므로 음이 아닌 정수 좌표를 가지며, 특히 $$d_m\neq 0$$이다.

이제 $$q$$가 positive definite임을 사용한다. Coxeter element $$c$$는 reflection들의 합성이므로 $$q$$를 보존하며 ([§반사 함자, ⁋명제 12](/ko/math/representation_theory/reflection_functors#prop12)), 따라서 모든 $$m$$에서 $$q(d_m)=q(\underline\dim V)$$로 일정하다. 한편 $$q$$가 positive definite이면 Coxeter element $$c$$는 유한위수(곧 어떤 $$h\geq 1$$에 대해 $$c^h=\mathrm{id}$$, 이 $$h$$가 Coxeter number이다)를 가지지만, $$\mathbb{R}^n$$ 위에서 $$c$$의 고윳값은 모두 $$1$$이 아닌 단위근이어서 $$c$$의 고정공간은 $$\{0\}$$이다. 곧 $$c$$는 어떤 nonzero 벡터도 고정하지 않는다. 핵심은 다음이다. $$q$$가 positive definite이면 $$\{d\in\mathbb{Z}^n\mid q(d)=q(\underline\dim V)\}$$은 유한집합인데 (positive definite 격자의 주어진 norm을 가지는 vector는 유한개), 만일 모든 $$d_m$$이 음이 아닌 좌표를 가지면서 이 유한집합 안에 머문다면 비둘기집 원리로 $$d_{m}=d_{m'}$$인 $$m<m'$$이 존재하여 $$c^{m'-m}$$이 nonzero vector $$d_m$$을 고정하게 된다. 그러나 positive definite 공간 위의 Coxeter element는 nonzero vector를 고정하지 않으므로 ($$c$$의 고정공간은 $$\{0\}$$이다) 이는 모순이다. 따라서 어떤 $$m$$에서 $$(C^+)^m V=0$$이어야 하고, $$V$$는 preprojective이다.

</details>

명제 3은 ADE quiver의 representation 이론을 유한한 그림으로 가두는 결정적 단계이다. $$q$$가 positive definite이면 모든 indecomposable이 preprojective이므로, 모든 indecomposable은 어떤 indecomposable projective $$P$$로부터 $$C^-$$를 유한 번 적용하여 얻어진다 ([§반사 함자, ⁋정의 11](/ko/math/representation_theory/reflection_functors#def11) 직후의 논의). Indecomposable projective는 vertex의 개수 $$n$$만큼 있고, 각각의 $$C^-$$-궤도는 dimension vector 위에서 Coxeter element의 궤도로 나타나므로, 이 모든 궤도를 합한 것이 indecomposable 전체이다. 다음 명제가 그 dimension vector들이 정확히 root임을 말한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$Q$$의 Tits form $$q$$가 positive definite이라 하자. 그럼 임의의 indecomposable representation $$V$$에 대하여 $$q(\underline\dim V)=1$$이다. 곧 $$\underline\dim V$$는 명제 2의 root system의 positive root이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

명제 3에 의하여 $$V$$는 preprojective이므로, 어떤 indecomposable projective $$P$$와 $$j\geq 0$$에 대하여 $$V\cong (C^-)^j P$$이고, 그 dimension vector는 reflection들의 합성을 projective의 dimension vector에 적용하여 얻어진다 ([§반사 함자, ⁋명제 10](/ko/math/representation_theory/reflection_functors#prop10)). 먼저 indecomposable projective의 dimension vector가 $$q$$ 값 $$1$$을 가짐을 본다. Admissible sink sequence $$(k_1,\ldots,k_n)$$을 잡으면, 이 orientation에서 첫 vertex $$k_1$$에 대응하는 indecomposable projective는 simple $$S_{k_1}$$이며 그 dimension vector는 $$e_{k_1}$$로 $$q(e_{k_1})=1$$이다. 일반적으로 각 indecomposable projective $$P_k$$는 admissible sink sequence를 따라 simple로부터 reflection들로 도달되며, 그 dimension vector는 $$e_k$$에 일련의 simple reflection을 적용한 것이라 $$q(\underline\dim P_k)=q(e_k)=1$$이다. 실제로 simple reflection은 $$q$$를 보존하므로 ([§반사 함자, ⁋명제 12](/ko/math/representation_theory/reflection_functors#prop12)) 표준 basis vector에서 reflection으로 도달되는 모든 dimension vector는 $$q$$ 값 $$1$$을 가진다.

이제 $$V\cong(C^-)^j P$$이므로

$$q(\underline\dim V)=q\bigl(c^{-j}(\underline\dim P)\bigr)=q(\underline\dim P)=1$$

이다. 둘째 등호는 Coxeter element $$c$$ (따라서 그 역 $$c^{-j}$$) 가 $$q$$를 보존하기 때문이다 ([§반사 함자, ⁋명제 12](/ko/math/representation_theory/reflection_functors#prop12)). 따라서 $$q(\underline\dim V)=1$$이다. $$V$$가 nonzero representation이므로 $$\underline\dim V$$는 음이 아닌 좌표를 가지며 $$0$$이 아니므로, 명제 2에 의하여 $$\underline\dim V$$는 root이고, 좌표가 음이 아니므로 positive root이다.

</details>

명제 4는 대응 $$V\mapsto\underline\dim V$$가 indecomposable의 isomorphism class에서 positive root로 가는 잘 정의된 사상임을 준다. 남은 것은 이 사상이 전단사임을 보이는 것이다. 단사성, 곧 같은 dimension vector를 가지는 indecomposable이 isomorphism을 무시하여 유일하다는 사실과, 전사성, 곧 모든 positive root가 어떤 indecomposable의 dimension vector로 실현된다는 사실을 reflection functor로 추적하면 Gabriel 정리가 완성된다.

## Gabriel 정리

이제 앞 절들의 결과를 묶어 정리를 진술한다. 한 방향은 $$q$$가 positive definite이면 indecomposable이 유한개의 positive root에 일대일 대응한다는 것이고, 다른 방향은 $$q$$가 positive definite가 아니면 indecomposable이 무한히 많다는 것이다.

<div class="proposition" markdown="1">

<ins id="thm5">**정리 5**</ins> (Gabriel) $$Q$$를 oriented cycle이 없는 연결 quiver라 하자. $$Q$$가 *representation-finite<sub>유한표현형</sub>*, 곧 isomorphism을 무시하여 유한개의 indecomposable representation만을 가지는 것은 $$Q$$의 underlying graph가 type $$A_n$$, $$D_n$$, $$E_6$$, $$E_7$$, $$E_8$$의 Dynkin diagram인 것과 동치이다. 이 경우 대응

$$V\longmapsto\underline\dim V$$

는 indecomposable representation의 isomorphism class들과 Tits form $$q$$의 positive root들 사이의 전단사를 이루며, 특히 indecomposable의 개수는 positive root의 개수와 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$Q$$의 underlying graph가 ADE Dynkin diagram인 경우, 곧 $$q$$가 positive definite인 경우를 본다 ([명제 2](#prop2)). 명제 4에 의하여 $$V\mapsto\underline\dim V$$는 indecomposable의 isomorphism class에서 positive root로 가는 사상이다. 이 사상이 전단사임을 reflection functor로 보인다.

*단사성.* Dimension vector가 같은 두 indecomposable $$V,V'$$이 isomorphic함을 보인다. Admissible sink sequence를 따라 Coxeter functor $$C^+$$를 거듭 적용하면, 명제 3에 의하여 유한 번 만에 둘 다 $$0$$이 된다. 매 단계에서 $$C^+$$의 한 조각인 sink reflection $$S_k^+$$는 dimension vector 위에서 $$s_k$$로 작용하고 ([§반사 함자, ⁋명제 7](/ko/math/representation_theory/reflection_functors#prop7)) indecomposability를 보존하므로 ([§반사 함자, ⁋명제 8](/ko/math/representation_theory/reflection_functors#prop8)), 두 representation은 같은 단계에서 같은 vertex의 simple $$S_k$$에 도달하여 소멸한다. 곧 어떤 합성 $$T=S_{k_r}^+\cdots S_{k_1}^+$$에 대하여 $$TV\cong S_k\cong TV'$$이 되는 단계가 처음으로 나타나며, 이 simple에 도달하기까지의 모든 $$S_{k_i}^+$$는 $$S_{k_i}$$ 이외의 indecomposable 위에서 quasi-inverse $$S_{k_i}^-$$를 가진다 ([§반사 함자, ⁋명제 8](/ko/math/representation_theory/reflection_functors#prop8)). 따라서 이 quasi-inverse들을 역순으로 적용하여 $$S_k$$로부터 $$V$$와 $$V'$$를 모두 유일하게 복원하면 $$V\cong V'$$이다.

*전사성.* 임의의 positive root $$d$$에 대하여 $$\underline\dim V=d$$인 indecomposable $$V$$가 존재함을 보인다. Root $$d$$는 simple reflection들의 합성으로 어떤 simple root $$e_k$$까지 환원된다 ([\[리 이론\] §근계, ⁋정의 15](/ko/math/lie_theory/root_systems#def15)). 곧 simple reflection의 열 $$s_{k_1},\ldots,s_{k_r}$$이 있어 $$s_{k_r}\cdots s_{k_1}(d)=e_k$$이며, 이 환원의 매 단계가 dimension vector를 양의 좌표로 유지하도록 잡을 수 있다. 각 단계의 simple reflection을 그에 대응하는 reflection functor로 들어 올린다. Simple root $$e_k$$는 simple representation $$S_k$$의 dimension vector이고, $$S_k$$는 indecomposable이므로, $$S_k$$에 위 reflection들의 quasi-inverse를 역순으로 적용하면 ([§반사 함자, ⁋명제 7](/ko/math/representation_theory/reflection_functors#prop7), [⁋명제 8](/ko/math/representation_theory/reflection_functors#prop8)) dimension vector가 $$d$$인 indecomposable $$V$$를 얻는다. 매 단계에서 dimension vector가 양의 좌표를 유지하므로 reflection functor가 nonzero indecomposable을 주며, 따라서 환원 전체가 잘 들어 올려진다. 이로써 $$V\mapsto\underline\dim V$$는 전사이다.

전단사가 확립되었으므로 indecomposable의 개수는 positive root의 개수와 같고, root system이 유한하므로 ([\[리 이론\] §근계, ⁋정의 9](/ko/math/lie_theory/root_systems#def9)) 유한이다. 따라서 ADE인 경우 $$Q$$는 representation-finite이다.

역으로 $$Q$$의 underlying graph가 ADE Dynkin diagram이 아니라 하자. 그럼 $$q$$는 positive definite가 아니며 ([명제 2](#prop2)), 그 underlying graph는 어떤 extended Dynkin diagram을 부분그래프로 포함한다. Extended Dynkin diagram 위에서는 모든 좌표가 양인 null vector $$\delta$$가 존재하여 $$q(\delta)=0$$이고, 따라서 $$q(m\delta)=m^2 q(\delta)=0$$이 모든 $$m\geq 1$$에서 성립한다. Tame 또는 wild quiver의 표현론에서, 이러한 isotropic 또는 부정부호 방향을 따라 무한히 많은 indecomposable이 실현됨이 알려져 있다. 가장 단순한 증거는 Kronecker quiver $$1\rightrightarrows 2$$ ([§Quiver와 경로대수, ⁋예시 8](/ko/math/representation_theory/path_algebras#ex8)) 로, 이는 extended Dynkin diagram $$\widetilde{A}_1$$ 위의 quiver이며 dimension vector $$(1,1)$$을 가지는 indecomposable이 $$\mathbb{P}^1(k)$$로 매개되는 무한족을 이룬다. 일반적으로 underlying graph가 ADE가 아닌 연결 quiver는 그 안에 이러한 무한족을 품으므로 representation-finite가 아니다. 완전한 논증은 [ASS, Chapter VII]과 [Br, §5]를 따른다.

</details>

정리 5는 quiver의 representation 이론과 finite root system의 분류가 정확히 포개진다는 것을 말한다. 한 vertex에서의 reflection functor가 dimension vector 위에서 simple reflection으로 작용한다는 사실이 ([§반사 함자, ⁋명제 7](/ko/math/representation_theory/reflection_functors#prop7)), indecomposable의 분류를 root system의 조합론으로 옮겨 주는 다리이다. 각 indecomposable에 하나의 positive root가 대응하고, 그 root는 Weyl group의 작용으로 simple root까지 환원되며, 그 환원의 매 단계가 곧 하나의 reflection functor이다. 이 그림에서 $$q$$가 positive definite인 경우, 곧 ADE인 경우에만 root가 유한하고 따라서 indecomposable도 유한하다. 다음 절에서 가장 작은 비자명한 예인 $$A_3$$에서 이 대응을 구체적으로 본다.

## $$A_3$$의 경우

선형 $$A_3$$ quiver는 Gabriel 정리의 모든 요소를 손으로 확인할 수 있는 가장 깔끔한 예이다. 이 quiver의 indecomposable은 여섯 개이고, 연관 root system $$A_3$$의 positive root도 여섯 개이며, 둘이 dimension vector를 통하여 정확히 대응한다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 선형 $$A_3$$ quiver $$Q:1\xrightarrow{\ \alpha\ }2\xrightarrow{\ \beta\ }3$$ ([§Quiver와 경로대수, ⁋예시 6](/ko/math/representation_theory/path_algebras#ex6)) 를 생각하자. 이 quiver의 Tits form은

$$q(d)=d_1^2+d_2^2+d_3^2-d_1 d_2-d_2 d_3$$

이고, 대칭화 $$(-,-)$$의 Gram 행렬은

$$\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$$

으로 type $$A_3$$의 Cartan matrix이다 ([\[리 이론\] §근계, ⁋정의 16](/ko/math/lie_theory/root_systems#def16)). 이 행렬은 positive definite이므로 ([명제 2](#prop2)) $$Q$$는 representation-finite이며, $$q(d)=1$$인 양의 정수 vector를 모두 구하면

$$(1,0,0),\ (0,1,0),\ (0,0,1),\ (1,1,0),\ (0,1,1),\ (1,1,1)$$

의 여섯 개이다. 가령 $$q(1,1,1)=1+1+1-1-1=1$$이고 $$q(1,1,0)=1+1+0-1-0=1$$이다. 이들은 $$A_3$$ root system의 positive root $$e_i-e_j$$ ($$1\leq i<j\leq 4$$) 와 정확히 대응한다 ([\[리 이론\] §근계, ⁋예시 13](/ko/math/lie_theory/root_systems#ex13)). 한편 [§Auslander–Reiten 이론, ⁋예시 9](/ko/math/representation_theory/auslander_reiten#ex9)에서 이 quiver의 indecomposable이 정확히 여섯 개

$$M_{[1,1]}=(1,0,0),\quad M_{[2,2]}=(0,1,0),\quad M_{[3,3]}=(0,0,1),$$

$$M_{[1,2]}=(1,1,0),\quad M_{[2,3]}=(0,1,1),\quad M_{[1,3]}=(1,1,1)$$

임을 보았다. 곧 각 $$1\leq i\leq j\leq 3$$에 대하여 vertex $$i,\ldots,j$$에 $$k$$를 얹고 그 사이 arrow에 $$\id_k$$를 둔 interval representation $$M_{[i,j]}$$이 유일한 indecomposable이며, 그 dimension vector는 위에서 구한 여섯 개의 positive root와 일대일로 대응한다. 이로써 정리 5의 전단사 $$V\mapsto\underline\dim V$$가 $$A_3$$에서 구체적으로 확인된다.

</div>

예시 6에서 dimension vector가 같은 indecomposable이 유일하다는 정리 5의 단사성은 interval representation $$M_{[i,j]}$$이 각 positive root마다 정확히 하나씩 있다는 사실로 나타나고, 전사성은 여섯 positive root가 모두 어떤 $$M_{[i,j]}$$로 실현된다는 사실로 나타난다. 또한 [§Auslander–Reiten 이론, ⁋예시 9](/ko/math/representation_theory/auslander_reiten#ex9)에서 본 AR translate $$\tau$$의 작용은 dimension vector 위에서 Coxeter element $$c$$의 작용에 대응한다. 가령 $$\tau M_{[1,1]}=M_{[2,2]}$$은 dimension vector $$(1,0,0)$$이 $$(0,1,0)$$으로 옮겨지는 것으로, 이것이 명제 3에서 본 Coxeter functor에 의한 preprojective 궤도의 한 걸음이다. 이렇게 $$A_3$$의 작은 그림 안에서 Tits form, root system, reflection functor, AR 이론이 하나의 정합적인 구조로 묶인다.

---

**참고문헌**

**[Gab]** P. Gabriel, *Unzerlegbare Darstellungen I*, Manuscripta Mathematica **6** (1972), 71–103.

**[BGP]** I. N. Bernstein, I. M. Gelfand, and V. A. Ponomarev, *Coxeter functors and Gabriel's theorem*, Russian Mathematical Surveys **28** (1973), 17–32.

**[ASS]** I. Assem, D. Simson, and A. Skowroński, *Elements of the representation theory of associative algebras, Volume 1: Techniques of representation theory*, Cambridge University Press, 2006.

**[Br]** M. Brion, *Representations of quivers*, in *Geometric methods in representation theory I*, Société Mathématique de France, 2012.

**[DW]** H. Derksen and J. Weyman, *An introduction to quiver representations*, American Mathematical Society, 2017.
