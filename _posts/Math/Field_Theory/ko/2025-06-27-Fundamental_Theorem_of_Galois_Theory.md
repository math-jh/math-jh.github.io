---
title: "갈루아 이론의 기본정리"
description: "갈루아 이론의 기본정리를 증명하며, 갈루아 확장의 부분확장과 갈루아 군의 닫힌 부분군 사이의 대응 관계를 다룬다."
excerpt: "Subgroup과 intermediate field 사이의 Galois correspondence"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/fundamental_theorem_of_galois_theory
sidebar: 
    nav: "field_theory-ko"

date: 2025-06-27
weight: 10
published: false

---

우리는 이제 드디어 갈루아 이론의 기본정리를 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="thm1">**정리 1**</ins> Field $$\mathbb{K}$$의 Galois extension $$\mathbb{L}/\mathbb{K}$$와 그 Galois group $$\Gamma=\Gal(\mathbb{L}/\mathbb{K})$$을 생각하자. $$\mathscr{K}$$를 $$\mathbb{L}$$의 subextension들의 모임이라 하고, $$\mathscr{G}$$를 $$\Gamma$$의 closed subgroup들의 모임이라 하면 $$\mathscr{K}$$와 $$\mathscr{G}$$ 사이의 두 함수

$$k:\mathscr{G}\rightarrow\mathscr{K};\qquad G\mapsto k(G)\text{ the field of invariants of $G$}$$

그리고 

$$g:\mathscr{K}\rightarrow\mathscr{G};\qquad \mathbb{M}\mapsto g(\mathbb{M})\text{ the group of $\mathbb{M}$-automorphisms of $L$}$$

을 생각하면 이들은 서로의 inverse이다. 

</div>

이를 증명하기 위해 다음과 같이 두 단계로 나누어 증명한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> 임의의 subextension $$\mathbb{M}\in \mathscr{K}$$에 대하여, $$\mathbb{L}/\mathbb{M}$$ 또한 Galois extension이다. 이 때, Galois group $$\Gal(\mathbb{L}/\mathbb{M})$$을 자명한 방식으로 $$\Gal(\mathbb{L}/\mathbb{K})$$의 subgroup으로 보면, 이는 $$\Gal(\mathbb{L}/\mathbb{K})$$의 *closed* subgroup이며 따라서 $$g$$가 잘 정의된다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\mathbb{L}/\mathbb{M}$$이 Galois extension임을 보이자. $$\mathbb{L}/\mathbb{K}$$가 algebraic이므로 $$\mathbb{L}/\mathbb{M}$$도 algebraic이다. 임의의 $$x\in \mathbb{L}$$에 대하여, $$x$$의 $$\mathbb{K}$$에 대한 minimal polynomial을 $$f$$, $$\mathbb{M}$$에 대한 minimal polynomial을 $$g$$라 하자. $$f$$는 $$\mathbb{M}[\x]$$의 원소이기도 하고 $$f(x)=0$$이므로 $$g$$는 $$f$$를 나눈다. ([§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)) 그런데 $$\mathbb{L}/\mathbb{K}$$가 Galois이므로 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 셋째 조건에 의하여 $$f$$는 $$\mathbb{L}[\x]$$에서 서로 다른 일차식들의 곱으로 쪼개지고, 따라서 그 약수인 $$g$$ 또한 그러하다. 즉 $$\mathbb{L}/\mathbb{M}$$은 같은 정리의 셋째 조건을 만족하므로 Galois extension이다.

이제 $$\Gal(\mathbb{L}/\mathbb{M})$$이 closed인 것을 보이자. 집합으로서

$$\Gal(\mathbb{L}/\mathbb{M})=\left\{\sigma\in \Gal(\mathbb{L}/\mathbb{K})\mid \text{$\sigma(x)=x$ for all $x\in \mathbb{M}$}\right\}=\bigcap_{x\in \mathbb{M}}\left\{\sigma\mid \sigma(x)=x\right\}$$

이 성립한다. 그런데 [§갈루아 군의 성질들](/ko/math/field_theory/properties_of_galois_extensions)에서 살펴본 subbase의 표기로 $$\{\sigma\mid\sigma(x)=x\}=U_{x,x}\cap\Gal(\mathbb{L}/\mathbb{K})$$는 열린집합이고, 그 여집합 또한 열린집합들 $$U_{x,y}$$ ($$y\neq x$$)들의 합집합이므로 이들은 모두 clopen이다. 따라서 $$\Gal(\mathbb{L}/\mathbb{M})$$은 closed set들의 교집합이므로 closed이고, subgroup인 것은 자명하다.

</details>

다음 보조정리는 흔히 *Artin의 보조정리*라는 이름으로 불리는 결과로, [정리 1](#thm1)의 증명에서 핵심적인 counting을 제공한다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3 (Artin)**</ins> Field $$\mathbb{N}$$과, $$\mathbb{N}$$의 automorphism들로 이루어진 유한군 $$H$$가 주어졌다 하자. $$H$$의 invariant들의 field를 $$\mathbb{N}^H$$라 하면, $$[\mathbb{N}:\mathbb{N}^H]\leq \card H$$가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\card H=m$$이라 하고 $$H=\{\sigma_1,\ldots,\sigma_m\}$$이라 적자. 여기서 $$\sigma_1=\id_\mathbb{N}$$이다. 결론에 반하여 $$\mathbb{N}^H$$ 위에서 일차독립인 원소들 $$x_1,\ldots,x_{m+1}\in \mathbb{N}$$이 존재한다 가정하자.

다음의 동차 연립일차방정식

$$\sum_{j=1}^{m+1}\sigma_i(x_j)\,c_j=0,\qquad i=1,\ldots,m$$

을 $$\mathbb{N}$$ 위에서 미지수 $$c_1,\ldots,c_{m+1}$$에 대해 생각하자. 이 system은 방정식이 $$m$$개, 미지수가 $$m+1$$개이므로 자명하지 않은 해를 갖는다. 만일 그렇지 않다면 $$(c_j)\mapsto \bigl(\sum_j \sigma_i(x_j)c_j\bigr)_i$$로 정의되는 linear map $$\mathbb{N}^{m+1} \rightarrow \mathbb{N}^m$$이 injective이고, 그럼 $$\mathbb{N}^{m+1}$$의 standard basis의 image는 $$\mathbb{N}^m$$의 일차독립인 $$m+1$$개의 원소들이 된다. 이를 포함하는 $$\mathbb{N}^m$$의 basis가 존재하므로 ([\[선형대수학\] §벡터공간의 차원, ⁋명제 5](/ko/math/linear_algebra/dimension#prop5)) $$\mathbb{N}^m$$은 크기 $$m+1$$ 이상의 basis를 갖게 되고, 이는 [\[선형대수학\] §벡터공간의 차원, ⁋정리 1](/ko/math/linear_algebra/dimension#thm1)에 모순이기 때문이다.

이제 자명하지 않은 해들 가운데 $$0$$이 아닌 성분의 개수가 가장 적은 해 $$(c_1,\ldots,c_{m+1})$$을 택하고, index를 재배열하여 $$c_1,\ldots,c_r\neq 0$$이고 $$c_{r+1}=\cdots=c_{m+1}=0$$이라 하자. 해 전체에 $$c_r^{-1}$$을 곱하여 $$c_r=1$$로 정규화할 수 있다. 우선 $$r\geq 2$$인데, $$r=1$$이라면 $$\sigma_1=\id_\mathbb{N}$$에 해당하는 방정식이 $$x_1c_1=0$$이 되어 $$c_1=0$$이 되기 때문이다.

임의의 $$\tau\in H$$를 각 방정식에 적용하면

$$\sum_{j=1}^{m+1}(\tau\sigma_i)(x_j)\,\tau(c_j)=0,\qquad i=1,\ldots,m$$

을 얻는데, $$i$$가 $$1$$부터 $$m$$까지 움직일 때 $$\tau\sigma_i$$들은 정확히 $$H$$ 전체를 움직이므로 $$(\tau(c_j))_j$$ 또한 같은 system의 해이다. 따라서 $$(c_j-\tau(c_j))_j$$도 해인데, 이 해의 $$r$$번째 성분은 $$c_r-\tau(1)=1-1=0$$이고 $$r+1$$번째 이후의 성분들도 모두 $$0$$이므로, $$0$$이 아닌 성분의 개수가 $$r$$개 미만이다. 그럼 $$(c_j)$$의 최소성에 의하여 이 해는 자명한 해여야 하고, 즉 모든 $$j$$와 모든 $$\tau\in H$$에 대하여 $$\tau(c_j)=c_j$$이다. 다시 말해 $$c_j\in \mathbb{N}^H$$이다.

그럼 $$\sigma_1=\id_\mathbb{N}$$에 해당하는 방정식 $$\sum_{j}x_jc_j=0$$은 $$x_1,\ldots,x_{m+1}$$ 사이의 자명하지 않은 $$\mathbb{N}^H$$-일차결합이 되어, 이들이 $$\mathbb{N}^H$$ 위에서 일차독립이라는 가정에 모순이다.

</details>

이제 [정리 1](#thm1)을 증명할 수 있다.

<details class="proof--alone" markdown="1">
<summary>정리 1의 증명</summary>

[보조정리 2](#lem2)에 의하여 $$g$$가 잘 정의되고, $$k$$가 잘 정의되는 것은 자명하다.

우선 $$k\circ g=\id_\mathscr{K}$$를 보이자. 임의의 $$\mathbb{M}\in\mathscr{K}$$에 대하여 [보조정리 2](#lem2)에 의해 $$\mathbb{L}/\mathbb{M}$$은 Galois extension이고, 따라서 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 첫째 조건에 의하여 $$\Gal(\mathbb{L}/\mathbb{M})$$-invariant element들은 모두 $$\mathbb{M}$$의 원소이다. 거꾸로 $$\mathbb{M}$$의 원소들이 $$\Gal(\mathbb{L}/\mathbb{M})$$에 의해 고정되는 것은 자명하므로 $$k(g(\mathbb{M}))=\mathbb{M}$$이다.

이제 $$g\circ k=\id_\mathscr{G}$$를 보여야 한다. Closed subgroup $$G\in\mathscr{G}$$에 대하여 $$\mathbb{M}=k(G)$$로 두고 $$G'=g(\mathbb{M})=\Gal(\mathbb{L}/\mathbb{M})$$이라 하자. $$G$$의 원소들은 정의에 의해 $$\mathbb{M}$$을 고정하므로 $$G\subseteq G'$$이다. 우리의 주장은 $$G$$가 $$G'$$에서 dense하다는 것이다.

이를 위해 임의의 $$\sigma\in G'$$와, $$\sigma$$의 $$\Gal(\mathbb{L}/\mathbb{K})$$에서의 기본근방 $$U_{\mathbb{M}_0}(\sigma)$$가 주어졌다 하자. 여기서 $$\mathbb{M}_0$$는 $$\mathbb{L}/\mathbb{K}$$의 finite subextension이다. 그럼 $$\mathbb{M}(\mathbb{M}_0)$$는 $$\mathbb{M}$$의 finite degree extension이므로, [§갈루아 확장, ⁋명제 11](/ko/math/field_theory/galois_extension#prop11)을 Galois extension $$\mathbb{L}/\mathbb{M}$$에 적용하면 $$\mathbb{M}(\mathbb{M}_0)$$를 포함하는 finite degree Galois subextension $$\mathbb{N}/\mathbb{M}$$이 존재한다.

$$\mathbb{N}/\mathbb{M}$$이 quasi-Galois이므로, [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의하여 임의의 $$\tau\in \Gal(\mathbb{L}/\mathbb{M})$$은 $$\mathbb{N}$$을 $$\mathbb{N}$$으로 보내고, 따라서 restriction homomorphism

$$\rho:\Gal(\mathbb{L}/\mathbb{M}) \rightarrow \Gal(\mathbb{N}/\mathbb{M});\qquad \tau\mapsto \tau\vert_\mathbb{N}$$

이 잘 정의된다. $$H=\rho(G)$$라 하면 $$H$$는 $$\mathbb{N}$$의 automorphism들로 이루어진 유한군이다. 이제 $$\mathbb{N}^H$$를 계산하면, $$x\in \mathbb{N}$$이 $$H$$의 모든 원소에 의해 고정되는 것은 $$G$$의 모든 원소에 의해 고정되는 것과 같고, 이는 곧 $$x\in k(G)=\mathbb{M}$$인 것과 같다. 즉 $$\mathbb{N}^H=\mathbb{M}$$이고, [보조정리 3](#lem3)에 의하여

$$[\mathbb{N}:\mathbb{M}]\leq \card H$$

이다. 한편 $$\mathbb{N}/\mathbb{M}$$은 finite degree Galois extension이므로 $$\card\Gal(\mathbb{N}/\mathbb{M})=[\mathbb{N}:\mathbb{M}]$$이다. 이는 $$\mathbb{N}/\mathbb{M}$$이 separable이므로 $$\mathbb{M}$$-homomorphism $$\mathbb{N} \rightarrow \overline{\mathbb{M}}$$의 개수가 $$[\mathbb{N}:\mathbb{M}]_s=[\mathbb{N}:\mathbb{M}]$$이고 ([§에탈대수, ⁋정의 10](/ko/math/field_theory/etale_algebras#def10), [§분리가능차수, ⁋명제 9](/ko/math/field_theory/separable_degree#prop9)), $$\mathbb{N}/\mathbb{M}$$이 quasi-Galois이므로 이들 homomorphism이 모두 $$\mathbb{N}$$의 $$\mathbb{M}$$-automorphism이 되기 때문이다. ([§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)) 따라서

$$\card H\leq \card \Gal(\mathbb{N}/\mathbb{M})=[\mathbb{N}:\mathbb{M}]\leq \card H$$

이고, $$H\subseteq \Gal(\mathbb{N}/\mathbb{M})$$이 같은 크기의 유한집합들이므로 $$H=\Gal(\mathbb{N}/\mathbb{M})$$이다.

특히 $$\sigma\vert_\mathbb{N}\in \Gal(\mathbb{N}/\mathbb{M})=\rho(G)$$이므로, $$\tau\vert_\mathbb{N}=\sigma\vert_\mathbb{N}$$이도록 하는 $$\tau\in G$$가 존재한다. 그럼 $$\mathbb{M}_0\subseteq \mathbb{N}$$이므로 $$\tau\in U_{\mathbb{M}_0}(\sigma)$$이고, 즉 $$\sigma$$의 임의의 기본근방이 $$G$$와 만난다. 따라서 $$G$$는 $$G'$$에서 dense하고, $$G$$가 closed라는 가정으로부터 $$G=G'$$이다. 

</details>

특별히 $$\mathbb{L}/\mathbb{K}$$가 finite degree Galois extension이라면 [§갈루아 군의 성질들, ⁋예시 1](/ko/math/field_theory/properties_of_galois_extensions#ex1)에서 살펴본 것과 같이 $$\Gal(\mathbb{L}/\mathbb{K})$$는 discrete space이고, 따라서 임의의 subgroup이 closed이다. 즉 이 경우 [정리 1](#thm1)은 subextension들과 subgroup들 사이의 대응이라는 고전적인 갈루아 이론의 기본정리가 된다. 또, [정리 1](#thm1)의 증명 과정에서 finite degree Galois extension $$\mathbb{N}/\mathbb{M}$$에 대하여 $$\card\Gal(\mathbb{N}/\mathbb{M})=[\mathbb{N}:\mathbb{M}]$$이 성립한다는 사실도 함께 얻었다.

기본정리의 두 번째 부분은 이 대응 하에서 normal subgroup이 무엇에 대응되는지를 알려준다.

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> [정리 1](#thm1)의 상황에서, closed subgroup $$H\in\mathscr{G}$$가 $$\Gal(\mathbb{L}/\mathbb{K})$$의 normal subgroup인 것과 $$\mathbb{M}=k(H)$$가 $$\mathbb{K}$$의 Galois extension인 것이 동치이다. 이 경우 restriction은 group isomorphism

$$\Gal(\mathbb{L}/\mathbb{K})/H\cong \Gal(\mathbb{M}/\mathbb{K})$$

을 유도한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 간단한 계산으로 시작하자. 임의의 closed subgroup $$H$$와 $$\sigma\in\Gal(\mathbb{L}/\mathbb{K})$$에 대하여, $$x\in \mathbb{L}$$이 $$\sigma H\sigma^{-1}$$의 모든 원소에 의해 고정되는 것은 $$\sigma^{-1}(x)$$가 $$H$$의 모든 원소에 의해 고정되는 것과 같으므로

$$\mathbb{L}^{\sigma H\sigma^{-1}}=\sigma(\mathbb{L}^H)=\sigma(\mathbb{M})\tag{$\ast$}$$

이 성립한다.

이제 $$H$$가 normal subgroup이라 가정하자. 그럼 식 $$(\ast)$$에 의해 임의의 $$\sigma\in\Gal(\mathbb{L}/\mathbb{K})$$에 대해 $$\sigma(\mathbb{M})=\mathbb{M}$$이고, 따라서 restriction $$\rho:\Gal(\mathbb{L}/\mathbb{K}) \rightarrow \Aut_\mathbb{K}(\mathbb{M})$$이 잘 정의된다. $$\mathbb{M}$$의 원소 $$x$$가 $$\rho$$의 image의 모든 원소에 의해 고정된다면 $$x$$는 $$\Gal(\mathbb{L}/\mathbb{K})$$ 전체에 의해 고정되므로, $$\mathbb{L}/\mathbb{K}$$가 Galois라는 것으로부터 $$x\in \mathbb{K}$$이다. 특히 $$\mathbb{M}$$의 모든 $$\mathbb{K}$$-automorphism들의 group의 invariant들은 $$\mathbb{K}$$에 포함되고, 따라서 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 첫째 조건에 의하여 $$\mathbb{M}/\mathbb{K}$$는 Galois extension이다.

거꾸로 $$\mathbb{M}/\mathbb{K}$$가 Galois extension이라 하자. 그럼 특히 $$\mathbb{M}/\mathbb{K}$$는 quasi-Galois이므로, [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의하여 임의의 $$\sigma\in \Gal(\mathbb{L}/\mathbb{K})$$가 $$\sigma(\mathbb{M})=\mathbb{M}$$을 만족한다. 그럼 식 $$(\ast)$$과 [정리 1](#thm1)의 대응에 의하여

$$\sigma H\sigma^{-1}=g\bigl(\sigma(\mathbb{M})\bigr)=g(\mathbb{M})=H$$

이므로 $$H$$는 normal subgroup이다. 여기서 $$\sigma H\sigma^{-1}$$이 closed인 것은 conjugation이 topological group의 homeomorphism이기 때문이다.

마지막으로 isomorphism을 확인하자. $$\mathbb{M}/\mathbb{K}$$가 Galois일 때, 위에서 정의한 restriction은 group homomorphism $$\rho:\Gal(\mathbb{L}/\mathbb{K}) \rightarrow \Gal(\mathbb{M}/\mathbb{K})$$이고, 그 kernel은 $$\mathbb{M}$$을 고정하는 원소들의 모임, 즉 $$\Gal(\mathbb{L}/\mathbb{M})=g(k(H))=H$$이다. 한편 $$\rho$$가 surjective인 것은 [§갈루아 확장, ⁋명제 13](/ko/math/field_theory/galois_extension#prop13)과 같다. 임의의 $$\tau\in\Gal(\mathbb{M}/\mathbb{K})$$는 [§갈루아 확장, ⁋명제 1](/ko/math/field_theory/galois_extension#prop1)에 의해 $$\overline{\mathbb{K}}$$의 $$\mathbb{K}$$-automorphism으로 확장되고, $$\mathbb{L}/\mathbb{K}$$가 quasi-Galois이므로 이 확장을 $$\mathbb{L}$$로 제한하면 $$\tau$$를 확장하는 $$\Gal(\mathbb{L}/\mathbb{K})$$의 원소를 얻기 때문이다. 따라서 first isomorphism theorem에 의해 $$\Gal(\mathbb{L}/\mathbb{K})/H\cong\Gal(\mathbb{M}/\mathbb{K})$$이다.

</details>

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.

---
