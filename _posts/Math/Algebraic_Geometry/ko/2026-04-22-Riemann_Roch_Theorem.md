---
title: "곡선에서의 리만-로흐 정리"
excerpt: "The Riemann–Roch theorem for curves"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/riemann_roch_theorem
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Riemann_Roch.png
    overlay_filter: 0.5

date: 2026-04-22
last_modified_at: 2026-04-22
weight: 16
published: false
---

우리는 이제 [§선형계, ⁋정의 2](/ko/math/algebraic_geometry/linear_systems#def2)에서 살펴본 line bundle $$\mathcal{L}$$의 complete linear system $$H^0(X, \mathcal{L})$$을 더 자세하게 살펴본다. 이는 linear system을 도입한 직후에 소개해도 되었겠지만, 증명을 위해서는 Serre duality가 필요하여 뒤로 두었다. 

## 리만-로흐 정리

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해 *Riemann–Roch dimension*을

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

로 정의한다.

</div>

일반적으로 우리는 $$\mathcal{O}_X(D)$$를 $$D$$를 따라 order $$1$$의 pole을 가질 수 있는 rational function들의 sheaf로 생각하므로, 이러한 관점에서 $$H^0(C, \mathcal{O}_C(D))$$는 $$X$$ 위에서 정의된 함수들이 이루는 공간이라 생각할 수 있다. 

이 공간 $$H^0(C, \mathcal{O}_C(D))$$는 [§선형계, ⁋정의 2](/ko/math/algebraic_geometry/linear_systems#def2)에서 처음 도입했던 것을 기억하자. 그에 따르면 공간 $$H^0(C, \mathcal{O}_C(D))$$는 주어진 divisor $$D$$와 linearly equivalent한 divisor들의 모임이며, 이를 projectivize하여 $$\mathcal{O}_C(D)$$의 *complete linear system* $$\lvert \mathcal{O}_X(D)\rvert$$를 얻을 수 있었다. 이 글에서는 편의상 이를 $$\lvert D\rvert$$으로 적기로 한다. 그럼 위의 Riemann-Roch dimension은 $$\lvert D\rvert$$의 projective dimension에 $$1$$을 더한 값이 된다. 

이제 점 $$p\in C$$를 고정하자. 그럼 $$p$$를 지나는 $$\lvert D\rvert$$의 원소들은 그 정의에 의해 $$H^0(C,\mathcal{O}_C(D))$$의 원소들 중 $$s(p)=0$$을 만족하는 section들로 생각할 수 있다. 즉, 이러한 $$s$$는 $$\divisor(s)-p\geq 0$$을 만족하는 $$H^0(C, \mathcal{O}_C(D))$$의 원소이며, 이를 통해 정확히 이러한 원소들의 모임이

$$\mathcal{O}_C(D-p)\cong \mathcal{O}_C(D)\otimes \mathcal{O}_C(-p)$$

의 global section임을 확인할 수 있다. 따라서 만일 $$H^0(C,\mathcal{O}_C(D-p))\subseteq H^0(C, \mathcal{O}_C(D))$$에서 등호가 성립한다면, 이는 곧 $$\lvert D\rvert$$의 모든 원소가 $$p$$를 지난다는 뜻이므로 $$p$$가 $$\lvert D\rvert$$의 base point가 된다. 한편 $$\lvert D\rvert$$가 basepoint-free라면 우리는 [§선형계](/ko/math/algebraic_geometry/linear_systems)에서 이를 사용하여 regular map $$\varphi_D:C\rightarrow \mathbb{P}^{\ell(D)-1}$$을 정의할 수 있었는데, 이러한 관점에서 $$\ell(D)$$와 $$\ell(D-p)$$의 차이는 점 $$p$$가 divisor $$D$$에 가하는 보정항이라 볼 수 있다. 

그럼 이번 글과 다음 글에서 살펴볼 리만-로흐 정리는 이를 어떤 의미에서 확장한 것으로, canonical class $$K_C$$가 점 $$p$$의 역할을 대신하는 전역적인 역할을 해 준다. 구체적으로 우리가 증명하고자 하는 식은

$$\ell(D)-\ell(K_C-D)=\deg D+1-g$$

로, 여기에서 $$\deg D+1$$는 기대값이며, $$g$$는 곡선의 위상적인 데이터가 가하는 손실이며 $$\ell(K_C-D)$$는 canonical class와 $$D$$의 위치관계가 가하는 보정항이다. 

이를 보기 위해 우선 Serre duality를 적용하면

$$H^1(C, \mathcal{O}_C(D)) \cong H^0(C, \omega_C \otimes \mathcal{O}_C(-D))^\vee = H^0(C, \mathcal{O}_C(K_C - D))^\vee\tag{$1$}$$

이 성립한다 ([§세르 쌍대성, ⁋명제 2](/ko/math/algebraic_geometry/serre_duality#prop2)). 여기서 canonical divisor $$K_C$$는 canonical line bundle에 대응되는 divisor였던 것을 기억하자. 그럼 다음 보조정리에 의해 $$\mathcal{O}_C(D)$$의 Euler characteristic에서 등장하는 항은 단 두 개 뿐임을 유도할 수 있다. 이 글에서 우리는 $$\mathbb{K}$$가 *infinite* field임을 가정한다. 

<div class="proposition" markdown="1">

<ins id="lem2">**보조정리 2**</ins> Smooth projective curve $$C$$ 위의 임의의 coherent sheaf $$\mathcal{F}$$에 대해

$$H^i(C, \mathcal{F}) = 0 \quad (i \ge 2)$$

가 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Embedding $$C\hookrightarrow \mathbb{P}^N$$을 고정하면, dimension count를 통해 $$C\cap H_1\cap H_2=\emptyset$$이도록 하는 hyperplane $$H_1,H_2$$가 존재한다. 따라서 $$U_i=C\setminus H_i$$로 두면 이들은 $$C$$의 affine open cover를 이루는 것을 안다. 

이제 $$\{U_1,U_2\}$$에 대한 Čech cohomology를 생각하자. [§층 코호몰로지, ⁋명제 12](/ko/math/algebraic_geometry/sheaf_cohomology#prop12) 직후에 간략하게 소개했듯, projective variety 위의 임의의 affine open cover는 [§층 코호몰로지, ⁋정리 11](/ko/math/algebraic_geometry/sheaf_cohomology#thm11)의 전제조건을 만족하며 따라서 구하고자 하는 sheaf cohomology는 정확하게 이 affine open cover에 대한 계산으로 귀결된다. 이제 Čech complex가 단순히

$$\check{C}(\mathcal{U}, \mathcal{F}):\qquad \mathcal{F}(U_1)\oplus \mathcal{F}(U_2)\rightarrow \mathcal{F}(U_1\cap U_2)\rightarrow 0$$

으로 길이 1짜리 complex가 되므로 $$\check{H}^i = 0\ (i \ge 2)$$가 즉시 따라온다. 

</details>

따라서, 이 결과에 의해 임의의 divisor $$D$$에 대해

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D))\tag{$2$}$$

가 성립한다. 여기서 $$h^i$$는 $$H^i$$의 dimension에 대한 shorthand notation이다.

한편, 우리는 위상수학적 관점에서 genus $$g$$ compact Riemann surface $$S$$의 Euler characteristic은

$$\rchi(S)=2(1-g)$$

로 주어진다는 사실을 잘 알고 있다. 이 때 Euler characteristic은 triangulation을 사용하여 꼭짓점 수 $$V$$, 모서리 수 $$E$$, 면 수 $$F$$를 사용하여 $$V-E+F$$로 생각할 수도 있고[^1], 혹은 Gauss-Bonnet 정리 등의 미분기하적 도구를 사용하여 정의된 것으로 생각해도 된다. 

대수기하학에서 우리는 보편적으로 underlying field $$\mathbb{K}$$가 복소수인 것으로 생각하므로, 위에서의 genus $$g$$ compact Riemann surface는 대수기하 관점에서는 1차원 곡선 $$C_S$$에 불과하다. 이 때, 대수기하적 관점에서의 Euler characteristic은 따라서 위의 식 ($$2$$)에 $$D=0$$을 대입한

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})$$

으로 주어진다. 한편, 위상수학에서 $$1$$차원 구멍이 $$H^1$$을 통해 나타나듯 대수기하에서의 1차원 구멍, 즉 위상수학 관점에서의 2차원 구멍인 genus는 $$g=h^1(C_S, \mathcal{O}_{C_S})$$로 정의되며, global section은 상수함수 뿐이므로 $$C_S$$의 Euler characteristic은

$$\rchi(\mathcal{O}_{C_S})=h^0(C_S, \mathcal{O}_{C_S})-h^1(C_S, \mathcal{O}_{C_S})=1-g$$

로 나타난다. 이 값이 위상수학적인 Euler characteristic의 절반이라는 것은 우연이 아니며, Hodge theory를 통해 확인할 수 있지만 이것은 우리의 목표와는 무관하므로 우선은 넘기기로 한다. 중요한 것은 대수기하에서의 Euler characteristic과, 이를 curve에서 계산했을 때의 값이 $$1-g$$가 나오는 것이 뜬금없는 것이 아니라 위상수학에서의 결과를 재해석하는 것이라는 것이다. 

이번 글의 주제인 Riemann–Roch 정리는 여기에 한 가지의 작업을 추가한다. 위의 계산은 아무것도 붙이지 않은 trivial sheaf $$\mathcal{O}_{C_S}$$에 대한 것이므로, 이를 임의의 divisor $$D$$를 사용하여 twist한 sheaf $$\mathcal{O}_{C_S}(D)$$를 생각하는 것이다. 그럼 이 때의 보정항이 $$\deg D$$만큼 생긴다는 것이 Riemann-Roch 정리의 결과이다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> (Riemann–Roch for curves) Smooth projective curve $$C$$ 위의 divisor $$D$$에 대해

$$\ell(D) - \ell(K_C - D) = \deg D + 1 - g$$

이 성립한다. 여기서 $$g$$는 $$C$$의 genus, $$K_C$$는 canonical divisor이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

위의 계산들과 정의들에 의하여

$$\rchi(\mathcal{O}_C(D)) = h^0(C, \mathcal{O}_C(D)) - h^1(C, \mathcal{O}_C(D)) = \ell(D) - \ell(K_C - D)$$

이다. 한편, effective divisor $$D$$에 대해 short exact sequence 

$$0 \to \mathcal{O}_C \to \mathcal{O}_C(D) \to \mathcal{O}_D \to 0$$

이 존재하며, 그럼 Euler characteristic의 additivity에 의해 $$\rchi(\mathcal{O}_C(D)) = \rchi(\mathcal{O}_C) + \rchi(\mathcal{O}_D)$$이다. 

여기서 $$\mathcal{O}_D$$는 차수 $$\deg D$$의 skyscraper sheaf이므로 $$\rchi(\mathcal{O}_D) = \deg D$$이고, 위에서 살펴본 것과 같이 $$\rchi(\mathcal{O}_C)=1-g$$이므로 이를 앞선 식과 결합하면 원하는 결과를 얻는다. 일반적인 (effective가 아닌) divisor에 대해서는 $$D$$를 effective divisor $$D'$$과의 차이로 표현한 후 동일한 additivity 논증을 적용하면 된다. 

</details>

위의 증명은 깔끔하지만 그 기하학적 내용이 Euler characterstic 안에 압축되어 있어 직관적으로 잘 와닿지 않을 수 있다. 이를 보완하기 위해 등식을 항별로 읽어보자. 우선 정의에 의해 

$$\ell(D) = \dim H^0(C, \mathcal{O}_C(D))$$

이며, 이 때 우변의 공간 $$H^0(C, \mathcal{O}_C(D))$$는 기하적으로 

$$\divisor(f)+D\geq 0$$

을 만족하는 meromorphic function들의 모임이다. 즉 $$D$$는 $$f$$의 pole이 $$D$$의 support 안에서만 일어나도록, 그리고 각 점 $$p$$에서 극의 차수가 최대 $$\operatorname{ord}_p D$$가 되도록 강제하며, 따라서 $$\deg D$$가 커질수록 허용되는 pole의 차수도 커지므로 $$\ell(D)$$가 커진다. 

뿐만 아니라, 우리의 상황에서 $$C$$는 $$1$$차원이므로 (effective) divisor는 $$D=\sum n_i p_i$$의 꼴이며 이를 이용하면 보다 정량적으로 다음의 부등식

$$\ell(D)\leq \deg(D)+1\tag{$3$}$$

을 얻을 수 있다. 구체적으로 $$D = \sum n_i p_i$$가 effective라 하면, $$f\in H^0(C, \mathcal{O}_C(D))$$를 각 점 $$p_i$$에서의 principal part로 보내는 선형사상

$$H^0(C, \mathcal{O}_C(D)) \longrightarrow \bigoplus_i \mathbb{K}^{n_i}\tag{$4$}$$

을 생각할 수 있다. 직관적으로, 이는 $$f$$가 점 $$p_i$$에서의 Laurent polynomial의 principal part를 다음의 식

$$\frac{a_{-n_i}}{(x-p_i)^{n_i}}+\frac{a_{-n_i-1}}{(x-p_i)^{n_i-1}}+\cdots +\frac{a_{-1}}{x-p_i}$$

과 같이 나타냈을 때, 

$$f\mapsto (a_{-n_i}, \ldots, a_{-1})$$

를 모든 $$p_i$$에 대해서 한 번에 고려하는 함수이다. 그럼 위의 선형사상의 우변의 차원은 $$\sum n_i = \deg D$$이고, 이 사상의 kernel은 pole을 갖지 않는 global section, 즉 $$H^0(C, \mathcal{O}_C) = \mathbb{K}$$와 같으며 이로부터 $$\ell(D) \leq 1 + \deg D$$를 얻는다. $$D$$가 effective가 아니지만 $$\ell(D) > 0$$이라면, $$D$$는 어떤 effective divisor와 linearly equivalent이므로 동일한 부등식이 성립한다.

일반적으로 이 식이 등식이 되기 위해서는 선형사상이 surjective여야 하지만, 이것이 항상 성립하는 것은 아니다. 이를 확인하기 위해 [명제 2](#prop2)의 증명에서 살펴본 short exact sequence

$$0\longrightarrow \mathcal{O}_C\overset{i}{\longrightarrow} \mathcal{O}_C(D)\overset{p}{\longrightarrow} \mathcal{O}_D\longrightarrow 0$$

으로부터 얻어지는 long exact sequence

$$0\longrightarrow H^0(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^0(C,\mathcal{O}_C(D)) \overset{p^\ast}{\longrightarrow} H^0(C,\mathcal{O}_D) \overset{\delta}{\longrightarrow} H^1(C,\mathcal{O}_C)\overset{i^\ast}{\longrightarrow} H^1(C,\mathcal{O}_C(D))\to 0$$

를 생각하자. 여기서 $$C$$는 curve이고 $$D=\sum n_i p_i$$이므로, $$\mathcal{O}_D$$는 support $$\lvert D\rvert$$를 갖는 degree $$D$$의 skyscraper sheaf이며 이로부터 $$H^0(C, \mathcal{O}_C)=\bigoplus_i \mathbb{K}^{n_i}$$임을 안다. 뿐만 아니라 위에서 살펴본 linear map ($$4$$)이 실제로 이 long exact sequence에서의 $$p^\ast$$와 맞아떨어진다는 것을 알고 이로부터 $$p^\ast$$의 cokernel은 다음 isomorphism들의 chain

$$\coker p^\ast=\frac{H^0(C, \mathcal{O}_D)}{\im p^\ast}=\frac{H^0(C, \mathcal{O}_D)}{\ker\delta}\cong \im\delta\cong\ker i^\ast$$

으로 구할 수 있고, 특히 그 차원은

$$\dim\coker p^\ast =\dim \ker (i^\ast: H^1(C, \mathcal{O}_C)\twoheadrightarrow H^1(C, \mathcal{O}_C(D)))=\dim H^1(C, \mathcal{O}_C)-\dim H^1(C, \mathcal{O}_C(D))$$

이다. 만일 여기에 식 (1)을 적용한다면, 

$$\dim\coker p^\ast=\dim H^1(C, \mathcal{O}_C)-\dim H^0(C, \mathcal{O}_C(K_C-D))^\vee=g-\ell(K_C-D)$$

임을 안다. 위의 부등식 ($$3$$)에서 $$\deg(D)+1$$과 $$\ell(D)$$의 차이만큼이 cokernel의 차원이므로, 이 계산들이 [명제 3](#prop3)의 결과를 복원한다. 즉, 바꿔말하면 $$\ell(K_C-D)$$는 $$\ell(D)$$가 그 upper bound $$\deg D+1$$로부터 얼마나 떨어지는지를 측정하는 양이며, 이는 본디 $$D$$를 따라 vanishing하는 $$1$$-form들의 counting 문제이지만 Serre duality를 사용하여 $$\ell(K_C-D)$$로 바꾸어 쓴 것이다. 

예로 degree $$D$$가 매우 커서 $$\deg(K_C-D)<0$$을 만족하는 경우를 생각하자. 그럼 이 경우 $$\ell(K_C-D)=0$$이고 따라서 Riemann-Roch theorem은 다음의 식

$$\ell(D)=\deg D+1-g$$

을 준다. 즉 genus가 커질수록 같은 degree의 divisor가 만드는 공간이 좁아지는 것이다. 그러나 일반적인 경우는 여기에 $$\ell(K_C-D)$$의 영향이 추가되며, 이 때 주의할 것은 $$\ell(K_C-D)$$ 항은 그 정의상 $$D$$의 degree 뿐만 아니라 $$D$$가 canonical class $$K_C$$와 어떤 관계가 있는지에 따라 달라질 수 있다는 것이다. 이는 *special divisor*의 현상으로 [Brill–Noether theory](#brill-noether)에서 본격적으로 다룬다. 

또 다른 특별한 예시로, $$D=0$$을 넣으면

$$\ell(0)-\ell(K_C)=\deg D+1-g$$

에서, $$\deg D=0$$, $$\ell(0)=1$$이므로 $$\ell(K_C)=g$$가 성립하는 것을 안다. 이제 $$D=K_C$$를 넣으면

$$\ell(K_C)-\ell(0)=\deg K_C +1-g$$

이고 이로부터 [§표준선다발, ⁋예시 10](/ko/math/algebraic_geometry/canonical_bundle#ex10)에서의 계산 $$\deg(K_C)=2g-2$$를 복원할 수 있다. 해당 예시에서는 degree-genus formula를 잘 알려진 공식으로 언급하고 이로부터 $$\deg(K_C)$$를 얻어냈지만 (그리고 이것이 역사적인 맥락에서는 더 타당하지만) 우리는 잠시 후 [명제 7](#prop7)에서 degree-genus formula가 Riemann-Roch theorem의 특수한 경우임을 살펴볼 것이다. 

어쨌든 지금까지의 계산을 정리하면 $$\ell(D)$$는 $$D$$의 complete linear system의 차원, $$\ell(K_C - D)$$는 $$K_C$$가 $$D$$ 위에 부과하는 수정항이며, 큰 degree에서는 이 수정항이 사라지고 작은 degree에서는 $$K_C$$의 기하학적 정보를 반영한다는 것으로 생각할 수 있다.

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> **$$\mathbb{P}^1$$**: $$\mathbb{P}^1$$의 genus는 $$g = 0$$이고, canonical divisor는 $$K_{\mathbb{P}^1} = -2H$$이다 ([§표준선다발, ⁋예시 8](/ko/math/algebraic_geometry/canonical_bundle#ex8)). 한편, 우리는 ([§선다발과 벡터다발, ⁋예시 12](/ko/math/algebraic_geometry/line_bundles#ex12))에서 $$\mathcal{O}_{\mathbb{P}^1}(d)$$의 global section이 차수 $$d$$의 동차다항식들임을 보였으므로,

$$\ell(dH) = d+1 \quad (d \ge 0), \qquad \ell(dH) = 0 \quad (d < 0)$$

이 성립하는 것을 안다. 이제 Riemann–Roch 식을 확인해보면, $$D = dH$$에 대해 $$\deg D = d$$이고 $$K_C - D = (-2-d)H$$이므로

$$\ell(dH) - \ell(-2H-dH) = d + 1 - 0 = d + 1$$

이 되어 양변이 모두 $$d+1$$로 일치함을 확인할 수 있다.

</div>

<div class="example" markdown="1">

<ins id="ex5">**예시 5 (Elliptic curve)**</ins> Genus $$1$$ case $$g = 1$$의 경우, 우리는 위의 계산을 통해 $$\deg K_C=2g-2=0$$이고 $$\ell(K_C)=g=1$$임을 안다. $$\ell(K_C)=1>0$$이므로, 앞서 본 것처럼 $$K_C$$와 linearly equivalent한 effective divisor가 존재하는데, $$\deg K_C=0$$이고 degree가 $$0$$인 effective divisor는 $$0$$뿐이므로 $$K_C\sim 0$$이다. 이를 사용하여 Riemann-Roch를 다시 보면

$$\ell(D) - \ell(-D) = \deg D$$

이 된다. 특히 $$\deg D > 0$$이면 $$\ell(-D) = 0$$이므로 $$\ell(D) = \deg D$$이다. 

$$\deg D=0$$인 경우가 위에서 언급한 작은 degree의 경우인데, 우선 부등식 ($$3$$)으로부터 $$\ell(D)=0$$이거나 $$\ell(D)=1$$이어야 한다. 만일 $$\ell(D)=1$$이면 $$D$$와 linearly equivalent한 유일한 effective divisor가 존재하는데 그 degree가 $$0$$이므로 이는 $$0$$이다. 따라서 $$D\sim 0$$이고, 거꾸로 $$D\sim 0$$이면 $$\mathcal{O}_C(D)\cong \mathcal{O}_C$$이므로 $$\ell(D)=1$$이다. 즉 $$D$$가 $$0$$과 linearly equivalent할 때만 $$\ell(K_C-D)$$ 항이 $$1$$이 되고, 그렇지 않으면 $$0$$이 되는 상황이 된다. 

</div>

$$K_C \sim 0$$이므로 elliptic curve에서 Riemann-Roch는 특히 단순해진다. $$\deg D > 0$$이면 보정항 $$\ell(K_C-D)=\ell(-D)$$가 사라지므로 $$\ell(D)=\deg D$$로 완벽히 결정되며, 이는 genus가 커질수록 보정항의 영향이 복잡해지는 과정에서 $$g=1$$이 가장 간단한 non-trivial case임을 보여준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6 ($$g=2$$)**</ins> 이제 한 단계 더 복잡한 상황인 $$g=2$$ 경우를 보자. 이 경우 $$\deg K_C = 2g - 2 = 2$$이고 $$\ell(K_C)=2$$이며, [명제 3](#prop3)에 $$D=p$$를 대입하면

$$\ell(p)-\ell(K_C-p)=2-g$$

이므로 $$\ell(K_C-p)=\ell(K_C)-1<\ell(K_C)$$이므로 canonical map

$$\varphi_{K_C}:C\rightarrow \mathbb{P}^1$$

이 잘 정의된다. 그럼 $$\mathbb{P}^1$$에서의 hyperplane, 즉 $$\mathbb{P}^1$$의 한 점에 대한 preimage는 $$K_C$$와 linearly equivalent한 effective divisor가 되며 이것이 degree $$2$$ map이라는 사실로부터 $$K_C$$를 두 점의 합 $$p_1+p_2$$로 쓸 수 있다.

이제 한 점 $$p$$의 배수 $$D=d\cdot p$$에 Riemann-Roch를 적용하여 $$\ell(D)$$가 $$d$$에 따라 어떻게 변하는지 살펴 보자. 작은 $$d$$, 즉 $$\ell(K_C-D)$$가 살아있는 곳에서는 특수한 현상이 나타나지만, $$d$$가 커지면 $$\ell(D)$$는 선형적으로 안정화된다.

1. $$d=1$$의 경우, $$\ell(p)\ge 2$$라면 degree 1 사상 $$C\to\mathbb{P}^1$$이 존재하여 $$C\cong\mathbb{P}^1$$이 되지만 $$g=2$$와 모순이므로 $$\ell(p)=1$$이다. Riemann-Roch에 의해 $$\ell(K_C-p)=1$$이다.
2. $$d=2$$의 경우, 만약 $$2p\sim K_C$$이면 $$\ell(2p)=2$$이다. 이 경우 $$p$$를 *Weierstrass point*라 부르는데, 이 조건은 정확히 위의 canonical map $$\varphi_{K_C}$$에 대한 어떤 점의 preimage가 $$p$$로 겹쳐있는 상황에 해당한다. 일반적인 점에서는 $$2p\not\sim K_C$$이므로 $$\ell(2p)=1$$이다.
3. $$d\ge 3$$이면 $$\deg(K_C-D)=2-d<0$$이므로 $$\ell(K_C-D)=0$$이고, 따라서 $$\ell(D)=d-1$$이다.

</div>

위의 예시에서 살펴 본 $$g=2$$의 canonical map $$\varphi_{K_C}: C \rightarrow \mathbb{P}^1$$은 2:1 branched covering이었다. 더 일반적으로, 우리는 genus $$g \ge 2$$인 curve 중 $$\mathbb{P}^1$$로의 degree 2 covering이 존재하는 것을 *hyperelliptic curve<sub>초타원곡선</sub>*라 부르고, 그렇지 않은 경우를 *non-hyperelliptic curve*라 한다. 관례적으로 genus $$0,1$$인 경우는 hyperelliptic curve에서 제외하는 것에 유의하자.

이제 $$g\geq 2$$인 $$C$$에서 canonical bundle $$K_C$$의 complete linear system $$\lvert K_C\rvert$$가 정의하는 morphism $$\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$$의 거동을 살펴보자. 우리는 위에서 $$\deg K_C = 2g - 2$$이고 $$h^0(K_C) = g$$인 것을 확인했으므로, $$\varphi_{K_C}$$의 공역은 $$\mathbb{P}^{g-1}$$이다. 그러나 이는 일반적으로는 closed embedding이 아니며, 이는 $$g=2$$인 경우 이것이 $$2:1$$ covering map이 된다는 것에서 이미 확인하였다. 실제로 $$\varphi_{K_C}$$의 image는 정확히 Veronese embedding $$\mathbb{P}^1 \hookrightarrow \mathbb{P}^{g-1}$$의 image, 즉 degree $$g-1$$의 rational normal curve이다. 이에 대한 증명은 [Har, IV.5.2]를 참조한다.

따라서 $$K_C$$는 ample이지만 very ample이 아닌 line bundle의 구체적인 예시를 제공한다. 이는 [§선형계, ⁋정의 10](/ko/math/algebraic_geometry/linear_systems#def10)에서 언급되었던 "ample but not very ample" 현상의 실현이다. Curve에서 $$\mathcal{L}$$이 very ample이기 위한 충분조건이 $$\deg \mathcal{L} \ge 2g + 1$$임이 알려져 있으며 ([Har, IV.3.2]), $$\deg K_C = 2g - 2 < 2g + 1$$이므로 이 조건을 만족하지 못함도 확인할 수 있다. 대신 $$K_C$$의 적절한 거듭제곱이 very ample이 됨을 확인할 수 있다. $$g \ge 3$$이면 $$\deg K_C^{\otimes 2} = 4g - 4 \ge 2g + 1$$이 성립하므로 $$K_C^{\otimes 2}$$는 very ample이다. $$g = 2$$이면 $$\deg K_C^{\otimes 2} = 4 < 5 = 2g + 1$$이지만, $$\deg K_C^{\otimes 3} = 3(2g - 2) = 6 > 5 = 2g + 1$$이므로 $$K_C^{\otimes 3}$$가 very ample이다. 어느 경우에도 $$K_C$$의 어떤 거듭제곱이 very ample이 되므로, ample의 정의—어떤 거듭제곱이 very ample이면 ample—와 완벽하게 부합한다.

이와 대조적으로, $$g \ge 3$$인 non-hyperelliptic curve에서는 canonical map $$\varphi_{K_C} : C \rightarrow \mathbb{P}^{g-1}$$가 closed embedding이 되어, $$K_C$$ 자체가 very ample이다 ([Har, IV.5.4]).



## 응용

우리는 [§표준선다발, ⁋예시 10](/ko/math/algebraic_geometry/canonical_bundle#ex10)에서 $$\deg K_C=2g-2$$가 된다는 것을 보이기 위해 다음 명제를 잘 알려진 사실이라고 주장하며 넘겼지만, 이제는 이에 대한 증명을 엄밀하게 할 수 있다. 다만 이는 해당 예시와는 정반대로, 해당 예시에서는 adjunction formula와 degree-genus formula를 활용하여 $$\deg K_C=2g-2$$임을 증명하였지만 이제 우리는 $$\deg K_C=2g-2$$라는 사실과 adjunction formula로부터 degree-genus formula를 유도한다. $$K_C$$의 degree는 앞서 [예시 4](#ex4) 이전에 이미 Riemann-Roch로부터 (degree-genus formula를 사용하지 않고) 얻어졌음에 유의하자.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Degree-genus formula)**</ins> Degree $$d$$의 smooth plane curve $$C \subset \mathbb{P}^2$$에 대해

$$g(C) = \frac{(d-1)(d-2)}{2}$$

이 성립한다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Adjunction formula ([§표준선다발, ⁋명제 9](/ko/math/algebraic_geometry/canonical_bundle#prop9))에 의해 $$K_C = (K_{\mathbb{P}^2} + C)\vert_C = (d-3)H\vert_C$$이다. 따라서 $$\deg K_C = d(d-3)$$이고, 이를 $$\deg K_C = 2g - 2$$에 대입하면

$$d(d-3) = 2g - 2 \implies g = \frac{d(d-3) + 2}{2} = \frac{(d-1)(d-2)}{2}$$

을 얻는다.

</details>

이 공식은 평면곡선의 기하학적 성질을 직접적으로 계산해준다. 예를 들어 smooth plane cubic의 genus는 1이므로, 이는 [예시 5](#ex5)에서 다룬 elliptic curve와 같다. 반면 $$d = 1, 2$$인 경우에는 $$g = 0$$으로, 직선과 원뿔곡선이 모두 $$\mathbb{P}^1$$과 birationally equivalent임을 반영한다 ([§유리사상, ⁋명제 10](/ko/math/algebraic_geometry/rational_maps#prop10)).

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> Degree $$d$$에 따른 genus를 계산해보면, degree 3 (cubic)의 경우 $$g = \frac{2 \cdot 1}{2} = 1$$로 elliptic curve이고, degree 4 (quartic)의 경우 $$g = \frac{3 \cdot 2}{2} = 3$$, degree 5 (quintic)의 경우 $$g = \frac{4 \cdot 3}{2} = 6$$이다. Genus가 degree에 따라 빠르게 증가하므로, 고차원의 smooth plane curve는 점점 더 복잡한 위상적 구조를 갖는다.

</div>

### Brill–Noether theory {#brill-noether}

Riemann–Roch 정리가 divisor의 complete linear system $$\lvert D\rvert$$의 차원을 계산하는 공식임을 생각하면, 자연스러운 다음 질문이 떠오른다. 주어진 곡선 $$C$$ (genus $$g$$) 위에서, degree $$d$$이고 차원이 $$r$$ 이상인 linear system을 갖는 divisor가 존재하는가? 그리고 그런 divisor들이 이루는 공간은 어떤 기하학적 구조를 갖는가? 이것이 Brill–Noether 이론의 출발점이다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Genus $$g$$인 curve $$C$$ 위의 degree $$d$$인 divisor $$D$$에 대해, $$d \ge r + g$$이면 $$\ell(D) \ge r + 1$$이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

Riemann–Roch에 의해 $$\ell(D) - \ell(K_C - D) = d + 1 - g$$이다. $$\ell(K_C - D) \ge 0$$이므로 $$\ell(D) \ge d + 1 - g$$이다. $$d \ge r + g$$이면 $$\ell(D) \ge r + 1$$을 얻는다.

</details>

이 결과의 역방향, 즉 $$d < r + g$$일 때 어떤 일이 일어나는지를 묻는 것이 Brill–Noether 이론의 본질적인 내용이다. 보다 정밀한 Brill–Noether 정리에 의하면, 일반적인 (general) genus $$g$$ curve에서 $$\ell(D) \ge r + 1$$인 degree $$d$$ divisor들의 parameter space $$W^r_d$$는 *Brill–Noether 수*

$$\rho(g, r, d) = g - (r+1)(g - d + r)$$

가 음이 아닐 때 ($$\rho \ge 0$$) 차원 $$\rho$$인 nonempty variety이고, $$\rho < 0$$이면 빈 집합이다. 이 수치는 $$G^r_d(C)$$ (degree $$d$$, rank $$r$$의 complete linear series들의 parameter space)가 Grassmannian $$\Gr(r+1, h^0(C, \mathcal{O}_C(D)))$$ 위에서 갖는 예상 차원으로부터 산출된다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> **$$g = 2$$에서의 Brill–Noether**: $$K_C$$는 degree $$2$$를 갖는다. $$d = 2$$, $$r = 1$$의 경우 Brill–Noether 수 $$\rho = 2 - (1+1)(2-2+1) = 2 - 2 = 0$$이므로, 일반적인 $$g = 2$$ 곡선에서 $$W^1_2$$는 차원 0, 즉 유한개의 점으로 구성된다. 실제로 $$D = K_C$$가 유일한 $$g^1_2$$인데, 모든 genus 2 곡선은 hyperelliptic curve이므로 canonical divisor에 의해 유일한 degree 2 map $$C \to \mathbb{P}^1$$을 갖는다.

$$d = 3$$, $$r = 1$$의 경우 $$\rho = 2 - (1+1)(2-3+1) = 2 - 0 = 2 > 0$$이므로 $$W^1_3$$은 차원 2의 nonempty variety이다. [명제 9](#prop9)에 의해서도 $$d = 3 \ge r + g = 3$$이므로 $$\ell(D) \ge 2$$가 보장된다. Riemann–Roch에 의해 $$\ell(D) \ge 3 + 1 - 2 = 2$$이다.

$$d = 0$$, $$r = 0$$의 경우 $$\rho = 2 - 1 \cdot 2 = 0$$이고, $$W^0_0 = \{0\}$$로 trivial divisor가 유일한 점이다.

</div>

---

**참고문헌**

**[Hart]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.
**[Sha]** I. R. Shafarevich, *Basic Algebraic Geometry I: Varieties in Projective Space*, Springer, 2013.

---

[^1]: 이것은 cohomology의 alternating sum으로서 Euler characteristic을 정의하는 것과 맞아떨어진다. 