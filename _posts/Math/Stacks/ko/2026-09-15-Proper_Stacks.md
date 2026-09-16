---
title: "고유스택"
description: "Algebraic stack의 separatedness와 properness를 diagonal로 정의하고, finite base change를 허용하는 valuative criterion 및 coarse moduli space와의 관계를 다룬다."
excerpt: "Proper Deligne–Mumford stacks, their valuative criterion, and coarse moduli spaces"

categories: [Math / Stacks]
permalink: /ko/math/stacks/proper_stacks
sidebar:
    nav: "stacks-ko"

date: 2026-09-15
weight: 5

---

우리는 이전 글에서 moduli space에 대해 살펴보았다. Moduli space의 가장 초등적인 예시는 [§모듈라이 공간, ⁋예시 3](/ko/math/stacks/moduli_spaces#ex3)에서 살펴본 Grassmannian으로, 이를 통해 moduli space가 어떤 식으로 활용되는지 살펴보자. 

[\[대수적 위상수학\] §슈티펠-휘트니 특성류, ⁋예시 7](/ko/math/algebraic_topology/stiefel_whitney_classes#ex7){: data-relation="weak" }에서는 $\Gr(2,\mathbb{R}^4)$ 위의 두 Schubert cycle을 general position에서 교차시켜 cohomology relation

$$\sigma_{(1,0)}\smile\sigma_{(1,0)}=\sigma_{(1,1)}+\sigma_{(2,0)}$$

을 직접 계산하였다. 같은 relation이 complex Grassmannian $\Gr(2,\mathbb{C}^4)$에서도 성립하며, 이를 projectivize하면 $\Gr(2,\mathbb{C}^4)$를 $\mathbb{P}^3$ 안의 line들의 공간과 identify할 수 있다. 이제 주어진 line $A\subseteq\mathbb{P}^3$과 만나는 line들의 Schubert divisor를 $\Omega_A$라 하면, 좌변은 두 line $A,B$를 모두 만나는 line들의 locus $\Omega_A\cap\Omega_B$를 나타낸다. 만일 우리가 직선 $B$를 움직여 $A$와 한 점 $p$에서 만나게 하면, $A$와 $B$를 동시에 지난다는 조건은 $A,B$가 span하는 평면에 포함되거나, $A,B$의 교점을 지나는 두 가지 경우가 가능하며 이것이 바로 위의 식이 의미하는 바이다.

이 specialization은 Grassmannian이 line들의 좋은 moduli space가 되는 이유도 보여 준다. 예를 들어, 두 skew line $A,B$와 점 $p,q$에서 각각 만나는 line $C$를 생각하자. 이는 정확히 두 점 $p,q$에 의해 유일하게 결정되지만, 위의 설명처럼 $B$의 점 $q$를 $A$의 점 $p$로 움직인다면, 한 점 $p$만으로는 직선을 특정할 수 없으므로 이 극한이 기여하는 성분은 사라질 수도 있었다. 그럼에도 이 성분이 남아있는 것이 위에서 살펴본 $\sigma_{(2,0)}$ 부분으로, 대수기하학에서 이렇게 극한이 존재하도록 하는 것은 properness의 개념이었다. ([\[스킴\] §값매김환, ⁋정리 11](/ko/math/scheme_theory/valuative_criteria#thm11){: data-relation="weak" })

이번 글에서 우리는 algebraic stack이 proper하다는 것이 어떤 것인지를 정의하고 그 성질들을 살펴본다. 특별한 언급이 없는 한 이 글에서 다루는 Deligne–Mumford stack은 field $\mathbb{K}$ 위에서 finite type이고 quasi-separated인 것으로 약속한다.

## 고유성

Scheme theory에서 다룬 많은 성질들이 그러하듯, properness 또한 scheme 자체의 성질이라기보다는 scheme morphism의 성질이었고, 어떠한 $S$-scheme $X$가 proper하다는 것은 이를 사용하여 structure morphism $X\rightarrow S$가 proper인 것으로 정의했었다. 마침 우리는 representable stack morphism의 경우 scheme morphism으로서의 성질 $P$를 그대로 부여할 수 있음을 알고 있다. ([§대수적 스택, ⁋정의 4](/ko/math/stacks/algebraic_stacks#def4){: data-relation="required" })

다만 여기에는 주의할 점이 있다. Scheme theory에서 separated morphism을 diagonal이 closed embedding인 것으로 정의했던 것과 달리 ([\[스킴\] §값매김환, ⁋정의 3](/ko/math/scheme_theory/valuative_criteria#def3){: data-relation="required" }), stack에서는 대상들의 automorphism 때문에 diagonal이 monomorphism이 될 수 없다. 그 대신, closed embedding은 proper monomorphism이므로 ([\[스킴\] §값매김환, ⁋따름정리 13](/ko/math/scheme_theory/valuative_criteria#cor13){: data-relation="required" } 직후의 논의) 우리는 algebraic stack의 morphism $f: \mathcal{X}\rightarrow \mathcal{Y}$가 separated라는 것을, *algebraic space 사이의 morphism* $\Delta_f$가 proper하다는 것으로 정의하고, 그 후 *algebraic stack 사이의 morphism* $f: \mathcal{X}\rightarrow \mathcal{Y}$가 proper하다는 것은 이 separatedness 정의를 이용하여 언제나처럼 정의한다. ([\[스킴\] §값매김환, ⁋정리 11](/ko/math/scheme_theory/valuative_criteria#thm11){: data-relation="weak" })

::: 정의 1
두 algebraic stack $\mathcal{X}$, $\mathcal{Y}$와 이들 사이의 morphism $f: \mathcal{X}\rightarrow \mathcal{Y}$가 주어졌다 하자. 

1. $f$가 *separated*라는 것은 diagonal $\Delta_f$가 proper라는 것이다. 
2. $f$가 *proper<sub>고유(의)</sub>*라는 것은 $f$가 finite type, separated, universally closed라는 것이다. 

특히 structure morphism $\mathcal{X}\rightarrow\Spec\mathbb{K}$가 각각 separated 또는 proper일 때 $\mathcal{X}$를 separated 또는 proper algebraic stack이라 부른다.
:::

위에서 설명한 것과 같이, stack으로 올라오며 생긴 유일한 차이는 $f$의 separatedness가 diagonal의 properness를 요구한다는 것으로, 만일 $f$가 scheme 혹은 algebraic space 사이의 morphism이었다면 diagonal이 monomorphism이므로 이 정의는 원래의 조건을 정확하게 보존한다. 

일반적인 stack에서 geometric point $x:\Spec\mathbb{K}\rightarrow\mathcal{X}$의 stabilizer $\rAut_\mathbb{K}(x)$는 diagonal $\Delta_\mathcal{X}:\mathcal{X}\rightarrow\mathcal{X}\times_\mathbb{K}\mathcal{X}$를 $(x,x):\Spec\mathbb{K}\rightarrow\mathcal{X}\times_\mathbb{K}\mathcal{X}$를 따라 base change한 fiber로 얻어졌던 것을 기억하자. ([§대수적 스택, ⁋명제 5](/ko/math/stacks/algebraic_stacks#prop5){: data-relation="weak" }) Deligne-Mumford stack의 경우 이 diagonal이 unramified이므로, 이를 base change하여 얻어지는 stabilizer $\rAut_\mathbb{K}(x)$ 또한 $\mathbb{K}$ 위에서 unramified group scheme이며, 따라서 이는 locally quasi-finite group scheme이 된다. 여기에 만일 추가로 $\mathcal{X}$가 separated라면, diagonal이 proper이므로 automorphism group 역시 proper이다. Proper morphism은 quasi-compact이므로 locally quasi-finite인 $\Aut_{\mathbb{K}}(x)$는 quasi-finite이고, 따라서 proper quasi-finite morphism이 finite라는 사실에 의해 $\Aut_{\mathbb{K}}(x)$는 $\mathbb{K}$ 위의 finite group scheme이다. 더욱이 이는 unramified이므로 실제로 finite étale group scheme이다.

## Valuative criterion

Scheme에서 separatedness와 universally closedness를 직접 확인하는 대신 valuation ring을 이용해 판정했던 것처럼 ([\[스킴\] §값매김환, ⁋정리 6](/ko/math/scheme_theory/valuative_criteria#thm6){: data-relation="weak" }, [⁋정리 11](/ko/math/scheme_theory/valuative_criteria#thm11){: data-relation="weak" }), stack에서도 대상의 properness를 판별하는 핵심 도구는 discrete valuation ring을 통한 valuative criterion이다. 

Complete discrete valuation ring $A$의 fraction field를 $K$라 하고, generic point inclusion을 $j:\Spec K\rightarrow\Spec A$로 쓰자. $\mathcal{X}$의 $K$-object $\xi_K$는 morphism $\Spec K\rightarrow\mathcal{X}$과 같은 자료이다. Scheme에서 이를 $A$ 위로 연장한다는 것은 $j^\ast\xi_A=\xi_K$가 되는 $A$-point를 찾는 것이었으나, stack에서는 다이어그램이 strictly commute하는 대신 $2$-categorical sense에서 isomorphism들을 올바르게 bookkeeping해야 한다. 즉 이를 $A$ 위로 연장한다는 것은 $\xi_A\in\mathcal{X}(A)$와 함께 지정된 isomorphism

$$\alpha:j^\ast\xi_A\xrightarrow{\sim}\xi_K$$

를 주는 것이며, stack의 valuative criterion에서는 이 $2$-isomorphism $\alpha$라는 데이터를 반드시 남겨두어야 한다.

::: 정리 2 (Valuative criterion)
Finite type이고 quasi-separated인 Deligne–Mumford stack $\mathcal{X}$ over $\mathbb{K}$에 대하여 다음 두 조건은 동치이다.

1. $\mathcal{X}$는 proper하다.

2. 임의의 complete discrete valuation ring $A$ over $\mathbb{K}$와 fraction field $K$에 대하여 다음 existence와 uniqueness가 성립한다.

   **Existence.** 임의의 $\xi_K\in\mathcal{X}(K)$에 대하여 finite field extension $K'/K$과 $A$를 dominate하는 discrete valuation ring $A'\subseteq K'$이 존재하여, 어떤 $\xi_{A'}\in\mathcal{X}(A')$와 isomorphism

   $$\alpha:\xi_{A'}\vert_{K'}\xrightarrow{\sim}\xi_K\vert_{K'}$$

   이 존재하도록 할 수 있다.

   **Uniqueness.** 두 object $\xi_A,\eta_A\in\mathcal{X}(A)$와 generic fiber에서 <em-ko>지정된</em-ko> isomorphism

   $$\varphi_K:\xi_A\vert_K\xrightarrow{\sim}\eta_A\vert_K$$

   이 주어지면, $\varphi_K$을 제한으로 갖는 isomorphism $\varphi_A:\xi_A\xrightarrow{\sim}\eta_A$이 유일하게 존재한다.
:::

즉, stack의 valuative criterion은 $1$-categorical formulation을 $2$-isomorphism으로 올바르게 대체하여 moduli의 극한과 automorphism 정보를 동시에 보존하도록 설계된 것이다.

::: 예시 3 (Finite group의 classifying stack)
$\ch \mathbb{K}$를 나누지 않는 자연수 $n\geq 2$에 대하여, finite étale group scheme $G=\mu_n$을 생각하자. 그럼 classifying stack $\bB G=[\Spec\mathbb{K}/G]$는 $G$-torsor들을 분류하는 Deligne-Mumford stack임을 이미 살펴보았다. ([§대수적 스택, ⁋정의 7](/ko/math/stacks/algebraic_stacks#def7){: data-relation="required" reviewed="" }) 우리는 [정리 2](#thm2){: data-relation="required" reviewed="" }의 valuative criterion을 통해 $\bB G$가 proper함을 확인할 수 있다.

우선 uniqueness의 경우, 두 $G$-torsor $P_A, Q_A$ 사이의 $\rIsom_A(P_A, Q_A)$는 $\Spec A$ 위에서 finite étale scheme이므로 generic fiber의 isomorphism $\varphi_K:P_A\vert_K\xrightarrow{\sim} Q_A\vert_K$는 $A$ 전체 위의 $\varphi_A:P_A\xrightarrow{\sim} Q_A$로 유일하게 연장된다.

반면 existence의 경우, 임의의 $G$-torsor $P_K\rightarrow\Spec K$는 finite étale scheme이므로 적당한 finite extension $K'/K$ 위에서 section을 갖는다. Section을 갖는 $G$-torsor는 trivial하므로 $P_K\vert_{K'}\cong G\times\Spec K'$이고, 이는 $A'$ 위에서 trivial torsor $G\times\Spec A'$로 즉시 연장된다. 가령 $A=\mathbb{K}[[t]]$와 $K=\mathbb{K}((t))$ 위의 $\mu_n$-torsor

$$P_K=\Spec K[u]/(u^n-t)$$

는 $K$ 위에서 자명하지 않아 $A$ 위로 직접 연장되지 않지만, $t=s^n$인 $K'=\mathbb{K}((s))$ 위에서는 $u=s$를 통해 trivial torsor로 식별되어 $A'=\mathbb{K}[[s]]$ 위로 연장된다.
:::

## Coarse moduli space와 quotient chart

Separated finite type Deligne–Mumford stack은 finite inertia stack을 가지므로, 이제 우리는 [§모듈라이 공간, ⁋정리 8](/ko/math/stacks/moduli_spaces#thm8){: data-relation="required" reviewed="" }의 첫째 주장이 둘째 주장을 함의하는 것을 확인할 수 있다. 이를

$$\pi:\mathcal{X}\longrightarrow X$$

로 쓰자. Characteristic $0$인 field $\mathbb{K}$ 위에서는 stabilizer가 finite linearly reductive group이고, coarse morphism은 étale-locally finite group quotient의 형태를 갖는다.

::: 명제 4 (Local quotient chart)
Characteristic $0$ field $\mathbb{K}$ 위의 separated, finite type Deligne-Mumford stack $\mathcal{X}$와, $\mathcal{X}$의 coarse moduli $\pi: \mathcal{X}\rightarrow X$를 생각하자. $\mathcal{X}$의 임의의 geometric point $x\rightarrow\mathcal{X}$와 그 stabilizer $G_x$에 대하여, $\bar{x}=\pi(x)$의 étale neighborhood $U\rightarrow X$와 affine scheme $V$ 위의 $G_x$-action이 존재하여

$$\mathcal{X}\times_X U\cong[V/G_x],\qquad U\cong V/G_x$$

이도록 할 수 있다. 뿐만 아니라, 만일 $\mathcal{X}$가 smooth이면 $V$ 역시 smooth하게 택할 수 있다.
:::

이는 separated finite type Deligne-Mumford stack의 local structure theorem이라 부를 만하다. 즉 Deligne-Mumford stack은 coarse moduli space의 étale topology에서 finite group에 의한 quotient stack으로 국소적으로 표현되며, 그 coarse moduli space 역시 대응하는 categorical quotient들을 étale하게 이어붙인 것으로 생각할 수 있다. 특히 $\mathcal{X}$가 smooth하면 $V$를 smooth하게 택할 수 있으므로, coarse moduli space $X$는 국소적으로 smooth variety의 finite quotient $V/G_x$의 꼴로 나타난다. 따라서 $X$는 일반적으로 smooth하지는 않더라도 finite quotient singularity만을 갖는다.

눈여겨볼 만한 것은 여기서 등장하는 group $G_x$는, 설령 원래 stack이 전역적으로 $\mathcal{X}=[M/G]$의 꼴로 주어져 있더라도 이 $G$와 같을 필요는 없다는 것이다. 이는 quotient stack에서 coarse moduli로 넘어가는 과정을 생각하면 자연스럽게 이해할 수 있다.

Quotient stack $[M/G]$에서 $G$의 작용은 두 종류의 정보를 동시에 담고 있다. 하나는 $M$ 위에서 실제로 점들을 움직이는 작용에 해당하는 부분이며, 다른 부분은 그 점을 움직이지 않은 채, 그 점의 automorphism으로만 남는 stabilizer $H$ 부분이다. Coarse moduli $M/G$를 취하는 과정에서, 전자의 경우에는 하나의 orbit에 속한 점들을 모두 한 점으로 identify하는 방식으로 scheme 단계에서도 보이는 것이지만, 후자의 stabilizer 정보는 점에 붙어 있던 automorphism data 자체가 사라지므로 없어지는 정보이다. 즉 coarse moduli에는 orbit만 남고, 각 점이 원래 어떤 stabilizer를 가지고 있었는지는 기록되지 않는다.

이제 위의 정리의 관점에서, 한 점 $x\in\mathcal{X}$를 잡고 이를 전역 quotient presentation $[M/G]$의 점 $p\in M$으로 나타낸다면, $x$의 automorphism group $G_x=\Stab_G(p)$은 $G$의 subgroup으로, $G$ 전체 원소 중 $p$를 고정하는 부분만 $G_x$로 남게 되며, 이를 사용한 것이 위의 local model이다. 

그럼 이 local model에서의 $G_x$ 안에서도 역할에 따라 실제로 유효하게 작용하는 부분이 나뉜다. Local quotient $[V/G_x]$와 그 coarse moduli $[V/G_x]\longrightarrow V/G_x$를 보면, 각각의 $G_x$-orbit이 한 점으로 줄어드는 반면 $H$는 stack으로 내려오는 과정에서 사라지므로, 실제로 $V$의 점을 움직이는 원소들은 $G_x/H$ 부분이다. 

이제 $H$의 원소들을 골라내기 위해서는 function field를 보면 된다. 즉, $H$가 $K(V)$에 trivial하게 작용하므로 $G_x$의 function field 위 action은 $G_x/H$를 통해 factor하고,

$$K(V/G_x)=K(V)^{G_x}=K(V)^{G_x/H}$$

가 된다. Characteristic $0$에서는 $G_x/H$가 $K(V)$에 faithful하게 작용하므로

$$[K(V):K(V/G_x)]=\lvert G_x/H\rvert=\frac{\lvert G_x\rvert}{\lvert H\rvert}$$

가 성립하게 된다. 

 또 다른 중요한 사실 중 하나는 finite group action에 대한 local quotient morphism $[V/G_x]\rightarrow V/G_x$는 proper하므로, 이러한 local description을 이용하면 coarse moduli morphism $\pi:\mathcal{X}\rightarrow X$ 역시 proper morphism이 된다는 것이다.

::: 정리 5
Field $\mathbb{K}$ 위의 separated finite type Deligne–Mumford stack $\mathcal{X}$와 coarse moduli space $\pi:\mathcal{X}\rightarrow X$에 대하여 다음 두 조건은 동치이다.

1. $\mathcal{X}$는 proper하다.

2. Algebraic space $X$는 proper하다.
:::
::: 증명
$X$가 proper이면 [명제 4](#prop4){: data-relation="required" reviewed="" }에서 얻은 proper coarse morphism $\pi$와 $X\rightarrow\Spec\mathbb{K}$을 합성하여 $\mathcal{X}$가 proper임을 얻는다.

거꾸로 $\mathcal{X}$가 proper하다고 하자. Coarse morphism $\pi$는 surjective이고 $X$는 separated finite type algebraic space이다. 임의의 base change $T\rightarrow\Spec\mathbb{K}$ 뒤에도 $\mathcal{X}_T\rightarrow X_T$는 surjective이다. $\mathcal{X}_T\rightarrow T$가 closed이므로 $X_T$의 closed subset을 inverse image한 뒤 $T$로 보내면 closed subset을 얻고, surjectivity에 의하여 이는 원래 closed subset의 image와 같다. 따라서 $X\rightarrow\Spec\mathbb{K}$는 universally closed이고, separated finite type이므로 proper하다.
:::

한편 stabilizer가 완전히 사라지는 경우에는 stack과 coarse space의 차이도 사라진다.

::: 따름정리 6
Field $\mathbb{K}$ 위의 separated finite type Deligne–Mumford stack $\mathcal{X}$의 모든 geometric point에서 stabilizer가 trivial이면 $\mathcal{X}$는 algebraic space이고, coarse morphism $\pi:\mathcal{X}\rightarrow X$는 isomorphism이다.
:::
::: 증명
Separated Deligne–Mumford 조건에 의하여 inertia morphism $I_\mathcal{X}\rightarrow\mathcal{X}$은 finite unramified이다. Identity section $e:\mathcal{X}\rightarrow I_\mathcal{X}$은 unramified morphism의 section이므로 open immersion이고, 가정에 의하여 모든 geometric point가 그 image에 속한다. 따라서 $e$는 isomorphism이고 inertia는 identity이다.

임의의 두 isomorphism 사이의 차이는 automorphism이므로 diagonal $\Delta_\mathcal{X}$는 monomorphism이다. 따라서 각 fiber groupoid는 set과 equivalent하고 descent에 의하여 $\mathcal{X}$는 set-valued sheaf로 identified된다. Étale atlas를 가진 이 sheaf는 algebraic space이고, coarse moduli morphism의 universal property를 이 algebraic space 자체에 적용하면 $\pi$의 inverse를 얻는다.
:::

따라서 moduli stack이 trivial stabilizer를 갖는 범위에서는 geometric point를 세는 문제가 algebraic space의 point를 세는 문제로 돌아간다. Stabilizer가 남는 범위에서는 coarse space가 같은 geometric isomorphism classes를 가지더라도 automorphism 정보까지 보존하지는 않는다.

---

**참고문헌**

**[AV]** D. Abramovich and A. Vistoli, *Compactifying the space of stable maps*, Journal of the American Mathematical Society **15** (2002), 27–75.  
**[Vis]** A. Vistoli, *Intersection theory on algebraic stacks and on their moduli spaces*, Inventiones Mathematicae **97** (1989), 613–670.  
**[Stacks]** The Stacks Project Authors, *The Stacks Project*, Tags 0CLA, 0CLG, 0CLK, 0CLT, 0CLU, 0CLW, 0CLX, 0CLZ, 0CQ8, 0CQM, https://stacks.math.columbia.edu.
