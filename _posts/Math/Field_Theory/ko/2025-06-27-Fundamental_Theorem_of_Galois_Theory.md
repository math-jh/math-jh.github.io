---
title: "갈루아 이론의 기본정리"
description: "갈루아 이론의 기본정리를 증명하며, 갈루아 확장의 부분확장과 갈루아 군의 닫힌 부분군 사이의 대응 관계를 다룬다."
excerpt: "Subgroup과 intermediate field 사이의 Galois correspondence"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/fundamental_theorem_of_galois_theory
drift_needed: true
sidebar: 
    nav: "field_theory-ko"

date: 2025-06-27
weight: 10

--- 

## 기본정리의 서술과 응용

우리는 이제 드디어 Galois 이론의 기본정리를 증명한다. 우리는 우선 이를 서술하고, 그 결과들을 살펴본 후 증명을 시작하기로 한다. 

::: 정리 1
Field $\mathbb{K}$의 Galois extension $\mathbb{L}/\mathbb{K}$와 그 Galois group $\Gamma=\Gal(\mathbb{L}/\mathbb{K})$을 생각하자. $\Ext(\mathbb{L}/\mathbb{K})$를 $\mathbb{L}$의 subextension들의 모임이라 하고, $\SubGrp_{\cl}(\Gamma)$를 $\Gamma$의 closed subgroup들의 모임이라 하면 $\Ext(\mathbb{L}/\mathbb{K})$와 $\SubGrp_{\cl}(\Gamma)$ 사이의 두 함수

$$k:\SubGrp_{\cl}(\Gamma)\rightarrow\Ext(\mathbb{L}/\mathbb{K});\qquad G\mapsto k(G)\text{ the field of invariants of $G$}$$

그리고 

$$g:\Ext(\mathbb{L}/\mathbb{K})\rightarrow\SubGrp_{\cl}(\Gamma);\qquad \mathbb{M}\mapsto g(\mathbb{M})\text{ the group of $\mathbb{M}$-automorphisms of $\mathbb{L}$}$$

을 생각하면 이들은 서로의 inverse이다. 
:::

일반적으로 $\mathbb{L}/\mathbb{K}$가 infinite degree Galois extension이라면 위 정리에서 *closed* subgroup인 것이 핵심적인 서술이지만, 만일 $\mathbb{L}/\mathbb{K}$가 finite degree Galois extension이라면 [§갈루아 군의 성질들, ⁋예시 1](/ko/math/field_theory/properties_of_galois_extensions#ex1)에서 살펴본 것과 같이 $\Gal(\mathbb{L}/\mathbb{K})$는 discrete space이고, 따라서 임의의 subgroup이 closed가 되어 이 경우 [정리 1](#thm1)은 subextension들과 subgroup들 사이의 대응이라는 고전적인 Galois 이론의 기본정리가 복원된다. 

::: 명제 2
Finite degree Galois extension $\mathbb{L}/\mathbb{K}$에 대하여 $\lvert\Gal(\mathbb{L}/\mathbb{K})\rvert=[\mathbb{L}:\mathbb{K}]$가 성립한다.
:::
::: 증명
우리의 주장은 $\mathbb{L}$의 $\mathbb{K}$-automorphism들의 집합이 정확히 $\mathbb{L}$에서 $\overline{\mathbb{K}}$로의 $\mathbb{K}$-homomorphism들과 일대일 대응을 이룬다는 것이다. 우선 $\mathbb{L}$의 $\mathbb{K}$-automorphism이 주어졌을 때, 이는 $\mathbb{L}$에서 $\overline{\mathbb{K}}$로 가는 inclusion과 합성하여 $\mathbb{K}$-homomorphism $\mathbb{L} \rightarrow \overline{\mathbb{K}}$를 준다. 거꾸로 $\mathbb{K}$-homomorphism $u:\mathbb{L} \rightarrow \overline{\mathbb{K}}$가 주어졌다 하면, $\mathbb{L}/\mathbb{K}$가 quasi-Galois이므로 [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)의 넷째 조건에 의하여 $u$의 image가 $\mathbb{L}$에 들어가고, 따라서 $u$를 $\mathbb{L}$의 $\mathbb{K}$-endomorphism으로 생각할 수 있다. Field homomorphism은 반드시 단사이며, $\mathbb{L}/\mathbb{K}$가 finite degree이므로 단사인 $\mathbb{K}$-linear endomorphism은 전사이다. ([\[선형대수학\] §동형사상, ⁋정리 7](/ko/math/linear_algebra/isomorphic_vector_spaces#thm7)) 즉 $u$는 $\mathbb{L}$의 $\mathbb{K}$-automorphism이며, 이 대응이 서로의 역임을 쉽게 확인할 수 있다.

따라서 $\lvert\Gal(\mathbb{L}/\mathbb{K})\rvert$는 $\mathbb{L}$에서 $\overline{\mathbb{K}}$로의 $\mathbb{K}$-homomorphism의 개수, 곧 separable degree $[\mathbb{L}:\mathbb{K}]_s$이다. ([§에탈대수, ⁋정의 10](/ko/math/field_theory/etale_algebras#def10)) 그런데 $\mathbb{L}/\mathbb{K}$가 finite degree separable extension이므로 étale algebra이고 ([§분리가능확대체, ⁋정의 8](/ko/math/field_theory/separable_extensions#def8)), 따라서 [§에탈대수, ⁋명제 13](/ko/math/field_theory/etale_algebras#prop13)에 의하여 이 값은 $[\mathbb{L}:\mathbb{K}]$와 같다.
:::

이제 우리는 [정리 1](#thm1)의 구체적인 사용을 살펴본다. 우선 처음 살펴볼 것은 가장 단순한 다음의 예이다. 

::: 예시 3
$\mathbb{L}=\mathbb{Q}(\sqrt{2},\sqrt{3})$이라 하자. 이는 다항식 $(\x^2-2)(\x^2-3)\in\mathbb{Q}[\x]$의 splitting field이므로 [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)의 마지막 조건에 의해 quasi-Galois이다. 한편, [§체, ⁋명제 18](/ko/math/field_theory/fields#prop18)에 의하여 $\mathbb{Q}$의 algebraic extension은 모두 separable이므로 ([§분리가능확대체, ⁋명제 9](/ko/math/field_theory/separable_extensions#prop9)), [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 둘째 조건에 의하여 $\mathbb{L}/\mathbb{Q}$는 Galois extension이다.

우선 $\sqrt{3}\not\in\mathbb{Q}(\sqrt{2})$이다. 만일 $\sqrt{3}=a+b\sqrt{2}$라면 양변을 제곱하여 $3=a^2+2b^2+2ab\sqrt{2}$를 얻는데, $\sqrt{2}$가 유리수가 아니므로 $ab=0$이어야 하고, $b=0$이면 $\sqrt{3}$이, $a=0$이면 $\sqrt{3/2}$가 유리수가 되어 모두 모순이기 때문이다. 따라서 $\mathbb{L}/\mathbb{Q}$는 $\mathbb{Q}(\sqrt{2})$를 intermediate field로 가지고, 따라서 $[\mathbb{L}:\mathbb{Q}]=[\mathbb{L}:\mathbb{Q}(\sqrt{2})][\mathbb{Q}(\sqrt{2}):\mathbb{Q}]=4$이며, [명제 2](#prop2)에 의하여 $\lvert\Gal(\mathbb{L}/\mathbb{Q})\rvert=4$이다.

한편 $\mathbb{L}$은 $f=(\x^2-2)(\x^2-3)$의 해들로 생성되므로, [§갈루아 확장, ⁋정의 12](/ko/math/field_theory/galois_extension#def12) 이후의 논의에 의하여 이 해들의 permutation으로 주어지는 injective homomorphism

$$\Gal(\mathbb{L}/\mathbb{Q})\rightarrow S_4$$

을 얻으며, 그 image는 $f$의 irreducible factor $\x^2-2$와 $x^2-3$의 해집합 $\{\pm\sqrt{2}\}$와 $\{\pm\sqrt{3}\}$의 symmetric group들의 곱에 포함된다. 즉 위 image는 $S_2\times S_2\subset S_4$로 들어가며, 원소 개수를 세 보면 이는 isomorphism이다.

구체적으로, $S_2\times S_2$에서 항등원이 아닌 세 원소는 모두 order $2$이므로 자명하지 않은 proper subgroup은 이들이 각각 생성하는 셋뿐이며, $\Gal(\mathbb{L}/\mathbb{Q})$ 쪽에서 이는 $\sqrt{3}$의 부호만 바꾸는 $\sigma$, $\sqrt{2}$의 부호만 바꾸는 $\tau$, 그리고 $\sigma\tau$가 각각 생성하는 subgroup들이다. 위의 tower $\mathbb{L}/\mathbb{Q}(\sqrt{2})/\mathbb{Q}$로부터 $\{1,\sqrt{2},\sqrt{3},\sqrt{6}\}$이 $\mathbb{L}$의 $\mathbb{Q}$-basis이므로 $x=a+b\sqrt{2}+c\sqrt{3}+d\sqrt{6}$에 대하여

$$\sigma(x)=a+b\sqrt{2}-c\sqrt{3}-d\sqrt{6},\qquad \tau(x)=a-b\sqrt{2}+c\sqrt{3}-d\sqrt{6},\qquad \sigma\tau(x)=a-b\sqrt{2}-c\sqrt{3}+d\sqrt{6}$$

을 얻고, 따라서 세 subgroup의 fixed field는 각각 $\mathbb{Q}(\sqrt{2})$, $\mathbb{Q}(\sqrt{3})$, $\mathbb{Q}(\sqrt{6})$이다. [정리 1](#thm1)에 의하여 이들이 $\mathbb{L}$의 자명하지 않은 subextension 전부이다.
:::

앞의 예시에서는 Galois group이 abelian이라 모든 subgroup이 normal이었다. 다음은 그렇지 않은 가장 작은 예이다.

::: 예시 4
우선 $\alpha=\sqrt[3]{2}$, $\omega=e^{2\pi i/3}$이라 하고 $\mathbb{L}=\mathbb{Q}(\alpha,\omega)$라 하자. 그럼 $\alpha$는 $\x^3-2$의 해이며 $\omega$는 $\x^2+\x+1$의 해이다. 또, $\alpha$만 넣어준 $\mathbb{Q}(\alpha)$는 $\x^3-2$의 splitting field가 될 수 <em-ko>없지만</em-ko>, $\omega$를 함께 넣어주면 $\x^3-2$의 세 해들이 $\alpha$, $\omega\alpha$, $\omega^2\alpha$이므로 $\mathbb{L}=\mathbb{Q}(\alpha,\omega)$은 $\x^3-2$의 splitting field가 된다. 뿐만 아니라, 앞선 예시와 마찬가지 이유로 $\mathbb{L}/\mathbb{Q}$는 Galois extension이다. 

$\x^3-2$는 유리수 해를 갖지 않는 삼차식이므로 $\mathbb{Q}$에서 irreducible이고, 따라서 $[\mathbb{Q}(\alpha):\mathbb{Q}]=3$인데, $\mathbb{Q}(\alpha)$가 $\mathbb{R}$에 포함되어 $\omega$를 포함하지 않으므로 $\mathbb{Q}(\alpha)$ 위에서 $\omega$의 minimal polynomial은 $\x^2+\x+1$이다. 즉 $[\mathbb{L}:\mathbb{Q}]=6$이고 [명제 2](#prop2)에 의하여 $\lvert\Gal(\mathbb{L}/\mathbb{Q})\rvert=6$이다. 한편 $\omega=(\omega\alpha)/\alpha$이므로 $\mathbb{L}$은 정확히 $\x^3-2$의 해들로 생성되고, 따라서 [§갈루아 확장, ⁋정의 12](/ko/math/field_theory/galois_extension#def12) 이후의 논의에서와 같이 해들의 permutation으로 주어지는 injective homomorphism $\Gal(\mathbb{L}/\mathbb{Q})\rightarrow S_3$을 얻는다. 양쪽 모두 여섯 개의 원소를 가지므로 이는 isomorphism이다.

앞서 [예시 3](#ex3)에서 $\Gal(\mathbb{L}/\mathbb{Q})$의 원소가 해들의 집합에 작용하는 방식은 꽤나 자명했는데, 이번 예시의 action은 조금 더 복잡하다. 

이제 이 isomorphism 아래에서 $S_3$의 원소가 세 해에 무엇을 하는지 읽어보자. Order $3$인 원소는 세 해를 순환시키며, 가령 $\alpha\mapsto\omega\alpha\mapsto\omega^2\alpha\mapsto\alpha$인 $\sigma$에 대하여 $\sigma(\omega)=\sigma(\omega\alpha)/\sigma(\alpha)=\omega^2\alpha/(\omega\alpha)=\omega$이므로 $\sigma$는 $\omega$를 고정한다. Order $2$인 원소는 두 해를 맞바꾸고 나머지 하나를 고정하는데, 가령 복소수의 켤레를 취하는 automorphism은 실수인 $\alpha$를 고정하고 $\omega\alpha$와 $\omega^2\alpha$를 맞바꾼다. 따라서 $S_3$의 자명하지 않은 proper subgroup은 order $3$인 원소들이 이루는 $A_3$ 하나와, 각각의 $i$마다 $\omega^i\alpha$를 고정하는 order $2$의 subgroup 셋이다.

그럼 [정리 1](#thm1)에 의하여 이 네 subgroup이 $\mathbb{L}$의 자명하지 않은 subextension 전부와 대응한다. 각각의 subgroup $H$에 대하여 $\mathbb{L}/k(H)$는 Galois extension이고 그 Galois group이 $H$이므로 ([보조정리 7](#lem7)) [명제 2](#prop2)에 의하여 $[\mathbb{L}:k(H)]=\lvert H\rvert$이고, 따라서 $A_3$에는 degree $2$인 subextension이, 나머지 셋에는 degree $3$인 subextension이 대응한다.

위에서 확인한 고정원소로부터 이들을 지목할 수 있다. $A_3$의 원소들이 $\omega$를 고정하므로 $k(A_3)$는 $\mathbb{Q}(\omega)$를 포함하는데, $\omega$의 minimal polynomial이 $\x^2+\x+1$이라 양쪽 모두 $\mathbb{Q}$ 위에서 degree $2$이고 따라서 이들은 같다. 마찬가지로 $\omega^i\alpha$를 고정하는 order $2$의 subgroup의 fixed field는 $\mathbb{Q}(\omega^i\alpha)$를 포함하며, $\omega^i\alpha$가 irreducible polynomial $\x^3-2$의 해이므로 양쪽 모두 degree $3$이 되어 이들도 같다.

한편 $\x^3-2$의 서로 다른 두 해를 함께 포함하는 field는 그 비인 $\omega$ 또는 $\omega^2$를, 따라서 어느 쪽이든 $\omega$를 포함하여 $\mathbb{L}$ 전체가 된다. 그럼 degree $3$인 위의 세 field는 서로 다르며 각각 $\x^3-2$의 해를 하나씩만 포함하므로, [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)의 둘째 조건을 만족하지 않아 $\mathbb{Q}$의 quasi-Galois extension이 아니다. 그럼에도 이들은 $\Gal(\mathbb{L}/\mathbb{Q})$의 원소에 의해 서로 옮겨진다.
:::

이제 [정리 1](#thm1)의 서술에 등장하는 closed 조건이 왜 필요한지를 보여주는 예시를 살펴보자. Galois group이 무한할 때에는 subgroup 전체가 아니라 그중 closed인 것만이 subextension과 대응한다.

::: 예시 5
소수 $p$를 고정하고 $\mathbb{F}_p$의 algebraic closure $\overline{\mathbb{F}}_p$를 생각하자. $\mathbb{F}_p$는 유한집합이므로 perfect이고 ([§체, ⁋명제 18](/ko/math/field_theory/fields#prop18)) 따라서 그 algebraic extension은 모두 separable이다. ([§분리가능확대체, ⁋명제 9](/ko/math/field_theory/separable_extensions#prop9)) 한편 $\overline{\mathbb{F}}_p$는 $\mathbb{F}_p[\x]$의 non-constant polynomial 전체의 splitting field이므로 [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)의 다섯째 조건에 의해 quasi-Galois이고, 즉 $\overline{\mathbb{F}}_p/\mathbb{F}_p$는 Galois extension이다. 그 Galois group을 $\Gamma$라 적자.

$\overline{\mathbb{F}}_p$ 또한 perfect이므로 ([§분리가능차수, ⁋따름정리 3](/ko/math/field_theory/separable_degree#cor3)) Frobenius endomorphism $\varphi:x\mapsto x^p$는 $\overline{\mathbb{F}}_p$의 automorphism이고, $\mathbb{F}_p$의 원소들은 $\x^p-\x$의 해이므로 $\varphi\in\Gamma$이다. 거꾸로 $\varphi(x)=x$인 것은 $x$가 $\x^p-\x$의 해인 것인데, 이 다항식의 해는 많아야 $p$개이고 $\mathbb{F}_p$의 원소 $p$개가 이미 모두 해이다. 따라서 $\varphi$가 생성하는 subgroup $H$에 대하여

$$k(H)=\mathbb{F}_p=k(\Gamma)$$

가 성립한다. 따라서 $H\neq\Gamma$이기만 하면 $k$는 subgroup 전체 위에서 단사가 아니게 된다.

이를 확인하기 위해 각각의 $n\geq1$마다 $\x^{p^n}-\x$의 $\overline{\mathbb{F}}_p$에서의 해들의 집합을 $\mathbb{F}_{p^n}$이라 하자. 이는 $\varphi^n$에 의해 고정되는 원소들의 모임이므로 subfield이고, $\x^{p^n}-\x$의 derivative가 $-1$이라 중근이 없으므로 ([\[환론\] §다항식환, ⁋명제 11](/ko/math/ring_theory/polynomial_rings#prop11)) 원소가 정확히 $p^n$개이다. 그럼 $\mathbb{F}_{p^n}$은 $\mathbb{F}_p$-벡터공간으로서 dimension $n$을 가지므로 $[\mathbb{F}_{p^n}:\mathbb{F}_p]=n$이고, $\x^{p^n}-\x$의 splitting field이므로 quasi-Galois이며, 위에서 본 것과 같이 separable이므로 $\mathbb{F}_{p^n}/\mathbb{F}_p$는 finite degree Galois extension이다. 한편 $\varphi^d$가 $\mathbb{F}_{p^n}$ 위에서 항등함수라면 $p^n$개의 원소가 모두 $\x^{p^d}-\x$의 해가 되어 $n\leq d$이므로, $\varphi\vert_{\mathbb{F}_{p^n}}$의 order는 정확히 $n$이고 [명제 2](#prop2)에 의하여

$$\Gal(\mathbb{F}_{p^n}/\mathbb{F}_p)=\langle\varphi\vert_{\mathbb{F}_{p^n}}\rangle\cong\mathbb{Z}/n\mathbb{Z}$$

이다. 여기서 마지막 isomorphism은 $\varphi\vert_{\mathbb{F}_{p^n}}$을 $1$로 보내는 것이다.

이제 $m\mid n$일 때 $x^{p^m}=x$로부터 $x^{p^{n}}=x$가 따라나오므로 $\mathbb{F}_{p^m}\subseteq\mathbb{F}_{p^n}$이고, 특히 $\mathbb{F}_{p^m}$과 $\mathbb{F}_{p^n}$은 언제나 $\mathbb{F}_{p^{mn}}$에 함께 포함된다. 또 임의의 $x\in\overline{\mathbb{F}}_p$에 대하여 $d=[\mathbb{F}_p(x):\mathbb{F}_p]$라 하면 $\mathbb{F}_p(x)$는 $p^d$개의 원소를 갖는 field이고, 그 가역원들의 group의 order가 $p^d-1$이므로 ([\[대수적 구조\] §몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups#prop5)) $x\neq0$일 때 $x^{p^d-1}=1$이다. $x=0$인 경우와 합치면 언제나 $x^{p^d}=x$, 즉 $x\in\mathbb{F}_{p^d}$이다. 즉 $\overline{\mathbb{F}}_p$는 $\mathbb{F}_{p^n}$들의 union이며, [§갈루아 군의 성질들, ⁋명제 5](/ko/math/field_theory/properties_of_galois_extensions#prop5)를 이 family에 적용하면 restriction들이 유도하는

$$\Gamma\cong\varprojlim_n\Gal(\mathbb{F}_{p^n}/\mathbb{F}_p)\cong\varprojlim_n\mathbb{Z}/n\mathbb{Z}$$

이 topological group들의 isomorphism이다. 여기서 오른쪽의 inverse limit은 $m\mid n$일 때의 reduction map들에 대한 것이고, $\varphi^k$는 각 성분에서 $k$의 residue class로 주어지는 원소에 대응한다.

이제 자연수 $n$을 $n=2^am$ ($m$은 홀수)으로 쓰고, $c_n\in\mathbb{Z}/n\mathbb{Z}$을 $c_n\equiv0\pmod{2^a}$이고 $c_n\equiv1\pmod m$인 유일한 residue class라 하자. 만일 $n'\mid n$이라면 $n'=2^{a'}m'$의 $a'$과 $m'$이 각각 $a'\leq a$와 $m'\mid m$을 만족하므로 $c_n$을 $n'$으로 나눈 나머지가 $c_{n'}$이고, 따라서 $(c_n)_n$은 위의 inverse limit의 원소이다. 만일 이것이 어떤 $\varphi^k$에 대응한다면 $n=2^a$인 성분들로부터 모든 $a$에 대하여 $2^a\mid k$가 되어 $k=0$이어야 하는데, $n=3$인 성분은 $k\equiv1\pmod 3$을 요구하므로 이는 불가능하다. 즉 $(c_n)_n$은 $H$에 속하지 않는 $\Gamma$의 원소이다.

한편 $H$의 closure $\overline{H}$는 다시 subgroup이고, $H\subseteq\overline{H}\subseteq\Gamma$로부터 $k(\overline{H})$가 $k(\Gamma)=\mathbb{F}_p$와 $k(H)=\mathbb{F}_p$ 사이에 놓이므로 $k(\overline{H})=\mathbb{F}_p$이다. 그럼 [정리 1](#thm1)을 closed subgroup $\overline{H}$에 적용하여 $\overline{H}=g(\mathbb{F}_p)=\Gamma$를 얻는다. 즉 $H$는 $\Gamma$에서 dense하지만 closed가 아닌 subgroup이다.
:::

기본정리의 두 번째 부분은 이 대응 하에서 normal subgroup이 무엇에 대응되는지를 알려준다.

::: 따름정리 6
[정리 1](#thm1)의 상황에서, closed subgroup $H\in\SubGrp_{\cl}(\Gamma)$가 $\Gal(\mathbb{L}/\mathbb{K})$의 normal subgroup인 것과 $\mathbb{M}=k(H)$가 $\mathbb{K}$의 Galois extension인 것이 동치이다. 이 경우 restriction은 group isomorphism

$$\Gal(\mathbb{L}/\mathbb{K})/H\cong \Gal(\mathbb{M}/\mathbb{K})$$

을 유도한다.
:::
::: 증명
우선 간단한 계산으로 시작하자. 임의의 closed subgroup $H$와 $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$에 대하여, $x\in \mathbb{L}$이 $\sigma H\sigma^{-1}$의 모든 원소에 의해 고정되는 것은 $\sigma^{-1}(x)$가 $H$의 모든 원소에 의해 고정되는 것과 같으므로

$$\mathbb{L}^{\sigma H\sigma^{-1}}=\sigma(\mathbb{L}^H)=\sigma(\mathbb{M})\tag{$\ast$}$$

이 성립한다.

이제 $H$가 normal subgroup이라 가정하자. 그럼 식 $(\ast)$에 의해 임의의 $\sigma\in\Gal(\mathbb{L}/\mathbb{K})$에 대해 $\sigma(\mathbb{M})=\mathbb{M}$이고, 따라서 restriction $\rho:\Gal(\mathbb{L}/\mathbb{K}) \rightarrow \Aut_\mathbb{K}(\mathbb{M})$이 잘 정의된다. $\mathbb{M}$의 원소 $x$가 $\rho$의 image의 모든 원소에 의해 고정된다면 $x$는 $\Gal(\mathbb{L}/\mathbb{K})$ 전체에 의해 고정되므로, $\mathbb{L}/\mathbb{K}$가 Galois라는 것으로부터 $x\in \mathbb{K}$이다. 특히 $\mathbb{M}$의 모든 $\mathbb{K}$-automorphism들의 group의 invariant들은 $\mathbb{K}$에 포함되고, 따라서 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 첫째 조건에 의하여 $\mathbb{M}/\mathbb{K}$는 Galois extension이다.

거꾸로 $\mathbb{M}/\mathbb{K}$가 Galois extension이라 하자. 그럼 특히 $\mathbb{M}/\mathbb{K}$는 quasi-Galois이므로, [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의하여 임의의 $\sigma\in \Gal(\mathbb{L}/\mathbb{K})$가 $\sigma(\mathbb{M})=\mathbb{M}$을 만족한다. 그럼 식 $(\ast)$과 [정리 1](#thm1)의 대응에 의하여

$$\sigma H\sigma^{-1}=g\bigl(\sigma(\mathbb{M})\bigr)=g(\mathbb{M})=H$$

이므로 $H$는 normal subgroup이다. 여기서 $\sigma H\sigma^{-1}$이 closed인 것은 conjugation이 topological group의 homeomorphism이기 때문이다.

마지막으로 isomorphism을 확인하자. $\mathbb{M}/\mathbb{K}$가 Galois일 때, 위에서 정의한 restriction은 group homomorphism $\rho:\Gal(\mathbb{L}/\mathbb{K}) \rightarrow \Gal(\mathbb{M}/\mathbb{K})$이고, 그 kernel은 $\mathbb{M}$을 고정하는 원소들의 모임, 즉 $g(\mathbb{M})=g(k(H))=H$이다. 한편 $\rho$가 surjective인 것은 [§갈루아 확장, ⁋명제 13](/ko/math/field_theory/galois_extension#prop13)과 같다. 임의의 $\tau\in\Gal(\mathbb{M}/\mathbb{K})$는 [§갈루아 확장, ⁋명제 1](/ko/math/field_theory/galois_extension#prop1)에 의해 $\overline{\mathbb{K}}$의 $\mathbb{K}$-automorphism으로 확장되고, $\mathbb{L}/\mathbb{K}$가 quasi-Galois이므로 이 extension을 $\mathbb{L}$로 제한하면 $\tau$를 확장하는 $\Gal(\mathbb{L}/\mathbb{K})$의 원소를 얻기 때문이다. 따라서 first isomorphism theorem에 의해 $\Gal(\mathbb{L}/\mathbb{K})/H\cong\Gal(\mathbb{M}/\mathbb{K})$이다.
:::

[예시 4](#ex4)의 order $2$인 세 subgroup은 서로 conjugate이므로 normal이 아니며, 실제로 이들에 대응하는 $\mathbb{Q}(\omega^i\alpha)$는 $\mathbb{Q}$의 Galois extension이 아니었다. 반면 $A_3$은 normal subgroup이고 $\mathbb{Q}(\omega)$는 $\x^2+\x+1$의 splitting field로서 $\mathbb{Q}$의 Galois extension이며, 이 경우 [따름정리 6](#cor6)의 isomorphism은 $S_3/A_3\cong\Gal(\mathbb{Q}(\omega)/\mathbb{Q})$이다.

## 기본정리의 증명

[정리 1](#thm1)은 다음과 같이 두 단계로 나누어 증명한다. 

::: 보조정리 7
임의의 subextension $\mathbb{M}\in \Ext(\mathbb{L}/\mathbb{K})$에 대하여, $\mathbb{L}/\mathbb{M}$ 또한 Galois extension이다. 이 때, $\mathbb{M}$-automorphism을 $\mathbb{K}$-automorphism으로 보아 Galois group $\Gal(\mathbb{L}/\mathbb{M})$을 $\Gal(\mathbb{L}/\mathbb{K})$의 subgroup으로 보면, 이는 $\Gal(\mathbb{L}/\mathbb{K})$의 *closed* subgroup이며 따라서 $g$가 잘 정의된다. 
:::
::: 증명
우선 $\mathbb{L}/\mathbb{M}$이 Galois extension임을 보이자. $\mathbb{L}/\mathbb{K}$가 algebraic이므로 $\mathbb{L}/\mathbb{M}$도 algebraic이다. 임의의 $x\in \mathbb{L}$에 대하여, $x$의 $\mathbb{K}$에 대한 minimal polynomial을 $f$, $\mathbb{M}$에 대한 minimal polynomial을 $g$라 하자. $f$는 $\mathbb{M}[\x]$의 원소이기도 하고 $f(x)=0$이므로 $g$는 $f$를 나눈다. ([§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)) 그런데 $\mathbb{L}/\mathbb{K}$가 Galois이므로 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 셋째 조건에 의하여 $f$는 $\mathbb{L}[\x]$에서 서로 다른 일차식들의 곱으로 쪼개지고, 따라서 그 약수인 $g$ 또한 그러하다. 즉 $\mathbb{L}/\mathbb{M}$은 같은 정리의 셋째 조건을 만족하므로 Galois extension이다.

이제 $\Gal(\mathbb{L}/\mathbb{M})$이 closed인 것을 보이자. 집합으로서

$$\Gal(\mathbb{L}/\mathbb{M})=\left\{\sigma\in \Gal(\mathbb{L}/\mathbb{K})\mid \text{$\sigma(x)=x$ for all $x\in \mathbb{M}$}\right\}=\bigcap_{x\in \mathbb{M}}\left\{\sigma\mid \sigma(x)=x\right\}$$

이 성립한다. 그런데 [§갈루아 군의 성질들](/ko/math/field_theory/properties_of_galois_extensions)에서 살펴본 subbase의 표기로 $\{\sigma\mid\sigma(x)=x\}=U_{x,x}\cap\Gal(\mathbb{L}/\mathbb{K})$는 열린집합이고, 그 여집합 또한 열린집합들 $U_{x,y}$ ($y\neq x$)들의 합집합이므로 이들은 모두 clopen이다. 따라서 $\Gal(\mathbb{L}/\mathbb{M})$은 closed set들의 교집합이므로 closed이고, subgroup인 것은 자명하다.
:::

다음 보조정리는 흔히 *Artin의 보조정리*라는 이름으로 불리는 결과로, [정리 1](#thm1)의 증명에서 핵심적인 counting을 제공한다.

::: 보조정리 8 (Artin)
Field $\mathbb{N}$과, $\mathbb{N}$의 automorphism들로 이루어진 유한군 $H$가 주어졌다 하자. $H$의 invariant들의 field를 $\mathbb{N}^H$라 하면, $[\mathbb{N}:\mathbb{N}^H]\leq \lvert H\rvert$가 성립한다.
:::
::: 증명
$\lvert H\rvert=m$이라 하고 $H=\{\sigma_1,\ldots,\sigma_m\}$이라 적자. 여기서 $\sigma_1=\id_\mathbb{N}$이다. 결론에 반하여 $\mathbb{N}^H$ 위에서 일차독립인 원소들 $x_1,\ldots,x_{m+1}\in \mathbb{N}$이 존재한다 가정하자.

다음의 homogeneous 연립일차방정식

$$\sum_{j=1}^{m+1}\sigma_i(x_j)c_j=0,\qquad i=1,\ldots,m$$

을 $\mathbb{N}$ 위에서 미지수 $c_1,\ldots,c_{m+1}$에 대해 생각하자. 이 system은 방정식이 $m$개, 미지수가 $m+1$개이므로 자명하지 않은 해를 갖는다. 만일 그렇지 않다면 $(c_j)\mapsto \bigl(\sum_j \sigma_i(x_j)c_j\bigr)_i$로 정의되는 linear map $\mathbb{N}^{m+1} \rightarrow \mathbb{N}^m$이 injective이고, 그럼 $\mathbb{N}^{m+1}$의 standard basis의 image는 $\mathbb{N}^m$의 일차독립인 $m+1$개의 원소들이 된다. 이를 포함하는 $\mathbb{N}^m$의 basis가 존재하므로 ([\[선형대수학\] §벡터공간의 차원, ⁋명제 5](/ko/math/linear_algebra/dimension#prop5)) $\mathbb{N}^m$은 크기 $m+1$ 이상의 basis를 갖게 되고, 이는 [\[선형대수학\] §벡터공간의 차원, ⁋정리 1](/ko/math/linear_algebra/dimension#thm1)에 모순이기 때문이다.

이제 자명하지 않은 해들 가운데 $0$이 아닌 성분의 개수가 가장 적은 해 $(c_1,\ldots,c_{m+1})$을 택하고, index를 재배열하여 $c_1,\ldots,c_r\neq 0$이고 $c_{r+1}=\cdots=c_{m+1}=0$이라 하자. 해 전체에 $c_r^{-1}$을 곱하여 $c_r=1$로 normalize할 수 있다. 우선 $r\geq 2$인데, $r=1$이라면 $\sigma_1=\id_\mathbb{N}$에 해당하는 방정식이 $x_1c_1=0$이 되어 $c_1=0$이 되기 때문이다.

임의의 $\tau\in H$를 각 방정식에 적용하면

$$\sum_{j=1}^{m+1}(\tau\sigma_i)(x_j)\tau(c_j)=0,\qquad i=1,\ldots,m$$

을 얻는데, $i$가 $1$부터 $m$까지 움직일 때 $\tau\sigma_i$들은 정확히 $H$ 전체를 움직이므로 $(\tau(c_j))_j$ 또한 같은 system의 해이다. 따라서 $(c_j-\tau(c_j))_j$도 해인데, 이 해의 $r$번째 성분은 $c_r-\tau(1)=1-1=0$이고 $r+1$번째 이후의 성분들도 모두 $0$이므로, $0$이 아닌 성분의 개수가 $r$개 미만이다. 그럼 $(c_j)$의 최소성에 의하여 이 해는 자명한 해여야 하고, 즉 모든 $j$와 모든 $\tau\in H$에 대하여 $\tau(c_j)=c_j$이다. 다시 말해 $c_j\in \mathbb{N}^H$이다.

그럼 $\sigma_1=\id_\mathbb{N}$에 해당하는 방정식 $\sum_{j}x_jc_j=0$은 $x_1,\ldots,x_{m+1}$ 사이의 자명하지 않은 $\mathbb{N}^H$-일차결합이 되어, 이들이 $\mathbb{N}^H$ 위에서 일차독립이라는 가정에 모순이다.
:::

이제 [정리 1](#thm1)을 증명할 수 있다.

::: 증명 (정리 1)
[보조정리 7](#lem7)에 의하여 $g$가 잘 정의되고, $k$의 경우 $G$의 원소들이 모두 $\mathbb{K}$를 고정하므로 invariant들의 field $k(G)$는 $\mathbb{K}$를 포함하는 $\mathbb{L}$의 subfield, 곧 $\Ext(\mathbb{L}/\mathbb{K})$의 원소이다.

우선 $k\circ g=\id_{\Ext(\mathbb{L}/\mathbb{K})}$를 보이자. 임의의 $\mathbb{M}\in\Ext(\mathbb{L}/\mathbb{K})$에 대하여 [보조정리 7](#lem7)에 의해 $\mathbb{L}/\mathbb{M}$은 Galois extension이고, 따라서 [§갈루아 확장, ⁋정리 8](/ko/math/field_theory/galois_extension#thm8)의 첫째 조건에 의하여 $\Gal(\mathbb{L}/\mathbb{M})$-invariant element들은 모두 $\mathbb{M}$의 원소이다. 거꾸로 $\mathbb{M}$의 원소들이 $\Gal(\mathbb{L}/\mathbb{M})$에 의해 고정되는 것은 자명하므로 $k(g(\mathbb{M}))=\mathbb{M}$이다.

이제 $g\circ k=\id_{\SubGrp_{\cl}(\Gamma)}$를 보여야 한다. Closed subgroup $G\in\SubGrp_{\cl}(\Gamma)$에 대하여 $\mathbb{M}=k(G)$로 두고 $G'=g(\mathbb{M})=\Gal(\mathbb{L}/\mathbb{M})$이라 하자. $G$의 원소들은 정의에 의해 $\mathbb{M}$을 고정하므로 $G\subseteq G'$이다. 우리의 주장은 $G$가 $G'$에서 dense하다는 것이다.

이를 위해 임의의 $\sigma\in G'$와, $\sigma$의 $\Gal(\mathbb{L}/\mathbb{K})$에서의 기본근방 $U_{\mathbb{M}_0}(\sigma)$가 주어졌다 하자. 여기서 $\mathbb{M}_0$는 $\mathbb{L}/\mathbb{K}$의 finite subextension이다. 그럼 $\mathbb{M}(\mathbb{M}_0)$는 $\mathbb{M}$의 finite degree extension이므로, [§갈루아 확장, ⁋명제 11](/ko/math/field_theory/galois_extension#prop11)을 Galois extension $\mathbb{L}/\mathbb{M}$에 적용하면 $\mathbb{M}(\mathbb{M}_0)$를 포함하는 finite degree Galois subextension $\mathbb{N}/\mathbb{M}$이 존재한다.

$\mathbb{N}/\mathbb{M}$이 quasi-Galois이므로, [§갈루아 확장, ⁋명제 5](/ko/math/field_theory/galois_extension#prop5)에 의하여 임의의 $\tau\in \Gal(\mathbb{L}/\mathbb{M})$은 $\mathbb{N}$을 $\mathbb{N}$으로 보내고, 따라서 restriction homomorphism

$$\rho:\Gal(\mathbb{L}/\mathbb{M}) \rightarrow \Gal(\mathbb{N}/\mathbb{M});\qquad \tau\mapsto \tau\vert_\mathbb{N}$$

이 잘 정의된다. $H=\rho(G)$라 하면 $H$는 $\mathbb{N}$의 automorphism들로 이루어진 유한군이다. 이제 $\mathbb{N}^H$를 계산하면, $x\in \mathbb{N}$이 $H$의 모든 원소에 의해 고정되는 것은 $G$의 모든 원소에 의해 고정되는 것과 같고, 이는 곧 $x\in k(G)=\mathbb{M}$인 것과 같다. 즉 $\mathbb{N}^H=\mathbb{M}$이고, [보조정리 8](#lem8)에 의하여

$$[\mathbb{N}:\mathbb{M}]\leq \lvert H\rvert$$

이다. 한편 $\mathbb{N}/\mathbb{M}$은 finite degree Galois extension이므로 [명제 2](#prop2)에 의하여 $\lvert\Gal(\mathbb{N}/\mathbb{M})\rvert=[\mathbb{N}:\mathbb{M}]$이다. 따라서

$$\lvert H\rvert\leq \lvert\Gal(\mathbb{N}/\mathbb{M})\rvert=[\mathbb{N}:\mathbb{M}]\leq \lvert H\rvert$$

이고, $H\subseteq \Gal(\mathbb{N}/\mathbb{M})$이 같은 크기의 유한집합들이므로 $H=\Gal(\mathbb{N}/\mathbb{M})$이다.

특히 $\sigma\vert_\mathbb{N}\in \Gal(\mathbb{N}/\mathbb{M})=\rho(G)$이므로, $\tau\vert_\mathbb{N}=\sigma\vert_\mathbb{N}$이도록 하는 $\tau\in G$가 존재한다. 그럼 $\mathbb{M}_0\subseteq \mathbb{N}$이므로 $\tau\in U_{\mathbb{M}_0}(\sigma)$이고, 즉 $\sigma$의 임의의 기본근방이 $G$와 만난다. 따라서 $G$는 $G'$에서 dense하고, $G$가 closed라는 가정으로부터 $G=G'$이다. 
:::

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.

---
