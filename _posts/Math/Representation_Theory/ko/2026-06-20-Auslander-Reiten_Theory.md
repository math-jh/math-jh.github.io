---
title: "Auslander–Reiten 이론"
description: "유한차원 대수 위의 module category에서 irreducible morphism을 section도 retraction도 아니면서 분해되지 않는 사상으로 정의하고, left/right almost split morphism과 almost split (Auslander–Reiten) sequence 0→A→B→C→0를 도입하여 그 본질적 유일성을 증명한다. Transpose Tr를 minimal projective presentation으로부터, duality D=Hom_k(−,k)와 함께 AR translate τ=D Tr를 구성하고, 각 non-projective indecomposable C에 대하여 끝점이 C이고 시작점이 τC인 almost split sequence가 존재한다는 Auslander–Reiten 정리를 진술한다. 선형 A_3 quiver에 대하여 Auslander–Reiten quiver를 구체적으로 계산한다."
excerpt: "Irreducible morphism, almost split sequence, AR translate τ=D Tr, Auslander–Reiten quiver"

categories: [Math / Representation Theory]
permalink: /ko/math/representation_theory/auslander_reiten
sidebar: 
    nav: "representation_theory-ko"

date: 2026-06-20
weight: 12

published: false

---

앞선 글에서 우리는 유한차원 $$kQ$$-module이 indecomposable들의 직합으로 본질적으로 유일하게 분해됨을 보았다 ([§Krull–Schmidt 정리, ⁋정리 6](/ko/math/representation_theory/krull_schmidt#thm6)). 이로써 유한차원 representation을 이해하는 문제는 indecomposable들을 분류하고, 그들 사이의 morphism을 기술하는 문제로 환원된다. *Auslander–Reiten 이론*은 후자에 대한 체계적인 답을 제공한다. 핵심 발상은 indecomposable들 사이의 모든 morphism이 가장 기본적인 morphism, 곧 *irreducible morphism*들의 합성으로 생성된다는 것이며, 이 irreducible morphism들을 표준적인 짧은 완전열인 *almost split sequence*로 한꺼번에 포착하는 것이다. 이 자료를 그래프로 정리한 것이 *Auslander–Reiten quiver*이고, 이 quiver는 module category의 구조를 시각적으로 압축한다.

이 글에서 $$A$$는 field $$k$$ 위의 유한차원 결합대수이고, module이라 하면 별다른 언급이 없는 한 유한차원 left $$A$$-module을 뜻한다. 이러한 module들이 이루는 category를 $$\operatorname{mod} A$$로 적는다. Path algebra $$kQ$$가 $$Q$$에 oriented cycle이 없을 때 유한차원이므로 ([§Quiver와 경로대수, ⁋명제 5](/ko/math/representation_theory/path_algebras#prop5)), $$A=kQ$$인 경우가 우리의 주된 관심사이며, 이때 $$\operatorname{mod} A$$는 유한차원 representation들의 category $$\Rep(Q)$$와 동치이다 ([§Quiver와 경로대수, ⁋정리 12](/ko/math/representation_theory/path_algebras#thm12)). 유한차원성 덕분에 모든 module은 유한 길이를 가지며, 따라서 Krull–Schmidt 정리가 적용된다. $$M,N$$이 module일 때 $$\Hom_A(M,N)$$은 $$A$$-linear 사상들의 $$k$$-벡터공간이고, $$M$$이 indecomposable이면 $$\End_A(M)$$은 local ring이다 ([§Krull–Schmidt 정리, ⁋따름정리 4](/ko/math/representation_theory/krull_schmidt#cor4)).

## Irreducible morphism

Indecomposable들 사이의 morphism 가운데 어떤 것이 가장 기본적인가를 먼저 결정한다. Isomorphism은 분류의 관점에서 자명하고, 둘로 쪼개지는 morphism, 곧 split monomorphism이나 split epimorphism도 직합의 포함·사영에 다름 아니므로 새로운 정보를 담지 않는다. 우리는 이들을 제외한 뒤, 비자명한 방식으로 더 작은 morphism들의 합성으로 분해되지 않는 morphism을 골라낸다. 여기서 *section*은 left inverse를 가지는 morphism(split monomorphism), *retraction*은 right inverse를 가지는 morphism(split epimorphism)을 뜻한다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$A$$-module 사상 $$f:M\rightarrow N$$이 *irreducible<sub>기약</sub>*이라는 것은 다음 두 조건이 성립하는 것이다.

1. $$f$$는 section도 retraction도 아니다.
2. $$f=gh$$로 분해될 때마다, $$h$$가 section이거나 $$g$$가 retraction이다. 곧 $$f$$가 $$M\xrightarrow{h}X\xrightarrow{g}N$$으로 적히면 $$h$$가 split monomorphism이거나 $$g$$가 split epimorphism이다.

</div>

조건 (1)은 $$f$$가 isomorphism이 아닐 뿐 아니라 직합 인자의 포함이나 사영처럼 분해를 동반하지도 않음을 뜻한다. 실제로 irreducible morphism은 자동으로 단사이거나 전사이다. $$f$$의 image $$I=\im f$$를 통하여 $$f$$를 전사 $$M\twoheadrightarrow I$$와 단사 $$I\hookrightarrow N$$의 합성으로 적으면, 조건 (2)에 의하여 둘 중 하나가 split이고, 그러면 $$f$$ 자신이 단사 또는 전사가 되기 때문이다. 조건 (2)는 $$f$$가 더 단순한 두 단계로 비자명하게 쪼개지지 않는다는 *최소성*을 표현한다. 비자명한 분해란 $$h$$가 split mono도 아니고 $$g$$가 split epi도 아닌 분해를 말하며, irreducible morphism은 그러한 분해를 허용하지 않는다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> $$M,N$$이 indecomposable이고 $$f:M\rightarrow N$$이 isomorphism이 아닌 nonzero 사상이라 하자. 그럼 $$f$$가 section이거나 retraction일 수 없다. 따라서 indecomposable 사이의 사상에 대하여 [정의 1](#def1)의 조건 (1)은 "$$f$$가 isomorphism이 아니다"와 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$f:M\rightarrow N$$이 section이라 하자. 그럼 left inverse $$g:N\rightarrow M$$이 있어 $$gf=\id_M$$이다. 이때 $$e=fg\in\End_A(N)$$은 $$e^2=fgfg=f\id_M g=fg=e$$이므로 idempotent이고, $$N=\im e\oplus\ker e$$이다. $$N$$이 indecomposable이므로 $$e=0$$ 또는 $$e=\id_N$$이다. $$e=0$$이면 $$fgf=ef=0$$이지만 $$gf=\id_M$$에서 $$fgf=f$$이므로 $$f=0$$이 되어 $$f\neq 0$$에 모순이다. 따라서 $$e=fg=\id_N$$이고, 이는 $$gf=\id_M$$과 함께 $$f$$가 isomorphism임을 뜻하여 가정에 모순이다.

$$f$$가 retraction인 경우도 대칭적이다. Right inverse $$g:N\rightarrow M$$이 있어 $$fg=\id_N$$이면 $$e=gf\in\End_A(M)$$이 idempotent이고, $$M$$이 indecomposable이므로 $$e=0$$ 또는 $$e=\id_M$$이다. $$e=0$$이면 $$gfg=0$$인데 $$fg=\id_N$$에서 $$gfg=g$$이므로 $$g=0$$, 따라서 $$\id_N=fg=0$$이 되어 $$N\neq 0$$에 모순이다. 따라서 $$e=gf=\id_M$$이고 $$f$$는 isomorphism이어서 가정에 모순이다. 어느 경우에도 모순이 나오므로 $$f$$는 section도 retraction도 아니다.

역으로 $$f$$가 isomorphism이면 $$f$$ 자신이 section이자 retraction이므로 조건 (1)이 깨진다. 따라서 indecomposable 사이에서 조건 (1)은 $$f$$가 isomorphism이 아니라는 것과 같다.

</details>

명제 2는 indecomposable 사이의 morphism을 다룰 때 irreducible morphism의 조건 (1)을 "isomorphism이 아니다"로 단순화할 수 있게 해 준다. 따라서 indecomposable $$M,N$$에 대하여 irreducible morphism $$f:M\rightarrow N$$이란, isomorphism이 아니면서 임의의 분해 $$f=gh$$에서 $$h$$가 split mono이거나 $$g$$가 split epi인 nonzero 사상이다. 이러한 morphism들이 module category에서 "한 칸 떨어진" 가장 가까운 이웃 사이의 사상을 나타내며, Auslander–Reiten quiver의 화살표가 된다.

## Almost split sequence

Irreducible morphism들을 한 module $$C$$ 둘레에서 한꺼번에 포착하기 위하여, $$C$$로 들어오는 모든 비자명한 사상이 단 하나의 사상을 통하여 인수분해되는 표준적인 사상을 찾는다. 이것이 *right almost split morphism*이며, 대칭적으로 *left almost split morphism*도 정의한다.

<div class="definition" markdown="1">

<ins id="def3">**정의 3**</ins> $$A$$-module 사상에 대하여 다음을 정의한다.

1. 사상 $$g:B\rightarrow C$$가 *right almost split*이라는 것은 $$g$$가 retraction이 아니며, retraction이 아닌 임의의 사상 $$h:X\rightarrow C$$가 $$g$$를 통하여 인수분해되는 것이다. 곧 $$h=g h'$$인 $$h':X\rightarrow B$$가 존재한다.
2. 사상 $$f:A\rightarrow B$$가 *left almost split*이라는 것은 $$f$$가 section이 아니며, section이 아닌 임의의 사상 $$h:A\rightarrow Y$$가 $$f$$를 통하여 인수분해되는 것이다. 곧 $$h=h' f$$인 $$h':B\rightarrow Y$$가 존재한다.

짧은 완전열

$$0\longrightarrow A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C\longrightarrow 0$$

이 *almost split sequence*<sub>거의 분할 수열</sub> 또는 *Auslander–Reiten sequence*라는 것은, 이 열이 split하지 않으며, $$f$$가 left almost split이고 $$g$$가 right almost split인 것이다.

</div>

이 정의의 비대칭적 모양에도 불구하고 두 조건은 서로를 강하게 제약한다. $$g$$가 right almost split이고 $$C$$로의 split epimorphism이 아니라는 것은, $$C$$로 가는 모든 사상 가운데 split epi로 들어오지 못하는 것들이 전부 $$B$$를 경유함을 뜻한다. 특히 항등사상 $$\id_C:C\rightarrow C$$는 retraction이지만, $$C$$가 indecomposable일 때 $$C$$의 proper submodule이나 다른 indecomposable로부터 들어오는 비자명한 사상은 모두 $$g$$를 통과한다. Almost split sequence에서 $$A$$와 $$C$$가 자동으로 indecomposable이 됨을 다음에서 확인한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$0\rightarrow A\xrightarrow{f}B\xrightarrow{g}C\rightarrow 0$$이 almost split sequence이면 $$A$$와 $$C$$는 모두 indecomposable이며, $$C$$는 projective가 아니고 $$A$$는 injective가 아니다. 또한 이러한 almost split sequence는 $$C$$에 의하여 isomorphism을 무시하면 유일하게 결정된다. 곧 $$0\rightarrow A'\xrightarrow{f'}B'\xrightarrow{g'}C\rightarrow 0$$이 같은 끝점 $$C$$를 가지는 또 하나의 almost split sequence이면, 세 수직사상이 모두 isomorphism이고 두 사각형이 commute하는 완전열의 동형

![두 almost split sequence 사이의 동형](/assets/images/Math/Representation_Theory/Auslander-Reiten_Theory-1.svg){:style="width:18.58em" class="invert" .align-center}

이 존재한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$C$$가 indecomposable임을 보인다. $$C=C_1\oplus C_2$$가 nonzero 직합이라 하면, 각 인자의 포함 $$\iota_t:C_t\rightarrow C$$ ($$t=1,2$$)는 split mono이고, $$C$$가 nonzero 직합으로 갈라지므로 $$\iota_t$$는 retraction이 아니다. (만일 $$\iota_t$$가 retraction이면 $$\iota_t$$는 전사이자 단사인 isomorphism이 되어 $$C_t=C$$, 곧 다른 인자가 $$0$$이 되어 모순이다.) 따라서 $$\iota_t$$는 $$g$$를 통하여 인수분해되어 $$\iota_t=g\, s_t$$인 $$s_t:C_t\rightarrow B$$가 있다. 이들을 모으면 $$s=(s_1,s_2):C_1\oplus C_2\rightarrow B$$가 $$gs=\id_C$$를 만족하므로 $$g$$가 retraction이 되는데, 이는 almost split sequence가 split하지 않는다는 가정에 모순이다. 따라서 $$C$$는 indecomposable이다. 대칭적으로 $$f$$가 left almost split이라는 조건으로부터 $$A$$가 indecomposable임을 얻는다.

$$C$$가 projective가 아님을 보인다. $$C$$가 projective이면 전사 $$g:B\rightarrow C$$가 분할되어 $$g$$가 retraction이 되는데, 이는 right almost split의 정의에 모순이다. 대칭적으로 $$A$$가 injective이면 단사 $$f:A\rightarrow B$$가 분할되어 $$f$$가 section이 되어 left almost split에 모순이므로, $$A$$는 injective가 아니다.

이제 유일성을 보인다. 두 almost split sequence가 같은 $$C$$로 끝난다 하자. $$g':B'\rightarrow C$$는 retraction이 아니므로 right almost split인 $$g$$를 통하여 $$g'=g\varphi$$로 인수분해되고, 마찬가지로 $$g:B\rightarrow C$$가 $$g=g'\psi$$로 인수분해되어 사상 $$\varphi:B'\rightarrow B$$, $$\psi:B\rightarrow B'$$를 얻는다. 그럼 $$\theta:=\varphi\psi\in\End_A(B)$$가 $$g\theta=g'\psi=g$$를 만족한다. 여기서 $$\theta$$가 automorphism임을 보인다. $$g(\id_B-\theta)=0$$이므로 $$\id_B-\theta$$는 image가 $$\ker g=\im f$$에 들어가며, $$f$$가 단사이므로 유일한 $$\rho:B\rightarrow A$$에 대하여 $$\id_B-\theta=f\rho$$로 적힌다. 곧 $$\theta=\id_B-f\rho$$이다. 합성 $$\rho f\in\End_A(A)$$를 보자. $$A$$가 indecomposable이므로 $$\End_A(A)$$는 local ring이고 ([§Krull–Schmidt 정리, ⁋따름정리 4](/ko/math/representation_theory/krull_schmidt#cor4)), 따라서 $$\rho f$$는 automorphism이거나 nilpotent이다. 만일 $$\rho f$$가 automorphism이면 $$(\rho f)^{-1}\rho$$가 $$f$$의 왼쪽 역이 되어 $$f$$가 section, 곧 split mono가 되는데 이는 $$f$$가 left almost split이라는 데에 모순이다. 따라서 $$\rho f$$는 nilpotent이고, 적당한 $$n$$에 대하여 $$(\rho f)^n=0$$이다. 그럼

$$(f\rho)^{n+1}=f\,(\rho f)^n\,\rho=0$$

이므로 $$f\rho$$는 $$\End_A(B)$$에서 nilpotent이고, 따라서

$$\theta^{-1}=\id_B+(f\rho)+(f\rho)^2+\cdots+(f\rho)^n$$

이 $$\theta=\id_B-f\rho$$의 역이 되어 $$\theta=\varphi\psi$$가 automorphism이다. 대칭적으로, $$g'\psi\varphi=g'$$와 $$f'$$의 단사성을 이용하여 같은 논법을 $$\psi\varphi\in\End_A(B')$$에 적용하면 $$\psi\varphi$$ 또한 automorphism이다. 따라서 $$\varphi,\psi$$는 서로 역인 isomorphism이다. 끝으로 $$g\varphi=g'$$로부터 $$\varphi$$가 두 열의 오른쪽 사각형을 commute하게 하고, $$\im f=\ker g$$, $$\im f'=\ker g'$$가 $$\varphi$$ 아래에서 대응하므로 $$\varphi f$$가 $$\im f'$$로 들어가 $$A\xrightarrow{\sim}A'$$를 유도한다. 이로써 세 수직사상이 모두 isomorphism인 완전열의 동형을 얻는다.

</details>

명제 4의 유일성은 almost split sequence를 $$C$$의 불변량으로 만든다. 곧 non-projective indecomposable $$C$$ 하나에 대하여 그것으로 끝나는 almost split sequence가 (존재한다면) 본질적으로 하나뿐이므로, 시작점 $$A$$와 중간항 $$B$$가 $$C$$로부터 결정된다. 이 시작점 $$A$$를 $$C$$로부터 구성하는 표준적인 방법이 다음 절의 *AR translate*이며, 존재성 자체는 [정리 7](#thm7)에서 다룬다. 한편 $$g:B\rightarrow C$$가 right almost split이고 $$B=\bigoplus_i B_i$$를 indecomposable 분해라 하면, 각 합성 $$B_i\hookrightarrow B\xrightarrow{g}C$$가 irreducible morphism이 됨을 보일 수 있고, 이것이 [정의 8](#def8)에서 Auslander–Reiten quiver의 화살표 $$B_i\rightarrow C$$를 정의하는 근거가 된다.

## Transpose와 AR translate

이제 non-projective indecomposable $$C$$로부터 almost split sequence의 시작점이 될 module을 구성한다. 두 단계를 거치는데, 먼저 right module 쪽으로 옮기는 *transpose* $$\Tr$$를, 다음으로 다시 left module로 되돌리는 *duality* $$\D$$를 적용한다. Transpose는 $$C$$의 minimal projective presentation을 dualize하여 얻는다. 여기서 $$C$$의 *projective cover*는 전사 $$P_0\twoheadrightarrow C$$ 가운데 $$P_0$$의 차원이 최소인 것이며, 유한차원 대수 위에서 항상 존재한다.

<div class="definition" markdown="1">

<ins id="def5">**정의 5**</ins> 유한차원 left $$A$$-module $$C$$의 *minimal projective presentation*<sub>최소 사영 표시</sub>은 완전열

$$P_1\xrightarrow{\ p_1\ }P_0\xrightarrow{\ p_0\ }C\longrightarrow 0$$

으로서, $$p_0:P_0\rightarrow C$$가 projective cover이고 $$p_1:P_1\rightarrow\ker p_0$$이 다시 projective cover인 것이다. $$(-)^{\ast}=\Hom_A(-,A)$$를 적용하면 right $$A$$-module의 사상열

$$P_0^{\ast}\xrightarrow{\ p_1^{\ast}\ }P_1^{\ast}\longrightarrow \Tr C\longrightarrow 0$$

을 얻으며, $$C$$의 *transpose*<sub>전치</sub>를

$$\Tr C=\coker\bigl(p_1^{\ast}:P_0^{\ast}\rightarrow P_1^{\ast}\bigr)$$

으로 정의한다. 이는 right $$A$$-module이다.

</div>

함자 $$(-)^{\ast}=\Hom_A(-,A)$$는 left $$A$$-module을 right $$A$$-module로 보내며, projective module $$P$$에 대하여 $$P^{\ast}$$ 또한 projective right module이다. Minimal projective presentation은 projective cover의 유일성에 의하여 isomorphism을 무시하면 유일하게 결정되므로, $$\Tr C$$ 또한 그러하다. 다만 $$\Tr$$는 projective summand에 둔감하다. $$C$$가 projective이면 $$P_1=0$$으로 둘 수 있어 $$\Tr C=0$$이 되며, 일반적으로 $$\Tr$$는 projective을 제외한 부분에서만 잘 정의된 대응을 준다. 다음으로 $$k$$ 위의 duality를 도입하여 right module을 다시 left module로 되돌린다.

<div class="definition" markdown="1">

<ins id="def6">**정의 6**</ins> 유한차원 대수 $$A$$ 위의 module $$M$$에 대하여, $$k$$ 위의 *duality*를

$$\D M=\Hom_k(M,k)$$

로 정의한다. $$M$$이 left $$A$$-module이면 $$\D M$$ 위에 $$(\xi\cdot a)(m)=\xi(am)$$ ($$\xi\in\D M$$, $$a\in A$$, $$m\in M$$) 으로 right $$A$$-action을 주어 $$\D M$$을 right $$A$$-module로 만들고, 대칭적으로 right module을 left module로 옮긴다. 유한차원 벡터공간 위에서 evaluation 사상 $$M\rightarrow\D\D M$$이 isomorphism이므로 $$\D$$는 left와 right module category 사이의 contravariant equivalence이다. 이를 이용하여 non-projective indecomposable left $$A$$-module $$C$$의 *Auslander–Reiten translate*<sub>AR 변환</sub>를

$$\tau C=\D\Tr C$$

로 정의한다. $$\tau C$$는 다시 left $$A$$-module이다.

</div>

$$\D$$가 유한차원 벡터공간 위에서 $$\D\D M\cong M$$을 만족하는 contravariant equivalence이므로, $$\tau=\D\Tr$$는 non-projective indecomposable module들을 non-injective indecomposable module들로 일대일 대응시킨다. 그 역함자는 $$\tau^{-1}=\Tr\D$$로 주어지며, $$\tau$$와 $$\tau^{-1}$$이 각각 indecomposable의 isomorphism class들 위에서 서로 역인 전단사를 준다. 곧 $$\tau$$는 projective을 제외한 indecomposable과 injective을 제외한 indecomposable을 맞바꾸며, 다음 정리가 이 대응이 almost split sequence의 시작점과 끝점의 관계임을 말해 준다.

## Auslander–Reiten 정리

이제 거의 모든 non-projective indecomposable $$C$$에 대하여 그것으로 끝나는 almost split sequence가 실제로 존재하고, 그 시작점이 정확히 $$\tau C$$임을 진술한다. 이 존재성 정리는 함자적 방법, 곧 module category 위의 함자들과 그들의 minimal projective resolution을 정밀하게 분석하여 증명되며, 그 전체 논증은 상당히 길다. 우리는 정리를 정확히 진술하고 완전한 증명은 문헌으로 미룬다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7**</ins> (Auslander–Reiten) $$A$$를 field $$k$$ 위의 유한차원 대수라 하자.

1. 임의의 non-projective indecomposable left $$A$$-module $$C$$에 대하여, $$C$$로 끝나는 almost split sequence

$$0\longrightarrow \tau C\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C\longrightarrow 0$$

이 존재한다. 곧 그 시작점은 [정의 6](#def6)의 AR translate $$\tau C=\D\Tr C$$와 isomorphic하다.

2. 대칭적으로, 임의의 non-injective indecomposable $$A$$ 대하여 $$A$$로 시작하는 almost split sequence $$0\rightarrow A\rightarrow B\rightarrow \tau^{-1}A\rightarrow 0$$이 존재한다.

[명제 4](#prop4)에 의하여 이 almost split sequence는 $$C$$ (각각 $$A$$)에 의하여 isomorphism을 무시하면 유일하게 결정된다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

이 정리는 Auslander와 Reiten이 도입한 함자적 방법으로 증명된다. 핵심은 $$\D\Tr C$$를 $$\End_A(C)$$의 잉여체로의 사상에 대한 함자 $$\D\Hom_A(-,C)$$의 minimal projective resolution과 연결짓는 것으로, 이로부터 $$\Ext_A^1(C,\tau C)$$ 안에 right almost split이 되는 표준적인 원소가 존재함을 보인다. 완전한 증명은 길어 여기서 재구성하지 않으며, [ASS, Chapter IV, Theorem 1.13 및 Theorem 3.1]과 [ARS, Chapter V]의 함자적 논증을 따른다. Schiffler의 [Sch, Chapter 7]에는 hereditary algebra의 경우에 대한 보다 직접적인 구성이 있다.

존재성을 전제로 하면, 시작점이 $$\tau C$$임은 다음과 같이 정리된다. Almost split sequence는 $$\Ext_A^1(C,A')$$의 원소이며, 그것이 almost split이라는 조건이 $$A'\cong\D\Tr C$$를 강제한다. 한편 [명제 4](#prop4)의 유일성은 존재성과 독립적으로 성립하므로, 일단 almost split sequence가 존재하면 그것은 $$C$$로부터 유일하게 결정되고 그 시작점은 $$\tau C$$로 확정된다. 두 번째 진술은 $$\D$$를 통한 left–right 대칭과 $$\tau^{-1}=\Tr\D$$로부터 첫 번째와 대칭적으로 따라온다.

</details>

정리 7은 module category $$\operatorname{mod} A$$의 거의 모든 morphism 구조를 $$\tau$$와 almost split sequence로 조직화한다. Non-projective indecomposable $$C$$마다 almost split sequence $$0\rightarrow\tau C\rightarrow B\rightarrow C\rightarrow 0$$이 하나씩 대응하고, 그 중간항 $$B$$의 indecomposable 분해가 $$C$$의 이웃들을 결정한다. Projective indecomposable $$P$$는 almost split sequence의 끝점이 될 수 없지만, 대신 $$\rad P\hookrightarrow P$$ ($$\rad P$$는 $$P$$의 radical, 곧 maximal submodule들의 교집합)가 right almost split morphism의 역할을 하여 quiver에서 $$P$$로 들어오는 화살표를 결정한다. 이로써 모든 indecomposable과 그 사이의 irreducible morphism이 하나의 조합론적 자료로 묶이며, 이를 정리한 것이 다음의 Auslander–Reiten quiver이다.

## Auslander–Reiten quiver

<div class="definition" markdown="1">

<ins id="def8">**정의 8**</ins> 유한차원 대수 $$A$$의 *Auslander–Reiten quiver* $$\Gamma_A$$는 다음의 quiver이다. Vertex는 indecomposable $$A$$-module들의 isomorphism class이다. 두 indecomposable $$M,N$$에 대하여, irreducible morphism $$M\rightarrow N$$이 존재할 때 vertex $$[M]$$에서 $$[N]$$으로 화살표를 하나 그린다. (보다 정밀하게는 화살표에 $$\Irr(M,N)=\rad(M,N)/\rad^2(M,N)$$의 차원을 valuation으로 붙이나, $$k$$가 algebraically closed이고 $$A=kQ$$가 acyclic이면 모든 valuation이 $$1$$이다.) 또한 $$\tau$$가 정의되는 non-projective vertex $$[C]$$마다 점선 $$[C]\dashrightarrow[\tau C]$$를 그려 AR translate를 기록한다.

</div>

Auslander–Reiten quiver는 정리 7이 보장하는 구조를 그래프로 압축한 것이다. 각 almost split sequence $$0\rightarrow\tau C\rightarrow\bigoplus_i B_i\rightarrow C\rightarrow 0$$은 quiver 안에서 *mesh*라 불리는 그림, 곧 $$\tau C$$에서 각 $$B_i$$로 향하는 화살표들과 각 $$B_i$$에서 $$C$$로 향하는 화살표들로 이루어진 평행사변형 모양을 이룬다. 이 mesh 구조 덕분에 $$\Gamma_A$$의 한 부분을 알면 $$\tau$$를 따라 나머지를 복원할 수 있으며, representation-finite 대수의 경우 $$\Gamma_A$$는 유한 그래프로서 module category 전체를 담는다. 구체적인 모양을 선형 $$A_3$$ quiver에서 계산한다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> 선형 $$A_3$$ quiver $$1\xrightarrow{\alpha}2\xrightarrow{\beta}3$$ ([§Quiver와 경로대수, ⁋예시 6](/ko/math/representation_theory/path_algebras#ex6)) 를 생각하자. 이 quiver의 indecomposable representation은 정확히 여섯 개이며, 각 $$1\leq i\leq j\leq 3$$에 대하여 vertex $$i,i+1,\ldots,j$$에 $$k$$를, 그 사이의 arrow에 $$\id_k$$를, 나머지에 $$0$$을 둔 representation $$M_{[i,j]}$$로 주어진다. 이를 dimension vector $$(\dim V_1,\dim V_2,\dim V_3)$$로 적으면

$$M_{[1,1]}=(1,0,0),\quad M_{[2,2]}=(0,1,0),\quad M_{[3,3]}=(0,0,1),$$

$$M_{[1,2]}=(1,1,0),\quad M_{[2,3]}=(0,1,1),\quad M_{[1,3]}=(1,1,1)$$

이다. 여기서 $$M_{[1,1]},M_{[2,2]},M_{[3,3]}$$은 세 simple module이다. Projective indecomposable은 $$P_i=e_i\cdot kQ$$에 대응하는 것으로, 이 orientation에서 $$P_1=M_{[1,3]}$$, $$P_2=M_{[2,3]}$$, $$P_3=M_{[3,3]}$$이고, injective indecomposable은 $$I_1=M_{[1,1]}$$, $$I_2=M_{[1,2]}$$, $$I_3=M_{[1,3]}$$이다.

Non-projective indecomposable은 $$M_{[1,1]},M_{[2,2]},M_{[1,2]}$$의 셋이며, 각각에 대한 almost split sequence는 다음과 같다.

$$0\rightarrow M_{[2,2]}\rightarrow M_{[1,2]}\rightarrow M_{[1,1]}\rightarrow 0,$$

$$0\rightarrow M_{[2,3]}\rightarrow M_{[1,3]}\oplus M_{[2,2]}\rightarrow M_{[1,2]}\rightarrow 0,$$

$$0\rightarrow M_{[3,3]}\rightarrow M_{[2,3]}\rightarrow M_{[2,2]}\rightarrow 0.$$

각 열이 dimension vector를 보존함을 확인할 수 있다. 가령 둘째 열에서 $$(0,1,1)+(1,1,0)=(1,2,1)=(1,1,1)+(0,1,0)$$이다. 이로부터 AR translate는 $$\tau M_{[1,1]}=M_{[2,2]}$$, $$\tau M_{[1,2]}=M_{[2,3]}$$, $$\tau M_{[2,2]}=M_{[3,3]}$$이다. 화살표를 모으면 Auslander–Reiten quiver $$\Gamma_{kQ}$$는 다음 모양이 된다.

![A3 Auslander-Reiten quiver](/assets/images/Math/Representation_Theory/Auslander-Reiten_Theory-2.svg){:style="width:22.72em" class="invert" .align-center}

여기서 각 화살표는 $$M_{[i,j]}$$에서 한 끝을 늘이거나 줄이는 inclusion·quotient에 해당하는 irreducible morphism이다. 가장 아래 행 $$M_{[3,3]},M_{[2,2]},M_{[1,1]}$$과 가운데 행 $$M_{[2,3]},M_{[1,2]}$$ 위에서 $$\tau$$는 각각 한 칸씩 왼쪽으로 옮기는 대응 $$\tau M_{[2,2]}=M_{[3,3]}$$, $$\tau M_{[1,1]}=M_{[2,2]}$$, $$\tau M_{[1,2]}=M_{[2,3]}$$으로 나타나고, 맨 위의 $$M_{[1,3]}=I_3$$은 injective이므로 $$\tau$$의 정의역에 들지 않는다. 이 quiver는 type $$A_3$$의 Dynkin diagram 모양을 따른다.

</div>


<div class="remark" markdown="1">

<ins id="rmk10">**참고 10**</ins> Irreducible morphism은 module category의 *radical*로도 특징지어진다. $$\rad(M,N)$$을 isomorphism의 합성으로 분해되지 않는 사상들이 이루는 부분공간(indecomposable $$M,N$$에 대해서는 non-isomorphism들)으로, $$\rad^2(M,N)$$을 $$\rad(M,X)$$와 $$\rad(X,N)$$의 원소들의 합성으로 생성되는 부분공간으로 두면, indecomposable $$M,N$$에 대하여 $$f:M\rightarrow N$$이 irreducible인 것은

$$f\in\rad(M,N)\setminus\rad^2(M,N)$$

인 것과 동치이다. 따라서 $$\Irr(M,N)=\rad(M,N)/\rad^2(M,N)$$의 차원이 Auslander–Reiten quiver에서 $$M\rightarrow N$$ 화살표의 multiplicity(valuation)를 준다. 이 관점에서 almost split sequence는 $$\rad/\rad^2$$ 수준의 정보를 짧은 완전열로 묶어 낸 것이며, 이것이 [정의 8](#def8)의 quiver가 module category의 morphism 구조를 충실히 반영하는 이유이다.

</div>

---

**참고문헌**

**[ASS]** I. Assem, D. Simson, and A. Skowroński, *Elements of the representation theory of associative algebras, Volume 1: Techniques of representation theory*, Cambridge University Press, 2006.

**[ARS]** M. Auslander, I. Reiten, and S. O. Smalø, *Representation theory of Artin algebras*, Cambridge University Press, 1995.

**[Sch]** R. Schiffler, *Quiver representations*, Springer, 2014.

**[ASm]** M. Auslander and I. Reiten, *Representation theory of Artin algebras III: Almost split sequences*, Communications in Algebra **3** (1975), 239–294.
