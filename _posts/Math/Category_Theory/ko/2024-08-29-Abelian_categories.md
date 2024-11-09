---

title: "아벨 카테고리"
excerpt: "아벨 카테고리"

categories: [Math / Category Theory]
permalink: /ko/math/category_theory/abelian_categories
header:
    overlay_image: /assets/images/Math/Category_Theory/Abelian_categories.png
    overlay_filter: 0.5
sidebar: 
    nav: "category_theory-ko"

date: 2022-12-21
last_modified_at: 2022-12-21
weight: 9

---

이번 글에서 우리는 abelian category의 개념과 chain complex, exact sequence의 개념을 정의한다. 

## Additive category

Abelian category를 정의하기 위해서는 우선 additive category를 정의해야 한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Category $\mathcal{A}$가 *$\Ab$-category*라는 것은 $\Hom_\mathcal{C}(A,B)$가 모두 abelian group의 구조를 갖고 있으며, 이 때 $(\Hom_\mathcal{C}(A,B),+)$가 합성에 대한 분배법칙을 만족하는 것이다. 즉, 임의의 $g_1,g_2\in\Hom_\mathcal{C}(B,C)$와, 임의의 $f:A\rightarrow B$ 혹은 $h:C\rightarrow D$에 대하여

$$(g_1+g_2)\circ f=g_1\circ f+g_2\circ f,\qquad h\circ(g_1+g_2)=h\circ g_1+h\circ g_2$$

이 모두 성립하는 것이다. Zero object $0$을 가지고, 임의의 두 object에 대해 이들의 곱이 존재하는 $\Ab$-category를 *additive category<sub>덧셈 카테고리</sub>*라 부른다.

</div>

두 additive category $\mathcal{A},\mathcal{B}$ 사이의 functor $F:\mathcal{A}\rightarrow\mathcal{B}$가 *additive functor<sub>덧셈함자</sub>*라는 것은 $F$가 abelian group $\Hom\_\mathcal{A}(A,B)$에서 $\Hom\_\mathcal{B}(F(A),F(B))$ 사이의 group homomorphism을 유도하는 것이다.

Additive category에서는 임의의 $A,B\in\obj(\mathcal{A})$에 대하여, *zero map<sub>영사상</sub>* $0\_{AB}:A\rightarrow B$가 $A\rightarrow 0\rightarrow B$로 정의된다. 이렇게 정의한 zero map은 물론 abelian group $\Hom\_\mathcal{A}(A,B)$의 덧셈에 대한 항등원이 된다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 additive category $\mathcal{A}$와 두 대상 $A,B\in\obj(\mathcal{A})$에 대하여, 위에서 정의한 zero map $0_{AB}$는 $\Hom\_\mathcal{A}(A,B)$의 덧셈에 대한 항등원이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

Zero object $0$에서 $B$로의 morphism $0\_{0B}$가 유일하게 존재한다. 따라서 $0\_{0B}+0\_{0B}=0\_{0B}$가 성립한다. 이제 주어진 명제는 다음의 식

$$0_{AB}+0_{AB}=0_{0B}\circ0_{A0}+0_{0B}\circ0_{A0}=(0_{0B}+0_{0B})\circ 0_{A0}=0_{0B}\circ 0_{A0}=0_{AB}$$

으로부터 자명하다.

</details>

## Abelian category

이제 abelian category를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> Additive category $\mathcal{A}$가 *abelian category<sub>아벨 카테고리</sub>*라는 것은 다음 조건들이 추가로 성립하는 것이다.

1. 임의의 homomorphism이 kernel과 cokernel을 갖는다.
2. 임의의 monomorphism $f$는 $\coker f$의 kernel과 같다.
3. 임의의 epimorphism $f$는 $\ker f$의 cokernel과 같다.

</div>

Additive category $\mathcal{A}$의 임의의 morphism $f:A \rightarrow B$의 kernel은 $0:A \rightarrow B$와의 equalizer $\Eq(f,0)$으로 정의되며, 비슷하게 $f$의 cokernel은 $0$과의 coequalizer $\CoEq(f,0)$으로 정의된다. 

특히, 이러한 상황에서는 다음의 exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C$$

가 주어졌을 때 $A$를 $B \rightarrow C$의 kernel과 동일시할 수 있고, 또 다음의 exact sequence

$$A \rightarrow B \rightarrow C \rightarrow 0$$

이 주어졌을 때 $C$를 $A \rightarrow B$의 cokernel과 동일시할 수 있다. Abelian category에서는 임의의 homomorphism $f:A\rightarrow B$에 대해 $f$의 kernel $i:\ker f\rightarrow A$와 cokernel $p:B\rightarrow \coker f$가 존재한다. 

임의의 abelian category $\mathcal{A}$에서, $f$의 *image*는 다음의 morphism

$$\ker(\coker f)\rightarrow\coker f$$

으로 정의된다. 비슷하게, $f$의 *coimage*는 다음의 morphism

$$\coim(f)=\coker(\ker(f))$$

으로 정의한다.

일반적인 abelian category에서, monomorphism $f:A\rightarrow B$가 주어진다면 $\coker f$를 *quotient object*라 부르고 $B\rightarrow B/A$, 혹은 더 간단히 $B/A$라 표기한다. 

## 사슬 복합체

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> Additive category $\mathcal{A}$에서 정의된 다음의 데이터를 생각하자.

- 대상들의 모임 $(A\_n)\_{n\in \mathbb{Z}}$,
- morphism들의 모임 $(d_n:A_n \rightarrow A\_{n-1})_{n\in \mathbb{Z}}$

만일 이들 데이터가 조건 $d_n\circ d_{n-1}=0$을 만족한다면, 이를 *chain complex<sub>사슬복합체</sub>*라 부르고 $A_\bullet$으로 적는다. 

</div>

한편, chain complex $A_\bullet$, $B_\bullet$ 사이의 morphism을 *chain map*이라 부르며, 이는 조건 $d_n^B\circ f_n=f_{n-1}\circ d_n^A$를 만족하는 morphism들의 모임 $(f_n: A_n \rightarrow B_n)_{n\in \mathbb{Z}}$으로 주어진다. 이를 통해 chain complex들의 category $\Ch(\mathcal{A})$를 정의할 수 있다.

$\mathcal{A}$가 abelian category였다면 이를 조금 더 자세히 살펴볼 수 있다. 이러한 상황에서 chain complex를 다룰 때 흔히 사용하는 이름과 표기를 고정하자. 우선, 각각의 $d_n$들은 문맥에 따라 *differential* 혹은 *boundary map*이라 부른다. 

이들의 kernel과 image를 각각

$$Z_n=\ker(d_{n-1}),\qquad B_n=\im(d_n)$$

으로 표기하며, 이들의 원소들은 각각 *$n$-cycle*과 *$n$-boundary*라 부른다. $C_n$의 원소는 *$n$-chain*이라 부른다. 어렵지 않게 다음의 monomorphism들

$$Z_n \hookrightarrow B_n \hookrightarrow C_n$$

이 존재함을 확인할 수 있으며, 이 때 cokernel $Z_n/B_n$을 $A_\bullet$의 *$n$-th homology*라 부르고 $H_n(A_\bullet)$ 혹은 간단히 $H_n(A)$로 적는다. 

$\mathcal{A}^\op$에서의 chain complex는 *cochain complex<sub>공사슬복합체</sub>*라 부른다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 임의의 chain complex $A_\bullet$이 주어졌다 하자. 그럼

$$\cdots \rightarrow A_{n+1}\overset{d_{n+1}}{\longrightarrow}A_n\overset{d_n}{\longrightarrow}A_{n-1}\rightarrow\cdots$$

이 $A_n$에서 *exact*라는 것은 위의 monomorphism $Z_n \rightarrow B_n$이 isomorphism인 것이다. 모든 곳에서 exact인 chain complex를 *exact sequence*라 부른다.

</div>

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> 다음의 chain complex

$$\cdots 0 \rightarrow 0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0 \rightarrow 0 \rightarrow \cdots$$

을 *short exact sequence<sub>짧은 완전열</sub>*이라 부르고, 이를 간단하게

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

으로 적는다.

</div>

Additive functor $F:\mathcal{A}\rightarrow \mathcal{B}$가 주어졌다 하자. 그럼 $\mathcal{A}$에서 정의된 임의의 chain complex $A_\bullet$에 대하여, 다음의 데이터

$$\cdots \rightarrow F(A_{n+1}) \overset{F(d_{n+1})}{\longrightarrow} F(A_n) \overset{F(d_n)}{\longrightarrow} F(A_{n-1})\rightarrow\cdots$$

가 chain complex가 된다는 것을 쉽게 확인할 수 있다. 즉 additive functor $F$는 functor $\Ch(\mathcal{A})\rightarrow \Ch(\mathcal{B})$를 유도한다. 그러나 일반적인 functor에 대하여, 원래의 chain complex $A_\bullet$이 exact라는 것이 위와 같이 얻어진 새로운 complex $F(A_\bullet)$가 exact라는 것을 보장해주지는 않는다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> Additive functor $F: \mathcal{A} \rightarrow \mathcal{B}$가 *left exact*인 것은 임의의 short exact sequence

$$0 \rightarrow A \rightarrow B \rightarrow C \rightarrow 0$$

에 대하여 다음의 sequence

$$0 \rightarrow F(A) \rightarrow F(B) \rightarrow F(C)$$

가 exact인 것이다. 비슷하게 $F$가 *right exact*인 것은 위와 같이 임의의 short exact sequence가 주어졌을 때, 다음의 sequence

$$A \rightarrow B \rightarrow C \rightarrow 0$$

이 exact인 것이다. Left exact인 동시에 right exact인 functor를 *exact functor*라 부른다.

</div>

즉, kernel을 보존하는 additive functor를 left exact functor라 부르고, cokernel을 보존하는 functor를 right exact functor라 부른다. 그럼 특히 left adjoint functor는 right exact이고, right adjoint functor는 left exact임을 확인할 수 있다.

$F$가 contravariant였더라도 위의 정의와 마찬가지로 left exactness와 right exactness를 정의할 수 있다. 

## Freyd-Mitchell embedding theorem

한편, 앞서 살펴본 것처럼 abelian category에서는 kernel, cokernel, image와 quotient 등이 모두 정의된다. 이로부터 $\lMod{A}$에서의 정리들을 임의의 abelian category로 옮겨올 수 있다. 가령 first isomorphism theorem을 임의의 abelian category의 언어로 바꾸어 쓰자면, 

> 임의의 abelian category $\mathcal{A}$의 morphism $f:A\rightarrow B$가 주어졌다 하자. 그럼 $A/\ker f\cong \im f$가 성립한다.

와 같이 적을 수 있으며, 좌변은 $i:\ker f\rightarrow A$로부터 얻어지는 quotient object가 된다. 이러한 종류의 정리들은 모두 abelian category로 올릴 수 있고, 증명 또한 kernel과 cokernel의 universal property 등만 이용하여 진행할 수 있으나 그 증명은 다소 복잡하다. 

따라서, 일반적으로는 이러한 정리들을 일일히 보이는 대신 다음 정리를 사용한다. 

<div class="proposition" markdown="1">

<ins id="thm8">**정리 8 (Freyd-Mitchell embedding theorem)**</ins> 임의의 small abelian category $\mathcal{A}$에 대하여, 적당한 ring $A$와 fully faithful, exact functor $F:\mathcal{A}\rightarrow\lMod{A}$이 존재한다.

</div>

따라서, 임의의 abelian category의 대상들을 $A$-module로 생각하고, 이들의 morphism을 $A$-linear map으로 생각한 후 계산을 해도 무관하다.

---

**참고문헌**

**[Wei]** C.A. Weibel. *An Introduction to Homological Algebra*. Cambridge Studies in Advanced Mathematics. Cambridge University Press, 1995.  
**[Vak]** R. Vakil, *The rising sea: foundations of algebraic geometry*. 2015. Preprint. [링크](http://math.stanford.edu/~vakil/216blog/FOAGnov1817public.pdf)

---

[^1]: 이들이 실제로 집합이라는 것은 $B^A$가 집합이라는 사실로부터 자명하다. 따라서, 해당 예시에서 다룬 대수적 구조들의 카테고리는 모두 국소적으로 작은 카테고리이다. 