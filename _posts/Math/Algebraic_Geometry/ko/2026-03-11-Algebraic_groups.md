---
title: "대수적 군과 그 작용"
excerpt: "대수적 군, 작용, weight decomposition, 그리고 표현 이론"

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/algebraic_groups
sidebar: 
    nav: "algebraic_geometry-ko"

header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Algebraic_Groups.png
    overlay_filter: 0.5

date: 2026-03-11
last_modified_at: 2026-03-11
weight: 1000

---

## 대수적 군

우리는 이미 특정한 대상이 다른 대상 위에 작용하는 많은 예시들을 알고 있다. 

대수기하학에서 *group*의 개념은 단순히 집합 위에 정의된 연산 구조가 아니라, 대수다양체로서의 기하학적 구조와 군으로서의 대수적 구조가 조화를 이루는 대상이다. 이번 글에서 우리는 대수적 군의 정의와 기본 성질을 살펴보고, 대수다양체 위로의 작용을 정의한 후, torus action과 representation theory로의 연결고리를 확립한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> *대수적 군<sub>algebraic group</sub>* $$G$$는 다음 조건들을 만족하는 대수다양체이다:

1. $$G$$는 group 구조를 갖는다.
2. 곱셈사상 $$m: G \times G \to G$$와 역원사상 $$i: G \to G$$가 모두 morphism of varieties이다.

</div>

즉, 대수적 군은 대수다양체인 동시에 군이며, 두 구조가 morphism이라는 기하학적 조건을 통해 서로 호환된다. 

<div class="example" markdown="1">

<ins id="ex2">**예시 2**</ins> 가장 기본적인 예시들은 다음과 같다:

1. **일반선형군**: $$\GL(n, \mathbb{C}) = \{A \in M_{n \times n}(\mathbb{C}) \mid \det A \ne 0\}$$는 $$\mathbb{C}^{n^2}$$의 열린부분다양체로서 대수적 군의 구조를 갖는다.
2. **특수선형군**: $$\SL(n, \mathbb{C}) = \{A \in \GL(n, \mathbb{C}) \mid \det A = 1\}$$는 $$\GL(n, \mathbb{C})$$의 닫힌 부분군으로서 대수적 군이다.
3. **가환군**: $$\mathbb{G}_a = \mathbb{C}$$ (덧셈)과 $$\mathbb{G}_m = \mathbb{C}^\ast$$ (곱셈)은 모두 1차원 대수적 군이다.

</div>

대수적 군 중에서 특히 중요한 역할을 하는 것은 *affine algebraic group*이다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> 대수적 군 $$G$$가 *affine algebraic group*라는 것은 $$G$$가 affine variety인 것이다. 이를 *linear algebraic group*이라고도 부른다.

</div>

Affine algebraic group의 중요성은 모든 affine algebraic group이 어떤 $$\GL(n, \mathbb{C})$$의 닫힌 부분군으로 실현된다는 사실로부터 온다. 이는 affine variety가 좌표환을 통해 완전히 결정된다는 사실과 밀접하게 연관된다.

### 대수적 토러스

대수적 토러스는 toric geometry의 핵심적인 대상이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> *대수적 토러스<sub>algebraic torus</sub>*는 $$\mathbb{G}_m = \mathbb{C}^\ast$$의 유한개 직적분과 동형인 대수적 군이다. 즉,

$$T \cong (\mathbb{C}^\ast)^n$$

을 만족하는 $$n \ge 1$$이 존재하는 대수적 군이다.

</div>

Toric geometry에서 우리는 격자 $$N \cong \mathbb{Z}^n$$과 그 쌍대격자 $$M = \Hom(N, \mathbb{Z})$$를 사용하여 대수적 토러스를

$$T_N = N \otimes_\mathbb{Z} \mathbb{C}^\ast$$

로 표현한다. 이 표현은 torus의 좌표를 격자의 basis $$e_1, \ldots, e_n$$을 통해

$$t = e_1 \otimes t_1 + \cdots + e_n \otimes t_n$$

로 parametrize할 수 있게 해주며, 여기서 $$(t_1, \ldots, t_n) \in (\mathbb{C}^\ast)^n$$이다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 격자 $$N$$과 그 쌍대격자 $$M = \Hom(N, \mathbb{Z})$$에 대하여, 각 $$m \in M$$에 대응하는 torus $$T_N = N \otimes \mathbb{C}^\ast$$의 *character* $$\chi^m: T_N \to \mathbb{C}^\ast$$를

$$\chi^m(u \otimes c) = c^{m(u)}$$

으로 정의한다. Basis 표현 $$t = \sum_i e_i \otimes t_i$$에서 이는

$$\chi^m(t) = \chi^m\left(\sum_i e_i \otimes t_i\right) = \prod_i t_i^{m(e_i)}$$

으로 주어진다.

</div>

Character의 정의로부터 $$\chi^m$$이 group homomorphism임을 쉽게 확인할 수 있다:

$$\chi^m((u \otimes c) + (u' \otimes c')) = \chi^m((u+u') \otimes (cc')) = (cc')^{m(u+u')} = c^{m(u)} (c')^{m(u')} = \chi^m(u \otimes c) \chi^m(u' \otimes c').$$

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> 대수적 토러스 $$T_N$$의 좌표환은 $$\mathbb{C}[M]$$과 동형이다.

</div>

<details class="proof" markdown="1">
<summary>증명</summary>

정의 5에서 정의한 character들 $$\chi^m$$ ($$m \in M$$)의 polynomial ring이 바로 $$\mathbb{C}[M]$$이며, 이는 $$T_N$$의 정칙함수환과 일치한다.

</details>

이로부터 $$T_N \cong \Spec(\mathbb{C}[M])$$임을 안다. 이 사실은 torus action을 coordinate ring 위의 comodule structure로 정의하는 데 핵심적인 역할을 한다.

## 대수적 군의 작용

이제 대수적 군이 대수다양체 위에 작용하는 방식을 정의한다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 대수적 군 $$G$$의 대수다양체 $$X$$ 위로의 *작용<sub>action</sub>*이란 morphism

$$\alpha: G \times X \to X$$

으로서, 다음 조건들을 만족하는 것이다:

1. $$\alpha(e, x) = x$$ for all $$x \in X$$ (항등원 보존)
2. $$\alpha(g, \alpha(h, x)) = \alpha(gh, x)$$ for all $$g, h \in G$$, $$x \in X$$ (결합법칙)

</div>

작용이 주어지면 우리는 각 점의 *orbit*과 *stabilizer*를 정의할 수 있다.

<div class="definition" markdown="1">

<ins id="def7">**정의 7**</ins> $$G$$가 $$X$$ 위에 작용할 때, 점 $$x \in X$$의

- *Orbit*: $$G \cdot x = \{g \cdot x \mid g \in G\} \subseteq X$$
- *Stabilizer*: $$G_x = \{g \in G \mid g \cdot x = x\} \le G$$
- *Fixed point set*: $$X^G = \{x \in X \mid g \cdot x = x \text{ for all } g \in G\}$$

</div>

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> Torus $$T_N$$이 affine toric variety $$U_\sigma = \Spec(\mathbb{C}[S_\sigma])$$ 위에 작용하는 경우를 생각하자. 이 작용은 coordinate ring $$\mathbb{C}[S_\sigma]$$ 위의 comodule structure

$$\rho: \mathbb{C}[S_\sigma] \to \mathbb{C}[S_\sigma] \otimes_\mathbb{C} \mathbb{C}[M], \qquad \chi^u \mapsto \chi^u \otimes \chi^u$$

를 통해 정의된다. $$\Spec$$이 contravariant functor이므로, 이 comodule structure는 $$U_\sigma$$ 위에 $$T_N$$-action을 유도한다.

</div>

### Quotient Varieties

작용이 주어진 대수다양체에서 우리는 종종 *quotient variety*를 구성하고자 한다. 그러나 이는 일반적으로 어려운 문제이며, 모든 작용에 대해 quotient variety가 존재하는 것은 아니다.

<div class="definition" markdown="1">

<ins id="def9">**정의 9**</ins> $$G$$가 $$X$$ 위에 작용할 때, *geometric quotient*란 다음 조건을 만족하는 대수다양체 $$X/G$$와 morphism $$\pi: X \to X/G$$이다:

1. $$\pi$$는 상수함수가 $$G$$-invariant function들로 제한됨
2. $$\pi$$의 fiber들이 정확히 $$G$$-orbit들과 일치함

</div>

Toric geometry에서 닫힌 원뿔 $$\sigma$$에 대해 $$U_\sigma$$의 torus action에 대한 quotient는 toric variety의 기하학을 이해하는 데 핵심적이다.

## Torus Action과 Weight Decomposition

대수적 토러스 $$T_N$$의 작용은 특별한 성질을 갖는데, 바로 *weight decomposition*이 존재한다는 것이다. 이에 대한 자세한 내용은 [\[리 군\] §원환면의 작용](/ko/math/lie_theory/torus_action)에서 다루고 있으므로, 여기서는 핵심적인 아이디어만 간단히 요약한다.

<div class="proposition" markdown="1">

<ins id="prop10">**명제 10**</ins> Torus $$T_N$$이 affine variety $$X = \Spec(A)$$ 위에 작용하면, coordinate ring $$A$$는 weight space들로 분해된다:

$$A = \bigoplus_{\lambda \in \Lambda} A_\lambda$$

여기서 $$\Lambda \subseteq M$$은 weight들의 집합이고, 각 $$A_\lambda$$는

$$A_\lambda = \{f \in A \mid t \cdot f = \chi^\lambda(t) f \text{ for all } t \in T_N\}$$

으로 정의된다.

</div>

이 weight decomposition은 torus action이 coordinate ring의 grading을 통해 완전히 결정된다는 것을 보여준다. 특히 toric variety $$U_\sigma$$의 경우, 이 grading은 semigroup $$S_\sigma \subseteq M$$에 의해 주어진다:

$$\mathbb{C}[S_\sigma] = \bigoplus_{u \in S_\sigma} \mathbb{C} \cdot \chi^u$$

이 decomposition에서 각 $$\mathbb{C} \cdot \chi^u$$는 weight $$u$$를 갖는 1차원 weight space이다.

<div class="remark" markdown="1">

Weight decomposition의 존재성, 그 각 weight space의 구조, 그리고 이를 통한 torus action의 완전한 분류에 대해서는 [\[리 군\] §원환면의 작용, §§Weight Decomposition](/ko/math/lie_theory/torus_action#weight-decomposition)을 참조하라.

</div>

## 대수적 군의 표현

이제 우리는 대수적 군의 표현 이론을 간단히 소개한다.

<div class="definition" markdown="1">

<ins id="def11">**정의 11**</ins> 대수적 군 $$G$$의 *표현<sub>representation</sub>*이란 유한차원 벡터공간 $$V$$와 group homomorphism

$$\rho: G \to \GL(V)$$

으로서, $$G \times V \to V$$가 morphism인 것이다.

</div>

표현 이론의 핵심 도구 중 하나는 *character*이다. (이는 앞서 정의한 torus의 character [정의 5](#def5)와 다른 개념이다. Torus의 character는 torus에서 $$\mathbb{C}^\ast$$로의 group homomorphism이지만, 표현의 character는 group에서 $$\mathbb{C}$$로의 함수이다.)

<div class="definition" markdown="1">

<ins id="def12">**정의 12**</ins> 표현 $$\rho: G \to \GL(V)$$의 *character<sub>지표</sub>* $$\chi_\rho: G \to \mathbb{C}$$는

$$\chi_\rho(g) = \tr(\rho(g))$$

으로 정의된다.

</div>

Character theory에 대한 자세한 내용은 [\[표현론\] §표현의 지표](/ko/math/representation_theory/character_theory)를 참조하라. 특히 character의 직교성, irreducible representation의 분류, 그리고 character table의 구성 등은 표현론의 핵심 주제이다.

### Comodule Structure

대수기하학적 관점에서 표현은 comodule structure로 재해석될 수 있다. 이는 torus action을 이해하는 데 있어 핵심적인 관점이다.

<div class="definition" markdown="1">

<ins id="def13">**정의 13**</ins> $$G$$가 affine algebraic group이고 그 coordinate ring이 $$\mathbb{C}[G]$$일 때, 벡터공간 $$V$$ 위의 *comodule structure*란 linear map

$$\rho: V \to V \otimes_\mathbb{C} \mathbb{C}[G]$$

로서, 다음 다이어그램들이 가환인 것이다:

1. (Coassociativity)

   $$\begin{CD}
   V @>\rho>> V \otimes \mathbb{C}[G] \\
   @V\rho VV @VV\id \otimes \Delta V \\
   V \otimes \mathbb{C}[G] @>>\rho \otimes \id> V \otimes \mathbb{C}[G] \otimes \mathbb{C}[G]
   \end{CD}$$

2. (Counit)

   $$\begin{CD}
   V @>\rho>> V \otimes \mathbb{C}[G] \\
   @V\id VV @VV\id \otimes \epsilon V \\
   V @= V \otimes \mathbb{C}
   \end{CD}$$

</div>

여기서 $$\Delta: \mathbb{C}[G] \to \mathbb{C}[G] \otimes \mathbb{C}[G]$$는 $$G$$의 곱셈으로부터 유도되는 comultiplication이고, $$\epsilon: \mathbb{C}[G] \to \mathbb{C}$$는 항등원으로부터 유도되는 counit이다.

<div class="proposition" markdown="1">

<ins id="prop14">**명제 14**</ins> Affine algebraic group $$G$$의 표현 $$\rho: G \to \GL(V)$$는 $$V$$ 위의 comodule structure와 일대일 대응한다.

</div>

이 대응은 $$\Spec$$의 contravariance를 통해 이해할 수 있다. $$G$$-action on $$V$$는 $$\Spec(V^\ast)$$ 위에 $$G$$-action을 주는 것과 같고, 이는 coordinate ring $$V^\ast$$ 위에 comodule structure를 주는 것과 동등하다.

### Torus의 Character

Torus $$T_N$$의 경우, 그 표현은 특히 단순한 형태를 갖는다.

<div class="proposition" markdown="1">

<ins id="prop15">**명제 15**</ins> Torus $$T_N$$의 임의의 표현 $$V$$는 1차원 표현들의 직합으로 분해된다:

$$V = \bigoplus_{\lambda \in \Lambda} V_\lambda$$

여기서 각 $$V_\lambda$$는 character $$\chi^\lambda: T_N \to \mathbb{C}^\ast$$에 대하여 $$t \cdot v = \chi^\lambda(t) v$$로 작용하는 weight space이다.

</div>

이는 torus action이 완전히 diagonalizable하다는 것을 의미하며, 이 성질이 toric geometry에서 torus action이 다루기 쉬운 이유이다.

---

**참고문헌**

**[Spr]** T. A. Springer, *Linear Algebraic Groups*, Birkhäuser, 1998.  
**[Hum]** J. E. Humphreys, *Linear Algebraic Groups*, Springer, 1975.  
**[Mil]** J. S. Milne, *Algebraic Groups*, Cambridge University Press, 2017.
