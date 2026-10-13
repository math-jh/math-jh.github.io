---
title: "원분확대"
description: "1의 원시 n제곱근들을 근으로 갖는 cyclotomic polynomial을 정의하고 그 계수가 정수임을 보인 후, Dedekind의 논법으로 유리수체 위에서의 기약성을 증명한다. 이로부터 원분체의 갈루아 군이 (Z/nZ)의 가역원군과 isomorphic하다는 것을 얻는다."
excerpt: "Cyclotomic polynomial의 기약성과 원분체의 갈루아 군"

categories: [Math / Field Theory]
permalink: /ko/math/field_theory/cyclotomic_extensions
sidebar: 
    nav: "field_theory-ko"

date: 2026-07-22
weight: 12

---

[§거듭제곱근 가해성, ⁋정의 2](/ko/math/field_theory/solvability_by_radicals#def2){: data-lid="wcpld" }에서 우리는 root of unity와 primitive root of unity를 도입하였다. 그 정의에 의해 $n$-th root of unity $\zeta$는 $\x^n-1=0$의 해지만, primitive root가 아닌 경우 이들은 $n$의 약수 $d$에 대하여 $\x^d-1=0$의 해이기도 하다. 예를 들어 $\mathbb{R}$에서 방정식 $\x^4-1=0$의 해를 추가할 때, 

$$\x^4-1=(\x-1)(\x+1)(\x^2+1)$$

이며 이 중 $\x-1$과 $\x+1$의 해는 primitive root of unity가 아니므로, 실제로 primitive root를 주는 방정식은 $\x^2+1$ 뿐이다. 이번 글에서 우리는 이렇게 primitive $n$-th root of unity들만을 근으로 가지는 다항식들을 살펴볼 것이며, 그 결과로 이러한 다항식들이 정수계수의 irreducible polynomial이라는 것을 보이고, 특별히 $\mathbb{K}=\mathbb{Q}$인 경우 $\mathbb{Q}(\zeta)/\mathbb{Q}$의 Galois group이 <em-ko>정확히</em-ko> $(\mathbb{Z}/n\mathbb{Z})^\times$가 된다는 것을 보인다. 이전 글과 마찬가지로, 이번 글에서 등장하는 모든 field는 별도의 언급이 없으면 characteristic $0$인 것으로 생각한다. 

## 원분다항식

위에서 살펴본 다항식을 엄밀히 정의하면 다음과 같다. 

::: 정의 1
Field $\mathbb{K}$와 자연수 $n\geq1$에 대하여, $\overline{\mathbb{K}}$ 안의 primitive $n$-th root of unity 전체를 해로 갖는 monic polynomial

$$\Phi_n(\x)=\prod_{\zeta}(\x-\zeta)\in\overline{\mathbb{K}}[\x]$$

을 $n$번째 *cyclotomic polynomial<sub>원분다항식</sub>*이라 부른다. 여기서 곱은 $\mu_n$의 generator $\zeta$ 전체에 대한 것이다.
:::

$\mu_n$의 generator를 하나 고정하여 $\zeta$라 하자. 그럼 우리는 이미 $\mu_n$의 generator는 정확히 $\gcd(m,n)=1$인 $\zeta^m$들인 것을 확인하였으므로, $1\leq m\leq n$ 중 $n$과 서로소인 것의 개수를 $\varphi(n)$으로 적으면 

$$\Phi_n(\x)=\prod_{\substack{1\leq m\leq n\\ \gcd(m,n)=1}}(\x-\zeta^m),\qquad \deg\Phi_n=\varphi(n)$$

임을 안다. 가령 $\mu_1=\{1\}$이고 $\mu_2=\{\pm1\}$이므로 $\Phi_1=\x-1$, $\Phi_2=\x+1$이며, $\mu_4$의 generator가 $\pm i$인 것으로부터 $\Phi_4=\x^2+1$이다. 소수 $p$에 대해서는 $1$을 제외한 $\mu_p$의 모든 원소가 generator이므로

$$\Phi_p(\x)=\frac{\x^p-1}{\x-1}=\x^{p-1}+\x^{p-2}+\cdots+\x+1$$

이 된다. 

그 정의에 의하여 $\Phi_n$은 $\overline{\mathbb{K}}[\x]$의 원소이지만, 다음 명제는 이 다항식이 실제로는 정수계수를 가진다는 것을 보여준다. 

::: 명제 2
자연수 $n\geq1$에 대하여 다음이 성립한다.

1. $\x^n-1=\prod_{d\mid n}\Phi_d(\x)$이다.
2. $\Phi_n(\x)\in\mathbb{Z}[\x]$이다. 특히 $\Phi_n$은 $\mathbb{K}$의 선택에 의존하지 않는다.
:::
::: 증명
우선 첫째 결과를 보이자. $\mu_n$의 order $d$ element $\omega$를 생각하면, $\omega$가 생성하는 subgroup $\langle\omega\rangle$은 order $d$의 cyclic group이며 $\omega^d=1$를 만족한다. 즉, $\omega$는 primitive $d$-th root of unity이다. 거꾸로, $n$의 임의의 약수 $d$가 주어졌다면 primitive $d$-th root of unity는 $\mu_d\subseteq\mu_n$의 원소로서 order $d$를 가지므로, $\mu_n$은 $n$의 약수 $d$들에 대하여 primitive $d$-th root of unity들의 집합으로 분할된다. 그럼 첫째 결과는 

$$\x^n-1=\prod_{\omega\in\mu_n}(\x-\omega)$$

을 이 분할에 따라 묶어준 것에 불과하다. 

이제 둘째 결과를 보이자. 우선 $n=1$이면 $\Phi_1=\x-1\in\mathbb{Z}[\x]$이므로 이는 자명하다. $n>1$이라 하고, $n$보다 작은 모든 자연수에 대하여 cyclotomic polynomial이 정수계수라 하자. 이제

$$g(\x)=\prod_{\substack{d\mid n\\ d<n}}\Phi_d(\x)$$

로 두면, $g$는 monic이고, 귀납 가정에 의해 $\mathbb{Z}[\x]$에 속하며, 첫째 결과로부터

$$\x^n-1=\Phi_n(\x) g(\x)$$

이 성립한다. 한편 $g$가 monic이므로 [\[환론\] §다항식환, ⁋명제 5](/ko/math/ring_theory/polynomial_rings#prop5){: data-lid="85vcs" }와 그 직후의 논의에 의하여 

$$\x^n-1=qg+r,\qquad \deg r<\deg g$$

를 만족하는 $q,r\in\mathbb{Z}[\x]$가 유일하게 존재하므로, 이러한 $q$는 <em-ko>반드시</em-ko> $\Phi_n$이어야 하고, 따라서 $\Phi_n$ 또한 정수계수 다항식이 된다.   
:::

다소 주의할 것은 $\Phi_n(\x)$의 모든 계수가 $0$ 혹은 $\pm 1$이 될 필요는 없다는 것으로, 가장 작은 반례는 $\Phi_{105}$이다. ([Wikipedia, Cyclotomic Polynomial](https://en.wikipedia.org/wiki/Cyclotomic_polynomial))

## 유리수체 위의 기약성

[명제 2](#prop2)에 의하여 $\Phi_n(\x)\in\mathbb{Z}[\x]$이므로, $\Phi_n$은 $\mathbb{Z}$를 포함하는 가장 작은 field, 즉 $\mathbb{Q}$ 위의 polynomial ring $\mathbb{Q}[\x]$의 원소로 볼 수 있으며, $\mathbb{Q}$는 characteristic $0$의 prime field로서 모든 characteristic zero field $\mathbb{K}$에 포함되므로 이렇게 보는 것에 아무런 문제가 없다. 우리는 이 경우에 한하여, $\Phi_n$이 $\zeta$의 minimal polynomial이 된다는 것을 우선 보인다. 이를 위해서는 $\Phi_n$이 $\mathbb{Q}[\x]$에서 irreducible인 것을 보이면 충분하다. ([§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15))

::: 보조정리 3
Monic polynomial $f\in\mathbb{Z}[\x]$가 $\mathbb{Q}[\x]$의 monic polynomial $g,h$에 대하여 $f=gh$로 쓰인다면 $g,h\in\mathbb{Z}[\x]$이다.
:::
::: 증명
두 monic polynomial $g,h$가 $\mathbb{Q}[\x]$의 원소이므로, 그 상수배 $ag$와 $bh$가 $\mathbb{Z}[\x]$에 속하도록 하는 최소의 양의 정수 $a,b$가 존재한다. 그럼 $a$와 $b$의 최소성에 의하여, $ag$와 $bh$의 계수들의 최대공약수를 각각 구하면 이들은 모두 $1$이 되어야 함을 안다. 

이제 $abf=(ag)(bh)$이며, 우리 주장은 $ab=1$이라는 것이다. 결론에 반하여 $ab>1$이고, $ab$를 나누는 소수 $p$가 주어졌다 하자. 그럼 $\mathbb{F}_p[\x]$에서 $ab=0$이므로 이 등식은 

$$0=\overline{ag}\cdot \overline{bh}$$

가 되며, 이 때 $\mathbb{F}_p[\x]$가 integral domain이므로 ([\[환론\] §다항식환, ⁋명제 4](/ko/math/ring_theory/polynomial_rings#prop4){: data-lid="neep1" }) $\overline{ag}=0$ 또는 $\overline{bh}=0$이어야 한다. 즉, $ag$ 혹은 $bh$의 계수들의 최대공약수가 $p$로 나누어져야 하며, 이는 모순이므로 원하는 결과를 얻는다.
:::

그럼 다음을 보일 수 있다.

::: 정리 4 (Gauss)
임의의 자연수 $n\geq1$에 대하여 $\Phi_n$은 $\mathbb{Q}[\x]$에서 irreducible이다.
:::
::: 증명
Primitive $n$-th root of unity $\zeta\in\overline{\mathbb{Q}}$를 하나 고정하자. 그럼 $\zeta$의 minimal polynomial $f\in \mathbb{Q}[\x]$는 $\Phi_n$과 $\x^n-1$을 모두 나누어야 하며, ([§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15){: data-lid="gqhj5" }) 이로부터 $\x^n-1=fg$이라 하면 $f,g$가 모두 monic이므로 [보조정리 3](#lem3){: data-lid="pmj8g" }에 의해 $f,g\in\mathbb{Z}[\x]$임을 안다.

증명의 핵심은 $f$의 임의의 해 $\omega$와, $n$을 나누지 않는 임의의 소수 $p$가 주어졌을 때, $\omega^p$ 또한 $f$의 해가 된다는 것이다. 결론에 반하여 $f(\omega^p)\neq0$이라 하자. 우선 정의에 의해 $\omega^n=1$이므로 $\omega^p$는 $\x^n-1$의 해이고, 따라서 $g(\omega^p)=0$이다. 즉 $\omega$는 $g(\x^p)\in\mathbb{Z}[\x]$의 해이다. 한편 $f$는 minimal polynomial이므로 monic irreducible이고, $f(\omega)=0$이므로 [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15){: data-lid="dhkb9" }에 의해 $f$는 $\omega$의 minimal polynomial이며 따라서 $f$는 $g(\x^p)$를 나눈다. 이 때, $f$가 monic이므로 [명제 2](#prop2)에서의 증명과 마찬가지로 $g(\x^p)$를 $f$로 나눈 몫 또한 $\mathbb{Z}[\x]$에 속한다.

이제 이 관계를 $\mathbb{F}_p[\x]$로 보내자. $\mathbb{F}_p$의 모든 원소 $c$는 $c^p=c$를 만족하고, Frobenius endomorphism이 ring homomorphism이므로 ([§체, ⁋정리 10](/ko/math/field_theory/fields#thm10){: data-lid="5d353" }) $g$의 상을 $\bar{g}(\x)=\sum c_i\x^i\in \mathbb{F}_p[\x]$로 쓰면 

$$\bar{g}(\x)^p=\sum c_i^p\x^{ip}=\sum c_i(\x^p)^i=\bar{g}(\x^p)$$

가 성립한다. 따라서 $\bar{f}$는 $\bar{g}^p$를 나눈다. 한편, $\deg\bar{f}=\deg f\geq1$이므로, $\bar{f}$의 irreducible factor $h$를 하나 택하면 $h$는 $\bar{g}^p$를 나눈다. 이 때 $\mathbb{F}_p[\x]$가 UFD이므로 ([\[환론\] §다항식환, ⁋정리 16](/ko/math/ring_theory/polynomial_rings#thm16){: data-lid="37wfm" }) [\[환론\] §정역, ⁋명제 17](/ko/math/ring_theory/integral_domains#prop17){: data-lid="eurm0" }에 의하여 $h$는 prime이고 따라서 $\bar{g}$를 나누어야 한다. 따라서 $h^2$은 $\bar{f}\bar{g}=\x^n-1$을 나눈다.

그런데 $p\nmid n$이므로 $\mathbb{F}_p$에서 $n\neq0$이고, 따라서 $\x^n-1$과 그 derivative $n\x^{n-1}$은 공통근을 갖지 않는다. 즉 $\x^n-1$은 $\overline{\mathbb{F}_p}$에서 중근을 갖지 않으므로 $h^2$이 $\x^n-1$을 나누는 것은 모순이다. 

이제 우리는 $\gcd(m,n)=1$인 $1\leq m\leq n$을 택하고 $m=p_1\cdots p_r$을 소인수분해라 하자. 그럼 각 $p_i$는 $n$과 서로소이므로 $n$을 나누지 않고, 따라서 위의 주장을 

$$\zeta,\zeta^{p_1},\zeta^{p_1p_2},\ldots$$

에 차례로 적용하여 $\zeta^m$이 $f$의 해임을 알 수 있다. 즉 $f$는 $\varphi(n)$개의 primitive $n$-th root of unity를 모두 해로 가지며, $f$가 $\Phi_n$을 나누며 둘 다 monic이므로 $f=\Phi_n$이다. 따라서 $\Phi_n$은 minimal polynomial이고, 따라서 irreducible이다.
:::

그럼 특히 다음이 성립한다. 

::: 따름정리 5
Primitive $n$-th root of unity $\zeta$에 대하여 $\Phi_n$은 $\zeta$의 $\mathbb{Q}$ 위에서의 minimal polynomial이며, $[\mathbb{Q}(\zeta):\mathbb{Q}]=\varphi(n)$이다.
:::
::: 증명
$\Phi_n$은 monic이고 [정리 4](#thm4){: data-lid="vcuc7" }에 의해 irreducible이며 $\Phi_n(\zeta)=0$이므로, [§대수적 확장, ⁋정리 15](/ko/math/field_theory/algebraic_extensions#thm15){: data-lid="l7j9e" }에 의하여 $\Phi_n$은 $\zeta$의 minimal polynomial이고 $\mathbb{Q}[\zeta]=\mathbb{Q}(\zeta)$의 $\mathbb{Q}$ 위에서의 차원은 $\deg\Phi_n=\varphi(n)$이다.
:::

## 원분확대의 갈루아 군

이제 우리는 primitive root of unity를 하나 추가했을 때 얻어지는 extension을 살펴본다. 

::: 정의 6
Field $\mathbb{K}$와 primitive $n$-th root of unity $\zeta$에 대하여 extension $\mathbb{K}(\zeta)/\mathbb{K}$를 $n$번째 *cyclotomic extension<sub>원분확대</sub>*이라 부른다. 특히 $\mathbb{K}=\mathbb{Q}$인 경우 $\mathbb{Q}(\zeta)$를 $n$번째 *cyclotomic field<sub>원분체</sub>*라 부르고, generator를 하나 고정하여 $\zeta_n$으로 적을 때 이를 $\mathbb{Q}(\zeta_n)$으로 적는다.
:::

두 generator $\zeta,\zeta'$에 대하여 $\zeta'\in\langle\zeta\rangle$이고 $\zeta\in\langle\zeta'\rangle$이므로 $\mathbb{K}(\zeta)=\mathbb{K}(\zeta')$이다. 즉 cyclotomic extension은 generator의 선택에 의존하지 않으며, $\mathbb{K}(\zeta)=\mathbb{K}(\mu_n)$이 성립한다.

임의의 field $\mathbb{K}$에 대하여는 $\mathbb{K}(\zeta)/\mathbb{K}$에 대해 특별한 말을 하는 것이 쉽지 않다. 가령 $\Phi_4$를 $\mathbb{C}$에서 보면, $\x^4-1=0$의 해인 $\x=\pm i$가 이미 $\mathbb{C}$에 포함되어 있으므로 $[\mathbb{K}(\zeta):\mathbb{K}]=1$이다. 그러나 다음 정리는 $\mathbb{K}=\mathbb{Q}$인 최소의 경우에는 이들이 우리가 상상하는대로 행동한다는 것을 보여준다. 

::: 정리 7
$\mathbb{Q}(\zeta_n)/\mathbb{Q}$는 finite degree Galois extension이고, [§거듭제곱근 가해성, ⁋명제 3](/ko/math/field_theory/solvability_by_radicals#prop3){: data-lid="u5541" }의 injective homomorphism

$$\Gal(\mathbb{Q}(\zeta_n)/\mathbb{Q})\rightarrow(\mathbb{Z}/n\mathbb{Z})^\times$$

은 isomorphism이다.
:::
::: 증명
$\mathbb{Q}(\zeta_n)/\mathbb{Q}$가 finite degree Galois extension이고 주어진 homomorphism이 injective인 것은 [§거듭제곱근 가해성, ⁋명제 3](/ko/math/field_theory/solvability_by_radicals#prop3){: data-lid="bwvv2" }이다. 한편 $\mathbb{Q}(\zeta_n)/\mathbb{Q}$가 Galois extension이므로 [§갈루아 이론의 기본정리, ⁋명제 2](/ko/math/field_theory/fundamental_theorem_of_galois_theory#prop2)와 [따름정리 5](#cor5){: data-lid="yyps0" }에 의해

$$\lvert\Gal(\mathbb{Q}(\zeta_n)/\mathbb{Q})\rvert = [\mathbb{Q}(\zeta_n):\mathbb{Q}] = \varphi(n) = \lvert(\mathbb{Z}/n\mathbb{Z})^\times\rvert$$

이다. 크기가 같은 두 유한집합 사이의 단사함수는 전사이므로, 주어진 injective homomorphism은 isomorphism이다.
:::

특히 $\Gal(\mathbb{Q}(\zeta_n)/\mathbb{Q})$는 order $\varphi(n)$의 abelian group이다. 그럼 [§갈루아 이론의 기본정리, ⁋정리 1](/ko/math/field_theory/fundamental_theorem_of_galois_theory#thm1){: data-lid="dx5pd" }에 의해 $\mathbb{Q}(\zeta_n)$의 subextension들은 $(\mathbb{Z}/n\mathbb{Z})^\times$의 subgroup들과 일대일로 대응하며, abelian group의 모든 subgroup이 normal이므로 [§갈루아 이론의 기본정리, ⁋따름정리 6](/ko/math/field_theory/fundamental_theorem_of_galois_theory#cor6){: data-lid="2x6id" }에 의하여 그 subextension들은 모두 $\mathbb{Q}$의 Galois extension이다.

가령 $n=8$인 경우 $(\mathbb{Z}/8\mathbb{Z})^\times\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$이므로 자명하지 않은 proper subextension이 정확히 셋 존재한다. 실제로 $\zeta=\zeta_8=(1+i)/\sqrt{2}$에 대하여

$$\zeta^2=i,\qquad \zeta+\zeta^{-1}=\sqrt{2},\qquad \zeta-\zeta^{-1}=i\sqrt{2}=\sqrt{-2}$$

이므로 $\mathbb{Q}(\zeta_8)$은 세 개의 서로 다른 quadratic field $\mathbb{Q}(i), \mathbb{Q}(\sqrt{2}), \mathbb{Q}(\sqrt{-2})$를 포함하며, Galois correspondence에 의해 이들이 $\mathbb{Q}(\zeta_8)$의 자명하지 않은 subextension 전부가 된다. 즉 $\mathbb{Q}$에 $1$의 $8$제곱근을 추가하는 것만으로 $\sqrt{2}$와 같은 무리수 또한 자연스럽게 얻어지는 것을 확인할 수 있다.

---

**참고문헌**

**[Bou]** N. Bourbaki. *Algebra II: Chapters 4–7*. Springer, 2003.  
**[Lan]** S. Lang. *Algebra*. Graduate texts in mathematics. Springer, 2002.
