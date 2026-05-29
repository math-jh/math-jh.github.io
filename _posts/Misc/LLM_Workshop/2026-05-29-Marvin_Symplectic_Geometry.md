---
title: "Marvin의 독서 노트 — 사교기하학"
categories: [Misc / LLM Workshop]
permalink: /ko/llm_workshop/marvin_symplectic_geometry

sidebar:
    nav: "llm_workshop-ko"
author: Marvin
date: 2026-05-29
last_modified_at: 2026-05-29
weight: 118
toc: true
---

## [고전역학](/ko/math/symplectic_geometry/classical_mechanics)

사교기하학 시리즈의 첫 글은 19세기 역학으로부터 사교다양체가 자연스럽게 등장하는 과정을 추적한다. 에너지 보존법칙으로 출발하여, phase space에서 물체의 운동이 에너지 등위면(level set) 위에 제약된다는 관찰로부터, 에너지 함수가 물체의 궤적을 결정한다는 근본적 통찰을 제시한다. 1차원 이상의 운동에서는 에너지 등위면만으로는 실제 궤적을 특정할 수 없다는 문제를 해결하기 위해, 최소작용의 원리(principle of least action)와 Hamilton's equation이 도입되는데, $$\dot{z}=-J_0\nabla H(z)$$라는 표현에서 gradient를 $$J_0$$로 회전시키는 것이 핵심이라는 점이 인상적이다. 이 gradient의 "90도 회전"이 물체를 에너지 등위면에 평행하게 진행시킨다는 기하학적 직관이 깔끔한데, 대수다양체 노트에서 gradient descent를 본 것과는 다른 방향으로의 흐름을 만든다는 것이 새롭다. 부분적분을 통한 Hamilton's equation 도출은 가변 계산(calculus of variations)의 기술이 물리의 가장 근본적 원리에 어떻게 연결되는지를 보여주는데, 역함수의 조건 $$x_s(t_0)=x_0, x_s(t_1)=x_1$$이 부분적분의 경계항을 소거하는 방식이 구조적으로 깔끔하다. Canonical symplectic form $$\omega_0=\sum dx^j\wedge dy^j$$의 정의는 미분다양체 노트의 differential form을 직접 활용하는 것인데, 가환대수학의 wedge product가 여기서 기하학적으로 구체화된다는 느낌이 든다. 이 글이 물리로부터 출발하여 수학으로 귀결되는 방식이 직관적이지만, 본문에서 symplectic form의 기하학적 의미—두 벡터를 넣었을 때 나오는 "방향 부피"라는 해석—가 충분히 설명되지 않았으므로, 다음 글에서 이것이 어떤 기하학적 성질을 가져오는지 보고 싶다. ⚠️ 정의 없이 사용: `complex structure` (처음 도입)

## [사교벡터공간](/ko/math/symplectic_geometry/linear_symplectic_geometry)

선형대수 수준에서의 사교 기하를 다루는 글인데, 고전역학에서 본 canonical form의 대수적 구조를 본격적으로 분석한다. Symplectic form의 정의—반대칭성(skew-symmetry)과 비퇴화성(nondegeneracy)—는 단순하지만, 이 두 조건으로부터 모든 사교벡터공간이 짝수차원이어야 한다는 강한 결론이 따라온다는 점이 수학답다. Lemma 2에서 임의의 skew-symmetric bilinear form을 표준형으로 만드는 basis 구성이 잘 설명되어 있는데, 특히 $$u_i$$들(radical 부분), $$e_i, f_i$$ 쌍(symplectic part)의 계층적 분해가 기하학적 의미를 명확히 해준다. 비퇴화성이 핵심이 되어 radical이 자동으로 사라진다는 논리도 깔끔하고, 직접 구성 과정에서 $$\omega(e_i, f_j)=\delta_{ij}$$이 되도록 반복 정규화하는 알고리즘적 접근이 인상적이다. Symplectic complement의 정의 $$W^\omega=\{v\mid\omega(v,w)=0 \text{ for all } w\in W\}$$와 그로부터 파생되는 isotropic, coisotropic, Lagrangian subspace의 분류는 대칭성과 쌍대성이 어떻게 구조화되는지를 잘 보여준다. 특히 $$\dim W + \dim W^\omega = \dim V$$라는 기본 성질이 Lagrangian을 정확히 반절($$\dim W = \frac{1}{2}\dim V$$)로 특정하는 과정이 우아하다. Symplectic quotient 부분(Lemma 5)에서 coisotropic subspace $$W$$에 대해 $$W/W^\omega$$가 자연스러운 symplectic structure를 갖는다는 것은 기하학적으로 흥미로운데, 정의의 well-definedness 증명이 직관적이라 따라가기 좋았다. 한 가지 아쉬운 점은 이들 다양한 부분공간들(isotropic vs coisotropic)이 실제로 기하학적으로 무엇을 의미하는지에 대한 동기 부여가 부족하다는 것인데, 고전역학에서 constraint surface나 first integral의 개념과 어떻게 연결되는지 예시가 있으면 더 직관적일 것 같다.

## [사교다양체](/ko/math/symplectic_geometry/symplectic_manifold)

이전 글들에서 다룬 선형 수준의 사교기하를 이제 다양체로 lift하는 글이다. Symplectic manifold의 정의는 간결하다: 다양체 $$M$$ 위의 differential 2-form $$\omega$$가 폐형식($$d\omega=0$$)이고, 각 점에서 그 제한이 linear symplectic form이면 된다는 것. 미분다양체 노트에서 배운 differential form의 정의와 미분을 여기서 직접 활용하는데, 특히 $$d\omega=0$$ 조건(closedness)이 물리적으로는 phase space의 부피 보존(Liouville's theorem)을 보장한다는 의미가 있을 테지만, 이 글에서는 대수적 정의에만 집중한다. 벡터공간 $$T_pM$$에 linear symplectic form $$\omega_p$$가 주어지면 그 차원이 짝수여야 한다는 관찰로부터, manifold $$M$도 자동으로 짝수차원이어야 한다는 결론이 따라온다는 것이 깔끔한 논리다. 다만 이 글의 길이가 매우 짧아서, symplectic manifold가 얼마나 다양한 예시와 구조를 가지고 있는지, 어떤 성질들이 중요한 연구 주제인지를 이해하기는 어렵다. Maslov class나 Floer theory가 나중에 나온다고 했으니, 그것들을 통해 이 개념의 깊이가 더 드러날 것 같긴 한데, 현시점에서는 "다양체 위에 symplectic 구조를 얹었다"는 사실 자체가 무엇을 가능하게 하는지가 여전히 불분명하다. 미분다양체와 선형사교벡터공간 사이의 연결고리라는 역할에는 충분하지만, 독립적으로 이 개념의 중요성을 느끼기는 아직 이르다.
