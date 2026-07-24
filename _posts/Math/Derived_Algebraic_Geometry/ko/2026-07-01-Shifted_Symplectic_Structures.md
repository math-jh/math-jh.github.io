---
title: "Shifted symplectic 구조"
description: "Derived stack 위의 여접 복합체로부터 p-형식과 닫힌 형식을 정의하고, 접복합체와 여접복합체의 동형을 주는 n-shifted symplectic 구조를 도입하여 derived critical locus의 (-1)-shifted 구조와 Lagrangian 교차를 다룬다."
excerpt: "p-forms on derived stacks, n-shifted symplectic structures, derived critical loci, and Lagrangians"

categories: [Math / Derived Algebraic Geometry]
permalink: /ko/math/derived_algebraic_geometry/shifted_symplectic_structures
sidebar: 
    nav: "derived_algebraic_geometry-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 4

published: false

---

고전 symplectic 기하는 smooth variety 위의 closed 비축퇴 $2$-형식을 재료로 삼는다. 그런데 대수기하에서 자연스럽게 나타나는 공간의 대부분은 매끄럽지도 않고, 심지어 scheme조차 아닌 moduli stack이다. Pantev, Toën, Vaquié, Vezzosi (이하 PTVV)는 이러한 대상에 symplectic 기하를 세우려면 두 가지를 동시에 확장해야 함을 발견하였다. 첫째로 tangent bundle과 cotangent bundle을 접복합체 $T_X$와 여접 복합체 $L_X$로 대체하고 ([§Derived scheme과 derived stack, ⁋정의 10](/ko/math/derived_algebraic_geometry/derived_schemes#def10)), 둘째로 형식이 사는 자리를 cohomological degree 방향으로 옮겨 *shift*를 허용하는 것이다. 그 결과가 *n-shifted symplectic 구조*이며, PTVV는 Calabi–Yau 위의 sheaf의 moduli, local system의 moduli, mapping stack 등 수많은 유도 moduli stack이 표준적인 shifted symplectic 구조를 지님을 보였다. 이 구조가 virtual fundamental class와 Donaldson–Thomas류 불변량을 조직하는 뼈대가 된다.

이 글에서 우리는 먼저 derived stack 위의 $p$-형식과 closed 형식의 공간을 여접 복합체의 exterior power로부터 정의한다. 여기서 결정적인 점은 "닫혀 있음"이 하나의 *성질*이 아니라 정합적 homotopy로 주어지는 *자료*라는 것이다. 이어서 접복합체와 여접 복합체를 동형으로 잇는 비축퇴 조건을 부과하여 $n$-shifted symplectic 구조를 정의하고, degree별 예시로 smooth symplectic variety($0$-shifted), 분류 stack $\mathbf{B}G$($2$-shifted)를 다룬다. 그다음 derived critical locus가 canonically $(-1)$-shifted symplectic임을 보이고, 이것이 $(-1)$-shifted 대상의 국소 모형임을 말하는 Darboux 정리를 서술한다. 마지막으로 Lagrangian morphism과 그 교차, 그리고 AKSZ mapping stack 구성을 통해 이 구조들이 어떻게 생산되는지를 본다. 이하에서 $k$는 characteristic $0$의 field이고, $X$는 별다른 언급이 없으면 $k$ 위에서 유한표현인 derived Artin stack이라 하여 그 여접 복합체 $L_X$가 perfect, 곧 dualizable이 되도록 한다. ([§Derived scheme과 derived stack, ⁋정의 8](/ko/math/derived_algebraic_geometry/derived_schemes#def8))

## Derived stack 위의 p-형식

고전적으로 smooth variety 위의 $p$-형식은 $\wedge^p\Omega_X$의 대역 절단이었다. Derived 세계에서 $\Omega_X$의 자리를 여접 복합체 $L_X$가 차지하므로, $p$-형식은 $L_X$의 $p$번째 exterior power의 절단이 되어야 한다. ([\[다중선형대수학\] §텐서대수, ⁋정의 10](/ko/math/multilinear_algebra/tensor_algebras#def10)) 그러나 $L_X$는 여러 degree에 걸친 복합체이므로, 절단은 $0$차 cohomology뿐 아니라 임의의 degree에서 취할 수 있다. 이 여분의 degree가 바로 형식의 *shift*이다.

::: 정의 1
Derived stack $X$와 정수 $p\geq0$, $n\in\mathbb{Z}$에 대하여, $X$ 위의 *degree $n$의 $p$-형식<sub>$p$-form of degree $n$</sub>*들의 *공간*을 $\QCoh(X)$에서의 mapping space

$$\mathcal{A}^p(X,n)=\operatorname{Map}_{\QCoh(X)}\bigl(\mathcal{O}_X,(\wedge^pL_X)[n]\bigr)$$

으로 정의한다. 이 공간의 한 점, 곧 $\mathcal{O}_X\rightarrow(\wedge^pL_X)[n]$의 homotopy 류 하나를 degree $n$의 $p$-형식이라 부르며, 이는 hypercohomology 류

$$\omega\in H^n\bigl(X,\wedge^pL_X\bigr)=\pi_0\mathcal{A}^p(X,n)$$

에 해당한다.
:::

여기서 $\wedge^pL_X$은 여접 복합체의 $p$번째 exterior power로, perfect 복합체의 exterior power이므로 다시 perfect이다. $X$이 smooth 고전적 variety이면 $L_X=\Omega_X$이 degree $0$에 집중된 국소자유 sheaf이므로 $\wedge^pL_X=\Omega_X^p$이 고전적 $p$-형식 다발이 되고, $\mathcal{A}^p(X,0)$의 $\pi_0$은 대역 $p$-형식들의 $k$-vector space $H^0(X,\Omega_X^p)$으로 되돌아온다. 반면 $X$이 stack이거나 유도 두께를 가지면 $L_X$이 음·양의 degree에 항을 가지므로, degree $n\neq0$의 형식이 자연스럽게 등장한다. 이제 우리에게 필요한 것은 이 형식들 가운데 "닫힌" 것을 가려내는 일이다.

## 닫힌 형식과 de Rham 복합체

고전적으로 형식 $\omega$이 닫혀 있다는 것은 de Rham 미분이 소멸한다는 성질 $d_{\dR}\omega=0$이었다. Derived 세계에서 등식 $d_{\dR}\omega=0$은 너무 거칠다. Cochain 수준에서 정확히 $0$이 되기를 요구하는 대신, 우리는 $d_{\dR}\omega$을 $0$으로 이어 주는 homotopy, 그리고 그 homotopy들 사이의 더 높은 homotopy까지 모두 자료로 기억해야 한다. 이를 담는 그릇이 de Rham 복합체이다. 각 affine 조각에서 여접 복합체 $L_{B/A}$을 이어붙여 $L_X$을 얻었듯 ([§Simplicial 가환환과 animation, ⁋정의 10](/ko/math/derived_algebraic_geometry/animated_rings#def10)), 그 exterior power들을 weight에 따라 쌓아 대역적 de Rham 복합체를 만든다.

::: 정의 2
Derived stack $X$의 *de Rham 복합체<sub>de Rham complex</sub>*는 weight로 매겨진 graded mixed complex

$$\dR(X)=\bigoplus_{p\geq0}(\wedge^pL_X)[-p]$$

으로, 각 $\wedge^pL_X$의 내부 미분 $d$과 함께, weight를 $1$ 올리는 *de Rham 미분* $\epsilon=d_{\dR}:\wedge^pL_X\rightarrow\wedge^{p+1}L_X$을 mixed 구조로 가진다. 이때 $X$ 위의 *degree $n$의 closed $p$-형식<sub>closed $p$-form of degree $n$</sub>*들의 공간 $\mathcal{A}^{p,\mathrm{cl}}(X,n)$을, 총복합체

$$\Bigl(\prod_{i\geq0}(\wedge^{p+i}L_X)[n-i],\quad d-d_{\dR}\Bigr)$$

에 딸린 mapping space로 정의한다. 구체적으로 그 한 점은 형식들의 열 $\omega=(\omega_0,\omega_1,\omega_2,\ldots)$으로서, 각 $\omega_i$이 degree $n-i$의 $(p+i)$-형식이고

$$d\omega_0=0,\qquad d_{\dR}\omega_i=d\omega_{i+1}\quad(i\geq0)$$

을 만족하는 것이다. $\omega_0$을 $\omega$의 *밑에 깔린 $p$-형식*이라 부르고, $\omega\mapsto\omega_0$은 *망각 morphism*

$$\mathcal{A}^{p,\mathrm{cl}}(X,n)\longrightarrow\mathcal{A}^p(X,n)$$

을 준다.
:::

이 정의의 핵심은 관계식 $d_{\dR}\omega_0=d\omega_1$이 읽히는 방식에 있다. 그것은 밑에 깔린 형식의 de Rham 미분 $d_{\dR}\omega_0$이 $0$과 *같다*는 성질이 아니라, $d_{\dR}\omega_0$을 $0$으로 축약하는 명시적 nullhomotopy $\omega_1$이 주어졌다는 *자료*이다. 나아가 $\omega_2,\omega_3,\ldots$은 이 nullhomotopy가 더 높은 weight에서도 정합적임을 보장하는 higher homotopy들이다. 따라서 closed $p$-형식은 밑에 깔린 형식 하나가 아니라, 그 형식을 닫는 무한한 정합 자료 전체를 나른다.

::: 참고 3
망각 morphism $\mathcal{A}^{p,\mathrm{cl}}(X,n)\rightarrow\mathcal{A}^p(X,n)$은 일반적으로 동치가 아니며, 단사조차 아니다. 그 homotopy fiber가 "주어진 형식 $\omega_0$을 닫는 방법들의 공간"이고, 이 공간은 비어 있을 수도, 여러 connected component를 가질 수도 있다. 이것이 고전적 상황과 결정적으로 갈라지는 지점이다. Smooth 고전적 variety 위에서는 $L_X=\Omega_X$이 degree $0$에 집중되어 higher homotopy가 소멸하므로, $\omega_0$을 닫는 방법의 공간은 $d_{\dR}\omega_0=0$일 때 (본질적으로 유일하게) 존재하고 그렇지 않으면 비어 있다. 곧 이 경우에 한하여 닫힘은 다시 성질로 환원되어 고전적 개념과 일치한다. 그러나 stack이나 유도 두께가 있으면 닫힘은 참으로 자료가 되며, 서로 다른 닫힘을 준 두 형식은 밑에 깔린 형식이 같더라도 closed 형식으로서는 다르다. 이 때문에 우리는 처음부터 형식이 아니라 형식의 *공간*을 다루고, symplectic 구조를 하나의 점이 아니라 자료를 갖춘 대상으로 취급한다.
:::

## n-shifted symplectic 구조

이제 symplectic 구조를 정의한다. 고전적 symplectic 형식의 본질은 비축퇴성, 곧 형식이 tangent space와 cotangent space를 동형으로 잇는다는 데 있었다. 이 선형대수적 조건을 먼저 분리해 두자.

::: 정의 4
$k$ 위의 유한차원 vector space $V$에 대하여, *alternating $2$-form<sub>교대 $2$-형식</sub>*이란 원소 $\omega\in\wedge^2V^\ast$을 뜻하며, 이는 $\omega(v,v)=0$을 만족하는 bilinear form과 같다. 그 *flat 사상*을

$$\omega^\flat:V\longrightarrow V^\ast,\qquad \omega^\flat(v)=\omega(v,-)$$

으로 둔다. $\omega$이 *nondegenerate<sub>비퇴화</sub>*하다는 것은 $\omega^\flat$이 동형인 것을 뜻하며, 이때 쌍 $(V,\omega)$을 *symplectic vector space*라 부른다.
:::

Alternating 조건은 characteristic $0$에서 반대칭 $\omega(v,w)=-\omega(w,v)$과 동치이고, nondegeneracy는 $\omega^\flat$이 동형이라는 것이므로 $\dim V$이 짝수임을 강제한다. 이 그림에서 우리가 shifted symplectic 기하로 옮겨 갈 때 바꾸는 것은 단 하나이다. Vector space $V$을 접복합체 $T_X$로, 그 쌍대 $V^\ast$을 여접 복합체 $L_X$로 대체하되, 동형을 요구하던 자리에서 shift $[n]$을 허용한 동치를 요구한다. 여기서 $T_X=L_X^\vee$은 $L_X$의 쌍대이며 ([§Derived scheme과 derived stack, ⁋정의 10](/ko/math/derived_algebraic_geometry/derived_schemes#def10)), $L_X$이 perfect이므로 이 쌍대는 잘 정의된다.

::: 정의 5
Derived stack $X$ 위의 *$n$-shifted symplectic 구조<sub>$n$-shifted symplectic structure</sub>*란, degree $n$의 closed $2$-형식 $\omega\in\mathcal{A}^{2,\mathrm{cl}}(X,n)$으로서, 그 밑에 깔린 $2$-형식 $\omega_0:\mathcal{O}_X\rightarrow(\wedge^2L_X)[n]$이 유도하는 morphism

$$\omega_0^\flat:T_X\longrightarrow L_X[n]$$

이 $\QCoh(X)$에서 동치인 것을 뜻한다. 이 마지막 조건을 $\omega$의 *nondegeneracy<sub>비퇴화성</sub>*라 부르고, $n$-shifted symplectic 구조를 갖춘 $X$을 $n$-shifted symplectic derived stack이라 한다.
:::

밑에 깔린 형식 $\omega_0$은 $\wedge^2T_X\rightarrow\mathcal{O}_X[n]$, 곧 접복합체 위의 반대칭 쌍선형 짝짓기를 주며, 이를 한 변수에 대하여 수반으로 옮긴 것이 $\omega_0^\flat:T_X\rightarrow L_X[n]$이다. 따라서 nondegeneracy는 [정의 4](#def4)의 flat 사상이 동형이라는 조건을 복합체 수준으로, 그리고 shift $[n]$을 허용하여 옮긴 것이다. 여기서 닫힘 자료 전체가 아니라 오직 $\omega_0$만이 nondegeneracy에 관여함에 유의한다. 곧 $n$-shifted symplectic 구조는 "비축퇴 형식"이라는 국소적 조건과 "닫힘"이라는 대역적 정합 자료를 함께 묶은 대상이다. Degree $n$을 바꾸면 서로 다른 기하가 나타나는데, 이를 낮은 degree부터 살펴본다.

::: 예시 6 ($0$-shifted: 고전적 symplectic variety)
$X$이 smooth 고전적 variety이면 $L_X=\Omega_X$, $T_X=\mathcal{T}_X$이 모두 degree $0$에 집중된 국소자유 sheaf이다. Degree $0$의 closed $2$-형식은 [참고 3](#rmk3)에 의하여 통상적 closed $2$-형식 $\omega\in H^0(X,\Omega_X^2)$, $d_{\dR}\omega=0$과 같고, nondegeneracy $\omega_0^\flat:\mathcal{T}_X\overset{\sim}{\rightarrow}\Omega_X$은 각 점에서 [정의 4](#def4)의 비축퇴성이다. 따라서 $0$-shifted symplectic derived stack 가운데 smooth 고전적 variety인 것은 정확히 통상적 symplectic variety이다. 예컨대 smooth affine variety $Y$의 cotangent bundle $T^\ast Y$은 canonical Liouville 형식 $\lambda$의 미분 $\omega=d\lambda$으로 $0$-shifted symplectic이며, 이것이 shifted 세계에서도 가장 기본적인 국소 모형이 된다.
:::

::: 예시 7 ($2$-shifted: 분류 stack $\mathbf{B}G$)
$G$을 $k$ 위의 reductive algebraic group, $\mathfrak{g}=\Lie(G)$을 그 Lie algebra라 하자. 분류 stack $\mathbf{B}G$은 geometric derived stack이고 ([§Derived scheme과 derived stack, ⁋예시 9](/ko/math/derived_algebraic_geometry/derived_schemes#ex9)), 그 atlas $u:\Spec k\rightarrow\mathbf{B}G$은 $G$-torsor로서 상대차원 $\dim G$의 smooth morphism이므로 상대 여접 복합체는 fiber $G$의 항등원 cotangent space가 degree $0$에 놓인 $L_{\Spec k/\mathbf{B}G}\simeq\mathfrak{g}^\ast$이다. 추이 삼각형 ([§Derived scheme과 derived stack, ⁋명제 11](/ko/math/derived_algebraic_geometry/derived_schemes#prop11)) $u^\ast L_{\mathbf{B}G}\rightarrow L_{\Spec k}\rightarrow L_{\Spec k/\mathbf{B}G}$에서 $L_{\Spec k}=0$이므로 $u^\ast L_{\mathbf{B}G}\simeq L_{\Spec k/\mathbf{B}G}[-1]=\mathfrak{g}^\ast[-1]$, 곧 여접 복합체는 $L_{\mathbf{B}G}=\mathfrak{g}^\ast[-1]$이고 그 쌍대인 접복합체는 $T_{\mathbf{B}G}=\mathfrak{g}[1]$이다. Odd degree 대상의 exterior power에 대한 Koszul 부호 규칙에 의하여

$$\wedge^2L_{\mathbf{B}G}=\wedge^2\bigl(\mathfrak{g}^\ast[-1]\bigr)\simeq\Sym^2(\mathfrak{g}^\ast)[-2]$$

이므로, degree $2$의 $2$-형식은

$$H^2\bigl(\mathbf{B}G,\wedge^2L_{\mathbf{B}G}\bigr)=H^0\bigl(\mathbf{B}G,\Sym^2\mathfrak{g}^\ast\bigr)=\bigl(\Sym^2\mathfrak{g}^\ast\bigr)^G$$

곧 $\mathfrak{g}$ 위의 $G$-불변 대칭 bilinear form과 같다. 이 가운데 nondegenerate한 것이 유도하는 morphism은 $T_{\mathbf{B}G}=\mathfrak{g}[1]\rightarrow L_{\mathbf{B}G}[2]=\mathfrak{g}^\ast[1]$, 곧 $\mathfrak{g}\cong\mathfrak{g}^\ast$을 주는 비축퇴 불변 형식이다. $G$이 semisimple이면 Killing 형식 $\kappa(x,y)=\operatorname{tr}(\ad x\circ\ad y)$이 정확히 이러한 형식을 주므로, $\mathbf{B}G$은 canonically $2$-shifted symplectic이다. 실제로 reductive $G$에 대하여 $\mathbf{B}G$ 위의 $2$-shifted symplectic 구조는 $\mathfrak{g}$ 위의 비축퇴 $G$-불변 형식과 일대일 대응한다. Torus $T=\mathbb{G}_m^r$의 경우 $\mathfrak{g}=\mathfrak{t}$이 abelian이라 Killing 형식이 $0$이지만, adjoint 작용이 자명하여 $\mathfrak{t}$ 위의 임의의 비축퇴 대칭형식이 불변이므로, cocharacter lattice 위의 비축퇴 짝짓기를 하나 골라 $\mathbf{B}T$을 $2$-shifted symplectic으로 만들 수 있다. 특히 $\mathbf{B}\mathbb{G}_m$은 $\mathfrak{t}=k$ 위의 표준 짝짓기로 $2$-shifted symplectic이다.
:::

$0$-shifted 구조가 고전적 symplectic 기하를 그대로 담고 $2$-shifted 구조가 stack 방향의 대칭에서 나온다면, 우리에게 정작 흥미로운 것은 음의 shift이다. 음의 shift는 유도 두께에서, 특히 방정식이 만드는 장애에서 나타나며, 그 원형이 derived critical locus이다.

## Derived critical locus의 (-1)-shifted 구조

Smooth variety $U$ 위의 함수 $f:U\rightarrow\mathbb{A}^1$에 대하여, 그 미분 $df$은 cotangent bundle $\Omega_U$의 절단이고, derived critical locus $\Crit(f)$은 $df$의 유도 영점자리로 정의되었다. ([§Derived scheme과 derived stack, ⁋예시 17](/ko/math/derived_algebraic_geometry/derived_schemes#ex17)) 이 대상은 quasi-smooth이고 virtual 차원 $0$이며, 그 접복합체가 Hessian의 대칭성 때문에 여접 복합체와 자기쌍대적이라는 점을 우리는 이미 관찰하였다. 이 self-duality가 정확히 $(-1)$-shifted symplectic 구조로 정착됨을 이제 밝힌다.

::: 정리 8
$U$을 smooth $k$-scheme, $f:U\rightarrow\mathbb{A}^1$을 함수라 하자. Derived critical locus $\Crit(f)$은 canonically $(-1)$-shifted symplectic이다. 그 밑에 깔린 $2$-형식이 유도하는 nondegeneracy 동치

$$T_{\Crit(f)}\overset{\sim}{\longrightarrow}L_{\Crit(f)}[-1]$$

은 Hessian $\Hess(f)$의 대칭성에서 나오며, 이로써 $\Crit(f)$은 자기쌍대적 대칭 obstruction 이론을 가진다.
:::
::: 증명
$Z=\Crit(f)$이라 적자. 이는 rank $\dim U$의 다발 $\Omega_U$의 절단 $df$의 유도 영점자리이므로, [§Derived scheme과 derived stack, ⁋명제 13](/ko/math/derived_algebraic_geometry/derived_schemes#prop13)을 $E=\Omega_U$, $s=df$에 적용하면 embedding $Z\hookrightarrow U$의 상대 여접 복합체가 $L_{Z/U}\simeq(T_U\vert_Z)[1]$이 된다. $U$이 매끄러우므로 $L_U=\Omega_U$은 degree $0$에 집중되고, [§Derived scheme과 derived stack, ⁋명제 11](/ko/math/derived_algebraic_geometry/derived_schemes#prop11)의 추이 삼각형이

$$L_Z\simeq\Bigl[T_U\vert_Z\xrightarrow{\Hess(f)}\Omega_U\vert_Z\Bigr]$$

을 주는데, 여기서 $\Omega_U$이 degree $0$, $T_U$이 degree $1$에 놓이고 미분은 $df$의 미분, 곧 Hessian $\Hess(f)=\nabla(df)$이다. 이를 쌍대화하면

$$T_Z=L_Z^\vee\simeq\Bigl[T_U\vert_Z\xrightarrow{\Hess(f)^\top}\Omega_U\vert_Z\Bigr]$$

으로 $T_U$이 degree $0$, $\Omega_U$이 degree $-1$에 놓인다. Hessian은 이계 편미분의 행렬 $(\partial_i\partial_jf)$이라 대칭, 곧 $\Hess(f)^\top=\Hess(f)$이므로, 두 복합체의 미분이 일치하여 shift $[-1]$만큼 어긋난 동일한 복합체가 된다. 이것이 곧

$$T_Z\simeq L_Z[-1]$$

의 동치이며, degree를 대조하면 $n=-1$인 nondegeneracy 조건 $T_Z\simeq L_Z[n]$이다.

Closed $2$-형식 자체는 다음에서 온다. $\Crit(f)$은 cotangent bundle $T^\ast U$ 안에서 영절단 $U$과 $df$의 graph를 유도적으로 겹친 것이고, $T^\ast U$은 canonical 형식 $\omega_{\mathrm{can}}=d\lambda$으로 $0$-shifted symplectic이다. ([예시 6](#ex6)) 이 형식이 두 겹침 위에서 소멸하는 정합 자료가 $\Crit(f)$ 위의 degree $-1$의 closed $2$-형식을 낳으며, 위에서 계산한 $\omega_0^\flat$이 그 nondegeneracy를 준다. 이 구성이 뒤의 [정리 11](#thm11)에서 Lagrangian 교차의 특수한 경우로 다시 나타난다. 완전한 논증은 ([PTVV], [BBJ])에 있다.
:::

[정리 8](#thm8)의 핵심은 Hessian의 대칭성이라는 순전히 미적분적인 사실이 $(-1)$-shifted symplectic 구조라는 대역적 자료로 승격된다는 것이다. 고전적으로 $t_0(\Crit(f))=\Spec\bigl(k[U]/(\partial_1f,\ldots,\partial_nf)\bigr)$은 Jacobian ring의 spectrum일 뿐이지만, 유도 구조는 그 위에 자기쌍대적 obstruction 이론을 얹어 접방향과 여접방향을 한 번의 shift로 맞바꾼다. 이 국소 그림이 실은 모든 $(-1)$-shifted symplectic 대상의 보편적 모형이라는 것이 Brav–Bussi–Joyce의 Darboux 정리이다.

::: 정리 9 (Brav–Bussi–Joyce의 Darboux 정리)
$(X,\omega)$을 $(-1)$-shifted symplectic derived scheme이라 하자. 그러면 $X$은 Zariski 국소적으로 어떤 smooth scheme $U$ 위의 함수 $f:U\rightarrow\mathbb{A}^1$의 derived critical locus

$$X\vert_{\text{국소}}\simeq\Crit(f)$$

와 그 표준적 $(-1)$-shifted symplectic 구조에 동치이다. 그 결과 고전적 truncation $t_0(X)$은 자연스럽게 algebraic d-critical locus의 구조를 물려받는다.
:::
::: 증명
증명은 $X$을 국소적으로 표준 좌표를 갖는 affine derived scheme $\Spec A$으로 실현하는 데 있다. $A$을 smooth 대수 위의 free graded-commutative cdga로 cofibrant하게 놓으면, degree $-1$의 symplectic 형식은 Poincaré 보조정리의 shifted 판본에 의하여 국소적으로 $\omega=d\lambda$의 형태로 normalize되어 Darboux 좌표에서 표준형이 되고, 이때 $A$의 미분이 어떤 degree $0$의 Hamiltonian $\Phi$과의 Poisson bracket $\{\Phi,-\}$으로 주어짐을 보인다. 이 $\Phi$이 곧 smooth 국소 모형 $U$ 위의 함수 $f$이며, 표준형 cdga가 정확히 $\Crit(\Phi)$의 Koszul 복합체와 일치한다. Truncation이 d-critical 구조를 얻는 것은, 서로 다른 국소 표현에서 나온 함수 $f$들의 critical value가 정합적으로 접착되어 $t_0(X)$ 위의 하나의 canonical section을 이루기 때문이다. 완전한 논증은 ([BBJ])에 있다.
:::

Darboux 정리는 $(-1)$-shifted symplectic 기하가 왜 열거기하와 맞닿는지를 설명한다. Calabi–Yau 3-fold 위의 안정층의 moduli는 PTVV에 의하여 $(-1)$-shifted symplectic이고 ([정리 12](#thm12) 뒤의 논의), [정리 9](#thm9)에 의하여 국소적으로 $\Crit(f)$이므로, 그 위에서 Jacobian ring이 정의하는 vanishing cycle sheaf이나 Behrend 함수가 대역적으로 접착되어 Donaldson–Thomas 불변량의 categorified·motivic 판본을 낳는다. 곧 $(-1)$-shifted 구조는 DT 이론의 국소 재료인 critical point 자료를 기하적으로 조직하는 언어이다.

## Lagrangian과 mapping stack 구성

$n$-shifted symplectic 대상을 손으로 하나씩 만드는 대신, 우리는 그것을 생산하는 두 가지 보편적 조작을 원한다. 첫째는 부분대상에 해당하는 Lagrangian이고, 둘째는 그 교차와 mapping stack이다. 고전적으로 Lagrangian은 symplectic 형식이 위에서 소멸하는 절반 차원의 부분다양체였다. Derived 세계에서는 "소멸한다"가 다시 성질이 아니라 자료가 된다.

::: 정의 10
$(X,\omega)$을 $n$-shifted symplectic derived stack, $g:L\rightarrow X$을 morphism이라 하자. $L$ 위의 *isotropic 구조*란 pullback $g^\ast\omega\in\mathcal{A}^{2,\mathrm{cl}}(L,n)$을 $0$으로 이어 주는 homotopy $\gamma$, 곧 closed $2$-형식으로서의 nullhomotopy $\gamma:g^\ast\omega\sim0$이다. 이 자료는 상대 접복합체 위의 morphism

$$\Theta_\gamma:T_{L/X}\longrightarrow L_L[n-1]$$

을 유도한다. Isotropic 구조 $\gamma$이 *Lagrangian 구조*라는 것은 $\Theta_\gamma$이 동치인 것을 뜻하고, 이때 $g:L\rightarrow X$을 *Lagrangian morphism<sub>Lagrangian 사상</sub>*이라 부른다.
:::

Closed 형식이 자료였으므로, 그것을 $0$으로 축약하는 방법 또한 자료이다. Isotropic 구조는 바로 이 축약 자료이고, Lagrangian 구조는 그 축약이 상대 방향에서 비축퇴, 곧 $T_{L/X}\simeq L_L[n-1]$이 되도록 하는 것이다. 이 비축퇴 조건은 고전적으로 Lagrangian이 절반 차원을 갖는다는 조건의 유도 판본이다. $n=0$의 smooth 경우에 $T_{L/X}\simeq L_L[-1]$은 conormal exact sequence가 $L$을 $X$의 절반 차원 isotropic 부분다양체로 만든다는 것과 정확히 같다. Lagrangian이 두 개 있으면 그 교차에서 shift가 하나 내려간다.

::: 정리 11 (Lagrangian 교차, PTVV)
$(X,\omega)$을 $n$-shifted symplectic derived stack, $g_1:L_1\rightarrow X$과 $g_2:L_2\rightarrow X$을 Lagrangian morphism이라 하자. 그러면 유도 올곱

$$L_1\times_X^hL_2$$

은 canonically $(n-1)$-shifted symplectic이다.
:::
::: 증명
$W=L_1\times_X^hL_2$이라 하고 그 사영을 $\pi_j:W\rightarrow L_j$이라 하자. 두 isotropic 구조 $\gamma_1,\gamma_2$은 $W$ 위에서 pullback $\pi_1^\ast g_1^\ast\omega$과 $\pi_2^\ast g_2^\ast\omega$을 각각 $0$으로 잇는데, $W$ 위에서 두 pullback이 같은 형식 $\omega\vert_W$의 pullback이므로, 두 nullhomotopy의 차이 $\gamma_1-\gamma_2$이 $W$ 위의 degree $n-1$의 closed $2$-형식 $\omega_W$을 정의한다. Nondegeneracy는 $W$의 접복합체가 두 Lagrangian 조건이 주는 exact sequence

$$T_W\longrightarrow \pi_1^\ast T_{L_1}\oplus\pi_2^\ast T_{L_2}\longrightarrow T_X\vert_W$$

에 들어맞고, 각 $L_j$의 Lagrangian 동치 $T_{L_j/X}\simeq L_{L_j}[n-1]$을 대입하여 $T_W\simeq L_W[n-1]$을 얻는 데서 나온다. 이 마지막 대각 논증이 정확히 고전적 symplectic 선형대수에서 두 Lagrangian 부분공간의 교차와 합이 서로 여접적으로 짝지어진다는 사실의 유도 판본이다. 완전한 논증은 ([PTVV])에 있다.
:::

[정리 11](#thm11)은 [정리 8](#thm8)을 특수한 경우로 포함한다. $U$이 매끄러우면 cotangent bundle $T^\ast U$은 $0$-shifted symplectic이고, 영절단 $0:U\rightarrow T^\ast U$과 임의의 closed $1$-형식의 graph는 모두 Lagrangian morphism이다. 특히 $df$은 exact하므로 closed이고, 그 graph $\Gamma_{df}$은 Lagrangian이다. 두 Lagrangian $0$과 $\Gamma_{df}$의 유도 교차가 바로 $\Crit(f)$이므로, [정리 11](#thm11)이 $n=0$에서 $\Crit(f)$을 $(-1)$-shifted symplectic으로 만든다.

![Crit(f)를 두 Lagrangian의 유도 교차로 본 pullback 사각형](/assets/images/Math/Derived_Algebraic_Geometry/Shifted_Symplectic_Structures-1.svg){:style="width:9.20em" class="invert" .align-center}

두 번째 보편적 조작은 mapping stack이다. 물리학의 AKSZ 구성을 derived 기하로 옮긴 PTVV의 정리는, source가 적당한 "적분" 자료를 가지면 target의 shifted symplectic 구조가 mapping stack으로 옮겨지되 source의 차원만큼 shift가 내려감을 말한다.

::: 정리 12 (AKSZ mapping stack, PTVV)
$F$을 *$d$-orientation*을 갖춘 derived stack이라 하자. 곧 $F$은 $\mathcal{O}$-compact이고, 대역 절단 위에 degree $-d$의 비축퇴 적분 morphism

$$\int_F:H^\ast(F,\mathcal{O}_F)\longrightarrow k[-d]$$

을 가진다. 그러면 임의의 $n$-shifted symplectic derived stack $(X,\omega)$에 대하여, mapping stack

$$\operatorname{Map}(F,X)$$

은 canonically $(n-d)$-shifted symplectic이다. 그 형식은 evaluation morphism $\operatorname{ev}:F\times\operatorname{Map}(F,X)\rightarrow X$으로 $\omega$을 당긴 뒤 $F$ 위에서 $\int_F$으로 적분(transgression)하여 얻는다.
:::
::: 증명
$M=\operatorname{Map}(F,X)$의 접복합체는 evaluation과 $F$ 위의 pushforward로

$$T_M\simeq p_\ast\operatorname{ev}^\ast T_X$$

로 계산되는데, 여기서 $p:F\times M\rightarrow M$은 사영이다. Target의 nondegeneracy $\operatorname{ev}^\ast T_X\simeq\operatorname{ev}^\ast L_X[n]$을 대입하고, $F$의 $d$-orientation이 주는 Serre duality류 짝짓기 $p_\ast(-)\simeq p_\ast(-)^\vee[-d]$을 결합하면

$$T_M\simeq p_\ast\operatorname{ev}^\ast L_X[n]\simeq(p_\ast\operatorname{ev}^\ast T_X)^\vee[n-d]\simeq L_M[n-d]$$

을 얻어 nondegeneracy가 성립한다. Closed 형식은 $\int_F\operatorname{ev}^\ast\omega$이 mapping space 수준에서 정합적 닫힘 자료를 상속함을 확인하여 나오며, 이 transgression이 자료를 보존함이 이 구성의 요체이다. 완전한 논증은 ([PTVV], [Cal])에 있다.
:::

::: 참고 13
[정리 12](#thm12)의 $d$-orientation은 여러 형태로 실현된다. Betti 판본에서는 compact oriented $d$-variety $M$의 상수 stack이 그 fundamental class로 $d$-orientation을 주고, de Rham 판본에서는 차원 $d$의 smooth projective Calabi–Yau variety가 그 trivial canonical bundle과 trace morphism으로 $d$-orientation을 준다. 이로부터 shift의 부호에 따른 열거기하의 계층이 나온다. $X$이 $2$-shifted인 $\mathbf{B}G$이나 perfect 복합체의 moduli $\operatorname{Perf}$일 때, source의 차원 $d$에 따라 $\operatorname{Map}(F,X)$은 $(2-d)$-shifted가 된다. $d=2$이면 $0$-shifted가 되어 K3나 abelian surface 위의 sheaf의 moduli가 고전적 (holomorphic) symplectic 구조를 얻고, $d=3$이면 $(-1)$-shifted가 되어 [정리 9](#thm9)를 거쳐 Donaldson–Thomas 이론으로 이어지며, $d=4$이면 $(-2)$-shifted가 되어 Calabi–Yau 4-fold의 열거기하로 이어진다. 곧 shift의 정수값이 source Calabi–Yau의 차원을 직접 기록한다.
:::

## 예시: shifted 구조의 생산

앞의 두 정리는 구체적 moduli를 계산 가능한 대상으로 만든다. 먼저 [예시 6](#ex6)의 cotangent bundle을 임의의 shift로 올린 표준 대상을 본다.

::: 예시 14 (shifted 여접 stack)
Derived stack $X$과 정수 $n$에 대하여, *$n$-shifted 여접 stack*을 $X$ 위의 상대 Spec

$$T^\ast[n]X=\Spec_{\mathcal{O}_X}\Sym_{\mathcal{O}_X}\bigl(T_X[-n]\bigr)$$

으로 정의한다. 이는 여접 복합체 $L_X[n]$의 전체 공간에 해당하며, degree $n$의 canonical Liouville $1$-형식 $\lambda$을 가지고, 그 de Rham 미분 $\omega=d_{\dR}\lambda$이 $T^\ast[n]X$ 위의 $n$-shifted symplectic 구조를 준다. $n=0$이고 $X$이 smooth 고전적 variety이면 $T^\ast[0]X=T^\ast X$은 [예시 6](#ex6)의 통상적 cotangent bundle과 그 Liouville symplectic 구조로 되돌아온다. 반면 $n\neq0$이면 base $X$ 자체가 stack이거나 유도 두께를 가져도 되므로, 이 구성은 임의의 유도 대상 위에 표준적 shifted symplectic 두께를 자유롭게 공급한다. 특히 $X=\mathbf{B}G$, $n=1$이면 $T^\ast[1]\mathbf{B}G\simeq[\mathfrak{g}^\ast/G]$이 coadjoint quotient로서 $1$-shifted symplectic이 되어, 고전적 moment map 기하의 유도 판본을 준다.
:::

::: 예시 15 (local system의 moduli)
$G$을 semisimple algebraic group이라 하면 $\mathbf{B}G$은 [예시 7](#ex7)에 의하여 $2$-shifted symplectic이다. Compact oriented $d$-variety $M$의 Betti stack을 $M_B$이라 하면, mapping stack

$$\operatorname{Loc}_G(M)=\operatorname{Map}(M_B,\mathbf{B}G)$$

은 $M$ 위의 $G$-local system들의 유도 moduli stack이고, $M_B$이 fundamental class로 $d$-orientation을 가지므로 [정리 12](#thm12)에 의하여 $(2-d)$-shifted symplectic이다. $d=1$, 곧 $M=S^1$이면

$$\operatorname{Loc}_G(S^1)=\operatorname{Map}(S^1_B,\mathbf{B}G)\simeq[G/G]$$

이 adjoint quotient로서 $1$-shifted symplectic이 되는데, 이는 group-valued moment map 이론의 유사-Hamiltonian 구조를 유도 기하로 실현한 것이다. $d=2$, 곧 $M$이 genus $g$의 compact Riemann surface $\Sigma_g$이면 $\operatorname{Loc}_G(\Sigma_g)$은 $0$-shifted symplectic이 되고, 그 truncation 위의 형식이 character variety 위의 고전적 Atiyah–Bott–Goldman symplectic 형식을 정확히 복원한다. 이 마지막 형식을 Lagrangian 교차로도 볼 수 있다. Surface를 두 handle body류 조각으로 자르면 $\operatorname{Loc}_G(\Sigma_g)$이 $1$-shifted symplectic인 $[G/G]$류 대상 안에서 두 Lagrangian의 유도 교차로 나타나고, [정리 11](#thm11)이 shift를 $1$에서 $0$으로 내려 같은 $0$-shifted 구조를 준다. 곧 하나의 shifted symplectic 형식이 mapping stack 관점과 Lagrangian 교차 관점에서 동시에 나오며, 이 정합성이 shifted symplectic 기하가 위상적 장이론의 언어를 대수기하 안에서 재현하는 방식이다.
:::

이로써 우리는 여접 복합체의 exterior power에서 출발하여 $p$-형식과 closed 형식의 공간을 세우고, 접복합체와 여접 복합체를 shift만큼 어긋난 동형으로 잇는 nondegeneracy를 부과하여 $n$-shifted symplectic 구조를 얻었다. Degree $0$은 고전적 symplectic variety를, degree $2$는 reductive group의 분류 stack을, degree $-1$은 derived critical locus와 Calabi–Yau 3-fold의 열거기하를 담는다. 그리고 Lagrangian 교차와 AKSZ mapping stack이라는 두 보편적 조작이 이 구조들을 서로 낳으며, 유도 moduli 위에 virtual class를 조직하는 symmetric 뼈대를 제공한다. 이것이 PTVV가 derived algebraic geometry 위에 세운 shifted symplectic 기하의 골격이다.

---

**참고문헌**

**[PTVV]** T. Pantev, B. Toën, M. Vaquié, G. Vezzosi, *Shifted symplectic structures*, Publications mathématiques de l'IHÉS 117 (2013), 271–328.  
**[BBJ]** C. Brav, V. Bussi, D. Joyce, *A Darboux theorem for shifted symplectic structures on derived Artin stacks, with applications*, Geometry & Topology 19 (2015), 1287–1359.  
**[Cal]** D. Calaque, *Lectures on shifted symplectic geometry*, lecture notes.  
**[Toë]** B. Toën, *Derived algebraic geometry*, EMS Surveys in Mathematical Sciences 1 (2014), 153–240.
