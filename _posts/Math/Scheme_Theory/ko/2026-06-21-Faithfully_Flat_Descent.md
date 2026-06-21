---
title: "충실평탄 하강"
description: "충실평탄 사상을 따라 대수적·기하학적 데이터를 내려보내는 Grothendieck의 하강 이론을 다룬다. Amitsur 복합체의 정확성으로부터 가군의 하강 정리를 유도하고, descent datum의 범주가 밑환 위의 가군 범주와 동치임을 보인 뒤, 이를 fpqc 위상 위의 준연접층과 사상의 하강으로 확장한다."
excerpt: "Faithfully flat descent, descent datum, the cocycle condition, fpqc topology and effective descent"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/faithfully_flat_descent
sidebar: 
    nav: "scheme_theory-ko"

date: 2026-06-21
weight: 22

published: false
---

대수기하학에서 어떤 대상이 국소적으로 주어졌을 때 이를 전역적으로 붙여 하나의 대상으로 만드는 일은 흔하다. 가장 익숙한 예는 열린덮개를 따라 sheaf의 section을 붙이는 것이다. 그런데 열린덮개는 본질적으로 단사적인 국소화에 불과하여, 실제로 다루고 싶은 많은 상황을 포착하지 못한다. 예를 들어 field extension $$\mathbb{K}\subseteq L$$을 따라 $$L$$ 위에서 정의된 대상을 $$\mathbb{K}$$ 위로 내려보내는 일이나, 어떤 covering space 위의 데이터를 밑공간 위로 모으는 일은 열린덮개의 언어로는 표현되지 않는다. Grothendieck은 이러한 상황을 통일적으로 다루기 위해, 열린포함사상보다 훨씬 넓은 *충실평탄 사상<sub>faithfully flat morphism</sub>*을 일종의 덮개로 받아들이는 관점을 도입하였다. 핵심은 충실평탄 사상이 정확성을 정확히 반영한다는 대수적 사실이며, 이로부터 밑환 위의 가군을 그보다 큰 환 위의 가군과 적절한 접합 조건으로 완전히 복원할 수 있다는 *하강<sub>descent</sub>* 정리가 따라온다. 이번 글에서는 먼저 가군 수준에서 이 정리를 확립하고, 이어 그 sheaf적·기하학적 형태인 fpqc 위상 위의 하강으로 끌어올린다.

## 충실평탄 사상

충실평탄성은 평탄성에 전사성을 더한 조건이다. 가군 수준에서 ring homomorphism $$\varphi: A \rightarrow B$$가 충실평탄이라 함은 $$B$$가 평탄 $$A$$-가군이면서 ([\[가환대수학\] §평탄성, ⁋명제 1](/ko/math/commutative_algebra/flatness#prop1)) 다음 명제가 보여주듯 정확성을 단순히 보존할 뿐 아니라 반영하는 것이다. 사상 수준에서는 이를 ([§평탄사상, ⁋정의 2](/ko/math/scheme_theory/flat_morphisms#def2))에서 평탄이면서 surjective인 morphism으로 정의하였다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Ring homomorphism $$\varphi: A \rightarrow B$$가 *faithfully flat<sub>충실평탄</sub>*하다는 것은, $$B$$가 평탄 $$A$$-가군이고, 동시에 임의의 $$A$$-가군 $$M$$에 대하여 $$M\otimes_A B=0$$이면 $$M=0$$인 것이다.

</div>

위 정의의 둘째 조건이 "충실"이라는 이름의 출처이다. 즉 $$-\otimes_A B$$가 $$0$$이 아닌 가군을 $$0$$으로 보내지 않는다는 것이다. 이 조건은 여러 동치 형태를 가진다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 평탄 ring homomorphism $$\varphi: A \rightarrow B$$에 대하여 다음이 동치이다.

1. $$\varphi$$는 충실평탄이다.
2. $$A$$-가군의 sequence $$M' \rightarrow M \rightarrow M''$$이 정확한 것은, $$B$$-가군의 sequence $$M'\otimes_A B \rightarrow M\otimes_A B \rightarrow M''\otimes_A B$$가 정확한 것과 동치이다.
3. $$\varphi$$가 유도하는 사상 $$\Spec B \rightarrow \Spec A$$는 surjective이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

(1) $$\Rightarrow$$ (2). $$B$$가 평탄이므로 정확한 sequence는 $$-\otimes_A B$$ 후에도 정확하다. 역을 보이기 위해 $$M' \xrightarrow{f} M \xrightarrow{g} M''$$이 $$-\otimes_A B$$ 후 정확하다 하자. $$H=\ker g/\im f$$라 두면, $$B$$가 평탄이므로 homology가 tensor와 commute하여 $$H\otimes_A B=\ker(g\otimes 1)/\im(f\otimes 1)=0$$이다. 충실성에 의해 $$H=0$$이고 따라서 원래 sequence가 정확하다.

(2) $$\Rightarrow$$ (1). $$M\otimes_A B=0$$이라 하면, sequence $$0 \rightarrow M \rightarrow 0$$이 $$-\otimes_A B$$ 후 정확하므로 (2)에 의해 $$0 \rightarrow M \rightarrow 0$$이 정확하여 $$M=0$$이다. 따라서 $$\varphi$$는 충실평탄이다.

(1) $$\Rightarrow$$ (3). 임의의 $$\mathfrak{p}\in \Spec A$$에 대하여 잔여체 $$\kappa(\mathfrak{p})=A_\mathfrak{p}/\mathfrak{p}A_\mathfrak{p}$$를 생각하면, $$\mathfrak{p}$$가 $$\varphi$$의 상에 속하는 것은 fiber $$\Spec(B\otimes_A \kappa(\mathfrak{p}))$$가 비어있지 않은 것, 즉 $$B\otimes_A \kappa(\mathfrak{p})\neq 0$$인 것과 동치이다. ([§올곱, ⁋예시 9](/ko/math/scheme_theory/fiber_products#ex9)) 그런데 $$\kappa(\mathfrak{p})\neq 0$$이므로 충실성에 의해 $$\kappa(\mathfrak{p})\otimes_A B\neq 0$$이고, 따라서 $$\mathfrak{p}$$는 상에 속한다.

(3) $$\Rightarrow$$ (1). $$M\neq 0$$인 $$A$$-가군을 잡고 $$0\neq x\in M$$을 택하면, $$Ax\cong A/I$$ ($$I=\operatorname{Ann}(x)$$)인 부분가군이 있다. $$I\subseteq \mathfrak{m}$$인 maximal ideal $$\mathfrak{m}$$을 잡으면, (3)에 의해 $$\mathfrak{m}$$은 $$\varphi$$의 상에 속하므로 $$\kappa(\mathfrak{m})\otimes_A B\neq 0$$이다. 전사 $$A/I\twoheadrightarrow A/\mathfrak{m}=\kappa(\mathfrak{m})$$에 $$-\otimes_A B$$를 적용하면 (텐서곱은 우완전) 전사 $$(A/I)\otimes_A B\twoheadrightarrow \kappa(\mathfrak{m})\otimes_A B$$를 얻는데, 우변이 $$0$$이 아니므로 $$(A/I)\otimes_A B\neq 0$$이다. 다시 $$A/I=Ax\hookrightarrow M$$에 평탄성을 적용하면 $$(A/I)\otimes_A B\hookrightarrow M\otimes_A B$$이므로 $$M\otimes_A B\neq 0$$이다.

</details>

[명제 2](#prop2)의 둘째 조건이 하강 이론 전체를 떠받치는 사실이다. 정확성을 base change로 검사할 수 있다는 것은, $$B$$ 위에서 성립하는 정확성에 관한 진술이 $$A$$ 위로 그대로 내려온다는 것을 뜻한다. 특별히 $$M' \rightarrow M$$이 단사 또는 전사인 것도 $$-\otimes_A B$$ 후의 단사·전사로 판정된다. 셋째 조건은 이 대수적 성질이 정확히 사상 $$\Spec B \rightarrow \Spec A$$의 전사성에 대응함을 보여주며, 따라서 충실평탄 ring homomorphism은 [§평탄사상, ⁋정의 2](/ko/math/scheme_theory/flat_morphisms#def2)의 affine 충실평탄 사상에 다름 아니다.

가장 중요한 예시는 $$A$$의 원소들 $$f_1,\ldots, f_n$$이 $$A$$ 전체를 생성할 때 ($$\sum f_i A=A$$) 얻어지는 $$A \rightarrow \prod_i A_{f_i}$$이다. 각 $$A_{f_i}$$가 평탄이므로 그 곱도 평탄이고, $$\Spec \prod A_{f_i}=\coprod D(f_i)$$가 $$\Spec A$$를 덮으므로 surjective이다. 즉 한 affine scheme의 principal open cover는 충실평탄 사상의 한 경우이며, 이 점에서 충실평탄 하강은 열린덮개를 따른 sheaf의 접합을 포함하는 일반화이다. 더 나아가 field extension $$\mathbb{K}\subseteq L$$은 항상 충실평탄인데, $$L$$이 $$\mathbb{K}$$ 위의 vector space로서 free이고 $$L\neq 0$$이기 때문이다.

## Amitsur 복합체의 정확성

하강의 출발점은 충실평탄 사상이 그 자신의 "이중 덮개"와 맺는 관계이다. Ring homomorphism $$\varphi: A \rightarrow B$$가 주어지면 두 사상

$$d^0, d^1: B \rightrightarrows B\otimes_A B,\qquad d^0(b)=b\otimes 1,\quad d^1(b)=1\otimes b$$

이 있고, 이들의 차 $$d=d^1-d^0$$를 통해 sequence

$$0 \rightarrow A \xrightarrow{\varphi} B \xrightarrow{d} B\otimes_A B$$

를 얻는다. 이를 *Amitsur 복합체<sub>Amitsur complex</sub>*의 처음 두 마디라 부른다. 다음 보조정리가 충실평탄 하강의 핵심이다.

<div class="proposition" markdown="1">

<ins id="lem3">**보조정리 3**</ins> $$\varphi: A \rightarrow B$$가 충실평탄이면, 위의 sequence

$$0 \rightarrow A \xrightarrow{\varphi} B \xrightarrow{d^1-d^0} B\otimes_A B$$

는 정확하다. 즉 $$\varphi$$는 단사이고, 그 상은 $$d^0$$과 $$d^1$$이 일치하는 원소들 $$\{b\in B\mid b\otimes 1=1\otimes b\}$$과 정확히 일치한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

[명제 2](#prop2)에 의하여, 이 sequence가 정확함을 보이는 것은 $$-\otimes_A B$$를 취한 뒤의 sequence가 정확함을 보이는 것으로 충분하다. $$-\otimes_A B$$를 적용하면

$$0 \rightarrow B \xrightarrow{\varphi\otimes 1} B\otimes_A B \xrightarrow{(d^1-d^0)\otimes 1} B\otimes_A B\otimes_A B$$

를 얻는데, 이는 $$B$$ 위에서 분리되어 정확함을 직접 확인할 수 있다. 실제로 $$B$$ 자신을 통한 section을 만들기 위해, 사상

$$s: B\otimes_A B \rightarrow B;\qquad s(b\otimes b')=bb'$$

과 $$t: B\otimes_A B\otimes_A B \rightarrow B\otimes_A B$$를 $$t(b\otimes b'\otimes b'')=bb'\otimes b''$$로 정의하자. 이들은 $$B$$-선형이며 (가장 왼쪽 $$B$$ 인수에 대한 작용으로 본다), $$s\circ(\varphi\otimes 1)=\id_B$$이므로 $$\varphi\otimes 1$$은 단사이다. 또 $$b\otimes b'\in \ker((d^1-d^0)\otimes 1)$$이면 $$b\otimes 1\otimes b'=b\otimes b'\otimes 1$$이고, 여기에 $$t$$를 적용하면

$$b\otimes b'=t(b\otimes 1\otimes b')=t(b\otimes b'\otimes 1)=bb'\otimes 1=(\varphi\otimes 1)(s(b\otimes b'))$$

이므로 $$\ker((d^1-d^0)\otimes 1)\subseteq \im(\varphi\otimes 1)$$이다. 역포함은 $$(d^1-d^0)\circ \varphi=0$$로부터 자명하므로, base change된 sequence는 정확하다. 따라서 원래 sequence도 정확하다.

</details>

[보조정리 3](#lem3)은 $$A$$가 $$B$$의 데이터로부터 어떻게 복원되는지를 정확하게 말해준다. $$A$$는 $$B$$ 안에서 "두 가지 방식의 base change가 일치하는" 원소들로 특징지어진다. 이 원리를 가군 위로 옮기면 하강 정리가 된다. 직관적으로, $$B$$-가군 하나만으로는 $$A$$-가군을 복원하기에 부족하지만, 그 $$B$$-가군이 $$B\otimes_A B$$ 위에서 "양쪽 base change가 호환된다"는 추가 데이터를 가지면 충분하다는 것이다. 이 추가 데이터를 정식화한 것이 descent datum이다.

## Descent datum

$$B$$-가군 $$N$$이 어떤 $$A$$-가군 $$M$$의 base change $$M\otimes_A B$$로부터 왔다고 하자. 그럼 $$N\otimes_A B$$를 만드는 두 방법, 즉 $$N$$의 $$B$$-구조를 첫째 인수로 보느냐 둘째 인수로 보느냐에 따라 $$B\otimes_A B$$-가군 두 개가 생기는데, $$N=M\otimes_A B$$인 경우 둘 다 $$M\otimes_A B\otimes_A B$$와 같아져 자연스러운 동형을 가진다. Descent datum은 이 동형을 추상적인 출발 데이터로 승격한 것이다.

표기를 고정하자. $$B\otimes_A B$$ 위에서 세 사상

$$p_1, p_2: B \rightrightarrows B\otimes_A B,\qquad p_{12}, p_{13}, p_{23}: B\otimes_A B \rightrightarrows B\otimes_A B\otimes_A B$$

를 둔다. 여기에서 $$p_1(b)=b\otimes 1$$, $$p_2(b)=1\otimes b$$이고, $$p_{12}, p_{13}, p_{23}$$은 세 인수 가운데 표시된 두 자리로 보내는 자명한 사상이다. $$B$$-가군 $$N$$에 대하여 $$p_i^\ast N=N\otimes_{B, p_i}(B\otimes_A B)$$로 적으면, $$p_1^\ast N=N\otimes_A B$$ (둘째 인수에 새 $$B$$를 붙임), $$p_2^\ast N=B\otimes_A N$$ (첫째 인수에 붙임)이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$\varphi: A \rightarrow B$$에 대한 *descent datum<sub>하강 자료</sub>*은 $$B$$-가군 $$N$$과 $$B\otimes_A B$$-가군 동형사상

$$\varphi_N: p_1^\ast N=N\otimes_A B \xrightarrow{\ \sim\ } B\otimes_A N=p_2^\ast N$$

의 쌍 $$(N, \varphi_N)$$으로서, $$B\otimes_A B\otimes_A B$$ 위에서 *cocycle 조건*

$$p_{13}^\ast \varphi_N=p_{23}^\ast \varphi_N\circ p_{12}^\ast \varphi_N$$

을 만족하는 것이다. 두 descent datum $$(N, \varphi_N)$$과 $$(N', \varphi_{N'})$$ 사이의 *morphism*은 $$B$$-가군 준동형사상 $$g: N \rightarrow N'$$으로서 $$\varphi_{N'}\circ(g\otimes 1)=(1\otimes g)\circ \varphi_N$$을 만족하는 것이다. 이들은 category를 이루며 이를 $$\operatorname{Desc}(B/A)$$로 적는다.

</div>

여기에서 $$p_{ij}^\ast \varphi_N$$은 $$\varphi_N$$을 $$p_{ij}$$를 따라 $$B\otimes_A B\otimes_A B$$ 위로 base change한 사상으로, 각각 $$N\otimes_A B\otimes_A B$$의 세 가지 배치 사이의 동형이다. Cocycle 조건은 세 변 $$1\to 2$$, $$2\to 3$$, $$1\to 3$$ 위에서 이 동형들이 합성에 대해 일관됨을 요구하는 것이며, 그 기하학적 의미는 세 겹 겹침 위에서 접합이 모순 없이 이루어진다는 것이다. 이는 sheaf를 열린덮개에서 붙일 때 transition function들이 만족해야 하는 cocycle 관계의 직접적인 유비이다.

![cocycle condition](/assets/images/Math/Scheme_Theory/Faithfully_Flat_Descent-1.svg){:style="width:15.94em" class="invert" .align-center}

Base change로 만들어지는 자연스러운 descent datum이 위 정의의 원형이다.

<div class="example" markdown="1">

<ins id="ex5">**예시 5**</ins> $$A$$-가군 $$M$$에 대하여 $$N=M\otimes_A B$$로 두면, 두 base change는

$$p_1^\ast N=M\otimes_A B\otimes_A B=p_2^\ast N$$

으로 동일한 $$B\otimes_A B$$-가군이며, $$\varphi_N=\id$$로 두면 descent datum이 된다. 이를 $$M$$에 딸린 *canonical descent datum*이라 부른다. Cocycle 조건은 세 사상이 모두 항등이므로 자명하게 성립한다. 더 일반적으로 $$A$$-가군 준동형사상 $$M \rightarrow M'$$은 base change하여 canonical descent datum 사이의 morphism을 주므로, 대응 $$M\mapsto (M\otimes_A B, \id)$$은 functor

$$\Mod(A) \rightarrow \operatorname{Desc}(B/A)$$

를 정의한다.

</div>

[예시 5](#ex5)의 functor가 무엇을 잃거나 더하는지가 다음 절의 주제이다. Descent 정리는 이 functor가 충실평탄 $$\varphi$$에 대하여 범주의 동치임을 주장한다. 즉 모든 descent datum이 본질적으로 canonical한 것이며, 따라서 $$B\otimes_A B$$ 위의 호환 데이터를 갖춘 $$B$$-가군은 언제나 어떤 $$A$$-가군으로부터 유일하게 내려온다는 것이다.

## 가군의 하강

이제 주요 정리를 진술하고 증명한다. 한 방향은 descent datum으로부터 $$A$$-가군을 복원하는 것으로, [보조정리 3](#lem3)이 알려준 "$$A$$는 $$B$$ 안의 호환 원소들"이라는 원리를 가군 위에서 실현한다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6** (충실평탄 하강)</ins> $$\varphi: A \rightarrow B$$가 충실평탄이면, [예시 5](#ex5)의 functor

$$\Mod(A) \rightarrow \operatorname{Desc}(B/A);\qquad M\mapsto (M\otimes_A B, \id)$$

은 categorical equivalence이다. 그 역함자는 descent datum $$(N, \varphi_N)$$에 대하여

$$M=\{n\in N\mid \varphi_N(n\otimes 1)=1\otimes n\}$$

으로 주어진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

두 functor가 서로 quasi-inverse임을 보인다. 역함자를 $$(N, \varphi_N)\mapsto N^{\varphi}$$로 적자. 여기에서 $$N^\varphi=\{n\in N\mid \varphi_N(n\otimes 1)=1\otimes n\}$$이며, 이는 $$N\otimes_A B \rightrightarrows B\otimes_A N$$의 두 사상 $$n\mapsto \varphi_N(n\otimes 1)$$과 $$n\mapsto 1\otimes n$$의 equalizer이므로 $$A$$-부분가군이다.

먼저 canonical descent datum $$(M\otimes_A B, \id)$$에서 출발하면, $$N=M\otimes_A B$$ 위에서 $$\varphi_N=\id$$이므로 $$N^\varphi$$는 $$\{x\in M\otimes_A B\mid x\otimes 1=1\otimes x\}$$이다. [보조정리 3](#lem3)에 $$-\otimes_A M$$의 정확성 대신 $$M$$을 계수로 한 형태를 적용하면, 즉 sequence $$0 \rightarrow M \rightarrow M\otimes_A B \rightarrow M\otimes_A B\otimes_A B$$가 정확하므로 (이는 [보조정리 3](#lem3)의 정확한 sequence에 평탄한 $$-\otimes_A M$$ 대신 충실평탄 $$B$$로의 base change 논증을 그대로 반복하여 얻는다) $$N^\varphi=M$$이고, 따라서 한 합성은 항등과 자연동형이다.

반대 방향이 본질적인 부분이다. Descent datum $$(N, \varphi_N)$$에서 출발하여 $$M=N^\varphi$$라 두고, 자연스러운 $$B$$-가군 사상

$$\theta: M\otimes_A B \rightarrow N;\qquad m\otimes b\mapsto bm$$

이 동형임을 보여야 하며, 또 그 위에서 descent datum이 보존됨을 확인해야 한다. $$\theta$$가 동형임을 보이는 것은 충실평탄 $$\varphi$$ 덕분에 $$-\otimes_A B$$ 후에 확인하면 충분하다. ([명제 2](#prop2)) Base change $$\theta\otimes_A B: M\otimes_A B\otimes_A B \rightarrow N\otimes_A B=p_1^\ast N$$를 계산하기 위해, $$\varphi_N$$을 이용하여 $$N\otimes_A B=p_1^\ast N\cong p_2^\ast N=B\otimes_A N$$로 옮긴다.

핵심은 다음의 관찰이다. $$\varphi_N$$의 cocycle 조건은 $$M=N^\varphi$$의 정의와 결합하여, $$p_1^\ast N$$ 위에서 "$$\varphi_N$$으로 평행이동된 좌표"를 잡으면 $$N\otimes_A B$$가 $$M\otimes_A B\otimes_A B$$와 동일시됨을 함의한다. 구체적으로, $$B\otimes_A B$$를 밑환으로 보고 $$\psi=\varphi_N$$로 두면, cocycle 조건 $$p_{13}^\ast \psi=p_{23}^\ast \psi\circ p_{12}^\ast \psi$$는 정확히 $$(N\otimes_A B, p_1^\ast \psi)$$가 다시 $$B\otimes_A B$$에 대한 descent datum을 이루고 그 invariant 부분이 $$N$$ 자신이 되도록 한다. 따라서 base change된 $$\theta\otimes_A B$$는 [보조정리 3](#lem3)이 보장하는 동형

$$N^\varphi\otimes_A B\xrightarrow{\ \sim\ }\{x\in N\otimes_A B\mid p_1^\ast\varphi_N(x)=p_2^\ast \text{ 자명배치}\}\cong N$$

으로 귀착되어 전단사이다. 따라서 $$\theta$$가 base change 후 동형이고, 충실평탄성에 의해 $$\theta$$ 자신이 동형이다.

마지막으로 이 $$\theta$$가 canonical descent datum $$\id_{M\otimes_A B}$$을 주어진 $$\varphi_N$$으로 옮기는 것은, $$\theta$$의 정의가 $$\varphi_N$$의 좌표를 그대로 사용했다는 사실로부터 따라온다. 두 functor의 합성이 양쪽 모두 항등과 자연동형이므로 동치이다.

</details>

[정리 6](#thm6)은 충실평탄 사상을 따라 가군이 완전히 하강함을 말한다. $$B$$ 위의 가군 $$N$$에 $$B\otimes_A B$$ 위의 cocycle 동형 하나를 더하면, 그것은 유일한 $$A$$-가군 $$M$$의 base change이다. 이 정리의 직접적인 결과로, 가군의 여러 성질들이 충실평탄 base change에 대해 내려온다. 가령 $$M\otimes_A B$$가 유한생성 $$B$$-가군이면 $$M$$도 유한생성이고, $$M\otimes_A B$$가 finitely presented이면 $$M$$도 finitely presented이며, $$M\otimes_A B$$가 평탄 또는 projective이면 $$M$$ 역시 그러하다. 이들은 모두 해당 성질이 정확열로 표현되고 [명제 2](#prop2)가 그 정확성을 $$A$$ 위로 반영하기 때문이다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\varphi: A \rightarrow B$$가 충실평탄이고 $$M$$이 $$A$$-가군이라 하자. 그럼 $$M$$이 유한생성(각각 finitely presented, 평탄, locally free of finite rank)인 것은 $$M\otimes_A B$$가 $$B$$-가군으로서 유한생성(각각 finitely presented, 평탄, locally free of finite rank)인 것과 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 성질은 한쪽 방향이 base change에 대한 보존이므로 자명하고, 내려오는 방향만 본다. 유한생성의 경우, $$M\otimes_A B$$가 $$y_1,\ldots, y_n$$으로 생성된다 하면 각 $$y_i$$는 유한히 많은 $$m_{ij}\otimes b_{ij}$$의 합이므로, 그 $$m_{ij}$$들이 생성하는 유한생성 부분가군 $$M_0\subseteq M$$에 대해 $$M_0\otimes_A B \rightarrow M\otimes_A B$$가 전사이다. 그럼 $$(M/M_0)\otimes_A B=0$$이고 충실성에 의해 $$M/M_0=0$$이므로 $$M=M_0$$은 유한생성이다.

Finitely presented의 경우, $$M$$이 유한생성임은 위에서 얻었으므로 $$A^n \twoheadrightarrow M$$의 kernel $$K$$가 유한생성임을 보이면 된다. $$0 \rightarrow K \rightarrow A^n \rightarrow M \rightarrow 0$$을 base change하면 ($$B$$가 평탄) $$0 \rightarrow K\otimes_A B \rightarrow B^n \rightarrow M\otimes_A B \rightarrow 0$$이 정확하고, $$M\otimes_A B$$가 finitely presented이므로 $$K\otimes_A B$$는 유한생성이다. ([\[가환대수학\] §평탄성, ⁋따름정리 6](/ko/math/commutative_algebra/flatness#cor6) 이후의 finitely presented 논의) 따라서 위 유한생성 판정을 $$K$$에 적용하면 $$K$$도 유한생성이고 $$M$$은 finitely presented이다.

평탄의 경우, $$M$$이 평탄임을 보이려면 임의의 단사 $$A$$-가군 사상 $$M' \hookrightarrow M''$$에 대해 $$M'\otimes_A M \rightarrow M''\otimes_A M$$이 단사임을 보이면 된다. 이를 $$-\otimes_A B$$하면 ([명제 2](#prop2)로 단사성을 검사) $$M'\otimes_A M\otimes_A B \rightarrow M''\otimes_A M\otimes_A B$$인데, 이는 $$M\otimes_A B$$가 평탄 $$B$$-가군이고 $$M'\otimes_A B \rightarrow M''\otimes_A B$$가 단사이므로 ($$B$$ 평탄) 단사이다. 따라서 원래 사상도 단사이고 $$M$$은 평탄이다. Locally free of finite rank는 finitely presented이면서 평탄인 것과 동치이므로 ([\[가환대수학\] §평탄성, ⁋따름정리 6](/ko/math/commutative_algebra/flatness#cor6)) 앞의 두 경우로부터 따라온다.

</details>

## Fpqc 위상과 준연접층의 하강

지금까지의 affine 위의 결과를 일반적인 scheme 위로 옮기려면, 충실평탄 사상을 적절한 Grothendieck 위상의 덮개로 받아들여야 한다. 그 위상이 fpqc 위상이다. 이름은 *fidèlement plat quasi-compact*, 즉 충실평탄이며 quasi-compact라는 뜻이다.

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme $$X$$ 위의 morphism들의 모임 $$\{f_i: U_i \rightarrow X\}_{i\in I}$$이 *fpqc cover<sub>fpqc 덮개</sub>*라는 것은, 각 $$f_i$$가 평탄이고, 합 $$\coprod_i U_i \rightarrow X$$가 surjective이며, 각 affine open $$V\subseteq X$$가 유한히 많은 $$U_i$$의 affine open들 $$W_{ij}$$의 상으로 덮이는 quasi-compact 조건을 만족하는 것이다. 이러한 덮개들이 정의하는 $$\Sch$$ 위의 Grothendieck 위상을 *fpqc 위상*이라 부른다.

</div>

Fpqc 위상에서 한 affine scheme $$\Spec A$$를 덮는 가장 단순한 덮개는 충실평탄 ring homomorphism $$A \rightarrow B$$ 하나로 이루어진 $$\{\Spec B \rightarrow \Spec A\}$$이다. 이 경우 [정리 6](#thm6)이 곧바로 sheaf 조건의 형태로 다시 쓰인다. 우리는 준연접층이 이 위상에 대한 sheaf임을 주장한다. ([§준연접층, ⁋정의 8](/ko/math/scheme_theory/quasicoherent_sheaves#def8))

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9**</ins> 임의의 scheme $$X$$와 $$X$$ 위의 준연접층 $$\mathcal{F}$$에 대하여, presheaf

$$T\mapsto \Gamma(T, f^\ast \mathcal{F})\qquad (f: T \rightarrow X)$$

은 fpqc 위상에 대한 sheaf이다. 즉 임의의 fpqc cover $$\{T_i \rightarrow T\}$$에 대하여, sequence

$$\Gamma(T, f^\ast\mathcal{F}) \rightarrow \prod_i \Gamma(T_i, f_i^\ast\mathcal{F}) \rightrightarrows \prod_{i,j}\Gamma(T_i\times_T T_j, f_{ij}^\ast\mathcal{F})$$

는 정확하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 국소적이고 quasi-compact 조건 덕분에 유한 덮개로 환원되므로, $$T=\Spec A$$가 affine이고 덮개가 단일 충실평탄 사상 $$\{\Spec B \rightarrow \Spec A\}$$인 경우만 보이면 충분하다. 이 때 $$\mathcal{F}=\widetilde M$$인 $$A$$-가군 $$M$$이 있고 ([§준연접층, ⁋정리 9](/ko/math/scheme_theory/quasicoherent_sheaves#thm9)), pullback이 base change로 주어지므로 ([§준연접층, ⁋명제 18](/ko/math/scheme_theory/quasicoherent_sheaves#prop18)) 위 sequence는

$$M \rightarrow M\otimes_A B \rightrightarrows M\otimes_A B\otimes_A B$$

이다. 이는 [보조정리 3](#lem3)을 $$M$$을 계수로 일반화한 sequence

$$0 \rightarrow M \rightarrow M\otimes_A B \rightarrow M\otimes_A B\otimes_A B$$

의 정확성, 즉 [정리 6](#thm6)의 증명에서 사용한 사실에 다름 아니다. 두 사상 $$d^0, d^1$$의 equalizer가 $$M$$임이 곧 위 sheaf 조건이므로 결론을 얻는다.

</details>

[정리 9](#thm9)는 준연접층의 global section을 충실평탄 덮개 위에서 계산할 수 있게 해준다. 덮개 위의 section이 두 겹 겹침에서 일치하면 그것은 밑공간 위의 section에서 유일하게 온다는 것이다. 이로부터 준연접층 자체의 하강, 즉 정의 4의 sheaf 버전이 따라온다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> $$\{f_i: U_i \rightarrow X\}$$가 fpqc cover라 하자. 그럼 $$X$$ 위의 준연접층을 주는 것은, 각 $$U_i$$ 위의 준연접층 $$\mathcal{F}_i$$들과, $$U_i\times_X U_j$$ 위에서 cocycle 조건을 만족하는 동형사상 $$\varphi_{ij}: \operatorname{pr}_2^\ast \mathcal{F}_j\cong \operatorname{pr}_1^\ast \mathcal{F}_i$$들의 데이터를 주는 것과 동치이다. 즉 준연접층은 fpqc 위상에 대하여 *effective descent*를 가진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 국소적이므로 $$X=\Spec A$$이고 덮개가 단일 충실평탄 사상 $$\Spec B \rightarrow \Spec A$$인 경우로 환원된다. 이 때 $$U_i\times_X U_j$$는 $$\Spec(B\otimes_A B)$$이고, 주어진 데이터는 정확히 $$B$$-가군 $$N=\Gamma(\Spec B, \mathcal{F}_1)$$과 $$B\otimes_A B$$-가군 동형 $$\varphi_N$$의 cocycle 쌍, 즉 [정의 4](#def4)의 descent datum이다. 준연접층과 가군의 대응 ([§준연접층, ⁋정리 9](/ko/math/scheme_theory/quasicoherent_sheaves#thm9))과 pullback의 base change 해석 ([§준연접층, ⁋명제 18](/ko/math/scheme_theory/quasicoherent_sheaves#prop18)) 아래에서, 이 데이터는 $$\operatorname{Desc}(B/A)$$의 대상에 정확히 대응한다. 따라서 [정리 6](#thm6)에 의해 이는 유일한 $$A$$-가군 $$M$$, 즉 유일한 준연접층 $$\widetilde M$$으로부터 오며, 그 사상까지 동치이다.

일반적인 fpqc cover의 경우, quasi-compact 조건으로 유한 부분덮개를 잡고 그 disjoint union을 단일 affine 충실평탄 사상으로 만들어 위 affine 경우를 적용한 뒤, 결과들을 $$X$$의 affine open들 위에서 접합한다. 접합의 정합성은 [정리 9](#thm9)의 sheaf 성질이 보장한다.

</details>

[정리 10](#thm10)의 "effective"라는 표현은 descent datum이 단지 형식적으로 존재하는 데 그치지 않고 실제로 어떤 전역 대상을 산출함을 강조한다. 일반적인 Grothendieck 위상에서는 sheaf 조건만으로 충분하지 않고 데이터가 실제 대상을 이루는지가 별개의 문제인데, 준연접층의 경우 [정리 6](#thm6)이 그 실효성까지 보장하는 것이다.

## 사상과 성질의 하강

마지막으로, 가군과 준연접층을 넘어 사상 자체와 그 성질들이 fpqc base change에 대해 어떻게 하강하는지를 본다. Fpqc cover $$\{U_i \rightarrow X\}$$ 위에서 정의된 $$X$$-scheme 데이터가 cocycle 조건을 만족하면 $$X$$ 위의 scheme으로 모여야 하는데, 이는 가군의 경우와 달리 항상 effective인 것은 아니다. 그러나 덮개 위의 대상이 충분히 affine에 가까우면 effective하다.

<div class="proposition" markdown="1">

<ins id="thm11">**정리 11**</ins> $$\{U_i \rightarrow X\}$$가 fpqc cover이고, 각 $$U_i$$ 위에서 affine morphism $$V_i \rightarrow U_i$$들과 $$U_i\times_X U_j$$ 위의 cocycle 동형 데이터가 주어졌다 하자. 그럼 이 데이터는 $$X$$ 위의 affine morphism $$V \rightarrow X$$로부터 유일하게 base change되어 온다. 즉 affine scheme은 fpqc 위상에 대하여 effective descent를 가진다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Affine morphism $$V_i \rightarrow U_i$$은 $$U_i$$ 위의 준연접 $$\mathcal{O}_{U_i}$$-대수층 $$\mathcal{A}_i=(g_i)_\ast \mathcal{O}_{V_i}$$에 의해 $$V_i=\operatorname{\mathbf{Spec}}\mathcal{A}_i$$로 복원된다. 주어진 cocycle 데이터는 $$\mathcal{A}_i$$들 위의 준연접층 동형으로서 대수 구조를 보존하는 것이므로, [정리 10](#thm10)에 의해 $$X$$ 위의 준연접 $$\mathcal{O}_X$$-대수층 $$\mathcal{A}$$로 유일하게 하강한다. 대수 구조의 하강은 곱셈 사상 $$\mathcal{A}_i\otimes \mathcal{A}_i \rightarrow \mathcal{A}_i$$ 또한 [정리 10](#thm10)의 동치 아래에서 함께 내려오기 때문이다. 그럼 $$V=\operatorname{\mathbf{Spec}}\mathcal{A} \rightarrow X$$가 원하는 affine morphism이며, 그 base change가 주어진 $$V_i \rightarrow U_i$$들을 회복함은 affine morphism과 준연접 대수층의 대응이 base change와 호환되기 때문이다.

</details>

[정리 11](#thm11)은 affine 또는 더 일반적으로 quasi-affine scheme이 fpqc 하강에 대해 effective임을 말하며, 이것이 표현가능성 이론과 만나는 지점이다. 어떤 함자 $$F:\Sch^\op \rightarrow \Set$$이 fpqc sheaf이고, 적절한 fpqc cover 위에서 representable이며 그 위의 데이터가 affine으로 하강한다면, $$F$$ 자신이 어떤 scheme에 의해 representable이라고 결론지을 수 있다. ([§점함자, ⁋정의 5](/ko/math/scheme_theory/functor_of_points#def5)) 즉 하강은 함자적으로 정의된 moduli 문제가 실제 scheme을 산출하는지를 검증하는 표준 도구이다. 실제로 [§점함자](/ko/math/scheme_theory/functor_of_points)에서 다룬 fiber product의 점함자 기술 ([§점함자, ⁋명제 13](/ko/math/scheme_theory/functor_of_points#prop13))처럼, 점별로 정의된 함자의 representability는 국소적 representability와 하강의 결합으로 환원된다.

성질들의 하강 또한 같은 원리로 정리된다. Scheme morphism $$f: X \rightarrow Y$$의 여러 성질은 fpqc-local on the base이다. 즉 어떤 fpqc cover $$\{Y_i \rightarrow Y\}$$를 잡아 각 base change $$f_i: X\times_Y Y_i \rightarrow Y_i$$가 그 성질을 가지면, $$f$$ 자신도 그 성질을 가진다.

<div class="proposition" markdown="1">

<ins id="prop12">**명제 12**</ins> $$\{Y_i \rightarrow Y\}$$를 fpqc cover라 하고 $$f: X \rightarrow Y$$를 scheme morphism이라 하자. 그럼 $$f$$가 다음 성질들 가운데 하나를 가지는 것은, 각 base change $$f_i: X\times_Y Y_i \rightarrow Y_i$$가 그 성질을 가지는 것과 동치이다: 평탄, 충실평탄, 그리고 affine, locally of finite type, locally of finite presentation, 그리고 surjective.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 성질이 base change에 대해 보존됨은 표준적이므로 (평탄성의 경우 [§평탄사상, ⁋명제 12](/ko/math/scheme_theory/flat_morphisms#prop12)), fpqc cover 위에서 성립하면 원래 사상에서도 성립함만 보이면 된다. 문제가 $$Y$$ 위에서 국소적이고 quasi-compact 조건으로 유한 덮개로 환원되므로, $$Y=\Spec A$$, 덮개가 단일 충실평탄 $$\Spec A' \rightarrow \Spec A$$인 경우만 본다.

평탄성의 경우, 이는 affine 위에서 $$X$$를 덮는 각 $$\Spec B \rightarrow \Spec A$$에 대한 $$B$$의 $$A$$-평탄성으로 판정된다. $$B\otimes_A A'$$가 $$A'$$-평탄이라 가정하면, $$A \rightarrow A'$$가 충실평탄이므로 임의의 단사 $$A$$-가군 사상 $$M' \hookrightarrow M''$$에 대하여 $$(M'\otimes_A B \rightarrow M''\otimes_A B)\otimes_A A'$$이 단사이고 ($$B\otimes_A A'$$ 평탄), [명제 2](#prop2)로 단사성을 $$A$$ 위로 반영하면 $$M'\otimes_A B \rightarrow M''\otimes_A B$$가 단사이므로 $$B$$는 $$A$$-평탄이다. 충실평탄성은 평탄성에 surjective를 더한 것이고, surjective는 $$\coprod (X\times_Y Y_i) \rightarrow \coprod Y_i \rightarrow Y$$의 합성이 전사임과 $$\coprod Y_i \rightarrow Y$$가 전사임으로부터 $$X \rightarrow Y$$의 전사가 따라오므로 성립한다.

Affine의 경우, $$X\times_A A'=\Spec C'$$가 affine이라 하자. 그럼 $$\mathcal{O}_X$$의 pushforward가 준연접 대수층임을 [정리 10](#thm10)으로 $$A'$$에서 $$A$$로 하강시켜 얻으며, [정리 11](#thm11)의 논증으로 $$X=\operatorname{\mathbf{Spec}}$$ of 어떤 준연접 $$A$$-대수, 즉 affine임을 안다. Locally of finite type과 locally of finite presentation은 affine 위에서 각각 $$B$$가 $$A$$ 위에서 유한생성 대수, finitely presented 대수인 조건이며, [명제 7](#prop7)의 유한생성·finitely presented 하강을 대수 생성원과 관계식에 적용하여 $$A'$$에서 $$A$$로 내려온다.

</details>

[명제 12](#prop12)는 충실평탄 하강이 단지 가군이나 sheaf의 수준에 머물지 않고 사상의 기하학적 성질 전반을 지배함을 보여준다. 실용적으로 이는 어떤 성질을 검증할 때 base를 충실평탄하게 확장하여 더 다루기 쉬운 상황으로 옮긴 뒤, 거기에서 성질을 확인하고 다시 내려보내는 전략을 정당화한다. 가령 base change 후 $$Y$$가 algebraically closed field 위로 가거나 strictly Henselian local ring 위로 가는 경우처럼, 충실평탄 덮개를 통해 문제를 표준적인 형태로 환원하는 것은 scheme 이론 전반에서 반복되는 기법이다.

---

**참고문헌**

**[Vak]** R. Vakil, *The rising sea: Foundations of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).  
**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*. Mathematical Surveys and Monographs. American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*. Available [online](https://stacks.math.columbia.edu/).  
**[BLR]** S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron models*. Ergebnisse der Mathematik. Springer, 1990.  
**[EGA]** A. Grothendieck, J. Dieudonné, *Éléments de géométrie algébrique IV*. Publications mathématiques de l'IHÉS, 1964–1967.
</content>
</invoke>
