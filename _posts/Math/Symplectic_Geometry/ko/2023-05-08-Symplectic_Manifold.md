---
title: "사교다양체"
description: "다양체 위에 정의된 사교형식의 개념을 통해 사교다양체의 정의를 다룬다. 짝수차원에서만 존재하는 사교다양체의 기본 성질과 구조를 소개한다."
excerpt: "Symplectic manifold의 정의와 성질들"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/symplectic_manifold
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2023-05-08
weight: 3


drift_needed: true

---

**[MS]**에서는 symplectic vector space를 소개한 후, 시간을 좀 더 들여서 Maslov class를 소개하는 등등의 일을 한다. 우리는 이를 나중에 Floer theory를 다루며 필요할 때 소개하기로 하고, **[CdS]**를 따라 우선 symplectic manifold를 정의한다.

::: 정의 1
Manifold $M$ 위에 정의된 *symplectic form<sub>사교형식</sub>* $\omega$는 $\dd{\omega}=0$이고 모든 $p\in M$에 대하여 $\omega_p:T_pM\times T_pM\rightarrow \mathbb{R}$이 linear symplectic form이도록 하는 differential $2$-form을 뜻한다. 이 때 $(M,\omega)$를 *symplectic manifold<sub>사교다양체</sub>*라 부른다. 
:::

Symplectic manifold $(M,\omega)$에 대하여, 벡터공간 $T_pM$에는 linear symplectic form $\omega_p$가 주어져 있으므로 ([§사교벡터공간, ⁋정의 1](/ko/math/symplectic_geometry/linear_symplectic_geometry#def1)) $\dim T_pM$은 짝수이고, 따라서 $M$ 또한 짝수차원이어야 한다. 

## 예시

::: 예시 2
1. 유클리드 공간 $\mathbb{R}^{2n}$에 좌표 $(x_1,\ldots, x_n,y_1,\ldots, y_n)$를 주고 

	$$\omega_0=\sum_{i=1}^n \dd{x_i}\wedge \dd{y_i}$$

	으로 정의하면, 이는 상수계수 $2$-form이므로 $\dd{\omega_0}=0$이고 각 점에서 standard linear symplectic form을 주므로 nondegenerate이다. 이를 $\mathbb{R}^{2n}$의 *canonical symplectic form*이라 부르며, 이는 [§고전역학](/ko/math/symplectic_geometry/classical_mechanics)에서 phase space 위에 등장한 바로 그 form이다.

2. 임의의 manifold $Q$의 cotangent bundle $M=T^\ast Q$를 생각하자. Projection $\pi:T^\ast Q\rightarrow Q$에 대하여, 점 $(q,p)\in T^\ast Q$ (즉 $p\in T_q^\ast Q$)에서의 *tautological $1$-form* $\lambda$를 

	$$\lambda_{(q,p)}(\xi)=p\bigl(\dd{\pi_{(q,p)}}(\xi)\bigr),\qquad \xi\in T_{(q,p)}(T^\ast Q)$$

	으로 정의하고 $\omega=-\dd{\lambda}$라 하자. $Q$의 국소좌표 $(q_1,\ldots, q_n)$과 이에 대응되는 fiber 좌표 $(p_1,\ldots, p_n)$에서 $\lambda=\sum_i p_i\dd{q_i}$이므로 

	$$\omega=-\dd{\lambda}=\sum_{i=1}^n \dd{q_i}\wedge \dd{p_i}$$

	이고, 이는 1번의 형태와 같아 nondegenerate이며 $\omega=-\dd{\lambda}$는 exact이므로 closed이다. 이렇게 cotangent bundle은 항상 표준적인 symplectic 구조를 가지며, 이것이 고전역학의 phase space이다. 

3. Orientable surface $\Sigma$ 위의 nowhere-vanishing $2$-form(즉 area form) $\sigma$를 생각하자. $\Sigma$가 $2$차원이므로 $\dd{\sigma}$는 $3$-form, 즉 $0$이고, $\sigma$가 각 점에서 $0$이 아니므로 nondegenerate이다. 따라서 모든 orientable surface는 area form과 함께 symplectic manifold가 된다.
:::

Kähler manifold, 특히 Fubini--Study form을 갖춘 $\mathbb{CP}^n$ 또한 중요한 예시이지만, 이는 복소기하의 언어를 필요로 하므로 나중에 다룬다. 

## 부피형식과 방향

Nondegeneracy는 $\omega$의 최고차 거듭제곱이 사라지지 않게 하여, symplectic manifold에 자연스러운 방향을 부여한다. 

::: 명제 3
$2n$차원 symplectic manifold $(M,\omega)$에 대하여, $n$개의 wedge product

$$\omega^n=\underbrace{\omega\wedge\cdots\wedge\omega}_{n}$$

은 어디서도 사라지지 않는 $2n$-form, 즉 volume form이다. 따라서 $M$은 orientable이다.
:::
::: 증명
각 점 $p\in M$에서 $\omega_p$는 $T_pM$ 위의 linear symplectic form이므로, [§사교벡터공간, ⁋보조정리 2](/ko/math/symplectic_geometry/linear_symplectic_geometry#lem2)에 의하여 $T_pM$의 basis $e_1,\ldots, e_n,f_1,\ldots, f_n$이 존재하여 그 dual basis $e_1^\ast,\ldots, f_n^\ast$에 대해 

$$\omega_p=\sum_{i=1}^n e_i^\ast\wedge f_i^\ast$$

이 성립한다. (Nondegeneracy로부터 보조정리의 degenerate 부분 $u_j$들은 나타나지 않는다.) 그럼 

$$\omega_p^n=n!\,e_1^\ast\wedge f_1^\ast\wedge\cdots\wedge e_n^\ast\wedge f_n^\ast\neq 0$$

이다. 따라서 $\omega^n$은 어디서도 사라지지 않는 $2n$-form이고, nowhere-vanishing top-degree form은 곧 volume form이므로 $M$에 방향을 정의한다. ([\[미분다양체\] §향](/ko/math/manifolds/orientation)) 
:::

::: 참고 4
$M$이 boundary가 없는 compact symplectic manifold라면, $\omega$는 결코 exact일 수 없다. 만일 $\omega=\dd{\alpha}$라면, $\omega$가 closed이므로 

$$\omega^n=\dd{\alpha}\wedge\omega^{n-1}=\dd{(\alpha\wedge\omega^{n-1})}$$

이 exact가 되어, Stokes 정리에 의하여 ([\[미분다양체\] §스토크스 정리, ⁋따름정리 2](/ko/math/manifolds/stokes_theorem#cor2)) $\int_M\omega^n=0$이다. 그런데 [명제 3](#prop3)에서 $\omega^n$은 volume form이므로 그 적분은 $0$이 될 수 없어 모순이다. 이로부터 둘째 cohomology가 소멸하는 closed manifold, 가령 $n\geq 2$인 $S^{2n}$은 symplectic 구조를 가질 수 없음을 안다. 
:::

## Symplectomorphism

Symplectic manifold들 사이의 구조를 보존하는 morphism은 다음과 같다. 

::: 정의 5
두 symplectic manifold $(M,\omega)$, $(M',\omega')$ 사이의 diffeomorphism $\varphi:M\rightarrow M'$가 *symplectomorphism<sub>사교동형사상</sub>*이라는 것은 $\varphi^\ast\omega'=\omega$인 것이다. 
:::

리만기하의 isometry와는 달리, 다음 절과 [참고 8](#rmk8)에서 보듯 symplectomorphism은 국소적으로 항상 풍부하게 존재한다. 이것이 symplectic 기하가 리만 기하와 근본적으로 다른 지점이다. 

## 해밀턴 벡터장과 Poisson 괄호

Nondegeneracy의 가장 중요한 쓰임은, 함수의 미분을 벡터장으로 바꾸어 주는 것이다. 각 벡터장 $X$에 대하여 $1$-form $\iota_X\omega$를 $(\iota_X\omega)(Y)=\omega(X,Y)$로 정의하면, $\omega$가 nondegenerate이므로 대응 $X\mapsto\iota_X\omega$는 벡터장들과 $1$-form들 사이의 ($C^\infty(M)$-module로서의) isomorphism이 된다. 

::: 정의 6
Symplectic manifold $(M,\omega)$와 함수 $H\in C^\infty(M)$에 대하여, $H$의 *Hamiltonian vector field<sub>해밀턴 벡터장</sub>* $X_H$를 

$$\iota_{X_H}\omega=\dd{H}$$

을 만족하는 유일한 벡터장으로 정의한다. 
:::

위에서 본 대응이 isomorphism이므로 이러한 $X_H$는 실제로 유일하게 존재한다. $M=\mathbb{R}^{2n}$에 canonical form $\omega_0$를 준 경우 이 정의는 [§고전역학, ⁋명제 1](/ko/math/symplectic_geometry/classical_mechanics#prop1)의 Hamilton 방정식이 정의하던 바로 그 벡터장으로 환원되며, 따라서 $X_H$의 integral flow는 에너지 $H$ 아래에서의 물체의 운동을 기술한다. 

이 flow는 $\omega$를 보존한다. 실제로 [\[미분다양체\] §리 미분, ⁋명제 4](/ko/math/manifolds/Lie_derivative#prop4)의 Cartan's formula와 $\dd{\omega}=0$으로부터 

$$\mathcal{L}_{X_H}\omega=\iota_{X_H}\dd{\omega}+\dd{(\iota_{X_H}\omega)}=\dd{(\dd{H})}=0$$

이고, $X_H$의 flow $\varphi^t$에 대하여 $(\varphi^t)^\ast\omega$의 $t$에 대한 미분이 $(\varphi^t)^\ast(\mathcal{L}_{X_H}\omega)$이므로 $(\varphi^t)^\ast\omega=\omega$가 flow가 정의되는 범위에서 성립하기 때문이다. 곧 각각의 함수 $H\in C^\infty(M)$마다 symplectomorphism들의 $1$-parameter family가 하나씩 얻어진다. 

::: 정의 7
Symplectic manifold $(M,\omega)$와 두 함수 $f,g\in C^\infty(M)$에 대하여, 이들의 *Poisson 괄호<sub>Poisson bracket</sub>* $\{f,g\}$를 

$$\{f,g\}=\omega(X_f,X_g)$$

으로 정의한다.
:::

정의로부터 $\{f,g\}=(\iota_{X_f}\omega)(X_g)=\dd{f}(X_g)=X_g f$이므로, Poisson 괄호는 $g$를 따라 흐를 때의 $f$의 변화율이기도 하다. $\omega$가 antisymmetric이므로 $\{f,g\}=-\{g,f\}$이고, $X_f$가 derivation이므로 각 변수에 대해 Leibniz 법칙 $\{f,gh\}=\{f,g\}h+g\{f,h\}$가 성립한다. 뿐만 아니라 $\dd{\omega}=0$이라는 조건이 정확히 Jacobi 항등식 $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0$과 동치임을 보일 수 있으며, 따라서 $(C^\infty(M),\{-,-\})$는 Lie 대수를 이룬다. 

::: 참고 8
[예시 2](#ex2)의 1번은 단지 local model이 아니다. 다음 글에서 다룰 *Darboux 정리*는 임의의 symplectic manifold $(M,\omega)$가 각 점 근방에서 $(\mathbb{R}^{2n},\omega_0)$과 symplectomorphic함을 보여준다. 즉 symplectic manifold에는 곡률과 같은 국소 불변량이 존재하지 않으며, 모든 symplectic manifold는 국소적으로 동일하게 생겼다. 이것이 [정의 5](#def5) 이후에 언급한 "국소적 풍부함"의 정확한 의미이다. 
:::

## Lagrangian submanifold

선형 사교기하에서 Lagrangian subspace가 차지하던 위치를 ([§사교벡터공간, ⁋정의 3](/ko/math/symplectic_geometry/linear_symplectic_geometry#def3)) manifold 수준으로 끌어올린 것이 Lagrangian submanifold이다. 이는 사교기하에서 가장 중요한 부분다양체의 종류이다.

::: 정의 9
$2n$차원 symplectic manifold $(M,\omega)$의 부분다양체 $L\subseteq M$이 *Lagrangian submanifold<sub>라그랑지안 부분다양체</sub>*라는 것은, 포함사상 $\iota:L\hookrightarrow M$에 대하여 $\iota^\ast\omega=0$이고 $\dim L=n=(\dim M)/2$인 것이다.
:::

조건 $\iota^\ast\omega=0$은 각 점 $p\in L$에서 tangent space $T_pL\subseteq T_pM$ 위로 $\omega_p$가 항등적으로 $0$이라는 뜻, 곧 $T_pL$이 isotropic subspace라는 뜻이다. 여기에 차원조건이 더해지면 [§사교벡터공간, ⁋보조정리 4](/ko/math/symplectic_geometry/linear_symplectic_geometry#lem4)에 의하여 $T_pL$이 각 점에서 Lagrangian subspace가 된다. 곧 Lagrangian submanifold란 tangent space가 점마다 Lagrangian subspace인 부분다양체이다.

::: 예시 10
1. 곡면, 곧 $2$차원 symplectic manifold 위의 임의의 smooth한 곡선 (1차원 부분다양체) 은 Lagrangian이다. $1$차원 공간 위에서 반대칭 $2$-form은 항상 $0$이므로 $\iota^\ast\omega=0$이 자동이고, $\dim=1=(1/2)\cdot 2$이기 때문이다.

2. Cotangent bundle $T^\ast Q$ ([예시 2](#ex2)) 의 각 fiber $T_q^\ast Q$는 Lagrangian이다. 국소좌표에서 fiber는 $\{q=\text{const}\}$이고 그 tangent space는 $\partial/\partial p_i$들로 생성되는데, $\omega=\sum_i \dd{q_i}\wedge \dd{p_i}$를 이 위로 제한하면 모든 $\dd{q_i}$가 소멸하여 $0$이 된다. 차원도 $n=(\dim T^\ast Q)/2$이다.
:::

Cotangent bundle에서는 base $Q$ 방향으로 누운 부분다양체들이 $1$-form과 정확히 대응하며, 그 가운데 Lagrangian이 되는 것은 closed form뿐이다.

::: 명제 11
Manifold $Q$ 위의 $1$-form $\alpha$에 대하여, 그 graph

$$\Gamma_\alpha=\{(q,\alpha_q)\mid q\in Q\}\subseteq T^\ast Q$$

가 standard symplectic form $\omega=-\dd{\lambda}$ ([예시 2](#ex2)) 에 대해 Lagrangian submanifold인 것은 $\alpha$가 closed form ($\dd{\alpha}=0$) 인 것과 동치이다. 특히 zero section은 항상 Lagrangian이다.
:::
::: 증명
$1$-form $\alpha$를 section $s_\alpha:Q\rightarrow T^\ast Q$, $q\mapsto(q,\alpha_q)$로 보면 $\Gamma_\alpha=s_\alpha(Q)$이고 $s_\alpha$는 $Q$와 $\Gamma_\alpha$ 사이의 diffeomorphism이다. 핵심은 tautological $1$-form $\lambda$ ([예시 2](#ex2)) 의 pullback이 $s_\alpha^\ast\lambda=\alpha$라는 것이다. 실제로 임의의 $\xi\in T_qQ$에 대하여

$$(s_\alpha^\ast\lambda)(\xi)=\lambda_{(q,\alpha_q)}\bigl(\dd{s_\alpha}(\xi)\bigr)=\alpha_q\bigl(\dd{\pi}(\dd{s_\alpha}(\xi))\bigr)=\alpha_q\bigl(\dd{(\pi\circ s_\alpha)}(\xi)\bigr)=\alpha_q(\xi)$$

인데, 마지막 등식은 $\pi\circ s_\alpha=\id_Q$이기 때문이다. 따라서

$$s_\alpha^\ast\omega=s_\alpha^\ast(-\dd{\lambda})=-\dd{(s_\alpha^\ast\lambda)}=-\dd{\alpha}$$

이다. $s_\alpha$가 $Q$와 $\Gamma_\alpha$ 사이의 diffeomorphism이므로 $\Gamma_\alpha$ 위로의 $\omega$의 restriction이 $0$인 것은 $s_\alpha^\ast\omega=0$, 곧 $\dd{\alpha}=0$과 동치이다. 한편 $\dim\Gamma_\alpha=\dim Q=n=(\dim T^\ast Q)/2$는 언제나 성립하므로, $\Gamma_\alpha$가 Lagrangian인 것은 정확히 $\alpha$가 closed form인 것과 동치이다. $\alpha=0$이면 $\dd{\alpha}=0$이므로 zero section $\Gamma_0\cong Q$는 Lagrangian이다.
:::

::: 참고 12
Lagrangian submanifold는 symplectic manifold 사이의 morphism까지 포섭한다. 두 symplectic manifold $(M,\omega)$, $(M',\omega')$의 곱 $M\times M'$에 symplectic form $\Omega=\pi^\ast\omega-\pi'^\ast\omega'$ ($\pi,\pi'$는 각 인자로의 projection) 를 주면, diffeomorphism $\varphi:M\rightarrow M'$가 symplectomorphism ([정의 5](#def5)) 인 것은 그 graph $\Gamma_\varphi=\{(m,\varphi(m))\}$가 $(M\times M',\Omega)$의 Lagrangian submanifold인 것과 동치이다. 실제로 $j:M\rightarrow M\times M'$, $m\mapsto(m,\varphi(m))$에 대하여 $j^\ast\Omega=j^\ast\pi^\ast\omega-j^\ast\pi'^\ast\omega'=\omega-\varphi^\ast\omega'$이고 $\dim\Gamma_\varphi=\dim M=(\dim(M\times M'))/2$이므로, $\Gamma_\varphi$가 Lagrangian인 것이 $\varphi^\ast\omega'=\omega$와 동치이기 때문이다. 이처럼 사교 morphism마저 Lagrangian으로 환원되는 현상을 "symplectic category의 morphism은 Lagrangian이다"라는 Weinstein의 표어가 요약한다.
:::

---

**참고문헌**

**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[MS]** D. Mcduff and D. Salamon. *Introduction to symplectic topology*. Oxford graduate texts in mathematics. Oxford University Press, 2017.
