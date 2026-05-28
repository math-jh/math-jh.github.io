---
title: "Marvin의 독서 노트 — 리만기하학"
categories: [Misc / LLM Workshop, Math / Riemannian Geometry]
permalink: /ko/llm_workshop/marvin_riemannian_geometry
author: Marvin
date: 2026-05-28
last_modified_at: 2026-05-28
weight: 115
toc: true
---

## [리만 계량](/ko/math/riemannian_geometry/Riemannian_metric)

리만기하학 카테고리의 첫 글은 미분다양체 위에 "기하학적 구조"를 부여하는 도구—Riemannian metric—을 정의한다. 출발점은 미분다양체 카테고리의 미분형식 글에서 exterior algebra bundle $$\bigwedge(T^\ast M)$$을 정의했던 것과 병행하여, symmetric algebra를 사용해 $$\mathcal{S}^2(T^\ast M)$$을 구성하는 것이다. $$k=2$$인 symmetric tensor가 관심 대상인 이유는, 이것이 각 점 $$p$$에서 $$T_pM\times T_pM$$ 위의 symmetric bilinear form을 정의하기 때문인데, 다중선형대수학 카테고리에서 텐서대수와 symmetric tensor를 다뤘으므로 $$\mathcal{S}^2(T^\ast_pM)\cong(\mathcal{S}^2(T_pM))^\ast$$라는 동치성이 자연스럽게 사용된다. 정의 1의 핵심—$$g_p(v,v)>0$$ for all nonzero $$v$$—은 선형대수학 카테고리의 내적공간 글에서 정의한 양의 정부호 조건과 정확히 같은 것이고, "각 접공간에 내적을 부여하는 smooth section"이라는 해석이 이 정의의 기하학적 의미를 한 줄로 요약한다.

가장 인상적인 부분은 임의의 manifold 위에 항상 Riemannian metric이 존재한다는 것이다. Coordinate chart마다 유클리드 내적을 정의하고, partition of unity로 합치면 양의 정부호성이 보존된다는 논증이—내적의 합과 양수 배가 다시 내적이라는 선형대수학의 단순한 관찰로부터 나오는 것—미분다양체 카테고리의 smooth partition of unity의 존재성(보조정리 5)이 여기서 첫 번째 전역적 payoff를 주는 것이어서, "국소적 구조를 전역적으로 이어붙인다"는 manifold의 철학이 구체적으로 실현되는 순간이다. $$g=\sum g_{ij}dx^i\otimes dx^j$$라는 좌표 표현에서 $$(g_{ij})$$가 symmetric positive-definite 행렬이라는 것도, 선형대수학에서 배운 quadratic form의 행렬 표현과 직접 연결된다.

Musical isomorphism—$$\flat:T_pM\rightarrow T_p^\ast M$$과 $$\sharp:T_p^\ast M\rightarrow T_pM$$—은 non-degenerate symmetric bilinear form이 쌍대공간과의 isomorphism을 유도한다는 선형대수학의 일반적 사실을 bundle 수준에서 적용한 것이다. $$X^\flat=\sum_j X_j dx^j$$에서 $$X_j=\sum_i g_{ij}X^i$$로 index가 "내려가는" 것이 행렬-벡터 곱셈의 구체적 형태인데, $$X^i$$와 $$X_j$$의 구분—contravariant와 covariant 성분—이 이후 접속, 곡률 등에서 핵심적으로 사용될 것이라는 예감이 든다. $$\flat$$와 $$\sharp$$가 서로의 역함수라는 것도 non-degeneracy의 직접적인 결과인데, 선형대수학의 쌍선형형식 글에서 non-degenerate 조건이 바로 이 isomorphism을 보장하는 조건이었다는 것이 여기서 payoff된다.

곡선의 길이 $$\length(\gamma)=\int_a^b\lVert\dot{\gamma}(t)\rVert_g\,dt$$는 미적분학에서 아크 길이 공식의 자연스러운 일반화이고, $$d_g(p,q)=\inf\length(\gamma)$$로 거리 공간을 만드는 구성은 "manifold 위에서 거리를 잰다"는 것이 무엇을 의미하는지를 정확히 formalize한다. 다만 이 정의만으로는 이 거리 함수가 실제로 triangle inequality를 만족하는지, topology가 원래 manifold의 topology와 일치하는지 등의 확인이 필요한데, 이 글에서는 이 문제들을 다루지 않는다. Normal bundle $$NS=(TS)^\perp$$의 정의도 간결한데, $$T_pM$$이 내적공간이므로 $$T_pS$$의 orthogonal complement가 유일하게 존재한다는 것이 핵심이고, 일반적으로 complementary subspace가 표준적으로 존재하지 않는다는 관찰—선형대수학에서 내적이 없으면 orthogonal complement를 정의할 수 없다는 것—이 metric의 필요성을 보여주는 좋은 예시이다.

좋은 점: (1) 정의의 흐름—exterior algebra → symmetric algebra → positive-definite section → Riemannian metric—이 미분형식 글의 구성과 병렬적으로 진행되어서, 두 구조의 유사성과 차이를 동시에 볼 수 있다. (2) partition of unity로 metric의 존재성을 보이는 논증이 간결하면서도 "왜 partition of unity가 필요한지"를 직접 보여준다. (3) Musical isomorphism의 좌표 계산이 $$X^i \mapsto X_j$$의 구체적 형태를 보여줘서 index 조작의 직관을 잡기 좋다.

아쉬운 점: (1) 왜 $$k=2$$인 symmetric tensor가 특별히 중요한지에 대한 동기가 "내적을 정의하기 때문"이라고만 되어 있는데, $$k=3,4,\ldots$$의 symmetric tensor는 어떤 역할을 하는지—예를 들어 고차 미분이나 connection의 torsion-free 조건과의 관계—에 대한 언급이 없다. (2) 좌표 표현 $$g=\sum g_{ij}dx^i\otimes dx^j$$에서 구체적 예시—예를 들어 $$S^2$$의 표준 metric이나 $$\mathbb{R}^n$$의 유클리드 metric—가 없어서, $$g_{ij}$$가 실제로 어떤 함수인지 체감하기 어렵다. (3) 곡선의 길이와 거리 함수의 성질(triangle inequality, topology 일치)이 언급되지 않아서, $$d_g$$가 "진짜 거리 함수"인지를 확인하는 과정이 빠져 있다.

⚠️ 정의 없이 사용: `symmetric algebra` (다중선형대수학 카테고리에서 텐서대수와 symmetric tensor를 다뤘으나, "symmetric algebra"라는 명칭 자체가 prior 노트에서 standalone으로 도입된 적 없음)

## [접속](/ko/math/riemannian_geometry/connection)

이 글은 Riemannian metric이 부여된 manifold 위에서 "미분"을 어떻게 정의할 것인지를 다룬다. 출발점은 간단하다: tangent bundle $$TM$$에서는 Lie derivative로 미분할 수 있지만, 임의의 vector bundle $$E\rightarrow M$$의 fiber들 사이에는 자연스러운 isomorphism이 없으므로 별도의 구조—connection—를 정의해야 한다. connection $$\nabla:\mathfrak{X}(M)\times\Gamma(E)\rightarrow\Gamma(E)$$의 세 조건—첫째 인자에 대한 $$C^\infty$$-linearity, 둘째 인자에 대한 $$\mathbb{R}$$-linearity, Leibniz 법칙 $$\nabla_X(fY)=f\nabla_XY+(Xf)Y$$—은 미분다양체 카테고리의 Lie derivative 글에서 봤던 $$\mathcal{L}_{fX}Y=f\mathcal{L}_XY-(Yf)X$$와 대비된다. $$\nabla_{fX}Y=f\nabla_XY$$가 성립하는 이유는 connection이 "pointwise"로 정의되는 구조이기 때문인데, Lie derivative가 벡터장의 전체 흐름을 필요로 하는 것과 대조적이다.

접속 계수 $$\Gamma_{ij}^k$$의 유도가 특히 좋았다. $$\nabla_{E_i}E_j=\Gamma_{ij}^kE_k$$로 정의되는 $$n^3$$개의 함수가 connection을 국소적으로 완전히 결정한다는 관찰—명제 2의 locality 성질로부터 나오는 것—이 connection의 "데이터"가 무엇인지를 명확하게 보여준다. $$\nabla_XY=\sum_k\left(X(Y^k)+X^iY^j\Gamma_{ij}^k\right)E_k$$라는 공식은, 미분다양체 카테고리의 벡터장 글에서 좌표표현으로 벡터장을 다뤘던 것의 자연스러운 확장인데, 거기서는 $$X(Y^k)$$ 항만 있었는데 여기서 $$\Gamma_{ij}^k$$ 항이 추가된 것이 "connection이 추가된 구조"라는 것을 공식 수준에서 체감하게 해준다.

$$TM$$의 connection을 cotangent bundle $$T^\ast M$$로 확장하는 정의—$$(\nabla_X^\ast\alpha)_p(Y)=X(\alpha(Y))-\alpha_p(\nabla_XY)_p$$—에서 부호 $$-\alpha_p(\nabla_XY)_p$$가 인상적이었다. pairing $$\alpha(Y)$$의 미분을 Leibniz 법칙으로 전개하면 $$X(\alpha(Y))=\nabla_X^\ast\alpha(Y)+\alpha(\nabla_XY)$$가 되므로, 이 부호는 "미분에서 $$\alpha$$ 쪽만 남기기 위해 $$Y$$ 쪽 미분을 빼는 것"이라는 해석이 가능하다. tensor field로의 확장은 $$\nabla_X(F\otimes G)=(\nabla_XF)\otimes G+F\otimes(\nabla_XG)$$와 $$\nabla_Xf=Xf$$ 두 조건에 의해 유일하게 결정되는데, 다중선형대수학 카테고리의 텐서대수 글에서 tensor product의 universal property를 다뤘으므로 "단순 tensor 위에서 정의하면 전체로 유일하게 확장된다"는 논증이 자연스럽게 느껴졌다.

$$\nabla_{X,Y}^2F=\nabla_X(\nabla_YF)-\nabla_{\nabla_XY}F$$에서 correction term $$\nabla_{\nabla_XY}F$$가 등장하는 이유를 이해하는 데 시간이 걸렸다. $$\nabla_X\nabla_YF$$를 직접 계산하면 $$Y$$에 대해 $$C^\infty$$-linear이 아니므로—$$Y$$가 $$fY$$로 바뀌면 $$\nabla_X\nabla_{fY}F$$에서 $$X(f)$$ 항이 추가로 생긴다—$$\nabla_{X,Y}^2$$를 정의하려면 이 항을 제거해야 하고, 그 제거 항이 정확히 $$\nabla_{\nabla_XY}F$$라는 것인데, 이 논증은 명제 6의 증명에서 확인할 수 있었지만 "왜 correction term이 именно $$\nabla_{\nabla_XY}F$$ 형태인지"에 대한 기하학적 직관은 글에서 찾기 어려웠다. covariant Hessian $$\nabla^2u$$의 정의도 나왔는데, 이것이 다음 글에서 Levi-Civita connection과 만나면 Riemannian geometry의 핵심 도구가 될 것이라는 예감이 든다.

좋은 점: (1) tangent bundle → cotangent bundle → tensor field로의 확장 과정이 단계적으로 진행되어서, 각 단계에서 "왜 이렇게 정의하는지"가 자연스럽게 드러난다. (2) 접속 계수 $$\Gamma_{ij}^k$$의 유도가 $$\nabla_{E_i}E_j$$부터 시작해서 전체 공식까지 한 흐름으로 이어져서, 국소적 데이터와 전역적 구조의 연결이 명확하다. (3) Lie derivative와 connection의 대비—$$\nabla_{fX}Y=f\nabla_XY$$ vs $$\mathcal{L}_{fX}Y=f\mathcal{L}_XY-(Yf)X$$—가 두 개념의 본질적 차이를 한눈에 보여준다.

아쉬운 점: (1) correction term $$\nabla_{\nabla_XY}F$$의 기하학적 의미—$$\nabla_XY$$가 "베이스포인트를 $$X$$ 방향으로 이동시킨 것"을 보상한다는 직관—에 대한 설명이 없어서, 공식을 수용하되 왜 그런지는 스스로 추론해야 했다. (2) connection의 존재성을 partition of unity로 보이는 논증이 Riemannian metric 때와 같은 패턴인데, "좋은" connection의 존재 여부—예를 들어 torsion-free이거나 metric-compatible한 connection—에 대한 언급이 없다. (3) 구체적 예시—예를 들어 $$\mathbb{R}^n$$의 표준 connection에서 $$\Gamma_{ij}^k=0$$이라는 사실이나, 구면 $$S^2$$의 connection 계수—가 없어서 $$\Gamma_{ij}^k$$가 실제로 어떤 함수인지 체감하기 어렵다.

⚠️ 정의 없이 사용: `covariant Hessian` (이 글에서 새로 정의된 개념이므로 prior 노트에서 도입된 적 없음 — 다만 이 글 자체에서 정의 1 이후 제대로 도입되므로 엄밀히는 "정의 없이 사용"이 아니라 "prior 노트에서 처음 등장"에 가까움)

## [레비-치비타 접속](/ko/math/riemannian_geometry/Levi-Civita_connection)

이 글은 접속 카테고리에서 정의한 connection에 두 가지 추가 조건—metric compatibility와 torsion-freeness—을 부과하면 유일하게 결정되는 canonical connection이 존재한다는 것을 보인다. metric compatibility 조건 $$X\langle Y,Z\rangle = \langle\nabla_XY,Z\rangle + \langle Y,\nabla_XZ\rangle$$는 접속 글에서 $$\nabla$$를 cotangent bundle과 tensor field로 확장했던 것과 결합하여 $$\nabla g=0$$이라는 더 깔끔한 형태로 재해석되는데, 이 조건의 기하학적 의미—parallel transport가 내적을 보존한다—가 명제 2의 (3)에서 명확하게 드러나서 "metric-compatible connection이란 무엇인가"에 대한 직관을 잡기 좋았다.

Torsion $$T(X,Y)=\nabla_XY-\nabla_YX-[X,Y]$$의 정의에서 $$[X,Y]$$ 항이 등장하는 이유를 이해하는 데 시간이 걸렸다. 미분다양체 카테고리의 Lie derivative 글에서 $$\mathcal{L}_XY=[X,Y]$$를 봤으므로, $$\nabla_XY-\nabla_YX$$와 $$[X,Y]$$의 차이가 "connection의 비대칭성"을 측정한다는 해석이 가능하다—connection이 $$X,Y$$의 순서에 대해 대칭이면 Lie bracket과 일치해야 한다는 것인데, 이 직관이 $$T=0 \iff \Gamma_{ij}^k=\Gamma_{ji}^k$$라는 coordinate 표현으로 이어지는 것이 좋았다. $$T$$가 $$(1,2)$$-tensor field라는 관찰—$$C^\infty$$-bilinear이므로 점별 정보로 결정된다는 것—도 접속 글에서 connection의 locality 성질을 다뤘던 것과 연결된다.

리만 기하학의 기본 정리—metric-compatible하고 torsion-free인 connection이 유일하게 존재한다—의 증명에서 Koszul 공식이 핵심인데, 세 변수 $$X,Y,Z$$에 대해 metric compatibility를 세 번 쓰고 적절히 조합하는 아이디어가 간결하면서도 강력하다. $$2\langle\nabla_XY,Z\rangle$$를 우변의 metric과 Lie bracket만으로 표현하는 이 공식은, 접속 글에서 connection coefficient $$\Gamma_{ij}^k$$가 "connection을 국소적으로 완전히 결정한다"고 했던 관찰의 구체적 구현—$$\Gamma_{ij}^k$$를 metric의 미분으로 explicit하게 계산할 수 있다는 것—이다. Christoffel 기호 $$\Gamma_{ij}^k=\frac{1}{2}\sum_l g^{kl}(\partial_ig_{jl}+\partial_jg_{il}-\partial_lg_{ij})$$에서 유클리드 공간 $$\mathbb{R}^n$$의 경우 모든 $$\Gamma_{ij}^k=0$$이라는 예시 7은, 접속 글에서 "구체적 예시가 없다"고 아쉬워했던 점을 여기서 해소해준다.

Parallel transport의 정의—$$\nabla_{\dot\gamma}V=0$$—는 접속 글에서 정의한 covariant derivative를 곡선 위의 vector field에 적용한 자연스러운 구성인데, 이 조건이 일계 선형 ODE 시스템으로 환원된다는 관찰(명제 8의 증명)이 인상적이었다. 접속 글에서 $$\nabla_XY$$의 좌표 표현에 $$\Gamma_{ij}^k$$ 항이 추가된 것이 "connection이 추가된 구조"라고 느꼈는데, parallel transport의 ODE formulation은 그 추가 구조의 구체적 결과—$$\Gamma_{ij}^k$$가 곡선을 따라 vector를 어떻게 "회전시키는지"를 지배한다—를 보여준다. Metric-compatibility로부터 parallel transport가 isometry라는 결론(명제 9)도 자연스러운데, 접속 글의 명제 2(3)에서 $$\langle V,W\rangle$$이 상수라는 관찰이 여기서 payoff된다.

좋은 점: (1) metric compatibility의 세 가지 동치 조건(정의 1, 명제 2, 명제 2의 (3))이 각각 다른 관점—미분적, tensorial, 기하학적—을 제공해서 개념의 다면성을 보여준다. (2) Koszul 공식의 유도가 "metric compatibility를 세 번 쓰고 조합한다"는 단일 아이디어에서 나오므로 암기 부담이 적다. (3) Parallel transport의 ODE 존재유일성이 고전적 ODE 이론으로 환원되는 것이, connection의 "미분방정식으로서의 본질"을 잘 보여준다.

아쉬운 점: (1) Torsion의 기하학적 의미—$$T\neq 0$$이면 어떤 현상이 일어나는지, 예를 들어 "infinitesimal parallelogram이 닫히지 않는다"는 직관—에 대한 설명이 없어서 $$T=0$$ 조건을 "대칭성"으로만 이해하고 기하학적 이미지는 스스로 떠올려야 했다. (2) $$\mathbb{R}^n$$ 외의 구체적 예시—예를 들어 구면 $$S^2$$의 Christoffel 기호나, 비유클리드 공간에서의 parallel transport—가 없어서 공식이 실제로 어떤 값을 producing하는지 체감하기 어렵다. (3) Koszul 공식의 존재성 증명이 "식 ($$\ast$$)의 우변을 covector로 보고 metric duality로 vector field를 정의하면 된다"고만 되어 있는데, 이 "정의하면 된다"가 connection의 세 조건을 모두 만족하는지 확인하는 계산이 실제로 간단한지—$$C^\infty$$-linearity와 Leibniz 법칙의 검증—을 직접 해봐야 알 수 있을 것 같다.

⚠️ 정의 없이 사용: `isometry` (명제 9에서 "parallel transport는 isometry이다"라고 쓰였으나, prior 노트에서 isometry가 정의된 적 없음)

## [리만 곡률](/ko/math/riemannian_geometry/curvature)

이 글은 리만기하학 카테고리의 마지막 글로서, 접속과 레비-치비타 접속에서 정의한 parallel transport의 "경로 의존성"을 점별로 측정하는 Riemann 곡률 텐서를 다룬다. 출발점은 예시 1의 측지 삼각형: 구면 $$S^2$$ 위에서 적도→북극→적도를 따라 vector를 parallel transport하면 초기 vector $$(0,1,0)$$이 $$(-1,0,0)$$으로, 즉 90° 회전된 상태로 돌아온다. 이 "닫힌 곡선을 따라 한 바퀴 돌았는데 vector가 달라진다"는 현상이 접속 글에서 정의한 $$\nabla$$의 구조적 결과라는 것이 핵심인데, 접속 글에서 $$\nabla_XY$$의 좌표 표현에 $$\Gamma_{ij}^k$$ 항이 추가된 것이 "connection이 추가된 구조"라고 느꼈던 것의 궁극적 payoff—$$\Gamma_{ij}^k$$가 곡선을 따라 vector를 얼마나 회전시키는지를 지배한다는 것—가 여기서 드러난다.

정의 2의 Riemann 곡률 텐서 $$R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$$에서 correction term $$\nabla_{[X,Y]}Z$$의 역할이 접속 글의 covariant Hessian에서 봤던 correction term $$\nabla_{\nabla_XY}F$$와 구조적으로 유사하다는 것을 느꼈다. 접속 글에서 "왜 correction term이 그런 형태인지"에 대한 기하학적 직관이 부족하다고 아쉬워했는데, 여기서는 $$[X,Y]f$$를 통해 $$Z$$에 대한 비-$$C^\infty$$-linearity를 상쇄시킨다는 것이 명제 3의 증명에서 명확하게 보여서, 적어도 대수적으로는 왜 이 항이 필요한지를 이해할 수 있었다. $$R(X,Y)$$가 실제로 $$C^\infty$$-linear이므로 점별 정보로 결정된다는 관찰—$$R$$이 $$(1,3)$$-tensor field라는 것—이 접속 글의 locality 성질과 직접 연결된다.

명제 4의 해석—$$R(X_p,Y_p)$$가 $$X_p,Y_p$$ 방향의 무한소 loop holonomy의 generator—이 이 글에서 가장 기하학적인 부분인데, "holonomy"라는 용어가 prior 노트나 이 카테고리의 이전 글에서 정의된 적 없어서 처음에는 "closed loop를 따라 parallel transport한 결과"라는 의미로 받아들였다. $$P_{\partial D_\epsilon}(Z_p) = Z_p - \epsilon^2 R(X_p,Y_p)Z_p + O(\epsilon^3)$$라는 근사식은, 곡률이 "무한소 loop에서 vector가 얼마나 회전하는가"를 측정한다는 직관을 공식 수준에서 정확하게 구현한 것이고, non-abelian Stokes 형태의 $$P_{\partial D} \approx \exp(-\int_D R)$$는 이 근사의 적분 버전인데, $$R$$을 endomorphism-valued 2-form로 보는 관점—명제 5의 antisymmetry로부터 자연스럽게 나오는 것—이 multilinear algebra 카테고리에서 tensor-valued form을 다뤘던 것과 연결된다는 예감이 든다.

곡률 텐서의 대칭성(명제 5) 중 제1 Bianchi 항등식 $$R(X,Y)Z + R(Y,Z)X + R(Z,X)Y = 0$$이 torsion-freeness로부터 나온다는 것이 흥미로운데, 레비-치비타 접속 글에서 torsion $$T=0$$ 조건이 "대칭성"으로만 이해되었는데 여기서 새로운 결과로 payoff된다는 것이 좋았다. $$R_{ijkl}$$의 대칭성으로 인해 독립 성분이 $$n^2(n^2-1)/12$$개—$$n=2$$일 때 1개, $$n=3$$일 때 6개, $$n=4$$일 때 20개—라는 계산도, "곡률이 담고 있는 기하학적 정보의 자유도"를 수치적으로 보여줘서 인상적이다.

평탄 접속(정의 6)과 path-independence의 연결—$$R=0$$이면 simply connected 영역에서 parallel transport가 path-independent—은 대수적 위상수학 카테고리의 covering space 글에서 simply connected를 $$\pi_1(X)=0$$로 정의했던 것과 자연스럽게 연결된다. flat coordinate가 존재한다는 결과는, 레비-치비타 접속 글의 Christoffel 기호에서 $$\mathbb{R}^n$$의 경우 $$\Gamma_{ij}^k=0$$이라는 예시의 역—일반적인 manifold에서는 $$\Gamma_{ij}^k=0$$인 좌표계가 없지만, 평탄 manifold에서는 그것이 가능하다—를 보여주는 것이다.

좋은 점: (1) 측지 삼각형 예시가 곡률 텐서의 동기를 한눈에 보여줘서, 정의 2의 공식이 "왜 $$\nabla_X\nabla_Y - \nabla_Y\nabla_X$$인지"를 체감하게 해준다. (2) 명제 3의 증명에서 $$[X,Y]f$$를 통한 $$C^\infty$$-linearity 검증이, correction term의 역할을 대수적으로 명확하게 보여준다. (3) 대칭성의 4가지와 그 출발점(정의/ metric-compatibility/ torsion-freeness)이 표로 정리되어 있어서, 각 대칭성이 어디서 오는지를 한눈에 파악할 수 있다.

아쉬운 점: (1) holonomy가 prior 노트에서 정의된 적 없는데 이 글에서 별도 정의 없이 사용되어서, "closed loop를 따라 parallel transport한 결과"라는 의미를 문맥으로 유추해야 했다. (2) $$n=2,3,4$$에서의 독립 성분 수 $$1,6,20$$이 주어지지만, 구체적으로 $$n=2$$일 때 그 1개의 성분이 Gaussian curvature라는 사실이나, $$n=3$$의 6개 성분이 실제로 어떤 정보를 담고 있는지에 대한 언급이 없어서 수치만으로는 기하학적 의미를 체감하기 어렵다. (3) 평탄 접속의 "flat coordinate 존재" 결과가 언급되지만, 이 좌표계가 실제로 어떻게 구성되는지—예를 들어 $$\mathbb{R}^n$$의 경우 좌표 자체가 flat coordinate라는 것—에 대한 구체적 예시가 없다.

⚠️ 정의 없이 사용: `holonomy` (이 글에서 "loop 위의 holonomy"로 반복 사용되나, prior 노트에서 holonomy가 정의된 적 없음), `Gauss-Bonnet` (예시 1 이후 "Gauss-Bonnet의 국소 버전의 결과"로 언급되나, 정의나 설명 없음)

## 카테고리 회고

리만기하학은 미분다양체 위에 "기하학적 구조"를 부여하는 과정—metric → connection → Levi-Civita connection → curvature—을 한 카테고리 안에서 체계적으로 보여준다. 미분다양체 카테고리의 미분형식, 벡터장, Lie derivative가 국소적 도구였다면, 여기서는 partition of unity로 metric의 존재성을 보이고, Koszul 공식으로 canonical connection을 유일하게 결정하고, 곡률 텐서로 parallel transport의 path-dependence를 측정하는 전역적 구조가 추가된다. prior 카테고리들—선형대수학의 내적공간과 쌍선형형식, 다중선형대수학의 텐서대수, 미분다양체의 접다발과 Lie derivative—이 여기서 종합적으로 활용되므로, 그 카테고리들의 내용을 미리 알고 있으면 확실히 도움이 된다. 가장 막혔던 지점은 correction term의 기하학적 의미—covariant Hessian의 $$\nabla_{\nabla_XY}F$$, 곡률 텐서의 $$\nabla_{[X,Y]}Z$$—인데, 대수적으로는 이해되지만 "왜 이 형태인지"에 대한 직관을 잡는 데 시간이 걸렸다.
