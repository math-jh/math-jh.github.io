---

title: "분해차수"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/separable_degree
header:
    overlay_image: /assets/images/Math/Field_Theory/Separable_degree.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-17
last_modified_at: 2025-05-17
weight: 7

---

## 제곱근확대체

우리가 생각할 수 있는 가장 separable하지 않은 extension은, 당연히, $p$-radical extension이다. 이러한 이유로 $p$-radical extension은 종종 *purely inseparable extension*이라 부르기도 한다. 이번 글에서는 우선, $p$-radical extension과 separable extension의 관계에 대해 살펴보고, 이를 separable degree를 사용하여 설명할 것이다. 

우선 다음의 보조정리를 보이자.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> Characteristic $p\neq 0$의 field $\mathbb{K}$에 대하여, finite degree $\mathbb{K}$-algebra $A$가 étale인 것과 $A=\mathbb{K}[A^p]$인 것이 동치이다. 뿐만 아니라, 이 경우 $(a_i)$가 $A$의 $\mathbb{K}$-basis라면 $(a_i^p)$들도 그러하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$\mathbb{K}$의 algebraic closure $\overline{\mathbb{K}}$를 생각하자. 그럼 임의의 $u,v\in \Hom_\Alg{\mathbb{K}}(A, \overline{\mathbb{K}})$에 대하여, 만일 $u,v$를 subalgebra $\mathbb{K}[A^p]$로 제한한 것이 같다면 다음의 식

$$u(x)^p=u(x^p)=v(x^p)=v(x)^p$$

가 모든 $x\in A$에 대해 성립하므로 정의에 의하여 다음의 부등식

$$[A:\mathbb{K}]_s\leq[\mathbb{K}[A^p]:\mathbb{K}]_s$$

이 성립함을 안다. 만일 $A$가 étale $\mathbb{K}$-algebra라면 [§에탈대수, ⁋명제 13](/ko/math/field_theory/etale_algebras#prop13)의 부등식과 그 등호조건에 의하여 다음의 식

$$[A:\mathbb{K}]=[A:\mathbb{K}]_s\leq[\mathbb{K}[A^p]:\mathbb{K}]_s\leq [\mathbb{K}[A^p]:\mathbb{K}]$$

이 성립하고, 자명하게 $\mathbb{K}[A^p]\subset A$는 일반적인 경우에 대해 성립하므로 $A=\mathbb{K}[A^p]$가 성립한다. 

이제 거꾸로 $A=\mathbb{K}[A^p]$임을 가정하고 $A$가 étale임을 보이자. 이를 위해서는 뒤의 조건을 보이면 충분하다. $(a_i)$가 $A$의 $\mathbb{K}$-basis라 가정하면, $(a_i^p)$들이 $\mathbb{K}[A^p]$를 $\mathbb{K}$-벡터공간으로서 생성하는 것은 [§체, ⁋명제 12](/ko/math/field_theory/fields#prop12)의 결과이고, 그럼 주어진 가정 $A=\mathbb{K}[A^p]$로부터 $(a_i^p)$들은 $A$를 생성하기도 한다. 

이제 [§분해가능확대체, ⁋정리 7](/ko/math/field_theory/separable_extensions#thm7)의 결과를 사용하기 위해, $\overline{\mathbb{K}}\otimes_\mathbb{K}A$가 reduced임을 보이자. 만일 어떤 $u\in\overline{\mathbb{K}}\otimes_\mathbb{K}A$에 대하여 $u^2=0$이라 가정하면 $u^p=0$이고, 이로부터 만일 $u=\sum \lambda_i\otimes a_i$라 쓴다면

$$0=u^p=\sum_{i\in I} (\lambda_i\otimes a_i)^p=\sum_{i\in I} \lambda_i^p\otimes a_i^p$$

이고 따라서 각각의 $\lambda_i^p$들이 $0$이어야 한다. $\overline{\mathbb{K}}$는 (당연히) reduced이므로 $\lambda_i$들은 모두 $0$이어야 하고, 따라서 $u=0$이므로 이로부터 원하는 결과를 얻는다. 

</details>

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> Characteristic exponent $p$를 갖는 field $\mathbb{K}$와, algebraic extension $\mathbb{L}/\mathbb{K}$를 생각하자. 또, $\mathbb{L}=\mathbb{K}(S)$이도록 하는 부분집합 $S$를 생각하자. 만일 $\mathbb{L}/\mathbb{K}$가 separable이라면, 임의의 $n\geq 0$에 대하여 $\mathbb{L}=\mathbb{K}(S^{p^n})$이 성립한다. 거꾸로, 만일 $\mathbb{L}/\mathbb{K}$가 finite degree extension이고 $\mathbb{L}=\mathbb{K}(S^p)$라면 $\mathbb{L}/\mathbb{K}$가 separable이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

언제나 그렇듯 $p=1$인 경우는 증명할 것이 없다. 따라서 $p\neq 1$인 경우만 보면 충분하다. 

우선 $\mathbb{L}=\mathbb{K}(S)$라 가정하면

$$\mathbb{K}(\mathbb{L}^p)=\mathbb{K}(\mathbb{K}(S)^p)=\mathbb{K}(\mathbb{K}^p(S^p))=\mathbb{K}(S^p)$$

이므로 $\mathbb{K}(S^p)=\mathbb{K}(\mathbb{L}^p)=\mathbb{K}[\mathbb{L}^p]$이 성립한다. 우선 위의 [보조정리 1](#lem1)를 $A=\mathbb{L}$에 적용하면 $\mathbb{L}/\mathbb{K}$가 finite degree extension인 경우는 이것이 $\mathbb{L}$가 étale $\mathbb{K}$-algebra인 것과 동치이므로 자명하다. 이제 $\mathbb{L}/\mathbb{K}$가 infinite degree인 경우에도,  $\mathbb{L}/\mathbb{K}$의 임의의 finite degree subextension $\mathbb{L}'/\mathbb{K}$은 separable이므로 앞선 논의에 의해 

$$\mathbb{L}'=\mathbb{K}[(\mathbb{L}')^p]=\subseteq \mathbb{K}[\mathbb{L}^p]$$

이 성립하고, $\mathbb{K}[\mathbb{L}^p]$는 $\mathbb{L}'/\mathbb{K}$들의 union으로 원하는 등식을 얻는다. 임의의 $n$에 대한 등식은 단순한 귀납법이다. 

</details>

이로부터 다음 두 따름정리를 얻는다. 

<div class="proposition" markdown="1">

<ins id="cor3">**따름정리 3**</ins> Perfect field $\mathbb{K}$의 임의의 algebraic extension은 perfect이다. 

</div>

이에 대한 증명은 [명제 2](#prop2)로부터 거의 자명하다. 

뿐만 아니라 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor4">**따름정리 4**</ins> Field $\mathbb{K}$의 algebraic closure $\overline{\mathbb{K}}$와 이 안에서의 perfect closure $\mathbb{K}^{p^{-\infty}}$에 대하여, $\overline{\mathbb{K}}/\mathbb{K}$의 subextension $\mathbb{L}/\mathbb{K}$가 separable인 것과 $\mathbb{K}^{p^{-\infty}}$가 linearly disjoint한 것이 동치이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

언제나와 마찬가지로 $\mathbb{L}/\mathbb{K}$가 finite degree인 상황을 생각하면 충분하다. $\mathbb{L}/\mathbb{K}$의 basis $(x_i)$가 주어졌다 하면, $\mathbb{L}$이 $\mathbb{K}^{p^{-\infty}}$와 linearly disjoint인 것은 $(x_i)$가 모든 $\mathbb{K}^{p^{-n}}$과 linearly disjoint인 것과 동치이므로, 이는 임의의 family $(a_i)$와 임의의 $n$에 대하여

$$\sum x_i a_i^{p^{-n}}=0\implies a_i=0$$

이 항상 성립해야 한다는 것과 같은 말이다. 이제 양 변에 $p^n$-th power를 취하면, 이로부터 $x_i^{p^n}$들이 free여야 한다는 것을 알고, 따라서 이들이 $\mathbb{L}$의 basis를 정의해야 한다는 것을 알 수 있으며 그 역 또한 성립한다. 차원을 생각하면 이는 $\mathbb{L}=\mathbb{K}(\mathbb{L}^p)$인 것과 동치이므로, [명제 2](#prop2)로부터 원하는 결과를 얻는다. 

</details>

## 분해가능폐포

한편 algebraic closure 혹은 perfect closure 등과 마찬가지로 separable closure 또한 정의할 수 있다. 그럼 [§체, ⁋정리 15](/ko/math/field_theory/fields#thm15)에서의 perfect closure가 algebraic closure에 대한 relative perfect closure와 같듯, separable closure 또한 relative separable closure를 먼저 정의한 후, algebraic closure 안에서의 relative separable closure를 (absolute) separable closure라 정의하는 것이 자연스러울 것이다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Field extension $\mathbb{L}/\mathbb{K}$에 대하여, $\mathbb{L}_s$를 $\mathbb{K}$에 대해 separable한 원소들의 모임이라 하자. 그럼 $\mathbb{L}_s$는 $\mathbb{L}/\mathbb{K}$의 subextension이며, 뿐만 아니라 $\mathbb{L}$에 속하고 separable인 algebraic extension 중 가장 큰 것이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 separable extension의 임의의 원소는 separable이므로 ([§분해가능확대체, ⁋명제 12](/ko/math/field_theory/separable_extensions#prop12)), separable인 $\mathbb{L}$의 subextension은 항상 $\mathbb{L}$에 포함된다. 한편, 역으로 separable element들로만 생성되는 algebraic extension은 마찬가지로 [§분해가능확대체, ⁋명제 12](/ko/math/field_theory/separable_extensions#prop12)에 의해 separable이므로, $\mathbb{K}(\mathbb{L}_s)$는 그 자체로 separable extension이며 다시 위의 주장에 의해 $\mathbb{K}(\mathbb{L}_s)\subseteq \mathbb{L}_s$가 성립한다. 즉, $\mathbb{K}(\mathbb{L}_s)=\mathbb{L}_s$가 성립하고 따라서 [명제 2](#prop2)로부터 원하는 결과를 얻는다. 

</details>

위에서 언급한 것과 같이, $\mathbb{L}_s$를 ($\mathbb{L}/\mathbb{K}$에서의) *relative separable closure*라 부른다. 

이 글의 gor심 결과는 임의의 algebraic extension은 항상 (relative separable closure에 해당하는) separable한 부분과, inseparable한 부분으로 완전하게 나뉜다는 것이다. 