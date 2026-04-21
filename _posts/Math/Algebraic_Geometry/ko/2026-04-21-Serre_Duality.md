---
title: "세르 쌍대성"
excerpt: "Serre duality theorem and its applications"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/serre_duality
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Serre_Duality.png
    overlay_filter: 0.5

date: 2026-04-21
last_modified_at: 2026-04-22
weight: 15

---

기하적으로 좋은 경우 dimension $$k$$의 cohomology와 codimension $$k$$ cohomology 사이에는 자연스러운 쌍대성이 존재한다. 이를 증명하기 위해 우리는 perfect pairing

$$H^k(M;R)\times H^{n-k}(M;R)\rightarrow R$$

을 사용했으며, 이를 통해 [\[대수적 위상수학\] §푸앵카레 쌍대성, ⁋정리 11](/ko/math/algebraic_topology/Poincare_duality#thm11)와 같은 결과를 얻었다. 더 구체적으로, 이 pairing은 cap product와 fundamental class $$[M] \in H_n(M;R)$$를 통해 구성되므로 위상수학에서 duality의 원천은 orientation class $$[M]$$이라 할 수 있다. 

이번 글에서 우리는 대수기하학 버전의 duality인 Serre duality를 살펴본다. 

## 사영공간에서의 세르 쌍대성

우리는 우선 $$X=\mathbb{P}^n$$인 경우만 엄밀하게 살펴본다. 우리는 $$\mathbb{P}^n$$ 위에 정의된 line bundle은 모두 $$\mathcal{O}(d)$$의 꼴인 것을 알고 있으며, 특히 [§표준선다발, ⁋명제 7](/ko/math/algebraic_geometry/canonical_bundle#prop7)에서 이것이 $$\mathcal{O}(-n-1)$$임을 살펴보았다. 그럼 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)에서 우리는 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Projective space $$X=\mathbb{P}^n$$ 위의 canonical line bundle $$\omega_X$$에 대하여, isomorphism

$$H^n(X, \omega_X)\cong \mathbb{K}$$

이 존재한다. 

</div>

일반적으로 이는 명시적으로 $$\x_0^{-1}\cdots\x_n^{-1}$$을 basis로 두는 isomorphism으로 이해되지만, scalar multiplication에 대해서만 유일하게 결정된다. 이렇게 normalization을 택하는 것은 구체적으로 *trace map* $$\tr:H^n(\mathbb{P}^n, \omega_{\mathbb{P}^n}) \to \mathbb{K}$$을 택하는 것과 같다. 

이제 duality pairing을 얻기 위해서는 cup product를 정의해야 한다. 편의상 Čech cohomology 레벨에서 생각하자. 임의의 위상공간 $$X$$와 $$X$$의 open cover $$\mathcal{U}$$, 그리고 $$X$$ 위에 정의된 sheaf $$\mathcal{F}$$, $$\mathcal{G}$$에 대하여, 두 Čech cochain $$\alpha \in \check{C}^i(\mathcal{U}, \mathcal{F})$$, $$\beta \in \check{C}^j(\mathcal{U}, \mathcal{G})$$의 cup product를 다음의 식

$$(\alpha \smile \beta)_{i_0, \ldots, i_{i+j}} = \alpha_{i_0,\ldots,i_i}\big\vert_{U_{i_0,\ldots,i_{i+j}}} \otimes \beta_{i_i,\ldots,i_{i+j}}\big\vert_{U_{i_0,\ldots,i_{i+j}}}\in \check{C}^{i+j}(\mathcal{U}, \mathcal{F}\otimes\mathcal{G})$$

으로 정의한다. 우리는 이것이 cohomology 레벨로 떨어진다는 것을 명시적으로 계산할 수 있으며, 이로부터 다음의 함수

$$\smile:\check{H}^i(\mathcal{U}, \mathcal{F}) \times \check{H}^j(\mathcal{U}, \mathcal{G}) \to \check{H}^{i+j}(\mathcal{U}, \mathcal{F} \otimes \mathcal{G})$$

가 정의된다. Sheaf cohomology 레벨에서도 $$\mathcal{F}$$와 $$\mathcal{G}$$의 injective resolution $$\mathcal{I}^\bullet$$, $$\mathcal{J}^\bullet$$을 각각 잡은 후, 이들의 tensor product complex (즉 각각의 성분이 $$\mathcal{I}^p\otimes \mathcal{J}^q$$인 double complex의 total complex)가 $$\mathcal{F}\otimes \mathcal{G}$$의 resolution을 정의한다는 사실을 이용하면 이를 정의할 수 있다. 

어쨌든, cup product pairing에 의하여 우리는 임의의 locally free sheaf $$\mathcal{E}$$와 $$\omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee$$의 cocycle에 대하여 다음의 bilinear map

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)\rightarrow H^n(\mathbb{P}^n, \mathcal{E}\otimes \omega_{\mathbb{P}^n}\otimes \mathcal{E}^\vee)$$

을 얻은 후, isomorphism $$\mathcal{E}\otimes \mathcal{E}^\vee\rightarrow \mathcal{O}_{\mathbb{P}^n}$$과 위에서의 trace map을 활용하여 bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E})\times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)\rightarrow \mathbb{K}$$

를 얻는다. 우리는 이를 $$\mathcal{O}(d)$$의 경우에 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)에서 직접 계산하여 non-degeneracy를 보이고, syzygy theorem을 사용하여 이 non-degeneracy를 일반적인 locally free sheaf $$\mathcal{E}$$에 대하여 보일 수 있다.

지금까지의 논의에서 다음을 얻는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2 (Serre duality pairing, projective case)**</ins> $$\mathbb{P}^n$$ 위의 locally free sheaf $$\mathcal{E}$$에 대해 bilinear form

$$H^k(\mathbb{P}^n, \mathcal{E}) \times H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n} \otimes \mathcal{E}^\vee) \to \mathbb{K};\quad (\alpha, \beta) \mapsto \tr(\alpha \smile \beta)$$

은 perfect pairing이다.

</div>

더 명시적으로, 일반적으로 Serre duality는 이로부터 얻어지는 다음의 isomorphism

$$H^k(\mathbb{P}^n, \mathcal{E})\cong H^{n-k}(\mathbb{P}^n, \omega_{\mathbb{P}^n}\otimes\mathcal{E}^\vee)^\ast$$

를 의미한다. 

더 일반적으로, Noether normalization theorem에 의해 임의의 $$n$$차원 smooth projective variety $$X$$에 대하여 finite surjective morphism $$f: X \to \mathbb{P}^n$$이 존재한다. 그럼 우리는 이 finite morphism $$f$$를 통해 $$\mathbb{P}^n$$에서 증명한 Serre duality를 $$X$$로 옮겨올 수 있으며, 이러한 세팅에서 Serre duality는 다음 isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

을 의미한다.

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> $$\mathbb{P}^2$$에서 [명제 2](#prop2)를 구체적으로 살펴보자. 여기에서 $$\omega_{\mathbb{P}^2} \cong \mathcal{O}(-3)$$이므로, Serre duality가 주장하는 바는 isomorphism $$H^k(\mathbb{P}^2, \mathcal{O}(d)) \cong H^{2-k}(\mathbb{P}^2, \mathcal{O}(-d-3))^\ast$$이다.

우선 $$d=0$$인 경우, [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)에 의해 

$$H^0(\mathbb{P}^2, \mathcal{O}) = \mathbb{K},\qquad H^1(\mathbb{P}^2, \mathcal{O}) = 0, \qquad H^2(\mathbb{P}^2, \mathcal{O}) = 0$$

이며 $$\mathcal{O}(-3)$$의 cohomology는 

$$H^0(\mathbb{P}^2, \mathcal{O}(-3)) = 0, \qquad H^1(\mathbb{P}^2, \mathcal{O}(-3)) = 0,\qquad H^2(\mathbb{P}^2, \mathcal{O}(-3)) = \mathbb{K}$$

이 되어 Serre duality가 성립하는 것을 알 수 있다. 비슷하게 $$d=1$$인 경우에서도, 유일한 nonzero cohomology는

$$H^0(\mathbb{P}^2, \mathcal{O}(1)) = \mathbb{K}^3$$

이며, Serre duality에 의해 $$H^0(\mathcal{O}(1)) \cong H^2(\mathcal{O}(-4))^\ast$$이어야 하므로 $$\dim H^2(\mathcal{O}(-4)) = 3$$이어야 할 것이다. 다시 [§사영공간의 코호몰로지, ⁋명제 1](/ko/math/algebraic_geometry/cohomology_of_projective_spaces#prop1)를 적용하면 실제로 $$\mathcal{O}(-4)$$의 $$H^2$$는 

$$\binom{2+(-4)}{2}=\binom{-2}{2} = 3$$

차원이므로 일치하는 것을 확인할 수 있다.

</div>

## 세르 쌍대성의 일반화

우리는 지금까지의 논의를 일반화시킨다. 가장 처음으로 할 수 있는 것은 locally free sheaf $$\mathcal{E}$$를 임의의 coherent sheaf $$\mathcal{E}$$로 확장하는 것이다. 이는 생각보다 어려운 일은 아닌데, smooth variety에서는 임의의 coherent sheaf가 finite length locally free resolution을 갖기 때문으로, Serre duality의 주장을 귀납적으로 사용하면 된다. ([§표준선다발, ⁋정의 1](/ko/math/algebraic_geometry/canonical_bundle#def1))

그 후 우리는 $$X$$에서 smooth 조건을 포기한다. 이 경우 크게 두 가지의 문제가 있는데, 처음으로 보이는 문제는 $$X$$가 canonical line bundle을 갖지 않는다는 사실이다. 또 다른 문제는 약간 미묘한 것으로, 우리는 perfect pairing에서 명시적인 isomorphism을 얻어낼 때 다소 implicit하게 다음의 isomorphism

$$\mathcal{H}om(\mathcal{E}, \mathcal{F})\cong \mathcal{E}^\vee\otimes \mathcal{F}$$

를 사용하였으나, 실제로 이는 $$\mathcal{E}$$가 locally free이기 때문에 가능한 것으로, 만일 $$\mathcal{E}$$가 coherent sheaf이고 $$X$$가 singular라면 $$\mathcal{E}$$가 finite length locally free resolution을 갖는다는 보장이 없으므로 이 isomorphism이 성립하지 않는다. 때문에 우리는 다시 derived functor를 도입하여, 다음의 식

$$\Ext^i_X(\mathcal{F},\omega_X)\cong H^{n-i}(X,\mathcal{F})^\vee$$

을 만족하는 $$\omega_X$$를 $$X$$의 *dualizing sheaf*라 부른다. 일반적으로 이는 Cohen-Macaulay variety of pure dimension $$n$$에 대하여는 그 존재성이 보장되며, 정의를 내리지는 않을 것이지만 Cohen-Macaulay condition은 직관적으로 차원 문제를 일으키지 않는 singular variety들을 포함하는 개념이라 생각하면 된다.

조금 덜 직관적인 버전의 일반화는 relative Serre duality이다. 우리는 그 동안 variety의 underlying field $$\mathbb{K}$$에 대해 신경을 쓰지 않은 것이 사실이지만, 이 맥락에서는 그 역할을 명확하게 하는 것이 도움이 된다. 

Affine variety $$X$$가 $$\mathbb{K}$$ 위에서 정의되었다는 것은 그 coordinate ring $$A$$가 $$\mathbb{K}$$-algebra라는 것으로, 이 구조를 담는 ring homomorphism $$\mathbb{K}\rightarrow A$$가 존재한다. 이를 각각 $$\mathbb{A}^1_\mathbb{K}$$와 $$X$$의 coordinate ring 사이의 morphism으로 본다면, 이 structure morphism은 기하적으로는 $$X\rightarrow \mathbb{A}^1_\mathbb{K}$$로 주어지게 된다.

Relative Serre duality는 이 세팅을 일반화하는 것으로, target $$\mathbb{A}^1_\mathbb{K}$$를 또 다른 variety로 바꿔준다. 우선 임의의 variety $$X,Y$$에 대하여, morphism $$f:X\rightarrow Y$$가 *smooth projective morphism*이라는 것을 각각의 $$y\in Y$$ 위에서의 fiber $$f^{-1}(y)$$가 smooth projective variety가 되는 것으로 정의하자. 그럼 이 경우, $$f^{-1}(y)$$는 smooth projective variety로서 canonical line bundle $$\omega_{X_y}$$가 존재할 것이며, 이들을 일관적으로 모은 *relative dualizing sheaf* $$\omega_{X/Y}$$가 $$X$$ 위에 정의된다. 즉 $$\omega_{X/Y}$$는 각각의 $$y$$에 대하여 $$\omega_{X/Y}\vert_{X_y}\cong\omega_{X_y}$$을 만족하는 sheaf이다. 그럼 이 때의 일반화는 다음과 같다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4 (Relative Serre duality)**</ins> Smooth projective morphism $$f \colon X \to Y$$에서 $$n = \dim X - \dim Y$$라 하자. 그럼

$$R^n f_\ast \omega_{X/Y} \cong \mathcal{O}_Y$$

이며, $$i \neq n$$에 대해서는 $$R^i f_\ast \omega_{X/Y} = 0$$이다.

</div>

## Grothendieck Duality

앞서 Serre duality를 일반화하는 과정들을 되짚어보자. 우리는 먼저 $$\mathbb{P}^n$$ 위에서 trace map과 cup product를 사용하여 Serre duality를 증명하였고 ([명제 2](#prop2)), 이를 finite morphism을 통해 임의의 smooth projective variety로 확장하였다. 이후 coherent sheaf로의 확장은 locally free resolution을 통한 귀납으로 처리하였고, singular variety로의 확장은 dualizing sheaf의 도입으로 처리하였다. Relative Serre duality ([명제 4](#prop4))는 target을 point에서 임의의 variety로 바꾼 일반화였다.

Serre duality의 가장 현대적인 해석은 Grothendieck duality로, 이는 derived category의 언어에서 서술된다. ([\[호몰로지 대수학\] §유도카테고리, ⁋정의 2](/ko/math/homological_algebra/derived_categories#def2)) 이 일반화는 그 언어에 비해 motivation은 상당히 설득력 있는 것으로, 가령 우리는 sheaf cohomology를 정의할 때만 해도 injective resolution을 생각해야 했고, 위에서 Serre duality를 임의의 coherent sheaf로 일반화할 때도 locally free resolution을 생각해야 했으므로 derived category가 모든 일이 실제로 일어나는 곳임을 안다. 특히 핵심적인 내용은 Serre duality에서 perfect pairing이, 사실은 구체적인 isomorphism

$$H^n(X, \omega_X) \cong \mathbb{K}$$

의 선택과 같은 정보라는 것이며, 이를 derived category로 올리면 derived pushforward $$R f_\ast$$와 그 right adjoint 사이의 adjunction의 특수한 경우라는 관찰이다. 구체적으로, Serre duality의 isomorphism

$$H^i(X, \mathcal{E}) \cong H^{n-i}(X, \omega_X \otimes \mathcal{E}^\vee)^\ast$$

은 derived category에서 다음의 adjunction isomorphism

$$\operatorname{Hom}_{D(X)}(\mathcal{F}, f^! \mathcal{G}) \cong \operatorname{Hom}_{D(Y)}(R f_\ast \mathcal{F}, \mathcal{G})$$

으로부터 도출된다. 여기서 *exceptional inverse image* $$f^!$$는 derived category에서 $$R f_\ast$$의 right adjoint로 정의되는 functor이며, 이를 잘 정의하기 위해서는 반드시 derived category에서 이를 서술해야만 한다.

앞서 말했듯 Grothendieck duality는 relative Serre duality를 포함하는 결과이다. 이를 살펴보기 위해 smooth morphism $$f:X\rightarrow Y$$의 경우를 생각하면, $$f^! \mathcal{O}_Y \cong \omega_{X/Y}[n]$$이 성립하며, 이로부터 $$\omega_{X/Y}$$가 올바른 dimension에 들어있는 것이 정확히 $$f^!\mathcal{O}_Y$$임을 알 수 있다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Grothendieck Duality)**</ins> Proper morphism $$f \colon X \to Y$$와 coherent sheaf $$\mathcal{F}$$ on $$X$$에 대해, derived category에서 다음 isomorphism이 성립한다:

$$R f_\ast R\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F}, f^! \mathcal{G}) \cong R\mathcal{H}om_{\mathcal{O}_Y}(R f_\ast \mathcal{F}, \mathcal{G})$$

여기서 $$R\mathcal{H}om$$은 derived Hom ([\[호몰로지 대수학\] §유도카테고리, ⁋명제 10](/ko/math/homological_algebra/derived_categories#prop10))이며, $$\mathcal{G}$$는 $$Y$$ 위의 coherent sheaf의 bounded complex이다. 

</div>

직관적으로 이 정리는 'pushforward 후 Hom'과 'Hom 후 pushforward'가 같다는 것을 의미한다. 즉, $$\mathcal{F}$$와 $$f^! \mathcal{G}$$ 사이의 Hom을 $$X$$에서 계산한 후 $$Y$$로 내려보내는 것과, $$\mathcal{F}$$를 먼저 $$Y$$로 내려보낸 후 $$\mathcal{G}$$와의 Hom을 계산하는 것이 같다는 뜻이다. 

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics, Springer, 1977.  
**[Ser]** J.-P. Serre, *Faisceaux algébriques cohérents*, Annals of Mathematics, 1955.

---