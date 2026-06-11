---
title: "군 코호몰로지"
description: "군환 위의 가군으로서의 G-가군을 정의하고, bar resolution을 통해 군 코호몰로지를 계산 가능한 형태로 옮긴 후 낮은 차수에서의 해석과 순환군의 코호몰로지를 다룬다."
excerpt: "G-module의 invariant functor의 derived functor"

categories: [Math / Homological Algebra]
permalink: /ko/math/homological_algebra/group_cohomology
sidebar: 
    nav: "homological_algebra-ko"

date: 2026-06-11
last_modified_at: 2026-06-11
weight: 9
published: false

---

지금까지 우리는 derived functor의 일반론을 만들고 ([§유도함자](/ko/math/homological_algebra/derived_functors)), 그 대표적인 예시로 $$\Ext$$와 $$\Tor$$를 살펴보았다 ([§Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)). 이번 글에서는 이 기계를 group에 적용한다. Group $$G$$가 abelian group에 작용하는 상황은 수학 전반에서 등장하는데, 이 때 가장 기본적인 조작인 "$$G$$-invariant들을 취하는 것"은 exact functor가 아니다. 군 코호몰로지는 정확히 이 functor의 derived functor이다.

## G-가군

Group $$G$$를 고정하자. [\[대수적 구조\] §대수, ⁋정의 5](/ko/math/algebraic_structures/algebras#def5)에서 살펴본 group ring $$\mathbb{Z}G$$를 생각하면, $$\mathbb{Z}G$$는 $$G$$의 원소들을 basis로 갖는 free abelian group에 $$G$$의 곱셈을 선형으로 확장한 곱을 준 ring이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *$$G$$-module<sub>$G$-가군</sub>*은 left $$\mathbb{Z}G$$-module을 뜻한다. $$G$$-module $$M$$의 *invariant submodule<sub>불변 부분가군</sub>*은 다음의 집합

$$M^G=\left\{m\in M\mid \text{$g\cdot m=m$ for all $g\in G$}\right\}$$

으로 정의된다.

</div>

$$G$$-module 구조를 푸는 것은 어렵지 않다. Abelian group $$M$$ 위의 $$\mathbb{Z}G$$-module 구조는 $$G$$의 각 원소가 $$M$$에 어떻게 작용하는지로 결정되고, 각각의 $$g\in G$$의 작용은 $$M$$의 automorphism이며 ($$g^{-1}$$의 작용이 역함수), 작용이 곱셈과 호환되어야 하므로 이는 정확히 group homomorphism $$G \rightarrow \Aut(M)$$을 주는 것과 같다. 특히 임의의 abelian group은 모든 $$g\in G$$가 identity로 작용하는 *trivial $$G$$-module* 구조를 갖는다. 앞으로 $$\mathbb{Z}$$는 항상 trivial $$G$$-module로 생각하며, ring homomorphism

$$\varepsilon:\mathbb{Z}G \rightarrow \mathbb{Z};\qquad \sum_{g\in G}a_g\,g\mapsto\sum_{g\in G}a_g$$

를 *augmentation map*이라 부른다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 $$G$$-module $$M$$에 대하여, 다음의 두 함수

$$\Hom_{\lMod{\mathbb{Z}G}}(\mathbb{Z},M) \rightarrow M^G;\quad \varphi\mapsto\varphi(1),\qquad M^G \rightarrow \Hom_{\lMod{\mathbb{Z}G}}(\mathbb{Z},M);\quad m\mapsto(n\mapsto nm)$$

는 서로의 역함수인 isomorphism들이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 $$\varphi\in\Hom_{\lMod{\mathbb{Z}G}}(\mathbb{Z},M)$$에 대하여, $$\mathbb{Z}$$ 위에서 $$g$$가 trivial하게 작용하므로

$$g\cdot\varphi(1)=\varphi(g\cdot 1)=\varphi(1)$$

이 되어 $$\varphi(1)\in M^G$$이다. 거꾸로 $$m\in M^G$$에 대하여 $$\varphi_m(n)=nm$$으로 정의하면, 임의의 $$x=\sum a_gg\in\mathbb{Z}G$$에 대하여 $$x\cdot n=\varepsilon(x)n$$이고

$$\varphi_m(x\cdot n)=\varepsilon(x)nm=\sum_ga_g(nm)=x\cdot(nm)=x\cdot\varphi_m(n)$$

이다. 마지막 등식에서 $$m$$이 invariant라는 가정이 사용되었다. 즉 $$\varphi_m$$은 $$\mathbb{Z}G$$-linear이다. 두 함수가 서로의 역함수인 것과 abelian group homomorphism인 것은 자명하다.

</details>

즉 invariant들을 취하는 functor $$M\mapsto M^G$$는 $$\Hom_{\lMod{\mathbb{Z}G}}(\mathbb{Z},-)$$와 같은 functor이고, 특히 left exact이다. 따라서 다음의 정의가 자연스럽다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Group $$G$$와 $$G$$-module $$M$$에 대하여, $$G$$의 $$M$$에서의 계수를 갖는 *군 코호몰로지<sub>group cohomology</sub>*는 다음의 식

$$H^n(G;M)=\Ext^n_{\mathbb{Z}G}(\mathbb{Z},M)$$

으로 정의된다. ([§Ext와 Tor, ⁋정의 1](/ko/math/homological_algebra/ext_and_tor#def1))

</div>

정의와 [명제 2](#prop2)에 의하여 $$H^0(G;M)=M^G$$이고, $$G$$-module들의 short exact sequence는 군 코호몰로지의 long exact sequence를 유도한다.

## 표준 분해

[§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에 의하여 $$\Ext^n_{\mathbb{Z}G}(\mathbb{Z},M)$$은 $$\mathbb{Z}$$의 projective resolution을 하나 고정하여 계산할 수 있다. 군 코호몰로지가 쓸모있는 이유는 모든 group에 대해 일괄적으로 작동하는 표준적인 resolution이 있기 때문이다.

각각의 $$n\geq0$$에 대하여, $$B_n$$을 기호들 $$[g_1\mid g_2\mid\cdots\mid g_n]$$ ($$g_i\in G$$)을 basis로 갖는 free $$\mathbb{Z}G$$-module이라 하자. $$n=0$$일 때는 빈 기호 $$[\ ]$$ 하나가 basis이므로 $$B_0=\mathbb{Z}G$$이다. 이제 $$\mathbb{Z}G$$-linear map $$d_n:B_n \rightarrow B_{n-1}$$을 basis 위에서 다음의 식

$$d_n[g_1\mid\cdots\mid g_n]=g_1[g_2\mid\cdots\mid g_n]+\sum_{i=1}^{n-1}(-1)^i[g_1\mid\cdots\mid g_ig_{i+1}\mid\cdots\mid g_n]+(-1)^n[g_1\mid\cdots\mid g_{n-1}]$$

으로 정의한다. 가령 $$d_1[g]=g[\ ]-[\ ]=g-1$$이고, $$d_2[g\mid h]=g[h]-[gh]+[g]$$이다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4**</ins> 위의 데이터는 trivial $$G$$-module $$\mathbb{Z}$$의 free resolution

$$\cdots\longrightarrow B_2\overset{d_2}{\longrightarrow}B_1\overset{d_1}{\longrightarrow}B_0\overset{\varepsilon}{\longrightarrow}\mathbb{Z}\longrightarrow0$$

을 이룬다. 이를 $$G$$의 *bar resolution*이라 부른다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $$B_n$$은 free $$\mathbb{Z}G$$-module이므로 projective이다. ([\[다중선형대수학\] §사영가군, 단사가군, 평탄가군, ⁋명제 4](/ko/math/multilinear_algebra/various_modules#prop4))

위의 sequence가 chain complex를 이루고 exact라는 것을 한 번에 보이기 위해 contracting homotopy를 만든다. $$B_n$$은 abelian group으로서는 원소들 $$g_0[g_1\mid\cdots\mid g_n]$$ ($$g_0,\ldots,g_n\in G$$)을 basis로 가지므로, $$\mathbb{Z}$$-linear map $$h_n:B_n \rightarrow B_{n+1}$$을

$$h_n\bigl(g_0[g_1\mid\cdots\mid g_n]\bigr)=[g_0\mid g_1\mid\cdots\mid g_n]$$

으로, $$h_{-1}:\mathbb{Z} \rightarrow B_0$$를 $$h_{-1}(1)=[\ ]=1$$로 정의하자. $$h_n$$들은 $$\mathbb{Z}G$$-linear가 아니라는 것에 주의하라.

우선 $$\varepsilon\circ h_{-1}=\id_\mathbb{Z}$$는 자명하다. 다음으로 $$d_1h_0(g_0)+h_{-1}\varepsilon(g_0)=(g_0-1)+1=g_0$$이므로 degree $$0$$에서 $$d_1h_0+h_{-1}\varepsilon=\id_{B_0}$$이다. 이제 $$n\geq1$$에서 $$d_{n+1}h_n+h_{n-1}d_n=\id_{B_n}$$임을 basis 원소 $$g_0[g_1\mid\cdots\mid g_n]$$ 위에서 확인하자. 한편으로

$$d_{n+1}[g_0\mid\cdots\mid g_n]=g_0[g_1\mid\cdots\mid g_n]+\sum_{i=1}^n(-1)^i[g_0\mid\cdots\mid g_{i-1}g_i\mid\cdots\mid g_n]+(-1)^{n+1}[g_0\mid\cdots\mid g_{n-1}]$$

이다. 다른 한편으로 $$d_n$$이 $$\mathbb{Z}G$$-linear이므로

$$d_n\bigl(g_0[g_1\mid\cdots\mid g_n]\bigr)=(g_0g_1)[g_2\mid\cdots\mid g_n]+\sum_{i=1}^{n-1}(-1)^ig_0[g_1\mid\cdots\mid g_ig_{i+1}\mid\cdots\mid g_n]+(-1)^ng_0[g_1\mid\cdots\mid g_{n-1}]$$

이고, 여기에 $$h_{n-1}$$을 적용하면

$$h_{n-1}d_n\bigl(g_0[g_1\mid\cdots\mid g_n]\bigr)=[g_0g_1\mid g_2\mid\cdots\mid g_n]+\sum_{i=1}^{n-1}(-1)^i[g_0\mid g_1\mid\cdots\mid g_ig_{i+1}\mid\cdots\mid g_n]+(-1)^n[g_0\mid\cdots\mid g_{n-1}]$$

이다. 첫 식의 합에서 $$i=1$$ 항은 $$-[g_0g_1\mid g_2\mid\cdots\mid g_n]$$이고 $$i\geq2$$ 항들은 index를 $$j=i-1$$로 바꾸면 $$(-1)^{j+1}[g_0\mid\cdots\mid g_jg_{j+1}\mid\cdots\mid g_n]$$들이므로, 두 식을 더하면 첫 항 $$g_0[g_1\mid\cdots\mid g_n]$$만 남고 나머지가 모두 소거된다. 즉

$$d_{n+1}h_n+h_{n-1}d_n=\id_{B_n}$$

이다.

우선 위의 homotopy 항등식으로부터 $$d_nd_{n+1}=0$$을 확인하자. $$B_{n+1}$$이 abelian group으로서 $$h_n$$의 image로 생성되므로 ($$[g_0\mid\cdots\mid g_n]=h_n(g_0[g_1\mid\cdots\mid g_n])$$이고 $$d$$들은 additive이다) $$d_nd_{n+1}h_n=0$$만 보이면 충분하다. Homotopy 항등식을 두 번 적용하면

$$d_nd_{n+1}h_n=d_n(\id_{B_n}-h_{n-1}d_n)=d_n-(d_nh_{n-1})d_n=d_n-(\id_{B_{n-1}}-h_{n-2}d_{n-1})d_n=h_{n-2}d_{n-1}d_n$$

이므로, $$n$$에 대한 귀납법에 의해 $$d_{n-1}d_n=0$$이면 $$d_nd_{n+1}=0$$이다. 귀납법의 시작은 $$d_1d_2h_1=d_1-(d_1h_0)d_1=d_1-(\id_{B_0}-h_{-1}\varepsilon)d_1=h_{-1}(\varepsilon d_1)$$과 $$\varepsilon d_1[g]=\varepsilon(g-1)=0$$으로부터 얻어진다.

이제 exactness가 따라나온다. $$\varepsilon$$은 surjective이고, $$z\in B_n$$ ($$n\geq1$$)이 $$d_n(z)=0$$을 만족한다면 $$z=d_{n+1}(h_n(z))+h_{n-1}(d_n(z))=d_{n+1}(h_n(z))$$이므로 $$z\in\im d_{n+1}$$이다. Degree $$0$$에서도 $$\varepsilon(z)=0$$이라면 $$z=d_1(h_0(z))$$이다.

</details>

이제 $$\Hom_{\lMod{\mathbb{Z}G}}(-,M)$$을 bar resolution에 적용하자. $$B_n$$이 $$G^n$$으로 index되는 basis를 갖는 free module이므로

$$C^n(G;M)=\Hom_{\lMod{\mathbb{Z}G}}(B_n,M)\cong\left\{\text{함수 $\varphi:G^n \rightarrow M$}\right\}$$

이고, 위의 $$d_{n+1}$$이 유도하는 differential은

$$(d\varphi)(g_1,\ldots,g_{n+1})=g_1\cdot\varphi(g_2,\ldots,g_{n+1})+\sum_{i=1}^n(-1)^i\varphi(g_1,\ldots,g_ig_{i+1},\ldots,g_{n+1})+(-1)^{n+1}\varphi(g_1,\ldots,g_n)$$

으로 주어진다. [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에 의하여 $$H^n(G;M)$$은 이 cochain complex의 cohomology이다. 이 함수들을 *$$n$$-cochain*이라 부르고, $$\ker d$$와 $$\im d$$의 원소들을 각각 *$$n$$-cocycle*, *$$n$$-coboundary*라 부른다.

## 낮은 차수에서의 해석

차수가 낮을 때는 위의 cochain complex를 손으로 읽을 수 있다. $$n=0$$일 때 $$C^0(G;M)=M$$이고 $$(d m)(g)=g\cdot m-m$$이므로 $$H^0(G;M)=M^G$$를 다시 얻는다. $$n=1$$일 때 cocycle 조건은

$$(d\varphi)(g,h)=g\cdot\varphi(h)-\varphi(gh)+\varphi(g)=0$$

이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 함수 $$\varphi:G \rightarrow M$$이 *crossed homomorphism<sub>꼬인 준동형사상</sub>*이라는 것은 임의의 $$g,h\in G$$에 대하여

$$\varphi(gh)=g\cdot\varphi(h)+\varphi(g)$$

가 성립하는 것이다. 특별히 어떤 $$m\in M$$에 대하여 $$\varphi(g)=g\cdot m-m$$의 꼴로 쓰여지는 crossed homomorphism을 *principal*하다고 말한다.

</div>

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$H^1(G;M)$$은 crossed homomorphism들의 group을 principal crossed homomorphism들의 subgroup으로 나눈 quotient와 isomorphic하다. 특히 $$G$$가 $$M$$에 trivial하게 작용한다면 $$H^1(G;M)\cong\Hom_{\Grp}(G,M)$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

위에서 계산한 cocycle 조건이 정확히 crossed homomorphism의 조건이고, $$1$$-coboundary $$dm$$이 정확히 principal crossed homomorphism이므로 첫 주장은 정의 그대로이다. 작용이 trivial하다면 crossed homomorphism의 조건은 $$\varphi(gh)=\varphi(h)+\varphi(g)$$, 즉 group homomorphism의 조건이 되고, principal crossed homomorphism은 $$0$$ 뿐이다.

</details>

## 순환군의 코호몰로지

유한 cyclic group의 경우에는 bar resolution보다 훨씬 작은 resolution이 존재한다. $$G=\langle\sigma\rangle$$가 order $$n$$의 cyclic group이라 하고, $$\mathbb{Z}G$$의 두 원소

$$N=1+\sigma+\sigma^2+\cdots+\sigma^{n-1},\qquad \sigma-1$$

을 생각하자. 이들 각각을 곱하는 것은 $$\mathbb{Z}G$$-linear map $$\mathbb{Z}G \rightarrow \mathbb{Z}G$$를 정의한다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> 다음의 sequence

$$\cdots\longrightarrow\mathbb{Z}G\overset{\sigma-1}{\longrightarrow}\mathbb{Z}G\overset{N}{\longrightarrow}\mathbb{Z}G\overset{\sigma-1}{\longrightarrow}\mathbb{Z}G\overset{\varepsilon}{\longrightarrow}\mathbb{Z}\longrightarrow0$$

은 trivial $$G$$-module $$\mathbb{Z}$$의 free resolution이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{Z}G$$의 원소를 $$x=\sum_{i=0}^{n-1}a_i\sigma^i$$로 적자. 우선 complex가 되는 것을 확인하면, $$\sigma N=N$$이므로 $$(\sigma-1)N=N(\sigma-1)=0$$이고 $$\varepsilon(\sigma-1)=0$$이다.

Exactness를 확인하자. 먼저 $$\ker\varepsilon=\im(\sigma-1)$$이다. $$\varepsilon(x)=\sum a_i=0$$이라면

$$x=\sum_{i=0}^{n-1}a_i(\sigma^i-1)=(\sigma-1)\sum_{i=1}^{n-1}a_i(\sigma^{i-1}+\cdots+\sigma+1)$$

이기 때문이다. 다음으로 $$\ker(\sigma-1)=\im N$$이다. $$(\sigma-1)x=0$$이라면 $$\sigma x=x$$인데, $$\sigma x=\sum a_i\sigma^{i+1}$$이므로 계수를 비교하면 $$a_0=a_1=\cdots=a_{n-1}$$이고, 즉 $$x=a_0N=N\cdot a_0$$이다. 거꾸로 $$N\sigma^j=N$$이므로 $$\im N=\mathbb{Z}N\subseteq\ker(\sigma-1)$$이다. 마지막으로 $$\ker N=\im(\sigma-1)$$이다. $$Nx=N\varepsilon(x)$$이므로 ($$N\sigma^i=N$$) $$Nx=0$$인 것은 $$\varepsilon(x)=0$$인 것과 동치이고, 이는 위에서 보았듯 $$x\in\im(\sigma-1)$$인 것과 동치이다.

</details>

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> Order $$n$$의 cyclic group $$G=\langle\sigma\rangle$$과 $$G$$-module $$M$$에 대하여, $$N_M:M \rightarrow M$$을 $$m\mapsto\sum_{i=0}^{n-1}\sigma^i\cdot m$$이라 하면 다음이 성립한다.

$$H^0(G;M)=M^G,\qquad H^{2k-1}(G;M)\cong\frac{\ker N_M}{(\sigma-1)M},\qquad H^{2k}(G;M)\cong\frac{M^G}{N_M(M)}\qquad(k\geq1)$$

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 7](#prop7)의 resolution에 $$\Hom_{\lMod{\mathbb{Z}G}}(-,M)$$을 적용하자. $$\Hom_{\lMod{\mathbb{Z}G}}(\mathbb{Z}G,M)\cong M$$ ($$\varphi\mapsto\varphi(1)$$)이고, 이 identification 하에서 $$\sigma-1$$과 $$N$$을 곱하는 map들은 각각 $$m\mapsto(\sigma-1)\cdot m$$과 $$N_M$$이 된다. 즉 cochain complex는

$$0\longrightarrow M\overset{\sigma-1}{\longrightarrow}M\overset{N_M}{\longrightarrow}M\overset{\sigma-1}{\longrightarrow}M\longrightarrow\cdots$$

이고, [§Ext와 Tor, ⁋명제 3](/ko/math/homological_algebra/ext_and_tor#prop3)에 의해 이것의 cohomology가 $$H^n(G;M)$$이다. $$\ker(\sigma-1)=M^G$$이므로 주장의 식들을 얻는다.

</details>

즉 유한 cyclic group의 코호몰로지는 주기 $$2$$를 갖는다. 특히 $$H^1$$은 "norm이 $$0$$인 원소들"을 "자명한 이유로 norm이 $$0$$인 원소들"로 나눈 것으로, 이 quotient가 사라지는지를 묻는 것이 고전적인 Hilbert의 정리 90의 내용이다.

<div class="remark" markdown="1">

<ins id="rmk9">**참고 9**</ins> 군 코호몰로지의 낮은 차수들은 모두 고전적인 대수학의 문제들과 연결된다. $$H^1$$이 crossed homomorphism을 분류하는 것을 [명제 6](#prop6)에서 보았고, $$H^2(G;M)$$은 abelian kernel $$M$$을 갖는 $$G$$의 extension들을 분류한다는 것이 알려져 있다. ([\[군론\] §군의 확장](/ko/math/group_theory/extensions)) 또, Galois extension $$\mathbb{L}/\mathbb{K}$$에 대하여 $$\Gal(\mathbb{L}/\mathbb{K})$$가 $$\mathbb{L}^\times$$에 작용하는 상황의 코호몰로지를 *Galois cohomology*라 부르며, 이 경우 $$H^1$$이 자명하다는 것이 Hilbert의 정리 90이다. 이들 각각은 별도의 글에서 다루기로 한다.

</div>

---

**참고문헌**

**[Wei]** Charles A. Weibel. *An introduction to homological algebra*. Cambridge studies in advanced mathematics. Cambridge University Press, 1994.  
**[Bro]** Kenneth S. Brown. *Cohomology of groups*. Graduate texts in mathematics. Springer, 1982.

---
