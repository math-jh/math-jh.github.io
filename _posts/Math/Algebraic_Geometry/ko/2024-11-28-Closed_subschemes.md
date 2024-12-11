---

title: "닫힌 부분스킴"
excerpt: ""

categories: [Math / Algebraic Geometry]
permalink: /ko/math/algebraic_geometry/closed_embeddings
header:
    overlay_image: /assets/images/Math/Algebraic_Geometry/Closed_embeddings.png
    overlay_filter: 0.5
sidebar: 
    nav: "algebraic_geometry-ko"

date: 2024-11-28
last_modified_at: 2024-11-28
weight: 6

---

앞선 글에서 우리는 scheme morphism에 부여할 수 있는 아주 다양한 종류의 조건들을 살펴보았다. 그럼에도 불구하고 여러 조건들이 남아있는데, 이번 글에서는 그 중 하나인 *closed embedding*과 closed subscheme에 대해 다룬다. 

사실 이 개념은 스킴을 정의하기도 전부터 이미 대략적으로는 알고 있었던 것으로, [§스펙트럼, ⁋따름정리 4](/ko/math/algebraic_geometry/spectrums#cor4)의 결과를 scheme의 언어로 옮겨와보면 $\Spec A/\mathfrak{a}$는 affine scheme $\Spec A$의 *닫힌* 부분집합이라는 말이 된다. 

하지만 scheme $X$의 affine open subscheme과는 다르게, $X$의 닫힌집합에 scheme 구조를 주는 것은 잘 정의되지 않는다. 이는 아주 간단한 예시로 $\mathbb{A}^1\_\mathbb{k}=\Spec \mathbb{k}[\x]$의 닫힌집합 $\\{0\\}$만 봐도 여실히 드러나는데, $\mathbb{A}^1\_\mathbb{k}$의 원점을 정의하는 ideal은 $(\x)$ 뿐만이 아니라 $(\x^k)$꼴의 ideal들이 전부 그렇기 때문이다. 때문에 우리는 closed subscheme을 먼저 정의하는 대신 closed embedding을 먼저 정의한다.

## 기본 정의들

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Scheme morphism $\iota:X \rightarrow Y$가 *closed embedding<sub>닫힌 매장</sub>*이라는 것은 $\iota$가 affine morphism이고, $Y$의 임의의 affine open subset $V=\Spec B$, 그리고 이로부터 얻어지는 $\iota^{-1}(V)\cong\Spec A$에 대하여 ring homomorphism $B \rightarrow A$가 surjective인 것이다.

</div>

이전 글에서와 마찬가지로 이 성질은 affine-local on target임을 쉽게 보일 수 있다. 만일 여기에 더하여 $X$가 $Y$의 부분집합이고, $\iota$가 inclusion이라면 $X$를 $Y$의 *closed subscheme*이라 부른다. 정의로부터 closed embedding은 finite인 것이 자명하다. 

Closed embedding의 가장 자명한 예시는 surjective ring homomorphism $B \rightarrow A$에 의해 유도되는 scheme morphism $\Spec A \rightarrow \Spec B$이다. 그럼 [\[대수적 구조\] §몫환, 환 동형사상, ⁋정리 3](/ko/math/algebraic_structures/quotient_rings#thm3)에 의하여 $A$를 $B/\mathfrak{b}$와 identify할 수 있다. 일반적인 scheme들 사이의 closed embedding에서 비슷한 이야기를 하기 위해서는 다음을 정의한다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> 임의의 scheme $X$에 대하여, $X$ 위에 정의된 *ideal sheaf*는 structure sheaf $\mathscr{O}\_X$의 $\mathscr{O}\_X$-submodule을 뜻한다. 

</div>

즉, $X$의 ideal sheaf $\mathscr{I}$는 별다른 것이 아니고 임의의 열린집합 $U\subseteq X$가 주어질 때마다 $\mathscr{O}_X(U)$의 ideal $\mathscr{I}(U)$를 대응시키는 sheaf이다. 그럼 closed embeedding $\iota:X \rightarrow Y$가 주어질 때마다, 자연스러운 $\mathscr{O}\_Y$-module homomorphism의 kernel

$$\mathscr{I}_{X/Y}=\ker(\mathscr{O}_Y \rightarrow f_\ast \mathscr{O}_X)$$

이 $Y$ 위의 ideal sheaf가 된다. 즉 다음의 exact sequence

$$0 \rightarrow \mathscr{I}_{X/Y} \rightarrow \mathscr{O}_Y \rightarrow \iota_\ast \mathscr{O}_X \rightarrow 0$$

이 존재한다. 그러나 그 역이 항상 성립하는 것은 아니다. 

<div class="example" markdown="1">

<ins id="ex3">**예시 3**</ins> Scheme $X=\Spec \mathbb{k}[\x]_{(\x)}$를 생각하자. 이 scheme은 두 개의 prime ideal $(0)$과 $(\x)$를 가지며, 이 중 $(\x)$는 maximal ideal이므로 closed point이다. 따라서, $X$의 위상은 

$$\mathcal{T}=\{\emptyset, \{(0)\}, X\}$$

으로 주어지며 이 때 structure sheaf는

$$\mathscr{O}_X(X)=\mathbb{k}[\x]_{(\x)},\quad \mathscr{O}_X(D(\x))=\mathbb{k}(\x)$$

이다. 이제 ideal sheaf $\mathscr{I}$를

$$\mathscr{I}(X)=0,\quad \mathscr{I}(D(\x))=\mathbb{k}(\x)$$

으로 정의하면 $\mathscr{I}$는 closed subscheme을 정의하지 않는다. $\mathbb{k}[\x]_{(\x)} \rightarrow \mathbb{k}(\x)$가 surjective가 아니기 때문이다.

</div>

이는 ideal sheaf $\mathscr{I}$ 자체는 $X$ 위에서 sheaf의 gluing condition을 만족하여 잘 붙는다해도, 서로 만나는 두 열린집합 $U_1,U_2$에 대하여 $U_1$에서 $\mathscr{I}(U_1)$이 정의하는 closed subscheme과 $U_2$에서 $\mathscr{I}(U_2)$가 정의하는 closed subscheme은 그 교집합에서 일치하지 않을 수 있기 때문이다. 이를 바탕으로 다음 명제를 증명할 수 있다. 

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> Scheme $X$와 그 위에 정의된 ideal sheaf $\mathscr{I}$를 생각하자. 그럼 임의의 affine open subset $U=\Spec A$와 임의의 $f\in A$에 대하여, $V=\Spec A_f$는 $X$의 open subscheme

$$\Spec A_f \rightarrow \Spec A \rightarrow X$$

이다. 만일 임의의 $U=\Spec A$와 $f\in A$의 선택에 대하여, ring homomorphism $A \rightarrow A_f$에 의한 $\mathscr{I}(U)\subset A$의 image $\mathscr{I}(U)_f$가 정확히 $\mathscr{I}(V)$와 같다면 $\mathscr{I}$는 closed subscheme을 정의한다. 

</div>

특히 다음이 성립한다.

<div class="proposition" markdown="1">

<ins id="cor5">**따름정리 5**</ins> Scheme $X$와 global section $s\in \Gamma(X, \mathscr{O}_X)$에 대하여, 각각의 affine open subset $U=\Spec A$마다 $\mathscr{I}(U)=(s\vert_U)\subseteq A$으로 정의하면 ideal sheaf $\mathscr{I}$는 $X$의 closed subscheme $V(s)$를 정의한다.  

</div>

마지막으로 다음을 정의한다. 

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> Scheme morphism $f: X \rightarrow Y$가 *locally closed embedding<sub>국소적으로 닫힌 매장</sub>*이라는 것은 적당한 closed embedding $i: X \rightarrow Z$, open embedding $j:Z \rightarrow Y$가 존재하여 $f=j\circ i$인 것이다. 

</div>

앞서 cloed embedding은 finite morphism이므로, 자명한 이유로 finite type이었다. 비슷하게 locally closed embedding은 locally of finite type인 것이 자명하다. 

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> Affine scheme이 아닌 예시 중 가장 간단한 것은 projective space $\mathbb{P}^n_A$이다. 

[§스킴, §§사영공간과 Proj](/ko/math/algebraic_geometry/schemes#사영공간과-proj)에서 우리가 $\Proj S$를 정의한 직관은 $\mathbb{P}^n_A$ 위에서 homogeneous polynomial $f\in \mathbb{k}[\x_0,\ldots, \x_n]$은 잘 정의된 함수는 아니지만, $V(f)$는 $\mathbb{P}^n_A$의 닫힌집합을 잘 정의한다는 것이었다. 이제 우리는 $V(f)$가 $\mathbb{P}^n_A$의 closed subscheme이라는 것을 알 수 있는데, 각각의 affine cover 

$$U_i=\{[x_0:\cdots:x_n]\in \mathbb{P}^n_A\mid x_i\neq 0\}=\Spec A[\x_{0/i}, \ldots, \x_{(i-1)/i},\x_{(i+1)/i},\ldots,\x_{n/i}]$$

에서, $V(f)$를 정의하는 ideal은 정확히

$$\mathscr{I}(U_i)=(f(\x_{0/i},\ldots, \x_{(i-1)/i},1,\x_{(i+1)/i},\ldots, \x_{n/i}))$$

이다. 이와 같이 $V(f)$로 정의되는 closed subscheme을 $\mathbb{P}^n_A$의 *hypersurface*라 부르고, 그 차수를 $f$의 차수로 정의한다. 

</div>

## 스킴 사상의 상

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> Scheme morphism $f:X \rightarrow Y$에 대하여, $f$의 image가 closed subscheme $\iota: Z \rightarrow Y$에 포함된다는 것은 ideal sheaf $\mathscr{I}_{Z/Y}$에 대하여 합성

$$\mathscr{I}_{Z/Y} \rightarrow \mathscr{O}_Y \rightarrow f_\ast \mathscr{O}_X$$

가 $0$인 것이다. 이제 $f$의 *scheme-theoretic image*는 $f$의 image를 포함하는 가장 작은 closed subset, 즉 $f$의 image의 closure로 정의한다. 

</div>

이렇게 정의하는 이유는, $f$의 집합으로서의 image는 일반적으로 잘 행동하지 않기 때문이다. 한편 우리는 $Y$의 affine open subset $V$가 주어졌을 때, 다음의 scheme morphism

$$f\vert_{f^{-1}(V)}: f^{-1}(V) \rightarrow V$$

의 scheme-theoretic image와, $f$의 scheme-theoretic image를 $U$로 제한한 것이 같기를 바랄텐데, 일반적으로 이는 참이 아니지만 상대적으로 약한 조건만 가정하더라도 이는 참이 된다.

<div class="proposition" markdown="1">

<ins id="prop9">**명제 9**</ins> Scheme morphism $f:X \rightarrow Y$가 주어졌다 하자. 만일 $f$가 quasicompact라면, $Y$의 임의의 affine open subset $V$에 대하여 $f\vert_{f^{-1}(V)}$의 scheme-theoretic image와, $f$의 scheme-theoretic image를 $U$로 제한한 것이 같다.

</div>

## 닫힌 집합 위에 정의되는 스킴 구조

우리는 맨 처음에 $X$의 임의의 닫힌집합에 scheme 구조를 주는 것이 유일하지 않다는 것을 지적했는데, 그럼에도 불구하고 그 위에 *reduced* scheme structure를 주는 방법은 유일하다. Scheme 구조가 reduced임을 요구함으로써 우리는 그에 해당하는 ideal이 radical ideal일 것을 추가하게 되기 때문이다. 특히 이 정의는 $X$를 자기 자신의 닫힌집합으로 보았을 때도 적용되는데, 이를 통해 non-reduced scheme $X$가 주어졌을 때 이를 reduced scheme으로 바꿔줄 수 있다. 