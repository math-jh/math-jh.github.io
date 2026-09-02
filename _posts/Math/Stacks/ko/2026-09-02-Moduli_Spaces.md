---
title: "모듈라이 공간"
description: "Moduli 문제를 functor·stack으로 정식화하고, universal family를 갖는 fine moduli space의 representability와 automorphism obstruction, 그리고 coarse moduli space와 moduli stack의 역할을 다룬다."
excerpt: "Moduli functors, fine vs coarse moduli spaces, and why the moduli stack is the right object"

categories: [Math / Stacks]
permalink: /ko/math/stacks/moduli_spaces
sidebar: 
    nav: "stacks-ko"

date: 2026-09-02
weight: 4

---

이제 우리는 우리의 원래 관심사였던 moduli problem을 살펴본다. 앞서 살펴본 것과 같이, moduli problem은 functor 

$$F:\Sch^\op\rightarrow \Grpd$$

로서, 각 대상 $T$마다 $T$ 위에 정의된 기하학적 대상들의 family를 대응시키는 것이며 우리는 앞선 글들에서 이 functor가 sheaf가 될 조건 등을 살펴보았다. 이제 이번 글에서는 이러한 준비를 바탕으로 이 functor를 기하학적 대상으로 실현하는 문제를 다루고, 그 예시들을 살펴본다. 

## 모듈라이 함자

이러한 문제를 $\Grpd$-valued pseudofunctor로 적는 일은 [§스택, ⁋예시 9](/ko/math/stacks/fibered_categories_and_stacks#ex9)에서 이미 마쳤으므로, 여기에서는 그 functor에 이름을 붙이고 표기를 고정하는 것으로 시작한다. 

::: 정의 1
Pseudofunctor $\mathcal{M}:\Sch^\op \rightarrow \Grpd$을 *moduli functor<sub>모듈라이 함자</sub>*라 부른다. ([§스택, ⁋정의 3](/ko/math/stacks/fibered_categories_and_stacks#def3)) 

각 scheme $T$에 대하여, fiber groupoid $\mathcal{M}(T)$의 대상을 *$T$-family*라 부른다. 그 isomorphism class만을 취하여 얻는 set-valued functor

$$\underline{M}:\Sch^\op \rightarrow \Set,\qquad \underline{M}(T)=\obj \mathcal{M}(T)/\cong$$

를 $\mathcal{M}$의 *coarse moduli functor<sub>성긴 모듈라이 함자</sub>* 또는 *set-valued moduli functor*라 부른다.
:::

Moduli functor의 본질적인 내용은 $T$-family가 어떤 기하학적 대상을 담는지에 있다. 예를 들어 genus $g$ 곡선을 분류할 때에는 $T$-family를 모든 geometric fiber가 genus $g$ curve가 되는 smooth projective morphism $X \rightarrow T$으로 잡는 것이 맞을 것이고, 고정된 variety $X$ 위의 vector bundle을 분류할 때에는 $X\times T$ 위의 rank $r$ vector bundle로 잡는 것이 맞을 것이다. 어느 경우든 공통적으로 pullback은 morphism $f: T' \rightarrow T$에 대한 fiber product로 주어지며, pseudofunctor의 compatibility condition은 이 fiber product의 universal property, 즉 canonical isomorphism의 데이터로부터 나온다. 이 때문에 $\mathcal{M}$은 functor가 아니라 pseudofunctor가 되며, 위에서 살펴봤듯 $\mathcal{M}(T)$가 $T$-family를 담으므로 이를 다룰 때는 보편적으로 CFG의 언어를 사용한다. ([§스택, ⁋정리 8](/ko/math/stacks/fibered_categories_and_stacks#thm8))

위의 두 구조를 하나로 합치는 것은 *universal family*의 개념이다. Contravariant functor $F:\Sch^\op \rightarrow \Set$과 scheme $M$에 대하여, $\Hom_\Sch(-, M)$에서 $F$로 가는 natural transformation 전체와 집합 $F(M)$ 사이의 bijection은 명시적으로

$$\alpha\mapsto \alpha_M(\id_M)$$

을 통해 주어지던 것을 기억하자. ([\[범주론\] §표현가능한 함자, ⁋정리 4](/ko/math/category_theory/representable_functors#thm4)) 즉 natural transformation $\alpha$가 어떠한 것인지는 항등사상에서의 값 $\alpha_M(\id_M)$ 하나로 완전히 결정되며, $\alpha$가 natural isomorphism이면 이렇게 얻어지는 원소를 *universal element*라 불렀다. ([\[범주론\] §표현가능한 함자, ⁋정의 5](/ko/math/category_theory/representable_functors#def5))

Yoneda lemma 자체는 $\Set$-valued functor에 대한 것이지만 이를 $\Grpd$-valued 상황으로 올릴 수 있다. [§스택, ⁋예시 9](/ko/math/stacks/fibered_categories_and_stacks#ex9)에서와 같이 각 scheme $T$를 slice category가 주는 CFG로 보면, $T$에서 $\mathcal{M}$으로 가는 morphism들과 그 사이의 2-morphism들이 이루는 groupoid는 fiber groupoid $\mathcal{M}(T)$과 equivalent하며, 위에서와 마찬가지로 이 equivalence는  $f:T\rightarrow\mathcal{M}$을 $f(\id_T)$로 보낸다. 따라서 $f$의 전체 자료는 $T$-family $X=f(\id_T)$에 의해 isomorphism까지 결정되고, 두 morphism 사이의 2-morphism도 $\id_T$에서의 성분, 곧 두 $T$-family 사이의 isomorphism에 의해 결정된다. 거꾸로 $X\in\mathcal{M}(T)$는 각 $u:T'\rightarrow T$에 $u^\ast X$를 대응시키는 morphism $f_X:T\rightarrow\mathcal{M}$을 정한다.

따라서 이를 $\id_\mathcal{M}:\mathcal{M}\rightarrow\mathcal{M}$을 $\mathcal{M}$ 위의 universal family로 읽을 수 있다. $T$-family $X$에 대응하는 $f_X:T\rightarrow\mathcal{M}$을 따라 이를 pullback하는 것은 $\id_\mathcal{M}\circ f_X=f_X$를 취하는 것이고, 위의 동치 아래에서 이는 다시 $X$가 된다. 즉 moduli functor $\mathcal{M}$이 정의하는 <em-ko>모든</em-ko> family는 단 하나의 universal family $\id_\mathcal{M}$을 끌어당겨 얻어지며, 이는 [\[대수적 위상수학\] §분류공간, ⁋정리 8](/ko/math/algebraic_topology/classifying_spaces#thm8)의 직접적인 일반화이다.

## 섬세한 모듈라이 공간

Scheme $M$이 $\Sch$ 위에서 갖는 자료는 functor of points $\Hom_\Sch(-, M)$뿐이고 이는 set-valued이므로, moduli functor를 scheme으로 실현하겠다면 우리가 관심을 가져야 할 대상은 $\mathcal{M}$ 자체가 아니라 coarse moduli functor $\underline{M}$이다. 원래 $\mathcal{M}$을 $\Grpd$로 향하는 것으로 적은 것은 각 family의 automorphism을 기억하기 위함이었으니, 분류하려는 문제가 isomorphism class만을 묻는 것이라면 이 약화에서 잃는 것은 없다. 남는 물음은 이렇게 내린 $\underline{M}$이 어떤 scheme의 functor of points와 일치하는지, 그리고 이것이 우리가 기대하는 성질을 가지는지 등의 여부일 것이다.

::: 정의 2
Moduli functor $\mathcal{M}$의 coarse moduli functor $\underline{M}:\Sch^\op \rightarrow \Set$가 scheme $M$에 의하여 *representable*할 때, 곧 natural isomorphism

$$\underline{M}\cong \Hom_{\Sch}(-, M)$$

이 존재할 때, $M$을 $\mathcal{M}$의 *fine moduli space<sub>섬세한 모듈라이 공간</sub>*라 부른다. 이 때, 이 natural isomorphism 아래에서 identity morphism $\id_M\in \Hom_\Sch(M, M)$에 대응하는 원소

$$\mathcal{U}\in \underline{M}(M)$$

을 *universal family<sub>보편족</sub>*라 부른다.
:::

위의 universal family는 $\Set$-valued functor $\underline{M}$에 Yoneda lemma를 적용하여 얻어지는 것으로, 임의의 scheme $T$와 $T$-family $X\in \underline{M}(T)$에 대하여, natural isomorphism의 한 성분 $\underline{M}(T)\cong \Hom_\Sch(T, M)$이 $X$에 대응시키는 $f_X: T \rightarrow M$은 Yoneda의 naturality에 의하여

$$X\cong f_X^\ast \mathcal{U}$$

을 만족하는 유일한 morphism이 되며, 이를 $X$의 *classifying morphism*이라 부른다.

이 정보는 본질적으로 새로운 것이 아니다. Scheme $M$을 representable CFG로 보면, 앞선 섹션에서 살펴본 2-Yoneda lemma에 의하여 morphism $s:M\rightarrow\mathcal{M}$을 택하는 것은 $M$-family를 택하는 것과 같다. 따라서, fine moduli space의 universal family $\mathcal{U}\in\underline{M}(M)$의, $\mathcal{M}(M)$에서의 representative를 하나 택하면 이에 대응하는 morphism $s:M\rightarrow\mathcal{M}$이 up to 2-isomorphism으로 정해진다. 거꾸로 $\mathcal{M}$ 위의 tautological universal family $\id_\mathcal{M}$을 $s$를 따라 pullback하면 $\id_\mathcal{M}\circ s=s$이고, 2-Yoneda lemma 아래서 이 morphism에 대응하는 $M$-family가 바로 $\mathcal{U}$이다.

이 관점에서 moduli functor $\mathcal{M}$과 이를 표현하는 scheme $M$의 관계도 드러난다. 임의의 morphism $g:T\rightarrow\mathcal{M}$을 택하면 $\mathcal{M}$ 쪽에서는 이것이 automorphism까지 기억하는 $T$-family $X=g(\id_T)$을 정한다. 한편, 이 family $X$의 isomorphism class $[X]\in\underline{M}(T)$만을 취하면, scheme $M$이 $\underline{M}$을 표현하므로 이는 동시에 $M$ 쪽의 유일한 morphism $f_X:T\rightarrow M$도 정해준다. 이제

$$(s\circ f_X)(\id_T)=f_X^\ast s(\id_M)=f_X^\ast\mathcal{U}\cong X=g(\id_T)$$

이므로 다시 2-Yoneda lemma에 의하여 $g\simeq s\circ f_X$임을 확인할 수 있다. 즉, scheme에서 $\mathcal{M}$으로 가는 모든 morphism은 $s$를 통해 $M$을 거쳐 up to $2$-isomorphism으로 factor through하며, 거꾸로 이러한 조건 $g\simeq s\circ h$을 만족하는 $h:T\rightarrow M$는 반드시 $X\cong h^\ast\mathcal{U}$을 만족하므로 $h=f_X$이다. 즉 $M$의 universal property처럼 보인 것은 사실 $\mathcal{M}$의 universal property에, factorization에 대한 주장 $g\simeq s\circ f_X$를 더한 것이다. 이 factorization은 up to $2$-isomorphism으로 유일하지만, 그 $2$-isomorphism 자체는 $X$가 nontrivial한 automorphism을 갖는 경우에는 유일하지 않을 수 있다.

::: 예시 3 (Grassmannian)
[\[스킴\] §점함자, ⁋예시 6](/ko/math/scheme_theory/functor_of_points#ex6)에서 우리는 정수 $0<k<n$에 대하여 contravariant functor $F_{k,n}:\Sch^\op\rightarrow\Set$를

$$F_{k,n}(T)=\{\mathcal{O}_T^{\oplus n}\twoheadrightarrow\mathcal{Q}\mid\mathcal{Q}\text{ is locally free of rank }k\}/{\cong}$$

으로 정의하고, 이것이 Grassmannian의 functor of points $\Gr(k,n)$과 naturally isomorphic이라는 것을 살펴보았다. 이 예시에서 우리는 이를 moduli space의 언어로 살펴본다.

Grassmannian 위의 tautological quotient을

$$q^{\mathrm{univ}}:\mathcal{O}_{\Gr(k,n)}^{\oplus n}\twoheadrightarrow\mathcal{Q}^{\mathrm{univ}}$$

으로 쓰면, $\Gr(k,n)$이 $F_{k,n}$을 표현하는 natural isomorphism은 명시적으로

$$\Phi_T:\Hom_\Sch(T,\Gr(k,n))\longrightarrow F_{k,n}(T),\qquad f\longmapsto [f^\ast q^{\mathrm{univ}}]$$

으로 주어진다. [정의 2](#def2)에서 universal family는 이 natural isomorphism 아래에서 $\id_{\Gr(k,n)}$에 대응하는 원소이므로,

$$\mathcal{U}=\Phi_{\Gr(k,n)}(\id_{\Gr(k,n)})=[\id_{\Gr(k,n)}^\ast q^{\mathrm{univ}}]=[q^{\mathrm{univ}}]$$

이다. 따라서 $\Gr(k,n)$의 universal family는 바로 universal quotient $q^{\mathrm{univ}}$이다. 또한 $T$ 위의 quotient $q:\mathcal{O}_T^{\oplus n}\twoheadrightarrow\mathcal{Q}$는 유일한 classifying morphism $f_q:T\rightarrow\Gr(k,n)$을 정하며, $q$는 $q^{\mathrm{univ}}$을 $f_q$를 따라 pullback하여 얻는다.

이 parametrizing scheme의 한 점이 나타내는 대상을 universal family로부터 뽑아내자. Geometric point $x:\Spec\mathbb{K}\rightarrow\Gr(k,n)$을 택하고 universal quotient을 $x$를 따라 pullback하면

$$\mathbb{K}^n\twoheadrightarrow Q_x:=x^\ast\mathcal{Q}^{\mathrm{univ}}$$

을 얻는다. 여기에서 $Q_x$는 $\mathcal{Q}^{\mathrm{univ}}$의 $x$에서의 geometric fiber이고, quotient map $\mathbb{K}^n\twoheadrightarrow Q_x$가 $x$에 대응하는 moduli object이다. 이 quotient는 kernel $S_x\subseteq\mathbb{K}^n$에 의하여 유일하게 결정되고 $\dim S_x=n-k$이므로, $\Gr(k,n)$의 $\mathbb{K}$-point들은 $\mathbb{K}^n$의 $(n-k)$차원 부분공간들을 parametrize한다.
:::

한편, 일반적인 moduli problem은 fine moduli space를 가지지 않을 수 있으며, scheme 위의 vector bundle들을 분류하는 moduli problem이 정확히 그러한 예시이다. 반면 [예시 3](#ex3)의 functor $F_{k,n}$은 rank $k$ vector bundle $\mathcal{Q}$와 함께 quotient map $q:\mathcal{O}_T^{\oplus n}\twoheadrightarrow\mathcal{Q}$를 분류하며, Grassmannian $\Gr(k,n)$에 의하여 representable하다. 즉 vector bundle에 quotient map을 추가 자료로 포함하자 fine moduli space가 생긴 것이다. 이 차이는 quotient map이 automorphism에 가하는 제약에서 비롯된다.

Automorphism이 왜 문제가 되는지는 family를 생각하면 직관적으로 드러난다. 한 moduli object의 automorphism을 이용하면 locally constant이지만 base 전체에서는 constant이 아닌 family를 만들 수 있다. Fine moduli space가 존재한다면 두 family의 classifying morphism은 locally 같으므로 전체에서도 같아야 하지만, 하나의 universal family를 같은 morphism을 따라 pullback하여 서로 isomorphic하지 않은 두 family를 얻을 수는 없다.

Vector bundle들을 분류하는 moduli problem이 fine moduli space를 가지지 않는 핵심 원인은 vector bundle $\mathcal{Q}$가 비자명한 automorphism을 가질 수 있다는 데 있다. 반면 quotient map $q$를 추가 자료로 포함하면, 전체 자료의 automorphism $\theta:\mathcal{Q}\rightarrow\mathcal{Q}$는 $q$를 보존해야 하므로 $\theta\circ q=q$를 만족한다. $q$가 surjective이므로 이 등식은 $\theta=\id_\mathcal{Q}$를 강제한다. 이처럼 분류 대상에 추가된 자료는 automorphism이 보존해야 할 조건을 늘려 automorphism group을 작게 만들고, 충분한 조건을 주면 identity morphism만 남길 수 있다. 이러한 효과를 rigidity라 하며, [예시 3](#ex3)의 quotient map $q$와 같은 추가 자료를 rigidifying data라 부른다.

그럼 다음 명제는 위에서 살펴본 fine moduli space의 failure를 더 엄밀하게 적은 것이다.

::: 명제 4
Moduli functor $\mathcal{M}$에 대하여 scheme $T$, surjective étale covering $S\rightarrow T$, $T$-family $X\in\mathcal{M}(T)$, 고정된 moduli object $E$가 존재하여 $X\times_TS\cong E\times S$이지만 $X\not\cong E\times T$이면, $\mathcal{M}$은 fine moduli space를 가지지 않는다.
:::
::: 증명
결론에 반하여 fine moduli space $M$이 존재한다고 가정하자. [정의 2](#def2)에 의하여 set-valued moduli functor는 representable functor $\underline{M}\cong \Hom_\Sch(-, M)$이다. Representable functor는 fpqc topology에 대한 sheaf이므로 étale topology에 대해서도 sheaf이다. Sheaf 조건 가운데 separatedness는 임의의 covering $S \rightarrow T$에 대하여 restriction map

$$\underline{M}(T) \rightarrow \underline{M}(S)$$

이 injective인 것이다.

이제 가정의 두 family $X$과 $E\times T$을 $\underline{M}(T)$의 원소로 본다. $S$로 끌어당기면 $X\times_T S\cong E\times S\cong (E\times T)\times_T S$이므로, 두 isomorphism class는 $\underline{M}(S)$에서 같은 원소로 보내진다. 그러나 가정에 의하여 $X$과 $E\times T$은 $T$ 위에서 isomorphic이 아니므로 $\underline{M}(T)$에서 서로 다른 원소이다. 이는 restriction map $\underline{M}(T) \rightarrow \underline{M}(S)$의 injectivity에 모순이다. 따라서 $\underline{M}$은 separated presheaf조차 될 수 없고, representable할 수 없으므로 fine moduli space는 존재하지 않는다.
:::

[명제 4](#prop4)의 isotrivial family는 constant family $E\times S$의 descent datum을 $\Aut(E)$의 원소들로 비틀어 만들 수 있다. 이 descent datum이 nontrivial한 $\Aut(E)$-torsor를 정하면, 내려온 family는 covering 위에서는 constant이지만 base 위에서는 constant이 아니게 된다. 다만 automorphism의 존재만으로 이러한 일이 항상 일어나는 것은 아니므로, 실제 obstruction은 각 moduli problem에서 따로 확인해야 한다.

## 타원곡선

Field $\mathbb{K}$ 위의 elliptic curve는 $\mathbb{K}$-rational point $0$이 지정된 smooth projective genus $1$ curve $(E,0)$이다. Characteristic $0$의 field 위에서는 모든 elliptic curve를 short Weierstrass equation

$$E_{a,b}:\y^2=\x^3+a\x+b,\qquad \Delta=-16(4a^3+27b^2)\neq 0$$

으로 나타낼 수 있다는 것이 알려져 있으며, 이 표현 상에서 두 short Weierstrass curve $E_{a,b}$와 $E_{a',b'}$ 사이에 (pointed) isomorphism이 존재할 필요충분조건은 어떤 $\lambda\in\mathbb{K}^\times$에 대하여

$$(a',b')=(\lambda^4a,\lambda^6b)$$

가 성립하는 것이다. 이 때, isomorphism은 coordinate change $(\x,\y)\mapsto(\lambda^2\x,\lambda^3\y)$로 주어지며, 이 coordinate change 아래에서 변하지 않는

$$j(E_{a,b})=1728\frac{4a^3}{4a^3+27b^2}$$

를 $j$-invariant라 한다. Algebraically closed field 위에서는 두 elliptic curve가 isomorphic일 필요충분조건이 $j$-invariant가 같은 것이다.

Pointed automorphism은 이 coordinate change로부터 직접 계산할 수 있다. $E_{a,b}$의 automorphism에 대응하는 $\lambda$는 $\lambda^4a=a$와 $\lambda^6b=b$을 만족한다. 따라서 $a,b\neq0$이면 $\lambda^2=1$이고, $a=0$이면 $\lambda^6=1$, $b=0$이면 $\lambda^4=1$이다. Algebraically closed field of characteristic $0$ 위에서는 각각 $j(E)\neq0,1728$, $j(E)=0$, $j(E)=1728$인 경우이므로

$$\Aut(E,0)\cong\begin{cases}\mu_6 & j(E)=0,\\ \mu_4 & j(E)=1728,\\ \mu_2 & j(E)\neq 0,1728\end{cases}$$

이다. 특히 모든 elliptic curve에는 $\mu_2=\{\pm1\}$이 남는다. 그 nontrivial automorphism을 $\iota_E$라 쓰면

$$\iota_E:(\x,\y)\longmapsto(\x,-\y)$$

이다.

::: 예시 5 (Elliptic curves)
Algebraically closed field $\mathbb{K}$ of characteristic $0$ 위에서

$$ab(4a^3+27b^2)\neq0$$

인 elliptic curve $E=E_{a,b}$을 고정하자. 그럼 특히 $\Delta\neq 0$이고, $a,b\neq 0$이므로 $j(E)\neq0,1728$이어서 $\Aut(E,0)=\mu_2=\{1,\iota_E\}$가 된다.

Moduli problem에서 우리는 이러한 조건을 만족하는 elliptic curve의 family를 생각한다. 여기서 scheme $T$ 위의 elliptic curve family는 모든 geometric fiber가 smooth projective genus $1$ curve인 smooth proper morphism $\pi:\mathcal{E}\rightarrow T$와 section $0:T\rightarrow\mathcal{E}$의 쌍이다.

이 예시의 목적은 [명제 4](#prop4)를 손에 잡히는 예시로 계산하는 것이다. 이에 따르면 elliptic curve들의 moduli가 fine moduli space가 되지 않는다는 것을 보이기 위해서는 nontrivial한 automorphism $\iota_E$를 이용하여 locally trivial하지만 constant이지 않은 family를 구성하면 된다. 이를 위해 $T=\Spec\mathbb{K}(t)$로 두고 그 extension $\mathbb{K}(t)\subseteq\mathbb{K}(t)[\sqrt{t}]$을 생각하자. 이 위에서 $c=\sqrt{t}$에 대한 coordinate change는 $E_{a,b}$와 $E_{c^4a,c^6b}=E_{t^2a,t^3b}$ 사이의 isomorphism을 주므로, $T$ 위의 curve를

$$X:\y^2=\x^3+t^2a\x+t^3b$$

로 정하면 된다. 실제로 $X$의 discriminant는 $\Delta_X=t^6\Delta_E$이므로 nonzero가 되어 elliptic curve가 되며, étale double covering $S=\Spec(\mathbb{K}(t)[\sqrt{t}])\rightarrow T$ 위에서는 coordinate change $(\x,\y)\mapsto(t\x,t\sqrt{t}\y)$에 의하여 $X\times_TS\cong E\times_{\mathbb{K}}S$이다. 이 isomorphism에서 $\sqrt{t}$의 두 선택은 $\iota_E$만큼 차이 나므로, $X$는 $\iota_E$로부터 얻은 *quadratic twist*이다.

반면 $T$ 위에서 이러한 isomorphism이 존재하려면 어떤 $c\in\mathbb{K}(t)^\times$가 $c^4=t^2$과 $c^6=t^3$을 만족해야 한다. 그러면 $c^2=t$이어야 하지만, $t$은 $\mathbb{K}(t)$에서 square가 아니다. 즉 $X$은 $S$ 위에서는 constant이지만 $T$ 위에서는 constant가 아니다.

따라서 [명제 4](#prop4)에 의하여 elliptic curve의 moduli functor는 fine moduli space를 가지지 않는다. 또한 coefficient에 생긴 $t$의 power가 $j$-invariant의 numerator와 denominator에서 모두 $t^6$으로 소거되므로 $j(X)=j(E)$이다. 이로부터 geometric isomorphism class를 $j$의 값으로 나타내는 affine line $\mathbb{A}^1_j$ 위에도 universal family는 존재할 수 없다는 것을 안다.
:::

Grassmannian에서는 quotient map이 automorphism을 없앴지만, elliptic curve에서는 section을 고정한 뒤에도 $\iota_E$가 남아 nontrivial twist를 만든다. 이 차이는 automorphism을 기억하는 기하적 대상으로 옮겨 가는 방법과, automorphism을 버리고 isomorphism class만 담는 근사를 찾는 방법으로 이어진다.

## 모듈라이 스택과 성긴 모듈라이 공간

이러한 문제를 해결하는 방법 중 가장 간단한 것은 우리가 이미 가지고 있는 것이다.

::: 정의 6
Moduli functor $\mathcal{M}$이 algebraic stack일 때, 이를 *moduli stack<sub>모듈라이 스택</sub>*이라 부른다. ([§대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6))
:::

즉, 원래의 moduli problem $\mathcal{M}$을 더 이상 약화시키지 않고 있는 그대로 사용하되, 이것이 기하적으로 행동하기 위한 최소한의 조건, 즉 algebraic stack일 조건만 요구하는 것이다. 추가적으로 moduli stack $\mathcal{M}$이 Deligne–Mumford stack인 것은 diagonal $\Delta:\mathcal{M}\rightarrow\mathcal{M}\times\mathcal{M}$이 unramified인 것과 동치이고, 다시 모든 geometric point의 stabilizer가 unramified인 것과 동치이다. ([§대수적 스택, ⁋정의 6](/ko/math/stacks/algebraic_stacks#def6))

다른 한 가지 방법은 여전히 coarse moduli를 생각하되, universal family는 포기하고 isomorphism class를 담는 base space만 보는 것이다.

::: 정의 7
Moduli functor $\mathcal{M}$의 coarse moduli functor $\underline{M}:\Sch^\op \rightarrow \Set$에 대하여, algebraic space $M$과 natural transformation $\Phi:\underline{M} \rightarrow M$의 쌍이 *coarse moduli space<sub>성긴 모듈라이 공간</sub>*라는 것은 다음 두 조건을 만족하는 것이다.

1. (Universality) 임의의 algebraic space $N$과 natural transformation $\Psi:\underline{M} \rightarrow N$에 대하여, $\Psi=\pi\circ \Phi$을 만족하는 morphism $\pi:M\rightarrow N$이 유일하게 존재한다.

2. (Bijection on geometric points) 임의의 algebraically closed field $\mathbb{K}$에 대하여, $\Phi$의 성분 $\Phi(\Spec\mathbb{K}):\underline{M}(\Spec\mathbb{K})\rightarrow M(\mathbb{K})$이 bijective이다.
:::

Universality는 $\underline{M}$에서 algebraic space로 가는 모든 natural transformation이 $M$을 유일하게 factor through한다는 것으로, 이미 [정의 2](#def2) 직후에 우리는 이 조건에 대해 충분히 논의하였다. 새로 나온 두 번째 조건은 $M$의 geometric points가 분류하고자 하는 대상의 geometric isomorphism classes와 정확히 대응함을 보장하는 것으로, 가령 fine moduli가 주어진 [예시 3](#ex3)에서 우리는 family의 한 geometric point 위에 있는 대상을 빼오기 위해 비슷한 아이디어를 사용한 적이 있었다. 다만 차이는 그 때와는 다르게 universal family의 부재로 인하여 이 점이 실제로 담고 있는 기하적 대상이 무엇인지를 보는 것이 더 이상은 functorial하게는 불가능하다는 것이다.

이와 같이 요구조건을 약화시키면, coarse moduli space의 존재를 보장하는 대표적인 결과가 Keel–Mori 정리이다.

::: 정리 8 (Keel–Mori)
Noetherian base $S$ 위에서 locally of finite type인 algebraic stack $\mathcal{M}$의 inertia morphism

$$I_\mathcal{M}=\mathcal{M}\times_{\mathcal{M}\times_S\mathcal{M}}\mathcal{M}\longrightarrow\mathcal{M}$$

이 finite이면, coarse moduli space $\pi:\mathcal{M}\rightarrow M$이 존재한다. 여기에서 $M$은 $S$ 위에서 locally of finite type인 algebraic space이고, $\pi$은 geometric isomorphism classes와 $M$의 geometric points 사이의 bijection을 유도한다. 특히 separated finite type Deligne–Mumford stack은 coarse moduli space를 가진다.
:::

Inertia stack $I_\mathcal{M}$의 geometric fiber는 해당 point의 stabilizer group scheme이다. 따라서 positive-dimensional stabilizer를 갖는 [§대수적 스택, ⁋예시 11](/ko/math/stacks/algebraic_stacks#ex11)의 $\bB\mathbb{G}_m$이나 [§대수적 스택, ⁋예시 12](/ko/math/stacks/algebraic_stacks#ex12)의 $[\mathbb{A}^1/\mathbb{G}_m]$에는 [정리 8](#thm8)을 적용할 수 없다. 정리는 이러한 경우 coarse moduli space의 존재 여부에 관하여 결론을 주지 않는다.

::: 예시 9 (Coarse moduli space of elliptic curves)
Algebraically closed field $\mathbb{K}$ of characteristic $0$ 위에서 $\Delta\neq0$인 Weierstrass coefficient의 parameter scheme을

$$U=\Spec\mathbb{K}[a,b,\Delta^{-1}]$$

로 두자. Elliptic curve의 coordinate change는 $\mathbb{G}_m$-action $\lambda\cdot(a,b)=(\lambda^4a,\lambda^6b)$으로 보면 elliptic curve의 moduli stack은 quotient stack

$$\mathcal{M}_{1,1}\cong[U/\mathbb{G}_m]$$

으로 표현된다. ([§대수적 스택, ⁋정의 7](/ko/math/stacks/algebraic_stacks#def7)) 이 때, 각 point의 stabilizer는 이미 앞에서 계산한 $\Aut(E,0)$이다. 이들은 characteristic $0$에서 finite étale이므로 $\mathcal{M}_{1,1}$은 Deligne–Mumford stack이고, inertia가 finite이므로 [정리 8](#thm8)을 적용할 수 있다. ([§대수적 스택, ⁋정리 10](/ko/math/stacks/algebraic_stacks#thm10))

이 action에서 $a$와 $b$의 weight는 각각 $4$와 $6$이고 $\Delta$의 weight는 $12$이다. 따라서 invariant ring은

$$\mathbb{K}[a,b,\Delta^{-1}]^{\mathbb{G}_m}=\mathbb{K}[j]$$

이다. 이 계산으로 [정리 8](#thm8)이 보장하는 coarse moduli morphism은 $j$-invariant가 주는 natural transformation

$$\Phi:\underline{M}_{1,1}\longrightarrow\mathbb{A}^1_j,\qquad(E,0)\longmapsto j(E)$$

로 주어진다. Algebraically closed field 위에서는 $j$-invariant가 elliptic curve의 isomorphism class를 완전히 결정하므로, $\Phi$는 geometric points에서 bijective이다. 따라서 $(\mathbb{A}^1_j,\Phi)$은 $\mathcal{M}_{1,1}$의 coarse moduli space이다.

그러나 $\mathbb{A}^1_j$ 위에는 universal family가 존재하지 않는다. [예시 5](#ex5)의 nontrivial quadratic twist는 $j$-invariant가 constant이므로 $\mathbb{A}^1_j$로 가는 동일한 constant morphism을 정하지만, 두 family는 base 위에서 isomorphic하지 않다. 반면 $\mathcal{M}_{1,1}$로 가는 classifying morphism은 이 twist를 구별한다. 또한 $j=0$과 $j=1728$ 위에서 $\mathcal{M}_{1,1}$은 각각 $\mu_6$과 $\mu_4$ stabilizer를 기억하지만 $\mathbb{A}^1_j$은 이를 평범한 point로만 나타낸다. 이 예시는 moduli stack과 coarse moduli space가 같은 geometric isomorphism classes를 담으면서도 서로 다른 정보를 보존한다는 것을 보여준다.
:::

Elliptic curve는 하나의 marked point를 가진 genus $1$ smooth projective curve이므로, $\mathcal{M}_{1,1}$은 pointed curve의 moduli stack $\mathcal{M}_{g,n}$에서 $(g,n)=(1,1)$인 경우이다. Genus와 marked point의 수를 바꾸면 일반적인 curve의 moduli로 이어지며, automorphism을 stack에 어떻게 보존할지, coarse moduli space를 언제 얻을 수 있는지, stable curve를 더하여 어떻게 compactify할지가 다음 단계의 문제가 된다.

---

**참고문헌**

**[FGA]** B. Fantechi, L. Göttsche, L. Illusie, S. L. Kleiman, N. Nitsure, A. Vistoli, *Fundamental algebraic geometry: Grothendieck's FGA explained*, American Mathematical Society, 2005.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*, https://stacks.math.columbia.edu.
