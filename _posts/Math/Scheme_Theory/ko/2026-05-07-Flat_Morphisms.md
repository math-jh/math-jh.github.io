---
title: "평탄사상"
description: "가환대수학에서 평탄 가군의 정의를 시작으로, 스킴 사이의 평탄 사상의 개념과 기하학적 의미, 그리고 판정법과 예시를 다룬다. 평탄성은 사상의 fiber가 기저 위에서 일정한 대수적·기하학적 성질을 유지하도록 보장하는 핵심적인 성질이다."
excerpt: "Flat morphisms in algebraic geometry"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/flat_morphisms
drift_needed: true
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-02-21
weight: 10

---

대수기하학에서 모양들의 family를 다룰 때, 우리는 기저 위의 점이 변함에 따라 fiber가 "연속적으로" 변하기를 기대한다. 그러나 단순히 사상의 연속성만으로는 이 직관을 포착하기에 부족하다. 예를 들어 기저의 한 점에서 fiber의 차원이 갑자기 뛰거나, 특이점의 개수가 달라지는 등의 비연속적인 변화가 일어날 수 있다. 이러한 현상을 배제하고 fiber들이 일정한 대수적·기하학적 성질을 유지하도록 하는 개념이 바로 **평탄성**(flatness)이다. 본 글에서는 먼저 가환대수학적 맥락에서 평탄 가군을 정의한 뒤, 이를 바탕으로 [§스킴](/ko/math/scheme_theory/schemes) 사이의 평탄 사상을 소개하고 그 기하학적 의미와 판정법, 예시들을 살펴본다.

## 평탄 가군

가환환 $$A$$ 위의 가군 $$M$$이 평탄하다는 것은 대수적으로 자연스러운 조건이다. $$A$$-가군 사이의 텐서곱 함자 $$-\otimes_A M$$은 일반적으로 완전열을 보존하지 않는다. 즉, 단사 가군 동형사상 $$N' \hookrightarrow N$$에 대하여 $$N' \otimes_A M \rightarrow N \otimes_A M$$이 단사가 되지 않을 수 있다. 텐서곱이 가군들 사이의 "관계"를 망가뜨리는 이러한 현상을 방지하는 것이 평탄 가군의 본질이다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 가환환 $$A$$ 위의 가군 $$M$$이 **평탄**(flat)하다고 하면, 텐서곱 함자 $$-\otimes_A M$$이 정확한 함자(exact functor)인 것을 말한다. 즉, 임의의 $$A$$-가군의 짧은 완전열

$$0 \longrightarrow N' \longrightarrow N \longrightarrow N'' \longrightarrow 0$$

에 대하여

$$0 \longrightarrow N' \otimes_A M \longrightarrow N \otimes_A M \longrightarrow N'' \otimes_A M \longrightarrow 0$$

역시 짧은 완전열이 되는 것이다.

</div>

직관적으로 평탄 가군 $$M$$은 기존의 가군들에 포함되어 있던 선형관계를 텐서곱 이후에도 그대로 유지시킨다. 예를 들어 $$A = \mathbb{Z}$$ 위에서 $$\mathbb{Z}/2\mathbb{Z}$$는 평탄하지 않은데, 단사사상 $$\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}$$에 $$\mathbb{Z}/2\mathbb{Z}$$를 텐서곱하면

$$\mathbb{Z}/2\mathbb{Z} \xrightarrow{\times 2} \mathbb{Z}/2\mathbb{Z}$$

이 되어 영사상이 되고 단사성이 깨지기 때문이다. 반면 자유 가군은 항상 평탄하다. 역으로, 국소환 위에서는 유한표시 평탄 가군이 자유 가군이라는 사실 또한 알려져 있다.

## 평탄 사상의 정의

이제 scheme의 맥락으로 넘어가보자. Morphism $$f: X \to Y$$가 평탄하다는 것은 대역적으로 말해 $$X$$의 구조층이 $$Y$$의 구조층 위에서 평탄한 가군 구조를 가진다는 의미이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Morphism $$f: X \to Y$$가 **평탄**(flat)하다고 하면, 임의의 $$x \in X$$에 대하여 국소환 $$\mathcal{O}_{X,x}$$가 $$\mathcal{O}_{Y,f(x)}$$-가군으로서 평탄한 것을 말한다. 추가로 $$f$$가 대응하는 위상공간의 사상이 surjective이면 **충실히 평탄**(faithfully flat)하다고 부른다.

</div>

평탄성은 [§스킴 사이의 사상](/ko/math/scheme_theory/morphism_of_schemes)이 가지는 가장 중요한 대수적 성질 중 하나이다. 특히 평탄 사상의 fiber는 기저의 변화에 따라 예측 가능한 방식으로 변화하며, 이는 곧 기하학적 성질들이 family를 따라 일정하게 유지됨을 의미한다.

## 기하학적 성질

평탄 사상의 가장 기하학적으로 직관적인 특징은 fiber의 [§차원](/ko/math/scheme_theory/dimension)이 기저 위에서 locally constant하다는 점이다. 일반적인 morphism의 경우 Chevalley의 정리에 의해 fiber 차원은 위로 반연속(upper semi-continuous)이지만, 평탄성이 주어지면 이 반연속성이 양방향이 되어 fiber 차원이 일정해진다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> Locally Noetherian scheme 사이의 평탄 사상 $$f: X \to Y$$가 locally of finite type이면, 함수

$$y \longmapsto \dim f^{-1}(y)$$

은 $$Y$$ 위에서 locally constant이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Chevalley의 정리에 의해, locally of finite type인 사상에 대하여 $$y \mapsto \dim f^{-1}(y)$$는 위로 반연속이다. 한편 평탄성 가정 하에서, 임의의 $$y \in Y$$에 대하여 $$f^{-1}(y)$$의 차원은 근처의 점들에서 떨어지지 않는다는 사실도 성립한다. 이는 [\[가환대수학\] §평탄성과 국소화, ⁋정리 1](/ko/math/commutative_algebra/local_criterion_for_flatness#thm1)의 국소 판정법과 차원공식을 통해 보일 수 있다. 위로 반연속이면서 동시에 아래로도 반연속인 함수는 locally constant이므로 결론을 얻는다.

</details>

평탄 사상의 또 다른 중요한 기하학적 성질은 열린집합을 열린집합으로 본다는 점이다. 사실 더 강력한 결과가 성립한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> 평탄하고 locally of finite type이며 dominant인 사상 $$f: X \to Y$$는 열린 사상(open map)이다. 즉, 임의의 열린집합 $$U \subseteq X$$의 상 $$f(U)$$는 $$Y$$의 열린집합이다.

</div>
<details class="proof" markdown="1">

Chevalley의 정리에 의해 locally of finite type 사상의 상은 생성가능 집합(constructible set)이다. Noetherian 공간에서 생성가능 집합이 열린집합이 될 필요충분조건은 일반화(generization)에 대해 닫혀 있는 것이다. $$f$$가 평탄이면 충실히 평탄인 국소화를 통해, $$f(U)$$가 일반화에 대해 닫혀 있음을 보일 수 있다. 구체적으로 $$y' \in \overline{\{y\}}$$이고 $$y \in f(U)$$라 하자. 평탄성에 의해 $$U$$ 위의 일반화는 $$f(U)$$ 위로 올라가고, 따라서 $$y' \in f(U)$$이다.

</details>

평탄성은 매끄러운 사상(smooth morphism)보다 더 약한 조건이다. 사실 매끄러움은 정칙성(regularity)의 상대적 버전이며, 이는 평탄성을 내포한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> 매끄러운 사상(smooth morphism)은 평탄이다.

</div>
<details class="proof" markdown="1">

$$f: X \to Y$$가 매끄러운 사상이라 하자. 매끄러움은 locally of finite presentation이며, 임의의 $$x \in X$$에 대하여 국소환 $$\mathcal{O}_{X,x}$$가 $$\mathcal{O}_{Y,f(x)}$$ 위에서 정칙 국소환(regular local ring)으로서 상대차원 $$d$$를 가진다. 즉, 최대 아이디얼 $$\mathfrak{m}_x$$는 $$d$$개의 원소 $$f_1, \dots, f_d$$와 $$\mathfrak{m}_{f(x)}$$에 의해 생성되며, $$\mathcal{O}_{X,x}/(f_1, \dots, f_d)$$는 $$\mathcal{O}_{Y,f(x)}$$ 위에서 평탄하다. 정칙 국소환의 정의와 국소 판정법에 의해 $$\mathcal{O}_{X,x}$$ 자체가 $$\mathcal{O}_{Y,f(x)}$$-평탄 가군이 됨을 알 수 있다.

</details>

## 평탄성의 판정법

평탄성을 직접 검증하는 것은 어려울 수 있으므로, 이를 판정하는 여러 기준이 개발되었다. 가장 기본적인 것은 국소 판정법(local criterion for flatness)이다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6** (국소 평탄성 판정법). Noetherian 국소환 $$(A, \mathfrak{m})$$과 유한생성 $$A$$-가군 $$M$$이 주어졌다고 하자. $$A$$의 임의의 아이디얼 $$I$$에 대하여 $$M/IM$$이 $$A/I$$-평탄이고, 추가로 $$\operatorname{Tor}_1^A(M, A/I) = 0$$이면 $$M$$은 $$A$$-평탄이다. 특히 $$I = \mathfrak{m}$$인 경우, $$M/\mathfrak{m}M$$이 $$A/\mathfrak{m}$$ 위에서 평탄(즉, 자유)이고 $$\operatorname{Tor}_1^A(M, A/\mathfrak{m}) = 0$$이면 $$M$$은 평탄이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

아이디얼 $$I$$에 대하여, $$M$$이 $$A$$-평탄임을 보이기 위해 $$\operatorname{Tor}_1^A(M, N) = 0$$이 임의의 유한생성 $$A$$-가군 $$N$$에 대해 성립함을 보인다. $$N$$에 대한 filtration을 사용하여, 귀납적으로 $$N = A/\mathfrak{p}$$인 소아이디얼 $$\mathfrak{p}$$에 대한 경우만 확인하면 충분하다. 국소 판정법의 표준적인 증명은 $$I$$-adic 완비화와 Artin-Rees 보조정리를 사용하여, $$M$$의 완비화가 평탄임을 보이고 이로부터 $$M$$ 자체의 평탄성을 유도한다. 자세한 내용은 [\[가환대수학\] §평탄성과 국소화, ⁋정의 4](/ko/math/commutative_algebra/local_criterion_for_flatness#def4)를 참고하라.

</details>

호몰로지 대수학의 관점에서는 [§Ext와 Tor](/ko/math/homological_algebra/ext_and_tor)를 이용하여 평탄성을 판정할 수 있다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7** ($$\operatorname{Tor}$$ 판정법). $$A$$-가군 $$M$$이 평탄인 것은 임의의 아이디얼 $$I \subseteq A$$에 대하여 $$\operatorname{Tor}_1^A(M, A/I) = 0$$이 되는 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$-\otimes_A M$$이 정확한 함자임을 보이기 위해, 단사사상 $$N' \hookrightarrow N$$이 주어졌을 때 $$N' \otimes_A M \rightarrow N \otimes_A M$$이 단사임을 확인하면 충분하다. $$\operatorname{Tor}_1^A(M, -)$$가 모든 순환 가군 $$A/I$$에 대해 소멸한다는 가정 하에서, 긴 완전열에 의해 이는 임의의 유한생성 가군, 나아가 임의의 가군에 대해서도 성립한다. 따라서 $$-\otimes_A M$$은 정확하고, $$M$$은 평탄이다. 역방향은 평탄 가군의 정의에 의해 $$-\otimes_A M$$이 정확한 함자이므로, 임의의 단사사상에 대한 텐서곱이 단사가 되어 $$\operatorname{Tor}_1^A(M, A/I) = 0$$이 성립한다.

</details>

마지막으로, 제네릭 평탄성(generic flatness)은 평탄 영역이 기저 위에서 조밀한 열린집합을 이룬다는 중요한 정리이다.

<div class="proposition" markdown="1">

<ins id="prop8">**명제 8** (제네릭 평탄성). Noetherian scheme $$Y$$ 위의 integral scheme $$X$$로의 dominant morphism $$f: X \to Y$$가 finite type이면, $$Y$$의 어떤 조밀한 열린집합 $$U$$ 위에서 $$f\rvert_{f^{-1}(U)}: f^{-1}(U) \to U$$가 평탄이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제는 affine하게 환원할 수 있다. 즉, $$Y = \operatorname{Spec} A$$, $$X = \operatorname{Spec} B$$로 두고, $$A$$가 Noetherian 정역, $$B$$가 $$A$$ 위에서 finite type인 가군이며 $$A \to B$$가 단사라고 가정한다. 대수적 버전의 제네릭 평탄성에 의해, $$A$$의 영원소 $$f \neq 0$$가 존재하여 $$B_f$$가 $$A_f$$-평탄이다. 이는 곧 $$D(f) \subseteq Y$$ 위에서 $$f$$가 평탄임을 의미한다. 이 정리의 증명은 $$B$$를 유한생성 $$A$$-대수로 보고, 그 분수체에서의 평탄성을 확보한 뒤 이를 적절한 localization으로 전파시키는 방식으로 이루어진다.

</details>

## 예시

평탄 사상과 그렇지 않은 사상의 전형적인 예시들을 살펴보자.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins>

(1) 열린 부분스킴으로의 열린 포함사상(open immersion)은 평탄이다. 이는 국소적으로 localization에 해당하며, localization은 항상 평탄하다.

(2) 아핀 공간 사이의 사영사상 $$\mathbb{A}_k^{n+m} \to \mathbb{A}_k^n$$, 즉 $$k[x_1, \dots, x_n] \to k[x_1, \dots, x_n, y_1, \dots, y_m]$$은 평탄이다. 이는 다변수 다항식환의 자유 가군 구조로부터 바로 얻어진다.

</div>

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 평탄하지 않은 대표적인 예로, cusp의 family를 고려하자. $$k$$를 체로 하고, $$\mathbb{A}_k^1 = \operatorname{Spec} k[t]$$ 위의 family

$$X = \operatorname{Spec} k[t, x, y]/(y^2 - x^3 - t) \longrightarrow \mathbb{A}_k^1$$

를 생각한다. $$t \neq 0$$인 점에서는 fiber가 non-singular한 타원곡선(genus 1)이 되지만, $$t = 0$$에서는 fiber가 cusp $$y^2 = x^3$$가 되어 singular해진다. 이 사상은 $$t = 0$$에서 평탄하지 않다. 사실 $$k[t]_{(t)}$$ 위에서 $$k[t, x, y]/(y^2 - x^3 - t)_{(t)}$$를 생각하면, 이 가군은 $$t$$에 의해 영이 되는 원소를 가지므로 $$t$$-torsion이 존재하여 평탄성이 깨진다. 직관적으로 fiber의 위상적 형태가 갑자기 변하기 때문에 평탄성이 상실된 것이다.

비슷하게 node의 family

$$\operatorname{Spec} k[t, x, y]/(xy - t) \longrightarrow \mathbb{A}_k^1$$

역시 $$t = 0$$에서 평탄하지 않다. $$t \neq 0$$일 때는 fiber가 두 개의 교차하는 직선이지만, $$t = 0$$에서는 노드(node) $$xy = 0$$가 되어 위상적으로 다른 형태를 띤다.

</div>

<div class="example" markdown="1">

<ins id="ex11">**예시 11**</ins> 양수 특성 $$p > 0$$인 체 $$k$$ 위의 scheme $$X$$에 대하여, **Frobenius 사상**

$$F: X \longrightarrow X$$

은 구조층 위에서 $$p$$제곱사상 $$a \mapsto a^p$$을 유도한다. 이 사상은 일반적으로 평탄하지 않다. Kunz의 정리에 의해, $$X$$가 정칙(regular)인 것과 $$F$$가 평탄인 것이 동치이다. 따라서 $$X$$가 특이점을 가지면 Frobenius 사상은 평탄이 아니다. 예를 들어 $$X = \operatorname{Spec} k[x, y]/(xy)$$는 노드(node)이며, 이 점에서 Frobenius는 평탄하지 않다.

</div>

## 평탄 사상의 성질

평탄성은 기본적인 연산들 아래에서 잘 거동한다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins>

(1) 평탄 사상의 기저변환([§올곱](/ko/math/scheme_theory/fiber_products))은 평탄이다. 즉, $$f: X \to Y$$가 평탄이고 $$Z \to Y$$가 임의의 사상이면, 투영사상 $$X \times_Y Z \to Z$$는 평탄이다.

(2) 평탄 사상들의 합성은 평탄이다. 즉, $$f: X \to Y$$와 $$g: Y \to Z$$가 모두 평탄이면 $$g \circ f: X \to Z$$도 평탄이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) 기저변환은 국소적으로 텐서곱 $$B \otimes_A C$$의 형태를 띤다. $$B$$가 $$A$$-평탄이면, $$-\otimes_A (B \otimes_A C) \cong (-\otimes_A B) \otimes_B (B \otimes_A C)$$이므로 정확성이 보존된다. 따라서 $$B \otimes_A C$$는 $$C$$-평탄이다.

(2) 합성의 경우, $$(g \circ f)^{-1}$$에 대한 구조층의 전진은 $$g_\ast f_\ast \mathcal{O}_X$$이다. $$f_\ast \mathcal{O}_X$$가 $$\mathcal{O}_Y$$-평탄 가군이고, $$g_\ast$$에 의해 평탄성이 보존되므로, 합성사상 역시 평탄이다. 대수적으로, $$A \to B$$와 $$B \to C$$가 모두 평탄이면 임의의 $$A$$-가군 $$N$$에 대해 $$N \otimes_A C \cong (N \otimes_A B) \otimes_B C$$이며, 각 단계에서 정확성이 보존되어 $$-\otimes_A C$$도 정확하다.

</details>

또한 평탄하지 않은 점들이 모여 있는 집합은 닫힌 집합을 이룬다는 사실도 중요하다.

<div class="proposition" markdown="1">

<ins id="prop13">**명제 13**</ins> Locally finite presentation인 사상 $$f: X \to Y$$에 대하여, $$X$$에서 $$f$$가 평탄하지 않은 점들의 집합은 닫힌집합이다. equivalently, 평탄 영역(flat locus)은 $$X$$의 열린집합이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제는 국소적이므로 $$Y = \operatorname{Spec} A$$, $$X = \operatorname{Spec} B$$로 가정한다. $$B$$가 $$A$$ 위에서 finite presentation이라 하자. 평탄성은 국소적으로 $$\operatorname{Tor}$$ 함자의 소멸으로 판정되며, $$\operatorname{Tor}_1^A(B, -)$$의 소멸은 특정 행렬식의 비소멸 조건으로 기술된다. 이러한 조건은 열린 조건을 이루므로, 평탄한 점들의 집합은 열린집합이 된다. Noetherian 경우에는 이를 아이디얼들의 높이를 통해 더욱 명시적으로 기술할 수 있다.

</details>

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*, Springer, 1977.

**[Stacks]** The Stacks Project Authors, *Stacks Project*, https://stacks.math.columbia.edu, Tag 00MD, Tag 00R3, Tag 01UA.

**[EGA]** A. Grothendieck, *Éléments de géométrie algébrique*, IHES, 1960–1967.

**[Mats]** H. Matsumura, *Commutative ring theory*, Cambridge University Press, 1986.
