---
title: "사영공간의 닫힌 부분스킴"
description: "사영공간의 닫힌 부분스킴은 동차 다항식들의 영점집합으로 표현할 수 있으며, 이 성질 덕분에 아핀 스킴과 거의 비슷한 방식으로 다룰 수 있다."
excerpt: "Projective space의 closed subscheme과 homogeneous ideal의 대응"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/closed_subschemes_of_projective_spaces
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
last_modified_at: 2025-03-08
weight: 14
published: false

---

이제 우리는 closed subscheme의 예시로 $$\mathbb{P}_\mathbb{K}^n$$의 closed subscheme들을 살펴본다. $$\mathbb{P}^n$$은 affine scheme보다는 약간 복잡하지만 그래도 일반적인 scheme보다는 다루기가 편한 대상인데, [§사영스킴, ⁋정의 4](/ko/math/scheme_theory/projective_schemes#def4)에 의하여 $$\mathbb{P}^n$$의 임의의 닫힌집합은 항상 $$\mathbb{K}[\x_0,\ldots, \x_n]$$의 homogeneous polynomial들의 zero set으로 쓸 수 있기 때문이다. 즉, 이들 homogeneous polynomial들은, 비록 $$\mathbb{P}^n$$에서 정의된 함수는 아니지만 적어도 닫힌집합을 표현할 때는 affine scheme과 거의 유사한 방식을 사용할 수 있다.

이번 글에서 우리는 이 대응을 scheme의 단계로 끌어올린다. 즉 homogeneous ideal이 $$\mathbb{P}^n$$의 closed subscheme을 정의하고, 거꾸로 $$\mathbb{P}^n$$의 임의의 closed subscheme이 이러한 방식으로 얻어진다는 것을 살펴본다. 이번 글에서 $$S_\bullet=\mathbb{K}[\x_0,\ldots,\x_n]$$은 표준적인 grading이 주어진 graded ring이고, $$\mathbb{P}^n=\Proj S_\bullet$$이다.

## 동차 아이디얼이 정의하는 닫힌 부분스킴

Affine scheme의 경우 closed subscheme은 정확히 surjection $$A \rightarrow A/\mathfrak{a}$$들로부터 얻어졌다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의) 비록 $$\Proj$$는 functor가 아니지만 ([§사영스킴](/ko/math/scheme_theory/projective_schemes)), graded ring의 *surjection*은 언제나 $$\Proj$$들 사이의 morphism을 유도하며, 이것이 위 이야기의 projective 버전이 된다.

<div class="proposition" markdown="1">

<ins id="prop1">**명제 1**</ins> Homogeneous ideal $$\mathfrak{a}\subseteq S_\bullet$$과 canonical projection $$\pi:S_\bullet \rightarrow S_\bullet/\mathfrak{a}$$가 주어졌다 하자. 그럼 $$\pi$$는 closed embedding

$$\iota:\Proj (S_\bullet/\mathfrak{a}) \rightarrow \Proj S_\bullet=\mathbb{P}^n$$

을 유도하며, 그 image는 $$Z_+(\mathfrak{a})$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[\[대수적 구조\] §등급환](/ko/math/algebraic_structures/graded_rings)에서 살펴본 것과 같이 $$S_\bullet/\mathfrak{a}$$는 graded ring이고, 몫환의 ideal correspondence는 homogeneous ideal들을 homogeneous ideal들로 대응시킨다. 특히 $$\mathfrak{q}\mapsto \pi^{-1}(\mathfrak{q})$$는 $$\Proj(S_\bullet/\mathfrak{a})$$의 점들, 즉 $$(S_\bullet/\mathfrak{a})_+$$를 포함하지 않는 homogeneous prime ideal들을, $$\mathfrak{a}$$를 포함하고 $$S_+$$를 포함하지 않는 $$S_\bullet$$의 homogeneous prime ideal들로 보내는 bijection이며, 후자는 정확히 $$Z_+(\mathfrak{a})$$이다. ([§사영스킴, ⁋정의 2](/ko/math/scheme_theory/projective_schemes#def2)) 또, 이 대응 하에서 $$Z_+(\bar{\mathfrak{b}})$$ 꼴의 닫힌집합은 $$Z_+(\pi^{-1}(\bar{\mathfrak{b}}))\cap Z_+(\mathfrak{a})$$와 대응되므로 $$\iota$$는 그 image $$Z_+(\mathfrak{a})$$로의 homeomorphism이다.

이제 scheme morphism의 구조와 sheaf morphism의 surjectivity를 표준적인 affine cover 위에서 확인하자. 각각의 $$i$$에 대하여 $$\bar{\x}_i=\pi(\x_i)$$라 하면, 위의 대응에 의해 $$\iota^{-1}(D_+(\x_i))=D_+(\bar{\x}_i)$$이다. [§사영스킴, ⁋보조정리 8](/ko/math/scheme_theory/projective_schemes#lem8)의 identification $$D_+(\x_i)\cong\Spec S_{(\x_i)}$$, $$D_+(\bar\x_i)\cong \Spec (S_\bullet/\mathfrak{a})_{(\bar\x_i)}$$ 하에서, $$\iota$$의 제한은 ring homomorphism

$$S_{(\x_i)} \rightarrow (S_\bullet/\mathfrak{a})_{(\bar\x_i)};\qquad \frac{f}{\x_i^d}\mapsto \frac{\pi(f)}{\bar\x_i^d}$$

이 유도하는 affine scheme들 사이의 morphism이다. $$\pi$$가 surjective이므로 이 ring homomorphism도 surjective이고, 그 kernel은 localization의 exactness에 의하여

$$\mathfrak{a}_{(\x_i)}=\left\{\frac{a}{\x_i^d}\;\middle\vert\;\text{$a\in\mathfrak{a}$ homogeneous of degree $d$}\right\}$$

이다. 즉 $$\iota$$는 각 chart 위에서 $$\Spec\bigl(S_{(\x_i)}/\mathfrak{a}_{(\x_i)}\bigr) \rightarrow \Spec S_{(\x_i)}$$ 꼴의 closed embedding이고, 이들이 $$D_+(\x_i\x_j)$$들 위에서 호환되는 것은 위의 식이 $$\x_i$$의 선택과 무관한 방식으로 정의되었기 때문이다. 따라서 $$\iota$$는 scheme morphism이며, sheaf morphism $$\iota^\sharp:\mathcal{O}_{\mathbb{P}^n} \rightarrow \iota_\ast\mathcal{O}_{\Proj(S_\bullet/\mathfrak{a})}$$가 cover $$(D_+(\x_i))$$ 위에서 surjective이므로 stalk들 위에서도 surjective이다. 즉 $$\iota$$는 closed embedding이다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2))

</details>

이렇게 얻어진 closed subscheme을 $$V_+(\mathfrak{a})$$로 적는다. 즉 $$V_+(\mathfrak{a})$$는 위상공간으로서는 $$Z_+(\mathfrak{a})$$이고, scheme으로서는 $$\Proj(S_\bullet/\mathfrak{a})$$이다. 표기에서 짐작할 수 있듯 이는 affine scheme에서의 대응 $$\mathfrak{a}\mapsto \Spec(A/\mathfrak{a})$$의 projective 버전이다.

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 하나의 homogeneous polynomial $$f$$가 생성하는 ideal $$(f)$$에 대하여 $$V_+(f)=\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/(f)\bigr)$$를 degree $$\deg f$$의 *hypersurface*라 부른다. 가령 $$\mathbb{P}^2$$에서 $$V_+(\x_0\x_2-\x_1^2)$$은 conic이다.

한편 $$\mathbb{P}^2$$의 두 closed subscheme $$V_+(\x_0)$$과 $$V_+(\x_0^2)$$을 비교하면, 이들의 underlying space는 $$Z_+(\x_0)=Z_+(\x_0^2)$$으로 동일하지만 scheme 구조는 다르다. 실제로 chart $$D_+(\x_2)\cong\Spec\mathbb{K}[\x_0/\x_2,\x_1/\x_2]$$ 위에서 전자는 ideal $$(\x_0/\x_2)$$로, 후자는 $$(\x_0^2/\x_2^2)$$로 주어지며 후자의 좌표환은 nilpotent element를 갖는다. 이는 [§닫힌 부분스킴, ⁋예시 1](/ko/math/scheme_theory/closed_subschemes#ex1)에서 살펴본 double point의 projective 버전이다.

</div>

## 모든 닫힌 부분스킴은 동차 아이디얼로부터 얻어진다

이제 거꾸로 $$\mathbb{P}^n$$의 임의의 closed subscheme이 $$V_+(\mathfrak{a})$$의 꼴임을 보인다.

<div class="proposition" markdown="1">

<ins id="thm3">**정리 3**</ins> $$\mathbb{P}^n$$의 임의의 closed subscheme $$Z$$에 대하여, $$Z=V_+(\mathfrak{a})$$이도록 하는 homogeneous ideal $$\mathfrak{a}\subseteq S_\bullet$$이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각각의 $$i$$에 대하여 $$Z\cap D_+(\x_i)$$는 affine scheme $$D_+(\x_i)\cong\Spec S_{(\x_i)}$$의 closed subscheme이므로, [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의에 의하여 유일한 ideal $$I_i\subseteq S_{(\x_i)}$$에 대응된다. 이제 homogeneous element들의 집합

$$T=\left\{f\in S_\bullet\;\middle\vert\;\text{$f$ homogeneous,}\quad \frac{f}{\x_i^{\deg f}}\in I_i\text{ for all }i\right\}$$

을 생각하고, $$\mathfrak{a}$$를 $$T$$로 생성되는 ideal이라 하자. $$T$$가 homogeneous element들로 이루어져 있으므로 $$\mathfrak{a}$$는 homogeneous ideal이다. 우리의 주장은 모든 $$i$$에 대해 $$\mathfrak{a}_{(\x_i)}=I_i$$가 성립한다는 것이다.

우선 $$\mathfrak{a}_{(\x_i)}$$는 $$f/\x_i^{\deg f}$$ ($$f\in T$$) 꼴의 원소들로 생성되는 $$S_{(\x_i)}$$의 ideal인데, $$T$$의 정의에 의해 이들 생성원이 모두 $$I_i$$에 속하므로 $$\mathfrak{a}_{(\x_i)}\subseteq I_i$$이다.

거꾸로 $$g=f/\x_i^d\in I_i$$가 주어졌다 하자. 여기서 $$f$$는 degree $$d$$의 homogeneous polynomial이다. 충분히 큰 $$N$$에 대하여 $$\x_i^Nf\in T$$임을 보이면, $$g=(\x_i^Nf)/\x_i^{N+d}\in\mathfrak{a}_{(\x_i)}$$가 되어 증명이 끝난다. 이를 위해 각각의 $$j$$에 대하여 $$(\x_i^Nf)/\x_j^{N+d}\in I_j$$이도록 하는 $$N$$을 찾자. $$j=i$$인 경우는 임의의 $$N$$에 대해 성립하므로 $$j\neq i$$라 하자.

핵심은 $$I_i$$와 $$I_j$$가 교집합 $$D_+(\x_i\x_j)$$ 위에서 호환된다는 것이다. $$Z$$의 ideal sheaf $$\mathcal{I}_{Z/\mathbb{P}^n}=\ker\iota^\sharp$$를 생각하면 ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)), kernel은 단면들 위에서 계산되므로 $$\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i))=I_i$$이다. 한편 [§사영스킴, ⁋보조정리 9](/ko/math/scheme_theory/projective_schemes#lem9)에 의하여 $$D_+(\x_i\x_j)$$는 $$\Spec S_{(\x_i)}$$의 principal open subset $$D(\x_j/\x_i)$$이고, affine scheme 위에서 structure sheaf와 $$\iota_\ast\mathcal{O}_Z$$의 단면들은 모두 localization으로 주어지므로, localization의 exactness에 의해

$$\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i\x_j))=(I_i)_{\x_j/\x_i}=(I_j)_{\x_i/\x_j}$$

이다. 여기서 양변은 모두 $$S_{(\x_i\x_j)}$$의 ideal이다.

이제 $$g\in I_i$$의 $$S_{(\x_i\x_j)}$$에서의 image는 $$(I_j)_{\x_i/\x_j}$$에 속한다. 한편 $$h=f/\x_j^d\in S_{(\x_j)}$$에 대하여 $$S_{(\x_i\x_j)}$$ 안에서 $$h=(\x_i/\x_j)^d\,g$$이므로 $$h$$의 image도 $$(I_j)_{\x_i/\x_j}$$에 속한다. 즉 적당한 $$m_j\geq 0$$이 존재하여

$$\left(\frac{\x_i}{\x_j}\right)^{m_j}h=\frac{\x_i^{m_j}f}{\x_j^{m_j+d}}\in I_j$$

이다. 그럼 $$N=\max_{j\neq i}m_j$$로 두면, $$I_j$$가 ideal이므로 모든 $$j$$에 대하여 $$(\x_i^Nf)/\x_j^{N+d}=(\x_i/\x_j)^{N-m_j}\cdot(\x_i^{m_j}f)/\x_j^{m_j+d}\in I_j$$이고, 따라서 $$\x_i^Nf\in T$$이다.

종합하면 $$Z$$와 $$V_+(\mathfrak{a})$$는 $$\mathbb{P}^n$$의 closed subscheme으로서 같은 ideal sheaf를 가지므로, [§닫힌 부분스킴, ⁋보조정리 9](/ko/math/scheme_theory/closed_subschemes#lem9)를 양방향으로 적용하면 $$Z=V_+(\mathfrak{a})$$이다.

</details>

<div class="remark" markdown="1">

<ins id="rmk4">**참고 4**</ins> Affine의 경우와 달리 이 대응은 일대일이 아니다. 가령 irrelevant ideal $$S_+=(\x_0,\ldots,\x_n)$$에 대하여 $$Z_+(S_+)=\emptyset$$이므로 $$V_+(S_+)=V_+(S_\bullet)$$은 모두 empty scheme이다. 더 일반적으로 두 homogeneous ideal이 충분히 큰 degree에서 일치한다면 같은 closed subscheme을 정의하는데, 이는 chart $$D_+(\x_i)$$ 위에서의 ideal $$\mathfrak{a}_{(\x_i)}$$가 $$\x_i$$의 거듭제곱을 곱하는 것에 영향을 받지 않기 때문이다. 주어진 closed subscheme을 정의하는 homogeneous ideal 중 가장 큰 것을 택하는 표준적인 방법이 있으며 (*saturation*), 이에 대해서는 필요할 때 다시 살펴보기로 한다.

</div>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

--- 