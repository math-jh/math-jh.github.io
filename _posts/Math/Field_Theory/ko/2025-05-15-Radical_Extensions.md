---
title: "제곱근확대체"
description: "갈루아 이론의 기본 아이디어를 제곱근확대체의 예시를 통해 소개한다. 성질이 좋은 수체의 확대에서 다항식의 근들을 바꾸는 작용으로 갈루아 군을 정의하는 과정을 다룬다."
excerpt: "Radical extension의 정의와 Galois theory에서의 역할"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/radical_extensions
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-15
last_modified_at: 2025-05-15
weight: 4
published: false

---

우리가 살펴볼 갈루아 이론의 큰 테마를 아주 간단한 예시에서 살펴보자. 가령 $$\mathbb{Q}$$의 degree $$4$$ extension $$\mathbb{Q}(\sqrt{2}, \sqrt{3})$$을 생각하면, $$\mathbb{Q}$$로부터 새로 추가되는 원소들인 $$\sqrt{2}$$와 $$\sqrt{3}$$은 각각 유리수계수의 minimal polynomial들

$$\x^2-2,\qquad \x^2-3$$

으로부터 나오는 것이다. 그런데 이 두 다항식을 각각 살펴보면, 이들은 각각 두 개의 근 $$\pm \sqrt{2}$$, $$\pm\sqrt{3}$$을 가지는 다항식이며 이를 $$\mathbb{Q}$$에서는 대수적인 방식으로 구별할 방법이 없다. 따라서 이들 근을 서로 바꾸는 action (혹은 $$\mathbb{Q}(\sqrt{2},\sqrt{3})$$의 $$\mathbb{Q}$$-automorphism)을 생각하면, 즉 permutation group $$S_2\times S_2$$를 생각하면 이것은 $$S_4$$의 subgroup이다. 

이와 같은 방식으로 우리는 다항식이 주어질 때마다 적절한 Galois group을 정의해줄 수 있고, 이들을 보는 것이 $$\mathbb{Q}$$의 extension들을 분류해줄 수 있다는 것이 갈루아 이론의 철학이다. 

그러나 이러한 철학을 바탕으로 생각했을 때, 가령 minimal polynomial이 중근을 갖는다면 permutation action을 정의하기가 상당히 껄끄러워질 것이다. 이는 $$\mathbb{Q}$$에서는 기우이지만, 어떠한 경우에는 이러한 일이 실제로 일어날 수도 있다. 

<div class="remark" markdown="1">

**참고** 이번 글에서 등장하는 모든 field는 characteristic exponent $$p$$를 갖는다.

</div>

## $$p$$-제곱근확대체

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field extension $$\mathbb{L}/\mathbb{K}$$에 대하여, $$x\in \mathbb{L}$$이 *$$p$$-radical*이라는 것은 어떠한 $$m\geq 0$$이 존재하여 $$x^{p^m}\in \mathbb{K}$$이도록 할 수 있는 것이다. 이러한 $$m$$들 중 가장 작은 것을 $$x$$의 *height*라 부른다. 

</div>

만일 $$p=1$$이라면 위의 정의는 별 의미가 없으며, 이번 글에서 나올 나머지 내용들 또한 마찬가지이다. 즉, 본질적으로 이번 글의 내용은 모두 characteristic $$p$$의 field에 대한 것이라 보아도 된다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Field extension $$\mathbb{L}/\mathbb{K}$$와 $$p$$-radical element $$x\in \mathbb{K}$$ of height $$e$$를 고정하자. 그럼 $$a=x^{p^e}\in \mathbb{K}$$에 대하여, $$x$$의 minimal polynomial은

$$\x^{p^e}-a\in \mathbb{K}[\x]$$

으로 주어진다. 따라서 $$[\mathbb{K}(x):\mathbb{K}]=p^e$$이다. 

</div>

Frobenius endomorphism $$\Frob_p:\mathbb{K}\rightarrow \mathbb{K}$$의 image를 우리는 $$\mathbb{K}^p$$라 적기로 하였다. $$e$$의 최소성에 의하여 $$a\not\in \mathbb{K}^p$$이므로, 주장은 다음 보조정리의 결과이다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Field $$\mathbb{K}$$의 원소 $$a$$가 $$a\not\in \mathbb{K}^p$$를 만족한다 가정하자. 그럼 임의의 $$e\geq 0$$에 대하여, $$f(\x)=\x^{p^e}-a$$는 $$\mathbb{K}[\x]$$의 irreducible polynomial이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

만일 $$p=1$$이라면 $$\mathbb{K}^p=\mathbb{K}$$이므로 가정을 만족하는 $$a$$가 존재하지 않는다. 따라서 $$p$$가 prime인 경우만 보면 충분하다. 또 $$e=0$$이라면 $$f$$는 일차식이므로 자명하게 irreducible이다. 이제 $$e\geq 1$$이라 하자.

$$\overline{\mathbb{K}}$$에서 $$f$$의 근 $$\alpha$$를 하나 택하자. 즉 $$\alpha^{p^e}=a$$이다. 그럼 [§체, ⁋정리 10](/ko/math/field_theory/fields#thm10)의 Frobenius endomorphism을 characteristic $$p$$의 ring $$\overline{\mathbb{K}}[\x]$$에 반복하여 적용하면

$$f(\x)=\x^{p^e}-\alpha^{p^e}=(\x-\alpha)^{p^e}$$

이 성립한다. 한편, 만일 어떠한 $$m<e$$에 대하여 $$\alpha^{p^m}\in \mathbb{K}$$라면 $$a=(\alpha^{p^m})^{p^{e-m}}\in \mathbb{K}^p$$가 되어 가정에 모순이므로, $$\alpha^{p^m}\in\mathbb{K}$$이도록 하는 $$m$$은 반드시 $$m\geq e$$를 만족해야 한다.

이제 $$g\in \mathbb{K}[\x]$$가 $$f$$의 monic factor라 하자. 그럼 $$\overline{\mathbb{K}}[\x]$$에서 $$g$$는 $$(\x-\alpha)^{p^e}$$의 monic factor이므로, 적당한 $$0< d\leq p^e$$에 대하여 $$g=(\x-\alpha)^d$$의 꼴이어야 한다. $$d=p^cu$$로 적자. 여기서 $$u$$는 $$p$$와 서로소인 양의 정수이다. 그럼 다시 Frobenius에 의하여

$$g=\bigl((\x-\alpha)^{p^c}\bigr)^u=(\x^{p^c}-\alpha^{p^c})^u$$

이고, 이를 전개하면 $$\x^{p^c(u-1)}$$의 계수는 $$-u\alpha^{p^c}$$이다. $$g\in\mathbb{K}[\x]$$이므로 $$-u\alpha^{p^c}\in \mathbb{K}$$인데, $$p$$가 $$u$$를 나누지 않으므로 $$u\cdot 1$$은 $$\mathbb{K}$$에서 invertible이고 따라서 $$\alpha^{p^c}\in \mathbb{K}$$이다. 그럼 앞 문단에서 살펴본 것에 의하여 $$c\geq e$$여야 하고, 따라서 $$d\geq p^c\geq p^e$$이므로 $$d=p^e$$, 즉 $$g=f$$이다. 그러므로 $$f$$는 일차 이상의 monic factor로 자기 자신만을 가지며, 이는 $$f$$가 irreducible이라는 뜻이다.

</details>

다음 정의는 [정의 1](#def1) 직후에 왔어도 자연스러웠을 것이다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Field extension $$\mathbb{L}/\mathbb{K}$$가 *$$p$$-radical*이라는 것은 $$\mathbb{L}$$의 임의의 원소가 $$p$$-radical인 것이다. 만일 $$\mathbb{L}$$의 <em-ko>모든</em-ko> 원소 $$x$$에 대하여 $$x^{p^e}\in \mathbb{K}$$가 성립하도록 하는 정수 $$e$$가 존재한다면, 이러한 성질을 만족하는 $$e$$들 중 가장 작은 것을 $$\mathbb{L}$$의 *height*라 부른다. 

</div>

즉 $$\mathbb{L}/\mathbb{K}$$의 height는 (만일 정의된다면) $$\mathbb{L}$$의 원소들의 height들의 maximum이라 생각할 수 있다. 또, [명제 2](#prop2)에 의하여 임의의 $$p$$-radical extension은 자연스럽게 algebraic extension이다. 

만일 Frobenius endomorphism $$\Frob_p:A\rightarrow A$$가 bijection이라면 우리는 $$A$$를 *perfect ring*이라 불렀다. 따라서  만일 $$\mathbb{K}$$가 perfect field였다면, $$\mathbb{K}^p=\mathbb{K}$$일 것이므로, perfect field의 임의의 $$p$$-radical extension은 자기 자신이어야 한다. 뿐만 아니라, 정의로부터 $$p$$-radical extension들의 합성이 $$p$$-radical임이 자명하다. 다음 명제는 (relative) $$p$$-radical closure의 존재성에 대한 것이다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Field extension $$\mathbb{L}/\mathbb{K}$$를 고정하고, 각각의 $$n\geq 0$$마다 

$$\mathbb{L}_n=\{x\in \mathbb{L}\mid\text{$x$ is $p$-radical of height $\leq n$}\}$$

으로 정의하자. 그럼 increasing sequence $$\mathbb{L}_n$$들의 union $$\mathbb{L}_\infty$$는 $$\mathbb{K}$$를 포함하는 $$\mathbb{L}$$의 $$p$$-radical subextension 중 가장 큰 것이다. 

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{L}_n\subseteq \mathbb{L}_{n+1}$$인 것은 정의로부터 자명하다. $$\mathbb{L}_\infty$$가 subfield인 것을 보이자. $$x,y\in \mathbb{L}_\infty$$라 하면 적당한 $$N$$에 대하여 $$x^{p^N},y^{p^N}\in \mathbb{K}$$이도록 할 수 있고, [§체, ⁋정리 10](/ko/math/field_theory/fields#thm10)의 Frobenius endomorphism으로부터

$$(x\pm y)^{p^N}=x^{p^N}\pm y^{p^N}\in \mathbb{K},\qquad (xy)^{p^N}=x^{p^N}y^{p^N}\in\mathbb{K}$$

이며, $$x\neq 0$$이라면 $$(x^{-1})^{p^N}=(x^{p^N})^{-1}\in \mathbb{K}$$이다. 즉 $$\mathbb{L}_\infty$$는 $$\mathbb{K}=\mathbb{L}_0$$를 포함하는 $$\mathbb{L}$$의 subfield이고, 그 임의의 원소가 $$p$$-radical이므로 $$\mathbb{L}_\infty/\mathbb{K}$$는 $$p$$-radical extension이다. 마지막으로 $$\mathbb{M}/\mathbb{K}$$이 $$\mathbb{L}$$의 임의의 $$p$$-radical subextension이라면, $$\mathbb{M}$$의 임의의 원소 $$x$$는 유한한 height $$n$$을 가지므로 $$x\in \mathbb{L}_n\subseteq\mathbb{L}_\infty$$이다. 즉 $$\mathbb{L}_\infty$$가 가장 크다.

</details>

앞선 글에서 우리는 임의의 field $$\mathbb{K}$$는 algebraic closure $$\overline{\mathbb{K}}$$를 갖는다는 것을 보았다. 따라서 [명제 5](#prop5)에서 $$\mathbb{L}=\overline{\mathbb{K}}$$로 둘 수 있다. 그럼 $$\overline{\mathbb{K}}$$는 perfect field이며, 뿐만 아니라 각각의 $$n$$에 대하여 $$\overline{\mathbb{K}}_n$$은 정확히 $$\mathbb{K}^{p^{-n}}$$과 같음을 안다. 이 상황에서의 (relative) $$p$$-radical closure를 $$\mathbb{K}^{p^{-\infty}}$$라 적자. 이는 정확히 [§체, ⁋정리 15](/ko/math/field_theory/fields#thm15)와 같은 것이다. 만일 $$\mathbb{K}$$가 imperfect라면, 즉 $$\mathbb{K}\neq \mathbb{K}^p$$라면 위의 ascending sequence는 strictly increasing이며, 따라서 $$\mathbb{K}^{p^{-\infty}}/\mathbb{K}$$는 infinite degree의 extension이 된다. 

한편 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Field extension $$\mathbb{L}/\mathbb{K}$$이 $$p$$-radical extension이라 하고, $$\mathbb{K}$$에서 어떠한 perfect field $$\mathbb{F}$$로의 homomorphism $$u$$가 주어졌다 하자. 그럼 $$u$$를 확장하는 유일한 homomorphism $$v:\mathbb{L} \rightarrow \mathbb{F}$$이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathbb{F}$$가 perfect이므로 Frobenius endomorphism $$\Frob_p:\mathbb{F} \rightarrow \mathbb{F}$$는 bijective이고, 따라서 임의의 $$b\in \mathbb{F}$$와 $$m\geq 0$$에 대하여 $$\xi^{p^m}=b$$를 만족하는 $$\xi\in \mathbb{F}$$가 유일하게 존재한다.

이제 $$x\in \mathbb{L}$$가 height $$m$$의 $$p$$-radical element라 하면 $$x^{p^m}\in \mathbb{K}$$이고, $$v(x)$$를 $$\xi^{p^m}=u(x^{p^m})$$을 만족하는 유일한 $$\xi\in\mathbb{F}$$로 정의하자. 이 정의는 $$m$$의 선택에 의존하지 않는다. 실제로 $$n\geq m$$에 대하여 $$x^{p^n}\in \mathbb{K}$$이기도 한데, 위에서 정의한 $$\xi$$는

$$\xi^{p^n}=(\xi^{p^m})^{p^{n-m}}=u(x^{p^m})^{p^{n-m}}=u\bigl((x^{p^m})^{p^{n-m}}\bigr)=u(x^{p^n})$$

을 만족하므로 $$n$$을 사용해 정의한 원소와 일치하기 때문이다.

$$v$$가 homomorphism인 것을 보이자. $$x,y\in \mathbb{L}$$의 height가 모두 $$N$$ 이하라 하면

$$\bigl(v(x)+v(y)\bigr)^{p^N}=v(x)^{p^N}+v(y)^{p^N}=u(x^{p^N})+u(y^{p^N})=u\bigl((x+y)^{p^N}\bigr)=v(x+y)^{p^N}$$

이고, $$\mathbb{F}$$에서 Frobenius가 injective이므로 $$v(x+y)=v(x)+v(y)$$이다. 곱셈에 대해서도 같은 논증이 성립하며, $$v(1)=1$$도 자명하다. 또 height $$0$$인 원소들, 즉 $$\mathbb{K}$$의 원소들에 대해서는 $$v=u$$이므로 $$v$$는 $$u$$를 확장한다.

마지막으로 유일성을 보이자. $$w:\mathbb{L} \rightarrow \mathbb{F}$$가 $$u$$를 확장하는 homomorphism이라면, height $$m$$의 임의의 $$x\in \mathbb{L}$$에 대하여

$$w(x)^{p^m}=w(x^{p^m})=u(x^{p^m})$$

이므로 $$\mathbb{F}$$에서 $$p^m$$제곱근의 유일성에 의하여 $$w(x)=v(x)$$이다.

</details>

따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> Field extension $$\mathbb{L}/\mathbb{K}$$가 $$\mathbb{K}$$의 perfect closure일 필요충분조건은 $$\mathbb{L}$$이 $$\mathbb{K}$$의 $$p$$-radical extension이고 $$\mathbb{L}$$이 perfect field인 것이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

여기서 perfect closure는 위에서 살펴본 $$\mathbb{K}^{p^{-\infty}}$$를 의미한다.

우선 $$\mathbb{K}^{p^{-\infty}}$$가 두 조건을 만족함을 보이자. 구성에 의하여 $$\mathbb{K}^{p^{-\infty}}$$의 임의의 원소는 유한한 height를 가지므로 $$\mathbb{K}^{p^{-\infty}}/\mathbb{K}$$는 $$p$$-radical extension이다. 또 $$x\in \mathbb{K}^{p^{-\infty}}$$라 하면 $$\overline{\mathbb{K}}$$가 algebraically closed이므로 $$y^p=x$$이도록 하는 $$y\in \overline{\mathbb{K}}$$가 존재하는데, $$x^{p^n}\in \mathbb{K}$$라 하면 $$y^{p^{n+1}}=x^{p^n}\in \mathbb{K}$$이므로 $$y\in \mathbb{K}^{p^{-\infty}}$$이다. 즉 $$\mathbb{K}^{p^{-\infty}}$$에서 Frobenius는 surjective이고, field에서 Frobenius는 항상 injective이므로 $$\mathbb{K}^{p^{-\infty}}$$는 perfect이다.

거꾸로 $$\mathbb{L}/\mathbb{K}$$가 $$p$$-radical이고 $$\mathbb{L}$$이 perfect라 하자. Inclusion $$u:\mathbb{K}\hookrightarrow \mathbb{K}^{p^{-\infty}}$$에 [명제 6](#prop6)을 적용하면 $$\mathbb{K}$$-homomorphism $$v:\mathbb{L} \rightarrow \mathbb{K}^{p^{-\infty}}$$를 얻는다. 우선 $$v(\mathbb{L})$$은 perfect field인데, $$v(x)\in v(\mathbb{L})$$가 주어질 때마다 $$\mathbb{L}$$이 perfect라는 것으로부터 $$x=z^p$$이도록 하는 $$z\in \mathbb{L}$$가 존재하고 $$v(x)=v(z)^p$$이기 때문이다. 한편 $$\mathbb{K}^{p^{-\infty}}$$의 임의의 원소 $$t$$는 적당한 $$n$$에 대하여 $$t^{p^n}\in \mathbb{K}\subseteq v(\mathbb{L})$$를 만족하고, $$v(\mathbb{L})$$이 perfect이므로 $$\xi^{p^n}=t^{p^n}$$이도록 하는 $$\xi\in v(\mathbb{L})$$가 존재한다. 그런데 field에서 Frobenius가 injective이므로 $$t=\xi\in v(\mathbb{L})$$이다. 즉 $$v$$는 surjective이고, field들 사이의 nonzero homomorphism은 injective이므로 ([§체, ⁋명제 2](/ko/math/field_theory/fields#prop2)) $$v$$는 $$\mathbb{K}$$-isomorphism이다. 따라서 $$\mathbb{L}$$은 $$\mathbb{K}$$의 perfect closure이다.

</details>

이로부터 perfect closure의 유일성도 얻어진다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> Field $$\mathbb{K}$$의 두 perfect closure $$\mathbb{L}_1$$, $$\mathbb{L}_2$$, 즉 perfect field이면서 $$\mathbb{K}$$의 $$p$$-radical extension인 두 field가 주어졌다 하자. 그럼 유일한 $$\mathbb{K}$$-isomorphism $$\mathbb{L}_1 \rightarrow \mathbb{L}_2$$가 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Inclusion $$\mathbb{K}\hookrightarrow \mathbb{L}_2$$에 [명제 6](#prop6)을 적용하면 $$\mathbb{K}$$-homomorphism $$v:\mathbb{L}_1 \rightarrow \mathbb{L}_2$$가 유일하게 존재하고, 대칭적으로 $$\mathbb{K}$$-homomorphism $$w:\mathbb{L}_2 \rightarrow \mathbb{L}_1$$도 유일하게 존재한다. 그럼 합성 $$w\circ v:\mathbb{L}_1 \rightarrow \mathbb{L}_1$$은 inclusion $$\mathbb{K}\hookrightarrow\mathbb{L}_1$$을 확장하는 homomorphism인데, $$\id_{\mathbb{L}_1}$$ 또한 그러하므로 다시 [명제 6](#prop6)의 유일성에 의하여 $$w\circ v=\id_{\mathbb{L}_1}$$이다. 같은 이유로 $$v\circ w=\id_{\mathbb{L}_2}$$이므로 $$v$$는 isomorphism이고, 그 유일성은 이미 살펴보았다.

</details>

이 글을 서두에서 언급한 반례를 소개하며 마치기로 한다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Field $$\mathbb{K}=\mathbb{F}_p(t)$$를 생각하자. 그럼 다항식 $$u(\x)=\x^p-t\in \mathbb{K}[\x]$$을 생각하고, 이를 통해 $$p$$-radical extension $$\mathbb{L}=\mathbb{K}[\x]/(\x^p-t)$$을 생각할 수 있다. 그럼 $$\mathbb{L}$$에서의 $$u(\x)=0$$의 근 $$\alpha$$에 대한 minimal polynomial이 $$u(\x)$$여야 하고 ([명제 2](#prop2)), 이를 미분하면 $$Du=p\x^{p-1}=0$$이므로 [\[환론\] §다항식환, ⁋명제 11](/ko/math/ring_theory/polynomial_rings#prop11)에 의하여 $$\alpha$$는 $$u$$의 중근임을 안다. 실은 [§체, ⁋정리 10](/ko/math/field_theory/fields#thm10)에 의해 $$(\x-\alpha)^p=\x^p-\alpha^p=\x^p-t$$이므로  $$\alpha$$는 multiplicity $$p$$를 갖는다. 

</div>

이제 다음 글과 그 다음 글에서는 이러한 경우를 어떻게 논의의 대상에서 제외시키는지 살펴본다. 

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.

---