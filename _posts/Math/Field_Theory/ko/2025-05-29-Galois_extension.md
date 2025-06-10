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

으로 표현된다. 이제 각각의 $a_i$들은 conjugate이므로, 이로부터 

</details>