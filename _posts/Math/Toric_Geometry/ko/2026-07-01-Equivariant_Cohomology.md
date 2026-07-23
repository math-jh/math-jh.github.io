---
title: "동변 코호몰로지"
description: "위상군의 작용을 기억하는 코호몰로지 이론을 Borel 구성으로 정의하고, 분류공간의 코호몰로지를 계수로 갖는 대수 구조와 torus 작용의 weight 기술을 다룬다."
excerpt: "Borel construction, equivariant cohomology H_G(X)=H(X_G), and H_T(pt)=Sym(character lattice)"

categories: [Math / Toric Geometry]
permalink: /ko/math/toric_geometry/equivariant_cohomology
sidebar: 
    nav: "toric_geometry-ko"

date: 2026-07-01
last_modified_at: 2026-07-01
weight: 10

published: false

---

위상군 $G$가 위상공간 $X$ 위에 연속적으로 작용할 때, 이 작용을 반영하는 cohomology 불변량을 어떻게 정의할 것인가? 가장 소박한 후보는 orbit space $X/G$의 cohomology $H^\bullet(X/G)$이다. 작용이 free이고 quotient $X\rightarrow X/G$가 충분히 좋은 경우, 가령 principal $G$-bundle인 경우에는 이것이 올바른 답을 준다. 그러나 작용에 fixed point나 그 밖의 비자명한 stabilizer가 있으면 $X/G$는 특이해지고, 그 cohomology는 작용의 정보를 대부분 잃어버린다.

전형적인 예가 원군 $S^1$이 $2$-구면 $S^2$ 위에 수직축을 중심으로 회전하며 작용하는 경우이다. 이 작용의 orbit는 위도원들이며, 북극과 남극의 두 fixed point가 있다. 따라서 orbit space는 위도를 좌표로 갖는 닫힌 구간 $S^2/S^1\cong[-1,1]$이 되고, 이는 contractible이므로 $H^\bullet(S^2/S^1)$은 $0$차에 $\mathbb{Z}$ 하나만 남는다. 곧 naive quotient는 $S^2$의 위상과 회전 작용을 모두 망각한다.

우리가 원하는 것은 (i) 작용이 어떻든 항상 "좋은 quotient"의 cohomology처럼 행동하고, (ii) 작용이 free일 때는 $H^\bullet(X/G)$로 환원되는 불변량이다. 해결의 열쇠는 $X$를 그와 homotopy equivalent하면서 $G$가 free하게 작용하는 공간으로 바꾸는 것이다. Universal bundle의 total space $EG$는 contractible이고 그 위에서 $G$가 free하게 작용하므로, 곱 $EG\times X$ 위에서도 $G$가 free하게 작용한다. $EG$가 contractible이라 $EG\times X$는 $X$와 같은 homotopy type을 가지면서도, 이제 작용이 free이므로 그 quotient는 특이성을 갖지 않는다. 이 quotient의 cohomology를 취하는 것이 Borel의 구성이며, 이 글의 주제인 *equivariant cohomology*이다. 앞으로 $G$는 topological group, $X$는 paracompact $G$-space (별다른 언급이 없는 한 CW complex)를 뜻하고, $R$은 계수환을 뜻한다.

## Borel 구성

우리는 $EG$를 곱하여 작용을 free하게 만든 뒤 quotient를 취하는 위 아이디어를 정의로 옮긴다. [\[대수적 위상수학\] §분류공간, ⁋정의 6](/ko/math/algebraic_topology/classifying_spaces#def6)에서 구성한 universal bundle $EG\rightarrow BG$와 classifying space $BG$를 다시 쓰면, $EG$는 contractible하며 $G$는 그 위에 right action으로 free하게 작용한다. 한편 $X$ 위의 $G$-작용은 left action으로 둔다.

::: 정의 1
Topological group $G$와 left $G$-space $X$에 대하여, 곱공간 $EG\times X$ 위에 $G$-작용을

$$(e,x)\cdot g=(e\cdot g, g^{-1}\cdot x)$$

로 정의하고, 그 orbit space를

$$X_G:=EG\times_G X=(EG\times X)/G$$

로 적는다. 이 공간을 $G$-작용의 *homotopy quotient<sub>호모토피 몫</sub>* 또는 *Borel construction<sub>보렐 구성</sub>*이라 부른다. 계수환 $R$에 대한 $X$의 *equivariant cohomology<sub>동변 코호몰로지</sub>*를

$$H_G^\bullet(X;R):=H^\bullet(X_G;R)$$

로 정의한다.
:::

$X_G$는 정확히 principal $G$-bundle $EG\rightarrow BG$에 fiber $X$를 붙인 associated bundle이다. ([\[대수적 위상수학\] §분류공간, ⁋정의 3](/ko/math/algebraic_topology/classifying_spaces#def3)) 계수환 $R$을 고정한 동안에는 이를 생략하고 $H_G^\bullet(X)$로 적는다. Cohomology의 cup product가 $H^\bullet(X_G)$에 graded-commutative $R$-algebra 구조를 주므로 ([\[대수적 위상수학\] §합곱, ⁋정의 1](/ko/math/algebraic_topology/cup_products#def1)) $H_G^\bullet(X)$ 역시 graded-commutative $R$-algebra이다.

이 구성은 두 가지 방향으로 functorial하다. 첫째, $X$에 대해 contravariant이다. $G$-equivariant 연속함수 $f:X\rightarrow Y$는 $\id\times f:EG\times X\rightarrow EG\times Y$를 주고, 이것이 $G$-작용과 호환되므로 quotient 사이의 morphism $f_G:X_G\rightarrow Y_G$로 내려간다. 따라서 $f^\ast:H_G^\bullet(Y)\rightarrow H_G^\bullet(X)$를 얻으며, 항등사상과 합성을 보존한다. 둘째, $G$에 대해서도 contravariant이다. 연속적인 group homomorphism $\phi:H\rightarrow G$가 주어지면 $G$-space $X$는 $\phi$를 통해 $H$-space가 되고, $BH\rightarrow BG$를 덮는 $H$-equivariant morphism $EH\rightarrow EG$가 존재한다. ([\[대수적 위상수학\] §분류공간, ⁋보조정리 9](/ko/math/algebraic_topology/classifying_spaces#lem9)) 이 morphism이 $X_H=EH\times_H X\rightarrow EG\times_G X=X_G$를 유도하여 $H_G^\bullet(X)\rightarrow H_H^\bullet(X)$를 준다. 특히 $H=\{e\}$인 경우가 곧 아래에서 다룰 ordinary cohomology로의 restriction이다.

## 동변 코호몰로지의 기본 성질

Borel 구성이 fiber bundle $X_G\rightarrow BG$로 실현된다는 사실로부터 equivariant cohomology의 기본 성질이 한꺼번에 따라온다. 우리는 먼저 이 bundle 구조를 정리한다.

::: 명제 2
$G$-space $X$에 대하여 projection $\pi:X_G\rightarrow BG$, $[e,x]\mapsto [e]$는 fiber $X$를 갖는 fiber bundle이다. 이로부터 다음이 성립한다.

1. $H_G^\bullet(\mathrm{pt})=H^\bullet(BG)$이다.
2. $\pi^\ast:H^\bullet(BG)\rightarrow H_G^\bullet(X)$는 $H_G^\bullet(X)$에 $H^\bullet(BG)$-algebra 구조를 준다.
3. Fiber의 포함 $\iota:X\hookrightarrow X_G$은 algebra homomorphism인 *restriction* $\iota^\ast:H_G^\bullet(X)\rightarrow H^\bullet(X)$을 유도한다.
:::
::: 증명
$X_G=EG\times_G X$는 principal $G$-bundle $EG\rightarrow BG$에 fiber $X$를 붙인 associated bundle이고 ([\[대수적 위상수학\] §분류공간, ⁋정의 3](/ko/math/algebraic_topology/classifying_spaces#def3)) associated bundle은 fiber bundle이므로, $\pi:X_G\rightarrow BG$는 fiber $X$를 갖는 fiber bundle이다.

(1) $X=\mathrm{pt}$이면 $G$가 한 점 위에 자명하게 작용하므로

$$\mathrm{pt}_G=EG\times_G\mathrm{pt}=EG/G=BG$$

이고, 따라서 $H_G^\bullet(\mathrm{pt})=H^\bullet(BG)$이다.

(2) 유일한 $G$-equivariant morphism $X\rightarrow\mathrm{pt}$가 유도하는 morphism이 바로 $\pi:X_G\rightarrow\mathrm{pt}_G=BG$이다. 그 pullback $\pi^\ast:H^\bullet(BG)\rightarrow H^\bullet(X_G)=H_G^\bullet(X)$은 ring homomorphism이며, 이를 통해 $H_G^\bullet(X)$은 $H^\bullet(BG)$-algebra가 된다.

(3) $EG$의 한 점 $e_0$을 고정하면, 그 image $b_0=[e_0]\in BG$ 위의 fiber는 $\pi^{-1}(b_0)=\{[e_0,x]\mid x\in X\}$이고, $x\mapsto[e_0,x]$가 $X$와 이 fiber 사이의 위상동형을 준다. 이 포함 $\iota:X\hookrightarrow X_G$의 pullback $\iota^\ast:H_G^\bullet(X)\rightarrow H^\bullet(X)$이 restriction이다. $EG$가 path-connected이므로 $e_0$의 선택을 바꾸어도 $\iota$의 homotopy class, 따라서 $\iota^\ast$는 변하지 않는다.
:::

성질 (2)는 equivariant cohomology가 단순한 $R$-가군이 아니라 항상 $H^\bullet(BG)$ 위의 algebra라는, 이 이론의 가장 중요한 구조적 특징을 말한다. 이 base ring $H^\bullet(BG)=H_G^\bullet(\mathrm{pt})$이 작용의 정보를 담는 좌표 역할을 하며, 이후 torus의 경우 이것이 character lattice 위의 다항식환으로 구체화된다. 성질 (3)의 restriction $\iota^\ast$은 작용을 잊고 보통의 cohomology로 내려가는 morphism이며, $H^\bullet(BG)$의 양의 degree 부분을 $0$으로 보내는 augmentation과 호환된다.

작용이 free일 때 equivariant cohomology가 orbit space의 cohomology로 환원된다는, 도입부에서 요구한 성질을 이제 증명한다.

::: 명제 3
$G$가 $X$ 위에 free하게 작용하고 quotient $X\rightarrow X/G$가 principal $G$-bundle이라 하자. 그럼 자연스러운 동형

$$H_G^\bullet(X)\cong H^\bullet(X/G)$$

이 성립한다.
:::
::: 증명
Morphism

$$q:X_G=EG\times_G X\rightarrow X/G,\qquad [e,x]\mapsto Gx$$

를 생각한다. 이는 잘 정의되어 있다. $X\rightarrow X/G$가 principal $G$-bundle이므로 $X/G$의 각 점은 $X\vert_U\cong U\times G$로 trivialize되는 열린 이웃 $U$를 가지며, 그 위에서

$$q^{-1}(U)=EG\times_G(U\times G)\cong U\times EG$$

이다. 마지막 동형은 $[e,(u,g)]\mapsto(u,e\cdot g)$로 주어지며 ($G$가 두 번째 성분에서 simply transitive하게 작용하므로 잘 정의된 위상동형이다), 따라서 $q:X_G\rightarrow X/G$는 fiber $EG$를 갖는 fiber bundle이다. $EG$가 contractible이므로 이 bundle은 fiber가 contractible하다. Contractible fiber를 갖는 fiber bundle은 Dold의 정리에 의해 paracompact base 위에서 homotopy equivalence이므로 ([tD] §6), $q$는 homotopy equivalence이고

$$H_G^\bullet(X)=H^\bullet(X_G)\xrightarrow[\cong]{q^\ast}H^\bullet(X/G)$$

가 성립한다.
:::

이 명제는 equivariant cohomology가 free 작용에 대해서는 새로운 정보를 주지 않음을 보여 준다. 곧 $H_G^\bullet$의 쓸모는 작용이 free가 아닐 때, 가령 fixed point가 있을 때 드러난다. 이 경우 orbit space $X/G$는 특이하지만 $X_G$는 항상 smooth fiber bundle의 total space로서 잘 행동하므로, $H_G^\bullet(X)$이 $H^\bullet(X/G)$를 대신하는 올바른 불변량이 된다.

## Torus 작용과 character lattice

이제 우리가 실제로 사용할 경우, 곧 구조군이 $n$차원 torus $T=(S^1)^n$인 경우로 넘어간다. 이때 base ring $H_T^\bullet(\mathrm{pt})=H^\bullet(BT)$은 명시적으로 계산되어 있으며, 그 degree $2$ 부분이 torus의 character lattice와 동일시된다.

::: 명제 4
$n$차원 torus $T=(S^1)^n$의 character lattice $M=\mathrm{Hom}(T,S^1)$에 대하여,

$$H_T^\bullet(\mathrm{pt};\mathbb{Z})=H^\bullet(BT;\mathbb{Z})=\mathrm{Sym}_{\mathbb{Z}}(M)=\mathbb{Z}[t_1,\ldots,t_n],\qquad \lvert t_i\rvert=2$$

이다. 여기서 $M$은 degree $2$ 부분 $H^2(BT;\mathbb{Z})$에 놓이며, 각 character $\chi\in M$은 associated line bundle $L_\chi=ET\times_T\mathbb{C}_\chi$의 first Chern class $c_1(L_\chi)\in H^2(BT;\mathbb{Z})$에 대응한다.
:::
::: 증명
$H^\bullet(BT;\mathbb{Z})=\mathbb{Z}[t_1,\ldots,t_n]$이며 degree $2$ 부분 $H^2(BT;\mathbb{Z})$이 character lattice $\mathrm{Hom}(T,S^1)$과 표준적으로 동형이라는 사실은 [\[대수적 위상수학\] §분류공간, ⁋따름정리 12](/ko/math/algebraic_topology/classifying_spaces#cor12)에서 보였다. 그 동형은 character $\chi:T\rightarrow S^1$에 $B\chi:BT\rightarrow BS^1=\mathbb{CP}^\infty$의 pullback $(B\chi)^\ast(t)\in H^2(BT;\mathbb{Z})$를 대응시키는 것이었고, $t=c_1$이 $BS^1=\mathbb{CP}^\infty$ 위의 tautological line bundle의 first Chern class였으므로, 이 pullback은 곧 $\chi$가 주는 일차원 representation $\mathbb{C}_\chi$에 대한 associated line bundle $L_\chi=ET\times_T\mathbb{C}_\chi$의 $c_1(L_\chi)$이다. Polynomial ring이 그 degree $2$ 부분 위의 symmetric algebra이므로 $\mathbb{Z}[t_1,\ldots,t_n]=\mathrm{Sym}_{\mathbb{Z}}(M)$이다.
:::

이 동형은 character lattice의 원소, 곧 [\[리 이론\] §원환면의 작용, ⁋정의 4](/ko/math/lie_theory/torus_action#def4)에서 정의한 torus representation의 weight를 $H_T^\bullet(\mathrm{pt})$의 degree $2$ class로 읽게 해 준다. 좌표 character $T\rightarrow S^1$, $(\lambda_1,\ldots,\lambda_n)\mapsto\lambda_i$를 $t_i$로 적으면, weight $a=(a_1,\ldots,a_n)\in M\cong\mathbb{Z}^n$인 representation은 degree $2$ class $a_1t_1+\cdots+a_nt_n$에 대응한다. 이 degree의 두 배 차이 (weight는 degree $1$처럼 세지만 cohomology에서는 degree $2$에 놓인다) 는 $\mathbb{CP}^\infty$의 cohomology가 짝수 degree에만 있다는 사실에서 비롯한다. 앞으로 보게 될 계산에서 fixed point에 놓인 representation의 weight들이 $H_T^\bullet(\mathrm{pt})=\mathbb{Z}[t_1,\ldots,t_n]$의 일차식으로 직접 나타난다.

## 사영다발 정리

뒤따르는 두 계산은 모두 projective space를 fiber로 갖는 bundle의 cohomology를 구하는 일로 환원된다. 이를 위해 vector bundle의 projectivization에 대한 표준적인 결과를 line bundle들의 직합인 경우에 한해 정리해 둔다.

::: 명제 5 (사영다발 정리)
Paracompact 공간 $B$ 위의 복소 line bundle들 $L_1,\ldots,L_r$과 그 직합 $E=L_1\oplus\cdots\oplus L_r$에 대하여, fiberwise 일차원 부분공간들의 공간 $\mathbb{P}(E)\xrightarrow{\pi}B$를 생각하자. Tautological subbundle $\mathcal{O}_{\mathbb{P}(E)}(-1)\subseteq\pi^\ast E$의 first Chern class를 $h=c_1(\mathcal{O}_{\mathbb{P}(E)}(-1))$라 하면, $H^\bullet(\mathbb{P}(E))$은 $1,h,\ldots,h^{r-1}$을 기저로 갖는 free $H^\bullet(B)$-가군이며 단 하나의 관계식

$$\prod_{i=1}^r\big(h-\pi^\ast c_1(L_i)\big)=0$$

을 만족한다. 곧 $H^\bullet(\mathbb{P}(E))=H^\bullet(B)[h]\big/\prod_{i=1}^r(h-c_1(L_i))$이다.
:::
::: 증명
Tautological 포함 $\mathcal{O}(-1)\hookrightarrow\pi^\ast E$은 어디서도 사라지지 않는 bundle morphism이고, 이는 $\mathrm{Hom}(\mathcal{O}(-1),\pi^\ast E)=\pi^\ast E\otimes\mathcal{O}(1)$의 nowhere-zero section과 같다. 여기서 $\mathcal{O}(1)=\mathcal{O}(-1)^\ast$이고 $c_1(\mathcal{O}(1))=-h$이다. Rank $r$인 복소 bundle이 nowhere-zero section을 가지면 top Chern class $c_r$이 사라지므로

$$c_r\big(\pi^\ast E\otimes\mathcal{O}(1)\big)=0$$

이다. $\pi^\ast E$의 Chern root는 $\pi^\ast c_1(L_i)=:x_i$이고, line bundle $\mathcal{O}(1)$을 텐서하면 각 root가 $-h$만큼 평행이동하므로

$$0=c_r\big(\pi^\ast E\otimes\mathcal{O}(1)\big)=\prod_{i=1}^r(x_i-h)$$

이고, 전체 부호 $(-1)^r$을 정리하면 진술한 관계식을 얻는다. Free 기저 $1,h,\ldots,h^{r-1}$은 Leray–Hirsch 정리에서 나온다. 한 fiber로 제한하면 $\mathcal{O}(-1)$은 $\mathbb{P}^{r-1}$ 위의 tautological line bundle로 제한되어 $h$는 hyperplane class의 음수가 되고, 따라서 $1,h,\ldots,h^{r-1}$이 fiber $\mathbb{P}^{r-1}$의 cohomology의 기저로 제한된다. Leray–Hirsch 정리에 의해 이들은 $H^\bullet(\mathbb{P}(E))$의 free $H^\bullet(B)$-기저를 이룬다. 자세한 내용은 [tD]의 §16, §19를 따른다.
:::

이 정리에서 $E$가 일반적인 vector bundle일 때는 관계식이 $E$의 Chern class들로 쓰이지만, 우리가 다룰 torus의 경우 $E$가 항상 character에 대응하는 line bundle들의 직합으로 나타나므로 위의 분해된 형태로 충분하다. 이제 $h$를 $H^\bullet(B)$-계수 다항식환의 변수로 보면, $H^\bullet(\mathbb{P}(E))$은 $h$에 대해 $r$차의 monic 다항식 하나를 법으로 하는 quotient임을 알 수 있다.

## 예시: 회전하는 2-구면

도입부의 회전하는 $S^2$로 돌아가, 그 equivariant cohomology를 명시적으로 계산하고 naive quotient와 대조한다. $S^2=\mathbb{P}^1=\mathbb{P}(\mathbb{C}_0\oplus\mathbb{C}_1)$로 두고, $S^1$이

$$\lambda\cdot[z_0:z_1]=[z_0:\lambda z_1]$$

로 작용한다 하자. 곧 두 좌표선은 각각 weight $0$, weight $1$인 일차원 representation $\mathbb{C}_0$, $\mathbb{C}_1$이며, 작용은 두 fixed point $p_0=[1:0]$과 $p_1=[0:1]$을 갖는다. ([\[리 이론\] §원환면의 작용, ⁋예시 3](/ko/math/lie_theory/torus_action#ex3)) Projectivization이 associated bundle 구성과 교환하므로

$$S^2_{S^1}=ES^1\times_{S^1}\mathbb{P}(\mathbb{C}_0\oplus\mathbb{C}_1)=\mathbb{P}(L_0\oplus L_1)$$

이다. 여기서 $L_a=ES^1\times_{S^1}\mathbb{C}_a$이고, $H^\bullet(BS^1)=\mathbb{Z}[t]$ 안에서 $c_1(L_0)=0$, $c_1(L_1)=t$이다. ([명제 4](#prop4)) 따라서 [명제 5](#prop5)에 의해

$$H_{S^1}^\bullet(S^2)=\mathbb{Z}[t][h]\big/\big((h-0)(h-t)\big)=\mathbb{Z}[t][h]/(h^2-th)$$

이고, 이는 $\{1,h\}$를 기저로 갖는 free $\mathbb{Z}[t]$-가군이다 ($\lvert t\rvert=\lvert h\rvert=2$).

이 결과를 naive quotient와 대조하자. 앞서 보았듯 $S^2/S^1\cong[-1,1]$은 contractible이므로 $H^\bullet(S^2/S^1)=\mathbb{Z}$로 $0$차에만 남는다. 반면 $H_{S^1}^\bullet(S^2)$은 rank $2$의 free $\mathbb{Z}[t]$-가군으로, $S^2$의 위상을 ($2$라는 rank가 $H^\bullet(S^2)$의 차원과 같다는 점에서) 그리고 회전 작용을 (관계식 $h^2-th$에 나타나는 두 fixed point의 weight $0,1$을 통해) 모두 기억한다. 실제로 restriction $\iota^\ast:H_{S^1}^\bullet(S^2)\rightarrow H^\bullet(S^2)$은 $t=0$을 대입하는 것에 해당하여 ([명제 2](#prop2)의 (3))

$$\mathbb{Z}[t][h]/(h^2-th)\xrightarrow{t\mapsto 0}\mathbb{Z}[h]/(h^2)=H^\bullet(S^2)$$

를 준다.

이 계산에서 정작 비자명한 정보는 fixed point로의 restriction에 담겨 있다.

::: 예시 6
위 회전하는 $S^2$에서 두 fixed point $p_0,p_1\hookrightarrow S^2$의 포함은

$$H_{S^1}^\bullet(S^2)\rightarrow H_{S^1}^\bullet(p_0)\oplus H_{S^1}^\bullet(p_1)=\mathbb{Z}[t]\oplus\mathbb{Z}[t]$$

로의 restriction을 준다. $h$가 $\mathcal{O}(-1)$의 Chern class이므로 각 fixed point에서 그 값은 그 점의 representation이 갖는 weight, 곧 $h\mapsto(0,t)$이다. 그럼 관계식의 좌변은 $h^2-th\mapsto(0\cdot(0-t),t(t-t))=(0,0)$으로 사라져 일관성이 확인된다. 두 성분을 함께 보면 $1\mapsto(1,1)$, $h\mapsto(0,t)$이므로 이 restriction은 $t$를 가역으로 만든 뒤에는 단사가 되며, 곧 $H_{S^1}^\bullet(S^2)$이 두 fixed point에서의 값으로 거의 결정된다.
:::

Fixed point로의 restriction이 $H_T^\bullet$을 거의 결정한다는 이 현상이 다음 글에서 다룰 localization의 출발점이다.

## 예시: 사영공간

이제 표준적인 torus 작용을 갖는 $\mathbb{P}^n$의 equivariant cohomology를 계산한다. 이것이 이 글의 중심 계산이며, 동시에 다음에 정의할 equivariant formality의 대표적인 예가 된다.

::: 정리 7
$T=(S^1)^{n+1}$이 $\mathbb{C}^{n+1}$ 위에 좌표별 곱

$$(\lambda_0,\ldots,\lambda_n)\cdot(z_0,\ldots,z_n)=(\lambda_0 z_0,\ldots,\lambda_n z_n)$$

으로 작용하여 유도하는 $\mathbb{P}^n$ 위의 작용에 대하여,

$$H_T^\bullet(\mathbb{P}^n)=\mathbb{Z}[t_0,\ldots,t_n][h]\Big/\prod_{i=0}^n(h-t_i)$$

이다. 이는 $1,h,\ldots,h^n$을 기저로 갖는 free $\mathbb{Z}[t_0,\ldots,t_n]$-가군이다.
:::
::: 증명
$\mathbb{C}^{n+1}$의 $i$번째 좌표선은 $i$번째 좌표 character $t_i\in M=\mathrm{Hom}(T,S^1)$에 대한 일차원 representation $\mathbb{C}_{t_i}$이므로, $T$-representation으로서

$$\mathbb{C}^{n+1}=\bigoplus_{i=0}^n\mathbb{C}_{t_i}$$

이고 $\mathbb{P}^n=\mathbb{P}\big(\bigoplus_i\mathbb{C}_{t_i}\big)$이다. Projectivization이 associated bundle과 교환하므로

$$\mathbb{P}^n_T=ET\times_T\mathbb{P}\Big(\bigoplus_i\mathbb{C}_{t_i}\Big)=\mathbb{P}\Big(\bigoplus_{i=0}^n L_i\Big),\qquad L_i=ET\times_T\mathbb{C}_{t_i}$$

이다. [명제 4](#prop4)에 의해 $c_1(L_i)=t_i\in H^2(BT)=\bigoplus_i\mathbb{Z}t_i$이므로, $E=\bigoplus_i L_i$에 [명제 5](#prop5)를 적용하면 $h=c_1(\mathcal{O}(-1))$에 대하여

$$H_T^\bullet(\mathbb{P}^n)=H^\bullet(\mathbb{P}^n_T)=\mathbb{Z}[t_0,\ldots,t_n][h]\Big/\prod_{i=0}^n(h-t_i)$$

를 얻으며, 같은 명제로부터 이것이 $1,h,\ldots,h^n$을 기저로 갖는 free $\mathbb{Z}[t_0,\ldots,t_n]$-가군임이 따라온다.
:::

관계식을 전개하면

$$\prod_{i=0}^n(h-t_i)=h^{n+1}-e_1 h^n+e_2 h^{n-1}-\cdots+(-1)^{n+1}e_{n+1}$$

이며, 여기서 $e_j=e_j(t_0,\ldots,t_n)$은 $j$번째 elementary symmetric polynomial이다. 이 식에서 $t_i$를 모두 $0$으로 보내는 restriction $\iota^\ast$은 ([명제 2](#prop2)의 (3))

$$\mathbb{Z}[t_0,\ldots,t_n][h]\Big/\prod_{i}(h-t_i)\xrightarrow{t_i\mapsto 0}\mathbb{Z}[h]/(h^{n+1})=H^\bullet(\mathbb{P}^n)$$

을 주어, equivariant cohomology가 보통의 cohomology $H^\bullet(\mathbb{P}^n)=\mathbb{Z}[h]/(h^{n+1})$를 정확히 변형한 것임을 보여 준다. 한편 대각 $S^1\subseteq T$은 $\mathbb{P}^n$ 위에 자명하게 작용하지만, equivariant cohomology를 풍부하게 만들기 위해서는 효과적이지 않은 이 부분까지 포함한 full torus $T=(S^1)^{n+1}$을 쓰는 것이 자연스럽다. 관계식은 $n+1$개의 fixed point $p_i=[0:\cdots:1:\cdots:0]$에서 $h$가 각각 $t_i$로 제한된다는 사실을 기억하고 있다.

## Equivariant formality

위 두 계산의 공통된 특징은 $H_T^\bullet(X)$이 $H_T^\bullet(\mathrm{pt})$ 위의 free 가군이고, $t_i=0$을 대입하면 정확히 $H^\bullet(X)$가 회복된다는 점이었다. 이 성질은 모든 작용에서 성립하지는 않으나, 성립할 때는 equivariant cohomology와 ordinary cohomology의 관계가 가장 단순해진다.

::: 정의 8
Torus $T$가 작용하는 공간 $X$ (cohomology가 각 degree에서 finitely generated)가 *equivariantly formal<sub>동변 형식적</sub>*이라는 것은 $H_T^\bullet(X)$이 $H_T^\bullet(\mathrm{pt})$ 위의 free 가군이고, augmentation $H_T^\bullet(\mathrm{pt})\rightarrow\mathbb{Z}$ (양의 degree를 $0$으로 보내는 morphism) 에 대하여 자연스러운 morphism

$$H_T^\bullet(X)\otimes_{H_T^\bullet(\mathrm{pt})}\mathbb{Z}\xrightarrow{\cong}H^\bullet(X)$$

이 동형인 것이다.
:::

여기서 오른쪽으로 가는 morphism은 [명제 2](#prop2)의 restriction $\iota^\ast$이 유도하는 것이다. [예시 6](#ex6)의 $S^2$와 [정리 7](#thm7)의 $\mathbb{P}^n$은 모두 equivariantly formal이다. 두 경우 모두 $H_T^\bullet(X)$이 $h$의 거듭제곱을 free 기저로 가졌고, $t_i\mapsto 0$이 $H^\bullet(X)$를 회복하였기 때문이다. 더 일반적으로 fiber bundle $X\rightarrow X_T\rightarrow BT$의 Serre spectral sequence

$$E_2^{p,q}=H^p\big(BT;H^q(X)\big)\Longrightarrow H_T^{p+q}(X)$$

를 생각하면, equivariant formality는 이 spectral sequence가 $E_2$ 면에서 collapse하는 것과 동치이다. 이 경우 $H_T^\bullet(X)$은 $H^\bullet(BT)$-가군으로서 $H^\bullet(X)\otimes_{\mathbb{Z}}H^\bullet(BT)$와 동형이 된다. Cohomology가 짝수 degree에만 있는 공간 (가령 cell이 모두 짝수 차원인 CW complex로, $\mathbb{P}^n$이나 일반적인 smooth projective toric variety가 이에 속한다) 은 degree의 parity 때문에 미분이 모두 사라져 항상 equivariantly formal이다. 이 freeness가 fixed point로의 restriction을 거의 단사로 만들어, 다음 글에서 다룰 localization 정리를 통한 계산을 가능하게 한다.

::: 참고 9
$X$가 smooth variety이고 $G$가 compact Lie group으로 매끄럽게 작용할 때는, 위의 위상적 Borel 구성과 같은 $H_G^\bullet(X;\mathbb{R})$을 differential form으로 계산하는 model이 존재한다. Cartan model에서는 equivariant differential form의 복합체

$$\Omega_G^\bullet(X)=\big(\mathrm{Sym}(\mathfrak{g}^\ast)\otimes\Omega^\bullet(X)\big)^G$$

와 그 위의 equivariant 미분 $d_G$을 사용하며, Weil model은 $EG$ 위의 connection과 그 curvature를 명시적으로 도입한다. 이들은 Lie algebra $\mathfrak{g}$와 connection 데이터를 필요로 하므로 smooth 범주에 한정된다. 우리는 임의의 topological group과 임의의 paracompact space에 적용되는 위상적 Borel model만을 사용한다. 두 model의 동치성과 de Rham 판본의 자세한 전개는 [AB]와 [GS]를 따른다.
:::

---

**참고문헌**

**[AF]** D. Anderson and W. Fulton, *Equivariant Cohomology in Algebraic Geometry*, Cambridge Studies in Advanced Mathematics 210, Cambridge University Press, 2023.

**[AB]** M. F. Atiyah and R. Bott, *The moment map and equivariant cohomology*, Topology **23** (1984), 1–28.

**[GS]** V. W. Guillemin and S. Sternberg, *Supersymmetry and Equivariant de Rham Theory*, Springer, 1999.

**[tD]** T. tom Dieck, *Algebraic Topology*, EMS Textbooks in Mathematics, European Mathematical Society, 2008.
