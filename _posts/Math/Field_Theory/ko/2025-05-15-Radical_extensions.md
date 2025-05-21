---

title: "제곱근확대체"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/radical_extensions
header:
    overlay_image: /assets/images/Math/Field_Theory/Radical_extensions.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-15
last_modified_at: 2025-05-15
weight: 4

---

우리가 살펴볼 갈루아 이론의 큰 테마를 아주 간단한 예시에서 살펴보자. 가령 $\mathbb{Q}$의 degree $4$ extension $\mathbb{Q}(\sqrt{2}, \sqrt{3})$을 생각하면, $\mathbb{Q}$로부터 새로 추가되는 원소들인 $\sqrt{2}$와 $\sqrt{3}$은 각각 유리수계수의 minimal polynomial들

$$\x^2-2,\qquad \x^2-3$$

으로부터 나오는 것이다. 그런데 이 두 다항식을 각각 살펴보면, 이들은 각각 두 개의 근 $\pm \sqrt{2}$, $\pm\sqrt{3}$을 가지는 다항식이며 이를 $\mathbb{Q}$에서는 대수적인 방식으로 구별할 방법이 없다. 따라서 이들 근을 서로 바꾸는 action (혹은 $\mathbb{Q}(\sqrt{2},\sqrt{3})$의 $\mathbb{Q}$-automorphism)을 생각하면, 즉 permutation group $S_2\times S_2$를 생각하면 이것은 $S_4$의 subgroup이다. 

이와 같은 방식으로 우리는 다항식이 주어질 때마다 적절한 Galois group을 정의해줄 수 있고, 이들을 보는 것이 $\mathbb{Q}$의 extension들을 분류해줄 수 있다는 것이 갈루아 이론의 철학이다. 

그러나 이러한 철학을 바탕으로 생각했을 때, 가령 minimal polynomial이 중근을 갖는다면 permutation action을 정의하기가 상당히 껄끄러워질 것이다. 이는 $\mathbb{Q}$에서는 기우이지만, 어떠한 경우에는 이러한 일이 실제로 일어날 수도 있다. 

<div class="remark" markdown="1">

<ins id="rmk1">**참고**</ins> 이번 글에서 등장하는 모든 field는 characteristic exponent $p$를 갖는다.

</div>

## $p$-제곱근확대체

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Field extension $\mathbb{L}/\mathbb{K}$에 대하여, $x\in \mathbb{L}$이 *$p$-radical*이라는 것은 어떠한 $m\geq 0$이 존재하여 $x^{p^m}\in \mathbb{K}$이도록 할 수 있는 것이다. 이러한 $m$들 중 가장 작은 것을 $x$의 *height*라 부른다. 

</div>

만일 $p=1$이라면 위의 정의는 별 의미가 없으며, 이번 글에서 나올 나머지 내용들 또한 마찬가지이다. 즉, 본질적으로 이번 글의 내용은 모두 characteristic $p$의 field에 대한 것이라 보아도 된다. 

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Field extension $\mathbb{L}/\mathbb{K}$와 $p$-radical element $x\in \mathbb{K}$ of height $e$를 고정하자. 그럼 $a=x^{p^e}\in \mathbb{K}$에 대하여, $x$의 minimal polynomial은

$$\x^{p^e}-a\in \mathbb{K}[\x]$$

으로 주어진다. 따라서 $[\mathbb{K}(x):\mathbb{K}]=p^e$이다. 

</div>

Frobenius endomorphism $\Frob_p:\mathbb{K}\rightarrow \mathbb{K}$의 image를 우리는 $\mathbb{K}^p$라 적기로 하였다. $e$의 최소성에 의하여 $a\not\in \mathbb{K}^p$이므로, 주장은 다음 보조정리의 결과이다. 

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> Field $\mathbb{K}$의 원소 $a$가 $a\not\in \mathbb{K}^p$를 만족한다 가정하자. 그럼 임의의 $e\geq 0$에 대하여, $f(\x)=\x^{p^e}-a$는 $\mathbb{K}[\x]$의 irreducible polynomial이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>



</details>

다음 정의는 [정의 1](#def1) 직후에 왔어도 자연스러웠을 것이다. 

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Field extension $\mathbb{L}/\mathbb{K}$가 *$p$-radical*이라는 것은 $\mathbb{L}$의 임의의 원소가 $p$-radical인 것이다. 만일 $\mathbb{L}$의 <em_ko>모든</em_ko> 원소 $x$에 대하여 $x^{p^e}\in \mathbb{K}$가 성립하도록 하는 정수 $e$가 존재한다면, 이러한 성질을 만족하는 $e$들 중 가장 작은 것을 $\mathbb{L}$의 *height*라 부른다. 

</div>

즉 $\mathbb{L}/\mathbb{K}$의 height는 (만일 정의된다면) $\mathbb{L}$의 원소들의 height들의 maximum이라 생각할 수 있다. 또, [명제 2](#prop2)에 의하여 임의의 $p$-radical extension은 자연스럽게 algebraic extension이다. 

만일 Frobenius endomorphism $\Frob_p:A\rightarrow A$가 bijection이라면 우리는 $A$를 *perfect ring*이라 불렀다. 따라서  만일 $\mathbb{K}$가 perfect field였다면, $\mathbb{K}^p=\mathbb{K}$일 것이므로, perfect field의 임의의 $p$-radical extension은 자기 자신이어야 한다. 뿐만 아니라, 정의로부터 $p$-radical extension들의 합성이 $p$-radical임이 자명하다. 다음 명제는 (relative) $p$-radical closure의 존재성에 대한 것이다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Field extension $\mathbb{L}/\mathbb{K}$를 고정하고, 각각의 $n\geq 0$마다 

$$\mathbb{L}_n=\{x\in \mathbb{L}\mid\text{$x$ is $p$-radical of height $\leq n$}\}$$

으로 정의하자. 그럼 increasing sequence $\mathbb{L}\_n$들의 union $\mathbb{L}\_\infty$는 $\mathbb{K}$를 포함하는 $\mathbb{L}$의 $p$-radical subextension 중 가장 큰 것이다. 

</div>

이에 대한 증명은 본질적으로 자명하다.

앞선 글에서 우리는 임의의 field $\mathbb{K}$는 (유일한) algebraic closure $\overline{\mathbb{K}}$를 갖는다는 것을 보았다. 따라서 [명제 5](#prop5)에서 $\mathbb{L}=\overline{\mathbb{K}}$로 둘 수 있다. 그럼 $\overline{\mathbb{K}}$는 perfect field이며, 뿐만 아니라 각각의 $n$에 대하여 $\overline{\mathbb{K}}_n$은 정확히 $\mathbb{K}^{p^{-n}}$과 같음을 안다. 이 상황에서의 (relative) $p$-radical closure를 $\mathbb{K}^{p^{-\infty}}$라 적자. 이는 정확히 [§체, ⁋정리 15](/ko/math/field_theory/fields#prop15)와 같은 것이다. 만일 $\mathbb{K}$가 imperfect라면, 즉 $\mathbb{K}\neq \mathbb{K}^p$라면 위의 ascending sequence는 strictly increasing이며, 따라서 $\mathbb{K}^{p^{-\infty}}/\mathbb{K}$는 infinite degree의 extension이 된다. 

한편 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> Field extension $\mathbb{L}/\mathbb{K}$이 $p$-radical extension이라 하고, $\mathbb{K}$에서 어떠한 perfect field $\mathbb{F}$로의 homomorphism $u$가 주어졌다 하자. 그럼 $u$를 확장하는 유일한 homomorphism $v:\mathbb{L} \rightarrow \mathbb{F}$이 존재한다. 

</div>

따라서 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor7">**따름정리 7**</ins> Field extension $\mathbb{L}/\mathbb{K}$가 $\mathbb{K}$의 perfect closure일 필요충분조건은 $\mathbb{L}$이 $\mathbb{K}$의 $p$-radical extension이고 $\mathbb{L}$이 perfect field인 것이다. 

</div>

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8**</ins> 

</div>

이 글을 서두에서 언급한 반례를 소개하며 마치기로 한다. 

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Field $\mathbb{K}=\mathbb{F}_p(t)$를 생각하자. 그럼 다항식 $u(\x)=\x^p-t\in \mathbb{K}[\x]$을 생각하고, 이를 통해 $p$-radical extension $\mathbb{L}=\mathbb{K}[\x]/(\x^p-t)$을 생각할 수 있다. 그럼 $\mathbb{L}$에서의 $u(\x)=0$의 근 $\alpha$에 대한 minimal polynomial이 $u(\x)$여야 하고 ([명제 2](#prop2)), 이를 미분하면 $Du=p\x^{p-1}=0$이므로 [\[환론\] §다항식환, ⁋명제 11](/ko/math/ring_theory/polynomial_rings#prop11)에 의하여 $\alpha$는 $u$의 중근임을 안다. 실은 [§체, ⁋정리 10](/ko/math/field_theory/fields#thm10)에 의해 $(\x-\alpha)^p=\x^p-\alpha^p=\x^p-t$이므로  $\alpha$는 multiplicity $p$를 갖는다. 

</div>

이제 다음 글과 그 다음 글에서는 이러한 경우를 어떻게 논의의 대상에서 제외시키는지 살펴본다. 