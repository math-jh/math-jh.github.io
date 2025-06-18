---

title: "갈루아 확장"
excerpt: ""

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/galois_extension
header:
    overlay_image: /assets/images/Math/Field_Theory/Galois_extension.png
    overlay_filter: 0.5
sidebar: 
    nav: "field_theory-ko"

date: 2025-05-29
last_modified_at: 2025-05-29
weight: 8

---

이제 우리는 갈루아 확장이 무엇인지 정의할 준비가 되었지만, 그 전에 우선 다음의 명제를 살펴본다. 

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Algebraic extension $\mathbb{L}$과 inclusion $u:\mathbb{L}\rightarrow \overline{\mathbb{K}}$를 생각하자. 

1. 만일 $u(\mathbb{L})\subseteq \mathbb{L}$이라면 $u$는 $\mathbb{L}$에서 $\mathbb{L}$로의 $\mathbb{K}$-automorphism이다. 
2. $u$를 확장하는 $\overline{\mathbb{K}}$의 $\mathbb{K}$-automorphism이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 임의의 $x\in E$에 대하여, $x$의 minimal polynomial $f$가 주어졌다 하자. 집합 $\Phi$를 $\mathbb{L}$ 인에서의 $f$의 근들의 모임이라 하면 $\Phi$는 유한집합이다. 뿐민 아니라, 만일 $\alpha\in\Phi$라 하면 

    $$0=u(0)=u(f(\alpha))=f(u(\alpha))$$
    
    이므로 $u(\Phi)\subseteq\Phi$가 성립한다. 그런데 $u$는 zero map이 아니므로 injective이고 ([§체, ⁋명제 2](/ko/math/field_theory/fields#prop2)), 따라서 $u$는 $\Phi$에서 $\Phi$로의 bijection이다. 따라서 $x\in\Phi=u(\Phi)\subseteq u(E)$이고 이로부터 $u(E)=E$이다.

2. $\overline{\mathbb{K}}$는 $u(\mathbb{L})$과 $\mathbb{L}$의 algebraic closure이므로 [§대수적 폐포, ⁋정리 5](/ko/math/field_theory/algebraically_closed_extensions#thm5)의 universal property로부터 원하는 결과를 얻는다. 

</details>

우리의 목적은 고정된 field $\mathbb{K}$의 algebraic extension들을 모두 살펴보는 것이며, 더 정확히는 algebraic extension들의 equivalence class들을 보는 것이다.  

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Field $\mathbb{K}$의 두 algebraic extension $\mathbb{L}$, $\mathbb{M}$에 대하여, $u(\mathbb{L})=\mathbb{M}$이도록 하는 $\mathbb{K}$-automorphism $u:\overline{\mathbb{K}}\rightarrow \overline{\mathbb{K}}$이 존재한다면 이들이 *conjugate*한다고 말한다. 특히 두 원소 $x,y\in\overline{\mathbb{K}}$이 *conjugate*이라는 것은 적당한 $\mathbb{K}$-automorphism $u: \overline{\mathbb{K}}\rightarrow \overline{\mathbb{K}}$이 존재하여 $u(x)=y$인 것이다. 

</div>

[명제 1](#prop1)에 의하여, 만일 $\mathbb{M}$과 $\mathbb{L}$이 isomorphic한 $\mathbb{K}$의 extension이라면 이들은 conjugate extension들이며, 정의에 의해 conjugate extension들은 isomorphic하다. 뿐만 아니라 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $\overline{\mathbb{K}}$의 두 원소 $x,y$들 고정하자. 다음이 성립한다. 

1. $x,y$는 conjugate element들이다. 
2. $v(x)=y$를 만족하는 적당한 $\mathbb{K}$-isomorphism $v: \mathbb{K}(x) \rightarrow \mathbb{K}(y)$이 존재한다. 
3. $x$와 $y$는 동일한 minimal polynomial을 갖는다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 첫번째 조건을 가정하자. $x$의 minimal polynomial을 $f$라 하면, 

$$f(y)=f(u(x))=u(f(x))=u(0)=0$$

이므로 $y$의 minimal polynomial은 $f$를 나눈다. 같은 논리로 $x$의 minimal polynomial은 $y$의 minimal polynomial을 나누고 따라서 이들은 서로 겉다. 

한편 $x,y$가 같은 minimal polynomial $f$를 갖는다 하면 first isomorphism theorem으로부터 

$$\mathbb{K}(x)\cong \mathbb{K}[\x]/(f)\cong \mathbb{K}(y)$$

이므로 셋째 조건이 둘째 조건을 함의하는 것은 자명하다. 마지막으로 둘째 조건을 가정하면 [명제 1](#prop1)로부터 $v$를 확장하는 $\mathbb{K}$-isomorphism $u:\overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$이 존재하고 따라서 $x$, $y$가 conjugate이다. 

</details>

이로부터 만일 degree $n$의 algebraic element $x\in \overline{\mathbb{K}}$가 주어졌다면, $x$와 conjugate인 원소들은 반드시 $x$의 minimal polynomial의 근이고 따라서 이러한 원소는 많아야 $n$개 뿐임을 안다. 뿐만 아니라, 여기에서 $x$와 conjugate한 원소가 $n$개 *미만*인 것은 정확하게 $x$의 minimal polynomial이 separable하지 않은 것과 동치이다. 즉, $\overline{\mathbb{K}}$의 $\mathbb{K}$-automorphism들의 group을 $\Aut_\mathbb{K}(\overline{\mathbb{K}})$라 하고 $\Aut_\mathbb{K}\overline{\mathbb{K}}$가 $\overline{\mathbb{K}}$에 자명한 방식으로 act할 때, 이 action에 의해 fix되는 원소들의 모임 $\overline{\mathbb{K}}^{\Aut_{\mathbb{K}}(\overline{\mathbb{K}})}$은 정확히 $\mathbb{K}^{p^{-\infty}}$와 같다. 

## 갈루아 확장

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Field extension $\mathbb{L}/\mathbb{K}$이 *quasi-Galois extension<sub>준갈루아확대</sub>* 혹은 *normal extension<sub>정규확대</sub>*이라는 것은 $\mathbb{L}/\mathbb{K}$가 algebraic이며, $\mathbb{L}$에서 근을 갖는 임의의 irreducible polynomial $f\in \mathbb{K}[\x]$가 $\mathbb{L}[\x]$안에서 일차식들의 곱으로 쪼개지는 것이다. 

</div>

그럼 본질적으로 quasi-Galois extension은 splitting field의 다른 이름에 불과하다. 

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> Algebraic extension $\mathbb{L}/\mathbb{K}$에 대하여, 다음이 모두 동치이다. 

1. $\mathbb{L}/\mathbb{K}$가 quasi-Galois이다. 
2. 암의의 $x\in \mathbb{L}$에 대하여, $x$의 ($\overline{\mathbb{K}}$에서의) conjugate들은 모두 $\mathbb{L}$에 속한다. 
3. $\overline{\mathbb{K}}$의 임의의 $\mathbb{K}$-automorphism은 $\mathbb{L}$을 $\mathbb{L}$로 보낸다, 
4. $\mathbb{L}$에서 $\overline{\mathbb{K}}$로의 임의의 $\mathbb{K}$-homomorphism은 $\mathbb{L}$로 들어간다. 
5. $\mathbb{L}$은 어떠한 non-constant polynomial들의 family $(f_i\in \mathbb{K}[\x])$의 splitting field이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

우선 셋째 조건과 넷째 조건의 동치는 [명제 1](#prop1)로부터 나온다. 한편 quasi-Galois extension은 그 원소들의 minimal polynomial들의 splitting field로 볼 수 있으므로 마지막 조건은 첫째 조건에 의해 유도된다. 한편 마지막 조건이 성립한다면 [명제 1](#prop1)과 같은 논리로 $\overline{\mathbb{K}}$의 임의의 $\mathbb{K}$-automorphism은 $f\_i$의 근을 $f\_i$로 보내므로 $\mathbb{L}$을 $\mathbb{L}$로 보낸다. 따라서 셋째 조건이 성립한다. 또 셋째 조건은 정의에 의해 둘째 조건을 함의하는 것이 자명하다. 따라서 

$$(1)\implies (5)\implies (3)\iff (4)\implies (2)$$

이므로 $(2)\implies (1)$만 보이면 충분하다. 이를 위해 $\mathbb{L}$에서 근을 갖는 (monic) irreducible polynomial $f\in \mathbb{K}[\x]$가 주어졌다 하자. 그럼 우선 $\overline{\mathbb{K}}$가 algebraically closed이므로 $f$는 $\overline{\mathbb{K}}$에서 다음의 식 

$$f(\x)=\prod_{i=1}^d (\x- a_i), \qquad a_i\in \overline{\mathbb{K}}$$

으로 표현된다. 이제 각각의 $a_i$들은 conjugate이고 따라서 가정에 의해 이들이 모두 $\mathbb{L}$에 속해야한다. 
pf
</details>

이로부터 다음이 성립한다. 

<div class="proposition" markdown="1">

<ins id="cor6">**따름정리 6**</ins> 다음이 성립한다. 

1. Algebraic extension $\mathbb{L}/\mathbb{K}$가 quasi-Galois인 것과, $\mathbb{L}$의 임의의 conjugate이 자기 자신 뿐인 것이 동치이다. 
2. Algebraic extension $\mathbb{K}\subseteq \mathbb{L}\subseteq \mathbb{M}$에 대하여, 만일 $\mathbb{M}/\mathbb{K}$가 quasi-Galois라면 $\mathbb{L}/\mathbb{K}$ 또한 그러하다. 
3. Quasi-Galois extension $\mathbb{M}/\mathbb{K}$와 그 subextension $\mathbb{L}/\mathbb{K}$가 주어졌다 하자. 그럼 임의의 $\mathbb{K}$-homomorphism $u: \mathbb{L}\rightarrow \overline{\mathbb{K}}$에 대해 $u(\mathbb{L})\subseteq \mathbb{M}$이 성립하며, 이를 확장하는 $\mathbb{M}$의 $\mathbb{K}$-automorphism $v$가 존재한다. 
4. 임의의 field extension $\mathbb{K}'/\mathbb{K}$와 quasi-Galois extension $\mathbb{L}/\mathbb{K}$에 대해 $\mathbb{K}'(\mathbb{L})$은 $\mathbb{K}'$에 대해 quasi-Galois이다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. [명제 5](#prop5)에 의해 $\mathbb{L}/\mathbb{K}$가 quasi-Galois인 것과 $\overline{\mathbb{K}}$의 임의의 $\mathbb{K}$-automorphism이 $\mathbb{L}$을 $\mathbb{L}$로 보내는 것이 동치이다. 
2. $\mathbb{M}/\mathbb{K}$가 quasi-Galois라 하자. 그럼 우선 $\overline{\mathbb{K}}$는 $\mathbb{L}$의 algebraic closure이기도 하므로, [명제 5](#prop5)에 의해 임의의 $\mathbb{L}$-automorphism $u: \overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$에 대해 $u(\mathbb{M})=\mathbb{M}$임을 보이면 충분하다. 그런데 $\mathbb{M}$은 $\mathbb{K}$의 quasi-Galois extension이고, $u$는 $\mathbb{L}$-automorphism이므로 자동적으로 $\mathbb{K}$-automorphism이기도 하다. 이로부터 $u$가 원하는 조건을 만족해야 함을 안다. 
3. [명제 1](#prop1)로부터 $u$를 확장하는 $\mathbb{K}$-automorphism $v:\overline{\mathbb{K}}\rightarrow\overline{\mathbb{K}}$이 존재함을 안다. 이 때, 이를 $\mathbb{M}$으로 제한한 것은 $\mathbb{M}$이 quasi-Galois라는 가정으로부터 $v(\mathbb{M})=\mathbb{M}$을 만족해야 하고, 따라서 원하는 주장이 성립한다. 
4. $\mathbb{L}$이 $f_i\in \mathbb{K}[\x]$들의 splitting field라면, $\mathbb{L}'$이 $f_i\in \mathbb{K}'[\x]$들의 splitting field이다. 

</details>

위의 따름정리의 증명에서 볼 수 있듯 quasi-Galois extension $\mathbb{L}/\mathbb{K}$를 특징짓는 가장 중요한 성질은 임의의 $\mathbb{K}$-automorphism이 $\mathbb{L}$을 $\mathbb{L}$로 보년다는 것이다. 다음 명제도 이 사실로부터 자명하다. 

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $\mathbb{K}$의 algebraic closure $\overline{\mathbb{K}}$ 안에서의 quasi-Galois extension들 $\mathbb{L}\_i$이 주어졌다 하자. 그럼 $\bigcap \mathbb{L}\_i$와 $\mathbb{K}(\bigcup \mathbb{L}\_i)$도 모두 quasi-Galois이다. 

</div>

특히 $\overline{\mathbb{K}}$의 임의의 원소들의 집합 $S$에 대하여, 이를 포함하는 quasi-Galois extenson 중 가장 작은 것을 생각할 수 있다. 이는 정의에 의해, $S$의 각 원소들의 conjugate들을 모두 모은 후, 이들로 생성되는 $\mathbb{K}$의 extension이다. 이를 $S$에 의해 생성되는 quasi-Galois extension이라 부른다. 

[정의 4](#dzef3)에서 우리는 quasi-Galois extension을 정의할 때, irreducible polynomial $f$가 일차식들의 곱으로 쪼개질 것을 요구했지만 이들이 서로 다를 필요는 없었다. Galois extension은 여기에 separable 조건을 추가하여 얻어진다. 

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8**</ins> Algebraic extension $\mathbb{L}/\mathbb{K}$와, $\mathbb{L}$의 $\mathbb{K}$-automorphism들의 group $\Gamma$가 주어졌다 하자. 다음이 모두 동치이다. 

1. $\mathbb{L}$의 $\Gamma$-invariant element들은 모두 $\mathbb{K}$의 원소이다. 
2. $\mathbb{L}$은 $\mathbb{K}$의 separable quasi-Galois extension이다. 
3. 임의의 $x\in \mathbb{L}$에 대하여, $x$의 minimal polynomial $f\in \mathbb{K}[\x]$는 $\mathbb{L}[\x]$에서 서로 다른 일차식들의 곱으로 쪼개진다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

둘째 조건과 셋째 조건이 동치임은 자명하므로, 이들과 첫째 조건이 동치임만 보이면 충분하다. 

우선 첫째 조건을 가정하자. 임의의 $x\in \mathbb{L}$와 그 minimal polynomial $f\in \mathbb{K}[\x]$에 대하여 $f$가 $\mathbb{L}[\x]$에서 서로 다른 일차식들의 곱으로 쪼개진다는 것을 보여야 한다. 이를 위해 $f$의 $\mathbb{L}$에서의 모든 근들의 모임을 $S$라 하고, 새로운 다항식 

$$g(\x)=\prod_{a\in S}(\x-a)$$

이라 정의하면 $g$는 $\mathbb{L}[\x]$의 원소이며 임의의 $\sigma\in\Gamma$에 대해 

$$(\sigma\cdot g)(\x)=\prod_{a\in S}(\x-\sigma(a))=\prod_{a\in S}(\x-a)$$

이므로 $g$의 계수들은 $\sigma$에 의해 변하지 않고 따라서 첫째 조건의 가정으로부터 $g\in\mathbb{K}
[\x]$이다. 이제 $g(x)=0$이므로 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)에 의하여 $g$는 $f$를 나누며, 이들의 차수를 고려하면 $g=f$여야 함을 안다. 즉 셋째 조건이 성립한다. 

거꾸로 셋째 조건을 가정하고 첫째 조건을 보이자. $x\in\mathbb{L}$이 $\mathbb{K}$에 속하지 않는다면 $x$를 다른 원소로 보내는 $\sigma\in\Gamma$가 존재함을 보여야 한다. $x$의 minimal polynomial을 $f$라 하면, $x\not\in\mathbb{K}$인 것으로부터 $f$는 2차 이상이고, 가정에 의해 

$$f(\x)=\prod_{a\in S}(\x-a), \qquad \text{$S$ the set of comjugates of $x$ in $\overline{\mathbb{K}}$}$$

로 쪼갤 수 있으며 한편 $\mathbb{L}/\mathbb{K}$는 quasi-Galois이므로 $x$를 자신과 다른 $a\in S$로 보내는 $\overline{\mathbb{K}}$의 $\mathbb{K}$-automorphism $u$가 존재하며 이는 [명제 5](#prop5)에 의해 $\mathbb{L}$의 $\mathbb{K}$-automorphism이다. 이로부터 원하는 결과를 얻는다.

</details>

이제 다음을 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> Algebraic extension $\mathbb{L}/\mathbb{K}$이 *Galois<sub>갈루아</sub>*라는 것은 $\mathbb{L}/\mathbb{K}$이 [명제 8](#prop8)의 조건을 만족하는 것이다. 

</div>

그럼 [명제 7](#prop7)의 결과와 separable extension에 대한 결과로부터 다음의 두 명제를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> $\mathbb{K}$의 algebraic closure $\overline{\mathbb{K}}$ 안에서의 Galois extension들 $\mathbb{L}\_i$이 주어졌다 하자. 그럼 $\bigcap \mathbb{L}\_i$와 $\mathbb{K}(\bigcup \mathbb{L}\_i)$도 모두 Galois이다. 
 
</div>

<div class="proposition" markdown="1">

<ins id="prop11">**명제 11**</ins> Galois extension $\mathbb{L}/\mathbb{K}$와 finite degree subextension $\mathbb{M}/\mathbb{K}$가 주어졌다 하자. 그럼 $\mathbb{M}$을 포함하고, finite degree Galois인 $\mathbb{L}/\mathbb{K}$의 적당한 subextension $\mathbb{N}/\mathbb{K}$이 존재한다.

</div>

## 갈루아 군

이미 살펴보았듯 Galois extension $\mathbb{L}/\mathbb{K}$을 다룰 때 중요하게 사용되는 것은 $\mathbb{L}$의 $\mathbb{K}$-automorphism들의 모임이다.

<div class="definition" markdown="1">
 
<ins id="def12">**정의 12**</ins> Galois extension $\mathbb{L}/\mathbb{K}$에 대하여, $\mathbb{L}$의 $\mathbb{K}$-automorphism들의 group을 *Galois group<sub>갈루아 군</sub>*이라 부르고 $\Gal(\mathbb{L}/\mathbb{K})$으로 적는다.

</div> 

특별히 field $\mathbb{K}$를 고정하고 그 algebraic closure $\overline{\mathbb{K}}$를 생각하자. $\mathbb{K}[\x]$의 separable polynomial $f$와, $f$의 근들의 집합 $A$에 대하여 $\mathbb{L}=\mathbb{K}(A)$는 $\mathbb{K}$의 Galois extension임을 이미 살펴보았다. 그런데 $\mathbb{L}$는 $S$에 의해 생성되므로 임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$는 $A$에서의 값으로 완전히 결정되며 이로부터 injective group homomorphism 

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow S_A$$

이 유도된다. 일반적으로 이 homomorphism은 surjective일 필요가 없다. 즉 임의의 separable polynomial $f$의 근들 가운데 comjugate하지 않은 것들이 있을 수 있으며 이는 [명제 3](#prop3)에 의하여 이들 두 근 $x,y$가 서로 다른 minimal polynomial을 갖는 것과 동치이다. 한편 $x,y$가 $f$의 근이라면 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)로부터 이들의 minimal polynomial들은 각각 $f$를 나누며 따라서 $x$와 $y$는 서로 다른 $f$의 irreducible factor의 근이다. 이로부터 우리는 위의 injective homomorphism의 image가 어떻게 생겼는지까지 확인해줄 수 있다.

한편 Galois extension $\mathbb{L}/\mathbb{K}$와, $\mathbb{L}$의 subextension인 또 다른 Galois extension $\mathbb{M}/\mathbb{K}$에 대하여, 우리는 [명제 1](#prop1)로부터 다음의 결과를 얻는다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> 위와 같은 상황에서 restriction homomorphism

$$\Gal(\mathbb{L}/\mathbb{K})\rightarrow\Gal(\mathbb{M}/\mathbb{K});\qquad \sigma\mapsto \sigma\vert_\mathbb{M}$$

은 surjective이다.

</div>