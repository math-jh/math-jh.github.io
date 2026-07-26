---
title: "사영공간의 닫힌 부분스킴"
description: "사영공간의 닫힌 부분스킴은 동차 다항식들의 영점집합으로 표현할 수 있으며, 이 성질 덕분에 아핀 스킴과 거의 비슷한 방식으로 다룰 수 있다."
excerpt: "Projective space의 closed subscheme과 homogeneous ideal의 대응"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/closed_subschemes_of_projective_spaces
drift_needed: true
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
weight: 11
published: false

---

이제 우리는 closed subscheme의 예시로 $\mathbb{P}_\mathbb{K}^n$의 closed subscheme들을 살펴본다. $\mathbb{P}^n$은 affine scheme보다는 약간 복잡하지만 그래도 일반적인 scheme보다는 다루기가 편한 대상인데, [§사영스킴, ⁋정의 4](/ko/math/scheme_theory/projective_schemes#def4)에 의하여 $\mathbb{P}^n$의 임의의 닫힌집합은 항상 $\mathbb{K}[\x_0,\ldots, \x_n]$의 homogeneous polynomial들의 zero set으로 쓸 수 있기 때문이다. 즉, 이들 homogeneous polynomial들은, 비록 $\mathbb{P}^n$에서 정의된 함수는 아니지만 적어도 닫힌집합을 표현할 때는 affine scheme과 거의 유사한 방식을 사용할 수 있다.

이번 글에서 우리는 이 대응을 scheme의 단계로 끌어올린다. 즉 homogeneous ideal이 $\mathbb{P}^n$의 closed subscheme을 정의하고, 거꾸로 $\mathbb{P}^n$의 임의의 closed subscheme이 이러한 방식으로 얻어진다는 것을 살펴본다. 이번 글에서 $A_\bullet=\mathbb{K}[\x_0,\ldots,\x_n]$은 표준적인 grading이 주어진 graded ring이고, $\mathbb{P}^n=\Proj A_\bullet$이다.

## $V_+(\mathfrak{a})$의 구성

Affine scheme의 경우 closed subscheme은 정확히 surjection $B \rightarrow B/\mathfrak{a}$들로부터 얻어졌다. ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의) 비록 $\Proj$는 functor가 아니지만 ([§사영스킴](/ko/math/scheme_theory/projective_schemes)), graded ring의 *surjection*은 언제나 $\Proj$들 사이의 morphism을 유도하며, 이것이 위 이야기의 projective 버전이 된다.

::: 명제 1
Homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$과 canonical projection $\pi:A_\bullet \rightarrow A_\bullet/\mathfrak{a}$가 주어졌다 하자. 그럼 $\pi$는 closed embedding

$$\iota:\Proj (A_\bullet/\mathfrak{a}) \rightarrow \Proj A_\bullet=\mathbb{P}^n$$

을 유도하며, 그 image는 $Z_+(\mathfrak{a})$이다.
:::
::: 증명
[\[대수적 구조\] §등급환](/ko/math/algebraic_structures/graded_rings)에서 살펴본 것과 같이 $A_\bullet/\mathfrak{a}$는 graded ring이고, quotient ring의 ideal correspondence는 homogeneous ideal들을 homogeneous ideal들로 대응시킨다. 특히 $\mathfrak{q}\mapsto \pi^{-1}(\mathfrak{q})$는 $\Proj(A_\bullet/\mathfrak{a})$의 점들, 즉 $(A_\bullet/\mathfrak{a})_+$를 포함하지 않는 homogeneous prime ideal들을, $\mathfrak{a}$를 포함하고 $A_+$를 포함하지 않는 $A_\bullet$의 homogeneous prime ideal들로 보내는 bijection이며, 후자는 정확히 $Z_+(\mathfrak{a})$이다. ([§사영스킴, ⁋정의 2](/ko/math/scheme_theory/projective_schemes#def2)) 또, 이 대응 하에서 $Z_+(\bar{\mathfrak{b}})$ 꼴의 닫힌집합은 $Z_+(\pi^{-1}(\bar{\mathfrak{b}}))\cap Z_+(\mathfrak{a})$와 대응되므로 $\iota$는 그 image $Z_+(\mathfrak{a})$로의 homeomorphism이다.

이제 scheme morphism의 구조와 sheaf morphism의 surjectivity를 표준적인 affine cover 위에서 확인하자. 각각의 $i$에 대하여 $\bar{\x}_i=\pi(\x_i)$라 하면, 위의 대응에 의해 $\iota^{-1}(D_+(\x_i))=D_+(\bar{\x}_i)$이다. [§사영스킴, ⁋보조정리 8](/ko/math/scheme_theory/projective_schemes#lem8)의 identification $D_+(\x_i)\cong\Spec A_{(\x_i)}$, $D_+(\bar\x_i)\cong \Spec (A_\bullet/\mathfrak{a})_{(\bar\x_i)}$ 하에서, $\iota$의 restriction은 ring homomorphism

$$A_{(\x_i)} \rightarrow (A_\bullet/\mathfrak{a})_{(\bar\x_i)};\qquad \frac{f}{\x_i^d}\mapsto \frac{\pi(f)}{\bar\x_i^d}$$

이 유도하는 affine scheme들 사이의 morphism이다. $\pi$가 surjective이므로 이 ring homomorphism도 surjective이고, 그 kernel은 localization의 exactness에 의하여

$$\mathfrak{a}_{(\x_i)}=\left\{\frac{a}{\x_i^d}\middle\vert\text{$a\in\mathfrak{a}$ homogeneous of degree $d$}\right\}$$

이다. 즉 $\iota$는 각 chart 위에서 $\Spec\bigl(A_{(\x_i)}/\mathfrak{a}_{(\x_i)}\bigr) \rightarrow \Spec A_{(\x_i)}$ 꼴의 closed embedding이고, 이들은 $D_+(\x_i\x_j)$들 위에서 호환된다. 실제로 [§사영스킴, ⁋보조정리 9](/ko/math/scheme_theory/projective_schemes#lem9)의 identification 하에서 $D_+(\x_i\x_j)$는 $\Spec A_{(\x_i\x_j)}$이고, 위의 ring homomorphism을 $A_{(\x_i)} \rightarrow A_{(\x_i\x_j)}$와 합성한 것은 $f/(\x_i\x_j)^d\mapsto \pi(f)/(\bar\x_i\bar\x_j)^d$로 주어져 $i$와 $j$의 역할에 대해 대칭이기 때문이다. 따라서 $\iota$는 scheme morphism이며, sheaf morphism $\iota^\sharp:\mathcal{O}_{\mathbb{P}^n} \rightarrow \iota_\ast\mathcal{O}_{\Proj(A_\bullet/\mathfrak{a})}$가 cover $(D_+(\x_i))$ 위에서 surjective이므로 stalk들 위에서도 surjective이다. 즉 $\iota$는 closed embedding이다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2))
:::

이렇게 얻어진 closed subscheme을 $V_+(\mathfrak{a})$로 적는다. 즉 $V_+(\mathfrak{a})$는 위상공간으로서는 $Z_+(\mathfrak{a})$이고, scheme으로서는 $\Proj(A_\bullet/\mathfrak{a})$이다. 표기에서 짐작할 수 있듯 이는 affine scheme에서의 대응 $\mathfrak{a}\mapsto \Spec(B/\mathfrak{a})$의 projective 버전이다.

::: 예시 2
양의 degree를 갖는 nonzero homogeneous polynomial $f$가 생성하는 ideal $(f)$에 대하여 $V_+(f)=\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/(f)\bigr)$를 degree $\deg f$의 *hypersurface*라 부른다. $f=0$이면 $V_+(0)=\mathbb{P}^n$이고 $f$가 nonzero 상수이면 $V_+(f)=\emptyset$이므로 이 조건이 필요하다. 가령 $\mathbb{P}^2$에서 $V_+(\x_0\x_2-\x_1^2)$은 conic이다.

한편 $\mathbb{P}^2$의 두 closed subscheme $V_+(\x_0)$과 $V_+(\x_0^2)$을 비교하면, 이들의 underlying space는 $Z_+(\x_0)=Z_+(\x_0^2)$으로 동일하지만 scheme 구조는 다르다. 실제로 chart $D_+(\x_2)\cong\Spec\mathbb{K}[\x_0/\x_2,\x_1/\x_2]$ 위에서 전자는 ideal $(\x_0/\x_2)$로, 후자는 $(\x_0^2/\x_2^2)$로 주어지며 후자의 coordinate ring은 nilpotent element를 갖는다. 이는 [§닫힌 부분스킴, ⁋예시 1](/ko/math/scheme_theory/closed_subschemes#ex1)에서 살펴본 double point와 같은 종류의 non-reduced thickening이다. 다만 $V_+(\x_0^2)$의 ambient space는 $\mathbb{P}^1$이므로 이는 double point가 아니라 double line이다.
:::

## 닫힌 부분스킴의 homogeneous ideal

이제 거꾸로 $\mathbb{P}^n$의 임의의 closed subscheme이 $V_+(\mathfrak{a})$의 꼴임을 보인다.

::: 정리 3
$\mathbb{P}^n$의 임의의 closed subscheme $Z$에 대하여, $Z=V_+(\mathfrak{a})$이도록 하는 homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$이 존재한다.
:::
::: 증명
각각의 $i$에 대하여 $Z\cap D_+(\x_i)$는 affine scheme $D_+(\x_i)\cong\Spec A_{(\x_i)}$의 closed subscheme이므로, [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의에 의하여 유일한 ideal $\mathfrak{b}_i\subseteq A_{(\x_i)}$에 대응된다. 이제 homogeneous element들의 집합

$$T=\left\{f\in A_\bullet\middle\vert\text{$f$ homogeneous,}\quad \frac{f}{\x_i^{\deg f}}\in \mathfrak{b}_i\text{ for all }i\right\}$$

을 생각하고, $\mathfrak{a}$를 $T$로 생성되는 ideal이라 하자. $T$가 homogeneous element들로 이루어져 있으므로 $\mathfrak{a}$는 homogeneous ideal이다. 우리의 주장은 모든 $i$에 대해 $\mathfrak{a}_{(\x_i)}=\mathfrak{b}_i$가 성립한다는 것이다.

우선 $\mathfrak{a}_{(\x_i)}$는 $f/\x_i^{\deg f}$ ($f\in T$) 꼴의 원소들로 생성되는 $A_{(\x_i)}$의 ideal인데, $T$의 정의에 의해 이들 generator가 모두 $\mathfrak{b}_i$에 속하므로 $\mathfrak{a}_{(\x_i)}\subseteq \mathfrak{b}_i$이다.

거꾸로 $g=f/\x_i^d\in \mathfrak{b}_i$가 주어졌다 하자. 여기서 $f$는 degree $d$의 homogeneous polynomial이다. 충분히 큰 $N$에 대하여 $\x_i^Nf\in T$임을 보이면, $g=(\x_i^Nf)/\x_i^{N+d}\in\mathfrak{a}_{(\x_i)}$가 되어 증명이 끝난다. 이를 위해 각각의 $j$에 대하여 $(\x_i^Nf)/\x_j^{N+d}\in \mathfrak{b}_j$이도록 하는 $N$을 찾자. $j=i$인 경우는 임의의 $N$에 대해 성립하므로 $j\neq i$라 하자.

핵심은 $\mathfrak{b}_i$와 $\mathfrak{b}_j$가 교집합 $D_+(\x_i\x_j)$ 위에서 호환된다는 것이다. $Z$의 ideal sheaf $\mathcal{I}_{Z/\mathbb{P}^n}=\ker\iota^\sharp$를 생각하면 ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)), kernel은 section들 위에서 계산되므로 $\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i))=\mathfrak{b}_i$이다. 한편 [§사영스킴, ⁋보조정리 9](/ko/math/scheme_theory/projective_schemes#lem9)에 의하여 $D_+(\x_i\x_j)$는 $\Spec A_{(\x_i)}$의 principal open subset $D(\x_j/\x_i)$이고, affine scheme 위에서 structure sheaf와 $\iota_\ast\mathcal{O}_Z$의 section들은 모두 localization으로 주어지므로, localization의 exactness에 의해

$$\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i\x_j))=(\mathfrak{b}_i)_{\x_j/\x_i}=(\mathfrak{b}_j)_{\x_i/\x_j}$$

이다. 여기서 양변은 모두 $A_{(\x_i\x_j)}$의 ideal이다.

이제 $g\in \mathfrak{b}_i$의 $A_{(\x_i\x_j)}$에서의 image는 $(\mathfrak{b}_j)_{\x_i/\x_j}$에 속한다. 한편 $h=f/\x_j^d\in A_{(\x_j)}$에 대하여 $A_{(\x_i\x_j)}$ 안에서 $h=(\x_i/\x_j)^d g$이므로 $h$의 image도 $(\mathfrak{b}_j)_{\x_i/\x_j}$에 속한다. 즉 적당한 $m_j\geq 0$이 존재하여

$$\left(\frac{\x_i}{\x_j}\right)^{m_j}h=\frac{\x_i^{m_j}f}{\x_j^{m_j+d}}\in \mathfrak{b}_j$$

이다. 그럼 $N=\max_{j\neq i}m_j$로 두면, $\mathfrak{b}_j$가 ideal이므로 모든 $j$에 대하여 $(\x_i^Nf)/\x_j^{N+d}=(\x_i/\x_j)^{N-m_j}\cdot(\x_i^{m_j}f)/\x_j^{m_j+d}\in \mathfrak{b}_j$이고, 따라서 $\x_i^Nf\in T$이다.

종합하면 $Z$와 $V_+(\mathfrak{a})$는 $\mathbb{P}^n$의 closed subscheme으로서 같은 ideal sheaf를 가지므로, [§닫힌 부분스킴, ⁋보조정리 9](/ko/math/scheme_theory/closed_subschemes#lem9)를 양방향으로 적용하면 $Z=V_+(\mathfrak{a})$이다.
:::

Affine의 경우와 달리 이 대응은 일대일이 아니다. 가령 irrelevant ideal $A_+=(\x_0,\ldots,\x_n)$에 대하여 $Z_+(A_+)=\emptyset$이므로 $V_+(A_+)$와 $V_+(A_\bullet)$은 모두 empty scheme이며, 더 일반적으로 두 homogeneous ideal이 충분히 큰 degree에서 일치하면 같은 closed subscheme을 정의한다.

## Saturation

비단사성의 원인은 [명제 1](#prop1)의 증명에 이미 드러나 있다. Chart 위에서 ideal을 계산할 때 $\x_i$의 거듭제곱은 분모로 흡수되므로, $\x_i$를 충분히 곱하면 $\mathfrak{a}$에 들어가는 원소는 $\mathfrak{a}$ 자신의 원소와 같은 정보를 준다. 이러한 원소들을 모두 모아 ideal을 키우면 그 정보만 남는다.

::: 정의 4
Homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$에 대하여, 각 $i$마다 $\x_i^Nf\in \mathfrak{a}$인 $N\geq 0$이 존재하는 $f\in A_\bullet$들의 모임을 $\mathfrak{a}$의 *saturation*이라 부르고 $\mathfrak{a}^{\mathrm{sat}}$으로 적는다. $\mathfrak{a}=\mathfrak{a}^{\mathrm{sat}}$인 homogeneous ideal은 *saturated*라 부른다.
:::

$\mathfrak{a}^{\mathrm{sat}}$이 $\mathfrak{a}$를 포함하는 ideal인 것은 정의에서 곧바로 나온다. 또 $\mathfrak{a}$가 homogeneous이므로 $\x_i^Nf\in \mathfrak{a}$는 $f$의 각 homogeneous component에 대해서도 성립하며, 따라서 $\mathfrak{a}^{\mathrm{sat}}$ 또한 homogeneous ideal이다. 한편 degree가 충분히 큰 monomial은 언제나 어떤 $\x_i^{N_i}$로 나누어떨어지므로, 정의 4의 조건은 적당한 $N$에 대하여 $A_+^Nf\subseteq \mathfrak{a}$인 것과 같다. 곧 $\mathfrak{a}^{\mathrm{sat}}=(\mathfrak{a}:A_+^\infty)$이다.

::: 명제 5
Homogeneous ideal $\mathfrak{a},\mathfrak{b}\subseteq A_\bullet$에 대하여 다음이 성립한다.

1. $V_+(\mathfrak{a})=V_+(\mathfrak{a}^{\mathrm{sat}})$이다.
2. $V_+(\mathfrak{a})=V_+(\mathfrak{b})$인 것과 $\mathfrak{a}^{\mathrm{sat}}=\mathfrak{b}^{\mathrm{sat}}$인 것은 서로 동치이다.

특히 $\mathbb{P}^n$의 closed subscheme들은 saturated homogeneous ideal들과 일대일로 대응한다.
:::
::: 증명
[명제 1](#prop1)의 증명에서 보았듯 $V_+(\mathfrak{a})\cap D_+(\x_i)$는 ideal $\mathfrak{a}_{(\x_i)}\subseteq A_{(\x_i)}$가 결정하고, affine scheme의 closed subscheme은 ideal과 일대일로 대응하므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의), $V_+(\mathfrak{a})=V_+(\mathfrak{b})$인 것은 모든 $i$에 대하여 $\mathfrak{a}_{(\x_i)}=\mathfrak{b}_{(\x_i)}$인 것과 동치이다.

1. $\mathfrak{a}\subseteq \mathfrak{a}^{\mathrm{sat}}$이므로 $\mathfrak{a}_{(\x_i)}\subseteq (\mathfrak{a}^{\mathrm{sat}})_{(\x_i)}$이다. 거꾸로 $f\in \mathfrak{a}^{\mathrm{sat}}$가 degree $d$의 homogeneous element이고 $\x_i^Nf\in \mathfrak{a}$라 하면

    $$\frac{f}{\x_i^d}=\frac{\x_i^Nf}{\x_i^{N+d}}\in \mathfrak{a}_{(\x_i)}$$

    이므로 반대 포함도 성립한다.
2. 한 방향은 1번의 결과이다. 역으로 $V_+(\mathfrak{a})=V_+(\mathfrak{b})$라 하고 $f\in \mathfrak{a}^{\mathrm{sat}}$가 degree $d$의 homogeneous element라 하자. 1번의 계산에 의하여 $f/\x_i^d\in \mathfrak{a}_{(\x_i)}=\mathfrak{b}_{(\x_i)}$이므로, degree $e$의 homogeneous element $g\in \mathfrak{b}$가 존재하여 $A_{(\x_i)}$ 안에서 $f/\x_i^d=g/\x_i^e$이다. $A_\bullet$이 integral domain이라 $A_\bullet \rightarrow A_{\x_i}$가 단사이므로 이는 $\x_i^ef=\x_i^dg\in \mathfrak{b}$를 뜻한다. $i$가 임의였으므로 $f\in \mathfrak{b}^{\mathrm{sat}}$이고, homogeneous component별로 확인하면 $\mathfrak{a}^{\mathrm{sat}}\subseteq \mathfrak{b}^{\mathrm{sat}}$을 얻는다. $\mathfrak{a}$와 $\mathfrak{b}$의 역할을 바꾸면 반대 포함이 나온다.

마지막 주장은 [정리 3](#thm3)과 1번에 의하여 임의의 closed subscheme이 saturated ideal로부터 얻어지고, 2번이 그러한 ideal의 유일성을 주기 때문이다.
:::

[명제 5](#prop5)의 둘째 결과는 $\mathfrak{a}^{\mathrm{sat}}$이 $V_+(\mathfrak{a})$를 정의하는 homogeneous ideal 가운데 가장 큰 것임을 말해준다. $V_+(\mathfrak{b})=V_+(\mathfrak{a})$이면 $\mathfrak{b}\subseteq \mathfrak{b}^{\mathrm{sat}}=\mathfrak{a}^{\mathrm{sat}}$이기 때문이다. 또 이 관점에서 보면 [정리 3](#thm3)의 증명이 만든 ideal은 이미 saturated이다. 그 증명의 $T$는 모든 $i$에 대하여 $f/\x_i^{\deg f}\in \mathfrak{b}_i$인 homogeneous element $f$들의 모임이었고, 위의 계산은 이것이 정확히 $\mathfrak{a}^{\mathrm{sat}}$의 homogeneous element들임을 말해주기 때문이다.

::: 예시 6
$\mathbb{P}^1$에서 $\mathfrak{a}=(\x_0^2,\x_0\x_1)$을 생각하자. $D_+(\x_1)$ 위에서 $\mathfrak{a}_{(\x_1)}$은 $\x_0^2/\x_1^2$과 $\x_0\x_1/\x_1^2=\x_0/\x_1$로 생성되므로 $(\x_0/\x_1)$이고, $D_+(\x_0)$ 위에서는 $\x_0^2/\x_0^2=1$을 포함하므로 $A_{(\x_0)}$ 전체이다. 따라서 $V_+(\mathfrak{a})$는 점 $[0:1]$ 하나로 이루어진 reduced closed subscheme, 곧 $V_+(\x_0)$이다.

이를 saturation으로 다시 읽으면, $\x_0^N\cdot \x_0\in (\x_0^2)$이고 $\x_1^N\cdot \x_0\in (\x_0\x_1)$이므로 $\x_0\in \mathfrak{a}^{\mathrm{sat}}$이다. 거꾸로 $f\in \mathfrak{a}^{\mathrm{sat}}$이면 $\x_1^Nf\in \mathfrak{a}\subseteq (\x_0)$인데 $(\x_0)$가 prime ideal이고 $\x_1\notin (\x_0)$이므로 $f\in (\x_0)$이다. 즉 $\mathfrak{a}^{\mathrm{sat}}=(\x_0)$이며, $\mathfrak{a}$는 이 점을 정의하지만 saturated는 아니다.
:::

## Projective scheme

[§사영스킴](/ko/math/scheme_theory/projective_schemes)에서 우리는 임의의 graded ring $A_\bullet$에 $\Proj$를 취해 scheme을 얻는 방법을 살펴보았지만, 그렇게 얻어지는 scheme들은 우리가 사영공간에서 기대하는 성질을 공유하지 않는다. 가령 $A_\bullet=\mathbb{K}[\x_1,\x_2,\ldots]$이라 두면 $\Proj A_\bullet$은 quasi-compact조차 아니다. 우리가 실제로 다루고 싶은 대상은 사영공간 안에 들어앉는 scheme들이며, 이번 글의 결과는 그러한 scheme들이 정확히 homogeneous ideal로 잘려나오는 것들임을 말해준다. 이제 이를 이름으로 확정한다.

::: 정의 7
Field $\mathbb{K}$ 위의 scheme $X$가 *projective scheme<sub>사영스킴</sub>*이라는 것은 적당한 $n\geq 0$과 closed embedding $X \rightarrow \mathbb{P}^n_\mathbb{K}$이 존재한다는 것이다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2))
:::

[정리 3](#thm3)과 [명제 5](#prop5)에 의하여, $\mathbb{K}$ 위의 projective scheme은 정확히 saturated homogeneous ideal $\mathfrak{a}\subseteq \mathbb{K}[\x_0,\ldots,\x_n]$에 대한 $\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/\mathfrak{a}\bigr)$들이다. 뒤집어 말하면 projective scheme은 degree $1$의 원소들로 생성되는 finitely generated graded $\mathbb{K}$-algebra의 $\Proj$이다. 실제로 그러한 algebra $B_\bullet$의 degree $1$ 부분의 generator $n+1$개를 택하면 surjection $\mathbb{K}[\x_0,\ldots,\x_n] \rightarrow B_\bullet$을 얻고, [명제 1](#prop1)이 이를 closed embedding $\Proj B_\bullet \rightarrow \mathbb{P}^n_\mathbb{K}$으로 옮겨준다.

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

--- 