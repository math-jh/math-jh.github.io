---
title: "Delzant 구성"
description: '콤팩트 connected symplectic toric manifold가 그 운동량 다면체에 의해 symplectomorphism을 무시하고 유일하게 결정되며, 모든 Delzant 다면체가 사교 축약을 통해 이렇게 실현됨을 보이는 Delzant 정리를 다룬다. 다면체의 facet 데이터로부터 부분 torus를 추출해 $$\mathbb{C}^d$$를 축약하는 명시적 구성을 서술하고, 같은 다면체가 결정하는 대수기하의 projective toric variety와의 대응을 정리한다.'
excerpt: "Delzant 다면체, Delzant 정리, 사교 축약에 의한 구성, symplectic toric manifold와 운동량 다면체의 일대일 대응"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/delzant_construction
sidebar: 
    nav: "toric_geometry-ko"

date: 2026-06-21
weight: 9

published: false
---

[\[사교기하학\] §운동량 사상, ⁋정리 10](/ko/math/symplectic_geometry/moment_map#thm10)의 Atiyah-Guillemin-Sternberg 볼록성 정리는 compact connected symplectic manifold 위의 torus 작용이 Hamiltonian일 때 그 운동량 사상의 상이 볼록 다면체가 됨을 말한다. 작용하는 torus의 차원이 다양체의 절반, 즉 가능한 가장 큰 차원에 이르는 극단적인 경우에 이 대응은 완벽해진다. 이때 다양체는 운동량 다면체에 의해 그 사교 구조와 작용까지 통째로 복원되며, 거꾸로 다면체가 만족해야 할 조합론적 조건도 정확히 결정된다. 이것이 1988년 Delzant가 증명한 정리이며, symplectic 기하의 한 부류 전체를 순전히 볼록 다면체의 데이터로 번역한다.

이 글에서 우리는 먼저 그 대응에 참여하는 다양체와 다면체를 각각 *symplectic toric manifold*와 *Delzant 다면체*로 정의하고, Delzant 정리를 서술한다. 정리의 핵심은 임의의 Delzant 다면체로부터 실제로 symplectic toric manifold를 만들어 내는 구성에 있다. 이 구성은 다면체의 $$d$$개 facet이 결정하는 짧은 완전열 $$0\to N\to\mathbb{T}^d\to\mathbb{T}^n\to0$$의 부분 torus $$N$$을 $$\mathbb{C}^d$$의 표준 Hamiltonian 작용에 제한하고, 이를 [\[사교기하학\] §사교 축약, ⁋정리 2](/ko/math/symplectic_geometry/symplectic_reduction#thm2)의 사교 축약으로 나누어 다양체를 얻는 것이다. 끝으로 같은 다면체가 [§토릭 다양체의 정의](/ko/math/toric_geometry/toric_varieties)에서 다룬 대수기하의 projective toric variety도 결정한다는 점을 정리하고, $$\mathbb{CP}^n$$과 $$\mathbb{CP}^1\times\mathbb{CP}^1$$, Hirzebruch 곡면을 예시로 든다.

## Symplectic toric manifold와 Delzant 다면체

운동량 다면체가 다양체를 완전히 결정하려면 torus의 차원이 충분히 커야 한다. $$2n$$차원 symplectic manifold 위에서 효과적으로 작용하는 torus의 차원은 많아야 $$n$$인데, 이 최대치에 도달하는 작용을 따로 이름 붙인다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> $$(M,\omega)$$를 차원 $$2n$$의 compact connected symplectic manifold라 하자. $$n$$차원 torus $$\mathbb{T}^n=(S^1)^n$$이 $$M$$ 위에 운동량 사상 $$\mu:M\rightarrow(\mathfrak{t}^n)^\ast$$을 갖는 *효과적<sub>effective</sub>* Hamiltonian 작용 ([\[사교기하학\] §운동량 사상, ⁋정의 2](/ko/math/symplectic_geometry/moment_map#def2))을 할 때, 네 쌍 $$(M,\omega,\mathbb{T}^n,\mu)$$을 *symplectic toric manifold<sub>사교 토릭 다양체</sub>*라 부른다. 여기서 작용이 효과적이라는 것은 모든 점을 고정하는 원소가 항등원뿐인 것, 즉 $$\mathbb{T}^n\rightarrow\Diff(M)$$이 단사인 것이다.

</div>

torus의 차원 $$n$$이 정확히 $$\tfrac12\dim M$$이라는 점이 결정적이다. 효과성은 이 작용이 더 작은 torus의 작용으로 환원되지 않음을, 즉 $$\mathbb{T}^n$$ 전체가 실질적으로 움직임을 보장한다. 두 symplectic toric manifold $$(M_1,\omega_1,\mathbb{T}^n,\mu_1)$$과 $$(M_2,\omega_2,\mathbb{T}^n,\mu_2)$$이 *동형*이라는 것은, $$\mathbb{T}^n$$-동변인 symplectomorphism $$\varphi:M_1\rightarrow M_2$$, 즉 $$\varphi^\ast\omega_2=\omega_1$$이고 작용과 가환인 미분동형이 존재하여 $$\mu_2\circ\varphi=\mu_1$$이 성립하는 것이다. 운동량 사상은 [\[사교기하학\] §운동량 사상, ⁋명제 4](/ko/math/symplectic_geometry/moment_map#prop4)에 의해 상수만큼의 자유도를 가지므로, 다면체를 평행이동시키는 자유도를 허용하여 $$\mu_2\circ\varphi=\mu_1+\text{(상수)}$$까지 같은 것으로 본다.

이제 다면체 쪽의 조건을 정한다. 볼록성 정리는 운동량 다면체가 볼록임만을 주지만, 작용이 효과적이고 차원이 최대일 때는 각 꼭짓점에서의 국소 모형이 다면체에 강한 정수론적 제약을 부과한다. 이 제약을 추출한 것이 다음 정의이다.

<div class="definition" markdown="1">

<ins id="def2">**정의 2**</ins> $$\mathbb{R}^n$$의 convex polytope $$\Delta$$가 *Delzant 다면체<sub>Delzant polytope</sub>*라는 것은 다음 세 조건을 만족하는 것이다.

1. (*simple*) 각 꼭짓점에서 정확히 $$n$$개의 facet이 만난다 (동치로, $$n$$개의 모서리가 만난다).
2. (*rational*) 각 꼭짓점에서 만나는 모서리들의 방향을 $$\mathbb{Z}^n$$의 원소인 primitive 벡터 $$v_1,\ldots,v_n\in\mathbb{Z}^n$$으로 택할 수 있다.
3. (*smooth*, 또는 *unimodular*) 각 꼭짓점에서 위 $$v_1,\ldots,v_n$$을 $$\mathbb{Z}^n$$의 $$\mathbb{Z}$$-basis가 되도록 택할 수 있다.

</div>

세 조건은 점점 강해지는 정수론적 매끄러움의 단계이다. 조건 1은 꼭짓점이 $$n$$개의 facet의 횡단 교차로만 생김을 요구하여, 가령 정팔면체의 꼭짓점처럼 $$n$$개보다 많은 facet이 모이는 경우를 배제한다. 조건 3은 꼭짓점에서 나가는 $$n$$개의 모서리 방향이 격자의 basis를 이룬다는 것으로, 동치로는 그 $$n$$개의 primitive 벡터를 열로 갖는 $$n\times n$$ 행렬의 행렬식이 $$\pm1$$이라는 조건이다. 이는 [§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11)에서 maximal cone의 generator들이 격자의 basis일 때 toric variety가 smooth였던 조건과 정확히 같은 형태이며, 실제로 두 매끄러움은 같은 대응의 양면이다.

<div class="remark" markdown="1">

<ins id="rmk3">**참고 3**</ins> 조건 3은 각 꼭짓점 $$p$$에서의 국소 모형을 표준화한다. 꼭짓점 $$p$$에서 만나는 $$n$$개의 facet의 안쪽을 향하는 primitive 법선 벡터 $$u_1,\ldots,u_n\in\mathbb{Z}^n$$이 격자의 basis를 이룰 때, 다면체는 $$p$$ 근방에서 표준 양사분면 $$\mathbb{R}_{\geq0}^n$$의 평행이동과 $$\GL(n,\mathbb{Z})$$ 변환으로 옮겨진다. 이 표준 모형이 아래 구성에서 각 꼭짓점에 대응하는 부분이 정확히 $$\mathbb{C}^n$$의 표준 toric chart가 되도록 보장하며, 그것이 결과 다양체의 smoothness의 근원이다. simple·rational만 만족하고 smooth가 깨지면 같은 구성이 매끄러운 다양체 대신 symplectic orbifold를 낳는다.

</div>

## Delzant 정리

이제 두 부류를 잇는 정리를 서술한다. 정리는 대응의 존재와 유일성을 한꺼번에 주장한다. 즉 모든 symplectic toric manifold는 Delzant 다면체를 운동량 다면체로 가지며, 다면체가 다양체를 동형을 무시하고 결정하고, 거꾸로 모든 Delzant 다면체가 이렇게 실현된다.

<div class="proposition" markdown="1">

<ins id="thm4">**정리 4 (Delzant)**</ins> 대응
$$(M,\omega,\mathbb{T}^n,\mu)\longmapsto\mu(M)$$
은 symplectic toric manifold의 동형류와 Delzant 다면체의 격자 합동류 (즉 평행이동과 $$\GL(n,\mathbb{Z})$$ 변환을 무시한 류) 사이의 전단사이다. 구체적으로 다음이 성립한다.

1. 임의의 symplectic toric manifold $$(M,\omega,\mathbb{T}^n,\mu)$$의 운동량 다면체 $$\Delta=\mu(M)$$은 Delzant 다면체이다.
2. 두 symplectic toric manifold가 동형일 필요충분조건은 그 운동량 다면체가 평행이동과 $$\GL(n,\mathbb{Z})$$ 변환으로 일치하는 것이다.
3. 임의의 Delzant 다면체 $$\Delta\subseteq\mathbb{R}^n$$에 대하여, $$\mu(M)=\Delta$$인 symplectic toric manifold $$(M_\Delta,\omega_\Delta,\mathbb{T}^n,\mu_\Delta)$$이 존재한다.

</div>

세 주장 가운데 가장 내용이 풍부한 것은 존재성 3이다. 1과 2는 각 꼭짓점에서의 국소 표준형, 즉 [참고 3](#rmk3)의 모형과 운동량 사상의 국소 정규형으로부터 따라오는 분석적 사실인 반면, 3은 주어진 조합론적 데이터로부터 실제로 다양체를 빚어내야 하기 때문이다. 우리는 이 구성을 다음 절에서 상세히 다루고, 그것이 곧 정리의 증명에서 가장 무거운 부분을 이룬다. 구성의 출발점은 다면체의 facet들이 주는 선형 데이터를 짧은 완전열로 묶는 것이다.

## Facet 데이터와 부분 torus

Delzant 다면체 $$\Delta\subseteq\mathbb{R}^n$$이 $$d$$개의 facet을 갖는다고 하자. 각 facet $$F_i$$는 안쪽을 향하는 primitive 법선 벡터 $$u_i\in\mathbb{Z}^n$$과 실수 $$\lambda_i\in\mathbb{R}$$로 결정되는 반공간 $$\{x\in\mathbb{R}^n:\langle x,u_i\rangle\geq-\lambda_i\}$$의 경계에 놓이며, 따라서 다면체는

$$\Delta=\{x\in\mathbb{R}^n:\langle x,u_i\rangle\geq-\lambda_i,\ i=1,\ldots,d\}$$

로 적힌다. 이 facet 법선들이 구성의 모든 선형 데이터를 담는다. 법선 벡터들을 모아 사상

$$\beta:\mathbb{R}^d\rightarrow\mathbb{R}^n,\qquad \beta(e_i)=u_i$$

을 정의하자. 여기서 $$e_1,\ldots,e_d$$은 $$\mathbb{R}^d$$의 표준 basis이다. Delzant 다면체의 simple·smooth 조건은 각 꼭짓점에서 $$n$$개의 $$u_i$$가 $$\mathbb{Z}^n$$의 basis를 이룸을 뜻하므로, 특히 $$\beta$$은 $$\mathbb{Z}^d$$을 $$\mathbb{Z}^n$$ 위로 보내는 전사이다. 다음 보조정리가 이 전사성을 정확히 만들고 부분 torus를 추출한다.

<div class="proposition" markdown="1">

<ins id="lem5">**보조정리 5**</ins> $$\Delta$$이 $$d$$개 facet을 갖는 Delzant 다면체이고 $$\beta:\mathbb{Z}^d\rightarrow\mathbb{Z}^n$$이 $$\beta(e_i)=u_i$$로 주어진다고 하자. 그럼 $$\beta$$은 전사이며, 그 핵 $$\mathfrak{n}:=\ker\beta\subseteq\mathbb{Z}^d$$은 rank $$d-n$$의 자유 부분군이고 $$\mathbb{Z}^d$$의 직합 인자(direct summand)이다. 따라서 $$\beta$$을 실수계수로 확장한 $$\beta:\mathbb{R}^d\rightarrow\mathbb{R}^n$$은 짧은 완전열

$$0\longrightarrow\mathfrak{n}_\mathbb{R}\longrightarrow\mathbb{R}^d\overset{\beta}{\longrightarrow}\mathbb{R}^n\longrightarrow0$$

을 주고, 이를 quotient torus로 지수화하면 짧은 완전열

$$0\longrightarrow N\longrightarrow\mathbb{T}^d\overset{\bar\beta}{\longrightarrow}\mathbb{T}^n\longrightarrow0$$

을 얻는다. 여기서 $$\mathbb{T}^k=\mathbb{R}^k/\mathbb{Z}^k$$이고 $$N=\mathfrak{n}_\mathbb{R}/\mathfrak{n}$$은 차원 $$d-n$$의 부분 torus이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$의 한 꼭짓점 $$p$$을 택하면, simple 조건에 의해 $$p$$에서 정확히 $$n$$개의 facet $$F_{i_1},\ldots,F_{i_n}$$이 만나고, smooth 조건에 의해 그 법선 $$u_{i_1},\ldots,u_{i_n}$$은 $$\mathbb{Z}^n$$의 $$\mathbb{Z}$$-basis를 이룬다. 이 $$n$$개의 벡터가 이미 $$\beta(\mathbb{Z}^d)$$ 안에서 $$\mathbb{Z}^n$$ 전체를 생성하므로 $$\beta$$은 전사이다.

전사인 $$\mathbb{Z}$$-가군 사상 $$\beta:\mathbb{Z}^d\rightarrow\mathbb{Z}^n$$에 대하여, $$\mathbb{Z}^n$$이 자유이므로 짧은 완전열 $$0\rightarrow\ker\beta\rightarrow\mathbb{Z}^d\rightarrow\mathbb{Z}^n\rightarrow0$$은 분할된다. 따라서 $$\mathbb{Z}^d\cong\ker\beta\oplus\mathbb{Z}^n$$이고 $$\mathfrak{n}=\ker\beta$$은 rank $$d-n$$의 자유 직합 인자이다. 분할성에 의해 $$\mathbb{R}^d=\mathfrak{n}_\mathbb{R}\oplus(\mathbb{Z}^n\text{의 들어올림})$$이므로 실수계수 완전열도 곧바로 따라온다.

마지막으로 functor $$V\mapsto V/(\text{격자})$$을 적용한다. $$\mathfrak{n}$$이 $$\mathbb{Z}^d$$의 직합 인자이므로 $$N=\mathfrak{n}_\mathbb{R}/\mathfrak{n}$$은 $$\mathbb{T}^d=\mathbb{R}^d/\mathbb{Z}^d$$의 닫힌 부분 torus이고, 몫 $$\mathbb{T}^d/N$$은 $$\mathbb{R}^n/\mathbb{Z}^n=\mathbb{T}^n$$과 동형이다. 분할성 덕분에 torsion이 생기지 않아 $$N$$은 연결된 차원 $$d-n$$의 torus이며, 지수화한 열 $$0\rightarrow N\rightarrow\mathbb{T}^d\rightarrow\mathbb{T}^n\rightarrow0$$이 완전하다.

</details>

이 완전열이 구성의 척추이다. 큰 torus $$\mathbb{T}^d$$은 곧 $$\mathbb{C}^d$$ 위에 표준적으로 작용하고, 그 안의 부분 torus $$N$$이 우리가 나눌 대칭이며, 몫 $$\mathbb{T}^n$$이 축약 후에도 살아남아 결과 다양체에 작용하는 토러스가 된다. $$N$$이 $$\mathbb{Z}^d$$의 직합 인자라는 점은 단순한 부수 사실이 아니라, $$N$$이 $$\mathbb{T}^d$$의 닫힌 부분군으로서 매끄럽게 작용하고 몫이 다시 torus가 되도록 보장하는 핵심이다. 상수 $$\lambda_i$$들은 아직 쓰이지 않았는데, 이들은 다음 절에서 축약을 취하는 운동량 사상의 값을 정하는 데 들어간다.

## 사교 축약에 의한 구성

이제 [\[사교기하학\] §운동량 사상, ⁋예시 8](/ko/math/symplectic_geometry/moment_map#ex8)의 $$\mathbb{C}^d$$ 위 표준 Hamiltonian torus 작용에서 출발한다. $$\mathbb{C}^d$$에 좌표 $$z_k=x_k+iy_k$$와 사교형식 $$\omega_0=\sum_{k=1}^d dx_k\wedge dy_k$$을 주고, $$\mathbb{T}^d$$이 성분별 회전

$$(t_1,\ldots,t_d)\cdot(z_1,\ldots,z_d)=(e^{2\pi it_1}z_1,\ldots,e^{2\pi it_d}z_d)$$

으로 작용한다고 하자. 이 작용의 운동량 사상은 부호 관례를 [정리 4](#thm4)의 구성에 맞도록 택하여

$$\phi:\mathbb{C}^d\rightarrow(\mathfrak{t}^d)^\ast\cong\mathbb{R}^d,\qquad \phi(z)=\pi\bigl(\lvert z_1\rvert^2,\ldots,\lvert z_d\rvert^2\bigr)$$

으로 둔다. 이는 예시 8의 운동량 사상의 부호를 뒤집고 상수배만큼 조정한 것으로, [\[사교기하학\] §운동량 사상, ⁋명제 4](/ko/math/symplectic_geometry/moment_map#prop4)의 자유도 안에 있다.

부분 torus $$N\subseteq\mathbb{T}^d$$의 작용에 대한 운동량 사상은 $$\phi$$을 $$N$$의 Lie algebra로 사영한 것이다. [보조정리 5](#lem5)의 완전열을 Lie algebra 수준에서 쌍대화하면, 포함 $$\iota:\mathfrak{n}\hookrightarrow\mathbb{R}^d$$의 쌍대 $$\iota^\ast:(\mathbb{R}^d)^\ast\rightarrow\mathfrak{n}^\ast$$을 합성하여 $$N$$-작용의 운동량 사상

$$\phi_N:=\iota^\ast\circ\phi:\mathbb{C}^d\rightarrow\mathfrak{n}^\ast$$

을 얻는다. 우리는 적절한 값에서 이 사상의 영점집합을 잘라 $$N$$으로 나눌 것이다. 그 값을 정하는 것이 다면체의 상수 $$\lambda=(\lambda_1,\ldots,\lambda_d)$$이다.

<div class="proposition" markdown="1">

<ins id="thm6">**정리 6 (Delzant 구성)**</ins> $$\Delta=\{x\in\mathbb{R}^n:\langle x,u_i\rangle\geq-\lambda_i\}$$을 $$d$$개 facet을 갖는 Delzant 다면체라 하고, [보조정리 5](#lem5)의 완전열 $$0\rightarrow N\rightarrow\mathbb{T}^d\rightarrow\mathbb{T}^n\rightarrow0$$과 위의 $$\phi_N=\iota^\ast\circ\phi$$을 택하자. $$\lambda\in\mathbb{R}^d$$의 상 $$\iota^\ast(\pi\lambda)\in\mathfrak{n}^\ast$$을 $$c$$라 두면, $$c$$은 $$\phi_N$$의 regular value이고 $$N$$은 영점집합 $$\phi_N^{-1}(c)$$ 위에 자유롭고 proper하게 작용한다. 따라서 사교 축약 ([\[사교기하학\] §사교 축약, ⁋정리 2](/ko/math/symplectic_geometry/symplectic_reduction#thm2))

$$M_\Delta:=\phi_N^{-1}(c)/N=\mathbb{C}^d /\!\!/_{\!c}\, N$$

은 차원 $$2n$$의 compact connected symplectic manifold이고, 그 위에는 몫 $$\mathbb{T}^n=\mathbb{T}^d/N$$의 효과적 Hamiltonian 작용이 잔여 작용으로 내려와 $$(M_\Delta,\omega_\Delta,\mathbb{T}^n,\mu_\Delta)$$을 symplectic toric manifold로 만든다. 그 운동량 다면체는 정확히 $$\mu_\Delta(M_\Delta)=\Delta$$이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

먼저 $$c$$이 regular value이고 작용이 자유로움을 본다. 점 $$z\in\mathbb{C}^d$$에서 좌표가 영이 되는 첨자의 집합을 $$I(z)=\{k:z_k=0\}$$이라 하자. $$\mathbb{T}^d$$의 점 $$z$$에서의 stabilizer는 정확히 $$I(z)$$가 지표하는 좌표 부분 torus $$\mathbb{T}^{I(z)}=\{t:t_k=0\text{ for }k\notin I(z)\}$$이다. 따라서 $$N$$이 $$z$$에서 자유롭게 작용할 필요충분조건은 $$N\cap\mathbb{T}^{I(z)}=\{1\}$$, 즉 Lie algebra 수준에서 $$\mathfrak{n}\cap\mathbb{R}^{I(z)}=0$$이다.

이제 $$\phi_N(z)=c$$인 점, 즉 $$\iota^\ast\bigl(\pi(\lvert z_1\rvert^2,\ldots,\lvert z_d\rvert^2)-\pi\lambda\bigr)=0$$인 점을 보자. 이 조건은 벡터 $$\pi(\lvert z_k\rvert^2)_k-\pi\lambda$$가 $$\iota^\ast$$의 핵, 곧 $$\mathfrak{n}^\perp=\im\beta^\ast=\{(\langle x,u_k\rangle)_k:x\in\mathbb{R}^n\}$$에 속함을 뜻한다. 따라서 어떤 $$x\in\mathbb{R}^n$$이 존재하여 모든 $$k$$에 대해

$$\pi\lvert z_k\rvert^2-\pi\lambda_k=\langle x,u_k\rangle,\qquad\text{즉}\qquad \lvert z_k\rvert^2=\langle x,u_k\rangle+\lambda_k\geq0$$

이 성립한다. 마지막 부등식은 정확히 $$x\in\Delta$$임을 말한다. 이 $$x=\mu_\Delta(z)$$이 곧 잔여 운동량 사상의 값이 되며, 따라서 $$\phi_N^{-1}(c)$$의 점은 다면체의 점 $$x\in\Delta$$로 사영된다. $$z_k=0$$인 첨자는 정확히 $$x$$이 facet $$F_k$$ 위에 놓이는, 즉 $$\langle x,u_k\rangle+\lambda_k=0$$인 첨자이므로 $$I(z)=\{k:x\in F_k\}$$이다.

$$x$$이 $$\Delta$$의 점일 때 그것이 놓이는 facet들의 집합 $$I(z)=\{k:x\in F_k\}$$을 보면, simple 조건에 의해 그 개수는 많아야 $$n$$이고 해당 법선 $$\{u_k:k\in I(z)\}$$은 일차독립이다. smooth 조건에 의해 이들은 $$\mathbb{Z}^n$$의 basis의 일부로 확장되므로, $$\beta$$을 $$\mathbb{R}^{I(z)}$$로 제한한 사상은 단사이다. 그런데 $$\mathfrak{n}=\ker\beta$$이므로 $$\mathfrak{n}\cap\mathbb{R}^{I(z)}=\ker(\beta\rvert_{\mathbb{R}^{I(z)}})=0$$이고, 따라서 위 판정에 의해 $$N$$은 $$\phi_N^{-1}(c)$$의 모든 점에서 자유롭게 작용한다. 자유로운 작용은 $$N$$이 compact이므로 proper하며, [\[사교기하학\] §사교 축약, ⁋보조정리 1](/ko/math/symplectic_geometry/symplectic_reduction#lem1)에 의해 stabilizer의 Lie algebra가 영이라는 것은 $$c$$이 $$\phi_N$$의 regular value임과 동치이다.

이제 [\[사교기하학\] §사교 축약, ⁋정리 2](/ko/math/symplectic_geometry/symplectic_reduction#thm2)의 모든 가정이 충족되었다. $$N$$은 compact torus이고 $$c$$은 regular value이며 작용은 자유롭고 proper하므로, 축약공간 $$M_\Delta=\phi_N^{-1}(c)/N$$은 매끄러운 다양체이고 유일한 사교형식 $$\omega_\Delta$$을 가지며 그 차원은

$$\dim M_\Delta=\dim\mathbb{C}^d-2\dim N=2d-2(d-n)=2n$$

이다. $$\Delta$$이 compact이고 위에서 $$\phi_N^{-1}(c)$$이 $$\Delta$$ 위로 사영되며 각 fiber가 좌표들의 위상 $$\lvert z_k\rvert$$이 고정된 torus의 부분집합이라 유계이고 닫혀 있으므로 $$\phi_N^{-1}(c)$$은 compact이고, 따라서 그 몫 $$M_\Delta$$도 compact이다. $$\mathbb{C}^d$$과 $$N$$, $$\Delta$$이 연결이므로 $$M_\Delta$$도 연결이다.

잔여 작용은 다음과 같이 내려온다. $$\mathbb{T}^d$$이 $$\mathbb{C}^d$$ 위에 작용하고 그 부분군 $$N$$의 작용으로 나누었으므로, 몫군 $$\mathbb{T}^n=\mathbb{T}^d/N$$이 $$M_\Delta$$ 위에 작용한다. 이 작용은 $$\omega_\Delta$$을 보존하며 그 운동량 사상은 $$\phi$$이 $$\phi_N^{-1}(c)$$ 위에서 유도하는 사상이 $$\mathbb{T}^n$$ 방향으로 내려온 것, 즉 위에서 정의한 $$\mu_\Delta(z)=x$$이다. 작용의 효과성은 다음에서 나온다. $$\mathbb{T}^n$$의 한 원소가 $$M_\Delta$$의 모든 점을 고정하면, 그것을 $$\mathbb{T}^d$$로 들어 올린 작용은 $$\phi_N^{-1}(c)$$을 $$N$$-orbit 안에서 보존하는데, 내부점 $$x\in\Delta^\circ$$ 위의 fiber에서는 $$I(z)=\varnothing$$이라 $$\mathbb{T}^d$$ 전체가 자유롭게 작용하므로 그 원소는 $$N$$에 속해야 하고, 따라서 $$\mathbb{T}^n$$에서는 항등원이다.

끝으로 운동량 다면체가 $$\Delta$$임은 위 사영에서 직접 읽힌다. $$\mu_\Delta(z)=x$$이 가능한 값의 집합은 정확히 $$\{x\in\mathbb{R}^n:\langle x,u_k\rangle+\lambda_k\geq0\text{ for all }k\}=\Delta$$이므로 $$\mu_\Delta(M_\Delta)=\Delta$$이다.

</details>

이 구성은 Delzant 정리의 존재성 부분, 즉 [정리 4](#thm4)의 3을 증명한다. 상수 $$\lambda_i$$들이 비로소 여기서 쓰였는데, 이들은 축약을 취하는 운동량 값 $$c=\iota^\ast(\pi\lambda)$$을 정하여 다면체의 facet들이 놓이는 위치, 곧 다면체의 크기와 모양을 결정한다. 법선 $$u_i$$들이 작용하는 부분 torus $$N$$을 통해 다양체의 *위상*과 작용을 빚는다면, 상수 $$\lambda_i$$들은 그 위에 얹히는 사교형식의 *부피*를 조절하는 셈이다. 두 다면체가 평행이동으로만 다르면 $$u_i$$이 같고 $$\lambda_i$$만 일제히 바뀌는데, 이는 운동량 사상에 상수를 더하는 자유도에 흡수되어 같은 symplectic toric manifold를 준다. 이것이 [정리 4](#thm4)의 유일성 2에서 평행이동을 합동으로 허용하는 이유이다.

증명 안에서 각 점 $$z$$의 좌표 소멸 패턴 $$I(z)$$이 그 상 $$x$$이 놓이는 facet들과 정확히 대응한 것은 우연이 아니다. 다면체의 면 구조가 그대로 축약공간의 torus orbit 구조로 번역되며, 꼭짓점(가장 많은 facet이 만나는 곳)은 $$\mathbb{T}^n$$-작용의 고정점에, facet의 상대 내부는 여차원 $$1$$의 orbit에 대응한다. 이 대응은 [§토릭 다양체의 정의, ⁋명제 5](/ko/math/toric_geometry/toric_varieties#prop5) 직후에서 본 cone과 orbit의 대응의 사교기하학적 짝이다.

## 대수기하의 toric variety와의 대응

같은 다면체 $$\Delta$$은 [§토릭 다양체의 정의](/ko/math/toric_geometry/toric_varieties)와 [§토러스 인자와 선다발](/ko/math/toric_geometry/toric_divisors)에서 다룬 대수기하의 toric variety도 결정한다. 그쪽에서는 $$\Delta$$의 *normal fan* ([§토릭 다양체의 정의, ⁋정의 6](/ko/math/toric_geometry/toric_varieties#def6)) $$\Sigma_\Delta$$을 만들고, 이로부터 projective toric variety $$X_\Sigma$$을 얻는다 ([§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)). 두 구성이 같은 입력에서 출발하므로, 한 다면체가 사교 쪽의 $$M_\Delta$$과 대수 쪽의 $$X_{\Sigma_\Delta}$$을 동시에 준다.

<div class="proposition" markdown="1">

<ins id="prop7">**명제 7**</ins> $$\Delta\subseteq\mathbb{R}^n$$을 Delzant 다면체라 하자. [정리 6](#thm6)의 사교 축약으로 얻은 symplectic toric manifold $$M_\Delta$$은, $$\Delta$$의 normal fan $$\Sigma_\Delta$$이 정의하는 smooth projective toric variety $$X_{\Sigma_\Delta}$$과 미분동형이며, 그 미분동형은 두 다양체 위의 $$\mathbb{T}^n$$-작용을 옮긴다. 나아가 $$M_\Delta$$ 위의 사교형식 $$\omega_\Delta$$은 $$\Delta$$이 결정하는 ample line bundle ([§토러스 인자와 선다발, ⁋명제 9](/ko/math/toric_geometry/toric_divisors#prop9))의 Chern 형식을 대표하는 Kähler 형식과 cohomology류가 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\Delta$$의 simple 조건은 $$\Sigma_\Delta$$의 모든 maximal cone이 simplicial임을, smooth 조건은 그 generator들이 $$\mathbb{Z}^n$$의 basis를 이룸을 준다. 따라서 [§토릭 다양체의 정의, ⁋명제 11](/ko/math/toric_geometry/toric_varieties#prop11)에 의해 $$X_{\Sigma_\Delta}$$은 smooth이고, $$\Delta$$이 full-dimensional lattice polytope의 normal fan이므로 [§토릭 다양체의 정의, ⁋명제 8](/ko/math/toric_geometry/toric_varieties#prop8)에 의해 projective이다.

미분동형은 양쪽 모두의 stratification이 $$\Delta$$의 면 격자(face lattice)와 같은 조합론으로 색인된다는 데에서 나온다. [정리 6](#thm6)의 증명에서 본 대로 $$M_\Delta$$의 점은 좌표 소멸 패턴 $$I(z)=\{k:x\in F_k\}$$으로 층화되며, 다면체의 면 $$F$$마다 그 상대 내부 위에 놓이는 점들이 한 $$\mathbb{T}^n$$-orbit을 이룬다. 한편 $$X_{\Sigma_\Delta}$$의 orbit은 [§토릭 다양체의 정의, ⁋명제 5](/ko/math/toric_geometry/toric_varieties#prop5)에 의해 $$\Sigma_\Delta$$의 cone, 곧 $$\Delta$$의 면으로 색인된다. 두 층화가 같은 색인 위에서 국소적으로 표준 모형 (꼭짓점 근방에서 $$\mathbb{C}^n$$의 표준 toric chart)으로 일치하므로, 이를 붙여 $$\mathbb{T}^n$$-동변 미분동형 $$M_\Delta\cong X_{\Sigma_\Delta}$$을 얻는다.

마지막 주장은 사교 축약이 주는 형식과 toric divisor가 주는 형식이 같은 부류임을 말한다. $$\Delta$$의 facet 데이터 $$\langle x,u_k\rangle\geq-\lambda_k$$은 [§토러스 인자와 선다발, ⁋명제 9](/ko/math/toric_geometry/toric_divisors#prop9)의 strictly convex piecewise linear 함수, 곧 ample divisor $$D=\sum_k\lambda_k D_{\rho_k}$$을 정의하며, 그 polytope $$\Delta_D$$이 정확히 $$\Delta$$이다. 축약으로 얻은 $$\omega_\Delta$$의 운동량 다면체가 $$\Delta$$이라는 [정리 6](#thm6)의 결론은, Atiyah-Guillemin-Sternberg 그림에서 $$[\omega_\Delta]$$이 이 ample 부류와 같은 $$\mathbb{T}^n$$-equivariant cohomology류로 표현됨과 동치이다. 따라서 $$\omega_\Delta$$은 $$\mathcal{O}(D)$$의 Chern 형식을 대표하는 Kähler 형식과 같은 부류이다.

</details>

이 명제는 사교기하와 대수기하의 두 toric 세계가 Delzant 다면체라는 하나의 조합론적 데이터 위에서 만남을 보여 준다. 대수 쪽은 다면체로부터 normal fan을 거쳐 복소다양체를 짓고, 사교 쪽은 같은 다면체의 facet으로부터 부분 torus를 거쳐 사교다양체를 짓는다. 둘은 같은 매끄러운 다양체이며, 다면체의 크기를 담은 상수 $$\lambda_i$$들이 한쪽에서는 ample line bundle의 선택으로, 다른 쪽에서는 사교형식의 부피로 나타난다. 다면체가 lattice polytope이라는 조건(상수 $$\lambda_i$$가 정수가 되도록 함)은 대수 쪽에서 line bundle이 실제로 존재하기 위한 정수성 조건이며, 사교 쪽에서는 형식이 정수 cohomology류를 갖는 prequantization 조건에 해당한다.

## 예시

가장 작은 예시부터 시작한다. 표준 단체가 $$\mathbb{CP}^n$$을 주는 것은 Delzant 구성의 원형이다.

<div class="example" markdown="1">

<ins id="ex8">**예시 8**</ins> $$\mathbb{R}^n$$의 표준 단체 ([§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10))

$$\Delta=\{x\in\mathbb{R}^n:x_i\geq0\ (i=1,\ldots,n),\ x_1+\cdots+x_n\leq1\}$$

을 생각하자. 이는 $$d=n+1$$개의 facet을 가지며, 안쪽 법선은 $$u_i=e_i$$ ($$i=1,\ldots,n$$)와 $$u_{n+1}=-e_1-\cdots-e_n$$이고 상수는 $$\lambda_i=0$$, $$\lambda_{n+1}=1$$이다. 각 꼭짓점에서 만나는 $$n$$개의 법선이 $$\mathbb{Z}^n$$의 basis를 이루므로 $$\Delta$$은 Delzant 다면체이다.

$$\beta:\mathbb{Z}^{n+1}\rightarrow\mathbb{Z}^n$$은 $$\beta(e_i)=e_i$$ ($$i\leq n$$), $$\beta(e_{n+1})=-e_1-\cdots-e_n$$이므로 그 핵은 $$\mathfrak{n}=\mathbb{Z}\cdot(1,1,\ldots,1)$$이고, 부분 torus $$N\subseteq\mathbb{T}^{n+1}$$은 대각 원 $$S^1$$이다. 따라서 [정리 6](#thm6)의 구성은 $$\mathbb{C}^{n+1}$$을 대각 $$S^1$$로 축약하는 것, 곧

$$M_\Delta=\mathbb{C}^{n+1}/\!\!/_{\!c}\,S^1=\mathbb{CP}^n$$

이며, 이는 정확히 [\[사교기하학\] §사교 축약, ⁋예시 6](/ko/math/symplectic_geometry/symplectic_reduction#ex6)에서 $$S^{2n+1}/S^1=\mathbb{CP}^n$$으로 계산한 그 축약이다. 잔여 작용 $$\mathbb{T}^n=\mathbb{T}^{n+1}/S^1$$의 운동량 다면체는 $$\Delta$$, 즉 표준 단체이고, 사교형식은 Fubini-Study 형식이다. 대수 쪽에서 같은 단체의 normal fan은 [§토릭 다양체의 정의, ⁋예시 10](/ko/math/toric_geometry/toric_varieties#ex10)의 $$\mathbb{P}^n$$의 fan이므로 [명제 7](#prop7)이 확인된다.

</div>

곱은 다면체의 곱에 대응한다. 정사각형이 $$\mathbb{CP}^1\times\mathbb{CP}^1$$을 주는 다음 예시가 그 가장 단순한 사례이다.

<div class="example" markdown="1">

<ins id="ex9">**예시 9**</ins> $$\mathbb{R}^2$$의 단위 정사각형

$$\Delta=[0,1]\times[0,1]=\{x\in\mathbb{R}^2:x_1\geq0,\ x_2\geq0,\ x_1\leq1,\ x_2\leq1\}$$

을 생각하자. 네 facet의 안쪽 법선은 $$u_1=e_1$$, $$u_2=e_2$$, $$u_3=-e_1$$, $$u_4=-e_2$$이고 상수는 $$\lambda_1=\lambda_2=0$$, $$\lambda_3=\lambda_4=1$$이다. 각 꼭짓점에서 만나는 두 법선, 가령 $$(0,0)$$에서 $$\{e_1,e_2\}$$과 $$(1,1)$$에서 $$\{-e_1,-e_2\}$$은 모두 $$\mathbb{Z}^2$$의 basis이므로 정사각형은 Delzant 다면체이다.

$$\beta:\mathbb{Z}^4\rightarrow\mathbb{Z}^2$$은 $$\beta(e_1)=e_1$$, $$\beta(e_2)=e_2$$, $$\beta(e_3)=-e_1$$, $$\beta(e_4)=-e_2$$이므로 그 핵은 $$\mathfrak{n}=\mathbb{Z}\cdot(1,0,1,0)\oplus\mathbb{Z}\cdot(0,1,0,1)$$이고, 부분 torus $$N\subseteq\mathbb{T}^4$$은 두 좌표쌍 $$(z_1,z_3)$$과 $$(z_2,z_4)$$을 각각 대각으로 회전시키는 $$S^1\times S^1$$이다. 축약은 두 인자에서 따로 일어나 각각 $$\mathbb{C}^2/\!\!/S^1=\mathbb{CP}^1$$을 주므로

$$M_\Delta=(\mathbb{C}^2/\!\!/_{\!c_1}S^1)\times(\mathbb{C}^2/\!\!/_{\!c_2}S^1)=\mathbb{CP}^1\times\mathbb{CP}^1$$

이다. 이는 정사각형이 두 구간의 곱 $$[0,1]\times[0,1]$$이고 구간 $$[0,1]$$이 [\[사교기하학\] §운동량 사상, ⁋예시 7](/ko/math/symplectic_geometry/moment_map#ex7)에서 본 $$\mathbb{CP}^1=S^2$$의 운동량 다면체라는 사실의 반영이다. 더 일반적으로 두 Delzant 다면체의 곱은 두 symplectic toric manifold의 곱에 대응하며, 직사각형 $$[0,a]\times[0,b]$$은 두 인자의 사교형식이 각각 $$a$$, $$b$$로 재조정된 $$\mathbb{CP}^1\times\mathbb{CP}^1$$을 준다.

</div>

마지막 예시는 같은 정사각형을 비틀어 얻는 Hirzebruch 곡면으로, 다면체의 모양이 다양체의 위상을 어떻게 바꾸는지를 보여 준다.

<div class="example" markdown="1">

<ins id="ex10">**예시 10**</ins> 정수 $$a\geq0$$과 양의 실수 $$h$$에 대하여 $$\mathbb{R}^2$$의 사다리꼴

$$\Delta_a=\{x\in\mathbb{R}^2:x_1\geq0,\ x_2\geq0,\ x_1\leq1,\ x_2\leq h-a x_1\}$$

을 생각하자 (여기서 $$h>a$$로 두어 다면체가 비지 않게 한다). 네 facet의 안쪽 법선은 $$u_1=e_1$$, $$u_2=e_2$$, $$u_3=-e_1$$, $$u_4=(-a,-1)$$이고, 위쪽 모서리의 기울기가 $$-a$$이다. 각 꼭짓점에서 만나는 두 법선의 행렬식을 보면, 가령 $$(1,h-a)$$에서 $$\{-e_1,(-a,-1)\}$$의 행렬식은 $$\det\begin{pmatrix}-1&-a\\0&-1\end{pmatrix}=1$$이고 나머지 꼭짓점에서도 $$\pm1$$이므로 $$\Delta_a$$은 Delzant 다면체이다.

이 다면체가 정의하는 symplectic toric manifold $$M_{\Delta_a}$$은 *Hirzebruch 곡면<sub>Hirzebruch surface</sub>* $$\mathbb{F}_a=\mathbb{P}(\mathcal{O}_{\mathbb{P}^1}\oplus\mathcal{O}_{\mathbb{P}^1}(a))$$이다. $$a=0$$이면 $$\Delta_0$$은 직사각형이 되어 [예시 9](#ex9)의 $$\mathbb{F}_0=\mathbb{CP}^1\times\mathbb{CP}^1$$로 환원되고, $$a$$이 커질수록 사다리꼴이 기울어지며 위쪽 모서리의 법선 $$(-a,-1)$$이 비틀린다. $$\beta:\mathbb{Z}^4\rightarrow\mathbb{Z}^2$$은 네 법선 $$e_1,e_2,-e_1,(-a,-1)$$로 주어지고 그 핵은 $$\mathfrak{n}=\mathbb{Z}\cdot(1,0,1,0)\oplus\mathbb{Z}\cdot(0,1,-a,1)$$이며, 대응하는 부분 torus $$N\subseteq\mathbb{T}^4$$의 비대각 작용이 $$\mathbb{C}^4$$을 비틀어 축약함으로써 $$\mathbb{CP}^1$$ 위의 비자명한 곡면 다발을 낳는다. 대수 쪽에서 $$\Delta_a$$의 normal fan은 ray $$e_1,e_2,-e_1,(-a,-1)$$이 생성하는 fan으로, 정확히 $$\mathbb{F}_a$$의 표준 fan이며 [명제 7](#prop7)이 다시 확인된다.

</div>

세 예시는 Delzant 다면체의 조합론적 변형이 symplectic toric manifold의 위상적 변형으로 직접 번역됨을 보여 준다. 단체를 정사각형으로 바꾸면 $$\mathbb{CP}^2$$이 $$\mathbb{CP}^1\times\mathbb{CP}^1$$이 되고, 정사각형을 사다리꼴로 비틀면 Hirzebruch 곡면들의 족이 나온다. 다면체의 facet을 잘라내는 조작은 다양체의 blow-up에, 모서리의 기울기를 바꾸는 조작은 다발 구조의 비틀림에 대응한다. 이렇게 Delzant 정리는 사교다양체의 분류 문제 하나를 격자 다면체의 조합론으로 온전히 옮겨 놓는다.

---

**참고문헌**

**[Del]** T. Delzant, *Hamiltoniens périodiques et images convexes de l'application moment*, Bull. Soc. Math. France **116** (1988), 315–339.  
**[CdS-T]** A. Cannas da Silva, *Symplectic toric manifolds*, in *Symplectic Geometry of Integrable Hamiltonian Systems*, Advanced Courses in Mathematics CRM Barcelona, Birkhäuser, 2003, pp. 85–173.  
**[CdS]** A. Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008.  
**[Gui]** V. Guillemin, *Moment Maps and Combinatorial Invariants of Hamiltonian $$T^n$$-spaces*, Progress in Mathematics 122, Birkhäuser, 1994.  
**[CLS]** D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics, American Mathematical Society, 2011.  
