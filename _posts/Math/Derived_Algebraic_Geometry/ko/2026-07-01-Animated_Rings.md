---
title: "Simplicial 가환환과 animation"
description: "Simplicial 대상과 Dold–Kan 대응을 도입하여 simplicial(animated) 가환환을 정의하고, 그 homotopy 군과 유도 텐서곱, 그리고 자유 분해로 구성하는 완전한 여접 복합체와 추이 삼각형을 다룬다."
excerpt: "Simplicial objects, Dold–Kan, animated commutative rings, ⊗^L, and the full cotangent complex"

categories: [Math / Derived Algebraic Geometry]
permalink: /ko/math/derived_algebraic_geometry/animated_rings
sidebar: 
    nav: "derived_algebraic_geometry-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 2

published: false

---

[\[스킴\] §변형이론과 여접 복합체, ⁋참고 12](/ko/math/scheme_theory/deformation_theory#rmk12)에서 우리는 naive 여접 복합체 $\operatorname{NL}_{B/A}$가 변형이론의 요구를 온전히 감당하지 못함을 보았다. 그것은 두 항짜리 절단이라 $T^2$ 이상의 장애를 담지 못하고, ring morphism의 사슬 $A\rightarrow B\rightarrow C$에 대하여 오른쪽에서만 exact한 transition exact sequence밖에 주지 못하며, base change가 $\otimes$의 non-exactness 때문에 어긋난다. 이 세 결함은 모두 같은 뿌리를 가진다. $\Omega$와 $\operatorname{NL}$은 tensor product와 quotient라는 non-exact한 연산을 그 유도된 형태로 다루지 못하고, 오직 $0$차 근사만을 붙든다는 것이다.

우리는 이 글에서 그 뿌리를 직접 교정한다. 곧 commutative ring 자체를 homotopy 이론적으로 정련하여, Tor가 처음부터 내장된 대상인 *animated (simplicial) commutative ring*을 도입한다. 그 무대 위에서 tensor product는 자동으로 유도 tensor product $\otimes^{\mathbb{L}}$이 되고, polynomial algebra에 의한 한 번의 presentation은 simplicial 자유 분해로 승격되며, 그 미분을 취해 얻는 완전한 여접 복합체 $L_{B/A}$가 모든 degree에서 homology를 갖고 추이 삼각형을 만족하게 된다. 이하에서 별다른 언급이 없으면 모든 ring은 commutative이고 unital이며, $k$는 field이다.

## Simplicial 대상과 Dold–Kan 대응

Homotopy 이론적 정련의 출발점은 대상을 하나의 고정된 집합이나 모듈이 아니라, 첨자 위에서 정합적으로 붙은 대상들의 열, 곧 *simplicial* 대상으로 보는 것이다. 그 첨자를 지배하는 것이 다음의 조합적 범주이다.

::: 정의 1
*단체 첨자 범주<sub>simplicial index category</sub>* $\Delta$는 대상이 각 정수 $n\geq0$에 대한 finite ordered set $[n]=\{0<1<\cdots<n\}$이고, morphism이 순서를 보존하는 함수인 범주이다. 범주 $\mathcal{C}$에서의 *simplicial object<sub>단체 대상</sub>*란 functor $X:\Delta^{\op}\rightarrow\mathcal{C}$를 뜻하며, $X_n=X([n])$이라 적는다. $\mathcal{C}=\Set$일 때 이를 *simplicial set<sub>단체 집합</sub>*, $\mathcal{C}$가 $A$-module들의 범주일 때 *simplicial module<sub>단체 가군</sub>*이라 부른다.

$\Delta$의 morphism은 $i$번째 원소를 건너뛰는 단사 *coface<sub>여면</sub>* $\delta^i:[n-1]\rightarrow[n]$과 $i$번째 원소를 겹치는 전사 *codegeneracy<sub>여퇴화</sub>* $\sigma^i:[n+1]\rightarrow[n]$으로 생성되므로, simplicial object $X$는 그 image $X_n$들과 함께 *face map<sub>면 사상</sub>* $d_i=X(\delta^i):X_n\rightarrow X_{n-1}$과 *degeneracy map<sub>퇴화 사상</sub>* $s_i=X(\sigma^i):X_n\rightarrow X_{n+1}$ ($0\leq i\leq n$)으로 완전히 결정되며, 이들은 *simplicial identity<sub>단체 항등식</sub>*, 곧 face 사이의 $d_id_j=d_{j-1}d_i$ ($i<j$), face와 degeneracy 사이의 $d_is_j=s_{j-1}d_i$ ($i<j$)와 $d_js_j=d_{j+1}s_j=\id$와 $d_is_j=s_jd_{i-1}$ ($i>j+1$), 그리고 degeneracy 사이의 $s_is_j=s_{j+1}s_i$ ($i\leq j$)를 만족한다.
:::

직관적으로 $X_n$은 "$n$-단체들의 모임"이고, face map은 한 단체의 $i$번째 face를 취하며, degeneracy map은 낮은 차원의 단체를 퇴화한 높은 차원 단체로 밀어 넣는다. Ring이나 module 같은 대수적 대상 $\mathcal{C}$에서의 simplicial object는 이렇게 조합적으로 얽힌 대상들의 열로서, 하나의 대상만으로는 볼 수 없는 higher homotopy 정보를 실어 나른다. Simplicial module의 경우 이 정보는 놀랍도록 깔끔한 대수적 형태로 번역되는데, 그 다리가 normalization 사슬 복합체이다.

::: 정의 2
Simplicial $A$-module $M$에 대하여, 각 $n$에서 degeneracy들의 image가 생성하는 부분모듈 $D_n=\sum_{i=0}^{n-1}\im(s_i)\subseteq M_n$을 잡고, *normalization 사슬 복합체<sub>normalized chain complex</sub>* $N(M)$를

$$N(M)_n=M_n/D_n,\qquad \partial=\sum_{i=0}^{n}(-1)^id_i:N(M)_n\rightarrow N(M)_{n-1}$$

로 정의한다. 이는 non-negatively graded, 곧 connective한 사슬 복합체이다.
:::

여기서 교대합 $\sum(-1)^id_i$가 $D_n$을 $D_{n-1}$로 보내 quotient 위에 잘 내려오고 $\partial^2=0$이 simplicial identity로부터 따르는 것은 직접 확인된다 ([\[호몰로지 대수학\] §호몰로지](/ko/math/homological_algebra/homology)의 사슬 복합체 형식). $N(M)_n$은 동형으로 $\bigcap_{i=0}^{n-1}\ker(d_i)\subseteq M_n$과 일치하며, 이 부분모듈 위에서 $\partial$은 남은 마지막 face $(-1)^nd_n$으로 주어진다. Normalization이 담아내는 정보가 얼마나 손실 없는지를 말해 주는 것이 다음의 고전적 정리이다.

::: 정리 3 (Dold–Kan)
Normalization 사슬 복합체 functor는 simplicial $A$-module들의 범주와 connective 사슬 복합체들의 범주 사이의 범주 동치

$$N:\operatorname{sMod}_A\overset{\sim}{\longrightarrow}\operatorname{Ch}_{\geq0}(A)$$

를 준다. 더욱이 이 동치는 simplicial homotopy를 사슬 homotopy로, 따라서 약한 동치를 quasi-isomorphism으로 대응시킨다.
:::
::: 증명
Inverse functor $\Gamma:\operatorname{Ch}_{\geq0}(A)\rightarrow\operatorname{sMod}_A$를 명시적으로 구성한다. Connective 복합체 $C$에 대하여

$$\Gamma(C)_n=\bigoplus_{[n]\twoheadrightarrow[k]}C_k$$

로 두는데, 여기서 direct sum은 $\Delta$의 모든 전사 $\eta:[n]\rightarrow[k]$ 위에서 취한다. Simplicial 구조는 $\Delta$의 임의의 morphism을 (단사)$\circ$(전사)로 유일하게 분해하는 성질과 $C$의 미분을 사용하여 정의한다. $N\circ\Gamma\cong\id$은 정의상 곧바로 나오고, $\Gamma\circ N\cong\id$은 각 $M_n$이 그 normalization 조각들의 direct sum $M_n\cong\bigoplus_{\eta:[n]\twoheadrightarrow[k]}N(M)_k$로 분해된다는 사실, 곧 *Eilenberg–Zilber decomposition* 또는 Moore 분해로부터 나온다. 이 direct sum decomposition은 degeneracy들이 서로 독립적으로 image를 채운다는 조합적 관찰에서 귀납적으로 세워진다. Homotopy의 대응은 두 functor가 모두 텐서-hom adjoint 구조를 보존함으로부터 따르며, 자세한 구성은 ([Qui], [Stacks, Simplicial Methods])에 있다.
:::

Dold–Kan 대응은 이 글의 전략 전체를 떠받친다. Simplicial module이라는 homotopy 이론적 대상이 connective 사슬 복합체라는 순수 대수적 대상과 완전히 같은 정보를 담으므로, 우리는 이후 simplicial 분해와 사슬 복합체를 자유롭게 오갈 수 있다. 특히 뒤에서 여접 복합체를 simplicial 분해로 정의하면서도 그 결과를 derived category $D(B)$의 한 대상으로 읽을 수 있는 것이 바로 이 대응 덕분이다 ([\[호몰로지 대수학\] §유도카테고리](/ko/math/homological_algebra/derived_categories)).

## Animated 가환환

이제 대수적 대상을 정련할 차례이다. 우리가 원하는 것은 commutative ring들의 범주를, 그 안에서 tensor product와 quotient가 자동으로 유도된 형태를 취하는 더 큰 범주로 확장하는 것이다. 그 extension의 원리는 "자유 대상은 그대로 두고, 그 밖의 모든 것은 자유 대상들의 homotopy colimit으로 다시 세운다"는 것이다. 여기서 자유 대상이란 polynomial ring이다.

::: 정의 4
$k$ 위의 finitely generated polynomial ring들이 이루는 범주를 $\operatorname{Poly}_k$라 하자. *animated commutative ring<sub>애니메이트 가환환</sub>*들의 $\infty$-범주 $\operatorname{Ani}(\mathrm{CRing}_k)$은 $\operatorname{Poly}_k$의 *sifted colimit completion*, 곧 sifted colimit에 대해 닫혀 있으면서 $\operatorname{Poly}_k$를 compact projective generator로 갖는 가장 작은 $\infty$-범주로 정의된다. 동치로, 이는 simplicial commutative $k$-algebra들에 약한 동치의 역을 형식적으로 붙여 얻는 $\infty$-범주이다.

$\operatorname{Poly}_k$에서의 대상, 곧 $k[\x_1,\ldots,\x_n]$을 *free animated ring<sub>자유 애니메이트 환</sub>*이라 부른다. 일반적으로 집합 $S$에 대한 free animated ring은 $S$가 첨자하는 변수들의 polynomial ring $k[\x_s]_{s\in S}$이며, 이는 밑범주로의 forgetful functor의 왼쪽 수반이 주는 자유 대상이다 ([\[범주론\] §수반함자](/ko/math/category_theory/adjoints)).
:::

이 정의의 요체는 "polynomial ring은 이미 완벽하므로 손대지 않고, 나머지 ring은 polynomial ring들의 정합적 colimit으로 재구성한다"는 *nonabelian derived functor<sub>비아벨 유도 함자</sub>*의 철학이다. 한 ordinary ring $B$를 이 $\infty$-범주 안에서 보려면, $B$를 free animated ring들의 simplicial diagram $P_\bullet$의 homotopy colimit으로 실현한다. Sifted colimit을 요구하는 이유는 정확히 이것인데, 유한곱과 정합적인 colimit인 sifted colimit만이 대수 구조 (곱셈)를 colimit 뒤에도 보존하기 때문이다 ([\[범주론\] §극한](/ko/math/category_theory/limits)의 colimit 개념). 실용적으로는 Dold–Kan 대응을 통해, animated $k$-algebra를 "각 항이 polynomial ring인 simplicial commutative ring $P_\bullet$"으로 다루어도 무방하다.

Animated ring $R$의 밑에 깔린 simplicial set (또는 Dold–Kan을 통한 connective 복합체)의 homotopy가 그 대상의 가장 기본적인 불변량이다.

::: 정의 5
Animated ring $R$을 simplicial commutative ring $R_\bullet$으로 실현했을 때, 그 밑에 깔린 simplicial abelian group의 *homotopy group*

$$\pi_i(R)=H_i\bigl(N(R_\bullet)\bigr)\qquad(i\geq0)$$

을 $R$의 homotopy group이라 부른다. Animated ring morphism $f:R\rightarrow S$가 *약한 동치<sub>weak equivalence</sub>*라는 것은 모든 $i$에 대하여 $\pi_i(f):\pi_i(R)\rightarrow\pi_i(S)$가 isomorphism인 것, 곧 $f$가 $\pi_\ast$-isomorphism인 것을 뜻한다.
:::

$\pi_i(R)$는 Dold–Kan 대응에 의하여 normalization 복합체 $N(R_\bullet)$의 $i$번째 homology이므로, 실현 $R_\bullet$의 선택에 약한 동치를 무시하면 무관한 불변량이다. 특히 $\pi_0$은 $R$이 나르는 "고전적 그림자"에 해당하고, 높은 $\pi_i$들은 ordinary ring에는 없던 순수 homotopy 정보이다. 다음 명제는 이 정보들이 어떤 대수 구조를 이루는지 밝힌다.

::: 명제 6
Animated ring $R$에 대하여 $\pi_0(R)$은 자연스럽게 ordinary commutative ring이 되고, 각 $\pi_i(R)$ ($i\geq1$)은 $\pi_0(R)$-module이 된다. Ordinary ring은 정확히 $\pi_i=0$ ($i\geq1$)인 animated ring, 곧 *discrete*한 animated ring으로서 $\operatorname{Ani}(\mathrm{CRing}_k)$에 완전 충실하게 들어간다.
:::
::: 증명
$R_\bullet$을 $R$의 실현이라 하자. $\pi_0(R)=\coker(d_0-d_1:R_1\rightarrow R_0)=R_0/{\sim}$는 $R_0$의 곱셈을 $R_1$이 주는 동치관계로 quotient한 것인데, $d_0,d_1$이 모두 ring homomorphism이므로 이 동치관계는 곱셈과 합에 대해 닫혀 있고, 따라서 $\pi_0(R)$이 commutative ring 구조를 물려받는다. 각 $\pi_i(R)$ 위의 $\pi_0(R)$-action은 다음과 같이 준다. $R_\bullet$의 곱셈은 simplicial abelian group morphism $R_\bullet\otimes R_\bullet\rightarrow R_\bullet$을 주고, 이것이 homotopy 위에 $\pi_0(R)\otimes\pi_i(R)\rightarrow\pi_i(R)$을 유도하며 (Eilenberg–Zilber를 통한 곱), 결합법칙과 단위원 조건이 이 action을 module 구조로 만든다. Discrete 대상의 완전 충실성은, 두 ordinary ring 사이의 animated morphism 공간 $\operatorname{Map}(R,S)$가 $\pi_0(S)=S$이고 higher homotopy가 소멸하여 discrete set $\Hom(R,S)$로 축약됨으로부터 나온다. 자세한 논의는 ([Lur, HA], [Toë])에 있다.
:::

이 명제는 animated ring이 ordinary ring의 진정한 extension임을 확립한다. $\pi_0(R)$은 옛 ring을 그대로 복원하고, $\pi_{\geq1}(R)$은 그 위에 얹힌 새로운 higher 정보이며, discrete 대상만 볼 때 이 이론은 고전적 가환대수로 정확히 되돌아온다. 이제 이 확장된 무대에서 tensor product가 무엇이 되는지를 본다.

## 유도 텐서곱

Ordinary ring들의 범주에서 두 $A$-algebra $B,C$의 tensor product $B\otimes_AC$는 $A$ 아래에서의 pushout, 곧 coproduct이다. Animated 범주는 이 보편 성질을 그대로 물려받되, colimit을 homotopy colimit으로 해석한다.

::: 정의 7
$A$-algebra $B,C$에 대하여, 그 *유도 tensor product<sub>derived tensor product</sub>* $B\otimes_A^{\mathbb{L}}C$는 animated ring들의 $\infty$-범주에서의 homotopy pushout

$$B\otimes_A^{\mathbb{L}}C=B\amalg_AC$$

으로 정의되는 animated ring이다. 구체적으로 $B$를 free simplicial $A$-algebra $P_\bullet\overset{\sim}{\rightarrow}B$로 분해하면 $B\otimes_A^{\mathbb{L}}C$는 $P_\bullet\otimes_AC$로 실현된다.
:::

{% diagram Math/Derived_Algebraic_Geometry/Animated_Rings-1.svg width="8.24em" alt="유도 tensor product의 homotopy pushout" %}

위 사각형은 ordinary pushout 사각형과 형태가 같지만, 오른쪽 아래 모서리가 homotopy pushout이라는 점에서 다르다. Free resolution $P_\bullet\rightarrow B$의 각 항이 polynomial $A$-algebra이므로 $P_n\otimes_AC$는 $C$ 위의 polynomial algebra이고, 따라서 $P_\bullet\otimes_AC$는 다시 free simplicial $C$-algebra가 되어 그 homotopy가 잘 정의된다. 이 유도된 연산이 classical tensor product와 어떻게 갈라지는지는 곧바로 homotopy group으로 읽힌다.

::: 명제 8
Ordinary $A$-algebra $B,C$에 대하여, 유도 tensor product의 homotopy group은 Tor로 주어진다.

$$\pi_n\bigl(B\otimes_A^{\mathbb{L}}C\bigr)\cong\Tor_n^A(B,C)\qquad(n\geq0)$$

특히 $\pi_0(B\otimes_A^{\mathbb{L}}C)=B\otimes_AC$는 classical tensor product이고, $B$나 $C$ 중 하나가 $A$ 위에서 flat이면 higher homotopy가 모두 소멸하여 유도 tensor product는 classical tensor product와 약하게 동치이다.
:::
::: 증명
$P_\bullet\overset{\sim}{\rightarrow}B$를 free simplicial $A$-algebra 분해라 하면 [정의 7](#def7)에 의하여 $B\otimes_A^{\mathbb{L}}C=P_\bullet\otimes_AC$이고, 그 homotopy는 Dold–Kan에 의하여 normalization 복합체 $N(P_\bullet\otimes_AC)=N(P_\bullet)\otimes_AC$의 homology이다. 각 $P_n$은 polynomial $A$-algebra이므로 free, 따라서 flat $A$-module이고, $P_\bullet\rightarrow B$가 약한 동치이므로 $N(P_\bullet)$은 $B$의 flat $A$-module 분해이다. 그럼 [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 2](/ko/math/homological_algebra/ext_and_tor#def2)의 $\Tor$ 정의에 의하여

$$\pi_n(P_\bullet\otimes_AC)=H_n\bigl(N(P_\bullet)\otimes_AC\bigr)=\Tor_n^A(B,C)$$

이다. $n=0$일 때 $\Tor_0^A(B,C)=B\otimes_AC$이고, $B$ 또는 $C$가 flat이면 $\Tor_n^A(B,C)=0$ ($n\geq1$)이므로 유도 tensor product가 discrete해져 classical tensor product와 약하게 동치이다.
:::

곧 유도 tensor product는 classical tensor product를 $\pi_0$으로 복원하면서, 그 위에 $\Tor$를 higher homotopy로 자동으로 실어 나른다. 이것이 "Tor가 처음부터 내장되었다"는 말의 정확한 의미이다. 이 현상의 가장 깨끗한 사례는 한 점을 자기 자신과 유도적으로 교차시킬 때 나타난다.

::: 예시 9 (점의 유도 자기교차)
$A=k[\x]$ 위에서 원점의 coordinate ring $k=k[\x]/(\x)$을 자기 자신과 유도적으로 텐서한 $k\otimes_{k[\x]}^{\mathbb{L}}k$를 계산한다. $\x$는 $k[\x]$의 nonzerodivisor이므로, [\[호몰로지 대수학\] §Ext와 Tor, ⁋정의 7](/ko/math/homological_algebra/ext_and_tor#def7)의 Koszul resolution

$$0\longrightarrow k[\x]\overset{\times\x}{\longrightarrow}k[\x]\longrightarrow k\longrightarrow0$$

이 $k$의 free $k[\x]$-module 분해를 준다. 여기에 $-\otimes_{k[\x]}k$를 적용하면 곱셈 $\times\x$가 $0$으로 가므로 미분이 사라진 복합체 $[k\overset{0}{\rightarrow}k]$를 얻고, 따라서

$$\pi_n\bigl(k\otimes_{k[\x]}^{\mathbb{L}}k\bigr)=\Tor_n^{k[\x]}(k,k)=\begin{cases}k&n=0,1\\0&n\geq2\end{cases}$$

이다. 곧 유도 tensor product는 degree $0,1$에 각각 $k$를 갖는 nondiscrete animated ring이며, 그 homotopy ring은 하나의 degree $1$ generator $\varepsilon$이 만드는 exterior algebra

$$\pi_\ast\bigl(k\otimes_{k[\x]}^{\mathbb{L}}k\bigr)\cong\Lambda_k[\varepsilon],\qquad \lvert\varepsilon\rvert=1$$

이다 (같은 Koszul 계산이 $\Tor_\ast^{k[\x]}(k,k)=\bigwedge_k(k)$를 준다). 고전적으로는 $k\otimes_{k[\x]}k=k$뿐이므로, 두 원점의 교차는 그저 한 점으로 보인다. 그러나 유도 tensor product는 $\pi_1=k\neq0$이라는 초과 정보를 붙드는데, 이는 affine 직선 $\Spec k[\x]$ 안에서 원점을 자기 자신과 겹칠 때 생기는 excess intersection을 재는 것으로, 이 대수적 그림자가 뒤에서 다룰 derived intersection의 기하로 이어진다.
:::

## 완전한 여접 복합체

이제 목표였던 여접 복합체를 구성한다. Naive 여접 복합체는 $B$를 polynomial algebra의 quotient로 한 번 표현한 뒤 conormal sequence의 두 항을 취한 것이었다 ([\[가환대수학\] §미분, ⁋정의 10](/ko/math/commutative_algebra/differentials#def10)). 완전한 여접 복합체는 그 "한 번의 표현"을 simplicial 자유 분해로 승격하여, Kähler differential을 각 항에서 취한 뒤 normalize한다.

::: 정의 10
$A$-algebra $B$에 대하여, 각 항 $P_n$이 polynomial $A$-algebra이고 약한 동치 $P_\bullet\overset{\sim}{\rightarrow}B$를 이루는 free simplicial 분해를 택하자 (곧 $\pi_0(P_\bullet)=B$, $\pi_{>0}(P_\bullet)=0$). 이때 $B$의 $A$ 위에서의 *cotangent complex<sub>여접 복합체</sub>* $L_{B/A}$는 각 항의 Kähler differential을 $B$로 base change한 simplicial $B$-module

$$L_{B/A}=\Omega_{P_\bullet/A}\otimes_{P_\bullet}B$$

를 Dold–Kan 대응을 통해 connective 복합체로 본 것, 곧 derived category $D(B)$의 대상이다.
:::

각 $P_n$이 polynomial algebra이므로 $\Omega_{P_n/A}$는 free $P_n$-module이고, 따라서 $\Omega_{P_n/A}\otimes_{P_n}B$는 free $B$-module이다. 곧 $L_{B/A}$는 각 degree에서 free인 connective 복합체로 실현되며, naive 여접 복합체가 하나의 presentation만 쓴 것과 달리 모든 higher degree에 항을 가진다. 이 구성이 의미를 가지려면 분해의 선택에 무관해야 하고, 낮은 degree에서 옛 불변량을 복원해야 한다.

::: 정리 11
[정의 10](#def10)의 $L_{B/A}\in D(B)$는 free simplicial resolution $P_\bullet\rightarrow B$의 선택에 quasi-isomorphism을 무시하면 무관하다. 나아가

$$H_0(L_{B/A})\cong\Omega_{B/A}$$

이고, degree $1$ 이하의 절단은 naive 여접 복합체와 일치한다.

$$\tau_{\leq1}L_{B/A}\simeq\operatorname{NL}_{B/A}$$
:::
::: 증명
무관성은 두 free simplicial resolution 사이에 언제나 세 번째 공통 정련이 존재하고, [\[가환대수학\] §미분, ⁋정리 14](/ko/math/commutative_algebra/differentials#thm14)이 각 단계에서 준 homotopy 무관성을 simplicial degree 전체에 걸쳐 정합적으로 이어 붙임으로써 나온다. 곧 $L_{B/A}$는 abelianization functor의 왼쪽 유도 functor (nonabelian derived functor)로서 잘 정의되며, cofibrant 분해의 선택에 무관하다.

$H_0$의 계산은 다음과 같다. $\Omega_{P_\bullet/A}\otimes_{P_\bullet}B$의 normalization 복합체에서 $H_0$은 $\Omega_{P_0/A}\otimes_{P_0}B$를 두 face의 image로 quotient한 것인데, $P_0\rightarrow B$가 전사이고 $P_1$이 relation들을 준다는 점에서 이는 정확히 conormal sequence의 cokernel, 곧 [\[가환대수학\] §미분, ⁋명제 11](/ko/math/commutative_algebra/differentials#prop11)에서와 같은 $\Omega_{B/A}$이다. 마지막으로 $P_\bullet$의 처음 두 항 $P_1\rightrightarrows P_0\rightarrow B$만 남겨 절단하면 그로부터 얻는 두 항 복합체가 $\operatorname{NL}_{B/A}$의 정의와 일치하므로 $\tau_{\leq1}L_{B/A}\simeq\operatorname{NL}_{B/A}$이다. 완전한 논증은 ([Qui], [Ill], [Stacks, Cotangent Complex])에 있다.
:::

곧 완전한 여접 복합체는 naive 여접 복합체의 정보를 낮은 degree에서 그대로 담으면서, 그 위에 higher homology를 얹은 대상이다. 이 higher homology가 있어야만 비로소 변형이론이 요구했던 추이 삼각형이 성립한다.

::: 정리 12 (추이 삼각형)
Ring morphism의 사슬 $A\rightarrow B\rightarrow C$에 대하여, $D(C)$ 안의 distinguished triangle

$$L_{B/A}\otimes_B^{\mathbb{L}}C\longrightarrow L_{C/A}\longrightarrow L_{C/B}\longrightarrow L_{B/A}\otimes_B^{\mathbb{L}}C[1]$$

이 존재한다. 특히 전사 $B\rightarrow C=B/I$에 대하여 $H_0(L_{C/B})=0$이고

$$H_1(L_{C/B})\cong I/I^2$$

이며, $I$가 국소적으로 regular sequence로 생성되는 경우 (곧 $B\rightarrow C$가 quasi-smooth, lci인 경우) 여접 복합체는 conormal module의 shift

$$L_{C/B}\simeq (I/I^2)[1]$$

로 집중된다.
:::
::: 증명
삼각형은 free simplicial 분해의 base change로부터 나온다. $P_\bullet\rightarrow B$를 $A$ 위의 free resolution, $Q_\bullet\rightarrow C$를 $B$ 위의 free 분해로 잡고 이들을 합성하여 $C$의 $A$ 위 free 분해를 구성하면, 각 simplicial degree에서 [\[다중선형대수학\] §미분가군, ⁋명제 13](/ko/math/multilinear_algebra/differential_modules#prop13)의 transition exact sequence가 split short exact sequence가 되고 (polynomial algebra 사이의 morphism이므로), 이를 normalize하면 short exact sequence들의 열이 사슬 복합체들의 short exact sequence를 이루어 그 long exact sequence가 위 삼각형이 된다. 오른쪽에서만 exact했던 옛 transition exact sequence가 이렇게 완전한 삼각형으로 승격되는 것이 완전한 여접 복합체를 도입한 핵심 동기였다 ([\[스킴\] §변형이론과 여접 복합체, ⁋참고 12](/ko/math/scheme_theory/deformation_theory#rmk12)).

전사 $B\rightarrow C=B/I$의 경우 $\Omega_{C/B}=0$이므로 $H_0(L_{C/B})=0$이고, $H_1(L_{C/B})=I/I^2$은 conormal module이 여접 복합체의 첫 nonzero homology로 나타남을 말한다. $I=(f_1,\ldots,f_r)$이 regular sequence이면 Koszul 분해가 $C$의 free 분해를 주고, 그 미분을 취한 여접 복합체가 정확히 $(I/I^2)[1]$ 한 항으로 축약된다. 세부는 ([Qui], [Ill])에 있다.
:::

추이 삼각형은 여접 복합체를 실제로 계산 가능한 대상으로 만든다. 임의의 $B$를 polynomial algebra 위의 quotient로 놓으면, smooth한 부분의 여접 복합체는 이미 알고 있고, quotient에서 오는 conormal 부분을 삼각형이 이어 붙여 주기 때문이다. 이를 곧바로 하나의 fat point에 적용해 본다.

::: 예시 13 (이중점의 여접 복합체)
$B=k[\x]/(\x^2)$, 곧 affine 직선 위 원점의 이중점을 생각하고, $k$의 characteristic이 $2$가 아니라 하자. 사슬 $k\rightarrow k[\x]\rightarrow B$에 [정리 12](#thm12)을 적용한다. $k[\x]$는 $k$ 위에서 smooth하므로 $L_{k[\x]/k}=\Omega_{k[\x]/k}=k[\x]\dd{\x}$는 degree $0$에 집중된 free module이다. 한편 $\x^2$은 $k[\x]$의 nonzerodivisor이므로 $k[\x]\rightarrow B$는 lci이고, [정리 12](#thm12)에 의하여

$$L_{B/k[\x]}\simeq(I/I^2)[1]\simeq B[1],\qquad I=(\x^2)$$

이다. 따라서 여접 복합체는 두 항짜리 free 복합체로 실현되며, 그 미분은 conormal morphism $\overline{d}:B[1]\rightarrow(k[\x]\dd{\x})\otimes B=B\dd{\x}$, 곧 $\overline{\x^2}\mapsto \dd{(\x^2)}=2\x \dd{\x}$이다. 곧

$$L_{B/k}\simeq\Bigl[B\overset{\times2\x}{\longrightarrow}B\dd{\x}\Bigr]$$

이고 (degree $1$에서 $0$으로), 그 homology는 $k$의 characteristic이 $2$가 아닐 때

$$H_0(L_{B/k})=\coker(\times2\x)=B/(\x)=k\cong\Omega_{B/k},\qquad H_1(L_{B/k})=\ker(\times2\x)=\ann_B(\x)=(\x)\cong k$$

이다. 곧 여접 복합체가 degree $0$을 넘어 $H_1\neq0$을 가진다. 이는 $B$가 $k$ 위에서 smooth가 아님을 정확히 검출하는 것으로, 이중점이라는 비축소 (nilpotent) 특이성이 $\Omega$만으로는 보이지 않던 higher homology로 드러난 것이다. Hypersurface이므로 여접 복합체 자체는 두 항짜리 perfect 복합체에 그쳐 $H_{\geq2}=0$이지만, $H_1$의 소멸 실패만으로도 non-smoothness는 이미 포착된다.
:::

이중점의 계산은 여접 복합체의 higher homology가 smoothness의 정확한 판정자임을 시사한다. 이를 일반 명제로 굳혀 이 글을 맺는다.

::: 명제 14 (매끄러움의 판정)
유한표현 $A$-algebra $B$에 대하여, 다음이 동치이다.

1. $B$가 $A$ 위에서 smooth하다.
2. $L_{B/A}$가 degree $0$에 집중되어 있고, $H_0(L_{B/A})=\Omega_{B/A}$가 finitely generated projective $B$-module이다.
:::
::: 증명
$(1)\Rightarrow(2)$. $B$가 smooth하면 [\[스킴\] §변형이론과 여접 복합체, ⁋명제 8](/ko/math/scheme_theory/deformation_theory#prop8)에 의하여 $H_1(\operatorname{NL}_{B/A})=0$이고 $\Omega_{B/A}$가 finitely generated projective이다. 국소적으로 $B$는 $A$ 위의 polynomial algebra $P$ 위에서 étale하다. Étale morphism $P\rightarrow B$는 $L_{B/P}\simeq0$을 주므로, 사슬 $A\rightarrow P\rightarrow B$에 [정리 12](#thm12)을 적용하면 $L_{B/A}\simeq L_{P/A}\otimes_P^{\mathbb{L}}B$를 얻는다. $P$는 $A$ 위에서 polynomial algebra이므로 $L_{P/A}\simeq\Omega_{P/A}$가 degree $0$에 집중된 free module이고, $P\rightarrow B$가 étale하여 $\Omega_{P/A}\otimes_PB\cong\Omega_{B/A}$이므로 $L_{B/A}\simeq\Omega_{B/A}$도 degree $0$에 집중된다.

$(2)\Rightarrow(1)$. $L_{B/A}$가 degree $0$에 집중되면 [정리 11](#thm11)에 의하여 $\tau_{\leq1}L_{B/A}=\operatorname{NL}_{B/A}$도 degree $0$에 집중되어 $H_1(\operatorname{NL}_{B/A})=0$이고, $H_0=\Omega_{B/A}$가 finitely generated projective이다. 그럼 [\[스킴\] §변형이론과 여접 복합체, ⁋명제 8](/ko/math/scheme_theory/deformation_theory#prop8)의 증명에서 본 대로, conormal exact sequence가 왼쪽에서도 split하는 short exact sequence가 되어 infinitesimal lifting 판정이 성립하고, 이는 $B$가 $A$ 위에서 smooth한 것과 동치이다. 완전한 논증은 ([Qui], [Stacks, Cotangent Complex])에 있다.
:::

이로써 여접 복합체는 변형이론이 요구한 세 가지, 곧 모든 degree에서의 homology, 추이 삼각형, 그리고 유도 tensor product와의 정합성을 모두 만족하는 대상으로 완성되었다. Smoothness는 이 복합체가 가장 단순해지는 경우 (degree $0$의 projective module)로, 특이성은 그 higher homology로 정확히 측정된다. Animated ring과 그 위의 여접 복합체는 이렇게 고전 가환대수를 homotopy 이론적으로 정련한 무대이며, 이 무대 위에서 quotient와 교차를 유도적으로 다루는 것이 derived algebraic geometry의 출발점이다.

---

**참고문헌**

**[Qui]** D. Quillen, *Homotopical algebra*, Lecture Notes in Mathematics 43, Springer, 1967. 또한 *On the (co-)homology of commutative rings*, Proc. Sympos. Pure Math. 17 (1970), 65–87.  
**[Ill]** L. Illusie, *Complexe cotangent et déformations I, II*, Lecture Notes in Mathematics 239, 283, Springer, 1971–1972.  
**[Lur]** J. Lurie, *Higher algebra* 및 *Higher topos theory*, [www.math.ias.edu/~lurie](https://www.math.ias.edu/~lurie).  
**[Toë]** B. Toën, *Derived algebraic geometry*, EMS Surveys in Mathematical Sciences 1 (2014), 153–240.  
**[Stacks]** The Stacks project authors, *The Stacks project*, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
