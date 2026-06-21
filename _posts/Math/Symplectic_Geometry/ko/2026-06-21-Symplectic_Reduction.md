---
title: "사교 축약"
description: "Marsden-Weinstein-Meyer 축약 정리를 다룬다. Hamiltonian G-공간에서 0이 운동량 사상의 regular value이고 작용이 자유롭고 proper하면 축약공간이 사교다양체가 됨을 증명하고, 일반값과 coadjoint orbit에서의 축약을 서술한 뒤 복소 사영공간을 예시로 든다."
excerpt: "Marsden-Weinstein-Meyer 축약, 축약공간, coadjoint orbit 축약, CP^n"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/symplectic_reduction
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2026-06-21
weight: 3.8

published: false

---

대칭성을 가진 역학계는 그 대칭성을 이용해 자유도를 줄일 수 있다. 보존되는 운동량을 고정하고 대칭의 작용으로 나누면, 더 낮은 차원의 새 위상공간에서 같은 운동을 기술하게 된다. 이 절차의 사교기하학적 형태가 *사교 축약<sub>symplectic reduction</sub>*이다. 출발점은 Hamiltonian $$G$$-공간 $$(M,\omega,G,\mu)$$ ([§운동량 사상, ⁋정의 2](/ko/math/symplectic_geometry/moment_map#def2))이다. 운동량 사상의 한 값, 가령 $$0\in\mathfrak{g}^\ast$$을 고정하면 그 fiber $$\mu^{-1}(0)$$은 $$G$$-불변인 부분다양체이고, 이를 $$G$$로 나눈 몫 $$\mu^{-1}(0)/G$$이 다시 사교다양체가 된다는 것이 핵심이다.

이 결과는 1974년 Marsden과 Weinstein, 그리고 독립적으로 Meyer가 증명하였다. 차원을 세어 보면 $$\mu^{-1}(0)$$은 $$M$$에서 $$\dim G$$만큼 낮고 다시 $$G$$로 나누며 또 $$\dim G$$만큼 낮아져, 축약공간은 $$M$$보다 정확히 $$2\dim G$$만큼 차원이 낮다. 이 짝수만큼의 감소가 사교 구조와 정확히 맞물린다는 점이 정리의 내용이다. 우리는 먼저 $$\mu^{-1}(0)$$이 매끄러운 다양체임을 보장하는 조건을 정리하고, 그 위에서 사교형식이 몫으로 잘 내려옴을 선형대수적으로 확인한 뒤, 일반값과 coadjoint orbit에서의 축약을 서술하고 $$\mathbb{CP}^n$$의 예시로 마무리한다.

## 영점집합의 기하

축약을 시작하려면 우선 $$\mu^{-1}(0)$$이 매끄러운 부분다양체여야 한다. 이는 $$0$$이 운동량 사상의 regular value일 때 보장된다. 다음 보조정리는 regularity 조건을 작용의 자유도로 번역한다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> $$(M,\omega,G,\mu)$$가 Hamiltonian $$G$$-공간이고 $$p\in\mu^{-1}(0)$$이라 하자. 그럼 미분 $$d\mu_p:T_pM\rightarrow\mathfrak{g}^\ast$$의 성질은 점 $$p$$에서의 작용의 stabilizer와 다음과 같이 대응한다.

$$\ker d\mu_p=(\mathfrak{g}\cdot p)^{\omega},\qquad \im d\mu_p=(\mathfrak{g}_p)^{\circ}$$

여기서 $$\mathfrak{g}\cdot p=\{X_M(p):X\in\mathfrak{g}\}\subseteq T_pM$$은 orbit의 접공간, $$(\,\cdot\,)^{\omega}$$은 $$\omega_p$$에 대한 사교여공간 ([§사교벡터공간, ⁋정의 3](/ko/math/symplectic_geometry/linear_symplectic_geometry#def3)), $$\mathfrak{g}_p=\{X\in\mathfrak{g}:X_M(p)=0\}$$은 stabilizer의 Lie algebra, $$(\mathfrak{g}_p)^{\circ}\subseteq\mathfrak{g}^\ast$$은 그 annihilator이다. 특히 $$0$$이 regular value일 필요충분조건은 모든 $$p\in\mu^{-1}(0)$$에서 $$\mathfrak{g}_p=0$$, 즉 작용이 $$\mu^{-1}(0)$$ 위에서 locally free인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

각 $$X\in\mathfrak{g}$$에 대하여, 운동량 사상의 정의 조건 1 ([§운동량 사상, ⁋정의 2](/ko/math/symplectic_geometry/moment_map#def2))은 $$d\mu^X=\iota_{X_M}\omega$$이다. 점 $$p$$와 접벡터 $$v\in T_pM$$에서 이를 평가하면

$$\langle d\mu_p(v),X\rangle=d\mu_p^X(v)=\omega_p(X_M(p),v)$$

이다. 따라서 $$v\in\ker d\mu_p$$일 필요충분조건은 모든 $$X\in\mathfrak{g}$$에 대해 $$\omega_p(X_M(p),v)=0$$, 즉 $$v$$가 모든 orbit 접벡터 $$X_M(p)$$와 $$\omega_p$$-직교하는 것이다. 이것이 정확히 $$v\in(\mathfrak{g}\cdot p)^{\omega}$$이므로 $$\ker d\mu_p=(\mathfrak{g}\cdot p)^{\omega}$$이다.

상에 대해서는, 위 식이 말하는 바를 $$X$$에 대한 선형범함수로 보면 $$d\mu_p(v)$$는 $$X\mapsto\omega_p(X_M(p),v)$$이다. 한 원소 $$\xi=d\mu_p(v)$$가 어떤 $$X\in\mathfrak{g}_p$$, 즉 $$X_M(p)=0$$인 $$X$$에서 소멸함은 자명하므로 $$\im d\mu_p\subseteq(\mathfrak{g}_p)^{\circ}$$이다. 역포함은 차원 계산으로 따라온다. 사교형식의 nondegeneracy로부터 부분공간 $$U=\mathfrak{g}\cdot p$$에 대해 $$\dim U+\dim U^{\omega}=\dim T_pM$$이므로

$$\dim\ker d\mu_p=\dim(\mathfrak{g}\cdot p)^{\omega}=\dim T_pM-\dim(\mathfrak{g}\cdot p)$$

이고, 한편 $$X\mapsto X_M(p)$$의 핵이 $$\mathfrak{g}_p$$이므로 $$\dim(\mathfrak{g}\cdot p)=\dim\mathfrak{g}-\dim\mathfrak{g}_p$$이다. 이를 합치면 rank-nullity에 의하여

$$\dim\im d\mu_p=\dim T_pM-\dim\ker d\mu_p=\dim(\mathfrak{g}\cdot p)=\dim\mathfrak{g}-\dim\mathfrak{g}_p=\dim(\mathfrak{g}_p)^{\circ}$$

이 되어 $$\im d\mu_p=(\mathfrak{g}_p)^{\circ}$$이다.

마지막 주장은 즉시 따라온다. $$d\mu_p$$가 surjective, 즉 $$0$$이 $$p$$에서 regular일 필요충분조건은 $$\im d\mu_p=\mathfrak{g}^\ast$$, 곧 $$(\mathfrak{g}_p)^{\circ}=\mathfrak{g}^\ast$$이고 이는 $$\mathfrak{g}_p=0$$과 동치이다. $$\mathfrak{g}_p=0$$은 stabilizer $$G_p$$가 discrete임, 즉 작용이 $$p$$에서 locally free임을 뜻한다.

</details>

이 보조정리는 영점집합의 두 가지 기하학적 사실을 한꺼번에 준다. 첫째, $$0$$이 regular value이면 $$\mu^{-1}(0)$$은 여차원 $$\dim G$$의 매끄러운 부분다양체이고 $$T_p(\mu^{-1}(0))=\ker d\mu_p=(\mathfrak{g}\cdot p)^{\omega}$$이다. 둘째, 이 접공간이 orbit 접공간 $$\mathfrak{g}\cdot p$$의 사교여공간이라는 등식 $$T_p(\mu^{-1}(0))=(\mathfrak{g}\cdot p)^{\omega}$$이 다음 절에서 사교형식을 내릴 때 결정적으로 쓰인다. 작용이 ($$\mu^{-1}(0)$$ 위에서) 자유로우면 $$\mathfrak{g}_p=0$$이므로 regularity는 자동이며, 우리는 앞으로 이 강한 가정 아래에서 작업한다.

등식 $$T_p(\mu^{-1}(0))=(\mathfrak{g}\cdot p)^{\omega}$$을 사교벡터공간의 언어로 다시 읽으면, $$\mu^{-1}(0)$$이 *coisotropic* 부분다양체임을 뜻한다. 부분공간 $$W\subseteq T_pM$$이 coisotropic이라는 것은 $$W^{\omega}\subseteq W$$인 것인데 ([§사교벡터공간, ⁋정의 3](/ko/math/symplectic_geometry/linear_symplectic_geometry#def3)), $$W=T_p(\mu^{-1}(0))$$에 대하여 $$W^{\omega}=\bigl((\mathfrak{g}\cdot p)^{\omega}\bigr)^{\omega}=\mathfrak{g}\cdot p$$이고, $$p\in\mu^{-1}(0)$$에서 각 $$X_M(p)$$이 $$\mu^{-1}(0)$$에 접하므로 ($$G$$가 $$\mu^{-1}(0)$$을 보존하기 때문) $$\mathfrak{g}\cdot p\subseteq T_p(\mu^{-1}(0))=W$$이다. 즉 영점집합의 사교수직방향이 정확히 orbit 방향이며, 이것이 몫을 취해 사교형식을 회복할 수 있게 하는 구조적 이유이다.

## Marsden-Weinstein-Meyer 정리

이제 사교형식을 몫으로 내릴 준비가 되었다. 작용이 자유롭고 proper하면 몫공간 $$\mu^{-1}(0)/G$$은 매끄러운 다양체가 되고, 사영 $$\pi:\mu^{-1}(0)\rightarrow\mu^{-1}(0)/G$$은 principal $$G$$-bundle이 된다. 우리가 할 일은 $$\mu^{-1}(0)$$ 위로 당겨 온 사교형식 $$\iota^\ast\omega$$이 이 사영을 통해 밑공간의 형식으로 유일하게 내려옴을 보이는 것이다. 여기서 $$\iota:\mu^{-1}(0)\hookrightarrow M$$은 포함사상이다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Marsden-Weinstein-Meyer)**</ins> $$(M,\omega,G,\mu)$$를 Hamiltonian $$G$$-공간이라 하고, $$G$$가 compact Lie group이며 $$0\in\mathfrak{g}^\ast$$이 $$\mu$$의 regular value라 하자. 또 $$G$$가 $$\mu^{-1}(0)$$ 위에 자유롭게 작용한다고 하자. 그럼 *축약공간<sub>reduced space</sub>*

$$M /\!\!/ G:=\mu^{-1}(0)/G$$

은 매끄러운 다양체이며, 유일한 사교형식 $$\omega_{\mathrm{red}}$$을 가져 사영 $$\pi:\mu^{-1}(0)\rightarrow M /\!\!/ G$$과 포함 $$\iota:\mu^{-1}(0)\hookrightarrow M$$에 대해

$$\pi^\ast\omega_{\mathrm{red}}=\iota^\ast\omega$$

가 성립한다. 그 차원은

$$\dim M /\!\!/ G=\dim M-2\dim G$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$Z=\mu^{-1}(0)$$으로 적는다. $$0$$이 regular value이므로 $$Z$$은 여차원 $$\dim\mathfrak{g}^\ast=\dim G$$의 매끄러운 부분다양체이고, [보조정리 1](#lem1)에 의하여 $$T_pZ=(\mathfrak{g}\cdot p)^{\omega}$$이다. $$G$$가 compact이고 $$Z$$ 위에 자유롭게 작용하므로 작용은 proper하며, 따라서 몫 $$M /\!\!/ G=Z/G$$은 매끄러운 다양체이고 $$\pi:Z\rightarrow Z/G$$은 매끄러운 submersion (principal $$G$$-bundle)이다. 자유로운 작용은 $$\mathfrak{g}_p=0$$을 주므로 $$\dim(\mathfrak{g}\cdot p)=\dim\mathfrak{g}=\dim G$$이고

$$\dim Z/G=\dim Z-\dim G=(\dim M-\dim G)-\dim G=\dim M-2\dim G$$

이다.

이제 사교형식을 내린다. 점 $$p\in Z$$에서 $$d\pi_p:T_pZ\rightarrow T_{\pi(p)}(Z/G)$$은 surjective이고 그 핵은 정확히 fiber의 접공간, 곧 orbit 방향 $$\mathfrak{g}\cdot p$$이다. 밑공간의 형식을 정의하려면, 두 벡터 $$\bar u,\bar v\in T_{\pi(p)}(Z/G)$$에 대해 이를 $$u,v\in T_pZ$$로 들어 올려

$$(\omega_{\mathrm{red}})_{\pi(p)}(\bar u,\bar v):=\omega_p(u,v)$$

으로 두면 된다. 이것이 잘 정의됨을 보이려면 (i) 들어 올림의 선택에 무관함과 (ii) 점 $$p$$를 같은 orbit 안에서 옮겨도 같은 값이 나옴을 확인해야 한다.

(i) 들어 올림은 $$\ker d\pi_p=\mathfrak{g}\cdot p$$만큼의 모호함을 가진다. $$u$$를 $$u+X_M(p)$$로 ($$X\in\mathfrak{g}$$) 바꾸어도 값이 변하지 않음은

$$\omega_p(X_M(p),v)=\langle d\mu_p(v),X\rangle=0$$

에서 나온다. 마지막 등식은 $$v\in T_pZ=\ker d\mu_p$$이기 때문이다. $$v$$에 대해서도 같으므로 $$\omega_p(u,v)$$은 들어 올림의 선택에 무관하다. 즉 $$\iota^\ast\omega$$은 orbit 방향으로 퇴화하며, 이는 $$T_pZ=(\mathfrak{g}\cdot p)^{\omega}$$, 곧 $$\mathfrak{g}\cdot p$$이 $$\iota^\ast\omega$$의 kernel임과 정확히 같은 말이다.

(ii) $$G$$가 $$\omega$$를 보존하고 ($$\psi_g^\ast\omega=\omega$$) $$Z$$을 보존하므로 $$\psi_g^\ast(\iota^\ast\omega)=\iota^\ast\omega$$이다. 따라서 $$p$$를 $$g\cdot p$$로 옮기고 들어 올림을 $$d\psi_g$$로 옮기면 같은 값을 준다. (i)과 (ii)에 의해 $$\omega_{\mathrm{red}}$$은 $$Z/G$$ 위에 well-defined인 $$2$$-form이고, 구성상 $$\pi^\ast\omega_{\mathrm{red}}=\iota^\ast\omega$$이며 이 조건이 $$\omega_{\mathrm{red}}$$을 유일하게 결정한다 ($$\pi^\ast$$이 injective이므로).

마지막으로 $$\omega_{\mathrm{red}}$$이 사교형식, 즉 closed이고 nondegenerate임을 보인다.

*Closedness.* $$\pi^\ast(d\omega_{\mathrm{red}})=d(\pi^\ast\omega_{\mathrm{red}})=d(\iota^\ast\omega)=\iota^\ast(d\omega)=0$$이고, $$\pi^\ast$$이 injective이므로 $$d\omega_{\mathrm{red}}=0$$이다.

*Nondegeneracy.* $$\bar u\in T_{\pi(p)}(Z/G)$$이 모든 $$\bar v$$에 대해 $$(\omega_{\mathrm{red}})_{\pi(p)}(\bar u,\bar v)=0$$이라 하자. 들어 올림 $$u\in T_pZ$$을 택하면 모든 $$v\in T_pZ$$에 대해 $$\omega_p(u,v)=0$$이므로 $$u\in(T_pZ)^{\omega}$$이다. 그런데 $$T_pZ=(\mathfrak{g}\cdot p)^{\omega}$$이므로 $$(T_pZ)^{\omega}=\mathfrak{g}\cdot p$$이고, 따라서 $$u\in\mathfrak{g}\cdot p=\ker d\pi_p$$이다. 즉 $$\bar u=d\pi_p(u)=0$$이므로 $$\omega_{\mathrm{red}}$$은 nondegenerate이다.

</details>

축약공간의 표기 $$M /\!\!/ G$$은 사교 몫임을 강조하는 기호로, 단순한 위상적 몫 $$M/G$$과 구별된다. 위 증명에서 사교형식이 내려올 수 있었던 두 기둥은 [보조정리 1](#lem1)의 등식 $$T_pZ=(\mathfrak{g}\cdot p)^{\omega}$$이다. 이 한 등식이 (i)에서는 $$\iota^\ast\omega$$의 퇴화방향이 정확히 orbit 방향임을, nondegeneracy에서는 그 퇴화방향을 몫으로 죽이고 나면 남는 형식이 nondegenerate임을 동시에 보장한다. coisotropic 부분다양체를 그 null 방향으로 나누어 사교다양체를 얻는 이 절차는 *coisotropic reduction*이라는 더 일반적인 구성의 특수한 경우이다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> 정리의 가정은 결론을 위한 충분조건일 뿐 최선은 아니다. $$G$$의 compactness는 작용이 proper함을 보장하기 위한 것이며, $$G$$가 noncompact이더라도 작용이 $$\mu^{-1}(0)$$ 위에서 자유롭고 proper하기만 하면 같은 결론이 성립한다. 자유로운 작용 대신 단지 locally free인 경우에는 $$0$$이 여전히 regular value여서 $$\mu^{-1}(0)$$은 매끄럽지만 몫 $$\mu^{-1}(0)/G$$은 매끄러운 다양체가 아니라 orbifold가 될 수 있으며, $$\omega_{\mathrm{red}}$$은 orbifold 위의 사교형식으로 살아남는다. Stabilizer가 더 큰 일반적인 경우의 축약은 stratified symplectic space를 낳는다.

</div>

## 일반값과 coadjoint orbit에서의 축약

운동량 사상의 값으로 $$0$$이 아니라 임의의 $$\xi\in\mathfrak{g}^\ast$$을 고를 수도 있다. 그러나 $$G$$가 nonabelian이면 fiber $$\mu^{-1}(\xi)$$은 일반적으로 $$G$$-불변이 아니다. equivariance ([§운동량 사상, ⁋정의 2](/ko/math/symplectic_geometry/moment_map#def2)의 조건 2)에 의해 $$\mu(g\cdot p)=\Ad_g^\ast\mu(p)$$이므로, $$g\cdot p$$이 다시 $$\mu^{-1}(\xi)$$에 들려면 $$\Ad_g^\ast\xi=\xi$$, 즉 $$g$$이 $$\xi$$의 stabilizer $$G_\xi$$에 속해야 한다. 따라서 $$\mu^{-1}(\xi)$$을 보존하는 것은 전체 $$G$$이 아니라 부분군 $$G_\xi$$이다.

<div class="definition" markdown="1">

<ins id="def4">**정의 4**</ins> $$(M,\omega,G,\mu)$$를 Hamiltonian $$G$$-공간, $$\xi\in\mathfrak{g}^\ast$$을 $$\mu$$의 regular value라 하고, $$G_\xi=\{g\in G:\Ad_g^\ast\xi=\xi\}$$을 $$\xi$$의 coadjoint stabilizer라 하자. $$G_\xi$$이 $$\mu^{-1}(\xi)$$ 위에 자유롭고 proper하게 작용할 때, $$\xi$$에서의 *축약공간*을

$$M /\!\!/_{\!\xi}\, G:=\mu^{-1}(\xi)/G_\xi$$

으로 정의한다.

</div>

이 정의에서 $$\xi=0$$이면 $$\Ad_g^\ast 0=0$$이 모든 $$g$$에 대해 성립하므로 $$G_0=G$$이고, 따라서 $$M /\!\!/_{\!0}\,G=M /\!\!/ G$$은 [정리 2](#thm2)의 축약공간으로 환원된다. $$G$$가 abelian, 가령 torus이면 coadjoint 작용이 자명하여 모든 $$\xi$$에 대해 $$G_\xi=G$$이므로, abelian 군에 대해서는 임의의 regular value $$\xi$$에서 곧바로 $$\mu^{-1}(\xi)/G$$을 취할 수 있다. 일반적인 $$\xi$$에서의 축약이 다시 사교다양체임은 다음과 같이 $$0$$에서의 축약으로 환원된다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5**</ins> [정의 4](#def4)의 가정 아래 축약공간 $$M /\!\!/_{\!\xi}\,G=\mu^{-1}(\xi)/G_\xi$$은 자연스러운 사교형식을 갖는 매끄러운 다양체이며, 그 차원은

$$\dim M /\!\!/_{\!\xi}\, G=\dim M-\dim G-\dim G_\xi$$

이다. 더 나아가, $$\mathcal{O}_\xi=\{\Ad_g^\ast\xi:g\in G\}\subseteq\mathfrak{g}^\ast$$을 $$\xi$$을 지나는 coadjoint orbit이라 하면

$$M /\!\!/_{\!\xi}\, G\cong\mu^{-1}(\mathcal{O}_\xi)/G$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

부분군 $$G_\xi\subseteq G$$은 Lie 부분군이고 그 Lie algebra는 $$\mathfrak{g}_\xi=\{X\in\mathfrak{g}:\ad_X^\ast\xi=0\}$$이다. $$\mu$$을 $$\mu^{-1}(\xi)$$의 근방에서 affine 평행이동하여 생각하면 $$\xi$$을 regular value로 갖는 상황은 국소적으로 $$0$$을 regular value로 갖는 상황과 같으므로, $$\mu^{-1}(\xi)$$은 여차원 $$\dim G$$의 매끄러운 부분다양체이다.

이제 $$G_\xi$$-작용에 대한 운동량 사상을 만든다. 포함 $$\mathfrak{g}_\xi\hookrightarrow\mathfrak{g}$$의 dual restriction $$r:\mathfrak{g}^\ast\rightarrow\mathfrak{g}_\xi^\ast$$을 합성한 $$\mu_\xi:=r\circ(\mu-\xi):M\rightarrow\mathfrak{g}_\xi^\ast$$은 $$G_\xi$$-작용의 운동량 사상이고, $$\mu^{-1}(\xi)\subseteq\mu_\xi^{-1}(0)$$이다. $$\mu^{-1}(\xi)$$ 위에서 $$G_\xi$$이 자유롭고 proper하게 작용하므로 [정리 2](#thm2)의 증명과 동일한 논법이 적용되어, $$T_p(\mu^{-1}(\xi))$$의 $$\omega_p$$에 대한 퇴화방향이 정확히 $$\mathfrak{g}_\xi\cdot p$$임을 확인하면 사교형식이 몫 $$\mu^{-1}(\xi)/G_\xi$$으로 내려온다. 차원은

$$\dim\mu^{-1}(\xi)/G_\xi=(\dim M-\dim G)-\dim G_\xi$$

이다.

동형 $$\mu^{-1}(\xi)/G_\xi\cong\mu^{-1}(\mathcal{O}_\xi)/G$$은 다음 사상에서 온다. equivariance에 의해 $$\mu(\mu^{-1}(\mathcal{O}_\xi))=\mathcal{O}_\xi$$이고 $$G$$이 $$\mu^{-1}(\mathcal{O}_\xi)$$을 보존한다. 포함 $$\mu^{-1}(\xi)\hookrightarrow\mu^{-1}(\mathcal{O}_\xi)$$은 $$G_\xi$$-동변이므로 몫 사이의 사상

$$\mu^{-1}(\xi)/G_\xi\rightarrow\mu^{-1}(\mathcal{O}_\xi)/G$$

을 유도한다. 이 사상이 전단사임은 다음에서 나온다. $$\mathcal{O}_\xi\cong G/G_\xi$$이므로 임의의 $$q\in\mu^{-1}(\mathcal{O}_\xi)$$에 대해 $$\mu(q)=\Ad_g^\ast\xi$$인 $$g$$이 존재하여 $$g^{-1}\cdot q\in\mu^{-1}(\xi)$$이고, 따라서 모든 $$G$$-orbit은 $$\mu^{-1}(\xi)$$을 만난다 (전사). 그 교집합은 $$\mu^{-1}(\xi)$$ 위의 한 $$G_\xi$$-orbit과 정확히 일치하므로 (단사) 사상은 전단사이며, 매끄러운 동형이다.

</details>

동형 $$M /\!\!/_{\!\xi}\,G\cong\mu^{-1}(\mathcal{O}_\xi)/G$$은 일반값에서의 축약을 다시 $$G$$ 전체에 대한 몫으로 보는 관점을 준다. coadjoint orbit $$\mathcal{O}_\xi$$ 자체가 Kirillov-Kostant-Souriau 형식이라 불리는 표준 사교형식을 갖는 Hamiltonian $$G$$-공간인데, 위 동형은 $$\xi$$에서의 축약이 곱공간 $$M\times\mathcal{O}_\xi^{-}$$을 $$0$$에서 축약한 것과 같음을 보이는 *shifting trick*으로 이어진다. 여기서 $$\mathcal{O}_\xi^{-}$$은 부호를 뒤집은 사교형식을 준 orbit이며, 곱의 운동량 사상은 [§운동량 사상, ⁋명제 6](/ko/math/symplectic_geometry/moment_map#prop6)에 따라 성분별 합이 된다. 이로써 임의 값에서의 축약 이론 전체가 [정리 2](#thm2)의 영점 축약으로 통일된다.

## 복소 사영공간

가장 투명한 예시는 $$\mathbb{C}^{n+1}$$ 위의 대각 원작용을 축약하여 $$\mathbb{CP}^n$$을 얻는 것이다. 이 예시는 [§운동량 사상, ⁋예시 8](/ko/math/symplectic_geometry/moment_map#ex8) 뒤에서 언급한 $$S^{2n+1}$$ 위 제약과 대각 $$S^1$$ 몫이 정확히 사교 축약임을 확인해 준다.

<div class="example" markdown="1">

<ins id="ex6">**예시 6**</ins> $$M=\mathbb{C}^{n+1}$$에 좌표 $$z_j=x_j+iy_j$$ ($$j=0,1,\ldots,n$$)와 사교형식 $$\omega=\sum_{j=0}^n dx_j\wedge dy_j$$을 주자 ([§운동량 사상, ⁋예시 8](/ko/math/symplectic_geometry/moment_map#ex8)). $$G=S^1$$이 모든 좌표에 동시에 작용하는 *대각* 회전

$$t\cdot(z_0,\ldots,z_n)=(e^{2\pi it}z_0,\ldots,e^{2\pi it}z_n)$$

을 생각한다. 이는 $$\sum_j\lvert z_j\rvert^2$$을 보존하므로 $$\omega$$를 보존하는 Hamiltonian 작용이고, 예시 8의 계산을 대각 생성원 $$X=(1,\ldots,1)\in\mathbb{R}^{n+1}=\mathfrak{t}$$에 적용하면 운동량 사상은

$$\mu(z)=-\pi\sum_{j=0}^n\lvert z_j\rvert^2+c$$

의 꼴이며, 상수 $$c$$을 [§운동량 사상, ⁋명제 4](/ko/math/symplectic_geometry/moment_map#prop4)의 자유도를 써서 적절히 택하면

$$\mu(z)=\frac{\pi}{2}\Bigl(\sum_{j=0}^n\lvert z_j\rvert^2-1\Bigr)$$

로 정규화할 수 있다. 그럼 영점집합은

$$\mu^{-1}(0)=\Bigl\{z\in\mathbb{C}^{n+1}:\sum_{j=0}^n\lvert z_j\rvert^2=1\Bigr\}=S^{2n+1}$$

으로 단위 구면이다. $$z=0$$은 영점집합에 없으므로 그 위에서 $$d\mu$$은 처처에서 nonzero, 즉 $$0$$은 regular value이고, $$S^1$$이 구면 위에 자유롭게 (그리고 compact이므로 proper하게) 작용한다. 따라서 [정리 2](#thm2)의 가정이 모두 충족된다.

축약공간은

$$\mathbb{C}^{n+1} /\!\!/ S^1=S^{2n+1}/S^1=\mathbb{CP}^n$$

으로, 대각 $$S^1$$로 나눈 구면은 정의에 의해 복소 사영공간이다. 차원은 $$\dim\mathbb{C}^{n+1}-2\dim S^1=2(n+1)-2=2n$$으로 $$\mathbb{CP}^n$$의 실차원과 일치한다. 정리가 주는 사교형식 $$\omega_{\mathrm{red}}$$은 정확히 $$\mathbb{CP}^n$$ 위의 *Fubini-Study form* $$\omega_{\mathrm{FS}}$$이며, 등식 $$\pi^\ast\omega_{\mathrm{FS}}=\iota^\ast\omega$$은 구면 위로 당겨 온 표준형식이 Hopf 사영 $$\pi:S^{2n+1}\rightarrow\mathbb{CP}^n$$을 통해 Fubini-Study form으로 내려옴을 말한다.

</div>

이 예시는 [§운동량 사상, ⁋예시 8](/ko/math/symplectic_geometry/moment_map#ex8) 뒤에서 윤곽만 그렸던 절차를 사교 축약의 언어로 완성한다. 거기서는 $$T^{n+1}$$ 작용을 다루며 대각 $$S^1$$을 나눈 뒤 남은 $$T^n=T^{n+1}/S^1$$의 운동량 다면체가 단체가 됨을 보였는데, 그 "대각 $$S^1$$을 나누는" 단계가 바로 위의 $$\mathbb{C}^{n+1} /\!\!/ S^1=\mathbb{CP}^n$$이다. 더 일반적으로, 원작용을 음이 아닌 운동량 값 $$\xi$$에서 축약하면 구면의 반지름이 바뀌어 Fubini-Study form이 상수배만큼 재조정된 $$\mathbb{CP}^n$$을 얻으며, 이렇게 운동량 값을 변화시키며 얻는 축약공간들의 족이 사교 축약을 토릭 기하 및 기하학적 불변식론과 잇는 다리가 된다.

<div class="remark" markdown="1">

<ins id="rmk7">**참고 7**</ins> 사교 축약은 [§운동량 사상, ⁋명제 3](/ko/math/symplectic_geometry/moment_map#prop3)의 Noether 정리와 같은 뿌리에서 나온 쌍둥이 절차이다. Noether 정리가 대칭성으로부터 보존량 $$\mu$$을 얻어 그 값을 고정하는 것이라면, 사교 축약은 그렇게 고정한 등위면 $$\mu^{-1}(\xi)$$ 위에서 대칭의 작용으로 나누어 자유도를 실제로 제거하는 것이다. $$G$$-불변 Hamiltonian $$H$$은 $$\mu^{-1}(\xi)$$ 위로 제한되고 다시 축약공간 $$M /\!\!/_{\!\xi}\,G$$ 위의 함수 $$H_{\mathrm{red}}$$으로 내려오며, $$M$$ 위의 $$H$$-흐름은 정확히 축약공간 위의 $$H_{\mathrm{red}}$$-흐름으로 사영된다. 이것이 고전역학에서 보존량을 이용해 위상공간의 차원을 낮추는 절차의 좌표 없는 정식화이다.

</div>

---

**참고문헌**

**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[MS]** D. McDuff and D. Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017.  
**[MW]** J. Marsden and A. Weinstein, *Reduction of symplectic manifolds with symmetry*, Rep. Mathematical Phys. **5** (1974), 121–130.  
**[Mey]** K. R. Meyer, *Symmetries and integrals in mechanics*, in *Dynamical Systems* (M. M. Peixoto, ed.), Academic Press, 1973, pp. 259–272.  
