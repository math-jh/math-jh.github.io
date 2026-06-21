---
title: "Killing 형식과 Cartan 판정법"
description: "Lie algebra 위의 Killing form을 adjoint representation의 trace로 정의하고 그 invariance와 ideal 제한 성질을 정리한 뒤, trace form lemma로부터 Cartan의 가해성 판정법과 반단순성 판정법을 증명한다. 반단순 Lie algebra가 simple ideal들의 직합으로 분해됨도 보인다."
excerpt: "Killing form, invariance, Cartan의 가해성·반단순성 판정, simple ideal 직합 분해"

categories: [Math / Lie Theory]
permalink: /ko/math/lie_theory/killing_form_and_cartan_criterion
sidebar: 
    nav: "lie_theory-ko"

date: 2026-06-21
weight: 3.6

published: false
---

가해성과 nilpotency를 derived series와 lower central series로 정의하고 Engel·Lie의 정리를 증명한 뒤 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋정의 10](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#def10)), 우리는 임의의 유한차원 Lie algebra가 가장 큰 가해 ideal인 radical과 그 몫인 반단순 부분으로 나뉜다는 것을 보았다. 그러나 그 정의만으로는 주어진 Lie algebra가 가해인지, 혹은 반단순인지를 직접 판정하기 어렵다. Cartan은 이 두 물음을 모두 하나의 bilinear form, 곧 Killing form의 trace 조건으로 환원하였다. 이 글에서 우리는 Killing form $$\kappa(x,y)=\tr(\ad x\,\ad y)$$를 정의하고 그 invariance와 ideal에 대한 제한 성질을 정리한 뒤, 임의의 $$\mathfrak{g}\subseteq\gl(V)$$의 가해성이 trace form의 소멸로 판정된다는 Cartan의 가해성 판정법과, $$\mathfrak{g}$$의 반단순성이 Killing form의 nondegeneracy로 판정된다는 Cartan의 반단순성 판정법을 증명한다.

이 글 전체에서 $$k$$는 대수적으로 닫힌 표수 $$0$$의 체이고, 별다른 언급이 없는 한 $$\mathfrak{g}$$는 $$k$$ 위의 유한차원 Lie algebra이다. $$\ad:\mathfrak{g}\rightarrow\gl(\mathfrak{g})$$는 adjoint representation ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋정의 6](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#def6))을 가리키며, $$\rad\mathfrak{g}$$는 radical ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋정의 15](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#def15))을 가리킨다.

## Killing form

Lie algebra 위에는 자기 자신에 대한 작용인 adjoint representation이 항상 존재하므로, 두 원소 $$x,y$$에 대하여 합성 $$\ad x\,\ad y\in\gl(\mathfrak{g})$$의 trace를 취하는 것이 자연스럽다. 이로써 얻어지는 bilinear form이 Lie algebra의 구조 이론 전체를 떠받친다.

<div class="definition" markdown="1">

<ins id="def1">**정의 1**</ins> 유한차원 Lie algebra $$\mathfrak{g}$$ 위에서

$$\kappa(x,y)=\tr(\ad x\,\ad y)$$

으로 정의되는 symmetric bilinear form $$\kappa:\mathfrak{g}\times\mathfrak{g}\rightarrow k$$를 $$\mathfrak{g}$$의 *Killing form*이라 부른다.

</div>

$$\kappa$$가 bilinear인 것은 $$\ad$$가 선형이고 trace가 선형이라는 데에서, symmetric인 것은 임의의 두 endomorphism $$f,g$$에 대하여 $$\tr(fg)=\tr(gf)$$라는 데에서 곧바로 따라온다. Killing form의 가장 기본적이면서 핵심적인 성질은 bracket과 호환된다는 것, 곧 *invariance<sub>불변성</sub>* 혹은 *associativity<sub>결합성</sub>*라 불리는 다음 항등식이다.

<div class="proposition" markdown="1">

<ins id="prop2">**명제 2**</ins> 임의의 $$x,y,z\in\mathfrak{g}$$에 대하여

$$\kappa([x,y],z)=\kappa(x,[y,z])$$

이 성립한다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\ad$$가 Lie algebra homomorphism이므로 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋명제 7](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#prop7)) $$\ad[x,y]=[\ad x,\ad y]=\ad x\,\ad y-\ad y\,\ad x$$이다. 임의의 endomorphism $$f,g,h$$에 대하여 $$\tr([f,g]h)=\tr(f[g,h])$$가 성립함을 이용한다. 실제로 trace의 순환성에서

$$\tr([f,g]h)=\tr(fgh)-\tr(gfh),\qquad \tr(f[g,h])=\tr(fgh)-\tr(fhg)$$

이고 $$\tr(gfh)=\tr(fhg)$$이므로 두 식이 같다. 이를 $$f=\ad x$$, $$g=\ad y$$, $$h=\ad z$$에 적용하면

$$\kappa([x,y],z)=\tr(\ad[x,y]\,\ad z)=\tr([\ad x,\ad y]\,\ad z)=\tr(\ad x\,[\ad y,\ad z])=\tr(\ad x\,\ad[y,z])=\kappa(x,[y,z])$$

을 얻는다.

</details>

Invariance를 $$\kappa([x,y],z)+\kappa(y,[x,z])=0$$의 꼴로 다시 쓰면, 이는 각 $$\ad x$$가 Killing form에 대하여 skew-adjoint임을 뜻한다. 이 형태는 $$\mathfrak{g}$$가 어떤 Lie group의 Lie algebra일 때, Killing form이 adjoint action에 대해 불변이라는 사실 ([§근계, ⁋정의 1](/ko/math/lie_theory/root_systems#def1) 이후의 논의)을 $$e$$에서 미분하여 얻는 무한소 판본이다. 같은 invariance는 Lie algebra automorphism에 대해서도 성립한다.

<div class="proposition" markdown="1">

<ins id="prop3">**명제 3**</ins> $$\sigma:\mathfrak{g}\rightarrow\mathfrak{g}$$가 Lie algebra automorphism이면 임의의 $$x,y\in\mathfrak{g}$$에 대하여

$$\kappa(\sigma x,\sigma y)=\kappa(x,y)$$

이다. 곧 Killing form은 $$\Aut(\mathfrak{g})$$-불변이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\sigma$$가 bracket을 보존하므로 임의의 $$x,z\in\mathfrak{g}$$에 대하여 $$\sigma([x,z])=[\sigma x,\sigma z]$$이다. 이를 $$\ad$$로 다시 적으면 $$\sigma(\ad x)(z)=(\ad\sigma x)(\sigma z)$$이므로, $$\sigma$$가 가역임을 써서

$$\ad\sigma x=\sigma\circ\ad x\circ\sigma^{-1}$$

을 얻는다. 따라서

$$\ad\sigma x\,\ad\sigma y=(\sigma\,\ad x\,\sigma^{-1})(\sigma\,\ad y\,\sigma^{-1})=\sigma\,(\ad x\,\ad y)\,\sigma^{-1}$$

이고, 켤레는 trace를 보존하므로

$$\kappa(\sigma x,\sigma y)=\tr(\sigma\,(\ad x\,\ad y)\,\sigma^{-1})=\tr(\ad x\,\ad y)=\kappa(x,y)$$

이다.

</details>

Killing form은 정의에 $$\mathfrak{g}$$ 전체에 대한 trace가 들어 있으므로, ideal로 제한할 때 그 ideal 자신의 Killing form과 어떤 관계인지가 문제된다. 다행히 둘은 정확히 일치한다.

<div class="proposition" markdown="1">

<ins id="prop4">**명제 4**</ins> $$\mathfrak{a}$$가 $$\mathfrak{g}$$의 ideal이고 $$\kappa_{\mathfrak{a}}$$가 Lie algebra $$\mathfrak{a}$$ 자신의 Killing form이면, 임의의 $$x,y\in\mathfrak{a}$$에 대하여

$$\kappa(x,y)=\kappa_{\mathfrak{a}}(x,y)$$

이다. 곧 $$\mathfrak{g}$$의 Killing form을 $$\mathfrak{a}\times\mathfrak{a}$$로 제한한 것은 $$\mathfrak{a}$$의 Killing form과 같다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

선형대수의 다음 사실을 이용한다. $$W$$가 유한차원 벡터공간 $$V$$의 부분공간이고 $$\phi\in\End(V)$$가 $$\phi(V)\subseteq W$$를 만족하면, $$\tr_V(\phi)=\tr_W(\phi\vert_W)$$이다. 실제로 $$W$$의 기저를 $$V$$의 기저로 확장하면 $$\phi$$의 행렬은 마지막 열들이 $$0$$인 블록 형태가 되어, 전체 trace가 $$W$$ 부분 블록의 trace와 같아진다.

이제 $$x,y\in\mathfrak{a}$$를 고정하자. $$\mathfrak{a}$$가 ideal이므로 임의의 $$z\in\mathfrak{g}$$에 대하여 $$[x,[y,z]]\in\mathfrak{a}$$, 곧 $$\phi=\ad x\,\ad y$$는 $$\mathfrak{g}$$를 $$\mathfrak{a}$$ 안으로 보낸다. 따라서 위 사실에 의해

$$\kappa(x,y)=\tr_{\mathfrak{g}}(\ad x\,\ad y)=\tr_{\mathfrak{a}}\bigl((\ad x\,\ad y)\vert_{\mathfrak{a}}\bigr)$$

이다. 한편 $$x,y\in\mathfrak{a}$$이므로 $$(\ad x\,\ad y)\vert_{\mathfrak{a}}=\ad_{\mathfrak{a}}x\,\ad_{\mathfrak{a}}y$$이며, 여기에서 $$\ad_{\mathfrak{a}}$$는 $$\mathfrak{a}$$ 위의 adjoint representation이다. 그러므로 우변은 $$\tr_{\mathfrak{a}}(\ad_{\mathfrak{a}}x\,\ad_{\mathfrak{a}}y)=\kappa_{\mathfrak{a}}(x,y)$$이다.

</details>

이 제한 성질 덕분에 Killing form은 ideal 단위로 분석된다. 특히 $$\mathfrak{g}$$의 Killing form에 대한 *radical<sub>근기</sub>*

$$\mathfrak{g}^{\perp}=\left\{x\in\mathfrak{g}\mid \kappa(x,y)=0\text{ for all }y\in\mathfrak{g}\right\}$$

은 그 자체로 $$\mathfrak{g}$$의 ideal이 된다. 임의의 $$x\in\mathfrak{g}^{\perp}$$, $$z\in\mathfrak{g}$$에 대하여 invariance ([명제 2](#prop2))로부터 $$\kappa([z,x],y)=-\kappa(x,[z,y])=0$$이 모든 $$y$$에 대해 성립하기 때문이다. Killing form이 nondegenerate라는 것은 정확히 $$\mathfrak{g}^{\perp}=0$$이라는 것이며, 아래에서 이 조건이 반단순성과 동치임을 본다.

## Jordan–Chevalley 분해

Cartan의 판정법의 증명은 단 한 번, endomorphism을 반단순 부분과 nilpotent 부분으로 쪼개는 분해에 의존한다. 우리는 이를 선형대수의 사실로서 상기한다.

<div class="proposition" markdown="1">

<ins id="prop5">**명제 5 (Jordan–Chevalley)**</ins> $$V$$가 대수적으로 닫힌 체 $$k$$ 위의 유한차원 벡터공간이고 $$x\in\End(V)$$라 하자. 그럼 다음을 만족하는 $$x_s,x_n\in\End(V)$$가 유일하게 존재한다.

1. $$x=x_s+x_n$$이고 $$x_s$$는 diagonalizable, $$x_n$$은 nilpotent이며 $$x_s x_n=x_n x_s$$이다.
2. $$x_s$$와 $$x_n$$은 각각 $$x$$의 상수항 없는 다항식으로 표현된다.

또한 $$\ad x_s$$는 diagonalizable, $$\ad x_n$$은 nilpotent이고 두 사상이 commute하므로, $$\ad x=\ad x_s+\ad x_n$$이 $$\gl(V)$$ 안에서 $$\ad x$$의 Jordan–Chevalley 분해이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$x$$의 특성다항식을 $$\prod_i (T-\lambda_i)^{m_i}$$ ($$\lambda_i$$는 서로 다른 고윳값) 라 하자. 중국인의 나머지정리로 각 $$i$$에 대해 $$p(T)\equiv\lambda_i\pmod{(T-\lambda_i)^{m_i}}$$ (그리고 $$0$$이 고윳값이면 $$p(T)\equiv 0\pmod T$$를 함께) 를 만족하는 상수항 없는 다항식 $$p$$가 존재한다. $$x_s=p(x)$$, $$x_n=x-x_s$$로 두면, 각 일반화 고유공간 $$V_i=\ker(x-\lambda_i)^{m_i}$$ 위에서 $$x_s$$는 스칼라 $$\lambda_i$$로 작용하므로 $$x_s$$는 diagonalizable이고 $$x_n=x-x_s$$는 $$V_i$$ 위에서 nilpotent이다. 둘 다 $$x$$의 다항식이므로 서로 commute하며 $$x$$와 commute하는 임의의 endomorphism과도 commute한다. 유일성은 다음에서 온다. $$x=s+n$$이 조건 1을 만족하는 또 하나의 분해이면 $$s,n$$은 $$x$$와 commute하므로 $$x$$의 다항식인 $$x_s,x_n$$과도 commute한다. 그럼 $$x_s-s=n-x_n$$에서 좌변은 commuting diagonalizable들의 차로 diagonalizable, 우변은 commuting nilpotent들의 차로 nilpotent인데, diagonalizable이면서 nilpotent인 endomorphism은 $$0$$뿐이므로 $$s=x_s$$, $$n=x_n$$이다. 끝으로 $$\ad x_s$$가 diagonalizable, $$\ad x_n$$이 nilpotent이고 둘이 commute하므로, 방금 보인 유일성에 의해 $$\ad x=\ad x_s+\ad x_n$$이 $$\ad x$$의 Jordan–Chevalley 분해이다.

</details>

여기에서 $$x_s$$를 $$x$$의 *semisimple part<sub>반단순 부분</sub>*, $$x_n$$을 *nilpotent part<sub>nilpotent 부분</sub>*라 부른다. $$x_s,x_n$$이 다항식으로 주어진다는 사실로부터 $$x$$와 commute하는 모든 endomorphism이 $$x_s,x_n$$과도 commute함이 따라온다. 우리가 아래에서 실제로 쓰는 것은 다음 한 가지 사실뿐이다. $$x=x_s+x_n$$이 $$x\in\End(V)$$의 분해이고 $$x_s$$의 고윳값이 $$\lambda_1,\ldots,\lambda_n$$이면, 임의의 다항식 $$p\in k[T]$$로 만든 endomorphism은 적절한 좌표에서 통제되며, 특히 trace $$\tr(x\,y)$$를 고윳값의 항으로 분석할 수 있다는 것이다. 이 점은 다음 절의 보조정리에서 구체화된다.

## Cartan의 가해성 판정

Cartan의 가해성 판정법은 $$\gl(V)$$의 부분대수가 가해인지를 trace의 소멸이라는 검사 가능한 조건으로 환원한다. 그 핵심은 어떤 endomorphism이 nilpotent임을 trace 조건만으로 판정하는 다음 보조정리이며, 이것이 증명에서 Jordan–Chevalley 분해를 쓰는 유일한 지점이다.

<div class="proposition" markdown="1">

<ins id="lem6">**보조정리 6**</ins> $$V$$가 유한차원 $$k$$-벡터공간이고 $$A\subseteq B$$가 $$\gl(V)$$의 두 부분공간이라 하자.

$$M=\left\{x\in\gl(V)\mid [x,B]\subseteq A\right\}$$

으로 둘 때, 어떤 $$x\in M$$이 모든 $$y\in M$$에 대하여 $$\tr(xy)=0$$을 만족하면 $$x$$는 nilpotent endomorphism이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$x=s+n$$을 $$x$$의 Jordan–Chevalley 분해 ([명제 5](#prop5))라 하고, $$s$$가 어떤 기저에서 대각성분 $$\lambda_1,\ldots,\lambda_m$$의 대각행렬이라 하자. $$x$$가 nilpotent임을 보이는 것은 모든 $$\lambda_i=0$$임을 보이는 것과 같다. 고윳값들이 생성하는 $$\mathbb{Q}$$-벡터공간 $$E=\span_{\mathbb{Q}}\{\lambda_1,\ldots,\lambda_m\}$$을 생각하고, $$E=0$$임을 보이기 위해 임의의 $$\mathbb{Q}$$-선형범함수 $$f:E\rightarrow\mathbb{Q}$$가 항등적으로 $$0$$임을 보인다.

$$f$$가 주어지면, 같은 기저에서 대각성분이 $$f(\lambda_1),\ldots,f(\lambda_m)$$인 대각행렬 $$y$$를 정의한다. $$s$$의 고유공간 분해에 맞춰 $$\ad s$$는 행렬단위 $$e_{ij}$$ 위에서 $$(\lambda_i-\lambda_j)$$로, $$\ad y$$는 $$(f(\lambda_i)-f(\lambda_j))$$로 작용한다. $$f$$가 $$\mathbb{Q}$$-선형이므로 $$\lambda_i-\lambda_j\mapsto f(\lambda_i)-f(\lambda_j)$$를 보내는 다항식 $$r\in k[T]$$로 (Lagrange 보간을 써서, 상수항 없이) $$\ad y=r(\ad s)$$가 되도록 할 수 있다. 한편 $$\ad s$$는 $$\ad x$$의 반단순 부분이므로 $$\ad x$$의 상수항 없는 다항식이며, 따라서 $$\ad y$$도 $$\ad x$$의 상수항 없는 다항식이다. $$x\in M$$, 곧 $$\ad x(B)\subseteq A$$이므로 $$\ad x(A)\subseteq\ad x(B)\subseteq A$$이고 $$\ad y$$가 $$\ad x$$의 다항식이라는 점에서 $$\ad y(B)\subseteq A$$, 곧 $$y\in M$$이다.

따라서 가정에 의해 $$\tr(xy)=0$$이다. 그런데 $$xy$$의 대각성분은 $$\lambda_i f(\lambda_i)$$이므로

$$0=\tr(xy)=\sum_{i=1}^{m}\lambda_i f(\lambda_i)$$

이다. 양변에 $$f$$를 적용하면 ($$f(\lambda_i)\in\mathbb{Q}\subseteq k$$이고 $$f$$가 $$\mathbb{Q}$$-선형) $$\sum_i f(\lambda_i)^2=0$$을 얻는데, $$f(\lambda_i)$$는 모두 유리수이므로 각 $$f(\lambda_i)=0$$이다. $$f$$가 $$\lambda_i$$들에서 모두 $$0$$이고 이들이 $$E$$를 생성하므로 $$f=0$$이다. 임의의 $$f$$에 대해 그러하므로 $$E=0$$, 곧 모든 $$\lambda_i=0$$이며 $$s=0$$이다. 따라서 $$x=n$$은 nilpotent이다.

</details>

이 보조정리를 $$A=[\mathfrak{g},\mathfrak{g}]$$, $$B=\mathfrak{g}$$로 적용할 채비를 한 뒤 Cartan의 판정법을 서술한다. 가해성의 충분조건 방향은 Lie의 정리로부터 derived algebra의 원소가 strictly 상삼각화된다는 사실 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋따름정리 21](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#cor21))과 결합된다.

<div class="proposition" markdown="1">

<ins id="thm7">**정리 7 (Cartan의 가해성 판정법)**</ins> $$V$$가 $$0$$이 아닌 유한차원 $$k$$-벡터공간이고 $$\mathfrak{g}\subseteq\gl(V)$$가 부분대수라 하자. 그럼 $$\mathfrak{g}$$가 solvable인 것과, 모든 $$x\in[\mathfrak{g},\mathfrak{g}]$$와 $$y\in\mathfrak{g}$$에 대하여

$$\tr(xy)=0$$

인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

($$\Rightarrow$$) $$\mathfrak{g}$$가 solvable이라 하자. [§가해 Lie algebra와 nilpotent Lie algebra, ⁋따름정리 21](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#cor21)에 의해 $$V$$의 적절한 기저에서 $$\mathfrak{g}$$의 모든 원소가 상삼각행렬로 표현된다. 그럼 $$[\mathfrak{g},\mathfrak{g}]$$의 원소는 두 상삼각행렬의 commutator이므로 대각성분이 모두 $$0$$인 strictly 상삼각행렬이다. 임의의 $$x\in[\mathfrak{g},\mathfrak{g}]$$ (strictly 상삼각)와 $$y\in\mathfrak{g}$$ (상삼각)에 대하여 $$xy$$는 strictly 상삼각이고, 따라서 $$\tr(xy)=0$$이다.

($$\Leftarrow$$) trace 조건을 가정한다. $$\mathfrak{g}$$가 solvable임을 보이는 것은 $$[\mathfrak{g},\mathfrak{g}]$$가 solvable임을 보이는 것으로 충분하다. $$\mathfrak{g}/[\mathfrak{g},\mathfrak{g}]$$는 abelian, 따라서 solvable이고, $$[\mathfrak{g},\mathfrak{g}]$$가 solvable이면 확장에 대한 닫힘성 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋명제 14](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#prop14))에서 $$\mathfrak{g}$$가 solvable이기 때문이다. $$[\mathfrak{g},\mathfrak{g}]\subseteq\mathfrak{gl}(V)$$의 모든 원소가 nilpotent endomorphism임을 보이면, Engel 정리의 선형 형태 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋따름정리 17](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#cor17))에 의해 $$[\mathfrak{g},\mathfrak{g}]$$가 동시에 strictly 상삼각화되어 nilpotent Lie algebra, 특히 solvable임이 따른다.

[보조정리 6](#lem6)을 $$A=[\mathfrak{g},\mathfrak{g}]$$, $$B=\mathfrak{g}$$에 적용한다. 이때

$$M=\left\{z\in\gl(V)\mid [z,\mathfrak{g}]\subseteq[\mathfrak{g},\mathfrak{g}]\right\}$$

은 $$\mathfrak{g}$$를 포함한다. 임의의 $$x\in[\mathfrak{g},\mathfrak{g}]$$를 고정하자. $$x$$가 nilpotent임을 보이려면, 보조정리에 의해 모든 $$z\in M$$에 대하여 $$\tr(xz)=0$$임을 보이면 충분하다. $$x$$는 $$[\mathfrak{g},\mathfrak{g}]$$의 원소이므로 $$x=\sum_i[a_i,b_i]$$ ($$a_i,b_i\in\mathfrak{g}$$) 꼴이며, trace의 선형성에서 각 $$[a,b]$$ ($$a,b\in\mathfrak{g}$$)에 대하여 $$\tr([a,b]z)=0$$임만 보이면 된다. 다음 항등식

$$\tr([a,b]z)=\tr(a[b,z])=\tr([z,a]b)$$

을 쓴다 (이는 [명제 2](#prop2)의 증명에서 본 $$\tr([f,g]h)=\tr(f[g,h])$$의 두 가지 적용이다). $$z\in M$$이므로 $$[z,a]\in[\mathfrak{g},\mathfrak{g}]$$이고 $$b\in\mathfrak{g}$$이다. 가정에 의해 $$[\mathfrak{g},\mathfrak{g}]$$의 원소와 $$\mathfrak{g}$$의 원소를 곱한 trace는 $$0$$이므로 $$\tr([z,a]b)=0$$, 곧 $$\tr([a,b]z)=0$$이다. 따라서 $$\tr(xz)=0$$이 모든 $$z\in M$$에 대해 성립하여 $$x$$는 nilpotent endomorphism이다. 이로써 $$[\mathfrak{g},\mathfrak{g}]$$의 모든 원소가 nilpotent이고, 결론이 따른다.

</details>

이 판정법을 추상적 Lie algebra $$\mathfrak{g}$$에 직접 적용하려면 $$\mathfrak{g}$$를 $$\gl(V)$$ 안으로 실현해야 하는데, $$V=\mathfrak{g}$$로 두고 $$\ad:\mathfrak{g}\rightarrow\gl(\mathfrak{g})$$를 쓰는 것이 자연스럽다. 그 결과 Killing form만으로 가해성을 판정하는 다음 따름정리를 얻는다.

<div class="proposition" markdown="1">

<ins id="cor8">**따름정리 8**</ins> 유한차원 Lie algebra $$\mathfrak{g}$$가 solvable인 것과

$$\kappa(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0,$$

곧 모든 $$x\in\mathfrak{g}$$, $$y\in[\mathfrak{g},\mathfrak{g}]$$에 대하여 $$\kappa(x,y)=0$$인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\ad:\mathfrak{g}\rightarrow\gl(\mathfrak{g})$$를 생각하면 $$\ker(\ad)=Z(\mathfrak{g})$$ ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋명제 7](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#prop7))이므로 $$\ad\mathfrak{g}\cong\mathfrak{g}/Z(\mathfrak{g})$$이고, 상 $$\ad\mathfrak{g}\subseteq\gl(\mathfrak{g})$$는 부분대수이다.

먼저 $$\mathfrak{g}$$가 solvable이라 하자. 그 몫인 $$\ad\mathfrak{g}$$도 solvable이고 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋명제 14](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#prop14)), [정리 7](#thm7)에 의해 모든 $$\ad x\in[\ad\mathfrak{g},\ad\mathfrak{g}]$$와 $$\ad y\in\ad\mathfrak{g}$$에 대하여 $$\tr(\ad x\,\ad y)=0$$이다. $$[\ad\mathfrak{g},\ad\mathfrak{g}]=\ad[\mathfrak{g},\mathfrak{g}]$$이므로, 이는 모든 $$x\in[\mathfrak{g},\mathfrak{g}]$$, $$y\in\mathfrak{g}$$에 대하여 $$\kappa(x,y)=\tr(\ad x\,\ad y)=0$$임을 뜻한다. $$\kappa$$가 symmetric이므로 곧 $$\kappa(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0$$이다.

역으로 $$\kappa(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0$$이라 하자. 그럼 모든 $$x\in[\mathfrak{g},\mathfrak{g}]$$, $$y\in\mathfrak{g}$$에 대하여 $$\tr(\ad x\,\ad y)=0$$이다. $$[\ad\mathfrak{g},\ad\mathfrak{g}]=\ad[\mathfrak{g},\mathfrak{g}]$$이므로 이는 [정리 7](#thm7)의 trace 조건을 $$\ad\mathfrak{g}\subseteq\gl(\mathfrak{g})$$에 대해 정확히 만족하며, 따라서 $$\ad\mathfrak{g}$$는 solvable이다. 그런데 $$\ad\mathfrak{g}\cong\mathfrak{g}/Z(\mathfrak{g})$$이고 $$Z(\mathfrak{g})$$는 abelian, 따라서 solvable이므로, $$\mathfrak{g}/Z(\mathfrak{g})$$와 $$Z(\mathfrak{g})$$가 모두 solvable이라는 데에서 확장에 대한 닫힘성 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋명제 14](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#prop14))으로 $$\mathfrak{g}$$가 solvable이다.

</details>

## Cartan의 반단순성 판정

이제 반단순성을 다룬다. $$\mathfrak{g}$$가 *semisimple*이라는 것은 그 radical이 $$0$$인 것, 곧 $$\mathfrak{g}$$가 $$0$$이 아닌 solvable ideal을 갖지 않는 것이었다 ([§가해 Lie algebra와 nilpotent Lie algebra, ⁋정의 15](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#def15) 이후의 논의). 가해성 판정법의 따름으로, 반단순성은 Killing form의 nondegeneracy와 정확히 일치한다.

<div class="proposition" markdown="1">

<ins id="thm9">**정리 9 (Cartan의 반단순성 판정법)**</ins> 유한차원 Lie algebra $$\mathfrak{g}$$가 semisimple인 것과 그 Killing form $$\kappa$$가 nondegenerate인 것이 동치이다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\mathfrak{g}^{\perp}=\{x\in\mathfrak{g}\mid\kappa(x,\mathfrak{g})=0\}$$을 Killing form의 radical이라 하면, 앞서 보았듯 이는 $$\mathfrak{g}$$의 ideal이고, $$\kappa$$가 nondegenerate인 것은 $$\mathfrak{g}^{\perp}=0$$인 것이다.

($$\Rightarrow$$의 대우) $$\mathfrak{g}^{\perp}\neq 0$$이라 하자. $$\mathfrak{g}^{\perp}$$ 위에서 $$\kappa$$는 항등적으로 $$0$$이므로, 특히 모든 $$x\in\mathfrak{g}^{\perp}$$, $$y\in[\mathfrak{g}^{\perp},\mathfrak{g}^{\perp}]\subseteq\mathfrak{g}^{\perp}$$에 대하여 $$\kappa(x,y)=0$$이다. [명제 4](#prop4)에 의해 $$\mathfrak{g}$$의 Killing form을 ideal $$\mathfrak{g}^{\perp}$$로 제한한 것은 $$\mathfrak{g}^{\perp}$$ 자신의 Killing form $$\kappa_{\mathfrak{g}^{\perp}}$$와 같으므로, $$\kappa_{\mathfrak{g}^{\perp}}(\mathfrak{g}^{\perp},[\mathfrak{g}^{\perp},\mathfrak{g}^{\perp}])=0$$이다. [따름정리 8](#cor8)을 Lie algebra $$\mathfrak{g}^{\perp}$$에 적용하면 $$\mathfrak{g}^{\perp}$$은 solvable이다. 따라서 $$\mathfrak{g}$$는 $$0$$이 아닌 solvable ideal $$\mathfrak{g}^{\perp}$$을 가지므로 $$\rad\mathfrak{g}\neq 0$$, 곧 $$\mathfrak{g}$$는 semisimple이 아니다.

($$\Leftarrow$$의 대우) $$\mathfrak{g}$$가 semisimple이 아니라 하자. 그럼 $$\rad\mathfrak{g}\neq 0$$이고, $$\rad\mathfrak{g}$$이 $$0$$이 아닌 solvable ideal이므로 그 derived series의 마지막 비자명한 항을 $$\mathfrak{a}$$라 하면 $$\mathfrak{a}$$는 $$0$$이 아닌 abelian ideal이다. ($$\mathfrak{a}=\mathfrak{r}^{(m-1)}$$에서 $$\mathfrak{r}^{(m)}=0$$이면 $$[\mathfrak{a},\mathfrak{a}]=0$$이고, $$\rad\mathfrak{g}$$의 derived series의 각 항이 $$\mathfrak{g}$$의 ideal임은 [§가해 Lie algebra와 nilpotent Lie algebra, ⁋정의 8](/ko/math/lie_theory/solvable_nilpotent_lie_algebras#def8) 이후의 논의에서 확인된다.) 이제 $$\mathfrak{a}\subseteq\mathfrak{g}^{\perp}$$임을 보인다.

임의의 $$a\in\mathfrak{a}$$와 $$x\in\mathfrak{g}$$를 택하자. $$\ad a\,\ad x$$는 $$\mathfrak{g}$$를 $$\mathfrak{a}$$ 안으로 보낸다. 실제로 $$\ad x$$는 $$\mathfrak{g}$$를 $$\mathfrak{g}$$로 보내고 $$\ad a$$는 ($$\mathfrak{a}$$가 ideal이므로) $$\mathfrak{g}$$를 $$\mathfrak{a}$$로 보내기 때문이다. 그럼 $$\phi=\ad a\,\ad x$$에 대하여 $$\phi(\mathfrak{g})\subseteq\mathfrak{a}$$이고 $$\phi(\mathfrak{a})\subseteq[\mathfrak{a},[\mathfrak{g},\mathfrak{a}]]\subseteq[\mathfrak{a},\mathfrak{a}]=0$$이므로 ($$\mathfrak{a}$$가 abelian), $$\phi^2(\mathfrak{g})\subseteq\phi(\mathfrak{a})=0$$이다. 곧 $$\phi$$는 nilpotent endomorphism이고, nilpotent endomorphism의 trace는 $$0$$이므로

$$\kappa(a,x)=\tr(\ad a\,\ad x)=\tr(\phi)=0$$

이다. $$x\in\mathfrak{g}$$가 임의였으므로 $$a\in\mathfrak{g}^{\perp}$$이고, 따라서 $$0\neq\mathfrak{a}\subseteq\mathfrak{g}^{\perp}$$이다. 곧 $$\kappa$$는 nondegenerate가 아니다.

</details>

이 판정법은 [§근계, ⁋명제 3](/ko/math/lie_theory/root_systems#prop3)에서 증명 없이 인용했던 동치, 곧 반단순성과 Killing form의 nondegeneracy의 동치를 정확히 채운다. nondegenerate Killing form은 $$\mathfrak{g}$$ 위에 invariant nondegenerate symmetric bilinear form을 제공하며, 이는 반단순 Lie algebra의 구조 이론 전체에서 직교 분해의 도구로 쓰인다. 그 첫 적용으로, 반단순 Lie algebra가 simple ideal들의 직합으로 유일하게 분해됨을 본다.

<div class="proposition" markdown="1">

<ins id="thm10">**정리 10**</ins> $$\mathfrak{g}$$가 $$0$$이 아닌 유한차원 semisimple Lie algebra이면, $$\mathfrak{g}$$의 simple ideal들 $$\mathfrak{g}_1,\ldots,\mathfrak{g}_r$$이 존재하여

$$\mathfrak{g}=\mathfrak{g}_1\oplus\cdots\oplus\mathfrak{g}_r$$

이고, $$\mathfrak{g}$$의 임의의 simple ideal은 이 $$\mathfrak{g}_i$$ 가운데 하나와 일치한다. 특히 이 직합 분해는 유일하다.

</div>
<details class="proof" markdown="1">
<summary>증명</summary>

$$\dim\mathfrak{g}$$에 대한 귀납법으로 분해의 존재를 보인다. $$\mathfrak{g}$$가 $$0$$이 아닌 proper ideal을 갖지 않으면, $$\mathfrak{g}$$가 semisimple이라 abelian이 아니므로 $$\mathfrak{g}$$ 자신이 simple이고 분해는 자명하다. 그렇지 않으면 $$0$$이 아닌 minimal한 ideal $$\mathfrak{a}\subseteq\mathfrak{g}$$를 택한다.

$$\mathfrak{a}^{\perp}=\{x\in\mathfrak{g}\mid\kappa(x,\mathfrak{a})=0\}$$이라 두면, invariance ([명제 2](#prop2))에 의해 $$\mathfrak{a}^{\perp}$$도 $$\mathfrak{g}$$의 ideal이다. 임의의 $$x\in\mathfrak{a}^{\perp}$$, $$z\in\mathfrak{g}$$, $$a\in\mathfrak{a}$$에 대하여 $$\kappa([z,x],a)=-\kappa(x,[z,a])=0$$이고 $$[z,a]\in\mathfrak{a}$$이기 때문이다. 그럼 $$\mathfrak{a}\cap\mathfrak{a}^{\perp}$$은 ideal이고, 그 위에서 $$\mathfrak{g}$$의 Killing form은 항등적으로 $$0$$이다. [명제 4](#prop4)에 의해 ideal $$\mathfrak{b}=\mathfrak{a}\cap\mathfrak{a}^{\perp}$$의 Killing form $$\kappa_{\mathfrak{b}}$$가 $$\kappa$$의 제한과 같으므로 $$\kappa_{\mathfrak{b}}$$가 항등적으로 $$0$$, 특히 $$\kappa_{\mathfrak{b}}(\mathfrak{b},[\mathfrak{b},\mathfrak{b}])=0$$이고 [따름정리 8](#cor8)에 의해 $$\mathfrak{b}$$는 solvable ideal이다. $$\mathfrak{g}$$가 semisimple이므로 $$\mathfrak{b}=\mathfrak{a}\cap\mathfrak{a}^{\perp}=0$$이다.

$$\kappa$$가 nondegenerate ([정리 9](#thm9))이므로 임의의 ideal $$\mathfrak{a}$$에 대하여 $$\dim\mathfrak{a}+\dim\mathfrak{a}^{\perp}=\dim\mathfrak{g}$$이고, $$\mathfrak{a}\cap\mathfrak{a}^{\perp}=0$$과 합쳐 $$\mathfrak{g}=\mathfrak{a}\oplus\mathfrak{a}^{\perp}$$를 얻는다. 두 ideal $$\mathfrak{a},\mathfrak{a}^{\perp}$$가 직합이므로 $$[\mathfrak{a},\mathfrak{a}^{\perp}]\subseteq\mathfrak{a}\cap\mathfrak{a}^{\perp}=0$$이며, 따라서 $$\mathfrak{a}$$와 $$\mathfrak{a}^{\perp}$$ 안에서의 ideal은 곧 $$\mathfrak{g}$$ 안에서의 ideal이다. 특히 $$\mathfrak{a}$$가 minimal ideal이었으므로 $$\mathfrak{a}$$는 $$0$$이 아닌 proper ideal을 갖지 않고, abelian도 아니므로 ($$\mathfrak{a}$$가 abelian이면 $$\mathfrak{g}$$의 $$0$$이 아닌 solvable ideal이 되어 반단순성에 모순) simple이다. 또 $$\mathfrak{a}^{\perp}$$의 임의의 solvable ideal은 $$\mathfrak{g}$$의 solvable ideal이므로 $$0$$이고, 따라서 $$\mathfrak{a}^{\perp}$$도 semisimple이다. $$\dim\mathfrak{a}^{\perp}<\dim\mathfrak{g}$$이므로 귀납 가정을 $$\mathfrak{a}^{\perp}$$에 적용하면 simple ideal들의 직합 $$\mathfrak{a}^{\perp}=\mathfrak{g}_2\oplus\cdots\oplus\mathfrak{g}_r$$을 얻고, $$\mathfrak{g}_1=\mathfrak{a}$$와 합쳐 원하는 분해 $$\mathfrak{g}=\mathfrak{g}_1\oplus\cdots\oplus\mathfrak{g}_r$$을 얻는다.

유일성을 보인다. $$\mathfrak{g}=\bigoplus_i\mathfrak{g}_i$$가 위 분해이고 $$\mathfrak{b}$$가 $$\mathfrak{g}$$의 임의의 simple ideal이라 하자. $$\mathfrak{b}$$가 ideal이고 각 $$\mathfrak{g}_i$$도 ideal이므로 $$[\mathfrak{b},\mathfrak{g}_i]\subseteq\mathfrak{b}\cap\mathfrak{g}_i$$이다. 만일 모든 $$i$$에 대하여 $$[\mathfrak{b},\mathfrak{g}_i]=0$$이면 $$\mathfrak{b}$$는 $$\mathfrak{g}=\bigoplus_i\mathfrak{g}_i$$ 전체와 commute하여 $$\mathfrak{b}\subseteq Z(\mathfrak{g})=0$$이 되는데 ($$\mathfrak{g}$$가 semisimple이라 $$Z(\mathfrak{g})=0$$), 이는 $$\mathfrak{b}\neq 0$$에 모순이다. 따라서 어떤 $$i$$에 대하여 $$[\mathfrak{b},\mathfrak{g}_i]\neq 0$$이다. 그럼 $$0\neq[\mathfrak{b},\mathfrak{g}_i]\subseteq\mathfrak{b}\cap\mathfrak{g}_i$$이고, $$\mathfrak{b}\cap\mathfrak{g}_i$$가 $$\mathfrak{b}$$와 $$\mathfrak{g}_i$$ 양쪽의 $$0$$이 아닌 ideal이므로 두 simple ideal의 단순성에서 $$\mathfrak{b}\cap\mathfrak{g}_i=\mathfrak{b}=\mathfrak{g}_i$$이다. 곧 $$\mathfrak{b}=\mathfrak{g}_i$$이다. 이로써 모든 simple ideal이 분해의 성분 가운데 하나이며, 따라서 성분 $$\mathfrak{g}_i$$들의 모임은 유일하게 결정된다.

</details>

이 분해에서 각 simple ideal $$\mathfrak{g}_i$$는 그 자체로 simple Lie algebra이고, [§근계, ⁋정의 2](/ko/math/lie_theory/root_systems#def2)에서 도입한 simple과 semisimple의 정의가 여기에서 직합 분해로 정확히 실현된다. 반단순 Lie algebra의 분류가 각 simple 성분의 분류로 환원되는 것이 이 정리의 직접적인 귀결이며, 그 분류는 Cartan subalgebra와 root system을 통해 이루어진다 ([§근계, ⁋정의 4](/ko/math/lie_theory/root_systems#def4)).

---

**참고문헌**

**[Hum]** J. E. Humphreys, *Introduction to Lie algebras and representation theory*, Graduate Texts in Mathematics, Springer, 1972.  
**[Kna]** A. W. Knapp, *Lie groups beyond an introduction*, 2nd ed., Progress in Mathematics, Birkhäuser, 2002.  
**[Bou]** N. Bourbaki, *Lie groups and Lie algebras, Chapters 1–3*, Springer, 1989.  
