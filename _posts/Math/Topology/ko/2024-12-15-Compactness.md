---
title: "옹골성"
description: "위상 공간의 옹골성과 관련된 결과들을 다루며, Tychonoff 정리와 ultrafilter 수렴을 이용한 옹골성의 동치 조건을 증명한다."
excerpt: "ultrafilter 수렴을 이용한 옹골성의 동치와 Tychonoff 정리"

categories: [Math / Topology]
permalink: /ko/math/topology/compactness
sidebar: 
    nav: "topology-ko"

date: 2024-12-15
weight: 16

published: false
drift_needed: true

---

이제 우리는 옹골성과 관련된 남은 결과인 Tychonoff 정리를 살펴본다. 

## Tychonoff theorem

Compact space의 임의의 product는 다시 compact space가 된다. 만일 이 product가 유한이라면 이 결과는 보다 직관적인 방식으로 보일 수 있지만, 이 product가 무한하다면 이를 위해서는 다음 보조정리가 필요하다. 이는 [§옹골성과 필터의 수렴, ⁋명제 5](/ko/math/topology/filter_convergence#prop5)를 filter의 언어로 일반화한 것이다. 

::: 보조정리 1
위상공간 $$X$$가 compact인 것은 임의의 ultrafilter가 수렴하는 것과 동치이다.
:::
::: 증명
우선 $$X$$가 compact라 가정하고, 임의의 ultrafilter $$\mathcal{F}$$가 주어졌다 하자. 결론에 반하여 $$\mathcal{F}$$의 limit point가 존재하지 않는다 하자. 즉, 어떠한 $$x\in X$$에 대해서도 열린근방 $$U_x$$가 존재하여 $$U_x\not\in \mathcal{F}$$이도록 할 수 있다. 그럼 $$X$$의 compactness에 의하여 $$X$$의 유한한 subcover $$U_{x_1},\ldots, U_{x_n}$$이 존재한다. 

한편 [\[집합론\] §필터와 아이디얼, 갈루아 대응, ⁋명제 5](/ko/math/set_theory/filter_and_ideal#prop5)에 의하여 $$\mathcal{F}$$는 prime이다. 즉, 임의의 부분집합 $$A\subseteq X$$에 대하여, $$A\in \mathcal{F}$$ 혹은 $$X\setminus A\in \mathcal{F}$$ 중 정확히 하나가 성립한다. 그럼 이제 임의의 $$A\in \mathcal{F}$$에 대하여,

$$A=A\cap X=(A\cap U_{x_1})\cup \cdots\cup (A\cap U_{x_n})\in \mathcal{F}$$

이며, 가정에 의하여 $$U_{x_i}\not\in \mathcal{F}$$이므로 각각의 $$A\cap U_{x_i}$$들도 $$\mathcal{F}$$에 속하지 않으며 $$\mathcal{F}$$가 maximal이므로 $$X\setminus (A\cap U_{x_i})\in \mathcal{F}$$여야 한다. 그럼 이들의 유한한 교집합

$$X\setminus A=(X\setminus (A\cap U_{x_1}))\cap\cdots\cap (X\setminus (A\cap U_{x_n}))$$

도 $$\mathcal{F}$$에 속해야 하므로, 이는 $$\mathcal{F}$$가 maximal이라는 가정에 모순이다. 

거꾸로 임의의 ultrafilter $$\mathcal{F}$$가 주어질 때마다 limit point $$x$$를 찾을 수 있다 하고, finite intersection property를 만족하는 $$X$$의 닫힌집합들의 family $$\mathcal{A}$$가 주어졌다 하자. 그럼 $$\mathcal{A}$$에 의해 생성되는 filter를 포함하는 ultrafilter $$\mathcal{F}$$를 생각할 수 있으며, 가정에 의해 $$\mathcal{F}$$는 limit point $$x$$를 가진다. 즉 $$\mathcal{N}(x)\subseteq \mathcal{F}$$이며, 따라서 임의의 $$F\in \mathcal{F}$$마다 적당한 $$x$$의 근방 $$U$$가 존재하여 $$U\cap F\neq\emptyset$$이다. 특히 임의의 $$A\in \mathcal{A}$$에 대하여 $$A\cap U\neq\emptyset$$이도록 할 수 있는 $$x$$의 근방 $$U$$가 존재하며, 따라서 $$x\in \cl(A)=A$$가 항상 성립한다. 이로부터 $$x\in\bigcap_{A\in \mathcal{A}}A$$임을 알고, 따라서 [§옹골공간, ⁋명제 11](/ko/math/topology/compact_spaces#prop11)에 의해 원하는 결과를 얻는다.
:::

그럼 다음이 성립한다.

::: 정리 2 (Tychonoff)
Compact space들 $$(X_i)_{i\in I}$$의 product $$X=\prod_{i\in I} X_i$$는 compact이다. 거꾸로, 만일 product space $$X$$가 compact라면, 각각의 $$X_i$$들이 모두 compact이다.
:::
::: 증명
만일 $$X$$가 compact라면, 각각의 $$X_i$$들이 모두 compact라는 것은 $$\pr_i$$의 연속성과 [§옹골공간, ⁋명제 8](/ko/math/topology/compact_spaces#prop8)에 의해 자명하다.

반대 방향은 $$X$$ 위에 정의된 임의의 ultrafilter $$\mathcal{F}$$에 대하여, $$\pr_i(\mathcal{F})$$가 $$X_i$$의 ultrafilter base를 정의한다는 것을 확인한 후, $$X_i$$가 compact라는 가정과 [보조정리 1](#lem1)로부터 이 ultrafilter의 limit point $$x_i$$를 얻고, $$x=(x_i)_{i\in I}$$가 $$\mathcal{F}$$의 limit point임을 보일 수 있으므로 다시 [보조정리 1](#lem1)에 의해 증명이 완료된다. 
:::

## 옹골성의 변주들

옹골성은 여러 방향으로 완화되어 위상수학의 핵심 개념들을 낳는다. 각 점 주위에서만 옹골성을 요구하는 국소적 옹골성과 거기에서 얻어지는 일점 옹골화는 별도의 글에서 다룬다. ([§국소적 옹골공간과 일점 옹골화](/ko/math/topology/locally_compact_spaces)) 또한 유한 부분덮개 대신 국소유한 세분을 허용하여 옹골성을 완화한 paracompactness와 그것이 낳는 단위분할, 그리고 그 응용인 위상다양체는 또 다른 글에서 전개한다. ([§Paracompact 공간과 단위분할](/ko/math/topology/paracompact_spaces))
