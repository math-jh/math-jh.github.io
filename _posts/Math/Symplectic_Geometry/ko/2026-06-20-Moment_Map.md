---
title: "운동량 사상"
description: "Symplectic manifold 위의 Hamiltonian 군작용과 운동량 사상을 정의하고, 그 기본 성질과 예시를 다룬다. 끝으로 Atiyah-Guillemin-Sternberg 볼록성 정리를 서술하여 toric 기하로의 다리를 놓는다."
excerpt: "Hamiltonian 군작용과 moment map, 그리고 볼록성 정리"

categories: [Math / Symplectic Geometry]
permalink: /ko/math/symplectic_geometry/moment_map
sidebar: 
    nav: "symplectic_geometry-ko"

date: 2026-06-20
weight: 3.7

published: false

---

[§사교다양체, ⁋정의 6](/ko/math/symplectic_geometry/symplectic_manifold#def6)에서 우리는 함수 $$H\in C^\infty(M)$$마다 nondegeneracy를 이용해 Hamiltonian 벡터장 $$X_H$$를 정의하였다. 이제 우리는 함수 하나가 아니라 Lie group $$G$$가 symplectic manifold $$(M,\omega)$$에 symplectomorphism으로 작용하는 상황을 생각한다. 이때 $$G$$의 Lie algebra $$\mathfrak{g}$$의 각 원소 $$X$$는 $$M$$ 위의 벡터장 $$X_M$$을 낳으며, 좋은 경우에는 이 $$X_M$$이 어떤 함수의 Hamiltonian 벡터장이 된다. 이 함수들을 $$\mathfrak{g}$$에 대해 한꺼번에 모은 것이 *운동량 사상<sub>moment map</sub>* $$\mu:M\rightarrow\mathfrak{g}^\ast$$이다.

운동량 사상은 고전역학에서 대칭성으로부터 보존량을 얻는 Noether 정리의 기하학적 형태이다. 회전 대칭이 각운동량을, 평행이동 대칭이 선운동량을 보존시키듯, 군작용의 각 일매개변수 부분군은 보존되는 함수 하나를 준다. 더 나아가 운동량 사상은 Marsden-Weinstein reduction의 출발점이며, torus 작용의 경우 그 상이 볼록 다면체가 되어 toric 기하와 Delzant 대응으로 이어진다. 우리는 먼저 fundamental 벡터장과 Hamiltonian 작용을 정의하고, 운동량 사상의 기본 성질과 표준적인 예시들을 살펴본 뒤, 끝으로 Atiyah-Guillemin-Sternberg 볼록성 정리를 서술한다.

## Fundamental 벡터장

Lie group $$G$$가 manifold $$M$$ 위에 왼쪽에서 매끄럽게 작용한다는 것은, 매끄러운 사상 $$\psi:G\times M\rightarrow M$$이 주어져 $$\psi(e,p)=p$$이고 $$\psi(g,\psi(h,p))=\psi(gh,p)$$가 성립하는 것이다. 우리는 $$\psi(g,p)$$를 간단히 $$g\cdot p$$로 적고, 고정된 $$g$$에 대한 사상 $$p\mapsto g\cdot p$$를 $$\psi_g:M\rightarrow M$$으로 적는다. 각 $$\psi_g$$는 diffeomorphism이다.

이 작용으로부터 $$\mathfrak{g}$$의 각 원소는 $$M$$ 위의 벡터장을 얻는다. $$X\in\mathfrak{g}$$에 대하여 exponential map ([\[리 이론\] §리 군, ⁋정의 16](/ko/math/lie_theory/Lie_groups#def16))이 일매개변수 부분군 $$t\mapsto\exp(tX)$$을 주므로, 이를 작용시켜 각 점 $$p$$를 지나는 곡선 $$t\mapsto\exp(tX)\cdot p$$를 얻는다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> Lie group $$G$$가 manifold $$M$$에 작용할 때, $$X\in\mathfrak{g}$$의 *fundamental vector field<sub>기본 벡터장</sub>* $$X_M$$을

$$X_M(p)=\left.\frac{d}{dt}\right\vert_{t=0}\bigl(\exp(tX)\cdot p\bigr)$$

으로 정의한다.

</div>

즉 $$X_M$$은 일매개변수 부분군 $$\exp(tX)$$의 흐름이 $$M$$ 위에 만드는 속도장이며, $$X_M$$의 흐름은 정확히 $$\psi_{\exp(tX)}$$이다. 대응 $$X\mapsto X_M$$은 선형이며, Lie bracket을 보존하는지의 여부는 부호의 관례에 따라 달라진다. 우리의 정의에서는 $$[X,Y]_M=-[X_M,Y_M]$$이 성립하여 부호 하나를 동반하는 Lie algebra 반준동형이 되는데, 이는 본문에서 직접 쓰이지 않으므로 [참고 5](#rmk5)로 미룬다.

이제 $$M$$이 symplectic manifold이고 $$G$$가 symplectomorphism으로 작용하는 경우, 즉 모든 $$g\in G$$에 대해 $$\psi_g^\ast\omega=\omega$$인 경우를 생각하자. 이를 $$X$$ 방향으로 미분하면 $$\mathcal{L}_{X_M}\omega=0$$을 얻는다. Cartan 공식 ([\[미분다양체\] §리 미분, ⁋명제 4](/ko/math/manifolds/Lie_derivative#prop4))과 $$d\omega=0$$에 의하여

$$0=\mathcal{L}_{X_M}\omega=d(\iota_{X_M}\omega)+\iota_{X_M}(d\omega)=d(\iota_{X_M}\omega)$$

이므로, $$1$$-form $$\iota_{X_M}\omega$$은 항상 closed이다. 만일 이것이 단지 closed일 뿐 아니라 exact라면, 즉 어떤 함수 $$\mu^X$$에 대해 $$\iota_{X_M}\omega=d\mu^X$$이라면 $$X_M$$은 $$\mu^X$$의 Hamiltonian 벡터장이 된다. Hamiltonian 작용은 이러한 $$\mu^X$$들을 $$X$$에 대해 선형이고 정합적으로 택할 수 있을 때를 가리킨다.

## Hamiltonian 작용과 운동량 사상

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> Symplectic manifold $$(M,\omega)$$ 위의 symplectomorphism에 의한 $$G$$-작용이 *Hamiltonian action<sub>해밀턴 작용</sub>*이라는 것은, 매끄러운 사상

$$\mu:M\rightarrow\mathfrak{g}^\ast$$

이 존재하여 다음 두 조건을 만족하는 것이다. 여기서 $$X\in\mathfrak{g}$$에 대해 함수 $$\mu^X:M\rightarrow\mathbb{R}$$을 $$\mu^X(p)=\langle\mu(p),X\rangle$$로, 즉 $$\mu(p)\in\mathfrak{g}^\ast$$를 $$X$$에서 평가한 값으로 정의한다.

1. 모든 $$X\in\mathfrak{g}$$에 대하여 $$d\mu^X=\iota_{X_M}\omega$$가 성립한다.
2. $$\mu$$는 $$\Ad^\ast$$-*equivariant*이다. 즉 $$G$$의 $$M$$ 위의 작용과 $$\mathfrak{g}^\ast$$ 위의 coadjoint 작용에 대하여 $$\mu(g\cdot p)=\Ad_g^\ast\bigl(\mu(p)\bigr)$$이다.

이때 $$\mu$$를 작용의 *moment map<sub>운동량 사상</sub>*이라 부르고, $$(M,\omega,G,\mu)$$를 *Hamiltonian $$G$$-공간*이라 부른다.

</div>

여기서 $$\mathfrak{g}^\ast$$ 위의 *coadjoint 작용* $$\Ad^\ast$$는 adjoint 작용 ([\[리 이론\] §리 군, ⁋정의 19](/ko/math/lie_theory/Lie_groups#def19))의 dual로 정의된다. 즉 $$\xi\in\mathfrak{g}^\ast$$, $$X\in\mathfrak{g}$$에 대하여 $$\langle\Ad_g^\ast\xi,X\rangle=\langle\xi,\Ad_{g^{-1}}X\rangle$$이다. 역원 $$g^{-1}$$이 들어가는 것은 $$g\mapsto\Ad_g^\ast$$가 왼쪽 작용이 되도록 하기 위함이다.

조건 1은 정의 1 직전의 관찰을 정합적으로 만든 것이다. 각 $$X$$마다 $$X_M$$의 Hamiltonian 함수 $$\mu^X$$를 주되, 그 함수가 $$X$$에 선형으로 의존하도록 $$\mathfrak{g}^\ast$$-값 사상 하나로 묶은 것이다. $$\mu^X$$가 $$X$$에 선형임은 $$\mu(p)$$가 $$\mathfrak{g}^\ast$$의 원소라는 데에 이미 담겨 있다. 조건 2는 운동량 사상이 군의 대칭성과 양립함을 요구하는데, 다음 명제에서 보듯 이는 조건 1로부터 거의 자동으로 따라온다.

운동량 사상의 가장 중요한 해석은 보존량이다. $$G$$-불변 함수 $$H\in C^\infty(M)$$, 즉 $$H\circ\psi_g=H$$인 함수를 Hamiltonian으로 갖는 흐름을 생각하면, $$\mu$$는 그 흐름을 따라 보존된다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3 (Noether)**</ins> $$(M,\omega,G,\mu)$$가 Hamiltonian $$G$$-공간이고 $$H\in C^\infty(M)$$이 $$G$$-불변이라 하자. 그럼 $$H$$의 Hamiltonian 벡터장 $$X_H$$의 흐름을 따라 $$\mu$$는 일정하다. 즉 각 $$X\in\mathfrak{g}$$에 대해 $$\mu^X$$는 $$X_H$$를 따라 보존되는 양이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mu^X$$가 $$X_H$$를 따라 변화하는 율은 Poisson 괄호 ([§사교다양체, ⁋정의 7](/ko/math/symplectic_geometry/symplectic_manifold#def7)) $$X_H\,\mu^X=\{\mu^X,H\}$$이다. $$H$$가 $$G$$-불변이므로 $$X$$ 방향으로 미분하면 $$X_M\,H=0$$, 즉 $$dH(X_M)=0$$이다. 한편 조건 1에 의하여 $$\iota_{X_M}\omega=d\mu^X$$이므로

$$\{\mu^X,H\}=-X_{\mu^X}H=-dH(X_{\mu^X})=-dH(X_M)=0$$

이다. 여기서 $$X_{\mu^X}=X_M$$은 조건 1과 Hamiltonian 벡터장의 유일성에서 온다. 따라서 $$\mu^X$$는 $$X_H$$의 흐름을 따라 일정하다.

</details>

이것이 운동량 사상이라는 이름의 유래이다. 고전역학에서 공간의 회전 대칭은 각운동량을, 평행이동 대칭은 선운동량을 보존량으로 주는데, 운동량 사상은 이 보존량들을 군작용 하나에 대해 한꺼번에 기술한다. 아래 [예시 9](#ex9)에서 보듯 cotangent bundle 위의 회전 작용의 운동량 사상은 실제로 고전적인 각운동량과 일치한다.

다음 명제는 운동량 사상의 존재와 유일성을 정리한다. 운동량 사상의 존재는 일반적으로 위상적 장애를 가지나, 일단 존재하면 그 자유도는 작다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$(M,\omega)$$ 위의 connected Lie group $$G$$의 symplectic 작용에 대하여 다음이 성립한다.

1. 조건 1을 만족하는 $$\mu:M\rightarrow\mathfrak{g}^\ast$$이 존재한다면, 또 하나의 그러한 $$\mu'$$은 $$\mu'=\mu+c$$ ($$c\in\mathfrak{g}^\ast$$ 상수)의 꼴이다. 단 $$M$$이 connected라고 가정한다.
2. $$M$$이 connected일 때, 조건 1을 만족하는 $$\mu$$가 조건 2 ($$\Ad^\ast$$-equivariance)도 만족할 필요충분조건은 사상 $$X\mapsto\mu^X$$이 Lie algebra 준동형, 즉 $$\{\mu^X,\mu^Y\}=\mu^{[X,Y]}$$인 것이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

**1.** 두 사상 $$\mu,\mu'$$이 조건 1을 만족하면, 각 $$X$$에 대해 $$d(\mu'^X-\mu^X)=\iota_{X_M}\omega-\iota_{X_M}\omega=0$$이다. $$M$$이 connected이므로 $$\mu'^X-\mu^X$$은 상수이고, 이 상수를 $$c(X)$$라 하면 $$X\mapsto c(X)$$는 선형이므로 $$c\in\mathfrak{g}^\ast$$를 정의한다. 즉 $$\mu'=\mu+c$$이다.

**2.** Coadjoint 작용을 $$X$$ 방향으로 미분하면 그 무한소 형태는 $$-\ad_X^\ast$$이다. $$\Ad^\ast$$-equivariance를 일매개변수 부분군 $$\exp(tY)$$에 대해 $$t$$로 미분하면, $$M$$이 connected이므로 equivariance는 다음의 무한소 형태와 동치이다.

$$X_M\,\mu^Y=-\langle\mu,[X,Y]\rangle=-\mu^{[X,Y]}\qquad\text{(모든 }X,Y\in\mathfrak{g}\text{에 대해)}$$

좌변을 풀어 쓰면 $$X_M\,\mu^Y=d\mu^Y(X_M)=\omega(Y_M,X_M)=\omega(X_{\mu^Y},X_{\mu^X})=\{\mu^Y,\mu^X\}=-\{\mu^X,\mu^Y\}$$이다. 여기서 조건 1로부터 오는 $$X_M=X_{\mu^X}$$, $$Y_M=X_{\mu^Y}$$와 Poisson 괄호의 정의, 그리고 $$\omega$$의 반대칭성을 사용하였다. 두 무한소 형태를 견주면 equivariance는 $$\{\mu^X,\mu^Y\}=\mu^{[X,Y]}$$과 동치이다.

</details>

1번에 의하면 운동량 사상은 존재할 경우 $$\mathfrak{g}^\ast$$의 상수만큼의 자유도를 갖는다. $$G$$가 가령 semisimple이어서 $$[\mathfrak{g},\mathfrak{g}]=\mathfrak{g}$$인 경우에는 2번의 준동형 조건이 이 상수를 강제로 고정하여 운동량 사상이 유일해진다. Compact group이나 torus의 경우에는 상수를 적절히 택해 equivariance가 성립하도록 만들 수 있다. 2번은 또한 운동량 사상이 Poisson 괄호와 Lie bracket을 잇는 준동형을 준다는 점을 보여 주며, 이는 Hamiltonian 작용을 Poisson 대수의 언어로 재서술하는 출발점이 된다.

<div class="remark" markdown="1">

<ins id="rmk5">**참고 5**</ins> Fundamental 벡터장의 대응 $$X\mapsto X_M$$에서 부호 하나가 나타나는 것은 왼쪽 작용의 결합법칙 $$\psi_g\circ\psi_h=\psi_{gh}$$ 때문이다. 일매개변수 부분군의 흐름을 합성하는 순서가 group과 vector field에서 반대로 작용하여 $$[X,Y]_M=-[X_M,Y_M]$$이 된다. 문헌에 따라서는 처음부터 $$X_M$$을 $$-\frac{d}{dt}\bigr\vert_{0}\exp(tX)\cdot p$$로 정의하거나 오른쪽 작용을 써서 준동형이 되게 하며, 이에 맞추어 운동량 사상의 정의 조건 1의 부호를 $$d\mu^X=-\iota_{X_M}\omega$$로 바꾸기도 한다. 우리는 **[CdS]**를 따라 위의 관례를 택하였다. 어느 관례를 택하든 운동량 사상의 상과 그 볼록성은 변하지 않는다.

</div>

운동량 사상은 군의 곱에 대해 자연스럽게 행동한다. 두 Hamiltonian 공간의 곱은 다시 Hamiltonian 공간이며, 그 운동량 사상은 성분별로 주어진다.

<div class="proposition" markdown="1">

<ins id="prop6">**명제 6**</ins> $$(M_1,\omega_1,G_1,\mu_1)$$과 $$(M_2,\omega_2,G_2,\mu_2)$$가 Hamiltonian 공간이면, 곱 $$G_1\times G_2$$의 곱 다양체 $$(M_1\times M_2,\,\pi_1^\ast\omega_1+\pi_2^\ast\omega_2)$$ 위의 작용은 Hamiltonian이며, 그 운동량 사상은

$$\mu(p_1,p_2)=\bigl(\mu_1(p_1),\mu_2(p_2)\bigr)\in\mathfrak{g}_1^\ast\oplus\mathfrak{g}_2^\ast=(\mathfrak{g}_1\oplus\mathfrak{g}_2)^\ast$$

이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$G_1\times G_2$$의 Lie algebra는 $$\mathfrak{g}_1\oplus\mathfrak{g}_2$$이고, $$(X_1,X_2)\in\mathfrak{g}_1\oplus\mathfrak{g}_2$$의 fundamental 벡터장은 곱 다양체 위에서 $$(X_1)_{M_1}\oplus(X_2)_{M_2}$$이다. 곱 symplectic form을 $$\omega=\pi_1^\ast\omega_1+\pi_2^\ast\omega_2$$라 하면, $$\iota_{(X_1)_{M_1}\oplus(X_2)_{M_2}}\omega=\pi_1^\ast(\iota_{(X_1)_{M_1}}\omega_1)+\pi_2^\ast(\iota_{(X_2)_{M_2}}\omega_2)$$이다. 한편 위에서 정의한 $$\mu$$에 대해 $$\mu^{(X_1,X_2)}=\mu_1^{X_1}\circ\pi_1+\mu_2^{X_2}\circ\pi_2$$이므로

$$d\mu^{(X_1,X_2)}=\pi_1^\ast(d\mu_1^{X_1})+\pi_2^\ast(d\mu_2^{X_2})=\pi_1^\ast(\iota_{(X_1)_{M_1}}\omega_1)+\pi_2^\ast(\iota_{(X_2)_{M_2}}\omega_2)$$

이 되어 조건 1이 성립한다. Equivariance는 각 성분에서 따로 성립하므로 곱에서도 성립한다.

</details>

## 예시

가장 기본적인 예시는 $$S^2$$ 위의 회전이다. 이 예시는 운동량 사상이 높이 함수라는 점에서 볼록성 정리의 원형이 된다.

<div class="example" markdown="1">

<ins id="ex7">**예시 7**</ins> 반지름 $$1$$의 구면 $$S^2\subseteq\mathbb{R}^3$$에 원기둥좌표 $$(\theta,h)$$를 주자. 여기서 $$h\in[-1,1]$$은 높이이고 $$\theta\in[0,2\pi)$$는 $$z$$축 둘레의 각이며, 점은 $$(\sqrt{1-h^2}\cos\theta,\sqrt{1-h^2}\sin\theta,h)$$이다. Area form은 이 좌표에서 $$\omega=d\theta\wedge dh$$로 적힌다. $$G=S^1$$이 $$z$$축 둘레의 회전 $$\theta\mapsto\theta+t$$로 작용하면 이는 $$\omega$$를 보존한다.

$$S^1$$의 Lie algebra $$\mathfrak{g}=\mathbb{R}$$의 표준 생성원 $$X=1$$의 fundamental 벡터장은 $$X_{S^2}=\partial_\theta$$이다. 그럼 $$\iota_{\partial_\theta}\omega=\iota_{\partial_\theta}(d\theta\wedge dh)=dh$$이므로, $$\mathfrak{g}^\ast\cong\mathbb{R}$$로 식별하여

$$\mu(\theta,h)=h$$

로 두면 $$d\mu^X=dh=\iota_{X_{S^2}}\omega$$가 성립한다. $$S^1$$이 abelian이므로 coadjoint 작용은 자명하고 equivariance는 자동이다. 따라서 운동량 사상은 곧 *높이 함수*이며, 그 상 $$\mu(S^2)=[-1,1]$$은 두 고정점 $$h=\pm1$$ (북극과 남극)의 상 $$\{-1,1\}$$의 볼록포이다.

</div>

다음 예시는 $$\mathbb{C}^n$$ 위의 표준 torus 작용으로, toric 기하의 출발점이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$\mathbb{C}^n$$에 좌표 $$z_j=x_j+iy_j$$를 주고 symplectic form

$$\omega=\sum_{j=1}^n dx_j\wedge dy_j=\frac{i}{2}\sum_{j=1}^n dz_j\wedge d\bar{z}_j$$

을 주자. $$T^n=(S^1)^n$$이 성분별 회전

$$(t_1,\ldots,t_n)\cdot(z_1,\ldots,z_n)=(e^{2\pi it_1}z_1,\ldots,e^{2\pi it_n}z_n)$$

으로 작용하면 이는 각 $$\lvert z_j\rvert$$를 보존하므로 $$\omega$$를 보존한다. $$\mathfrak{t}=\mathbb{R}^n$$의 $$j$$번째 표준 생성원 $$X=e_j$$의 fundamental 벡터장은 $$2\pi(x_j\partial_{y_j}-y_j\partial_{x_j})$$이고, $$\iota_{X_{\mathbb{C}^n}}\omega=-2\pi(x_j\,dx_j+y_j\,dy_j)=-\pi\,d(x_j^2+y_j^2)=-\pi\,d\lvert z_j\rvert^2$$이다. 따라서 $$\mathfrak{t}^\ast\cong\mathbb{R}^n$$으로 식별하여

$$\mu(z_1,\ldots,z_n)=-\pi\bigl(\lvert z_1\rvert^2,\ldots,\lvert z_n\rvert^2\bigr)$$

로 두면 조건 1이 성립한다. 즉 운동량 사상의 각 성분은 정확히 $$-\pi\lvert z_j\rvert^2$$, 즉 상수배를 무시하면 *반지름 제곱의 음수*이다. $$T^n$$이 abelian이므로 equivariance는 자동이다. 이 작용의 상은 음의 사분면 전체

$$\mu(\mathbb{C}^n)=\mathbb{R}_{\leq0}^n=\{(a_1,\ldots,a_n):a_j\leq0\}$$

이며, 이것이 affine toric 다양체 $$\mathbb{C}^n$$에 대응하는 운동량 다면체이다.

</div>

위 작용을 $$\mathbb{CP}^n$$으로 내리면 운동량 사상의 상이 유계인 단체가 된다. $$S^{2n+1}\subseteq\mathbb{C}^{n+1}$$ 위에서 $$\sum_j\lvert z_j\rvert^2=1$$이라는 제약을 가하고 대각 $$S^1$$로 나누면 $$\mathbb{CP}^n$$을 얻는데, 남은 $$T^n=T^{n+1}/S^1$$ 작용의 운동량 사상은 상수배 후 $$\bigl(\lvert z_1\rvert^2,\ldots,\lvert z_n\rvert^2\bigr)$$이 되어 그 상은 단체 $$\{a_j\geq0,\ \sum_j a_j\leq1\}$$이다. 이 절차가 reduction의 한 사례이며, 그 결과 얻어지는 단체가 $$\mathbb{CP}^n$$의 Fubini-Study 운동량 다면체이다. 일반적으로 compact toric 다양체는 그 운동량 다면체에 의해 완전히 결정되는데, 이것이 [볼록성 정리](#thm10) 뒤에서 언급할 Delzant 대응이다.

마지막으로 cotangent bundle 위의 작용은 운동량 사상이 고전적 운동량과 일치하는 가장 직접적인 예시이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> Manifold $$Q$$ 위에 Lie group $$G$$가 작용하면, 이를 cotangent bundle $$T^\ast Q$$로 들어 올린 *cotangent lift* 작용을 얻는다. $$g\in G$$의 $$Q$$ 위의 작용을 $$\phi_g:Q\rightarrow Q$$라 하면, $$T^\ast Q$$ 위의 작용은 $$(\phi_{g^{-1}})^\ast$$로 정의된다. 즉 $$g\cdot(q,p)=(\phi_g(q),\,(d\phi_{g^{-1}})^\ast_{\phi_g(q)}\,p)$$이다. 역원이 들어가는 것은 이것이 왼쪽 작용이 되게 하기 위함이며, 이 작용은 tautological $$1$$-form $$\lambda$$ ([§사교다양체, ⁋예시 2](/ko/math/symplectic_geometry/symplectic_manifold#ex2))를 보존하므로 $$\omega=-d\lambda$$ 또한 보존한다.

이 작용은 항상 Hamiltonian이며, 운동량 사상은

$$\langle\mu(q,p),X\rangle=\lambda_{(q,p)}(X_{T^\ast Q})=p\bigl(X_Q(q)\bigr)$$

로 주어진다. 여기서 $$X_Q$$는 $$Q$$ 위의 fundamental 벡터장이다. $$Q=\mathbb{R}^3$$이고 $$G=\mathrm{SO}(3)$$이 회전으로 작용하는 경우, 이 운동량 사상은 정확히 고전역학의 각운동량 $$\mu=q\times p$$를 준다.

</div>

Cotangent lift가 항상 Hamiltonian이라는 사실의 증명은 tautological $$1$$-form이 $$\iota_{X_{T^\ast Q}}\omega=d(\iota_{X_{T^\ast Q}}\lambda)$$를 만족하도록 자연스럽게 구성된다는 점에서 따라온다. 자세한 계산은 **[CdS]** 또는 **[MS]**에 있다.

## Atiyah-Guillemin-Sternberg 볼록성 정리

예시 7과 예시 8에서 우리는 torus 작용의 운동량 사상의 상이 볼록집합, 그것도 고정점들의 상의 볼록포로 나타나는 것을 보았다. 1982년 Atiyah와 Guillemin-Sternberg가 독립적으로 증명한 다음 정리는 이것이 일반적인 현상임을 말한다. 증명은 운동량 사상의 각 성분이 Morse-Bott 함수이며 그 임계 다양체가 짝수 지표를 가져 운동량 사상의 fiber가 연결됨을 이용하는 것으로, 상당한 분량을 요하므로 우리는 정확한 서술만 제시하고 증명은 문헌으로 미룬다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10 (Atiyah-Guillemin-Sternberg)**</ins> $$(M,\omega)$$가 compact connected symplectic manifold이고, torus $$T$$가 $$M$$ 위에 운동량 사상 $$\mu:M\rightarrow\mathfrak{t}^\ast$$을 갖는 Hamiltonian 작용을 한다고 하자. 그럼 $$\mu$$의 상 $$\mu(M)\subseteq\mathfrak{t}^\ast$$은 볼록집합이며, 구체적으로 작용의 고정점 집합 $$M^T$$의 상 $$\mu(M^T)$$의 볼록포이다. 특히 $$M^T$$가 유한 개의 연결성분을 가지므로 $$\mu(M)$$은 볼록 다면체이다.

</div>

이 정리의 상 $$\mu(M)$$을 작용의 *운동량 다면체<sub>moment polytope</sub>*라 부른다. 고정점은 운동량 사상의 임계점이며, $$\mu(M^T)$$의 점들이 운동량 다면체의 꼭짓점을 이룬다. 예시 7의 $$S^2$$에서 두 극점이 고정점이고 그 상 $$\{-1,1\}$$의 볼록포가 구간 $$[-1,1]$$인 것이 이 정리의 가장 단순한 사례이다.

볼록성 정리는 toric 기하와 직접 연결된다. $$2n$$차원 compact symplectic manifold에 $$n$$차원 torus, 즉 최대 차원의 torus가 효과적으로 Hamiltonian 작용을 할 때 이를 *symplectic toric manifold<sub>사교 토릭 다양체</sub>*라 부르며, 이 경우 운동량 다면체는 단순하고 정수적인 매우 특별한 다면체 (*Delzant 다면체*)가 된다. Delzant의 정리는 이러한 다면체와 symplectic toric manifold 사이에 일대일 대응이 성립함을, 즉 다면체가 다양체를 그 작용과 함께 완전히 결정함을 말한다. 이로써 symplectic 기하의 한 부류 전체가 순전히 조합론적인 볼록 다면체의 데이터로 번역된다.

<div class="remark" markdown="1">

<ins id="rmk11">**참고 11**</ins> 볼록성은 작용하는 군이 abelian, 즉 torus라는 점에 결정적으로 의존한다. 일반적인 nonabelian compact group $$G$$의 Hamiltonian 작용에서는 운동량 사상의 상 $$\mu(M)\subseteq\mathfrak{g}^\ast$$ 자체가 볼록일 필요는 없다. 대신 Kirwan은 $$\mu(M)$$과 양의 Weyl chamber $$\mathfrak{t}_+^\ast$$의 교집합 $$\mu(M)\cap\mathfrak{t}_+^\ast$$이 볼록 다면체임을 보였으며 (Kirwan 볼록성 정리), 이는 최대 torus의 작용으로 환원하여 위의 정리를 적용함으로써 증명된다. Coadjoint 작용이 자명하지 않은 nonabelian 경우에는 equivariance가 본질적인 역할을 한다.

</div>

---

**참고문헌**

**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[MS]** D. McDuff and D. Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017.  
**[Ati]** M. F. Atiyah, *Convexity and commuting Hamiltonians*, Bull. London Math. Soc. **14** (1982), 1–15.  
**[GS]** V. Guillemin and S. Sternberg, *Convexity properties of the moment mapping*, Invent. Math. **67** (1982), 491–513.  
**[Del]** T. Delzant, *Hamiltoniens périodiques et images convexes de l'application moment*, Bull. Soc. Math. France **116** (1988), 315–339.  
