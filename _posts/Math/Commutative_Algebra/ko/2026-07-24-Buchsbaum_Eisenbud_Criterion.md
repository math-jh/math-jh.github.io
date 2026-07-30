---
title: "Buchsbaum-Eisenbud 판정법"
description: "유한 자유복합체의 exactness가 각 행렬의 rank 등식과 소행렬식 아이디얼의 grade 조건만으로 판정된다는 Buchsbaum-Eisenbud 정리를 McCoy 정리와 Peskine-Szpiro acyclicity 보조정리로부터 증명하고, 응용으로 projective dimension 2인 아이디얼의 자유분해를 결정하는 Hilbert-Burch 정리를 다룬다."
excerpt: "Free complex의 exactness 판정과 Hilbert-Burch 정리"

categories: [Math / Commutative Algebra]
permalink: /ko/math/commutative_algebra/buchsbaum_eisenbud_criterion
sidebar: 
    nav: "commutative_algebra-ko"

date: 2026-07-24
weight: 30
published: false
drift_needed: true

---

[§Fitting 아이디얼](/ko/math/commutative_algebra/fitting_ideals)의 끝에서 우리는 free resolution의 각 행렬에서 뽑은 소행렬식 ideal의 depth가 complex의 exactness 자체를 판정한다고 예고하였다. 이 판정이 Buchsbaum과 Eisenbud의 1973년 논문 "What makes a complex exact?"의 주정리이다. 이 글에서 우리는 free module 사이의 map의 rank를 소행렬식 ideal로 정의하고, McCoy의 정리와 Peskine--Szpiro의 acyclicity 보조정리를 준비한 뒤 이 판정법을 증명한다. 응용으로는 regular sequence의 Koszul complex의 exactness를 판정법으로 재확인하고, projective dimension이 $2$인 ideal의 free resolution이 한 행렬의 소행렬식들로 완전히 결정된다는 Hilbert--Burch 정리를 다룬다.

## 자유복합체와 rank

이 글 전체에서 $A$는 Noetherian ring이다. 우리의 대상은 유한한 free complex, 곧 각 항이 finitely generated free module인 다음의 chain complex

$$F_\bullet:\quad 0 \rightarrow F_n\overset{\varphi_n}{\longrightarrow}F_{n-1}\overset{\varphi_{n-1}}{\longrightarrow}\cdots\overset{\varphi_2}{\longrightarrow}F_1\overset{\varphi_1}{\longrightarrow}F_0$$

이다. 목표는 이 complex가 언제 exact인지, 곧 언제 각각의 $1\leq i\leq n$에서 $H_i(F_\bullet)=0$인지를 ([\[호몰로지 대수학\] §호몰로지, ⁋정의 2](/ko/math/homological_algebra/homology#def2)) $\varphi_i$들의 행렬 자료만으로 판정하는 것이다. 여기서 행렬 자료란 [§Fitting 아이디얼, ⁋정의 1](/ko/math/commutative_algebra/fitting_ideals#def1)에서 도입한 소행렬식 ideal $I_r(\varphi)$를 뜻한다. $\varphi:A^m \rightarrow A^n$을 표준 basis에 대한 $n\times m$ 행렬로 보면 ([\[다중선형대수학\] §행렬과 선형사상, ⁋정의 1](/ko/math/multilinear_algebra/matrices_and_linear_maps#def1)), $1\leq r\leq \min(m,n)$에서 $I_r(\varphi)$는 $r\times r$ 소행렬식들이 생성하는 ideal이고, $r\leq 0$이면 $I_r(\varphi)=A$, $r>\min(m,n)$이면 $I_r(\varphi)=0$이며, 언제나 $I_{r+1}(\varphi)\subseteq I_r(\varphi)$이다. ([§Fitting 아이디얼, ⁋정의 1](/ko/math/commutative_algebra/fitting_ideals#def1) 직후의 포함관계)

::: 정의 1
Free module 사이의 $A$-linear map $\varphi:A^m \rightarrow A^n$에 대하여, $\varphi$의 *rank*와 ideal $I(\varphi)$를 다음의 식

$$\rank\varphi=\max\{r\geq 0\mid I_r(\varphi)\neq 0\},\qquad I(\varphi)=I_{\rank\varphi}(\varphi)$$

으로 정의한다.
:::

$I_0(\varphi)=A\neq 0$이므로 $\rank\varphi$는 잘 정의되고 $0\leq \rank\varphi\leq\min(m,n)$이다. 특히 zero map은 rank $0$을 가지며, 이 때 $I(0)=I_0=A$이다. Field 위에서는 $r\times r$ 소행렬식이 전부 $0$인 것과 행렬의 보통의 rank가 $r$ 미만인 것이 동치이므로 이 정의는 선형대수학의 rank와 일치한다. 일반적인 ring 위에서 $\rank\varphi$는 말하자면 generic한 rank이고, ideal $I(\varphi)$는 이 rank가 어디에서 무너지는지를 기록하는 자료이다. 이 두 자료가 판정법의 전부가 된다.

첫 준비물은 unit 성분이 있는 행렬을 잘라내는 보조정리이다.

::: 보조정리 2
$\varphi:A^m \rightarrow A^n$의 행렬의 어떤 성분이 $A$의 unit이라 하자. 그럼 $A^m$과 $A^n$의 basis를 바꾸어 $\varphi$의 행렬을 block 행렬

$$\begin{pmatrix}1&0\\0&\varphi'\end{pmatrix},\qquad \varphi':A^{m-1} \rightarrow A^{n-1}$$

의 꼴로 만들 수 있으며, 이 때 모든 $r\geq 1$에 대하여 $I_r(\varphi)=I_{r-1}(\varphi')$이다.
:::
::: 증명
우선 basis 변경이 모든 $I_r$를 보존함을 확인한다. Basis 변경은 행렬 $X$를 invertible 행렬 $P,Q$에 대한 $PXQ$로 바꾼다. ([\[다중선형대수학\] §기저변환, ⁋명제 4](/ko/math/multilinear_algebra/change_of_basis#prop4), [\[다중선형대수학\] §기저변환, ⁋명제 5](/ko/math/multilinear_algebra/change_of_basis#prop5)) $PX$의 각 행은 $X$의 행들의 $A$-linear combination이므로, $PX$의 $r\times r$ 소행렬식을 행에 대한 multilinearity로 전개하면 $X$의 행 $r$개를 고른 행렬식들의 combination이 되고, 행이 겹치는 항은 alternating 성질로 소멸하므로 남는 항들은 $X$의 $r\times r$ 소행렬식들이다. 이는 [§Fitting 아이디얼, ⁋정리 3](/ko/math/commutative_algebra/fitting_ideals#thm3)의 증명에서 열에 대해 수행한 논증과 같다. 따라서 $I_r(PX)\subseteq I_r(X)$이고, $P$가 invertible이므로 반대 포함도 성립하며, 열에 대해서도 마찬가지이므로 $I_r(PXQ)=I_r(X)$이다.

이제 unit 성분을 basis vector들의 재배열로 $(1,1)$ 자리로 옮기고, target의 첫 basis vector를 unit배로 바꾸어 그 성분을 $1$로 만들자. 첫 열의 나머지 성분들은 첫 행을 다른 행에 더하는 elementary 연산으로, 첫 행의 나머지 성분들은 첫 열을 다른 열에 더하는 elementary 연산으로 소거할 수 있고, 이들은 모두 invertible 행렬을 곱하는 것이므로 basis 변경이다. 결과가 주어진 block 꼴이다.

마지막으로 block 행렬의 $r\times r$ 소행렬식을 분류하자. 첫 행과 첫 열을 모두 포함하는 소행렬식은 첫 행에 대해 전개하면 $\varphi'$의 $(r-1)\times(r-1)$ 소행렬식이고, 첫 행이나 첫 열 중 하나만 포함하는 것은 $0$인 행 또는 열을 가져 $0$이며, 둘 다 포함하지 않는 것은 $\varphi'$의 $r\times r$ 소행렬식이다. 따라서

$$I_r(\varphi)=I_{r-1}(\varphi')+I_r(\varphi')=I_{r-1}(\varphi')$$

이고, 마지막 등호는 포함관계 $I_r(\varphi')\subseteq I_{r-1}(\varphi')$에 의한 것이다.
:::

::: 따름정리 3
Noetherian local ring $(A,\mathfrak{m})$과 $\varphi:A^m \rightarrow A^n$, 그리고 $r\geq 1$에 대하여 $I_r(\varphi)=A$라 하자. 그럼 basis를 바꾸어 $\varphi$를 $\id_{A^r}\oplus\varphi''$의 꼴로 만들 수 있으며, 이 때 모든 $s\geq 1$에서 $I_s(\varphi'')=I_{r+s}(\varphi)$이다.
:::
::: 증명
$r$에 대한 귀납법을 사용한다. $I_r(\varphi)\subseteq I_1(\varphi)$이므로 $I_1(\varphi)=A$인데, $\varphi$의 모든 성분이 $\mathfrak{m}$에 속한다면 $I_1(\varphi)\subseteq\mathfrak{m}$이 되어 모순이므로 어떤 성분은 unit이다. [보조정리 2](#lem2)로 $\varphi$를 $\id_A\oplus\varphi'$의 꼴로 만들면 $I_{r-1}(\varphi')=I_r(\varphi)=A$이므로 귀납적 가정을 $\varphi'$에 적용할 수 있고, $r$번의 분할 끝에 $\varphi\cong\id_{A^r}\oplus\varphi''$과 $I_s(\varphi'')=I_{r+s}(\varphi)$를 얻는다.
:::

다음은 free module 사이 map의 injectivity를 소행렬식으로 판정하는 McCoy의 정리이다. Exactness 판정의 가장 낮은 단계, 곧 complex의 왼쪽 끝에서의 exactness가 이미 이 정리로 소행렬식의 언어로 옮겨진다.

::: 정리 4 (McCoy)
$A$-linear map $\varphi:A^m \rightarrow A^n$에 대하여, $\varphi$가 injective인 것은 $\ann_A(I_m(\varphi))=0$인 것과 동치이다.
:::
::: 증명
우선 $\ann_A(I_m(\varphi))=0$이라 가정하고 $v\in\ker\varphi$가 주어졌다 하자. $\varphi$의 행렬에서 $m$개의 행을 골라 만든 임의의 $m\times m$ 부분행렬 $\psi$에 대하여, $\varphi v=0$의 해당 행들을 읽으면 $\psi v=0$이다. 수반행렬은 $\operatorname{adj}(\psi)\psi=(\det\psi)I$를 만족하므로 ([§Fitting 아이디얼, ⁋명제 6](/ko/math/commutative_algebra/fitting_ideals#prop6)에서와 같이 [\[다중선형대수학\] §행렬식, ⁋명제 9](/ko/math/multilinear_algebra/determinants#prop9)의 증명의 항등식), 왼쪽에 $\operatorname{adj}(\psi)$를 곱하면 $(\det\psi)v=0$이다. 이러한 $\det\psi$들이 $I_m(\varphi)$를 생성하므로 $v$의 각 좌표 $v_j$는 $I_m(\varphi)v_j=0$을 만족하고, 곧 $v_j\in\ann(I_m(\varphi))=0$이다. 따라서 $v=0$이고 $\varphi$는 injective이다.

거꾸로 $0\neq a\in\ann(I_m(\varphi))$가 존재한다고 가정하고 $\ker\varphi\neq 0$을 보인다. 만일 $aI_1(\varphi)=0$이라면 $\varphi$의 모든 성분이 $a$를 죽이므로 $\varphi(ae_1)=0$인데, $ae_1$은 첫 좌표가 $a\neq 0$이라 $0$이 아니므로 끝난다. 이제 $aI_1(\varphi)\neq 0$이라 하고, $aI_r(\varphi)\neq 0$인 가장 큰 $r\geq 1$을 잡자. $a\in\ann(I_m(\varphi))$이므로 $r<m$이다. $a\delta\neq 0$인 $r\times r$ 소행렬식 $\delta$를 고정하고 그 행 집합을 $R$, 열 집합을 $C$라 하자. $r<m$이므로 $C$에 속하지 않는 열 $c_0$를 하나 택할 수 있다. $C\cup\{c_0\}$의 원소들을 $j_1<\cdots<j_{r+1}$로 나열하고, 각각의 $k$에 대하여 행 집합 $R$과 열 집합 $(C\cup\{c_0\})\setminus\{j_k\}$로 만든 $r\times r$ 소행렬식을 $\Delta_k$라 한 뒤

$$v=\sum_{k=1}^{r+1}(-1)^ka\Delta_ke_{j_k}\in A^m$$

으로 정의하자. $j_k=c_0$인 항의 계수는 $\pm a\delta\neq 0$이므로 $v\neq 0$이다. 이제 임의의 행 $i$에 대하여 $\varphi v$의 $i$번째 좌표는 $\sum_k(-1)^ka\Delta_k\varphi_{ij_k}$이다. $R$의 행들 아래에 $i$번째 행을 덧붙이고 열을 $j_1,\ldots,j_{r+1}$로 제한한 $(r+1)\times(r+1)$ 행렬을 $M_i$라 하면, 마지막 행에 대한 전개로

$$\det M_i=\sum_{k=1}^{r+1}(-1)^{(r+1)+k}\varphi_{ij_k}\Delta_k$$

이므로 $(\varphi v)_i=\pm a\det M_i$이다. 만일 $i\in R$이라면 $M_i$는 같은 행을 두 번 가지므로 $\det M_i=0$이고, $i\notin R$이라면 $\det M_i$는 행의 순서를 재배열하면 $\varphi$의 $(r+1)\times(r+1)$ 소행렬식에 부호를 붙인 것이므로 $r$의 최대성에 의하여 $a\det M_i=0$이다. 따라서 $\varphi v=0$이고 $\varphi$는 injective가 아니다.
:::

$m>n$인 경우 $I_m(\varphi)=0$이고 $\ann(0)=A\neq 0$이므로, 정리는 $A^m$이 $A^n$에 embed될 수 없다는 고전적인 사실을 포함한다. 앞으로 필요한 것은 대부분 다음의 특수한 경우이다. Local ring $(A,\mathfrak{m})$에서 $\varphi$가 injective인데 그 성분이 전부 $\mathfrak{m}$에 속한다면, $\mathfrak{m}$을 죽이는 $0$이 아닌 원소는 존재할 수 없다. 실제로 $s\mathfrak{m}=0$이고 $s\neq 0$이면 $\varphi(se_1)=s\cdot(\text{첫 열의 성분들})=0$이 되어 injectivity에 모순이기 때문이다.

이 관찰을 complex 전체에 적용하기 위해, [보조정리 2](#lem2)의 분할을 chain complex의 수준으로 끌어올린다.

::: 보조정리 5
Ring $A$ 위의 finite free complex $F_\bullet$과 $1\leq i\leq n$에 대하여 $\varphi_i$의 행렬의 어떤 성분이 unit이라 하자. 그럼 $F_i$와 $F_{i-1}$의 basis를 바꾸어 $F_\bullet$을 각 degree에서의 direct sum과 block 대각 differential로 이루어진 두 complex의 direct sum $D_\bullet\oplus F_\bullet'$으로 분해할 수 있다. 여기서 $D_\bullet$은 degree $i,i-1$에 $A$를 두고 그 사이를 $\id_A$로 이은 complex이며, $F_\bullet'$은 $F_j'=F_j$ ($j\neq i,i-1$), $F_i'\cong A^{n_i-1}$, $F_{i-1}'\cong A^{n_{i-1}-1}$인 finite free complex이다. 이 분해는 다음을 만족한다.

1. 모든 $j$에 대하여 $H_j(F_\bullet)\cong H_j(F_\bullet')$이다.
2. 모든 $r\geq 1$에 대하여 $I_r(\varphi_i)=I_{r-1}(\varphi_i')$이고, $j\neq i$인 경우 $I_r(\varphi_j)=I_r(\varphi_j')$이다.
:::
::: 증명
[보조정리 2](#lem2)를 $\varphi_i$에 적용하여 $F_i$의 basis $e_1',\ldots,e_{n_i}'$와 $F_{i-1}$의 basis $f_1',\ldots,f_{n_{i-1}}'$를 잡되, $\varphi_i(e_1')=f_1'$이고 $\varphi_i$가 $e_2',\ldots$의 span $F_i'$를 $f_2',\ldots$의 span $F_{i-1}'$로 보내도록 하자. 이 $F_i' \rightarrow F_{i-1}'$의 restriction이 $\varphi_i'$이며, 둘째 주장의 앞부분은 [보조정리 2](#lem2)가 준다.

인접한 differential들이 이 분해와 호환됨을 본다. 임의의 $g\in F_{i+1}$에 대하여 $\varphi_{i+1}(g)=\alpha(g)e_1'+\beta(g)$ ($\beta(g)\in F_i'$)로 적으면, $\varphi_i\varphi_{i+1}=0$으로부터 $\alpha(g)f_1'+\varphi_i'(\beta(g))=0$인데 $f_1'$과 $F_{i-1}'$은 direct sum을 이루므로 $\alpha(g)=0$이고 $\varphi_i'(\beta(g))=0$이다. 곧 $\varphi_{i+1}$은 $F_i'$에 값을 가지며, 새 basis에 대한 행렬은 첫 행이 $0$이다. 마찬가지로 $\varphi_{i-1}(f_1')=\varphi_{i-1}\varphi_i(e_1')=0$이므로 $\varphi_{i-1}$의 새 basis에 대한 행렬은 첫 열이 $0$이고, $F_{i-1}'$로의 restriction이 잘 정의된다. 따라서 $F_\bullet$은 $Ae_1' \rightarrow Af_1'$ 부분과 나머지 부분의 direct sum으로 분해된다. $0$인 행 혹은 열을 지우는 것은 소행렬식 ideal을 바꾸지 않으므로 (그 행이나 열을 쓰는 소행렬식은 $0$이다) 둘째 주장의 나머지가 성립한다.

첫째 주장의 경우, direct sum complex의 kernel과 image는 성분별로 갈라지므로 $H_j(F_\bullet)\cong H_j(D_\bullet)\oplus H_j(F_\bullet')$인데, $D_\bullet$의 differential이 isomorphism이라 $H_j(D_\bullet)=0$이기 때문이다.
:::

이 소거를 반복하면, local ring 위의 finite free complex는 homology와 소행렬식 자료를 보존하면서 모든 differential의 성분이 $\mathfrak{m}$에 속하는 *minimal*한 것으로 축소된다. 이 축소가 판정법 증명의 엔진이다.

## Grade와 Peskine-Szpiro acyclicity

판정법의 조건을 서술할 불변량은 ideal이 품은 regular sequence의 길이이다. [§Depth, ⁋정의 3](/ko/math/commutative_algebra/depth#def3)에서 우리는 proper ideal $\mathfrak{a}$에 대하여 $\mathfrak{a}$ 안의 maximal $A$-sequence의 공통의 길이 $\operatorname{depth}_\mathfrak{a}(A)$를 정의하였다.

::: 정의 6
Noetherian ring $A$의 proper ideal $\mathfrak{a}$에 대하여, $\mathfrak{a}$의 *grade*를

$$\operatorname{grade}(\mathfrak{a})=\operatorname{depth}_\mathfrak{a}(A)$$

로 정의한다. 또, $\operatorname{grade}(A)=\infty$로 약속한다.
:::

이 값을 문헌에서는 흔히 $\mathfrak{a}$의 grade라 부르며, 우리는 $\operatorname{depth}_\mathfrak{a}(A)$와 병용한다. [§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)에 의하여 $\operatorname{grade}(\mathfrak{a})=\min\{i\mid\Ext_A^i(A/\mathfrak{a},A)\neq 0\}$이고, 특히 proper ideal의 grade는 유한하다. $\operatorname{grade}(A)=\infty$ 관례는 뒤에서 판정법의 조건을 예외 없이 서술하기 위한 것이다. 같은 이유로 이 글에서는 zero module의 depth를 $\infty$로 약속한다. Local ring $(A,\mathfrak{m})$의 proper ideal $\mathfrak{a}$의 경우 $\mathfrak{a}$ 안의 $A$-sequence는 $\mathfrak{m}$ 안의 $A$-sequence이고 maximal한 것으로 연장되므로, 언제나 $\operatorname{grade}(\mathfrak{a})\leq\operatorname{depth}A$이다.

Grade는 다음과 같이 국소적인 depth들의 최솟값으로 계산된다.

::: 보조정리 7
Noetherian ring $A$의 proper ideal $\mathfrak{a}$에 대하여 다음의 등식

$$\operatorname{grade}(\mathfrak{a})=\min\{\operatorname{depth}A_\mathfrak{p}\mid \mathfrak{p}\in V(\mathfrak{a})\}$$

이 성립한다. 여기서 $V(\mathfrak{a})$는 $\mathfrak{a}$를 포함하는 prime ideal들의 집합이다.
:::
::: 증명
$g=\operatorname{grade}(\mathfrak{a})$라 하고 $\mathfrak{a}$ 안의 maximal $A$-sequence $x_1,\ldots,x_g$를 고정하자.

우선 임의의 $\mathfrak{p}\in V(\mathfrak{a})$에 대하여 $\operatorname{depth}A_\mathfrak{p}\geq g$임을 보인다. 각각의 $k$에서 곱하기 $x_{k+1}$은 $A/(x_1,\ldots,x_k)$ 위에서 injective이고, localization은 exact이므로 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 곱하기 $x_{k+1}$은 $A_\mathfrak{p}/(x_1,\ldots,x_k)A_\mathfrak{p}$ 위에서도 injective이다. 또 $(x_1,\ldots,x_k)A_\mathfrak{p}\subseteq\mathfrak{a}A_\mathfrak{p}\subseteq\mathfrak{p}A_\mathfrak{p}$는 proper이므로 이 quotient들은 $0$이 아니다. 따라서 $x_1,\ldots,x_g$의 image들은 $\mathfrak{p}A_\mathfrak{p}$ 안의 $A_\mathfrak{p}$-sequence이고, 이를 maximal한 것으로 연장하면 [§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)에 의하여 $\operatorname{depth}A_\mathfrak{p}\geq g$이다.

이제 등호가 성립하는 $\mathfrak{p}$를 찾는다. Sequence의 maximality에 의하여 임의의 $y\in\mathfrak{a}$는 $A/(x_1,\ldots,x_g)$의 zerodivisor인데, $(x_1,\ldots,x_g,y)\subseteq\mathfrak{a}$가 proper이므로 sequence 조건이 실패하는 이유는 이것뿐이기 때문이다. 그럼 [§Depth, ⁋보조정리 1](/ko/math/commutative_algebra/depth#lem1)을 module $A/(x_1,\ldots,x_g)\neq 0$에 적용하여 $\mathfrak{a}\subseteq\mathfrak{p}$인 $\mathfrak{p}\in\Ass_A(A/(x_1,\ldots,x_g))$를 얻는다. $(x)=(x_1,\ldots,x_g)$로 줄여 적고 $\mathfrak{p}=\ann_A(z+(x))$인 $z$를 고정하자. 우리는 $z/1\notin(x)A_\mathfrak{p}$이고 $\mathfrak{p}A_\mathfrak{p}=\ann_{A_\mathfrak{p}}(z/1+(x)A_\mathfrak{p})$임을 주장한다. 실제로 $z/1\in(x)A_\mathfrak{p}$라면 적당한 $s\notin\mathfrak{p}$에 대하여 $sz\in(x)$이고, 곧 $s\in\ann(z+(x))=\mathfrak{p}$가 되어 모순이다. 포함 $\subseteq$는 $\mathfrak{p}z\subseteq(x)$를 localize한 것이고, 거꾸로 $(a/s)(z/1)\in(x)A_\mathfrak{p}$라면 적당한 $u\notin\mathfrak{p}$에 대하여 $uaz\in(x)$이므로 $ua\in\mathfrak{p}$, 곧 $a\in\mathfrak{p}$이다. 따라서 $\mathfrak{p}A_\mathfrak{p}\in\Ass_{A_\mathfrak{p}}(A_\mathfrak{p}/(x)A_\mathfrak{p})$이고, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 첫째 결과에 의하여 $\operatorname{depth}_{A_\mathfrak{p}}(A_\mathfrak{p}/(x)A_\mathfrak{p})=0$이다. 한편 앞 문단에서 본 것처럼 $x_1,\ldots,x_g$는 $\mathfrak{p}A_\mathfrak{p}$ 안의 $A_\mathfrak{p}$-sequence이므로, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 둘째 결과를 반복하면

$$\operatorname{depth}A_\mathfrak{p}=g+\operatorname{depth}_{A_\mathfrak{p}}(A_\mathfrak{p}/(x)A_\mathfrak{p})=g$$

를 얻는다. 두 문단을 종합하면 원하는 최솟값 공식이 성립한다.
:::

::: 따름정리 8
Noetherian ring $A$의 ideal $\mathfrak{a}$에 대하여 다음이 성립한다.

1. 정수 $k$에 대하여, $\operatorname{grade}(\mathfrak{a})\geq k$인 것은 모든 $\mathfrak{p}\in V(\mathfrak{a})$에서 $\operatorname{depth}A_\mathfrak{p}\geq k$인 것과 동치이다.
2. $\mathfrak{a}$를 포함하는 임의의 prime ideal $\mathfrak{q}$에 대하여 $\operatorname{grade}(\mathfrak{a}A_\mathfrak{q})\geq\operatorname{grade}(\mathfrak{a})$이다.
3. $\mathfrak{a}$가 proper이고 $x\in\mathfrak{a}$가 non-zerodivisor라면, $\overline{A}=A/(x)$에서 $\operatorname{grade}(\mathfrak{a})=1+\operatorname{grade}(\mathfrak{a}\overline{A})$이다.
:::
::: 증명
첫째 결과는 $\mathfrak{a}$가 proper이면 [보조정리 7](#lem7)이고, $\mathfrak{a}=A$이면 $V(\mathfrak{a})=\emptyset$이라 양쪽 모두 아무 조건이 아니므로 성립한다.

둘째 결과를 보이자. $A_\mathfrak{q}$의 prime ideal은 $\mathfrak{p}\subseteq\mathfrak{q}$인 prime $\mathfrak{p}$에 대한 $\mathfrak{p}A_\mathfrak{q}$들이고 ([§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)), $\mathfrak{p}A_\mathfrak{q}\supseteq\mathfrak{a}A_\mathfrak{q}$인 것은 $\mathfrak{p}\supseteq\mathfrak{a}$인 것과 같다. 이 때 $(A_\mathfrak{q})_{\mathfrak{p}A_\mathfrak{q}}\cong A_\mathfrak{p}$이다. 실제로 canonical map $A \rightarrow(A_\mathfrak{q})_{\mathfrak{p}A_\mathfrak{q}}$는 $s\notin\mathfrak{p}$를 unit으로 보내므로 ($s/1\notin\mathfrak{p}A_\mathfrak{q}$는 [§국소화, ⁋명제 8](/ko/math/commutative_algebra/localization#prop8)의 contraction 계산) [§국소화, ⁋명제 6](/ko/math/commutative_algebra/localization#prop6)이 ring homomorphism $A_\mathfrak{p} \rightarrow(A_\mathfrak{q})_{\mathfrak{p}A_\mathfrak{q}}$를 주고, 이는 분모들을 직접 정리하면 surjective이며, $a/1$이 $0$으로 가면 $cba=0$인 $c\notin\mathfrak{q}$, $b\notin\mathfrak{p}$가 있어 $cb\notin\mathfrak{p}$이므로 injective이다. 그럼 [보조정리 7](#lem7)을 $A_\mathfrak{q}$에 적용하면

$$\operatorname{grade}(\mathfrak{a}A_\mathfrak{q})=\min\{\operatorname{depth}A_\mathfrak{p}\mid\mathfrak{p}\in V(\mathfrak{a}),\ \mathfrak{p}\subseteq\mathfrak{q}\}\geq\min\{\operatorname{depth}A_\mathfrak{p}\mid\mathfrak{p}\in V(\mathfrak{a})\}=\operatorname{grade}(\mathfrak{a})$$

이다. ($\mathfrak{a}A_\mathfrak{q}=A_\mathfrak{q}$인 경우는 좌변이 $\infty$라 자명하다.)

셋째 결과를 보이자. [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)의 둘째 결과를 $M=A$에 적용하면 $\operatorname{depth}_\mathfrak{a}(A/xA)=\operatorname{grade}(\mathfrak{a})-1$이다. 한편 $\mathfrak{a}$의 원소는 $A$-module $\overline{A}$ 위에 그 image를 통해 작용하므로, $\mathfrak{a}$의 원소들로 이루어진 $\overline{A}$-sequence와 $\mathfrak{a}\overline{A}$의 원소들로 이루어진 $\overline{A}$-sequence는 image를 취하는 대응으로 정확히 일치하며 ($\mathfrak{a}\overline{A}$의 임의의 원소는 $\mathfrak{a}$의 원소로 lift된다), 대응되는 두 sequence의 quotient module들과 곱셈의 injectivity가 같으므로 maximality도 보존된다. 따라서 $\operatorname{depth}_\mathfrak{a}(A/xA)=\operatorname{depth}_{\mathfrak{a}\overline{A}}(\overline{A})=\operatorname{grade}(\mathfrak{a}\overline{A})$이고, 앞의 식과 종합하면 원하는 등식을 얻는다. ($x\in\mathfrak{a}$이므로 $\mathfrak{a}\overline{A}$는 proper이다.)
:::

판정법 증명의 마지막 준비물은 depth 조건이 homology의 소멸을 강제한다는 Peskine--Szpiro의 acyclicity 보조정리이다.

::: 보조정리 9 (Peskine--Szpiro acyclicity lemma)
Noetherian local ring $(A,\mathfrak{m})$ 위의 finitely generated module들의 유한 complex

$$0 \rightarrow M_s\overset{d_s}{\longrightarrow}M_{s-1}\overset{d_{s-1}}{\longrightarrow}\cdots\overset{d_2}{\longrightarrow}M_1\overset{d_1}{\longrightarrow}M_0\qquad(s\geq 1)$$

가 각각의 $1\leq i\leq s$에서 $\operatorname{depth}M_i\geq i$를 만족한다 하자. 만일 각각의 $i\geq 1$에서 homology $H_i$가 $0$이거나 $\operatorname{depth}H_i=0$이라면, 모든 $i\geq 1$에서 $H_i=0$이다.
:::
::: 증명
결론에 반하여 $H_q\neq 0$인 가장 큰 $1\leq q\leq s$가 존재한다고 하자. 그럼 가정에 의하여 $\operatorname{depth}H_q=0$이다. $B_i=\im d_{i+1}$, $Z_i=\ker d_i$로 적자 ($d_{s+1}=0$).

우선 $\operatorname{depth}Z_q\geq 1$임을 본다. $Z_q=0$이면 $H_q=0$이 되어 모순이므로 $Z_q\neq 0$이다. $\operatorname{depth}M_q\geq q\geq 1$이므로 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)에 의하여 $\mathfrak{m}\notin\Ass M_q$이고, $Z_q$는 $M_q$의 submodule이므로 $\Ass Z_q\subseteq\Ass M_q$이다. ([§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)) 따라서 $\mathfrak{m}\notin\Ass Z_q$이고, 다시 [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)에 의하여 $\operatorname{depth}Z_q\geq 1$이다.

만일 $B_q=0$이라면 $H_q=Z_q$이므로 $\operatorname{depth}H_q\geq 1$이 되어 $\operatorname{depth}H_q=0$과 모순이고, 증명이 끝난다. 이제 $B_q\neq 0$이라 하자. 특히 $B_s=\im d_{s+1}=0$이므로 $q<s$이다. 우리는 $q\leq j\leq s-1$에서 $B_j\neq 0$인 한 $\operatorname{depth}B_j\geq j+1$임을 $j$에 대한 내림 귀납법으로 보인다. $j>q$인 구간에서는 $H_j=0$이므로 $Z_j=B_j$이다. $j=s-1$의 경우, $Z_s=B_s=0$이라 $d_s$가 injective이므로 $B_{s-1}\cong M_s$이고 $\operatorname{depth}B_{s-1}\geq s$이다. $q\leq j<s-1$의 경우, $Z_{j+1}=B_{j+1}$로부터 short exact sequence

$$0 \rightarrow B_{j+1} \rightarrow M_{j+1} \rightarrow B_j \rightarrow 0$$

을 얻는다. $B_{j+1}=0$이면 $B_j\cong M_{j+1}$이라 $\operatorname{depth}B_j\geq j+1$이고, $B_{j+1}\neq 0$이면 귀납적 가정 $\operatorname{depth}B_{j+1}\geq j+2$와 [§Depth, ⁋명제 10](/ko/math/commutative_algebra/depth#prop10)의 셋째 부등식으로

$$\operatorname{depth}B_j\geq\min(\operatorname{depth}B_{j+1}-1,\operatorname{depth}M_{j+1})\geq\min(j+1,j+1)=j+1$$

이다. 특히 $\operatorname{depth}B_q\geq q+1\geq 2$이다.

이제 short exact sequence $0 \rightarrow B_q \rightarrow Z_q \rightarrow H_q \rightarrow 0$에 [§Depth, ⁋명제 10](/ko/math/commutative_algebra/depth#prop10)의 셋째 부등식을 적용하면

$$\operatorname{depth}H_q\geq\min(\operatorname{depth}B_q-1,\operatorname{depth}Z_q)\geq\min(q,1)\geq 1$$

인데, 이는 $\operatorname{depth}H_q=0$과 모순이다.
:::

이 보조정리에서 module들의 depth 조건은 complex의 왼쪽으로 갈수록 강해진다. 판정법의 grade 조건 $\operatorname{grade}I(\varphi_i)\geq i$가 정확히 같은 기울기를 갖는 것은 우연이 아니며, 아래 증명에서 두 조건이 맞물리는 것을 보게 된다.

## Buchsbaum-Eisenbud 판정법

이제 이 글의 주정리를 증명한다.

::: 정리 10 (Buchsbaum--Eisenbud)
Noetherian ring $A$ 위의 finite free complex

$$F_\bullet:\quad 0 \rightarrow F_n\overset{\varphi_n}{\longrightarrow}F_{n-1}\overset{\varphi_{n-1}}{\longrightarrow}\cdots\overset{\varphi_2}{\longrightarrow}F_1\overset{\varphi_1}{\longrightarrow}F_0$$

가 주어졌다 하고, 각각의 $F_i$는 rank $n_i$의 free module이며 $\varphi_{n+1}=0$이라 하자. 그럼 다음이 동치이다.

1. $F_\bullet$은 exact이다. 곧 각각의 $1\leq i\leq n$에서 $H_i(F_\bullet)=0$이다.
2. 각각의 $1\leq i\leq n$에서 $\rank\varphi_i+\rank\varphi_{i+1}=n_i$이고 $\operatorname{grade}I(\varphi_i)\geq i$이다.
:::
::: 증명
정수들 $r_i=\sum_{k=i}^n(-1)^{k-i}n_k$ ($1\leq i\leq n+1$, 특히 $r_{n+1}=0$)를 도입하면 $r_i+r_{i+1}=n_i$이다. 조건 (2)의 rank 등식들은 모든 $i$에서 $\rank\varphi_i=r_i$인 것과 동치이다. 실제로 후자가 성립하면 rank 등식들은 $r_i+r_{i+1}=n_i$이고, 거꾸로 rank 등식들이 성립하면 $\rank\varphi_{n+1}=0=r_{n+1}$에서 시작하여 $\rank\varphi_i=n_i-\rank\varphi_{i+1}$로 내려오는 귀납으로 $\rank\varphi_i=r_i$를 얻기 때문이다. 또, 임의의 ring homomorphism $A \rightarrow B$에 대하여 $I_r(\varphi\otimes_AB)=I_r(\varphi)B$임을 기억해 두자. ([§Fitting 아이디얼, ⁋명제 5](/ko/math/commutative_algebra/fitting_ideals#prop5)의 증명) 특히 소행렬식 ideal은 localization과 교환한다.

[(1)$\Rightarrow$(2)] 우선 $\mathfrak{p}\in\Ass A$를 고정하고 $B=A_\mathfrak{p}$로 localize한 complex $(F_\bullet)_\mathfrak{p}$를 분석한다. Localization은 exact이므로 ([§국소화의 성질들, ⁋명제 2](/ko/math/commutative_algebra/properties_of_localization#prop2)) 이 complex는 exact이다. $\mathfrak{p}=\ann_A(z)$로 적으면 [보조정리 7](#lem7)의 증명의 localization 논증을 $(x)=0$인 경우에 적용하여 $\mathfrak{p}B=\ann_B(z/1)$이고 $z/1\neq 0$임을 알며, 곧 $\mathfrak{p}B\in\Ass B$이므로 $\mathfrak{p}B\cdot s=0$인 $s\neq 0$이 존재한다. 이제 degree $1$ 이상의 항들의 rank의 합이 $0$이 될 때까지 [보조정리 5](#lem5)의 소거를 반복할 수 있음을 주장한다. 현재 complex에서 degree $i\geq 1$의 항이 $0$이 아닌 가장 큰 $i$를 잡으면, $i$의 최대성과 exactness에 의하여 $i$번째 differential은 injective이다. 만일 그 성분이 전부 $\mathfrak{p}B$에 속한다면 첫 basis vector $g_1$에 대하여 $s g_1\neq 0$이 kernel에 속하게 되어 모순이므로 ([정리 4](#thm4) 직후의 관찰) 어떤 성분은 unit이고, [보조정리 5](#lem5)로 소거하면 rank의 합이 줄어든 exact complex를 얻는다. 위치 $i$에서 수행된 소거의 횟수를 $t_i$라 하면, 최종 상태에서 degree $1$ 이상의 항이 모두 $0$이므로 $1\leq i\leq n$에서 $n_i=t_i+t_{i+1}$ ($t_{n+1}=0$)이고, 이를 풀면 $t_i=r_i$이다. 한편 [보조정리 5](#lem5)의 둘째 결과를 소거마다 추적하면 $I_r(\varphi_i)_\mathfrak{p}$는 $r\leq t_i$에서 $B$와 같고 $r>t_i$에서 최종 상태의 zero map의 소행렬식 ideal이 되어 $0$이다. 곧 임의의 $\mathfrak{p}\in\Ass A$에서

$$I_{r_i}(\varphi_i)_\mathfrak{p}=A_\mathfrak{p},\qquad I_{r_i+1}(\varphi_i)_\mathfrak{p}=0$$

이다.

이로부터 대역적인 결론을 끌어낸다. 만일 $I_{r_i+1}(\varphi_i)\neq 0$이라면 $0$이 아닌 원소 $x\in I_{r_i+1}(\varphi_i)$를 잡을 수 있고, $\Ass(Ax)$는 공집합이 아니며 $\Ass(Ax)\subseteq\Ass A$이므로 ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7), [§동반소아이디얼, ⁋보조정리 5](/ko/math/commutative_algebra/associated_primes#lem5)) $\mathfrak{p}=\ann(bx)\in\Ass A$인 $b$가 존재한다. 그럼 $sx=0$인 $s\notin\mathfrak{p}$가 있다면 $s\in\ann(bx)=\mathfrak{p}$가 되어 모순이므로 $x/1\neq 0$인데, 이는 $I_{r_i+1}(\varphi_i)_\mathfrak{p}=0$에 모순이다. 따라서 $I_{r_i+1}(\varphi_i)=0$이다. 또 $I_{r_i}(\varphi_i)$는 어떠한 $\mathfrak{p}\in\Ass A$에도 포함되지 않으므로 ($I_{r_i}(\varphi_i)\subseteq\mathfrak{p}$라면 localization이 $\mathfrak{p}A_\mathfrak{p}$에 포함되어 $A_\mathfrak{p}$일 수 없다) [§Depth, ⁋보조정리 1](/ko/math/commutative_algebra/depth#lem1)에 의하여 non-zerodivisor를 포함하고, 특히 $0$이 아니다. 종합하면 $\rank\varphi_i=r_i$이므로 rank 등식들이 성립하고, $I(\varphi_i)=I_{r_i}(\varphi_i)$는 non-zerodivisor를 포함하므로 $I(\varphi_i)$가 proper인 경우 그 non-zerodivisor가 길이 $1$의 $A$-sequence가 되어 $\operatorname{grade}I(\varphi_i)\geq 1$이다.

이제 grade 조건을 complex의 길이 $n$에 대한 귀납법으로 보인다. $n=1$이면 필요한 것은 $\operatorname{grade}I(\varphi_1)\geq 1$뿐이므로 이미 끝났다. $n\geq 2$라 하고, 모든 $I(\varphi_i)$가 $A$라면 보일 것이 없으므로 어떤 것은 proper이라 하자. 각각의 $I(\varphi_i)$가 $\Ass A$의 어떤 원소에도 포함되지 않으므로 곱 $I(\varphi_1)\cdots I(\varphi_n)$도 그러하고, $\Ass A$가 유한하므로 ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) [§동반소아이디얼, ⁋보조정리 2](/ko/math/commutative_algebra/associated_primes#lem2)에 의하여 이 곱에는 모든 associated prime을 피하는 원소 $x$가 존재한다. Zerodivisor 전체가 associated prime들의 합집합이므로 ([§동반소아이디얼, ⁋정리 7](/ko/math/commutative_algebra/associated_primes#thm7)) $x$는 non-zerodivisor이고, $x\in I(\varphi_i)$가 모든 $i$에서 성립한다. $\overline{A}=A/(x)$로 두자. 각 $F_j$가 free이고 $x$가 non-zerodivisor이므로 곱하기 $x$는 complex들의 short exact sequence

$$0 \rightarrow F_\bullet\overset{x}{\longrightarrow}F_\bullet \rightarrow F_\bullet/xF_\bullet \rightarrow 0$$

을 주고, [\[호몰로지 대수학\] §긴 완전열, ⁋정리 1](/ko/math/homological_algebra/long_exact_sequence#thm1)의 long exact sequence에서 $2\leq i\leq n$일 때 $H_i(F_\bullet)=0$과 $H_{i-1}(F_\bullet)=0$ 사이에 끼인 $H_i(F_\bullet/xF_\bullet)$는 $0$이다. 그럼 degree $0$의 항을 떼어낸 $\overline{A}$ 위의 finite free complex

$$0 \rightarrow \overline{F}_n\overset{\overline{\varphi}_n}{\longrightarrow}\cdots\overset{\overline{\varphi}_3}{\longrightarrow}\overline{F}_2\overset{\overline{\varphi}_2}{\longrightarrow}\overline{F}_1$$

은 길이가 $n-1$이고 degree $1$ 이상에서 exact이다 (이 절단의 degree $j\geq 1$에서의 homology는 $H_{j+1}(F_\bullet/xF_\bullet)$이다). 귀납적 가정을 적용하면, 절단된 complex의 rank 등식들로부터 $\rank_{\overline{A}}\overline{\varphi}_i=r_i$ ($2\leq i\leq n$, 절단된 complex의 교대합이 원래의 $r_i$와 같으므로)이고, 따라서 $I(\overline{\varphi}_i)=I_{r_i}(\overline{\varphi}_i)=I(\varphi_i)\overline{A}$이며, grade 조건으로부터 $\operatorname{grade}_{\overline{A}}(I(\varphi_i)\overline{A})\geq i-1$이다. $I(\varphi_i)$가 proper인 각각의 $i\geq 2$에서 $x\in I(\varphi_i)$가 non-zerodivisor이므로 [따름정리 8](#cor8)의 셋째 결과로

$$\operatorname{grade}I(\varphi_i)=1+\operatorname{grade}_{\overline{A}}(I(\varphi_i)\overline{A})\geq i$$

를 얻고, $i=1$의 경우는 이미 보였다.

[(2)$\Rightarrow$(1)] 우선 조건 (2)가 임의의 prime $\mathfrak{q}$에서의 localization에서 보존됨을 관찰한다. $I_{r_i+1}(\varphi_i)=0$은 localize되어도 $0$이고, $I_{r_i}(\varphi_i)$는 $A$이거나 (grade 조건에 의하여) non-zerodivisor $y$를 포함하는데 후자의 경우 $sy=0$인 $s\notin\mathfrak{q}$는 있을 수 없어 $y/1\neq 0$이므로, 어느 쪽이든 $I_{r_i}(\varphi_i)_\mathfrak{q}\neq 0$이다. 곧 $\rank_{A_\mathfrak{q}}(\varphi_i)_\mathfrak{q}=r_i$이고 rank 등식들이 유지된다. Grade 조건은 [따름정리 8](#cor8)의 둘째 결과가 준다. 한편 localization이 exact이므로 $H_i(F_\bullet)_\mathfrak{m}\cong H_i((F_\bullet)_\mathfrak{m})$이고, [§국소화의 성질들, ⁋보조정리 3](/ko/math/commutative_algebra/properties_of_localization#lem3)에 의하여 $H_i(F_\bullet)=0$은 모든 maximal ideal $\mathfrak{m}$에서 $H_i((F_\bullet)_\mathfrak{m})=0$인 것과 동치이다. 따라서 $A$가 Noetherian local ring인 경우만 증명하면 충분하다.

이제 $(A,\mathfrak{m})$이 local이라 하고 $\dim A$에 대한 귀납법을 사용한다 ($\dim A$는 [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 유한하다). 어떤 $\varphi_i$가 unit 성분을 갖는 한 [보조정리 5](#lem5)로 소거하자. 소거는 homology를 보존하고, 조건 (2)도 보존한다. 실제로 소거된 $\varphi_i'$는 $I_r(\varphi_i')=I_{r+1}(\varphi_i)$를 만족하므로 $\rank\varphi_i'=r_i-1$이고 $I(\varphi_i')=I_{r_i}(\varphi_i)=I(\varphi_i)$이며, 나머지 map들의 소행렬식 자료는 그대로이므로, 새 complex는 $n_i,n_{i-1}$이 $1$씩 줄어든 rank 등식들과 같은 grade 조건들을 만족한다. 이 소거가 끝난 complex를 $G_\bullet$ (differential $\psi_j$)라 하면 $G_\bullet$은 minimal, 곧 $0$이 아닌 모든 $\psi_j$의 성분이 $\mathfrak{m}$에 속한다.

만일 모든 $j\geq 1$에서 $G_j=0$이라면 $H_j(F_\bullet)\cong H_j(G_\bullet)=0$이므로 끝난다. 아니라면 $G_e\neq 0$인 가장 큰 $e\geq 1$을 잡자. $G_{e+1}=0$이므로 rank 등식에 의하여 $\rank\psi_e$는 free module $G_e$의 rank와 같고, $G_e\neq 0$이라 이 값은 $1$ 이상이다. 특히 $\psi_e\neq 0$이므로 minimality에 의하여 $I(\psi_e)\subseteq I_1(\psi_e)\subseteq\mathfrak{m}$은 proper이다. 그럼 grade 조건과 [정의 6](#def6) 직후의 관찰로

$$e\leq\operatorname{grade}I(\psi_e)\leq\operatorname{depth}A$$

이다. $\dim A=0$인 경우 $\operatorname{depth}A\leq\dim A=0$이므로 ([§Depth, ⁋따름정리 8](/ko/math/commutative_algebra/depth#cor8)) 이 경우는 일어날 수 없고, 앞 문단으로 증명이 끝난다. $\dim A\geq 1$인 경우, maximal이 아닌 임의의 prime $\mathfrak{q}$에 대하여 $\mathfrak{q}$에서 끝나는 prime ideal chain은 $\mathfrak{m}$으로 연장되므로 $\dim A_\mathfrak{q}<\dim A$이고, 조건 (2)가 $(G_\bullet)_\mathfrak{q}$에서 성립하므로 차원에 대한 귀납적 가정에 의하여 $H_j(G_\bullet)_\mathfrak{q}\cong H_j((G_\bullet)_\mathfrak{q})=0$이 모든 $j\geq 1$에서 성립한다. 그럼 $H_j(G_\bullet)\neq 0$인 경우 임의의 $\mathfrak{q}\in\Ass H_j(G_\bullet)$에 대하여 $A/\mathfrak{q}\hookrightarrow H_j(G_\bullet)$을 $\mathfrak{q}$에서 localize하면 $0\neq\kappa(\mathfrak{q})\hookrightarrow H_j(G_\bullet)_\mathfrak{q}$이므로 ([§국소화, ⁋정의 10](/ko/math/commutative_algebra/localization#def10)) $\mathfrak{q}=\mathfrak{m}$일 수밖에 없고, [§Depth, ⁋따름정리 4](/ko/math/commutative_algebra/depth#cor4)에 의하여 $\operatorname{depth}H_j(G_\bullet)=0$이다.

마지막으로 [보조정리 9](#lem9)를 complex $0 \rightarrow G_n \rightarrow\cdots \rightarrow G_1 \rightarrow G_0$에 적용한다. $0$이 아닌 $G_j$는 free module $A^{k_j}$ ($k_j\geq 1$)인데, 원소들 $x_1,\ldots,x_d$가 $A$-sequence인 것과 $A^{k_j}$-sequence인 것은 곱셈의 injectivity와 quotient의 비소멸이 성분별로 판정되므로 동치이고, 따라서 $\operatorname{depth}A^{k_j}=\operatorname{depth}A\geq e\geq j$가 $j\leq e$에서 성립하며 $j>e$에서는 $G_j=0$이라 depth 조건이 공허하게 성립한다. 각 homology는 $0$이거나 depth $0$임을 보였으므로 [보조정리 9](#lem9)에 의하여 모든 $j\geq 1$에서 $H_j(G_\bullet)=0$이고, 곧 $F_\bullet$은 exact이다.
:::

이 정리의 조건 (2)는 온전히 행렬들의 소행렬식으로 표현된다. Rank 등식은 exact complex에서 기대되는 덧셈 관계이고, grade 조건은 rank가 무너지는 자리가 complex의 왼쪽으로 갈수록, 정확히 위치 $i$만큼 깊어야 한다는 요구이다. 조건에 등장하는 ideal이 $A$ 전체가 되는 자리는 grade를 $\infty$로 약속하였으므로 자동으로 통과되는데, 증명에서 본 것처럼 이는 해당 위치에서 complex가 국소적으로 분할되는 상황에 대응한다.

첫 응용으로 regular sequence의 Koszul complex를 판정법에 통과시켜 본다.

::: 따름정리 11
Noetherian ring $A$의 $A$-sequence $x_1,\ldots,x_n$에 대하여, Koszul complex $K(x_1,\ldots,x_n)$은 [정리 10](#thm10)의 조건 (2)를 만족한다. 특히 [§코쥴 복합체, ⁋정리 7](/ko/math/commutative_algebra/koszul_complex#thm7)의 degree $1$ 이상에서의 exactness가 판정법으로 재확인된다.
:::
::: 증명
$K_i=\bigwedge\nolimits^iA^n$은 rank $\binom{n}{i}$의 free module이고, differential $d_i$의 행렬 성분은 [§코쥴 복합체](/ko/math/commutative_algebra/koszul_complex)에서 살펴본 명시적인 식에 의하여 basis $e_J$ ($J$는 $i$개의 원소를 갖는 index 집합)와 $e_K$ ($K$는 $i-1$개) 사이에서 $J=K\cup\{l\}$일 때 $\pm x_l$, 아닐 때 $0$이다. $c_i=\binom{n-1}{i-1}$로 두면 Pascal의 규칙으로 $c_i+c_{i+1}=\binom{n}{i}$이다.

우선 각각의 $j$에 대하여 $x_j^{c_i}\in I_{c_i}(d_i)$임을 본다. 행을 $j\notin K$인 $K$들로, 열을 $j\in J$인 $J$들로 제한하면 대응 $K\mapsto K\cup\{j\}$가 행과 열의 일대일대응을 주고 그 크기는 $c_i$이다. 이 부분행렬에서 대각 성분 $(K,K\cup\{j\})$는 $\pm x_j$이며, 비대각 성분 $(K,J)$는 $e_K$가 $d(e_J)$에 나타나려면 $K=J\setminus\{l\}$이어야 하는데 $j\notin K$와 $j\in J$로부터 $l=j$, 곧 $J=K\cup\{j\}$가 강제되므로 $0$이다. 따라서 이 부분행렬은 대각행렬이고 그 행렬식은 $\pm x_j^{c_i}$이다.

다음으로 $\rank d_i=c_i$임을 본다. 변수들 $t_1,\ldots,t_n$에 대한 polynomial ring $\mathbb{Z}[t_1,\ldots,t_n]$은 Noetherian이고 ([§기본 개념들, ⁋정리 12](/ko/math/commutative_algebra/basic_notions#thm12)) $t_1,\ldots,t_n$은 그 안의 regular sequence이므로 (각 단계의 quotient가 다시 polynomial ring이라 integral domain이다) [§코쥴 복합체, ⁋정리 7](/ko/math/commutative_algebra/koszul_complex#thm7)에 의하여 $K(t_1,\ldots,t_n)$은 degree $1$ 이상에서 exact이다. [정리 10](#thm10)의 (1)$\Rightarrow$(2)의 rank 결론을 위에서부터 풀면 $\rank d_n^{(t)}=\binom{n}{n}=1=c_n$이고 내려오면서 $\rank d_i^{(t)}=\binom{n}{i}-c_{i+1}=c_i$이므로, $d_i^{(t)}$의 모든 $(c_i+1)\times(c_i+1)$ 소행렬식은 $\mathbb{Z}[t]$에서 $0$이다. Ring homomorphism $\mathbb{Z}[t] \rightarrow A$, $t_j\mapsto x_j$가 두 Koszul complex의 행렬들을 대응시키므로 ([§Fitting 아이디얼, ⁋명제 5](/ko/math/commutative_algebra/fitting_ideals#prop5)의 증명) $I_{c_i+1}(d_i)=0$이고, 한편 $x_1$이 non-zerodivisor라 $x_1^{c_i}\neq 0$이므로 $I_{c_i}(d_i)\neq 0$이다. 따라서 $\rank d_i=c_i$이고 rank 등식들이 성립한다.

마지막으로 grade 조건을 본다. $I(d_i)=I_{c_i}(d_i)\subseteq I_1(d_i)\subseteq(x_1,\ldots,x_n)$은 proper이고, $\mathfrak{p}\in V(I(d_i))$이면 $x_j^{c_i}\in\mathfrak{p}$로부터 모든 $x_j$가 $\mathfrak{p}$에 속하므로 $V(I(d_i))\subseteq V((x_1,\ldots,x_n))$이다. 그럼 [보조정리 7](#lem7)에 의하여

$$\operatorname{grade}I(d_i)\geq\operatorname{grade}(x_1,\ldots,x_n)\geq n\geq i$$

이다. 마지막 부등식들은 $x_1,\ldots,x_n$이 $(x_1,\ldots,x_n)$ 안의 길이 $n$의 $A$-sequence라는 것에서 나온다.
:::

## Hilbert-Burch 정리

판정법의 대표적인 응용은 projective dimension이 $2$인 cyclic module의 free resolution이 완전히 결정된다는 것이다. 준비로 기호를 하나 도입한다. $A$-linear map $\varphi:A^{n-1} \rightarrow A^n$이 주어지면, $\varphi$의 행렬에서 $i$번째 행을 지운 $(n-1)\times(n-1)$ 소행렬식을 $\delta_i$라 하고

$$\Delta:A^n \rightarrow A;\qquad \Delta(e_i)=(-1)^{i+1}\delta_i$$

로 정의하자. 그럼 언제나 $\Delta\circ\varphi=0$이다. 실제로 $\varphi$의 $j$번째 열을 $\varphi$의 행렬 오른쪽에 덧붙인 $n\times n$ 행렬은 같은 열을 두 번 가지므로 행렬식이 $0$인데, 이를 덧붙인 열에 대하여 전개하면 $\sum_i(-1)^{i+n}\varphi_{ij}\delta_i=0$이고, 이는 $(\Delta\circ\varphi)(e_j)=\sum_i(-1)^{i+1}\delta_i\varphi_{ij}$의 $(-1)^{n-1}$배이기 때문이다. 또 $\Delta$의 성분들이 생성하는 ideal은 정확히 $I_{n-1}(\varphi)$이다.

::: 정리 12 (Hilbert--Burch)
Noetherian local ring $(A,\mathfrak{m})$과 $0$이 아닌 proper ideal $I$에 대하여, $A/I$가 free resolution

$$0 \rightarrow A^{n-1}\overset{\varphi}{\longrightarrow}A^n\overset{\psi}{\longrightarrow}A \rightarrow A/I \rightarrow 0$$

을 가지며 $\pd_A(A/I)=2$라 하자. 그럼 $A$-regular인 원소 $a$가 존재하여

$$I=a\cdot I_{n-1}(\varphi)$$

이고, $\operatorname{grade}I_{n-1}(\varphi)=2$이다. 거꾸로 $\operatorname{grade}I_{n-1}(\varphi)\geq 2$를 만족하는 임의의 $A$-linear map $\varphi:A^{n-1} \rightarrow A^n$과 $A$-regular 원소 $a$에 대하여, complex

$$0 \rightarrow A^{n-1}\overset{\varphi}{\longrightarrow}A^n\overset{a\Delta}{\longrightarrow}A$$

는 exact이고 $\im(a\Delta)=a\cdot I_{n-1}(\varphi)$이며, 따라서 이는 $A/aI_{n-1}(\varphi)$의 free resolution을 준다.
:::
::: 증명
$J=I_{n-1}(\varphi)$로 적자.

거꾸로의 방향을 먼저 보인다. $\operatorname{grade}J\geq 2$이므로 $J$는 non-zerodivisor $w$를 포함하고, 특히 $J\neq 0$이라 $\rank\varphi=n-1$이며 $I(\varphi)=J$이다. 또 $a$와 $w$가 non-zerodivisor이므로 $aw\neq 0$이고, $a\Delta$의 성분들이 생성하는 ideal은 $aJ\ni aw$라 $0$이 아니므로 $\rank(a\Delta)=1$이고 $I(a\Delta)=aJ$이다. 그럼 rank 등식은 두 위치에서 각각 $(n-1)+0=n-1$과 $1+(n-1)=n$으로 성립하고, grade 조건은 $\operatorname{grade}I(\varphi)=\operatorname{grade}J\geq 2$와, $aw$가 non-zerodivisor들의 곱이라 다시 non-zerodivisor이므로 $\operatorname{grade}(aJ)\geq 1$ (혹은 $aJ=A$)로 성립한다. 따라서 [정리 10](#thm10)에 의하여 complex는 exact이다. $\im(a\Delta)$가 성분들이 생성하는 ideal $aJ$라는 것은 정의에서 바로 나오고, cokernel을 붙이면 $A/aJ$의 free resolution을 얻는다.

이제 정방향을 보인다. 주어진 resolution은 $A^{n-1}$과 $A^n$에서 exact인 finite free complex $0 \rightarrow A^{n-1} \rightarrow A^n \rightarrow A$를 주므로, [정리 10](#thm10)의 (1)$\Rightarrow$(2)에 의하여 $\rank\varphi=n-1$, $\rank\psi=1$이고 $\operatorname{grade}I(\varphi)=\operatorname{grade}J\geq 2$이며, $I(\psi)=I_1(\psi)$는 $\psi$의 성분들이 생성하는 ideal, 곧 $\im\psi=I$이므로 $\operatorname{grade}(I)\geq 1$이다.

$J$가 proper임을 확인한다. 만일 $J=A$라면 [따름정리 3](#cor3)에 의하여 basis를 바꾸어 $\varphi$를 $\id_{A^{n-1}}\oplus(0:A^0 \rightarrow A)$의 꼴로 만들 수 있으므로 $A^n/\im\varphi\cong A$이고, exactness에 의하여 $I=\im\psi\cong A^n/\im\varphi\cong A$가 되어 $I$는 non-zerodivisor 하나로 생성되는 principal ideal이다. 그럼 $0 \rightarrow A \rightarrow A \rightarrow A/I \rightarrow 0$이 free resolution이 되어 $\pd_A(A/I)\leq 1$이고 ([§호몰로지 차원, ⁋정의 1](/ko/math/commutative_algebra/homological_dimension#def1)), 이는 가정 $\pd_A(A/I)=2$에 모순이다.

$\operatorname{grade}J=2$임을 보인다. 거꾸로의 방향을 $a=1$에 적용하면 $0 \rightarrow A^{n-1}\overset{\varphi}{\longrightarrow}A^n\overset{\Delta}{\longrightarrow}A$가 exact이고 $\im\Delta=J$이므로, cokernel을 붙인 $0 \rightarrow A^{n-1} \rightarrow A^n \rightarrow A \rightarrow A/J \rightarrow 0$은 $A/J$의 길이 $2$의 free resolution이고 $\pd_A(A/J)\leq 2$이다. $J$가 proper이므로 $g=\operatorname{grade}J$는 유한하고, [§Depth, ⁋정리 2](/ko/math/commutative_algebra/depth#thm2)에 의하여 $\Ext_A^g(A/J,A)\neq 0$인데, [§호몰로지 차원, ⁋명제 2](/ko/math/commutative_algebra/homological_dimension#prop2)에 의하여 $i>2$에서 $\Ext_A^i(A/J,A)=0$이므로 $g\leq 2$이다. 따라서 $g=2$이다.

이제 두 exact complex를 비교한다. $C=A^n/\im\varphi$로 두면 $\psi\circ\varphi=0$과 $\Delta\circ\varphi=0$으로부터 $\psi$와 $\Delta$는 각각 $A$-linear map $\overline{\psi},\overline{\Delta}:C \rightarrow A$를 유도하고, 두 complex의 $A^n$에서의 exactness는 $\ker\psi=\im\varphi=\ker\Delta$를 말하므로 $\overline{\psi}$와 $\overline{\Delta}$는 injective이며 그 image는 각각 $I$와 $J$이다. 특히 $\overline{\Delta}$는 isomorphism $C\cong J$를 주고, 합성 $\lambda=\overline{\psi}\circ\overline{\Delta}^{-1}:J \rightarrow A$는 $\lambda(J)=I$를 만족하는 $A$-linear map이다.

$\lambda$가 어떤 원소의 곱셈임을 보인다. $\operatorname{grade}J=2$이므로 $J$ 안의 길이 $2$의 $A$-sequence $u,v$가 존재한다. 임의의 $x,y\in J$에 대하여 $xy\in J$이고 $\lambda$가 $A$-linear이므로 $x\lambda(y)=\lambda(xy)=y\lambda(x)$이다. 특히 $v\lambda(u)=u\lambda(v)\in(u)$인데, $v$가 $A/(u)$의 non-zerodivisor이므로 $\lambda(u)\in(u)$, 곧 $\lambda(u)=au$인 $a\in A$가 존재한다. 그럼 임의의 $x\in J$에 대하여 $u\lambda(x)=x\lambda(u)=aux$이고 $u$가 non-zerodivisor이므로 $\lambda(x)=ax$이다.

따라서 $\overline{\psi}=a\overline{\Delta}$이고, canonical surjection $A^n \rightarrow C$와 합성하면 $\psi=a\Delta$이므로

$$I=\im\psi=a\cdot\im\Delta=aJ$$

이다. 마지막으로 $a$가 $A$-regular임을 본다. $\operatorname{grade}(I)\geq 1$이므로 $I$는 non-zerodivisor $w'$를 포함하고, $w'=aj$ ($j\in J$)로 적으면 $ba=0$인 $b$에 대하여 $bw'=baj=0$이므로 $b=0$이다.
:::

이 정리에서 map $\varphi$는 resolution의 <em-ko>마지막</em-ko> 행렬이고, ideal $I$의 generator들은 그 행렬의 maximal 소행렬식들에 공통 인자 $a$를 곱한 것들로 강제된다. 곧 pd $2$의 cyclic module의 resolution은 행렬 하나로 완전히 재구성된다. 거꾸로의 방향은 grade $2$ 조건만 갖추면 어떤 행렬에서 출발하든 이러한 resolution이 실제로 만들어진다는 생성 장치를 준다. 다음 예시에서 이 장치를 돌려본다.

::: 예시 13
Field $\mathbb{K}$에 대하여 $A=\mathbb{K}[[\x,\y,\z]]$와 ideal $I=(\y\z,\x\z,\x\y)$를 생각하자. $V(I)$는 세 좌표축의 합집합이다. [§Depth, ⁋예시 11](/ko/math/commutative_algebra/depth#ex11)에서 본 것처럼 $A$는 차원 $3$의 Noetherian local ring이고, maximal ideal $(\x,\y,\z)$가 정확히 $3$개의 원소로 생성되므로 regular local ring이다. ([§차원, ⁋정의 12](/ko/math/commutative_algebra/Krull_dimension#def12))

$A$-linear map $\varphi:A^2 \rightarrow A^3$을 행렬

$$\varphi=\begin{pmatrix}\x&0\\-\y&\y\\0&-\z\end{pmatrix}$$

로 정의하자. 세 개의 $2\times 2$ 소행렬식은 행 $\{1,2\}$에서 $\x\y$, 행 $\{1,3\}$에서 $-\x\z$, 행 $\{2,3\}$에서 $\y\z$이므로 $I_2(\varphi)=I$이고, $\delta_1=\y\z$, $\delta_2=-\x\z$, $\delta_3=\x\y$이므로

$$\Delta=(\y\z,\ \x\z,\ \x\y)$$

이다. 실제로 $\Delta\circ\varphi=0$은 $\y\z\cdot\x+\x\z\cdot(-\y)=0$과 $\x\z\cdot\y+\x\y\cdot(-\z)=0$으로 직접 확인된다.

$\operatorname{grade}(I)=2$임을 계산한다. $A$는 regular local ring이므로 Cohen--Macaulay이고 ([§Cohen-Macaulay 환, ⁋따름정리 5](/ko/math/commutative_algebra/cohen_macaulay_rings#cor5)), [§Cohen-Macaulay 환, ⁋정리 9](/ko/math/commutative_algebra/cohen_macaulay_rings#thm9)의 첫째 결과에 의하여 임의의 prime $\mathfrak{p}$에서 $A_\mathfrak{p}$도 Cohen--Macaulay이므로 $\operatorname{depth}A_\mathfrak{p}=\dim A_\mathfrak{p}=\codim\mathfrak{p}$이다. ([§차원, ⁋정의 2](/ko/math/commutative_algebra/Krull_dimension#def2)) 따라서 [보조정리 7](#lem7)에 의하여 $\operatorname{grade}(I)$는 $I$를 포함하는 prime들의 codimension의 최솟값이다. $\mathfrak{p}\supseteq I$라 하자. 만일 $\x\notin\mathfrak{p}$라면 $\x\z,\x\y\in\mathfrak{p}$로부터 $\y,\z\in\mathfrak{p}$이므로 $\mathfrak{p}\supseteq(\y,\z)$이고, $\x\in\mathfrak{p}$라면 $\y\z\in\mathfrak{p}$로부터 $\mathfrak{p}\supseteq(\x,\y)$이거나 $\mathfrak{p}\supseteq(\x,\z)$이다. 세 ideal $(\x,\y),(\y,\z),(\x,\z)$는 모두 $I$를 포함하는 prime ideal이며 (가령 $A/(\x,\y)\cong\mathbb{K}[[\z]]$는 integral domain이다), 각각 codimension이 $2$이다. 실제로 $2$개의 원소로 생성되는 자기 자신 위에 minimal하므로 [§차원, ⁋정리 7](/ko/math/commutative_algebra/Krull_dimension#thm7)에 의하여 $\codim\leq 2$이고, prime chain $0\subsetneq(\x)\subsetneq(\x,\y)$가 $\codim(\x,\y)\geq 2$를 준다 ($A/(\x)\cong\mathbb{K}[[\y,\z]]$가 integral domain이라 $(\x)$는 prime이다). 그럼 $I$를 포함하는 임의의 prime은 codimension $2$인 이 셋 중 하나를 포함하므로 $\operatorname{grade}(I)=2$이다.

이제 [정리 12](#thm12)의 거꾸로의 방향을 $\varphi$와 $a=1$에 적용하면, complex

$$0 \rightarrow A^2\overset{\varphi}{\longrightarrow}A^3\overset{\Delta}{\longrightarrow}A \rightarrow A/I \rightarrow 0$$

은 exact이고, 곧 $A/I$의 free resolution이다. [정리 10](#thm10)의 조건이 실제로 어떻게 성립하는지 짚어보면, rank 등식은 $\rank\varphi=2$, $\rank\Delta=1$로부터 $2+0=2$와 $1+2=3$으로 성립하고, grade 조건은 $\operatorname{grade}I(\Delta)=\operatorname{grade}(I)=2\geq 1$과 $\operatorname{grade}I(\varphi)=\operatorname{grade}I_2(\varphi)=\operatorname{grade}(I)=2\geq 2$로 성립한다. 세 좌표축의 합집합을 정의하는 이 ideal은 $2$개의 원소로는 생성될 수 없고 그 관계식들이 $\varphi$의 두 열로 전부 주어지는데, Hilbert--Burch 정리는 이 상황이 $a=1$인 일반적인 현상의 한 사례임을 말해준다.
:::

다음 글부터는 injective module의 구조론과 Matlis duality로 향한다.

---

**참고문헌**

**[BH]** W. Bruns, J. Herzog. *Cohen-Macaulay Rings*. Cambridge University Press, 1993.  
**[Eis]** David Eisenbud. *Commutative Algebra: with a view toward algebraic geometry*. Springer, 1995.  
**[Stacks]** The Stacks Project Authors. *The Stacks Project*. [https://stacks.math.columbia.edu](https://stacks.math.columbia.edu).

---
