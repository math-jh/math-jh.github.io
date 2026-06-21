---
title: "Darboux 정리"
description: "Moser의 방법을 이용하여 모든 symplectic manifold가 국소적으로 표준 모델과 symplectomorphic함을 보이는 Darboux 정리를 증명하고, 그 대역적 일반화인 Moser 안정성 정리를 다룬다."
excerpt: "Moser의 trick으로 증명하는 Darboux 정리와 Moser 안정성"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/darboux_theorem
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2026-06-20
weight: 3.5

published: false

---

[§사교다양체, ⁋참고 8](/ko/math/symplectic_geometry/symplectic_manifold#rmk8)에서 우리는 임의의 symplectic manifold $$(M,\omega)$$가 각 점 근방에서 표준 모델 $$(\mathbb{R}^{2n},\omega_0)$$과 symplectomorphic하다는 *Darboux 정리*를 예고하였다. 이는 symplectic 기하가 리만 기하와 근본적으로 다른 지점이다. 리만 기하에서는 곡률이라는 국소 불변량이 존재하여, 두 리만 다양체가 국소적으로 isometric하려면 곡률 텐서가 일치해야 한다. 반면 symplectic 기하에는 이러한 국소 불변량이 전혀 없다. 모든 symplectic manifold는 같은 차원이라면 국소적으로 완전히 동일하게 생겼으며, symplectic 기하의 모든 비자명한 내용은 대역적인 차원에서 비로소 나타난다.

이 사실을 증명하는 현대적인 방법은 J. Moser가 1965년에 도입한 *Moser의 방법<sub>Moser's method</sub>*, 혹은 *Moser의 trick*이다. 그 핵심은 두 symplectic form을 직선으로 잇는 경로 $$\omega_t$$를 만든 뒤, 이 경로를 따라 form을 옮겨 주는 시간의존 벡터장을 nondegeneracy를 이용해 풀어내는 것이다. 이 방법은 Darboux 정리뿐 아니라 그 대역적 일반화인 Moser 안정성 정리까지 한꺼번에 준다. 우리는 먼저 증명에 필요한 Poincaré lemma의 정밀한 형태를 정리한 후, Moser의 방법을 전개하여 Darboux 정리를 증명하고, 끝으로 Moser 안정성 정리를 서술한다.

## Poincaré lemma

Moser의 방법은 $$\omega-\omega_0$$가 exact라는 사실, 즉 적당한 $$1$$-form $$\alpha$$에 대하여 $$\omega-\omega_0=d\alpha$$임을 필요로 한다. 한 점 근방의 작은 공으로 정의역을 제한하면 closed form은 언제나 exact가 되는데, 이것이 Poincaré lemma이다. ([\[대수적 위상수학\] §코호몰로지](/ko/math/algebraic_topology/cohomology)) 우리의 증명에서는 단순히 $$d\alpha=\omega-\omega_0$$인 $$\alpha$$가 존재한다는 것뿐 아니라, 그 $$\alpha$$를 중심점에서 사라지도록 택할 수 있다는 정밀한 형태가 필요하다. 이를 위해 명시적인 homotopy operator를 구성한다.

<div class="proposition" markdown="1">

<ins id="lem1">**보조정리 1**</ins> 원점 $$0$$을 포함하는 볼록열린집합 $$U\subseteq\mathbb{R}^m$$ 위에서 정의된 closed $$k$$-form $$\beta$$ ($$k\geq 1$$)에 대하여, $$U$$ 위의 $$(k-1)$$-form $$\alpha$$가 존재하여 $$d\alpha=\beta$$를 만족한다. 더욱이 $$\beta_0=0$$이면, 즉 $$\beta$$가 원점에서 사라지면, 위의 $$\alpha$$를 $$\alpha_0=0$$이도록 택할 수 있다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$U$$가 원점에 대해 볼록이므로, 각 $$t\in[0,1]$$에 대하여 scaling map $$\psi_t(x)=tx$$는 $$U$$를 $$U$$ 안으로 보낸다. $$\psi_1=\id_U$$이고 $$\psi_0$$은 상수사상 $$x\mapsto 0$$이다. 이 homotopy를 따라 $$k$$-form들에 작용하는 operator $$h:\Omega^k(U)\rightarrow\Omega^{k-1}(U)$$를 다음과 같이 정의한다. $$x\in U$$에서 생성벡터장 $$V_t$$를 $$\frac{d}{dt}\psi_t(x)=x=V_t(\psi_t(x))$$로 두면 $$V_t(y)=y/t$$이며, 우리는

$$(h\beta)_x(v_1,\ldots,v_{k-1})=\int_0^1 \bigl(\iota_{V_t}(\psi_t^\ast\beta)\bigr)_x(v_1,\ldots,v_{k-1})\,dt=\int_0^1 t^{k-1}\beta_{tx}(x,v_1,\ldots,v_{k-1})\,dt$$

으로 둔다. 마지막 등식은 $$\psi_t^\ast\beta$$를 풀어 쓰고 $$\iota_{V_t}$$를 적용하여 $$t$$의 거듭제곱을 모은 것이다. 표준적인 계산에 의하여 이 operator는 chain homotopy 항등식

$$d(h\beta)+h(d\beta)=\psi_1^\ast\beta-\psi_0^\ast\beta$$

를 만족한다. ([\[미분다양체\] §리 미분, ⁋명제 4](/ko/math/manifolds/Lie_derivative#prop4)의 Cartan 공식 $$\mathcal{L}_{V_t}=d\iota_{V_t}+\iota_{V_t}d$$를 적분한 것이다.) 이제 $$\beta$$가 closed이므로 $$d\beta=0$$이고, $$k\geq 1$$이므로 $$\psi_0^\ast\beta=0$$이다. 따라서 $$\alpha=h\beta$$로 두면

$$d\alpha=d(h\beta)=\psi_1^\ast\beta=\beta$$

를 얻는다.

마지막으로 $$\beta_0=0$$인 경우를 보자. 위 적분식에서 $$\alpha_x=(h\beta)_x$$는 피적분함수 $$t^{k-1}\beta_{tx}(x,-)$$의 적분이다. $$x=0$$을 대입하면 모든 $$t$$에 대해 피적분함수가 $$\beta_0(0,-)=0$$이므로 $$\alpha_0=0$$이다.

</details>

위 보조정리에서 구성한 $$\alpha$$는 단지 존재할 뿐 아니라 $$\beta$$에 선형적으로 의존하므로, 본문에서 $$\beta=\omega-\omega_0$$에 적용할 때 $$\omega$$와 $$\omega_0$$이 한 점에서 일치하면 $$\beta$$가 그 점에서 사라지고, 따라서 $$\alpha$$ 또한 그 점에서 사라지도록 택할 수 있다. 이 마지막 성질은 Moser의 방법에서 생성하는 벡터장이 중심점을 고정점으로 갖게 하여, 흐름이 그 점 근방에서 짧은 시간 동안 잘 정의되도록 보장하는 데 결정적이다.

## Moser의 방법과 Darboux 정리

이제 Darboux 정리를 서술하고, Moser의 방법으로 증명한다. 증명의 골격은 다음과 같다. 한 점 $$p$$에서 출발하여, 우선 $$p$$에서 $$\omega$$를 표준형으로 만드는 좌표를 잡아 두 form $$\omega$$와 상수계수 form $$\omega_0$$이 $$p$$에서 일치하도록 한다. 그 다음 이 둘을 직선으로 잇는 경로 $$\omega_t$$를 만들고, 이 경로 전체가 작은 근방에서 symplectic임을 확인한 뒤, $$\omega_t$$를 $$\omega_0$$으로 끌어오는 isotopy를 nondegeneracy를 통해 구성한다.

<div class="proposition" markdown="1">

<ins id="thm2">**정리 2 (Darboux)**</ins> $$(M,\omega)$$가 $$2n$$차원 symplectic manifold라 하자. 그럼 임의의 점 $$p\in M$$마다 $$p$$의 열린근방 $$U$$와 좌표사상 $$\varphi:U\rightarrow\mathbb{R}^{2n}$$이 존재하여 $$\varphi(p)=0$$이고

$$\varphi^\ast\omega_0=\omega\vert_U$$

가 성립한다. 여기서 $$\omega_0=\sum_{i=1}^n dx_i\wedge dy_i$$은 $$\mathbb{R}^{2n}$$의 canonical symplectic form이다. 즉 $$U$$에서 좌표 $$(x_1,\ldots,x_n,y_1,\ldots,y_n)$$을 적당히 택하면 $$\omega=\sum_{i=1}^n dx_i\wedge dy_i$$로 적힌다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

문제가 국소적이므로, 우선 $$p$$ 근방의 임의의 좌표계를 잡아 상황을 $$\mathbb{R}^{2n}$$의 원점 $$0$$ 근방에서의 문제로 옮긴다. 즉 $$0$$의 열린근방 위에서 symplectic form $$\omega$$가 주어졌고 $$p$$가 $$0$$에 대응한다고 가정해도 좋으며, 우리의 목표는 $$0$$ 근방에서 정의된 diffeomorphism $$\varphi$$로 $$0$$을 고정하고 $$\varphi^\ast\omega_0=\omega$$를 만족하는 것을 찾는 것이다.

**1단계 (한 점에서의 표준화).** $$\omega_0$$의 원점에서의 값 $$\omega_0\vert_0$$과 $$\omega$$의 원점에서의 값 $$\omega\vert_0$$을 $$T_0\mathbb{R}^{2n}$$ 위의 두 linear symplectic form으로 비교한다. ([§사교벡터공간, ⁋보조정리 2](/ko/math/symplectic_geometry/linear_symplectic_geometry#lem2)에 의하여) 두 linear symplectic form은 적당한 선형동형으로 옮겨지므로, 원점에서의 선형좌표변환 $$A\in\GL(2n,\mathbb{R})$$을 취하여 $$A^\ast(\omega_0\vert_0)=\omega\vert_0$$이 성립하도록 할 수 있다. $$A$$로 좌표를 한 번 더 바꾸면, 처음부터

$$\omega\vert_0=\omega_0\vert_0\qquad\text{(원점 }0\text{에서)}$$

라고 가정해도 좋다. 즉 $$\omega$$와 $$\omega_0$$은 이제 원점에서 정확히 같은 값을 갖는다.

**2단계 (경로의 구성).** 두 form을 직선으로 잇는 form들의 족을

$$\omega_t=\omega_0+t(\omega-\omega_0)=(1-t)\omega_0+t\omega,\qquad t\in[0,1]$$

으로 정의한다. 각 $$\omega_t$$는 closed인 두 form의 일차결합이므로 $$d\omega_t=0$$이다. 한편 nondegeneracy를 살펴보자. 원점에서는 $$\omega\vert_0=\omega_0\vert_0$$이므로 모든 $$t$$에 대해

$$\omega_t\vert_0=(1-t)\,\omega_0\vert_0+t\,\omega\vert_0=\omega_0\vert_0$$

이고, 이는 nondegenerate이다. Nondegeneracy는 $$(\omega_t)_x^{\,n}\neq 0$$이라는 열린조건이고 $$[0,1]$$이 compact이므로, $$0$$의 충분히 작은 열린공 $$B$$가 존재하여 모든 $$x\in B$$와 모든 $$t\in[0,1]$$에 대해 $$(\omega_t)_x$$가 nondegenerate이도록 할 수 있다. 따라서 $$B$$ 위에서 $$\{\omega_t\}_{t\in[0,1]}$$은 symplectic form들의 경로이다.

**3단계 ($$\alpha$$의 선택).** $$\omega-\omega_0$$은 $$B$$ 위에서 closed이고, $$B$$가 볼록이므로 [보조정리 1](#lem1)에 의하여 $$1$$-form $$\alpha$$가 존재하여

$$d\alpha=\omega-\omega_0$$

을 만족한다. 더욱이 1단계에 의하여 $$\omega-\omega_0$$은 원점에서 사라지므로, [보조정리 1](#lem1)의 정밀한 형태에 의해 $$\alpha_0=0$$이도록 택할 수 있다.

**4단계 (벡터장의 구성).** 각 $$t\in[0,1]$$에 대하여 $$\omega_t$$가 $$B$$ 위에서 nondegenerate이므로, 대응 $$X\mapsto\iota_X\omega_t$$는 벡터장과 $$1$$-form 사이의 동형이다. ([§사교다양체](/ko/math/symplectic_geometry/symplectic_manifold)) 따라서 시간의존 벡터장 $$X_t$$를

$$\iota_{X_t}\omega_t=-\alpha\tag{$\ast$}$$

으로 유일하게 정의할 수 있다. 원점에서는 $$\alpha_0=0$$이므로 $$\iota_{(X_t)_0}(\omega_t)_0=0$$이고, $$(\omega_t)_0$$이 nondegenerate이므로 $$(X_t)_0=0$$이다. 즉 원점은 모든 $$t$$에 대해 $$X_t$$의 영점이다.

이제 $$X_t$$의 흐름 $$\phi_t$$, 즉 $$\phi_0=\id$$이고 $$\frac{d}{dt}\phi_t(x)=X_t(\phi_t(x))$$를 만족하는 isotopy를 생각한다. 일반적으로 시간의존 벡터장의 흐름은 짧은 시간 동안만 정의될 수 있으나, 원점이 $$X_t$$의 영점이므로 흐름은 원점을 고정하며, 흐름의 정의역에 대한 연속의존성에 의하여 ([\[미분다양체\] §벡터장, ⁋정리 6](/ko/math/manifolds/vector_fields#thm6)) 원점의 충분히 작은 열린근방 $$U\subseteq B$$가 존재하여 $$\phi_t$$가 모든 $$t\in[0,1]$$에 대해 $$U$$ 위에서 정의되고 $$\phi_t(U)\subseteq B$$이도록 할 수 있다.

**5단계 (Cartan 공식 계산).** $$U$$ 위에서 $$\phi_t^\ast\omega_t$$가 $$t$$에 무관하게 일정함을 보인다. $$t$$에 대해 미분하면

$$\frac{d}{dt}(\phi_t^\ast\omega_t)=\phi_t^\ast\left(\mathcal{L}_{X_t}\omega_t+\frac{d\omega_t}{dt}\right)$$

이다. 여기서 첫째 항은 흐름에 의한 pullback의 시간미분이 Lie derivative로 주어진다는 사실에서, 둘째 항은 $$\omega_t$$ 자체가 $$t$$에 의존하는 부분에서 나온다. 이제 Cartan 공식 $$\mathcal{L}_{X_t}=d\iota_{X_t}+\iota_{X_t}d$$ ([\[미분다양체\] §리 미분, ⁋명제 4](/ko/math/manifolds/Lie_derivative#prop4))를 적용하고, $$\omega_t$$가 closed이므로 $$\iota_{X_t}(d\omega_t)=0$$임과 $$\frac{d\omega_t}{dt}=\omega-\omega_0=d\alpha$$임을 쓰면

$$\begin{aligned}
\mathcal{L}_{X_t}\omega_t+\frac{d\omega_t}{dt}&=d(\iota_{X_t}\omega_t)+\iota_{X_t}(d\omega_t)+d\alpha\\
&=d(\iota_{X_t}\omega_t)+d\alpha\\
&=d(\iota_{X_t}\omega_t+\alpha)
\end{aligned}$$

을 얻는다. 그런데 $$(\ast)$$에 의하여 $$\iota_{X_t}\omega_t+\alpha=0$$이므로 괄호 안이 $$0$$이고, 따라서

$$\frac{d}{dt}(\phi_t^\ast\omega_t)=\phi_t^\ast\,d(0)=0$$

이다. 즉 $$\phi_t^\ast\omega_t$$는 $$t$$에 무관하게 일정하다.

**6단계 (결론).** 5단계로부터 $$U$$ 위에서

$$\phi_1^\ast\omega_1=\phi_0^\ast\omega_0=\id^\ast\omega_0=\omega_0$$

이다. 한편 $$\omega_1=\omega$$이므로, $$\phi_1$$은 원점을 고정하는 diffeomorphism이며 $$\phi_1^\ast\omega=\omega_0$$을 만족한다. 따라서 $$\varphi=\phi_1$$로 두면 $$\varphi^\ast\omega_0$$이 아니라 $$\phi_1^\ast\omega=\omega_0$$을 얻으므로, 원하는 좌표사상은 $$\varphi=\phi_1^{-1}$$이다. 실제로 $$\phi_1^\ast\omega=\omega_0$$의 양변에 $$(\phi_1^{-1})^\ast$$를 적용하면 $$\omega=(\phi_1^{-1})^\ast\omega_0$$, 즉 $$(\phi_1^{-1})^\ast\omega_0=\omega$$이고, $$\phi_1^{-1}$$은 원점을 고정한다. 처음에 잡은 좌표계와 1단계의 선형변환을 합성하면, 이는 곧 $$M$$의 원래 점 $$p$$ 근방에서 $$\varphi(p)=0$$, $$\varphi^\ast\omega_0=\omega$$를 만족하는 좌표사상을 준다.

</details>

위 증명에서 얻은 좌표 $$(x_1,\ldots,x_n,y_1,\ldots,y_n)$$을 *Darboux 좌표<sub>Darboux coordinates</sub>*라 부른다. 이 좌표에서 [§사교다양체, ⁋정의 6](/ko/math/symplectic_geometry/symplectic_manifold#def6)의 Hamiltonian 벡터장은 [§고전역학, ⁋명제 1](/ko/math/symplectic_geometry/classical_mechanics#prop1)의 Hamilton 방정식 그대로 적히므로, Darboux 정리는 모든 symplectic manifold가 국소적으로 고전역학의 phase space와 동일함을 말한다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> Moser의 방법의 핵심은 두 군데에서 nondegeneracy를 사용한다는 점이다. 첫째로 경로 $$\omega_t$$ 전체가 작은 근방에서 symplectic이어야 하며, 둘째로 그래야만 $$(\ast)$$에서 $$1$$-form $$\alpha$$를 벡터장 $$X_t$$로 풀어낼 수 있다. 만일 $$\omega$$가 nondegenerate가 아니었다면, 가령 일반적인 closed $$2$$-form에 대해서는 이 방법이 작동하지 않으며, 실제로 그러한 form에는 국소 불변량 (가령 각 점에서의 rank의 변화)이 존재할 수 있다. 또한 증명은 본질적으로 *왜* 국소 불변량이 없는지를 설명한다. 두 symplectic form을 잇는 직선경로가 항상 symplectic으로 유지되며, 그 경로를 따라 흐름으로 옮길 수 있기 때문이다.

</div>

## Moser 안정성 정리

Moser의 방법은 한 점 근방이 아니라 compact manifold 전체에서도 작동하며, 이때 얻어지는 결과가 Moser 안정성 정리이다. Darboux 정리에서는 두 form $$\omega_0$$과 $$\omega$$이 한 점에서 일치한다는 사실로부터 $$\alpha$$가 그 점에서 사라지게 만들어 흐름이 짧은 시간 동안 존재함을 보장하였다. 대역적인 경우에는 $$M$$이 compact라는 가정이 흐름의 대역적 존재를 보장하는 역할을 대신하며, $$\omega-\omega_0$$이 exact라는 조건이 $$\alpha$$의 존재를 준다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Moser 안정성)**</ins> $$M$$이 경계가 없는 compact manifold이고, $$\{\omega_t\}_{t\in[0,1]}$$이 $$M$$ 위의 symplectic form들의 $$C^\infty$$ 경로라 하자. 만일 de Rham cohomology class $$[\omega_t]\in H^2_{\mathrm{dR}}(M)$$이 모든 $$t$$에 대해 일정하다면, isotopy $$\{\phi_t\}_{t\in[0,1]}$$이 존재하여 $$\phi_0=\id$$이고

$$\phi_t^\ast\omega_t=\omega_0$$

이 모든 $$t$$에 대해 성립한다. 특히 $$\phi_1$$은 $$(M,\omega_0)$$과 $$(M,\omega_1)$$ 사이의 symplectomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$[\omega_t]$$가 $$t$$에 무관하게 일정하므로, 그 시간미분의 cohomology class는 $$\frac{d}{dt}[\omega_t]=\left[\frac{d\omega_t}{dt}\right]=0$$이다. 즉 각 $$t$$에 대하여 closed $$2$$-form $$\frac{d\omega_t}{dt}$$는 exact이다. 표준적인 논증에 의하여 ([\[대수적 위상수학\] §코호몰로지](/ko/math/algebraic_topology/cohomology)) 이 exact form들을 $$t$$에 대해 $$C^\infty$$로 의존하는 $$1$$-form들의 족 $$\alpha_t$$로 적을 수 있어,

$$\frac{d\omega_t}{dt}=d\alpha_t$$

가 성립한다. 각 $$\omega_t$$가 nondegenerate이므로, 대응 $$X\mapsto\iota_X\omega_t$$가 동형이고 따라서 시간의존 벡터장 $$X_t$$를

$$\iota_{X_t}\omega_t=-\alpha_t$$

로 유일하게 정의한다. $$M$$이 compact이므로 $$X_t$$의 흐름 $$\phi_t$$는 모든 $$t\in[0,1]$$에 대해 $$M$$ 전체에서 정의된다. 이제 [정리 2](#thm2)의 5단계와 동일한 계산을 수행하면, Cartan 공식 ([\[미분다양체\] §리 미분, ⁋명제 4](/ko/math/manifolds/Lie_derivative#prop4))과 $$d\omega_t=0$$에 의하여

$$\frac{d}{dt}(\phi_t^\ast\omega_t)=\phi_t^\ast\left(\mathcal{L}_{X_t}\omega_t+\frac{d\omega_t}{dt}\right)=\phi_t^\ast\,d(\iota_{X_t}\omega_t+\alpha_t)=\phi_t^\ast\,d(0)=0$$

을 얻는다. 따라서 $$\phi_t^\ast\omega_t$$는 $$t$$에 무관하게 일정하며, $$\phi_0=\id$$이므로 $$\phi_t^\ast\omega_t=\omega_0$$이다. $$t=1$$로 두면 $$\phi_1^\ast\omega_1=\omega_0$$이므로 $$\phi_1$$은 symplectomorphism이다.

</details>

이 정리는 symplectic 구조가 cohomology class를 고정한 채로는 *변형에 대해 안정적*이라는 것을 말한다. 즉 같은 cohomology class를 갖는 두 symplectic form을 그 class를 유지하는 경로로 이을 수 있다면, 그 둘은 본질적으로 같은 symplectic manifold를 정의한다. Darboux 정리는 이 정리의 국소판으로 볼 수 있는데, 국소적으로는 $$H^2_{\mathrm{dR}}$$이 소멸하므로 cohomology class 조건이 자동으로 성립하고, compact성 대신 중심점을 고정점으로 갖는 흐름의 국소존재성이 그 역할을 대신한다.

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> Cohomology class가 일정하다는 가정은 본질적이다. 만일 $$[\omega_0]\neq[\omega_1]$$이라면, symplectomorphism $$\phi_1$$은 $$\phi_1^\ast[\omega_1]=[\omega_0]$$을 강제하는데, $$\phi_1$$이 $$\id$$과 isotopic하다면 $$\phi_1^\ast$$는 $$H^2_{\mathrm{dR}}(M)$$ 위에서 항등사상이므로 $$[\omega_1]=[\omega_0]$$이어야 하기 때문이다. 가령 $$2$$차원 torus $$T^2$$ 위에서 area form의 전체 면적은 $$\int_{T^2}\omega=[\omega]\frown[T^2]$$로 cohomology class에 의해 결정되며, 면적이 다른 두 area form은 결코 symplectomorphic할 수 없다. 따라서 대역적인 symplectic 기하에는 Darboux 정리에도 불구하고 부피와 같은 대역 불변량이 존재한다.

</div>

---

**참고문헌**

**[MS]** D. McDuff and D. Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017.  
**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[Mos]** J. Moser, *On the volume elements on a manifold*, Trans. Amer. Math. Soc. **120** (1965), 286–294.  
