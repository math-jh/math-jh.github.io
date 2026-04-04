---
title: "표준선다발"
excerpt: "Canonical bundle and canonical divisor"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/canonical_bundle
sidebar:
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Canonical_Bundle.png
    overlay_filter: 0.5

date: 2026-03-15
last_modified_at: 2026-03-29
weight: 11

published: false
---

[§선형계](/ko/math/algebraic_geometry/linear_systems)에서 우리는 line bundle의 (basepoint-free) complete linear system을 사용하여 projective space에 embed할 수 있다는 것을 살펴보았고, 만일 이것이 closed embedding을 정의한다면 이러한 line bundle을 *very ample*이라 부르기도 하였다. 

이렇듯 line bundle이 우리의 기하학에 꽤나 중요한 영향을 미치고 있음에도 불구하고, 우리는 아직까지 임의의 variety 위에 일반적으로 line bundle을 정의하는 방법을 제대로 살펴보지 않았다. 만일 $$X$$가 *smooth* variety라면, 우리는 [§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24)를 사용하여 이 위에 정의된 cotangent bundle $$\Omega_X^1$$을 생각할 수 있으며 이것의 top exterior power를 생각하여 *canonical bundle* $$\omega_X$$를 생각할 수 있다. 이번 글에서 우리의 목표는 이 bundle $$\omega_X$$를 살펴보는 것이다. 

## 벡터다발과 준연접층

위에서 언급한 것과 같이, $$\omega_X$$를 정의하기 위해서는 cotangent bundle $$\Omega_X^1$$로부터 시작한다. 이는 $$X$$ 위에 정의된 differential form들의 bundle인 것을 이미 살펴보았다. 이것이 대수적인 세팅에서의 미분과 맞아떨어짐을 보이자. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3)) 이를 위해서는 임의의 affine variety $$X$$와 그 coordinate ring $$A$$, 그리고 $$A$$-module $$M$$이 주어졌을 때 $$M$$을 $$X$$ 위의 vector bundle로 옮기는 과정을 살펴보아야 한다. 

우리의 기본적인 철학은 [§아핀다양체, ⁋명제 16](/ko/math/algebraic_geometry/affine_varieties#prop16)을 이용하여 coordinate *ring* 사이의 homomorphism을 variety들 사이의 반대방향 morphism으로 옮길 수 있으며 따라서 $$X$$ 위에 정의된 bundle을 얻어낼 수 있다는 것이다. 그러나 문제는 $$M$$은 ring이 아니라는 것이다. 즉 $$M$$ 위에는 곱셈이 정의되어 있지 않다. 그러나 [\[다중선형대수학\] §텐서대수, ⁋정의 5](/ko/math/multilinear_algebra/tensor_algebras#def5)에 따르면 우리는 $$M$$ 위에 (commutative) 곱셈을 강제로 정의해주는 symmetric algebra $$\S(M)$$을 생각할 수 있다. 

그러나 이를 곧바로 적용하기에는 문제가 있다. 우리의 목적은 $$M$$을 $$X$$ 위에 정의된 vector bundle로 보려는 것임을 기억하자. 즉 대략적으로 $$X$$의 각 점 위에 $$M$$을 잘 달아주는 것이 우리의 목적인데, [§아핀다양체, ⁋명제 16](/ko/math/algebraic_geometry/affine_varieties#prop16)에 따르면 $$M$$이 variety의 세상에서 (fiber로) 등장한다면, 이를 정의하는 coordinate ring은 이것의 좌표함수여야 한다. 즉, 우리는 $$M$$ 대신 $$M^\vee$$를 사용해야만 하고, 따라서 $$\S_A(M)$$ 대신 $$\S_A(M^\vee)$$을 생각한다. 그럼 이는 $$A$$-algebra이며 따라서 coordinate ring 사이의 함수 $$A\rightarrow \S_A(M^\vee)$$을 얻고, 여기에 [§아핀다양체, ⁋명제 16](/ko/math/algebraic_geometry/affine_varieties#prop16)를 적용하면 어떠한 variety $$V(M)$$에서 $$X$$로 가는 morphism을 얻는다. 

이 morphism이 실제로 $$X$$ 위의 vector bundle 구조를 갖는지 확인하자. 점 $$x\in X$$는 coordinate ring $$A$$의 maximal ideal $$\mathfrak{m}_x$$에 해당하며, 따라서 $$V(M) \to X$$에서 $$x$$ 위의 set-theoretic fiber $$V(M)_x = \pi^{-1}(x)$$의 점들은 $$\mathfrak{m}_x\cdot \S_A(M^\vee)$$를 포함하는 $$\S_A(M^\vee)$$의 maximal ideal들이다. 

대수적으로 이 fiber를 정의하는 coordinate ring을 얻기 위해서는 이 위에서 정의된 함수가 무엇인지부터 생각해야 한다. 그런데 $$x\in X$$를 정의하는 maximal ideal $$\mathfrak{m}_x$$에 포함되는 함수들은 모두 $$x$$ 위에서 vanish하므로, 이 fiber에서 정의된 함수는 $$A/\mathfrak{m}_x$$-valued function으로 생각하는 것이 타당하다. 우리는 이 field $$\kappa(x)=A/\mathfrak{m}_x$$를 $$x$$에서의 *residue field*라 부르며, 따라서 일반적으로 $$\kappa(x)$$는 $$\mathbb{K}$$의 algebraic extension이다. ([\[가환대수학\] §영점정리, ⁋정리 4](/ko/math/commutative_algebra/nullstellensatz#thm4)) 우리는 보통 $$\mathbb{K}$$가 algebraically closed field인 경우를 생각하므로, $$\kappa(x)$$는 그냥 $$\mathbb{K}$$라 생각해도 무방하다. 

이제 위의 논의로부터 $$\S_A(M^\vee)$$의 $$\kappa(x)$$-valued function들의 모임 $$\S_A(M^\vee)\otimes_A\kappa(x)$$을 생각해야 하는 것을 안다. 그럼 symmetric algebra가 tensor product와 commute하는 것으로부터 다음의 식

$$\S_A(M^\vee)\otimes_A\kappa(x)=\S_{\kappa(x)} (M^\vee\otimes_A\kappa(x))=\S_{\kappa(x)}(M_x^\vee)$$

을 얻으며, 여기서 우변의 $$M_x = M \otimes_A \kappa(x)$$이며, 여기서 등장하는 텐서곱들은 위에서 설명한 것과 마찬가지로 대강 모든 대상들을 $$\mathbb{K}$$-vector space (정확히는 $$\kappa(x)$$-vector space)로 보는 것이라 생각하면 된다. 

이제 $$\S_{\kappa(x)}(M_x^\vee)$$는 $$\kappa(x)$$를 계수로 갖고, $$M_x^\vee$$의 각 원소들을 1차식으로 갖는 polynomial algebra이며, 그렇다면 $$V(M)_x$$의 fiber는 이들 $$M_x^\vee$$의 원소들을 coordinate function으로 갖는 점들이고, 따라서 이들 점들은 $$M_x$$의 double dual이라 생각할 수 있다. 이제 만일 $$M$$이 finitely generated $$A$$-module이라면, canonical isomorphism $$M_x\cong M_x^{\vee\vee}$$이 존재하므로 이로부터 각각의 fiber $$V(M)_x$$을 $$\kappa(x)$$-vector space $$M_x$$로 이해할 수 있다. 

추가적인 계산을 통해 이 데이터가 locally trivial 조건을 만족한다는 것을 확인할 수 있으며, 이로서 우리는 finitely generated $$A$$-module $$M$$이 주어졌을 때 이를 $$X$$ 위에 정의된 vector bundle로 생각할 수 있다는 것을 확인할 수 있다. 

한편 이 vector bundle이 locally trivial임을 보이는 것은 본질적으로 sheaf의 언어로 이를 살펴보는 것과 같다. 우리는 기하적 직관을 위해 sheaf의 언어를 많이 사용하지는 않았는데, 대략적으로 설명하면 다음과 같다. 

위와 마찬가지로 affine variety $$X$$와 그 coordinate ring $$A$$, 그리고 $$A$$-module $$M$$이 주어졌을 때, $$X$$ 위에 정의된 sheaf $$\widetilde{M}$$을 다음의 식

$$\widetilde{M}(U)=M\otimes_A \mathcal{O}_X(U)$$

으로 정의한다. 이는 기본적으로 위에서 $$\kappa(x)$$를 도입하는 것과 같은 맥락이며, 실제로 우리가 자세히 계산하지는 않았지만 $$V(M)$$의 local triviality를 보일 때는 이와 같이 structure sheaf를 사용해서 base change를 했을 것이다. 그럼 특히 $$X$$ 전체에 대해서는 

$$\widetilde{M}(X)=M\otimes_A A=M$$

이 되어 $$M$$이 $$\widetilde{M}$$의 global section space가 된다. 

이 두 정의는 본질적으로 같은 대상을 다른 기하적 언어로 표현한 것에 불과하다. 즉, affine variety $$X$$와 그 coordinate ring $$A$$, finitely generated $$A$$-module $$M$$에 대하여, $$\widetilde{M}$$의 étale space가 곧 $$V(M)$$이고, $$V(M)$$의 section sheaf가 $$\widetilde{M}$$이다. 

일반적으로, 구체적인 기하적 언어에 비교했을 때 sheaf 언어의 장점은 더 일반적인 경우에 적용이 가능하다는 것이다. 가령 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 일반적인 variety $$X$$ 위의 $$\mathcal{O}_X$$-module $$\mathcal{F}$$가 *quasi-coherent sheaf<sub>준연접층</sub>라는 것은, $$X$$의 affine open cover $$\{U_i\}$$와 각각의 coordinate ring $$A_i=\mathcal{O}_X(U_i)$$-module $$M_i$$가 존재하여 $$\mathcal{F}\vert_{U_i}\cong \widetilde{M_i}$$가 되는 것이다. 만일 각 $$M_i$$가 finitely generated $$A_i$$-module이라면, $$\mathcal{F}$$를 *coherent sheaf<sub>연접층</sub>*라 부른다.

</div>

일반적으로 quasi-coherent sheaf를 다룰 때는 각각의 affine cover마다 다른 $$M$$이 붙어있을 수 있으므로 조심해야 하지만, affine case로만 한정할 경우 $$M\mapsto \widetilde{M}$$은 $$\lMod{A}$$에서 $$\QCoh(X)$$로의 categorical equivalence를 정의한다. 이는 임의의 quasi-coherent sheaf $$\mathcal{F}$$에 대하여, $$\widetilde{\Gamma(X,\mathcal{F})}$$가 $$\mathcal{F}$$ 자신을 복원한다는 것을 확인하면 된다. 즉 우리의 슬로건은, affine case에서는 quasi-coherent sheaf는 $$A$$-module이고, coherent sheaf는 finite rank $$A$$-module이라는 것이다.

이러한 관점에서는 vector bundle은 아주 특수한 경우의 (quasi-)coherent sheaf라 생각할 수 있다. 혹은 반대로 이들 (quasi-)coherent sheaf들을 생각할 때 아주 일반적인 형태의 vector bundle이라 생각해도 된다. 구체적으로, coherent sheaf는 (finite rank) vector bundle들의 category에서 이들이 abelian category의 연산, 즉 kernel이나 image, cokernel 등에 대해 닫혀있도록 하기 위해서 확장한 것이라 생각할 수 있으며 직관적으로는 fiber dimension이 점마다 달라질 수 있는 vector bundle이라 생각할 수 있다. Quasi-coherent sheaf는 여기에서 finite rank 조건까지 뺀 것이다. 

## Canonical Bundle

이제 우리는 canonical bundle을 정의할 준비가 되었다. 이를 위해서는 먼저 variety 위의 cotangent bundle을 도입해야 하는데, 다음 정의는 이미 [§선다발과 벡터다발, ⁋예시 24](/ko/math/algebraic_geometry/line_bundles#ex24)에서 살펴본 것이지만 완결성을 위해 다시 소개한다. 

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Smooth variety $$X$$의 *cotangent bundle<sub>여접다발</sub>* $$\Omega_X^1$$는 tangent bundle $$\mathcal{T}_X$$의 dual vector bundle이다. 

</div>

그럼 우리가 이전 섹션에서 살펴본 construction은 다음을 위한 것이다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Affine variety $$X$$와 $$X$$의 coordinate ring $$A$$에 대하여, $$\Omega_X^1$$은 $$\widetilde{\Omega}_{A/\mathbb{K}}$$에 대응되는 vector bundle이다. ([\[가환대수학\] §미분, ⁋정의 3](/ko/math/commutative_algebra/differentials#def3))

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

이를 위해서는 기존에 정의한 tangent bundle과 cotangent bundle을 sheaf 언어로 바꿔쓰는 것이 편할 것이다. 우선 tangent sheaf $$\mathcal{T}_X$$를 정의하자. $$X$$의 열린집합 $$U$$에 대하여, $$\mathcal{T}_X(U)$$를 $$\mathcal{O}_X(U)$$ 위의 $$\mathbb{K}$$-derivation들의 모임 $$\Der_\mathbb{K}(\mathcal{O}_X(U),\mathcal{O}_X(U))$$이 정의하는 sheaf를 tangent sheaf라 부른다. 

우리의 메인 도구는 Kähler differential의 universal property이다. ([\[가환대수학\] §미분, ⁋보조정리 2](/ko/math/commutative_algebra/differentials#lem2)) 즉, 임의의 $$A$$-module $$N$$에 대하여 natural isomorphism

$$\Der_\mathbb{K}(A,N)\cong\Hom_A(\Omega_{A/\mathbb{K}},N)$$

을 사용하자. 그럼 $$\widetilde{(-)}$$이 categorical equivalence라는 사실과 위의 natural isomorphicm에 의하여 

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}},\widetilde{N})\cong\Hom_A(\Omega_{A/\mathbb{K}},N)\cong\Der_\mathbb{K}(A,N)$$

이 성립한다. 뿐만 아니라, derivation들의 sheaf를 생각하면 마지막 항 $$\Der_\mathbb{K}(A,N)$$은 다시 $$\Der_\mathbb{K}(\mathcal{O}_X, \widetilde{N})$$이므로 다음의 식

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}}, \widetilde{N})\cong \Der_\mathbb{K}(\mathcal{O}_X, \widetilde{N})$$

이 성립한다. 특별히 $$N=A$$인 경우, 즉 $$\widetilde{N}=\mathcal{O}_X$$인 경우를 생각하면

$$\Hom_{\mathcal{O}_X}(\widetilde{\Omega_{A/\mathbb{K}}}, \mathcal{O}_X)\cong\Der_\mathbb{K}(\mathcal{O}_X, \mathcal{O}_X)\cong \mathcal{T}_X$$

이 성립한다. 한편, $$\Omega_{A/\mathbb{K}}$$이 finitely generated projective $$A$$-module이라는 사실로부터 $$\widetilde{\Omega_{A/\mathbb{K}}^\vee}\cong \widetilde{\Omega_{A/\mathbb{K}}}^\vee$$임을 알고, 따라서

$$\widetilde{\Omega_{A/\mathbb{K}}}^\vee\cong \widetilde{\Omega_{A/\mathbb{K}}^\vee}\cong \widetilde{\Der_\mathbb{K}(A,A)}\cong \mathcal{T}_X$$

이므로 원하는 주장이 성립한다. 

</details>

이 결과는 cotangent bundle이 우리가 상상하는 것처럼 differential $$1$$-form들로 나타난다는 것을 보여준다. 

<div class="example" markdown="1">

<ins id="ex4">**예시 4**</ins> $$\mathbb{A}^n$$의 cotangent bundle은 $$\Omega_{\mathbb{A}^n}^1 \cong \mathcal{O}_{\mathbb{A}^n}^{\oplus n}$$이다. 대수적으로, 만일 $$\mathbb{A}^n$$의 coordinate ring $$\mathbb{K}[\x_1, \ldots, \x_n]$$을 고정하면 이 $$\mathbb{K}$$-algebra의 Kähler differentials은 free module $$\bigoplus_{i=1}^n \mathbb{K}[\x_1, \ldots, \x_n]  d\x_i$$이므로, 이 결과는 우리의 직관과 잘 맞아떨어진다.

</div>

한편 우리는 임의의 smooth variety $$X$$ of dimension $$n$$과 그 위의 cotangent bundle $$\Omega_X^1$$에 대하여, $$\Omega_X^1$$의 각 fiber는 $$n$$차원이므로 이를 $$n$$번 exterior product한 것은 line bundle이 되는 것을 안다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> Smooth variety $$X$$ of dimension $$n$$의 *canonical line bundle<sub>표준 선다발</sub>* $$\omega_X$$를 cotangent bundle의 top exterior power

$$\omega_X = \bigwedge\nolimits^{\!n} \Omega_X^1$$

로 정의한다. 

</div>

우리는 canonical bundle $$\omega_X$$의 global section $$s\in \Gamma(X, \omega_X)$$을 $$X$$ 위의 *regular $$n$$-form*이라 부른다. 이들은 만일 $$\omega_X$$의 trivializing open set $$U$$를 잡고, 이를 [예시 4](#ex4)과 같이 affine space 위의 cotangent bundle로 identify할 경우 regular function $$f$$에 대하여 $$fd\x_1 \wedge \cdots \wedge d\x_n$$의 꼴로 나타나는 $$n$$-form들이다. 

한편 우리는 line bundle과 divisor class의 대응으로부터 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Canonical bundle $$\omega_X$$에 대응하는 divisor class를 *canonical divisor*라 하고 $$K_X$$로 표기한다. 즉, $$\omega_X \cong \mathcal{O}_X(K_X)$$이다.

</div>

이를 위해서는 [§선다발과 벡터다발, ⁋명제 19](/ko/math/algebraic_geometry/line_bundles#prop19)를 사용하므로, $$K_X$$는 오직 divisor class로만 정의된다는 것에 유의하자.

## $$\mathbb{P}^n$$의 Canonical Bundle

앞선 글들과 마찬가지로, 우리에게 가장 친숙한 예시는 $$\mathbb{P}^n$$의 예시이다. 직관적으로 $$\mathbb{P}^n$$을 정의하는 quotient

$$\mathbb{P}^n=(\mathbb{A}^{n+1}\setminus\{0\})/\mathbb{K}^\ast$$

을 뜯어보면, $$\mathbb{K}^\ast$$-action은 원점을 중심으로 뻗어나가는 방향, 즉 Euler vector field가 정의하는 방향의 작용이며 이는 $$\mathbb{P}^n$$ 입장에서는 그냥 trivial line bundle에 불과하다. 그럼 $$\mathbb{P}^n$$의 tangent space는 $$\mathbb{A}^{n+1}$$의 방향, 즉 1차식들을 이 trivial line bundle로 quotient한 후 남은 부분에 해당한다. 즉 tangent bundle에 해당하는 다음의 short exact sequence

$$0 \rightarrow \mathcal{O}_{\mathbb{P}^{n}}\rightarrow \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus (n+1)}\rightarrow T_{\mathbb{P}^n}\rightarrow 0$$

가 존재하며 여기에 dual을 취하면 다음을 얻는다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7 (Euler Exact Sequence)**</ins> $$\mathbb{P}^n$$ 위에 정의된 vector bundle들의 exact sequence

$$0 \rightarrow \Omega_{\mathbb{P}^n}^1 \rightarrow \mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)} \rightarrow \mathcal{O}_{\mathbb{P}^n} \rightarrow 0$$

가 존재한다. 

</div>

이제 $$\mathbb{P}^n$$의 canonical bundle을 계산하기 위해서는 이 exact sequence에 top exterior power를 취해야 한다. 더 일반적으로, 다음의 short exact sequence

$$0\rightarrow E\rightarrow F\rightarrow L\rightarrow 0$$

이 주어졌다 하자. 이때 $$E$$는 rank $$r$$, $$L$$은 rank $$1$$의 vector bundle이라 하자. 이 sequence에 $$\bigwedge\nolimits^{\!r}(-)$$를 취하면, determinant가 tensor product와 compatible이라는 사실로부터

$$\det(F)\cong \det(E)\otimes \det(L)$$

임을 안다. 이제 [명제 7](#prop7)의 Euler exact sequence에 이를 적용하자. $$E=\Omega_{\mathbb{P}^n}^1$$은 rank $$n$$, $$F=\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)}$$은 rank $$n+1$$, $$L=\mathcal{O}_{\mathbb{P}^n}$$은 rank $$1$$이므로

$$\det(\mathcal{O}_{\mathbb{P}^n}(-1)^{\oplus(n+1)})\cong \det(\Omega_{\mathbb{P}^n}^1)\otimes \det(\mathcal{O}_{\mathbb{P}^n})$$

이다. 우변의 $$\det(\mathcal{O}_{\mathbb{P}^n})\cong \mathcal{O}_{\mathbb{P}^n}$$이고, 좌변은 $$\mathcal{O}_{\mathbb{P}^n}(-1)^{\otimes(n+1)}\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$이므로

$$\omega_{\mathbb{P}^n}=\det(\Omega_{\mathbb{P}^n}^1)\cong \mathcal{O}_{\mathbb{P}^n}(-n-1)$$

을 얻는다. 이 때 canonical divisor는 $$K_{\mathbb{P}^n}=-(n+1)H$$로 주어진다. 이 계산과 [§선다발과 벡터다발, ⁋예시 16](/ko/math/algebraic_geometry/line_bundles#ex16)부터 $$\omega_{\mathbb{P}^n}$$은 regular section을 갖지 않는다는 것을 안다. 

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> 위의 계산을 $$n$$-form의 transition function 관점에서도 확인할 수 있다. $$\mathbb{P}^n$$의 standard open cover $$U_i = \{\x_i \neq 0\}$$ 위에서 affine coordinate을 $$\y_j^{(i)} = \x_j / \x_i$$ ($$j \neq i$$)로 놓으면, $$U_i$$ 위의 $$n$$-form 

$$d \y_1^{(i)} \wedge \cdots \wedge \widehat{d \y_i^{(i)}} \wedge \cdots \wedge d \y_n^{(i)}$$

을 생각할 수 있다. $$U_i \cap U_j$$ 위에서 $$\y_k^{(j)} = \x_k / \x_j = (\x_k / \x_i) / (\x_j / \x_i) = \y_k^{(i)} / \y_j^{(i)}$$이므로, $$k \neq i, j$$에 대해 

$$d \y_k^{(j)} = d(\y_k^{(i)} / \y_j^{(i)}) = \frac{\y_j^{(i)} d \y_k^{(i)} - \y_k^{(i)}  d \y_j^{(i)}}{(\y_j^{(i)})^2}$$

이다. 따라서 $$U_j$$ 위의 $$n$$-form은 $$U_i \cap U_j$$에서

$$\bigwedge_{k \neq j} d \y_k^{(j)} = (\y_j^{(i)})^{-(n+1)} \cdot \bigwedge_{k \neq i} d \y_k^{(i)}$$

로 변환된다. 여기서 $$(\y_j^{(i)})^{-(n+1)} = (\x_j / \x_i)^{-(n+1)}$$이므로, transition function이 $$g_{ij} = (\x_i / \x_j)^{-(n+1)}$$임을 확인할 수 있다. 이는 $$\mathcal{O}_{\mathbb{P}^n}(-n-1)$$의 transition function과 일치한다.

</div>

## Adjunction Formula

많은 경우, 우리는 $$\mathbb{P}^n$$으로부터 적당히 많은 다항식들을 통해 얻어지는 variety들에 관심이 있다. 직관적으로 이는 smooth variety $$X$$의 smooth divisor $$D$$들을 계속하여 생각하여 얻아지는 것이다. 다음의 *adjunction formula*는 이러한 경우 $$X$$의 canonical line bundle로부터 $$D$$의 canonical line bundle을 계산하는 방법을 알려준다. 

이를 위해, smooth variety $$X$$와 smooth divisor $$D$$에 대하여 다음의 short exact sequence

$$0\rightarrow \mathcal{I}_D\rightarrow \mathcal{O}_X\rightarrow \mathcal{O}_D\rightarrow 0$$

을 만족하는 ideal sheaf $$\mathcal{I}_D=\mathcal{O}_X(-D)$$를 기억하자. ([§선다발과 벡터다발, ⁋정의 17](/ko/math/algebraic_geometry/line_bundles#def17)) 그럼 이로부터 $$\mathcal{I}_D$$의 일차근사 부분은

$$\mathcal{I}_D/\mathcal{I}_D^2=\mathcal{I}_D\otimes_{\mathcal{O}_X}\mathcal{O}_D=\mathcal{O}_X(-D)\vert_D$$

으로 주어지는 것을 계산할 수 있다. 한편 $$X$$와 $$D$$의 tangent sheaf $$\mathcal{T}_X=\Der(\mathcal{O}_X)$$, $$\mathcal{T}_D=\Der(\mathcal{O}_D)$$를 각각 계산하자. 그럼 natural inclusion $$\mathcal{T}_D\rightarrow \mathcal{T}_X\vert_D$$이 존재하며, 이것의 cokernel을 *normal sheaf* $$\mathcal{N}_{D/X}$$으로 정의한다. 즉 다음의 short exact sequence

$$0\rightarrow \mathcal{T}_D\rightarrow \mathcal{T}_X\vert_D\rightarrow \mathcal{N}_{D/X}\rightarrow 0$$

이 존재한다. 그럼 우리는 이 normal bundle $$\mathcal{N}_{D/X}$$의 dual이 곧 $$\mathcal{I}_D/\mathcal{I}_D^2$$가 된다는 것을 확인할 수 있다. 이러한 이유로 우리는 이를 *conormal sheaf*라 부르며, 구체적으로 이는 위의 short exact sequence의 dual에 해당하는

$$0 \rightarrow \mathcal{I}_D/\mathcal{I}_D^2\rightarrow \Omega_X^1\lvert D\rightarrow \Omega_D^1\rightarrow 0$$

을 확인하여 얻어진다. 여기서 첫째 화살표는 $$f\mapsto df$$로 주어진다. 이 short exact sequence에 top exterior power를 취하면 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> (Adjunction Formula) Smooth variety $$X$$의 smooth divisor $$D$$에 대해

$$\omega_D \cong (\omega_X \otimes \mathcal{O}_X(D))\vert_D$$

이다.

</div>

이로부터 canonical divisor에 대한 주장 또한 바로 따라온다. 어쨌든, 이 명제가 담고 있는 주장은 ambient variety $$X$$의 canonical bundle $$\omega_X$$를 normal bundle $$\mathcal{O}_X(D)$$로 twist한 후 $$D$$로 restrict하면, subvariety $$D$$의 canonical bundle $$\omega_D$$가 나온다. 쉽게 말해, $$D$$ 위의 differential form은 ambient space의 differential form에 normal direction의 정보를 추가하여 얻어진다는 것이다. 

다음 예시는 이를 사용한 계산을 구체적으로 보여준다. 

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> $$C \subset \mathbb{P}^2$$가 degree $$d$$의 smooth curve라 하자. Adjunction formula에 의해

$$\omega_C \cong \omega_{\mathbb{P}^2}\vert_C \otimes \mathcal{O}_{\mathbb{P}^2}(C)\vert_C \cong \mathcal{O}_{\mathbb{P}^2}(-3)\vert_C \otimes \mathcal{O}_{\mathbb{P}^2}(d)\vert_C \cong \mathcal{O}_C(d-3)$$

이다. 따라서 $$K_C \sim (d-3)H\vert_C$$이며, 이 때 $$H\vert_C$$의 degree가 $$d$$이므로 $$\deg K_C = d(d-3)$$이다. 

한편, classical한 algebraic geometry에서 plane curve (즉 projective curve in $$\mathbb{P}^2$$)의 genus는 그 degree로부터 

$$g=\frac{(d-1)(d-2)}{2}$$

로 주어진다는 사실이 잘 알려져 있다. ([Degree-genus formula](https://en.wikipedia.org/wiki/Genus%E2%80%93degree_formula)) 이로부터 우리는

$$\deg K_C=d(d-3)=(d-1)(d-2)-2=2g-2$$

가 됨을 확인할 수 있다. 

</div>

Degree-genus formula는, 실은 다음 글에서 살펴볼 Riemann-Roch theorem의 특수한 경우이며, 우리는 다음 글에서 이를 사용하여 smooth curve를 살펴볼 것이다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977. (II.8. Differentials; III.7. The Dualizing Sheaf)