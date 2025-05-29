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

<ins id="prop1">**명제 1**</ins> Algebraic closure $\overline{\mathbb{K}}/\mathbb{K}$의 subextension $\mathbb{L}$과 inclusion $u:\mathbb{L}\rightarrow \overline{\mathbb{K}}$를 생각하자. 

1. 만일 $u(\mathbb{L})\subseteq \mathbb{L}$이라면 $u$는 $\mathbb{L}$에서 $\mathbb{L}$로의 $\mathbb{K}$-automorphism이다. 
2. $u$를 확장하는 $\Omega$의 $\mathbb{K}$-automorphism이 존재한다. 

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

1. 임의의 $x\in E$에 대하여, $x$의 minimal polynomial $f$가 주어졌다 하자. 집합 $\Phi$를 $\mathbb{L}$ 인에서의 $f$의 근들의 모임이라 하면 $\Phi$는 유한집합이다. 뿐민 아니라, 만일 $\alpha\in\Phi$라 하면 

    $$0=u(0)=u(f(\alpha))=f(u(\alpha))$$
    
    이므로 $u(\Phi)\subseteq\Phi$가 성립한다. 그런데 $u$는 zero map이 아니므로 injective이고, 따라서 $u$는 $\Phi$에서 $\Phi$로의 bijection이다. 따라서 $x\in\Phi=u(\Phi)\subseteq u(E)$이고 이로부터 $u(E)=E$이다.

2. $\overline{\mathbb{K}}$는 $u(\mathbb{L})$과 $\mathbb{L}$의 algebraic closure이므로 [§대수적 폐포, ⁋정리 5](/ko/math/field_theory/algebraically_closed_extensions#thm5)의 universal property로부터 원하는 결과를 얻는다. 

</details>