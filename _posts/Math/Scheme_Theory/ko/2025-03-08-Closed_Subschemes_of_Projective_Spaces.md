---
title: "사영공간의 닫힌 부분스킴"
description: "사영공간의 닫힌 부분스킴은 동차 다항식들의 영점집합으로 표현할 수 있으며, 이 성질 덕분에 아핀 스킴과 거의 비슷한 방식으로 다룰 수 있다."
excerpt: "Projective space의 closed subscheme과 homogeneous ideal의 대응"

categories: [Math / Scheme Theory]
permalink: /ko/math/scheme_theory/closed_subschemes_of_projective_spaces
sidebar: 
    nav: "scheme_theory-ko"

date: 2025-03-08
weight: 11

---

이제 우리는 closed subscheme의 예시로 $\mathbb{P}^n=\mathbb{P}_\mathbb{K}^n$의 closed subscheme들을 살펴본다. $\mathbb{P}^n$은 affine scheme보다는 약간 복잡하지만 그래도 일반적인 scheme보다는 다루기가 편한 대상인데, [§사영공간과 Proj 구성, ⁋정의 4](/ko/math/scheme_theory/projective_schemes#def4)에 의하여 $\mathbb{P}^n$의 임의의 닫힌집합은 항상 $\mathbb{K}[\x_0,\ldots, \x_n]$의 homogeneous polynomial들의 zero set으로 쓸 수 있기 때문이다. 즉, 이들 homogeneous polynomial들은, 비록 $\mathbb{P}^n$에서 정의된 함수는 아니지만 적어도 닫힌집합을 표현할 때는 affine scheme과 거의 유사한 방식을 사용할 수 있다.

이번 글에서 우리는 이 대응을 scheme의 단계로 끌어올린다. 즉 homogeneous ideal이 $\mathbb{P}^n$의 closed subscheme을 정의하고, 거꾸로 $\mathbb{P}^n$의 임의의 closed subscheme이 이러한 방식으로 얻어진다는 것을 살펴본다. 이번 글에서 $A_\bullet=\mathbb{K}[\x_0,\ldots,\x_n]$은 표준적인 grading이 주어진 graded ring이고, $\mathbb{P}^n=\Proj A_\bullet$이다.

## $V_+(\mathfrak{a})$의 구성

우리는 이미 $\Proj$가 functor가 아닌 것을 알고 있다. 이는 graded ring homomorphism $\phi_\bullet:A_\bullet \rightarrow B_\bullet$과 $B_+$를 포함하지 않는 homogeneous prime ideal $\mathfrak{q}$에 대하여 그 inverse image $\phi^{-1}(\mathfrak{q})$가 $A_+$를 포함할 수 있어, $\mathfrak{q}$가 $\Proj B_\bullet$의 점이더라도 $\phi^{-1}(\mathfrak{q})$는 $\Proj A_\bullet$의 점이 아닐 수 있기 때문이었다. 그러나 만일 $\phi_\bullet$이 *surjection*이라면 상황이 달라진다. 이 경우 $\phi(A_+)=B_+$이므로, $\phi^{-1}(\mathfrak{q})$가 $A_+$를 포함하는 것은 $\mathfrak{q}$가 $B_+$를 포함하는 것이며 따라서 $\mathfrak{q}$는 처음부터 $\Proj B_\bullet$의 점이 아니게 되어 문제를 피할 수 있기 때문이다. 한편 affine scheme에서 surjective ring homomorphism은 정확히 closed subscheme을 의미하는 것이었으며 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의) 이는 projective space의 경우에서도 마찬가지이다. 

::: 명제 1
Homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$과 canonical projection $\pi:A_\bullet \rightarrow A_\bullet/\mathfrak{a}$가 주어졌다 하자. 그럼 $\pi$는 closed embedding

$$\iota:\Proj (A_\bullet/\mathfrak{a}) \rightarrow \Proj A_\bullet=\mathbb{P}^n$$

을 유도하며, 그 image는 $Z_+(\mathfrak{a})$이다.
:::
::: 증명
[\[대수적 구조\] §등급환](/ko/math/algebraic_structures/graded_rings)에서 살펴본 것과 같이 $A_\bullet/\mathfrak{a}$는 graded ring이고, quotient ring의 ideal correspondence는 homogeneous ideal들을 homogeneous ideal들로 대응시킨다. 여기에 $\pi$가 surjective이므로 $\pi(A_+)=(A_\bullet/\mathfrak{a})_+$이고, 따라서 $\mathfrak{q}$가 $(A_\bullet/\mathfrak{a})_+$를 포함하지 않는 것과 $\pi^{-1}(\mathfrak{q})$가 $A_+$를 포함하지 않는 것이 서로 동치이다. 특히 $\mathfrak{q}\mapsto \pi^{-1}(\mathfrak{q})$는 $\Proj(A_\bullet/\mathfrak{a})$의 점들, 즉 $(A_\bullet/\mathfrak{a})_+$를 포함하지 않는 homogeneous prime ideal들을, $\mathfrak{a}$를 포함하고 $A_+$를 포함하지 않는 $A_\bullet$의 homogeneous prime ideal들로 보내는 bijection이며, 후자는 정확히 $Z_+(\mathfrak{a})$이다. ([§사영공간과 Proj 구성, ⁋정의 2](/ko/math/scheme_theory/projective_schemes#def2)) 또, 이 대응 하에서 $Z_+(\bar{\mathfrak{b}})$ 꼴의 닫힌집합은 $Z_+(\pi^{-1}(\bar{\mathfrak{b}}))\cap Z_+(\mathfrak{a})$와 대응되므로 $\iota$는 그 image $Z_+(\mathfrak{a})$로의 homeomorphism이다.

이제 scheme morphism의 구조와 sheaf morphism의 surjectivity를 표준적인 affine cover 위에서 확인하자. 각각의 $i$에 대하여 $\bar{\x}_i=\pi(\x_i)$라 하면, 위의 대응에 의해 $\iota^{-1}(D_+(\x_i))=D_+(\bar{\x}_i)$이다. [§사영공간과 Proj 구성, ⁋정리 10](/ko/math/scheme_theory/projective_schemes#thm10)이 $\Proj$에 준 scheme structure의 identification $D_+(\x_i)\cong\Spec A_{(\x_i)}$, $D_+(\bar\x_i)\cong \Spec (A_\bullet/\mathfrak{a})_{(\bar\x_i)}$ 하에서, $\iota$의 restriction은 ring homomorphism

$$A_{(\x_i)} \rightarrow (A_\bullet/\mathfrak{a})_{(\bar\x_i)};\qquad \frac{f}{\x_i^d}\mapsto \frac{\pi(f)}{\bar\x_i^d}$$

이 유도하는 affine scheme들 사이의 morphism이다. $\pi$가 surjective이므로 이 ring homomorphism도 surjective이고, 그 kernel은 localization의 exactness에 의하여

$$\mathfrak{a}_{(\x_i)}=\left\{\frac{a}{\x_i^d}\middle\vert\text{$a\in\mathfrak{a}$ homogeneous of degree $d$}\right\}$$

이다. 즉 $\iota$는 각 chart 위에서 $\Spec\bigl(A_{(\x_i)}/\mathfrak{a}_{(\x_i)}\bigr) \rightarrow \Spec A_{(\x_i)}$ 꼴의 closed embedding이고, 이들은 $D_+(\x_i\x_j)$들 위에서 호환된다. 실제로 [§사영공간과 Proj 구성, ⁋보조정리 9](/ko/math/scheme_theory/projective_schemes#lem9)의 identification 하에서 $D_+(\x_i\x_j)$는 $\Spec A_{(\x_i\x_j)}$이고, 위의 ring homomorphism을 $D_+(\x_i\x_j)$ 위로 더 localize한 $A_{(\x_i\x_j)} \rightarrow (A_\bullet/\mathfrak{a})_{(\bar\x_i\bar\x_j)}$은 $f/(\x_i\x_j)^d\mapsto \pi(f)/(\bar\x_i\bar\x_j)^d$로 주어져 $i$와 $j$의 역할에 대해 대칭이기 때문이다. 따라서 이들은 하나의 scheme morphism $\iota$로 붙는다. 한편 [§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3)의 증명이 보여주듯 closed embedding임은 하나의 affine open cover 위에서 확인하면 충분하므로, $\iota$는 closed embedding이다.
:::

이렇게 얻어진 closed subscheme을 $V_+(\mathfrak{a})$로 적는다. 즉 $V_+(\mathfrak{a})$는 위상공간으로서는 $Z_+(\mathfrak{a})$이고, scheme으로서는 $\Proj(A_\bullet/\mathfrak{a})$이다. 표기에서 짐작할 수 있듯 이는 affine scheme에서의 대응 $\mathfrak{a}\mapsto \Spec(B/\mathfrak{a})$의 projective 버전이다.

::: 예시 2
Positive degree를 갖는 nonzero homogeneous polynomial $f$가 생성하는 ideal $(f)$에 대하여 $V_+(f)=\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/(f)\bigr)$를 degree $\deg f$의 *hypersurface*라 부른다. $f=0$이면 $V_+(0)=\mathbb{P}^n$이고 $f$가 nonzero 상수이면 $V_+(f)=\emptyset$이므로 이 조건이 필요하다. 가령 $\mathbb{P}^2$에서 $V_+(\x_0\x_2-\x_1^2)$은 conic이다.

한편 $\mathbb{P}^2$의 두 closed subscheme $V_+(\x_0)$과 $V_+(\x_0^2)$을 비교하면, 이들의 underlying space는 $Z_+(\x_0)=Z_+(\x_0^2)$으로 동일하지만 scheme 구조는 다르다. 실제로 chart $D_+(\x_2)\cong\Spec\mathbb{K}[\x_0/\x_2,\x_1/\x_2]$ 위에서 전자는 ideal $(\x_0/\x_2)$로, 후자는 $(\x_0^2/\x_2^2)$로 주어지며 후자의 coordinate ring은 nilpotent element를 갖는다. 이는 [§닫힌 부분스킴, ⁋예시 1](/ko/math/scheme_theory/closed_subschemes#ex1)에서 살펴본 double point와 같은 종류의 non-reduced thickening이다. 다만 이 thickening이 얹혀 있는 것은 점이 아니라 직선 $V_+(\x_0)\cong \mathbb{P}^1$이므로 이는 double point가 아니라 double line이다.
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

핵심은 $\mathfrak{b}_i$와 $\mathfrak{b}_j$가 교집합 $D_+(\x_i\x_j)$ 위에서 호환된다는 것이다. $Z$의 ideal sheaf $\mathcal{I}_{Z/\mathbb{P}^n}=\ker\iota^\sharp$를 생각하면 ([§닫힌 부분스킴, ⁋정의 5](/ko/math/scheme_theory/closed_subschemes#def5)), kernel은 section들 위에서 계산되므로 $\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i))=\mathfrak{b}_i$이다. 한편 [§사영공간과 Proj 구성, ⁋보조정리 9](/ko/math/scheme_theory/projective_schemes#lem9)에 의하여 $D_+(\x_i\x_j)$는 $\Spec A_{(\x_i)}$의 principal open subset $D(\x_j/\x_i)$이고, affine scheme 위에서 structure sheaf와 $\iota_\ast\mathcal{O}_Z$의 section들은 모두 localization으로 주어지므로, localization의 exactness에 의해

$$\mathcal{I}_{Z/\mathbb{P}^n}(D_+(\x_i\x_j))=(\mathfrak{b}_i)_{\x_j/\x_i}=(\mathfrak{b}_j)_{\x_i/\x_j}$$

이다. 여기서 양변은 모두 $A_{(\x_i\x_j)}$의 ideal이다.

이제 $g\in \mathfrak{b}_i$의 $A_{(\x_i\x_j)}$에서의 image는 $(\mathfrak{b}_j)_{\x_i/\x_j}$에 속한다. 한편 $h=f/\x_j^d\in A_{(\x_j)}$에 대하여 $A_{(\x_i\x_j)}$ 안에서 $h=(\x_i/\x_j)^d g$이므로 $h$의 image도 $(\mathfrak{b}_j)_{\x_i/\x_j}$에 속한다. 즉 적당한 $m_j\geq 0$이 존재하여

$$\left(\frac{\x_i}{\x_j}\right)^{m_j}h=\frac{\x_i^{m_j}f}{\x_j^{m_j+d}}\in \mathfrak{b}_j$$

이다. 그럼 $N=\max_{j\neq i}m_j$로 두면, $\mathfrak{b}_j$가 ideal이므로 모든 $j$에 대하여 $(\x_i^Nf)/\x_j^{N+d}=(\x_i/\x_j)^{N-m_j}\cdot(\x_i^{m_j}f)/\x_j^{m_j+d}\in \mathfrak{b}_j$이고, 따라서 $\x_i^Nf\in T$이다.

종합하면 $Z$와 $V_+(\mathfrak{a})$는 $\mathbb{P}^n$의 closed subscheme으로서 같은 ideal sheaf를 가지므로, [§닫힌 부분스킴, ⁋보조정리 9](/ko/math/scheme_theory/closed_subschemes#lem9)를 양방향으로 적용하면 서로를 지나는 closed embedding을 얻는다. 그 증명은 이 embedding을 affine open subset $U=\Spec A$ 위에서 두 ideal sheaf의 section이 주는 quotient들 사이의 사상으로 실현하는데, 지금은 그 두 ideal이 같아 이것이 항등사상이므로 얻어진 closed embedding은 isomorphism이고, 따라서 $Z=V_+(\mathfrak{a})$이다.
:::

Affine의 경우와 달리 이 대응은 일대일이 아니다. 가령 임의의 homogeneous ideal $\mathfrak{a}$와 $N\geq 1$에 대하여 $\mathfrak{a}$와 $\mathfrak{a}A_+^N$은 언제나 같은 closed subscheme을 정의한다. 실제로 $V_+(\mathfrak{a})$는 각 chart $D_+(\x_i)$위에서 [명제 1](#prop1)의 증명이 계산한 ideal $\mathfrak{a}_{(\x_i)}$가 결정하는데, 

$$\mathfrak{a}A_+^N\subseteq \mathfrak{a}$$

임은 자명하므로 $(\mathfrak{a}A_+^N)_{(\x_i)}\subseteq \mathfrak{a}_{(\x_i)}$이다. 거꾸로 $\mathfrak{a}_{(\x_i)}$의 원소는 degree $d$의 homogeneous element $f\in \mathfrak{a}$에 대해 $f/\x_i^d$ 꼴인데, 이를 $\x_i^Nf/\x_i^{N+d}$ 꼴로 쓰면 이 원소가 $(\mathfrak{a}A_+^N)_{(\x_i)}$의 원소임을 보일 수 있다. 즉, 모든 $i$에 대하여 $\mathfrak{a}_{(\x_i)}=(\mathfrak{a}A_+^N)_{(\x_i)}$이며 이로부터 위의 대응이 일대일이 아니라는 것을 안다. 

## Saturation

위의 계산에서 드러난 문제는 chart 위에서 ideal을 계산할 때 $\x_i$의 거듭제곱이 분모로 흡수되므로, $\x_i$를 충분히 곱했을 때 $\mathfrak{a}$에 들어가는 원소는 $\mathfrak{a}$ 자신의 원소와 같은 정보를 준다는 것이다. 바꿔 말하면, $\mathfrak{a}$의 각 원소가 chart에서 주는 데이터는, 그 원소에 $\x_i$의 거듭제곱을 곱해 얻은 더 높은 degree의 원소가 이미 알고 있는 것으로, 실제로 만일 두 homogeneous ideal이 충분히 큰 degree에서 일치하면 같은 closed subscheme을 정의한다.

거꾸로 읽으면, degree $d$의 homogeneous element $f$가 $\mathfrak{a}$에 속하지 않더라도 어떤 $N$에 대하여 $\x_i^Nf\in \mathfrak{a}$이기만 하면 $f/\x_i^d=\x_i^Nf/\x_i^{N+d}$는 이미 $\mathfrak{a}_{(\x_i)}$에 속한다. 이러한 $f$는 chart 위에서 $\mathfrak{a}$가 이미 담고 있는 정보이므로, 모든 $i$에 대하여 그러한 $f$들을 전부 모아 ideal을 키워도 각각의 $\mathfrak{a}_{(\x_i)}$는 그대로이고 따라서 closed subscheme도 그대로이다. 

::: 정의 4
Homogeneous ideal $\mathfrak{a}\subseteq A_\bullet$에 대하여, 각 $i$마다 $\x_i^Nf\in \mathfrak{a}$인 $N\geq 0$이 존재하는 $f\in A_\bullet$들의 모임을 $\mathfrak{a}$의 *saturation*이라 부르고 $\mathfrak{a}^\sat$으로 적는다. $\mathfrak{a}=\mathfrak{a}^\sat$인 homogeneous ideal은 *saturated*라 부른다.
:::

그럼 정의에 의해 $\mathfrak{a}^\sat$이 $\mathfrak{a}$를 포함하는 ideal인 것은 자명하다. 또 $\mathfrak{a}$가 homogeneous이므로 $\x_i^Nf\in \mathfrak{a}$는 $f$의 각 homogeneous component에 대해서도 성립하며, 따라서 $\mathfrak{a}^\sat$ 또한 homogeneous ideal이다.

::: 명제 5
Homogeneous ideal $\mathfrak{a},\mathfrak{b}\subseteq A_\bullet$에 대하여 다음이 성립한다.

1. $V_+(\mathfrak{a})=V_+(\mathfrak{a}^\sat)$이다.
2. $V_+(\mathfrak{a})=V_+(\mathfrak{b})$인 것과 $\mathfrak{a}^\sat=\mathfrak{b}^\sat$인 것은 서로 동치이다.

특히 $\mathbb{P}^n$의 closed subscheme들은 saturated homogeneous ideal들과 일대일로 대응한다.
:::
::: 증명
[명제 1](#prop1)의 증명에서 보았듯 $V_+(\mathfrak{a})\cap D_+(\x_i)$는 ideal $\mathfrak{a}_{(\x_i)}\subseteq A_{(\x_i)}$가 결정하고, affine scheme의 closed subscheme은 ideal과 일대일로 대응하므로 ([§닫힌 부분스킴, ⁋명제 3](/ko/math/scheme_theory/closed_subschemes#prop3) 이후의 논의), $V_+(\mathfrak{a})=V_+(\mathfrak{b})$인 것은 모든 $i$에 대하여 $\mathfrak{a}_{(\x_i)}=\mathfrak{b}_{(\x_i)}$인 것과 동치이다.

1. $\mathfrak{a}\subseteq \mathfrak{a}^\sat$이므로 $\mathfrak{a}_{(\x_i)}\subseteq (\mathfrak{a}^\sat)_{(\x_i)}$이다. 거꾸로 $f\in \mathfrak{a}^\sat$가 degree $d$의 homogeneous element이고 $\x_i^Nf\in \mathfrak{a}$라 하면

    $$\frac{f}{\x_i^d}=\frac{\x_i^Nf}{\x_i^{N+d}}\in \mathfrak{a}_{(\x_i)}$$

    이므로 반대 포함도 성립한다.
2. 한 방향은 1번의 결과이다. 역으로 $V_+(\mathfrak{a})=V_+(\mathfrak{b})$라 하고 $f\in \mathfrak{a}^\sat$가 degree $d$의 homogeneous element라 하자. 1번의 계산에 의하여 $f/\x_i^d\in \mathfrak{a}_{(\x_i)}=\mathfrak{b}_{(\x_i)}$이므로, degree $e$의 homogeneous element $g\in \mathfrak{b}$가 존재하여 $A_{(\x_i)}$ 안에서 $f/\x_i^d=g/\x_i^e$이다. $A_\bullet$이 integral domain이라 $A_\bullet \rightarrow A_{\x_i}$가 단사이므로 이는 $\x_i^ef=\x_i^dg\in \mathfrak{b}$를 뜻한다. $i$가 임의였으므로 $f\in \mathfrak{b}^\sat$이고, homogeneous component별로 확인하면 $\mathfrak{a}^\sat\subseteq \mathfrak{b}^\sat$을 얻는다. $\mathfrak{a}$와 $\mathfrak{b}$의 역할을 바꾸면 반대 포함이 나온다.

마지막 주장은 [정리 3](#thm3)에 의하여 임의의 closed subscheme이 $V_+(\mathfrak{a})$의 꼴이고, 1번이 주는 $V_+(\mathfrak{a})=V_+(\mathfrak{a}^\sat)$에 2번을 적용하면 $(\mathfrak{a}^\sat)^\sat=\mathfrak{a}^\sat$, 곧 $\mathfrak{a}^\sat$이 saturated이므로 이것이 saturated ideal로부터 얻어지며, 2번이 그러한 ideal의 유일성 또한 주기 때문이다.
:::

[명제 5](#prop5)의 둘째 결과는 $\mathfrak{a}^\sat$이 $V_+(\mathfrak{a})$를 정의하는 homogeneous ideal 가운데 가장 큰 것임을 말해준다. $V_+(\mathfrak{b})=V_+(\mathfrak{a})$이면 $\mathfrak{b}\subseteq \mathfrak{b}^\sat=\mathfrak{a}^\sat$이기 때문이다. 즉 saturation은 같은 closed subscheme을 정의하는 ideal들 가운데 표준적인 대표를 택하는 연산이고, $\x_i^Nf\in \mathfrak{a}$에서 $N$은 얼마든지 키울 수 있으므로 이 대표는 $\mathfrak{a}$의 충분히 큰 degree 부분만으로 결정된다. 따라서 이 절의 도입부에서 언급했듯, 두 homogeneous ideal이 충분히 큰 degree에서 일치하면 그 saturation이 같고, 따라서 둘은 같은 closed subscheme을 정의한다. 한편 이 관점에서 보면 [정리 3](#thm3)의 증명이 만든 ideal은 이미 saturated인데, 그 증명의 $T$는 모든 $i$에 대하여 $f/\x_i^{\deg f}\in \mathfrak{b}_i$인 homogeneous element $f$들의 모임이었고 위의 계산은 이것이 정확히 $\mathfrak{a}^\sat$의 homogeneous element들임을 말해주기 때문이다.

::: 예시 6
$\mathbb{P}^1$에서 $\mathfrak{a}=(\x_0^2,\x_0\x_1)$을 생각하자. $D_+(\x_1)$ 위에서 $\mathfrak{a}_{(\x_1)}$은 $\x_0^2/\x_1^2$과 $\x_0\x_1/\x_1^2=\x_0/\x_1$로 생성되므로 $(\x_0/\x_1)$이고, $D_+(\x_0)$ 위에서는 $\x_0^2/\x_0^2=1$을 포함하므로 $A_{(\x_0)}$ 전체이다. 따라서 $V_+(\mathfrak{a})$는 점 $[0:1]$ 하나로 이루어진 reduced closed subscheme, 곧 $V_+(\x_0)$이다.

이를 saturation으로 다시 읽으면, $\x_0^N\cdot \x_0\in (\x_0^2)$이고 $\x_1^N\cdot \x_0\in (\x_0\x_1)$이므로 $\x_0\in \mathfrak{a}^\sat$이다. 거꾸로 $f\in \mathfrak{a}^\sat$이면 $\x_1^Nf\in \mathfrak{a}\subseteq (\x_0)$인데 $(\x_0)$가 prime ideal이고 $\x_1\notin (\x_0)$이므로 $f\in (\x_0)$이다. 즉 $\mathfrak{a}^\sat=(\x_0)$이며, $\mathfrak{a}$는 이 점을 정의하지만 saturated는 아니다.

Cone의 언어로 보면 $\mathfrak{a}$가 $\mathbb{A}^2$에서 자르는 것은 직선 $\x_0=0$에 원점에서의 embedded point가 얹힌 scheme이고 ([§스킴의 대수구조, ⁋예시 11](/ko/math/scheme_theory/algebra_of_schemes#ex11)), saturation은 그 성분을 지워 직선만 남긴다. 원점은 $\mathbb{P}^1$의 어느 chart에도 나타나지 않으므로 그 차이가 $V_+(\mathfrak{a})$에서 보이지 않는 것이다.
:::

## Projective scheme

[\[대수다양체\] §사영다양체, ⁋정의 3](/ko/math/algebraic_varieties/projective_varieties#def3)에서 우리는 homogeneous polynomial들이 $\mathbb{P}^n$에서 자르는 닫힌집합을 projective algebraic set이라 부르고, 그 가운데 irreducible한 것을 projective variety라 불렀다. 이번 글의 결과는 이 정의를 scheme의 언어로 올릴 수 있게 해 준다. 

::: 정의 7
Field $\mathbb{K}$ 위의 scheme $X$가 *projective scheme<sub>사영스킴</sub>*이라는 것은 적당한 $n\geq 0$과 closed embedding $X \rightarrow \mathbb{P}^n_\mathbb{K}$이 존재한다는 것이다. ([§닫힌 부분스킴, ⁋정의 2](/ko/math/scheme_theory/closed_subschemes#def2))
:::

[정리 3](#thm3)과 [명제 5](#prop5)에 의하여, 동형을 무시하면 $\mathbb{K}$ 위의 projective scheme은 정확히 saturated homogeneous ideal $\mathfrak{a}\subseteq \mathbb{K}[\x_0,\ldots,\x_n]$에 대한 $\Proj\bigl(\mathbb{K}[\x_0,\ldots,\x_n]/\mathfrak{a}\bigr)$들이다. 뒤집어 말하면 projective scheme은 degree $1$의 원소들로 생성되는 finitely generated graded $\mathbb{K}$-algebra의 $\Proj$이다. 실제로 그러한 algebra $B_\bullet$의 degree $1$ 부분의 generator $n+1$개를 택하면 surjection $\mathbb{K}[\x_0,\ldots,\x_n] \rightarrow B_\bullet$을 얻고, [명제 1](#prop1)이 이를 closed embedding $\Proj B_\bullet \rightarrow \mathbb{P}^n_\mathbb{K}$으로 옮겨준다. 한편 [정의 7](#def7)은 고전적인 정의에서 irreducibility를 떼어낸 것으로, $\mathbb{K}$가 algebraically closed일 때 projective variety에 해당하는 것은 integral한 projective scheme이다. ([§스킴의 대수구조, ⁋정의 1](/ko/math/scheme_theory/algebra_of_schemes#def1))

---

**참고문헌**

**[Har]** R. Hartshorne, *Algebraic geometry*. Graduate texts in mathematics. Springer, 1977.  
**[Vak]** R. Vakil, *The rising sea: Foundation of algebraic geometry*. Available [online](https://math.stanford.edu/~vakil/216blog/).

--- 