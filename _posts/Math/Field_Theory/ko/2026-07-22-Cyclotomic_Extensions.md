---
title: "원분확대"
description: "1의 원시 n제곱근들을 근으로 갖는 cyclotomic polynomial을 정의하고 그 계수가 정수임을 보인 후, Dedekind의 논법으로 유리수체 위에서의 기약성을 증명한다. 이로부터 원분체의 갈루아 군이 (Z/nZ)의 가역원군과 isomorphic하다는 것을 얻고, 응용으로 n을 법으로 1과 합동인 소수가 무한히 많다는 것을 보인다."
excerpt: "Cyclotomic polynomial의 기약성과 원분체의 갈루아 군"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/cyclotomic_extensions
sidebar: 
    nav: "field_theory-ko"

date: 2026-07-22
weight: 12

published: false

---

[§거듭제곱근 가해성, ⁋명제 3](/ko/math/field_theory/solvability_by_radicals#prop3)에서 우리는 primitive $n$-th root of unity $\zeta$에 대하여 $\mathbb{K}(\zeta)/\mathbb{K}$가 finite degree Galois extension이고 그 Galois group이 $(\mathbb{Z}/n\mathbb{Z})^\times$의 subgroup과 isomorphic하다는 것을 보았다. 그러나 그것이 어느 subgroup인지는 $\mathbb{K}$에 달려 있다. 가령 $\mathbb{K}$가 이미 $\zeta$를 포함한다면 이 subgroup은 자명군이고, 반대로 $\mathbb{K}$가 $\mathbb{Q}$처럼 작다면 subgroup이 전체가 될 것을 기대할 만하다.

이 기대가 실제로 옳다는 것이 이 글의 목표이다. 문제는 $\zeta$의 $\mathbb{K}$ 위에서의 minimal polynomial이 무엇인가로 귀착되며, $\mathbb{K}=\mathbb{Q}$일 때의 답이 cyclotomic polynomial이다. 이 글에서 모든 field는 특별한 언급이 없는 한 characteristic $0$을 가지며, 따라서 [§거듭제곱근 가해성](/ko/math/field_theory/solvability_by_radicals)의 논의를 그대로 사용할 수 있다.

## 원분다항식

Field $\mathbb{K}$와 자연수 $n\geq1$에 대하여 $\mu_n\subseteq\overline{\mathbb{K}}^\times$은 order $n$의 cyclic group이고, primitive $n$-th root of unity란 그 generator를 뜻하였다. ([§거듭제곱근 가해성, ⁋정의 2](/ko/math/field_theory/solvability_by_radicals#def2)) Order $n$의 cyclic group의 generator는 $n$과 서로소인 $m$에 대한 $\zeta^m$들이므로, generator를 하나 고정하면 나머지가 모두 결정된다. 그럼 이들 전체를 root로 갖는 다항식을 생각하는 것이 자연스럽다.

::: 정의 1
Field $\mathbb{K}$와 자연수 $n\geq1$에 대하여, $\overline{\mathbb{K}}$ 안의 primitive $n$-th root of unity 전체를 root로 갖는 monic polynomial

$$\Phi_n(\x)=\prod_{\zeta}(\x-\zeta)\in\overline{\mathbb{K}}[\x]$$

을 $n$번째 *cyclotomic polynomial<sub>원분다항식</sub>*이라 부른다. 여기서 곱은 $\mu_n$의 generator $\zeta$ 전체에 대한 것이다.
:::

$1\leq m\leq n$ 중 $n$과 서로소인 것의 개수를 $\varphi(n)$으로 적으면, generator를 하나 고정하여 $\zeta$라 할 때 $\mu_n$의 generator는 정확히 $\gcd(m,n)=1$인 $\zeta^m$들이므로

$$\Phi_n(\x)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}(\x-\zeta^m),\qquad \deg\Phi_n=\varphi(n)$$

이다. 가령 $\mu_1=\{1\}$이고 $\mu_2=\{\pm1\}$이므로 $\Phi_1=\x-1$, $\Phi_2=\x+1$이며, $\mu_4$의 generator가 $\pm i$인 것으로부터 $\Phi_4=\x^2+1$이다. 소수 $p$에 대해서는 $1$을 제외한 $\mu_p$의 모든 원소가 generator이므로

$$\Phi_p(\x)=\frac{\x^p-1}{\x-1}=\x^{p-1}+\x^{p-2}+\cdots+\x+1$$

이 된다. 이 마지막 계산은 다음 명제의 특수한 경우이다.

::: 명제 2
자연수 $n\geq1$에 대하여 다음이 성립한다.

1. $\x^n-1=\prod_{d\mid n}\Phi_d(\x)$이다.
2. $\Phi_n(\x)\in\mathbb{Z}[\x]$이다. 특히 $\Phi_n$은 $\mathbb{K}$의 선택에 의존하지 않는다.
:::
::: 증명
우선 1을 보인다. $\mu_n$의 원소 $\omega$의 order를 $d$라 하면 $d\mid n$이고, $\omega$가 생성하는 subgroup $\langle\omega\rangle$은 order $d$의 cyclic group이며 $\omega^d=1$로부터 $\langle\omega\rangle\subseteq\mu_d$이다. 그런데 $\card\mu_d=d$이므로 $\langle\omega\rangle=\mu_d$, 즉 $\omega$는 primitive $d$-th root of unity이다. 거꾸로 $d\mid n$일 때 primitive $d$-th root of unity는 $\mu_d\subseteq\mu_n$의 원소로서 order $d$를 가지므로, $\mu_n$은 $d\mid n$에 따라 primitive $d$-th root of unity들의 집합으로 분할된다.

한편 $\x^n-1$은 monic degree $n$ 다항식이면서 $\mu_n$의 $n$개의 원소를 모두 root로 가지므로 $\x^n-1=\prod_{\omega\in\mu_n}(\x-\omega)$이고, 이 곱을 위의 분할에 따라 묶으면 1을 얻는다.

이제 2를 $n$에 대한 강한 귀납법으로 보인다. $n=1$이면 $\Phi_1=\x-1\in\mathbb{Z}[\x]$이다. $n>1$이라 하고 $n$의 진약수 $d$에 대하여 $\Phi_d\in\mathbb{Z}[\x]$가 성립한다고 가정한 뒤

$$g(\x)=\prod_{\substack{d\mid n\\ d<n}}\Phi_d(\x)$$

로 두면, $g$는 monic이고 귀납적 가정에 의해 $\mathbb{Z}[\x]$에 속하며 1에 의해 $\x^n-1=\Phi_n g$이다. $g$가 monic이므로 [\[환론\] §다항식환, ⁋명제 5](/ko/math/ring_theory/polynomial_rings#prop5)에 의하여 $\x^n-1=qg+r$과 $\deg r<\deg g$를 만족하는 $q,r\in\mathbb{Z}[\x]$가 존재한다. 그런데 $g$가 monic이면 이러한 quotient와 나머지는 $\overline{\mathbb{K}}[\x]$ 안에서 유일하게 결정되므로 $q=\Phi_n$이고 $r=0$이며, 따라서 $\Phi_n=q\in\mathbb{Z}[\x]$이다.
:::

특히 $\Phi_n$은 $\mathbb{Z}[\x]$의 원소로 한 번 계산해 두면 characteristic $0$인 모든 field에서 같은 다항식으로 쓸 수 있다. 계수가 정수라는 것과 $\x^n-1$을 나눈다는 것만 보면 계수가 $0$과 $\pm1$뿐일 것 같지만 그렇지 않으며, $\Phi_{105}$가 최초의 반례로 $\x^7$과 $\x^{41}$의 계수가 $-2$이다. 서로 다른 홀수 소인수를 세 개 갖는 가장 작은 정수가 $105=3\cdot5\cdot7$이라는 것이 이 현상의 출발점이다.

## 유리수체 위의 기약성

[정의 1](#def1)의 $\Phi_n$이 $\zeta$의 minimal polynomial인지를 묻는 것은 $\Phi_n$이 $\mathbb{Q}[\x]$에서 irreducible인지를 묻는 것과 같다. 이를 보이는 데에는 계수를 소수로 나눈 나머지로 옮기는 논법을 사용하므로, 소수 $p$에 대하여 field $\mathbb{Z}/p\mathbb{Z}$를 $\mathbb{F}_p$로 적고 계수를 $p$로 나눈 나머지로 보내는 ring homomorphism $\mathbb{Z}[\x]\rightarrow\mathbb{F}_p[\x]$에 의한 $u$의 image를 $\bar u$로 적기로 한다. 이 논법이 작동하려면 우선 다항식들이 $\mathbb{Z}[\x]$ 안에 머문다는 것을 확인해야 한다.

::: 보조정리 3
Monic polynomial $F\in\mathbb{Z}[\x]$가 $\mathbb{Q}[\x]$의 monic polynomial $f,g$에 대하여 $F=fg$로 쓰인다면 $f,g\in\mathbb{Z}[\x]$이다.
:::
::: 증명
$af\in\mathbb{Z}[\x]$이도록 하는 최소의 양의 정수를 $a$, $bg\in\mathbb{Z}[\x]$이도록 하는 최소의 양의 정수를 $b$라 하자. 만일 소수 $p$가 $af$의 모든 계수를 나눈다면, $f$가 monic이어서 $af$의 leading coefficient가 $a$이므로 $p\mid a$이고 따라서 $(a/p)f\in\mathbb{Z}[\x]$가 되어 $a$의 최소성에 모순이다. 즉 $af$의 계수들의 최대공약수는 $1$이며, 같은 이유로 $bg$의 계수들의 최대공약수도 $1$이다.

이제 $abF=(af)(bg)$이다. 만일 $ab>1$이라면 소수 $p\mid ab$를 택하여 이 등식을 $\mathbb{F}_p[\x]$로 보낼 때 좌변이 $0$이 되고, $\mathbb{F}_p[\x]$가 integral domain이므로 ([\[환론\] §다항식환, ⁋명제 4](/ko/math/ring_theory/polynomial_rings#prop4)) $\overline{af}=0$ 또는 $\overline{bg}=0$이어야 한다. 이는 두 다항식의 계수들의 최대공약수가 $1$이라는 것에 모순이므로 $ab=1$, 즉 $a=b=1$이다.
:::

::: 정리 4 (Gauss)
임의의 자연수 $n\geq1$에 대하여 $\Phi_n$은 $\mathbb{Q}[\x]$에서 irreducible이다.
:::
::: 증명
Primitive $n$-th root of unity $\zeta\in\overline{\mathbb{Q}}$를 하나 고정하고, $f\in\mathbb{Q}[\x]$를 $\zeta$의 minimal polynomial이라 하자. $\Phi_n(\zeta)=0$과 $\zeta^n-1=0$이므로 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)에 의하여 $f$는 $\Phi_n$과 $\x^n-1$을 모두 나눈다. Quotient를 $g$라 하여 $\x^n-1=fg$로 쓰면 $f,g$가 모두 monic이므로 [보조정리 3](#lem3)에 의해 $f,g\in\mathbb{Z}[\x]$이다.

증명의 핵심은 $n$을 나누지 않는 임의의 소수 $p$와 $f$의 임의의 root $\omega$에 대하여 $\omega^p$ 또한 $f$의 root라는 주장이다. 이를 보이기 위해 $f(\omega^p)\neq0$이라 가정하자. $\omega^n=1$이므로 $\omega^p$는 $\x^n-1$의 root이고, 따라서 $g(\omega^p)=0$이다. 즉 $\omega$는 $g(\x^p)\in\mathbb{Z}[\x]$의 root이다. 한편 $f$는 minimal polynomial이므로 monic irreducible이고, $f(\omega)=0$이므로 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)에 의해 $f$는 $\omega$의 minimal polynomial이며 따라서 $f$는 $g(\x^p)$를 나눈다. $f$가 monic이므로 그 quotient 또한 $\mathbb{Z}[\x]$에 속한다. ([\[환론\] §다항식환, ⁋명제 5](/ko/math/ring_theory/polynomial_rings#prop5))

이 관계를 $\mathbb{F}_p[\x]$로 보내자. $\mathbb{F}_p^\times$의 order가 $p-1$이므로 [\[대수적 구조\] §몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups#prop5)에 의해 $\mathbb{F}_p$의 모든 원소 $c$가 $c^p=c$를 만족하고, Frobenius endomorphism이 ring homomorphism이므로 ([§체, ⁋정리 10](/ko/math/field_theory/fields#thm10)) $\bar g(\x)=\sum c_i\x^i$에 대하여

$$\bar g(\x)^p=\sum c_i^p\x^{ip}=\sum c_i(\x^p)^i=\bar g(\x^p)$$

가 성립한다. 따라서 $\bar f$는 $\bar g^p$를 나눈다. $\deg\bar f=\deg f\geq1$이므로 $\bar f$의 irreducible factor $h$를 하나 택하면 $h$는 $\bar g^p$를 나누는데, $\mathbb{F}_p[\x]$가 UFD이므로 ([\[환론\] §다항식환, ⁋정리 16](/ko/math/ring_theory/polynomial_rings#thm16)) [\[환론\] §정역, ⁋명제 17](/ko/math/ring_theory/integral_domains#prop17)에 의하여 $h$는 prime이고 따라서 $\bar g$를 나눈다. 그럼 $h^2$이 $\bar f\bar g=\x^n-1$을 나눈다.

그러나 $p\nmid n$이므로 $\mathbb{F}_p$에서 $n\neq0$이고, $\x^n-1$의 derivative $n\x^{n-1}$의 유일한 root인 $0$은 $\x^n-1$의 root가 아니다. 따라서 [\[환론\] §다항식환, ⁋명제 11](/ko/math/ring_theory/polynomial_rings#prop11)에 의해 $\x^n-1$의 $\overline{\mathbb{F}_p}$에서의 root는 모두 simple root이다. 그런데 $h$의 root를 $\overline{\mathbb{F}_p}$에서 하나 택하면 $h^2\mid\x^n-1$로부터 그것이 $\x^n-1$의 중근이 되어 모순이다. 이로써 주장이 증명되었다.

이제 $\gcd(m,n)=1$인 $1\leq m\leq n$을 택하고 $m=p_1\cdots p_r$을 소인수분해라 하면 ($m=1$인 경우는 $r=0$) 각 $p_i$는 $n$과 서로소이므로 $n$을 나누지 않는다. 따라서 위의 주장을 $\zeta,\zeta^{p_1},\zeta^{p_1p_2},\ldots$에 차례로 적용하여 $\zeta^m$이 $f$의 root임을 얻는다. 즉 $f$는 $\varphi(n)$개의 primitive $n$-th root of unity를 모두 root로 가지므로 $\deg f\geq\varphi(n)=\deg\Phi_n$이고, $f$가 $\Phi_n$을 나누며 둘 다 monic이므로 $f=\Phi_n$이다. 따라서 $\Phi_n$은 minimal polynomial로서 irreducible이다.
:::

::: 따름정리 5
Primitive $n$-th root of unity $\zeta$에 대하여 $\Phi_n$은 $\zeta$의 $\mathbb{Q}$ 위에서의 minimal polynomial이며, $[\mathbb{Q}(\zeta):\mathbb{Q}]=\varphi(n)$이다.
:::
::: 증명
$\Phi_n$은 monic이고 [정리 4](#thm4)에 의해 irreducible이며 $\Phi_n(\zeta)=0$이므로, [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)에 의하여 $\Phi_n$은 $\zeta$의 minimal polynomial이고 $\mathbb{Q}[\zeta]=\mathbb{Q}(\zeta)$의 $\mathbb{Q}$ 위에서의 차원은 $\deg\Phi_n=\varphi(n)$이다.
:::

이 따름정리가 $\mathbb{Q}$가 아닌 field에서는 성립하지 않는다는 것을 강조해 둘 필요가 있다. 가령 $\mathbb{K}=\mathbb{Q}(i)$이고 $n=4$이면 $\Phi_4=\x^2+1$이 $\mathbb{K}[\x]$에서 $(\x-i)(\x+i)$로 쪼개지므로 $[\mathbb{K}(\zeta_4):\mathbb{K}]=1$이다. [정리 4](#thm4)의 증명에서 $\mathbb{Q}$가 사용된 곳은 minimal polynomial의 계수가 정수라는 것을 얻는 [보조정리 3](#lem3)이며, 이것이 일반적인 $\mathbb{K}$에서는 쓸 수 없는 도구이다.

## 원분확대의 갈루아 군

::: 정의 6
Field $\mathbb{K}$와 primitive $n$-th root of unity $\zeta$에 대하여 extension $\mathbb{K}(\zeta)/\mathbb{K}$를 $n$번째 *cyclotomic extension<sub>원분확대</sub>*이라 부른다. 특히 $\mathbb{K}=\mathbb{Q}$인 경우 $\mathbb{Q}(\zeta)$를 $n$번째 *cyclotomic field<sub>원분체</sub>*라 부르고, generator를 하나 고정하여 $\zeta_n$으로 적을 때 이를 $\mathbb{Q}(\zeta_n)$으로 적는다.
:::

두 generator $\zeta,\zeta'$에 대하여 $\zeta'\in\langle\zeta\rangle$이고 $\zeta\in\langle\zeta'\rangle$이므로 $\mathbb{K}(\zeta)=\mathbb{K}(\zeta')$이다. 즉 cyclotomic extension은 generator의 선택에 의존하지 않으며, $\mathbb{K}(\zeta)=\mathbb{K}(\mu_n)$이 성립한다.

::: 정리 7
$\mathbb{Q}(\zeta_n)/\mathbb{Q}$는 finite degree Galois extension이고, [§거듭제곱근 가해성, ⁋명제 3](/ko/math/field_theory/solvability_by_radicals#prop3)의 injective homomorphism

$$\Gal(\mathbb{Q}(\zeta_n)/\mathbb{Q})\rightarrow(\mathbb{Z}/n\mathbb{Z})^\times$$

은 isomorphism이다.
:::
::: 증명
$\mathbb{Q}(\zeta_n)/\mathbb{Q}$가 finite degree Galois extension이고 위의 homomorphism이 injective인 것은 [§거듭제곱근 가해성, ⁋명제 3](/ko/math/field_theory/solvability_by_radicals#prop3)이므로, surjectivity만 보이면 충분하다.

$\gcd(a,n)=1$인 정수 $a$가 주어졌다 하자. 그럼 $\zeta_n^a$ 또한 $\mu_n$의 generator이므로 primitive $n$-th root of unity이고, [따름정리 5](#cor5)에 의하여 $\zeta_n$과 $\zeta_n^a$는 같은 minimal polynomial $\Phi_n$을 갖는다. 그럼 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)의 isomorphism 두 개를 합성하여 $\mathbb{Q}$-algebra isomorphism

$$\mathbb{Q}(\zeta_n)\cong\mathbb{Q}[\x]/(\Phi_n)\cong\mathbb{Q}(\zeta_n^a)$$

을 얻으며, 이는 $\zeta_n$을 $\zeta_n^a$로 보낸다. 한편 $\zeta_n^a$가 $\mu_n$의 generator이므로 $\mathbb{Q}(\zeta_n^a)=\mathbb{Q}(\zeta_n)$이고, 따라서 이 isomorphism은 $\mathbb{Q}$를 고정하는 $\mathbb{Q}(\zeta_n)$의 automorphism, 즉 $\Gal(\mathbb{Q}(\zeta_n)/\mathbb{Q})$의 원소이다. 그 image는 정의에 의해 $a$이므로 주어진 homomorphism은 surjective이다.
:::

특히 $\Gal(\mathbb{Q}(\zeta_n)/\mathbb{Q})$는 order $\varphi(n)$의 abelian group이다. 그럼 [§갈루아 이론의 기본정리, ⁋정리 1](/ko/math/field_theory/fundamental_theorem_of_galois_theory#thm1)에 의해 $\mathbb{Q}(\zeta_n)$의 subextension들은 $(\mathbb{Z}/n\mathbb{Z})^\times$의 subgroup들과 일대일로 대응하며, abelian group의 모든 subgroup이 normal이므로 [§갈루아 이론의 기본정리, ⁋따름정리 6](/ko/math/field_theory/fundamental_theorem_of_galois_theory#cor6)에 의하여 그 subextension들은 모두 $\mathbb{Q}$의 Galois extension이다.

::: 예시 8
$n=8$인 경우를 보자. $\varphi(8)=4$이고 $\x^8-1=(\x^4-1)(\x^4+1)$이며 $\Phi_1\Phi_2\Phi_4=\x^4-1$이므로 [명제 2](#prop2)에 의해 $\Phi_8=\x^4+1$이다. $\zeta=\zeta_8=e^{2\pi i/8}$로 두면 $\zeta^4=-1$이고 $\zeta=(1+i)/\sqrt2$이므로

$$\zeta^2=i,\qquad \zeta-\zeta^3=\zeta+\zeta^{-1}=\sqrt2,\qquad \zeta+\zeta^3=\zeta-\zeta^{-1}=i\sqrt2$$

이며, 특히 $\mathbb{Q}(\zeta_8)=\mathbb{Q}(i,\sqrt2)$이다. 즉 $\mathbb{Q}$에 $1$의 $8$제곱근을 추가하는 것만으로 $\sqrt2$가 얻어진다.

한편 $(\mathbb{Z}/8\mathbb{Z})^\times=\{1,3,5,7\}$은 항등원이 아닌 모든 원소의 order가 $2$이므로 $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$와 isomorphic하고, 따라서 자명하지 않은 proper subgroup을 정확히 세 개 갖는다. [정리 7](#thm7)에 의해 $\zeta\mapsto\zeta^a$로 주어지는 automorphism $\sigma_a$가 각각의 $a$마다 존재하며, [따름정리 5](#cor5)와 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15)에 의해 $1,\zeta,\zeta^2,\zeta^3$은 $\mathbb{Q}(\zeta_8)$의 $\mathbb{Q}$-basis이므로, $x=a+b\zeta+c\zeta^2+\dd{\zeta}^3$에 대하여 $\zeta^4=-1$을 사용하면

$$\sigma_5(x)=a-b\zeta+c\zeta^2-\dd{\zeta}^3,\qquad \sigma_7(x)=a-\dd{\zeta}-c\zeta^2-b\zeta^3,\qquad \sigma_3(x)=a+\dd{\zeta}-c\zeta^2+b\zeta^3$$

을 얻는다. 따라서 $\sigma_5(x)=x$인 것은 $b=d=0$인 것이고, $\sigma_7(x)=x$인 것은 $c=0$이고 $d=-b$인 것이며, $\sigma_3(x)=x$인 것은 $c=0$이고 $d=b$인 것이다. 위의 등식들을 사용하여 이를 다시 쓰면 세 subgroup $\langle\sigma_5\rangle$, $\langle\sigma_7\rangle$, $\langle\sigma_3\rangle$의 fixed field가 각각

$$\mathbb{Q}+\mathbb{Q}\zeta^2=\mathbb{Q}(i),\qquad \mathbb{Q}+\mathbb{Q}(\zeta-\zeta^3)=\mathbb{Q}(\sqrt2),\qquad \mathbb{Q}+\mathbb{Q}(\zeta+\zeta^3)=\mathbb{Q}(\sqrt{-2})$$

임을 안다. [§갈루아 이론의 기본정리, ⁋정리 1](/ko/math/field_theory/fundamental_theorem_of_galois_theory#thm1)에 의하여 이들이 $\mathbb{Q}(\zeta_8)$의 자명하지 않은 subextension 전부이다.
:::

$\mathbb{Q}(\zeta_n)$과 그 subextension들은 이렇게 $\mathbb{Q}$의 abelian extension을 대량으로 공급한다. 거꾸로 $\mathbb{Q}$의 임의의 finite degree abelian extension이 어떤 $\mathbb{Q}(\zeta_n)$에 포함된다는 것이 Kronecker와 Weber의 정리인데, 그 증명은 class field theory에 속하므로 여기서 다루지 않는다.

## 소수의 분포에 대한 응용

$\Phi_n$이 정수 계수를 갖는다는 사실은 field 이론 바깥에서도 쓰인다. [\[환론\] §나눗셈환](/ko/math/ring_theory/division_rings)에서 Wedderburn의 소정리를 증명할 때 $\Phi_n(q)$가 정수로서 $q^n-1$을 나눈다는 것이 결정적이었던 것이 그 예이다. 여기서는 같은 종류의 논법으로 Dirichlet 정리의 특수한 경우를 얻는다.

::: 보조정리 9
자연수 $n\geq1$, 정수 $a$, 소수 $p$가 $p\mid\Phi_n(a)$와 $p\nmid n$을 만족한다 하자. 그럼 $\mathbb{F}_p^\times$에서 $\bar a$의 order는 $n$이며, 특히 $n\mid p-1$이다.
:::
::: 증명
[명제 2](#prop2)의 등식은 $\mathbb{Z}[\x]$에서 성립하므로 $\mathbb{F}_p[\x]$로 보내도 성립한다. 특히 $\Phi_n$은 $\x^n-1$을 나누므로 $p\mid a^n-1$이고, 따라서 $\bar a\in\mathbb{F}_p^\times$이며 그 order $d$는 $n$을 나눈다.

$d<n$이라 가정하자. $\bar a^d=1$이므로 $\bar a$는 $\x^d-1$의 root이고, [명제 2](#prop2)에 의해 어떤 $e\mid d$에 대하여 $\Phi_e(\bar a)=0$이다. 그런데 $e\mid d$이고 $d<n$이므로 $e\neq n$이며, 따라서 $\Phi_e$는 $\mathbb{F}_p[\x]$에서 $(\x^n-1)/\Phi_n$을 나눈다. 가정에서 $\Phi_n(\bar a)=0$이었으므로 $\bar a$는 $\Phi_n$과 $(\x^n-1)/\Phi_n$의 공통근이고, 그럼 $\bar a$는 $\x^n-1$의 중근이다. 이는 $p\nmid n$일 때 $\x^n-1$의 root가 모두 simple root라는 [정리 4](#thm4)의 증명 속 관찰에 모순이므로 $d=n$이다.

마지막으로 $\mathbb{F}_p^\times$의 order가 $p-1$이므로 [\[대수적 구조\] §몫군, ⁋명제 5](/ko/math/algebraic_structures/quotient_groups#prop5)에 의하여 $n=d$는 $p-1$을 나눈다.
:::

::: 정리 10
임의의 자연수 $n\geq1$에 대하여, $p\equiv1\pmod n$인 소수 $p$는 무한히 많다.
:::
::: 증명
먼저 $\Phi_1(0)=-1$이고 $n\geq2$이면 $\Phi_n(0)=1$임을 확인한다. [명제 2](#prop2)의 등식에 $\x=0$을 대입하면 $-1=\prod_{d\mid n}\Phi_d(0)$인데, $\Phi_1(0)=-1$이므로 $n\geq2$에 대하여 $n$의 $1$보다 큰 약수 $d$에 대한 $\Phi_d(0)$들의 곱이 $1$이다. $n$에 대한 강한 귀납법으로 $2\leq d<n$인 약수에 대해 $\Phi_d(0)=1$이라 하면 $\Phi_n(0)=1$을 얻는다.

이제 $p\equiv1\pmod n$인 소수가 유한하다고 가정하고 이들을 $p_1,\ldots,p_r$이라 하자. $N=np_1\cdots p_r$로 두고 자연수 $t$에 대하여 $a=Nt$라 하자. $\Phi_n$이 monic이고 $\deg\Phi_n=\varphi(n)\geq1$이므로 $t$를 충분히 크게 잡으면 $\lvert\Phi_n(a)\rvert>1$이고, 그럼 소수 $p$가 존재하여 $p\mid\Phi_n(a)$이다.

$\Phi_n\in\mathbb{Z}[\x]$이고 $N\mid a$이므로 $\Phi_n(a)\equiv\Phi_n(0)\pmod N$이며, 위에서 $\Phi_n(0)=\pm1$이므로 $\Phi_n(a)$와 $N$은 서로소이다. 특히 $p\nmid n$이고 $p$는 어떤 $p_i$와도 같지 않다. 그럼 [보조정리 9](#lem9)에 의하여 $n\mid p-1$, 즉 $p\equiv1\pmod n$이므로 $p$가 $p_i$들 중 하나여야 하여 모순이다.
:::

서로소인 $a,n$에 대하여 $p\equiv a\pmod n$인 소수가 무한히 많다는 Dirichlet의 정리는 해석적인 방법을 필요로 하며, 위의 논법은 $a=1$인 경우에만 작동한다. $\Phi_n$이 잡아내는 것이 order가 정확히 $n$인 원소이고, [보조정리 9](#lem9)가 그로부터 곧바로 $n\mid p-1$을 주기 때문이다.

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  
**[Lan]** S. Lang. *Algebra*. Graduate texts in mathematics. Springer, 2002.
