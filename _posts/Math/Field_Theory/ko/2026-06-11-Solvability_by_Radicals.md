---
title: "거듭제곱근 가해성"
description: "1의 거듭제곱근과 순환확대의 구조를 살펴본 후, 다항식이 거듭제곱근으로 풀리는 것과 갈루아 군이 가해군인 것이 동치라는 갈루아의 정리를 증명한다."
excerpt: "Solvability by radicals와 solvable Galois group"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/solvability_by_radicals
sidebar: 
    nav: "field_theory-ko"

date: 2026-06-11
weight: 11
published: false

---

[§제곱근확대체](/ko/math/field_theory/radical_extensions)의 서두에서 우리는 다항식의 근들을 서로 바꾸는 작용으로 group을 만들고, 이 group을 통해 extension들을 분류하겠다는 갈루아 이론의 철학을 언급했었다. [§갈루아 이론의 기본정리](/ko/math/field_theory/fundamental_theorem_of_galois_theory)로 이 철학이 완성되었으므로, 이제 우리는 갈루아 이론의 역사적인 출발점이었던 질문에 답할 수 있다. 어떤 다항식의 근을 사칙연산과 거듭제곱근만으로 표현할 수 있는가?

<div class="remark" markdown="1">

**참고** 이번 글에서 모든 field는 characteristic $$0$$을 갖는다. 그럼 characteristic exponent가 $$1$$이므로 Frobenius endomorphism이 identity가 되어 모든 field가 perfect이고, 따라서 [§분리가능확대체, ⁋명제 9](/ko/math/field_theory/separable_extensions#prop9)에 의하여 모든 algebraic extension이 separable이다. 특히 임의의 quasi-Galois extension이 Galois extension이다. Characteristic $$p$$에서의 가해성 이론은 separability와 관련된 추가적인 논의를 필요로 하므로 여기서는 다루지 않는다.

</div>

## 1의 거듭제곱근

거듭제곱근을 다루기 위한 첫 번째 재료는 1의 거듭제곱근들이다. 우선 다음의 일반적인 보조정리를 살펴보자.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Field $$\mathbb{K}$$의 multiplicative group $$\mathbb{K}^\times$$의 임의의 유한한 subgroup $$G$$는 cyclic group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$G$$의 원소들의 order들의 최소공배수를 $$n$$이라 하자. 우선 order가 $$n$$인 원소가 존재함을 보인다. 이를 위해 order가 각각 $$r,s$$인 $$x,y\in G$$에 대하여 order가 $$\lcm(r,s)$$인 원소가 존재함을 보이면, 이를 반복하여 원하는 원소를 얻는다.

$$\lcm(r,s)$$를 소인수분해하여 각 소인수의 거듭제곱 $$p^e$$마다, $$p^e$$가 $$r$$ 혹은 $$s$$를 나누므로 $$x^{r/p^e}$$ 혹은 $$y^{s/p^e}$$가 order $$p^e$$의 원소가 된다. 따라서 order가 서로소인 두 원소 $$u,v$$의 곱이 order $$\operatorname{ord}(u)\operatorname{ord}(v)$$를 갖는 것만 보이면 충분하다. $$G$$가 abelian이므로 $$(uv)^{\operatorname{ord}(u)\operatorname{ord}(v)}=e$$이고, 거꾸로 $$(uv)^k=e$$라면 $$u^k=v^{-k}\in\langle u\rangle\cap\langle v\rangle$$인데 이 교집합의 order는 [\[대수적 구조\] §몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups#prop5)에 의해 서로소인 $$\operatorname{ord}(u)$$와 $$\operatorname{ord}(v)$$를 모두 나누므로 $$1$$이다. 즉 $$u^k=v^k=e$$이고 $$\operatorname{ord}(u),\operatorname{ord}(v)$$가 모두 $$k$$를 나누므로 $$\operatorname{ord}(u)\operatorname{ord}(v)\mid k$$이다.

이제 $$G$$의 모든 원소는 $$x^n=1$$, 즉 다항식 $$\x^n-1$$의 근이다. Field 위에서 $$n$$차 다항식은 많아야 $$n$$개의 근을 가지므로 ([\[환론\] §다항식환, ⁋명제 9](/ko/math/ring_theory/polynomial_rings#prop9)) $$\card G\leq n$$이다. 한편 위에서 찾은 order $$n$$의 원소 $$a$$에 대하여 $$\langle a\rangle$$은 $$n$$개의 원소를 갖는 $$G$$의 subgroup이므로 $$G=\langle a\rangle$$이고, 즉 $$G$$는 cyclic이다.

</details>

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Field $$\mathbb{K}$$와 자연수 $$n\geq1$$에 대하여, $$\overline{\mathbb{K}}$$에서의 다항식 $$\x^n-1$$의 근들의 모임을 $$\mu_n$$으로 적고 그 원소들을 *1의 $$n$$제곱근<sub>$n$-th root of unity</sub>*이라 부른다. Group $$\mu_n$$의 generator를 *primitive $$n$$-th root of unity<sub>1의 원시 $n$제곱근</sub>*이라 부른다.

</div>

이 정의가 말이 되는 것을 확인하자. $$\mu_n$$이 $$\overline{\mathbb{K}}^\times$$의 subgroup인 것은 자명하다. 한편 $$\x^n-1$$의 derivative는 $$n\x^{n-1}$$이고, characteristic이 $$0$$이므로 이 둘은 공통근을 갖지 않는다. 따라서 [\[환론\] §다항식환, ⁋명제 11](/ko/math/ring_theory/polynomial_rings#prop11)에 의해 $$\x^n-1$$의 근들은 모두 simple root이고, $$\overline{\mathbb{K}}$$에서 $$\x^n-1$$이 일차식들로 쪼개지므로 $$\card\mu_n=n$$이다. 그럼 [보조정리 1](#lem1)에 의하여 $$\mu_n$$은 order $$n$$의 cyclic group이고, 특히 generator, 즉 primitive $$n$$-th root of unity $$\zeta$$가 존재한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Primitive $$n$$-th root of unity $$\zeta$$에 대하여, $$\mathbb{K}(\zeta)/\mathbb{K}$$는 finite degree Galois extension이고 그 Galois group은 abelian group $$(\mathbb{Z}/n\mathbb{Z})^\times$$의 subgroup과 isomorphic하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mu_n=\langle\zeta\rangle$$이므로 $$\mathbb{K}(\zeta)$$는 $$\x^n-1$$의 모든 근을 포함하고, 따라서 $$\x^n-1$$의 splitting field이다. 그럼 [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의해 $$\mathbb{K}(\zeta)/\mathbb{K}$$는 quasi-Galois이고, characteristic $$0$$ 가정에 의해 Galois이며, 하나의 algebraic element로 생성되므로 finite degree이다.

이제 임의의 $$\sigma\in\Gal(\mathbb{K}(\zeta)/\mathbb{K})$$에 대하여, $$\sigma$$는 $$\mu_n$$의 원소를 $$\mu_n$$의 원소로 보내고 group 연산을 보존하므로 cyclic group $$\mu_n$$의 automorphism을 유도한다. 그럼 $$\sigma(\zeta)$$도 $$\mu_n$$의 generator여야 하므로 $$n$$과 서로소인 $$a_\sigma$$에 대하여 $$\sigma(\zeta)=\zeta^{a_\sigma}$$로 쓸 수 있다. 대응 $$\sigma\mapsto a_\sigma$$가 group homomorphism

$$\Gal(\mathbb{K}(\zeta)/\mathbb{K}) \rightarrow (\mathbb{Z}/n\mathbb{Z})^\times$$

을 정의하는 것은 $$(\sigma\tau)(\zeta)=\sigma(\zeta^{a_\tau})=\zeta^{a_\sigma a_\tau}$$로부터 자명하고, $$\mathbb{K}(\zeta)$$가 $$\zeta$$로 생성되므로 $$\sigma$$는 $$\sigma(\zeta)$$에 의해 완전히 결정되어 이 homomorphism은 injective이다.

</details>

## 순환확대와 거듭제곱근

거듭제곱근을 하나 추가하는 extension과 cyclic Galois group을 갖는 extension이, 1의 거듭제곱근이 충분히 있다면 같은 것임을 살펴본다. 이번 절에서 $$\mathbb{K}$$는 primitive $$n$$-th root of unity $$\zeta$$를 포함한다고 가정한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$a\in\mathbb{K}^\times$$와, $$\alpha^n=a$$를 만족하는 $$\alpha\in\overline{\mathbb{K}}$$에 대하여 $$\mathbb{K}(\alpha)/\mathbb{K}$$는 finite degree Galois extension이고, 그 Galois group은 $$n$$을 나누는 order의 cyclic group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

다항식 $$\x^n-a$$의 근들은 정확히 $$\zeta^i\alpha$$ ($$i=0,\ldots,n-1$$)들이고 ($$n$$개의 서로 다른 원소들이 모두 근이며 근은 많아야 $$n$$개이므로), $$\zeta\in\mathbb{K}$$이므로 이들이 모두 $$\mathbb{K}(\alpha)$$에 속한다. 즉 $$\mathbb{K}(\alpha)$$는 $$\x^n-a$$의 splitting field이고, [명제 3](#prop3)의 증명에서와 같이 finite degree Galois extension이다.

이제 임의의 $$\sigma\in\Gal(\mathbb{K}(\alpha)/\mathbb{K})$$에 대하여 $$\sigma(\alpha)$$도 $$\x^n-a$$의 근이므로 $$\sigma(\alpha)/\alpha\in\mu_n$$이다. 대응 $$\sigma\mapsto\sigma(\alpha)/\alpha$$를 생각하면, $$\mu_n\subseteq\mathbb{K}$$가 $$\sigma$$들에 의해 고정되므로

$$(\sigma\tau)(\alpha)/\alpha=\sigma\bigl(\tau(\alpha)/\alpha\bigr)\cdot\sigma(\alpha)/\alpha=\bigl(\tau(\alpha)/\alpha\bigr)\bigl(\sigma(\alpha)/\alpha\bigr)$$

이 되어 이는 group homomorphism $$\Gal(\mathbb{K}(\alpha)/\mathbb{K}) \rightarrow \mu_n$$이고, $$\sigma$$가 $$\sigma(\alpha)$$로 결정되므로 injective이다. 따라서 Galois group은 cyclic group $$\mu_n$$의 subgroup과 isomorphic하고, [\[대수적 구조\] §몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups#prop5)에 의해 그 order는 $$n$$을 나눈다.

</details>

핵심은 다음의 역방향으로, 그 증명에 사용되는 $$\alpha$$를 *Lagrange resolvent*라 부른다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> $$\mathbb{L}/\mathbb{K}$$가 degree $$n$$의 Galois extension이고 $$\Gal(\mathbb{L}/\mathbb{K})$$가 cyclic group이라 하자. 그럼 ($$\zeta\in\mathbb{K}$$ 가정 하에) 적당한 $$\alpha\in\mathbb{L}$$가 존재하여 $$\mathbb{L}=\mathbb{K}(\alpha)$$이고 $$\alpha^n\in\mathbb{K}$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Gal(\mathbb{L}/\mathbb{K})$$의 generator를 $$\sigma$$라 하자. [§갈루아 이론의 기본정리](/ko/math/field_theory/fundamental_theorem_of_galois_theory)의 마지막에 언급한 counting에 의하여 $$\card\Gal(\mathbb{L}/\mathbb{K})=[\mathbb{L}:\mathbb{K}]=n$$이고, 따라서 $$\id,\sigma,\sigma^2,\ldots,\sigma^{n-1}$$은 $$\mathbb{L}$$에서 $$\mathbb{L}$$로의 서로 다른 homomorphism들이다. [§에탈대수, ⁋따름정리 3](/ko/math/field_theory/etale_algebras#cor3)의 Dedekind 정리에 의하여 이들은 $$\mathbb{L}$$-벡터공간 안에서 일차독립이므로, 일차결합

$$\id+\zeta\sigma+\zeta^2\sigma^2+\cdots+\zeta^{n-1}\sigma^{n-1}$$

은 zero map이 아니다. 즉 적당한 $$x\in\mathbb{L}$$에 대하여

$$\alpha=x+\zeta\sigma(x)+\zeta^2\sigma^2(x)+\cdots+\zeta^{n-1}\sigma^{n-1}(x)\neq0$$

이다. 이제 $$\zeta\in\mathbb{K}$$가 $$\sigma$$에 의해 고정된다는 것과 $$\sigma^n=\id$$로부터

$$\sigma(\alpha)=\sigma(x)+\zeta\sigma^2(x)+\cdots+\zeta^{n-1}x=\zeta^{-1}\bigl(\zeta\sigma(x)+\zeta^2\sigma^2(x)+\cdots+\zeta^{n-1}\sigma^{n-1}(x)+x\bigr)=\zeta^{-1}\alpha$$

를 얻는다. 따라서 $$\sigma(\alpha^n)=\zeta^{-n}\alpha^n=\alpha^n$$이고, $$\alpha^n$$은 $$\Gal(\mathbb{L}/\mathbb{K})=\langle\sigma\rangle$$ 전체에 의해 고정되므로 $$\mathbb{L}/\mathbb{K}$$가 Galois라는 것으로부터 $$\alpha^n\in\mathbb{K}$$이다.

마지막으로 $$\sigma^i(\alpha)=\zeta^{-i}\alpha$$들은 서로 다른 $$n$$개의 원소들이므로, $$\alpha$$는 $$\mathbb{K}(\alpha)$$ 위에서 적어도 $$n$$개의 conjugate을 갖고 따라서 $$[\mathbb{K}(\alpha):\mathbb{K}]\geq n$$이다. $$\mathbb{K}(\alpha)\subseteq\mathbb{L}$$이고 $$[\mathbb{L}:\mathbb{K}]=n$$이므로 $$\mathbb{L}=\mathbb{K}(\alpha)$$이다.

</details>

## 거듭제곱근 가해성

이제 이번 글의 주인공을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Field들의 chain

$$\mathbb{K}=\mathbb{K}_0\subseteq\mathbb{K}_1\subseteq\cdots\subseteq\mathbb{K}_r$$

이 *거듭제곱근 탑<sub>radical tower</sub>*이라는 것은 각각의 $$i$$마다 적당한 $$\alpha_i\in\mathbb{K}_{i+1}$$와 자연수 $$n_i\geq1$$이 존재하여 $$\mathbb{K}_{i+1}=\mathbb{K}_i(\alpha_i)$$이고 $$\alpha_i^{n_i}\in\mathbb{K}_i$$인 것이다. 다항식 $$f\in\mathbb{K}[\x]$$가 *거듭제곱근으로 풀린다<sub>solvable by radicals</sub>*는 것은 $$f$$의 splitting field $$\mathbb{L}_f$$가 어떤 거듭제곱근 탑의 가장 위의 field $$\mathbb{K}_r$$에 포함되는 것이다.

</div>

즉 $$f$$가 거듭제곱근으로 풀린다는 것은, $$f$$의 모든 근을 $$\mathbb{K}$$의 원소들로부터 시작하여 사칙연산과 거듭제곱근을 유한 번 취하는 것으로 표현할 수 있다는 것이다.

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> 여기서의 radical tower는 [§제곱근확대체](/ko/math/field_theory/radical_extensions)의 $$p$$-radical extension과는 별개의 개념이다. 후자는 characteristic $$p$$에서 Frobenius와 관련된 inseparability를 다루는 개념이고, 전자는 임의의 거듭제곱근을 추가하는 조작이다. 영문 문헌에서 둘 모두 radical이라는 단어를 사용하므로 주의해야 한다.

</div>

다음의 군론적 보조정리들을 준비하자. 가해군의 정의와 기본 성질은 [\[군론\] §군의 열](/ko/math/group_theory/series_of_groups)에서 가져온다.

<div class="proposition" markdown="1">

<ins id="lem8">**보조정리 8**</ins> Solvable group의 subgroup과 quotient group은 solvable이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Derived series를 $$D_n$$으로 적자. $$H\leq G$$에 대하여 inclusion $$H \hookrightarrow G$$에 [\[군론\] §군의 열, ⁋명제 10](/ko/math/group_theory/series_of_groups#prop10)을 적용하면 $$D_n(H)\subseteq D_n(G)$$이므로, $$D_{n+1}(G)=\{e\}$$라면 $$D_{n+1}(H)=\{e\}$$이다. 한편 surjection $$\pi:G \rightarrow Q$$에 대하여 같은 명제에 의해 $$D_n(Q)=\pi(D_n(G))$$이므로 $$D_{n+1}(G)=\{e\}$$라면 $$D_{n+1}(Q)=\{e\}$$이다. ([\[군론\] §군의 열, ⁋정의 11](/ko/math/group_theory/series_of_groups#def11))

</details>

<div class="proposition" markdown="1">

<ins id="lem9">**보조정리 9**</ins> 유한한 solvable group $$G$$는 모든 quotient가 cyclic인 subnormal series

$$G=H_0\supseteq H_1\supseteq\cdots\supseteq H_r=\{e\}$$

를 갖는다. 즉 각각의 $$H_{i+1}$$은 $$H_i$$의 normal subgroup이고 $$H_i/H_{i+1}$$은 cyclic group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 유한한 abelian group $$A$$가 이러한 series를 갖는 것을 $$\card A$$에 대한 귀납법으로 보이자. $$A$$가 trivial이면 자명하다. 그렇지 않다면 $$e$$가 아닌 원소 $$a\in A$$를 택하고 quotient $$A/\langle a\rangle$$을 생각하면, 귀납가정에 의해 $$A/\langle a\rangle$$은 cyclic quotient들을 갖는 series를 갖고, 몫군의 subgroup correspondence로 이를 $$A$$의 series로 끌어올린 후 마지막에 $$\langle a\rangle\supseteq\{e\}$$를 붙이면 된다. $$A$$가 abelian이므로 모든 subgroup이 normal이고, 끌어올린 series의 quotient들은 원래 series의 quotient들과 isomorphic하다.

이제 일반적인 solvable group $$G$$에 대하여, derived series

$$G=D_1(G)\supseteq D_2(G)\supseteq\cdots\supseteq D_{n+1}(G)=\{e\}$$

를 생각하면 각 quotient $$D_k(G)/D_{k+1}(G)$$는 abelian이다. 각각의 단계를 위에서 살펴본 abelian group의 series로 refine하자. 즉 $$D_k(G)/D_{k+1}(G)$$의 cyclic quotient들을 갖는 series를 correspondence로 끌어올려 $$D_k(G)$$와 $$D_{k+1}(G)$$ 사이의 중간 subgroup들로 바꾸면, 이들 중간 subgroup들은 abelian quotient $$D_k(G)/D_{k+1}(G)$$의 subgroup들에 대응되므로 각각이 바로 앞의 것의 normal subgroup이고, 연이은 quotient들이 cyclic이다. 이렇게 모든 단계를 refine하면 원하는 series를 얻는다.

</details>

이제 갈루아의 정리를 증명할 준비가 되었다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (Galois)**</ins> Characteristic $$0$$의 field $$\mathbb{K}$$와 다항식 $$f\in\mathbb{K}[\x]$$, 그리고 $$f$$의 splitting field $$\mathbb{L}_f$$에 대하여, 다음이 동치이다.

1. $$f$$가 거듭제곱근으로 풀린다.
2. $$\Gal(\mathbb{L}_f/\mathbb{K})$$가 solvable group이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\mathbb{L}_f/\mathbb{K}$$는 splitting field이므로 quasi-Galois이고 ([§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)), characteristic $$0$$이므로 finite degree Galois extension이다.

**(2)$$\implies$$(1)** $$G=\Gal(\mathbb{L}_f/\mathbb{K})$$가 solvable이라 하고 $$n=\card G$$로 두자. Primitive $$n$$-th root of unity $$\zeta$$를 택하고 $$\mathbb{K}'=\mathbb{K}(\zeta)$$, $$\mathbb{L}'=\mathbb{L}_f(\zeta)$$라 하자. $$\mathbb{L}'$$은 $$\mathbb{K}'$$ 위에서의 $$f$$의 splitting field이므로 $$\mathbb{L}'/\mathbb{K}'$$도 finite degree Galois extension이다.

우선 $$H=\Gal(\mathbb{L}'/\mathbb{K}')$$가 solvable임을 보이자. 임의의 $$\sigma\in H$$에 대하여 $$\sigma$$는 $$\mathbb{K}$$를 고정하고, $$\mathbb{L}_f/\mathbb{K}$$가 quasi-Galois이므로 [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의해 $$\sigma(\mathbb{L}_f)=\mathbb{L}_f$$이다. 따라서 restriction homomorphism $$H \rightarrow G$$가 잘 정의되며, $$\sigma\in H$$가 $$\mathbb{L}_f$$를 고정한다면 $$\zeta\in\mathbb{K}'$$도 고정하므로 $$\mathbb{L}'=\mathbb{K}'(\mathbb{L}_f)$$ 전체를 고정한다. 즉 이 restriction은 injective이고, $$H$$는 solvable group $$G$$의 subgroup과 isomorphic하므로 [보조정리 8](#lem8)에 의해 solvable이다.

이제 [보조정리 9](#lem9)에 의하여 모든 quotient가 cyclic인 series $$H=H_0\supseteq\cdots\supseteq H_r=\{e\}$$가 존재한다. $$\mathbb{L}'/\mathbb{K}'$$가 finite degree Galois이므로 $$\Gal(\mathbb{L}'/\mathbb{K}')$$는 discrete group이고 모든 subgroup이 closed이다. 따라서 [§갈루아 이론의 기본정리, ⁋정리 1](/ko/math/field_theory/fundamental_theorem_of_galois_theory#thm1)의 대응으로 fixed field들

$$\mathbb{K}'=\mathbb{F}_0\subseteq\mathbb{F}_1\subseteq\cdots\subseteq\mathbb{F}_r=\mathbb{L}',\qquad \mathbb{F}_i=\mathbb{L}'^{H_i}$$

을 얻는다. 각각의 $$i$$에 대하여 [§갈루아 이론의 기본정리, ⁋보조정리 2](/ko/math/field_theory/fundamental_theorem_of_galois_theory#lem2)에 의해 $$\mathbb{L}'/\mathbb{F}_{i-1}$$은 Galois extension이고 그 Galois group은 $$H_{i-1}$$이며, $$H_i$$가 $$H_{i-1}$$의 normal subgroup이므로 [§갈루아 이론의 기본정리, ⁋따름정리 4](/ko/math/field_theory/fundamental_theorem_of_galois_theory#cor4)에 의하여 $$\mathbb{F}_i/\mathbb{F}_{i-1}$$은 Galois extension이고

$$\Gal(\mathbb{F}_i/\mathbb{F}_{i-1})\cong H_{i-1}/H_i$$

는 cyclic group이다. 그 order를 $$d_i$$라 하면 [\[대수적 구조\] §몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups#prop5)에 의해 $$d_i$$는 $$\card H$$를 나누고, 다시 $$\card H$$는 $$n$$을 나눈다. 따라서 $$\zeta^{n/d_i}$$는 primitive $$d_i$$-th root of unity이고 $$\mathbb{K}'\subseteq\mathbb{F}_{i-1}$$에 속하므로, [명제 5](#prop5)에 의하여 $$\mathbb{F}_i=\mathbb{F}_{i-1}(\alpha_i)$$, $$\alpha_i^{d_i}\in\mathbb{F}_{i-1}$$이도록 하는 $$\alpha_i$$가 존재한다.

종합하면 $$\zeta^n=1\in\mathbb{K}$$이므로

$$\mathbb{K}\subseteq\mathbb{K}(\zeta)=\mathbb{F}_0\subseteq\mathbb{F}_1\subseteq\cdots\subseteq\mathbb{F}_r=\mathbb{L}'$$

은 거듭제곱근 탑이고, $$\mathbb{L}_f\subseteq\mathbb{L}'$$이므로 $$f$$는 거듭제곱근으로 풀린다.

**(1)$$\implies$$(2)** 거듭제곱근 탑 $$\mathbb{K}=\mathbb{K}_0\subseteq\cdots\subseteq\mathbb{K}_r$$이 $$\mathbb{L}_f\subseteq\mathbb{K}_r$$을 만족한다 하고, 그 데이터를 $$\mathbb{K}_{i+1}=\mathbb{K}_i(\alpha_i)$$, $$\alpha_i^{n_i}\in\mathbb{K}_i$$라 하자. $$n=n_0n_1\cdots n_{r-1}$$로 두고 primitive $$n$$-th root of unity $$\zeta$$를 택하자.

우선 탑을 키워 Galois extension으로 만든다. $$E=\mathbb{K}_r(\zeta)$$로 두면

$$\mathbb{K}\subseteq\mathbb{K}(\zeta)\subseteq\mathbb{K}_1(\zeta)\subseteq\cdots\subseteq\mathbb{K}_r(\zeta)=E$$

는 다시 거듭제곱근 탑이고 ($$\zeta^n=1\in\mathbb{K}$$, 그리고 각 단계는 $$\alpha_i$$를 추가하는 것), $$E/\mathbb{K}$$는 finite degree extension이다. $$u_1=\id,u_2,\ldots,u_s$$를 $$E$$에서 $$\overline{\mathbb{K}}$$로의 서로 다른 $$\mathbb{K}$$-homomorphism들 전부라 하자. 이들은 유한 개인데, 그 개수가 separable degree $$[E:\mathbb{K}]_s$$와 같기 때문이다. ([§에탈대수, ⁋정의 10](/ko/math/field_theory/etale_algebras#def10)) 이제

$$\mathbb{N}=\mathbb{K}\bigl(u_1(E)\cup\cdots\cup u_s(E)\bigr)$$

으로 정의하자. $$\overline{\mathbb{K}}$$의 임의의 $$\mathbb{K}$$-automorphism $$v$$에 대하여 $$v\circ u_j$$들도 $$E$$에서 $$\overline{\mathbb{K}}$$로의 $$\mathbb{K}$$-homomorphism들이므로 $$v$$는 $$u_j(E)$$들을 permute하고, 따라서 $$v(\mathbb{N})=\mathbb{N}$$이다. 즉 [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의해 $$\mathbb{N}/\mathbb{K}$$는 quasi-Galois이고, characteristic $$0$$이므로 finite degree Galois extension이다.

다음으로 $$\mathbb{N}$$도 거듭제곱근 탑을 갖는다는 것을 확인하자. 각각의 $$u_j$$에 대하여 $$u_j(E)$$는 $$\mathbb{K}$$ 위에서 원소들 $$u_j(\zeta),u_j(\alpha_0),\ldots,u_j(\alpha_{r-1})$$로 생성되는데, $$u_j(\zeta)\in\mu_n$$이고

$$u_j(\alpha_i)^{n_i}=u_j(\alpha_i^{n_i})\in u_j(\mathbb{K}_i(\zeta))=\mathbb{K}\bigl(u_j(\zeta),u_j(\alpha_0),\ldots,u_j(\alpha_{i-1})\bigr)$$

이다. 따라서 $$\mathbb{K}(\zeta)$$에서 시작하여 $$u_1(E)$$의 생성원들, $$u_2(E)$$의 생성원들, $$\ldots$$을 차례로 추가하면, 각 단계에서 추가되는 원소의 거듭제곱이 항상 그 이전까지 만들어진 field에 속하므로 ($$u_j(\zeta)\in\mu_n=\langle\zeta\rangle\subseteq\mathbb{K}(\zeta)$$이고 위의 식), 이는 $$\mathbb{K}$$에서 $$\mathbb{N}$$까지의 거듭제곱근 탑

$$\mathbb{K}\subseteq\mathbb{K}(\zeta)=\mathbb{T}_1\subseteq\mathbb{T}_2\subseteq\cdots\subseteq\mathbb{T}_t=\mathbb{N}$$

이 된다. 여기서 각 단계 $$\mathbb{T}_{k+1}=\mathbb{T}_k(\beta_k)$$에서 $$\beta_k^{d_k}\in\mathbb{T}_k$$이고 $$d_k$$는 어떤 $$n_i$$이므로 $$n$$을 나눈다.

이제 $$\Gal(\mathbb{N}/\mathbb{K})$$가 solvable임을 보이자. Subgroup들 $$G_k=\Gal(\mathbb{N}/\mathbb{T}_k)$$를 생각하면 ([§갈루아 이론의 기본정리, ⁋보조정리 2](/ko/math/field_theory/fundamental_theorem_of_galois_theory#lem2)) 다음의 decreasing sequence

$$\Gal(\mathbb{N}/\mathbb{K})=G_0\supseteq G_1\supseteq\cdots\supseteq G_t=\{e\}$$

를 얻는다. 첫 단계 $$\mathbb{T}_1=\mathbb{K}(\zeta)$$는 [명제 3](#prop3)에 의해 $$\mathbb{K}$$의 Galois extension이고 그 Galois group이 abelian이며, $$k\geq1$$인 단계 $$\mathbb{T}_{k+1}=\mathbb{T}_k(\beta_k)$$는 $$\zeta^{n/d_k}\in\mathbb{T}_1\subseteq\mathbb{T}_k$$가 primitive $$d_k$$-th root of unity이므로 [명제 4](#prop4)에 의해 $$\mathbb{T}_k$$의 Galois extension이고 그 Galois group이 cyclic이다. 그럼 각각의 $$k$$에 대하여 [§갈루아 이론의 기본정리, ⁋따름정리 4](/ko/math/field_theory/fundamental_theorem_of_galois_theory#cor4)를 Galois extension $$\mathbb{N}/\mathbb{T}_k$$에 적용하면, $$G_{k+1}$$은 $$G_k$$의 normal subgroup이고

$$G_k/G_{k+1}\cong\Gal(\mathbb{T}_{k+1}/\mathbb{T}_k)$$

는 abelian이다. 따라서 [\[군론\] §군의 열, ⁋명제 12](/ko/math/group_theory/series_of_groups#prop12)에 의하여 $$\Gal(\mathbb{N}/\mathbb{K})$$는 solvable group이다.

마지막으로 $$\mathbb{L}_f\subseteq E\subseteq\mathbb{N}$$이고 $$\mathbb{L}_f/\mathbb{K}$$가 Galois이므로, [§갈루아 확장, ⁋명제 13](/ko/math/field_theory/galois_extension#prop13)에 의하여 restriction $$\Gal(\mathbb{N}/\mathbb{K}) \rightarrow \Gal(\mathbb{L}_f/\mathbb{K})$$이 surjective이다. 즉 $$\Gal(\mathbb{L}_f/\mathbb{K})$$는 solvable group의 quotient이므로 [보조정리 8](#lem8)에 의해 solvable이다.

</details>

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> [정리 10](#thm10)으로부터 5차 이상의 일반 방정식에 대한 근의 공식이 존재하지 않는다는 Abel–Ruffini 정리가 따라나온다. 실제로 $$S_5$$는 solvable이 아닌데, 만일 solvable이라면 [보조정리 8](#lem8)에 의해 그 subgroup $$A_5$$도 solvable이어야 하지만, $$A_5$$는 abelian이 아닌 simple group이므로 ([\[군론\] §대칭군, ⁋예시 13](/ko/math/group_theory/symmetric_groups#ex13)) derived subgroup이 자명해질 수 없기 때문이다. 따라서 Galois group이 $$S_5$$가 되는 다항식, 가령 $$\mathbb{Q}$$ 위의 적당한 5차 다항식은 거듭제곱근으로 풀리지 않는다. 구체적인 다항식의 Galois group을 계산하는 일은 그 자체로 별도의 주제이므로 여기서 다루지는 않는다.

</div>

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  
**[Lan]** S. Lang. *Algebra*. Graduate texts in mathematics. Springer, 2002.

---
